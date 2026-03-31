---
pattern_id: "sped-falha-de-produto"
vertical: sped
root_cause: falha_de_produto
module: geral
ticket_count: 7
ticket_ids: [19, 9644, 9887, 11595, 12577, 14445, 23642]
last_occurrence: "2021-10-25"
keywords: ["erro", "efd", "reinf", "1000", "retifica\u00e7\u00e3o", "enviar", "reabertura", "periodo", "impeditivo"]
is_not_bug: false
---

# GERAL: Falha De Produto

## Descricao do Padrao
Clientes reportam problemas relacionados a: EFD-REINF - R-1000 - vr 1.4; Erro ao enviar o Reinf 1.5.1; Erro na reabertura de periodo REINF

## Causa Raiz
Falha De Produto — classificacao baseada em 7 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Eduardo, boa tarde
&nbsp;
Conforme exposto, isso corrobora que é uma questão do ambiente + banco de dados quanto a interpretação do valor de data/hora. Por parte de produto estamos avaliando uma implementação para fazer o "de/para" para estes campos de datas, visto que no momento este problema só ocorre para determinados clientes onde estive esta composição citada (JVM + Banco de Dados).
&nbsp;
Entretanto, nos pacotes ainda não temos nenhuma liberação prevista visto que a alteração que foi...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 23642 | 2021-10-06 | REINF - Erro Impeditivo |
| 14445 | 2021-06-23 | Erro na reabertura de periodo REINF |
| 12577 | 2021-06-04 | Erro ao enviar o Reinf 1.5.1 |
| 11595 | 2021-05-24 | Retificação do REINF |
| 9887 | 2021-05-04 | REINF 1.5 |
| 9644 | 2021-04-30 | EFD-REINF - R-1000 - vr 1.4 |
| 19 | 2020-06-09 | erro DW |

## Keywords para Matching
erro, efd, reinf, 1000, retificação, enviar, reabertura, periodo, impeditivo
