# MTZ-Ressarc-PR-Parametrizacao_CFOPs_Estab

- **Fonte:** MTZ-Ressarc-PR-Parametrizacao_CFOPs_Estab.docx
- **Modificado:** 2023-05-30
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – PR

Parametrização das Operações – CFOPs por Estabelecimento

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST \- PR, menu Parâmetros 🡪 Operações 🡪 CFOP \(Por Estabelecimento\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS527163__

Criação da parametrização por CFOP

Criação da parametrização das operações \(entradas e saídas\) para a atualização legal do módulo Ressarcimento ST – PR \(Norma de Procedimento Fiscal 003/20\)\. 

30/05/2023\.

Sumário

[1\.	Regras Gerais	2](#_Toc451940535)

[2\.	Layout da Tela	2](#_Toc451940536)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc451940537)

# <a id="_Toc451940535"></a>Regras Gerais

Esta é uma parametrização de CFOP por Estabelecimento e Operação \(entradas e saídas\), para identificar as operações a serem geradas nos registros específicos das notas fiscais de entradas, saídas, e suas devoluções, do arquivo magnético da NPF 003/2020\.

Operações:

- Entradas \(e Devoluções\)
- Vendas para Consumidor Final \(e Devoluções\)
- Vendas para Outros Estados \(e Devoluções\)
- Vendas para optantes do Simples Nacional \(e Devoluções\) 

Para cada uma destas operações o usuário deve informar os CFOP’s da entrada ou saída, conforme o caso, e também o CFOP de suas respectivas devoluções\. 

Assim, para cada operação são disponibilizados para seleção tanto os CFOP’s de entrada como de saída, para que o usuário possa informar os CFOP’s da operação principal, e também os CFOP’s referentes à sua devolução\.

Esta parametrização é utilizada na rotina de geração dos movimentos de entradas e saídas\.

# <a id="_Toc451940536"></a>Layout da Tela

__Botões da barra de menu__:

CONFIRMA

Opção para salvar os dados informados para a parametrização da CFOP e Operação\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc451940537"></a>Regras de Funcionamento dos Campos

Na abertura da tela, será exibida o estabelecimento, se for informado no login, e o usuário poderá selecionar a operação desejada \(campo Operação\)\.

Após escolher a Operação, serão exibidos os dados dos CFOP’s da SAFX2012\. Os CFOP’s já parametrizados para a Operação escolhida aparecerão marcados nos botões à esquerda do quadro\.

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

S

Este campo é uma lista dos estabelecimentos de PR, da empresa do login para seleção do usuário\. 

Quando for informado um estabelecimento de PR no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá\-lo\.

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

CFOP’s

Alfanumérico

__S__

S

Neste campo é exibida a lista dos CFOP’s \(SAFX2012\) para seleção do usuário\.

Serão disponibilizados para seleção tanto os CFOP’s de entrada como de saída, para que o usuário informe os CFOP’s da operação principal e também de suas devoluções\.

Quando existir na SAFX2012 mais de uma ocorrência do mesmo CFOP, com datas de  validade diferentes, será considerado para exibição apenas o registro de maior data de validade \(para não exibir códigos repetidos\)\.

Como facilitador, poderá ser utilizado o botão “Marcar todos” que marca ou desmarca todos os CFOP’s simultaneamente\.

Ver abaixo \(__RN01__\) a crítica efetuada ao salvar a operação\.

 

Ao salvar os dados será feita a seguinte verificação:

__RN01 – CFOP já parametrizado para outra operação:__

O CFOP a ser incluído *não* pode constar na parametrização de outra operação \(campo “Operação”\)\. 

Quando ocorrer esta situação, a inclusão será efetuada apenas para os CFOP’s “corretos” \(não parametrizados para outra operação\)\.

Os CFOP’s inválidos *não* serão incluídos, e será exibida a seguinte mensagem:

                                                     *“O CFOP XXXX já foi parametrizado para outra operação” *

 

Onde “*XXXX”* é o código do CFOP inválido\.

OBS: Caso existam vários CFOP’s inválidos a mensagem deve exibir o código de apenas um deles, já que não haveria como mostrar todos simultaneamente\. 

= = = = = =

