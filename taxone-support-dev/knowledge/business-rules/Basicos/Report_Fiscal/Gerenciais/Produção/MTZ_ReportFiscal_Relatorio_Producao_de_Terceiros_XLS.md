# MTZ_ReportFiscal_Relatorio_Producao_de_Terceiros_XLS

- **Fonte:** MTZ_ReportFiscal_Relatorio_Producao_de_Terceiros_XLS.docx
- **Modificado:** 2020-08-10
- **Tamanho:** 78 KB

---

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

THOMSON REUTERS

Módulo Report Fiscal

Relatório de Produção de Terceiros em XLS \(SAFX153/SAFX154\)

__Localização__: Menu Básicos 🡪 Report Fiscal, item de menu Gerenciais 🡪 Produção 🡪 Produção de Terceiros – Formato XLS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS41403

Andréa Rocha

Criação do Relatório de Produção de Terceiros – Formato XLS\.

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

MFS41403

Data Final

Data

S

S

DD/MM/AAAA

Neste campo o usuário informará uma data final, a ser utilizada como filtro dos registros do relatório\.

MFS41403

Opções:

\- Todos os produtos

\- Selecionar um produto

Radiobutton

N

S

Default: Todos os produtos

Neste campo o usuário informará se irá gerar o relatório para todos os produtos ou se irá selecionar um produto específico\.

Quando for selecionada a opção “Selecionar um produto”, os campos de Grupo, Indicador e Código ficarão habilitados para a digitação, caso contrário estes campos ficaram desabilitados\.

MFS41403

Grupo

Listbox

N

S

Default: EmBranco

Este campo é uma lista dos grupos da Tabela dos Grupos de Relacionamento \(GRUPO\_ESTAB\)\.  A lista será habilitada apenas quando o usuário optar por selecionar um produto\. 

MFS41403

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

MFS41403

Produto

Alfanumérico

N

S

Default: EmBranco

Para selecionar um produto, o usuário deverá clicar na pastinha de pesquisa, onde será aberta uma janela de pesquisa da Tabela de Produtos \(SAFX2013\)\. Serão disponibilizados para seleção apenas os códigos de produto do Grupo e Indicador já escolhidos\.

O campo será habilitado apenas quando o usuário optar por selecionar um produto

MFS41403

Estabelecimento

S

S

Neste campo serão disponibilizados para seleção do usuário todos os estabelecimentos da Empresa do login\. 

MFS41403

# <a id="_Toc427766287"></a><a id="_Toc453687763"></a><a id="_Toc47543867"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas informações das seguintes tabelas:

- __SAFX153 __– Tabela de Produção de Terceiros; 
- __SAFX154 __– Tabela de Produção de Terceiros – Insumos Consumidos;

__Regra de seleção dos Relatórios: __

Deverá criar um relatório de conferência dos dados das tabelas de Produção de Terceiros \(SAFX153 e SAFX154\)\.

Para cada produção de terceiro a ser demonstrada, exibir os dados da ordem de produção/serviço, e de todos os itens relacionados\.

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

MFS41403

Estabelecimento

Texto

Código do estabelecimento\.

MFS41403

CNPJ

Alfanumérico

Campo CNPJ da tabela Estabelecimento\.

MFS41403

Razão Social

Texto

Campo Razão social da tabela Estabelecimento\.

MFS41403

Período Inicial

Numérico

Formato: DD/MM/AAAA

Período inicial informado em tela\. 

MFS41403

Período Final

Numérico

Formato: DD/MM/AAAA

Período final informado em tela\. 

MFS41403

Ind\. Produto

Alfanumérico

Campo 04\-Indicador do Produto da SAFX153\.

MFS41403

Cód\. Produto

Alfanumérico

Campo 05\-Código do Produto da SAFX153\.

MFS41403

Desc\. Produto

Alfanumérico

Campo 04\-Descrição do Produto da SAFX2013 referente ao produto da SAFX153\.

MFS41403

                                                       Data da Produção

Data

Formato: DD/MM/AAAA

Campo 03\-Data da Produção da SAFX153\.

MFS41403

Qtd Produzida

Numérico

Campo 06\-Quantidade da SAFX153\.

MFS41403

Unidade de Medida

Alfanumérico

Campo 07\-Unidade de Medida da SAFX153\.

MFS41403

                                                       Inscrição Estadual/AM

Alfanumérico

Campo 08\-Inscrição Estadual\-AM da SAFX153\.

MFS41403

Data Consumo \- Insumos Consumidos

Data

Formato: DD/MM/AAAA

Campo 06\-Data do Consumo da SAFX154\.

MFS41403

Ind\. Produto \- Insumos Consumidos

Alfanumérico

Campo 07\-Indicador do Insumo da SAFX154\.

MFS41403

Cód\. Produto \- Insumos Consumidos

Alfanumérico

Campo 08\-Código do Insumo da SAFX154\.

MFS41403

Descrição \- Insumos Consumidos

Alfanumérico

Campo 04\-Descrição do Produto da SAFX2013, referente ao Código do Insumo da SAFX154\.

MFS41403

Quantidade \- Insumos Consumidos

Numérico

Campo 10\-Quantidade da SAFX154\.

MFS41403

Unidade de Medida \- Insumos Consumidos

Alfanumérico

Campo 11\-Unidade de Medida da SAFX154\.

MFS41403

Ind\. Insumo Subst\. \- Insumos Consumidos

Alfanumérico

Campo 12\-Indicador do Insumo Substituído da SAFX154\.

MFS41403

Cód\. Insumo Subst\. \- Insumos Consumidos

Alfanumérico

Campo 13\-Código do Insumo Substituído da SAFX154\.

MFS41403

Descrição Insumo Subst\.\- Insumos Consumidos

Alfanumérico

Campo 04\-Descrição do Produto da SAFX2013, referente ao código do insumo substituído da SAFX154\.

MFS41403

