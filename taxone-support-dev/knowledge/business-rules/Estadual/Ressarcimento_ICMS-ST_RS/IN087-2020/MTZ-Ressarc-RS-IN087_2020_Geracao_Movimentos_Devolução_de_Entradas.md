# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Entradas

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Entradas.docx
- **Modificado:** 2024-08-15
- **Tamanho:** 171 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Geração dos Movimentos – Devolução de Entradas 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\),

 itens: Geração à IN\-RE 087/20 à Geração dos Movimentos 

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS48753__

Liliane Videira Assaf

Criação da funcionalidade\.

Não estamos trabalhando com Produtos Associados, apesar do documento mencionar tal parametrização em algumas regras\.

22/12/2020 

__MFS65137__

Liliane Videira Assaf

Retirada dos parâmetros da tela de geração, pois foram para a Tela de Dados Iniciais:

\- Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)

\- Tratamento p/ Entrada objeto da Devolução de períodos anteriores à adoção da sistemática da IN\-RE 087/20:

Valores Unitários Médios recuperados:

\( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

\( \) da própria Nota de Entrada referenciada pela Devolução

Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]

13/05/2021

__MFS64191__

Liliane Videira Assaf

IN\-RE 037/21:

Passar a considerar o código da operação 780 na geração dos movimentos de devolução de entrada, gerando o código motivo RS413\. 

- 780 \- Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

15/07/2021

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

01/10/2021

__MFS81749__

Liliane Assaf

Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473

15/03/2022

__MFS84243__

Andréa Rocha

Inclusão da verificação da data fiscal da nota fiscal para recuperar a parametrização por Produto/NCM/CEST\. 

12/04/2022

__MFS90131__

Liliane Assaf

Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte\. 

01/08/2022

__MFS446958__

Andréa Rocha

Alteração da forma de preenchimento do campo Data Escrita Fiscal do Documento de Referência\.

24/08/2022

__MFS520407__

Andréa Rocha

Alteração da forma de preenchimento do campo Data Escrita Fiscal do Documento de Referência\.

15/03/2023

__MFS543860__

Andréa Rocha

Tratamento do parâmetro para definir se o valor do FECEP está embutido nos valores de ICMS não destacado e não escriturado\.

19/06/2023

Sumário

[1\.	Introdução	1](#_Toc62485213)

[2\.	Recuperação dos Dados e Processamento	1](#_Toc62485214)

[2\.1 – Recuperação das Notas Fiscais de Devoluções das Entradas	1](#_Toc62485215)

[2\.2 – Recuperação dos Valores Unitários Médios do Inventário	1](#_Toc62485216)

[3\.	Gravação dos Dados na Tabela dos Movimentos	1](#_Toc62485217)

[4\.	RELATORIO DE CONFERÊNCIA	1](#_Toc62485218)

# <a id="_Toc62485213"></a>Introdução 

Esse documento tem como objetivo definir a geração das __Devoluções das Entradas__ que consiste em:

- Recuperar as notas fiscais de devolução de entradas do período;
- Recuperar as notas de entradas referenciadas pelas notas de devolução;
- Calcular os valores untários médios ponderados com base nos valores da nota de entrada;
- Gravar as notas de devolução e suas respectivas entradas na tabela específica dessa geração \(EST\_ST\_RS\_NF\_DEV\_ENT\);
- Gerar o Relatório de Conferência a partir da tabela EST\_ST\_RS\_NF\_DEV\_ENT, demonstrando o detalhamento do cálculo dos valores que serão apresentados no __C186__ do Sped Fiscal\.

Esse processamento é base para a geração do registro __C186__\. Todos os registros gravados na tabela EST\_ST\_RS\_NF\_DEV\_ENT numa próxima etapa serão copiados para a tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV de onde parte a geração do registro C186 no módulo SPED FISCAL\.  Ou seja, as regras que definem o C186 são realizadas nessa fase\.

__Nota__: A parametrização dos Produtos Associados se aplica apenas na geração da IN048/18\. Não se aplica a IN087/20\!

# <a id="_Toc350763252"></a><a id="_Toc62485214"></a>Recuperação dos Dados e Processamento

## <a id="_2.1_–_Recuperação_1"></a><a id="_Toc60248158"></a><a id="_Toc62485215"></a>2\.1 – Recuperação das Notas Fiscais de Devoluções das Entradas

A Devolução de Entrada é uma nota de saída carregada na SAFX07/SAFX08\.

A nota de entrada que está sendo devolvida, também está carregada na SAFX07/SAFX08\. 

A associação da nota de devolução com a nota de entrada é feita utilizando os campos de referência da SAFX08 \(117, 118, 119, 102\) são preenchidos com os dados de identificação da nota fiscal de entrada;

*Observação:*

*Não estamos utilizando a tabela de referência SAFX192, pois ela não tem tratamento para devolução de entradas \(o campo “Tipo de Referência” não tem opção de “Devolução \(Saída\) x Documentos de Origem \(Entradas\)\)\.*

*O ressarcimento PR está trabalhando da mesma forma, ou seja, devoluções de entrada com a SAFX08 e devoluções de saídas com a SAFX192 ou SAFX08*\.

<a id="_2.1_–_Recuperação"></a>__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais \(DATAMART\)

__Critérios da recuperação das Notas Fiscais de Devolução: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Nota fiscal de devolução \(NORM\_DEV = “2”\);

\- Nota de Saída \(MOVTO\_E\_S = “9”\);

\- Modelo = 01, 1B, 04, 55, 65 

\- Somente notas *não canceladas*;

\- Somente notas *com itens*;

__\[MFS84243\] __Inclusão da verificação da data fiscal da nota fiscal para recuperar a parametrização por Produto/NCM/CEST\.

\- O produto do item deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros à Produtos à Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros à Produtos à Por CEST*”\. 

  Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.  Somente devem ser considerados os produtos em que a data fiscal da nota fiscal esteja compreendida entre a data inicial de vigência e a data final de vingência da parametrização\.  Quando a data final de vigência não estiver preenchida, a parametrização ainda está válida, ou seja, o produto será considerado\.

   No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a parametrização por código, deve\-se considerar também os produtos associados\. Ou seja, o produto da nota deve constar como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\), ou ser um produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\)\.  Módulos de ressarcimento de SC e SP trabalham com produto associado\.

   Os produtos “associados” são produtos cuja movimentação será demonstrada na Ficha 3 em nome do produto principal parametrizado\. 

  A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

 \- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros à \(IN\-RE 087/20\) à Operações*” para a seguinte operação:

- “Entradas \(e Devoluções\)” \(código parâmetro 771\)

__MFS64191__

- “Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)” \(código parâmetro 780\)

Recuperar as seguintes informações da nota de devolução \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de devolução;

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

__\- Caso o produto do item da nota de devolução tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) recuperar o Produto Principal \(grupo, indicador e código\) e a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.__

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

__\[[MFS81749](https://jira.thomsonreuters.com/browse/MFS-81749" \o "TICKET 35007 - DW - ESTADUAL - Ressarcimento ICMS-ST RS - Produtos Farmacêuticos  - Não devem ser gerados os registros C180, C181, C185, C186, H030, nem cálculo de média de inventário para produtos parametrizados como farmacêuticos (parte 3))\]__

__Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores:__

<a id="_Hlk75258358"></a>Verificar os critérios a seguir:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não; 
- <a id="_Hlk78292438"></a>__Produto__ do Item da Nota de Devolução da Entrada estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

<a id="_Hlk75258481"></a>Se os dois critérios forem atendidos, então:

            O item de mercadoria dessa nota de devolução da entrada não será gravado na tabela EST\_ST\_RS\_NF\_DEV\_ENT, e a seguinte mensagem será exibida no log:

“*Registro C186: Nota de Devolução de Entrada de produto farmacêutico amparada pelo art 103/104 do Livro III do RICMS não será gerada no C186”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução de Entrada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Obsevação importante: Este tratamento deve ser aplicado antes da verificação se a devolução possui referência para nota de entrada\. Caso contrário cairá na mensagem *Registro C186: Nota de Devolução de entrada não considerada na geração, pois não existe referência para operação de origem* indevidamente\.

Para cada item de mercadoria da nota de devolução vamos recuperar a\(s\) nota\(s\) de entradas\(s\) devolvida\(s\)\.

Primeiro buscar a entrada a partir dos campos de referência da SAFX08 \(117, 118, 119, 102\)\.

Caso esses campos não estejam preenchidos, exibir a seguinte mensagem no log e não gravar a nota de devolução na tabela EST\_ST\_RS\_NF\_DEV\_ENT:

*         “Registro *<a id="_Hlk98245202"></a>*C186: Nota de Devolução de entrada não considerada na geração, pois não existe referência para operação de origem\.*

*          Favor informar a entrada que está sendo devolvida utilizando os campos de referência da SAFX08 \(117, 118, 119, 102\)\.”*

                                \(o log deve exibir a identificação do item da devolução para conferência do usuário\)

__Recuperação das entradas referenciadas pela SAFX08:__

Caso o item de mercadoria da nota de devolução possua os campos 117, 118, 119, 102 \(SAFX08\) preenchidos, recuperar o documento de referência \(nota de entrada devolvida\), a partir dos critérios descritos abaixo: 

\- Empresa                  = Código da empresa da nota de devolução

\- Estabelecimento      = Código do estabelecimento da nota de devolução

\- Movimento E/S        = deve ser uma nota de entrada \(MOVTO\_E\_S <> “9”\) 

\- Normal/Devolução   = deve ser uma nota normal \(NORM\_DEV = ‘1’\)

\- Pessoa Fis/Jur         = mesma pessoa fis/jur da nota de devolução

\- Número                    = campo “117\-Número do Documento Fiscal de Referência” da nota de devolução

\- Série                         = campo “118\-Série do Documento Fiscal de Referência “da nota de devolução

\- Subsérie                  = campo “119\-Subsérie do Documento Fiscal de Referência “da nota de devolução

\- Data de Emissão     = campo “102\-Data DI / Data Doc Refer” da nota de devolução

\- Produto                    = produto do item da nota de devolução \(grupo,indicador e código\); 

Recuperar as seguintes informações da nota de entrada referenciada \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de entrada referenciada;

\- 11 \- Data da Emissão \- DATA\_EMISSAO \(SAFX07\)

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

\- 64 \- Valor Contábil do Item \- VLR\_CONTAB\_ITEM \(SAFX08\) 

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de saída será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

__OBS__: O uso dos campos de referência da SAFX08 da nota de devolução para identificar a nota de entrada, espera\-se que apenas um item da nota de entrada seja recuperado\. Mas, caso seja encontrado mais de um item da nota de entrada para o produto devolvido, todos serão gravados na tabela EST\_ST\_RS\_NF\_DEV\_ENT\.  

O correto é utilizar os campos de referência da SAFX08 da nota de devolução quando apenas um item da nota de entrada está relacionado ao produto devolvido\. Caso mais de um item de entrada esteja relacionado ao produto devolvido, deve\-se utilizar a SAFX192\. E caso esse cenário existir, devemos alterar a Geração da Devolução da Entrada para trabalhar também com a SAFX192\. Na criação da rotina, fizemos uma pesquisa com os clientes e não identificamos tal necessidade\.

Crítica a ser realizada:

Caso a nota de referência não seja encontrada na base de dados, será gravada a seguinte mensagem no log: 

   “*Registro C186: Nota de Devolução de entrada não considerada na geração, pois a nota de entrada original referenciada no item da nota não foi encontrada na base de dados\.”*\. 

                                \(o log deve exibir a identificação do item da devolução para conferência do usuário\)

## <a id="_2.2_–_Recuperação"></a><a id="_Toc62485216"></a>2\.2 – Recuperação dos Valores Unitários Médios do Inventário

Segundo a IN\-RE 087/20, Tópico __19\.3\-A\.2\.2__, alínea “d” os valores untários médios a serem considerados para as devoluções, são os calculados a partir dos valores da entrada objeto da devolução\. Veja: 

”*d\) subtrair do valor apurado na alínea "c" as informações referentes a todas as devoluções de entradas de que trata a alínea "d" do subitem 19\.3\-A\.1, que corresponderá à soma das multiplicações da quantidade de cada saída em devolução pelo valor unitário que serviu de base de cálculo do imposto retido por substituição tributária para a mercadoria objeto de devolução*;”

Segundo a IN\-RE 087/20, Tópico __19\.3\-A\.1\.4\.1__, para as devoluções cuja entrada ocorreu anteriormente a 01/01/2021, os valores unitários serão recuperados do estoque de 31/12/2020\.  Veja:

*"19\.3\-A\.1\.4\.1 \- Se a entrada objeto de devolução ocorreu antes de 1º de janeiro de 2021, para o preenchimento dos campos:*

*a\) VL\_UNIT\_CONV\_ENTRADA, deverá ser utilizado o resultado da multiplicação do valor informado no campo VL\_BC\_ICMS\_ST pelo resultado da divisão do valor informado no campo VL\_ICMS\_OP pelo total da soma dos valores informados nos campos VL\_ICMS\_OP e VL\_ICMS\_ST, todos os campos do registro H030, informado conforme o subitem 19\.3\-A\.3;*

*b\) VL\_UNIT\_ICMS\_OP\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_ICMS\_OP do registro H030, informado conforme o subitem 19\.3\-A\.3;*

*c\) VL\_UNIT\_BC\_ICMS\_ST\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_BC\_ICMS\_ST do registro H030, informado conforme o subitem 19\.3\-A\.3;*

*d\) VL\_UNIT\_ICMS\_ST\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_ICMS\_ST do registro H030, informado conforme o subitem 19\.3\-A\.3\."*

*Veja o tópico *<a id="_Hlk62220183"></a>*19\.3\-A\.3:*

*“19\.3\-A\.3 \-Conforme disposto no RICMS, Livro III, art\. 25\-B, parágrafo único, I, o contribuinte deverá apresentar o registro H005, com o campo MOT\_INV igual a "06" e DT\_INV igual ao dia imediatamente anterior ao campo DT\_INI informado no registro 0000, com informações do inventário das mercadorias recebidas com substituição tributária existentes em estoque no fim do dia *__*31 de dezembro de 2020 ou do dia anterior àquele em que passar a apurar o ajuste*__*, se posterior a 1º de janeiro de 2021”\.* 

De acordo com o tópico da IN\-RE 087/20 acima descrito, as notas de entrada anteriores a 01/01/2021 devem utilizar os valores unitários apresentados no H030 – inventário de 31/12/2020 \(ou dia anterior ao primeiro mês que adotar a nova sistemática da IN\-087/20\)\. Já as notas de entradas posteriores a 01/01/2021, consideram os valores de ICMS, BC ICMS\-ST e ICMS\-ST da própria nota de entrada\.

Como solução para notas de entradas anteriores a 01/01/2021, o usuário pode escolher se considera os valores unitários do estoque \(conforme Tópico 19\.3\-A\.1\.4\.1\), ou se calcula os valores unitários a partir dos valores de ICMS, BC ICMS\-ST e ICMS\-ST presentes na nota de entrada objeto da devolução\. Essa escolha é feita através da Tela de Dados Iniciais \(Parâmetros >> IN\-RE 087/20 >> Dados Iniciais\) __\[MFS65137\]__:

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

Valores Unitários Médios recuperados:

\( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

\( \) da própria Nota de Entrada referenciada pela Devolução”

Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]

A seguir a definição da recuperação do inventário\.  A aplicação do parâmetro se dá nas regras de preechimento dos campos – tópico 3\. 

__Recuperação dos Valores Unitários da Tabela de Inventário \(X52\_INVENT\_PRODUTO\) __

__Origem dos dados__: \- Tabela do Inventário \(X52\_INVENT\_PRODUTO\)\.

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) __*= *__“Dt anterior à adoção IN\-RE087/20” informada na Tela de Dados Iniciais \(Parâmetros >> IN\-RE 087/20 >> Dados Iniciais\) __\[MFS65137\]__

\- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;

\- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) à 1, 2, 3 e 5;

\- Produto \- produto do item da nota de entrada \(grupo, indicador e código\);

Os critérios acima podem retornar mais de um registro de inventário para o mesmo produto\. 

Caso isso ocorra, considerar o registro de __menor Grupo de Contagem__ e gravar a seguinte mensagem no log\. 

“*Registro C186: Foi encontrado mais de um registro de inventário em < Dt anterior à adoção IN\-RE087/20 informada na Tela de Dados Iniciais> para o produto X\-XXXXXX\. O inventário considerado para recuperação dos valores unitários é o de Grupo Contágem Y\.”*\.  Onde X\-XXXXXX é o indicador e o código do produto e Y é o codigo do grupo de contagem\.

 \(O log deve demonstrar as informações que permita a identificação do item da Nota de Devolução da Entrada e da Entrada referenciada, exibindo o estabelecimento, a data, o número   do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Caso a consulta acima não retorne registro, gravar mensagem no log:

*“Registro C186: Não foi encontrado registro de inventário em < Dt anterior à adoção IN\-RE087/20 informada na Tela de Dados Iniciais> para o produto X\-XXXXXX, com Motivo Inventário 06\. A Nota de Devolução de entrada será gerada no C186 sem valores unitários de ICMS e ICMS\-ST e não irá compor Média Pondera Móvel dos Valores Unitários do dia DD/MM/YYYY\.*

DD/MM/YYYY é Data Fiscal da Nota de Devolução da Entrada\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Entrada e da Entrada referenciada, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Considerar as seguintes informações:

- 21 \- Valor de ICMS Médio \(VLR\_ICMS\_MEDIO\)
- 22 \- Valor de ICMS\-ST Médio \(VLR\_ICMSS\_MEDIO\)
- 43 \- Valor Base ICMS\-ST Médio \(VLR\_BASE\_ICMSS\_MEDIO\)
- 44 \- Valor FECEP Médio \(VLR\_FCP\_MEDIO\)

Pontos que pode ser objeto de futura alteração \(22/01/2021\):

1. O tratamento para o caso de existir mais de um registro de inventário na X52\_INVENT\_PRODUTO está diferente do aplicado no Cálculo da Média Ponderada na obtenção do Saldo Inicial\. No Cálculo da média todos os registros seriam considerados\. E nessa definição, apenas o registro de menor grupo de Contagem será considerado\. Se for necessário obter nessa regra o mesmo valor demonstrado no H030, haverá necessidade de alterarmos para fazer como no Cálculo da Média Ponderada\. 

# <a id="_Toc62485217"></a>Gravação dos Dados na Tabela dos Movimentos

Os documentos fiscais de Devolução recuperados serão gravados__ item a item__, com todas as referências para as notas de entradas devolvidas, conforme definido a seguir\.

__Tabela EST\_ST\_RS\_NF\_DEV\_ENT__

Os campos sinalizados com asterisco compõem a chave da tabela\.

A estrutura da tabela __EST\_ST\_RS\_NF\_DEV\_ENT__ é baseada na SAFX308\. Contém todos os campos da SAFX308 e campos a mais usados no relatorio de conferência\.

PK

Item

SAFX308

Campo

Regra de Preenchimento

Campos para relatório

\(\*\)

Código do Estabelecimento

COD\_ESTAB\_GER

Código do estabelecimento SELECIONADO na tela de geração\.

Esse campo foi criado, pois no futuro poderemos ter a geração por Inscrição Estadual Única, e nessa opção o estabelecimento selecionado na tela de geração é o centralizador, e as notas fiscais são dos estabelecimentos centralizador e centralizados\.

Não apresentar

__*Campos do layout da SAFX308 \(Item da nota de devoução com item da nota de entrada objeto da devolução\)*__

\(\*\)

01

Código da Empresa 

COD\_EMPRESA

Código da empresa da nota de Devolução da Entrada \(SAFX07\) 

Cod Empresa

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento da nota de Devolução da Entrada \(SAFX07\)

Cod Estab

\(\*\)

03

Data Escrita Fiscal

DATA\_FISCAL

Data fiscal da nota de Devolução da Entrada \(SAFX07\)

Dt Fiscal NF Devolução

\(\*\)

04

Movimento Entrada / Saída

MOVTO\_E\_S

Indicador do movimento da nota de Devolução da Entrada \(SAFX07\)

E/S NF Devolução

\(\*\)

05

Normal ou Devolução

NORM\_DEV

Indicando de Normal/Devolução da nota de Devolução da Entrada \(SAFX07\)

Norm/Dev NF Devolução

\(\*\)

06

Tipo do Documento

COD\_DOCTO 

\(IDENT\_DOCTO\)

Tipo do documento da nota de Devolução da Entrada\.

Cod Docto NF Devolução

\(\*\)

07

08

Pessoa Física/Jurídica

IND\_FIS\_JUR/ COD\_FIS\_JUR

\(IDENT\_FIS\_JUR\)

Pessoa física/jurídica da nota de Devolução da Entrada \(SAFX07\)

Ind Fis/Jur NF Devolução

Cod Fis/Jur NF Devolução

\(\*\)

09

Número do Documento Fiscal

NUM\_DOCFIS

Número do documento fiscal da Devolução da Entrada\.

Num Docfis NF Devolução

 \(\*\)

10

Série do Documento Fiscal

SERIE\_DOCFIS

Série do documento fiscal da Devolução da Entrada\.

Serie NF Devolução

 \(\*\)

11

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

Subsérie do documento fiscal da Devolução da Entrada

SubSerie NF Devolução

\(\*\)

12 13 14 15

Identificador do Item

DISCRI\_ITEM

Campo identificador do item de mercadoria da Devolução da Entrada 

\(DISCR\_ITEM da X08\_ITENS\_MERC\)\.

Num Item NF Devolução

\(\*\)

16

Espécie do Documento de Referência da Devolução

ESPECIE\_DOCTO\_DEV

Preencher com:

   1\-Nota Fiscal \(SAFX07/08\)

A identificação do documento fiscal de referência, é feita através dos campos 17 ao 30, e dependendo da espécie do documento, devem ser preenchidos, obrigatoriamente, os seguintes campos:  
Se opção = 1, devem ser preenchidos os campos 17 ao 23, e o campo 30;  
Se opção = 2, devem ser preenchidos os campos  24, 25, 26, 27 e 30;  
Se opção = 3, devem ser preenchidos os campos 27, 28, 29 e 30\.  


Não Apresentar

 \(\*\)

17

Número do Documento Fiscal de Referência

NUM\_DOCFIS\_REF

Preencher com:

   Número da nota fiscal de entrada referenciada pela devolução\.

Num Docfis NF Entrada

\(C186\-11\)

 \(\*\)

18

Série do Documento Fiscal de Referência

SERIE\_DOCFIS\_REF

Preencher com:

   Série da nota fiscal de entrada referenciada pela devolução\.

Serie NF Entrada \(C186\-10\)

 \(\*\)

19

Subsérie do Documento Fiscal de Referência

SUB\_SERIE\_DOCFIS\_REF

Preencher com:

   Subsérie da nota fiscal de entrada referenciada pela devolução\.

SubSerie NF Entrada

 \(\*\)

20

Tipo do Documento de Referência

COD\_DOCTO\_REF

\(IDENT\_DOCTO\_REF\)

Preencher com:

Tipo do documento fiscal da nota fiscal de entrada referenciada pela devolução, de acordo com a Tabela de Tipos de Documentos \(SAFX2005\)\.

Cod Docto NF Entrada

 \(\*\)

21

Data Escrita Fiscal do Documento de Referência

DATA\_FISCAL\_REF

__\[MFS446958\] __

__\[MFS520407\] __Retornar o preenchimento do campo com a data fiscal da nota\.  O tratamento 

da data de emissão será feito na geração do registro C186 do SPED\.

Preencher com:

  Data de emissão da nota fiscal de entrada referenciada pela devolução\.

  Data da Fiscal da nota fiscal de entrada referenciada pela devolução\.

Dt Fiscal NF Entrada \(C186\-13\)

 \(\*\)

22

23

Pessoa Física/Jurídica do Documento de Referência

IND\_FIS\_JUR\_REF/ COD\_FIS\_JUR\_REF

\(IDENT\_FIS\_JUR\_REF\)

Preencher com:

Pessoa física/jurídica da nota fiscal de entrada referenciada pela devolução, de acordo com a Tabela de Pessoas Físicas/Jurídicas \(SAFX04\)\.

Não Apresentar, pois é igual a Pessoa Fis/Jur da Devolução

 \(\*\)

24

Modelo do Cupom Fiscal de Referência

COD\_MODELO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

Não Apresentar

 \(\*\)

25

Número do Caixa do Cupom Fiscal de Referência

COD\_CAIXA\_ECF\_REF

\(IDENT\_CAIXA\_ECF\)

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

Não Apresentar

 \(\*\)

26

COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência

NUM\_COO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

Não Apresentar

 \(\*\)

27

Data de Emissão do Cupom Fiscal de Referência

DATA\_EMISSAO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

Não Apresentar

 \(\*\)

28

Número do Equipamento SAT do Cupom Fiscal de Referência

NUM\_EQUIP\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

Não Apresentar

\(\*\) 

29

Número do Cupom Fiscal do Referência 

NUM\_CUPOM\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado 

Não Apresentar

\(\*\)

30

Número do Item do Documento de Referência

NUM\_ITEM\_DOC\_REF

Número do Item da nota fiscal de entrada referenciada pela devolução\.

Num Item NF Entrada

\(C186\-14\)

31

Código Motivo

Campos da EFD correspondentes: 02 do C181 e 06 do C186\.

COD\_MOTIVO

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal de devolução \(vide tópico [2\.1](#_2.1_–_Recuperação_1)\):

- Para Cód\. Operação = 771 – “Entradas \(e Devoluções\)”: 

Preencher com RS400\.

__MFS64191__

- Para Cód\. Operação = 780 – “Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)”:

Preencher com RS413\.

Cod Motivo \(C186\-06\)

32

Quantidade Convertida

Campos da EFD correspondentes: 03 do C181 e 07 do C186\.

QTD\_CONV

Preencher com:

“Qtde Convertida Calculada para NF de Devolução de Entrada \(safx08\) \([QTD\_CONV\_NF\_DEV](#QTD_CONV_NF_DEV)\)”

Ver __*[Detalhamento da Nota de Devolução](#Detalha_NF_DEV)*__

Qtde Conv \(C186\-07\)

33

Unidade de Medida

Campos da EFD correspondentes: 04 do C181 e 08 do C186\.

COD\_MEDIDA

Campo 14 – Unidade de Medida do Cadastro do Produto \(SAFX2013\), do produto pertencente ao item da nota de Devolução da Entrada\. *\(ver OBS abaixo sobre os produtos associados\)*

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a unidade de medida apresentada será a __unidade do produto principal__\.

Medida

\(C186\-08\)

 

34

Valor Unitário Conv

Campos da EFD correspondentes: 12 do C181 e 15 do C186\.

VLR\_UNIT\_CONV

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”, então:

       Preencher com:

       \[ VLR\_BASE\_ICMSS\_MEDIO \* 

         \(VLR\_ICMS\_MEDIO / \(VLR\_ICMS\_MEDIO \+ VLR\_ICMSS\_MEDIO\)\) \]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_ICMS\_MEDIO: campo 21 \- Valor de ICMS Médio \(SAFX52\)
- VLR\_ICMSS\_MEDIO: campo 22 \- Valor de ICMS\-ST Médio \(SAFX52\)
- VLR\_BASE\_ICMSS\_MEDIO: campo 43 \- Valor Base ICMS\-ST Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

  \(VLR\_CONTAB\_ITEM \- Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Onde os valores são oriundos do item da nota de Entrada referenciada:

- VLR\_CONTAB\_ITEM é o campo 64\-Valor Contabil \(SAFX08\) do Item da nota de Entrada referenciada;
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”
- Valor do ICMS\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                         “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e

                              “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

Ver  __*[Detalhamento da Nota de Entrada Referenciada pela Devolução](#Detalha_NF_SAI)*__\.

__Obs__: O valor do ICMS\-ST está sendo subtraído do valor contábil com base na orientação do Guia Prático do Sped Fiscal, do registro da entrada C180: 

*“Campo 05 \(VL\_UNIT\_CONV\) – *__*Preenchimento*__*: informar o valor unitário líquido do item/produto \(considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto\)\. O valor unitário do campo 05 não inclui o ICMS ST na aquisição de participante substituto ou nas hipóteses em que o informante é responsável pela substituição\.”*

Essa interpretação foi confirmada com nossa Área de Informação \(CAN\) juntamente com o Carrefour\.

Vlr Unit Conv \(C186\-15\)

 

35

Valor Unitário ICMS OP Conv

Campos da EFD correspondentes: 17 do C181 e 16 do C186

VLR\_ICMS\_CONV

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”, então:

       Preencher com: \[VLR\_ICMS\_MEDIO\]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_ICMS\_MEDIO: campo 21 \- Valor de ICMS Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor do ICMS / QTD\_CONV\_NF\_ENT 

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Nota de Entrada Referenciada pela Devolução](#Detalha_NF_SAI)*__\.

__\[MFS90131\]__ Arredondar para 6 casas decimais o valor, pois compçõe o layout do C186\.

Vlr Unit ICMS Conv \(C186\-16\)

 

36

Valor Unitário Base ICMS ST Conv da Entrada

Campo da EFD correspondente: 17 do C186\.

VLR\_UNIT\_BC\_ICMSS\_ENT

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”, então:

       Preencher com: \[VLR\_BASE\_ICMSS\_MEDIO\]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_BASE\_ICMSS\_MEDIO: campo 43 \- Valor Base ICMS\-ST Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor da BC\-ST / QTD\_CONV\_NF\_ENT

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

       Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

       Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                        “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

          Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

       Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e

                            “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Nota de Entrada Referenciada pela Devolução](#Detalha_NF_SAI)*__\.

__\[MFS90131\]__ Arredondar para 6 casas decimais o valor, pois compçõe o layout do C186\.

Vlr Unit BC ICMS\-ST Conv \(C186\-17\)

 

37

Valor Unitário ICMS ST Conv da Entrada

Campo da EFD correspondente: 18 do C186\.

VLR\_UNIT\_ICMSS\_CONV\_ENT

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”, então:

       Preencher com: \[VLR\_ICMSS\_MEDIO\]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_ICMSS\_MEDIO: campo 22 \- Valor de ICMS\-ST Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

O preenchimento do campo seria:

 \(Valor do ICMS\-ST \+ Valor do FECEP\-ST\)/ QTD\_CONV\_NF\_ENT

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Mas deve\-se tratar o caso do Valor do ICMS\-ST já conter o FECEP\-ST, para que este não seja somado duas vezes\. 

Como premissa, a tabela DATAMART já contém o FECEP\-ST embutido no campo 52\-ICMS\-ST, pois na equalização do DATA MART, os cliente são orientados a marcar o parâmetro para Somar FECEP ao ICMS/ICMS\-ST, quando o FECEP não “nasce” embutido ao ICMS/ICMS\-ST nas tabelas “normais” X07/X08\. 

Quanto às tabelas “normais”, o FECEP pode ou não estar embutido campo 52\-ICMS\-ST via importação da SAFX08, por isso existe o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” \)” da tela de Dados Iniciais \(menu Parâmetros à IN\-RE 087/2020 à Dados Iniciais\)\.__ \[MFS65137\]__\.

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

  Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

        Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos 

        itens \(SAFX08\)” foi marcado na tela de Dados Iniciais, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o  __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com: 

                 \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

        Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos 

        itens \(SAFX08\)” não foi marcado, então:

           Preencher com: \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

  Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

       Se for considerado o “52\-Valor ICMS Substituição Tributária” para o  __Valor do ICMS\-ST__ \(\*\):

             Preencher com: \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

       Senão

             Preencher com: \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

__\[MFS543860\]__ Tratamento do parâmetro para identificar se o valor do FECP está embutido nos valores de ICMS não destacado/não escriturado

Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado \(aplicado às Entradas e Devoluções de Entradas\):

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” for marcado na tela de Dados Iniciais, então:

             Se for considerado o campo “145\- VLR\_ICMSS\_N\_ESCRIT” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_N\_ESCRIT\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

            Se for considerado o campo “133\- VLR\_ICMSS\_NDESTAC” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_NDESTAC\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” não for marcado, então:

         Preencher com:  

         \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) /   

          QTD\_CONV\_NF\_ENT

              OU

         \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / 

          QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada referenciada:

- \(\*\)__Valor do ICMS\-ST__ é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                              “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Nota de Entrada Referenciada pela Devolução](#Detalha_NF_SAI)*__\.

__\[MFS90131\]__ Arredondar para 6 casas decimais o valor, pois compçõe o layout do C186\.

Vlr Unit ICMS\-ST Conv \(C186\-18\)

 

38

Valor Unitário FCP ST Conv da Entrada

Campo da EFD correspondente: 19 do C186\.

VLR\_UNIT\_FCP\_CONV\_ENT

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”,então:

       Preencher com: \[VLR\_FCP\_MEDIO\]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_FCP\_MEDIO: campo 44 \- Valor FECEP Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

Valor do FECEP\-ST/ QTD\_CONV\_NF\_ENT

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Nota de Entrada Referenciada pela Devolução](#Detalha_NF_SAI)*__\.

__\[MFS90131\]__ Arredondar para 6 casas decimais o valor, pois compçõe o layout do C186\.

Vlr Unit FCP\-ST Conv \(C186\-19\)

 

39

Valor Unitário ICMS OP Estoque Conv

Campo da EFD correspondente: 13 do C181\.

VLR\_UNIT\_ICMS\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.  


Não Apresentar

 

40

Valor Unitário ICMS ST Estoque Conv

Campo da EFD correspondente: 14 do C181\.

VLR\_UNIT\_ICMSS\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

Não Apresentar

 

41

Valor Unitário FCP ICMS ST Estoque Conv

Campo da EFD correspondente: 15 do C181\.

VLR\_UNIT\_FCP\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

Não Apresentar

 

42

Valor Unitário ICMS na Operação Conv

Campo da EFD correspondente: 16 do C181\.

VLR\_UNIT\_ICMS\_OPER\_SAI

 Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

Não Apresentar

 

43

Valor Unitário ICMS ST Conv Rest

Campo da EFD correspondente: 18 do C181\.

VLR\_UNIT\_ICMSS\_REST\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

Não Apresentar

 

44

Valor Unitário FCP ST Conv Rest

Campo da EFD correspondente: 19 do C181\.

VLR\_UNIT\_FCP\_REST\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

Não Apresentar

 

45

Valor Unitário ICMS ST Conv Compl

Campo da EFD correspondente: 20 do C181\.

VLR\_UNIT\_ICMSS\_COMPL\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

Não Apresentar

 

46

Valor Unitário FCP ST Conv Compl

Campo da EFD correspondente: 21 do C181\.

VLR\_UNIT\_FCP\_COMPL\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

Não Apresentar

__*Parametrização do Produto \(por Código, NCM ou CEST\)*__

Produto da NF de Devolução

GRUPO\_PROD\_NF\_DEV

IND\_PROD\_NF\_DEV

COD\_PROD\_NF\_DEV

Produto do item da nota de devolução\.

Ind Produto

\(SAFX2013\-01\)

Cod Produto \(SAFX2013\-02\)

Unidade de Medida do Produto NF de Devolução

COD\_MEDIDA\_PROD\_NF\_DEV

Unidade de Medida do Produto da nota de Devolução \(SAFX2013 – campo 14 – COD\_MEDIDA\)

Medida Produto \(SAFX2013\-14\)

NCM do Produto NF de Devolução

COD\_NBM\_PROD\_NF\_DEV

Código NBM do Produto da nota de Devolução \(SAFX2013 – campo 05 – Código NBM\)

NCM Produto \(SAFX2013\-05\)

CEST do Produto NF de Devolução

COD\_CEST\_PROD\_NF\_DEV

Código CEST do Produto da nota de Devolução \(SAFX2013 – campo 54 – Código Especificador da Substituição Tributária\)

CEST Produto \(SAFX2013\-54\)

Produto Principal

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

Caso o produto do item da nota de devolução tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) apresentar o Produto Principal \(grupo, indicador e código\)\.

Não Apresentar

Unidade de Medida do Produto Principal

COD\_MEDIDA\_PROD\_PRINC

Caso o produto do item da nota de devolução tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) apresentar a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.

Não Apresentar

<a id="Detalha_NF_DEV"></a>__*Detalhamento da Nota de Devolução*__

Quantidade da NF de Devolução da Entrada

\(safx08 – item 24\)

QTD\_NF\_DEV

Campo 24\-Quantidade \(SAFX08\) do item da nota de Devolução de Entrada 

Qtde Item NF Devolução \(SAFX08\-24\)

Quantidade Convertida da NF de Devolução de Entrada \(safx08 – item137\)

QTD\_CONV\_X08\_NF\_DEV

Campo 137 – Quantidade Convertida \(SAFX08\) do item da nota de Devolução de Entrada

Qtde Conv Item NF Devolução \(SAFX08\-137\)

Unidade de Medida da NF de Devolução de Entrada \(safx08 \- item 25\)

COD\_MEDIDA\_NF\_DEV

Campo 25 – Unidade de Medida \(SAFX08\) do item da nota de Devolução de Entrada\.

Medida Item NF Devolução \(SAFX08\-25\)

Fator Conversão da Medida da NF de Devolução de Entrada p/ Medida do Produto

FAT\_CONV\_NF\_DEV

Preecher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para NF de Devolução de Entrada \(QTD\_CONV\_NF\_DEV\)” a seguir\.

__Se__ unidade da nota = unidade do cadastro do produto, então:__  __

__    __Campo será preenchido com 1;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Campo não será preenchido;

     Senão         

           Se não encontrado Fator de Conversão nos Cadastros de Conversão de Unidades de 

           Medidas, então:

                Campo será preenchido com \-1;

           Senão

                 Campo será preenchido com o Fator de Conversão encontrado\.

Fator Conv NF Devolução \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para NF de Devolução de Entrada \(safx08\)

\(<a id="QTD_CONV_NF_DEV"></a>QTD\_CONV\_NF\_DEV\)

QTD\_CONV\_NF\_DEV

Campo 24\-Quantidade \(SAFX08\) do Item da nota de Devolução de Entrada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do

      item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

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

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, será gravada a seguinte mensagem de erro no log:

“*Registro C186: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de entrada será gerada no C186 sem informação no campo 07 \- Quantidade Convertida e não irá compor a Média Pondera Móvel dos Valores Unitários do dia DD/MM/YYYY\. Favor rever medida da NF de devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Entrada e da Entrada referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Não Apresentar pois já é o campo Qtde Conv \(C186\-07\)

<a id="Detalha_NF_SAI"></a>__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__

Quantidade do Item da NF de Entrada Referenciada \(safx08 – item 24\)

QTD\_NF\_ENT

Campo 24\-Quantidade \(SAFX08\) do item da nota fiscal de Entrada referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)

Qtde Item NF Entrada \(SAFX08\-24\)

Quantidade Convertida do Item da NF de Entrada Referenciada \(safx08 – item137\)

QTD\_CONV\_X08\_NF\_ENT

Campo 137 – Quantidade Convertida \(SAFX08\) do item da nota fiscal de Entrada referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)

Qtde Conv Item NF Entrada \(SAFX08\-137\)

Unidade de Medida do Item da NF de Entrada Referenciada

\(safx08 \- item 25\)

COD\_MEDIDA\_NF\_ENT

Campo 25 – Unidade de Medida \(SAFX08\) do item da nota fiscal de Entrada referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)\.

Medida Item NF Entrada \(SAFX08\-25\)

Fator Conversão

FAT\_CONV\_NF\_ENT

Preecher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para o Item da Nota de Entrada \(QTD\_CONV\_NF\_ENT\)” a seguir\.

__Se__ unidade da nota = unidade do cadastro do produto, então:__  __

__    __Campo será preenchido com 1;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Campo não será preenchido;

     Senão         

           Se não encontrado Fator de Conversão nos Cadastros de Conversão de Unidades de 

           Medidas, então:

                Campo será preenchido com \-1;

           Senão

                 Campo será preenchido com o Fator de Conversão encontrado\.

Fator Conv NF Entrada \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para o Item da NF de Entrada Referenciada

\(<a id="QTD_CONV_NF_ENT"></a>QTD\_CONV\_NF\_ENT\)

QTD\_CONV\_NF\_ENT

Campo 24\-Quantidade \(SAFX08\) do Item da nota de Entrada referenciada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 do Item da NF de Entrada Referenciada

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do

      item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

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

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“*Registro C186: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de Entrada será gerada no C186 sem valores unitários da Mercadoria, do ICMS, BC\-ST, ICMS\-ST e FCP \(campos 15 a 19\)\. Favor rever medida da NF de entrada referenciada pela devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Entrada e da Entrada referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Qtde Conv Calculada p/ NF Entrada

Valor Contabil do Item da NF de Entrada Referenciada

\(safx08 – item 64\)

VLR\_CONTAB\_ENT

Campo 64\-“Vlr Contabil do Item”\(SAFX08\) do item da nota fiscal de Entrada referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)

Vlr Contabil Item NF Entrada \(SAFX08\-64\)

Valor do ICMS do Item da NF de Entrada Referenciada

VLR\_ICMS\_ENT

Valor do ICMS é oriundo de um dos três campos do item da nota fiscal de Entrada referenciada \(SAFX08\), dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

Vlr ICMS Item NF Entrada \(SAFX08\-43,80,225\)

Valor da BC\-ST do Item da NF de Entrada Referenciada

VLR\_BC\_ST\_ENT

Valor da Base de Cálculo do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada referenciada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” 

    estiverem preenchidos, então:

        Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” 

        estiverem preenchidos, então:

           Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

        Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem 

           preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

Vlr BC ICMS\-ST Item NF Entrada \(SAFX08\-61,144,106\)

Valor do ICMS\-ST do Item da NF de Entrada Referenciada

VLR\_ICMS\_ST\_ENT

Valor do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada referenciada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem 

    preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” 

        estiverem preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem 

            preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

Vlr ICMS\-ST Item NF Entrada \(SAFX08\-52,145,133,107\)

Valor do FECEP\-ST do Item da NF de Entrada Referenciada

VLR\_FECEP\_ST\_ENT

Valor do FECEP\-ST é oriundo do item da nota fiscal de Entrada referenciada \(SAFX08\):

- Campo 140\-FECEP ICMS\-ST da SAFX08\.

Vlr FECEP\-ST Item NF Entrada \(SAFX08\-144\)

__*Valores Unitários do Inventário \(recuperado no tópico *__[__*2\.2*__](#_2.2_–_Recuperação)__*\)*__

Valor Médio Unitário do ICMS 

VLR\_UNIT\_ICMS\_INV

Preencher com VLR\_ICMS\_MEDIO \(campo 21 \- Valor de ICMS Médio SAFX52\), recuperado do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação)\.

Vlr Unit ICMS Inventário dd/mm/aaaa

Onde:

Dd/mm/aaaa é a Dt anterior à adoção IN\-RE087/20 informada na tela de geração\.

Valor Médio Unitário do ICMS\-ST 

VLR\_UNIT\_ICMS\_ST\_INV

Preencher com VLR\_ICMSS\_MEDIO \(campo 22 \- Valor de ICMS\-ST Médio SAFX52\), recuperado do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação)\.

Vlr Unit ICMS\-ST Inventário dd/mm/aaaa

Onde:

Dd/mm/aaaa é a Dt anterior à adoção IN\-RE087/20 informada na tela de geração\.

Valor Médio Unitário da Base ICMS\-ST 

VLR\_UNIT\_BC\_ST\_INV

Preencher com VLR\_BASE\_ICMSS\_MEDIO \(campo 43 \- Valor Base ICMS\-ST Médio SAFX52\), recuperado do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação)\.

Vlr Unit BC ICMS\-ST Inventário dd/mm/aaaa

Onde:

Dd/mm/aaaa é a Dt anterior à adoção IN\-RE087/20 informada na tela de geração\.

Valor Médio Unitário do FECEP\-ST 

VLR\_UNIT\_FECEP\_ST\_INV

Preencher com VLR\_FCP\_MEDIO \(campo 44 \- Valor FECEP Médio SAFX52\), recuperado do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação)\.

Vlr Unit FECEP\-ST Inventário dd/mm/aaaa

Onde:

Dd/mm/aaaa é a Dt anterior à adoção IN\-RE087/20 informada na tela de geração\.

__*Dados para o “Cálculo da Média Pondera Móvel dos Valores Unitários” alínea “d” do 19\.3\-A\.2\.2 da IN\-RE 087/20*__

Quantidade Devolvida Convertida \(a\)

QTD\_CONV\_DEV\_ENT\_MP

__Idem ao campo 32 – Quantidade Convertida \(QTD\_CONV\)__

Preencher com:

“Qtde Convertida Calculada para NF de Devolução de Entrada \(safx08\) \([QTD\_CONV\_NF\_DEV](#QTD_CONV_NF_DEV)\)”

Ver [__*Detalhamento da Nota de Devolução*__](#Detalha_NF_DEV)

Não Apresentar pois já é o campo Qtde Conv \(C186\-07\)

Valor Médio Unitário do ICMS  \(b\)

VLR\_UNIT\_ICMS\_DEV\_ENT\_MP

__Idem ao campo 35 \- Valor Unitário ICMS OP Conv \(VLR\_ICMS\_CONV\)__

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”,então:

       Preencher com: \[VLR\_ICMS\_MEDIO\]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_ICMS\_MEDIO: campo 21 \- Valor de ICMS Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor do ICMS / QTD\_CONV\_NF\_ENT 

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__](#Detalha_NF_SAI)\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário do ICMS\-ST \(c\)

VLR\_UNIT\_ICMS\_ST\_DEV\_ENT\_MP

__Não é igual ao campo 37 \- Valor Unitário ICMS ST Conv da Entrada \(VLR\_UNIT\_ICMSS\_CONV\_ENT\)__

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”,então:

       Preencher com: \[VLR\_ICMSS\_MEDIO\]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_ICMSS\_MEDIO: campo 22 \- Valor de ICMS\-ST Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

O preenchimento do campo seria:

 Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Mas para cálculo da Média Ponderada, precisamos separar o FECEP\-ST do ICMS\-ST\. O motivo é que na geração da Saída e Devolução de Saída o campo VLR\_UNIT\_ICMSS\_ESTQ\_SAI \(13 \(C185\) e 09 \(C380\)\) é resultante da soma do ICMS\-ST e FECEP\-ST oriundos do Cálculo da Média Ponderada \(EST\_ST\_RS\_MEDIA\_POND\)\. Se não calcularmos e gravá\-los separadamente na tabela EST\_ST\_RS\_MEDIA\_POND, o FECEP\-ST pode sair duplicado no campo VLR\_UNIT\_ICMSS\_ESTQ\_SAI\.

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

  Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

        Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST 

        nos itens \(SAFX08\)” foi marcado na tela de Dados Iniciais, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: 

    \(Valor do ICMS\-ST\- Valor do ICMS\-ST FECEP\) /

    QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

        Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST

        nos itens \(SAFX08\)” não foi marcado, então:

             Preencher com:  

             \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

  Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

       Se for considerado o “52\-Valor ICMS Substituição Tributária” para o  

__       Valor do ICMS\-ST__ \(\*\):

           Preencher com:  

            \(Valor do ICMS\-ST \- Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

       Senão

           Preencher com:

          \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

__\[MFS543860\]__ Tratamento do parâmetro para identificar se o valor do FECP está embutido nos valores de ICMS não destacado/não escriturado

Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado \(aplicado às Entradas e Devoluções de Entradas\):

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” for marcado na tela de Dados Iniciais, então:

             Se for considerado o campo “145\- VLR\_ICMSS\_N\_ESCRIT” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_N\_ESCRIT\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

            Se for considerado o campo “133\- VLR\_ICMSS\_NDESTAC” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_NDESTAC\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” não for marcado, então:

         Preencher com:  

         \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) /   

          QTD\_CONV\_NF\_ENT

              OU

         \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / 

          QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada referenciada:

- \(\*\)__Valor do ICMS\-ST__ é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__](#Detalha_NF_SAI)\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(d\)

VLR\_UNIT\_BC\_ST\_DEV\_ENT\_MP

__Idem ao campo 36 \- Valor Unitário Base ICMS ST Conv da Entrada \(VLR\_UNIT\_BC\_ICMSS\_ENT\)__

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”,então:

       Preencher com: \[VLR\_BASE\_ICMSS\_MEDIO\]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_BASE\_ICMSS\_MEDIO: campo 43 \- Valor Base ICMS\-ST Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor da BC\-ST / QTD\_CONV\_NF\_ENT

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem   

    preenchidos, então:

       Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

       Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” 

       estiverem preenchidos, então:

          Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

       Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem 

           preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__](#Detalha_NF_SAI)\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário do FECEP\-ST \(e\)

VLR\_UNIT\_FECEP\_ST\_DEV\_ENT\_MP

__Idem ao campo 38 \- Valor Unitário FCP ST Conv da Entrada \(VLR\_UNIT\_FCP\_CONV\_ENT\)__

__Tratamento das entradas de períodos anteriores à sistemática da IN\-RE 087/20:__

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

  Valores Unitários Médios recuperados:

  \( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

  \( \) da própria Nota de Entrada referenciada pela Devolução

  Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]”

__Se__ a Data Fiscal da nota de Entrada referenciada for __<=__ __Dt anterior à adoção IN\-RE087/20__ informada na Tela de Dados Iniciais __\[MFS65137\]__, então:

   Se for escolhida a opção “*do Inventário do Produto \(conforme IN\-RE 096/20 \- item 19\.3\-A\.1\.4\.1\)*”,então:

       Preencher com: \[VLR\_FCP\_MEDIO\]

       Onde os valores foram recuperados do Inventário conforme tópico [2\.2](#_2.2_–_Recuperação):

- VLR\_FCP\_MEDIO: campo 44 \- Valor FECEP Médio \(SAFX52\)

   Se for escolhida a opção “*da própria Nota de Entrada referenciada pela Devolução*”, então:

       Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

__Senão__

  Preencher conforme a Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

Valor do FECEP\-ST/ QTD\_CONV\_NF\_ENT

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o valor calculado\.

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__](#Detalha_NF_SAI)\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit FECEP\-ST  \(p/ Cálculo da Média Ponderada\)

Valor do ICMS Calculado para Devolução \(f\) = \(a \* b\)

VLR\_ICMS\_DEV\_ENT\_MP

Preencher com:

\[Quantidade Devolvida Convertida \(a\) \* Valor Médio Unitário do ICMS  \(b\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr ICMS \(p/ Cálculo da Média Ponderada\)

Valor do ICMS\-ST Calculado para Devolução \(g\) = \(a \* c\)

VLR\_ICMS\_ST\_DEV\_ENT\_MP

Preencher com:

\[Quantidade Devolvida Convertida \(a\) \* Valor Médio Unitário do ICMS\-ST \(c\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução \(h\) = \(a \* d\)

VLR\_BC\_ST\_DEV\_ENT\_MP

Preencher com:

\[Quantidade Devolvida Convertida \(a\) \* Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(d\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)

Valor FECEP\-ST Calculado para Devolução \(i\) = \(a \* e\)

VLR\_FECEP\_ST\_DEV\_ENT\_MP

Preencher com:

\[Quantidade Devolvida Convertida \(a\) \* Valor Médio Unitário do FECEP\-ST \(e\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\)

# <a id="_Toc62485218"></a>RELATORIO DE CONFERÊNCIA

Gerar um arquivo excel a partir da leitura da tabela __EST\_ST\_RS\_NF\_DEV\_ENT__

Nome do arquivo: Relatório\_Conferencia\_C186\_mm\_aaaa\_cod\_estab\.xlsx

= = = = = =

 

