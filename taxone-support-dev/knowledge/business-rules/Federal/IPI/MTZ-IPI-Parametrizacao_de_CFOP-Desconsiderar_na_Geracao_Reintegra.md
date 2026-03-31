# MTZ-IPI-Parametrizacao_de_CFOP-Desconsiderar_na_Geracao_Reintegra

- **Fonte:** MTZ-IPI-Parametrizacao_de_CFOP-Desconsiderar_na_Geracao_Reintegra.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Módulo IPI

Parametrização de CFOP \- Desconsiderar na Geração Reintegra

__Localização__: Módulo Federal 🡪 IPI Menu Meio Magnético 🡪 IN 320/03 PER/DCOMP 🡪 Parametrização de CFOP \- Desconsiderar na Geração Reintegra

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MF6444

IN 320/03 PER/DCOMP 🡪 Reintegra

Criação da parametrização de CFOP’s para geração do Arquivo  Reintegra\. 

14/11/2016

Sumário

[1\.	Regras Gerais	2](#_Toc451940535)

[2\.	Layout da Tela	2](#_Toc451940536)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc451940537)

# <a id="_Toc451940535"></a>Regras Gerais

Os dados parametrizados neste item são utilizados na rotina de Geração Arquivo Reintegra, realizada no menu “Meio Magnético 🡪 IN 320/03 PER/DCOMP 🡪 Geração Arquivo Reintegra” do módulo IPI\.

# <a id="_Toc451940536"></a>Layout da Tela

 Estabelecimento:   \[                                                                                                              \]

 CFOP’s:

 \[   \]   \[xxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\] 

 \[   \]   \[xxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]   \[xxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]   \[xxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]   \[xxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]   \[xxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]   \[xxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 Replicar para os Estabelecimentos:

 \[   \]  \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]  \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]  \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]  \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 \[   \]  \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

 

 

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

Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário\. 

Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá\-lo\.

CFOP’s

Alfanumérico

__S__

S

Neste campo é exibida a lista dos CFOP’s \(SAFX2012\) para seleção do usuário, considerando *apenas* as operações de saída \(códigos iniciados por “5”, “6” ou “7”\)\.

Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade \(para não exibir códigos repetidos\)\.

Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado\.

Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

       = = = = = =

