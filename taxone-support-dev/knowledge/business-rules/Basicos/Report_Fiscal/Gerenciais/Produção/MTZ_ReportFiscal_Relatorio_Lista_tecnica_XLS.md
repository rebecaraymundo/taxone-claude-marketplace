# MTZ_ReportFiscal_Relatorio_Lista_tecnica_XLS

- **Fonte:** MTZ_ReportFiscal_Relatorio_Lista_tecnica_XLS.docx
- **Modificado:** 2020-08-10
- **Tamanho:** 80 KB

---

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

THOMSON REUTERS

Módulo Report Fiscal

Relatório da Lista Técnica \(SAFX16/17/18\)

__Localização__: Menu Básicos 🡪 Report Fiscal, item de menu Gerenciais 🡪 Produção 🡪 Lista Técnica – Formato XLS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS41431

Andréa Rocha

Criação do Relatório de Lista Técnica – Formato XLS\.

Sumário

[TELA A SER DESENVOLVIDA	3](#_Toc47543865)

[1\.	REGRAS DA TELA	3](#_Toc47543866)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	4](#_Toc47543867)

# <a id="_Toc462838137"></a><a id="_Toc47543865"></a>TELA A SER DESENVOLVIDA

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc462838138"></a><a id="_Toc47543866"></a>REGRAS DA TELA

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Data Inicial

Data

S

S

DD/MM/AAAA

Neste campo o usuário informará uma data inicial, a ser utilizada como filtro dos registros do relatório\.

MFS41431

Data Final

Data

S

S

DD/MM/AAAA

Neste campo o usuário informará uma data final, a ser utilizada como filtro dos registros do relatório\.

MFS41431

Opções:

\- Todos os produtos

\- Selecionar um produto

Radiobutton

N

S

Default: Todos os produtos

Neste campo o usuário informará se irá gerar o relatório para todos os produtos ou se irá selecionar um produto específico\.

Quando for selecionada a opção “Selecionar um produto”, os campos de Grupo, Indicador e Código ficarão habilitados para a digitação, caso contrário estes campos ficaram desabilitados\.

MFS41431

Grupo

Listbox

N

S

Default: EmBranco

Este campo é uma lista dos grupos da Tabela dos Grupos de Relacionamento \(GRUPO\_ESTAB\)\.  A lista será habilitada apenas quando o usuário optar por selecionar um produto\. 

MFS41431

Indicador

Listbox

N

S

Default: EmBranco

Este campo é uma lista dos indicadores de produto da SAFX2013:

\- 1 \- Produto

\- 2 \- Matéria Prima/Insumo

\- 3 – Embalagem

\- 4 \- Material Uso/Consumo

\- 5 \- Outros

\- 6 \- Em Elaboração

\- 7 \- Intermediário

\- 8 \- Miscelâneas

 O campo será habilitado apenas quando o usuário optar por selecionar um produto\.

MFS41431

Produto

Alfanumérico

N

S

Default: EmBranco

Para selecionar um produto, o usuário deverá clicar na pastinha de pesquisa, onde será aberta uma janela de pesquisa da Tabela de Produtos \(SAFX2013\)\. Serão disponibilizados para seleção apenas os códigos de produto do Grupo e Indicador já escolhidos\.

O campo será habilitado apenas quando o usuário optar por selecionar um produto

MFS41431

Estabelecimento

S

S

Neste campo serão disponibilizados para seleção do usuário todos os estabelecimentos da Empresa do login\. 

MFS41431

# <a id="_Toc427766287"></a><a id="_Toc453687763"></a><a id="_Toc47543867"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas informações das seguintes tabelas:

- __SAFX16 __\- Tabela de Arquivo de Produtos Fabricados; 
- __SAFX17 __– Tabela de Arquivo de Insumos;
- __SAFX18 __\- Tabela de Arquivo Referente a Embalagem;

__Regra de seleção dos Relatórios: __

Deverá criar um relatório de conferência dos dados das tabelas da lista técnica \(SAFX16, SAFX17 e SAFX18\)\.

Para cada lista técnica a ser impressa, exibir os dados do produto principal \(SAFX16\), e a seguir, todos os insumos relacionados, mostrando os

insumos \(SAFX17\) e as embalagens \(SAFX18\)\.

Como filtro para emissão do relatório, deve utilizar um período \(data inicial e data final\), o produto e o estabelecimento\. 

O estabelecimento e o período \(campos Data Inicial e Data Final\) devem ser obrigatórios e o produto deve ser opcional \(quando não informado, considerar todos os produtos do período informado\)\.

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

Empresa

Texto

Código da empresa do login\.

MFS41431

Estabelecimento

Texto

Código do estabelecimento\.

MFS41431

CNPJ

Alfanumérico

Campo CNPJ da tabela Estabelecimento\.

MFS41431

Razão Social

Texto

Campo Razão social da tabela Estabelecimento\.

MFS41431

Período Inicial

Numérico

Formato: DD/MM/AAAA

Período inicial informado em tela\. 

MFS41431

Período Final

Numérico

Formato: DD/MM/AAAA

Período final informado em tela\. 

MFS41431

Ind\. Produto Acabado

Alfanumérico

Campo 03\-Indicador do Produto da SAFX16\.

MFS41431

Cód\. Produto Acabado

Alfanumérico

Campo 04\-Código do Produto da SAFX16\.

MFS41431

Desc\. Produto Acabado

Alfanumérico

Campo 04\-Descrição do Produto da SAFX2013 referente ao produto da SAFX16\.

MFS41431

Unidade de Medida \- Prod\. Acabado

Alfanumérico

Campo 06\-Unidade de Medida da SAFX16\.

MFS41431

                                                       Quantidade \- Prod\. Acabado

Numérico

Campo 07\-Quantidade da SAFX16\.

MFS41431

Percentual Perda \- Prod\. Acabado

Numérico

Campo 12\-Percentual de Perda da SAFX16\.

MFS41431

Data – Prod\. Acabado

Data

Formato: DD/MM/AAAA

Campo 05\-Data de Validade da SAFX16\.

MFS41431

Ind\. Produto \- Insumo

Alfanumérico

Campo 06\-Indicador do Insumo da SAFX17\.

MFS41431

Cód\. Produto \- Insumo

Alfanumérico

Campo 07\-Código do Insumo da SAFX17\.

MFS41431

Descrição \- Insumo

Alfanumérico

Campo 04\-Descrição do Produto da SAFX2013, referente ao Código do Insumo da SAFX17\.

MFS41431

Unidade de Medida \- Insumo

Alfanumérico

Campo 08\-Unidade de Medida da SAFX17\.

MFS41431

Quantidade \- Insumo

Numérico

Campo 09\-Quantidade da SAFX17\.

MFS41431

Percentual Perda \- Insumo

Numérico

Campo 11\-Percentual de Variação da SAFX17\.

MFS41431

Variação \- Insumo

Alfanumérico

Campo 15\-Tipo de Variação da SAFX17\.

Se Tipo de Variação = 0

      Mostrar “Perda”

Se Tipo de Variação = 1

      Mostrar “Ganho”

MFS41431

Ind\. Produto \- Embalagem

Alfanumérico

Campo 06\-Indicador do Insumo da SAFX18\.

MFS41431

Cód\. Produto \- Embalagem

Alfanumérico

Campo 07\-Código do Insumo da SAFX18\.

MFS41431

Descrição \- Embalagem

Alfanumérico

Campo 04\-Descrição do Produto da SAFX2013, referente ao Código do Insumo da SAFX18\.

MFS41431

Unidade de Medida \- Embalagem

Alfanumérico

Campo 08\-Unidade de Medida da SAFX18\.

MFS41431

Quantidade \- Embalagem

Numérico

Campo 09\-Quantidade da SAFX18\.

MFS41431

Percentual Perda \- Embalagem

Numérico

Campo 11\-Percentual de Variação da SAFX18\.

MFS41431

Variação \- Embalagem

Alfanumérico

Campo 15\-Tipo de Variação da SAFX18\.

Se Tipo de Variação = 0

      Mostrar “Perda”

Se Tipo de Variação = 1

      Mostrar “Ganho”

MFS41431

