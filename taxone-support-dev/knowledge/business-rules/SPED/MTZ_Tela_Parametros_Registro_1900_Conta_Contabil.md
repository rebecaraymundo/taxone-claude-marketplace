# MTZ_Tela_Parâmetros_Registro 1900_Conta_Contabil

> Fonte: MTZ_Tela_Parâmetros_Registro 1900_Conta_Contabil.docx




THOMSON REUTERS

Módulo EFD Contribuições – Parametrização das Contas Contábeis

Localização: Menu SPED,  Módulo: Escrituração Fiscal Digital das Contribuições, item Parâmetros  Registro 1900  Conta Contábil

DOCUMENTO DE REQUISITO










REGRAS DE NEGÓCIO



Manutenção criada na MFS10591 para a parametrização das contas contábeis (SAFX2002) a serem consideradas na geração do registro 1900 do EFD Contribuições.

Opções da barra de menu:

SELECIONAR GRUPO – Ao clicar nesta opção, abrirá uma janela de seleção dos grupos de relacionamento das tabelas do Mastersaf, e o usuário deverá selecionar o grupo e estabelecimento. Na abertura da tela esta janela será exibida automaticamente, obrigando o usuário a selecionar o Grupo e Estabelecimento. O grupo e estabelecimento selecionados serão exibidos nos campos “Estabelecimento” e “Grupo Conta”.

Caso tenha sido informado um estabelecimento no login, serão disponibilizados apenas os grupos aos quais o estabelecimento esteja associado. Caso contrário, serão disponibilizados todos os grupos e estabelecimentos da Empresa do login.

CONFIRMA – Salva os dados incluídos ou alterados;

RELATÓRIO – Para emitir o relatório o usuário poderá selecionar um estabelecimento (e também uma categoria específica, se desejar), e serão listados todos os dados parametrizados para os critérios selecionados;

FECHA – Fecha a janela da parametrização;




Neste campo será exibido o estabelecimento selecionado na janela de seleção do Grupo.


Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Selecionar Grupo” da barra de menu.



Este campo apresenta duas opções:
(  ) Pelas inicias do código
(  ) Pelas iniciais da descrição

Default: opção “Pelas iniciais do código”


Utilização dos campos “Pesquisar contas” e “Conteúdo para pesquisa” como facilitadores da pesquisa das contas:

Os campos “Pesquisar contas” e “Conteúdo para pesquisa” são um facilitador para a pesquisa das contas a serem demonstradas no campo “Contas”.

Não existe a obrigatoriedade de sua utilização, pois a princípio o campo “Contas” já exibe todas as contas do Grupo selecionado, conforme consta na RN06.

Apenas quando o usuário escolher uma das formas de pesquisa (código ou descrição), informar o conteúdo no campo “Conteúdo para pesquisa”, e clicar no botão “Pesquisar”, é que a lista das contas do campo “Contas” será regerada com as contas selecionadas de acordo com a pesquisa realizada (ver RN04 e RN05).



Este é um campo alfanumérico no qual o usuário poderá informar uma quantidade variável de caracteres a serem utilizados como as iniciais a serem pesquisadas no código, ou na descrição da conta, dependendo da opção informada no campo “Pesquisar contas”.

O conteúdo informado permitirá filtrar as contas por um código ou descrição específica, como também, pelas iniciais do código ou da descrição.

Utilização dos campos “Pesquisar contas” e “Conteúdo para pesquisa” como facilitadores da pesquisa das contas:

(ver RN03 e RN05)



Sempre que o usuário clicar no botão “PESQUISAR”, a lista das contas exibidas no campo “Contas” será regerada.

O procedimento quando o usuário clicar neste botão será o seguinte:






Assim que o Grupo e a Categoria forem selecionados pelo usuário, no campo “Contas” será exibida a lista das contas do Plano de Contas (SAFX2002) para que o usuário selecione aos contas a serem associados à categoria informada no campo “Categoria”.

Serão disponibilizadas para seleção apenas as contas do grupo selecionado (campo “Grupo Operação”).

As contas aparecerão ordenadas pelo código.

Quando no cadastro da SAFX2002 existir o mesmo código de conta em linhas repetidas, com datas de validade diferentes, será exibido na lista apenas uma ocorrência do código (que será o de maior data de validade).

Reformulação da lista das contas através do botão “PESQUISAR”:

Sempre que o usuário clicar no botão “PESQUISAR”, a lista das contas será regerada, considerando os critérios para pesquisa informados nos campos “Pesquisar contas” e “Conteúdo para pesquisa”  (ver detalhes na RN05).



Este campo aparecerá desmarcado por default, e quando selecionado, os dados parametrizados serão replicados para os estabelecimentos selecionados pelo usuário no quadro dos Estabelecimentos.

= = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS10591 | Andréa Rocha | Criação da parametrização por conta contábil | 23/08/2017 |
|  |  |  |  |


| RN00 | Regras Gerais |
| --- | --- |


| RN01 | Estabelecimento |
| --- | --- |


| RN02 | Grupo Conta |
| --- | --- |


| RN03 | Pesquisar contas |
| --- | --- |


| RN04 | Conteúdo para pesquisa |
| --- | --- |


| RN05 | Opção “Pesquisar” |
| --- | --- |


| Se o campo “Conteúdo para pesquisa” estiver vazio:        Neste caso, a lista das contas será refeita considerando a regra geral descrita na RN06);  Senão       Se campo “Pesquisar contas” = “Pelas inicias do código”             Neste caso, a lista das contas será refeita considerando os critérios definidos na regra geral (RN06), e também, considerando            apenas as contas cujo código apresenta as iniciais iguais ao conteúdo informado no campo ““Conteúdo para pesquisa”;       Senão    (opção “Pelas iniciais da descrição”)              Neste caso, a lista das contas será refeita considerando os critérios definidos na regra geral (RN06), e também, considerando             apenas as contas cuja descrição apresenta as iniciais iguais ao conteúdo informado no campo ““Conteúdo para pesquisa”; |
| --- |


| RN06 | Contas |
| --- | --- |


| RN07 | Replicar para os Estabelecimentos |
| --- | --- |
