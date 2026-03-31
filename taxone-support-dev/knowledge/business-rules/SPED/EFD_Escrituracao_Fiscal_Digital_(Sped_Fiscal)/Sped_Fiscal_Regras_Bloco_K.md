# Sped_Fiscal_Regras_Bloco_K

- **Fonte:** Sped_Fiscal_Regras_Bloco_K.docx
- **Modificado:** 2024-11-04
- **Tamanho:** 156 KB

---

Sped FiscaI – Bloco K

__\(documento criado em 12/06/2018, quando o conteúdo do Bloco K foi extraído do documento Sped\_Fiscal\_Regras\) __

__\(para consultar as revisões anteriores, ver o documento Sped\_Fiscal\_Regras original\)__

Quadro de Revisões

__                                                                 Revisões realizadas a partir de 12/06/2018__

__          __

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

09/10/2018

MFS\-20988

Inclusão das origens 6, 7, 8 e 9 no Registro K270 referentes aos registros K291, K292, K301 e K302 e inclusão dos Registros K290, K291, K292, K300, K301 e K302, em atendimento ao Ato COTEPE 48/2017\.

Julyana Perrucini

19/11/2018

MFS\-21976

Inclusão dos Registros K290, K291, K292, K300, K301 e K302 na geração do meio magnético PIM, inclusão da conversão da unidade de medida nos Registros K291, K292, K301 e K302 e tratamento para código diferenciador da produção para casos em que possa ocorrer duplicidade\.

Julyana Perrucini

18/01/2019

MFS23846

Alteração do registro K235 para incluir o tratamento do campo tipo do item do registro 0200\.

Andréa Rocha

30/01/2018

MFS24090

Alteração dos registros K270 e K275 para incluir o tratamento do campo tipo do item do registro 0200\.

Andréa Rocha

10/05/2019

MFS26934

Alteração dos registros K235 para incluir o tratamento da geração do K230 sem gerar o K235\.

Andréa Rocha

12/06/2019

MFS28094

Alteração dos registros K235 para incluir o tratamento da geração do K230 sem gerar o K235\.

Andréa Rocha

11/12/2019

MFS31413

Alteração da chave do registro K260

Andréa Rocha

26/05/2021

MFS64813

Alteração do registro K200 para passar a gravar o registro 0220, quando houver conversão de unidade de medida\.

Andréa Rocha

21/10/2021

MFS74583

Alteração do campo 05 dos registros K235 e K255\.

Aline Melo

11/05/2022

MFS85920

Alteração da obrigatoriedade e validação de registros\. 

Aline Melo

18/05/2022

MFS85955

Criação do registro K010\.

Aline Melo

16/11/2022

MFS97186

Inclusão da opção 2 no registro K010 e ajustes nas regras sobre a NÃO OBRIGATORIEDADE de alguns registros conforme o tipo de leiaute\.

Aline Melo

06/02/2023

MFS435439

Inclusão de tratamento do campo de DT\_FIN, para considerar o novo campo de DAT\_ENCERRAMENTO da tabela de Inscrição Estadual para os clientes que encerrarem a Inscrição Estadual\. K100\. 

Rogério Ohashi

28/10/2024

MFS700354

Inclusão do tratamento da classificação do produto para o registro K215, conforme as regras do guia prático\.

Andréa Rocha

01/11/2024

MFS703404

Inclusão do tratamento da classificação do produto para o produto destino do registro K220, conforme as regras do guia prático\.

Andréa Rocha

04/11/2024

MFS703457

Inclusão do tratamento da classificação do produto para o insumo do registro K255, conforme as regras do guia prático\.

Andréa Rocha

#### Bloco K – Controle da Produção e do Estoque 

__Registro K001 – Abertura do Bloco K__

RNK001

Um registro por arquivo\.

__Registro K010 – Informação sobre o Tipo de Leiaute \(Simplificado/Completo\)__

<a id="_Hlk103776038"></a>RNK010

Este registro indica o tipo de leiaute que o contribuinte adotou na informação do bloco K\.

Um registro por arquivo\.

__\[MFS85955\] Válido a partir da versão 1\.16 \(Janeiro/2023\), em atendimento ao ATO COTEPE 21/2022\.__

RNK010\-02

Campo 02 – IND\_TP\_LEIAUTE

Se o campo “Leiaute Simplificado”, no item de menu Parâmetros > Dados Iniciais estiver marcado, preencher com ‘0’ \(Simplificado\), senão ‘1’ \(Completo\)\.

__\[MFS97186\] Inclusão da opção 2 – Leiaute restrito aos saldos de estoque__

Para o correto preenchimento deste campo, no item de menu <a id="_Hlk119511242"></a>Parâmetros > Dados Iniciais, verificar:

Se no campo “Tipo de Leiaute” estiver selecionado:

Completo: preencher com ‘1’;

Simplificado: preencher com ‘0’;

Restrito aos Saldos de Estoque: preencher com ‘2’\.

__Registro K100 – Período de Apuração do ICMS __

RNK100

Este registro indica o período de apuração a que se referem os dados apresentados no Bloco K\.

Conforme planilha DEPARA, as datas inicial e final serão as mesmas do registro E100\.

__\[ALTERAÇÃO\-MFS435439\] __Tratamento da Regra para Inscrição Estadual Encerrada

Tratamento na geração do campo de DT\_FIN para os clientes que encerrarem a Inscrição Estadual da UF do próprio Estabelecimento, nesse caso o sistema deverá consultar o campo de Data de Encerramento \(DAT\_ENCERRAMENTO\) da tabela REGISTRO\_ESTADUAL, e segui conforme a Regra abaixo:  

__Tratamento:__

__Se__ o campo de DAT\_ENCERRAMENTO da tabela REGISTRO\_ESTADUAL estiver preenchido;

   __E __o campo de UF da tabela REGISTRO\_ESTADUAL for igual ao campo de UF do Estabelecimento;

__   Preencher __o campo de DT\_FIN com o campo de DAT\_ENCERRAMENTO da tabela REGISTRO\_ESTADUAL\.

__Obs¹\.:__ Preencher os demais campos com a mesma Regra do Registro K100, conforme regra já existente\.

__Obs²\.:__ Para esse campo ser considerado, a data de encerramento deverá estar entre o período de referência da geração\.

__Registro K200 – Estoque Escriturado__

RNK200

Este registro demonstra a quantidade em estoque de cada produto na data final do período\.

__ __

__Origem dos dados:__ SAFX52

__Recuperação dos Dados__:

__\[ALTERADA – CH13518\_2015\]__

\-Empresa à código da Empresa informante

\-Estabelecimento à código do Estabelecimento informante *\(ver OBS 1 e OBS 2\)*

\-Data do Inventário à data final do período \(campo DT\_FIN do registro K100\)

\-Grupo de Contagem à 1, 2, 3 e 5 *\(ver OBS 3\)*

\-Produto à considerar apenas os registros de inventário cujo produto tenha o campo TIPO\_ITEM do

                   registro 0200 = __00, 01, 02, 03, 04, 05, 06 e 10; __

__\[ALTERADA – CH25342\_2015\]__

\-Quantidade à considerar apenas os registros de inventário cuja quantidade seja <> zero\.

A identificação do tipo do item considera a mesma regra do registro 0200, ou seja, verifica a parametrização do menu “*Parâmetros à Registro 0200 à Tipo do Item*”, e quando o produto não constar, verifica o campo “*39\-Classificação do Item*” da SAFX2013\.

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo 23\-Insc\.Estadual da SAFX52\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

OBS 3 \- Seguindo a mesma regra do registro do Inventário \(H010\), o grupo 4 \(estoque de terceiros em poder de terceiros\) não será considerado, e o grupo 5 \(estoque em depósito fechado\) será apresentado junto com o grupo 1\.

Todos os produtos gravados neste registro serão gravados no Bloco 0, registro 0200\.

__Agrupamento dos dados:__

Os dados recuperados de acordo com os critérios acima, serão agrupados por:

\-Produto \(campos 06 e 07 SAFX52\)

\-Grupo de Contagem \(campo 03 SAFX52\)

\-Pessoa Fis/Jur proprietária da mercadoria \(campos 24 e 25 da SAFX52\)

O grupamento é necessário pois a chave da SAFX52 permite a existência de ‘n’ registros de inventário referentes a um mesmo produto e mesma data\. Isso porque existem várias informações que compõe a chave, como por exemplo a *Natureza do Estoque* \(além dos campos que compõe a coluna DISCRI\_INVENTARIO\)\.

Como citado na OBS3, o grupo de contagem 5 será tratado junto com o 1, sendo considerado também “Estoque Próprio em poder do Estabelecimento”\.

 

No grupamento, a pessoa fis/jur será utilizada *apenas* quando o grupo de contagem for = 2 ou 3, conforme o quadro abaixo:

        Tratamento da pessoa fis/jur no grupamento: 

Grupo de Contagem

Utilização da pessoa fis/jur proprietária \(campos 24 e 25\)

1 \(estoque próprio, em poder do estabelecimento\)

Não usar

2 \(estoque próprio em poder de terceiros\)

Usa

3 \(estoque de terceiros em poder do estabelecimento\)

Usar

5 \(estoque em depósito fechado\)

Não usar

Sobre a pessoa fis/jur à Observar que a pessoa fis/jur *não é campo obrigatório* na SAFX52\. No registro K200 ele é obrigatório apenas para os grupos de contagem 2 e 3 \(IND\_EST = 1 ou 2\)\. Assim, o procedimento será o seguinte: quando se tratar dos grupos do contagem 2 e 3, mas a pessoa fis/jur não estiver preenchida na SAFX52, será considerada uma pessoa em branco, e o registro será gravado com o campo COD\_PART vazio \(||\)\. Este recurso é para evitar que o produto seja desconsiderado no Inventário\. O log trará mensagem de erro para estas situações

__Será gerado um registro K200 para cada agrupamento descrito acima:__

O campo 04\-QTD será gravado com a totalização da quantidade de todos os registros grupados, mas considerando sempre a unidade de medida do cadastro \(SAFX2013\), conforme explicado a seguir:

__Sobre a conversão de medida:__

A quantidade informada neste registro \(campo 04\-QTD\) será sempre referente à unidade de medida do cadastro do produto \(SAFX2013\)\. 

Nos casos em que a unidade de medida do inventário \(campo “12\-Unidade de Medida” da SAFX52\) for diferente da unidade do cadastro \(campo “14\-Código de Medida” da SAFX2013\), será feita a conversão de medida para calcular a quantidade do inventário com base na unidade de medida do cadastro\.

Se ao efetuar a comparação entra as unidades \(X52 x X2013\) for verificado que o campo “14\-Código de Medida” da SAFX2013 *não* esta preenchido, o registro de inventário em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log: *“Na geração do registro K200 é necessário o preenchimento do campo 14\-Código de Medida do cadastro do produto, p/efeito de comparação de medidas entre SAFX52 x SAFX2013\. O registro do inventário não será considerado na geração”*\. O log mostrará também os dados de identificação do produto, para que o usuário possa verificar o problema\.

*\(quanto à X52 não é necessária esta crítica, pois o campo é de preenchimento obrigatório\)*

 

Observações sobre a comparação das unidades de medida \(X52 x X2013\):

*   \- Este procedimento garante que as quantidades sejam expressas na unidade de cadastro do*

*     produto, como orienta o manual, e também que a totalização seja feita sempre considerando uma*

*     única unidade, para não haver inconsistências;*

*   \- A comparação das unidades é feita a partir dos campos referentes à  SAFX2007, porque as tabelas*

*     de conversão de medida do Mastersaf usam esta medida\. Já na geração do 0200 a medida utilizada*

*     é a do campo da unidade padrão \(SAFX2017\)\. Assim, a geração prevê que as duas unidades*

*     estejam preenchidas no cadastro, e naturalmente, que sejam sempre as mesmas\.*

A conversão será feita conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro de inventário em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O registro não será considerado na geração do registro K200\.”*

\(na coluna do log que mostra a chave do registro, serão demonstradas as informações necessárias para permitir a identificação do registro do inventário que foi originou a mensagem de erro\) 

Alteração da __MFS64813__: Conforme verificado com o setor de informação, se houver conversão de unidade de medida, o registro 0220 deve ser gerado\.

__Informar Fator de Conversão entre as Unidade do Inventário x Unidade de cadastro do Produto:__

*\(considerando a unidade registrada no Bloco 0, registro 0200\)*

__Se__ a unidade de medida do inventário for <> unidade de medida do cadastro do produto 

        Neste caso será gerado o registro 0220 informando o fator de conversão da unidade do produto 

        de origem para a unidade do produto de destino\.

RNK200\-03

Campo 03\-COD\_ITEM:

Produto do grupamento \(campos 6 e 7 da SAFX52\), conforme a regra __RNK200__\.

Na gravação deste campo será utilizada a mesma regra definida para os demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo, será gravado no Bloco 0 \(registro 0200\)\.

RNK200\-04

Campo 04\-QTD:

Total da quantidade dos registros consolidados, conforme o grupamento definido na __RNK200__\. 

A quantidade informada neste campo considera a unidade de medida gravada no registro 0200, conforme as regras de conversão de medida definidas na regra __RNK200__\. 

RNK200\-05

Campo 05\-IND\_EST:

Grupo de contagem do grupamento, conforme a regra __RNK200__,  fazendo o seguinte de\-para entre o grupo de contagem da SAFX52 e o campo IND\_EST do Sped:

__SAFX52__

__IND\_EST__

1 – Estoque próprio em poder do Estabelecimento

5 – Estoque em Depósito Fechado

0

2 – Estoque próprio em poder de terceiros

1

3 – Estoque de terceiros em poder do Estabelecimento

2

Obs: a opção “4 \- Estoque de terceiros em poder de terceiros” da SAFX52 não consta deste de\-para porque não será contabilizada, conforme definido na __RNK200__\.

RNK200\-06

Campo 08\-COD\_PART:

Código da pessoa fís/jur do grupamento \(campos 24 e 25 da SAFX52\), conforme a regra __RNK200__\.

Será utilizada a mesma regra de concatenação já definida para os demais registros:   \[Indicador da pessoa  \+  "\-"  \+  Código da pessoa\]

A pessoa fis/jur informada neste campo, será gravada no Bloco 0 \(registro 0150\)\.

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\)\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Quando a informação for = um caracter branco \(“ “\), conforme a regra do grupamento quando não existe a pessoa fis/jur p/os grupos de contagem 2 e 3, o campo será gravado sem informação \(||\), e no log será gravada a seguinte mensagem de erro:

   

*“O campo COD\_PART é de preenchimento obrigatório p/o Grupo de Contagem 2 ou 3, e não foi informado” *

__Registro K210 – Desmontagem de Mercadorias – Item de Origem__

<a id="_Hlk103162818"></a>RNK210

Este registro foi criado pelo Ato Cotepe 7/2016, e implementado na __MFS4992__ \(Jun/2016\)\.

 

Neste registro são gravadas as informações sobre os processos de DESMONTAGEM efetuados durante o período de apuração em questão \(data inicial e final do registro K100\)\.

__\[MFS85920\] e \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

<a id="_Hlk120885492"></a>A partir desse layout, a geração do registro K210 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K210, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K210 será gerado ou não, pois não foi feito tratamento  pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX108 – Ordens de Produção

Critérios para a recuperação dos dados na SAFX108:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e OBS 2\)*;

\-PERIODO\_REF   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-Produto \(campos 05/06\) = serão considerados apenas os registros cujo produto seja do tipo 

                                         “00\-Mercadoria para Revenda”, “01\-Matéria Prima”, “02\-Embalagem”, 

                                         “03\-Produto em Processo”, “04\-Produto Acabado”, “05\-Subproduto” e

                                         “10\-Outros Insumos”\. Ou seja,  produtos em que o campo TIPO\_ITEM do

                                          registro 0200 = __00, 01, 02, 03, 04, 05 __ou__ 10__;

\-Tipo da Ordem de Produção/Serviço = __2__ \(“Desmontagem de Mercadorias”\)

Em relação ao tipo do item: Observar que a identificação do tipo do item é feita através da parametrização do menu “*Parâmetros à Registro 0200 à Tipo do Item*”, ou do campo “*39\-Classificação do Item*” da SAFX2013, quando o produto não constar na parametrização\. Trata\-se exatamente da mesma regra já utilizada por todo o Sped Fiscal, para os registros em que é necessário identificar o tipo do item\.

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “19\-Inscrição Estadual\-AM” da SAFX108\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada ordem de produção recuperada da SAFX108 será gravado um registro K210, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\. 

Sobre o número da ordem de produção: Quando o registro K210 for gravado com o parâmetro “*Não informar o número da ordem de produção \(SAFX108\)*” ativado, ou seja, sem a informação dos campos 02, 03 e 04 \(ordem de produção, e sua data inicial e final\), a chave do K210 passa a ser apenas o campo COD\_ITEM\_ORI, de acordo com o Guia Prático Vrs 2\.0\.19\. Desta forma, poderá ocorrer duplicidade do registro caso o usuário não siga as orientações de utilização do parâmetro \(a orientação nesse caso é carregar p/a SAFX108 apenas um registro por Período/Produto\)\. Caso ocorra a duplicidade, os registros serão gravados normalmente, mas no log será gravada a seguinte mensagem:

* “O registro K210 foi gerado em duplicidade para o produto\.Consultar help dos parâmetros do Bloco K no menu Dados Iniciais”*

  

Será gravada apenas uma mensagem por cada caso de duplicidadep, ou seja, uma mensagem para cada produto que tiver gerado registros duplicados\. O log mostrará também a identificação do produto em duplicidade\.

RNK210\-02

Campo DT\_INI\_OS:

__Se__ parâmetro “*Não informar o número da ordem de produção no registro *__*K210*__” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

__Senão__  

     Este campo é preenchido com a data de início da OP/OS \(campo “07\-Data de Início da OP” da

     SAFX108\)\.

Obs: Por orientação do Guia Prático as datas da OP/OS também não devem ser apresentadas quando não existir a informação da OP/OS\.

RNK210\-03

Campo DT\_FIN\_OS:

__Se__ parâmetro “*Não informar o número da ordem de produção no registro *__*K210*__” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

__Senão__  

     Este campo é preenchido com a data de conclusão da OP \(campo “08\-Data de Conclusão da OP” 

     da SAFX108\), da seguinte forma:

__     Se__  data de conclusão não preenchida 

           *ou* 

          data de conclusão > data final do periodo da geração \(DT\_FIN do K100\)  

           Neste caso o campo será gravado sem informação;

__      Senão__

           Neste caso o campo será preenchido normalmente com a data da conclusão da OP;

RNK210\-04

Campo COD\_DOC\_OS:

\(__MFS10054__: passou a usar o parâmetro “*Considerar o Cód\. Diferenciador no Cód Ordem de Produção*”\)

A geração deste campo depende de alguns parâmetros do menu “Dados Iniciais”, da seguinte forma:

__Se__ parâmetro “*Não informar o número da ordem de produção no registro *__*K210*__” = “S”:

     Neste caso este campo *não* será preenchido\. 

__Senão__  

     __Se__ conteúdo do campo “Cód\. Diferenciador de Produção” <>  ‘ ‘ \(um caracter branco\)

           __e           __

          parâmetro “*Considerar o Código Diferenciador no Código da Ordem de Produção*” = “S”

           O campo será preenchido com a concatenação do campo “04\-Código da Ordem de Produção” 

           com o campo “15\-Cód\. Diferenciador de Produção”, sem utilizar nenhum separador;

           \(conforme alteração da __MFS2159 \(ch 25797\)__ a concatenação deixou de utilizar o separador\) 

           Se ao concatenar os dois campos o conteúdo a ser gravado ultrapassar 30 posições \(limite do

           layout\), o registro da ordem de produção em questão será *desconsiderado*, e será gravada a

           seguinte mensagem no log da geração: *“O campo COD\_DOC\_OS ultrapassou o tamanho máximo*

*          permitido \(30 posições\)\. Verificar os parâmetros sobre a geração deste campo\. A ordem de*

*          produção não será considerada na geração do registro K210”\.*\(o log informará também os dados  

          para identificação da ordem de produção\)\. 

##### __     __Senão

           O campo será preenchido apenas c/o conteúdo do campo “04\-Código da Ordem de Produção”;

RNK210\-05

Campo COD\_ITEM\_ORI:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à concatenação do Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no registro 0200 do Bloco 0\.

RNK210\-06

Campo QTD\_ORI:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificada a igualdade entre as duas, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX108 \(campo 09\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K210/K215 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. A ordem de produção não será considerada na geração”\.*\(o log informará também os dados para identificação da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX108, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX108 se refere à SAFX2007 \(apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017\), mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD\_ORI será a própria quantidade de origem da

      SAFX108 \(campo 29\-Quantidade Origem\) ; 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX108 para a SAFX2013, e a quantidade da

      SAFX108 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX108:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX108 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. A ordem de produção não será considerada na geração do registro K210\.”*

__Registro K215 – Desmontagem de Mercadorias – Item de Destino __

<a id="_Hlk103169536"></a>RNK215

Este registro foi criado pelo Ato Cotepe 7/2016, e implementado na __MFS4992__ \(Jun/2016\)\.

 

Este registro é “filho” do K210, e demonstra os insumos retornados ao estoque resultante do processo de desmontagem\. Para cada registro “pai” gravado no registro K210, serão gravados no K215 todos os insumos relacionados\. 

__\[MFS85920__<a id="_Hlk120885649"></a>__\] \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

<a id="_Hlk120885849"></a>__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K215 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K215, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K215 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

<a id="_Hlk120885863"></a>__Para o período de geração anterior a 01/01/2023:__

__Origem dos Dados: __

SAFX109 – Itens das Ordens de Produção

__\[MFS700354\] Inclusão da validação do TIPO\_ITEM do registro 0200__

__Critérios para a recuperação dos dados na SAFX109__:

	

A recuperação dos itens de cada ordem de produção/serviço gravada no K210 é feita a partir dos dados chave que identificam a ordem de produção/serviço:

\- COD\_EMPRESA  

\- COD\_ESTAB      

\- PERIODO\_REF

\- COD\_OP

\- COD\_DIF\_PRODUCAO

\- IDENT\_PRODUTO\_OP

\- Produto OP \(campos 13/14\) = serão considerados apenas os registros cujo produto seja do tipo 

                                               “00\-Mercadoria para Revenda”, “01\-Matéria Prima”, “02\-Embalagem”, 

                                               “03\-Produto em Processo”, “04\-Produto Acabado”, “05\-Subproduto” e

                                               “10\-Outros Insumos”\. Ou seja,  produtos em que o campo TIPO\_ITEM do

                                               registro 0200 = __00, 01, 02, 03, 04, 05 __ou__ 10__;

Para cada item de produção recuperado da SAFX109, será gravado um registro K215, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\. 

__Procedimento quando não existirem dados na SAFX109 para a produção gravada no K210:__

*\(seguindo a mesma regra criada pela *__*MFS2413 *__*\(chamado 25930/15\) para o registro K235\)*

Segundo regras do Guia Prático \(vrs 1\.0\.19\) quando a informação do registro “pai” K210 é feita sem apresentar a ordem de produção/serviço, a apresentação do\(s\) registro\(s\) filho\(s\) é obrigatória\. Por isso, é realizada a crítica a seguir:

__Se__ parâmetro “*Não informar o número da ordem de produção no registro* __K210__” = “S” e *não* houver informação na SAFX109:

      Neste caso o registro de produção K215 *não* será gravado *\(procedimento já adotado antes da*

*      MFS2413\)*, e será gravada a seguinte msg de erro no log da geração: *“Quando a geração do registro*

*      K210 é realizada sem a informação do número da ordem de produção, é obrigatório informar os*

*      insumos de destino \(SAFX109\)”\.  *O log informará os dados necessários para identificação do

      registro da SAFX108 em questão\.

RNK215\-02

Campo COD\_ITEM\_DES:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à concatenação do Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no registro 0200 do Bloco 0\.

RNK215\-03

Campo QTD\_DES:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificada a igualdade entre as duas, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX109 \(campo 09\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro do item da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K210/K215 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O item da ordem de produção não será considerado na geração”\.*\(o log informará também os dados para identificação do item da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX109, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX109 se refere à SAFX2007 \(apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017\), mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD\_DES será a própria quantidade do campo 

      “29\-Quantidade de Destino” da SAFX109; 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX109 para a SAFX2013, e a quantidade da

      SAFX109 será ajustada para esta nova medida \(seguindo o mesmo exemplo da RNK210\-06\)\.

      O conteúdo a ser gravado será a quantidade já ajustada\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item da ordem de produção não será considerado na geração do registro K215\.”*

__Registro K220 – Outras Movimentações Internas entre Mercadorias__

RNK220

Neste registro são demonstradas as movimentações internas entre produtos\. Estas movimentações são identificadas pelo indicador de redesignação da SAFX10 \(campo 51\-Redesignação\)\. 

*OBS: Os campos 51, 52 e 53 da SAFX10 \(Indicador de redesignação e produto de origem\) foram criados para atender ao Ato Cotepe 35/05, que tinha um registro idêntico ao H220 da Resolução 4232/MG \(RCPE\-MG\), inclusive c/o mesmo nome \(H220\)\. Posteriormente, o registro foi retirado pelo  AC 70/05, e os campos não chegaram a ser utilizados\. Quando o módulo RCPE\-MG foi criado, foi utilizada a mesma solução planejada para o AC 35/05\. Agora, com a revogação da Resolução, o registro K220 do Sped será gerado, a princípio, seguindo a mesma lógica\.*

__\[MFS97186\] Tratamento em atendimento ao layout versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K220 passa a ser __NÃO OBRIGATÓRIA __para o tipo de leiaute__ Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K220, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K220 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

__Origem dos dados__ à SAFX10

__\[MFS703404\] Inclusão da validação do TIPO\_ITEM do registro 0200 para o produto destino__

__Recuperação dos Dados__:

Serão recuperados todos os movimentos de *saída* no período que sejam redesignação \(movimentação interna entre produtos\), que atendam aos seguintes critérios:

\-Empresa = código da Empresa informante

\-Estabelecimento = código do Estabelecimento informante *\(ver OBS 1 e OBS 2\)*

\-Movimento E/S        = 9  \(somente as saídas\)

\-Data do Movimento  = deve estar compreendida no período \(período do registro “pai” K100\)

\-Redesignação \(campo 51\) = “S”

Alteração da __MFS1993__: inclusão de filtro por tipo de produto:

\-Produto \(campos 11/12\) = serão considerados apenas os movimentos de redesignação cujo produto 

                                            de origem seja do tipo “00”, “01”, “02”, “03”, “04”, “05” e “10”, ou seja, 

                                            produtos em que o campo TIPO\_ITEM do registro 0200 = algum destes 

                                            valores;

\-Produto Origem/Destino \(campos 52/53\) = serão considerados apenas os movimentos de 

                                            redesignação cujo produto de origem seja do tipo “00”, “01”, “02”, “03”, “04”, 

                                           “05” e “10”, ou seja, produtos em que o campo TIPO\_ITEM do registro 0200 

                                           = algum destes valores;

A identificação do tipo do item considera a mesma regra do registro 0200, ou seja, verifica a parametrização do menu “*Parâmetros à Registro 0200 à Tipo do Item*”, e quando o produto não constar, verifica o campo “*39\-Classificação do Item*” da SAFX2013\.

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo 44\-Inscrição Estadual da SAFX10\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Obs: Os dados são recuperados a partir dos movimentos de saída, porque a quantidade a ser informada é a quantidade do produto de origem da redesignação \(de acordo com informações obtidas no desenvolvimento do RCPE\-MG, no site da Sefaz\-MG, opção “Perguntas & Respostas” da Cartilha da Resolução\)\.

__Agrupamento dos Dados__:

A chave do K220 é composta pelos campos: \[DT\_MOV \+ COD\_ITEM\_ORI \+ COD\_ITEM\_DEST\], e assim, só pode existir um registro por dia para um mesmo produto origem e destino\.

 

Por isso, os dados recuperados de acordo com os critérios descritos acima serão agrupados, e a quantidade totalizada\.

Critérios para o grupamento: 

\-Data do Movimento – campo “07\-Data do Movimento”

\-Produto Origem à campos “11\-Indicador do Produto” e 12\-Código do Produto”

\-Produto Destino à campos “52\-Indicador do Produto Orig/Dest” e “53\-Código do Produto Orig/Dest”  

\-campo a ser totalizado à campo “20\-Quantidade”

 \(Alteração da MFS13290 devido a inclusão do campo QTD\_DEST\)

\-valores a serem totalizados à Quantidade na unidade de medida do produto origem

                                                   e Quantidade na unidade de medida do produto destino

Essas duas quantidades se baseiam na quantidade do movimento \(campo “20\-Quantidade”\), sendo que:

A quantidade origem é a quantidade do movimento na unidade de medida do produto de origem;  

A quantidade destino é a quantidade do movimento na unidade de medida do produto de destino;  

*\(Originalmente o K220 tinha apenas o campo “05\-QTD”\. Este campo é gerado com a totalização da quantidade na unidade de medida do produto origem\. Quando o AC 48/17 criou o campo 06\-QTD\_DEST, a geração passou a totalizar também a quantidade do movimento na unidade de medida do produto destino\)*

__Será gerado um registro K220 para cada agrupamento descrito acima:__

O campo 05\-QTD__\_ORI__ será gravado com a totalização da quantidade de todos os movimentos grupados, mas considerando sempre a unidade de medida do cadastro do produto origem \(SAFX2013\), conforme explicado a seguir\. 

O campo __06\-QTD\_DEST__ será gravado com a totalização da quantidade de todos os movimentos grupados, mas considerando sempre a unidade de medida do cadastro do produto destino \(SAFX2013\), conforme explicado a seguir\. 

No caso em que a unidade de medida dos dois produtos \(origem e destino\) seja a mesma, a quantidade também será a mesma\.

	

__Sobre a conversão de medida da unidade do movimento p/a unidade do produto origem:__

A quantidade de origem informada neste registro no campo 05\-QTD\_ORI será sempre referente à unidade de medida do cadastro do produto origem \(SAFX2013\)\.

Nos casos em que a unidade de medida do movimento \(campo “33\-Unidade de Medida” da SAFX10\) for diferente da unidade informada no cadastro do produto origem \(campo “14\-Código de Medida” da SAFX2013\), será feita a conversão de medida para calcular a quantidade do movimento com base na unidade de medida do cadastro\.

Se ao efetuar a comparação entra as unidades \(X10 x X2013\) for verificado que algum dos campos envolvidos \(campo 33 da SAFX10 ou campo “14 da SAFX2013 *não* esta preenchido, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

*“Na geração do registro K220 é necessário o preenchimento dos campos “14\-Código de Medida” do           cadastro do produto \(SAFX2013\) e “33\-Unidade de Medida” do movimento \(SAFX10\), p/efeito de comparação de medidas entre SAFX10 x SAFX2013\. O movimento não será considerado na geração”*\. O log mostrará os dados de identificação do movimento, para que o usuário possa verificar o problema\.

Observações sobre a comparação das unidades de medida \(X10 x X2013\):

*   \- Este procedimento garante que as quantidades sejam expressas na unidade de cadastro do*

*     produto, como orienta o manual, e também que a totalização seja feita sempre considerando uma*

*     única unidade, para não haver inconsistências;*

*   \- A comparação das unidades é feita a partir dos campos referentes à  SAFX2007, porque as tabelas*

*     de conversão de medida do Mastersaf usam esta medida\. Já na geração do 0200 a medida utilizada*

*     é a do campo da unidade padrão \(SAFX2017\)\. Assim, a geração prevê que as duas unidades*

*     estejam preenchidas no cadastro, e naturalmente, que sejam sempre as mesmas\.*

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O movimento não será considerado na geração do registro K220\.”*

__Sobre a conversão de medida da unidade do movimento p/a unidade do produto destino:__

A quantidade de destino informada no campo 05\-QTD\_DEST será sempre referente à unidade de medida do cadastro do produto destino \(SAFX2013\)\.

Nos casos em que a unidade de medida do movimento \(campo “33\-Unidade de Medida” da SAFX10\) for diferente da unidade informada no cadastro do produto destino \(campo “14\-Código de Medida” da SAFX2013\), será feita a conversão de medida para calcular a quantidade do movimento com base na unidade de medida do cadastro\.

Demais regras sobre a conversão da quantidade do movimento para a unidade de medida do produto destino, são as mesmas descritas acima para converter para a unidade do produto origem, inclusive as críticas descritas sobre o preenchimento da unidade na SAFX2013 e as críticas sobre a existência dos fatores de conversão nas tabelas de conversão de medida\.

__Crítica sobre o preenchimento do produto de destino da redesignação:__

Todos os movimentos de redesignação devem ter a informação do produto de destino \(campos 52 e 53\) preenchido\. Quando não existir a informação, será gravada uma mensagem de erro no log, e o movimento *não* será considerado p/o K220:

*“O produto de destino \(campo 52/53\) não foi informado no movimento de estoque\. O registro K220 não será gerado para estes movimentos”\.*

\(na coluna do log que mostra a chave do registro, serão demonstrados os dados de identificação do movimento\)

__Informar Fator de Conversão entre as Unidade do Produto Origem x Produto Destino:__

*\(considerando a unidade registrada no Bloco 0, registro 0200\)*

Alteração da __MFS8332 \(CH24201\)__: Devido a erro no PVA, a geração passou a verificar se a unidade do produto de origem é a mesma do produto de destino:

__Se__ a unidade de medida do produto de origem for <> unidade de medida do produto de destino

        Neste caso será gerado o registro 0220 informando o fator de conversão da unidade do produto 

        de origem para a unidade do produto de destino\.

As unidades a serem comparadas são as unidades do cadastro dos produtos \(SAFX2013\), ou seja, a unidade que aparecerá no registro 0200 de cada um destes produtos\.

RNK220\-02

Campo DT\_MOV:

Data do movimento, conforme o agrupamento de dados descrito na __RNK220__\.

RNK220\-03

Campo COD\_ITEM\_ORI:

Produto de origem conforme o agrupamento de dados descrito na __RNK220__\.

Na gravação deste campo será utilizada a mesma regra definida para os demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo, será gravado no Bloco 0 \(registro 0200\)\.

RNK220\-04

Campo COD\_ITEM\_DEST:

Produto de destino conforme o agrupamento de dados descrito na __RNK220__\.

Na gravação deste campo será utilizada a mesma regra definida para os demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo, será gravado no Bloco 0 \(registro 0200\)\.

RNK220\-05

Campo QTD __QTD\_ORI__:

*\(este campo foi renomeado pelo Ato Cotepe 48/17, mas seu conteúdo se mantém inalterado\) *

Total da quantidade dos registros consolidados, considerando a unidade de medida do produto origem, conforme o grupamento definido na __RNK220__\. 

A quantidade informada neste campo considera a unidade de medida gravada no registro 0200 do produto origem, conforme as regras de conversão de medida definidas na regra __RNK220__\. 

RNK220\-06

Campo QTD\_DEST:

\(campo incuído pelo Ato Cotepe 48/17, alteração da __MFS13290__\) 

Total da quantidade dos registros consolidados, considerando a unidade de medida do produto destino, conforme o grupamento definido na __RNK220__\. 

A quantidade informada neste campo considera a unidade de medida gravada no registro 0200 do produto destino, conforme as regras de conversão de medida definidas na regra __RNK220__\. 

*\(quando as unidades de medida entre o produto origem e o produto destino forem as mesmas, esta quantidade será a mesma do campo QTD\_ORI\)*

__Registro K230 – Itens Produzidos__

<a id="_Hlk103169693"></a>RNK230

Neste registro são gravadas as informações sobre a produção efetuada durante o período de apuração em questão \(data inicial e final do registro K100\)\.

__\[MFS85920\] \[MFS97186\] Tratamento em atendimento ao layout versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K230 passa a ser __NÃO OBRIGATÓRIA __para o tipo de leiaute__ Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K230, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K230 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

   Se o parâmetro “Tipo de Leiaute” = “__Simplificado__” da tela Parâmetros > Dados Iniciais estiver 

__SELECIONADO E__ campo QTD\_ENC \(campo 06 do K230\) for __IGUAL__ a zero, verificar a seguinte situação:

Se o parâmetro “Gerar Registro K230 com quantidade IGUAL a zero“ da tela Parâmetros > Dados Iniciais estiver __MARCADO__, registro __DEVE SER GERADO__\.

 Se o parâmetro “Gerar Registro K230 com quantidade IGUAL a zero” da tela Parâmetros > Dados Iniciais estiver __DESMARCADO__, registro __NÃO__ __DEVE SER GERADO__\.

   Senão o registro deve ser gerado conforme regra já existente\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX108 – Ordens de Produção

Critérios para a recuperação dos dados na SAFX108:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e OBS 2\)*;

\-PERIODO\_REF   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-Produto \(campos 05/06\) = serão considerados apenas os registros cujo produto seja do tipo 

                                            “03\-Produto em Processo” ou “04\-Produto Acabado”, ou seja, produtos em

                                            que o campo TIPO\_ITEM do registro 0200 = __03 __ou__ 04__;

\-Tipo da Ordem de Produção/Serviço = 1 \(“Produção”\) ou nulo

Alteração da __MFS4992__: Para atender ao AC 7/2016 a SAFX108 passou a tratar três diferentes tipos de produção \(Produção, Desmontagem e Reprocessamento\)\. Para isso foi criado o campo “28\-Tipo da Ordem de Produção/Serviço”, e para o K230 serão consideradas apenas os registros com tipo = “1”\.

Alteração da __MFS1993__: a identificação do tipo do item passou a considerar a mesma regra do registro 0200, ou seja, verifica a parametrização do menu “*Parâmetros à Registro 0200 à Tipo do Item*”, e quando o produto não constar, verifica o campo “*39\-Classificação do Item*” da SAFX2013\.

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “19\-Inscrição Estadual\-AM” da SAFX108\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada ordem de produção recuperada da SAFX108 será gravado um registro K230, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\. 

Alteração da __MFS1993__: Quando o registro K230 for gravado com o parâmetro “*Não informar o número da ordem de produção no registro K230*” ativado, ou seja, sem a informação dos campos 02, 03 e 04 \(ordem de produção, e sua data inicial e final\), a chave do K230 passa a ser apenas o campo COD\_DOC\_OP, de acordo com o Guia Prático Vrs 2\.0\.16\. Desta forma, poderá ocorrer duplicidade do registro caso o usuário não siga as orientações de utilização do parâmetro \(a orientação nesse caso é carregar p/a SAFX108 apenas um registro por Período/Produto\)\. Caso ocorra a duplicidade, os registros serão gravados normalmente, mas no log será gravada a seguinte mensagem:

 “O registro K230 foi gerado em duplicidade para o produto\. Consultar help dos parâmetros do Bloco K no menu Dados Iniciais”

  

Será gravada apenas uma mensagem por cada caso de duplicidade, ou seja, uma mensagem para cada produto que tiver gerado registros duplicados\. O log mostrará também a identificação do produto em duplicidade\.

RNK230\-02

Campo DT\_INI\_OP:

Alteração da __MFS1993__: 

__Se__ parâmetro “*Não informar o número da ordem de produção no registro K230*” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

__Senão__  \(permanece a regra original de preenchimento, conforme descrito a seguir\)

     Este campo é preenchido com a data de início da OP \(campo “07\-Data de Início da OP” da

     SAFX108\)\.

RNK230\-03

Campo DT\_FIN\_OP:

Alteração da __MFS1993__: 

__Se__ parâmetro “*Não informar o número da ordem de produção no registro K230*” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

__Senão__  \(permanece a regra original de preenchimento, conforme descrito a seguir\)

     Este campo é preenchido com a data de conclusão da OP \(campo “08\-Data de Conclusão da OP” 

     da SAFX108\), da seguinte forma:

__     Se__  data de conclusão não preenchida 

           *ou* 

          data de conclusão > data final do periodo da geração \(DT\_FIN do K100\)  \(CH16394/15\)

           Neste caso o campo será gravado sem informação;

__      Senão__

           Neste caso o campo será preenchido normalmente com a data da conclusão da OP;

RNK230\-04

Campo COD\_DOC\_OP:

A geração deste campo depende de alguns parâmetros do menu “Dados Iniciais”, da seguinte forma:

__MFS1993__: passou a usar o parâmetro “*Não informar o número da ordem de produção”*

__MFS10054__: passou a usar o parâmetro “*Considerar o Cód\. Diferenciador no Cód Ordem de Produção*”

__Se__ parâmetro “*Não informar o número da ordem de produção no registro K230*” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

__Senão__  

     __Se__ conteúdo do campo “Cód\. Diferenciador de Produção” <>  ‘ ‘ \(um caracter branco\)

__          e           __

          parâmetro “*Considerar o Código Diferenciador no Código da Ordem de Produção*” = “S”

         O campo será preenchido com a concatenação do campo “04\-Código da Ordem de Produção” 

         com o campo “15\-Cód\. Diferenciador de Produção”, sem utilizar nenhum separador;

         Alteração da __MFS2159 \(ch 25797\)__: a concatenação deixou de utilizar o separador \(“\-“\) 

         Se ao concatenar os dois campos o conteúdo a ser gravado ultrapassar 30 posições \(limite do

         layout\), o registro da ordem de produção em questão será *desconsiderado*, e será gravada a

         seguinte mensagem no log da geração: *“O campo COD\_DOC\_OP ultrapassou o tamanho máximo*

*         permitido \(30 posições\)\. Verificar os parâmetros sobre a geração deste campo\. A ordem de*

*         produção não será considerada na geração do registro K230”\.*\(o log informará também os dados  

         para identificação da ordem de produção\)\. 

##### __     __Senão

        O campo será preenchido apenas com o conteúdo do campo “04\-Código da Ordem de Produção”;

RNK230\-05

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0 da seguinte forma:

\- No registro 0200 à Dados de cadastro do produto, conforme as regras do 0200;

\- No registro 0210 à Formulação padrão do produto, que é obtida a partir das tabelas SAFX16/17/18,

                                  de acordo com as regras descritas na __RN0210__\.

RNK230\-06

Campo QTD\_ENC:

Se o campo “10\-Quantidade Produzida” da SAFX108 = 0 ou nulo, será gravado zero \(|0|\), pois o campo QTD\_ENC é de preenchimento obrigatório\.

Caso contrário, será executado o procedimento descrito a seguir, que verifica a necessidade de efetuar ou não conversão de medida:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificada a igualdade entre as duas, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX108 \(campo 09\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K230/K235 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. A ordem de produção não será considerada na geração”\.*\(o log informará também os dados para identificação da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX108, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX108 se refere à SAFX2007 \(apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017\), mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD\_ENC será a própria quantidade da

      SAFX108; 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX108 para a SAFX2013, e a quantidade da

      SAFX108 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX108:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX108 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. A ordem de produção não será considerada na geração do registro K230\.”*

__Registro K235 – Insumos Consumidos__

<a id="_Hlk523154107"></a>RNK235

<a id="_Hlk523147785"></a>Este registro é “filho” do K230, e demonstra os insumos utilizados no processo produtivo\. Para cada ordem de produção gravada no registro K230, serão gravados no K235 os seus insumos relacionados\. 

__Origem dos Dados: __

SAFX109 – Itens das Ordens de Produção

__Critérios para a recuperação dos dados na SAFX109__:

	

A recuperação dos itens de cada ordem de produção gravada no K230 é feita a partir dos dados chave que identificam a ordem de produção:

\- COD\_EMPRESA  

\- COD\_ESTAB      

\- PERIODO\_REF

\- COD\_OP

\- COD\_DIF\_PRODUCAO

\- IDENT\_PRODUTO\_OP

\[MFS23846\]

Somente devem ser recuperados os itens da ordem de produção que:

\-Produto \(campos 06/07\) = serão considerados apenas os registros cujo produto seja do tipo “00 – Mercadoria para Revenda”, “01 – Matéria\-prima”,  “02 – Embalagem”, “03\-Produto em Processo”, “04\-Produto Acabado”, “05 – Subproduto” ou “10 – Outros insumos” ou seja, produtos em que o campo TIPO\_ITEM do registro 0200 = 00 ou 01 ou 02 ou 03 ou 04 ou 05 ou 10;

__\[MFS85920\] \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K235 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K235, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K210 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

Caso o registro seja marcado para geração, deve seguir a seguinte regra:

O agrupamento deve ser feito conforme a regra abaixo:

\- A chave deste registro deve ser data da saída \(DT\_SAÍDA\) e insumo \(COD\_ITEM\)\.

\- Os itens recuperados da SAFX109 serão agrupados por:

\- Data da saída \(campos 08\-Data da Saída\)

\- Insumo/Componente \(campos 06\-Indicador e 07\-Produto Componente/Insumo\)

__Para o período de geração anterior a 01/01/2023:__

<a id="_Hlk523147506"></a>Os itens recuperados da SAFX109 serão agrupados por:

\- Data da saída \(campos 08\-Data da Saída\)

\- Insumo/Componente \(campos 06\-Indicador e 07\-Produto Componente/Insumo\)

\- Insumo Substituído \(campos 18\-Indicador e 19\-Código do Insumo Substituído\)              __\(MFS8933\)__

\(os campos do Insumo Substituído são campos *não obrigatórios* na SAFX109\)

__Alteração da MFS8933__: Conforme GP da vrs 2\.0\.20, a chave deste registro passou a ser data da saída, insumo, e insumo substituído \(quando existir\);

Para cada grupamento, será totalizada a quantidade do campo “10\-Quantidade Utilizada”, observando as regras sobre conversão de medida descritas na __RNK235\-04__\.  

Observar que a chave do K235 = data saída \+ produto \+ insumo substituído, por isso, é necessária a consolidação\.

Sobre o campo “05\-COD\_INS\_SUBST” observar a __RNK235\-05__\.

 Para o resultado de cada consolidação, será gravado um registro K235, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\. 

__Procedimento quando não existirem dados na SAFX109 para a produção gravada no K230:__

\(regra criada pela __MFS2413, Chamado 25930/15__\)

\(regra alterada pela __MFS26934 – MFS28094__\)

__Se__ parâmetro “*Não informar o número da ordem de produção no registro K230*” = “S”

      Neste caso o registro da produção K230 *não* será gravado *\(procedimento já adotado antes da*

*      MFS2413\)*, e será gravada a seguinte msg de erro no log da geração: *“Quando a geração do registro*

*      K230 é realizada sem a informação do número da ordem de produção, é obrigatório informar os*

*      insumos consumidos \(SAFX109\)”\.  *O log informará os dados necessários para identificação do

      registro da SAFX108 em questão\. *Obs: o validador critica a falta do K235 quando os campos 02, 03*

*      e 04 não são informados no K230, exatamente o que acontece quando este parâmetro é ativado\.* 

__Senão__

__      Se__ OP iniciada no mês da geração \(data início da OP da SAFX108\) e estiver concluída no mês da geração \(data conclusão da OP da SAFX108\)

           Neste caso o registro da produção K230 *não* será, e será gravada a seguinte mensagem de erro 

           no log da geração: *“Para as Ordens de Produção \(SAFX108\) iniciadas e concluídas no período, *

*           é obrigatório informar os insumos consumidos \(SAFX109\)”\.  *O log informará os dados 

           necessários para identificação do registro da SAFX108 em questão\.

__      Senão__

           Neste caso o registro K230 *será gravado normalmente*, e não existirão os registros “filhos” 

           K235;

           

RNK235\-03

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0, registro 0200\.

RNK235\-04

Campo QTD:

Se o campo “10\-Quantidade Utilizada” da SAFX109 = 0 ou nulo, será gravado zero \(|0|\), pois o campo QTD é de preenchimento obrigatório\.

Caso contrário, será executado o procedimento descrito a seguir, que verifica a necessidade de efetuar ou não conversão de medida:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificada a igualdade entre as duas, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX109 \(campo 09\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro do item da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K230/K235 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O item da ordem de produção não será considerado na geração”\.*\(o log informará também os dados para identificação do item da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX109, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX109 se refere à SAFX2007 \(apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017\), mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD será a própria quantidade da SAFX109; 

     * \(ou conteúdo a ser totalizado, quando se tratar de uma consolidação dos itens da SAFX109,*

*      conforme descrito na *__*RNK235*__*\)  *

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX109 para a SAFX2013, e a quantidade da

      SAFX109 será ajustada para esta nova medida \(seguindo o mesmo exemplo da RNK230\-06\)\.

      O conteúdo a ser gravado será a quantidade já ajustada \(*ou conteúdo a ser totalizado, quando se*

*      tratar de uma consolidação dos registros da SAFX109, conforme descrito na *__*RNK235*__*\)  *

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item da ordem de produção não será considerado na geração do registro K235\.”*

RNK235\-05

Campo COD\_INS\_SUBST:

__Para período de geração até 31/12/2021:__

__= = = = = MFS8933__

O layout solicita a informação do insumo substituído \(campos 18 e 19 da SAFX109\) no campo 05\-COD\_INS\_SUBST, mas *não* prevê que um mesmo insumo possa dar saída do estoque numa mesma data, mas para ser utilizado em substituição a insumos diferentes\. Trata\-se de uma situação incomum, mas poderia acontecer\. Mas como a chave do K235 *não* prevê este cenário, o insumo substituído será tratado da seguinte forma:

\- Caso a informação exista na SAFX109 \(campos 18 e 19\) e seja igual em todos os registros de uma 

  mesma consolidação à neste caso a informação será gravada no arquivo com o conteúdo existente;

\- Caso a informação exista na SAFX109 \(campos 18 e 19\), mas com conteúdo diferente entre os 

  registros de uma mesma consolidação à neste caso o campo será gerado sem informação;

__Alteração da MFS8933__: Conforme GP da vrs 2\.0\.20, a chave deste registro passou a ser data da saída, insumo, e insumo substituído \(quando existir\)\. Por isso, a consolidação dos itens da SAFX109 passou a considerar o insumo substituído \(conforme __RNK235__\)\. Com esta alteração, o problema descrito acima não ocorrerá mais, e as regras de geração que foram tachadas não serão mais necessárias\.

__= = = = = MFS8933__

Este campo será gerado com a informação do insumo substituído \(campos 18\-Indicador e 19\-Código do Insumo Substituído\), quando existir a informação, Caso contrário, será gerado sem preenchimento \(“||”\)\.

Sobre o preenchimento do campo \(quando for o caso\):

 

O preenchimento deste campo segue a mesma regra de preenchimento do campo COD\_ITEM, dependendo do parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0, registro 0200\.

__\[ALTERAÇÃO – MFS74583\] Tratamento em atendimento ao layout  versão 1\.15 \(Janeiro/2022\)__

__Para período de geração a partir de 01/01/2022:__

O campo não deve ser gerado\. 

    

__Registro K250 – Industrialização Efetuada p/Terceiros \- Itens Produzidos__

RNK250

Neste registro são gravadas as informações sobre a produção efetuada por terceiros durante o período de apuração em questão \(data inicial e final do registro K100\)\.

__\[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K250 passa a ser __NÃO OBRIGATÓRIA __para o tipo de leiaute__ Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K250, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K250 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

__Origem dos Dados: __

SAFX153 – Produção de Terceiros

__Critérios para a recuperação dos dados na SAFX153:__

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e OBS 2\)*;

\-DAT\_PRODUCAO = deve estar compreendida entre a data inicial e final do período \(registro K100\)

\-Produto \(campos 04/05\) = serão considerados apenas os registros cujo produto seja do tipo 

                                            “03\-Produto em Processo” ou “04\-Produto Acabado”, ou seja, produtos em

                                            que o campo TIPO\_ITEM do registro 0200 = __03 __ou__ 04__;

Alteração da __MFS1993__: a identificação do tipo do item passou a considerar a mesma regra do registro 0200, ou seja, verifica a parametrização do menu “*Parâmetros à Registro 0200 à Tipo do Item*”, e quando o produto não constar, verifica o campo “*39\-Classificação do Item*” da SAFX2013\.

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “19\-Inscrição Estadual\-AM” da SAFX108\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada registro de produção recuperado da SAFX153 será gravado um registro K250, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\. 

*\(observar que a chave da SAFX153 é exatamente a chave descrita p/o registro K250 no Guia Prático, que é: data da produção \+ produto\)*

RNK250\-03

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0 da seguinte forma:

\- No registro 0200 à Dados de cadastro do produto, conforme as regras do 0200;

\- No registro 0210 à Formulação padrão do produto, que é obtida a partir das tabelas SAFX16/17/18,

                                  de acordo com as regras descritas na __RN0210__\.

RNK250\-04

Campo QTD:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificada a igualdade entre as duas, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX153 \(campo 07\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K250/K255 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O registro da produção de terceiros não será considerada na geração”\.*\(o log informará também os dados para identificação do registro da SAFX153\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX153, pois é campo obrigatório\)*

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD será a própria quantidade da SAFX153;

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX153 para a SAFX2013, e a quantidade da

      SAFX153 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX153:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX153 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O registro da produção de terceiros  não será considerado na geração do registro K250\.”*

__Registro K255 – Industrialização Efetuada p/Terceiros \- Insumos Consumidos__

<a id="_Hlk103175011"></a>RNK255

Este registro é “filho” do K250, e demonstra os insumos utilizados no processo produtivo\. Para cada registro de produção gravado no registro K250, serão gravados no K255 os seus insumos relacionados\. 

__\[MFS703457\] Inclusão da validação do TIPO\_ITEM do registro 0200 para o insumo__

__Origem dos Dados: __

SAFX154 – Insumos Consumidos \(Produção de Terceiros\)

__Critérios para a recuperação dos dados na SAFX154__:

	

Para cada registro de produção gravado no K250, serão recuperados todos os seus insumos na SAFX154\. A recuperação destes itens \(insumos\) é feita a partir dos dados chave que relacionam as duas tabelas:

\- COD\_EMPRESA  

\- COD\_ESTAB      

\- DAT\_PRODUCAO

\- IDENT\_PRODUTO

\[__MFS85920\] \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K255 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K255, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K255 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

Caso o registro seja marcado para geração no leiaute Simplificado, deve seguir a seguinte regra: 

O agrupamento deve ser feito conforme a regra abaixo:

\- A chave deste registro deve ser a data do consumo \(DT\_CONS\) e insumo \(COD\_ITEM\);

\- Os itens recuperados da SAFX154 serão agrupados por:

\- Data da saída \(campos 06\-Data do Consumo\)

\- Insumo \(campos 07\-Indicador do Insumo e 08\-Código do Insumo\)

__Para o período de geração anterior a 01/01/2023:__

Os itens recuperados da SAFX154 serão agrupados por:

\- Data do consumo \(campos 06\-Data do Consumo\)

\- Insumo \(campos 07\-Indicador do Insumo e 08\-Código do Insumo\) = serão considerados apenas    

              os insumos consumidos cujo produto de origem seja do tipo “00”, “01”, “02”, “03”, “04”,“05” 

              e “10”, ou seja, produtos em que o campo TIPO\_ITEM do registro 0200 = algum destes        

              valores;

\- Insumo Substituído \(campos 12\-Indicador e 13\-Código do Insumo Substituído\)              __\(MFS8933\)__

\(os campos do Insumo Substituído são campos *não obrigatórios* na SAFX154\)

   

__Alteração da MFS8933__: Conforme GP da vrs 2\.0\.20, a chave deste registro passou a ser data do consumo, insumo, e insumo substituído \(quando existir\);

Observar que a chave do K255 = data consumo \+ insumo \+ insumo substituído, por isso, é necessária a consolidação\.

Para cada grupamento, será totalizada a quantidade do campo “10\-Quantidade”, observando as regras sobre conversão de medida descritas na __RNK255\-04__\.  

Sobre o campo “05\-COD\_INS\_SUBST”, observar a __RNK255\-05__\.

Para o resultado de cada consolidação, será gravado um registro K255, conforme os dados descritos na planilha DEPARA, e nas regras especificas de cada campo, quando for o caso\.\. 

RNK255\-03

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0, registro 0200\.

RNK255\-04

Campo QTD:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificada a igualdade entre as duas, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX154 \(campo 11\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da SAFX154 será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K250/K255 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. Este insumo da produção de terceiros não será considerado na geração”\.*\(o log informará também os dados para identificação do registro da produção de terceiro e o insumo em questão\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX154, pois é campo obrigatório\)*

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD será a própria quantidade da SAFX154; 

     * \(ou conteúdo a ser totalizado, quando se tratar de uma consolidação dos itens da SAFX154,*

*      conforme descrito na *__*RNK255*__*\)  *

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX154 para a SAFX2013, e a quantidade da

      SAFX154 será ajustada para esta nova medida \(seguindo o mesmo exemplo da __RNK250\-04__\)\.

      O conteúdo a ser gravado será a quantidade já ajustada \(*ou conteúdo a ser totalizado, quando se*

*      tratar de uma consolidação dos registros da SAFX154, conforme descrito na *__*RNK255*__*\)  *

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O insumo da produção de terceiros não será considerado na geração do registro K255\.”*

RNK255\-05

Campo COD\_INS\_SUBST:

__Para período de geração até 31/12/2021:__

__= = = = = MFS8933__

O layout solicita a informação do insumo substituído \(campos 12 e 13 da SAFX154\) no campo 05\-COD\_INS\_SUBST, mas *não* prevê que um mesmo insumo possa ser consumido numa mesma data, mas para ser utilizado em substituição a insumos diferentes\. Trata\-se de uma situação incomum, mas poderia acontecer\. Mas como a chave do K255 *não* prevê este cenário, o insumo substituído será tratado da seguinte forma:

\- Caso a informação exista na SAFX154 \(campos 12\-Indicador e 13\-Código do Insumo Substituído\) e

  seja igual em todos os registros de uma mesma consolidação à neste caso a informação será

  gravada no arquivo com o conteúdo existente;

\- Caso a informação exista na SAFX154 \(campos 12\-Indicador e 13\-Código do Insumo Substituído\),   

  mas com conteúdo diferente entre os registros de uma mesma consolidação à neste caso o campo

  será gerado sem informação;

__Alteração da MFS8933__: Conforme GP da vrs 2\.0\.20, a chave deste registro passou a ser data do consumo, insumo, e insumo substituído \(quando existir\)\. Por isso, a consolidação dos itens da SAFX154 passou a considerar o insumo substituído \(conforme __RNK255__\)\. Com esta alteração, o problema descrito acima *não* ocorrerá mais, e as regras de geração que foram tachadas não serão mais necessárias\.

__= = = = = MFS8933__

Este campo será gerado com a informação do insumo substituído \(campos 12\-Indicador e 13\-Código do Insumo Substituído\), quando existir a informação, Caso contrário, será gerado sem preenchimento \(“||”\)\.

Sobre o preenchimento do campo \(quando for o caso\):

 

O preenchimento deste campo segue a mesma regra de preenchimento do campo COD\_ITEM, dependendo do parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0, registro 0200\.

__\[ALTERAÇÃO – MFS74583\] Tratamento em atendimento ao layout  versão 1\.15 \(Janeiro/2022\)__

__Para período de geração a partir de 01/01/2022:__

O campo não deve ser gerado\. 

__Registro K260 – Reprocessamento / Reparo de Produtos__

<a id="_Hlk103170386"></a>RNK260

Este registro foi criado pelo Ato Cotepe 7/2016, e implementado na __MFS4992__ \(Jun/2016\)\.

 

Neste registro são gravadas as informações sobre os processos de REPROCESSAMENTO/REPARO efetuados durante o período de apuração em questão \(data inicial e final do registro K100\)\.

__\[MFS85920\] \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K260 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K260, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K260 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX108 – Ordens de Produção

Critérios para a recuperação dos dados na SAFX108:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e OBS 2\)*;

\-PERIODO\_REF   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-Tipo da Ordem de Produção/Serviço = __3__ \(“Reprocessamento / Reparo”\)

No Guia Prático da vrs 1\.0\.19 não existe restrição sobre os tipos de produto a serem considerados, por isso, não haverá filtro sobre o tipo do item\.

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “19\-Inscrição Estadual\-AM” da SAFX108\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada ordem de produção recuperada da SAFX108 será gravado um registro K260, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\. 

__\[MFS31413\] Inclusão do campo DT\_RET na chave do registro__

Sobre o número da ordem de produção: Quando o registro K260 for gravado com o parâmetro “*Não informar o número da ordem de produção \(SAFX108\)*” ativado, ou seja, sem a informação do campo 02 \(ordem de produção\), a chave do K260 passa a ser os campos COD\_ITEM \+ DT\_RET, de acordo com o Guia Prático Vrs 3\.0\.2\. Desta forma, poderá ocorrer duplicidade do registro caso o usuário não siga as orientações de utilização do parâmetro \(a orientação nesse caso é carregar p/a SAFX108 apenas um registro por Período/Produto\)\. Caso ocorra a duplicidade, os registros serão gravados normalmente, mas no log será gravada a seguinte mensagem:

* “O registro K260 foi gerado em duplicidade para o produto\.Consultar help dos parâmetros do Bloco K no menu Dados Iniciais”*

  

Será gravada apenas uma mensagem por cada caso de duplicidade, ou seja, uma mensagem para cada produto que tiver gerado registros duplicados\. O log mostrará também a identificação do produto em duplicidade\.

RNK260\-02

Campo COD\_OP\_OS:

\(__MFS10054__: passou a usar o parâmetro “*Considerar o Cód\. Diferenciador no Cód Ordem de Produção*”\)

A geração deste campo depende de alguns parâmetros do menu “Dados Iniciais”, da seguinte forma:

__Se__ parâmetro “*Não informar o número da ordem de produção no registro *__*K260*__” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

__Senão__  

     __Se__ conteúdo do campo “Cód\. Diferenciador de Produção” <>  ‘ ‘ \(um caracter branco\)

__           e           __

           parâmetro “*Considerar o Código Diferenciador no Código da Ordem de Produção*” = “S”

         O campo será preenchido com a concatenação do campo “04\-Código da Ordem de Produção” 

         com o campo “15\-Cód\. Diferenciador de Produção”, sem utilizar nenhum separador;

         \(conforme alteração  da __MFS2159 \(ch 25797\)__ a concatenação deixou de utilizar o separador\) 

         Se ao concatenar os dois campos o conteúdo a ser gravado ultrapassar 30 posições \(limite do

         layout\), o registro da ordem de produção em questão será *desconsiderado*, e será gravada a

         seguinte mensagem no log da geração: *“O campo COD\_OP\_OS ultrapassou o tamanho máximo*

*         permitido \(30 posições\)\. Verificar os parâmetros sobre a geração deste campo\. A ordem de*

*         produção não será considerada na geração do registro K260”\.*\(o log informará também os dados  

         para identificação da ordem de produção\)\. 

##### __     __Senão

        O campo será preenchido apenas com o conteúdo do campo “04\-Código da Ordem de Produção”;

RNK260\-03

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à concatenação do Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no registro 0200 do Bloco 0\.

RNK260\-05

Campo QTD\_SAIDA:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX108 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX108 \(campo 09\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K260/K265 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. A ordem de produção não será considerada na geração”\.*\(o log informará também os dados para identificação da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX108, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX108 se refere à SAFX2007 \(apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017\), mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD\_SAIDA será a própria quantidade de saída da

      SAFX108 \(campo *31\-Quantidade da Saída*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX108 para a SAFX2013, e a quantidade da

      SAFX108 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX108:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX108 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. A ordem de produção não será considerada na geração do registro K260\.”*

RNK260\-07

Campo QDT\_RET:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX108 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

O procedimento para conversão de unidade é o mesmo descrito para o campo 05\-QTD\_SAIDA, mas, obviamente, o campo a ser considerado aqui é o campo “*33\-Quantidade do Retorno*”\.

__Registro K265 – Reprocessamento/Reparo \- Mercadorias Consumidas ou Retornadas__

<a id="_Hlk103170544"></a><a id="_Hlk523154259"></a>RNK265

Este registro foi criado pelo Ato Cotepe 7/2016, e implementado na __MFS4992__ \(Jun/2016\)\.

 

Este registro é “filho” do K260, e demonstra os insumos consumidos ou  retornados ao estoque durante o processo de reprocessamento/reparo\. Para cada registro “pai” gravado no registro K260, serão gravados no K265 todos os insumos relacionados\. 

__\[MFS85920\] \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K265 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K265, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K265 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

__Origem dos Dados: __

SAFX109 – Itens das Ordens de Produção

__Critérios para a recuperação dos dados na SAFX109__:

	

A recuperação dos itens de cada ordem de produção/serviço gravada no K260 é feita a partir dos dados chave que identificam a ordem de produção/serviço:

\- COD\_EMPRESA  

\- COD\_ESTAB      

\- PERIODO\_REF

\- COD\_OP

\- COD\_DIF\_PRODUCAO

\- IDENT\_PRODUTO\_OP

Para cada item de produção recuperado da SAFX109, será gravado um registro K265, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\.

RNK265\-02

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à concatenação do Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no registro 0200 do Bloco 0\.

RNK265\-03

Campo QTD\_CONS:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX108 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX108 \(campo 09\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K260/K265 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O item da ordem de produção não será considerada na geração”\.*\(o log informará também os dados para identificação da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX108, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX108 se refere à SAFX2007 \(apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017\), mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD\_CONS será a própria quantidade informada na

      SAFX108 \(campo *29\-Quantidade Utilizada \- Reprocessamento*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX108 para a SAFX2013, e a quantidade da

      SAFX108 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX108:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX108 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item da ordem de produção não será considerada na geração do registro K265\.”*

RNK265\-04

Campo QDT\_RET:

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto    \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX108 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

O procedimento para conversão de unidade é o mesmo descrito para o campo 03\-QTD\_CONS, mas, obviamente, o campo a ser considerado aqui é o campo “*30\-Quantidade Retornada*”\.

__Registro K270 – Correção de Apontamento Registros K210, K220, K230, K250, K260, K291, K292, K301 e K302__

RNK270

Este registro foi criado pelo Ato Cotepe 7/2016, e implementado na __MFS4993__ \(Jun/2016\)\.

__MFS\-20988:__ Inclui as origens 6, 7, 8 e 9, referentes aos registros K291, K292, K301 e K302, em atendimento ao Ato COTEPE 48/2017\.

 

Neste registro são gravadas as informações sobre as correções de erros de apontamento de períodos anteriores, originados dos registros K210, K220, K230, K250 ou K260\.

__\[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K270 passa a ser __NÃO OBRIGATÓRIA __para o tipo de leiaute__ Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K270, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K270 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

 

Origem dos Dados: 

SAFX235 – Tabela de Correções de Apontamento

Critérios para a recuperação dos dados na SAFX235:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e OBS 2\)*;

\-PERIODO\_REF   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-TIPO DA CORREÇÃO = __2, 3, 4, 5, 6, 7, 8, 9 e 10__; 

\[__MFS24090__\]

Somente devem ser recuperados os produtos da correção de apontamento que:

\-Produto \(campos 05/06\) = serão considerados apenas os registros cujo produto seja do tipo “00 – Mercadoria para Revenda”, “01 – Matéria\-prima”,  “02 – Embalagem”, “03\-Produto em Processo”, “04\-Produto Acabado”, “05 – Subproduto” ou “10 – Outros insumos” ou seja, produtos em que o campo TIPO\_ITEM do registro 0200 = 00 ou 01 ou 02 ou 03 ou 04 ou 05 ou 10;

Para este registro são considerados todos os tipos de correção da SAFX235, exceto as correções de estoque escriturado \(K200\), onde o Tipo da Correção é = __1__ \(estas correções são lançadas no K280\)\.

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das correções de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “18\-Inscrição Estadual\-AM” da SAFX235\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada correção de apontamento recuperada da SAFX235 será gravado um registro K270, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\. 

Sobre o número da ordem de produção: Para os registros de correção de apontamento \(K270 e K280\) não existe o parâmetro “*Não informar o número da ordem de produção*”\. O motivo é que na tabela SAFX235 não é obrigatório o preenchimento do campo da ordem de produção\. Assim, quando a empresa não trabalham com ordens de produção, o usuário poderá carregar os dados da SAFX235 sem preencher este campo\.

RNK270\-04

Campo COD\_OP\_OS:

\(__MFS10054__: passou a usar o parâmetro “*Considerar o Cód\. Diferenciador no Cód Ordem de Produção*”\)

Na SAFX235 o código da ordem de produção /serviço *não* é obrigatório, portanto, quando o campo “*09\-Código da Ordem de Produção/Serviço*” não estiver preenchido, o campo COD\_OP\_OS será gerado sem informação\.

Caso contrário:

__Se__ conteúdo do campo “10\-Cód\. Diferenciador de Produção” <>  ‘ ‘ \(um caracter branco\)

__      e           __

      parâmetro “*Considerar o Código Diferenciador no Código da Ordem de Produção*” = “S”

      O campo será preenchido c/a concatenação do campo “09\-Código da Ordem de Produção/Serviço” 

      com o campo “10\-Cód\. Diferenciador de Produção”, sem utilizar nenhum separador;

      \(conforme alteração da __MFS2159 \(ch 25797\)__ a concatenação deixou de utilizar o separador\) 

      Se ao concatenar os dois campos o conteúdo a ser gravado ultrapassar 30 posições \(limite do

      layout\), o registro da ordem de produção em questão será *desconsiderado*, e será gravada a

      seguinte mensagem no log da geração: *“O campo COD\_OP­\_OS ultrapassou o tamanho máximo*

*      permitido \(30 posições\)\. Verificar os parâmetros sobre a geração deste campo\. A ordem de*

*      produção não será considerada na geração do registro K270”\.*\(o log informará também os dados  

      para identificação da ordem de produção\)\. 

##### Senão

   O campo será preenchido apenas c/o conteúdo do campo “09\-Código da Ordem de Produção/Serviço”;

RNK270\-05

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à concatenação do Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no registro 0200 do Bloco 0\.

RNK270\-06 e 

RNK270\-07

Campos QTD\_COR\_POS e QTD\_COR\_NEG:

Estes campos serão preenchidos a partir do campo “*17\-Correção Positiva/Negativa*”, que indica se a correção é positiva ou negativa, da seguinte forma: 

Se campo “16\-Quantidade da Correção” = zeros ou nulo

     Os dois campos, QTD\_COR\_POS e QTD\_COR\_NEG serão gerados sem informação \(“||”\); 

Senão

     Se campo “17\-Correção Positiva/Negativa” = 1

         O campo QTD\_COR\_POS será preenchido com o valor do campo “16\-Quantidade da Correção”;

         O campo QTD\_COR\_NEG será gerado sem informação; 

     Senão

         O campo QTD\_COR\_POS será gerado sem informação;

         O campo QTD\_COR\_NEG será preenchido com o valor do campo “16\-Quantidade da Correção”;

A quantidade a ser informada neste campo deve ser referente a unidade de medida do cadastro do produto \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX235 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX235 \(campo 15\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da correção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K270/K275 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. A correção de apontamento não será considerada na geração”\.*\(o log informará também os dados para identificação da correção de apontamento em questão\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX235, pois é campo obrigatório\)*

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD\_COR\_POS ou QTD\_COR\_NEG \(conforme a 

     regra descrita acima\) será o próprio conteúdo do campo *16\-Quantidade da Correção*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX235 para a SAFX2013, e a quantidade da

      SAFX235 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX235:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX235 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. A correção de apontamento não será considerada na geração do registro K270\.”*

RNK270\-08

Campo ORIGEM:

__MFS\-20988:__ Inclui as origens 6, 7, 8 e 9, referentes aos registros K291, K292, K301 e K302, em atendimento ao Ato COTEPE 48/2017\.

Este campo será gerado a partir do campo “04\-Tipo da Correção”, fazendo o seguinte de\-para entre o tipo da correção da SAFX235 e o campo ORIGEM do Sped:

__Tipo da Correção da SAFX235__

__Campo ORIGEM__

2\- Correção de apontamento de Desmontagem \(K210/K215\)

3

3\- Correção de apontamento de Movimentação Interna \(K220\)

5

4\- Correção de apontamento de Produção Própria \(K230/K235\)

1

5\- Correção de apontamento de Produção de Terceiros \(K250/K255\)

2

6\- Correção de apontamento de Reprocessamento/Reparo \(K260/K265\)

4

7\- Correção de apontamento de Produção Conjunta \- Itens Produzidos \(K291\)

6

8\- Correção de apontamento de Produção Conjunta \- Insumos Consumidos \(K292\)

7

9\- Correção de apontamento de Produção Conjunta Ind\. por Terceiros \- Itens Produzidos \(K301\)

8

10\- Correção de apontamento de Produção Conjunta Ind\. por Terceiros \- Insumos Consumidos \(K302\)

9

\(lembrando que para este registro as correções do tipo “1” *não* são recuperadas\)

__Registro K275 \- Correção de Apontamento \- Insumos \(K215, K220, K235, K255 e K265\)__

<a id="_Hlk103170696"></a>RNK275

Este registro foi criado pelo Ato Cotepe 7/2016, e implementado na __MFS4993__ \(Jun/2016\)\.

 

__MFS\-20988:__ Inclui as origens 6, 7, 8 e 9, referentes aos registros K291, K292, K301 e K302, em atendimento ao Ato COTEPE 48/2017\.

Este registro é “filho” do K270, e demonstra os componentes/insumos corrigidos, ou, o produto de destino do movimento de redesignação, quando se tratar de correção de apontamento de movimentação interna \(correção do K220\)\. 

Para cada registro “pai” gravado no registro K270, serão gravados no K275 todos os insumos relacionados\. 

__\[MFS85920\] \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K275 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K275, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K275 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

__Origem dos Dados: __

SAFX236 – Tabela de Itens das Correções de Apontamento

__Critérios para a recuperação dos dados na SAFX236__:

\[__MFS24090__\]

Somente devem ser recuperados os produtos \(Componente/Insumo\) dos itens das correções de apontamento que:

\-Produto  \(Componente/Insumo\- campos 15/16\) = serão considerados apenas os registros cujo produto seja do tipo “00 – Mercadoria para Revenda”, “01 – Matéria\-prima”,  “02 – Embalagem”, “03\-Produto em Processo”, “04\-Produto Acabado”, “05 – Subproduto” ou “10 – Outros insumos” ou seja, produtos em que o campo TIPO\_ITEM do registro 0200 = 00 ou 01 ou 02 ou 03 ou 04 ou 05 ou 10;

	

A recuperação dos itens de cada correção de apontamento gravada no K270 é feita a partir dos dados chave que identificam as correções do tipo 2, 3, 4, 5, 6, 7, 8, 9 e 10:

*\(observar que para estes tipos de correção, os demais campos 11, 12, 13 e 14, que também compõem a chave da tabela “mãe” SAFX235, não são utilizados, e estarão preenchidos com zeros ou branco\)*

\- COD\_EMPRESA

\- COD\_ESTAB

\- PERIODO\_REF

\- TIPO DA CORREÇÃO 

\- Indicador do Produto

\- Código do Produto

\- Data Inicial do Período de Apuração

\- Data Final do Período de Apuração

\- Código da Ordem de Produção/Serviço

\- Cód\. Diferenciador de Produção

Para cada item de correção recuperados da SAFX236, será gravado um registro K275, conforme os dados descritos na planilha DEPARA, e nas regras especificas de cada campo, quando for o caso\.

 

RNK275\-02

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à concatenação do Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no registro 0200 do Bloco 0\.

RNK275\-03 e 

RNK275\-04

Campos QTD\_COR\_POS e QTD\_COR\_NEG:

Estes campos serão preenchidos a partir do campo “*19\-Correção Positiva/Negativa*”, que indica se a correção é positiva ou negativa, da seguinte forma: 

Se campo “18\-Quantidade da Correção” = zeros ou nulo

     Os dois campos, QTD\_COR\_POS e QTD\_COR\_NEG serão gerados sem informação \(“||”\); 

Senão

     Se campo “19\-Correção Positiva/Negativa” = 1

         O campo QTD\_COR\_POS será preenchido com o valor do campo “18\-Quantidade da Correção”;

         O campo QTD\_COR\_NEG será gerado sem informação; 

     Senão

         O campo QTD\_COR\_POS será gerado sem informação;

         O campo QTD\_COR\_NEG será preenchido com o valor do campo “18\-Quantidade da Correção”;

A quantidade a ser informada neste campo deve ser referente a unidade de medida do cadastro do produto \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX236 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX236 \(campo 17\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da correção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K270/K275 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O item da correção de apontamento não será considerada na geração”\.*\(o log informará também os dados para identificação do item da correção de apontamento em questão\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX236, pois é campo obrigatório\)*

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD\_COR\_POS ou QTD\_COR\_NEG \(conforme a 

     regra descrita acima\) será o próprio conteúdo do campo *18\-Quantidade da Correção*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX236 para a SAFX2013, e a quantidade da

      SAFX236 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX236:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX236 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item da correção de apontamento não será considerada na geração do registro K275\.”*

RNK275\-05

Campo COD\_INS\_SUBST:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

   \- Parâmetro marcado à concatenação dos campos 20 e 21 \(Indicador e Código do Insumo

                                          Substituído\);

   \- Parâmetro desmarcado à o campo será gerado apenas com a informação do campo 21 \(Código do

                                                 Insumo Substituído\);

O produto informado neste campo será gravado no registro 0200 do Bloco 0\.

__Registro K280 – Correção de Apontamento de Estoque Escriturado \(K200\)__

RNK280

Este registro foi criado pelo Ato Cotepe 7/2016, e implementado na __MFS4993__ \(Jun/2016\)\.

 

Neste registro são gravadas as informações sobre as correções de erros de apontamento de períodos anteriores, originado do registro K200 \(Estoque Escriturado\)\.

 

Origem dos Dados: 

SAFX235 – Tabela de Correções de Apontamento

Critérios para a recuperação dos dados na SAFX235:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e OBS 2\)*;

\-PERIODO\_REF   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-TIPO DA CORREÇÃO = __1__; 

Para este registro são consideradas apenas as correções do tipo “__1__” \(correção de estoque escriturado\)\.

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das correções de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “18\-Inscrição Estadual\-AM” da SAFX235\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada correção de apontamento recuperada da SAFX235 será gravado um registro K280, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\. 

RNK280\-03

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à concatenação do Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no registro 0200 do Bloco 0\.

__\[ALTERADO CH3814/2017\]__

No entanto, deverá ser verificado se o tipo do item é igual a 00, 01, 02, 03, 04, 05, 06 ou 10 \(campo TIPO\_ITEM do Registro 0200\), caso contrário, será gravada uma mensagem de erro no log, e o item *não* será considerado p/o K280:

*“O tipo do Item é diferente dos valores permitidos:* *00, 01, 02, 03, 04, 05, 06 e 10  \(campo TIPO\_ITEM do Registro 0200\) para o registro K280\. O registro K280 não será gerado para esse tipo do Item”\.*

\(na coluna do log que mostra a chave do registro, serão demonstrados os dados de identificação do item\)

RNK280\-04 e 

RNK280\-05

Campos QTD\_COR\_POS e QTD\_COR\_NEG:

Estes campos serão preenchidos a partir do campo “*17\-Correção Positiva/Negativa*”, que indica se a correção é positiva ou negativa, da seguinte forma: 

Se campo “16\-Quantidade da Correção” = zeros ou nulo

     Os dois campos, QTD\_COR\_POS e QTD\_COR\_NEG serão gerados sem informação \(“||”\); 

Senão

     Se campo “17\-Correção Positiva/Negativa” = 1

         O campo QTD\_COR\_POS será preenchido com o valor do campo “16\-Quantidade da Correção”;

         O campo QTD\_COR\_NEG será gerado sem informação; 

     Senão

         O campo QTD\_COR\_POS será gerado sem informação;

         O campo QTD\_COR\_NEG será preenchido com o valor do campo “16\-Quantidade da Correção”;

A quantidade a ser informada neste campo deve ser referente a unidade de medida do cadastro do produto \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX235 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX235 \(campo 15\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da correção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar o registro K280 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. A correção de apontamento não será considerada na geração”\.*\(o log informará também os dados para identificação da correção de apontamento em questão\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX235, pois é campo obrigatório\)*

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD\_COR\_POS ou QTD\_COR\_NEG \(conforme a 

     regra descrita acima\) será o próprio conteúdo do campo *16\-Quantidade da Correção*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX235 para a SAFX2013, e a quantidade da

      SAFX235 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX235:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX235 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. A correção de apontamento não será considerada na geração do registro K280\.”*

RNK280\-06

Campo IND\_EST:

Este campo será gerado a partir do campo “12\-Grupo de Contagem”, fazendo o seguinte de\-para entre o grupo de contagem da SAFX235 e o campo IND\_EST do Sped:

__SAFX235__

__IND\_EST__

1 – Estoque próprio em poder do Estabelecimento

0

2 – Estoque próprio em poder de terceiros

1

3 – Estoque de terceiros em poder do Estabelecimento

2

5 – Estoque em Depósito Fechado

0

RNK280\-07

Campo COD\_PART:

Este campo será gerado a partir dos campos 13 e 14 \(Indicador e Código da Pessoa Fis/Jur\) sempre que o Grupo de Contagem \(campo 12\) for = 2 ou 3 \(Estoque próprio em poder de terceiros e Estoque de terceiros em poder do Estabelecimento\)\.

Nesse caso, os campos 13 e 14 sempre estarão preenchidos na SAFX235, pois a crítica já e realizada na importação e na manutenção da SAFX235\.

Desta forma e regra para geração é a seguinte:

Se o campo “12\-Grupo de Contagem” = 2 ou 3,

     Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_PART dos

     demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Participante*”

     \(menu “Dados Iniciais”\), da seguinte forma:

      \- Parâmetro marcado à concatenação do Indicador da pessoa \+  "\-"  \+  Código da pessoa;

      \- Parâmetro desmarcado à o campo será gravado apenas com a informação do código da pessoa;

     A pessoa fis/jur informada neste campo, será gravada no Bloco 0 \(registro 0150\)

Senão

     O campo será gravado sem informação \(“||”\);

__Registro K290 – Produção Conjunta \- Ordem de Produção__

RNK290

Este registro foi criado pelo Ato Cotepe 48/2017, e implementado na __MFS\-20988__ \(Jan/2019\)\.

Neste registro são gravadas as informações sobre a produção conjunta efetuada durante o período de apuração em questão \(data inicial e final do registro K100\)\.

Devem ser considerados para a classificação de produção conjunta apenas os produtos resultantes classificados como co\-produtos \(produto principal\)\. Não se deve informar a produção de subprodutos\.

*Exemplo:* Processo produtivo que resulta em dois subprodutos e um coproduto: declarar nos registros K230/K250\. Processo produtivo que resulta em dois coprodutos e um subproduto: declarar nos registros K290/K300\.

__\[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K290 passa a ser __NÃO OBRIGATÓRIA __para o tipo de leiaute__ Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K290, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K290 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX266 – Produção Conjunta

__\[ALTERADA – MFS\-21976\]__

Critérios para a recuperação dos dados:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e 2\)*;

\-PERIODO\_REFER   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-IND\_PROD\_CONJ = 1 – Própria

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “11\-Inscrição Estadual\-AM” da SAFX266\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada ordem de produção recuperada da SAFX266 será gravado um registro K290, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\.

O parâmetro “*Não informar o número da ordem de produção no registro”* localizado em Dados Iniciais* *será utilizado nesse registro porque o código não é obrigatório no Guia Prático e o usuário poderá decidir se quer gerar ou não a informação no arquivo magnético, pois esse campo é obrigatório na SAFX266, então a partir do momento que esse parâmetro estiver ativado para o registro K290, a informação dos campos 02, 03 e 04 \(ordem de produção, sua data inicial e final\) ficarão como nulo e consequentemente só existirão os produtos a serem declarados nos registros filhos\.

*Consideração:* A geração do arquivo pelo PIM será tratada posteriormente\.

RNK290\-02

Campo DT\_INI\_OP:

__Se__ parâmetro “*Não informar o número da ordem de produção no registro K290*” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

__Senão__  \(permanece a regra original de preenchimento, conforme descrito a seguir\)

     Este campo é preenchido com a data início OP \(campo “07\- Data de Início da Ordem de Produção” da SAFX266\)\.

RNK290\-03

Campo DT\_FIN\_OP:

__Se__ parâmetro “*Não informar o número da ordem de produção no registro K290*” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

__Senão__  \(permanece a regra original de preenchimento, conforme descrito a seguir\)

     Este campo é preenchido com a data conclusão OP \(campo “08\- Data de Conclusão da Ordem de Produção” da SAFX266\), da seguinte forma:

__     Se__  data de conclusão não preenchida 

           *ou* 

          data de conclusão > data final do período da geração \(DT\_FIN do K100\)

           Neste caso o campo será gravado sem informação;

__      Senão__

           Neste caso o campo será preenchido normalmente com a data conclusão OP\.

RNK290\-04

Campo COD\_DOC\_OP:

__\[ALTERADA – MFS\-21976\]__

A geração deste campo depende de alguns parâmetros do menu “Dados Iniciais”, da seguinte forma:

__Se__ parâmetro “*Não informar o número da ordem de produção no registro K290*” = “S”:

     \(parametrização do menu “*Parâmetros à Dados Iniciais*”\)

 

     Neste caso este campo *não* será preenchido\. 

##### __     Senão__

        O campo será preenchido apenas com o conteúdo do campo “06\-Código da Ordem de Produção”\.

__Senão__  

     __Se__ conteúdo do campo “Cód\. Diferenciador de Produção” <>  ‘ ‘ \(um caracter branco\)

           __e           __

          parâmetro “*Considerar o Código Diferenciador no Código da Ordem de Produção*” = “S”

           O campo será preenchido com a concatenação do campo “06\-Código da Ordem de Produção” 

           com o campo “07\-Cód\. Diferenciador de Produção”, sem utilizar nenhum separador;

           Se ao concatenar os dois campos o conteúdo a ser gravado ultrapassar 30 posições \(limite do

           layout\), o registro da ordem de produção em questão será *desconsiderado*, e será gravada a

           seguinte mensagem no log da geração: *“O campo COD\_DOC\_OP ultrapassou o tamanho*

*           máximo permitido \(30 posições\)\. Verificar os parâmetros sobre a geração deste campo\. A ordem*

*           de produção não será considerada na geração do registro K290”\. *\(o log informará também os

           dados para identificação da ordem de produção\)\. 

##### __     __Senão

           O campo será preenchido apenas c/o conteúdo do campo “06\-Código da Ordem de Produção”\.

__Registro K291 – Produção Conjunta \- Itens Produzidos__

RNK291

Este registro foi criado pelo Ato Cotepe 48/2017, e implementado na __MFS\-20988__ \(Jan/2019\)\.

Este registro é “filho” do K290, e será gerado para todas as ordens de produção gravadas no K290 demonstrando cada item e sua quantidade produzida\.

__\[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K291 passa a ser __NÃO OBRIGATÓRIA __para o tipo de leiaute__ Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K291, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K291 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX267 – Produção Conjunta \- Item de Produção

Critérios para a recuperação dos dados:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e 2\)*;

\-PERIODO\_REFER   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-IND\_PROD\_CONJ = 1 – Própria

\-Produto \(campos 08/09\) = serão considerados apenas os registros cujo produto seja do tipo 

                                            “03\-Produto em Processo” ou “04\-Produto Acabado”, ou seja, produtos em

                                            que o campo TIPO\_ITEM do registro 0200 = __03 __ou__ 04__;

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “11\-Inscrição Estadual\-AM” da SAFX266\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada item produzido recuperado da SAFX267 será gravado um registro K291, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\.

*Consideração:* A geração do arquivo pelo PIM será tratada posteriormente\.

RNK291\-02

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0 da seguinte forma:

\- No registro 0200 à Dados de cadastro do produto, conforme as regras do 0200\.

RNK291\-03

Campo QTD:

Se o campo “10\-Quantidade Produzida” da SAFX267 = 0 ou nulo, será gravado zero \(|0|\), pois o campo QTD é de preenchimento obrigatório\.

__\[ALTERADA – MFS\-21976\]__

*Consideração:* A conversão da unidade de medida será tratada posteriormente\.

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX267 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX267 \(campo 11\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K290/K291 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O item da ordem de produção não será considerado na geração”\. *\(o log informará também os dados para identificação da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX267, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX267 se refere à SAFX2007, apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017, mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD será a própria quantidade informada da

      SAFX267 \(campo *10\-Quantidade Produzida*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX267 para a SAFX2013, e a quantidade da

      SAFX267 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX267:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX108 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item da ordem de produção não será considerado na geração do registro K291\.”*

__Registro K292 – Produção Conjunta – Insumos Consumidos__

<a id="_Hlk103176685"></a>RNK292

Este registro foi criado pelo Ato Cotepe 48/2017, e implementado na __MFS\-20988__ \(Jan/2019\)\.

Este registro é “filho” do K290, e demonstra os insumos utilizados durante o processo produtivo, relativo à produção conjunta\. Para cada registro “pai” gravado no registro K290, serão gravados no K292 todos os insumos relacionados\. 

__\[MFS85920\] \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K292 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K292, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K292 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX268 – Produção Conjunta \- Insumo Consumido

Critérios para a recuperação dos dados:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e 2\)*;

\-PERIODO\_REFER   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-IND\_PROD\_CONJ = 1 – Própria

\-Produto \(campos 08/09\) = serão considerados apenas os registros cujo produto seja do tipo 

                                            “00\-Mercadoria para Revenda”, “01\-Matéria Prima”, “02\-Embalagem”, “03\-

                                            Produto em Processo”, “04\-Produto Acabado”, “05\-Subproduto” ou “10\-

                                            Outros Insumos”, ou seja, produtos em que o campo TIPO\_ITEM do

                                            registro 0200 = __00, 01, 02, 03, 04, 05 ou 10__;

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “11\-Inscrição Estadual\-AM” da SAFX266\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada item de produção recuperado da SAFX268, será gravado um registro K292, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\.

*Consideração:* A geração do arquivo pelo PIM será tratada posteriormente\.

RNK292\-02

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à concatenação do Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0 da seguinte forma:

\- No registro 0200 à Dados de cadastro do produto, conforme as regras do 0200\.

RNK292\-03

Campo QTD:

Se o campo “10\-Quantidade Consumida” da SAFX268 = 0 ou nulo, será gravado zero \(|0|\), pois o campo QTD é de preenchimento obrigatório\.

__\[ALTERADA – MFS\-21976\]__

*Consideração:* A conversão da unidade de medida será tratada posteriormente\.

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX268 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX268 \(campo 11\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K290/K292 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O item da ordem de produção não será considerado na geração”\. *\(o log informará também os dados para identificação da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX268, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX268 se refere à SAFX2007, apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017, mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD será a própria quantidade informada da

      SAFX268 \(campo *10\-Quantidade Produzida*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX268 para a SAFX2013, e a quantidade da

      SAFX268 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX268:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX108 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item da ordem de produção não será considerado na geração do registro K292\.”*

__Registro K300 \- Produção Conjunta \- Industrialização Efetuada por Terceiros__

RNK300

Este registro foi criado pelo Ato Cotepe 48/2017, e implementado na __MFS\-20988__ \(Jan/2019\)\.

Neste registro são gravadas as informações sobre a produção conjunta efetuada por terceiros durante o período de apuração em questão \(data inicial e final do registro K100\)\.

Este registro tem como objetivo informar a data de reconhecimento da produção ocorrida em terceiro, relativa à produção conjunta\. Entenda\-se por produção conjunta a produção de mais de um produto resultante a partir do consumo de um ou mais insumos em um mesmo processo\.

__\[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K300 passa a ser __NÃO OBRIGATÓRIA __para o tipo de leiaute__ Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K300, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K300 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX266 – Produção Conjunta

Critérios para a recuperação dos dados:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e 2\)*;

\-PERIODO\_REFER   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-IND\_PROD\_CONJ = 2 – Efetuada por Terceiros

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “11\-Inscrição Estadual\-AM” da SAFX266\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada ordem de produção recuperada da SAFX266 será gravado um registro K300, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\.

*Consideração:* A geração do arquivo pelo PIM será tratada posteriormente\.

__Registro K301 \- Produção Conjunta \- Industrialização Efetuada por Terceiros \- Itens Produzidos__

RNK301

Este registro foi criado pelo Ato Cotepe 48/2017, e implementado na __MFS\-20988__ \(Jan/2019\)\.

Este registro é “filho” do K300, e será gerado para a produção realizada por terceiro gravada no K300 demonstrando cada item e sua quantidade produzida\.

__\[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K301 passa a ser __NÃO OBRIGATÓRIA __para o tipo de leiaute__ Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K301, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K301 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX267 – Produção Conjunta \- Item de Produção

Critérios para a recuperação dos dados:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e 2\)*;

\-PERIODO\_REFER   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-IND\_PROD\_CONJ = 2 – Efetuada por Terceiro

\-Produto \(campos 08/09\) = serão considerados apenas os registros cujo produto seja do tipo 

                                            “03\-Produto em Processo” ou “04\-Produto Acabado”, ou seja, produtos em

                                            que o campo TIPO\_ITEM do registro 0200 = __03 __ou__ 04__;

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “11\-Inscrição Estadual\-AM” da SAFX266\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada item produzido recuperado da SAFX267 será gravado um registro K301, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\.

*Consideração:* A geração do arquivo pelo PIM será tratada posteriormente\.

RNK301\-02

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0 da seguinte forma:

\- No registro 0200 à Dados de cadastro do produto, conforme as regras do 0200\.

RNK301\-03

Campo QTD:

Se o campo “10\-Quantidade Produzida” da SAFX267 = 0 ou nulo, será gravado zero \(|0|\), pois o campo QTD é de preenchimento obrigatório\.

__\[ALTERADA – MFS\-21976\]__

*Consideração:* A conversão da unidade de medida será tratada posteriormente\.

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX267 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX267 \(campo 11\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K300/K301 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O item da ordem de produção não será considerado na geração”\. *\(o log informará também os dados para identificação da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX267, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX267 se refere à SAFX2007, apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017, mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD será a própria quantidade informada da

      SAFX267 \(campo *10\-Quantidade Produzida*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX267 para a SAFX2013, e a quantidade da

      SAFX267 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX267:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX108 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item da ordem de produção não será considerado na geração do registro K301\.”*

__Registro K302 \- Produção Conjunta \- Industrialização Efetuada por Terceiros \- Insumos Consumidos__

<a id="_Hlk103177031"></a>RNK302

Este registro foi criado pelo Ato Cotepe 48/2017, e implementado na __MFS\-20988__ \(Jan/2019\)\.

Este registro é “filho” do K300, e demonstra os insumos utilizados durante o processo produtivo, relativo à produção conjunta efetuada por terceiros\. Para cada registro “pai” gravado no registro K300, serão gravados no K302 todos os insumos relacionados\. 

__MFS85920\] \[MFS97186\] Tratamento em atendimento ao layout  versão 1\.16 \(Janeiro/2023\)__

__Para o período de geração a partir de 01/01/2023:__

A partir desse layout, a geração do registro K302 passa a ser __NÃO OBRIGATÓRIA __para os tipos de leiaute__ Simplificado__ ou __Restrito aos Saldos de__ __Estoque\.__

A escolha em gerar o registro K302, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro K302 será gerado ou não, pois não foi feito tratamento pelo código\-fonte para essa tratativa\.

__Para o período de geração anterior a 01/01/2023:__

Origem dos Dados: 

SAFX268 – Produção Conjunta \- Insumo Consumido

Critérios para a recuperação dos dados:

\-COD\_EMPRESA  = código da empresa;  

\-COD\_ESTAB        = código do Estabelecimento informado para a geração *\(ver OBS 1 e 2\)*;

\-PERIODO\_REFER   = mês e ano da apuração \(mês/ano da DT\_FIN do K100\);

\-IND\_PROD\_CONJ = 2 – Efetuada por Terceiro

\-Produto \(campos 08/09\) = serão considerados apenas os registros cujo produto seja do tipo 

                                            “00\-Mercadoria para Revenda”, “01\-Matéria Prima”, “02\-Embalagem”, “03\-

                                            Produto em Processo”, “04\-Produto Acabado”, “05\-Subproduto” ou “10\-

                                            Outros Insumos”, ou seja, produtos em que o campo TIPO\_ITEM do

                                            registro 0200 = __00, 01, 02, 03, 04, 05 ou 10__;

OBS 1 \- Na geração por inscrição estadual única, deve\-se recuperar os dados das ordens de produção de todos os estabelecimentos envolvidos na centralização\.

OBS 2 \- Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), feita no menu “Geração\-PIM”, os registros serão filtrados além do Estabelecimento, pela inscrição estadual \(campo “11\-Inscrição Estadual\-AM” da SAFX266\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\.

Para cada item de produção recuperado da SAFX268, será gravado um registro K302, conforme os dados descritos na __planilha DEPARA__, e nas regras especificas de cada campo, quando for o caso\.

*Consideração:* A geração do arquivo pelo PIM será tratada posteriormente\.

RNK302\-02

Campo COD\_ITEM:

Na gravação deste campo será utilizada a mesma regra definida para o campo COD\_ITEM dos demais registros, considerando o parâmetro “*Considerar o Indicador no Código do Item*” \(menu “Dados Iniciais”\):

     \- Parâmetro marcado à Indicador do produto  \+  "\-"  \+  Código do produto

     \- Parâmetro desmarcado à Código do produto

O produto informado neste campo será gravado no Bloco 0 da seguinte forma:

\- No registro 0200 à Dados de cadastro do produto, conforme as regras do 0200\.

RNK302\-03

Campo QTD:

Se o campo “10\-Quantidade Consumida” da SAFX268 = 0 ou nulo, será gravado zero \(|0|\), pois o campo QTD é de preenchimento obrigatório\.

__\[ALTERADA – MFS\-21976\]__

*Consideração:* A conversão da unidade de medida será tratada posteriormente\.

A quantidade a ser informada deve ser referente a unidade de medida do cadastro do produto \(SAFX2013\), por isso, será verificado se a unidade de medida informada na SAFX268 é a mesma unidade do cadastro, e realizada conversão se necessário, da seguinte forma:

A unidade de medida da SAFX268 \(campo 11\-Unidade de Medida\) será comparada a unidade de medida do cadastro do produto \(SAFX2013, campo 14\-Código de Medida\)\. 

Caso a unidade de medida do cadastro não esteja preenchida, o registro da ordem de produção em questão será *desconsiderado*, e será gravada a seguinte mensagem no log da geração: *“Para gerar os registros K300/K302 é necessário o preenchimento do campo “14\-Código de Medida” no cadastro do produto \(SAFX2013\)\. O item da ordem de produção não será considerado na geração”\. *\(o log informará também os dados para identificação da ordem de produção\)\.

*\(não é necessário validar o preenchimento da unidade da SAFX268, pois é campo obrigatório\)*

*\(observar que a unidade da SAFX268 se refere à SAFX2007, apesar do tamanho do campo e do nome da coluna no BD serem referentes à SAFX2017, mas tanto na importação como na manutenção, a crítica é feita com base na SAFX2007\) *

  

__Se__ as duas medidas forem iguais:

      Neste caso o conteúdo a ser gravado no campo QTD será a própria quantidade informada da

      SAFX268 \(campo *10\-Quantidade Produzida*\); 

__Senão__ 

      Neste caso será feita a conversão de medida da SAFX268 para a SAFX2013, e a quantidade da

      SAFX268 será ajustada para esta nova medida\.

      Exemplo:  

          SAFX2013:  Unidade = Kilo

          SAFX268:    Unidade = Tonelada       Quantidade: 12 toneladas

          Fator de conversão obtido nas tabelas de conversão:   1 Tonelada = 1\.000 Kilos 

          Quantidade ajustada = 12\.000 Kilos \(qtd da SAFX108 ajustada p/a medida “Kilo”\)  

          O conteúdo a ser gravado será a quantidade ajustada \(no exemplo, seria 12\.000 Kilos\)\.

A conversão será feita conforme o procedimento padrão, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

     \- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por

       produto;

     \- Caso não exista, é feita a pesquisa na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o registro do movimento em questão será *desconsiderado*, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item da ordem de produção não será considerado na geração do registro K302\.”*

__Registro K990 – Encerramento do Bloco K__

RNK990

Um registro por arquivo, informando a quantidade total de linhas do Bloco K gravadas no arquivo\.

= = = = =

