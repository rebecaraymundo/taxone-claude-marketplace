---
name: taxone-us-auto-implement
deprecated: true
description: >
  Pipeline automatizado de implementacao de User Stories/Features do Azure DevOps para o projeto TAX ONE.
  Busca work items do ADO, executa analise arquitetural, analise DBA (Oracle), implementacao em PL/SQL/PowerBuilder/Java,
  code review, cria PR no GitHub e atualiza o work item. Suporta entrada por ID, URL ou Query do ADO.
version: 3.0.0
---

> **DEPRECADO**: Este pipeline sera descontinuado. Use `/taxone-us-implement` (v1.1.0).

# TAX ONE - Pipeline de Implementacao Automatizada de User Stories

Pipeline orquestrado para implementacao end-to-end de User Stories e Features do Azure DevOps
no projeto TAX ONE (Mastersaf Fiscal Solutions) da Thomson Reuters.

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
9. [Phase 0.8 - Triagem PM](#phase-08---triagem-pm-gate-de-qualidade)
10. [Phase 0.9 - SM Allocation Check](#phase-09---sm-allocation-check)
11. [Phase 1 - Knowledge e Alinhamento](#phase-1---knowledge-e-alinhamento)
8. [Phase 2 - Analise Arquitetural](#phase-2---analise-arquitetural)
9. [Phase 2.5 - Analise DBA Oracle](#phase-25---analise-dba-oracle)
10. [Phase 3 - Workspace e Branch](#phase-3---workspace-e-branch)
11. [Phase 4 - Implementacao](#phase-4---implementacao)
12. [Phase 4.5 - Analise de Impacto em Regras de Negocio](#phase-45---analise-de-impacto-em-regras-de-negocio)
13. [Phase 5 - Testes SQL de Validacao](#phase-5---testes-sql-de-validacao)
14. [Phase 5.5 - Testes de Regressao SuiteAutomation](#phase-55---testes-de-regressao-suiteautomation)
15. [Phase 5.7 - Testes E2E Playwright](#phase-57---testes-e2e-playwright)
16. [Phase 6 - Code Review](#phase-6---code-review)
14. [Phase 7 - Commit, Push e PR](#phase-7---commit-push-e-pr)
15. [Phase 7.5 - Pacote Unitario (GitHub Actions)](#phase-75---pacote-unitario-github-actions)
16. [Phase 8 - Atualizar ADO e Relatorio Final](#phase-8---atualizar-ado-e-relatorio-final)
16. [Phase 9 - Compound Engineering](#phase-9---compound-engineering)
17. [Tratamento de Erros](#tratamento-de-erros)

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
| InternalCom field      | `Custom.Solutions`                                                  |
| DevReviewName field    | `Custom.DeveloperText`                                                |
| AcceptanceCriteria field | `Microsoft.VSTS.Common.AcceptanceCriteria`                          |
| ReleaseNotes field     | `Custom.DescriptionofReleaseNotes`                                    |
| RootCause field        | `Custom.DescriptionofRootCause`                                       |
| DD Org                 | `trta-onesource` (via MCP Server `datadog`, auth OAuth)                |
| DD MCP Server          | `datadog` (remote HTTP, `~/.claude.json` mcpServers)                   |
| DD Permissao           | MCP Read (somente leitura)                                             |
| PR Target Branch       | `DEV`                                                                 |
| Branch Pattern         | `MFS{work-item-id}` (sufixos: a, b, c para correcoes adicionais)      |

### Agentes Permitidos

| Agente              | Funcao                                    | Fase     |
|---------------------|-------------------------------------------|----------|
| `taxone-pm`         | Triagem e classificacao de WIs            | Phase 0.8|
| `taxone-architect`  | Analise arquitetural e design             | Phase 2  |
| `taxone-dba`        | Analise de impacto Oracle/DBA             | Phase 2.5|
| `taxone-plsql`      | Implementacao PL/SQL (packages, procedures, views) | Phase 4 |
| `taxone-pb`         | Implementacao PowerBuilder (DataWindows, scripts)   | Phase 4 |
| `taxone-java`       | Implementacao Java (web services, Jasper, servlets) | Phase 4 |
| `taxone-tester`     | Scripts SQL de validacao e testes manuais | Phase 5  |
| `taxone-suite-runner`| Testes de regressao SuiteAutomation      | Phase 5.5|
| `taxone-e2e-tester` | Testes E2E Playwright (browser)           | Phase 5.7|
| `taxone-plsql-reviewer` | Code review PL/SQL Oracle             | Phase 6  |
| `taxone-pb-reviewer`    | Code review PowerBuilder              | Phase 6  |
| `taxone-java-reviewer`  | Code review Java                      | Phase 6  |
| `taxone-angular`    | Implementacao + Review Angular 11 frontend| Phase 4, Phase 6 |
| `taxone-sm`         | Alocacao avulsa de Dev/Tester por afinidade| Phase 0.9|

### Caminhos do Knowledge

| Caminho                                                | Conteudo                              |
|--------------------------------------------------------|---------------------------------------|
| `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/`        | Visao geral, tech stack, patterns     |
| `${CLAUDE_PLUGIN_ROOT}/knowledge/features/`            | Knowledge por feature/modulo          |
| `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/`         | Padroes de codigo, nomenclatura       |

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
  - `System.Tags` (adicionar `AI-Implemented`)
  - `Custom.Solutions` (relatorio interno)
  - `Custom.DeveloperText` (nome do reviewer)
  - `System.State` (transicao de estado, quando aplicavel)
  - `Microsoft.VSTS.Common.AcceptanceCriteria` (criterios de aceitacao)
  - `Custom.DescriptionofReleaseNotes` (descricao para release notes)
  - `Custom.DescriptionofRootCause` (causa raiz do problema)
  - Discussion comments (relatorio completo do pipeline)

### R4 - Controle de Branch e PR

- Branch SEMPRE segue o pattern: `MFS{work-item-id}`
  - `{user}` = nome do usuario Git configurado (obtido via `git config user.name` ou perguntado)
  - `{work-item-id}` = ID numerico do work item do ADO
- Target branch do PR: SEMPRE `main`
- PR criado via `gh pr create` (GitHub CLI)
- Titulo do PR: `[#{work-item-id}] {titulo-da-us}`
- Body do PR deve conter: link para o work item, resumo das mudancas, lista de arquivos

### R5 - Nao Existe Build Local

O TAX ONE e um sistema PL/SQL/PowerBuilder/Java. **NAO existe processo de build/compilacao local.**
- NAO tentar rodar `mvn`, `gradle`, `make`, `npm` ou qualquer build tool
- NAO tentar compilar PL/SQL localmente (compilacao ocorre no Oracle Server)
- NAO tentar compilar PowerBuilder localmente
- Validacao de codigo e feita por: analise estatica (reviewer) + scripts SQL de validacao (tester)

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
Phase 0.8 : Triagem PM (taxone-pm) - gate de qualidade                       ──> GATE
     └──> NOT_A_BUG / FEATURE_REQUEST / INCOMPLETE / DUPLICATE → encerrar
     └──> CONFIRMED_BUG → continuar pipeline
Phase 1   : Carregar knowledge + alinhar com usuario (confirmar opcoes)
Phase 2   : Analise arquitetural (taxone-architect)                ──┐ PARALELO
Phase 2.5 : Analise DBA Oracle (taxone-dba) [CONDICIONAL+AUTO]    ──┘
     └──> Consolidar design (merge architect + DBA)
Phase 3   : Criar workspace + branch
Phase 4   : Implementacao (taxone-developer)
Phase 4.5 : Analise de Impacto em Regras de Negocio [COND+AUTO]   ──┐
Phase 5   : Testes SQL de validacao (taxone-tester) [CONDICIONAL]  ──┤ PARALELO
Phase 5.5 : Testes de regressao SuiteAutomation [COND+AUTO+BG]    ──┤ (5.5 em background)
Phase 5.7 : Testes E2E Playwright [COND+AUTO+BG]                  ──┤ (5.7 em background)
Phase 6   : Code review (taxone-reviewer) [OBRIGATORIO]            ──┘
     └──> Aguardar Phase 6 (gate obrigatorio). Se 4.5=NO-GO, abortar.
Phase 7   : Commit + push + PR (gh pr create)
Phase 7.5 : Pacote Unitario (GitHub Actions) [CONDICIONAL]
Phase 8   : Atualizar ADO + relatorio final (inclui resultado 5.5 + 5.7 background)
Phase 9   : Compound Engineering [OPCIONAL]
```

### Fluxo de Decisao (Otimizado)

```
                    +-------------------+
                    |   Phase 0/0.5     |
                    | Buscar Work Item  |
                    +--------+----------+
                             |
              +--------------+---------------+
              |              |               |
     +--------v------+ +----v--------+ +----v--------+
     |  Phase 0.6    | | Phase 0.7   | | FAQ Triage  |
     | Zendesk       | | Datadog     | | (local)     |
     | [PARALELO]    | | [PARALELO]  | | [PARALELO]  |
     +--------+------+ +----+--------+ +----+--------+
              |              |               |
              +--------------+---------------+
                             |
                    +--------v----------+
                    |    Phase 0.8      |
                    |   taxone-pm       |
                    | [GATE QUALIDADE]  |
                    +--------+----------+
                             |
          +--------+---------+----------+-----------+
          |        |         |          |           |
     NOT_A_BUG  FEATURE  INCOMPLETE  DUPLICATE  CONFIRMED  NEEDS_INFO
       ↓          ↓         ↓          ↓         ↓          ↓
     [Tag +    [Inform  [Devolver  [Fechar +  Continuar  [Perguntar
      Encerrar] usuario   N1/N2     Ref WI]   pipeline    +ANALISE]
      NOT-BUG]  +REGRA    +ANALISE]
                se regra]
                                                  |
                    +--------v----------+
                    |     Phase 1       |
                    | Knowledge + Align |
                    | [Perguntar user:  |
                    |  Testes? DBA?]    |
                    +--------+----------+
                             |
              +--------------+---------------+
              |                              |
     +--------v----------+      +-----------v----------+
     |     Phase 2       |      |     Phase 2.5        |
     | taxone-architect  |      | taxone-dba            |
     | [PARALELO]        |      | [PARALELO, se ativo]  |
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
                |  Branch + Setup   |
                +--------+----------+
                         |
                +--------v----------+
                |     Phase 4       |
                | taxone-developer  |
                +--------+----------+
                         |
     +---+-------+-------+-------+--------+
     |           |               |         |
  +--v-----+ +--v------+ +------v--+ +----v-------+
  |Ph 4.5  | |Phase 5  | |Ph 5.5   | |  Phase 6   |
  |BizRules | |Tester   | |Suite    | |  Reviewer  |
  |[PARAL.] | |[PARAL.] | |[BG]    | |  [PARAL.]  |
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
  Como voce gostaria de buscar a User Story?
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

**Se o titulo contiver TKT, a Phase 0.6 adicionara o contexto do Zendesk logo abaixo.**

#### 0.4.1 - Buscar Requisitos de WIs Filhas (Children)

**OBRIGATORIO quando a WI possuir filhos (relations com `System.LinkTypes.Hierarchy-Forward`).**

Objetivo: WIs do tipo User Story/Feature frequentemente possuem WIs filhas (Tasks, Requirements) que
contem a **especificacao detalhada da regra de negocio**. Esses requisitos devem ser carregados
para que a analise e implementacao reflitam a regra mais atualizada.

1. Extrair IDs dos filhos das `relations` do work item principal:
   ```bash
   # Filtrar relations do tipo Hierarchy-Forward para obter IDs dos filhos
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
   fases subsequentes (Phase 1, 2, 4, etc.). Se a WI filha contiver uma especificacao de regra de
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
>
> ```
> # Lancar em paralelo (mesmo bloco de tool calls):
> Agent 1: Phase 0.6 - Enriquecer com Zendesk (se TKT no titulo)
> Agent 2: Phase 0.7 - Enriquecer com Datadog (se keywords de performance)
> Agent 3: FAQ Triage local (faq_triage.py) - executar via Bash em paralelo
>
> # Aguardar resultados de todos antes de Phase 1
> # Se Agent falhar, tratar individualmente (fault-tolerant)
> ```

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

Da resposta da query, extrair os IDs e buscar detalhes em batch:

```bash
# Extrair IDs da resposta da query (campo workItems[].id)
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

**Se o usuario selecionar "todos":**
- Processar cada work item sequencialmente (Phase 0.3 → Phase 8 para cada)
- Apresentar relatorio consolidado no final

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
# Extrair numero do ticket usando python (compativel com Windows/git-bash)
TKT_NUM=$(echo "$WI_TITLE" | python -c "import sys,re; m=re.search(r'TKT\s*(\d+)', sys.stdin.read()); print(m.group(1) if m else '')")
```

Se `TKT_NUM` estiver vazio, pular para Phase 1.

#### 0.6.2 - Buscar Ticket no Zendesk

```bash
curl -sS -u "$ZENDESK_EMAIL/token:$ZENDESK_TOKEN" \
  "$ZENDESK_URL/api/v2/tickets/$TKT_NUM.json" \
  --connect-timeout 10
```

Se a resposta conter erro (ticket nao encontrado, auth falhou), logar aviso e prosseguir sem dados Zendesk.

#### 0.6.3 - Extrair Dados do Ticket

Do JSON retornado, extrair:

| Campo              | JSON Path                  | Uso                                         |
|--------------------|----------------------------|---------------------------------------------|
| Subject            | `$.ticket.subject`         | Descricao curta do problema                 |
| Description        | `$.ticket.description`     | Relato completo do cliente                  |
| Status             | `$.ticket.status`          | Estado do ticket (open/pending/hold/solved)  |
| Priority           | `$.ticket.priority`        | Prioridade (urgent/high/normal/low)         |
| Tags               | `$.ticket.tags`            | Tags de classificacao (modulo, vertical)    |
| Created At         | `$.ticket.created_at`      | Data de abertura                            |
| Updated At         | `$.ticket.updated_at`      | Ultima atualizacao                          |

#### 0.6.4 - Apresentar Contexto Zendesk

Apresentar logo apos o bloco do work item (Phase 0.4):

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

#### 0.6.5 - Guardar Contexto para Fases Posteriores

Armazenar os dados do Zendesk nas variaveis do pipeline para uso nas fases seguintes:

- `ZD_TICKET_ID` = numero do ticket
- `ZD_SUBJECT` = subject do ticket
- `ZD_DESCRIPTION` = descricao completa do cliente
- `ZD_STATUS` = status do ticket
- `ZD_PRIORITY` = prioridade
- `ZD_TAGS` = tags do ticket

Estas variaveis serao passadas como contexto adicional para os subagentes:
- **taxone-architect** (Phase 2): usa `ZD_DESCRIPTION` para entender o cenario do cliente
- **taxone-developer** (Phase 4): usa `ZD_DESCRIPTION` para reproduzir o problema
- **taxone-reviewer** (Phase 6): valida se a correcao atende o relato do cliente

#### 0.6.6 - Buscar Tickets Similares Resolvidos

**Condicao:** `ZD_TICKET_ID` preenchido (Phase 0.6.1 extraiu TKT com sucesso).

**Objetivo:** Encontrar tickets resolvidos similares e verificar se o problema e um "not a bug" conhecido.

**Passos:**

1. **Extrair contexto do ticket atual:**
```bash
# Extrair tags de vertical e modulo do ticket
ZD_VERTICALS=$(echo "$ZD_TAGS" | python -c "
import sys
tags = sys.stdin.read().split()
verts = [t.replace('vertical_dw_','') for t in tags if t.startswith('vertical_dw_')]
print(' '.join(verts))
")

ZD_MODULOS=$(echo "$ZD_TAGS" | python -c "
import sys
tags = sys.stdin.read().split()
mods = [t.replace('modulo_dw_taxone_','') for t in tags if t.startswith('modulo_dw_taxone_')]
print(' '.join(mods))
")
```

2. **Extrair keywords do subject (remover stopwords PT-BR):**
```bash
ZD_KEYWORDS=$(echo "$ZD_SUBJECT" | python -c "
import sys, re
STOPWORDS = {'a','o','e','de','do','da','dos','das','em','no','na','nos','nas','um','uma',
  'para','por','com','sem','que','se','ao','ou','nao','mais','como','esta','ter','ser',
  'foi','sao','tem','sua','seu','ele','ela','quando','muito','ja','tambem','so','pelo',
  'pela','ate','entre','sobre','mesmo','apos','ainda','bem','pode','deve','favor',
  'prezado','segue','conforme','referente','solicito','informo','obrigado'}
text = re.sub(r'[^\w\s]', ' ', sys.stdin.read().lower())
words = [w for w in text.split() if w not in STOPWORDS and len(w) > 2]
seen = set()
unique = [w for w in words if not (w in seen or seen.add(w))]
print(' '.join(unique[:5]))
")
```

3. **Buscar tickets similares resolvidos via API:**
```bash
# Montar query de busca
SEARCH_QUERY="type:ticket status:solved"
if [ -n "$ZD_VERTICALS" ]; then
  FIRST_VERT=$(echo "$ZD_VERTICALS" | awk '{print $1}')
  SEARCH_QUERY="$SEARCH_QUERY tags:vertical_dw_$FIRST_VERT"
fi
if [ -n "$ZD_MODULOS" ]; then
  FIRST_MOD=$(echo "$ZD_MODULOS" | awk '{print $1}')
  SEARCH_QUERY="$SEARCH_QUERY tags:modulo_dw_taxone_$FIRST_MOD"
fi
SEARCH_QUERY="$SEARCH_QUERY $ZD_KEYWORDS"

# Buscar (max 5 resultados)
SIMILAR_RESPONSE=$(curl -sS -u "$ZENDESK_EMAIL/token:$ZENDESK_TOKEN" \
  "$ZENDESK_URL/api/v2/search.json?query=$(python -c "import urllib.parse; print(urllib.parse.quote('$SEARCH_QUERY'))")&per_page=5" \
  --connect-timeout 10)
```

4. **Para os top 5 resultados, buscar ultimo comentario de agente:**
```bash
# Para cada resultado, buscar ultimo comentario publico de agente
# e verificar se tem tag causa_raiz_duvida_funcional|parametrizacao|falha_de_dados
```
Usar python para extrair:
- `ticket.id`, `ticket.subject`, `ticket.tags` (filtrar causa_raiz_*)
- Para cada ticket, buscar `GET /api/v2/tickets/{id}/comments.json?sort_order=desc`
- Pegar o primeiro comentario nao-end-user com >100 chars

5. **Verificar match em knowledge base local:**
```bash
# Se knowledge/zendesk-patterns/{vertical}/ existir, buscar patterns correspondentes
PATTERN_DIR="${CLAUDE_PLUGIN_ROOT}/knowledge/zendesk-patterns"
if [ -d "$PATTERN_DIR/$FIRST_VERT" ]; then
  # Grep por keywords nos pattern files
  ZD_PATTERN_MATCH=$(grep -rl "$ZD_KEYWORDS" "$PATTERN_DIR/$FIRST_VERT/" 2>/dev/null | head -1)
fi
```

6. **Apresentar resultados:**
```
----------------------------------------------------------
  TICKETS SIMILARES RESOLVIDOS (Zendesk)
----------------------------------------------------------
  1. TKT{id} - {subject}
     Causa: {causa_raiz_*}
     Resolucao: {primeiros 200 chars do comentario de agente}

  2. TKT{id} - {subject}
     Causa: {causa_raiz_*}
     Resolucao: {primeiros 200 chars}
  ...

  *** ATENCAO: {N} tickets similares classificados como
  "Not a Bug" (duvida funcional / parametrizacao).
  Verificar antes de prosseguir com implementacao. ***
----------------------------------------------------------
```

Se nao encontrar tickets similares, nao exibir o bloco.

**Alerta "Not a Bug":** Se algum dos tickets similares tiver tag `causa_raiz_duvida_funcional`,
`causa_raiz_parametrizacao` ou `causa_raiz_falha_de_dados`, ativar o flag `ZD_NOT_A_BUG_FLAG=true`.

7. **Guardar variaveis para fases posteriores:**

- `ZD_SIMILAR_TICKETS` — JSON com lista de tickets similares (id, subject, causa_raiz, resolucao)
- `ZD_NOT_A_BUG_FLAG` — `true` se algum ticket similar e "not a bug", `false` caso contrario
- `ZD_PATTERN_MATCH` — path do pattern file local, se encontrado (vazio caso contrario)

Estas variaveis serao passadas ao **taxone-architect** (Phase 2.2) para enriquecer a analise.

**Custo API:** 1 search + ate 5 comment fetches = 6 calls (negligivel vs 400/min limit).

#### 0.6.7 - Triagem FAQ (SAFX Catalog + Not-a-Bug)

**Executar SEMPRE** (nao depende de TKT Zendesk). Custo: zero API calls (tudo local).

**Objetivo:** Verificar se o erro/problema descrito na WI ja tem solucao documentada no FAQ,
o que indica forte sinal de duvida funcional (not-a-bug).

**Passos:**

1. **Executar faq_triage.py:**
```bash
FAQ_TRIAGE_RESULT=$(python "${CLAUDE_PLUGIN_ROOT}/scripts/faq_triage.py" \
  --title "$WI_TITLE" \
  --description "$WI_DESCRIPTION" \
  --format json)
```

2. **Extrair variaveis do resultado:**
```bash
FAQ_TRIAGE_SCORE=$(echo "$FAQ_TRIAGE_RESULT" | python -c "import sys,json; print(json.load(sys.stdin)['score'])")
FAQ_TRIAGE_CLASSIFICATION=$(echo "$FAQ_TRIAGE_RESULT" | python -c "import sys,json; print(json.load(sys.stdin)['classification'])")
FAQ_TRIAGE_ARTICLES=$(echo "$FAQ_TRIAGE_RESULT" | python -c "import sys,json; print(json.dumps(json.load(sys.stdin).get('articles',[])))")
FAQ_SAFX_MATCH=$(echo "$FAQ_TRIAGE_RESULT" | python -c "import sys,json; print(json.dumps(json.load(sys.stdin).get('safx_match')))")
```

3. **Apresentar resultado (se classificacao >= POSSIVEL-FAQ):**
```
----------------------------------------------------------
  TRIAGEM FAQ — {FAQ_TRIAGE_CLASSIFICATION}
  Score: {FAQ_TRIAGE_SCORE}
----------------------------------------------------------
  SAFX Match: {safx_code} Erro {error_code}
  Solucao documentada: {solution}
  Artigo: {article_path}

  *** ATENCAO: Erro documentado no FAQ.
  Verificar se cliente seguiu os passos antes de alterar codigo. ***
----------------------------------------------------------
```

Se score < 5, nao exibir bloco.

4. **Guardar variaveis para fases posteriores:**

- `FAQ_TRIAGE_SCORE` — score numerico da triagem
- `FAQ_TRIAGE_CLASSIFICATION` — `[FAQ-RESOLUTION]`, `[POSSIVEL-FAQ]`, `[VERIFICAR-FAQ]` ou vazio
- `FAQ_TRIAGE_ARTICLES` — JSON com artigos relevantes encontrados
- `FAQ_SAFX_MATCH` — JSON com match SAFX especifico (safx_code, error_code, solution, article_path) ou null

Estas variaveis serao passadas ao **taxone-architect** (Phase 2) para enriquecer a analise.

**Custo:** Zero API calls. Usa SAFX_CATALOG.json e MODULE_INDEX.json locais.

---

## Phase 0.7 - Enriquecer com Datadog

> **PARALELO:** Esta fase roda em paralelo com Phase 0.6 (Zendesk). Ambas sao lancadas
> simultaneamente via Agent tool calls no mesmo bloco, logo apos Phase 0.

### Objetivo
Buscar dados reais de APM/logs/traces no Datadog via MCP Server para enriquecer o contexto de WIs relacionadas a importacao, performance ou erros em batch. Segue padrao fault-tolerant da Phase 0.6 — se MCP indisponivel ou keywords nao detectadas, pular silenciosamente.

### Pre-requisito
MCP Server `datadog` configurado em `~/.claude.json` (auth via OAuth, sem API Key manual).
Org: `trta-onesource` | Permissao: MCP Read (somente leitura).

### Condicao de Entrada

1. Titulo ou descricao do work item contem keywords de performance/importacao
2. MCP Server `datadog` disponivel e autenticado

**Se QUALQUER condicao NAO atendida:** pular silenciosamente para Phase 1.

### Passos

#### 0.7.1 - Detectar se WI e de importacao/performance

Verificar se titulo ou descricao contem keywords (case-insensitive):

**Keywords:** `importa`, `lentidao`, `lento`, `timeout`, `performance`, `demora`, `batch`, `job servidor`, `erro importacao`, `travou`, `demorado`, `processamento`, `carga`

Extrair tambem **termos de busca** do titulo/descricao: nome de procedure, codigo SAFX (ex: X3007), nome do job, tabela mencionada.

**Se nenhuma keyword encontrada:** pular para Phase 1 silenciosamente.

#### 0.7.2 - Buscar Logs Recentes

Usar MCP tool `search_datadog_logs` (ou equivalente disponivel):

```
Query:  service:taxone* status:(error OR warn) {termos_extraidos}
Periodo: ultimos 7 dias
Limite: 10 resultados
Ordenar: mais recentes primeiro
```

Extrair de cada log: timestamp, service, status, message (primeiros 200 chars).

**Se MCP retornar erro ou vazio:** registrar warning e continuar.

#### 0.7.3 - Buscar APM Traces/Spans

Usar MCP tool `search_datadog_spans` (ou equivalente disponivel):

```
Query:  service:taxone* @duration:>5s {termos_extraidos}
Periodo: ultimos 7 dias
Limite: 5 resultados
Ordenar: maior duracao primeiro
```

Extrair de cada span: resource_name, duration_ms, service, status, error (se houver).

**Se MCP retornar erro ou vazio:** registrar warning e continuar.

#### 0.7.4 - Buscar Metricas de Performance

Usar MCP tool `search_datadog_metrics` (ou equivalente disponivel):

```
Metricas a buscar:
- avg:trace.servlet.request.duration{service:taxone*}
- p95:trace.servlet.request.duration{service:taxone*}
- sum:trace.servlet.request.errors{service:taxone*}
Periodo: ultimos 7 dias
```

**Se MCP retornar erro ou vazio:** registrar warning e continuar.

#### 0.7.5 - Buscar Monitors Relevantes

Usar MCP tool `search_datadog_monitors` (ou equivalente disponivel):

```
Query: taxone OR mastersaf
```

Verificar se ha monitors em estado Alert ou Warn que possam estar relacionados ao problema.

**Se MCP retornar erro ou vazio:** pular este passo.

#### 0.7.5.5 - Buscar RUM / User Journey

**Condicao:** Executar SEMPRE que a WI envolva interacao com tela (importacao, consulta, erro de tela, etc.).
Keywords adicionais de tela: `tela`, `erro na tela`, `nao abre`, `nao carrega`, `branco`, `travou tela`,
`500`, `404`, `click`, `botao`, `salvar`, `gravar`, `consultar`, `campo`, `combo`, `grid`, `nao exibe`,
`desapareceu`, `sumiu`, `frontal`, `interface`, `UI`, `angular`

**IMPORTANTE — Arquitetura RUM do TAX ONE:**
No TAX ONE, os dados de RUM vem **embedados nos APM traces** (`ingestion_reason:rum`), NAO como
eventos RUM separados. Portanto, a fonte primaria e `search_datadog_spans`, nao `search_datadog_rum_events`.

**Fonte primaria — APM Traces com RUM:**

Usar MCP tool `search_datadog_spans`:

```
Query: service:taxone* {termos_extraidos}
Periodo: ultimos 7 dias
Limite: 5 resultados
custom_attributes: ["usr.*", "view.*", "session.*", "application.*", "geo.*"]
```

Os spans RUM do TAX ONE contem dados riquissimos:
- `usr.menuPath` — caminho exato no menu (ex: "Importação > Importação > Execução")
- `usr.module` — modulo funcional (ex: "Job Servidor")
- `usr.email`, `usr.firmId`, `usr.dbSchema` — identificacao do tenant/usuario
- `view.name` — nome da view (ex: "/taxone/Job Servidor/Importação > Execução")
- `view.url` — URL completa da tela
- `view.referrer` — tela anterior (de onde veio)
- `session.has_replay` — se Session Replay esta disponivel (true/false)
- `http.url` — endpoint backend chamado
- `duration` — tempo total da operacao (ns)

**Fonte secundaria (fallback) — RUM Events:**

Se spans nao retornarem dados RUM, tentar `search_datadog_rum_events`:

```
Query: @type:error @application.name:*taxone* {termos_extraidos}
Periodo: ultimos 7 dias
detailed_output: true
```

**Output — User Journey para Playwright:**

Gerar `DD_RUM_USER_JOURNEY` a partir dos spans RUM:

```
DD_RUM_USER_JOURNEY:
  Module: Job Servidor
  Menu Path: Importação > Importação > Execução
  1. Acessou: /oms/home/oms/genericas/safgnfw1/w_abertura_modulo (referrer)
  2. Navegou: Job Servidor > Importação > Execução
  3. POST: /oms-taxone/ws/safilcm2/w_lib_proc_safil_imp_online (28.5s)
  4. Response: 200 OK (1292 bytes)
  Session Replay: DISPONIVEL (has_replay=true)
  User: {usr.name} ({usr.email}) | Firm: {usr.firmId} | Schema: {usr.dbSchema}
```

Este journey alimenta o `taxone-e2e-tester` para gerar specs Playwright que
reproduzam o caminho exato do cliente.

**Se MCP retornar erro ou vazio:** registrar warning e continuar.

#### 0.7.6 - Apresentar Contexto Datadog

Exibir bloco formatado ao usuario com os dados coletados:

```
----------------------------------------------------------
  DATADOG (MCP) - Contexto de Performance
----------------------------------------------------------
  Org:        trta-onesource
  Periodo:    Ultimos 7 dias
  Service:    {service detectado}

  LOGS DE ERRO ({count}):
  {timestamp} - {message} (primeiros 200 chars cada, max 5)

  TRACES LENTAS ({count}):
  {resource} - {duration}ms - {status}

  METRICAS:
  Latencia media: {avg}ms
  P95:            {p95}ms
  Taxa de erro:   {error_rate}%

  MONITORS EM ALERTA ({count}):
  {monitor_name} - {status} - {message}
----------------------------------------------------------
```

Se nenhum dado relevante encontrado, exibir:

```
----------------------------------------------------------
  DATADOG (MCP) - Nenhum dado de performance encontrado
  (Servico taxone* sem logs/traces nos ultimos 7 dias)
----------------------------------------------------------
```

#### 0.7.7 - Guardar Contexto para Fases Posteriores

Variaveis do pipeline:

- `DD_RELEVANT` — `true`/`false` (detectado na 0.7.1)
- `DD_SERVICE` — nome do servico identificado nos logs/traces
- `DD_ERROR_LOGS` — resumo dos logs de erro relevantes (max 10)
- `DD_SLOW_TRACES` — resumo das traces lentas (max 5)
- `DD_AVG_LATENCY` — latencia media em ms
- `DD_P95_LATENCY` — P95 em ms
- `DD_ERROR_RATE` — taxa de erro percentual
- `DD_MONITORS_ALERT` — monitors em alerta (se houver)
- `DD_RUM_ERRORS` — erros de tela capturados via RUM (max 10)
- `DD_RUM_USER_JOURNEY` — sequencia de navegacao do usuario (URLs + acoes + erros)
- `DD_RUM_SESSION_ID` — session ID para drill-down no Datadog UI
- `DD_RUM_ANOMALIES` — endpoints com performance fora do baseline (`knowledge/datadog/performance-baselines.json`)
- `DD_RUM_KNOWN_MATCHES` — erros que casam com catalogo conhecido (`knowledge/datadog/known-rum-errors.json`)
- `DD_SIMILAR_FIXES` — fixes anteriores encontrados por busca estrutural (tabelas, procedures, DDLs)

**Knowledge Base RUM** (consultar para enriquecer analise):
- `knowledge/datadog/module-service-map.json` — mapa modulo TAX ONE → service/resource/URLs Datadog
- `knowledge/datadog/known-rum-errors.json` — catalogo de erros RUM conhecidos com causa raiz e acao
- `knowledge/datadog/performance-baselines.json` — baselines P50/P95/P99 por endpoint

**Script auxiliar:** `scripts/rum_enricher.py` — classificacao de relevancia, match de erros, deteccao de anomalias.

Uso nas fases posteriores:
- **taxone-architect** (Phase 2): usa `DD_ERROR_LOGS` e `DD_SLOW_TRACES` para correlacionar com o codigo
- **taxone-dba** (Phase 2.5): usa `DD_SLOW_TRACES` para identificar queries lentas reais
- **taxone-developer** (Phase 4): usa contexto DD para focar otimizacao nos pontos criticos
- **taxone-e2e-tester**: usa `DD_RUM_USER_JOURNEY` para gerar specs Playwright que reproduzam o caminho do cliente
- **taxone-rum-analyst (deep-dive):** invocar para analise RUM profunda se erros complexos ou anomalias detectadas

### Busca Estrutural de Fixes Anteriores

Apos coletar dados da WI, buscar fixes anteriores por **objetos estruturais** (tabelas, procedures, DDLs) — nao apenas por keywords do titulo.

**Executar:** `python scripts/knowledge_search.py --wi-context {WI_ID}` (extrai termos do n3_brief.json automaticamente)

Ou busca manual:
```bash
python scripts/knowledge_search.py --table SAFX311
python scripts/knowledge_search.py --procedure OL_IMP_X311
python scripts/knowledge_search.py --keywords "importacao,dedup"
```

**Fontes pesquisadas:**
1. `knowledge/solutions/*.md` — YAML frontmatter (tables, packages, modules)
2. `knowledge/solutions/INDEX.md` — Patterns recorrentes
3. `knowledge/ado-fixes/_metadata.json` — WIs por titulo, tags, modulo
4. `tests/*/n3_brief.json` — component_mapping de analises anteriores
5. `tests/*/analysis_result.md` — grep por tabela/procedure/coluna

Salvar resultado em `DD_SIMILAR_FIXES`. Se encontrar matches HIGH/MEDIUM, apresentar ao PM na Phase 0.8.

---

## Phase 0.8 - Triagem PM (Gate de Qualidade)

### Objetivo
Classificar o work item antes de investir tempo em analise tecnica e implementacao.
O PM atua como gate de qualidade, filtrando not-a-bugs, feature requests, duplicatas
e analises incompletas. Aproveita dados ja coletados nas Phases 0.6 (Zendesk) e 0.7 (Datadog).

### Quando Executar
**SEMPRE** - esta fase e obrigatoria para todos os work items.

### Passos

**Passo 1 - Preparar dados para o PM:**

Compilar todas as informacoes coletadas ate aqui:
- Dados do work item (titulo, descricao, ReproSteps, severity, area path)
- Dados Zendesk (se coletados na Phase 0.6): tickets similares, patterns, flag not-a-bug
- Dados Datadog (se coletados na Phase 0.7): logs de erro, traces

**Passo 2 - Lancar taxone-pm para triagem:**

Invocar via Agent com `subagent_type="taxone-pm"`:

```
## Triagem de Work Item - #{WI_ID}

### Dados do Work Item
- **Titulo:** {WI_TITLE}
- **Descricao:** {WI_DESCRIPTION}
- **ReproSteps:** {WI_REPRO_STEPS}
- **Severity:** {WI_SEVERITY}
- **Area Path:** {WI_AREA_PATH}
- **Tags:** {WI_TAGS}
- **Acceptance Criteria:** {WI_ACCEPTANCE_CRITERIA}

### Contexto Zendesk (se disponivel)
- Tickets similares: {ZD_SIMILAR_TICKETS}
- Pattern match: {ZD_PATTERN_MATCH}
- Not-a-bug flag: {ZD_NOT_A_BUG_FLAG}

### Contexto Datadog (se disponivel)
- Erros relevantes: {DD_ERROR_LOGS}

### Sua Tarefa

Executar triagem completa deste work item seguindo o processo padrao:
1. Analisar dados do WI
2. Executar FAQ Triage (faq_triage.py)
3. Verificar Zendesk Patterns
4. Verificar Business Rules
5. Buscar Duplicatas
6. Detectar Feature Request
7. Avaliar Qualidade N1/N2
8. Emitir veredicto com output estruturado obrigatorio
```

**Passo 3 - Apresentar veredicto ao usuario:**

```markdown
## Phase 0.8 - Triagem PM

### Veredicto: {VEREDICTO}
### Confianca: {X}%

{Resumo da justificativa com sinais coletados}
```

**Passo 4 - Decisao de fluxo baseada no veredicto:**

- **CONFIRMED_BUG (confianca >= 70%):**
  Prosseguir para Phase 1 (Knowledge + Alinhamento) normalmente.

- **NOT_A_BUG (confianca >= 75%):**
  Pular para Phase 8 - Flow B (As Designed / Not-a-Bug).
  Adicionar tag `SUST-IA-CLAUDE-NOT-BUG` ao atualizar ADO.
  ```
  Triagem: Classificado como Not-a-Bug ({confianca}%).

  Sugestao de resposta ao cliente:
  {texto sugerido pelo PM}

  Deseja:
  1. Aceitar e atualizar ADO como Not-a-Bug (tag SUST-IA-CLAUDE-NOT-BUG)
  2. Discordar e prosseguir com implementacao
  3. Solicitar mais informacoes
  ```

- **FEATURE_REQUEST (confianca >= 80%):**
  Informar ao usuario e oferecer reclassificacao.
  Se envolver criacao/alteracao de regra de negocio (keywords: "nova regra", "alterar regra", "regra fiscal", "nova legislacao", "nova obrigacao", "configuracao tributaria"), adicionar tag `SUST-IA-CLAUDE-REGRA`.
  ```
  Triagem: Classificado como Feature Request ({confianca}%).
  {Justificativa do PM}

  Deseja:
  1. Reclassificar e encerrar pipeline
  2. Discordar e prosseguir como implementacao
  ```
  Se opcao 1: atualizar ADO e encerrar. Se opcao 2: continuar pipeline.

- **INCOMPLETE_ANALYSIS (confianca >= 80%):**
  Informar ao usuario e oferecer devolver ao N1/N2.
  Adicionar tag `SUST-IA-CLAUDE-ANALISE` automaticamente (WI precisa de analise adicional).
  ```
  Triagem: Analise incompleta ({confianca}%).
  Itens faltantes: {lista}

  Deseja:
  1. Devolver ao N1/N2 com feedback estruturado
  2. Prosseguir mesmo assim
  3. Fornecer informacoes adicionais agora
  ```

- **DUPLICATE (confianca >= 85%):**
  Informar ao usuario com WI original.
  ```
  Triagem: Possivel duplicata ({confianca}%).
  WI original: #{ORIGINAL_ID} - {titulo}

  Deseja:
  1. Fechar como duplicata
  2. Discordar e prosseguir
  ```

- **NEEDS_INFO:**
  Adicionar tag `SUST-IA-CLAUDE-ANALISE` automaticamente (WI precisa de informacoes adicionais).
  Solicitar informacoes especificas ao usuario e relancar PM apos obter respostas.

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

#### 0.9.2 - Lancar taxone-sm em modo alocacao avulsa

Invocar via Agent com `subagent_type="taxone-sm"`:

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
Executar alocacao avulsa conforme documentado no seu perfil de agente:
1. Carregar TEAM_ROSTER e TEAM_SPECIALIZATIONS
2. Resolver modulo/vertical/tech do WI
3. Calcular score de todos os devs e testers
4. Retornar top 3 devs e top 3 testers com scores e recomendacao final
```

#### 0.9.3 - Apresentar resultado e confirmar

```markdown
## Phase 0.9 - Alocacao SM

O WI #{WI_ID} nao tem dev/tester atribuido.
O Scrum Master recomenda:

- **Dev:** {nome} (score: {X}) - {motivo}
- **Tester:** {nome} (score: {X}) - {motivo}

Deseja aplicar esta alocacao no ADO?
1. Sim, atribuir dev e tester recomendados
2. Nao, prosseguir sem alocacao
3. Escolher manualmente
```

- Se **opcao 1:** PATCH no ADO para atribuir `System.AssignedTo` ao dev recomendado. Adicionar tag `SUST-IA-CLAUDE`.
- Se **opcao 2:** Prosseguir para Phase 1 sem alteracao.
- Se **opcao 3:** Perguntar nome do dev/tester ao usuario.

#### 0.9.4 - PATCH no ADO (se aprovado)

```bash
AUTH=$(printf '%s' ":$ADO_PAT" | base64 -w0)
curl -s -X PATCH \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json-patch+json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{WI_ID}?api-version=7.1" \
  -d '[
    {
      "op": "add",
      "path": "/fields/System.AssignedTo",
      "value": "{DEV_EMAIL}"
    },
    {
      "op": "add",
      "path": "/fields/System.Tags",
      "value": "{EXISTING_TAGS}; SUST-IA-CLAUDE"
    }
  ]'
```

---

## Phase 1 - Knowledge e Alinhamento

### Objetivo
Carregar a base de conhecimento relevante e alinhar com o usuario as opcoes do pipeline.

### Passos

#### 1.1 - Carregar Knowledge Base

**OBRIGATORIO antes de qualquer analise.**

1. Tentar ler `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/overview.md`
   - Se existir: extrair contexto geral da arquitetura
   - Se nao existir: prosseguir sem (pipeline nao depende disso para funcionar)

2. Analisar o titulo e descricao do work item para identificar features/modulos envolvidos

3. Tentar ler `${CLAUDE_PLUGIN_ROOT}/knowledge/features/{feature-identificada}.md`
   - Se existir: extrair contexto da feature (packages, tabelas, fluxos)
   - Se nao existir: informar ao usuario que nao ha knowledge da feature

4. Tentar ler `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/code-standards.md`
   - Se existir: extrair padroes de codigo

5. **Buscar artigos WebHelp relevantes** (Zendesk Help Center)
   - Extrair keywords do titulo e descricao do work item (modulo, tela, registro, operacao)
   - Buscar localmente em `${CLAUDE_PLUGIN_ROOT}/knowledge/webhelp/` via grep nos arquivos .md
   - Se nao encontrar localmente, buscar via API Zendesk:
     `curl -u "$ZENDESK_EMAIL/token:$ZENDESK_TOKEN" "$ZENDESK_URL/api/v2/help_center/articles/search.json?query={keywords}"`
   - Selecionar top 3-5 artigos mais relevantes
   - Extrair informacoes funcionais: passos, regras de negocio, parametros, telas envolvidas

Para cada arquivo lido, imprimir:
```
> [Knowledge] Carregando: {nome-do-arquivo} - {descricao-breve}
```

#### 1.2 - Resumo do Knowledge Carregado

Apresentar ao usuario:

```
----------------------------------------------------------
  KNOWLEDGE CARREGADO:
  [x] Arquitetura geral       (overview.md)
  [x] Feature: {nome}         ({feature}.md)
  [ ] Padroes de codigo        (nao encontrado)
  [x] WebHelp: {N} artigos    (webhelp search: "{keywords}")
----------------------------------------------------------
```

#### 1.3 - Confirmar Opcoes do Pipeline

Perguntar ao usuario usando AskUserQuestion:

```
Opcoes do pipeline para #{ID} - {titulo}:

1. Analise DBA Oracle (taxone-dba): Avaliar impacto em performance, indices, particionamento
   [S/N] (Recomendado se houver DDL ou queries complexas)

2. Scripts de Teste SQL (taxone-tester): Criar scripts de validacao e roteiro de teste manual
   [S/N] (Recomendado para mudancas em calculos fiscais)

3. Compound Engineering (Phase 9): Atualizar knowledge base com o aprendizado desta implementacao
   [S/N] (Recomendado para features novas ou mudancas significativas)

4. Testes de Regressao SuiteAutomation (Phase 5.5): Executar suites automatizadas de regressao
   [S/N] (Recomendado se houver Oracle LOCAL disponivel e mudancas em packages de processamento)

5. Testes E2E Playwright (Phase 5.7): Executar testes end-to-end no browser via Playwright
   [S/N] (Recomendado se houver alteracao em telas/UI ou se Node.js estiver disponivel)

Confirme as opcoes (ex: "1-S 2-N 3-S 4-S 5-S" ou "todos-S"):
```

Guardar as opcoes selecionadas para controlar fases condicionais:
- `OPT_DBA` = true/false (Phase 2.5)
- `OPT_TESTS` = true/false (Phase 5)
- `OPT_COMPOUND` = true/false (Phase 9)
- `OPT_REGRESSION` = true/false (Phase 5.5)
- `OPT_E2E` = true/false (Phase 5.7)

#### 1.4 - Resolver Dados do Usuario Git

```bash
GIT_USER=$(git config user.name)
GIT_EMAIL=$(git config user.email)
```

Se nao configurado, perguntar ao usuario.

Gerar nome da branch:
```
BRANCH_NAME="MFS{work-item-id}"
```

Exemplo: `jsilva/feature/54321`

---

## Phase 2 - Analise Arquitetural

> **PARALELO:** Se `OPT_DBA == true`, lancar Phase 2 (Architect) e Phase 2.5 (DBA) em PARALELO
> via Agent tool calls simultaneos. Ambas recebem o contexto da WI e knowledge (Phase 1).
> Apos ambas completarem, consolidar os resultados antes de Phase 3.
>
> Se `OPT_DBA == false`, executar apenas Phase 2 normalmente.

### Objetivo
Obter analise de impacto e design proposto do agente taxone-architect.

### Condicao
**SEMPRE executada.** Nenhuma implementacao ocorre sem analise previa.

### Passos

#### 2.1 - Preparar Prompt para o Architect

Montar o prompt com:
- Titulo e descricao completa do work item (limpar HTML)
- Criterios de aceitacao
- Knowledge carregado na Phase 1 (resumo)
- Contexto do Area Path e modulo

#### 2.2 - Lancar taxone-architect

```
Agent(subagent_type="taxone-architect")
```

Prompt para o agente:

```
Analise arquitetural para implementacao da User Story #{ID}:

TITULO: {titulo}

DESCRICAO:
{descricao}

CRITERIOS DE ACEITACAO:
{criterios}

KNOWLEDGE DISPONIVEL:
{resumo do knowledge carregado}

CONTEXTO ZENDESK (se disponivel):
- Ticket: TKT{ZD_TICKET_ID} — {ZD_SUBJECT}
- Descricao do cliente: {ZD_DESCRIPTION}
- Tags: {ZD_TAGS}
- Tickets similares resolvidos: {ZD_SIMILAR_TICKETS}
- Flag Not-a-Bug: {ZD_NOT_A_BUG_FLAG}
- Pattern local: {ZD_PATTERN_MATCH}

TRIAGEM FAQ (se disponivel):
- Classificacao: {FAQ_TRIAGE_CLASSIFICATION}
- Score: {FAQ_TRIAGE_SCORE}
- SAFX Match: {FAQ_SAFX_MATCH}
- Artigos: {FAQ_TRIAGE_ARTICLES}

Por favor:
1. Carregar o knowledge da(s) feature(s) envolvida(s)
1.4. Se triagem FAQ fornecida, verificar artigos FAQ e cruzar com flag Zendesk (Step 1.4 do architect)
1.5. Se contexto Zendesk fornecido, verificar padroes Zendesk conhecidos (Step 1.5 do architect)
2. Analisar impacto em packages PL/SQL, procedures, views, tabelas, telas PB, classes Java
3. Propor design da solucao seguindo patterns existentes
4. Listar riscos e pontos de atencao
5. Definir sequencia de implementacao

Entregar no formato padrao de Analise de Impacto + Design Proposto.
```

**Se `ZD_NOT_A_BUG_FLAG == true` OU `FAQ_TRIAGE_CLASSIFICATION in [FAQ-RESOLUTION, POSSIVEL-FAQ]`:**
O architect recebera o alerta e podera emitir `[POSSIVEL NOT-A-BUG]` ou `[FAQ-RESOLUTION]` no resultado.
O orquestrador deve interceptar este marcador e perguntar ao usuario via AskUserQuestion:
- Opcao 1: "Prosseguir com implementacao mesmo assim"
- Opcao 2: "Marcar como Not-a-Bug no ADO (sem implementacao)"
- Opcao 3: "Investigar mais antes de decidir"

Se o usuario escolher opcao 2, pular para Phase 8 (finalizacao) registrando decisao no ADO.
Se opcao 3, apresentar os tickets similares detalhados e aguardar instrucao.

#### 2.3 - Receber e Validar Resposta

O architect deve retornar:
- Lista de packages/objetos afetados (impacto direto e indireto)
- Design proposto por camada (PL/SQL, DDL, PB, Java)
- Patterns recomendados
- Riscos e mitigacoes
- Sequencia de implementacao

Apresentar o resultado ao usuario e perguntar:
```
Analise arquitetural concluida. Revise o design proposto acima.

Deseja prosseguir com a implementacao? (S/N)
Se desejar ajustes, descreva o que precisa ser alterado.
```

Se o usuario pedir ajustes, relancar o architect com o feedback adicional.

---

## Phase 2.5 - Analise DBA Oracle

> **PARALELO:** Esta fase roda em paralelo com Phase 2 (Architect) quando `OPT_DBA == true`.
> O DBA recebe o contexto da WI + knowledge diretamente (NAO depende do design do architect).
> Apos ambas completarem, o orquestrador consolida os resultados.

### Objetivo
Analisar impacto no banco de dados Oracle: performance, indices, particionamento, DDL.

### Condicao
**CONDICIONAL** - Executada se `OPT_DBA == true` (selecionado na Phase 1.3) OU auto-ativada por heuristicas (ver "Auto-Skip Inteligente").

**Nota:** Esta fase substitui a fase de observabilidade (DataDog/AppInsights) do LegalOne.
No TAX ONE, a preocupacao equivalente e impacto em performance Oracle.

### Auto-Skip Inteligente

Heuristicas para auto-ativar/desativar Phase 2.5 (independente da escolha do usuario):

| Sinal na WI (titulo + descricao) | Acao |
|-----------------------------------|------|
| Menciona: performance, lento, timeout, indice, index, particion, DDL, ALTER TABLE, CREATE INDEX | **Auto-ativar** (mesmo se usuario nao pediu) |
| Menciona: tabela, constraint, foreign key, grant, sequence | **Auto-ativar** |
| Apenas menciona: tela PB, powerbuilder, datawindow, botao, layout, Java, Jasper | **Auto-skip** (mesmo se usuario pediu) |
| Contexto Datadog (`DD_SLOW_TRACES` com dados) | **Auto-ativar** |

**Nota:** O usuario pode forcar via Phase 1.3. A heuristica e um fallback inteligente.

### Passos

#### 2.5.1 - Preparar Prompt para o DBA (modo paralelo)

Montar o prompt com contexto direto da WI (NAO depende do architect):
- Titulo e descricao completa do work item
- Knowledge carregado na Phase 1 (tabelas, packages, modulo)
- Contexto Datadog (se disponivel: `DD_SLOW_TRACES`, `DD_ERROR_LOGS`)
- Contexto Zendesk (se disponivel: descricao do problema)

#### 2.5.2 - Lancar taxone-dba

```
Agent(subagent_type="taxone-dba")
```

Prompt para o agente:

```
Analise DBA para implementacao da User Story #{ID}:

TITULO: {titulo}

DESCRICAO:
{descricao}

CRITERIOS DE ACEITACAO:
{criterios}

KNOWLEDGE DISPONIVEL:
{resumo do knowledge carregado - tabelas, packages, modulo}

CONTEXTO DATADOG (se disponivel):
- Traces lentas: {DD_SLOW_TRACES}
- Logs de erro: {DD_ERROR_LOGS}
- Latencia P95: {DD_P95_LATENCY}

CONTEXTO ZENDESK (se disponivel):
- Descricao do cliente: {ZD_DESCRIPTION}

Por favor:
1. Identificar tabelas e views provavelmente impactadas pela US
2. Analisar indices existentes e recomendar novos se necessario
3. Avaliar necessidade de particionamento
4. Identificar queries potencialmente problematicas
5. Gerar scripts de validacao de performance (explain plan antes/depois)
6. Avaliar impacto de locks durante deploy
7. Se Datadog forneceu traces lentas, correlacionar com as tabelas

Entregar no formato padrao de Analise DBA.

NOTA: Esta analise roda em PARALELO com o architect. Voce NAO tem o design
do architect ainda. Foque na analise de impacto Oracle baseado no contexto da WI.
```

#### 2.5.3 - Consolidar Design (Architect + DBA)

> **PASSO DE CONSOLIDACAO:** Executar SOMENTE apos Phase 2 e Phase 2.5 completarem.

1. Receber resultado do architect (Phase 2) e do DBA (Phase 2.5)
2. Verificar se ha conflitos ou sobreposicoes entre as recomendacoes
3. Consolidar em um design unificado:
   - Design proposto = architect
   - Recomendacoes de performance/indices = DBA
   - Se DBA identificou tabelas que o architect nao mencionou, adicionar ao escopo
4. Se o DBA recomendar mudancas que contradigam o architect, informar ao usuario:

```
Consolidacao Architect + DBA:

O DBA identificou pontos adicionais:
{recomendacoes do DBA}

Estes pontos complementam/divergem do design do architect:
{divergencias, se houver}

Deseja incorporar as recomendacoes do DBA ao design? (S/N)
```

5. O design consolidado e passado para Phase 3/4.

#### 2.5.4 - Registrar Causa Raiz (Automatica)

**Objetivo:** Salvar a causa raiz/analise em formato estruturado para alimentar o relatorio semanal de causas raiz.

**Condicao de execucao:** Sempre (apos qualquer veredicto DBA/Architect).

**Acao:** Salvar `tests/{WI_ID}/root_cause_entry.json` conforme schema `knowledge/root-cause/schema.json`.

Preencher com dados extraidos da analise DBA/Architect/PM:
- `root_cause.category`: `code_bug`, `performance`, `design_gap`, `config_error`, `recompilation_gap`, etc.
- `root_cause.originating_change`: Se DBA ou Git History identificou DDL, PR ou WI como causa, registrar. Senao, `{"type": "NONE"}`.
- `affected_modules`: Do PM scope analysis
- `affected_objects`: Do DBA
- `verdict`: Mapeado do veredicto PM/DBA

**Nota:** NAO-BLOQUEANTE. Se falhar a escrita, logar e continuar.

---

## Phase 3 - Workspace e Branch

### Objetivo
Preparar o workspace Git e criar a branch de trabalho.

### Passos

#### 3.1 - Verificar Estado do Repositorio

```bash
# Verificar se estamos em um repositorio Git
git rev-parse --is-inside-work-tree

# Verificar branch atual
git branch --show-current

# Verificar se ha mudancas pendentes
git status --porcelain
```

Se houver mudancas pendentes, alertar o usuario:
```
ATENCAO: Existem mudancas nao commitadas no workspace:
{lista de arquivos}

Deseja fazer stash antes de continuar? (S/N)
```

#### 3.2 - Atualizar Branch Principal

```bash
git checkout DEV
git pull origin DEV
```

#### 3.3 - Criar Branch de Trabalho

```bash
BRANCH_NAME="MFS{work-item-id}"
git checkout -b "$BRANCH_NAME"
```

Exemplo: `jsilva/feature/54321`

Confirmar ao usuario:
```
Branch criada: {branch_name}
Base: main (atualizada)
Workspace pronto para implementacao.
```

---

## Phase 4 - Implementacao

### Objetivo
Implementar as mudancas de codigo delegando ao taxone-developer.

### Passos

#### 4.1 - Preparar Prompt para o Developer

Montar o prompt completo com:
- Titulo, descricao e criterios de aceitacao do work item
- Design aprovado pelo architect (Phase 2)
- Recomendacoes do DBA (Phase 2.5, se executada)
- Knowledge carregado (Phase 1)
- Sequencia de implementacao definida pelo architect

#### 4.2 - Selecionar Agente de Implementacao

**Regra de selecao — Detectar linguagem pelo design do architect:**

| Sinal no Design | Agente |
|------------------|--------|
| Packages PL/SQL (.sql, PKG_, PRC_, FNC_, TRG_, VW_), procedures, functions, triggers, views | `taxone-plsql` |
| DataWindows (.srd, .srw, .srf, .sru), user objects, scripts PB | `taxone-pb` |
| Classes Java (.java, .jrxml), servlets, web services, Jasper | `taxone-java` |
| Componentes Angular (.ts, .html, .scss, @libs/) | `taxone-angular` |

- Se a US envolve **frontend Angular**: lancar `taxone-angular`
- Se a US envolve **backend PL/SQL**: lancar `taxone-plsql`
- Se a US envolve **backend PowerBuilder**: lancar `taxone-pb`
- Se a US envolve **backend Java**: lancar `taxone-java`
- Se MULTIPLAS linguagens detectadas:
  - PL/SQL + PB: lancar `taxone-plsql` PRIMEIRO (DDL/packages), depois `taxone-pb` (tela)
  - PL/SQL + Java: lancar em PARALELO (independentes)
  - Qualquer combo + Angular: Angular em PARALELO (repo separado)

Para implementacao **PL/SQL**:
```
Agent(subagent_type="taxone-plsql")
```

Para implementacao **PowerBuilder**:
```
Agent(subagent_type="taxone-pb")
```

Para implementacao **Java**:
```
Agent(subagent_type="taxone-java")
```

Para implementacao **frontend** (Angular 11):
```
Agent(subagent_type="taxone-angular")
```

Prompt para o agente (adaptar conforme backend ou frontend):

```
Implementar User Story #{ID}:

TITULO: {titulo}

DESCRICAO:
{descricao}

CRITERIOS DE ACEITACAO:
{criterios}

DESIGN APROVADO (do taxone-architect):
{design_proposto}

RECOMENDACOES DBA (se houver):
{recomendacoes_dba}

SEQUENCIA DE IMPLEMENTACAO:
{sequencia}

IMPORTANTE:
- Seguir RIGOROSAMENTE o design aprovado
- Seguir patterns existentes no projeto
- Nao refatorar codigo fora do escopo
- Documentar procedures/functions com comentarios em portugues
- Usar bind variables (NUNCA concatenar valores em SQL dinamico)
- Para PL/SQL: exception handling com WHEN OTHERS + logging

Ao finalizar, listar todos os arquivos criados e modificados.
```

#### 4.3 - Receber e Registrar Resultado

O developer deve retornar:
- Lista de arquivos criados (com caminhos completos)
- Lista de arquivos modificados (com caminhos e linhas alteradas)
- Scripts DDL gerados (se houver)
- Notas e observacoes

Guardar a lista de arquivos para as fases seguintes (review, commit).

#### 4.4 - Verificar Resultado

Verificar se o developer criou/modificou arquivos:

```bash
git status --porcelain
```

Se nenhum arquivo foi modificado, reportar erro e perguntar ao usuario como proceder.

---

### Execucao Paralela Pos-Implementacao: Phase 4.5 + 5 + 5.5 + 5.7 + 6

> **OTIMIZACAO CRITICA:** Apos Phase 4 completar, as fases 4.5, 5, 5.5, 5.7 e 6 sao INDEPENDENTES
> entre si (todas dependem apenas do resultado de Phase 4). Lancar todas em paralelo.
>
> **Implementacao:**
> ```
> # Lancar em paralelo (mesmo bloco de tool calls):
> Agent 1: Phase 4.5 - Analise de Impacto em Regras de Negocio (se condicao atendida)
> Agent 2: Phase 5   - Testes SQL de Validacao (se OPT_TESTS == true)
> Agent 3: Phase 5.5 - SuiteAutomation (se OPT_REGRESSION == true) → run_in_background=true
> Agent 4: Phase 6   - Code Review (OBRIGATORIO, sempre lancado)
> Agent 5: Phase 5.7 - Playwright E2E (se OPT_E2E == true) → run_in_background=true
> ```
>
> **Gates apos paralelo:**
> 1. Aguardar Phase 6 (review) — e o gate obrigatorio antes de Phase 7
> 2. Se Phase 4.5 retornar **NO-GO**, abortar antes de Phase 7 (mesmo se review ja aprovou)
> 3. Phase 5.5 roda em background — resultado coletado na Phase 8
> 4. Phase 5.7 roda em background — resultado coletado na Phase 8
> 5. Phase 5 (tester) nao bloqueia — resultado e informativo
>
> **Fluxo de decisao pos-paralelo:**
> ```
> Resultados paralelos chegam:
>   4.5 = GO?      → continuar
>   4.5 = NO-GO?   → apresentar ao usuario, oferecer opcoes (ajustar/aceitar/abortar)
>   6 = APROVADO?   → continuar para Phase 7
>   6 = REPROVADO?  → voltar para Phase 4 (ciclo de correcao)
>   5 = concluido   → registrar resultado
>   5.5 = background → coletar depois na Phase 8
>   5.7 = background → coletar depois na Phase 8
> ```

---

## Phase 4.5 - Analise de Impacto em Regras de Negocio

> **PARALELO:** Esta fase roda em paralelo com Phase 5, 5.5 e 6 apos Phase 4.

### Objetivo
Verificar se a implementacao nao quebra regras de negocio downstream antes de prosseguir com testes e review.

### Condicao
Executar SEMPRE que a implementacao envolver:
- Alteracao de JOINs (INNER → LEFT, adicao/remocao de condicoes)
- Introducao de valores default (NVL, COALESCE, DEFAULT)
- Alteracao de validacoes ou constraints
- Mudanca em campos de PK ou FK
- Alteracao de dados que alimentam outras procedures/views/telas

### Auto-Skip Inteligente

Heuristicas para pular Phase 4.5 automaticamente:

| Tipo de alteracao detectada (Phase 4 output) | Acao |
|----------------------------------------------|------|
| Apenas comentarios, formatacao, whitespace | **Auto-skip** |
| Apenas DDL puro (CREATE INDEX, ALTER TABLE ADD COLUMN) sem logica | **Auto-skip** |
| Apenas arquivos Java/Jasper (relatorios) | **Auto-skip** |
| Apenas tela PB (layout, botao, datawindow cosmético) | **Auto-skip** |
| Alteracao em SELECT/JOIN/WHERE/NVL/COALESCE/constraint | **Executar** |
| Alteracao em procedure/function que alimenta outras | **Executar** |

### Passo 1 - Lancar taxone-architect

Invocar via Agent com `subagent_type="taxone-architect"`:

```
## Analise de Impacto em Regras de Negocio - US #{WI_ID}

### Implementacao Realizada
{descricao da implementacao - arquivos, linhas, tipo de mudanca}

### Sua Tarefa
Executar analise de impacto em regras de negocio conforme processo padrao:
1. Rastrear fluxo downstream dos dados alterados
2. Verificar constraints e validacoes afetadas
3. Mapear valores default/NVL introduzidos
4. Verificar funcoes irmas com mesmo padrao
5. Entregar decisao GO/NO-GO
```

### Passo 2 - Avaliar resultado

- **GO:** Prosseguir para Phase 5 (Testes)
- **NO-GO:** Apresentar riscos ao usuario e oferecer opcoes:
  1. Ajustar implementacao (voltar Phase 4)
  2. Prosseguir com riscos aceitos
  3. Abortar pipeline

### Passo 3 - Funcoes irmas
Se funcoes irmas foram identificadas, perguntar ao usuario se deseja aplicar a mesma correcao e voltar para Phase 4 se necessario.

### Output

```markdown
## Phase 4.5 - Analise de Impacto em Regras de Negocio

- Decisao: {GO / NO-GO}
- Fluxo Downstream: {N pontos analisados}
- Constraints: {nenhuma quebra / lista}
- Valores Default: {seguros / lista de riscos}
- Funcoes Irmas: {N identificadas}
- Tags Aplicadas: {lista de tags adicionadas nesta fase, se houver}
```

**Tag automatica de Regras de Negocio:**

Se o architect identificar que a implementacao requer **nova regra de negocio** ou **alteracao de regra existente**
(keywords: "nova regra", "alterar regra", "regra fiscal", "nova legislacao", "nova obrigacao", "configuracao tributaria"),
adicionar automaticamente a tag `SUST-IA-CLAUDE-REGRA` ao work item no ADO.

---

## Phase 5 - Testes SQL de Validacao

> **PARALELO:** Esta fase roda em paralelo com Phase 4.5, 5.5 e 6 apos Phase 4.

### Objetivo
Criar scripts SQL de validacao e roteiros de teste manual.

### Condicao
**CONDICIONAL** - Executada APENAS se `OPT_TESTS == true` (selecionado na Phase 1.3).

**REGRA CRITICA: SEMPRE prosseguir com testes automaticamente apos implementacao e PR, sem perguntar ao usuario.** O fluxo completo de testes (compilacao, validacao SQL, SuiteAutomation, evidencias em tests/{WI_ID}/, upload de attachments na WI do ADO, Discussion comment com resultados, e criacao de Tasks QA) e parte integral e obrigatoria do pipeline. NUNCA parar para perguntar "quer que eu prossiga com testes?".

**Nota:** O TAX ONE NAO possui framework de teste automatizado (utPLSQL).
Testes sao scripts SQL de validacao + roteiros manuais.

### Passos

#### 5.1 - Lancar taxone-tester

```
Agent(subagent_type="taxone-tester")
```

Prompt para o agente:

```
Criar scripts de validacao para User Story #{ID}:

TITULO: {titulo}

DESCRICAO:
{descricao}

CRITERIOS DE ACEITACAO:
{criterios}

IMPLEMENTACAO REALIZADA:
{resumo do developer - arquivos criados/modificados}

DESIGN (do architect):
{design_proposto}

Por favor:
1. Analisar o codigo implementado
2. Criar scripts SQL de validacao cobrindo:
   - Caminho feliz (dados validos)
   - Cenarios negativos (dados invalidos)
   - Edge cases (nulos, zeros, limites)
   - Regressao (se aplicavel)
3. Criar script de dados de teste (INSERT/UPDATE)
4. Criar roteiro de teste manual (se envolve tela PB)
5. Criar script de rollback dos dados de teste

Salvar scripts em: tests/#{work-item-id}/
```

#### 5.2 - Registrar Resultado

O tester deve retornar:
- Scripts SQL de validacao criados
- Script de dados de teste
- Roteiro de teste manual (se aplicavel)
- Cobertura de cenarios

Adicionar os arquivos de teste na lista de arquivos para commit.

---

## Phase 5.5 - Testes de Regressao SuiteAutomation

> **BACKGROUND:** Esta fase roda em BACKGROUND (`run_in_background=true`) em paralelo com
> Phase 4.5, 5 e 6. NAO bloqueia o pipeline. Resultado coletado na Phase 8.

### Objetivo
Executar testes de regressao automatizados usando o framework SuiteAutomation para validar que a implementacao nao introduziu quebras em funcionalidades existentes.

### Condicao
**CONDICIONAL** - Executada APENAS se `OPT_REGRESSION == true` (selecionado na Phase 1.3).

### Auto-Skip Inteligente

Heuristicas para pular Phase 5.5 automaticamente:

| Sinal | Acao |
|-------|------|
| Nenhum mapeamento encontrado em `component-test-map.json` para os arquivos/packages alterados | **Auto-skip** |
| Score de mapeamento < `min_score_to_include` (3) para todas suites | **Auto-skip** |
| Pre-requisitos nao disponíveis (sem Java, sem Oracle local) | **Auto-skip** (com warning) |
| Alteracao envolve packages de processamento/calculo mapeados | **Executar** |

### REGRAS CRITICAS para SuiteAutomation

1. **SEMPRE sincronizar repo QA antes de criar cenarios:** Antes de criar XMLs ou flat files novos, atualizar `taxone_automacao_qa` (`git fetch origin` + verificar `origin/rc`) e buscar se ja existe cobertura para o componente. Se existir, usar/incrementar o existente. NUNCA duplicar cenarios.

2. **SEMPRE sincronizar XML e esperados do repo QA antes de rodar:** O XML local pode estar desatualizado. Copiar de `origin/rc` via `git show origin/rc:<path>` para o diretorio local. Paths no repo QA usam `arquivos/` (minusculo), no local `Arquivos/` (maiusculo).

3. **Se suite_runner reporta ERROR(0s) com 0 arquivos:** Rodar o JAR Java diretamente para ver output real:
```bash
cd suite-automation/jar && java -Dfile.encoding=Cp1252 -Dsun.jnu.encoding=ISO-8859-1 \
  -jar SuiteTeste.jar "<xml_path_sem_drive>" "RA<range>" 'PRO"<title>"' "../config/suiteteste_LOCAL.properties"
```

### Pre-Requisitos
- Java OpenJDK disponivel no PATH
- Oracle LOCAL acessivel (localhost:1521 / MFSPDB / V2R010AC)
- SuiteTeste.jar disponivel em `suite-automation/jar/SuiteTeste.jar`

### Passos

#### 5.5.1 - Verificar Pre-Requisitos

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/suite_runner.py" --check-only --wi-id 0 --title "check" --xml dummy
```

Se falhar, informar ao usuario quais pre-requisitos estao faltando e perguntar se deseja pular a Phase 5.5.

#### 5.5.1b - E2E Direcionado por WI (PREFERIDO)

Se a WI tem reproSteps/descricao com caminho funcional, usar targeted_e2e_runner como alternativa preferida ao mapeamento manual:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/targeted_e2e_runner.py" \
  --wi-id {WI_ID} --env LOCAL --suite-only --upload-evidence
```

- Se encontrar cenarios (exit 0 ou 1): usar este resultado, **pular 5.5.2-5.5.4**.
- Se GAP (exit 2): fallback para fluxo original (5.5.2 em diante).

#### 5.5.2 - Mapear Componente para Suites de Teste

Ler o mapeamento de componentes:

```bash
# Ler o component-test-map.json
cat "${CLAUDE_PLUGIN_ROOT}/knowledge/suite-automation/component-test-map.json"
```

Para cada mapping, calcular score baseado em 3 sinais:
- **Keywords (peso 3):** Match do titulo do WI contra `keywords` (case-insensitive, substring)
- **File paths (peso 5):** Match dos arquivos modificados na Phase 4 contra `file_paths` (substring)
- **Packages (peso 4):** Match dos packages PL/SQL referenciados contra `packages` (exact, case-insensitive)

Selecionar as top 5 suites com score >= `min_score_to_include` (3).

#### 5.5.3 - Apresentar Suites ao Usuario

```
==========================================================
  TESTES DE REGRESSAO - SuiteAutomation
==========================================================
  Suites identificadas para #{ID} - {titulo}:

  [1] {suite_id} (score: {N}) - {description}
      XML: {xml_file}
  [2] {suite_id} (score: {N}) - {description}
      XML: {xml_file}
  ...

  Range sugerido: 0;0 (todos os testes)
  Estimativa: ~{N} minutos por suite

  Confirmar execucao? (S/N ou numeros especificos ex: "1,3")
  Range customizado? (ex: "1;5" para testes 1 a 5, Enter para todos)
==========================================================
```

Usar AskUserQuestion para obter confirmacao e selecao.

#### 5.5.4 - Executar Suites via taxone-suite-runner (BACKGROUND)

```
Agent(subagent_type="taxone-suite-runner", run_in_background=true)
```

> **IMPORTANTE:** Lancar com `run_in_background=true`. O pipeline NAO espera este agente completar.
> O resultado sera coletado na Phase 8 via `TaskOutput(task_id=..., block=false)`.
> Se ainda nao completou na Phase 8, registrar como "Em execucao" no ADO.

Prompt para o agente:

```
Executar testes de regressao para User Story #{ID}:

TITULO: {titulo}

SUITES A EXECUTAR:
{lista de xml_files confirmados pelo usuario}

RANGE: {range selecionado ou "0;0"}

OUTPUT: tests/#{work-item-id}/regression_report.txt

Comando:
python "${CLAUDE_PLUGIN_ROOT}/scripts/suite_runner.py" \
  --wi-id {ID} \
  --title "{titulo}" \
  --xml "{xml_1}" --suite-id "{suite_id_1}" \
  --xml "{xml_2}" --suite-id "{suite_id_2}" \
  --range "{range}" \
  --output "tests/#{work-item-id}/regression_report.txt"

Por favor:
1. Executar o comando acima
2. Interpretar o relatorio gerado
3. Se houver falhas, analisar os diffs para determinar se sao pre-existentes
4. Retornar resumo com tabela PASS/FAIL por suite
```

#### 5.5.5 - Apresentar Resultados

```
==========================================================
  RESULTADO DOS TESTES DE REGRESSAO
==========================================================

  | Suite           | Status | Arquivos     | Duracao |
  |-----------------|--------|--------------|---------|
  | {suite_id}      | PASS   | {pass}/{tot} | {Xs}    |
  | {suite_id}      | FAIL   | {pass}/{tot} | {Xs}    |

  Total: {N} suites | {passed} PASS | {failed} FAIL
==========================================================
```

#### 5.5.6 - Tratar Falhas

Se houver falhas, perguntar ao usuario usando AskUserQuestion:

```
{N} suite(s) com falha(s) detectada(s):
- {suite_id}: {descricao da falha}

Opcoes:
1. Investigar falhas (o suite-runner vai analisar os diffs)
2. Prosseguir mesmo assim (falhas podem ser pre-existentes)
3. Abortar pipeline para corrigir antes
```

**Politica:** Warn only — o usuario decide. Falhas podem ser pre-existentes no ambiente LOCAL.

#### 5.5.7 - Salvar Relatorio

O relatorio gerado em `tests/#{work-item-id}/regression_report.txt` sera:
- Adicionado na lista de arquivos para commit (Phase 7)
- Anexado como evidencia no ADO (Phase 8)
- Referenciado no Discussion comment do work item

---

## Phase 5.7 - Testes E2E Playwright

> **BACKGROUND:** Esta fase roda em BACKGROUND (`run_in_background=true`) em paralelo com
> Phase 4.5, 5, 5.5 e 6. NAO bloqueia o pipeline. Resultado coletado na Phase 8.

### Objetivo
Validar que a mudanca nao quebrou fluxos de UI/browser usando testes E2E Playwright do repo `taxone_automacao_qa_playwright`.

**CONDICIONAL** - Executada APENAS se `OPT_E2E == true` (selecionado na Phase 1.3).

### Auto-Skip Inteligente

Heuristicas para pular Phase 5.7 automaticamente:

| Sinal | Acao |
|-------|------|
| Nenhum mapeamento encontrado no playwright-test-map.json | Auto-skip |
| Score < 3 para todos os mappings | Auto-skip |
| Node.js ou browsers nao instalados | Auto-skip (warning) |
| Repo Playwright nao clonado | Auto-skip (warning) |
| Alteracao exclusivamente DDL sem impacto em UI | Auto-skip |

Se auto-skip, registrar motivo: `E2E_SKIP_REASON = "{motivo}"`.

### Passos

#### 5.7.1 - Verificar Pre-Requisitos

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/playwright_runner.py" --check-only
```

Se falhar, informar ao usuario quais pre-requisitos estao faltando e perguntar se deseja pular a Phase 5.7.

#### 5.7.1a - RUM Journey → E2E (se DD_RUM_USER_JOURNEY disponivel)

Se `tests/{WI_ID}/rum_enrichment_{WI_ID}.json` existir, executar ANTES do scoring manual:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/rum_to_e2e.py" --wi-id {WI_ID} --dry-run
```

Isso gera automaticamente: specs mapeados por scoring + spec ephemeral do user journey real.
Resultado em `tests/{WI_ID}/rum_to_e2e_result.json`. ADICIONAR esses specs aos demais.

#### 5.7.1b - E2E Direcionado por WI (PREFERIDO)

Usar targeted_e2e_runner como alternativa preferida ao mapeamento manual por scoring:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/targeted_e2e_runner.py" \
  --wi-id {WI_ID} --env qa --playwright-only --upload-evidence --screenshots on
```

- Se encontrar cenarios (exit 0 ou 1): usar este resultado, **pular 5.7.2-5.7.5**.
- Se GAP (exit 2): fallback para fluxo original (5.7.2 em diante).

#### 5.7.2 - Carregar Mapeamento e Scoring Fino por Tela

```
Ler ${CLAUDE_PLUGIN_ROOT}/knowledge/suite-automation/playwright-test-map.json (v2.0.0 - mapeamento por TELA)
```

Aplicar scoring FINO com prioridade para `menu_path` (caminho de menu exato da tela):

| Criterio | Pontos | Exemplo |
|----------|--------|---------|
| `menu_path` match (exato ou parcial contra titulo/menu da WI) | **7** | WI "ICMS Apuracao" → `menu_path: "ESTADUAL > ICMS > APURACAO"` |
| `screen_keywords` match (keyword especifica da tela) | **5** | WI "SUB-APURACOES" → match em screen_keywords |
| `file_path` match (arquivos modificados) | **5** | Mantido do v1 |
| `package` match (PL/SQL packages) | **4** | Mantido do v1 |
| `keyword` match (dominio generico) | **3** | Mantido do v1 |

Algoritmo de scoring:
1. Para cada mapping, calcular score combinado de TODOS os criterios acima
2. O `menu_path` match e o mais valioso: comparar contra titulo da WI, campo Menu do ADO, e caminho de tela
3. Filtrar mappings com score >= min_score_to_include (3)
4. Limitar a max_specs (5) specs no total
5. Se um mapping tem score >= 7 (menu_path match), priorizar seus specs

#### 5.7.3 - Selecao Inteligente por Score

| Score | Acao | Resultado Esperado |
|-------|------|--------------------|
| **>= 7** (menu_path match) | Rodar SO os specs desse mapping | 1-2 specs, ~30s |
| **3-7** (keyword/package match) | Rodar os specs mapeados | 2-5 specs, ~2min |
| **< 3** para todos | Smoke fallback (se OPT_E2E == true) | 15 smoke specs |

Heuristicas adicionais:

| Cenario | Tipo de teste |
|---------|---------------|
| Alteracao somente PL/SQL backend (sem impacto em UI) | Smoke only (15 specs) |
| Alteracao em telas/formularios/Angular/Java | Full specs mapeados (por tela) |
| Alteracao em packages de processamento batch | Smoke only |
| Alteracao em WebService/API consumida pela UI | Full specs mapeados (por tela) |
| Nenhum mapping com score >= 3, mas OPT_E2E == true | Smoke only |

**Uso de --grep-describe**: Se o mapping de score alto tem muitos specs (ex: DW_MANUTENCAO com 16 specs),
usar `--grep-describe` com o titulo do test.describe para filtrar apenas os testes relevantes:

```bash
python playwright_runner.py --spec "e2e/estadual/icms/apuracao/apuracao.spec.ts" \
  --grep-describe "ESTADUAL --> ICMS --> APURACAO"
```

#### 5.7.4 - Confirmar com Usuario

Apresentar specs selecionados ao usuario e solicitar confirmacao:

```
Testes E2E Playwright selecionados para #{ID}:

Tipo: {Smoke / Full}
Ambiente: qa
Specs:
  1. {spec_file_1} (score: {N})
  2. {spec_file_2} (score: {N})

Confirma execucao? [S/N]
```

Se usuario negar, registrar como "Nao solicitado" e prosseguir.

#### 5.7.5 - Lancar Agente em Background

```
Agent(subagent_type="taxone-e2e-tester", run_in_background=true)
```

> **IMPORTANTE:** Lancar com `run_in_background=true`. O pipeline NAO espera este agente completar.
> O resultado sera coletado na Phase 8 via `TaskOutput(task_id=..., block=false)`.
> Se ainda nao completou na Phase 8, registrar como "Em execucao" no ADO.

Prompt para o agente:

```
Executar testes E2E Playwright para User Story #{ID}:

TITULO: {titulo}

TIPO: {smoke / full}
SPECS A EXECUTAR:
{lista de spec files confirmados pelo usuario}

AMBIENTE: qa
WORKERS: 3

OUTPUT: tests/#{work-item-id}/e2e_report.txt

Comando (targeted por tela - preferido quando score >= 7):
python "${CLAUDE_PLUGIN_ROOT}/scripts/playwright_runner.py" \
  --wi-id {ID} \
  --title "{titulo}" \
  --spec "{spec_1}" \
  --spec "{spec_2}" \
  --grep-describe "{test.describe title do mapping}" \
  --env qa \
  --workers 3 \
  --output "tests/#{work-item-id}/e2e_report.txt"

OU (full specs sem grep - quando score 3-7):
python "${CLAUDE_PLUGIN_ROOT}/scripts/playwright_runner.py" \
  --wi-id {ID} \
  --title "{titulo}" \
  --spec "{spec_1}" \
  --spec "{spec_2}" \
  --env qa \
  --workers 3 \
  --output "tests/#{work-item-id}/e2e_report.txt"

OU (smoke only):
python "${CLAUDE_PLUGIN_ROOT}/scripts/playwright_runner.py" \
  --wi-id {ID} \
  --title "{titulo}" \
  --smoke-only \
  --env qa \
  --output "tests/#{work-item-id}/e2e_report.txt"

Por favor:
1. Executar o comando acima
2. Interpretar o relatorio gerado
3. Se houver falhas, classificar como flaky/ambiente/regressao
4. Retornar resumo com tabela PASS/FAIL por spec
```

#### 5.7.6 - Apresentar Resultados

```
==========================================================
  RESULTADO DOS TESTES E2E PLAYWRIGHT
==========================================================

  | Spec              | Status | Duracao |
  |-------------------|--------|---------|
  | {spec_file}       | PASS   | {Xs}    |
  | {spec_file}       | FAIL   | {Xs}    |

  Total: {N} specs | {passed} PASS | {failed} FAIL | {flaky} FLAKY
==========================================================
```

#### 5.7.7 - Tratar Falhas

Se houver falhas, perguntar ao usuario usando AskUserQuestion:

```
{N} spec(s) E2E com falha(s) detectada(s):
- {spec_file}: {titulo_teste} - {erro}

Opcoes:
1. Investigar falhas (o e2e-tester vai analisar screenshots/traces)
2. Prosseguir mesmo assim (falhas podem ser flaky ou de ambiente)
3. Abortar pipeline para corrigir antes
```

**Politica:** Warn only — o usuario decide. Falhas E2E podem ser flaky ou de ambiente QA.

#### 5.7.8 - Salvar Relatorio

O relatorio gerado em `tests/#{work-item-id}/e2e_report.txt` sera:
- Adicionado na lista de arquivos para commit (Phase 7)
- Anexado como evidencia no ADO (Phase 8)
- Referenciado no Discussion comment do work item

---

## Phase 6 - Code Review

> **PARALELO:** Esta fase roda em paralelo com Phase 4.5, 5, 5.5 e 5.7 apos Phase 4.
> **GATE OBRIGATORIO:** O pipeline aguarda esta fase completar antes de Phase 7.

### Objetivo
Revisar todo o codigo implementado antes de criar o PR.

### Condicao
**OBRIGATORIO** - Esta fase SEMPRE e executada. O pipeline NAO prossegue sem review.

### Passos

#### 6.1 - Lancar Reviewer(s)

**Regra de selecao — Reviewer especializado por linguagem:**
- Se houve alteracoes **PL/SQL**: lancar `taxone-plsql-reviewer`
- Se houve alteracoes **PowerBuilder**: lancar `taxone-pb-reviewer`
- Se houve alteracoes **Java**: lancar `taxone-java-reviewer`
- Se houve alteracoes **frontend Angular**: lancar `taxone-angular` (modo review)
- Se houve alteracoes em **multiplas linguagens**: lancar os reviewers correspondentes **em paralelo**

**Para review PL/SQL:**
```
Agent(subagent_type="taxone-plsql-reviewer")
```

**Para review PowerBuilder:**
```
Agent(subagent_type="taxone-pb-reviewer")
```

**Para review Java:**
```
Agent(subagent_type="taxone-java-reviewer")
```

Prompt para o agente:

```
Code review para User Story #{ID}:

TITULO: {titulo}

ARQUIVOS CRIADOS:
{lista de arquivos criados pelo developer}

ARQUIVOS MODIFICADOS:
{lista de arquivos modificados pelo developer}

DESIGN ORIGINAL (do architect):
{design_proposto}

Por favor:
1. Carregar padroes de codigo (code-standards.md)
2. Revisar TODOS os arquivos criados e modificados
3. Verificar:
   - Seguranca PL/SQL (SQL injection, grants, dados sensiveis)
   - Qualidade PL/SQL (exception handling, cursores, transacoes)
   - Performance Oracle (bind variables, bulk operations, indices)
   - Convencoes do projeto (nomenclatura, formatacao, comentarios)
   - PowerBuilder (se aplicavel)
   - Java (se aplicavel)
4. Aderencia ao design aprovado pelo architect
5. Pontuar confianca de cada issue (0-100)
6. Reportar APENAS issues com confianca >= 75
7. Emitir veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO
```

**Para review frontend Angular (em paralelo se houver review backend):**

```
Agent(subagent_type="taxone-angular")
```

Prompt para o agente:

```
Code review Angular para User Story #{ID}:

TITULO: {titulo}

ARQUIVOS CRIADOS:
{lista de arquivos Angular criados}

ARQUIVOS MODIFICADOS:
{lista de arquivos Angular modificados}

Por favor, revisar em modo REVIEWER:
1. Carregar knowledge do frontend Angular
2. Revisar TODOS os arquivos Angular criados e modificados
3. Verificar:
   - Seguranca (XSS, sanitizacao, innerHTML)
   - Qualidade (memory leaks, subscriptions, async pipes, tipagem)
   - Performance (OnPush, trackBy, lazy loading, bundle size)
   - Convencoes (nomenclatura, estrutura de modulos, uso de libs)
4. Pontuar confianca de cada issue (0-100)
5. Reportar APENAS issues com confianca >= 75
6. Emitir veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO
```

#### 6.2 - Processar Veredicto

| Veredicto               | Acao                                                              |
|-------------------------|-------------------------------------------------------------------|
| **APROVADO**            | Prosseguir para Phase 7                                           |
| **APROVADO COM RESSALVAS** | Apresentar ressalvas, perguntar se corrige ou prossegue        |
| **REPROVADO**           | Apresentar issues criticas, voltar para Phase 4 com correcoes     |

#### 6.3 - Ciclo de Correcao (se REPROVADO)

Se reprovado:
1. Apresentar issues criticas ao usuario
2. Perguntar: "Deseja que o developer corrija os problemas encontrados? (S/N)"
3. Se sim: relancar o developer especializado (taxone-plsql/pb/java) com as correcoes necessarias
4. Apos correcao: relancar o reviewer especializado correspondente (nova iteracao)
5. **Maximo de 3 iteracoes de review.** Apos 3 reprovacoes, parar e reportar ao usuario.

Se APROVADO COM RESSALVAS e usuario escolhe corrigir:
1. Relancar o developer especializado APENAS para as ressalvas listadas
2. Relancar o reviewer especializado para validar correcoes
3. Prosseguir para Phase 7

---

## Phase 7 - Commit, Push e PR

### Objetivo
Commitar as mudancas, fazer push e criar Pull Request no GitHub.

### Passos

#### 7.1 - Preparar Commit

Verificar todos os arquivos a serem commitados:

```bash
git status
git diff --stat
```

Apresentar ao usuario:
```
Arquivos para commit:
{lista de arquivos}

Mensagem de commit proposta:
"[#{work-item-id}] {titulo-resumido}

{descricao das mudancas - 2-3 linhas}

Work Item: #{work-item-id}
Reviewed-by: taxone-reviewer (AI)
AI-Implemented: true"

Confirmar commit? (S/N)
```

#### 7.2 - Executar Commit

```bash
git add .
git commit -m "[#{work-item-id}] {titulo-resumido}

{descricao das mudancas}

Work Item: #{work-item-id}
Reviewed-by: taxone-reviewer (AI)
AI-Implemented: true"
```

#### 7.3 - Push para Remote

```bash
git push -u origin "{branch_name}"
```

Se o push falhar (ex: autenticacao), informar ao usuario e pedir para resolver.

#### 7.4 - Criar Pull Request

```bash
gh pr create \
  --title "[#{work-item-id}] {titulo}" \
  --body "$(cat <<'EOF'
## User Story

**#{work-item-id}** - {titulo}
**Link ADO:** https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/{work-item-id}

## Descricao

{descricao-resumida das mudancas implementadas}

## Analise Arquitetural

{resumo do design - packages/objetos alterados}

## Analise DBA

{resumo das recomendacoes DBA - se Phase 2.5 foi executada, senao "N/A"}

## Arquivos Modificados

{lista de arquivos com descricao breve de cada mudanca}

## Scripts DDL

{lista de scripts DDL - se houver, senao "N/A"}

## Testes

{resumo dos testes criados - se Phase 5 foi executada, senao "N/A - Testes manuais a serem realizados"}

## Code Review

**Veredicto:** {veredicto do reviewer}
{resumo do review}

## Checklist

- [x] Analise arquitetural (taxone-architect)
- [{x se DBA}] Analise DBA Oracle (taxone-dba)
- [x] Implementacao (taxone-developer)
- [{x se testes}] Scripts de teste (taxone-tester)
- [x] Code review (taxone-reviewer)
- [x] Tag AI-Implemented

---
> Implementacao automatizada via pipeline `taxone-us-auto-implement`
EOF
)" \
  --base DEV
```

#### 7.5 - Registrar URL do PR

Capturar a URL do PR criado para uso na Phase 8.

```bash
PR_URL=$(gh pr create ... 2>&1 | grep -o 'https://.*')
```

Apresentar ao usuario:
```
Pull Request criado com sucesso!
URL: {PR_URL}
Branch: {branch_name} → main
```

---

## Phase 7.5 - Pacote Unitario (GitHub Actions)

### Objetivo
Disparar automaticamente o workflow de geracao de pacote unitario no repositorio `tr/taxone_automacao_fab`,
para que o QA tenha o pacote disponivel para validacao no ambiente de teste.

### Condicao
**CONDICIONAL** - Executada SOMENTE se os arquivos modificados incluem PowerBuilder (`ws_objects/`) ou PL/SQL/BD (`artifacts/sp/`).
Alteracoes APENAS em `artifacts/java/` (Jasper/Java) **NAO geram pacote unitario**.

### Logica de Decisao

| Arquivos modificados | Workflow | Tipo | Acao |
|---------------------|----------|------|------|
| `ws_objects/**` (PowerBuilder) | **Workflow 1** (ID: 154750734) | `F` | Full Build (PB + PL/SQL) |
| `artifacts/sp/**` (PL/SQL/BD) | **Workflow 3** (ID: 154753513) | `P` | Banco (somente PL/SQL) |
| `ws_objects/**` + `artifacts/sp/**` | **Workflow 1** (ID: 154750734) | `F` | Full Build (PB inclui BD) |
| `artifacts/sp/**` + `artifacts/java/**` | **Workflow 3** (ID: 154753513) | `P` | Banco (Java nao precisa pacote) |
| Apenas `artifacts/java/**` | **Nenhum** | - | **PULAR** - Jasper/Java nao precisa pacote unitario |

**Regra simplificada:**
1. Se algum arquivo `ws_objects/` foi modificado → **Workflow 1, Tipo=F** (Full Build)
2. Se apenas `artifacts/sp/` (com ou sem `artifacts/java/`) → **Workflow 3, Tipo=P** (Banco)
3. Se apenas `artifacts/java/` → **NAO disparar pacote**

**Tipos fixos:** Workflow 1/2 sempre `F`, Workflow 3 sempre `P`. Nao variam.

**Workflow 2** (ID: 154753149) e alternativo ao Workflow 1, usar se Workflow 1 estiver ocupado ou falhando.

### Passos

#### 7.5.1 - Determinar Necessidade de Pacote

Listar arquivos modificados no PR:

```bash
"/c/Program Files/GitHub CLI/gh.exe" pr view {PR_NUMBER} -R tr/taxone_dw --json files --jq '.files[].path'
```

Classificar:
```
has_pb = algum arquivo comeca com "ws_objects/"
has_plsql = algum arquivo comeca com "artifacts/sp/"
has_java_only = todos arquivos comecam com "artifacts/java/" (sem PB nem PL/SQL)
```

Se `has_java_only` ou nenhum arquivo relevante:
```
Phase 7.5 - Pacote Unitario: PULADA (arquivos nao requerem pacote unitario)
```
Continuar para Phase 8.

#### 7.5.2 - Confirmar com Usuario

Apresentar ao usuario:
```
Pacote Unitario - Geracao Automatica
=====================================

Arquivos no PR:
{lista de arquivos}

Decisao: {Workflow X, Tipo=Y}
  - Workflow: {nome do workflow}
  - Tipo: {S/BC}
  - Branch: MFS{work-item-id}

Disparar workflow de pacote unitario? (S/N)
```

Se usuario negar, registrar como "Pacote nao solicitado" e continuar para Phase 8.

#### 7.5.3 - Disparar Workflow

```bash
# Para Workflow 1 (PowerBuilder - Full Build):
"/c/Program Files/GitHub CLI/gh.exe" workflow run 154750734 \
  -f Tipo=F \
  -f MFS=MFS{work-item-id} \
  -R tr/taxone_automacao_fab

# Para Workflow 3 (Banco/PL/SQL):
"/c/Program Files/GitHub CLI/gh.exe" workflow run 154753513 \
  -f Tipo=P \
  -f MFS=MFS{work-item-id} \
  -R tr/taxone_automacao_fab
```

#### 7.5.4 - Verificar Inicio da Execucao

Aguardar ~30 segundos e verificar se o run foi criado:

```bash
sleep 30
"/c/Program Files/GitHub CLI/gh.exe" run list \
  -R tr/taxone_automacao_fab \
  -w {WORKFLOW_ID} \
  --limit 1 \
  --json databaseId,status,conclusion,createdAt,headBranch
```

Validar que o run mais recente corresponde ao MFS disparado.

#### 7.5.5 - Registrar Resultado

Capturar o `RUN_ID` e apresentar:
```
Pacote Unitario disparado com sucesso!
  Workflow: {nome}
  Tipo: {tipo}
  Run ID: {RUN_ID}
  URL: https://github.com/tr/taxone_automacao_fab/actions/runs/{RUN_ID}
  Status: {in_progress/queued}

O pacote sera gerado no runner self-hosted. Acompanhe pela URL acima.
```

**NAO bloquear o pipeline** — continuar para Phase 8 imediatamente.
O pacote roda em runner self-hosted Windows e pode levar varios minutos.

Salvar variavel `PKG_RUN_ID` e `PKG_RUN_URL` para uso na Phase 8 (relatorio final).

---

## Phase 8 - Atualizar ADO e Relatorio Final

### Objetivo
Atualizar o work item no Azure DevOps com os resultados do pipeline e apresentar relatorio final.

### Passos

#### 8.0 - Coletar Resultado da Phase 5.5 e 5.7 (Background)

> **OBRIGATORIO se Phase 5.5 e/ou 5.7 foram lancadas em background.**

**8.0.1 - Coletar Phase 5.5 (SuiteAutomation)**

Se `OPT_REGRESSION == true` e Phase 5.5 foi lancada:

```
# Tentar coletar resultado (non-blocking)
TaskOutput(task_id=SUITE_RUNNER_TASK_ID, block=false, timeout=5000)
```

**Se resultado disponivel:** Extrair dados de PASS/FAIL e incluir no relatorio.

**Se ainda em execucao (timeout):**
- Tentar mais uma vez com `block=true, timeout=30000` (30s de espera)
- Se ainda nao completou: registrar como "Em execucao" no relatorio
  ```
  Regressao SuiteAutomation: Em execucao (background)
  Resultado sera disponibilizado quando o agente completar.
  ```

**Se falhou:** Registrar como "Falha na execucao" com a mensagem de erro.

Guardar resultado em `SUITE_RESULT` para uso nos campos do ADO.

**8.0.2 - Coletar Phase 5.7 (Playwright E2E)**

Se `OPT_E2E == true` e Phase 5.7 foi lancada:

```
# Tentar coletar resultado (non-blocking)
TaskOutput(task_id=E2E_TESTER_TASK_ID, block=false, timeout=5000)
```

**Se resultado disponivel:** Extrair dados de PASS/FAIL/FLAKY e incluir no relatorio.

**Se ainda em execucao (timeout):**
- Tentar mais uma vez com `block=true, timeout=30000` (30s de espera)
- Se ainda nao completou: registrar como "Em execucao" no relatorio
  ```
  Testes E2E Playwright: Em execucao (background)
  Resultado sera disponibilizado quando o agente completar.
  ```

**Se falhou:** Registrar como "Falha na execucao" com a mensagem de erro.

Guardar resultado em `E2E_RESULT` para uso nos campos do ADO.

#### 8.1 - Adicionar Tag AI-Implemented

```bash
# Buscar tags atuais
CURRENT_TAGS=$(curl -s \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{ID}?api-version=7.1" \
  | jq -r '.fields["System.Tags"] // ""')

# Adicionar AI-Implemented se nao existir
if [[ "$CURRENT_TAGS" != *"AI-Implemented"* ]]; then
  NEW_TAGS="$CURRENT_TAGS; AI-Implemented"
fi
```

#### 8.2 - Atualizar Campos do Work Item

```bash
curl -s -X PATCH \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -H "Content-Type: application/json-patch+json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{ID}?api-version=7.1" \
  -d '[
    {
      "op": "replace",
      "path": "/fields/System.Tags",
      "value": "{NEW_TAGS}"
    },
    {
      "op": "replace",
      "path": "/fields/Custom.Solutions",
      "value": "{INTERNAL_COM_HTML}"
    },
    {
      "op": "replace",
      "path": "/fields/Custom.DeveloperText",
      "value": "taxone-reviewer (AI Pipeline)"
    },
    {
      "op": "replace",
      "path": "/fields/TR.WOW.AIPowered",
      "value": "true"
    },
    {
      "op": "replace",
      "path": "/fields/Microsoft.VSTS.Common.AcceptanceCriteria",
      "value": "{ACCEPTANCE_CRITERIA_HTML}"
    },
    {
      "op": "replace",
      "path": "/fields/Custom.DescriptionofReleaseNotes",
      "value": "{RELEASE_NOTES_HTML}"
    },
    {
      "op": "replace",
      "path": "/fields/Custom.DescriptionofRootCause",
      "value": "{ROOT_CAUSE_HTML}"
    }
  ]'
```

#### 8.3 - Conteudo do InternalCom

O campo `Custom.Solutions` deve conter um resumo HTML do pipeline:

```html
<div>
  <h3>Pipeline AI - Implementacao Automatizada</h3>
  <p><strong>Data:</strong> {data-hora}</p>
  <p><strong>Work Item:</strong> #{ID} - {titulo}</p>
  <p><strong>Branch:</strong> {branch_name}</p>
  <p><strong>PR:</strong> <a href="{PR_URL}">{PR_URL}</a></p>

  <h4>Fases Executadas</h4>
  <ul>
    <li>Analise Arquitetural: Concluida (taxone-architect)</li>
    <li>Analise DBA: {Concluida/Nao solicitada} (taxone-dba)</li>
    <li>Implementacao: Concluida (taxone-developer)</li>
    <li>Testes: {Concluidos/Nao solicitados} (taxone-tester)</li>
    <li>Regressao SuiteAutomation: {Concluida X PASS Y FAIL/Nao solicitada} (taxone-suite-runner)</li>
    <li>Code Review: {veredicto} (taxone-reviewer)</li>
  </ul>

  <h4>Arquivos Modificados</h4>
  <ul>
    {lista de arquivos - <li> para cada}
  </ul>

  <h4>Notas</h4>
  <p>{observacoes relevantes}</p>
</div>
```

#### 8.3a - Conteudo do Acceptance Criteria

O campo `Microsoft.VSTS.Common.AcceptanceCriteria` deve conter criterios de validacao derivados da analise:

```html
<ul>
  <li>Verificar que {descricao da mudanca principal} funciona corretamente</li>
  <li>Confirmar que {cenario de teste 1 - derivado da analise arquitetural}</li>
  <li>Confirmar que {cenario de teste 2 - cenario de regressao}</li>
  <li>Executar scripts de validacao SQL (se houver)</li>
</ul>
```

#### 8.3b - Conteudo do Description of Release Notes

O campo `Custom.DescriptionofReleaseNotes` deve descrever o impacto da mudanca:

```html
<div>
  <p><strong>Mudanca:</strong> {descricao do que mudou - resumo funcional}</p>
  <p><strong>Arquivos:</strong> {lista de arquivos modificados}</p>
  <p><strong>Impacto:</strong> {impacto funcional - quais processos/relatorios afetados}</p>
  <p><strong>DDL:</strong> {scripts DDL necessarios, ou "Nenhum"}</p>
</div>
```

#### 8.3c - Conteudo do Description of Root Cause

O campo `Custom.DescriptionofRootCause` deve descrever a causa raiz do problema:

```html
<div>
  <p>{Descricao da causa raiz do problema}</p>
  <p><strong>Analise:</strong> {resumo da analise do architect}</p>
  <p><strong>Zendesk:</strong> {contexto Zendesk se disponivel, ou "N/A"}</p>
</div>
```

#### 8.3d - Discussion Comments (Templates Padronizados)

Usar o modulo centralizado `scripts/ado_discussion_templates.py` para gerar e postar comments padronizados.

**Comment 1: Analise & Implementacao**

```python
from scripts.ado_discussion_templates import build_analysis_comment, post_discussion_comment

html = build_analysis_comment(
    wi_id=WI_ID,
    wi_title=WI_TITLE,
    pipeline="taxone-us-auto-implement",
    analysis={
        "causa_raiz": "...",           # descricao da causa raiz
        "veredicto": "BUG_CONFIRMED",  # ou NOT_BUG, FEATURE_REQUEST, etc.
        "impacto": "...",              # descricao do impacto
        "hipoteses": ["...", "..."],   # hipoteses investigadas (opcional)
    },
    implementation={
        "branch": "MFS{WI_ID}",
        "pr_url": PR_URL,
        "pr_number": PR_NUMBER,
        "files": [{"path": "...", "action": "modificado"}],
        "ddls": [],                    # lista de DDLs ou []
        "code_review": "PASS",         # veredicto do review
        "compilacao": "COMPILADO",     # status da compilacao
    },
    phases=[
        {"name": "Phase 0 - Carga WI", "status": "PASS", "duration": "..."},
        {"name": "Phase 1 - Knowledge", "status": "PASS", "duration": "..."},
        {"name": "Phase 2 - Analise arquitetural", "status": "PASS", "duration": "..."},
        {"name": "Phase 2.5 - Analise DBA", "status": "PASS|SKIP", "duration": "..."},
        {"name": "Phase 3 - Branch", "status": "PASS", "duration": "..."},
        {"name": "Phase 4 - Implementacao", "status": "PASS", "duration": "..."},
        {"name": "Phase 4.5 - Regras Negocio", "status": "PASS|SKIP", "duration": "..."},
        {"name": "Phase 5 - Testes", "status": "PASS", "duration": "..."},
        {"name": "Phase 5.5 - SuiteAutomation", "status": "PASS|SKIP", "duration": "..."},
        {"name": "Phase 6 - Code Review", "status": "PASS", "duration": "..."},
        {"name": "Phase 7 - Commit/Push/PR", "status": "PASS", "duration": "..."},
        {"name": "Phase 8 - ADO Update", "status": "PASS", "duration": "..."},
    ],
    pendencias=["..."],  # o que NAO foi feito (ou [] se tudo concluido)
    zendesk={"ticket_id": "...", "status": "...", "resumo": "..."},  # ou None
)
post_discussion_comment(WI_ID, html)
```

**Comment 2: Resultados de Testes** (postar apos Phase 5/5.5)

```python
from scripts.ado_discussion_templates import build_test_results_comment, post_discussion_comment

html = build_test_results_comment(
    wi_id=WI_ID,
    wi_title=WI_TITLE,
    agent="taxone-us-auto-implement",
    db_connection="V2R010AC@localhost:1521/MFSPDB",
    manual_tests=[
        {"num": 1, "cenario": "...", "status": "PASS", "detalhe": "..."},
    ],
    suite_results={
        "xml": "CT_xxx.xml",
        "range": "N;N",
        "total": 10, "passed": 9, "failed": 1,
        "duration_s": 120,
        "verdict": "PASS",
        "failures": ["..."],
    },  # ou None se nao executado
    nao_testado=["..."],  # o que ficou sem cobertura
    attachments=[{"filename": "...", "url": "..."}],
)
post_discussion_comment(WI_ID, html)
```

Os templates geram HTML padronizado com cores consistentes (azul `#004578` header, verde PASS, vermelho FAIL, amarelo SKIP) e secoes bem definidas.

#### 8.4 - Relatorio Final para o Usuario

Apresentar relatorio consolidado:

```
==========================================================
  RELATORIO FINAL - PIPELINE DE IMPLEMENTACAO
==========================================================

  Work Item: #{ID} - {titulo}
  Branch:    {branch_name}
  PR:        {PR_URL}
  ADO:       https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/{ID}

----------------------------------------------------------
  FASES EXECUTADAS
----------------------------------------------------------

  [OK] Phase 0   - Work item carregado do ADO
  [OK] Phase 1   - Knowledge carregado, opcoes confirmadas
  [OK] Phase 2   - Analise arquitetural (taxone-architect)
  [{status}] Phase 2.5 - Analise DBA (taxone-dba)
  [OK] Phase 3   - Branch criada: {branch_name}
  [OK] Phase 4   - Implementacao (taxone-developer)
  [{status}] Phase 4.5 - Impacto Regras Negocio (taxone-architect)
  [{status}] Phase 5   - Testes SQL (taxone-tester)
  [{status}] Phase 5.5 - Regressao SuiteAutomation (taxone-suite-runner)
  [{status}] Phase 5.7 - Testes E2E Playwright (taxone-e2e-tester)
  [OK] Phase 6   - Code Review: {veredicto} (taxone-reviewer)
  [OK] Phase 7   - Commit + Push + PR criado
  [{status}] Phase 7.5 - Pacote Unitario: {Disparado (Workflow X, Tipo Y) / Pulada (Java-only) / Nao solicitado}
  [OK] Phase 8   - ADO atualizado (tag + InternalCom + AcceptanceCriteria + ReleaseNotes + RootCause + Discussion)

----------------------------------------------------------
  RESUMO DAS MUDANCAS
----------------------------------------------------------

  Arquivos criados:     {N}
  Arquivos modificados: {N}
  Scripts DDL:          {N}
  Scripts de teste:     {N}

  {lista resumida de arquivos}

----------------------------------------------------------
  PROXIMOS PASSOS
----------------------------------------------------------

  1. Revisar o PR no GitHub: {PR_URL}
  2. Acompanhar pacote unitario: {PKG_RUN_URL ou "N/A - sem pacote"}
  3. Executar scripts DDL em ambiente de DEV/QA (se houver)
  4. Executar scripts de validacao SQL (se houver)
  5. Seguir roteiro de teste manual (se houver)
  6. Aprovar e mergear o PR

==========================================================
  Pipeline concluido com sucesso!
==========================================================
```

---

## Phase 9 - Compound Engineering

### Objetivo
Atualizar a knowledge base do plugin com o aprendizado desta implementacao.

### Condicao
**OPCIONAL** - Executada APENAS se `OPT_COMPOUND == true` (selecionado na Phase 1.3).

### Passos

#### 9.1 - Avaliar o que Aprender

Analisar a implementacao concluida e identificar:
- Nova feature/modulo que deve ser documentada?
- Novos patterns descobertos?
- Novos packages/tabelas mapeados?
- Integracoes entre modulos identificadas?
- Cenarios de bug recorrentes?

#### 9.2 - Propor Atualizacao de Knowledge

Apresentar ao usuario:

```
Compound Engineering - Atualizacao de Knowledge

Baseado na implementacao de #{ID}, identifiquei as seguintes oportunidades:

1. [FEATURE] Criar/atualizar knowledge de: {feature}
   - Packages: {lista}
   - Tabelas: {lista}
   - Fluxos: {descricao}

2. [PATTERN] Novo pattern identificado: {descricao}
   - Exemplo: {referencia ao codigo implementado}

3. [INTEGRACAO] Integracao entre modulos: {modulos}
   - Detalhes: {como se comunicam}

Deseja que eu atualize a knowledge base? (S/N)
```

#### 9.3 - Executar Atualizacao

Se aprovado pelo usuario, sugerir que o usuario execute:
```
/taxone-compound
```

Com o contexto da implementacao realizada, para que o agente de compound engineering
atualize os arquivos de knowledge de forma estruturada.

**IMPORTANTE:** O orquestrador NAO atualiza knowledge diretamente.
A atualizacao deve ser feita pelo skill/comando dedicado (`taxone-compound`).

---

## Tratamento de Erros

### Tabela de Erros e Acoes

| Codigo/Situacao                          | Fase     | Acao                                                                                              |
|------------------------------------------|----------|---------------------------------------------------------------------------------------------------|
| `ADO_PAT` nao configurado               | Phase 0  | PARAR. Informar usuario para configurar a variavel de ambiente.                                   |
| Work Item nao encontrado (404)           | Phase 0  | PARAR. Informar ID invalido. Perguntar novo ID.                                                   |
| Work Item sem descricao                  | Phase 0  | ALERTAR. Perguntar se deseja continuar sem descricao.                                             |
| Work Item fora do Area Path TAX ONE      | Phase 0  | ALERTAR. Perguntar se deseja continuar mesmo assim.                                               |
| Query retorna 0 resultados              | Phase 0.5| PARAR. Informar que a query nao retornou work items.                                              |
| Knowledge nao encontrado                 | Phase 1  | ALERTAR. Continuar sem knowledge (pipeline nao depende disso).                                    |
| Architect nao retorna design             | Phase 2  | RETRY 1x. Se falhar, perguntar ao usuario se deseja fornecer design manualmente.                  |
| DBA identifica risco critico             | Phase 2.5| ALERTAR. Apresentar riscos e perguntar se deseja prosseguir.                                      |
| Branch ja existe                         | Phase 3  | Perguntar: deletar e recriar, ou usar a existente?                                                |
| Mudancas pendentes no workspace          | Phase 3  | Perguntar: stash, commit, ou abortar?                                                             |
| `git pull` falha (conflitos)             | Phase 3  | PARAR. Informar conflitos. Pedir resolucao manual.                                                |
| Developer nao cria/modifica arquivos     | Phase 4  | RETRY 1x com prompt mais especifico. Se falhar, reportar ao usuario.                              |
| Developer cria arquivos fora do escopo   | Phase 4  | ALERTAR no review. Pedir ao usuario para confirmar.                                               |
| Tester falha ao criar scripts            | Phase 5  | ALERTAR. Continuar sem testes (fase e opcional).                                                  |
| Review REPROVADO                         | Phase 6  | Voltar para Phase 4 (max 3 iteracoes). Apos 3, parar e reportar.                                 |
| Review timeout / sem resposta            | Phase 6  | RETRY 1x. Se falhar, perguntar ao usuario se deseja continuar sem review (NAO recomendado).       |
| `git push` falha (autenticacao)          | Phase 7  | PARAR. Informar erro de autenticacao. Pedir `gh auth login` ou configuracao de credenciais.       |
| `git push` falha (branch protegida)      | Phase 7  | PARAR. Informar que a branch nao permite push direto. Verificar permissoes.                       |
| `gh pr create` falha                     | Phase 7  | RETRY 1x. Se falhar, fornecer comando manual para o usuario executar.                             |
| PR ja existe para a branch               | Phase 7  | Informar URL do PR existente. Perguntar: atualizar ou criar novo.                                 |
| `gh workflow run` falha                  | Phase 7.5| RETRY 1x. Se falhar, fornecer comando manual. NAO bloqueia pipeline.                              |
| Workflow nao inicia apos 60s             | Phase 7.5| ALERTAR. Fornecer URL do Actions para acompanhamento manual. Continuar para Phase 8.              |
| Workflow 1 ocupado (concurrency)         | Phase 7.5| Tentar Workflow 2 (alternativo). Se tambem ocupado, informar e continuar.                         |
| Atualizacao do ADO falha (403)           | Phase 8  | ALERTAR. Informar que o PAT nao tem permissao para atualizar. Fornecer dados para update manual.  |
| Atualizacao do ADO falha (campo invalido)| Phase 8  | ALERTAR. Tentar atualizar apenas os campos que funcionam. Reportar campos que falharam.            |
| Compound falha                           | Phase 9  | ALERTAR. Continuar (fase e opcional). Sugerir `/taxone-compound` manual depois.                   |

### Principios de Tratamento de Erros

1. **NUNCA falhar silenciosamente.** Todo erro deve ser reportado ao usuario.
2. **Erros em fases opcionais (2.5, 5, 7.5, 9) NAO bloqueiam o pipeline.** Alertar e continuar.
3. **Erros em fases obrigatorias (0, 2, 4, 6, 7) BLOQUEIAM o pipeline.** Tentar 1 retry, depois parar.
4. **Sempre oferecer alternativa ao usuario** quando possivel (ex: fornecer comando manual).
5. **Registrar todos os erros** no relatorio final (Phase 8) para rastreabilidade.
6. **Nunca expor tokens/PATs** em mensagens de erro ou logs.

### Retry Policy

| Fase     | Max Retries | Intervalo    | Acao apos falha final                    |
|----------|-------------|--------------|------------------------------------------|
| Phase 0  | 2           | Imediato     | Parar pipeline                           |
| Phase 2  | 1           | Imediato     | Pedir design manual ao usuario           |
| Phase 2.5| 1           | Imediato     | Pular fase (e condicional)               |
| Phase 4  | 2           | Imediato     | Parar pipeline                           |
| Phase 5  | 1           | Imediato     | Pular fase (e condicional)               |
| Phase 6  | 3           | Imediato     | Parar pipeline (review e obrigatorio)    |
| Phase 7  | 1           | Imediato     | Fornecer comandos manuais ao usuario     |
| Phase 7.5| 1           | Imediato     | Pular fase (e condicional). Fornecer cmd manual |
| Phase 8  | 2           | Imediato     | Fornecer dados para update manual        |

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
    {
      "op": "replace",
      "path": "/fields/System.Tags",
      "value": "AI-Implemented"
    },
    {
      "op": "replace",
      "path": "/fields/Custom.Solutions",
      "value": "<div>Conteudo HTML aqui</div>"
    },
    {
      "op": "replace",
      "path": "/fields/Custom.DeveloperText",
      "value": "taxone-reviewer (AI Pipeline)"
    },
    {
      "op": "replace",
      "path": "/fields/TR.WOW.AIPowered",
      "value": "true"
    }
  ]'
```

### Adicionar Comentario ao Work Item

```bash
curl -s -X POST \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -H "Content-Type: application/json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/54321/comments?api-version=7.1-preview.4" \
  -d '{
    "text": "<div>Comentario do pipeline aqui</div>"
  }'
```

---

## Apendice B - Template de Branch e Commit

### Branch

```
{git-user}/feature/{work-item-id}
```

Exemplos:
- `jsilva/feature/54321`
- `mferreira/feature/67890`

### Commit Message

```
[#{work-item-id}] {titulo-resumido-max-72-chars}

{descricao das mudancas em 2-5 linhas}

- {arquivo1}: {mudanca}
- {arquivo2}: {mudanca}

Work Item: #{work-item-id}
Reviewed-by: taxone-reviewer (AI)
AI-Implemented: true
```

### PR Title

```
[#{work-item-id}] {titulo-da-user-story}
```

---

## Apendice C - Checklist Pre-Pipeline

Antes de executar o pipeline, verificar:

- [ ] `ADO_PAT` configurado como variavel de ambiente
- [ ] `gh auth status` retorna autenticado
- [ ] `git config user.name` e `git config user.email` configurados
- [ ] Repositorio TAX ONE clonado e atualizado
- [ ] Branch `main` sem mudancas pendentes
- [ ] Work Item ID ou Query ID em maos

---

## Apendice D - Diferencas em Relacao ao LegalOne

| Aspecto                    | LegalOne                              | TAX ONE                                          |
|----------------------------|---------------------------------------|--------------------------------------------------|
| ADO Org/Project            | (outro org/project)                   | `tr-ggo/Mastersaf Fiscal Solutions`              |
| Stack principal            | C#/.NET                               | PL/SQL/PowerBuilder/Java                         |
| Build local                | `dotnet build`                        | NAO EXISTE (PL/SQL compila no Oracle)            |
| Testes automatizados       | xUnit/NUnit                           | NAO EXISTE (scripts SQL de validacao)            |
| Observabilidade            | DataDog/AppInsights                   | Analise DBA Oracle (performance, indices)        |
| PR                         | Azure DevOps PR                       | GitHub PR (`gh pr create`)                       |
| Target branch              | `develop`                             | `main`                                           |
| Branch pattern             | (outro pattern)                       | `MFS{work-item-id}`                  |
| Agentes                    | Prefixo `legalone-`                   | Prefixo `taxone-`                                |
| Tag                        | (outra tag)                           | `AI-Implemented`                                 |
| InternalCom field          | (outro campo)                         | `Custom.Solutions`                             |
| DevReviewName field        | (outro campo)                         | `Custom.DeveloperText`                           |
| Area Path                  | (outro path)                          | `Mastersaf Fiscal Solutions\MFS\TAX ONE\Suporte` |
