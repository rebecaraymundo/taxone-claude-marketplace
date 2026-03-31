# MTZ_Prodepe_Lancamento_Automatico_dos_Incentivos

- **Fonte:** MTZ_Prodepe_Lancamento_Automatico_dos_Incentivos.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 86 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__                 Geração Automática de Lançamentos \- Lançamento Automático dos Incentivos __

__Localização__: Menu Estadual, Módulo Prodepe, item Obrigações 🡪 Geração Automática de Lançamentos 🡪 Lançamento Automático dos Incentivos   

Este documento é especifico da opção “Lançamento Automático dos incentivos” do menu “Geração Automática de Lançamentos”\. Para as demais opções, consultar o documento de regras específico\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4138

Lançamentos Automáticos 

Inclusão do código de ajuste do SEF II\-PE nas telas de parametrização dos lançamentos

03/02/2014

\(criação do docto\)

__MFS21919__

Lançamentos Automáticos 

A geração dos lançamentos foi alterada para considerar o campo “__*Código de Ajuste do Sped Fiscal*__”, que foi incluído nas telas de parametrização dos lançamentos

09/07/2019

REGRAS DE NEGÓCIO

__RN00__

__                                                                             Regras Gerais__

O processo executado neste item de menu gera de forma automática, alguns tipos de lançamentos nas apurações dos livros incentivados do Prodepe\.

Segue relação dos lançamentos gerados, a parametrização relacionada e a regra da geração: 

__Lançamento__

__Modalidade do Incentivo__

__Parametrização utilizada__

__Regra __

Incentivo das saídas p/fora NE

Indústria 

Menu 🡪 “Parâmetros > __Dados Gerais__”

Campos 🡪 “Parâmetros p/o Incentivo das Saídas p/fora NE” 

__RN02__

Crédito presumido

Indústria 

Menu 🡪 “Parâmetros > __Grupos de Incentivo__”

Campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido”

__RN03__

Crédito presumido

Importação

Menu 🡪”Parâmetros > __Grupos de Incentivo__”

Campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido”

__RN04__

Crédito presumido

CD \(Entradas\)

Menu 🡪 “Parâmetros > __Grupos de Incentivo__”

Campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido – Entradas \(Central de Distribuição\)”

__RN05__

Crédito presumido

CD \(Saídas\)

Menu 🡪 “Parâmetros > __Grupos de Incentivo__”

Campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido”

__RN06__

Estorno calculado

Indústria

Menu 🡪 “Parâmetros > __Grupos de Incentivo__”

Campos 🡪 “Parâmetros p/o Lançamento de Estorno de Crédito”

__RN07__

A seguir serão descritas as regras de funcionamento da tela e a geração de cada tipo de lançamento\.

__RN01__

__                                                                        Parâmetros de Tela__

__RN02__

__                                                      Incentivo das saídas p/fora NE   \(Indústria\)                                            __

Origem dos dados do lançamento:

\- Parametrização do menu “Parâmetros > __Dados Gerais__”, campos 🡪 “Parâmetros p/o Incentivo das Saídas p/fora NE”

\- Tabela do Valor dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

__Para cada Estabelecimento e Livro de Apuração \(Série\-Subsérie\) selecionado em tela__:

 

Alteração da __OS3148__: inclusão do código de Ajuste do SEF II na parametrização dos lançamentos;

Alteração da __MFS21919__: inclusão do código de Ajuste do Sped Fiscal na parametrização dos lançamentos;

 

__Passo 1__: Recuperação dos parâmetros do lançamento:

Serão recuperados os dados da parametrização \(ICT\_PAR\_INCENT\) do estabelecimento: COD\_OPER\_FRETE, DSC\_OPER\_FRETE, COD\_CLASSE\_FRETE, COD\_AMP\_FRETE, COD\_SUB\_AMP\_FRETE, COD\_AJUSTE\_SEF\_FRETE e__ COD\_AJUSTE\_ICMS\_FRETE__\. 

__Passo 2__: Recuperação dos Valores de Incentivo Calculado:

O valor do incentivo a ser utilizado no lançamento, será recuperado da tabela dos incentivos calculados \(ICT\_VLR\_INCENT\), considerando os seguintes critérios:

    COD\_EMPRESA 🡪 código da Empresa do login 

    COD\_ESTAB 🡪 código do estabelecimento selecionado 

    DAT\_APURACAO 🡪 data de apuração do livro selecionado

    COD\_GRP\_INCENT 🡪 código do grupo de incentivo referente à série/subsérie do livro de apuração em questão 

    PERCENTUAL\_INCENT 🡪 percentual de incentivo referente à série/subsérie do livro de apuração em questão 

    TIPO\_INCENT 🡪 = ‘__F__’  \(os registros deste tipo de incentivo são identificados por ‘__F__’\) 

    VLR\_CPRES 🡪  > 0 \(não serão considerados registros com este valor igual a zero ou nulo\)

Caso exista o valor para efetuar o lançamento, mas o campo COD\_OPER\_FRETE da parametrização esteja nulo, será gerada uma mensagem de erro no log de processo, e o lançamento não será gerado\.

__Passo 3__: Gravar na tabela dos lançamentos \(ICT\_AP\_DISC\_INCE\) um novo registro, com os seguintes dados:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

COD\_TIPO\_LIVRO

= “142”

Livro de Apuração Incentivada

SERIE\_LIVRO

Série do livro de apuração

SUB\_SERIE\_LIVRO

Sub\-série do livro de apuração

DAT\_APURACAO

Data final do período de apuração selecionada em tela\.

COD\_OPER\_APUR

Campo COD\_OPER\_FRETE da parametrização

NUM\_DISCRIMINACAO

Recuperar a maior discriminação, para os campos acima, e somar mais um\.

Este campo é um  sequencial dos lançamentos de um determinado item da apuração \(COD\_OPER\)  

VAL\_ITEM\_DISCRIMINACAO

Valor do lançamento \(campo VLR\_CPRES da tabela dos incentivos calculados\)

IND\_TIPO\_DEDUCAO

*\(sem informação\)*

Esse campo, inicialmente, não será utilizado\.

IND\_DIG\_CALCULADO

= “2”

1\-Digitado e 2\-Calculado

DSC\_ITEM\_APURADO

Campo DSC\_OPÉR\_FRETE da parametrização

COD\_CLASSE

Campo COD\_CLASSE\_FRETE da parametrização

COD\_AMPARO\_LEGAL

Campo COD\_AMP\_FRETE da parametrização

COD\_SUB\_ITEM\_OCORR

Campo COD\_SUB\_AMP\_FRETE da parametrização

COD\_AJUSTE\_SEF

Campo COD\_AJUSTE\_SEF\_FRETE da parametrização

__OS3148__: o código de ajuste do SEF II parametrizado, passou a ser gravado no lançamento

COD\_AJUSTE\_ICMS

Campo COD\_AJUSTE\_ICMS\_FRETE da parametrização

\(Campo “Código de Ajuste \(Sped Fiscal \- Reg\. E111\)”\)

__MFS21919__: o código de ajuste do Sped Fiscal, incluído na parametrização, passou a ser gravado no lançamento

__RN03__

__                                                              Crédito presumido \- Indústria                                              __

Origem dos dados do lançamento:

\- Parametrização do menu “Parâmetros > __Grupos de Incentivo__”, campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido”

\- Tabela do Valor dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

__Para cada Estabelecimento e Livro de Apuração \(Série\-Subsérie\) selecionado em tela__:

 

Alteração da __OS3148__: inclusão do código de Ajuste do SEF II na parametrização dos lançamentos;

Alteração da __MFS21919__: inclusão do código de Ajuste do Sped Fiscal na parametrização dos lançamentos;

 

__Passo 1__: Recuperação dos parâmetros do lançamento:

Serão recuperados os dados da parametrização \(ICT\_GRP\_INCENT\) do estabelecimento: COD\_OPER\_APUR, DSC\_OPER\_APUR, COD\_CLASSE, COD\_AMPARO\_LEGAL, COD\_SUB\_ITEM\_OCORR, COD\_AJUSTE\_SEF e __COD\_AJUSTE\_ICMS__\. 

__Passo 2__: Recuperação dos Valores de Incentivo Calculado:

O valor do incentivo a ser utilizado no lançamento, será recuperado da tabela dos incentivos calculados \(ICT\_VLR\_INCENT\), considerando os seguintes critérios:

    COD\_EMPRESA 🡪 código da Empresa do login 

    COD\_ESTAB 🡪 código do estabelecimento selecionado 

    DAT\_APURACAO 🡪 data de apuração do livro selecionado

    COD\_GRP\_INCENT 🡪 código do grupo de incentivo referente à série/subsérie do livro de apuração em questão 

    PERCENTUAL\_INCENT 🡪 percentual de incentivo referente à série/subsérie do livro de apuração em questão 

    TIPO\_INCENT 🡪 = ‘__C__’  \(os registros deste tipo de incentivo são identificados por ‘__C__’\) 

    VLR\_CPRES 🡪  > 0 \(não serão considerados registros com este valor igual a zero ou nulo\)

Caso exista valor para efetuar o lançamento, mas o campo COD\_OPER\_APUR da parametrização esteja nulo, será gerada uma mensagem de erro no log de processo, e o lançamento não será gerado\.

__Passo 3__: Gravar na tabela dos lançamentos \(ICT\_AP\_DISC\_INCE\) um novo registro, com os seguintes dados:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

COD\_TIPO\_LIVRO

= “142”

Livro de Apuração Incentivada

SERIE\_LIVRO

Série do livro de apuração

SUB\_SERIE\_LIVRO

Sub\-série do livro de apuração

DAT\_APURACAO

Data final do período de apuração selecionada em tela\.

COD\_OPER\_APUR

Campo COD\_OPER\_APUR da parametrização

NUM\_DISCRIMINACAO

Recuperar a maior discriminação, para os campos acima, e somar mais um\.

Este campo é um  sequencial dos lançamentos de um determinado item da apuração \(COD\_OPER\)  

VAL\_ITEM\_DISCRIMINACAO

Valor do lançamento \(campo VLR\_CPRES da tabela dos incentivos calculados\)

IND\_TIPO\_DEDUCAO

*\(sem informação\)*

Esse campo, inicialmente, não será utilizado\.

IND\_DIG\_CALCULADO

= “2”

1\-Digitado e 2\-Calculado

DSC\_ITEM\_APURADO

Campo DSC\_OPÉR\_APUR da parametrização

COD\_CLASSE

Campo COD\_CLASSE da parametrização

COD\_AMPARO\_LEGAL

Campo COD\_AMPARO\_LEGAL da parametrização

COD\_SUB\_ITEM\_OCORR

Campo COD\_SUB\_ITEM\_OCORR da parametrização

COD\_AJUSTE\_SEF

Campo COD\_AJUSTE\_SEF da parametrização

__OS3148__: o código de ajuste do SEF II parametrizado, passou a ser gravado no lançamento

COD\_AJUSTE\_ICMS

Campo COD\_AJUSTE\_ICMS da parametrização

Campo “Código de Ajuste \(Sped Fiscal \- Reg\. E111\)” da parametrização

__MFS21919__: o código de ajuste do Sped Fiscal, incluído na parametrização, passou a ser gravado no lançamento

__RN04__

__                                                             Crédito presumido \- Importação                                                                                              __

Origem dos dados do lançamento:

\- Parametrização do menu “Parâmetros > __Grupos de Incentivo__”, campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido”

\- Tabela do Valor dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

__Para cada Estabelecimento e Livro de Apuração \(Série\-Subsérie\) selecionado em tela__:

 

Alteração da __OS3148__: inclusão do código de Ajuste do SEF II na parametrização dos lançamentos;

Alteração da __MFS21919__: inclusão do código de Ajuste do Sped Fiscal na parametrização dos lançamentos;

 

__Passo 1__: Recuperação dos parâmetros do lançamento:

Serão recuperados os dados da parametrização \(ICT\_GRP\_INCENT\) do estabelecimento: COD\_OPER\_APUR, DSC\_OPER\_APUR, COD\_CLASSE, COD\_AMPARO\_LEGAL, COD\_SUB\_ITEM\_OCORR, COD\_AJUSTE\_SEF e__ COD\_AJUSTE\_ICMS__\. 

__Passo 2__: Recuperação dos Valores de Incentivo Calculado:

O valor do incentivo a ser utilizado no lançamento, será recuperado da tabela dos incentivos calculados \(ICT\_VLR\_INCENT\), considerando os seguintes critérios:

    COD\_EMPRESA 🡪 código da Empresa do login 

    COD\_ESTAB 🡪 código do estabelecimento selecionado 

    DAT\_APURACAO 🡪 data de apuração do livro selecionado

    COD\_GRP\_INCENT 🡪 código do grupo de incentivo referente à série/subsérie do livro de apuração em questão 

    PERCENTUAL\_INCENT 🡪= 0 *\(esta coluna é utilizada somente p/os incentivos tipo “Indústria”\)* 

    TIPO\_INCENT 🡪 = ‘__I__’  \(os registros deste tipo de incentivo são identificados por ‘__I__’\) 

    VLR\_CPRES 🡪  > 0 \(não serão considerados registros com este valor igual a zero ou nulo\)

Caso exista o valor para efetuar o lançamento, mas o campo COD\_OPER\_APUR da parametrização esteja nulo, será gerada uma mensagem de erro no log de processo, e o lançamento não será gerado\.

__Passo 3__: Gravar na tabela dos lançamentos \(ICT\_AP\_DISC\_INCE\) um novo registro, com os seguintes dados:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

COD\_TIPO\_LIVRO

= “142”

Livro de Apuração Incentivada

SERIE\_LIVRO

Série do livro de apuração

SUB\_SERIE\_LIVRO

Sub\-série do livro de apuração

DAT\_APURACAO

Data final do período de apuração selecionada em tela\.

COD\_OPER\_APUR

Campo COD\_OPER\_APUR da parametrização

NUM\_DISCRIMINACAO

Recuperar a maior discriminação, para os campos acima, e somar mais um\.

Este campo é um  sequencial dos lançamentos de um determinado item da apuração \(COD\_OPER\)  

VAL\_ITEM\_DISCRIMINACAO

Valor do lançamento \(campo VLR\_CPRES da tabela dos incentivos calculados\)

IND\_TIPO\_DEDUCAO

*\(sem informação\)*

Esse campo, inicialmente, não será utilizado\.

IND\_DIG\_CALCULADO

= “2”

1\-Digitado e 2\-Calculado

DSC\_ITEM\_APURADO

Campo DSC\_OPÉR\_APUR da parametrização

COD\_CLASSE

Campo COD\_CLASSE da parametrização

COD\_AMPARO\_LEGAL

Campo COD\_AMPARO\_LEGAL da parametrização

COD\_SUB\_ITEM\_OCORR

Campo COD\_SUB\_ITEM\_OCORR da parametrização

COD\_AJUSTE\_SEF

Campo COD\_AJUSTE\_SEF da parametrização

__OS3148__: o código de ajuste do SEF II parametrizado, passou a ser gravado no lançamento

COD\_AJUSTE\_ICMS

Campo COD\_AJUSTE\_ICMS da parametrização

Campo “Código de Ajuste \(Sped Fiscal \- Reg\. E111\)” da parametrização

__MFS21919__: o código de ajuste do Sped Fiscal, incluído na parametrização, passou a ser gravado no lançamento

__RN05__

__                                              Crédito presumido – Central de Distribuição \(Entradas\)                                               __

*Obs: O incentivo da Central de Distribuição é o único que pode gerar dois tipos de lançamentos, um referente às operações de entrada, e outro às operações de saída\. Para efetuar o lançamento do CP das Entradas, são utilizados os parâmetros do quadro “Parâmetros p/o Lançamento do Crédito Presumido – Entradas \(Central de Distribuição\)”, e para o lançamento do CP das Saídas, são utilizados os parâmetros do quadro “Parâmetros p/o Lançamento do Crédito Presumido”\. Para maior detalhamento das regras, a RN05 define o lançamento referente às entradas, e a RN06 o referente às saídas\.*

Origem dos dados do lançamento:

\- Parametrização do menu “Parâmetros > __Grupos de Incentivo__”, campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido – 

   Entradas \(Central de Distribuição\)”

\- Tabela do Valor dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

__Para cada Estabelecimento e Livro de Apuração \(Série\-Subsérie\) selecionado em tela__:

 

Alteração da __OS3148__: inclusão do código de Ajuste do SEF II na parametrização dos lançamentos;

Alteração da __MFS21919__: inclusão do código de Ajuste do Sped Fiscal na parametrização dos lançamentos;

 

__Passo 1__: Recuperação dos parâmetros do lançamento:

Serão recuperados os dados da parametrização \(ICT\_GRP\_INCENT\) do estabelecimento: COD\_OPER\_APUR\_E, DSC\_OPER\_APUR\_E, COD\_CLASSE\_E, COD\_AMPARO\_LEGAL\_E, COD\_SUB\_ITEM\_OCORR\_E, COD\_AJUSTE\_SEF\_E e__ COD\_AJUSTE\_ICMS\_E__\. 

__Passo 2__: Recuperação dos Valores de Incentivo Calculado:

O valor do incentivo a ser utilizado no lançamento, será recuperado da tabela dos incentivos calculados \(ICT\_VLR\_INCENT\), considerando os seguintes critérios:

    COD\_EMPRESA 🡪 código da Empresa do login 

    COD\_ESTAB 🡪 código do estabelecimento selecionado 

    DAT\_APURACAO 🡪 data de apuração do livro selecionado

    COD\_GRP\_INCENT 🡪 código do grupo de incentivo referente à série/subsérie do livro de apuração em questão 

    PERCENTUAL\_INCENT 🡪= 0 *\(esta coluna é utilizada somente p/os incentivos tipo “Indústria”\)* 

    TIPO\_INCENT 🡪 = ‘__DE__‘ \(os registros deste tipo de incentivo são identificados por ‘__DE__’\) 

    VLR\_CPRES 🡪  > 0 \(não serão considerados registros com este valor igual a zero ou nulo\)

Caso exista o valor para efetuar o lançamento, mas o campo COD\_OPER\_APUR\_E da parametrização esteja nulo, será gerada uma mensagem de erro no log de processo, e o lançamento não será gerado\.

__Passo 3__: Gravar na tabela dos lançamentos \(ICT\_AP\_DISC\_INCE\) um novo registro, com os seguintes dados:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

COD\_TIPO\_LIVRO

= “142”

Livro de Apuração Incentivada

SERIE\_LIVRO

Série do livro de apuração

SUB\_SERIE\_LIVRO

Sub\-série do livro de apuração

DAT\_APURACAO

Data final do período de apuração selecionada em tela\.

COD\_OPER\_APUR

Campo COD\_OPER\_APUR\_E da parametrização

NUM\_DISCRIMINACAO

Recuperar a maior discriminação, para os campos acima, e somar mais um\.

Este campo é um  sequencial dos lançamentos de um determinado item da apuração \(COD\_OPER\)  

VAL\_ITEM\_DISCRIMINACAO

Valor do lançamento \(campo VLR\_CPRES da tabela dos incentivos calculados\)

IND\_TIPO\_DEDUCAO

*\(sem informação\)*

Esse campo, inicialmente, não será utilizado\.

IND\_DIG\_CALCULADO

= “2”

1\-Digitado e 2\-Calculado

DSC\_ITEM\_APURADO

Campo DSC\_OPÉR\_APUR\_E da parametrização

COD\_CLASSE

Campo COD\_CLASSE\_E da parametrização

COD\_AMPARO\_LEGAL

Campo COD\_AMPARO\_LEGAL\_E da parametrização

COD\_SUB\_ITEM\_OCORR

Campo COD\_SUB\_ITEM\_OCORR\_E da parametrização

COD\_AJUSTE\_SEF

Campo COD\_AJUSTE\_SEF\_E da parametrização

__OS3148__: o código de ajuste do SEF II parametrizado, passou a ser gravado no lançamento

COD\_AJUSTE\_ICMS

Campo COD\_AJUSTE\_ICMS\_E da parametrização

Campo “Código de Ajuste \(Sped Fiscal \- Reg\. E111\)” da parametrização

__MFS21919__: o código de ajuste do Sped Fiscal, incluído na parametrização, passou a ser gravado no lançamento

__RN06__

__                                                 Crédito presumido – Central de Distribuição \(Saídas\)                                              __

*Obs: O incentivo da Central de Distribuição é o único que pode gerar dois tipos de lançamentos, um referente às operações de entrada, e outro às operações de saída\. Para efetuar o lançamento do CP das Entradas, são utilizados os parâmetros do quadro “Parâmetros p/o Lançamento do Crédito Presumido – Entradas \(Central de Distribuição\)”, e para o lançamento do CP das Saídas, são utilizados os parâmetros do quadro “Parâmetros p/o Lançamento do Crédito Presumido”\. Para maior detalhamento das regras, a RN05 define o lançamento referente às entradas, e a RN06 o referente às saídas\.*

Origem dos dados do lançamento:

\- Parametrização do menu “Parâmetros > __Grupos de Incentivo__”, campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido”

\- Tabela do Valor dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

__Para cada Estabelecimento e Livro de Apuração \(Série\-Subsérie\) selecionado em tela__:

 

Alteração da __OS3148__: inclusão do código de Ajuste do SEF II na parametrização dos lançamentos;

Alteração da __MFS21919__: inclusão do código de Ajuste do Sped Fiscal na parametrização dos lançamentos;

 

__Passo 1__: Recuperação dos parâmetros do lançamento:

Serão recuperados os dados da parametrização \(ICT\_GRP\_INCENT\) do estabelecimento: COD\_OPER\_APUR, DSC\_OPER\_APUR, COD\_CLASSE, COD\_AMPARO\_LEGAL, COD\_SUB\_ITEM\_OCORR, COD\_AJUSTE\_SEF e__ COD\_AJUSTE\_ICMS\.__ 

__Passo 2__: Recuperação dos Valores de Incentivo Calculado:

O valor do incentivo a ser utilizado no lançamento, será recuperado da tabela dos incentivos calculados \(ICT\_VLR\_INCENT\), considerando os seguintes critérios:

    COD\_EMPRESA 🡪 código da Empresa do login 

    COD\_ESTAB 🡪 código do estabelecimento selecionado 

    DAT\_APURACAO 🡪 data de apuração do livro selecionado

    COD\_GRP\_INCENT 🡪 código do grupo de incentivo referente à série/subsérie do livro de apuração em questão 

    PERCENTUAL\_INCENT 🡪= 0 *\(esta coluna é utilizada somente p/os incentivos tipo “Indústria”\)* 

    TIPO\_INCENT 🡪 = ‘__DS__‘ \(os registros deste tipo de incentivo são identificados por ‘__DS__’\) 

    VLR\_CPRES 🡪  > 0 \(não serão considerados registros com este valor igual a zero ou nulo\)

Caso exista o valor para efetuar o lançamento, mas o campo COD\_OPER\_APUR da parametrização esteja nulo, será gerada uma mensagem de erro no log de processo, e o lançamento não será gerado\.

__Passo 3__: Gravar na tabela dos lançamentos \(ICT\_AP\_DISC\_INCE\) um novo registro, com os seguintes dados:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

COD\_TIPO\_LIVRO

= “142”

Livro de Apuração Incentivada

SERIE\_LIVRO

Série do livro de apuração

SUB\_SERIE\_LIVRO

Sub\-série do livro de apuração

DAT\_APURACAO

Data final do período de apuração selecionada em tela\.

COD\_OPER\_APUR

Campo COD\_OPER\_APUR\_E da parametrização

NUM\_DISCRIMINACAO

Recuperar a maior discriminação, para os campos acima, e somar mais um\.

Este campo é um  sequencial dos lançamentos de um determinado item da apuração \(COD\_OPER\)  

VAL\_ITEM\_DISCRIMINACAO

Valor do lançamento \(campo VLR\_CPRES da tabela dos incentivos calculados\)

IND\_TIPO\_DEDUCAO

*\(sem informação\)*

Esse campo, inicialmente, não será utilizado\.

IND\_DIG\_CALCULADO

= “2”

1\-Digitado e 2\-Calculado

DSC\_ITEM\_APURADO

Campo DSC\_OPÉR\_APUR da parametrização

COD\_CLASSE

Campo COD\_CLASSE da parametrização

COD\_AMPARO\_LEGAL

Campo COD\_AMPARO\_LEGAL da parametrização

COD\_SUB\_ITEM\_OCORR

Campo COD\_SUB\_ITEM\_OCORR da parametrização

COD\_AJUSTE\_SEF

Campo COD\_AJUSTE\_SEF da parametrização

__OS3148__: o código de ajuste do SEF II parametrizado, passou a ser gravado no lançamento

COD\_AJUSTE\_ICMS

Campo COD\_AJUSTE\_ICMS da parametrização

Campo “Código de Ajuste \(Sped Fiscal \- Reg\. E111\)” da parametrização

__MFS21919__: o código de ajuste do Sped Fiscal, incluído na parametrização, passou a ser gravado no lançamento

__RN07__

__                                                                  Estorno Calculado \- Indústria                                              __

Origem dos dados do lançamento:

\- Parametrização do menu “Parâmetros > __Grupos de Incentivo__”, campos 🡪 “Parâmetros p/o Lançamento do Crédito Presumido”

\- Tabela do Valor dos Incentivos Calculados \(ICT\_VLR\_INCENT\)

__Para cada Estabelecimento e Livro de Apuração \(Série\-Subsérie\) selecionado em tela__:

 

Alteração da __OS3148__: inclusão do código de Ajuste do SEF II na parametrização dos lançamentos;

Alteração da __MFS21919__: inclusão do código de Ajuste do Sped Fiscal na parametrização dos lançamentos;

 

__Passo 1__: Recuperação dos parâmetros do lançamento:

Serão recuperados os dados da parametrização \(ICT\_GRP\_INCENT\) do estabelecimento: COD\_OPER\_APUR\_EST, DSC\_OPER\_APUR\_EST, COD\_CLASSE\_EST, COD\_AMP\_LEGAL\_EST, COD\_SUBIT\_OCORR\_EST, COD\_AJUSTE\_SEF\_EST e__ COD\_AJUSTE\_ICMS\_EST__\. 

__Passo 2__: Recuperação dos Valores de Estorno Calculado:

O valor do estorno a ser utilizado no lançamento, será recuperado da tabela dos incentivos calculados \(ICT\_VLR\_INCENT\), considerando os seguintes critérios:

    COD\_EMPRESA 🡪 código da Empresa do login 

    COD\_ESTAB 🡪 código do estabelecimento selecionado 

    DAT\_APURACAO 🡪 data de apuração do livro selecionado

    COD\_GRP\_INCENT 🡪 código do grupo de incentivo referente à série/subsérie do livro de apuração em questão 

    PERCENTUAL\_INCENT 🡪 percentual de incentivo referente à série/subsérie do livro de apuração em questão 

    TIPO\_INCENT 🡪 = ‘__C__’  \(os registros deste tipo de incentivo são identificados por ‘__C__’\) 

    VLR\_ESTORNO 🡪  > 0 \(não serão considerados registros com este valor igual a zero ou nulo\)

Caso exista o valor para efetuar o lançamento, mas o campo COD\_OPER\_APUR\_EST da parametrização esteja nulo, será gerada uma mensagem de erro no log de processo, e o lançamento não será gerado\.

*Obs: Este é o único tipo de lançamento que utiliza o campo VLR\_ESTORNO, ao invés do VLR\_CPRES\. Cada linha da tabela ICT\_VLR\_INCENT com TIPO\_INCENT = “*__*C*__*” terá valor de crédito presumido \(*__*VLR\_CPRES*__*\), valor de estorno \(*__*VLR\_ESTORNO*__*\),*

* ou nenhum dos dois \(nunca ocorrerá crédito e estorno simultaneamente\)\.*

__Passo 3__: Gravar na tabela dos lançamentos \(ICT\_AP\_DISC\_INCE\) um novo registro, com os seguintes dados:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

COD\_TIPO\_LIVRO

= “142”

Livro de Apuração Incentivada

SERIE\_LIVRO

Série do livro de apuração

SUB\_SERIE\_LIVRO

Sub\-série do livro de apuração

DAT\_APURACAO

Data final do período de apuração selecionada em tela\.

COD\_OPER\_APUR

Campo COD\_OPER\_APUR\_EST da parametrização

NUM\_DISCRIMINACAO

Recuperar a maior discriminação, para os campos acima, e somar mais um\.

Este campo é um  sequencial dos lançamentos de um determinado item da apuração \(COD\_OPER\)  

VAL\_ITEM\_DISCRIMINACAO

Valor do lançamento \(campo VLR\_ESTORNO da tabela dos incentivos calculados\)

IND\_TIPO\_DEDUCAO

*\(sem informação\)*

Esse campo, inicialmente, não será utilizado\.

IND\_DIG\_CALCULADO

= “2”

1\-Digitado e 2\-Calculado

DSC\_ITEM\_APURADO

Campo DSC\_OPÉR\_APUR\_EST da parametrização

COD\_CLASSE

Campo COD\_CLASSE\_EST da parametrização

COD\_AMPARO\_LEGAL

Campo COD\_AMP\_LEGAL\_EST da parametrização

COD\_SUB\_ITEM\_OCORR

Campo COD\_SUBIT\_OCORR\_EST da parametrização

COD\_AJUSTE\_SEF

Campo COD\_AJUSTE\_SEF\_EST da parametrização

__OS3148__: o código de ajuste do SEF II parametrizado, passou a ser gravado no lançamento

COD\_AJUSTE\_ICMS

Campo COD\_AJUSTE\_ICMS\_EST da parametrização

Campo “Código de Ajuste \(Sped Fiscal \- Reg\. E111\)” da parametrização

__MFS21919__: o código de ajuste do Sped Fiscal, incluído na parametrização, passou a ser gravado no lançamento

	

= = = = = = = =  

