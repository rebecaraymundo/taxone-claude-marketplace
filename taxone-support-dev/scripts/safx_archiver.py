#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
safx_archiver.py - Archive SAFX test data from QA for reproduction in RC.

After QA validation, exports the SAFX rows used in testing so they can be
replayed in the RC environment.  Reads a test_data_manifest.json to know which
SAFX tables and isolation marker to use, then produces pipe-delimited flat
files (SuiteAutomation import format), SQL INSERT scripts with an {OWNER}
placeholder, and a snapshot of the corresponding X (definitive) tables.

Usage:
    python scripts/safx_archiver.py --wi-id 1078744
    python scripts/safx_archiver.py --wi-id 1078744 --env QA
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Well-known SAFX -> X table mappings (prefix-based convention)
# SAFX{NN} -> X{NN}_* (the X table includes a suffix with the functional name)
# We discover the actual X table name via DB catalog query when possible.

# Columns commonly used as isolation markers in SAFX tables, tried in order
ISOLATION_COLUMNS = ("NUM_LOTE", "LOTE_IMPORT", "NUM_LOTE_IMPORT")

# ---------------------------------------------------------------------------
# Imports from project
# ---------------------------------------------------------------------------

sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from env_connection import get_connection, get_owner  # noqa: E402


# ---------------------------------------------------------------------------
# Layout & Formatting (based on SAF_EXPORTA_TAB / PKG_FORMATA_EXPORTACAO)
# ---------------------------------------------------------------------------

# CAT_LAYOUT_IMP_CACHE.json location
_LAYOUT_CACHE_PATH = PROJECT_ROOT / "knowledge" / "schema" / "CAT_LAYOUT_IMP_CACHE.json"

# In-memory cache for loaded layouts
_layout_cache: dict | None = None


def _load_layout_cache() -> dict:
    """Load the CAT_LAYOUT_IMP_CACHE.json into memory (lazy, singleton)."""
    global _layout_cache
    if _layout_cache is not None:
        return _layout_cache
    if _LAYOUT_CACHE_PATH.exists():
        with open(_LAYOUT_CACHE_PATH, encoding="utf-8") as f:
            _layout_cache = json.load(f).get("layouts", {})
    else:
        _layout_cache = {}
    return _layout_cache


def _get_layout_for_table(
    table_name: str, wi_id: str | None = None
) -> dict[str, dict] | None:
    """Return a {column_name: {tipo, tamanho}} dict for the given SAFX table.

    Resolution order:
      1. tests/{wi_id}/safx_files/safx_layout_{num}.json (WI-specific)
      2. knowledge/schema/CAT_LAYOUT_IMP_CACHE.json (global cache)
      3. None (fallback: no formatting)
    """
    tbl = table_name.upper()

    # 1. WI-specific layout
    if wi_id:
        m = re.match(r"SAFX(\d+)", tbl)
        num = m.group(1) if m else tbl.replace("SAFX", "")
        wi_layout_path = PROJECT_ROOT / "tests" / str(wi_id) / "safx_files" / f"safx_layout_{num}.json"
        if wi_layout_path.exists():
            with open(wi_layout_path, encoding="utf-8") as f:
                data = json.load(f)
            fields = data.get("fields", [])
            if fields:
                return {f["nome_campo"].upper(): f for f in fields}

    # 2. Global cache
    cache = _load_layout_cache()
    if tbl in cache:
        return {f["nome_campo"].upper(): f for f in cache[tbl]}

    return None


def _parse_tamanho(tamanho: str) -> tuple[int, bool]:
    """Parse a tamanho spec like '003', '015V002' into (total_width, is_decimal).

    Returns (total_width, is_decimal):
      '003'     -> (3, False)
      '015V002' -> (17, True)   # 15 + 2 = 17
      '008'     -> (8, False)
    """
    if not tamanho:
        return (0, False)
    tamanho = tamanho.strip()
    if "V" in tamanho.upper():
        parts = tamanho.upper().split("V")
        int_part = int(parts[0])
        dec_part = int(parts[1]) if len(parts) > 1 else 0
        return (int_part + dec_part, True)
    return (int(tamanho), False)


def _format_field(val, field_info: dict | None) -> str:
    """Format a single value according to SAF_EXPORTA_TAB conventions.

    Rules (from PKG_FORMATA_EXPORTACAO):
      - NULL text  → empty string
      - NULL number → empty string
      - Number with 'NNNVDDD' spec → zero-padded to total width (already int in DB)
      - Number with 'NNN' spec → zero-padded
      - Date → YYYYMMDD (8 chars)
      - Text → raw value (no padding in pipe-delimited format)
    """
    if val is None:
        return ""

    if isinstance(val, datetime):
        return val.strftime("%Y%m%d")

    if field_info is None:
        # No layout info — best effort
        if isinstance(val, datetime):
            return val.strftime("%Y%m%d")
        return str(val)

    tipo = field_info.get("tipo", "A").upper()
    tamanho = field_info.get("tamanho", "")
    total_width, is_decimal = _parse_tamanho(tamanho)

    if tipo == "N" and total_width > 0:
        # Numeric field: zero-pad to width
        s = str(val).strip()
        # Remove any decimal point (values stored as scaled integers in SAFX)
        if "." in s:
            s = s.replace(".", "")
        # Remove leading minus for negative (edge case)
        neg = s.startswith("-")
        if neg:
            s = s[1:]
        return s.zfill(total_width)

    # Alfanumérico or unknown: raw value
    return str(val)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _find_isolation_column(cursor, owner: str, table_name: str) -> str | None:
    """Return the first matching isolation column that exists in *table_name*."""
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


def _resolve_x_table(cursor, owner: str, safx_name: str) -> str | None:
    """Find the corresponding X table for a given SAFX table.

    Convention: SAFX{NN} -> X{NN}_* (e.g. SAFX07 -> X07, SAFX2101 -> X2101_*).
    We query ALL_TABLES to find the actual name since X tables carry a suffix.
    """
    m = re.match(r"SAFX(\d+)", safx_name.upper())
    if not m:
        return None
    num = m.group(1)
    prefix = f"X{num}"

    # Try exact match first (e.g. X07)
    cursor.execute(
        "SELECT table_name FROM all_tables "
        "WHERE owner = :owner AND table_name = :tab",
        {"owner": owner.upper(), "tab": prefix},
    )
    row = cursor.fetchone()
    if row:
        return row[0]

    # Try prefix match (e.g. X07_%, X2101_%)
    cursor.execute(
        "SELECT table_name FROM all_tables "
        "WHERE owner = :owner AND table_name LIKE :pat "
        "ORDER BY table_name",
        {"owner": owner.upper(), "pat": f"{prefix}_%"},
    )
    row = cursor.fetchone()
    if row:
        return row[0]

    return None


def _escape_sql_value(val) -> str:
    """Return a SQL literal for *val*."""
    if val is None:
        return "NULL"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, datetime):
        return f"TO_DATE('{val.strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS')"
    # String — escape single quotes
    s = str(val).replace("'", "''")
    return f"'{s}'"


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------


def generate_flat_file(
    columns: list[str],
    rows: list[tuple],
    layout: dict[str, dict] | None = None,
    include_header: bool = False,
) -> str:
    """Return pipe-delimited text in SuiteAutomation import format.

    Formatting follows SAF_EXPORTA_TAB / PKG_FORMATA_EXPORTACAO conventions:
      - No header by default (data-only, as expected by SuiteAutomation)
      - Numeric fields zero-padded to declared width
      - Dates formatted as YYYYMMDD
      - NULLs as empty strings between pipes
    """
    lines: list[str] = []
    if include_header:
        lines.append("|".join(columns))
    for row in rows:
        parts = []
        for i, val in enumerate(row):
            col_name = columns[i].upper() if i < len(columns) else None
            field_info = layout.get(col_name) if layout and col_name else None
            parts.append(_format_field(val, field_info))
        lines.append("|".join(parts))
    return "\n".join(lines) + "\n"


def generate_inserts(columns: list[str], rows: list[tuple], table_name: str) -> str:
    """Return INSERT statements with ``{OWNER}`` placeholder for the schema.

    Each row becomes one INSERT ... VALUES (...) statement.
    """
    header = (
        f"-- INSERT statements for {table_name}\n"
        f"-- Generated by safx_archiver.py on {datetime.now(timezone.utc).isoformat()}\n"
        f"-- Replace {{OWNER}} with the target schema (e.g. USER_TAXONE_OCLOUD)\n"
        f"-- Total rows: {len(rows)}\n\n"
    )
    col_list = ", ".join(columns)
    stmts = []
    for row in rows:
        vals = ", ".join(_escape_sql_value(v) for v in row)
        stmts.append(f"INSERT INTO {{OWNER}}.{table_name} ({col_list}) VALUES ({vals});")
    return header + "\n".join(stmts) + "\n\nCOMMIT;\n"


def archive_safx_table(
    conn, owner: str, table_name: str, marker: str, output_dir: Path,
    wi_id: str | None = None,
) -> dict:
    """Export a single SAFX table filtered by the isolation marker.

    Returns a dict with metadata (name, rows_archived, flat_file, inserts_file).
    """
    cursor = conn.cursor()

    iso_col = _find_isolation_column(cursor, owner, table_name)
    if iso_col is None:
        print(f"  WARNING: no isolation column found in {table_name}, skipping")
        return {"name": table_name, "rows_archived": 0, "skipped": True,
                "reason": "no isolation column"}

    # Fetch column names
    cursor.execute(
        "SELECT column_name FROM all_tab_columns "
        "WHERE owner = :owner AND table_name = :tab "
        "ORDER BY column_id",
        {"owner": owner.upper(), "tab": table_name.upper()},
    )
    columns = [r[0] for r in cursor.fetchall()]
    if not columns:
        print(f"  WARNING: no columns found for {owner}.{table_name}, skipping")
        return {"name": table_name, "rows_archived": 0, "skipped": True,
                "reason": "table not found"}

    # Query data
    sql = f'SELECT * FROM {owner}.{table_name} WHERE {iso_col} = :marker'
    cursor.execute(sql, {"marker": marker})
    rows = cursor.fetchall()

    if not rows:
        print(f"  {table_name}: 0 rows (marker={marker})")
        return {"name": table_name, "rows_archived": 0,
                "flat_file": None, "inserts_file": None}

    # Load layout for field formatting (SAF_EXPORTA_TAB reference)
    layout = _get_layout_for_table(table_name, wi_id=wi_id)
    if layout:
        print(f"    Layout loaded: {len(layout)} fields")
    else:
        print(f"    WARNING: no layout found for {table_name}, using raw format")

    # Generate outputs
    flat_file_name = f"{table_name}.txt"
    inserts_file_name = f"{table_name}_inserts.sql"

    flat_content = generate_flat_file(columns, rows, layout=layout)
    (output_dir / flat_file_name).write_text(flat_content, encoding="utf-8")

    inserts_content = generate_inserts(columns, rows, table_name)
    (output_dir / inserts_file_name).write_text(inserts_content, encoding="utf-8")

    print(f"  {table_name}: {len(rows)} rows archived")

    cursor.close()
    return {
        "name": table_name,
        "rows_archived": len(rows),
        "flat_file": flat_file_name,
        "inserts_file": inserts_file_name,
    }


def snapshot_x_tables(
    conn, owner: str, safx_tables: list[dict], marker: str
) -> dict:
    """Query the corresponding X (definitive) tables for each SAFX table.

    Returns a dict keyed by SAFX table name with the X table name, row count
    and sample column values for validation reference.
    """
    cursor = conn.cursor()
    snapshots = {}

    for tbl in safx_tables:
        safx_name = tbl["name"]
        x_table = _resolve_x_table(cursor, owner, safx_name)
        if x_table is None:
            snapshots[safx_name] = {
                "x_table": None,
                "note": f"No corresponding X table found for {safx_name}",
            }
            continue

        # Check if the X table has an isolation column too
        iso_col = _find_isolation_column(cursor, owner, x_table)
        if iso_col:
            cursor.execute(
                f"SELECT COUNT(*) FROM {owner}.{x_table} WHERE {iso_col} = :marker",
                {"marker": marker},
            )
            count = cursor.fetchone()[0]

            # Grab a few column names for reference
            cursor.execute(
                "SELECT column_name FROM all_tab_columns "
                "WHERE owner = :owner AND table_name = :tab "
                "ORDER BY column_id FETCH FIRST 10 ROWS ONLY",
                {"owner": owner.upper(), "tab": x_table.upper()},
            )
            sample_cols = [r[0] for r in cursor.fetchall()]

            snapshots[safx_name] = {
                "x_table": x_table,
                "isolation_column": iso_col,
                "row_count": count,
                "sample_columns": sample_cols,
            }
        else:
            # No isolation column in X table — just note its existence
            cursor.execute(
                f"SELECT COUNT(*) FROM {owner}.{x_table}",
            )
            total = cursor.fetchone()[0]
            snapshots[safx_name] = {
                "x_table": x_table,
                "isolation_column": None,
                "total_rows": total,
                "note": "X table has no isolation column; total count shown for reference",
            }

        print(f"  {safx_name} -> {x_table}: {snapshots[safx_name].get('row_count', 'N/A')} matched rows")

    cursor.close()
    return snapshots


def archive_all(wi_id: str, env: str = "QA") -> dict:
    """Orchestrate the full SAFX archival for a Work Item.

    1. Read test_data_manifest.json
    2. Connect to the specified environment
    3. Archive each SAFX table (flat file + INSERT script)
    4. Snapshot corresponding X tables
    5. Write manifest.json

    Returns the manifest dict.
    """
    # --- Paths ---
    tests_dir = PROJECT_ROOT / "tests" / str(wi_id)
    manifest_path = tests_dir / "test_data_manifest.json"

    if not manifest_path.exists():
        raise FileNotFoundError(
            f"test_data_manifest.json not found at {manifest_path}\n"
            f"Run test data setup first to create the manifest."
        )

    with open(manifest_path, encoding="utf-8") as f:
        input_manifest = json.load(f)

    # --- Resolve isolation marker (v1 and v3 manifest formats) ---
    marker = input_manifest.get("isolation_marker", "")
    if not marker:
        # v3 format: environment.usuario_marker or derive from NUM_LOTE convention
        env_block = input_manifest.get("environment", {})
        if isinstance(env_block, dict):
            marker = env_block.get("usuario_marker", "")
            if not marker:
                # fallback: LOTE_TESTE_{WI_ID} convention
                marker = f"LOTE_TESTE_{wi_id}"
        elif not marker:
            marker = f"LOTE_TESTE_{wi_id}"
    if not marker:
        raise ValueError("isolation_marker is empty in test_data_manifest.json")

    # --- Resolve tables list (v1 and v3 manifest formats) ---
    tables = input_manifest.get("tables", [])
    if not tables:
        # v3 format: tables_affected with {table: "NAME"} entries
        tables_affected = input_manifest.get("tables_affected", [])
        tables = [
            {"name": t["table"]} if isinstance(t, dict) and "table" in t
            else {"name": t} if isinstance(t, str)
            else t
            for t in tables_affected
        ]
    else:
        # Normalize: tables can be ["SAFX07"] (v3 shorthand) or [{"name": "SAFX07"}] (v1)
        tables = [
            {"name": t} if isinstance(t, str) else t
            for t in tables
        ]
    if not tables:
        raise ValueError("No tables listed in test_data_manifest.json")

    # --- Output directory ---
    output_dir = tests_dir / "safx_archive_rc"
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Connect ---
    print(f"\n=== SAFX Archiver ===")
    print(f"  WI       : {wi_id}")
    print(f"  Env      : {env}")
    print(f"  Marker   : {marker}")
    print(f"  Tables   : {[t['name'] for t in tables]}")
    print(f"  Output   : {output_dir}\n")

    conn = get_connection(env)
    owner = get_owner(env)
    print(f"  Connected to {env} (owner: {owner})\n")

    # --- Archive each SAFX table ---
    print("[1/3] Archiving SAFX tables...")
    archived_tables = []
    for tbl in tables:
        result = archive_safx_table(conn, owner, tbl["name"], marker, output_dir, wi_id=wi_id)
        archived_tables.append(result)

    # --- Snapshot X tables ---
    print("\n[2/3] Capturing X-table snapshots...")
    x_snapshots = snapshot_x_tables(conn, owner, tables, marker)
    x_snapshot_path = output_dir / "x_tables_snapshot.json"
    x_snapshot_path.write_text(
        json.dumps(x_snapshots, indent=2, default=str, ensure_ascii=False),
        encoding="utf-8",
    )

    # --- Write manifest ---
    print("\n[3/3] Writing manifest...")
    manifest = {
        "version": "1.0.0",
        "wi_id": str(wi_id),
        "archived_at": datetime.now(timezone.utc).isoformat(),
        "source_env": env.upper(),
        "source_owner": owner,
        "target_env": "RC",
        "isolation_marker": marker,
        "tables": [
            {
                "name": t["name"],
                "rows_archived": t["rows_archived"],
                "flat_file": t.get("flat_file"),
                "inserts_file": t.get("inserts_file"),
            }
            for t in archived_tables
            if not t.get("skipped")
        ],
    }
    manifest_out = output_dir / "manifest.json"
    manifest_out.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    conn.close()

    total_rows = sum(t["rows_archived"] for t in archived_tables)
    print(f"\n  Done! {total_rows} total rows archived across "
          f"{len(manifest['tables'])} tables.")
    print(f"  Output: {output_dir}")

    return manifest


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _cli():
    parser = argparse.ArgumentParser(
        description="Archive SAFX test data from QA for reproduction in RC."
    )
    parser.add_argument(
        "--wi-id",
        required=True,
        help="Work Item ID (e.g. 1078744)",
    )
    parser.add_argument(
        "--env",
        default="QA",
        choices=["QA", "qa", "LOCAL", "local", "AC", "ac"],
        help="Source environment (default: QA)",
    )
    args = parser.parse_args()

    try:
        manifest = archive_all(args.wi_id, env=args.env.upper())
        print(f"\nManifest: {json.dumps(manifest, indent=2)}")
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    _cli()
