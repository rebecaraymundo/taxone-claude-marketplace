---
name: query-executor-prod-uat
description: Execute SQL queries on Production or UAT environments. Use when the user mentions running a query on prod, uat, production, or homologation for a client/empresa.
---

# Query Executor

## When to Use

Use this skill when the user:
- Wants to **execute a SQL query** on a client's Production or UAT environment
- Asks to **dispatch a custom query workflow** for a specific empresa
- Mentions running a query on **prod** or **uat** for a client
- Asks to send a SQL file or inline query to an environment

### Examples that SHOULD trigger this skill

- "Executa essa query em UAT para a ACHE: SELECT * FROM DUAL"
- "Roda esse SQL em prod para a FEMSA"
- "Envia essa query para produção da BMW"
- "Dispara essa consulta no ambiente de homologação da RAIZEN"
- "Preciso rodar um SELECT na ACHE em uat"
- "Manda esse arquivo .sql para o ambiente prod da MRV"

### Examples that should NOT trigger this skill

- "Me ajuda a montar uma query SQL" (no prod/uat environment mentioned)
- "Qual a estrutura da tabela X?" (database inspection, not deployment)
- "Executa essa query no banco local" (no reference to prod/uat)
- "Cria um script PL/SQL" (development, not deployment)

## Prerequisites

Environment variables required:
- `JFROG_TOKEN` - JFrog Artifactory authentication token
- `GITHUB_TOKEN` - GitHub token with workflow dispatch permission

Configuration file: `config.yaml` (in this skill's root directory) must have `jfrog.user` and `user.email` filled in.

## REGRA OBRIGATORIA: Validar Schema ANTES de Despachar

**NUNCA despachar uma query sem antes validar que TODAS as colunas e tabelas existem.**

Antes de chamar `run_query.py`, executar OBRIGATORIAMENTE:

1. Para cada tabela na query, verificar colunas em `knowledge/schema/COLUMN_GLOSSARY.md` ou `knowledge/schema/tables_{PREFIXO}.md`
2. Usar `grep -i "NOME_COLUNA" knowledge/schema/COLUMN_GLOSSARY.md` para confirmar existencia
3. Se a coluna nao for encontrada, buscar alternativas no glossario antes de montar a query

**Exemplos de erros comuns a evitar:**
- `DWT_DOCTO_FISCAL.NUM_DOCTO` NAO existe → o correto e `NUM_DOCFIS`
- `PRT_VALIDADOR.DESCRICAO` NAO existe → usar apenas colunas confirmadas no schema
- `PRT_NOTA_C_S_RETENCAO.IND_ISS_RETIDO` NAO existe → verificar nome real da coluna

**Motivo:** Queries remotas demoram ~5 min para executar via GitHub Actions. Cada erro de coluna (ORA-00904) gasta um ciclo inteiro de retrabalho. Validar antes custa segundos e evita minutos de espera.

---

## How to Execute

### Option A: Automated (orchestrator script)

Run the orchestrator script that handles all steps automatically:

```bash
# With inline query
python "${CLAUDE_PLUGIN_ROOT}/skills/query-executor-prod-uat/scripts/run_query.py" --query "SELECT * FROM DUAL" --empresa ACHE --env uat

# With SQL file
python "${CLAUDE_PLUGIN_ROOT}/skills/query-executor-prod-uat/scripts/run_query.py" --file "/path/to/query.sql" --empresa ACHE --env prod

# Dry run (show commands without executing)
python "${CLAUDE_PLUGIN_ROOT}/skills/query-executor-prod-uat/scripts/run_query.py" --query "SELECT 1 FROM DUAL" --empresa ACHE --env uat --dry-run
```

> **Nota**: `${CLAUDE_PLUGIN_ROOT}` resolve para o diretorio raiz do projeto taxone-support-dev.
> Se `python` nao estiver no PATH, use o caminho completo do seu interpretador Python 3.10+.

### Internal Pipeline Steps

The orchestrator (`run_query.py`) executes the following steps via direct module imports (no external CLIs needed):

1. **Tenant Lookup** - Searches `resources/TENANT_LOOKUP_*.txt` for the empresa to resolve schema and environment identifiers.
2. **Generate Patch ZIP** - Calls `patch_generator.generate_patch()` to create a ZIP with `patch.sql` (header + sanitized query). Output: `{user}_{empresa}_{timestamp}.zip`.
3. **Cleanup Old Files** - Removes previous ZIPs from the user in the JFrog destination folder.
4. **Upload to JFrog** - Calls `jfrog_upload.upload_file()` to PUT the ZIP to Artifactory.
5. **Dispatch Workflow** - Calls `gha_dispatch.dispatch_workflow()` to trigger the GitHub Actions workflow via REST API.

## Input Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| query     | Yes*     | Inline SQL query (mutually exclusive with file) |
| file      | Yes*     | Path to .sql or .txt file with the query |
| empresa   | Yes      | Client/empresa name (e.g., ACHE, FEMSA, BMW) |
| env       | Yes      | Target environment: `prod` or `uat` |

## Configuration Reference

See `config.yaml` in the skill root directory for all configurable values:
- **jfrog.url** - JFrog Artifactory base URL
- **jfrog.repo** - JFrog repository name
- **jfrog.dest_folder** - Destination folder in Artifactory
- **jfrog.user** - JFrog username
- **jfrog.auth_mode** - Authentication mode (default: basic)
- **github.base_url** - Base GitHub workflow URL
- **github.workflow_suffix** - Workflow file suffix
- **user.email** - Email for result notifications

## Directory Structure

```
query-executor-prod-uat/
  SKILL.md              -- This file
  config.yaml           -- User configuration
  resources/
    TENANT_LOOKUP.txt    -- Empresa/schema/environment mapping
  scripts/
    run_query.py         -- Main orchestrator
    tenant_lookup.py     -- Tenant search helper
    patch_generator.py   -- Generates patch.sql ZIP
    jfrog_upload.py      -- Uploads files to JFrog Artifactory
    gha_dispatch.py      -- Dispatches GitHub Actions workflows
```
