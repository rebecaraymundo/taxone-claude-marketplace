# MTZ-Ressarc-PR-Geracao_dos_Dados_da_CD

- **Fonte:** MTZ-Ressarc-PR-Geracao_dos_Dados_da_CD.docx
- **Modificado:** 2024-02-20
- **Tamanho:** 123 KB

---

THOMSON REUTERS

Módulo Ressarcimento e Complemento de ICMS\-ST – Paraná 

Geração dos Dados da Central de Distribuição   

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST \- PR, menu Geração 🡪 NPF 003/20 🡪 Central de Distribuição 🡪 Geração dos Dados \(CD\)

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS34475__

Geração dos Dados da Central de Distribuição

Geração dos dados da Central de Distribuição

30/03/2020 

\(criação do documento\)

__MFS40546__

Alteração no campo CST\_ICMS

Alterada a regra de geração do campo CST \(Código Situação Tributária\)

20/07/2020

__MFS47333__

Inclusão dos Produtos Associados

Alterar a geração para passar a considerar a parametrização de produtos associados

17/12/2020

__MFS47313__

Campo 137 \- SAFX08

Inclusão do campo 137 – Quantidade Convertida da SAFX08

08/06/2021

__MFS527163__

Andréa Rocha

Alteração da regra de recuperação das notas fiscais para passar a verificar a parametrização de CFOP/Natureza por estabelecimento, caso a parametrização tenha sido cadastrada\.

30/05/2023

MFS591074

Andréa Rocha

Inclusão do tratamento das Incorporações de Empresas/Estabelecimentos na geração dos movimentos de entrada\.

25/01/2024

Sumário

[1\.	Parâmetros da Tela	2](#_Toc36731527)

[2\.	Recuperação dos Dados e Processamento	4](#_Toc36731528)

[3\.	Gravação dos Dados na Tabela dos Movimentos	8](#_Toc36731529)

[4\.	Totalização das Entradas por Produto	13](#_Toc36731530)

[5\.	Relatório de Conferência	17](#_Toc36731531)

# <a id="_Toc36731527"></a>Parâmetros da Tela 

Geração dos Dados \(CD\)

  Estabelecimento Central Distribuição: \[ XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \]

  Período: 99/9999

  Pesquisar últimas entradas até: 99/99/9999

  \[  \] Utilizar somente DATA MART p/ períodos anteriores

Funcionamento dos campos:

	

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

Estabelecimento Central Distribuição

Alfanumérico 

__S__

S

Este campo é uma lista de todos os estabelecimentos cadastrados como “Central de Distribuição” na parametrização dos Dados Iniciais\.

Trata\-se dos estabelecimentos informados no campo “*Estabelecimento da Central de Distribição*” da parametrização dos dados iniciais de todos os estabelecimentos\.

O usuário deverá selecionar a central de distribuição desejada\.

Caso a lista não tenha informação \(o que acontecerá se nenhum dos estabelecimentos tiver o campo da Central de Distribuição preenchido\), então será exibida a seguinte mensagem logo após a abertura da tela:

*“Não existem estabelecimentos cadastrados como Central de Distribuição na parametrização dos dados iniciais de nenhum estabelecimento \(campo “Estabelecimento da Central de Distribição”\)”*

<a id="_Hlk517437550"></a>Período

Mês/Ano

__S__

S

MM/AAAA

Neste campo o usuário informa o período \(mês e ano\) para a geração dos dados\.

Deve ser um mês e ano válidos\.

Pesquisar últimas entradas até

Data

__S__

S

DD/MM/AAAA

Neste campo o usuário informa uma data, que servirá de limite para a pesquisa das entradas em períodos anteriores\.

 

Deve ser uma data válida e *inferior* à data do primeiro dia do período informado \(campo “Período”\)\. Caso seja informada uma data superior a este dia, será exibida a seguinte mensagem: *“A data limite para pesquisa das entradas deve ser uma data de períodos anteriores \(verificar detalhes no Help\)\.”*\.

Esta data é apenas um limite “*genérico”* para os casos em que for necessário recuperar notas de entrada de períodos anteriores\. Isso evita que a pesquisa seja feita indefinidamente, caso ocorra algum erro ou problema de base\.

Utilizar somente DATA MART p/ períodos anteriores

Alfanumérico

N

N

Checkbox

Default = desmarcado

Através deste campo o usuário pode optar como será feita a recuperação dos dados de notas de períodos anteriores, nos casos em que este procedimento for necessário\.

*\(Ver detalhes sobre a utilização deste parâmetro no item “2\-Recuperação dos Dados e Processamento”\)*

Considerar as notas fiscais da empresa incorporada

Alfanumérico

__N__

S

Defalt desmarcado\.

__\[MFS591074\] Tratamento das Incorporações de Empresas/Estabelecimentos__

Check\-box, com default habilitado e desmarcado\.

Este campo é um checkbox onde o usuário informa se vai considerar as notas fiscais de entrada da empresa incorporada, além das notas fiscais da empresa/estabelecimento da geração\.

# <a id="_Toc350763252"></a><a id="_Toc36731528"></a>Recuperação dos Dados e Processamento

Esta é uma geração preliminar dos dados solicitados no arquivo complementar “__ADRC\-ST CD__”\.

Trata\-se de um arquivo de entrega não obrigatória, que poderá ser solicitado pelo Fisco, para conferência das compras efetuadas pelo estabelecimento que funciona como central de distribuição\. 

No processo serão gerados os seguintes dados:

- As aquisições dos produtos sujeitos ao ICMS\-ST, feitas pela Central de Distribuição\. Estas notas são armazenadas na *Tabela dos Movimentos de Entrada*, e irão originar posteriormente o registro “*1111\-Identificador das Notas Fiscais de Entrada*” do arquivo ADRC\-ST CD;
- Totalização das entradas de cada produto\. Os totais apurados são gravados na *Tabela dos Totais por Produto*, e utilizados posteriormente na geração do registro “*1101\-Totalizador das Entradas do Produto*” do arquivo \(ADRC\-ST CD\);
- Quantidade de cada Produto transferida para as filiais que solicitaram ressarcimento/complemento no mês\. Esta informação também é gravado na *Tabela dos Totais por Produto*, e utilizada posteriormente na geração do registro “*1101\-Totalizador das Entradas do Produto*” do arquivo \(ADRC\-ST CD\);

__\[MFS527163\]__ Inclusão da utilização da parametrização de CFOP/Natureza por Estabelecimento quando estiver cadastrada para o estabelecimento da geração

__Origem dos dados__: \- Parametrização de Produtos

                                  \- Parametrização de NCM’s;

                                  \- Parametrização das Operações por CFOP e por Natureza de Operação \(Por UF ou por Estabelecimento\);

                                  \- Tabelas dos Documentos Fiscais \(SAFX07/SAFX08\);

__Considerações sobre a recuperação das entradas: __

- Conforme as orientações da NPF 003/20, para cada produto, devem ser recuperadas *todas* as entradas no período informado em tela\. Quando a quantidade total destas entradas não for suficiente para cobrir o total das saídas *do produto* no período, então, nesse caso \(__*e somente nesse caso*__\), serão utilizadas as entradas de períodos anteriores;
- Quando for necessário pesquisar período\(s\) anterior\(es\), a pesquisa será feita até atingir a quantidade total das saídas, __ou__, até a data limite informada em tela \(campo “*Pesquisar últimas entradas até*”\), *o que acontecer primeiro*;
- __\[MFS591074\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

Quando acontecer desta data limite ser alcançada, sem que a quantidade apurada nas entradas seja suficiente para atingir a quantidade total das saídas, verificar se o parâmetro para buscar as notas nas empresas incorporadas está marcado na tela da geração\. 

     Se o parâmetro “Considerar as notas fiscais da empresa incorporada” estiver marcado:

           Considerar as notas das empresas/estabelecimentos cadastradas como incorporadas na tela de Relação de Empresa 

           Incorporadora x Incorporada\*\* para a empresa/estabelecimento da geração \(incorporadora\), para recuperar as notas de  

           entrada afim de atingir a quantidade da saída do produto\.

    Senão

          Considerar somente as notas fiscais da empresa e estabelecimento selecionados para a geração\. 

          

\*\* Módulo Parâmetros, item Preliminares 🡪 Relação de Empresa Incorporadora x Incorporada

__Obs__\.: Não estamos tratando o cenário de Cadastros de Produtos distintos entre as empresas incorporadora e incorporadas\. Ou seja, os produtos entre essas empresas devem ser identificados pelo mesmo grupo, indicador e código do produto\.  A Lasa que foi o cliente que abriu essa demanda, possui cadastros iguais entre as empresas participantes da incorporação\. Se os cadastros fossem diferentes, teríamos que criar uma espécie de dexpara entre os cadastros dos produtos da empresa incorporadora para com os das empresas incorporadas\.

- A recuperação de notas em períodos anteriores é feita com base no parâmetro “*Utilizar somente DATA MART p/ períodos anteriores*”, da seguinte forma:

               Marcado – Nesse caso a recuperação das notas de períodos anteriores será feita *apenas* com base no DATA MART;

               Desmarcado – Nesse caso a recuperação destas notas utilizará normalmente o DATA MART, no entanto, quando não existirem mais

                                       dados,  e a pesquisa ainda não tiver sido finalizada __*\(\*\)*__, então a pesquisa utilizará as tabelas “normais” \(tabelas X07/X08\);

__*                                       \(\*\)*__ Ou seja, ainda não atingiu a quantidade total das saídas, e nem a data limite informada;

- Desta forma, a geração das entradas depende do total das saídas do Produto\. No caso deste arquivo da CD, as saídas a serem contabilizadas são as transferências do Produto realizadas para todas as filiais;
- Sobre a totalização das saídas: o total das saídas do produto no período, será calculado com base em todas as notas fiscais de saída do produto, cuja pessoa fis/jur \(destinatário\) seja uma filial, da seguinte forma:

           Critérios de recuperação das __saídas__ a serem totalizadas:

          \- Empresa – código da empresa do login;

          \- Estabelecimento – código do estabelecimento Central Distribuição informado em tela;

          \- Movimento Entrada/Saída – somente notas de saída \(MOVTO\_E\_S = “9”\);

          \- Pessoa Fis/Jur \(destinatário\) – deve ser uma filial do estabelecimento Central de Distribuição, e deve ser do Paraná:

- CNPJ raiz da Pessoa Fis/Jur = CNPJ raiz do estabelecimento CD \(cnpj raiz são os 8 primeiros dígitos do cnpj\)
- UF da Pessoa Fis/Jur = Paraná

          \- Data Fiscal – data enquadrada no período informado em tela;

          \- Somente notas *não canceladas*;

          \- Somente notas *com itens*;

          \- O produto do item deve constar na parametrização do menu “*Parâmetros 🡪 Produtos*”, __ou__, seu NCM deve estar parametrizado

             no menu “*Parâmetros 🡪 NCM’s*”\. 

__\[MFS47333\] __Inclusão da parametrização de Produtos Associados

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização de Produtos\. Ao verificar a

parametrização por produto, deve\-se considerar também os produtos associados\. Ou seja, o produto da nota deve constar como o produto

“principal” da parametrização, ou ser um produto “associado” ao produto principal\.  

 	Os produtos “associados” são produtos cuja movimentação serão gravadas em nome do produto principal parametrizado\.

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\. A prioridade na pesquisa da parametrização dos produtos é: por Código, e depois por NCM, da seguinte forma:

- Caso o produto conste na parametrização por código \(opção “Produtos”\), a parametrização por NCM não precisa ser verificada;
- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “NCM’s”;

Sobre a recuperação das saídas da CD para as filiais:

A princípio, *não* será feita a verificação do CFOP do item\. Serão consideradas *todas* as saídas dos produtos para as filiais do estado\. 

Para apurar a quantidade total destas transferências feitas do CD para as filiais, __foram avaliadas duas opções__:

Opção 1: Considerar as entradas que tenham sido geradas para estas filiais \(menu "Geração dos Movimentos de Entrada\), em que o emitente \(Pessoa Fis/Jur da nota\) seja o estabelecimento da Central de Distribuição\. Desvantagem: se alguma filial, por um motivo qualquer, não gerar o cálculo do Ressar/Complemento para o período em questão, as transferências para esta filial não seriam consideradas;

Opção 2: Trabalhar com as próprias notas de saída do estabelecimento CD, considerando TODAS as saídas em que o destinatário seja alguma filial do PR;

Foi escolhida a opção 2, por ser a mais segura e acertiva\.

             

              Com base nas saídas recuperadas conforme estes critérios, será contabilizado o __total da quantidade de saídas__ de cada Produto\. 

              A totalização da quantidade será feita sempre com base na unidade de medida do cadastro do produto \(campo “14\-Código de Medida” da 

               SAFX2013, que é referente à unidade da SAFX2007\)\.

              Assim, quando a unidade de medida do item da nota \(*campo “25\-Unidade de Medida” da SAFX08*\) for diferente da unidade de medida do 

              cadastro do produto \(*campo “14\-Código de Medida” *da SAFX2013\), é necessário realizar a conversão da Quantidade do item antes de fazer a

               totalização deste valor, segundo a regra a seguir:

   __Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade 

      do item da nota;

   __Senão __

      __\[MFS47313\] Inclusão do campo 137 – Quantidade Convertida da SAFX08__

      Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

      Senão

         Nesse caso o campo será preenchido com a quantidade do item da nota convertida para a unidade de 

         medida declarada no campo anterior \(unidade de medida do cadastro do produto\), utilizando o fator de

         conversão obtido nas tabelas de Conversão de Medida\.

         Assim, será a multiplicação dos seguintes campos:

              

          \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__= = = = = \[MFS47333\] Inclusão de Produtos Associados__

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

__Sobre a conversão de medida na totalização das saídas:__

A conversão de medida é efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das tabelas, *o item da nota não será considerado na totalização das saídas do produto*, e no log da geração será gravada a seguinte mensagem de erro: “Fator de conversão de medida de XXX para XXX não encontrado\. O item não será considerado na totalização das saídas do produto, interferindo nas regras da geração do registro 1111 \(ver detalhes no Help da geração\)*”*

* *\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

__Critérios da recuperação das Notas Fiscais de entrada: __

- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento da Central de Distribuição informado em tela;
- Data Fiscal – data enquadrada no período informado em tela;
- Somente notas de entrada \(MOVTO\_E\_S <> “9”\) – no caso da CD são consideradas apenas as aquisições \(devoluções *não* são tratadas\);
- Somente notas *não canceladas*;
- Somente notas *com itens*;
- Modelo – somente os documentos de modelo = 55 \(NF\-e\) e 65 \(NFC\-e\);   
- O produto do item deve constar na parametrização do menu “*Parâmetros 🡪 Produtos*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros 🡪 NCM’s*”; 

__\[MFS47333\] __Inclusão da parametrização de Produtos Associados

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização de Produtos\. Ao verificar a

parametrização por produto, deve\-se considerar também os produtos associados\. Ou seja, o produto da nota deve constar como o produto

“principal” da parametrização, ou ser um produto “associado” ao produto principal\.  

	Os produtos “associados” são produtos cuja movimentação serão gravadas em nome do produto principal parametrizado\.

      Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

             A prioridade na pesquisa da parametrização dos produtos é: por Código, e depois por NCM, da seguinte forma:

            \- Caso o produto conste na parametrização por código \(opção “Produtos”\), a parametrização por NCM não precisa ser verificada;

            \- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “NCM’s”;

- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros à Operações*” para a operação “*Entradas \(e Devoluções\)”*\.  Primeiro deve\-se verificar se existe parametrização cadastrada na opção Por Estabelecimento, para o estabelecimento da geração \(tratar I\.E\.U\.\)\.  Se houver parametrização, deve\-se considerar os CFOP/Naturezas cadastrados na parametrização por Estabelecimento \(Parâmetros 🡪 Operações 🡪 CFOP \(Por Estabelecimento\) ou Natureza de Operação \(Por Estabelecimento\)\)\.  Se não houver parametrização cadastrada para o estabelecimento, deve\-se utilizar os CFOP/Naturezas cadastrados por UF \(Parâmetros 🡪 Operações 🡪 CFOP ou Natureza de Operação\)\.

__*Importante*__*: Como já citado acima, serão geradas todas as entradas do período, e caso a quantidade total destas entradas não seja suficiente para cobrir o total das saídas do Produto, serão utilizadas entradas de períodos anteriores, conforme a regra definida acima \(no item “Considerações sobre a recuperação das entradas”\)\. Para efeito de comparação de quantidades, é importante lembrar que todas as quantidades devem ser convertidas, quando necessário, antes de fazer qualquer tipo de comparação\. *

Os movimentos recuperados serão armazenados na Tabela dos Movimentos de Entrada, conforme descrito no item “__3\-Gravação dos Dados na Tabela dos Movimentos__”\. 

Após o processamento de todas as entradas, será feita a totalização das entradas de cada produto, conforme descrito no item “__4\-Totalização das Entradas por Produto__”\. 

# <a id="_Toc36731529"></a>Gravação dos Dados na Tabela dos Movimentos 

<a id="_Hlk508706613"></a>

Os documentos fiscais recuperados da SAX07 / SAFX08 __serão gravados na tabela item a item__, com as seguintes informações:

\(Trata\-se da mesma tabela dos movimentos de entrada utilizada para armazenar as entradas do arquivo principal, o ADRC\-ST\) 

Os campos sinalizados com asterisco compõem a chave da tabela\.

__\*\*\*__

__Código da empresa__

Código da empresa \(SAFX07\)

__\*\*\*__

__Código do estabelecimento__

Código do estabelecimento da Central de Distribuição informado em tela \(SAFX07\) 

__\*\*\*__

__Código do estabelecimento de origem__

Código do estabelecimento de origem do documento \(SAFX07\)

 

Obs\.: Este campo foi criado na tabela por causa da geração por inscrição estadual única, que poderá ser desenvolvida posteriormente, caso solicitado\. A princípio, a geração será desenvolvida sem esta opção, e assim, este campo será gravado com o mesmo conteúdo do anterior;

__\*\*\*__

__Período \(mês e ano\)__

Período da geração \(mês a ano\) informado em tela\.

__\*\*\*__

__Produto__

Produto referente ao item da nota \(campos 13 e 14 da SAFX08\)\.

__\[MFS47333\] __Inclusão da parametrização de Produtos Associados

Quando se tratar de um produto “associado”, a informação gravada neste campo será o produto principal da parametrização\.

__\*\*\*__

__Data Fiscal __

Data fiscal do documento \(SAFX07\)

__\*\*\*__

__Tipo do Documento__

Tipo do Documento \(campo “05\-Tipo do Documento” da SAFX07\)

__\*\*\*__

__Série do Documento__

Série do documento fiscal \(campo “09\-Série do Documento” da SAFX07\)

__\*\*\*__

__Número do Documento__

Número do documento fiscal \(campo “08\-Número do Documento” da SAFX07\)

__\*\*\*__

__Pessoa Fis/Jur__

Pessoa fis/jur do documento fiscal \(campos 06 e 07 da SAFX07\)

__\*\*\*__

__Número do Item__

Número do item do documento fiscal \(campo “18\-Item Nota Fiscal” da SAFX08\)

__\*\*\*__

__Movimento E/S__

Indicador do movimento \(campo “03\-Movimento Entrada/Saída” da SAFX07\)

__Tipo de Registro__

Este campo será preenchido com “__1111__”;

__Data Emissão__

Data de emissão do documento \(campo 11\-Data de Emissão da SAFX07\)

__Modelo do Documento__

Modelo do documento \(campo 13\-Modelo do Documento da SAFX07\)

*Obs\.: O modelo não consta no layout do arquivo, mas será armazenado para facilitar a identificação dos documentos no relatório de conferência\.* 

__Código Responsável Retenção__

Este campo é preenchido de acordo com os campos 131 e 132 do item \(SAFX08\), da seguinte foma:

__Se__ campo “132 \- Situação Especial \- Substituição Tributária” = ‘1’

     O campo será preencido com  “__3__” \(= Próprio Declarante\);      

__Senão__

     __Se__ campo “131\- Indicador de ICMS\-ST” = ‘1’:

           O campo será preencido com  “__1__” \(= Rementente Direto\);

__     Se__ campo “131\- Indicador de ICMS\-ST” igual a ‘2’:

          O campo será preencido com  “__2__” \(= Rementente Indireto\);

\(O campo “131\-Código Responsável pela Retenção” é o campo IND\_FORNEC\_ICMSS da SAFX08\)

\(O campo “132\-Situação Especial \- Substituição Tributária” é o campo IND\_SITUACAO\_ESP\_ST da SAFX08\)

*Obs\.: Esta é a mesma regra de preenchimento do campo “18\- COD\_RESP\_RET” do registro C176 do Sped Fiscal, e do campo “08\-COD\_RESP\_RET” do registro 2130 do Ressarcimento – SC\.*

Crítica:

Se ao aplicar a regra acima, resultar conteúdo nulo para o campo, o mesmo será gerado sem informação, e no log de erros será gravada a seguinte menagem: “*Não foi possível identificar o Código do Responsável pela Retenção\. O item do documento será gerado sem esta informação\. Verificar os pré\-requisitos para a geração das entradas no help do menu\.”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)\.  

 

__CST\_ICMS__

Concatenação dos seguintes campos do item \(SAFX08\):

“30\-Código Situação Tributária A” \+ “31\-Código Situação Tributária B” 

\[Alteração __MFS40546__\]

A regra de geração do CST foi alterada para considerar as orientações do fiscal da Sefaz\-PR, conforme retorno do cliente Via Varejo no chamado 12272:

__*\[*__* Hoje a fiscal me retornou, através de contato telefônico,  informando que o tamanho *__*máximo*__* de caractere do campo *__*CST\_CSOSN*__* é 3, não deve ser informado a origem\. *

*Para o caso de fornecedor  não optante pelo simples devemos preencher com 2 caracteres\. O campo será preenchido com 3 caracteres quando a aquisição através de fornecedor Optante do Simples Nacional\. *__*\]*__

Isso significa que, no caso das aquisições de fornecedores que sejam optantes pelo simples nacional, deve ser informado o código específico da Tabela de Situação da Operação no Simples Nacional \(CSOSN\), que é uma tabela diferente, que não existe no DW\. Para a informação deste código, quando for o caso,  foi criado o campo 262\-Código CSOSN na SAFX08\. E para as aquisições de fornecedores *não* optantes do SN, deve ser informado apenas o Código da Situação Tributária B, ou seja, *apenas 2 posições*\.

__Se__ emitente da nota \(pessoa fis/jur\) for Simples Nacional \(campo “43\-Enquadrado como SN” da SAFX04 = “S”\):

      Será gravado o conteúdo do campo “__262\-Código CSOSN__” da SAFX08\. Se este campo estiver nulo,

      o campo CST\_ICMS será gerado sem informação, e no log de erros será gravada a seguinte mensagem: 

      *“Em aquisições de fornecedores optantes pelo Simples Nacional, é necessário preencher o campo “262\-Código*

*       CSOSN” do item da nota \(SAFX08\)\. O item do documento será gerado sem esta informação\. Verificar os pré\-*

*       requisitos para a geração das entradas no help do menu”\.*

       O log deve demonstrar as informações necessárias para permitir a identificação do item do documento,

       exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

__  Senão__,

      Será gravado o conteúdo do campo “__31\-Código Situação Tributária B__”, e assim, o campo ficará com apenas

      duas posições, conforme a orientação da Sefaz\-PR;

__Chave Documento Fiscal Eletrônico __

Chave do documento fiscal eletrônico \(campo 226\-Chave de Acesso da NF\-Eletrônica, SAFX07\)

__CFOP__

CFOP do item do documento fiscal \(campo “22\-Código Fiscal” da SAFX08\)

__Unidade de Medida__

De acordo com o manual do PR, deve ser informada neste campo a mesma unidade declarada no campo UNID\_ITEM do registro 1000, que é a unidade de medida do cadastro do produto \(unidade da SAFX2007\):

Campo “14\-Código de Medida” da SAFX2013 \(unidade da SAFX2007\)

__\[MFS47333\] __Inclusão da parametrização de Produtos Associados

Quando se tratar de um produto “associado”, a informação gravada neste campo será a unidade de medida do produto principal da parametrização\.

__Quantidade da Entrada  __

__Campo no layout do reg\. 1111:__

__14D\-QTD\_ENTRADA__

De acordo com o manual do PR, neste campo deve ser informada a quantidade do item da nota, *sempre convertida para a unidade de medida declarada no campo anterior* \(unidade de medida do cadastro do produto\)\.

Para isso, é necessário verificar se no item da nota \(SAFX08\) foi utilizada a mesma unidade de medida do cadastro do produto, e caso não, obter o fator de conversão\.

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade 

      do item da nota;

__Senão __

      __\[MFS47313\] Inclusão do campo 137 – Quantidade Convertida da SAFX08__

      Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

      Senão

         Nesse caso o campo será preenchido com a quantidade do item da nota convertida para a unidade de 

         medida declarada no campo anterior \(unidade de medida do cadastro do produto\), utilizando o fator de

         conversão obtido nas tabelas de Conversão de Medida\.

         Assim, será a multiplicação dos seguintes campos:

              

          \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__= = = = = \[MFS47333\] Inclusão de Produtos Associados__

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

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será gerado com o campo Quantidade da Saída sem informação, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será gerado sem a informação da quantidade e do valor unitário”*

*\.*

* *\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

__Valor Unitário__

__Campo no layout do reg\. 1111:__

__15D\-VL\_UNIT\_ITEM__

Neste campo será informado o preço unitário do item da nota, sempre convertido para a unidade de medida declarada no campo “Unidade de Medida” \(unidade de medida do cadastro do produto\), quando necessário\.

Para isso, é necessário verificar se no item da nota \(SAFX08\) foi utilizada a mesma unidade de medida do cadastro do produto, e caso não, obter o fator de conversão \(o procedimento é o mesmo descrito p/a quantidade\)\.

__\[MFS47333\] Inclusão de Produtos Associados__

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __*\(ver Obs no campo anterior sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado com o próprio preço unitário do item 

      da nota;

__Senão __

      Nesse caso o campo será preenchido com o preço unitário do item da nota convertido para a unidade de 

      medida declarada no campo “Unidade de Medida” \(unidade de medida do cadastro do produto\), utilizando o 

      fator de conversão obtido nas tabelas de Conversão de Medida ou calculado pelas quantidades da SAFX08:

      __\[MFS47313\] Inclusão do campo 137 – Quantidade Convertida da SAFX08__

      Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Calcular o Fator de conversão com as quantidades da SAFX08\. Veja:

                  Fator de Conversão = \[137 \- Quantidade Convertida / 24 \- Quantidade do Item \]

                 \[ Preço Unitário do item da nota / Fator de Conversão \]

      Senão

         Considerar o fator de conversão obtido nas tabelas de Conversão de Medida:

         Ver exemplo sobre conversão de medida no documento anexo \(“*Exemplo\_Conversao\_de\_Medida*”\)\.

                 \[ Preço Unitário do item da nota / Fator de Conversão \]

__Valor Base ICMS\-ST__

__Campo no layout do reg\. 1111:__

__16D\-VL\_BC\_ICMS\_ST__

A geração deste campo depende do campo que estiver preenchido na SAFX08, da seguinte forma:

__Se__ campo “61\-Base ICMS\-ST” da SAFX08 estiver preenchido:

     O campo será preenchido com o conteúdo do campo “*61\-Base ICMS\-ST*”;

__Senão__

     __Se__ campo “144\-Base ICMS\-ST não Escriturada”, estiver preenchido:

         O campo será preenchido com o conteúdo do campo “*144\-Base ICMS\-ST não Escriturada*”;

     __Senão__

          __Se__ campo “106\-Base Cálculo Carga Tribut Origem”, estiver preenchido:

               O campo será preenchido com o conteúdo do campo “*106\-Base Cálculo Carga Tribut Origem*”;

          __Senão__

               O campo não será preenchido\.

__*OBS*__*: A base de cálculo a ser utilizada depende do campo que estiver preenchido no item, isso porque devemos considerar que a operação pode ter o ICMS\-ST escriturado ou não escriturado, e em qualquer um dos casos o valor precisa ser demonstrado\. Esta regra segue o mesmo procedimento feito na geração do C176 do Sped Fiscal para obter a base de cálculo do ST \(no cálculo do campo 09 – VL\_UNIT\_BC\_ST\)\. Desta forma, qualquer que seja a situação tributária da nota de entrada, a informação será demonstrada\.  *

__Valor ICMS Suportado__

__Campo no layout do reg\. 1111:__

__17D\-VL\_ICMS\_SUPORT\_ENTR__

Este campo é gerado com o seguinte resultado:

 

                       \[ __Valor do ICMS\-ST__ \] \+ \[ __Valor do ICMS__ \] \+ \[ __Valor do ICMS\-ST FECEP__ \]

Os campos da SAFX08 utilizados para cada um destes valores são os seguintes:

__Valor do ICMS\-ST:__

O valor do ICMS\-ST a ser utilizado depende do campo que estiver preenchido, uma vez que a operação pode ter o ICMS\-ST escriturado ou não escriturado, e nos dois casos o valor do ICMS\-ST precisa ser considerado\. Assim, será utilizado apenas um dos campos descritos a seguir, utilizando o campo que estiver preenchido, na prioridade apresentada:

Campo “52\-Valor ICMS Substituição Tributária”, se preenchido, ou

Campo “145\-Valor de ICMS\-ST não Escriturado”, se preenchido, ou

Campo “133\-ICMS\-ST Não Escriturado”,  se preenchido, ou 

Campo <a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>“107\-Valor Carga Tributária Origem”, se preenchido\.

__*OBS*__*: Esta regra para obter o valor do ICMS\-ST é a mesma utilizada na Portaria CAT 42 \(campo “12\-Valor total do imposto suportado pelo contribuinte substituído” da Ficha 3\)\. *

__Valor do ICMS:__

O valor do ICMS a ser utilizado depende do campo que estiver preenchido, uma vez que a operação pode ter o ICMS escriturado ou não escriturado, e nos dois casos o valor do ICMS precisa ser considerado\. Assim, será utilizado um dos campos descritos a seguir, utilizando o campo que estiver preenchido, na prioridade apresentada:

Campo “43\-Valor ICMS”, se preenchido, ou

Campo “80\-ICMS não Escriturado”

__Valor ICMS\-ST FECEP:__

Campo “140\-FECEP ICMS\-ST”;

__Chave Documento Fiscal Eletrônico de Referência na Devolução__

Este campo não será preenchido\.

*Obs\.: Este campo da tabela é utilizado apenas quando se trata de notas de devolução\. Como a geração dos dados para a CD não considera as devoluções, o campo não será utilizado\.*

__Número do Item do Documento Fiscal de Referência na Devolução__

Este campo não será preenchido\.

*Obs\.: Este campo da tabela é utilizado apenas quando se trata de notas de devolução\. Como a geração dos dados para a CD não considera as devoluções, o campo não será utilizado\.*

# <a id="_Toc36731530"></a>Totalização das Entradas por Produto 

As entradas processadas no item anterior serão totalizadas por Produto, e os resultados armazenados na __Tabela dos Totais por Produto__\. Estes totais darão origem ao registro “*1101\-Totalizador das Entradas do Produto*” do arquivo magnético “ADRC\-ST CD”\.

O cálculo dos totais das entradas é feito produto a produto, e depende *apenas* dos movimentos de entradas do produto\.

Além de totalizar as entradas, também será apurado o total de transferências do produto feita para as filiais que solicitaram ressarcimento/complemento no período\. Esta informação também será armazenada na tabela, e dará origem ao campo 06C\-QTD\_TRANSF do registro 1101 \(ver no quadro abaixo, a regra para geração do campo __QTD\_TRANSF\_E __da__ Tabela dos Totais por Produto__\)\. 

__Origem dos dados:__  Tabelas dos Movimentos;

Recuperação dos movimentos na tabela:

   \- Empresa = código da empresa do login;

   \- Estabelecimento = Código do estabelecimento da Central de Distribuição informado em tela;

   \- Período = período informado em tela;

   \- Tipo de Registro = “__1111__”*;*

Os dados recuperados serão agrupados por Produto\.

Para cada __Produto__ será gravada uma linha na __Tabela dos Totais por Produto__, com os seguintes valores:

\(Os campos sinalizados com asterisco compõem a chave da tabela\)

__\*\*\*__

__Código da empresa__

Código da empresa do login

__\*\*\*__

__Código do estabelecimento__

Código do estabelecimento da Central de Distribuição informado em tela

__\*\*\*__

__Período \(mês e ano\)__

Período \(mês a ano\) informado na tela da geração\.

__\*\*\*__

__Produto__

Produto em questão \(indicador e código\)\. 

__\[MFS47333\] __Inclusão da parametrização de Produtos Associados

Quando se tratar de um produto “associado”, a informação gravada neste campo será o produto principal da parametrização\.

\*\*\*

__Tipo de Registro__

= “__1101__”

__QTD\_TOT\_ENTRADA\_E__

Este campo é preenchido com o seguinte resultado:

Total do campo Quantidade da Entrada  dos movimentos do Produto \(campo __QTD\_ENTRADA __do reg\. 1111\)

__MENOR\_VL\_UNIT\_ITEM\_E__

Este campo __*não*__ será preenchido \(não existe a informação no regitro 1101\)\.

__VL\_BC\_ICMSST\_UNIT\_MED\_E __

Este campo é preenchido com o seguinte resultado:

__                   \[__ Total do campo Valor Base ICMS\-ST dos movimentos do Produto

                             \(campo __VL\_BC\_ICMS\_ST__ do registro 1111\) 

__                                                             __

__                             /__   Campo __QTD\_TOT\_ENTRADA\_E__ deste registro __\]__

__VL\_TOT\_ICMS\_SUPORT\_E __

Este campo é preenchido com o seguinte resultado:

Total do campo Valor ICMS Suportado  dos movimentos do Produto

 \(campo __VL\_ICMS\_SUPORT\_ENTR__ do registro 1111\)

__VL\_UNIT\_MED\_ICMS\_SUPORT\_E __

Este campo é preenchido com o resultado da divisão dos seguintes campos deste registro:

        Campo __VL\_TOT\_ICMS\_SUPORT\_E__    /__    __Campo __QTD\_TOT\_ENTRADA\_E__ 

__QTD\_TRANSF\_E__

Neste campo é informada a quantidade total do produto transferida para as filiais, __*mas*__, considerando __*apenas*__ as filiais que tiveram ressarcimento/recuperação do ICMS\-ST no período\.

O manual orienta que neste campo seja informada *apenas* a quantidade transferida para estas filiais, e não para *todas* as filiais\. 

Assim, será informado neste campo apenas uma parte do total das saídas apurado para o produto __\(\*\*\*\)__, mas considerando apenas as saídas para filiais cujo cálculo do período tenha resultado em ressarcimento\.

__*\(\*\*\*\)*__* Total das saídas do produto apurado na recuperação das entradas, conforme descrito no item “Considerações sobre a recuperação das entradas”\. *

	

Para verificar se a filial teve ressarcimento no período, a seguinte condição deve ser verdadeira:

A filial deve constar na *Tabela da Apuração por Estabelecimento* para o período em questão, e no registro deve constar algum valor de ressarcimento ou recuperação de ICMS\-ST\. Ou seja, um dos seguintes campos deve estar preenchido com valor > zero:

    \- Valor Ressarcimento ST – 1200

    \- Valor Ressarcimento ST – 1300

    \- Valor Ressarcimento ST – 1400

    \- Valor Ressarcimento ST – 1500

    \- Valor Ressarcimento FECOP

 

Obs\.: Esta tabela é gerada no cálculo do Ressarcimento/Complemento \(etapa do processo que é pré\-requisito para a geração dos dados da CD\)\.

Para verificar se a filial consta na Tabela, é necessário obter o Código do Estabelecimento\. Isso pode ser feito através do CNPJ, buscando o CNPJ da Pessoa Fis/Jur da nota fiscal de saída, na tabela ESTABELECIMENTO\. Desta forma, pode se identificar qual o Estabelecimento que correpsonde à filial\. 

Caso não exista o registro da filial na tabela, ou exista, mas nenhum dos campos tenha valor > zeros, então a filial não será considerada para o total de saídas a ser gerado neste campo\.

__QTD\_TOT\_SAIDA\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__VL\_TOT\_ICMS\_EFETIVO\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__VL\_CONFRONTO\_ICMS\_ENTRADA\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__RESULT\_RECUPERAR\_RESSARCIR\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__RESULT\_COMPLEMENTAR\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__APUR\_ICMSST\_RECUPERAR\_RESSARCIR\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__APUR\_ICMSST\_COMPLEMENTAR\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__APUR\_FECOP\_RESSARCIR\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__APUR\_FECOP\_COMPLEMENTAR\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

__VL\_ICMSST\_UNIT\_ENTR\_S__

Para o registro totalizador das entradas \(1100\) este campo __*não*__ será preenchido\.

	

        

# <a id="_Toc36731531"></a>Relatório de Conferência 

O framework desta geração terá uma aba com o título “*Arquivo*”, onde estarão disponíveis dois relatórios de conferência para o usuário:

- Um relatório demonstrando as notas fiscais de entrada processadas para cada Produto \(notas gravadas na Tabela dos Movimentos\);
- Um relatório com os totais apurados para cada Produto \(totais gravados na Tabela dos Totais por Produto\);    

O objetivo deste relatório é possibilitar a conferência das notas fiscais geradas no processo, e também dos resultados obtidos para cada Produto\.

Seguindo as orientações da equipe, os relatórios serão apenas salvos em arquivo, e não serão visualizados em tela\.

Esta aba será semelhante a aba “Arquivo” das gerações de meio magnético \(Sped Fiscal, por exemplo\), onde o usuário informa um diretório onde o arquivo do relatório será salvo\.  

__*Obs*__*\.: Avaliar a melhor forma de gerar estes dois relatórios\. Observar que os totais por produto \(segundo relatório\), tem totais apurados a partir dos movimentos, mas também tem valores apurados a partir de informações que não constam nos movimentos, como por exemplo o campo QTD\_TRANSF\_E\. *

__Detalhes sobre o primeiro relatório:__

- O relatório mostra os dados processados e gravados na Tabela dos Movimentos, item a item; 
- As informações demonstradas são as informações armazenadas na tabela \(vide exemplo na planilha “<a id="_Hlk34317648"></a>*Relatorios\-de\-Conferencia*”, aba “*Entradas CD*”\);
- Os campos que trabalham com IDENT devem sempre exibir a informação do código em questão, e não do IDENT\. Desta forma, teremos:

\-A coluna “Produto” exibirá a informação do ind	icador e código do produto \(“X\-XXXXXXXXXXXXXXX”\);

            \-A coluna “Pessoa Fis/Jur” exibida a informação do indicador e código da pessoa fis/jur \(“X\-XXXXXXXXXXXXXXXXXXXXXXXX”\);

            \-As colunas “Tipo Documento”, “Modelo”, “CFOP” e “Unidade Medida”, exibirão a informação dos respectivos códigos; 

- As linhas serão gravadas no arquivo ordenadas por: *Produto, Data Fiscal, Série do Documento* e *Número do Documento*;

__Detalhes sobre o segundo relatório:__

- O relatório mostra os dados processados e gravados na Tabela dos Totais por Produto; 
- As informações demonstradas são as informações armazenadas na tabela \(vide exemplo na planilha “*Relatorios\-de\-Conferencia*”, aba “*Totais por Produto CD*”\);
- Os campos que trabalham com IDENT devem sempre exibir a informação do código em questão, e não do IDENT \(ex: a coluna “Produto” exibirá a informação do indicador e código do produto\);
- As linhas serão gravadas no arquivo ordenadas por: *Produto*;

= = = = =

