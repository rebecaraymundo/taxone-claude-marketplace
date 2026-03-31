---
source: "MTZ-RF_Conf_Doctos_Fiscais_ICMS_IPI_PIS_COFINS.docx"
category: Report_Fiscal
converted: auto
---



THOMSON REUTERS

**Módulo Report Fiscal**

**Relatório de Conferência de Documentos Fiscais (ICMS/IPI/PIS/COFINS)**


Localização: Menu Básicos, Módulo Report Fiscal, item Gerenciais  Documentos Fiscais  Analíticos  Conferência de Documentos Fiscais (ICMS/IPI/PIS/COFINS)


DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO



Este relatório foi criado na OS4312.

Seu objetivo é a conferência dos valores de  ICMS, IPI, PIS e COFINS por item de documento fiscal.


Período – Neste campo o usuário informará uma data inicial e uma data final, a serem utilizadas como filtro dos documentos fiscais.

Movimento – Este campo é uma lista com as seguintes opções: “Entradas”, “Saídas” e “Ambos”. Seu preenchimento é obrigatório.

UF – Este campo é uma lista das UF’s da tabela de estados + a opção “Todas”. Seu preenchimento é obrigatório.

Estabelecimentos – Neste campo serão disponibilizados para seleção do usuário todos os estabelecimentos da Empresa do login que sejam da UF selecionada no campo “UF”.


Origem dos dados: Tabelas dos Documentos Fiscais – Capa e Itens  (SAFX07/SAFX08/SAFX09)

Critérios de recuperação dos documentos na SAFX07:

- COD_EMPRESA – código da empresa do  login
- COD_ESTAB – estabelecimentos selecionados em tela
- DATA_FISCAL – data fiscal que se enquadre no período informado em tela
- MOVTO_E_S – se parâmetro “Movimento” = Entradas  serão consideradas apenas notas de entrada (MOVTO_E_S <> 9);
se parâmetro “Movimento” = Saídas serão consideradas apenas notas de saída (MOVTO_E_S = 9);
se parâmetro “Movimento” = Ambos  serão consideradas tanto as entradas, como as saídas;
- SITUACAO – somente os documentos não cancelados

Para cada documento recuperado de acordo com os critérios acima, serão recuperados todos os seus itens, tanto itens de mercadorias (SAFX08), como serviços (SAFX09), ou ambos (SAFX08 e SAFX09).

Notas fiscais sem itens também serão consideradas para o relatório.



Os dados recuperados serão agrupados por Estabelecimento, e para cada Estabelecimento, será emitido um relatório.

Na quebra de estabelecimento, haverá um salto de página no relatório.

Para cada Estabelecimento, serão listadas em primeiro lugar as operações de entrada (MOVTO_E_S <> 9), e depois as saídas (MOVTO_E_S = 9).

Ordenação dos dados:

- Tanto para as operações de entrada, como para as saídas, os documentos serão ordenados por data fiscal.

- Para uma mesma data fiscal, os documentos serão ordenados por número.

- Para um mesmo número de documento, os seus itens serão ordenados pelo número do item.




As três primeiras colunas do relatório são referentes às informações da capa do documento (SAFX07).

A partir da coluna “Item”, são informações referentes aos itens do documento, que poderão ser itens de mercadoria (SAFX08), ou itens de serviço (SAFX09). No caso das notas sem itens, estas colunas serão preenchidas com informações da própria capa do documento (SAFX07), e em alguns casos, ficarão sem preenchimento.

Segue regras de preenchimento dos campos:

Cabeçalho:


Linhas de Detalhe:


Linhas de Totalização:






= = = = =

---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OS4312 | Novo relatório | Desenvolvimento de um novo relatório no RF para conferência dos documentos fiscais, com os valores de ICMS, IPI, PIS e COFINS. | 25/02/2014 (criação do docto) |
| CH3025_2016 | Tratamento no preenchimento dos campos CST PIS e COFINS | Este documento tem como objetivo alterar o preenchimento da coluna CST de PIS e Cofins do relatório de Conferência de Documentos Fiscais (ICMS/IPI/COFINS) do módulo Básicos – Report Fiscal, para considerar sempre dois dígitos. | 11/05/2016 |
| MFS_4449 | Inclusão do campo CFOP nos campos de detalhe do relatório. | Este documento tem como objetivo incluir a coluna CFOP | 25/05/2016 |


---

| RN00 | Regras Gerais |
| --- | --- |



---

| RN01 | Parâmetros de Tela |
| --- | --- |



---

| RN02 | Recuperação dos Dados |
| --- | --- |



---

| RN03 | Processamento |
| --- | --- |



---

| RN04 | Preenchimento dos Dados |
| --- | --- |



---

| Primeira linha do cabeçalho | A primeira linha do cabeçalho demonstra a razão social da empresa, a data de emissão do relatório e o número da página. |
| --- | --- |
| Segunda linha do cabeçalho | O campo “Filial” será preenchido com o código e a razão social do estabelecimento em questão. No campo “Período” será exibido o período solicitado em tela (data inicial e data final), e ao lado aparecerá o tipo de movimento solicitado em tela, no seguinte formato:       - Se opção de tela = Entradas  o conteúdo será = (Entradas)      - Se opção de tela = Saídas    o conteúdo será = (Saídas)      - Se opção de tela = Ambos   o conteúdo será = (Entradas e Saídas)  O campo “Insc.Estadual” será preenchido com a inscrição estadual do estabelecimento (inscrição estadual da sua própria UF). O campo “CNPJ” será preenchido com o CNPJ do estabelecimento. |


---

| NF | Número do documento fiscal (SAFX07) | Estas colunas são informações da capa do documento, e serão preenchidas apenas na linha do primeiro item do documento. Para os demais itens (caso existam), as colunas aparecerão em branco. |
| --- | --- | --- |
| Dt.Fiscal | Data fiscal do documento (SAFX07) | Estas colunas são informações da capa do documento, e serão preenchidas apenas na linha do primeiro item do documento. Para os demais itens (caso existam), as colunas aparecerão em branco. |
| Item | Número do item do documento: Se item da SAFX08  campo 18-Item Nota Fiscal;  Se item da SAFX09  campo 13-Item Nota Fiscal;  Notas sem itens  neste caso, a coluna não será preenchida; | Número do item do documento: Se item da SAFX08  campo 18-Item Nota Fiscal;  Se item da SAFX09  campo 13-Item Nota Fiscal;  Notas sem itens  neste caso, a coluna não será preenchida; |
| Descrição | Descrição complementar do item: Se item da SAFX08  campo 21-Descrição Complementar;  Se item da SAFX09  campo 16-Descrição Complementar;  Notas sem itens  neste caso, a coluna não será preenchida; | Descrição complementar do item: Se item da SAFX08  campo 21-Descrição Complementar;  Se item da SAFX09  campo 16-Descrição Complementar;  Notas sem itens  neste caso, a coluna não será preenchida; |
| CFOP | Código Fiscal (SAFX07) | Código Fiscal (SAFX07) |
| Valor Contábil | Valor do item: Se item da SAFX08  campo 64-Valor Contábil do Item;  Se item da SAFX09  campo 15-Valor Total do Serviço;  Notas sem itens  campo 23-Valor Total da SAFX07 | Valor do item: Se item da SAFX08  campo 64-Valor Contábil do Item;  Se item da SAFX09  campo 15-Valor Total do Serviço;  Notas sem itens  campo 23-Valor Total da SAFX07 |
| ICMS – CST | Código da situação tributária do ICMS: Se item da SAFX08  concatenação dos campos 30 e 31 (códigos de Situação Tributária A e B);  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  concatenação dos campos 179 e 180 (códigos de Situação Tributária A e B) da SAFX07; | Código da situação tributária do ICMS: Se item da SAFX08  concatenação dos campos 30 e 31 (códigos de Situação Tributária A e B);  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  concatenação dos campos 179 e 180 (códigos de Situação Tributária A e B) da SAFX07; |
| ICMS - Base | Valor da base tributada do ICMS: Se item da SAFX08  campo 56-Base ICMS (se campo 55-Tributação ICMS = 1);  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “51-Base ICMS Tributada” da SAFX07; | Valor da base tributada do ICMS: Se item da SAFX08  campo 56-Base ICMS (se campo 55-Tributação ICMS = 1);  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “51-Base ICMS Tributada” da SAFX07; |
| ICMS – Valor | Valor do ICMS: Se item da SAFX08  campo 43-Valor ICMS;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “35-Valor ICMS” da SAFX07; | Valor do ICMS: Se item da SAFX08  campo 43-Valor ICMS;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “35-Valor ICMS” da SAFX07; |
| ICMS – Aliq | Alíquota do ICMS: Se item da SAFX08  campo 42-Alíquota ICMS;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “34-Alíquota ICMS” da SAFX07; | Alíquota do ICMS: Se item da SAFX08  campo 42-Alíquota ICMS;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “34-Alíquota ICMS” da SAFX07; |
| IPI – CST | Código da situação tributária do IPI: Se item da SAFX08  campo 146-Código de Tributação IPI;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  neste caso, a coluna não será preenchida; | Código da situação tributária do IPI: Se item da SAFX08  campo 146-Código de Tributação IPI;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  neste caso, a coluna não será preenchida; |
| IPI – Base | Valor da base tributada do IPI: Se item da SAFX08  campo 59-Base IPI (se campo 58-Tributação IPI = 1);  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “55-Base IPI Tributada” da SAFX07; | Valor da base tributada do IPI: Se item da SAFX08  campo 59-Base IPI (se campo 58-Tributação IPI = 1);  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “55-Base IPI Tributada” da SAFX07; |
| IPI – Valor | Valor do IPI: Se item da SAFX08  campo 48-Valor IPI;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “40-Valor IPI” da SAFX07; | Valor do IPI: Se item da SAFX08  campo 48-Valor IPI;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “40-Valor IPI” da SAFX07; |
| IPI – Aliq | Alíquota do IPI: Se item da SAFX08  campo 47-Alíquota IPI;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “39-Alíquota IPI” da SAFX07; | Alíquota do IPI: Se item da SAFX08  campo 47-Alíquota IPI;  Se item da SAFX09  neste caso, a coluna não será preenchida;  Notas sem itens  campo “39-Alíquota IPI” da SAFX07; |
| PIS - CST | Código da situação tributária do PIS: Se item da SAFX08  campo 175-Código Situação Tributária PIS;  Se item da SAFX09  campo 68-Código de Situação Tributária PIS;  Notas sem itens  campo “249-Código Situação Tributária PIS” da SAFX07;  [ALTERADA – CH3025_2016] Tratamento: Para CST 01, 02, 03, 04, 05, 06, 07, 08 e 09 trazer a informação com dois dígitos para o relatório, ou seja, quando vier com uma posição, preencher com zero à esquerda. | Código da situação tributária do PIS: Se item da SAFX08  campo 175-Código Situação Tributária PIS;  Se item da SAFX09  campo 68-Código de Situação Tributária PIS;  Notas sem itens  campo “249-Código Situação Tributária PIS” da SAFX07;  [ALTERADA – CH3025_2016] Tratamento: Para CST 01, 02, 03, 04, 05, 06, 07, 08 e 09 trazer a informação com dois dígitos para o relatório, ou seja, quando vier com uma posição, preencher com zero à esquerda. |
| PIS – Base | Valor da base PIS: Se item da SAFX08  campo 86-Base PIS;  Se item da SAFX09  campo 46-Base de Cálculo PIS;  Notas sem itens  campo “102-Base PIS” da SAFX07; | Valor da base PIS: Se item da SAFX08  campo 86-Base PIS;  Se item da SAFX09  campo 46-Base de Cálculo PIS;  Notas sem itens  campo “102-Base PIS” da SAFX07; |
| PIS – Valor | Valor do PIS: Se item da SAFX08  campo 87-Valor PIS;  Se item da SAFX09  campo 48-Valor Tributo PIS;  Notas sem itens  campo “103-Valor PIS” da SAFX07; | Valor do PIS: Se item da SAFX08  campo 87-Valor PIS;  Se item da SAFX09  campo 48-Valor Tributo PIS;  Notas sem itens  campo “103-Valor PIS” da SAFX07; |
| PIS - Aliq | Alíquota do PIS: Se item da SAFX08  campo 129-Valor Alíquota PIS;  Se item da SAFX09  campo 47-Alíquota do PIS;  Notas sem itens  campo “164-Valor Alíquota PIS” da SAFX07; | Alíquota do PIS: Se item da SAFX08  campo 129-Valor Alíquota PIS;  Se item da SAFX09  campo 47-Alíquota do PIS;  Notas sem itens  campo “164-Valor Alíquota PIS” da SAFX07; |
| COFINS - CST | Código da situação tributária da COFINS: Se item da SAFX08  campo 178-Código Situação Tributária COFINS;  Se item da SAFX09  campo 69-Código de Situação Tributária COFINS;  Notas sem itens  campo “250-Código Situação Tributária COFINS” da SAFX07;  [ALTERADA – CH3025_2016] Tratamento: Para CST 01, 02, 03, 04, 05, 06, 07, 08 e 09 trazer a informação com dois dígitos para o relatório, ou seja, quando vier com uma posição, preencher com zero à esquerda. | Código da situação tributária da COFINS: Se item da SAFX08  campo 178-Código Situação Tributária COFINS;  Se item da SAFX09  campo 69-Código de Situação Tributária COFINS;  Notas sem itens  campo “250-Código Situação Tributária COFINS” da SAFX07;  [ALTERADA – CH3025_2016] Tratamento: Para CST 01, 02, 03, 04, 05, 06, 07, 08 e 09 trazer a informação com dois dígitos para o relatório, ou seja, quando vier com uma posição, preencher com zero à esquerda. |
| COFINS – Base | Valor da base COFINS: Se item da SAFX08  campo 88-Base COFINS;  Se item da SAFX09  campo 49-Base de Cálculo COFINS;  Notas sem itens  campo “104-Base COFINS” da SAFX07; | Valor da base COFINS: Se item da SAFX08  campo 88-Base COFINS;  Se item da SAFX09  campo 49-Base de Cálculo COFINS;  Notas sem itens  campo “104-Base COFINS” da SAFX07; |
| COFINS - Valor | Valor da COFINS: Se item da SAFX08  campo 89-Valor COFINS;  Se item da SAFX09  campo 51-Valor Tributo COFINS;  Notas sem itens  campo “105-Valor COFINS” da SAFX07; | Valor da COFINS: Se item da SAFX08  campo 89-Valor COFINS;  Se item da SAFX09  campo 51-Valor Tributo COFINS;  Notas sem itens  campo “105-Valor COFINS” da SAFX07; |
| COFINS – Aliq | Alíquota da COFINS: Se item da SAFX08  campo 130-Valor Alíquota COFINS;  Se item da SAFX09  campo 50-Alíquota da COFINS; Notas sem itens  campo “165-Valor Alíquota COFINS” da SAFX07; | Alíquota da COFINS: Se item da SAFX08  campo 130-Valor Alíquota COFINS;  Se item da SAFX09  campo 50-Alíquota da COFINS; Notas sem itens  campo “165-Valor Alíquota COFINS” da SAFX07; |


---

| Totais (Entradas) | Ao finalizar as notas de entradas do estabelecimento, será gerada uma linha com a totalização das colunas “Valor Contábil” e “Base” e “Valor” de cada um dos quatro tributos (ICMS, IPI, PIS e COFINS). |
| --- | --- |
| Totais (Saídas) | Ao finalizar as notas de saídas do estabelecimento, será gerada uma linha com a totalização das colunas “Valor Contábil” e “Base” e “Valor” de cada um dos quatro tributos (ICMS, IPI, PIS e COFINS). |
