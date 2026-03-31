# MTZ_Documento_Utilities_Item_Reforma_Tributária_SAFX3043

> Fonte: MTZ_Documento_Utilities_Item_Reforma_Tributária_SAFX3043.docx






THOMSON REUTERS

TAXONE
Básicos / Data Warehouse /
Documento Fiscal / Documento Fiscal Utilities
ITEM – REFORMA TRIBUTÁRIA – SAFX3043



DOCUMENTO DE REQUISITO

Sumário

1.	Objetivo	3
2.	Tela	3
3.	Regras dos Campos	4






















## Objetivo


Criar tela de documentos fiscais de Utilities (Item), referente à SAFX3043, que contempla os campos da reforma tributária.
## Tela


## Regras dos Campos


Localização da tela: Módulo: Básicos>> Data Warehouse
Menu: Manutenção >> Documento Fiscal >> Documento Fiscal Utilities

Título da tela: Novo Documento Fiscal Utilities

Aba ITEM >>  Radio buton, selecionada a opção Reforma






| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-859982 | Alessandra Cristina Navatta | Criação da tela Item do Documento de Utilities – Reforma Tributária (SAFX3043) |
| MFS-951840 | Alessandra Cristina Navatta | Em atendimento ao INFOLEGIS 2191/25 - M - NFCOM - NT RTC 2025.001_v.1.10, temos:  Inclusão do campo de Indicador de Doação, no agrupamento ‘IBS/CBS’ Inclusão do campo de valor do tributo do IBS (IBS UF+ IBS MUN), no agrupamento ‘IBS’ Inclusão dos campos de Tributação Regular (alíquota efetiva e tributo do IBS MUN), no agrupamento ‘Tributação Regular’ Exclusão dos campos de Crédito Presumido, agrupamento ‘Crédito Presumido’ Exclusão do agrupamento ‘Monofasia e Alíquotas AD REM ’ Criação do Agrupamento ‘Compras Governamentais’ Inclusão dos campos de valor a ser estornado (IBS e CBS), agrupamento ‘Créditos Estornados’ Ajuste na regra da recuperação do campo ‘Código Classificação Tributária’ dos agrupamentos IBS/CBS e Tributação Regular |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Aba ITEM | Aba ITEM | Aba ITEM | Aba ITEM | Aba ITEM | Aba ITEM | Aba ITEM |
| Reforma | Radio-Buton |  |  |  | Quando marcada a opção Reforma, exibir os campos mencionados a seguir | MFS-859982 |
| IBS/CBS | IBS/CBS | IBS/CBS | IBS/CBS | IBS/CBS | IBS/CBS | IBS/CBS |
| Código Situação Tributária IBS/CBS | Pasta | N | S |  | Recuperar a informação da TACES115 - Tabela de Código de Situação Tributária do IBS e da CBS - Reforma Tributária | MFS-859982 |
| Código Classificação Tributária IBS/CBS | Pasta | N | S |  | Recuperar a informação da TACES116 - Tabela de Classificação Tributária do IBS e da CST - Reforma Tributária. TACES117 - Tabela de Código de Situação Tributária x Classificação Tributária (do IBS e da CBS) - Reforma Tributária. Apresentar apenas os registros vinculados ao código de situação tributária indicado no campo anterior. | MFS-859982 MFS-951840 |
| Base Cálculo IBS/CBS | Numérico | N | S | 0,00 | Informar o valor da Base de Cálculo IBS/CBS | MFS-859982 |
| Indicador de Doação | Combo | N | S |  | Informar se a operação é normal ou de doação.  Lista de valores válidos: Branco Operação normal, sem doação.  Operação com doação | MFS-951840 |
| IBS | IBS | IBS | IBS | IBS | IBS | IBS |
| Alíquota IBS UF | Numérico | N | S | 0,00 | Informar o valor da alíquota do IBS UF | MFS-859982 |
| Percentual Diferimento IBS UF | Numérico | N | S | 0,00 | Informar o valor percentual do Diferimento IBS UF | MFS-859982 |
| Diferimento IBS UF | Numérico | N | S | 0,00 | Informar o valor do Diferimento IBS UF | MFS-859982 |
| Devolução IBS UF | Numérico | N | S | 0,00 | Informar o valor da Devolução IBS UF | MFS-859982 |
| Percentual Redução Alíquota IBS UF | Numérico | N | S | 0,00 | Informar o valor do Percentual Redução Alíquota IBS UF | MFS-859982 |
| Alíquota Efetiva IBS UF | Numérico | N | S | 0,00 | Informar o valor da Alíquota Efetiva IBS UF Aplicada Base Cálculo | MFS-859982 |
| IBS UF | Numérico | N | S | 0,00 | Informar o valor do IBS UF | MFS-859982 |
| Alíquota IBS Municipal | Numérico | N | S | 0,00 | Informar o valor do IBS Municipal | MFS-859982 |
| Percentual Diferimento IBS Municipal | Numérico | N | S | 0,00 | Informar o valor da percentual Diferimento IBS Municipal | MFS-859982 |
| Diferimento IBS Municipal | Numérico | N | S | 0,00 | Informar o valor do Diferimento IBS Municipal | MFS-859982 |
| Devolução IBS Municipal | Numérico | N | S | 0,00 | Informar o valor da DEVOLUÇÃO IBS Municipal | MFS-859982 |
| Percentual Redução Alíquota IBS Municipal | Numérico | N | S | 0,00 | Informar o valor do Percentual Redução Alíquota IBS Municipal | MFS-859982 |
| Alíquota Efetiva IBS Municipal | Numérico | N | S | 0,00 | Informar o valor da Alíquota Efetiva IBS Municipal Aplicada Base Cálculo | MFS-859982 |
| IBS Municipal | Numérico | N | S | 0,00 | Informar o valor IBS Municipal | MFS-859982 |
| IBS (IBS UF + IBS Municipal) | Numérico | N | S | 0,00 | Informar o valor IBS Total (IBS UF + IBS Municipal) | MFS-951840 |
| CBS | CBS | CBS | CBS | CBS | CBS | CBS |
| Alíquota CBS | Numérico | N | S | 0,00 | Informar o valor da Alíquota da CBS | MFS-859982 |
| Percentual Diferimento CBS | Numérico | N | S | 0,00 | Informar o valor do Percentual Diferimento CBS | MFS-859982 |
| Diferimento CBS | Numérico | N | S | 0,00 | Informar o valor do Diferimento CBS | MFS-859982 |
| Devolução CBS | Numérico | N | S | 0,00 | Informar o valor da Devolução CBS | MFS-859982 |
| Percentual Redução Alíquota CBS | Numérico | N | S | 0,00 | Informar o valor do Percentual Redução Alíquota CBS | MFS-859982 |
| Alíquota Efetiva CBS | Numérico | N | S | 0,00 | Informar o valor da Alíquota Efetiva CBS Aplicada Base Cálculo | MFS-859982 |
| CBS | Numérico | N | S | 0,00 | Informar o valor da CBS | MFS-859982 |
| Tributação Regular | Tributação Regular | Tributação Regular | Tributação Regular | Tributação Regular | Tributação Regular | Tributação Regular |
| Código Situação Tributária | Pasta | S | S |  | Recuperar a informação da TACES115 - Tabela de Código de Situação Tributária do IBS e da CBS - Reforma Tributária | MFS-859982 |
| Código Classificação Tributária | Pasta | S | S |  | Recuperar a informação da TACES116 - Tabela de Classificação Tributária do IBS e da CST - Reforma Tributária. TACES117 - Tabela de Código de Situação Tributária x Classificação Tributária (do IBS e da CBS) - Reforma Tributária. Apresentar apenas os registros vinculados ao código de situação tributária indicado no campo anterior. | MFS-859982 MFS-951840 |
| Alíquota Efetiva IBS UF | Numérico | N | S | 0,00 | Informar o valor da Alíquota do IBS UF (da tributação regular) | MFS-859982 |
| IBS UF | Numérico | N | S | 0,00 | Informar o valor do IBS UF(da tributação regular) | MFS-859982 |
| Alíquota Efetiva IBS Municipal | Numérico | N | S | 0,00 | Informar o valor da Alíquota do IBS Municipal (da tributação regular) | MFS-951840 |
| IBS Municipal | Numérico | N | S | 0,00 | Informar o valor do IBS Municipal (da tributação regular) | MFS-951840 |
| Alíquota Efetiva CBS | Numérico | N | S | 0,00 | Informar o valor da Alíquota da CBS (da tributação regular) | MFS-859982 |
| CBS | Numérico | N | S | 0,00 | Informar o valor da CBS (da tributação regular) | MFS-859982 |
| Crédito Presumido | Crédito Presumido | Crédito Presumido | Crédito Presumido | Crédito Presumido | Crédito Presumido | Crédito Presumido |
| Código Crédito Presumido IBS | Pasta | N | S |  | Informar o código do crédito Presumido do IBS da TACES118 - Tabela de Codigo de Credito Presumido do IBS e da CBS- Reforma Tributaria | MFS-859982 |
| Percentual IBS | Numérico | N | S | 0,00 | Informar o valor do Percentual do Crédito Presumido IBS | MFS-859982 |
| IBS | Numérico | N | S | 0,00 | Informar o valor do Crédito Presumido IBS | MFS-859982 |
| Código Crédito Presumido CBS | Pasta | N | S |  | Informar o código do crédito Presumido do CBS da TACES118 - Tabela de Codigo de Credito Presumido do IBS e da CBS- Reforma Tributaria | MFS-859982 |
| Percentual CBS | Numérico | N | S | 0,00 | Informar o valor do Percentual Crédito Presumido CBS | MFS-859982 |
| CBS | Numérico | N | S | 0,00 | Informar o valor do Crédito Presumido CBS | MFS-859982 |
| Monofasia e Alíquotas AD REM | Monofasia e Alíquotas AD REM | Monofasia e Alíquotas AD REM | Monofasia e Alíquotas AD REM | Monofasia e Alíquotas AD REM | Monofasia e Alíquotas AD REM | Monofasia e Alíquotas AD REM |
| Alíq. Ad Rem IBS - Compras Govern. | Numérico | N | S | 0,00 | Informar o valor da Alíquota IBS Utilizada Compras Governamentais | MFS-859982 |
| Alíq. Ad Rem IBS Retido - Compras Govern. | Numérico | N | S | 0,00 | Informar o valor da Alíquota IBS Retido Utilizada Compras Governamentais | MFS-859982 |
| Alíq. Ad Rem CBS - Compras Govern. | Numérico | N | S | 0,00 | Informar o valor da Alíquota CBS Utilizada Compras Governamentais | MFS-859982 |
| IBS | Numérico | N | S | 0,00 | Informar o valor do IBS (Monofasia) | MFS-859982 |
| IBS Retido | Numérico | N | S | 0,00 | Informar o valor do IBS Retido  (Monofasia) | MFS-859982 |
| CBS | Numérico | N | S | 0,00 | Informar o valor da CBS  (Monofasia) | MFS-859982 |
| Compras Governamentais | Compras Governamentais | Compras Governamentais | Compras Governamentais | Compras Governamentais | Compras Governamentais | Compras Governamentais |
| Alíquota IBS UF | Numérico | N | S | 0,00 | Informar o valor da alíquota do IBS UF utilizado em compras governamentais. | MFS-951840 |
| IBS UF | Numérico | N | S | 0,00 | Informar o valor do IBS UF utilizado em compras governamentais | MFS-951840 |
| Alíquota IBS Municipal | Numérico | N | S | 0,00 | Informar o valor da alíquota do IBS Municipal utilizado em compras governamentais | MFS-951840 |
| IBS Municipal | Numérico | N | S | 0,00 | Informar o valor do IBS Municipal utilizado em compras governamentais | MFS-951840 |
| Alíquota CBS | Numérico | N | S | 0,00 | Informar o valor da alíquota da CBS utilizado em compras governamentais | MFS-951840 |
| CBS | Numérico | N | S | 0,00 | Informar o valor da CBS utilizado em compras governamentais |  |
| Créditos Estornados | Créditos Estornados | Créditos Estornados | Créditos Estornados | Créditos Estornados | Créditos Estornados | Créditos Estornados |
| IBS | Numérico | N | S | 0,00 | Informar o valor do estorno de crédito do IBS. | MFS-951840 |
| CBS | Numérico | N | S | 0,00 | Informar o valor do estorno de crédito da CBS. | MFS-951840 |
