# MTZ_EFD_Parametros_Registro_1400_Padrao_EPPP_CFO

> Fonte: MTZ_EFD_Parametros_Registro_1400_Padrao_EPPP_CFO.docx






THOMSON REUTERS

Módulo EFD- Escrituração Fiscal Digital

Parametrização de CFOP – Registro 1400 - EPPP


Localização: Menu Sped, Módulo: EFD- Escrituração Fiscal Digital, item menu Parâmetros  Registro 1400  Padrão  Aquisição de Produtos Primários (EPPP-PR)   Por CFOP





DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4

























## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina de geração padrão do registro 1400, Aquisição de Produtos Primários - EPPP, realizada no menu “Geração  Meio Magnético” do módulo Sped Fiscal.


## Layout da Tela







Botões da barra de menu:



## Regras de Funcionamento dos Campos





= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS25117 | Andréa Rocha | Criação da parametrização de CFOP’s para geração do registro 1400 (EPPP). | 21/08/2019 |
|  |  |  |  |


| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário.  Somente devem ser mostrados os estabelecimentos do estado do “PR”. Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. | MFS25117 |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) para seleção do usuário, considerando apenas as operações de entrada (códigos iniciados por “1”, “2” ou “3”).  Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS25117 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS25117 |
