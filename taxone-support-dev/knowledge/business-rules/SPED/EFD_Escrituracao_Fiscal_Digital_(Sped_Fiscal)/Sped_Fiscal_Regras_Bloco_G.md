# Sped_Fiscal_Regras_Bloco_G

- **Fonte:** Sped_Fiscal_Regras_Bloco_G.docx
- **Modificado:** 2026-03-18
- **Tamanho:** 78 KB

---

Sped Fiscal – Bloco G

 Controle do Crédito de ICMS do Ativo Permanente \- CIAP

O Bloco G tem três formas de geração: 

   \- A partir dos dados do Módulo CIAP \(para clientes que utilizam o módulo\);

   \- A partir de dados importados via SAFX133/134/135/136 \(para clientes que *não* utilizam o módulo\);

   \- A partir dos dados do Módulo CIAP \(para clientes que utilizam o módulo\), mas demonstrando as informações de apropriação do crédito de forma extemporânea, ou seja, considerando os dados do CIAP do mês imediatamente anterior ao da geração;

A forma de geração é identificada através de parâmetros na tela “Dados Iniciais” do Sped Fiscal\.

 Este documento define *apenas* as regras da geração a partir das informações do Módulo CIAP\. 

Para verificar a forma de geração através das tabelas SAFX133/134/135/136, ver o documento “*Sped\_Fiscal\_Regras\_BlocoG\_OutrasOrigens*”\.

Para verificar a forma de geração extemporânea, ver o documento “Sped\_Fiscal\_Regras\_Bloco\_G\_Per\_Anterior”\.

Quadro de Revisões

__                         Revisões realizadas a partir de 08/04/2016__

*            \(para consultar revisões anteriores, verificar o documento das revisões originais\)*

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

02/05/16

CH3435/2016

Inclusão da RNG130\-05, campo 05 – SERIE\.

Lara Aline

19/01/2017

MFS4805

Alteração na geração dos Bens originados das tabelas SAFX233/SAFX234 \(menu “Créditos Extemporâneos \- Integral” do módulo CIAP\)\.

Ver RNG125\-ESP e RNG130\. 

Vânia Mattos 

22/12/2017

MFS14642

Inclusão da chamada da geração extemporânea

Andréa Rocha

04/09/2018

CH20668\_2018

MFS\-20726

Quando o tipo de movimentação – TIPO\_MOV do registro G125 – for igual a “CI”, não devem ser informados os documentos fiscais relativos ao tipo de movimentação “IA” dos seus componentes que entraram no mesmo período da finalização, os registros G130/G140 não devem ser gerados\.

João Henrique

13/05/2019

MFS26746

Essa MFS tem como objetivo alterar a regra de recuperação do livro de apuração do ICMS\.

Andréa Rocha

09/12/2019

MFS31420

Essa MFS tem como objetivo incluir os campos novos nos registros G130 e G140

Andréa Rocha

22/01/2019

MFS33434

Alteração na geração do campo VL\_ICMS\_DIF\_APLICADO do Registro G140

Andréa Rocha

19/01/2019

MFS34318

Alteração dos campos de valor do Registro G140

Andréa Rocha

12/03/2020

MFS34966

Alteração da geração do Registro G140

Andréa Rocha

28/04/2022

MFS84519

Inclusão de comentário da relação entre a  geração do campo 03 – COD\_ITEM do Registro G140 e o campo 06 \- UNID\_INV do registro 0200

Andréa Rocha

05/08/2022

MFS91149

Alteração na geração do Campo 02 \- COD\_IND\_BEM do Registro 0300 para considerar o parâmetro “Gerar o separador “I” – Para o código de Bem / Incorporador” de separador para o Código do Bem x Código de Incorporador\.

Rogério Ohashi

__06/02/2023__

MFS435439

Inclusão de tratamento do campo de DT\_FIN, para considerar o novo campo de DAT\_ENCERRAMENTO da tabela de Inscrição Estadual para os clientes que encerrarem a Inscrição Estadual\. G110\.

Rogério Ohashi

__01/10/2024__

MFS689479

Alteração da geração do registro G110, para gerar o registro quando não houver movimentação de bens no mês e houver somente registros extemporâneos no registro G126\. O registro G110 deve ser gerado somente com o valor no campo 10\-SOM\_ICMS\_OC, que é o valor dos créditos extemporâneos\.

Andréa Rocha

__Registro G001 – ABERTURA DO BLOCO G__

__RNG001__

Este registro deve ser gerado para abertura do Bloco G, indicando se há registros de informações no bloco\.

CH99308\-A:

 Para abrir o Bloco G é necessário possuir a apuração referente ao livro 108 \(Livro Registro de Apuração do ICMS \- RAICMS \- Modelo P9\)\.

Quando não encontrado o livro 108 para o período e estabelecimento informado, então gerar mensagem no log conforme referência 366 do documento “Sped\_Fiscal\_Log\_Erros\.xls”

__\[Alterada MFS26746\]__ O tipo de apuração igual a “3 – Prodepe \(livros 142/143\)” passa a ser considerado na geração da EFD\.  Quando o tipo for 3, deve ser feito o mesmo tratamento do tipo de apuração igual a “1\-Apuração Normal \(livro 108\)”, ou seja, deve se considerar o período de apuração do livro 108 para a geração\.

__Registro G110 – ICMS Ativo Permanente \- CIAP__

RNG110

Os dados deste registro serão gerados a partir do Módulo CIAP, considerando a apuração do período correspondente a apuração do ICMS\. 

Assim, as datas inicial e final do período a serem consideradas são as mesmas do E100\.

__Problemas sobre o Bloco G__:

Originalmente o layout do Bloco G tratava alguns campos separadamente, dependendo do tipo do livro \(modelo C ou D\)\. Posteriormente, a partir do GP vrs 2\.0\.1, a EFD definiu *regras próprias* para o cálculo do CIAP, e o layout foi unificado\. Com isso, surgiu a dúvida sobre a possibilidade de termos diferença entre o resultado obtido de acordo com as regras do Guia Prático \(campo ICMS\_APROP do G110\) e o resultado calculado no Módulo do CIAP\. 

Segue parecer da Informação sobre o assunto \(reunião realizada em 24/06/2010, Can, Victória e Vânia\): 

A EFD não tem como extinguir a utilização do Modelo C\. As regras do cálculo descritas na legislação do CIAP, que prevê os dois modelos de livro \(C e D\), não podem ser alteradas pela EFD\. Para isso, seria necessário ato legal específico, alterando a legislação do CIAP\. Sendo assim, nós devemos gerar as informações do Bloco G, exatamente como solicitadas no novo Guia Prático \(vrs 2\.0\.1\), lembrando que o novo GP não faz mais nenhuma referência aos modelos C e D, e simplesmente descreve a informação a ser demonstrada\. 

__Conclusão__: Devemos prever que os clientes continuarão a utilizar os modelos de livro que já usavam antes \(C ou o D\), e devemos levar para o Sped a informação solicitada no Guia Prático, sem a preocupação com o tipo de livro utilizado\.  O resultado disso é que poderemos ter no campo ICMS\_APROP \(G110\) um valor diferente do resultado do CIAP calculado no Modelo C ou D, que será o valor lançado de fato na apuração do ICMS\. No entanto, a opinião da Informação é que esta questão não poderá ser resolvida neste momento\.

As regras de geração dos registros do Bloco G dependem do modelo de livro utilizado \(C ou D\), e também do formato do livro\. A identificação destes dados é feita através da parametrização do CIAP, na tabela __APT\_ESTAB __\(menu “Cadastros à Parâmetros de Estabelecimento”\), da seguinte forma:

MODELO\_102 \(modelo C ou D\)

         TIPO\_MODELO\_102 \(layout do livro\)

                     C

            1  \(layout da IN 50 DRP/RS\)

            2  \(layout do Ajuste SINIEF 03/01\)

            3  \(layout do Decreto 27\.427/00 – RJ\)

            4  \(layout do Decreto 7\.886/00 – BA\)

            6  \(layout do Decreto 5\.141/01 – PR\)

                      D

            1  \(layout da IN 50 DRP/RS\)

            2  \(layout do Ajuste SINIEF 03/01\)

            5  \(layout CIAF/MS\) 

__OBS1__: Na geração por inscrição estadual única, os cálculos do CIAP já terão sido executados em nome do centralizador, e assim, todas as tabelas que contêm o resultado da apuração do CIAP, estarão gravadas sempre em nome do centralizador\. Algumas tabelas têm o código do estabelecimento de origem do Bem, para possibilitar o acesso aos cadastros \(APT\_AQUISICAO ou APT\_ALIENACAO\), quando necessário\.

__OBS2 \(OS2931\-B12\)__: Na geração da opção “*Geração \- PIM*” o Bloco G só será gerado para o arquivo da inscrição estadual parametrizada no Módulo CIAP \(campo “Inscrição Estadual p/AM” do item “Cadastros à Parâmetros por Estabelecimento”\)\. Os dados do Bloco G serão gerados a partir da apuração do CIAP feita para o Estabelecimento\. Nos arquivos das demais inscrições estaduais o Bloco G será gerado sem informação\.  

__OBS3 \(OS3114\-E\)__: Na geração da opção “*Geração \- PIM*” foi incluída uma nova forma de gerar o Bloco G\. Através do parâmetro “*Geração para os usuários do Módulo PIM*”, o usuário poderá optar se deseja gerar o Bloco G para uma única IE \(conforme descrito na OBS anterior\), ou se deseja gerar o Bloco G separadamente por Inscrição Estadual – PIM\. Para possibilitar a geração do Bloco G por IE\-PIM, o Módulo CIAP foi alterado para a criação do cálculo por Inscrição Estadual – PIM \(alterações efetuadas nas OS’s 3114\-A, B, C e D\)\. Para gerar o Bloco G por IE, deverão ser utilizadas as tabelas do cálculo do CIAP gerado por IE, que terão a inscrição estadual incluída na chave da tabela\. Assim, para um único estabelecimento, poderão existir várias apurações do CIAP, uma para cada inscrição estadual\. 

__OBS4 \(MFS689479\)__: O registro G110 deve ser gerado quando houver dados no registro G126, mesmo que não haja dados gerados pelo cálculo do crédito do ICMS no período gerado\. Ou seja, se as tabelas do cálculo do crédito do ICMS, de acordo com modelo selecionado, C ou D \(APT\_DEM\_CR\_MENSAL ou APT\_EST\_MENS\_ANO\), não tiverem informações no mês da geração, e houver somente informações de créditos extemporâneos \(G126\), o registro G110 deve ser gerado\.  Os campos DT\_INI, DT\_FIN e SOM\_ICMS\_OC devem ser preenchidos conforme as regras, e os demais campos devem ser preenchidos com zeros\.

__\[ALTERAÇÃO\-MFS435439\]__ Tratamento da Regra para Inscrição Estadual Encerrada

Tratamento na geração do campo de DT\_FIN para os clientes que encerrarem a Inscrição Estadual da UF do próprio Estabelecimento, nesse caso o sistema deverá consultar o campo de Data de Encerramento \(DAT\_ENCERRAMENTO\) da tabela REGISTRO\_ESTADUAL, e segui conforme a Regra abaixo:  

Tratamento:

Se o campo de DAT\_ENCERRAMENTO da tabela REGISTRO\_ESTADUAL estiver preenchido;

   E o campo de UF da tabela REGISTRO\_ESTADUAL for igual ao campo de UF do Estabelecimento;

   Preencher o campo de DT\_FIN com o campo de DAT\_ENCERRAMENTO da tabela REGISTRO\_ESTADUAL\.

Obs\.: Para esse campo ser considerado, a data de encerramento deverá estar entre o período de referência da geração

RNG110\-04

Campo SALDO\_IN\_ICMS:

Neste campo é demonstrado o valor do ICMS referente aos Bens adquiridos em períodos anteriores \(Bens que entraram no CIAP até o mês anterior\)\. Este valor representa o saldo total do crédito no início do período, independente da movimentação que ocorrerá no mesmo\.

Preencher com o total dos valores de ICMS de todos os registros ‘filhos’ G125, que sejam movimentos de *entrada* caracterizados como “*SI*” \(campo 04\-TIPO\_MOV = SI\):

05\-VL\_IMOB\_ICMS\_OP   \+   06\-VL\_IMOB\_ICMS\_ST   \+   07\-VL\_IMOB\_ICMS\_FRT   \+   08\-VL\_IMOB\_ICMS\_DIF

RNG110\-05

Campo SOM\_PARC:

Preencher com o total do campo 10\-VL\_PARC\_PASS de todos os registros ‘filhos’ G125\.

\(este valor corresponde a soma do \[valor de ICMS / 48\] de todos os Bens que compõe o livro do período\)

RNG110\-06

Campo VL\_TRIB\_EXP:

Preencher com o valor das saídas tributadas \+ exportações  do período, que correspondente ao campo descrito a seguir, dependendo do modelo do livro do CIAP:

Se Modelo = “C”

      Preencher com o conteúdo da coluna VLR\_TOT\_OP\_TRIBUT da tabela APT\_DEM\_CR\_MENSAL

      \(corresponde ao campo “Total das Op\. de Saída Tributadas” do menu “Movimento à Manutenção

        Dados do Cálculo à Modelo C à Cálculo Geral dos Créditos”\)  

Se Modelo = “D” 

      Preencher com o conteúdo da coluna VLR\_TOT\_OP\_ISENTAS da tabela APT\_EST\_MENS\_ANO

     \(corresponde ao campo “Total de Operações Tributadas” do menu “Movimento à Manutenção

       Dados do Cálculo à Modelo D à Fator de Cálculo”\) 

__OS3114\-E__: No caso da geração do Bloco G por Inscrição Estadual – PIM, considerar a tabela do cálculo do CIAP realizado por IE\-PIM\. 

__Alteração da OS4459\-A:__

As tabelas envolvidas na geração deste campo tiveram sua chave primária alterada na OS4459 para inclusão da fração\. Isso significa que a partir de então, poderão existir de ‘n’ linhas referentes a *um mesmo período*, diferenciadas justamente pela fração\. No entanto, a informação tratada neste campo terá sempre o *mesmo conteúdo* nas ‘n’ linhas referentes a um único período\. Por isso, a informação poderá ser recuperada de qualquer uma das linhas de resultado referentes ao período em questão\.

RNG110\-07

Campo VL\_TOTAL:

Preencher com o valor total das saídas do período, que correspondente ao campo descrito a seguir, dependendo do modelo do livro do CIAP:

Se Modelo = “C”

      Preencher com o conteúdo da coluna VLR\_TOT\_OP\_SAIDAS da tabela APT\_DEM\_CR\_MENSAL

      \(corresponde ao campo “Total Geral das Op\. de Saída” do menu “Movimento à Manutenção

        Dados do Cálculo à Modelo C à Cálculo Geral dos Créditos”\)  

Se Modelo = “D” 

      Preencher com o conteúdo da coluna VLR\_TOT\_OP\_SAIDAS da tabela APT\_EST\_MENS\_ANO

     \(corresponde ao campo “Total das Operações de Saída” do menu “Movimento à Manutenção

       Dados do Cálculo à Modelo D à Fator de Cálculo”\)

__OS3114\-E__: No caso da geração do Bloco G por Inscrição Estadual – PIM, considerar a tabela do cálculo do CIAP realizado por IE\-PIM\. 

__Alteração da OS4459\-A:__

As tabelas envolvidas na geração deste campo tiveram sua chave primária alterada na OS4459 para inclusão da fração\. Isso significa que a partir de então, poderão existir de ‘n’ linhas referentes a *um mesmo período*, diferenciadas justamente pela fração\. No entanto, a informação tratada neste campo terá sempre o *mesmo conteúdo* nas ‘n’ linhas referentes a um único período\. Por isso, a informação poderá ser recuperada de qualquer uma das linhas de resultado referentes ao período em questão\.

RNG110\-08

Campo IND\_PER\_SAI:

Este valor representa o índice de participação das saídas tributadas/exportação sobre o valor total das saídas do período, e deve ser preenchido com o seguinte conteúdo: 

                        \( campo 08\-VL\_TRIB\_EXP  /  campo 09\-VL\_TOTAL \)

A partir da OS2388\-E23, este cálculo passou a ser feito considerando 8 casas decimais\.

RNG110\-09

Campo ICMS\_APROP:

Este valor representa o crédito final a ser apropriado, e deve ser preenchido com o seguinte conteúdo: 

                            \( campo 05\-SOM\_PARC \* campo 08\- IND\_PER\_SAI \)

__Obs__: Como a EFD definiu regras próprias para a apuração do CIAP, que difere tanto do Modelo C como do Modelo D, existe a possibilidade deste valor não coincidir com o resultado final calculado no módulo CIAP \(ver obs a respeito na RNG110\)\.

RNG110\-10

Campo SOM\_ICMS\_OC:

Preencher com o total das parcelas “extemporâneas” gravadas no registro G126\. 

\(é a totalização do campo “09 \- VL\_PARC\_APROP” do G126\)

__Alteração da MFS3615: __Com a criação da SAFX233 \(Cadastro dos Bens com prazo de apropriação “normal” já vencido\), a totalização dos registros G126 irá considerar tanto os créditos extemporâneos originados dos Bens da APT\_AQUISICAO, como os creditos extemporãneos originados da SAFX233\.

__Registro G125 – Movimentação de Bem ou Componente do Ativo Imobilizado__

RNG125

__Alteração da MFS3615: __Com a criação da SAFX233 \(Cadastro dos Bens com prazo de apropriação “normal” já vencido\), o Bloco G passou a considerar tanto os Bens da APT\_AQUISICAO, como os Bens da SAFX233 *que tenham parcelas extemporâneas calculadas para o período*\. As regras da geração atual \(Bens originados da APT\_AQUISICAO\) *não se modificam*\. As regras da geração do G125 para os Bens da SAFX233 estão definidas na regra abaixo “__RNG125\-ESP__”\.

Neste registro serão gravadas todas as movimentações dos Bens que compõe a apuração do CIAP no período em questão, com exceção das baixas parciais\. 

Estes movimentos correspondem aos dados demonstrados nos livros do CIAP, que são as informações sobre a NF da entrada do Bem, e também sobre as baixas efetuadas no período\.

__Sobre as Baixas Parciais:__

As baixas parciais *não* aparecerão no G125\. Em caso de Bens com baixas parciais, o movimento da entrada do Bem no G125 demonstra os valores de ICMS  atualizados \(valor original da entrada do Bem menos as baixas já efetuadas\)\. 

Além dos Bens que compõe o CIAP do período, também serão gravados no G125 os Bens do tipo “componente” adquiridos ou baixados no período em questão, e que *não tenham direito à apropriação de créditos*\. São os Bens do cadastro do CIAP com status = “I” \(Informativo\)\. Para maiores informações sobre a *não apropriação* de créditos dos componentes, ver help referente ao menu “*Cadastros à Parâmetros por Estabelecimento*”, parâmetro “Não Apropriar Créditos dos Bens Componentes”\.

A seguir serão definidas as regras para recuperação dos dados nas duas situações: os Bens que compõe o CIAP e os Bens Componentes adquiridos no período:

__Regra geral de recuperação dos dados \(Bens que compõe o CIAP\)__:

Se Modelo = “C”à utilizar a tabela APT\_DEM\_BASE\_CR

Se Modelo = “D”à utilizar as tabelas APT\_EST\_SAIDA  e  APT\_ALIENACAO

No caso do __Modelo C__  os movimentos ficam em uma única tabela, a APT\_DEM\_BASE\_CR:

     Movimentos de entrada à linhas da APT\_DEM\_BASE\_CR com IND\_E\_S = ‘E’

     Movimentos de saída   à  linhas da APT\_DEM\_BASE\_CR com IND\_E\_S = ‘S’

     Obs: É provável que algumas informações referentes às saídas tenham que ser recuperadas do

     cadastro das alienações, já que nem todos os dados constam da tabela do cálculo\. 

No caso do __Modelo D__  são utilizadas duas tabelas, uma para as entradas e outra para as saídas:

     Movimentos de entrada à  APT\_EST\_SAIDA

     Movimentos de saída    à  APT\_ALIENACAO

    

Critérios para recuperação dos dados:

\(sendo DT\_INI e DT\_FIN as datas inicial e final do registro G110\)

APT\_DEM\_BASE\_CR à COD\_EMPRESA, COD\_ESTAB e DAT\_APURACAO = DT\_FIN

APT\_EST\_SAIDA    à COD\_EMPRESA, COD\_ESTAB e DAT\_APURACAO = DT\_FIN

APT\_ALIENACAO  à COD\_EMPRESA, COD\_ESTAB e DAT\_OPER >= DT\_INI e <= DT\_FIN 

__Cada linha recuperada representa um movimento que será gravado neste registro__ \(com exceção das baixas parciais\)\.

As baixas parciais não geram movimentos de saída no G125\. Elas precisam ser recuperadas apenas para calcular os valores de ICMS a serem gravados no movimento de entrada do G125 \(no caso dos Bens com baixas parciais\)\. 

A gravação dos campos deve seguir as regras específicas de cada campo, podendo variar de acordo com a tabela utilizada\.

Desta forma, para cada Bem será gravado:

- Um movimento de entrada com os valores da entrada do Bem; 
- Zero ou um movimento de saída referente a baixa total do Bem;

èOriginalmente definimos a geração para gravar as baixas por término do período de apropriação somente no mês seguinte ao da última parcela, seguindo as regras do GP vrs 2\.0\.0\. \(registro G125, campo 4, item 3\), que coincide com as regras do livro Modelo C do CIAP\. No entanto, no GP vrs 2\.0\.1, a regra foi alterada para gravar estas baixas no mês da ocorrência \(registro G125, campo 4, item 5\)\. 

__OS3114\-E__: No caso da geração do Bloco G por Inscrição Estadual – PIM, considerar a tabela do cálculo do CIAP realizado por IE\-PIM, onde a inscrição estadual compõe a chave\. Neste tipo de geração, a recuperação dos dados das aquisições e alienações \(APT\_AQUISICAO e APT\_ALIENACAO\) é feita normalmente através do identificador do CIAP \(NUM\_CIAP\), lembrando que o controle da numeração do CIAP é feito por Estabelecimento, inclusive para os usuários do PIM\.

__Regra geral de recuperação dos Componentes adquiridos ou baixados no período__:

Recuperar todos os itens do cadastro do CIAP \(APT\_AQUISICAO\) nas seguintes condições:

Para os Componentes adquiridos no período:

- Data Fiscal = deve estar compreendida no período \(DT\_INI e DT\_FIN do G110\) 
- Status do CIAP = “I” \(Informativo\)

Para os Componentes baixados no período \(alteração OS2388\-E22\):

- Data da alienação deve estar compreendida no período \(DT\_INI e DT\_FIN do G110\) 
- Status do CIAP = “I” \(Informativo\)

O status “I” identifica os Bens componentes sem direito à apropriação de créditos\.

Os componentes nesta situação são recuperados direto da APT\_AQUISICAO porque eles *não constam* das tabelas do cálculo\.

__OS3114\-E__: No caso da geração do Bloco G por inscrição estadual do PIM, deve\-se incluir a inscrição estadual ao filtrar as linhas da APT\_AQUISICAO\.  

__OS2388\-E22__: Além de recuperar os Bens “informativos” adquiridos no período, a geração passou a recuperar também os Bens “informativos” que tenham tido alguma baixa no período da geração\. Esta alteração foi realizada para atender as alterações do Guia Prático vrs 2\.0\.3 \(registro G125, item \(2\.4\) do campo 04\)\. 

__Regra p/ Totalização das Aquisições de mesmo Código de Bem__:     __\(OS2931\-B13\)__

Na OS2931\-B13 foi alterada a geração do arquivo para efetuar a totalização dos valores do G125 no caso de itens do cadastro do CIAP que tenham o mesmo Código de Bem\.

Critérios para totalização das aquisições para o registro G125:

- Mesmo estabelecimento \(por causa da geração por I\.E\.U\);
- Mesmo Código de Bem;
- As aquisições devem estar *no mesmo período de apropriação dos créditos*, ou seja, a informação a ser gravada no campo 09\-NUM\_PARC do G125 deve ser a mesma; 

Só serão totalizadas as aquisições que se encontrem *na mesma parcela de apropriação*, considerando os créditos extemporâneos que possam existir para alguma aquisição\.

Sobre o campo DT\_MOV do G125 è Quando duas aquisições a serem totalizadas tiverem datas de operação diferentes, a data a ser gravada no G125 será ser a *menor data* \(exemplo: aquisições do Bem __B700__ do cenário de teste\)\.

Obs: Quando esta situação ocorre para Bens adquiridos em períodos anteriores ao da geração, não é necessário aplicar esta regra, pois o G125 é gerado sempre com a data do primeiro dia do período \(exemplo: aquisições do Bem __B240__ do cenário de teste\)\. 

 

Sobre o tipo do movimento do G125 è O tipo do movimento do G125 também deveria constar dos critérios para efetuar a totalização, pois é campo chave deste registro\. No entanto, observa\-se que no caso das entradas, o tipo de movimento será sempre o mesmo, independente do número de aquisições\. Isso porque nas entradas o campo 04\-TIPO\_MOV é gerado a partir do indicador da SAFX13 \(campo “Tipo do Bem”\), e como todas as aquisições estão relacionadas ao mesmo Bem, o tipo de movimento será sempre o mesmo\.

Para as aquisições a serem totalizadas deve\-se somar:

- Os valores do ICMS \(campos 05, 06, 07 e 08\);
- O valor passível de apropriação \(campo 10\);

Sempre que um movimento de entrada do registro G125 for o *resultado de uma consolidação*, as saídas correspondentes e os registros “filhos” G126, G130 e G140 também deverão ser totalizados *ou* agrupados, conforme o caso:

__Baixas \(movimentos de saída do registro G125\)__: 

Baixas do tipo “Parcial” à Estas baixas servem apenas para deduzir os valores de ICMS a serem demonstrados no movimento de entrada, pois elas *não* são gravadas no arquivo\. Neste caso, dependendo de como a totalização for realizada, temos duas situações:

Baixas do tipo “Total” à Fazer um grupamento dos registros *para evitar a repetição de registros iguais*, lembrando que no caso das saídas o registro G125 é gravado sempre *sem* informação nos campos de valor \(campo 05 ao 10\)\. Logo, *não existem valores a serem totalizados*, basta evitar a gravação de baixas de mesmo Código de Bem e Tipo de Movimento;

Sobre o campo DT\_MOV do G125 è A data do movimento \(campo DT\_MOV do G125\) *não* deve ser considerada no grupamento, e quando duas baixas a serem grupadas tiverem datas diferentes, a data a ser gravada no G125 será ser a *menor data* \(exemplo: baixas do Bem __B005__ do cenário de teste\)\.

OBS à A chave do registro G125 é COD\_IND\_BEM  \+  TIPO\_MOV \(até o Guia Prático vrs 2\.0\.2\)

__Créditos Extemporâneos \(G126\)__:

Os créditos extemporâneos referentes às aquisições totalizadas em um registro G125, deverão ter os seus valores   totalizados \(campos 05\-VL\_PARC\_PASS e 09\-VL\_PARC\_APROP\) por período e número da parcela \(campos 02\-DT\_INI, 03\-DT\_FIM e 04\-NUM\_PARC\);

__Notas Fiscais e Itens de Notas Fiscais \(G130 e G140\)__:

As informações das notas fiscais e itens das notas fiscais referentes às aquisições ou baixas totalizadas num único registro G125, deverão ser agrupadas *para evitar a repetição de registros iguais*\. No caso destes registros não é necessário fazer nenhuma totalização, pois eles não têm informações de valores\. Assim, basta evitar a gravação de registros iguais\.

RNG125\-ESP

__Alteração da MFS3615: __Com a criação da SAFX233 \(Cadastro dos Bens com prazo de apropriação “normal” já vencido\), o Bloco G passou a considerar tanto os Bens da APT\_AQUISICAO, como os Bens da SAFX233 *que tenham parcelas extemporâneas calculadas para o período*\. Esta regra __RNG125\-ESP__ trata *apenas* a geração dos Bens originados da SAFX233\.

Os Bens da tabela SAFX233 a serem gravados neste registro serão *apenas* aqueles que tiverem parcelas extemporâneas calculadas para o período da geração\. 

A consulta destes créditos é feita na “Tabela dos Créditos Extemporâneos \(Integral\)”\. Esta tabela é gerada no seguinte menu: “*Créditos Extemporâneos \(Integral\) à Cálculo dos Créditos*”

Para verificar a existência de valores para o período, serão utilizados os seguintes critérios:

\- Empresa                 =  código da empresa do login

\- Estabelecimento      =  código do estabelecimento em questão

\- Data da Apuração   =  data final do período de apuração 

A partir destes critérios retornarão ‘n’ linhas, referentes a cada uma das parcelas calculadas para o período\.

Para cada Bem, existirão ‘n’ linhas, uma para cada parcela calculada\. 

Todas estas parcelas são extemporâneas, e serão gravadas no registro G126\.

__Gravação do Registro G125 referente à entrada do Bem:__

Todos os Bens que tiverem parcelas calculadas, serão gravados no G125, e também terão seus dados de cadastro gravados no registro 0300, da mesma forma feita para os Bens da APT\_AQUISICAO\.  

Para estes Bens, os campos do G125 serão gerados da seguinte forma:  

  

\- COD\_INC\_BEM – campo 04 e 05 da SAFX233, utilizando a regra da concatenação \(ver RNG125\-02\);

\- DT\_MOV – campo 06 da SAFX233;

\- TIPO\_MOV \- campo 07 da SAFX233

\- VL\_IMOB\_ICMS\_OP – campo 08 da SAFX233;

\- VL\_IMOB\_ICMS\_ST – campo 09 da SAFX233;

\- VL\_IMOB\_ICMS\_FRT – campo 10 da SAFX233;

\- VL\_IMOB\_ICMS\_DIF – campo 11 da SAFX233;

\- NUM\_PARC – este campo será gravado sem informação \(“||”\);

\- VL\_PARC\_PASS – este campo será gravado sem informação \(“||”\);

__Gravação do Registro G125 referente à saída do Bem:__     \(MFS4805\)

__Alteração da MFS4805: __Além do G125 referente à entrada do Bem, a geração passou a gravar um segundo registro G125 para cada Bem, com objetivo de registrar a sua saída do controle do CIAP\.

O registro G125 da saída será gerado da seguinte forma:

1\-Para os Bens sem ocorrência de baixa:

    São os Bens em que o campo “13\-Data da Baixa” na SAFX233 *não esta preenchido*, e portanto, foi

    gerada a totalidade das parcelas\. Neste caso, será gerado um registro G125 demonstrando a saída

    do Bem por término do período de apropriação\. Este registro será gravado da seguinte forma:

    \-Tipo de Movimento = “BA”

    \-Data do Movto =  último dia do período referente à última parcela extemporânea gerada no G126;

    \-Os campos abaixo *não* serão preenchidos \(“||”\):

     \-VL\_IMOB\_ICMS\_OP

     \-VL\_IMOB\_ICMS\_ST

     \-VL\_IMOB\_ICMS\_FRT

     \-VL\_IMOB\_ICMS\_DIF

     \-NUM\_PARC

     \-VL\_PARC\_PASS 

2\-Para os Bens com ocorrência de baixa:

    São os Bens em que o campo “13\-Data da Baixa” da SAFX233 *esta preenchido*, e portanto, foram

    geradas as parcelas extemporâneas somente até o mês anterior ao da baixa\. Neste caso, será

    gerado um registro G125 demonstrando a saída do Bem, e o motivo será o tipo de movimento

    informado na SAFX233 \(campo 14\)\. Este registro será gravado da seguinte forma:

    \-Tipo de Movimento = tipo de movimento informado no campo “14\-Tipo da Movimentação da Baixa”

                                       da SAFX233 \(será  "AT", "PE" ou "OT"\)\.

    \-Data do Movto = data da baixa informada no campo “13\-Data da Baixa” da SAFX233;

    \-Os campos referentes aos valores e ao número de parcelas não serão preenchidos \(“||”\), da mesma

     forma que o caso anterior; 

      Neste caso, após gerar este G125 da saída, também serão gerados os registros de identificação da 

      nota fiscal da saída do Bem \(SAFX234\), *caso existam*\. Ver detalhes na __RNG130__\.

__OBS__: Tanto num caso como no outro, este G125 da saída será gerado ao final de todos os registros G126, e do G130/G140 referentes à NF da entrada\. Este procedimento segue a hierarquia do Bloco G\.

RNG125\-02

Campo COD\_IND\_BEM:

Preencher com a informação do código do Bem / Incorporador que consta no cadastro das aquisições \(campos 23 e 24 da APT\_AQUISICAO\)\.

A partir do movimento da APT\_DEM\_BASE\_CR, APT\_EST\_SAIDA ou APT\_ALIENACAO \(dependendo do modelo\), acessar o cadastro \(APT\_AQUISICAO\) da seguinte forma:

APT\_AQUISICAO\.COD\_EMPRESA  = COD\_EMPRESA

APT\_AQUISICAO\.COD\_ESTAB  = COD\_ESTAB ou COD\_ESTAB\_ORIG \(ver Obs abaixo sobre IEU\) 

APT\_AQUISICAO\.NUM\_CIAP  = NUM\_CIAP

= = = = 

__Obs sobre I\.E\.U\. à __Na apuração centralizada por IEU os dados do cálculo do CIAP são gravados nas tabelas em nome do centralizador \(COD\_ESTAB\), e o estabelecimento ‘dono’ do Bem é gravado no campo COD\_ESTAB\_ORIG\. Na apuração normal o COD\_ESTAB\_ORIG não é preenchido\. Logo, o critério para acessar o cadastro do Bem na APT\_AQUISICAO é o seguinte:

Se COD\_ESTAB\_ORIG <> nulo

       Utilizar o COD\_ESTAB\_ORIG;

Senão

       Utilizar o COD\_ESTAB;

= = = = 

__MFS91149__\] Readequação da regra para considerar o parâmetro “Gerar o separador “I” – Para o código de Bem / Incorporador”\.

__Parâmetro Marcado__: Se o parâmetro “*Gerar o separador “I” – Para o código de Bem / Incorporador*“, na tela de Dados Iniciais estiver __marcado__, preencher o campo conforme regra abaixo:

__Preencher__ com a concatenação do Código do Bem \+ Código do Incorporador, da seguinte forma:

                                 Código do Bem \+  “\-I”  \+  Código Incorporador

\(é a mesma forma que o Bem é gravado no registro 0200, só que não incluímos o “B” no início\)

__Parâmetro Desmarcado__: Se o parâmetro “*Gerar o separador “I” – Para o código de Bem / Incorporador*“, na tela de Dados Iniciais estiver __desmarcado__, preencher o campo conforme regra abaixo:

__Preencher __com a concatenação do Código do Bem \+ Código do Incorporador, da seguinte forma:

                                 Código do Bem \+  “\-”  \+  Código Incorporador

__*Default = marcado *__

Obs à O incorporador é opcional, e quando não existe, o campo no Mastersaf é gravado com  um caracter em branco \(pois é chave da X13\)\. Logo, quando não houver incorporador, o campo deverá ser preenchido apenas com o código do Bem, *sem fazer a concatenação*\.

 

Para cada Bem gravado no G125 deve ser gravado um registro 0300 com os seus dados cadastrais\.   

__Obs__:__ __Caso não exista a informação do código do Bem no cadastro \(APT\_AQUISICAO\), o registro G125 *não será gravado*, e será gravada mensagem de aviso no log \(msg 351 da planilha do log de erros\)\.__ __

RNG125\-03

Campo DT\_MOV:

Para as movimentações ocorridas no período, será informada a data da entrada ou saída, e para os Bens adquiridos em períodos anteriores será informada a data inicial do período, da seguinte forma:

Nos movimentos de entrada:

     Se a entrada foi em períodos anteriores \(se o campo 03\-DT\_MOV < DT\_INI do G110\)  __\(\*\*\*\)__

           Preencher com a data inicial do período \(DT\_INI do G110\)

     Senão 

           Preencher com a própria data da entrada;

__     \(\*\*\*\)__ são os Bens em que o campo 04\-TIPO\_MOV é gravado com “SI” \(ver RNG125\-04\)

     Para obter a data de entrada do Bem:

     Para o modelo C à a data de entrada é a DAT\_OPER da APT\_DEM\_BASE\_CR

     Para o modelo D à a data de entrada é a DAT\_OPER da APT\_AQUISICAO \(a partir da 

                                     APT\_EST\_SAIDA, acessar o cadastro do Bem na APT\_AQUISICAO conforme

                                     regra já descrita na RNG125\-02\)

Nos movimentos de saída:

    Para o modelo C à será a DAT\_OPER da APT\_DEM\_BASE\_CR

    Para o modelo D à será a DAT\_OPER da APT\_ALIENACAO

RNG125\-04

Campo TIPO\_MOV:

__Nos movimentos de entrada__:

Nos movimentos de entrada o preenchimento deste campo depende de vários fatores, conforme segue:

Se o Bem entrou p/o CIAP em períodos anteriores \(se o campo 03\-DT\_MOV < DT\_INI do G110\)

      Preencher com “SI”

Senão 

      A partir do código do Bem que consta no cadastro do CIAP \(campos 23 e 24 da APT\_AQUISICAO\),

      acessar a X13\_BEM\_ATIVO \(Tabela dos Bens Patrimoniais\) e verificar se o Bem é originado do

      estoque do ativo circulante, e qual o tipo do Bem:

       Se o Bem é originado do estoque \(se “Bem oriundo do Ativo Circulante” = S\) 

             Preencher com “MC”

       Senão 

             Se Tipo do Bem = 1 \(Bem\)                 à preencher com “IM”

             Se Tipo do Bem = 2 \(Componente\)     à preencher com “IA” 

             Se Tipo do Bem = 3 \(Bem Resultante\) à preencher com “CI”

             Se Tipo do Bem não informado \(=nulo\) à preencher com “IM” 

__Nos movimentos de saída__:

Nos movimentos de saída o preenchimento deste campo é feito a partir do tipo de movimento informado na saída do Bem\.

Através do tipo de movimento \(TIPO\_MOV\) que consta na APT\_DEM\_BASE\_CR \(se modelo C\) ou na APT\_ALIENACAO \(se modelo D\), recuperar o detalhamento do movimento na APT\_TIPO\_MOV \(coluna IND\_TRANSF\), e verificar:

      Se opção = Saída por Transferência \(IND\_TRANSF = S\)  à preencher com “AT”

      Se opção = Saída por Venda \(IND\_TRANSF = N\)             à preencher com “AT” 

      Se opção = Perda \(IND\_TRANSF = P\)                             à preencher com “PE”

      Se opção = Término do Período \(IND\_TRANSF = T\)      à preencher com “BA”

      Se opção = Outros \(IND\_TRANSF = O\)                         à preencher com “OT”

\(em consulta à Informação, a operação de venda deve ser atribuída a opção “Alienação” do G125\)

__OS\-2388\-E22: __

As saídas de Bens Componentes do tipo “Informativo” também devem ser demonstradas no G125\. A saída de um componente deste tipo, cuja entrada ocorreu em mês anterior ao período da escrituração \(se o campo 03\-DT\_MOV < DT\_INI do G110\), deve ser informada no período de ocorrência, com a apresentação de um registro SI e outro “AT”, “PE” ou “OT”, conforme o caso\. 

RNG125\-05

Campo VL\_IMOB\_ICMS\_OP:

Preencher apenas nos movimentos de entrada \(campo TIPO\_MOV = SI, IM, IA, MC ou CI\)\. Nas saídas, o campo fica sem informação \(‘||’\)\.

Para qualquer modelo do livro \(C/D\), este campo é preenchido com o valor do ICMS próprio que foi utilizado no cálculo do CIAP\. Trata\-se do valor original da entrada do Bem, menos as baixas parciais que possam ter sido realizadas até o período\. 

Para acessar o cadastro do Bem na APT\_AQUISICAO utilizar regra já descrita na RNG125\-02\.

Para recuperar as baixas, acessar a APT\_ALIENACAO a partir do identificador do Bem \(NUM\_CIAP\)\.

Na prática, seria:

     \(Campo “Valor ICMS” do cadastro\)  –  \(Campo “Vlr\.ICMS” das alienações com Tipo de Baixa = Parcial 

                                                                                                 e data de operação <= Data Final do período\)

                                                                        ou

          \(APT\_AQUISICAO\.VLR\_CRED\_ICMS\)  –  \(somatório do APT\_ALIENACAO\.VLR\_ICMS\_BX\)

                                                                                                              \(__\*\*\*__\)

\(__\*\*\*__\) Considerar todas as baixas parciais \(TIPO\_BAIXA = 2 ou 3\) existentes até o final do período em questão \(DAT\_OPER < = DATA\_FIM do G110\)\.  

Obs: O Guia Prático descreve este campo como sendo o valor da entrada do Bem\. No entanto, devemos considerar se já houveram baixas parciais, para utilizar exatamente o valor do saldo restante, pois o validador irá verificar se o campo 10\-VL\_PARC\_PASS é igual aos campos \(05\+06\+07\+08\) / 09\-NUM\_PARC\.

RNG125\-06

Campo VL\_IMOB\_ICMS\_ST:

Preencher apenas nos movimentos de entrada \(campo TIPO\_MOV = SI, IM, IA, MC ou CI\)\. Nas saídas, o campo fica sem informação \(‘||’\)\.

Para qualquer modelo do livro \(C/D\), este campo é preenchido com o valor do ICMS próprio que foi utilizado no cálculo do CIAP\. Trata\-se do valor original da entrada do Bem, menos as baixas parciais que possam ter sido realizadas até o período\. 

Para acessar o cadastro do Bem na APT\_AQUISICAO utilizar regra já descrita na RNG125\-02\.

Para recuperar as baixas, acessar a APT\_ALIENACAO a partir do identificador do Bem \(NUM\_CIAP\)\.

Na prática, seria:

\(Campo “Valor ICMS\-S n/Escrit” do cadastro\)  –  \(Campo “Vlr\.ICMS\-S n/Escrit” das alienações com Tipo de Baixa = 

                                                                                                  Parcial e data de operação <= Data Final do período\)

Obs: O Guia Prático descreve este campo como sendo o valor da entrada do Bem\. No entanto, devemos considerar se já houveram baixas parciais, para utilizar exatamente o valor do saldo restante, pois o validador irá verificar se o campo 10\-VL\_PARC\_PASS é igual aos campos \(05\+06\+07\+08\) / 09\-NUM\_PARC\.

RNG125\-07

Campo VL\_IMOB\_ICMS\_FRT:

Preencher apenas nos movimentos de entrada \(campo TIPO\_MOV = SI, IM, IA, MC ou CI\)\. Nas saídas, o campo fica sem informação \(‘||’\)\.

A regra de preenchimento é a mesma do campo 05\- VL\_IMOB\_ICMS\_OP, mas utilizando o campo referente ao ICMS do Frete: 

  \(Campo “Valor ICMS Frete” do cadastro\)  –  \(Campo “Vlr\.Frete” das alienações com Tipo de Baixa = Parcial 

                                                                                                      e data de operação <= Data Final do período\)

                                                                        ou

        \(APT\_AQUISICAO\.VLR\_ICMS\_FRETE\)  –  \(somatório do APT\_ALIENACAO\.VLR\_ICMS\_FRETE\_BX\)

                                                                                                                            \(__\*\*\*__\)

\(__\*\*\*__\) Considerar todas as baixas parciais \(TIPO\_BAIXA = 2 ou 3\) existentes até o final do período em questão \(DAT\_OPER < = DATA\_FIM do G110\)\.  

RNG125\-08

Campo VL\_IMOB\_ICMS\_DIF:

Preencher apenas nos movimentos de entrada \(campo TIPO\_MOV = SI, IM, IA, MC ou CI\)\. Nas saídas, o campo fica sem informação \(‘||’\)\.

A regra de preenchimento é a mesma do campo 05\- VL\_IMOB\_ICMS\_OP, mas utilizando os campos referentes ao diferencial de alíquota: 

\(Campo “Valor Dif\. Alíquota”  \+  “Valor Dif\. Alíq\. Frete” do cadastro\)  – 

\(Campo “Vlr\.Dif Aliq”  \+  “Dif Aliq Frete” das alienações c/tipo de Baixa = Parcial e data operação <= Data Final do período\)

                                                                        ou

\(APT\_AQUISICAO\.VLR\_CRED\_DIF\_ALIQ  \+  APT\_AQUISICAO\.VLR\_DIFAL\_FRETE \)  – 

\(somatório \(APT\_ALIENACAO\.VLR\_DIFAL\_BX  \+  APT\_ALIENACAO\.VLR\_DIFAL\_FRETE\_BX\)  \(__\*\*\*__\)

\(__\*\*\*__\) Considerar todas as baixas parciais \(TIPO\_BAIXA = 2 ou 3\) existentes até o final do período em questão \(DAT\_OPER < = DATA\_FIM do G110\)\.  

RNG125\-09

Campo NUM\_PARC:

Este campo é preenchido com o número da parcela calculada para o Bem\. 

Preencher apenas nos movimentos de entrada \(campo TIPO\_MOV = SI, IM, IA, MC ou CI\) , e quando existir parcela de crédito calculada no período \(a parcela calculada é <> zero\)\. Nas saídas, o campo fica sem informação \(‘||’\)\.

__Se __ \(Modelo = “C”  e  VLR\_CRED\_MENSAL da APT\_DEM\_BASE\_CR <> zeros\)  ou

       \(Modelo = “D” e VLR\_TOT\_EST\_MENSAL da APT\_EST\_SAIDA <> zeros\)

__Se __ \(Modelo = “C”  e  VLR\_PASS\_APROP \(\*\) da APT\_DEM\_BASE\_CR <> zeros\) ou 

      \(Modelo = “D”  e  VLR\_PASS\_APROP \(\*\) da APT\_EST\_SAIDA <> zeros\)

       Preencher com o número da parcela que será calculada conforme as regras descritas abaixo

__Senão__

       O campo ficará sem informação \(’||’\)

\(\*\) __OS2931\-B13 /__ __CH31587:__ Alterada a geração deste campo, que passou a utilizar a informação da nova coluna criada nas tabelas de cálculo do CIAP \(“Valor Passível de Apropriação”\) p/armazenar o valor do crédito passível de apropriação \(valor da parcela *antes de aplicar o coeficiente das saídas*\)\.

__Obs__: no caso dos bens do tipo “componente” sem direito a crédito, o campo não será preenchido \(‘||’\), pois estes bens não entram no cálculo do CIAP\.  São os Bens com status = “I” que são recuperados direto da APT\_AQUISICAO, pois não se encontram nas tabelas do cálculo \(ver detalhes na RNG125\)\.

O número de parcelas deverá ser calculado da seguinte forma:

__OS2931\-B10__: como o CIAP passou a calcular as parcelas “extemporâneas”, no caso dos Bens cadastrados no CIAP em período posterior à data fiscal da nota, o cálculo do número da parcela foi alterado para considerar estas parcelas\. Para isso, a definição foi dividida em três etapas, sendo a *Etapa I* o procedimento já feito anteriormente, e as *Etapas II e III* criadas por causa desta alteração\.

 

__ETAPA I – Verificar a quantidade de parcelas já calculadas __:

Calcular o número de parcelas já apropriadas no processo “normal” do CIAP\.

Parâmetros para o cálculo:

\-Periodicidade da apuração \(coluna IND\_PERIODIC\_102 da APT\_ESTAB, que pode ser ‘M’, ‘Q’ ‘ou ‘D’\) 

\-Data de início da apropriação dos créditos do Bem \(coluna DAT\_OPER da APT\_AQUISICAO\)

\-Data da Apuração em questão \(é a DT\_FIN gravada no G110\)

__è Se periodicidade for mensal  \(IND\_PERIODIC\_102  = ‘M’\):__

Calcular o número de meses existente entre DAT\_OPER e Data da Apuração, __incluindo__ o último mês\.

Exemplo:  entre as datas 01/JAN/2000 e 31/OUT/2000 o resultado deve ser = 10\.        

                 entre as datas 20/10/2000 e 30/04/2002 deve ser = 19\.

__è Se periodicidade for quinzenal  \(IND\_PERIODIC\_102  = ‘Q’\):__

Passo 1 à verificar o número de quinzenas que faltam para completar o mês da data de apuração\. P/ isso, deve\-se testar qual o dia da data de apuração \(vide ex\)\.   

Passo 2 à calcular o número de meses existente entre DAT\_OPER e Data da Apuração, da mesma forma feita para a periodicidade mensal\. 

Passo 3 à o número encontrado deve ser multiplicado por 2 para se transformar no número de quinzenas\.

Passo 4 à subtrair do número de quinzenas encontrado, o número de quinzenas que falta para completar o mês da data de apuração\. 

EXEMPLO:

Passo 1:    Se dia = 15

                       Num\_falta\_aux  = 1

                  Senão

                       Num\_falta\_aux = 0\.            

Passo 2:    Num\_meses\_aux        = Data Apuração  – DATA\_OPER

Passo 3:    Num\_quinzenas\_aux  = Num\_meses\_aux  \*  2

Passo 4:    Resultado                    =  Num\_quinzenas\_aux  –  Num\_falta\_aux

__è Se periodicidade for decendial  \(IND\_PERIODIC\_102  = ‘D’\):__

 Passo 1 à verificar o número de decendios que faltam para completar o mês da data de apuração\. P/ isso, deve\-se testar qual o dia da data de apuração \(vide ex\)\.

   

Passo 2 à calcular o número de meses existente entre DAT\_OPER e Data de Apuração,  da mesma forma feita para a periodicidade mensal\. 

Passo 3 à o número encontrado deve ser multiplicado por 3 para se transformar no número de decendios\.

Passo 4à subtrair do número de decendios encontrado, o número de decendios que falta para completar o mês da data de referência\.

EXEMPLO:

Passo1:      Se dia = 10

                         Num\_falta\_aux  = 2

                   Senão

                         Se dia = 20

                               Num\_falta\_aux  = 1

                         Senão

                                Num\_falta\_aux = 0\.            

Passo 2:     Num\_meses\_aux        = Data Apuração  –  DATA\_OPER

Passo 3:     Num\_decendios\_aux  = Num\_meses\_aux  \*  3

Passo 4:     Resultado                    =  Num\_decendios\_aux  –  Num\_falta\_aux

Observações:

- Este cálculo *já é feito* no livro Modelo C do RJ, e foi definido na OS500, quando o livro foi desenvolvido \(OS500, item “Procedimentos p/Produção”, item \(2\), parágrafo “Como calcular o número da parcela”\)\. A informação é armazenada na coluna PARCELA da tabela APT\_DEM\_BASE\_CR\. Para os demais formatos do Modelo C esta coluna não é preenchida, e quanto ao Modelo D, não existe nem a coluna PARCELA na tabela, pois nenhum dos formatos de livro tem esta informação\.

__ETAPA II – Verificar a existência de parcelas extemporâneas__:

Verificar se existem parcelas extemporâneas para o Bem\. Pesquisar na tabela que armazena os dados dos créditos extemporâneos se existem registros para o Bem, de acordo com os critérios a seguir:

*Empresa                     =  código da empresa*

*Estabelecimento         =  código do estabelecimento*

*Data da Apuração      =  data da apuração*

*Identificador do CIAP = identificador do Bem \(NUM\_CIAP\)*

O número de parcelas extemporâneas será exatamente o número de linhas encontradas\.

__OS3114\-E__: No caso da geração do Bloco G por inscrição estadual do PIM, deve ser utilizada a tabela específica do cálculo realizado por IE\-PIM, e a IE deve ser incluída no filtro p/a recuperação dos dados\.

__ETAPA III – Calcular o total de parcelas calculadas__:

Para obter o número da parcela do período, somar a quantidade de parcelas apurada na Etapa II ao número da parcelas calculado na Etapa I\.

RNG125\-10

Campo VL\_PARC\_PASS:

Preencher apenas nos movimentos de entrada \(campo TIPO\_MOV = SI, IM, IA, MC ou CI\), e quando existir parcela de crédito calculada no período \(a parcela calculada é <> zero\)\. Nas saídas, o campo fica sem informação \(‘||’\)\.

	

Este campo é o valor da parcela *antes de aplicar o coeficiente das saídas tributadas*\. 

__Se __ \(Modelo = “C”  e  VLR\_CRED\_MENSAL da APT\_DEM\_BASE\_CR <> zeros\)  ou

       \(Modelo = “D” e VLR\_TOT\_EST\_MENSAL da APT\_EST\_SAIDA <> zeros\)

__Se __ \(Modelo – “C”  e  VLR\_PASS\_APROP \(\*\) da APT\_DEM\_BASE\_CR <> zeros\) ou 

      \(Modelo –  “D”  e  VLR\_PASS\_APROP \(\*\) da APT\_EST\_SAIDA <> zeros\)

      __Se Modelo = “C”__

            Preencher com o conteúdo da nova coluna VLR\_PASS\_APROP \(\*\) da APT\_DEM\_BASE\_CR

      __Se Modelo = “D”__

           Preencher com o conteúdo do nova coluna VLR\_PASS\_APROP \(\*\) da APT\_EST\_SAIDA

__Senão__

       O campo ficará sem informação \(’||’\)\.

\(\*\) __OS2931\-B13 /__ __CH31587:__ Alterada a geração deste campo, que passou a utilizar a informação da nova coluna criada nas tabelas de cálculo do CIAP \(“Valor Passível de Apropriação”\) p/armazenar o valor do crédito passível de apropriação \(valor da parcela *antes de aplicar o coeficiente das saídas*\)\.

__Obs__: No caso dos bens do tipo “componente” sem direito a crédito, o campo não será preenchido \(‘||’\), pois estes bens não entram no cálculo do CIAP\.  São os Bens com status = “I” que são recuperados direto da APT\_AQUISICAO, pois não se encontram nas tabelas do cálculo \(ver detalhes na RNG125\)\.

__Registro G126 – Outros  Créditos do CIAP__

RNG126

Este registro é “filho” do G125, e nele serão gravadas as parcelas de crédito extemporâneas que possam ter sido calculadas *no período* para o Bem gravado no G125\.

__Alteração da MFS3615: __Com a criação da SAFX233 \(Cadastro dos Bens com prazo de apropriação “normal” já vencido\), o Bloco G passou a considerar tanto os Bens da APT\_AQUISICAO, como os Bens da SAFX233 *que tenham parcelas extemporâneas calculadas para o período*\. Com isso, a geração do registro G126 passou a ter regras diferenciadas, dependendo se o Bem gravado no G125 é originado da APT\_AQUISICAO ou SAFX233, da seguinte forma:

__No caso dos Bens originados da APT\_AQUISICAO:__

 

Origem dos dados: Tabela dos Créditos Extemporâneos 

\(esta tabela é carregada durante o processo do cálculo dos créditos extemporâneos\)

Critérios para recuperação dos dados na tabela dos créditos extemporâneos:

Empresa                    = código da empresa informante

Estabelecimento        = código do Estabelecimento informante

Data de Apuração      = data da apuração em questão \(é a DT\_FIN gravada no G110\)

Identificador do CIAP  = identificador do Bem gravado no G125 \(NUM\_CIAP\)

Observar que num mesmo período poderão existir várias parcelas de crédito extemporâneas calculadas para um mesmo Bem\. Por isso, a pesquisa poderá retornar várias linhas\. Para cada uma, será gerado um registro G126\.

OBS: Quando o registro “pai” G125 for o resultado de uma consolidação de várias aquisições, os créditos extemporâneos também serão consolidados \(ver regras da consolidação na RNG125\)\.

__OS3114\-E__: No caso da geração do Bloco G por inscrição estadual do PIM, deve ser utilizada a tabela específica do cálculo realizado por IE\-PIM, e a IE deve ser incluída no filtro p/a recuperação dos dados\.

= = = = =

__No caso dos Bens originados da SAFX233:__

Origem dos dados: Tabela dos Créditos Extemporâneos da opção “Integral”

\(esta tabela é carregada durante o processo do cálculo dos créditos extemporâneos do menu “Integral”\)

Critérios para recuperação dos dados na tabela dos créditos extemporâneos:

Empresa                      = código da empresa informante

Estabelecimento          = código do Estabelecimento informante

Data de Apuração        = data da apuração em questão \(é a DT\_FIN gravada no G110\)

Código do Bem            = código do Bem gravado no G125

Código do Incorporador = código do incorporador do Bem gravado no G125

Observar que num mesmo período poderão existir várias parcelas de crédito extemporâneas calculadas para um mesmo Bem\. Por isso, a pesquisa poderá retornar várias linhas\. 

Para cada parcela, será gerado um G126 com as seguintes informações originadas da tabela do cálculo:

\- DT\_INI – campo “Data Inicial do Período da Parcela”;

\- DT\_FIM – campo “Data Final do Período da Parcela”;

\- NUM\_PARC \- campo “Número da Parcela”;

 \- VL\_PARC\_PASS – campo “Valor da Parcela Passível de Apropriação”;

\- VL\_TRIB\_OC – campo “Valor Total das Saídas Tributadas do Período”;

\- VL\_TOTAL – campo “Valor Total das Saídas do Período”;

\- IND\_PER\_SAI – este campo será gravado com o seguinte resultado, calculado com 8 casas decimais:

             Valor Total das Saídas Tributadas do Período / Valor Total das Saídas do Período

                                  \(VL\_TRIB\_OC\)                                          \( VL\_TOTAL\)

\- VL\_PARC\_APROR – campo “Valor da Parcela”;

= = = = =

RNG126\-08

Campo IND\_PER\_SAI

Este valor representa o índice de participação das saídas tributadas/exportação sobre o valor total das saídas do período, e deve ser preenchido com o seguinte conteúdo: 

                        \( campo 06\-VL\_TRIB\_OC  /  campo 07\-VL\_TOTAL \)

A partir da OS2388\-E23, este cálculo passou a ser feito considerando 8 casas decimais\.

__Registro G130 – Identificação do Documento Fiscal__

RNG130

Neste registro são gravadas as informações da nota fiscal referente ao movimento gravado no registro G125\. 

__Alteração da MFS3615: __Com a criação da SAFX233 \(Cadastro dos Bens com prazo de apropriação “normal” já vencido\), o Bloco G passou a considerar tanto os Bens da APT\_AQUISICAO, como os Bens da SAFX233 *que tenham parcelas extemporâneas calculadas para o período*\. Com isso, a geração do registro G126 passou a ter regras diferenciadas, dependendo se o Bem gravado no G125 é originado da APT\_AQUISICAO ou SAFX233, da seguinte forma:

__No caso dos Bens originados da APT\_AQUISICAO:__

__Se Tipo de Movimento do G125 = BA:__

     Nos casos em que o G125 for um movimento de saída do tipo “BA” \(Término de 

     Apropriação\), os registros G130 e G140 *não devem ser gerados*\.

__Se Tipo de Movimento do G125 = CI:__

\[__CH13043\_2015__\] \[CH20668\_2018\]

Nos casos em que o G125 for um movimento de entrada tipo “CI” \(entrada de Bens Resultantes\), os registros G130 e G140 não devem ser gerados, ou seja, serão gerados com base as NFs registradas nos componentes associados ao bem resultante que entrarem no mesmo período de escrituração\.

Para identificar quais são os componentes associados ao bem resultante, basta procurar na SAFX13 – Arquivo de Cadastro de Bem os bens cujo Tipo do Bem \(campo 34 \- TIPO\_BEM\) seja igual a 2 – Componente e que tenham na identificação do bem origem \(campos 16 \+ 17, COD\_BEM\_ORIG e COD\_INC\_ORIG\) o código do bem resultante que está sendo demonstrado no arquivo\. As informações das NFs serão obtidas da SAFX82 \- Arquivo Bens do Ativo Permanente – CIAP destes componentes\.

__Se Demais Tipos: __

     A origem dos dados dependerá se o movimento do G125 for entrada ou saída:

     Se __entrada__ à os dados devem ser recuperados do cadastro das aquisições 

                             \(__APT\_AQUISICAO__\)

     Se __saída__ à os dados devem ser recuperados do cadastro das alienações

                         \(__APT\_ALIENACAO__\)

     Algumas informações, como o número da nota por exemplo, já existem nas tabelas do cálculo \(APT\_DEM\_BASE\_CR e APT\_EST\_SAIDA\), no entanto, o Sped solicita várias outras informações,  inclusive campos novos que foram incluídos nos cadastros do CIAP\.

Crítica da existência do documento fiscal:

Caso não exista a informação do documento fiscal \(seja na APT\_AQUISICAO ou na APT\_ALIENACAO\), o registro G130 *não será gravado*, e neste caso será gravada mensagem de aviso no log \(msg 354 da planilha do log de erros\) somente para os movimentos que o PVA exige a informação da nota fiscal, que são os movimentos “IM”, “MC”, “IA”, “CI” e “AT” \(conforme a versão 17\.0\.21 do validador\)\.

__Movimento__

__Obrigatoriedade do G130 __

__Obrigatoriedade Geração Especial__

SI

__Não__

Sim \(vide OBS2\)

IM

Sim

Sim

MC

Sim

Sim

IA

Sim

Sim

CI

__Não Sim__

Sim

BA

Não \(a regra é não gerar G130/G140\) 

Não

AT

Sim

Sim

PE

__Não__

Não

OT

__Não__

Não

OBS1: Quando o registro “pai” G125 for o resultado de uma consolidação de várias aquisições, os documentos fiscais e seus itens \(G130 e G140\) também serão agrupados para evitar a duplicidade de informações \(ver regras da consolidação na RNG125\)\.

\[__CH4543\_2015__\]

OBS2: Quando se tratar da geração através da tela de geração especial as informações de documentos fiscais e seus itens \(G130 e G140\) serão geradas conforme tabela acima que descreve Tipo de Movimento X Obrigatoriedade\. Para o registro com tipo “SI”, serão demonstradas as notas dos bens conforme registrado na SAFX82 \- Arquivo Bens do Ativo Permanente – CIAP destes componentes\. Se for um “SI” oriundo de um “CI”, serão demonstradas as NFs dos componentes, conforme regra específica do “CI”\.

\[__Alteração CH104481__\]

Quando o tipo de movimento for igual a perda, ou seja, movimento = PE, então não gerar o registro G130

__No caso dos Bens originados da SAFX233:__

__Alteração da MFS4805__: Incluído o campo “*16\-Indicador Entrada/Saída*” na SAFX234, que passará a indicar se a nota fiscal se refere à entrada ou à saída do Bem\.

Nesse caso as informações das notas fiscais e itens relacionados ao Bem gravado no G125 serão recuperadas da tabela __SAFX234__, a partir dos seguintes critérios:

Notas referentes à __entrada__ do Bem \(qdo o registro “pai” G125 for um movto de __entrada__\):

   \-Empresa = código da empresa informante

   \-Estabelecimento = código do Estabelecimento informante

   \-Data de Apuração = data da apuração em questão \(é a DT\_FIN gravada no

    G110\)

   \-Código do Bem = código do Bem gravado no G125

   \-Código do Incorporador = código do incorporador do Bem gravado no G125

   \-Indicador E/S = “__E__”        \(alteração da __MFS4805__\)

Para um único Bem poderão retornar várias linhas da tabela, o que dependerá da quantidade de itens associados ao Bem\. A chave desta tabela considera a *nota* e também o número do item, sendo assim, poderá existir uma ou mais notas associadas ao Bem, assim como um ou mais itens *de uma mesma nota*\. Observar também que o item é obrigatório\.

Para cada nota associada ao Bem será gerado um G130 com as seguintes informações, originadas da tabela SAFX234 e da SAFX04:

\- IND\_EMIT – se nota de terceiros, será gravado “1”, senão, será gravado “0” \(ver __OBS__\); 

\- COD\_PART – código de identificação da pessoa fis/jur informada nos campos 06 e 07 da

   SAFX234, considerando a mesma regra de concatenação descrita na RNG130\-03\. Os

   dados cadastrais da pessoa fis/jur serão gravados no registro 0150, seguindo a regra geral

   de todos os registros do Sped;

\- COD\_MOD \- campo “12\-Modelo do Documento” da SAFX234;

\- SERIE – campo “09\-Serie do Documento” da SAFX234;

\- NUM\_DOC – campo “08\-Numero do Documento” da SAFX234;

\- CHV\_NFE\_CTE – campo “13\-Chave da NFe” da SAFX234; 

\- DT\_DOC – campo “10\-Data de Emissão” da SAFX234;

__\[MFS31420\]__

\- NUM\_DA – campo “17\-Número do Documento de Arrecadação” da SAFX234;

__OBS:__ Para verificar se a nota é de emissão própria ou de terceiros, será verificado se a pessoa fis/jur consta na parametrização “Estabelecimentos x Pessoa Fis/Jur” \(Módulo DW\) associada ao código do estabelecimento\. Caso sim, considerar emissão própria, caso não, considerar emissão de terceiros\. 

Notas referentes à __saída__ do Bem \(qdo o registro “pai” G125 for um movto de __saída__\):

As regras de recuperação e gravação dos dados são as mesmas das notas de entrada, a única diferença é na questão do indicador da SAFX234, que será = “Saídas”:

   \-Indicador E/S = “__S__”        \(alteração da __MFS4805__\)

 

*OBS: Para as saídas do tipo “BA” não existirá a nota de saída\. Para os demais tipos \(AT, PE e OT\), pode existir ou não \(pelo Guia Prático é obrigatório apenas para o tipo “AT”\)\.*

RNG130\-02

Campo IND\_EMIT:

__Nos movimentos de entrada__:

Preencher de acordo com o campo “39\-Movimento Entrada/Saída” da APT\_AQUISICAO:

     Se MOVTO\_E\_S = ‘1’

          Gravar 1 \(documento de terceiros\)

     Senão

          Gravar 0 \(documento de emissão própria\)

__Nos movimentos de saída__:

      Gravar 0 \(documento de emissão própria\)

Exceto: Quando Notas Fiscais Eletrônicas – NF\-e, modelo 55, emitidas com inscrição estadual única e CNPJs dos demais estabelecimentos pelo contribuinte quando indicado no § 2º\-A do art\. 4º, sempre gravar com “1” \(emissão terceiros\)\. 

Obs\.: Na geração por Inscrição Estadual Única, deve\-se considerar os documentos fiscais de todos os Estabelecimentos envolvidos na centralização \- RNG110\)\.

RNG130\-03

Campo COD\_PART

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RNG130\-04

Campo COD\_MOD:

__Nos movimentos de entrada__:

Preencher com o conteúdo do “Código Modelo NF” da APT\_AQUISICAO \(novo campo criado na SAFX82 pela OS2931\-B\)\.

__Nos movimentos de saída__ :

A partir do campo “Modelo Documento” \(campo 10\) da APT\_ALIENACAO, acessar a tabela dos modelos de documento do CIAP \(APT\_MODELO\_DOCTO\)\. Esta tabela tem o campo “Modelo Doc \(SAFX2024\)”, que é o código oficial do modelo, e que deverá ser gravado neste campo\. 

__RNG130\-05__

Campo 05\-SERIE:

__\[ALTERADA – CH3435\_2016\]__

Se no documento fiscal o campo 04\-COD\_MOD for igual a “55” \(origem campo “Código Modelo NF” da APT\_AQUISICAO/campo “10\-Modelo Documento” da APT\_ALIENACAO = 55\), considerar as três posições do campo “SERIE\_DOCFIS da APT\_AQUISICAO/APT\_ALIENACAO”, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchido preencher com zeros \(gravar = 000\)\.

Para os demais modelos de documento caso o série não estiver preenchida deixar o campo sem preenchimento \(gravar ||\) 

RNG130\-07

Campo CHV\_NFE\_CTE:

__Nos movimentos de entrada__:

\(__CH13043\-B/2015\)__ 

Preencher com o conteúdo do campo “53\-Chave Nfe” da APT\_AQUISICAO, somente quando o campo 02 \- IND\_EMIT for igual “0” \(documento de emissão própria\), ou seja, o campo MOVTO\_E\_S diferente de “1” da tabela APT\_AQUISICAO\.

__Nos movimentos de saída__:

Preencher com o conteúdo do “32\-Chave Nfe” da APT\_ALIENACAO\. 

RNG130\-09

Campo NUM\_DA:

__\[MFS31420\]__

__Nos movimentos de entrada__:

 

Preencher com o conteúdo do campo “61\-Número do Documento de Arrecadação” da APT\_AQUISICAO\.

__Nos movimentos de saída__:

Não preencher\. 

__Registro G140 – Identificação do Item do Documento Fiscal__

RNG140

Neste registro são gravadas as informações do item da nota fiscal gravada no registro G130\. 

__Alteração da MFS3615: __Com a criação da SAFX233 \(Cadastro dos Bens com prazo de apropriação “normal” já vencido\), o Bloco G passou a considerar tanto os Bens da APT\_AQUISICAO, como os Bens da SAFX233 *que tenham parcelas extemporâneas calculadas para o período*\. Com isso, a geração do registro G140 passou a ter regras diferenciadas, dependendo se o Bem gravado no G125 é originado da APT\_AQUISICAO ou SAFX233, da seguinte forma:

= = = = =

__No caso dos Bens originados da APT\_AQUISICAO:__

A origem dos dados é a mesma do registro G130, dependendo se for uma entrada ou uma saída:

Se __entrada__ à os dados devem ser recuperados do cadastro das aquisições \(__APT\_AQUISICAO__\)

Se __saída__ à os dados devem ser recuperados do cadastro das alienações \(__APT\_ALIENACAO__\)

__Obs__:__ __Caso não exista a informação do número do item na *SAFX82 ou SAFX83*, o registro G140 *não será gravado*, e será gravada mensagem de aviso no log \(msg 356 da planilha do log de erros\)\.

OBS: Quando o registro “pai” G125 for o resultado de uma consolidação de várias aquisições, os documentos fiscais e seus itens \(G130 e G140\) também serão agrupados para evitar a duplicidade de informações \(ver regras da consolidação na RNG125\)\.

= = = = =

__No caso dos Bens originados da SAFX233:__

Nesse caso as informações do item serão recuperadas da tabela __SAFX234__, considerando a nota gravada no registro G130\.

Para cada item associado a nota gravada no G130 será gerado um G140, com as seguintes informações, originadas da tabela SAFX234 e da SAFX2013:

\- NUM\_ITEM – campo “11\-Número do Item” da SAFX234;

\- COD\_ITEM – código de identificação do produto informado nos campos 14 e 15 da SAFX234, seguindo o mesmo padrão do registro 0200 \(utilizando o parâmetro “Considerar o indicador no código do item”, conforme descrito na RN0200\-02\);

Os dados cadastrais do produto serão gravados no registro 0200, seguindo a regra geral de todos os registros do Sped;

__\[MFS31420\]__

\- QTDE – campo “18\-Quantidade” da SAFX234;

\- UNID – campo “19\-Unidade de Medida” da SAFX234;

Os dados cadastrais da unidade de medida serão gravados no registro 0190, seguindo a regra geral de todos os registros do Sped;

\- VL\_ICMS\_OP\_APLICADO – campo “19\-Valor ICMS” da SAFX234;

\- VL\_ICMS\_ST\_APLICADO – campo “20\-Valor ICMS\-ST” da SAFX234;

\- VL\_ICMS\_FRT\_APLICADO – campo “21\-Valor ICMS Frete” da SAFX234;

\- VL\_ICMS\_DIF\_APLICADO – campo “22\-Valor ICMS Dif\. Aliq” da SAFX234;

RNG140\-03

Campo COD\_ITEM:

__Nos movimentos de entrada__:

Preencher com a informação do produto da APT\_AQUISICAO, seguindo o mesmo padrão do registro 0200/C170 \(utilizando o parâmetro “Considerar o indicador no código do item”, conforme descrito na RN0200\-02\);

__Nos movimentos de saída__ :

Preencher com a informação do produto da APT\_ALIENACAO, seguindo o mesmo padrão do registro 0200/C170 \(utilizando o parâmetro “Considerar o indicador no código do item”\);

O produto / Bem gravado neste campo será gravado no Bloco 0, registro 0200\.

__Caso o produto não esteja preenchido__:

Se os campos do indicador e código  do produto não estiverem preenchidos, seja no movimento de entrada ou de saída \(na APT\_AQUISICAO ou na APT\_ALIENACAO\),  deverá ser gravado o código do Bem da APT\_AQUISICAO, seguindo o mesmo padrão dos registros 0200/ C170 /  \(utilizando o parâmetro “Considerar o indicador no código do item”, conforme descrito na RN0200\-02\);

= = = = =

O produto / Bem gravado neste campo será gravado no Bloco 0, registro 0200\.

__\[MFS\-84519\]__ Tratamento do novo parâmetro para indicar a forma de preenchimento do campo 06 \- UNID\_INV do registro 0200\. Esse parâmetro somente será utilizado quando se tratar de um código de Bem no campo 02 \- COD\_ITEM do registro 0200, que seja oriundo da geração do registro G140 \- bloco G \(CIAP\)\. 

__Obs__\.: Quando o código do item gravado for um Bem, deve\-se utilizar a unidade de medida \(campo 05 \- UNID\) deste registro, para preencher o campo 06 \- UNID\_INV do registro 0200\.  Para maiores detalhes, consultar a RN0200\-06 do documento Sped\_Fiscal\_Regras\_Bloco\_0\.docx\.

RNG140\-04

Campo QTDE:

__\[MFS31420\] Alterada pela \[MFS34966\]__

__Nos movimentos de entrada e de saída__:

Preencher com o conteúdo do campo “28\-Quantidade de Bens” da APT\_AQUISICAO\.

__Nos movimentos de saída__:

Não preencher\.

RNG140\-05

Campo UNID:

__\[MFS31420\] Alterada pela \[MFS34966\]__

__Nos movimentos de entrada e de saída__:

Preencher com o conteúdo do campo “60\-Unidade de Medida” da APT\_AQUISICAO\.

__Nos movimentos de saída__:

Não preencher\.

A unidade de medida gravada neste campo será gravada no Bloco 0, registro 0190\.

RNG140\-06

Campo VL\_ICMS\_OP\_APLICADO:

__\[MFS31420\] Alterada pela \[MFS34966\]__

__Nos movimentos de entrada e de saída__:

Preencher com o conteúdo do campo “20\-Valor ICMS” da APT\_AQUISICAO\.

__Nos movimentos de saída__:

Não preencher\.

__\[MFS34318\] __

__Obs\.:__ Quando não houver valor, preencher com zero\.

RNG140\-07

Campo VL\_ICMS\_ST\_APLICADO:

__\[MFS31420\] Alterada pela \[MFS34966\]__

__Nos movimentos de entrada e de saída__:

Preencher com o conteúdo do campo “57\-ICMS ST Não Escriturado” da APT\_AQUISICAO\.

__Nos movimentos de saída__:

Não preencher\.

__\[MFS34318\] __

__Obs\.:__ Quando não houver valor, preencher com zero\.

RNG140\-08

Campo VL\_ICMS\_FRT\_APLICADO:

__\[MFS31420\] Alterada pela \[MFS34966\]__

__Nos movimentos de entrada e de saída__:

Preencher com o conteúdo do campo “45\-Valor do ICMS Frete” da APT\_AQUISICAO\.

__Nos movimentos de saída__:

Não preencher\.

__\[MFS34318\] __

__Obs\.:__ Quando não houver valor, preencher com zero\.

RNG140\-09

Campo VL\_ICMS\_DIF\_APLICADO:

__\[MFS31420\] Alterada pela \[MFS34966\]__

__\[MFS33434\]__

__Nos movimentos de entrada e de saída__:

Preencher com o conteúdo do campo “35\-Valor do ICMS Diferencial de Alíquota”” \+ “46\-Valor do ICMS Dif\. Alíquota Frete” da APT\_AQUISICAO\.

__Nos movimentos de saída__:

Não preencher\.

__\[MFS34318\] __

__Obs\.:__ Quando não houver valor, preencher com zero\.

