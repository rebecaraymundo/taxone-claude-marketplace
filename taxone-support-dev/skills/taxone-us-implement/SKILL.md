---
name: taxone-us-implement
description: >
  Pipeline automatizado de implementacao de Features e User Stories do Azure DevOps para o TAX ONE.
  Orientado a requisitos: analisa escopo, formaliza regras de negocio, projeta solucao arquitetural,
  implementa codigo novo, valida cobertura de regras, executa testes e cria PR no GitHub.
  Totalmente separado do fluxo de bugs (taxone-auto-fix / taxone-bug-fix).
version: 1.0.0
---

# TAX ONE - Pipeline de Implementacao de Features / User Stories

Pipeline orquestrado para implementacao end-to-end de **Features e User Stories** do Azure DevOps
no projeto TAX ONE (Mastersaf Fiscal Solutions) da Thomson Reuters.

**Diferenca fundamental do bug fix:** Este pipeline pergunta "Qual o escopo e quais as regras?"
em vez de "O que esta quebrado?". O PM faz analise de escopo (nao triage de bug), as regras
de negocio sao formalizadas antes da implementacao, e o developer cria codigo novo seguindo
o design spec — nao corrige codigo existente.

---

## Indice

1. [Configuracao](#configuracao)
2. [Regras (R1-R6)](#regras)
3. [Regra de Visibilidade do Knowledge](#regra-de-visibilidade-do-knowledge)
4. [Pipeline - Visao Geral](#pipeline---visao-geral)
5. [Phase 0 - Resolver Variaveis e Buscar Work Item](#phase-0---resolver-variaveis-e-buscar-work-item)
6. [Phase 0.5 - Buscar Work Items via Query](#phase-05---buscar-work-items-via-query)
7. [Phase 0.6 - Enriquecer com Zendesk](#phase-06---enriquecer-com-zendesk)
8. [Phase 0.7 - Enriquecer com Datadog](#phase-07---enriquecer-com-datadog)
9. [Phase 0.9 - SM Allocation Check](#phase-09---sm-allocation-check)
10. [Phase 1 - Analise de Escopo PM](#phase-1---analise-de-escopo-pm)
11. [Phase 1.5 - Analise de Regras de Negocio](#phase-15---analise-de-regras-de-negocio)
12. [Phase 1.6 - Pre-Dev Validation Scripts](#phase-16---pre-dev-validation-scripts-cenarios-executaveis-para-o-dev)
13. [Phase 2 - Design Arquitetural](#phase-2---design-arquitetural)
13. [Phase 2.5 - Analise DBA Oracle](#phase-25---analise-dba-oracle)
14. [Phase 3 - Workspace e Branch](#phase-3---workspace-e-branch)
15. [Phase 4 - Implementacao](#phase-4---implementacao)
16. [Phase 4.5 - Verificacao de Cobertura de Regras](#phase-45---verificacao-de-cobertura-de-regras)
17. [Phase 5 - Testes SQL de Validacao](#phase-5---testes-sql-de-validacao)
18. [Phase 5.5 - Testes de Regressao SuiteAutomation](#phase-55---testes-de-regressao-suiteautomation)
19. [Phase 5.7 - Testes E2E Playwright](#phase-57---testes-e2e-playwright)
20. [Phase 6 - Code Review](#phase-6---code-review)
21. [Phase 7 - Commit, Push e PR](#phase-7---commit-push-e-pr)
22. [Phase 7.5 - Pacote Unitario (GitHub Actions)](#phase-75---pacote-unitario-github-actions)
23. [Phase 8 - Atualizar ADO e Relatorio Final](#phase-8---atualizar-ado-e-relatorio-final)
24. [Phase 9 - Compound Engineering](#phase-9---compound-engineering)
25. [Tratamento de Erros](#tratamento-de-erros)

---

## Configuracao

### Variaveis de Ambiente (Obrigatorias)

| Variavel      | Descricao                                        | Exemplo                                          |
|---------------|--------------------------------------------------|--------------------------------------------------|
| `ADO_PAT`     | Personal Access Token do Azure DevOps            | `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`    |
| `GITHUB_TOKEN`| Token do GitHub (para `gh` CLI)                  | Configurado via `gh auth login`                   |
| `ZENDESK_URL` | URL base da instancia Zendesk                    | `https://atendimentotr.zendesk.com`               |
| `ZENDESK_EMAIL`| Email do usuario Zendesk                        | `user@thomsonreuters.com`                         |
| `ZENDESK_TOKEN`| API Token do Zendesk                            | `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`    |

### Constantes do Pipeline

| Constante              | Valor                                                                 |
|------------------------|-----------------------------------------------------------------------|
| ADO Org                | `tr-ggo`                                                              |
| ADO Project            | `Mastersaf Fiscal Solutions` (URL: `Mastersaf%20Fiscal%20Solutions`)   |
| ADO API Version        | `api-version=7.1`                                                     |
| ADO Base URL           | `https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions`         |
| Area Path              | `Mastersaf Fiscal Solutions\MFS\TAX ONE\Suporte`                      |
| Tag AI                 | `AI-Implemented`                                                      |
| Tag CLAUDE             | `SUST-IA-CLAUDE`                                                      |
| Tag REGRA              | `SUST-IA-CLAUDE-REGRA`                                                |
| Tag ANALISE            | `SUST-IA-CLAUDE-ANALISE`                                              |
| InternalCom field      | `Custom.Solutions`                                                    |
| DevReviewName field    | `Custom.DeveloperText`                                                |
| AcceptanceCriteria field | `Microsoft.VSTS.Common.AcceptanceCriteria`                          |
| ReleaseNotes field     | `Custom.DescriptionofReleaseNotes`                                    |
| RootCause field        | `Custom.DescriptionofRootCause`                                       |
| DD Org                 | `trta-onesource` (via MCP Server `datadog`, auth OAuth)               |
| DD MCP Server          | `datadog` (remote HTTP, `~/.claude.json` mcpServers)                  |
| DD Permissao           | MCP Read (somente leitura)                                            |
| PR Target Branch       | `DEV`                                                                 |
| Branch Pattern         | `MFS{work-item-id}`                                                   |
| Commit Title Pattern   | `[DEV] MFS{work-item-id} - {descricao curta}`                        |
| Commit Body Last Line  | `AB#{work-item-id}`                                                   |

### Agentes Permitidos

| Agente              | Funcao                                         | Fase          |
|---------------------|-------------------------------------------------|---------------|
| `taxone-pm`         | Analise de escopo e extracao de regras          | Phase 1       |
| `taxone-architect`  | Formalizacao de regras + Design arquitetural    | Phase 1.5, 2  |
| `taxone-dba`        | Analise de impacto Oracle/DBA                   | Phase 2.5     |
| `taxone-plsql`      | Implementacao PL/SQL (packages, procedures, views) | Phase 4    |
| `taxone-pb`         | Implementacao PowerBuilder (DataWindows, scripts)   | Phase 4    |
| `taxone-java`       | Implementacao Java (web services, Jasper, servlets) | Phase 4    |
| `taxone-tester`     | Scripts SQL de validacao e testes manuais       | Phase 5       |
| `taxone-suite-runner`| Testes de regressao SuiteAutomation            | Phase 5.5     |
| `taxone-e2e-tester` | Testes E2E Playwright (browser)                 | Phase 5.7     |
| `taxone-plsql-reviewer` | Code review PL/SQL Oracle                   | Phase 6       |
| `taxone-pb-reviewer`    | Code review PowerBuilder                    | Phase 6       |
| `taxone-java-reviewer`  | Code review Java                            | Phase 6       |
| `taxone-angular`    | Implementacao + Review Angular 11 frontend      | Phase 4, 6    |
| `taxone-sm`         | Alocacao avulsa de Dev/Tester por afinidade     | Phase 0.9     |

### Caminhos do Knowledge

| Caminho                                                | Conteudo                              |
|--------------------------------------------------------|---------------------------------------|
| `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/`        | Visao geral, tech stack, patterns     |
| `${CLAUDE_PLUGIN_ROOT}/knowledge/features/`            | Knowledge por feature/modulo          |
| `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/`         | Padroes de codigo, nomenclatura       |
| `${CLAUDE_PLUGIN_ROOT}/knowledge/business-rules/`      | Regras de negocio por modulo          |
| `${CLAUDE_PLUGIN_ROOT}/knowledge/webhelp/`             | Artigos do Help Center                |
| `${CLAUDE_PLUGIN_ROOT}/knowledge/schema/`              | Schema do banco (tabelas, FKs, etc.)  |

### Protocolo de Consulta Remota (Prod/UAT)

Quando qualquer fase do pipeline detectar que faltam dados do ambiente do cliente
(producao ou UAT) para prosseguir, o orquestrador pode despachar queries SELECT
para execucao remota via GitHub Actions.

#### Constantes

| Constante | Valor |
|-----------|-------|
| **QUERY_SCRIPT_PATH** | `skills/query-executor-prod-uat/scripts/run_query.py` |
| **EMPRESA_RESOLVER_PATH** | `scripts/empresa_resolver.py` |
| **DEFAULT_ENV** | `uat` |
| **TAG_QUERY_DESPACHADA** | `SUST-IA-CLAUDE-ANALISE` |

#### Regras de Seguranca

1. **Somente SELECT** — Validar que a query NAO contem DML/DDL (INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, TRUNCATE, MERGE) antes de despachar. Se contiver, abortar com erro.
2. **Default UAT** — Sempre usar `--env uat` a menos que o usuario confirme explicitamente que precisa de `--env prod`.
3. **Confirmacao obrigatoria** — SEMPRE apresentar ao usuario a query, empresa e ambiente antes de executar. Aguardar confirmacao via `AskUserQuestion`.
4. **Empresa validada** — Deve existir no TENANT_LOOKUP.txt. Se nao encontrada, perguntar ao usuario.
5. **Sem credenciais no state file** — `pipeline_state.json` NUNCA armazena tokens ou senhas.

#### Fluxo de Despacho de Query

```
1. Agente detecta que faltam dados do cliente
2. Agente sugere queries SELECT no output estruturado
3. Orquestrador executa empresa_resolver.py para identificar a empresa
4. Se 0 matches → perguntar empresa ao usuario
5. Se multiplos matches → apresentar opcoes para escolha
6. Apresentar ao usuario: empresa, ambiente (default UAT), query(s)
7. Aguardar confirmacao do usuario
8. Executar: python {QUERY_SCRIPT_PATH} --query "SELECT ..." --empresa {EMPRESA} --env {ENV}
9. Documentar na WI (Custom.Solutions) + tags
10. Salvar pipeline_state.json
11. PAUSAR pipeline
```

---

## Regras

### R1 - Ferramentas Permitidas no Orquestrador

O orquestrador (esta skill) so pode usar:
- **Read** - Leitura de arquivos (knowledge, configuracoes)
- **Bash** - APENAS para: `curl` (ADO API), `git`, `gh` (GitHub CLI), comandos de ambiente
- **Agent** - Para lancar subagentes (APENAS os agentes listados na tabela de Agentes Permitidos)
- **AskUserQuestion** - Para interagir com o usuario (confirmacoes, selecoes)

**PROIBIDO no orquestrador:**
- Write, Edit, Glob, Grep (sao ferramentas dos subagentes)
- Qualquer implementacao direta de codigo
- Qualquer analise direta de codigo (delegar para agentes)

### R2 - Delegacao Obrigatoria

| Tarefa                          | Agente Obrigatorio    |
|---------------------------------|-----------------------|
| Analise de escopo               | `taxone-pm`           |
| Formalizacao de regras          | `taxone-architect`    |
| Analise arquitetural            | `taxone-architect`    |
| Analise de impacto Oracle/DBA   | `taxone-dba`          |
| Implementacao PL/SQL            | `taxone-plsql`        |
| Implementacao PowerBuilder      | `taxone-pb`           |
| Implementacao Java              | `taxone-java`         |
| Implementacao frontend Angular  | `taxone-angular`      |
| Criacao de scripts de teste     | `taxone-tester`       |
| Code review PL/SQL              | `taxone-plsql-reviewer` |
| Code review PowerBuilder        | `taxone-pb-reviewer`  |
| Code review Java                | `taxone-java-reviewer`|
| Code review Angular             | `taxone-angular`      |

O orquestrador NUNCA executa estas tarefas diretamente. Sempre delega via Agent.

### R3 - Integridade do ADO

- Toda chamada a API do ADO DEVE usar o header: `-H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)"`
- Toda atualizacao do work item DEVE usar PATCH com Content-Type `application/json-patch+json`
- NUNCA alterar campos que nao sao de responsabilidade do pipeline
- Campos que o pipeline atualiza:
  - `System.Tags` (adicionar tags: `SUST-IA-CLAUDE`, `AI-Implemented`, `SUST-IA-CLAUDE-REGRA`)
  - `Custom.Solutions` (relatorio interno)
  - `Custom.DeveloperText` (nome do reviewer)
  - `System.State` (transicao de estado, quando aplicavel)
  - `System.AssignedTo` (alocacao de dev, se aprovado pelo usuario)
  - `Microsoft.VSTS.Common.AcceptanceCriteria` (criterios de aceitacao)
  - `Custom.DescriptionofReleaseNotes` (descricao para release notes — **NAO sobrescrever se ja preenchido**)
  - `Custom.DescriptionofRootCause` (causa raiz / descricao da feature)
  - Discussion comments (relatorio completo do pipeline)

### R4 - Controle de Branch e PR

- Branch SEMPRE segue o pattern: `MFS{work-item-id}`
  - Exemplo: `MFS1058668`
  - Para correcoes adicionais na mesma WI: `MFS{work-item-id}a`, `MFS{work-item-id}b`, etc.
- Base branch: `DEV` (verificar se existe, senao usar `main`)
- Target branch do PR: SEMPRE `DEV`
- PR criado via `gh pr create` (GitHub CLI) — **NUNCA fazer merge**
- Titulo do commit/PR: `[DEV] MFS{work-item-id} - {descricao curta}`
- Body do commit: ultima linha DEVE ser `AB#{work-item-id}`

### R5 - Nao Existe Build Local

O TAX ONE e um sistema PL/SQL/PowerBuilder/Java. **NAO existe processo de build/compilacao local.**
- NAO tentar rodar `mvn`, `gradle`, `make`, `npm` ou qualquer build tool
- NAO tentar compilar PL/SQL localmente (compilacao ocorre no Oracle Server porta 1521)
- NAO tentar compilar PowerBuilder localmente
- Validacao de codigo e feita por: analise estatica (reviewer) + scripts SQL de validacao (tester)
- **PL/SQL DEVE ser compilado no banco (porta 1521) ANTES de testes** via `taxone-dba`

### R6 - Comunicacao em Portugues

- Toda comunicacao com o usuario DEVE ser em portugues brasileiro
- Mensagens de log/progresso do pipeline em portugues
- Comentarios no ADO em portugues
- Mensagens de commit e PR em portugues
- Codigo-fonte segue o idioma do projeto (portugues para comentarios, ingles para nomes tecnicos)

### R7 - Testes OBRIGATORIOS Antes da PR

**NUNCA pular as fases de teste (Phase 5, 5.5, 5.7) e ir direto para a PR (Phase 7).**
Compilar NAO e testar. A sequencia obrigatoria e:

1. **Compilar** (Phase 4 / DBA) — objetos VALID no banco
2. **Evidencia ANTES** — capturar comportamento atual (query, screenshot, output) ANTES da alteracao
3. **Testes SQL de validacao** (Phase 5 / taxone-tester) — cenarios base + alteracao + nao-regressao
4. **Evidencia DEPOIS** — capturar comportamento corrigido APOS a alteracao, comparando com o ANTES
5. **SuiteAutomation** (Phase 5.5 / taxone-suite-runner) — regressao automatizada
6. **Salvar artefatos** em `tests/{WI_ID}/` (incluindo evidencias antes/depois)
7. **Upload Attachments** na WI do ADO
8. **Discussion comment** com resultados de testes (incluindo comparativo antes x depois)
9. **Code review** (Phase 6) — APROVADO obrigatorio
10. **Somente entao**: Commit + Push + PR (Phase 7)
11. **Criar Tasks QA** — executar `qa_task_creator.py --wi-id {WI_ID}` para criar Tasks filhas [QA]

**Evidencias Antes/Depois:**
- ANTES: Capturar resultado da query/tela/funcionalidade SEM a correcao (antes de compilar o objeto alterado)
- DEPOIS: Capturar o mesmo cenario COM a correcao aplicada
- Salvar ambas em `tests/{WI_ID}/evidencia_ANTES_{WI_ID}.html` e `tests/{WI_ID}/evidencia_DEPOIS_{WI_ID}.html`
- Formato: HTML com tabelas estilizadas (o `qa_task_creator.py` embute no Description da Task QA)
- Fallback: `.md` e aceito (`evidencia_antes.md` / `evidencia_depois.md`) — convertido automaticamente para HTML
- O comparativo deve estar visivel no Discussion comment da WI para o QA validar
- **Se a alteracao modifica campos em tela**: executar tambem teste de regressao visual (screenshot antes/depois da tela)

Se qualquer fase de teste falhar, **corrigir e re-testar** antes de prosseguir.
Uma WI SEM testes NAO esta concluida, independente de compilar e ter PR.

### R8 - Upload de Evidencias AUTOMATICO
Apos gerar QUALQUER artefato em `tests/{WI_ID}/`, SEMPRE fazer upload automaticamente na WI do ADO — **SEM perguntar ao usuario**.
1. Upload de TODOS os arquivos relevantes como Attachments na WI (exceto utilitarios como .bat, upload scripts)
2. Postar Discussion comment com tabela de resultados (arquivos, status, conclusao)
3. Publicar em `cenarios/{WI_ID}/` no repo `taxone_automacao_qa` (Phase 9.6)
**NUNCA perguntar "quer que eu anexe?" — e parte obrigatoria do fluxo.**

---

## Regra de Visibilidade do Knowledge

**OBRIGATORIO para o orquestrador e TODOS os subagentes:**

Sempre que for ler qualquer arquivo em `${CLAUDE_PLUGIN_ROOT}/knowledge/`, ANTES de usar a ferramenta Read,
imprimir uma mensagem visivel no console:

```
> [Knowledge] Carregando: {nome-do-arquivo} - {descricao-breve}
```

Exemplo:
```
> [Knowledge] Carregando: overview.md - Visao geral da arquitetura TAX ONE
> [Knowledge] Carregando: icms-apuracao.md - Knowledge do modulo de apuracao ICMS
```

Isso garante transparencia sobre quais knowledge bases estao sendo consultadas.

---

## Pipeline - Visao Geral

> **OTIMIZADO:** Fases independentes rodam em paralelo via Agent tool calls simultaneos.
> Fases condicionais possuem auto-skip por heuristicas. Phase 5.5 e 5.7 rodam em background.

```
Phase 0   : Resolver variaveis + buscar work item do ADO
Phase 0.5 : Buscar work items via query (se input for query ID)
Phase 0.6 : Enriquecer com Zendesk (extrair TKT do titulo, buscar ticket)    ──┐ PARALELO
Phase 0.7 : Enriquecer com Datadog (logs, traces, metricas APM) [CONDICIONAL] ──┘
Phase 0.9 : SM Allocation Check [CONDICIONAL]
Phase 1   : Analise de Escopo PM (taxone-pm em modo SCOPE)                  ──> GATE
     └──> SCOPE_INCOMPLETE → devolver PO/BA + tag SUST-IA-CLAUDE-ANALISE
     └──> SCOPE_AMBIGUOUS  → parar e pedir esclarecimento
     └──> REDIRECTED_BUG   → sugerir /taxone-auto-fix
     └──> SCOPE_CLEAR      → continuar pipeline
Phase 1.5 : Formalizacao de Regras de Negocio (taxone-architect)             ──> NEW
     └──> business_rules.json + test_scenarios.json
Phase 1.6 : Pre-Dev Validation Scripts (taxone-tester, modo pre_dev)        ──> TDD
     └──> validation_scripts_pre_dev.sql (cenarios executaveis para o dev)
Phase 2   : Design Arquitetural (taxone-architect)                ──┐ PARALELO
Phase 2.5 : Analise DBA Oracle (taxone-dba) [CONDICIONAL+AUTO]   ──┘
     └──> Consolidar design (merge architect + DBA)
Phase 3   : Criar workspace + branch MFS{work-item-id}
Phase 4   : Implementacao — criar codigo novo (taxone-developer)
Phase 4.5 : Verificacao de Cobertura de Regras [OBRIGATORIO]      ──┐
Phase 5   : Testes SQL de validacao (taxone-tester) [CONDICIONAL]  ──┤ PARALELO
Phase 5.5 : Testes de regressao SuiteAutomation [COND+AUTO+BG]    ──┤ (5.5 em background)
Phase 5.7 : Testes E2E Playwright [COND+AUTO+BG]                  ──┤ (5.7 em background)
Phase 6   : Code review (taxone-reviewer) [OBRIGATORIO]            ──┘
     └──> Aguardar Phase 6 (gate obrigatorio). Se 4.5=NO-GO, abortar.
Phase 7   : Commit + push + PR (gh pr create) — NUNCA merge
Phase 7.5 : Pacote Unitario (GitHub Actions) [CONDICIONAL]
Phase 8   : Atualizar ADO + relatorio final (inclui resultado 5.5 + 5.7 background)
Phase 9   : Compound Engineering [OPCIONAL]
```

### Fluxo de Decisao

```
                    +-------------------+
                    |   Phase 0/0.5     |
                    | Buscar Work Item  |
                    +--------+----------+
                             |
              +--------------+---------------+
              |                              |
     +--------v------+            +----------v--------+
     |  Phase 0.6    |            | Phase 0.7         |
     | Zendesk       |            | Datadog           |
     | [PARALELO]    |            | [PARALELO]        |
     +--------+------+            +----------+--------+
              |                              |
              +--------------+---------------+
                             |
                    +--------v----------+
                    |    Phase 0.9      |
                    |  SM Allocation    |
                    | [CONDICIONAL]     |
                    +--------+----------+
                             |
                    +--------v----------+
                    |    Phase 1        |
                    |  SCOPE ANALYSIS   |
                    |  taxone-pm        |
                    | [GATE DE ESCOPO]  |
                    +--------+----------+
                             |
          +--------+---------+----------+-----------+
          |        |         |          |
     SCOPE     SCOPE     SCOPE      REDIRECTED
     CLEAR     INCOMPLETE AMBIGUOUS  BUG
       ↓          ↓         ↓          ↓
     Continuar  [Devolver  [Parar    [Sugerir
     pipeline    PO/BA      +pedir    /taxone-
                 +ANALISE]  esclare-  auto-fix]
                            cimento]
                                                     |
                    +--------v----------+
                    |   Phase 1.5       |
                    | BUSINESS RULES    |
                    | taxone-architect  |
                    | [business_rules   |
                    |  .json]           |
                    +--------+----------+
                             |
              +--------------+---------------+
              |                              |
     +--------v----------+      +-----------v----------+
     |     Phase 2       |      |     Phase 2.5        |
     | taxone-architect  |      | taxone-dba            |
     | Design            |      | [PARALELO, se ativo]  |
     +--------+----------+      +-----------+----------+
              |                              |
              +--------->+<------------------+
                         |
                +--------v----------+
                | Consolidar Design |
                | (merge arch+DBA)  |
                +--------+----------+
                         |
                +--------v----------+
                |     Phase 3       |
                | Branch MFS{ID}    |
                +--------+----------+
                         |
                +--------v----------+
                |     Phase 4       |
                | CRIAR CODIGO NOVO |
                | taxone-developer  |
                +--------+----------+
                         |
     +---+-------+-------+-------+--------+
     |           |               |         |
  +--v-----+ +--v------+ +------v--+ +----v-------+
  |Ph 4.5  | |Phase 5  | |Ph 5.5   | |  Phase 6   |
  |Cobert. | |Tester   | |Suite    | |  Reviewer  |
  |Regras  | |[PARAL.] | |[BG]    | |  [PARAL.]  |
  +--+-----+ +--+------+ +------+--+ +----+-------+
     |           |           (bg)          |
     +-----+-----+----+-------------------+
           |           |
  +--------v--------+  |
  | 4.5=NO-GO?      |  |
  | Abortar se sim  |  |
  +--------+--------+  |
           |           |
  +--------v-----------v--+
  | Review APROVADO?      |
  +---+---------------+---+
  Sim |               | Nao
  +---v---------+ +---v----------+
  |  Phase 7    | | Voltar Ph. 4 |
  | Commit+PR   | | Corrigir     |
  +---+---------+ +--------------+
      |
  +---v---------+
  |  Phase 7.5  |
  | Pacote Unit.|
  +---+---------+
      |
  +---v---------+
  |  Phase 8    |
  | ADO Update  |
  | +coletar 5.5|
  +---+---------+
      |
  +---v---------+
  |  Phase 9    |
  | Compound    |
  | [OPCIONAL]  |
  +-------------+
```

---

## Phase 0 - Resolver Variaveis e Buscar Work Item

### Objetivo
Validar ambiente, resolver variaveis e obter os dados completos do work item do ADO.

### Passos

#### 0.1 - Validar PAT do ADO

```bash
# Verificar que ADO_PAT esta configurado
if [ -z "$ADO_PAT" ]; then
  echo "ERRO: Variavel ADO_PAT nao configurada"
  exit 1
fi
```

Se `ADO_PAT` nao estiver definido:
- Perguntar ao usuario: "A variavel de ambiente ADO_PAT nao esta configurada. Por favor, configure-a com seu Personal Access Token do Azure DevOps."
- **NAO continuar sem o PAT.**

#### 0.1b - Validar Ambiente Completo

```bash
# 1. Resolver REPO_ROOT
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
# Se falhar: abortar

# 2. Resolver usuario Git
GIT_USER=$(git config user.name 2>/dev/null)
# Se vazio: perguntar ao usuario

# 3. Verificar ADO_PAT
echo "$ADO_PAT" | head -c 5
# Se vazio: abortar

# 4. Verificar GitHub CLI
gh auth status
# Se nao autenticado: abortar
```

Imprimir resumo:
```
## Phase 0 - Ambiente Validado

- Repositorio: {REPO_ROOT}
- Usuario Git: {GIT_USER}
- ADO PAT: configurado (*****)
- GitHub CLI: autenticado
- Plugin Root: ${CLAUDE_PLUGIN_ROOT}
```

#### 0.2 - Resolver o Input

O input pode vir em 3 formatos:

| Formato                  | Exemplo                                                                                    | Acao                          |
|--------------------------|--------------------------------------------------------------------------------------------|-------------------------------|
| **Work Item ID**         | `12345`                                                                                    | Buscar diretamente            |
| **Query ID**             | `query:9bb6e572-8580-4eb3-86e6-a56bc5303d69`                                              | Ir para Phase 0.5             |
| **URL do ADO**           | `https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/12345`        | Extrair ID e buscar           |
| **Sem input**            | (vazio)                                                                                    | Perguntar ao usuario          |

Regras de parsing:
- Se o input e puramente numerico → Work Item ID
- Se comeca com `query:` → Query ID (ir para Phase 0.5)
- Se e uma URL contendo `_workitems/edit/` → extrair o ID numerico do final
- Se nao foi fornecido input → perguntar ao usuario com AskUserQuestion:
  ```
  Como voce gostaria de buscar a User Story/Feature?
  1. Informar o ID do Work Item (ex: 12345)
  2. Informar o ID de uma Query do ADO (ex: query:uuid)
  3. Colar a URL do Work Item do ADO
  ```

#### 0.3 - Buscar Work Item do ADO

```bash
curl -s \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{ID}?\$expand=all&api-version=7.1"
```

#### 0.4 - Extrair e Apresentar Dados

Extrair do JSON retornado:

| Campo                          | JSON Path                                          |
|--------------------------------|----------------------------------------------------|
| ID                             | `$.id`                                             |
| Titulo                         | `$.fields["System.Title"]`                         |
| Tipo                           | `$.fields["System.WorkItemType"]`                  |
| Estado                         | `$.fields["System.State"]`                         |
| Descricao                      | `$.fields["System.Description"]`                   |
| Acceptance Criteria            | `$.fields["Microsoft.VSTS.Common.AcceptanceCriteria"]` |
| Area Path                      | `$.fields["System.AreaPath"]`                      |
| Iteration Path                 | `$.fields["System.IterationPath"]`                 |
| Assigned To                    | `$.fields["System.AssignedTo"]`                    |
| Tags                           | `$.fields["System.Tags"]`                          |
| Attached Files                 | `$.relations[]` (filtrar por `AttachedFile`)       |
| Parent                         | `$.relations[]` (filtrar por `System.LinkTypes.Hierarchy-Reverse`) |
| Children                       | `$.relations[]` (filtrar por `System.LinkTypes.Hierarchy-Forward`) |

Apresentar ao usuario em formato legivel:

```
==========================================================
  WORK ITEM #{ID} - {Tipo}
==========================================================
  Titulo:     {titulo}
  Estado:     {estado}
  Area Path:  {area_path}
  Iteration:  {iteration}
  Assigned:   {assigned_to}
  Tags:       {tags}
----------------------------------------------------------
  DESCRICAO:
  {descricao - limpar HTML tags}
----------------------------------------------------------
  CRITERIOS DE ACEITACAO:
  {acceptance_criteria - limpar HTML tags}
----------------------------------------------------------
  ANEXOS: {quantidade}
  FILHOS: {quantidade}
==========================================================
```

#### 0.4.1 - Buscar Requisitos de WIs Filhas (Children)

**OBRIGATORIO quando a WI possuir filhos (relations com `System.LinkTypes.Hierarchy-Forward`).**

Objetivo: WIs do tipo User Story/Feature frequentemente possuem WIs filhas (Tasks, Requirements) que
contem a **especificacao detalhada da regra de negocio**. Esses requisitos devem ser carregados
para que a analise e implementacao reflitam a regra mais atualizada.

1. Extrair IDs dos filhos das `relations` do work item principal:
   ```bash
   CHILD_IDS=$(echo "$WI_JSON" | python -c "
   import json,sys,re
   wi=json.load(sys.stdin)
   ids=[]
   for r in wi.get('relations',[]):
       if 'Hierarchy-Forward' in r.get('rel',''):
           m=re.search(r'/(\d+)$', r.get('url',''))
           if m: ids.append(m.group(1))
   print(','.join(ids))
   ")
   ```

2. Se `CHILD_IDS` nao estiver vazio, buscar detalhes em batch:
   ```bash
   curl -s \
     -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
     "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems?ids={CHILD_IDS}&\$expand=all&api-version=7.1"
   ```

3. Para cada WI filha, extrair e armazenar:
   - ID, Titulo, Tipo, Estado
   - `System.Description` (descricao / especificacao da regra)
   - `Microsoft.VSTS.Common.AcceptanceCriteria` (criterios de aceitacao)
   - Anexos (contar e listar nomes)

4. Apresentar ao usuario:
   ```
   ----------------------------------------------------------
     WORK ITEMS FILHAS (Requisitos/Especificacoes):
   ----------------------------------------------------------
     #{CHILD_ID1} - {Tipo} - {Titulo} [{Estado}]
       Descricao: {resumo da descricao - primeiros 200 chars}

     #{CHILD_ID2} - {Tipo} - {Titulo} [{Estado}]
       Descricao: {resumo da descricao - primeiros 200 chars}
   ----------------------------------------------------------
   ```

5. **CRITICO:** O conteudo das WIs filhas deve ser incluido como contexto complementar em TODAS as
   fases subsequentes (Phase 1, 1.5, 2, 4, etc.). Se a WI filha contiver uma especificacao de regra de
   negocio mais detalhada que a WI pai, **a especificacao da filha tem precedencia** pois representa
   o requisito mais atualizado e granular.

6. Armazenar em variavel `CHILDREN_CONTEXT` para uso nas fases seguintes.

**Se nao houver filhos:** prosseguir normalmente.

### Execucao Paralela: Phase 0.6 + Phase 0.7

> **OTIMIZACAO:** Apos Phase 0 (ou 0.5), lancar Phase 0.6 (Zendesk) e Phase 0.7 (Datadog) em PARALELO.
> Ambas dependem apenas dos dados do work item (Phase 0) e sao independentes entre si.
>
> **Implementacao:** Usar Agent tool calls simultaneos (multiplos Agent no mesmo bloco de resposta).
> Aguardar ambas completarem antes de prosseguir para Phase 1.

#### 0.5 - Validar Area Path

Verificar se o Area Path do work item e compativel com TAX ONE:
- Deve conter `TAX ONE` no path
- Se nao conter, alertar o usuario:
  ```
  ATENCAO: Este work item nao pertence ao TAX ONE.
  Area Path: {area_path}
  Deseja continuar mesmo assim? (S/N)
  ```

---

## Phase 0.5 - Buscar Work Items via Query

### Objetivo
Quando o input e um Query ID, executar a query no ADO e apresentar os resultados para selecao.

### Condicao de Entrada
Input comeca com `query:` seguido de um UUID.

### Passos

#### 0.5.1 - Executar Query no ADO

```bash
QUERY_ID="9bb6e572-8580-4eb3-86e6-a56bc5303d69"  # extraido do input

curl -s \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/wiql/{QUERY_ID}?api-version=7.1"
```

#### 0.5.2 - Buscar Detalhes dos Work Items

```bash
IDS="id1,id2,id3"

curl -s \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems?ids={IDS}&\$expand=all&api-version=7.1"
```

#### 0.5.3 - Apresentar Lista para Selecao

```
==========================================================
  RESULTADOS DA QUERY
==========================================================
  Encontrados: {N} work items

  [1] #{ID1} - {Tipo} - {Titulo} [{Estado}]
  [2] #{ID2} - {Tipo} - {Titulo} [{Estado}]
  [3] #{ID3} - {Tipo} - {Titulo} [{Estado}]
  ...

  Selecione o work item para implementar (numero):
  Ou digite "todos" para implementar todos sequencialmente.
==========================================================
```

Usar AskUserQuestion para obter a selecao. Depois, voltar para Phase 0.3 com o ID selecionado.

---

## Phase 0.6 - Enriquecer com Zendesk

### Objetivo
Extrair o numero do ticket Zendesk (TKT) do titulo do work item e buscar os detalhes do ticket
para enriquecer o contexto da investigacao com a descricao do problema reportado pelo cliente.

### Condicao de Entrada
- O titulo do work item contem um padrao `TKT` seguido de digitos (ex: `TKT173337`, `TKT 175343`)
- As variaveis `ZENDESK_URL`, `ZENDESK_EMAIL` e `ZENDESK_TOKEN` estao configuradas

**Se o titulo NAO conter TKT ou as variaveis Zendesk nao estiverem configuradas: pular esta fase silenciosamente.**

### Passos

#### 0.6.1 - Extrair TKT do Titulo

```bash
TKT_NUM=$(echo "$WI_TITLE" | python -c "import sys,re; m=re.search(r'TKT\s*(\d+)', sys.stdin.read()); print(m.group(1) if m else '')")
```

Se `TKT_NUM` estiver vazio, pular fase.

#### 0.6.2 - Buscar Ticket no Zendesk

```bash
curl -sS -u "$ZENDESK_EMAIL/token:$ZENDESK_TOKEN" \
  "$ZENDESK_URL/api/v2/tickets/$TKT_NUM.json" \
  --connect-timeout 10
```

#### 0.6.3 - Extrair e Apresentar Dados

Do JSON retornado, extrair: Subject, Description, Status, Priority, Tags, Created At, Updated At.

```
----------------------------------------------------------
  ZENDESK - TKT{TKT_NUM}
----------------------------------------------------------
  Subject:     {subject}
  Status:      {status}
  Priority:    {priority}
  Aberto em:   {created_at}
  Atualizado:  {updated_at}
  Tags:        {tags relevantes - max 5}
----------------------------------------------------------
  RELATO DO CLIENTE:
  {description - primeiros 500 caracteres}
----------------------------------------------------------
```

#### 0.6.4 - Guardar Contexto

Armazenar: `ZD_TICKET_ID`, `ZD_SUBJECT`, `ZD_DESCRIPTION`, `ZD_STATUS`, `ZD_PRIORITY`, `ZD_TAGS`.

---

## Phase 0.7 - Enriquecer com Datadog

> **PARALELO:** Esta fase roda em paralelo com Phase 0.6 (Zendesk).

### Objetivo
Buscar dados reais de APM/logs/traces no Datadog via MCP Server para enriquecer o contexto
de WIs relacionadas a importacao, performance ou erros em batch.

### Pre-requisito
MCP Server `datadog` configurado em `~/.claude.json` (auth via OAuth, sem API Key manual).
Org: `trta-onesource` | Permissao: MCP Read (somente leitura).

### Condicao de Entrada

1. Titulo ou descricao do work item contem keywords de performance/importacao
2. MCP Server `datadog` disponivel e autenticado

**Se QUALQUER condicao NAO atendida:** pular silenciosamente.

### Keywords de Ativacao

`importa`, `lentidao`, `lento`, `timeout`, `performance`, `demora`, `batch`, `job servidor`,
`erro importacao`, `travou`, `demorado`, `processamento`, `carga`

### Passos

1. **Buscar Logs:** `search_datadog_logs` — `service:taxone* status:(error OR warn) {termos}` (7 dias)
2. **Buscar Traces:** `search_datadog_spans` — `service:taxone* @duration:>5s {termos}` (7 dias)
3. **Buscar Metricas:** `get_datadog_metric` — latencia media, P95, taxa de erro
4. **Buscar Monitors:** `search_datadog_monitors` — `taxone OR mastersaf`
5. **Buscar RUM / User Journey:** SEMPRE que WI envolver tela. **IMPORTANTE**: No TAX ONE, dados RUM vem embedados nos APM traces (`ingestion_reason:rum`), NAO como eventos RUM separados.
   - **Fonte primaria**: `search_datadog_spans` — `service:taxone* {termos}` com `custom_attributes: ["usr.*", "view.*", "session.*"]`
   - **Fonte secundaria (fallback)**: `search_datadog_rum_events` — `@type:error @application.name:*taxone*`
   - Extrair: `usr.menuPath`, `usr.module`, `view.name`, `view.url`, `session.has_replay`, `duration`
   - Gerar `DD_RUM_USER_JOURNEY` para alimentar Playwright

Apresentar bloco formatado e guardar variaveis: `DD_RELEVANT`, `DD_SERVICE`, `DD_ERROR_LOGS`,
`DD_SLOW_TRACES`, `DD_AVG_LATENCY`, `DD_P95_LATENCY`, `DD_ERROR_RATE`, `DD_MONITORS_ALERT`,
`DD_RUM_ERRORS`, `DD_RUM_USER_JOURNEY`, `DD_RUM_SESSION_ID`, `DD_RUM_ANOMALIES`, `DD_RUM_KNOWN_MATCHES`,
`DD_SIMILAR_FIXES`.

**Busca Estrutural de Fixes Anteriores** (executar durante scope analysis):

Buscar fixes anteriores que tocaram as mesmas tabelas/procedures/DDLs identificados:
```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/knowledge_search.py --wi-context {WI_ID} --format table
```
Fontes: `knowledge/solutions/*.md` (YAML frontmatter), `knowledge/solutions/INDEX.md` (patterns), `knowledge/ado-fixes/_metadata.json`, `tests/*/n3_brief.json`.
Se encontrar matches HIGH/MEDIUM, PM deve considerar na analise de escopo.

**Knowledge Base RUM** (consultar para enriquecer analise):
- `knowledge/datadog/module-service-map.json` — mapa modulo TAX ONE → service/resource/URLs Datadog
- `knowledge/datadog/known-rum-errors.json` — catalogo de erros RUM conhecidos com causa raiz e acao
- `knowledge/datadog/performance-baselines.json` — baselines P50/P95/P99 por endpoint

**Script auxiliar:** `scripts/rum_enricher.py` — classificacao de relevancia, match de erros, deteccao de anomalias.
**Agente deep-dive:** `taxone-rum-analyst` — invocar para analise RUM profunda se erros complexos ou anomalias detectadas.

**Fault-tolerant:** Se MCP retornar erro ou vazio em qualquer passo, registrar warning e continuar.

---

## Phase 0.9 - SM Allocation Check (OBRIGATORIA)

### Objetivo
Garantir que o WI tenha Developer e Tester atribuidos ANTES de iniciar o desenvolvimento.

### REGRA
Esta fase e **OBRIGATORIA**. O pipeline NAO pode prosseguir para Phase 1 sem `Custom.Developer` E `Custom.Tester` preenchidos.

### Passos

#### 0.9.1 - Verificar Custom.Developer e Custom.Tester

Verificar se AMBOS os campos estao preenchidos no WI.

- Se **AMBOS preenchidos**: pular direto para Phase 1. Exibir:
  ```
  ## Phase 0.9 - Alocacao (Skip)
  WI ja tem Developer: {dev} e Tester: {tester}. Mantendo alocacao existente.
  ```
- Se **pelo menos um vazio**: prosseguir com Passo 0.9.2. **NAO sobrescrever campo ja preenchido.**

#### 0.9.2 - Lancar taxone-sm

```
Agent(subagent_type="taxone-sm")
```

Prompt:
```
## Alocacao Avulsa - {Tipo} #{WI_ID}

### Dados do Work Item
- **Titulo:** {WI_TITLE}
- **Tipo:** {WI_TYPE}
- **Area Path:** {area_path}
- **Tags:** {WI_TAGS}
- **Priority:** {WI_PRIORITY}
- **Descricao:** {WI_DESCRIPTION} (resumo)

### Tarefa
Executar alocacao avulsa conforme documentado no seu perfil de agente.
```

#### 0.9.3 - Confirmar e PATCH (se aprovado)

Apresentar recomendacao ao usuario. Se aprovado, PATCH `System.AssignedTo` + tag `SUST-IA-CLAUDE`.

---

## Phase 1 - Analise de Escopo PM

### Objetivo
Classificar a User Story/Feature quanto a clareza de escopo e extrair regras de negocio.
**DIFERENTE da triage de bug:** aqui o PM pergunta "O escopo esta claro?" e nao "E um bug real?".

### Quando Executar
**SEMPRE** — esta fase e obrigatoria para todas as User Stories/Features.

### Verditos do PM (modo SCOPE)

| Verdito | Confianca Min | Acao |
|---------|---------------|------|
| `SCOPE_CLEAR` | >= 70% | Prosseguir para Phase 1.5 (formalizacao de regras) |
| `SCOPE_INCOMPLETE` | >= 75% | Devolver ao PO/BA + tag `SUST-IA-CLAUDE-ANALISE` |
| `SCOPE_AMBIGUOUS` | >= 70% | Parar pipeline e pedir esclarecimento ao usuario |
| `REDIRECTED_BUG` | >= 80% | Sugerir `/taxone-auto-fix` (nao implementar aqui) |

### Passos

#### 1.1 - Preparar Dados para o PM

Compilar todas as informacoes coletadas:
- Dados do work item (titulo, descricao, AcceptanceCriteria, area path, tags)
- Dados das WIs filhas (`CHILDREN_CONTEXT`)
- Dados Zendesk (se coletados na Phase 0.6)
- Dados Datadog (se coletados na Phase 0.7)

#### 1.2 - Lancar taxone-pm em modo SCOPE

```
Agent(subagent_type="taxone-pm")
```

Prompt para o agente:

```
## Analise de Escopo - User Story/Feature #{WI_ID}

### MODO: SCOPE (NAO triage de bug)
Voce esta analisando uma User Story/Feature, NAO um bug.
A pergunta central e: "O escopo e as regras estao claros para implementar?"
NAO pergunte "E um bug real?" — isso NAO se aplica aqui.

### Dados do Work Item
- **Titulo:** {WI_TITLE}
- **Tipo:** {WI_TYPE}
- **Descricao:** {WI_DESCRIPTION}
- **Acceptance Criteria:** {WI_ACCEPTANCE_CRITERIA}
- **Area Path:** {WI_AREA_PATH}
- **Tags:** {WI_TAGS}

### Work Items Filhas (Requisitos/Especificacoes)
{CHILDREN_CONTEXT — conteudo completo das WIs filhas}

### Contexto Zendesk (se disponivel)
{ZD_SUBJECT}, {ZD_DESCRIPTION}

### Contexto Datadog (se disponivel)
{DD_ERROR_LOGS}

### Checklist de Escopo (executar TODOS)

1. **Acceptance Criteria**: O campo AcceptanceCriteria esta preenchido E testavel?
   - Se vazio: forte sinal de SCOPE_INCOMPLETE
   - Se vago ("funcionar corretamente"): sinal de SCOPE_AMBIGUOUS
   - Se testavel (Given/When/Then ou criterios claros): OK

2. **Extracao de Regras**: Listar TODAS as regras de negocio como R01, R02, R03...
   - Extrair da Description + AcceptanceCriteria + WIs filhas
   - Cada regra deve ter: ID, descricao, tipo (calculation|validation|flow|configuration|integration)
   - Se nenhuma regra pode ser extraida: SCOPE_INCOMPLETE

3. **Modulo/Componente**: Identificar modulos afetados
   - Consultar MODULE_MAP.md para mapear prefixos DB → modulos
   - Usar area path como fallback

4. **Dependencias**: Checar WIs pai/irma via relacoes ADO
   - Se ha dependencias nao resolvidas: alertar

5. **Limite de Escopo**: O escopo esta delimitado?
   - Red flags: "todos modulos", "generico", "sistema inteiro", escopo aberto
   - Se red flags: sinal de SCOPE_AMBIGUOUS

6. **Impacto no Modelo**: A feature precisa de novas tabelas/colunas?
   - Cruzar regras extraidas com schema (knowledge/schema/)
   - Se precisa DDL: sinalizar para Phase 2.5

### Output Estruturado OBRIGATORIO

```json
{
  "verdict": "SCOPE_CLEAR|SCOPE_INCOMPLETE|SCOPE_AMBIGUOUS|REDIRECTED_BUG",
  "confidence": 85,
  "justification": "descricao do racional",
  "rules_extracted": [
    {"id": "R01", "description": "...", "source": "WI description / child #ID", "type": "calculation"},
    {"id": "R02", "description": "...", "source": "AcceptanceCriteria", "type": "validation"}
  ],
  "modules_affected": ["ICMS", "SAFX"],
  "needs_ddl": true,
  "needs_new_tables": false,
  "scope_gaps": ["lista de lacunas no escopo, se houver"],
  "test_scenarios": [
    {"id": "TC01", "description": "cenario de teste derivado de R01", "type": "happy_path"},
    {"id": "TC02", "description": "cenario negativo", "type": "negative"}
  ]
}
```

Se SCOPE_INCOMPLETE ou SCOPE_AMBIGUOUS, incluir `"missing_items"` com lista detalhada do que falta.
Se REDIRECTED_BUG, incluir `"redirect_reason"` explicando por que e bug e nao feature.
```

#### 1.3 - Processar Verdito do PM

Apresentar resultado ao usuario:

```markdown
## Phase 1 - Analise de Escopo PM

### Verdito: {VERDITO}
### Confianca: {X}%

{Resumo da justificativa}

### Regras Extraidas: {N}
{lista de R01...Rnn com descricao}

### Cenarios de Teste: {N}
{lista de TC01...TCnn}
```

#### 1.4 - Decisao de Fluxo

- **SCOPE_CLEAR (confianca >= 70%):**
  Prosseguir para Phase 1.5 (formalizacao de regras).
  Salvar `tests/{WI_ID}/test_scenarios.json` com os cenarios gerados.
  ```
  Escopo claro ({confianca}%). {N} regras extraidas. Prosseguindo para formalizacao...
  ```

- **SCOPE_INCOMPLETE (confianca >= 75%):**
  Devolver ao PO/BA. Adicionar tag `SUST-IA-CLAUDE-ANALISE`.
  ```
  Escopo incompleto ({confianca}%).

  Itens faltantes:
  {missing_items}

  Deseja:
  1. Devolver ao PO/BA com feedback estruturado + tag ANALISE
  2. Fornecer as informacoes faltantes agora
  3. Prosseguir mesmo assim (com escopo incompleto)
  ```
  Se opcao 1: PATCH ADO com feedback + tags, encerrar.
  Se opcao 2: coletar informacoes e relancar PM.
  Se opcao 3: continuar com warning.

- **SCOPE_AMBIGUOUS (confianca >= 70%):**
  Parar e pedir esclarecimento.
  ```
  Escopo ambiguo ({confianca}%).

  Pontos ambiguos:
  {scope_gaps}

  Por favor, esclarecer os pontos acima para que o pipeline possa prosseguir.
  ```

- **REDIRECTED_BUG (confianca >= 80%):**
  Sugerir redirecionamento para pipeline de bugs.
  ```
  Esta WI parece ser um BUG, nao uma Feature ({confianca}%).

  Motivo: {redirect_reason}

  Deseja:
  1. Redirecionar para /taxone-auto-fix (pipeline de bugs)
  2. Discordar e prosseguir como Feature
  ```

#### 1.5 - Carregar Knowledge Base

**Apos verdito SCOPE_CLEAR (ou usuario forcou continuacao):**

1. Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/overview.md`
2. Identificar features/modulos via titulo e regras extraidas
3. Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/features/{feature}.md`
4. Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/code-standards.md`
5. Buscar artigos WebHelp relevantes

Para cada arquivo lido: `> [Knowledge] Carregando: {nome} - {descricao}`

#### 1.6 - Confirmar Opcoes do Pipeline

Perguntar ao usuario usando AskUserQuestion:

```
Opcoes do pipeline para #{ID} - {titulo}:

1. Analise DBA Oracle (taxone-dba): Avaliar DDL, indices, performance
   [S/N] (Recomendado: {Sim se needs_ddl, Nao caso contrario})

2. Scripts de Teste SQL (taxone-tester): Criar scripts de validacao
   [S/N] (Recomendado para mudancas em calculos fiscais)

3. Compound Engineering (Phase 9): Atualizar knowledge base
   [S/N] (Recomendado para features novas)

4. Testes de Regressao SuiteAutomation (Phase 5.5)
   [S/N]

5. Testes E2E Playwright (Phase 5.7)
   [S/N]

Confirme as opcoes (ex: "1-S 2-N 3-S 4-S 5-S" ou "todos-S"):
```

Guardar opcoes: `OPT_DBA`, `OPT_TESTS`, `OPT_COMPOUND`, `OPT_REGRESSION`, `OPT_E2E`.

---

## Phase 1.5 - Analise de Regras de Negocio

### Objetivo
Formalizar TODAS as regras de negocio extraidas pelo PM em um formato estruturado,
consultando a base de conhecimento para enriquecer cada regra com tabelas, packages e SQL hints.

**Esta fase NAO existe no pipeline de bug fix.** E exclusiva do pipeline de features.

### Condicao de Entrada
Phase 1 emitiu verdito `SCOPE_CLEAR` (ou usuario forcou continuacao).

### Passos

#### 1.5.1 - Lancar taxone-architect para Formalizacao

```
Agent(subagent_type="taxone-architect")
```

Prompt para o agente:

```
## Formalizacao de Regras de Negocio - Feature #{WI_ID}

### MODO: FORMALIZACAO DE REGRAS (NAO design de solucao — isso vem na Phase 2)

### Dados do Work Item
- **Titulo:** {WI_TITLE}
- **Descricao:** {WI_DESCRIPTION}
- **Acceptance Criteria:** {WI_ACCEPTANCE_CRITERIA}

### Work Items Filhas
{CHILDREN_CONTEXT}

### Regras Extraidas pelo PM (Phase 1)
{rules_extracted — lista de R01...Rnn do PM}

### Cenarios de Teste do PM
{test_scenarios — lista de TC01...TCnn}

### Sua Tarefa

Formalizar TODAS as regras extraidas pelo PM em formato estruturado.
Para CADA regra:
1. Validar a descricao (corrigir ambiguidades)
2. Identificar tipo: calculation | validation | flow | configuration | integration
3. Consultar knowledge/schema/ para identificar tabelas afetadas
4. Consultar PLSQL_MAP.md para identificar packages/procedures afetados
5. Consultar knowledge/business-rules/{module}/ para verificar regras existentes similares
6. Consultar knowledge/webhelp/ e knowledge/features/ para contexto funcional
7. Definir se a regra e testavel e sugerir SQL de validacao (hint)
8. Identificar se sao necessarios novos objetos (tabelas, colunas, packages)

### Output OBRIGATORIO

Criar arquivo `tests/{WI_ID}/business_rules.json` com:

```json
{
  "work_item_id": {WI_ID},
  "title": "{WI_TITLE}",
  "total_rules": N,
  "rules": [
    {
      "id": "R01",
      "description": "descricao formalizada da regra",
      "source": "WI description / child #{CHILD_ID} / business-rules/{file}",
      "type": "calculation|validation|flow|configuration|integration",
      "tables_affected": ["SAFX07", "X07"],
      "packages_affected": ["PKG_EXAMPLE"],
      "testable": true,
      "sql_validation_hint": "SELECT ... FROM ... WHERE ...",
      "existing_similar_rule": "knowledge/business-rules/{module}/{file}.md#section (se existir)",
      "notes": "observacoes relevantes"
    }
  ],
  "new_objects_needed": [
    {"type": "column", "table": "X07", "name": "NEW_COL", "datatype": "VARCHAR2(100)", "reason": "R03 requer armazenar X"}
  ],
  "affected_modules": ["ICMS", "SAFX"],
  "cross_module_impacts": [
    {"from_module": "ICMS", "to_module": "SPED", "impact": "descricao do impacto"}
  ]
}
```

Tambem enriquecer `tests/{WI_ID}/test_scenarios.json` com cenarios derivados das regras formalizadas.

IMPORTANTE: Cada regra DEVE ter `testable: true|false` e `sql_validation_hint` para guiar o tester.
```

#### 1.5.2 - Validar e Apresentar Resultado

Verificar que `business_rules.json` foi criado:
```bash
test -f "tests/${WI_ID}/business_rules.json" && echo "OK" || echo "MISSING"
```

Apresentar ao usuario:

```markdown
## Phase 1.5 - Regras de Negocio Formalizadas

- **Total de regras:** {N}
- **Novos objetos necessarios:** {N}
- **Modulos afetados:** {lista}
- **Impactos cross-module:** {N}

### Regras
| ID  | Tipo          | Descricao (resumo)          | Testavel | Tabelas       |
|-----|---------------|-----------------------------|----------|---------------|
| R01 | calculation   | {descricao curta}           | Sim      | SAFX07, X07   |
| R02 | validation    | {descricao curta}           | Sim      | EST_APURACAO   |
...

### Novos Objetos
{lista ou "Nenhum"}

As regras acima serao usadas como contrato para a implementacao (Phase 4)
e verificacao de cobertura (Phase 4.5).

Prosseguir para Pre-Dev Validation Scripts? (S/N)
```

---

## Phase 1.6 - Pre-Dev Validation Scripts (Cenarios Executaveis para o Dev)

> **TDD Adaptado:** Gerar scripts SQL executaveis ANTES da implementacao para que o dev possa iterar durante o desenvolvimento.

### Objetivo
Expandir os cenarios do `test_scenarios.json` (gerados na Phase 1) em scripts SQL executaveis que o dev pode rodar no banco Oracle local durante o desenvolvimento.

### Condicao de entrada
- `test_scenarios.json` existe COM cenarios (`scenarios` nao vazio)
- Phase 1.5 concluida (regras formalizadas em `business_rules.json`)

### Skip automatico
- Se PM emitiu `SCOPE_INCOMPLETE` ou `SCOPE_AMBIGUOUS` (nao ha cenarios confiáveis)
- Se `test_scenarios.json` nao existe ou `scenarios: []`
- Se todos os cenarios sao puramente de arquivo magnetico (SPED/ECD/EFD)

Nesse caso:
```
## Phase 1.6 - Pre-Dev Validation Scripts (Skip)
Motivo: {cenarios insuficientes / scope incompleto / todos dev_runnable: false}
```

### Passos

#### 1.6.1 - Executar test_enricher em modo pre_dev

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/test_enricher.py \
  --wi-id ${WI_ID} \
  --mode pre_dev \
  --packages "{packages_involved do JSON, separados por virgula}" \
  --tables "{tables_involved do JSON, separados por virgula}" \
  --format summary
```

#### 1.6.2 - Lancar taxone-tester em modo PRE-DEV

Invocar via Agent com `subagent_type="taxone-tester"`:

```
## Modo: PRE-DEV (antes da implementacao)

WI: #{WI_ID} - {WI_TITLE}
Tipo: Feature/User Story (NAO bug)
Cenarios disponiveis: tests/{WI_ID}/test_scenarios.json
Regras de negocio: tests/{WI_ID}/business_rules.json

IMPORTANTE - Diferenca de Feature vs Bug:
- Em bugs, o sql_pre_dev valida que o PROBLEMA existe (estado incorreto)
- Em features, o sql_pre_dev valida o "ESTADO ZERO" — as tabelas AINDA NAO tem
  os dados que a feature vai criar. O teste deve FALHAR antes da implementacao
  e PASSAR depois (TDD classico).

Para cada cenario com priority critical ou high:
1. Expandir sql_hint em sql_pre_dev (SELECT executavel no banco Oracle local V2R010AC)
2. Para features: sql_pre_dev deve retornar 'FALHA' antes da implementacao (estado zero)
3. Marcar dev_runnable: true/false
4. Gerar setup_data/teardown_data se necessario
5. Salvar validation_scripts_pre_dev.sql em tests/{WI_ID}/
6. Atualizar test_scenarios.json

Usar regras formalizadas (business_rules.json) como fonte adicional de cenarios.
Cada regra com testable: true deve ter pelo menos um cenario com sql_pre_dev.

TABELAS DISPONIVEIS: {tables_involved do test_scenarios.json}
Schema reference: knowledge/conventions/test-scenarios-schema.md
```

#### 1.6.3 - Apresentar resumo

```markdown
## Phase 1.6 - Pre-Dev Validation Scripts

- **Arquivo:** tests/{WI_ID}/validation_scripts_pre_dev.sql
- **Cenarios executaveis (dev_runnable: true):** {N}
- **Cenarios manuais (dev_runnable: false):** {N}
- **Regras com cenario executavel:** {N}/{total regras testaveis}
- **Setup de dados necessario:** {Sim/Nao}

> O dev pode executar validation_scripts_pre_dev.sql a qualquer momento
> durante o desenvolvimento para verificar progresso.
> Scripts de feature validam "estado zero" — devem FALHAR antes da implementacao.
```

#### 1.6.4 - Review Pre-Dev (SOMENTE risco Alto/Critico)

Se tabelas em `TABLE_HOTSPOTS.md` com >5 bugs OU packages em `PLSQL_MAP.md` com >50 refs:
Invocar `taxone-techlead-qa` para review pre-dev (NAO bloqueante).

**Nota:** Esta fase e nao-bloqueante. Se falhar, o pipeline continua normalmente.

---

## Phase 2 - Design Arquitetural

> **PARALELO:** Se `OPT_DBA == true`, lancar Phase 2 (Architect) e Phase 2.5 (DBA) em PARALELO.

### Objetivo
Obter design proposto do agente taxone-architect **a partir dos requisitos e regras formalizadas**.
**Diferente do bug fix:** aqui o architect projeta uma solucao nova, nao diagnostica causa raiz.

### Condicao
**SEMPRE executada.** Nenhuma implementacao ocorre sem design previo.

### Passos

#### 2.1 - Lancar taxone-architect para Design

```
Agent(subagent_type="taxone-architect")
```

Prompt para o agente:

```
## Design Arquitetural para Feature #{WI_ID}

### MODO: DESIGN DE FEATURE (NAO diagnostico de bug)
Voce esta projetando uma SOLUCAO NOVA, nao diagnosticando uma causa raiz.
A pergunta e: "Como construir isso seguindo os patterns existentes?"

### Dados do Work Item
- **Titulo:** {WI_TITLE}
- **Descricao:** {WI_DESCRIPTION}
- **Acceptance Criteria:** {WI_ACCEPTANCE_CRITERIA}

### Regras de Negocio Formalizadas (Phase 1.5)
{conteudo de business_rules.json — TODAS as regras R01...Rnn}

### Knowledge Disponivel
{resumo do knowledge carregado na Phase 1.5}

### Contexto Zendesk (se disponivel)
{ZD_DESCRIPTION}

### Contexto Datadog (se disponivel)
{DD_SLOW_TRACES}

### Sua Tarefa

1. Carregar knowledge das features/modulos envolvidos
2. Para CADA regra formalizada (R01...Rnn):
   - Definir em qual camada sera implementada (PL/SQL, DDL, PB, Java/Angular)
   - Identificar packages/procedures existentes a serem modificados
   - Identificar packages/procedures NOVOS a serem criados
3. Propor design por camada:
   - **PL/SQL:** Packages, procedures, functions, triggers
   - **DDL:** Tabelas, colunas, indices, constraints, sequences
   - **PowerBuilder:** DataWindows, windows, menus, user objects
   - **Java/Angular:** Classes, services, components
4. Definir sequencia de implementacao com dependencias (o que deve ser criado primeiro)
5. Listar riscos e pontos de atencao
6. Enriquecer test_scenarios.json com cenarios derivados do design

### Output

Entregar no formato padrao de Design Proposto:
- Design por camada (PL/SQL, DDL, PB, Java)
- Mapeamento regra → componente (qual regra e implementada onde)
- Sequencia de implementacao
- Riscos e mitigacoes
- Cenarios de teste adicionais
```

#### 2.2 - Receber e Validar Resposta

O architect deve retornar:
- Design por camada com mapeamento regra → componente
- Sequencia de implementacao com dependencias
- Riscos e mitigacoes

Apresentar ao usuario:
```
Design arquitetural concluido. Revise o design proposto acima.

Deseja prosseguir com a implementacao? (S/N)
Se desejar ajustes, descreva o que precisa ser alterado.
```

Se o usuario pedir ajustes, relancar o architect com feedback.

#### 2.3 - Salvar Impact Assessment

O taxone-architect gera um Impact Assessment JSON como parte do seu output (secao 4 do agente).
Extrair o JSON e salvar em `tests/{WI_ID}/impact_assessment.json`.

**Schema:** `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/impact-assessment-schema.json`

**Decisao de fluxo baseada no Impact Assessment:**
- `architect_recommendation == "BLOCKED"`: PARAR pipeline, reportar ao usuario
- `architect_recommendation == "NEEDS_REVIEW"`: Alertar usuario, prosseguir com cautela
- `risk_score == "CRITICAL"`: Requerer confirmacao explicita do usuario antes de prosseguir

---

## Phase 2.5 - Analise DBA Oracle

> **PARALELO:** Esta fase roda em paralelo com Phase 2 (Architect) quando `OPT_DBA == true`.

### Objetivo
Analisar impacto no banco de dados Oracle: DDL, performance, indices, particionamento.

### Condicao
**CONDICIONAL** - Executada se `OPT_DBA == true` OU auto-ativada por heuristicas.

### Auto-Skip Inteligente

| Sinal na WI ou business_rules.json | Acao |
|-------------------------------------|------|
| `new_objects_needed` nao vazio | **Auto-ativar** |
| Menciona: performance, lento, timeout, indice, DDL, ALTER TABLE | **Auto-ativar** |
| Contexto Datadog (`DD_SLOW_TRACES` com dados) | **Auto-ativar** |
| Apenas tela PB/Java sem impacto em banco | **Auto-skip** |

### Passos

#### 2.5.1 - Lancar taxone-dba

```
Agent(subagent_type="taxone-dba")
```

Prompt:
```
Analise DBA para Feature #{WI_ID}:

TITULO: {titulo}
DESCRICAO: {descricao}

REGRAS DE NEGOCIO (business_rules.json):
{conteudo completo — especialmente new_objects_needed}

KNOWLEDGE: {resumo — tabelas, packages, modulo}

CONTEXTO DATADOG (se disponivel):
{DD_SLOW_TRACES}, {DD_P95_LATENCY}

Por favor:
1. Gerar DDL scripts para novos objetos (tabelas, colunas, indices, constraints)
2. Salvar como DDL_MFS{work-item-id}.sql (NUNCA alterar DDL antiga existente)
3. Avaliar indices necessarios
4. Gerar explain plans para queries criticas
5. Avaliar impacto de locks durante deploy
6. Se Datadog forneceu traces lentas, correlacionar

NOTA: Compilar objetos PL/SQL no banco porta 1521 (V2R010AC/V2R010AC@localhost:1521/MFSPDB).
```

#### 2.5.2 - Consolidar Design (Architect + DBA)

> Executar SOMENTE apos Phase 2 e Phase 2.5 completarem.

1. Receber resultado do architect e do DBA
2. Verificar conflitos/sobreposicoes
3. Consolidar design unificado
4. Se divergencias: informar usuario e pedir decisao

---

## Phase 3 - Workspace e Branch

### Objetivo
Preparar o workspace Git e criar a branch de trabalho.

### Passos

#### 3.1 - Verificar Estado do Repositorio

```bash
git rev-parse --is-inside-work-tree
git branch --show-current
git status --porcelain
```

Se mudancas pendentes: perguntar stash/commit/abortar.

#### 3.2 - Atualizar Branch Base

```bash
# Verificar se branch DEV existe
git branch -a | grep -q "DEV" && BASE_BRANCH="DEV" || BASE_BRANCH="main"
git checkout "$BASE_BRANCH"
git pull origin "$BASE_BRANCH"
```

#### 3.3 - Criar Branch de Trabalho

```bash
BRANCH_NAME="MFS{work-item-id}"
git checkout -b "$BRANCH_NAME"
```

Exemplo: `MFS1058668`

Confirmar:
```
Branch criada: MFS{work-item-id}
Base: {BASE_BRANCH} (atualizada)
Workspace pronto para implementacao.
```

#### 3.4 - Capturar Baseline RC

**Objetivo:** Obter a versao estavel (RC) dos arquivos que serao modificados, garantindo que o developer trabalhe sobre codigo de producao e nao sobre alteracoes nao testadas em DEV.

**Passo 1 - Coletar arquivos afetados:**

Extrair dos outputs anteriores:
- Phase 2 (Architect): `packages_affected` do design spec, arquivos listados na sequencia de implementacao
- Phase 1.5 (PM): componentes mencionados no `business_rules.json`
- Combinar em lista unica, deduplicar

**Passo 1.5 - Atualizar branch RC local:**

```bash
cd "$TAXONE_DW_REPO"
git fetch origin RC:RC
```

> OBRIGATORIO antes de qualquer comparacao — RC local pode estar desatualizada.

**Passo 2 - Verificar divergencia RC vs DEV:**

Para cada arquivo identificado:
```bash
cd "$TAXONE_DW_REPO"
git diff --stat RC..DEV -- "path/to/file"
```

- Se output vazio: RC e DEV sao identicos para este arquivo — sem acao
- Se output mostra diferencas: arquivo diverge — capturar baseline RC

**Passo 3 - Capturar conteudo RC dos divergentes:**

Para cada arquivo que diverge:
```bash
git show RC:"path/to/file"
```

- Se o comando falha (arquivo nao existe em RC): registrar como "arquivo novo em DEV, nao existe em producao"
- Se o arquivo tem mais de 500 linhas: capturar apenas o diff (`git diff RC..DEV -- "path"`) + a funcao/procedure especifica afetada

**Passo 4 - Montar RC_BASELINE_CONTEXT:**

Gerar tabela resumo:
```
| Arquivo | RC==DEV? | Linhas alteradas em DEV |
|---------|----------|-------------------------|
| pkg_x.sql | NAO | +15 -3 |
| prc_y.sql | SIM | — |
| fnc_z.sql | NOVO_DEV | (nao existe em RC) |
```

Para cada arquivo divergente, anexar:
- Diff RC vs DEV: `git diff RC..DEV -- "path"`
- Conteudo RC completo (ou trecho relevante se >500 linhas)

**Passo 5 - Decisao:**

- Se TODOS os arquivos sao identicos (RC==DEV): pular secao RC Baseline no prompt do developer (caso mais comum)
- Se HA divergencias: incluir `RC_BASELINE_CONTEXT` no prompt da Phase 4

**Nota:** Esta fase e NAO-BLOQUEANTE. Se o branch RC nao existir ou o comando falhar, registrar aviso e continuar normalmente para a Phase 4.

---

## Phase 4 - Implementacao

### Objetivo
Implementar as mudancas de codigo delegando ao agente especializado (`taxone-plsql` / `taxone-pb` / `taxone-java`).
**Diferente do bug fix:** o developer CRIA codigo novo seguindo o design spec da Phase 2
e as regras formalizadas da Phase 1.5. NAO corrige codigo existente.

### Passos

#### 4.1 - Selecionar Agente

**Detectar linguagem pelo design do architect:**

| Sinal no Design | Agente |
|------------------|--------|
| Packages PL/SQL (.sql, PKG_, PRC_, FNC_, TRG_, VW_) | `taxone-plsql` |
| DataWindows (.srd, .srw, .srf, .sru), scripts PB | `taxone-pb` |
| Classes Java (.java, .jrxml), servlets, Jasper | `taxone-java` |
| Componentes Angular (.ts, .html, .scss) | `taxone-angular` |

- Se MULTIPLAS linguagens:
  - PL/SQL + PB: lancar `taxone-plsql` PRIMEIRO, depois `taxone-pb`
  - PL/SQL + Java: lancar em PARALELO
  - Qualquer combo + Angular: Angular em PARALELO

#### 4.2 - Lancar Agente de Implementacao

PL/SQL: `Agent(subagent_type="taxone-plsql")`
PowerBuilder: `Agent(subagent_type="taxone-pb")`
Java: `Agent(subagent_type="taxone-java")`
Angular: `Agent(subagent_type="taxone-angular")`

Prompt:
```
## Implementar Feature #{WI_ID}

### MODO: CRIACAO DE CODIGO NOVO (NAO correcao de bug)
Voce esta CRIANDO codigo novo seguindo o design spec e as regras de negocio.
NAO procure "o que esta quebrado" — implemente o que esta especificado.

### Dados do Work Item
TITULO: {titulo}
DESCRICAO: {descricao}
CRITERIOS DE ACEITACAO: {criterios}

### Regras de Negocio (business_rules.json)
{conteudo completo — CADA regra R01...Rnn deve ser implementada}

### Design Aprovado (Phase 2)
{design_proposto — mapeamento regra → componente}

### Sequencia de Implementacao
{sequencia definida pelo architect}

### Recomendacoes DBA (se houver)
{DDL scripts, indices, explain plans}

### RC Baseline (Codigo Estavel de Referencia)
{RC_BASELINE_CONTEXT — incluir SOMENTE se ha divergencias RC vs DEV (Passo 3.4)}

**INSTRUCAO:** Se RC baseline fornecido acima, RESTAURAR a versao RC de cada arquivo
divergente ANTES de aplicar suas mudancas:
```bash
git show RC:"path/to/file" > "path/to/file"
```
Implementar em cima da versao RC (producao estavel), NAO da versao DEV.
Arquivos marcados como "identico RC==DEV" nao precisam de restauracao.
Arquivos marcados como "NOVO_DEV" devem ser trabalhados normalmente.

### IMPORTANTE:
- Seguir RIGOROSAMENTE o design aprovado
- Implementar TODAS as regras listadas em business_rules.json
- Para cada regra implementada, adicionar comentario no codigo: -- R{XX}: {descricao}
- Seguir patterns existentes no projeto
- Nao refatorar codigo fora do escopo
- Documentar procedures/functions com comentarios em portugues
- Usar bind variables (NUNCA concatenar valores em SQL dinamico)
- Para PL/SQL: exception handling com WHEN OTHERS + logging
- **Compilar PL/SQL no banco porta 1521 ANTES de finalizar**
  (V2R010AC/V2R010AC@localhost:1521/MFSPDB)

### Checklist de Entrega
Ao finalizar, retornar:
1. Lista de TODOS os arquivos criados e modificados
2. Para CADA regra (R01...Rnn): indicar ONDE foi implementada (arquivo:linha)
3. DDL scripts gerados (se houver) — salvar como DDL_MFS{work-item-id}.sql
4. Resultado da compilacao PL/SQL no banco
5. Notas e observacoes
```

#### 4.3 - Verificar Resultado

```bash
git status --porcelain
```

Se nenhum arquivo modificado: reportar erro. Retry 1x com prompt mais especifico.

### Execucao Paralela Pos-Implementacao: Phase 4.5 + 5 + 5.5 + 5.7 + 6

> Apos Phase 4 completar, lancar fases 4.5, 5, 5.5, 5.7 e 6 em PARALELO.
>
> ```
> Agent 1: Phase 4.5 - Verificacao de Cobertura de Regras (OBRIGATORIO)
> Agent 2: Phase 5   - Testes SQL (se OPT_TESTS == true)
> Agent 3: Phase 5.5 - SuiteAutomation (se OPT_REGRESSION == true) → background
> Agent 4: Phase 6   - Code Review (OBRIGATORIO)
> Agent 5: Phase 5.7 - Playwright E2E (se OPT_E2E == true) → background
> ```
>
> **Gates apos paralelo:**
> 1. Se Phase 4.5 = **NO-GO**: abortar (mesmo se review ja aprovou)
> 2. Phase 6 = gate obrigatorio antes de Phase 7
> 3. Phases 5.5 e 5.7 rodam em background — coletados na Phase 8

---

## Phase 4.5 - Verificacao de Cobertura de Regras

> **PARALELO:** Roda em paralelo com Phase 5, 5.5, 5.7 e 6.

### Objetivo
Verificar que TODAS as regras formalizadas em `business_rules.json` foram implementadas.
**Diferente do bug fix:** no bug fix, 4.5 verifica "nao quebrou regras existentes".
Aqui, 4.5 verifica "TODAS as regras NOVAS foram implementadas" (cobertura).

### Condicao
**OBRIGATORIO** — sempre executada quando `business_rules.json` existe.

### Passos

#### 4.5.1 - Lancar taxone-architect

```
Agent(subagent_type="taxone-architect")
```

Prompt:
```
## Verificacao de Cobertura de Regras - Feature #{WI_ID}

### MODO: VERIFICACAO DE COBERTURA (NAO analise de impacto)
Sua tarefa e verificar que CADA regra do business_rules.json foi implementada.
NAO e uma analise de "o que pode quebrar" — e uma checklist de "o que foi feito".

### Regras de Negocio (business_rules.json)
{conteudo completo}

### Implementacao Realizada (Phase 4)
{lista de arquivos criados/modificados}
{mapeamento regra → arquivo:linha retornado pelo developer}

### Design Aprovado (Phase 2)
{design_proposto}

### Sua Tarefa
Para CADA regra em business_rules.json:
1. Verificar se a regra foi implementada no(s) arquivo(s) indicado(s)
2. Verificar se a implementacao esta correta conforme a descricao da regra
3. Verificar se o sql_validation_hint da regra seria satisfeito
4. Marcar como: IMPLEMENTED / NOT_IMPLEMENTED / PARTIALLY_IMPLEMENTED

### Output Estruturado

```json
{
  "verdict": "GO|NO-GO",
  "total_rules": N,
  "implemented": N,
  "not_implemented": N,
  "partially_implemented": N,
  "coverage_pct": 95,
  "rules_status": [
    {"id": "R01", "status": "IMPLEMENTED", "location": "pkg_example.sql:45", "notes": ""},
    {"id": "R02", "status": "NOT_IMPLEMENTED", "location": "", "notes": "regra nao encontrada no codigo"}
  ],
  "new_rules_detected": [],
  "business_rule_tag_needed": true
}
```

**Decisao GO/NO-GO:**
- GO: Todas regras IMPLEMENTED (coverage 100%)
- GO com ressalvas: coverage >= 80% e parciais sao aceitaveis
- NO-GO: coverage < 80% ou regra critica NOT_IMPLEMENTED
```

#### 4.5.2 - Avaliar Resultado

- **GO:** Prosseguir.
- **GO com ressalvas:** Apresentar regras parciais/faltantes, perguntar ao usuario.
- **NO-GO:** Apresentar regras nao implementadas e oferecer:
  1. Voltar para Phase 4 (developer implementa regras faltantes)
  2. Aceitar com riscos
  3. Abortar pipeline

Se `business_rule_tag_needed == true`: adicionar tag `SUST-IA-CLAUDE-REGRA`.

```markdown
## Phase 4.5 - Verificacao de Cobertura de Regras

- Decisao: {GO / NO-GO}
- Cobertura: {coverage_pct}%
- Regras implementadas: {N}/{total}
- Regras faltantes: {lista}
- Tag REGRA: {Sim/Nao}
```

---

## Phase 5 - Testes SQL de Validacao

> **PARALELO:** Roda em paralelo com Phase 4.5, 5.5, 5.7 e 6.

### Objetivo
Criar scripts SQL de validacao para CADA regra de negocio.

### Condicao
**CONDICIONAL** - Executada APENAS se `OPT_TESTS == true`.

**REGRA CRITICA: SEMPRE prosseguir com testes automaticamente apos implementacao e PR, sem perguntar ao usuario.** O fluxo completo de testes (compilacao, validacao SQL, SuiteAutomation, evidencias em tests/{WI_ID}/, upload de attachments na WI do ADO, Discussion comment com resultados, e criacao de Tasks QA) e parte integral e obrigatoria do pipeline. NUNCA parar para perguntar "quer que eu prossiga com testes?".

### Passos

#### 5.1 - Lancar taxone-tester

```
Agent(subagent_type="taxone-tester")
```

Prompt:
```
Criar scripts de validacao para Feature #{WI_ID}:

TITULO: {titulo}

REGRAS DE NEGOCIO (business_rules.json):
{conteudo — usar sql_validation_hint de cada regra como base}

CENARIOS DE TESTE (test_scenarios.json):
{conteudo}

IMPLEMENTACAO REALIZADA:
{resumo do developer}

DESIGN (do architect):
{design_proposto}

Por favor:
1. Para CADA regra (R01...Rnn): criar script SQL que valida a regra
2. Usar sql_validation_hint como ponto de partida
3. Cobrir cenarios:
   - Caminho feliz (dados validos para cada regra)
   - Cenarios negativos (dados invalidos)
   - Edge cases (nulos, zeros, limites)
   - Regressao (se aplicavel)
4. Criar script de dados de teste (INSERT/UPDATE)
5. Criar roteiro de teste manual (se envolve tela PB)
6. Criar script de rollback dos dados de teste

Salvar scripts em: tests/{work-item-id}/
```

---

## Phase 5.2 - Geracao de Dados SAFX (Auto-detect)

### Objetivo
Gerar flat-files SAFX de teste para importacao em outros ambientes (QA/RC).
Quando nao existe cenario SuiteAutomation para o componente, SAFX e gerada automaticamente.

### Passos

**Passo 1 - Executar safx_auto_generator:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/safx_auto_generator.py --wi-id ${work-item-id} --env LOCAL
```

O script:
1. Detecta packages modificados no branch `MFS{work-item-id}` via `git diff`
2. Consulta `component-test-map.json` — se existe cenario SuiteAutomation, retorna `SUITE_EXISTS`
3. Se NAO existe cenario: detecta tabelas SAFX via `ALL_DEPENDENCIES` + `safx-table-index.json`
4. Gera flat-files pipe-delimited + SQL INSERTs em `tests/{work-item-id}/safx_files/`
5. Gera `test_data_manifest.json` e executa `safx_archiver.py` para archive RC

**Resultados possiveis:**
- `SUITE_EXISTS` — cenario SuiteAutomation encontrado, SAFX nao necessaria (prosseguir para Phase 5.5)
- `GENERATED` — flat-files gerados com sucesso
- `NO_SAFX` — packages nao referenciam tabelas SAFX (prosseguir para Phase 5.5)
- `NO_PACKAGES` — nenhum package PL/SQL no branch

**Passo 2 - Validar output (se GENERATED):**
- Verificar que `tests/{work-item-id}/safx_files/` contem `.txt` flat-files
- Verificar que `test_data_manifest.json` foi gerado

**Passo 3 - Apresentar resultado:**

```markdown
## Phase 5.2 - Dados SAFX Gerados
- Tabelas: {lista}
- Flat-files: {N} arquivos
- Rows geradas: {N}
- Manifest: tests/{work-item-id}/test_data_manifest.json
```

---

## Phase 5.5 - Testes de Regressao SuiteAutomation

> **BACKGROUND:** Roda em BACKGROUND (`run_in_background=true`).

### Objetivo
Executar testes de regressao automatizados usando SuiteAutomation.

### Condicao
**CONDICIONAL** - Executada APENAS se `OPT_REGRESSION == true`.

### Auto-Skip Inteligente

| Sinal | Acao |
|-------|------|
| Nenhum mapeamento em `component-test-map.json` | **Auto-skip** |
| Score < 3 para todas suites | **Auto-skip** |
| Pre-requisitos indisponiveis (sem Java, sem Oracle local) | **Auto-skip** (warning) |

### REGRAS CRITICAS para SuiteAutomation

1. **SEMPRE sincronizar repo QA antes de criar cenarios:** Antes de criar XMLs ou flat files novos, atualizar `taxone_automacao_qa` (`git fetch origin` + verificar `origin/rc`) e buscar se ja existe cobertura para o componente. Se existir, usar/incrementar o existente.
2. **SEMPRE sincronizar XML e esperados do repo QA antes de rodar:** Copiar de `origin/rc` via `git show origin/rc:<path>`. Paths no repo QA: `arquivos/` (minusculo), local: `Arquivos/` (maiusculo).
3. **Se suite_runner reporta ERROR(0s) com 0 arquivos:** Rodar JAR diretamente: `cd suite-automation/jar && java -Dfile.encoding=Cp1252 -Dsun.jnu.encoding=ISO-8859-1 -jar SuiteTeste.jar "<xml_sem_drive>" "RA<range>" 'PRO"<title>"' "../config/suiteteste_LOCAL.properties"`

### Passos

#### 5.5.1 - Verificar Pre-Requisitos

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/suite_runner.py" --check-only --wi-id 0 --title "check" --xml dummy
```

#### 5.5.2 - Mapear Componente para Suites

Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/suite-automation/component-test-map.json`.

Calcular score: Keywords (peso 3), File paths (peso 5), Packages (peso 4).
Selecionar top 5 suites com score >= 3.

#### 5.5.3 - Confirmar e Lancar em Background

```
Agent(subagent_type="taxone-suite-runner", run_in_background=true)
```

Resultado coletado na Phase 8 via `TaskOutput(task_id=..., block=false)`.

---

## Phase 5.7 - Testes E2E Playwright

> **BACKGROUND:** Roda em BACKGROUND (`run_in_background=true`).

### Objetivo
Validar fluxos de UI/browser usando testes E2E Playwright.

### Condicao
**CONDICIONAL** - Executada APENAS se `OPT_E2E == true`.

### Auto-Skip Inteligente

| Sinal | Acao |
|-------|------|
| Nenhum mapeamento em `playwright-test-map.json` | Auto-skip |
| Score < 3 para todos | Auto-skip |
| Node.js/browsers nao instalados | Auto-skip (warning) |
| Alteracao exclusivamente DDL | Auto-skip |

### Passos

#### 5.7.1 - Verificar Pre-Requisitos

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/playwright_runner.py" --check-only
```

#### 5.7.1c - RUM Journey → E2E (se DD_RUM_USER_JOURNEY disponivel)

Se `tests/{WI_ID}/rum_enrichment_{WI_ID}.json` existir, executar ANTES do scoring manual:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/rum_to_e2e.py" --wi-id {WI_ID} --dry-run
```

Isso gera automaticamente: specs mapeados por scoring + spec ephemeral do user journey real.
Resultado em `tests/{WI_ID}/rum_to_e2e_result.json`. ADICIONAR esses specs aos da Phase 5.7.2.

#### 5.7.2 - Mapear e Scoring

Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/suite-automation/playwright-test-map.json` (v2.0.0).

Scoring fino com `menu_path` (peso 7), `screen_keywords` (peso 5), `file_path` (peso 5),
`package` (peso 4), `keyword` (peso 3).

#### 5.7.3 - Selecao por Score

| Score | Acao |
|-------|------|
| >= 7 (menu_path match) | Rodar SO os specs desse mapping |
| 3-7 (keyword/package match) | Rodar specs mapeados |
| < 3 para todos | Smoke fallback |

#### 5.7.4 - Confirmar e Lancar em Background

```
Agent(subagent_type="taxone-e2e-tester", run_in_background=true)
```

Resultado coletado na Phase 8 via `TaskOutput(task_id=..., block=false)`.

---

## Phase 6 - Code Review

> **PARALELO:** Roda em paralelo com Phase 4.5, 5, 5.5, 5.7.
> **GATE OBRIGATORIO:** Pipeline aguarda esta fase antes de Phase 7.

### Objetivo
Revisar todo o codigo implementado antes de criar o PR.

### Condicao
**OBRIGATORIO** — SEMPRE executada.

### Passos

#### 6.1 - Lancar Reviewer(s)

**Reviewer especializado por linguagem:**
- PL/SQL: `taxone-plsql-reviewer`
- PowerBuilder: `taxone-pb-reviewer`
- Java: `taxone-java-reviewer`
- Angular: `taxone-angular` (modo review)
- Multiplas linguagens: lancar reviewers correspondentes **em paralelo**.

Prompt backend:
```
Code review para Feature #{WI_ID}:

TITULO: {titulo}

REGRAS DE NEGOCIO IMPLEMENTADAS:
{resumo de business_rules.json + resultado de Phase 4.5}

ARQUIVOS CRIADOS: {lista}
ARQUIVOS MODIFICADOS: {lista}

DESIGN ORIGINAL: {design_proposto}

Por favor:
1. Carregar padroes de codigo (code-standards.md)
2. Revisar TODOS os arquivos
3. Verificar:
   - Seguranca PL/SQL (SQL injection, grants, dados sensiveis)
   - Qualidade PL/SQL (exception handling, cursores, transacoes)
   - Performance Oracle (bind variables, bulk operations, indices)
   - Convencoes do projeto
   - Aderencia ao design aprovado
   - Cobertura das regras de negocio
4. Pontuar confianca de cada issue (0-100)
5. Reportar APENAS issues com confianca >= 75
6. Emitir veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO
```

#### 6.2 - Processar Veredicto

| Veredicto               | Acao                                                              |
|-------------------------|-------------------------------------------------------------------|
| **APROVADO**            | Prosseguir para Phase 7                                           |
| **APROVADO COM RESSALVAS** | Apresentar ressalvas, perguntar se corrige ou prossegue        |
| **REPROVADO**           | Voltar para Phase 4 (max 3 iteracoes)                             |

**GATE adicional:** Se Phase 4.5 retornou **NO-GO**, abortar mesmo se review aprovou.

---

## Phase 6.5 - Compliance Check (Gate GO/NO-GO)

### Objetivo
Verificar seguranca e compliance do codigo antes de criar PR.

### Condicao
**OBRIGATORIO** — SEMPRE executada apos Phase 6 (Code Review).

### Passos

#### 6.5.1 - Lancar taxone-compliance

```
Agent(subagent_type="taxone-compliance")
```

Prompt:
```
Verificar compliance dos arquivos alterados na Feature #{WI_ID}.

Arquivos modificados:
{LISTA_ARQUIVOS_MODIFICADOS}

Repositorio: {TAXONE_DW_REPO}
Branch: MFS{WI_ID}
```

#### 6.5.2 - Processar Resultado

Salvar output em `tests/{WI_ID}/compliance_report.json`.

| Veredicto               | Acao                                                              |
|-------------------------|-------------------------------------------------------------------|
| **PASS**                | Prosseguir para Phase 7                                           |
| **PASS_WITH_WARNINGS**  | Alertar usuario sobre findings HIGH. Prosseguir se confirmar.     |
| **FAIL**                | **BLOQUEAR PR.** Voltar para Phase 4 com instrucoes de correcao.  |

Se FAIL: incrementar loop counter em `workflow_state.json`. Se loop >= 3: escalar para TechLead.

---

## Phase 7 - Commit, Push e PR

### Objetivo
Commitar as mudancas, fazer push e criar Pull Request no GitHub.

### Passos

#### 7.1 - Preparar Commit

```bash
git status
git diff --stat
```

Apresentar ao usuario a lista de arquivos e mensagem proposta:

```
Arquivos para commit:
{lista}

Mensagem de commit proposta:
"[DEV] MFS{work-item-id} - {descricao curta}

{descricao das mudancas - 2-3 linhas}

Regras implementadas: R01...Rnn
Reviewed-by: taxone-reviewer (AI)

AB#{work-item-id}"

Confirmar commit? (S/N)
```

**IMPORTANTE:** Arquivos de `tests/` NAO sobem para o GitHub. Sao evidencias locais.

#### 7.2 - Executar Commit

```bash
git add {lista de arquivos — excluir tests/}
git commit -m "$(cat <<'EOF'
[DEV] MFS{work-item-id} - {descricao curta}

{descricao das mudancas}

Regras implementadas: R01...Rnn
Reviewed-by: taxone-reviewer (AI)

AB#{work-item-id}
EOF
)"
```

#### 7.3 - Push

```bash
git push -u origin "MFS{work-item-id}"
```

#### 7.4 - Criar Pull Request

```bash
gh pr create \
  --title "[DEV] MFS{work-item-id} - {descricao curta}" \
  --body "$(cat <<'EOF'
## User Story/Feature

**#{work-item-id}** - {titulo}
**Link ADO:** https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/{work-item-id}

## Regras de Negocio Implementadas

| ID  | Descricao | Status |
|-----|-----------|--------|
| R01 | {descricao} | Implementada |
| R02 | {descricao} | Implementada |

## Design Arquitetural

{resumo do design — packages/objetos}

## Analise DBA

{resumo DBA ou "N/A"}

## Arquivos Modificados

{lista com descricao breve}

## Scripts DDL

{lista ou "N/A"}

## Testes

{resumo dos testes ou "N/A"}

## Code Review

**Veredicto:** {veredicto}
{resumo}

## Cobertura de Regras (Phase 4.5)

**Cobertura:** {coverage_pct}%
**Decisao:** {GO/NO-GO}

## Checklist

- [x] Analise de escopo PM (Phase 1)
- [x] Regras de negocio formalizadas (Phase 1.5)
- [x] Design arquitetural (Phase 2)
- [{x}] Analise DBA Oracle (Phase 2.5)
- [x] Implementacao (Phase 4)
- [x] Verificacao de cobertura de regras (Phase 4.5)
- [{x}] Scripts de teste SQL (Phase 5)
- [x] Code review (Phase 6)
- [x] Tags: AI-Implemented, SUST-IA-CLAUDE

---
> Implementacao automatizada via pipeline `taxone-us-implement`

AB#{work-item-id}
EOF
)" \
  --base DEV
```

**NUNCA fazer merge.** Apenas criar a PR.

#### 7.5 - Registrar URL

Capturar URL do PR e apresentar ao usuario.

---

## Phase 7.5 - Pacote Unitario (GitHub Actions)

### Objetivo
Disparar workflow de geracao de pacote unitario no repositorio `tr/taxone_automacao_fab`.

### Condicao
**CONDICIONAL** - Executada SOMENTE se arquivos modificados incluem `ws_objects/` ou `artifacts/sp/`.

### Logica de Decisao

| Arquivos modificados | Workflow | Tipo | Acao |
|---------------------|----------|------|------|
| `ws_objects/**` (PowerBuilder) | Workflow 1 (ID: 154750734) | `F` | Full Build |
| `artifacts/sp/**` (PL/SQL/BD) | Workflow 3 (ID: 154753513) | `P` | Banco |
| Ambos | Workflow 1 (ID: 154750734) | `F` | Full Build |
| Apenas `artifacts/java/**` | Nenhum | - | PULAR |

### Passos

1. Classificar arquivos modificados
2. Confirmar com usuario
3. Disparar workflow:
```bash
"/c/Program Files/GitHub CLI/gh.exe" workflow run {WORKFLOW_ID} \
  -f Tipo={TIPO} \
  -f MFS=MFS{work-item-id} \
  -R tr/taxone_automacao_fab
```
4. Verificar inicio da execucao (30s)
5. Registrar RUN_ID e continuar (NAO bloquear)

---

## Phase 8 - Atualizar ADO e Relatorio Final

### Objetivo
Atualizar o work item no Azure DevOps e apresentar relatorio final.

### Passos

#### 8.0 - Coletar Resultados Background (5.5 e 5.7)

Para cada agente em background:
```
TaskOutput(task_id=..., block=false, timeout=5000)
```
Se indisponivel: retry com `block=true, timeout=30000`. Se ainda nao completou: "Em execucao".

#### 8.1 - Preparar Tags

Tags a adicionar:
- `SUST-IA-CLAUDE` (SEMPRE)
- `AI-Implemented` (SEMPRE)
- `SUST-IA-CLAUDE-REGRA` (se Phase 4.5 indicou `business_rule_tag_needed` ou keywords de regra)

```bash
CURRENT_TAGS=$(curl -s \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{ID}?api-version=7.1" \
  | python -c "import sys,json; print(json.load(sys.stdin)['fields'].get('System.Tags',''))")

NEW_TAGS="$CURRENT_TAGS"
# Adicionar tags que nao existem ainda
for TAG in "SUST-IA-CLAUDE" "AI-Implemented"; do
  if [[ "$NEW_TAGS" != *"$TAG"* ]]; then
    NEW_TAGS="$NEW_TAGS; $TAG"
  fi
done
# Se regra:
if [ "$NEEDS_REGRA_TAG" = "true" ] && [[ "$NEW_TAGS" != *"SUST-IA-CLAUDE-REGRA"* ]]; then
  NEW_TAGS="$NEW_TAGS; SUST-IA-CLAUDE-REGRA"
fi
```

#### 8.2 - Release Notes (Template Automatico)

**REGRA:** Se o campo `Custom.DescriptionofReleaseNotes` ja estiver preenchido, NAO sobrescrever.

Se vazio, aplicar o template da Carta do Patch:
- Formato texto simples com bold nos labels e `<br>` para quebras de linha
- Extrair Modulo, Menu e Descricao dos dados da WI
- Ver `memory/release-notes-template.md` para formato exato

#### 8.2b - Description of Root Cause (OBRIGATORIO)

**REGRA:** SEMPRE preencher o campo `Custom.DescriptionofRootCause` ao concluir analise/implementacao.
- Texto descritivo da causa raiz ou da motivacao tecnica da feature
- Para bugs: descrever exatamente o que causava o problema e onde no codigo
- Para features: descrever o gap funcional que a feature resolve
- Pode usar `<br>` para quebras de linha, sem HTML complexo
- **NUNCA esquecer este campo** — ele e cobrado na revisao da WI

#### 8.3 - Atualizar Campos do Work Item

```bash
curl -s -X PATCH \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -H "Content-Type: application/json-patch+json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{ID}?api-version=7.1" \
  -d '[
    {"op": "replace", "path": "/fields/System.Tags", "value": "{NEW_TAGS}"},
    {"op": "replace", "path": "/fields/Custom.Solutions", "value": "{INTERNAL_COM_HTML}"},
    {"op": "replace", "path": "/fields/Custom.DeveloperText", "value": "taxone-reviewer (AI Pipeline)"},
    {"op": "replace", "path": "/fields/TR.WOW.AIPowered", "value": "true"},
    {"op": "replace", "path": "/fields/Custom.DescriptionofReleaseNotes", "value": "{RELEASE_NOTES}"},
    {"op": "replace", "path": "/fields/Custom.DescriptionofRootCause", "value": "{FEATURE_DESCRIPTION_HTML}"}
  ]'
```

#### 8.3a - Conteudo do InternalCom (Custom.Solutions)

```html
<div>
  <h3>Pipeline AI - Implementacao de Feature</h3>
  <p><strong>Data:</strong> {data-hora}</p>
  <p><strong>Work Item:</strong> #{ID} - {titulo}</p>
  <p><strong>Branch:</strong> MFS{work-item-id}</p>
  <p><strong>PR:</strong> <a href="{PR_URL}">{PR_URL}</a></p>

  <h4>Regras de Negocio ({total_rules})</h4>
  <ul>
    <li>R01: {descricao} — {IMPLEMENTED}</li>
    <li>R02: {descricao} — {IMPLEMENTED}</li>
  </ul>
  <p><strong>Cobertura:</strong> {coverage_pct}%</p>

  <h4>Fases Executadas</h4>
  <ul>
    <li>Phase 1 - Analise de Escopo: {verdito}</li>
    <li>Phase 1.5 - Regras Formalizadas: {N} regras</li>
    <li>Phase 2 - Design Arquitetural: Concluido</li>
    <li>Phase 2.5 - Analise DBA: {Concluida/Nao solicitada}</li>
    <li>Phase 4 - Implementacao: Concluida</li>
    <li>Phase 4.5 - Cobertura de Regras: {GO/NO-GO} ({coverage_pct}%)</li>
    <li>Phase 5 - Testes SQL: {Concluidos/Nao solicitados}</li>
    <li>Phase 5.5 - Regressao: {status}</li>
    <li>Phase 5.7 - E2E Playwright: {status}</li>
    <li>Phase 6 - Code Review: {veredicto}</li>
  </ul>

  <h4>Arquivos Modificados</h4>
  <ul>{lista de arquivos}</ul>
</div>
```

#### 8.3b - Discussion Comments (Templates Padronizados)

Usar o modulo centralizado `scripts/ado_discussion_templates.py` para gerar e postar comments padronizados.

**Comment 1: Analise & Implementacao**

```python
from scripts.ado_discussion_templates import build_analysis_comment, post_discussion_comment

html = build_analysis_comment(
    wi_id=WI_ID, wi_title=WI_TITLE,
    pipeline="taxone-us-implement",
    analysis={"causa_raiz": "...", "veredicto": "...", "impacto": "..."},
    implementation={"branch": "MFS{WI_ID}", "pr_url": PR_URL, "pr_number": N,
                    "files": [...], "ddls": [], "code_review": "PASS", "compilacao": "COMPILADO"},
    phases=[{"name": "Phase N - ...", "status": "PASS", "duration": "..."}],
    pendencias=[],
    zendesk=None,  # ou {"ticket_id": "...", "status": "...", "resumo": "..."}
)
post_discussion_comment(WI_ID, html)
```

**Comment 2: Resultados de Testes** (postar apos Phase 5/5.5)

```python
from scripts.ado_discussion_templates import build_test_results_comment, post_discussion_comment

html = build_test_results_comment(
    wi_id=WI_ID, wi_title=WI_TITLE,
    agent="taxone-us-implement",
    db_connection="V2R010AC@localhost:1521/MFSPDB",
    manual_tests=[{"num": 1, "cenario": "...", "status": "PASS", "detalhe": "..."}],
    suite_results={"xml": "...", "range": "...", "total": N, "passed": N, "failed": 0,
                   "duration_s": 0, "verdict": "PASS", "failures": []},
    nao_testado=[],
    attachments=[{"filename": "...", "url": "..."}],
)
post_discussion_comment(WI_ID, html)
```

Os templates geram HTML padronizado com paleta de cores consistente.
**Imagens inline:** Upload via `_apis/wit/attachments`, montar `<img src="{url}">` no HTML.

#### 8.3c - Attachments (Evidencias) — OBRIGATORIO

**REGRA:** NUNCA concluir uma WI sem anexar evidencias de teste. Se rodou teste, DEVE anexar na WI e postar na Discussion.

**Passo 1 - Executar testes de validacao** e salvar resultados em `tests/{WI_ID}/`:
- Script de teste (`run_tests.py` ou similar)
- JSON com resultados (`test_results.json`)
- Analise de causa raiz (`root_cause_analysis.md`)
- Screenshots, relatorios, qualquer artefato gerado

**Passo 2 - Upload de TODOS os arquivos** de `tests/{WI_ID}/` como Attachments na WI via REST API (`_apis/wit/attachments`).

**Passo 3 - Postar Discussion comment** com tabela de resultados (PASS/FAIL/SKIP) — usar o template de Comment 2 acima.

Usar `requests` (Python) para uploads — `curl` via `subprocess` falha com binarios no Windows.

**Motivo:** Na WI #1086591, evidencias de teste foram esquecidas — apenas compilacao foi feita mas nenhum teste/upload/comment foi anexado. Isso invalida a entrega.

#### 8.4 - Relatorio Final

```
==========================================================
  RELATORIO FINAL - PIPELINE DE FEATURES
==========================================================

  Work Item: #{ID} - {titulo}
  Branch:    MFS{work-item-id}
  PR:        {PR_URL}
  ADO:       https://dev.azure.com/tr-ggo/.../edit/{ID}

----------------------------------------------------------
  REGRAS DE NEGOCIO
----------------------------------------------------------

  Total: {N} regras | Cobertura: {coverage_pct}%
  {tabela R01...Rnn com status}

----------------------------------------------------------
  FASES EXECUTADAS
----------------------------------------------------------

  [OK] Phase 0   - Work item carregado do ADO
  [OK] Phase 1   - Analise de escopo: {verdito}
  [OK] Phase 1.5 - Regras formalizadas: {N} regras
  [OK] Phase 2   - Design arquitetural
  [{s}] Phase 2.5 - Analise DBA
  [OK] Phase 3   - Branch: MFS{work-item-id}
  [OK] Phase 4   - Implementacao (criacao de codigo novo)
  [OK] Phase 4.5 - Cobertura de regras: {GO} ({coverage_pct}%)
  [{s}] Phase 5   - Testes SQL
  [{s}] Phase 5.5 - Regressao SuiteAutomation
  [{s}] Phase 5.7 - Testes E2E Playwright
  [OK] Phase 6   - Code Review: {veredicto}
  [OK] Phase 7   - Commit + Push + PR criado
  [{s}] Phase 7.5 - Pacote Unitario
  [OK] Phase 8   - ADO atualizado

----------------------------------------------------------
  RESUMO DAS MUDANCAS
----------------------------------------------------------

  Arquivos criados:     {N}
  Arquivos modificados: {N}
  Scripts DDL:          {N}
  Scripts de teste:     {N}

----------------------------------------------------------
  PROXIMOS PASSOS
----------------------------------------------------------

  1. Revisar o PR no GitHub: {PR_URL}
  2. Acompanhar pacote unitario: {PKG_RUN_URL ou "N/A"}
  3. Executar scripts DDL em DEV/QA (se houver)
  4. Validar regras de negocio no ambiente
  5. Aprovar e mergear o PR (responsabilidade do usuario)

==========================================================
  Pipeline concluido com sucesso!
==========================================================
```

---

## Phase 9 - Compound Engineering

### Objetivo
Atualizar a knowledge base com o aprendizado desta implementacao.

### Condicao
**OPCIONAL** - Executada APENAS se `OPT_COMPOUND == true`.

### Passos

1. Analisar implementacao e identificar oportunidades:
   - Nova feature/modulo documentavel
   - Novos patterns
   - Novas business rules para knowledge base
   - Integracoes cross-module

2. Propor atualizacao ao usuario

3. Se aprovado, sugerir: `/taxone-compound`

**O orquestrador NAO atualiza knowledge diretamente.**

---

## Phase 9.5 - Archival SAFX para RC

### Objetivo
Exportar dados SAFX do banco com formatacao SAF_EXPORTA_TAB para reproducao em RC.

### Condicao de entrada
`tests/{work-item-id}/safx_files/` existe com flat-files gerados na Phase 5.2.

Se nao existe `tests/{work-item-id}/safx_files/`: **SKIP esta fase**.

### Passos

**Passo 1 - Executar safx_archiver:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/safx_archiver.py --wi-id ${work-item-id} --env LOCAL
```

**Passo 2 - Upload para ADO:**
- Anexar todos os arquivos de `tests/{work-item-id}/safx_archive_rc/` como Attachments na WI
- Postar Discussion comment com lista de arquivos e instrucoes de importacao RC

**Passo 3 - Apresentar resultado:**

```markdown
## Phase 9.5 - SAFX Arquivado para RC
- Arquivos: {lista}
- Upload ADO: {OK/FAIL}
- Instrucoes RC: Importar flat-files via PKG_IMP_ONLINE_FPROC
```

---

### Phase 9.6 - Publicar Cenarios no Repo QA (OBRIGATORIO)

**Objetivo:** Publicar artefatos de teste no repositorio `taxone_automacao_qa` para rastreabilidade e reuso.

**Passo 1 - Preparar artefatos:**
- Coletar todos os arquivos de `tests/{work-item-id}/` (scripts SQL, outputs, screenshots, test_scenarios.json, SAFX files)
- Se `test_data_manifest.json` existe, incluir na publicacao

**Passo 2 - Publicar no repo QA:**

```bash
QA_REPO="C:/@@Dev/Git/taxone_automacao_qa"
WI_ID={work-item-id}

# Garantir repo atualizado
cd "$QA_REPO" && git checkout rc && git pull origin rc

# Criar branch
git checkout -b "MFS${WI_ID}"

# Copiar artefatos
mkdir -p "cenarios/${WI_ID}"
cp -r "C:/Claude/Taxone_support/taxone-support-dev/tests/${WI_ID}/"* "cenarios/${WI_ID}/"

# Commit e push
git add "cenarios/${WI_ID}/"
git commit -m "MFS${WI_ID} - Cenarios de teste"
git push origin "MFS${WI_ID}"
```

**Passo 3 - Criar PR no repo QA:**
- Base: `rc`
- Titulo: `[RC] MFS{work-item-id} - Cenarios de teste`
- Body: lista de arquivos publicados + link para WI do ADO

**Passo 4 - Apresentar resultado:**

```markdown
## Phase 9.6 - Cenarios Publicados no Repo QA
- Branch: MFS{work-item-id}
- Arquivos: {lista}
- PR: {URL}
- Repo: taxone_automacao_qa
```

**Se `qa_test_publisher.py` estiver disponivel e `test_data_manifest.json` existir**, usar o script ao inves do fluxo manual:
```bash
python scripts/qa_test_publisher.py --wi-id {work-item-id} --source tests/{work-item-id}/
```

---

## Tratamento de Erros

### Tabela de Erros e Acoes

| Situacao                                | Fase      | Acao                                                                     |
|-----------------------------------------|-----------|--------------------------------------------------------------------------|
| `ADO_PAT` nao configurado              | Phase 0   | PARAR. Informar para configurar.                                         |
| Work Item nao encontrado (404)          | Phase 0   | PARAR. Perguntar novo ID.                                                |
| Work Item sem descricao                 | Phase 0   | ALERTAR. Perguntar se continua.                                          |
| Work Item fora do TAX ONE              | Phase 0   | ALERTAR. Perguntar se continua.                                          |
| Query retorna 0 resultados             | Phase 0.5 | PARAR. Informar query vazia.                                             |
| PM retorna SCOPE_INCOMPLETE            | Phase 1   | GATE. Devolver PO/BA ou pedir info.                                      |
| PM retorna SCOPE_AMBIGUOUS             | Phase 1   | GATE. Pedir esclarecimento.                                              |
| PM retorna REDIRECTED_BUG              | Phase 1   | GATE. Sugerir /taxone-auto-fix.                                          |
| Architect nao gera business_rules.json | Phase 1.5 | RETRY 1x. Se falhar, pedir input manual.                                |
| Architect nao retorna design           | Phase 2   | RETRY 1x. Se falhar, pedir design manual.                               |
| DBA identifica risco critico           | Phase 2.5 | ALERTAR. Perguntar se prossegue.                                         |
| Branch ja existe                       | Phase 3   | Perguntar: deletar/recriar ou usar existente.                            |
| Mudancas pendentes no workspace        | Phase 3   | Perguntar: stash/commit/abortar.                                         |
| Developer nao cria arquivos            | Phase 4   | RETRY 1x. Se falhar, reportar.                                          |
| Cobertura de regras < 80%             | Phase 4.5 | GATE. Voltar Phase 4 ou aceitar.                                         |
| Tester falha                           | Phase 5   | ALERTAR. Continuar (opcional).                                           |
| Review REPROVADO                       | Phase 6   | Voltar Phase 4 (max 3 iteracoes).                                        |
| `git push` falha                       | Phase 7   | PARAR. Informar erro.                                                    |
| `gh pr create` falha                   | Phase 7   | RETRY 1x. Fornecer cmd manual.                                          |
| Workflow falha                         | Phase 7.5 | RETRY 1x. Nao bloqueia pipeline.                                        |
| ADO update falha (403)                 | Phase 8   | ALERTAR. Fornecer dados para manual.                                     |
| test-data-engineer falha               | Phase 5.2 | ALERTAR. SKIP SAFX e continuar pipeline.                                 |
| safx_archiver falha                    | Phase 9.5 | ALERTAR. SKIP archival e continuar pipeline.                             |

### Principios

1. **NUNCA falhar silenciosamente.** Todo erro reportado ao usuario.
2. Erros em fases opcionais (2.5, 5, 5.5, 5.7, 7.5, 9) NAO bloqueiam pipeline.
3. Erros em fases obrigatorias (0, 1, 1.5, 2, 4, 4.5, 6, 7) BLOQUEIAM.
4. Sempre oferecer alternativa ao usuario.
5. Registrar todos os erros no relatorio final.
6. NUNCA expor tokens/PATs.

### Retry Policy

| Fase      | Max Retries | Acao apos falha final                    |
|-----------|-------------|------------------------------------------|
| Phase 0   | 2           | Parar pipeline                           |
| Phase 1   | 1           | Parar pipeline (escopo obrigatorio)      |
| Phase 1.5 | 1           | Pedir regras manualmente                 |
| Phase 2   | 1           | Pedir design manual                      |
| Phase 2.5 | 1           | Pular fase                               |
| Phase 4   | 2           | Parar pipeline                           |
| Phase 4.5 | 1           | Pedir verificacao manual                 |
| Phase 5   | 1           | Pular fase                               |
| Phase 6   | 3           | Parar pipeline                           |
| Phase 7   | 1           | Fornecer comandos manuais                |
| Phase 7.5 | 1           | Pular fase                               |
| Phase 8   | 2           | Fornecer dados para update manual        |

---

## Apendice A - Exemplos de Chamadas ADO API

### Buscar Work Item por ID

```bash
curl -s \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/54321?\$expand=all&api-version=7.1"
```

### Executar Query por ID

```bash
curl -s \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/wiql/9bb6e572-8580-4eb3-86e6-a56bc5303d69?api-version=7.1"
```

### Buscar Multiplos Work Items

```bash
curl -s \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems?ids=111,222,333&\$expand=all&api-version=7.1"
```

### Atualizar Work Item (PATCH)

```bash
curl -s -X PATCH \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -H "Content-Type: application/json-patch+json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/54321?api-version=7.1" \
  -d '[
    {"op": "replace", "path": "/fields/System.Tags", "value": "SUST-IA-CLAUDE; AI-Implemented"},
    {"op": "replace", "path": "/fields/Custom.Solutions", "value": "<div>Conteudo</div>"},
    {"op": "replace", "path": "/fields/Custom.DeveloperText", "value": "taxone-reviewer (AI Pipeline)"},
    {"op": "replace", "path": "/fields/TR.WOW.AIPowered", "value": "true"}
  ]'
```

### Adicionar Comentario

```bash
curl -s -X POST \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -H "Content-Type: application/json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/54321/comments?api-version=7.1-preview.4" \
  -d '{"text": "<div>Comentario</div>"}'
```

---

## Apendice B - Template de Branch e Commit

### Branch

```
MFS{work-item-id}
```

Exemplos:
- `MFS1058668`
- `MFS1058668a` (correcao adicional)

### Commit Message

```
[DEV] MFS{work-item-id} - {descricao curta max 72 chars}

{descricao das mudancas em 2-5 linhas}

Regras implementadas: R01, R02, R03...
Reviewed-by: taxone-reviewer (AI)

AB#{work-item-id}
```

### PR Title

```
[DEV] MFS{work-item-id} - {descricao curta}
```

### PR Body Last Line

```
AB#{work-item-id}
```

---

## Apendice C - Diferenca Bug Fix vs Feature

| Aspecto | Bug Fix (auto-fix) | Feature (us-implement) |
|---------|-------------------|----------------------|
| Pergunta central | "O que esta quebrado?" | "Qual o escopo/regras?" |
| PM Phase | Triage (is it a bug?) | Scope Analysis (is scope clear?) |
| Verditos PM | CONFIRMED_BUG, NOT_A_BUG, FEATURE_REQUEST... | SCOPE_CLEAR, SCOPE_INCOMPLETE, SCOPE_AMBIGUOUS, REDIRECTED_BUG |
| Phase 1.5 | Nao existe | Business Rules formalizadas em JSON |
| Architect (Ph 2) | "O que causa o problema?" | "Como construir a solucao?" |
| Developer (Ph 4) | "Corrigir codigo existente" | "Criar codigo novo" |
| Phase 4.5 | "Fix nao quebrou regras?" | "TODAS regras foram implementadas?" |
| Branch | `MFS{id}` | `MFS{id}` |
| Tags | SUST-IA-CLAUDE, AI-Fixed | SUST-IA-CLAUDE, AI-Implemented, SUST-IA-CLAUDE-REGRA |

---

## Apendice D - Checklist Pre-Pipeline

Antes de executar o pipeline, verificar:

- [ ] `ADO_PAT` configurado como variavel de ambiente
- [ ] `gh auth status` retorna autenticado
- [ ] `git config user.name` e `git config user.email` configurados
- [ ] Repositorio TAX ONE clonado e atualizado
- [ ] Branch base (DEV ou main) sem mudancas pendentes
- [ ] Work Item ID ou Query ID em maos
- [ ] Work Item e do tipo User Story ou Feature (NAO Bug)
