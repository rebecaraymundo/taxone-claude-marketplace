# MTZ_JOB_SERVIDOR_Importacao_SAFX3043

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX3043.docx
- **Modificado:** 2025-11-05
- **Tamanho:** 110 KB

---

THOMSON REUTERS

Reforma Tributária

Nota Fiscal Fatura de Serviço de Comunicação Eletrônica, modelo 62

<a id="_Hlk201924536"></a>SAFX3043 – Itens de Documentos Fiscais de Utilities

Localização: Menu Básicos > Módulo Job Servidor

Processos:

- Carga >>Programação >> Execução
- Importação >> Programação >> Execução
- Importação batch >> Programação >> Execução
- Exportação de Dados >> Programação >> Execução

Sumário

[1\.	CONTROLE DE ALTERAÇÕES	3](#_Toc212714063)

[2\.	INTRODUÇÃO	4](#_Toc212714064)

[3\.	DOCUMENTOS DE REFERÊNCIA	4](#_Toc212714065)

[4\.	DEFINIÇÃO DAS REGRAS	4](#_Toc212714066)

[4\.1\.	Estrutura SAFX3043	5](#_Toc212714067)

[4\.2\.	Regras dos Campos \- SAFX3043	8](#_Toc212714068)

# <a id="_Toc462320891"></a><a id="_Toc212714063"></a>CONTROLE DE ALTERAÇÕES

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

Correção das nomenclaturas dos campos para o imposto CBS ao invés de IBS:

44\-Código do Crédito Presumido da CBS

45\-Percentual de crédito presumido da CBS

46\-Valor do crédito presumido da CBS

47\-Valor do Crédito Presumido Condição Suspensiva da CBS\.

Exclusão de campos duplicados:

36\-Alíquota efetiva da UF Informado a Alíquota caso não cumprida a condição resolutória/suspensiva \(ALIQ\_TRIB\_REG\_IBS\_UF\) 

37\-Informado como seria o valor do Tributo da UF caso não cumprida a condição resolutória/suspensiva \(VLR\_TRIB\_REG\_TRIB\_IBS\_UF\)\.

Ajustes nas nomenclaturas dos campos:

41 \- PERC\_CRED\_PRES\_IBS

43\-VLR\_CRED\_PRES\_C\_SUS\_IBS

45 \- PERC\_CRED\_PRES\_CBS

47\-VLR\_CRED\_PRES\_C\_SUS\_CBS

Alteração do tipo de campo de N para A e inclusão de validações:

10 \- Código da Situação Tributária do IBS/CBS

11 \- Código da Classificação Tributária do IBS/CBS

34 \- Código da Situação Tributária Informado como seria o CST caso não cumprida a condição resolutória/suspensiva

35 \- Código de Classificação Tributária Informado como seria o cClassTrib caso não cumprida a condição Resolutória/suspensiva

40 \- Código do Crédito Presumido do IBS

44 \- Código do Crédito Presumido da CBS

Reordenação dos campos, devido as exclusões\.

Ajuste nos campos do arquivo de reserva da SAFX3043, atualização da TFIX96, TFIX97 e do mapeamento da Reforma Tributária\.

Alessandra Navatta

28/10/2025

MFS\-951840

Em atendimento ao INFOLEGIS 2191/25 \- M \- NFCOM \- NT RTC 2025\.001\_v\.1\.10, temos:

- Inclusão do campo de Indicador de Doação,
- Inclusão do campo de valor do tributo do IBS \(IBS UF\+ IBS MUN\)
- Inclusão dos campos de Tributação Regular \(alíquota efetiva e tributo do IBS MUN\)
- Alteração dos nomes técnicos dos campos de valor do tributo do IBS UF e CBS da tributação regular
- Exclusão dos campos de Crédito Presumido
- Ajustes em nomenclatura e nome técnico dos campos referente a compra governamental
- Inclusão dos campos de valor a ser estornado \(IBS e CBS\)
- Alteração na validação dos campos de Classificação Tributária do IBS/CBS e Classificação Tributária do IBS/CBS de tributação regular

Alessandra Navatta

# <a id="_Toc462320892"></a><a id="_Toc212714064"></a>INTRODUÇÃO

V1 \- O objetivo desse documento é descrever a estrutura de campos das tabelas SAFX para o repositório das informações da RT \(IBS e CBS\) para os processos da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica, modelo 62 conforme mapeamento realizado no documento de requisitos de negócio relacionado no item 3\. 

V2 – Atualização versão 1\.4 da NT \(correção dos campos no layout\)\. 

V2 \- Atualização versão 1\.5a da NT \(correção dos campos no layout\)\.

V2 \- Acrescentados os campos para atender do grupo gCompraGov referente ao processo de Compras Governamentais\.

V3 – Elaboração da SAFX3043\.

# <a id="_Toc212714065"></a>DOCUMENTOS DE REFERÊNCIA

V1 \- [T1\_RT \- NFCom Modelo 62\_Requisitos de negocios\_v1\.docx](https://trten.sharepoint.com/:w:/r/sites/MarcosTeam/Shared%20Documents/General/Projetos/Solu%C3%A7%C3%B5es/Tax%20One/Reforma%20Tributaria/NFCOM%20-%20Mod%2062/T1_RT%20-%20NFCom%20Modelo%2062_Requisitos%20de%20negocios_v1.docx?d=w53da0d8bb8a44744a8b55fb4b7ec1f25&csf=1&web=1&e=PmKGH8) seções 2\.2, 3\.1\.1 e 7\.1\.\- Criação da estrutura SAFX para os imposto CBS e IBS\. 

V1 \- [Manual\_Layout\_MastersafDW\.xls](https://trten.sharepoint.com/:x:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Manuais-de-layout/Layout%20SAFX/Manual_Layout_MastersafDW.xls?d=we422f97384284e35897a6622693cca04&csf=1&web=1&e=nfPEBB) \- Layout dos Arquivo Mastersaf DW e ONESOURCE Tax One | Patch 306\.1\.1 \(SAFX08 e SAFX43\)

V1 \- 

![](data:image/x-emf;base64,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TAAAAGQAAAAAAAAAWgAAAAUEAABdAAAAAAAAAFoAAAAGBAAABAAAACEA8AAAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACUAAAAMAAAAAAAAgCgAAAAMAAAAAgAAABgAAAAMAAAAAAAAAlIAAABwAQAAAgAAABAAAAAHAAAAAAAAAAAAAAC8AgAAAAAAAAECAiJBAHIAaQBhAGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGR2AAgAAAAAJQAAAAwAAAACAAAAJQAAAAwAAAACAAAARgAAADQAAAAoAAAARU1GKypAAAAkAAAAGAAAAAAAgD8AAACAAAAAgAAAgD8AAACAAAAAgEYAAAAcAAAAEAAAAEVNRisCQAAADAAAAAAAAAAOAAAAFAAAAAAAAAAQAAAAFAAAAA==)V2 \- [Nota Técnica RTC\_v1\.05a](file:///C://Users/6132884/Downloads/NFCom_Nota_Tecnica_2025_001_RTC_v1.05a.pdf) incluir os novos campos referente às Compras Governamentais\. 

V2 – link – De\_para dos campos da DFe x SAFX\. 

# <a id="_Toc212714066"></a>DEFINIÇÃO DAS REGRAS

No contexto da Reforma tributária, o repositório de dados fiscais do Tax One terá sua estrutura atualizada para suportar os novos impostos com base na versão da publicação na presente data\. Nesse documento abordaremos a proposta de solução para os processos fiscais da __Nota Fiscal Fatura de Serviço de Comunicação Eletrônica NFCOM – Modelo 62 __suportados pela estrutura de arquivos:

__Operações de Saídas__

SAFX3042 – Capa de Documentos Fiscais de Utilities

SAFX3043 \- Itens de Documentos Fiscais de Utilities;

__Operações de entradas__

SAFX3007 \- Arquivo de Notas Fiscais;

SAFX3008\- Itens Notas Fiscais Mercadorias e Produtos\.

As informações para criação dos novos arquivos SAFX foram elaboradas com base na versão NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a da NFCom\.

## <a id="_Dashboard_–_Visão_1"></a><a id="_Toc212714067"></a>Estrutura SAFX3043  

Obg\.

Nr

Nome do campo

Campo

Tam

Tipo

\(\*\)

01

Código da Empresa

COD\_EMPRESA

003

A

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

006

A

\(\*\)

03

Data da Emissão/Escrita Fiscal

DAT\_FISCAL

008

N

\(\*\)

04

Indicador da Pessoa Física/Jurídica

IND\_FIS\_JUR

001

A

\(\*\)

05

Código do Destinatário/Emitente

COD\_FIS\_JUR

014

A

\(\*\)

06

Número do Documento Fiscal

NUM\_DOCFIS

012

A

\(\*\)

07

Série

SERIE\_DOCFIS

003

A

\(\*\)

08

Subsérie

SUB\_SERIE\_DOCFIS

002

A

\(\*\)

09

Item Nota Fiscal

NUM\_ITEM

007

N

 

10

Código da Situação Tributária do IBS/CBS

CST\_IBS\_CBS

003

A

 

11

Código da Classificação Tributária do IBS/CBS

CCLASS\_IBS\_CBS

006

A

12

Indicador de doação

IND\_DOACAO

001

A

 

13

Valor da Base de cálculo IBS/CBS

BC\_IBS\_CBS

015V002

N

 

14

Alíquota do IBS de competência da UF

ALIQ\_IBS\_UF

003V004

N

 

15

Percentual de diferimento do IBS de competência da UF

PERC\_DIF\_IBS\_UF

003V004

N

 

16

Valor do diferimento IBS de competência da UF

VLR\_DIF\_IBS\_UF

015V002

N

 

17

Valor do tributo devolvido do IBS de competência da UF

VLR\_TRIB\_DEV\_IBS\_UF

015V002

N

 

18

Percentual da redução de Alíquota do IBS de competência da UF

PERC\_RED\_ALIQ\_IBS\_UF

003V004

N

 

19

Alíquota efetiva do IBS de competência das UF

ALIQ\_EFET\_IBS\_UF

003V004

N

 

20

Valor do IBS de competência da UF

VLR\_IBS\_UF

015V002

N

 

21

Alíquota do IBS Municipal

ALIQ\_IBS\_MUN

003V004

N

 

22

Percentual do diferimento do IBS de competência do Município

PERC\_DIF\_IBS\_MUN

003V004

N

 

23

Valor do Diferimento do IBS de competência do Município

VLR\_DIF\_IBS\_MUN

015V002

N

 

24

Valor do tributo devolvido do IBS de competência do Município

VLR\_TRIB\_DEV\_IBS\_MUN

015V002

N

 

25

Percentual da redução de alíquota do IBS de competência do Município

PERC\_RED\_ALIQ\_IBS\_MUN

003V004

N

 

26

Aliquota Efetiva do IBS de competência dos Municípios

ALIQ\_EFET\_IBS\_MUN

003V004

N

 

27

Valor do IBS de competência do Município

VLR\_IBS\_MUN

015V002

N

28

Valor do IBS \(IBS UF \+ IBS MUN\)

TOT\_IBS\_ITEM

015V002

N

 

29

Alíquota da CBS

ALIQ\_CBS

003V004

N

 

30

Percentual do diferimento da CBS

PERC\_DIF\_CBS

003V004

N

 

31

Valor do Diferimento da CBS

VLR\_DIF\_CBS

015V002

N

 

32

Valor do tributo devolvido da CBS

VLR\_TRIB\_DEV\_CBS

015V002

N

 

33

Percentual da redução de alíquota da CBS

PERC\_RED\_ALIQ\_CBS

003V004

N

 

34

Alíquota Efetiva da CBS 

ALIQ\_EFET\_CBS

003V004

N

 

35

Valor da CBS

VLR\_CBS

015V002

N

 

36

Código da Situação Tributária \- Tributação Regular

CST\_TRIB\_REG\_IBS\_CBS

003

A

 

37

Código de Classificação Tributária\- \- Tributação Regular

CCLASS\_TRIB\_REG\_IBS\_CBS

006

A

 

38

Valor da alíquota do IBS da UF \- tributação regular

ALIQ\_TRIB\_REG\_IBS\_UF

003V004

N

 

39

Valor do Tributo do IBS da UF \- tributação regular

VLR\_TRIB\_REG\_IBS\_UF

015V002

N

40

Valor da alíquota efetiva do IBS do Município \- tributação regular

ALIQ\_TRIB\_REG\_IBS\_MUN

003V004

N

41

Valor do Tributo do IBS do Município \- tributação regular

VLR\_TRIB\_REG\_IBS\_MUN

015V002

N

 

42

Valor da alíquota da CBS \- tributação regular

ALIQ\_TRIB\_REG\_CBS

003V004

N

 

43

Valor do Tributo da CBS \- tributação regular

VLR\_TRIB\_REG\_CBS

015V002

N

 

40

Código do Crédito Presumido do IBS

CCLASS\_CRED\_PRES\_IBS

003

A

 

41

Percentual de crédito presumido do IBS

PERC\_CRED\_PRES\_IBS

003V004

N

 

42

Valor do crédito presumido do IBS

VLR\_CRED\_PRES\_IBS

015V002

N

 

43

Valor do Crédito Presumido Condição Suspensiva do IBS

VLR\_CRED\_PRES\_C\_SUS\_IBS

015V002

N

 

44

Código do Crédito Presumido da CBS

CCLASS\_CRED\_PRES\_CBS

003

A

 

45

Percentual de crédito presumido da CBS

PERC\_CRED\_PRES\_CBS

003V004

N

 

46

Valor do crédito presumido da CBS

VLR\_CRED\_PRES\_CBS

015V002

N

 

47

Valor do Crédito Presumido Condição Suspensiva da CBS

VLR\_CRED\_PRES\_C\_SUS\_CBS

015V002

N

 

44

Alíquota IBS da UF utilizada em compras governamentais

ALIQ\_IBS\_UF\_COMPRA\_GOVERN

003V004

N

 

45

Valor do Tributo do IBS da UF \(Monofásico\) utilizado em Compras governamentais

VLR\_IBS\_UF\_COMPRA\_GOVERN

015V002

N

 

46

Alíquota IBS do Município utilizada em compras governamentais

ALIQ\_IBS\_MUN\_COMPRA\_GOVERN

003V004

N

 

47

Valor do Tributo do IBS do Município utilizado em \(Monofásico\) Compras governamentais

VLR\_IBS\_MUN\_COMPRA\_GOVERN

015V002

N

 

48

Alíquota da CBS utilizada em compras governamentais

ALIQ\_CBS\_COMPRA\_GOVERN

003V004

N

49

Valor do Tributo da CBS  \(Monofásico\) utilizado em Compras governamentais

VLR\_CBS\_COMPRA\_GOVERN

015V002

N

50

Valor do IBS a ser estornado

IBS\_ESTORNADO

015V002

N

 

51

Valor da CBS a ser estornado

CBS\_ESTORNADO

015V002

N

__Alterações da versão 1\.4 __\[ADO\- 818668\] 

Campos 23, 30 e 36 – Alterado o texto de “Percentual da redução de Alíquota” para “Percentual da redução de Alíquota *do cClassTrib*”\. 

Campos 24 e 37 – Alterado o texto de “Alíquota efetiva do IBS/CBS  de competência das UF que será aplicada a base de cálculo” para “ Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo*, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)”*

__Alterações da versão 1\.5__ \[ADO\- 837947\]

Sem reflexos\. Ajuste na regra de validação G134 \- Município do Emitente diverge da UF\. 

__Alterações da versão 1\.5a__ \[ADO\-843670 | 842052\] 

Inclusão dos campos 49 a 54 – Acrescentadas as colunas com os campos para atender às Compras Governamentais\. 

## <a id="_Dashboard_–_Visão"></a><a id="_Toc212714068"></a>Regras dos Campos \- SAFX3043 

__Cód\.__

__Descrição__

__OS__

RN00

Regras Gerais

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

MFS\-851810

RN01 a 09

A tabela SAFX3043 é filha da tabela SAFX43 e deve refletir exatamente os dados do documento fiscal \(ver item 4\.1\)\. 

Chave de identificação 🡪 Empresa \+ Estabelecimento \+ Data \+ Pessoa Fis/Jur \+ Núm/Sér/Sub Documento \+ Núm do Item\.

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

__NUM\_ITEM__: Verifica o preenchimento do campo, e se não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90132 da TFIX22\)\.

Após a validação dos campos 01 ao 08, será verificada a existência da capa do documento informado na tabela SAFX43, a partir dos campos chave da tabela\. Se não identificado, será gravada a mensagem de erro padrão no log da importação \(mensagem 92496 da TFIX22\)\.

MFS\-851810

RN10

Campo 10 \- CST\_IBS\_CBS

__Regra__

Campo: Código da Classificação Tributária do IBS/CBS\. 

__Valores Válidos: __Alfanumérico – 3 dígitos  

__Críticas__

Preenchimento não obrigatório\.

O código deverá estar previamente cadastrado conforme a TACES : __TACES115__ \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária, caso não encontrado, exibir a mensagem: <<913267>>

MFS\-851810

RN11

Campo 11 \- CCLASS\_IBS\_CBS

__Regra__

Campo: Código da Classificação Tributária do IBS/CBS\. 

__Valores Válidos: __ Alfanumérico – 6 dígitos  

__Críticas__

Preenchimento não obrigatório\.

O código deve estar cadastrado na taces117\- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária e vinculado ao CST indicado no campo anterior, caso não esteja cadastrado, ou se cadastrado, mas, não vinculado, exibir a mensagem:<< 913310>

MFS\-851810

MFS\-951840

RN12

Campo 12 \-IND\_DOACAO

__Regra__

Campo: Indicador de Doação

 Formato__: Alfanumérico __com 1 posição

Lista de Valores Válidos:

Nulo

0 – Operação normal, sem doação\. 

1 – Operação com doação

__Críticas__

Quando preenchido, se for informado um conteúdo diferente, retornar mensagem <<913309>>: “Campo Indicador de Doação Inválido\. Conteúdo do campo deve ser igual a <0> ou <1>\.”

MFS\-951840

RN13

Campo 13 \- BC\_IBS\_CBS

__Regra__

Campo: Valor da Base de cálculo IBS/CBS\. 

 __Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN14

Campo 14 \- ALIQ\_IBS\_UF

__Regra__

Campo: Alíquota do IBS de competência da UF\.   
__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN15

Campo 15 \- PERC\_DIF\_IBS\_UF

__Regra__

Campo: Percentual de diferimento\. 

Percentual do diferimento do IBS de competência da UF\.   
__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN16

Campo 16 \- VLR\_DIF\_IBS\_UF

__Regra__

Campo: Valor do diferimento\.

Valor do Diferimento do IBS de competência da UF\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN17

Campo 17 \- VLR\_TRIB\_DEV\_IBS\_UF

__Regra__

Campo:  Valor do tributo devolvido\.

Valor do tributo devolvido do IBS de competência da UF\.  
__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN18

Campo 18 \- PERC\_RED\_ALIQ\_IBS\_UF

__Regra__

Campo: pRedAliq \(grupo gRed\) \- Percentual da redução de Alíquota do cClassTrib\.

Percentual da redução de alíquota do IBS de competência da UF\.  
__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN19

Campo 19 \- ALIQ\_EFET\_IBS\_UF

__Regra__

Campo: Alíquota efetiva do IBS de competência das UF 

Alíquota do IBS de competência das UF

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN20

Campo 20 \- VLR\_IBS\_UF

__Regra__

Campo: Valor do IBS de competência da UF\. 

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN21

Campo 21 \- ALIQ\_IBS\_MUN

__Regra__

Campo: Alíquota do IBS Municipal\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN22

Campo 22 \- PERC\_DIF\_IBS\_MUN

__Regra__

Campo:  Percentual de diferimento\.

Percentual do diferimento do IBS de competência do Município

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.__ __

MFS\-851810

RN23

Campo 23 \- VLR\_DIF\_IBS\_MUN

__Regra__

Campo: Valor do diferimento\.

Valor do Diferimento do IBS de competência do Município

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

Preenchimento não obrigatório e sem críticas\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN24

Campo 24 \- VLR\_TRIB\_DEV\_IBS\_MUN

__Regra__

Campo:Valor do tributo devolvido\.

Valor do tributo devolvido do IBS de competência do Município\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN25

Campo 25 \- PERC\_RED\_ALIQ\_IBS\_MUN

__Regra__

Campo: Percentual da redução de Alíquota do cClassTrib\.

Percentual da redução de alíquota do IBS de competência do Município

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN26

Campo 26 \- ALIQ\_EFET\_IBS\_MUN

__Regra__

Campo: Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. 

Alíquota Efetiva do IBS de competência dos Municípios que será aplicada a Base de Cálculo\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN27

Campo 27\- VLR\_IBS\_MUN

__Regra__

Campo: Valor do IBS de competência do município\.

Valor do IBS de competência do Município\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN28

Campo 28 – TOT\_IBS\_ITEM

__Regra__

Campo: Valor do IBS \(IBS UF \+ IBS MUN\)

Valor do IBS \(IBS UF \+ IBS MUN\)

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN29

Campo 29 \- ALIQ\_CBS

__Regra__

Campo: Alíquota da CBS\. 

Alíquota da CBS\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.__ __

MFS\-851810

RN30

Campo 30\- PERC\_DIF\_CBS

__Regra__

Campo: Percentual de diferimento\. 

Percentual de diferimento da CBS\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.__ __

MFS\-851810

RN31

Campo 31 \- VLR\_DIF\_CBS

__Regra__

Campo: Valor do diferimento da CBS\.

Valor do diferimento da CBS

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.__ __

MFS\-851810

RN32

Campo 32 \- VLR\_TRIB\_DEV\_CBS

__Regra__

Campo:  Valor da CBS devolvida\.

Valor do tributo devolvido da CBS\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN33

Campo 33 \- PERC\_RED\_ALIQ\_CBS

__Regra__

Campo: Percentual da redução de Alíquota da CBS  
Percentual da redução de alíquota da CBS\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN34

Campo 34 \- ALIQ\_EFET\_CBS

__Regra__

Campo:Alíquota efetiva da CBS

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN35

Campo 35 \- VLR\_CBS

__Regra__

Campo: Valor da CBS\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.__ __

MFS\-851810

RN36

Campo 36 \- CST\_TRIB\_REG\_IBS\_CBS

__Regra__

Campo: Código da Situação Tributária da tributação regular\.

__Valores Válidos: __Alfanumérico com 3 posições\.

__Críticas__

Preenchimento não obrigatório\.

O código deverá estar previamente cadastrado conforme a TACES : __TACES115__ \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária, caso não encontrado, exibir a mensagem: <<913269>>

MFS\-851810

RN37

Campo 37 \- CCLASS\_TRIB\_REG\_IBS\_CBS

__Regra__

Campo: Código de Classificação Tributária da tributação regular\.

__Valores Válidos: __Alfanumérico com 6 posições\. 

__Críticas__

Preenchimento não obrigatório\.

O código deve estar cadastrado na taces117\- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária e vinculado ao CST indicado no campo anterior, caso não esteja cadastrado, ou se cadastrado, mas, não vinculado, exibir a mensagem:<< 913311>

MFS\-851810

MFS\-951840

RN38

Campo 38\- ALIQ\_TRIB\_REG\_IBS\_UF

__Regra__

Campo: Alíquota efetiva do IBS da UF \- tributação regular

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN39

Campo 39 \- VLR\_TRIB\_REG\_IBS\_UF

__Regra__

Campo: Valor do Tributo do IBS da UF \- tributação regular\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN40

Campo 40\- ALIQ\_TRIB\_REG\_IBS\_MUN

__Regra__

Campo: Alíquota efetiva do IBS do Município \- tributação regular

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN41

Campo 41 \- VLR\_TRIB\_REG\_IBS\_MUN

__Regra__

Campo: Valor do Tributo do IBS do município\- tributação regular\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN42

Campo 42 \- ALIQ\_TRIB\_REG\_CBS

__Regra__

Campo: Alíquota efetiva da CBS – tributação regular

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN43

Campo 43 \- VLR\_TRIB\_REG\_CBS 

__Regra__

Campo: Valor do Tributo da CBS \- tributação regular\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN40

Campo 40 \- CCLASS\_CRED\_PRES\_IBS

__Regra__

Campo: cCredPres \- Código do Crédito Presumido do IBS

__Valores Válidos: __Alfanumérico com 3 posições\. 

__Críticas__

Preenchimento não obrigatório\.

O Codigo de Classificacao do Credito Presumido do IBS, deve estar previamente cadastrada na TACES118 \- Tabela de Codigo de Credito Presumido do IBS e do CBS\- Reforma Tributaria, caso não encontrado, exibir a mensagem: <<913271>>\.

MFS\-851810

RN41

Campo 41 \- PERC\_CRED\_PRES\_IBS

__Regra__

Campo: pCredPres – Percentual\.

Percentual de crédito presumido do IBS

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN42

Campo 42 \- VLR\_CRED\_PRES\_IBS

__Regra__

Campo: vCredPres \- Valor do crédito presumido do IBS

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN43

Campo 43 \- VLR\_CRED\_PRES\_C\_SUS\_IBS

__Regra__

Campo: vCredPresCondSus \- Valor do Crédito Presumido Condição Suspensiva do IBS

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas __

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN44

Campo 44 \- CCLASS\_CRED\_PRES\_CBS

__Regra__

Campo: cCredPres \- Código do Crédito Presumido da CBS

__Valores Válidos: __Alfanumérico com 3 posições

__Críticas__ 

Preenchimento não obrigatório\.

O Codigo de Classificacao do Credito Presumido da CBS, deve estar previamente cadastrada na TACES118 \- Tabela de Codigo de Credito Presumido do IBS e do CBS\- Reforma Tributaria, caso não encontrado, exibir a mensagem: <<913272>>

MFS\-851810

RN45

Campo 45 \- PERC\_CRED\_PRES\_CBS

__Regra__

Campo: pCredPres \- Percentual de crédito presumido da CBS

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas __

MFS\-851810

RN46

Campo 46 \- VLR\_CRED\_PRES\_CBS

__Regra__

Campo: vCredPres \- Valor do crédito presumido da CBS\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN47 

Campo 47 \- VLR\_CRED\_PRES\_C\_SUS\_CBS

__Regra__

Campo: vCredPresCondSus \- Valor do Crédito Presumido Condição Suspensiva da CBS\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

MFS\-851810

RN44

Campo 44\- ALIQ\_IBS\_UF\_COMPRA\_GOVERN

__Regra__

Campo: Alíquota IBS da UF utilizada em compras governamentais\. 

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN45

Campo 45 \- VLR\_IBS\_UF\_COMPRA\_GOVERN

__Regra__

Campo:Valor do Tributo do IBS da UF utilizado em compras governamentais\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

MFS\-851810

RN46

Campo 46\- ALIQ\_IBS\_MUN\_COMPRA\_GOVERN

__Regra__

Campo:Alíquota IBS do Município utilizada em compras governamentais\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN47

Campo 47\- VLR\_IBS\_MUN\_COMPRA\_GOVERN

__Regra__

Campo: Valor do Tributo do IBS do Município utilizada em compras governamentais\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN48

Campo 48 \- ALIQ\_CBS\_COMPRA\_GOVERN

__Regra__

Campo: Alíquota da CBS utilizada em compras governamentais\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN49

Campo 49\- VLR\_CBS\_COMPRA\_GOVERN

__Regra__

Campo: Valor do Tributo da CBS utilizado em compras governamentais\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-851810

RN50

Campo 50\- IBS\_ESTORNADO

__Regra__

Campo: Valor do IBS a ser estornado\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

RN51

Campo 51\- CBS\_ESTORNADO

__Regra__

Campo: Valor da CBS a ser estornado\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

Preenchimento não obrigatório e sem críticas\.

MFS\-951840

Quando uma Regra de Negócio for Excluída, deverá ser indicada__, em sua posição original, __uma observação conforme exemplo abaixo descrito abaixo:

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada__, em sua posição original, __uma observação conforme exemplo abaixo descrito abaixo:

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

As informaçõs de entrada serão suportadas pelos arquivos SAFX3007RT e SAFX2008RT conforme os campos dsiponíveis em sua documentação\. 

