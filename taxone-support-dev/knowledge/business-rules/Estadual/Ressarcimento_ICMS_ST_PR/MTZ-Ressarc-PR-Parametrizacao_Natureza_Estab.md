# MTZ-Ressarc-PR-Parametrizacao_Natureza_Estab

- **Fonte:** MTZ-Ressarc-PR-Parametrizacao_Natureza_Estab.docx
- **Modificado:** 2023-05-30
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – PR

Parametrização das Operações – Natureza Por Estabelecimento

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST \- PR, menu Parâmetros 🡪 Operações 🡪 CFOP / Natureza de Operação \(Por Estabelecimento\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS527163__

Criação da parametrização por CFOP/Natureza

Criação da parametrização das operações \(entradas e saídas\) para a atualização legal do módulo Ressarcimento ST – PR \(Norma de Procedimento Fiscal 003/20\)\. 

30/05/2023\.

Sumário

[1\.	Regras Gerais	2](#_Toc451940535)

[2\.	Layout da Tela	2](#_Toc451940536)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc451940537)

# <a id="_Toc451940535"></a>Regras Gerais

Esta é uma parametrização de CFOP/Natureza por Estabelecimento e Operação \(entradas e saídas\), para identificar as operações a serem geradas nos registros específicos das notas fiscais de entradas, saídas, e suas devoluções, do arquivo magnético da NPF 003/2020\.

Operações:

- Entradas \(e Devoluções\)
- Vendas para Consumidor Final \(e Devoluções\)
- Vendas para Outros Estados \(e Devoluções\)
- Vendas para optantes do Simples Nacional \(e Devoluções\) 

 

Para cada uma destas operações o usuário deve informar os CFOP’s/Naturezas da entrada ou saída, conforme o caso, e também o CFOP’s/Naturezas de suas respectivas devoluções\. 

Assim, para cada Operação são disponibilizados para seleção tanto os CFOP’s/Naturezas de entrada como de saída, para que o usuário possa informar os CFOP’s/Naturezas da operação principal, e também os CFOP’s/Naturezas referentes à sua devolução\.

Esta parametrização é utilizada na rotina de geração dos movimentos de entradas e saídas\.

# <a id="_Toc451940536"></a>Layout da Tela

__Botões da barra de menu__:

CONFIRMA

Opção para salvar os dados informados para a parametrização da UF e Operação\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc451940537"></a>Regras de Funcionamento dos Campos

<a id="OLE_LINK17"></a>Na abertura da tela, a janela de seleção do GRUPO será aberta automaticamente, obrigando o usuário a selecionar o grupo desejado\. Os critérios para exibição dos grupos são os mesmos descritos acima para a opção “GRUPO” da barra de menu\. 

Após a escolha do Grupo, serão exibidos o Estabelecimento e o Grupo escolhido, e o usuário poderá selecionar a Operação desejada \(campo Operação\)\.

Após escolher a Operação, serão exibidos os dados dos CFOP’s/Naturezas da SAFX2081\. As naturezas já parametrizadas para a Operação escolhida aparecerão marcadas nos botões à esquerda do quadro\.

Segue detalhamento do funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Estabelecimento

Alfanumérico 

__S__

N

Neste campo será exibido o Estabelecimento selecionado pelo usuário na abertura da tela\.

O campo não é habilitado para edição

Grupo

Alfanumérico

__S__

N

Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu\.

O campo não é habilitado para edição

Operação

Alfanumérico 

__S__

S

Listbox

Este campo é uma lista com as seguintes opções para seleção do usuário:

- Entradas \(e Devoluções\)
- Vendas para Consumidor Final \(e Devoluções\)
- Vendas para Outros Estados \(e Devoluções\)
- Vendas para optantes do Simples Nacional \(e Devoluções\)

CFOP / Natureza de Operação

Alfanumérico

__S__

S

Neste campo é exibida a lista da combinação CFOP \+ Natureza de Operação da tabela SAFX2081, para seleção do usuário\.

Os critérios para filtro dos dados da SAFX2081 são:

- CFOP \- tanto os CFOP’s de entrada como de saída, para que o usuário informe os CFOP’s da operação principal e também de suas devoluções;
- Natureza de Operação \- serão consideradas apenas as Natureza do GRUPO escolhido pelo usuário;

Como facilitador, poderá ser utilizado o botão “Marcar todos” que marca ou desmarca todos os CFOP’s/Naturezas simultaneamente\.

Ver abaixo \(__RN01__\) a crítica efetuada ao salvar a operação\.

Ao salvar os dados será feita a seguinte verificação:

__RN01 – CFOP/Natureza já parametrizado para outra operação:__

O CFOP/Natureza a ser incluído *não* pode constar na parametrização de outra operação \(campo “Operação”\)\. 

Quando ocorrer esta situação, a inclusão será efetuada apenas para os CFOP’s/Naturezas “corretos” \(não parametrizados para outra operação\)\.

Os CFOP’s/Naturezas inválidos *não* serão incluídos, e será exibida a seguinte mensagem:

                                                            *“O CFOP/Natureza XXXX\-XXX  já foi parametrizado para outra operação” *

 

Onde “*XXXX\-XXX”* é o código do CFOP/Natureza inválido\.

OBS: Caso existam vários CFOP’s/Naturezas inválidos a mensagem deve exibir o código de apenas um deles, já que não haveria como mostrar todos simultaneamente\. 

= = = = = =

