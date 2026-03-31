---
pattern_id: "municpal-falha-de-dados-de-ou-parametros-municipal-nota-joseense"
vertical: municpal
root_cause: falha_de_dados_de_ou_parametros
module: municipal_nota_joseense
ticket_count: 7
ticket_ids: [51225, 52946, 115376, 117481, 142635, 165777, 171175]
last_occurrence: "2026-02-26"
keywords: ["erro", "c\u00f3digo", "servi\u00e7o", "tipo", "recolhimento", "gera\u00e7\u00e3o", "iss", "s\u00e3o", "campos", "nota"]
is_not_bug: false
---

# MUNICIPAL NOTA JOSEENSE: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: Arquivo ISS Campinas; DFSNET SOROCABA; Erro Código Serviço e Tipo de Recolhimento

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 7 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Thays, bom dia!
&nbsp;
No layout de Campinas há 2 campos que indicam se o ISS é retido ou não. O campo "Tipo recolhimento imposto" e campo
&nbsp;"Exigibilidade do ISS". Segue regra de geração:
&nbsp;
&nbsp;Exigibilidade do ISS (este campo há varias opções, abaixo segue a regra das mais utilizadas)
&nbsp;
Gerar com 2 - Não Incidência:
&nbsp;
Verificar se o serviço e o município do prestador cadastrado na nota estão parametrizados no Módulo Parâmetros por Município &gt;
Classificação de Serviços...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 171175 | 2026-01-23 | MOBILIDADE - MUNICIPAL - BELÉM-PA - DFSNET-NOTA JOSEEENSE |
| 165777 | 2025-12-16 | Re: Geracao meio magnetico ISS campinas - valeo - producao |
| 142635 | 2025-07-04 | Arquivo ISS Campinas |
| 117481 | 2024-11-26 | Tipo de Recolhimento Sorocaba |
| 115376 | 2024-11-07 | DFSNET SOROCABA |
| 52946 | 2022-10-19 | Geração ISS São Jo´se do Campos - NOTA JOSEENSE |
| 51225 | 2022-09-26 | Erro Código Serviço e Tipo de Recolhimento |

## Keywords para Matching
erro, código, serviço, tipo, recolhimento, geração, iss, são, campos, nota
