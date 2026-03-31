---
pattern_id: "estadual-falha-de-ambiente-do-cliente-basicos-report-fiscal"
vertical: estadual
root_cause: falha_de_ambiente_do_cliente
module: basicos_report_fiscal
ticket_count: 4
ticket_ids: [27846, 49839, 55333, 170531]
last_occurrence: "2026-02-03"
keywords: ["calculo", "diferencial", "aliquota", "nsk", "hughes", "inconsist\u00eancia", "relat\u00f3rios", "report", "fiscal", "erro"]
is_not_bug: false
---

# BASICOS REPORT FISCAL: Falha De Ambiente Do Cliente

## Descricao do Padrao
Clientes reportam problemas relacionados a: Calculo de Diferencial de Aliquota - NSK; Erro Valor Relatório EC87 - Jequiti; Lançamentos complementares 

## Causa Raiz
Falha De Ambiente Do Cliente — classificacao baseada em 4 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde Joyce,
&nbsp;
Analisamos as evidências e realizamos um teste em nosso ambiente onde pudemos observar que o cálculo do Diferencial de Alíquota está gerando correto, tanto na Apuração do ICMS quanto para o relatório do report fiscal.
&nbsp;
O valor do ICMS destacado 965,95 (valor do ICMS não escriturado)
O valor do ICMS devido 1.506,88 (valor do diferencial de alíquota 540,93 + &nbsp;ICMS não escriturado 965,95 )
&nbsp;

&nbsp;
O lançamento na apuração está gerando...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 170531 | 2026-01-20 | Lançamentos complementares  |
| 55333 | 2022-11-23 | Erro Valor Relatório EC87 - Jequiti |
| 49839 | 2022-09-06 | [Hughes] Inconsistência entre Relatórios - Report Fiscal x... |
| 27846 | 2021-12-02 | Calculo de Diferencial de Aliquota - NSK |

## Keywords para Matching
calculo, diferencial, aliquota, nsk, hughes, inconsistência, relatórios, report, fiscal, erro
