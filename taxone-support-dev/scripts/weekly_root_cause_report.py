#!/usr/bin/env python3
"""
weekly_root_cause_report.py — Relatorio semanal consolidado de causas raiz.

Consolida dados de 3 fontes:
  1. tests/{WI_ID}/root_cause_entry.json  (dados estruturados)
  2. knowledge/solutions/{WI_ID}.md       (Compound Engineering — parse YAML + Root Cause)
  3. ADO API                              (Custom.DescriptionofRootCause, tag SUST-IA-CLAUDE)

Uso:
  python weekly_root_cause_report.py                        # ultima semana
  python weekly_root_cause_report.py --from 2026-03-01      # desde 01/Mar ate hoje
  python weekly_root_cause_report.py --from 2026-03-01 --to 2026-03-15
  python weekly_root_cause_report.py --output json           # saida JSON em vez de Markdown
  python weekly_root_cause_report.py --no-ado                # sem consulta ao ADO (offline)
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ado_client import (
    ADO_ORG, ADO_PROJECT_ENC, ADO_API_VERSION, ADO_BASE,
    get_ado_pat, get_auth_header, ado_get, ado_post,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = PROJECT_ROOT / "knowledge" / "solutions"
TESTS_DIR = PROJECT_ROOT / "tests"
REPORT_DIR = PROJECT_ROOT / "reports" / "root-cause"

# --- Categorias ---

CATEGORY_LABELS = {
    "recompilation_gap": "Recompilacao pendente",
    "code_bug": "Bug de codigo",
    "performance": "Performance",
    "config_error": "Erro de configuracao",
    "data_quality": "Qualidade de dados",
    "design_gap": "Gap de design",
    "regression": "Regressao",
    "environment": "Ambiente",
    "unknown": "Nao categorizado",
}

CHANGE_TYPE_LABELS = {
    "DDL": "DDL (estrutura de tabela)",
    "PR": "Pull Request (codigo)",
    "PATCH": "Patch/Hotfix",
    "CONFIG": "Configuracao/Regra",
    "MIGRATION": "Migracao de dados",
    "NONE": "Sem alteracao originadora",
}


# =============================================================================
# Fonte 1: tests/{WI_ID}/root_cause_entry.json
# =============================================================================

def load_structured_entries(date_from: str, date_to: str) -> list[dict]:
    """Carrega root_cause_entry.json de cada WI em tests/."""
    entries = []
    if not TESTS_DIR.exists():
        return entries

    for wi_dir in TESTS_DIR.iterdir():
        if not wi_dir.is_dir():
            continue
        entry_file = wi_dir / "root_cause_entry.json"
        if not entry_file.exists():
            continue
        try:
            data = json.loads(entry_file.read_text(encoding="utf-8"))
            analysis_date = data.get("analysis_date", "")
            if date_from <= analysis_date <= date_to:
                data["_source"] = "structured"
                entries.append(data)
        except (json.JSONDecodeError, KeyError):
            continue
    return entries


# =============================================================================
# Fonte 2: knowledge/solutions/{WI_ID}.md (Compound Engineering)
# =============================================================================

def parse_solution_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter de um arquivo de solucao."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip("'").strip('"') for v in val[1:-1].split(",")]
            fm[key] = val
    return fm


def extract_root_cause_section(content: str) -> str:
    """Extrai a secao ## Root Cause do markdown."""
    match = re.search(r"## Root Cause\s*\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_originating_change(root_cause_text: str, content: str) -> dict | None:
    """Tenta extrair a alteracao originadora do texto da causa raiz."""
    change = {}

    # Buscar DDL references
    ddl_match = re.search(r"DDL[_ ]?(MFS\d+)", root_cause_text + " " + content, re.IGNORECASE)
    if ddl_match:
        change["type"] = "DDL"
        change["reference"] = f"DDL_{ddl_match.group(1)}"
        wi_match = re.search(r"MFS(\d+)", ddl_match.group(1))
        if wi_match:
            change["wi_id"] = wi_match.group(1)

    # Buscar PR references
    if not change:
        pr_match = re.search(r"PR\s*#?(\d+)", root_cause_text)
        if pr_match:
            change["type"] = "PR"
            change["reference"] = f"PR #{pr_match.group(1)}"

    # Buscar WI references como causa
    if not change:
        wi_match = re.search(r"(?:WI|work.?item|bug)\s*#?(\d{5,})", root_cause_text, re.IGNORECASE)
        if wi_match:
            change["type"] = "PR"
            change["reference"] = f"WI #{wi_match.group(1)}"
            change["wi_id"] = wi_match.group(1)

    return change if change else None


def infer_category(root_cause_text: str) -> str:
    """Infere a categoria de causa raiz a partir do texto."""
    text_lower = root_cause_text.lower()

    if any(k in text_lower for k in ["recompil", "desatualiz", "nao foram recompilad", "invalid"]):
        return "recompilation_gap"
    if any(k in text_lower for k in ["union all", "performance", "lentidao", "consumindo"]):
        return "performance"
    if any(k in text_lower for k in ["configurac", "parametr", "regra"]):
        return "config_error"
    if any(k in text_lower for k in ["dados inconsist", "dados incorre"]):
        return "data_quality"
    if any(k in text_lower for k in ["nao previsto", "design", "funcionalidade"]):
        return "design_gap"
    if any(k in text_lower for k in ["regressao", "introduzid", "causado por"]):
        return "regression"
    if any(k in text_lower for k in ["ambiente", "permiss", "versao"]):
        return "environment"

    return "code_bug"


def load_compound_entries(date_from: str, date_to: str) -> list[dict]:
    """Carrega dados de knowledge/solutions/*.md."""
    entries = []
    if not SOLUTIONS_DIR.exists():
        return entries

    for md_file in SOLUTIONS_DIR.glob("*.md"):
        if md_file.name == "INDEX.md":
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        fm = parse_solution_frontmatter(content)
        if not fm.get("date"):
            continue
        if not (date_from <= fm["date"] <= date_to):
            continue

        root_cause_text = extract_root_cause_section(content)
        if not root_cause_text:
            continue

        originating = extract_originating_change(root_cause_text, content)

        entry = {
            "wi_id": fm.get("work_item", md_file.stem),
            "title": fm.get("title", ""),
            "analysis_date": fm["date"],
            "analyst": "Claude AI",
            "root_cause": {
                "category": infer_category(root_cause_text),
                "summary": root_cause_text.split("\n")[0][:200],
                "detail": root_cause_text[:500],
            },
            "affected_modules": fm.get("modules", []),
            "verdict": "BUG_CONFIRMED",
            "solution_type": "code_fix",
            "pr": fm.get("pr"),
            "zendesk": fm.get("zendesk"),
            "_source": "compound",
        }
        if originating:
            entry["root_cause"]["originating_change"] = originating
        if fm.get("branch"):
            entry["branch"] = fm["branch"]

        entries.append(entry)

    return entries


# =============================================================================
# Fonte 3: ADO API — Custom.DescriptionofRootCause
# =============================================================================

def ado_request(url: str) -> dict | None:
    """Faz request autenticado ao ADO."""
    try:
        return ado_get(url)
    except Exception as e:
        print(f"  [WARN] ADO request failed: {e}", file=sys.stderr)
        return None


def load_ado_entries(date_from: str, date_to: str) -> list[dict]:
    """Busca WIs com tag SUST-IA-CLAUDE no periodo e extrai root cause."""
    entries = []

    wiql_query = (
        "SELECT [System.Id] FROM WorkItems "
        "WHERE [System.Tags] CONTAINS 'SUST-IA-CLAUDE' "
        f"AND [System.ChangedDate] >= '{date_from}' "
        f"AND [System.ChangedDate] <= '{date_to}' "
        "ORDER BY [System.ChangedDate] DESC"
    )

    pat = get_ado_pat()
    if not pat:
        print("  [WARN] ADO_PAT nao configurado, pulando fonte ADO", file=sys.stderr)
        return entries

    try:
        result = ado_post(f"{ADO_BASE}/wit/wiql?{ADO_API_VERSION}", {"query": wiql_query})
    except Exception as e:
        print(f"  [WARN] WIQL query failed: {e}", file=sys.stderr)
        return entries

    wi_ids = [item["id"] for item in result.get("workItems", [])]
    if not wi_ids:
        return entries

    # Buscar detalhes em batches de 200
    for i in range(0, len(wi_ids), 200):
        batch = wi_ids[i:i+200]
        ids_str = ",".join(str(x) for x in batch)
        fields = "System.Id,System.Title,System.Tags,System.ChangedDate,Custom.DescriptionofRootCause,System.WorkItemType"
        detail_url = (
            f"{ADO_BASE}/wit/workitems?ids={ids_str}&fields={fields}&{ADO_API_VERSION}"
        )
        detail_data = ado_request(detail_url)
        if not detail_data:
            continue

        for wi in detail_data.get("value", []):
            f = wi.get("fields", {})
            root_cause_html = f.get("Custom.DescriptionofRootCause", "")
            if not root_cause_html:
                continue

            # Strip HTML
            root_cause_text = re.sub(r"<[^>]+>", " ", root_cause_html).strip()
            root_cause_text = re.sub(r"\s+", " ", root_cause_text)

            if len(root_cause_text) < 10:
                continue

            originating = extract_originating_change(root_cause_text, "")

            entry = {
                "wi_id": str(wi["id"]),
                "title": f.get("System.Title", ""),
                "analysis_date": f.get("System.ChangedDate", "")[:10],
                "root_cause": {
                    "category": infer_category(root_cause_text),
                    "summary": root_cause_text[:200],
                    "detail": root_cause_text[:500],
                },
                "affected_modules": [],
                "verdict": "BUG_CONFIRMED",
                "_source": "ado",
            }
            if originating:
                entry["root_cause"]["originating_change"] = originating

            entries.append(entry)

    return entries


# =============================================================================
# Consolidacao e deduplicacao
# =============================================================================

def consolidate(structured: list, compound: list, ado: list) -> list[dict]:
    """Consolida entradas das 3 fontes, priorizando structured > compound > ado."""
    by_wi = {}

    # ADO primeiro (menor prioridade)
    for e in ado:
        by_wi[e["wi_id"]] = e

    # Compound sobrescreve ADO
    for e in compound:
        by_wi[e["wi_id"]] = e

    # Structured sobrescreve tudo
    for e in structured:
        by_wi[e["wi_id"]] = e

    return sorted(by_wi.values(), key=lambda x: x.get("analysis_date", ""), reverse=True)


# =============================================================================
# Geracao de relatorio
# =============================================================================

def generate_markdown_report(entries: list[dict], date_from: str, date_to: str) -> str:
    """Gera relatorio Markdown."""
    lines = []
    lines.append(f"# Relatorio Semanal de Causas Raiz")
    lines.append(f"")
    lines.append(f"**Periodo:** {date_from} a {date_to}")
    lines.append(f"**Gerado em:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Total de WIs analisadas:** {len(entries)}")
    lines.append("")

    if not entries:
        lines.append("Nenhuma WI com causa raiz identificada no periodo.")
        return "\n".join(lines)

    # --- Resumo por categoria ---
    cat_counts: dict[str, int] = {}
    for e in entries:
        cat = e.get("root_cause", {}).get("category", "unknown")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    lines.append("## Resumo por Categoria")
    lines.append("")
    lines.append("| Categoria | Qtd | % |")
    lines.append("|-----------|-----|---|")
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        label = CATEGORY_LABELS.get(cat, cat)
        pct = round(count / len(entries) * 100)
        lines.append(f"| {label} | {count} | {pct}% |")
    lines.append("")

    # --- Detalhamento por WI ---
    lines.append("## Detalhamento por WI")
    lines.append("")
    lines.append("| WI | Modulo | Categoria | Causa Raiz | Alteracao Originadora | PR | Fonte |")
    lines.append("|-----|--------|-----------|------------|----------------------|-----|-------|")

    for e in entries:
        wi = e.get("wi_id", "?")
        modules = ", ".join(e.get("affected_modules", [])) or "-"
        cat = CATEGORY_LABELS.get(e.get("root_cause", {}).get("category", "unknown"), "?")
        summary = e.get("root_cause", {}).get("summary", "")[:80]
        orig = e.get("root_cause", {}).get("originating_change", {})
        orig_str = f"{orig.get('type', '')}: {orig.get('reference', '')}" if orig else "-"
        pr = e.get("pr", "-") or "-"
        source = e.get("_source", "?")
        lines.append(f"| {wi} | {modules} | {cat} | {summary} | {orig_str} | {pr} | {source} |")
    lines.append("")

    # --- Alteracoes originadoras ---
    orig_counts: dict[str, list] = {}
    for e in entries:
        orig = e.get("root_cause", {}).get("originating_change", {})
        if orig:
            ref = orig.get("reference", "desconhecida")
            if ref not in orig_counts:
                orig_counts[ref] = []
            orig_counts[ref].append(e.get("wi_id", "?"))

    if orig_counts:
        lines.append("## Alteracoes Originadoras (que geraram bugs)")
        lines.append("")
        lines.append("| Alteracao | Tipo | WIs afetadas | Qtd |")
        lines.append("|-----------|------|-------------|-----|")
        for ref, wis in sorted(orig_counts.items(), key=lambda x: -len(x[1])):
            # Find type from first entry
            change_type = "-"
            for e in entries:
                o = e.get("root_cause", {}).get("originating_change", {})
                if o.get("reference") == ref:
                    change_type = CHANGE_TYPE_LABELS.get(o.get("type", ""), o.get("type", "-"))
                    break
            lines.append(f"| {ref} | {change_type} | {', '.join(wis)} | {len(wis)} |")
        lines.append("")

    # --- Patterns recorrentes ---
    pattern_counts: dict[str, list] = {}
    for e in entries:
        pattern = e.get("pattern")
        if pattern:
            if pattern not in pattern_counts:
                pattern_counts[pattern] = []
            pattern_counts[pattern].append(e.get("wi_id", "?"))

    if pattern_counts:
        lines.append("## Patterns Recorrentes")
        lines.append("")
        for pattern, wis in sorted(pattern_counts.items(), key=lambda x: -len(x[1])):
            lines.append(f"- **{pattern}** ({len(wis)}x): WIs {', '.join(wis)}")
        lines.append("")

    # --- Recomendacoes ---
    lines.append("## Recomendacoes")
    lines.append("")

    if cat_counts.get("recompilation_gap", 0) > 0:
        lines.append("- **Recompilacao**: Incluir etapa de recompilacao obrigatoria apos aplicacao de DDLs nos patches")

    if cat_counts.get("performance", 0) >= 2:
        lines.append("- **Performance**: Padroes UNION→UNION ALL recorrentes — considerar grep sistematico no repositorio")

    if cat_counts.get("code_bug", 0) >= 3:
        lines.append("- **Code Review**: Alta incidencia de bugs de codigo — reforcar revisao antes do merge")

    if len(orig_counts) > 0:
        top_orig = max(orig_counts.items(), key=lambda x: len(x[1]))
        if len(top_orig[1]) >= 2:
            lines.append(f"- **Alteracao de alto impacto**: `{top_orig[0]}` gerou {len(top_orig[1])} bugs — revisar escopo do impacto")

    if not any([cat_counts.get("recompilation_gap"), cat_counts.get("performance", 0) >= 2, cat_counts.get("code_bug", 0) >= 3]):
        lines.append("- Nenhuma recomendacao especifica para este periodo")

    lines.append("")
    lines.append("---")
    lines.append(f"*Gerado por `weekly_root_cause_report.py` | Fontes: structured ({sum(1 for e in entries if e.get('_source') == 'structured')}), compound ({sum(1 for e in entries if e.get('_source') == 'compound')}), ado ({sum(1 for e in entries if e.get('_source') == 'ado')})*")

    return "\n".join(lines)


def generate_html_report(entries: list[dict], date_from: str, date_to: str) -> str:
    """Gera relatorio HTML com tabelas estilizadas."""
    cat_counts: dict[str, int] = {}
    for e in entries:
        cat = e.get("root_cause", {}).get("category", "unknown")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    # Cores por categoria
    cat_colors = {
        "code_bug": "#e74c3c",
        "recompilation_gap": "#f39c12",
        "performance": "#3498db",
        "config_error": "#9b59b6",
        "data_quality": "#1abc9c",
        "design_gap": "#e67e22",
        "regression": "#c0392b",
        "environment": "#7f8c8d",
        "unknown": "#bdc3c7",
    }

    # Pie chart via CSS conic-gradient
    total = len(entries)
    gradient_parts = []
    legend_html = ""
    pct_acc = 0
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        label = CATEGORY_LABELS.get(cat, cat)
        color = cat_colors.get(cat, "#95a5a6")
        pct = round(count / total * 100)
        gradient_parts.append(f"{color} {pct_acc}% {pct_acc + pct}%")
        pct_acc += pct
        legend_html += f'<div style="display:flex;align-items:center;gap:8px;margin:4px 0"><span style="width:14px;height:14px;background:{color};border-radius:3px;display:inline-block"></span>{label}: <b>{count}</b> ({pct}%)</div>\n'
    gradient = ", ".join(gradient_parts)

    # Tabela detalhamento
    rows_html = ""
    for e in entries:
        wi = e.get("wi_id", "?")
        modules = ", ".join(e.get("affected_modules", [])) or "-"
        cat = CATEGORY_LABELS.get(e.get("root_cause", {}).get("category", "unknown"), "?")
        cat_key = e.get("root_cause", {}).get("category", "unknown")
        color = cat_colors.get(cat_key, "#95a5a6")
        summary = e.get("root_cause", {}).get("summary", "")[:120]
        orig = e.get("root_cause", {}).get("originating_change", {})
        orig_str = f"{orig.get('type', '')}: {orig.get('reference', '')}" if orig else "-"
        pr = e.get("pr", "-") or "-"
        source = e.get("_source", "?")
        rows_html += f"""<tr>
  <td><a href="https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/{wi}" target="_blank">{wi}</a></td>
  <td>{modules}</td>
  <td><span style="background:{color};color:#fff;padding:2px 8px;border-radius:10px;font-size:12px">{cat}</span></td>
  <td style="font-size:13px">{summary}</td>
  <td><b>{orig_str}</b></td>
  <td>{pr}</td>
  <td>{source}</td>
</tr>\n"""

    # Tabela alteracoes originadoras
    orig_counts: dict[str, list] = {}
    for e in entries:
        orig = e.get("root_cause", {}).get("originating_change", {})
        if orig:
            ref = orig.get("reference", "desconhecida")
            if ref not in orig_counts:
                orig_counts[ref] = []
            orig_counts[ref].append(e.get("wi_id", "?"))

    orig_rows = ""
    for ref, wis in sorted(orig_counts.items(), key=lambda x: -len(x[1])):
        change_type = "-"
        for e in entries:
            o = e.get("root_cause", {}).get("originating_change", {})
            if o.get("reference") == ref:
                change_type = CHANGE_TYPE_LABELS.get(o.get("type", ""), o.get("type", "-"))
                break
        wi_links = ", ".join(
            f'<a href="https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/{w}" target="_blank">{w}</a>'
            for w in wis
        )
        bar_pct = min(len(wis) * 20, 100)
        orig_rows += f"""<tr>
  <td><b>{ref}</b></td>
  <td>{change_type}</td>
  <td>{wi_links}</td>
  <td><div style="background:#e74c3c;height:18px;width:{bar_pct}%;border-radius:3px;text-align:center;color:#fff;font-size:11px;line-height:18px">{len(wis)}</div></td>
</tr>\n"""

    # Recomendacoes
    recs_html = ""
    if cat_counts.get("recompilation_gap", 0) > 0:
        recs_html += "<li><b>Recompilacao:</b> Incluir etapa de recompilacao obrigatoria apos aplicacao de DDLs nos patches</li>\n"
    if cat_counts.get("performance", 0) >= 2:
        recs_html += "<li><b>Performance:</b> Padroes UNION&rarr;UNION ALL recorrentes &mdash; considerar grep sistematico no repositorio</li>\n"
    if cat_counts.get("code_bug", 0) >= 3:
        recs_html += "<li><b>Code Review:</b> Alta incidencia de bugs de codigo &mdash; reforcar revisao antes do merge</li>\n"
    if orig_counts:
        top_orig = max(orig_counts.items(), key=lambda x: len(x[1]))
        if len(top_orig[1]) >= 2:
            recs_html += f"<li><b>Alteracao de alto impacto:</b> <code>{top_orig[0]}</code> gerou {len(top_orig[1])} bugs &mdash; revisar escopo do impacto</li>\n"
    if not recs_html:
        recs_html = "<li>Nenhuma recomendacao especifica para este periodo</li>"

    src_structured = sum(1 for e in entries if e.get("_source") == "structured")
    src_compound = sum(1 for e in entries if e.get("_source") == "compound")
    src_ado = sum(1 for e in entries if e.get("_source") == "ado")

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Relatorio de Causas Raiz - {date_from} a {date_to}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #f5f6fa; color: #2d3436; padding: 20px; }}
  .container {{ max-width: 1400px; margin: 0 auto; }}
  h1 {{ color: #2c3e50; margin-bottom: 6px; font-size: 28px; }}
  h2 {{ color: #34495e; margin: 30px 0 12px; font-size: 20px; border-bottom: 2px solid #3498db; padding-bottom: 6px; }}
  .meta {{ color: #7f8c8d; font-size: 14px; margin-bottom: 20px; }}
  .cards {{ display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 20px; }}
  .card {{ background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); flex: 1; min-width: 200px; }}
  .card .number {{ font-size: 36px; font-weight: bold; color: #2c3e50; }}
  .card .label {{ font-size: 13px; color: #7f8c8d; margin-top: 4px; }}
  .chart-container {{ display: flex; gap: 30px; align-items: center; flex-wrap: wrap; }}
  .pie {{ width: 180px; height: 180px; border-radius: 50%; background: conic-gradient({gradient}); flex-shrink: 0; }}
  table {{ width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 20px; }}
  th {{ background: #2c3e50; color: #fff; padding: 10px 12px; text-align: left; font-size: 13px; font-weight: 600; }}
  td {{ padding: 8px 12px; border-bottom: 1px solid #ecf0f1; font-size: 13px; }}
  tr:hover {{ background: #f8f9fa; }}
  a {{ color: #2980b9; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  ul {{ padding-left: 24px; }}
  li {{ margin: 8px 0; }}
  .footer {{ margin-top: 30px; padding-top: 12px; border-top: 1px solid #ddd; color: #95a5a6; font-size: 12px; }}
</style>
</head>
<body>
<div class="container">

<h1>Relatorio Semanal de Causas Raiz</h1>
<div class="meta">Periodo: {date_from} a {date_to} &nbsp;|&nbsp; Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>

<div class="cards">
  <div class="card"><div class="number">{total}</div><div class="label">WIs analisadas</div></div>
  <div class="card"><div class="number">{len(cat_counts)}</div><div class="label">Categorias</div></div>
  <div class="card"><div class="number">{len(orig_counts)}</div><div class="label">Alteracoes originadoras</div></div>
  <div class="card"><div class="number">{cat_counts.get('code_bug', 0)}</div><div class="label">Bugs de codigo</div></div>
</div>

<h2>Resumo por Categoria</h2>
<div class="chart-container">
  <div class="pie"></div>
  <div>{legend_html}</div>
</div>

<h2>Detalhamento por WI</h2>
<table>
<tr><th>WI</th><th>Modulo</th><th>Categoria</th><th>Causa Raiz</th><th>Alteracao Originadora</th><th>PR</th><th>Fonte</th></tr>
{rows_html}
</table>

<h2>Alteracoes Originadoras (que geraram bugs)</h2>
<table>
<tr><th>Alteracao</th><th>Tipo</th><th>WIs afetadas</th><th>Qtd</th></tr>
{orig_rows if orig_rows else '<tr><td colspan="4" style="text-align:center;color:#95a5a6">Nenhuma alteracao originadora identificada</td></tr>'}
</table>

<h2>Recomendacoes</h2>
<ul>{recs_html}</ul>

<div class="footer">
  Gerado por <code>weekly_root_cause_report.py</code> &nbsp;|&nbsp;
  Fontes: structured ({src_structured}), compound ({src_compound}), ado ({src_ado})
</div>

</div>
</body>
</html>"""
    return html


def generate_json_report(entries: list[dict], date_from: str, date_to: str) -> str:
    """Gera relatorio JSON."""
    # Remover campo _source interno
    clean = []
    for e in entries:
        c = {k: v for k, v in e.items() if not k.startswith("_")}
        clean.append(c)

    report = {
        "period": {"from": date_from, "to": date_to},
        "generated_at": datetime.now().isoformat(),
        "total": len(clean),
        "entries": clean,
    }
    return json.dumps(report, indent=2, ensure_ascii=False)


# =============================================================================
# Main
# =============================================================================

def main():
    # Fix encoding on Windows
    if sys.stdout.encoding != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    if sys.stderr.encoding != "utf-8":
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Relatorio semanal de causas raiz")
    parser.add_argument("--from", dest="date_from", help="Data inicio (YYYY-MM-DD). Default: 7 dias atras")
    parser.add_argument("--to", dest="date_to", help="Data fim (YYYY-MM-DD). Default: hoje")
    parser.add_argument("--output", choices=["markdown", "json", "html", "both", "all"], default="markdown", help="Formato de saida")
    parser.add_argument("--no-ado", action="store_true", help="Nao consultar ADO API (modo offline)")
    parser.add_argument("--save", action="store_true", help="Salvar em reports/root-cause/")
    args = parser.parse_args()

    today = datetime.now().strftime("%Y-%m-%d")
    date_from = args.date_from or (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    date_to = args.date_to or today

    print(f"Periodo: {date_from} a {date_to}")
    print()

    # Fonte 1: Structured
    print("Carregando fonte 1: tests/*/root_cause_entry.json...")
    structured = load_structured_entries(date_from, date_to)
    print(f"  {len(structured)} entradas")

    # Fonte 2: Compound
    print("Carregando fonte 2: knowledge/solutions/*.md...")
    compound = load_compound_entries(date_from, date_to)
    print(f"  {len(compound)} entradas")

    # Fonte 3: ADO
    ado = []
    if not args.no_ado:
        print("Carregando fonte 3: ADO API (Custom.DescriptionofRootCause)...")
        ado = load_ado_entries(date_from, date_to)
        print(f"  {len(ado)} entradas")
    else:
        print("Fonte 3: ADO API (pulada --no-ado)")

    # Consolidar
    entries = consolidate(structured, compound, ado)
    print(f"\nTotal consolidado: {len(entries)} WIs")
    print()

    # Gerar relatorio
    if args.output in ("markdown", "both", "all"):
        md = generate_markdown_report(entries, date_from, date_to)
        print(md)
        if args.save:
            REPORT_DIR.mkdir(parents=True, exist_ok=True)
            out_file = REPORT_DIR / f"root_cause_{date_from}_{date_to}.md"
            out_file.write_text(md, encoding="utf-8")
            print(f"\nSalvo em: {out_file}")

    if args.output in ("json", "both", "all"):
        js = generate_json_report(entries, date_from, date_to)
        if args.output == "json":
            print(js)
        if args.save:
            REPORT_DIR.mkdir(parents=True, exist_ok=True)
            out_file = REPORT_DIR / f"root_cause_{date_from}_{date_to}.json"
            out_file.write_text(js, encoding="utf-8")
            print(f"\nSalvo em: {out_file}")

    if args.output in ("html", "all"):
        html = generate_html_report(entries, date_from, date_to)
        if args.save:
            REPORT_DIR.mkdir(parents=True, exist_ok=True)
            out_file = REPORT_DIR / f"root_cause_{date_from}_{date_to}.html"
            out_file.write_text(html, encoding="utf-8")
            print(f"\nSalvo em: {out_file}")
        else:
            # Salvar em temp e abrir no browser
            import tempfile
            tmp = Path(tempfile.gettempdir()) / f"root_cause_{date_from}_{date_to}.html"
            tmp.write_text(html, encoding="utf-8")
            print(f"\nHTML gerado em: {tmp}")
        # Abrir no browser
        import webbrowser
        target = out_file if args.save else tmp
        webbrowser.open(str(target))
        print("Aberto no navegador.")


if __name__ == "__main__":
    main()
