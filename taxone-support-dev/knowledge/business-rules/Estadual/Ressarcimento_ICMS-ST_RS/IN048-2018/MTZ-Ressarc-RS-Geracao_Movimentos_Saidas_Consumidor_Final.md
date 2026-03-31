# MTZ-Ressarc-RS-Geracao_Movimentos_Saidas_Consumidor_Final

- **Fonte:** MTZ-Ressarc-RS-Geracao_Movimentos_Saidas_Consumidor_Final.docx
- **Modificado:** 2024-01-22
- **Tamanho:** 117 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 048/2018\) 

Geração dos Movimentos – Saídas para Consumidor Final 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geraçãoà IN\-RE 048/2018 à Geração dos Movimentos \(opção “Gerar Saídas para Consumidor Final”\)

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS28006__

Liliane Videira Assaf

Geração dos movimentos de saída para Consumidor Final

\.\.\.\.\.

04/07/2019 

__MFS28006__

Liliane Videira Assaf

Tratamento da Redução de BC \(baseado na Ficha 3 – Ressarcimento SP\)

19/07/2019

__MFS28004__

Liliane Videira Assaf

Alterações no tópico 3 regras de preenchimento de campos \(marcação em verde\)

02/08/2019

__MFS62415__

Liliane Videira Assaf

Inclusão dos Cupons Fiscais na Geração da Saída para Consumidor Final

18/03/2021

__MFS47349__

Liliane Videira Assaf

Tratamento de Produtos Associados na geração dos movimentos

30/03/2021

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

24/09/2021

MFS81804

Liliane Assaf

Tratamento das Devoluções de Saídas de Mercadorias destinadas a Consumidor Final

07/03/2022

Sumário

[1\.	Introdução	1](#_Toc66978342)

[2\.	Recuperação dos Dados e Processamento	1](#_Toc66978343)

[2\.1 – Recuperação das Notas Fiscais \(ORIGEM=SAFX07/SAFX08\)	1](#_Toc66978344)

[2\.2 – Recuperação dos Cupons Fiscais \(ORIGEM=SAFX993/SAFX994\)	1](#_Toc66978345)

[2\.3 – Processamento para Gravação do Resultado	1](#_Toc66978346)

[3\.	Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\)	1](#_Toc66978347)

[4\.	Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(registro 1921\)	1](#_Toc66978348)

[5\.	Gravação dos Dados na Tabela de Subapuração do RS \(registro 1920\)	1](#_Toc66978349)

[6\.	Gravação dos Dados na Tabela de Controle da Execução das Gerações	1](#_Toc66978350)

# <a id="_Toc66978342"></a>Introdução 

A geração dos movimentos de saída para consumidor final é uma das gerações que compõe o processo de Geração dos Movimentos, responsável por calcular a Subapuração RS\.

A Geração dos Movimentos está definida pelo seguinte conjunto de documentos:

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx

Documento principal que referencia todos os outros documentos\.

Contém especificação de tela da geração, validações gerais e a regra de disparo para cada tipo de geração \(entradas, saídas para consumidor final\)\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\.docx

Documento específico da geração dos movimentos de Saída para Consumidor Final deste Estado\. 

Aplicada a contribuintes Varejistas e Não Varejistas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_Ufs\.docx

Documento específico da geração dos movimentos de Saída para outras UF’s, Isentas ou Não Tributadas\. 

Aplicada a contribuintes Varejistas\.

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

Esta geração será executada caso a opção “Gerar Saídas para consumidor final” seja selecionada na tela de geração\. Veja o tópico 4 do documento principal da Geração dos Movimentos \(MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx\)\.

A geração desse movimento de saída para consumidor final é utilizada tanto para contribuinte Varejista como Não Varejista\. Mas para contribuinte Não Varejista, ela é pré\-requisito para a geração das entradas\. Desta forma, para os Não Varejistas, toda vez que acontecer uma regeração dos movimentos de saída, a movimentação da entrada também deverá ser regerada para não ocorrer incompatibilidade\. A regra para este controle está definida no documento principal da Geração dos Movimentos \(MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx\)\.

__\[MFS47349\]__

__Quanto a Parametrização de Produtos Associados__:

A recuperação dos movimentos de entradas e saídas é feita considerando o produto Principal seus os produtos Associados, definidos na Parametrização de Produtos, opção Por Código\. 

No relatório de conferência, os documentos fiscais são apresentados com seus respectivos produtos e agrupados em nome do Produto Principal\. 

No Sped Fiscal, o documento fiscal é apresentado no registo 1923 com o produto que de fato está escriturado na nota, não havendo forma de demonstrar a relação do Produto Principal com os Produtos Associados\. Esta relação só é possível de ser observada dentro do módulo Ressarcimento ICMS\-ST RS, através dos relatórios de conferência dos movimentos\.

# <a id="_Toc350763252"></a><a id="_Toc66978343"></a>Recuperação dos Dados e Processamento

O objetivo desta geração é recuperar toda movimentação das saídas para Consumidor Final \(por notas e cupons\), dos produtos sujeitos ao ICMS\-ST e gerar um lançamento em Outros Débitos na Subapuração, carregando todo conjunto de tabelas da Subapuração, base para a geração dos registros 1920, 1921 e 1923 do SPED FISCAL\.

Tabelas que compõe a Subapuração: 

- Subapuração RS \(registro 1920\)
- Ajustes da Subapuração \(registro 1921\) 
- Identificação dos Documentos fiscais \(registro 1923\)

Na tabela de Subapuração \(registro 1920\) será gravado o campo de __Outros Débitos__ com o total da movimentação de Saída\.  Na tabela de Ajustes da Subapuração \(registro 1921\) um lançamento é realizado com o total da movimentação de Saída e código de ajuste especificado na IN048/2018, que será parametrizado na tela de Dados Iniciais\. Na tabela de Identificação dos Documentos fiscais \(registro 1923\) são gravados os documentos fiscais de saída e cupons fiscais que foram recuperados neste processo\.

Obs\.: 

1. Esta geração trata apenas as saídas destinadas a Consumidor Final\. A geração das saídas Isentas/Não Tributadas está definida em documento matriz específico para tal geração\.
2. Esta geração atende a contribuintes Varejistas e Não Varejistas\.

## <a id="_Toc66978344"></a>2\.1 – Recuperação das Notas Fiscais \(ORIGEM=SAFX07/SAFX08\)

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- Parametrização dos Dados Iniciais

                                  \- Tabelas dos Documentos Fiscais \(SAFX07 / SAFX08\);

__Critérios da recuperação das Notas Fiscais: __

- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal – data enquadrada no período informado em tela;
- Nota fiscal normal \(NORM\_DEV = “1”\); \[MFS81804\]
- Nota de saída \(MOVTO\_E\_S = “9”\); \[MFS81804\]
- Somente notas não canceladas;
- Somente notas com itens;
- \[__MFS62415\] __Modelo – serão desconsiderados os documentos de modelo 2D \(cupons fiscais\); 
- O produto do item deve constar na parametrização do menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, seu NCM deve estar parametrizado

no menu “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\. 

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

No caso da parametrização por Código, será verificado se o produto da nota consta como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\) ou como “produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\) \[__MFS47349\]__\.  

- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros à Operações*” para a seguinte operação:
- Saída à Consumidor Final \(código parâmetro __744__\)

## <a id="_Toc66978345"></a>2\.2 – Recuperação dos Cupons Fiscais \(ORIGEM=SAFX993/SAFX994\)

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- Tabelas dos Cupons Fiscais \(SAFX993 / SAFX994\);

__Critérios da recuperação dos Cupons Fiscais: __

- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data da Emissão \(campo “06\-Data da Emissão”\) – data enquadrada no período informado em tela;
- Somente cupons *não cancelados* \(somente os cupons com o campo “10\-Situação do Documento” da SAFX993 __=__ 1\);
- Somente cupons de modelo 2D \(campo “03\-Modelo Documento” da SAFX993\); 
- Somente cupons com o campo “09\-Tipo do Documento” da SAFX993 = 1 \(Cupom Fiscal\); 

*            \(as opções “2” e “3” não se referem à movimentação de mercadoria\)*

- Somente itens de cupons com o código do produto preenchido \(somente os cupons com os campos 08 e 09 <> nulo\);
- O produto do item deve constar na parametrização do menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\. 

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

No caso da parametrização por Código, será verificado se o produto da nota consta como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\) ou como “produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\) \[__MFS47349\]__\.  

- O CFOP do item deve constar na parametrização do menu “*Parâmetros à Operações*” para a seguinte operação:
- Saída à Consumidor Final \(código parâmetro __744__\)

Obs: regra baseada no Ressarcimento ICMS\-ST SP\.

## <a id="_Toc66978346"></a>2\.3 – Processamento para Gravação do Resultado

__Gravação dos Resultados da Geração:__

Os movimentos recuperados são armazenados em três tabelas que serão utilizadas posteriormentes para geração dos registros 1920, 1921, 1923 do Sped Fiscal:

- Tabela de Subapuração do RS \(registro 1920\) – __ICT\_SUB\_APURACAO\_RS__
- Tabela dos Ajustes da Subapuração do RS \(registro 1921\) – __ITEM\_APURAC\_SUBRS__
- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\) – __ITEM\_APURAC\_SUBRS\_AJUSTE__

Cada documento fiscal e cupom fiscal recuperado é gravando na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE__ relacionados ao lançamento e Subapuração parametrizados em Dados Iniciais\. 

Os documentos e cupons ficais recuperados são consolidados e geram um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, e atualizados na ICT\_SUB\_APURACAO\_RS, recalculando a Subapuração\.

O Resultado desta geração pode ser conferido através do Relatório de Conferência disponível no módulo\.

# <a id="_Toc66978347"></a>Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\)

Os documentos fiscais recuperados da SAX07 / SAFX08 serão gravados__ item a item__, na tabela conforme definido a seguir\.

Os cupons fiscais recuperados da SAX993 / SAFX994 serão gravados__ item a item__, na tabela conforme definido a seguir\.

Se em alguma geração ou relatório houver a necessidade de identificar se o registro gravado na tabela ITEM\_APURAC\_SUBRS\_AJUSTE é um cupom ou uma nota, pode\-se utilizar o campo “DISCRI\_ITEM”\. Para os cupons esse campo é gravado iniciando com o termo “CUPOM”\. 

__Tabela ITEM\_APURAC\_SUBRS\_AJUSTE__

Esta tabela contém os documentos fiscais e cupons fiscais que compuseram os lançamentos \(Ajustes\) da Subapuração de um estabelecimento e período\. 

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

Código da empresa \(SAFX07\)\.

Para Cupom Fiscal, preencher com Código da empresa \(SAFX993\)\.

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

Considerar o Item da Apuração do “Lançamento de Outros Débitos para Saídas de mercadorias destinadas a consumidor final deste Estado”\.

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

Para Cupom Fiscal, preencher com Código do estabelecimento do cupom \(SAFX993 – campo 02\)\.

Chave lógica de identificação do registro\.

__UK__

__Data Fiscal__

DATA\_FISCAL

Preencher com a Data Fiscal do documento fiscal \(SAFX07\)\.

Para Cupom Fiscal, preencher com Data de Emissão do cupom \(SAFX993 – campo 06\)\.

Chave lógica de identificação do registro\.

__UK__

__Entrada/Saída__

MOVTO\_E\_S

Preencher com o indicador do Movimento Entrada/Saída \(campo “03\-Movimento Entrada/Saída” da SAFX07\)\.

Para cupom fiscal, este campo não será preenchido\.

Chave lógica de identificação do registro\.

__UK__

__Normal/Devolução__

NORM\_DEV

Preencher com o indicador de Normal ou Devolução \(campo “04 \- Normal ou Devolução” da SAFX07\)\.

Para cupom fiscal, este campo não será preenchido\.

Chave lógica de identificação do registro\.

__UK__

__Tipo do Documento__

IDENT\_DOCTO

Preencher com o Identificador do Tipo do Documento \(campo “05\-Tipo do Documento” da SAFX07\)\.

Para cupom fiscal, este campo não será preenchido\.

Chave lógica de identificação do registro\.

__UK__

__Pessoa Fis/Jur__

*\(ref ao campo 02 do registro 1923\)*

IDENT\_FIS\_JUR

Preencher com o Identificador da Pessoa fis/jur do documento fiscal \(campos 06 e 07 da SAFX07\)\.

Para __cupom fiscal__, este campo será preenchido com a Pessoa Fis/Jur parametrizada para o Estabelecimento referenciado no cupom, cadastrada no módulo Básicos >> Data Warehouse, menu Manutenção >> Cadastros >> Estabelecimentos x Pessoas Físicas/Jurídicas\.

Caso o cadastro não seja encontrado para o Estabelecimento do cupom fiscal, então exibir a seguinte mensagem no log:

     “*Pessoa Física Jurídica não cadastradas para o Estabelecimento XXXX\.  Cupom Fiscal será gerado incompleto no registro 1923 do Sped Fiscal, sem o Código do Participante\. Favor realizar o cadastro no módulo Básicos >> Data Warehouse, menu Manutenção >> Cadastros >> Estabelecimentos x Pessoas Físicas/Jurídicas”\. *\(onde “XXX” é o código do estabelecimento\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do cupom \(dados chave da SAFX994\) exibindo: Estabelecimento \(SAFX993 – campo 02\), Modelo \(SAFX993 – campo 03\), Núm\. Caixa \(SAFX993 – campo 04\), Num\. COO \(SAFX993 – campo 05\), Data da Emissão \(SAFX993 – campo 06\) e Num\. Item \(SAFX994 – campo 07\)\. 

Obs: A tabela x993\_capa\_cupom\_ecf possui o campo Ident\_caixa\_ecf, que referencia a tabela x2087\_equipamento\_ecf, de onde recupera\-se o modelo e o número do caixa\.

Chave lógica de identificação do registro\.

__UK__

__Número do Documento__

*\(campo 06 do registro 1923\)*

NUM\_DOCFIS

Preencher com o Número do documento fiscal \(campo “08\-Número do Documento” da SAFX07\)\.

Para Cupom Fiscal, preencher com Número COO do cupom \(SAFX993 – campo 05\)\.

Chave lógica de identificação do registro\.

__UK__

__Série do Documento__

*\(campo 04 do registro 1923\)*

SERIE\_DOCFIS

Preencher com a Série do documento fiscal \(campo “09\-Série do Documento” da SAFX07\)\.

Para cupom fiscal, este campo não será preenchido\.

Chave lógica de identificação do registro\.

__UK__

__Subsérie do Documento__

*\(campo 05 do registro 1923\)*

SUB\_SERIE\_DOCFIS

Preencher com a Subsérie do documento fiscal \(campo “10\-Subsérie do Documento” da SAFX07\)\.

Para cupom fiscal, este campo não será preenchido\.

Chave lógica de identificação do registro\.

__UK__

__Identificador do Item__

DISCRI\_ITEM

Campo identificador do item de mercadoria \(DISCR\_ITEM da X08\_ITENS\_MERC\)\.

Para __Cupom Fiscal__, montar o discri\_item concatenando o termo “CUPOM” com os campos Modelo \(SAFX993 – campo 03\) \+ Número Caixa \(SAFX993 – campo 04\) \+ Número Item \(SAFX994 – campo 07\)\. 

Obs1: O termo CUPOM serve para identificar os cupons, pois nessa tabela teremos notas e cupons\. 

Obs2: A tabela x993\_capa\_cupom\_ecf possui o campo Ident\_caixa\_ecf, que referencia a tabela x2087\_equipamento\_ecf, de onde recupera\-se o modelo e o número do caixa\. 

Obs3: Os campos aqui concatenados completam a chave do item do cupom \(safx994\), que precisam ser gravados nos campos chave da tabela ITEM\_APURAC\_SUBRS\_AJUSTE\.

Chave lógica de identificação do registro\.

__UK__

__Identificador do Registro Referenciado__

ID\_REG\_AJUSTE\_REF

Não preencher\.

Este campo será preenchido apenas para notas de entrada, sendo a referência para o registro da nota de saída \(ID\_REG\_AJUSTE da nota de saída\)\.

Chave lógica de identificação do registro\.

__Número do Item__

NUM\_ITEM

Número do item de mercadoria do documento fiscal \(campo “18\-Item Nota Fiscal” da SAFX08\)\.

Para Cupom Fiscal, preencher com o Número Item \(SAFX994 – campo 07\)\.

__Núm Doc Fiscal Referência__

NUM\_DOCFIS\_REF

Número do documento fiscal de Referência \(campo 117 da SAFX08 \- NUM\_DOCFIS\_REF\)

Para cupom fiscal, este campo não será preenchido\.

__Série Doc Fiscal Referência__

SERIE\_DOCFIS\_REF

Série do documento fiscal de Referência \(campo 118 da SAFX08 \- SERIE\_DOCFIS\_REF\)

Para cupom fiscal, este campo não será preenchido\.

__Subsérie Doc Fiscal Referência__

S\_SER\_DOCFIS\_REF

Subsérie do documento fiscal de Referência \(campo 119 da SAFX08 \- SSERIE\_DOCFIS\_REF\)

Para cupom fiscal, este campo não será preenchido\.

__Data Doc Fiscal Referência__

DAT\_DI

Preencher com a Data do documento fiscal de Referência \(campo 102 da SAFX08 – DAT\_DI\)

Para cupom fiscal, este campo não será preenchido\.

__Modelo Documento__

COD\_MODELO

Preencher com o campo Modelo do documento \(campo 13 da SAFX07\)\.

Para Cupom Fiscal, preencher com Modelo do cupom \(SAFX993 – campo 03\)\.

Obs: A tabela x993\_capa\_cupom\_ecf possui o campo Ident\_caixa\_ecf, que referencia a tabela x2087\_equipamento\_ecf, de onde recupera\-se o modelo\.

__Código Fiscal__

COD\_CFOP

Preencher com o Código CFOP do item de mercadoria \(campo 22 da SAFX08\)\.

Para Cupom Fiscal, preencher com o Código CFOP do Item \(SAFX994 – campo 14\)\.

__Natureza da Operação__

COD\_NATUREZA\_OP

Preencher com o Código da Natureza de Operação do item de mercadoria \(campo 23 da SAFX08\)

Para cupom fiscal, este campo não será preenchido\.

__Produto da Nota/Cupom \(grupo, ind, código\)__

GRUPO\_PRODUTO,

IND\_PRODUTO,

COD\_PRODUTO,

DSC\_PRODUTO

Preencher com o produto do item de mercadoria \(campos 13 e 14 da SAFX08\)

Para Cupom Fiscal, preencher com o produto do Item \(SAFX994 – campos 08 e 09\)\.

\[__MFS47349\]__

Obs: No caso da parametrização do produto “Por Código” o produto da nota/cupom pode ser um Produto Principal ou um Produto Associado\.

__Produto Principal__

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

\[__MFS47349\]__

Preenchimento depende da Parametrização do Produto:

- Caso o produto do item da nota/cupom tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\), então: 

Preencher esse campo com o __Produto Principal__ \(grupo, indicador e código\)\.

- Caso o produto do item da nota/cupom tenha sido parametrizado por NCM ou por CEST \(menu Parâmetros 🡪 Produtos 🡪 Por NCM ou Por CEST\), então: 

Preencher esse campo com o __Produto do Item__ de mercadoria da nota ou do item do cupom \(campos 13 e 14 da SAFX08 ou SAFX994 – campos 08 e 09\)

__Medida da Origem__

GRUPO\_MEDIDA\_ORIG,

COD\_MEDIDA\_ORIG

Preencher com a unidade de __medida do item__ de mercadoria \(campo 25 da SAFX08\)\.

Para Cupom Fiscal, preencher com a __medida do Item__ \(SAFX994 – campo 17\)\.

__Medida de Destino__

GRUPO\_MEDIDA\_DEST COD\_MEDIDA\_DEST,

Preencher com a unidade de __medida do Produto__ \(campo 14 da SAFX2013\)\.

\[__MFS47349\]__

Preenchimento depende da Parametrização do Produto:

- Caso o produto do item da nota/cupom tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\), então: 

Preencher com a unidade de medida do __Produto Principal__ \(campo 14 da SAFX2013\)\.

- Caso o produto do item da nota/cupom tenha sido parametrizado por NCM ou por CEST \(menu Parâmetros 🡪 Produtos 🡪 Por NCM ou Por CEST\), então: 

Preencher com a unidade de medida do __Produto do item__ de mercadoria da nota ou do item do cupom \(campo 14 da SAFX2013\)\.

Regra Prática: unidade de medida do produto gravado no campo Produto Principal

__Fator de Conversão__

FAT\_CONV

Executar a regra a seguir apenas para Contribuintes NÃO VAREJISTA:

Fator de conversão da unidade de __medida do Item__ da nota/cupom para a unidade __medida do Produto\.__

Considerar a __Medida de Origem__ e a __Medida de Destino__ preenchidas nos campos anteriores\.

Para gerar este campo, é necessário verificar se na nota \(SAFX08\) / cupom \(SAFX994\) foi utilizada a mesma unidade de medida do cadastro do produto \(unidade de medida da SAFX2007\), e caso não, obter o fator de conversão\.

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

__      \(\*\)__ unidade da nota / cupom = campo “25\-Unidade de Medida” da SAFX08 ou

                                                       campo “17\-Unidade de Medida” SAFX994

__      \(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso o campo será preenchido com o número 1;

__Senão __

       Nesse caso o campo será preenchido com o fator de conversão obtido nas tabelas de conversão de medida, conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas 

      do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da 

      seguinte forma:

       \- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

       \- Caso não exista, pesquisa o fator na tabela de conversão padrão;

      Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será gerado com o campo FATOR DE CONVERSÃO sem informação, e será gravada a seguinte   

       mensagem de erro no log: 

     “*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será*

*     gerado sem esta informação”\. *\(o primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.

No caso do cupom, o log deve demonstrar as informações necessárias para permitir a identificação do item do cupom \(dados chave da SAFX994\) exibindo: Estabelecimento \(SAFX993 – campo 02\), Modelo \(SAFX993 – campo 03\), Núm\. Caixa \(SAFX993 – campo 04\), Num\. COO \(SAFX993 – campo 05\), Data da Emissão \(SAFX993 – campo 06\) e Num\. Item \(SAFX994 – campo 07\)\. 

<a id="OLE_LINK23"></a>

\[__MFS47349\]__

__= = = = =__

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

Obs:A quantidade do item da nota de saída e a quantidade convertida não são utilizadas no cálculo do valor do ajuste da nota de saída, mas sim no valor do ajuste das notas de entrada para Contribuintes Não Varejistas\.  Por isso, os campos “Fator de Conversão”, “Quantidade do item” e “Quantidade Convertida do item” não precisam ser preenchidos para contribuintes Varejistas\. Principalmente o erro acima NÃO não deve ser exibido para contribuinte Varejistas\.

__Quantidade do item __

QTDE\_ITEM

Executar a regra a seguir apenas para Contribuintes NÃO VAREJISTA:

Quantidade do item \(campo “24\-Quantidade” da SAFX08\)

Para Cupom Fiscal, preencher com a Quantidade do Item \(SAFX994 – campo 16\)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Truncar Arredondar o valor para 3 decimais\. Esta decisão foi tomada pois no relatório não tem espaço para apresentar 6 casas decimais\. Desta forma tomamos a decisão de trabalhar apenas com 3 casas decimais\. Portanto a geração já deve trabalhar com a quantidade com 3 decimais para nao dar diferença no cálculo do valor do ajuste por questões de arredondamento\.

__Quantidade Convertida do item__

QTDE\_CONV

Executar a regra a seguir apenas para Contribuintes NÃO VAREJISTA:

__Se__ o “Fator de Conversão” gerado no campo anterior = 1, então:

      Nesse caso este campo será preenchido com a mesma quantidade gerada no campo 

      “Quantidade do Item”;

__Senão __

      Se o “Fator de Conversão” gerado no campo anterior não estiver preenchido:

Preencher este campo com zero\.

      Senão:

Nesse caso o campo será preenchido com a quantidade do item \(SAFX08 ou SAFX994\) convertida para a unidade de medida do cadastro do produto, utilizando o fator de conversão obtido\. Assim, será a multiplicação dos seguintes campos gerados acima:

              

                                          \[Quantidade da Nota \* Fator de Conversão\]

OBS\.: Nesta obrigação *não* será utilizado o campo “137\-Quantidade Convertida” da SAFX08\. Este campo é utilizado por alguns clientes para informar na nota a quantidade já convertida, e quando preenchido, é utilizado em alguns casos \(como na CAT 42/18 por exemplo\)\. 

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Truncar Arredondar o valor para 3 decimais\. Esta decisão foi tomada pois no relatório não tem espaço para apresentar 6 casas decimais\. Desta forma tomamos a decisão de trabalhar apenas com 3 casas decimais\. Portanto a geração já deve trabalhar com a quantidade com 3 decimais para nao dar diferença no cálculo do valor do ajuste por questões de arredondamento\.

__% Redução BC__

PRC\_REDUCAO\_BC

% Redução BC da parametrização dos produtos \(por Código, por NCM, ou por CEST\) utilizada na recuperação do documento fiscal/cupom fiscal\.

__Alíquota Interna__

ALIQ\_INTERNA

Alíquota Interna da parametrização dos produtos \(por Código, por NCM, ou por CEST\) utilizada na recuperação do documento fiscal/cupom fiscal\.

__Alíquota FCP __

ALIQ\_FCP

Alíquota FCP da parametrização dos produtos \(por Código, por NCM, ou por CEST\) utilizada na recuperação do documento fiscal/cupom fiscal\.

__Valor Contábil do Item__

VLR\_CONTAB\_ITEM

Valor Contábil do Item \(campo “64\-Valor Contábil do Item” da SAFX08\)

Para Cupom Fiscal, preencher com Valor Total Líquido \(VLR\_LIQ\_ITEM\) \(SAFX994 – campo 22\)\.

__Valor da Base de Cálculo__

VLR\_BASE\_CALC

Calcular a Base de Cálculo a se usada no cálculo do Valor do Ajuste\.

__Para Nota Fiscal preencher com__:

Se o campo "% de Redução de BC" \(PRC\_REDUCAO\_BC\) não estiver preenchido, então:

Valor da Base de Cálculo = Valor Contábil do Item \(VLR\_CONTAB\_ITEM\)

Senão

   Valor da Base de Cálculo = \[Valor Contábil do Item \(VLR\_CONTAB\_ITEM\) x \(1 \- % de Redução de BC / 100\)\]

__Para Cupom Fiscal preencher com:__

Se o campo "% de Redução de BC" \(PRC\_REDUCAO\_BC\) não estiver preenchido, então:

Valor da Base de Cálculo = Valor Total Líquido \(VLR\_LIQ\_ITEM\)

Senão

   Valor da Base de Cálculo = \[Valor Total Líquido \(VLR\_LIQ\_ITEM\) x \(1 \- % de Redução de BC / 100\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Caso o valor resultante tenha mais de duas casas decimais, arredondar o valor para duas decimais\.

__Obs__: Mesma regra do campo “Valor Confronto – ICMS Efetivo Saída” na geração do movimento do Ressarcimento SP, \(MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor do ICMS__

VLR\_ICMS

Preencher com:

         Valor da Base de Cálculo \(VLR\_BASE\_CALC\) aplicada a Alíquota Interna:

VLR\_ICMS = Valor Base de Cálculo x Alíquota Interna /100

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Caso o valor resultante tenha mais de duas casas decimais, truncar arredondar o valor para duas decimais\.

__Valor do ICMS\-ST__

VLR\_ICMS\_ST

Não Preencher\. 

Este campo será preenchido apenas para notas de entrada

__Valor do FECP  ICMS\-ST__

VLR\_FECP\_ICMS\_ST

Preencher com:

         Valor da Base de Cálculo \(VLR\_BASE\_CALC\) aplicada a Alíquota do FCP \(Amparas/RS\)\.

VLR\_FECP\_ICMS\_ST = Valor Base de Cálculo x Alíquota FCP/100

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Caso o valor resultante tenha mais de duas casas decimais, truncar arredondar o valor para duas decimais\.

__Valor do Ajuste__

*\(campo 09 do registro 1923\)*

VLR\_AJUSTE

Calcular o valor do ajuste sendo a soma dos valores gravados nos campos anteriores\.

VLR\_AJUSTE = VLR\_ICMS \+ VLR\_FECP\_ICMS\_ST

__Obs__: Mesma regra do campo “__Valor Confronto – ICMS Efetivo Saída__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP \(ver MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor Unitário de ST __

VLR\_UNIT

Não preencher\.

Este campo será preenchido apenas para notas de entrada

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “2”\.

__2 __– lançamento gerado via processo de geração da saida a Consumidor Final\.

__Número do Processo__

NUM\_PROCESSO

Preencher com o número do processo da geração\.

# <a id="_Toc66978348"></a>Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(registro 1921\)

Os documentos ficais recuperados da SAX07 / SAFX08 juntamente com cupons fiscais \(SAFX993/SAFX994\) __serão consolidados__ e geram um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

__Tabela ITEM\_APURAC\_SUBRS__

Esta tabela contém os lançamentos \(Ajustes\) da Subapuração de um estabelecimento e período\. 

Cada Geração de Movimento disponível no módulo Ressarcimento RS \(entradas, saídas\), produz um lançamento em uma das operações da Subapuração \(002\- Outros Débitos, 003 – Estorno Crédito, 006 – Outros Créditos, 007 – Estorno Débito\)\. Os parâmetros necessários para esses lançamentos \(código de operação, descrição e código de ajuste\) são definidos em Dados Iniciais\.

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

Considerar o Item da Apuração do “Lançamento de Outros Débitos para Saídas de mercadorias destinadas a consumidor final deste Estado”\.

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Subapuração/Operação da Apuração\. 

Ou seja, recuperar o próximo número da seguencia de lançamentos da Subapuração/operação da Apuração que está sendo gerada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração\.

__Valor do Lançamento__

*\(campo 04 do registro 1921\)*

VAL\_ITEM\_DISCRIM

Somatório dos __Valores dos Ajustes __\(VLR\_AJUSTE\) calculados para os documentos e gravados na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE\.__

__Descrição do Lançamento__

*\(campo 03 do registro 1921\)*

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Considerar a Descrição do “Lançamento de Outros Débitos para Saídas de mercadorias destinadas a consumidor final deste Estado”\.

__Código do Ajuste ICMS__

*\(campo 02 do registro 1921\)*

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Considerar o Código de Ajuste Sped Fiscal do “Lançamento de Outros Débitos para Saídas de mercadorias destinadas a consumidor final deste Estado”\.

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com “2”\.

Este valor signfica que o lançamento possui documentos associados, que estão gravados na tabela ITEM\_APURAC\_SUBRS\_AJUSTE\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “2”\.

__2 __– lançamento gerado via processo de geração da saida a Consumidor Final\.

# <a id="_Toc66978349"></a>Gravação dos Dados na Tabela de Subapuração do RS \(registro 1920\)

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

Se \(VLR\_TOT\_DEB   \+ VLR\_OUT\_DEB   \+ VLR\_ESTORNO\_CRED\) \-

     \(VLR\_TOT\_CRED \+ VLR\_OUT\_CRED \+ VLR\_ESTORNO\_DEB \+ VLR\_SALDO\_CRED\) __>__ 0 Então

       Gravar o campo VLR\_SLD\_APURADO com o resultado da expressão:

        \(VLR\_TOT\_DEB    \+ VLR\_OUT\_DEB   \+ VLR\_ESTORNO\_CRED\) \-

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

Se \(VLR\_TOT\_DEB   \+ VLR\_OUT\_DEB   \+   VLR\_ESTORNO\_CRED\) \-

     \(VLR\_TOT\_CRED \+ VLR\_OUT\_CRED \+  VLR\_ESTORNO\_DEB \+  VLR\_SALDO\_CRED\) __>__ 0 Então

         Gravar o campo VLR\_SLD\_CREDOR\_TRANSP com zero\.

Sentão

       Gravar o campo VLR\_SLD\_CREDOR\_TRANSP com o resultado da expressão:

        \(VLR\_TOT\_CRED \+ VLR\_OUT\_CRED \+ VLR\_ESTORNO\_DEB \+ VLR\_SALDO\_CRED\) \- 

        \(VLR\_TOT\_DEB    \+ VLR\_OUT\_DEB   \+ VLR\_ESTORNO\_CRED\) 

__Valores recolhidos ou a recolher, extraapuração\.__

*\(campo 13 do registro 1920\)*

VLR\_DEB\_ESP

Gravar zero\.

Estes campo sempre ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

# <a id="_Toc66978350"></a>Gravação dos Dados na Tabela de Controle da Execução das Gerações 

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

 

