#!/usr/bin/env python3
"""
knowledge_search.py — Busca estrutural em knowledge base por tabelas, procedures, colunas, DDLs.

Resolve o gap de brainstorming: pipelines buscavam apenas por keywords do título,
sem cruzar por objetos estruturais (tabela, coluna, procedure, DDL).

Modos:
  python knowledge_search.py --table SAFX311
  python knowledge_search.py --procedure OL_IMP_X311
  python knowledge_search.py --column CHAVE_SAFX311
  python knowledge_search.py --ddl DDL_MFS868751
  python knowledge_search.py --keywords "importacao,SAFX311,dedup"
  python knowledge_search.py --wi-context 1081770

Fontes pesquisadas:
  1. knowledge/solutions/*.md (YAML frontmatter: tables, packages, modules)
  2. knowledge/solutions/INDEX.md (patterns recorrentes)
  3. knowledge/ado-fixes/_metadata.json (entries: title, tags, module, pr_numbers)
  4. tests/*/n3_brief.json (component_mapping)
  5. tests/*/analysis_result.md (grep)
"""

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = PROJECT_ROOT / "knowledge" / "solutions"
METADATA_PATH = PROJECT_ROOT / "knowledge" / "ado-fixes" / "_metadata.json"
TESTS_DIR = PROJECT_ROOT / "tests"


def parse_yaml_frontmatter(filepath: Path) -> dict:
    """Parse YAML frontmatter from a markdown file (simple parser, no PyYAML needed)."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}

    if not text.startswith("---"):
        return {}

    end = text.find("---", 3)
    if end == -1:
        return {}

    fm = {}
    for line in text[3:end].strip().splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        # Parse lists: [a, b, c]
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
            fm[key] = items
        else:
            fm[key] = val.strip("'\"")
    return fm


def search_solutions(terms: list[str]) -> list[dict]:
    """Search knowledge/solutions/*.md by YAML frontmatter fields."""
    results = []
    if not SOLUTIONS_DIR.exists():
        return results

    terms_lower = [t.lower() for t in terms]

    for md_file in SOLUTIONS_DIR.glob("*.md"):
        if md_file.name == "INDEX.md":
            continue

        fm = parse_yaml_frontmatter(md_file)
        if not fm:
            continue

        wi_id = str(fm.get("work_item", fm.get("wi_id", md_file.stem)))
        title = fm.get("title", "")

        # Collect searchable fields
        searchable = []
        for field in ("modules", "packages", "tables", "tags"):
            val = fm.get(field, [])
            if isinstance(val, str):
                val = [val]
            searchable.extend(val)

        searchable_lower = [s.lower() for s in searchable]
        # Also search in the title
        searchable_lower.append(title.lower())

        for term in terms_lower:
            for i, s in enumerate(searchable_lower):
                if term in s or s in term:
                    # Determine relevance
                    if term == s:
                        relevance = "HIGH"
                    elif term in s or s in term:
                        relevance = "MEDIUM"
                    else:
                        relevance = "LOW"

                    matched_val = searchable[i] if i < len(searchable) else title
                    results.append({
                        "source": "solutions",
                        "wi_id": wi_id,
                        "title": title,
                        "relevance": relevance,
                        "match_field": "frontmatter",
                        "match_value": matched_val,
                        "file": str(md_file.relative_to(PROJECT_ROOT)),
                    })
                    break  # One match per term per file is enough

    return results


def search_patterns_index(terms: list[str]) -> list[dict]:
    """Search knowledge/solutions/INDEX.md patterns section for structural matches."""
    index_path = SOLUTIONS_DIR / "INDEX.md"
    if not index_path.exists():
        return []

    try:
        text = index_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    # Extract patterns section
    patterns_start = text.find("## Patterns Recorrentes")
    if patterns_start == -1:
        patterns_start = text.find("## Patterns")
    if patterns_start == -1:
        return []

    patterns_text = text[patterns_start:]
    results = []
    terms_lower = [t.lower() for t in terms]

    # Parse each ### pattern block
    current_pattern = None
    current_content = []

    for line in patterns_text.splitlines():
        if line.startswith("### "):
            if current_pattern and current_content:
                content_joined = "\n".join(current_content).lower()
                for term in terms_lower:
                    if term in content_joined:
                        # Extract WI references
                        wi_refs = re.findall(r"WI\s+(\d+)", "\n".join(current_content))
                        results.append({
                            "source": "patterns",
                            "pattern": current_pattern,
                            "content_snippet": "\n".join(current_content)[:200],
                            "wi_references": wi_refs,
                            "matched_term": term,
                        })
                        break
            current_pattern = line[4:].strip()
            current_content = []
        elif current_pattern:
            current_content.append(line)

    # Last pattern
    if current_pattern and current_content:
        content_joined = "\n".join(current_content).lower()
        for term in terms_lower:
            if term in content_joined:
                wi_refs = re.findall(r"WI\s+(\d+)", "\n".join(current_content))
                results.append({
                    "source": "patterns",
                    "pattern": current_pattern,
                    "content_snippet": "\n".join(current_content)[:200],
                    "wi_references": wi_refs,
                    "matched_term": term,
                })

    return results


def search_metadata(terms: list[str]) -> list[dict]:
    """Search knowledge/ado-fixes/_metadata.json entries by title, tags, module."""
    if not METADATA_PATH.exists():
        return []

    try:
        with open(METADATA_PATH, "r", encoding="utf-8", errors="replace") as f:
            data = json.load(f)
    except Exception:
        return []

    entries = data.get("entries", [])
    results = []
    terms_lower = [t.lower() for t in terms]

    for entry in entries:
        title = (entry.get("title") or "").lower()
        module = (entry.get("module") or "").lower()
        tags = [str(t).lower() for t in (entry.get("tags") or [])]
        file_ref = entry.get("file", "")

        searchable = title + " " + module + " " + " ".join(tags) + " " + file_ref.lower()

        for term in terms_lower:
            if term in searchable:
                relevance = "HIGH" if term in title else "MEDIUM"
                results.append({
                    "source": "ado_metadata",
                    "wi_id": str(entry.get("id", "")),
                    "title": entry.get("title", ""),
                    "state": entry.get("state", ""),
                    "relevance": relevance,
                    "match_term": term,
                    "pr_numbers": entry.get("pr_numbers", []),
                    "has_solution": entry.get("has_solution", False),
                })
                break  # One match per entry

    # Limit to top 20 most relevant
    results.sort(key=lambda r: (0 if r["relevance"] == "HIGH" else 1, r.get("wi_id", "")))
    return results[:20]


def search_previous_analyses(terms: list[str]) -> list[dict]:
    """Search tests/*/n3_brief.json and analysis_result.md for structural matches."""
    if not TESTS_DIR.exists():
        return []

    results = []
    terms_lower = [t.lower() for t in terms]

    for wi_dir in TESTS_DIR.iterdir():
        if not wi_dir.is_dir():
            continue

        # Search n3_brief.json
        brief_path = wi_dir / "n3_brief.json"
        if brief_path.exists():
            try:
                with open(brief_path, "r", encoding="utf-8", errors="replace") as f:
                    brief = json.load(f)

                # Extract component_mapping tables and procedures
                cm = brief.get("component_mapping", {})
                tables = cm.get("tables", {})
                procs = cm.get("procedures", {})

                all_tables = []
                for v in tables.values():
                    if isinstance(v, list):
                        all_tables.extend(v)
                    elif isinstance(v, str):
                        all_tables.append(v)

                all_procs = []
                for v in procs.values():
                    if isinstance(v, list):
                        all_procs.extend(v)

                searchable = [t.lower() for t in all_tables + all_procs]

                for term in terms_lower:
                    for s in searchable:
                        if term in s or s in term:
                            wi_title = brief.get("work_item", {}).get("title", "")
                            results.append({
                                "source": "previous_analysis",
                                "wi_id": wi_dir.name,
                                "title": wi_title,
                                "relevance": "HIGH" if term == s else "MEDIUM",
                                "match_field": "component_mapping",
                                "match_value": s,
                            })
                            break
            except Exception:
                pass

        # Search analysis_result.md
        analysis_path = wi_dir / "analysis_result.md"
        if analysis_path.exists():
            try:
                text = analysis_path.read_text(encoding="utf-8", errors="replace").lower()
                for term in terms_lower:
                    if term in text:
                        # Extract verdict
                        verdict_match = re.search(r"veredicto:?\s*(\S+)", text)
                        verdict = verdict_match.group(1).upper() if verdict_match else "UNKNOWN"
                        results.append({
                            "source": "previous_analysis_md",
                            "wi_id": wi_dir.name,
                            "relevance": "MEDIUM",
                            "match_term": term,
                            "verdict": verdict,
                        })
                        break
            except Exception:
                pass

    return results


def extract_wi_context(wi_id: str) -> list[str]:
    """Extract structural terms from a WI's n3_brief.json."""
    brief_path = TESTS_DIR / wi_id / "n3_brief.json"
    terms = set()

    if brief_path.exists():
        try:
            with open(brief_path, "r", encoding="utf-8", errors="replace") as f:
                brief = json.load(f)

            cm = brief.get("component_mapping", {})

            # Tables
            for category, tables in cm.get("tables", {}).items():
                if isinstance(tables, list):
                    terms.update(tables)
                elif isinstance(tables, str):
                    terms.add(tables)

            # Procedures
            for category, procs in cm.get("procedures", {}).items():
                if isinstance(procs, list):
                    terms.update(procs)

            # Key columns
            for col_name in cm.get("key_columns_safx311", cm.get("key_columns", {})):
                terms.add(col_name)

            # Chave SAFX
            chave = cm.get("chave_safx311", cm.get("chave_safx", ""))
            if chave:
                terms.add("CHAVE_SAFX")

        except Exception:
            pass

    # Also try to extract from analysis_result.md
    analysis_path = TESTS_DIR / wi_id / "analysis_result.md"
    if analysis_path.exists():
        try:
            text = analysis_path.read_text(encoding="utf-8", errors="replace")
            # Extract table names (SAFX\d+, X\d+, ICT_*, etc.)
            table_matches = re.findall(r"\b(SAFX\d+|X\d+_\w+|ICT_\w+|DWT_\w+|EST_\w+)\b", text)
            terms.update(table_matches)
            # Extract procedure names
            proc_matches = re.findall(r"\b(OL_IMP_\w+|SAF_IMP_\w+|LIB_IMPORT|SAF_IMPORTA_\w+)\b", text)
            terms.update(proc_matches)
        except Exception:
            pass

    return list(terms)


def run_search(terms: list[str], exclude_wi: str = None) -> dict:
    """Run search across all sources and consolidate results."""
    if not terms:
        return {"query": {"terms": []}, "results": [], "patterns_matched": []}

    # Remove the current WI from results
    all_results = []

    solutions = search_solutions(terms)
    patterns = search_patterns_index(terms)
    metadata = search_metadata(terms)
    analyses = search_previous_analyses(terms)

    for r in solutions + metadata + analyses:
        if exclude_wi and str(r.get("wi_id", "")) == str(exclude_wi):
            continue
        all_results.append(r)

    # Deduplicate by wi_id, keeping highest relevance
    seen = {}
    for r in all_results:
        wi = r.get("wi_id", "")
        if wi not in seen or _relevance_rank(r["relevance"]) < _relevance_rank(seen[wi]["relevance"]):
            seen[wi] = r

    deduped = sorted(seen.values(), key=lambda r: _relevance_rank(r["relevance"]))

    return {
        "query": {"terms": terms},
        "results": deduped,
        "patterns_matched": patterns,
        "total_results": len(deduped),
        "total_patterns": len(patterns),
    }


def _relevance_rank(rel: str) -> int:
    return {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(rel, 3)


def main():
    parser = argparse.ArgumentParser(description="Busca estrutural na knowledge base TAX ONE")
    parser.add_argument("--table", help="Buscar por nome de tabela (ex: SAFX311)")
    parser.add_argument("--procedure", help="Buscar por nome de procedure/package (ex: OL_IMP_X311)")
    parser.add_argument("--column", help="Buscar por nome de coluna (ex: CHAVE_SAFX311)")
    parser.add_argument("--ddl", help="Buscar por DDL (ex: DDL_MFS868751)")
    parser.add_argument("--keywords", help="Keywords separados por virgula")
    parser.add_argument("--wi-context", help="Extrair termos automaticamente do n3_brief.json da WI")
    parser.add_argument("--output", help="Caminho para salvar output JSON")
    parser.add_argument("--format", choices=["json", "table"], default="json")
    args = parser.parse_args()

    terms = []
    exclude_wi = None

    if args.table:
        terms.append(args.table)
    if args.procedure:
        terms.append(args.procedure)
    if args.column:
        terms.append(args.column)
    if args.ddl:
        terms.append(args.ddl)
    if args.keywords:
        terms.extend([k.strip() for k in args.keywords.split(",") if k.strip()])
    if args.wi_context:
        exclude_wi = args.wi_context
        context_terms = extract_wi_context(args.wi_context)
        terms.extend(context_terms)
        if not terms:
            print(f"Nenhum termo estrutural encontrado para WI {args.wi_context}", file=sys.stderr)
            sys.exit(1)

    if not terms:
        parser.print_help()
        sys.exit(1)

    # Remove duplicates preserving order
    seen_terms = set()
    unique_terms = []
    for t in terms:
        tl = t.lower()
        if tl not in seen_terms:
            seen_terms.add(tl)
            unique_terms.append(t)

    result = run_search(unique_terms, exclude_wi=exclude_wi)

    if args.format == "table":
        print(f"\n## Busca Estrutural: {', '.join(unique_terms)}")
        print(f"\n### Resultados ({result['total_results']})\n")
        if result["results"]:
            print(f"| Relevancia | WI | Titulo | Fonte | Match |")
            print(f"|------------|-----|--------|-------|-------|")
            for r in result["results"]:
                print(f"| {r['relevance']} | {r.get('wi_id','-')} | {r.get('title','')[:50]} | {r['source']} | {r.get('match_value', r.get('match_term',''))} |")
        else:
            print("Nenhum resultado encontrado.")

        if result["patterns_matched"]:
            print(f"\n### Patterns Recorrentes ({result['total_patterns']})\n")
            for p in result["patterns_matched"]:
                print(f"- **{p['pattern']}** (WIs: {', '.join(p.get('wi_references',[]))})")
                print(f"  {p['content_snippet'][:100]}...")
    else:
        output = json.dumps(result, indent=2, ensure_ascii=False)
        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
            print(f"Output salvo em {args.output}", file=sys.stderr)
        print(output)


if __name__ == "__main__":
    main()
