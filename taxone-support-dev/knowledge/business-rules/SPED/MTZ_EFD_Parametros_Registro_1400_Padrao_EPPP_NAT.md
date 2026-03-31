# MTZ_EFD_Parametros_Registro_1400_Padrao_EPPP_NAT

> Fonte: MTZ_EFD_Parametros_Registro_1400_Padrao_EPPP_NAT.docx






THOMSON REUTERS

Módulo EFD- Escrituração Fiscal Digital

Parametrização de CFOP/Natureza – Registro 1400 - EPPP


Localização: Menu Sped, Módulo: EFD- Escrituração Fiscal Digital, item Parâmetros  Registro 1400  Padrão  Aquisição de Produtos Primários (EPPP-PR)   Por CFOP / Natureza de Operação



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
| MFS25117 | Andréa Rocha | Criação da parametrização de CFOP/Natureza para geração do registro 1400 (EPPP). | 21/08/2019 |
|  |  |  |  |
|  |  |  |  |


| SELECIONA GRUPO | Ao clicar nesta opção, abrirá uma janela de seleção dos grupos de relacionamento das tabelas do Mastersaf, e o usuário deverá selecionar o grupo e estabelecimento. Na abertura da tela esta janela será exibida automaticamente, obrigando o usuário a selecionar o Grupo e Estabelecimento. O grupo e estabelecimento selecionados serão exibidos nos campos “Estabelecimento” e “Grupo Natureza”.  Caso tenha sido informado um estabelecimento no login, serão disponibilizados apenas os grupos aos quais este estabelecimento esteja associado. Caso contrário, serão disponibilizados todos os grupos e estabelecimentos da Empresa do login. Somente devem ser mostrados os estabelecimentos do estado do “PR”. |
| --- | --- |
| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Neste campo será exibido o estabelecimento selecionado na janela de seleção do Grupo. | MFS25117 |
| Grupo Natureza | Alfanumérico | S | N |  | Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Seleciona Grupo” da barra de menu. | MFS25117 |
| CFOP’s / Naturezas de Operação | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s / Naturezas de Operação para seleção do usuário, considerando apenas as operações de entrada (códigos de CFOP iniciados por “1”, “2” ou “3”).  Quando existir mais de uma ocorrência do mesmo CFOP/Natureza, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS25117 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS25117 |
