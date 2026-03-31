# MTZ_JOB_SERVIDOR_Importacao_SAFX3042

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX3042.docx
- **Modificado:** 2026-01-08
- **Tamanho:** 96 KB

---

THOMSON REUTERS

Reforma Tributária

Nota Fiscal Fatura de Serviço de Comunicação Eletrônica, modelo 62

SAFX3042 \- Capa de Documentos Fiscais de Utilities 

Localização: Menu Básicos > Módulo Job Servidor

Processos:

- Carga >>Programação >> Execução
- Importação >> Programação >> Execução
- Importação batch >> Programação >> Execução
- Exportação de Dados >> Programação >> Execução

Sumário

[1\.	CONTROLE DE ALTERAÇÕES	3](#_Toc203401796)

[2\.	INTRODUÇÃO	4](#_Toc203401797)

[3\.	DOCUMENTOS DE REFERÊNCIA	4](#_Toc203401798)

[4\.	DEFINIÇÃO DAS REGRAS	5](#_Toc203401799)

[4\.1\.	Regras de Negócio \- SAFX3042	6](#_Toc203401800)

[4\.2\.	Regras dos campos \- SAFX3042	7](#_Toc203401801)

# <a id="_Toc462320891"></a><a id="_Toc203401796"></a>CONTROLE DE ALTERAÇÕES

__Data__

__Demanda__

__Descrição__

__Autor__

15/05/2025

[ADO\-822289](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/822289)

<RT>NT2025\_001\_RTC\_v1\.02 \-  Mapeamento NFCom Modelo 62 \- Fase 03

Erika Borges

03/06/2025

[ADO\-818668](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/818668)

Atualização NT2025\_001\_RTC\_v1\.04

Érika Borges

18/06/2025

[ADO\-843670](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/843670)

Atualização NT2025\_001\_RTC\_v1\.05a

Érika Borges

27/06/2025

[ADO\-851810](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/851810)

Criação das Novas SAFX3042 e SAFX3043

Érika Borges

16/09/2025

MFS\-851810

Correção das nomenclaturas dos campos \(18 \- Total do Crédito Presumido Condição Suspensiva \(IBS\), 20 \- Total do Crédito Presumido Condição Suspensiva \(CBS\) e 25 \- Percentual de redução de alíquota em compra governamental\)\. Inclusão de validação no campo 24\-Tipo de Ente\.

Ajuste nos campos do arquivo de reserva da SAFX3042, atualização da TFIX96, TFIX97 e do mapeamento da Reforma Tributária\.

Alessandra Navatta

23/10/2025

MFS\-951840

Em atendimento ao INFOLEGIS 2191/25 \- M \- NFCOM \- NT RTC 2025\.001\_v\.1\.10, temos:

- Exclusão dos campos de Crédito Presumido
- Inclusão dos campos de Estorno de Créditos
- Inclusão dos campos de valor do tributo de Tributação Regular do IBS UF, IBS MUN e CBS
- Inclusão dos campos de valor do tributo do IBS UF, IBS MUN e CBS, referente as comprar governamentais

Alessandra Navatta

# <a id="_Toc462320892"></a><a id="_Toc203401797"></a>INTRODUÇÃO

V1 \- O objetivo desse documento é descrever a estrutura de campos das tabelas SAFX para o repositório das informações da RT \(IBS e CBS\) para os processos da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica, modelo 62 conforme mapeamento realizado no documento de requisitos de negócio relacionado no item 3\. 

V2 – Atualização versão 1\.4 da NT \(correção dos campos no layout\)\. 

V2 \- Atualização versão 1\.5a da NT \(correção dos campos no layout\)\.

V2 \- Acrescentados os campos para atender do grupo gCompraGov referente ao processo de Compras Governamentais\.

V3 – Elaboração da SAFX3042\.

# <a id="_Toc203401798"></a>DOCUMENTOS DE REFERÊNCIA

V1 \- [T1\_RT \- NFCom Modelo 62\_Requisitos de negocios\_v1\.docx](https://trten.sharepoint.com/:w:/r/sites/MarcosTeam/Shared%20Documents/General/Projetos/Solu%C3%A7%C3%B5es/Tax%20One/Reforma%20Tributaria/NFCOM%20-%20Mod%2062/T1_RT%20-%20NFCom%20Modelo%2062_Requisitos%20de%20negocios_v1.docx?d=w53da0d8bb8a44744a8b55fb4b7ec1f25&csf=1&web=1&e=PmKGH8) seções 2\.2, 3\.1\.1 e 7\.1\.\- Criação da estrutura SAFX para os imposto CBS e IBS\. 

V1 \- [Manual\_Layout\_MastersafDW\.xls](https://trten.sharepoint.com/:x:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Manuais-de-layout/Layout%20SAFX/Manual_Layout_MastersafDW.xls?d=we422f97384284e35897a6622693cca04&csf=1&web=1&e=nfPEBB) \- Layout dos Arquivo Mastersaf DW e ONESOURCE Tax One | Patch 306\.1\.1 \(SAFX08 e SAFX43\)

V1 \- 

![](data:image/x-emf;base64,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TAAAAGQAAAAAAAAAWgAAAAUEAABdAAAAAAAAAFoAAAAGBAAABAAAACEA8AAAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACUAAAAMAAAAAAAAgCgAAAAMAAAAAgAAABgAAAAMAAAAAAAAAlIAAABwAQAAAgAAABAAAAAHAAAAAAAAAAAAAAC8AgAAAAAAAAECAiJBAHIAaQBhAGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGR2AAgAAAAAJQAAAAwAAAACAAAAJQAAAAwAAAACAAAARgAAADQAAAAoAAAARU1GKypAAAAkAAAAGAAAAAAAgD8AAACAAAAAgAAAgD8AAACAAAAAgEYAAAAcAAAAEAAAAEVNRisCQAAADAAAAAAAAAAOAAAAFAAAAAAAAAAQAAAAFAAAAA==)V2 \- [Nota Técnica RTC\_v1\.05a](file:///C://Users/6132884/Downloads/NFCom_Nota_Tecnica_2025_001_RTC_v1.05a.pdf) incluir os novos campos referente às Compras Governamentais\. 

V2 – link – De\_para dos campos da DFe x SAFX\. 

# <a id="_Toc203401799"></a>DEFINIÇÃO DAS REGRAS

No contexto da Reforma tributária, o repositório de dados fiscais do Tax One terá sua estrutura atualizada para suportar os novos impostos com base na versão da publicação na presente data\. Nesse documento abordaremos a proposta de solução para os processos fiscais da __Nota Fiscal Fatura de Serviço de Comunicação Eletrônica  NFCOM – Modelo 62 __suportados pela estrutura de arquivos:

__Operações de Saídas__

SAFX3042 – Capa de Documentos Fiscais de Utilities

SAFX3043 \- Itens de Documentos Fiscais de Utilities;

__Operações de entradas__

SAFX3007 \- Arquivo de Notas Fiscais;

SAFX3008 \- Itens Notas Fiscais Mercadorias e Produtos\.

As informações para criação dos novos arquivos SAFX foram elaboradas com base na versão NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a da NFCom\.

## <a id="_Dashboard_–_Visão_1"></a> <a id="_Toc203401800"></a>Estrutura SAFX3042

Obg\.

Nr

Nome do campo

Campo

Tam

Tipo

\(\*\)

1

Código da Empresa

COD\_EMPRESA

003

A

\(\*\)

2

Código do Estabelecimento

COD\_ESTAB

006

A

\(\*\)

3

Data de Emissão/Escr\. Fiscal

DAT\_FISCAL

008

N

\(\*\)

4

Indicador Pessoa Física/Jurídica

IND\_FIS\_JUR

001

A

\(\*\)

5

Código/Destinatário/Emitente/Remetente

COD\_FIS\_JUR

014

A

\(\*\)

6

Número do Documento Fiscal

NUM\_DOCFIS

012

A

 

7

Série

SERIE\_DOCFIS

003

A

 

8

Subsérie

SUB\_SERIE\_DOCFIS

002

A

 

9

Total da Base de cálculo do IBS/CBS

VLR\_TOT\_BC\_IBS\_CBS

015V002

N

 

10

Total do Diferimento do IBS de competência da UF

VLR\_TOT\_DIF\_IBS\_UF

015V002

N

 

11

Total de Devolução de Tributo IBS UF

VLR\_TOT\_DEV\_TRIB\_IBS\_UF

015V002

N

 

12

Total do IBS UF

VLR\_TOT\_IBS\_UF

015V002

N

 

13

Total do Diferimento do IBS do Município

VLR\_TOT\_DIF\_IBS\_MUN

015V002

N

 

14

Total de Devolução de Tributo IBS Municipal

VLR\_TOT\_DEV\_TRIB\_IBS\_MUN

015V002

N

 

15

Total do IBS Municipal

VLR\_TOT\_IBS\_MUN

015V002

N

 

16

Total do IBS \(IBS UF \+ IBS Mun\)

VLR\_TOT\_IBS

015V002

N

 

17

Total do Crédito Presumido \(IBS\)

VLR\_TOT\_CRED\_PRES\_IBS

015V002

N

 

18

Total do Crédito Presumido Condição Suspensiva \(IBS\)

VLR\_TOT\_CRED\_PRES\_C\_SUS\_IBS

015V002

N

 

19

Total do Crédito Presumido \(CBS\)

VLR\_TOT\_CRED\_PRES\_CBS

015V002

N

 

20

Total do Crédito Presumido Condição Suspensiva \(CBS\)

VLR\_TOT\_CRED\_PRES\_C\_SUS\_CBS

015V002

N

 

17

Total do Diferimento da CBS

VLR\_TOT\_DIF\_CBS

015V002

N

 

18

Total de Devolução do tributo CBS

VLR\_TOT\_DEV\_TRIB\_CBS

015V002

N

 

19

Total do CBS

VLR\_TOT\_CBS

015V002

N

20

Total do IBS da UF \- tributação regular

VLR\_TOT\_TRIB\_REG\_IBS\_UF

015V002

N

21

Total do IBS do Município \- tributação regular

VLR\_TOT\_TRIB\_REG\_IBS\_MUN

015V002

N

22

Total da CBS \- tributação regular

VLR\_TOT\_TRIB\_REG\_CBS

015V002

N

23

Total do IBS da UF utilizado em Compras governamentais

VLR\_TOT\_IBS\_UF\_COMPRA\_GOVERN

015V002

N

24

Total do IBS do Município utilizado em Compras governamentais

VLR\_TOT\_IBS\_MUN\_COMPRA\_GOVERN

015V002

N

25

Total da CBS utilizado em Compras governamentais

VLR\_TOT\_CBS\_COMPRA\_GOVERN

015V002

N

26

Total do IBS estornado

VLR\_TOT\_IBS\_ESTORNADO

015V002

N

27

Total da CBS estornado

VLR\_TOT\_CBS\_ESTORNADO

015V002

N

 

28

Tipo de Ente

TIPO\_ENTE\_GOVERN

001

N

 

29

Percentual de redução de alíquota em compra governamental

 PERC\_RED\_ALIQ\_COMPRA\_GOVERN

003V004

N

## <a id="_Toc203401801"></a>Regras dos campos \- SAFX3042

__Cód\.__

__Descrição__

__OS__

RN00

Regras Gerais

\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)

Para carregar as informações da tag __vTotDFe__, utilizar o campo 15 \- Valor dos serviços\.

MFS\-851810

RN01 a 08

A tabela SAFX3042 é filha da tabela SAFX42 e deve refletir exatamente os dados do documento fiscal \(ver item 4\.1\)\. 

Chave de identificação 🡪 Empresa \+ Estabelecimento \+ Data \+ Pessoa Fis/Jur \+ Núm/Sér/Sub Documento \+ Núm do Item\.

Estrutura da Tabela 🡪 vide Manual de Layout 

Utilizar críticas e código de erros da tabela mãe, para identificar o documento fiscal de origem, sendo eles: 

__COD\_EMPRESA__ : Verifica o preenchimento do campo\. Caso não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90001 da TFIX22\)\.

__COD\_ESTAB__: Verifica o preenchimento do campo\. Caso não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90002 da TFIX22\)\.

__DAT\_FISCAL__: Verifica o preenchimento do campo\. Caso não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90131 da TFIX22\)\.

Verifica a validade da data\. Se inválida, será gravada a mensagem de erro padrão no log da importação \(mensagem 90209 da TFIX22\)\.

__IND\_FIS\_JUR__: Verifica o preenchimento do campo e a validade dos indicadores conforme os indicadores da SAFX04\. Caso não preenchido ou inválido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90088 da TFIX22\)\.

__COD\_FIS\_JUR__: Verifica o preenchimento do campo, e se não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90089 da TFIX22\)\.

Verifica a existência da pessoa na SAFX04, com validade <= a data de emissão do documento \(campo “Data Emissão/Escr\.Fiscal”\)\. Caso não exista, será gravada a mensagem de erro padrão no log da importação \(mensagem 90124 da TFIX22\)\.

__NUM\_DOCFIS__: Verifica o preenchimento do campo, e se não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90112 da TFIX22\)\.

__SERIE\_DOCFIS__: Quando não preenchido, será gravado um caractere branco, procedimento padrão das tabelas de documentos fiscais\. 

Após a validação dos campos 01 ao 08, será verificada a existência da capa do documento informado na tabela SAFX42, a partir dos campos chave da tabela\. Se não identificado, será gravada a mensagem de erro padrão no log da importação \(mensagem 92496 da TFIX22\)\.

MFS\-851810

RN09

Campo 09 \- VLR\_TOT\_BC\_IBS\_CBS

__Regra__

Campo:  Total da Base de cálculo do IBS/CBS\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN10

Campo 10 \- VLR\_TOT\_DIF\_IBS\_UF

__Regra__

Campo:  Total do Diferimento

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN11

Campo 11\- VLR\_TOT\_DEV\_TRIB\_IBS\_UF 

__Regra__

Campo:  Total de Devolução de Tributo IBS UF\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN12

Campo 12 \- VLR\_TOT\_IBS\_UF

__Regra__

Campo:  Total do IBS UF\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN13

Campo 13\- VLR\_TOT\_DIF\_IBS\_MUN

__Regra__

Campo: Total do Diferimento\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN14

Campo 14 \- VLR\_TOT\_DEV\_TRIB\_IBS\_MUN 

__Regra__

Campo:  Total de Devolução de Tributo IBS Municipal\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN15

Campo 15 \- VLR\_TOT\_IBS\_MUN

__Regra__

Campo:  Total do IBS Municipal\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN16

Campo 16 \- VLR\_TOT\_IBS

__Regra__

Campo:  Total do IBS \(IBS UF \+ IBS Mun\)\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN17

__\[EXCLUÍDA – MFS\-951840\]__ Campo 17 \- VLR\_TOT\_CRED\_PRES\_IBS

__Regra__

Campo: vCredPres \- Total do Crédito Presumido \(IBS\)\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN18

__\[EXCLUÍDA – MFS\-951840\]__Campo 18 \- VLR\_TOT\_CRED\_PRES\_C\_SUS\_IBS 

__Regra__

Campo: vCredPresCondSus \- Total do Crédito Presumido Condição Suspensiva \(IBS\)\. 

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN19

__\[EXCLUÍDA – MFS\-951840\]__Campo 19 \- VLR\_TOT\_CRED\_PRES\_CBS

__Regra__

Campo: vCredPres \- Total do Crédito Presumido \(CBS\)\. 

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN20

__\[EXCLUÍDA – MFS\-951840\]__Campo 20 \- VLR\_TOT\_CRED\_PRES\_C\_SUS\_CBS 

__Regra__

Campo: vCredPresCondSus \- Total do Crédito Presumido Condição Suspensiva \(CBS\)\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN17

Campo 17 \- VLR\_TOT\_DIF\_CBS

__Regra__

Campo: Total do Diferimento \(CBS\)\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN18

Campo 18 \- VLR\_TOT\_DEV\_TRIB\_CBS 

__Regra__

Campo: Total de Devolução do tributo CBS\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN19

Campo 19 \- VLR\_TOT\_CBS

__Regra__

Campo: Total do CBS\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN20

Campo 20\- VLR\_TOT\_TRIB\_REG\_IBS\_UF

__Regra__

Campo: Total do IBS da UF – tributação regular

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN21

Campo 21 \- VLR\_TOT\_TRIB\_REG\_IBS\_MUN

__Regra__

Campo: Total do IBS do Município – tributação regular

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN22

Campo 22\- VLR\_TOT\_TRIB\_REG\_CBS

__Regra__

Campo: Total da CBS – tributação regular

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN23

Campo 23 \- VLR\_TOT\_IBS\_UF\_COMPRA\_GOVERN

__Regra__

Campo: Total do IBS da UF utilizado em Compras governamentais

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN24

Campo 24\- VLR\_TOT\_IBS\_MUN\_COMPRA\_GOVERN

__Regra__

Campo: Total do IBS do Município utilizado em Compras governamentais

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN25

Campo 25\- VLR\_TOT\_CBS\_COMPRA\_GOVERN

__Regra__

Campo: Total da CBS utilizado em Compras governamentais

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN26

Campo 26 \- VLR\_TOT\_IBS\_ESTORNADO

__Regra__

Campo: Total do IBS estornado

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN27

Campo 27\- VLR\_TOT\_CBS\_ESTORNADO

__Regra__

Campo:  Total da  CBS estornado\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN28

Campo 28 \- TIPO\_ENTE\_GOVERN

__Regra__

Campo: Tipo de Ente

__Valores Válidos: __

Numérico com 1 posição \(001\)\.

Informar o Tipo de Ente

Para administração pública direta e suas autarquias e fundações:

1=União

2=Estados

3=Distrito Federal

4=Municípios

__Críticas__

Preenchimento não obrigatório, mas, se preenchido, deve ser informado um valor válido, caso contrário, exibir a mensagem <<913266>>

MFS\-851810

RN29

Campo 29 \- PERC\_RED\_ALIQ\_COMPRA\_GOVERN

__Regra__

Campo:  Percentual de redução de alíquota em compra governamental\.

__Valores Válidos: __

Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

Quando uma Regra de Negócio for excluída, deverá ser indicada__, em sua posição original, __uma observação conforme exemplo abaixo descrita abaixo:

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

Quando uma Regra de Negócio for alterada, deverá ser indicada__, em sua posição original, __uma observação conforme exemplo abaixo descrita abaixo:

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

