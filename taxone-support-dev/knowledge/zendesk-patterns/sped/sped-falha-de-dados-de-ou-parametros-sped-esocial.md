---
pattern_id: "sped-falha-de-dados-de-ou-parametros-sped-esocial"
vertical: sped
root_cause: falha_de_dados_de_ou_parametros
module: sped_esocial
ticket_count: 5
ticket_ids: [2265, 3254, 3166, 4800, 41944]
last_occurrence: "2022-07-12"
keywords: ["esocial", "evento", "1200", "rejeitado", "erro", "integra\u00e7\u00e3o", "leiaute", "inv\u00e1lida"]
is_not_bug: false
---

# SPED ESOCIAL: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: Erro de Leiaute do evento inválida no eSocial; Erro integração ESOCIAL; Esocial evento S-1200 rejeitado no DW

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 5 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Douglas, bom dia

Conforme citado, o produto não permite realizar clone para o ONESOURCE, justamente pelo fato dos eventos serem de PRODUÇÃO, onde não sera possível realizar alteração do ambiente para HOMOLOGAÇÃO, logo os dados não serão compatíveis para uso, portanto não faz sentido realizar este tipo de clone para o ONESOURCE.

Quanto a questão de clone do Mastersaf DW, gera-se o impacto de mudar toda a cadeia de número de PROTOCOLOS, portanto se o integrador começar a buscar informações de...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 41944 | 2022-05-25 | Erro de Leiaute do evento inválida no eSocial |
| 4800 | 2021-03-03 | Esocial evento S-1200 rejeitado no DW |
| 3254 | 2021-02-11 | Erro integração ESOCIAL |
| 3166 | 2021-02-10 | Erro integração ESOCIAL |
| 2265 | 2021-02-02 | Esocial evento S-1200 rejeitado no DW |

## Keywords para Matching
esocial, evento, 1200, rejeitado, erro, integração, leiaute, inválida
