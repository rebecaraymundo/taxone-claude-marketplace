# MTZ-CIAP-Lancto_Credito_Extemporaneo

- **Fonte:** MTZ-CIAP-Lancto_Credito_Extemporaneo.docx
- **Modificado:** 2023-04-27
- **Tamanho:** 31 KB

---

# Módulo – Ativo Permanente – Lançamento dos Créditos Extemporâneos na Apuração do ICMS 

Localização: Menu Estadual, Módulo CIAP, item Movimento 🡪 Créditos Extemporâneos 🡪 Lançamento dos Créditos na Apuração

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS2931\-B10

Tratamento dos Créditos Extemporâneos

O objetivo desta OS é implementar o tratamento dos créditos extemporâneos do CIAP para a geração do registro G126 do Sped Fiscal – Bloco G\. 

27/09/2010

\(criação\)

## REGRAS DE NEGÓCIO

__Cód__

__Descrição__

__DR__

# RN00

O cálculo dos créditos extemporâneos foi implementado no Módulo CIAP para atender à geração do registro G126 do Sped Fiscal na __OS2931\-B10__\.

__Parâmetros de Tela__:

Campo “Estabelecimento” 🡪 Exibe todos os estabelecimentos parametrizados no CIAP \(APT\_ESTAB\)

Campo “Período de Apuração” 🡪 Exibe o período de apuração do ICMS que se encontra em aberto\. Estes períodos são obtidos com base no calendário da Apuração do ICMS, considerando o tipo de livro “108”\. 

    

OS2931\-B10

# RN01

__Processamento__:

Para cada estabelecimento selecionado, será gravado um lançamento complementar na apuração do ICMS, livro “__108__”\.

 

Origem dos dados: Tabela que armazena os créditos extemporâneos calculados e a tabela da parametrização do CIAP \(APT\_ESTAB\)\.

   

Para cada Estabelecimento é feita a totalização dos créditos extemporâneos de todos os Bens calculados no período\. O resultado obtido é gravado na tabela dos lançamentos complementares da Apuração do ICMS, conforme descrito na __RN02__\.  As informações do lançamento utilizam os dados parametrizados para o Estabelecimento\.

Para recuperar os créditos extemporâneos de cada estabelecimento, utilizar os seguintes critérios:

*Empresa                   =  código da empresa*

*Estabelecimento       =  código do estabelecimento*

*Data da Apuração    =  data final do período de apuração*

# RN02

__Gravação dos Dados__:

COD\_EMPRESA                =  código da empresa

COD\_ESTAB                      =  código do estabelecimento

COD\_TIPO\_LIVRO             =   '__108__'

DAT\_APURACAO               =  data final do período da apuração 

COD\_OPER\_APUR            =  item da apuração parametrizado \(coluna ITEM\_AP\_102  da APT\_ESTAB\)

DSC\_ITEM\_APURACAO   = grava o texto “Créditos Extemporâneos do CIAP”

VAL\_ITEM\_DISCRIM         = total dos créditos extemporâneos do período 

NUM\_DISCRIMINACAO    =  seqüencial do lançamento \(ver __OBS1\)__

IND\_TIPO\_DEDUCAO        = nulo

IND\_DIG\_CALCULADO     = “8”

COD\_CLASSE                  =  código da classe parametrizado \(coluna COD\_CLASSE\_102 da APT\_ESTAB\)

COD\_AMPARO\_LEGAL = código do amparo legal parametrizado \(coluna COD\_AMP\_LEG\_102  da APT\_ESTAB\)

                                                \(ver __OBS2__\)

COD\_SUB\_ITEM\_OCORR =  código do sub\-item parametrizado \(coluna COD\_SUB\_OCO\_102 da APT\_ESTAB\)

COD\_AJUSTE\_ICMS          = código de ajuste parametrizado \(coluna COD\_AJUSTE\_ICMS da APT\_ESTAB\)

IND\_TIPO\_LANCTO           =  3 \(“Outros Lançamentos”\)

 

__OBS 1__ – Coluna NUM\_DISCRIMINACAO:

A coluna NUM\_DISCRIMINACAO é um sequencial dos lançamentos feitos para um mesmo código de operação\.  Para preenchê\-la deve\-se recuperar o maior sequencial existente na ITEM\_APURAC\_DISCR para o código de operação que se deseja gravar, incrementar um, e gravar o registro\.  

__OBS 2__ – Validação do Amparo Legal:

Quando existir amparo legal parametrizado, será verificado se o amparo é válido para o período da apuração, da seguinte forma:

Deve existir na Tabela dos Amparos Legais \(DWT\_AMPARO\_LEGAL\) um registro do código de amparo na seguinte condição:

- Validade inicial  <=  Data da Apuração 
- Validade final     >= Data da Apuração

Caso *não* exista nenhum registro do código nesta condição, o lançamento será gravado normalmente, mas no log de processo será gravada a seguinte mensagem de aviso:   \(é a mensagem de código 108144 da TFIX22\) 

                 *“O Código do Amparo Legal/Subitem deste lançamento não é válido para o período da apuração” *

A data de validade final do amparo *não é obrigatória*, e portanto poderá estar sem informação\. A tabela dos amparos legais é por UF, e para recuperar o código desejado é utilizada a UF do Estabelecimento\.

