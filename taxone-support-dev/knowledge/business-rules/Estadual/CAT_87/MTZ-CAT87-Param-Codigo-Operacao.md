# MTZ-CAT87-Param-Codigo-Operacao

- **Fonte:** MTZ-CAT87-Param-Codigo-Operacao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>

THOMSON REUTERS

Portaria CAT87/06 – Protocolo ECF 04\-01

__Parametrização de Código de Operação x Tipo da Operação__

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS11281

Andrea Rocha

Criação da parametrização de Código de Operação x Tipo de Operação

<a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc425354742"></a>Regras dos Campos 

__Localização da tela:__ 

Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04/01

Menu: Parâmetros 🡪 Código de Operação X Tipo da Operação

__Título da tela: __Código de Operação X Tipo da Operação

__        Regras Gerais:__

Neste item é feito um DE\-PARA dos Códigos de Operações da SAFX2001 para os Tipos de Operações da CAT87/06\.

Sobre a chave da parametrização:

     Chave lógica da parametrização: Grupo de Relacionamento \+ Código de Operação da SAFX2001

     \(cada Grupo/Código da SAFX2001 deverá ser informado uma única vez, não podendo existir duplicidade de Grupo/Código da SAFX2001\)

     \(mas diferentes Grupo/Códigos poderão ser associados ao mesmo Tipo de Operação\) 

Na abertura da tela, a janela de seleção dos grupos \(Relacionamento Tabelas x Grupos\) será exibida automaticamente, obrigando o usuário a selecionar um Grupo\. O grupo escolhido será exibido no campo “Grupo”, e será utilizado na pesquisa dos Códigos de Operações da SAFX2001\. Ver regras do funcionamento da opção “Grupo” abaixo: 

Opções da barra de menu:

__GRUPO__ – Ao clicar nesta opção, será aberta a janela de seleção dos grupos \(Relacionamento Tabelas x Grupos\), e o usuário poderá selecionar um novo grupo\. O grupo escolhido será exibido no campo “Grupo”, e será utilizado na pesquisa dos Códigos de Operações da SAFX2001\.

Regra para exibição dos grupos:        

\- Caso tenha sido informado um estabelecimento no login 🡪 Neste caso, serão exibidos apenas os grupos para os quais o estabelecimento esteja parametrizado com relacionamento para a SAFX2001\. 

\- Caso não tenha sido informado um estabelecimento no login 🡪 Neste caso, serão exibidos todos os grupos para os quais todos os estabelecimentos da empresa do login  estejam parametrizados com relacionamento para a SAFX2001\. 

__ABRE__ – Clicando nesta opção, serão exibidos em tela todos os códigos de operações já parametrizados para o grupo informado pelo usuário\. 

__CONFIRMA__ – Salva os dados incluídos ou alterados\. 

__RELATÓRIO__ – Através desta opção o usuário poderá selecionar um Grupo e emitir um relatório com os dados da parametrização dos Códigos de Operações do grupo escolhido\.

__FECHA__ – fecha a janela;

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Grupo

Texto

S

N

Neste campo será exibido o grupo selecionado pelo usuário na janela de seleção dos grupos de relacionamento Tabelas x Grupos \(opção “GRUPO” da barra de menu\)\.

\(O campo não ficará habilitado para o usuário, pois a alteração do grupo deverá ser feita sempre na opção <GRUPO> da barra de menu\. O objetivo deste campo é apenas mostrar o grupo escolhido\)

MFS11281

Operação

Texto

S

S

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Operações \(SAFX2001\)\. Serão disponibilizados para seleção apenas os códigos do grupo selecionado pelo usuário \(campo “Grupo”\)\.

Se o código da operação for digitado, será verificada a sua existência na SAFX2001, considerando o grupo em questão\. Caso não encontrado, será exibida a mensagem “Operação não cadastrada” no campo destinado a exibir a descrição da operação\. Neste caso, se o usuário tente salvar a operação \(botão <Salvar>\) sem alterar o código informado, a operação não será salva, e aparecerá uma janela com a seguinte mensagem de erro:

        “Operação não existente na Tabela dos Códigos de Operação \(SAFX2001\)”

 \(nesse caso o foco será na linha referente à operação criticada\)

MFS11281

Tipo da Operação

Dropdown

S

S

Default: selecionado

Este campo deve exibir o tipo de operação da CAT 87/06\. Deverá possuir 5 opções, conforme informado no layout:

      \- 1 \- Operação Eletrônica 

      \- 2 \- Operação Manual

      \- 3 \- POS

      \- 4 \- E\-Commerce

      \- 5 \- Demais Tecnologias

Obs\.: Por default, deverá vir selecionado a opção “1 – Operação Eletrônica”\.

MFS11281

