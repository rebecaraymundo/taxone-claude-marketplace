# MTZ_RT_NFCom_Mod 62 - SAFX3042 e SAFX3043

- **Fonte:** MTZ_RT_NFCom_Mod 62 - SAFX3042 e SAFX3043.docx
- **Modificado:** 2025-09-08
- **Tamanho:** 116 KB

---

THOMSON REUTERS

Reforma Tributária

Nota Fiscal Fatura de Serviço de Comunicação Eletrônica, modelo 62

ONESOURCE Tax One

SAFX3042 \- Capa de Documentos Fiscais de Utilities e

 <a id="_Hlk201924536"></a>SAFX3043 – Itens de Documentos Fiscais de Utilities

Sumário

[1\.	CONTROLE DE ALTERAÇÕES	3](#_Toc202363489)

[2\.	INTRODUÇÃO	4](#_Toc202363490)

[3\.	DOCUMENTOS DE REFERÊNCIA	4](#_Toc202363491)

[4\.	DEFINIÇÃO DAS REGRAS	5](#_Toc202363492)

[4\.1\.	Regras de Negócio \- SAFX3042	6](#_Toc202363493)

[4\.2\.	Regras dos campos \- SAFX3042	7](#_Toc202363494)

[4\.3\.	Regras de Negócio \- SAFX3043 | Itens de Documentos Fiscais de Utilities	11](#_Toc202363495)

[4\.4\.	Regras dos Campos \- SAFX3043 | Itens de Documentos Fiscais de Utilities	15](#_Toc202363496)

# <a id="_Toc462320891"></a><a id="_Toc202363489"></a>CONTROLE DE ALTERAÇÕES

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

# <a id="_Toc462320892"></a><a id="_Toc202363490"></a>INTRODUÇÃO

V1 \- O objetivo desse documento é descrever a estrutura de campos das tabelas SAFX para o repositório das informações da RT \(IBS e CBS\) para os processos da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica, modelo 62 conforme mapeamento realizado no documento de requisitos de negócio relacionado no item 3\. 

V2 – Atualização versão 1\.4 da NT \(correção dos campos no layout\)\. 

V2 \- Atualização versão 1\.5a da NT \(correção dos campos no layout\)\.

V2 \- Acrescentados os campos para atender do grupo gCompraGov referente ao processo de Compras Governamentais\.

V3 – Elaboração das Novas SAFX3042 e SAFX3043\.

# <a id="_Toc202363491"></a>DOCUMENTOS DE REFERÊNCIA

V1 \- [T1\_RT \- NFCom Modelo 62\_Requisitos de negocios\_v1\.docx](https://trten.sharepoint.com/:w:/r/sites/MarcosTeam/Shared%20Documents/General/Projetos/Solu%C3%A7%C3%B5es/Tax%20One/Reforma%20Tributaria/NFCOM%20-%20Mod%2062/T1_RT%20-%20NFCom%20Modelo%2062_Requisitos%20de%20negocios_v1.docx?d=w53da0d8bb8a44744a8b55fb4b7ec1f25&csf=1&web=1&e=PmKGH8) seções 2\.2, 3\.1\.1 e 7\.1\.\- Criação da estrutura SAFX para os imposto CBS e IBS\. 

V1 \- [Manual\_Layout\_MastersafDW\.xls](https://trten.sharepoint.com/:x:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Manuais-de-layout/Layout%20SAFX/Manual_Layout_MastersafDW.xls?d=we422f97384284e35897a6622693cca04&csf=1&web=1&e=nfPEBB) \- Layout dos Arquivo Mastersaf DW e ONESOURCE Tax One | Patch 306\.1\.1 \(SAFX08 e SAFX43\)

V1 \- 

![](data:image/x-emf;base64,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TAAAAGQAAAAAAAAAWgAAAAUEAABdAAAAAAAAAFoAAAAGBAAABAAAACEA8AAAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACUAAAAMAAAAAAAAgCgAAAAMAAAAAgAAABgAAAAMAAAAAAAAAlIAAABwAQAAAgAAABAAAAAHAAAAAAAAAAAAAAC8AgAAAAAAAAECAiJBAHIAaQBhAGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGR2AAgAAAAAJQAAAAwAAAACAAAAJQAAAAwAAAACAAAARgAAADQAAAAoAAAARU1GKypAAAAkAAAAGAAAAAAAgD8AAACAAAAAgAAAgD8AAACAAAAAgEYAAAAcAAAAEAAAAEVNRisCQAAADAAAAAAAAAAOAAAAFAAAAAAAAAAQAAAAFAAAAA==)V2 \- [Nota Técnica RTC\_v1\.05a](C://Users/6132884/Downloads/NFCom_Nota_Tecnica_2025_001_RTC_v1.05a.pdf) incluir os novos campos referente às Compras Governamentais\. 

V2 – link – De\_para dos campos da DFe x SAFX\. 

# <a id="_Toc202363492"></a>DEFINIÇÃO DAS REGRAS

No contexto da Reforma tributária, o repositório de dados fiscais do Tax One terá sua estrutura atualizada para suportar os novos impostos com base na versão da publicação na presente data\. Nesse documento abordaremos a proposta de solução para os processos fiscais da __Nota Fiscal Fatura de Serviço de Comunicação Eletrônica  NFCOM – Modelo 62 __suportados pela estrutura de arquivos:

__Operações de Saídas__

SAFX3042 – Capa de Documentos Fiscais de Utilities

SAFX3043 \- Itens de Documentos Fiscais de Utilities;

__Operações de entradas__

SAFX3007RT \- Arquivo de Notas Fiscais;

SAFX3008RT \- Itens Notas Fiscais Mercadorias e Produtos\.

As informações para criação dos novos arquivos SAFX foram elaboradas com base na versão NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a da NFCom\.

## <a id="_Dashboard_–_Visão_1"></a> <a id="_Toc202363493"></a>Regras de Negócio \- SAFX3042

O objetivo do arquivo SAFX3042 Capa de Documentos Fiscais de Utilities  é atender aos documentos fiscais da NFCOM – Modelo 62 e as informações dos impostos CBS e IBS oriundos do projeto da Reforma tributária\. 

Obg\.

Nr

Nome do campo

Campo

Comentário

Tam

Tipo

\(\*\)

1

Código da Empresa

COD\_EMPRESA

Código da Empresa

003

A

\(\*\)

2

Código do Estabelecimento

COD\_ESTAB

Código do Estabelecimento

006

A

\(\*\)

3

Data de Emissão/Escr\. Fiscal

DAT\_FISCAL

Informar a Data da Emissão do Documento\.

008

N

\(\*\)

4

Indicador Pessoa Física/Jurídica

IND\_FIS\_JUR

Informar o Indicador de Pessoa Física/Jurídica relacionada, conforme segue:  
1 \- Fornecedor  
2 \- Cliente  
3 \- Estabelecimento  
4 \- Transportadora  
5 \- Cliente/Fornecedor/Transportadora

001

A

\(\*\)

5

Código/Destinatário/Emitente/Remetente

COD\_FIS\_JUR

Informar o código /Destinatário /Emitente/Remetente, deve estar registrado na Tabela de Pessoa Física/Jurídica \(SAFX04\)\.

014

A

\(\*\)

6

Número do Documento Fiscal

NUM\_DOCFIS

Informar o Número da NFST\.

012

A

 

7

Série

SERIE\_DOCFIS

Informar o Número de série do Documento Fiscal\.

003

A

 

8

Subsérie

SUB\_SERIE\_DOCFIS

Informar o Número de subsérie do Documento Fiscal\.

002

A

 

9

Total da Base de cálculo do IBS/CBS

VLR\_TOT\_BC\_IBS\_CBS

Informar o valor total da BC do IBS e da CBS\.

015V002

N

 

10

Total do Diferimento

VLR\_TOT\_DIF\_IBS\_UF

Informar o valor total do diferimento do IBS de competência da UF\.

015V002

N

 

11

Total de Devolução de Tributo IBS UF

VLR\_TOT\_DEV\_TRIB\_IBS\_UF

Informar o valor total de devolução de tributos do IBS de competência da UF\.

015V002

N

 

12

Total do IBS UF

VLR\_TOT\_IBS\_UF

Informar o valor total do IBS da UF\.

015V002

N

 

13

Total do Diferimento

VLR\_TOT\_DIF\_IBS\_MUN

Informar o valor total do diferimento do IBS do Município\.

015V002

N

 

14

Total de Devolução de Tributo IBS Municipal

VLR\_TOT\_DEV\_TRIB\_IBS\_MUN

Informar o valor total de devolução de tributos do IBS do Município\.

015V002

N

 

15

Total do IBS Municipal

VLR\_TOT\_IBS\_MUN

Informar o valor total do IBS do Município\.

015V002

N

 

16

Total do IBS \(IBS UF \+ IBS Mun\)

VLR\_TOT\_IBS

Informar o valor total do IBS\.

015V002

N

 

17

Total do Crédito Presumido \(IBS\)

VLR\_TOT\_CRED\_PRES\_IBS

Informar o valor total do crédito presumido do IBS\.

015V002

N

 

18

Total do Crédito Presumido Condição Suspensiva \(IBS\)

VLR\_TOT\_CRED\_PRES\_COND\_SUSP\_IBS

Informar o valor total do crédito presumido em condição suspensiva do IBS\.

015V002

N

 

19

Total do Crédito Presumido \(CBS\)

VLR\_TOT\_CRED\_PRES\_CBS

Informar o valor total do crédito presumido da CBS\.

015V002

N

 

20

Total do Crédito Presumido Condição Suspensiva \(CBS\)

VLR\_TOT\_CRED\_PRES\_COND\_SUSP\_CBS

Informar o valor total do crédito presumido em condição suspensiva da CBS\.

015V002

N

 

21

Total do Diferimento \(CBS\)

VLR\_TOT\_DIF\_CBS

Informar o valor total do diferimento da CBS\.

015V002

N

 

22

Total de Devolução do tributo CBS

VLR\_TOT\_DEV\_TRIB\_CBS

Informar o valor total de devolução de tributos da CBS\.

015V002

N

 

23

Total do CBS

VLR\_TOT\_CBS

Informar o valor total da CBS\.

015V002

N

 

24

Tipo de Ente

TIPO\_ENTE\_GOVERN

Informar o Tipo de Ente  
Para administração pública direta e suas autarquias e fundações:  
1=União  
2=Estados  
3=Distrito Federal  
4=Municípios

001

N

 

25

Percentual de redução de alíquota em compra governamental\. 

PERC\_RED\_ALIQ\_COMPRA\_GOV

Informar o Percentual de redução de alíquota em compra governamental\.   
Conforme LC 214/25: TÍTULO II DAS COMPRAS GOVERNAMENTAIS, Art\. 472

003V004

N

## <a id="_Toc202363494"></a>Regras dos campos \- SAFX3042

O objetivo do arquivo __SAFX3042 \- Capa de Documentos Fiscais de Utilities__ é atender aos documentos fiscais da NFCOM – Modelo 62 e as informações dos impostos CBS e IBS oriundos do projeto da Reforma tributária\. 

__Cód\.__

__Descrição__

__OS__

RN00

Regras Gerais

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

Para carregar as informações da tag __vTotDFe__, utilizar o campo 15 \- Valor dos serviços\.

RN01 a 08

Replica dos campos chaves SAFX42 \- Capa de Documentos Fiscais de Utilities Os campos deverão ser criados para  a nova SAFX com a mesma especificação da tabela SAFX42, considerando apenas a lista de campos no item 4\.1\. 

RN09

Campo 09 \- VLR\_TOT\_BC\_IBS\_CBS

__Regra__

Campo NT: vBCIBSCBS \- Total da Base de cálculo do IBS/CBS\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN10

Campo 10 \- VLR\_TOT\_DIF\_IBS\_UF

__Regra__

Campo NT: vDif \- Total do Diferimento

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN11

Campo 11\- VLR\_TOT\_DEV\_TRIB\_IBS\_UF 

__Regra__

Campo NT: vDevTrib \- Total de Devolução de Tributo IBS UF\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN12

Campo 12 \- VLR\_TOT\_IBS\_UF

__Regra__

Campo NT: vIBSUF \- Total do IBS UF\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN13

Campo 13\- VLR\_TOT\_DIF\_IBS\_MUN

__Regra__

Campo NT: vDif \- Total do Diferimento\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN14

Campo 14 \- VLR\_TOT\_DEV\_TRIB\_IBS\_MUN 

__Regra__

Campo NT: vDevTrib \- Total de Devolução de Tributo IBS Municipal\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN15

Campo 15 \- VLR\_TOT\_IBS\_MUN

__Regra__

Campo NT: vIBSMun \- Total do IBS Municipal\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN16

Campo 16 \- VLR\_TOT\_IBS

__Regra__

Campo NT: vIBS \- Total do IBS \(IBS UF \+ IBS Mun\)\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN17

Campo 17 \- VLR\_TOT\_CRED\_PRES\_IBS

__Regra__

Campo NT: vCredPres \- Total do Crédito Presumido \(IBS\)\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN18

Campo 18 \- VLR\_TOT\_CRED\_PRES\_COND\_SUSP\_IBS 

__Regra__

Campo NT: vCredPresCondSus \- Total do Crédito Presumido Condição Suspensiva \(IBS\)\. 

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN19

Campo 19 \- VLR\_TOT\_CRED\_PRES\_CBS

__Regra__

Campo NT: vCredPres \- Total do Crédito Presumido \(CBS\)\. 

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN20

Campo 20 \- VLR\_TOT\_CRED\_PRES\_COND\_SUSP\_CBS 

__Regra__

Campo NT: vCredPresCondSus \- Total do Crédito Presumido Condição Suspensiva \(CBS\)\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN21

Campo 21 \- VLR\_TOT\_DIF\_CBS

__Regra__

Campo NT: vDif \- Total do Diferimento \(CBS\)\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN22

Campo 22 \- VLR\_TOT\_DEV\_TRIB\_CBS 

__Regra__

Campo NT: vDevTrib \- Total de Devolução do tributo CBS\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN23

Campo 23 \- VLR\_TOT\_CBS

__Regra__

Campo NT: vCBS \- Total do CBS\.

__Valores Válidos: __

Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

 

__Observação: __

RN24

Campo 24 \- TIPO\_ENTE\_GOVERN

__Regra__

Campo NT: tpEnteGov \- Tipo de Ente

__Valores Válidos: __

Numérico com 1 posição \(001\)\.

Informar o Tipo de Ente

Para administração pública direta e suas autarquias e fundações:

1=União

2=Estados

3=Distrito Federal

4=Municípios

__Críticas__

 

__Observação: __

RN25

Campo 25 \- PERC\_RED\_ALIQ\_COMPRA\_GOV

__Regra__

Campo NT: pRedutor \- Percentual de redução de alíquota em compra governamental\.

__Valores Válidos: __

Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

 

__Observação: __

## <a id="_Toc202363495"></a>Regras de Negócio \- SAFX3043 | Itens de Documentos Fiscais de Utilities

O objetivo do arquivo SAFX3043 é atender aos documentos fiscais da NFCOM – Modelo 62 e as informações dos impostos CBS e IBS oriundos do projeto da Reforma tributária\. 

Obg\.

Nr

Nome do campo

Campo

Comentário

Tam

Tipo

\(\*\)

01

Código da Empresa

COD\_EMPRESA

Código da Empresa

003

A

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do Estabelecimento

006

A

\(\*\)

03

Data da  Emissão/Escrita Fiscal

DAT\_FISCAL

Informar a Data de Emissão da Nota Fiscal\.

008

N

\(\*\)

04

Indicador da Pessoa Física/Jurídica

IND\_FIS\_JUR

Informar o Indicador da Pessoa Física/Jurídica, de acordo com o Indicador de Pessoa Física/Jurídica relacionada\. Preencher com:  
1 \- Fornecedor  
2 \- Cliente  
3 \- Estabelecimento  
4 \- Transportadora  
5 \- Cliente/Fornecedor/Transportadora

001

A

\(\*\)

05

Código do Destinatário/Emitente

COD\_FIS\_JUR

Informar o Código do Destinatário/ Emitente, de acordo com a Tabela de Pessoa Física/Jurídica \(SAFX04\)\.

014

A

\(\*\)

06

Número do Documento Fiscal

NUM\_DOCFIS

Informar o Número da Nota Fiscal\.

012

A

\(\*\)

07

Série

SERIE\_DOCFIS

Informar a Série\.

003

A

\(\*\)

08

Subsérie

SUB\_SERIE\_DOCFIS

Informar a Subsérie\.

002

A

\(\*\)

09

Item Nota Fiscal

NUM\_ITEM

Informar o Número dos Itens sequencial de acordo com a NFST\.   
Apesar do campo possibilitar o tamanho de 05 posições, ou seja, notas fiscais com até 99\.999 itens, quanto da geração dos meios magnéticos \(Sintegra, IN86, IN89, SEF\-PE, etc\.\.\.\) o sistema irá considerar somente 03 posições, ou seja, notas fiscais com até 999 itens\. Esta consideração deve\-se ao fato dos layouts destes meios magnéticos estarem solicitando somente 03 posições\.

007

N

 

10

Código de Situação Tributária do Imposto Seletivo

CST\_IS

Informar o código de Situação Tributária do Imposto Seletivo\. Utilizar tabela CST do Imposto Seletivo 

003

N

 

11

Código de Classificação Tributária do Imposto Seletivo

CCLASS\_IS

Informar o código de Classificação Tributária do Imposto Seletivo\. Utilizar tabela cClassTribIS

006

N

 

12

Valor da Base de Cálculo do Imposto Seletivo

BC\_IS

Informar o valor da Base de Cálculo do Imposto Seletivo\.

015V002

N

 

13

Alíquota do IBS de competência das UF

ALIQ\_IBS\_UF

__Informar a alíquota do IBS de competência das UF\. Alíquota vigente do IBS da UF__

003V004

N

 

14

Percentual do diferimento do IBS de competência da UF

PERC\_DIF\_IBS\_UF

Informar o percentual do diferimento do IBS da competência da UF\.

003V004

N

 

15

Valor do Diferimento do IBS de competência da UF

VLR\_DIF\_IBS\_UF

Informar o valor do Diferimento do IBS da competência da UF\.

015V002

N

 

16

Valor do tributo devolvido do IBS de competência da UF

VLR\_TRIB\_DEVOLVIDO\_IBS\_UF

Informar o valor do tributo devolvido \(desconto na própria Nota Fiscal / Fatura\), do IBS da competência da UF\.

015V002

N

 

17

Percentual da redução de alíquota do IBS de competência da UF

PERC\_RED\_ALIQ\_IBS\_UF

Informar o percentual da redução de alíquota do IBS da competência da UF\.

003V004

N

 

18

Alíquota do IBS de competência das UF

ALIQ\_IBS\_UF

Informar a alíquota do IBS de competência das UF\. Alíquota vigente do IBS da UF

003V004

N

 

19

Valor do IBS de competência da UF

VLR\_IBS\_UF

Informar o valor do IBS de competência da UF\.

015V002

N

 

20

Alíquota do IBS Municipal

ALIQ\_IBS\_MUN

__Alíquota do IBS Municipal__

003V004

N

 

21

Percentual de diferimento  do IBS Municipal

PERC\_DIF\_IBS\_MUN

Percentual de diferimento  do IBS Municipal

003V004

N

 

22

Valor do diferimento  do IBS Municipal

VLR\_DIF\_IBS\_MUN

Valor do diferimento  do IBS Municipal

015V002

N

 

23

Valor do tributo devolvido  do IBS Municipal

VLR\_TRIB\_DEVOLVIDO\_IBS\_MUN

Valor do tributo devolvido  do IBS Municipal

015V002

N

 

24

Percentual da redução de Alíquota  do IBS Municipal

PERC\_RED\_ALIQ\_IBS\_MUN

Percentual da redução de Alíquota  do IBS Municipal

003V004

N

 

25

Aliquota Efetiva do IBS de competência dos Municípios que será aplicada a Base de Cálculo

ALIQ\_EFET\_IBS\_MUN

Alíquota efetiva do IBS de competência das municípios que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\.  
pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

003V004

N

 

26

Alíquota da CBS

ALIQ\_TRIB\_REG\_CBS

Informar a alíquota da CBS\. Alíquota vigente da CBS

003V004

N

 

27

Valor da CBS

VLR\_TRIB\_REG\_CBS

__Informar o valor da CBS\.__

015V002

N

 

28

Percentual do diferimento do IBS de competência da UF

PERC\_DIF\_IBS\_UF

Informar o percentual do diferimento do IBS da competência da UF\.

003V004

N

 

29

Valor do Diferimento do IBS de competência da UF

VLR\_DIF\_IBS\_UF

Informar o valor do Diferimento do IBS da competência da UF\.

015V002

N

 

30

Valor do tributo devolvido do IBS de competência da UF

VLR\_TRIB\_DEVOLVIDO\_IBS\_UF

Informar o valor do tributo devolvido \(desconto na própria Nota Fiscal / Fatura\), do IBS da competência da UF\.

015V002

N

 

31

Percentual da redução de alíquota do IBS de competência da UF

PERC\_RED\_ALIQ\_IBS\_UF

Informar o percentual da redução de alíquota do IBS da competência da UF\.

003V004

N

 

32

Alíquota do IBS de competência das UF

ALIQ\_IBS\_UF

Informar a alíquota do IBS de competência das UF\. Alíquota vigente do IBS da UF

003V004

N

 

33

Alíquota da CBS

ALIQ\_TRIB\_REG\_CBS

Informar a alíquota da CBS\. Alíquota vigente da CBS

003V004

N

 

34

Código de Situação Tributária do IBS e CBS \- tributação regular

CST\_TRIB\_REG\_IBS\_CBS

Informar o código de Situação Tributária do IBS e CBS, informado como seria caso não cumprida a condição resolutória/suspensiva\. Utilizar tabela CÓDIGO DE CLASSIFICAÇÃO TRIBUTÁRIA DO IBS E DA CBS\. \- tributação regular  
  
Validação:  
O código deve estar previamente cadastrado na TACES115\- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária

003

N

 

35

Código de Classificação Tributária do IBS e CBS \- tributação regular

CCLASS\_TRIB\_REG\_IBS\_CBS

Informar o código de Classificação Tributária do IBS e CBS, informado como seria caso não cumprida a condição resolutória/suspensiva\. Utilizar tabela CÓDIGO DE CLASSIFICAÇÃO TRIBUTÁRIA DO IBS E DA CBS\.\- tributação regular  
  
Validação:  
O código deve estar previamente cadastrado na tabela TACES116 \- Tabela de Classificação Tributária do IBS e da CBS \- Reforma Tributária 

006

N

 

36

Valor da alíquota do IBS da UF \- tributação regular

ALIQ\_TRIB\_REG\_IBS\_UF

Informar o valor da alíquota do IBS da UF\. \- tributação regular

003V004

N

 

37

Valor do Tributo do IBS da UF \- tributação regular

VLR\_TRIB\_REG\_TRIB\_IBS\_UF

Informar o valor do Tributo do IBS da UF\.\- tributação regular

015V002

N

 

38

Alíquota específica por unidade de medida apropriada do Imposto Seletivo

ALIQ\_ESPEC\_UNID\_MED\_APR\_IS

Informar a alíquota específica por unidade de medida apropriada do Imposto Seletivo\.

003V004

N

 

39

Valor do Imposto Seletivo

VLR\_IS

Informar o valor do Imposto Seletivo\.

015V002

N

 

40

Alíquota da CBS

ALIQ\_TRIB\_REG\_CBS

Informar a alíquota da CBS\. Alíquota vigente da CBS

003V004

N

 

41

Valor da CBS

VLR\_TRIB\_REG\_CBS

Informar o valor da CBS\.

015V002

N

 

42

Código de Classificação do Crédito Presumido do IBS

CCLASS\_CRED\_PRES\_IBS

Informar o código de Classificação do Crédito Presumido do IBS\. Utilizar tabela cCredPres

002

N

 

43

Percentual do Crédito Presumido do IBS

PER\_CRED\_PRES\_IBS

Informar o percentual do Crédito Presumido do IBS\.

003V004

N

 

44

Valor do Crédito Presumido do IBS

VLR\_CRED\_PRES\_IBS

Informar o valor do Crédito Presumido do IBS\.

015V002

N

 

45

Valor do Crédito Presumido em condição suspensiva do IBS\.

VLR\_CRED\_PRES\_COND\_SUSP\_IBS

Informar o valor do Crédito Presumido em condição suspensiva\. Valor do Crédito Presumido Condição Suspensiva do IBS\. Preencher apenas para cClassCredPres com indicação de Condição Suspensiva\.

015V002

N

 

46

Código de Classificação do Crédito Presumido da CBS

CCLASS\_CRED\_PRES\_CBS

Informar o código de Classificação do Crédito Presumido da CBS\. Utilizar tabela cCredPres

002

N

 

47

Percentual do Crédito Presumido da CBS

PERC\_CRED\_PRES\_CBS

Informar o percentual do Crédito Presumido da CBS\.

003V004

N

 

48

Valor do Crédito Presumido da CBS

VLR\_CRED\_PRES\_CBS

Informar o valor do Crédito Presumido da CBS\.

015V002

N

 

49

Valor do Crédito Presumido em condição suspensiva da CBS\.

VLR\_CRED\_PRES\_COND\_SUSP\_CBS

Informar o valor do Crédito Presumido em condição suspensiva da CBS\. Valor do Crédito Presumido Condição Suspensiva\. Preencher apenas para cClassCredPres com indicação de Condição Suspensiva\.

015V002

N

 

50

Alíquota ad rem do IBS

ALIQ\_AD\_REM\_IBS

Informar a alíquota ad rem do IBS\.

003V004

N

 

51

Valor do IBS monofásico

VLR\_MONO\_IBS

Informar o valor do IBS monofásico\. O valor do imposto é obtido pela multiplicação da alíquota ad rem pela quantidade do produto conforme unidade de medida estabelecida na legislação\.

015V002

N

 

52

Alíquota ad rem do IBS sujeito a retenção

ALIQ\_AD\_REM\_RET\_IBS

Informar a alíquota ad rem do imposto sujeito a retenção\.

003V004

N

 

53

Valor do IBS monofásico sujeito a retenção 

VLR\_MONO\_RET\_IBS

Informar o valor do IBS monofásico sujeito a retenção\. Valor do IBS com retenção, a ser somado ao valor de IBS a ser recolhido\.

015V002

N

 

54

Alíqutoa ad rem da CBS

ALIQ\_AD\_REM\_CBS

Informar a alíquota ad rem da CBS\.

003V004

N

 

55

Valor da CBS monofásica

VLR\_MONO\_CBS

Informar o valor da CBS monofásica\. O valor do imposto é obtido pela multiplicação da alíquota ad rem pela quantidade do produto conforme unidade de medida estabelecida na legislação\.

015V002

N

__Alterações da versão 1\.4 __\[ADO\- 818668\] 

Campos 23, 30 e 36 – Alterado o texto de “Percentual da redução de Alíquota” para “Percentual da redução de Alíquota *do cClassTrib*”\. 

Campos 24 e 37 – Alterado o texto de “Alíquota efetiva do IBS/CBS  de competência das UF que será aplicada a base de cálculo” para “ Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo*, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)”*

__Alterações da versão 1\.5__ \[ADO\- 837947\]

Sem reflexos\. Ajuste na regra de validação G134 \- Município do Emitente diverge da UF\. 

__Alterações da versão 1\.5a__ \[ADO\-843670 | 842052\] 

Inclusão dos campos 49 a 54 – Acrescentadas as colunas com os campos para atender às Compras Governamentais\. 

## <a id="_Dashboard_–_Visão"></a><a id="_Toc202363496"></a>Regras dos Campos \- SAFX3043 | Itens de Documentos Fiscais de Utilities

__Cód\.__

__Descrição__

__OS__

RN00

Regras Gerais

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

RN01 a 09

Replica dos campos chaves para as SAFX43 \- Itens de Documentos Fiscais de Utilities Os campos deverão ser criados para  a nova SAFX com a mesma especificação da tabela SAFX43, considerando apenas a lista de campos no item 4\.3\. 

RN10

Campo 10 \- CST\_IS

__Regra__

Campo NT: CST \- Código da Classificação Tributária do IBS/CBS\. 

Preencher conforme o cadastro da tabela e deverá representar a operação para validação dos campos de valores\. 

Campo criado para atender ao campo CST dos grupos CST, CSTReg e cCredPres da NFCOM nas situações que o CST for classificado e houver operações de condição regulatória, suspensão ou crédito presumido\. 

O código deverá estar previamente cadastrado conforme a TACES : __TACES115__ \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\.

Para relacionar os códigos CST x Códigos de Situação tributária, carregar a __TACES117__ \- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária\.   


__Valores Válidos: __Numérico – 3 dígitos  conforme  a tabela publicada pela Nota técnica 2025\.001\-RTC v1\.05a\.   
__Críticas__

 __Observação: __

RN11

Campo 11 \- CCLASS\_IS

__Regra__

Campo NT: CST –  Código da Classificação Tributária do IBS/CBS\. 

Preencher conforme o cadastro da tabela e deverá representar a operação para validação dos campos de valores\. 

Campo criado para atender ao campo cClassTrib  dos grupos CST, CSTReg e cCredPres da NFCOM nas situações que o CST for classificado e houver operações de condição regulatória, suspensão ou crédito presumido\. 

O código deverá estar previamente cadastrado conforme a TACES : __TACES115__ \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\.

Para relacionar os códigos CST x Códigos de Situação tributária, carregar a __TACES117__ \- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária\.   
__Valores Válidos: __Numérico – 6 dígitos  conforme  a tabela publicada pela Nota técnica 2025\.001\-RTC v1\.05a\.  
__Críticas__

__Observação: __

RN12

Campo 12 \- BC\_IS

__Regra__

Campo NT: vBC – Valor da Base de cálculo comum a IBS/CBS\. 

Valor da Base de Cálculo do Imposto Seletivo\. 

 __Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

__Observação: __

RN13

Campo 13 \- ALIQ\_IBS\_UF

__Regra__

Campo NT: pIBSUF \- Alíquota do IBS Estadual\. 

 Alíquota do IBS de competência das UF\.   
__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

__Observação: __

RN14

Campo 14 \- PERC\_DIF\_IBS\_UF

__Regra__

Campo NT: pDif \(grupo gDif\) \- Percentual de diferimento\. 

Percentual do diferimento do IBS de competência da UF\.   
__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

__Observação: __

RN15

Campo 15 \- VLR\_DIF\_IBS\_UF

__Regra__

Campo NT: vDif \(grupo gDif\) \- Valor do diferimento\.

Valor do Diferimento do IBS de competência da UF\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

__Observação: __

RN16

Campo 16 \- VLR\_TRIB\_DEVOLVIDO\_IBS\_UF

__Regra__

Campo NT: vDevTrib \(grupo gDevTrib\) \- Valor do tributo devolvido\.

Valor do tributo devolvido do IBS de competência da UF\.  
__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

__Observação: __

RN17

Campo 17 \- PERC\_RED\_ALIQ\_IBS\_UF

__Regra__

Campo NT: pRedAliq \(grupo gRed\) \- Percentual da redução de Alíquota do cClassTrib\.

Percentual da redução de alíquota do IBS de competência da UF\.  
__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

__Observação: __

RN18

Campo 18 \- ALIQ\_IBS\_UF

__Regra__

Campo NT: pAliqEfet \(grupo gRed\) \- Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\.

Alíquota do IBS de competência das UF

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

__Observação: __

RN19

Campo 19 \- VLR\_IBS\_UF

__Regra__

Campo NT: vIBSUF \- Valor do IBS de competência da UF\. 

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

__Observação: __

RN20

Campo 20 \- ALIQ\_IBS\_MUN

__Regra__

Campo NT: pIBSMun \(grupo gIBSMun\) \- Alíquota do IBS Municipal\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\. 

__Críticas__

__Observação: __

RN21

Campo 21 \- PERC\_DIF\_IBS\_MUN

__Regra__

Campo NT: pDif \(grupo gIBSMun\) \- Percentual de diferimento\.

Percentual de diferimento  do IBS Municipal\. 

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN22

Campo 22 \- VLR\_DIF\_IBS\_MUN

__Regra__

Campo NT: vDif \(grupo gIBSMun\) \- Valor do diferimento\.

Valor do diferimento  do IBS Municipal\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

__Observação: __

RN23

Campo 23 \- VLR\_TRIB\_DEVOLVIDO\_IBS\_MUN

__Regra__

Campo NT: vDevTrib \(grupo gIBSMun\) \- Valor do tributo devolvido\.

Valor do tributo devolvido  do IBS Municipal\. 

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

__Observação: __

RN24

Campo 24 \- PERC\_RED\_ALIQ\_IBS\_MUN

__Regra__

Campo NT: pRedAliq \(grupo gIBSMun\) \- Percentual da redução de Alíquota do cClassTrib\.

Percentual da redução de Alíquota  do IBS Municipal\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN25

Campo 25 \- ALIQ\_EFET\_IBS\_MUN

__Regra__

Campo NT: pAliqEfet \(grupo gIBSMun\) \- Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. 

Alíquota Efetiva do IBS de competência dos Municípios que será aplicada a Base de Cálculo\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN26

Campo 26 \- VLR\_IBS\_MUN

__Regra__

Campo NT: vIBSMun \(grupo gIBSMun\) \- Valor do IBS de competência do município\.

Valor do IBS de competência do Município\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\. 

__Críticas__

__Observação: __

RN27

Campo 27 \- ALIQ\_TRIB\_REG\_CBS

__Regra__

Campo NT: pCBS  \(grupo gIBSMun\) \- Alíquota da CBS\. 

Alíquota da CBS\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN28

Campo 28 \- PERC\_DIF\_IBS\_UF

__Regra__

Campo NT: pDif grupo gIBSMun\) \- Percentual de diferimento\. 

Percentual de diferimento\. 

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN29

Campo 29 \- VLR\_DIF\_IBS\_UF 

__Regra__

Campo NT: vDif grupo gIBSMun\) \- Valor do diferimento\.

Valor do diferimento\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN30

Campo 30 \- VLR\_TRIB\_DEVOLVIDO\_IBS\_UF

__Regra__

Campo NT: vDevTrib \(grupo gDevTrib\) \- Valor da CBS devolvida\.

Valor da CBS devolvida\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN31

Campo 31 \- PERC\_RED\_ALIQ\_IBS\_UF

__Regra__

Campo NT: pRedAliq \(grupo gDevTrib\) \- Percentual da redução de Alíquota do cClassTrib\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN32

Campo 32 \- ALIQ\_IBS\_UF

__Regra__

Campo NT: pAliqEfet \(grupo gDevTrib\) \- Alíquota efetiva da CBS que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN33

Campo 33 \- VLR\_TRIB\_REG\_CBS

__Regra__

Campo NT: vCBS \(grupo gDevTrib\) – Valor da CBS\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN34

Campo 34 \- CST\_TRIB\_REG\_IBS\_CBS

__Regra__

Campo NT: CSTReg \-  Código da Situação Tributária Informado como seria o CST caso não cumprida a __condição resolutória/suspensiva__\. 

Preencher conforme o cadastro da tabela e deverá representar a operação para validação dos campos de valores\. 

Campo criado para atender ao campo cClassTrib  dos grupos CST, CSTReg e cCredPres da NFCOM nas situações que o CST for classificado e houver operações de condição regulatória, suspensão ou crédito presumido\. 

O código deverá estar previamente cadastrado conforme a TACES : __TACES115__ \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\.

Para relacionar os códigos CST x Códigos de Situação tributária, carregar a __TACES117__ \- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária\.

__Valores Válidos: __Numérico com 3 posições\.

__Críticas__

__Observação: __

RN35

Campo 35 \- CCLASS\_TRIB\_REG\_IBS\_CBS

__Regra__

Campo NT: cClassTribReg \- Código de Classificação Tributária Informado como seria o cClassTrib caso não cumprida a __condição resolutória/suspensiva__\. 

Preencher conforme o cadastro da tabela e deverá representar a operação para validação dos campos de valores\. 

Campo criado para atender ao campo cClassTrib  dos grupos CST, CSTReg e cCredPres da NFCOM nas situações que o CST for classificado e houver operações de condição regulatória, suspensão ou crédito presumido\. 

O código deverá estar previamente cadastrado conforme a TACES : __TACES115__ \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária\.

Para relacionar os códigos CST x Códigos de Situação tributária, carregar a __TACES117__ \- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \- Reforma Tributária\.

__Valores Válidos: __Numérico com 6 posições\. 

__Críticas__

__Observação: __

RN36

Campo 36 \- ALIQ\_TRIB\_REG\_IBS\_UF

__Regra__

Campo NT: pAliqEfetRegIBSUF \- Alíquota efetiva da UF Informado a Alíquota caso não cumprida a __condição resolutória/suspensiva__\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN37

Campo 37 \- VLR\_TRIB\_REG\_TRIB\_IBS\_UF

__Regra__

Campo NT: vTribRegIBSUF \- Informado como seria o valor do Tributo da UF caso não cumprida a __condição resolutória/suspensiva__\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN38

Campo 38 \- ALIQ\_ESPEC\_UNID\_MED\_APR\_IS

__Regra__

Campo NT: pAliqEfetRegIBSMun \- Alíquota efetiva do Município Informado a Alíquota caso não cumprida a __condição resolutória/suspensiva__\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN39

Campo 39 \- VLR\_IS

__Regra__

Campo NT: vTribRegIBSMun \- Informado como seria o valor do Tributo do Município caso não cumprida a condição resolutória/suspensiva\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN40

Campo 40 \- ALIQ\_TRIB\_REG\_CBS

__Regra__

Campo NT: pAliqEfetRegCBS \- Alíquota efetiva da CBS Informado a Alíquota caso não cumprida a __condição resolutória/suspensiva__\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN41

Campo 41 \- VLR\_TRIB\_REG\_CBS

__Regra__

Campo NT: vTribRegICBS \- Informado como seria o valor do Tributo CBS caso não cumprida a __condição resolutória/suspensiva__\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN42

Campo 42 \- CCLASS\_CRED\_PRES\_IBS

__Regra__

Campo NT: cCredPres \- Código do Crédito Presumido \(ver Tabela\)\. 

__Valores Válidos: __Numérico com 2 posições\. 

__Críticas__

__Observação: __

RN43

Campo 43 \- PER\_CRED\_PRES\_IBS

__Regra__

Campo NT: pCredPres – Percentual\.

Percentual de crédito presumido\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN44

Campo 44 \- VLR\_CRED\_PRES\_IBS

__Regra__

Campo NT: vCredPres \- Valor do crédito presumido\. 

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN45

Campo 45 \- VLR\_CRED\_PRES\_COND\_SUSP\_IBS

__Regra__

Campo NT: vCredPresCondSus \- Valor do Crédito Presumido Condição Suspensiva\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN46

Campo 46 \- CCLASS\_CRED\_PRES\_IBS

__Regra__

Campo NT: cCredPres \- Código do Crédito Presumido \(ver Tabela\)

__Valores Válidos: __Numérico com 2 posições

__Críticas__

__Observação: __

RN47

Campo 47 \- PER\_CRED\_PRES\_IBS

__Regra__

Campo NT: pCredPres \- Percentual de crédito presumido\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN48

Campo 48 \- VLR\_CRED\_PRES\_IBS

__Regra__

Campo NT: vCredPres \- Valor do crédito presumido\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN49 

Campo 49 \- VLR\_CRED\_PRES\_COND\_SUSP\_IBS

__Regra__

Campo NT: vCredPresCondSus \- Valor do Crédito Presumido Condição Suspensiva\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN50

Campo 50 \- ALIQ\_AD\_REM\_IBS

__Regra__

Campo NT: pAliqIBSUF \- Alíquota IBS da UF utilizada nas compras governamentais\. 

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN51

Campo 51 \- VLR\_MONO\_IBS

__Regra__

Campo NT: vTribIBSUF \- Valor do Tributo do IBS da UF Valor que seria devido a UF nas __compras governamentais__, sem aplicação do Art\. 473\. da LC 214/20025

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN52

Campo 52 \- ALIQ\_AD\_REM\_RET\_IBS

__Regra__

Campo NT: pAliqIBSMun \- Alíquota IBS do Município utilizada nas compras governamentais\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN53

Campo 53 \- VLR\_MONO\_RET\_IBS

__Regra__

Campo NT: vTribIBSMun \- Valor do Tributo do Município da UF Valor que seria devido ao Município nas compras governamentais, sem aplicação do Art\. 473\. da LC 214/20025\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

RN54

Campo 54 \- ALIQ\_AD\_REM\_CBS

__Regra__

Campo NT: pAliqCBS \- Alíquota IBS do CBS utilizada nas compras governamentais\.

__Valores Válidos: __Numérico com 3 posições e 4 casas decimais \(3,4\)\.

__Críticas__

__Observação: __

RN55

Campo 55 \- VLR\_MONO\_CBS

__Regra__

Campo NT: vTribCBS \- Valor do Tributo da CBS Valor que seria devido a CBS nas compras governamentais, sem aplicação do Art\. 473\. da LC 214/20025\.

__Valores Válidos: __Numérico com 15 posições e 2 casas decimais \(15,2\)\.

__Críticas__

__Observação: __

As informaçõs de entrada serão suportadas pelos arquivos SAFX3007RT e SAFX2008RT conforme os campos dsiponíveis em sua documentação\. 

