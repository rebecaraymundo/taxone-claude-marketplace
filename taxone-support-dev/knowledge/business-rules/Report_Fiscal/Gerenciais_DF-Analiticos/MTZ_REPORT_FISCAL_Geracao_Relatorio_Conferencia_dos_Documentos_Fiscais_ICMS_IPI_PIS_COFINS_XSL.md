---
source: "MTZ_REPORT_FISCAL_Geracao_Relatorio_Conferencia_dos_Documentos_Fiscais_ICMS_IPI_PIS_COFINS_XSL.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Básicos – Report Fiscal
Conferência dos Documentos Fiscais (ICMS/IPI/PIS/COFINS) – Formato XLS



DOCUMENTO DE REQUISITO






REGRAS DE NEGÓCIO








Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4808 | Julyana Perrucini | Este documento tem como objetivo alterar o preenchimento da coluna Descrição de acordo com o parâmetro "Exibir Código Produto/Serviço”. |
| MFS-40265 | Alessandra Cristina Navatta | Inclusão da coluna ‘Data de Lancamento PIS/COFINS’ no relatório formato XLS. |
| MFS548165 | Aline Melo | Inclusão de novos campos no relatório da SAFX325 (ICMS Monofásico). |


---

|  |  |
| --- | --- |



---

| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra geral do relatório  Origem: SAFX07/ SAFX08/ SAFX09/SAFX325  Trazer as informações de documentos fiscais de mercadoria e serviço de acordo com o período, movimento e estabelecimento preenchidos na tela de geração. Deve recuperar também informações referente ao ICMS Monofásico. | <OS>. MFS548165 |
| RN01 | Campos da TELA    [ALTERADA – OS4808] Quando o parâmetro “Exibir Código Produto/Serviço” estiver desmarcado na tela de geração do relatório: Preencher com a informação do campo 21-Descrição Complementar da SAFX08 e do campo 16-Descrição Complementar da SAFX09. Quando o parâmetro “Exibir Código Produto/Serviço” estiver marcado na tela de geração do relatório: Preencher com a informação do campo 01-Indicador do Produto + 02-Código do Produto da SAFX2013 e do campo 01-Código do Tipo de Serviço da SAFX2018 de acordo com o produto e serviço vinculado ao item do documento fiscal. | OS4808 |
| RN02 | Incluir a coluna ‘Data de Lancamento PIS/COFINS’, após a coluna ‘Data Fiscal’, no relatório.  Recuperar esta informação do campo DAT_LANC_PIS_COFINS (campo 196 da SAFX08 ou campo 81 da SAFX09). | MFS-40265 |
| RN03 | Inclusão das colunas referentes a Informações de ICMS Monofásico:  Campo Aliq. Ad Rem ICMS Proprio - Recuperar campo ALIQ_AD_REM_ICMS da SAFX325. Campo Valor ICMS Mono Proprio - Recuperar campo VLR_ICMS_MONO da SAFX325. Campo Aliq. Ad Rem ICMS Retencao - Recuperar do campo SAFX325. Campo Valor ICMS Mono Retencao - Recuperar campo ALIQ_AD_REM_ICMS_RETEN da SAFX325. Campo Valor ICMS Mono Operacao - Recuperar campo VLR_ICMS_MONO_OP da SAFX325. Campo Valor ICMS Mono Diferido - Recuperar campo VLR_ICMS_MONO_DIF da SAFX325. Campo Aliq. Ad Rem ICMS Retido - Recuperar campo ALIQ_AD_REM_ICMS_RET da SAFX325. Valor ICMS Mono Retido - Recuperar campo VLR_ICMS_MONO_RET da SAFX325 | MFS548165 |
|  |  |  |
|  |  |  |
|  |  |  |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

