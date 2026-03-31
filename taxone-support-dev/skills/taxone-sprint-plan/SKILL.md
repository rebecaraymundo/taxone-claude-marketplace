---
name: taxone-sprint-plan
description: >
  Pipeline automatizado de Sprint Planning para o TAX ONE. Busca WIs do ADO,
  descobre especializacoes do time via historico, estima story points, aloca
  devs/testers por afinidade de modulo e apresenta sprint board com
  balanceamento de carga. Suporta modo sprint completa e alocacao avulsa.
version: 1.0.0
---

# TAX ONE - Pipeline de Sprint Planning

Pipeline orquestrado para planejamento de sprints do TAX ONE (Mastersaf Fiscal Solutions)
da Thomson Reuters. Busca WIs do Azure DevOps, estima story points com base em historico,
aloca desenvolvedores e testers por afinidade de modulo e balanceia a carga do time.

---

## Indice

1. [Configuracao](#configuracao)
2. [Regras (R1-R6)](#regras)
3. [Pipeline - Visao Geral](#pipeline---visao-geral)
4. [Phase 0 - Validacao e Setup](#phase-0---validacao-e-setup)
5. [Phase 0.5 - Descoberta de Especializacoes](#phase-05---descoberta-de-especializacoes)
6. [Phase 1 - Buscar Work Items](#phase-1---buscar-work-items)
7. [Phase 1.5 - Verificar Campos ADO](#phase-15---verificar-campos-ado)
8. [Phase 2 - Ordenacao](#phase-2---ordenacao)
9. [Phase 3 - Estimativa](#phase-3---estimativa)
10. [Phase 4 - Alocacao](#phase-4---alocacao)
11. [Phase 5 - Sprint Board](#phase-5---sprint-board)
12. [Phase 6 - Aplicar no ADO](#phase-6---aplicar-no-ado)

---

## Configuracao

### Variaveis de Ambiente (Obrigatorias)

| Variavel  | Descricao                            |
|-----------|--------------------------------------|
| `ADO_PAT` | Personal Access Token do Azure DevOps |

### Constantes do Pipeline

| Constante              | Valor                                                                 |
|------------------------|-----------------------------------------------------------------------|
| ADO Org                | `tr-ggo`                                                              |
| ADO Project            | `Mastersaf Fiscal Solutions` (URL: `Mastersaf%20Fiscal%20Solutions`)   |
| ADO API Version        | `api-version=7.1`                                                     |
| ADO Base URL           | `https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions`         |
| Area Path              | `Mastersaf Fiscal Solutions\MFS\TAX ONE\Suporte`                      |
| Knowledge Path         | `${CLAUDE_PLUGIN_ROOT}/knowledge/`                                    |
| Team Roster            | `${CLAUDE_PLUGIN_ROOT}/knowledge/team/TEAM_ROSTER.json`               |
| Team Specializations   | `${CLAUDE_PLUGIN_ROOT}/knowledge/team/TEAM_SPECIALIZATIONS.json`      |
| Module Map             | `${CLAUDE_PLUGIN_ROOT}/knowledge/triage/MODULE_KNOWLEDGE_MAP.json`    |
| ADO Guide              | `${CLAUDE_PLUGIN_ROOT}/references/ado-api-guide.md`                   |

### Agentes Permitidos

| Agente       | Funcao                              | Fase       |
|--------------|-------------------------------------|------------|
| `taxone-sm`  | Sprint Planning, SP, Alocacao       | Todas      |

---

## Regras

### R1 - Usar APENAS o agente taxone-sm

O UNICO agente que pode ser lancado e: `taxone-sm`

**PROIBIDO** invocar qualquer outro agente.

### R2 - Bash apenas para ADO API e variaveis

O Bash pode ser usado **SOMENTE** para:
- `curl` - chamadas a ADO REST API
- `echo` / `printenv` - verificar variaveis de ambiente

**PROIBIDO** usar Bash para:
- Explorar ou modificar codigo
- Executar SQL ou PL/SQL
- Operacoes de filesystem alem de leitura

### R3 - Preservar estimativas existentes

- Se o WI ja tiver `StoryPoints` no ADO, **MANTER** e marcar como `[PRE-ESTIMATED]`
- Se o WI ja tiver `OriginalEstimate`, **MANTER**
- So sobrescrever se o usuario explicitamente pedir re-estimativa

### R4 - Confirmacao antes de aplicar no ADO

**SEMPRE** pedir confirmacao via `AskUserQuestion` ANTES de:
- Atualizar StoryPoints no ADO
- Atualizar OriginalEstimate no ADO
- Atualizar AssignedTo no ADO
- Adicionar Tags no ADO

### R5 - Formato de comunicacao

- **Idioma:** Portugues brasileiro
- **Formato:** Markdown estruturado
- **Progresso:** Indicar phase atual (ex: `## Phase 3 - Estimativa`)
- **Erros:** Exibir mensagem clara e sugerir acao corretiva

### R6 - Tag SUST-IA-CLAUDE

**SEMPRE** adicionar a tag `SUST-IA-CLAUDE` em toda Work Item atualizada pelo pipeline.

### Regra de Visibilidade do Knowledge

Sempre que qualquer agente for ler um arquivo em `${CLAUDE_PLUGIN_ROOT}/knowledge/`,
**ANTES** de usar Read, deve imprimir:

```
> [Knowledge] Carregando: {nome-do-arquivo} - {descricao-breve}
```

---

## Pipeline - Visao Geral

```
Phase 0   -> Validacao (ADO_PAT, argumento, TEAM_ROSTER)
Phase 0.5 -> Descoberta de Especializacoes (ou carregar cache)
Phase 1   -> Buscar WIs do ADO (WIQL ou batch fetch)
Phase 1.5 -> Verificar Campos ADO (StoryPoints, OriginalEstimate)
Phase 2   -> Ordenacao (Priority ASC, Severity ASC, Bug antes de US)
Phase 3   -> Estimativa (Story Points + Original Estimate)
Phase 4   -> Alocacao (Devs por scoring, depois Testers)
Phase 5   -> Sprint Board (tabela + carga + alertas)
Phase 6   -> Aplicar no ADO (opcional, com confirmacao)
```

**Modo Alocacao Avulsa:** Se o argumento for um unico WI ID, pular direto para
estimativa + alocacao avulsa (sem sprint board completo).

---

## Phase 0 - Validacao e Setup

### Objetivo
Validar pre-requisitos e parsear o argumento do usuario.

### Passos

#### 0.1 - Validar ADO_PAT

```bash
if [ -z "$ADO_PAT" ]; then
  echo "ERRO: ADO_PAT nao configurado"
  exit 1
fi
echo "ADO_PAT configurado (${#ADO_PAT} caracteres)"
```

Se vazio, informar ao usuario:
```
ERRO: A variavel de ambiente ADO_PAT nao esta configurada.
Configure com: export ADO_PAT="seu-token-aqui"
```

#### 0.2 - Parsear Argumento

| Formato do Argumento | Tipo | Acao |
|---------------------|------|------|
| UUID (36 chars com hifens) | Query ID | Executar query no ADO (Phase 1) |
| Numeros separados por virgula | Lista de WI IDs | Fetch batch (Phase 1) |
| Numero unico | WI ID unico | Modo alocacao avulsa |
| Vazio | Nenhum | Perguntar ao usuario via AskUserQuestion |

Se vazio, perguntar:
```
Para planejar a sprint, preciso saber quais Work Items incluir.

Informe uma das opcoes:
1. ID da query do ADO (UUID)
2. Lista de WI IDs separados por virgula (ex: 123456,123457)
3. ID de um unico WI (para alocacao avulsa)
```

#### 0.3 - Carregar TEAM_ROSTER

```
> [Knowledge] Carregando: TEAM_ROSTER.json - Roster do time com capacidades
```

Ler `${CLAUDE_PLUGIN_ROOT}/knowledge/team/TEAM_ROSTER.json`.

Se nao existir: ABORTAR com erro.

Extrair:
- Lista de developers (nome, email, max_sprint_points, availability)
- Lista de testers (nome, email, max_sprint_points, availability)
- complexity_thresholds
- type_multipliers
- estimate_formula

Apresentar resumo:

```
## Phase 0 - Validacao

- ADO_PAT: OK
- Argumento: {tipo} - {valor}
- Time: {N} devs, {M} testers
- Capacidade total: {X} SP (devs) + {Y} SP (testers)
```

---

## Phase 0.5 - Descoberta de Especializacoes

### Objetivo
Descobrir (ou carregar cache) as especializacoes de modulo de cada membro do time.

### Passos

#### 0.5.1 - Verificar cache

```
> [Knowledge] Carregando: TEAM_SPECIALIZATIONS.json - Cache de especializacoes do time
```

Tentar ler `${CLAUDE_PLUGIN_ROOT}/knowledge/team/TEAM_SPECIALIZATIONS.json`.

- Se existir e `_generated` < 30 dias atras: **usar cache**
- Se nao existir ou desatualizado: **executar descoberta**

Se usar cache, apresentar:
```
## Phase 0.5 - Especializacoes (Cache)

Cache carregado de {_generated} ({N} membros mapeados, {M} WIs analisados)
```

#### 0.5.2 - Descoberta via ADO (se necessario)

Lancar agente `taxone-sm` com `subagent_type="taxone-sm"` para descoberta:

```
## Descoberta de Especializacoes do Time

### Tarefa
Executar Phase 0.5 (Descoberta de Especializacoes) conforme documentado no seu perfil de agente.

### Dados
- TEAM_ROSTER carregado com {N} devs e {M} testers
- ADO_PAT disponivel em $ADO_PAT
- Salvar resultado em: ${CLAUDE_PLUGIN_ROOT}/knowledge/team/TEAM_SPECIALIZATIONS.json

### Output Esperado
Retornar resumo com:
- Total de WIs analisados
- Top 3 especializacoes de cada membro
- Timestamp da geracao
```

Apresentar resultado:
```
## Phase 0.5 - Especializacoes (Descoberta)

{N} WIs analisados dos ultimos 6 meses.
Especializacoes mapeadas para {M} membros do time.
Cache salvo em TEAM_SPECIALIZATIONS.json.
```

---

## Phase 1 - Buscar Work Items

### Objetivo
Buscar os Work Items do ADO que serao incluidos na sprint.

### Passos

#### 1.1 - Buscar via Query ID

Se o argumento for um UUID (Query ID):

```bash
AUTH=$(printf '%s' ":$ADO_PAT" | base64 -w0)
curl -s -H "Authorization: Basic $AUTH" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/wiql/{QUERY_ID}?api-version=7.1"
```

Extrair `workItems[].id` do response.

#### 1.2 - Buscar via WI IDs

Se o argumento for lista de IDs (ou IDs extraidos da query):

```bash
AUTH=$(printf '%s' ":$ADO_PAT" | base64 -w0)
# Batch fetch (max 200 por chamada)
curl -s -H "Authorization: Basic $AUTH" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems?ids={IDS}&\$expand=none&fields=System.Id,System.Title,System.WorkItemType,System.State,System.AreaPath,System.Tags,System.AssignedTo,Microsoft.VSTS.Common.Priority,Microsoft.VSTS.Common.Severity,Microsoft.VSTS.Scheduling.StoryPoints,Microsoft.VSTS.Scheduling.OriginalEstimate&api-version=7.1"
```

Se mais de 200 IDs, dividir em batches.

#### 1.3 - Extrair dados

Para cada WI, extrair:

| Campo | JSON Path |
|-------|-----------|
| ID | `$.id` |
| Titulo | `$.fields["System.Title"]` |
| Tipo | `$.fields["System.WorkItemType"]` |
| Estado | `$.fields["System.State"]` |
| Area Path | `$.fields["System.AreaPath"]` |
| Tags | `$.fields["System.Tags"]` |
| Assigned To | `$.fields["System.AssignedTo"]` |
| Priority | `$.fields["Microsoft.VSTS.Common.Priority"]` |
| Severity | `$.fields["Microsoft.VSTS.Common.Severity"]` |
| Story Points | `$.fields["Microsoft.VSTS.Scheduling.StoryPoints"]` |
| Original Estimate | `$.fields["Microsoft.VSTS.Scheduling.OriginalEstimate"]` |

Apresentar resumo:
```
## Phase 1 - Work Items

{N} WIs encontrados:
| # | ID | Tipo | Titulo | Pri | Sev | SP | Assigned |
|---|-----|------|--------|-----|-----|-----|----------|
| 1 | #123456 | Bug | ... | P1 | S1 | - | - |
| 2 | #123457 | US | ... | P2 | - | 5 | Eduardo Sa |
```

---

## Phase 1.5 - Verificar Campos ADO

### Objetivo
Confirmar que os campos `StoryPoints` e `OriginalEstimate` existem no template do work item type.

### Passos

Fazer GET em um WI da lista para verificar campos disponiveis:

```bash
AUTH=$(printf '%s' ":$ADO_PAT" | base64 -w0)
curl -s -H "Authorization: Basic $AUTH" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{FIRST_WI_ID}?api-version=7.1"
```

Verificar se os campos existem no response:
- `Microsoft.VSTS.Scheduling.StoryPoints`
- `Microsoft.VSTS.Scheduling.OriginalEstimate`

Se algum campo nao existir:
```
AVISO: O campo {campo} nao esta disponivel neste tipo de WI.
O pipeline continuara, mas nao sera possivel gravar {campo} no ADO.
```

Se ambos existirem:
```
## Phase 1.5 - Campos Verificados

StoryPoints: OK
OriginalEstimate: OK
```

---

## Phase 2 - Ordenacao

### Objetivo
Ordenar os WIs por prioridade para alocacao otimizada.

### Criterios de Ordenacao (em ordem)

1. **Priority ASC** (P1 primeiro, P4 por ultimo)
2. **Severity ASC** (S1 primeiro; WIs sem severity vao para o final)
3. **Tipo:** Bug antes de User Story antes de Feature antes de Task
4. **ID ASC** (desempate)

### Output

```
## Phase 2 - Ordenacao

WIs ordenados por prioridade:
| Pos | ID | Tipo | Pri | Sev | Titulo |
|-----|-----|------|-----|-----|--------|
| 1 | #123456 | Bug | P1 | S1 | ... |
| 2 | #123458 | Bug | P1 | S2 | ... |
| 3 | #123457 | US | P2 | - | ... |
```

---

## Phase 3 - Estimativa

### Objetivo
Estimar Story Points e OriginalEstimate para WIs que nao possuem.

### Passos

#### 3.1 - Separar WIs

- **Com SP existente:** Manter e marcar `[PRE-ESTIMATED]`
- **Sem SP:** Estimar via algoritmo

#### 3.2 - Lancar taxone-sm para estimativa

Para cada WI sem SP, lancar `taxone-sm`:

```
## Estimativa de Story Points

### Work Items para Estimar
{lista de WIs sem SP com ID, titulo, tipo, area path}

### Dados Disponiveis
- MODULE_KNOWLEDGE_MAP: ${CLAUDE_PLUGIN_ROOT}/knowledge/triage/MODULE_KNOWLEDGE_MAP.json
- Historico: ${CLAUDE_PLUGIN_ROOT}/knowledge/ado-fixes/
- Thresholds: {complexity_thresholds do TEAM_ROSTER}
- Multiplicadores: {type_multipliers do TEAM_ROSTER}
- Formula: OriginalEstimate = max(14, SP * 2.8)

### Output Esperado
Para cada WI, retornar:
- story_points (Fibonacci)
- original_estimate (horas)
- justificativa (historico usado ou default)
- flag (PRE-ESTIMATED, NO-HISTORY, ou vazio)
```

#### 3.3 - Consolidar

Apresentar:
```
## Phase 3 - Estimativa

| ID | Tipo | SP | EST(h) | Flag | Justificativa |
|-----|------|-----|--------|------|---------------|
| #123456 | Bug | 5 | 14 | | 3 bugs similares em Estadual (mediana: 4 files) |
| #123457 | US | 8 | 22 | NO-HISTORY | Default US sem historico |
| #123458 | Bug | 3 | 14 | PRE-ESTIMATED | Ja estimado no ADO |

Total: {TOTAL_SP} SP | {TOTAL_HOURS}h estimadas
```

---

## Phase 4 - Alocacao

### Objetivo
Alocar desenvolvedor e tester para cada WI por scoring de afinidade.

### Passos

#### 4.1 - Carregar especializacoes

```
> [Knowledge] Carregando: TEAM_SPECIALIZATIONS.json - Especializacoes do time
```

#### 4.2 - Lancar taxone-sm para alocacao

```
## Alocacao de Dev/Tester

### Work Items (ordenados por prioridade)
{lista completa de WIs com SP estimados}

### Time Disponivel
- Devs: {lista com nome, max_sprint_points, especializacoes}
- Testers: {lista com nome, max_sprint_points, especializacoes}

### Regras de Scoring
- +30 se modulo nas especializacoes
- +20 se vertical nas especializacoes
- +15 se tecnologia compativel
- -10 * (pontos_alocados / max_sprint_points)
- * availability

### WIs ja com AssignedTo
{lista de WIs que ja tem dev/tester no ADO - MANTER alocacao existente}

### Output Esperado
Para cada WI:
- dev_name, dev_email, dev_score
- tester_name, tester_email, tester_score
- flag (OVERFLOW, KEPT, ou vazio)
```

#### 4.3 - Consolidar

```
## Phase 4 - Alocacao

| ID | SP | Dev | Score | Tester | Score | Flag |
|-----|-----|-----|-------|--------|-------|------|
| #123456 | 5 | Eduardo Sa | 45 | Henrique Silva | 50 | |
| #123457 | 8 | Daniel Oliveira | 38 | Lara Paulo | 42 | |
| #123458 | 3 | Eduardo Sa | 45 | Henrique Silva | 50 | KEPT |
```

---

## Phase 5 - Sprint Board

### Objetivo
Apresentar o sprint board completo com carga por membro e alertas.

### Output

```
================================================================
  SPRINT PLAN - {DATA}  |  WIs: {N}  |  Total SP: {TOTAL}
================================================================
  PRI  | WI       | TIPO | SP | EST(h) | DEV              | TESTER           | MODULO
  -----+----------+------+----+--------+------------------+------------------+--------
  P1/S1| #123456  | Bug  |  5 |   14   | Eduardo Sa       | Henrique Silva   | ICMS
  P1/S2| #123457  | US   |  8 |   22   | Daniel Oliveira  | Lara Paulo       | SPED
  P2/S3| #123458  | Bug  |  3 |   14   | Eduardo Sa       | Henrique Silva   | Federal

  CARGA POR DESENVOLVEDOR:
  Eduardo Sa         8/35 (23%) |||||...............
  Daniel Oliveira    8/35 (23%) |||||...............
  Michel Paiva       0/35 ( 0%) ....................
  Luiz Castro        0/35 ( 0%) ....................

  CARGA POR TESTER:
  Henrique Silva     8/35 (23%) |||||...............
  Lara Paulo         8/35 (23%) |||||...............
  Murielle Soares    0/35 ( 0%) ....................

  ALERTAS:
  - [OVERFLOW] WI #99999 sem dev disponivel (capacidade excedida)
  - [PRE-ESTIMATED] WI #88888 ja tinha SP=3 (mantido)
  - [NO-HISTORY] WI #77777 sem historico similar (SP default=5)
  - [KEPT] WI #66666 ja tinha AssignedTo (mantido)
================================================================
```

### Barra de Progresso

A barra de carga usa 20 caracteres:
- `|` para SP alocados (proporcional)
- `.` para SP disponiveis

Calculo: `bars = round(20 * pontos_alocados / max_sprint_points)`

### Alertas

| Tag | Significado |
|-----|-------------|
| `[OVERFLOW]` | Nenhum dev/tester disponivel com capacidade |
| `[PRE-ESTIMATED]` | WI ja tinha SP no ADO (mantido) |
| `[NO-HISTORY]` | SP estimado sem historico similar (default usado) |
| `[KEPT]` | AssignedTo ja existia no ADO (mantido) |

---

## Phase 6 - Aplicar no ADO

### Objetivo
(OPCIONAL) Aplicar as estimativas e alocacoes no ADO.

### Passo 1 - Confirmar com usuario

Usar `AskUserQuestion`:

```
Deseja aplicar o sprint plan no ADO?

Os seguintes campos serao atualizados para cada WI:
- Microsoft.VSTS.Scheduling.StoryPoints
- Microsoft.VSTS.Scheduling.OriginalEstimate
- System.AssignedTo
- System.Tags (adicionar SUST-IA-CLAUDE)

Opcoes:
1. Sim, aplicar tudo
2. Aplicar apenas SP e Estimate (sem AssignedTo)
3. Aplicar apenas AssignedTo (sem SP)
4. Nao aplicar (apenas exibir)
```

### Passo 2 - Aplicar via PATCH

Para cada WI (conforme opcao escolhida):

```bash
AUTH=$(printf '%s' ":$ADO_PAT" | base64 -w0)
curl -s -X PATCH \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json-patch+json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{WI_ID}?api-version=7.1" \
  -d '[
    {
      "op": "add",
      "path": "/fields/Microsoft.VSTS.Scheduling.StoryPoints",
      "value": {SP}
    },
    {
      "op": "add",
      "path": "/fields/Microsoft.VSTS.Scheduling.OriginalEstimate",
      "value": {ESTIMATE}
    },
    {
      "op": "add",
      "path": "/fields/System.AssignedTo",
      "value": "{EMAIL}"
    },
    {
      "op": "add",
      "path": "/fields/System.Tags",
      "value": "{EXISTING_TAGS}; SUST-IA-CLAUDE"
    }
  ]'
```

**IMPORTANTE:**
- Content-Type e `application/json-patch+json`
- Tags: concatenar existentes + `SUST-IA-CLAUDE` (nao sobrescrever)
- Se WI ja tinha SP (`[PRE-ESTIMATED]`): **NAO** incluir StoryPoints no PATCH
- Se WI ja tinha AssignedTo (`[KEPT]`): **NAO** incluir AssignedTo no PATCH

### Passo 3 - Relatorio Final

```
## Phase 6 - Aplicado no ADO

| WI | SP | Estimate | AssignedTo | Tag | Status |
|-----|-----|----------|------------|-----|--------|
| #123456 | 5 | 14h | Eduardo Sa | SUST-IA-CLAUDE | OK |
| #123457 | 8 | 22h | Daniel Oliveira | SUST-IA-CLAUDE | OK |
| #123458 | SKIP | SKIP | SKIP | SUST-IA-CLAUDE | PRE-ESTIMATED + KEPT |

Resultado: {N}/{TOTAL} WIs atualizados com sucesso.
```

---

## Modo Alocacao Avulsa

Quando o argumento e um **unico WI ID**, o pipeline simplifica:

1. **Phase 0:** Validar ADO_PAT, carregar TEAM_ROSTER
2. **Phase 0.5:** Carregar especializacoes (cache ou descoberta)
3. **Phase 1:** Buscar unico WI do ADO
4. **Phase 3:** Estimar SP (se nao existir)
5. **Phase 4:** Alocacao avulsa (sem considerar carga de sprint)
6. **Apresentar:** Top 3 devs + Top 3 testers com scores

**Output do modo avulso:**

```markdown
## Alocacao Avulsa - WI #{WI_ID}

### Dados do WI
- **Titulo:** {titulo}
- **Tipo:** {tipo}
- **Modulo:** {modulo}
- **Vertical:** {vertical}
- **SP Estimado:** {sp}

### Desenvolvedores Recomendados
| # | Nome | Score | Motivo |
|---|------|-------|--------|
| 1 | {nome} | {score} | Especialista em {modulo} (18 WIs) |
| 2 | {nome} | {score} | {motivo} |
| 3 | {nome} | {score} | {motivo} |

### Testers Recomendados
| # | Nome | Score | Motivo |
|---|------|-------|--------|
| 1 | {nome} | {score} | Especialista em {modulo} |
| 2 | {nome} | {score} | {motivo} |
| 3 | {nome} | {score} | {motivo} |

### Recomendacao Final
- **Dev:** {nome} ({email})
- **Tester:** {nome} ({email})

Deseja aplicar esta alocacao no ADO? (S/N)
```

---

## Tratamento de Erros

| Erro | Fase | Acao |
|------|------|------|
| ADO_PAT vazio | 0 | ABORTAR com instrucoes |
| Query retorna 0 WIs | 1 | Informar e encerrar |
| Query retorna 401 | 1 | Informar PAT invalido/expirado |
| Campos SP/Estimate nao existem | 1.5 | AVISAR e continuar sem gravar esses campos |
| Nenhum historico similar | 3 | Usar defaults com flag `[NO-HISTORY]` |
| Todos devs/testers lotados | 4 | Marcar WI como `[OVERFLOW]` |
| PATCH falha | 6 | Reportar erro por WI, continuar com os demais |
| TEAM_ROSTER nao encontrado | 0 | ABORTAR com instrucoes |
| Cache especializacoes desatualizado | 0.5 | Regerar via ADO |
