# MTZ_Report_Fiscal_Relatorio_Analitico_Detalhamento_de_Produto

- **Fonte:** MTZ_Report_Fiscal_Relatorio_Analitico_Detalhamento_de_Produto.docx
- **Modificado:** 2026-02-24
- **Tamanho:** 41 KB

---

__Relatório Detalhamento por Produto\.__

__Localização__: Menu Básicos, Módulo Report Fiscal, Gerenciais, Documentos Fiscais, Analíticos, Detalhamento por Produto

__DOCUMENTO DE REQUISITO__

###### DR

###### Nome

__Descrição__

OS4073

Jefferson Mota

Criação do relatório Analítico e definição das regras para geração\.

CH1414\_2014

Julyana Perrucini

Inclusão de campo Valor Desconto no relatório\.

CH13715\_2015

Julyana Perrucini

Inclusão de campos: Base IPI, Alíquota IPI e Valor IPI; no relatório\.

MFS\_3582

Eric Celestrino

Inclusão de campos: Valor FCP UF Destino, Valor ICMS UF Destino e Valor ICMS UF Origem\.

MFS\_4310

João Henrique

Inclusão de campos: IPI Isentas, IPI Outras e Base ICMSS\.

Revisão da Regra do Campo: Base IPI\.

MFS\_14922

João Henrique

Inclusão do campo de Código de Tributação IPI no relatório\.

MFS\-71662

Rogério Ohashi

Inclusão dos campos Valor Base INSS, Valor Alíquota INSS e Valor de INSS Retido no relatório\.

__REGRAS DE NEGÓCIO__

####    Cód\.

###   Descrição

###       DR

RN00

__Regra de Seleção: __Este relatório será gerado com base nas informações das tabelas SAFX04, SAFX07, SAFX08 e SAFX2013, considerando os parâmetros de, período, CFOP e estabelecimento parametrizados na tela de emissão do relatório\.

Serão considerados os registros das tabelas SAFX07 e SAFX08, cuja Data Fiscal compreenda o período parametrizado, considerando apenas os registros do estabelecimento \(ou estabelecimento\) indicado e que tenham os mesmos códigos de CFOP parametrizados com correspondência no item\. As notas fiscais canceladas e notas fiscais sem itens, não serão consideradas\.

Serão consideradas todas as classificações de documento fiscal, referente ao campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\. 

Como a quantidade de colunas é muito grande, ele será apenas disponibilizado em tela, com a possibilidade de visualizar todas as colunas, e poderá também ser salvo no formato Excel e texto\.

__Ordenação do relatório:__ Data Fiscal, N° NF, Série e Sub\-Série\.

OS4073

RN01

__Regra para hierarquia do Menu:__

Deverá ser criado o seguinte sub\-menu no módulo Report Fiscal:

- Gerenciais
	- Documentos Fiscais
	-        Analíticos  
	- __    Detalhamento por Produto__

OS4073

__Cabeçalho__

RN02

__Empresa:__

Por default, deve apresentar a empresa que está conectada no manager\.

OS4073

RN03

__Código do Estabelecimento:__

Corresponde ao estabelecimento selecionado na tela de geração do Relatório Analítico\.

OS4073

RN04

__Razão Social:__

Corresponde ao campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

OS4073

RN05

__Período de Geração do Relatório:__

Corresponde ao período incial e ao período final, informados na tela de geração do relátório analítico\. Exemplo: Período: dd/mm/aaaa à dd/mm/aaaa

OS4073

RN06

__CNPJ:__

Corresponde ao campo CNPJ da tabela ESTABELECIMENTO\.

OS4073

RN07

__Data e Horário de Geração do Relatório :__

Deverá inserir no relatório a data de geração seguida do horário atual, conforme exemplo abaixo:

Data: dd/mm/aaaa 00:00:00hs

OS4073

RN08

__Página:__

Corresponde ao número da página que esta sendo exibida para o usuário\.

OS4073

__Dados Geral do Relatório__

RN09

__Regra para inclusão da coluna N° NF:__

Deve ser incluída a coluna “N° NF” no relatório acima\.

Essa informação deve ser recuperada do campo 08 – NUM\_DOCFIS, da SAFX07\.

OS4073

RN10

__Regra para inclusão da coluna Série/Subsérie:__

Deve ser incluída a coluna “Série/Subsérie” no relatório\.

Essa informação deve ser recuperada do campo 09 – SERIE\_DOCFIS, seguido do campo 10 – SUB\_SERIE\_DOCFIS, da SAFX07\.

Formatação: Série/Sub\-série

OS4073

RN11

__Regra para inclusão da coluna Data Fiscal:__

Deve ser incluída a coluna “Data Fiscal” no relatório\.

Essa informação deve ser recuperada do campo Data Fiscal da SAFX07\.

OS4073

RN12

__Regra para inclusão da coluna Data Emissão:__

Deve ser incluída a coluna “Data Emissão” no relatório\.

Essa informação deve ser recuperada do campo 11 – DATA\_EMISSAO, da SAFX07\.

OS4073

RN13

__Regra para inclusão da coluna N° de Controle:__

Deve ser incluída a coluna “N° de Controle” no relatório\.

Essa informação deve ser recuperada do campo 69 – NUM\_CONTROLE\_DOCTO, da SAFX07\.

OS4073

RN14

__Regra para inclusão da coluna Mod\. Documento:__

Deve ser incluída a coluna “Mod\. Documento” no relatório\.Essa informação deve ser recuperada do campo 13 – COD\_MODELO, da SAFX07\.

OS4073

RN15

__Regra para inclusão da coluna Chave de acesso da NF\-e:__

Deve ser incluída a coluna “Chave de acesso da NF\-e” no relatório\.Essa informação deve ser recuperada do campo 226 – NUM\_AUTENTIC\_NFE, da SAFX07\.

OS4073

RN16

__Regra para inclusão da coluna Código FIS/JUR:__

Deve ser incluída a coluna “Código FIS/JUR” no relatório\.

Essa informação deve ser recuperada do campo 06 – IDENT\_FIS\_JUR seguido do campo 07 – COD\_FIS\_JUR, da SAFX07\. Separar a informação por um hífen\.

OS4073

RN17

__Regra para inclusão da coluna Código Razão Social:__

Deve ser incluída a coluna “Razão Social” no relatório\.

Essa informação deve ser recuperada do campo 05 – RAZAO\_SOCIAL, da SAFX04\.

OS4073

RN18

__Regra para inclusão da coluna CPF/CNPJ:__

Deve ser incluída a coluna “CPF/CNPJ” no relatório\.

Essa informação deve ser recuperada do campo 06 – CPF\_CGC, da SAFX04\.

OS4073

RN19

__Regra para inclusão da coluna Insc\. Estadual:__

Deve ser incluída a coluna “Insc\. Estadual” no relatório\.

Essa informação deve ser recuperada do campo 08 – INSC\_ESTADUAL, da SAFX04\.

OS4073

RN20

__Regra para inclusão da coluna UF:__

Deve ser incluída a coluna “UF” no relatório\.

Essa informação deve ser recuperada do campo 19 – UF, da SAFX04\.

OS4073

RN21

__Regra para inclusão da coluna N° do Item:__

Deve ser incluída a coluna “N° do Item” no relatório\.

Essa informação deve ser recuperada do campo 18 – NUM\_ITEM , da SAFX08\.

OS4073

RN22

__Regra para inclusão da coluna Código do Produto:__

Deve ser incluída a coluna “Código do Produto” no relatório\.

Essa informação deve ser recuperada do campo 13 – IND\_PRODUTO seguido do campo 14 – COD\_PRODUTO, da SAFX08\. Separar a informação por um hífen\.

OS4073

RN23

__Regra para inclusão da coluna Descrição:__

Deve ser incluída a coluna “Descrição” no relatório\.

Essa informação deve ser recuperada do campo 04 – DESCRICAO, da SAFX2013

OS4073

RN24

__Regra para inclusão da coluna Descrição Complementar:__

Deve ser incluída a coluna “Descrição Complementar” no relatório\.

Essa informação deve ser recuperada do campo 21 – DESCRICAO\_COMPL, da SAFX08\.

OS4073

RN25

__Regra para inclusão da coluna NCM:__

Deve ser incluída a coluna “NCM” no relatório\.

Essa informação deve ser recuperada do campo 26 – COD\_NBM, da SAFX08\.

OS4073

RN26

__Regra para inclusão da coluna CFOP:__

Deve ser incluída a coluna “CFOP” no relatório\.

Essa informação deve ser recuperada do campo 22 – COD\_CFO, da SAFX08\.

OS4073

RN27

__Regra para inclusão da coluna Nat\. Operação:__

Deve ser incluída a coluna “Nat\. Operação” no relatório\.

Essa informação deve ser recuperada do campo 23 – COD\_NATUREZA\_OP, da SAFX08\.

OS4073

RN28

__Regra para inclusão da coluna CST A/B:__

Deve ser incluída a coluna “CST A/B” no relatório\. 

Essa coluna deverá recuperar o código Situação Tributária “A” e código Situação Tributária “B”

Essa informação deve ser recuperada do campo 30 – COD\_SITUACAO\_A, da SAFX08 e do campo 31 \- COD\_SITUACAO\_B da SAFX08\. Separar a informação por uma barra __“/”__\.

OS4073

RN29

__Regra para inclusão da coluna VL Unitário:__

Deve ser incluída a coluna “VL Unitário” no relatório\.

Essa informação deve ser recuperada do campo 27 – VLR\_UNIT, da SAFX08\.

OS4073

RN30

__Regra para inclusão da coluna QTD:__

Deve ser incluída a coluna “QTD” no relatório\.

Essa informação deve ser recuperada do campo 24 – QUANTIDADE, da SAFX08\.

OS4073

RN31

__Regra para inclusão da coluna VL Total:__

Deve ser incluída a coluna “VL Total” no relatório\.

Essa informação deve ser recuperada do campo 23 \- VLR\_TOT\_NOTA , da SAFX07\. 

OS4073

RN32

__Regra para inclusão da coluna VL Contábil:__

Deve ser incluída a coluna “VL Contábil” no relatório\.

Essa informação deve ser recuperada do campo 64 – VLR\_CONTAB\_ITEM, da SAFX08\.

OS4073

RN33

__Regra para inclusão da coluna Base ICMS:__

Deve ser incluída a coluna “Base ICMS” no relatório\.

Essa informação deve ser recuperada do campo 56 – BASE\_ICMS, da SAFX08, considerando o código de tributação “Tributado” do campo 55 \-  TRIB\_ICMS da SAFX08\.

OS4073

RN34

__Regra para inclusão da coluna Aliq Trib\. ICMS:__

Deve ser incluída a coluna “Aliq Trib\. ICMS” no relatório\.

Essa informação deve ser recuperada do campo 42 – VLR\_ALIQ\_ICMS, da SAFX08\.

OS4073

RN35

__Regra para inclusão da coluna VL Trib\. ICMS:__

Deve ser incluída a coluna “VL Trib\. ICMS” no relatório\.

Essa informação deve ser recuperada do campo 43 –   VLR\_ICMS, da SAFX08\.

OS4073

RN36

__Regra para inclusão da coluna Base Red\. ICMS:__

Deve ser incluída a coluna “Base Red\. ICMS” no relatório\.

Essa informação deve ser recuperada do campo 57 –   BASE\_REDU\_ICMS, da SAFX08\. 

OS4073

RN37

__Regra para inclusão da coluna VL ICMS NDESTAC:__

Deve ser incluída a coluna “VL ICMS NDESTAC” no relatório\.

Essa informação deve ser recuperada do campo 80 – VLR\_ICMS\_NDESTAC, da SAFX08\.

OS4073

RN38

__Regra para inclusão da coluna VL IPI NDESTAC:__

Deve ser incluída a coluna “VL IPI NDESTAC” no relatório\.

Essa informação deve ser recuperada do campo 81 – VLR\_IPI\_NDESTAC, da SAFX08\.

OS4073

RN39

__Regra para inclusão da coluna VL Tributo ICMSS:__

Deve ser incluída a coluna “VL Tributo ICMSS” no relatório\.

Essa informação deve ser recuperada do campo 52 \-   VLR\_SUBST\_ICMS, da SAFX08\.

OS4073

RN40

__Regra para inclusão da coluna VL Isentas:__

Deve ser incluída a coluna “VL Isentas” no relatório\.Essa informação deve ser recuperada do campo 56 – BASE\_ICMS, da SAFX08, considerando o código de tributação “Isenta” do campo 55 \-  TRIB\_ICMS da SAFX08\.

OS4073

RN41

__Regra para inclusão da coluna VL Outras:__

Deve ser incluída a coluna “VL Outras” no relatório\.

Essa informação deve ser recuperada do campo 56 – BASE\_ICMS, da SAFX08, considerando o código de tributação “Outras” do campo 55 \-  TRIB\_ICMS da SAFX08\.

OS4073

RN42

__Regra para inclusão da coluna Alíq\. Diferença:__

Deve ser incluída a coluna “Alíq\. Diferença” no relatório\.

Essa informação deve ser recuperada do campo 44 \- DIF\_ALIQ\_ICMS, da SAFX08\.

OS4073

RN43

__Regra para inclusão da coluna VL DIFAL:__

Deve ser incluída a coluna “VL DIFAL” no relatório\.

Deve ser calculado com base na parametrização de Base de Cálculo p/ Diferencial de Alíquota \(Ferramentas >> Parâmetros do Sistema >> Parâmetros por Estabelecimento\)\.

Teremos as seguintes opções:

1 – \(Base Tributada\)

2 – \(Base Tributada \+ Base Outras\)

3 – \(Valor Contábil – ICMS\-S – Base Redução – Base Isenta\)

4 – Valor Informado \(Sem Base de Cálculo\)

Para os parâmetros de 1 a 3, com base na opção escolhida pelo usuário realiza\-se o cálculo do Diferencial de Alíquota, __multiplicando__ o valor obtido com para estes critérios de BC pela Diferença da Alíquota \(campo 44 \- DIF\_ALIQ\_ICMS da SAFX08, dividido por 100\)

Quando for informado o parâmetro 4, considerar o valor do campo Valor Diferença Alíquotas ICMS – Ativo / Material Consumo \(campo 69 \- VLR\_OUTROS1\)\.

Estes valores são obtidos através da SAFX08, considerando os documentos de entrada \(Movimento Entrada/Saída diferente de “9”\), cuja Data Fiscal compreenda o período de geração e o campo Diferença da Alíquota seja maior que zero, desconsiderando documentos cancelados\. 

OS4073

RN44

__Regra para inclusão da coluna Campo Observação LF E/S:__

Deve ser incluída a coluna “Campo Observação LF E/S” no relatório\.

Essa informação deve ser recuperada do campo campo 45 \-  OBS\_ICMS da SAFX08\.

OS4073

RN45

__Regra para inclusão da coluna Campo Desconto__:

Preencher com o campo Vlr Desconto do item do documento fiscal \(29 \- VLR\_DESCONTO da SAFX08\), caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

CH1414\_2014

RN46

__Regra para inclusão da coluna Campo Base IPI__:

Preencher com o campo Base IPI do item do documento fiscal \(59 \- BASE\_IPI da SAFX08\), considerando o código de tributação = 1, “Tributado” do campo \(58 – TRIB\_IPI da SAFX08\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

CH13715\_2015

MFS\_4310

RN47

__Regra para inclusão da coluna Campo Alíquota IPI__:

Preencher com o campo Alíquota IPI do item do documento fiscal \(47 \- VLR\_ALIQ\_IPI da SAFX08\), caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,0000

CH13715\_2015

RN48

__Regra para inclusão da coluna Campo Valor IPI__:

Preencher com o campo Vlr\. IPI do item do documento fiscal \(48 \- VLR\_IPI da SAFX08\), caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

CH13715\_2015

RN49

__Regra para inclusão da coluna Campo Valor do FCP UF Destino__:

Preencher com o campo Valor do FCP UF Destino do item do documento fiscal \(campo 221 VLR\_FCP\_UF\_DEST da SAFX08\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\_3582

RN50

__Regra para inclusão da coluna Campo Valor ICMS UF Destino__:

Preencher com o campo Valor do ICMS UF Destino do item do documento fiscal \(campo 222 VLR\_ICMS\_UF\_DEST da SAFX08\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\_3582

RN51

__Regra para inclusão da coluna Campo Valor ICMS UF Origem__:

Preencher com o campo Valor do ICMS UF origem do item do documento fiscal \(campo 223 VLR\_ICMS\_UF\_ORIG da SAFX08\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\_3582

RN52

__Regra para inclusão da coluna Campo  IPI Isentas: __

Essa informação deverá ser recuperada do campo \(59 \- BASE\_IPI da SAFX08\), considerando o código de tributação = 2, “Isenta” do campo \(58 – TRIB\_IPI da SAFX08\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\_4310

RN53

__Regra para inclusão da coluna Campo IPI Outras: __

Essa informação deverá ser recuperada do campo \(59 \- BASE\_IPI da SAFX08\), considerando o código de tributação = 3, “Outras” do campo \(58 – TRIB\_IPI da SAFX08\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\_4310

RN54

__Regra para inclusão da coluna Campo Base ICMS S: __

Essa informação deverá ser recuperada do item do documento fiscal \(campo 61 BASE\_SUB\_TRIB\_ICMS da SAFX08\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\_4310

RN55

__Regra para inclusão da coluna Código de Tributação IPI: __

Essa informação deverá ser recuperada do item do documento fiscal \(campo 146 COD\_TRIB\_IPI da SAFX08\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Numérico

Formato: 00

MFS\_14922

RN56

__Regra para inclusão da coluna Campo Base INSS: __

Essa informação deverá ser recuperada da __capa__ do documento fiscal \(campo 85 VLR\_INSS\_RETIDO da SAFX07\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\-71662

RN57

__Regra para inclusão da coluna Campo Valor Alíquota INSS: __

Essa informação deverá ser recuperada da __capa__ do documento fiscal \(campo 86 VLR\_ALIQ\_INSS da SAFX07\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\-71662

RN58

__Regra para inclusão da coluna Campo Valor INSS: __

Essa informação deverá ser recuperada do item do documento fiscal \(campo 87 VLR\_INSS\_RETIDO da SAFX07\)\. Caso este não esteja preenchido, preencher com zeros respeitando o formato\.

Formato: 0,00

MFS\-71662

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

