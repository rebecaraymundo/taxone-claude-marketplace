---
pattern_id: "estadual-solicitacao-de-servico-estadual-fci"
vertical: estadual
root_cause: solicitacao_de_servico
module: estadual_fci
ticket_count: 4
ticket_ids: [21504, 48283, 50877, 130074]
last_occurrence: "2025-04-14"
keywords: ["copi\u00e1", "licenciamento", "ficha", "conteudo", "importa\u00e7", "m\u00f3dulo", "fci", "conte\u00fado", "modulos", "xml"]
is_not_bug: false
---

# ESTADUAL FCI: Solicitacao De Servico

## Descricao do Padrao
Clientes reportam problemas relacionados a: Copiá licenciamento Ficha de Conteudo de importaç; FCI - Demora na execução do calculo da FCI; Licenciamento do Módulo FCI - Ficha de Conteúdo de Importação (Estadual)

## Causa Raiz
Solicitacao De Servico — classificacao baseada em 4 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde tudo bem?
&nbsp;
Favor solicitar ao seu DBA que execute os procedimentos abaixo:
&nbsp;
1 - Executar SQL Tuning Advisor no SQL_ID 67ft7kj72yb0x e nos enviar os resultados.
&nbsp;
2 - Alterar os parametros de BD conforme abaixo:
&nbsp;
Aumentar sga_max_size de 8G para 20G
Aumentar sga_target de 0 para 20G
Aumentar PGA para 6G
Aumentar cpu_count de 2 para 4
&nbsp;
3 - Realizar o update abaixo:
&nbsp;
update MASTERSAF.PRT_PAR_MSAF set num_thread=4;
update MASTERSAF.PRT_PAR_MSAF set...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 130074 | 2025-03-21 | FCI - Demora na execução do calculo da FCI |
| 50877 | 2022-09-20 | Licenciamento do módulo FCI e outros modulos - XML... |
| 48283 | 2022-08-16 | Licenciamento do Módulo FCI - Ficha de Conteúdo de... |
| 21504 | 2021-09-10 | Copiá licenciamento Ficha de Conteudo de importaç |

## Keywords para Matching
copiá, licenciamento, ficha, conteudo, importaç, módulo, fci, conteúdo, modulos, xml
