# MTZ_GIA_BA_Parametros_Quadros_30_31_CFO

- **Fonte:** MTZ_GIA_BA_Parametros_Quadros_30_31_CFO.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Módulo GIA BA

Parametrização de CFOP – Quadros 30 e 31

__Localização__: Menu Estadual, Módulo: GIA BA, item menu Parâmetros 🡪 Quadros 30/31 – CFOPs \(Compras, Vendas e Devoluções\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS21172

Andréa Rocha

Criação da parametrização de CFOP’s para a pré\-geração dos Quadros 30 e 31

17/09/2019

Sumário

[1\.	Regras Gerais	2](#_Toc451940535)

[2\.	Layout da Tela	2](#_Toc451940536)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc451940537)

# <a id="_Toc451940535"></a>Regras Gerais

Os dados parametrizados neste item são utilizados na rotina de pré\-geração dos Índices de Participação \(Quadros 30 e 31\), realizada no menu “Obrigações 🡪 Pré\-Geração dos Índices de Participação \(Reg 30 e 31\)” do módulo GIA BA\.

# <a id="_Toc451940536"></a>Layout da Tela

Estabelecimento \[XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

\-\- CFOP’s \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

         Código\-Descrição                   

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\[ x \] xxxx \-xxxxxxxxxxxxxxxxxx          

\[ x \] xxxx \-xxxxxxxxxxxxxxxxxx         

\[Selecionar Todos\] \[Desmarcar Todos\]

__Botões da barra de menu__:

CONFIRMA

Opção para salvar as informações da parametrização incluída ou alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc451940537"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

S

Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário\.  Somente devem ser mostrados os estabelecimentos do estado do “BA”\.

Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá\-lo\.

MFS21172

CFOP’s

Alfanumérico

__S__

S

Neste campo é exibida a lista dos CFOP’s \(SAFX2012\) para seleção do usuário, considerando *todos* \(códigos iniciados por “1”, “2” ou “3” ou “5”, “6” ou “7”\)\.

Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade \(para não exibir códigos repetidos\)\.

Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

MFS21172

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado\.

Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

MFS21172

       = = = = = =

