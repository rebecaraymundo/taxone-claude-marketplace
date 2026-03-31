# MTZ-Ressarc-RS-Geracao_Movimentos_Entradas_Nao_Varejista

- **Fonte:** MTZ-Ressarc-RS-Geracao_Movimentos_Entradas_Nao_Varejista.docx
- **Modificado:** 2024-01-22
- **Tamanho:** 143 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 048/2018\) 

Geração dos Movimentos – Entradas Não Varejista 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração 🡪 IN\-RE 048/2018 🡪 Geração dos Movimentos \(opção “Gerar Entradas”\)

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS29437__

Liliane Videira Assaf

Geração dos movimentos das entradas para Não Varejistas\.

20/07/2019

__MFS28012__

Liliane Videira Assaf

Inclusão de tratamento para recuperação de mais de uma nota de entrada mais recente do produto vendido\.

12/09/2019

__MFS62415__

Liliane Videira Assaf

Tratamento para Cupons Fiscais que foram incluídos na Geração da Saída para Consumidor Final

18/03/2021

__MFS47349__

Liliane Videira Assaf

Tratamento de Produtos Associados na geração dos movimentos

30/03/2021

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

23/09/2021

__MFS591083__

Liliane Assaf

Tratamento das Incorporações de Empresas/Estabelecimentos

22/01/2024

Sumário

[1\.	Introdução	3](#_Toc18676445)

[2\.	Recuperação dos Dados e Processamento	4](#_Toc18676446)

[3\.	Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\)	11](#_Toc18676447)

[4\.	Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(registro 1921\)	18](#_Toc18676448)

[5\.	Gravação dos Dados na Tabela de Subapuração do RS \(registro 1920\)	20](#_Toc18676449)

[6\.	Gravação dos Dados na Tabela de Controle da Execução das Gerações	24](#_Toc18676450)

# <a id="_Toc18676445"></a>Introdução 

A geração dos movimentos de entrada é uma das gerações que compõe o processo de Geração dos Movimentos, responsável por calcular a Subapuração RS\.

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

Esta geração será executada caso o contribuinte seja Não Varejista e a opção “Gerar entradas” seja selecionada na tela de geração\. Veja o tópico 4 do documento principal da Geração dos Movimentos \(MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx\)\.

__Pré\- requisito:__

A geração dos movimentos de entrada \(Não Varejista\) tem como pré\-requisito a geração dos movimentos de saída para consumidor final\.

Com base na movimentação de saída para consumidor final é que as notas fiscais de entrada serão recuperadas\. 

Toda vez que acontecer uma regeração dos movimentos de saída, a movimentação da entrada \(Não Varejista\) também deverá ser regerada para não ocorrer incompatibilidade\. A regra para este controle está definida no documento principal da Geração dos Movimentos \(MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx\)\.

__\[MFS47349\]__

__Quanto a Parametrização de Produtos Associados__:

A recuperação dos movimentos de entradas e saídas é feita considerando o produto Principal seus os produtos Associados, definidos na Parametrização de Produtos, opção Por Código\. 

No relatório de conferência, os documentos fiscais são apresentados com seus respectivos produtos e agrupados em nome do Produto Principal\. 

No Sped Fiscal, o documento fiscal é apresentado no registo 1923 com o produto que de fato está escriturado na nota, não havendo forma de demonstrar a relação do Produto Principal com os Produtos Associados\. Esta relação só é possível de ser observada dentro do módulo Ressarcimento ICMS\-ST RS, através dos relatórios de conferência dos movimentos\.

# <a id="_Toc350763252"></a><a id="_Toc18676446"></a>Recuperação dos Dados e Processamento

__Visão Geral__: 

A recuperação das notas fiscais de entrada depende do movimento de saída para consumidor final, resultante da execução da “Geração das Saídas para Consumidor Final” \(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\.docx\)\.

A partir do item de mercadoria da nota de saída será recuperada a última nota fiscal de entrada do produto vendido na nota de saída\.  

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

O total da movimentação das entradas gera um lançamento na Subapuração RS à crédito, carregando todo conjunto de tabelas da Subapuração, que são base para a geração dos registros 1920, 1921 e 1923 do SPED FISCAL\.

Tabelas que compõe a Subapuração: 

- Subapuração RS \(registro 1920\)
- Ajustes da Subapuração \(registro 1921\) 
- Identificação dos Documentos fiscais \(registro 1923\)

Na tabela de Subapuração \(registro 1920\) será gravado o campo de __Outros Créditos__ com o total da movimentação de Entradas\.  Na tabela de Ajustes da Subapuração \(registro 1921\) um lançamento é realizado com o total da movimentação de Entradas e código de ajuste especificado na IN048/2018, que será parametrizado na tela de Dados Iniciais\. Na tabela de Identificação dos Documentos fiscais \(registro 1923\) são gravadas as notas fiscais de entrada que foram recuperados neste processo, com a identificação da nota de saída\.

Obs\.: 

1. A notas de devolução __NÃO__ são consideradas nesta geração, pois segundo Art\. 25 do Decreto 37699/97 – Livro III, há uma forma particular de tratamento que não seja através da Subapuração\. Esta geração não irá descartar as notas de devolução\.  Cabe ao usuário não parametrizar os CFOPs relativos à devolução, para que as mesmas não sejam consideradas\.

__Recuperação do Movimento de Saída para Consumidor Final \(Nota ou Cupom\)__

Origem dos dados:  

- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\_AJUSTE\)

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

- SAFX07 / SAFX08 \- Tabelas dos Documentos Fiscais \(DATAMART\)
- Tabelas dos Cupons Fiscais \(SAFX993 / SAFX994\);

Critérios da recuperação da movimentação do período:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Única" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Única" marcado

- Indicador de Lançamento Digitado/calculado = ‘__2__’ \- lançamento gerado via processo de geração da saída a Consumidor Final\.

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

Os critérios abaixo servem tanto para a busca da entrada pela referência na nota de saída, quanto para a busca pela entrada mais recente do produto\.

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

- __Produto__ relacionado item de mercadoria da __nota de entrada__ = __Produto__ relacionado ao item de mercadoria da __nota/cupom de Saída __

\(esta relação deve ser feita pelo grupo, indicador e código do produto\)

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

\(esta relação deve ser feita pelo grupo, indicador e código do produto\)\.

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

__Mensagem de aviso quando mais de uma nota de entradas for recuperada p/uma determinada saída:__

<a id="_Hlk19203632"></a>

Se a __busca da última Nota de Entrada do Produto pela nota mais recente__ encontrar mais de uma nota de entrada para a nota de saída/cupom fiscal em questão, gravar mensagem no log de erro: *“Foram encontradas mais de uma nota de entrada com data fiscal mais recente referente ao produto vendido na nota de saída/cupom fiscal\. Apenas uma delas será considerada”\. O critério de desempate será considerar a nota de entrada de maior número de documento fiscal\.*

* *

O log deve exibir as informações de identificação do item da saída \(ao menos o número, série, data e item\) para conferência do usuário\.

__Gravação dos Resultados da Geração:__

Os movimentos recuperados são armazenados em três tabelas que serão utilizadas posteriormente para geração dos registros 1920, 1921, 1923 do Sped Fiscal:

- Tabela de Subapuração do RS \(registro 1920\) \- __ICT\_SUB\_APURACAO\_RS__
- Tabela dos Ajustes da Subapuração do RS \(registro 1921\) \- __ITEM\_APURAC\_SUBRS__
- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\) \- __ITEM\_APURAC\_SUBRS\_AJUSTE__

Cada documento fiscal de entrada recuperado é gravando na tabela __ITEM\_APURAC\_SUBRS\_AJUSTE__ relacionados ao lançamento e Subapuração parametrizados em Dados Iniciais\. 

Os documentos ficais recuperados são consolidados e geram um registro na tabela __ITEM\_APURAC\_SUBRS__, que é o lançamento na Subapuração cujo código de operação, descrição e código de ajuste foram parametrizados em Dados Iniciais\. 

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, e atualizados na ICT\_SUB\_APURACAO\_RS, recalculando a Subapuração RS\.

O Resultado desta geração pode ser conferido através do Relatório de Conferência disponível no módulo, e na emissão da Subapuração RS\.

# <a id="_Toc18676447"></a>Gravação dos Dados na Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\)

Os documentos fiscais de entrada recuperados da SAX07 / SAFX08 serão gravados__ item a item__, na tabela conforme definido a seguir\. 

Junto aos dados do documento fiscal de entrada será gravada a identificação da nota fiscal/cupom fiscal de saída que foi referência para a recuperação da entrada\.

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

Considerar o Item da Apuração do “Lançamento de Outros Créditos para Entradas de Mercadorias”\.

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

Preencher com o ID\_REG\_AJUSTE da __nota de saída/cupom fiscal__ \(ID\_REG\_AJUSTE da tabela de ajustes ITEM\_APURAC\_SUBRS\_AJUSTE\)

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

Preencher com o campo Modelo do documento de entrada \(campo 13 da SAFX07\)\.

__Código Fiscal__

COD\_CFOP

Preencher com o Código CFOP do item de mercadoria da nota de entrada \(campo 22 da SAFX08\)

__Natureza da Operação__

COD\_NATUREZA\_OP

Preencher com o Código da Natureza de Operação do item de mercadoria da nota de entrada \(campo 23 da SAFX08\)

__Produto da Nota \(grupo, ind, código\)__

GRUPO\_PRODUTO,

IND\_PRODUTO,

COD\_PRODUTO,

DSC\_PRODUTO

Preencher com o produto do item de mercadoria da nota de entrada \(campos 13 e 14 da SAFX08\)\.

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

Preencher com a unidade de __medida do Item__ de mercadoria da __nota de entrada__ \(campo 25 da SAFX08\)\.

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

    \[Valor do ICMS \+ Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\] / Quantidade Convertida do item \(\*\)

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Caso o valor resultante tenha mais de duas casas decimais, truncar arredondar o valor para duas decimais\.

\(\*\) Quantidade Convertida do Item da __nota de entrada__ que está sendo gravada\.

__Valor do Ajuste__

*\(campo 09 do registro 1923\)*

VLR\_AJUSTE

Calcular o valor do ajuste considerando os procedimentos abaixo:

Valor do Ajuste =  \[Valor Unitário de ST \]  \* Quantidade Convertida do item __Nota de Saída/Cupom__ __\(\*\*\)__

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Caso o valor resultante tenha mais de duas casas decimais, truncar arredondar o valor para duas decimais\.

__\(\*\*\)__ A nota de saída \(ou cupom fiscal\) que foi objeto de recuperação da nota de entrada que está sendo gravada\.

__Obs__: Regra semelhante ao cálculo do valor de confronto do campo “__Valor Confronto \- ICMS Efetivo Entrada__” da tabela dos movimentos da Ficha 3 do Ressarcimento SP, \(ver MTZ\-Ressarc\-SP\-Calculo\_Vlr\_Confronto\_Saidas\.doc\)\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “__3__”\.

3 – lançamento gerado via processo de geração das entradas\.

__Número do Processo__

NUM\_PROCESSO

Preencher com o número do processo da geração\.

# <a id="_Toc18676448"></a>Gravação dos Dados na Tabela dos Ajustes da Subapuração do RS \(registro 1921\)

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

Considerar o Item da Apuração do “Lançamento de Outros Créditos para Entradas de Mercadorias”\.

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

3 – lançamento gerado via processo de geração das entradas\.

# <a id="_Toc18676449"></a>Gravação dos Dados na Tabela de Subapuração do RS \(registro 1920\)

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

__OBS__: Estes campo sempre ficará zerado, pois nenhuma das gerações existentes hoje no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

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

# <a id="_Toc18676450"></a>Gravação dos Dados na Tabela de Controle da Execução das Gerações 

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

 

