# MTZ-Job_Servidor-Importacao-automatica

- **Fonte:** MTZ-Job_Servidor-Importacao-automatica.docx
- **Modificado:** 2026-01-06
- **Tamanho:** 65 KB

---

# Módulo – Job Servidor

#  Importação Automática \(Somente para o TAX ONE\)

__Localização: __

__Módulo__: Básicos à Job Servidor

__Menu__: Importação à Importação Automática à Parametrização

##### DOCUMENTO DE REQUISITO

###### MFS

###### Nome

__Descrição__

MFS41944

Andréa Rocha 

O objetivo é criar uma tela para informar os parâmetros necessários para a rotina de importação automática do TAX ONE\.

MFS\-45844

Alessandra Cristina Navatta

Excluir os parâmetros ‘Log para Produtos Idênticos \(X2013\)’ e ‘Validade \(X2013\)’ da tela\. 

Estes parâmetros não devem ser apresentados na tela, pois os mesmos só tem função, quando o parâmetro ‘Sobrepor Reg’ estiver com ‘N’ e na importação automática, sempre estamos considerando como ‘S’

MFS\-78772

Rogério Ohashi

O objetivo é criar o parâmetro “Sobrepor Registro” na tela de parametrização da rotina de importação automática do TAX ONE\.

MFS\-92334

Alessandra Cristina Navatta

Excluir os parâmetros ‘Importar DARFs Complementares \(X75/X751\)’ e ‘Importar DARFs Complementares \(X75/X751\)’

MFS542820

Andréa Rocha

Incluir um parâmetro que permita a exportação automática dos dados das SAFXs, cujos registros não foram importados porque estão com erros\.  A exportação deve ser feita antes da exclusão dos dados\.

## REGRAS DE NEGÓCIO

#### Cód\.

#### Descrição

#### MFS

__RN00__

__Regras Gerais:__

Na programação da importação existem alguns parâmetros específicos relacionados com algumas tabelas SAFXs, estes parâmetros precisam ser informados pelo usuário para definir a forma de importação das tabelas\. Nesta tela os parâmetros serão informados uma única vez para cada estabelecimento da empresa, e serão armazenados numa tabela que será utilizada na rotina de importação automática do TAX ONE, de maneira que não haja dependência de se informar estes dados no momento da importação\. 

MFS41944

__RN01__

Regra p/ campo Estabelecimento

Campo deve ser do tipo Listbox, devem ser exibidos os estabelecimentos que estejam licenciados e que o usuário possua acesso no Concert\.

MFS41944

__RN02__

- __\[EXCLUSÃO MFS\-45844\]__ __Regra p/ campo Log para Produtos Idênticos \(X2013\);__

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

Este campo não deve ser apresentado em tela\.

MFS41944

MFS\-45844

__RN03__

- __\[EXCLUSÃO MFS\-45844\]__ __Regra p/ campo Validade__ __\(X2013\);__

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

Este campo não deve ser apresentado em tela\.

MFS41944

MFS\-45844

__RN04__

Regra p/ campo Data Averbação \(X48\)

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

MFS41944

__RN05__

- __\[EXCLUSÃO MFS\-92334\]__ __Regra p/ campo Importar Retificador de Retenções \(X53/X530\)__

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

MFS41944

MFS\-92334

__RN06__

\[EXCLUSÃO MFS\-92334\] Regra p/ campo Importar DARFs Complementares \(X75/X751\)

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

MFS41944

MFS\-92334

__RN07__

Regra p/ campo Validar CEP \(X04\)

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

MFS41944

__RN08__

__\[INCLUSÃO \- MFS\-78772\] Regra para o campo Sobrepor Registros__

O campo deve ser do tipo checkbox, sendo a opção default __marcado__\.

__Se__ o campo estiver __marcado__, na importação da tabela temporária \(SAFX\), cada registro a ser importado que tenha algum campo, __não chave__, diferente do encontrado na base, __é sobreposto__, ou seja, é atualizado com as novas informações, __sendo considerado registro alterado__\. 

__Se__ o campo estiver __desmarcado__, cada registro a ser importado que tiver algum campo, __não chave__, diferente do encontrado na base, __não é atualizado__, __sendo considerado como registro ignorado__\.

*Obs\.: Incluir abaixo do Campo “Validar CEP \(X04\)”*

MFS78772

__RN09__

__\[INCLUSÃO \- MFS\-542820\] Regra para o campo Exportar Registros não Importados__

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

__Se__ o campo estiver __marcado__, os registros que não foram importados de cada SAFX, devido a algum erro na importação, serão exportados e gravados em um arquivo no formato CSV\. 

__Se__ o campo estiver __desmarcado__, os registros que não foram importados porque estão com erros, serão excluídos, conforme o padrão da rotina de importação automática\.

Obs\.:  Quando o parâmetro estiver marcado, verificar a regra “__Regra \- Exportar Registros não Importados”\.__

MFS542820

__RN10__

__Regra p/ campo Grupo \(X188\)__

O campo Grupo X188 deve ser do tipo Listbox, onde deveram ser listados todos os grupos existentes na tabela de grupos, independente do estabelecimento selecionado\.

Campo não obrigatório\.

MFS41944

__RN11__

__Regra p/ campo Grupo \(X189\)__

O campo Grupo X189 deve ser do tipo Listbox, onde deveram ser listados todos os grupos existentes na tabela de grupos, independente do estabelecimento selecionado\.

Campo não obrigatório\.

MFS41944

__RN12__

__Regra para campo Replicar para os Estabelecimentos__

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

Quando for marcado, deve habilitar o quadro de estabelecimentos para a seleção de um ou mais estabelecimentos\.

MFS41944

__RN13__

__Regra para Botão Pesquisar – Quadro de Estabelecimento__

__Pesquisar \(Estabelecimento\):__ O botão de pesquisa deve ser incluído antes do quadro de Estabelecimentos, com um campo para informar os dados da pesquisa\.  A pesquisa pode ser feita pela coluna “código do estabelecimento” ou pela coluna “descrição do estabelecimento”, pode ser informada uma palavra ou parte de uma palavra de uma das colunas para se fazer a pesquisa\.

MFS41944

__RN14__

__Regra para Quadro de Estabelecimentos__

Devem ser exibidos todos os estabelecimentos que estejam licenciados e que o usuário possua acesso no Concert, menos o estabelecimento selecionado no campo Estabelecimento\.

Deve\-se ter a opção de selecionar todos os estabelecimentos\.

MFS41944

__RN15__

__\[INCLUSÃO \- MFS\-542820\] Regra \- Exportar Registros não Importados__

Quando for selecionado o parâmetro para exportar os registros que estão com erro e não foram importados, deve\-se executar a rotina de Exportação de Dados para Tabelas Temporárias \(menu: Exportação Dados 🡪 Tabelas Temporárias \(SAFXs\)\)\.

Para cada SAFX que for importada, os registros que não foram importados por algum erro, devem ser gravados em um arquivo no formato CSV\.  Portanto, antes de se fazer a exclusão/limpeza de cada SAFX, após os seus dados serem importados, deve\-se executar a package EXPORTACAO\_SAFX\_CSV\_FPROC, passando a SAFX \(EX\.: SAFX01\), para fazer a gravação dos dados não importados num arquivo em formato CSV\.

MFS542820

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

