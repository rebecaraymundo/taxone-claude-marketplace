---
source: "MTZ_ReportFiscal_Relatorio_Lista_Tecnica.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Módulo Report Fiscal
Relatório da Lista Técnica (SAFX16/17/18)

Localização: Menu Básicos /  Report Fiscal, item de menu Gerenciais> Produção > Lista Técnica



DOCUMENTO DE REQUISITO


Sumário

**1.	REGRAS DE GERAÇÃO DO RELATÓRIO	3**
1.1.	Layout do Relatório	6

# TELA A SER DESENVOLVIDA

# REGRAS DOS CAMPOS

**Localização: Menu Básicos /  Report Fiscal, item de menu Gerenciais> Produção > Lista Técnica**

- Título da tela: Relatório da Lista Técnica




## LAYOUT DA TELA:










# REGRAS DE GERAÇÃO DO RELATÓRIO

**Regra Geral:**

- O novo relatório será criado no Módulo Report Fiscal.

-  Para isso, deve ficar localizado no menu Gerenciais> “Produção”> Lista Técnica. Neste novo menu, será incluído este relatório, e posteriormente, os demais
relatórios previstos para as issues MFS6569, MFS6570 e MFS6571.

- Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

**Origem das informações para geração:**

Para geração deste relatório, serão consideradas informações das seguintes origens:

SAFX16 - Tabela de Arquivo de Produtos;
SAFX17 – Tabela de Arquivo de Insumos;
SAFX18 - Tabela de Arquivo Referente a Embalagem;

**Regra de seleção dos Relatórios:**

Deverá criar um relatório de conferência dos dados das tabelas da lista técnica (SAFX16, SAFX17 e SAFX18).

Para cada lista técnica a ser impressa, exibir os dados do produto principal (SAFX16), e a seguir, todos os insumos relacionados, mostrando primeiro os
insumos (SAFX17) e depois as embalagens (SAFX18).

Como filtro para emissão do relatório, deve utilizar um período (data inicial e final), e o produto. O período deve ser filtro obrigatório, e o produto será opcional
(quando não informado, considerar todos os produtos do período informado).

- Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a
mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.

- A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout
anexo. Ver layout do relatório na planilha anexa.

- Devem ser exibidos os seguintes campos no relatório:

- Da SAFX16 informar as seguintes colunas:
- Identificação do produto;
- Data de Validade;
- Identificação de Medida;
- Quantidade Fabricado;
- Percentual de Perda;
- Da SAFX17:
- Identificação do Insumo;
- Identificação de Medida;
- Quantidaded de Insumo Utilizado;
- Percentual de Variação;
- Tipo de Variação;
- Da SafX18:
- Identificação da Embalagem;
- Medida Embalagem;
- Quantidade Utilizada;







Exemplo :


---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS6567 | Jefferson Mota | Definição das regras de criação do Relatório da Lista Técnica. |
|  |  |  |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | DD/MM/AAAA | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório.  Obs: No campo do Período final, o usuário deverá informar um período maior ou igual ao período inicial. Caso informe um período menor do que o período inicial retornar a mensagem:  “O período final informado deve ser maior ou igual ao período inicial”. | MFS6567 |
| Estabelecimento | ComboBox | S | S | Default: Em Branco | Nesse campo, o usuário poderá selecionar o estabelecimento. O Estabelecimento será exibido, exibindo o Código do Estabelecimento e a Descrição do mesmo. Exemplo: 001 – Estabelecimento 001.  Por default esse campo irá exibir o estabelecimento informado no Manager, caso no Manager não exista nenhum estabelecimento informado, esse campo será exibido vazio.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento dever ser Selecionado”. | MFS6567 |
| Produto | ComboBox | S | S | Default: Em Branco | - Local onde deve exibir para o usuário os produtos que constam na tabela SAFX16.  O campo produto é opcional. Quando não informado, considerar todos os produtos do período informado. | MFS6567 |


---

| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS6567 |
| Empresa | Texto |  | Razão social da empresa. | MFS6567 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS6567 |
| Filial | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS6567 |
| CNPJ | Alfanumérico |  | Deve exibir o CNPJ do Estabelecimento. | MFS6567 |
| Título | Texto |  | Título do relatório | MFS6567 |
| Período | Numérico | Formato: DD/MM/AAAA | Período de Referência da geração do relatório. Essa informação será recuperada de acordo com o campo “Período” da tela de Geração. | MFS6567 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Identificação do Produto | Alfanumérico |  | Neste coluna deve exibir a identificação do Produto do campo IND_PRODUTO da SAFX16. | MFS6567 |
| Data de Validade | Data | Formato: DD/MM/AAAA | Neste coluna deve exibir a Data de Validade do campo DATA_MOVTO da SAFX16. | MFS6567 |
| Identificação de Medida | Alfanumérico |  | Neste coluna deve exibir a Identificação de Medida do campo COD_MEDIDA da SAFX16. | MFS6567 |
| Quantidade Fabricado | Numérico |  | Neste coluna deve exibir a Quantidade Fabricado do campo QTD_FABR da SAFX16. | MFS6567 |
| Percentual de Perda | Numérico |  | Neste coluna deve exibir o Percentual de Perda do campo PERC_PERDA da SAFX16. | MFS6567 |
| Identificação do Insumo | Alfanumérico |  | Neste coluna deve exibir a Identificação do Insumo do campo COD_INSUMO da SAFX17. | MFS6567 |
| Identificação de Medida | Alfanumérico |  | Neste coluna deve exibir a Identificação de Medida do campo COD_MEDIDA da SAFX17. | MFS6567 |
| Quantidaded de Insumo Utilizado | Numérico |  | Neste coluna deve exibir a Quantidaded de Insumo Utilizado do campo QTD_USADA da SAFX17. | MFS6567 |
| Percentual de Variação | Numérico |  | Neste coluna deve exibir o Percentual de Variação do campo PERC_PERDA da SAFX17. | MFS6567 |
| Tipo de Variação | Numérico |  | Neste coluna deve exibir o Tipo de Variação do campo TPO_VARIACAO da SAFX17. | MFS6567 |
| Identificação da Embalagem | Numérico |  | Neste coluna deve exibir a Identificação da Embalagem do campo EMBALAGEM da SAFX18. | MFS6567 |
| Medida Embalagem | Numérico |  | Neste coluna deve exibir a Medida da Embalagem do campo COD_MEDIDA da SAFX18. | MFS6567 |
| Quantidade Utilizada | Numérico |  | Neste coluna deve exibir a Quantidade Utilizada do campo QTD_USADA da SAFX18. | MFS6567 |
