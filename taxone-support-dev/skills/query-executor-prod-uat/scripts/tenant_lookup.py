#!/usr/bin/env python3
"""
Módulo auxiliar para busca de tenant (empresa) nos arquivos TENANT_LOOKUP.

Formato dos arquivos:
    EMPRESA|SCHEMA|PROD|UAT

Exemplo:
    ACHE|USER_TAXONE_ACHE|taxoneprod2|taxoneuat2
"""

from __future__ import annotations

import pathlib
from typing import TypedDict


class TenantInfo(TypedDict):
    empresa: str
    schema: str
    prod: str
    uat: str


def find_tenant(
    empresa: str,
    resources_dir: str | pathlib.Path | None = None,
) -> TenantInfo:
    """Busca uma empresa nos arquivos TENANT_LOOKUP_*.txt.

    Args:
        empresa: Nome da empresa (case-insensitive).
        resources_dir: Diretório contendo os arquivos TENANT_LOOKUP_*.txt.
            Se ``None``, usa a pasta ``resources`` ao lado da pasta ``scripts``.

    Returns:
        Dicionário com empresa, schema, prod e uat.

    Raises:
        FileNotFoundError: Se nenhum arquivo TENANT_LOOKUP_*.txt for encontrado.
        LookupError: Se a empresa não for encontrada.
    """
    if resources_dir is None:
        resources_dir = pathlib.Path(__file__).resolve().parent.parent / "resources"
    else:
        resources_dir = pathlib.Path(resources_dir)

    # Aceita arquivo único (TENANT_LOOKUP.txt) ou múltiplos (TENANT_LOOKUP_*.txt)
    lookup_files = sorted(resources_dir.glob("TENANT_LOOKUP*.txt"))
    if not lookup_files:
        raise FileNotFoundError(
            f"Nenhum arquivo TENANT_LOOKUP*.txt encontrado em {resources_dir}"
        )

    empresa_upper = empresa.strip().upper()

    for lf in lookup_files:
        for line in lf.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            # Ignora linhas vazias e comentários
            if not line or line.startswith("#"):
                continue

            parts = line.split("|")
            if len(parts) < 4:
                continue

            if parts[0].strip().upper() == empresa_upper:
                return TenantInfo(
                    empresa=parts[0].strip(),
                    schema=parts[1].strip(),
                    prod=parts[2].strip(),
                    uat=parts[3].strip(),
                )

    raise LookupError(
        f"Empresa '{empresa}' não encontrada nos arquivos de tenant lookup."
    )


def validate_environment(tenant: TenantInfo, env: str) -> str:
    """Valida que o ambiente solicitado está disponível para o tenant.

    Args:
        tenant: Informações do tenant retornadas por ``find_tenant``.
        env: Ambiente desejado (``prod`` ou ``uat``).

    Returns:
        Identificador do ambiente (ex: ``taxoneprod2``, ``taxoneuat``).

    Raises:
        ValueError: Se o ambiente não estiver disponível para a empresa.
    """
    env_lower = env.strip().lower()
    if env_lower not in ("prod", "uat"):
        raise ValueError(f"Ambiente inválido: '{env}'. Use 'prod' ou 'uat'.")

    env_value = tenant[env_lower]  # type: ignore[literal-required]
    if not env_value:
        raise ValueError(
            f"Empresa '{tenant['empresa']}' não possui ambiente "
            f"'{env_lower.upper()}' configurado."
        )

    # Quando há múltiplos ambientes separados por vírgula, usa o primeiro
    return env_value.split(",")[0].strip()
