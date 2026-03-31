---
pattern_id: "sped-falha-de-dados-de-ou-parametros"
vertical: sped
root_cause: falha_de_dados_de_ou_parametros
module: geral
ticket_count: 18
ticket_ids: [9808, 10458, 10428, 10905, 13959, 13827, 15898, 19020, 20470, 20266, 20602, 24202, 24213, 24082, 24512, 40266, 43275, 50798]
last_occurrence: "2025-02-17"
keywords: ["tax", "one", "reinf", "mensageria", "n\u00e3o", "entrega", "extempor\u00e2nea", "erro", "evento", "br20"]
is_not_bug: false
---

# GERAL: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: EFD REINF - EVENTO 2098; EFD Reinf - Envio para o Onesource não está funcionando; Entrega extemporânea de REINF, erro "Evento impedido, pois não foi encontrado evento de Informações do Contribuinte aceito pelo governo e com vigência

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 18 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Fábio, boa tarde.&nbsp;
&nbsp;
Apenas matar o processamento em banco não resolve a questão de processamento dos serviços. É preciso limpar as filas do AMQ
&nbsp;
  Pare todos os serviços.&nbsp;  Delete o conteúdo da pasta DATA do ActiveMQ  Suba os serviços novamente  Deixem o Integrador do ECF parado e subam apenas REINF  &nbsp;
Peça para o usuário realizar um teste do REINF para análise de performance.&nbsp;


  Jheferson Crescencio

Thomson Reuters

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 50798 | 2022-09-19 | Evento R2098 - Em Processamento (Mensageria)  |
| 43275 | 2022-06-13 | Integrador está fora, envio insdiponivel |
| 40266 | 2022-05-05 | Retorno Onesource para DW - Reinf |
| 24512 | 2021-10-19 | EFD REINF - EVENTO 2098 |
| 24213 | 2021-10-14 | Evento do REINF aprovado no Onesource e Rejeitado no DW |
| 24202 | 2021-10-14 | EFD Reinf - Envio para o Onesource não está funcionando |
| 24082 | 2021-10-13 | Problema na Geração do REINF |
| 20602 | 2021-08-30 | Unidas - Erro extração CAD2003 |
| 20470 | 2021-08-27 | Evento não está enviando xml para a mensageria |
| 20266 | 2021-08-25 | Status Evento REINF |

## Keywords para Matching
tax, one, reinf, mensageria, não, entrega, extemporânea, erro, evento, br20
