---
name: taxone-auto-fix
description: >
  Pipeline automatizado de correcao de bugs do Azure DevOps para o TAX ONE.
  Busca bugs via WIQL query, cria branch, orquestra agentes especializados
  (PL/SQL, PowerBuilder, Java, DBA, Tester), faz commit/push, cria PR no
  GitHub e atualiza o work item no ADO com tags e campos customizados.
version: 1.0.0
---

# taxone-auto-fix

Pipeline end-to-end de correcao automatizada de bugs vindos do Azure DevOps
para o projeto **TAX ONE** (Mastersaf Fiscal Solutions) da Thomson Reuters.

O pipeline busca bugs de uma query ADO, apresenta ao usuario, cria branch,
carrega knowledge embarcado, orquestra agentes especializados para diagnostico,
implementacao, review e testes, e finaliza com commit, push, PR no GitHub e
atualizacao do work item no ADO.

---

## Configuracao

### Constantes ADO

| Constante | Valor |
|-----------|-------|
| **ADO_ORG** | `tr-ggo` |
| **ADO_PROJECT** | `Mastersaf Fiscal Solutions` |
| **ADO_PROJECT_ENCODED** | `Mastersaf%20Fiscal%20Solutions` |
| **ADO_API_VERSION** | `api-version=7.1` |
| **ADO_BASE_URL** | `https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions` |
| **AREA_PATH** | `Mastersaf Fiscal Solutions\MFS\TAX ONE\Suporte` |

### Constantes do Pipeline

| Constante | Valor |
|-----------|-------|
| **BRANCH_PATTERN** | `MFS{work-item-id}` (sufixos: `MFS{id}a`, `MFS{id}b` para correcoes adicionais) |
| **TARGET_BRANCH** | `DEV` |
| **TAG_BUG_REAL** | `AI-Fixed` |
| **TAG_AS_DESIGNED** | `AI-AsDesigned` |
| **INTERNAL_COM_FIELD** | `Custom.Solutions` |
| **DEV_REVIEW_FIELD** | `Custom.DeveloperText` |
| **KNOWLEDGE_PATH** | `${CLAUDE_PLUGIN_ROOT}/knowledge/` |
| **ADO_GUIDE_PATH** | `${CLAUDE_PLUGIN_ROOT}/references/ado-api-guide.md` |

### Datadog (Observabilidade)

| Constante | Valor |
|-----------|-------|
| **DD_ORG** | `trta-onesource` |
| **DD_MCP_SERVER** | `datadog` (configurado em `~/.claude.json`, auth via OAuth) |
| **DD_PERMISSAO** | MCP Read (somente leitura) |

### Agentes Disponiveis

| Agente | Funcao | Ferramentas |
|--------|--------|-------------|
| **taxone-n3-triage** | Enrichment e estruturacao de WIs N3 (pre-PM) | Read, Grep, Glob, Bash |
| **taxone-pm** | Triagem, classificacao de WIs e geracao de cenarios de teste | Read, Write, Grep, Glob, Bash |
| **taxone-architect** | Analise de impacto, design de solucao | Read, Grep, Glob |
| **taxone-plsql** | Implementacao PL/SQL (packages, procedures, views) | Read, Write, Edit, Bash, Grep, Glob |
| **taxone-pb** | Implementacao PowerBuilder (DataWindows, scripts) | Read, Write, Edit, Bash, Grep, Glob |
| **taxone-java** | Implementacao Java (web services, Jasper, servlets) | Read, Write, Edit, Bash, Grep, Glob |
| **taxone-dba** | Analise critica Oracle, performance, DDL | Read, Write, Edit, Grep, Glob |
| **taxone-plsql-reviewer** | Code review PL/SQL Oracle | Read, Grep, Glob |
| **taxone-pb-reviewer** | Code review PowerBuilder | Read, Grep, Glob |
| **taxone-java-reviewer** | Code review Java | Read, Grep, Glob |
| **taxone-angular** | Implementacao + Review Angular 11 frontend | Read, Write, Edit, Bash, Grep, Glob |
| **taxone-tester** | Scripts SQL de validacao, roteiros manuais | Read, Write, Edit, Bash, Grep, Glob |
| **taxone-sm** | Alocacao avulsa de Dev/Tester por afinidade | Read, Grep, Glob, Bash |

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

#### Template de Documentacao na WI (Custom.Solutions)

```
[CONSULTA REMOTA DESPACHADA - {DATA}]
Fase: {fase_atual}
Query: {SQL}
Empresa: {empresa}
Ambiente: {env}
Motivo: {justificativa do agente}
Status: AGUARDANDO RESULTADO (email)
```

---

## Regras

### R1 - Usar APENAS os agentes deste plugin

Os UNICOS agentes que podem ser lancados sao:
- `taxone-pm`
- `taxone-architect`
- `taxone-plsql`
- `taxone-pb`
- `taxone-java`
- `taxone-angular`
- `taxone-dba`
- `taxone-plsql-reviewer`
- `taxone-pb-reviewer`
- `taxone-java-reviewer`
- `taxone-tester`
- `taxone-sm`

**PROIBIDO** invocar qualquer agente externo ao plugin.

### R2 - Bash apenas para operacoes de infraestrutura

O Bash pode ser usado **SOMENTE** para:
- `curl` - chamadas a ADO REST API
- `git` - operacoes de versionamento (branch, add, commit, push)
- `gh` - GitHub CLI (criar PR, autenticacao)
- `echo` / `printenv` - verificar variaveis de ambiente
- `python run_query.py` - despachar queries SELECT para Prod/UAT via GitHub Actions
- `python scripts/empresa_resolver.py` - resolver empresa/tenant a partir do texto do WI

**PROIBIDO** usar Bash para:
- Explorar ou modificar codigo (usar agentes)
- Executar SQL ou PL/SQL
- Compilar ou buildar qualquer coisa
- Operacoes de filesystem (criar/deletar diretorios)

### R3 - Todo codigo via agentes

- **Exploracao de codigo:** via `taxone-plsql`, `taxone-pb`, `taxone-java`, `taxone-angular` ou `taxone-architect`
- **Implementacao backend:** via `taxone-plsql` (PL/SQL), `taxone-pb` (PowerBuilder), `taxone-java` (Java)
- **Implementacao frontend:** via `taxone-angular` (Angular 11)
- **Analise DBA:** via `taxone-dba`
- **Code review backend:** via `taxone-plsql-reviewer` (PL/SQL), `taxone-pb-reviewer` (PowerBuilder), `taxone-java-reviewer` (Java)
- **Code review frontend:** via `taxone-angular` (modo review)
- **Testes:** via `taxone-tester`

O orquestrador (esta skill) **NUNCA** le ou modifica codigo diretamente.

### R4 - Sem build ou compilacao local

O TAX ONE usa **PL/SQL** como stack principal. PL/SQL e compilado no banco Oracle,
nao localmente. **NUNCA** tentar:
- Compilar PL/SQL
- Fazer build de PowerBuilder
- Executar `msbuild`, `dotnet build`, `maven` ou qualquer ferramenta de build
- Rodar testes automatizados (nao existem - usar taxone-tester para scripts SQL)

### R5 - Confirmacao do usuario antes de acoes destrutivas

**SEMPRE** pedir confirmacao via `AskUserQuestion` ANTES de:
- Criar branch
- Fazer commit
- Fazer push
- Criar PR
- Atualizar work item no ADO (tags, campos, estado)

Apresentar o que sera feito e aguardar `sim`/`ok`/`confirmar` do usuario.

### R6 - Formato de comunicacao

- **Idioma:** Portugues para toda comunicacao com o usuario
- **Formato:** Markdown estruturado
- **Progresso:** Indicar fase atual (ex: `## Fase 3 - Knowledge + Alinhamento`)
- **Erros:** Exibir mensagem clara e sugerir acao corretiva

### R7 - Testes OBRIGATORIOS Antes da PR

**NUNCA pular as fases de teste e ir direto para a PR.**
Compilar NAO e testar. A sequencia obrigatoria e:

1. **Compilar** (DBA) — objetos VALID no banco
2. **Evidencia ANTES** — capturar comportamento atual (query, screenshot, output) ANTES da alteracao
3. **Testes SQL de validacao** (taxone-tester) — cenarios base + alteracao + nao-regressao
4. **Evidencia DEPOIS** — capturar comportamento corrigido APOS a alteracao, comparando com o ANTES
5. **SuiteAutomation** (taxone-suite-runner) — regressao automatizada
6. **Salvar artefatos** em `tests/{WI_ID}/` (incluindo evidencias antes/depois)
7. **Upload Attachments** na WI do ADO
8. **Discussion comment** com resultados de testes (incluindo comparativo antes x depois)
9. **Code review** (reviewer) — APROVADO obrigatorio
10. **Somente entao**: Commit + Push + PR
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
3. Publicar em `cenarios/{WI_ID}/` no repo `taxone_automacao_qa` (Fase 8.5)
**NUNCA perguntar "quer que eu anexe?" — e parte obrigatoria do fluxo.**

### Regra de Visibilidade do Knowledge

**OBRIGATORIO para TODOS os agentes:**

Sempre que qualquer agente for ler um arquivo em `${CLAUDE_PLUGIN_ROOT}/knowledge/`,
**ANTES** de usar a ferramenta Read, deve imprimir:

```
> [Knowledge] Carregando: {nome-do-arquivo} - {descricao-breve}
```

Isto garante rastreabilidade de qual knowledge foi consumido durante o pipeline.

---

## Pipeline de Execucao

### Fase 0 - Resolver Variaveis de Ambiente

**Objetivo:** Garantir que o ambiente esta configurado corretamente.

**Passos:**

1. **Resolver REPO_ROOT:**
   ```bash
   REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
   ```
   - Se falhar: abortar com mensagem `"ERRO: Este comando deve ser executado dentro do repositorio do TAX ONE."`

2. **Resolver usuario Git:**
   ```bash
   GIT_USER=$(git config user.name 2>/dev/null)
   GIT_USER_SLUG=$(echo "$GIT_USER" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
   ```
   - Se vazio: perguntar ao usuario via `AskUserQuestion`

3. **Verificar ADO_PAT:**
   ```bash
   echo "$ADO_PAT" | head -c 5
   ```
   - Se vazio ou inexistente: abortar com mensagem:
     ```
     ERRO: Variavel de ambiente ADO_PAT nao encontrada.
     Configure com: export ADO_PAT="seu-personal-access-token"
     O token precisa de permissoes de leitura/escrita em Work Items.
     ```

4. **Verificar GitHub CLI:**
   ```bash
   gh auth status
   ```
   - Se nao autenticado: abortar com mensagem:
     ```
     ERRO: GitHub CLI nao esta autenticado.
     Execute: gh auth login
     ```

5. **Verificar TAXONE_DW_REPO:**
   ```bash
   test -d "$TAXONE_DW_REPO/.git" && echo "OK" || echo "MISSING"
   ```
   - Se env var vazia ou diretorio nao existe: **AVISAR** (nao abortar):
     ```
     AVISO: TAXONE_DW_REPO nao configurado ou diretorio nao existe.
     Configure no .env: TAXONE_DW_REPO=C:\@@Dev\Git\taxone_dw
     Algumas fases (branch, commit, PR) podem falhar.
     ```

6. **Verificar Oracle acessivel (porta 1521):**
   ```bash
   python -c "import oracledb; c=oracledb.connect(user='V2R010AC',password='V2R010AC',dsn='localhost:1521/MFSPDB'); c.close(); print('OK')" 2>/dev/null || echo "UNAVAILABLE"
   ```
   - Se falhar: **AVISAR** (nao abortar):
     ```
     AVISO: Oracle localhost:1521/MFSPDB nao acessivel.
     Compilacao PL/SQL e SuiteAutomation podem falhar.
     ```

7. **Verificar config/.env e config/environments.json:**
   ```bash
   test -f "${CLAUDE_PLUGIN_ROOT}/config/.env" && echo "ENV_OK" || echo "ENV_MISSING"
   test -f "${CLAUDE_PLUGIN_ROOT}/config/environments.json" && echo "ENVJSON_OK" || echo "ENVJSON_MISSING"
   ```
   - Se `.env` faltando: **AVISAR** com instrucao de copiar de `.env.example`
   - Se `environments.json` faltando: **AVISAR** — scripts multi-ambiente podem falhar

8. **Verificar knowledge/ existe:**
   ```bash
   test -d "${CLAUDE_PLUGIN_ROOT}/knowledge" && echo "OK" || echo "MISSING"
   ```
   - Se faltando: **ABORTAR** — knowledge e obrigatorio para analise:
     ```
     ERRO: Diretorio knowledge/ nao encontrado em ${CLAUDE_PLUGIN_ROOT}.
     O pipeline nao pode executar sem a base de conhecimento.
     ```

9. **Imprimir resumo do ambiente:**
   ```
   ## Fase 0 - Ambiente Validado

   - Repositorio: {REPO_ROOT}
   - Usuario Git: {GIT_USER} ({GIT_USER_SLUG})
   - ADO PAT: configurado (*****)
   - GitHub CLI: autenticado
   - Plugin Root: ${CLAUDE_PLUGIN_ROOT}
   - TAXONE_DW_REPO: {OK / AVISO: nao configurado}
   - Oracle 1521: {OK / AVISO: indisponivel}
   - Config .env: {OK / AVISO: faltando}
   - Config environments.json: {OK / AVISO: faltando}
   - Knowledge: OK
   ```

**Nota:** NAO verificar MSBuild, dotnet, maven ou qualquer ferramenta de build.
O TAX ONE nao possui build local - PL/SQL e compilado diretamente no banco Oracle.

---

### Fase 1 - Buscar Bugs do ADO

**Objetivo:** Executar query WIQL no Azure DevOps e apresentar lista de bugs.

**Entrada:** O usuario fornece o `QUERY_ID` como argumento do comando.
Se nao fornecido, perguntar via `AskUserQuestion`:
```
Informe o ID da query do Azure DevOps (GUID).
Voce pode encontra-lo na URL: https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_queries/query/{QUERY_ID}
```

**Passo 1 - Executar a query:**

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/wiql/$QUERY_ID?api-version=7.1"
```

**Passo 2 - Extrair IDs dos work items** do JSON retornado (campo `workItems[].id`).

**Passo 3 - Para cada work item, buscar detalhes:**

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{ID}?\$expand=all&api-version=7.1"
```

Extrair campos relevantes:
- `System.Id` - ID do work item
- `System.Title` - Titulo
- `System.State` - Estado atual
- `System.AssignedTo` - Responsavel
- `System.Description` - Descricao (HTML)
- `Microsoft.VSTS.TCM.ReproSteps` - Passos de reproducao (HTML)
- `System.Tags` - Tags existentes
- `System.AreaPath` - Area path
- `System.IterationPath` - Iteration
- `Custom.Solutions` - Comunicacao interna
- `Custom.DeveloperText` - Nome do revisor dev

**Passo 4 - Apresentar lista formatada ao usuario:**

```markdown
## Fase 1 - Bugs Encontrados

| # | ID | Titulo | Estado | Responsavel |
|---|----|--------|--------|-------------|
| 1 | {id} | {titulo} | {estado} | {responsavel} |
| 2 | {id} | {titulo} | {estado} | {responsavel} |

Qual bug deseja corrigir? (informe o numero ou ID)
```

**Passo 5 - Aguardar selecao do usuario** via `AskUserQuestion`.

**Passo 6 - Armazenar dados do bug selecionado** em variaveis internas:

```
BUG_ID = {id selecionado}
BUG_TITLE = {titulo}
BUG_DESCRIPTION = {descricao limpa - sem HTML}
BUG_REPRO_STEPS = {passos de reproducao limpos}
BUG_STATE = {estado}
BUG_TAGS = {tags existentes}
```

**Apresentar o bug selecionado:**

```markdown
## Bug Selecionado

- **ID:** {BUG_ID}
- **Titulo:** {BUG_TITLE}
- **Estado:** {BUG_STATE}
- **Area Path:** {area_path}
- **Tags:** {BUG_TAGS}

### Descricao
{BUG_DESCRIPTION}

### Passos de Reproducao
{BUG_REPRO_STEPS}
```

---

### Fase 1.3 - N3 Brief Enrichment

**Objetivo:** Enriquecer e estruturar dados da WI antes da triagem PM. Produz o `n3_brief.json` — documento canonico consumido por todos os agentes downstream.

**Passo 1 - Lancar taxone-n3-triage:**

Invocar via Agent com `subagent_type="taxone-n3-triage"`:

```
## N3 Brief Enrichment - WI #{BUG_ID}

### Dados da Work Item
- **ID:** {BUG_ID}
- **Titulo:** {BUG_TITLE}
- **Descricao:** {BUG_DESCRIPTION}
- **ReproSteps:** {BUG_REPRO_STEPS}
- **Severity:** {BUG_SEVERITY}
- **Area Path:** {area_path}
- **Tags:** {BUG_TAGS}

### Sua Tarefa
Produzir o N3 Brief completo para esta Work Item:
1. Normalizar dados da WI (strip HTML, extrair error codes, numerar repro steps)
2. Enriquecer com Zendesk (se TKT no titulo)
3. Resolver modulo via MODULE_KNOWLEDGE_MAP.json
4. Pre-scan FAQ, Zendesk patterns, solutions, ADO fixes
5. Mapear componentes suspeitos (tabelas, packages)
6. Detectar gaps de dados
7. Coletar sinais de classificacao (SEM emitir veredicto)
8. Salvar tests/{BUG_ID}/n3_brief.json
9. Postar Discussion comment na WI do ADO
```

**Passo 2 - Carregar output:**

Apos retorno do agente, carregar `tests/{BUG_ID}/n3_brief.json` e armazenar em `N3_BRIEF`.

Extrair para variaveis de pipeline:
- `ZD_STATUS` = `N3_BRIEF.zendesk.status`
- `ZD_SUMMARY` = `N3_BRIEF.zendesk.comments_summary`
- `MODULE` = `N3_BRIEF.module.primary`
- `CONFIDENCE` = `N3_BRIEF.confidence.overall`

**Nota:** Esta fase absorve a antiga Fase 1.4 (Enriquecer com Zendesk). O N3 triage ja faz o enrichment Zendesk como parte do processo.

---

### Fase 1.5 - Triagem PM (Gate de Qualidade)

**Objetivo:** Classificar o bug antes de investir tempo em analise tecnica. Identificar
not-a-bugs, feature requests, duplicatas e analises incompletas.

**Pre-condicao:** `tests/{BUG_ID}/n3_brief.json` deve existir (gerado na Fase 1.3).

**Passo 1 - Lancar taxone-pm para triagem:**

Invocar via Agent com `subagent_type="taxone-pm"`:

```
## Triagem de Work Item - Bug #{BUG_ID}

### N3 Brief Disponivel
O N3 Brief ja foi gerado e esta em tests/{BUG_ID}/n3_brief.json.
Carregue-o para aproveitar: modulo resolvido, FAQ pre-scan, Zendesk enrichment,
patterns historicos, component mapping e gaps detectados.
Voce NAO precisa refazer a coleta das fontes ja cobertas pelo brief.
Foque em: avaliar sinais, aplicar decision matrix, emitir veredicto.

### Dados do Work Item
- **Titulo:** {BUG_TITLE}
- **Descricao:** {BUG_DESCRIPTION}
- **ReproSteps:** {BUG_REPRO_STEPS}
- **Severity:** {BUG_SEVERITY}
- **Area Path:** {area_path}
- **Tags:** {BUG_TAGS}

### Sua Tarefa

Executar triagem usando o N3 Brief como base:
1. Carregar n3_brief.json (modulo, FAQ, Zendesk, patterns, gaps)
2. Validar/complementar sinais se necessario
3. Aplicar decision matrix
4. Emitir veredicto com output estruturado obrigatorio
```

**Passo 2 - Processar veredicto do PM:**

Apresentar o resultado ao usuario:

```markdown
## Fase 1.5 - Triagem PM

### Veredicto: {VEREDICTO}
### Confianca: {X}%

{Resumo da justificativa}

{Sinais coletados - resumo}
```

**Passo 3 - Decisao de fluxo baseada no veredicto:**

- **CONFIRMED_BUG (confianca >= 70%):**
  Prosseguir para Fase 1.6 (Geracao de Cenarios) e depois Fase 2 (Workspace + Branch).
  ```
  Triagem: Bug confirmado ({confianca}%). Gerando cenarios de teste...
  ```

- **NOT_A_BUG (confianca >= 75%):**
  Pular para Fase 7 - Flow B (As Designed).
  Adicionar tag `SUST-IA-CLAUDE-NOT-BUG` ao atualizar ADO.
  ```
  Triagem: Classificado como Not-a-Bug ({confianca}%).

  Sugestao de resposta ao cliente:
  {texto sugerido pelo PM}

  Deseja:
  1. Aceitar e atualizar ADO como Not-a-Bug (tag SUST-IA-CLAUDE-NOT-BUG)
  2. Discordar e prosseguir com correcao
  3. Solicitar mais informacoes
  ```

- **FEATURE_REQUEST (confianca >= 80%):**
  Informar ao usuario e oferecer reclassificacao.
  Se envolver criacao/alteracao de regra de negocio (keywords: "nova regra", "alterar regra", "regra fiscal", "nova legislacao", "nova obrigacao", "configuracao tributaria"), adicionar tag `SUST-IA-CLAUDE-REGRA`.
  ```
  Triagem: Classificado como Feature Request ({confianca}%).

  {Justificativa do PM}

  Deseja:
  1. Reclassificar WI como Feature e encerrar pipeline
  2. Discordar e prosseguir como bug
  3. Solicitar mais informacoes
  ```
  Se opcao 1: atualizar ADO e encerrar. Se opcao 2: continuar pipeline.

- **INCOMPLETE_ANALYSIS (confianca >= 80%):**
  Informar ao usuario e oferecer devolver ao N1/N2.
  Adicionar tag `SUST-IA-CLAUDE-ANALISE` automaticamente (WI precisa de analise adicional).
  ```
  Triagem: Analise incompleta ({confianca}%).

  Itens faltantes:
  {lista do PM}

  Deseja:
  1. Devolver ao N1/N2 com feedback estruturado
  2. Prosseguir mesmo assim (com dados incompletos)
  3. Fornecer informacoes adicionais agora
  ```
  Se opcao 1: atualizar ADO com feedback e encerrar. Se opcao 2: continuar pipeline.

- **DUPLICATE (confianca >= 85%):**
  Informar ao usuario com WI original.
  ```
  Triagem: Possivel duplicata ({confianca}%).

  WI original: #{ORIGINAL_ID}
  Solucao ja aplicada: {resumo}

  Deseja:
  1. Fechar como duplicata referenciando #{ORIGINAL_ID}
  2. Discordar e prosseguir como bug novo
  3. Verificar WI original antes de decidir
  ```
  Se opcao 1: atualizar ADO e encerrar. Se opcao 2: continuar pipeline.

- **NEEDS_INFO:**
  Solicitar informacoes especificas ao usuario.
  Adicionar tag `SUST-IA-CLAUDE-ANALISE` automaticamente (WI precisa de informacoes adicionais).
  ```
  Triagem: Informacoes insuficientes para classificacao.

  O PM precisa das seguintes informacoes:
  {lista de perguntas do PM}

  Por favor, fornecer as informacoes solicitadas.
  ```
  Apos receber informacoes: relancar taxone-pm com dados atualizados.

**Passo 4 - Sub-passo: Consulta Remota (NEEDS_INFO / INCOMPLETE_ANALYSIS)**

Se o PM indicou que faltam **dados do ambiente do cliente** (base de producao/UAT)
e incluiu a secao "Queries Remotas Sugeridas" no output:

1. **Resolver empresa:** Executar `python scripts/empresa_resolver.py --title "{BUG_TITLE}" --description "{BUG_DESCRIPTION}" --tags "{BUG_TAGS}" --format json`
   - Se 0 matches: perguntar empresa ao usuario via `AskUserQuestion`
   - Se 1 match: usar diretamente
   - Se multiplos: apresentar opcoes ao usuario

2. **Validar queries:** Para cada query sugerida pelo PM, verificar que e SELECT puro (sem DML/DDL).

3. **Confirmar com usuario:**
   ```
   O PM sugeriu consultas no ambiente do cliente para obter dados faltantes.

   Empresa: {empresa}
   Ambiente: {env, default UAT}

   Queries a despachar:
   1. {query_1} — Motivo: {motivo_1}
   2. {query_2} — Motivo: {motivo_2}

   Confirma o despacho? (sim/nao/editar)
   ```

4. **Despachar:** Para cada query confirmada:
   ```bash
   python skills/query-executor-prod-uat/scripts/run_query.py \
     --query "{SQL}" --empresa {EMPRESA} --env {ENV}
   ```

5. **Documentar na WI:** PATCH em Custom.Solutions com template do Protocolo de Consulta Remota + tags SUST-IA-CLAUDE + SUST-IA-CLAUDE-ANALISE.

6. **Salvar estado e PAUSAR:** Salvar `tests/{BUG_ID}/pipeline_state.json` (ver Protocolo de Pausa/Retomada) e encerrar pipeline com mensagem:
   ```
   Pipeline PAUSADO - Aguardando resultado da consulta remota.
   O resultado sera enviado por email. Apos receber, re-execute o pipeline
   fornecendo os dados obtidos.
   ```

---

### Fase 1.5.5 - Enriquecer com Datadog (Automatica)

**Objetivo:** Buscar dados reais de APM/logs/traces no Datadog via MCP Server para enriquecer o
contexto de WIs relacionadas a importacao, performance, erros em batch ou job servidor.
Segue padrao fault-tolerant — se MCP indisponivel ou keywords nao detectadas, pular silenciosamente.

**Pre-requisito:** MCP Server `datadog` configurado em `~/.claude.json` (auth via OAuth, sem API Key manual).
Org: `trta-onesource` | Permissao: MCP Read (somente leitura).

**Condicao de Entrada:**

1. Titulo ou descricao do work item contem keywords de performance/importacao
2. MCP Server `datadog` disponivel e autenticado

**Se QUALQUER condicao NAO atendida:** pular silenciosamente para Fase 1.6.

**Keywords de Ativacao (case-insensitive):**

`importa`, `importacao`, `lentidao`, `lento`, `timeout`, `performance`, `demora`, `batch`,
`job servidor`, `erro importacao`, `travou`, `demorado`, `processamento`, `carga`, `SAFX`,
`rejeita`, `desconsidera`, `ignora registros`

**Passo 1 - Detectar se WI e de importacao/performance:**

Verificar se titulo ou descricao contem keywords acima. Extrair tambem **termos de busca**
do titulo/descricao: nome de procedure, codigo SAFX (ex: SAFX311), nome do job, tabela mencionada.

Se nenhuma keyword encontrada: pular para Fase 1.6 silenciosamente.

**Passo 2 - Buscar Logs Recentes:**

Usar MCP tool `search_datadog_logs`:

```
Query:  service:taxone* status:(error OR warn) {termos_extraidos}
Periodo: ultimos 7 dias
Limite: 10 resultados
Ordenar: mais recentes primeiro
```

Extrair de cada log: timestamp, service, status, message (primeiros 200 chars).

Se MCP retornar erro ou vazio: registrar warning e continuar.

**Passo 3 - Buscar APM Traces/Spans:**

Usar MCP tool `search_datadog_spans`:

```
Query:  service:taxone* @duration:>5s {termos_extraidos}
Periodo: ultimos 7 dias
Limite: 5 resultados
Ordenar: maior duracao primeiro
```

Extrair de cada span: resource_name, duration_ms, service, status, error (se houver).

Se MCP retornar erro ou vazio: registrar warning e continuar.

**Passo 4 - Buscar Metricas de Performance:**

Usar MCP tool `get_datadog_metric`:

```
Metricas a buscar:
- avg:trace.servlet.request.duration{service:taxone*}
- p95:trace.servlet.request.duration{service:taxone*}
- sum:trace.servlet.request.errors{service:taxone*}
Periodo: ultimos 7 dias
```

Se MCP retornar erro ou vazio: registrar warning e continuar.

**Passo 5 - Buscar Monitors Relevantes:**

Usar MCP tool `search_datadog_monitors`:

```
Query: taxone OR mastersaf
```

Verificar se ha monitors em estado Alert ou Warn que possam estar relacionados ao problema.

Se MCP retornar erro ou vazio: pular este passo.

**Passo 5.5 - Buscar RUM (Real User Monitoring) — User Journey e Erros de Tela:**

**Condicao:** Executar SEMPRE que a WI envolva interacao com tela (importacao, consulta, erro de tela).
Keywords adicionais de tela: `tela`, `erro na tela`, `nao abre`, `nao carrega`, `branco`, `travou tela`,
`500`, `404`, `click`, `botao`, `salvar`, `gravar`, `consultar`, `campo`, `combo`, `grid`, `nao exibe`,
`desapareceu`, `sumiu`, `frontal`, `interface`, `UI`, `angular`

**IMPORTANTE — Arquitetura RUM do TAX ONE:**
No TAX ONE, os dados de RUM vem **embedados nos APM traces** (`ingestion_reason:rum`), NAO como
eventos RUM separados. Portanto, a fonte primaria e `search_datadog_spans`, nao `search_datadog_rum_events`.

**5.5.1 - Buscar traces RUM (fonte primaria):**

Usar MCP tool `search_datadog_spans`:

```
Query: service:taxone* {termos_extraidos}
Periodo: ultimos 7 dias
Limite: 5 resultados
custom_attributes: ["usr.*", "view.*", "session.*", "application.*", "geo.*"]
```

Os spans RUM do TAX ONE contem dados riquissimos:
- `usr.menuPath` — caminho exato no menu do TAX ONE (ex: "Importação > Importação > Execução")
- `usr.module` — modulo funcional (ex: "Job Servidor")
- `usr.email`, `usr.firmId`, `usr.dbSchema` — identificacao do tenant/usuario
- `view.name` — nome da view formatado (ex: "/taxone/Job Servidor/Importação > Execução")
- `view.url` — URL completa da tela
- `view.referrer` — tela anterior (de onde veio)
- `session.has_replay` — se Session Replay esta disponivel (true/false)
- `http.url` — endpoint backend chamado
- `duration` — tempo total da operacao (ns)
- `geo.*` — localizacao do usuario

**5.5.2 - Buscar RUM events (fonte secundaria, fallback):**

Se spans nao retornarem dados RUM, tentar `search_datadog_rum_events`:

```
Query: @type:error @application.name:*taxone* {termos_extraidos}
Periodo: ultimos 7 dias
detailed_output: true
```

**5.5.3 - Extrair User Journey:**

A partir dos spans RUM, reconstruir a sequencia de navegacao:

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

Este journey alimenta diretamente o `taxone-e2e-tester` para gerar specs Playwright que
reproduzam o caminho exato do cliente.

Se MCP retornar erro ou vazio: registrar warning e continuar.

**Passo 6 - Apresentar Contexto Datadog:**

Exibir bloco formatado:

```
----------------------------------------------------------
  DATADOG (MCP) - Contexto de Performance / Importacao
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

  RUM - ERROS DE TELA ({count}):
  {url} - {error_message} - {error_source}

  RUM - USER JOURNEY (se disponivel):
  1. {url_path} - {action} - {loading_time}ms
  2. {url_path} - ERRO: {error_message}
  (caminho real do cliente, usar para gerar specs Playwright)
----------------------------------------------------------
```

Se nenhum dado relevante encontrado:

```
----------------------------------------------------------
  DATADOG (MCP) - Nenhum dado de performance encontrado
  (Servico taxone* sem logs/traces nos ultimos 7 dias)
----------------------------------------------------------
```

**Passo 7 - Guardar Contexto para Fases Posteriores:**

Variaveis do pipeline:

- `DD_RELEVANT` — `true`/`false` (detectado no Passo 1)
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
- `DD_SIMILAR_FIXES` — fixes anteriores encontrados por busca estrutural (tabelas/procedures/DDLs via `scripts/knowledge_search.py`)

**Knowledge Base RUM** (consultar para enriquecer analise):
- `knowledge/datadog/module-service-map.json` — mapa modulo TAX ONE → service/resource/URLs Datadog
- `knowledge/datadog/known-rum-errors.json` — catalogo de erros RUM conhecidos com causa raiz e acao
- `knowledge/datadog/performance-baselines.json` — baselines P50/P95/P99 por endpoint

**Script auxiliar:** `scripts/rum_enricher.py` — classificacao de relevancia, match de erros, deteccao de anomalias.

Uso nas fases posteriores:
- **Fase 3.7 (DBA):** usa `DD_SLOW_TRACES` para correlacionar performance com queries PL/SQL
- **Fase 4 (Developer):** usa contexto DD para focar otimizacao nos pontos criticos
- **Fase 5 (Review):** valida se a correcao melhora os indicadores detectados
- **Fase 5 (E2E Playwright):** usa `DD_RUM_USER_JOURNEY` para gerar specs que reproduzam o caminho do cliente. Automatizar via `scripts/rum_to_e2e.py --wi-id {BUG_ID}` que cruza RUM journey com `playwright-test-map.json` e gera spec ephemeral.
- **Fase 7 (Relatorio Final):** inclui dados DD no relatorio de conclusao
- **taxone-rum-analyst (deep-dive):** invocar para analise RUM profunda se erros complexos ou anomalias detectadas

**Fault-tolerant:** Se MCP retornar erro em qualquer passo, registrar warning e continuar pipeline normalmente. NUNCA bloquear o pipeline por falha no Datadog.

---

### Fase 1.6 - Geracao de Cenarios de Teste

**Objetivo:** Gerar cenarios de teste estruturados a partir da descricao do WI, alimentando
automaticamente o tester SQL, e2e-tester Playwright e explorer com cenarios pre-definidos.

**Condicao de entrada:** Veredicto do PM = `CONFIRMED_BUG`.

**Nota:** Esta fase e executada pelo PROPRIO taxone-pm como parte do seu output.
O PM ja possui toda a informacao necessaria (titulo, descricao, ReproSteps, modulo,
business rules, WebHelp). A geracao de cenarios e uma secao adicional do output do PM.

**Passo 1 - Verificar que o PM gerou o arquivo:**

O taxone-pm (Fase 1.5), quando veredicto = CONFIRMED_BUG, gera automaticamente
`tests/{BUG_ID}/test_scenarios.json` seguindo a Fase 1.6 documentada no agente.

Verificar que o arquivo foi criado:
```bash
test -f "tests/${BUG_ID}/test_scenarios.json" && echo "OK" || echo "MISSING"
```

Se MISSING: nao bloquear pipeline (backwards-compatible). Registrar aviso:
```
AVISO: test_scenarios.json nao foi gerado pelo PM. Testes serao criados ad-hoc.
```

**Passo 2 - Apresentar resumo ao usuario:**

```markdown
## Fase 1.6 - Cenarios de Teste Gerados

- **Arquivo:** tests/{BUG_ID}/test_scenarios.json
- **Total de cenarios:** {N}
  - Happy path: {X}
  - Negativos: {Y}
  - Edge cases: {Z}
  - Regressao: {W}
- **Tela mapeada:** {mapping_id ou "nenhuma"}
- **Specs E2E:** {N specs ou "nenhum"}

Estes cenarios serao usados como base para scripts SQL (tester),
filtros Playwright (e2e-tester) e navegacao guiada (explorer).
```

---

### Fase 1.7 - Enriquecimento de Cenarios de Teste

**Objetivo:** Enriquecer `test_scenarios.json` com conhecimento de schema, impacto git e recomendacao de suites XML.

**Condicao de entrada:** Fase 1.6 executada (test_scenarios.json existe ou sera criado como esqueleto).

**Passo 1 - Executar test_enricher.py:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/test_enricher.py \
  --wi-id ${BUG_ID} \
  --repo "$TAXONE_DW_REPO" \
  --branch MFS${BUG_ID} \
  --format summary
```

**Passo 2 - Processar resultado:**

O script enriquece automaticamente o `test_scenarios.json` com:
- `sql_hint_enriched` — SQL hints com colunas tipadas, JOINs via FK, WHERE type-safe
- `priority: critical` — Cenarios que tocam tabelas hotspot (historico de bugs)
- `git_impact` — Flag de tabelas diretamente alteradas vs indiretamente impactadas
- `suite_recommendations[]` — Suites XML pontuadas (git diff, table overlap, hotspot, recency)
- Cenarios de regressao adicionais para tabelas indiretamente impactadas

**Passo 3 - Apresentar resumo:**

```markdown
## Fase 1.7 - Cenarios Enriquecidos

- **SQL hints enriquecidos:** {N}
- **Cenarios git impact adicionados:** {N}
- **Cenarios critical (hotspot):** {N}
- **Suites recomendadas:** {N}
  {lista de suites com score}
```

**Nota:** Esta fase e automatica e nao-bloqueante. Se o enricher falhar ou nao houver test_scenarios.json, o pipeline continua normalmente. O enricher cria um esqueleto vazio se o arquivo nao existir.

---

### Fase 1.8 - Scripts Pre-Dev (Cenarios Executaveis para o Dev)

**Objetivo:** Gerar scripts SQL executaveis que o dev pode rodar DURANTE o desenvolvimento para validar progresso (TDD adaptado).

**Condicao de entrada:** `tests/{BUG_ID}/test_scenarios.json` existe COM cenarios (`scenarios` nao vazio).

**Skip automatico:** Se `test_scenarios.json` nao existe, OU `scenarios: []`, OU todos os cenarios tem tipo que impede execucao direta (ex: WI puramente de arquivo magnetico SPED/ECD/EFD). Nesse caso, exibir:
```
## Fase 1.8 - Scripts Pre-Dev (Skip)
Motivo: {cenarios vazios / todos dev_runnable: false / arquivo nao existe}
O dev usara testes manuais na Fase 5.
```

**Passo 1 - Executar test_enricher em modo pre_dev:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/test_enricher.py \
  --wi-id ${BUG_ID} \
  --mode pre_dev \
  --packages "{packages_involved do JSON, separados por virgula}" \
  --tables "{tables_involved do JSON, separados por virgula}" \
  --format summary
```

**Passo 2 - Lancar taxone-tester em modo PRE-DEV:**

Invocar via Agent com `subagent_type="taxone-tester"`:

```
## Modo: PRE-DEV (antes da implementacao)

WI: #{BUG_ID} - {BUG_TITLE}
Cenarios disponiveis: tests/{BUG_ID}/test_scenarios.json

Para cada cenario com priority critical ou high:
1. Expandir sql_hint em sql_pre_dev (SELECT executavel no banco Oracle local V2R010AC)
2. Marcar dev_runnable: true/false conforme criterios do schema v2.0
3. Se o cenario precisa de dados de setup: gerar INSERT statements em setup_data[]
4. Gerar teardown_data[] correspondente
5. Salvar validation_scripts_pre_dev.sql em tests/{BUG_ID}/
6. Atualizar test_scenarios.json com campos sql_pre_dev, setup_data, teardown_data, dev_runnable

TABELAS DISPONIVEIS NO BANCO LOCAL: {tables_involved do test_scenarios.json}
RESTRICAO: sql_pre_dev DEVE ser executavel sem procedures complexas.
Usar SELECT simples com JOINs e CASE WHEN para resultado OK/FALHA.
Consultar schema reference: knowledge/conventions/test-scenarios-schema.md
```

**Passo 3 - Apresentar resumo:**

```markdown
## Fase 1.8 - Scripts Pre-Dev Gerados

- **Arquivo:** tests/{BUG_ID}/validation_scripts_pre_dev.sql
- **Cenarios executaveis (dev_runnable: true):** {N}
- **Cenarios manuais (dev_runnable: false):** {N}
- **Setup de dados necessario:** {Sim/Nao}

> O dev pode executar validation_scripts_pre_dev.sql a qualquer momento
> durante o desenvolvimento para verificar progresso.
```

**Passo 4 - Review Pre-Dev (SOMENTE para risco Alto/Critico):**

Se a WI envolve tabelas em `TABLE_HOTSPOTS.md` com >5 bugs historicos OU packages em `PLSQL_MAP.md` com >50 refs, invocar `taxone-techlead-qa` para review pre-dev:

```
## Review Pre-Dev - WI #{BUG_ID}
Verificar se a matriz de cobertura pre-dev esta adequada.
Cenarios: tests/{BUG_ID}/test_scenarios.json
```

O TL-QA NAO bloqueia nesta fase — apenas identifica gaps e recomenda.

**Nota:** Esta fase e nao-bloqueante. Se o tester falhar na geracao dos scripts, o pipeline continua. O dev pode criar seus proprios scripts durante o desenvolvimento.

---

### Fase 1.9 - SM Allocation Check (OBRIGATORIA)

**Objetivo:** Garantir que o WI tenha Developer e Tester atribuidos ANTES de iniciar o desenvolvimento.

**REGRA:** Esta fase e **OBRIGATORIA**. O pipeline NAO pode prosseguir para a Fase 2 (desenvolvimento) sem `Custom.Developer` E `Custom.Tester` preenchidos.

**Passo 1 - Verificar Custom.Developer e Custom.Tester:**

Verificar se AMBOS os campos `Custom.Developer` e `Custom.Tester` estao preenchidos no WI.

- Se **AMBOS preenchidos**: pular direto para Fase 2. Exibir:
  ```
  ## Fase 1.9 - Alocacao (Skip)
  WI ja tem Developer: {dev} e Tester: {tester}. Mantendo alocacao existente.
  ```
- Se **pelo menos um vazio**: prosseguir com Passo 2. **NAO sobrescrever campo ja preenchido.**

**Passo 2 - Lancar taxone-sm em modo alocacao avulsa:**

Invocar via Agent com `subagent_type="taxone-sm"`:

```
## Alocacao Avulsa - Bug #{BUG_ID}

### Dados do Work Item
- **Titulo:** {BUG_TITLE}
- **Tipo:** Bug
- **Area Path:** {area_path}
- **Tags:** {BUG_TAGS}
- **Severity:** {BUG_SEVERITY}
- **Priority:** {BUG_PRIORITY}

### Tarefa
Executar alocacao avulsa conforme documentado no seu perfil de agente:
1. Carregar TEAM_ROSTER e TEAM_SPECIALIZATIONS
2. Resolver modulo/vertical/tech do WI
3. Calcular score de todos os devs e testers
4. Retornar top 3 devs e top 3 testers com scores e recomendacao final
```

**Passo 3 - Apresentar resultado e confirmar:**

```markdown
## Fase 1.9 - Alocacao SM

O WI #{BUG_ID} nao tem dev/tester atribuido.
O Scrum Master recomenda:

- **Dev:** {nome} (score: {X}) - {motivo}
- **Tester:** {nome} (score: {X}) - {motivo}

Deseja aplicar esta alocacao no ADO?
1. Sim, atribuir dev e tester recomendados
2. Nao, prosseguir sem alocacao
3. Escolher manualmente
```

- Se **opcao 1:** PATCH no ADO para atribuir `System.AssignedTo` ao dev recomendado. Adicionar tag `SUST-IA-CLAUDE`.
- Se **opcao 2:** Prosseguir para Fase 2 sem alteracao.
- Se **opcao 3:** Perguntar nome do dev/tester ao usuario.

**Passo 4 - PATCH no ADO (se aprovado):**

```bash
AUTH=$(printf '%s' ":$ADO_PAT" | base64 -w0)
curl -s -X PATCH \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json-patch+json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{BUG_ID}?api-version=7.1" \
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

### Fase 2 - Verificar Workspace Limpo

**Objetivo:** Garantir que o workspace Git esta limpo antes de criar branch.

**Passo 1 - Verificar status do Git:**

```bash
git status --porcelain
```

- Se a saida for vazia: workspace limpo, prosseguir
- Se houver arquivos modificados/nao-rastreados:
  ```
  AVISO: Workspace nao esta limpo. Arquivos pendentes:
  {lista de arquivos}

  Deseja fazer stash das mudancas e continuar? (sim/nao)
  ```
  - Se `sim`: executar `git stash push -m "taxone-auto-fix: stash antes de #{BUG_ID}"`
  - Se `nao`: abortar pipeline

**Passo 2 - Atualizar branch base:**

```bash
git checkout DEV && git pull origin DEV
```

**Passo 3 - Criar branch de trabalho:**

```
BRANCH_NAME=MFS{BUG_ID}
```

```bash
git checkout -b "$BRANCH_NAME"
```

**Apresentar:**

```markdown
## Fase 2 - Workspace Preparado

- Branch base: main (atualizada)
- Branch de trabalho: {BRANCH_NAME}
- Workspace: limpo
```

---

### Fase 3 - Knowledge + Alinhamento

**Objetivo:** Carregar base de conhecimento embarcada e alinhar contexto com o usuario.

**Passo 1 - Listar knowledge disponivel:**

```bash
find "${CLAUDE_PLUGIN_ROOT}/knowledge/" -name "*.md" -type f
```

**Passo 2 - Carregar knowledge obrigatorio:**

Sempre carregar (se existirem):
1. `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/overview.md` - Visao geral da arquitetura
2. `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/tech-stack.md` - Stack tecnologica
3. `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/patterns.md` - Padroes de codigo
4. `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/code-standards.md` - Padroes de qualidade
5. `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/naming.md` - Convencoes de nomenclatura

Para cada arquivo lido, imprimir:
```
> [Knowledge] Carregando: {nome-do-arquivo} - {descricao}
```

**Passo 3 - Identificar knowledge da feature:**

Analisar o titulo e descricao do bug para identificar qual modulo/feature e afetado.
Buscar em `${CLAUDE_PLUGIN_ROOT}/knowledge/features/` por documentacao relevante.

Se encontrado:
```
> [Knowledge] Carregando: features/{feature}.md - Documentacao da feature {nome}
```

Se NAO encontrado:
```
> [Knowledge] Nenhuma documentacao de feature encontrada para: {modulo identificado}
> Continuando com knowledge de arquitetura e convencoes.
```

**Passo 4 - Perguntar sobre knowledge adicional:**

```
Carreguei o seguinte knowledge do plugin:
- {lista de arquivos carregados}

Existe algum documento adicional, wiki ou contexto que voce gostaria de fornecer
para ajudar na analise deste bug?

Se sim, informe o caminho ou cole o conteudo. Se nao, digite "continuar".
```

Aguardar resposta via `AskUserQuestion`.

**Apresentar:**

```markdown
## Fase 3 - Knowledge Carregado

### Base de Conhecimento
- Arquitetura: {sim/nao}
- Tech Stack: {sim/nao}
- Patterns: {sim/nao}
- Convencoes: {sim/nao}
- Feature especifica: {sim/nao - qual}
- Adicional do usuario: {sim/nao}
```

---

### Fase 3.5 - Buscar Bugs Similares

**Objetivo:** Pesquisar no ADO, na base de solucoes e por objetos estruturais (tabelas, procedures, DDLs) por bugs similares ja resolvidos.

**Passo 0 - Busca estrutural por objetos** (OBRIGATORIO):

Executar busca por tabelas, procedures e colunas identificados na analise (n3_brief.json, component_mapping):

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/knowledge_search.py --wi-context {BUG_ID} --format table
```

Ou equivalente inline:
1. Parse `tests/{BUG_ID}/n3_brief.json` → extrair tabelas (staging + definitive), procedures, key_columns
2. Para cada tabela/procedure: buscar em `knowledge/solutions/*.md` (YAML frontmatter: tables, packages, modules)
3. Buscar patterns em `knowledge/solutions/INDEX.md` (secao "Patterns Recorrentes")
4. Buscar em `knowledge/ado-fixes/_metadata.json` (title, tags, module)
5. Buscar em `tests/*/n3_brief.json` anteriores (component_mapping)

Salvar resultado em **DD_SIMILAR_FIXES** (nova variavel).

**CRITICO**: Se encontrar matches HIGH/MEDIUM, apresentar ANTES de prosseguir com hipoteses — um fix anterior pode revelar a causa raiz diretamente.

**Passo 1 - Extrair termos-chave** do titulo e descricao do bug para busca textual.

**Passo 2 - Buscar no ADO via WIQL:**

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "SELECT [System.Id], [System.Title], [System.State], [System.Tags] FROM workitems WHERE [System.TeamProject] = '\''Mastersaf Fiscal Solutions'\'' AND [System.WorkItemType] = '\''Bug'\'' AND [System.AreaPath] UNDER '\''Mastersaf Fiscal Solutions\\MFS\\TAX ONE\\Suporte'\'' AND [System.State] IN ('\''Resolved'\'', '\''Closed'\'') AND [System.Title] CONTAINS '\''TERMO_CHAVE'\'' ORDER BY [System.ChangedDate] DESC"
  }' \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/wiql?api-version=7.1"
```

**Passo 3 - Buscar na base de solucoes:**

Verificar `${CLAUDE_PLUGIN_ROOT}/knowledge/solutions/` por documentos que mencionem
termos similares ao bug atual (se o diretorio existir).

**Passo 4 - Apresentar resultados consolidados (estrutural + textual):**

```markdown
## Fase 3.5 - Bugs Similares Encontrados

### Busca Estrutural (por tabelas/procedures)
| Relevancia | WI | Titulo | Fonte | Match |
|------------|-----|--------|-------|-------|
| {HIGH/MEDIUM} | {id} | {titulo} | {solutions/ado_metadata/patterns} | {tabela/procedure} |

### Patterns Recorrentes Aplicaveis
- **{Pattern}** (WIs: {refs}) — {descricao}

### Busca Textual (ADO WIQL)
| ID | Titulo | Estado | Tags |
|----|--------|--------|------|
| {id} | {titulo} | {estado} | {tags} |

Deseja que eu carregue os detalhes de algum desses bugs para referencia? (IDs ou "nao")
```

Se NAO encontrou em nenhuma busca:
```markdown
## Fase 3.5 - Nenhum Bug Similar Encontrado

Nao foram encontrados bugs resolvidos similares (estrutural nem textual).
Continuando com analise independente.
```

---

### Fase 3.7 - Analise Critica: Bug Real vs As Designed

**Objetivo:** Antes de investir tempo em implementacao, fazer uma analise critica
para determinar se o comportamento reportado e realmente um bug ou se esta
funcionando conforme projetado (As Designed).

**Esta fase usa o agente `taxone-dba` como analista critico** (equivalente ao
"observador" no LegalOne, mas com expertise Oracle/fiscal).

**Passo 1 - Lancar taxone-dba para analise critica:**

Invocar via Agent com `subagent_type="taxone-dba"`:

```
Analise critica do bug #{BUG_ID}: {BUG_TITLE}

## Descricao do Bug
{BUG_DESCRIPTION}

## Passos de Reproducao
{BUG_REPRO_STEPS}

## Contexto (Knowledge carregado)
{resumo do knowledge relevante}

## Sua Tarefa

Analisar CRITICAMENTE se este e um bug real ou se o sistema esta funcionando
conforme projetado (As Designed). Considere:

1. **Regra fiscal aplicavel:** O calculo/comportamento segue legislacao vigente?
2. **Especificacao do sistema:** O comportamento esta alinhado com o design documentado?
3. **Consistencia:** Outros cenarios similares se comportam da mesma forma?
4. **Dados do usuario:** O cenario do usuario esta configurado corretamente?
5. **Impacto Oracle:** Se for bug, qual o impacto em dados ja processados?

## Formato de Resposta OBRIGATORIO:

### Veredicto
**[BUG REAL]** ou **[AS DESIGNED]** ou **[INCONCLUSIVO - PRECISA MAIS INFORMACAO]**

### Justificativa
[Analise detalhada com evidencias do codigo]

### Se Bug Real:
- Causa raiz provavel: [descricao]
- Packages/procedures afetados: [lista]
- Impacto em dados existentes: [analise]

### Se As Designed:
- Comportamento esperado: [descricao]
- Referencia: [package/procedure/regra que confirma]
- Recomendacao ao usuario: [orientacao]

### Confianca
[0-100] - [justificativa da pontuacao]
```

**Passo 2 - Apresentar veredicto ao usuario:**

```markdown
## Fase 3.7 - Analise Critica (DBA)

### Veredicto: {BUG REAL | AS DESIGNED | INCONCLUSIVO}
{resumo da justificativa}

### Confianca: {score}/100

{Se INCONCLUSIVO:}
O DBA precisa de mais informacoes para determinar. Detalhes:
{lista de informacoes faltantes}

Voce pode fornecer essas informacoes? Ou deseja prosseguir como bug real?
```

**Passo 3 - Decisao de fluxo:**

- **BUG REAL (confianca >= 70):** Prosseguir para Fase 4
- **AS DESIGNED (confianca >= 70):** Pular para Fase 7 - Flow B (As Designed)
- **INCONCLUSIVO ou confianca < 70:** Adicionar tag `SUST-IA-CLAUDE-ANALISE` automaticamente (DBA nao conseguiu determinar se e bug).
  Se a analise identificar necessidade de nova regra fiscal ou alteracao de regra existente, adicionar tambem tag `SUST-IA-CLAUDE-REGRA`.
  Perguntar ao usuario:
  ```
  A analise critica nao foi conclusiva (confianca: {score}/100).

  Opcoes:
  1. Prosseguir com correcao (tratar como bug real)
  2. Marcar como As Designed
  3. Fornecer mais contexto para nova analise
  4. Despachar consulta remota para obter dados do cliente

  O que deseja fazer?
  ```

  **Se opcao 4 (ou se DBA incluiu "Queries Remotas Sugeridas" no output):**
  Executar o mesmo fluxo de Consulta Remota descrito na Fase 1.5 Passo 4,
  usando as queries sugeridas pelo DBA (EXPLAIN PLAN, distribuicao de dados, etc.).
  Documentar na WI, salvar estado e PAUSAR pipeline.

### Fase 3.7.1 - Registrar Causa Raiz (Automatica)

**Objetivo:** Salvar a causa raiz identificada pelo DBA em formato estruturado para alimentar o relatorio semanal de causas raiz.

**Condicao de execucao:** Sempre (apos qualquer veredicto DBA).

**Acao:** Salvar `tests/{BUG_ID}/root_cause_entry.json` com os dados extraidos da analise DBA:

```json
{
  "wi_id": "{BUG_ID}",
  "title": "{WI_TITLE}",
  "analysis_date": "{DATA_HOJE_YYYY-MM-DD}",
  "analyst": "Claude AI",
  "root_cause": {
    "category": "{recompilation_gap|code_bug|performance|config_error|data_quality|design_gap|regression|environment}",
    "summary": "{resumo_1_linha_da_causa_raiz}",
    "detail": "{descricao_detalhada}",
    "originating_change": {
      "type": "{DDL|PR|PATCH|CONFIG|MIGRATION|NONE}",
      "reference": "{referencia_ex_DDL_MFS848597}",
      "wi_id": "{WI_originadora_se_conhecida}",
      "description": "{o_que_a_alteracao_fez}"
    }
  },
  "affected_modules": ["{modulos}"],
  "affected_objects": ["{objetos_plsql_tabelas}"],
  "verdict": "{BUG_CONFIRMED|NOT_A_BUG|NEEDS_INFO|DESIGN_GAP}",
  "solution_type": "{code_fix|recompilation|config_change|ddl|data_fix|no_action}",
  "pattern": "{pattern_recorrente_se_identificado}",
  "pr": null,
  "zendesk": "{TKT_se_existir}"
}
```

**Mapeamento de veredicto DBA → category:**
- BUG REAL (codigo errado) → `code_bug`
- BUG REAL (recompilacao) → `recompilation_gap`
- BUG REAL (performance) → `performance`
- AS DESIGNED → `design_gap`
- INCONCLUSIVO → preencher com melhor estimativa

**Campo `originating_change`:** Extrair do output DBA e da Fase 3.8 (Git History). Se DBA mencionou DDL, PR ou WI como causa, registrar aqui. Se nao identificado, usar `{"type": "NONE"}`.

**Schema de validacao:** `knowledge/root-cause/schema.json`

**Nota:** Esta fase e NAO-BLOQUEANTE. Se falhar a escrita, logar e continuar.

---

### Fase 3.7.2 - Impact Assessment (Automatica)

**Objetivo:** Gerar avaliacao formal de impacto antes da implementacao, com risk score, arquivos afetados, dependencias cross-module e instrucoes de teste.

**Condicao de execucao:** Sempre (apos qualquer veredicto DBA, inclusive AS DESIGNED).

**Acao:** O taxone-architect ja gera o Impact Assessment como parte do seu output (secao 4 do agente). Extrair o JSON estruturado do output e salvar em `tests/{BUG_ID}/impact_assessment.json`.

**Schema:** `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/impact-assessment-schema.json`

**Campos a preencher a partir dos outputs anteriores:**
- `wi_id`: do contexto da WI
- `risk_score`: classificado pelo architect (LOW/MEDIUM/HIGH/CRITICAL)
- `structural`: true se novo modulo, migracao de camada, novo pattern
- `files_affected`: dos outputs DBA + PM (packages_involved, objetos afetados)
- `tables_affected`: do output DBA (tabelas citadas na causa raiz)
- `dependencies_cross_module`: do PLSQL_MAP.md + MODULE_MAP.md
- `test_instructions`: instrucoes derivadas da analise de impacto
- `risks`: riscos identificados pelo architect
- `architect_recommendation`: PROCEED/PROCEED_WITH_CAUTION/NEEDS_REVIEW/BLOCKED

**Decisao de fluxo baseada no Impact Assessment:**
- `architect_recommendation == "BLOCKED"`: PARAR pipeline, reportar ao usuario
- `architect_recommendation == "NEEDS_REVIEW"`: Alertar usuario, prosseguir com cautela
- Demais: prosseguir normalmente

**Nota:** Esta fase e NAO-BLOQUEANTE. Se falhar a geracao, logar e continuar.

---

### Fase 3.7.3 - Formalizar Regras de Negocio Afetadas (Automatica)

**Objetivo:** Identificar e formalizar as regras de negocio EXISTENTES que o bug viola ou que a correcao pode impactar, criando um contrato estruturado (`affected_rules.json`) que alimenta as fases posteriores (4.5 coverage, 5.0 enriquecimento, 5 tester).

**Diferenca do us-implement:** O pipeline de features formaliza regras NOVAS. Aqui identificamos regras EXISTENTES afetadas pelo bug.

**Condicao de execucao:** Veredicto DBA (Fase 3.7) = BUG REAL (qualquer subtipo).

**Auto-Skip Inteligente:**

| Criterio | Acao |
|----------|------|
| 1 arquivo, 1 package, sem cross-module, sem DDL | **SKIP COMPLETO** — gerar versao minima com 1 regra inferida |
| `impact_assessment.risk_score` == LOW | **SKIP COMPLETO** — gerar versao minima |
| 2+ packages OU DDL OU cross-module OU risk HIGH/CRITICAL | **EXECUTAR** architect completo |

Se SKIP: gerar `affected_rules.json` minimo automaticamente (sem invocar architect):
```json
{
  "work_item_id": "{BUG_ID}",
  "title": "{BUG_TITLE}",
  "total_rules_affected": 1,
  "rules": [
    {
      "id": "R01",
      "description": "Regra inferida a partir da causa raiz DBA",
      "source": "inferred_from_root_cause",
      "type": "validation",
      "violation": "{root_cause resumido}",
      "tables_affected": ["{tabelas do DBA}"],
      "packages_affected": ["{packages do DBA}"],
      "testable": true,
      "sql_validation_hint": "{sql_hint do test_scenarios se disponivel}",
      "adjacent_rules": []
    }
  ],
  "affected_modules": ["{modulo}"],
  "cross_module_risks": []
}
```

**Se EXECUTAR — Passo 1 - Lancar taxone-architect para formalizacao de regras:**

Invocar via Agent com `subagent_type="taxone-architect"`:

```
## Formalizacao de Regras de Negocio Afetadas - Bug #{BUG_ID}

### MODO: FORMALIZACAO DE REGRAS AFETADAS (NAO design de solucao — isso ja foi feito na 3.7)

### Dados do Work Item
- **Titulo:** {BUG_TITLE}
- **Descricao:** {BUG_DESCRIPTION}
- **Repro Steps:** {REPRO_STEPS}

### Causa Raiz (DBA - Fase 3.7)
{root_cause_resumo}

### Impact Assessment (Fase 3.7.2)
{impact_assessment resumido — risk_score, files_affected, tables_affected, dependencies_cross_module}

### Knowledge Carregado (Fase 3)
{lista de features/modulos carregados}

### Sua Tarefa

Identificar TODAS as regras de negocio EXISTENTES afetadas pelo bug:

1. **Identificar regra violada:** Qual regra de negocio este bug viola?
   - Consultar `knowledge/business-rules/{module}/` para regras documentadas
   - Se nao ha regra documentada, formalizar a partir do comportamento esperado
2. **Classificar tipo:** calculation | validation | flow | configuration | integration
3. **Consultar schema:** `knowledge/schema/` para tabelas afetadas
4. **Consultar PLSQL_MAP.md:** packages/procedures envolvidos
5. **Definir testabilidade:** Para cada regra, sql_validation_hint (esperado vs actual)
6. **Regras adjacentes:** Quais outras regras podem ser impactadas pela correcao?
   - Consultar MODULE_MAP.md para cross-module
   - Consultar TABLE_HOTSPOTS.md para tabelas de risco

### Output OBRIGATORIO

Criar arquivo `tests/{BUG_ID}/affected_rules.json` com:

{
  "work_item_id": "{BUG_ID}",
  "title": "{BUG_TITLE}",
  "total_rules_affected": N,
  "rules": [
    {
      "id": "R01",
      "description": "descricao da regra existente violada",
      "source": "knowledge/business-rules/{module}/{file}.md OU inferred",
      "type": "calculation|validation|flow|configuration|integration",
      "violation": "como o bug viola esta regra",
      "tables_affected": ["SAFX07", "X07"],
      "packages_affected": ["PKG_EXAMPLE"],
      "testable": true,
      "sql_validation_hint": "SELECT ... WHERE ... -- esperado vs actual",
      "adjacent_rules": ["R02 - pode ser impactada pela correcao"]
    }
  ],
  "affected_modules": ["ICMS"],
  "cross_module_risks": [
    {"from_module": "ICMS", "to_module": "SPED", "risk": "descricao do risco"}
  ]
}

IMPORTANTE: Cada regra DEVE ter `testable: true|false` e `sql_validation_hint` para guiar o tester e o coverage.
```

**Passo 2 - Validar e Apresentar Resultado:**

Verificar que `affected_rules.json` foi criado:
```bash
test -f "tests/${BUG_ID}/affected_rules.json" && echo "OK" || echo "MISSING"
```

Apresentar ao usuario:

```markdown
## Fase 3.7.3 - Regras de Negocio Afetadas

- **Total de regras afetadas:** {N}
- **Modulos afetados:** {lista}
- **Riscos cross-module:** {N}

### Regras
| ID  | Tipo          | Violacao (resumo)              | Testavel | Tabelas       |
|-----|---------------|--------------------------------|----------|---------------|
| R01 | calculation   | {como o bug viola a regra}     | Sim      | SAFX07, X07   |
| R02 | validation    | {como o bug viola a regra}     | Sim      | EST_APURACAO   |
...

Estas regras serao usadas como contrato para:
- Coverage da correcao (Fase 4.5)
- Enriquecimento de cenarios de teste (Fase 5.0)
- Scripts de validacao (Fase 5)
```

**Nota:** Esta fase e NAO-BLOQUEANTE. Se falhar, logar e continuar — o pipeline funciona sem affected_rules.json (modo legado).

---

### Fase 3.8 - Analise de Historico Git (Automatica)

**Objetivo:** Identificar qual commit/PR introduziu o bug, cruzando objetos afetados com o historico git do `taxone_dw`.

**Condicao de execucao:** Veredicto DBA = BUG REAL (qualquer subtipo).

**Passo 1 - Coletar objetos afetados:**

Extrair dos outputs anteriores:
- PM (Fase 1): packages mencionados no titulo/descricao
- DBA (Fase 3.7): objetos citados na causa raiz (`packages_involved`, objetos afetados)
- Combinar em lista unica, deduplicar

**Passo 2 - Executar git_history_analyzer:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/git_history_analyzer.py \
  --repo "$TAXONE_DW_REPO" \
  --objects "{LISTA_OBJETOS_CSV}" \
  --timeframe 90 \
  --wi-title "{WI_TITLE}" \
  --wi-date "{WI_CREATED_DATE}" \
  --format json
```

**Passo 3 - Processar resultado:**

- Se `status == "ok"` e `top_suspects` nao vazio:
  - Guardar `top_suspects` para enriquecer prompt do developer (Fase 4)
  - Gerar versao HTML: re-executar com `--format html`
- Se `status == "no_files_found"` ou `"no_commits_found"`:
  - Registrar no log, continuar sem bloquear

**Passo 4 - Postar na WI:**

Se houver suspects, postar Discussion comment na WI via API REST:
```
POST {ADO_ORG}/{ADO_PROJECT}/_apis/wit/workitems/{WI_ID}/comments?api-version=7.1-preview.4
```
Com o HTML gerado no passo anterior, prefixado com:
`<h3>🔍 Git History Analysis (Automated)</h3>`

**Passo 5 - Enriquecer contexto do developer:**

Adicionar ao prompt da Fase 4:
```
## Historico Git (commits suspeitos)
Os seguintes commits alteraram os objetos afetados recentemente:
{top_suspects formatado como lista}
Considerar estas alteracoes como possiveis causas raiz.
```

**Nota:** Esta fase e NAO-BLOQUEANTE. Se o analyzer falhar ou nao encontrar dados, o pipeline continua normalmente para a Fase 3.9.

---

### Fase 3.9 - Capturar Baseline RC

**Objetivo:** Obter a versao estavel (RC) dos arquivos que serao modificados, garantindo que o developer trabalhe sobre codigo de producao e nao sobre alteracoes nao testadas em DEV.

**Condicao de execucao:** Sempre que houver arquivos identificados para modificacao (do DBA ou Git History).

**Passo 1 - Coletar arquivos afetados:**

Extrair dos outputs anteriores:
- DBA (Fase 3.7): `packages_involved`, objetos afetados na causa raiz
- Git History (Fase 3.8): `top_suspects` — arquivos dos commits suspeitos
- PM (Fase 1): packages mencionados no titulo/descricao
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
- Se HA divergencias: incluir `RC_BASELINE_CONTEXT` no prompt da Fase 4

**Nota:** Esta fase e NAO-BLOQUEANTE. Se o branch RC nao existir ou o comando falhar, registrar aviso e continuar normalmente para a Fase 4.

---

### Fase 4 - Explorar + Diagnosticar + Corrigir

**Objetivo:** Lancar o agente de implementacao especializado (`taxone-plsql` / `taxone-pb` / `taxone-java`) para explorar o codigo,
diagnosticar a causa raiz e implementar a correcao.

**Passo 1 - Preparar contexto para o developer:**

Compilar todas as informacoes coletadas ate aqui:
- Dados do bug (titulo, descricao, repro steps)
- Knowledge carregado (resumo)
- Analise critica do DBA (veredicto + causa raiz provavel)
- Bugs similares (se encontrados)
- Informacoes adicionais do usuario (se fornecidas)

**Passo 2 - Selecionar e lancar agente de implementacao:**

**Regra de selecao — Detectar linguagem pelo output do DBA/architect:**

| Sinal no Diagnostico | Agente |
|------------------------|--------|
| Packages PL/SQL (.sql, PKG_, PRC_, FNC_, TRG_, VW_), procedures, functions, triggers, views | `taxone-plsql` |
| DataWindows (.srd, .srw, .srf, .sru), user objects, scripts PB | `taxone-pb` |
| Classes Java (.java, .jrxml), servlets, web services, Jasper | `taxone-java` |
| Componentes Angular (.ts, .html, .scss, @libs/) | `taxone-angular` |

- Se o bug envolve **frontend Angular**: lancar `taxone-angular`
- Se o bug envolve **backend PL/SQL**: lancar `taxone-plsql`
- Se o bug envolve **backend PowerBuilder**: lancar `taxone-pb`
- Se o bug envolve **backend Java**: lancar `taxone-java`
- Se o bug envolve **multiplas linguagens**:
  - PL/SQL + PB: lancar `taxone-plsql` PRIMEIRO (DDL/packages), depois `taxone-pb` (tela)
  - PL/SQL + Java: lancar em PARALELO (independentes)
  - Qualquer combo + Angular: Angular em PARALELO (repo separado)

Para **PL/SQL**, invocar via Agent com `subagent_type="taxone-plsql"`.
Para **PowerBuilder**, invocar via Agent com `subagent_type="taxone-pb"`.
Para **Java**, invocar via Agent com `subagent_type="taxone-java"`.
Para **frontend Angular**, invocar via Agent com `subagent_type="taxone-angular"`.

Prompt (adaptar conforme backend ou frontend):

```
## Bug #{BUG_ID}: {BUG_TITLE}

### Descricao
{BUG_DESCRIPTION}

### Passos de Reproducao
{BUG_REPRO_STEPS}

### Analise do DBA
{ANALISE_DBA - veredicto, causa raiz provavel, packages afetados}

### Knowledge Relevante
{RESUMO_KNOWLEDGE}

### Bugs Similares (se houver)
{BUGS_SIMILARES}

### RC Baseline (Codigo Estavel de Referencia)
{RC_BASELINE_CONTEXT — incluir SOMENTE se ha divergencias RC vs DEV (Fase 3.9)}

**INSTRUCAO:** Se RC baseline fornecido acima, RESTAURAR a versao RC de cada arquivo
divergente ANTES de aplicar a correcao:
```
git show RC:"path/to/file" > "path/to/file"
```
Corrigir em cima da versao RC (producao estavel), NAO da versao DEV.
Arquivos marcados como "identico RC==DEV" nao precisam de restauracao.
Arquivos marcados como "NOVO_DEV" devem ser trabalhados normalmente.

### Sua Tarefa

1. **Carregar knowledge** da feature (OBRIGATORIO - primeiro passo)
2. **Restaurar baseline RC** dos arquivos divergentes (se RC Baseline fornecido acima)
3. **Explorar** o codigo nos packages/procedures indicados pelo DBA
4. **Diagnosticar** a causa raiz exata (arquivo:linha)
5. **Implementar** a correcao seguindo os padroes do projeto
6. **Reportar** no formato padrao (root cause, arquivos modificados, notas)

### Restricoes
- Alterar SOMENTE o minimo necessario para corrigir o bug
- NAO refatorar codigo adjacente
- Seguir naming conventions e patterns existentes
- Documentar em portugues
- Se a correcao envolver DDL (ALTER TABLE, CREATE INDEX), gerar scripts separados
```

**Passo 3 - Receber relatorio do developer.**

**Passo 4 - Apresentar ao usuario:**

```markdown
## Fase 4 - Diagnostico e Correcao

### Root Cause
{causa raiz identificada pelo developer}

### Arquivos Modificados
{lista de arquivos com descricao das mudancas}

### Scripts DDL (se aplicavel)
{scripts de DDL gerados}

### Notas do Developer
{observacoes relevantes}
```

Se o developer NAO conseguiu corrigir:

```markdown
## Fase 4 - Diagnostico Inconclusivo

O developer nao conseguiu identificar/corrigir o problema.

### Motivo
{descricao do impedimento}

### Informacoes Adicionais Necessarias
{o que falta}

Opcoes:
1. Fornecer mais contexto e tentar novamente
2. Abortar pipeline e tratar manualmente
3. Marcar como necessita investigacao adicional no ADO
4. Despachar consulta remota para obter dados do cliente
```

**Se opcao 4 (ou se developer incluiu "Queries Remotas Sugeridas" no output):**
Executar o mesmo fluxo de Consulta Remota descrito na Fase 1.5 Passo 4,
usando as queries sugeridas pelo developer (dados para reproducao, configuracoes, etc.).
Documentar na WI, salvar estado e PAUSAR pipeline.

---

### Fase 4.5 - Analise de Impacto e Cobertura de Regras

**Objetivo:** Verificar se a correcao implementada (1) nao quebra regras de negocio downstream
e (2) resolve TODAS as regras violadas documentadas em `affected_rules.json`.

**Gate Estrutural (quando invocar architect):**

| Criterio | Acao |
|----------|------|
| 1 arquivo, 1 package, sem DDL, sem cross-module, sem affected_rules.json | **SKIP** architect — bug simples, prosseguir direto |
| `affected_rules.json` existe (Fase 3.7.3 executou) | **INVOCAR** architect (coverage obrigatorio) |
| Alteracao de JOINs, NVL/COALESCE, validacoes, PK/FK | **INVOCAR** architect |
| 2+ packages afetados | **INVOCAR** architect |
| DDL necessario | **INVOCAR** architect |
| Cross-module (packages de modulos diferentes no MODULE_MAP.md) | **INVOCAR** architect |
| `impact_assessment.risk_score` da Fase 3.7.2 == "HIGH" ou "CRITICAL" | **INVOCAR** architect |

**Se SKIP:** Registrar no log: "Fase 4.5 SKIP — bug simples (1 package, sem DDL, sem cross-module, sem affected_rules)". Prosseguir para Fase 5.

**Se INVOCAR:** Executar normalmente:

**Passo 1 - Lancar taxone-architect para analise de impacto + coverage:**

Invocar via Agent com `subagent_type="taxone-architect"`:

```
## Analise de Impacto e Cobertura de Regras - Bug #{BUG_ID}

### Correcao Implementada
{descricao da correcao feita pelo developer - arquivos, linhas, tipo de mudanca}

### Regras de Negocio Afetadas (affected_rules.json)
{conteudo completo do affected_rules.json se existir, OU "Nenhum affected_rules.json disponivel — executar apenas analise de impacto"}

### Sua Tarefa

#### Parte A - Analise de Impacto (SEMPRE executar)

Analisar o IMPACTO da correcao nas regras de negocio do sistema:

1. **Rastrear fluxo downstream:** Quem consome os dados alterados?
   - TMP tables → Java REST API → telas web
   - Procedures → exports/relatorios
   - Triggers → cascata
   - Views/MVs → consultas

2. **Verificar constraints e validacoes:**
   - NOT NULL, CHECK, FK nas tabelas destino
   - Validacoes em procedures/packages dependentes
   - Validacoes na camada Java (entity annotations)

3. **Mapear valores default/NVL introduzidos:**
   - Se NVL(campo, ' '): verificar se ' ' nao quebra validacoes downstream
   - Se NVL(campo, 0): verificar se 0 nao altera calculos fiscais

4. **Verificar funcoes irmas:**
   - Funcoes com mesmo padrao que tambem precisam da correcao

5. **Enriquecer cenarios de teste (se existirem):**
   - Ler `tests/{BUG_ID}/test_scenarios.json` se existir
   - Gerar enrichments para funcoes irmas, data integrity downstream, performance
   - Incluir JSON dos enrichments no output (secao 3.5 do taxone-architect)

#### Parte B - Verificacao de Cobertura (SOMENTE se affected_rules.json disponivel)

Para CADA regra em affected_rules.json:
1. Verificar se a correcao RESOLVE a violacao descrita na regra
2. Verificar se a implementacao esta correta conforme o `sql_validation_hint`
3. Verificar se regras adjacentes nao foram quebradas
4. Marcar como: FIXED / STILL_BROKEN / NEW_RISK / NOT_APPLICABLE

### Output Estruturado OBRIGATORIO (Parte B)

Se affected_rules.json disponivel, incluir no output:

{
  "verdict": "GO|NO-GO",
  "total_rules_affected": N,
  "rules_fixed": N,
  "rules_still_broken": N,
  "rules_new_risk": N,
  "coverage_pct": 85,
  "rules_status": [
    {"id": "R01", "status": "FIXED", "location": "pkg_example.sql:45", "notes": ""},
    {"id": "R02", "status": "STILL_BROKEN", "location": "", "notes": "nao corrigido pelo developer"}
  ],
  "sibling_functions_covered": true
}

Decisao GO/NO-GO (adaptado para bug fix):
- GO: Todas regras FIXED + funcoes irmas corrigidas (coverage 100%)
- GO com ressalvas: coverage >= 80% + parciais aceitaveis
- NO-GO: regra critica STILL_BROKEN ou NEW_RISK identificado

### Formato de Resposta OBRIGATORIO (Parte A):
{usar template da secao 3 do taxone-architect, incluindo secao 3.5 de enriquecimento}
```

**Passo 2 - Avaliar resultado (impacto):**

- **GO:** Prosseguir para Fase 5 (Review + Testes)
- **NO-GO:** Apresentar ao usuario os pontos de impacto identificados:
  ```
  A analise de impacto identificou os seguintes riscos:
  {lista de riscos}

  Opcoes:
  1. Ajustar a correcao (voltar para Fase 4 com feedback)
  2. Prosseguir mesmo assim (aceitar riscos)
  3. Abortar pipeline

  O que deseja fazer?
  ```

**Passo 2b - Avaliar resultado (coverage, se affected_rules.json disponivel):**

- **GO (coverage 100%):** Prosseguir.
- **GO com ressalvas (coverage >= 80%):** Apresentar regras parciais, perguntar ao usuario.
- **NO-GO (coverage < 80% ou regra critica STILL_BROKEN):** Apresentar regras nao corrigidas:
  ```
  A verificacao de cobertura identificou regras NAO corrigidas:
  {tabela de regras com status STILL_BROKEN/NEW_RISK}

  Coverage: {coverage_pct}%

  Opcoes:
  1. Voltar para Fase 4 (developer corrige regras faltantes)
  2. Aceitar com riscos
  3. Abortar pipeline
  ```

Salvar resultado em `tests/{BUG_ID}/rules_coverage.json`.

**Passo 3 - Se funcoes irmas foram identificadas:**

Perguntar ao usuario:
```
A analise identificou funcoes com o mesmo padrao que tambem precisam de correcao:
{lista de funcoes irmas}

Deseja aplicar a mesma correcao nessas funcoes? (sim/nao)
```

Se `sim`: voltar para Fase 4 com as funcoes adicionais como input.

**Apresentar:**

```markdown
## Fase 4.5 - Analise de Impacto e Cobertura de Regras

### Decisao Impacto: {GO / NO-GO}
### Fluxo Downstream: {N pontos analisados}
### Constraints Afetadas: {N - nenhuma quebra / lista de problemas}
### Valores Default: {seguros / lista de riscos}
### Funcoes Irmas: {N identificadas - correcao aplicada: sim/nao}
### Coverage de Regras: {coverage_pct}% ({rules_fixed}/{total_rules_affected})
### Regras ainda quebradas: {lista ou "nenhuma"}
### Tags Aplicadas: {lista de tags adicionadas nesta fase, se houver}
```

**Passo 4 - Aplicar enrichments do architect (se houver):**

Se o architect incluiu enrichments no output (secao "Enriquecimento de Cenarios de Teste"):

1. Ler `tests/{BUG_ID}/test_scenarios.json` existente
2. Fazer parse do JSON
3. Append os enrichments do architect ao array `enrichments[]`
4. Salvar o JSON atualizado (Write tool)

Se o architect nao incluiu enrichments ou o arquivo nao existe: pular silenciosamente.

**Passo 5 - Tags automaticas de Regras de Negocio:**

Se o architect identificar que a correcao requer **nova regra de negocio** ou **alteracao de regra existente**
(keywords: "nova regra", "alterar regra", "regra fiscal", "nova legislacao", "nova obrigacao", "configuracao tributaria"),
adicionar automaticamente a tag `SUST-IA-CLAUDE-REGRA` ao work item no ADO.

---

### Fase 5.0 - Enriquecimento Pre-Test com Regras Afetadas

**Objetivo:** Cruzar `affected_rules.json` (Fase 3.7.3) com `test_scenarios.json` (Fase 1.6/1.7) para garantir que TODA regra testavel tenha pelo menos um cenario de teste e um script SQL executavel. Alimenta a Fase 5 (tester) com cenarios mais completos.

**Condicao de entrada:** `affected_rules.json` existe em `tests/{BUG_ID}/`.

**Auto-Skip:** Se `affected_rules.json` nao existe (Fase 3.7.3 nao executou ou fez skip), pular silenciosamente:
```
Fase 5.0 SKIP — affected_rules.json nao disponivel (modo legado).
```

**Passo 1 - Cruzar regras com cenarios existentes:**

1. Ler `tests/{BUG_ID}/affected_rules.json`
2. Ler `tests/{BUG_ID}/test_scenarios.json` (se existir)
3. Para CADA regra com `testable: true`:
   a. Verificar se existe cenario em `test_scenarios.json` que cobre esta regra
   b. Se NAO existe: gerar cenario automaticamente a partir de:
      - `sql_validation_hint` da regra
      - `tables_affected` e `packages_affected`
      - Tipo: `regression` (verificar que a regra continua funcionando apos a correcao)
   c. Se EXISTE: enriquecer cenario com `sql_validation_hint` da regra (se mais preciso)

**Passo 2 - Gerar scripts SQL adicionais:**

Para cada cenario novo gerado no Passo 1:
1. Expandir `sql_validation_hint` em SQL executavel (banco Oracle local V2R010AC)
2. Marcar `dev_runnable: true`
3. Adicionar ao `validation_scripts_pre_dev.sql` (append, nao sobrescrever)

**Passo 3 - Atualizar test_scenarios.json:**

1. Append novos cenarios ao array `scenarios[]`
2. Adicionar campo `source: "affected_rules_enrichment"` nos cenarios gerados
3. Salvar JSON atualizado

**Passo 4 - Apresentar resumo:**

```markdown
## Fase 5.0 - Enriquecimento Pre-Test com Regras

- **Regras testaveis:** {N} (de {total} em affected_rules.json)
- **Cenarios ja existentes:** {N}
- **Cenarios novos gerados:** {N}
- **Scripts SQL adicionados:** {N}
- **Cobertura de regras por cenarios:** {pct}%

| Regra | Cenario | Status |
|-------|---------|--------|
| R01   | TC03    | Existente |
| R02   | TC07    | Novo (gerado) |
| R03   | —       | Nao testavel |
```

**Nota:** Esta fase e NAO-BLOQUEANTE. Se falhar, logar e continuar — o tester na Fase 5 opera normalmente com os cenarios disponiveis.

---

### Fase 5 - Review + Scripts de Validacao

**Objetivo:** Revisar o codigo implementado e gerar scripts de validacao SQL.

Esta fase lanca **dois agentes em sequencia**:
1. `taxone-plsql-reviewer` / `taxone-pb-reviewer` / `taxone-java-reviewer` - Code review (conforme linguagem)
2. `taxone-tester` - Scripts SQL de validacao + roteiro manual

#### Passo 1 - Lancar reviewer(s)

**Regra de selecao — Reviewer especializado por linguagem:**
- Se houve alteracoes **PL/SQL**: lancar `taxone-plsql-reviewer`
- Se houve alteracoes **PowerBuilder**: lancar `taxone-pb-reviewer`
- Se houve alteracoes **Java**: lancar `taxone-java-reviewer`
- Se houve alteracoes **frontend Angular**: lancar `taxone-angular` (modo review)
- Se houve alteracoes em **multiplas linguagens**: lancar os reviewers correspondentes **em paralelo**

Para review **PL/SQL**, invocar via Agent com `subagent_type="taxone-plsql-reviewer"`.
Para review **PowerBuilder**, invocar via Agent com `subagent_type="taxone-pb-reviewer"`.
Para review **Java**, invocar via Agent com `subagent_type="taxone-java-reviewer"`.
Para review **frontend Angular**, invocar via Agent com `subagent_type="taxone-angular"` com prompt de review.

Para review backend, invocar via Agent com o reviewer especializado correspondente:

```
## Code Review - Bug #{BUG_ID}: {BUG_TITLE}

### Contexto
{resumo do bug e da correcao implementada}

### Arquivos para Revisar
{lista de arquivos modificados pelo developer}

### Sua Tarefa

Revisar TODOS os arquivos modificados seguindo o processo padrao:
1. Carregar knowledge de convencoes (OBRIGATORIO)
2. Analisar seguranca PL/SQL (SQL injection, grants, exposicao de dados)
3. Analisar qualidade (excecoes, cursores, transacoes)
4. Analisar performance Oracle (full scans, queries em loop, indices)
5. Validar convencoes do projeto (naming, formatacao, comentarios)
6. Pontuar confianca (reportar APENAS issues >= 75)
7. Entregar veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO
```

**Passo 2 - Processar resultado do review:**

- **APROVADO:** Prosseguir para tester
- **APROVADO COM RESSALVAS:** Apresentar ressalvas ao usuario e perguntar se deseja corrigir antes
- **REPROVADO:**
  - Apresentar issues criticas ao usuario
  - Incrementar contador de loops de review em `workflow_state.json`
  - Se loop < 3: voltar para Fase 4 com as issues como input adicional
  - Se loop >= 3: escalar para TechLead (taxone-techlead-dev) — pipeline excedeu tentativas de correcao

#### Passo 3 - Lancar taxone-tester

Invocar via Agent com `subagent_type="taxone-tester"`:

```
## Scripts de Validacao - Bug #{BUG_ID}: {BUG_TITLE}

### Contexto
{resumo do bug e da correcao implementada}

### Arquivos Modificados
{lista de arquivos}

### Root Cause
{causa raiz identificada}

### Cenarios Pre-Gerados
{Se tests/{BUG_ID}/test_scenarios.json existir:}
Cenarios de teste pre-gerados disponiveis em: tests/{BUG_ID}/test_scenarios.json
Use-os como esqueleto (sql_hint → query completa, preconditions → setup de dados).
{Se NAO existir:}
Nenhum cenario pre-gerado disponivel. Criar cenarios ad-hoc.

### Sua Tarefa

Criar scripts de validacao SQL e roteiro de teste manual:

0. **Ler cenarios pre-gerados** em `tests/{BUG_ID}/test_scenarios.json` (se existir)
   - Usar sql_hint como base para queries de validacao
   - Usar type/preconditions/expected_result como esqueleto
1. **Carregar knowledge** da feature (OBRIGATORIO)
2. **Scripts SQL de validacao:**
   - Cenario do bug (reproducao do problema ANTES da correcao)
   - Cenario corrigido (validacao DEPOIS da correcao)
   - Cenarios de regressao (garantir que nada mais quebrou)
   - Edge cases (valores limite, nulos, zeros)
   - {Se cenarios pre-gerados: expandir TODOS os sql_hints em queries completas}
3. **Roteiro de teste manual** (se envolver telas PowerBuilder)
4. **Script de dados de teste** (se necessario)
5. **Script de rollback** dos dados de teste

### Formato
Seguir os templates padrao do taxone-tester.
Salvar scripts no repositorio se o reviewer aprovou.
```

**Passo 4 - Apresentar resultado consolidado:**

```markdown
## Fase 5 - Review + Testes

### Code Review
- Veredicto: {APROVADO/RESSALVAS/REPROVADO}
- Issues criticas: {N}
- Issues importantes: {N}

### Scripts de Validacao
- Scripts SQL: {lista com N cenarios cada}
- Roteiro manual: {sim/nao - N cenarios}
- Dados de teste: {sim/nao}

### Proximos Passos
**REGRA CRITICA: SEMPRE prosseguir com testes automaticamente apos implementacao e PR, sem perguntar ao usuario.** O fluxo completo de testes (compilacao, validacao SQL, SuiteAutomation, evidencias em tests/{BUG_ID}/, upload de attachments na WI do ADO, Discussion comment com resultados, e criacao de Tasks QA) e parte integral e obrigatoria do pipeline. NUNCA parar para perguntar "quer que eu prossiga com testes?".

**REGRAS SuiteAutomation:**
1. **SEMPRE sincronizar repo QA antes de criar cenarios:** Atualizar `taxone_automacao_qa` (`git fetch origin` + `origin/rc`) e verificar cobertura existente antes de criar XMLs/flat files novos.
2. **SEMPRE sincronizar XML e esperados do repo QA antes de rodar:** Copiar de `origin/rc` via `git show`. Paths repo QA: `arquivos/` (minusculo), local: `Arquivos/` (maiusculo).
3. **Se suite_runner reporta ERROR(0s):** Rodar JAR diretamente: `cd suite-automation/jar && java -Dfile.encoding=Cp1252 -Dsun.jnu.encoding=ISO-8859-1 -jar SuiteTeste.jar "<xml_sem_drive>" "RA<range>" 'PRO"<title>"' "../config/suiteteste_LOCAL.properties"`
```

---

### Fase 5.5 - Coverage Report (Gate GO/NO-GO)

**Objetivo:** Gerar relatorio de cobertura de testes e aplicar gate de qualidade antes de commit/PR.

**Condicao de entrada:** Fase 5 concluida (tester gerou scripts e evidencias em `tests/{BUG_ID}/`).

**Passo 1 - Executar test_coverage_reporter.py:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/test_coverage_reporter.py \
  --wi-id ${BUG_ID} \
  --tests-dir tests/${BUG_ID}/ \
  --repo "C:/@@Dev/Git/taxone_dw" \
  --branch MFS${BUG_ID} \
  --format markdown
```

**Passo 2 - Avaliar veredicto:**

- **GO:** Todos cenarios critical/high cobertos + procedures exercitadas. Prosseguir para Fase 6.
- **CONDITIONAL GO:** >=80% critical/high cobertos, gaps em medium/low. Apresentar warning:
  ```
  ## Fase 5.5 - Coverage Report: CONDITIONAL GO ⚠️

  Gaps identificados:
  {tabelas/procedures sem teste}

  Deseja:
  1. Prosseguir com commit/PR (aceitar gaps)
  2. Executar testes adicionais para cobrir gaps
  3. Abortar pipeline
  ```
- **NO-GO:** Cenario critical sem evidencia ou >50% procedures sem teste. Apresentar bloqueio:
  ```
  ## Fase 5.5 - Coverage Report: NO-GO ❌

  Motivos:
  {lista de motivos}

  Gaps criticos:
  {tabelas/procedures sem teste}

  Deseja:
  1. Voltar para Fase 5 (executar testes faltantes)
  2. Forcar prosseguimento (override manual)
  3. Abortar pipeline
  ```

**Passo 3 - Salvar e documentar:**

- Salvar `tests/{BUG_ID}/coverage_report.json` (automatico pelo script)
- Salvar `tests/{BUG_ID}/coverage_report.md` (automatico no formato markdown)
- Incluir coverage report no Discussion comment da WI (junto com evidencias)
- O coverage report e anexado como Attachment na WI

**Nota:** O coverage report considera todas as dimensoes: cenarios planejados vs executados,
tabelas impactadas vs testadas, procedures alteradas vs exercitadas, e sugestoes de developers.

---

### Fase 5.9 - Compliance Check (Gate GO/NO-GO)

**Objetivo:** Verificar seguranca e compliance do codigo alterado antes de criar PR.
Inspirado no Step 5 (Compliance, Code Review) do TaxPillot-Patagonia.

**Condicao de entrada:** Fase 5 concluida (review feito, testes executados).

**Passo 1 - Lancar taxone-compliance:**

```
Agent(subagent_type="taxone-compliance")
```

Prompt:
```
Verificar compliance dos arquivos alterados na WI #{BUG_ID}.

Arquivos modificados:
{LISTA_ARQUIVOS_MODIFICADOS}

Repositorio: {TAXONE_DW_REPO}
Branch: MFS{BUG_ID}
```

**Passo 2 - Processar resultado:**

O agente retorna `compliance_report.json`. Salvar em `tests/{BUG_ID}/compliance_report.json`.

**Passo 3 - Decisao de fluxo:**

- **PASS:** Prosseguir para Fase 5.8 (SAFX) e depois Fase 6 (PR)
- **PASS_WITH_WARNINGS:** Alertar usuario sobre findings HIGH. Prosseguir se usuario confirmar.
- **FAIL:** **BLOQUEAR PR.** Apresentar findings CRITICAL ao usuario:
  ```
  COMPLIANCE FAIL: {N} finding(s) critico(s) encontrado(s).

  {lista de findings com file:line e recomendacao}

  O developer deve corrigir antes de prosseguir.
  ```
  - Voltar ao developer (Fase 4) com instrucoes de correcao do compliance
  - Incrementar contador de loops em `workflow_state.json`
  - Se loop >= 3: escalar para TechLead (taxone-techlead-dev)

**Nota:** Findings pre-existentes (codigo que ja estava assim antes da WI) tem severidade rebaixada e NAO bloqueiam.

---

### Fase 5.8 - Geracao de Dados SAFX (Auto-detect)

**Objetivo:** Gerar flat-files SAFX de teste para importacao em outros ambientes (QA/RC).
Quando nao existe cenario SuiteAutomation para o componente, SAFX e gerada automaticamente.

**Passo 1 - Executar safx_auto_generator:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/safx_auto_generator.py --wi-id ${BUG_ID} --env LOCAL
```

O script:
1. Detecta packages modificados no branch `MFS{BUG_ID}` via `git diff`
2. Consulta `component-test-map.json` — se existe cenario SuiteAutomation, retorna `SUITE_EXISTS`
3. Se NAO existe cenario: detecta tabelas SAFX via `ALL_DEPENDENCIES` + `safx-table-index.json`
4. Gera flat-files pipe-delimited + SQL INSERTs em `tests/{BUG_ID}/safx_files/`
5. Gera `test_data_manifest.json` e executa `safx_archiver.py` para archive RC

**Resultados possiveis:**
- `SUITE_EXISTS` — cenario SuiteAutomation encontrado, SAFX nao necessaria (prosseguir para Fase 6)
- `GENERATED` — flat-files gerados com sucesso
- `NO_SAFX` — packages nao referenciam tabelas SAFX (prosseguir para Fase 6)
- `NO_PACKAGES` — nenhum package PL/SQL no branch

**Passo 2 - Validar output (se GENERATED):**
- Verificar que `tests/{BUG_ID}/safx_files/` contem `.txt` flat-files
- Verificar que `test_data_manifest.json` foi gerado

**Passo 3 - Apresentar resultado:**

```markdown
## Fase 5.8 - Dados SAFX Gerados
- Tabelas: {lista}
- Flat-files: {N} arquivos
- Rows geradas: {N}
- Manifest: tests/{BUG_ID}/test_data_manifest.json
```

---

### Fase 6 - Commit + Push + PR

**Objetivo:** Versionar as mudancas, fazer push e criar Pull Request no GitHub.

**Passo 1 - Listar arquivos modificados:**

```bash
git status --porcelain
```

Apresentar ao usuario:
```markdown
## Fase 6 - Commit + Push + PR

### Arquivos a serem commitados:
{lista de arquivos com status M/A/D}

### Mensagem de commit proposta:
```
fix(#{BUG_ID}): {descricao curta da correcao}

Bug: {BUG_TITLE}
Root cause: {causa raiz resumida}
ADO: https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/{BUG_ID}

AI-Generated fix by TAX ONE Support Dev
```

Confirmar commit? (sim/nao/editar mensagem)
```

**Passo 2 - Aguardar confirmacao** via `AskUserQuestion`.

**Passo 3 - Executar commit:**

```bash
git add {arquivos}
git commit -m "{mensagem de commit}"
```

**Passo 4 - Push:**

```bash
git push -u origin "{BRANCH_NAME}"
```

**Passo 5 - Criar Pull Request via GitHub CLI:**

```bash
gh pr create \
  --title "fix(#{BUG_ID}): {descricao curta}" \
  --body "$(cat <<'EOF'
## Bug #{BUG_ID}: {BUG_TITLE}

### Root Cause
{causa raiz}

### Correcao
{descricao da correcao}

### Arquivos Modificados
{lista de arquivos}

### Scripts de Validacao
{lista de scripts de teste}

### Roteiro de Teste Manual
{roteiro se aplicavel}

### ADO Work Item
https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/{BUG_ID}

---
AI-Generated by TAX ONE Support Dev (taxone-auto-fix)
EOF
)" \
  --base "DEV"
```

**Passo 6 - Capturar URL do PR:**

```
PR_URL = {URL retornada pelo gh pr create}
PR_NUMBER = {numero extraido da URL}
```

**Apresentar:**

```markdown
## Fase 6 - PR Criado

- Branch: {BRANCH_NAME}
- PR: {PR_URL}
- Target: DEV
- Commit: {hash}
```

---

### Fase 7.5 - Pacote Unitario (GitHub Actions)

**Objetivo:** Disparar automaticamente o workflow de geracao de pacote unitario no repositorio `tr/taxone_automacao_fab`,
para que o QA tenha o pacote disponivel para validacao no ambiente de teste.

**Condicao:** Executada SOMENTE no **Flow A** (Bug Real com correcao implementada) e SOMENTE se os arquivos modificados incluem PowerBuilder (`ws_objects/`) ou PL/SQL/BD (`artifacts/sp/`).
Alteracoes APENAS em `artifacts/java/` (Jasper/Java) **NAO geram pacote unitario**.

**Logica de Decisao:**

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

#### Passo 7.5.1 - Determinar Necessidade de Pacote

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
Fase 7.5 - Pacote Unitario: PULADA (arquivos nao requerem pacote unitario)
```
Continuar para Fase 7.

#### Passo 7.5.2 - Confirmar com Usuario

Apresentar ao usuario:
```
Pacote Unitario - Geracao Automatica
=====================================

Arquivos no PR:
{lista de arquivos}

Decisao: {Workflow X, Tipo=Y}
  - Workflow: {nome do workflow}
  - Tipo: {F/P}
  - Branch: MFS{work-item-id}

Disparar workflow de pacote unitario? (S/N)
```

Se usuario negar, registrar como "Pacote nao solicitado" e continuar para Fase 7.

#### Passo 7.5.3 - Disparar Workflow

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

#### Passo 7.5.4 - Verificar Inicio da Execucao

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

#### Passo 7.5.5 - Registrar Resultado

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

**NAO bloquear o pipeline** — continuar para Fase 7 imediatamente.
O pacote roda em runner self-hosted Windows e pode levar varios minutos.

Salvar variavel `PKG_RUN_ID` e `PKG_RUN_URL` para uso na Fase 7 (relatorio final).

---

### Fase 7 - Atualizar ADO + Relatorio Final

**Objetivo:** Atualizar o work item no Azure DevOps e gerar relatorio final.

Existem dois fluxos possiveis:

#### Flow A - Bug Real (Correcao Implementada)

**Passo 1 - Atualizar work item no ADO:**

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -X PATCH \
  -H "Content-Type: application/json-patch+json" \
  -d '[
    {
      "op": "add",
      "path": "/fields/System.Tags",
      "value": "{BUG_TAGS_EXISTENTES}; AI-Fixed"
    },
    {
      "op": "add",
      "path": "/fields/Custom.Solutions",
      "value": "## Correcao AI - Bug #{BUG_ID}\n\n### Root Cause\n{causa_raiz}\n\n### Correcao\n{descricao_correcao}\n\n### PR\n{PR_URL}\n\n### Scripts de Validacao\n{lista_scripts}\n\n---\nAI-Generated by TAX ONE Support Dev"
    },
    {
      "op": "add",
      "path": "/fields/Custom.DeveloperText",
      "value": "TAX ONE Support Dev (AI)"
    },
    {
      "op": "add",
      "path": "/fields/TR.WOW.AIPowered",
      "value": "true"
    },
    {
      "op": "add",
      "path": "/fields/Custom.DescriptionofRootCause",
      "value": "{CAUSA_RAIZ_TEXTO}"
    },
    {
      "op": "add",
      "path": "/fields/Custom.DescriptionofReleaseNotes",
      "value": "{RELEASE_NOTES}"
    }
  ]' \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{BUG_ID}?api-version=7.1"
```

**REGRA:** SEMPRE preencher `Custom.DescriptionofRootCause` com a causa raiz do bug.
Texto descritivo (pode usar `<br>` para quebras). NUNCA esquecer este campo.

**REGRA:** Se `Custom.DescriptionofReleaseNotes` ja estiver preenchido, NAO sobrescrever.

**Nota:** Os campos `Custom.Solutions`, `Custom.DeveloperText` e `TR.WOW.AIPowered`
foram verificados com a equipe. Se falharem, registrar o erro e continuar
com a atualizacao de tags apenas.

**Passo 2 - Discussion Comments (Templates Padronizados):**

Usar o modulo centralizado `scripts/ado_discussion_templates.py` para gerar e postar comments padronizados.

**Comment 1: Analise & Implementacao**

```python
from scripts.ado_discussion_templates import build_analysis_comment, post_discussion_comment

html = build_analysis_comment(
    wi_id=BUG_ID, wi_title=BUG_TITLE,
    pipeline="taxone-auto-fix",
    analysis={"causa_raiz": "...", "veredicto": "BUG_CONFIRMED", "impacto": "..."},
    implementation={"branch": BRANCH_NAME, "pr_url": PR_URL, "pr_number": N,
                    "files": [...], "ddls": [], "code_review": "PASS", "compilacao": "COMPILADO",
                    "pacote_url": PKG_RUN_URL or "N/A - sem pacote"},
    phases=[
        {"name": "Fase 0 - Ambiente", "status": "PASS", "duration": "..."},
        {"name": "Fase 1 - Buscar Bugs", "status": "PASS", "duration": "..."},
        {"name": "Fase 1.3 - N3 Brief", "status": "PASS", "duration": "..."},
        {"name": "Fase 1.5 - Triagem PM", "status": "PASS", "duration": "..."},
        {"name": "Fase 3.7 - Analise Critica", "status": "PASS", "duration": "..."},
        {"name": "Fase 4 - Diagnostico + Fix", "status": "PASS", "duration": "..."},
        {"name": "Fase 5 - Review + Testes", "status": "PASS", "duration": "..."},
        {"name": "Fase 6 - Commit + PR", "status": "PASS", "duration": "..."},
        {"name": "Fase 7.5 - Pacote Unitario", "status": "PASS/PULADA", "duration": "..."},
        {"name": "Fase 7 - ADO Update", "status": "PASS", "duration": "..."},
    ],
    pendencias=[],
    zendesk={"ticket_id": "...", "status": "...", "resumo": "..."},
)
post_discussion_comment(BUG_ID, html)
```

**Comment 2: Resultados de Testes** (postar apos Fase 5)

```python
from scripts.ado_discussion_templates import build_test_results_comment, post_discussion_comment

html = build_test_results_comment(
    wi_id=BUG_ID, wi_title=BUG_TITLE,
    agent="taxone-auto-fix",
    db_connection="V2R010AC@localhost:1521/MFSPDB",
    manual_tests=[{"num": 1, "cenario": "...", "status": "PASS", "detalhe": "..."}],
    suite_results={...},  # ou None
    nao_testado=[],
    attachments=[{"filename": "...", "url": "..."}],
)
post_discussion_comment(BUG_ID, html)
```

**Passo 3 - Gerar relatorio final (terminal):**

Apresentar no terminal o resumo consolidado das fases executadas para o usuario.

---

### Fase 8 - Archival SAFX para RC

**Objetivo:** Exportar dados SAFX do banco com formatacao SAF_EXPORTA_TAB para reproducao em RC.

**Condicao de entrada:** `tests/{BUG_ID}/safx_files/` existe com flat-files gerados na Fase 5.8.

**Auto-Skip:**
- Se nao existe `tests/{BUG_ID}/safx_files/`: **SKIP** — nenhum SAFX foi gerado.
- Se Fase 5.8 reportou `safx_generated: false`: **SKIP** — componente nao usa SAFX.
- Se `TAXONE_DW_REPO` nao configurado (aviso da Fase 0): **SKIP** com aviso.

Se SKIP:
```
Fase 8 SKIP — {motivo: sem safx_files / componente sem SAFX / repo nao configurado}
```

**Passo 1 - Executar safx_archiver:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/safx_archiver.py --wi-id ${BUG_ID} --env LOCAL
```

**Passo 2 - Upload para ADO:**
- Anexar todos os arquivos de `tests/{BUG_ID}/safx_archive_rc/` como Attachments na WI
- Postar Discussion comment com lista de arquivos e instrucoes de importacao RC

**Passo 3 - Apresentar resultado:**

```markdown
## Fase 8 - SAFX Arquivado para RC
- **Status:** {OK / SKIP}
- **Arquivos:** {lista ou "nenhum"}
- **Upload ADO:** {OK / FAIL / N/A}
- **Instrucoes RC:** Importar flat-files via PKG_IMP_ONLINE_FPROC
```

---

### Fase 8.5 - Publicar Cenarios no Repo QA (OBRIGATORIO)

**Objetivo:** Publicar artefatos de teste em `cenarios/{BUG_ID}/` no repo `taxone_automacao_qa`.

**Condicao de entrada:** Testes foram executados com sucesso (Fase 5 concluida com APROVADO).

**Auto-Skip:**
- Se Fase 5 nao foi executada (Flow B - As Designed): **SKIP**
- Se `tests/{BUG_ID}/` esta vazio (nenhum artefato gerado): **SKIP** com aviso
- Se repo `taxone_automacao_qa` nao acessivel: **SKIP** com aviso (nao abortar pipeline)

Se SKIP:
```
Fase 8.5 SKIP — {motivo: flow B / sem artefatos / repo QA inacessivel}
```

**SEMPRE executar** quando houver artefatos e o repo QA estiver acessivel.

**Passo 1 - Copiar artefatos + branch + commit + push + PR:**
```bash
mkdir -p /c/@@Dev/Git/taxone_automacao_qa/cenarios/${BUG_ID}
cp tests/${BUG_ID}/* /c/@@Dev/Git/taxone_automacao_qa/cenarios/${BUG_ID}/
cd /c/@@Dev/Git/taxone_automacao_qa
git fetch origin && git checkout -b MFS${BUG_ID} origin/dev
git add cenarios/${BUG_ID}/
git commit -m "MFS${BUG_ID} - Cenarios de teste"
git push -u origin MFS${BUG_ID}
gh pr create --base dev --title "[DEV] MFS${BUG_ID} - Cenarios de teste" --body "AB#${BUG_ID}"
```

**Alternativa:** `python scripts/qa_test_publisher.py --wi-id ${BUG_ID}`

**Passo 2 - Apresentar resultado:**

```markdown
## Fase 8.5 - Cenarios Publicados no Repo QA
- **Status:** {OK / SKIP}
- **Artefatos copiados:** {N arquivos}
- **Branch:** MFS{BUG_ID}
- **PR:** {URL ou N/A}
```

---

#### Flow B - As Designed (Nao e Bug)

**Passo 1 - Confirmar com usuario:**

```
A analise critica determinou que este comportamento e "As Designed" (conforme projetado).

Deseja:
1. Atualizar o ADO com tag "AI-AsDesigned" e justificativa
2. Abortar sem atualizar o ADO

Opcao?
```

**Passo 2 - Se confirmado, remover branch de trabalho:**

```bash
git checkout DEV
git branch -D "{BRANCH_NAME}"
```

**Passo 3 - Atualizar work item no ADO:**

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -X PATCH \
  -H "Content-Type: application/json-patch+json" \
  -d '[
    {
      "op": "add",
      "path": "/fields/System.Tags",
      "value": "{BUG_TAGS_EXISTENTES}; AI-AsDesigned"
    },
    {
      "op": "add",
      "path": "/fields/Custom.Solutions",
      "value": "## Analise AI - Bug #{BUG_ID}\n\n### Veredicto: As Designed\n\n### Justificativa\n{justificativa_dba}\n\n### Comportamento Esperado\n{comportamento_esperado}\n\n### Recomendacao\n{recomendacao_usuario}\n\n---\nAI-Generated by TAX ONE Support Dev"
    },
    {
      "op": "add",
      "path": "/fields/TR.WOW.AIPowered",
      "value": "true"
    }
  ]' \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{BUG_ID}?api-version=7.1"
```

**Passo 3.5 - Gerar sugestao de resposta ao cliente:**

Quando a WI tiver ticket Zendesk associado (TKT no titulo), gerar sugestao de resposta
profissional para o cliente em `tests/{BUG_ID}/resposta_cliente.txt`.

A resposta deve:
- Ser em portugues formal e cordial
- Explicar o que esta ocorrendo de forma clara (sem jargao tecnico interno)
- Descrever o comportamento esperado do sistema
- Incluir recomendacao pratica (o que o cliente deve fazer)
- Indicar como o cliente pode verificar/confirmar que o sistema funciona corretamente
- Oferecer suporte adicional se necessario
- Finalizar com "Atenciosamente, Suporte TAX ONE"

Template:

```
Prezado(a),

Analisamos a questao reportada sobre {descricao_simples_do_problema}.

Apos verificacao detalhada {dos logs / dos dados / do ambiente}, identificamos que {explicacao_do_comportamento}.

{detalhamento_claro_sem_jargao}

Recomendacao:
{orientacao_pratica_para_o_cliente}

Como verificar:
{passos_para_o_cliente_confirmar}

Caso necessite de suporte adicional, estamos a disposicao.

Atenciosamente,
Suporte TAX ONE
```

Salvar em `tests/{BUG_ID}/resposta_cliente.txt` e postar na Discussion do ADO como
sugestao (com prefixo "Sugestao de resposta ao cliente:").

---

**Passo 4 - Gerar relatorio final:**

```markdown
## Relatorio Final - Bug #{BUG_ID}

### Resumo
- **Bug:** #{BUG_ID} - {BUG_TITLE}
- **Veredicto:** As Designed - Nao e Bug
- **PR:** Nenhum (nao houve correcao)
- **ADO:** Atualizado (tag: AI-AsDesigned)

### Analise Critica (DBA)
{justificativa completa}

### Comportamento Esperado
{descricao do comportamento conforme projetado}

### Recomendacao ao Usuario
{orientacao para o usuario/cliente}

### Proximos Passos
1. Revisar a justificativa
2. Comunicar ao solicitante a analise
3. Resolver o bug no ADO como "As Designed" (se concordar)

### Fases Executadas
| Fase | Status |
|------|--------|
| 0 - Ambiente | OK |
| 1 - Buscar Bugs | OK |
| 1.5 - Triagem PM | {Veredicto} ({confianca}%) |
| 1.6 - Cenarios de Teste | {N cenarios / Pulado} |
| 2 - Workspace | OK |
| 3 - Knowledge | OK |
| 3.5 - Bugs Similares | {OK/Nenhum encontrado} |
| 3.7 - Analise Critica | As Designed ({confianca}%) |
| 4 - Diagnostico + Fix | Pulado (As Designed) |
| 5 - Review + Testes | Pulado (As Designed) |
| 5.8 - SAFX Gerados | Pulado (As Designed) |
| 6 - Commit + PR | Pulado (As Designed) |
| 7.5 - Pacote Unitario | Pulado (As Designed) |
| 7 - ADO Update | OK (tag: AI-AsDesigned) |
| 8 - SAFX Archival RC | Pulado (As Designed) |
```

---

## Protocolo de Pausa/Retomada do Pipeline

### Salvar Estado (Pausa)

Quando o pipeline precisa pausar (ex: aguardando resultado de consulta remota),
salvar o estado em `tests/{BUG_ID}/pipeline_state.json`:

```json
{
  "bug_id": "{BUG_ID}",
  "bug_title": "{BUG_TITLE}",
  "fase_atual": "{fase onde pausou}",
  "motivo_pausa": "{descricao}",
  "timestamp": "{ISO 8601}",
  "veredictos": {
    "pm": "{veredicto PM ou null}",
    "dba": "{veredicto DBA ou null}",
    "developer": "{status developer ou null}"
  },
  "queries_despachadas": [
    {
      "query": "{SQL}",
      "empresa": "{EMPRESA}",
      "env": "{uat|prod}",
      "motivo": "{justificativa}",
      "timestamp": "{ISO 8601}"
    }
  ],
  "knowledge_carregado": ["{lista de arquivos carregados}"],
  "contexto_adicional": "{informacoes extras do usuario}"
}
```

**Regra:** O state file NUNCA armazena tokens, senhas ou credenciais.

### Detectar e Retomar (Fase 1)

Na Fase 1, apos o usuario selecionar um bug, verificar se existe
`tests/{BUG_ID}/pipeline_state.json`:

```
Se state file existe:
  Apresentar resumo:
  ---
  ## Pipeline com estado salvo encontrado

  - **Bug:** #{BUG_ID} - {BUG_TITLE}
  - **Pausado na fase:** {fase_atual}
  - **Motivo:** {motivo_pausa}
  - **Queries despachadas:** {N}

  Deseja:
  1. Retomar pipeline (fornecer resultados das queries)
  2. Reiniciar pipeline do zero (descarta estado anterior)
  ---
  Se opcao 1: pedir resultados ao usuario e injetar como contexto adicional
  Se opcao 2: deletar state file e continuar normalmente
```

Na retomada, injetar os resultados fornecidos pelo usuario como contexto adicional
para os agentes subsequentes (PM, DBA, Developer).

---

## Tratamento de Erros

| Codigo | Erro | Fase | Acao |
|--------|------|------|------|
| **E001** | `ADO_PAT` nao configurado | 0 | Abortar com instrucoes de configuracao |
| **E002** | GitHub CLI nao autenticado | 0 | Abortar com instrucoes `gh auth login` |
| **E003** | Nao esta em repositorio Git | 0 | Abortar com instrucoes de navegacao |
| **E004** | Query ADO retornou 0 bugs | 1 | Informar e encerrar |
| **E005** | Query ADO falhou (401/403) | 1 | Verificar permissoes do PAT |
| **E006** | Query ADO falhou (404) | 1 | Verificar QUERY_ID e URL do projeto |
| **E007** | Work item nao encontrado | 1 | Informar ID invalido |
| **E008** | Workspace sujo + usuario recusou stash | 2 | Abortar pipeline |
| **E009** | Branch ja existe | 2 | Perguntar se deseja reusar ou criar nova |
| **E010** | git pull falhou (conflitos) | 2 | Informar e pedir resolucao manual |
| **E011** | Knowledge path inexistente | 3 | Continuar sem knowledge (aviso) |
| **E012** | WIQL de busca similar falhou | 3.5 | Continuar sem similares (aviso) |
| **E013** | DBA inconclusivo + usuario nao decidiu | 3.7 | Perguntar novamente ou abortar |
| **E014** | Developer nao conseguiu corrigir | 4 | Oferecer opcoes (retry, abortar, manual) |
| **E015** | Reviewer reprovou | 5 | Voltar para Fase 4 ou abortar |
| **E016** | git commit falhou | 6 | Diagnosticar e informar |
| **E017** | git push falhou | 6 | Verificar permissoes e remote |
| **E018** | gh pr create falhou | 6 | Verificar auth e permissoes |
| **E019** | ADO update falhou (campo custom) | 7 | Tentar somente tags; informar erro |
| **E020** | ADO update falhou (permissao) | 7 | Informar; gerar texto para update manual |
| **E021** | Empresa nao encontrada no TENANT_LOOKUP | 1.5/3.7/4 | Perguntar empresa ao usuario via AskUserQuestion |
| **E022** | Falha no run_query.py (dispatch) | 1.5/3.7/4 | Exibir erro detalhado; oferecer retry ou continuar sem query |
| **E023** | Estado de pipeline corrompido (JSON invalido) | 1 | Oferecer reiniciar do zero ou abortar |

### Estrategia de Recuperacao

Para qualquer erro NAO listado acima:

1. **Registrar** o erro com detalhes (fase, comando, saida)
2. **Apresentar** ao usuario com contexto claro
3. **Sugerir** acao corretiva quando possivel
4. **Perguntar** se deseja tentar novamente, pular a fase ou abortar
5. **NUNCA** continuar silenciosamente apos um erro

---

## Fluxograma Resumido

```
[Fase 0] Ambiente (+ validacao completa: TAXONE_DW_REPO, Oracle, config, knowledge)
    |
[Fase 1] Buscar Bugs ADO + Selecionar Bug
    |
[Fase 1.3] N3 Brief Enrichment (taxone-n3-triage → n3_brief.json)
    |
[Fase 1.5] Triagem PM (taxone-pm, consome n3_brief.json)  <-- GATE DE QUALIDADE
    |
    +---> [NOT_A_BUG] ---------> [Fase 7 - Flow B] (tag SUST-IA-CLAUDE-NOT-BUG)
    +---> [FEATURE_REQUEST] ----> Reclassificar + Encerrar (+ tag SUST-IA-CLAUDE-REGRA se envolver regra)
    +---> [INCOMPLETE_ANALYSIS] -> Devolver N1/N2 + Encerrar (tag SUST-IA-CLAUDE-ANALISE)
    |                              +---> [Consulta Remota?] -> Despachar query + PAUSAR
    +---> [DUPLICATE] ----------> Fechar + Encerrar
    +---> [NEEDS_INFO] ---------> Perguntar + Retriar (tag SUST-IA-CLAUDE-ANALISE)
    |                              +---> [Consulta Remota?] -> Despachar query + PAUSAR
    |
    +---> [CONFIRMED_BUG]
             |
         [Fase 1.6] Geracao de Cenarios de Teste (taxone-pm → test_scenarios.json)
             |
         [Fase 1.7] Enriquecimento de Cenarios (test_enricher.py)
             |
         [Fase 1.8] Scripts Pre-Dev (taxone-tester, modo pre_dev → validation_scripts_pre_dev.sql)
             |
         [Fase 1.9] SM Allocation Check (se AssignedTo vazio)
             |
         [Fase 2] Workspace Limpo + Branch
             |
         [Fase 3] Knowledge + Alinhamento
             |
         [Fase 3.5] Buscar Bugs Similares
             |
         [Fase 3.7] Analise Critica (taxone-dba)
             |
             +---> [AS DESIGNED] ---> [Fase 7 - Flow B]
             +---> [INCONCLUSIVO] --> Perguntar (tag SUST-IA-CLAUDE-ANALISE, + SUST-IA-CLAUDE-REGRA se regra)
             |                      +---> [Consulta Remota?] -> Despachar query + PAUSAR
             |
             +---> [BUG REAL]
                      |
                  [Fase 3.7.1] Registrar Causa Raiz (root_cause_entry.json)
                      |
                  [Fase 3.7.2] Impact Assessment (impact_assessment.json)
                      |
                  [Fase 3.7.3] Formalizar Regras Afetadas (NEW) → affected_rules.json
                      |          (taxone-architect, auto-skip se bug simples)
                      |
                  [Fase 3.8] Historico Git (git_history_analyzer.py)
                      |
                  [Fase 3.9] Baseline RC
                      |
                  [Fase 4] Explorar + Diagnosticar + Corrigir (taxone-developer)
                      |
                      +---> [NAO REPRODUZIU] -> [Consulta Remota?] -> Despachar query + PAUSAR
                      |
                  [Fase 4.5] Impacto + Cobertura de Regras (taxone-architect)
                      |        (+ coverage quantitativo GO/NO-GO % se affected_rules.json existe)
                      |        (+ tag SUST-IA-CLAUDE-REGRA se nova regra)
                      |
                      +---> [NO-GO] ---> Voltar Fase 4 com feedback
                      |
                      +---> [GO]
                               |
                           [Fase 5.0] Enriquecimento Pre-Test com Regras (NEW)
                               |       (cruzar affected_rules x test_scenarios, auto-skip se sem affected_rules)
                               |
                           [Fase 5] Review (taxone-reviewer) + Testes (taxone-tester)
                               |
                               +---> [REPROVADO] ---> Voltar Fase 4
                               |
                               +---> [APROVADO]
                                        |
                                    [Fase 5.5] Coverage Report (Gate GO/NO-GO)
                                        |
                                    [Fase 5.8] SAFX Auto-detect
                                        |
                                    [Fase 5.9] Compliance Check (Gate GO/NO-GO)
                                        |
                                    [Fase 6] Commit + Push + PR (gh pr create)
                                        |
                                    [Fase 7 - Flow A] ADO Update + Relatorio Final
                                        |
                                    [Fase 8] Archival SAFX para RC (auto-skip se sem SAFX)
                                        |
                                    [Fase 8.5] Publicar Cenarios no Repo QA (auto-skip se Flow B)
```

---

## Documentacao de Features

Os seguintes documentos de features podem ser criados incrementalmente
via `/taxone-compound` e serao consumidos por este pipeline:

| Documento | Caminho | Descricao |
|-----------|---------|-----------|
| Overview arquitetura | `knowledge/architecture/overview.md` | Visao geral do TAX ONE |
| Tech Stack | `knowledge/architecture/tech-stack.md` | Stack tecnologica detalhada |
| Patterns | `knowledge/architecture/patterns.md` | Padroes PL/SQL, PB, Java |
| Code Standards | `knowledge/conventions/code-standards.md` | Padroes de qualidade |
| Naming | `knowledge/conventions/naming.md` | Convencoes de nomenclatura |
| Features | `knowledge/features/{feature}.md` | Documentacao por feature/modulo |
| Solutions | `knowledge/solutions/{solution}.md` | Solucoes de bugs para referencia |
| ADO API Guide | `references/ado-api-guide.md` | Guia de uso da REST API do ADO |

### Estrutura do Knowledge

```
${CLAUDE_PLUGIN_ROOT}/knowledge/
├── architecture/
│   ├── overview.md           → Visao geral da arquitetura
│   ├── tech-stack.md         → Stack tecnologica
│   └── patterns.md           → Padroes de codigo
├── conventions/
│   ├── code-standards.md     → Padroes de qualidade
│   └── naming.md             → Convencoes de nomenclatura
├── features/
│   ├── {modulo-1}.md         → Feature: Modulo 1
│   ├── {modulo-2}.md         → Feature: Modulo 2
│   └── ...
└── solutions/
    ├── {bug-id-1}.md         → Solucao documentada
    ├── {bug-id-2}.md         → Solucao documentada
    └── ...
```

---

## Exemplos de Uso

### Exemplo 1 - Correcao de Bug Real

```
Usuario: /taxone-auto-fix 9bb6e572-8580-4eb3-86e6-a56bc5303d69

[Fase 0] Ambiente validado
[Fase 1] 3 bugs encontrados - usuario seleciona #54321
[Fase 2] Branch joao-silva/bugfix/54321 criada
[Fase 3] Knowledge de apuracao carregado
[Fase 3.5] 2 bugs similares encontrados
[Fase 3.7] DBA: Bug Real (confianca 85%)
[Fase 4] Developer: Correcao em PKG_APURACAO_BODY.sql:234
[Fase 4.5] Architect: GO - sem impacto em regras downstream
[Fase 5] Reviewer: Aprovado | Tester: 5 scripts SQL
[Fase 6] PR #123 criado no GitHub
[Fase 7] ADO atualizado (tag: AI-Fixed)
```

### Exemplo 2 - Bug As Designed

```
Usuario: /taxone-auto-fix 9bb6e572-8580-4eb3-86e6-a56bc5303d69

[Fase 0] Ambiente validado
[Fase 1] 3 bugs encontrados - usuario seleciona #54322
[Fase 2] Branch joao-silva/bugfix/54322 criada
[Fase 3] Knowledge de notas fiscais carregado
[Fase 3.5] Nenhum similar encontrado
[Fase 3.7] DBA: As Designed (confianca 90%)
         "O calculo segue a legislacao estadual vigente"
[Fase 4-6] Pulados
[Fase 7] ADO atualizado (tag: AI-AsDesigned)
         Branch removida
```

---

## Notas Tecnicas

### Sobre PL/SQL e Build

O TAX ONE usa PL/SQL como stack principal (~90% da logica de negocio).
PL/SQL e uma linguagem de banco de dados Oracle - nao possui build local.
Os scripts `.sql` sao versionados no Git e deployados diretamente no banco Oracle.

Implicacoes para o pipeline:
- **Sem etapa de build** (diferente de projetos .NET/Java)
- **Sem testes automatizados** (sem utPLSQL configurado)
- **Validacao via scripts SQL** (o taxone-tester gera scripts de validacao)
- **Review focado em PL/SQL** (SQL injection, excecoes, performance Oracle)

### Sobre PowerBuilder

PowerBuilder e usado para a interface desktop. Arquivos `.pbl`, `.pbd` e
DataWindows (`.srd`) sao versionados. NAO e possivel compilar PowerBuilder
via linha de comando neste ambiente.

### Sobre Java

Java e usado para integracao e web services. Se a correcao envolver Java,
o developer pode usar Maven/Gradle se disponivel, mas isso NAO e obrigatorio
e NAO deve bloquear o pipeline.

### Autenticacao ADO

Todas as chamadas a API do ADO usam Basic Auth com PAT via header Authorization:
```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" "https://dev.azure.com/..."
```

O formato usa `printf '%s' ":$ADO_PAT" | base64 -w0` para codificar em Base64
o par `:PAT` (usuario vazio + PAT como senha) e passa via header `Authorization: Basic`.

### Campos Customizados ADO (Verificados)

Os seguintes campos foram verificados com a equipe do TAX ONE:

- `Custom.Solutions` - Campo para comunicacao interna no work item
- `Custom.DeveloperText` - Campo para nome do revisor
- `TR.WOW.AIPowered` - Flag indicando que o item foi processado por AI (valor: "true")

Se algum desses campos falhar na atualizacao, a Fase 7 deve:
1. Registrar o erro
2. Atualizar somente as tags (que sempre funcionam)
3. Apresentar o texto que seria inserido para o usuario copiar manualmente

### Limites e Restricoes

- **Maximo de bugs por query:** 50 (limit da API WIQL)
- **Tamanho maximo de campo ADO:** 32.000 caracteres (HTML)
- **Timeout de curl:** 30 segundos por chamada
- **Branches simultaneas:** Uma por execucao do pipeline
- **Re-execucao:** Se o pipeline falhar no meio, limpar branch e re-executar do inicio

---

## Historico de Versoes

| Versao | Data | Descricao |
|--------|------|-----------|
| 1.0.0 | 2026-03-06 | Versao inicial - adaptado do pattern LegalOne para TAX ONE PL/SQL/PB/Java |
| 1.2.0 | 2026-03-28 | Enriquecimento com features do us-implement: (1) Validacao de ambiente completa na Fase 0 (TAXONE_DW_REPO, Oracle, config, knowledge), (2) Nova Fase 3.7.3 - Formalizar regras afetadas (affected_rules.json), (3) Coverage quantitativo GO/NO-GO na Fase 4.5, (4) Nova Fase 5.0 - Enriquecimento pre-test cruzando regras com cenarios, (5) Compliance renumerado de 5.7 para 5.9, (6) Archival/QA com auto-skip estruturado |
