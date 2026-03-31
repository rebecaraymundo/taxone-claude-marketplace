# MTZ-SAICS-Relatorios

- **Fonte:** MTZ-SAICS-Relatorios.docx
- **Modificado:** 2023-02-28
- **Tamanho:** 31 KB

---

# Módulo – SAICS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data__

CH107003

SAICS – Relatório

Cliente solicita que na emissão do relatório Emissão dos Demonstrativos das Fichas, seja disponibilizada na Ficha 1A, a opção de gerar para todos os produtos\.

OS4377

Vitor Canin de Souza

Cliente a criação de um relatório para verificação dos produtos que estão ativos no saics\.

13/02/2014

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra para inclusão de item no drop\-dow:__

No módulo Estadual → SAICS → Relatórios → Emissão dos Demonstrativos das Fichas:

Incluir a opção \*\*\* TODOS \*\*\*, para gerar o relatório simultâneo das fichas grupo 1A, 1B, 2A, 2B, 2F, 2G, 3A, 3B e 3C\.__  __

OS3365

__RN01__

__Regra para apresentação do relatório gerado para todos os produtos, conforme RN00:__

A apresentação do relatório deve separada por produto\.

OS3365

__RN02__

__Regra para apresentação do submenu ‘Produtos Ativos no SAICS’ __

O submenu ‘Produtos Ativos no SAICS’ deve ser apresentado abaixo do submenu ‘Emissão dos Demonstrativos das Fichas’\.

OS4377

__RN03__

__Regra para seleção de grupo__

Ao clicar no submenu ‘Produtos Ativos no SAICS’ será apresentada a tela de seleção de grupo;

Serão apresentados os grupos do estabelecimento selecionado na tela inicial do Mastersaf\.

OS4377

__RN04__

__Regra para critério de seleção de Produtos Ativos no Saics__

Ao selecionar o grupo no critério de seleção de grupo;

O relatório será aberto sem informações

Será apresentada a barra de menu com os botões ‘Abre’, ‘Imprime’, ‘Página \- \-‘, ‘Página \-‘, ‘Página \+’ e ‘Página \+\+’;

Será apresentada a tela de critério de seleção de Produtos Ativos no SAICS\.

OS4377

__RN05__

__Regra para critério de seleção de Produtos Ativos no Saics – campos Cod Empresa, Cod Estab, Grupo Produto:__

__Cod Empresa__: Esse campo será preenchido com a empresa selecionada na tela inicial do sistema;

__Cod Estab:__ Esse campo será preenchido com o estabelecimento selecionado na tela inicial do sistema;

__Grupo Produto:__ Esse campo será preenchido com o grupo selecionado na tela inicial do relatório\.

OS4377

__RN06__

__Regra para critério de seleção de Produtos Ativos no Saics – campo Ind Produto, Cod Produto, Valid Produto, Descrição, Classificação do Item:__

__Ind Produto: __Nesse campo o usuário poderá informar o Indicador do Produto para qual será gerado o relatório;

__Cod Produto: __Nesse campo o usuário poderá informar o Código do Produto para qual será gerado o relatório;

__Valid Produto: __Nesse campo o usuário poderá informar a Validade  do Produto para qual será gerado o relatório;

__Descrição: __Nesse campo o usuário poderá informar a Descrição do Produto para qual será gerado o relatório;

__Classificação do Item: __Nesse campo o usuário poderá informar a Classificação do Item do Produto para qual será gerado o relatório;

OS4377

__RN07__

__Regra para apresentação do Relatório de Produtos Ativos no Saics – Título:__

‘Relatório de Produtos Ativos no SAICS’

OS4377

__RN08__

__Regra para apresentação do Relatório de Produtos Ativos no Saics – Cabeçalho:__

Na primeira linha do cabeçalho:

Será apresentada a descrição da Empresa selecionada na tela inicial do sistema no canto esquerdo;

Será apresentado o número da página ‘Página : 000001’ \(incremental\);

Na segunda linha do cabeçalho:

Será apresentado o título do relatório centralizado;

Será apresentado a data e a hora no canto direito ‘Data : 13/02/2014 às 15:11:58 hr’\.

OS4377

__RN09__

__Regra para apresentação do Relatório de Produtos Ativos no Saics:__

Serão apresentados os produtos de acordo com o critério de seleção realizado\.

OS4377

__RN10__

__Regra para apresentação do Relatório de Produtos Ativos no Saics – campos:__

Serão apresentados os Produtos \(tabela X2013\_PRODUTO\) que possuam o campo IND\_ATIVO\_SAICS = ‘S’\.

__Campos a serem apresentados:__

__Grupo Produto:__ Será apresentado o grupo selecionado na tela inicial do relatório;

__Indicador: __Será apresentada a informação do campo Ind Produto da tabela X2013\_Produto;

__Código: __Será apresentada a informação do campo Cod Produto da tabela X2013\_Produto;

__Início Validade: __Será apresentada a informação do campo Valid Produto da tabela X2013\_Produto;__ __

__Descrição: __Será apresentada a informação do campo Descricao da tabela X2013\_Produto;

__Classificação do Item: __Será apresentada a informação do campo Clas\_Item da tabela X2013\_Produto\.

OS4377

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

