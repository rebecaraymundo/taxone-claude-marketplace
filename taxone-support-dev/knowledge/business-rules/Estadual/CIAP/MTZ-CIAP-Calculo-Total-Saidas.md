# MTZ-CIAP-Calculo-Total-Saidas

- **Fonte:** MTZ-CIAP-Calculo-Total-Saidas.docx
- **Modificado:** 2021-08-28
- **Tamanho:** 92 KB

---

THOMSON REUTERS

Módulo CIAP

Cálculo do Total Geral das Saídas e Saídas Tributadas

<a id="OLE_LINK1"></a>__Localização__: 

Menu Estadual, módulo Ativo Permanente, menu Movimento à Cálculo do Crédito \- ICMS 

Menu Estadual, módulo Ativo Permanente, menu Movimento à Cálculo do Crédito \- ICMS p/Inscrição Estadual Única

Menu Estadual, módulo Ativo Permanente, menu Movimento à Cálculo do Crédito \- ICMS p/ Inscrição Estadual PIM

<a id="OLE_LINK9"></a>A apuração do total das saídas do período é feita para calcular o Fator de Cálculo do CIAP \(= Saídas Tributadas / Total das Saídas\)\. Este procedimento é realizado nos três menus de cálculo do CIAP: o “normal”, o cálculo por Inscrição Estadual Única e o cálculo por Inscrição Estadual do AM \(PIM\)\. 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__\(documentação\)__

Apuração do total das operações de saída 

Apuração do total geral das saídas e total das saídas tributadas, para cálculo do Fator de Cálculo do CIAP 

24/05/2018 

\(criação do documento\)

MFS18604

Decreto 9\.192 Sefaz PR \(05/04/2018\)

Alteração na parametrização específica das saídas tributadas p/o usuário indicar os valores da nota a serem considerados para cada CFOP ou CFOP/Natureza parametrizado \(ver item 4\-Processamento das Saídas Tributadas\)\.

28/05/2018

MFS14391

Novo parâmetro 

Novo parâmetro para o cálculo do valor total das saídas \(ver itens 1, 2 e 3\)\.

11/02/2019

MFS15006

Atendimento ao RS

Considerar as opções de Valores para Totalização criadas nas parametrizações p/ Cálculo do Total das Operações de Saídas/Devoluções \(ver item 3 – Processamento do Total Geral das Saídas\)\.

27/08/2021

Sumário

[1\.	Regra Geral	2](#_Toc514939188)

[2\.	Parâmetros Utilizados na Totalização das Saídas	3](#_Toc514939189)

[3\.	Processamento – Total Geral das Saídas	7](#_Toc514939190)

[4\.	Processamento – Total das Saídas Tributadas	7](#_Toc514939191)

# <a id="_Toc514939188"></a><a id="OLE_LINK34"></a>Regra Geral 

A apuração do valor total das saídas do período é feita para calcular o Fator de Cálculo do CIAP \(= Saídas Tributadas / Total das Saídas\)\. Para isso, é feita a apuração de dois totais:

<a id="OLE_LINK35"></a>     \- Valor total das saídas do período;

     \- Valor total das saídas tributadas do período;

Este procedimento é chamado pelos três menus de cálculo do CIAP:

<a id="OLE_LINK10"></a>\- <a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>Cálculo do Crédito – ICMS

\- Cálculo do Crédito – ICMS <a id="OLE_LINK14"></a><a id="OLE_LINK15"></a>p/ Inscrição Estadual Única 

\- Cálculo do Crédito – ICMS <a id="OLE_LINK16"></a><a id="OLE_LINK17"></a><a id="OLE_LINK24"></a>p/ Inscrição Estadual – PIM

 A diferença entre eles são as seguintes:

   1\-Recuperação das notas a serem consideradas na totalização, conforme o quadro abaixo:

<a id="OLE_LINK25"></a><a id="OLE_LINK26"></a><a id="_Hlk514925732"></a>Cálculo do Crédito – ICMS 

<a id="OLE_LINK29"></a><a id="OLE_LINK30"></a><a id="OLE_LINK31"></a>Considera apenas as notas do estabelecimento selecionado para o cálculo do CIAP

Cálculo do Crédito – ICMS p/ IEU

Considera as notas de todos os estabelecimentos envolvidos na centralização por IEU: o centralizador \(estabelecimento selecionado em tela\) e os centralizados; 

Cálculo do Crédito – ICMS p/ IE \- PIM

Considera apenas as notas do estabelecimento e inscrição estadual selecionados para o cálculo do CIAP \(lembrando que nesse caso, o usuário já seleciona em tela o estabelecimento \+ I\.E\. do PIM\);

   2\-Utilização do parâmetro “Parâmetros Específicos p/Apuração do Total das Saídas”\.

__MFS14391__: Criado parâmetro para o cálculo do Valor Total das Saídas \(campo “Parâmetros Específicos p/ Apuração do Total das Saídas”\), que permite ao usuário deduzir o valor do ICMS\-ST do valor contábil na apuração do total das saídas do período\. O parâmetro foi criado apenas na tela do cálculo “normal” \(o cálculo da I\.E\.U\. e do PIM não foram alterados\), e se refere somente ao cálculo do total geral das saídas \(vide item “3\-Processamento\-Total Geral das Saídas”\)\.

__MFS15006__: O parâmetro que foi criado pela __MFS14391 __apenas no cálculo “normal”, através da __MFS15006__ foi replicado para os cálculos p/ IEU e IE \- PIM\. Com a MFS15006, os __Parâmetros Específicos p/ Apuração do Total das Saídas __passam a ficar habilitados apenas quando o campo “Utiliza parametrização p/ Total de Saídas” existente na tela, estiver desmarcado\. Isso porque quando estiver marcado, as opções de valores utilizadas no cálculo proverão das parametrizações p/ Cálculo do Total das Operações de Saídas/Devoluções, vide menu Cadastro >> Parâmetros p/ Cálculo do Total das Operações de Saídas/Devoluções >> por CFOP e por Extensão CFOP

# <a id="_Toc514939189"></a>Parâmetros Utilizados na Totalização das Saídas 

Para a totalização das notas são utilizados os seguintes parâmetros:

<a id="OLE_LINK36"></a>\- __Parametrização p/ Cálculo do Total das Operações de Saída / Devoluções \(por CFOP e CFOP/NAT\)__

<a id="OLE_LINK58"></a>   O objetivo desta parametrização é definir quais operações de saída serão consideradas para o total geral das saídas\.

   Também podem ser definidas as operações de entrada \(devoluções\) a serem descontadas do total apurado\.

   Esta parametrização é utilizada apenas quando o parâmetro “*Utiliza parametrização p/ Total de Saídas*” \(tela do Cálculo do Crédito\) 

   estiver marcado\. Caso contrário, serão consideradas todas as saídas e todas as devoluções\.

<a id="OLE_LINK37"></a>\- __Parametrização p/ Cálculo das Operações de Saídas Tributadas / Devoluções \(por CFOP e CFOP/NAT\)__

   O objetivo desta parametrização é definir quais operações de saída serão consideradas para o total das saídas tributadas\.

   Também podem ser definidas as operações de entrada \(devoluções\) a serem descontadas do total apurado\.

   Esta parametrização é utilizada apenas quando o parâmetro “*Utiliza parametrização p/ Saídas Tributadas*” \(tela do Cálculo do Crédito\) 

   estiver marcado\. Caso contrário, serão consideradas todas as saídas e todas as devoluções com valor na Base de Cálculo do ICMS

  \(exceto as exportações, que serão sempre consideradas, independente da base de cálculo\)\.

\- __Parametrização Específica p/ Cálculo das Operações de Saídas Tributadas \(por UF, CFOP e CFOP/NAT\)__  \(MFS4302, Ch497/16\)

   O objetivo desta parametrização é fazer com que determinadas operações isentas/não tributadas \(sem base de cálculo\), sejam 

   consideradas para o total das saídas tributadas\.  Ao totalizar estas operações, o campo utilizado é __sempre__ o *valor contábil\. *  

   Esta parametrização é utilizada __apenas__ quando o parâmetro “*Valor da Base de Cálculo*” \(campo “Opção de valor a ser utilizada” da

   tela do Cálculo do Crédito\) estiver marcado \(indicando que as operações tributadas serão totalizadas pelo valor da base de cálculo\)\. 

<a id="OLE_LINK38"></a>\- __Utiliza parametrização p/ Total de Saídas__ <a id="OLE_LINK39"></a><a id="OLE_LINK40"></a><a id="OLE_LINK41"></a>\(tela do cálculo\)

<a id="OLE_LINK63"></a>   O objetivo deste parâmetro é indicar se ao recuperar as notas de saída, a parametrização “Parametrização p/ Cálculo do Total das Operações 

   de Saída” será ou não utilizada\.

   Quando marcado, serão consideradas apenas as operações com CFOP ou CFOP/NAT parametrizado\.

   Quando desmarcado, serão consideradas todas as operações\. 

 

\- __Utiliza parametrização p/ Saídas Tributadas__ \(tela do cálculo\)

  O objetivo deste parâmetro é indicar se ao recuperar as notas de saída tributadas, a parametrização “Parametrização p/ Cálculo das 

  Operações de Saída Tributadas” será ou não utilizada\.

   Quando marcado, serão consideradas apenas as operações com CFOP ou CFOP/NAT parametrizado, e <a id="OLE_LINK64"></a>com valor na Base de 

   Cálculo de ICMS\.

   Quando desmarcado, serão consideradas todas as operações com valor na Base de Cálculo de ICMS\.

 

<a id="OLE_LINK42"></a>\- __Descontar as Operações de Devolução__ \(tela do cálculo\)

   O objetivo desta parametrização é indicar se as devoluções devem ser descontadas dos totais apurados, tanto no total geral das 

   saídas, como no total das saídas tributadas\.

\- __Parâmetros Específicos p/ Apuração do Total das Saídas __\(tela do cálculo\) \(criado na __MFS14391__\)

  Este parâmetro é utilizado somente na apuração do total geral das saídas:

Informe a opção de valor a ser utilizada

Neste campo o usuário escolhe qual valor será utilizado na totalização geral das saídas:

\- Valor Contábil

\- Valor Contábil – Valor ICMS ST

__MFS15006__: O parâmetro que foi criado pela __MFS14391 __apenas no cálculo “normal”, através da __MFS15006__ foi replicado para os cálculos p/ IEU e IE \- PIM\. Com a MFS15006, os __Parâmetros Específicos p/ Apuração do Total das Saídas __serão considerados no cálculo apenas quando o campo “Utiliza parametrização p/ Total de Saídas” existente na tela, estiver desmarcado\. Isso porque quando estiver marcado, as opções de valores utilizadas no cálculo proverão das parametrizações p/ Cálculo do Total das Operações de Saídas/Devoluções, vide menu Cadastro >> Parâmetros p/ Cálculo do Total das Operações de Saídas/Devoluções >> por CFOP e por Extensão CFOP\.

\- __Parâmetros Específicos p/ Apuração das Saídas Tributadas__ \(tela do cálculo\)

  Estes parâmetros são utilizados apenas na apuração do total das saídas tributadas:

 Informe a opção de valor a ser utilizado

Neste campo o usuário escolhe qual campo da nota fiscal será utilizado na totalização das operações de saída tributadas:

<a id="OLE_LINK81"></a>\- Valor Contábil

\- Base de Cálculo

\- Base de Cálculo \+ IPI

__OBS__: Independente da opção escolhida, para as operações de exportação \(CFOP “7”\) é sempre utilizado o valor do campo Valor Contábil\. 

<a id="_Hlk514949704"></a>Considerar Base Tributada \+ Valor Outras \(somente operações com diferimento/suspensão/antecipação\)

Este parâmetro serve para que operações normalmente tributadas, mas que tenham o imposto diferido, suspenso ou antecipado, sejam consideradas na totalização\. 

Nesta condição \(diferimento/suspensão/antecipação\), a nota *não* terá a base de cálculo preenchida, e este valor estará no campo “Outras”\. 

Assim, para que este valor da __base “Outras__” seja considerado, o usuário deve marcar este parâmetro\. 

Ao marcar o parâmetro, o usuário deve informar também como esta condição de diferimento, suspensão ou antecipação será identificada nas notas, através das seguintes opções:

__Identificar as operações pelo Código de Situação Tributária Estadual  B \(CST\-B\):__

<a id="OLE_LINK57"></a>Nesta opção, serão considerados os valores lançados no campo Base Outras apenas dos itens das notas que tenham os seguintes códigos de Situação Tributária Estadual B \(campo 31 \- SAFX08\): 50 \- Suspensão, 51 \- Diferimento ou 60 \- Antecipação\.

Para utilizar esta opção, o usuário deve garantir que o CST\-B de todos os itens estarão preenchidos\.

__Considerar todas as operações com valor lançado na base “Outras”:__

Nesta opção, serão considerados os valores lançados no campo Base Outras de todas as notas \(independente do Código de Situação Tributária Estadual B\)\.

Para utilizar esta opção, o usuário deve garantir que todas as operações com base outras preenchida são realmente situações de diferimento, suspensão ou antecipação;

# <a id="_Toc514939190"></a><a id="OLE_LINK65"></a>Processamento – Total Geral das Saídas

<a id="OLE_LINK71"></a><a id="OLE_LINK72"></a>A totalização das operações de saída é feita da seguinte forma:

- 1\-Apura o total das saídas;
- 2\-Se parâmetro <a id="OLE_LINK67"></a><a id="OLE_LINK68"></a><a id="OLE_LINK69"></a>“*Descontar as operações de devolução*” \(tela do cálculo\) = “S”, apura o total das devoluções de saída; 
- __Total apurado__ = \[ valor apurado no Passo 1 \] – \[ valor apurado no Passo 2 \];

Segue as regras da recuperação das notas de saída e notas de devolução:

 

<a id="OLE_LINK66"></a>__1\-Critérios da recuperação das saídas:__

\- Empresa – código da empresa do login;  

\- Estabelecimento – código do estabelecimento da geração \(considerando as regras sobre IEU e IE\-PIM, descritas no item 1\-Regras 

  Gerais\);

\- Data Fiscal – data enquadrada no período informado em tela;

<a id="OLE_LINK70"></a>\- Movimento E/S = “9”;

\- Situação da Nota – apenas as notas não canceladas;

\- Classificação – 1 ou 3;

\- Se parâmetro “*Utiliza parametrização p/ Total de Saídas*” \(tela do cálculo\) = “S”

      Nesse caso o CFOP ou CFOP/NAT da capa ou do item, conforme o caso, deve estar parametrizado no menu <a id="OLE_LINK74"></a><a id="OLE_LINK75"></a><a id="OLE_LINK76"></a>“Parâmetros p/Cálculo 

      do Total das Operações de Saídas/Devoluções” 

  Senão

      Nesse caso serão consideradas todas as operações de saída;

Valor a ser utilizado na totalização das notas:

__MFS15006__: O parâmetro “__Parâmetros Específicos p/ Apuração do Total das Saídas__” foi criado pela __MFS14391 __apenas no cálculo “normal”\. Através da __MFS15006__ foi replicado para os cálculos p/ IEU e IE \- PIM\. Com a MFS15006, os __Parâmetros Específicos p/ Apuração do Total das Saídas __passam a ser considerados no cálculo apenas quando o campo “*Utiliza parametrização p/ Total de Saídas*” existente na tela, estiver desmarcado\. Isso porque quando estiver marcado, as opções de valores utilizadas no cálculo proverão das parametrizações p/ Cálculo do Total das Operações de Saídas/Devoluções, vide menu Cadastro >> Parâmetros p/ Cálculo do Total das Operações de Saídas/Devoluções >> por CFOP e por Extensão CFOP\.

__Se__ a geração for por I\.E\.U\. ou I\.E\.\-PIM: *\(Menus “Cálculo do Crédito \- ICMS p/IEU” ou “Cálculo do Crédito \- ICMS p/IE PIM”\)*

      Valor utilizado na totalização = Valor Contábil \(conforme a versão original do cálculo\)

__Se__ a geração for “normal”: *\(Menus “Cálculo do Crédito – ICMS”\)*

     O valor a ser utilizado depende da opção informada em tela para o parâmetro “*Parâmetros Específicos p/ Apuração do Total*

*     das Saídas*” \(parâmetro criado na __MFS14391__\), da seguinte forma:

      Se opção = Valor Contábil 

           As notas serão totalizadas pelo valor contábil \(conforme a versão original do cálculo\); 

      Senão \(opção = Valor Contábil – ICMS ST\)

           As notas serão totalizadas pelo resultado: \[ valor contábil – valor do ICMS ST \]; 

 Se parâmetro “*Utiliza parametrização p/ Total de Saídas*” \(tela do cálculo\) = “S”

    O valor a ser utilizado depende da opção escolhida para o CFOP ou CFOP/NAT da nota, nas parametrizações p/ Cálculo do Total das Operações de Saídas/Devoluções\.

    Veja:

O valor utilizado para totalização depende do CFOP ou CFOP/Nat \(conforme o caso\), da capa ou item da nota \(conforme o caso\)\. Assim, será verificado na parametrização \(“Parâmetros p/ Cálculo do Total das Operações de Saídas/Devoluções”\) os valores indicados, e serão utilizados todos os valores marcados pelo usuário, que podem ser:

\- Valor contábil

\-  Valor contábil \- ICMS ST

\- Base tributada

\- Base isenta

\- Base outras

\- Base de redução

*Obs\.: A tela da parametrização tem uma regra que não permite ao usuário marcar o valor contábil junto com qualquer outro valor\. Ou seja, ou escolhe o valor contábil, *__*ou*__*, escolhe valor contábil – ICMS\-ST, *__*ou*__*, escolhe uma ou várias bases\.*

 Senão

     O valor a ser utilizado depende da opção informada em tela para o parâmetro “*Parâmetros Específicos p/ Apuração do Total*

*     das Saídas*” \(parâmetro criado na __MFS14391__\), da seguinte forma:

      Se opção = Valor Contábil 

           As notas serão totalizadas pelo valor contábil \(conforme a versão original do cálculo\); 

      Senão \(opção = Valor Contábil – ICMS ST\)

           As notas serão totalizadas pelo resultado: \[ valor contábil – valor do ICMS ST \]; 

__2\-Critérios da recuperação das devoluções de saídas:__

As devoluções serão utilizadas no cálculo apenas se o parâmetro “*Descontar as operações de devolução*” \(tela do cálculo\) = “S”\.

Os critérios para a recuperação das notas são os mesmos das notas de saída, exceto pelo indicador de movimento da nota, já que nesse caso se trata de notas de entrada:

\- Movimento E/S <> “9”;

Valor a ser utilizado na totalização das notas de devolução:  

\(a regra é a mesma da totalização das saídas\)

__MFS15006__: O parâmetro “__Parâmetros Específicos p/ Apuração do Total das Saídas__” foi criado pela __MFS14391 __apenas no cálculo “normal”\. Através da __MFS15006__ foi replicado para os cálculos p/ IEU e IE \- PIM\. Com a MFS15006, os __Parâmetros Específicos p/ Apuração do Total das Saídas __passam a ser considerados no cálculo apenas quando o campo “*Utiliza parametrização p/ Total de Saídas*” existente na tela, estiver desmarcado\. Isso porque quando estiver marcado, as opções de valores utilizadas no cálculo proverão das parametrizações p/ Cálculo do Total das Operações de Saídas/Devoluções, vide menu Cadastro >> Parâmetros p/ Cálculo do Total das Operações de Saídas/Devoluções >> por CFOP e por Extensão CFOP\. 

Como o parâmetro “*Descontar as operações de devolução*” só fica habilitado quando os parâmetros “*Utiliza parametrização p/ Total de Saídas*” e “*Utiliza parametrização p/ Saídas Tributadas*” forem marcados, para devoluções só necessitam do tratamento descrito para “parâmetro “*Utiliza parametrização p/ Total de Saídas” \(tela do cálculo\) = “S”*” na regra descrita no item “1\-Critérios da recuperação das saídas”\.

__Se__ a geração for por I\.E\.U\. ou I\.E\.\-PIM: *\(Menus “Cálculo do Crédito \- ICMS p/IEU” ou “Cálculo do Crédito \- ICMS p/IE PIM”\)*

      Valor utilizado na totalização \- Valor Contábil \(conforme a versão original do cálculo\)

__Se__ a geração for “normal”: *\(Menus “Cálculo do Crédito – ICMS”\)*

     O valor a ser utilizado depende da opção informada em tela para o parâmetro “*Parâmetros Específicos p/ Apuração do Total*

*     das Saídas*” \(parâmetro criado na __MFS14391__\), da seguinte forma:

      Se opção = Valor Contábil 

           As notas serão totalizadas pelo valor contábil \(conforme a versão original do cálculo\); 

      Senão \(opção = Valor Contábil – ICMS ST\)

           As notas serão totalizadas pelo resultado: \[ valor contábil – valor do ICMS ST \]; 

__Resultado final do Total Geral das Saídas__ = total apurado das saídas – total apurado das devoluções\.

# <a id="_Toc514939191"></a>Processamento – Total das Saídas Tributadas

A totalização das operações de saída tributadas é feita da seguinte forma:

- <a id="OLE_LINK73"></a>1\-Apura o total das saídas tributadas;
- 2\-Apura o total das saídas tributadas “especiais” \(ver OBS\);
- 3\-Se parâmetro “*Descontar as operações de devolução*” \(tela do cálculo\) = “S”, apura o total das devoluções de saídas tributadas; 
- __Total apurado__ = \[ valor apurado no Passo 1 \+ valor apurado do Passo 2 \] – \[ valor apurado no Passo 3 \];

OBS: Saídas tributadas “especiais” são as saídas isentas/não tributadas que são consideradas como tributadas\. A apuração destas saídas é feita pela parametrização do menu “*Parâmetro Específico p/Cálculo  das Operações de Saídas Tributadas \(por UF\)*”\.

Segue as regras da recuperação das notas das 3 etapas \(saídas tributadas, saídas tributadas “especiais” e notas de devolução\):

 

<a id="OLE_LINK77"></a>__1\-Critérios da recuperação das saídas tributadas:__

<a id="OLE_LINK20"></a>\- Empresa – código da empresa do login;  

\- Estabelecimento – código do estabelecimento da geração \(considerando as regras sobre IEU e IE\-PIM, descritas no item 1\-Regras 

  Gerais\);

\- Data Fiscal – data enquadrada no período informado em tela;

\- Movimento E/S = “9”;

\- Situação da Nota – apenas as notas não canceladas;

\- Classificação – 1 ou 3;

<a id="OLE_LINK8"></a>\- Se parâmetro “*Utiliza parametrização p/Saídas Tributadas*” \(tela do cálculo\) = “S”

      Nesse caso o CFOP ou CFOP/NAT da capa ou do item, conforme o caso, deve estar parametrizado no menu “Parâmetros p/Cálculo 

      das Operações de Saídas Tributadas” 

  Senão

      Nesse caso serão consideradas todas as operações de saída com valor na base de cálculo do ICMS;

<a id="OLE_LINK2"></a>\- O valor a ser utilizado na totalização destas notas segue a seguinte regra:

Nas saídas internas ou interestaduais:

\(CFOP “5” ou “6”\)

O valor da nota a ser utilizado para totalização é indicado pelo parâmetro “*Informe a opção do valor a ser utilizado*” \(tela do cálculo\):

<a id="OLE_LINK85"></a><a id="OLE_LINK86"></a><a id="OLE_LINK87"></a>= 1 à Utiliza o Valor Contábil

<a id="OLE_LINK88"></a>= 2 à Utiliza o Valor da Base Tributada do ICMS 

= 3 à Utiliza o Valor da Base Tributada do ICMS \+ Valor do IPI

Tratamento do parâmetro “Considerar Base Outras” \(tela do cálculo\):

 

Se \(parâmetro “Considerar Base Tributada \+ Valor Outras” = “S”\) __e__

     \(opção de valor = “2” ou “3”\) <a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>__e__

     \(valor da Base Outras preenchido\) 

 

     Atendidas estas condições, a base Outras será utilizada dependendo 

     da opção do usuário para identificar as operações \(Diferimento, 

     Suspensão ou Antecipação\) pelo CST ou não:

     Se opção “Identificar as operações pelo CST\- B = “S”

           Se código CST\-B = 50 \(Susp\), 51 \(Dif\) ou 60 \(Antec\),

                Utiliza valor da Base Outras na totalização;

           Senão

                Nesse caso, a base Outras *não* será utilizada;

     Senão

<a id="OLE_LINK6"></a>          Utiliza valor da Base Outras na totalização;

*Obs: O parâmetro referente a utilização da Base Outras só pode ser usado quando a opção de valor escolhida for 2 ou 3, pois na opção 1 \(Valor Contábil\) já estão incluídas todas as bases, inclusive a base Outras\.*

Nas exportações:

 \(CFOP “7”\)

No caso das exportações será utilizado sempre o Valor Contábil

__2\-Critérios da recuperação das saídas tributadas “especiais”:__

Os critérios para recuperação das notas nessa etapa são semelhantes aos das saídas tributadas, sendo que nesse caso é utilizada a parametrização do menu “Parâmetro Específico p/Cálculo das Operações de Saídas Tributadas \(por UF\)”\. Para recuperar os dados desta parametrização é utilizada a UF do estabelecimento selecionado para geração\.

Então, teríamos:

\- Empresa – código da empresa do login;  

\- Estabelecimento – código do estabelecimento da geração \(considerando as regras sobre IEU e IE\-PIM, descritas no item 1\-Regras 

  Gerais\);

\- Data Fiscal – data enquadrada no período informado em tela;

\- Movimento E/S = “9”;

\- Situação da Nota – apenas as notas não canceladas;

\- Classificação – 1 ou 3;

\- O CFOP ou CFOP/NAT da capa ou do item, conforme o caso, deve estar parametrizado no menu <a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK5"></a><a id="OLE_LINK7"></a>“Parâmetro Específico p/Cálculo

  das Operações de Saídas Tributadas \(por UF\)” 

 

\- Valor utilizado na totalização: Valor Contábil

__MFS18604__: Esta MFS alterou a parametrização específica das saídas tributadas para o usuário indicar qual o valor da nota a ser utilizado para cada CFOP ou CFOP/Natureza parametrizado\. Desta forma, ao invés de usar o valor contábil destas notas, serão utilizados os valores indicados pelo usuário, conforme a regra a seguir:

 

\- O valor a ser utilizado na totalização destas notas depende do CFOP ou CFOP/NAT, da seguinte forma:

O valor utilizado para totalização depende do CFOP ou CFOP/Nat \(conforme o caso\), da capa ou item da nota \(conforme o caso\)\. Assim, será verificado na parametrização \(*“Parâmetro Específico p/Cálculo das Operações de Saídas Tributadas \(por UF\)”\)* os valores indicados, e serão utilizados todos os valores marcados pelo usuário, que podem ser:

\- Valor contábil

\- Base tributada

\- Base isenta

\- Base outras

\- Base de redução

*Obs\.: A tela da parametrização tem uma regra que não permite ao usuário marcar o valor contábil junto com qualquer outro valor\. Ou seja, ou escolhe o valor contábil, *__*ou*__*, escolhe uma ou várias bases\.*

__3\-Critérios da recuperação das devoluções de saídas tributadas:__

As devoluções serão utilizadas no cálculo apenas se o parâmetro “*Descontar as operações de devolução*” \(tela do cálculo\) = “S”\.

Os critérios para a recuperação das notas são os mesmos das notas de saída tributadas, exceto pelo indicador de movimento da nota, já que nesse caso se trata de notas de entrada:

\- Movimento E/S <> “9”;

\- O valor usado na totalização das devoluções também é o mesmo usado ao totalizar as saídas tributadas \(conforme regras descritas na

   totalização das saídas tributadas\);

*\(não identificado no código a utilização do NORM\_DEV\)*

*\(desta forma, são recuperadas todas as entradas com CFOP ou CFOP/NAT parametrizados\)*

*\(observar que a parametrização das saídas tributadas “especiais” foi criada sem CFOP’s de entrada, e assim, as devoluções destas operações tributadas “especiais” não são tratadas\) Através da *__*MFS15006*__* os CFOPs de entrada foram incluídos nas parametrizações das saídas tributadas “especiais”\. Com isso, as devoluções dessas operações passam a ser tratadas no cálculo\.*

__Resultado final do Total das Saídas Tributadas:__

     \( total apurado das saídas tributadas \+ total apurado das saídas tributadas “especiais” \)  –  total apurado das devoluções

= = = = = =

 

