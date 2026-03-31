# MTZ_IPI_Lancamentos_Automaticos_IPI_P8

- **Fonte:** MTZ_IPI_Lancamentos_Automaticos_IPI_P8.docx
- **Modificado:** 2025-08-26
- **Tamanho:** 111 KB

---

THOMSON REUTERS

Módulo IPI

Processamento Lançamentos Automáticos IPI

__Localização__: Menu Federal, módulo IPI, menu Apuração IPI à Apuração do IPI à Geração da Apuração 

Menu Federal, módulo IPI, DATA MART à Apuração do IPI

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data__

MFS\-433282

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a>Alessandra Cristina Navatta

<a id="OLE_LINK15"></a><a id="OLE_LINK19"></a>Criação do Documento\.

Estas informações serão utilizadas na geração do Sped Fiscal, registros E530 e E531\. 

19/06/2023

MFS\-617413

Alessandra Cristina Navatta

Detalhamento das regras para a deleção dos lançamentos no processamento/reprocessamento

11/03/2024

Sumário

[1\.	Objetivo e Start do Processo	3](#_Toc155274635)

[2\.	Recuperação dos Dados e Cálculo dos Lançamentos	3](#_Toc155274636)

[3\.	Consolidação das informações:	4](#_Toc155274637)

[4\.	Critérios e Prioridade da Parametrização:	4](#_Toc155274638)

[5\.	Gravação dos Dados	5](#_Toc155274639)

[6\.	Gravação dos Lançamentos na ITEM\_APURAC\_DISCR e ITEM\_APURAC\_DISCR\_AJUSTE	5](#_Toc155274640)

[7\.	Detalhamento da Gravação dos Lançamentos na ITEM\_APURAC\_DISCR	7](#_Toc155274641)

[8\.	Detalhamento da Gravação dos Lançamentos na ITEM\_APURAC\_DISCR\_AJUSTE	9](#_Toc155274642)

[9\.	Reprocessamento das Informações e Sinalização dos Lançamentos como ‘Lançamentos Automáticos’\.	11](#_Toc155274643)

# <a id="_Toc155274635"></a><a id="_Toc350763252"></a>Objetivo e Start do Processo

A rotina criada será chamada no módulo IPI, nas telas de Geração de Apuração \(menu Apuração do IPI\) e/ou ‘Apuração IPI’ \(menu DATA MART\)\. 

No momento da geração, será verificada a existência de parametrizações da apuração e configuração de pelo menos um critério definido, nas telas do Menu Parâmetros > Lançamentos Automáticos, dentro do menu Parâmetros, para o estabelecimento que está efetuando a geração da apuração\.  O sistema recuperará as notas fiscais que atendam os critérios estabelecidos nestas telas e criará um lançamento automático \(de acordo com as regras detalhadas nos demais tópicos deste documento\) gravando as informações na __FDT\_LANCTO\_P8 e FDT\_LANCTO\_P8\_NF__, no menu “Geração da Apuração” , e ‘Apuração IPI’,  e na tela de lançamentos complementares da Apuração do IPI __\(tabelas ITEM\_APURAC\_DISCR e ITEM\_APURAC\_DISCR\_AJUSTE\)__ , sendo esta última, as informações dos documentos fiscais vinculados ao lançamento__, __já que os lançamentos automáticos são de origem exclusiva de documento fiscal\.

# <a id="_Toc155274636"></a>Recuperação dos Dados e Cálculo dos Lançamentos

Origem dos dados: 

- 
	- Documentos Fiscais \(SAFX07/SAFX08\);
	- Notas fiscais normais e de devolução \(campo NORM\_DEV = 1 e/ou 2\);
	- Itens de notas fiscais do estabelecimento em questão;
	- Itens de notas fiscais com data fiscal no período de geração do livro;
	- Itens de notas fiscais não canceladas;
	- Parametrizações definidas na tela “Parâmetros da Apuração”, no menu IPI > Parâmetros > Lançamentos Automáticos;
	- Pelo menos um critério \(Por CFOP, Por CFOP/ Natureza de Operação, Por NBM e/ou Por Produto\), definido no menu IPI > Parâmetros > Lançamentos Automáticos> Lançamentos Complementares;

Para cada estabelecimento é gerado um lançamento por código de ajuste do Sped, item de apuração e período de apuração\.

O valor do lançamento é calculado a partir do somatório dos campos indicado na tela “Parâmetros da Apuração” dentro do menu Lançamentos Automáticos, de todos os itens das notas fiscais que atendam às condições acima\. Valor totalizado pode ser o somatório de um ou mais valores listados abaixo:

- <a id="OLE_LINK26"></a>Valor IPI \(Campo 48 \- VLR\_IPI\)
- Valor de Estorno de IPI \(Campo 68 \- VLR\_OUTROS\_IPI\)
- IPI não Escriturado \(Campo 81 \- VLR\_IPI\_NDESTAC\)
- Valor Total do IPI Devolvido \(Campo 254 \- VLR\_IPI\_DEV\)

# <a id="_Toc155274637"></a>Consolidação das informações:

- Estabelecimento
- Código de Ajuste do Sped
- Item Apuração

# <a id="_Toc155274638"></a>Critérios e Prioridade da Parametrização:

Critérios, existente no menu IPI > Parâmetros > Lançamentos Automáticos > Lançamentos Complementares:

- Por CFOP
- Por CFOP/ Natureza de Operação
- Por NBM
- Por Produto

Caso um mesmo item de nota se enquadre em mais de uma parametrização, a ordem de prioridade \(de maior relevância, para a menor relevância\) das parametrizações é:

- Por Produto 
- Por NBM
- Por CFOP/ Natureza de Operação
- Por CFOP

# <a id="_Toc155274639"></a>Gravação dos Dados

Os valores dos lançamentos calculados para cada estabelecimento, serão armazenados na apuração do P8 \(tabela FDT\_LANCTO\_P8\) e as informações de identificação de todos os itens que originaram cada lançamento, ficarão armazenadas na tabela “filha” da FDT\_LANCTO\_P8\. Essas informações darão origem aos lançamentos complementares da tela de manutenção dos lançamentos complementares da Apuração do IPI \(tabela ITEM\_APURAC\_DISCR\) e aos documentos, listados no botão “*Documentos Fiscais Vinculados*”, \(tabela ITEM\_APURAC\_DISCR\_AJUSTE\)\. Tais informações serão utilizadas posteriormente na geração do Sped Fiscal, registro E530 \(lançamentos\) e E531\(documentos fiscais\)\.

# <a id="_Toc155274640"></a>Gravação dos Lançamentos na ITEM\_APURAC\_DISCR e ITEM\_APURAC\_DISCR\_AJUSTE

As informações dos lançamentos e dos itens serão gravadas nas tabelas, conforme:

	

- Dados da chave de identificação da tabela “mãe” \(ITEM\_APURAC\_DISCR\);
- Valor do Lançamento __\(\*\)__
- Dados da chave de identificação do item do documento fiscal da tabela “filha” \(ITEM\_APURAC\_DISCR\_AJUSTE\);
- Número do item do documento fiscal;
- Valor do ajuste corresponde ao item __\(\*\*\)__;

__\(\*\)__ O valor do lançamento correspondente ao somatório dos valores recuperados referente aos campos indicados na parametrização, já que estes valores são utilizados para compor o lançamento\. 

__\(\*\*\)__ O valor do documento correspondente a cada item será o somatório dos valores dos campos indicados na parametrização, já que estes valores são utilizados na totalização dos itens para compor o lançamento\. 

O lançamento a ser gravado na ITEM\_APURAC\_DISCR sempre terá __documentos fiscais vinculados informados na tabela “filha” da FDT\_LANCTO\_P8__, por isso, a coluna ORIGEM\_PROC será gravada da seguinte forma:

__ITEM\_APURAC\_DISCR__

__Conteúdo__

ORIGEM\_PROC

= __3__

\(indica lançamento originado de NF’s\)

Obs\.: Na tela dos lançamentos complementares da Apuração do IPI, os lançamentos que têm documentos fiscais vinculados devem ter o campo ORIGEM\_PROC = 3 \(na tela é o campo “Origem” do quadro “Documento Vinculado ao Ajuste”\)\. 

__Gravação dos documentos vinculados na ITEM\_APURAC\_DISCR\_AJUSTE:__

O processo de lançamentos automáticos, tem origem documentos fiscais, então, também devemos gravar de forma automática os documentos fiscais vinculados\. 

O preenchimento destas informações \(originadas da tabela “filha” da FDT\_LANCTO\_P8\) na tabela dos documentos fiscais vinculados do Livro de Apuração do IPI \(tabela __ITEM\_APURAC\_DISCR\_AJUSTE__\) é feito da seguinte forma:

__ITEM\_APURAC\_DISCR\_AJUSTE__

__Conteúdo__

__Origem Informação__

COD\_EMPRESA

Dados da chave do lançamento gravado na ITEM\_APURAC\_DISCR

ITEM\_APURAC\_DISCR

COD\_ESTAB

COD\_TIPO\_LIVRO

DAT\_APURACAO

COD\_OPER\_APUR

NUM\_DISCRIMINACAO

DATA\_FISCAL

Dados da chave do item do documento fiscal 

Tabela “filha” da FDT\_LANCTO\_P8 que contém as informações dos documentos ficais vinculados ao lançamento

MOVTO\_E\_S

NORM\_DEV

IDENT\_DOCTO

IDENT\_FIS\_JUR

NUM\_DOCFIS

SERIE\_DOCFIS

SUB\_SERIE\_DOCFIS

DISCRI\_ITEM

NUM\_ITEM

Número do item do documento fiscal

VLR\_AJUSTE

Valor do ajuste correspondente ao item

IND\_DIG\_CALCULADO

= __9__ 

\(indica lançamento gerado automaticamente pelo módulo Lançamentos Automáticos do ICMS ou IPI\)  

\(conteúdo fixo\)

	

# <a id="_Toc155274641"></a>Detalhamento da Gravação dos Lançamentos na ITEM\_APURAC\_DISCR

Lançamentos Complementares \- ITEM\_APURAC\_DISCR:

01

\(\*\)

Código da Empresa

COD\_EMPRESA

Informar o Código da Empresa que gerou o processo

02

\(\*\)

Código do Estabelecimento

COD\_ESTAB

Informar o Código do Estabelecimento que gerou o processo

03

\(\*\)

Obrigação Fiscal

COD\_TIPO\_LIVRO

Informar o código do livro fiscal\. Gravar:  
‘002 \- Livro de Apuração do IPI’;  


04

\(\*\)

Data da Apuração

DAT\_APURACAO

Informar a data da apuração a que se refere o lançamento\.   
Esta data deve ser sempre a data do último dia do período em questão\.

05

\(\*\)

Indicador da Apuração

IND\_TP\_APUR

Informar o tipo de apuração a que se refere o lançamento\. Gravar:   
‘3 \- Apuração do IPI’\.

06

 

UF

COD\_ESTADO

Não preencher

07

\(\*\)

Item da Apuração

COD\_OPER\_APUR

Informar o item da apuração para o qual será feito o lançamento\. Preencher de acordo com a parametrização, podendo ser:  
004 – Estorno de Débitos;  
005 – Outros Créditos;  
010 – Estorno de Créditos;  
011 – Ressarcimentos de Crédito;  
012 – Outros Débitos\.

08

\(\*\)

Número de Discriminação

NUM\_DISCRIMINACAO

Informar o número sequencial do lançamento\. \(gerado pelo sistema\)  


09

\(\*\)

Valor do Lançamento

VAL\_ITEM\_DISCRIM

Informar o valor do lançamento \(calculado pelo processo\)\.

10

\(\*\)

Descrição do Lançamento

DSC\_ITEM\_APURACAO

Informar a Descrição do Lançamento\.

Campo Descrição do Lançamentos das telas de parametrizações

11

 

Classe do Lançamento

COD\_CLASSE

Não preencher

12

 

Amparo/Texto/Ocorrência

COD\_AMPARO\_LEGAL

Não preencher

13

 

Subitem do Amparo/Texto/Ocorrência

COD\_SUB\_ITEM\_OCORR

Não preencher

14

 

Número Certificado

NUM\_CERTIFICADO

Não preencher

15

 

Identificação do Regime Especial \(DIME\-SC\)

COD\_REGIME\_ESPECIAL

Não preencher

16

 

Origem do Crédito \(DIME\-SC\)

COD\_ORIGEM

Não preencher

17

 

Número do Processo

NUM\_PROC

Não preencher

18

 

Origem do Processo

ORIGEM\_PROC

Informar a origem do processo/declaração de acordo com o campo “Número do Processo”\. Gravar:  
3 – Documento Fiscal;

19

 

Descrição do Processo

DSC\_PROC

Não preencher

20

 

Código de Ajuste \- Ato Cotepe ICMS 70/05 / IPI

COD\_AJUSTE

Informar o código de ajuste do lançamento para o Ato Cotepe 70/05,

Campo Código de Ajuste Sped \(Reg\. E530\) 

21

 

Observação

COD\_OBSERVACAO

Preencher com a informação do campo Observações SPED \(tela Parâmetros da Apuração\)

22

 

Código de Ajuste – Sped Fiscal \(E111/E220\)

COD\_AJUSTE\_ICMS

Não preencher

23

Tipo de Lançamento – Sped Fiscal

IND\_TIPO\_LANC

Não preencher

24

 

Sub\-Apuração do Sped Fiscal

IND\_SUB\_APUR

Não preencher

25

 

Indicador de Lançamento Complementar do Conv\. 52/05

IND\_EST\_DEB\_CONV

Não preencher

26

 

UF \- Conv\. 52/05

COD\_ESTADO\_CONV

Não preencher

27

 

Código de Ajuste \- Conv\. 52/05

COD\_AJ\_ICMS\_CONV

Não preencher

28

 

Código de Ajuste – SEFII – PE

COD\_AJUSTE\_SEF

Não preencher

29

 

Carta de Habilitação do Patrocínio

COD\_CHP\_LIC

Não preencher

30

 

Código do Motivo do Estorno \(DAPI\-MG\)

COD\_MOT\_EST

Não preencher

31

 

Auto de Infração \(DAPI\-MG\)

NUM\_AUTO\_INFRACAO

Não preencher

32

 

Código de Ajuste IPI – Sped Fiscal \(E530\)

COD\_AJUSTE\_IPI

Não preencher

33

 

Código NCM

COD\_NBM

Não preencher

Atenção\! Os campos acima \(inclusive a nomenclatura\), estão baseados na estrutura da SAFX216\. Caso haja campos que não existe na tabela ITEM\_APURAC\_DISCR, não gravar os mesmos\.

# <a id="_Toc155274642"></a>Detalhamento da Gravação dos Lançamentos na ITEM\_APURAC\_DISCR\_AJUSTE

 Documentos Vinculados \- ITEM\_APURAC\_DISCR\_AJUSTE:

01

\(\*\)

Código da Empresa

COD\_EMPRESA

Campo Chave da ITEM\_APURAC\_DISCR

02

\(\*\)

Código do Estabelecimento

COD\_ESTAB

Campo Chave da ITEM\_APURAC\_DISCR

03

\(\*\)

Obrigação Fiscal

COD\_TIPO\_LIVRO

Campo Chave da ITEM\_APURAC\_DISCR

04

\(\*\)

Data da Apuração

DAT\_APURACAO

Campo Chave da ITEM\_APURAC\_DISCR

05

\(\*\)

Indicador da Apuração

IND\_TP\_APUR

Campo Chave da ITEM\_APURAC\_DISCR

06

 

UF

COD\_ESTADO

Campo Chave da ITEM\_APURAC\_DISCR

07

\(\*\)

Item da Apuração

COD\_OPER\_APUR

Campo Chave da ITEM\_APURAC\_DISCR

08

\(\*\)

Número de Discriminação

NUM\_DISCRIMINACAO

Campo Chave da ITEM\_APURAC\_DISCR

09

\(\*\)

Data Fiscal do Documento Fiscal Vinculado

DATA\_FISCAL

Informar a data fiscal do documento fiscal vinculado\.

10

\(\*\)

Movimento Entrada/Saída do Documento Fiscal Vinculado

MOVTO\_E\_S

Informar o tipo do movimento do documento fiscal vinculado,  de acordo com:  
1\-Documento de entrada  de terceiros;  
2 \- Documento de entrada emitida pelo Estabelecimento, acolhendo notas de produtores agropecuários;  
3 \- Documento de entrada emitida pelo Estabelecimento, por retorno de mercadorias não entregues ao destinatário;                                                                                                                                          
4 \- Documento de entrada emitida pelo Estabelecimento, outros motivos legais;  
5 \- Documento de entrada emitida pelo Estabelecimento, globalizando conhecimento de frete ou material Uso/Consumo;  
9 \- Documento de saída\.

11

\(\*\)

Normal/ Devolução do Documento Fiscal Vinculado

NORM\_DEV

Informar o indicador de devolução do documento fiscal vinculado, de acordo com:  
1\-Normal;  
2\-Devolução\.

12

\(\*\)

Tipo do Documento Fiscal Vinculado

COD\_DOCTO

Informar o tipo do documento fiscal vinculado de acordo com a Tabela dos Tipos de Documento \(SAFX2005\)\.

13

\(\*\)

Indicador da Pessoa Física/Jurídica do Documento Fiscal Vinculado

IND\_FIS\_JUR

Informar o indicador da pessoa física/jurídica do documento fiscal vinculado, de acordo com a Tabela de Pessoas Física/Jurídica \(SAFX04\)\.

14

\(\*\)

Código da Pessoa Física/Jurídica do Documento Fiscal Vinculado

COD\_FIS\_JUR

Informar o código da pessoa física/jurídica do documento fiscal vinculado de acordo com a Tabela de Pessoas Física/Jurídica \(SAFX04\)\.

15

\(\*\)

Número do Documento Fiscal Vinculado

NUM\_DOCFIS

Informar o número do documento fiscal vinculado\.

16

 

Série do Documento Fiscal Vinculado

SERIE\_DOCFIS

Informar a série do documento fiscal vinculado\.

17

 

Subsérie do Documento Fiscal Vinculado

SUB\_SERIE\_DOCFIS

Informar a subsérie do documento fiscal vinculado\.

18

 

Número do Item do Documento Fiscal Vinculado

NUM\_ITEM

Informar o número do item do documento fiscal vinculado\.  
O preenchimento deste campo não é obrigatório e deve ser informado apenas quando o ajuste em questão tiver relação com algum item do documento\.

19

\(\*\)

Valor do Ajuste

VLR\_AJUSTE

Informar o valor do ajuste\.   
Este valor poderá ser o valor integral do lançamento complementar, ou apenas um dos valores que irão compor o total do lançamento\.

20

\(\*\)

Sequencial

NUM\_SEQUENCIAL

Preencher esse campo com valor fixo igual a 00001\. 

# <a id="_Toc155274643"></a>

Atenção\! Os campos acima \(inclusive a nomenclatura\), estão baseados na estrutura da SAFX218\. Caso haja campos que não existe na tabela ITEM\_APURAC\_DISCR\_AJUSTE, não gravar os mesmos\.

# Reprocessamento das Informações e Sinalização dos Lançamentos como ‘Lançamentos Automáticos’\.

Toda vez que for feita a geração do livro, na tela de Geração de Apuração, o sistema deve excluir os lançamentos automáticos gerado por esse processo e regerá\-los, para que não haja duplicidade ou perda de informações\.

Ao gerar um lançamento automático, o mesmo deve ficar sinalizado como lançamentos automáticos \(ind\_dig\_calc = ‘9’\)\.

__*\[MFS\-617413\] Detalhamento das regras para a deleção dos lançamentos no processamento/reprocessamento:*__

1. Ao executar o processo e não existir parametrização para a geração dos lançamentos automáticos, os lançamentos já existentes na base \(com ind\_dig\_calc <> '9'\) não devem ser apagados\. Caso existam lançamentos com ind\_dig\_calc = '9', os mesmos devem ser apagados\.
2. Apagar os lançamentos \(com ind\_dig\_calc <> '9'\), se for encontrado parametrização e dados para a geração de um determinado código de apuração que tenha o nº de discriminação '1', mesmo que a origem seja <> '3'\. Isto se faz necessário, pois utilizamos sempre o nº de discriminação '1' nos processos automáticos \(essa informação está inclusive no manual layout\) e a origem não faz parte da chave da tabela\. Caso necessário, o usuário deve primeiro efetuar os lançamentos automáticos e depois carregar ou digitar manualmente os demais lançamentos\.

 

