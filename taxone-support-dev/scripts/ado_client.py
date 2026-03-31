"""
ado_client — Modulo centralizado para autenticacao e chamadas ao Azure DevOps REST API.

Consolida auth (PAT + Bearer fallback) e constantes ADO usados por multiplos scripts.

Uso:
    from ado_client import get_auth_header, ado_get, ado_post, ado_patch
    from ado_client import ADO_BASE, ADO_API_VERSION

    # Buscar WI
    wi = ado_get(f"{ADO_BASE}/wit/workitems/1058668?{ADO_API_VERSION}")

    # WIQL
    result = ado_post(f"{ADO_BASE}/wit/wiql?{ADO_API_VERSION}", {"query": "SELECT ..."})

    # Patch WI
    ado_patch(f"{ADO_BASE}/wit/workitems/1058668?{ADO_API_VERSION}", [
        {"op": "add", "path": "/fields/System.Tags", "value": "SUST-IA-CLAUDE"}
    ])
"""

import base64
import json
import os
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

# ── Constantes ADO ──────────────────────────────────────────────────────────

ADO_ORG = "tr-ggo"
ADO_PROJECT = "Mastersaf Fiscal Solutions"
ADO_PROJECT_ENC = urllib.parse.quote(ADO_PROJECT, safe="")
ADO_BASE = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT_ENC}/_apis"
ADO_API_VERSION = "api-version=7.1"

_PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ── Auth ────────────────────────────────────────────────────────────────────

def get_ado_pat() -> str:
    """Retorna ADO PAT: env var > .env > string vazia."""
    pat = os.environ.get("ADO_PAT", "")
    if pat:
        return pat

    env_file = _PROJECT_ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("ADO_PAT="):
                pat = line.partition("=")[2].strip().strip('"').strip("'")
                break
    return pat


def get_az_bearer_token() -> str:
    """Tenta obter bearer token via az CLI (Azure Identity)."""
    try:
        result = subprocess.run(
            ["az", "account", "get-access-token",
             "--resource", "499b84ac-1321-427f-aa17-267ca6975798",
             "--query", "accessToken", "-o", "tsv"],
            capture_output=True, text=True, timeout=15,
            shell=(os.name == "nt"),
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return ""


def get_auth_header(content_type: str = "application/json") -> dict:
    """Retorna headers com Authorization.

    Prioridade: Bearer (az CLI) > Basic (PAT).

    Args:
        content_type: Content-Type header (default: application/json)

    Returns:
        dict com Authorization e Content-Type
    """
    # Tentar Bearer (az CLI) primeiro
    bearer = get_az_bearer_token()
    if bearer:
        return {
            "Authorization": f"Bearer {bearer}",
            "Content-Type": content_type,
        }

    # Fallback: PAT (Basic)
    pat = get_ado_pat()
    if pat:
        auth = base64.b64encode(f":{pat}".encode()).decode()
        return {
            "Authorization": f"Basic {auth}",
            "Content-Type": content_type,
        }

    return {"Content-Type": content_type}


def get_auth_headers_multi() -> dict:
    """Retorna dict de headers para diferentes content types.

    Returns:
        dict com chaves 'json', 'json_patch', 'octet', cada uma com headers completos.
    """
    # Resolver auth uma vez
    bearer = get_az_bearer_token()
    if bearer:
        auth_value = f"Bearer {bearer}"
    else:
        pat = get_ado_pat()
        if pat:
            auth_value = f"Basic {base64.b64encode(f':{pat}'.encode()).decode()}"
        else:
            auth_value = ""

    return {
        "json": {
            "Content-Type": "application/json",
            "Authorization": auth_value,
        },
        "json_patch": {
            "Content-Type": "application/json-patch+json",
            "Authorization": auth_value,
        },
        "octet": {
            "Content-Type": "application/octet-stream",
            "Authorization": auth_value,
        },
    }


# ── HTTP helpers (urllib, sem dependencia de requests) ──────────────────────

def ado_get(url: str, headers: dict = None) -> dict:
    """GET request ao ADO API.

    Args:
        url: URL completa (incluir api-version como query param)
        headers: Headers customizados (se None, usa get_auth_header())

    Returns:
        dict com resposta JSON
    """
    if headers is None:
        headers = get_auth_header()
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def ado_post(url: str, body: dict, headers: dict = None) -> dict:
    """POST request ao ADO API.

    Args:
        url: URL completa
        body: dict serializado como JSON
        headers: Headers customizados (se None, usa get_auth_header())

    Returns:
        dict com resposta JSON
    """
    if headers is None:
        headers = get_auth_header()
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def ado_patch(url: str, operations: list, headers: dict = None) -> dict:
    """PATCH request ao ADO API (JSON Patch).

    Args:
        url: URL completa
        operations: lista de operacoes JSON Patch
        headers: Headers customizados (se None, usa json-patch+json)

    Returns:
        dict com resposta JSON
    """
    if headers is None:
        headers = get_auth_header(content_type="application/json-patch+json")
    data = json.dumps(operations).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="PATCH")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def ado_upload(url: str, file_bytes: bytes, headers: dict = None) -> dict:
    """Upload binario ao ADO API (octet-stream).

    Args:
        url: URL completa (ex: attachment upload)
        file_bytes: conteudo binario
        headers: Headers customizados (se None, usa octet-stream)

    Returns:
        dict com resposta JSON
    """
    if headers is None:
        headers = get_auth_header(content_type="application/octet-stream")
    req = urllib.request.Request(url, data=file_bytes, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))
