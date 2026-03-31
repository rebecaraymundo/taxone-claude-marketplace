# MTZ_EFD_Parametros_Registro_C177_CFOP

> Fonte: MTZ_EFD_Parametros_Registro_C177_CFOP.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de CFOP – Registro C177 – Comércio Atacadista


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro C177 – Comércio Atacadista  CFOP




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4

























## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina de geração do registro C177, realizada no menu na Geração do Meio Magnético do módulo Sped Fiscal.

## Layout da Tela








Botões da barra de menu:



## Regras de Funcionamento dos Campos








= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS80572 | Andréa Rocha | Criação da parametrização de CFOP’s para geração dos dados do registro C177 – Comércio Atacadista. | 11/11/2022 |
|  |  |  |  |


| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário.  Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. |  |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista de todos os CFOP’s (SAFX2012) para seleção do usuário.  Quando existir mais de uma ocorrência do mesmo CFOP, mas com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”, “Marcar Entradas” e “Desmarcar Entradas” e “Marcar Saídas” e “Desmarcar Saídas”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
