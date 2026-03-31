#!/usr/bin/env python3
"""
rum_to_e2e.py — Bridge RUM user journey → Playwright E2E specs.

Reads RUM enrichment data (DD_RUM_USER_JOURNEY), matches against
playwright-test-map.json scoring, generates ephemeral Playwright spec
from the real user journey, and optionally executes via playwright_runner.py.

Modes:
  python rum_to_e2e.py --wi-id 1066293 --match-only     # apenas identificar specs
  python rum_to_e2e.py --wi-id 1066293 --dry-run         # match + gerar spec (sem executar)
  python rum_to_e2e.py --wi-id 1066293 --env qa          # match + gerar spec + executar
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = PROJECT_ROOT / "tests"
PLAYWRIGHT_MAP_PATH = PROJECT_ROOT / "knowledge" / "suite-automation" / "playwright-test-map.json"
PLAYWRIGHT_RUNNER = PROJECT_ROOT / "scripts" / "playwright_runner.py"

# URL fragments → normalized keywords for matching
URL_KEYWORD_MAP = {
    "imp": "IMPORTACAO",
    "importa": "IMPORTACAO",
    "export": "EXPORTACAO",
    "job": "JOB SERVIDOR",
    "agend": "AGENDAMENTO",
    "manut": "MANUTENCAO",
    "param": "PARAMETROS",
    "relat": "RELATORIOS",
    "gera": "GERACAO",
    "apura": "APURACAO",
    "escrit": "ESCRITURACAO",
    "contrib": "CONTRIBUICOES",
    "fiscal": "FISCAL",
    "ecd": "ECD",
    "reinf": "REINF",
    "icms": "ICMS",
    "iss": "ISS",
    "ipi": "IPI",
    "pis": "PIS",
    "cofins": "COFINS",
    "cred": "CREDITO",
    "gia": "GIA",
    "dime": "DIME",
    "sped": "SPED",
    "nfts": "NFTS",
    "dw": "DATA WAREHOUSE",
    "datamart": "DATAMART",
    "ferramenta": "FERRAMENTAS",
    "obrigac": "OBRIGACOES",
    "fci": "FCI",
}


def load_rum_enrichment(wi_id: str) -> dict:
    """Load rum_enrichment_{wi_id}.json from tests/{wi_id}/."""
    rum_path = TESTS_DIR / wi_id / f"rum_enrichment_{wi_id}.json"
    if not rum_path.exists():
        print(f"ERRO: {rum_path} nao encontrado.", file=sys.stderr)
        print("Execute rum_enricher.py primeiro para gerar o enrichment.", file=sys.stderr)
        sys.exit(1)

    with open(rum_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_playwright_map() -> dict:
    """Load playwright-test-map.json."""
    if not PLAYWRIGHT_MAP_PATH.exists():
        print(f"ERRO: {PLAYWRIGHT_MAP_PATH} nao encontrado.", file=sys.stderr)
        sys.exit(1)

    with open(PLAYWRIGHT_MAP_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_search_terms(journey: dict) -> dict:
    """Extract normalized search terms from DD_RUM_USER_JOURNEY."""
    keywords = set()

    # 1. Module name → keywords
    module = (journey.get("module") or "").upper()
    if module:
        keywords.add(module)
        for word in module.split():
            keywords.add(word)

    # 2. Menu path → keywords
    menu_path = journey.get("menu_path") or ""
    menu_path_normalized = ""
    if menu_path:
        # "Importação > Importação > Execução" → "IMPORTACAO > IMPORTACAO > EXECUCAO"
        normalized = menu_path.upper()
        # Remove diacritics (simple approach for PT-BR)
        for orig, repl in [("Ã", "A"), ("Õ", "O"), ("Ç", "C"), ("É", "E"),
                           ("Ê", "E"), ("Á", "A"), ("Ó", "O"), ("Ú", "U"),
                           ("Â", "A"), ("Ô", "O"), ("Í", "I")]:
            normalized = normalized.replace(orig, repl)
        menu_path_normalized = normalized
        for part in re.split(r"\s*>\s*", normalized):
            part = part.strip()
            if part and len(part) > 2:
                keywords.add(part)

    # 3. URLs → keywords via URL_KEYWORD_MAP
    for step in journey.get("steps", []):
        url = (step.get("url") or "").lower()
        # Extract window names from URL (last segment usually)
        segments = url.strip("/").split("/")
        for seg in segments:
            # Match against known URL fragments
            for fragment, kw in URL_KEYWORD_MAP.items():
                if fragment in seg:
                    keywords.add(kw)
            # Also try the raw segment as keyword (uppercase, clean)
            clean = re.sub(r"[^a-z0-9]", " ", seg).strip().upper()
            if clean and len(clean) > 3:
                keywords.add(clean)

    return {
        "module": module,
        "menu_path_normalized": menu_path_normalized,
        "keywords_upper": keywords,
    }


def score_mappings(search_terms: dict, playwright_map: dict) -> list[dict]:
    """Score each mapping from playwright-test-map.json against RUM search terms."""
    scoring = playwright_map.get("scoring", {})
    menu_path_pts = scoring.get("menu_path_match", 7)
    screen_kw_pts = scoring.get("screen_keyword_match", 5)
    keyword_pts = scoring.get("keyword_match", 3)
    min_score = scoring.get("min_score_to_include", 3)
    max_specs = scoring.get("max_specs", 5)

    kw_upper = search_terms["keywords_upper"]
    menu_norm = search_terms["menu_path_normalized"]
    results = []

    for mapping in playwright_map.get("mappings", []):
        score = 0
        reasons = []

        # menu_path match
        map_menu = (mapping.get("menu_path") or "").upper()
        if menu_norm and map_menu:
            # Check if any significant part of the RUM menu matches the mapping menu
            rum_parts = set(re.split(r"\s*>\s*", menu_norm))
            map_parts = set(re.split(r"\s*>\s*", map_menu))
            overlap = rum_parts & map_parts
            # Need at least 2 matching parts, or the specific part (not generic like "BASICO")
            significant = [p for p in overlap if len(p) > 5]
            if len(significant) >= 1:
                score += menu_path_pts
                reasons.append(f"menu_path: {map_menu}")

        # screen_keywords match
        for skw in mapping.get("screen_keywords", []):
            skw_upper = skw.upper()
            if skw_upper in kw_upper or any(skw_upper in kw for kw in kw_upper):
                score += screen_kw_pts
                reasons.append(f"screen_kw: {skw}")

        # keywords match
        for kw in mapping.get("keywords", []):
            kw_up = kw.upper()
            if kw_up in kw_upper or any(kw_up in k for k in kw_upper):
                score += keyword_pts
                reasons.append(f"keyword: {kw}")

        if score >= min_score:
            results.append({
                "id": mapping.get("id", ""),
                "category": mapping.get("category", ""),
                "spec_files": mapping.get("spec_files", []),
                "score": score,
                "reasons": reasons,
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:max_specs]


def generate_ephemeral_spec(journey: dict, wi_id: str, output_dir: Path) -> str | None:
    """Generate ephemeral Playwright spec from RUM user journey steps."""
    steps = journey.get("steps", [])
    if not steps:
        return None

    module = journey.get("module", "Unknown")
    lines = [
        "import { test, expect } from '@playwright/test';",
        "",
        f"test('RUM Replay - WI {wi_id} - {module}', async ({{ page }}) => {{",
    ]

    for step in steps:
        action = step.get("action", "")
        url = step.get("url", "")

        if action == "navigate":
            duration = step.get("duration_ms", 0)
            lines.append(f"  // Step {step.get('seq', '?')}: navigate ({duration}ms)")
            lines.append(f"  await page.goto('{url}');")
            lines.append(f"  await page.waitForLoadState('networkidle');")
            if duration > 3000:
                lines.append(f"  // ALERTA: loading_time={duration}ms (acima de 3s)")
            lines.append("")

        elif action == "click":
            target = step.get("target", "element")
            lines.append(f"  // Step {step.get('seq', '?')}: click '{target}'")
            lines.append(f"  await page.getByText('{target}').click();")
            lines.append("")

        elif action == "error":
            err_type = step.get("type", "Error")
            msg = step.get("message", "")
            lines.append(f"  // Step {step.get('seq', '?')}: RUM capturou erro {err_type}")
            lines.append(f"  // Mensagem: {msg[:100]}")
            if url:
                lines.append(f"  await page.goto('{url}');")
                lines.append(f"  await page.waitForLoadState('networkidle');")
            # Escape single quotes in assertion
            safe_msg = msg[:60].replace("'", "\\'").replace('"', '\\"')
            lines.append(f"  // Validar que o erro NAO aparece apos o fix:")
            lines.append(f"  await expect(page.locator('body')).not.toContainText('{safe_msg}');")
            lines.append("")

    lines.append("});")

    spec_content = "\n".join(lines)
    spec_path = output_dir / f"e2e_rum_replay.spec.ts"
    output_dir.mkdir(parents=True, exist_ok=True)
    spec_path.write_text(spec_content, encoding="utf-8")

    return str(spec_path)


def execute_playwright(wi_id: str, specs: list[str], ephemeral_spec: str | None,
                       env: str, title: str, screenshots_dir: Path | None = None) -> dict:
    """Execute playwright_runner.py with matched specs + ephemeral."""
    all_specs = []
    for spec_entry in specs:
        if isinstance(spec_entry, dict):
            all_specs.extend(spec_entry.get("spec_files", []))
        else:
            all_specs.append(spec_entry)

    if ephemeral_spec:
        all_specs.append(ephemeral_spec)

    if not all_specs:
        return {"status": "skipped", "reason": "no specs to execute"}

    cmd = [
        sys.executable, str(PLAYWRIGHT_RUNNER),
        "--wi-id", wi_id,
        "--title", title,
        "--env", env,
        "--screenshot", "on",
    ]
    if screenshots_dir:
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        cmd.extend(["--screenshots-dir", str(screenshots_dir)])

    for spec in all_specs:
        cmd.extend(["--spec", spec])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=1200)
        return {
            "status": "success" if result.returncode == 0 else "failed",
            "returncode": result.returncode,
            "stdout": result.stdout[-2000:] if result.stdout else "",
            "stderr": result.stderr[-1000:] if result.stderr else "",
        }
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "reason": "playwright execution exceeded 20 min"}
    except FileNotFoundError:
        return {"status": "error", "reason": f"playwright_runner.py not found at {PLAYWRIGHT_RUNNER}"}


def save_result(wi_id: str, output_dir: Path, journey: dict, matched_specs: list[dict],
                ephemeral_spec: str | None, execution: dict | None, mode: str):
    """Save rum_to_e2e_result.json."""
    result = {
        "wi_id": wi_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "rum_source": str(TESTS_DIR / wi_id / f"rum_enrichment_{wi_id}.json"),
        "journey": {
            "module": journey.get("module", ""),
            "menu_path": journey.get("menu_path", ""),
            "steps_count": len(journey.get("steps", [])),
            "has_errors": any(s.get("action") == "error" for s in journey.get("steps", [])),
            "session_id": journey.get("session_id", ""),
        },
        "matched_specs": matched_specs,
        "total_playwright_specs": sum(len(m.get("spec_files", [])) for m in matched_specs),
        "ephemeral_spec": ephemeral_spec,
        "execution": execution or {"status": mode},
    }

    output_path = output_dir / "rum_to_e2e_result.json"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return result


def post_evidence_to_ado(wi_id: str, result: dict, output_dir: Path) -> bool:
    """Post Discussion comment + attach files to ADO Work Item."""
    try:
        sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
        from ado_discussion_templates import post_discussion_comment
        from ado_evidence_uploader import upload_attachment, attach_files_to_wi
        from ado_client import get_auth_headers_multi
    except ImportError as e:
        print(f"WARN: Nao foi possivel importar modulos ADO: {e}", file=sys.stderr)
        return False

    # 1. Build HTML comment
    j = result["journey"]
    specs = result["matched_specs"]
    exec_info = result.get("execution", {})
    status = exec_info.get("status", "N/A")
    stdout = exec_info.get("stdout", "")

    status_emoji = "PASS" if status == "success" else "FAIL" if status == "failed" else status.upper()

    html = f"""<h3>RUM -> E2E Bridge - Evidencia Automatizada</h3>
<table border="1" cellpadding="4" cellspacing="0">
<tr><td><b>Work Item</b></td><td>#{wi_id}</td></tr>
<tr><td><b>Modulo RUM</b></td><td>{j.get('module', '-')}</td></tr>
<tr><td><b>Menu Path</b></td><td>{j.get('menu_path', '-')}</td></tr>
<tr><td><b>Steps RUM</b></td><td>{j.get('steps_count', 0)} (erros: {'Sim' if j.get('has_errors') else 'Nao'})</td></tr>
<tr><td><b>Session ID</b></td><td>{j.get('session_id', '-')}</td></tr>
<tr><td><b>Specs Mapeados</b></td><td>{result.get('total_playwright_specs', 0)}</td></tr>
<tr><td><b>Resultado E2E</b></td><td><b>{status_emoji}</b></td></tr>
<tr><td><b>Data</b></td><td>{result.get('generated_at', '-')}</td></tr>
</table>
"""

    if specs:
        html += "<h4>Specs Playwright Mapeados via RUM</h4><table border='1' cellpadding='4' cellspacing='0'>"
        html += "<tr><th>Score</th><th>Mapping ID</th><th>Specs</th><th>Razoes</th></tr>"
        for m in specs:
            reasons = "<br>".join(m.get("reasons", [])[:3])
            html += f"<tr><td>{m['score']}</td><td>{m['id']}</td><td>{len(m.get('spec_files', []))}</td><td>{reasons}</td></tr>"
        html += "</table>"

    if stdout:
        # Extract just the summary portion
        summary_start = stdout.find("======")
        if summary_start >= 0:
            html += f"<h4>Relatorio Playwright</h4><pre>{stdout[summary_start:]}</pre>"

    if result.get("ephemeral_spec"):
        html += f"<p><i>Spec ephemeral gerado: e2e_rum_replay.spec.ts (replay do user journey real)</i></p>"

    # 2. Upload attachments FIRST (need URLs for inline images)
    print(f"\nUploading evidencias como attachments...")
    headers = get_auth_headers_multi()

    files_to_attach = []
    # rum_to_e2e_result.json
    result_json = output_dir / "rum_to_e2e_result.json"
    if result_json.exists():
        files_to_attach.append((str(result_json), result_json.name))
    # e2e_rum_replay.spec.ts
    spec_file = output_dir / "e2e_rum_replay.spec.ts"
    if spec_file.exists():
        files_to_attach.append((str(spec_file), spec_file.name))
    # e2e_report.txt
    report_file = output_dir / "e2e_report.txt"
    if report_file.exists():
        files_to_attach.append((str(report_file), report_file.name))
    # rum_enrichment JSON
    rum_file = output_dir / f"rum_enrichment_{wi_id}.json"
    if rum_file.exists():
        files_to_attach.append((str(rum_file), rum_file.name))

    # Screenshots
    screenshots_dir = output_dir / "screenshots"
    screenshot_urls = {}  # filename -> att_url (for inline images)
    if screenshots_dir.exists():
        for img in sorted(screenshots_dir.iterdir()):
            if img.is_file() and img.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".webp"):
                files_to_attach.append((str(img), img.name))

    attachment_urls = []
    for filepath, filename in files_to_attach:
        att_url = upload_attachment(filepath, filename, headers)
        if att_url:
            attachment_urls.append((filename, att_url))
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                screenshot_urls[filename] = att_url

    if attachment_urls:
        attach_files_to_wi(wi_id, attachment_urls, headers)

    # 3. Add screenshots inline in HTML
    if screenshot_urls:
        html += "<h4>Screenshots dos Testes E2E</h4>"
        for filename, url in screenshot_urls.items():
            label = filename.replace(".png", "").replace("-", " ").replace("_", " ")
            html += f"<p><b>{label}</b><br/>"
            html += f"<img src='{url}' alt='{filename}' style='max-width:800px; border:1px solid #ccc;' />"
            html += "</p>"

    html += "<p><i>Gerado automaticamente por rum_to_e2e.py (RUM -> Playwright bridge)</i></p>"

    # 4. Post Discussion comment (with inline images)
    print(f"Postando Discussion comment na WI #{wi_id}...")
    posted = post_discussion_comment(wi_id, html)

    return posted


def print_summary(result: dict):
    """Print human-readable summary."""
    j = result["journey"]
    print(f"\n## RUM -> E2E Bridge -- WI {result['wi_id']}")
    print(f"Modo: {result['mode']}")
    print(f"Modulo: {j['module']} | Menu: {j['menu_path']}")
    print(f"Steps RUM: {j['steps_count']} | Tem erros: {'Sim' if j['has_errors'] else 'Nao'}")

    specs = result["matched_specs"]
    if specs:
        print(f"\n### Specs Mapeados ({result['total_playwright_specs']} specs de {len(specs)} mappings)\n")
        print("| Score | ID | Specs | Razoes |")
        print("|-------|-------|-------|--------|")
        for m in specs:
            reasons_str = "; ".join(m["reasons"][:3])
            print(f"| {m['score']} | {m['id']} | {len(m['spec_files'])} | {reasons_str} |")
    else:
        print("\nNenhum spec mapeado encontrado.")

    if result.get("ephemeral_spec"):
        print(f"\n### Spec Ephemeral: {result['ephemeral_spec']}")

    exec_info = result.get("execution", {})
    status = exec_info.get("status", "")
    if status and status not in ("match_only", "dry_run"):
        print(f"\n### Execucao: {status}")


def main():
    parser = argparse.ArgumentParser(
        description="Bridge RUM user journey → Playwright E2E specs"
    )
    parser.add_argument("--wi-id", required=True, help="Work Item ID")
    parser.add_argument("--env", default="qa", help="Ambiente Playwright (default: qa)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Match + gerar spec, sem executar")
    parser.add_argument("--match-only", action="store_true",
                        help="Apenas identificar specs, sem gerar spec ephemeral")
    parser.add_argument("--no-ephemeral", action="store_true",
                        help="Nao gerar spec ephemeral, usar apenas specs mapeados")
    parser.add_argument("--output", help="Diretorio de output (default: tests/{WI_ID}/)")
    parser.add_argument("--title", default="", help="Titulo da WI (para playwright_runner)")
    parser.add_argument("--post-ado", action="store_true",
                        help="Postar evidencia na WI do ADO (Discussion + Attachments)")
    args = parser.parse_args()

    output_dir = Path(args.output) if args.output else TESTS_DIR / args.wi_id

    # 1. Load RUM enrichment
    rum_data = load_rum_enrichment(args.wi_id)
    journey = rum_data.get("DD_RUM_USER_JOURNEY")
    if not journey:
        print("ERRO: DD_RUM_USER_JOURNEY nao encontrado no enrichment.", file=sys.stderr)
        sys.exit(1)

    # 2. Extract search terms
    search_terms = extract_search_terms(journey)
    print(f"Termos extraidos do RUM: {', '.join(sorted(search_terms['keywords_upper']))}")

    # 3. Score against playwright-test-map.json
    playwright_map = load_playwright_map()
    matched_specs = score_mappings(search_terms, playwright_map)

    # 4. Generate ephemeral spec (unless --match-only or --no-ephemeral)
    ephemeral_spec = None
    if not args.match_only and not args.no_ephemeral:
        ephemeral_spec = generate_ephemeral_spec(journey, args.wi_id, output_dir)

    # 5. Execute (unless --dry-run or --match-only)
    execution = None
    mode = "execute"
    if args.match_only:
        mode = "match_only"
    elif args.dry_run:
        mode = "dry_run"
    else:
        title = args.title or journey.get("menu_path", f"WI {args.wi_id}")
        screenshots_dir = output_dir / "screenshots" if args.post_ado else None
        execution = execute_playwright(
            args.wi_id, matched_specs, ephemeral_spec, args.env, title,
            screenshots_dir=screenshots_dir
        )

    # 6. Save result
    result = save_result(
        args.wi_id, output_dir, journey, matched_specs,
        ephemeral_spec, execution, mode
    )

    print_summary(result)
    print(f"\nResultado salvo em: {output_dir / 'rum_to_e2e_result.json'}")

    # 7. Post evidence to ADO (if --post-ado)
    if args.post_ado:
        post_evidence_to_ado(args.wi_id, result, output_dir)


if __name__ == "__main__":
    main()
