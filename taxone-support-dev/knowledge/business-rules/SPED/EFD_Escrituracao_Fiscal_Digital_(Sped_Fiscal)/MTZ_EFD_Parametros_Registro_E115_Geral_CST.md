# MTZ_EFD_Parametros_Registro_E115_Geral_CST

- **Fonte:** MTZ_EFD_Parametros_Registro_E115_Geral_CST.docx
- **Modificado:** 2026-03-13
- **Tamanho:** 81 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros p/ Pré\-Geração do Registro E115 por CST \(Geral\)

__Localização__: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Geral\) 🡪 CST

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS28993

Andréa Rocha

Criação da parametrização de CST para a pré\-geração do registro E115\. 

10/09/2019

MFS30407

Andréa Rocha

Retirar a validação do campo estabelecimento para o estado igual a RS\.

26/09/2019

MFS1051812

Liliane Assaf

Alteração na pré‑geração do E115 \(Geral\) para considerar a parametrização por CST, sem utilização conjunta das parametrizações por CFOP ou CFOP/Natureza de Operação\.

Para isso a tela de Parametrização do CST está sendo alterada para inclusão do campo “Recuperação de Valores”\.

13/03/2026

Sumário

[1\.	Introdução	3](#_Toc19000873)

[2\.	Layout da Tela	3](#_Toc19000874)

[3\.	Funcionamento da Tela	4](#_Toc19000875)

[4\.	Botões da barra de menu:	5](#_Toc19000876)

[5\.	Regras de Funcionamento dos Campos	5](#_Toc19000877)

[6\.	Validações	7](#_Toc19000878)

# <a id="_Toc19000873"></a>Introdução

Esta tela tem objetivo de promover a manutenção da parametrização dos CST’s a serem utilizados na rotina de pré\-geração do registro E115, realizada no menu “Pré\-Geração 🡪 Registro E115 \(Geral\)” do módulo Sped Fiscal\.

Esta parametrização relaciona por estabelecimento, os CST’s aos Códigos de Informação Adicional, criados no item “Parâmetro 🡪 Registros E115/1925🡪 Informações Adicionais da Apuração \(Registros E115/1925\)”, determinando o valor a ser recuperado do item de mercadoria na pré\-geração\.

# <a id="_Toc19000874"></a>Layout da Tela

Estabelecimento \[XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Grupo:          \[XXXXXXXXX\]

Código:        \[\.\.\.\] \[XXXX\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

\[MFS1051812\]: incluir texto na tela:

O campo Recuperação de Valores deve ser preenchido exclusivamente quando a Parametrização do CST for utilizada isolada, sem utilização conjunta das parametrizações por CFOP ou CFOP/Natureza de Operação

\-\- CST \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-                             \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

         Código\-Descrição                                                     Recuperação de Valores \[MFS1051812\]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-                             \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\[ x \] x \-xxxxxxxxxxxxxxxxxx                                          \[\\/\] \[Valor Base Isenta  \]

\[ x \] x \-xxxxxxxxxxxxxxxxxx                                          \[\\/\] \[Valor Base Isenta  \]

\[Selecionar Todos\] \[Desmarcar Todos\]

Os dados que definem a chave de identificação da parametrização são os seguintes:

- __Empresa__
- __Estabelecimento__
- __Código__
- __Grupo CST__
- __CST__

# <a id="_Funcionamento_da_Tela"></a><a id="_Toc19000875"></a>Funcionamento da Tela

__Passo__

__Acionador__

__Descrição__

1

Usuário

Usuário seleciona o item de menu Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Geral\) 🡪 CST

2

Sistema

Verifica o usuário informou estabelecimento no login do Manager\.

3

Sistema

Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos \(Relac\_Tab\_Grupo\)\.

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Situação Tributária Estadual – B\.

Senão

Sistema exibe os grupos dos estabelecimentos da empresa, relacionados a Tabela Situação Tributária Estadual – B\.

4

Usuário

Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo\.

5

Sistema

Abre a tela de Parametrização de CST\.

Se no login foi informado estabelecimento, então:

Sistema apresenta o campo Estabelecimento bloqueado e preenchido com o estabelecimento de login\.

Senão

Sistema apresenta o campo Estabelecimento desbloqueado\.

Sistema monta a Relação de CST’s\. 

Vide regras descritas no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

6

Usuário

Usuário seleciona ou digita um Código de Informação Adicional no campo “Código”\.

7

Sistema

Valida o Código digitado\.

Vide regra do campo “Código” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

8

Usuário

Seleciona um CST e pode escolher um item da lista de Recuperação de Valores \[MFS1051812\]

9

Usuário 

Seleciona botão confirma\.

10

Sistema

Executa validações descritas no tópico [5\- Validações](#_Validações)\. 

Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva\.

11

Usuário

Seleciona outras ações disponíveis na barra de menu da janela\.

Vide tópico “[4 \- Botões da barra de menu](#_Botões_da_barra)”

# <a id="_Botões_da_barra"></a><a id="_Toc19000876"></a>Botões da barra de menu:

SELECIONAR GRUPO

Ao clicar nesta opção será aberta a janela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos \(Relac\_Tab\_Grupo\), e o usuário poderá selecionar o grupo desejado\.

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Situação Tributária B\.

Senão

Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Situação Tributária B\.

Seguir o passo 4 do fluxo descrito no tópico [3 – Funcionamento da Tela](#_Funcionamento_da_Tela)\.

CONFIRMA

Opção para salvar as informações da parametrização incluída, excluída ou alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Regras_de_Funcionamento"></a><a id="_Toc19000877"></a>Regras de Funcionamento dos Campos

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

S

Formato:

Combo Box

Lista exibindo o código e a razão social dos estabelecimentos\.

Campo ficará habilitado ou bloqueado dependendo do estabelecimento de login\.

Se no login foi informado estabelecimento, então:

Sistema apresenta o campo Estabelecimento bloqueado e preenchido com o estabelecimento de login\.

Senão

Sistema apresenta o campo Estabelecimento desbloqueado e com a lista de estabelecimentos de UF <> RS\.

__Tratamento:__

- Ao selecionar um novo estabelecimento, o campo Código deve ser limpo e consequentemente os CST’s devem ser desmarcados\.

MFS28993

Grupo 

Alfanumérico

__S__

N

Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu\.

MFS28993

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

- Ao selecionar um novo Código, os CST’s devem ser atualizados\.

__Tabela Origem:__

EFD\_INF\_ADIC\_APUR

MFS28993

Relação dos CST’s

Alfanumérico

__S__

__S__

Neste campo é exibida a lista dos CST’s cadastrados na TACES04 \- Situação Tributária Estadual – B \(Y2026\_SIT\_TRB\_UF\_B\) para seleção do usuário\.

__Seleção dos CSTs no Cadastro \(Y2026\_SIT\_TRB\_UF\_B\):__

Selecionar todos os registros de CST da tabela\.  Caso exista mais de um registro de mesmo código CST, recuperar apenas o de máxima validade\.

Do conjunto de CSTs recuperados, o sistema deve ainda aplicar o seguinte tratamento:

 \- Apresentar marcado o CST já parametrizado para o estabelecimento e Código de Informação Adicional informados\.

\- Apresentar desmarcado o CST que não está parametrizado para o estabelecimento e Código informados\.

Para selecionar os CSTs, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

MFS28993

Recuperação de Valores          

Alfanumérico

__N__

__S__

Formato:

      Combo Box

Exibir uma lista composta pela descrição dos seguintes itens:

1 \- Base Isenta ICMS

2 \- Base Outras ICMS

3 \- Base Reduzida ICMS

4 \- Base Isenta ICMS \+ Base Reduzida ICMS

5 \- Base Outras ICMS \+ Valor do ICMS\-S

6 \- Valor Desonerado ICMS

7 \- Valor Diferido ICMS

 

MFS1051812

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado e da mesma UF do Estabelecimento informado\.

Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

MFS28993

# <a id="_Validações"></a><a id="_Toc517344573"></a>

# <a id="_Toc19000878"></a>Validações

__Críticas a serem realizadas antes de salvar a operação:__

- __RN01: Campos Obrigatórios__

Validações de Campos Obrigatórios não preenchidos\.

Quando o campo é obrigatório e não estiver preenchido, exibir mensagem padrão\.

A obrigatoriedade dos campos está definida no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

       = = = = = =

