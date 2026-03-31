# MTZ_EFD_Parametros_Registro_C176_NAT_NFs_Saida

> Fonte: MTZ_EFD_Parametros_Registro_C176_NAT_NFs_Saida.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de CFOP / Natureza de Operação – NF’s Saida com direito ao Ressarcimento (C176)


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro C176  NF’s Saída c/direito a Ressarcimento  CFOP / Natureza de Operação



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
| MFS9749 | Tratamento das Devoluções de Saídas c/direito à Ressarcimento | Inclusão das operações de entrada para o tratamento das devoluções de saídas c/direito à ressarcimento. | 17/02/2017 |
|  |  |  |  |
|  |  |  |  |


| SELECIONA GRUPO | Ao clicar nesta opção, abrirá uma janela de seleção dos grupos de relacionamento das tabelas do Mastersaf, e o usuário deverá selecionar o grupo e estabelecimento. Na abertura da tela esta janela será exibida automaticamente, obrigando o usuário a selecionar o Grupo e Estabelecimento. O grupo e estabelecimento selecionados serão exibidos nos campos “Estabelecimento” e “Grupo Natureza”.  Caso tenha sido informado um estabelecimento no login, serão disponibilizados apenas os grupos aos quais este estabelecimento esteja associado. Caso contrário, serão disponibilizados todos os grupos e estabelecimentos da Empresa do login. |
| --- | --- |
| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Neste campo será exibido o estabelecimento selecionado na janela de seleção do Grupo. |  |
| Grupo Natureza | Alfanumérico | S | N |  | Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Seleciona Grupo” da barra de menu. |  |
| CFOP’s/Natureza de Operação | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s / Naturezas de Operação para seleção do usuário, considerando apenas as operações de saída (códigos de CFOP iniciados por “5”, “6” ou “7”).  Alteração da MFS9749: A parametrização foi alterada para disponibilizar também os CFOP’s de entrada, para que sejam parametrizadas também as devoluções.  Quando existir mais de uma ocorrência do mesmo CFOP/Natureza, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
