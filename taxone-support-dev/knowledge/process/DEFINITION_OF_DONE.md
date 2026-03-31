# Definition of Done — TAX ONE Support

> Regras obrigatorias de processo para TODOS os agentes e skills.
> Fonte canonica — skills devem referenciar este arquivo ao inves de manter regras duplicadas.
>
> Ultima atualizacao: 2026-03-25

---

## 1. Checklist Pos-Implementacao (9 passos obrigatorios)

Apos implementar qualquer WI (bug, feature, chamado de regra — sem excecao), executar TODOS os passos na ordem, automaticamente, sem esperar o usuario pedir:

| # | Passo | Detalhes |
|---|-------|----------|
| 1 | **Compilar** | Compilar objetos PL/SQL no banco porta 1521 (`V2R010AC/V2R010AC@localhost:1521/MFSPDB`). Usar agente taxone-dba. Compilar ANTES de qualquer teste. |
| 2 | **Testes** | Testes manuais/SQL + SuiteAutomation (obrigatorio). Minimo 3 cenarios (ver secao 4). Rodar ANTES do commit/PR. |
| 3 | **Salvar artefatos** | Salvar scripts, outputs, screenshots, relatorios em `tests/{WI_ID}/` |
| 4 | **Upload Attachments** | TODOS os arquivos de `tests/{WI_ID}/` como Attachments na WI do ADO via REST API (`_apis/wit/attachments`). Usar `requests` (Python) — `curl` falha com binarios no Windows. |
| 5 | **Discussion comment** | Postar analise + resultados de testes na WI. Reportar CADA FASE separadamente (nao consolidar tudo). Embutir imagens inline com `<img src="{attachment_url}">`. |
| 6 | **Commit + Push + PR** | Branch `MFS{WI_ID}`, formato de commit/PR conforme secao 2, reviewer round-robin. Adicionar ArtifactLink do commit na WI (ver secao 2.4). |
| 7 | **Pacote unitario** | Disparar workflow no `tr/taxone_automacao_fab` (Phase 7.5 do auto-fix) |
| 8 | **Atualizar WI no ADO** | Tags (`SUST-IA-CLAUDE` + especificas), board column (`AI Review`), Solutions, Root Cause, Release Notes |
| 9 | **Criar Tasks QA** | Criar 2 Tasks filhas obrigatorias (ver secao 5) |

**CRITICO:** Nunca pular do passo 1 (compilar) direto para o passo 6 (PR). Os passos 2-5 sao OBRIGATORIOS antes da PR. Se algum passo falhar, registrar o erro e continuar com os demais. Uma WI so esta "concluida" quando todos os 9 passos estiverem feitos.

---

## 2. Convencoes Git

### 2.1 Branch

- Formato: `MFS{WI_ID}` a partir de DEV
- Correcoes adicionais na mesma WI: sufixo letra minuscula sequencial (`MFS{WI_ID}a`, `MFS{WI_ID}b`, `MFS{WI_ID}c`)
- Vale para TODOS os repositorios (taxone_dw, taxone-support-dev, etc.)

### 2.2 Commit

- Formato: `MFS{WI_ID} - {descricao curta}`
- **SEM** prefixo `[DEV]` no commit (o `[DEV]` e SOMENTE no titulo da PR)
- Ultima linha do body: `AB#{WI_ID}` (vincula ao Azure DevOps)

### 2.3 Pull Request

- Titulo: `[DEV] MFS{WI_ID} - {descricao curta}`
- Body: conteudo detalhado das mudancas
- Ultima linha do body: `AB#{WI_ID}`
- Reviewer round-robin entre: Daniel Oliveira (`DanielOliveira73`), Renato Ramos (`RenatoRamosTR`), Marcus Britto (`marcusbrittoTR`)
  - Para balancear: verificar PRs recentes (`gh api repos/tr/taxone_dw/pulls?state=all&per_page=30&base=DEV`)
- **NUNCA** fazer merge de PR — apenas criar. Merge e responsabilidade do usuario.

### 2.4 ArtifactLink do Commit na WI

Apos `git push`, SEMPRE adicionar o link do commit como ArtifactLink na WI do ADO via PATCH:

```python
artifact_url = f'vstfs:///GitHub/Commit/{conn_id}%2f{commit_sha}'
patch = [{'op': 'add', 'path': '/relations/-', 'value': {
    'rel': 'ArtifactLink', 'url': artifact_url,
    'attributes': {'name': 'GitHub Commit'}
}}]
```

- `conn_id`: extrair de ArtifactLink de PR existente, ou usar `9fb79fd1-0e5d-4bb0-a365-9c49bbb53464` (conexao GitHub tr/taxone_dw)
- Fazer ANTES de criar a PR (commit aparece primeiro na timeline)

### 2.5 Baseline RC

Antes de implementar, capturar baseline RC dos arquivos a modificar:

1. `git diff --stat RC..DEV -- "path"` para detectar divergencias
2. Se diverge: `git show RC:"path" > "path"` ANTES de implementar
3. Implementar sobre a versao RC (producao estavel), NAO sobre DEV

---

## 3. Regras ADO

### 3.1 Tags obrigatorias

| Tag | Quando aplicar |
|-----|---------------|
| `SUST-IA-CLAUDE` | TODA WI atualizada por analise da IA |
| `SUST-IA-CLAUDE-NOT-BUG` | WI avaliada como "Not a Bug" / "As Designed" |
| `SUST-IA-CLAUDE-ANALISE` | WI que precisa de analise adicional (NEEDS_INFO, INCOMPLETE_ANALYSIS, INCONCLUSIVO) |
| `SUST-IA-CLAUDE-REGRA` | WI que envolve criar/alterar/avaliar regra de negocio |

### 3.2 Board Columns

| Situacao | Board Column | Notas |
|----------|-------------|-------|
| Pos-analise com codigo no GitHub | `AI Review` | Verificar: `git branch -a \| grep MFS{WI_ID}` e/ou `gh pr list --search "{WI_ID}"` |
| Pos-implementacao com sucesso | `AI Review` | Mover AUTOMATICAMENTE apos implementacao correta |
| NEEDS_INFO / tag ANALISE | `Needs Info` | Mover junto com a tag, sem perguntar |
| Ticket ZD resolvido | `ZD Solved` | SOMENTE para WIs com ticket Zendesk (TKT no titulo) |

- Campo Kanban: `WEF_4D29798DEEEA43DE9E2EE295259A115B_Kanban.Column` via REST API (System.BoardColumn e read-only)
- Coluna "Pendente" foi renomeada para **"Pending"**

### 3.3 Cross-Area Path

WIs de outro Area Path podem nao ter as mesmas board columns. Se a API retornar erro (400, 404) ao mudar board column:

- **NAO insistir** — ignorar silenciosamente a movimentacao de board column
- Logar que foi pulada por ser de outro Area Path
- Todas as demais atualizacoes (tags, fields, discussion) continuam normalmente

### 3.4 Fechamento de WI

- **User Story**: States New/Active/Closed. **Closed e IRREVERSIVEL.**
  - ZD SOLVED → Board Column "Resolvido" (NAO fechar como Closed)
  - ZD CLOSED → State Closed com `Custom.ResolutionType=Done`, `Custom.ReleaseNotesNeeded=No`
- Campos obrigatorios para fechar: `System.State=Closed`, `Custom.ResolutionType` (Done/Cancelled), `Custom.ReleaseNotesNeeded` (Yes/No)

### 3.5 Release Notes

- Preencher `Custom.DescriptionofReleaseNotes` automaticamente (template em `knowledge/process/release-notes-template.md`)
- Se campo ja preenchido, NAO sobrescrever
- SOMENTE descricao funcional sucinta — SEM detalhes tecnicos (variaveis, px, nomes de campos, patterns, arquivos)

### 3.6 Campos de alocacao

- `Custom.Developer` para atribuir desenvolvedor (NAO `System.AssignedTo`)
- `Custom.Tester` para tester
- Sem dev/tester alocado → pedir ao SM para alocar

---

## 4. Regras de Teste

### 4.1 Cenarios minimos obrigatorios (3)

Para cada WI implementada, criar no minimo:

1. **Cenario base (happy path)**: Fluxo normal continua funcionando apos a correcao
2. **Cenario de erro corrigido**: Simular a condicao que causava o bug, verificar comportamento correto
3. **Cenario de nao-regressao**: Integridade dos dados existentes, nenhum fluxo adjacente quebrado

Salvar cenarios como scripts PL/SQL executaveis em `tests/{WI_ID}/`.

### 4.2 SuiteAutomation obrigatorio

- SEMPRE tentar rodar o SuiteAutomation apos implementacao, ALEM dos testes manuais/SQL
- Usar `scripts/suite_detached.py` (desacoplado do node.exe)
- Se falhar por falta de dados/config: registrar motivo e informar ao usuario
- NAO considerar WI como "testada" apenas com testes SQL

### 4.3 E2E para alteracoes de tela

Quando a WI alterar campos, combos, botoes ou comportamento de tela:

- Rodar `playwright_runner.py` com specs mapeados em `playwright-test-map.json`
- Buscar specs por `packages` (ex: EPC_SPED_FPROC → E2E_SPED_CONTRIBUICOES_OBRIGACOES)
- PL/SQL backend → smoke test | UI/forms → full test
- Se ambiente QA indisponivel: registrar tentativa e recomendar reexecucao

### 4.4 Sincronizar repo QA antes de criar cenarios

Antes de criar cenarios de teste ou flat files novos:

1. `git fetch` / `git pull` no repo `taxone_automacao_qa` (branch `rc`)
2. Buscar XMLs e arquivos esperados relacionados ao componente
3. Se ja existir cobertura: usar/incrementar o existente
4. Se nao: criar novo seguindo o padrao

---

## 5. Tasks QA (pos-teste)

Apos gerar evidencias e publicar na WI, criar **2 Tasks filhas obrigatorias**:

### Task 1: `[QA] Taxone - WI {WI_ID}`

- Contem os **testes unitarios** (SuiteAutomation, testes SQL manuais, validacoes de compilacao)
- Escopo: tudo que valida a correcao isoladamente

### Task 2: `[QA] Revisao de Plano de Testes | ID da(s) demanda(s) testada(s): {WI_ID}`

- Contem os **testes ANTES e DEPOIS** (baseline capture, comparacao, relatorio HTML)
- Escopo: evidencias de regressao, comparacao pre/pos-deploy, validacao end-to-end

### Regras de criacao

- Campo obrigatorio `Custom.Component` copiado do parent (sem ele a criacao falha)
- Campo obrigatorio `Custom.ResolutionType = Done` ao fechar (State = Closed)
- Reviewer QA por round-robin: Lucas Santos / Shayenne (via WIQL nas ultimas 10 tasks)
- Idempotente: se task ja existe, fazer UPDATE ao inves de duplicata
- Tag `SUST-IA-CLAUDE` em todas as tasks criadas
- Vincular como filha (Hierarchy-Reverse) da WI parent

---

## 6. N3 Triage — Regras de Enriquecimento

### 6.1 Processar anexos SEMPRE

O N3 Triage deve SEMPRE processar anexos relevantes (logs, XMLs, docs, SQLs) tanto da WI do ADO quanto do ticket Zendesk:

- Listar e classificar anexos por tipo
- Download de logs e XMLs
- Extrair error codes, stack traces, campos relevantes
- Consolidar achados no campo `problem.attachments_analysis` do `n3_brief.json`

**Por que:** Anexos frequentemente contem informacoes criticas (stack traces, campos nulos, mensagens de erro) que nao aparecem no texto da descricao.

---

## 7. Conhecimento de Dominio

### 7.1 Tabelas SAFX vs X

- **SAFX** = staging (dados importados aguardando processamento)
- **X** = dados definitivos/consolidados (ex: SAFX2101 → X2101_CONTAS_REF_CCUSTO)
- Ao consultar dados de clientes em Prod/UAT: SEMPRE usar tabelas **X**, NUNCA SAFX
- Se tabela X nao for obvia: procurar no procedure/package de importacao para o mapeamento

### 7.2 Manutencao de Documento Fiscal

- E SEMPRE Java, em OUTRO repositorio (nao no taxone_dw)
- O taxone_dw tem componentes PB legados, mas a tela ativa e Java
- WIs de manutencao de doc fiscal NAO podem ser implementadas no taxone_dw

### 7.3 Chamado de Regra

- WIs com request type "Chamado de Regra" NAO devem ser implementadas ate que a regra esteja desenvolvida pelo BA
- Aguardar definicao da regra antes de iniciar desenvolvimento

### 7.4 DDL

- NUNCA alterar DDL antiga existente
- Sempre criar DDL nova com ID da WI: `DDL_MFS{WI_ID}.sql`
- DDLs sao imutaveis apos criacao
