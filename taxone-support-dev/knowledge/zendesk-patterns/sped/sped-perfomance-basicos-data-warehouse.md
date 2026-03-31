---
pattern_id: "sped-perfomance-basicos-data-warehouse"
vertical: sped
root_cause: perfomance
module: basicos_data_warehouse
ticket_count: 4
ticket_ids: [26445, 46310, 68729, 152058]
last_occurrence: "2025-10-07"
keywords: ["fto", "lentid\u00e3o", "programado", "tecpar", "taxone", "inc38104123", "baixa", "performance", "tax"]
is_not_bug: false
---

# BASICOS DATA WAREHOUSE: Perfomance

## Descricao do Padrao
Clientes reportam problemas relacionados a: FTO - Lentidão; INC38104123 - Lentidão/baixa performance Tax One; Programado

## Causa Raiz
Perfomance — classificacao baseada em 4 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa Tarde Charles tudo certo?
&nbsp;
Conforme falamos em call encontramos mais de 1300 jobs agendados, superior ao parametro job_queue_processes do BD.
&nbsp;
Sugiro que sejam revistos os jobs ou que o parametro job_queue_processes seja aumentado para 2500 e realize um novo teste.
&nbsp;
Se o parametro for aumentado sem que os jobs sejam revisitados, corre o risco de ultrapassar a quantidade de processos do BD(parametro processes), por isso a recomendação de validar os jobs antes.
&nbsp;
Muito...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 152058 | 2025-09-16 | INC38104123 - Lentidão/baixa performance Tax One |
| 68729 | 2023-05-16 | Tecpar - Lentidão TaxOne |
| 46310 | 2022-07-21 | Programado |
| 26445 | 2021-11-16 | FTO - Lentidão |

## Keywords para Matching
fto, lentidão, programado, tecpar, taxone, inc38104123, baixa, performance, tax
