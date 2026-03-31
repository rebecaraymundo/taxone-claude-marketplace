# MTZ_EFD_Parametros_Registro_C176_CFOP_NFs_Saida

> Fonte: MTZ_EFD_Parametros_Registro_C176_CFOP_NFs_Saida.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de CFOP – NF’s Saida com direito ao Ressarcimento (C176)


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro C176  NF’s Saída c/direito a Ressarcimento  CFOP




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4

























## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina de pré-geração do registro C176, realizada no menu “Pré-Geração  Registro C176” do módulo Sped Fiscal.

Alteração da MFS9749:
Esta parametrização passou a disponibilizar também CFOP’s de entrada, onde serão parametrizadas as devoluções das saídas com direito a ressarcimento/crédito de ICMS-ST.


## Layout da Tela








Botões da barra de menu:



## Regras de Funcionamento dos Campos








= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS2772 | Atendimento a Portaria CAT 158 | Criação da parametrização de CFOP’s para geração dos dados do registro C176. | 25/05/2016 |
| MFS9749 | Tratamento das Devoluções de Saídas c/direito à Ressarcimento | Inclusão das operações de entrada para o tratamento das devoluções de saídas c/direito à ressarcimento. | 17/02/2017 |
|  |  |  |  |


| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário.  Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. |  |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) para seleção do usuário, considerando apenas as operações de saída (códigos iniciados por “5”, “6” ou “7”).  Alteração da MFS9749: A parametrização foi alterada para disponibilizar também os CFOP’s de entrada, para que sejam parametrizadas também as devoluções.  Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
