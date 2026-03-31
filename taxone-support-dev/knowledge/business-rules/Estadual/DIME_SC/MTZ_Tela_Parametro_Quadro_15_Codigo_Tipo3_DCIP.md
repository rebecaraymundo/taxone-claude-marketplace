# MTZ_Tela_Parametro_Quadro_15_Codigo_Tipo3_DCIP

- **Fonte:** MTZ_Tela_Parametro_Quadro_15_Codigo_Tipo3_DCIP.docx
- **Modificado:** 2022-09-20
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Módulo DIME\-SC

Cadastro dos Códigos do Tipo 3 – Crédito Presumido \(DCIP\)

__Localização__: Menu Estadual, módulo DIME\-SC, menu Parâmetros 🡪 Informações de ICMS 🡪 Quadro 15 🡪 Códigos do Tipo 3 – Crédito Presumido \(DCIP\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS91937__

Liliane Videira Assaf

Criação da tela

13/09/2022

__MFS91937__

Aline Melo

Inclusão das regras na nova tela

14/09/2022

Sumário

[1\.	Regras Gerais	2](#_Toc524527071)

[2\.	Layout da Tela	2](#_Toc524527072)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc524527073)

# <a id="_Toc524527071"></a>Regras Gerais

O objetivo desta tela é permitir a manutenção do cadastro de códigos do Tipo 3 – Crédito Presumido \(DCIP\), utilizado no Quadro 15, em atendimento a<a id="_Hlk114063207"></a> Portaria SEF N° 314/2022\.

Este cadastro também é carregado através da importação da Tabela de Cadastro dos Códigos do Tipo 3 – Crédito Presumido \(TACES108\)\.

# <a id="_Toc524527072"></a>Layout da Tela

<a id="_Hlk114123129"></a>Tela do tipo múltiplos registros\.

Tabela: EST\_SC\_DIME\_TIPO3\.

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

Esta opção permite imprimir as informações da tela\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

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

Código Tipo 3

Alfanumérico

S

S

Texto

Campo destinado a informar o código de acordo com a Tabela de Códigos do Tipo 3 – Crédito Presumido DCIP \(TACES108\)\. 

Ao salvar o registro, se o código não for informado, exibir a mensagem de erro abaixo, e a operação não será salva: 

*  “Código do Tipo 3 – Crédito Presumido \(DCIP\) deve ser preenchido”* 

MFS91937

Descrição Tipo 3

Alfanumérico

N

S

Texto

Campo destinado a demonstrar a descrição do código selecionado no campo Código Tipo 3\.

MFS91937

Descrição Complementar

Alfanumérico

N

S

Texto

Campo destinado para demonstrar a descrição complementar do código selecionado no campo Código Tipo 3\.

MFS91937

Validade Inicial

Data

N

S

Formato: DD/MM/AAAA

Campo destinado para informar a data de validade inicial do código\.

MFS91937

Validade Final

Data

N

S

Formato: DD/MM/AAAA

Campo destinado para informar a data de validade final do código\.

Se o usuário preencher a data de Validade final menor que a data de validade inicial, o sistema deverá exibir a mensagem de erro: “*Data de Validade Final menor que a Data Validade Inicial*”\.

MFS91937

