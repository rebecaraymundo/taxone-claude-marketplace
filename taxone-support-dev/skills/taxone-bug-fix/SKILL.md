# taxone-bug-fix Skill

Pipeline autonomo e leve para diagnostico e correcao de bugs no TAX ONE.
Sem integracao com ADO - foco exclusivo em correcao local no codigo PL/SQL/PowerBuilder/Java.

---

## Visao Geral

Pipeline de 4 estagios para correcao de bugs no sistema fiscal TAX ONE (Mastersaf).
Opera de forma autonoma apos alinhamento inicial com o desenvolvedor.

---

## Regras do Pipeline

### R1 - Interacao Minima
O UNICO ponto de interacao com o desenvolvedor e no final do Estagio 1 (Alinhamento).
Apos confirmacao, o pipeline trabalha de forma 100% autonoma ate o relatorio final.

### R2 - Agentes Permitidos
Os UNICOS agentes permitidos neste pipeline sao:
- `taxone-sm` - Alocacao de Developer e Tester por afinidade tecnologica
- `taxone-n3-triage` - Enrichment e estruturacao de WIs N3 (pre-analise)
- `taxone-plsql` - Implementacao PL/SQL (packages, procedures, views)
- `taxone-pb` - Implementacao PowerBuilder (DataWindows, scripts)
- `taxone-java` - Implementacao Java (web services, Jasper, servlets)
- `taxone-plsql-reviewer` - Code review PL/SQL Oracle
- `taxone-pb-reviewer` - Code review PowerBuilder
- `taxone-java-reviewer` - Code review Java
- `taxone-dba` - Analise de performance e impacto em banco Oracle

### R3 - Knowledge First
SEMPRE carregar knowledge relevante ANTES de explorar codigo.
A base de conhecimento esta em `${CLAUDE_PLUGIN_ROOT}/knowledge/`.

### R4 - Minimo Necessario
Alterar SOMENTE o que resolve o bug. NAO refatorar codigo adjacente.
NAO criar features novas. NAO otimizar codigo que nao esta relacionado.

### R5 - Upload de Evidencias AUTOMATICO
Apos gerar QUALQUER artefato em `tests/{WI_ID}/`, SEMPRE fazer upload automaticamente na WI do ADO — **SEM perguntar ao usuario**.
1. Upload de TODOS os arquivos relevantes como Attachments na WI (exceto utilitarios como .bat, upload scripts)
2. Postar Discussion comment com tabela de resultados (arquivos, status, conclusao)
3. Publicar em `cenarios/{WI_ID}/` no repo `taxone_automacao_qa` (Phase 3.9)
**NUNCA perguntar "quer que eu anexe?" — e parte obrigatoria do fluxo.**

---

## Estagios

### Estagio 0.9: SM Allocation Check (OBRIGATORIA)

**Objetivo:** Garantir que o WI tenha Developer e Tester atribuidos ANTES de iniciar o desenvolvimento.

**REGRA:** Esta fase e **OBRIGATORIA**. O pipeline NAO pode prosseguir para o Estagio 1 sem `Custom.Developer` E `Custom.Tester` preenchidos.

**Passo 1 - Verificar Custom.Developer e Custom.Tester:**

Verificar se AMBOS os campos estao preenchidos no WI (via ADO API).

- Se **AMBOS preenchidos**: pular direto para Estagio 1. Exibir:
  ```
  ## Estagio 0.9 - Alocacao (Skip)
  WI ja tem Developer: {dev} e Tester: {tester}. Mantendo alocacao existente.
  ```
- Se **pelo menos um vazio**: prosseguir com Passo 2. **NAO sobrescrever campo ja preenchido.**

**Passo 2 - Lancar taxone-sm em modo alocacao avulsa:**

Invocar via Agent com `subagent_type="taxone-sm"`:

```
## Alocacao Avulsa - Bug #{WI_ID}

### Dados do Work Item
- **Titulo:** {WI_TITLE}
- **Tipo:** Bug
- **Area Path:** {area_path}
- **Tags:** {WI_TAGS}
- **Severity:** {WI_SEVERITY}
- **Priority:** {WI_PRIORITY}

### Tarefa
Executar alocacao avulsa conforme documentado no seu perfil de agente:
1. Carregar TEAM_ROSTER e TEAM_SPECIALIZATIONS
2. Resolver modulo/vertical/tech do WI
3. Calcular score de todos os devs e testers
4. Retornar top 3 devs e top 3 testers com scores e recomendacao final
```

**Passo 3 - Apresentar resultado e confirmar:**

```markdown
## Estagio 0.9 - Alocacao SM

O WI #{WI_ID} nao tem dev/tester atribuido.
O Scrum Master recomenda:

- **Dev:** {nome} (score: {X}) - {motivo}
- **Tester:** {nome} (score: {X}) - {motivo}

Deseja aplicar esta alocacao no ADO?
1. Sim, atribuir dev e tester recomendados
2. Nao, prosseguir sem alocacao
3. Escolher manualmente
```

- Se **opcao 1:** PATCH no ADO para atribuir `Custom.Developer` e `Custom.Tester`. Adicionar tag `SUST-IA-CLAUDE`. Setar `TR.WOW.AIPowered` = `"true"`.
- Se **opcao 2:** Registrar que usuario optou por nao alocar. Prosseguir.
- Se **opcao 3:** Perguntar nomes e PATCH.

---

### Estagio 1: Knowledge + Alinhamento

**Objetivo:** Carregar contexto e alinhar entendimento com o desenvolvedor.

**Pre-passo - Carregar N3 Brief (se existir):**

Se `tests/{WI_ID}/n3_brief.json` existir (gerado pelo `taxone-n3-triage`), carrega-lo:
- Usar `problem.summary` como resumo inicial do bug
- Usar `component_mapping` como hipotese de packages/tabelas
- Usar `module.primary` como modulo afetado
- Usar `data_gaps` para saber o que ainda falta
- **Pular** etapas 1 e 2 abaixo se o brief ja cobrir essas informacoes

1. **Carregar Knowledge:**
   - Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/features/[feature].md` (se existir para a feature afetada)
   - Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/patterns.md` para padroes do projeto
   - Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/code-standards.md` para convencoes

2. **Formular Entendimento:**
   - Resumir o bug em 2-3 frases (ou usar `n3_brief.problem.summary` se disponivel)
   - Listar packages/procedures/views suspeitos (ou usar `n3_brief.component_mapping` se disponivel)
   - Identificar modulo afetado (ou usar `n3_brief.module.primary` se disponivel)

3. **Ponto de Interacao (UNICO):**
   - Apresentar entendimento ao desenvolvedor
   - Perguntar se precisa carregar knowledge adicional
   - Perguntar se ha contexto extra (ambiente, dados, logs)
   - Apos confirmacao, iniciar execucao autonoma

### Estagio 1.5: Analise de Historico Git (Opcional)

**Condicao:** Executar se o Estagio 1 identificou packages/procedures PL/SQL no contexto do bug.

**Objetivo:** Consultar historico git para identificar commits recentes que possam ter causado o problema.

**Execucao:**
```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/git_history_analyzer.py \
  --repo "$TAXONE_DW_REPO" \
  --objects "{PACKAGES_IDENTIFICADOS}" \
  --timeframe 60 \
  --wi-title "{TITULO_DO_BUG}" \
  --format json
```

**Processamento:**
- Se `top_suspects` encontrados: incluir no contexto do Estagio 2 como pistas de investigacao
- Se nada encontrado: seguir normalmente, nao bloqueia

**Nota:** Este estagio e automatico e nao-bloqueante. Nao requer interacao com o usuario.

### Estagio 1.5.5: Enriquecer com Datadog (Automatica)

**Objetivo:** Buscar dados reais de APM/logs/traces no Datadog via MCP Server para enriquecer o
contexto de WIs relacionadas a importacao, performance, erros em batch ou job servidor.

**Pre-requisito:** MCP Server `datadog` configurado em `~/.claude.json` (auth via OAuth).
Org: `trta-onesource` | Permissao: MCP Read (somente leitura).

**Condicao de Entrada:**

1. Titulo ou descricao do bug contem keywords de performance/importacao
2. MCP Server `datadog` disponivel

**Se QUALQUER condicao NAO atendida:** pular silenciosamente para Estagio 2.

**Keywords de Ativacao (case-insensitive):**

`importa`, `importacao`, `lentidao`, `lento`, `timeout`, `performance`, `demora`, `batch`,
`job servidor`, `erro importacao`, `travou`, `demorado`, `processamento`, `carga`, `SAFX`,
`rejeita`, `desconsidera`, `ignora registros`

**Passos:**

1. **Buscar Logs:** `search_datadog_logs` — `service:taxone* status:(error OR warn) {termos}` (7 dias, 10 results)
2. **Buscar Traces:** `search_datadog_spans` — `service:taxone* @duration:>5s {termos}` (7 dias, 5 results)
3. **Buscar Metricas:** `get_datadog_metric` — latencia media, P95, taxa de erro (7 dias)
4. **Buscar Monitors:** `search_datadog_monitors` — `taxone OR mastersaf`
5. **Buscar RUM / User Journey:** SEMPRE que WI envolver tela. **IMPORTANTE**: No TAX ONE, dados RUM vem embedados nos APM traces (`ingestion_reason:rum`), NAO como eventos RUM separados.
   - **Fonte primaria**: `search_datadog_spans` — `service:taxone* {termos}` com `custom_attributes: ["usr.*", "view.*", "session.*"]`
   - **Fonte secundaria (fallback)**: `search_datadog_rum_events` — `@type:error @application.name:*taxone*`
   - Extrair dos spans RUM: `usr.menuPath`, `usr.module`, `view.name`, `view.url`, `view.referrer`, `session.has_replay`, `usr.email`, `usr.firmId`, `usr.dbSchema`, `duration`
   - Gerar `DD_RUM_USER_JOURNEY` com sequencia de navegacao (module, menu path, URLs, tempos) para alimentar Playwright

Apresentar bloco formatado e guardar variaveis: `DD_RELEVANT`, `DD_SERVICE`, `DD_ERROR_LOGS`,
`DD_SLOW_TRACES`, `DD_AVG_LATENCY`, `DD_P95_LATENCY`, `DD_ERROR_RATE`, `DD_MONITORS_ALERT`,
`DD_RUM_ERRORS`, `DD_RUM_USER_JOURNEY`, `DD_RUM_SESSION_ID`, `DD_RUM_ANOMALIES`, `DD_RUM_KNOWN_MATCHES`,
`DD_SIMILAR_FIXES`.

**Busca Estrutural de Fixes Anteriores** (executar ANTES do brainstorming de hipoteses):

Buscar fixes anteriores que tocaram as mesmas tabelas/procedures/DDLs da WI atual:
```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/knowledge_search.py --wi-context {WI_ID} --format table
```
Fontes: `knowledge/solutions/*.md` (YAML frontmatter), `knowledge/solutions/INDEX.md` (patterns), `knowledge/ado-fixes/_metadata.json`, `tests/*/n3_brief.json`.
Se encontrar matches HIGH/MEDIUM, considerar como hipotese prioritaria na analise.

**Knowledge Base RUM** (consultar para enriquecer analise):
- `knowledge/datadog/module-service-map.json` — mapa modulo TAX ONE → service/resource/URLs Datadog
- `knowledge/datadog/known-rum-errors.json` — catalogo de erros RUM conhecidos com causa raiz e acao
- `knowledge/datadog/performance-baselines.json` — baselines P50/P95/P99 por endpoint

**Script auxiliar:** `scripts/rum_enricher.py` — classificacao de relevancia, match de erros, deteccao de anomalias.

Uso nas fases posteriores:
- **Estagio 2 (Diagnostico):** usa `DD_ERROR_LOGS` e `DD_SLOW_TRACES` para correlacionar com o codigo
- **Estagio 2 (E2E):** usa `DD_RUM_USER_JOURNEY` para gerar specs Playwright que reproduzam o caminho do cliente. Automatizar via `scripts/rum_to_e2e.py --wi-id {WI_ID}` que cruza RUM journey com `playwright-test-map.json` e gera spec ephemeral.
- **Estagio 3 (Review):** valida se a correcao melhora os indicadores detectados
- **taxone-rum-analyst (deep-dive):** invocar para analise RUM profunda se erros complexos ou anomalias detectadas

**Fault-tolerant:** Se MCP retornar erro em qualquer passo, registrar warning e continuar.
NUNCA bloquear o pipeline por falha no Datadog.

### Estagio 2: Explorar + Diagnosticar + Corrigir

**Objetivo:** Encontrar a causa raiz e implementar a correcao.

**Agente: taxone-plsql / taxone-pb / taxone-java** (conforme linguagem detectada)

Selecionar agente conforme sinais no diagnostico:
- Packages PL/SQL (.sql, PKG_, PRC_, FNC_, TRG_, VW_) → `taxone-plsql`
- DataWindows (.srd, .srw, .srf, .sru), scripts PB → `taxone-pb`
- Classes Java (.java, .jrxml), servlets, Jasper → `taxone-java`
- Multiplas linguagens: lancar na ordem PL/SQL → PB (sequencial) ou PL/SQL + Java (paralelo)

Instrucoes para o subagente:

```
Voce recebeu a seguinte descricao de bug no TAX ONE:
{descricao_do_bug}

Knowledge carregado:
{knowledge_resumido}

Hipotese inicial:
{hipotese_do_estagio_1}

Seu trabalho:
1. EXPLORAR: Ir direto nos packages/procedures suspeitos. Confirmar ou refutar a hipotese.
2. DIAGNOSTICAR: Identificar a causa raiz exata (package:procedure:linha).
3. CORRIGIR: Implementar a correcao minima necessaria seguindo patterns do projeto.
4. REPORTAR: Entregar root cause + arquivos modificados + justificativa.
```

**Se o bug envolver performance Oracle**, lancar tambem `taxone-dba`:

```
Analisar o impacto em performance da seguinte mudanca:
{descricao_da_mudanca}

Tabelas envolvidas: {tabelas}
Verificar: indices necessarios, explain plan, particionamento.
```

**Gate Estrutural — invocar taxone-architect se:**
- 2+ packages afetados
- DDL necessario
- Cross-module (packages de modulos diferentes)
- Alteracao de JOINs, validacoes, PK/FK
Se nenhum criterio atendido (bug simples, 1 package): **SKIP** architect.

### Estagio 2.4: Registrar Causa Raiz (Automatica)

**Objetivo:** Salvar a causa raiz identificada no Estagio 2 em formato estruturado para o relatorio semanal.

**Condicao de entrada:** Estagio 2 concluido (com ou sem implementacao).

**Acao:** Salvar `tests/{WI_ID}/root_cause_entry.json` conforme schema `knowledge/root-cause/schema.json`.

Preencher com dados extraidos do diagnostico do developer:
- `root_cause.category`: `code_bug`, `performance`, `recompilation_gap`, etc.
- `root_cause.summary`: resumo de 1 linha da causa raiz
- `root_cause.originating_change`: Se identificado DDL/PR/commit que causou o problema
- `affected_objects`: packages/procedures/tabelas envolvidos
- `verdict`: `BUG_CONFIRMED`, `NOT_A_BUG`, etc.

**Nota:** NAO-BLOQUEANTE. Se falhar, logar e continuar.

---

### Estagio 2.4.1: Impact Assessment (Automatica)

**Objetivo:** Gerar avaliacao formal de impacto com risk score, arquivos afetados, dependencias cross-module e instrucoes de teste.

**Condicao de entrada:** Estagio 2 concluido com implementacao.

**Acao:** Gerar `tests/{WI_ID}/impact_assessment.json` seguindo o schema `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/impact-assessment-schema.json`.

Preencher a partir dos outputs do Estagio 2 (developer):
- `files_affected`: arquivos modificados pelo developer
- `tables_affected`: tabelas citadas no diagnostico
- `risk_score`: LOW (1 arquivo), MEDIUM (2-3), HIGH (cross-module/DDL), CRITICAL (>5 ou tabelas core)
- `structural`: geralmente false para bug fixes
- `test_instructions`: instrucoes derivadas da causa raiz
- `architect_recommendation`: PROCEED (maioria dos bugs) ou PROCEED_WITH_CAUTION (se cross-module)

**Decisao de fluxo:**
- `risk_score == "CRITICAL"`: Alertar usuario antes de prosseguir
- Demais: prosseguir normalmente

**Nota:** NAO-BLOQUEANTE. Se falhar, logar e continuar.

---

### Estagio 2.5: Enriquecer Cenarios de Teste

**Objetivo:** Extrair sugestoes de teste do developer e enriquecer test_scenarios.json.

**Condicao de entrada:** Estagio 2 concluido com implementacao bem-sucedida.

**Passo 1 - Extrair developer_suggestions do output do Estagio 2:**

Se o developer incluiu `### Sugestoes de Teste` no relatorio, extrair o JSON `developer_suggestions[]`.

**Passo 2 - Atualizar test_scenarios.json:**

```python
# Ler ou criar tests/{WI_ID}/test_scenarios.json
# Adicionar developer_suggestions como cenarios com source: "developer_suggestion"
# Salvar
```

**Passo 3 - Executar test_enricher (se branch disponivel):**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/test_enricher.py \
  --wi-id ${WI_ID} \
  --repo "$TAXONE_DW_REPO" \
  --branch MFS${WI_ID} \
  --format summary
```

Isto enriquece sql_hints, marca hotspots como critical, e recomenda suites XML.

**Nota:** Se nao houver branch ou repo, pular silenciosamente. Nao bloqueia o pipeline.

---

### Estagio 3: Review + Relatorio

**Objetivo:** Validar qualidade do codigo e gerar relatorio final.

**Agente: taxone-plsql-reviewer / taxone-pb-reviewer / taxone-java-reviewer** (conforme linguagem)

Selecionar reviewer conforme linguagem dos arquivos modificados no Estagio 2.
Se multiplas linguagens: lancar reviewers correspondentes em paralelo.

Instrucoes para o subagente:

```
Revisar o codigo implementado para correcao do bug:
{descricao_do_bug}

Arquivos criados/modificados:
{lista_de_arquivos}

Focar em:
1. Seguranca PL/SQL (SQL injection, grants, dados sensiveis)
2. Qualidade (exception handling, cursores, controle de transacao)
3. Performance (bulk collect, bind variables, indices)
4. Convencoes (nomenclatura, comentarios em portugues)
```

**Relatorio Final ao Desenvolvedor:**

```markdown
## Relatorio de Correcao - {titulo_do_bug}

### Root Cause
[Causa raiz tecnica com package:procedure:linha]

### Correcao Implementada
[Descricao da solucao aplicada]

### Arquivos Modificados
- `caminho/arquivo.sql:linha` - [o que mudou e por que]

### Scripts DDL (se aplicavel)
- [CREATE INDEX, ALTER TABLE, etc.]

### Resultado do Code Review
- Veredicto: [APROVADO / APROVADO COM RESSALVAS / REPROVADO]
- Issues encontradas: [lista se houver]

**Acao por veredicto:**
- **APROVADO:** Prosseguir para Estagio 3.3 (Compliance)
- **APROVADO COM RESSALVAS:** Apresentar ao dev, prosseguir se confirmar
- **REPROVADO:** Voltar ao Estagio 2 (max 3 loops → escalar TechLead)

### Impacto
- Modulos afetados: [lista]
- Performance: [impacto estimado]
- Rollback: [instrucoes para reverter se necessario]

### Tags Aplicadas
- [lista de tags SUST-IA-CLAUDE-* aplicadas durante o pipeline, se houver]

### Proximos Passos
- [ ] Testar em ambiente DEV
- [ ] Validar cenarios de regressao
- [ ] Criar PR no GitHub
```

**Tags automaticas durante o pipeline:**

- Se o developer identificar que precisa de **dados do cliente** ou **acesso a base do cliente** para diagnostico,
  adicionar automaticamente a tag `SUST-IA-CLAUDE-ANALISE` ao reportar no relatorio.
- Se a correcao envolver **nova regra de negocio** ou **alteracao de regra existente**
  (keywords: "nova regra", "alterar regra", "regra fiscal", "nova legislacao", "nova obrigacao", "configuracao tributaria"),
  adicionar automaticamente a tag `SUST-IA-CLAUDE-REGRA` ao reportar no relatorio.

### Estagio 3.3: Compliance Check (Gate GO/NO-GO)

**Objetivo:** Verificar seguranca e compliance do codigo antes de finalizar.

**Condicao de entrada:** Estagio 3 concluido (review feito).

**Passo 1 - Lancar taxone-compliance:**

```
Agent(subagent_type="taxone-compliance")
```

Prompt:
```
Verificar compliance dos arquivos alterados na WI #{WI_ID}.

Arquivos modificados:
{LISTA_ARQUIVOS_MODIFICADOS}

Repositorio: {TAXONE_DW_REPO}
Branch: MFS{WI_ID}
```

**Passo 2 - Processar resultado:**

Salvar output em `tests/{WI_ID}/compliance_report.json`.

- **PASS:** Prosseguir para Estagio 3.5 (Coverage Report)
- **PASS_WITH_WARNINGS:** Alertar desenvolvedor. Prosseguir se confirmar.
- **FAIL:** **BLOQUEAR.** Devolver ao Estagio 2 com instrucoes de correcao. Max 3 loops → escalar TechLead.

---

### Estagio 3.5: Coverage Report (Gate GO/NO-GO)

**Objetivo:** Gerar relatorio de cobertura de testes como gate de qualidade.

**Condicao de entrada:** Estagio 3.3 concluido (compliance OK).

**Passo 1 - Executar test_coverage_reporter:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/test_coverage_reporter.py \
  --wi-id ${WI_ID} \
  --tests-dir tests/${WI_ID}/ \
  --repo "$TAXONE_DW_REPO" \
  --branch MFS${WI_ID} \
  --format markdown
```

**Passo 2 - Avaliar veredicto:**

- **GO:** Prosseguir para Estagio 4 (Compound) ou finalizar.
- **CONDITIONAL GO:** Apresentar gaps ao desenvolvedor, prosseguir com warning.
- **NO-GO:** Informar gaps criticos. Sugerir retornar ao Estagio 2 para testes adicionais.

**Passo 3 - Incluir no relatorio final:**

Adicionar secao de cobertura ao relatorio do Estagio 3:
```markdown
### Cobertura de Testes
- Veredicto: {GO/CONDITIONAL GO/NO-GO}
- Cenarios cobertos: {X}/{Y}
- Tabelas testadas: {X}/{Y}
- Procedures exercitadas: {X}/{Y}
- Gaps: {lista ou "nenhum"}
```

**Nota:** Se nao houver diretorio de testes ou evidencias, gerar relatorio baseline com NO-GO.
O relatorio e salvo automaticamente em `tests/{WI_ID}/coverage_report.json`.

#### REGRA: Evidencias de Teste OBRIGATORIAS

**NUNCA concluir uma WI sem anexar evidencias de teste.** Se rodou teste, DEVE anexar na WI e postar na Discussion.

1. **Executar testes de validacao** e salvar resultados em `tests/{WI_ID}/`
2. **Upload de TODOS os arquivos** de `tests/{WI_ID}/` como Attachments na WI via API (`_apis/wit/attachments`)
3. **Postar Discussion comment** com tabela de resultados (PASS/FAIL/SKIP) e resumo consolidado

**Motivo:** Na WI #1086591, evidencias de teste foram esquecidas — regra adicionada para garantir que nunca mais ocorra.

#### REGRA: AI Powered OBRIGATORIO

**SEMPRE setar `TR.WOW.AIPowered` = `"true"`** em toda WI processada pelo pipeline.
Incluir no PATCH junto com os demais campos (tags, root cause, release notes, etc.).

#### REGRA: Description of Root Cause OBRIGATORIO

**SEMPRE preencher o campo `Custom.DescriptionofRootCause`** ao concluir a analise/implementacao.

- Para bugs: descrever exatamente o que causava o problema e onde no codigo
- Texto descritivo, pode usar `<br>` para quebras de linha, sem HTML complexo
- Tambem verificar `Custom.RootCauseList` e `Custom.ExpectedCauseofProblem` se aplicaveis
- **NUNCA esquecer este campo** — ele e cobrado na revisao da WI

---

### Estagio 3.6: Geracao de Dados SAFX (Auto-detect)

**Objetivo:** Gerar flat-files SAFX de teste para importacao em outros ambientes (QA/RC).
Quando nao existe cenario SuiteAutomation para o componente, SAFX e gerada automaticamente
para garantir que o teste seja portavel entre ambientes.

**Passo 1 - Verificar cobertura SuiteAutomation:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/safx_auto_generator.py --wi-id ${WI_ID} --env LOCAL
```

O script:
1. Detecta packages modificados no branch `MFS{WI_ID}` via `git diff`
2. Consulta `component-test-map.json` — se existe cenario SuiteAutomation, retorna `SUITE_EXISTS` (suite ja cobre)
3. Se NAO existe cenario: detecta tabelas SAFX via `ALL_DEPENDENCIES` + `safx-table-index.json`
4. Gera flat-files pipe-delimited + SQL INSERTs em `tests/{WI_ID}/safx_files/`
5. Gera `test_data_manifest.json` com isolation marker
6. Executa `safx_archiver.py` para archive RC

**Resultados possiveis:**
- `SUITE_EXISTS` — cenario SuiteAutomation encontrado, SAFX nao necessaria (prosseguir para Suite)
- `GENERATED` — flat-files SAFX gerados com sucesso
- `NO_SAFX` — packages nao referenciam tabelas SAFX (prosseguir normalmente)
- `NO_PACKAGES` — nenhum package PL/SQL detectado no branch

**Passo 2 - Validar output (se GENERATED):**
- Verificar que `tests/{WI_ID}/safx_files/` contem `.txt` flat-files
- Verificar que `test_data_manifest.json` foi gerado

---

### Estagio 3.8: Archival SAFX para RC (Condicional)

**Objetivo:** Exportar dados SAFX do banco com formatacao SAF_EXPORTA_TAB para reproducao em RC.

**Condicao de entrada:** `tests/{WI_ID}/safx_files/` existe com flat-files gerados no Estagio 3.6.

Se nao existe `tests/{WI_ID}/safx_files/`: **SKIP este estagio**.

**Passo 1 - Executar safx_archiver:**

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python scripts/safx_archiver.py --wi-id ${WI_ID} --env LOCAL
```

**Passo 2 - Upload para ADO:**
- Anexar todos os arquivos de `tests/{WI_ID}/safx_archive_rc/` como Attachments na WI
- Postar Discussion comment com lista de arquivos e instrucoes de importacao RC

---

### Estagio 3.9: Publicar Cenarios no Repo QA (OBRIGATORIO)

**Objetivo:** Publicar artefatos de teste em `cenarios/{WI_ID}/` no repo `taxone_automacao_qa` para reproducao em QA/RC.

**SEMPRE executar** apos testes bem-sucedidos. Artefatos devem ser portaveis entre ambientes.

**Passo 1 - Copiar artefatos:**
```bash
mkdir -p /c/@@Dev/Git/taxone_automacao_qa/cenarios/${WI_ID}
cp tests/${WI_ID}/* /c/@@Dev/Git/taxone_automacao_qa/cenarios/${WI_ID}/
```

**Passo 2 - Criar branch, commit e push:**
```bash
cd /c/@@Dev/Git/taxone_automacao_qa
git fetch origin && git checkout -b MFS${WI_ID} origin/dev
git add cenarios/${WI_ID}/
git commit -m "MFS${WI_ID} - Cenarios de teste"
git push -u origin MFS${WI_ID}
```

**Passo 3 - Criar PR:**
```bash
gh pr create --base dev --title "[DEV] MFS${WI_ID} - Cenarios de teste" --body "Cenarios de teste para WI #${WI_ID}\n\nAB#${WI_ID}"
```

**Alternativa:** Usar `python scripts/qa_test_publisher.py --wi-id ${WI_ID}` (requer `test_data_manifest.json`).

---

### Estagio 4: Compound (Opcional)

**Objetivo:** Documentar a solucao como conhecimento reutilizavel.

Executar se o bug atender a QUALQUER criterio:
- Investigacao levou mais de 15 minutos
- Causa raiz nao era obvia
- Pattern de bug pode se repetir em outro modulo
- Mudanca envolveu multiplas camadas (PL/SQL + View + Tabela)

Usar a skill `taxone-compound` para gerar documentacao da solucao.

---

## Exemplos de Uso

```
/taxone-bug-fix Calculo de ICMS-ST gerando valor incorreto quando aliquota interestadual e zero
/taxone-bug-fix Erro na apuracao de PIS/COFINS para empresas do Simples Nacional
/taxone-bug-fix View de consulta de notas fiscais nao retornando registros cancelados
/taxone-bug-fix Procedure de importacao travando com timeout em arquivos grandes
/taxone-bug-fix Trigger de auditoria nao registrando alteracoes em lote via FORALL
```

---

## Fluxo Visual

```
[Bug Report]
     |
     v
[E1: Knowledge + Alinhamento] --> Interacao com Dev (UNICO ponto)
     |
     v
[E2: Explorar + Diagnosticar + Corrigir] --> taxone-developer (+ taxone-dba se performance)
     |
     v
[E3: Review + Relatorio] --> taxone-reviewer --> Relatorio Final
     |
     v
[E3.6: SAFX Gerados] --> (condicional) taxone-test-data-engineer --> flat-files SAFX
     |
     v
[E3.8: Archival RC] --> (condicional) safx_archiver.py --> Upload ADO
     |
     v
[E4: Compound] --> (opcional) taxone-compound --> Doc reutilizavel
```
