#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
safx_auto_generator.py - Auto-detect and generate SAFX test data for a Work Item.

When no SuiteAutomation scenario exists for the component, this script detects
SAFX tables involved in the modified packages and generates portable flat-files
(pipe-delimited, SuiteAutomation-compatible) + SQL INSERT scripts so the test
can be reproduced in another environment (QA/RC).

Flow:
  1. Detect modified packages from branch MFS{WI_ID}
  2. Check component-test-map.json — if suite exists, exit (suite handles SAFX)
  3. Detect SAFX tables via DB dependencies + knowledge indexes
  4. Query existing rows as templates (from LOCAL)
  5. Generate flat-files + test_data_manifest.json
  6. Optionally invoke safx_archiver.py for RC archive

Usage:
    python scripts/safx_auto_generator.py --wi-id 1086591
    python scripts/safx_auto_generator.py --wi-id 1086591 --packages MUN_ISSNET_GERA_TOMAD,MUN_ISSNET_MM_FPROC
    python scripts/safx_auto_generator.py --wi-id 1086591 --env LOCAL --skip-archive
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

COMPONENT_MAP_PATH = PROJECT_ROOT / "knowledge" / "suite-automation" / "component-test-map.json"
SAFX_INDEX_PATH = PROJECT_ROOT / "knowledge" / "utplsql" / "safx-table-index.json"
LAYOUT_CACHE_PATH = PROJECT_ROOT / "knowledge" / "schema" / "CAT_LAYOUT_IMP_CACHE.json"

# Isolation marker convention
ISOLATION_MARKER_PREFIX = "LOTE_TESTE_"

# Columns commonly used as isolation markers, tried in order
ISOLATION_COLUMNS = ("NUM_LOTE", "LOTE_IMPORT", "NUM_LOTE_IMPORT")

# ---------------------------------------------------------------------------
# Imports from project
# ---------------------------------------------------------------------------

sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from env_connection import get_connection, get_owner  # noqa: E402
from env_loader import get_repo_path  # noqa: E402


# ---------------------------------------------------------------------------
# Step 1: Detect modified packages from branch
# ---------------------------------------------------------------------------

def detect_packages_from_branch(wi_id: str, repo_path: str | None = None) -> list[str]:
    """Detect PL/SQL package names modified in branch MFS{wi_id} vs DEV."""
    if repo_path is None:
        try:
            repo_path = get_repo_path("TAXONE_DW_REPO")
        except Exception:
            repo_path = r"C:\@@Dev\Git\taxone_dw"

    branch = f"MFS{wi_id}"
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"DEV..{branch}"],
            cwd=repo_path, capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            # Try origin/DEV
            result = subprocess.run(
                ["git", "diff", "--name-only", f"origin/DEV..{branch}"],
                cwd=repo_path, capture_output=True, text=True, timeout=30,
            )
    except Exception as exc:
        print(f"  AVISO: Nao foi possivel detectar packages do branch: {exc}")
        return []

    if result.returncode != 0:
        print(f"  AVISO: git diff falhou: {result.stderr.strip()}")
        return []

    packages = []
    for line in result.stdout.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        # PL/SQL files: .fon, .pck, .fnc, .prc, .trg, .sql
        if re.search(r'\.(fon|pck|fnc|prc|trg)$', line, re.IGNORECASE):
            # Extract package name from filename (without extension)
            name = Path(line).stem.upper()
            if name not in packages:
                packages.append(name)

    return packages


# ---------------------------------------------------------------------------
# Step 2: Check SuiteAutomation coverage
# ---------------------------------------------------------------------------

def check_suite_coverage(packages: list[str], file_paths: list[str] | None = None) -> dict | None:
    """Check component-test-map.json for SuiteAutomation coverage.

    Returns the matched mapping entry if score >= threshold, or None.
    """
    if not COMPONENT_MAP_PATH.exists():
        print(f"  AVISO: component-test-map.json nao encontrado, assumindo sem cobertura")
        return None

    with open(COMPONENT_MAP_PATH, encoding="utf-8") as f:
        data = json.load(f)

    scoring = data.get("scoring", {})
    pkg_score = scoring.get("package_match", 4)
    file_score = scoring.get("file_path_match", 5)
    min_score = scoring.get("min_score_to_include", 3)

    packages_upper = {p.upper() for p in packages}
    file_paths_lower = {fp.lower() for fp in (file_paths or [])}

    best_match = None
    best_score = 0

    for mapping in data.get("mappings", []):
        score = 0

        # Package match
        for mp in mapping.get("packages", []):
            if mp.upper() in packages_upper:
                score += pkg_score
                break

        # File path match
        for mfp in mapping.get("file_paths", []):
            for fp in file_paths_lower:
                if mfp.lower() in fp:
                    score += file_score
                    break
            if score >= file_score:
                break

        if score >= min_score and score > best_score:
            best_score = score
            best_match = mapping

    return best_match


# ---------------------------------------------------------------------------
# Step 3: Detect SAFX tables from packages
# ---------------------------------------------------------------------------

# DWT tables are working copies of X/SAFX tables.
# DWT_DOCTO_FISCAL = X07 = SAFX07, DWT_ITENS_MERC = X08 = SAFX08, etc.
DWT_TO_SAFX = {
    "DWT_DOCTO_FISCAL": "SAFX07",
    "DWT_ITENS_MERC": "SAFX08",
    "DWT_ITENS_SERV": "SAFX09",
}


def _x_to_safx(x_table: str) -> str | None:
    """Map an X table name back to its SAFX equivalent.

    Convention: X{NN}_* -> SAFX{NN}
    Examples: X07 -> SAFX07, X08_TIPO_DOCTO -> SAFX08, X2101_CONTAS_REF_CCUSTO -> SAFX2101
    """
    m = re.match(r"^X(\d+)", x_table.upper())
    if m:
        return f"SAFX{m.group(1)}"
    return None


def _dwt_to_safx(dwt_table: str) -> str | None:
    """Map a DWT table name to its SAFX equivalent.

    DWT tables are working/temporary copies of X (definitive) tables:
      DWT_DOCTO_FISCAL -> SAFX07 (X07)
      DWT_ITENS_MERC   -> SAFX08 (X08)
      DWT_ITENS_SERV   -> SAFX09 (X09)
    """
    return DWT_TO_SAFX.get(dwt_table.upper())


def _verify_safx_exists(cursor, owner: str, safx_name: str) -> bool:
    """Check if a SAFX table actually exists in the database."""
    cursor.execute(
        "SELECT COUNT(*) FROM all_tables WHERE owner = :owner AND table_name = :tab",
        {"owner": owner.upper(), "tab": safx_name.upper()},
    )
    return cursor.fetchone()[0] > 0


def detect_safx_from_db(conn, owner: str, packages: list[str]) -> list[str]:
    """Query ALL_DEPENDENCIES to find SAFX tables used by packages.

    Detection strategy:
      1. Direct: tables SAFX% referenced by the package
      2. Indirect: tables X% referenced by the package, mapped back to SAFX via
         convention X{NN}_* -> SAFX{NN} (each SAFX is the staging/import table
         for its corresponding X definitive table)
    """
    if not packages:
        return []

    cursor = conn.cursor()
    safx_tables = set()
    x_tables_found = set()

    for pkg in packages:
        try:
            # 1. Direct SAFX references
            cursor.execute(
                "SELECT DISTINCT referenced_name FROM all_dependencies "
                "WHERE owner = :owner AND name = :pkg AND referenced_type = 'TABLE' "
                "AND referenced_name LIKE 'SAFX%' "
                "ORDER BY referenced_name",
                {"owner": owner.upper(), "pkg": pkg.upper()},
            )
            for row in cursor.fetchall():
                safx_tables.add(row[0])

            # 2. Indirect: X tables -> reverse map to SAFX
            cursor.execute(
                "SELECT DISTINCT referenced_name FROM all_dependencies "
                "WHERE owner = :owner AND name = :pkg AND referenced_type = 'TABLE' "
                "AND referenced_name LIKE 'X%' "
                "AND referenced_name NOT LIKE 'XML%' "
                "ORDER BY referenced_name",
                {"owner": owner.upper(), "pkg": pkg.upper()},
            )
            for row in cursor.fetchall():
                x_name = row[0]
                safx_name = _x_to_safx(x_name)
                if safx_name and safx_name not in safx_tables:
                    if _verify_safx_exists(cursor, owner, safx_name):
                        safx_tables.add(safx_name)
                        x_tables_found.add(f"{x_name}->{safx_name}")

            # 3. Indirect: DWT tables -> reverse map to SAFX
            #    DWT_DOCTO_FISCAL=X07=SAFX07, DWT_ITENS_MERC=X08=SAFX08,
            #    DWT_ITENS_SERV=X09=SAFX09
            cursor.execute(
                "SELECT DISTINCT referenced_name FROM all_dependencies "
                "WHERE owner = :owner AND name = :pkg AND referenced_type = 'TABLE' "
                "AND referenced_name LIKE 'DWT%' "
                "ORDER BY referenced_name",
                {"owner": owner.upper(), "pkg": pkg.upper()},
            )
            for row in cursor.fetchall():
                dwt_name = row[0]
                safx_name = _dwt_to_safx(dwt_name)
                if safx_name and safx_name not in safx_tables:
                    if _verify_safx_exists(cursor, owner, safx_name):
                        safx_tables.add(safx_name)
                        x_tables_found.add(f"{dwt_name}->{safx_name}")

        except Exception as exc:
            print(f"  AVISO: Erro ao consultar dependencias de {pkg}: {exc}")

    if x_tables_found:
        print(f"    Mapeamento X->SAFX: {sorted(x_tables_found)}")

    cursor.close()
    return sorted(safx_tables)


def detect_safx_from_index(packages: list[str]) -> list[str]:
    """Fallback: use safx-table-index.json to find SAFX tables by procedure name patterns."""
    if not SAFX_INDEX_PATH.exists():
        return []

    with open(SAFX_INDEX_PATH, encoding="utf-8") as f:
        data = json.load(f)

    tables_section = data.get("tables", {})
    packages_upper = {p.upper() for p in packages}
    safx_tables = set()

    for safx_name, info in tables_section.items():
        # Check if any package matches the insere_procedure prefix
        proc = info.get("insere_procedure", "").upper()
        pkg_of_proc = proc.split(".")[0] if "." in proc else proc
        if pkg_of_proc in packages_upper:
            safx_tables.add(safx_name.upper())

    return sorted(safx_tables)


def detect_safx_tables(conn, owner: str, packages: list[str]) -> list[str]:
    """Detect SAFX tables using DB dependencies + knowledge indexes."""
    # Primary: DB dependencies
    tables = detect_safx_from_db(conn, owner, packages)
    if tables:
        print(f"  SAFX detectadas via DB dependencies: {tables}")
        return tables

    # Fallback: safx-table-index.json
    tables = detect_safx_from_index(packages)
    if tables:
        print(f"  SAFX detectadas via safx-table-index.json: {tables}")
        return tables

    print(f"  Nenhuma tabela SAFX detectada para packages: {packages}")
    return []


# ---------------------------------------------------------------------------
# Step 4: Extract existing rows as template data
# ---------------------------------------------------------------------------

def find_isolation_column(cursor, owner: str, table_name: str) -> str | None:
    """Return the first matching isolation column that exists in the table."""
    cursor.execute(
        "SELECT column_name FROM all_tab_columns "
        "WHERE owner = :owner AND table_name = :tab "
        "ORDER BY column_id",
        {"owner": owner.upper(), "tab": table_name.upper()},
    )
    existing = {row[0].upper() for row in cursor.fetchall()}
    for col in ISOLATION_COLUMNS:
        if col.upper() in existing:
            return col
    return None


def get_table_columns(cursor, owner: str, table_name: str) -> list[str]:
    """Get ordered column names for a table."""
    cursor.execute(
        "SELECT column_name FROM all_tab_columns "
        "WHERE owner = :owner AND table_name = :tab "
        "ORDER BY column_id",
        {"owner": owner.upper(), "tab": table_name.upper()},
    )
    return [r[0] for r in cursor.fetchall()]


def extract_sample_rows(conn, owner: str, table_name: str, max_rows: int = 5) -> tuple[list[str], list[tuple]]:
    """Extract a few sample rows from the SAFX table as template data.

    Returns (columns, rows).
    """
    cursor = conn.cursor()
    columns = get_table_columns(cursor, owner, table_name)
    if not columns:
        cursor.close()
        return [], []

    try:
        cursor.execute(
            f"SELECT * FROM {owner}.{table_name} "
            f"WHERE ROWNUM <= :maxr ORDER BY ROWID DESC",
            {"maxr": max_rows},
        )
        rows = cursor.fetchall()
    except Exception as exc:
        print(f"  AVISO: Erro ao extrair dados de {table_name}: {exc}")
        rows = []

    cursor.close()
    return columns, rows


# ---------------------------------------------------------------------------
# Step 5: Generate flat-files + manifest
# ---------------------------------------------------------------------------

def load_layout_cache() -> dict:
    """Load CAT_LAYOUT_IMP_CACHE.json."""
    if not LAYOUT_CACHE_PATH.exists():
        return {}
    with open(LAYOUT_CACHE_PATH, encoding="utf-8") as f:
        return json.load(f).get("layouts", {})


def get_layout_for_table(table_name: str, layouts: dict) -> dict | None:
    """Return {column_name: {tipo, tamanho}} for a SAFX table."""
    tbl = table_name.upper()
    if tbl in layouts:
        return {f["nome_campo"].upper(): f for f in layouts[tbl]}
    return None


def parse_tamanho(tamanho: str) -> tuple[int, bool]:
    """Parse CAT_LAYOUT_IMP tamanho spec."""
    if not tamanho:
        return (0, False)
    tamanho = tamanho.strip()
    if "V" in tamanho.upper():
        parts = tamanho.upper().split("V")
        int_part = int(parts[0])
        dec_part = int(parts[1]) if len(parts) > 1 else 0
        return (int_part + dec_part, True)
    return (int(tamanho), False)


def format_field(val, field_info: dict | None) -> str:
    """Format a single value per SAF_EXPORTA_TAB conventions."""
    if val is None:
        return ""

    if isinstance(val, datetime):
        return val.strftime("%Y%m%d")

    if field_info is None:
        if isinstance(val, datetime):
            return val.strftime("%Y%m%d")
        return str(val)

    tipo = field_info.get("tipo", "A").upper()
    tamanho = field_info.get("tamanho", "")
    total_width, is_decimal = parse_tamanho(tamanho)

    if tipo == "N" and total_width > 0:
        s = str(val).strip()
        if "." in s:
            s = s.replace(".", "")
        neg = s.startswith("-")
        if neg:
            s = s[1:]
        return s.zfill(total_width)

    return str(val)


def generate_flat_file(columns: list[str], rows: list[tuple], layout: dict | None = None) -> str:
    """Generate pipe-delimited flat-file content."""
    lines = []
    for row in rows:
        parts = []
        for i, val in enumerate(row):
            col_name = columns[i].upper() if i < len(columns) else None
            field_info = layout.get(col_name) if layout and col_name else None
            parts.append(format_field(val, field_info))
        lines.append("|".join(parts))
    return "\n".join(lines) + "\n" if lines else ""


def generate_inserts(columns: list[str], rows: list[tuple], table_name: str) -> str:
    """Generate INSERT statements with {OWNER} placeholder."""
    header = (
        f"-- INSERT statements for {table_name}\n"
        f"-- Generated by safx_auto_generator.py on {datetime.now(timezone.utc).isoformat()}\n"
        f"-- Replace {{OWNER}} with the target schema\n"
        f"-- Total rows: {len(rows)}\n\n"
    )
    col_list = ", ".join(columns)
    stmts = []
    for row in rows:
        vals = []
        for v in row:
            if v is None:
                vals.append("NULL")
            elif isinstance(v, (int, float)):
                vals.append(str(v))
            elif isinstance(v, datetime):
                vals.append(f"TO_DATE('{v.strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS')")
            else:
                s = str(v).replace("'", "''")
                vals.append(f"'{s}'")
        stmts.append(f"INSERT INTO {{OWNER}}.{table_name} ({col_list}) VALUES ({', '.join(vals)});")
    return header + "\n".join(stmts) + "\n\nCOMMIT;\n"


def generate_safx_files(
    conn, owner: str, wi_id: str, safx_tables: list[str], output_dir: Path
) -> list[dict]:
    """Generate flat-files + INSERT scripts for each SAFX table.

    Returns list of table metadata dicts.
    """
    layouts = load_layout_cache()
    results = []

    for table_name in safx_tables:
        print(f"\n  Processando {table_name}...")

        columns, rows = extract_sample_rows(conn, owner, table_name, max_rows=10)
        if not columns:
            print(f"    SKIP: tabela nao encontrada ou sem colunas")
            results.append({"name": table_name, "rows": 0, "skipped": True})
            continue

        layout = get_layout_for_table(table_name, layouts)
        if layout:
            print(f"    Layout: {len(layout)} campos")
        else:
            print(f"    AVISO: sem layout CAT_LAYOUT_IMP, usando formato raw")

        # Generate flat-file
        flat_content = generate_flat_file(columns, rows, layout)
        flat_file = output_dir / f"{table_name}.txt"
        flat_file.write_text(flat_content, encoding="utf-8")

        # Generate INSERT script
        inserts_content = generate_inserts(columns, rows, table_name)
        inserts_file = output_dir / f"{table_name}_inserts.sql"
        inserts_file.write_text(inserts_content, encoding="utf-8")

        print(f"    {len(rows)} rows -> {flat_file.name} + {inserts_file.name}")
        results.append({
            "name": table_name,
            "rows": len(rows),
            "flat_file": flat_file.name,
            "inserts_file": inserts_file.name,
            "columns": len(columns),
        })

    return results


def write_manifest(
    wi_id: str, env: str, packages: list[str],
    safx_tables: list[dict], output_dir: Path,
) -> dict:
    """Write test_data_manifest.json for downstream tools (safx_archiver, etc)."""
    marker = f"{ISOLATION_MARKER_PREFIX}{wi_id}"
    manifest = {
        "version": "3.0.0",
        "wi_id": str(wi_id),
        "generated_by": "safx_auto_generator",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "env": env.upper(),
            "usuario_marker": marker,
        },
        "packages_detected": packages,
        "tables_affected": [
            {"table": t["name"], "rows": t.get("rows", 0)}
            for t in safx_tables if not t.get("skipped")
        ],
        "tables": [
            {"name": t["name"]}
            for t in safx_tables if not t.get("skipped")
        ],
        "isolation_marker": marker,
    }

    # Write to tests/{WI_ID}/
    tests_dir = PROJECT_ROOT / "tests" / str(wi_id)
    tests_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = tests_dir / "test_data_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n  Manifest: {manifest_path}")

    return manifest


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def auto_generate(
    wi_id: str,
    packages: list[str] | None = None,
    env: str = "LOCAL",
    repo_path: str | None = None,
    skip_archive: bool = False,
    force: bool = False,
) -> dict:
    """Main orchestration: detect → check suite → detect SAFX → generate.

    Returns a result dict with status and details.
    """
    print(f"\n{'='*60}")
    print(f"  SAFX Auto Generator")
    print(f"  WI: {wi_id} | Env: {env}")
    print(f"{'='*60}")

    # --- Step 1: Detect packages ---
    if packages:
        print(f"\n[1/5] Packages informados: {packages}")
    else:
        print(f"\n[1/5] Detectando packages do branch MFS{wi_id}...")
        packages = detect_packages_from_branch(wi_id, repo_path)
        if not packages:
            print(f"  Nenhum package PL/SQL detectado no branch.")
            return {"status": "NO_PACKAGES", "wi_id": wi_id}
        print(f"  Packages: {packages}")

    # --- Step 2: Check SuiteAutomation coverage ---
    if not force:
        print(f"\n[2/5] Verificando cobertura SuiteAutomation...")
        suite_match = check_suite_coverage(packages)
        if suite_match:
            xml_file = suite_match.get("xml_file", "?")
            suite_id = suite_match.get("id", "?")
            print(f"  SUITE_EXISTS: {suite_id} -> {xml_file}")
            print(f"  A SuiteAutomation ja cobre este componente. SAFX nao necessaria.")
            return {
                "status": "SUITE_EXISTS",
                "wi_id": wi_id,
                "suite_id": suite_id,
                "suite_xml": xml_file,
            }
        print(f"  Nenhum cenario SuiteAutomation encontrado -> gerando SAFX")
    else:
        print(f"\n[2/5] --force: pulando verificacao SuiteAutomation")

    # --- Step 3: Detect SAFX tables ---
    print(f"\n[3/5] Detectando tabelas SAFX...")
    conn = get_connection(env)
    owner = get_owner(env)
    print(f"  Conectado a {env} (owner: {owner})")

    safx_tables = detect_safx_tables(conn, owner, packages)
    if not safx_tables:
        conn.close()
        print(f"\n  Nenhuma tabela SAFX encontrada para os packages.")
        return {
            "status": "NO_SAFX",
            "wi_id": wi_id,
            "packages": packages,
        }

    # --- Step 4: Generate flat-files ---
    print(f"\n[4/5] Gerando flat-files para {len(safx_tables)} tabelas SAFX...")
    output_dir = PROJECT_ROOT / "tests" / str(wi_id) / "safx_files"
    output_dir.mkdir(parents=True, exist_ok=True)

    table_results = generate_safx_files(conn, owner, wi_id, safx_tables, output_dir)

    # Write manifest
    manifest = write_manifest(wi_id, env, packages, table_results, output_dir)

    conn.close()

    # --- Step 5: Archive for RC ---
    if not skip_archive:
        print(f"\n[5/5] Executando safx_archiver para archive RC...")
        try:
            from safx_archiver import archive_all
            archive_all(wi_id, env=env)
        except Exception as exc:
            print(f"  AVISO: safx_archiver falhou: {exc}")
            print(f"  Os flat-files foram gerados em {output_dir}")
    else:
        print(f"\n[5/5] --skip-archive: pulando archive RC")

    total_rows = sum(t.get("rows", 0) for t in table_results if not t.get("skipped"))
    generated_tables = [t for t in table_results if not t.get("skipped")]

    print(f"\n{'='*60}")
    print(f"  Concluido!")
    print(f"  Tabelas: {len(generated_tables)} | Rows: {total_rows}")
    print(f"  Output: {output_dir}")
    print(f"{'='*60}")

    return {
        "status": "GENERATED",
        "wi_id": wi_id,
        "packages": packages,
        "safx_tables": [t["name"] for t in generated_tables],
        "total_rows": total_rows,
        "output_dir": str(output_dir),
        "manifest": manifest,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli():
    parser = argparse.ArgumentParser(
        description="Auto-detect and generate SAFX test data for a Work Item."
    )
    parser.add_argument(
        "--wi-id", required=True,
        help="Work Item ID (e.g. 1086591)",
    )
    parser.add_argument(
        "--packages", default="",
        help="Comma-separated list of PL/SQL packages (auto-detected from branch if omitted)",
    )
    parser.add_argument(
        "--env", default="LOCAL",
        choices=["LOCAL", "local", "QA", "qa", "AC", "ac"],
        help="Source environment (default: LOCAL)",
    )
    parser.add_argument(
        "--repo", default=None,
        help="Path to taxone_dw repo (default: from .env TAXONE_DW_REPO)",
    )
    parser.add_argument(
        "--skip-archive", action="store_true",
        help="Skip safx_archiver step (only generate flat-files)",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Force SAFX generation even if SuiteAutomation exists",
    )

    args = parser.parse_args()
    packages = [p.strip() for p in args.packages.split(",") if p.strip()] if args.packages else None

    try:
        result = auto_generate(
            wi_id=args.wi_id,
            packages=packages,
            env=args.env.upper(),
            repo_path=args.repo,
            skip_archive=args.skip_archive,
            force=args.force,
        )
        print(f"\nResultado: {json.dumps(result, indent=2, default=str)}")
        sys.exit(0 if result["status"] in ("GENERATED", "SUITE_EXISTS", "NO_SAFX") else 1)
    except Exception as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    _cli()
