# MTZ_EFD_PIS-COFINS_Relatório_de_Ajustes_no_ Crédito_do_Rateio_Proporcional_dos_Registros_M105_M505 - Receita Cumulativa

> Fonte: MTZ_EFD_PIS-COFINS_Relatório_de_Ajustes_no_ Crédito_do_Rateio_Proporcional_dos_Registros_M105_M505 - Receita Cumulativa.docx






THOMSON REUTERS

PRODUTO TAXONE
Módulo EFD-Escrituração Fiscal Digital das Contribuições

Localização: Produto: TAXONE: Menu SPED, Módulo: EFD-Escrituração Fiscal Digital das Contribuições, item de menu Relatórios >> Relatório de Ajustes no Crédito do Rateio Proporcional dos Registros M105/M505 - Receita Cumulativa



DOCUMENTO DE REQUISITO

Sumário


1.	TELA	3
2.	REGRAS DOS CAMPOS	3
3.	REGRAS DE GERAÇÃO DO RELATÓRIO	5
3.1.	Layout do Relatório	13

## TELA




## REGRAS DOS CAMPOS


Produto: TAXONE
Localização da tela: Menu: SPED, Módulo: EFD-Escrituração Fiscal Digital das Contribuições, item de menu Relatórios >
Título da tela: Relatório de Ajustes no Crédito do Rateio Proporcional dos Registros M105/M505 - Receita Cumulativa
> Geração


## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:

Para geração deste relatório, serão consideradas as informações da seguinte origem:

Cadastro do Estabelecimento, SAFX04, SAFX07, SAFX08 e SAFX09

Regra de seleção:

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = Data Inicial e Data Final informado em tela
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada estabelecimento (Centralizador) selecionado em tela será gerado um relatório.
Serão recuperadas as informações das notas fiscais de entradas sendo mercadorias ou serviços das tabelas SAFX07/08/09, considerando a parametrização da tela do Módulo: EFD_Escrituração Fiscal Digital das Contribuições Menu: Parâmetros > Ajustes no Crédito do Rateio Proporcional dos Registros M105/M505 – Receita Cumulativa, listando somente as notas que contém essas parametrizações.

Ordenação:

Empresa
Estabelecimento
Data Fiscal
Data Lancto PIS/COFINS
Cod.PF/PJ
CPF/CGC
Movto
Num. Docto
Serie
Tipo Docto
CFOP
Nat. Operação
Cód. Produto/Serviço
Valor Contábil
Valor Produto/Servico
CST PIS
Base de Cálculo PIS
Alíquota PIS
Valor do PIS
CST COFINS
Base de Cálculo COFINS
Alíquota COFINS
Valor do COFINS
Nat. Base de Crédito
Cod. Tipo Crédito PIS/COFINS
Classificação da Receita


Segue regras do preenchimento dos dados no relatório:



### Layout do Relatório




| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-772608 | Rosemeire Santos | Criação do Relatório de Ajustes no Crédito do Rateio Proporcional dos Registros M105/M505 - Receita Cumulativa | 26/03/2025 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Data Inicial | Data | S | S | Formato: DD/MM/AAAA. | Deverá ser informada a Data Inicial para recuperarmos as notas de entradas. Esse campo deverá ser obrigatório de preenchimento | MFS-772608 |
| Data Final | Data | S | S | Formato: DD/MM/AAAA. | Deverá ser informada a Data Final para recuperarmos as notas de entradas. Esse campo deverá ser obrigatório de preenchimento | MFS-772608 |
| Estabelecimentos | CheckBox | S | S | XXX / XXXXX-XXXXXXXXXXXXXXXXX  (Centralizador + cód. + Descrição)  XXX / XXXXX-XXXXXXXXXXXXXXXXX  (Descentralizado + cód. + Descrição)    Default: não selecionado | Na lista será demonstrado os estabelecimentos da empresa logada e que o usuário tenha acesso.  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS-772608 |
| Executar |  |  |  |  | Campos de preenchimento obrigatório não preenchido: Se um campo obrigatório não for preenchido, exibir a mensagem: “<<Nome do campo que é exibido em tela>> deve ser preenchido!”  Outras Validações: O campo data final deve ser maior que a data inicial, caso contrário, exibir a mensagem: Data Final deve ser maior que a Data Inicial! | MFS-772608 |


| Campo/Coluna | Tipo | Decrição | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Empresa | Alfanumérico | Código - Empresa | Campo 01 - COD_EMPRESA da SAFX07 | MFS-772608 |
| Estabelecimento | Alfanumérico | Código - Estabelecimento | Campo 02 - COD_ESTAB da SAFX07 | MFS-772608 |
| Data Fiscal | DD/MM/AAAA | Data da Escrita Fiscal | Campo 03 - DATA_FISCAL da SAFX08, para mercadoria e ou Campo 03 - DATA_FISCAL da SAFX09, quando for serviços. | MFS-772608 |
| Data Lancto PIS/COFINS | DD/MM/AAAA | Data de Lançamento na EFD-PIS/PASEP-COFINS | Campo 196 - DAT_LANC_PIS_COFINS da SAFX08, para mercadoria e ou Campo 81 - DAT_LANC_PIS_COFINS da SAFX09, quando for serviços.  Se nenhum desses campos acima tiver preenchido verificar na SAFX07 – Campo 274 - DAT_LANC_PIS_COFINS | MFS-772608 |
| Cód. PF/PJ | Alfanumérico | Código Pessoa Física/Jurídica | Campo 02 - COD_FIS_JUR da SAFX04 | MFS-772608 |
| CPF/CGC | Alfanumérico | CPF-CGC | Campo 06 - CPF_CGC da SAFX04 | MFS-772608 |
| Movto | Alfanumérico | Movimento Entrada/Saída | Campo 03 - MOVTO_E_S da SAFX07 – Considerar somente documento de entradas | MFS-772608 |
| Num. Docto | Alfanumérico | Número do Documento Fiscal | Campo 09 - NUM_DOCFIS da SAFX08, para mercadoria e ou Campo 09 - NUM_DOCFIS da SAFX09, quando for serviços. | MFS-772608 |
| Serie | Alfanumérico | Série do Documento Fiscal | Campo 10 - SERIE_DOCFIS da SAFX08, para mercadoria e ou Campo 10 - SERIE_DOCFIS da SAFX09, quando for serviços. | MFS-772608 |
| Tipo Docto | Alfanumérico | Tipo do Documento | Campo 06 - COD_DOCTO da SAFX08, para mercadoria e ou Campo 10 - COD_DOCTO da SAFX09, quando for serviços. | MFS-772608 |
| CFOP | Alfanumérico | Código Fiscal | Campo 22 - COD_CFO da SAFX08, para mercadoria e ou Campo 17 - COD_CFO da SAFX09, quando for serviços. Ou Campo 01 - COD_CFO da SAFX2012 | MFS-772608 |
| Nat. Operação | Alfanumérico | Código da Natureza de Operação | Campo 23 - COD_NATUREZA_OP da SAFX08, para mercadoria e ou Campo 18 - COD_NATUREZA_OP da SAFX09, quando for serviços. Ou Campo 02 - COD_NATUREZA_OP da SAFX2081 | MFS-772608 |
| Cód. Produto/Serviço | Alfanumérico | Produto/Serviço | Quando for mercadoria buscar Campo 14 - COD_PRODUTO – SAFX08 ou Campo 02 - COD_PRODUTO da SAFX2013 e quando for serviços buscar Campo 12 - COD_SERVICO da SAFX09. Ou Campo 01 - COD_SERVICO da SAFX2018 | MFS-772608 |
| Valor Contábil | Numérico | Valor Contábil | Campo 64 - VLR_CONTAB_ITEM da SAFX08, para mercadoria e ou Campo 15 - VLR_TOT da SAFX09, quando for serviços. | MFS-772608 |
| Valor Produto/Serviço | Numérico | Valor do Produto/Serviço | Campo 28 - VLR_ITEM da SAFX08, para mercadoria e ou Campo 14 - VLR_SERVICO da SAFX09, quando for serviços. | MFS-772608 |
| CST PIS | Numérico | Código Situação Tributária PIS | Campo 175 - COD_SITUACAO_PIS da SAFX08, para mercadoria e ou Campo 68 - COD_SITUACAO_PIS da SAFX09, quando for serviços. | MFS-772608 |
| Base de Cálculo PIS | Numérico | Base de Cálculo PIS | Campo 86 - VLR_BASE_PIS da SAFX08, para mercadoria e ou Campo 46 - VLR_BASE_PIS da SAFX09, quando for serviços. | MFS-772608 |
| Alíquota PIS | Numérico | Alíquota do PIS | Campo 129 - VLR_ALIQ_PIS da SAFX08, para mercadoria e ou Campo 47 - VLR_ALIQ_PIS da SAFX09, quando for serviços. | MFS-772608 |
| Valor do PIS | Numérico | Valor Tributo PIS | Campo 87 - VLR_PIS da SAFX08, para mercadoria e ou Campo 48 - VLR_PIS da SAFX09, quando for serviços. | MFS-772608 |
| CST COFINS | Numérico | Código de Situação Tributária COFINS | Campo 178 - COD_SITUACAO_COFINS da SAFX08, para mercadoria e ou Campo 69 - COD_SITUACAO_COFINS da SAFX09, quando for serviços. | MFS-772608 |
| Base de Cálculo COFINS | Numérico | Base de Cálculo COFINS | Campo 88 - VLR_BASE_COFINS da SAFX08, para mercadoria e ou Campo 49 - VLR_BASE_COFINS da SAFX09, quando for serviços. | MFS-772608 |
| Alíquota COFINS | Numérico | Alíquota do COFINS | Campo 130 - VLR_ALIQ_COFINS da SAFX08, para mercadoria e ou Campo 50 - VLR_ALIQ_COFINS da SAFX09, quando for serviços. | MFS-772608 |
| Valor do COFINS | Numérico | Valor Tributo COFINS | Campo 89 - VLR_COFINS da SAFX08, para mercadoria e ou Campo 51 - VLR_COFINS da SAFX09, quando for serviços. | MFS-772608 |
| Nat. Base de Crédito | Numérico | Natureza da Base do Crédito | Preenchimento do campo “Natureza de Base de Crédito”, considerar os dados do parâmetro “Identificador da Nat. da Base de Crédito “e ou do “documento fiscal”, conforme o flag do menu dos Dados Iniciais (Registro da Natureza da Base do Crédito).  Regra: Se IND_NAT_BASE_CRED, da capa da nota fiscal estiver preenchido E se IND_NAT_BASE_CRED_POR_DOC de Dados Iniciais for igual a "S", então o sistema retorna o valor de IND_NAT_BASE_CRED, do contrário, calcula o valor conforme regra pré-existente, tanto para Notas Fiscais e Produto quanto para Notas Fiscais de Serviço do relatório Memoria de Cálculo – Analítico. | MFS-772608 |
| Cod. Tipo Crédito PIS/COFINS | Numérico | Código do Tipo do Crédito | Para fazer a busca pelo “Tipo de crédito” na tabela EPC_PARAM_TP_CRED, utilizar os filtros de CST.  Obs: O relatório Memoria de Cálculo – Analítico, tem essa regra | MFS-772608 |
| Classificação da Receita | Alfanumérico | Classificação da Receita | Classificar como “RBC”, quando o parâmetro Regime de Tributação – Dados Iniciais estiver como ‘3 – Escrituração de operações com incidência nos regimes não-cumulativo e cumulativo’ | MFS-772608 |
