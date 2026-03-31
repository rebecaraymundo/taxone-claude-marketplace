# MTZ_Tela_Manutencao_Quadro_15

- **Fonte:** MTZ_Tela_Manutencao_Quadro_15.docx
- **Modificado:** 2024-05-20
- **Tamanho:** 84 KB

---

THOMSON REUTERS

Módulo DIME\-SC

Manutenção do Demonstrativo dos Valores Devidos aos Fundos – Quadro 15  

__Localização__: Menu Estadual, módulo DIME\-SC, menu Obrigações > Manutenção do Demonstrativo dos Valores Devidos aos Fundos – Quadro 15  

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS91937__

Aline Melo

Criação do Documento

15/09/2022

__MFS639390__

Andréa Rocha

Alteração do código FUNDES para FUMDES\.

20/05/2024

Sumário

[1\.	Regras Gerais	2](#_Toc524527071)

[2\.	Layout da Tela	2](#_Toc524527072)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc524527073)

# <a id="_Toc524527071"></a>Regras Gerais

O objetivo desta tela é permitir a manutenção do Demonstrativo dos Valores Devidos aos Fundos, referente ao Quadro 15, em atendimento Portaria SEF N° 314/2022\. 

Este cadastro também é carregado através da importação da SAFX321\.

# <a id="_Toc524527072"></a>Layout da Tela

<a id="_Hlk114122903"></a>Tela do tipo simples \(manutenção de um registro por vez\)\.

Tabela: X321\_SC\_DIME\_QUAD\_15\.

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar as informações para um novo estabelecimento\. 

ABRE

Exibe janela de pesquisa dos dados já cadastrados, para que o usuário selecione o cadastro <a id="OLE_LINK4"></a>desejado a ser exibido em tela\.

EXCLUI

Opção para excluir o cadastro de um estabelecimento

CONFIRMA

Opção para salvar os dados do cadastro incluído / alterado\.

ORDENA

Opção para ordenar os cadastros\.

RELATÓRIO

Esta opção permite imprimir os dados do cadastro\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc524527073"></a>Regras de Funcionamento dos Campos

Ao acessar a janela através do menu, o sistema deve verificar se o estabelecimento foi informado no login do Manager\.

Caso o estabelecimento tenha sido informado no login e a UF do mesmo seja diferente de SC, o sistema exibir a mensagem a seguir e não abrir a janela:

*“Este estabelecimento não pertence a Santa Catarina”*

 

__Campo__ 

__Tipo__ 

__Obrig__ 

__Ed__ 

__Formato/Default__ 

__Regra__ 

__MFS__

Estabelecimento

Texto

S

S

Formato: Combo Box 

 Default: Habilitado

Neste campo será exibido o Estabelecimento escolhido pelo usuário, na Tela de Login do Sistema, não tendo a opção de escolha de outro Estabelecimento, apenas será habilitado para seleção caso o usuário não entre com o Estabelecimento na Tela de Login\.  

Somente apresentar estabelecimentos de Santa Catarina\.

Ao salvar o registro se o campo não for preenchido, exibir a mensagem de erro abaixo, e a operação não será salva: 

*  “Estabelecimento deve ser preenchido”* 

MFS91937

Mês/Ano

Data

S

S

Formato: MM/AAAA 

Default: Habilitado 

 

Permite ao usuário informar o mês e o ano referente aos dados lançados\.

Gravar o campo DATA\_REF com o último dia do mês/ano\.

Ao salvar o registro se o campo não for preenchido, exibir a mensagem de erro abaixo, e a operação não será salva: 

*  “Mês/Ano deve ser preenchido”* 

MFS91937

Benefício \(cód\./dsc\.\)

Alfanumérico

N

S

Formato: Pesquisa 

Default: conforme regra

Campo destinado a informar o código do benefício TTD de acordo com a Tabela de Códigos de Benefício TTD \(TACES107\)\. Deve ser demonstrado o código e a descrição do benefício\. 

Este campo trabalha com janela de seleção dos dados da Tabela de Códigos de Benefício TTD \(TACES107\)\.

Quando o campo for digitado e o código não for encontrado na tabela, será exibida a mensagem de erro abaixo, e a operação não será salva: 

*  “Código de Benefício TTD não cadastrado”* 

MFS91937

Número Concessão

Alfanumérico

N

S

Formato: Texto 

 Default: conforme regra

Permite ao usuário informar o número da concessão\.

Ao salvar o registro, se os campos Benefício e Número Concessão estiverem preenchidos, validá\-los no Cadastro da Concessão para Benefício TTD \(módulo DIME\-SC, menu Parâmetros >> Informações de ICMS >> Quadro 15 >> Cadastro da Concessão para Benefício TTD\)\.

Para isso consultar a Tabela de Cadastro da Concessão para Benefício TTD \(EST\_SC\_DIME\_CONC\_BENEF\), obedecendo aos seguintes critérios:

\- Empresa = Código da Empresa de login

\- Estabelecimento = Código do Estabelecimento informado

\- Benefício \(TTD\) = Código de Benefício \(TTD\) informado

\- Número concessão = Número de Concessão informado

\- Validade Inicial <= último dia do mês/ano informado \(Data Referência\)

\- Validade Final nula ou 

   Validade Final >= último dia do mês/ano informado \(Data Referência\)

Se o cadastro não for encontrado, o registro não será gravado, e a seguinte mensagem deve ser exibida:

*Número de Concessão para o Benefício TTD não cadastrado\.*

MFS91937

Tipo 3 – Crédito Presumido \(cód\./dsc\.\) 

Alfanumérico

N

S

Formato: Pesquisa 

 Default: conforme regra

Campo destinado a informar o código de acordo com a Tabela de Códigos do Tipo 3 – Crédito Presumido DCIP \(TACES108\)\. Deve ser demonstrado o código e a descrição\.

Este campo trabalha com janela de seleção dos dados da Tabela de Códigos do Tipo 3 – Crédito Presumido DCIP \(TACES108\)\.

Quando o campo for digitado e o código não for encontrado na tabela, será exibida a mensagem de erro abaixo, e a operação não será salva: 

*  “Código do Tipo 3 – Crédito Presumido \(DCIP\) não cadastrado”* 

Não permitir o preenchimento dos três campos ao mesmo tempo __*Benefício \(cód\./dsc\.\)*__ \+ __*Número Concessão*__ \+ __*Tipo 3 – Crédito Presumido*__ __*\(cód\./dsc\.\)*__\. 

Para isso realizar os tratamentos a seguir:

\- Se preencher o campo Benefício \(cód\./dsc\.\):

- Desabilitar o campo Tipo 3 – Crédito Presumido \(cód\./dsc\.\) 
- Habilitar o campo Número Concessão\. 

\- Se preencher o campo Tipo 3 – Crédito Presumido \(cód\./dsc\.\):

- Desabilitar os campos Benefício \(cód\./dsc\.\) e Número Concessão 

MFS91937

Vlr da Base de Cálculo do ICMS da Operação

Numérico

N

S

Formato: 0,00 

Default: Habilitado 

Permite ao usuário informar o valor da base de cálculo do ICMS\.

MFS91937

Vlr do ICMS Exonerado

Numérico

N

S

Formato: 0,00 

Default: Habilitado 

Permite o usuário informar o valor do ICMS exonerado\.

MFS91937

Cálculo FUMDES

Cálculo FUNDES 

 

Alfanumérico

N

S

Formato: Combo Box 

Default: Habilitado

Permite o usuário selecionar o tipo de cálculo FUMDES disponível na lista\. 

 

Conteúdo: 

- 0 \- Não exigido na Portaria SEF 143/22 
- 1 \- 2% do ICMS Exonerado

 

MFS91937

MFS639390

Vlr FUMDES 

Vlr FUNDES 

Numérico

N

S

Formato: 0,00 

 

Default: Habilitado 

Permite ao usuário informar o valor do FUMDES

MFS91937

MFS639390

Cálculo FUNDO SOCIAL 

Alfanumérico

N

S

Formato: Combo Box 

Default: Habilitado

Permite ao usuário selecionar o tipo de cálculo do FUNDO SOCIAL disponível na lista\. 

 

Conteúdo: 

- 0 \- Não exigido na Portaria SEF 143/22; 
- 1 \- 2,5% do ICMS Exonerado; 
- 2 \- 0,4% da BC ICMS \- FUMDES 
- 3 \- 0,4% da BC ICMS \- \(FUNDO SOCIAL \+ FUMDES\) 
- 4 \- 4,5% do ICMS Exonerado 

MFS91937

Vlr FUNDO SOCIAL 

Numérico

N

S

Formato: 0,00 

Default: Habilitado 

Permite ao usuário informar o valor do Fundo Social\.

MFS91937

Vlr da Base de Cálculo do ICMS da Devolução 

Numérico

N

S

Formato: 0,00 

Default: Habilitado 

Permite ao usuário informar o valor da base de cálculo do ICMS da devolução\.

MFS91937

Vlr do ICMS Exonerado da Devolução 

Numérico

N

S

Formato: 0,00 

Default: Habilitado 

Permite ao usuário informar o valor do ICMS exonerado da devolução\.

MFS91937

Vlr FUMDES da Devolução 

Vlr FUNDES da Devolução 

Numérico

N

S

Formato: 0,00 

Default: Habilitado 

Permite ao usuário informar o valor do FUMDES da devolução\.

MFS91937

MFS639390

Vlr FUNDO SOCIAL da Devolução 

Numérico

N

S

Formato: 0,00 

Default: Habilitado 

Permite ao usuário informar o valor do Fundo Social da devolução\.

MFS91937

Ao gravar o registro, realizar a seguinte regra:

Deve ser obrigatório o preenchimento dos campos __*Benefício \(cód\./dsc\.\)*__ \+ __*Número Concessão*__ OU __*Tipo 3 – Crédito Presumido \(cód\./dsc\.\)*__\. 

Caso os três campos 04 \- Código de Benefício \(TTD\), 05 \- Número de Concessão e 06 \- Código do Tipo 3 – Crédito Presumido \(DCIP\) __não__ estejam preenchidos, não salvar o registro e exibir a seguinte mensagem de erro:

*Os campos de identificação do Benefício \(Código de Benefício TTD e Número de Concessão\) ou do Crédito Presumido \(Código do Tipo 3 – Crédito Presumido \(DCIP\)\) devem ser preenchidos\.*

Caso o 04 \- Código de Benefício \(TTD\) esteja preenchido e o campo 05 \- Número de Concessão não preenchido, não salvar o registro e exibir a seguinte mensagem de erro:

*Os campos que compõe a identificação do Benefício \(Código de Benefício TTD e Número de Concessão\) devem ser preenchidos*

Caso o 04 \- Código de Benefício \(TTD\) não esteja preenchido e o campo 05 \- Número de Concessão esteja preenchido, não salvar o registro e exibir a seguinte mensagem de erro:

*Os campos que compõe a identificação do Benefício \(Código de Benefício TTD e Número de Concessão\) devem ser preenchidos\.*

