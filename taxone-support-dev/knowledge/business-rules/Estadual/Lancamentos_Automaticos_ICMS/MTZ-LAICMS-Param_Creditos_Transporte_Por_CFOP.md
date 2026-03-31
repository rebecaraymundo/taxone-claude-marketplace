# MTZ-LAICMS-Param_Creditos_Transporte_Por_CFOP

- **Fonte:** MTZ-LAICMS-Param_Creditos_Transporte_Por_CFOP.docx
- **Modificado:** 2023-09-12
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Módulo Lançamentos Automáticos de ICMS

Parametrização de CFOP – Crédito Presumido Transporte \- Estorno

__Localização__:  Menu Estadual, Módulo Lançamentos Automáticos ICMS, item Parâmetros 🡪 Imposto sobre Serviço de Transporte 🡪 Crédito Presumido 🡪 Por CFOP \- Estorno

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS565161

Andréa Rocha

Criação da parametrização de CFOP’s para geração das anulações no cálculo do crédito presumido de transporte\.

04/09/2023

Sumário

[1\.	Regras Gerais	2](#_Toc144735490)

[2\.	Regras de Funcionamento dos Campos	2](#_Toc144735491)

# <a id="_Toc144735490"></a>

# Regras Gerais

Os dados parametrizados neste item são utilizados na rotina de geração do cálculo do crédito presumido de transporte, para recuperar as notas fiscais de entrada de Estorno, realizada no menu “Lançamentos 🡪 Cálculo dos Lançamentos” do módulo Lançamentos Automáticos\.

__Botões da barra de menu__:

CONFIRMA

Opção para salvar as informações da parametrização incluída ou alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc144735491"></a>Regras de Funcionamento dos Campos

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

MFS565161

CFOP’s

Alfanumérico

__S__

S

Neste campo é exibida a lista dos CFOP’s \(SAFX2012\) para seleção do usuário, considerando *apenas* as operações de entrada \(códigos iniciados por “1”, “2” ou “3”\)\.

Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade \(para não exibir códigos repetidos\)\.

Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

MFS565161

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado\.

Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

MFS565161

       = = = = = =

