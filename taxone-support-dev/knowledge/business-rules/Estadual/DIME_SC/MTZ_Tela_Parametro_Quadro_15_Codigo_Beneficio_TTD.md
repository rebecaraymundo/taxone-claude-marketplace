# MTZ_Tela_Parametro_Quadro_15_Codigo_Beneficio_TTD

- **Fonte:** MTZ_Tela_Parametro_Quadro_15_Codigo_Beneficio_TTD.docx
- **Modificado:** 2022-09-20
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Módulo DIME\-SC

Quadro 15 \- Códigos Benefícios de TTD

__Localização__: Menu Estadual, módulo DIME\-SC, menu Parâmetros 🡪 Informações de ICMS 🡪 Quadro 15 🡪 Códigos de Benefício TTD  

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS91937

Liliane Assaf

Criação do documento

13/09/2022

MFS91937

Aline Melo

Inclusão das regras da nova tela

14/09/2022

Sumário

[1\.	Regras Gerais	2](#_Toc524527071)

[2\.	Layout da Tela	2](#_Toc524527072)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc524527073)

# <a id="_Toc524527071"></a>Regras Gerais

<a id="_Hlk114063686"></a>O objetivo desta tela é permitir a manutenção dos códigos de benefícios TTD, que serão utilizados para o preenchimento do Quadro 15, em atendimento a Portaria SEF N° 314/2022\.

Os códigos serão importados para o sistema através da Tabela de Códigos de Benefício TTD \(TACES107\)\.

# <a id="_Toc524527072"></a>Layout da Tela

Tela do tipo múltiplos registros\.

Tabela: EST\_SC\_DIME\_BENEF

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção será apresentada uma nova linha para inclusão de dados\.

ABRE

Exibe janela de pesquisa dos dados já parametrizados, para que o usuário selecione a parametrização <a id="OLE_LINK4"></a>desejada a ser exibida em tela\.

EXCLUI

Opção para excluir a informação em tela\.

CONFIRMA

Opção para salvar a informação incluída / alterada\.

ORDENA

Opção para ordenar as informações em tela\.

PESQUISA

Opção para pesquisar um dado específico

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc524527073"></a>Regras de Funcionamento dos Campos

Ao acessar a janela através do menu Parâmetros à Informações de ICMS > Quadro 15 > Códigos de Benefício TTD, o sistema deve verificar se o estabelecimento foi informado no login do Manager\.

Caso o estabelecimento tenha sido informado no login e a UF do mesmo seja diferente de SC, o sistema deve exibir a mensagem a seguir e não abrir a janela:

*“Este estabelecimento não pertence a Santa Catarina”*

<a id="_Hlk114063531"></a>__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS__

Código Benefício \(Nr do TTD\)

Alfanumérico

S

S

Texto

Campo destinado a informar o código do benefício TTD de acordo com a Tabela de Códigos de Benefício TTD \(TACES107\)\. 

Ao salvar o registro se o código não for informado, exibir a mensagem de erro abaixo, e a operação não será salva: 

*  “Código de Benefício TTD deve ser preenchido”* 

MFS91937

Descrição Benefício

Alfanumérico

N

S

Texto

Campo destinado a demonstrar a descrição do benefício TTD selecionado no campo anterior\.

MFS91937

