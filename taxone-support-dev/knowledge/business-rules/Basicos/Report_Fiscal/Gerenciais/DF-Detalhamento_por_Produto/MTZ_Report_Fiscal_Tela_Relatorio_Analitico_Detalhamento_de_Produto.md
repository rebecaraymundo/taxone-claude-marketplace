# MTZ_Report_Fiscal_Tela_Relatorio_Analitico_Detalhamento_de_Produto

- **Fonte:** MTZ_Report_Fiscal_Tela_Relatorio_Analitico_Detalhamento_de_Produto.docx
- **Modificado:** 2023-11-09
- **Tamanho:** 32 KB

---

__Relatório Analítico por Documento__

__Localização__: Menu Básicos, Módulo Report Fiscal, Gerenciais, Documentos Fiscais, Analíticos, Detalhamento por Produto

__DOCUMENTO DE REQUISITO__

###### DR

###### Nome

__Descrição__

OS4073

Criação do Relatório Analítico por Produto

Validação das Críticas da Tela

__REGRAS DE NEGÓCIO__

#### Cód\.

### Descrição

### DR

RN01

__Campo “Período”:__

Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA  a  DD/MM/AAAA\.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para criar o relatório\.

Obrigatoriedade: S

Obs\.: No campo da data final, o usuário deverá informar um período maior ou igual ao período inicial\. Caso informe um período menor do que o período inicial retornar a mensagem: __“O período final informado deve ser maior ou igual ao período inicial”\.__

OS4073

RN02

__Campo “Seleção de CFOP’s”:__

Este campo exibe todos os códigos fiscais\.  Exibir os CFOP’s da SAFX2012\. 

OS4073

RN03

__Botão “Marcar Todos”:__

Este botão ao ser acionado, deverá selecionar todos os códigos CFOP's automaticamente\. 

OS4073

RN04

__Botão “Desmarcar Todos”:__

Este botão ao ser acionado, deverá  desmarcar todos os códigos CFOP's automaticamente \. 

OS4073

RN05

__Botão “Marcar Entradas”:__

Este botão ao ser acionado, deverá selecionar todos os códigos CFOP's de entradas automaticamente \(códigos iniciados por 1, 2 ou 3\)\. 

OS4073

RN06

__Botão “Desmarcar Entradas”:__

Este botão ao ser acionado, deverá desmarcar todos os códigos CFOP's de entradas automaticamente \(códigos iniciados por 1, 2 ou 3\)\. 

OS4073

RN07

__Botão “Marcar Saídas”:__

Este botão ao ser acionado, deverá selecionar todos os códigos CFOP's de saída automaticamente \(códigos iniciados por 5, 6 ou 7\)\. 

OS4073

RN08

__Botão “Desmarcar Saída”:__

Este botão ao ser acionado, deverá desmarcar todos os códigos CFOP's de saída \(códigos iniciados por 5, 6 ou 7\)\. 

OS4073

RN09

__Campo “UF”:__

Campo para informar a UF dos estabelecimentos que deseja para a geração do relatório\.

OS4073

RN10

__Campo “Estabelecimento”:__

Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do Report Fiscal\. Caso o usuário selecione uma UF específica, demonstrar apenas os estabelecimentos pertencentes ao Estado selecionado\.

OS4073

RN11

__Botão “Marcar Todos”:__

Este botão ao ser acionado, deverá selecionar todos os estabelecimentos automaticamente\. 

OS4073

RN12

__Botão “Desmarcar Todos”:__

Este botão ao ser acionado, deverá  desmarcar todos os estabelecimentos automaticamente \. 

OS4073

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

