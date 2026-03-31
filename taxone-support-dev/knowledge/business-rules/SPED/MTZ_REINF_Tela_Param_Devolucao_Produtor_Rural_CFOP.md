# MTZ_REINF_Tela_Param_Devolucao_Produtor_Rural_CFOP

> Fonte: MTZ_REINF_Tela_Param_Devolucao_Produtor_Rural_CFOP.docx






THOMSON REUTERS

Módulo REINF

Devoluções de Aquisição de Produtor Rural (R-2055)


Localização: Menu SPED, Módulo EFD-REINF, item Parâmetros  Devoluções de Aquisição de Produtor Rural (R-2055)




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4
## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina da geração do REINF, evento R-2055 (Aquisição de Produção Rural), para a identificação das operações de devolução.


## Layout da Tela








Botões da barra de menu:



## Regras de Funcionamento dos Campos








= = = = = =

| OS/CH/MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-58343 | Alessandra Cristina Navatta | Criação da parametrização de CFOP’s p/a operações de devolução a serem deduzidas dos totais das aquisições por produtor rural. | 22/01/2021 |
|  |  |  |  |
|  |  |  |  |


| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH/MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login.   Serão disponibilizados para seleção apenas os estabelecimentos centralizadores ou centralizados em algum centralizador da parametrização das obrigações federais (módulo Parâmetros, menu Preliminares > Centralização da Escrituração de Obrigações Federais). | MFS-58343 |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) para seleção do usuário, considerando apenas as operações de saída (códigos iniciados por “5”, “6” ou “7”).  Quando existir mais de uma ocorrência do mesmo CFOP, com validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS-58343 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Serão disponibilizados para seleção apenas os estabelecimentos centralizadores ou centralizados em algum centralizador da parametrização das obrigações federais (módulo Parâmetros, menu Preliminares > Centralização da Escrituração de Obrigações Federais).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS-58343 |
