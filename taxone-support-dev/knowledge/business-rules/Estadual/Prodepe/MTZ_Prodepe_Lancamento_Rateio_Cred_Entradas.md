# MTZ_Prodepe_Lancamento_Rateio_Cred_Entradas

- **Fonte:** MTZ_Prodepe_Lancamento_Rateio_Cred_Entradas.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 65 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__            Geração Automática de Lançamentos \- Lançamento do Rateio do Crédito das Entradas __

__Localização__: Menu Estadual, Módulo Prodepe, item Obrigações 🡪 Geração Automática de Lançamentos 🡪 Lançamento do Rateio do Crédito das Entradas   

Este documento é especifico da opção “Lançamento do Rateio do Crédito das Entradas” do menu “Geração Automática de Lançamentos”\. Para as demais opções, consultar o documento de regras específico\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4138

Lançamentos Automáticos 

Inclusão do código de ajuste do SEF II\-PE nas telas de parametrização dos lançamentos

05/02/2014

\(criação do docto\)

OS4794

Ajustes na geração do Meio Magnético do SEF II \- PE

Ajustes na geração do Meio Magnético do SEF II – PE

16/05/2015

__MFS21919__

Lançamentos Automáticos 

A geração dos lançamentos foi alterada para considerar o campo “__*Código de Ajuste do Sped Fiscal*__”, que foi incluído nas telas de parametrização dos lançamentos

09/07/2019

REGRAS DE NEGÓCIO

__RN00__

__                                                                             Regras Gerais__

O processo executado neste item de menu gera de forma automática, os lançamentos que transferem créditos do livro não incentivado para os livros incentivados do Prodepe\.

Os valores a serem transferidos entre os livros são calculados previamente no relatório “Rateio do Crédito das Entradas” do Módulo Prodepe\. O cálculo é feito por perfil\. Cada perfil parametrizado para este relatório \(menu “Parâmetros 🡪 Rateio do Crédito das Entradas”\) será calculado separadamente\. Desta forma, ao consultar o relatório, os valores aparecerão separados, perfil a perfil\.

*\(para detalhes consultar o help deste item de menu, e também a OS1512 \(Dez/2004\), cuja documentação da época ainda não era através dos documentos de regras\)*

__RN01__

__                                                                        Parâmetros de Tela__

__RN02__

__                                                                 Geração dos Lançamentos __

Origem dos dados do lançamento:

\- Parametrização do menu “Parâmetros > __Dados Gerais__”, campos 🡪 “Parâmetros p/o Lançamento de Rateio do Crédito das Entradas”

\- Tabela dos dados gerados pelo relatório de rateio dos créditos \(menu “Relatórios 🡪 Rateio do Crédito das Entradas”\)

Para cada estabelecimento selecionado em tela, os lançamentos serão gerados para cada perfil de rateio existente para o Estabelecimento, considerando apenas os perfis selecionados na tela\.

*Obs: A geração dos valores do rateio é feita previamente no relatório ““Rateio do Crédito das Entradas”\. Para cada perfil, o relatório calcula um valor de crédito a ser rateado entre os livros parametrizados \(o usuário escolhe os livros que entram no rateio\)\. *

Para cada perfil, os lançamentos são gerados a partir dos valores de crédito apurados para os livros não incentivados \(Série = B\)\. Ou seja, consultando o relatório, são as linhas onde a coluna Série = B\. 

__                 Para cada linha com Série = “B”, serão efetuados dois lançamentos, conforme descrito abaixo:__

__Lançamento__

__Parametrização utilizada__

Um lançamento de saída do crédito do livro não incentivado

Menu 🡪 “Parâmetros > Dados Gerais”

Campos 🡪 “Parâmetros p/o Lançamento de Rateio do Crédito das Entradas”, opção “Lançamento de __saída__ do crédito do livro __não incentivado__” 

Um  lançamento de entrada do crédito no livro não incentivado

Menu 🡪 “Parâmetros > Dados Gerais”

Campos 🡪 “Parâmetros p/o Lançamento de Rateio do Crédito das Entradas”, opção “Lançamento de __entrada__ do crédito no __livro incentivado__”

Os lançamentos são gravados na tabela dos lançamentos complementares do Prodepe \(ICT\_AP\_DISC\_INCE\), com os seguintes dados: 

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

DAT\_APURACAO

Data final do período de apuração selecionao em tela\.

SERIE\_LIVRO

Série do livro em questão

SUB\_SERIE\_LIVRO

Sub\-série do livro em questão

COD\_OPER\_APUR

No lançamento de __saída__ de crédito do livro não incentivado:

     Campo COD\_OPER\_RATEIO\___S__ da parametrização

No lançamento de __entrada__ de crédito no livro incentivado:

     Campo COD\_OPER\_RATEIO\___E__ da parametrização

NUM\_DISCRIMINACAO

Recuperar a maior discriminação, para os campos acima, e somar mais um\.

Este campo é um  sequencial dos lançamentos de um determinado item da apuração \(COD\_OPER\)

VAL\_ITEM\_DISCRIM

Valor do lançamento\.

Será o valor que aparece na coluna “Valor do Crédito” do relatório do rateio\.

IND\_TIPO\_DEDUCAO

*\(sem informação\)*

Esse campo, inicialmente, não será utilizado\.

DSC\_ITEM\_APURACAO

Descrição fixa = “Transf crédito do LNI para o LI”

IND\_DIG\_CALCULADO

2

1\-Digitado e 2\-Calculado

COD\_CLASSE

No lançamento de __saída__ de crédito do livro não incentivado:

     Campo COD\_CLASSE\_RATEIO\___S__ da parametrização

No lançamento de __entrada__ de crédito no livro incentivado:

     Campo COD\_CLASSE\_RATEIO\___E__ da parametrização

COD\_AMPARO\_LEGAL

No lançamento de __saída__ de crédito do livro não incentivado:

     Campo COD\_AMP\_RATEIO\___S__ da parametrização

No lançamento de __entrada__ de crédito no livro incentivado:

     Campo COD\_AMP\_RATEIO\___E__ da parametrização

COD\_SUB\_ITEM\_OCORR

No lançamento de __saída__ de crédito do livro não incentivado:

     Campo COD\_SUB\_AMP\_RATEIO\___S__ da parametrização

No lançamento de __entrada__ de crédito no livro incentivado:

     Campo COD\_SUB\_AMP\_RATEIO\___E__ da parametrização

COD\_AJUSTE\_SEF

No lançamento de __saída__ de crédito do livro não incentivado:

    Campo COD\_AJ\_SEF\_RATEIO\___S__ da parametrização

No lançamento de __entrada__ de crédito no livro incentivado:

    Campo COD\_AJ\_SEF\_RATEIO\___E__ da parametrização

__OS3148__: o código de ajuste parametrizado passou a ser gravado nos lançamentos

COD\_AJUSTE\_ICMS

No lançamento de __saída__ de crédito do livro não incentivado:

    Campo __COD\_AJ\_ICMS\_RATEIO\_S__ da parametrização

No lançamento de __entrada__ de crédito no livro incentivado:

    Campo __COD\_AJ\_ICMS\_RATEIO\_E__ da parametrização

__MFS21919__: o código de ajuste do Sped Fiscal, incluído na parametrização, passou a ser gravado no lançamento

Identificador de lançamento de transferência de crédito referente a notas fiscais de modelos diferentes de 01/55

Para cada perfil da geração, todos os lançamentos envolvidos \(tanto de saída do crédito do livro não incentivado, como da entrada do crédito no livro incentivado\), este campo será gravado de acordo com a informação parametrizada no menu “Parâmetros 🡪 Relatório de Rateio do Crédito das Entradas”, aba “Dados Gerais/Lanctos”, campo “*Lancto de transferência de crédito referente a NFs de modelos diferentes de 01/55*”:

Se marcado 🡪 será gravado “S”

Se desmarcado 🡪 será gravado “N”

__OS4794__: nesta OS foi criado este parâmetro que passou a ser gravado nos lançamentos

 

= = = = = = = =  

