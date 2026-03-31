# MTZ_RT_CTE_Mod 57 e 67 - SAFX3007 e SAFX3008

- **Fonte:** MTZ_RT_CTE_Mod 57 e 67 - SAFX3007 e SAFX3008.docx
- **Modificado:** 2026-02-16
- **Tamanho:** 92 KB

---

THOMSON REUTERS

Reforma Tributária

Conhecimento de Transporte Eletrônico, modelo 57 e 67\. 

ONESOURCE Tax One

SAFX3007 – Arquivo de Notas Fiscais

SAFX3008 \- Itens Notas Fiscais Mercadorias e Produtos

Sumário

[1\.	CONTROLE DE ALTERAÇÕES	3](#_Toc202364857)

[2\.	INTRODUÇÃO	4](#_Toc202364858)

[3\.	DOCUMENTOS DE REFERÊNCIA	4](#_Toc202364859)

[4\.	DEFINIÇÃO DAS REGRAS	5](#_Toc202364860)

[4\.1\.	CTE – Regra de Negócio \-SAFX3007 \[Em avaliação\]	6](#_Toc202364861)

[4\.2\.	CTE – Regra de negócio  – SAFX3008	6](#_Toc202364862)

[4\.4\.	CTE – SAFX3007 e SAFX3008  – Regra para os campos	11](#_Toc202364863)

# <a id="_Toc462320891"></a><a id="_Toc202364857"></a>CONTROLE DE ALTERAÇÕES

__Data__

__Demanda__

__Descrição__

__Autor__

18/06/2025

[ADO\-843670](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/843670)

Atualização NT2025\_001\_RTC\_v1\.05a

Érika Borges

# <a id="_Toc462320892"></a><a id="_Toc202364858"></a>INTRODUÇÃO

V1 \- O objetivo desse documento é descrever a estrutura de campos das tabelas SAFX para o repositório das informações da RT \(IBS e CBS\) para os processos do CTE – Conhecimento de Transporte Eletrônico \(modelos 57 e 5=67\) com base na versão da CTe\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05ª\. 

V1 \- Atualização versão 1\.5a da NT \(correção dos campos no layout\)\.

V1 – Acrescentados os campos para atender do grupo gCompraGov referente ao processo de Compras Governamentais\.

# <a id="_Toc202364859"></a>DOCUMENTOS DE REFERÊNCIA

V1 – [T1\_RT \- NFCom Requisitos de negocios\_v1\.docx](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Reforma_Tributaria/NFCOM%20e%20CTE/T1_RT%20-%20NFCom%20Requisitos%20de%20negocios_v1.docx?d=wd50fab2b4f39430981a7bc906f9cb65e&csf=1&web=1&e=lT0QNJ)

V1 \- [Manual\_Layout\_MastersafDW\.xls](https://trten.sharepoint.com/:x:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Manuais-de-layout/Layout%20SAFX/Manual_Layout_MastersafDW.xls?d=we422f97384284e35897a6622693cca04&csf=1&web=1&e=nfPEBB) \- Layout dos Arquivo Mastersaf DW e ONESOURCE Tax One | Patch 306\.1\.1 \(SAFX08 e SAFX43\)

V1 \- [Nota Técnica RTC\_v1\.05a](C://Users/6132884/Downloads/NFCom_Nota_Tecnica_2025_001_RTC_v1.05a.pdf) incluir os novos campos referente às Compras Governamentais\. 

 

# <a id="_Toc202364860"></a>DEFINIÇÃO DAS REGRAS

No contexto da Reforma tributária, o repositório de dados fiscais do Tax One terá sua estrutura atualizada para suportar os novos impostos com base na versão da publicação na presente data\. Nesse documento abordaremos a proposta de solução para os processos fiscais do Conhecimento de Transporte Eletrônico __Modelo 57 e 67__  com base na versão CTe\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a e suas alterações, que serão suportados pela estrutura nova estrutura de arquivos:

- SAFX3007 – Arquivo de Notas Fiscais
- SAFX3008 \- Itens Notas Fiscais Mercadorias e Produtos
- SAFX3050 \- Arquivo Relacional de Transportadora
- SAFX3051 \- Arquivo de Itens de Conhecimento de Fretes

## <a id="_Toc202364861"></a>CTE – Regra de Negócio \-SAFX3007 \[Em avaliação\]

A nova estrutura dos arquivos SAFX3007 para o CTE será contemplada em documentação dessas tabelas\. 

Os campos definidos pela CTe\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a para a emissão do Modelo 57 e 67 são: 

Origem

PK

Obg\.

Nr

Nome do campo

Campo

Comentário

Tam

Tipo

vTar

 

 

115

Valor da tarifa

VLR\_TARIFA\_DUTO

Valor da tarifa \- Modal Dutoviário

9V6

C

dIni

 

 

116

Data de Início da prestação do serviço

DATA\_INICIO\_SERVICO\_DUTO

Data de Início da prestação do serviço do Modal Dutoviário

10

D

dFim

 

 

117

Data de Fim da prestação do serviço

DATA\_FIM\_SERVICO\_DUTO

Data de Fim da prestação do serviço Modal Dutoviário

10

D

classDuto

 

 

118

Classificação Dutoviário

COD\_CLASS\_DUTO

Classificação Dutoviário\. Informar:  
1 – Gasoduto;  
2 – Mineroduto ou  
3 \- Oleoduto

1

N

tpContratacao

 

 

119

Tipo de contratação do serviço de  
transporte \(apenas para gasoduto\)

TP\_CONTRATACAO\_DUTO

Tipo de contratação do serviço de transporte \(apenas para gasoduto\)\. Informar:  
0 – Ponto a ponto  
1 – Capacidade de Entrada ou  
2 – Capacidade de Saída

1

N

codPontoEntrada

 

 

120

Código do Ponto de Entrada

COD\_PONTO\_ENTRADA\_DUTO

Código do Ponto de Entrada do Modal Dutoviário

20

C

codPontoSaida

 

 

121

Código do Ponto de Saída

COD\_PONTO\_SAIDA\_DUTO

Código do Ponto de Saída do Modal Dutoviário

20

C

nContrato

 

 

122

Número do Contrato de Capacidade

NRO\_CONTRATO\_DUTO

Número do Contrato de Capacidade do Modal Dutoviário

20

C

## <a id="_Dashboard_–_Visão_1"></a><a id="_Toc202364862"></a>CTE – Regra de negócio  – SAFX3008

A nova estrutura dos arquivos SAFX3007 e SAFX3008 para o CTE será contemplada em documentação dessas tabelas\. 

Os campos definidos pela CTe\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05ª para a emissão do Modelo 57 e 67 são: 

__\#__

__Campo__

__Ele__

__Pai__

__Tipo__

__Ocor\.__

__Tam\.__

__Descrição/Observação__

__Campo2__

__Tabela__

\#

IBSCBS

G

imposto

\-

0\-1

\-

Grupo de informações da Tributação IBS/CBS

 

 

1

CST

E

IBSCBS

N

1\-1

3

Código da Situação Tributária do IBS/CBS

CST\_IS

SAFX3008

2

cClassTrib

E

IBSCBS

N

1\-1

6

Código da Classificação Tributária do IBS/CBS

CCLASS\_IS

SAFX3008

3

gIBSCBS

G

IBSCBS

\-

0\-1

\-

Grupo de informações específicas do IBS/CBS

 

SAFX3008

4

vBC

E

gIBSCBS

N

1\-1

13,2

Valor da Base de cálculo comum a IBS/CBS

BC\_IS

SAFX3008

5

gIBSUF

G

gIBSCBS

\-

1\-1

\-

Grupo de informações do IBS/CBS de competência  
das Unidades Federadas

 

SAFX3008

6

pIBSUF

E

gIBSUF

N

1\-1

3,2/3,4

Alíquota do IBS Estadual

ALIQ\_IBS\_UF

SAFX3008

7

gDif

G

gIBSUF

\-

0\-1

\-

Grupo de campos do diferimento

 

SAFX3008

8

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

PERC\_DIF\_IBS\_UF

SAFX3008

9

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

VLR\_DIF\_IBS\_UF

SAFX3008

10

gDevTrib

G

gIBSUF

\-

0\-1

\-

Grupo de informações da devolução de tributos

 

SAFX3008

11

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor do tributo devolvido\.  
No fornecimento de energia elétrica, água, esgoto e  
gás natural e em outras hipóteses definidas no  
regulamento

VLR\_TRIB\_DEVOLVIDO\_IBS\_UF

SAFX3008

12

gRed

G

gIBSUF

\-

0\-1

\-

Grupo de informações da redução de Alíquota

 

SAFX3008

13

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

PERC\_RED\_ALIQ\_IBS\_UF

SAFX3008

14

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

ALIQ\_IBS\_UF

SAFX3008

15

vIBSUF

E

gIBSUF

N

1\-1

13,2

Valor do IBS de competência da UF

VLR\_IBS\_UF

SAFX3008

16

gIBSMun

G

gIBSCBS

\-

1\-1

\-

Grupo de informações do IBS/CBS de competência  
do municipio

 

SAFX3008

17

pIBSMun

E

gIBSMun

N

1\-1

3,2/3,4

Alíquota do IBS Municipal

 

SAFX3008

18

gDif

G

gIBSMun

\-

0\-1

\-

Grupo de campos do diferimento

 

SAFX3008

19

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

PERC\_DIF\_IBS\_UF

SAFX3008

20

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

VLR\_DIF\_IBS\_UF

SAFX3008

21

gDevTrib

G

gIBSMun

\-

0\-1

\-

Grupo de informações da devolução do tributo

 

SAFX3008

22

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor do tributo devolvido\. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento

VLR\_TRIB\_DEVOLVIDO\_IBS\_UF

SAFX3008

23

gRed

G

gIBSMun

\-

0\-1

\-

Grupo de informações da redução de Alíquota

 

SAFX3008

24

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

PERC\_RED\_ALIQ\_IBS\_UF

SAFX3008

25

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

ALIQ\_EFET\_IBS\_UF

SAFX3008

26

vIBSMun

E

gIBSMun

N

1\-1

13,2

Valor do IBS de competência do município

ALIQ\_TRIB\_REG\_CBS

SAFX3008

27

gCBS

G

gIBSCBS

\-

1\-1

\-

Grupo de informações da CBS

 

SAFX3008

28

pCBS

E

gCBS

N

1\-1

3,2/3,4

Alíquota da CBS

VLR\_TRIB\_REG\_CBS

SAFX3008

29

gDif

G

gCBS

\-

0\-1

\-

Grupo de campos do diferimento

 

SAFX3008

30

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

PERC\_DIF\_TRIB\_REG\_CBS

SAFX3008

31

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

VLR\_DIF\_TRIB\_REG\_CBS

SAFX3008

32

gDevTrib

G

gCBS

\-

0\-1

\-

Grupo de informações da devolução do tributo

 

SAFX3008

33

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor da CBS devolvida\. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento

VLR\_TRIB\_DEVOLVIDO\_TRIB\_REG\_CBS

SAFX3008

34

gRed

G

gCBS

\-

0\-1

\-

Grupo de informações da redução de Alíquota

 

SAFX3008

35

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

PERC\_RED\_ALIQ\_TRIB\_REG\_CBS

SAFX3008

36

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva da CBS que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

ALIQ\_EFET\_TRIB\_REG\_CBS

SAFX3008

37

vCBS

E

gCBS

N

1\-1

13,2

Valor da CBS

ALIQ\_TRIB\_REG\_CBS

SAFX3008

38

gTribRegular

G

gIBSCBS

\-

0\-1

\-

Grupo de informações da Tributação Regular\.  
Informar como seria a tributação caso não cumprida  
a condição resolutória/suspensiva\. Exemplo 1: Art\.  
442, §4\. Operações com ZFM e ALC\. Exemplo 2:  
Operações com suspensão do tributo\.\.

 

SAFX3008

39

CSTReg

E

gTribRegular

N

1\-1

3

Código da Situação Tributária  
Informado como seria o CST caso não cumprida a  
condição resolutória/suspensiva

CST\_TRIB\_REG\_IBS\_CBS

SAFX3008

40

cClassTribReg

E

gTribRegular

N

1\-1

6

Código de Classificação Tributária  
Informado como seria o cClassTrib caso não  
cumprida a condição resolutória/suspensiva

CCLASS\_TRIB\_REG\_IBS\_CBS

SAFX3008

41

pAliqEfetRegIBSUF

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva da UF  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

ALIQ\_TRIB\_REG\_IBS\_UF

SAFX3008

42

vTribRegIBSUF

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo da UF caso  
não cumprida a condição resolutória/suspensiva

VLR\_TRIB\_REG\_TRIB\_IBS\_UF

SAFX3008

43

pAliqEfetRegIBSMun

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva do Município  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

ALIQ\_ESPEC\_UNID\_MED\_APR\_IS

SAFX3008

44

vTribRegIBSMun

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo do  
Município caso não cumprida a condição  
resolutória/suspensiva

VLR\_IS

SAFX3008

45

pAliqEfetRegCBS

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva da CBS  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

ALIQ\_TRIB\_REG\_CBS

SAFX3008

46

vTribRegCBS

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo CBS caso  
não cumprida a condição resolutória/suspensiva

VLR\_TRIB\_REG\_TRIB\_CBS

SAFX3008

47

gIBSCredPres

G

gIBSCBS

\-

0\-1

\-

Grupo de Informações do Crédito Presumido,  
quando aproveitado pelo emitente do documento\.

 

SAFX3008

48

cCredPres

E

gIBSCredPres

N

1\-1

 

Código do Crédito Presumido \(ver Tabela\)

CCLASS\_CRED\_PRES\_IBS

SAFX3008

49

pCredPres

E

gIBSCredPres

N

1\-1

3,2/3,4

Percentual

PER\_CRED\_PRES\_IBS

SAFX3008

50

vCredPres

CE

gIBSCredPres

N

1\-1

13,2

Valor do crédito presumido

VLR\_CRED\_PRES\_IBS

SAFX3008

51

vCredPresCondSus

CE

gIBSCredPres

N

1\-1

13,2

Valor do Crédito Presumido Condição Suspensiva Preencher apenas para cCredPres com indicação de Condição Suspensiva

VLR\_CRED\_PRES\_COND\_SUSP\_IBS

SAFX3008

52

gCBSCredPres

G

gIBSCBS

\-

0\-1

\-

Grupo de Informações do Crédito Presumido,  
quando aproveitado pelo emitente do documento\.

 

SAFX3008

53

cCredPres

E

gCBSCredPres

N

1\-1

 

Código do Crédito Presumido \(ver Tabela\)

CCLASS\_CRED\_PRES\_CBS

SAFX3008

54

pCredPres

E

gCBSCredPres

N

1\-1

3,2/3,4

Percentual

PERC\_CRED\_PRES\_CBS

SAFX3008

55

vCredPres

CE

gCBSCredPres

N

1\-1

13,2

Valor do crédito presumido

VLR\_CRED\_PRES\_CBS

SAFX3008

56

vCredPresCondSus

CE

gCBSCredPres

N

1\-1

13,2

Valor do Crédito Presumido Condição Suspensiva Preencher apenas para cCredPres com indicação de Condição Suspensiva

VLR\_CRED\_PRES\_COND\_SUSP\_CBS

SAFX3008

57

gTribCompraGov

G

gIBSCBS

\-

0\-1

\-

Grupo de informações da composição do valor do IBS e da CBS em compras governamenta

 

SAFX3008

58

pAliqIBSUF

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota IBS da UF utilizada

ALIQ\_AD\_REM\_IBS

SAFX3008

59

vTribBSUF

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo do IBS da UF Valor que seria devido a UF, sem aplicação do Art\. 473\. da LC 214/20025

VLR\_MONO\_IBS

SAFX3008

60

pAliqIBSMun

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota IBS do Município utilizada

ALIQ\_AD\_REM\_RET\_IBS

SAFX3008

61

vTribIBSMun

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo do Município da UF Valor que seria devido ao Município, sem aplicação do Art\. 473\. da LC 214/20025

VLR\_MONO\_RET\_IBS

SAFX3008

62

pAliqCBS

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota do CBS utilizada

ALIQ\_AD\_REM\_CBS

SAFX3008

63

vTribCBS

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo da CBS Valor que seria devido a CBS, sem aplicação do Art\. 473\. da LC 214/20025

VLR\_MONO\_CBS

SAFX3008

__Alterações da versão 1\.4 __\[ADO\- 818668\] 

Campos 23, 30 e 36 – Alterado o texto de “Percentual da redução de Alíquota” para “Percentual da redução de Alíquota *do cClassTrib*”\. 

Campos 24 e 37 – Alterado o texto de “Alíquota efetiva do IBS/CBS  de competência das UF que será aplicada a base de cálculo” para “ Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo*, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)”*

__Alterações da versão 1\.5__ \[ADO\- 837947\]

Sem reflexos\. Ajuste na regra de validação G134 \- Município do Emitente diverge da UF\. 

__Alterações da versão 1\.5a__ \[ADO\-843670 | 842052\] 

Inclusão dos campos 49 a 54 – Acrescentadas as colunas com os campos para atender às Compras Governamentais\. 

## <a id="_Toc202364863"></a>CTE – SAFX3007 e SAFX3008  – Regra para os campos

SAFX3007 \- As regras para a criação dos campos referente a TAG __DUTO__ das informações do __Modal Dutoviário__ constam na documentação da SAFX3007\.

SAFX3008 – As regras para criação dos campos referente a TAG IBSCBS das informações impostos constam na documentação própria\.

<a id="_Dashboard_–_Detalhamento"></a><a id="_Toc466277417"></a><a id="_Toc466277749"></a><a id="_Toc466277881"></a><a id="_Toc466277931"></a><a id="_Toc466541683"></a><a id="_Toc466541785"></a><a id="_Toc466542263"></a><a id="_Toc467246123"></a><a id="_Toc467246221"></a><a id="_Toc467577858"></a>

