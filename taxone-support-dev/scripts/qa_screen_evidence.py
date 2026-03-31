#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
QA Screen Evidence - Captura visual ANTES/DEPOIS em ambiente QA.

Orquestra Playwright E2E e Explorer para:
1. Capturar screenshots das telas afetadas ANTES do deploy (evidencia visual)
2. Deploy do pacote PL/SQL no banco QA
3. Capturar screenshots das mesmas telas DEPOIS do deploy
4. Gerar relatorio HTML comparativo (lado-a-lado ANTES vs DEPOIS)

Uso:
  python qa_screen_evidence.py --wi-id 1071803 --title "TKT163246" --packages "PKG_FPROC" --menu-paths "FEDERAL > PIS COFINS > APURACAO" --env qa
  python qa_screen_evidence.py --wi-id 1071803 --title "TKT" --env qa --antes-only
  python qa_screen_evidence.py --wi-id 1071803 --title "TKT" --env qa --depois-only
  python qa_screen_evidence.py --wi-id 1071803 --title "TKT" --env qa --skip-deploy
"""

import argparse
import base64
import json
import os
import platform
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

# === Configuracao ===
IS_WINDOWS = platform.system() == "Windows"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

# Garantir que scripts/ esta no sys.path para importar modulos irmaos
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

# Arquivos de mapeamento
PLAYWRIGHT_TEST_MAP = PROJECT_ROOT / "knowledge" / "suite-automation" / "playwright-test-map.json"
SCREEN_NAV_MAP = PROJECT_ROOT / "knowledge" / "suite-automation" / "screen-navigation-map.json"

# Timeouts
EXPLORER_TIMEOUT = 120  # segundos por tela
DEPLOY_TIMEOUT = 300    # 5 min para deploy


# ============================================================
# 1. RESOLUCAO DE TELAS
# ============================================================

def load_playwright_test_map():
    """Carrega playwright-test-map.json com scoring config."""
    if not PLAYWRIGHT_TEST_MAP.exists():
        print(f"  AVISO: {PLAYWRIGHT_TEST_MAP} nao encontrado", file=sys.stderr)
        return {"scoring": {}, "mappings": []}
    return json.loads(PLAYWRIGHT_TEST_MAP.read_text(encoding="utf-8"))


def load_screen_nav_map():
    """Carrega screen-navigation-map.json para explorer fallback."""
    if not SCREEN_NAV_MAP.exists():
        print(f"  AVISO: {SCREEN_NAV_MAP} nao encontrado", file=sys.stderr)
        return {"default_config": {}, "navigation_configs": {}}
    return json.loads(SCREEN_NAV_MAP.read_text(encoding="utf-8"))


def resolve_screens(wi_title, packages, menu_paths, modified_files=None):
    """Detecta quais telas capturar baseado nos dados da WI.

    Returns:
        dict com:
          playwright_screens: lista de mappings com spec_files
          explorer_screens: lista de menu_paths para captura via explorer
          resolved_log: log de resolucao (para resolved_screens.json)
    """
    test_map = load_playwright_test_map()
    scoring = test_map.get("scoring", {})
    mappings = test_map.get("mappings", [])
    modified_files = modified_files or []

    menu_path_weight = scoring.get("menu_path_match", 7)
    screen_kw_weight = scoring.get("screen_keyword_match", 5)
    keyword_weight = scoring.get("keyword_match", 3)
    file_path_weight = scoring.get("file_path_match", 5)
    package_weight = scoring.get("package_match", 4)
    min_score = scoring.get("min_score_to_include", 3)
    max_specs = scoring.get("max_specs", 5)

    title_upper = wi_title.upper() if wi_title else ""
    pkg_list = [p.strip().upper() for p in packages if p.strip()]
    menu_list = [m.strip().upper() for m in menu_paths if m.strip()]

    scored = []
    resolved_log = []

    for m in mappings:
        score = 0
        reasons = []

        # menu_path match
        m_menu = (m.get("menu_path") or "").upper()
        if m_menu and any(mp in m_menu or m_menu in mp for mp in menu_list):
            score += menu_path_weight
            reasons.append(f"menu_path({menu_path_weight})")

        # screen_keywords match
        for kw in m.get("screen_keywords", []):
            if kw.upper() in title_upper:
                score += screen_kw_weight
                reasons.append(f"screen_kw({screen_kw_weight}): {kw}")
                break

        # packages match
        for pkg in m.get("packages", []):
            if pkg.upper() in pkg_list:
                score += package_weight
                reasons.append(f"package({package_weight}): {pkg}")
                break

        # file_paths match
        for fp in m.get("file_paths", []):
            if any(fp.lower() in mf.lower() for mf in modified_files):
                score += file_path_weight
                reasons.append(f"file_path({file_path_weight}): {fp}")
                break

        # keywords match
        for kw in m.get("keywords", []):
            if kw.upper() in title_upper:
                score += keyword_weight
                reasons.append(f"keyword({keyword_weight}): {kw}")
                break

        if score >= min_score:
            scored.append((score, m, reasons))

    scored.sort(key=lambda x: -x[0])
    playwright_screens = []
    # Para screen evidence, pegar apenas o top-1 mapping (mais relevante)
    # O max_specs do JSON (default 5) e para test suites completas
    effective_max = min(max_specs, 1)
    for score, m, reasons in scored[:effective_max]:
        playwright_screens.append(m)
        resolved_log.append({
            "id": m["id"],
            "score": score,
            "reasons": reasons,
            "method": "playwright",
            "spec_files": m.get("spec_files", []),
        })

    # Explorer complementar: menu_paths que nao foram cobertas por Playwright
    covered_menus = set()
    for m in playwright_screens:
        covered_menus.add((m.get("menu_path") or "").upper())

    explorer_screens = []
    for mp in menu_list:
        already_covered = any(mp in cm or cm in mp for cm in covered_menus)
        if not already_covered:
            explorer_screens.append(mp)
            resolved_log.append({
                "menu_path": mp,
                "method": "explorer",
                "reason": "Nao coberto por Playwright specs",
            })

    return {
        "playwright_screens": playwright_screens,
        "explorer_screens": explorer_screens,
        "resolved_log": resolved_log,
    }


# ============================================================
# 2. CAPTURA VIA PLAYWRIGHT
# ============================================================

def capture_via_playwright(screens, env, target_dir):
    """Roda specs Playwright com screenshot=on e coleta os PNGs.

    Returns:
        dict com status, screenshots_count, specs_run, errors
    """
    try:
        from playwright_runner import (
            run_playwright, _clean_test_results, _collect_screenshots,
            check_prerequisites, sync_repo
        )
    except ImportError as e:
        return {
            "status": "SKIP",
            "message": f"playwright_runner nao importavel: {e}",
            "screenshots_count": 0,
            "errors": [str(e)],
        }

    # Verificar prereqs
    prereq_errors = check_prerequisites()
    if prereq_errors:
        return {
            "status": "SKIP",
            "message": "Playwright prereqs ausentes",
            "screenshots_count": 0,
            "errors": prereq_errors,
        }

    # Sincronizar repo
    try:
        sync_repo()
    except Exception as e:
        print(f"  AVISO: sync_repo falhou ({e}), continuando...", file=sys.stderr)

    # Coletar apenas o primeiro spec file do mapping mais relevante
    # (para screen evidence, 1 spec e suficiente - nao precisa rodar a suite inteira)
    all_specs = []
    for screen in screens:
        specs = screen.get("spec_files", [])
        if specs and specs[0] not in all_specs:
            all_specs.append(specs[0])
            break  # apenas 1 spec total

    if not all_specs:
        return {
            "status": "SKIP",
            "message": "Nenhum spec file para executar",
            "screenshots_count": 0,
            "errors": [],
        }

    # Limpar screenshots anteriores
    _clean_test_results()

    # Executar com workers=1 para screenshots deterministicos
    print(f"  Playwright: executando {len(all_specs)} spec(s) com screenshot=on...", file=sys.stderr)
    result = run_playwright(
        specs=all_specs,
        env=env,
        workers=1,
        screenshot="on",
        timeout=180,  # 3min max por spec (screen evidence, nao suite completa)
    )

    # Coletar screenshots
    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    count = _collect_screenshots(str(target))

    return {
        "status": result.get("status", "ERROR"),
        "screenshots_count": count,
        "specs_run": all_specs,
        "duration_s": result.get("duration_s", 0),
        "errors": [] if result.get("status") != "ERROR" else [result.get("message", "")],
    }


# ============================================================
# 3. CAPTURA VIA EXPLORER
# ============================================================

def capture_via_explorer(menu_paths, env, target_dir):
    """Navega telas via explorer_runner e captura screenshots.

    Returns:
        dict com status, screenshots_count, screens_captured, errors
    """
    nav_map = load_screen_nav_map()
    default_cfg = nav_map.get("default_config", {})
    nav_configs = nav_map.get("navigation_configs", {})

    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)

    results = {
        "status": "PASS",
        "screenshots_count": 0,
        "screens_captured": [],
        "errors": [],
    }

    if not menu_paths:
        results["status"] = "SKIP"
        results["message"] = "Nenhum menu_path para explorer"
        return results

    # Construir sequencia JSONL de comandos
    commands = []

    # Login com config default
    login_cmd = {
        "action": "login",
        "empresa": default_cfg.get("empresa", "076 - DEMOSTRACAO TSL - TECNOLOGIA EM SISTEMAS DE LEGISLACAO S/A"),
    }

    for mp in menu_paths:
        mp_upper = mp.upper().strip()
        # Encontrar config de navegacao mais especifica (prefixo mais longo)
        best_match = None
        best_len = 0
        for nav_key, nav_cfg in nav_configs.items():
            nav_upper = nav_key.upper()
            if mp_upper.startswith(nav_upper) and len(nav_upper) > best_len:
                best_match = nav_cfg
                best_len = len(nav_upper)

        # Sanitizar menu_path para nome de arquivo
        safe_name = mp_upper.replace(" > ", "_").replace(" ", "_").replace("/", "_")
        screenshot_path = str(target / f"EXPLORER_{safe_name}.png")

        # Adicionar agrupamento/modulo se encontrado
        if best_match:
            login_with_module = dict(login_cmd)
            if best_match.get("agrupamento"):
                login_with_module["agrupamento"] = best_match["agrupamento"]
            if best_match.get("modulo"):
                login_with_module["modulo"] = best_match["modulo"]
            commands.append(login_with_module)
        else:
            commands.append(login_cmd)

        # Navegar
        commands.append({"action": "navigate", "menuPath": mp})
        # Screenshot
        commands.append({"action": "screenshot", "output": screenshot_path})

        results["screens_captured"].append({
            "menu_path": mp,
            "screenshot": screenshot_path,
        })

    # Quit
    commands.append({"action": "quit"})

    # Executar via multi mode (piped JSONL)
    jsonl_input = "\n".join(json.dumps(cmd, ensure_ascii=False) for cmd in commands)

    explorer_script = str(SCRIPTS_DIR / "explorer_runner.py")
    try:
        proc = subprocess.run(
            [sys.executable, explorer_script, "multi"],
            input=jsonl_input,
            capture_output=True,
            text=True,
            timeout=EXPLORER_TIMEOUT * len(menu_paths) + 60,
            cwd=str(PROJECT_ROOT),
            encoding="utf-8",
            errors="replace",
        )

        # Contar screenshots realmente salvos
        for sc in results["screens_captured"]:
            if Path(sc["screenshot"]).exists():
                results["screenshots_count"] += 1
            else:
                results["errors"].append(f"Screenshot nao gerado: {sc['screenshot']}")

        if proc.returncode != 0:
            results["errors"].append(f"Explorer retornou codigo {proc.returncode}")
            if results["screenshots_count"] == 0:
                results["status"] = "ERROR"

    except subprocess.TimeoutExpired:
        results["status"] = "ERROR"
        results["errors"].append(f"Explorer timeout ({EXPLORER_TIMEOUT * len(menu_paths)}s)")
    except Exception as e:
        results["status"] = "ERROR"
        results["errors"].append(str(e))

    return results


# ============================================================
# 4. CAPTURA COMBINADA (PARALELO)
# ============================================================

def capture_screens(wi_id, phase, env, playwright_screens, explorer_screens, base_dir):
    """Captura screenshots via Playwright + Explorer em paralelo.

    Args:
        phase: "antes" ou "depois"
    Returns:
        dict com playwright_result, explorer_result, total_screenshots
    """
    target_dir = Path(base_dir) / phase
    # Limpar screenshots anteriores desta fase
    if target_dir.exists():
        for old_png in target_dir.glob("*.png"):
            old_png.unlink()
    target_dir.mkdir(parents=True, exist_ok=True)

    pw_result = {"status": "SKIP", "screenshots_count": 0, "errors": []}
    exp_result = {"status": "SKIP", "screenshots_count": 0, "errors": []}

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {}

        if playwright_screens:
            futures["playwright"] = executor.submit(
                capture_via_playwright, playwright_screens, env, str(target_dir)
            )

        if explorer_screens:
            futures["explorer"] = executor.submit(
                capture_via_explorer, explorer_screens, env, str(target_dir)
            )

        for key, future in futures.items():
            try:
                result = future.result(timeout=600)
                if key == "playwright":
                    pw_result = result
                else:
                    exp_result = result
            except Exception as e:
                err = {"status": "ERROR", "screenshots_count": 0, "errors": [str(e)]}
                if key == "playwright":
                    pw_result = err
                else:
                    exp_result = err

    total = pw_result.get("screenshots_count", 0) + exp_result.get("screenshots_count", 0)
    print(f"  [{phase.upper()}] Total: {total} screenshot(s) "
          f"(PW: {pw_result.get('screenshots_count', 0)}, "
          f"EXP: {exp_result.get('screenshots_count', 0)})", file=sys.stderr)

    return {
        "playwright": pw_result,
        "explorer": exp_result,
        "total_screenshots": total,
    }


# ============================================================
# 5. DEPLOY QA
# ============================================================

def deploy_qa(wi_id, env="QA"):
    """Compila PL/SQL no banco QA via qa_object_deployer.

    Returns:
        dict com status, message, duration_s
    """
    deployer_script = SCRIPTS_DIR / "qa_object_deployer.py"
    if not deployer_script.exists():
        return {
            "status": "SKIP",
            "message": f"qa_object_deployer.py nao encontrado em {SCRIPTS_DIR}",
            "duration_s": 0,
        }

    start = time.time()
    try:
        result = subprocess.run(
            [sys.executable, str(deployer_script), "--wi-id", str(wi_id), "--env", env],
            capture_output=True,
            text=True,
            timeout=DEPLOY_TIMEOUT,
            cwd=str(PROJECT_ROOT),
            encoding="utf-8",
            errors="replace",
        )
        duration = time.time() - start

        if result.returncode == 0:
            return {"status": "PASS", "message": "Deploy OK", "duration_s": round(duration, 1)}
        else:
            return {
                "status": "FAIL",
                "message": f"Deploy falhou (code {result.returncode}): {result.stderr[:500]}",
                "duration_s": round(duration, 1),
            }
    except subprocess.TimeoutExpired:
        return {"status": "ERROR", "message": f"Deploy timeout ({DEPLOY_TIMEOUT}s)", "duration_s": DEPLOY_TIMEOUT}
    except Exception as e:
        return {"status": "ERROR", "message": str(e), "duration_s": round(time.time() - start, 1)}


# ============================================================
# 6. COMPARACAO DE SCREENSHOTS
# ============================================================

def compare_screenshots(antes_dir, depois_dir, diff_dir):
    """Compara screenshots ANTES vs DEPOIS pixel-a-pixel.

    Returns:
        lista de dicts com antes, depois, diff_pct, identical, diff_path
    """
    antes = Path(antes_dir)
    depois = Path(depois_dir)
    diff = Path(diff_dir)
    diff.mkdir(parents=True, exist_ok=True)

    comparisons = []

    # Match por nome de arquivo
    antes_files = {f.name: f for f in antes.glob("*.png")}
    depois_files = {f.name: f for f in depois.glob("*.png")}

    matched = set(antes_files.keys()) & set(depois_files.keys())

    # Arquivos somente em ANTES
    for name in sorted(set(antes_files.keys()) - matched):
        comparisons.append({
            "name": name,
            "antes": str(antes_files[name]),
            "depois": None,
            "diff_pct": 100.0,
            "identical": False,
            "status": "REMOVED",
            "diff_path": None,
        })

    # Arquivos somente em DEPOIS
    for name in sorted(set(depois_files.keys()) - matched):
        comparisons.append({
            "name": name,
            "antes": None,
            "depois": str(depois_files[name]),
            "diff_pct": 100.0,
            "identical": False,
            "status": "ADDED",
            "diff_path": None,
        })

    # Arquivos em ambos - diff visual
    try:
        from PIL import Image, ImageChops
        has_pillow = True
    except ImportError:
        has_pillow = False
        print("  AVISO: Pillow nao instalado - diff visual desabilitado. "
              "Instale com: pip install Pillow", file=sys.stderr)

    for name in sorted(matched):
        comp = {
            "name": name,
            "antes": str(antes_files[name]),
            "depois": str(depois_files[name]),
            "diff_pct": 0.0,
            "identical": True,
            "status": "IDENTICAL",
            "diff_path": None,
        }

        if has_pillow:
            try:
                img_a = Image.open(antes_files[name]).convert("RGB")
                img_b = Image.open(depois_files[name]).convert("RGB")

                # Redimensionar se tamanhos diferentes
                if img_a.size != img_b.size:
                    img_b = img_b.resize(img_a.size, Image.LANCZOS)

                diff_img = ImageChops.difference(img_a, img_b)
                pixels = list(diff_img.getdata())
                total = len(pixels)
                changed = sum(1 for p in pixels if sum(p) > 30)
                diff_pct = (changed / total) * 100 if total > 0 else 0

                comp["diff_pct"] = round(diff_pct, 2)
                comp["identical"] = diff_pct < 0.5
                comp["status"] = "IDENTICAL" if comp["identical"] else "CHANGED"

                # Salvar diff amplificado
                if not comp["identical"]:
                    diff_amplified = diff_img.point(lambda x: min(x * 5, 255))
                    diff_path = diff / f"{Path(name).stem}_diff.png"
                    diff_amplified.save(str(diff_path))
                    comp["diff_path"] = str(diff_path)

            except Exception as e:
                comp["status"] = "ERROR"
                comp["diff_pct"] = -1
                comp["identical"] = False
                print(f"  AVISO: Erro ao comparar {name}: {e}", file=sys.stderr)
        else:
            # Sem Pillow: comparacao por tamanho de arquivo
            size_a = antes_files[name].stat().st_size
            size_b = depois_files[name].stat().st_size
            comp["identical"] = size_a == size_b
            comp["status"] = "IDENTICAL" if comp["identical"] else "CHANGED (size)"

        comparisons.append(comp)

    return comparisons


# ============================================================
# 7. RELATORIO HTML
# ============================================================

def _img_to_base64(path):
    """Converte imagem para base64 data URI."""
    if not path or not Path(path).exists():
        return ""
    data = Path(path).read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/png;base64,{b64}"


def generate_html_report(wi_id, env, comparisons, timestamps, target_path):
    """Gera relatorio HTML self-contained com imagens base64."""
    n_changed = sum(1 for c in comparisons if c["status"] == "CHANGED")
    n_identical = sum(1 for c in comparisons if c["status"] == "IDENTICAL")
    n_errors = sum(1 for c in comparisons if c["status"] in ("ERROR", "REMOVED", "ADDED"))

    if n_changed == 0 and n_errors == 0:
        verdict_color = "#27ae60"
    elif n_errors == 0:
        verdict_color = "#e67e22"
    else:
        verdict_color = "#e74c3c"

    rows_html = ""
    details_html = ""

    for comp in comparisons:
        name = comp["name"]
        status = comp["status"]
        diff_pct = comp.get("diff_pct", "-")

        # Status badge
        badge_colors = {
            "IDENTICAL": ("#27ae60", "IDENTICAL"),
            "CHANGED": ("#e67e22", "CHANGED"),
            "CHANGED (size)": ("#e67e22", "CHANGED"),
            "ADDED": ("#3498db", "ADDED"),
            "REMOVED": ("#e74c3c", "REMOVED"),
            "ERROR": ("#e74c3c", "ERROR"),
        }
        bg, label = badge_colors.get(status, ("#95a5a6", status))
        badge = f'<span style="background:{bg};color:#fff;padding:2px 8px;border-radius:4px;">{label}</span>'

        rows_html += f"""
        <tr>
            <td>{name}</td>
            <td>{diff_pct}%</td>
            <td style="text-align:center">{badge}</td>
        </tr>"""

        # Detalhes lado-a-lado
        antes_b64 = _img_to_base64(comp.get("antes"))
        depois_b64 = _img_to_base64(comp.get("depois"))
        diff_b64 = _img_to_base64(comp.get("diff_path"))

        antes_img = f'<img src="{antes_b64}" style="max-width:100%">' if antes_b64 else "<p>Nao disponivel</p>"
        depois_img = f'<img src="{depois_b64}" style="max-width:100%">' if depois_b64 else "<p>Nao disponivel</p>"

        diff_section = ""
        if diff_b64:
            diff_section = f"""
            <div style="margin-top:10px;">
                <h4>DIFF ({diff_pct}%)</h4>
                <img src="{diff_b64}" style="max-width:100%">
            </div>"""

        details_html += f"""
        <div style="margin-top:30px; border-top:2px solid #ecf0f1; padding-top:15px;">
            <h3>{name} - {badge}</h3>
            <div style="display:flex; gap:20px;">
                <div style="flex:1;">
                    <h4>ANTES</h4>
                    {antes_img}
                </div>
                <div style="flex:1;">
                    <h4>DEPOIS</h4>
                    {depois_img}
                </div>
            </div>
            {diff_section}
        </div>"""

    ts_antes = timestamps.get("antes", "-")
    ts_deploy = timestamps.get("deploy", "-")
    ts_depois = timestamps.get("depois", "-")

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Evidencia Visual ANTES vs DEPOIS - WI #{wi_id}</title>
<style>
body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 20px; background: #f5f6fa; }}
.container {{ max-width: 1200px; margin: 0 auto; }}
h1 {{ color: #2c3e50; border-bottom: 3px solid #27ae60; padding-bottom: 10px; }}
h2 {{ color: #34495e; margin-top: 30px; }}
h3 {{ color: #2c3e50; }}
h4 {{ color: #7f8c8d; margin-bottom: 5px; }}
table {{ border-collapse: collapse; width: 100%; margin: 15px 0; background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
th {{ background: #34495e; color: #fff; padding: 10px 12px; text-align: left; }}
td {{ padding: 8px 12px; border-bottom: 1px solid #ecf0f1; }}
tr:hover {{ background: #f8f9fa; }}
.verdict {{ font-size: 24px; font-weight: bold; color: {verdict_color}; padding: 15px; background: #fff; border-left: 5px solid {verdict_color}; margin: 20px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
.meta {{ color: #7f8c8d; font-size: 0.9em; }}
</style>
</head>
<body>
<div class="container">

<h1>Evidencia Visual ANTES vs DEPOIS - WI #{wi_id}</h1>
<p class="meta">
  Ambiente: <b>{env.upper()}</b> |
  ANTES: {ts_antes} |
  Deploy: {ts_deploy} |
  DEPOIS: {ts_depois} |
  Gerado: {datetime.now().isoformat()}
</p>

<div class="verdict">Resultado: {n_changed} tela(s) com alteracao, {n_identical} sem alteracao, {n_errors} erro(s)</div>

<h2>Resumo</h2>
<table>
<tr><th>Tela</th><th>Diff %</th><th>Status</th></tr>
{rows_html}
</table>

<h2>Detalhes</h2>
{details_html}

</div>
</body>
</html>"""

    Path(target_path).write_text(html, encoding="utf-8")
    print(f"  Relatorio HTML gerado: {target_path}", file=sys.stderr)
    return str(target_path)


# ============================================================
# 8. MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="QA Screen Evidence - Captura visual ANTES/DEPOIS em QA"
    )
    parser.add_argument("--wi-id", required=True, help="ID da Work Item")
    parser.add_argument("--title", required=True, help="Titulo da WI (usado para matching)")
    parser.add_argument("--packages", default="", help="Pacotes PL/SQL afetados (virgula-separados)")
    parser.add_argument("--menu-paths", default="", help="Menu paths afetados (pipe-separados, ex: 'FEDERAL > PIS|SPED > EFD')")
    parser.add_argument("--modified-files", default="", help="Arquivos modificados (virgula-separados)")
    parser.add_argument("--env", default="qa", help="Ambiente (qa, sat, uat)")
    parser.add_argument("--antes-only", action="store_true", help="Somente captura ANTES (pre-deploy)")
    parser.add_argument("--depois-only", action="store_true", help="Somente captura DEPOIS (deploy ja feito)")
    parser.add_argument("--skip-deploy", action="store_true", help="Pula etapa de deploy")
    parser.add_argument("--spec", default="", help="Spec files explicitamente (virgula-separados)")
    parser.add_argument("--no-playwright", action="store_true", help="Desabilita Playwright, usa somente Explorer")
    parser.add_argument("--output", default="", help="Path do JSON summary output")

    args = parser.parse_args()

    wi_id = args.wi_id
    env = args.env
    packages = [p.strip() for p in args.packages.split(",") if p.strip()]
    menu_paths = [m.strip() for m in args.menu_paths.split("|") if m.strip()]
    modified_files = [f.strip() for f in args.modified_files.split(",") if f.strip()]

    # Diretorio base para evidencias
    base_dir = PROJECT_ROOT / "tests" / wi_id / "qa_screens"
    base_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"  QA Screen Evidence - WI #{wi_id}", file=sys.stderr)
    print(f"  Ambiente: {env}", file=sys.stderr)
    print(f"{'='*60}\n", file=sys.stderr)

    # === FASE 1: Resolver telas ===
    print("[1/5] Resolvendo telas a capturar...", file=sys.stderr)

    # Override manual via --spec
    if args.spec:
        spec_list = [s.strip() for s in args.spec.split(",") if s.strip()]
        resolved = {
            "playwright_screens": [{"id": "MANUAL", "spec_files": spec_list}],
            "explorer_screens": [],
            "resolved_log": [{"id": "MANUAL", "method": "playwright", "spec_files": spec_list}],
        }
    else:
        resolved = resolve_screens(args.title, packages, menu_paths, modified_files)

    pw_screens = resolved["playwright_screens"]
    exp_screens = resolved["explorer_screens"]

    # --no-playwright: mover telas Playwright para Explorer (usando menu_paths)
    if args.no_playwright and pw_screens:
        for pw in pw_screens:
            mp = (pw.get("menu_path") or "").upper()
            if mp and mp not in [e.upper() for e in exp_screens]:
                exp_screens.append(mp)
        pw_screens = []
        # Se nenhum menu_path dos PW, forcar os do --menu-paths
        if not exp_screens and menu_paths:
            exp_screens = [m.strip().upper() for m in menu_paths if m.strip()]

    total_screens = len(pw_screens) + len(exp_screens)
    print(f"  Playwright: {len(pw_screens)} mapping(s), Explorer: {len(exp_screens)} tela(s)", file=sys.stderr)

    if total_screens == 0:
        summary = {
            "wi_id": wi_id,
            "env": env,
            "status": "SKIP",
            "message": "Nenhuma tela resolvida para esta WI",
            "total_screens": 0,
        }
        (base_dir / "resolved_screens.json").write_text(
            json.dumps(resolved["resolved_log"], indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        sys.exit(0)

    # Salvar log de resolucao
    (base_dir / "resolved_screens.json").write_text(
        json.dumps(resolved["resolved_log"], indent=2, ensure_ascii=False), encoding="utf-8"
    )

    timestamps = {}

    # === FASE 2: Captura ANTES ===
    antes_result = None
    if not args.depois_only:
        print("\n[2/5] Capturando screenshots ANTES...", file=sys.stderr)
        timestamps["antes"] = datetime.now().isoformat()
        antes_result = capture_screens(wi_id, "antes", env, pw_screens, exp_screens, base_dir)
    else:
        print("\n[2/5] ANTES pulado (--depois-only)", file=sys.stderr)

    # === FASE 3: Deploy ===
    deploy_result = None
    if not args.antes_only and not args.depois_only and not args.skip_deploy:
        print("\n[3/5] Deploy no banco QA...", file=sys.stderr)
        timestamps["deploy"] = datetime.now().isoformat()
        deploy_result = deploy_qa(wi_id, env.upper())
        print(f"  Deploy: {deploy_result['status']} ({deploy_result.get('duration_s', 0)}s)", file=sys.stderr)

        if deploy_result["status"] not in ("PASS", "SKIP"):
            print(f"  ERRO: Deploy falhou - {deploy_result['message']}", file=sys.stderr)
            print("  Abortando captura DEPOIS. Resultado parcial (ANTES only).", file=sys.stderr)
            summary = {
                "wi_id": wi_id,
                "env": env,
                "status": "PARTIAL",
                "message": f"Deploy falhou: {deploy_result['message']}",
                "timestamps": timestamps,
                "antes": antes_result,
                "deploy": deploy_result,
            }
            output_path = args.output or str(base_dir / "screen_evidence_summary.json")
            Path(output_path).write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
            print(json.dumps(summary, indent=2, ensure_ascii=False))
            sys.exit(1)
    else:
        reason = "--antes-only" if args.antes_only else "--skip-deploy" if args.skip_deploy else "--depois-only"
        print(f"\n[3/5] Deploy pulado ({reason})", file=sys.stderr)

    # === FASE 4: Captura DEPOIS ===
    depois_result = None
    if not args.antes_only:
        print("\n[4/5] Capturando screenshots DEPOIS...", file=sys.stderr)
        timestamps["depois"] = datetime.now().isoformat()
        depois_result = capture_screens(wi_id, "depois", env, pw_screens, exp_screens, base_dir)
    else:
        print("\n[4/5] DEPOIS pulado (--antes-only)", file=sys.stderr)

    # === FASE 5: Comparacao e Relatorio ===
    comparisons = []
    antes_dir = base_dir / "antes"
    depois_dir = base_dir / "depois"
    diff_dir = base_dir / "diff"

    if antes_dir.exists() and depois_dir.exists():
        print("\n[5/5] Comparando screenshots e gerando relatorio...", file=sys.stderr)
        comparisons = compare_screenshots(str(antes_dir), str(depois_dir), str(diff_dir))

        # Gerar HTML
        report_path = str(base_dir / "screen_evidence_report.html")
        generate_html_report(wi_id, env, comparisons, timestamps, report_path)
    else:
        print("\n[5/5] Comparacao pulada (ANTES ou DEPOIS indisponivel)", file=sys.stderr)

    # === Summary JSON ===
    n_changed = sum(1 for c in comparisons if c.get("status") == "CHANGED")
    n_identical = sum(1 for c in comparisons if c.get("status") == "IDENTICAL")
    n_errors = sum(1 for c in comparisons if c.get("status") in ("ERROR", "REMOVED", "ADDED"))

    summary = {
        "wi_id": wi_id,
        "env": env,
        "status": "PASS" if n_errors == 0 else "PARTIAL",
        "timestamps": timestamps,
        "screens_resolved": total_screens,
        "antes": {
            "total_screenshots": antes_result["total_screenshots"],
        } if antes_result else None,
        "deploy": deploy_result,
        "depois": {
            "total_screenshots": depois_result["total_screenshots"],
        } if depois_result else None,
        "comparison": {
            "total": len(comparisons),
            "changed": n_changed,
            "identical": n_identical,
            "errors": n_errors,
        } if comparisons else None,
        "report_html": str(base_dir / "screen_evidence_report.html") if comparisons else None,
    }

    output_path = args.output or str(base_dir / "screen_evidence_summary.json")
    Path(output_path).write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    # Stdout: JSON summary (machine-readable)
    print(json.dumps(summary, indent=2, ensure_ascii=False))

    # Exit code
    all_errors = []
    if antes_result:
        all_errors.extend(antes_result.get("playwright", {}).get("errors", []))
        all_errors.extend(antes_result.get("explorer", {}).get("errors", []))
    if depois_result:
        all_errors.extend(depois_result.get("playwright", {}).get("errors", []))
        all_errors.extend(depois_result.get("explorer", {}).get("errors", []))

    if all_errors:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
