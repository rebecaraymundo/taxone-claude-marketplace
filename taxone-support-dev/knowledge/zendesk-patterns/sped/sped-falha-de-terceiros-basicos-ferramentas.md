---
pattern_id: "sped-falha-de-terceiros-basicos-ferramentas"
vertical: sped
root_cause: falha_de_terceiros
module: basicos_ferramentas
ticket_count: 2
ticket_ids: [31501, 39624]
last_occurrence: "2022-05-23"
keywords: ["atualiza\u00e7\u00e3o", "patch", "mastersaf", "vers\u00e3o", "262", "homologa\u00e7\u00e3o", "onesource", "erro"]
is_not_bug: false
---

# BASICOS FERRAMENTAS: Falha De Terceiros

## Descricao do Padrao
Clientes reportam problemas relacionados a: Atualização do Patch Mastersaf-DW Versão: Versão: 262.1.1 e Onesource Versão: 1R18700 no ambiente de homologação; Homologação de versão do onesource com erro

## Causa Raiz
Falha De Terceiros — classificacao baseada em 2 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Carla, boa tarde.&nbsp;
&nbsp;
Este cenário está ocorrendo devido a problemas no próprio Governo.&nbsp;
&nbsp;
Falha no Governo (falha de terceiro)&nbsp;
&nbsp;
Pelas evidências e testes realizados, identificamos o seguinte cenário:
&nbsp;
O Governo está rejeitando os lotes quando o mesmo está com muitos eventos, ou seja, ao realizar o envio de um lote onde tenha mais de 10 eventos associados, esta gerando a seguinte mensagem nos logs da mensageria:
&nbsp;
  HTTP response '413: Request Entity...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 39624 | 2022-04-27 | Homologação de versão do onesource com erro |
| 31501 | 2022-01-18 | Atualização do Patch Mastersaf-DW Versão: Versão: 262.1.1 e... |

## Keywords para Matching
atualização, patch, mastersaf, versão, 262, homologação, onesource, erro
