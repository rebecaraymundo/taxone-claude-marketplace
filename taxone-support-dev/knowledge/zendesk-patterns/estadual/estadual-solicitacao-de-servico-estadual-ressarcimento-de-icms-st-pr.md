---
pattern_id: "estadual-solicitacao-de-servico-estadual-ressarcimento-de-icms-st-pr"
vertical: estadual
root_cause: solicitacao_de_servico
module: estadual_ressarcimento_de_icms-st_-_pr
ticket_count: 4
ticket_ids: [77333, 102540, 115970, 156411]
last_occurrence: "2026-01-06"
keywords: ["solicita\u00e7\u00e3o", "melhoria", "exporta\u00e7\u00e3o", "logs", "relat\u00f3rios", "adequa\u00e7\u00e3o", "entrega", "adrc", "atacadao", "lentid\u00e3o"]
is_not_bug: false
---

# ESTADUAL RESSARCIMENTO DE ICMS-ST - PR: Solicitacao De Servico

## Descricao do Padrao
Clientes reportam problemas relacionados a: ADEQUAÇÃO PARA ENTREGA DA ADRC - PR; ATACADÃO | PROBLEMA DE PERFORMANCE NO RESSARCIMENTO PR; Re: ATACADAO | Lentidão Geração Movimentos de Saída - Ressarcimento ICMS ST Paraná

## Causa Raiz
Solicitacao De Servico — classificacao baseada em 4 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde!
&nbsp;
O servidor está no topo dos recursos de CPU:
&nbsp;

&nbsp;
É possível liberar mais recursos?
&nbsp;
Isso ocorreu devido a diversos disparos de jobs, que causaram consumo excessivo de recursos:
&nbsp;

&nbsp;
Além disso, há vários parametros não documentados(hidden), setados nesse banco de dados:
&nbsp;



&nbsp;
Sugerimos também que seja aberto um chamado no suporte da Oracle, pois nós não solicitamos esses parametros hidden, que podem causar problemas de performance e/ou...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 156411 | 2025-10-16 | ATACADÃO | PROBLEMA DE PERFORMANCE NO RESSARCIMENTO PR |
| 115970 | 2024-11-11 | Re: ATACADAO | Lentidão Geração Movimentos de Saída -... |
| 102540 | 2024-06-19 | ADEQUAÇÃO PARA ENTREGA DA ADRC - PR |
| 77333 | 2023-08-31 | Solicitação de melhoria na exportação de logs e relatórios |

## Keywords para Matching
solicitação, melhoria, exportação, logs, relatórios, adequação, entrega, adrc, atacadao, lentidão
