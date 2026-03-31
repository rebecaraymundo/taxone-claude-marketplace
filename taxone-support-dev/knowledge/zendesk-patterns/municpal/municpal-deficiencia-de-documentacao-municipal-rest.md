---
pattern_id: "municpal-deficiencia-de-documentacao-municipal-rest"
vertical: municpal
root_cause: deficiencia_de_documentacao
module: municipal_rest
ticket_count: 3
ticket_ids: [27326, 27176, 32283]
last_occurrence: "2022-02-10"
keywords: ["tipo", "servi\u00e7o", "prestador", "goi\u00e2nia", "rest", "al\u00edquota", "base", "iss", "obrigat\u00f3rio", "prefeituras"]
is_not_bug: false
---

# MUNICIPAL REST: Deficiencia De Documentacao

## Descricao do Padrao
Clientes reportam problemas relacionados a: Alíquota e Base de ISS obrigatório - Goiânia-Rest; REST - Prefeituras GO; Tipo do serviço do prestador - Goiânia Rest

## Causa Raiz
Deficiencia De Documentacao — classificacao baseada em 3 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Luciano, bom dia!
&nbsp;
Por gentileza verificar a regra abaixo para geração de cada código do campo "Tipo do Serviço do Prestador", verificar que o DE X PARA é realizado para o município do Prestador e não do Tomador.
&nbsp;
Regra do Registro D – Tipo do serviço do prestador
&nbsp;
Preencher com:
&nbsp;
0, quando nenhuma das outras opções forem verdadeiras;
&nbsp;
2, quando&nbsp;o campo&nbsp;IND_CLASSE_PFJ da tabela SAFX04 = “07”, se não estiver preenchido verificar se o serviço e o município...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 32283 | 2022-01-27 | REST - Prefeituras GO |
| 27326 | 2021-11-26 | Tipo do serviço do prestador - Goiânia Rest |
| 27176 | 2021-11-24 | Alíquota e Base de ISS obrigatório - Goiânia-Rest |

## Keywords para Matching
tipo, serviço, prestador, goiânia, rest, alíquota, base, iss, obrigatório, prefeituras
