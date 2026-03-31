"""
Módulo para upload de arquivo no JFrog Artifactory.

Uso como módulo:
    from jfrog_upload import upload_file
    upload_file(base_url="https://empresa.jfrog.io", repo="libs-release",
                dest_folder="Custom", file_path="patch.zip",
                user="YOUR_USER_ID", token="xxx")
"""

from __future__ import annotations

import os
import pathlib
from typing import Final
from urllib.parse import quote, urlsplit, urlunsplit

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException

DEFAULT_TIMEOUT_SECONDS: Final[int] = 60


class JFrogUploadError(Exception):
    """Erro genérico do upload para JFrog."""


def _normalize_base_url(base_url: str) -> str:
    """Normaliza a URL base do Artifactory, garantindo /artifactory."""
    parsed = urlsplit(base_url.strip())
    if not parsed.scheme or not parsed.netloc:
        raise JFrogUploadError(
            "URL inválida. Use o formato https://empresa.jfrog.io"
        )

    path = parsed.path.rstrip("/")
    if "/ui/" in f"{path}/" or path == "/ui":
        raise JFrogUploadError(
            "A URL informada parece ser da interface web (/ui). "
            "Use a URL do Artifactory API, ex.: https://empresa.jfrog.io/artifactory"
        )

    if "/artifactory" not in f"{path}/":
        path = f"{path}/artifactory" if path else "/artifactory"

    return urlunsplit((parsed.scheme, parsed.netloc, path.rstrip("/"), "", ""))


def _build_upload_url(
    base_url: str, target_folder: str, file_name: str, repo: str | None
) -> str:
    """Constrói a URL completa de upload."""
    clean_base = _normalize_base_url(base_url)
    clean_folder = target_folder.strip().strip("/")
    folder_parts = [part for part in clean_folder.split("/") if part]
    repo_part = repo.strip().strip("/") if repo else ""

    full_path_parts = (
        ([repo_part] if repo_part else []) + folder_parts + [file_name]
    )
    if not full_path_parts:
        raise JFrogUploadError("Informe ao menos repo ou dest_folder.")

    encoded_path = "/".join(quote(part, safe="") for part in full_path_parts)
    return f"{clean_base}/{encoded_path}"


def _build_auth(
    auth_mode: str, user: str | None, token: str
) -> tuple[HTTPBasicAuth | None, dict[str, str], str]:
    """Retorna (auth, headers, mode_selecionado)."""
    mode = auth_mode
    if mode == "auto":
        mode = "basic" if user else "bearer"

    if mode == "basic":
        if not user:
            raise JFrogUploadError(
                "No modo basic, o parâmetro user é obrigatório."
            )
        return HTTPBasicAuth(user, token), {}, mode

    if mode == "bearer":
        return None, {"Authorization": f"Bearer {token}"}, mode

    if mode == "apikey":
        return None, {"X-JFrog-Art-Api": token}, mode

    raise JFrogUploadError(f"Modo de autenticação inválido: {mode}")


def upload_file(
    base_url: str,
    repo: str,
    dest_folder: str,
    file_path: str | pathlib.Path,
    user: str,
    token: str = "",
    auth_mode: str = "basic",
    timeout: int = DEFAULT_TIMEOUT_SECONDS,
) -> None:
    """Faz upload de um arquivo para o JFrog Artifactory.

    Args:
        base_url: URL base do Artifactory (ex.: https://empresa.jfrog.io).
        repo: Repositório no Artifactory.
        dest_folder: Pasta de destino no Artifactory.
        file_path: Caminho local do arquivo para upload.
        user: Usuário do JFrog.
        token: Token/API key. Se vazio, usa JFROG_TOKEN do ambiente.
        auth_mode: Modo de autenticação (auto, basic, bearer, apikey).
        timeout: Timeout da requisição em segundos.

    Raises:
        JFrogUploadError: em caso de erro de validação, comunicação ou upload.
    """
    resolved = pathlib.Path(file_path).expanduser().resolve()
    if not resolved.exists():
        raise JFrogUploadError(f"Arquivo não encontrado: {resolved}")
    if not resolved.is_file():
        raise JFrogUploadError(
            f"O caminho informado não é um arquivo: {resolved}"
        )

    effective_token = token or os.getenv("JFROG_TOKEN", "")
    if not effective_token:
        raise JFrogUploadError(
            "Token não informado. Passe via parâmetro ou defina JFROG_TOKEN."
        )

    upload_url = _build_upload_url(base_url, dest_folder, resolved.name, repo)
    auth, headers, selected_mode = _build_auth(auth_mode, user, effective_token)

    print(f"  URL de upload: {upload_url}")
    print(f"  Autenticação: {selected_mode}")

    try:
        with resolved.open("rb") as file_data:
            response = requests.put(
                upload_url,
                data=file_data,
                auth=auth,
                headers=headers,
                timeout=timeout,
            )
    except RequestException as exc:
        raise JFrogUploadError(
            f"Erro de comunicação com JFrog: {exc}"
        ) from exc

    if response.ok:
        print(f"  Upload concluído com sucesso: {resolved.name}")
        return

    msg = f"Falha no upload. HTTP {response.status_code}"
    if response.status_code == 405:
        msg += (
            "\n  Dica: verifique se a URL final contém "
            "'/artifactory/<repo>/...' e não aponta para endpoint de UI."
        )
    if response.text:
        msg += f"\n  {response.text.strip()}"
    raise JFrogUploadError(msg)
