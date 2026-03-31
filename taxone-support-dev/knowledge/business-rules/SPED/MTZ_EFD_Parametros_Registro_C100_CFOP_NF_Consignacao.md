# MTZ_EFD_Parametros_Registro_C100_CFOP_NF_Consignacao

> Fonte: MTZ_EFD_Parametros_Registro_C100_CFOP_NF_Consignacao.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de CFOP – NF’s em Consignação


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro C100  NF’s em Consignação - CFOP




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Regras de Funcionamento dos Campos	2


## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina de geração do meio magnético do registro C100, para identificar as notas fiscais de consignação.  Essas notas serão utilizadas por um parâmetro específico (Dados Iniciais), que vai definir a forma de preencher o campo 6 – Código do Situação do registro C100.



Botões da barra de menu:



## Regras de Funcionamento dos Campos








= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS75220 | Andréa Rocha | Criação da parametrização de CFOP’s para NF’s em consignação | 25/11/2021 |
|  |  |  |  |


| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário.  Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. |  |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) para seleção do usuário.  Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
