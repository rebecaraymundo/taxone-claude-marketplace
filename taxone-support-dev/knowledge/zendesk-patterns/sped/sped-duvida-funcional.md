---
pattern_id: "sped-duvida-funcional"
vertical: sped
root_cause: duvida_funcional
module: geral
ticket_count: 9
ticket_ids: [9275, 14882, 14739, 15284, 16530, 18243, 20426, 21418, 28888]
last_occurrence: "2021-12-29"
keywords: ["integrador", "onesouce", "indispon\u00edvel", "evento", "reabertura", "r2098", "erro", "reinf", "teste", "oat"]
is_not_bug: true
---

# GERAL: Duvida Funcional

## Descricao do Padrao
Clientes reportam problemas relacionados a: ERRO  XML ; Evento de reabertura R2098 com erro.; Evento em "Processamento de Mensageria"

## Causa Raiz
Duvida Funcional — classificacao baseada em 9 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Carlos, bom dia
&nbsp;
Para este cenário, precisa ser avaliado a questão internamente, quanto a questões de Certificado Digital e vínculos no eCAC, visto que para o módulo da EFD-REINF, o CNPJ a ser utilizado é apenas a raiz do mesmo, desta forma, não importa se o final do CNPJ era um e agora é outro, desde que a raiz do CNPJ seja a mesma.

Portanto, os senhores precisam avaliar a questão do Certificado Digital a ser vinculado para o CNPJ que que será utilizado para autenticar os eventos...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 28888 | 2021-12-14 | [EXT] RES: [Thomson Reuters] Re: Ticket 20741 - 99 TECH -... |
| 21418 | 2021-09-10 | erro envio Registro R2010 REINF |
| 20426 | 2021-08-27 | Reabertura período NOV2019 |
| 18243 | 2021-08-05 | Evento em "Processamento de Mensageria" |
| 16530 | 2021-07-16 | ERRO  XML  |
| 15284 | 2021-07-02 | Fechamento de período |
| 14882 | 2021-06-28 | Evento de reabertura R2098 com erro. |
| 14739 | 2021-06-25 | Reinf - Teste em OAT |
| 9275 | 2021-04-27 | Integrador Onesouce indisponível |

## Keywords para Matching
integrador, onesouce, indisponível, evento, reabertura, r2098, erro, reinf, teste, oat
