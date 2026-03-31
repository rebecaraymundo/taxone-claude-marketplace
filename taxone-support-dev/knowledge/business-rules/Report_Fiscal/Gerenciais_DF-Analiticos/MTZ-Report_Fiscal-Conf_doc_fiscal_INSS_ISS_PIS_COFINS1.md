---
source: "MTZ-Report_Fiscal-Conf_doc_fiscal_INSS_ISS_PIS_COFINS1.docx"
category: Report_Fiscal
converted: auto
---

# Report Fiscal – Conferência de Documentos Fiscais (INSS/ISS/PIS/COFINS)

**Localização:**
Módulo: Básicos à Report Fiscal
DW: Menu: Gerenciais à Documentos Fiscais  à Analíticos à Conferência de Documentos Fiscais (INSS/ISS/PIS/COFINS) – Formato XLS
TAXONE: :Menu: Gerenciais à Documentos Fiscais  à Analíticos à Conferência de Documentos Fiscais (INSS/ISS/PIS/COFINS)




# DOCUMENTO DE REQUISITO



# REGRAS DE NEGÓCIO






Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| DR | Nome | Descrição |
| --- | --- | --- |
| MFS34022 | Andréa Rocha | Geração de um relatório onde sejam descriminados os documentos fiscais de serviços. |
| MFS36193 | Andréa Rocha | Inclusão de 3 novas colunas no relatório. |
| MFS37436 | Andréa Rocha | Inclusão de 2 novas colunas no relatório. |
| MFS70395 | Alessandra Cristina Navatta | Incluir parâmetros na tela de geração para considerar notas canceladas e tipo de  tributo.  Criar regra para exibir os campos de valores de acordo com o tributo selecionado em tela e considerar no filtro de recuperação dos dados, notas canceladas se o parâmetro Considerar Notas Canceladas estiver marcado.  Inclusão das colunas: Situação da Nota, Código do Serviço Lei 116/03, Descrição Serviço e Descrição Serviço Lei 116/03 |
| MFS565387 | Andréa Rocha | Inclusão de um novo parâmetro para demonstrar as notas fiscais sem escrituração no relatório. |
| MFS-633546/MFS-647617 | Alessandra Cristina Navatta | Apenas para o produto TAXONE:  Migração do relatório para o Servidor de Relatórios.  Criação da Tela de Geração e Emissão Devido a migração, ajustamos o nome do relatório de Conferência de Documentos Fiscais (INSS/ISS/PIS/COFINS) - Formato XLS para: Conferência de Documentos Fiscais (INSS/ISS/PIS/COFINS). Disponibilizado o layout em PDF. O Layout em excel, não foi alterado.  Produto DW e TAXONE Retiramos o filtro de Tributo da tela  As mensagens de validação de preenchimento dos campos Data Inicial e Data Final foram retiradas do log. Elas passam a ser exibidas em tela.  A validação de data final menor que a data inicial se manteve no log. Inclusão da coluna classificação do documento no relatório formato XLS |
| MFS-713089 | Rosemeire Santos | Inclusão de coluna e Campo COD_ATIV_RJ, nos formatos PDF e EXCEL. |
| MFS-800883 | Rosemeire Santos | Inclusão de coluna e Campo DOCNUM, na geração do relatório nos formatos PDF e EXCEL. |
| MFS-1028394 | Lyene Benvenutti | Alteração na regra para considerar o código “I” (Internacional/Invoice - proveniente do campo 12 da SAFX07) na geração do relatório quando o parâmetro “Considerar notas fiscais de serviço não escrituradas” estiver marcado. |


---

|  | Telas   DW     TAXONE   Geração   Mesma tela apresentada no DW .   Emissão |  |
| --- | --- | --- |
| RN | Regras | MFS |
| RN01 | Parâmetros de tela:  - Data Inicial: informar uma data válida (Formato: DD/MM/AAAA). Campo obrigatório. Caso não preenchida, exibir a mensagem (em tela): “Informe Data Inicial”   - Data Final: informar uma data válida (Formato: DD/MM/AAAA). Campo obrigatório. Caso não preenchida, exibir a mensagem (em tela): “Informe Data Final”. A data inicial deve ser menor que a data inicial, caso contrário, exibir a mensagem no LOG: “Data Inicial deve ser inferior a Data Final”.    - Movimento: Campo do tipo checkbox, com as opções:                         - Entrada                        - Saída                         - Entrada e Saída  [MFS70395 ALTERAÇÃO] - Considerar notas Canceladas (check box, com a opção default desmarcada)   [MFS565387 ALTERAÇÃO] - Considerar Notas Fiscais de Serviço não escrituradas (checkbox, com a opção default desmarcada)   [MFS647617 ALTERAÇÃO] - Remover filtro Tributo [MFS70395 ALTERAÇÃO] - -Tributo: Apresentar em cada opção um check-box (por default, todos os tributos estarão marcados)  - INSS - IR - ISS - PIS -COFINS  Obs. Ao executar, se nenhum tributo estiver marcado, o sistema automaticamente, considerará a opção ISS marcada. Obs. Ao executar, se nenhum tributo estiver marcado, exibir mensagem no log: “Informe pelo menos um tipo de tributo.”  - UF: campo do tipo Listbox, lista dos estados cadastrados na tabela Estado, com a opção “Todos”.  - Estabelecimento: Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  Serão mostrados os estabelecimentos conforme a seleção da UF, quando for selecionada a opção “Todos”, serão mostrados todos os estabelecimentos. Incluir botão “Selecionar” para seleção de estabelecimento e o botão “Marcar Todos” caso o usuário queira marcar todos os estabelecimentos. | MFS34022 MFS70395 MFS565387 MFS-633546/647617 |
| RN01.01 | Apena para Produto TAXONE – (Server Report)   Tela de Emissão  Campos:  Período de Execução da Geração:  Tipo Data Formato DD/MM/AAAA DD/MM/AAAA  Tipo de Geração:  Tipo Lista  Opções válidas: Arquivo PDF Excel – XLSX  Default: Arquivo PDF  Selecionar Todos:   Tipo ckeck-box default desmarcado | MFS-633546/MFS-647617 |
| RN02 | Regra geral - Critérios para a recuperação dos dados:   Para a geração deste relatório serão recuperados os documentos fiscais de serviços, capa e item de serviço.    Origem dos dados: Tabelas de documentos fiscais de Serviços (SAFX07 e SAFX09):   - Empresa igual a empresa selecionada na geração;   - Estabelecimento igual ao estabelecimento selecionado na geração;   - A data fiscal da nota deve ser referente ao período informado em tela (>= data inicial e <= data final);   [MFS565387 ALTERAÇÃO] Inclusão das notas de serviço não escrituradas [MFS-1028394 ALTERAÇÃO] Inclusão do código “I” (Internacional/Invoice)   Se parâmetro “Considerar Notas Fiscais de Serviço não escrituradas” estiver desmarcado      Considerar as notas de Classificação fiscal 2 e 3 (nota fiscal de serviço e nota fiscal mista, campo 12-      COD_CLASS_DOC_FIS = 2, 3 da tabela SAFX07); Senão       Considerar as notas de Classificação fiscal 2, 3, 8, 9 e I (nota fiscal de serviço, nota fiscal mista, notas não escrituradas e Internacional/Invoice,                 campo 12-COD_CLASS_DOC_FIS = 2, 3, 8, 9, I da tabela SAFX07);   - Selecionar o Tipo de Movimento conforme o parâmetro de tela:        - Entrada: campo 03 da SAFX07 (MOVTO_E_S <> “9”);        - Saída: campo 03 da SAFX07 (MOVTO_E_S = “9”);         - Entrada e Saída: recuperar todos os movimentos;   [MFS70395 – ALTERAÇÃO] - Não considerar notas fiscais canceladas (campo 30-SITUACAO = S da tabela SAFX07), se o parâmetro ‘Considerar Notas Canceladas’ estiver desmarcado. Caso o parâmetro esteja marcado, as notas canceladas e as normais (campo 30-SITUACAO = S ou N da tabela SAFX07), devem ser consideradas e exibidas no relatório.   Ordenação do relatório: empresa, estabelecimento, número do documento fiscal, tipo de documento, série, subsérie, tipo de movimento, data emissão, data fiscal, CPF_CGC (pessoa física/jurídica), código do serviço. | MFS34022 MFS70395 MFS565387 MFS-1028394 |
| RN03 | Layout do Relatório    O relatório não terá opção de impressão, ele somente terá a opção de salvar em excel.  Os campos abaixo serão mostrados no excel: | MFS34022 MFS-800883 MFS-1028394 |


---

| Empresa | Empresa da geração |
| --- | --- |
| Estabelecimento | Estabelecimento da geração |
| CPF_CGC do estabelecimento | CPF_CGC da tabela Estabelecimento |
| Razão social do estabelecimento | Razão social da tabela Estabelecimento |
| Tipo de Movimento | Movimento Entrada/Saída (campo 03 da SAFX07) |
| Situação da Nota | [MFS70395 – ALTERAÇÃO] -Situação da Nota (campo 30 da SAFX07] |
| Tipo de documento | Tipo de documento (campo 03 da SAFX07) |
| Classificação do documento | [ALTERAÇÃO MFS-633546/MFS-647617/ MFS-1028394] Classificação do documento (campo 12-COD_CLASS_DOC_FIS da SAFX07)   Apresentar as seguintes nomenclaturas:   2-Serviços  3-Merc/Serv  8- NF Serv n escr  9- Out Doctos n escr I- Doctos Inter/Invoice   As demais opções não estão sendo consideradas no relatório. |
| DocNum | Inclusão do Campo DOCNUM - (Campo 69 - NUM_CONTROLE_DOCTO da SAFX07) |
| Número da NF | Número do Documento Fiscal (campo 08 da SAFX07) |
| Série da NF | Série do Documento Fiscal (campo 09 da SAFX07) |
| Subsérie da NF | Subsérie do Documento Fiscal (campo 10 da SAFX07) |
| Data Emissão | Data de emissão (campo 11 da SAFX07) |
| Data Fiscal | Data fiscal |
| Data Pagamento | Data de Pagamento da Nota Fiscal (campo 175 da SAFX07) |
| Ind./Código Pessoa Fis/Jur | Indicador e Código da Pessoa Física/Jurídica (campos 01 e 02 da SAFX04) [MFS37436] Alteração |
| CPF_CGC Pessoa Fis/Jur | CPF_CGC (campo 06 da SAFX04) |
| Razão social da Pessoa Fis/Jur | Razão Social (campo 06 da SAFX04) |
| UF da Pessoa Fis/Jur | UF (campo 06 da SAFX04) |
| Município da Pessoa Fis/Jur | Município (campo 06 da SAFX04) |
| Item | Número do item (campo 13 da SAFX09) |
| Código do serviço | Código do serviço (campo 12 da SAFX09) |
| Descrição Serviço | [MFS70395 – ALTERAÇÃO] Descrição (campo 03 da SAFX2018) |
| Código do Serviço Lei 116/03 | [MFS70395 – ALTERAÇÃO] - Código da lei complementar (campo 20 da SAFX2018) |
| Descrição Serviço Lei 116/03 | [MFS70395 – ALTERAÇÃO] - Descrição (campo da dwt_servico_lei_116) |
| Valor total do serviço | Valor total do serviço (campo 15 da SAFX09 ou campo 22 da safx07) |
| Base INSS | Valor base INSS (campo 76 da SAFX09 ou campo 85 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘INSS’ estiver selecionado |
| Alíquota INSS | Valor Alíquota INSS (campo 78 da SAFX09 ou campo 86 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘INSS’ estiver selecionado |
| Valor INSS Retido | Valor INSS Retido (campo 77 da SAFX09 ou campo 87 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘INSS’ estiver selecionado |
| Base ISS | Valor base ISS (campo 39 da SAFX09 ou campo 61 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘ISS’ estiver selecionado |
| Alíquota ISS | Valor Alíquota ISS (campo 32 da SAFX09 ou campo 45 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘ISS’ estiver selecionado |
| Valor ISS | Valor ISS (campo 33 da SAFX09 ou campo 46 da safx07)  [MFS36193] Alteração [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘ISS’ estiver selecionado |
| Base ISS Retido | Base ISS Retido (campo 57 da SAFX09 ou campo 188 da safx07)  [MFS36193] Alteração [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘ISS’ estiver selecionado |
| Valor ISS Retido | Valor ISS Retido (campo 58 da SAFX09 ou campo 189 da safx07)  [MFS36193] Alteração [MFS-70395  - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘ISS’ estiver selecionado |
| Base IR | Base IR (campo 37 da SAFX09 ou campo 59 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘IR’ estiver selecionado |
| Alíquota IR | Alíquota IR (campo 30 da SAFX09 ou campo 43 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘IR’ estiver selecionado |
| Valor IR | Valor IR (campo 31 da SAFX09 ou campo 44 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘IR’ estiver selecionado |
| Código da situação PIS | Valor base INSS (campo 68 da SAFX09 ou campo 249 da safx07)  [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘PIS’ estiver selecionado |
| Base PIS | Base de Cálculo PIS (campo 46 da SAFX09 ou campo 102 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘PIS’ estiver selecionado |
| Alíquota PIS | Alíquota PIS (campo 47 da SAFX09 ou campo 164 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘PIS’ estiver selecionado |
| Valor PIS | Valor Tributo PIS (campo 48 da SAFX09 ou campo 103 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘PIS’ estiver selecionado |
| Código da situação COFINS | Valor base COFINS (campo 69 da SAFX09 ou campo 250 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘COFINS’ estiver selecionado |
| Base COFINS | Base de Cálculo COFINS (campo 49 da SAFX09 ou campo 104 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘COFINS’ estiver selecionado |
| Alíquota COFINS | Alíquota COFINS (campo 50 da SAFX09 ou campo 165 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘COFINS’ estiver selecionado |
| Valor COFINS | Valor Tributo COFINS (campo 51 da SAFX09 ou campo 105 da safx07) [MFS-70395 - ALTERAÇÃO] - Apresentar esse campo se o parâmetro de tributo ‘COFINS’ estiver selecionado |
| COD_ATIV_RJ | [MFS-713089 - INCLUSÂO] – Incluir o campo 113 oriundo da SAFX09, este código será utilizado para a geração da obrigação municipal de Niterói, para o preenchimento do campo Código do Serviço Municipal. |


---

| RN04 | Layout do Relatório (PDF) – Apenas TAXONE (Server Report)    As colunas abaixo devem constar no formato PDF:   Data da Geração Empresa Estabelecimento Tipo de Movimento Situação da Nota Tipo de documento Classificação do documento DocNum Número da NF Série da NF Subsérie da NF Data Emissão Data Fiscal Data Pagamento Razão social da Pessoa Fis/Jur UF da Pessoa Fis/Jur Município da Pessoa Fis/Jur Código Atividade RJ Item Código do serviço Código do Serviço Lei 116/03 Base INSS Alíquota INSS Valor INSS Retido Base ISS Alíquota ISS Valor ISS  Base ISS Retido Alíquota ISS Retido  Valor ISS Retido Base IR Alíquota IR Valor IR Base PIS Alíquota PIS Valor PIS Base COFINS Alíquota COFINS Valor COFINS    Layout PDF (considerando os labels e agrupamentos indicado abaixo): | MFS-633546/MFS-647617 MFS-713089 MFS-800883 |
| --- | --- | --- |



---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

