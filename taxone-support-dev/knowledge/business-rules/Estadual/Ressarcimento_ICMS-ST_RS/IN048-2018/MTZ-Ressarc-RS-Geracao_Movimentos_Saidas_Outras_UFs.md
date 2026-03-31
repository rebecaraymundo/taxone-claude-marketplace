# MTZ-Ressarc-RS-Geracao_Movimentos_Saidas_Outras_UFs

- **Fonte:** MTZ-Ressarc-RS-Geracao_Movimentos_Saidas_Outras_UFs.docx
- **Modificado:** 2024-01-22
- **Tamanho:** 163 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 048/2018\) 

Geração dos Movimentos – Saídas para Outras Ufs, Isentas ou Não Tributadas \(só para Varejista\) 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração 🡪 IN\-RE 048/2018 🡪 Geração dos Movimentos \(opção “Gerar saídas para Outras Ufs, Isentas ou Não Tributadas \(Varejista\)”\)

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS28012__

Liliane Videira Assaf

Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)

21/08/2019

__MFS62415__

Liliane Videira Assaf

Inclusão dos Cupons Fiscais na Geração 

18/03/2021

__MFS47349__

Liliane Videira Assaf

Tratamento de Produtos Associados na geração dos movimentos

30/03/2021

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

27/09/2021

__MFS591083__

Liliane Assaf

Tratamento das Incorporações de Empresas/Estabelecimentos

22/01/2024

Sumário

[1\.	Introdução	1](#_Toc68106266)

[2\.	Visão Geral	1](#_Toc68106267)

[3\.	ETAPA 1 – PROCESSAMENTO DAS SAÍDAS PARA OUTRAS Ufs, ISENTAS OU NÃO TRIBUTADAS	1](#_Toc68106268)

[3\.1 – Recuperação dos Dados e Processamento	1](#_Toc68106269)

[3\.1\.1 \- Recuperação das Notas Fiscais \(ORIGEM=SAFX07/SAFX08\)	1](#_Toc68106270)

[*3\.1\.2 – Recuperação dos Cupons Fiscais \(ORIGEM=SAFX993/SAFX994*\)	1](#_Toc68106271)

[3\.2 – Gravação dos Dados	1](#_Toc68106272)

[3\.2\.1 – Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração \(ITEM\_APURAC\_SUBRS\_AJUSTE\)	1](#_Toc68106273)

[4\.	ETAPA 2 – PROCESSAMENTO DAS ÚLTIMAS ENTRADAS	1](#_Toc68106274)

[4\.1 – Recuperação dos Dados e Processamento	1](#_Toc68106275)

[4\.2 – Gravação dos Dados	1](#_Toc68106276)

[4\.2\.1 \- Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração \(ITEM\_APURAC\_SUBRS\_AJUSTE\)	1](#_Toc68106277)

[5\.	ETAPA 3 – ATUALIZAÇÃO DO VALOR DO AJUSTE DAS SAÍDAS PARA OUTRAS Ufs, ISENTAS OU NÃO TRIBUTADAS	1](#_Toc68106278)

[5\.1 – Recuperação dos Dados e Processamento	1](#_Toc68106279)

[5\.2 – Gravação dos Dados	1](#_Toc68106280)

[5\.2\.1 – Atualização do Valor do Ajuste na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração \(ITEM\_APURAC\_SUBRS\_AJUSTE\)	1](#_Toc68106281)

[5\.2\.2 \- Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\)	1](#_Toc68106282)

[5\.2\.3 \- Gravação dos Dados na Tabela de Subapuração do RS \(ICT\_SUB\_APURACAO\_RS\)	1](#_Toc68106283)

[6\.	Gravação dos Dados na Tabela de Controle da Execução das Gerações	1](#_Toc68106284)

# <a id="_Toc68106266"></a>Introdução 

A geração dos movimentos de saídas para Outras Ufs, Isentas ou Não Tributadas é uma das gerações que compõe o processo de Geração dos Movimentos, responsável por calcular a Subapuração RS\.

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

Esta geração será executada caso o contribuinte seja __Varejista__ e a opção “Gerar saídas para Outras Ufs, Isentas ou Não Tributadas” seja selecionada na tela de geração\. Veja o tópico 4 do documento principal da Geração dos Movimentos \(MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx\)\.

__\[MFS47349\]__

__Quanto a Parametrização de Produtos Associados__:

A recuperação dos movimentos de entradas e saídas é feita considerando o produto Principal seus os produtos Associados, definidos na Parametrização de Produtos, opção Por Código\. 

No relatório de conferência, os documentos fiscais são apresentados com seus respectivos produtos e agrupados em nome do Produto Principal\. 

No Sped Fiscal, o documento fiscal é apresentado no registo 1923 com o produto que de fato está escriturado na nota, não havendo forma de demonstrar a relação do Produto Principal com os Produtos Associados\. Esta relação só é possível de ser observada dentro do módulo Ressarcimento ICMS\-ST RS, através dos relatórios de conferência dos movimentos\.

# <a id="_Toc68106267"></a>Visão Geral

Podemos fazer uma correspondência desta geração com a lógica de geração das Entradas para contribuintes Não Varejistas\. 

A geração das entradas não varejistas parte das notas de saída para consumidor final, já gravadas pela Geração do Movimento opção “Gerar saídas para Consumidor Final”\.  Ou seja, leem as notas de saída para consumidor final da tabela resultante \(__ITEM\_APURAC\_SUBRS\_AJUSTE__\) e buscam as últimas notas fiscais de entrada do produto vendido\.

A geração da saída para Outras Ufs, Isentas ou Não Tributadas também busca as últimas notas fiscais de entrada dos produtos vendidos, só que relacionados nas notas de saída para Outras Ufs, Isentas ou Não Tributadas\. 

Podemos dividir a geração da saída para Outras Ufs, Isentas ou Não Tributadas em __três etapas__:

1. Processar as saídas para Outras Ufs, Isentas ou Não Tributadas:

Esta etapa consiste em recuperar as notas e cupons de saídas das tabelas de Documento Fiscal \(SAFX07/SAFX08\), com produto parametrizado por Código, NBM ou CEST nas opções disponíveis neste módulo, e com CFOP ou CFOP/Natureza de Operação parametrizado para “Saídas para outro Estado, Saída Isenta ou Não Tributada”\. As notas e cupons recuperados são gravados na tabelas de resultado do processamento \(__ITEM\_APURAC\_SUBRS\_AJUSTE\)__\.

1. Processar as últimas entradas do produto vendido:

Nesta etapa, a partir das notas e cupons de saídas para Outras Ufs, Isentas ou Não Tributadas gravados na tabela resultado do processamento \(__ITEM\_APURAC\_SUBRS\_AJUSTE\)__, recuperar a última entrada do produto vendido\. 

Gravar a nota de entrada relacionada a cada item da nota de saída na tabela \(__ITEM\_APURAC\_SUBRS\_AJUSTE\)__\.

1. Atualizar o valor do Ajuste das notas de saídas para Outras Ufs, Isentas ou Não Tributadas na tabela \(__ITEM\_APURAC\_SUBRS\_AJUSTE\)__, considerando o valor Unitário da nota de entrada\.

# <a id="_Toc68106268"></a>ETAPA 1 – PROCESSAMENTO DAS SAÍDAS PARA OUTRAS Ufs, ISENTAS OU NÃO TRIBUTADAS

O objetivo desta etapa é recuperar toda movimentação das saídas para outras Ufs, Isentas ou Não Tributadas e gerar um lançamento em Estorno de Crédito na Subapuração, carregando todo conjunto de tabelas da Subapuração, base para a geração dos registros 1920, 1921 e 1923 do SPED FISCAL\.

Tabelas que compõe a Subapuração: 

- Subapuração RS \(registro 1920\)
- Ajustes da Subapuração \(registro 1921\) 
- Identificação dos Documentos fiscais \(registro 1923\)

Na tabela de Subapuração \(registro 1920\) será gravado o campo de Estorno de Crédito com o total da movimentação de Saídas\.  Na tabela de Ajustes da Subapuração \(registro 1921\) um lançamento é realizado com o total da movimentação de Saída e código de ajuste específicado na IN048/2018, que será parametrizado na tela de Dados Iniciais\. Na tabela de Identificação dos Documentos fiscais \(registro 1923\) são gravados os documentos fiscais de saída e cupons fiscais que foram recuperados neste processo\.

Obs\.: 

1. <a id="_Hlk17384168"></a>A notas de devolução de venda __NÃO__ são consideradas nesta geração, pois na verdade elas são cadastradas como entradas e tratadas na geração do movimento de entradas, compondo o lançamento em outros Créditos na Subapuração\.  
2. As notas fiscais estão sendo gravadas na tabela de Identificação dos Documentos fiscais objetivando a conferência através do relatório disponível neste módulo\.

## <a id="_Toc68106269"></a>3\.1 – Recuperação dos Dados e Processamento

### <a id="_Toc68106270"></a>3\.1\.1 \- Recuperação das Notas Fiscais \(ORIGEM=SAFX07/SAFX08\)

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- Parametrização dos Dados Iniciais

                                  \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais;

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Somente notas *não canceladas*;

\- Somente notas *com itens*;

\- \[__MFS62415\] __Modelo – serão desconsiderados os documentos de modelo 2D \(cupons fiscais\);

\- O produto do item deve constar na parametrização do menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, seu NCM deve estar parametrizado

  no menu “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\. 

  Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

  A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

 No caso da parametrização por Código, será verificado se o produto da nota consta como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\) ou como “produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\) \[__MFS47349\]__\. 

\- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros 🡪 Operações*” para a seguinte

   operação:

- Saída para Outro Estado, Saídas Isentas ou Não Tributadas \(código parâmetro __745__\)

## <a id="_Toc66978345"></a><a id="_Toc68106271"></a>__3\.1\.2 – Recuperação dos Cupons Fiscais \(ORIGEM=SAFX993/SAFX994__\)

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
- Saída para Outro Estado, Saídas Isentas ou Não Tributadas \(código parâmetro __745__\)

## <a id="_Toc68106272"></a>3\.2 – Gravação dos Dados

__Gravação dos Resultados da Geração:__

Os movimentos recuperados são armazenados em três tabelas que serão utilizadas posteriormentes para geração dos registros 1920, 1921, 1923 do Sped Fiscal:

- Tabela de Subapuração do RS \(registro 1920\) – __ICT\_SUB\_APURACAO\_RS__
- Tabela dos Ajustes da Subapuração do RS \(registro 1921\) – __ITEM\_APURAC\_SUBRS__
- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\) – __ITEM\_APURAC\_SUBRS\_AJUSTE__

Cada documento fiscal e cupom fiscal recuperado é gravando na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE__ relacionados ao lançamento e Subapuração parametrizados em Dados Iniciais\. 

Os documentos ficais e cupons fiscais recuperados são consolidados e geram um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, e atualizados na __ICT\_SUB\_APURACAO\_RS__, recalculando a Subapuração\.

O Resultado desta geração pode ser conferido através do Relatório de Conferência disponível no módulo\.

__Nesta etapa vamos apenas gravar os documentos fiscais na tabela ITEM\_APURAC\_SUBRS\_AJUSTE\.  As demais tabelas serão atualizadas na etapa 3, vide item __[__5\.2__](#_5.2_–_Gravação)__ deste documento__\.

### <a id="_Toc68106273"></a>3\.2\.1 – Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração \(ITEM\_APURAC\_SUBRS\_AJUSTE\)

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

Considerar o Item da Apuração do “Lançamento de Estorno de Crédito para Saídas de Mercadorias destinadas a outros Estados ou isentas ou não tributadas”\.

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

Número do item de mercadoria do documento fiscal \(campo “18\-Item Nota Fiscal” da SAFX08\)

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

__Data Doc Fiscal Referencia__

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

Preencher com o Código CFOP do item de mercadoria \(campo 22 da SAFX08\)

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

Fator de conversão da unidade de __medida do Item__ da nota/cupom para a unidade __medida do Produto\.__

Considerar a __Medida de Origem__ e a __Medida de Destino__ preenchidas nos campos anteriores

Para gerar este campo, é necessário verificar se na nota \(SAFX08\) / cupom \(SAFX994\) foi utilizada a mesma unidade de medida do cadastro do produto \(unidade de medida da SAFX2007\), e caso não, obter o fator de conversão\.

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade da nota / cupom = campo “25\-Unidade de Medida” da SAFX08 ou

                                                      campo “17\-Unidade de Medida” SAFX994

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso o campo será preenchido com o número 1;

__Senão __

       Nesse caso o campo será preenchido com o fator de conversão obtido nas tabelas de conversão de

       medida, conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas 

      do Módulo DW \(menu “*Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medida*”\), da 

      seguinte forma:

       \- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

       \- Caso não exista, pesquisa o fator na tabela de conversão padrão;

      Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será 

       gerado com o campo FATOR DE CONVERSÃO sem informação, e será gravada a seguinte   

       mensagem de erro no log: 

     “*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será gerado sem esta informação”\. *\(o primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.

No caso do cupom, o log deve demonstrar as informações necessárias para permitir a identificação do item do cupom \(dados chave da SAFX994\) exibindo: Estabelecimento \(SAFX993 – campo 02\), Modelo \(SAFX993 – campo 03\), Núm\. Caixa \(SAFX993 – campo 04\), Num\. COO \(SAFX993 – campo 05\), Data da Emissão \(SAFX993 – campo 06\) e Num\. Item \(SAFX994 – campo 07\)\. 

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

__Quantidade do item __

QTDE\_ITEM

Quantidade do item \(campo “24\-Quantidade” da SAFX08\)

Para Cupom Fiscal, preencher com a Quantidade do Item \(SAFX994 – campo 16\)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Truncar Arredondar o valor para 3 decimais\. Esta decisão foi tomada pois no relatório não tem espaço para apresentar 6 casas decimais\. Desta forma tomamos a decisão de trabalhar apenas com 3 casas decimais\. Portanto a geração já deve trabalhar com a quantidade com 3 decimais para nao dar diferença no cálculo do valor do ajuste por questões de arredondamento\.

__Quantidade Convertida do item__

QTDE\_CONV

__Se__ o “Fator de Conversão” gerado no campo anterior = 1, então:

      Nesse caso este campo será preenchido com a mesma quantidade gerada no campo “Quantidade do Item”;

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

Não preencher

__Alíquota Interna__

ALIQ\_INTERNA

Não preencher

__Alíquota FCP __

ALIQ\_FCP

Não preencher

__Valor Contábil do Item__

VLR\_CONTAB\_ITEM

Não preencher

__Valor da Base de Cálculo__

VLR\_BASE\_CALC

Não preencher

__Valor do ICMS__

VLR\_ICMS

Não preencher

__Valor do ICMS\-ST__

VLR\_ICMS\_ST

Não Preencher\. 

__Valor do FECP  ICMS\-ST__

VLR\_FECP\_ICMS\_ST

Não preencher

__Valor do Ajuste__

*\(campo 09 do registro 1923\)*

VLR\_AJUSTE

Não preencher neste momento\.

Este valor será atualizado na etapa 3, com o valor unitário da nota de entrada multiplicado pela quantidade do item convertida da nota de saída\.

__Valor Unitário de ST __

VLR\_UNIT

Não preencher\.

Este campo será preenchido apenas para notas de entrada

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “4”\.

__4 __– lançamento gerado via processo de geração da saida para outras Ufs, Isentas ou Não Tributadas\.

__Número do Processo__

NUM\_PROCESSO

Preencher com o número do processo da geração\.

# <a id="_Toc68106274"></a>ETAPA 2 – PROCESSAMENTO DAS ÚLTIMAS ENTRADAS 

## <a id="_Toc68106275"></a>4\.1 – Recuperação dos Dados e Processamento

A partir do item de mercadoria da nota de saída \(ou item do cupom fiscal\) para outra Ufs, Isentas ou Não Tributadas, será recuperada a última nota fiscal de entrada do produto vendido no documento de saída\.  

A última nota fiscal de entrada do produto pode estar referenciada no item da nota de saída \(campo 117 \- Número do Docto\. Fiscal de Referência da SAFX08\)\. Mas caso não esteja, esta rotina tentará buscar a última nota fiscal de entrada do produto sendo a mais recente nota de entrada deste produto\.

No caso de saída por cupom fiscal, a última nota de entrada do produto não está referenciada no item do cupom\. Portanto a rotina tentará buscar a última nota fiscal de entrada do produto sendo a mais recente nota de entrada deste produto\.

Se houver necessidade de identificar se o registro gravado na tabela ITEM\_APURAC\_SUBRS\_AJUSTE é um cupom ou uma nota, pode\-se utilizar o campo “DISCRI\_ITEM”\. Para os cupons esse campo é gravado iniciando com o termo “CUPOM”

\[__MFS47349\]__

Caso o produto da nota de saída esteja parametrizado Por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código\), a busca pela última nota de entrada deve considerar dois cenários:

- produto da entrada igual ao produto da saída;
- produto da entrada diferente do produto da saída, e ambos pertencendo a uma parametrização de Produto Principal com Produtos Associados\. 

\- O produto da saída pode ser um produto associado e o produto da entrada ser o produto principal\. OU

\- O produto da saída pode ser o produto principal e o produto da entrada ser um produto associado\. OU

\- Ambos os produtos \(saída e entrada\) serem produtos associados a um produto principal qualquer\.

Para isso a seguinte regra será aplicada:

__Para Nota Fiscal de Saída:__

	__Se__ o item de mercadoria da nota fiscal de saída possuir a informação de documento fiscal de referência preenchido, então:

		Buscaremos a nota de entrada referenciada nas tabelas de documento fiscal \(X07/X08\)\.

		__Se__ a nota fiscal de entrada referenciada for encontrada, então:

Esta nota de entrada será considerada como a última nota fiscal de entrada do produto vendido\.

		__Senão__

			Buscaremos a nota fiscal de entrada mais recente do produto vendido\.

	__Senão__

		Buscaremos a nota fiscal de entrada mais recente do produto relacionado\.

__Para Cupom Fiscal:__

		Buscaremos a nota fiscal de entrada mais recente do produto relacionado\.

A nota fiscal de entrada recuperada será gravada com a identificação da nota de saída, pois esta relação será demonstrada no relatório de conferência desta geração\.

![](data:image/png;base64,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)

__Recuperação do Movimento de Saída para Outras Ufs, Isentas ou Não Tributadas \( Nota ou Cupom\)__

Origem dos dados:  

- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\_AJUSTE\)

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

- SAFX07 / SAFX08 \- Tabelas dos Documentos Fiscais \(DATAMART\)
- Tabelas dos Cupons Fiscais \(SAFX993 / SAFX994\);

 

Critérios da recuperação da movimentação do período:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado = ‘__4’ __– lançamento gerado via processo de geração da saida para outras Ufs, Isentas ou Não Tributadas\. 

Recuperar os seguintes campos:

- Campo de identificação da nota de saída \- chave física \(ID\_REG\_AJUSTE da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)
- Campos de identificação da nota de saída \- chave lógica \(cod\_empresa, cod\_estab,\.\.\. tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\) 
- Produto da nota/cupom de saída \(GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)
- \[__MFS47349\] __Produto Principal \(GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)
- Medida Destino \(GRUPO\_MEDIDA\_DEST, COD\_MEDIDA\_DEST da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)
- Quantidade Convertida \(QTDE\_CONV da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)
- Número do documento fiscal de Referência \(NUM\_DOCFIS\_REF da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)
- Série do documento fiscal de Referência \(SERIE\_DOCFIS\_REF da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)
- Subsérie do documento fiscal de Referência \(S\_SERIE\_DOCFIS\_REF da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)
- Data do documento fiscal de Referência \(DAT\_DI da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)

Caso a busca não retorne registro, então:

Esta geração é finalizada\.

Caso contrário:

Recuperação da última nota fiscal de entrada do produto vendido, para cada item da nota de saída retornado pela consulta acima\.

 

__Recuperação das Notas Fiscais de Entrada: __

Origem dos dados:

\- Parametrização de Produtos \(por Código, por NCM e por CEST\);

\- Parametrização de CFOP / Natureza de Operação;

\- Parametrização dos Dados Iniciais

\- SAFX07 / SAFX08 \- Tabelas dos Documentos Fiscais;

Considerar a necessidade de pesquisar esta nota nas tabelas normais \(X07/X08\), já que a nota fiscal poderá estar num período anterior ao período da movimentação gerada no Datamart;

Critérios Gerais para recuperação da movimentação das entradas:

Os criterios abaixo servem tanto para a busca da entrada pela referência na nota de saída, quanto para a busca pela entrada mais recente do produto\.

- Código Empresa = Código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;
- nota fiscal de entrada \(MOVTO\_E\_S  <> ‘9’\);
- nota fiscal normal \(NORM\_DEV = ‘1’\)
- Somente notas *não canceladas*;
- Somente notas *com itens*;
- O produto do item deve constar na parametrização do menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\.

  Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

  A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

 No caso da parametrização por Código, será verificado se o produto da nota consta como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\) ou como “produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\) \[__MFS47349\]__\. 

- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros 🡪 Operações*” para a seguinte

   operação:

- Entrada com Substituição Tributária \(código parâmetro __746__\)

__Critérios Específicos para busca da última Nota de Entrada do Produto pela Referência:__

Para as notas de saída com Número do documento fiscal de Referência e Data do documento fiscal de Referência preenchidos, adicionar os critérios abaixo na busca na nota de entrada:

- __Produto__ relacionado item de mercadoria da __nota de entrada__ = __Produto__ relacionado ao item de mercadoria da __nota de Saída __

\(esta relação deve ser feita pelo indicador e código do produto\)

Considerar o Produto da __nota/cupom de saída__ = GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\.

Ou

\[__MFS47349\] __

__Produto__ relacionado item de mercadoria da __nota de entrada__ diferente do __Produto__ relacionado ao item de mercadoria da __nota/cupom de Saída, mas__

que ambos pertençam a uma parametrização de Produto Principal com Produtos Associados, na Parametrização de Produto opção Por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código\)\. 

Para isso, considerar o Produto Principal \(GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC\) gravado na tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE para a __nota/cupom de Saída__ e recuperar os produtos associados na tabela__ ESP\_SP\_PROD\_ST\_ASS__\. 

Verificar se o produto da __nota de entrada__ é igual ao Produto Principal \(GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC\) ou igual a algum dos produtos associados ao produto principal\. 

Três situações são atendidas por essa regra:

\- O produto da saída pode ser um produto associado e o produto da entrada ser o produto principal\. 

\- O produto da saída pode ser o produto principal e o produto da entrada ser um produto associado\.

\- Ambos os produtos \(saída e entrada\) serem produtos associados a um produto principal qualquer

- Data Fiscal do Documento Fiscal de entrada <= Data Fiscal da nota de saída
- Número do Documento Fiscal de entrada = Número do documento fiscal de Referência da nota de saída
- Série do Documento Fiscal de entrada = Série do documento fiscal de Referência da nota de saída
- Subsérie do Documento Fiscal de entrada = Subsérie do documento fiscal de Referência da nota de saída
- Data de emissão do Documento Fiscal de entrada = Data do documento fiscal de Referência da nota de saída \(DAT\_DI\)

__Critérios Específicos para busca da última Nota de Entrada do Produto pela nota mais recente:__

Adicionar os critérios abaixo para busca na nota de entrada mais recente do produto, para as situações: 

1. Notas de saída __sem__ Número do documento fiscal de Referência e Data do documento fiscal de Referência preenchidos\. 
2. Notas de saída com Número do documento fiscal de Referência e Data do documento fiscal de Referência preenchidos, mas que a nota de entrada não foi encontrada nas Tabelas dos Documentos Fiscais\.
3. Saída por cupom fiscal\.

Critérios:

- __Produto__ relacionado item de mercadoria da __nota de entrada__ = __Produto__ relacionado ao item de mercadoria da __nota de Saída__

\(esta relação deve ser feita pelo indicador e código do produto\)

Considerar o Produto da __nota/cupom de saída__ = GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\.

Ou

\[__MFS47349\] __

__Produto__ relacionado item de mercadoria da __nota de entrada__ diferente do __Produto__ relacionado ao item de mercadoria da __nota/cupom de Saída, mas__

que ambos pertençam a uma parametrização de Produto Principal com Produtos Associados, na Parametrização de Produto opção Por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código\)\. 

Para isso, considerar o Produto Principal \(GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC\) gravado na tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE para a __nota/cupom de Saída__ e recuperar os produtos associados na tabela__ ESP\_SP\_PROD\_ST\_ASS__\. 

Verificar se o produto da __nota de entrada__ é igual ao Produto Principal \(GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC\) ou igual a algum dos produtos associados ao produto principal\. 

Três situações são atendidas por essa regra:

\- O produto da saída pode ser um produto associado e o produto da entrada ser o produto principal\. 

\- O produto da saída pode ser o produto principal e o produto da entrada ser um produto associado\.

\- Ambos os produtos \(saída e entrada\) serem produtos associados a um produto principal qualquer

- Data Fiscal do Documento Fiscal de entrada <= Data Fiscal da nota de saída \(ou Data Emissão do Cupom Fiscal\)
- Data Fiscal do Documento Fiscal de entrada compreendida entre a data informada em tela no campo “__Pesquisar últimas entradas até__” e a Data Fiscal da nota de saída \(ou Data Emissão do Cupom Fiscal\);

__\[MFS591083\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

- Se a nota de entrada não for encontrada na empresa de login e estabelecimento selecionado para geração, então verificar se o parâmetro para buscar as notas nas empresas incorporadas está marcado na tela da geração\. 

     Se o parâmetro “Considerar as notas fiscais da empresa incorporada” estiver marcado:

           Buscar as notas das empresas/estabelecimentos cadastradas como incorporadas na tela de Relação de Empresa 

           Incorporadora x Incorporada\*\* para a empresa/estabelecimento da geração \(incorporadora\)\.

    Senão

          Considerar somente as notas fiscais da empresa e estabelecimento selecionados para a geração\.

\*\* Módulo Parâmetros, item Preliminares 🡪 Relação de Empresa Incorporadora x Incorporada

- Dentre todos os documentos fiscais que atendam aos critérios acima, recuperar o documento fiscal de maior a Data Fiscal\.

__Mensagem de aviso quando não identificar entradas p/uma determinada saída:__

Se nenhuma entrada for identificada para a nota de saída/cupom fiscal em questão, seja entrada referenciada na SAFX08, ou recuperada da SAFX08, gravar mensagem no log de erro: *“Não foi encontrada a última nota de entrada para o produto vendido na nota de saída/cupom fiscal\. Consultar os detalhes e pré\-requisitos da geração no help e roteiro operacional do módulo”\.*

Se a __busca da última Nota de Entrada do Produto pela nota mais recente__ encontrar mais de uma nota de entrada para a nota de saída/cupom fiscal em questão, gravar mensagem no log de erro: *“Foram encontradas mais de uma nota de entrada com data fiscal mais recente referente ao produto vendido na nota de saída/cupom fiscal\. Apenas uma delas será considerada”\. O critério de desempate será considerar a nota de entrada de maior número de documento fiscal\.*

* *

O log deve exibir as informações de identificação do item da saída \(ao menos o número, série, data e item\) para conferência do usuário\.

## <a id="_Toc68106276"></a>4\.2 – Gravação dos Dados

O total da movimentação das entradas __NÃO PODE__ ser lançado na Subapuração RS\. Mas precisamos apresentar as notas fiscais de entrada acompanhando as notas de saídas, no Relatório de Conferência da Saídas para Outras Ufs, Isentas ou Não tributadas, a fim de esclarecer o cálculo do valor do ajuste das saídas a partir dos valores das entradas\. 

Desta forma, vamos gravar apenas a tabela de Identificação dos Documentos fiscais da Subapuração \(ITEM\_APURAC\_SUBRS\_AJUSTE\) e utilizaremos o código de operação da apuração =__ 005__ – POR ENTRADAS/AQUISICOES COM CREDITO DO IMPOSTO, para não interferir na Subapuração nem no registro 1920 do SPED FISCAL\. 

__Gravação dos Resultados da Geração:__

A subapuração é composta pelas três tabelas:

- Tabela de Subapuração do RS \(registro 1920\) \- __ICT\_SUB\_APURACAO\_RS__
- Tabela dos Ajustes da Subapuração do RS \(registro 1921\) \- __ITEM\_APURAC\_SUBRS__
- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\) \- __ITEM\_APURAC\_SUBRS\_AJUSTE__

Cada documento fiscal de entrada recuperado é gravado na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE__, relacionando à nota de saída\. O código de operação da apuração considerado é __005__ – POR ENTRADAS/AQUISICOES COM CREDITO DO IMPOSTO e a Subapuração parametrizada em Dados Iniciais\.  O total dessas notas não será gravado nas tabelas __ITEM\_APURAC\_SUBRS__ e __ICT\_SUB\_APURACAO\_RS__\.

O Resultado desta geração pode ser conferido através do Relatório de Conferência das Saída para Outras Ufs, Isentas ou Não tributadas disponível no módulo\.

### <a id="_Toc68106277"></a>4\.2\.1 \- Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração \(ITEM\_APURAC\_SUBRS\_AJUSTE\)

Os documentos fiscais de entrada recuperados da SAX07 / SAFX08 serão gravados__ item a item__, na tabela conforme definido a seguir\. 

Junto aos dados do documento fiscal de entrada será gravada a identificação da nota fisca de saída que foi referência para a recuperação da entrada\.

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

__Preencher com “005”__ – POR ENTRADAS/AQUISICOES COM CREDITO DO IMPOSTO 

Mesmo código gravado para o registro pai na tabela Ajustes da Subapuração __ITEM\_APURAC\_SUBRS__\.

Chave lógica de identificação do registro\.

__UK__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Mesmo sequencial gravado para o registro pai na tabela Ajustes da Subapuração __ITEM\_APURAC\_SUBRS__\.

Chave lógica de identificação do registro\.

__UK__

__Código da Empresa de Origem__

COD\_EMPRESA\_ORIG

__\[MFS591083\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

Código da empresa do documento fiscal de entrada \(SAFX07\)\.

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

Preencher com o ID\_REG\_AJUSTE da __nota de saída/cupom__ \(ID\_REG\_AJUSTE da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)

__Número do Item__

NUM\_ITEM

Número do item de mercadoria do documento fiscal de entrada \(campo “18\-Item Nota Fiscal” da SAFX08\)

__Núm Doc Fiscal Referência__

NUM\_DOCFIS\_REF

Não preencher\. 

Este campo será preenchido apenas para notas de saída\.

__Série Doc Fiscal Referência__

SERIE\_DOCFIS\_REF

Não preencher\.

Este campo será preenchido apenas para notas de saída\.

__Subsérie Doc Fiscal Referência__

S\_SER\_DOCFIS\_REF

Não preencher\.

Este campo será preenchido apenas para notas de saída\.

__Data Doc Fiscal Referencia__

DAT\_DI

Não preencher\.

Este campo será preenchido apenas para notas de saída\.

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

Obs: No caso da parametrização do produto “Por Código” o produto da nota pode ser um Produto Principal ou um Produto Associado\.

__Produto Principal__

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

\[__MFS47349\]__

Preenchimento depende da Parametrização do Produto:

- Caso o produto do item da nota de entrada tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\), então: 

Preencher esse campo com o __Produto Principal__ \(grupo, indicador e código\)\.

- Caso o produto do item da nota de entrada tenha sido parametrizado por NCM ou por CEST \(menu Parâmetros 🡪 Produtos 🡪 Por NCM ou Por CEST\), então: 

Preencher esse campo com o __Produto do Item__ de mercadoria da nota de entrada \(campos 13 e 14 da SAFX08\)\.

Regra Prática: considerar o Produto Principal gravado nos campos GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE para a__ nota de Saída/cupom__\.

__Medida da Origem__

GRUPO\_MEDIDA\_ORIG,

COD\_MEDIDA\_ORIG

Preencher com a unidade de __medida do item__ de mercadoria da __nota de entrada__ \(campo 25 da SAFX08\)\.

__Medida de Destino__

GRUPO\_MEDIDA\_DEST COD\_MEDIDA\_DEST,

Preencher com a unidade de __medida do Produto__ \(campo 14 da SAFX2013\)\.

\(GRUPO\_MEDIDA\_DEST, COD\_MEDIDA\_DEST da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)\.

\[__MFS47349\]__

Preenchimento depende da Parametrização do Produto:

- Caso o produto do item da nota de entrada tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\), então: 

Preencher com a unidade de medida do __Produto Principal__ \(campo 14 da SAFX2013\)\.

- Caso o produto do item da nota de entrada tenha sido parametrizado por NCM ou por CEST \(menu Parâmetros 🡪 Produtos 🡪 Por NCM ou Por CEST\), então: 

Preencher com a unidade de medida do Produto da __nota de Saída/cupom__ \(campo 14 da SAFX2013\)\. __\(\*\)__

Regra Prática: considerar a Unidade de Medida gravada campo GRUPO\_MEDIDA\_DEST, COD\_MEDIDA\_DEST da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE para a __nota de Saída/cupom__\.

 

__\(\*\)__ Não vamos considerar a unidade de medida do Produto relacionado ao item de mercadoria da nota de entrada \(campo 14 da SAFX2013\) e sim o produto da nota de saída\. Motivo: o cadastro do produto \(SAFX2013\) pode sofrer variações ao logo do tempo, e a unidade de medida do produto relacionado a nota de entrada pode ser diferente da unidade de medida do mesmo produto relacionado a nota de saída/cupom\. Para evitar essa diferença, vamos considerar a Unidade de Medida do produto relacionado a nota de saída/cupom, que já está armazenada no campo de Medida de Destino\.

Este mesmo tratamento é feito no Cálculo do Valor do Confronto do Ressarcimento SP\.

__Fator de Conversão__

FAT\_CONV

Fator de conversão da unidade de __medida do Item__ da nota de entrada para a unidade __medida do Produto\.__

Considerar a __Medida de Origem__ e a __Medida de Destino__ preenchidas nos campos anteriores\.

Para gerar este campo, é necessário verificar se na nota \(SAFX08\) foi utilizada a mesma unidade de medida do cadastro do produto \(unidade de medida da SAFX2007\), e caso não, obter o fator de conversão\.

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso o campo será preenchido com o número 1;

__Senão __

       Nesse caso o campo será preenchido com o fator de conversão obtido nas tabelas de conversão 

      de medida, conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de 

      medidas do Módulo DW \(menu “*Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medida*”\), 

      da seguinte forma:

       \- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

       \- Caso não exista, pesquisa o fator na tabela de conversão padrão;

      Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será 

      gerado com o campo FATOR DE CONVERSÃO sem informação, e será gravada a seguinte 

       mensagem de erro no log: 

      “*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será *

*      gerado sem esta informação”\. *\(o primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.

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

__Quantidade do item __

QTDE\_ITEM

Quantidade do item de mercadoria do documento fiscal de entrada\. \(campo “24\-Quantidade” da SAFX08\)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Truncar Arredondar o valor para 3 decimais\. Esta decisão foi tomada pois no relatório não tem espaço para apresentar 6 casas decimais\. Desta forma tomamos a decisão de trabalhar apenas com 3 casas decimais\. Portanto a geração já deve trabalhar com a quantidade com 3 decimais para nao dar diferença no cálculo do valor do ajuste por questões de arredondamento\. 

__Quantidade Convertida do item __

QTDE\_CONV

__Se__ o “Fator de Conversão” gerado no campo anterior = 1, então:

      Nesse caso este campo será preenchido com a mesma quantidade gerada no campo “Quantidade do item”;

__Senão __

      Se o “Fator de Conversão” gerado no campo anterior não estiver preenchido:

Preencher este campo com zero\.

      Senão:

Nesse caso o campo será preenchido com a quantidade do item \(SAFX08\) convertida para a unidade de medida do cadastro do produto, utilizando o fator de conversão obtido\. Assim, será a multiplicação dos seguintes campos gerados acima:

              

                                          \[Quantidade do item \* Fator de Conversão\]

OBS\.: Nesta obrigação *não* será utilizado o campo “137\-Quantidade Convertida” da SAFX08\. Este campo é utilizado por alguns clientes para informar na nota a quantidade já convertida, e quando preenchido, é utilizado em alguns casos \(como na CAT 42/18 por exemplo\)\. 

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Truncar Arredondar o valor para 3 decimais\. Esta decisão foi tomada pois no relatório não tem espaço para apresentar 6 casas decimais\. Desta forma tomamos a decisão de trabalhar apenas com 3 casas decimais\. Portanto a geração já deve trabalhar com a quantidade com 3 decimais para nao dar diferença no cálculo do valor do ajuste por questões de arredondamento\.

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

Não preencher\.

Este campo será preenchido apenas na geração das notas de saída para consumidor final\.

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

Os valores acima relacionados são do Item de mercadoria do documento fiscal de entrada\.

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

Os valores acima relacionados são do Item de mercadoria do documento fiscal de entrada\.

*OBS: Esta regra para obter o valor do ICMS\-ST é a mesma utilizada na Portaria CAT 158 \(no preenchimento do campo” Valor Unitário da Base de Cálculo do ICMS\-ST da Entrada” do C176, Sped Fiscal\)\. Sendo que, para o C176 utilizamos os campos referentes ao valor da base de cálculo, ao invés do valor do imposto\. Ou seja, lá são utilizados os campos 61, 144 e 106, ao invés dos campos 52, 145 e 107\. *

__Obs__: As regras de preenchimento dos campos Valor do ICMS, Valor do ICMS\-ST e Valor do ST FECEP estão baseadas na regra do campo “__Valor Total ICMS – Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP \(ver MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor do ICMS\-ST FECEP__

VLR\_FECP\_ICMS\_ST

Campo FECEP ICMS\-ST do Item de mercadoria do documento fiscal de entrada \(“140\-FECEP ICMS\-ST \- VLR\_FECP\_ICMS\_ST” da SAFX08\)\.

__Obs__: As regras de preenchimento dos campos Valor do ICMS, Valor do ICMS\-ST e Valor do ST FECEP estão baseadas na regra do campo “__Valor Total ICMS – Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP \(ver MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3\.doc\)\.

__Valor Unitário de ST __

VLR\_UNIT

Preencher o valor unitário considerando o procedimento abaixo:

Se Quantidade Convertida do Item \(\*\) for zero, então:

    Preencher este campo com zero\.

Senão

    Preencher este campo com:

    \[Valor do ICMS \+ Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP \] / Quantidade Convertida do item \(\*\)

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Caso o valor resultante tenha mais de duas casas decimais, truncar arredondar o valor para duas decimais\.

\(\*\) Quantidade Convertida do Item da __nota de entrada__ que está sendo gravada\.

__Valor do Ajuste__

*\(campo 09 do registro 1923\)*

VLR\_AJUSTE

Calcular o valor do ajuste considerando os procedimentos abaixo:

Valor do Ajuste = \[ Valor Unitário de ST \]  \* Quantidade Convertida do item da __Nota de Saída/cupom__ __\(\*\*\)__

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Caso o valor resultante tenha mais de duas casas decimais, truncar arredondar o valor para duas decimais\.

__\(\*\*\)__ A nota/cupom de saída que foi objeto de recuperação da nota de entrada que está sendo gravada\.

__Obs__: Regra semelhante ao cálculo do valor de confronto do campo “__Valor Confronto \- ICMS Efetivo Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP, \(ver MTZ\-Ressarc\-SP\-Calculo\_Vlr\_Confronto\_Saidas\.doc\)\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “4”\.

‘__4’ __– lançamento gerado via processo de geração da saida para outras Ufs, Isentas ou Não Tributadas

__Número do Processo__

NUM\_PROCESSO

Preencher com o número do processo da geração\.

# <a id="_Toc68106278"></a>ETAPA 3 – ATUALIZAÇÃO DO VALOR DO AJUSTE DAS SAÍDAS PARA OUTRAS Ufs, ISENTAS OU NÃO TRIBUTADAS

## <a id="_Toc68106279"></a>5\.1 – Recuperação dos Dados e Processamento

Origem dos dados:  \- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

			\(ITEM\_APURAC\_SUBRS\_AJUSTE\)

Critérios da recuperação das Notas de Saída e Cupons Fiscais para outras Ufs, Isentas ou Não Tributadas:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado = ‘__4’ __– lançamento gerado via processo de geração da saida para outras Ufs, Isentas ou Não Tributadas\. 

Para cada documento fiscal/cupom de saída recuperado, buscar na tabela ITEM\_APURAC\_SUBRS\_AJUSTE a nota fiscal de entrada relacionada, que foi gravada na etapa 2\. Recuperar o Valor do Ajuste\.

Critérios da recuperação das Notas de Entrada:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Campo interno da tabela \(ID\_REG\_AJUSTE\_REG\) = identificação do ajuste gerado para a nota de saída 
- Indicador de Lançamento Digitado/calculado = ‘__4’ __– lançamento gerado via processo de geração da saida para outras Ufs, Isentas ou Não Tributadas 

A nota de entrada pode ou não ser encontrada\.

## <a id="_5.2_–_Gravação"></a><a id="_Toc68106280"></a>5\.2 – Gravação dos Dados

__Gravação dos Resultados da Geração:__

Atualizar o valor do ajuste do documento fiscal/cupom de saída na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE__ com o valor do ajuste da entrada relacionada\. 

Consolidar os valores de ajuste dos documentos ficais/cupom de saída e gerar um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, e atualizados na __ICT\_SUB\_APURACAO\_RS__, recalculando a Subapuração\.

O Resultado desta geração pode ser conferido através do Relatório de Conferência disponível no módulo\.

### <a id="_Toc68106281"></a>5\.2\.1 – Atualização do Valor do Ajuste na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração \(ITEM\_APURAC\_SUBRS\_AJUSTE\)

Atualizar o valor do ajuste do documento fiscal de saída na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE__ com o valor do ajuste da entrada relacionada\.

__Valor do Ajuste__

*\(campo 09 do registro 1923\)*

VLR\_AJUSTE

Calcular o valor do ajuste considerando os procedimentos abaixo:

Valor do Ajuste =  \[ Valor Unitário de ST \]  \* Quantidade Convertida do item da __Nota de Saída/cupom__ __\(\*\*\)__

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Caso o valor resultante tenha mais de duas casas decimais, truncar arredondar o valor para duas decimais\.

__\(\*\*\)__ A nota/cupom de saída que foi objeto de recuperação da nota de entrada que está sendo gravada\.

__Obs__: Regra semelhante ao cálculo do valor de confronto do campo “__Valor Confronto \- ICMS Efetivo Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP, \(ver MTZ\-Ressarc\-SP\-Calculo\_Vlr\_Confronto\_Saidas\.doc\)\.

### <a id="_Toc68106282"></a>5\.2\.2 \- Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\)

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

Considerar o Item da Apuração do “Lançamento de Estorno de Créditos para Saídas de Mercadorias destinada a outros Estados ou isentas ou não tributadas”\.

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

Considerar a Descrição do “Lançamento de Estorno de Créditos para Saídas de Mercadorias destinada a outros Estados ou isentas ou não tributadas”\.

__Código do Ajuste ICMS__

*\(campo 02 do registro 1921\)*

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Considerar o Código de Ajuste Sped Fiscal do “Lançamento de Estorno de Créditos para Saídas de Mercadorias destinada a outros Estados ou isentas ou não tributadas”\.

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com “2”\.

Este valor signfica que o lançamento possui documentos associados, que estão gravados na tabela ITEM\_APURAC\_SUBRS\_AJUSTE\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com __“4”__\.

‘__4’ __– lançamento gerado via processo de geração da saida para outras Ufs, Isentas ou Não Tributadas

### <a id="_Toc68106283"></a>5\.2\.3 \- Gravação dos Dados na Tabela de Subapuração do RS \(ICT\_SUB\_APURACAO\_RS\)

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

# <a id="_Toc68106284"></a>Gravação dos Dados na Tabela de Controle da Execução das Gerações 

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

 

