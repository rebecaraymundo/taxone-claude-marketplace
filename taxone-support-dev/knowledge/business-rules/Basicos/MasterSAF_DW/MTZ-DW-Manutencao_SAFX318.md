# MTZ-DW-Manutencao_SAFX318

- **Fonte:** MTZ-DW-Manutencao_SAFX318.docx
- **Modificado:** 2021-10-29
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Módulo DW

CADASTRO DE CÓDIGOS DE BARRAS DO PRODUTO POR MEDIDA COMERCIALIZADA \(SAFX318\)

__Localização__: Menu Básicos, módulo DW, menu Manutenção 🡪 Cadastros 🡪 Códigos de Barras do Produto por Medida Comercializada

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS73698

Criação da SAFX318 

Criação da SAFX318 para permitir o cadastro dos diversos códigos de barras dos produtos atribuídos às unidades de medidas comercializadas\. Informações a serem utilizadas na geração do Sped Fiscal, registro 0220 \(versão 1\.15, Jan/2022\)

28/10/2021

Sumário

[1\.	Regras Gerais	2](#_Toc451260495)

[2\.	Layout da Tela	2](#_Toc451260496)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc451260497)

# <a id="_Toc451260495"></a>Regras Gerais

Tabela SAFX318 \- Cadastro de Códigos de Barras do Produto por Medida Comercializada:

Estrutura da tabela:

__Descrição__

__CAMPO__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Indicador de Produto

IND\_PRODUTO

A

001

SIM

SIM

Código do Produto

COD\_PRODUTO

A

035

SIM

SIM

Código de Unidade de Medida

COD\_MEDIDA

A

008

SIM

SIM

Código de Barras

COD\_BARRA

A

255

SIM

NÃO

Observação: essa tela pode ser desenvolvida tomando como base a tela de Cadastro de Conversão de Unidades de Medidas por Produto\.

# <a id="_Toc451260496"></a>Layout da Tela

__Título: __Cadastro de Códigos de Barras do Produto por Medida Comercializada

Produto: \[grupo\] \[pastinha\] \[indicador\] \[código \]   \[validade\]   \[ descrição                                 \]

\(Gr\./Ind\./Cód\./Val\./Desc\.\)

Medida: \[grupo\] \[pastinha\]  \[código \]   \[validade\]  \[ descrição                                 \]

\(Gr\./Cód\./Val\./Desc\.\)

Código de Barras: \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

__Botões da barra de menu__:

Selecionar Grupo

Sistema disponibiliza a tela padrão de seleção de Grupo da Tabela de Medidas \(SAFX2007\) e depois a tela de seleção de Grupo da Tabela de Produtos \(SAFX2013\)\.

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastrados para consulta ou manutenção\. 	

EXCLUI

Esta opção permite a exclusão do registro\. 

CONFIRMA

Opção para salvar as informações do registro incluído ou alterado\.

RELATÓRIO

Esta opção permite imprimir os dados da tabela\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

Ao acionar a tela, o sistema disponibiliza a tela padrão de seleção de Grupo da Tabela de Medidas \(SAFX2007\) e depois a tela de seleção de Grupo da Tabela de Produtos \(SAFX2013\)\. Os grupos selecionados pelo usuário serão apresentados nos campos Produto e Medida de forma desabilitada\.

# <a id="_Toc451260497"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Produto

\(Gr\./Ind\./Cód\./Val\./Desc\.\)

Alfanumérico 

__S__

S

Pastinha \+ grupo \+ indicador \+ código \+ validade \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro da Produtos \(SAFX2013\)\.

Via pastinha ou via digitação do indicador e código, o sistema deve sempre recuperar o registro de maior validade para o grupo, indicador e código do produto determinado\.

Caso o código digitado não pertença a Tabela de Cadastro de Produtos, exibir a mensagem de erro no campo descrição:

*“Produto não cadastrado”*

Caso ao salvar o registro, o campo não esteja preenchido, exibir a mensagem de erro:

*O código do produto deve ser preenchido\.*

Medida

\(Gr\./Cód\./Val\./Desc\.\)

Alfanumérico

__S__

S

  Pastinha \+ grupo \+ código \+ validade \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro de Medidas \(SAFX2007\)\.

Via pastinha ou via digitação do código, o sistema deve sempre recuperar o registro de maior validade para o grupo e código de medida determinado\.

Caso o código digitado não pertença a Tabela de Cadastro de Medidas, exibir a mensagem de erro no campo descrição:

*“Medida não cadastrada”*

Caso ao salvar o registro, o campo não esteja preenchido, exibir a mensagem de erro:

*O código de medida deve ser preenchido\.*

Código de Barras

Alfanumérico

__S__

S

Neste campo deve se preenchido\.

Caso ao salvar o registro, o campo não esteja preenchido, exibir a mensagem de erro:

*“O campo Código de Barras deve ser preenchido”*

       = = = = = =

