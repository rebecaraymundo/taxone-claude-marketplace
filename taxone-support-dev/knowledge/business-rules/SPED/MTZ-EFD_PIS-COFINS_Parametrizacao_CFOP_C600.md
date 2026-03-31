# MTZ-EFD PIS-COFINS_Parametrizacao_CFOP_C600

> Fonte: MTZ-EFD PIS-COFINS_Parametrizacao_CFOP_C600.docx






THOMSON REUTERS

Módulo EFD-Contribuições

Parametrização de CFOP – Registro C600


Localização: Menu Sped, Módulo: EFD- Escrituração Fiscal Digital das Contribuições, item Parâmetros  Registro C600  Por CFOP




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4

























## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina de geração do registro C600, realizada no menu “Obrigações  Geração dos Registros” do módulo Sped Contribuições.


## Layout da Tela








Botões da barra de menu:



## Regras de Funcionamento dos Campos





= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS29621 | Andréa Rocha | Criação da parametrização de CFOP’s para geração do registro C600. | 16/08/2019 |
|  |  |  |  |


| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário.  Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. |  |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) para seleção do usuário, considerando apenas as operações de saída (códigos iniciados por “5”, “6” ou “7”).  Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
