---
pattern_id: "utilitarios-falha-de-ambiente-do-cliente"
vertical: utilitarios
root_cause: falha_de_ambiente_do_cliente
module: geral
ticket_count: 16
ticket_ids: [58, 468, 11511, 12528, 22842, 24720, 27070, 28550, 33753, 35061, 45046, 54666, 91839, 120278, 122507, 143532]
last_occurrence: "2025-07-22"
keywords: ["teste", "projeto", "migra\u00e7\u00e3o", "taxone", "resultado", "schemadiff", "vers\u00e3o", "254", "acesso", "base"]
is_not_bug: false
---

# GERAL: Falha De Ambiente Do Cliente

## Descricao do Padrao
Clientes reportam problemas relacionados a: Acesso a base de treinamento ; Atualização patch 261.1.0 -ambiente de homologação - GRPCOM; BASF - Erro na conexão com banco de dados Conector INFOR

## Causa Raiz
Falha De Ambiente Do Cliente — classificacao baseada em 16 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Prezado(a) Ricardo,
&nbsp;
Favor conectar no SQL*Plus com o usuário SYS ou SYSTEM &nbsp;e executar a consulta abaixo
++++++++++++++++++++++++++++++
&nbsp;
select *
from dba_errors
where owner='MSAFPROD';
&nbsp;
++++++++++++++++++++++++++++++
&nbsp;
Foi realizado algum refresh de base neste ambiente?
&nbsp;
Att;
Valmir R. Brito
Thomson Reuters

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 143532 | 2025-07-14 | Problema no envio de arquivos para ONESOURCE |
| 122507 | 2025-01-21 | Erro na aplicaçãol do patch 302 |
| 120278 | 2024-12-20 | Erro na atualização de patch 301.0.1 |
| 91839 | 2024-02-26 | OBTI - Request Customizing  incopátivel com a versão pacote... |
| 54666 | 2022-11-11 | BASF - Erro na conexão com banco de dados Conector INFOR |
| 45046 | 2022-07-06 | Ocorreu um erro no sistema - Mastersaf DW |
| 35061 | 2022-02-24 | Lentidão ao abrir o item de menu customizados |
| 33753 | 2022-02-10 | Schemadiff para a versão 264.0.0 |
| 28550 | 2021-12-10 | Importação de DUMP para a Base do Tax One - Homologação |
| 27070 | 2021-11-23 | Atualização patch 261.1.0 -ambiente de homologação - GRPCOM |

## Keywords para Matching
teste, projeto, migração, taxone, resultado, schemadiff, versão, 254, acesso, base
