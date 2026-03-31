# MTZ-LAICMS-Param_Creditos_Transporte_Por_Natureza

- **Fonte:** MTZ-LAICMS-Param_Creditos_Transporte_Por_Natureza.docx
- **Modificado:** 2023-09-12
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Módulo Lançamentos Automáticos de ICMS

Parametrização de Extensão CFOP – Crédito Presumido Transporte \- Estorno

__Localização__: Menu Estadual, Módulo Lançamentos Automáticos ICMS, item Parâmetros 🡪 Imposto sobre Serviço de Transporte 🡪 Crédito Presumido 🡪 Por Extensão de CFOP \- Estorno

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS565161

Andréa Rocha

Criação da parametrização de Extensão de CFOP’s para geração das anulações no cálculo do crédito presumido de transporte

21/08/2019

Sumário

[1\.	Regras Gerais	2](#_Toc144735668)

[2\.	Regras de Funcionamento dos Campos	2](#_Toc144735669)

# <a id="_Toc144735668"></a>Regras Gerais

Os dados parametrizados neste item são utilizados na rotina de geração do cálculo do crédito presumido de transporte, para recuperar as notas fiscais de entrada de Estorno, realizada no menu “Lançamentos 🡪 Cálculo dos Lançamentos” do módulo Lançamentos Automáticos\.

__Botões da barra de menu__:

SELECIONA GRUPO

Ao clicar nesta opção, abrirá uma janela de seleção dos grupos de relacionamento das tabelas do Mastersaf, e o usuário deverá selecionar o grupo e estabelecimento\. Na abertura da tela esta janela será exibida automaticamente, obrigando o usuário a selecionar o Grupo e Estabelecimento\. O grupo e estabelecimento selecionados serão exibidos nos campos “Estabelecimento” e “Grupo Natureza”\.

Caso tenha sido informado um estabelecimento no login, serão disponibilizados apenas os grupos aos quais este estabelecimento esteja associado\. Caso contrário, serão disponibilizados todos os grupos e estabelecimentos da Empresa do login\. 

CONFIRMA

Opção para salvar as informações da parametrização incluída ou alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc144735669"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

<a id="_Hlk475116293"></a>Estabelecimento

Alfanumérico 

__S__

N

Neste campo será exibido o estabelecimento selecionado na janela de seleção do Grupo\.

MFS565161

Grupo Natureza

Alfanumérico 

__S__

N

Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Seleciona Grupo” da barra de menu\. 

MFS565161

CFOP’s / Naturezas de Operação

Alfanumérico

__S__

S

Neste campo é exibida a lista dos CFOP’s / Naturezas de Operação para seleção do usuário, considerando *apenas* as operações de entrada \(códigos de CFOP iniciados por “1”, “2” ou “3”\)\.

Quando existir mais de uma ocorrência do mesmo CFOP/Natureza, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade \(para não exibir códigos repetidos\)\.

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

