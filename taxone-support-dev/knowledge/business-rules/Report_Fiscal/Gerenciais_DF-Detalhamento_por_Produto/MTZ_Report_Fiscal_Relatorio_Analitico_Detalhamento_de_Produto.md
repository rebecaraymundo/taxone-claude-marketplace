---
source: "MTZ_Report_Fiscal_Relatorio_Analitico_Detalhamento_de_Produto.docx"
category: Report_Fiscal
converted: auto
---

**Relatório Detalhamento por Produto.**

Localização: Menu Básicos, Módulo Report Fiscal, Gerenciais, Documentos Fiscais, Analíticos, Detalhamento por Produto

**DOCUMENTO DE REQUISITO**


**REGRAS DE NEGÓCIO**


Considerações deste modelo:
**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**
**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| DR | Nome | Descrição |
| --- | --- | --- |
| OS4073 | Jefferson Mota | Criação do relatório Analítico e definição das regras para geração. |
| CH1414_2014 | Julyana Perrucini | Inclusão de campo Valor Desconto no relatório. |
| CH13715_2015 | Julyana Perrucini | Inclusão de campos: Base IPI, Alíquota IPI e Valor IPI; no relatório. |
| MFS_3582 | Eric Celestrino | Inclusão de campos: Valor FCP UF Destino, Valor ICMS UF Destino e Valor ICMS UF Origem. |
| MFS_4310 | João Henrique | Inclusão de campos: IPI Isentas, IPI Outras e Base ICMSS. Revisão da Regra do Campo: Base IPI. |
| MFS_14922 | João Henrique | Inclusão do campo de Código de Tributação IPI no relatório. |
| MFS-71662 | Rogério Ohashi | Inclusão dos campos Valor Base INSS, Valor Alíquota INSS e Valor de INSS Retido no relatório. |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Regra de Seleção: Este relatório será gerado com base nas informações das tabelas SAFX04, SAFX07, SAFX08 e SAFX2013, considerando os parâmetros de, período, CFOP e estabelecimento parametrizados na tela de emissão do relatório.  Serão considerados os registros das tabelas SAFX07 e SAFX08, cuja Data Fiscal compreenda o período parametrizado, considerando apenas os registros do estabelecimento (ou estabelecimento) indicado e que tenham os mesmos códigos de CFOP parametrizados com correspondência no item. As notas fiscais canceladas e notas fiscais sem itens, não serão consideradas.  Serão consideradas todas as classificações de documento fiscal, referente ao campo 12-COD_CLASS_DOC_FIS da SAFX07.   Como a quantidade de colunas é muito grande, ele será apenas disponibilizado em tela, com a possibilidade de visualizar todas as colunas, e poderá também ser salvo no formato Excel e texto.  Ordenação do relatório: Data Fiscal, N° NF, Série e Sub-Série. | OS4073 |
| RN01 | Regra para hierarquia do Menu:  Deverá ser criado o seguinte sub-menu no módulo Report Fiscal:  Gerenciais Documentos Fiscais        Analíticos       Detalhamento por Produto | OS4073 |
| Cabeçalho | Cabeçalho | Cabeçalho |
| RN02 | Empresa: Por default, deve apresentar a empresa que está conectada no manager. | OS4073 |
| RN03 | Código do Estabelecimento: Corresponde ao estabelecimento selecionado na tela de geração do Relatório Analítico. | OS4073 |
| RN04 | Razão Social: Corresponde ao campo RAZAO_SOCIAL da tabela ESTABELECIMENTO. | OS4073 |
| RN05 | Período de Geração do Relatório: Corresponde ao período incial e ao período final, informados na tela de geração do relátório analítico. Exemplo: Período: dd/mm/aaaa à dd/mm/aaaa | OS4073 |
| RN06 | CNPJ: Corresponde ao campo CNPJ da tabela ESTABELECIMENTO. | OS4073 |
| RN07 | Data e Horário de Geração do Relatório : Deverá inserir no relatório a data de geração seguida do horário atual, conforme exemplo abaixo: Data: dd/mm/aaaa 00:00:00hs | OS4073 |
| RN08 | Página: Corresponde ao número da página que esta sendo exibida para o usuário. | OS4073 |
| Dados Geral do Relatório | Dados Geral do Relatório | Dados Geral do Relatório |
| RN09 | Regra para inclusão da coluna N° NF: Deve ser incluída a coluna “N° NF” no relatório acima. Essa informação deve ser recuperada do campo 08 – NUM_DOCFIS, da SAFX07. | OS4073 |
| RN10 | Regra para inclusão da coluna Série/Subsérie: Deve ser incluída a coluna “Série/Subsérie” no relatório. Essa informação deve ser recuperada do campo 09 – SERIE_DOCFIS, seguido do campo 10 – SUB_SERIE_DOCFIS, da SAFX07.  Formatação: Série/Sub-série | OS4073 |
| RN11 | Regra para inclusão da coluna Data Fiscal: Deve ser incluída a coluna “Data Fiscal” no relatório. Essa informação deve ser recuperada do campo Data Fiscal da SAFX07. | OS4073 |
| RN12 | Regra para inclusão da coluna Data Emissão: Deve ser incluída a coluna “Data Emissão” no relatório. Essa informação deve ser recuperada do campo 11 – DATA_EMISSAO, da SAFX07. | OS4073 |
| RN13 | Regra para inclusão da coluna N° de Controle: Deve ser incluída a coluna “N° de Controle” no relatório. Essa informação deve ser recuperada do campo 69 – NUM_CONTROLE_DOCTO, da SAFX07. | OS4073 |
| RN14 | Regra para inclusão da coluna Mod. Documento: Deve ser incluída a coluna “Mod. Documento” no relatório.Essa informação deve ser recuperada do campo 13 – COD_MODELO, da SAFX07. | OS4073 |
| RN15 | Regra para inclusão da coluna Chave de acesso da NF-e: Deve ser incluída a coluna “Chave de acesso da NF-e” no relatório.Essa informação deve ser recuperada do campo 226 – NUM_AUTENTIC_NFE, da SAFX07. | OS4073 |
| RN16 | Regra para inclusão da coluna Código FIS/JUR: Deve ser incluída a coluna “Código FIS/JUR” no relatório. Essa informação deve ser recuperada do campo 06 – IDENT_FIS_JUR seguido do campo 07 – COD_FIS_JUR, da SAFX07. Separar a informação por um hífen. | OS4073 |
| RN17 | Regra para inclusão da coluna Código Razão Social: Deve ser incluída a coluna “Razão Social” no relatório. Essa informação deve ser recuperada do campo 05 – RAZAO_SOCIAL, da SAFX04. | OS4073 |
| RN18 | Regra para inclusão da coluna CPF/CNPJ: Deve ser incluída a coluna “CPF/CNPJ” no relatório. Essa informação deve ser recuperada do campo 06 – CPF_CGC, da SAFX04. | OS4073 |
| RN19 | Regra para inclusão da coluna Insc. Estadual: Deve ser incluída a coluna “Insc. Estadual” no relatório. Essa informação deve ser recuperada do campo 08 – INSC_ESTADUAL, da SAFX04. | OS4073 |
| RN20 | Regra para inclusão da coluna UF: Deve ser incluída a coluna “UF” no relatório. Essa informação deve ser recuperada do campo 19 – UF, da SAFX04. | OS4073 |
| RN21 | Regra para inclusão da coluna N° do Item: Deve ser incluída a coluna “N° do Item” no relatório. Essa informação deve ser recuperada do campo 18 – NUM_ITEM , da SAFX08. | OS4073 |
| RN22 | Regra para inclusão da coluna Código do Produto: Deve ser incluída a coluna “Código do Produto” no relatório. Essa informação deve ser recuperada do campo 13 – IND_PRODUTO seguido do campo 14 – COD_PRODUTO, da SAFX08. Separar a informação por um hífen. | OS4073 |
| RN23 | Regra para inclusão da coluna Descrição: Deve ser incluída a coluna “Descrição” no relatório. Essa informação deve ser recuperada do campo 04 – DESCRICAO, da SAFX2013 | OS4073 |
| RN24 | Regra para inclusão da coluna Descrição Complementar: Deve ser incluída a coluna “Descrição Complementar” no relatório. Essa informação deve ser recuperada do campo 21 – DESCRICAO_COMPL, da SAFX08. | OS4073 |
| RN25 | Regra para inclusão da coluna NCM: Deve ser incluída a coluna “NCM” no relatório. Essa informação deve ser recuperada do campo 26 – COD_NBM, da SAFX08. | OS4073 |
| RN26 | Regra para inclusão da coluna CFOP: Deve ser incluída a coluna “CFOP” no relatório. Essa informação deve ser recuperada do campo 22 – COD_CFO, da SAFX08. | OS4073 |
| RN27 | Regra para inclusão da coluna Nat. Operação: Deve ser incluída a coluna “Nat. Operação” no relatório. Essa informação deve ser recuperada do campo 23 – COD_NATUREZA_OP, da SAFX08. | OS4073 |
| RN28 | Regra para inclusão da coluna CST A/B: Deve ser incluída a coluna “CST A/B” no relatório.  Essa coluna deverá recuperar o código Situação Tributária “A” e código Situação Tributária “B”  Essa informação deve ser recuperada do campo 30 – COD_SITUACAO_A, da SAFX08 e do campo 31 - COD_SITUACAO_B da SAFX08. Separar a informação por uma barra “/”. | OS4073 |
| RN29 | Regra para inclusão da coluna VL Unitário: Deve ser incluída a coluna “VL Unitário” no relatório. Essa informação deve ser recuperada do campo 27 – VLR_UNIT, da SAFX08. | OS4073 |
| RN30 | Regra para inclusão da coluna QTD: Deve ser incluída a coluna “QTD” no relatório. Essa informação deve ser recuperada do campo 24 – QUANTIDADE, da SAFX08. | OS4073 |
| RN31 | Regra para inclusão da coluna VL Total: Deve ser incluída a coluna “VL Total” no relatório. Essa informação deve ser recuperada do campo 23 - VLR_TOT_NOTA , da SAFX07. | OS4073 |
| RN32 | Regra para inclusão da coluna VL Contábil: Deve ser incluída a coluna “VL Contábil” no relatório. Essa informação deve ser recuperada do campo 64 – VLR_CONTAB_ITEM, da SAFX08. | OS4073 |
| RN33 | Regra para inclusão da coluna Base ICMS: Deve ser incluída a coluna “Base ICMS” no relatório. Essa informação deve ser recuperada do campo 56 – BASE_ICMS, da SAFX08, considerando o código de tributação “Tributado” do campo 55 -  TRIB_ICMS da SAFX08. | OS4073 |
| RN34 | Regra para inclusão da coluna Aliq Trib. ICMS: Deve ser incluída a coluna “Aliq Trib. ICMS” no relatório. Essa informação deve ser recuperada do campo 42 – VLR_ALIQ_ICMS, da SAFX08. | OS4073 |
| RN35 | Regra para inclusão da coluna VL Trib. ICMS: Deve ser incluída a coluna “VL Trib. ICMS” no relatório. Essa informação deve ser recuperada do campo 43 –   VLR_ICMS, da SAFX08. | OS4073 |
| RN36 | Regra para inclusão da coluna Base Red. ICMS: Deve ser incluída a coluna “Base Red. ICMS” no relatório. Essa informação deve ser recuperada do campo 57 –   BASE_REDU_ICMS, da SAFX08. | OS4073 |
| RN37 | Regra para inclusão da coluna VL ICMS NDESTAC: Deve ser incluída a coluna “VL ICMS NDESTAC” no relatório. Essa informação deve ser recuperada do campo 80 – VLR_ICMS_NDESTAC, da SAFX08. | OS4073 |
| RN38 | Regra para inclusão da coluna VL IPI NDESTAC: Deve ser incluída a coluna “VL IPI NDESTAC” no relatório. Essa informação deve ser recuperada do campo 81 – VLR_IPI_NDESTAC, da SAFX08. | OS4073 |
| RN39 | Regra para inclusão da coluna VL Tributo ICMSS: Deve ser incluída a coluna “VL Tributo ICMSS” no relatório. Essa informação deve ser recuperada do campo 52 -   VLR_SUBST_ICMS, da SAFX08. | OS4073 |
| RN40 | Regra para inclusão da coluna VL Isentas: Deve ser incluída a coluna “VL Isentas” no relatório.Essa informação deve ser recuperada do campo 56 – BASE_ICMS, da SAFX08, considerando o código de tributação “Isenta” do campo 55 -  TRIB_ICMS da SAFX08. | OS4073 |
| RN41 | Regra para inclusão da coluna VL Outras: Deve ser incluída a coluna “VL Outras” no relatório. Essa informação deve ser recuperada do campo 56 – BASE_ICMS, da SAFX08, considerando o código de tributação “Outras” do campo 55 -  TRIB_ICMS da SAFX08. | OS4073 |
| RN42 | Regra para inclusão da coluna Alíq. Diferença: Deve ser incluída a coluna “Alíq. Diferença” no relatório. Essa informação deve ser recuperada do campo 44 - DIF_ALIQ_ICMS, da SAFX08. | OS4073 |
| RN43 | Regra para inclusão da coluna VL DIFAL: Deve ser incluída a coluna “VL DIFAL” no relatório. Deve ser calculado com base na parametrização de Base de Cálculo p/ Diferencial de Alíquota (Ferramentas >> Parâmetros do Sistema >> Parâmetros por Estabelecimento). Teremos as seguintes opções: 1 – (Base Tributada) 2 – (Base Tributada + Base Outras) 3 – (Valor Contábil – ICMS-S – Base Redução – Base Isenta) 4 – Valor Informado (Sem Base de Cálculo) Para os parâmetros de 1 a 3, com base na opção escolhida pelo usuário realiza-se o cálculo do Diferencial de Alíquota, multiplicando o valor obtido com para estes critérios de BC pela Diferença da Alíquota (campo 44 - DIF_ALIQ_ICMS da SAFX08, dividido por 100) Quando for informado o parâmetro 4, considerar o valor do campo Valor Diferença Alíquotas ICMS – Ativo / Material Consumo (campo 69 - VLR_OUTROS1). Estes valores são obtidos através da SAFX08, considerando os documentos de entrada (Movimento Entrada/Saída diferente de “9”), cuja Data Fiscal compreenda o período de geração e o campo Diferença da Alíquota seja maior que zero, desconsiderando documentos cancelados. | OS4073 |
| RN44 | Regra para inclusão da coluna Campo Observação LF E/S: Deve ser incluída a coluna “Campo Observação LF E/S” no relatório. Essa informação deve ser recuperada do campo campo 45 -  OBS_ICMS da SAFX08. | OS4073 |
| RN45 | Regra para inclusão da coluna Campo Desconto:  Preencher com o campo Vlr Desconto do item do documento fiscal (29 - VLR_DESCONTO da SAFX08), caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | CH1414_2014 |
| RN46 | Regra para inclusão da coluna Campo Base IPI:  Preencher com o campo Base IPI do item do documento fiscal (59 - BASE_IPI da SAFX08), considerando o código de tributação = 1, “Tributado” do campo (58 – TRIB_IPI da SAFX08). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | CH13715_2015 MFS_4310 |
| RN47 | Regra para inclusão da coluna Campo Alíquota IPI:  Preencher com o campo Alíquota IPI do item do documento fiscal (47 - VLR_ALIQ_IPI da SAFX08), caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,0000 | CH13715_2015 |
| RN48 | Regra para inclusão da coluna Campo Valor IPI:  Preencher com o campo Vlr. IPI do item do documento fiscal (48 - VLR_IPI da SAFX08), caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | CH13715_2015 |
| RN49 | Regra para inclusão da coluna Campo Valor do FCP UF Destino:  Preencher com o campo Valor do FCP UF Destino do item do documento fiscal (campo 221 VLR_FCP_UF_DEST da SAFX08). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS_3582 |
| RN50 | Regra para inclusão da coluna Campo Valor ICMS UF Destino:  Preencher com o campo Valor do ICMS UF Destino do item do documento fiscal (campo 222 VLR_ICMS_UF_DEST da SAFX08). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS_3582 |
| RN51 | Regra para inclusão da coluna Campo Valor ICMS UF Origem:  Preencher com o campo Valor do ICMS UF origem do item do documento fiscal (campo 223 VLR_ICMS_UF_ORIG da SAFX08). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS_3582 |
| RN52 | Regra para inclusão da coluna Campo  IPI Isentas:   Essa informação deverá ser recuperada do campo (59 - BASE_IPI da SAFX08), considerando o código de tributação = 2, “Isenta” do campo (58 – TRIB_IPI da SAFX08). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS_4310 |
| RN53 | Regra para inclusão da coluna Campo IPI Outras:   Essa informação deverá ser recuperada do campo (59 - BASE_IPI da SAFX08), considerando o código de tributação = 3, “Outras” do campo (58 – TRIB_IPI da SAFX08). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS_4310 |
| RN54 | Regra para inclusão da coluna Campo Base ICMS S:   Essa informação deverá ser recuperada do item do documento fiscal (campo 61 BASE_SUB_TRIB_ICMS da SAFX08). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS_4310 |
| RN55 | Regra para inclusão da coluna Código de Tributação IPI:   Essa informação deverá ser recuperada do item do documento fiscal (campo 146 COD_TRIB_IPI da SAFX08). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Numérico Formato: 00 | MFS_14922 |
| RN56 | Regra para inclusão da coluna Campo Base INSS:   Essa informação deverá ser recuperada da capa do documento fiscal (campo 85 VLR_INSS_RETIDO da SAFX07). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS-71662 |
| RN57 | Regra para inclusão da coluna Campo Valor Alíquota INSS:   Essa informação deverá ser recuperada da capa do documento fiscal (campo 86 VLR_ALIQ_INSS da SAFX07). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS-71662 |
| RN58 | Regra para inclusão da coluna Campo Valor INSS:   Essa informação deverá ser recuperada do item do documento fiscal (campo 87 VLR_INSS_RETIDO da SAFX07). Caso este não esteja preenchido, preencher com zeros respeitando o formato.  Formato: 0,00 | MFS-71662 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

