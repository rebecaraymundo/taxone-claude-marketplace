---
source: "MTZ-Report_Fiscal-ICMS_e_ICMSS_NAO_ESCRITURADOS.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Relatório Analítico de Mercadorias - ICMS / ICMS-S Não Escriturados


Report Fiscal => Gerencial =>Documento Fiscal => Analíticos > Mercadoria - ICMS/ICMS-S não Escriturado


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3296
Criação de Relatório - ICMS Não Escriturado e ICMS-S Não escriturado 
Geração de um novo relatório onde sejam descriminados os documentos fiscais de mercadoria que possuem valores de "ICMS Não escriturado" e "ICMS-S Não escriturado".

OS3506
DW - REPORT FISCAL - GERENCIAIS - Documento Fiscal - Analítico - Mercadoria - ICMS/ICMS - ST Não Escriturado
O objetivo deste requisito é permitir a geração do relatório de ICMS/ICMS-ST Não Escriturado para os itens da nota fiscal que tenham os campos Valor do ICMS-S e Base do ICMS-S preenchidos.

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Critérios para a recuperação dos dados:

Para a geração deste relatório serão filtrados os documentos fiscais e itens de mercadorias que possuírem valores de ICMS Não escriturados e ICMS-S Não escriturados.

- Origem dos dados: Tabelas dos documentos fiscais de mercadorias e itens (SAFX07 e SAFX08)

- Somente se o documento possuir item.

- Somente itens que possuem os campos VLR_ICMS_NDESTAC (Item 80 da SAFX08) ou  VLR_ICMSS_NDESTAC  (Item 133 da SAFX08) ou VLR_ICMSS_N_ESCRIT (item 145 da SAFX08) > 0.

- Considerar notas fiscais canceladas  (Se SITUACAO = S), item 30 da SAFX07

- Considerar notas fiscais conjugadas (Se COD_CLASS_DOC_FIS = 3), item 12 da SAFX07.


OS3296
RN01
Critérios para a recuperação dos dados conforme parametrização da tela:

Se o parâmetro "Número do processo" estiver selecionado, buscar pelo campo NUM_PROCESSO da X07_DOCTO_FISCAL
Se o parâmetro "Período/Pessoa física ou jurídica" estiver selecionado, buscar os seguintes campos:

       Período inicial e final deve estar entre o período da DATA_FISCAL da SAFX07.
       Movimento deve buscar o campo MOVTO_E_S (Item 03 da SAFX07), onde:
                    Quando selecionado "Entrada" deve ser igual á "1" ou "2" ou "3" ou "4" ou "5".
                    Quando selecionado "Saída" deve ser igual á "9".
                    Quando selecionado "Ambos", buscar todos.

        Pessoa Fís/Jur deve buscar o indicador através do campo IDENT_FIS_JUR (Item 06 da SAFX07) onde:
                     1-  Fornecedor;
                     2 - Cliente;
                     3 - Estabelecimento;
                     4 - Transportadora;
                     5 - Cliente/Fornecedor/Transportadora.

          Pessoa Fís/Jur deve buscar o código através do campo COD_FIS_JUR (item 07 da SAFX07).

Após o preenchimento da pessoa física/jurídica, o sistema deve preencher automaticamente os campos abaixo com as seguintes informações:
Data de validade do grupo da pessoa física/jurídica
Nome do grupo da pessoa física/jurídica
Razão social da pessoa física/jurídica --> SAFX04: RAZAO_SOCIAL (Item 05)

OS3296
RN02
Layout do Relatório

 O layout do relatório deverá ser similar ao relatório "Analítico de Mercadorias - IPI Não Escriturado", onde deve possuir cabeçalho conforme os padrões de relatórios da Mastersaf e deverão apresentados os valores dos seguintes campos do documento: 

Número do documento --> SAFX07 --> NUM_DOCFIS (Item 08)
Tipo Docto --> SAFX07 --> COD_DOCTO (item 05)
 Série/Subsérie --> SAFX07 --> SERIE_DOCFIS (Item 09) / SUB_SERIE_DOCFIS (Item 10)
Data Emissão, --> SAFX07 --> DATA_EMISSAO (Item 11)
Data Fiscal --> SAFX08 --> DATA_FISCAL (Item 03)
Pessoa Física/Jurídica --> SAFX07 --> COD_FIS_JUR (Item 07)
CFOP --> SAFX08 --> COD_CFO (Item 22)
UF --> SAFX04 --> UF (Item 19) --> UF da Pessoa Física/Jurídica do documento.
Valor Total --> SAFX08 --> VLR_CONTAB_ITEM (Item 64)
Base ICMS --> SAFX08 --> BASE_ICMS (Item 56)
Valor ICMS --> SAFX08 --> VLR_ICMS (Item 43)
Valor ICMS Não escriturado --> SAFX08 --> VLR_ICMS_NDESTAC (Item 80)
Base ICMS-S --> SAFX08 --> BASE_SUB_TRIB_ICMS (Item 61)
Valor ICMS-S --> SAFX08 --> VLR_SUBST_ICMS (Item 52)
Valor ICMS-S Não escriturado --> SAFX08 --> VLR_ICMSS_NDESTAC (Item 133)
Valor ICMS-S Não escriturado (Port. ICMS 49/2004) --> SAFX08 --> VLR_ICMSS_N_ESCRIT (Item 145)

- Os dados devem ser agrupados e totalizados por entradas e saídas para cada dia.

- A ordenação dos dados será por data, seguindo o critério de ordem crescente.

- Ao final haverá uma totalização das entradas do estabelecimento e outra totalização das saídas do estabelecimento referente ao período do relatório.

OS3296
RN03
Campo Gerar Itens com Base ICMS-S e Valor ICMS-S preenchidos da tela de critério de seleção

Esse campo deve ser um checkbox, com as seguintes opções: "S" - Marcado e "N" - Desmarcado (opção default).
OS3506
RN04
Regra p/ Campo Gerar Itens com Base ICMS-S e Valor ICMS-S preenchidos

Esse parâmetro tem referência com a recuperação dos valores de acordo com o layout da RN02.

Se o campo "Gerar Itens com Base ICMS-S e Valor ICMS-S preenchidos" estiver marcado, considerar os valores p/ layout quando:
- Itens da Nota Fiscal que possua pelo menos um dos campos de ICMS Não Escriturado (VLR_ICMS_NDESTAC (Item 80 da SAFX08) ou VLR_ICMSS_NDESTAC (Item 133 da SAFX08) ou VLR_ICMSS_N_ESCRIT (item 145 da SAFX08) > 0) preenchidos;
- Itens da Nota Fiscal que possua valor tributado de ICMS-ST (VLR_SUBST_ICMS (item 52 da SAFX08) > 0) preenchidos.

Se o campo "Gerar Itens com Base ICMS-S e Valor ICMS-S preenchidos" não estiver marcado, considerar os valores p/ layout quando:
- Somente os itens da Nota Fiscal que possua pelo menos um dos campos de ICMS Não Escriturado (VLR_ICMS_NDESTAC (Item 80 da SAFX08) ou VLR_ICMSS_NDESTAC (Item 133 da SAFX08) ou VLR_ICMSS_N_ESCRIT (item 145 da SAFX08) > 0) preenchidos (como é feito atualmente), ou seja, não serão gerados os valores dos campos Base ICMS-S e Valor ICMS-S.

OS3506


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

