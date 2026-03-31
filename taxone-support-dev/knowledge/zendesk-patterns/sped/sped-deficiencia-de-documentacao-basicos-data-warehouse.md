---
pattern_id: "sped-deficiencia-de-documentacao-basicos-data-warehouse"
vertical: sped
root_cause: deficiencia_de_documentacao
module: basicos_data_warehouse
ticket_count: 8
ticket_ids: [26503, 28461, 31595, 32444, 34072, 35212, 36857, 38920]
last_occurrence: "2022-05-04"
keywords: ["atualiza\u00e7\u00e3o", "mastersaf", "major", "r260", "guia", "pr\u00e1tico", "efd", "icms", "ipi", "publica\u00e7\u00e3o"]
is_not_bug: false
---

# BASICOS DATA WAREHOUSE: Deficiencia De Documentacao

## Descricao do Padrao
Clientes reportam problemas relacionados a: ATUALIZAÇÃO DO MASTERSAF DW – MAJOR R260.0.0; Em qual Safx deve informar o COD_SIT da tabela sped 4.1.2?; Geração registro 0205

## Causa Raiz
Deficiencia De Documentacao — classificacao baseada em 8 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Luciane bom dia!
&nbsp;
Hoje o sistema realiza a geração da seguinte forma: Pesquisa se durante o período de geração dos dados do arquivo, constam alterações na descrição do produto e/ou no código do produto. Caso sim, para cada alteração deve ser gravado um registro 0205. Os campos 02 e 05 são mutuamente excludentes, sendo obrigatório o preenchimento de um deles. Em caso de alteração da DESCR_ANT_ITEM e do COD_ANT_ITEM deverá ser gerado um registro para cada alteração.
&nbsp;
O Registro 0205...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 38920 | 2022-04-18 | documento de atualização Patch |
| 36857 | 2022-03-21 | Geração registro 0205 |
| 35212 | 2022-02-28 | Manual para geração do registro C115 Sped Fiscal |
| 34072 | 2022-02-14 | Unidade de medida 0200 |
| 32444 | 2022-01-28 | Em qual Safx deve informar o COD_SIT da tabela sped 4.1.2? |
| 31595 | 2022-01-19 | Publicação Patch 263.1.0 |
| 28461 | 2021-12-09 | Guia Prático EFD-ICMS/IPI – Versão 3.0.7 |
| 26503 | 2021-11-16 | ATUALIZAÇÃO DO MASTERSAF DW – MAJOR R260.0.0 |

## Keywords para Matching
atualização, mastersaf, major, r260, guia, prático, efd, icms, ipi, publicação
