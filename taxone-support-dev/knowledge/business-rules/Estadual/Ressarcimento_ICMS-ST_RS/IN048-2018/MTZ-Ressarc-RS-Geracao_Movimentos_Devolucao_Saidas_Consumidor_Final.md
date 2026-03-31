# MTZ-Ressarc-RS-Geracao_Movimentos_Devolucao_Saidas_Consumidor_Final

- **Fonte:** MTZ-Ressarc-RS-Geracao_Movimentos_Devolucao_Saidas_Consumidor_Final.docx
- **Modificado:** 2022-03-11
- **Tamanho:** 102 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 048/2018\) 

Geração dos Movimentos – Devolução das Saídas de Mercadorias destinadas a Consumidor Final  

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração 🡪 IN\-RE 048/2018 🡪 Geração dos Movimentos \(opção “Gerar Devolução das Saídas de Mercadoria destinadas a Consumidor Final”\)

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS81804

Liliane Assaf

Tratamento das Devoluções de Saídas de Mercadorias destinadas a Consumidor Final

07/03/2022

Sumário

[1\.	Introdução	1](#_Toc97913259)

[4	Recuperação dos Dados e Processamento	1](#_Toc97913260)

[2\.1 – Recuperação dos Dados e Processamento	1](#_Toc97913261)

[2\.2 – Gravação dos Dados	1](#_Toc97913262)

[3 – Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\)	1](#_Toc97913263)

[4	\- Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(registro 1921\)	1](#_Toc97913264)

[5	Gravação dos Dados na Tabela de Subapuração do RS \(registro 1920\)	1](#_Toc97913265)

[6	Gravação dos Dados na Tabela de Controle da Execução das Gerações	1](#_Toc97913266)

# <a id="_Toc97913259"></a>Introdução 

A geração dos movimentos de devolução de saídas é uma das gerações que compõe o processo de Geração dos Movimentos, responsável por calcular a Subapuração RS\.

A Geração dos Movimentos está definida pelo seguinte conjunto de documentos:

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx

Documento principal que referencia todos os outros documentos\.

Contém especificação de tela da geração, validações gerais e a regra de disparo para cada tipo de geração \(entradas, saídas para consumidor final\)\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\.docx

Documento específico da geração dos movimentos de Saída para Consumidor Final deste Estado\.  Aplicada a contribuintes Varejistas e Não Varejistas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_Ufs\.docx

Documento específico da geração dos movimentos de Saída para outras UF’s, Isentas ou Não Tributadas\. Aplicada a contribuintes Varejistas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\.docx

Documento específico da geração dos movimentos de Entrada sujeita a Substituição Tributária\. Aplicada a contribuintes Varejistas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Nao\_Varejista

Documento específico da geração dos movimentos de Entrada sujeita a Substituição Tributária\. Aplicada a contribuintes Não Varejistas\.

__MFS81764__

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\.docx

Documento específico da geração dos créditos das mercadorias em estoque\. Aplicada a contribuintes Varejistas e Não Varejistas\.

__MFS81804__

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\.docx

Documento específico da geração dos movimentos de Devolução das Saídas de mercadorias destinadas a consumidor final\. Aplicada a contribuintes Varejistas e Não Varejistas\.

Esta geração será executada caso o contribuinte seja __Varejista__ ou __Não Varejista__ e a opção “Gerar Devolução das Saídas de Mercadoria destinadas a Consumidor Final” seja selecionada na tela de geração\. 

__Quanto a Parametrização de Produtos Associados__:

A recuperação dos movimentos de entradas e saídas é feita considerando o produto Principal seus os produtos Associados, definidos na Parametrização de Produtos, opção Por Código\. 

No relatório de conferência, os documentos fiscais são apresentados com seus respectivos produtos e agrupados em nome do Produto Principal\. 

No Sped Fiscal, o documento fiscal é apresentado no registo 1923 com o produto que de fato está escriturado na nota, não havendo forma de demonstrar a relação do Produto Principal com os Produtos Associados\. Esta relação só é possível de ser observada dentro do módulo Ressarcimento ICMS\-ST RS, através dos relatórios de conferência dos movimentos\.

# <a id="_Toc97913260"></a>Recuperação dos Dados e Processamento

O objetivo desta geração é recuperar toda movimentação das devoluções de saídas e gerar um lançamento em Outros de Crédito na Subapuração, carregando todo conjunto de tabelas da Subapuração, base para a geração dos registros 1920, 1921 e 1923 do SPED FISCAL\.

Tabelas que compõe a Subapuração: 

- Subapuração RS \(registro 1920\)
- Ajustes da Subapuração \(registro 1921\) 
- Identificação dos Documentos fiscais \(registro 1923\)

Na tabela de Subapuração \(registro 1920\) será gravado o campo de Outros Créditos com o total da movimentação de Devoluçoes de Saídas\.  Na tabela de Ajustes da Subapuração \(registro 1921\) um lançamento é realizado com o total da movimentação de Devolução de Saída e código de ajuste específicado na IN048/2018, que será parametrizado na tela de Dados Iniciais\. Na tabela de Identificação dos Documentos fiscais \(registro 1923\) são gravados os documentos fiscais de devolução de saída que foram recuperados neste processo\.

 Na geração da devolução da saída da IN\-87/20 consideramos as notas de saída objeto da devolução, pois o C181 solicita tal informação e o cálculo do valor do ressarcimento/complemento é realizado por nota\. Na geração da IN\-48/18 não há necessidade de recuperar as saídas, pois o cálculo do ressarcimento/complemento é pelos totais das notas de entradas e saídas gerados através de lançamentos na subapuração\. Obs: Estamos seguindo a mesma lógica do Ressarcimento SP \(CAT\-42\) que também não considera as notas de saída para cálculo do ICMS das notas de devolução, no caso de operações para consumidor final\.

## <a id="_Toc97913261"></a>2\.1 – Recuperação dos Dados e Processamento

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- Parametrização dos Dados Iniciais

                                  \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais;

__Critérios da recuperação das Notas Fiscais de Devolução: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Nota fiscal de devolução \(NORM\_DEV = “2”\);

\- Nota de entrada \(MOVTO\_E\_S <> “9”\);

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

 No caso da parametrização por Código, será verificado se o produto da nota consta como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\) ou como “produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\) 

\- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros 🡪 Operações*” para a seguinte

   operação:

- Saída à Consumidor Final \(e Devoluções\) \(código parâmetro __744__\)

## <a id="_Toc97913262"></a>2\.2 – Gravação dos Dados

__Gravação dos Resultados da Geração:__

Os movimentos recuperados são armazenados em três tabelas que serão utilizadas posteriormentes para geração dos registros 1920, 1921, 1923 do Sped Fiscal:

- Tabela de Subapuração do RS \(registro 1920\) – __ICT\_SUB\_APURACAO\_RS__
- Tabela dos Ajustes da Subapuração do RS \(registro 1921\) – __ITEM\_APURAC\_SUBRS__
- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\) – __ITEM\_APURAC\_SUBRS\_AJUSTE__

Cada documento fiscal de devolução de saída é gravada na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE__ relacionados ao lançamento e Subapuração parametrizados em Dados Iniciais\. 

Os documentos ficais de devolução de saída são consolidados e geram um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, e atualizados na __ICT\_SUB\_APURACAO\_RS__, recalculando a Subapuração\.

O Resultado desta geração pode ser conferido através do Relatório de Conferência disponível no módulo\.

# <a id="_Toc97913263"></a>3 – <a id="_Toc66978347"></a>Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\)

Os documentos fiscais de devolução de saída serão gravados__ item a item__, na tabela conforme definido a seguir\.

__Tabela ITEM\_APURAC\_SUBRS\_AJUSTE__

Esta tabela contém os documentos fiscais que compuseram os lançamentos \(Ajustes\) da Subapuração de um estabelecimento e período\. 

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK/UK__

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

Código da empresa de login\.

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

Se a opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

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

Considerar o Item da Apuração do “__Lançamento de Outros Créditos para Devolução das Saídas de Mercadorias destinadas a Consumidor Final deste Estado__”\.

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

Código do estabelecimento do documento fiscal \(SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Data Fiscal__

DATA\_FISCAL

Preencher com a Data Fiscal do documento fiscal \(SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Entrada/Saída__

MOVTO\_E\_S

Preencher com o indicador do Movimento Entrada/Saída \(campo “03\-Movimento Entrada/Saída” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Normal/Devolução__

NORM\_DEV

Preencher com o indicador de Normal ou Devolução \(campo “04 \- Normal ou Devolução” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Tipo do Documento__

IDENT\_DOCTO

Preencher com o Identificador do Tipo do Documento \(campo “05\-Tipo do Documento” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Pessoa Fis/Jur__

*\(ref ao campo 02 do registro 1923\)*

IDENT\_FIS\_JUR

Preencher com o Identificador da Pessoa fis/jur do documento fiscal \(campos 06 e 07 da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Número do Documento__

*\(campo 06 do registro 1923\)*

NUM\_DOCFIS

Preencher com o Número do documento fiscal \(campo “08\-Número do Documento” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Série do Documento__

*\(campo 04 do registro 1923\)*

SERIE\_DOCFIS

Preencher com a Série do documento fiscal \(campo “09\-Série do Documento” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Subsérie do Documento__

*\(campo 05 do registro 1923\)*

SUB\_SERIE\_DOCFIS

Preencher com a Subsérie do documento fiscal \(campo “10\-Subsérie do Documento” da SAFX07\)\.

Chave lógica de identificação do registro\.

__UK__

__Identificador do Item__

DISCRI\_ITEM

Campo identificador do item de mercadoria \(DISCR\_ITEM da X08\_ITENS\_MERC\)\.

Chave lógica de identificação do registro\.

__UK__

__Identificador do Registro Referenciado__

ID\_REG\_AJUSTE\_REF

Não preencher\.

Este campo será preenchido apenas para notas de entrada, sendo a referência para o registro da nota de saída \(ID\_REG\_AJUSTE da nota de saída\)\.

Chave lógica de identificação do registro\.

__Número do Item__

NUM\_ITEM

Número do item de mercadoria do documento fiscal \(campo “18\-Item Nota Fiscal” da SAFX08\)

__Núm Doc Fiscal Referência__

NUM\_DOCFIS\_REF

Não preencher

__Série Doc Fiscal Referência__

SERIE\_DOCFIS\_REF

Não preencher

__Subsérie Doc Fiscal Referência__

S\_SER\_DOCFIS\_REF

Não preencher

__Data Doc Fiscal Referencia__

DAT\_DI

Não preencher

__Modelo Documento__

COD\_MODELO

Preencher com o campo Modelo do documento \(campo 13 da SAFX07\)\.

__Código Fiscal__

COD\_CFOP

Preencher com o Código CFOP do item de mercadoria \(campo 22 da SAFX08\)

__Natureza da Operação__

COD\_NATUREZA\_OP

Preencher com o Código da Natureza de Operação do item de mercadoria \(campo 23 da SAFX08\)

__Produto da Nota/Cupom \(grupo, ind, código\)__

GRUPO\_PRODUTO,

IND\_PRODUTO,

COD\_PRODUTO,

DSC\_PRODUTO

Preencher com o produto do item de mercadoria \(campos 13 e 14 da SAFX08\)

Obs: No caso da parametrização do produto “Por Código” o produto da nota pode ser um Produto Principal ou um Produto Associado\.

__Produto Principal__

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

Preenchimento depende da Parametrização do Produto:

- Caso o produto do item da nota tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\), então: 

Preencher esse campo com o __Produto Principal__ \(grupo, indicador e código\)\.

- Caso o produto do item da nota tenha sido parametrizado por NCM ou por CEST \(menu Parâmetros 🡪 Produtos 🡪 Por NCM ou Por CEST\), então: 

Preencher esse campo com o __Produto do Item__ de mercadoria da nota \(campos 13 e 14 da SAFX08\)

__Medida da Origem__

GRUPO\_MEDIDA\_ORIG,

COD\_MEDIDA\_ORIG

Preencher com a unidade de __medida do item__ de mercadoria \(campo 25 da SAFX08\)\.

Para Cupom Fiscal, preencher com a __medida do Item__ \(SAFX994 – campo 17\)\.

__Medida de Destino__

GRUPO\_MEDIDA\_DEST COD\_MEDIDA\_DEST,

Preencher com a unidade de __medida do Produto__ \(campo 14 da SAFX2013\)\.

Preenchimento depende da Parametrização do Produto:

- Caso o produto do item da nota tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\), então: 

Preencher com a unidade de medida do __Produto Principal__ \(campo 14 da SAFX2013\)\.

- Caso o produto do item da nota tenha sido parametrizado por NCM ou por CEST \(menu Parâmetros 🡪 Produtos 🡪 Por NCM ou Por CEST\), então: 

Preencher com a unidade de medida do __Produto do item__ de mercadoria da nota \(campo 14 da SAFX2013\)\.

Regra Prática: unidade de medida do produto gravado no campo Produto Principal

__Fator de Conversão__

FAT\_CONV

Não preencher\.

__Quantidade do item __

QTDE\_ITEM

Não preencher

__Quantidade Convertida do item__

QTDE\_CONV

Nao preencher

__% Redução BC__

PRC\_REDUCAO\_BC

% Redução BC da parametrização dos produtos \(por Código, por NCM, ou por CEST\) utilizada na recuperação do documento fiscal\.

__Alíquota Interna__

ALIQ\_INTERNA

Alíquota Interna da parametrização dos produtos \(por Código, por NCM, ou por CEST\) utilizada na recuperação do documento fiscal\.

__Alíquota FCP __

ALIQ\_FCP

Alíquota FCP da parametrização dos produtos \(por Código, por NCM, ou por CEST\) utilizada na recuperação do documento fiscal\.

__Valor Contábil do Item__

VLR\_CONTAB\_ITEM

Valor Contábil do Item \(campo “64\-Valor Contábil do Item” da SAFX08\)

__Valor da Base de Cálculo__

VLR\_BASE\_CALC

Calcular a Base de Cálculo a se usada no cálculo do Valor do Ajuste\.

__Para Nota Fiscal preencher com__:

Se o campo "% de Redução de BC" \(PRC\_REDUCAO\_BC\) não estiver preenchido, então:

Valor da Base de Cálculo = Valor Contábil do Item \(VLR\_CONTAB\_ITEM\)

Senão

   Valor da Base de Cálculo = \[Valor Contábil do Item \(VLR\_CONTAB\_ITEM\) x \(1 \- % de Redução de BC / 100\)\]

Caso o valor resultante tenha mais de duas casas decimais, arredondar o valor para duas decimais\.

__Obs__: Mesma regra do campo “Valor Confronto – ICMS Efetivo Saída” na geração do movimento do Ressarcimento SP, \(MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor do ICMS__

VLR\_ICMS

Preencher com:

         Valor da Base de Cálculo \(VLR\_BASE\_CALC\) aplicada a Alíquota Interna:

VLR\_ICMS = Valor Base de Cálculo x Alíquota Interna /100

Caso o valor resultante tenha mais de duas casas decimais, arredondar o valor para duas decimais\.

__Valor do ICMS\-ST__

VLR\_ICMS\_ST

Não Preencher\. 

Este campo será preenchido apenas para notas de entrada

__Valor do FECP  ICMS\-ST__

VLR\_FECP\_ICMS\_ST

Preencher com:

         Valor da Base de Cálculo \(VLR\_BASE\_CALC\) aplicada a Alíquota do FCP \(Amparas/RS\)\.

VLR\_FECP\_ICMS\_ST = Valor Base de Cálculo x Alíquota FCP/100

Caso o valor resultante tenha mais de duas casas decimais, arredondar o valor para duas decimais\.

__Valor do Ajuste__

*\(campo 09 do registro 1923\)*

VLR\_AJUSTE

Calcular o valor do ajuste sendo a soma dos valores gravados nos campos anteriores\.

VLR\_AJUSTE = VLR\_ICMS \+ VLR\_FECP\_ICMS\_ST

__Obs__: Mesma regra do campo “__Valor Confronto – ICMS Efetivo Saída__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP \(ver MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor Unitário de ST __

VLR\_UNIT

Não preencher\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “7”\.

__7 __– lançamento gerado via processo de geração da devolução das saidas para consumidor final\.

__Número do Processo__

NUM\_PROCESSO

Preencher com o número do processo da geração\.

# <a id="_Toc66978348"></a><a id="_Toc97913264"></a>\- Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(registro 1921\)

Os documentos ficais recuperados da SAX07 / SAFX08 __serão consolidados__ e geram um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

__Tabela ITEM\_APURAC\_SUBRS__

Esta tabela contém os lançamentos \(Ajustes\) da Subapuração de um estabelecimento e período\. 

Cada Geração de Movimento disponível no módulo Ressarcimento RS \(entradas, saídas, devolução, inventário\), produz um lançamento em uma das operações da Subapuração \(002\- Outros Débitos, 003 – Estorno Crédito, 006 – Outros Créditos, 007 – Estorno Débito\)\. Os parâmetros necessários para esses lançamentos \(código de operação, descrição e código de ajuste\) são definidos em Dados Iniciais\.

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa de login

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento informado na tela de geração\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

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

Considerar o Item da Apuração do “__Lançamento de Outros Créditos para Devolução das Saídas de Mercadorias destinadas a Consumidor Final deste Estado__”\.

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Subapuração/Operação da Apuração\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Subapuração/operação da Apuração que está sendo gerada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração\.

__Valor do Lançamento__

*\(campo 04 do registro 1921\)*

VAL\_ITEM\_DISCRIM

Somatório dos __Valores dos Ajustes __calculados para os documentos e gravados na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE\.__

__Descrição do Lançamento__

*\(campo 03 do registro 1921\)*

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Considerar a Descrição do “__Lançamento de Outros Créditos para Devolução das Saídas de Mercadorias destinadas a Consumidor Final deste Estado__”\.

__Código do Ajuste ICMS__

*\(campo 02 do registro 1921\)*

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Considerar o Código de Ajuste Sped Fiscal do “__Lançamento de Outros Créditos para Devolução das Saídas de Mercadorias destinadas a Consumidor Final deste Estado__”\.

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com “2”\.

Este valor signfica que o lançamento possui documentos associados, que estão gravados na tabela ITEM\_APURAC\_SUBRS\_AJUSTE\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com __“7”__\.

__7 __– lançamento gerado via processo de geração da devolução das saidas para consumidor final

# <a id="_Toc66978349"></a><a id="_Toc97913265"></a>Gravação dos Dados na Tabela de Subapuração do RS \(registro 1920\)

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, e atualizados na ICT\_SUB\_APURACAO\_RS, recalculando a Subapuração\.

__Tabela ICT\_SUB\_APURACAO\_RS__

Esta tabela contém os totais da Subapuração de um estabelecimento e período\. 

Os valores da Subapuração são resultantes das gerações dos movimentos das entradas, saídas, devoluções e inventário disponíveis no módulo de Ressarcimento RS\. 

Os campos sinalizados com asterisco compõem a chave da tabela\.

<a id="_Hlk508706613"></a>

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa de login

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento informado na tela de geração\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

<a id="OLE_LINK22"></a>Se a opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

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

Este campo contém o resultado somatório dos lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__002’__ – Outros Débitos\.

__OBS__: Conforme parametrização dos Dados Iniciais, ‘002’ é o código de operação destinado ao lançamento resultante do processo de Geração das Saídas para Consumidor Final\.

__Valor total de Ajustes “Estornos de créditos”__

*\(campo 04 do registro 1920\)*

VLR\_ESTORNO\_CRED

Este campo contém o resultado somatório dos lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__003’__ – Estorno de Créditos\.

__OBS__: Conforme parametrização dos Dados Iniciais, ‘003’ é o código de operação destinado ao lançamento resultante do processo de Geração das Saídas para Outras UF’s\. 

     

__Valor total dos créditos por “Entradas e aquisições com crédito do imposto__

*\(campo 05 do registro 1920\)*

VLR\_TOT\_CRED

Gravar zero\.

Este campo __sempre__ ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

__Valor total de “Ajustes a crédito”__

*\(campo 06 do registro 1920\)*

VLR\_OUT\_CRED

Este campo contém o resultado somatório dos lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__006’__ – Outros Créditos\.

__OBS__: Conforme parametrização dos Dados Iniciais, o ‘006’ é o código de operação destinado ao lançamento resultante do processo de Geração das Entradas\.

__Valor total de Ajustes “Estornos de Débitos”__

*\(campo 07 do registro 1920\)*

VLR\_ESTORNO\_DEB

Este campo contém o resultado somatório dos lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__007’__ – Estorno de Débito\.

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

# <a id="_Toc97913266"></a>Gravação dos Dados na Tabela de Controle da Execução das Gerações 

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

 

