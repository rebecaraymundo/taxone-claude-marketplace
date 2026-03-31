# MTZ-Job_Servidor-Importacao-automatica

- **Fonte:** MTZ-Job_Servidor-Importacao-automatica.docx
- **Modificado:** 2026-01-06
- **Tamanho:** 59 KB

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

MFS642694

Andréa Rocha 

O objetivo é retornar com o parâmetro ‘Validade \(X2013\)’ para a tela, uma vez que o parâmetro “Sobrepor Registro” foi incluído na tela\.

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

- __Regra p/ campo Validade__ __\(X2013\);__

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

Este campo não deve ser apresentado em tela\.

MFS41944

MFS\-45844

MFS642694

__RN04__

Regra p/ campo Data Averbação \(X48\)

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

MFS41944

__RN05__

- __Regra p/ campo Importar Retificador de Retenções \(X53/X530\)__

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

MFS41944

__RN06__

\[EXCLUSÃO MFS\-92334\] Regra p/ campo Importar DARFs Complementares \(X75/X751\)

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

MFS41944

MFS\-92334

__RN07__

\[EXCLUSÃO MFS\-92334\] Regra p/ campo Validar CEP \(X04\)

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

MFS41944

MFS\-92334

__RN08__

__Regra p/ campo Grupo \(X188\)__

O campo Grupo X188 deve ser do tipo Listbox, onde deveram ser listados todos os grupos existentes na tabela de grupos, independente do estabelecimento selecionado\.

Campo não obrigatório\.

MFS41944

__RN09__

__Regra p/ campo Grupo \(X189\)__

O campo Grupo X189 deve ser do tipo Listbox, onde deveram ser listados todos os grupos existentes na tabela de grupos, independente do estabelecimento selecionado\.

Campo não obrigatório\.

MFS41944

__RN10__

__Regra para campo Replicar para os Estabelecimentos__

O campo deve ser do tipo checkbox, sendo a opção default desmarcado\.

Quando for marcado, deve habilitar o quadro de estabelecimentos para a seleção de um ou mais estabelecimentos\.

MFS41944

__RN11__

__Regra para Botão Pesquisar – Quadro de Estabelecimento__

__Pesquisar \(Estabelecimento\):__ O botão de pesquisa deve ser incluído antes do quadro de Estabelecimentos, com um campo para informar os dados da pesquisa\.  A pesquisa pode ser feita pela coluna “código do estabelecimento” ou pela coluna “descrição do estabelecimento”, pode ser informada uma palavra ou parte de uma palavra de uma das colunas para se fazer a pesquisa\.

MFS41944

__RN12__

__Regra para Quadro de Estabelecimentos__

Devem ser exibidos todos os estabelecimentos que estejam licenciados e que o usuário possua acesso no Concert, menos o estabelecimento selecionado no campo Estabelecimento\.

Deve\-se ter a opção de selecionar todos os estabelecimentos\.

MFS41944

__RN13__

__\[INCLUSÃO \- MFS\-78772\] Regra para o campo Sobrepor Registros__

O campo deve ser do tipo checkbox, sendo a opção default __marcado__\.

__Se__ o campo estiver __marcado__, na importação da tabela temporária \(SAFX\), cada registro a ser importado que tenha algum campo, __não chave__, diferente do encontrado na base, __é sobreposto__, ou seja, é atualizado com as novas informações, __sendo considerado registro alterado__\. 

__Se__ o campo estiver __desmarcado__, cada registro a ser importado que tiver algum campo, __não chave__, diferente do encontrado na base, __não é atualizado__, __sendo considerado como registro ignorado__\.

*Obs\.: Incluir abaixo do Campo “Validar CEP \(X04\)”*

MFS78772

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

