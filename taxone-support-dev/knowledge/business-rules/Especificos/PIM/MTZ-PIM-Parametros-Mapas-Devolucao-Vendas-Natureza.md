# MTZ-PIM-Parametros-Mapas-Devolucao-Vendas-Natureza

- **Fonte:** MTZ-PIM-Parametros-Mapas-Devolucao-Vendas-Natureza.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

__PIM \- Gestão do Controle de Incentivos Fiscais do Pólo Industrial de Manaus__

__   __

__Parametrização de CFOP/ Natureza de Operação – Devolução de Vendas__

__                                          __

__Localização__: Módulo PIM \- item Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP/ Natureza de Operação – Devolução de Vendas

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS6111

Andréa Rocha

Criação de parametrização de CFOP/Natureza de Operação de devolução de vendas para a geração dos Mapas Acessórios

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Esta parametrização tem como objetivo selecionar os CFOP/Natureza de Operação de Devolução de Vendas que serão utilizados na geração dos Mapas Acessórios, no cálculo dos componentes de F\.T\.I\. e U\.E\.A\. 

Opções da barra de menu:

__Abre__ 🡪Na abertura da tela, deve ser mostrada a tela de seleção dos dados\.  Devem ser mostrados o estabelecimento, o componente e a sua descrição, a estrutura e a sua descrição, o item e a sua descrição, conforme a parametrização de itens e estruturas e o cadastro dos componentes \(TFIX44\)\.  Somente devem ser mostrados os registros para a seleção que tenham o conteúdo abaixo:

__Componente__

__Estrutura__

__Item__

19

01

002

21

01

002

    Obs\.: Quando o estabelecimento estiver selecionado no login, só devem ser mostrados os registros do estabelecimento selecionado\. Caso contrário, devem ser mostrados os registros de todos os estabelecimentos que tenham cadastro de itens e estruturas\.

Após a seleção do Componente, da Estrutura e do Item de um estabelecimento, abrir a janela de seleção dos grupos de relacionamento das tabelas do Mastersaf para o estabelecimento selecionado\.

__Confirma__ 🡪 Salva os dados incluídos ou alterados para o estabelecimento, o componente, a estrutura e o item questão; 

__Relatório__ 🡪 Esta opção permite a emissão de relatório de conferência dos dados parametrizados, conforme padrão das telas de manutenção\. O critério para emissão do relatório é o Estabelecimento\. O usuário deverá obrigatoriamente selecionar um estabelecimento\. Serão listados todos os dados parametrizados para o critério selecionado;

__Fecha__ 🡪 Fecha a janela da parametrização\.

__RN01__

__                                                  Campo Estabelecimento:__

__Estabelecimento__ 🡪 mostrar o estabelecimento selecionado na abertura da tela\.

__RN02__

__                                                  Campo Componente:__

__Componente__ 🡪 mostrar o componente selecionado na abertura da tela:

__RN03__

__                                                  Campo Estrutura:__

__Estrutura__ 🡪 mostrar a estrutura selecionada na abertura da tela:

__RN04__

__                                                  Campo Item:__

__Item__ 🡪 mostrar o item selecionado na abertura da tela:

__RN05__

__                                                  Campo CFOP’s e Natureza de Operação:__

__CFOP’s__ __e Natureza de Operação__ 🡪 Neste campo é exibida a lista dos CFOP/Natureza de Operação \(SAFX2012\) para seleção do usuário, considerando apenas as operações de entrada \(códigos iniciados por “1”, “2” ou “3”\)\.

Quando existir mais de uma ocorrência do mesmo CFOP, com validades diferentes, será considerado para exibição apenas o registro de maior data de validade \(para não exibir códigos repetidos\)\.

Só estarão disponíveis para seleção, os CFOP/Natureza ainda não parametrizados para nenhum item do mapa em questão\.

Como facilitador, poderão ser utilizadas as opções “*Marcar todos*” e “*Desmarcar todos*”, para marcar ou desmarcar todos os cfop’s simultaneamente\.

__Pesquisar por CFOP: __quando for informado um CFOP, fazer a pesquisa pelo CFOP indicado, com a opção de marcar e desmarcar o CFOP selecionado\.

= = = = = 

