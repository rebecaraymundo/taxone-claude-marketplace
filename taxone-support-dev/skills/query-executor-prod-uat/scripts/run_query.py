#!/usr/bin/env python3
"""
Orquestrador: empacota uma query SQL, faz upload no JFrog e dispara
o workflow do GitHub Actions para execução em Produção ou UAT.

Uso:
    python run_query.py --query "SELECT 1 FROM DUAL" --empresa ACHE --env uat
    python run_query.py --file minha_query.sql --empresa ACHE --env prod
"""

from __future__ import annotations

import argparse
import os
import pathlib
import sys
import tempfile

import requests
import yaml
from requests.auth import HTTPBasicAuth

from gha_dispatch import GHADispatchError, dispatch_workflow
from jfrog_upload import JFrogUploadError, upload_file
from patch_generator import PatchGeneratorError, generate_patch
from tenant_lookup import find_tenant, validate_environment

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SKILL_ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG_PATH = SKILL_ROOT / "config.yaml"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_config() -> dict:
    """Carrega config.yaml e retorna como dicionário."""
    if not CONFIG_PATH.exists():
        print(
            f"Erro: arquivo de configuração não encontrado: {CONFIG_PATH}",
            file=sys.stderr,
        )
        sys.exit(2)

    with CONFIG_PATH.open(encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)

    if not isinstance(cfg, dict):
        print("Erro: config.yaml está vazio ou mal-formado.", file=sys.stderr)
        sys.exit(2)

    return cfg


def _cleanup_old_files(base_url: str, repo: str, dest_folder: str,
                       user: str, token: str) -> None:
    """Remove arquivos antigos do usuario na pasta do JFrog."""
    api_url = f"{base_url}/artifactory/api/storage/{repo}/{dest_folder}"
    auth = HTTPBasicAuth(user, token)
    resp = requests.get(api_url, auth=auth, timeout=30)
    if not resp.ok:
        print(f"Aviso: nao foi possivel listar arquivos em {dest_folder}")
        return
    children = resp.json().get("children", [])
    prefix = f"{user}_"
    for child in children:
        name = child.get("uri", "").lstrip("/")
        if not child.get("folder", False) and name.startswith(prefix):
            del_url = f"{base_url}/artifactory/{repo}/{dest_folder}/{name}"
            del_resp = requests.delete(del_url, auth=auth, timeout=30)
            status = "OK" if del_resp.ok else f"FALHA ({del_resp.status_code})"
            print(f"  Removido: {name} -> {status}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Orquestra patchgen → jfrogupload → ghadispatch para executar "
            "uma query SQL em Produção ou UAT."
        ),
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--query",
        help="Query SQL inline (entre aspas).",
    )
    group.add_argument(
        "--file",
        help="Caminho de um arquivo .sql ou .txt contendo a query.",
    )

    parser.add_argument(
        "--empresa",
        required=True,
        help="Nome da empresa (ex.: ACHE, FEMSA).",
    )
    parser.add_argument(
        "--env",
        required=True,
        choices=("prod", "uat"),
        help="Ambiente de execução: prod ou uat.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Apenas mostra os passos que seriam executados, sem executar.",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = load_config()

    # ---- Tenant Lookup ----
    print(f"Buscando tenant para empresa '{args.empresa}'...")
    try:
        tenant = find_tenant(args.empresa)
    except (FileNotFoundError, LookupError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2

    try:
        env_identifier = validate_environment(tenant, args.env)
    except ValueError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2

    print(f"  Empresa:    {tenant['empresa']}")
    print(f"  Schema:     {tenant['schema']}")
    print(f"  Ambiente:   {args.env.upper()} -> {env_identifier}")

    # ---- Preparar arquivo SQL ----
    temp_file = None
    if args.query:
        temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".sql",
            delete=False,
            encoding="utf-8",
        )
        temp_file.write(args.query)
        temp_file.close()
        sql_file = temp_file.name
        print(f"\n  Query inline salva em: {sql_file}")
    else:
        sql_file = args.file
        if not pathlib.Path(sql_file).exists():
            print(f"Erro: arquivo não encontrado: {sql_file}", file=sys.stderr)
            return 2

    # ---- Configuração ----
    jfrog_cfg = cfg.get("jfrog", {})
    github_cfg = cfg.get("github", {})
    user_cfg = cfg.get("user", {})

    jfrog_url = jfrog_cfg.get("url", "")
    jfrog_repo = jfrog_cfg.get("repo", "")
    jfrog_dest = jfrog_cfg.get("dest_folder", "")
    jfrog_user = jfrog_cfg.get("user", "")
    jfrog_auth = jfrog_cfg.get("auth_mode", "basic")

    gh_base_url = github_cfg.get(
        "base_url",
        "https://github.com/tr/a202606_mastersafdevops-tools-dbscripts/actions/workflows",
    )
    gh_workflow_suffix = github_cfg.get("workflow_suffix", "querycustom-single.yml")

    user_email = user_cfg.get("email", "")

    # ---- Construir URL do workflow ----
    workflow_url = f"{gh_base_url}/{env_identifier}-{gh_workflow_suffix}"
    print(f"\n  Workflow URL: {workflow_url}")

    if args.dry_run:
        print("\n[DRY RUN] Passos que seriam executados:\n")
        print(f"  1. generate_patch(sql_file=\"{sql_file}\", empresa=\"{tenant['empresa']}\", user=\"{jfrog_user}\")")
        print(f"  2. Limpar arquivos antigos de '{jfrog_user}' em {jfrog_dest}")
        print(f"  3. upload_file(base_url=\"{jfrog_url}\", repo=\"{jfrog_repo}\", "
              f"dest_folder=\"{jfrog_dest}\", file_path=\"<ZIP>\", "
              f"user=\"{jfrog_user}\", auth_mode=\"{jfrog_auth}\")")
        print(f"  4. dispatch_workflow(workflow_url=\"{workflow_url}\", filename=\"<ZIP_NAME>\", "
              f"tenant=\"{tenant['schema']}\", email=\"{user_email}\")")
        print("\n[DRY RUN] Nenhum passo foi executado.")
        return 0

    # ---- Step 1: generate_patch ----
    print(f"\n{'='*60}")
    print("  PASSO 1: Gerar ZIP com patch.sql")
    print(f"{'='*60}\n")
    try:
        zip_path = generate_patch(sql_file, tenant["empresa"], user=jfrog_user)
    except PatchGeneratorError as exc:
        print(f"\nErro no passo 'generate_patch': {exc}", file=sys.stderr)
        return 1
    zip_name = zip_path.name
    print(f"  ZIP gerado: {zip_path}")

    # ---- Step 2: Limpar arquivos antigos do usuario no JFrog ----
    jfrog_token = os.environ.get("JFROG_TOKEN", "")
    if jfrog_token:
        print(f"\n{'='*60}")
        print("  PASSO 2: Limpar arquivos antigos do usuario no JFrog")
        print(f"{'='*60}\n")
        _cleanup_old_files(jfrog_url, jfrog_repo, jfrog_dest,
                           jfrog_user, jfrog_token)
    else:
        print("Aviso: JFROG_TOKEN nao definido, pulando limpeza de arquivos antigos.")

    # ---- Step 3: upload_file ----
    print(f"\n{'='*60}")
    print("  PASSO 3: Upload do ZIP para Artifactory")
    print(f"{'='*60}\n")
    try:
        upload_file(
            base_url=jfrog_url,
            repo=jfrog_repo,
            dest_folder=jfrog_dest,
            file_path=zip_path,
            user=jfrog_user,
            token=jfrog_token,
            auth_mode=jfrog_auth,
        )
    except JFrogUploadError as exc:
        print(f"\nErro no passo 'upload_file': {exc}", file=sys.stderr)
        return 1

    # ---- Remover ZIP local após upload bem-sucedido ----
    try:
        zip_path.unlink()
        print(f"  ZIP local removido: {zip_path}")
    except OSError as exc:
        print(f"  Aviso: não foi possível remover o ZIP local: {exc}")

    # ---- Step 4: dispatch_workflow ----
    print(f"\n{'='*60}")
    print("  PASSO 4: Disparar workflow no GitHub Actions")
    print(f"{'='*60}\n")
    try:
        dispatch_workflow(
            workflow_url=workflow_url,
            filename=zip_name,
            tenant=tenant["schema"],
            email=user_email,
        )
    except GHADispatchError as exc:
        print(f"\nErro no passo 'dispatch_workflow': {exc}", file=sys.stderr)
        return 1

    # ---- Limpeza ----
    if temp_file:
        try:
            pathlib.Path(temp_file.name).unlink()
        except OSError:
            pass

    print(f"\n{'='*60}")
    print("  CONCLUÍDO COM SUCESSO!")
    print(f"  Empresa:   {tenant['empresa']}")
    print(f"  Schema:    {tenant['schema']}")
    print(f"  Ambiente:  {args.env.upper()} ({env_identifier})")
    print(f"  Workflow:  {workflow_url}")
    print(f"  Arquivo:   {zip_name}")
    print(f"{'='*60}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
