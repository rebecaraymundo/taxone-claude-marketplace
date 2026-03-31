---
pattern_id: "sped-sem-atuacao-ou-conclusao-thomson-reuters-sped-esocial"
vertical: sped
root_cause: sem_atuacao_ou_conclusao_thomson_reuters
module: sped_esocial
ticket_count: 2
ticket_ids: [37390, 60818]
last_occurrence: "2023-02-10"
keywords: ["eventos", "esocial", "n\u00e3o", "foram", "desimpedidos", "erro", "evento", "1200"]
is_not_bug: false
---

# SPED ESOCIAL: Sem Atuacao Ou Conclusao Thomson Reuters

## Descricao do Padrao
Clientes reportam problemas relacionados a: Erro no evento S-1200 do eSocial; Eventos do eSocial não foram desimpedidos automaticamente

## Causa Raiz
Sem Atuacao Ou Conclusao Thomson Reuters — classificacao baseada em 2 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Olá Fran, bom dia!
&nbsp;
Avaliando os logs da mensageria, conseguimos identificar algum erros de Lock:
&nbsp;
 ERROR 2022-03-29 14:24:56,163&nbsp; - dd.trace_id= dd.span_id= - [Camel (esocial-context) thread #622 - JmsConsumer[TaxBrEsocialImpedimentQueue]] - [SYSTEM] - [org.apache.camel.processor.FatalFallbackErrorHandler] - \--&gt; Previous exception on exchangeId: ID-HBBWAPLP141-1644010134191-8-13073889&nbsp;
com.thomsonreuters.taxit.lock.service.exception.TaxitLockException:...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 60818 | 2023-02-03 | Erro no evento S-1200 do eSocial |
| 37390 | 2022-03-28 | Eventos do eSocial não foram desimpedidos automaticamente |

## Keywords para Matching
eventos, esocial, não, foram, desimpedidos, erro, evento, 1200
