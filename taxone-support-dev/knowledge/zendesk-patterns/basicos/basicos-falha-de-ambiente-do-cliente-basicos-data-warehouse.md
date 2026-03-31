---
pattern_id: "basicos-falha-de-ambiente-do-cliente-basicos-data-warehouse"
vertical: basicos
root_cause: falha_de_ambiente_do_cliente
module: basicos_data_warehouse
ticket_count: 231
ticket_ids: [719, 189, 204, 1556, 2713, 2552, 2544, 2400, 3440, 3401, 2892, 3675, 4554, 4208, 4349, 4088, 5048, 4834, 4926, 4752, 4738, 4723, 6232, 6577, 7155, 9177, 10586, 10285, 11133, 12013, 11836, 13333, 14155, 14494, 14669, 15227, 16280, 16168, 17294, 19146, 19385, 19376, 19950, 20658, 20657, 20568, 21023, 21118, 21775, 21618, 22242, 22846, 23129, 23484, 23393, 24552, 24961, 25215, 24929, 25746, 25745, 26345, 26245, 25981, 26258, 25907, 26645, 26581, 26457, 26446, 27261, 27255, 27586, 28230, 27944, 28785, 29586, 29916, 30789, 30628, 30625, 30631, 30630, 31360, 30939, 31116, 30874, 31459, 31640, 31618, 32172, 32080, 32266, 32609, 32763, 33279, 33873, 33860, 33590, 33539, 34482, 34589, 34979, 35412, 36222, 36078, 36020, 35880, 36709, 36444, 37212, 37623, 38111, 37979, 38697, 39494, 40445, 40852, 43328, 43603, 44630, 46198, 46104, 47928, 50100, 52423, 53614, 53384, 53723, 54606, 54584, 54455, 55334, 56273, 56886, 56670, 57449, 58296, 59034, 58871, 58754, 58579, 60083, 60352, 60312, 60631, 62514, 62497, 62382, 62375, 62329, 62296, 63397, 65122, 67164, 66968, 67834, 67688, 69412, 69372, 70562, 71461, 72350, 73142, 72915, 75733, 75347, 76181, 76075, 80386, 82316, 85451, 87162, 88297, 91900, 93355, 95353, 99171, 101760, 105806, 107445, 108858, 111165, 110739, 111858, 112475, 112400, 113044, 112786, 113919, 114669, 115261, 114895, 114824, 116140, 116935, 117561, 122369, 123505, 122997, 123971, 126403, 130567, 133605, 136058, 135981, 138486, 140090, 141006, 140509, 141463, 142505, 143474, 143077, 146398, 146370, 148288, 149060, 148848, 151033, 152517, 154733, 155743, 156654, 159126, 163361, 168724, 170711, 170059, 172345, 175083]
last_occurrence: "2026-03-05"
keywords: ["lentid\u00e3o", "equalizar", "tax", "one", "senha", "acesso", "prd", "erro", "atualiza\u00e7\u00e3o", "patch"]
is_not_bug: false
---

# BASICOS DATA WAREHOUSE: Falha De Ambiente Do Cliente

## Descricao do Padrao
Clientes reportam problemas relacionados a:  Erro na execução da Stored Procedure; #57657 - Continuação - Senha base de dados - Qual o procedimento/recomendação?; (Embraport) - Lentidão excessiva

## Causa Raiz
Falha De Ambiente Do Cliente — classificacao baseada em 231 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Jayme, bom dia!
&nbsp;
Verificamos que uma usuária estava executando 2 processos de datamart com período de 01/01/2017 até 31/01/2027. Esse período de quase 10 anos processa uma imensidão de dados e concorre com as outras gerações. Orientá-la e verificar se o procedimento está correto, pois geralmente se processa mês a mês.
&nbsp;
Além disso, haviam algum carimbos (updates) apresentando problemas com muitos paralelismos e concorrendo com asoutras sessões e o Eli corrigiu.
&nbsp;
As próximas...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 175083 | 2026-02-20 | Opção Empresa sem informação |
| 172345 | 2026-02-02 | Problema de performance na equalização do datamart |
| 170711 | 2026-01-21 | Manutenção na Capa e item - não salva |
| 170059 | 2026-01-16 | Performance  |
| 168724 | 2026-01-09 | O balancete gerado não possui uma estrutura de balanço e... |
| 163361 | 2025-12-02 | Erro para salvar notas fiscais |
| 159126 | 2025-11-03 | Erro ao listar os arquivos do NAS |
| 156654 | 2025-10-17 | Erro na geração da equalização |
| 155743 | 2025-10-13 | STELLANTIS | Erro geração de relatórios |
| 154733 | 2025-10-06 | Erro Mastersaf DW Após aplicicar Patch |

## Keywords para Matching
lentidão, equalizar, tax, one, senha, acesso, prd, erro, atualização, patch
