# MTZ-eSocial-Parametros-Informacoes-dos-Setor-do-Estabelecimento

> Fonte: MTZ-eSocial-Parametros-Informacoes-dos-Setor-do-Estabelecimento.docx






THOMSON REUTERS

Módulo eSocial

Parâmetros Setores do Estabelecimento


Localização: Menu Sped, Módulo: Informações para o ESOCIAL, item Parâmetros  Informações dos Setores do Estabelecimento




DOCUMENTO DE REQUISITO


Sumário

1.	Introdução	2
2.	Layout da Tela	2
3.	Funcionamento da Tela	3
4.	Botões da barra de menu:	4
5.	Regras de Funcionamento dos Campos	4
6.	Validações	7
Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.

## Introdução


Esta tela tem objetivo parametrizar os setores de um estabelecimento centralizador, que serão utilizados na geração do registro S-1020-Lotações.

A relação dos setores (SAFX2037) ao estabelecimento possui datas inicial e final de vigência.



## Layout da Tela

Título: Informações dos Setores do Estabelecimento

Estabelecimento [XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]
Grupo: [XX]

Informar Código/Descrição para Pesquisa [                                            ] ( )Código    ( )Descrição
-- Relação de Setores--------------------------------------------------------------------------------------------------------------------------
Código - Validade - Descrição
-----------------------------------------------------------------------------------------------------------------------------------------------------
[ x ] xxxxxx- dd/mm/aaaa - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[ x ] xxxxxx- dd/mm/aaaa - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[    ] xxxxxx- dd/mm/aaaa - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[Selecionar Todos] [Desmarcar Todos]

Replicar para os Estabelecimentos
[ x ] xxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[ x ] xxxxxx- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[    ] xxxxxx- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[Selecionar Todos] [Desmarcar Todos]


Os dados que definem a chave de identificação da parametrização são os seguintes:

Empresa
Estabelecimento
Grupo do Setor
Código do Setor
Data Validade do Setor

A tabela onde a parametrização é gravada é ESOCIAL_PAR_SETOR_ESTAB.


## Funcionamento da Tela








## Botões da barra de menu:





## Regras de Funcionamento dos Campos






## Validações



Críticas a serem realizadas antes de salvar a operação:

RN01: Campos Obrigatórios
Validações de Campos Obrigatórios não preenchidos.
Quando o campo é obrigatório e não estiver preenchido, exibir mensagem padrão.
A obrigatoriedade dos campos está definida no tópico “5 – Regras de Funcionamento dos Campos”.


= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS25900 | Liliane Assaf | Criação da parametrização de setores relacionados aos Estabelecimentos Centralizadores. | 15/04/2019 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| Passo | Acionador | Descrição |
| --- | --- | --- |
| 1 | Usuário | Usuário seleciona o item de menu Parâmetros  Informações dos Setores do Estabelecimento |
| 2 | Sistema | Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo). Demonstrar o grupo e o estabelecimento para seleção. Ver definição da tela no tópico “4 – Botões da Barra de Menu”, menu “SELECIONAR GRUPO”. |
| 3 | Usuário | Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo. |
| 4 | Sistema | Abre a tela de Informação dos Setores do Estabelecimento, com os campos Estabelecimento e Grupo preenchidos e bloqueados e a relação dos Setores (SAFX2037) atualizada. Vide regra do campo “Relação de Produtos” descrita no tópico “5 – Regras de Funcionamento dos Campos”. |
| 5 | Usuário | Seleciona um ou vários setores. |
| 6 | Usuário | Seleciona botão confirma. |
| 7 | Sistema | Executa validações descritas no tópico 5- Validações.  Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva. |
| 8 | Usuário | Seleciona outras ações disponíveis na barra de menu da janela. Vide tópico “4 - Botões da barra de menu” |


| SELECIONAR GRUPO | Ao clicar nesta opção será aberta a janela de seleção dos grupos/estabelecimentos cadastrados no Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo). Apresentar os registros do Cadastro de Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo) considerando: Apenas os estabelecimentos centralizadores da parametrização das obrigações federais (módulo Parâmetros, menu Preliminares > Centralização da Escrituração de Obrigações Federais).  Código da tabela igual a ‘2037’; Demonstrar o grupo e o estabelecimento para seleção do usuário. |
| --- | --- |
| CONFIRMA | Opção para salvar as informações da parametrização incluída, alterada ou excluída. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Neste campo são apresentados o código e a razão social do estabelecimento selecionado na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu.  O campo Estabelecimento é apresentado bloqueado. Observação: Esta tela trabalha apenas com estabelecimentos centralizadores definidos na parametrização das obrigações federais (módulo Parâmetros, menu Preliminares > Centralização da Escrituração de Obrigações Federais). |  |
| Grupo | Alfanumérico | S | N |  | Este campo apresenta o grupo do Cadastro de Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo) selecionado na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu.  O campo Grupo é apresentado bloqueado. |  |
| Informar código/descrição para pesquisa | Alfanumérico | N | S |  | Neste campo o usuário poderá informar os caracteres iniciais do código, ou da descrição do Setor a serem pesquisados, através do botão “Pesquisar”. |  |
| - Código  - Descrição | Radio Button | N | S | Opção default:     “Código” | Estas duas opções indicam a forma como será feita a pesquisa dos Setores a serem disponibilizados para seleção do usuário no campo “Relação dos Setores”. As opções são alternativas, pois o filtro dos setores é feito pelo código, ou pela descrição do setor. |  |
| Pesquisar | Botão | N | S |  | Ao clicar nesta opção, será feita a pesquisa dos setores, de acordo com o código ou a descrição informada, e a lista dos setores será refeita e demonstrada para a seleção do usuário.  Esta pesquisa considera os setores cujo código ou descrição, conforme o caso, tenha as mesmas iniciais do código ou da descrição informados.     Observar também que na pesquisa dos setores serão considerados apenas os produtos que estejam na Relação dos Setores. |  |
| Relação dos Setores | Alfanumérico | S | S |  | Neste campo é exibida a lista dos setores (SAFX2037) para seleção do usuário.  Critérios de Seleção dos Setores (SAFX2037): - Grupo da SAFX2037 = Grupo informado no campo “Grupo”. Observação: Um setor identificado pelo Grupo e Código pode ter vários registros na SAFX2037, com validades distintas. A relação dos Setores deve apresentar todos os registros de um setor, de todas as validades.  Do conjunto de setores recuperados, o sistema deve ainda aplicar o seguinte tratamento:  - APRESENTAR MARCADO o setor já parametrizado para o estabelecimento e grupo informados. - APRESENTAR DESMARCADO o setor que não está parametrizado para o estabelecimento e grupo informados.  Para selecionar os setores, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão exibidos para seleção: apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado;  do mesmo Grupo informado;  apenas estabelecimentos Centralizadores.  Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
