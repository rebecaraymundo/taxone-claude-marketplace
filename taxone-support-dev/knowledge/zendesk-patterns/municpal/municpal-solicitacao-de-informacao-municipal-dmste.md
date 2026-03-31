---
pattern_id: "municpal-solicitação-de-informacao-municipal-dmste"
vertical: municpal
root_cause: solicitação_de_informacao
module: municipal_dmste
ticket_count: 2
ticket_ids: [29885, 91871]
last_occurrence: "2024-03-14"
keywords: ["dmst", "campo", "parametriza\u00e7\u00e3o", "iss"]
is_not_bug: false
---

# MUNICIPAL DMSTE: Solicitação De Informacao

## Descricao do Padrao
Clientes reportam problemas relacionados a: DMST - Campo Bom - Parametrização; ISS - Campo Bom

## Causa Raiz
Solicitação De Informacao — classificacao baseada em 2 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Matheus, boa tarde!
&nbsp;
Conforme acesso realizado, verificamos que o erro estava ocorrendo porque no arquivo o campo Tipo ISS estava preenchido como N - Não Retido, o que impactava
na campo Cidade de Tributação. Após realizado um teste alterando para F- Fora do municipio, não ocorreu o erro.
&nbsp;
Desta forma, segue abaixo a regra de geração para o código F, M e N.
&nbsp;
Preencher com ‘F’ – ISSQN Fora do Município:
&nbsp;
Se o serviço e o município do prestador (Pessoa Fis/Jur) cadastrados...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 91871 | 2024-02-26 | ISS - Campo Bom |
| 29885 | 2021-12-24 | DMST - Campo Bom - Parametrização |

## Keywords para Matching
dmst, campo, parametrização, iss
