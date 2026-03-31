# MTZ-Ressarc-RS-Geracao_Movimentos_Entradas_Varejista

- **Fonte:** MTZ-Ressarc-RS-Geracao_Movimentos_Entradas_Varejista.docx
- **Modificado:** 2024-01-22
- **Tamanho:** 103 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 048/2018\) 

Geração dos Movimentos – Entradas Contribuinte Varejista 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração🡪 IN\-RE 048/2018 🡪 Geração dos Movimentos \(opção “Gerar Entradas”\)

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS28004__

Liliane Videira Assaf

Geração dos movimentos das entradas para Varejistas\. Ver marcações em verde\.

01/08/2019

__MFS47349__

Liliane Videira Assaf

Tratamento de Produtos Associados na geração dos movimentos

30/03/2021

Sumário

[1\.	Introdução	2](#_Toc18676483)

[2\.	Recuperação dos Dados e Processamento	3](#_Toc18676484)

[3\.	Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\)	5](#_Toc18676485)

[4\.	Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(registro 1921\)	11](#_Toc18676486)

[5\.	Gravação dos Dados na Tabela de Subapuração do RS \(registro 1920\)	12](#_Toc18676487)

[6\.	Gravação dos Dados na Tabela de Controle da Execução das Gerações	16](#_Toc18676488)

# <a id="_Toc18676483"></a>Introdução 

A geração dos movimentos de entrada para contribuintes varejistas é uma das gerações que compõe o processo de Geração dos Movimentos, responsável por calcular a Subapuração RS\.

A Geração dos Movimentos está definida pelo seguinte conjunto de documentos:

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx

Documento principal que referencia todos os outros documentos\.

Contém especificação de tela da geração, validações gerais e a regra de disparo de cada tipo de geração \(entradas, saídas para consumidor final\)\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\.docx

Documento específico da geração dos movimentos de Saída para Consumidor Final deste Estado\. 

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\.docx

Documento específico da geração dos movimentos de Saída para outras UF’s, Isentas ou Não Tributadas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\.docx

Documento específico da geração dos movimentos de Entrada para contribuintes Varejistas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Nao\_Varejista\.docx

Documento específico da geração dos movimentos de Entrada para contribuintes não Varejistas\.

__MFS81764__

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\.docx

Documento específico da geração dos créditos das mercadorias em estoque\. Aplicada a contribuintes Varejistas e Não Varejistas\.

__MFS81804__

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\.docx

Documento específico da geração dos movimentos de Devolução das Saídas de mercadorias destinadas a consumidor final\. Aplicada a contribuintes Varejistas e Não Varejistas\.

Esta geração será executada caso o contribuinte seja Varejista e a opção “Gerar entradas” seja selecionada na tela de geração\. Veja o tópico 4 do documento principal da Geração dos Movimentos \(MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx\)\.

__\[MFS47349\]__

__Quanto a Parametrização de Produtos Associados__:

A recuperação dos movimentos de entradas e saídas é feita considerando o produto Principal seus os produtos Associados, definidos na Parametrização de Produtos, opção Por Código\. 

No relatório de conferência, os documentos fiscais são apresentados com seus respectivos produtos e agrupados em nome do Produto Principal\. 

No Sped Fiscal, o documento fiscal é apresentado no registo 1923 com o produto que de fato está escriturado na nota, não havendo forma de demonstrar a relação do Produto Principal com os Produtos Associados\. Esta relação só é possível de ser observada dentro do módulo Ressarcimento ICMS\-ST RS, através dos relatórios de conferência dos movimentos\.

# <a id="_Toc350763252"></a><a id="_Toc18676484"></a>Recuperação dos Dados e Processamento

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- Parametrização dos Dados Iniciais

                                  \- SAFX07 / SAFX08 \- Tabelas dos Documentos Fiscais;

O objetivo desta geração é recuperar toda movimentação das entradas dos produtos sujeitos ao ICMS\-ST e gerar um lançamento na Subapuração RS, carregando todo conjunto de tabelas da Subapuração, base para a geração dos registros 1920, 1921 e 1923 do SPED FISCAL\.

Tabelas que compõe a Subapuração: 

- Subapuração RS \(registro 1920\)
- Ajustes da Subapuração \(registro 1921\) 
- Identificação dos Documentos fiscais \(registro 1923\)

Na tabela de Subapuração \(registro 1920\) será gravado o campo de __Outros Créditos __com o total da movimentação de Entradas\.  Na tabela de Ajustes da Subapuração \(registro 1921\) um lançamento é realizado com o total da movimentação de Entradas e código de ajuste especificado na IN048/2018, que será parametrizado na tela de Dados Iniciais\. Na tabela de Identificação dos Documentos fiscais \(registro 1923\) são gravados os documentos fiscais que foram recuperados neste processo\.

Obs\.: 

1. A notas de devolução __NÃO__ são consideradas nesta geração, pois segundo Art\. 25 do Decreto 37699/97 – Livro III, há uma forma particular de tratamento que não seja através da Subapuração\. Esta geração não irá descartar as notas de devolução\.  Cabe ao usuário não parametrizar os CFOP’s relativos à devolução, para que as mesmas não sejam consideradas\.

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Somente notas *não canceladas*;

\- Somente notas *com itens*;

\- O produto do item deve constar na parametrização do menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, seu NCM deve estar parametrizado

  no menu “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\. 

  Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

  A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

 No caso da parametrização por Código, será verificado se o produto da nota consta como produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\), ou como “produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\) \[__MFS47349\]__\.   

\- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros 🡪 Operações*” para a seguinte

   operação:

- Entrada com Substituicao Tributaria \(código parâmetro __746__\)

__Gravação dos Resultados da Geração:__

Os movimentos recuperados são armazenados em três tabelas que serão utilizadas posteriormente para geração dos registros 1920, 1921, 1923 do Sped Fiscal:

- Tabela de Subapuração do RS \(registro 1920\) \- __ICT\_SUB\_APURACAO\_RS__
- Tabela dos Ajustes da Subapuração do RS \(registro 1921\) \- __ITEM\_APURAC\_SUBRS__
- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\) \- __ITEM\_APURAC\_SUBRS\_AJUSTE__

Cada documento fiscal recuperado é gravando na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE__ relacionados ao lançamento e Subapuração parametrizados em Dados Iniciais\. 

Os documentos ficais recuperados são consolidados e geram um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, e atualizados na ICT\_SUB\_APURACAO\_RS, recalculando a Subapuração RS\.

O Resultado desta geração pode ser conferido através do Relatório de Conferência disponível no módulo, e na emissão da Subapuração RS\.

# <a id="_Toc18676485"></a>Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\)

Os documentos fiscais recuperados da SAX07 / SAFX08 serão gravados__ item a item__, na tabela conforme definido a seguir\.

__Tabela ITEM\_APURAC\_SUBRS\_AJUSTE__

Esta tabela contém os documentos fiscais que compuseram os lançamentos \(Ajustes\) da Subapuração de um estabelecimento e período\. 

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__PK__

__Identificador do Registro__

ID\_REG\_AJUSTE

Sequencial único a ser gerado na inclusão do registro\. 

Chave física de identificação do registro\.

__UK__

__Código da empresa__

COD\_EMPRESA

Código da empresa \(SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento informado na tela de geração\.

Chave lógica de identificação do registro\.

__UK__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

Chave lógica de identificação do registro\.

__UK__

__Código do Livro __

COD\_TIPO\_LIVRO

Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

    Gravar o código ‘165’

Senão

    Gravar o código ‘108’\.

Chave lógica de identificação do registro\.

__UK__

__Identificador da Subapuração__

IND\_SUB\_APUR

Recuperar o código da SUBAPURAÇÃO cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e estabelecimento foco da geração\.

Chave lógica de identificação do registro\.

__UK__

__Operação da Apuração__

COD\_OPER\_APUR

Recuperar o Código da Operação da Apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e estabelecimento foco da geração\.

Considerar o Item da Apuração do “Lançamento de Outros Créditos para Entradas de Mercadorias”\.

Mesmo código gravado para o registro pai na tabela Ajustes da Subapuração __ITEM\_APURAC\_SUBRS__\.

Chave lógica de identificação do registro\.

__UK__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Mesmo sequencial gravado para o registro pai na tabela Ajustes da Subapuração __ITEM\_APURAC\_SUBRS__\.

Chave lógica de identificação do registro\.

__UK__

__Código do Estabelecimento de Origem__

COD\_ESTAB\_ORIG

Código do estabelecimento do documento fiscal de entrada \(SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Data Fiscal__

DATA\_FISCAL

Preencher com a Data Fiscal do documento fiscal de entrada \(SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Entrada/Saída__

MOVTO\_E\_S

Preencher com o indicador do Movimento Entrada/Saída do documento fiscal de entrada \(campo “03\-Movimento Entrada/Saída” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Normal/Devolução__

NORM\_DEV

Preencher com o indicador de Normal ou Devolução do documento fiscal de entrada \(campo “04 \- Normal ou Devolução” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Tipo do Documento__

IDENT\_DOCTO

Preencher com o Identificador do Tipo do Documento do documento fiscal de entrada \(campo “05\-Tipo do Documento” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Pessoa Fis/Jur__

*\(ref ao campo 02 do registro 1923\)*

IDENT\_FIS\_JUR

Preencher com o Identificador da Pessoa fis/jur do documento fiscal de entrada \(campos 06 e 07 da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Número do Documento__

*\(campo 06 do registro 1923\)*

NUM\_DOCFIS

Preencher com o Número do documento fiscal de entrada \(campo “08\-Número do Documento” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Série do Documento__

*\(campo 04 do registro 1923\)*

SERIE\_DOCFIS

Preencher com a Série do documento fiscal de entrada \(campo “09\-Série do Documento” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Subsérie do Documento__

*\(campo 05 do registro 1923\)*

SUB\_SERIE\_DOCFIS

Preencher com a Subsérie do documento fiscal de entrada \(campo “10\-Subsérie do Documento” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Identificador do Item__

DISCRI\_ITEM

Campo identificador do item de mercadoria do documento fiscal de entrada \(DISCR\_ITEM da X08\_ITENS\_MERC\)\.

Chave lógica de identificação do registro\.

__UK__

__Identificador do Registro Referenciado__

ID\_REG\_AJUSTE\_REF

Não preencher\.

Este campo será preenchido apenas na Geração das Entradas para Não Varejista\.

__Número do Item__

NUM\_ITEM

Número do item de mercadoria do documento fiscal de entrada \(campo “18\-Item Nota Fiscal” da SAFX08\)

__Núm Doc Fiscal Referência__

NUM\_DOCFIS\_REF

Não preencher\. 

Este campo será preenchido apenas para notas de saída para consumidor final\.

__Série Doc Fiscal Referência__

SERIE\_DOCFIS\_REF

Não preencher\.

Este campo será preenchido apenas para notas de saída para consumidor final\.

__Subsérie Doc Fiscal Referência__

S\_SER\_DOCFIS\_REF

Não preencher\.

Este campo será preenchido apenas para notas de saída para consumidor final\.

__Data Doc Fiscal Referência__

DAT\_DI

Não preencher\.

Este campo será preenchido apenas para notas de saída para consumidor final\.

__Modelo Documento__

COD\_MODELO

Preencher com o campo Modelo do documento \(campo 13 da SAFX07\)\.

__Código Fiscal__

COD\_CFOP

Preencher com o Código CFOP do item de mercadoria \(campo 22 da SAFX08\)

__Natureza da Operação__

COD\_NATUREZA\_OP

Preencher com o Código da Natureza de Operação do item de mercadoria \(campo 23 da SAFX08\)

__Produto da Nota \(grupo, ind, código\)__

GRUPO\_PRODUTO,

IND\_PRODUTO,

COD\_PRODUTO,

DSC\_PRODUTO

Preencher com o produto do item de mercadoria da nota de entrada \(campos 13 e 14 da SAFX08\)

\[__MFS47349\]__

Obs: No caso da parametrização do produto “Por Código” o produto da nota pode ser o Produto Principal ou um Produto Associado\.

__Produto Principal__

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

\[__MFS47349\]__

Preenchimento depende da Parametrização do Produto:

- Caso o produto do item da nota de entrada tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\), então: 

Preencher esse campo com o __Produto Principal__ \(grupo, indicador e código\)\.

- Caso o produto do item da nota de entrada tenha sido parametrizado por NCM ou por CEST \(menu Parâmetros 🡪 Produtos 🡪 Por NCM ou Por CEST\), então: 

Preencher esse campo com o __Produto do Item__ de mercadoria da nota de entrada \(campos 13 e 14 da SAFX08\)

__Medida da Origem__

GRUPO\_MEDIDA\_ORIG,

COD\_MEDIDA\_ORIG

Não preencher\.

__Medida de Destino__

GRUPO\_MEDIDA\_DEST COD\_MEDIDA\_DEST,

Preencher com a unidade de __medida do Produto__ \(campo 14 da SAFX2013\)\.

\[__MFS47349\]__

Preenchimento depende da Parametrização do Produto:

- Caso o produto do item da nota de entrada tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\), então: 

Preencher com a unidade de medida do __Produto Principal__ \(campo 14 da SAFX2013\)\.

- Caso o produto do item da nota de entrada tenha sido parametrizado por NCM ou por CEST \(menu Parâmetros 🡪 Produtos 🡪 Por NCM ou Por CEST\), então: 

Preencher com a unidade de medida do __Produto do item__ de mercadoria da nota de entrada \(campo 14 da SAFX2013\)

Regra Prática: unidade de medida do produto gravado no campo Produto Principal

__Fator de Conversão__

FAT\_CONV

Não preencher\.

__Quantidade do item __

QTDE\_ITEM

Não preencher\.

__Quantidade Convertida do item__

QTDE\_CONV

Não preencher\.

__% Redução BC__

PRC\_REDUCAO\_BC

Não preencher\.

Este campo será preenchido apenas na geração das notas de saída para consumidor final\.

__Alíquota Interna__

ALIQ\_INTERNA

Não preencher\.

Este campo será preenchido apenas na geração das notas de saída para consumidor final\.

__Alíquota FCP__

ALIQ\_FCP

Não preencher\.

Este campo será preenchido apenas na geração das notas de saída para consumidor final\.

__Valor Contábil do Item__

VLR\_CONTAB\_ITEM

Valor Contábil do Item \(campo “64\-Valor Contábil do Item” da SAFX08\)\.

__Valor da Base de Calculo__

VLR\_BASE\_CALC

Não preencher\.

Este campo será preenchido apenas na geração das notas de saída para consumidor final\.

__Valor do ICMS__

VLR\_ICMS

__Valor do ICMS:__

O valor do ICMS a ser utilizado depende do campo que estiver preenchido na SAFX08, uma vez que a operação pode ter o ICMS escriturado ou não escriturado, e nos dois casos o valor do ICMS precisa ser considerado\.

Assim, será utilizado um dos campos descritos a seguir, utilizando o campo que estiver preenchido, na prioridade apresentada:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

__Obs__: As regras de preenchimento dos campos Valor do ICMS, Valor do ICMS\-ST e Valor do ST FECEP estão baseadas na regra do campo “__Valor Total ICMS – Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP \(ver MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor do ICMS\-ST__

VLR\_ICMS\_ST

__Valor do ICMS\-ST:__

O valor do ICMS\-ST a ser utilizado depende do campo que estiver preenchido na SAFX08, uma vez que a operação pode ter o ICMS\-ST escriturado ou não escriturado, e nos dois casos o valor do ICMS\-ST precisa ser considerado\.

Assim, será utilizado apenas um dos campos descritos a seguir, utilizando o campo que estiver preenchido, na prioridade apresentada:

Campo “52\-Valor ICMS Substituição Tributária”,                 se preenchido, ou

   Campo “145\-Valor de ICMS\-ST não Escriturado”,            se preenchido, ou

       Campo “133\-ICMS\-ST Não Escriturado”,                      se preenchido, ou 

           Campo “107\-Valor Carga Tributária Origem”,             se preenchido\.

*OBS: Esta regra para obter o valor do ICMS\-ST é a mesma utilizada na Portaria CAT 158 \(no preenchimento do campo” Valor Unitário da Base de Cálculo do ICMS\-ST da Entrada” do C176, Sped Fiscal\)\. Sendo que, para o C176 utilizamos os campos referentes ao valor da base de cálculo, ao invés do valor do imposto\. Ou seja, lá são utilizados os campos 61, 144 e 106, ao invés dos campos 52, 145 e 107\. *

__Obs__: As regras de preenchimento dos campos Valor do ICMS, Valor do ICMS\-ST e Valor do ST FECEP estão baseadas na regra do campo “__Valor Total ICMS – Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP \(ver MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor do ICMS\-ST FECEP__

VLR\_FECP\_ICMS\_ST

Campo “140\-FECEP ICMS\-ST” da SAFX08;

__Obs__: As regras de preenchimento dos campos Valor do ICMS, Valor do ICMS\-ST e Valor do ST FECEP estão baseadas na regra do campo “__Valor Total ICMS – Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP \(ver MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor Unitário de ST __

VLR\_UNIT

Não preencher\.

Este campo será preenchido apenas na Geração das Entradas para Não Varejistas\.

__Valor do Ajuste__

*\(campo 09 do registro 1923\)*

VLR\_AJUSTE

Calcular o valor do ajuste considerando os procedimentos abaixo:

Valor do Ajuste =  \[Valor do ICMS  \+  Valor do ICMS\-ST  \+  Valor do ICMS\-ST FECEP\] 

__Obs__: Regra semelhante ao cálculo do valor de confronto do campo “__Valor Confronto \- ICMS Efetivo Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP, \(ver MTZ\-Ressarc\-SP\-Calculo\_Vlr\_Confronto\_Saidas\.doc\)\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “3”\.

__3__ – lançamento gerado via processo de geração das entradas\.

__Número do Processo__

NUM\_PROCESSO

Preencher com o número do processo da geração\.

# <a id="_Toc18676486"></a>Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(registro 1921\)

Os documentos ficais recuperados da SAX07 / SAFX08 __serão consolidados__ e geram um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

__Tabela ITEM\_APURAC\_SUBRS__

Esta tabela contém os lançamentos \(Ajustes\) da Subapuração de um estabelecimento e período\. 

Cada tipo de geração que compõe a Geração de Movimento \(entradas, saídas\), produz um lançamento em uma das operações da Subapuração \(002\- Outros Débitos, 003 – Estorno Crédito, 006 – Outros Créditos, 007 – Estorno Débito\)\. Os parâmetros necessários para esses lançamentos \(código de operação, descrição e código de ajuste\) são definidos na tela de parametrização dos Dados Iniciais\.

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa \(SAFX07\)

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento \(SAFX07\) 

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Se a opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

    Gravar o código ‘165’

Senão

    Gravar o código ‘108’

__\*\*\*__

__Identificador da Subapuração__

IND\_SUB\_APUR

Recuperar o código da SUBAPURAÇÃO cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e estabelecimento foco da geração\.

__\*\*\*__

__Operação da Apuração__

COD\_OPER\_APUR

Recuperar o Código da Operação da Apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e estabelecimento foco da geração\.

Considerar o Item da Apuração do “Lançamento de Outros Créditos para Entradas de Mercadorias”\.

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Subapuração/Operação da Apuração\. 

Ou seja, recuperar o próximo número da seguencia de lançamentos da Subapuração/operação da Apuração que está sendo gerada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração\.

__Valor do Lançamento__

*\(campo 04 do registro 1921\)*

VAL\_ITEM\_DISCRIM

Somatório dos __Valores dos Ajustes __calculados para os documentos e gravados na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE\.__

__Descrição do Lançamento__

*\(campo 03 do registro 1921\)*

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Considerar a Descrição do “Lançamento de Outros Créditos para Entradas de Mercadorias”\.

__Código do Ajuste ICMS__

*\(campo 02 do registro 1921\)*

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Considerar o Código de Ajuste Sped Fiscal do “Lançamento de Outros Créditos para Entradas de Mercadorias”\.

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com “2”\.

Este valor signfica que o lançamento possui documentos associados, que estão gravados na tabela ITEM\_APURAC\_SUBRS\_AJUSTE\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “3”\.

__3__ – lançamento gerado via processo de geração das entradas\.

# <a id="_Toc18676487"></a>Gravação dos Dados na Tabela de Subapuração do RS \(registro 1920\)

<a id="_Hlk508706613"></a>

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, e atualizados na ICT\_SUB\_APURACAO\_RS, recalculando a Subapuração\.

__Tabela ICT\_SUB\_APURACAO\_RS__

Esta tabela contém os totais da Subapuração de um estabelecimento e período\. 

Os valores da Subapuração são resultantes das gerações dos movimentos das entradas e saídas disponíveis no módulo de Ressarcimento RS\. 

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa \(SAFX07\)

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento \(SAFX07\) 

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

<a id="OLE_LINK22"></a>Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

    Gravar o código ‘165’

Senão

    Gravar o código ‘108’

__\*\*\*__

__Identificador da Subapuração__

IND\_SUB\_APUR

Recuperar o código da SUBAPURAÇÃO cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para o estabelecimento foco da geração\.

__Valor total dos débitos por “Saídas e prestações com débito do imposto”__

*\(campo 02 do registro 1920\)*

VLR\_TOT\_DEB

Gravar zero\.

Este campo __sempre__ ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\. 

__Valor total de “Ajustes a débito”__

*\(campo 03 do registro 1920\)*

VLR\_OUT\_DEB

Este campo contém o resultado somatório dos  lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__002’__ – Outros Débitos\.

__OBS__: Conforme parametrização dos Dados Iniciais, ‘002’ é o código de operação destinado ao lançamento resultante do processo de Geração das Saídas para Consumidor Final\.

__Valor total de Ajustes “Estornos de créditos”__

*\(campo 04 do registro 1920\)*

VLR\_ESTORNO\_CRED

Este campo contém o resultado somatório dos  lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__003’__ – Estorno de Créditos\.

__OBS__: Conforme parametrização dos Dados Iniciais, ‘003’ é o código de operação destinado ao lançamento resultante do processo de Geração das Saídas para Outras UF’s\. 

     

__Valor total dos créditos por “Entradas e aquisições com crédito do imposto__

*\(campo 05 do registro 1920\)*

VLR\_TOT\_CRED

Gravar zero\.

Este campo __sempre__ ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

__Valor total de “Ajustes a crédito”__

*\(campo 06 do registro 1920\)*

VLR\_OUT\_CRED

Este campo contém o resultado somatório dos  lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__006’__ – Outros Créditos\.

__OBS__: Conforme parametrização dos Dados Iniciais, o ‘006’ é o código de operação destinado ao lançamento resultante do processo de Geração das Entradas\.

__Valor total de Ajustes “Estornos de Débitos”__

*\(campo 07 do registro 1920\)*

VLR\_ESTORNO\_DEB

Este campo contém o resultado somatório dos  lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__007’__ – Estorno de Débito\.

__OBS__: Este campo sempre ficará zerado, pois nenhuma das gerações existentes hoje no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

__Valor total de “Saldo credor do período anterior”__

*\(campo 08 do registro 1920\)*

VLR\_SALDO\_CRED

Gravar zero\.

Este campo sempre ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

__Valor do saldo devedor apurado__

*\(campo 09 do registro 1920\)*

VLR\_SLD\_APURADO

Se \(VLR\_TOT\_DEB   \+  VLR\_OUT\_DEB   \+   VLR\_ESTORNO\_CRED\) \-

     \(VLR\_TOT\_CRED \+  VLR\_OUT\_CRED \+  VLR\_ESTORNO\_DEB \+  VLR\_SALDO\_CRED\) __>__ 0 Então

       Gravar o campo VLR\_SLD\_APURADO com o resultado da expressão:

        \(VLR\_TOT\_DEB    \+  VLR\_OUT\_DEB   \+ VLR\_ESTORNO\_CRED\) \-

        \(VLR\_TOT\_CRED \+ VLR\_OUT\_CRED \+ VLR\_ESTORNO\_DEB \+ VLR\_SALDO\_CRED\)

Sentão

       Gravar o campo VLR\_SLD\_APURADO com zero\.

__Valor total de “Deduções”__

*\(campo 10 do registro 1920\)*

VLR\_TOT\_DED

Este campo contém o resultado somatório dos lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__012’__ – Deduções\.

__OBS__: Conforme parametrização dos Dados Iniciais, o ‘012’ é o código de operação destinado ao lançamento resultante do processo de Transferência entre apurações\.

__Valor total de "ICMS a recolher \(09\-10\)__

*\(campo 11 do registro 1920\)*

VLR\_ICMS\_RECOLHER

Se VLR\_SLD\_APURADO > 0, Então:\.

    Se VLR\_SLD\_APURADO \- VLR\_TOT\_DED > 0 Então:

          Gravar o campo VLR\_ICMS\_RECOLHER com o resultado da expressão:

          VLR\_SLD\_APURADO \- VLR\_TOT\_DED

    Senão

         Gravar o campo VLR\_ICMS\_RECOLHER com zero\.

Senão 

     Gravar o campo VLR\_ICMS\_RECOLHER com zero\.

__Valor total de “Saldo credor a transportar para o período seguinte”__

*\(campo 12 do registro 1920\)*

VL\_SLD\_CREDOR\_TRANSP

Se \(VLR\_TOT\_DEB   \+  VLR\_OUT\_DEB   \+   VLR\_ESTORNO\_CRED\) \-

     \(VLR\_TOT\_CRED \+  VLR\_OUT\_CRED \+  VLR\_ESTORNO\_DEB \+  VLR\_SALDO\_CRED\) __>__ 0 Então

         Gravar o campo VLR\_SLD\_CREDOR\_TRANSP com zero\.

Sentão

       Gravar o campo VLR\_SLD\_CREDOR\_TRANSP com o resultado da expressão:

        \(VLR\_TOT\_CRED \+ VLR\_OUT\_CRED \+ VLR\_ESTORNO\_DEB \+ VLR\_SALDO\_CRED\) \- 

        \(VLR\_TOT\_DEB    \+  VLR\_OUT\_DEB   \+ VLR\_ESTORNO\_CRED\) 

__Valores recolhidos ou a recolher, extraapuração\.__

*\(campo 13 do registro 1920\)*

VLR\_DEB\_ESP

Gravar zero\.

Estes campo sempre ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

# <a id="_Toc18676488"></a>Gravação dos Dados na Tabela de Controle da Execução das Gerações 

Um registro será gravado na tabela com as seguintes informações:

__Tabela CTRL\_PROC\_MSAF__

Os campos sinalizados com asterisco compõem a chave da tabela\.

create table CTRL\_PROC\_MSAF

\(

  COD\_EMPRESA      VARCHAR2\(3\) not null,

  COD\_ESTAB        VARCHAR2\(6\) not null,

  DAT\_APURACAO     DATE        not null,

  COD\_MODULO       VARCHAR2\(8\) not null, 

  COD\_GERACAO      VARCHAR2\(3\) not null, *\-\- ex: 001 \- ENTRADA, 002 \- SAIDA, 003\- SAIDA POR ECF, 004 \- CALCULO DA RESTITUICAO/COMPLEMENTO, 005 \- TRANSFERENCIA DO ICMS\-ST*

  IND\_STATUS       VARCHAR2\(1\), *\-\- ex: 0 \- sucesso, \-1 \- erro, 1 \- advertencia*

  NUM\_PROCESSO     NUMBER,

  VLR\_TOT\_GERACAO  NUMBER\(17,2\)

= = = = = =

 

