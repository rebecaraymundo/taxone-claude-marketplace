---
pattern_id: "estadual-falha-de-dados-de-ou-parametros-estadual-dimp"
vertical: estadual
root_cause: falha_de_dados_de_ou_parametros
module: estadual_dimp
ticket_count: 4
ticket_ids: [53786, 53736, 66222, 107209]
last_occurrence: "2024-08-28"
keywords: ["melhoria", "meio", "magn\u00e9tico", "dimp", "erro", "gera\u00e7\u00e3o", "campo", "ind_nat_jur", "falta", "reg"]
is_not_bug: false
---

# ESTADUAL DIMP: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: DIMP - ERRO CAMPO IND_NAT_JUR; DIMP - Falta geração REG 0200; Erro geração meio magnético DIMP

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 4 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Geison, boa tarde
&nbsp;
Conforme verificado a não geração não é devido ao código do meio de Captura e sim pelo o cliente ser Pessoa Física, realizado um teste com os mesmo dados com o cliente sendo Pessoa Jurídica a informação foi gerada no arquivo.
&nbsp;
De acordo com o Manual de Layout da DIMP:
&nbsp;
Não deverão ser reportadas as transações cujo valor total mensal recebido por pessoa física, seja inferior a R$ 3.375,00 ou menos que 30 transações, ou seja, somente serão reportados...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 107209 | 2024-08-12 | DIMP - Falta geração REG 0200 |
| 66222 | 2023-04-14 | DIMP - ERRO CAMPO IND_NAT_JUR |
| 53786 | 2022-10-31 | Melhoria meio magnético DIMP |
| 53736 | 2022-10-31 | Erro geração meio magnético DIMP |

## Keywords para Matching
melhoria, meio, magnético, dimp, erro, geração, campo, ind_nat_jur, falta, reg
