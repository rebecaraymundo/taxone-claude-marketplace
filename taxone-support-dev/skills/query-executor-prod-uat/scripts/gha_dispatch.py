"""
Módulo para disparar um workflow do GitHub Actions via API REST.

Uso como módulo:
    from gha_dispatch import dispatch_workflow
    dispatch_workflow(
        workflow_url="https://github.com/owner/repo/actions/workflows/wf.yml",
        filename="patch.zip",
        tenant="USER_TAXONE_ACHE",
        email="user@example.com",
        token="ghp_xxx",
    )
"""

from __future__ import annotations

import os
import re
from typing import Final

import requests
from requests.exceptions import RequestException

DEFAULT_TIMEOUT_SECONDS: Final[int] = 30
DEFAULT_REF: Final[str] = "main"

# Regex para extrair owner, repo e workflow_file a partir da URL do GitHub.
_URL_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)"
    r"/actions/workflows/(?P<workflow>[^/]+\.ya?ml)",
    re.IGNORECASE,
)


class GHADispatchError(Exception):
    """Erro genérico do dispatch de workflow."""


def _parse_workflow_url(url: str) -> tuple[str, str, str]:
    """Extrai owner, repo e workflow_file de uma URL do GitHub Actions.

    Returns:
        Tupla (owner, repo, workflow_file).

    Raises:
        GHADispatchError: se a URL não corresponder ao formato esperado.
    """
    match = _URL_PATTERN.match(url.strip())
    if not match:
        raise GHADispatchError(
            "URL inválida. Formato esperado: "
            "https://github.com/<owner>/<repo>/actions/workflows/<workflow>.yml"
        )
    return match.group("owner"), match.group("repo"), match.group("workflow")


def dispatch_workflow(
    workflow_url: str,
    filename: str,
    tenant: str = "",
    email: str = "",
    token: str = "",
    ref: str = DEFAULT_REF,
    timeout: int = DEFAULT_TIMEOUT_SECONDS,
) -> None:
    """Dispara um workflow do GitHub Actions via API REST.

    Args:
        workflow_url: URL completa do workflow no GitHub.
        filename: Valor do input FileName do workflow.
        tenant: Valor do input SchemaName (opcional).
        email: Valor do input EmailToSend (opcional).
        token: Token do GitHub. Se vazio, usa GITHUB_TOKEN do ambiente.
        ref: Branch ou tag para execução (padrão: main).
        timeout: Timeout da requisição em segundos.

    Raises:
        GHADispatchError: em caso de erro de validação, comunicação ou dispatch.
    """
    effective_token = token or os.getenv("GITHUB_TOKEN", "")
    if not effective_token:
        raise GHADispatchError(
            "Token não informado. Passe via parâmetro ou defina GITHUB_TOKEN."
        )

    owner, repo, workflow_file = _parse_workflow_url(workflow_url)

    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}"
        f"/actions/workflows/{workflow_file}/dispatches"
    )

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {effective_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    inputs: dict[str, str] = {"FileName": filename}
    if tenant:
        inputs["SchemaName"] = tenant
    if email:
        inputs["EmailToSend"] = email

    payload = {"ref": ref, "inputs": inputs}

    print(f"  Repositório: {owner}/{repo}")
    print(f"  Workflow:    {workflow_file}")
    print(f"  Branch/Ref:  {ref}")
    print(f"  FileName:    {filename}")
    if tenant:
        print(f"  Tenant:      {tenant}")
    if email:
        print(f"  Email:       {email}")

    try:
        response = requests.post(
            api_url,
            json=payload,
            headers=headers,
            timeout=timeout,
        )
    except RequestException as exc:
        raise GHADispatchError(
            f"Erro de comunicação com GitHub: {exc}"
        ) from exc

    # HTTP 204 = sucesso (sem corpo de resposta)
    if response.status_code == 204:
        print("  Workflow disparado com sucesso.")
        return

    msg = f"Falha ao disparar o workflow. HTTP {response.status_code}"
    if response.status_code == 404:
        msg += (
            "\n  Dica: verifique se o repositório e o workflow existem "
            "e se o token possui permissão de acesso."
        )
    elif response.status_code == 422:
        msg += (
            "\n  Dica: verifique se a branch/ref informada existe "
            "e se os inputs do workflow estão corretos."
        )
    if response.text:
        msg += f"\n  {response.text.strip()}"
    raise GHADispatchError(msg)
