# MTZ_Documento_Utilities_Capa_Reforma_Tributária_SAFX3042

> Fonte: MTZ_Documento_Utilities_Capa_Reforma_Tributária_SAFX3042.docx






THOMSON REUTERS

TAXONE
Básicos / Data Warehouse /
Documento Fiscal / Documento Fiscal Utilities
CAPA – REFORMA TRIBUTÁRIA – SAFX3042



DOCUMENTO DE REQUISITO

Sumário

1.	Objetivo	3
2.	Tela	3
3.	Regras dos Campos	4






















## Objetivo


Criar tela de documentos fiscais de Utilities (Capa), referente à SAFX3042, que contempla os campos da reforma tributária.
## Tela


## Regras dos Campos


Localização da tela: Módulo: Básicos>> Data Warehouse
Menu: Manutenção >> Documento Fiscal >> Documento Fiscal Utilities

Título da tela: Novo Documento Fiscal Utilities

Aba CAPA >>  Radio buton, selecionada a opção Reforma






| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-859982 | Alessandra Cristina Navatta | Criação da tela Capa do Documento de Utilities – Reforma Tributária (SAFX3042) |
| MFS-951840 | Alessandra Cristina Navatta | Em atendimento ao INFOLEGIS 2191/25 - M - NFCOM - NT RTC 2025.001_v.1.10, temos:  Exclusão dos campos de Crédito Presumido Inclusão dos campos de valor do tributo de Tributação Regular do IBS UF, IBS MUN e CBS (Agrupamento Totais da Tributação Regular) Inclusão dos campos de valor do tributo do IBS UF, IBS MUN e CBS, referente as comprar governamentais e reordenação do campo de percentual de redução de alíquota de compras governamentais. Inclusão dos campos de Estorno de Créditos (Agrupamento Totais de Estorno de Créditos) |
|  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Aba CAPA | Aba CAPA | Aba CAPA | Aba CAPA | Aba CAPA | Aba CAPA | Aba CAPA |
| Reforma | Radio-Buton |  |  |  | Quando marcada a opção Reforma, exibir os campos mencionados a seguir | MFS-859982 |
| Tipo Ente | Lista | N | S |  | Lista de Valores válidos:  1-União 2-Estados 3-Distrito Federal 4-Municípios | MFS-859982 |
| IBS/CBS | IBS/CBS | IBS/CBS | IBS/CBS | IBS/CBS | IBS/CBS | IBS/CBS |
| Total Base Cálculo IBS/CBS | Numérico | N | S | 0,00 | Informar o valor do Total da Base de Cálculo IBS/CBS | MFS-859982 |
| Totais do IBS | Totais do IBS | Totais do IBS | Totais do IBS | Totais do IBS | Totais do IBS | Totais do IBS |
| IBS UF | Numérico | N | S | 0,00 | Informar o valor do IBS UF | MFS-859982 |
| Devolução IBS UF | Numérico | N | S | 0,00 | Informar o valor da Devolução IBS UF | MFS-859982 |
| Diferimento IBS UF | Numérico | N | S | 0,00 | Informar o valor do Diferimento IBS UF | MFS-859982 |
| IBS Municipal | Numérico | N | S | 0,00 | Informar o valor do IBS Municipal | MFS-859982 |
| Devolução IBS Municipal | Numérico | N | S | 0,00 | Informar o valor da Devolução IBS Municipal | MFS-859982 |
| Diferimento IBS Municipal | Numérico | N | S | 0,00 | Informar o valor do Diferimento IBS Municipal | MFS-859982 |
| IBS (IBS UF + IBS Municipal) | Numérico | N | S | 0,00 | Informar o valor total do IBS (somatório do IBS UF e IBS Municipal) | MFS-859982 |
| Totais Crédito Presumido | Totais Crédito Presumido | Totais Crédito Presumido | Totais Crédito Presumido | Totais Crédito Presumido | Totais Crédito Presumido |  |
| IBS | Numérico | N | S | 0,00 | Informar o valor do Crédito Presumido IBS | MFS-859982 |
| Condição Suspensiva IBS | Numérico | N | S | 0,00 | Informar o valor do Crédito Presumido Condição Suspensiva IBS | MFS-859982 |
| CBS | Numérico | N | S | 0,00 | Informar o valor do Crédito Presumido CBS | MFS-859982 |
| Condição Suspensiva CBS | Numérico | N | S | 0,00 | Informar o valor do Crédito Presumido Condição Suspensiva CBS | MFS-859982 |
| Totais da CBS | Totais da CBS | Totais da CBS | Totais da CBS | Totais da CBS | Totais da CBS | Totais da CBS |
| CBS | Numérico | N | S | 0,00 | Informar o valor da CBS | MFS-859982 |
| Devolução CBS | Numérico | N | S | 0,00 | Informar o valor da Devolução CBS | MFS-859982 |
| Diferimento CBS | Numérico | N | S | 0,00 | Informar o valor do Diferimento CBS | MFS-859982 |
| Totais da Tributação Regular | Totais da Tributação Regular | Totais da Tributação Regular | Totais da Tributação Regular | Totais da Tributação Regular | Totais da Tributação Regular | Totais da Tributação Regular |
| IBS UF | Numérico | N | S | 0,00 | Informar o valor do IBS UF da tributação Regular | MFS-951840 |
| IBS Municipal | Numérico | N | S | 0,00 | Informar o valor total do IBS Municipal da tributação Regular | MFS-951840 |
| CBS | Numérico | N | S | 0,00 | Informar o valor total da CBS da tributação Regular | MFS-951840 |
| Totais Compras Governamentais | Totais Compras Governamentais | Totais Compras Governamentais | Totais Compras Governamentais | Totais Compras Governamentais | Totais Compras Governamentais | Totais Compras Governamentais |
| Percentual Redução Alíquota-Compra Governamental | Numérico | N | S | 0,0000 | Informar o Percentual de Redução de Alíquota em Compra Governamental | MFS-859982 MFS-951840 |
| IBS UF | Numérico | N | S | 0,00 | Informar o valor do IBS UF utilizados em compras governamentais. | MFS-951840 |
| IBS Municipal | Numérico | N | S | 0,00 | Informar o valor total do IBS utilizados em compras governamentais. | MFS-951840 |
| CBS | Numérico | N | S | 0,00 | Informar o valor total da CBS utilizados em compras governamentais. | MFS-951840 |
| Totais de Estorno de Créditos | Totais de Estorno de Créditos | Totais de Estorno de Créditos | Totais de Estorno de Créditos | Totais de Estorno de Créditos | Totais de Estorno de Créditos | Totais de Estorno de Créditos |
| IBS | Numérico | N | S | 0,00 | Informar o valor total do estorno de crédito do IBS. | MFS-951840 |
| CBS | Numérico | N | S | 0,00 | Informar o valor total do estorno de crédito da CBS. | MFS-951840 |
