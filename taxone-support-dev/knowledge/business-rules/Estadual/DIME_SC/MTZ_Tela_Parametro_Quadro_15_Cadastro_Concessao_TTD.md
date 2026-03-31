# MTZ_Tela_Parametro_Quadro_15_Cadastro_Concessao_TTD

- **Fonte:** MTZ_Tela_Parametro_Quadro_15_Cadastro_Concessao_TTD.docx
- **Modificado:** 2022-09-20
- **Tamanho:** 83 KB

---

THOMSON REUTERS

Módulo DIME\-SC

Cadastro da Concessão para Benefício TTD 

__Localização__: Menu Estadual, módulo DIME\-SC, menu Parâmetros 🡪 Informações de ICMS 🡪 Quadro 15 🡪 Cadastro da Concessão para Benefício TTD 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS91937__

Aline Melo

Criação do documento\.

15/09/2022

Sumário

[1\.	Regras Gerais	2](#_Toc524527071)

[2\.	Layout da Tela	2](#_Toc524527072)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc524527073)

# <a id="_Toc524527071"></a>Regras Gerais

O objetivo desta tela é permitir a manutenção do cadastro da concessão para benefício TTD, em atendimento Portaria SEF N° 314/2022\. 

# <a id="_Toc524527072"></a>Layout da Tela

<a id="_Hlk114122903"></a>Tela do tipo simples \(manutenção de um registro por vez\)\.

Tabela: EST\_SC\_DIME\_CONC\_BENEF\.

Chave Primária: Empresa, Estabelecimento Código Benefício TTD, Número Concessão, Validade Inicial\.

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

Benefício \(cód\./dsc\.\)

Alfanumérico

S

S

Formato: Pesquisa 

Default: Habilitado

Campo destinado a informar o código do benefício TTD de acordo com a Tabela de Códigos de Benefício TTD \(TACES107\)\. Deve ser demonstrado o código e a descrição do benefício\. 

Este campo trabalha com janela de seleção dos dados da Tabela de Códigos de Benefício TTD \(TACES107\)\.

Quando o campo for digitado e o código não for encontrado na tabela, será exibida a mensagem de erro abaixo, e a operação não será salva: *“Código de Benefício TTD não cadastrado”* 

Ao salvar o registro se o campo não for preenchido, exibir a mensagem de erro abaixo, e a operação não será salva: 

*  “Código de Benefício TTD deve ser preenchido”* 

MFS91937

Número Concessão

Alfanumérico

S

S

Formato: Texto

Permite ao usuário informar o número da concessão\.

Ao salvar o registro se o campo não for preenchido, exibir a mensagem de erro abaixo, e a operação não será salva: 

*  “Número Concessão deve ser preenchido”* 

Validade Inicial

Data

S

S

Formato: DD/MM/AAAA

Default: Habilitado

Campo destinado para informar a data de validade inicial do código\.

- Ao salvar o registro esse campo não poderá ser alterado;
- Se o campo não for preenchido, emitir a mensagem na tela: *“Data de Validade Inicial deve ser preenchida”\.*

Validar intervalos intercalados\. Vide “[__Tratamento para não permitir Intervalos Intercalados de Datas__](#Intevalos_Intercalados)”

MFS91937

Validade Final

Data

N

S

Formato: DD/MM/AAAA

Default: Habilitado

Campo destinado para informar a data de validade final do código\.

Se o usuário preencher a data de Validade final menor que a data de validade inicial, o sistema deverá exibir a mensagem de erro: “*Data de Validade Final menor que a Data Validade Inicial*”\.

MFS91937

<a id="Intevalos_Intercalados"></a>__Tratamento para não permitir Intervalos Intercalados de Datas__:

Vamos adotar tratamentos para impedir que parametrizações de uma concessão sejam criadas com intervalos de datas inicial e final intercalados\. Ou seja, não podemos permitir que uma parametrização de concessão tenha Data Início ou Fim de Validade entre as datas Início e Fim Validade da parametrização já existente na base\.

__Exemplo1: Concessão sem Data Fim de Validade__

Supondo que exista uma parametrização na base com os seguintes dados:

\- Empresa ‘076’ 

\- Estabelecimento ‘001’

\- Código Benefício = ‘10’

\- Número Concessão = ‘123456’

\- Validade Inicial = 01/01/2018

\- Validade Final = não preenchida

Na inclusão ou alteração de registros de mesma empresa \(076\), estabelecimento \(001\), Código Benefício \(10\) e Número Concessão \(‘123456’\), a gravação é permitida ou não, de acordo com a Data de Validade Inicial e Final informada\. Veja os Cenários:

__Início Validade__

__Fim Validade__

__Resultado __

01/01/2017

31/12/2017

Registro gravado com sucesso\.

01/01/2017

01/01/2018

Registro rejeitado\.

Data Fim intercala o registro já existe na base\. Registro não gravado\.

01/01/2017

Registro rejeitado\.

Data Fim nula, intercalando com o registro já existe na base\. Registro não gravado\.

02/01/2018

Registro rejeitado\.

Data Fim do registro existente na base é nula\. Registro não gravado\.

__Exemplo2: Concessão com Data Fim de Validade__

Supondo que exista uma parametrização na base com os seguintes dados:

\- Empresa ‘076’ 

\- Estabelecimento ‘001’

\- Código Benefício = ‘10’

\- Número Concessão = ‘123456’

\- Validade Inicial = 01/01/2018

\- Validade Final = 31/01/2018

Na inclusão ou alteração de registros de mesma empresa \(076\), estabelecimento \(001\), Código Benefício \(10\) e Número Concessão \(‘123456’\), a gravação é permitida ou não, de acordo com a Data de Validade Inicial e Final informada\. Veja os Cenários:

__Início Validade__

__Fim Validade__

__Resultado__

01/01/2017

31/12/2017

Registro gravado com sucesso\.

01/01/2017

01/01/2018

Registro rejeitado\.

Data Fim intercala o registro já existe na base\. Registro não gravado\.

01/01/2017

Registro rejeitado\.

Data Fim nula, intercalando com o registro já existe na base\. Registro não gravado\.

02/01/2018

Registro rejeitado\. 

Data Início intercala com o registro já existe na base\. Registro não gravado\.

01/02/2018

Registro gravado com sucesso\.

<a id="_Hlk2188990"></a>

__Situações tratadas na gravação \(inclusão ou alteração do registro\)__:

1. Dada a Empresa, Estabelecimento, Código Benefício e Número Concessão da parametrização que está sendo salva, buscar na base a parametrização de mesma Empresa, Estabelecimento, Código Benefício e Número Concessão com Data Início Validade imediatamente posterior à Data Início Validade do registro que está sendo gravado\.

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro que está sendo gravado com a Data Início Validade do registro encontrado\.

Se Data Fim de Validade do registro que está sendo gravado >= Data Início Validade do registro encontrado ou

     Data Fim de Validade do registro que está sendo gravado for nula então:

O registro não será gravado e a seguinte mensagem será exibida na tela:

*Foi encontrada parametrizacao para a Concessão, com datas de vigencia em conflito com as datas de vigencia informadas\. Reveja as datas de Validade Inicial e Final da Concessão de forma a não gerar sobreposição de intervalos de datas das parametrizações\.*

1. Dada a Empresa, Estabelecimento, Código Benefício e Número Concessão da parametrização que está sendo salva, buscar na base a parametrização de mesma Empresa, Estabelecimento, Código Benefício e Número Concessão com Data Início Validade imediatamente anterior à Data Início Validade do registro que está sendo gravado\.

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro encontrado com a Data Início Validade do registro que está sendo gravado\.

Se Data Fim de Validade do registro encontrado >= Data Início Validade do registro que está sendo gravado ou

     Data Fim de Validade do registro encontrado for nula então:

O registro não será gravado e a seguinte mensagem será exibida na tela:

*Foi encontrada parametrizacao para a Concessão, com datas de vigencia em conflito com as datas de vigencia informadas\. Reveja as datas de Validade Inicial e Final da Concessão de forma a não gerar sobreposição de intervalos de datas das parametrizações\.*

