---
pattern_id: "basicos-falha-de-terceiros-basicos-ferramentas"
vertical: basicos
root_cause: falha_de_terceiros
module: basicos_ferramentas
ticket_count: 3
ticket_ids: [52054, 156992, 156913]
last_occurrence: "2025-11-03"
keywords: ["rejei\u00e7\u00e3o", "notas", "ambiente", "homologa\u00e7\u00e3o", "dfe", "impossibilidade", "acessar", "tax", "one", "erro"]
is_not_bug: false
---

# BASICOS FERRAMENTAS: Falha De Terceiros

## Descricao do Padrao
Clientes reportam problemas relacionados a: Erro TAx One; Impossibilidade de acessar ao Tax one; Rejeição de notas no ambiente de homologação DFe

## Causa Raiz
Falha De Terceiros — classificacao baseada em 3 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Douglas,
&nbsp;
Novamente foi um retorno da SEFAZ:
&nbsp;
2022-10-14 17:34:33,727 INFO b.c.m.i.s.HttpClientUtil [pool-2-thread-9992] /ws/NfeAutorizacao/NFeAutorizacao4.asmx : The page was not displayed because the request entity is too large.
2022-10-14 17:34:33,727 INFO b.c.m.m.b.WebserviceBPMBase [pool-2-thread-9992] status: 413
&nbsp;
Sugerimos um contato diretamente com a mesma para questionar por que essa nota não foi processada, com o xml em anexo.
&nbsp;
Ficamos à disposição.


 ...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 156992 | 2025-10-20 | Impossibilidade de acessar ao Tax one |
| 156913 | 2025-10-20 | Erro TAx One |
| 52054 | 2022-10-06 | Rejeição de notas no ambiente de homologação DFe |

## Keywords para Matching
rejeição, notas, ambiente, homologação, dfe, impossibilidade, acessar, tax, one, erro
