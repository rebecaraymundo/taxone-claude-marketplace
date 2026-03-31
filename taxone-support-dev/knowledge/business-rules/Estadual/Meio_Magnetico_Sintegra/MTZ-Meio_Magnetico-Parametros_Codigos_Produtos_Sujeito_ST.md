# MTZ-Meio_Magnetico-Parametros_Codigos_Produtos_Sujeito_ST

- **Fonte:** MTZ-Meio_Magnetico-Parametros_Codigos_Produtos_Sujeito_ST.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 86 KB

---

THOMSON REUTERS

Módulo Estadual – Meio Magnético

Parâmetros Códigos dos Produtos Sujeitos ao ICMS\-ST

__Localização__: Menu Estadual, Módulo: Meio Magnético, item Parâmetros 🡪 Minas Gerais  🡪 Estoque de Produtos ICMS\-ST \(88STEST e 88STITNF\) 🡪 Códigos dos Produtos Sujeitos ao ICMS\-ST

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS28851

Parametrização dos Códigos de Produto Sujeitos ao ICMS\-ST

Criação da parametrização de produtos para geração dos registros 88STITNF e 88STEST\.

19/08/2019

Sumário

[1\.	Introdução	2](#_Toc17213007)

[2\.	Layout da Tela	3](#_Toc17213008)

[3\.	Funcionamento da Tela	4](#_Toc17213009)

[4\.	Botões da barra de menu:	5](#_Toc17213010)

[5\.	Regras de Funcionamento dos Campos	6](#_Toc17213011)

[6\.	Validações	10](#_Toc17213012)

[1\.1	RN01: Campos Obrigatórios	10](#_Toc17213013)

[1\.2	RN02: Crítica de Faixas de Produtos Intercalados	11](#_Toc17213014)

# <a id="_Toc17213007"></a>Introdução

Esta tela tem objetivo disponibilizar a parametrização dos produtos sujeitos a ST para atendimento a geração dos registros 88STEST e 88STITNF de Minas Gerais\.

Inicialmente o módulo dispunha da parametrização por NCM para identificar os produtos sujeitos a ST para geração dos registros 88STEST e 88STITNF\.  Mas um cliente apresentou um cenário em que nem todos os produtos cadastrados para o mesmo NBM/NCM, eram regidos pelo regime de substituição tributária\.  Neste caso, a parametrização por NCM não atendia\.  Foi para atender este cenário que a parametrização por produto foi criada\. 

O cliente pode fazer uso das duas parametrizações simultaneamente, basta entender como utilizá\-las:

1. Utilizar a parametrização por NCM apenas quando todos produtos referentes a ele, forem regidos por substituição tributária\. 
2. Se apenas alguns produtos de um determinado NBM/NCM forem regidos por ICMS\-ST, utilizar a parametrização por produto\. Neste caso,  os códigos de produtos sujeitos ao ICMS\-ST podem ser parametrizados individualmente \(código a código\) ou por uma faixa definida pelos códigos inicial ao final\. 

# <a id="_Toc17213008"></a>Layout da Tela

Estabelecimento \[XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Grupo: \[XX\]

Indicador: \[ x \- xxxxxxxxxxxx  \\/ \]

Código Inicial: \[\.\.\.\] \[XXXX\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Código Final:   \[\.\.\.\] \[XXXX\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Informar Exclusões: \[ \] 

Produtos Excluídos da Faixa:

 \[ x \] xxxxxx\-xxxxxxxxxxxxxxx 

 \[ x \] xxxxxx\-xxxxxxxxxxxxxxx 

 \[   \]  xxxxxx\-xxxxxxxxxxxxxxx 

Replicar para os Estabelecimentos:

\[  \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[  \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[  \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[Selecionar Todos\] \[Desmarcar Todos\]

Os dados que definem a chave de identificação da parametrização são os seguintes:

- __Empresa__
- __Estabelecimento__
- __Grupo do Produto__
- __Indicador do Produto__
- __Código do Produto Inicial__
- __Código do Parâmetro __\(campo não apresentado em tela\)

A tabela onde a parametrização é gravada é  PRT\_PROD\_MSAF\. 

Os produtos excluídos da faixa são gravados na tabela PRT\_PROD\_EXC\_MSAF\. 

Essas tabelas são genéricas, ou seja, são utilizada para outras funcionalidades dentro do módulo Meio Magnético ou em outros módulos\.

A identificação dos registros relacionados a esta parametrização se dá através do Código do Parâmetro \(COD\_PARAM\) = 435\.

# <a id="_Funcionamento_da_Tela"></a><a id="_Toc17213009"></a>Funcionamento da Tela

__Fluxo Principal: Criação da Parametrização:__

__Passo__

__Acionador__

__Descrição__

1

Usuário

Usuário seleciona o item de menu Parâmetros 🡪 Minas Gerais  🡪 Estoque de Produtos ICMS\-ST \(88STEST e 88STITNF\) 🡪 Códigos dos Produtos Sujeitos ao ICMS\-ST

2

Sistema

Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos \(módulo Básicos>> Parâmetros, item Funcionais >> Relac\. Entre Tabelas e Grupos\) \(Relac\_Tab\_Grupo\)\.

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos cadastrados para o estabelecimento em questão, relacionados a Tabela Produto \(código da tabela = 2013\)\.

Senão

Sistema exibe todos os grupos cadastrados para todos os estabelecimentos da empresa de login, relacionados a Tabela Produto \(código da tabela = 2013\)\.

3

Usuário

Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo\. 

4

Sistema

Abre a tela de Parametrização dos Produtos, com os campos Estabelecimento e Grupo preenchidos e bloqueados\. Os demais campos são apresentados “em branco”\.

5

Usuário

Usuário seleciona um indicador do produto \(SAFX2013\) no campo “Indicador”\.

Vide regra do campo “Indicador” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

6

Usuário

Usuário digita ou seleciona via “pastinha” um código de produto \(SAFX2013\) no campo “Código Inicial”\.

7

Sistema

Valida código digitado\.

Vide regra do campo “Código Inicial” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

8

Usuário

Usuário digita ou seleciona via “pastinha” um código de produto \(SAFX2013\) no campo “Código Final”\.

9

Sistema

Valida código digitado\.

Vide regra do campo “Código Final” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

10

Sistema

Após a digitação do código Inicial e Final, o sistema habilita o campo “Informar Exclusões”\.

11

Usuário

Para definir os produtos a serem excluídos da faixa, executar fluxo alternativo: 

“Seleção dos Produtos excluídos da Faixa”\.

12

Usuário

Para definir os estabelecimentos para os quais a parametrização será replicada, executar fluxo alternativo: 

“Replicação para Estabelecimentos”\.

13

Usuário 

Seleciona botão confirma\.

14

Sistema

Executa validações descritas no tópico [5\- Validações](#_Validações)\. 

Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva com COD\_PARAM = 435\.

15

Usuário

Seleciona outras ações disponíveis na barra de menu da janela\.

Vide tópico “[4 \- Botões da barra de menu](#_Botões_da_barra)”

__Fluxo alternativo: Seleção dos Produtos excluídos da Faixa:__

Passo

Acionador

Descrição

1

Usuário

Seleciona o flag “Informar Exclusões”\.

2

Sistema

Disponibiliza a lista de produtos formada pelos códigos que estão compreendidos na faixa de produtos definidos pelo “Código Inicial” e “Código Final”\.

3

Usuário

Seleciona um ou mais produtos da lista de “Produtos Excluídos da Faixa”

4

Usuário

Volta ao passo 11 do fluxo principal\.

__Fluxo alternativo: Replicação para Estabelecimentos:__

Passo

Acionador

Descrição

1

Usuário

Seleciona o flag “Replicar para os Estabelecimentos”\.

2

Sistema

Disponibiliza a lista de estabelecimentos que atendam aos critérios:

\- Estabelecimentos pertencentes à empresa de login;

\- Estabelecimento diferente do selecionado na tela;

\- Apenas estabelecimentos associados ao grupo do selecionado em tela, para a Tabela Produto \(código da tabela = 2013\)\.  Vide Relacionamento entre Tabela e Grupos \(módulo Básicos>> Parâmetros, item Funcionais >> Relac\. Entre Tabelas e Grupos\)\.

3

Usuário

Volta ao passo 12 do fluxo principal\.

# <a id="_Botões_da_barra"></a><a id="_Toc17213010"></a>Botões da barra de menu:

SELECIONAR GRUPO

Ao clicar nesta opção será aberta a janela de seleção dos grupos de relacionamento \(relacionamento Tabela x Grupos\), e o usuário poderá selecionar o grupo desejado\.

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Produto\.

Senão

Sistema exibe todos os grupos cadastrados para todos os estabelecimentos da empresa de login, relacionados a Tabela Produto \(código da tabela = 2013\)\.

Seguir o *passo 4* do fluxo principal descrito no tópico [3 – Funcionamento da Tela](#_Funcionamento_da_Tela)\.

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas \(exceto os campos Estabelecimento e Grupo que mantém preenchidos e bloqueados\) e o usuário poderá incluir uma nova parametrização\.

Seguir o *passo 5* do fluxo principal descrito no tópico [3 – Funcionamento da Tela](#_Funcionamento_da_Tela)\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para o Estabelecimento e Grupo e cod\_param = 435\.

A tela deve apresentar os campos:

\- grupo 

\- Indicador

\- Código Inicial

\- Código Final 

\- cod\_param

EXCLUI

Esta opção permite a exclusão da parametrização identificada pelo estabelecimento, grupo, Indicador e Código Inicial e Final em questão, e Código do Parâmetro \(COD\_PARAM\) = 435\.

CONFIRMA

Opção para salvar as informações da parametrização incluída ou alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Regras_de_Funcionamento"></a><a id="_Toc17213011"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

__N__

Neste campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu\.* *

Grupo

Alfanumérico

__S__

__N__

Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu\.

Indicador

Alfanumérico

__S__

__S__

Este campo é uma lista dos indicadores de produto da SAFX2013:

1 \- Produto

2 \- Matéria Prima/Insumo

3 \- Embalagem

4 \- Material Uso/Consumo

5 \- Outros

6 \- Em Elaboração

7 \- Intermediário

8 \- Miscelâneas

Código Inicial

Alfanumérico

__S__

S

Formato:

Pastinha \+ Código \+ Descrição

Este campo corresponde ao Cadastro do Produto \(SAFX2013\) onde o usuário pode digitar ou selecionar via pastinha o código do produto\.

__Critérios de Seleção dos Produtos no Cadastro \(SAFX2013\):__

\- Grupo = Grupo informado \(campo “Grupo”\);

\- Indicador selecionado no campo “Indicador”

Caso os critérios acima recupere mais de um registro de mesmo produto, identificado pelo grupo, indicador e código, recuperar o registro de máxima validade\.

__Pastinha:__

Apresentar para seleção os produtos que atendam os critérios:

\- Grupo = Grupo informado \(campo “Grupo”\);

\- Indicador selecionado no campo “Indicador”

Caso o critério acima recupere mais de um registro de mesmo produto, identificado pelo grupo, indicador e código, recuperar o registro de máxima validade\.

__Consistência:__

- Quando o código for digitado, será verificada a existência do produto na tabela de produtos \(SAFX2013\), considerando o Grupo e o indicador informados\. Caso não exista, será exibida mensagem __*“Produto não Cadastrado”*__ no campo destinado a descrição do produto\.
- Após informar o Código Incial \(via pastinha ou digitado\), comparar com o Código Final, caso este esteja preenchido\.

O Código Inicial deve ser __<=__ ao Código Final\.  Caso não seja, exibir a seguinte mensagem:

__*“Código do produto inicial deve ser menor ou igual ao código do produto final”*__

- Ao salvar a parametrização, será validada a faixa de códigos de produto, impedindo que se intercale com alguma já existente\. Ver __[RN02](#_RN02:_Critica_de)__\.

__Tratamento:__

- Após informar o código inicial, caso o campo “Código Final” ainda não tenha sido informado, o campo do código final será inicializado com o mesmo conteúdo do produto inicial\.

Código Final

Alfanumérico

__S__

S

Formato:

Pastinha \+ Código \+ Descrição

Este campo corresponde ao Cadastro do Produto \(SAFX2013\) onde o usuário pode digitar ou selecionar via pastinha o código do produto\.

Este campo será inicializado com o mesmo código de produto informado no campo “Código Inicial”, mas o usuário poderá alterar este conteúdo através da janela de seleção da SAFX2013 ou de digitação, assim como é feito no campo do código inicial\.

__Critérios de Seleção dos Produtos no Cadastro \(SAFX2013\):__

\- Grupo = Grupo informado \(campo “Grupo”\);

\- Indicador selecionado no campo “Indicador”

Caso os critérios acima recupere mais de um registro de mesmo produto, identificado pelo grupo, indicador e código, recuperar o registro de máxima validade\.

__Pastinha:__

Apresentar para seleção os produtos que atendam os critérios:

\- Grupo = Grupo informado \(campo “Grupo”\);

\- Indicador selecionado no campo “Indicador”

Caso o critério acima recupere mais de um registro de mesmo produto, identificado pelo grupo, indicador e código, recuperar o registro de máxima validade\.

__Consistência:__

- Quando o código for digitado, será verificada a existência do produto na tabela de produtos \(SAFX2013\), considerando o Grupo e o indicador informados\. Caso não exista, será exibida mensagem__* “Produto não Cadastrado”*__ no campo destinado a descrição do produto\.
- Após informar o Código Final \(via pastinha ou digitado\), comparar com o código Inicial, caso este esteja preenchido\.

O Código Final deve ser __>=__ ao código Inicial\.  Caso não seja, exibir a seguinte mensagem:

__*“Código do produto final deve ser maior ou igual ao código do produto inicial”*__

- Ao salvar a parametrização, será validada a faixa de códigos de produto, impedindo que se intercale com alguma já existente\. Ver __[RN02](#_RN02:_Critica_de)__\.

Informar Exclusões

Alfanumérico

N

S

Através deste parâmetro o usuário poderá selecionar alguns produtos da faixa escolhida para desconsiderar da parametrização\. 

Ao clicar nesta opção, todos os produtos da faixa informada \(código inicial ao final\) serão exibidos no quadro “*Produtos Excluídos da Faixa*”\.

Ao desmarcar a opção, todo o conteúdo do quadro “*Produtos Excluídos da Faixa*” será apagado\.

Produtos Excluídos da Faixa: 

Radio Button

N

S

Neste quadro serão demonstrados todos os produtos da faixa informada \(código inicial ao final\), e o usuário poderá selecionar os produtos que desejar para que sejam desconsiderados da parametrização\. 

O conteúdo deste quadro será automaticamente apagado sempre que o usuário desmarcar a opção “*Informar Exclusões*”\.

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado e do mesmo Grupo informado\.

Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

# <a id="_Validações"></a><a id="_Toc517344573"></a>

# <a id="_Toc17213012"></a>Validações

__Críticas a serem realizadas antes de salvar a operação:__

## <a id="_Toc17213013"></a>__RN01: Campos Obrigatórios__

Validações de Campos Obrigatórios não preenchidos\.

Quando o campo é obrigatório e não estiver preenchido, exibir mensagem padrão\.

A obrigatoriedade dos campos está definida no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

## <a id="_RN02:_Critica_de"></a><a id="_Toc17213014"></a>RN02: Crítica de Faixas de Produtos Intercalados 

Ao salvar uma parametrização que está sendo incluída ou alterada, o sistema deve verificar se já existe outro registro na parametrização que contenha o produto informado, __ou__ a faixa de produtos, quando for o caso \(ou seja, se haverá faixas de produtos intercalados\)\.

Quando ocorrer este tipo de problema, a operação não será salva, e será exibida a mensagem abaixo:

*                   “Código Inicial e/ou Final já contido em outra faixa de produtos”*

Para fazer esta validação, o sistema deve buscar as parametrizações já gravadas com os seguintes critérios:

- Empresa de login
- Estabelecimento informado na tela
- Grupo informado na tela
- Indicador de Produto informado na tela
- Código do Parâmetro = 435

Para as parametrizações recuperadas, fazer as seguintes consistências:

1. Para Código Inicial do registro a ser salvo __<__ Código Inicial da parametrização recuperada:

Se Código Final do registro a ser salvo for >= Código Inicial da parametrização recuperada, então:

	Faixas de Produtos se intercalaram, dar mensagem de erro e não salvar registro\.

1. Para Código Inicial do registro a ser salvo__ =__ Código Inicial da parametrização recuperada:

	Faixas de Produtos se intercalaram, dar mensagem de erro e não salvar registro\.

1. Para Código Inicial do registro a ser salvo __>__ Código Inicial da parametrização recuperada:

Se Código Final da parametrização recuperada >= Código Inicial do registro a ser salvo for, então:

		Faixas de Produtos se intercalaram, dar mensagem de erro e não salvar registro\.

	

Exemplo I:

Registro 1 🡪  Código inicial = 1000500  Código final = 1000599

Registro 2 🡪  Código inicial = 1000600  Código final = 1000699

Registro a ser incluído 🡪  Código inicial = 1000540  Código final = 1000545

Neste exemplo, teríamos um erro na parametrização, pois a faixa do registro a ser importado já se encontra contida na faixa do registro 1\.

 

Exemplo II:

Registro 1 🡪  Código inicial = 1000500  Código final = 1000599

Registro 2 🡪  Código inicial = 1000600  Código final = 1000900

Registro a ser incluído 🡪  Código inicial = 1000000  Código final = 1000800

Neste exemplo, também teríamos erro na parametrização, pois a faixa do registro a ser importado engloba  toda faixa do registro 1, e além disso, se intercala com a faixa do registro 2\.

       = = = = = =

