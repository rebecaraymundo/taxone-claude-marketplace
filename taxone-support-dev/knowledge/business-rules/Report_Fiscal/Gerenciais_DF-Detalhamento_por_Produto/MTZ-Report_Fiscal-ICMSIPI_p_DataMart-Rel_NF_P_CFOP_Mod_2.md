---
source: "MTZ-Report_Fiscal-ICMSIPI_p_DataMart-Rel_NF_P_CFOP_Mod_2.docx"
category: Report_Fiscal
converted: auto
---

# REPORT FISCAL


# Relatório de NF p/ CFOP Modelo 2


Menu: Básicos - Report Fiscal > Obrigações Acessórias  ICMS/IPI por DataMart Relatório de NF p/ CFOP Modelo 2

# DOCUMENTO DE REQUISITO





## REGRAS DE NEGÓCIO





Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| DR | Nome | Descrição |
| --- | --- | --- |
| CH71351 | DW - RF - Inclusão de Modelo Doc e Chave de Acesso no relatório por CFOP Modelo 2 | Criados das colunas: Chave de Acesso e Modelo de Documento no relatório. |
| OS3629 | Criação e remanejamento de colunas | Criação e remanejamento de colunas do Relatório |
| OS4260 | Criação de campo Nº Item NF | Alteração do relatório para criação do campo Nº Item NF |
| MFS32994 | Andréa Rocha | Incluir novas colunas no relatório, mostrando os campos BC ICMS ST, Base do PIS e COFINS, Valores PIS e COFINS. |
| MFS575466 | Rogério Ohashi | Inclusão de Regra para recuperar os valores da Capa para Notas Fiscais sem Item. |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Regras da tela:  Criar “Flag” com a opção “Inscrição Estadual Única”. Se o flag for habilitado recuperar os estabelecimentos relacionados ao selecionado na opção de seleção “Estabelecimento” através da tabela ICP_INSC_EST_CENTR (CONTROLE DE OBRIGAÇÕES ESTADUAIS => OBRIGAÇÕES => EMPRESAS/ESTABELECIMENTOS I. E. U.) campo cod_estab que estiverem com o campo cod_estab_centr igual ao selecionado na opção “Estabelecimento” desde que eles estejam na mesma UF da selecionada na opção “UF”.  Caso o Estabelecimento selecionado não seja Centralizador e o cliente flegue a opção “Inscrição Estadual Única” deverá ser exibida a seguinte mensagem de erro: “O Estabelecimento selecionado não é Centralizador, verificar se o parâmetro selecionado (Inscrição Estadual Única) está correto.”  Na listbox “ESTABELECIMENTO”, deverão aparecer somente os Estabelecimentos situados na UF selecionada na listbox anterior “UF”; Caso o usuário a selecione a opção “TODOS”, deverão ser gerados os dados de todos os Estabelecimentos daquela determinada UF previamente selecionada. | CH72444 CH72452 |
| RN01 | Diminuir a coluna: Nº/Série/SubSérie/Nota Fiscal em 5 posições; Caso as informações ultrapassem o espaço do relatório, as mesmas deverão ser quebradas para continuar na próxima linha; O nome da coluna deve ser abreviada da seguinte forma: Nº/Série/SubSérie/NF | CH71351 |
| RN02 | Diminuir a coluna: Produto em 21 posições; Caso as informações ultrapassem o espaço do relatório, as mesmas deverão ser quebradas para continuar na próxima linha; | CH71351 |
| RN03 | Diminuir a coluna: Código Razão Social em 7 posições; Caso as informações ultrapassem o espaço do relatório, as mesmas deverão ser quebradas para continuar na próxima linha; | CH71351 |
| RN04 | Criar a coluna: Mod. NF com 3 posições (embora sejam duas posições, é necessário caber o título) será preenchida com a informação cadastrada no campo 13 da SAFX07 | CH71351 |
| RN05 | Criar a coluna: Chave de Acesso com 30 posições e será preenchido com a informação cadastrada no campo 226 da SAFX07. Caso as informações ultrapassem o espaço do relatório, as mesmas deverão ser quebradas para continuar na próxima linha; | CH71351 |
| RN06 | Deverá ser alterada a ordem das colunas do Relatório utilizando a lista descrita abaixo:  UF Cliente/Fornecedor Nº/Série/Subserie NF NF AR  Data Fiscal Produto (código + descrição) Nº Item NF Descrição Complementar CFOP Extensão CFOP NBM Pessoa Física/Jurídica: Código – Razão Social Pessoa Física/Jurídica: CNPJ/CPF Valor Líquido Vlr Unit. Quant. Vlr Base ICMS Vlr ICMS  Alíq. ICMS  Base PIS e Vlr PIS [MFS32994] ICMS ST  Base ICMS ST  [MFS32994] Vlr ICMS ñ escrit. Vlr IPI ñ escrit.  Vlr IPI Vlr Base IPI Aliq. IPI Base COFINS e Vlr COFINS [MFS32994] Mod. NF Chave de Acesso | OS3629 OS4260 MFS32994 |
| RN07 | Criar a coluna: UF Cliente/Fornecedor com 2 posições e será preenchido com a informação cadastrada no campo 19 da SAFX04. Para seleção do campo, deverá buscar a informação que estiver contida no campo IDENT_FIS_JUR da tabela SAFX07 e comparar com a mesma do campo IND_FIS_JUR da SAFX04. | OS3629 |
| RN08 | Criar a coluna: NF AR com 12 posições e será preenchido com a informação cadastrada no campo 69 da SAFX07. | OS3629 |
| RN09 | Criar a coluna: Vlr Base de Cálculo com 17 posições (015V002) e será preenchido com a informação cadastrada no campo 56 da SAFX08 ou Campo 51 da SAFX07. | OS3629 MFS575466 |
| RN10 | Criar a coluna: Alíquota ICMS com 07 posições (003V004) e será preenchido com a informação cadastrada no campo 42 da SAFX08 ou Campo 34 da SAFX07. | OS3629 MFS575466 |
| RN11 | Criar a coluna: ICMS ST com 17 posições (015V002) e será preenchido com a informação cadastrada no campo 52 da SAFX08 ou Campo 48 da SAFX07. | OS3629 MFS575466 |
| RN12 | Criar a coluna: Vlr ICMS ñ escrit. com 17 posições (015V002) e será preenchido com a informação cadastrada no campo 80 da SAFX08 ou Campo 83 da SAFX07. | OS3629 MFS575466 |
| RN13 | Criar a coluna: Vlr IPI ñ escrit. com 17 posições (015V002) e será preenchido com a informação cadastrada no campo 81 da SAFX08 ou Campo 84 da SAFX07. | OS3629 MFS575466 |
| RN14 | Criar a coluna: IE com 14 posições e será preenchido com a informação cadastrada no campo 08 da SAFX04. Para seleção do campo, deverá buscar a informação que estiver contida no campo IDENT_FIS_JUR da tabela SAFX07 e comparar com a mesma do campo IND_FIS_JUR da SAFX04. | OS3629 |
| RN15 | Criar a coluna: Nº Item NF com tamanho de 05 posições (005) de tipo numérico que será preenchido com a informação cadastrada no campo 18 (NUM_ITEM) da SAFX08. | OS4260 |
| RN16 | Criar nova coluna no relatório de NF p/ CFOP - Modelo 2, o campo deve receber concatenado o código da situação tributária A (CST – ICMS - Origem da Mercadoria) – TACES03 + o código da situação tributária B, (CST – ICMS - Tributação pelo ICMS) - TACES04. (Campo 179 e 180 da SAFX07 ou Campo 30 e 31 da SAFX08) | OS4406 MFS575466 |
| RN17 | Criar nova coluna no relatório de NF p/ CFOP - Modelo 2, o campo deve receber a Unidade de Medida utilizado no item de Notas Fiscais de Mercadorias e Produtos, coluna COD_MEDIDA item 25 da SAFX08. | OS4527 |
| RN18 | Incluir campo de descrição complementar no relatório. Este campo é descricao_compl da tabela x08_itens_merc. A coluna terá como título: “DESCRIÇÃO COMPLEMENTAR” e será colocada logo após a coluna de Produto. | CH73529 |
| RN19 | Nova Coluna: Base ICMS-ST:  Preencher com o campo 61- Base ICMS Substituição Tributária da SAFX08 ou Campo 64 da SAFX07. | MFS32994 MFS575466 |
| RN20 | Nova Coluna: Base PIS:  Preencher com o campo 86- Base PIS da SAFX08 ou campo 102 – Base PIS da SAFX07. | MFS32994 MFS575466 |
| RN21 | Nova Coluna: Valor PIS:  Preencher com o campo 87- Valor PIS da SAFX08 ou campo 103 – Valor PIS da SAFX07. | MFS32994 MFS575466 |
| RN22 | Nova Coluna: Base COFINS:  Preencher com o campo 88- Base COFINS da SAFX08 ou campo 104 – Base COFINS da SAFX07. | MFS32994 MFS575466 |
| RN23 | Nova Coluna: Valor COFINS:  Preencher com o campo 89- Valor COFINS da SAFX08 ou campo 105 – Valor COFINS da SAFX07. | MFS32994 MFS575466 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

