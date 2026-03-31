# MTZ-Importacao_SAFX502

- **Fonte:** MTZ-Importacao_SAFX502.docx
- **Modificado:** 2022-06-17
- **Tamanho:** 46 KB

---

    

# Módulo Job Servidor – Importação – Arquivo Relacionado de Transportadora \- Veículo Composto \(SAFX502\)

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX502, conforme o Manual de Layout,  o que facilita a consulta\) *

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

MFS85875

Alteração p/ Campo Não Obrigatório 

Alteração do Campo 14 – Placa do Veículo para Campo não obrigatório\.

18/05/2022

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN01__

__Campo 01 \- Código da empresa__

 

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código da empresa na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

__Campo Obrigatório__

__RN02__

__Campo 02 \- Código do estabelecimento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código do estabelecimento na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__Chave Primária__

__Campo Obrigatório__

__RN03__

__Campo 03 \- Data da Escrita Fiscal__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Data da Escrita Fiscal na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __03

__Nome do Campo: __DATA\_FISCAL

__Descrição: __Data da Escrita Fiscal

__Tipo:__ N

__Tamanho: __008

__Conteúdo do Campo: __Informar a Data da Escrita Fiscal\. Para as notas fiscais de:

- 
	- 
		- 
			- Entradas: Data do Recolhimento do Documento \(na SAFX07\)\.
			- Saídas: Data de Emissão do Documento \(na SAFX07\)\.

__Chave Primária__

__Campo Obrigatório__

__RN04__

__Campo 04 \- Motivo da Entrada/Saída__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Motivo da Entrada/Saída na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __04

__Nome do Campo: __MOVTO\_E\_S

__Descrição:__ Motivo da Entrada/Saída

__Tipo:__ A

__Tamanho: __001

__Comentário: __Campo destinado ao Motivo da Entrada/Saída\.

__Chave Primária__

__Campo Obrigatório__

__RN05__

__Campo 05 \- Normal/Devolução__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo de  Normal/Devolução na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __05

__Nome do Campo: __NORM\_DEV

__Descrição:__ Normal/Devolução

__Tipo:__ A

__Tamanho: __001

__Comentário: __Campo destinado a informação de Normal/Devolução\.

__Chave Primária__

__Campo Obrigatório__

__RN06__

__Campo 06 \- Tipo de documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Tipo de documento na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __06

__Nome do Campo: __COD\_DOCTO

__Descrição: __Código do documento

__Tipo:__ A

__Tamanho: __005

__Conteúdo do Campo: __Código de Tipo de Documento deverá estar devidamente cadastrado da tabela SAFX2005, caso contrário deverá gerar com Log de Erro\. \(código de erro 90125\)

__Chave Primária__

__Campo Obrigatório__

__RN07__

__Campo 07 \- Indicador da Pessoa física/Jurídica__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Indicador da Pessoa física/Jurídica na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __07

__Nome do Campo: __IND\_FIS\_JUR

__Descrição:__ Indicador de Pessoa Física/Jurídica

__Tipo:__ A

__Tamanho: __001

__Comentário: __Campo que deverá ser preenchido com o Indicador de Pessoa Física/Jurídica

 relacionada na Tabela de Pessoa Física/Jurídica \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

__Chave Primária__

__Campo Obrigatório__

__RN08__

__Campo 08 – Código/Destinatário/Emitente/ Remetente__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código/Destinatário/Emitente/ Remetente na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __08

__Nome do Campo: __COD\_FIS\_JUR

__Descrição:__ Código/Destinatário/Emitente/ Remetente

__Tipo:__ A

__Tamanho: __014

__Comentário: __Deve estar registrado na Tabela de Pessoa Física/Jurídica \(SAFX04\)\. 

__ Chave Primária__

__ Campo Obrigatório__

__RN09__

__Campo 09 – Número do documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Número do Documento Fiscal na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __9

__Nome do Campo:__ NUM\_DOCFIS

__Descrição: __Número do Documento Fiscal

__Tipo:__ A

__Tamanho: __012

__Comentário: __Campo destinado a informação de Número do Documento Fiscal\.

__Chave Primária__

__Campo Obrigatório__

__RN10__

__Campo 10 – Série do Documento Fiscal__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Série do Documento Fiscal na tabela SAFX502\.

__Tabela: __SAFX502

__Item: 1__0

__Nome do Campo:__ SERIE\_DOCFIS

__Descrição: __Série do Documento Fiscal

__Tipo:__ A	

__Tamanho: __003

__Comentário: __Campo destinado a informação de Série do Documento Fiscal\.

__Chave Primária__

__Não Obrigatório__

__RN11__

__Campo 11 – Subsérie do Documento Fiscal__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Subsérie do Documento Fiscal na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __11

__Nome do Campo:__ SUB\_SERIE\_DOCFIS

__Descrição:__ Subsérie do Documento Fiscal

__Tipo:__ A

__Tamanho: __002

__Comentário: __Campo destinado a informação de Subsérie do Documento Fiscal\.

__Chave Primária__

__Não Obrigatório__

__RN12__

__Campo 12 – Indicador de pessoa Física/Jurídica para Transportadora__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Indicador de pessoa Física/Jurídica para Transportadora na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __12

__Nome do Campo: __IND\_FIS\_TRANSP

__Descrição:__ Indicador de pessoa Física/Jurídica para Transportadora

__Tipo:__ A

__Tamanho: __001

__Comentário: __Campo que deverá ser preenchido com o Indicador de pessoa Física/Jurídica para Transportadora relacionada na Tabela de Pessoa Física/Jurídica \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

Este campo pode ser preenchido com o Indicador da Pessoa Física/Jurídica emitente do documento fiscal, para os modelos 07, 08, 09, 10, 26, 13, 14, 16\. Isso possibilitará a inclusão de informações de transporte , solicitadas pelo Ato COTEPE 70/05, relativas a estes modelos\.

__Chave Primária__

__Campo Obrigatório__

__RN13__

__Campo 13 – Código da Transportadora__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código da Transportadora na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __13

__Nome do Campo: __COD\_FIS\_TRANSP

__Descrição:__ Código da Transportadora

__Tipo:__ A

__Tamanho: __014

__Comentário: __Deve estar registrado na Tabela de Pessoa Física/Jurídica \(SAFX04\)\. 

Este campo pode ser preenchido com o indicador do Código da Transportadora emitente do documento fiscal, para os modelos 07, 08, 09, 10, 26, 13, 14, 16\. Isso possibilitará a inclusão de informações de transporte, solicitadas pelo Ato COTEPE 70/05, relativas a estes modelos\.

__Chave Primária__

__Campo Obrigatório__

__RN14__

__Campo 14 – Placa do Veículo__

__\[MFS83787\] Alteração para campo Não Obrigatório__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Placa do Veículo na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __14

__Nome do Campo: __PLACA\_VEICULO

__Descrição: __Placa do Veículo

__Tipo:__ A

__Tamanho: __017

__Conteúdo do Campo: __Deve estar registrado a Placa do Veículo\.

__Chave Primária__

__Não Obrigatório__

__Campo Obrigatório__

MFS85875

__RN15__

__Campo 15 – Unidade da Federação da Placa__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Unidade da Federação da Placa na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __15

__Nome do Campo:__ UF\_VEIC

__Descrição: __Unidade da Federação da Placa

__Tipo:__ A

__Tamanho: __002

__Comentário: __Deve estar registrado a Unidade da Federação da Placa\.

__Não Obrigatório__

__RN16__

__Campo 16 – Numeração do Volume__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Numeração do Volume na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __16

__Nome do Campo:__ NUM\_VOLUME

__Descrição: __Numeração do Volume

__Tipo:__ A

__Tamanho: __050

__Comentário: __Deve estar registrado a Numeração do Volume\.

__Não Obrigatório__

__RN17__

__Campo 17 – Peso Bruto __

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Peso Bruto na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __17

__Nome do Campo:__ PESO\_BRUTO

__Descrição: __Peso Bruto

__Tipo:__ N

__Tamanho: __011V003

__Comentário: __Deve estar registrado o Peso Bruto\.

__Não Obrigatório__

__RN18__

__Campo 18 – Peso Líquido__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Peso Líquido na tabela SAFX502\.

__Tabela: __SAFX502

__Item: __18

__Nome do Campo:__ PESO\_LIQUIDO

__Descrição: __Peso Líquido

__Tipo:__ N

__Tamanho: __011V003

__Comentário: __Deve estar registrado o Peso Líquido\.

__Não Obrigatório__

