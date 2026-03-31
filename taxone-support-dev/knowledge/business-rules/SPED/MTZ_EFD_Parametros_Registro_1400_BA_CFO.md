# MTZ_EFD_Parametros_Registro_1400_BA_CFO

> Fonte: MTZ_EFD_Parametros_Registro_1400_BA_CFO.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de CFOP – Registro 1400 - BA – CFOPs

Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item menu Parâmetros à Registro 1400  à Específico por UF à BA – CFOPs (Compras, Vendas e Devoluções)






DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4

























## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina de pré-geração do Registro 1400 – DMA BA, realizada no menu “Pré-Geração à Registro 1400 – DMA BA” do módulo SPED Fiscal.
Esta tela é a mesma utilizada no módulo da GIA BA (Item de menu: Parâmetros à Quadros 30/31 – CFOPs (Compras, Vendas e Devoluções)).


## Layout da Tela



Estabelecimento [XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]

-- CFOP’s --------------------------------------------------------------------------------------------------------------------------
Código-Descrição
----------------------------------------------------------------------------------------------------------------------------------------
[ x ] xxxx -xxxxxxxxxxxxxxxxxx
[ x ] xxxx -xxxxxxxxxxxxxxxxxx
[Selecionar Todos] [Desmarcar Todos]




Botões da barra de menu:



## Regras de Funcionamento dos Campos





= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS21172 | Andréa Rocha | Criação da parametrização de CFOP’s para a pré-geração do registro 1400 – DMA BA | 17/09/2019 |
|  |  |  |  |


| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário.  Somente devem ser mostrados os estabelecimentos do estado do “BA”. Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. | MFS21172 |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) para seleção do usuário, considerando todos (códigos iniciados por “1”, “2” ou “3” ou “5”, “6” ou “7”).  Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS21172 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS21172 |
