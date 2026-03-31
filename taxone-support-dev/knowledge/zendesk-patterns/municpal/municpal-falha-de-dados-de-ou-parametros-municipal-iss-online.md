---
pattern_id: "municpal-falha-de-dados-de-ou-parametros-municipal-iss-online"
vertical: municpal
root_cause: falha_de_dados_de_ou_parametros
module: municipal_iss_online
ticket_count: 3
ticket_ids: [76336, 110423, 156669]
last_occurrence: "2025-11-03"
keywords: ["sesi_iss_itapetininga", "erro", "importar", "arquivo", "prefeitura", "barcarena", "gera\u00e7\u00e3o", "municipal", "monte", "mor"]
is_not_bug: false
---

# MUNICIPAL ISS ONLINE: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: Erro ao importar arquivo na Prefeitura de Barcarena; Erro geração Municipal de Monte Mor. Não traz Situação.; SESI_ISS_ITAPETININGA

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 3 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Olá Daniela, boa tarde!
&nbsp;
Conforme conversamos em acesso, para a geração da Situação "3" “ – Isenta no arquivo de ISS de Itapetininga, ajustar o campo 26 IND_CLASSE_PFJ da tabela SAFX04 PESSOA FIS_JUR = “10”, conforme detalha na regra abaixo:
&nbsp;
Para notas Recebidas: Verificar se o campo INDCLASSEPFJ da tabela X04PESSOAFISJUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador (Pessoa Fis/Jur) cadastrados na nota estão parametrizado na tela Parâmetros –...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 156669 | 2025-10-17 | Erro geração Municipal de Monte Mor. Não traz Situação. |
| 110423 | 2024-09-19 | Erro ao importar arquivo na Prefeitura de Barcarena |
| 76336 | 2023-08-21 | SESI_ISS_ITAPETININGA |

## Keywords para Matching
sesi_iss_itapetininga, erro, importar, arquivo, prefeitura, barcarena, geração, municipal, monte, mor
