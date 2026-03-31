---
source: "MTZ_ReportFiscal_Relatorio_Producao_de_Terceiros.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Módulo Report Fiscal
Relatório de Produção de Terceiros (SAFX153/SAFX154)

Localização: Menu Básicos /  Report Fiscal, item de menu Gerenciais> Produção > Produção de Terceiros



DOCUMENTO DE REQUISITO


Sumário

**TELA A SER DESENVOLVIDA	3**
1.	REGRAS DOS CAMPOS	3
1.1.	LAYOUT DA TELA:	5
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	5
2.1.	Layout do Relatório	12

# TELA A SER DESENVOLVIDA

# REGRAS DOS CAMPOS

**Localização: Menu Básicos /  Report Fiscal, item de menu Gerenciais> Produção > Produção de Terceiros**

- Título da tela: Relatório de Produção de Terceiros


## LAYOUT DA TELA:








# REGRAS DE GERAÇÃO DO RELATÓRIO

**Regra Geral:**

- O novo relatório será criado no Módulo Report Fiscal.

- Para isso, deve ficar localizado no menu Gerenciais> “Produção”> Produção de Terceiros. Neste novo menu, será incluído este relatório.

- Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.




**Origem das informações para geração:**

Para geração deste relatório, serão consideradas informações das seguintes origens:

SAFX153 – Tabela de Produção de Terceiros;
SAFX154 – Tabela de Produção de Terceiros – Insumos Consumidos;

**Regra de seleção dos Relatórios:**

Deverá criar um relatório de conferência dos dados das tabelas de Produção de Terceiros (SAFX153 e 154).

Para cada produção de terceiro a ser impressa, exibir os dados da ordem de produção/serviço, e a seguir, todos os itens relacionados.

Como filtro para emissão do relatório, deve utilizar um período (data inicial e data final) e o produto.
O período (campos Data Inicial e Data Final) deve ser obrigatório e o produto ser opcional (quando não informado, considerar todos os produtos do período informado).

- Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem: “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.

- A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout
Anexo.

- Devem ser exibidos os seguintes campos no relatório:

Da SAFX153 informar as seguintes:
Identificação do Produto;
Data da Produção;
Quantidade Produzida;
Identificação da Medida;
Inscrição Estadual – AM;
Da SAFX154 informar as seguintes:
Data do Consumo;
Identificação do Insumo consumido;
Quantidade consumida;
Identificação da Medida;
Identificação do Insumo substituído;



## Layout do Relatório

Consultar o Layout no Excel:
Layout_Rel_Producao_de_Terceiros.xlsx



---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS6570 | Lara Aline | Definição das regras de criação do Relatório de Produção de Terceiros |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | ComboBox | S | S | Default: Em Branco | Nesse campo, o usuário poderá selecionar o estabelecimento. O Estabelecimento será exibido, exibindo o Código do Estabelecimento e a Descrição do mesmo. Exemplo: 001 – Estabelecimento 001.  Por default esse campo irá exibir o estabelecimento informado no Manager, caso no Manager não exista nenhum estabelecimento informado, esse campo será exibido vazio.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento dever ser Selecionado”. | MFS6570 |
| Data Inicial | Data | S | S | DD/MM/AAAA | Local para digitação do período inicial de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data Inicial que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS6570 |
| Data Final | Data | S | S | DD/MM/AAAA | Local para digitação do período final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data Final que o sistema deverá considerar para seleção das informações para a criação do relatório. Será considerada a data de produção da SAFX153 para recuperar os dados entre o período inicial e final informado. | MFS6570 |
| Produto | Alfanumérico | N | S | Default: EmBranco | - Local onde deve exibir para o usuário os produtos que constam na tabela SAFX153 (Campo COD_PRODUTO).  O campo produto é opcional. Quando não informado, considerar todos os produtos do período informado. | MFS6570 |


---

| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS6570 |
| Empresa | Texto |  | Razão social da empresa. | MFS6570 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS6570 |
| Filial | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS6570 |
| CNPJ | Alfanumérico |  | Deve exibir o CNPJ do Estabelecimento. | MFS6570 |
| Título | Texto |  | Título do relatório ‘Relatório de Produção de Terceiros’ | MFS6570 |
| Período | Numérico | Formato: MM/AAAA | Período de Referência da geração do relatório. Essa informação será recuperada de acordo com os campos “Data Inicial e Data Final” da tela de Geração. | MFS6570 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Produto | Alfanumérico |  | O conteúdo desta coluna será a concatenação dos dados de identificação do produto campo COD_PRODUTO da SAFX153:  [Indicador do produto – Código do Produto – Descrição do Produto]  (campos 01, 02 e 04 da SAFX2013).  Quando necessário, por questões de espaço, a descrição do produto poderá ser truncada. | MFS6570 |
| Data da Produção | Data | Formato: DD/MM/AAAA | Nesta coluna deve exibir a Data da Produção da Produção de Terceiros, campo DAT_PRODUCAO da SAFX153. | MFS6570 |
| Qtd Produzida | Numérico |  | Nesta coluna deve exibir a Quantidade Produzida do campo QUANTIDADE da SAFX153. | MFS6570 |
| Unidade de Medida | Alfanumérico |  | Nesta coluna deve exibir a Unidade de Medida, campo COD_MEDIDA da SAFX153. | MFS6570 |
| Inscrição Estadual/AM | Alfanumérico |  | Nesta coluna deve exibir a Inscrição Estadual – AM, campo INSC_ESTADUAL da SAFX153. | MFS6570 |
| Data Consumo | Data | Formato: DD/MM/AAAA | Nesta coluna deve exibir a Data de Consumo do campo DAT_CONSUMO da SAFX154. | MFS6570 |
| Insumo | Alfanumérico |  | O conteúdo desta coluna será a concatenação dos dados de identificação do produto campo COD_PRODUTO_INS da SAFX154:  [Indicador do Insumo – Código do Insumo – Descrição do Insumo]  (campos 01, 02 e 04 da SAFX2013).  Quando necessário, por questões de espaço, a descrição do insumo poderá ser truncada. | MFS6570 |
| Quantidade | Numérico |  | Nesta coluna deve exibir a Quantidade do campo QUANTIDADE da SAFX154. | MFS6570 |
| Unidade de Medida | Alfanumérico |  | Nesta coluna deve exibir a Unidade de Medida, campo COD_MEDIDA da SAFX154. | MFS6570 |
| Insumo Substituído | Alfanumérico |  | O conteúdo desta coluna será a concatenação dos dados de identificação do produto campo COD_PRODUTO_SUB da SAFX154:  [Indicador do Insumo – Código do Insumo – Descrição do Insumo]  (campos 01, 02 e 04 da SAFX2013).  Quando necessário, por questões de espaço, a descrição do insumo poderá ser truncada. | MFS6570 |
