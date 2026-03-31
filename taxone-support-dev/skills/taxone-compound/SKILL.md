# taxone-compound Skill

Compound Engineering adaptado para o TAX ONE.
Transforma cada unidade de trabalho (bug fix, feature, refactoring, optimization)
em documentacao reutilizavel que acelera trabalhos futuros.

---

## Visao Geral

O Compound Engineering e a pratica de documentar sistematicamente cada solucao
implementada, criando uma base de conhecimento cumulativa. No contexto do TAX ONE,
isso e especialmente valioso dada a complexidade do sistema fiscal PL/SQL/Oracle.

**Filosofia:** Plan -> Work -> Review -> **Compound** -> Repeat

---

## YAML Frontmatter Schema

Cada documento gerado deve iniciar com YAML frontmatter searchable:

```yaml
---
title: "{titulo descritivo da solucao}"
date: "{YYYY-MM-DD}"
author: "taxone-compound"
type: "{problem_type}"
component: "{component}"
category: "{category}"
severity: "{severity}"
wi_id: "{work_item_id}"
vertical: "{vertical}"
modules:
  - "{modulo1}"
  - "{modulo2}"
packages:
  - "{PKG_XXX}"
tables:
  - "{TB_XXX}"
tags:
  - "{tag1}"
  - "{tag2}"
pr_number: "{pr_number}"
pr_files:
  - "{file1}"
  - "{file2}"
pr_stats:
  additions: {N}
  deletions: {N}
  files_changed: {N}
related_solutions:
  - "{caminho/para/solucao-relacionada.md}"
---
```

### Enums do Frontmatter

**problem_type:**
- `bug_fix` - Correcao de bug
- `feature` - Implementacao de feature nova
- `refactoring` - Refatoracao de codigo existente
- `optimization` - Otimizacao de performance (Oracle/PL/SQL)
- `hotfix` - Correcao urgente em producao
- `migration` - Migracao de dados ou schema

**component:**
- `plsql_package` - Package PL/SQL (spec/body)
- `plsql_procedure` - Procedure standalone
- `plsql_function` - Function standalone
- `plsql_trigger` - Trigger
- `oracle_table` - Tabela Oracle (DDL)
- `oracle_view` - View ou Materialized View
- `oracle_index` - Indice
- `oracle_partition` - Particionamento
- `powerbuilder_window` - Tela PowerBuilder
- `powerbuilder_datawindow` - DataWindow
- `powerbuilder_userobject` - User Object
- `java_service` - Servico Java
- `java_dao` - DAO Java
- `java_batch` - Processamento batch Java
- `multi_layer` - Multiplas camadas afetadas

**category:**
- `apuracao` - Apuracao de impostos (ICMS, IPI, PIS, COFINS, ISS, etc.)
- `obrigacoes` - Obrigacoes acessorias (SPED, EFD, DCTF, GIA, etc.)
- `cadastro` - Cadastros (notas fiscais, participantes, produtos, etc.)
- `importacao` - Importacao de dados (XML, TXT, CSV, EDI, etc.)
- `calculo` - Calculos fiscais e tributarios
- `consulta` - Consultas e views de dados
- `relatorios` - Relatorios fiscais e gerenciais
- `integracao` - Integracoes com sistemas externos
- `outros` - Outros (infraestrutura, configuracao, etc.)

**severity:**
- `critical` - Impacto em producao, dados incorretos
- `high` - Funcionalidade quebrada, sem workaround
- `medium` - Funcionalidade parcial, com workaround
- `low` - Melhoria, sem impacto funcional

**vertical:** (extraida de _metadata.json ou inferida do modulo)
- `basicos`, `estadual`, `federal`, `municpal`, `sped`, `especificos`, `utilitarios`

---

## Pipeline de Execucao

### Pre-check: Extrair WI ID e Vertical

1. Validar que estamos em um repositorio git do TAX ONE
2. Criar estrutura `knowledge/solutions/` se nao existir
3. Verificar se ha historico de conversa suficiente para documentar
4. **Extrair WI ID** (6-7 digitos) do historico da conversa (ex: "WI 1067285", "MFS1067285", "#1067285")
5. **Buscar WI no _metadata.json** via Grep no `knowledge/ado-fixes/_metadata.json` pelo WI ID:
   - Extrair `vertical`, `tags`, `pr_numbers`, `module`
6. **Buscar PR no _pr_cache.json** via Grep no `knowledge/ado-fixes/_pr_cache.json` (`"pr#NNNN"`):
   - Extrair `files` (lista de arquivos alterados), `additions`, `deletions`
7. **Verificar se WI ja existe** em `knowledge/solutions/INDEX.md`:
   - Se existe: mode = "update" (complementar documento existente)
   - Se nao existe: mode = "create"
8. Passar `wi_id`, `vertical`, `pr_data`, e `mode` como contexto a todos os 5 subagentes

### Fase 1: Pesquisa Paralela (5 Subagentes Simultaneos)

Lancar 5 subagentes em paralelo via Agent tool:

#### 1. Context Analyzer (taxone-architect)

```
Analisar o historico completo da conversa e extrair os campos do YAML frontmatter:
- title, type, component, category, severity
- modules, packages, tables envolvidos
- tags relevantes para busca futura
- wi_id e vertical (fornecidos no contexto)

Enriquecer com dados do _metadata.json (se fornecidos no contexto):
- Adicionar tags da WI ao campo tags
- Confirmar/corrigir vertical e module

Enriquecer com dados do _pr_cache.json (se fornecidos no contexto):
- Adicionar pr_number ao YAML
- Adicionar pr_files (lista de arquivos alterados)
- Adicionar pr_stats (additions, deletions, files_changed)

Retornar APENAS o bloco YAML formatado.
```

#### 2. Solution Extractor (taxone-developer)

```
Analisar o historico completo da conversa e extrair:

## Approach
[Como o problema foi abordado - hipoteses testadas, caminhos percorridos]

## Analysis
[Analise tecnica detalhada - root cause, codigo afetado, dependencias]

## Solution
[Solucao implementada - mudancas feitas, justificativas tecnicas]

## Failed Attempts (se houver)
[Tentativas que nao funcionaram e por que - aprendizados criticos]

Incluir trechos de codigo PL/SQL/SQL relevantes.

Complementar root cause lendo `knowledge/ado-fixes/{vertical}/{wi_id}.md` (se existir).
O vertical e wi_id sao fornecidos no contexto.
```

#### 3. Related Docs Finder (taxone-architect)

```
Buscar documentos relacionados em 4 fontes da base de conhecimento:

### Fonte 1: Compound Docs (knowledge/solutions/)
Buscar em knowledge/solutions/INDEX.md por documentos do mesmo modulo, packages, ou tabelas.
Ler INDEX.md e filtrar por modulo/packages/tabelas relevantes (fornecidos no contexto).

### Fonte 2: WIs Similares (knowledge/ado-fixes/_metadata.json)
Grep por package/tabela/modulo no _metadata.json para encontrar WIs similares.
Retornar top 5 matches com WI ID, titulo e modulo.

### Fonte 3: Zendesk Patterns (knowledge/zendesk-patterns/{vertical}/INDEX.md)
Ler o INDEX.md da vertical correspondente (fornecida no contexto).
Buscar patterns do mesmo modulo/area funcional.
Retornar top 3 patterns com titulo, N tickets, causa raiz.

### Fonte 4: Webhelp (knowledge/webhelp/MODULE_INDEX.json)
Grep por modulo no MODULE_INDEX.json para encontrar artigos de documentacao relevantes.
Retornar top 5 artigos com titulo e path.

Retornar output com 4 subsecoes:
- Compound Docs: lista de caminhos relativos
- WIs Similares: tabela com WI ID, titulo, modulo
- Zendesk Patterns: tabela com pattern, tickets, causa raiz
- Webhelp: lista de artigos relevantes
```

#### 4. Prevention Strategist (taxone-tester)

```
Analisar a solucao implementada e gerar:

## Patterns Identificados
[Patterns de codigo que devem ser seguidos/evitados]

Antes de gerar, ler knowledge/solutions/INDEX.md secao "Patterns Recorrentes":
- Se o pattern ja existe no INDEX, referenciar (ex: "Ver Pattern: UNION vs UNION ALL")
- Se e um pattern NOVO, marcar como "[NOVO]" para inclusao futura no INDEX

## Dados Quantitativos
Ler knowledge/zendesk-patterns/{vertical}/INDEX.md (vertical fornecida no contexto):
- Incluir dados quantitativos se disponiveis (N tickets, causa raiz recorrente)
- Verificar knowledge/zendesk-patterns/not-a-bug/INDEX.md:
  Se o modulo tem patterns not-a-bug, alertar: "ATENCAO: Modulo X tem N patterns not-a-bug no Zendesk"

## Cenarios de Teste
[Lista de cenarios para validar a correcao, incluindo regressao]

## Checklist de Validacao
- [ ] [item 1]
- [ ] [item 2]

## Takeaways
[Licoes aprendidas, dicas para problemas similares futuros]

Focar em PL/SQL, Oracle e contexto fiscal.
```

#### 5. Category Classifier (taxone-architect)

```
Determinar:
1. Subcategoria dentro da category principal (ex: apuracao -> icms-st)
2. Filename: {wi_id}.md (usando o WI ID fornecido no contexto)
3. Diretorio: knowledge/solutions/
4. Mode: "update" ou "create" (fornecido no contexto via pre-check)

Se mode = "update":
  - Ler o documento existente em knowledge/solutions/{wi_id}.md
  - Identificar secoes que precisam ser complementadas/atualizadas

Retornar: diretorio completo + filename + mode + secoes a atualizar (se update).
```

### Fase 2: Assembly (Sequencial)

**Aguardar TODOS os 5 subagentes completarem.**

1. **Validar YAML frontmatter:**
   - Todos os campos obrigatorios preenchidos
   - Enums dentro dos valores permitidos
   - Packages e tabelas com nomes validos
   - wi_id e vertical presentes
   - pr_files e pr_stats preenchidos (se PR existir)

2. **Montar documento completo:**

```markdown
---
{YAML frontmatter do Context Analyzer}
---

# {title}

## Contexto
[Breve contexto do problema/requisito]

## PR Stats
| Metrica | Valor |
|---------|-------|
| PR | #{pr_number} |
| Arquivos alterados | {files_changed} |
| Additions | +{additions} |
| Deletions | -{deletions} |

**Arquivos:**
{lista de pr_files}

## Approach
{do Solution Extractor}

## Analysis
{do Solution Extractor}

## Solution
{do Solution Extractor}

## Failed Attempts
{do Solution Extractor - se houver}

## Patterns
{do Prevention Strategist - incluindo dados quantitativos e alertas not-a-bug}

## Cenarios de Teste
{do Prevention Strategist}

## Checklist de Validacao
{do Prevention Strategist}

## Takeaways
{do Prevention Strategist}

## Solucoes Relacionadas

### Compound Docs
{do Related Docs Finder - Fonte 1}

### WIs Similares
{do Related Docs Finder - Fonte 2}

### Zendesk Patterns
{do Related Docs Finder - Fonte 3}

### Webhelp
{do Related Docs Finder - Fonte 4}
```

3. **Escrever arquivo** em `knowledge/solutions/{wi_id}.md`

4. **Atualizar INDEX.md:**
   - Ler `knowledge/solutions/INDEX.md`
   - Se mode = "create": adicionar nova linha na tabela de Solucoes
   - Se mode = "update": atualizar linha existente (data, PR, titulo se necessario)
   - Se pattern e NOVO: adicionar na secao "Patterns Recorrentes"

5. **Apresentar resultado** ao usuario com caminho do arquivo criado/atualizado

---

## Quando Usar

O Compound se aplica a QUALQUER trabalho de desenvolvimento que atenda a pelo menos um criterio:

- Bug fix com investigacao > 15 minutos
- Feature implementation com decisoes tecnicas relevantes
- Refactoring com melhorias mensuaveis
- Optimization com ganhos de performance em Oracle
- Qualquer trabalho onde tentativas falharam antes do sucesso
- Mudancas em multiplas camadas (PL/SQL + View + Tabela + PowerBuilder)

---

## Exemplos de Documentos Gerados

```
knowledge/solutions/1060768.md
knowledge/solutions/1053341.md
knowledge/solutions/1067285.md
knowledge/solutions/1028814.md
knowledge/solutions/951077.md
```
