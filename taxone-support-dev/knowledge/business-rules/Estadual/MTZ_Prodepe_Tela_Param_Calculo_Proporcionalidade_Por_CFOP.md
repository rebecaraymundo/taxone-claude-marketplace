# MTZ_Prodepe_Tela_Param_Cálculo_Proporcionalidade_Por_CFOP

> Fonte: MTZ_Prodepe_Tela_Param_Cálculo_Proporcionalidade_Por_CFOP.docx






THOMSON REUTERS

Módulo PRODEPE

Tela de Parametrização de CFOP – Cálculo de Proporcionalidade – Por CFOP


Localização: Menu Estadual, Módulo: Prodepe  Parâmetros  Incentivo - Industria  Cálculo de Proporcionalidade – Por CFOP






DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4

























## Regras Gerais


Os dados parametrizados neste item serão utilizados na rotina de geração dos Livros Incentivados e Não Incentivados no Módulo do Prodepe para os CFOP’s que devem serem rateados proporcionalmente de acordo com o percentual das saídas, nos Livros de Apuração 'Incentivada' e 'Não Incentivada', de acordo com o disposto nas alíneas “c” e “e” do inciso VIII do Art. 1º da Portaria 239/01.

O novo submenu “Cálculo de Proporcionalidade – Por CFOP” deverá ser incluído no Menu: Parâmetros  Incentivo – Indústria, abaixo do submenu “Produtos Incentivados”.



## Layout da Tela


v




Botões da barra de menu:


## Regras de Funcionamento dos Campos





| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS62923 | Rogério Ohashi | Criação de novo menu de parametrização de CFOP’s para serem utilizados no Cálculo de Proporcionalidade. | 23/04/2021 |


| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário. Somente devem ser mostrados os estabelecimentos cujo estado seja igual a Pernambuco. | MFS62923 |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) para seleção do usuário, somente os CFOP’s referente a entradas, que iniciados com ‘1’, ‘2’ e ‘3’.  Quando existir mais de uma ocorrência do mesmo CFOP, com validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS62923 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado e que pertençam a Pernambuco.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS62923 |
