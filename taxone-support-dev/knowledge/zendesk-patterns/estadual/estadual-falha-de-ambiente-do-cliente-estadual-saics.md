---
pattern_id: "estadual-falha-de-ambiente-do-cliente-estadual-saics"
vertical: estadual
root_cause: falha_de_ambiente_do_cliente
module: estadual_saics
ticket_count: 2
ticket_ids: [24476, 51646]
last_occurrence: "2022-12-15"
keywords: ["erro", "gera\u00e7\u00e3o", "devolu\u00e7\u00e3o", "ficha", "saics", "sistema", "apura\u00e7\u00e3o", "icms", "falta"]
is_not_bug: false
---

# ESTADUAL SAICS: Falha De Ambiente Do Cliente

## Descricao do Padrao
Clientes reportam problemas relacionados a: Erro na geração da devolução na Ficha 3A do SAICS; SAICS - Sistema de apuração do ICMS - Falta Registro 0150

## Causa Raiz
Falha De Ambiente Do Cliente — classificacao baseada em 2 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Olá Alessandro,
&nbsp;
O problema inicial era a duplicidade de linhas geradas na devolução, que foi causada por informações a mais que tinham na TFIX81 na base do cliente.
Provavelmente em algum momento foi incluída manualmente nesse arquivo txt essa linha a mais, com cód. de lançamento 773178 no registro 5315, e essa tabela foi importada no sistema, o pacote enviado corrigiu essas informações indevidas que continham nessa tabela, deixando a TFIX81 padrão do sistema.
&nbsp;
Segue abaixo print...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 51646 | 2022-09-30 | SAICS - Sistema de apuração do ICMS - Falta Registro 0150 |
| 24476 | 2021-10-19 | Erro na geração da devolução na Ficha 3A do SAICS |

## Keywords para Matching
erro, geração, devolução, ficha, saics, sistema, apuração, icms, falta
