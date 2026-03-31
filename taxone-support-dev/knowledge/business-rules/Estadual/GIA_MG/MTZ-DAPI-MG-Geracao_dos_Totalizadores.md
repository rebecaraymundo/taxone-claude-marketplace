# MTZ-DAPI-MG-Geracao_dos_Totalizadores

- **Fonte:** MTZ-DAPI-MG-Geracao_dos_Totalizadores.docx
- **Modificado:** 2022-04-06
- **Tamanho:** 65 KB

---

THOMSON REUTERS

                                               __Módulo GIA\-MG \- Rotina de Geração dos Totalizadores__

__Localização__: Menu Estadual, Módulo GIA\-MG,  menu Obrigações 🡪 DAPI 🡪 Geração 🡪 Geração dos Totalizadores

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4576

Atualizações da versão 8\.00

Atualizações da versão 8\.00 \(inclusão dos dados do incentivo ao esporte na linha 23\)

\(ver __RN01__\)

28/07/2014

\(criação do docto\)

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Esta geração calcula e atualiza vários valores nas tabelas dos dados da DAPI\.

__RN01__

__                                           Geração da Linha 23 \(EST\_MG\_GIA\_LIN23\)__

Uma das atualizações feitas na geração dos totalizadores é a geração da linha 23 da DAPI \(tabela EST\_MG\_GIA\_LIN23\)\.

\(a linha 23 é a linha dos dados apresentados no menu ““Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento”, aba “Campo 98”\)

__Levantamento feito sobre o funcionamento da linha 23 da DAPI \(em 27/07/2014\):__

Da forma como foi construído o tratamento da linha \(23\), a lógica é a seguinte:

\(1\) O usuário deve fazer a geração dos registros, e depois a geração dos totalizadores, para que a linha 23 seja gerada, e seus dados possam aparecer na tela da manutenção\. A linha é criada com o valor do saldo anterior \(caso exista\), e demais campos de totalizações;

*    \(enquanto a geração dos totalizadores não for executada, os campos referentes à linha 23 não são exibidos na tela de manutenção\)*

\(2\) Na manutenção, o usuário poderá inserir as informações de entrada manual da linha 23, que são os campos: “Saldo Período Anterior”, “Alíquota de Dedução” e “Estorno de Saldo de Incentivo à Cultura”;

\(3\) Efetuar novamente a geração dos totalizadores para que as informações manuais inseridas possam ser consideradas na totalização;

__Alteração da OS4576:__

Esta Os incluiu na linha 23 os campos referentes ao incentivo ao esporte, atendendo à versão 8\.00 da DAPI\-MG, que são os seguintes:

\(\*\) \- Saldo Período Anterior \- Incentivo ao Esporte

     \- Incentivo ao Esporte

     \- Total Dedução Incentivo ao Esporte

     \- Vlr Limite para Dedução \- Incentivo ao Esporte

     \- Saldo Credor Período Seguinte \- Incentivo ao Esporte

\(\*\) \- Alíquota de Dedução \- Incentivo ao Esporte

\(\*\) \- Estorno de Saldo de Incentivo ao Esporte

Tamanho dos campos: Campos de valor 🡪 Number \(17,2\)

                                      Alíquota 🡪 Number \(7,4\) 

Estes novos campos serão tratados na rotina de totalização da seguinte forma:

Saldo Período Anterior \-  Incentivo ao Esporte

Na criação da linha:

O valor deste campo será obtido na apuração do período anterior\. Será o conteúdo do campo “*Saldo Credor Período Seguinte – Incentivo ao Esporte*” referente ao mês anterior \(tabela EST\_MG\_GIA\_LIN23\)\. Quando não existir a informação, será considerado valor = 0\.

Quando a rotina for reexecutada p/um mesmo período \(__ou seja, a linha já existir__\):

Neste caso o conteúdo do campo *não* será alterado, já que o mesmo pode ter sido alterado via manutenção\. 

Incentivo ao Esporte

Este campo será sempre atualizado com a totalização dos valores inseridos na nova aba “__Incentivo ao Esporte__” da tela de manutenção do campo 98 \(menu “Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento”\)\.

 

Total Dedução Incentivo ao Esporte

Este campo será sempre atualizado com o seguinte resultado:

Campo “*Saldo Período Anterior \- Incentivo ao Esporte*”

__\+__

Campo “*Incentivo ao Esporte*”

__\-__

Campo “*Estorno de Saldo de Incentivo ao Esporte*”

Vlr Limite para Dedução – Incentivo ao Esporte

Este campo será sempre atualizado com o seguinte resultado:

Se campo “Alíquota de Dedução \- Incentivo ao Esporte” > 0

      O resultado será = campo 97 da DAPI \* Alíquota / 100

Senão

      O resultado será = zero;

__Obs__: O campo 97 da DAPI é o campo “*Saldo Devedor Apurado*” exibido no menu “Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Anexos”, aba “Apuração”\. 

Saldo Credor Período Seguinte – Incentivo ao Esporte

Este campo será sempre atualizado com o seguinte resultado:

Se campo “*Total Dedução Incentivo ao Esporte*” > 

                 campo “*Vlr Limite para Dedução – Incentivo ao Esporte*”

      O resultado será a diferença entre os dois campos, da seguinte forma:

*      Total Dedução Incentivo ao Esporte* __\- __*Vlr Limite para Dedução Incentivo ao Esporte*

Senão

      O resultado será = zero;

Alíquota de Dedução – Incentivo ao Esporte

A informação deste campo é inserida manualmente na tela de manutenção, assim, ele nunca será atualizado, e seu valor será sempre mantido\.

Estorno de Saldo de Incentivo ao Esporte

A informação deste campo é inserida manualmente na tela de manutenção, assim, ele nunca será atualizado, e seu valor será sempre mantido\.

__                                                         __

= = = = = 

