# RCPE_MG_REGRAS

- **Fonte:** RCPE_MG_REGRAS.docx
- **Modificado:** 2023-12-26
- **Tamanho:** 86 KB

---

__               Regras de Geração do Meio Magnético do RCPE – MG__

__                           Resolução 3\.884/07\-MG e 4\.232/10\-MG__

                                                    Revisões:

 

__Data__

__OS / Chamado__

__Descrição __

__Responsável__

17/09/2010

OS3146\-H, I e J

Inclusão do documento no CVS\. 

Vânia Dias Mattos

03/03/2011

OS3146\-H

Alterações RN0005\-05, RN0005\-09 e RNH200

Vânia Dias Mattos

10/03/2011

OS3146\-H

Alteradas as seguintes regras:

RN0200\-06 / RN0205\-06 \(campo EX\_IPI\)

RN0200\-04 \(crítica do TIPO\_ITEM\)

RNH200 e RNH200\-04

RNH200\-12  

RN0220 \(crítica na falta dos índices de conversão p/o H220\) 

Vânia Dias Mattos

06/09/2011

CH113761

Incluído filtro do produto na regra de geração do H230 

Vânia Dias Mattos

12/09/2011

OS3374

Atendimento a Resolução 4\.319/11 a partir de Jan/2012:

\- Exclui o registro 0150

\- Inclui o registro H270 

\- Inclui o registro H275

Juliana Garcia

19/04/2012

CH7363

Alteração na regra de recuperação da composição do produto \(RN0210\)

Vânia Dias Mattos

08/01/2012

Os3837

Inclusão de campo novos nos registros H270 e H275 e novo leiaute – Registro 0000

Tatiane Lima

10/04/2013

CH29889\_2012

Atualização da regra RNH200 incluindo o campo finalidade no agrupamento e da RNH200\-11 gerando o campo com base na informação da SAFX10\.

Marcos

18/04/2013

CH8103\_2013

Alteração na regra de geração do campo 04 do registro H200

Paulo Silva

02/12/2013

CH28986\_2013

Alteração da regra geral de seleção das informações e do campo 04 do Registro H200

Julyana Perrucini

#### Bloco 0 – Abertura, Identificação e Referências

Registro 0000 – Abertura do Arquivo Digital

RN0000

Um registro por arquivo, com os dados de identificação do estabelecimento\.

Origem dos dados: cadastro do estabelecimento \(Módulo Parâmetros\)

RN0000\-03

NUM\_RES

Se o leiaute seleccionado for “*RCPE03 – Resolucao 4\.497/12 – MG”, *gerar a* *informação deste campo com “4497”\.

RN0000\-08

Campo IE:

Este campo tem crítica de obrigatoriedade, e usa a msg de número 01 do doc “RCPE\-MG\_Log\_Erros”\.

RN0000\-09

Campo COD\_MUN:

Este campo tem crítica de obrigatoriedade, e usa a msg de número 02 do doc “RCPE\-MG\_Log\_Erros”\.

Registro 0001 \- Abertura do Bloco 0

RN0001

Um registro por arquivo\.

RN0001\-02

Gravar sempre o conteúdo "0" pois os registros do bloco 0 sempre conterão dados

__Registro 0005 – Dados Complementares do Contribuinte __

RN0005

Este registro é um complemento do 0000, e contém outras informações sobre o estabelecimento\.

Origem dos dados: cadastro do estabelecimento \(Módulo Parâmetros\)

RN0005\-03

Campo CEP:

Este campo tem crítica de obrigatoriedade, e usa a msg de número 03 do doc “RCPE\-MG\_Log\_Erros”\.

RN0005\-04

Campo END:

Este campo tem crítica de obrigatoriedade, e usa a msg de número 04 do doc “RCPE\-MG\_Log\_Erros”\.

RN0005\-05

Campo NUM:

Crítica 1 àEste campo tem crítica de obrigatoriedade, e usa a msg de número 05 do doc “RCPE\-MG\_Log\_Erros”\.

Crítica 2 à Sempre que o conteúdo do número a ser gravado neste campo ultrapassar o tamanho máximo permitido no layout \(05 posições\), gravar mensagem de aviso no log:

                 *“O campo NUM ultrapassou o tamanho máximo permitido \(05 posições\)”*

\(Neste caso o campo deve ser gravado com o conteúdo integral da informação, mesmo excedendo o tamanho máximo do layout\. A idéia é *não* alterar o dado do cliente, e provocar erro no validador caso o usuário não tenha verificado corretamente a msg gerada no log do processo\.\)    

RN0005\-07

Campo BAIRRO:

Este campo tem crítica de obrigatoriedade, e usa a msg de número 06 do doc “RCPE\-MG\_Log\_Erros”\.

RN0005\-08

Campo FONE:

Este campo tem crítica de obrigatoriedade, e usa a msg de número 07 do doc “RCPE\-MG\_Log\_Erros”\.

RN0005\-09

Campo E\-MAIL:

Crítica 1 à Este campo tem crítica de obrigatoriedade, e usa a msg de número 08 do doc “RCPE\-MG\_Log\_Erros”\.

Crítica 2 à Sempre que o conteúdo do e\-mail a ser gravado neste campo ultrapassar o tamanho máximo permitido no layout \(35 posições\), gravar mensagem de aviso no log:

                 *“O campo E\-MAIL ultrapassou o tamanho máximo permitido \(35 posições\)”*

\(Neste caso o campo deve ser gravado com o conteúdo integral da informação, mesmo excedendo o tamanho máximo do layout\. A idéia é *não* alterar o dado do cliente, e provocar erro no validador caso o usuário não tenha verificado corretamente a msg gerada no log do processo\.\)

__Registro 0200 – Tabela de Identificação do Item __

RN0200

Um registro para cada produto referenciado nos demais registros do arquivo\.

Origem dos dados: Tabela de Produtos \(SAFX2013\)\.

RN0200\-03

Campo DESCR\_ITEM:

Preencher de acordo com o parâmetro “*Utilizar a Descrição Detalhada do Produto*” da tela de parametrização dos dados iniciais \(menu “Parâmetros à Dados Iniciais”\):

Se parâmetro “Utilizar a Descrição Detalhada do Produto” *não marcado*:

      Gravar a descrição do produto \(campo 4 da SAFX2013\);

Se parâmetro “Utilizar a Descrição Detalhada do Produto” *marcado*:

     Gravar a descrição detalhada \(campo 22 da SAFX2013\), mas se esta descrição estiver nula, 

     utilizar a descrição do campo 4;

RN0200\-04

Campo TIPO\_ITEM:

Preencher o campo com o conteúdo do campo “*39\-Classificação do Item \(Sped Fiscal\)*” da SAFX2013\.

Crítica 1: Este campo tem crítica de obrigatoriedade, e usa a msg de número 12 do doc “RCPE\-MG\_Log\_Erros”

Crítica 2:  Quando o tipo do item tiver uma classificação <> 00, 01, 02, 03, 04, 05 e 06 \(tipos de produtos que compõem o P3, conforme regra do H200\), o campo deve ser gravado normalmente com a informação que consta na SAX2013, mas deverá ser gerada uma mensagem de erro com a seguinte descrição:

                   *“Tipo de Item inválido de acordo com as regras do registro 0200”*

\(mostrar no log os dados de identificação do produto em questão\)

Observação sobre a critica 2: Para gerar os movimentos no H200 há filtro para recuperar apenas os produtos de classificação 00 a 06\. No entanto, podemos ter produtos vindos de outros registros, como por exemplo, o da composição do produto \(registro 0210\), e os registros referentes à produção própria e de terceiros \(H230/H235/H250/H255\)\. Por isso, foi criada esta mensagem para avisar ao usuário quando um destes produtos tiver uma classificação não aceita pela Resolução\.

RN0200\-05

Campo COD\_NCM:

Gravar o código do NCM \(*considerar as 8 primeiras posições*\)\. Quando o NCM não estiver preenchido no produto, o campo deverá ser gravado sem informação\.

Obs: lembrar que os NCM’s são carregados para o campo 05\-COD\_NBM da tabela de produtos \(SAFX2013\), pois o Mastersaf trabalha com a SAFX2043, que contém na verdade os NCM’s\.

Quando não preenchido __e__ o tipo do item \(campo 04\)  for = \(01, 02, 04 ou 05\) será feita crítica de obrigatoriedade, usando a msg de número 13 do doc “RCPE\-MG\_Log\_Erros”\.

RN0200\-06

Campo EX\_IPI:

Este campo é o código de exceção do NCM, e no Mastersaf ele é carregado para os dois últimos dígitos do NCM , conforme a tabela básica SAFX2043\.

Preencher com os dois últimos dígitos do NCM do produto \(posições 9 e 10\), acrescentando um zero à esquerda, pois o validador não aceita apenas dois dígitos\. Exemplo:

Se código de exceção = 01 à gravar “001”

Se código de exceção = 12 à gravar “012”

Quando estas posições estiverem com brancos \(posições 9 e 10\), o campo EX\_IPI não deve ser preenchido, pois o NCM não tem exceção\.

Registro 0205 – Características Anteriores do Produto

RN0205

Gravar um registro 0205 para cada alteração existente para o item gravado no registro 0200\.

- Considerar apenas as alterações efetuadas durante o período solicitado para a geração;
- Considerar apenas as alterações referentes à descrição do item ou ao NCM;

Pesquisar se durante o período de geração dos dados do arquivo, constam alterações na descrição do produto ou no NCM\. Caso sim, *para cada alteração* deve ser gravado um registro 0205\.

Exemplo:

Produto    =  0001

Descrição = __Caixa da Lápis \- 200 Unidades__

Validade    = __01/01/2000__

Alteração realizada:

Descrição = __Caixa da Lápis  \- Grande__

Validade    = __10/01/2000__

Ao gerar o arquivo para o mês da 01/2000, deve\-se gravar o registro 0200 com a descrição nova \(Caixa da Lápis  \- Grande\), e gravar um registro 0205 com os seguintes dados:

DESCR\_ANT\_IT  =  __Caixa da Lápis \- 200 Unidades__

DT\_INI     =  __01/01/2000__

DT\_FIM   =  __09/01/2000      __*\(será = ao dia anterior ao início da validade da nova descrição\)*

RN0205\-02

Campo DT\_INI:

Data de validade do registro que tem a descrição anterior \(gravada no campo 02\)\.

\(é a data a partir da qual esta descrição começou a ser utilizada\)

RN0205\-03

Campo DT\_FIN:

Preencher com a data imediatamente anterior à data de validade do próximo registro, ou seja, do registro com a nova descrição \(será  o último  dia em que a descrição anterior foi utilizada\)\.

RN0205\-04

Campo DESCR\_ANT\_ITEM:

Gravar a descrição anterior do item, conforme a regra exemplificada na __RN0205__\.

A descrição a ser verificada deve considerar o parâmetro “*Utilizar a Descrição Detalhada do Produto*” \(menu “Parâmetros à Dados Iniciais”\), com objetivo de utilizar a mesma descrição que foi usada no registro 0200:

Se parâmetro “Utilizar a Descrição Detalhada do Produto” *não marcado*:

      Considerar as alterações na descrição do produto \(campo 4 da SAFX2013\);

Se parâmetro “Utilizar a Descrição Detalhada do Produto” *marcado*:

     Considerar as alterações da descrição detalhada \(campo 22 da SAFX2013\), mas se esta descrição

     estiver nula, considerar a descrição do campo 4;

RN0205\-05

Campo COD\_NCM:

Gravar o NCM anterior do item, conforme a regra exemplificada na __RN0205__

Obs: Observar se a alteração foi apenas no próprio NCM \(oito primeiros dígitos do código\), apenas no EX\_IPI \(dois últimos dígitos do código\), ou nos dois\. Dependendo, deve\-se preencher o campo 05\-COD\_NCM, o campo 06\-EX\_IPI, ou os dois\.

RN0205\-06

Campo EX\_IPI:

Gravar o código de exceção anterior do item, conforme a regra exemplificada na __RN0205__

Registro 0210 – Consumo Específico Padronizado

RN0210

Este registro contém a composição padrão do produto gravado no registro 0200\. Será gravado apenas no caso dos produtos com o TIPO\_ITEM = 03 ou 04 \(produto em processo ou produto acabado\)\. 

Origem dos Dados: Tabelas da Composição dos Produtos

                             \(SAFX16, SAFX17, SAFX18, SAFX170 e SAFX180\)

                                                  Estrutura da Árvore de Produtos do Mastersaf:

SAFX16

Produto fabricado \(uma linha para cada produto\)\.

SAFX17

Tabela “filha” da SAFX16\. Insumos utilizados na fabricação do produto \(uma linha para cada insumo, podendo existir ‘n’ insumos para um mesmo produto da SAFX16\)\.

SAFX170

Tabela “filha” da SAFX17\. Detalhamento das fases da produção em que o insumo da SAFX17 é utilizado\.  

SAFX18

Tabela “filha” da SAFX16\. Embalagens utilizadas na fabricação do produto \(uma linha para cada embalagem, podendo existir ‘n’ embalagens para um mesmo produto da SAFX16\)\.

SAFX180

Tabela “filha” da SAFX18\. Detalhamento das fases da produção em que a embalagem da SAFX18 é utilizada\.  

Recuperação dos Dados:

- Obter o produto na SAFX16 através dos seguintes critérios:

               COD\_EMPRESA  = código da empresa  

               COD\_ESTAB       = código do Estabelecimento informado para a geração

               IND\_PRODUTO   = Indicador do produto

               COD\_PRODUTO = Código do produto

                   __Alteração do chamado 7363/2012:__

               DATA\_MOVTO   = considerar a maior data que seja <= data inicial da geração

               DATA\_MOVTO   = Se houverem dados com data enquadrado no período \(\*\), será considerada

                                           a primeira fórmula do período, ou seja, a de menor data\. Caso contrário, ou

                                           seja, caso *não* existam dados no período, será considerada a fórmula mais

                                           recente cadastrada em períodos anteriores\.

                                           \(\*\) período =  intervalo entre a data inicial e final do registro 0000

           

                    \(O manual da Resolução explica que deve ser informada a composição do produto projetada para o início do

                     período, por isso, se existir mais de uma composição no período, será utilizada a primeira\) 

                    \(A alteração do chamado 7363/2012 tem por objetivo permitir que um novo produto possa ter a sua 

                     composição cadastrada em qualquer dia do mês, e não necessariamente no dia inicial do período, como 

                     previa a regra original\. Assim, a composição poderá ser cadastrada para qualquer data de validade, a partir 

                     do início da movimentação do produto\) 

               Se não for encontrado registro da composição do produto, será gravada uma mensagem de

               aviso no log da geração \(“*O produto não foi encontrado na Tabela de Produtos Fabricados *

*               \(SAFX16\)\. O registro da sua composição não será gerado \(0210\)*”\)\.

- A partir da SAFX16, recuperar os componentes do produto \(insumos e embalagens\) nas tabelas “filhas” SAFX17 \(insumos\) e SAFX18 \(embalagens\)\.

                Se não existirem dados nem na SAFX17 nem na SAFX18, gravar mensagem de aviso no log

                da geração \(“*Não existem registros dos componentes do produto nas tabelas de insumos e*

*                embalagens \(SAFX17/SAFX18\)\. O registro da sua composição não será gerado \(0210\)*”\)\.

Tratamentos dos componentes:

Poderão ser recuperados um ou vários componentes do produto\. 

*Para cada componente* deve ser gravado um ou mais registros 0210, *dependendo das fases da produção*, da seguinte forma:

è Quando o componente é utilizado numa única fase, será gerado um único 0210\.

è Quando o componente é utilizado em mais de uma fase, serão gerados tantos registros 0210 quantas forem as fases em que o componente é utilizado\.

A chave deste registro é COD\_ITEM\_COMP \+ COD\_FASE\. 

O conceito para identificar o número de fases é o seguinte:

è Quando o componente é usado *numa única fase*, o código da fase é informado na SAFX17/SAFX18,

     e *não* existirão registros “filhos” nas tabelas de detalhamento das fases \(SAFX170 e SAFX180\);

è Quando o componente é utilizado *em várias fases*, o código da fase *não* é informado na SAFX17 e  

     SAFX18, e neste caso,  o detalhamento das fases é informado nas  tabelas SAFX170 e SAFX180;

 

Logo, *para cada componente* recuperado na SAFX17/SAFX18, deve\-se verificar a necessidade de recuperar o detalhamento das fases na SAFX170/SAFX180 ou não:

__     Se__ Código da Fase da SAFX17/SAFX18 estiver preenchido

           Não utilizar a SAFX170/SAFX180\. Neste caso, serão utilizados os dados da própria

           SAFX17/SAFX18 para gravar o registro 0210;

#     Senão 

           Recuperar os dados da SAFX170/SAFX180 \(a partir do componente da SAFX17/SAFX18\)\. Neste

           caso, serão utilizados os dados da SAFX170/SAFX180 para gravar o registro 0210, e deverá ser  

           gravado um registro para cada fase existente;

__Tratamento de erro quando a fase não for preenchida e não existirem “filhos” na SAFX170/180__:

O código da fase é informação chave do registro 0210, por isso, a sua utilização é obrigatória para quem atende à Resolução 3\.884/07\-MG\. Quando a fase *não* estiver preenchida na SAFX17/SAFX18, e também não existirem registros “filhos” na SAFX170/SAFX180, o registro 0210 *não* deverá ser gerado\.  Nestes casos, deverá ser gravada a seguinte mensagem de erro no log:

\(a mensagem vale para as duas situações, tanto insumo como embalagem, basta que o item seja devidamente identificado no log\)

O código da fase é de preenchimento obrigatório e não foi informado\. O registro 0210 não será gerado para este componente do produto \(consultar Manual de Layout das tabelas SAFX17/18/170/180\)\.

__Sobre as unidades de medida gravadas nos campos 02\-UNID\_ITEM x 06\-UNID\_COMP:__

Quando a unidade do insumo \(UNID\_COMP\) for diferente da unidade do produto \(UNID\_ITEM\), deve\-se gravar um registro “*0220\-Índices de Conversão*” com o fator de conversão entre as duas unidades \(verificar na RN0220 as regras para gravação deste registro\)\.

RN0210\-04

Campo QTD\_COMP\_MIN:

Preencher de acordo com a regra de recuperação dos dados descrita na RN0210:

Se o componente é utilizado numa única fase \(usa a SAFX17/SAFX18\):

      Preencher com o campo “*09\-Quantidade”* da SAFX17/SAFX18;  

Se o componente é utilizado em várias fases \(usa a SAFX170/SAFX180\):

      Preencher com o campo “*10\-Quantidade Mínima*” da SAFX170/SAFX180;

       Obs: Caso a quantidade mínima *não* esteja preenchida, preencher com o mesmo conteúdo da quantidade máxima gravada

       no campo 05 \(nas tabelas SAFX170 e SAFX180 sempre haverá uma das quantidades preenchida, pois esta crítica é feita na

       importação e manutenção\);   

RN0210\-05

Campo QTD\_COMP\_MAX:

Preencher de acordo com a regra de recuperação dos dados descrita na RN0210:

Se o componente é utilizado numa única fase \(usa a SAFX17/SAFX18\):

      Preencher com o campo “*13\-Quantidade Máxima*” da SAFX17/SAFX18;  

       Obs: Caso a quantidade máxima *não* esteja preenchida, preencher com o mesmo conteúdo da quantidade mínima gravada

       no campo 04 \(nas tabelas SAFX17 e SAFX18 a quantidade mínima é obrigatória\);   

Se o componente é utilizado em várias fases \(usa a SAFX170/SAFX180\):

      Preencher com o campo “*11\-Quantidade Máxima*” da SAFX170/SAFX180;

       Obs: Caso a quantidade máxima *não* esteja preenchida, preencher com o mesmo conteúdo da quantidade mínima gravada

       no campo 04 \(nas tabelas SAFX170 e SAFX180 sempre haverá uma das quantidades preenchida, pois esta crítica é feita na

       importação e manutenção\);   

RN0210\-06

Campo UNID\_COMP:

Preencher de acordo com a regra de recuperação dos dados descrita na RN0210:

Se o componente é utilizado numa única fase \(usa a SAFX17/SAFX18\):

      Preencher com o campo “08*\-Unidade de Medida*” da SAFX17/SAFX18;  

Se o componente é utilizado em várias fases \(usa a SAFX170/SAFX180\):

      Preencher com o campo “09*\-Unidade de Medida*” da SAFX170/SAFX180;

Gravar a unidade de medida no Bloco 0, registro 0250\.

RN0210\-07

Campo COD\_FASE:

Preencher de acordo com a regra de recuperação dos dados descrita na RN0210:

Se o componente é utilizado numa única fase \(usa a SAFX17/SAFX18\):

      Preencher com o campo “*14\-Código da Linha/Fase/Processo da Produção*” da SAFX17/SAFX18;  

Se o componente é utilizado em várias fases \(usa a SAFX170/SAFX180\):

      Preencher com o campo “*08\-Código da Linha/Fase/Processo da Produção*” da SAFX170/SAFX180;

Cada código de fase gravado neste campo deve ser gravado no registro H260\.

Registro 0220 – Índices de Conversão de Unidades de Medida 

RN0220

Neste registro serão gravados índices de conversão entre unidades de medida, nas seguintes situações previstas pela Resolução:

__Situação A__ à Quando no registro 0210 a unidade do insumo \(campo 06\-UNID\_COMP\) for diferente da unidade do produto resultante \(campo 02\-UNID\_ITEM\);

__Situação B__ à Quando nos registros H230 x H235 a unidade do insumo \(campo 05\-UNID do H235\) for diferente da unidade do produto produzido \(campo 06\-UNID do H230\);

__Situação C__ à Quando nos registros H250 x H255 a unidade do insumo \(campo 05\-UNID do H255\) for diferente da unidade do produto produzido \(campo 05\-UNID do H250\);

 

__Situação D__ à Quando no registro H220 a unidade do item de origem \(campo 04\-UNID\_ORI\) for diferente da unidade de destino \(campo 06\-UNID\_DEST\)\. 

O preenchimento dos campos dependerá da situação, conforme as regras descritas a seguir:   

Observações:

- __Quando o índice de conversão *não* for encontrado na tabela, será gravada uma mensagem de aviso, *mas apenas para a situação D* \(conversão das unidades orig/dest do registro H220\)\. Para as demais situações \(A, B e C\) *não* será gerada nenhuma mensagem\. Justificativa à quando a comparação das unidades é feita entre o produto resultante e seus insumos, a Resolução 3\.884 cita que muitas vezes a conversão não será possível, e por isso, nestes casos, que são as situações A, B e C, não devemos tratar como erro\. Descrição da mensagem:__

__                   *“Não foi encontrado índice de conversão de medida para a movimentação interna\. *__

__*                               O registro 0220\-Índices de Conversão não será gerado”*\.  __

__               \(informar no log o movimento interno em questão\)__

- A tabela de conversões a ser utilizada \(Padrão ou Por Produto\) dependerá de cada uma das situações citadas acima\. Assim, as regras para cada caso estão descritas no campo RN0220\-05 \(campo FAT\_CONV\)\.

RN0220\-02

Campo UNID\_EST:

__Na situação A__ à preencher com a unidade de medida do produto resultante \(campo 02\-UNID\_ITEM\) do registro 0210\.

__Na situação B__ à preencher com a unidade de medida do produto produzido \(campo 06\-UNID\) do registro H230\.

__Na situação C__ à__ __preencher com a unidade de medida do produto produzido \(campo 06\-UNID\) do registro H250\.

__Na situação D__ à__ __preencher com a unidade de medida do produto de destino \(campo 06\-UNID\_DEST\) do registro H220\.

RN0220\-03

Campo COD\_ITEM\_ORIG:

__Na situação A __à preencher com o código do insumo \(campo 03\-COD\_ITEM\_COMP\) do registro 0210\.

 

__Na situação B__ à preencher com o código do insumo \(campo 03\-COD\_ITEM\) do registro H235\.

__Na situação C__ à preencher com o código do insumo \(campo 03\-COD\_ITEM\) do registro H255\.

__Na situação D__ à preencher com o código do produto de origem \(campo 03\-COD\_ITEM\_ORI\) do registro H220\.

RN0220\-04

Campo UNID\_ORIG:

__Na situação A__ à preencher com a unidade de medida do insumo \(campo 06\-UNID\_COMP\) do registro 0210\.

__Na situação B__ à preencher com a unidade de medida do insumo \(campo 05\-UNID\) do registro H235\.

__Na situação C __à__ __preencher com a unidade de medida do insumo \(campo 05\-UNID\) do registro H255\.

__Na situação D__ à__ __preencher com a unidade de medida do produto de origem \(campo 04\-UNID\_ORI\) do registro H220\.

RN0220\-05

Campo FAT\_CONV:

__Na situação A à__ preencher com o fator de conversão recuperado da tabela de conversão de unidades de medida padrão \(DWT\_CONV\_MEDIDA\) da seguinte forma:

      Medida Origem \(DWT\_CONV\_MEDIDA\) ß unidade gravada no campo 04\-UNID\_ORIG

      Medida Destino \(DWT\_CONV\_MEDIDA\) ß unidade gravada no campo 02\-UNID\_EST 

Obs: Não será utilizada a tabela de conversão por produto \(DWT\_CONV\_PRODUTO\), pois a situação envolve dois produtos diferentes: o insumo e o produto resultante\.

__Na situação B__ à idem 

__Na situação C __à__ __idem

__Na situação D __à__ __idem

__Registro 0250 – Identificação das Unidades de Medida__

RN0250

Todas as unidades de medida referenciadas no arquivo terão os seus dados de cadastro gravados neste registro\.

__Importante__: Observar que na geração deste arquivo são utilizadas unidades de medida originadas de diferentes cadastros\. Como exemplo, a árvore de produtos \(registro 0210\) utiliza as unidades da SAFX2007 \(Unidades de Medida\), enquanto as ordens de produção \(registros H230/H235\) utilizam as unidades da SAFX2017 \(Unidades Padrão\)\. Logo, poderão ocorrer situações em que uma mesma unidade seja cadastrada nas duas tabelas de formas diferentes, exemplo: UN, Un, un etc \.\.\. 

Seria interessante que a implementação pensasse numa forma de impedir a duplicidade, para que a mesma unidade não seja gravada no registro duas vezes \(no Sped houve este problema, e a solução foi gravar sempre os caracteres em maiúscula\)\.

RN0250\-02

Campo UNID:

Quando a unidade for originada da SAFX2017 \(Unidades Padrão\), seu conteúdo deve ser criticado, pois neste caso o tamanho do código é de 08 posições\. Se o código ultrapassar o tamanho máximo do layout \(06 posições\), gravar mensagem de aviso no log:

             *“O campo UNID ultrapassou o tamanho máximo permitido \(06 posições\)”*

\(Neste caso o campo deve ser gravado com o conteúdo integral da informação, mesmo excedendo o tamanho máximo do layout\. A idéia é *não* alterar o dado do cliente, e provocar erro no validador caso o usuário não tenha verificado corretamente a msg gerada no log do processo\.\)

__ __

#### Bloco H – Processo Produtivo

Registro H100 – Período de Apuração do ICMS

RNH100

O arquivo magnético da Resolução 3\.884/07\-MG poderá ser solicitado para um período que contenha mais de uma apuração \(diferentemente do Sped Fiscal cujo PVA só suporta uma apuração\), conforme cita o artigo 5 da Resolução 4\.232/10:

__“Art\. 5º As informações serão entregues ao Fisco sempre que solicitado e será atendida por meio de um só arquivo eletrônico contendo os dados relativos aos períodos solicitados” __

Assim, será gerado um registro H100 para cada apuração de ICMS que esteja contida no período solicitado na tela da geração do meio magnético\. Para gerar os períodos da apuração contidos no intervalo de datas informado em tela, deve\-se verificar  a periodicidade da obrigação fiscal “Apuração do ICMS” \(código da obrigação = “108”\) no Módulo de Controle das Obrigações Estaduais, menu “Obrigações à Obrigações Fiscais à Por Estabelecimento”\.

Obs: Este registro é igual ao registro I200\.

Registro H200 – Controle Permanente do Estoque

RNH200

Registro “filho” do H100\. 

Este registro demonstra toda a movimentação do estoque efetuada no período de apuração do H100\.

Além dos movimentos, também são gravados os saldos do produto ao final *de cada dia*\. Na verdade, o registro H200 representa o Livro da Movimentação de Estoque \(P3\), e se for analisado seguindo a ordenação correta dos campos, demonstra exatamente o formato do livro P3\.

O tipo de informação gravada no H200 é definido pelo campo IND\_OPE:

IND\_OPE  =  E ou S  à são as linhas dos movimentos de entrada e saída

IND\_OPE  =  0, 1 ou 2  à são as linhas dos saldos diários por grupo de contagem

\[__CH29889\_2012__\]

Campos chave do H200 à DT\_MOV, COD\_ITEM, IND\_OPE, TIPO\_MOV, COD\_CCUS e FINALID

Origem dos dados à __SAFX10__ \(Movimentação do Estoque\) e __SAFX52__ \(Saldos Iniciais\)

__\[ALTERADA – CH28986\_2013\]__

Os produtos apresentados no H200 são os produtos da SAFX10 e SAFX52 que atendam às seguintes condições:

- Produtos movimentados no período \(SAFX10\);
- Produtos *sem* movimento no período \(SAFX10\), mas com saldo em estoque \(SAFX52\); __\(\*\*\*\)__
- Somente os produtos de classificação = 00, 01, 02, 03, 04, 05 ou 06 \(campo 39 SAFX2013\);
- NÃO gerar produtos *sem* movimento no período \(SAFX10\) e *sem* saldo em estoque \(SAFX52\);

Para cada produto, deverão ser gravados todos os movimentos do período em questão, gravando também o saldo final do dia na mudança de data, e ao final de todos os movimentos, o saldo final do período\.

__Sobre o parâmetro “Apurar saldos do estoque para o registro H200”__:

A cada geração do arquivo este processo é realizado somente quando este parâmetro da tela da geração for ativado\. Como se trata de um processo demorado, a idéia é que ele seja realizado ao gerar o arquivo pela primeira vez, mas que em eventuais regerações, o processo seja refeito somente quando necessário, ou seja, quando algum saldo ou movimento de estoque tiver sido alterado\. 

Quando a regeração do arquivo for realizada por qualquer outro motivo, não será necessário refazer o processo, e neste caso, serão utilizados os dados já apurados na última geração \(consultar help do menu “Geração à Meio Magnético”\)\.

  

A seguir serão descritas as etapas para a recuperação dos movimentos e apuração dos saldos diários:

Etapas a serem executadas para cada produto:

1\-Recuperação dos movimentos de estoque \(SAFX10\);

2\-Recuperação dos saldos iniciais \(SAFX52\);

3\-Atualização diária dos saldos;

4\-Gravação dos movimentos e dos saldos atualizados;

Detalhes da cada uma das etapas descritas acima:

__1\-Recuperação dos movimentos de estoque__

Critérios de recuperação:

Empresa             = código da empresa  

Estabelecimento = código do estabelecimento informado para a geração

Data do Movimento à deve estar compreendida no período em questão \(período do registro ‘pai” H100\)

Classificação do produto deve ser = 00, 01, 02, 03, 04, 05 ou 06

A classificação do produto é verificada através do campo “*39\-Classificação do Item \- Sped Fiscal*” da Tabela de Produtos \(SAFX2013\)\. Este campo é de preenchimento obrigatório para geração da Resolução 3\.883, pois é utilizado na gravação do registro 0200 \(Bloco 0\)\.

Agrupamento dos dados:

Os movimentos de cada produto são agrupados por data do movimento, entrada / saída, tipo de movimento e centro de custo, que correspondem aos seguintes campos da SAFX10:

Data do movimento à campo “07\-Data do Movimento”

Entrada/Saída         à campo “03\-Movimento de Entrada/Saída”, sendo:

                                      Se = ‘9’  à considerar como saída \(o campo IND\_OPE será  “E”\)

                                      Se <> ‘9’ à considerar como entrada \(o campo IND\_OPE será  “S”\)

Tipo de movimento  à campo “60\-Tipo de Movimento” 

Centro de custo     à campo “15\-Centro de Custo” 

\[__CH29889\_2012__\]

Finalizada     à campo “59\-Finalidade” da SAFX10 ou “47\-Finalidade” da SAFX2013, conforme regra do campo

Assim, os movimentos de entrada ou saída, de mesma data, e que tenham o mesmo tipo de movimento e centro de custo, geram um único registro H200\.

Importante: 

- Observar que os campos “Tipo de Movimento” e “Centro de Custo” são campos *não obrigatórios* na SAFX10, e por isso poderão estar nulos\. Neste caso, o movimento será considerado numa linha de consolidação com a informação = ‘||’ \(ou seja, sem informação\); 

                \(as mensagens sobre a obrigatoriedade de preenchimento de alguns campos estão descritas

                 nas regras específicas de cada campo\)

- A unidade de medida é campo *não chave* da consolidação, e portanto, será tratada aleatoriamente, e terá o conteúdo do primeiro movimento que compõe a consolidação;

__Dúvida x Solução__: Trabalhar igual à emissão do livro P3, que *não* verifica as unidades de medida, ou prever que as unidades possam estar diferentes e efetuar a conversão \(Ex: verificar se os saldos e os movimentos têm as mesmas unidades, e quando não, fazer a conversão com base na unidade do Inventário \(saldo inicial\), ou do primeiro movimento, na falta do saldo inicial\)\. Inicialmente, vamos trabalhar da mesma forma que funciona o P3 do Módulo ICMS, ou seja, sem considerar esta questão das unidades\. Posteriormente, se for o caso, analisaremos os problemas caso ocorram\.  

- O indicador do tipo de documento \(campo 49 da SAFX10 e campo 09\-IND\_DOC\_OPE do H200\) também é campo *não chave* da consolidação, e portanto, será tratado aleatoriamente, e terá o conteúdo do primeiro movimento que compõe a consolidação;

__2\-Recuperação dos saldos iniciais __

Os saldos iniciais do período *não são gravados no arquivo*, mas servem de ponto de partida para os saldos diários que serão contabilizados e gravados no H200 \(são as linhas com IND\_OPE = 0, 1 e 2\)\. 

Critérios de recuperação dos saldos na SAFX52:

Empresa             = código da empresa  

Estabelecimento = código do estabelecimento informado para a geração

Data do Inventário à Dependendo do parâmetro “*Data dos Saldos Anteriores*” \(opção “Parâmetros à

                                   Dados Iniciais”\), a recuperação dos saldos iniciais é feita da seguinte forma:

                                        Se = “Primeiro dia do Período”: 

                                                 A  data do inventário será = data inicial do período \(DT\_INI do H100\);

                                        Se = “Último dia do Período Anterior”: 

                                                 A data do Inventário será = data final do período *anterior*; 

                                                 \(ou seja, será o dia imediatamente anterior ao DT\_INI do H100\)

Grupo de Contagem  = 1, 2, 3 ou 5  \(ver OBS sobre os grupos de contagem\)

Classificação do produto deve ser = 00, 01, 02, 03, 04, 05 ou 06

A classificação do produto é verificada através do campo “*39\-Classificação do Item*” da SAFX2013\.

Obs sobre os grupos de contagem:

- O saldo inicial do grupo de contagem “*5\-Estoque em Depósito Fechado*”, quando existir, será somado ao grupo de contagem “1”\. 
- Campos totalizados:  campo “*13\-Quantidade*” e campo __“*14\-Custo Total*”__
- Já os saldos referentes ao grupo de contagem “*4\-Estoque de Terceiros em poder de Terceiros*” *não* são considerados, pois *não* são solicitados no registro H200 \(ver descrição do campo “IND\_OPE”\)\.

Desta forma, para cada produto pode existir até 3 linhas de saldo, uma para cada grupo \(1/2/3\);

__3\-Atualização diária dos saldos__

Durante o processamento dos movimentos de um produto, os saldos vão sendo atualizados, sempre por grupo de contagem, da seguinte forma:

Grupo de contagem da SAFX10 à campo “05 \- Grupo de Contagem”\.

Grupo de contagem da SAFX52 à campo “04 \- Grupo de Contagem”\.

Saldo final do dia \(grupo “1”\) = saldo do dia anterior do grupo de contagem “1 / 5”   \+  

                                                  movimentos de entrada do dia com grupo de contagem  “1 / 5”   \-

                                                  movimentos de saída do dia com grupo de contagem = “1 / 5”

Saldo final do dia \(grupo “2”\) = saldo do dia anterior do grupo de contagem “2”   \+

                                                  movimentos de entrada do dia com grupo de contagem  “2”   \-

                                                  movimentos de saída do dia com grupo de contagem = “2”

Saldo final do dia \(grupo “3”\) = saldo do dia anterior do grupo de contagem “3”   \+

                                                  movimentos de entrada do dia com grupo de contagem  “3”   \-

                                                  movimentos de saída do dia com grupo de contagem = “3”

Obs:

- Quando se tratar do primeiro dia de movimento, o “saldo do dia anterior” será o saldo inicial recuperado na SAFX52;
- Como já citado anteriormente, o grupo de contagem “5” é tratado junto com o “1”, e o grupo “4” não é considerado na geração do registro H200;

Valores a serem totalizados:

Na apuração dos saldos, totalizar os seguintes valores:

SAFX52 à campo “*13\-Quantidade*” e campo __“*14\-Custo Total”*__

SAFX10 à campo “*20\-Quantidade*” e campo __“*24\-Custo do Item”*__

__4\-Gravação dos movimentos e dos saldos atualizados__

Para cada produto são gravados ‘n’ registros H200, dependendo da movimentação do período;

Os movimentos são consolidados, a partir de determinados critérios, conforme já descrito acima;

Ao mudar a data de movimento, são gravadas as linhas dos saldos resultantes do dia\. Para cada data, poderá existir até 3 linhas de saldo, uma para cada grupo de contagem solicitado no registro H200 \(IND\_OPE = 0, 1 e 2\);

Após a gravação do último registro de movimento, são gravados os últimos saldos do produto, que poderão *ou não* ser referentes à data do último dia do período; 

Tratamento de situações especiais:

\(produtos *com* saldo inicial e *sem* movimentos  __ou__  produtos *sem* saldo inicial e *com* movimentos\) 

- Para os produtos com saldo na SAFX52, mas que *não* tenham movimentação no período em questão, será gravado um registro H200 com o valor do saldo no último dia do período;
- Para os produtos sem registro de saldo na SAFX52, mas que tenham movimentação no período, será considerado saldo inicial = zero para iniciar a totalização dos saldos diários;

__Obs: Como já citado acima, este processo prevê que tanto nos saldos \(SAFX52\) como nos movimentos \(SAFX10\) seja sempre utilizada a mesma unidade de medida para um único produto\. A emissão do livro P3 também se  comporta desta maneira\.__

__Crítica da não existência de dados para o registro H200:__

Caso *não* existam dados para a gravação do registro H200 \(nenhuma linha de saldo ou movimento\!\), deverá ser gravada a seguinte mensagem no log de processo:

"Não foram encontrados dados de saldo e movimentação de estoque para o período solicitado\. O registro H200 não foi gerado\. Favor verificar os dados das tabelas SAFX52 e SAFX10, como também consultar o help referente ao parâmetro "Apurar os saldos do estoque p/o registro H200" da tela de geração da obrigação"\. __ __

RNH200\-02

Campo DT\_MOV:

Preencher de acordo com o tipo de registro \(se saldo, ou movimento\):

Se registro de movimento \(IND\_OPE = E ou S\) 

      Gravar a data do movimento, conforme as regras da consolidação definida na RNH200\.

Se registro de saldo \(IND\_OPE = 0, 1 ou 2\)

     Gravar a data do saldo, conforme as regras de totalização dos saldos definida na RNH200\.

RNH200\-04

Campo VL\_UNIT:

Preencher de acordo com o tipo de registro \(se saldo, ou movimento\):

__Se__ registro de movimento \(IND\_OPE = E ou S\) 

     Gravar o valor unitário que deve ser calculado da seguinte forma:

 

                           Custo total apurado __\(\*\)__  /  Quantidade total apurada __\(\*\*\)__

__       \(\*\)__ Totalização do campo “24\-Custo do Item” da SAFX10 conforme com as regras da consolidação

            dos movimentos definida na RNH200;

__       \(\*\*\)__ Totalização do campo “20\-Quantidade” da SAFX10 \(que será gravado no campo 05 do H200\)

              conforme com as regras da consolidação dos movimentos definida na RNH200;

__Se__ registro de saldo \(IND\_OPE = 0, 1 ou 2\)

     Gravar o saldo do valor unitário que deve ser calculado da seguinte forma:

 

                           Custo total apurado __\(\*\)__  /  Quantidade total apurada __\(\*\*\)__

__       \(\*\)__ Custo apurado ao final de cada dia, totalizado por grupo de contagem, de acordo com as regras

            definidas no RNH200\. O valor do custo é contabilizado a partir do saldo inicial da

              SAFX52, campo “14\-Custo Total”;

__       \(\*\*\)__ Quantidade apurada ao final de cada dia, totalizada por grupo de contagem, de acordo com as

             regras definidas no RNH200\. A quantidade é contabilizada a partir do saldo inicial da SAFX52,

             campo “13\-Quantidade”;

__\[ALTERADO CH8103\_2013\]__

Este campo deverá ser gerado para os seguintesTipos de Itens \(campo 04 do registro 0200\):

00 – Mercadoria para Revenda

01 – Matéria Prima

02 – Embalagem

06 – Produto Intermediário

__\[ALTERADA \- CH28986\_2013\]__

\*Quando este campo não apresentar valor, deve ser gerado com a informação “0” = |0|\.

\*\* Para os Códigos de Itens 03, 04 e 05, deverá ser gerado || havendo valores ou não\.

Obs:O intuíto desta alteração é evitar que devido ao processo de movimentação dos demais produtos, sejam gerados valores negativos neste campo\.

RNH200\-05

Campo QTD:

Preencher de acordo com o tipo de registro \(se saldo, ou movimento\):

Se registro de movimento \(IND\_OPE = E ou S\) 

     Gravar o resultado da totalização do campo “20\-Quantidade” dos movimentos \(SAFX10\), 

     conforme com as regras da consolidação dos movimentos definida na RNH200\.

Se registro de saldo \(IND\_OPE = 0, 1 ou 2\)

     Gravar os saldos apurados ao final de cada dia, por grupo de contagem, de acordo com as

     regras definidas na RNH200\. Os saldos são contabilizados a partir do saldo inicial da SAFX52,

     campo “13\-Quantidade”\. 

\(nos casos em que o campo da quantidade não estiver preenchido, considerar zero\)

RNH200\-06

Campo UNID:

Para geração do H200 é utilizada a unidade padrão, a mesma unidade utilizada na emissão do livro P3 do módulo ICMS\.  

Se registro de movimento \(IND\_OPE = E ou S\) 

     Gravar o conteúdo do campo “13\-Unidade Padrão”, de acordo com as regras de consolidação dos

      movimentos definida na RNH200\.

     

     Obs: A unidade de medida *não* é chave da consolidação, e por isso, será considerada a unidade do

              primeiro movimento que compõe a consolidação\.

              __\(Verificar a observação “Dúvida x Solução” na RNH0200\)__

Se registro de saldo \(IND\_OPE = 0, 1 ou 2\)

     Gravar o conteúdo do campo “08\-Unidade Padrão” referente ao saldo inicial do produto \(SAFX52\)\.  

     Quando não existir saldo inicial, considerar a unidade utilizada na movimentação do produto\.

Crítica à Como esta unidade se refere à tabela de Unidades Padrão \(SAFX2017\), seu conteúdo deve ser criticado:  se o conteúdo do código ultrapassar o tamanho máximo do layout \(06 posições\), gravar mensagem de aviso no log:

                *“O campo UNID ultrapassou o tamanho máximo permitido \(06 posições\)”*

\(Neste caso o campo deve ser gravado com o conteúdo integral da informação, mesmo excedendo o tamanho máximo do layout\. A idéia é *não* alterar o dado do cliente, e provocar erro no validador caso o usuário não tenha verificado corretamente a msg gerada no log do processo\.\)

Gravar a unidade de medida no Bloco 0, registro 0250\.

RNH200\-07

Campo IND\_OPE:

Preencher de acordo com o tipo de registro \(se saldo, ou movimento\):

Se registro de movimento \(IND\_OPE = E ou S\) 

     Gravar “E” quando se tratar de movimento de entrada, ou “S” para os movimentos de saída;

Se registro de saldo \(IND\_OPE = 0, 1 ou 2\)

     O conteúdo deste campo depende do grupo de contagem, conforme as regras da apuração dos

     saldos definida na __RNH0200__\. 

     Gravar “0” quando se tratar de saldo referente ao grupo de contagem 1 e 5  \(*Obs*\)

     Gravar “1” quando se tratar de saldo referente ao grupo de contagem 2  

     Gravar “2” quando se tratar de saldo referente ao grupo de contagem 3  

Obs: Os saldos referentes aos grupos “1” e “5” são somados, e considerados sempre como estoque

próprio em poder do Estabelecimento, utilizando a mesma regra do Inventário do Sped Fiscal; 

RNH200\-08

Campo TIPO\_MOV:

Preencher apenas quando se tratar de registro de movimento \(IND\_OPE = “E” ou “S”\)\.

Informar o conteúdo do campo “60\-Tipo de Movimento”, de acordo com as regras de consolidação dos movimentos definida na RNH200\.

Este campo *é chave* da consolidação, e quando não preenchido no movimento, será gerado um registro consolidado com o campo TIPO\_MOV sem informação \(‘||’\)\.

Crítica à Quando não existir a informação no registro consolidado a ser gravado no H200, será gravada a msg de número 14 do doc “RCPE\-MG\_Log\-Erros”\.

RNH200\-09

Campo IND\_DOC\_OPE:

Preencher apenas quando se tratar de registro de movimento \(IND\_OPE = “E” ou “S”\)\. 

Informar o conteúdo do campo “49\-Indicador do Tipo de Documento” \(F/I\), de acordo com as regras de consolidação dos movimentos definida na RNH200\.

Este campo *não* é chave da consolidação, e por isso, será considerado o conteúdo do primeiro movimento que compõe a consolidação\.

Crítica à Quando não existir a informação no registro consolidado a ser gravado no H200, será gravada a msg de número 15 do doc “RCPE\-MG\_Log\_Erros\.doc”\.

RNH200\-10

Campo COD\_CCUS:

Preencher apenas quando se tratar de registro de movimento \(IND\_OPE = “E” ou “S”\)\.

Informar o código do centro de custo do movimento \(campo 15\-Centro de Custo da SAFX10\), de acordo com as regras de consolidação dos movimentos definida na RNH200\.

Este campo é obrigatório apenas quando o tipo de movimento  = “CS” \(Consumo no Estabelecimento\)\. 

Crítica à Quando no registro consolidado a ser gravado no H200, o campo 08\-TIPO\_MOV = “CS” e campo 10\-COD\_CCUS = ‘||’, será gravada a msg de número 16 do doc “RCPE\-MG\_Log\_Erros\.doc”\.

RNH200\-11

Campo FINALID:

Preencher apenas quando se tratar de registro de movimento \(IND\_OPE = “E” ou “S”\)\.

\[__CH29889\_2012__\]

Informar o conteúdo do campo “59\-Finalidade” do Controle de Estoques \(SAFX10\) quando o campo estiver preenchido\. Quando não estiver preenchida a informação no Controle de Estoques, considerar o campo “*47\-Finalidade*” da Tabela de Produtos \(SAFX2013\), referente ao produto gravado no campo COD\_ITEM\. 

 

Este campo é obrigatório apenas quando o tipo de movimento  = “CS” \(Consumo no Estabelecimento\)\. 

Crítica à Quando no registro consolidado a ser gravado no H200, o campo 08\-TIPO\_MOV = “CS” e campo 11\-FINALID = ‘||’, será gravada a msg de número 17 do doc “RCPE\-MG\_Log\_Erros\.doc”\.

RNH200\-12

Campo CAPAC\_ARMAZ

Preencher apenas quando se tratar de registro de saldo do grupo de contagem '1', ou seja, quando o campo 07\-IND\_OPE for = 0\.

Preencher apenas para os produtos de classificação = 01, 02, 03, 04 ou 05 \(campo 04\-TIPO\_ITEM do registro 0200, que é gerado a partir do campo “39\-Classificação do Item” da SAFX2013\)\.

Informar o conteúdo do campo “*48\-Capacidade Máxima de Armazenamento*” da Tabela de Produtos \(SAFX2013\), referente ao produto gravado no campo COD\_ITEM\. 

Registro H220 – Outras Movimentações Internas entre Mercadorias

RNH220

Neste registro são demonstradas as movimentações internas entre produtos\. Estas movimentações são identificadas pelo indicador de redesignação da SAFX10\. 

OBS: Os campos 51, 52 e 53 da SAFX10 \(Indicador de redesignação e produto de origem\) foram criados para atender ao Ato Cotepe 35/05, que tinha um registro idêntico a esse, com o mesmo nome \(H220\)\. Posteriormente, no Ato Cotepe 70/05 este registro foi retirado, e os campos não chegaram a ser utilizados\. Para a Resolução, utilizaremos a mesma solução planejada para o Ato Cotepe 35/05, mas foi incluído também o campo “61\-Un Méd Produto Origem/Destino”\. 

Origem dos dados à SAFX10

Recuperar todos os movimentos de *saída* no período que sejam redesignação \(movimentação interna entre produtos\), que atendam aos seguintes critérios:

\-Empresa                   = código da empresa  

\-Estabelecimento      = código do estabelecimento informado para a geração

\-Movimento E/S        = 9  \(somente as saídas\)

\-Data do Movimento  = deve estar compreendida no período \(período do registro “pai” \-H100\)

\-Redesignação \(campo 51\) = S

OBS: Os dados serão recuperados a partir dos movimentos de saída, porque precisamos da quantidade do produto de origem para gravar o campo 07\-QTD do H220\. De acordo com as informações do site daSefaz\-MG \(opção “Perguntas & Respostas” da Cartilha da Resolução\) esta quantidade é referente *ao produto de origem* da redesignação\.

Só pode existir um registro por dia para um mesmo produto origem e destino\. A chave deste registro é \[DT\_MOV \+ COD\_ITEM\_ORI \+ COD\_ITEM\_DEST\]\.

Por isso, os dados devem ser agrupados, e a quantidade totalizada\.

Critérios para o grupamento: 

\-Data do Movimento – campo “07\-Data do Movimento”

\-Produto Origem à campos “11\-Indicador do Produto” e 12\-Código do Produto”

\-Unidade Origem à campo “33\-Unidade de Medida”

\-Produto Destino à campos “52\-Indicador do Produto Orig/Dest” e “53\-Código do Produto Orig/Dest”  

\-Unidade Destino à campo “61\-Unidade do Produto Orig/Dest”

\-campo a ser totalizado à campo “20\-Quantidade”

OBS: No grupamento utilizaremos também as unidades de medida, para evitar problemas\. Em condições normais a unidade será sempre a mesma para um dado produto\. Mas se ocorrer de um produto apresentar unidades diferentes, as quantidades serão somadas separadamente, para cada unidade\. Sendo assim, poderá ocorrer de numa data gerarmos mais de um registro H220 para o mesmo produto Orig x Dest\. Neste caso o validador acusará o erro e o usuário poderá identificar o problema\. 

__Críticas sobre campos não preenchidos:__

\(1\)\-Sempre que a informação da unidade de origem não estiver preenchida no movimento recuperado da SAFX10 \(campo 33\), deve\-se gravar uma mensagem de erro no log, e o movimento não poderá ser considerado p/o H220\. Mensagem de erro:

 “A unidade de medida do produto não foi informada no\(s\) movimento\(s\) de estoque\. O registro H220 não será gerado para este\(s\) movimento\(s\)”\.

\(2\)\-Sempre que a informação do produto de destino ou da unidade de medida de destino não estiver preenchida no movimento recuperado da SAFX10 \(campos 52, 53 e 61\), deve\-se gravar uma mensagem de erro no log, e o movimento não poderá ser considerado p/o H220\. Mensagem de erro:

“O produto de destino \(campo 52/53\) não foi informado no\(s\) movimento\(s\) de estoque\. O registro H220 não será gerado para este\(s\) movimento\(s\)”\.

ou

“A unidade de medida do produto de destino não foi informada no\(s\) movimento\(s\) de estoque\. O registro H220 não será gerado para este\(s\) movimento\(s\)”\.

Para que o usuário possa identificar o movimento, o log deve mostrar a data, o produto e outras informações importantes do movimento\. 

OBS: Se for necessário para facilitar a recuperação dos dados, a mensagem poderá ser emitida para um conjunto de movimentos na mesma situação\. Para isso, o agrupamento dos dados poderá tratar estes campos sem informação com um caracter branco\. Mas eles não devem ser gravados no H220\! 

__Sobre a unidade de origem \(campo 04\) x unidade de destino \(campo 06\):__

Sempre que a unidade do produto de origem gravada no campo 04 for diferente da unidade do produto de destino gravada no campo 06, será gravado no registro “*0220\-Índices de Conversão*” o fator de conversão entre as duas unidades \(verificar na RN0220 as regras para gravação deste registro\)\. Lembrando que o registro 0220 é um registro “filho” do “*0200\-Identificação do Item*”, e assim, o registro 0220 a ser gravado deve ficar associado ao registro 0200 *do produto final*\.

 

RNH220\-02

Campo DT\_MOV:

Informar a data do movimento conforme o agrupamento de dados descrito na RNH220\.

RNH220\-03

Campo COD\_ITEM\_ORI:

Informar o produto de origem conforme o agrupamento de dados descrito na RNH220\.

RNH220\-04

Campo UNID\_ORI:

Informar a unidade de medida do produto de origem conforme o agrupamento de dados descrito na RNH220\.

RNH220\-05

Campo COD\_ITEM\_DEST:

Informar o produto de destino conforme o agrupamento de dados descrito na RNH220\.

RNH220\-06

Campo UNID\_DEST:

Informar a unidade de medida do produto de destino conforme o agrupamento de dados descrito na RNH220\.

RNH220\-07

Campo QTD:

Informar a quantidade conforme o agrupamento de dados descrito na RNH220\.

Registro H230 – Ordem de Produção – Itens Produzidos

RNH230

Neste registro são gravadas as Ordens de Produção referentes aos produtos fabricados durante o período de apuração em questão \(registro H100\)\.

Origem dos Dados: 

SAFX108 – Ordens de Produção

SAFX109 – Itens das Ordens de Produção

SAFX139 – Detalhamento dos Itens da Ordem de Produção por Fases 

As ordens de produção da SAXF108 devem ser recuperadas pelo período de referência:

Critérios para a recuperação dos dados na SAFX108:

\-COD\_EMPRESA  = código da empresa;

\-COD\_ESTAB       = código do Estabelecimento informado para a geração;

\-PERIODO\_REF = deve ser o mês e ano da apuração \(mês/ano = mês/ano da DT\_FIN do H100\); 

  Alteração incluída no chamado CH113761: 

\-Considerar apenas as ordens de produção cujo produto \(campos 05/06\) seja do tipo “03\-Produto em Processo” ou “04\-Produto Acabado”, ou seja, produtos em que o campo “*39\-Classificação do Item – Sped Fiscal*” da SAFX2013 seja = 03 ou 04; 

\(Obs: Como o “PERIODO\_REF” da SAFX108 só prevê periodicidade mensal p/a apuração do ICMS, \(pois tem apenas o mês e o ano\), não há como tratar a periodicidade\) 

As OP’s devem ser gravadas no H230 por produto, e por fase da produção\. Quanto ao produto, o seu código já compõe a chave da SAFX108 junto com o número da OP, mas a fase esta nas tabelas dos insumos consumidos na produção, seguindo a mesma lógica da Árvore de Produtos \(SAFX16/17/18\)\.

\(ver conceito do campo “Código Linha/Fase/Processo da Produção” das tabela  SAFX109 e SAFX139 no Manual de Layout\)

Será gravado *um registro* da OP/Produto no H230, para cada fase da produção  existente nas tabelas SAFX109 e SAFX139\. Seguem dois exemplos demonstrando os dados da SAFX108/109/139 e os resultados gravados no H230 e H235:

__à Exemplo 1: __\(todos os insumos numa única fase\) 

__   Na SAFX108:__

__      Na SAFX109:__

   OP

 Produto

Insumo

Fase

QTD

  OP1

   XYZ

INS1

F1

  25,00

INS2

F1

120,00

INS3

F1

  40,00

__                No H230: __

__     No H235:__

   OP

 Produto

   Fase

Insumo

 QTD

 OP1

   XYZ

    F1

INS1

  25,00

INS2

120,00

INS3

  40,00

__à Exemplo 2: __\(os insumos são utilizados em diferentes fases, mas cada insumo numa única fase\) 

__   Na SAFX108:__

__      Na SAFX109:__

   OP

 Produto

Insumo

Fase

QTD

  OP1

   XYZ

INS1

F1

  25,00

INS2

F2

120,00

INS3

F3

  40,00

__                No H230: __

__     No H235:__

   OP

 Produto

   Fase

Insumo

 QTD

 OP1

   XYZ

    F1

INS1

  25,00

 OP1

   XYZ

    F2

INS2

120,00

 OP1

   XYZ

    F3

INS3

  40,00

__à Exemplo 3: __\(os insumos INS1 e INS2 são usados em mais de uma fase, por isso, a SAFX139 é utilizada\) 

__   Na SAFX108:__

__         Na SAFX109:__

__ Na SAFX139:__

   OP

 Produto

Insumo

Fase

QTD

Fase

QTD

 OP1

   XYZ

INS1

25,00

   F1

 20,00

   F2

   5,00

INS2

120,00

   F1

 80,00

   F2

 30,00

   F3

 10,00

INS3

   F1

40,00

__                No H230: __

__     No H235:__

   OP

 Produto

   Fase

Insumo

 QTD

 OP1

   XYZ

    F1

INS1

 20,00

INS2

 80,00

INS3

 40,00

 OP1

   XYZ

    F2

INS1

   5,00

INS2

 30,00

 OP1

   XYZ

    F3

INS2

 10,00

Pelos exemplos descritos acima, observa\-se que os dados da Fase no registro H230, e os dados do H235, são gerados a partir da SAFX109 __ou__ da SAFX139, dependendo do preenchimento do campo Fase na SAFX109, da seguinte forma:

- Quando o insumo é usado *numa única fase*, o código da fase é informado na SAFX109, e não há registros “filhos” na SAFX139 para este insumo;
- Quando o insumo é usado *em várias fases*, o código da fase *não* é informado na SAFX109, e ao invés disso, existirão registros “filhos” na SAFX139 para demonstrar as diferentes fases e suas respectivas quantidades;

Logo, *para cada insumo da OP* recuperado na SAFX109, deve\-se verificar a necessidade de recuperar o detalhamento das fases na SAFX139 ou não:

__     Se__ Código da Fase da SAFX109 estiver preenchido

           Não utilizar a SAFX139\. Neste caso, serão utilizados os dados da própria SAFX109;

#     Senão 

           Recuperar os dados da SAFX139 \(a partir do insumo da SAFX109\)\. Neste caso, serão utilizados

           os dados da SAFX139;

__Tratamento de erro quando a fase não for preenchida e não existirem “filhos” na SAX139__:

O código da fase é informação chave do registro H230, por isso, a sua utilização é obrigatória para quem atende à Resolução 3\.884/07\-MG\. Quando a fase não estiver preenchida na SAFX109, e também não existirem registros “filhos” na SAFX139, o registro H230 não deverá ser gerado, assim como os seus insumos no H235\. Nestes casos, deverá ser gerada a seguinte mensagem de erro no log:

O código da fase é de preenchimento obrigatório e não foi informado\. O registro H230 não será gerado p/esta Ordem de Produção \(consultar Manual de Layout das tabelas SAFX109 e SAFX139\)\.

No campo do log destinado à identificação do registro, informar os dados da OP e Produto em questão\. 

RNH230\-04

Campo COD\_DOC\_OP:

Se conteúdo do campo “Cód\. Diferenciador de Produção” <>  ‘ ‘ \(um caracter branco\)

      Preencher com a concatenação do campo “04\-Código da Ordem de Produção” com o campo 

      “15\-Cód\. Diferenciador de Produção”, no seguinte formato:   COD\_OP  \+  ‘\-‘  \+  COD\_DIF\_OP

##### Senão

      Preencher apenas com o conteúdo do campo “04\-Código da Ordem de Produção”;

   

RNH230\-06

Campo UNID:

Preencher com o campo “09\-Unidade a ser Produzida” da SAFX108\.

Obs: Apesar do tamanho do campo na SAFX108 ter 8 posições, o campo se refere à SAFX2007, cujo código da unidade tem apenas 3 posições\. Por isso, não será necessário criticar se o campo excede o tamanho máximo do layout \(6 posições\)\.

Gravar a unidade de medida no Bloco 0, registro 0250\.

RNH230\-08

Campo COD\_FASE:

O preenchimento deste campo depende das diferentes fases de produção em que os componentes do produto fabricado forem utilizados, conforme as regras gerais descritas na RNH230\.

  

No caso dos componentes utilizados numa única fase:

      Campo “Código da Linha/Fase/Processo da Produção” da tabela SAFX109;

No caso dos componentes utilizados em mais de uma fase:

      Campo “Código da Linha/Fase/Processo da Produção” da tabela SAFX139;

Cada código de fase gravado neste campo deve ser gravado no registro H260\. Ao gravar a fase no H260, verificar a necessidade de gravar o fator de conversão de unidades de medida no H265, caso a unidade do H230 seja diferente da unidade do H260 \(ver detalhes nas regras RNH260 e RNH265\)\. 

Registro H235 – Ordem de Produção – Insumos Consumidos

RNH235

Este registro é “filho” do H230, e nele serão gravados todos os componentes utilizados na produção do produto final informado no H230 \(campo 05\-COD\_ITEM\), lembrando que os componentes são demonstrados por fases do processo \(campo 08\-COD\_FASE do H230\)\.

Para melhor entendimento, verificar os três exemplos descritos na RNH230\. 

Origem dos Dados: 

SAFX109 – Itens das Ordens de Produção

SAFX139 – Detalhamento dos Itens da Ordem de Produção por Fases 

Quando o componente for utilizado em mais de uma fase do processo de produção, alguns dados serão recuperados da SAFX139\. Do contrário todas as informações serão obtidas na SAFX109, da seguinte forma:

Se o código da fase for informado na SAFX109:

      Utilizar os dados da SAFX109; 

Senão 

      Recuperar os dados da SAFX139, que contém o detalhamento das fases;

__Sobre a unidade do componente \(H235\) x unidade do produto final \(H230\):__

Sempre que a unidade do insumo gravado no H235 \(campo 05\-UNID do H235\) for diferente da unidade do produto final \(campo 06\-UNID do H230\), deve\-se gravar um registro “*0220\-Índices de Conversão*” com o fator de conversão entre as duas unidades \(verificar na RN0220 as regras para gravação deste registro\)\. Lembrando que o registro 0220 é um registro “filho” do “*0200\-Identificação do Item*”, e assim, o registro 0220 a ser gravado deve ficar associado ao registro 0200 *do produto final*\.

RNH235\-02

Campo DT\_SAIDA:

Preencher com a data da saída do componente do estoque, conforme tabela utilizada \(ver RNH235\):

Campo “08\-Data de Saída” da SAFX109 __ou__ “10\-Data de Saída” da SAFX139 

RNH235\-04

Campo QTD:

Preencher com a quantidade utilizada do componente, conforme tabela utilizada \(ver RNH235\):

Campo “10\-Quantidade Utilizada” da SAFX109 __ou__ “12\-Quantidade Utilizada” da SAFX139 

RNH235\-05

Campo UNID:

Preencher com a unidade de medida do componente, conforme tabela utilizada \(ver RNH235\):

Campo “09\-Unidade de Medida” da SAFX109 __ou__ “11\-Unidade de Medida” da SAFX139 

Obs: Apesar do tamanho do campo na SAFX109 ter 8 posições, o campo se refere à SAFX2007, cujo código da unidade tem apenas 3 posições\. Por isso, não será necessário criticar se o campo excede o tamanho máximo do layout \(6 posições\)\.

Gravar a unidade de medida no Bloco 0, registro 0250\.

Registro H250 – Industrialização Terceiros – Itens Produzidos

RNH250

Neste registro são gravadas as informações da produção efetuada por terceiros\.

Origem dos dados: SAFX153 \(Produção de Terceiros\) e SAFX154 \(Insumos Consumidos\)

Filtro para recuperação dos dados:

__SAFX153__ è Empresa               = código da empresa  

                     Estabelecimento   = código do Estabelecimento informado para a geração

                     Data da Produção = deve estar compreendida entre a data inicial e data final do registro 

                                                       H100 \(lembrando que este registro é “filho” do registro H100\)

__SAFX154__ è Para cada registro recuperado da SAFX153, recuperar todos os registros “filho” na

                     SAFX154\.

Para cada registro recuperado da SAFX153, será gravado um ou vários registros H250, dependendo das fases de produção envolvidas na industrialização do produto\. As fases de produção se encontram na SAFX154, tabela “filha” da SAFX153, que detalha os insumos consumidos por fase da produção\.

 

Exemplos:

__à Exemplo 1: __\(todos os insumos consumidos se referem a uma única fase\) 

__                      Na SAFX153:__

__             Na SAFX154:__

 Data Produção

   Produto

   QTD

Insumo

Fase

     QTD

     15/01/2011

      XYZ

    150

 INS1

   F1

       25

 INS2

   F1

     120

 INS3

   F1

       40

__                           No H250: __

__               No H255:__

Data Produção

 Produto

 QTD

Fase

   Insumo

      QTD

    15/01/2011

    XYZ

  150

   F1

     INS1

        25

     INS2

      120

     INS3

        40

__à Exemplo 2: __\(os insumos são utilizados em diferentes fases, *mas cada insumo numa única fase*\) 

__                       Na SAFX153:__

__             Na SAFX154:__

   Data Produção

 Produto

   QTD

Insumo

 Fase

     QTD

     15/01/2011

    XYZ

    150

 INS1

  F1

       25

 INS2

  F2

     120

 INS3

  F3

       40

__                           No H250: __

__               No H255:__

 Data Produção

  Produto

QTD

Fase

   Insumo

      QTD

    15/01/2011

    XYZ

 150

   F1

     INS1

        25

    15/01/2011

    XYZ

 150

   F2

     INS2

      120

    15/01/2011

    XYZ

 150

   F3

     INS3

        40

__à Exemplo 3: __\(os insumos são utilizados em diferentes fases, e alguns, *em mais de uma fase*\) 

__                       Na SAFX153:__

__             Na SAFX154:__

   Data Produção

 Produto

   QTD

Insumo

 Fase

     QTD

     15/01/2011

    XYZ

    150

 INS1

  F1

      20

 INS1

  F2

        5

 INS2

  F1

      80

 INS2

  F2

      30

 INS2

  F3

      10

 INS3

  F1

      40

__                           No H250: __

__               No H255:__

Data Produção

 Produto

QTD

Fase

   Insumo

      QTD

    15/01/2011

    XYZ

 150

   F1

     INS1

        20

     INS2

        80

     INS3

        40

    15/01/2011

    XYZ

 150

   F2

     INS1

          5

     INS2

        30

    15/01/2011

    XYZ

 150

   F3

     INS2

        10

Registro H255 – Industrialização Terceiros – Insumos Consumidos

RNH255

Este registro é “filho” do H250, e nele serão gravados todos os insumos utilizados na produção do produto final informado no H250, lembrando que os insumos são demonstrados por fases do processo \(campo 06\-COD\_FASE do H250\)\.

Para melhor entendimento, verificar os exemplos descritos na RNH250\. 

Origem dos Dados: 

SAFX154 – Produção de Terceiros – Insumos Consumidos

__Sobre a unidade do componente \(H255\) x unidade do produto final \(H250\):__

Sempre que a unidade do insumo gravado no H255 \(campo 05\-UNID do H255\) for diferente da unidade do produto final \(campo 05\-UNID do H250\), deve\-se gravar um registro “*0220\-Índices de Conversão*” com o fator de conversão entre as duas unidades \(verificar na RN0220 as regras para gravação deste registro\)\. Lembrando que o registro 0220 é um registro “filho” do “*0200\-Identificação do Item*”, e assim, o registro 0220 a ser gravado deve ficar associado ao registro 0200 *do produto final*\.

Registro H260 – Linha, Fase e Processo de Produção

RNH260

Neste registro serão gravadas as informações de todas as fases de produção \(campo COD\_FASE\) referenciadas no arquivo \(registros 0210, H230 e H250\)\.

Os dados de cada código de fase devem ser obtidos na *Tabela de Fases da Produção* \(módulo DW, item “Manutenção à Produção à Fases da Produção”\)\.

Critérios para recuperação dos dados:

\-Empresa                                     = código da empresa

\-Estabelecimento                         = código do estabelecimento informado p/ geração

\-Código da Linha/Fase/Processo = campo COD\_FASE em questão \(gravado no 0210,H230 ou H250\)

\-Data de validade inicial à deve ser <= data final do período em questão \(DT\_FIM do registro H100\)

\-Data de validade final   à quando preenchida, deve ser >= data inicial do período em questão \(DT\_INI

                                           do registro H100\)

Como a tabela trabalha com validade, a linha a ser recuperada é a que estiver válida p/o período em questão, que é o período do registro H100 \(lembrando que o registro H260 é “filho” do H100\)\. Por isso, a validade da fase deve estar de acordo c/o período do H100\.

OBS: Serão gravadas no H260 *apenas* as fases referenciadas em algum registro do arquivo, de acordo com a orientação que consta na Resolução 4\.232/2010\-MG: “Este registro tem o objetivo de identificar as linhas, fases e processos de produção, existentes no estabelecimento informante e aqueles terceiros participantes que industrializam por encomenda, cujo processo seja pertinente ao processo produtivo do estabelecimento informante, de tal forma que reflita o retrato do processo produtivo\. Devem ser identificadas as linhas, fases e processos de produção, e os terceiros participantes, identificados nos Registros: 0210, H230 e H250”\.  

RNH260\-04

Campo ORD\_FASE:

Gravar a concatenação dos campos “Linha” \+ “Número de Ordem de Execução da Fase”\.

Estes dois campos são numéricos de duas posições , e o campo ORD\_FASE é numérico de quatro posições\.  Ao fazer a concatenação deve\-se preservar os zeros à esquerda de cada campo, e ao gravar a informação no campo ORD\_FASE deve\-se manter os zeros\.

Exemplos:

Linha                                 =   01

N\. Ordem de Execução     =   05

Conteúdo a ser gravado   =   0105

Linha                                 =   10

N\. Ordem de Execução     =   01

Conteúdo a ser gravado   =   1001

Registro H265 – Índices de Conversão entre Produto Resultante x Fase

RNH265

Este registro é “filho” do H260, e deverá ser gerado sempre que ocorrer a seguinte situação:

- A fase de produção gravada no H260 for referente ao estabelecimento, e não a terceiros\. Neste caso, o campo “Industrialização Terceiros” da Tabela de Fases da Produção \(utilizada para geração do H260\) será = “N”;
- Quando a fase de produção gravada no H260 for originada do registro H230, campo \(08\-COD\_FASE\);
- Quando a unidade de medida gravada no H260 \(campo 06\-UNID\_CAPAC\)  for diferente da unidade gravada no registro H230 \(campo 06\-UNID\);

Ocorrendo esta situação deverá ser gravado um registro H265, seguindo as regras de preenchimento descritas para cada campo\.   

OBS: Observar que a situação descrita acima poderá ocorrer ‘n’ vezes, considerando a mesma fase de produção e as mesmas unidades de medida, mas o índice de conversão será gravado uma única vez\! 

RNH265\-02

Campo COD\_ITEM:

Gravar o código do produto produzido, que consta no registro H230, campo 05\-COD\_ITEM\.

\(da mesma forma que no H230, gravar a concatenação do indicador \+ código do produto\)

RNH265\-03

Campo UNID\_ITEM:

Gravar a unidade de medida que consta no registro H230, campo 06\-UNID\.

RNH265\-04

Campo IND\_CONV:

Preencher com o fator de conversão recuperado das tabelas de conversão de unidades de medida, da seguinte forma:

Como neste registro as unidades de medida se referem a um único produto, que é o produto do H230, utilizaremos o procedimento padrão de recuperação do índice de conversão, que é primeiro pesquisar  na tabela de conversão específica do produto, e quando não encontrar, efetuar a pesquisa na tabela de conversão padrão:

- Recuperar o índice da *tabela de conversão por produto* \(__DWT\_CONV\_MEDIDA2__\), a partir dos   seguintes critérios: 

  

                 Produto              = produto gravado no campo 02\-COD\_ITEM    \(produto do H230\)

                 Medida Origem  = unidade gravada no campo 03\-UNID\_ITEM   \(unidade do H230\)

                 Medida Destino  = unidade que consta na fase  \(unidade do registro “pai” H260\)

 

- Se o índice *for encontrado*: 

                  Gravar o conteúdo do índice de conversão \(campo “Fator de Conversão”\);

- Se o índice *não for encontrado*:

                 Recuperar o índice da *tabela de conversão padrão* \(__DWT\_CONV\_MEDIDA__\), a partir dos

                 seguintes critérios: 

  

                  Medida Origem  = unidade gravada no campo 03\-UNID\_ITEM   \(unidade do H230\)

                  Medida Destino  = unidade que consta na fase  \(unidade do registro “pai” H260\)

- Se o índice *for encontrado* na tabela padrão: 

                  Gravar o conteúdo do índice de conversão \(campo “Fator de Conversão”\);

- Se o índice *não for encontrado*:

                 Gravar o campo sem informação \(“||”\)

                 Gravar mensagem de erro no log com a seguinte descrição: “*O registro H265 foi gerado sem*

*                 a informação do índice de conversão, pois o fator de conversão não foi encontrado nas*

*                 tabelas de conversão de medida*” 

 

Registro H270 – Produção – Acerto de Erro de Apontamento

RNH270

Neste registro serão gravadas as informações de acerto de erro de apontamento ocorrido na quantidade de produção acabada de produtos de tipos 03 ou 04, informada nos Registros H230 e H250, por período de apuração de ocorrência do fato\. Ou seja:

Será gravado apenas no caso dos produtos com o TIPO\_ITEM = 03 ou 04 \(produto em processo ou produto acabado\)\.

Critérios para recuperação dos dados:

\-Empresa                  = código da empresa

\-Estabelecimento       = código do estabelecimento informado p/ geração

\-IND\_PRODUTO       = Indicador do produto da Safx13

\-COD\_PRODUTO      = Código do produto da Safx13

\-Data de validade inicial do erroà deve ser preenchida a data inicial

\-Data de validade final do erro à deve ser preenchida a data final, sendo >= a data inicial\.

A linha a ser recuperada é a que estiver válida p/o período em questão, que é o período do registro H100 \(lembrando que o registro H270 é “filho” do H100\)\. Por isso, a validade da fase deve estar de acordo c/o período do H100\.

Caso ocorra erro de apontamento apenas do consumo \(Registro H275\), o Registro H270 deverá ser informado com os campos de quantidade zerados;         

RNH270\-04

__COD\_DOC\_OP__

Inclusão deste campo a partir do leiaute “*RCPE03 – Resolucao 4\.497/12 – MG”\.*

Se conteúdo do campo “Cód\. Diferenciador de Produção” <>  ‘ ‘ \(um caracter branco\)

      Preencher com a concatenação do campo “Código da Ordem” com o campo 

      “Cód\. Diferenciador de Produção”, no seguinte formato:   COD\_OP  \+  ‘\-‘  \+  COD\_DIF\_OP

##### Senão

      Preencher apenas com o conteúdo do campo “Código da Ordem”;

Registro H275 – Insumos Consumidos – Acerto de Erro de Apontamento

RNH275

Este registro é “filho” do H270\. Serão gravadas as informações de acerto de erro de apontamento ocorrido na quantidade de consumo de insumos de tipos 01 a 05, informada nos Registros H235 e H255, por período de apuração de ocorrência do fato\. Ou seja:

Será gravado apenas no caso dos produtos com o TIPO\_ITEM = 01 ou 05 \(matéria prima ou subproduto\)\.

Caso ocorra erro de apontamento apenas da produção, o Registro H275 não deverá ser informado;

OBS: Observar que a situação descrita acima poderá ocorrer ‘n’ vezes, considerando que o H270 uma única vez\!

RNH275\-06

__COD\_INS\_SUBST__

Inclusão deste campo a partir do leiaute “*RCPE03 – Resolucao 4\.497/12 – MG”\.*

Recuperar a informação do campo “Insumo”\.

#### Bloco I – Informações Contábeis

Registro I100 – Centros de Custos

RNI100

Neste registro são gravados todos os centros de custos utilizados na empresa, e não apenas os referenciados nos registros H200 \(ver consulta feita à Sefaz\-MG respondida em 26/05/10\)\.

Origem dos dados à SAFX2003

Considerar apenas os centros de custo com validade \(campo 02\-Data Início/Inclusão/Alteração\) <= a data final informada na tela da geração do arquivo \(campo 02\-Data Início/Inclusão/Alteração\)\.

Importante:

Quando ocorrer de um mesmo centro de custo ter vários registros na tabela, com diferentes datas de validade, serão considerados apenas os registros em que ocorreu alteração da descrição\. Se a alteração *não for referente à descrição*, o registro da nova validade *será desconsiderado*\. 

Exemplo:

Considerando os seguintes dados na SAFX2003:

CC              55

Data            01/01/2010

Descrição:  Lavanderia  

Indicador de Controle Investimento: Sim

CC              55

Data            20/01/2010

Descrição:  Lavanderia  

Indicador de Controle Investimento: Não

CC              55

Data            01/02/2010

Descrição:  Cozinha  

Indicador de Controle Investimento: Não

CC              55

Data            15/02/2010

Descrição:  Cozinha  

Indicador de Controle Investimento: Sim

Serão gravados no registro I100 apenas as seguintes linhas:

REG

DT\_ALT

COD\_CCUS

CCUS

I100

01/01/2010

55

Lavanderia 

I100

01/02/2010

55

Cozinha

 

Registro I200 – Período de Apuração do ICMS

RNI200

O arquivo magnético da Resolução 3\.884/07\-MG poderá ser solicitado para um período que contenha mais de uma apuração \(diferentemente do Sped Fiscal cujo PVA só suporta uma apuração\) conforme cita o artigo 5 da Resolução 4\.232/10:

__“Art\. 5º As informações serão entregues ao Fisco sempre que solicitado e será atendida por meio de um só arquivo eletrônico contendo os dados relativos aos períodos solicitados” __

Assim, será gerado um registro I200 para cada apuração de ICMS que esteja contida no período solicitado na tela da geração do meio magnético\. Para gerar os períodos da apuração contidos no intervalo de datas informado em tela, deve\-se verificar  a periodicidade da obrigação fiscal “Apuração do ICMS” \(código da obrigação = “108”\) no Módulo de Controle das Obrigações Estaduais, menu “Obrigações à Obrigações Fiscais à Por Estabelecimento”\.

Obs: Este registro é igual ao registro H100\.

Registro I210 – Apuração de Custos

RNI210

Registro “filho” do I200\. Para cada registro I200, que representa um período de apuração do ICMS, serão gravados os valores da apuração de custos no I210\.

Origem dos dados: SAFX143

Critérios para recuperação dos dados:

Empresa             = código da empresa  

Estabelecimento = código do estabelecimento informado para a geração

Data da Apuração = data final do período da apuração do registro “pai” \(DT\_FIN do I200\)

Classificação do produto deve ser = 03 \(Produto em Processo\) ou 04 \(Produto Acabado\)  

A classificação do produto é verificada através do campo “*39\-Classificação do Item \- Sped Fiscal*” da Tabela de Produtos \(SAFX2013\)\. Este campo é de preenchimento obrigatório para geração da Resolução 3\.883, pois é utilizado na gravação do registro 0200 \(Bloco 0\)\.

Apesar do Manual de Layout da SAFX143 orientar que apenas os produtos deste tipo devem ser carregados para esta tabela, será feito o filtro na geração\. Desta forma, evitamos problemas no validador do arquivo\.  

