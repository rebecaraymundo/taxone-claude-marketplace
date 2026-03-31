# MTZ_REPORT_FISCAL_Geracao_Relatorio_Conferencia_dos_Documentos_Fiscais_ICMS_IPI_PIS_COFINS_XSL

- **Fonte:** MTZ_REPORT_FISCAL_Geracao_Relatorio_Conferencia_dos_Documentos_Fiscais_ICMS_IPI_PIS_COFINS_XSL.docx
- **Modificado:** 2025-11-03
- **Tamanho:** 62 KB

---

THOMSON REUTERS

Básicos – Report Fiscal

Conferência dos Documentos Fiscais \(ICMS/IPI/PIS/COFINS\) – Formato XLS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4808

Julyana Perrucini

Este documento tem como objetivo alterar o preenchimento da coluna Descrição de acordo com o parâmetro "Exibir Código Produto/Serviço”\.

MFS\-40265

Alessandra Cristina Navatta

Inclusão da coluna ‘Data de Lancamento PIS/COFINS’ no relatório formato XLS\.

MFS548165

Aline Melo

Inclusão de novos campos no relatório da SAFX325 \(ICMS Monofásico\)\.

####  

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

Regra geral do relatório

__Origem:__ SAFX07/ SAFX08/ SAFX09/SAFX325

Trazer as informações de documentos fiscais de mercadoria e serviço de acordo com o período, movimento e estabelecimento preenchidos na tela de geração\. Deve recuperar também informações referente ao ICMS Monofásico\.

<OS>\.

MFS548165

RN01

__Campos da TELA __

__\[ALTERADA – OS4808\]__

__Quando o parâmetro “Exibir Código Produto/Serviço” estiver desmarcado na tela de geração do relatório:__

Preencher com a informação do campo 21\-Descrição Complementar da SAFX08 e do campo 16\-Descrição Complementar da SAFX09\.

__Quando o parâmetro “Exibir Código Produto/Serviço” estiver marcado na tela de geração do relatório:__

Preencher com a informação do campo 01\-Indicador do Produto \+ 02\-Código do Produto da SAFX2013 e do campo 01\-Código do Tipo de Serviço da SAFX2018 de acordo com o produto e serviço vinculado ao item do documento fiscal\.

OS4808

RN02

Incluir a coluna ‘Data de Lancamento PIS/COFINS’, após a coluna ‘Data Fiscal’, no relatório\. 

Recuperar esta informação do campo DAT\_LANC\_PIS\_COFINS \(campo 196 da SAFX08 ou campo 81 da SAFX09\)\.

MFS\-40265

RN03

Inclusão das colunas referentes a Informações de ICMS Monofásico:

Campo Aliq\. Ad Rem ICMS Proprio \- Recuperar campo ALIQ\_AD\_REM\_ICMS da SAFX325\.

Campo Valor ICMS Mono Proprio \- Recuperar campo VLR\_ICMS\_MONO da SAFX325\.

Campo Aliq\. Ad Rem ICMS Retencao \- Recuperar do campo SAFX325\.

Campo Valor ICMS Mono Retencao \- Recuperar campo ALIQ\_AD\_REM\_ICMS\_RETEN da SAFX325\.

Campo Valor ICMS Mono Operacao \- Recuperar campo VLR\_ICMS\_MONO\_OP da SAFX325\.

Campo Valor ICMS Mono Diferido \- Recuperar campo VLR\_ICMS\_MONO\_DIF da SAFX325\.

Campo Aliq\. Ad Rem ICMS Retido \- Recuperar campo ALIQ\_AD\_REM\_ICMS\_RET da SAFX325\.

Valor ICMS Mono Retido \- Recuperar campo VLR\_ICMS\_MONO\_RET da SAFX325

MFS548165

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

