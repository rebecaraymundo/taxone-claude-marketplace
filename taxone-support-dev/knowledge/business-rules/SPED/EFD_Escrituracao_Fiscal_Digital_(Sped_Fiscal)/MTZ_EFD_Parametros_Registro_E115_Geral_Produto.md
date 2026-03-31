# MTZ_EFD_Parametros_Registro_E115_Geral_Produto

- **Fonte:** MTZ_EFD_Parametros_Registro_E115_Geral_Produto.docx
- **Modificado:** 2021-01-26
- **Tamanho:** 88 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros p/ Pré\-Geração do Registro E115 por Produto \(Geral\)

__Localização__: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Geral\) 🡪 Produtos

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS24916__

Pré\-Geração do E115 \(Geral\)

Criação da parametrização de produtos para a pré\-geração do registro E115\. 

27/02/2019

__MFS30407__

Andréa Rocha

Retirar a validação do campo estabelecimento para o estado igual a RS\.

26/09/2019

__MFS32389__

Vânia Mattos

Alteração da X272\_PAR\_PROD\_E115 para inclusão do COD\_INF\_ADIC na PK\. Este alteração permitirá que o mesmo produto seja parametrizado para diferentes COD\_INF\_ADIC\.

25/08/2020

Sumário

[1\.	Introdução	2](#_Toc2189877)

[2\.	Layout da Tela	2](#_Toc2189878)

[3\.	Funcionamento da Tela	3](#_Toc2189879)

[4\.	Botões da barra de menu:	5](#_Toc2189880)

[5\.	Regras de Funcionamento dos Campos	5](#_Toc2189881)

[6\.	Validações	8](#_Toc2189882)

# <a id="_Toc2189877"></a>Introdução

Esta tela tem objetivo de promover a manutenção da parametrização dos produtos a serem utilizados na rotina de pré\-geração do registro E115, realizada no menu “Pré\-Geração 🡪 Registro E115 \(Geral\)” do módulo Sped Fiscal\.

Esta parametrização também pode ser carregada via importação da SAFX272\.

Esta parametrização relaciona os produtos \(SAFX2013\) aos Códigos de Informação Adicional, criados no item “Parâmetro 🡪 Registros E115/1925🡪 Informações Adicionais da Apuração \(Registros E115/1925\)”\. Essa relação é feita por estabelecimento atribuindo\-se datas inicial e final de vigência\.

Os dados que definem a chave de identificação da parametrização são os seguintes:

__MFS32389:__ A chave da tabela foi alterada para permitir que o mesmo produto, seja parametrizado para diferentes COD\_INF\_ADIC\.

*\(Esta tabela é específica da pré\-geração do E115 da opção “Geral”, assim, não terá impacto em nenhuma outra geração\)*

- __Empresa__
- __Estabelecimento__
- __Grupo do Produto__
- __Indicador do Produto__
- __Código do Produto__
- __Data inicial da validade__
- __Código da Informação Adicional__

A tabela onde a parametrização é gravada é X272\_PAR\_PROD\_E115\.

# <a id="_Toc2189878"></a>Layout da Tela

Estabelecimento \[XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Grupo: \[XX\]

Código: \[\.\.\.\] \[XXXX\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Início Validade: \[dd/mm/aaaa\]

Informar Código/Descrição para Pesquisa                         \[                                            \] \( \)Código    \( \)Descrição

\-\- Relação de Produtos\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

         Ind\-Código\-Descrição                                |    Fim Validade       |  Descr Complementar                                                          

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\[ x \] x \-xxxxxx\-xxxxxxxxxxxxxxx  | \[dd/mm/aaaa\]  | \[xxxxxxxxxxxxxxxxxxx\]                   

\[ x \] x \-xxxxxx\-xxxxxxxxxxxxxxx  | \[dd/mm/aaaa\]  | \[xxxxxxxxxxxxxxxxxxx\]  

\[   \] x \-xxxxxx\-xxxxxxxxxxxxxxx   | \[dd/mm/aaaa \] | \[xxxxxxxxxxxxxxxxxxx\]  

\[Selecionar Todos\] \[Desmarcar Todos\]

# <a id="_Funcionamento_da_Tela"></a><a id="_Toc2189879"></a>Funcionamento da Tela

__Passo__

__Acionador__

__Descrição__

1

Usuário

Usuário seleciona o item de menu Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Geral\) 🡪 Produtos

2

Sistema

Verifica o usuário informou estabelecimento no login do Manager\.

Se no login foi informado estabelecimento, então:

Sistema verifica a UF do Estabelecimento\.

Se a UF do Estabelecimento de login for igual a __RS__, então:

Sistema apresenta mensagem: 

“*A parametrização de Produto para Informações Adicionas E115 não é válida para estabelecimentos do Rio Grande do Sul”*

Fecha a janela\.

Finaliza o fluxo\.

Senão

Segue o fluxo\.

Senão

Segue o fluxo\.

3

Sistema

Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos \(Relac\_Tab\_Grupo\)\.

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Produto\.

Senão

Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Produto\.

4

Usuário

Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo\. 

5

Sistema

Abre a tela de Parametrização dos Produtos, com os campos Estabelecimento e Grupo preenchidos e bloqueados\.

Os campos Código, Início Validade e a Relação dos Produtos são apresentados “em branco”\.

6

Usuário

Usuário seleciona ou digita um Código de Informação Adicional no campo “Código”\.

7

Sistema

Valida o Código digitado\.

Vide regra do campo “Código” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

8

Usuário

Digita uma data no campo Início Validade\.

8\.1

Sistema

Valida a data digitada\.

Vide regra do campo “Início Validade” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

9

Sistema

Recupera os produtos do Cadastro de Produtos \(SAFX2013\), considerando o grupo e a data Início Validade informados\.

Vide regra do campo “Relação de Produtos” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

10

Usuário

Seleciona um produto podendo preencher os campos Fim de Validade e Descrição Complementar\.

11

Sistema

Caso o usuário preencha o campo Fim de Validade, o sistema valida data digitada\.

Vide regra do campo “Fim Validade” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

12

Usuário 

Seleciona botão confirma\.

13

Sistema

Executa validações descritas no tópico [5\- Validações](#_Validações)\. 

Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva\.

14

Usuário

Seleciona outras ações disponíveis na barra de menu da janela\.

Vide tópico “[4 \- Botões da barra de menu](#_Botões_da_barra)”

# <a id="_Botões_da_barra"></a><a id="_Toc2189880"></a>Botões da barra de menu:

SELECIONAR GRUPO

Ao clicar nesta opção será aberta a janela de seleção dos grupos de relacionamento \(relacionamento Tabela x Grupos\), e o usuário poderá selecionar o grupo desejado\.

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Produto\.

Senão

Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Produto\. 

Seguir o *passo 4* do fluxo descrito no tópico [3 – Funcionamento da Tela](#_Funcionamento_da_Tela)\.

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas \(exceto os campos Estabelecimento e Grupo que mantém preenchidos e bloqueados\) e o usuário poderá incluir uma nova parametrização\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção\. 	

A tela deve apresentar os campos Início Validade e Código\. 

E recuperar de forma unívoca as parametrizações de mesmo Início Validade e Código, para que o resultado não apresente linhas repetidas na tela\.

EXCLUI

Esta opção permite a exclusão das parametrizações do estabelecimento, grupo, Data Início Validade e Código em questão\. 

CONFIRMA

Opção para salvar as informações da parametrização incluída ou alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Regras_de_Funcionamento"></a><a id="_Toc2189881"></a>Regras de Funcionamento dos Campos

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

Código 

Alfanumérico

__S__

S

Formato:

Pesquisar Pasta – Seleção da Manutenção Informações Adicionais da Apuração \(Registro E115/ 1925\)

Permitir seleção da tabela dos Códigos de Informação Adicional parametrizados na Manutenção Informações Adicionais da Apuração \(Registro E115/ 1925\), item de menu Parâmetro 🡪 Registros E115/1925🡪 Informações Adicionais da Apuração \(Registros E115/1925\)\.

__Pastinha:__

- Só recuperar os códigos cuja UF seja igual a UF do Estabelecimento;

__Consistência:__

- Verificar se o código digitado existe na tabela de Informações Adicionais da Apuração \(Registro E115/ 1925\), considerando a UF do Estabelecimento\. Caso não exista, exibir a seguinte mensagem:

*Código da Informação Adicional não cadastrado para a UF do Estabelecimento\.*

__Tratamento:__

- Ao selecionar um novo Código, os Produtos e os campos Fim Validade e Descrição Complementar devem ser atualizados\.

__Tabela Origem:__

EFD\_INF\_ADIC\_APUR

Início Validade

Data

__S__

S

  \(dd/mm/aaaa\)

O usuário deverá informar uma data inicial de validade da parametrização\.

A data de validade inicial é obrigatória, já a data final pode ficar sem preenchimento\. 

__Consistência Validade x Grupo:__

A data de validade inicial *não* pode ser inferior à data de validade do Grupo informado \(campo “Grupo”\)\. Caso isso ocorra, será exibida a seguinte mensagem:

*“A data Início Validade não pode ser inferior à validade do Grupo informado”*

 

__Tratamento:__

- Ao digitar uma nova data, os Produtos e os campos Fim Validade e Descrição Complementar devem ser atualizados\.

Informar código/descrição para pesquisa

Alfanumérico

N

S

Neste campo o usuário poderá informar os caracteres iniciais do código, ou da descrição do Produto a serem pesquisados, através do botão “Pesquisar”\.

\- Código 

\- Descrição

Radio Button

N

S

Opção default:     “Código”

Estas duas opções indicam a forma como será feita a pesquisa dos produtos a serem disponibilizados para seleção do usuário no campo “Relação dos Produtos”\.

As opções são alternativas, pois o filtro dos produtos é feito pelo código, ou pela descrição do produto\.

Pesquisar

Botão

N

S

Ao clicar nesta opção, será feita a pesquisa dos produtos, de acordo com o código ou a descrição informada, e a lista dos produtos será refeita e demonstrada para a seleção do usuário\.

Esta pesquisa considera os produtos cujo código ou descrição, conforme o caso, tenha as mesmas iniciais do código ou da descrição informados\.

   

Observar também que na pesquisa dos produtos serão considerados apenas os produtos que estejam na Relação dos Produtos\.  

Relação dos Produtos

Alfanumérico

__S__

S

Neste campo é exibida a lista dos produtos \(SAFX2013\) para seleção do usuário\.

__Critérios de Seleção dos Produtos no Cadastro \(SAFX2013\):__

\- Grupo = Grupo informado \(campo “Grupo”\);

\- Data Validade <= data informada no campo “Início Validade”\.

Caso o critério acima recupere mais de um registro de um mesmo produto, identificado pelo grupo, indicador e código, recuperar apenas o de máxima validade\.

Do conjunto de produtos recuperados, o sistema deve ainda aplicar o seguinte tratamento:

 \- APRESENTAR MARCADO o produto já parametrizado para o estabelecimento e data “Inicio Validade” informados e de mesmo Código de Informação Adicional informado\.

\- APRESENTAR DESMARCADO o produto que não está parametrizado para o estabelecimento, data “Inicio Validade” e Código de Informação Adicional informados\.

\- NÃO APRESENTAR o produto já parametrizado para o estabelecimento e data “Inicio Validade” informados e com outro Código de Informação Adicional\.

__MFS32389:__ A chave da tabela foi alterada para permitir que o mesmo produto, seja parametrizado para diferentes COD\_INF\_ADIC\.

Para selecionar os produtos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

Fim Validade

Data

N

S

  \(dd/mm/aaaa\)

O usuário poderá informar uma data fim de validade\.

__Consistência Inicio Validade x Fim Validade:__

Caso a data de validade final seja informada, *não* pode ser inferior à data de validade inicial\. Caso isso ocorra, será exibida a seguinte mensagem:

*“A data Fim Validade deve ser maior ou igual à data Início Validade”*

 

Descrição Complementar

Alfanumérico

N

S

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado, do mesmo Grupo informado, e da mesma UF do Estabelecimento informado\.

Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

# <a id="_Validações"></a><a id="_Toc517344573"></a>

# <a id="_Toc2189882"></a>Validações

__Críticas a serem realizadas antes de salvar a operação:__

- __RN01: Campos Obrigatórios__

Validações de Campos Obrigatórios não preenchidos\.

Quando o campo é obrigatório e não estiver preenchido, exibir mensagem padrão\.

A obrigatoriedade dos campos está definida no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

- __RN02: Ocorrência do mesmo produto em mais de uma parametrização do Estabelecimento e Cód\. Inf\. Adicional __

Nesta regra será feito um tratamento para não permitir intervalos intercalados de datas na parametrização de um determinado produto para a Empresa, Estabelecimento e __Cód\. Inf\. Adicional__\.

Vamos adotar tratamentos para evitar que um produto para uma determinada empresa, estabelecimento e código de informação adicional tenha parametrizações com intervalos de datas inicial e final que se intercalem\. Ou seja, não podemos permitir que uma parametrização do produto tenha Data Início ou Fim de Validade entre as datas Início e Fim Validade da parametrização já existente na base\.

Um produto poderá constar em outra parametrização da mesma empresa/estabelecimento/cód\.inf\.adicional, desde que a os intervalos determinados pelas datas Início e Fim de Validade das mesmas, não se intercalem\.

\-\-\-\-\-\-\-\-\-\-\-|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

             Dt ini                       Dt Fim     

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

                     Dt ini                       Dt Fim

__Exemplo 1:__

Estabelecimento ‘001’

Código: PR840007

Início Validade 01/01/2018 \- Produto 1\-A00 \- Fim Validade nulo\.

Novas parametrizações para o Estabelecimento ‘001’, Código: PR840007 e Produto 1\-A00:

__Início Validade__

__Fim Validade__

__Resultado __

01/01/2017

31/12/2017

SUCESSO\. Parametrização válida\.

01/01/2017

01/01/2018

ERRO

Parametrização inválida\. A Data Fim \(01/01/2018\) intercala com a Início Validade da parametrização já existente\.

01/01/2017

ERRO\. 

Parametrização inválida\. A Data Fim \(nula\), intercala com a Início Validade da parametrização já existente\.

02/01/2018

ERRO\.

Parametrização inválida\. A Data Fim nula da parametrização já existente intercala com a data Início Validade\.

__Exemplo 2:__

Estabelecimento ‘001’

Código: PR840007

Início Validade 01/01/2018 \- Produto 1\-A00 \- Fim Validade 31/01/2018\.

Novas parametrizações para o Estabelecimento ‘001’, Código: PR840007 e Produto 1\-A00:

__Início Validade__

__Fim Validade__

__Resultado __

01/01/2017

31/12/2017

SUCESSO\. Parametrização válida\.

02/01/2018

ERRO\. Parametrização inválida\. Data Início intercala com a Início e Fim de Validade da parametrização já existente\.

01/02/2018

SUCESSO\. Parametrização válida\.

__Situações a serem tratadas__:

1. Dada a Empresa, Estabelecimento, Cód\.Inf\.Adic\. e Produto da parametrização que está sendo incluída/alterada, buscar na base a parametrização de mesma Empresa, Estabelecimento, Cód\.Inf\.Adic\. e Produto com Data Início Validade imediatamente posterior à Data Início Validade do registro que está sendo parametrizado\.

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro que está sendo incluído/alterado com a Data Início Validade do registro encontrado\.

Se Data Fim de Validade do registro que está sendo incluído/alterado >= Data Início Validade do registro encontrado ou

     Data Fim de Validade do registro que está sendo incluído/alterado for nula então:

O registro não será gravado e a seguinte mensagem será exibida:

*Já existem parametrizações para Produtos vigentes nas datas Início e/ou Fim de Validade informadas\.*

1. Dada a Empresa, Estabelecimento, Cód\.Inf\.Adic\. e Produto da parametrização que está sendo incluída, buscar na base a parametrização de mesma Empresa, Estabelecimento, Cód\.Inf\.Adic\. e Produto com Data Início Validade imediatamente anterior à Data Início Validade do registro que está sendo parametrizado\.

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro encontrado com a Data Início Validade do registro que está sendo incluído\.

Se Data Fim de Validade do registro encontrado >= Data Início Validade do registro que está sendo incluído ou

     Data Fim de Validade do registro encontrado for nula então:

O registro não será gravado e a seguinte mensagem será exibida:

*Já existem parametrizações para Produtos vigentes nas datas Início e/ou Fim de Validade informadas\.*

Considerando a chave da tabela \(empresa, estabelecimento, Cód\.Inf\.Adic\., produto e Início Validade\), uma inclusão tratar as situações __\(a\)__ e __\(b\)__\. Na atualização do registro basta tratar a situação __\(a\)__\.

       = = = = = =

