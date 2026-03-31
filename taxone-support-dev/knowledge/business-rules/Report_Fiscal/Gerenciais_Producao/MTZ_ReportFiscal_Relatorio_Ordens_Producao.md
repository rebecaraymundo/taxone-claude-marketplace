---
source: "MTZ_ReportFiscal_Relatorio_Ordens_Producao.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Módulo Report Fiscal
Relatório de Ordem de Produção (SAFX108/SAFX109)

Localização: Menu Básicos /  Report Fiscal, item de menu Gerenciais> Produção > Ordens de Produção



DOCUMENTO DE REQUISITO


Sumário

**TELA A SER DESENVOLVIDA	3**
1.	REGRAS DOS CAMPOS	3
1.1.	LAYOUT DA TELA:	5
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	5
2.1.	Layout do Relatório	12

# TELA A SER DESENVOLVIDA

# REGRAS DOS CAMPOS

**Localização: Menu Básicos /  Report Fiscal, item de menu Gerenciais> Produção > Ordens de Produção**

- Título da tela: Relatório de Ordens de Produção










## LAYOUT DA TELA:








# REGRAS DE GERAÇÃO DO RELATÓRIO

**Regra Geral:**

- O novo relatório será criado no Módulo Report Fiscal.

- Para isso, deve ficar localizado no menu Gerenciais> “Produção”> Ordens de Produção. Neste novo menu, será incluído este relatório, e posteriormente, os demais relatórios previstos para as issues MFS6570 e MFS6571.

- Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

[MFS528672]  Alteração das regras de geração para permitir gerar o relatório quando não houver itens na SAFX109

**Origem das informações para geração:**

Para geração deste relatório, serão consideradas informações das seguintes origens:

SAFX108 - Tabela de Ordem de Produção;
SAFX109 – Tabela de Item da Ordem de Produção;

**Regra de seleção dos Relatórios:**

Deverá criar um relatório de conferência dos dados das tabelas de Ordem de Produção (SAFX108 e 109).

Para cada ordem de produção a ser impressa, exibir os dados da ordem de produção/serviço, e a seguir, todos os itens relacionados, se houver itens cadastrados na SAFX109.  Se não houver itens cadastrados na tabela de Item da Ordem de Produção, deverá ser gerado o relatório somente com as informações da Tabela de Ordem de Produção (SAFX108), sem mostrar o cabeçalho referente ao Item da Ordem de Produção.

Como filtro para emissão do relatório, deve utilizar um período (mês/ano), o tipo da ordem de produção/serviço, o código da ordem de produção e o produto.
O período e o tipo da ordem de produção/serviço devem ser filtros obrigatórios, o código da ordem de produção e produto serão opcionais
(quando não informado, considerar todos os códigos da ordem de produção e produtos do período informado).

- Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a
mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.

- A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout
Anexo.


Para o Tipo da Ordem de Produção/Serviço igual a ‘Produção’:


- Devem ser exibidos os seguintes campos no relatório:

Da SAFX108 informar as seguintes:
Código da Ordem de Produção/Serviço;
Cód. Diferenciador de Produção;
Data de Início da Ordem de Produção/Serviço;
Data de Conclusão da Ordem de Produção/Serviço;
Identificação do Produto;
Inscrição Estadual – AM;
Identificação de Medida;
Código do Processo de Produção Conjunta;
Quantidade Produzida;
Apuração de Custo;
Total de Custos Diretos e Indiretos;
Quantidade Transferida;
Valor Transferido;
Valor do Custo SAICS;
Valor do Custo SAICS.
Da SAFX109 informar as seguintes:
Item da Ordem de Produção/Serviço;
Identificação do Produto;
Identificação da Medida;
Identificação do Insumo Substituído;
Data de Saída;
Quantidade Utilizada;
Valor Unitário;
Valor do Custo SAICS;
Valor do Custo SAICS.

Para o Tipo da Ordem de Produção/Serviço igual a ‘Desmontagem de Mercadorias’:


- Devem ser exibidos os seguintes campos no relatório:

Da SAFX108 informar as seguintes:
Código da Ordem de Produção/Serviço;
Cód. Diferenciador de Produção;
Identificação de Medida;
Identificação do Produto;
Data de Início da Ordem de Produção/Serviço;
Data de Conclusão da Ordem de Produção/Serviço;

Inscrição Estadual – AM;
Quantidade de Origem (saída do estoque).
Da SAFX109 informar as seguintes:
Item da Ordem de Produção/Serviço;
Identificação do Produto;
Identificação da Medida;
Quantidade de Destino (entrada no estoque).

Para o Tipo da Ordem de Produção/Serviço igual a ‘Reprocessamento/Reparo:


- Devem ser exibidos os seguintes campos no relatório:

Da SAFX108 informar as seguintes:
Código da Ordem de Produção/Serviço;
Cód. Diferenciador de Produção;
Identificação de Medida;
Identificação do Produto;
Data de Início da Ordem de Produção/Serviço;
Data de Conclusão da Ordem de Produção/Serviço;
Inscrição Estadual – AM;
Data da Saída do Estoque;
Data Retorno;
Quantidade da Saída;
Quantidade Retorno.
Da SAFX109 informar as seguintes:
Item da Ordem de Produção/Serviço;
Identificação do Produto;
Identificação da Medida;
Qtd Utilizada;
Qtd Retornada.






## Layout do Relatório

Consultar o Layout no Excel:
Layout_Rel_Ordens_Producao.xlsx



---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS6569 | Lara Aline | Definição das regras de criação do Relatório das Ordens de Produção |  |
| MFS6641 | Lara Aline | Definição das regras para o Tipo da Ordem de Produção/Serviço - Desmontagem de Mercadorias. |  |
| MFS6642 | Lara Aline | Definição das regras para o Tipo da Ordem de Produção/Serviço - Reprocessamento/Reparo. |  |
| MFS10055 | Alteração tamanho do código da OP | Aumento do número da ordem de produção de 15 para 30 posições | 21/03/2017 |
| MFS528672 | Andréa Rocha | Alteração da regra de geração do relatório, para permitir gerar o relatório quando só houver dados na SAFX108, ou seja, quando não houver itens na SAFX109. Essa alteração está sendo feita porque a geração do arquivo do SPED-EFD para períodos a partir de janeiro de 2023, não obriga a geração dos itens da ordem produção (SAFX109). | 19/04/2023 |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | ComboBox | S | S | Default: Em Branco | Nesse campo, o usuário poderá selecionar o estabelecimento. O Estabelecimento será exibido, exibindo o Código do Estabelecimento e a Descrição do mesmo. Exemplo: 001 – Estabelecimento 001.  Por default esse campo irá exibir o estabelecimento informado no Manager, caso no Manager não exista nenhum estabelecimento informado, esse campo será exibido vazio.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento dever ser Selecionado”. | MFS6569 |
| Período | Data | S | S | MM/AAAA | Local para digitação do período referencia da geração do relatório, no formato de MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS6569 |
| Tipo da Ordem de Produção/Serviço | ComboBox | S | S | Default: Em Branco | Nesse campo, o usuário deverá selecionar o Tipo da Ordem de Produção/Serviço conforme opções abaixo:  - Produção; - Desmontagem de Mercadorias; - Reprocessamento/Reparo;  Campo de preenchimento obrigatório. Existem três layouts específicos de relatório (Layout_Rel_Ordens_Producao.xlsx) um para cada opção de Tipo da Ordem de Produção/Serviço escolhida pelo usuário:  Aba Produção = Opção Produção; Aba Desmontagem de Mercadorias = Opção Desmontagem de Mercadorias; Aba Reprocessamento-Reparo = Opção Reprocessamento/Reparo; | MFS6569 MFS6641 MFS6642 |
| Código da Ordem de Produção | ComboBox | N | S | Default: Em Branco | - Local onde deve exibir para o usuário os códigos da ordem de produção/serviço que constam na tabela SAFX108 (Campo COD_OP).  O campo é opcional. Quando não informado, considerar todos os códigos da ordem de produção/serviço do período informado.  Alteração da MFS10055: O tamanho deste campo foi alterado de 15 para 30 posições. | MFS6569 |
| Produto | Alfanumérico | N | S | Default: EmBranco | - Local onde deve exibir para o usuário os produtos que constam na tabela SAFX108 (Campo COD_PRODUTO_OP).  O campo produto é opcional. Quando não informado, considerar todos os produtos do período informado. | MFS6569 |


---

| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS6569 |
| Empresa | Texto |  | Razão social da empresa. | MFS6569 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS6569 |
| Filial | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS6569 |
| CNPJ | Alfanumérico |  | Deve exibir o CNPJ do Estabelecimento. | MFS6569 |
| Título | Texto |  | Título do relatório ‘Relatório de Ordens de Produção (SAFX108/109)’ | MFS6569 |
| Período | Numérico | Formato: MM/AAAA | Período de Referência da geração do relatório. Essa informação será recuperada de acordo com o campo “Período (mês/ano)” da tela de Geração. | MFS6569 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Cód. OP/Serviço | Alfanumérico |  | Nesta coluna deve exibir o Código da Ordem de Produção/Serviço, campo COD_OP da SAFX108.  Alteração da MFS10055: O tamanho deste campo  foi alterado de 15 para 30 posições. | MFS6569 |
| Cód. Dif.Produção | Alfanumérico |  | Nesta coluna deve exibir o Cód. Diferenciador de Produção, campo COD_DIF_PRODUCAO da SAFX108. | MFS6569 |
| Data Início OP/OS | Data | Formato: DD/MM/AAAA | Nesta coluna deve exibir a Data de Início da Ordem de Produção/Serviço, campo DT_INI_OP da SAFX108. | MFS6569 |
| Data Conclusão OP/OS | Data | Formato: DD/MM/AAAA | Nesta coluna deve exibir a Data de Conclusão da Ordem de Produção/Serviço, campo DT_FIM_OP da SAFX108. | MFS6569 |
| Produto | Alfanumérico |  | O conteúdo desta coluna será a concatenação dos dados de identificação do produto campo COD_PRODUTO_OP da SAFX108:  [Indicador do produto – Código do Produto – Descrição do Produto]  (campos 01, 02 e 04 da SAFX2013).  Quando necessário, por questões de espaço, a descrição do produto poderá ser truncada. | MFS6569 |
| Inscrição Estadual/AM | Alfanumérico |  | Nesta coluna deve exibir a Inscrição Estadual – AM, campo INSC_ESTADUAL da SAFX108. | MFS6569 |
| Unidade de Medida | Alfanumérico |  | Nesta coluna deve exibir a Unidade de Medida, campo COD_UND_PADRAO da SAFX108. | MFS6569 |
| Cód. Descr Processo Produção | Alfanumérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  O conteúdo desta coluna será a concatenação dos dados de identificação do Código do Processo de Produção Conjunta, campo COD_PROCESSO_PRODUCAO da SAFX108:  [Código do Processo Produção – Descrição do Processo Produção]  (campos COD_PROCESSO_PRODUCAO e DSC_PROCESSO_PRODUCAO da tabela SAICS_PROCESSO_PRODUCAO).  Quando necessário, por questões de espaço, a descrição do processo produção poderá ser truncada. | MFS6569 |
| Qtd Produzida | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Quantidade Produzida do campo QTD_PRODUZIDO da SAFX108. | MFS6569 |
| Apuração de Custo | Alfanumérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir informação da Apuração de Custo do campo IND_APUR_CUSTO da SAFX108.  Demonstrar conforme abaixo: S - Sim N - Não | MFS6569 |
| Total dos Custos | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir o Total de Custos Diretos e Indiretos, campo VLR_TOT_CUSTO da SAFX108. | MFS6569 |
| Qtd Transferida | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Quantidade Transferida, campo QTD_TRANSF da SAFX108. | MFS6569 |
| Valor Transferido | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir o Valor Transferido, campo VLR_TRANSF da SAFX108. | MFS6569 |
| Valor Custo (SAICS) | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir o Valor Custo (SAICS), campo VLR_CUSTO_DCA da SAFX108. | MFS6569 |
| Valor ICMS (SAICS) | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir o Valor ICMS (SAICS), campo VLR_ICMS_DCA da SAFX108. | MFS6569 |
| Quantidade de Origem (saída do estoque) | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Desmontagem de Mercadorias’, aba Desmontagem de Mercadorias Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Quantidade Origem do campo QTD_ORIGEM da SAFX108. | MFS6569 MFS6641 |
| Data da Saída do Estoque | Data | Formato: DD/MM/AAAA | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Reprocessamento/Reparo’, aba Reprocessamento/Reparo Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Data Saída do Estoque do campo DT_SAIDA_ESTQ da SAFX108. | MFS6569 MFS6642 |
| Data Retorno | Data | Formato: DD/MM/AAAA | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Reprocessamento/Reparo’, aba Reprocessamento/Reparo Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Data Retorno ao Estoque do campo DT_RET_ESTQ da SAFX108. | MFS6569 MFS6642 |
| Quantidade da Saída | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Reprocessamento/Reparo’, aba Reprocessamento/Reparo Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Quantidade da Saída do campo QTD_SAIDA_ESTQ da SAFX108. | MFS6569 MFS6642 |
| Quantidade Retorno | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Reprocessamento/Reparo’, aba Reprocessamento/Reparo Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Quantidade do Retorno do campo QTD_RET_ESTQ da SAFX109. | MFS6569 MFS6642 |
| Item | Numérico |  | Nesta coluna deve exibir o Item da Ordem de Produção/Serviço, campo NUM_ITEM da SAFX109. | MFS6569 |
| Unidade de Medida | Alfanumérico |  | Nesta coluna deve exibir a Unidade de Medida, campo COD_UND_PADRAO da SAFX109. | MFS6569 |
| Produto | Alfanumérico |  | O conteúdo desta coluna será a concatenação dos dados de identificação do produto campo COD_PRODUTO da SAFX109:  [Indicador do produto – Código do Produto – Descrição do Produto]  (campos 01, 02 e 04 da SAFX2013).  Quando necessário, por questões de espaço, a descrição do produto poderá ser truncada. | MFS6569 |
| Insumo Substituído | Alfanumérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  O conteúdo desta coluna será a concatenação dos dados de identificação do produto campo COD_INSUMO_SUBST da SAFX109:  [Indicador do Insumo – Código do Insumo – Descrição do Insumo]  (campos 01, 02 e 04 da SAFX2013).  Quando necessário, por questões de espaço, a descrição do insumo poderá ser truncada. | MFS6569 |
| Data Saída | Data | Formato: DD/MM/AAAA | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Data de Saída do campo DT_SAIDA da SAFX109. | MFS6569 |
| Qtd Utilizada | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Qtd Utilizada, campo QTD_PRODUZIDO da SAFX109. | MFS6569 |
| Valor Unitário | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir o Valor Unitário, campo VLR_UNIT da SAFX109. | MFS6569 |
| Valor Custo (SAICS) | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir o Valor Custo (SAICS), campo VLR_CUSTO_DCA da SAFX109. | MFS6569 |
| Valor ICMS (SAICS) | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Produção’, aba Produção Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir o Valor ICMS (SAICS), campo VLR_ICMS_DCA da SAFX109. | MFS6569 |
| Quantidade de Destino (entrada no estoque) | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Desmontagem de Mercadorias’, aba Desmontagem de Mercadorias Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Quantidade de Destino do campo QTD_DESTINO da SAFX108. | MFS6569 MFS6641 |
| Qtd Utilizada | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Reprocessamento/Reparo’, aba Reprocessamento/Reparo Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Quantidade Utilizada – Reprocessamento do campo QTD_REPROC da SAFX108. | MFS6569 MFS6642 |
| Qtd Retornada | Numérico |  | Esse campo corresponde apenas ao layout do relatório do Tipo da Ordem de Produção/Serviço igual a ‘Reprocessamento/Reparo’, aba Reprocessamento/Reparo Excel: Layout_Rel_Ordens_Producao.xlsx  Nesta coluna deve exibir a Quantidade Retornada do campo QTD_RETORNADA da SAFX108. | MFS6569 MFS6642 |
