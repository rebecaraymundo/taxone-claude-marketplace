# Schema Canônico — test_scenarios.json v2.0

Referência normativa para a estrutura de `tests/{WI_ID}/test_scenarios.json`.
Todos os agentes (PM, tester, enricher) devem gerar/consumir conforme este schema.

## Versão

- **v2.0.0** — Adicionados campos `sql_pre_dev`, `setup_data`, `teardown_data`, `dev_runnable`
- **v1.0.0** — Schema original (compatível — campos novos são opcionais)

## Estrutura Root

```json
{
  "version": "2.0.0",
  "wi_id": 1058668,
  "wi_title": "TKT999999 - Descrição da WI",
  "generated_by": "taxone-pm",
  "generated_at": "2026-03-23T10:00:00Z",
  "module": "Estadual",
  "vertical": "ICMS",
  "screen": {
    "menu_path": "ESTADUAL > ICMS > APURACAO > ...",
    "mapping_id": "E2E_GIA_SP",
    "e2e_specs": ["e2e/estadual/giaSP/obrigacoes/obrigacoes.spec.ts"]
  },
  "tables_involved": ["ICT_GIA_ST", "ICT_GIA_ST_ANEX1_2"],
  "packages_involved": ["SAF_GIA_ST", "EST_GIA_ST_FPROC"],
  "scenarios": [],
  "enrichments": [],
  "suite_recommendations": [],
  "enriched_by": "test_enricher",
  "enriched_at": "2026-03-23T10:05:00Z",
  "enrichment_stats": {}
}
```

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `version` | string | Sim | Versão do schema (`"2.0.0"`) |
| `wi_id` | number | Sim | ID da Work Item |
| `wi_title` | string | Sim | Título da WI |
| `generated_by` | string | Sim | Agente que gerou (`taxone-pm`, `taxone-architect`, `manual`) |
| `generated_at` | string | Sim | ISO 8601 timestamp |
| `module` | string | Sim | Módulo fiscal (Estadual, Federal, SPED, etc.) |
| `vertical` | string | Sim | Vertical do módulo (ICMS, PIS/COFINS, ECD, etc.) |
| `screen` | object | Sim | Info da tela (`menu_path`, `mapping_id`, `e2e_specs`) — campos nullable |
| `tables_involved` | string[] | Sim | Tabelas Oracle identificadas na análise |
| `packages_involved` | string[] | Sim | Packages/procedures PL/SQL identificados |
| `scenarios` | array | Sim | Array de cenários (ver abaixo) |
| `enrichments` | array | Não | Fontes consultadas pelo PM |
| `suite_recommendations` | array | Não | Suites XML recomendadas (populado pelo enricher) |
| `enriched_by` | string | Não | Script/agente que enriqueceu |
| `enriched_at` | string | Não | Timestamp do enriquecimento |
| `enrichment_stats` | object | Não | Estatísticas do enriquecimento |

## Estrutura de Cenário

```json
{
  "id": "S01",
  "type": "happy_path",
  "title": "Guia GIA-ST emitida com período de referência correto",
  "preconditions": [
    "Apuração ICMS-ST gerada para período 12/2025",
    "Dados da GIA-ST em ICT_GIA_ST com DAT_APURACAO = 31/12/2025"
  ],
  "steps": [
    "Acessar Menu Estadual > ICMS > Apuração > GIA-ST > Emissão",
    "Selecionar empresa/estabelecimento e período 12/2025",
    "Emitir relatório"
  ],
  "expected_result": "Campo 'Período de Referência' exibe '12/2025'",
  "sql_hint": "SELECT COD_EMPRESA, DAT_APURACAO FROM ICT_GIA_ST WHERE ...",
  "sql_pre_dev": "SELECT COD_EMPRESA, COD_ESTAB, DAT_APURACAO, TO_CHAR(DAT_APURACAO, 'MM/YYYY') AS PERIODO, CASE WHEN TO_CHAR(DAT_APURACAO, 'MM/YYYY') = '12/2025' THEN 'OK' ELSE 'FALHA' END AS resultado FROM ICT_GIA_ST WHERE DAT_APURACAO = TO_DATE('31/12/2025','DD/MM/YYYY') AND ROWNUM <= 10",
  "setup_data": [
    "INSERT INTO ICT_GIA_ST (COD_EMPRESA, COD_ESTAB, DAT_APURACAO) VALUES ('TST', '001', TO_DATE('31/12/2025','DD/MM/YYYY'))"
  ],
  "teardown_data": [
    "DELETE FROM ICT_GIA_ST WHERE COD_EMPRESA = 'TST' AND COD_ESTAB = '001'"
  ],
  "dev_runnable": true,
  "e2e_grep": "GIA-ST|emissao|periodo.*referencia",
  "priority": "critical",
  "hotspot_matches": [],
  "typed_columns": [],
  "sql_hint_enriched": null,
  "git_impact": {
    "directly_changed": false,
    "indirectly_impacted": false
  }
}
```

| Campo | Tipo | Obrigatório | Quem gera | Descrição |
|-------|------|-------------|-----------|-----------|
| `id` | string | Sim | PM | Identificador sequencial: `S01`, `S02`... |
| `type` | enum | Sim | PM | Ver enum abaixo |
| `title` | string | Sim | PM | Título descritivo do cenário (em português) |
| `preconditions` | string[] | Sim | PM | Pré-condições necessárias |
| `steps` | string[] | Sim | PM | Passos do cenário |
| `expected_result` | string | Sim | PM | Resultado esperado (descritivo) |
| `sql_hint` | string\|null | Sim | PM | Fragmento SQL conceitual (dica para o tester) |
| `sql_pre_dev` | string\|null | **v2.0** | Tester (pré-dev) | **SELECT executável** no banco local. Retorna linhas com coluna `resultado` = `'OK'` ou `'FALHA'` |
| `setup_data` | string[]\|null | **v2.0** | Tester (pré-dev) | INSERTs com dados sintéticos para o cenário |
| `teardown_data` | string[]\|null | **v2.0** | Tester (pré-dev) | DELETEs de limpeza |
| `dev_runnable` | boolean | **v2.0** | Tester (pré-dev) | `true` se o cenário pode ser executado diretamente no banco local |
| `e2e_grep` | string\|null | Não | PM | String para filtro Playwright |
| `priority` | enum | Sim | PM/enricher | `critical`, `high`, `medium`, `low` |
| `hotspot_matches` | string[] | Não | enricher | Hotspots que coincidem com tabelas do cenário |
| `typed_columns` | string[] | Não | enricher | Colunas com tipo (do COLUMN_GLOSSARY) |
| `sql_hint_enriched` | string\|null | Não | enricher | sql_hint expandido com tipos e JOINs |
| `git_impact` | object\|null | Não | enricher | `{directly_changed, indirectly_impacted}` |

## Enums

### `type` (tipo de cenário)

| Valor | Descrição |
|-------|-----------|
| `happy_path` | Fluxo principal que deve funcionar |
| `negative` | Comportamento que NÃO deve ocorrer |
| `edge_case` | Valores limite, nulos, zeros, datas extremas |
| `regression` | Funcionalidades adjacentes inalteradas |
| `bug_reproduction` | Cenário exato do bug reportado |
| `performance` | Volume alto, timeout |
| `data_integrity` | Consistência entre tabelas (FKs, totalizadores) |
| `investigation` | Cenário exploratório (não tem expected_result definido) |

### `priority` (prioridade)

| Valor | Descrição |
|-------|-----------|
| `critical` | Cenário do bug reportado ou hotspot match |
| `high` | Cenários negativos e regressão |
| `medium` | Edge cases |
| `low` | Cenários opcionais |

**IMPORTANTE**: NÃO usar `P1`/`P2`. Sempre usar as strings acima.

## Critérios para `dev_runnable`

Um cenário é `dev_runnable: true` quando:
1. Todas as tabelas em `tables_involved` existem no schema Oracle local (`V2R010AC`)
2. A query `sql_pre_dev` não depende de dados de cliente específico (usa dados existentes ou `setup_data` incluído)
3. Não requer execução prévia de procedures PL/SQL complexas como pré-condição

Um cenário é `dev_runnable: false` quando:
1. Depende de geração de arquivo magnético (SPED, ECD, EFD)
2. Depende de dados de produção/UAT não replicáveis localmente
3. A pré-condição é "ter rodado o processo X completo"

## Regras para `setup_data`

- Usar PKs **claramente fictícias**: empresa `'TST'`, CNPJ `'00000000000000'`, estabelecimento `'001'`
- Períodos fictícios: `01/2099` ou similar (evitar conflito com dados reais)
- **NUNCA** incluir dados de cliente real
- `teardown_data` deve reverter 100% do `setup_data`
- `setup_data` pode ser `null` se o cenário usa dados existentes no banco local

## Backward Compatibility

Consumidores (tester, enricher) devem usar fallback para campos que mudaram entre variantes:

```python
# Fallback de título
title = scenario.get("title") or scenario.get("name") or scenario.get("description", "Sem título")

# Fallback de query
sql = scenario.get("sql_pre_dev") or scenario.get("sql_hint_enriched") or scenario.get("sql_hint") or scenario.get("validation_query", "")

# Fallback de prioridade
priority = scenario.get("priority", "medium")
if priority in ("P1",): priority = "critical"
if priority in ("P2",): priority = "high"

# Campos novos v2.0 (default seguro)
dev_runnable = scenario.get("dev_runnable", False)
setup_data = scenario.get("setup_data") or []
teardown_data = scenario.get("teardown_data") or []
```

## Exemplo Completo

Ver `tests/1053341/test_scenarios.json` como exemplo de referência v1.0 (compatível com v2.0 via fallback).
