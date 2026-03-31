---
pattern_id: "sped-falha-de-ambiente-do-cliente-basicos-data-warehouse"
vertical: sped
root_cause: falha_de_ambiente_do_cliente
module: basicos_data_warehouse
ticket_count: 5
ticket_ids: [23911, 26358, 44216, 60125, 64141]
last_occurrence: "2023-03-28"
keywords: ["erro", "efd", "contribui\u00e7\u00f5es", "safx48", "processo", "importa\u00e7\u00e3o", "referencia", "chamado", "unidade", "medida"]
is_not_bug: false
---

# BASICOS DATA WAREHOUSE: Falha De Ambiente Do Cliente

## Descricao do Padrao
Clientes reportam problemas relacionados a: 26677 | ##RE-394430## - DW QAS - Erro ao gerar Sped Fiscal; Erro EFD Contribuições; Erro na geração de evento

## Causa Raiz
Falha De Ambiente Do Cliente — classificacao baseada em 5 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Oi Adrian, bom dia tudo bem?
&nbsp;
O problema está no índice que está como inutilizável e esse mesmo seria um índice antigo, alguma alteração ocorreu em algo na base. Neste cenário é necessário o DBA interno verificar. Em uma pesquisa rápida na internet seria só dar um rebuild no index e se o problema for na partição dar um rebuild na partição.
&nbsp;
https://atitudereflexiva.wordpress.com/2019/08/03/ora-01502-como-tratar-um-indice-inutilizado-no-oracle/
&nbsp;
Status do ticket alterado para...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 64141 | 2023-03-17 | Erro na geração de evento |
| 60125 | 2023-01-26 | 26677 | ##RE-394430## - DW QAS - Erro ao gerar Sped Fiscal |
| 44216 | 2022-06-24 | Unidade de Medida do item divergente do cadastro de produto. |
| 26358 | 2021-11-12 | SAFX48 - Processo de Importação - Referencia chamado #25953 |
| 23911 | 2021-10-11 | Erro EFD Contribuições |

## Keywords para Matching
erro, efd, contribuições, safx48, processo, importação, referencia, chamado, unidade, medida
