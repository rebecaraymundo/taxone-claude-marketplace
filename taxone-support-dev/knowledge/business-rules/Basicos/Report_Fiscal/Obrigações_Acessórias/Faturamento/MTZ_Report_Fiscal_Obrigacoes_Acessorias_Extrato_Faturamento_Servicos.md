# MTZ_Report_Fiscal_Obrigacoes_Acessorias_Extrato_Faturamento_Servicos

- **Fonte:** MTZ_Report_Fiscal_Obrigacoes_Acessorias_Extrato_Faturamento_Servicos.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Report Fiscal – Obrigações Acessórias – Extrato do Faturamento p/ DataMart \- Serviços

*Localização:* 

Report Fiscal\\ Obrigações Acessórias\\ Extrato do Faturamento p/ DataMart\\ Serviços\\ Cliente

Report Fiscal\\ Obrigações Acessórias\\ Extrato do Faturamento p/ DataMart\\ Serviços\\ Conta

Report Fiscal\\ Obrigações Acessórias\\ Extrato do Faturamento p/ DataMart\\ Serviços\\ Data

Report Fiscal\\ Obrigações Acessórias\\ Extrato do Faturamento p/ DataMart\\ Serviços\\ UF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

CH8064\_2014

Julyana Perrucini

Definição das colunas do relatório\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral:__

- Manter tratamento atual do relatório, ou seja, recuperação por SAFX07/09, classificação igual a 2 e 3, situação do documento fiscal diferente de cancelada e demais parametrizações comuns para NF\.
- O título do relatório será “Extrato Faturamento de Serviços por <<Classificação>>”, em que Classificação será o menu selecionado pelo usuário, sendo Cliente, Conta, Data ou UF\.
- O cabeçalho e a coluna serão iguais para Tipo de Seleção Analítico ou Sintético:
	- Descrição Classificação
	- Valor Total
	- ISS
	- IR
	- COFINS
	- PIS
	- Despesas Acessórias

CH8064\_2014

RN01

Campo __Filial \(Cabeçalho\)__:

Preencher com o estabelecimento selecionado na tela de geração do relatório\.

Obs\.: Como padrão dos relatórios MSAF DW, será demonstrada a empresa selecionada na tela inicial\.

CH8064\_2014

RN02

Campo __Período \(Cabeçalho\)__:

Preencher com a data apontada na tela de geração do relatório\.

CH8064\_2014

RN03

Campo __Data \(Cabeçalho\)__:

Preencher com a data e a hora de geração do relatório\.

CH8064\_2014

RN04

Campo __Pág\. \(Cabeçalho\)__:

Preencher sequencial de página\.

CH8064\_2014

RN05

Campo __Insc\. Estadual \(Cabeçalho\)__:

Preencher com a Inscrição Estadual do estabelecimento selecionado na tela de geração do relatório\. \(A IE é cadastrada no caminho: Básicos\\ Parâmetros\\ Preliminares\\ Inscrições Estaduais\)\.

CH8064\_2014

RN06

Campo __CNPJ \(Cabeçalho\)__:

Preencher com o CNPJ do estabelecimento selecionado na tela de geração do relatório\. \(O CNPJ é cadastrado no caminho: Básicos\\ Parâmetros\\ Preliminares\\ Empresa/Estabelecimento\)\.

CH8064\_2014

RN07

Campo __Descrição Classificação__:

Será demonstrado de acordo com a seleção do menu, ou seja, por Cliente, Conta, Data ou UF respeitando o período preenchido na tela de geração do relatório para seleção dos documentos fiscais\.

__Tratamento:__

- Quando selecionado menu Cliente – Agrupar, ordenar e concatenar código e descrição do cliente da SAFX04 cadastrada no documento fiscal\.
- Quando selecionado menu Conta – Agrupar, ordenar e concatenar código e descrição da conta da FAX2002 cadastrada no documento fiscal\. Observação: para geração desse relatório, é necessário que o documento fiscal esteja com a conta contábil cadastrada na capa do documento, além disso, é necessário existir um CFOP que incida PIS e COFINS, ou seja, precisam constar valores de PIS e COFINS e o CFOP no item do documento fiscal e este CFOP precisa ser parametrizado em Report Fiscal\\ Obrigações Acessórias\\ Faturamento\\ PIS/COFINS\\ Parâmetros\\ Parâmetros do PIS/COFINS\\ Por CFOP ou Por CFOP/Natureza da Operação\.
- Quando selecionado menu Data – Agrupar e ordenar pela Data Fiscal do documento fiscal\.
- Quando selecionado menu UF – Agrupar, ordenar e concatenar código e descrição da UF da SAFX04 cadastrada no documento fiscal\.

CH8064\_2014

RN08

Campo __Valor Total__:

Preencher de acordo com o agrupamento do menu selecionado com a soma do Valor Total do item do serviço \(campo 15\-VLR\_TOT da SAFX09\)\.

CH8064\_2014

RN09

Campo __ISS__:

Preencher de acordo com o agrupamento do menu selecionado com a soma do Vlr ISS do item do serviço \(campo 33\-VLR\_ISS da SAFX09\)\.

CH8064\_2014

RN10

Campo __IR__:

Preencher de acordo com o agrupamento do menu selecionado com a soma do Valor IR do item do serviço \(campo 31\-VLR\_IR da SAFX09\)\.

CH8064\_2014

RN11

Campo __COFINS__:

Preencher de acordo com o agrupamento do menu selecionado com a soma do Vlr COFINS do item do serviço \(campo 51\-VLR\_COFINS da SAFX09\)\.

CH8064\_2014

RN12

Campo __PIS__:

Preencher de acordo com o agrupamento do menu selecionado com a soma do Vlr PIS do item do serviço \(campo 48\-VLR\_PIS da SAFX09\)\.

CH8064\_2014

RN13

Campo __Despesas Acessórias__:

Preencher com zeros\.

CH8064\_2014

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

