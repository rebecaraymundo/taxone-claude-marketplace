---
pattern_id: "sped-falha-de-ambiente-do-cliente"
vertical: sped
root_cause: falha_de_ambiente_do_cliente
module: geral
ticket_count: 34
ticket_ids: [10158, 10102, 9757, 10631, 10367, 11475, 10992, 12096, 11961, 11919, 12752, 13335, 13278, 13201, 13346, 13331, 13302, 13050, 14103, 13847, 13841, 16001, 18149, 18735, 18493, 20622, 21057, 21708, 21585, 21724, 21582, 38292, 42604, 43234]
last_occurrence: "2022-06-29"
keywords: ["erro", "integrador", "envio", "eventos", "mensageria", "reinf", "r2055", "evento", "r2099", "periodo"]
is_not_bug: false
---

# GERAL: Falha De Ambiente Do Cliente

## Descricao do Padrao
Clientes reportam problemas relacionados a: EFD REINF; EFD REINF -  ERRO NA ABERTURA DO PERIODO; EFD REINF - MSAF

## Causa Raiz
Falha De Ambiente Do Cliente — classificacao baseada em 34 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Charles, bom dia.&nbsp;
&nbsp;
Conforme acesso remoto, o serviço da mensageria estava funcional, o evento estava travado no painel LOTE, foi preciso usar o botão "desbloquear" lotes para o envio ocorrer.&nbsp;
 Recentemente os serviços da Apache sofreram com ataques devido a vulnerabilidade em bibliotecas do log4j, e com isso várias alterações foram feitas no produto e no deploy do Apache TomCat, homologamos para o Produto:&nbsp;
&nbsp;
  TomCat-9.0.63.exe  Apache Activemq-5.17.1  Amazon...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 43234 | 2022-06-10 | NORDEX - ONESOURCE INTEGRADOR ERROR |
| 42604 | 2022-06-02 | Mensageria esta parada no DW |
| 38292 | 2022-04-07 | EFD REINF |
| 21724 | 2021-09-14 | Processo em processamento |
| 21708 | 2021-09-14 | EFD REINF -  ERRO NA ABERTURA DO PERIODO |
| 21585 | 2021-09-13 | EFD REINF - MSAF |
| 21582 | 2021-09-13 | Erro ao enviar eventos do REINF |
| 21057 | 2021-09-03 | Evento R-2098 - Rejeitado com periodo indevido |
| 20622 | 2021-08-31 | Re: EFD - REINF - O integrador está fora, envio... |
| 18735 | 2021-08-10 | REINF |

## Keywords para Matching
erro, integrador, envio, eventos, mensageria, reinf, r2055, evento, r2099, periodo
