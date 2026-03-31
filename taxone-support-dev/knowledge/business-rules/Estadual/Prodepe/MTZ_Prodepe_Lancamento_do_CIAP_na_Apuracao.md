# MTZ_Prodepe_Lancamento_do_CIAP_na_Apuracao

- **Fonte:** MTZ_Prodepe_Lancamento_do_CIAP_na_Apuracao.docx
- **Modificado:** 2021-04-23
- **Tamanho:** 67 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__            Geração Automática de Lançamentos \- Lançamento do CIAP na Apuração do ICMS __

__Localização__: Menu Estadual, Módulo Prodepe, item Obrigações 🡪 Geração Automática de Lançamentos 🡪 Lançamento do CIAP na Apuração do ICMS   

Este documento é especifico da opção “Lançamento do CIAP na Apuração do ICMS” do menu “Geração Automática de Lançamentos”\. Para as demais opções, consultar o documento de regras específico\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4138

Lançamentos Automáticos 

Inclusão do código de ajuste do SEF II\-PE nas telas de parametrização dos lançamentos

04/02/2014

\(criação do docto\)

__MFS21919__

Lançamentos Automáticos 

A geração dos lançamentos foi alterada para considerar o campo “__*Código de Ajuste do Sped Fiscal*__”, que foi incluído nas telas de parametrização dos lançamentos

09/07/2019

REGRAS DE NEGÓCIO

__RN00__

__                                                                             Regras Gerais__

O processo executado neste item de menu gera de forma automática o lançamento do crédito do CIAP nas apurações dos livros do Prodepe\. O valor do CIAP será rateado entre todos os livros de apuração do Estabelecimento, conforme o percentual de participação das saídas de cada livro\.

*\(para detalhes consultar o help deste item de menu, e também a OS1044\-A \(Fev/2003\), cuja documentação da época ainda não era através dos documentos de regras\)*

__RN01__

__                                                                        Parâmetros de Tela__

__RN02__

__                                                                 Geração dos Lançamentos __

Origem dos dados do lançamento:

\- Parametrização do menu “Parâmetros > __Dados Gerais__”, campos 🡪 “__Parâmetros p/o Lançamento do Crédito do CIAP__”

\- Tabela do Cálculo da Proporção das Saídas \(ICT\_TOT\_SAIDA\_INCE\)

__Para cada Estabelecimento selecionado em tela__:

 

Alteração da __OS3148__: inclusão do código de Ajuste do SEF II na parametrização dos lançamentos;

Alteração da __MFS21919__: inclusão do código de Ajuste do Sped Fiscal na parametrização dos lançamentos;

 

__Passo 1__: Recuperação dos parâmetros do lançamento:

Serão recuperados os dados da parametrização \(ICT\_PAR\_INCENT\) do estabelecimento: COD\_OPER\_APUR, DSC\_OPER\_APUR, COD\_CLASSE, COD\_AMPARO\_LEGAL, COD\_SUB\_ITEM\_OCORR, COD\_AJUSTE\_SEF e__ COD\_AJUSTE\_ICMS__\. Caso o campo COD\_OPER\_APUR esteja nulo, será gerada uma mensagem de erro no log de processo, e o estabelecimento em questão não será processado\.

__Passo 2__: Recuperação dos Percentuais das Saídas de cada livro do Estabelecimento:

*\(estes percentuais são previamente calculados no menu “Cálculo da Proporção das Saídas”\)*

Será recuperado o percentual das saídas de *cada livro de apuração do estabelecimento* \(tabela ICT\_TOT\_SAIDA\_INCE\), filtrando pela data final da apuração, estabelecimento e empresa selecionados em tela\. O percentual que será utilizado corresponde ao campo VLR\_PERC\_SAI\.

__Passo 3__: Cálculo do Valor Proporcional do Crédito:

Para cada registro recuperado no Passo 2, ou seja, cada livro de apuração do estabelecimento, será calculado o valor do CIAP\. O cálculo é feito aplicando\-se o percentual obtido de cada livro \(Passo 2\), sobre o valor total do CIAP \(que aparece na tela da geração\), da seguinte forma:

                                                 VLR\_LANCTO = \( VLR\_CRED\_CIAP \* VLR\_PERC\_SAI \) / 100

__Obs\.1__: o campo VLR\_LANCTO, equivale ao valor do lançamento que caberá a cada livro de apuração do estabelecimento;

__Obs\.2__: o campo VLR\_CRED\_CIAP, equivale ao valor do campo “Valor Crédito CIAP” da tela da geração;

__Obs\.3__: o campo VLR\_PERC\_SAI é o percentual obtido para cada livro do estabelecimento, recuperado no Passo 2;

Importante 🡪O tratamento de rateio proporcional para os CFOP’s parametrizados na tela de “Cálculo de Proporcionalidade – Por CFOP”  

__Passo 4__: Gravação dos Lançamentos nos livros de apuração:

Para cada livro de apuração do estabelecimento em questão \(cada registro recuperado no Passo 2\), será gravado um lançamento \(tabela ICT\_AP\_DISC\_INCE\), de acordo com a definição abaixo:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

COD\_TIPO\_LIVRO

Para o livro não incentivado será gravado ‘143’ 

Para os livros incentivados será gravado ‘142’

A identificação do tipo de livro esta no campo SERIE\_LIVRO \(recuperado no passo 2\):

Se = ‘A’ 🡪 indica que o livro é não incentivado;

Se = ‘B’ 🡪 indica que o livro é incentivado;

DAT\_APURACAO

Data final do período de apuração selecionao em tela\.

SERIE\_LIVRO

Campo SERIE\_LIVRO \(recuperado no Passo 2\)

SUB\_SERIE\_LIVRO

Campo SUB\_SERIE\_LIVRO \(recuperado no Passo 2\)

COD\_OPER\_APUR

Campo COD\_OPER\_APUR da parametrização

NUM\_DISCRIMINACAO

Recuperar a maior discriminação, para os campos acima, e somar mais um\.

Este campo é um  sequencial dos lançamentos de um determinado item da apuração \(COD\_OPER\)

VAL\_ITEM\_DISCRIM

Valor do lançamento \(VLR\_LANCTO calculado no Passo 3\)

IND\_TIPO\_DEDUCAO

*\(sem informação\)*

Esse campo, inicialmente, não será utilizado\.

DSC\_ITEM\_APURACAO

Campo DSC\_OPER\_APUR da parametrização

IND\_DIG\_CALCULADO

2

1\-Digitado e 2\-Calculado

COD\_CLASSE

Campo COD\_CLASSE da parametrização

COD\_AMPARO\_LEGAL

Campo COD\_AMPARO\_LEGAL da parametrização

COD\_SUB\_ITEM\_OCORR

Campo COD\_SUB\_ITEM\_OCORR da parametrização

COD\_AJUSTE\_SEF

Campo COD\_AJUSTE\_SEF da parametrização

__OS3148__: o código de ajuste parametrizado passou a ser gravado no lançamento

COD\_AJUSTE\_ICMS

Campo COD\_AJUSTE\_ICMS da parametrização

\(Campo “Código de Ajuste \(Sped Fiscal \- Reg\. E111\)”\)

__MFS21919__: o código de ajuste do Sped Fiscal, incluído na parametrização, passou a ser gravado no lançamento

 

= = = = = = = =  

