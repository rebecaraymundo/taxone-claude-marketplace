---
pattern_id: "estadual-falha-de-dados-de-ou-parametros-estadual-lançamentos-automáticos-de-icms"
vertical: estadual
root_cause: falha_de_dados_de_ou_parametros
module: estadual_lançamentos_automáticos_de_icms
ticket_count: 5
ticket_ids: [118509, 140760, 142444, 152261, 170825]
last_occurrence: "2026-02-11"
keywords: ["bug", "c\u00e1lculo", "autom\u00e1tico", "lan\u00e7amento", "estorno", "cpfl_falha", "tax", "one", "sandoz", "erro"]
is_not_bug: false
---

# ESTADUAL LANÇAMENTOS AUTOMÁTICOS DE ICMS: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: Bug| Cálculo Automático Lançamento Estorno de Crédito Anulação de Transporte; CPFL_Falha Tax One; ICMS - Documentos Fiscais Vinculados (Tipo 2) - REGISTRO E113 (SAFX218) - ESCRITURAÇÃO POSTERIOR A APURAÇÃO

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 5 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde a todos!
&nbsp;
Conforme as orientações recebidas, o sistema estava calculando o Diferencial de Alíquotas de forma incorreta devido à configuração inadequada de um campo (conforme anexo). O time de produto identificou que havia um parâmetro incorreto na T01: o valor estava como "4", quando, para a filial de São Paulo, o correto seria "2", pois o cálculo do DIFAL é diferente nesse caso.

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 170825 | 2026-01-21 | ICMS - Documentos Fiscais Vinculados (Tipo 2) - REGISTRO... |
| 152261 | 2025-09-17 | REF. FECHAMENTO LIVRO ICMS REF AGOSTO/25 FILIAL 001 |
| 142444 | 2025-07-03 | [SANDOZ] - erro ao cadastrar lançamento automático  |
| 140760 | 2025-06-18 | CPFL_Falha Tax One |
| 118509 | 2024-12-04 | Bug| Cálculo Automático Lançamento Estorno de Crédito... |

## Keywords para Matching
bug, cálculo, automático, lançamento, estorno, cpfl_falha, tax, one, sandoz, erro
