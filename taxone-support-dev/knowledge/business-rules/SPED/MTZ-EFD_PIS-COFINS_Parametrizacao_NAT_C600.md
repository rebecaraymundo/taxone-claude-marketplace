# MTZ-EFD PIS-COFINS_Parametrizacao_NAT_C600

> Fonte: MTZ-EFD PIS-COFINS_Parametrizacao_NAT_C600.docx






THOMSON REUTERS

Módulo EFD-Contribuições

Parametrização Por Extensão CFOP – Registro C600


Localização: Menu Sped, Módulo: EFD- Escrituração Fiscal Digital das Contribuições, item Parâmetros  Registro C600  Por Extensão CFOP



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
| MFS29621 | Andréa Rocha | Criação da parametrização de Extensão CFO para geração do registro C600. | 16/08/2019 |
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
| Extensão CFO | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s / Naturezas de Operação para seleção do usuário, considerando apenas as operações de saída (códigos de CFOP iniciados por “5”, “6” ou “7”).  Quando existir mais de uma ocorrência do mesmo CFOP/Natureza, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
