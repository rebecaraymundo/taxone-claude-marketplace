---
pattern_id: "federal-falha-de-dados-de-ou-parametros-federal-conexao-onesource-br-esocial"
vertical: federal
root_cause: falha_de_dados_de_ou_parametros
module: federal_conexao_onesource_br_esocial
ticket_count: 2
ticket_ids: [7119, 81363]
last_occurrence: "2023-10-23"
keywords: ["n\u00e3o", "envia", "evento", "onesource", "reinf", "urgente"]
is_not_bug: false
---

# FEDERAL CONEXAO ONESOURCE BR ESOCIAL: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: DW não envia evento para onesource; REINF 2.1. - URGENTE

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 2 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Daniel, bom dia. 

Conforme acesso remoto, validamos que os eventos não estão sendo "lido" pelo Integrador, devido ao Tipo de Ambiente. Os eventos estão sendo gerados como Tipo de Ambiente 1 (produção) e o Integrador esta parametrizado para ler Eventos tipo de Ambiente 2 (Produção Restrita). 

Sendo assim, é necessário solicitar que os usuários gerem eventos de produção restrita para prosseguir. 

Sigo à disposição. 


  Jheferson Crescencio

Thomson Reuters

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 81363 | 2023-10-16 | REINF 2.1. - URGENTE |
| 7119 | 2021-03-30 | DW não envia evento para onesource |

## Keywords para Matching
não, envia, evento, onesource, reinf, urgente
