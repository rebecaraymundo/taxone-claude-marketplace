---
pattern_id: "sped-falha-de-dados-de-ou-parametros-federal-conexao-onesource-br-ecf-escrituracao-contabil-fiscal"
vertical: sped
root_cause: falha_de_dados_de_ou_parametros
module: federal_conexao_onesource_br_ecf_escrituracao_contabil_fiscal
ticket_count: 3
ticket_ids: [17686, 79472, 84146]
last_occurrence: "2023-12-06"
keywords: ["carga", "ecf", "banco", "erro", "envio", "eventos", "reif", "onesource", "inc35513962", "encerramento"]
is_not_bug: false
---

# FEDERAL CONEXAO ONESOURCE BR ECF ESCRITURACAO CONTABIL FISCAL: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: Carga ECF - Banco a Banco; Erro no envio de eventos REIF para o Onesource; INC35513962 - Encerramento do exercício no TaxOne

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 3 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Bom Dia Diego,
&nbsp;
Conforme acesso remoto identificamos que a URL do parâmetro reinf.webservice.sendAsincUrl estava com o valor https://reinf.receita.economia.gov.br/recepcao/lote, incluímos o 'S' faltante e os eventos foram processados com sucesso!

Valor correto do campo https://reinf.receita.economia.gov.br/recepcao/lotes.
&nbsp;
Passamos as orientações sobre a configuração de envio automático e ajustamos o parâmetro de retorno do governo para o valor de 120 segundos.
&nbsp;
Seguimos a...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 84146 | 2023-11-21 | INC35513962 - Encerramento do exercício no TaxOne |
| 79472 | 2023-09-27 | Erro no envio de eventos REIF para o Onesource |
| 17686 | 2021-07-30 | Carga ECF - Banco a Banco |

## Keywords para Matching
carga, ecf, banco, erro, envio, eventos, reif, onesource, inc35513962, encerramento
