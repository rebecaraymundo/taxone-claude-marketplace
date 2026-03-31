#!/usr/bin/env python3
"""
RUM Enricher — Centraliza logica de enriquecimento Datadog RUM para pipelines TAX ONE.

Modos de operacao:
  --mode analyze          Analisa RUM para uma WI (keywords + knowledge base)
  --mode refresh-baselines Atualiza performance-baselines.json com dados reais
  --mode match-errors     Cruza mensagem de erro com catalogo conhecido

O script NAO chama MCP diretamente. Ele:
1. Prepara queries e parametros para MCP Datadog
2. Analisa dados ja coletados (via --spans-file / --events-file)
3. Gera JSON/MD de enrichment padronizado

Uso tipico no pipeline:
  1. Pipeline executa MCP tools (search_datadog_spans, search_datadog_rum_events)
  2. Salva resultados em JSON
  3. Chama este script com --spans-file / --events-file
  4. Script gera rum_enrichment_{wi_id}.json + rum_enrichment_{wi_id}.md
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge" / "datadog"
TESTS_DIR = PROJECT_ROOT / "tests"

APP_ID = "56ad1497-3dd2-451b-95b7-906544ca1b09"
SERVICE = "taxone"
HOST = "www.onesourcetax.com"


def load_json(path: Path) -> dict | None:
    """Carrega JSON de arquivo. Retorna None se nao existe."""
    if not path.exists():
        print(f"[WARN] Arquivo nao encontrado: {path}", file=sys.stderr)
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_module_map() -> dict:
    return load_json(KNOWLEDGE_DIR / "module-service-map.json") or {}


def load_known_errors() -> list:
    data = load_json(KNOWLEDGE_DIR / "known-rum-errors.json")
    return data.get("errors", []) if data else []


def load_baselines() -> dict:
    data = load_json(KNOWLEDGE_DIR / "performance-baselines.json")
    return data.get("baselines", {}) if data else {}


def load_thresholds() -> dict:
    data = load_json(KNOWLEDGE_DIR / "performance-baselines.json")
    return data.get("thresholds", {
        "anomaly_deviation_pct": 50,
        "slow_page_load_ms": 10000,
        "critical_page_load_ms": 30000,
        "high_error_rate_pct": 5.0,
    }) if data else {}


# ---------------------------------------------------------------------------
# Classificacao de relevancia RUM
# ---------------------------------------------------------------------------

def classify_wi_rum_relevance(title: str, description: str = "") -> tuple[bool, list[str]]:
    """Determina se WI precisa de RUM enrichment e quais keywords ativaram."""
    module_map = load_module_map()
    all_keywords = set()

    for kw_list_key in ("rum_keywords_screen", "rum_keywords_performance"):
        for kw in module_map.get(kw_list_key, []):
            all_keywords.add(kw.lower())

    for mod_data in module_map.get("modules", {}).values():
        for kw in mod_data.get("keywords", []):
            all_keywords.add(kw.lower())

    text = f"{title} {description}".lower()
    matched = [kw for kw in all_keywords if kw in text]

    return bool(matched), sorted(set(matched))


def detect_module(title: str, description: str = "") -> str | None:
    """Detecta modulo TAX ONE a partir do texto da WI."""
    module_map = load_module_map()
    text = f"{title} {description}".lower()

    best_match = None
    best_count = 0

    for mod_name, mod_data in module_map.get("modules", {}).items():
        count = sum(1 for kw in mod_data.get("keywords", []) if kw.lower() in text)
        if count > best_count:
            best_count = count
            best_match = mod_name

    return best_match


# ---------------------------------------------------------------------------
# Query builders (geram instrucoes para MCP, nao executam)
# ---------------------------------------------------------------------------

def build_spans_query(module: str | None = None, error_only: bool = False,
                      from_time: str = "now-7d", to_time: str = "now") -> dict:
    """Gera parametros para search_datadog_spans MCP tool."""
    parts = [f"service:{SERVICE}"]
    if error_only:
        parts.append("status:error")

    module_map = load_module_map()
    if module and module in module_map.get("modules", {}):
        mod = module_map["modules"][module]
        resource_patterns = mod.get("resource_patterns", [])
        if resource_patterns:
            rp = " OR ".join(f'resource_name:"{p}"' for p in resource_patterns)
            parts.append(f"({rp})")

    return {
        "tool": "search_datadog_spans",
        "params": {
            "query": " ".join(parts),
            "from": from_time,
            "to": to_time,
            "custom_attributes": ["usr.*", "view.*", "session.*", "application.*", "geo.*"],
        }
    }


def build_rum_events_query(event_type: str = "error", module: str | None = None,
                           from_time: str = "now-7d", to_time: str = "now") -> dict:
    """Gera parametros para search_datadog_rum_events MCP tool."""
    parts = [f"@type:{event_type}", f"@application.id:{APP_ID}"]

    module_map = load_module_map()
    if module and module in module_map.get("modules", {}):
        parts.append(f'@usr.module:"{module}"')

    return {
        "tool": "search_datadog_rum_events",
        "params": {
            "query": " ".join(parts),
            "from": from_time,
            "to": to_time,
            "detailed_output": True,
        }
    }


def generate_mcp_queries(wi_id: str, title: str = "", description: str = "",
                         module: str | None = None) -> dict:
    """Gera todas as queries MCP necessarias para enrichment de uma WI."""
    if not module:
        module = detect_module(title, description)

    queries = {
        "wi_id": wi_id,
        "detected_module": module,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "queries": {
            "spans_errors": build_spans_query(module, error_only=True),
            "spans_all": build_spans_query(module, error_only=False),
            "rum_errors": build_rum_events_query("error", module),
            "rum_views": build_rum_events_query("view", module),
        }
    }
    return queries


# ---------------------------------------------------------------------------
# Analise de dados RUM ja coletados
# ---------------------------------------------------------------------------

def extract_user_journey(events: list[dict]) -> dict:
    """Reconstroi DD_RUM_USER_JOURNEY a partir de eventos RUM (views/spans)."""
    if not events:
        return {}

    steps = []
    module = None
    menu_path = None
    session_id = None
    has_replay = False
    user_info = {}

    sorted_events = sorted(events, key=lambda e: e.get("timestamp", ""))

    for i, evt in enumerate(sorted_events):
        attrs = evt.get("attributes", {})
        custom = attrs.get("custom", {})

        usr = custom.get("usr", {})
        if usr:
            if not module and usr.get("module"):
                module = usr["module"]
            if not menu_path and usr.get("menuPath"):
                menu_path = usr["menuPath"]
            if not user_info and usr.get("email"):
                user_info = {
                    "email": usr.get("email", ""),
                    "firm_id": usr.get("firmId", ""),
                    "db_schema": usr.get("dbSchema", ""),
                    "name": usr.get("name", ""),
                }

        session = custom.get("session", {})
        if session.get("id"):
            session_id = session["id"]
        if session.get("has_replay"):
            has_replay = True

        view = custom.get("view", {})
        evt_type = custom.get("type", "")

        if evt_type == "view":
            step = {
                "seq": i + 1,
                "action": "navigate",
                "url": view.get("url_path", view.get("url", "")),
                "view_name": view.get("name", ""),
                "duration_ms": (view.get("loading_time", 0) or 0) // 1_000_000,
            }
        elif evt_type == "error":
            error = custom.get("error", {})
            step = {
                "seq": i + 1,
                "action": "error",
                "message": error.get("message", ""),
                "type": error.get("type", ""),
                "source": error.get("source", ""),
                "url": view.get("url_path", ""),
            }
        else:
            step = {
                "seq": i + 1,
                "action": evt_type or "unknown",
                "url": view.get("url_path", ""),
            }

        steps.append(step)

    return {
        "module": module,
        "menu_path": menu_path,
        "steps": steps[:20],
        "session_replay": has_replay,
        "session_id": session_id,
        "user": user_info,
    }


def match_known_errors(error_messages: list[str]) -> list[dict]:
    """Cruza mensagens de erro com catalogo known-rum-errors.json."""
    known = load_known_errors()
    matches = []

    for msg in error_messages:
        for known_err in known:
            regex = known_err.get("regex", "")
            pattern = known_err.get("pattern", "")
            if (regex and re.search(regex, msg, re.IGNORECASE)) or \
               (pattern and pattern.lower() in msg.lower()):
                matches.append({
                    "error_message": msg[:200],
                    "matched_id": known_err["id"],
                    "matched_pattern": known_err["pattern"],
                    "severity": known_err["severity"],
                    "root_cause": known_err["root_cause"],
                    "action": known_err["action"],
                })
                break

    return matches


def detect_anomalies(metrics: dict) -> list[dict]:
    """Compara metricas atuais com baselines. metrics = {endpoint: {p50_ms, p95_ms, ...}}."""
    baselines = load_baselines()
    thresholds = load_thresholds()
    deviation_pct = thresholds.get("anomaly_deviation_pct", 50)
    anomalies = []

    for endpoint, current in metrics.items():
        baseline = baselines.get(endpoint)
        if not baseline:
            continue

        for metric_key in ("p50_ms", "p95_ms", "p99_ms"):
            current_val = current.get(metric_key)
            baseline_val = baseline.get(metric_key)
            if current_val and baseline_val and baseline_val > 0:
                pct = ((current_val - baseline_val) / baseline_val) * 100
                if pct > deviation_pct:
                    anomalies.append({
                        "endpoint": endpoint,
                        "metric": metric_key,
                        "current": current_val,
                        "baseline": baseline_val,
                        "deviation_pct": round(pct, 1),
                    })

    return anomalies


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def generate_enrichment_json(wi_id: str, journey: dict, errors: list,
                             anomalies: list, known_matches: list,
                             relevant: bool, keywords: list) -> dict:
    """Gera JSON padronizado com todas as variaveis DD_RUM_*."""
    return {
        "wi_id": wi_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "rum_relevant": relevant,
        "keywords_matched": keywords,
        "DD_RUM_USER_JOURNEY": journey,
        "DD_RUM_ERRORS": errors[:10],
        "DD_RUM_SESSION_ID": journey.get("session_id", ""),
        "DD_RUM_ANOMALIES": anomalies,
        "DD_RUM_KNOWN_MATCHES": known_matches,
    }


def generate_enrichment_md(wi_id: str, data: dict) -> str:
    """Gera markdown legivel para Discussion da WI."""
    lines = [
        f"## Datadog RUM Enrichment — WI #{wi_id}",
        f"**Data**: {data.get('generated_at', 'N/A')}",
        f"**RUM Relevante**: {'Sim' if data.get('rum_relevant') else 'Nao'}",
        f"**Keywords**: {', '.join(data.get('keywords_matched', []))}",
        "",
    ]

    journey = data.get("DD_RUM_USER_JOURNEY", {})
    if journey:
        lines.append("### User Journey")
        lines.append(f"- **Modulo**: {journey.get('module', 'N/A')}")
        lines.append(f"- **Menu Path**: {journey.get('menu_path', 'N/A')}")
        lines.append(f"- **Session Replay**: {'Disponivel' if journey.get('session_replay') else 'Indisponivel'}")
        user = journey.get("user", {})
        if user:
            lines.append(f"- **Usuario**: {user.get('name', 'N/A')} ({user.get('email', 'N/A')}) | Firm: {user.get('firm_id', 'N/A')} | Schema: {user.get('db_schema', 'N/A')}")
        lines.append("")

        steps = journey.get("steps", [])
        if steps:
            lines.append("| # | Acao | URL/Detalhe | Duracao |")
            lines.append("|---|------|------------|---------|")
            for step in steps[:10]:
                dur = f"{step.get('duration_ms', '')}ms" if step.get("duration_ms") else "-"
                detail = step.get("url", step.get("message", ""))[:80]
                lines.append(f"| {step.get('seq', '')} | {step.get('action', '')} | {detail} | {dur} |")
            lines.append("")

    errors = data.get("DD_RUM_ERRORS", [])
    if errors:
        lines.append("### Erros RUM")
        for err in errors[:5]:
            lines.append(f"- `{err.get('type', 'Error')}`: {err.get('message', '')[:100]}")
        lines.append("")

    known = data.get("DD_RUM_KNOWN_MATCHES", [])
    if known:
        lines.append("### Erros Conhecidos (Catalogo)")
        for km in known:
            lines.append(f"- **{km['matched_pattern']}** (severity: {km['severity']})")
            lines.append(f"  - Causa: {km['root_cause'][:100]}")
            lines.append(f"  - Acao: {km['action'][:100]}")
        lines.append("")

    anomalies = data.get("DD_RUM_ANOMALIES", [])
    if anomalies:
        lines.append("### Anomalias de Performance")
        lines.append("| Endpoint | Metrica | Atual | Baseline | Desvio |")
        lines.append("|----------|---------|-------|----------|--------|")
        for a in anomalies:
            lines.append(f"| {a['endpoint'][:40]} | {a['metric']} | {a['current']}ms | {a['baseline']}ms | +{a['deviation_pct']}% |")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Modos de execucao
# ---------------------------------------------------------------------------

def mode_analyze(args):
    """Modo analyze: classifica WI, analisa dados RUM, gera enrichment."""
    wi_id = args.wi_id
    if not wi_id:
        print("[ERROR] --wi-id obrigatorio para modo analyze", file=sys.stderr)
        sys.exit(1)

    title = args.title or ""
    description = args.description or ""
    keywords_override = args.keywords.split(",") if args.keywords else None

    # Classificar relevancia
    relevant, keywords = classify_wi_rum_relevance(title, description)
    if keywords_override:
        relevant = True
        keywords = keywords_override

    # Diretorio de output
    output_dir = Path(args.output_dir) if args.output_dir else TESTS_DIR / wi_id
    output_dir.mkdir(parents=True, exist_ok=True)

    # Se temos dados de spans/events, analisar
    journey = {}
    errors = []
    known_matches = []
    anomalies = []

    if args.spans_file and Path(args.spans_file).exists():
        spans_data = load_json(Path(args.spans_file))
        if spans_data and isinstance(spans_data, list):
            journey = extract_user_journey(spans_data)

    if args.events_file and Path(args.events_file).exists():
        events_data = load_json(Path(args.events_file))
        if events_data and isinstance(events_data, list):
            if not journey:
                journey = extract_user_journey(events_data)
            # Extrair mensagens de erro
            for evt in events_data:
                custom = evt.get("attributes", {}).get("custom", {})
                error = custom.get("error", {})
                msg = error.get("message", "")
                if msg:
                    errors.append({
                        "message": msg,
                        "type": error.get("type", ""),
                        "source": error.get("source", ""),
                    })

    # Match com catalogo
    error_messages = [e.get("message", "") for e in errors if e.get("message")]
    known_matches = match_known_errors(error_messages)

    # Gerar enrichment
    enrichment = generate_enrichment_json(
        wi_id, journey, errors, anomalies, known_matches, relevant, keywords
    )

    # Salvar JSON
    json_path = output_dir / f"rum_enrichment_{wi_id}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(enrichment, f, ensure_ascii=False, indent=2)
    print(f"[OK] Enrichment JSON: {json_path}")

    # Salvar MD
    md_content = generate_enrichment_md(wi_id, enrichment)
    md_path = output_dir / f"rum_enrichment_{wi_id}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[OK] Enrichment MD: {md_path}")

    # Se nao temos dados, gerar queries para o pipeline
    if not args.spans_file and not args.events_file:
        module = detect_module(title, description)
        queries = generate_mcp_queries(wi_id, title, description, module)
        queries_path = output_dir / f"rum_queries_{wi_id}.json"
        with open(queries_path, "w", encoding="utf-8") as f:
            json.dump(queries, f, ensure_ascii=False, indent=2)
        print(f"[OK] MCP Queries: {queries_path}")
        print(f"[INFO] Pipeline deve executar as queries MCP e re-chamar com --spans-file / --events-file")

    return enrichment


def mode_match_errors(args):
    """Modo match-errors: cruza mensagem com catalogo."""
    msg = args.error_message
    if not msg:
        print("[ERROR] --error-message obrigatorio para modo match-errors", file=sys.stderr)
        sys.exit(1)

    matches = match_known_errors([msg])
    if matches:
        for m in matches:
            print(f"[MATCH] {m['matched_pattern']} (severity: {m['severity']})")
            print(f"  Causa: {m['root_cause']}")
            print(f"  Acao:  {m['action']}")
    else:
        print(f"[NO MATCH] Nenhum erro conhecido encontrado para: {msg[:100]}")

    return matches


def mode_refresh_baselines(args):
    """Modo refresh-baselines: placeholder — requer dados MCP."""
    print("[INFO] refresh-baselines requer dados do Datadog.")
    print("[INFO] Pipeline deve:")
    print("  1. Executar get_datadog_metric para cada endpoint em module-service-map.json")
    print("  2. Passar resultados via --metrics-file")
    print("  3. Script atualiza performance-baselines.json")

    if args.metrics_file and Path(args.metrics_file).exists():
        metrics_data = load_json(Path(args.metrics_file))
        if metrics_data:
            baselines_path = KNOWLEDGE_DIR / "performance-baselines.json"
            current = load_json(baselines_path) or {
                "version": "1.0.0",
                "baselines": {},
                "thresholds": load_thresholds(),
            }
            current["generated_at"] = datetime.now(timezone.utc).isoformat()
            current["data_window_days"] = args.days

            for endpoint, data in metrics_data.items():
                current["baselines"][endpoint] = data

            with open(baselines_path, "w", encoding="utf-8") as f:
                json.dump(current, f, ensure_ascii=False, indent=2)
            print(f"[OK] Baselines atualizados: {baselines_path}")
    else:
        print("[INFO] Sem --metrics-file. Gerando queries necessarias:")
        module_map = load_module_map()
        for mod_name, mod_data in module_map.get("modules", {}).items():
            for pattern in mod_data.get("resource_patterns", [])[:1]:
                print(f"  get_datadog_metric: avg:trace.servlet.request.duration{{service:{SERVICE},resource_name:{pattern}}}")


def main():
    parser = argparse.ArgumentParser(
        description="RUM Enricher — Enriquecimento Datadog RUM para pipelines TAX ONE"
    )
    parser.add_argument("--mode", required=True,
                        choices=["analyze", "refresh-baselines", "match-errors"],
                        help="Modo de operacao")
    parser.add_argument("--wi-id", help="Work Item ID")
    parser.add_argument("--title", default="", help="Titulo da WI")
    parser.add_argument("--description", default="", help="Descricao da WI")
    parser.add_argument("--keywords", help="Keywords separados por virgula (override)")
    parser.add_argument("--error-message", help="Mensagem de erro para match")
    parser.add_argument("--spans-file", help="JSON com spans coletados via MCP")
    parser.add_argument("--events-file", help="JSON com RUM events coletados via MCP")
    parser.add_argument("--metrics-file", help="JSON com metricas para refresh-baselines")
    parser.add_argument("--days", type=int, default=7, help="Janela de dados em dias")
    parser.add_argument("--output-dir", help="Diretorio de output (default: tests/{wi_id}/)")

    args = parser.parse_args()

    if args.mode == "analyze":
        mode_analyze(args)
    elif args.mode == "match-errors":
        mode_match_errors(args)
    elif args.mode == "refresh-baselines":
        mode_refresh_baselines(args)


if __name__ == "__main__":
    main()
