#!/usr/bin/env python3
"""Build a granular test-case index from SuiteAutomation XML files.

Parses all XML files under suite-automation/teste/ and generates
knowledge/suite-automation/suite-test-index.json with per-test metadata
(packages, tables, comparison dirs, keywords).

Usage:
    python scripts/suite_index_builder.py              # Build index
    python scripts/suite_index_builder.py --dry-run    # Stats only
    python scripts/suite_index_builder.py --output /tmp/index.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SUITE_DIR = PROJECT_ROOT / "suite-automation"
TESTE_DIR = SUITE_DIR / "teste"
DEFAULT_OUTPUT = PROJECT_ROOT / "knowledge" / "suite-automation" / "suite-test-index.json"

VERSION = "1.0.0"


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------

def extract_packages(text: str) -> list[str]:
    """Extract PL/SQL package/procedure names from execpkg text.

    Examples:
        'SAF_SPED_CONTABIL_FPROC.executar(...)' → ['SAF_SPED_CONTABIL_FPROC']
        'SAF_IMPORTA_BAT(...)' → ['SAF_IMPORTA_BAT']
        'PKG.PROC1(...)\nPKG.PROC2(...)' → ['PKG']
    """
    # Oracle built-in functions to exclude (not actual PL/SQL packages)
    ORACLE_BUILTINS = {
        'TO_DATE', 'TO_CHAR', 'TO_NUMBER', 'NVL', 'NVL2', 'DECODE',
        'SUBSTR', 'INSTR', 'TRIM', 'LTRIM', 'RTRIM', 'UPPER', 'LOWER',
        'REPLACE', 'LPAD', 'RPAD', 'LENGTH', 'ROUND', 'TRUNC', 'MOD',
        'SYSDATE', 'SYSTIMESTAMP', 'MONTHS_BETWEEN', 'ADD_MONTHS',
        'COALESCE', 'GREATEST', 'LEAST', 'ABS', 'CEIL', 'FLOOR',
        'DBMS_OUTPUT', 'UTL_FILE', 'RAISE_APPLICATION_ERROR',
    }
    # Match WORD before optional .WORD then (
    matches = re.findall(r'(\w+)(?:\.\w+)?\s*\(', text)
    seen = set()
    result = []
    for m in matches:
        upper = m.upper()
        if upper not in seen and len(upper) > 2 and upper not in ORACLE_BUILTINS:
            seen.add(upper)
            result.append(upper)
    return result


def extract_tables(sql: str) -> list[str]:
    """Extract table names from SQL UPDATE/DELETE/INSERT statements."""
    matches = re.findall(
        r'(?:UPDATE|DELETE\s+FROM|INSERT\s+INTO)\s+(\w+)',
        sql, re.IGNORECASE,
    )
    seen = set()
    result = []
    for m in matches:
        upper = m.upper()
        if upper not in seen and len(upper) > 2:
            seen.add(upper)
            result.append(upper)
    return result


def extract_comparison_dirs(test_el: ET.Element) -> list[str]:
    """Extract comparison directory paths from a <teste> element.

    Looks in compararArqLog, compararArqSaida, compararArqCursor.
    Returns unique dir paths like 'UT_SPED_CONT/OS4791/3.00/DATA_CISAO'.
    """
    dirs = set()
    pattern = re.compile(r'/[Ee]sperado/(.+?)(?:/[^/]+\.\w+)$')

    for tag in ('compararArqLog', 'compararArqSaida', 'compararArqCursor'):
        for el in test_el.findall(tag):
            text = (el.text or '').strip()
            if not text:
                continue
            # Split by ; to get individual paths
            parts = text.split(';')
            for part in parts:
                part = part.strip()
                m = pattern.search(part)
                if m:
                    dirs.add(m.group(1))

    return sorted(dirs)


def extract_keywords(descricao: str) -> list[str]:
    """Extract keywords from test description.

    Split by |, -, spaces. Filter tokens < 3 chars. Uppercase.
    """
    tokens = re.split(r'[\|\-\s_]+', descricao)
    seen = set()
    result = []
    for t in tokens:
        t = t.strip().upper()
        if len(t) >= 3 and t not in seen:
            seen.add(t)
            result.append(t)
    return result


# ---------------------------------------------------------------------------
# XML parsing
# ---------------------------------------------------------------------------

def parse_xml_file(xml_path: Path, teste_dir: Path) -> dict | None:
    """Parse a single suite XML file. Returns suite-level dict or None on error."""
    rel_path = xml_path.relative_to(teste_dir).as_posix()

    try:
        # Try ISO-8859-1 first (most XMLs use this)
        tree = ET.parse(xml_path, parser=ET.XMLParser(encoding='iso-8859-1'))
    except ET.ParseError:
        try:
            tree = ET.parse(xml_path, parser=ET.XMLParser(encoding='utf-8'))
        except Exception as e:
            print(f"  AVISO: Falha ao parsear {rel_path}: {e}", file=sys.stderr)
            return None
    except Exception as e:
        print(f"  AVISO: Erro ao ler {rel_path}: {e}", file=sys.stderr)
        return None

    root = tree.getroot()

    # Check if this is a caso_teste XML
    if root.tag != 'caso_teste':
        return None

    grupo = (root.findtext('grupo') or '').strip()
    modulo = (root.findtext('modulo') or '').strip()

    testes_el = root.find('testes')
    if testes_el is None:
        return None

    tests = []
    for teste_el in testes_el.findall('teste'):
        num_str = teste_el.get('num', '')
        descricao = teste_el.get('descricao', '')

        try:
            num = int(num_str)
        except (ValueError, TypeError):
            continue

        # Collect all execpkg/execprocedure text
        pkg_texts = []
        for tag in ('execpkg', 'execprocedure'):
            for el in teste_el.findall(tag):
                if el.text:
                    pkg_texts.append(el.text)
        packages = extract_packages('\n'.join(pkg_texts))

        # Collect all SQL from update/delete/cargasafx
        sql_texts = []
        for tag in ('update', 'delete', 'cargasafx'):
            for el in teste_el.findall(tag):
                if el.text:
                    sql_texts.append(el.text)
        tables = extract_tables('\n'.join(sql_texts))

        # Comparison dirs
        comp_dirs = extract_comparison_dirs(teste_el)

        # Keywords from description
        keywords = extract_keywords(descricao)

        tests.append({
            'num': num,
            'descricao': descricao,
            'packages': packages,
            'tables': tables,
            'comparison_dirs': comp_dirs,
            'keywords': keywords,
        })

    if not tests:
        return None

    return {
        'grupo': grupo,
        'modulo': modulo,
        'test_count': len(tests),
        'tests': tests,
    }


# ---------------------------------------------------------------------------
# Index builder
# ---------------------------------------------------------------------------

def build_index(teste_dir: Path) -> dict:
    """Walk all XML files and build the complete index."""
    suites = {}
    xml_count = 0
    test_count = 0
    errors = 0

    xml_files = sorted(teste_dir.rglob('*.xml'))
    print(f"Encontrados {len(xml_files)} arquivos XML em {teste_dir}")

    for xml_path in xml_files:
        result = parse_xml_file(xml_path, teste_dir)
        if result is None:
            errors += 1
            continue

        rel_path = xml_path.relative_to(teste_dir).as_posix()
        suites[rel_path] = result
        xml_count += 1
        test_count += result['test_count']

        # Collect unique packages for stats
        all_pkgs = set()
        for t in result['tests']:
            all_pkgs.update(t['packages'])

        print(f"  {rel_path}: {result['test_count']} testes, {len(all_pkgs)} packages")

    return {
        'version': VERSION,
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'xml_count': xml_count,
        'test_count': test_count,
        'errors_skipped': errors,
        'suites': suites,
    }


def print_stats(index: dict) -> None:
    """Print summary stats from built index."""
    print(f"\n{'='*60}")
    print(f"Suite Test Index — Estatisticas")
    print(f"{'='*60}")
    print(f"XMLs parseados:    {index['xml_count']}")
    print(f"XMLs com erro:     {index['errors_skipped']}")
    print(f"Total de testes:   {index['test_count']}")

    # Package stats
    all_pkgs = set()
    all_tables = set()
    for suite in index['suites'].values():
        for t in suite['tests']:
            all_pkgs.update(t['packages'])
            all_tables.update(t['tables'])
    print(f"Packages unicos:   {len(all_pkgs)}")
    print(f"Tabelas unicas:    {len(all_tables)}")

    # Top 10 suites by test count
    print(f"\nTop 10 suites por quantidade de testes:")
    sorted_suites = sorted(
        index['suites'].items(),
        key=lambda x: x[1]['test_count'],
        reverse=True,
    )
    for xml, data in sorted_suites[:10]:
        print(f"  {data['test_count']:4d} testes  {xml}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Gerar indice de cenarios SuiteAutomation a partir dos XMLs',
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Apenas mostrar estatisticas, nao gravar arquivo',
    )
    parser.add_argument(
        '--output', type=Path, default=DEFAULT_OUTPUT,
        help=f'Caminho do arquivo de saida (default: {DEFAULT_OUTPUT})',
    )
    parser.add_argument(
        '--teste-dir', type=Path, default=TESTE_DIR,
        help=f'Diretorio dos XMLs (default: {TESTE_DIR})',
    )
    args = parser.parse_args()

    if not args.teste_dir.exists():
        print(f"ERRO: Diretorio de testes nao encontrado: {args.teste_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Construindo indice de cenarios SuiteAutomation...")
    print(f"Diretorio: {args.teste_dir}")
    print()

    index = build_index(args.teste_dir)
    print_stats(index)

    if args.dry_run:
        print(f"\n(dry-run: indice NAO gravado)")
        return

    # Write index
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    size_kb = args.output.stat().st_size / 1024
    print(f"\nIndice gravado em: {args.output} ({size_kb:.1f} KB)")


if __name__ == '__main__':
    main()
