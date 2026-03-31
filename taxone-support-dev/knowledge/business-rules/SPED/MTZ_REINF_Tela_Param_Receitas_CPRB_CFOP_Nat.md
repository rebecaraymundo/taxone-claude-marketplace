# MTZ_REINF_Tela_Param_Receitas_CPRB_CFOP_Nat

> Fonte: MTZ_REINF_Tela_Param_Receitas_CPRB_CFOP_Nat.docx






THOMSON REUTERS

Parametrização dos Identificadores de Receita por CFOP/Natureza de Operação p/ Cálculo da CPRB

EFD – REINF

Localização: Parâmetros  CPRB  Apuração da CPRB  Identificador das Receitas (por CFOP/Natureza de Operação)

Produto: Mastersaf-DW



Sumário

1.	CONTROLE DE ALTERAÇÕES	3
2.	INTRODUÇÃO	4
3.	DOCUMENTOS DE REFERÊNCIA	4
4.	DEFINIÇÃO DAS REGRAS	4
4.1.	Tela de Pesquisa e de Resultados	5
4.2.	Botões da Toolbar	5
4.3.	Layout e Campos – Tela Principal	6


## CONTROLE DE ALTERAÇÕES






## INTRODUÇÃO


O objetivo desta tela é identificar as receitas para o cálculo da CPRB através de parametrização por CFOP e Naturezas de Operação.

Esta parametrização é utilizada no cálculo da CPRB para filtro dos documentos fiscais que compõem as receitas a serem demonstradas.

Esta parametrização utiliza a tabela padrão de parametrização de Natureza de Operação:


## DOCUMENTOS DE REFERÊNCIA

(Não se aplica)

## DEFINIÇÃO DAS REGRAS


Esta é uma tela padrão de parametrização por CFOP e Natureza de Operação para filtro de notas fiscais.

Por se tratar de Natureza de Operação, a tela trabalha com a informação do GRUPO da tabela de relacionamento Tabelas x Grupos (RELAC_TAB_GRUPO).

Na abertura da tela, a janela de seleção do GRUPO será aberta automaticamente, obrigando o usuário a selecionar o Grupo desejado. Os critérios para exibição dos Grupos para seleção do usuário estão descritos no item 4.2.

Campos chave da parametrização:

Empresa (código da empresa do login)
Estabelecimento
Código do Parâmetro (código interno controlado pelo sistema para cada parametrização existente)
CFOP
Grupo Natureza
Natureza de Operação

#### Tela de Pesquisa e de Resultados


(Não se aplica)

#### Botões da Toolbar


Botões da barra de menu:




#### Layout e Campos – Tela Principal





Funcionamento dos campos:





| Data | Demanda | Descrição | Autor |
| --- | --- | --- | --- |
| 14/05/2019 | MFS23185 | Criação da Tela | Vânia Dias Mattos |


| Tabela: | PRT_EXTCFO_MSAF |  |
| --- | --- | --- |
| Código do Parâmetro: | 660 - CFOPs para cálculo de CPRB | (código de parâmetro na PRT_PAR2_MSAF) |


| Botão | Tratamentos | Demanda |
| --- | --- | --- |
| Seleciona Grupo | Ao clicar nesta opção será aberta a janela de seleção dos grupos de relacionamento (relacionamento Tabela x Grupos), e o usuário poderá selecionar o grupo desejado.  Caso o usuário tenha informado um estabelecimento no login, serão disponibilizados apenas os grupos relacionados ao estabelecimento em questão, caso contrário, serão exibidos os grupos de todos os estabelecimentos da empresa. | MFS23185 |
| Confirma | Opção para salvar os dados da parametrização incluída / alterada. | MFS23185 |
| Relatório | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. | MFS23185 |
| Fecha | Ao clicar nesta opção a tela será fechada. | MFS23185 |


| Campo | Regra | Demanda |
| --- | --- | --- |
| Estabelecimento | Tipo do campo: Listbox  Caso o usuário tenha informado um estabelecimento no login, o campo exibirá o estabelecimento fixo, não permitindo a seleção do usuário.  Caso contrário, o campo mostrará a lista de estabelecimentos para seleção do usuário, considerando apenas os que atendam às seguintes condições:  - Estabelecimentos da empresa do login; - Estabelecimentos cadastrados no menu “Parâmetros  Dados Iniciais”; |  |
| Grupo Natureza | Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu.  O campo não é habilitado para edição. |  |
| Informar Código/Descrição de Pesquisa | Tipo do campo: Texto   Neste campo o usuário poderá digitar o código ou a descrição do CFOP a ser pesquisado. O conteúdo da informação digitada é identificado pelos campos “Código” e “Descrição” descritos a seguir (dependendo da opção que estiver marcada).  Após digitar a informação, o usuário poderá clicar no botão <Pesquisar> para realizar a pesquisa. |  |
| Código | Tipo do campo: Radio Button Default: Marcado  Os campos “Código” e “Descrição” são alternativos, e desta forma, somente um deles pode ficar marcado. |  |
| Descrição | Tipo do campo: Radio Button Default: Desmarcado  Os campos “Código” e “Descrição” são alternativos, e desta forma, somente um deles pode ficar marcado. |  |
| Pesquisar | Tipo do campo: Botão  Ao clicar neste botão, caso exista informação no campo “Informar Código/Descrição de Pesquisa”, será efetuada a pesquisa na tabela das naturezas de operação (SAFX2081). Todos os registros da tabela que atendam às condições abaixo, serão exibidos no quadro “CFOP/Natureza de Operação”.  - Se campo “Código” marcado, o código do CFOP deve ser igual ao código informado; - Se campo “Descrição” marcado, a descrição do CFOP deve ser igual à descrição informada; - O CFOP deve ser uma operação de saída (CFOP’s iniciados por “5”, “6” ou “7”); - A natureza de operação deve ser do GRUPO escolhido pelo usuário     Se o usuário clicar no botão “Pesquisar”, e não existir informação no campo “Informar Código/Descrição de Pesquisa”, o quadro permanece inalterado.  Se ao efetuar a pesquisa conforme os critérios acima, não retornar nenhum resultado, o quadro ficará limpo (sem informação). Nesse caso, para voltar a exibir as informações, o usuário deverá limpar o campo “Informar Código/Descrição de Pesquisa” e clicar novamente no botão “Pesquisar”. |  |
| CFOP/Natureza de Operação | Neste campo é exibida a lista da combinação CFOP + Natureza de Operação da tabela SAFX2081, para seleção do usuário.  Os critérios para filtro dos dados da SAFX2081 são:  CFOP – Apenas as operações de saída (CFOP’s iniciados por “5”, “6” ou “7”); Natureza de Operação – Apenas as Naturezas do GRUPO escolhido pelo usuário;  Todos os CFOP’s/Naturezas já parametrizados anteriormente, aparecerão selecionados.   Como facilitador, poderão ser utilizados os botões <Selecionar Todos> e <Desmarcar Todos> descritos a seguir. |  |
| Selecionar Todos | Tipo do campo: Botão  Ao clicar neste botão, todos os CFOP’s/Naturezas  do quadro serão marcados simultaneamente. |  |
| Desmarcar Todos | Tipo do campo: Botão  Ao clicar neste botão, todos os CFOP’s/Naturezas  do quadro serão desmarcados simultaneamente |  |
| Replicar para os Estabelecimentos | Tipo do campo: Checkbox  Default: Desmarcado  Esta opção permite que ao salvar a operação (botão “Confirma” da barra de menu), a parametrização salva seja replicada para todos os estabelecimentos selecionados.  Ao clicar nesta opção, será exibido no quadro abaixo a lista de estabelecimentos para os quais a parametrização será replicada. Serão exibidos apenas os estabelecimentos que atendam às seguintes condições:  - Estabelecimentos da empresa do login; - Estabelecimentos cadastrados no menu “Parâmetros  Dados Iniciais”; - Estabelecimento diferente do exibido no campo “Estabelecimento”;  Quando esta opção for desmarcada, o quadro dos estabelecimentos será limpo.  Como facilitador, poderão ser utilizados os botões <Selecionar Todos> e <Desmarcar Todos> descritos a seguir. |  |
| Selecionar Todos | Tipo do campo: Botão  Ao clicar neste botão, todos os estabelecimentos do quadro serão marcados simultaneamente. |  |
| Desmarcar Todos | Tipo do campo: Botão  Ao clicar neste botão, todos os estabelecimentos do quadro serão desmarcados simultaneamente. |  |
