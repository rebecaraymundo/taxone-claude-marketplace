---
name: taxone-feature-dev
description: >
  Pipeline generico de desenvolvimento de features e correcao de bugs no TAX ONE.
  Orquestra 11 agentes especializados em 14 fases: Brainstorming (escopo + alternativas + HARD GATE) →
  Design Spec → Cenarios de Teste → Arquitetura → DBA → Plano → Implementacao →
  Cobertura de Regras → Testes SQL → SuiteAutomation → E2E Playwright → Explorer Visual →
  Code Review → Compound Engineering.
  Sem integracao ADO — foco em codigo e qualidade.
version: 2.1.0
---

# taxone-feature-dev v2.1

Pipeline generico de desenvolvimento para o projeto **TAX ONE** (Mastersaf Fiscal Solutions).
Diferente do `taxone-auto-fix` e `taxone-us-auto-implement`, este pipeline NAO integra
com Azure DevOps. E focado exclusivamente em desenvolvimento local com agentes especializados.

**Novidades v2:** Geracao de cenarios de teste, 4 camadas de teste (SQL + SuiteAutomation +
E2E Playwright + Explorer Visual), compilacao DBA obrigatoria, suporte Angular, verificacao
de cobertura de regras e Compound Engineering.

---

## Agentes Disponiveis

| Agente | Funcao | Ferramentas | Tipo |
|--------|--------|-------------|------|
| **taxone-architect** | Analise de impacto, design, regras de negocio | Read, Grep, Glob | Read-only |
| **taxone-plsql** | Implementacao PL/SQL (packages, procedures, views) | Read, Write, Edit, Bash, Grep, Glob | Read-write |
| **taxone-pb** | Implementacao PowerBuilder (DataWindows, scripts) | Read, Write, Edit, Bash, Grep, Glob | Read-write |
| **taxone-java** | Implementacao Java (web services, Jasper, servlets) | Read, Write, Edit, Bash, Grep, Glob | Read-write |
| **taxone-angular** | Implementacao + Review Angular 11 frontend | Read, Write, Edit, Bash, Grep, Glob | Read-write |
| **taxone-dba** | Analise Oracle, performance, DDL, compilacao | Read, Write, Edit, Grep, Glob | Read-write |
| **taxone-plsql-reviewer** | Code review PL/SQL Oracle | Read, Grep, Glob | Read-only |
| **taxone-pb-reviewer** | Code review PowerBuilder | Read, Grep, Glob | Read-only |
| **taxone-java-reviewer** | Code review Java | Read, Grep, Glob | Read-only |
| **taxone-tester** | Scripts SQL de validacao, roteiros manuais | Read, Write, Edit, Bash, Grep, Glob | Read-write |
| **taxone-suite-runner** | Testes de regressao SuiteAutomation (Java) | Read, Bash, Grep, Glob | Read-only |
| **taxone-e2e-tester** | Testes E2E Playwright (browser) | Read, Bash, Grep, Glob | Read-only |
| **taxone-explorer** | Teste exploratorio visual (browser + screenshots) | Bash, Read, Write, Glob, Grep | Read-write |
| **taxone-sm** | Alocacao de Dev/Tester por especialidade | Read, Grep, Glob, Bash | Read-only |

---

## Regras

### R1 - Usar APENAS os agentes deste plugin
Os UNICOS agentes que podem ser lancados sao os listados na tabela acima. NUNCA usar agentes externos.

### R2 - Compilacao PL/SQL no banco
PL/SQL DEVE ser compilado no banco Oracle via taxone-dba ANTES de qualquer teste.
Conexao: `V2R010AC/V2R010AC@localhost:1521/MFSPDB`. NUNCA porta 1523.

### R3 - Pausar entre fases
Reportar progresso entre cada fase e aguardar confirmacao do usuario para prosseguir.

### R4 - Knowledge primeiro
SEMPRE carregar knowledge relevante antes de iniciar qualquer fase de analise ou implementacao.

### R5 - Encoding PL/SQL
Arquivos PL/SQL sao ISO-8859-1 com CRLF. Usar Python binary replacement, NUNCA Edit tool.

### R6 - Testes sao locais
Artefatos de teste ficam em `tests/{feature-name}/` e NUNCA sobem para Git.

### Regra de Visibilidade do Knowledge
Sempre que qualquer agente for ler um arquivo em `${CLAUDE_PLUGIN_ROOT}/knowledge/`,
ANTES de usar Read, deve imprimir:
```
> [Knowledge] Carregando: {nome-do-arquivo} - {descricao-breve}
```

---

## Pipeline de Execucao — Visao Geral

```
Fase 1    Brainstorming e Alinhamento (knowledge + escopo + alternativas + HARD GATE)
Fase 1.2  Design Spec Document (spec + self-review + aprovacao)
Fase 1.5  Geracao de Cenarios de Teste (test_scenarios.json)
Fase 2    Analise Arquitetural (architect)
Fase 2.5  Analise DBA Oracle (condicional)
Fase 3    Plano de Implementacao (consolidacao + aprovacao)
Fase 4    Implementacao (developer / angular)
Fase 4.5  Verificacao de Cobertura de Regras (architect)
Fase 5    Compilacao DBA + Testes SQL (dba + tester)
Fase 5.3  Testes de Regressao SuiteAutomation (suite-runner)
Fase 5.5  Testes E2E Playwright (e2e-tester)
Fase 5.7  Teste Exploratorio Visual (explorer)
Fase 6    Code Review (reviewer)
Fase 7    Resumo Final + Compound Engineering
```

---

## Principios de Brainstorming

- **Uma pergunta por vez** — nao sobrecarregar o usuario
- **Multipla escolha sempre que possivel** — mais facil responder
- **YAGNI** — remover features e complexidade desnecessarias de todas as propostas
- **Explorar alternativas** — SEMPRE propor 2-3 abordagens antes de decidir
- **Validacao incremental** — apresentar design, obter aprovacao, depois avancar
- **Decompor quando grande** — se a demanda cobre subsistemas independentes, dividir
- **Design antes de codigo** — NUNCA implementar sem spec aprovado (Hard Gate)

---

### Fase 1 - Brainstorming e Alinhamento

**Objetivo:** Entender o escopo da demanda, explorar alternativas e alinhar a abordagem com o usuario.

**Passos:**

1. **Carregar knowledge obrigatorio:**
   - `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/overview.md`
   - `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/patterns.md`
   - `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/code-standards.md`
   - `${CLAUDE_PLUGIN_ROOT}/knowledge/process/DEFINITION_OF_DONE.md`

2. **Buscar knowledge da feature:**
   - Verificar `${CLAUDE_PLUGIN_ROOT}/knowledge/features/` por documentacao relevante
   - Buscar em `${CLAUDE_PLUGIN_ROOT}/knowledge/business-rules/` regras do modulo
   - Consultar `${CLAUDE_PLUGIN_ROOT}/knowledge/schema/MODULE_MAP.md` para mapear prefixo DB → modulo

3. **Identificar tecnologia:**
   - Se envolve tela web / Angular → marcar para usar `taxone-angular` na Fase 4
   - Se envolve PL/SQL → marcar para usar `taxone-plsql` na Fase 4
   - Se envolve PowerBuilder → marcar para usar `taxone-pb` na Fase 4
   - Se envolve Java / Jasper → marcar para usar `taxone-java` na Fase 4

4. **Avaliar escopo:**
   - Antes de perguntar detalhes, avaliar se a demanda descreve multiplos subsistemas independentes
   - Se a demanda toca >3 modulos independentes OU >2 tecnologias sem relacao → sugerir decomposicao em sub-projetos
   - Se sim: listar sub-projetos, dependencias entre eles, e priorizar o primeiro
   - Se nao: prosseguir normalmente

5. **Perguntas clarificadoras (uma por vez):**
   - Preferir multipla escolha quando possivel
   - Foco: proposito, restricoes, criterios de sucesso, impacto em fluxos existentes
   - Maximo 5 perguntas antes de propor abordagens
   - Usar `AskUserQuestion` para cada pergunta

6. **Propor 2-3 abordagens com trade-offs:**

   ```markdown
   ## Abordagens Propostas

   ### Opcao A: {nome} (Recomendada)
   - **Descricao:** {como resolve}
   - **Pros:** {beneficios}
   - **Contras:** {riscos/limitacoes}
   - **Complexidade:** {Baixa/Media/Alta}
   - **Impacto regressao:** {Minimo/Moderado/Alto}

   ### Opcao B: {nome}
   - **Descricao:** {como resolve}
   - **Pros:** {beneficios}
   - **Contras:** {riscos/limitacoes}
   - **Complexidade:** {Baixa/Media/Alta}
   - **Impacto regressao:** {Minimo/Moderado/Alto}

   ### Recomendacao
   {por que a opcao A e a melhor — aplicar YAGNI: remover complexidade desnecessaria}
   ```

   - Liderar com a abordagem recomendada e explicar por que
   - Aplicar YAGNI: remover features/complexidade desnecessaria de TODAS as opcoes

7. **Apresentar entendimento consolidado:**

   ```markdown
   ## Fase 1 - Entendimento

   ### Demanda
   {descricao da demanda conforme entendida}

   ### Tecnologia Detectada
   {PL/SQL / PowerBuilder / Java / Angular / Misto}

   ### Modulos/Packages Provavelmente Envolvidos
   {lista baseada no knowledge}

   ### Abordagem Escolhida
   {Opcao A/B/C — resumo da abordagem aprovada}

   ### Knowledge Carregado
   - {lista de arquivos}
   ```

8. **HARD GATE — Aguardar aprovacao** via `AskUserQuestion`.
   - NAO prosseguir para Fase 1.2 sem aprovacao explicita da abordagem
   - Se o usuario pedir ajustes, voltar ao passo 5 ou 6 conforme necessario

---

### Fase 1.2 - Design Spec Document

**Objetivo:** Documentar o design aprovado em spec persistente e commitavel.

**Passos:**

1. **Gerar spec document** em `docs/specs/{feature-name}-design.md`:

   ```markdown
   # Design Spec: {feature-name}

   **Data:** {YYYY-MM-DD}
   **Demanda:** {descricao}
   **Abordagem escolhida:** {Opcao A/B/C}

   ## Escopo
   {o que esta IN e OUT}

   ## Arquitetura
   {componentes afetados, fluxo de dados, camadas (PL/SQL, DDL, PB, Java, Angular)}

   ## Regras de Negocio
   {regras identificadas, R01..Rnn, com descricao e tabelas/packages afetados}

   ## Tabelas e Packages
   {mapeamento modulo → objetos DB}

   ## Riscos
   {riscos identificados + mitigacoes}

   ## YAGNI — Excluido do Escopo
   {features/complexidade removidas deliberadamente e por que}
   ```

2. **Self-review do spec (automatico):**
   - **Placeholder scan:** Algum "TBD", "TODO", secao vazia? → Preencher
   - **Consistencia interna:** Secoes contradizem entre si? → Corrigir
   - **Escopo:** Focado o suficiente para um plano unico? → Se nao, decompor
   - **Ambiguidade:** Algum requisito interpretavel de 2 formas? → Explicitar uma e documentar

3. **Apresentar spec ao usuario:**
   > "Spec gerado em `docs/specs/{feature-name}-design.md`. Revise e me avise se quer ajustar algo antes de gerar os cenarios de teste."

4. **Aguardar aprovacao** — so prosseguir para Fase 1.5 apos usuario confirmar.
   - Se houver alteracoes: atualizar o spec, re-executar self-review, re-apresentar.

---

### Fase 1.5 - Geracao de Cenarios de Teste

**Objetivo:** Gerar cenarios de teste estruturados ANTES da implementacao para guiar todas as camadas de teste.

**Logica:** Extrair cenarios da descricao da demanda, business rules e knowledge carregado.

**Passos:**

1. Ler business rules do modulo envolvido (`knowledge/business-rules/{modulo}/`)
2. Consultar `knowledge/suite-automation/playwright-test-map.json` para mapear tela → specs E2E
3. Gerar `tests/{feature-name}/test_scenarios.json` com o schema padrao:

```json
{
  "version": "1.0.0",
  "feature_name": "{nome-da-feature}",
  "generated_by": "taxone-feature-dev",
  "generated_at": "{ISO-8601}",
  "module": "{modulo}",
  "vertical": "{vertical}",
  "screen": {
    "menu_path": "{caminho do menu}",
    "mapping_id": "{ID do playwright-test-map}",
    "e2e_specs": ["{spec1.ts}", "{spec2.ts}"]
  },
  "tables_involved": ["{tabela1}", "{tabela2}"],
  "packages_involved": ["{package1}"],
  "scenarios": [
    {
      "id": "S01",
      "type": "happy_path|negative|edge_case|regression|data_integrity|performance",
      "title": "{titulo descritivo}",
      "preconditions": ["{pre-condicao}"],
      "steps": ["{passo 1}", "{passo 2}"],
      "expected_result": "{resultado esperado}",
      "sql_hint": "{fragmento SQL ou null}",
      "e2e_grep": "{string para --grep ou null}",
      "priority": "P1|P2|P3"
    }
  ],
  "enrichments": []
}
```

4. Gerar no minimo:
   - 1-2 cenarios `happy_path` (fluxo principal funciona)
   - 1 cenario `negative` (erros sao tratados)
   - 1 cenario `edge_case` (limites e excecoes)
   - 1 cenario `regression` (funcionalidades existentes nao quebraram)

5. Apresentar resumo: `{N} cenarios gerados: {X} happy_path, {Y} negative, {Z} edge_case, {W} regression`

---

### Fase 2 - Analise Arquitetural

**Objetivo:** Mapear impacto e propor design da solucao.

**Lancar taxone-architect:**

```
## Demanda: {descricao}

### Knowledge Relevante
{resumo do knowledge carregado}

### Cenarios de Teste Gerados (Fase 1.5)
{resumo dos cenarios — tipos e cobertura}

### Sua Tarefa
1. Carregar knowledge da feature (OBRIGATORIO)
2. Mapear packages, procedures, views, triggers e tabelas afetadas
3. Propor design da solucao seguindo patterns existentes
4. Executar analise de impacto em regras de negocio (se aplicavel)
5. Entregar no formato padrao: Analise de Impacto + Design Proposto + Riscos + Sequencia
6. Enriquecer cenarios de teste: append em enrichments[] com cenarios de regressao
   para funcoes irmas e data integrity para downstream
```

**Apresentar resultado e aguardar aprovacao do plano.**

---

### Fase 2.5 - Analise DBA Oracle (Condicional)

**Executar quando:** A demanda envolver DDL, queries complexas, indices, particionamento,
tabelas com mais de 50 colunas, ou potencial impacto de performance.

**Lancar taxone-dba:**

```
## Demanda: {descricao}

### Design Proposto pelo Architect
{resumo do design}

### Sua Tarefa
1. Analisar impacto Oracle: performance, indices, particionamento, explain plan
2. Se envolver DDL, gerar scripts com rollback (nome: DDL_{feature-name}.sql)
3. NUNCA alterar DDL existente — sempre criar nova
4. Validar constraints e FKs cross-module
5. Reportar: APROVADO / APROVADO COM RESSALVAS / REPROVADO
```

---

### Fase 3 - Plano de Implementacao

**Objetivo:** Consolidar analises e apresentar plano detalhado ao usuario.

```markdown
## Fase 3 - Plano de Implementacao

### Tecnologia
{PL/SQL / Angular / Misto}

### Arquivos a Modificar
| Arquivo | Tipo | Alteracao |
|---------|------|-----------|
| {arquivo} | {PL/SQL/PB/Java/Angular/DDL/Jasper} | {descricao} |

### Sequencia
1. {passo 1}
2. {passo 2}

### Riscos
- {risco}: {mitigacao}

### DDL (se aplicavel)
- {scripts DDL}

### Cenarios de Teste
- {N} cenarios em test_scenarios.json
- E2E specs mapeadas: {specs}

Confirmar plano para iniciar implementacao?
```

**Aguardar confirmacao.**

---

### Fase 4 - Implementacao

**Selecionar agente pela tecnologia:**
- **PL/SQL** (packages, procedures, views) → Lancar `taxone-plsql`
- **PowerBuilder** (DataWindows, scripts) → Lancar `taxone-pb`
- **Java / Jasper** (servlets, web services) → Lancar `taxone-java`
- **Angular 11 frontend** → Lancar `taxone-angular`
- **Misto**: PL/SQL + PB → sequencial (PL/SQL primeiro); PL/SQL + Java → paralelo; + Angular → paralelo

**Prompt para o agente:**

```
## Demanda: {descricao}

### Plano Aprovado
{plano detalhado com arquivos e sequencia}

### Knowledge Relevante
{resumo}

### Sua Tarefa
1. Carregar knowledge da feature (OBRIGATORIO)
2. Implementar conforme plano aprovado
3. Seguir padroes do projeto (code-standards.md, naming.md)
4. Alterar SOMENTE o minimo necessario
5. Se envolver DDL, gerar scripts separados (DDL_{feature-name}.sql)
6. PL/SQL: preservar encoding ISO-8859-1 + CRLF (usar Python binary replacement)
7. Reportar: arquivos modificados, descricao das mudancas
```

**Apresentar resultado da implementacao.**

---

### Fase 4.5 - Verificacao de Cobertura de Regras

**Executar quando:** A implementacao envolver alteracao de JOINs, valores default (NVL),
validacoes, constraints, campos PK/FK, ou novas regras de negocio.

**Lancar taxone-architect:**

```
## Verificacao de Cobertura de Regras

### Implementacao Realizada
{descricao das mudancas — arquivos e linhas}

### Cenarios de Teste (test_scenarios.json)
{lista de cenarios}

### Sua Tarefa
1. Rastrear fluxo downstream (quais funcoes/telas consomem o que foi alterado)
2. Verificar constraints e validacoes
3. Mapear valores default/NVL alterados
4. Verificar funcoes irmas (mesma tabela/package)
5. Verificar se cenarios de teste cobrem todos os impactos
6. Se faltar cobertura: sugerir cenarios adicionais para test_scenarios.json
7. Entregar decisao GO/NO-GO com justificativa
```

- **GO:** Prosseguir para Testes
- **NO-GO:** Apresentar riscos e ajustar implementacao (voltar Fase 4)

---

### Fase 5 - Compilacao DBA + Testes SQL

**Passo 1 — Compilacao obrigatoria (se houver PL/SQL alterado):**

Lancar `taxone-dba`:

```
## Compilacao PL/SQL

### Arquivos Modificados
{lista de .sql / .pkb / .pks / .trg}

### Sua Tarefa
1. Compilar TODOS os objetos PL/SQL alterados no banco Oracle
2. Conexao: V2R010AC/V2R010AC@localhost:1521/MFSPDB (SOMENTE porta 1521)
3. Verificar se compilou sem erros (SHOW ERRORS)
4. Reportar: COMPILADO OK / ERRO DE COMPILACAO (com detalhes)
```

**IMPORTANTE:** Se compilacao falhar, voltar para Fase 4 para corrigir.

**Passo 2 — Testes SQL de validacao:**

Lancar `taxone-tester`:

```
## Testes SQL de Validacao

### Demanda: {descricao}

### Cenarios de Teste
{conteudo do test_scenarios.json}

### Arquivos Modificados
{lista}

### Sua Tarefa
1. Ler test_scenarios.json e usar como esqueleto
2. Expandir cada sql_hint em query completa de validacao
3. Gerar scripts SQL: setup, validacao por cenario, cleanup
4. Gerar roteiro manual de teste se aplicavel
5. Salvar em tests/{feature-name}/
6. Reportar: {N} scripts gerados, cenarios cobertos
```

---

### Fase 5.3 - Testes de Regressao SuiteAutomation (Condicional)

**Executar quando:** A demanda envolver alteracoes em packages PL/SQL que tem suites
de teste mapeadas no `knowledge/suite-automation/component-test-map.json`.

**Lancar taxone-suite-runner:**

```
## Teste de Regressao SuiteAutomation

### Packages Alterados
{lista de packages}

### Sua Tarefa
1. Consultar component-test-map.json para identificar suites aplicaveis
2. Executar suite_runner.py com as suites mapeadas
3. Comparar expected vs obtained (encoding ISO-8859-1)
4. Reportar: PASS / FAIL com detalhes de divergencia
```

- **PASS:** Prosseguir
- **FAIL:** Apresentar divergencias ao usuario

---

### Fase 5.5 - Testes E2E Playwright (Condicional)

**Executar quando:** Existirem cenarios com `e2e_grep` nao-nulo no test_scenarios.json
OU a demanda envolver alteracoes em telas/relatorios.

**Lancar taxone-e2e-tester:**

```
## Testes E2E Playwright

### Cenarios de Teste com E2E
{cenarios filtrados onde e2e_grep != null}

### Specs Mapeadas
{screen.e2e_specs do test_scenarios.json}

### Sua Tarefa
1. Ler test_scenarios.json e coletar e2e_grep nao-nulos
2. Usar screen.e2e_specs para spec files
3. Executar playwright_runner.py com --grep-describe derivado dos cenarios
4. Se nenhum cenario tem e2e_grep, usar fluxo baseado em scoring do playwright-test-map.json
5. Reportar: specs executadas, PASS/FAIL, screenshots se falha
```

---

### Fase 5.7 - Teste Exploratorio Visual (Condicional)

**Executar quando:** A demanda envolver telas, relatorios visuais, ou componentes UI
que precisam validacao visual humana.

**Lancar taxone-explorer:**

```
## Teste Exploratorio Visual

### Cenarios de Teste
{cenarios do test_scenarios.json}

### Menu Path
{screen.menu_path do test_scenarios.json}

### Sua Tarefa
1. Usar screen.menu_path para navegacao direta (sem descoberta)
2. Iterar sobre scenarios[].steps como acoes da exploracao
3. Capturar screenshots em cada passo relevante
4. Validar expected_result visualmente em cada cenario
5. Salvar screenshots em tests/{feature-name}/explore_*.png
6. Gerar exploratory_report.md com resultado consolidado
```

---

### Fase 6 - Code Review

**Lancar reviewer especializado** (`taxone-plsql-reviewer` / `taxone-pb-reviewer` / `taxone-java-reviewer` conforme linguagem, em paralelo se multiplas):

```
## Code Review - {descricao da demanda}

### Arquivos Modificados
{lista com tipo: PL/SQL, Angular, Java, DDL, Jasper}

### Resultados dos Testes
- SQL: {resultado}
- SuiteAutomation: {resultado ou N/A}
- E2E Playwright: {resultado ou N/A}
- Explorer: {resultado ou N/A}

### Sua Tarefa
Revisar TODOS os arquivos modificados:
1. Carregar knowledge de convencoes (OBRIGATORIO)
2. Seguranca: SQL injection, XSS (Angular), grants, permissoes
3. Qualidade: excecoes, cursores, transacoes, memory leaks
4. Performance Oracle: full scans, indices, explain plan
5. Convencoes do projeto (code-standards.md, naming.md)
6. Encoding: PL/SQL em ISO-8859-1 (NUNCA UTF-8)
7. Veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO
```

- **APROVADO:** Prosseguir para resumo
- **RESSALVAS:** Apresentar ao usuario
- **REPROVADO:** Voltar para Fase 4

---

### Fase 7 - Resumo Final + Compound Engineering

**Passo 1 — Resumo:**

```markdown
## Resumo Final

### Demanda
{descricao}

### Tecnologia
{PL/SQL / Angular / Misto}

### Arquivos Modificados
| Arquivo | Tipo | Alteracao |
|---------|------|-----------|
| {arquivo} | {tipo} | {descricao} |

### DDL (se aplicavel)
{scripts}

### Code Review
- Veredicto: {resultado}
- Issues: {resumo}

### Cobertura de Regras
- Decisao: {GO/NO-GO/N/A}

### Testes Executados
| Camada | Status | Detalhes |
|--------|--------|----------|
| SQL Validacao | {OK/FAIL/N/A} | {N scripts, M cenarios} |
| SuiteAutomation | {PASS/FAIL/N/A} | {suites executadas} |
| E2E Playwright | {PASS/FAIL/N/A} | {specs executadas} |
| Explorer Visual | {OK/N/A} | {screenshots capturadas} |

### Cenarios de Teste
- Total: {N} cenarios em test_scenarios.json
- Cobertos: {M} / {N}

### Proximos Passos
1. Revisar mudancas
2. Testar em ambiente DEV
3. Commit e PR (se desejado)

### Fases Executadas
| Fase | Status |
|------|--------|
| 1 - Brainstorming | OK — Abordagem {A/B/C} aprovada |
| 1.2 - Design Spec | docs/specs/{name}-design.md |
| 1.5 - Cenarios de Teste | {N} cenarios |
| 2 - Arquitetura | OK |
| 2.5 - DBA | {OK/Pulado} |
| 3 - Plano | Aprovado |
| 4 - Implementacao | {developer/angular/ambos} |
| 4.5 - Cobertura Regras | {GO/NO-GO/Pulado} |
| 5 - Compilacao + SQL | {OK/FAIL} |
| 5.3 - SuiteAutomation | {PASS/FAIL/Pulado} |
| 5.5 - E2E Playwright | {PASS/FAIL/Pulado} |
| 5.7 - Explorer Visual | {OK/Pulado} |
| 6 - Code Review | {Aprovado/Ressalvas/Reprovado} |
| 7 - Resumo + Compound | OK |
```

**Passo 2 — Compound Engineering:**

Documentar a solucao no knowledge base para reutilizacao futura:

```
Gerar knowledge/solutions/{feature-name}.md com:
- Titulo e descricao da feature
- Root cause / motivacao
- Solucao implementada (arquivos, tecnica)
- Regras de negocio afetadas
- Tabelas e packages envolvidos
- Cenarios de teste criados
- Licoes aprendidas

Atualizar knowledge/solutions/INDEX.md com entrada nova.
```

**Aguardar confirmacao** antes de gravar no knowledge base.

---

## Notas Tecnicas

- Este pipeline NAO integra com Azure DevOps (sem busca de WIs, sem update de tags)
- Para integracao ADO, usar `/taxone-auto-fix` (bugs) ou `/taxone-us-auto-implement` (USs)
- Commit e PR sao opcionais — o pipeline reporta as mudancas e o usuario decide
- Encodificacao: PL/SQL files em ISO-8859-1 com CRLF — usar Python binary replacement
- Compilacao PL/SQL e OBRIGATORIA antes de qualquer teste (via taxone-dba, porta 1521)
- Artefatos de teste ficam em `tests/{feature-name}/` e NUNCA sobem para Git
- Fases condicionais (2.5, 4.5, 5.3, 5.5, 5.7) podem ser puladas conforme contexto
- O pipeline detecta automaticamente se precisa Angular ou PL/SQL pela descricao da demanda
