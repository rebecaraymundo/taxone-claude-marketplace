"""
Módulo para gerar patch.sql empacotado em ZIP para deploy de queries.

Uso como módulo:
    from patch_generator import generate_patch
    zip_path = generate_patch("query.sql", "FEMSA", user="YOUR_USER_ID")
"""

from __future__ import annotations

import pathlib
import re
import shutil
import zipfile
from datetime import datetime

PATCH_HEADER = """\
Set feed off
set echo off
set line 500;
set pagesize 0
set SERVEROUTPUT ON SIZE UNLIMITED;
set markup csv on
-----------------------------------------------------------
--
-- Para gerar o output em formato CSV deve-se colocar o 
-- sql a partir da linha 14, colocar no final da query os 
-- caracteres '\\' ou ';'. saida em formato CSV 
--
-----------------------------------------------------------
"""

BASE_FOLDER_NAME = "Base de Dados"
PATCH_FILE_NAME = "patch.sql"
ALLOWED_EXTENSIONS = {".txt", ".sql"}


class PatchGeneratorError(Exception):
    """Erro genérico do gerador de patch."""


def _sanitize_query(content: str) -> str:
    """Remove comentários e garante que a query termina com ';'."""
    # Remove comentários multi-linha /* ... */
    content = re.sub(r"/\*.*?\*/", "", content, flags=re.DOTALL)
    # Remove comentários single-line -- ...
    content = re.sub(r"--[^\n]*", "", content)
    # Colapsa linhas em branco consecutivas
    content = re.sub(r"\n{3,}", "\n\n", content)
    # Remove espaços em branco no início/fim
    content = content.strip()
    # Garante ; no final
    if content and not content.endswith(";"):
        content += ";"
    return content + "\n"


def _validate_input(file_path: pathlib.Path) -> None:
    """Valida se o arquivo de entrada existe e possui extensão permitida.

    Raises:
        PatchGeneratorError: se a validação falhar.
    """
    if not file_path.exists():
        raise PatchGeneratorError(f"Arquivo não encontrado: {file_path}")

    if not file_path.is_file():
        raise PatchGeneratorError(
            f"O caminho informado não é um arquivo: {file_path}"
        )

    if file_path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise PatchGeneratorError(
            f"Extensão '{file_path.suffix}' não suportada. "
            f"Use: {', '.join(sorted(ALLOWED_EXTENSIONS))}"
        )


def generate_patch(
    sql_file: str | pathlib.Path,
    empresa: str,
    user: str = "",
) -> pathlib.Path:
    """Gera ZIP com patch.sql e retorna o caminho absoluto do ZIP.

    Args:
        sql_file: Caminho do arquivo .txt ou .sql contendo a query SQL.
        empresa: Nome da empresa (usado no nome do ZIP).
        user: Usuário (opcional). Quando informado, o ZIP terá o formato
              user_empresa_timestamp.zip.

    Returns:
        Caminho absoluto do ZIP gerado.

    Raises:
        PatchGeneratorError: em caso de erro de validação, leitura ou escrita.
    """
    file_path = pathlib.Path(sql_file).expanduser().resolve()
    _validate_input(file_path)

    # --- Leitura da query ---
    try:
        query_content = file_path.read_text(encoding="utf-8")
    except Exception as exc:
        raise PatchGeneratorError(f"Erro ao ler o arquivo: {exc}") from exc

    # --- Sanitização da query ---
    query_content = _sanitize_query(query_content)

    # --- Criação da pasta "Base de Dados" ---
    base_folder = pathlib.Path.cwd() / BASE_FOLDER_NAME
    base_folder.mkdir(parents=True, exist_ok=True)

    # --- Geração do patch.sql ---
    patch_path = base_folder / PATCH_FILE_NAME
    patch_content = PATCH_HEADER + query_content
    try:
        patch_path.write_text(patch_content, encoding="utf-8")
    except Exception as exc:
        raise PatchGeneratorError(
            f"Erro ao gravar {PATCH_FILE_NAME}: {exc}"
        ) from exc

    # --- Criação do ZIP ---
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if user:
        zip_name = f"{user}_{empresa}_{timestamp}.zip"
    else:
        zip_name = f"{timestamp}_{empresa}.zip"
    zip_path = (pathlib.Path.cwd() / zip_name).resolve()

    try:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            arcname = f"{BASE_FOLDER_NAME}/{PATCH_FILE_NAME}"
            zf.write(patch_path, arcname)
    except Exception as exc:
        raise PatchGeneratorError(f"Erro ao criar o ZIP: {exc}") from exc

    # --- Limpeza da pasta temporária ---
    try:
        shutil.rmtree(base_folder)
    except Exception as exc:
        # Apenas aviso, não é crítico
        print(
            f"Aviso: não foi possível remover a pasta "
            f"'{BASE_FOLDER_NAME}': {exc}"
        )

    return zip_path
