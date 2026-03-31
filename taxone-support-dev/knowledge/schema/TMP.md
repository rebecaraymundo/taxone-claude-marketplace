# Módulo: TMP (Temporárias) - 140 tabelas

## TMP_ANEXO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANEXO | VARCHAR2(10) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(40) | Y |  |  |

**PK**: ANEXO

---

## TMP_ARQUIVOS_SERVIDOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DIRECTORY_NAME | VARCHAR2(30) | Y |  |  |
| 2 | DIRECTORY_PATH | VARCHAR2(4000) | Y |  |  |
| 3 | NOME_ARQ | VARCHAR2(100) | Y |  |  |

---

## TMP_ARQ_AJUSTE_MASSA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LINHA | NUMBER | Y |  |  |
| 2 | COLUNA | NUMBER | Y |  |  |
| 3 | VALOR | VARCHAR2(2000) | Y |  |  |

**Indexes**:
- IX_AJUSTE_MASSA_02: (LINHA, COLUNA)
- IX_ARQ_AJUSTE_MASSA: (LINHA)

---

## TMP_ARQ_SERVIDOR_GEMT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DIRECTORY_NAME | VARCHAR2(30) | Y |  |  |
| 2 | DIRECTORY_PATH | VARCHAR2(4000) | Y |  |  |
| 3 | NOME_ARQ | VARCHAR2(100) | Y |  |  |
| 4 | ID_GER | NUMBER(12) | Y |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 6 | COD_TIPO_ARQ | VARCHAR2(5) | Y |  |  |
| 7 | COD_LAYOUT | VARCHAR2(3) | Y |  |  |
| 8 | GRUPO_TRIBUTO | VARCHAR2(1) | Y |  |  |
| 9 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 10 | DATA_INICIAL | DATE | Y |  |  |
| 11 | DATA_FINAL | DATE | Y |  |  |

---

## TMP_BALANCO_TOT_TREE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA_AGLUT_TOT | VARCHAR2(70) | N |  |  |
| 2 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |

**PK**: COD_CONTA_AGLUT_TOT, COD_CONTA_AGLUT

---

## TMP_CARGA_ARQUIVO
**Comment**: Tabela Temporária utilizada para armazenar os dados de um arquivos, cuja importação não seja por SAFX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_REG | VARCHAR2(200) | N |  | campo de identificacao da linha do arquivo, pode ser um sequencial, ou os dados da chave, utilizado para ordenacao |
| 2 | LINHA | VARCHAR2(2000) | Y |  | campo referente a linha do arquivo importado |
| 3 | IND_DEMONST | CHAR(1) | Y |  |  |
| 4 | DSC_CABEC_DEMONST | VARCHAR2(1000) | Y |  |  |
| 5 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 6 | PERIODO | NUMBER(2) | Y |  |  |
| 7 | ANO | NUMBER(4) | Y |  |  |
| 8 | ID_TP_DEMONST | NUMBER(12) | Y |  |  |
| 9 | DSC_DIRETORIO | VARCHAR2(500) | Y |  |  |
| 10 | PROC_ID | NUMBER(12) | N |  |  |

**PK**: IDENT_REG, PROC_ID

---

## TMP_CONF_DIVERGE_DOCFISCAL_GR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | DATA_INICIAL | DATE | Y |  |  |
| 8 | DATA_FINAL | DATE | Y |  |  |
| 9 | DATA_EMISSAO | DATE | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(6) | Y |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 13 | VALOR_TOTAL | NUMBER(17,2) | Y |  |  |
| 14 | VALOR_TOTAL_ITENS | NUMBER(17,2) | Y |  |  |
| 15 | QTDE_ITENS | VARCHAR2(6) | Y |  |  |
| 16 | COD_CFOP | VARCHAR2(6) | Y |  |  |
| 17 | VALOR_CONTABIL_ITENS | NUMBER(17,2) | Y |  |  |
| 18 | CLASSIFICACAO_DOC | VARCHAR2(50) | Y |  |  |
| 19 | MODELO_DOCUMENTO | VARCHAR2(6) | Y |  |  |
| 20 | NORM_DEV | VARCHAR2(10) | Y |  |  |
| 21 | TIPO_MOVIMENTO | VARCHAR2(20) | Y |  |  |
| 22 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(70) | Y |  |  |
| 23 | PROCESSADO | VARCHAR2(1) | Y |  |  |
| 24 | PERIODO_COM_MOVIMENTO | VARCHAR2(50) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_CONF_DIV_DOC: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_CONF_DOC_FIS_RS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | DATA_INICIAL | DATE | Y |  |  |
| 6 | DATA_FINAL | DATE | Y |  |  |
| 7 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 8 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 9 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 10 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(100) | Y |  |  |
| 11 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | DATA_FISCAL | DATE | Y |  |  |
| 14 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 15 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 16 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 17 | CPF_CGC | VARCHAR2(20) | Y |  |  |
| 18 | RAZAO_SOCIAL_PFJ | VARCHAR2(70) | Y |  |  |
| 19 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 20 | DESCRICAO | VARCHAR2(255) | Y |  |  |
| 21 | COD_CFOP | VARCHAR2(6) | Y |  |  |
| 22 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 23 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 24 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 25 | CST_ICMS | VARCHAR2(20) | Y |  |  |
| 26 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ALIQ_ICMS | NUMBER(19,4) | Y |  |  |
| 28 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 29 | VLR_SUBST_ICMS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 31 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 33 | CST_IPI | VARCHAR2(20) | Y |  |  |
| 34 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 35 | VLR_ALIQ_IPI | NUMBER(19,4) | Y |  |  |
| 36 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 37 | CST_PIS | VARCHAR2(20) | Y |  |  |
| 38 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 39 | VLR_ALIQ_PIS | NUMBER(19,4) | Y |  |  |
| 40 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 41 | CST_COFINS | VARCHAR2(20) | Y |  |  |
| 42 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 43 | VLR_ALIQ_COFINS | NUMBER(19,4) | Y |  |  |
| 44 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 45 | ALIQ_AD_REM_ICMS | NUMBER(7,4) | Y |  |  |
| 46 | VLR_ICMS_MONO | NUMBER(17,2) | Y |  |  |
| 47 | ALIQ_AD_REM_ICMS_RETEN | NUMBER(7,4) | Y |  |  |
| 48 | VLR_ICMS_MONO_RETEN | NUMBER(17,2) | Y |  |  |
| 49 | VLR_ICMS_MONO_OP | NUMBER(17,2) | Y |  |  |
| 50 | VLR_ICMS_MONO_DIF | NUMBER(17,2) | Y |  |  |
| 51 | ALIQ_AD_REM_ICMS_RET | NUMBER(7,4) | Y |  |  |
| 52 | VLR_ICMS_MONO_RET | NUMBER(17,2) | Y |  |  |
| 53 | PERIODO_COM_MOVIMENTO | VARCHAR2(50) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_CONF_DOC_RS: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_COUNT_SAFX
**Comment**: Tabela utilizada no expurgo das tabelas temporárias (SAFX) para armazenamento da quantidade de linhas existentes em cada SAFX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 2 | NUMERO_ARQUIVO | NUMBER(3) | N |  |  |
| 3 | DESCRICAO_ARQUIVO | VARCHAR2(50) | Y |  |  |
| 4 | NOM_TAB_WORK | VARCHAR2(8) | N |  |  |
| 5 | COUNT_ROWS | NUMBER(20) | Y |  |  |

**PK**: GRUPO_ARQUIVO, NUMERO_ARQUIVO, NOM_TAB_WORK

---

## TMP_CREDPIS_SALDO_CRED_BEM_GR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | PERIODO | DATE | Y |  |  |
| 8 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 9 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 10 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 11 | DATA_INI_CRED | DATE | Y |  |  |
| 12 | DATA_FIM_CRED | DATE | Y |  |  |
| 13 | IND_PARCELA | NUMBER(3) | Y |  |  |
| 14 | NUM_PARCELA_CREDPIS | NUMBER(3) | Y |  |  |
| 15 | QT_PARC_A_CRED | NUMBER(3) | Y |  |  |
| 16 | DATA_LANCTO | DATE | Y |  |  |
| 17 | VLR_PIS_MENSAL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_COFINS_MENSAL | NUMBER(17,2) | Y |  |  |
| 19 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 20 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 21 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 22 | RAZAO_SOCIAL_FIS_JUR | VARCHAR2(70) | Y |  |  |
| 23 | DATA_AQUIS | DATE | Y |  |  |
| 24 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_PIS_CREDITADO | NUMBER(17,2) | Y |  |  |
| 27 | VLR_COFINS_CREDITADO | NUMBER(17,2) | Y |  |  |
| 28 | QT_PARCELAS_CREDITADO | NUMBER(3) | Y |  |  |
| 29 | VLR_PIS_CREDITAR | NUMBER(17,2) | Y |  |  |
| 30 | VLR_COFINS_CREDITAR | NUMBER(17,2) | Y |  |  |
| 31 | QT_PARCELAS_CREDITAR | NUMBER(3) | Y |  |  |
| 32 | SLD_CREDITAR_PIS | NUMBER(17,2) | Y |  |  |
| 33 | SLD_CREDITAR_COFINS | NUMBER(17,2) | Y |  |  |
| 34 | QTD_PARCELAS_SLD_CREDITAR | NUMBER(3) | Y |  |  |
| 35 | IND_BAIXA | CHAR(1) | Y |  |  |
| 36 | DAT_BAIXA | DATE | Y |  |  |
| 37 | MOTIVO_BAIXA | CHAR(15) | Y |  |  |
| 38 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(70) | Y |  |  |
| 39 | RAZAO_SOCIAL_ESTABELECIMENTO | VARCHAR2(100) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_CREDPIS_SALDO: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_CRED_PORBENS_GR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | DATA_INICIAL | DATE | Y |  |  |
| 8 | DATA_FINAL | DATE | Y |  |  |
| 9 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 10 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 11 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 12 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 13 | DATA_INI_CRED | DATE | Y |  |  |
| 14 | DATA_FIM_CRED | DATE | Y |  |  |
| 15 | DATA_LANCTO | DATE | Y |  |  |
| 16 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 18 | MES_ANO | VARCHAR2(7) | Y |  |  |
| 19 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(70) | Y |  |  |
| 20 | RAZAO_SOCIAL_ESTABELECIMENTO | VARCHAR2(100) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_CRED_PORBENS_GR: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_DAC_ANEXO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANEXO | VARCHAR2(10) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(40) | Y |  |  |

**PK**: ANEXO

---

## TMP_DAC_MODELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MODULO | VARCHAR2(6) | N |  |  |
| 2 | ANEXO | VARCHAR2(10) | N |  |  |
| 3 | IDENT_PESQUISA | NUMBER(12) | N |  |  |
| 4 | IND_TIPO | NUMBER(2) | Y |  |  |
| 5 | IND_NCM_21 | CHAR(1) | Y |  |  |
| 6 | IND_NCM_23 | CHAR(1) | Y |  |  |
| 7 | IND_NCM_24 | CHAR(1) | Y |  |  |
| 8 | IND_NCM_812 | CHAR(1) | Y |  |  |
| 9 | IND_NCM_815 | CHAR(1) | Y |  |  |
| 10 | IND_NF_42 | CHAR(1) | Y |  |  |
| 11 | IND_NF_814 | CHAR(1) | Y |  |  |
| 12 | IND_SALDO_815 | CHAR(1) | Y |  |  |
| 13 | IND_CONTA_815 | CHAR(1) | Y |  |  |

**PK**: MODULO, ANEXO, IDENT_PESQUISA

**FKs**:
- IDENT_PESQUISA → RGR_PESQUISA(IDENT_PESQUISA)
- ANEXO → TMP_DAC_ANEXO(ANEXO)

---

## TMP_DAC_MODELO_X_COLUNA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANEXO | VARCHAR2(10) | Y |  |  |
| 2 | IDENT_PESQUISA | NUMBER(12) | Y |  |  |
| 3 | IDENT_PARAM | NUMBER(12) | Y |  |  |
| 4 | INTEGRA_B | CHAR(1) | Y |  |  |
| 5 | INTEGRA_C | CHAR(1) | Y |  |  |
| 6 | INTEGRA_I | CHAR(1) | Y |  |  |
| 7 | TRIBUTO | VARCHAR2(10) | Y |  |  |
| 8 | TXT_CONS_IND | VARCHAR2(20) | Y |  |  |

**FKs**:
- ANEXO → TMP_DAC_ANEXO(ANEXO)
- IDENT_PESQUISA → RGR_PESQUISA(IDENT_PESQUISA)

---

## TMP_DAC_MODELO_X_LISTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANEXO | VARCHAR2(10) | N |  |  |
| 2 | IDENT_PESQUISA | NUMBER(12) | N |  |  |
| 3 | IDENT_PARAM | NUMBER(12) | N |  |  |
| 4 | TXT_CONS_IND | VARCHAR2(20) | Y |  |  |
| 5 | TXT_CONTRIB_FINAL | CHAR(1) | Y |  |  |

**PK**: ANEXO, IDENT_PESQUISA, IDENT_PARAM

**FKs**:
- ANEXO → TMP_DAC_ANEXO(ANEXO)
- IDENT_PESQUISA → RGR_PESQUISA(IDENT_PESQUISA)

---

## TMP_DAC_MODELO_X_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MODULO | VARCHAR2(6) | N |  |  |
| 2 | ANEXO | VARCHAR2(10) | N |  |  |
| 3 | IDENT_PESQUISA | NUMBER(12) | N |  |  |
| 4 | COD_PARAM | NUMBER(3) | N |  |  |

**PK**: MODULO, ANEXO, IDENT_PESQUISA, COD_PARAM

**FKs**:
- MODULO, ANEXO, IDENT_PESQUISA → TMP_DAC_MODELO(MODULO, ANEXO, IDENT_PESQUISA)

---

## TMP_DAC_TIPO_X_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MODULO | VARCHAR2(6) | N |  |  |
| 2 | COD_PARAM | NUMBER(3) | N |  |  |
| 3 | IND_TIPO | NUMBER(2) | N |  |  |

**PK**: MODULO, COD_PARAM, IND_TIPO

**FKs**:
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## TMP_DIMP_QTD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | REGISTRO | VARCHAR2(4) | Y |  |  |
| 2 | QTD | NUMBER(10) | Y |  |  |

---

## TMP_DIMP_REGISTROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | REGISTRO | VARCHAR2(4) | N |  |  |
| 2 | CHAVE | VARCHAR2(255) | N |  |  |
| 3 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: REGISTRO, CHAVE

---

## TMP_DWT_TRIB_ESP_REGRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 2 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 3 | DAT_VALIDADE_INI | DATE | Y |  |  |
| 4 | IND_PERIODICIDADE | CHAR(1) | Y |  |  |
| 5 | NUM_DIAS_CORR_ANT | NUMBER(3) | Y |  |  |
| 6 | NUM_DIAS_CORR_POS | NUMBER(3) | Y |  |  |
| 7 | NUM_DIAS_UTEIS | NUMBER(3) | Y |  |  |
| 8 | IND_ULT_DIA_UTIL | CHAR(1) | Y |  |  |
| 9 | COD_DARF | VARCHAR2(4) | Y |  |  |

---

## TMP_ECD_X2102_CONTAS_AGLUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | NUM_ORD | NUMBER(4) | N |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | N |  |  |
| 6 | IND_BALANCO_DRE | CHAR(1) | N |  |  |
| 7 | IND_NATUREZA | CHAR(1) | Y |  |  |
| 8 | IND_CLASSIF_DRE | CHAR(1) | Y |  |  |
| 9 | NIVEL | VARCHAR2(5) | N |  |  |
| 10 | CONTA | VARCHAR2(100) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | IND_UTIL_AGLUT | VARCHAR2(10) | N |  |  |

**Indexes**:
- IX_TMP_ECD_01: (COD_EMPRESA, COD_ESTAB, CONTA)

---

## TMP_EFD_SALDO_CRED_BEM_GR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | PERIODO | DATE | Y |  |  |
| 8 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 9 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 10 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 11 | DATA_INI_CRED | DATE | Y |  |  |
| 12 | DATA_FIM_CRED | DATE | Y |  |  |
| 13 | IND_PARCELA | NUMBER(3) | Y |  |  |
| 14 | NUM_PARCELA_CREDPIS | NUMBER(3) | Y |  |  |
| 15 | QT_PARC_A_CRED | NUMBER(3) | Y |  |  |
| 16 | DATA_LANCTO | DATE | Y |  |  |
| 17 | VLR_PIS_MENSAL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_COFINS_MENSAL | NUMBER(17,2) | Y |  |  |
| 19 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 20 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 21 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 22 | RAZAO_SOCIAL_FIS_JUR | VARCHAR2(70) | Y |  |  |
| 23 | DATA_AQUIS | DATE | Y |  |  |
| 24 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_PIS_CREDITADO | NUMBER(17,2) | Y |  |  |
| 27 | VLR_COFINS_CREDITADO | NUMBER(17,2) | Y |  |  |
| 28 | QT_PARCELAS_CREDITADO | NUMBER(3) | Y |  |  |
| 29 | VLR_PIS_CREDITAR | NUMBER(17,2) | Y |  |  |
| 30 | VLR_COFINS_CREDITAR | NUMBER(17,2) | Y |  |  |
| 31 | QT_PARCELAS_CREDITAR | NUMBER(3) | Y |  |  |
| 32 | SLD_CREDITAR_PIS | NUMBER(17,2) | Y |  |  |
| 33 | SLD_CREDITAR_COFINS | NUMBER(17,2) | Y |  |  |
| 34 | QTD_PARCELAS_SLD_CREDITAR | NUMBER(3) | Y |  |  |
| 35 | IND_BAIXA | CHAR(1) | Y |  |  |
| 36 | DAT_BAIXA | DATE | Y |  |  |
| 37 | MOTIVO_BAIXA | CHAR(15) | Y |  |  |
| 38 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(70) | Y |  |  |
| 39 | RAZAO_SOCIAL_ESTABELECIMENTO | VARCHAR2(100) | Y |  |  |
| 40 | TIPO_GERACAO | VARCHAR2(20) | Y |  |  |
| 41 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 42 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 43 | VLR_AQUISICAO | NUMBER(17,2) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_EFD_SALDO: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_EPC64

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | IND_NFC_E | CHAR(1) | Y |  |  |
| 7 | PROD_SERV | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, PROD_SERV

---

## TMP_EPC_APUR_REL_ANALITICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | Y |  |  |
| 2 | ORIGEM | VARCHAR2(20) | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | COD_RECEITA_BRUTA_PIS | VARCHAR2(100) | Y |  |  |
| 6 | COD_RECEITA_BRUTA_COFINS | VARCHAR2(100) | Y |  |  |
| 7 | DATA_FISCAL | DATE | Y |  |  |
| 8 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 9 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 16 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 17 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 18 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 19 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 21 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 22 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 24 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 25 | COD_SITUACAO_PIS_ST | NUMBER(2) | Y |  |  |
| 26 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 28 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 29 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 30 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 32 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 33 | COD_SITUACAO_COFINS_ST | NUMBER(2) | Y |  |  |
| 34 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 35 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 36 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 37 | NAT_BASE_CREDITO | VARCHAR2(100) | Y |  |  |
| 38 | COD_TIPO_CREDITO_PIS | VARCHAR2(100) | Y |  |  |
| 39 | COD_TIPO_CREDITO_COFINS | VARCHAR2(100) | Y |  |  |
| 40 | COD_MERCADO | VARCHAR2(1) | Y |  |  |
| 41 | GERADOR_RECEITA | VARCHAR2(1) | Y |  |  |
| 42 | IS_DEVOLUCAO | VARCHAR2(1) | Y |  |  |
| 43 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 44 | PARTICIPANTE | VARCHAR2(2) | Y |  |  |
| 45 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 46 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 47 | DESC_PROD_SERV | VARCHAR2(80) | Y |  |  |
| 48 | NCM_LEI116 | VARCHAR2(10) | Y |  |  |
| 49 | DESC_CONTA_CONTABIL | VARCHAR2(50) | Y |  |  |
| 50 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 51 | DESC_COD_CUSTO | VARCHAR2(50) | Y |  |  |

**Indexes**:
- IX_TMP_EPC_AP_REL_AN_PROC_ID: (PROC_ID)

---

## TMP_EPC_REL_DEV_COMPRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(15) | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(20) | Y |  |  |
| 5 | DATA_FISCAL | DATE | Y |  |  |
| 6 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 7 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 11 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 12 | QTD_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 15 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 16 | QTD_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 18 | IND_CAPA_ITEM | VARCHAR2(30) | Y |  |  |

**Indexes**:
- IDX_TMP_EPC_REL_DEV_COMP: (PROC_ID)

---

## TMP_EXEC_SAF_OL_DW

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOM_PACKAGE | VARCHAR2(50) | Y |  |  |
| 2 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 3 | NUM_LINHA | NUMBER(5) | Y |  |  |
| 4 | CAMPO_001 | VARCHAR2(1000) | Y |  |  |
| 5 | CAMPO_002 | VARCHAR2(1000) | Y |  |  |
| 6 | CAMPO_003 | VARCHAR2(1000) | Y |  |  |
| 7 | CAMPO_004 | VARCHAR2(1000) | Y |  |  |
| 8 | CAMPO_005 | VARCHAR2(1000) | Y |  |  |
| 9 | CAMPO_006 | VARCHAR2(1000) | Y |  |  |
| 10 | CAMPO_007 | VARCHAR2(1000) | Y |  |  |
| 11 | CAMPO_008 | VARCHAR2(1000) | Y |  |  |
| 12 | CAMPO_009 | VARCHAR2(1000) | Y |  |  |
| 13 | CAMPO_010 | VARCHAR2(1000) | Y |  |  |
| 14 | CAMPO_011 | VARCHAR2(1000) | Y |  |  |
| 15 | CAMPO_012 | VARCHAR2(1000) | Y |  |  |
| 16 | CAMPO_013 | VARCHAR2(1000) | Y |  |  |
| 17 | CAMPO_014 | VARCHAR2(1000) | Y |  |  |
| 18 | CAMPO_015 | VARCHAR2(1000) | Y |  |  |
| 19 | CAMPO_016 | VARCHAR2(1000) | Y |  |  |
| 20 | CAMPO_017 | VARCHAR2(1000) | Y |  |  |
| 21 | CAMPO_018 | VARCHAR2(1000) | Y |  |  |
| 22 | CAMPO_019 | VARCHAR2(1000) | Y |  |  |
| 23 | CAMPO_020 | VARCHAR2(1000) | Y |  |  |
| 24 | CAMPO_021 | VARCHAR2(1000) | Y |  |  |
| 25 | CAMPO_022 | VARCHAR2(1000) | Y |  |  |
| 26 | CAMPO_023 | VARCHAR2(1000) | Y |  |  |
| 27 | CAMPO_024 | VARCHAR2(1000) | Y |  |  |
| 28 | CAMPO_025 | VARCHAR2(1000) | Y |  |  |
| 29 | CAMPO_026 | VARCHAR2(1000) | Y |  |  |
| 30 | CAMPO_027 | VARCHAR2(1000) | Y |  |  |
| 31 | CAMPO_028 | VARCHAR2(1000) | Y |  |  |
| 32 | CAMPO_029 | VARCHAR2(1000) | Y |  |  |
| 33 | CAMPO_030 | VARCHAR2(1000) | Y |  |  |
| 34 | CAMPO_031 | VARCHAR2(1000) | Y |  |  |
| 35 | CAMPO_032 | VARCHAR2(1000) | Y |  |  |
| 36 | CAMPO_033 | VARCHAR2(1000) | Y |  |  |
| 37 | CAMPO_034 | VARCHAR2(1000) | Y |  |  |
| 38 | CAMPO_035 | VARCHAR2(1000) | Y |  |  |
| 39 | CAMPO_036 | VARCHAR2(1000) | Y |  |  |
| 40 | CAMPO_037 | VARCHAR2(1000) | Y |  |  |
| 41 | CAMPO_038 | VARCHAR2(1000) | Y |  |  |
| 42 | CAMPO_039 | VARCHAR2(1000) | Y |  |  |
| 43 | CAMPO_040 | VARCHAR2(1000) | Y |  |  |
| 44 | CAMPO_041 | VARCHAR2(1000) | Y |  |  |
| 45 | CAMPO_042 | VARCHAR2(1000) | Y |  |  |
| 46 | CAMPO_043 | VARCHAR2(1000) | Y |  |  |
| 47 | CAMPO_044 | VARCHAR2(1000) | Y |  |  |
| 48 | CAMPO_045 | VARCHAR2(1000) | Y |  |  |
| 49 | CAMPO_046 | VARCHAR2(1000) | Y |  |  |
| 50 | CAMPO_047 | VARCHAR2(1000) | Y |  |  |
| 51 | CAMPO_048 | VARCHAR2(1000) | Y |  |  |
| 52 | CAMPO_049 | VARCHAR2(1000) | Y |  |  |
| 53 | CAMPO_050 | VARCHAR2(1000) | Y |  |  |
| 54 | CAMPO_051 | VARCHAR2(1000) | Y |  |  |
| 55 | CAMPO_052 | VARCHAR2(1000) | Y |  |  |
| 56 | CAMPO_053 | VARCHAR2(1000) | Y |  |  |
| 57 | CAMPO_054 | VARCHAR2(1000) | Y |  |  |
| 58 | CAMPO_055 | VARCHAR2(1000) | Y |  |  |
| 59 | CAMPO_056 | VARCHAR2(1000) | Y |  |  |
| 60 | CAMPO_057 | VARCHAR2(1000) | Y |  |  |
| 61 | CAMPO_058 | VARCHAR2(1000) | Y |  |  |
| 62 | CAMPO_059 | VARCHAR2(1000) | Y |  |  |
| 63 | CAMPO_060 | VARCHAR2(1000) | Y |  |  |
| 64 | CAMPO_061 | VARCHAR2(1000) | Y |  |  |
| 65 | CAMPO_062 | VARCHAR2(1000) | Y |  |  |
| 66 | CAMPO_063 | VARCHAR2(1000) | Y |  |  |
| 67 | CAMPO_064 | VARCHAR2(1000) | Y |  |  |
| 68 | CAMPO_065 | VARCHAR2(1000) | Y |  |  |
| 69 | CAMPO_066 | VARCHAR2(1000) | Y |  |  |
| 70 | CAMPO_067 | VARCHAR2(1000) | Y |  |  |
| 71 | CAMPO_068 | VARCHAR2(1000) | Y |  |  |
| 72 | CAMPO_069 | VARCHAR2(1000) | Y |  |  |
| 73 | CAMPO_070 | VARCHAR2(1000) | Y |  |  |
| 74 | CAMPO_071 | VARCHAR2(1000) | Y |  |  |
| 75 | CAMPO_072 | VARCHAR2(1000) | Y |  |  |
| 76 | CAMPO_073 | VARCHAR2(1000) | Y |  |  |
| 77 | CAMPO_074 | VARCHAR2(1000) | Y |  |  |
| 78 | CAMPO_075 | VARCHAR2(1000) | Y |  |  |
| 79 | CAMPO_076 | VARCHAR2(1000) | Y |  |  |
| 80 | CAMPO_077 | VARCHAR2(1000) | Y |  |  |
| 81 | CAMPO_078 | VARCHAR2(1000) | Y |  |  |
| 82 | CAMPO_079 | VARCHAR2(1000) | Y |  |  |
| 83 | CAMPO_080 | VARCHAR2(1000) | Y |  |  |
| 84 | CAMPO_081 | VARCHAR2(1000) | Y |  |  |
| 85 | CAMPO_082 | VARCHAR2(1000) | Y |  |  |
| 86 | CAMPO_083 | VARCHAR2(1000) | Y |  |  |
| 87 | CAMPO_084 | VARCHAR2(1000) | Y |  |  |
| 88 | CAMPO_085 | VARCHAR2(1000) | Y |  |  |
| 89 | CAMPO_086 | VARCHAR2(1000) | Y |  |  |
| 90 | CAMPO_087 | VARCHAR2(1000) | Y |  |  |
| 91 | CAMPO_088 | VARCHAR2(1000) | Y |  |  |
| 92 | CAMPO_089 | VARCHAR2(1000) | Y |  |  |
| 93 | CAMPO_090 | VARCHAR2(1000) | Y |  |  |
| 94 | CAMPO_091 | VARCHAR2(1000) | Y |  |  |
| 95 | CAMPO_092 | VARCHAR2(1000) | Y |  |  |
| 96 | CAMPO_093 | VARCHAR2(1000) | Y |  |  |
| 97 | CAMPO_094 | VARCHAR2(1000) | Y |  |  |
| 98 | CAMPO_095 | VARCHAR2(1000) | Y |  |  |
| 99 | CAMPO_096 | VARCHAR2(1000) | Y |  |  |
| 100 | CAMPO_097 | VARCHAR2(1000) | Y |  |  |
| 101 | CAMPO_098 | VARCHAR2(1000) | Y |  |  |
| 102 | CAMPO_099 | VARCHAR2(1000) | Y |  |  |
| 103 | CAMPO_100 | VARCHAR2(1000) | Y |  |  |
| 104 | CAMPO_101 | VARCHAR2(1000) | Y |  |  |
| 105 | CAMPO_102 | VARCHAR2(1000) | Y |  |  |
| 106 | CAMPO_103 | VARCHAR2(1000) | Y |  |  |
| 107 | CAMPO_104 | VARCHAR2(1000) | Y |  |  |
| 108 | CAMPO_105 | VARCHAR2(1000) | Y |  |  |
| 109 | CAMPO_106 | VARCHAR2(1000) | Y |  |  |
| 110 | CAMPO_107 | VARCHAR2(1000) | Y |  |  |
| 111 | CAMPO_108 | VARCHAR2(1000) | Y |  |  |
| 112 | CAMPO_109 | VARCHAR2(1000) | Y |  |  |
| 113 | CAMPO_110 | VARCHAR2(1000) | Y |  |  |
| 114 | CAMPO_111 | VARCHAR2(1000) | Y |  |  |
| 115 | CAMPO_112 | VARCHAR2(1000) | Y |  |  |
| 116 | CAMPO_113 | VARCHAR2(1000) | Y |  |  |
| 117 | CAMPO_114 | VARCHAR2(1000) | Y |  |  |
| 118 | CAMPO_115 | VARCHAR2(1000) | Y |  |  |
| 119 | CAMPO_116 | VARCHAR2(1000) | Y |  |  |
| 120 | CAMPO_117 | VARCHAR2(1000) | Y |  |  |
| 121 | CAMPO_118 | VARCHAR2(1000) | Y |  |  |
| 122 | CAMPO_119 | VARCHAR2(1000) | Y |  |  |
| 123 | CAMPO_120 | VARCHAR2(1000) | Y |  |  |
| 124 | CAMPO_121 | VARCHAR2(1000) | Y |  |  |
| 125 | CAMPO_122 | VARCHAR2(1000) | Y |  |  |
| 126 | CAMPO_123 | VARCHAR2(1000) | Y |  |  |
| 127 | CAMPO_124 | VARCHAR2(1000) | Y |  |  |
| 128 | CAMPO_125 | VARCHAR2(1000) | Y |  |  |
| 129 | CAMPO_126 | VARCHAR2(1000) | Y |  |  |
| 130 | CAMPO_127 | VARCHAR2(1000) | Y |  |  |
| 131 | CAMPO_128 | VARCHAR2(1000) | Y |  |  |
| 132 | CAMPO_129 | VARCHAR2(1000) | Y |  |  |
| 133 | CAMPO_130 | VARCHAR2(1000) | Y |  |  |
| 134 | CAMPO_131 | VARCHAR2(1000) | Y |  |  |
| 135 | CAMPO_132 | VARCHAR2(1000) | Y |  |  |
| 136 | CAMPO_133 | VARCHAR2(1000) | Y |  |  |
| 137 | CAMPO_134 | VARCHAR2(1000) | Y |  |  |
| 138 | CAMPO_135 | VARCHAR2(1000) | Y |  |  |
| 139 | CAMPO_136 | VARCHAR2(1000) | Y |  |  |
| 140 | CAMPO_137 | VARCHAR2(1000) | Y |  |  |
| 141 | CAMPO_138 | VARCHAR2(1000) | Y |  |  |
| 142 | CAMPO_139 | VARCHAR2(1000) | Y |  |  |
| 143 | CAMPO_140 | VARCHAR2(1000) | Y |  |  |
| 144 | CAMPO_141 | VARCHAR2(1000) | Y |  |  |
| 145 | CAMPO_142 | VARCHAR2(1000) | Y |  |  |
| 146 | CAMPO_143 | VARCHAR2(1000) | Y |  |  |
| 147 | CAMPO_144 | VARCHAR2(1000) | Y |  |  |
| 148 | CAMPO_145 | VARCHAR2(1000) | Y |  |  |
| 149 | CAMPO_146 | VARCHAR2(1000) | Y |  |  |
| 150 | CAMPO_147 | VARCHAR2(1000) | Y |  |  |
| 151 | CAMPO_148 | VARCHAR2(1000) | Y |  |  |
| 152 | CAMPO_149 | VARCHAR2(1000) | Y |  |  |
| 153 | CAMPO_150 | VARCHAR2(1000) | Y |  |  |
| 154 | CAMPO_151 | VARCHAR2(1000) | Y |  |  |
| 155 | CAMPO_152 | VARCHAR2(1000) | Y |  |  |
| 156 | CAMPO_153 | VARCHAR2(1000) | Y |  |  |
| 157 | CAMPO_154 | VARCHAR2(1000) | Y |  |  |
| 158 | CAMPO_155 | VARCHAR2(1000) | Y |  |  |
| 159 | CAMPO_156 | VARCHAR2(1000) | Y |  |  |
| 160 | CAMPO_157 | VARCHAR2(1000) | Y |  |  |
| 161 | CAMPO_158 | VARCHAR2(1000) | Y |  |  |
| 162 | CAMPO_159 | VARCHAR2(1000) | Y |  |  |
| 163 | CAMPO_160 | VARCHAR2(1000) | Y |  |  |
| 164 | CAMPO_161 | VARCHAR2(1000) | Y |  |  |
| 165 | CAMPO_162 | VARCHAR2(1000) | Y |  |  |
| 166 | CAMPO_163 | VARCHAR2(1000) | Y |  |  |
| 167 | CAMPO_164 | VARCHAR2(1000) | Y |  |  |
| 168 | CAMPO_165 | VARCHAR2(1000) | Y |  |  |
| 169 | CAMPO_166 | VARCHAR2(1000) | Y |  |  |
| 170 | CAMPO_167 | VARCHAR2(1000) | Y |  |  |
| 171 | CAMPO_168 | VARCHAR2(1000) | Y |  |  |
| 172 | CAMPO_169 | VARCHAR2(1000) | Y |  |  |
| 173 | CAMPO_170 | VARCHAR2(1000) | Y |  |  |
| 174 | CAMPO_171 | VARCHAR2(1000) | Y |  |  |
| 175 | CAMPO_172 | VARCHAR2(1000) | Y |  |  |
| 176 | CAMPO_173 | VARCHAR2(1000) | Y |  |  |
| 177 | CAMPO_174 | VARCHAR2(1000) | Y |  |  |
| 178 | CAMPO_175 | VARCHAR2(1000) | Y |  |  |
| 179 | CAMPO_176 | VARCHAR2(1000) | Y |  |  |
| 180 | CAMPO_177 | VARCHAR2(1000) | Y |  |  |
| 181 | CAMPO_178 | VARCHAR2(1000) | Y |  |  |
| 182 | CAMPO_179 | VARCHAR2(1000) | Y |  |  |
| 183 | CAMPO_180 | VARCHAR2(1000) | Y |  |  |
| 184 | CAMPO_181 | VARCHAR2(1000) | Y |  |  |
| 185 | CAMPO_182 | VARCHAR2(1000) | Y |  |  |
| 186 | CAMPO_183 | VARCHAR2(1000) | Y |  |  |
| 187 | CAMPO_184 | VARCHAR2(1000) | Y |  |  |
| 188 | CAMPO_185 | VARCHAR2(1000) | Y |  |  |
| 189 | CAMPO_186 | VARCHAR2(1000) | Y |  |  |
| 190 | CAMPO_187 | VARCHAR2(1000) | Y |  |  |
| 191 | CAMPO_188 | VARCHAR2(1000) | Y |  |  |
| 192 | CAMPO_189 | VARCHAR2(1000) | Y |  |  |
| 193 | CAMPO_190 | VARCHAR2(1000) | Y |  |  |
| 194 | CAMPO_191 | VARCHAR2(1000) | Y |  |  |
| 195 | CAMPO_192 | VARCHAR2(1000) | Y |  |  |
| 196 | CAMPO_193 | VARCHAR2(1000) | Y |  |  |
| 197 | CAMPO_194 | VARCHAR2(1000) | Y |  |  |
| 198 | CAMPO_195 | VARCHAR2(1000) | Y |  |  |
| 199 | CAMPO_196 | VARCHAR2(1000) | Y |  |  |
| 200 | CAMPO_197 | VARCHAR2(1000) | Y |  |  |
| 201 | CAMPO_198 | VARCHAR2(1000) | Y |  |  |
| 202 | CAMPO_199 | VARCHAR2(1000) | Y |  |  |
| 203 | CAMPO_200 | VARCHAR2(1000) | Y |  |  |
| 204 | CAMPO_201 | VARCHAR2(1000) | Y |  |  |
| 205 | CAMPO_202 | VARCHAR2(1000) | Y |  |  |
| 206 | CAMPO_203 | VARCHAR2(1000) | Y |  |  |
| 207 | CAMPO_204 | VARCHAR2(1000) | Y |  |  |
| 208 | CAMPO_205 | VARCHAR2(1000) | Y |  |  |
| 209 | CAMPO_206 | VARCHAR2(1000) | Y |  |  |
| 210 | CAMPO_207 | VARCHAR2(1000) | Y |  |  |
| 211 | CAMPO_208 | VARCHAR2(1000) | Y |  |  |
| 212 | CAMPO_209 | VARCHAR2(1000) | Y |  |  |
| 213 | CAMPO_210 | VARCHAR2(1000) | Y |  |  |
| 214 | CAMPO_211 | VARCHAR2(1000) | Y |  |  |
| 215 | CAMPO_212 | VARCHAR2(1000) | Y |  |  |
| 216 | CAMPO_213 | VARCHAR2(1000) | Y |  |  |
| 217 | CAMPO_214 | VARCHAR2(1000) | Y |  |  |
| 218 | CAMPO_215 | VARCHAR2(1000) | Y |  |  |
| 219 | CAMPO_216 | VARCHAR2(1000) | Y |  |  |
| 220 | CAMPO_217 | VARCHAR2(1000) | Y |  |  |
| 221 | CAMPO_218 | VARCHAR2(1000) | Y |  |  |
| 222 | CAMPO_219 | VARCHAR2(1000) | Y |  |  |
| 223 | CAMPO_220 | VARCHAR2(1000) | Y |  |  |
| 224 | CAMPO_221 | VARCHAR2(1000) | Y |  |  |
| 225 | CAMPO_222 | VARCHAR2(1000) | Y |  |  |
| 226 | CAMPO_223 | VARCHAR2(1000) | Y |  |  |
| 227 | CAMPO_224 | VARCHAR2(1000) | Y |  |  |
| 228 | CAMPO_225 | VARCHAR2(1000) | Y |  |  |
| 229 | CAMPO_226 | VARCHAR2(1000) | Y |  |  |
| 230 | CAMPO_227 | VARCHAR2(1000) | Y |  |  |
| 231 | CAMPO_228 | VARCHAR2(1000) | Y |  |  |
| 232 | CAMPO_229 | VARCHAR2(1000) | Y |  |  |
| 233 | CAMPO_230 | VARCHAR2(1000) | Y |  |  |
| 234 | CAMPO_231 | VARCHAR2(1000) | Y |  |  |
| 235 | CAMPO_232 | VARCHAR2(1000) | Y |  |  |
| 236 | CAMPO_233 | VARCHAR2(1000) | Y |  |  |
| 237 | CAMPO_234 | VARCHAR2(1000) | Y |  |  |
| 238 | CAMPO_235 | VARCHAR2(1000) | Y |  |  |
| 239 | CAMPO_236 | VARCHAR2(1000) | Y |  |  |
| 240 | CAMPO_237 | VARCHAR2(1000) | Y |  |  |
| 241 | CAMPO_238 | VARCHAR2(1000) | Y |  |  |
| 242 | CAMPO_239 | VARCHAR2(1000) | Y |  |  |
| 243 | CAMPO_240 | VARCHAR2(1000) | Y |  |  |
| 244 | CAMPO_241 | VARCHAR2(1000) | Y |  |  |
| 245 | CAMPO_242 | VARCHAR2(1000) | Y |  |  |
| 246 | CAMPO_243 | VARCHAR2(1000) | Y |  |  |
| 247 | CAMPO_244 | VARCHAR2(1000) | Y |  |  |
| 248 | CAMPO_245 | VARCHAR2(1000) | Y |  |  |
| 249 | CAMPO_246 | VARCHAR2(1000) | Y |  |  |
| 250 | CAMPO_247 | VARCHAR2(1000) | Y |  |  |
| 251 | CAMPO_248 | VARCHAR2(1000) | Y |  |  |
| 252 | CAMPO_249 | VARCHAR2(1000) | Y |  |  |
| 253 | CAMPO_250 | VARCHAR2(1000) | Y |  |  |
| 254 | CAMPO_251 | VARCHAR2(1000) | Y |  |  |
| 255 | CAMPO_252 | VARCHAR2(1000) | Y |  |  |
| 256 | CAMPO_253 | VARCHAR2(1000) | Y |  |  |
| 257 | CAMPO_254 | VARCHAR2(1000) | Y |  |  |
| 258 | CAMPO_255 | VARCHAR2(1000) | Y |  |  |
| 259 | CAMPO_256 | VARCHAR2(1000) | Y |  |  |
| 260 | CAMPO_257 | VARCHAR2(1000) | Y |  |  |
| 261 | CAMPO_258 | VARCHAR2(1000) | Y |  |  |
| 262 | CAMPO_259 | VARCHAR2(1000) | Y |  |  |
| 263 | CAMPO_260 | VARCHAR2(1000) | Y |  |  |
| 264 | CAMPO_261 | VARCHAR2(1000) | Y |  |  |
| 265 | CAMPO_262 | VARCHAR2(1000) | Y |  |  |
| 266 | CAMPO_263 | VARCHAR2(1000) | Y |  |  |
| 267 | CAMPO_264 | VARCHAR2(1000) | Y |  |  |
| 268 | CAMPO_265 | VARCHAR2(1000) | Y |  |  |
| 269 | CAMPO_266 | VARCHAR2(1000) | Y |  |  |
| 270 | CAMPO_267 | VARCHAR2(1000) | Y |  |  |
| 271 | CAMPO_268 | VARCHAR2(1000) | Y |  |  |
| 272 | CAMPO_269 | VARCHAR2(1000) | Y |  |  |
| 273 | CAMPO_270 | VARCHAR2(1000) | Y |  |  |
| 274 | CAMPO_271 | VARCHAR2(1000) | Y |  |  |
| 275 | CAMPO_272 | VARCHAR2(1000) | Y |  |  |
| 276 | CAMPO_273 | VARCHAR2(1000) | Y |  |  |
| 277 | CAMPO_274 | VARCHAR2(1000) | Y |  |  |
| 278 | CAMPO_275 | VARCHAR2(1000) | Y |  |  |
| 279 | CAMPO_276 | VARCHAR2(1000) | Y |  |  |
| 280 | CAMPO_277 | VARCHAR2(1000) | Y |  |  |
| 281 | CAMPO_278 | VARCHAR2(1000) | Y |  |  |
| 282 | CAMPO_279 | VARCHAR2(1000) | Y |  |  |
| 283 | CAMPO_280 | VARCHAR2(1000) | Y |  |  |
| 284 | CAMPO_281 | VARCHAR2(1000) | Y |  |  |
| 285 | CAMPO_282 | VARCHAR2(1000) | Y |  |  |
| 286 | CAMPO_283 | VARCHAR2(1000) | Y |  |  |
| 287 | CAMPO_284 | VARCHAR2(1000) | Y |  |  |
| 288 | CAMPO_285 | VARCHAR2(1000) | Y |  |  |
| 289 | CAMPO_286 | VARCHAR2(1000) | Y |  |  |
| 290 | CAMPO_287 | VARCHAR2(1000) | Y |  |  |
| 291 | CAMPO_288 | VARCHAR2(1000) | Y |  |  |
| 292 | CAMPO_289 | VARCHAR2(1000) | Y |  |  |
| 293 | CAMPO_290 | VARCHAR2(1000) | Y |  |  |
| 294 | CAMPO_291 | VARCHAR2(1000) | Y |  |  |
| 295 | CAMPO_292 | VARCHAR2(1000) | Y |  |  |
| 296 | CAMPO_293 | VARCHAR2(1000) | Y |  |  |
| 297 | CAMPO_294 | VARCHAR2(1000) | Y |  |  |
| 298 | CAMPO_295 | VARCHAR2(1000) | Y |  |  |
| 299 | CAMPO_296 | VARCHAR2(1000) | Y |  |  |
| 300 | CAMPO_297 | VARCHAR2(1000) | Y |  |  |
| 301 | CAMPO_298 | VARCHAR2(1000) | Y |  |  |
| 302 | CAMPO_299 | VARCHAR2(1000) | Y |  |  |
| 303 | CAMPO_300 | VARCHAR2(1000) | Y |  |  |

---

## TMP_FCONT_BALANCETE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_SALDO | DATE | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 4 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 5 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 6 | COD_CONTA_REF | VARCHAR2(70) | N |  |  |
| 7 | GRUPO_CONTA_REF | VARCHAR2(9) | N |  |  |
| 8 | VLR_SALDO | NUMBER(17,2) | Y |  |  |
| 9 | IND_DEB_CRE | CHAR(1) | Y |  |  |

**Indexes**:
- IX_TMP_FCONT_BALANCETE (UNIQUE): (DATA_SALDO, COD_CONTA, GRUPO_CONTA, COD_CUSTO, GRUPO_CUSTO)

---

## TMP_ICMS_DIF_DOC_EX_RS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(70) | Y |  |  |
| 7 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 8 | DATA_INICIAL | DATE | Y |  |  |
| 9 | DATA_FINAL | DATE | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | COD_DOCTO | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(6) | Y |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 14 | DATA_FISCAL | DATE | Y |  |  |
| 15 | DATA_INTERN_AM | DATE | Y |  |  |
| 16 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 17 | COD_CFOP | VARCHAR2(6) | Y |  |  |
| 18 | COD_NATUREZA_OP | VARCHAR2(12) | Y |  |  |
| 19 | COD_ESTADO_ORIGEM | VARCHAR2(5) | Y |  |  |
| 20 | VLR_ALIQ_ORIGEM | NUMBER(19,4) | Y |  |  |
| 21 | VLR_ALIQ_DESTINO | NUMBER(19,4) | Y |  |  |
| 22 | DIF_ALIQ_TRIBUTO | NUMBER(19,4) | Y |  |  |
| 23 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 24 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMS_TRIBUTADO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMS_OUTRAS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ICMS_ISENTA_REDUCAO | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ICMS_RETIDO | NUMBER(17,2) | Y |  |  |
| 29 | VLR_ICMS_DEVIDO | NUMBER(17,2) | Y |  |  |
| 30 | VLR_ICMS_DESTACADO | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ICMS_DIF_ALIQ | NUMBER(17,2) | Y |  |  |
| 32 | VLR_BASE_CALC_ICMS | NUMBER(17,2) | Y |  |  |
| 33 | RAZAO_SOCIAL_ESTAB | VARCHAR2(100) | Y |  |  |
| 34 | CGC_ESTAB | VARCHAR2(14) | Y |  |  |
| 35 | PERIODO_COM_MOVIMENTO | VARCHAR2(50) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_ICMS_DOC_RS: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_IN86_BEM_ATIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_BEM | VARCHAR2(60) | N |  |  |
| 4 | COD_INC | VARCHAR2(6) | N |  |  |
| 5 | VALID_BEM | DATE | N |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | NUM_CAD_BEM | VARCHAR2(36) | Y |  |  |
| 8 | IND_NAT_BEM | VARCHAR2(1) | Y |  |  |
| 9 | NUM_BEM_INI | VARCHAR2(36) | Y |  |  |
| 10 | DESCR_BEM | VARCHAR2(100) | Y |  |  |
| 11 | CONTA_BEM | VARCHAR2(70) | Y |  |  |
| 12 | CONTA_DEPR | VARCHAR2(70) | Y |  |  |
| 13 | DATA_AQUIS | NUMBER(8) | Y |  |  |
| 14 | TIPO_DOCTO | VARCHAR2(5) | Y |  |  |
| 15 | SERIE_NF | VARCHAR2(3) | Y |  |  |
| 16 | SSERIE_NF | VARCHAR2(2) | Y |  |  |
| 17 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 18 | VLR_AQUIS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_REAIS | NUMBER(17,2) | Y |  |  |
| 20 | NUM_ARQUIV | VARCHAR2(50) | Y |  |  |
| 21 | DT_INI_DEPR | NUMBER(8) | Y |  |  |
| 22 | TX_DEPR | NUMBER(8,4) | Y |  |  |
| 23 | VLR_DEPR_ACUM | NUMBER(17,2) | Y |  |  |
| 24 | VLR_DEPR_PER | NUMBER(17,2) | Y |  |  |
| 25 | DT_BAIXA | NUMBER(8) | Y |  |  |
| 26 | ALMOZARIFAD | VARCHAR2(20) | Y |  |  |
| 27 | IDENT_CONTA_DEPR | NUMBER(12) | Y |  |  |
| 28 | IDENT_CONTA_CM | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM

---

## TMP_LANCTO_P9_NF
**Comment**: Tabela Temporária p/ auxiliar na geração das notas que compõe os lançamentos automáticos da Apuração do P9.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 13 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_DIFAL | NUMBER(17,2) | Y |  |  |
| 15 | ALIQ_DIFAL | NUMBER(7,4) | Y |  |  |
| 16 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## TMP_LISTA_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |

---

## TMP_MMAG_ACUMULA_REGISTRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | REGISTRO | VARCHAR2(10) | N |  |  |
| 3 | COD_ID | VARCHAR2(255) | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 5 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 6 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | COD_PRODUTO | VARCHAR2(65) | Y |  |  |
| 10 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | DATA_FISCAL | DATE | Y |  |  |
| 13 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 14 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 15 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 16 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: PROC_ID, REGISTRO, COD_ID

---

## TMP_MMAG_ECF
**Comment**: Tabela Temporária p/ geração da SAFR63

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_EMISSAO | DATE | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 5 | COD_SERV_MERC | VARCHAR2(40) | N |  |  |
| 6 | SEQ_REG | NUMBER(12) | N |  |  |
| 7 | COD_SIT_TRIB_PIS | NUMBER(2) | Y |  |  |
| 8 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 9 | VLR_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 10 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 11 | COD_SIT_TRIB_COFINS | NUMBER(2) | Y |  |  |
| 12 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 14 | VLR_COFINS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, COD_MODELO, COD_SERV_MERC, SEQ_REG

---

## TMP_MMAG_ECF_EMITER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_EMISSAO | DATE | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(20) | N |  |  |
| 5 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 6 | COD_SERV_MERC | VARCHAR2(50) | N |  |  |
| 7 | SEQ_REG | NUMBER(12) | N |  |  |
| 8 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 9 | VLR_ALIQ_PIS | NUMBER(8,4) | Y |  |  |
| 10 | VLR_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 11 | VLR_PIS_EXP | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PIS_TRIB | NUMBER(17,2) | Y |  |  |
| 13 | VLR_PIS_NTRIB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 15 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 16 | VLR_ALIQ_COFINS | NUMBER(8,4) | Y |  |  |
| 17 | VLR_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 18 | VLR_COFINS_EXP | NUMBER(17,2) | Y |  |  |
| 19 | VLR_COFINS_TRIB | NUMBER(17,2) | Y |  |  |
| 20 | VLR_COFINS_NTRIB | NUMBER(17,2) | Y |  |  |
| 21 | VLR_COFINS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, COD_FIS_JUR, COD_MODELO, COD_SERV_MERC, SEQ_REG

---

## TMP_MMAG_FIS_JUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |

**PK**: PROC_ID, IDENT_FIS_JUR

---

## TMP_MMAG_ISS_PFJ
**Comment**: Tabela utilizada nas obrigacoes municipais para armazenamento das pessoas fis/jur.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 5 | SEQ_ID | NUMBER(5) | Y |  |  |

**PK**: PROC_ID, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

**Indexes**:
- IX_TMP_MMAG_ISS_PFJ: (PROC_ID, IND_FIS_JUR, COD_FIS_JUR)

---

## TMP_MMAG_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 3 | COD_UNIDADE | VARCHAR2(8) | N | ' ' |  |

**PK**: PROC_ID, COD_PRODUTO, COD_UNIDADE

---

## TMP_MMAG_PRODUTO_88E

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: PROC_ID, COD_PRODUTO

---

## TMP_MMAG_PRODUTO_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 3 | ALIQUOTA | NUMBER(7,4) | N |  |  |
| 4 | QUANTIDADE | NUMBER | Y |  |  |
| 5 | VALOR_BRUTO | NUMBER | Y |  |  |
| 6 | VLR_BASE | NUMBER | Y |  |  |

**PK**: PROC_ID, COD_PRODUTO, ALIQUOTA

---

## TMP_MMAG_PROD_REG78

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 3 | VLR_PRECO_SUGER | NUMBER(17,2) | N |  |  |

**PK**: PROC_ID, COD_PRODUTO, VLR_PRECO_SUGER

---

## TMP_MMAG_REGISTRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | REGISTRO | VARCHAR2(10) | N |  |  |
| 3 | COD_ID | VARCHAR2(255) | N |  |  |

**PK**: PROC_ID, REGISTRO, COD_ID

---

## TMP_MMAG_SERVICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | IDENT_SERVICO | NUMBER(12) | N |  |  |

**PK**: PROC_ID, IDENT_SERVICO

---

## TMP_MMAG_TOTAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | TOT_REG50 | NUMBER | Y |  |  |
| 3 | TOT_REGM2 | NUMBER | Y |  |  |
| 4 | TOT_REG51 | NUMBER | Y |  |  |
| 5 | TOT_REG52 | NUMBER | Y |  |  |
| 6 | TOT_REG53 | NUMBER | Y |  |  |
| 7 | TOT_REG54 | NUMBER | Y |  |  |
| 8 | TOT_REG56 | NUMBER | Y |  |  |
| 9 | TOT_REG60 | NUMBER | Y |  |  |
| 10 | TOT_REG61 | NUMBER | Y |  |  |
| 11 | TOT_REG70 | NUMBER | Y |  |  |
| 12 | TOT_REG71 | NUMBER | Y |  |  |
| 13 | TOT_REG74 | NUMBER | Y |  |  |
| 14 | TOT_REG75 | NUMBER | Y |  |  |
| 15 | TOT_REG76 | NUMBER | Y |  |  |
| 16 | TOT_REG77 | NUMBER | Y |  |  |
| 17 | TOT_REG85 | NUMBER | Y |  |  |
| 18 | TOT_REG86 | NUMBER | Y |  |  |
| 19 | TOT_REG88 | NUMBER | Y |  |  |
| 20 | TOT_REG88C | NUMBER | Y |  |  |
| 21 | TOT_REG88D | NUMBER | Y |  |  |
| 22 | TOT_REG88E | NUMBER | Y |  |  |
| 23 | TOT_REG88Q | NUMBER | Y |  |  |
| 24 | TOT_REG88T | NUMBER | Y |  |  |
| 25 | TOT_REG88_50 | NUMBER | Y |  |  |
| 26 | TOT_REG88C_CAT95 | NUMBER | Y |  |  |
| 27 | TOT_REG88D_CAT95 | NUMBER | Y |  |  |
| 28 | TOT_REG88E_CAT95 | NUMBER | Y |  |  |
| 29 | TOT_REG88T_CAT95 | NUMBER | Y |  |  |
| 30 | STATUS | NUMBER | Y |  |  |
| 31 | DATA_INI | DATE | Y |  |  |
| 32 | DATA_FIM | DATE | Y |  |  |
| 33 | TEM_MOV_ENT | CHAR(1) | Y |  |  |
| 34 | TEM_MOV_SAI | CHAR(1) | Y |  |  |
| 35 | TOT_REG78 | NUMBER | Y | 0 | Atendimento ao novo registro especificado pela CAT 90/05 - SP |
| 36 | TOT_REG88A | NUMBER | Y |  |  |
| 37 | TOT_REG88MS | NUMBER | Y |  |  |
| 38 | TOT_REG57 | NUMBER | Y |  |  |

**PK**: PROC_ID

---

## TMP_MODELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MODULO | VARCHAR2(6) | N |  |  |
| 2 | ANEXO | VARCHAR2(10) | N |  |  |
| 3 | IDENT_PESQUISA | NUMBER(12) | N |  |  |
| 4 | IND_VALOR | CHAR(1) | Y |  |  |
| 5 | RELATID | NUMBER(12) | Y |  |  |
| 6 | ITEMID | NUMBER(12) | Y |  |  |
| 7 | IND_NCM_21 | CHAR(1) | Y |  |  |
| 8 | IND_NCM_23 | CHAR(1) | Y |  |  |
| 9 | IND_NCM_24 | CHAR(1) | Y |  |  |
| 10 | IND_NCM_812 | CHAR(1) | Y |  |  |
| 11 | IND_NCM_815 | CHAR(1) | Y |  |  |
| 12 | IND_NF_42 | CHAR(1) | Y |  |  |
| 13 | IND_NF_814 | CHAR(1) | Y |  |  |
| 14 | IND_SALDO_815 | CHAR(1) | Y |  |  |
| 15 | IND_CONTA_815 | CHAR(1) | Y |  |  |
| 16 | IND_DEV_VEND | CHAR(1) | Y |  |  |
| 17 | IND_DEV_COMP | CHAR(1) | Y |  |  |

**PK**: MODULO, ANEXO, IDENT_PESQUISA

**FKs**:
- IDENT_PESQUISA → RGR_PESQUISA(IDENT_PESQUISA)
- ANEXO → TMP_ANEXO(ANEXO)

---

## TMP_MODELO_X_COLUNA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANEXO | VARCHAR2(10) | Y |  |  |
| 2 | IDENT_PESQUISA | NUMBER(12) | Y |  |  |
| 3 | IDENT_PARAM | NUMBER(12) | Y |  |  |
| 4 | IND_MAIS_MENOS | CHAR(1) | Y |  |  |
| 5 | TRIBUTO | VARCHAR2(10) | Y |  |  |
| 6 | TXT_CONS_IND | VARCHAR2(20) | Y |  |  |
| 7 | TXT_SALDO_815 | VARCHAR2(20) | Y |  |  |

**FKs**:
- ANEXO → TMP_ANEXO(ANEXO)
- IDENT_PESQUISA → RGR_PESQUISA(IDENT_PESQUISA)

---

## TMP_MODELO_X_LISTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANEXO | VARCHAR2(10) | N |  |  |
| 2 | IDENT_PESQUISA | NUMBER(12) | N |  |  |
| 3 | IDENT_PARAM | NUMBER(12) | N |  |  |
| 4 | TXT_CONS_IND | VARCHAR2(20) | Y |  |  |
| 5 | TXT_CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 6 | TXT_CONTA_815 | VARCHAR2(10) | Y |  |  |

**PK**: ANEXO, IDENT_PESQUISA, IDENT_PARAM

**FKs**:
- ANEXO → TMP_ANEXO(ANEXO)
- IDENT_PESQUISA → RGR_PESQUISA(IDENT_PESQUISA)

---

## TMP_MODELO_X_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MODULO | VARCHAR2(6) | N |  |  |
| 2 | ANEXO | VARCHAR2(10) | N |  |  |
| 3 | IDENT_PESQUISA | NUMBER(12) | N |  |  |
| 4 | COD_PARAM | NUMBER(3) | N |  |  |

**PK**: MODULO, ANEXO, IDENT_PESQUISA, COD_PARAM

**FKs**:
- MODULO, ANEXO, IDENT_PESQUISA → TMP_MODELO(MODULO, ANEXO, IDENT_PESQUISA)

---

## TMP_NF_ENTR_CONFRONTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | REG | CHAR(3) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 5 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | NUM_ITEM | NUMBER(5) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 10 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 12 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 13 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 14 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 15 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 16 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 17 | IND_PRODUTO | CHAR(1) | N |  |  |
| 18 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 20 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 21 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMSS_FECEP | NUMBER(17,2) | Y |  |  |
| 24 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 25 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 26 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 27 | NUM_ITEM_REF | NUMBER(5) | Y |  |  |
| 28 | DATA_FISCAL_REF | DATE | Y |  |  |
| 29 | CAMPO_52_VLR_TRIB_ICMSS | VARCHAR2(1) | Y |  |  |
| 30 | COD_EMPRESA_ENT | VARCHAR2(3) | Y |  |  |
| 31 | COD_ESTAB_ENT | VARCHAR2(6) | Y |  |  |

**PK**: REG, COD_EMPRESA, COD_ESTAB, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, NUM_ITEM, DATA_FISCAL, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, IDENT_FIS_JUR

**Indexes**:
- IX_TMP_NF_ENTR_CONF_01: (COD_EMPRESA, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_FISCAL)

---

## TMP_NOTAS_AJUSTE_MASSA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 6 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 9 | NORM_DEV | VARCHAR2(1) | Y |  |  |

---

## TMP_PARAM_REL_DIFAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | Y |  |  |
| 4 | DATA_FIM | DATE | Y |  |  |
| 5 | IND_CENTR | VARCHAR2(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | IND_COM_DIFAL | VARCHAR2(1) | Y |  |  |
| 8 | IND_BASE_ISENTA | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## TMP_PARAM_REL_REINF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_TMP_PARAM_REL_REINF_1: (COD_EMPRESA, COD_ESTAB, COD_USUARIO, NUM_PROCESSO)

---

## TMP_PIM_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(54) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | Y |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL

---

## TMP_PORT63_I050

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTA | NUMBER(12) | N |  |  |

**PK**: IDENT_CONTA

---

## TMP_PRD_ANP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REF, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## TMP_REINF_CAD_MOV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROC | VARCHAR2(25) | N |  | Numero do Processo (R1070 - nrProc) |
| 2 | IND_TP_PROC | CHAR(1) | N |  | Tipo de Processo (R1070 - tpProc) Dominio: 1 - Administrativo 2 - Judicial  |
| 3 | VALID_PROC_INI | DATE | N |  | Validade Inicial (R1070 - iniValid) |
| 4 | VALID_PROC_FIM | DATE | Y |  | Validade Final (R1070 - fimValid) |
| 5 | GRUPO | VARCHAR2(9) | Y |  | Grupo do Processo |
| 6 | COD_EMPRESA | VARCHAR2(3) | N |  | Codigo da Empresa |
| 7 | COD_ESTAB | VARCHAR2(6) | N |  | Codigo do Estabelecimento Contribuinte |

---

## TMP_REINF_FAMILIA_4000

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_OC | NUMBER(12) | N |  |  |
| 2 | COD_EVENTO | VARCHAR2(6) | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | PROC_ID | NUMBER(12) | N |  |  |
| 5 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 6 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 10 | IND_USADO | VARCHAR2(1) | Y |  |  |

**Indexes**:
- IX_TMP_REINF_FAMILIA_4000_1: (COD_USUARIO, PROC_ID, IND_USADO)

---

## TMP_REINF_PGER_R2070

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PAGTO | VARCHAR2(4) | Y |  |  |
| 2 | COD_BENEF | VARCHAR2(50) | Y |  |  |
| 3 | IND_BENEF | CHAR(1) | Y |  |  |
| 4 | TP_INSCRICAO | CHAR(1) | Y |  |  |
| 5 | NR_INSCRICAO | VARCHAR2(14) | Y |  |  |
| 6 | NOME_BENEF | VARCHAR2(150) | Y |  |  |
| 7 | DAT_MOLESTIA | DATE | Y |  |  |
| 8 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 9 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 10 | CGC | VARCHAR2(14) | Y |  |  |
| 11 | DATA_MOVTO | DATE | Y |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 13 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 14 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 15 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 16 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 17 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 18 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 19 | TP_RENDIMENTO | VARCHAR2(3) | Y |  |  |
| 20 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |
| 21 | DATA_PAGTO | DATE | Y |  |  |
| 22 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 23 | IND_TIPO_ISENCAO | VARCHAR2(2) | Y |  |  |
| 24 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 25 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 26 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 27 | IND_CONTEM_COD | CHAR(1) | Y |  |  |
| 28 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 29 | ENDERECO | VARCHAR2(80) | Y |  |  |
| 30 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 31 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 32 | BAIRRO | VARCHAR2(60) | Y |  |  |
| 33 | CEP | VARCHAR2(12) | Y |  |  |
| 34 | CIDADE | VARCHAR2(30) | Y |  |  |
| 35 | IND_CLASSE_PFJ | VARCHAR2(2) | Y |  |  |
| 36 | IND_IDENTIF_FISCAL | CHAR(1) | Y |  |  |
| 37 | NUM_ID_FISCAL | VARCHAR2(30) | Y |  |  |
| 38 | TP_FONTE_PAGADORA | VARCHAR2(3) | Y |  |  |
| 39 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 40 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 41 | VLR_PREV_PRIVADA | NUMBER(17,2) | Y |  |  |
| 42 | VLR_PENS_ALIMENT | NUMBER(17,2) | Y |  |  |
| 43 | VLR_IR_RETIDO | NUMBER(17,2) | Y |  |  |
| 44 | VLR_SALARIO_13 | NUMBER(17,2) | Y |  |  |
| 45 | VLR_TRIBUTO_13 | NUMBER(17,2) | Y |  |  |
| 46 | VLR_OUTROS_TRIB_EXCL | NUMBER(17,2) | Y |  |  |
| 47 | VLR_DED_INSS_TERC | NUMBER(17,2) | Y |  |  |
| 48 | VLR_DED_DEP_TERC | NUMBER(17,2) | Y |  |  |
| 49 | VLR_AJUDA_CUSTO | NUMBER(17,2) | Y |  |  |
| 50 | VLR_OUTROS_DIRF | NUMBER(17,2) | Y |  |  |
| 51 | DSC_OUTROS_DIRF | VARCHAR2(50) | Y |  |  |
| 52 | VLR_APOSENT_ISENTA | NUMBER(17,2) | Y |  |  |
| 53 | VLR_LUCRO_PJ | NUMBER(17,2) | Y |  |  |
| 54 | VLR_VOLUNTARIO_COPA | NUMBER(17,2) | Y |  |  |
| 55 | VLR_VOLUNTARIO_COPA_13 | NUMBER(17,2) | Y |  |  |
| 56 | VLR_BOLSA_MEDICO_RESID | NUMBER(17,2) | Y |  |  |
| 57 | VLR_BOLSA_MEDICO_RESID_13 | NUMBER(17,2) | Y |  |  |

---

## TMP_REINF_PGER_R4010

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_FILIAL | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | IND_CENTRALIZADO | VARCHAR2(1) | Y |  |  |
| 5 | DATA_MOVTO | DATE | Y |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 12 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 13 | TP_INSCRICAO | VARCHAR2(1) | Y |  |  |
| 14 | NR_INSCRICAO | VARCHAR2(14) | Y |  |  |
| 15 | COD_NAT_REND | VARCHAR2(9) | Y |  |  |
| 16 | OBS_IDE_PGTO | VARCHAR2(200) | Y |  |  |
| 17 | NUM_CPF_BENEF | VARCHAR2(14) | Y |  |  |
| 18 | GRUPO_CPF_BENEF | VARCHAR2(9) | Y |  |  |
| 19 | IND_CPF_BENEF | VARCHAR2(1) | Y |  |  |
| 20 | COD_CPF_BENEF | VARCHAR2(14) | Y |  |  |
| 21 | NOM_BENEF | VARCHAR2(70) | Y |  |  |
| 22 | DSC_COMP_FP | VARCHAR2(7) | Y |  |  |
| 23 | IND_DEC_TERC | VARCHAR2(1) | Y |  |  |
| 24 | VLR_REND_BRUTO | NUMBER(17,2) | Y |  |  |
| 25 | VLR_REND_TRIB | NUMBER(17,2) | Y |  |  |
| 26 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 27 | IND_RRA | VARCHAR2(1) | Y |  |  |
| 28 | IND_FCI_SCP | VARCHAR2(1) | Y |  |  |
| 29 | NUM_INSCR_FCI_SCP | VARCHAR2(14) | Y |  |  |
| 30 | PERCENTUAL_SCP | NUMBER(4,1) | Y |  |  |
| 31 | IND_JUD | VARCHAR2(1) | Y |  |  |
| 32 | COD_PAIS_RESID_EXT | VARCHAR2(3) | Y |  |  |
| 33 | DATA_ESCR_CONT | DATE | Y |  |  |
| 34 | OBS_INFO_PGTO | VARCHAR2(200) | Y |  |  |
| 35 | IND_TP_LANCTO_DIRF | VARCHAR2(1) | Y |  |  |
| 36 | VLR_DED_INSS_TERC | NUMBER(17,2) | Y |  |  |
| 37 | VLR_PREV_PRIVADA | NUMBER(17,2) | Y |  |  |
| 38 | VLR_FAPI | NUMBER(17,2) | Y |  |  |
| 39 | VLR_FUNPRESP | NUMBER(17,2) | Y |  |  |
| 40 | VLR_PENS_ALIMENT | NUMBER(17,2) | Y |  |  |
| 41 | VLR_DED_DEP_TERC | NUMBER(17,2) | Y |  |  |
| 42 | NUM_INSC_PREV | VARCHAR2(14) | Y |  |  |
| 43 | NUM_INSC_FAPI | VARCHAR2(14) | Y |  |  |
| 44 | NUM_INSC_FUNPRESP | VARCHAR2(14) | Y |  |  |
| 45 | VLR_CONTRIB | NUMBER(17,2) | Y |  |  |
| 46 | IND_TP_ISENCAO | NUMBER(2) | Y |  |  |
| 47 | VLR_ISENCAO | NUMBER(17,2) | Y |  |  |
| 48 | DSC_RENDIMENTO | VARCHAR2(100) | Y |  |  |
| 49 | DATA_LAUDO | DATE | Y |  |  |
| 50 | IND_IDENTIF_FISCAL | VARCHAR2(1) | Y |  |  |
| 51 | NUM_ID_FISCAL | VARCHAR2(30) | Y |  |  |
| 52 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |
| 53 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 54 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 55 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 56 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 57 | CIDADE | VARCHAR2(30) | Y |  |  |
| 58 | DSC_PROVINCIA_EX | VARCHAR2(40) | Y |  |  |
| 59 | CEP | VARCHAR2(8) | Y |  |  |
| 60 | TELEFONE | VARCHAR2(15) | Y |  |  |
| 61 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 62 | IND_CLASSE_PFJ | VARCHAR2(2) | Y |  |  |
| 63 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 64 | IND_TIPO_ISENCAO | VARCHAR2(2) | Y |  |  |
| 65 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 66 | OBS_INFO_PGTO_COMUM | VARCHAR2(200) | Y |  |  |
| 67 | OBS_IDE_PGTO_COMUM | VARCHAR2(200) | Y |  |  |
| 68 | DSC_COMP_FP_COMUM | VARCHAR2(7) | Y |  |  |
| 69 | IND_DEC_TERC_COMUM | VARCHAR2(1) | Y |  |  |
| 70 | IND_RRA_COMUM | VARCHAR2(1) | Y |  |  |
| 71 | IND_FCI_SCP_COMUM | VARCHAR2(1) | Y |  |  |
| 72 | NUM_INSCR_FCI_SCP_COMUM | VARCHAR2(14) | Y |  |  |
| 73 | PERCENTUAL_SCP_COMUM | NUMBER(4,1) | Y |  |  |
| 74 | IND_JUD_COMUM | VARCHAR2(1) | Y |  |  |
| 75 | COD_PAIS_RESID_EXT_COMUM | VARCHAR2(3) | Y |  |  |
| 76 | DATA_ESCR_CONT_COMUM | DATE | Y |  |  |
| 77 | COD_DARF_COMUM | VARCHAR2(4) | Y |  |  |
| 78 | DATA_LAUDO_COMUM | DATE | Y |  |  |
| 79 | IDENT_FIS_JUR_COMUM | NUMBER(12) | Y |  |  |
| 80 | IDENT_DOCTO_COMUM | NUMBER(12) | Y |  |  |
| 81 | IDENT_DARF_COMUM | NUMBER(12) | Y |  |  |
| 82 | NUM_LINHA | NUMBER(14) | Y |  |  |
| 83 | NUM_LINHA_COMUM | NUMBER(14) | Y |  |  |
| 84 | VLR_DESC_SIMPL_MENSAL | NUMBER(17,2) | Y |  |  |
| 85 | DATA_MOVTO_REAL | DATE | Y |  |  |
| 86 | DATA_COMPETENCIA | DATE | Y |  |  |

**Indexes**:
- IX_TMP_REINF_PGER_R4010_1: (TP_INSCRICAO, NR_INSCRICAO, COD_NAT_REND, DATA_MOVTO, NUM_CPF_BENEF, GRUPO_CPF_BENEF, IND_CPF_BENEF, COD_CPF_BENEF, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO)
- IX_TMP_REINF_PGER_R4010_2: (NUM_CPF_BENEF, TP_INSCRICAO, NR_INSCRICAO, COD_NAT_REND, DATA_MOVTO, NUM_LINHA)

---

## TMP_REINF_PGER_R4020

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_FILIAL | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | IND_CENTRALIZADO | VARCHAR2(1) | Y |  |  |
| 5 | DATA_MOVTO | DATE | Y |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 12 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 13 | TP_INSCRICAO | VARCHAR2(1) | Y |  |  |
| 14 | NR_INSCRICAO | VARCHAR2(14) | Y |  |  |
| 15 | COD_NAT_JUR | VARCHAR2(4) | Y |  |  |
| 16 | COD_NAT_REND | VARCHAR2(9) | Y |  |  |
| 17 | OBS_IDE_PGTO | VARCHAR2(200) | Y |  |  |
| 18 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 19 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 20 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 21 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 22 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 23 | IND_ISENTO_IMUNE | VARCHAR2(1) | Y |  |  |
| 24 | IDENT_EVENTO_ADICIONAL | VARCHAR2(8) | Y |  |  |
| 25 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 26 | IND_FCI_SCP | VARCHAR2(1) | Y |  |  |
| 27 | NUM_INSCR_FCI_SCP | VARCHAR2(14) | Y |  |  |
| 28 | PERCENTUAL_SCP | NUMBER(5,1) | Y |  |  |
| 29 | IND_JUD | VARCHAR2(1) | Y |  |  |
| 30 | COD_PAIS_RESID_EXT | VARCHAR2(3) | Y |  |  |
| 31 | DATA_ESCR_CONT | DATE | Y |  |  |
| 32 | OBS_INFO_PGTO | VARCHAR2(200) | Y |  |  |
| 33 | IND_CLASSE_PFJ | VARCHAR2(2) | Y |  |  |
| 34 | IND_IDENTIF_FISCAL | VARCHAR2(1) | Y |  |  |
| 35 | NUM_ID_FISCAL | VARCHAR2(30) | Y |  |  |
| 36 | TP_FONTE_PAGADORA | VARCHAR2(3) | Y |  |  |
| 37 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |
| 38 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 39 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 40 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 41 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 42 | CIDADE | VARCHAR2(30) | Y |  |  |
| 43 | DSC_PROVINCIA_EX | VARCHAR2(40) | Y |  |  |
| 44 | CEP | VARCHAR2(8) | Y |  |  |
| 45 | TELEFONE | VARCHAR2(15) | Y |  |  |
| 46 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 47 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 48 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 49 | VLR_BRUTO_RETEN | NUMBER(17,2) | Y |  |  |
| 50 | VLR_IR_RETIDO | NUMBER(17,2) | Y |  |  |
| 51 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 52 | OBS_IDE_PGTO_COMUM | VARCHAR2(200) | Y |  |  |
| 53 | IND_FCI_SCP_COMUM | VARCHAR2(1) | Y |  |  |
| 54 | NUM_INSCR_FCI_SCP_COMUM | VARCHAR2(14) | Y |  |  |
| 55 | PERCENTUAL_SCP_COMUM | NUMBER(5,1) | Y |  |  |
| 56 | IND_JUD_COMUM | VARCHAR2(1) | Y |  |  |
| 57 | COD_PAIS_RESID_EXT_COMUM | VARCHAR2(3) | Y |  |  |
| 58 | DATA_ESCR_CONT_COMUM | DATE | Y |  |  |
| 59 | OBS_INFO_PGTO_COMUM | VARCHAR2(200) | Y |  |  |
| 60 | IND_ISENTO_IMUNE_COMUM | VARCHAR2(1) | Y |  |  |
| 61 | TP_FONTE_PAGADORA_COMUM | VARCHAR2(3) | Y |  |  |
| 62 | TP_TRIBUTACAO_IR_COMUM | VARCHAR2(2) | Y |  |  |
| 63 | VLR_BRUTO_COMUM | NUMBER(17,2) | Y |  |  |
| 64 | NUM_LINHA | NUMBER(14) | Y |  |  |
| 65 | NUM_LINHA_COMUM | NUMBER(14) | Y |  |  |
| 66 | DSC_TRIBUTO | VARCHAR2(10) | Y |  |  |
| 67 | IND_REGRA_AGREGADO | VARCHAR2(1) | Y |  |  |
| 68 | DATA_MOVTO_REAL | DATE | Y |  |  |
| 69 | DATA_COMPETENCIA | DATE | Y |  |  |

**Indexes**:
- IX_TMP_REINF_PGER_R4020_1: (TP_INSCRICAO, NR_INSCRICAO, COD_NAT_REND, DATA_MOVTO, CPF_CGC, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO)
- IX_TMP_REINF_PGER_R4020_2: (CPF_CGC, TP_INSCRICAO, NR_INSCRICAO, COD_NAT_REND, DATA_MOVTO, NUM_LINHA)
- IX_TMP_REINF_PGER_R4020_3: (NUM_LINHA)

---

## TMP_REL_DOC_FIS_ISS_EXCEL_GR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | RAZAO_SOCIAL_ESTAB | VARCHAR2(100) | Y |  |  |
| 5 | CNPJ | VARCHAR2(4000) | Y |  |  |
| 6 | MOVIMENTO | VARCHAR2(1) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(60) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | DATA_FISCAL | DATE | Y |  |  |
| 13 | DATA_PAGTO | DATE | Y |  |  |
| 14 | CGC_CPF_FIS_JUR | VARCHAR2(4000) | Y |  |  |
| 15 | RAZAO_SOCIAL_FIS_JUR | VARCHAR2(70) | Y |  |  |
| 16 | COD_ESTADO_FIS_JUR | VARCHAR2(2) | Y |  |  |
| 17 | MUNICIPIO_FIS_JUR | VARCHAR2(50) | Y |  |  |
| 18 | NUM_ITEM | NUMBER | Y |  |  |
| 19 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 20 | DSC_SERVICO | VARCHAR2(50) | Y |  |  |
| 21 | COD_SERV_LEI_116 | VARCHAR2(4) | Y |  |  |
| 22 | DSC_SERV_LEI_116 | VARCHAR2(100) | Y |  |  |
| 23 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 24 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 26 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 28 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |
| 29 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ALIQ_ISS_RETIDO | NUMBER(7,4) | Y |  |  |
| 32 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BASE_IR | NUMBER(17,2) | Y |  |  |
| 34 | ALIQ_TRIBUTO_IR | NUMBER(7,4) | Y |  |  |
| 35 | VLR_TRIBUTO_IR | NUMBER(17,2) | Y |  |  |
| 36 | CST_PIS | NUMBER(2) | Y |  |  |
| 37 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 38 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 39 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 40 | CST_COFINS | NUMBER(2) | Y |  |  |
| 41 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 42 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 43 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 44 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 45 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 46 | SITUACAO | VARCHAR2(9) | Y |  |  |
| 47 | COD_USUARIO | VARCHAR2(50) | Y |  |  |
| 48 | COD_CLASS_DOC_FIS | VARCHAR2(1) | Y |  |  |
| 49 | COD_ATIV_RJ | NUMBER(7) | Y |  |  |
| 50 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |

**Indexes**:
- IX_REL_DOC_FIS_ISS: (PROC_ID)

---

## TMP_REL_FICHA3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_PERIODO | DATE | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(63) | Y |  |  |
| 5 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 6 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 7 | QTD_SLD | NUMBER(17,3) | Y |  |  |
| 8 | VLR_TOT_SLD | NUMBER(17,2) | Y |  |  |
| 9 | VLR_UNIT_SLD | NUMBER(19,6) | Y |  |  |
| 10 | NUM_ORDEM | NUMBER(9) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 13 | NUM_SERIE_ECF | VARCHAR2(21) | Y |  |  |
| 14 | TIPO_DOCTO | VARCHAR2(40) | Y |  |  |
| 15 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 16 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 17 | COD_FIS_JUR | VARCHAR2(17) | Y |  |  |
| 18 | CFOP | VARCHAR2(4) | Y |  |  |
| 19 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 20 | QTD_ENTRADA | NUMBER(17,3) | Y |  |  |
| 21 | VLR_ICMS_ENT | NUMBER(17,2) | Y |  |  |
| 22 | QTD_SAIDA | NUMBER(17,3) | Y |  |  |
| 23 | VLR_UNIT | NUMBER(19,6) | Y |  |  |
| 24 | VLR_SAIDA_CONS_USU_FIN | NUMBER(17,2) | Y |  |  |
| 25 | VLR_SAIDA_FATO_N_REAL | NUMBER(17,2) | Y |  |  |
| 26 | VLR_SAIDA_SUB_ISEN | NUMBER(17,2) | Y |  |  |
| 27 | VLR_SAIDA_OUTRO_ESTADO | NUMBER(17,2) | Y |  |  |
| 28 | VLR_SAIDA_COMERC_SUB | NUMBER(17,2) | Y |  |  |
| 29 | VLR_CONF_SAIDA | NUMBER(17,2) | Y |  |  |
| 30 | VLR_CONF_ENT | NUMBER(17,2) | Y |  |  |
| 31 | QTDE_SALDO | NUMBER(17,3) | Y |  |  |
| 32 | VLR_UNIT_SALDO | NUMBER(19,6) | Y |  |  |
| 33 | VLR_TOT_SALDO | NUMBER(17,2) | Y |  |  |
| 34 | VLR_RESSARC | NUMBER(17,2) | Y |  |  |
| 35 | VLR_COMPL | NUMBER(17,2) | Y |  |  |
| 36 | VLR_ICMS_PROP | NUMBER(17,2) | Y |  |  |
| 37 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 38 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 39 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 40 | IND_NOTA_DEVOL | CHAR(1) | Y |  |  |
| 41 | COD_ENQ_LEGAL | CHAR(1) | Y |  |  |
| 42 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 43 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 44 | DESC_PROD | VARCHAR2(50) | Y |  |  |
| 45 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 46 | USUARIO | VARCHAR2(40) | Y |  |  |

---

## TMP_REL_IPI_NDESC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO_DATA | VARCHAR2(255) | N |  | PK da tabela, composta pelo USER_ID \|\| to_char(SYSDATE, YYYYMMDDHHMISS ) |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IND_CENTR | CHAR(1) | Y | 'D' |  "C" - Centralizado / "D" - Descentralizado |
| 5 | IDENT_ESTADO | NUMBER(12) | Y |  |  |

**PK**: USUARIO_DATA, COD_EMPRESA, COD_ESTAB

---

## TMP_REL_LIVRO_DIARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_LANCTO | DATE | Y |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 6 | DESC_CONTA | VARCHAR2(50) | Y |  |  |
| 7 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 8 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 9 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 10 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 11 | IDENT_DESPESA | NUMBER(12) | Y |  |  |
| 12 | COD_DESPESA | VARCHAR2(20) | Y |  |  |
| 13 | IDENT_HISTPADRAO | NUMBER(12) | Y |  |  |
| 14 | COD_HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 15 | DESC_HISTPADRAO | VARCHAR2(50) | Y |  |  |
| 16 | TXT_HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 17 | VLR_LANCTO | NUMBER(19,2) | Y |  |  |
| 18 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 19 | CGC | VARCHAR2(14) | Y |  |  |
| 20 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 21 | VLR_TOT_CREDITO | NUMBER(19,2) | Y |  |  |
| 22 | VLR_TOT_DEBITO | NUMBER(19,2) | Y |  |  |
| 23 | VLR_TRANSP_DEB | NUMBER(19,2) | Y |  |  |
| 24 | VLR_TRANSP_CRED | NUMBER(19,2) | Y |  |  |
| 25 | NUM_SEQ | NUMBER(17) | Y |  |  |

**Indexes**:
- IX_TMP_REL_LIVRO_DIARIO: (NUM_SEQ)

---

## TMP_REL_LIVRO_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 6 | DAT_APURACAO | DATE | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | DATA_FISCAL | DATE | Y |  |  |
| 14 | DATA_EMISSAO | DATE | Y |  |  |
| 15 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 16 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 17 | COD_TRIBUTACAO | VARCHAR2(1) | Y |  |  |
| 18 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 19 | SITUACAO | CHAR(1) | Y |  |  |
| 20 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 21 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 22 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 23 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 24 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 26 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 27 | SEQ_OBS | NUMBER(12) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 30 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 31 | ESTAB_RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 32 | ESTAB_CGC | VARCHAR2(14) | Y |  |  |
| 33 | ESTAB_INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 34 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 35 | IND_MERC_SERV | CHAR(1) | Y |  |  |
| 36 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 37 | DATA_EMISSAO_FIM | DATE | Y |  |  |
| 38 | NUM_ORDEM | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_TMP_REL_LIVRO_P1: (NUM_ORDEM)

---

## TMP_REL_LIVRO_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | TIPO_RESUMO | VARCHAR2(5) | Y |  |  |
| 8 | IND_MERC_SERV | CHAR(1) | Y |  |  |
| 9 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 10 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 11 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 12 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 13 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 16 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 17 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 18 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 19 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 20 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 21 | DATA_EMISSAO | DATE | Y |  |  |
| 22 | DATA_EMISSAO_FIM | DATE | Y |  |  |
| 23 | DATA_FISCAL | DATE | Y |  |  |
| 24 | DESC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 25 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 26 | DSC_TRIB_INT | VARCHAR2(100) | Y |  |  |
| 27 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 28 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 29 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 30 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 31 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 32 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |
| 33 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 34 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 35 | NORM_DEV | CHAR(1) | Y |  |  |
| 36 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 37 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 38 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 39 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 40 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 41 | SEQ_OBS | NUMBER(12) | Y |  |  |
| 42 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 43 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 44 | SITUACAO | CHAR(1) | Y |  |  |
| 45 | USUARIO | VARCHAR2(40) | Y |  |  |
| 46 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 47 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 48 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 49 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 50 | VLR_BASE1 | NUMBER(17,2) | Y |  |  |
| 51 | VLR_BASE2 | NUMBER(17,2) | Y |  |  |
| 52 | VLR_BASE3 | NUMBER(17,2) | Y |  |  |
| 53 | VLR_BASE4 | NUMBER(17,2) | Y |  |  |
| 54 | VLR_CONT_CONTR | NUMBER(17,2) | Y |  |  |
| 55 | VLR_CONT_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 56 | VLR_BASE_CONTR | NUMBER(17,2) | Y |  |  |
| 57 | VLR_BASE_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 58 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 59 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 60 | VLR_ISENTAS_ICMS | NUMBER(17,2) | Y |  |  |
| 61 | VLR_OUTRAS_ICMS | NUMBER(17,2) | Y |  |  |
| 62 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 63 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 64 | VLR_ISENTAS_IPI | NUMBER(17,2) | Y |  |  |
| 65 | VLR_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |
| 66 | VLR_ST | NUMBER(17,2) | Y |  |  |
| 67 | VLR_ST_D_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 68 | VLR_ST_DENTRO_UF | NUMBER(17,2) | Y |  |  |
| 69 | VLR_ST_F_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 70 | VLR_ST_FORA_UF | NUMBER(17,2) | Y |  |  |
| 71 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 72 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 73 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 74 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 75 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 76 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 77 | COD_TRIBUT_IPI | CHAR(1) | Y |  |  |
| 78 | VLR_ICMSS_PET_ENER | NUMBER(17,2) | Y |  |  |
| 79 | VLR_ICMSS_OUTROS_PRODS | NUMBER(17,2) | Y |  |  |
| 80 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 81 | RAZAO_SOCIAL_FIS_JUR | VARCHAR2(70) | Y |  |  |
| 82 | ESTAB_RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 83 | ESTAB_CGC | VARCHAR2(14) | Y |  |  |
| 84 | ESTAB_INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 85 | NUM_ORDEM | NUMBER(7) | Y |  |  |

**Indexes**:
- IX_TMP_REL_LIVRO_P2: (NUM_ORDEM)

---

## TMP_REL_LUCRO_PRESUM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | Y |  |  |
| 2 | ORIGEM | VARCHAR2(10) | Y |  |  |
| 3 | TIPO_APURACAO | CHAR(1) | Y |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 6 | IDENT_CONTA | VARCHAR2(50) | Y |  |  |
| 7 | DATA_LANCTO | DATE | Y |  |  |
| 8 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 9 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 10 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_COFINS | NUMBER | Y |  |  |
| 13 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 15 | DESCR_AGRUPAMENTO | VARCHAR2(80) | Y |  |  |
| 16 | COD_AGRUP | VARCHAR2(10) | Y |  |  |
| 17 | NUM_ORDEM | NUMBER | Y |  |  |

---

## TMP_REL_MODELO03
**Comment**: Tabela para armazenar do dados do livro Modelo III - Grandes Volumes. Modulo Estadual - Ressarcimento e Complemento.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 10 | IND_PRODUTO | CHAR(1) | N |  |  |
| 11 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 12 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 13 | QTD_E_S | NUMBER(13,3) | Y |  |  |
| 14 | VLR_UNIT_SAIDA | NUMBER(18,4) | Y |  |  |
| 15 | VLR_SAI_USU_FINAL | NUMBER(17,2) | Y |  |  |
| 16 | VLR_NAO_RALIZ | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SAI_OUT_UF | NUMBER(17,2) | Y |  |  |
| 19 | VLR_SAI_COM_S | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_S_VC | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_E_VC | NUMBER(17,2) | Y |  |  |
| 22 | QTD_SALDOS | NUMBER(13,3) | Y |  |  |
| 23 | VLR_UNIT_SALDO | NUMBER(18,4) | Y |  |  |
| 24 | VLR_TOT_SALDO | NUMBER(17,2) | Y |  |  |
| 25 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 26 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 27 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 28 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 29 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 30 | QTD_SALDO | NUMBER(13,3) | Y |  |  |
| 31 | VLR_TOT | NUMBER(13,2) | Y |  |  |
| 32 | VLR_UNIT | NUMBER(15,4) | Y |  |  |
| 33 | SALDO_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 34 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 35 | NUM_LINHA | NUMBER(10) | Y |  |  |
| 36 | QTD_SALDO_ANT | NUMBER(13,3) | Y |  |  |
| 37 | VLR_TOT_ANT | NUMBER(13,2) | Y |  |  |
| 38 | VLR_UNIT_ANT | NUMBER(15,4) | Y |  |  |
| 39 | TEXTO_SALDO | VARCHAR2(20) | Y |  |  |
| 40 | NUM_ORDEM_PRODUTO | NUMBER(10) | Y |  |  |
| 41 | PROC_ID | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_PRODUTO, IND_PRODUTO, COD_PRODUTO

**Indexes**:
- IX_TMP_REL_MODELO03: (PROC_ID, NUM_ORDEM_PRODUTO)

---

## TMP_REL_VALIDA_SEQ_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(50) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | TIPO_REL | VARCHAR2(1) | N |  |  |
| 6 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 7 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 8 | MOVTO_E_S | VARCHAR2(3) | Y |  |  |
| 9 | DATA_INI | DATE | Y |  |  |
| 10 | DATA_FIM | DATE | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 14 | NUM_DOCTO_MENOR | VARCHAR2(12) | Y |  |  |
| 15 | NUM_DOCTO_MAIOR | VARCHAR2(12) | Y |  |  |
| 16 | NUM_DOCTO_AUSENTE | VARCHAR2(12) | Y |  |  |
| 17 | QTD_LIDOS | NUMBER(12) | Y |  |  |
| 18 | QTD_INEXISTENTE | NUMBER(12) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ, TIPO_REL

**Indexes**:
- IX_TMP_REL_VALIDA_SEQ_DOCTO_01: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_RESSARC_INV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | DATA_INVENTARIO | DATE | N |  |  |
| 7 | FATOR | NUMBER | N |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 10 | QUANTIDADE | NUMBER | Y |  |  |
| 11 | VLR_ICMS_MEDIO | NUMBER | Y |  |  |
| 12 | VLR_ICMSS_MEDIO | NUMBER | Y |  |  |
| 13 | VLR_BASE_ICMSS_MEDIO | NUMBER | Y |  |  |
| 14 | VLR_FCP_MEDIO | NUMBER | Y |  |  |
| 15 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 16 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, FATOR, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## TMP_RESSARC_MG_C180

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_FISCAL | DATE | Y |  |  |
| 2 | GRUPO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 3 | IND_PROD_PRINC | CHAR(1) | Y |  |  |
| 4 | COD_PROD_PRINC | VARCHAR2(60) | Y |  |  |
| 5 | QTD_CONV_ENT_MP | NUMBER | Y |  |  |
| 6 | VLR_ICMS_ENT_MP | NUMBER | Y |  |  |
| 7 | VLR_ICMS_ST_ENT_MP | NUMBER | Y |  |  |
| 8 | VLR_BC_ST_ENT_MP | NUMBER | Y |  |  |
| 9 | VLR_FECEP_ST_ENT_MP | NUMBER | Y |  |  |

**Indexes**:
- IX_TMP_RESSARC_MG_C180: (COD_PROD_PRINC, DATA_FISCAL, IND_PROD_PRINC, GRUPO_PROD_PRINC)

---

## TMP_RESSARC_MG_C186

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_FISCAL | DATE | Y |  |  |
| 2 | GRUPO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 3 | IND_PROD_PRINC | CHAR(1) | Y |  |  |
| 4 | COD_PROD_PRINC | VARCHAR2(60) | Y |  |  |
| 5 | QTD_CONV_DEV_ENT_MP | NUMBER | Y |  |  |
| 6 | VLR_ICMS_DEV_ENT_MP | NUMBER | Y |  |  |
| 7 | VLR_ICMS_ST_DEV_ENT_MP | NUMBER | Y |  |  |
| 8 | VLR_BC_ST_DEV_ENT_MP | NUMBER | Y |  |  |
| 9 | VLR_FECEP_ST_DEV_ENT_MP | NUMBER | Y |  |  |

**Indexes**:
- IX_TMP_RESSARC_MG_C186: (COD_PROD_PRINC, DATA_FISCAL, IND_PROD_PRINC, GRUPO_PROD_PRINC)

---

## TMP_RESSARC_MG_INVENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INVENTARIO | DATE | Y |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 11 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 12 | QUANTIDADE | NUMBER | Y |  |  |
| 13 | VLR_ICMS_MEDIO | NUMBER | Y |  |  |
| 14 | VLR_BASE_ICMSS_MEDIO | NUMBER | Y |  |  |
| 15 | VLR_ICMSS_MEDIO | NUMBER | Y |  |  |
| 16 | VLR_FCP_MEDIO | NUMBER | Y |  |  |

**Indexes**:
- IX_TMP_RESSARC_MG_INVENT: (COD_PRODUTO, IND_PRODUTO, GRUPO_PRODUTO)

---

## TMP_RESSARC_MG_MOV_DWT_P

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 5 | DATA_PERIODO | DATE | Y |  |  |
| 6 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 7 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | DATA_FISCAL | DATE | Y |  |  |
| 10 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 11 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 14 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 15 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 16 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 17 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 18 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 19 | NORM_DEV | CHAR(1) | Y |  |  |
| 20 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 21 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 22 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 23 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 24 | DATA_EMISSAO | DATE | Y |  |  |
| 25 | DATA_SAIDA_REC | DATE | Y |  |  |
| 26 | IND_NOTA_DEVOL | CHAR(1) | Y |  |  |
| 27 | COD_RESP_RET | CHAR(1) | Y |  |  |
| 28 | GRUPO_SITUACAO_A | VARCHAR2(9) | Y |  |  |
| 29 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 30 | GRUPO_SITUACAO_B | VARCHAR2(9) | Y |  |  |
| 31 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 32 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 33 | CFOP | VARCHAR2(4) | Y |  |  |
| 34 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 35 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 36 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 37 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 38 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 39 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 40 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 41 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 42 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 43 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 44 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 45 | ALIQ_ICMSS | NUMBER(7,4) | Y |  |  |
| 46 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 47 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 48 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 49 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 50 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 51 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 52 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 53 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 54 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 55 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 56 | VL_BC_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 57 | VL_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 58 | VL_ICMS | NUMBER(17,2) | Y |  |  |
| 59 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 60 | IDENT_MEDIDA_PROD | NUMBER(12) | Y |  |  |
| 61 | IDENT_MEDIDA_ITEM | NUMBER(12) | Y |  |  |
| 62 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 63 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 64 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 65 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 66 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 67 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 68 | IND_TP_DOC_ARREC | VARCHAR2(1) | Y |  |  |
| 69 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 70 | IND_SIMPLES_NAC | VARCHAR2(1) | Y |  |  |
| 71 | IND_SITUACAO_ESP | VARCHAR2(1) | Y |  |  |
| 72 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 73 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 74 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 75 | DAT_DI | DATE | Y |  |  |
| 76 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 77 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 78 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |

**Indexes**:
- IX_TMP_RESSARC_MG_MOV_DWT_P: (COD_PRODUTO, IND_PRODUTO, GRUPO_PRODUTO)

---

## TMP_RFT_MOV_ANALITICOS_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | DATA_INICIAL | DATE | Y |  |  |
| 8 | DATA_FINAL | DATE | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(100) | Y |  |  |
| 11 | RAZAO_SOCIAL_ESTABELECIMENTO | VARCHAR2(130) | Y |  |  |
| 12 | CGC | VARCHAR2(14) | Y |  |  |
| 13 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 14 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 15 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 16 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 17 | DATA_EMISSAO | DATE | Y |  |  |
| 18 | DATA_FISCAL | DATE | Y |  |  |
| 19 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 20 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 21 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 22 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 26 | VLR_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |
| 29 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 30 | IND_CONTEM_COD | CHAR(1) | Y |  |  |
| 31 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 32 | PIND_NUMPROC_PFJ | CHAR(1) | Y |  |  |
| 33 | I_REL | NUMBER(1) | Y |  |  |
| 34 | PERIODO_COM_MOVIMENTO | VARCHAR2(50) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_RFT_MOV_ANALITICOS_MERC: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_RFT_MOV_DET_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(100) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | DATA_FISCAL | DATE | Y |  |  |
| 8 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 9 | NORM_DEV | CHAR(1) | Y |  |  |
| 10 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 15 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 16 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 17 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 18 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 19 | DATA_EMISSAO | DATE | Y |  |  |
| 20 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 21 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 22 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 23 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 24 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 25 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 26 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 27 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 28 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 29 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 30 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 31 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 32 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 35 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 36 | VLR_BASE_RED | NUMBER(17,2) | Y |  |  |
| 37 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 38 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 39 | VLR_SUBST_ICMS | NUMBER(17,2) | Y |  |  |
| 40 | VLR_BASE_ISENTAS | NUMBER(17,2) | Y |  |  |
| 41 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 42 | DIF_ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 43 | VLR_DIFAL | NUMBER(17,2) | Y |  |  |
| 44 | DSC_OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 45 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 46 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 47 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 48 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 49 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 50 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 51 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 52 | VLR_ISENTA_IPI | NUMBER(17,2) | Y |  |  |
| 53 | VLR_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |
| 54 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 55 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 56 | DSC_UND_PADRAO | VARCHAR2(50) | Y |  |  |
| 57 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 58 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 59 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 60 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 61 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 62 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 63 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 64 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 65 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 66 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 67 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 68 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 69 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 70 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 71 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 72 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 73 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 74 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 75 | COD_TRIB_IPI | VARCHAR2(2) | Y | 'N' |  |
| 76 | IND_CRED_ESTIMULO | CHAR(1) | Y | 'N' |  |
| 77 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 78 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 79 | VLR_ALIQ_SUB_ICMS | NUMBER(7,4) | Y |  |  |
| 80 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 81 | VLR_FECP_ICMS | NUMBER(17,2) | Y |  |  |
| 82 | VLR_FECP_DIFALIQ | NUMBER(17,2) | Y |  |  |
| 83 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 84 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  |  |
| 85 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 86 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 87 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 88 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 89 | DESC_MUNICIPIO | VARCHAR2(50) | Y |  |  |
| 90 | COD_BENEFICIO | VARCHAR2(10) | Y |  |  |
| 91 | INSC_ESTAD_SUBSTIT | VARCHAR2(14) | Y |  |  |
| 92 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 93 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 94 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 95 | ALIQ_AD_REM_ICMS | NUMBER(17,2) | Y |  |  |
| 96 | VLR_ICMS_MONO | NUMBER(17,2) | Y |  |  |
| 97 | ALIQ_AD_REM_ICMS_RETEN | NUMBER(17,2) | Y |  |  |
| 98 | VLR_ICMS_MONO_RETEN | NUMBER(17,2) | Y |  |  |
| 99 | VLR_ICMS_MONO_OP | NUMBER(17,2) | Y |  |  |
| 100 | VLR_ICMS_MONO_DIF | NUMBER(17,2) | Y |  |  |
| 101 | ALIQ_AD_REM_ICMS_RET | NUMBER(17,2) | Y |  |  |
| 102 | VLR_ICMS_MONO_RET | NUMBER(17,2) | Y |  |  |
| 103 | PERC_B100 | NUMBER(7,4) | Y |  |  |
| 104 | PERC_GLP | NUMBER(7,4) | Y |  |  |
| 105 | PERC_GLGN_N | NUMBER(7,4) | Y |  |  |
| 106 | PERC_GLGN_I | NUMBER(7,4) | Y |  |  |
| 107 | IND_ORIGEM_COM | VARCHAR2(1) | Y |  |  |
| 108 | QTD_BC_MONO | NUMBER(17,6) | Y |  |  |
| 109 | QTD_BC_MONO_RETEN | NUMBER(17,6) | Y |  |  |
| 110 | PERC_RED_AD_REM | NUMBER(7,4) | Y |  |  |
| 111 | DSC_RED_AD_REM | VARCHAR2(1) | Y |  |  |
| 112 | PERC_DIF | NUMBER(7,4) | Y |  |  |
| 113 | QTD_BC_MONO_RET | NUMBER(17,6) | Y |  |  |
| 114 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 115 | VLR_FRETE_ITEM | NUMBER(17,2) | Y |  |  |
| 116 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 117 | DAT_LANC_PIS_COFINS_ITEM | DATE | Y |  |  |
| 118 | DSC_CFO | VARCHAR2(50) | Y |  |  |
| 119 | DSC_NATUREZA_OP | VARCHAR2(50) | Y |  |  |
| 120 | UF_CONSUMO | VARCHAR2(2) | Y |  |  |
| 121 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 122 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 123 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 124 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 125 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 126 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 127 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 128 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 129 | RAZAO_SOCIAL_ESTAB | VARCHAR2(100) | Y |  |  |
| 130 | CGC_ESTAB | VARCHAR2(14) | Y |  |  |
| 131 | PERIODO_COM_MOVIMENTO | VARCHAR2(50) | Y |  |  |
| 132 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 133 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(70) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_RFT_MOV_DET_PROD: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_SAICS_INSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_REG_DCA | NUMBER(4) | N |  |  |
| 2 | COD_PRODUTO | VARCHAR2(62) | N |  |  |
| 3 | COD_INSUMO | VARCHAR2(37) | N |  |  |
| 4 | VAL1 | NUMBER(17,2) | Y |  |  |
| 5 | VAL2 | NUMBER(17,2) | Y |  |  |
| 6 | VAL3 | NUMBER(17,2) | Y |  |  |
| 7 | VAL4 | NUMBER(17,2) | Y |  |  |
| 8 | VAL5 | NUMBER(17,2) | Y |  |  |

**PK**: COD_REG_DCA, COD_PRODUTO, COD_INSUMO

---

## TMP_SAICS_ITENS_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 2 | IDENT_ITEM_MERC | NUMBER(12) | N |  |  |
| 3 | COD_TP_LANCTO | NUMBER(6) | Y |  |  |

**PK**: IDENT_DOCTO_FISCAL, IDENT_ITEM_MERC

---

## TMP_SAICS_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 2 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 3 | COD_LEGAL | NUMBER(4) | N |  |  |
| 4 | DATA_FISCAL | DATE | Y |  |  |
| 5 | COD_PART | VARCHAR2(100) | Y |  |  |
| 6 | COD_CHAVE | NUMBER(2) | Y |  |  |
| 7 | VALOR_SAI | NUMBER(17,2) | Y |  |  |
| 8 | PERC_CRDOUT | NUMBER(17,2) | Y |  |  |
| 9 | VALOR_CRDOUT | NUMBER(17,2) | Y |  |  |
| 10 | BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VALOR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 14 | DATA_SAI | DATE | Y |  |  |
| 15 | REG_5315 | NUMBER(5) | Y |  |  |
| 16 | REG_5320 | NUMBER(5) | Y |  |  |
| 17 | REG_5325 | NUMBER(5) | Y |  |  |
| 18 | REG_5330 | NUMBER(5) | Y |  |  |

**PK**: NUM_DOCFIS, SERIE_DOCFIS, COD_LEGAL

---

## TMP_SAICS_NF_EXP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 2 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 3 | COD_LEGAL | NUMBER(4) | N |  |  |
| 4 | NUM_DOCUMENTO | VARCHAR2(12) | N |  |  |
| 5 | COMP_OPER | CHAR(1) | Y |  |  |
| 6 | NUM_DOCFIS_EXP | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS_EXP | VARCHAR2(3) | Y |  |  |
| 8 | DATA_DOCFIS_EXP | DATE | Y |  |  |
| 9 | BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VALOR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | REG_5335 | NUMBER(5) | Y |  |  |
| 12 | REG_5340 | NUMBER(5) | Y |  |  |
| 13 | REG_5350 | NUMBER(5) | Y |  |  |

**PK**: NUM_DOCFIS, SERIE_DOCFIS, COD_LEGAL, NUM_DOCUMENTO

---

## TMP_SAICS_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_REG_DCA | NUMBER(4) | N |  |  |
| 2 | COD_ITEM | VARCHAR2(62) | N |  |  |
| 3 | VAL1 | NUMBER(17,2) | Y |  |  |
| 4 | VAL2 | NUMBER(17,2) | Y |  |  |
| 5 | VAL3 | NUMBER(17,2) | Y |  |  |
| 6 | VAL4 | NUMBER(17,2) | Y |  |  |
| 7 | VAL5 | NUMBER(17,2) | Y |  |  |

**PK**: COD_REG_DCA, COD_ITEM

---

## TMP_SAICS_REG_0200

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | N |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | VALID_PRODUTO | DATE | Y |  |  |
| 6 | IND_ANT_PROD | CHAR(1) | Y |  |  |
| 7 | COD_ANT_ITEM | VARCHAR2(60) | Y |  |  |
| 8 | DAT_ALT_CODIGO | DATE | Y |  |  |
| 9 | COD_UND_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | COD_GEN | VARCHAR2(2) | Y |  |  |
| 11 | COD_ITEM_FINAL | VARCHAR2(62) | Y |  |  |

**PK**: GRUPO_PRODUTO, COD_PRODUTO, IND_PRODUTO

---

## TMP_SAICS_TIPO_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | COD_CHAVE | NUMBER(4) | Y |  |  |

**PK**: COD_DOCTO

---

## TMP_SAICS_X10

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | REGISTRO | VARCHAR2(20) | N |  |  |
| 2 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 3 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |
| 4 | VLR_ICMS_DCA | NUMBER(21,6) | Y |  |  |

---

## TMP_SALDO_CONTA_HIERARQUICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | IND_CONTA | CHAR(1) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 8 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SALDO_FIM | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_CRE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 12 | CHAVE | VARCHAR2(1000) | Y |  |  |
| 13 | NIVEL | NUMBER(2) | Y |  |  |
| 14 | DATA_SALDO_INI | DATE | Y |  |  |
| 15 | DATA_SALDO_FIM | DATE | Y |  |  |

---

## TMP_SALD_CRED_RS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | DAT_GRAVACAO | DATE | N |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 4 | SEQ | NUMBER(12) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | DATA_SALDO | DATE | Y |  |  |
| 8 | DATA_INI | DATE | Y |  |  |
| 9 | DATA_FIM | DATE | Y |  |  |
| 10 | DATA_ULT_CALC | DATE | Y |  |  |
| 11 | DESC_CIAP | VARCHAR2(200) | Y |  |  |
| 12 | DAT_OPER | DATE | Y |  |  |
| 13 | DAT_FISCAL | DATE | Y |  |  |
| 14 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 15 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_CRED_APROP | NUMBER(17,2) | Y |  |  |
| 17 | NUM_ALT_PARC | VARCHAR2(7) | Y |  |  |
| 18 | VLR_ICMS_BX | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CRED_DEDUZ | NUMBER(17,2) | Y |  |  |
| 20 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 21 | VLR_CRED_PASS | NUMBER(17,2) | Y |  |  |
| 22 | IND_LEGENDA | VARCHAR2(2) | Y |  |  |
| 23 | PARCELA_SEQ | NUMBER(3) | Y |  |  |
| 24 | P_DESCR_BEM | VARCHAR2(1) | Y |  |  |
| 25 | RAZAO_SOCIAL_ESTAB | VARCHAR2(100) | Y |  |  |
| 26 | CGC_ESTAB | VARCHAR2(14) | Y |  |  |
| 27 | PERIODO_COM_MOVIMENTO | VARCHAR2(50) | Y |  |  |

**PK**: PROC_ID, DAT_GRAVACAO, COD_USUARIO, SEQ

**Indexes**:
- IX_TMP_SALD_CRED_RS: (COD_USUARIO, DAT_GRAVACAO)

---

## TMP_SELECT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA_OU_COD_ESTAB | VARCHAR2(21) | Y |  |  |
| 2 | DESCRICAO | VARCHAR2(156) | Y |  |  |

---

## TMP_SELECT_SCP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA_OU_COD_ESTAB | VARCHAR2(21) | Y |  |  |
| 2 | COD_SCP | VARCHAR2(21) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(156) | Y |  |  |
| 4 | COD_USUARIO | VARCHAR2(40) | Y |  |  |

---

## TMP_SPED_BPDRE_CUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO | DATE | N |  |  |
| 4 | ORDEM | NUMBER(4) | Y |  |  |
| 5 | NIVEL | NUMBER(4) | Y |  |  |
| 6 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 7 | DESCRICAO | VARCHAR2(150) | Y |  |  |
| 8 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 9 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 10 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 11 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 12 | VLR_SALDO_CALC_INI | NUMBER(19,2) | Y |  |  |
| 13 | IND_DEB_CRED_INI | CHAR(1) | Y |  |  |
| 14 | VLR_SALDO_CALC | NUMBER(19,2) | Y |  |  |
| 15 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 16 | VLR_SALDO_CALC_INI_MF | NUMBER(19,2) | Y |  |  |
| 17 | IND_DEB_CRED_INI_MF | CHAR(1) | Y |  |  |
| 18 | VLR_SALDO_CALC_MF | NUMBER(19,2) | Y |  |  |
| 19 | IND_DEB_CRED_MF | CHAR(1) | Y |  |  |
| 20 | DATA_SALDO_INI | DATE | Y |  |  |
| 21 | CHAVE_ORD | VARCHAR2(200) | Y |  |  |
| 22 | TIPO | CHAR(3) | N |  |  |
| 23 | BPDRE | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO, COD_CONTA_AGLUT, COD_CONTA, GRUPO_CONTA, COD_CUSTO, GRUPO_CUSTO, BPDRE, TIPO

---

## TMP_SPED_C425_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | INDCAPAITEM | VARCHAR2(30) | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_MOD | VARCHAR2(2) | Y |  |  |
| 5 | ECF_MOD | VARCHAR2(30) | Y |  |  |
| 6 | ECF_FAB | VARCHAR2(21) | Y |  |  |
| 7 | ECF_CX | VARCHAR2(3) | N |  |  |
| 8 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 9 | DT_DOC | DATE | N |  |  |
| 10 | CRZ | VARCHAR2(6) | N |  |  |
| 11 | COD_TOT_PAR_CTRL | VARCHAR2(7) | N |  |  |
| 12 | COD_TOT_PAR | VARCHAR2(7) | Y |  |  |
| 13 | NR_TOT | VARCHAR2(2) | N |  |  |
| 14 | COD_TOTALIZADOR_OBRIG | VARCHAR2(7) | Y |  |  |
| 15 | IND_SITUACAO_CUPOM | CHAR(1) | Y |  |  |
| 16 | IND_SITUACAO_ITEM | CHAR(1) | Y |  |  |
| 17 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 18 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 19 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 20 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 21 | SIT_ESCRITURA_ESPECIAL | VARCHAR2(300) | Y |  |  |
| 22 | COD_ITEM | VARCHAR2(62) | N |  |  |
| 23 | QTD | NUMBER(17,4) | Y |  |  |
| 24 | UNID | VARCHAR2(8) | N |  |  |
| 25 | VL_ITEM | NUMBER(17,2) | Y |  |  |
| 26 | VL_PIS_CUPOM | NUMBER(17,2) | Y |  |  |
| 27 | VL_COFINS_CUPOM | NUMBER(17,2) | Y |  |  |
| 28 | COD_SIT | VARCHAR2(2) | Y |  |  |
| 29 | NUM_DOC_CUPOM | VARCHAR2(9) | Y |  |  |
| 30 | DT_DOC_CUPOM | DATE | Y |  |  |
| 31 | VL_DOC | NUMBER(17,2) | Y |  |  |
| 32 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 33 | NOM_ADQ | VARCHAR2(60) | Y |  |  |
| 34 | QTD_CANC | NUMBER(17,4) | Y |  |  |
| 35 | CST_ICMS | VARCHAR2(3) | Y |  |  |
| 36 | CFOP | VARCHAR2(4) | Y |  |  |
| 37 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 38 | VL_BC_ICMS | NUMBER(17,2) | Y |  |  |
| 39 | VL_ICMS | NUMBER(17,2) | Y |  |  |
| 40 | COD_OBS | VARCHAR2(8) | Y |  |  |
| 41 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 42 | IDENT_CAIXA_ECF | NUMBER(12) | Y |  |  |
| 43 | IDENT_TOTALIZADOR_ECF | NUMBER(12) | Y |  |  |
| 44 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ECF_CX, CRZ, DT_DOC, COD_ITEM, UNID, COD_TOT_PAR_CTRL, NR_TOT

---

## TMP_SPED_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CFO | NUMBER(12) | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |
| 3 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |

**PK**: IDENT_CFO

---

## TMP_SPED_CFOCSTALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | INDCAPAITEM | VARCHAR2(30) | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_FISCAL | DATE | Y |  |  |
| 5 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 6 | NORM_DEV | CHAR(1) | Y |  |  |
| 7 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 9 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 12 | NUM_DOC | VARCHAR2(12) | Y |  |  |
| 13 | SER | VARCHAR2(3) | Y |  |  |
| 14 | SUB_SERIE | VARCHAR2(2) | Y |  |  |
| 15 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 16 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 17 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 18 | SITUACAO | CHAR(1) | Y |  |  |
| 19 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 20 | GRUPO_FIS_JUR_TRANSP | VARCHAR2(9) | Y |  |  |
| 21 | IND_FIS_JUR_TRANSP | CHAR(1) | Y |  |  |
| 22 | COD_FIS_JUR_TRANSP | VARCHAR2(14) | Y |  |  |
| 23 | ALIQ_IRRF | NUMBER(7,4) | Y |  |  |
| 24 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 25 | COD_ANP | VARCHAR2(12) | Y |  |  |
| 26 | IND_CONTROLE_SELO | CHAR(1) | Y |  |  |
| 27 | CLAS_ENQUAD_IPI | VARCHAR2(5) | Y |  |  |
| 28 | DAT_ESCR_EXTEMP | DATE | Y |  |  |
| 29 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 30 | IND_NFE_DENEG_INUT | NUMBER(1) | Y |  |  |
| 31 | IND_NF_REG_ESPECIAL | VARCHAR2(1) | Y |  |  |
| 32 | SIT_ESCRITURA_ESPECIAL | VARCHAR2(300) | Y |  |  |
| 33 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  |  |
| 34 | IDENT_FIS_CONCES | NUMBER(12) | Y |  |  |
| 35 | COD_UF_ST | VARCHAR2(2) | Y |  |  |
| 36 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 37 | SIT_NFE_CONTRIBUINTE | CHAR(1) | Y |  |  |
| 38 | IND_OPER | CHAR(1) | Y |  |  |
| 39 | IND_EMIT | CHAR(1) | Y |  |  |
| 40 | COD_PART | VARCHAR2(16) | Y |  |  |
| 41 | COD_MOD | VARCHAR2(2) | Y |  |  |
| 42 | COD_SIT | VARCHAR2(2) | Y |  |  |
| 43 | CHV_NFE | VARCHAR2(80) | Y |  |  |
| 44 | DT_DOC | DATE | Y |  |  |
| 45 | DT_E_S | DATE | Y |  |  |
| 46 | VL_DOC | NUMBER(17,2) | Y |  |  |
| 47 | IND_PAGTO | CHAR(1) | Y |  |  |
| 48 | VL_DESC | NUMBER(17,2) | Y |  |  |
| 49 | VL_ABAT_NT | NUMBER(17,2) | Y |  |  |
| 50 | VL_MERC | NUMBER(17,2) | Y |  |  |
| 51 | IND_FRT | CHAR(1) | Y |  |  |
| 52 | VL_FRT | NUMBER(17,2) | Y |  |  |
| 53 | VL_SEG | NUMBER(17,2) | Y |  |  |
| 54 | VL_OUT_DA | NUMBER(17,2) | Y |  |  |
| 55 | VL_BC_ICMS | NUMBER(17,2) | Y |  |  |
| 56 | VL_ICMS | NUMBER(17,2) | Y |  |  |
| 57 | VL_BC_ST | NUMBER(17,2) | Y |  |  |
| 58 | VL_ST | NUMBER(17,2) | Y |  |  |
| 59 | VL_IPI | NUMBER(17,2) | Y |  |  |
| 60 | VL_PIS | NUMBER(17,2) | Y |  |  |
| 61 | VL_COFINS | NUMBER(17,2) | Y |  |  |
| 62 | VL_PIS_ST | NUMBER(17,2) | Y |  |  |
| 63 | VL_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 64 | VL_SERV_NT | NUMBER(17,2) | Y |  |  |
| 65 | VL_BC_ISSQN | NUMBER(17,2) | Y |  |  |
| 66 | VL_ISSQN | NUMBER(17,2) | Y |  |  |
| 67 | VL_BC_IRRF | NUMBER(17,2) | Y |  |  |
| 68 | VL_IRRF | NUMBER(17,2) | Y |  |  |
| 69 | VL_BC_PREV | NUMBER(17,2) | Y |  |  |
| 70 | VL_PREV | NUMBER(17,2) | Y |  |  |
| 71 | VL_FCP | NUMBER(17,2) | Y |  |  |
| 72 | IND_F0 | CHAR(1) | Y |  |  |
| 73 | COD_PART_TRANSP | VARCHAR2(16) | Y |  |  |
| 74 | VEIC_ID | VARCHAR2(17) | Y |  |  |
| 75 | QTD_VOL | NUMBER(17,6) | Y |  |  |
| 76 | PESO_BRT | NUMBER(14,3) | Y |  |  |
| 77 | PESO_LIQ | NUMBER(14,3) | Y |  |  |
| 78 | UF_ID | CHAR(2) | Y |  |  |
| 79 | COD_AUT_COMB | VARCHAR2(21) | Y |  |  |
| 80 | NR_PASSE | VARCHAR2(20) | Y |  |  |
| 81 | HORA | VARCHAR2(4) | Y |  |  |
| 82 | TEMPER | NUMBER(5,2) | Y |  |  |
| 83 | NOM_MOT | VARCHAR2(24) | Y |  |  |
| 84 | CPF_COMB | VARCHAR2(11) | Y |  |  |
| 85 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 86 | COD_ITEM | VARCHAR2(62) | Y |  |  |
| 87 | DESCR_COMPL | VARCHAR2(50) | Y |  |  |
| 88 | QTD | NUMBER(17,6) | Y |  |  |
| 89 | UNID | VARCHAR2(8) | Y |  |  |
| 90 | VL_ITEM | NUMBER(17,2) | Y |  |  |
| 91 | IND_MOV | CHAR(1) | Y |  |  |
| 92 | CST_ICMS | VARCHAR2(3) | N |  |  |
| 93 | CFOP | VARCHAR2(4) | N |  |  |
| 94 | COD_NAT | VARCHAR2(3) | Y |  |  |
| 95 | ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 96 | ALIQ_ST | NUMBER(7,4) | Y |  |  |
| 97 | IND_APUR | CHAR(1) | Y |  |  |
| 98 | CST_IPI | VARCHAR2(2) | Y |  |  |
| 99 | COD_ENQ | VARCHAR2(3) | Y |  |  |
| 100 | VL_BC_IPI | NUMBER(17,2) | Y |  |  |
| 101 | ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 102 | CST_PIS | VARCHAR2(2) | Y |  |  |
| 103 | VL_BC_PIS | NUMBER(17,2) | Y |  |  |
| 104 | ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 105 | QUANT_BC_PIS | NUMBER(18,3) | Y |  |  |
| 106 | ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 107 | CST_COFINS | VARCHAR2(2) | Y |  |  |
| 108 | VL_BC_COFINS | NUMBER(17,2) | Y |  |  |
| 109 | ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 110 | QUANT_BC_COFINS | NUMBER(18,3) | Y |  |  |
| 111 | ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 112 | COD_CTA | VARCHAR2(70) | Y |  |  |
| 113 | GRUPO_CTA | VARCHAR2(9) | Y |  |  |
| 114 | ALIQ_ISSQN | NUMBER(7,4) | Y |  |  |
| 115 | IND_TP_PROD_MEDIC | CHAR(1) | Y |  |  |
| 116 | COD_SELO_IPI | VARCHAR2(6) | Y |  |  |
| 117 | QT_SELO_IPI | NUMBER(17,6) | Y |  |  |
| 118 | CL_ENQ | VARCHAR2(5) | Y |  |  |
| 119 | VL_UNID | NUMBER(19,4) | Y |  |  |
| 120 | QUANT_PAD | NUMBER(17,6) | Y |  |  |
| 121 | VL_RED_BC | NUMBER(17,2) | Y |  |  |
| 122 | COD_OBS | VARCHAR2(6) | Y |  |  |
| 123 | COD_ESTADO_ORIG | VARCHAR2(2) | Y |  |  |
| 124 | COD_ESTADO_DEST | VARCHAR2(2) | Y |  |  |
| 125 | IDENT_FIS_LSG | NUMBER(12) | Y |  |  |
| 126 | COD_NAT_SPED | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, CFOP, CST_ICMS, ALIQ_ICMS

---

## TMP_SPED_CONTAS_CUSTO
**Comment**: Tabela Temporária p/ auxliar a geração do J100 e J150

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_SALDO | DATE | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 4 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 5 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 6 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 7 | IND_DEB_CRED_INI | CHAR(1) | Y |  |  |
| 8 | VLR_SALDO_FIM | NUMBER(19,2) | Y |  |  |
| 9 | IND_DEB_CRED_FIM | CHAR(1) | Y |  |  |
| 10 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 11 | VLR_TOT_CRED | NUMBER(19,2) | Y |  |  |
| 12 | VLR_SALDO_INI_MF | NUMBER(19,2) | Y |  |  |
| 13 | IND_DEB_CRED_INI_MF | CHAR(1) | Y |  |  |
| 14 | VLR_SALDO_FIM_MF | NUMBER(19,2) | Y |  |  |
| 15 | IND_DEB_CRED_FIM_MF | CHAR(1) | Y |  |  |
| 16 | VLR_TOT_DEB_MF | NUMBER(19,2) | Y |  |  |
| 17 | VLR_TOT_CRED_MF | NUMBER(19,2) | Y |  |  |

**PK**: DATA_SALDO, COD_CONTA, GRUPO_CONTA, COD_CUSTO, GRUPO_CUSTO

**Indexes**:
- IX_TMP_SPED_CONTAS_CUSTO: (COD_CONTA, GRUPO_CONTA)

---

## TMP_SPED_I015

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA | VARCHAR2(70) | N |  |  |

**Indexes**:
- IX_TMP_SPED_I015 (UNIQUE): (COD_CONTA)

---

## TMP_SPED_I050
**Comment**: Tabela Temporária p/ auxiliar a geração do I050

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 2 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |

**Indexes**:
- IX_TMP_SPED_I050 (UNIQUE): (COD_CONTA, GRUPO_CONTA)

---

## TMP_SPED_I050_SINT
**Comment**: Tabela Temporária p/ auxliar a geração do I050, marcando as contas sintéticas já processadas

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 2 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |

**PK**: COD_CONTA, GRUPO_CONTA

---

## TMP_SPED_I100
**Comment**: Tabela Temporária p/ auxliar a geração do I100

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 2 | COD_CUSTO | VARCHAR2(50) | N |  |  |

**Indexes**:
- IX_TMP_SPED_I100 (UNIQUE): (GRUPO_CUSTO, COD_CUSTO)

---

## TMP_SPED_I310_I355
**Comment**: Tabela Temporária p/ auxliar a geração do I310 e I355

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_LANCTO | DATE | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 4 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 5 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 6 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 7 | VLR_TOT_CRED | NUMBER(19,2) | Y |  |  |
| 8 | VLR_ENCERRAMENTO | NUMBER(19,2) | Y |  |  |
| 9 | VLR_TOT_DEB_MF | NUMBER(19,2) | Y | 0 |  |
| 10 | VLR_TOT_CRED_MF | NUMBER(19,2) | Y | 0 |  |
| 11 | VLR_ENCERRAMENTO_MF | NUMBER(19,2) | Y | 0 |  |

**Indexes**:
- IX_TMP_SPED_I310_I355 (UNIQUE): (COD_CONTA, COD_CUSTO, DATA_LANCTO, GRUPO_CONTA, GRUPO_CUSTO)

---

## TMP_SPED_J100_J150
**Comment**: Tabela Temporária p/ auxliar a geração do J100 e J150

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 2 | VLR_SALDO_CALC | NUMBER(19,2) | Y |  |  |
| 3 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 4 | VLR_SALDO_CALC_INI | NUMBER(19,2) | Y |  |  |
| 5 | IND_DEB_CRED_INI | CHAR(1) | Y |  |  |
| 6 | VLR_SALDO_CALC_MF | NUMBER(19,2) | Y |  |  |
| 7 | IND_DEB_CRED_MF | CHAR(1) | Y |  |  |
| 8 | VLR_SALDO_CALC_INI_MF | NUMBER(19,2) | Y |  |  |
| 9 | IND_DEB_CRED_INI_MF | CHAR(1) | Y |  |  |

**PK**: COD_CONTA_AGLUT

---

## TMP_SPED_LVR_RAZAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COL_GRP | VARCHAR2(99) | Y |  |  |
| 2 | COL_TOT | NUMBER(21,6) | Y |  |  |
| 3 | COL1 | VARCHAR2(99) | Y |  |  |
| 4 | COL2 | VARCHAR2(99) | Y |  |  |
| 5 | COL3 | VARCHAR2(99) | Y |  |  |
| 6 | COL4 | VARCHAR2(99) | Y |  |  |
| 7 | COL5 | VARCHAR2(99) | Y |  |  |
| 8 | COL6 | VARCHAR2(99) | Y |  |  |
| 9 | COL7 | VARCHAR2(99) | Y |  |  |
| 10 | COL8 | VARCHAR2(99) | Y |  |  |
| 11 | COL9 | VARCHAR2(99) | Y |  |  |
| 12 | COL10 | VARCHAR2(99) | Y |  |  |
| 13 | COL11 | VARCHAR2(99) | Y |  |  |
| 14 | COL12 | VARCHAR2(99) | Y |  |  |
| 15 | COL13 | VARCHAR2(99) | Y |  |  |
| 16 | COL14 | VARCHAR2(99) | Y |  |  |
| 17 | COL15 | VARCHAR2(99) | Y |  |  |
| 18 | COL16 | VARCHAR2(99) | Y |  |  |
| 19 | COL17 | VARCHAR2(99) | Y |  |  |
| 20 | COL18 | VARCHAR2(99) | Y |  |  |
| 21 | COL19 | VARCHAR2(99) | Y |  |  |
| 22 | COL20 | VARCHAR2(99) | Y |  |  |
| 23 | COL21 | VARCHAR2(99) | Y |  |  |
| 24 | COL22 | VARCHAR2(99) | Y |  |  |
| 25 | COL23 | VARCHAR2(99) | Y |  |  |
| 26 | COL24 | VARCHAR2(99) | Y |  |  |
| 27 | COL25 | VARCHAR2(99) | Y |  |  |
| 28 | COL26 | VARCHAR2(99) | Y |  |  |
| 29 | COL27 | VARCHAR2(99) | Y |  |  |
| 30 | COL28 | VARCHAR2(99) | Y |  |  |
| 31 | COL29 | VARCHAR2(99) | Y |  |  |
| 32 | COL30 | VARCHAR2(99) | Y |  |  |
| 33 | COL31 | VARCHAR2(99) | Y |  |  |
| 34 | COL32 | VARCHAR2(99) | Y |  |  |
| 35 | COL33 | VARCHAR2(99) | Y |  |  |
| 36 | COL34 | VARCHAR2(99) | Y |  |  |
| 37 | COL35 | VARCHAR2(99) | Y |  |  |
| 38 | COL36 | VARCHAR2(99) | Y |  |  |
| 39 | COL37 | VARCHAR2(99) | Y |  |  |
| 40 | COL38 | VARCHAR2(99) | Y |  |  |
| 41 | COL39 | VARCHAR2(99) | Y |  |  |
| 42 | COL40 | VARCHAR2(99) | Y |  |  |
| 43 | COL41 | VARCHAR2(99) | Y |  |  |
| 44 | COL42 | VARCHAR2(99) | Y |  |  |
| 45 | COL43 | VARCHAR2(99) | Y |  |  |
| 46 | COL44 | VARCHAR2(99) | Y |  |  |
| 47 | COL45 | VARCHAR2(99) | Y |  |  |
| 48 | COL46 | VARCHAR2(99) | Y |  |  |
| 49 | COL47 | VARCHAR2(99) | Y |  |  |
| 50 | COL48 | VARCHAR2(99) | Y |  |  |
| 51 | COL49 | VARCHAR2(99) | Y |  |  |
| 52 | COL50 | VARCHAR2(99) | Y |  |  |

**Indexes**:
- IDX_TMP_SPED_LVR_RAZAO: (COL_GRP)

---

## TMP_SPED_REL_REF_ANL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO | DATE | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | COD_CONTA_REF | VARCHAR2(30) | N |  |  |
| 6 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 7 | VLR_TOTAL_CREF | NUMBER(19,2) | Y |  |  |
| 8 | DESC_CONTA | VARCHAR2(100) | Y |  |  |
| 9 | DESC_CONTA_REF | VARCHAR2(100) | Y |  |  |
| 10 | VLR_SALDO_CALC | NUMBER(19,2) | Y |  |  |
| 11 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 12 | IND_CONTA | CHAR(1) | Y |  |  |
| 13 | COD_CONTA_REF_MAE | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO, COD_CONTA, COD_CONTA_REF, COD_CUSTO

---

## TMP_SPED_REL_REF_SNT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO | DATE | N |  |  |
| 4 | COD_CONTA_REF | VARCHAR2(30) | N |  |  |
| 5 | DESCRICAO_CONTA_REF | VARCHAR2(100) | Y |  |  |
| 6 | VLR_SALDO_CALC | NUMBER(19,2) | Y |  |  |
| 7 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 8 | IND_CONTA | CHAR(1) | Y |  |  |
| 9 | COD_CONTA_REF_MAE | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO, COD_CONTA_REF

---

## TMP_X07_DOCTO_FISCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 15 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 16 | DATA_EMISSAO | DATE | Y |  |  |
| 17 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 18 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 19 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 20 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 21 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 22 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 23 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 24 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 25 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 26 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 27 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 28 | DATA_SAIDA_REC | DATE | Y |  |  |
| 29 | INSC_ESTAD_SUBSTIT | VARCHAR2(14) | Y |  |  |
| 30 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 31 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 32 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 33 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 34 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 35 | VLR_BASE_DIF_FRETE | NUMBER(17,2) | Y |  |  |
| 36 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 37 | CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 38 | SITUACAO | CHAR(1) | Y |  |  |
| 39 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 40 | VLR_NOTA_CONV | NUMBER(18,4) | Y |  |  |
| 41 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 42 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 43 | IND_MODELO_CUPOM | VARCHAR2(2) | Y |  |  |
| 44 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 45 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 46 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 47 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 49 | VLR_OUTROS3 | NUMBER(17,2) | Y |  |  |
| 50 | VLR_OUTROS4 | NUMBER(17,2) | Y |  |  |
| 51 | VLR_OUTROS5 | NUMBER(17,2) | Y |  |  |
| 52 | VLR_ALIQ_OUTROS1 | NUMBER(7,4) | Y |  |  |
| 53 | VLR_ALIQ_OUTROS2 | NUMBER(7,4) | Y |  |  |
| 54 | IND_NF_ESPECIAL | CHAR(1) | Y |  |  |
| 55 | NUM_MAQUINA | NUMBER(6) | Y |  |  |
| 56 | NUM_CUPOM_FINAL | NUMBER(6) | Y |  |  |
| 57 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 58 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 59 | DIF_ALIQ_TRIB_ICMS | NUMBER(7,4) | Y |  |  |
| 60 | OBS_TRIBUTO_ICMS | VARCHAR2(45) | Y |  |  |
| 61 | IDENT_DET_OP_ICMS | NUMBER(12) | Y |  |  |
| 62 | COD_DET_OP_ICMS | VARCHAR2(5) | Y |  |  |
| 63 | ALIQ_TRIBUTO_IPI | NUMBER(7,4) | Y |  |  |
| 64 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 65 | OBS_TRIBUTO_IPI | VARCHAR2(45) | Y |  |  |
| 66 | IDENT_DET_OP_IPI | NUMBER(12) | Y |  |  |
| 67 | COD_DET_OP_IPI | VARCHAR2(5) | Y |  |  |
| 68 | ALIQ_TRIBUTO_ICMSS | NUMBER(7,4) | Y |  |  |
| 69 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 70 | OBS_TRIBUTO_ICMSS | VARCHAR2(45) | Y |  |  |
| 71 | IDENT_DET_OP_ICMSS | NUMBER(12) | Y |  |  |
| 72 | COD_DET_OP_ICMSS | VARCHAR2(5) | Y |  |  |
| 73 | ALIQ_TRIBUTO_IR | NUMBER(7,4) | Y |  |  |
| 74 | VLR_TRIBUTO_IR | NUMBER(17,2) | Y |  |  |
| 75 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |
| 76 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 77 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 78 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 79 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 80 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 81 | VLR_BASE_IPI_1 | NUMBER(17,2) | Y |  |  |
| 82 | VLR_BASE_IPI_2 | NUMBER(17,2) | Y |  |  |
| 83 | VLR_BASE_IPI_3 | NUMBER(17,2) | Y |  |  |
| 84 | VLR_BASE_IPI_4 | NUMBER(17,2) | Y |  |  |
| 85 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 86 | VLR_BASE_IR_1 | NUMBER(17,2) | Y |  |  |
| 87 | VLR_BASE_IR_2 | NUMBER(17,2) | Y |  |  |
| 88 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 89 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 90 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 91 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 92 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 93 | IND_TP_FRETE | CHAR(1) | Y |  |  |
| 94 | COD_MUNICIPIO | NUMBER(7) | Y |  |  |
| 95 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 96 | DAT_DI | DATE | Y |  |  |
| 97 | VLR_TOM_SERVICO | NUMBER(17,2) | Y |  |  |
| 98 | DAT_ESCR_EXTEMP | DATE | Y |  |  |
| 99 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 100 | COD_REGIAO | NUMBER(2) | Y |  |  |
| 101 | DAT_AUTENTIC | DATE | Y |  |  |
| 102 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 103 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 104 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 105 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 106 | VLR_TOT_IN | NUMBER(17,2) | Y |  |  |
| 107 | VLR_ICMS_IN | NUMBER(17,2) | Y |  |  |
| 108 | VLR_ICMS_B1_IN | NUMBER(17,2) | Y |  |  |
| 109 | VLR_ICMS_B2_IN | NUMBER(17,2) | Y |  |  |
| 110 | VLR_ICMS_B3_IN | NUMBER(17,2) | Y |  |  |
| 111 | VLR_ICMS_B4_IN | NUMBER(17,2) | Y |  |  |
| 112 | VLR_IPI_IN | NUMBER(17,2) | Y |  |  |
| 113 | VLR_IPI_B1_IN | NUMBER(17,2) | Y |  |  |
| 114 | VLR_IPI_B2_IN | NUMBER(17,2) | Y |  |  |
| 115 | VLR_IPI_B3_IN | NUMBER(17,2) | Y |  |  |
| 116 | VLR_IPI_B4_IN | NUMBER(17,2) | Y |  |  |
| 117 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 118 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 119 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 120 | VLR_MAT_APLIC_ISS | NUMBER(17,2) | Y |  |  |
| 121 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 122 | IND_MUNIC_ISS | CHAR(1) | Y |  |  |
| 123 | IND_CLASSE_OP_ISS | CHAR(1) | Y |  |  |
| 124 | DAT_FATO_GERADOR | DATE | Y |  |  |
| 125 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 126 | NUM_PAGINA | VARCHAR2(6) | Y |  |  |
| 127 | NUM_LIVRO | VARCHAR2(6) | Y |  |  |
| 128 | NRO_AIDF_NF | VARCHAR2(12) | Y |  |  |
| 129 | DAT_VALID_DOC_AIDF | DATE | Y |  |  |
| 130 | IND_FATURA | CHAR(1) | Y |  |  |
| 131 | IDENT_QUITACAO | NUMBER(12) | Y |  |  |
| 132 | COD_QUITACAO | VARCHAR2(5) | Y |  |  |
| 133 | NUM_SELO_CONT_ICMS | VARCHAR2(12) | Y |  |  |
| 134 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 135 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 136 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 137 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 138 | BASE_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 139 | VLR_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 140 | ALIQ_ICMS_ORIGDEST | NUMBER(7,4) | Y |  |  |
| 141 | VLR_DESC_CONDIC | NUMBER(17,2) | Y |  |  |
| 142 | VLR_BASE_ISE_ICMSS | NUMBER(17,2) | Y |  |  |
| 143 | VLR_BASE_OUT_ICMSS | NUMBER(17,2) | Y |  |  |
| 144 | VLR_RED_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 145 | PERC_RED_BASE_ICMS | NUMBER(7,4) | Y |  |  |
| 146 | IDENT_FISJUR_CPDIR | NUMBER(12) | Y |  |  |
| 147 | IND_FISJUR_CPDIR | CHAR(1) | Y |  |  |
| 148 | COD_FISJUR_CPDIR | VARCHAR2(14) | Y |  |  |
| 149 | IND_MEDIDAJUDICIAL | CHAR(1) | Y |  |  |
| 150 | IDENT_UF_ORIG_DEST | NUMBER(12) | Y |  |  |
| 151 | COD_UF_ORIG_DEST | VARCHAR2(2) | Y |  |  |
| 152 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  |  |
| 153 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 154 | NUM_CTR_DISP | NUMBER(10) | Y |  |  |
| 155 | NUM_FIM_DOCTO | VARCHAR2(12) | Y |  |  |
| 156 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 157 | COD_UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 158 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 159 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 160 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 161 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 162 | COD_PAGTO_INSS | VARCHAR2(4) | Y |  |  |
| 163 | DAT_OPERACAO | DATE | Y |  |  |
| 164 | USUARIO | VARCHAR2(40) | Y |  |  |
| 165 | DAT_INTERN_AM | DATE | Y |  |  |
| 166 | IDENT_FISJUR_LSG | NUMBER(12) | Y |  |  |
| 167 | IND_FISJUR_LSG | CHAR(1) | Y |  |  |
| 168 | COD_FISJUR_LSG | VARCHAR2(14) | Y |  |  |
| 169 | COMPROV_EXP | VARCHAR2(15) | Y |  |  |
| 170 | NUM_FINAL_CRT_DISP | NUMBER(12) | Y |  |  |
| 171 | NUM_ALVARA | VARCHAR2(8) | Y |  |  |
| 172 | NOTIFICA_SEFAZ | VARCHAR2(14) | Y |  |  |
| 173 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 174 | IND_NOTA_SERVICO | CHAR(1) | Y |  |  |
| 175 | COD_MOTIVO | VARCHAR2(10) | Y |  |  |
| 176 | COD_AMPARO | VARCHAR2(10) | Y |  |  |
| 177 | IDENT_ESTADO_AMPAR | NUMBER(12) | Y |  |  |
| 178 | COD_ESTADO_AMPAR | VARCHAR2(2) | Y |  |  |
| 179 | OBS_COMPL_MOTIVO | VARCHAR2(100) | Y |  |  |
| 180 | IND_TP_RET | CHAR(1) | Y |  |  |
| 181 | IND_TP_TOMADOR | CHAR(1) | Y |  |  |
| 182 | COD_ANTEC_ST | CHAR(1) | Y |  |  |
| 183 | IND_TELECOM | CHAR(1) | Y |  |  |
| 184 | CNPJ_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 185 | IDENT_UF_ARMAZ_ORIG | NUMBER(12) | Y |  |  |
| 186 | COD_UF_ARMAZ_ORIG | VARCHAR2(2) | Y |  |  |
| 187 | INS_EST_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 188 | CNPJ_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 189 | IDENT_UF_ARMAZ_DEST | NUMBER(12) | Y |  |  |
| 190 | COD_UF_ARMAZ_DEST | VARCHAR2(2) | Y |  |  |
| 191 | INS_EST_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 192 | OBS_INF_ADIC_NF | VARCHAR2(250) | Y |  |  |
| 193 | VLR_BASE_INSS_2 | NUMBER(17,2) | Y |  |  |
| 194 | VLR_ALIQ_INSS_2 | NUMBER(7,4) | Y |  |  |
| 195 | VLR_INSS_RETIDO_2 | NUMBER(17,2) | Y |  |  |
| 196 | COD_PAGTO_INSS_2 | VARCHAR2(4) | Y |  |  |
| 197 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 198 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 199 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 200 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 201 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 202 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 203 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 204 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 205 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 206 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 207 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 208 | BASE_ICMSS_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 209 | VLR_ICMSS_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 210 | COD_CEI | VARCHAR2(15) | Y |  |  |
| 211 | VLR_JUROS_INSS | NUMBER(17,2) | Y |  |  |
| 212 | VLR_MULTA_INSS | NUMBER(17,2) | Y |  |  |
| 213 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 214 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 215 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 216 | DAT_PGTO_GNRE_DARJ | DATE | Y |  |  |
| 217 | DT_PAGTO_NF | DATE | Y |  |  |
| 218 | IND_ORIGEM_INFO | CHAR(1) | Y | '0' |  |
| 219 | HORA_SAIDA | NUMBER(6) | Y |  |  |
| 220 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  |  |
| 221 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 222 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 223 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 224 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 225 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 226 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 227 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |
| 228 | COD_MUNICIPIO_ORIG | NUMBER(5) | Y |  |  |
| 229 | COD_MUNICIPIO_DEST | NUMBER(5) | Y |  |  |
| 230 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 231 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 232 | VLR_MAT_PROP | NUMBER(17,2) | Y |  |  |
| 233 | VLR_MAT_TERC | NUMBER(17,2) | Y |  |  |
| 234 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 235 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 236 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  |  |
| 237 | COD_MUNIC_ARMAZ_ORIG | NUMBER(5) | Y |  |  |
| 238 | INS_MUNIC_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 239 | COD_MUNIC_ARMAZ_DEST | NUMBER(5) | Y |  |  |
| 240 | INS_MUNIC_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 241 | IDENT_CLASSE_CONSUMO | NUMBER(12) | Y |  |  |
| 242 | COD_CLASSE_CONSUMO | VARCHAR2(2) | Y |  |  |
| 243 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 244 | NUM_CONTRATO | VARCHAR2(14) | Y |  |  |
| 245 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  |  |
| 246 | COD_TP_UTIL | VARCHAR2(2) | Y |  |  |
| 247 | GRUPO_TENSAO | VARCHAR2(2) | Y |  |  |
| 248 | DATA_CONSUMO_INI | DATE | Y |  |  |
| 249 | DATA_CONSUMO_FIM | DATE | Y |  |  |
| 250 | DATA_CONSUMO_LEIT | DATE | Y |  |  |
| 251 | QTD_CONTRATADA_PONTA | NUMBER(17,6) | Y |  |  |
| 252 | QTD_CONTRATADA_FPONTA | NUMBER(17,6) | Y |  |  |
| 253 | QTD_CONSUMO_TOTAL | NUMBER(17,6) | Y |  |  |
| 254 | IDENT_UF_CONSUMO | NUMBER(12) | Y |  |  |
| 255 | COD_UF_CONSUMO | VARCHAR2(2) | Y |  |  |
| 256 | COD_MUNIC_CONSUMO | NUMBER(5) | Y |  |  |
| 257 | COD_OPER_ESP_ST | CHAR(1) | Y |  |  |
| 258 | ATO_NORMATIVO | VARCHAR2(20) | Y |  |  |
| 259 | NUM_ATO_NORMATIVO | NUMBER(5) | Y |  |  |
| 260 | ANO_ATO_NORMATIVO | NUMBER(4) | Y |  |  |
| 261 | CAPITULACAO_NORMA | VARCHAR2(30) | Y |  |  |
| 262 | VLR_OUTRAS_ENTID | NUMBER(17,2) | Y |  |  |
| 263 | VLR_TERCEIROS | NUMBER(17,2) | Y |  |  |
| 264 | IND_TP_COMPL_ICMS | VARCHAR2(2) | Y |  |  |
| 265 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 266 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 267 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 268 | COD_VERIFIC_NFE | VARCHAR2(60) | Y |  |  |
| 269 | COD_TP_RPS_NFE | VARCHAR2(5) | Y |  |  |
| 270 | NUM_RPS_NFE | NUMBER(12) | Y |  |  |
| 271 | SERIE_RPS_NFE | VARCHAR2(5) | Y |  |  |
| 272 | DAT_EMISSAO_RPS_NFE | DATE | Y |  |  |
| 273 | DSC_SERVICO_NFE | VARCHAR2(1000) | Y |  |  |
| 274 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 275 | NUM_DV_NFE | NUMBER(1) | Y |  |  |
| 276 | MODELO_NF_DMS | VARCHAR2(3) | Y |  |  |
| 277 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  |  |
| 278 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 279 | IND_NFE_DENEG_INUT | NUMBER(1) | Y |  |  |
| 280 | IND_NF_REG_ESPECIAL | VARCHAR2(1) | Y |  |  |
| 281 | VLR_ABAT_NTRIBUTADO | NUMBER(15,2) | Y |  |  |
| 282 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  |  |
| 283 | HORA_EMISSAO | NUMBER(6) | Y |  |  |
| 284 | OBS_DADOS_FATURA | VARCHAR2(256) | Y |  |  |
| 285 | HORA_SAIDA_REC | NUMBER(6) | Y |  |  |
| 286 | IDENT_FIS_CONCES | NUMBER(12) | Y |  |  |
| 287 | IND_FIS_CONCES | CHAR(1) | Y |  |  |
| 288 | COD_FIS_CONCES | VARCHAR2(14) | Y |  |  |
| 289 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |
| 290 | IND_PORT_CAT44 | CHAR(1) | Y |  |  |
| 291 | NUM_AUTENTIC_NFE_AUX | NUMBER(9) | Y |  |  |
| 292 | VLR_BASE_INSS_RURAL | NUMBER(17,2) | Y |  |  |
| 293 | VLR_ALIQ_INSS_RURAL | NUMBER(7,4) | Y |  |  |
| 294 | VLR_INSS_RURAL | NUMBER(17,2) | Y |  |  |
| 295 | IDENT_CLASSE_CONSUMO_SEF_PE | NUMBER(12) | Y |  |  |
| 296 | COD_CLASSE_CONSUMO_SEF_PE | VARCHAR2(2) | Y |  |  |
| 297 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 298 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 299 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 300 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 301 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 302 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 303 | IND_NAT_FRETE | CHAR(1) | Y |  |  |
| 304 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  |  |
| 305 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 306 | IND_VENDA_CANC | CHAR(1) | Y |  |  |
| 307 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 308 | IND_NF_CONTINGENCIA | VARCHAR2(1) | Y |  |  |
| 309 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 310 | VLR_ANTECIP_TRIB | NUMBER(17,2) | Y |  |  |
| 311 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 312 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 313 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 314 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |
| 315 | NUM_NFTS | VARCHAR2(12) | Y |  |  |
| 316 | IND_NF_VENDA_TERCEIROS | CHAR(1) | Y |  |  |
| 317 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 318 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 319 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 320 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 321 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 322 | IDENTIF_DOCFIS | VARCHAR2(128) | Y |  |  |
| 323 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 324 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 325 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 326 | IND_PREST_SERV | CHAR(1) | Y |  |  |
| 327 | IND_TIPO_PROC | CHAR(1) | Y |  |  |
| 328 | NUM_PROC_JUR | VARCHAR2(20) | Y |  |  |
| 329 | IND_DEC_PROC | CHAR(1) | Y |  |  |
| 330 | IND_TIPO_AQUIS | CHAR(1) | Y |  |  |
| 331 | VLR_DESC_GILRAT | NUMBER(17,2) | Y |  |  |
| 332 | VLR_DESC_SENAR | NUMBER(17,2) | Y |  |  |
| 333 | CNPJ_SUBEMPREITEIRO | VARCHAR2(14) | Y |  |  |
| 334 | CNPJ_CPF_PROPRIETARIO_CNO | VARCHAR2(14) | Y |  |  |
| 335 | VLR_RET_SUBEMPREITADO | NUMBER(17,2) | Y |  |  |
| 336 | NUM_DOCFIS_SERV | VARCHAR2(60) | Y |  |  |
| 337 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 338 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 339 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 340 | VLR_CONTRIB_PREV | NUMBER(17,2) | Y |  |  |
| 341 | VLR_GILRAT | NUMBER(17,2) | Y |  |  |
| 342 | VLR_CONTRIB_SENAR | NUMBER(17,2) | Y |  |  |
| 343 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 344 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 345 | NUM_CERTIF_QUAL | VARCHAR2(10) | Y |  |  |
| 346 | OBS_REINF | VARCHAR2(250) | Y |  |  |
| 347 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 348 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 349 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 350 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 351 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 352 | VLR_IPI_DEV | NUMBER(17,2) | Y |  |  |
| 353 | VLR_SEST | NUMBER(17,2) | Y |  |  |
| 354 | VLR_SENAT | NUMBER(17,2) | Y |  |  |
| 355 | IND_FIN_EMISSAO_NFE | VARCHAR2(1) | Y |  |  |
| 356 | NUM_AUTENTIC_NFE_SUBST | VARCHAR2(80) | Y |  |  |
| 357 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 358 | DATA_INDEMISS | DATE | Y | CASE  WHEN (("COD_CLASS_DOC_FIS"='2' OR "COD_CL... |  |
| 359 | DATA_INDEMISN | DATE | Y | CASE  WHEN "COD_CLASS_DOC_FIS"='1' THEN NVL("DA... |  |
| 360 | V_DATA_TRAB | DATE | Y | NVL("DAT_ESCR_EXTEMP","DATA_FISCAL") |  |
| 361 | IND_TRIB_PRODUTOR_CP | VARCHAR2(1) | Y |  |  |
| 362 | IDENT_MODELO_NFE_SUBST | NUMBER(12) | Y |  |  |
| 363 | COD_MODELO_NFE_SUBST | VARCHAR2(2) | Y |  |  |
| 364 | COD_AUTENTIC_NFE_SUBST | VARCHAR2(32) | Y |  |  |
| 365 | VLR_ENERGIA_INJ | NUMBER(17,2) | Y |  |  |
| 366 | VLR_OUTRAS_DED | NUMBER(17,2) | Y |  |  |
| 367 | IND_TP_FAT_NFE | VARCHAR2(1) | Y |  |  |
| 368 | IND_TP_AMB_NFE | VARCHAR2(1) | Y |  |  |
| 369 | COD_NF_NFE | VARCHAR2(7) | Y |  |  |
| 370 | IND_PRE_PAGO | VARCHAR2(1) | Y |  |  |
| 371 | IND_SESSAO_REDE | VARCHAR2(1) | Y |  |  |
| 372 | DAT_INI_CONTRATO | DATE | Y |  |  |
| 373 | DAT_FIM_CONTRATO | DATE | Y |  |  |
| 374 | NUM_TERMINAL_TEL | VARCHAR2(12) | Y |  |  |
| 375 | IDENT_UF_TERMINAL_TEL | NUMBER(12) | Y |  |  |
| 376 | UF_TERMINAL_TEL | VARCHAR2(2) | Y |  |  |
| 377 | VLR_ICMS_DESONERADO | NUMBER(17,2) | Y |  |  |
| 378 | VLR_FCP | NUMBER(17,2) | Y |  |  |
| 379 | VLR_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 380 | VLR_FUST | NUMBER(17,2) | Y |  |  |
| 381 | CNPJ_DOWNLOAD | VARCHAR2(14) | Y |  |  |
| 382 | CPF_DOWNLOAD | VARCHAR2(11) | Y |  |  |
| 383 | VLR_CSLL_RETIDO | NUMBER(17,2) | Y |  |  |
| 384 | VLR_IRRF_RETIDO | NUMBER(17,2) | Y |  |  |
| 385 | INSC_EST_VIRTUAL | VARCHAR2(14) | Y |  |  |
| 386 | PERIOD_APUR_SUBST | VARCHAR2(6) | Y |  |  |
| 387 | COD_MOTIVO_SUBST | VARCHAR2(2) | Y |  |  |
| 388 | COD_AUTENTIC_COF | VARCHAR2(44) | Y |  |  |
| 389 | CNPJ_EMIT_FATURAMENTO | VARCHAR2(14) | Y |  |  |
| 390 | UF_EMIT_FATURAMENTO | VARCHAR2(2) | Y |  |  |
| 391 | IDENT_UF_EMIT_FATURAMENTO | NUMBER(12) | Y |  |  |
| 392 | CNPJ_EMIT_COF | VARCHAR2(14) | Y |  |  |
| 393 | IDENT_MODELO_COF | NUMBER(12) | Y |  |  |
| 394 | COD_MODELO_COF | VARCHAR2(2) | Y |  |  |
| 395 | SERIE_DOCFIS_COF | VARCHAR2(3) | Y |  |  |
| 396 | NUM_DOCFIS_COF | VARCHAR2(12) | Y |  |  |
| 397 | ANO_MES_COF | VARCHAR2(6) | Y |  |  |
| 398 | COD_HASH_COF | VARCHAR2(32) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, USERNAME

---

## TMP_X08_ITENS_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | IDENT_ITEM_MERC | NUMBER(12) | N |  |  |
| 3 | USERNAME | VARCHAR2(50) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | DATA_FISCAL | DATE | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | N |  |  |
| 8 | NORM_DEV | CHAR(1) | N |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 16 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 17 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 18 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 19 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 20 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 21 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 22 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 23 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 24 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 25 | VALID_BEM | DATE | Y |  |  |
| 26 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 27 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 28 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 29 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 30 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 31 | DESCRICAO_COMPL | VARCHAR2(255) | Y |  |  |
| 32 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 33 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 34 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 35 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 36 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 37 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 38 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 39 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 40 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 41 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 42 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 43 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 44 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 45 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 46 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 47 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 48 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 49 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 50 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 51 | IDENT_FEDERAL | NUMBER(12) | Y |  |  |
| 52 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 53 | IND_IPI_INCLUSO | CHAR(1) | Y |  |  |
| 54 | NUM_ROMANEIO | VARCHAR2(12) | Y |  |  |
| 55 | DATA_ROMANEIO | DATE | Y |  |  |
| 56 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 57 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 58 | VLR_ITEM_CONVER | NUMBER(17,2) | Y |  |  |
| 59 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 60 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 61 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 62 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 63 | VLR_OUTROS3 | NUMBER(17,2) | Y |  |  |
| 64 | VLR_OUTROS4 | NUMBER(17,2) | Y |  |  |
| 65 | VLR_OUTROS5 | NUMBER(17,2) | Y |  |  |
| 66 | VLR_ALIQ_OUTROS1 | NUMBER(7,4) | Y |  |  |
| 67 | VLR_ALIQ_OUTROS2 | NUMBER(7,4) | Y |  |  |
| 68 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 69 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 70 | DIF_ALIQ_TRIB_ICMS | NUMBER(7,4) | Y |  |  |
| 71 | OBS_TRIBUTO_ICMS | VARCHAR2(45) | Y |  |  |
| 72 | IDENT_DET_OP_ICMS | NUMBER(12) | Y |  |  |
| 73 | COD_DET_OP_ICMS | VARCHAR2(5) | Y |  |  |
| 74 | ALIQ_TRIBUTO_IPI | NUMBER(7,4) | Y |  |  |
| 75 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 76 | OBS_TRIBUTO_IPI | VARCHAR2(45) | Y |  |  |
| 77 | IDENT_DET_OP_IPI | NUMBER(12) | Y |  |  |
| 78 | COD_DET_OP_IPI | VARCHAR2(5) | Y |  |  |
| 79 | ALIQ_TRIBUTO_ICMSS | NUMBER(7,4) | Y |  |  |
| 80 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 81 | OBS_TRIBUTO_ICMSS | VARCHAR2(45) | Y |  |  |
| 82 | IDENT_DET_OP_ICMSS | NUMBER(12) | Y |  |  |
| 83 | COD_DET_OP_ICMSS | VARCHAR2(5) | Y |  |  |
| 84 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 85 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 86 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 87 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 88 | VLR_BASE_IPI_1 | NUMBER(17,2) | Y |  |  |
| 89 | VLR_BASE_IPI_2 | NUMBER(17,2) | Y |  |  |
| 90 | VLR_BASE_IPI_3 | NUMBER(17,2) | Y |  |  |
| 91 | VLR_BASE_IPI_4 | NUMBER(17,2) | Y |  |  |
| 92 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 93 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 94 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 95 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 96 | COD_OBS_VCONT_COMP | VARCHAR2(10) | Y |  |  |
| 97 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 98 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  |  |
| 99 | VLR_OUTROS_IPI | NUMBER(17,2) | Y |  |  |
| 100 | IND_RESP_VCONT_ITM | CHAR(1) | Y |  |  |
| 101 | NUM_ATO_CONCES | VARCHAR2(15) | Y |  |  |
| 102 | DAT_EMBARQUE | DATE | Y |  |  |
| 103 | NUM_REG_EXP | VARCHAR2(12) | Y |  |  |
| 104 | NUM_DESP_EXP | VARCHAR2(11) | Y |  |  |
| 105 | VLR_TOM_SERVICO | NUMBER(17,2) | Y |  |  |
| 106 | VLR_DESP_MOEDA_EXP | NUMBER(17,2) | Y |  |  |
| 107 | COD_MOEDA_NEGOC | VARCHAR2(10) | Y |  |  |
| 108 | COD_PAIS_DEST_ORIG | VARCHAR2(3) | Y |  |  |
| 109 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 110 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 111 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 112 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 113 | VLR_CONT_IT_IN | NUMBER(17,2) | Y |  |  |
| 114 | VLR_ICMS_IN | NUMBER(17,2) | Y |  |  |
| 115 | VLR_ICMS_B1_IN | NUMBER(17,2) | Y |  |  |
| 116 | VLR_ICMS_B2_IN | NUMBER(17,2) | Y |  |  |
| 117 | VLR_ICMS_B3_IN | NUMBER(17,2) | Y |  |  |
| 118 | VLR_ICMS_B4_IN | NUMBER(17,2) | Y |  |  |
| 119 | VLR_IPI_IN | NUMBER(17,2) | Y |  |  |
| 120 | VLR_IPI_B1_IN | NUMBER(17,2) | Y |  |  |
| 121 | VLR_IPI_B2_IN | NUMBER(17,2) | Y |  |  |
| 122 | VLR_IPI_B3_IN | NUMBER(17,2) | Y |  |  |
| 123 | VLR_IPI_B4_IN | NUMBER(17,2) | Y |  |  |
| 124 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 125 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 126 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 127 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 128 | BASE_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 129 | VLR_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 130 | ALIQ_ICMS_ORIGDEST | NUMBER(7,4) | Y |  |  |
| 131 | VLR_DESC_CONDIC | NUMBER(17,2) | Y |  |  |
| 132 | VLR_BASE_ICMSS_2 | NUMBER(17,2) | Y |  |  |
| 133 | VLR_BASE_ICMSS_3 | NUMBER(17,2) | Y |  |  |
| 134 | VLR_BASE_ICMSS_4 | NUMBER(17,2) | Y |  |  |
| 135 | VLR_CUSTO_TRANSF | NUMBER(17,6) | Y |  |  |
| 136 | PERC_RED_BASE_ICMS | NUMBER(7,4) | Y |  |  |
| 137 | QTD_EMBARCADA | NUMBER(17,6) | Y |  |  |
| 138 | DAT_REGISTRO_EXP | DATE | Y |  |  |
| 139 | DAT_DESPACHO | DATE | Y |  |  |
| 140 | DAT_AVERBACAO | DATE | Y |  |  |
| 141 | DAT_DI | DATE | Y |  |  |
| 142 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 143 | DSC_MOT_OCOR | VARCHAR2(45) | Y |  |  |
| 144 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 145 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 146 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 147 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 148 | VLR_BASE_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 149 | VLR_TRIB_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 150 | VLR_PERC_PRES_ICMS | NUMBER(7,4) | Y |  |  |
| 151 | VLR_PRECO_BASE_ST | NUMBER(17,2) | Y |  |  |
| 152 | IDENT_OPER_OIL | NUMBER(12) | Y |  |  |
| 153 | COD_OPER_OIL | VARCHAR2(10) | Y |  |  |
| 154 | COD_DCR | VARCHAR2(15) | Y |  |  |
| 155 | IDENT_PROJETO | NUMBER(12) | Y |  |  |
| 156 | COD_PROJETO | VARCHAR2(20) | Y |  |  |
| 157 | DAT_OPERACAO | DATE | Y |  |  |
| 158 | USUARIO | VARCHAR2(40) | Y |  |  |
| 159 | IND_MOV_FIS | CHAR(1) | Y |  |  |
| 160 | CHASSI | VARCHAR2(17) | Y |  |  |
| 161 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 162 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 163 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 164 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 165 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 166 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 167 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 168 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 169 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 170 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 171 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 172 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 173 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 174 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 175 | IND_FORNEC_ICMSS | CHAR(1) | Y |  |  |
| 176 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 177 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 178 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 179 | DAT_PGTO_GNRE_DARJ | DATE | Y |  |  |
| 180 | VLR_CUSTO_UNIT | NUMBER(17,2) | Y |  |  |
| 181 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 182 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 183 | VLR_FECP_ICMS | NUMBER(17,2) | Y |  |  |
| 184 | VLR_FECP_DIFALIQ | NUMBER(17,2) | Y |  |  |
| 185 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 186 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  |  |
| 187 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 188 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 189 | COD_TRIB_IPI | VARCHAR2(2) | Y |  |  |
| 190 | LOTE_MEDICAMENTO | VARCHAR2(50) | Y |  |  |
| 191 | VALID_MEDICAMENTO | DATE | Y |  |  |
| 192 | IND_BASE_MEDICAMENTO | CHAR(1) | Y |  |  |
| 193 | VLR_PRECO_MEDICAMENTO | NUMBER(17,2) | Y |  |  |
| 194 | IND_TIPO_ARMA | CHAR(1) | Y |  |  |
| 195 | NUM_SERIE_ARMA | VARCHAR2(50) | Y |  |  |
| 196 | NUM_CANO_ARMA | VARCHAR2(50) | Y |  |  |
| 197 | DSC_ARMA | VARCHAR2(100) | Y |  |  |
| 198 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 199 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 200 | COD_EX_NCM | VARCHAR2(2) | Y |  |  |
| 201 | COD_EX_IMP | VARCHAR2(2) | Y |  |  |
| 202 | CNPJ_OPERADORA | VARCHAR2(14) | Y |  |  |
| 203 | CPF_OPERADORA | VARCHAR2(14) | Y |  |  |
| 204 | IDENT_UF_OPERADORA | NUMBER(12) | Y |  |  |
| 205 | COD_UF_OPERADORA | VARCHAR2(2) | Y |  |  |
| 206 | INS_EST_OPERADORA | VARCHAR2(14) | Y |  |  |
| 207 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 208 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  |  |
| 209 | VLR_TERCEIROS | NUMBER(17,2) | Y |  |  |
| 210 | VLR_PRECO_SUGER | NUMBER(17,2) | Y |  |  |
| 211 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 212 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 213 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 214 | COD_OPER_ESP_ST | CHAR(1) | Y |  |  |
| 215 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 216 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 217 | VLR_DIFAL_FRETE | NUMBER(17,2) | Y |  |  |
| 218 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' |  |
| 219 | COD_ENQUAD_IPI | VARCHAR2(3) | Y |  |  |
| 220 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 221 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 222 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 223 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 224 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 225 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 226 | ITEM_PORT_TARE | VARCHAR2(2) | Y |  |  |
| 227 | VLR_FUNRURAL | NUMBER(17,2) | Y |  |  |
| 228 | IND_TP_PROD_MEDIC | CHAR(1) | Y |  |  |
| 229 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 230 | COD_TP_LANCTO | NUMBER(6) | Y |  |  |
| 231 | VLR_PERC_CRED_OUT | NUMBER(7,4) | Y |  |  |
| 232 | VLR_CRED_OUT | NUMBER(17,2) | Y |  |  |
| 233 | VLR_ICMS_DCA | NUMBER(21,6) | Y |  |  |
| 234 | VLR_PIS_EXP | NUMBER(17,2) | Y |  |  |
| 235 | VLR_PIS_TRIB | NUMBER(17,2) | Y |  |  |
| 236 | VLR_PIS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 237 | VLR_COFINS_EXP | NUMBER(17,2) | Y |  |  |
| 238 | VLR_COFINS_TRIB | NUMBER(17,2) | Y |  |  |
| 239 | VLR_COFINS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 240 | COD_ENQ_LEGAL | NUMBER(4) | Y |  |  |
| 241 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |
| 242 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 243 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 244 | IND_NATUREZA_FRETE | CHAR(1) | Y |  |  |
| 245 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 246 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 247 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 248 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 249 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 250 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 251 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |
| 252 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |
| 253 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 254 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 255 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 256 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 257 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 258 | INDICE_PROD_ACAB | VARCHAR2(3) | Y |  |  |
| 259 | VLR_BASE_DIA_AM | NUMBER(17,2) | Y |  |  |
| 260 | VLR_ALIQ_DIA_AM | NUMBER(7,4) | Y |  |  |
| 261 | VLR_ICMS_DIA_AM | NUMBER(17,2) | Y |  |  |
| 262 | VLR_ADUANEIRO | NUMBER(17,2) | Y |  |  |
| 263 | COD_SITUACAO_PIS_ST | NUMBER(2) | Y |  |  |
| 264 | COD_SITUACAO_COFINS_ST | NUMBER(2) | Y |  |  |
| 265 | VLR_ALIQ_DCIP | NUMBER(7,4) | Y |  |  |
| 266 | NUM_LI | VARCHAR2(10) | Y |  |  |
| 267 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 268 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 269 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 270 | VLR_DIF_DUB | NUMBER(17,2) | Y |  |  |
| 271 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 272 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 273 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 274 | IND_MOTIVO_RES | CHAR(1) | Y |  |  |
| 275 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  |  |
| 276 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  |  |
| 277 | NUM_AUTENTIC_NFE_RET | VARCHAR2(80) | Y |  |  |
| 278 | NUM_ITEM_RET | NUMBER(5) | Y |  |  |
| 279 | IDENT_FIS_JUR_RET | NUMBER(12) | Y |  |  |
| 280 | IND_FIS_JUR_RET | CHAR(1) | Y |  |  |
| 281 | COD_FIS_JUR_RET | VARCHAR2(14) | Y |  |  |
| 282 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 283 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 284 | IDENT_CFO_DCIP | NUMBER(12) | Y |  |  |
| 285 | COD_CFO_DCIP | VARCHAR2(4) | Y |  |  |
| 286 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 287 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 288 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 289 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 290 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 291 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 292 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 293 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 294 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 295 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 296 | IDENT_PROC_ADJ_PRINC | NUMBER(12) | Y |  |  |
| 297 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 298 | NUM_PROC_ADJ_PRINC | VARCHAR2(21) | Y |  |  |
| 299 | IDENT_SUSP_TBT_PRINC | NUMBER(12) | Y |  |  |
| 300 | COD_SUSP_TBT_PRINC | VARCHAR2(14) | Y |  |  |
| 301 | IDENT_PROC_ADJ_ADIC | NUMBER(12) | Y |  |  |
| 302 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 303 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 304 | IDENT_SUSP_TBT_ADIC | NUMBER(12) | Y |  |  |
| 305 | COD_SUSP_TBT_ADIC | VARCHAR2(14) | Y |  |  |
| 306 | VLR_IPI_DEV | NUMBER(17,2) | Y |  |  |
| 307 | COD_BENEFICIO | VARCHAR2(10) | Y |  |  |
| 308 | VLR_ABAT_NTRIBUTADO | NUMBER(17,2) | Y |  |  |
| 309 | VLR_CREDITO_MVA_SN | NUMBER(17,2) | Y |  |  |
| 310 | VLR_DESONERADO_ICMS | NUMBER(17,2) | Y |  |  |
| 311 | VLR_DIFERIDO_ICMS | NUMBER(17,2) | Y |  |  |
| 312 | VLR_EXC_BC_PIS | NUMBER(17,2) | Y |  |  |
| 313 | VLR_EXC_BC_COFINS | NUMBER(17,2) | Y |  |  |
| 314 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 315 | VLR_FECP_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 316 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 317 | COD_GRUPO_CCLASS | VARCHAR2(3) | Y |  |  |
| 318 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 319 | COD_AUTENTIC_NFE_ANT | VARCHAR2(44) | Y |  |  |
| 320 | NUM_ITEM_NFE_ANT | VARCHAR2(4) | Y |  |  |
| 321 | COD_CCLASS | VARCHAR2(7) | Y |  |  |
| 322 | CNPJ_OPER_LD | VARCHAR2(14) | Y |  |  |
| 323 | DAT_EXPIRA_CRED | DATE | Y |  |  |
| 324 | IND_DEVOLUCAO | VARCHAR2(1) | Y |  |  |
| 325 | TIPO_ITEM | VARCHAR2(1) | Y |  |  |
| 326 | IDENT_PRODUTO_ACABADO | NUMBER(12) | Y |  |  |
| 327 | IND_PRODUTO_ACABADO | VARCHAR2(1) | Y |  |  |
| 328 | COD_PRODUTO_ACABADO | VARCHAR2(60) | Y |  |  |
| 329 | IND_NF_ANT | VARCHAR2(1) | Y |  |  |
| 330 | NUM_GUIA_RECOL | VARCHAR2(16) | Y |  |  |
| 331 | DAT_EMISSAO_GUIA | DATE | Y |  |  |
| 332 | DAT_PAGTO_GUIA | DATE | Y |  |  |
| 333 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 334 | COD_ESTADO_RECEITA_EST | VARCHAR2(2) | Y |  |  |
| 335 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 336 | VLR_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 337 | QTD_PROD_20C | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, USERNAME

---

## TMP_X09_ITENS_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | IDENT_ITEM_SERV | NUMBER(12) | N |  |  |
| 3 | USERNAME | VARCHAR2(50) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | DATA_FISCAL | DATE | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | N |  |  |
| 8 | NORM_DEV | CHAR(1) | N |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | N |  |  |
| 17 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 18 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 19 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 20 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 21 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 22 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 23 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 24 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 25 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 26 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 27 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 28 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 29 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 30 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 31 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 32 | VLR_SERVICO_CONV | NUMBER(18,4) | Y |  |  |
| 33 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 34 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 35 | DIF_ALIQ_TRIB_ICMS | NUMBER(7,4) | Y |  |  |
| 36 | OBS_TRIBUTO_ICMS | VARCHAR2(45) | Y |  |  |
| 37 | IDENT_DET_OP_ICMS | NUMBER(12) | Y |  |  |
| 38 | COD_DET_OP_ICMS | VARCHAR2(5) | Y |  |  |
| 39 | ALIQ_TRIBUTO_IR | NUMBER(7,4) | Y |  |  |
| 40 | VLR_TRIBUTO_IR | NUMBER(17,2) | Y |  |  |
| 41 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |
| 42 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 43 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 44 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 45 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 46 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 47 | VLR_BASE_IR_1 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_BASE_IR_2 | NUMBER(17,2) | Y |  |  |
| 49 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 50 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 51 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 52 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 53 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 54 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 55 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 56 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 57 | DAT_OPERACAO | DATE | Y |  |  |
| 58 | USUARIO | VARCHAR2(40) | Y |  |  |
| 59 | COMPL_ISENCAO | VARCHAR2(5) | Y |  |  |
| 60 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 61 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 62 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 63 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 64 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 65 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 66 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 67 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 68 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 69 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 70 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 71 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 72 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 73 | COD_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 74 | VLR_MAT_PROP | NUMBER(17,2) | Y |  |  |
| 75 | VLR_MAT_TERC | NUMBER(17,2) | Y |  |  |
| 76 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 77 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 78 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  |  |
| 79 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 80 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 81 | VLR_OUT_DESP | NUMBER(17,2) | Y |  |  |
| 82 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 83 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 84 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 85 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 86 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' |  |
| 87 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 88 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 89 | VLR_PIS_EXP | NUMBER(17,2) | Y |  |  |
| 90 | VLR_PIS_TRIB | NUMBER(17,2) | Y |  |  |
| 91 | VLR_PIS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 92 | VLR_COFINS_EXP | NUMBER(17,2) | Y |  |  |
| 93 | VLR_COFINS_TRIB | NUMBER(17,2) | Y |  |  |
| 94 | VLR_COFINS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 95 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 96 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 97 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 98 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 99 | IND_LOCAL_EXEC_SERV | CHAR(1) | Y |  |  |
| 100 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 101 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 102 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 103 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 104 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 105 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 106 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 107 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 108 | IDENT_NBS | NUMBER(12) | Y |  |  |
| 109 | COD_NBS | VARCHAR2(9) | Y |  |  |
| 110 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 111 | VLR_TOT_RET | NUMBER(17,2) | Y |  |  |
| 112 | VLR_DEDUCAO_NF | NUMBER(17,2) | Y |  |  |
| 113 | VLR_RET_NF | NUMBER(17,2) | Y |  |  |
| 114 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 115 | VLR_ALIQ_ISS_RETIDO | NUMBER(7,4) | Y |  |  |
| 116 | COD_SIT_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 117 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 118 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 119 | VLR_DED_ALIM | NUMBER(17,2) | Y |  |  |
| 120 | VLR_DED_TRANS | NUMBER(17,2) | Y |  |  |
| 121 | IDENT_PROC_ADJ_PRINC | NUMBER(12) | Y |  |  |
| 122 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 123 | NUM_PROC_ADJ_PRINC | VARCHAR2(21) | Y |  |  |
| 124 | IDENT_SUSP_TBT_PRINC | NUMBER(12) | Y |  |  |
| 125 | COD_SUSP_TBT_PRINC | VARCHAR2(14) | Y |  |  |
| 126 | IDENT_PROC_ADJ_ADIC | NUMBER(12) | Y |  |  |
| 127 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 128 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 129 | IDENT_SUSP_TBT_ADIC | NUMBER(12) | Y |  |  |
| 130 | COD_SUSP_TBT_ADIC | VARCHAR2(14) | Y |  |  |
| 131 | NUM_PROC_ADJ_PREST_PRINC | VARCHAR2(21) | Y |  |  |
| 132 | NUM_PROC_ADJ_PREST_ADIC | VARCHAR2(21) | Y |  |  |
| 133 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 134 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 135 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 136 | VLR_ABAT_NTRIBUTADO | NUMBER(17,2) | Y |  |  |
| 137 | COD_ATIV_RJ | NUMBER(7) | Y |  |  |
| 138 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 139 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 140 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 141 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 142 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 143 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 144 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 145 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 146 | DSC_SERVICO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_SERVICO, NUM_ITEM, USERNAME

---

## TMP_X110_ITEM_ROMANEIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | IDENT_PRODUTO_DOCFIS | NUMBER(12) | Y |  |  |
| 16 | NUM_ROMANEIO | VARCHAR2(12) | N |  |  |
| 17 | NUM_ITEM_ROMANEIO | NUMBER(5) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | NUM_ITEM | NUMBER(10) | Y |  |  |
| 21 | IND_PRODUTO_DOCFIS | CHAR(1) | Y |  |  |
| 22 | COD_PRODUTO_DOCFIS | VARCHAR2(60) | Y |  |  |
| 23 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 24 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 25 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 26 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 27 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 28 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 29 | PRECO_UNITARIO | NUMBER(17,2) | Y |  |  |
| 30 | PRECO_TOTAL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_ROMANEIO, NUM_ITEM_ROMANEIO, USERNAME

---

## TMP_X112_OBS_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 15 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 16 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 17 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 18 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 19 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 22 | VINCULACAO | CHAR(1) | Y |  |  |
| 23 | DSC_INFO_FISCO | VARCHAR2(2000) | Y |  |  |
| 24 | DSC_INFO_CONTRIB | VARCHAR2(3000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OBSERVACAO, IND_ICOMPL_LANCTO, USERNAME

---

## TMP_X113_AJUSTE_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 15 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 16 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 17 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 21 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 22 | DSC_COMP_AJUSTE | VARCHAR2(255) | Y |  |  |
| 23 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | ALIQUOTA_ICMS | NUMBER(7,4) | Y |  |  |
| 25 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OBSERVACAO, IND_ICOMPL_LANCTO, COD_AJUSTE_SPED, DISCRI_ITEM, USERNAME

---

## TMP_X114_PROC_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 15 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 16 | NUM_PROCESSO | VARCHAR2(60) | N |  |  |
| 17 | ORIG_PROCESSO | CHAR(1) | N |  |  |
| 18 | NUM_ITEM | NUMBER(5) | N |  |  |
| 19 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 20 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 21 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 22 | IDENT_PROC_REF | NUMBER(12) | Y |  |  |
| 23 | NUM_PROC_REF | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OBSERVACAO, IND_ICOMPL_LANCTO, NUM_PROCESSO, ORIG_PROCESSO, NUM_ITEM, USERNAME

---

## TMP_X115_DOC_ARRCD_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 15 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 16 | IND_TP_DOC_ARREC | CHAR(1) | N |  |  |
| 17 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 18 | NUM_DOC_ARREC | VARCHAR2(50) | N |  |  |
| 19 | COD_AUTEN_BANC | VARCHAR2(100) | N |  |  |
| 20 | DATA_VENC_DOC_ARREC | DATE | N |  |  |
| 21 | VLR_TOT_DOC_ARREC | NUMBER(17,2) | N |  |  |
| 22 | DATA_PGTO_DOC_ARREC | DATE | N |  |  |
| 23 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 24 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 25 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 26 | IDENT_ESTADO | NUMBER(8) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OBSERVACAO, IND_ICOMPL_LANCTO, IND_TP_DOC_ARREC, IDENT_ESTADO, NUM_DOC_ARREC, COD_AUTEN_BANC, DATA_VENC_DOC_ARREC, USERNAME

---

## TMP_X116_DOCFIS_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 15 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 16 | DATA_FISCAL_REF | DATE | N |  |  |
| 17 | MOVTO_E_S_REF | CHAR(1) | N |  |  |
| 18 | IND_FIS_JUR_REF | CHAR(1) | N |  |  |
| 19 | COD_FIS_JUR_REF | VARCHAR2(14) | N |  |  |
| 20 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 21 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 22 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | N |  |  |
| 23 | COD_MODELO_REF | VARCHAR2(2) | Y |  |  |
| 24 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 25 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 26 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 27 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 28 | IDENT_FIS_JUR_REF | NUMBER(12) | Y |  |  |
| 29 | IDENT_MODELO_REF | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OBSERVACAO, IND_ICOMPL_LANCTO, DATA_FISCAL_REF, MOVTO_E_S_REF, IND_FIS_JUR_REF, COD_FIS_JUR_REF, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, USERNAME

---

## TMP_X117_CUPOM_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 15 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 16 | COD_EQUIPAMENTO | VARCHAR2(9) | N |  |  |
| 17 | NUM_DOC | VARCHAR2(12) | N |  |  |
| 18 | DATA_EMISSAO | DATE | N |  |  |
| 19 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 20 | COD_FABRICACAO_ECF | VARCHAR2(21) | Y |  |  |
| 21 | NUM_CHAVE_CFE | VARCHAR2(80) | Y |  |  |
| 22 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 23 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 24 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 25 | IDENT_MODELO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OBSERVACAO, IND_ICOMPL_LANCTO, COD_EQUIPAMENTO, NUM_DOC, DATA_EMISSAO, USERNAME

---

## TMP_X118_COLETA_ENTRG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 15 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 16 | NUM_SEQ | NUMBER(3) | N |  |  |
| 17 | COD_VIA_TRANSP | VARCHAR2(5) | N |  |  |
| 18 | IDENT_UF_COLETA | NUMBER(12) | Y |  |  |
| 19 | COD_MUNIC_COLETA | NUMBER(12) | Y |  |  |
| 20 | CNPJ_COLETA | VARCHAR2(14) | Y |  |  |
| 21 | IE_COLETA | VARCHAR2(14) | Y |  |  |
| 22 | IDENT_UF_ENTREGA | NUMBER(12) | Y |  |  |
| 23 | COD_MUNIC_ENTREGA | NUMBER(12) | Y |  |  |
| 24 | CNPJ_ENTREGA | VARCHAR2(14) | Y |  |  |
| 25 | IE_ENTREGA | VARCHAR2(14) | Y |  |  |
| 26 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 27 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 28 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 29 | IDENT_VIA_TRANSP | NUMBER(12) | Y |  |  |
| 30 | COD_UF_COLETA | VARCHAR2(2) | Y |  |  |
| 31 | COD_UF_ENTREGA | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OBSERVACAO, IND_ICOMPL_LANCTO, NUM_SEQ, COD_VIA_TRANSP, USERNAME

---

## TMP_X119_ITENS_MEDICAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | NUM_FAB_LOTE | VARCHAR2(50) | N |  |  |
| 16 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 17 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 18 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 19 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 20 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 21 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 22 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 23 | QTD_LOTE | NUMBER(17,6) | Y |  |  |
| 24 | DAT_FABRIC | DATE | Y |  |  |
| 25 | DAT_VALIDADE | DATE | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_FAB_LOTE, USERNAME

---

## TMP_X120_ITENS_ARMA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | NUM_SERIE_FABRIC | VARCHAR2(50) | N |  |  |
| 16 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 17 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 18 | DSC_COMPLEM | VARCHAR2(150) | Y |  |  |
| 19 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 20 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 21 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 22 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 23 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_SERIE_FABRIC, USERNAME

---

## TMP_X130_POR_NOTA
**Comment**: Tabela utilizada na emissao do livro P2/P2A para armazenar da numeracao de NFE baseada nas colunas NUM_DOCFIS_INI e NUM_DOCFIS_FIN da tabela X130_NFE_DENEGADA_INUTILIZADA.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | DATA_REF | DATE | N |  |  |
| 8 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 9 | IND_SITUACAO | CHAR(1) | N |  |  |
| 10 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_REF, IDENT_MODELO, IND_SITUACAO, USUARIO

---

## TMP_X138_ITEM_CUPOM_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 15 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 16 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 17 | NUM_DOC | VARCHAR2(12) | N |  |  |
| 18 | DATA_EMISSAO | DATE | N |  |  |
| 19 | NUM_DOC_ITEM | VARCHAR2(12) | N |  |  |
| 20 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 21 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 22 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 23 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 24 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 25 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 26 | QUANTIDADE | NUMBER(17,3) | Y |  |  |
| 27 | NUM_RELATORIO | NUMBER(6) | Y |  |  |
| 28 | DATA_RELATORIO | DATE | Y |  |  |
| 29 | CNPJ_CGC | VARCHAR2(14) | Y |  |  |
| 30 | VLR_MERCADORIA | NUMBER(17,2) | Y |  |  |
| 31 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OBSERVACAO, IND_ICOMPL_LANCTO, COD_EQUIPAMENTO, NUM_DOC, DATA_EMISSAO, NUM_DOC_ITEM, USERNAME

---

## TMP_X158_CRED_EXTEMP_ITEM_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | DAT_LANC_PIS_COFINS | DATE | N |  |  |
| 16 | IND_PIS_COFINS_EXTEMP | CHAR(1) | N |  |  |
| 17 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 18 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 19 | IND_BEM_PATR | CHAR(1) | Y |  |  |
| 20 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 21 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 22 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 23 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 24 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 25 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 26 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 27 | IND_NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 28 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 29 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 30 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 32 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 33 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 34 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 35 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 36 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 37 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 38 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 39 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 40 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 41 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 42 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 43 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 44 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 45 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 46 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 47 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, USERNAME

---

## TMP_X159_CRED_EXTEMP_ITEM_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 15 | NUM_ITEM | NUMBER(5) | N |  |  |
| 16 | DAT_LANC_PIS_COFINS | DATE | N |  |  |
| 17 | IND_PIS_COFINS_EXTEMP | CHAR(1) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 21 | IND_NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 22 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 23 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 24 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 26 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 27 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 28 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 29 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 30 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 31 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 32 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 33 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 34 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 35 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 36 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 37 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_SERVICO, NUM_ITEM, USERNAME

---

## TMP_X192_ITENS_MERC_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | VARCHAR2(50) | N |  |  |
| 2 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 3 | USERNAME | VARCHAR2(50) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | DATA_FISCAL | DATE | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | N |  |  |
| 8 | NORM_DEV | CHAR(1) | N |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | IND_PRODUTO | CHAR(1) | N |  |  |
| 16 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 17 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 18 | NUM_ITEM | NUMBER(5) | N |  |  |
| 19 | IND_TIPO_REF | CHAR(1) | N |  |  |
| 20 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 21 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 22 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 23 | DATA_FISCAL_REF | DATE | Y |  |  |
| 24 | IND_FIS_JUR_REF | CHAR(1) | Y |  |  |
| 25 | COD_FIS_JUR_REF | VARCHAR2(14) | Y |  |  |
| 26 | NUM_ITEM_REF | NUMBER(5) | N |  |  |
| 27 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 28 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 29 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 30 | IDENT_FIS_JUR_REF | NUMBER(12) | Y |  |  |
| 31 | QTD_DEVOL | NUMBER(17,6) | Y |  |  |
| 32 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 33 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 34 | NUM_AUTENTIC_NFE_REF | VARCHAR2(80) | Y |  |  |
| 35 | NUM_CNPJ_NFE_REF | VARCHAR2(14) | Y |  |  |
| 36 | COD_MODELO_REF | VARCHAR2(2) | Y |  |  |
| 37 | IDENT_CAIXA_ECF_REF | NUMBER(12) | Y |  |  |
| 38 | COD_CAIXA_ECF_REF | VARCHAR2(3) | Y |  |  |
| 39 | NUM_COO_REF | VARCHAR2(9) | Y |  |  |
| 40 | DATA_EMISSAO_REF | DATE | Y |  |  |

**PK**: ID

**Indexes**:
- UK_TMP_X192_ITENS_MERC_REF (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, IND_TIPO_REF, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, DATA_FISCAL_REF, IND_FIS_JUR_REF, COD_FIS_JUR_REF, NUM_ITEM_REF, NUM_AUTENTIC_NFE_REF, NUM_CNPJ_NFE_REF, IDENT_CAIXA_ECF_REF, NUM_COO_REF, DATA_EMISSAO_REF, USERNAME)

---

## TMP_X205_FORMA_PAGTO_NFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_OPERACAO | VARCHAR2(6) | N |  |  |
| 15 | NUM_COMP_PAG | VARCHAR2(18) | N |  |  |
| 16 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 17 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 18 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 19 | IND_NAT_OPER | CHAR(1) | Y |  |  |
| 20 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 21 | CEP | NUMBER(8) | Y |  |  |
| 22 | NUM_PONTO_VENDA | VARCHAR2(8) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OPERACAO, NUM_COMP_PAG, USERNAME

---

## TMP_X206_ITENS_BOLETIM_CONF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | N |  |  |
| 18 | COD_CARACT | VARCHAR2(3) | N |  |  |
| 19 | NUM_BOLETIM_CONF | VARCHAR2(35) | N |  |  |
| 20 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 21 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 22 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 23 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 24 | COD_METODO | VARCHAR2(3) | Y |  |  |
| 25 | COD_VAL_CARACT | VARCHAR2(20) | Y |  |  |
| 26 | VAL_MASSA_ESPEC | NUMBER(19,4) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, COD_CARACT, NUM_BOLETIM_CONF, USERNAME

---

## TMP_X254_TERM_TEL_NFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | NUM_TERMINAL_TEL | VARCHAR2(15) | N |  |  |
| 15 | VLR_TOT_FATURA | NUMBER(17,2) | Y |  |  |
| 16 | UF_TERMINAL_TEL | VARCHAR2(2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_TERMINAL_TEL, USERNAME

**Indexes**:
- IX_TMP_X254_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X254_USER: (USERNAME)

---

## TMP_X263_DOCTO_PROC_SUSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 15 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 16 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 17 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 21 | VLR_PREV_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 22 | VLR_GIBRAT_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 23 | VLR_SENAR_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 26 | IND_EVENTO | CHAR(1) | N | '5' |  |
| 27 | IND_PRINC_ADIC | CHAR(1) | N | ' ' |  |
| 28 | VLR_N_RET | NUMBER(17,2) | Y |  |  |
| 29 | IND_TP_PROC_JUD | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TP_PROC_ADJ, NUM_PROC_ADJ, USERNAME

---

## TMP_X296_INFO_COMPL_ST_IT_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 22 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 23 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 24 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 25 | VLR_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 26 | IND_RESP_RET_ENT | VARCHAR2(1) | Y |  |  |
| 27 | VLR_UNIT_BC_ICMSS_ENT | NUMBER(19,6) | Y |  |  |
| 28 | VLR_UNIT_ICMSS_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 29 | VLR_UNIT_FCP_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 30 | COD_MOTIVO_SAI | VARCHAR2(5) | Y |  |  |
| 31 | VLR_UNIT_ICMS_OPER_SAI | NUMBER(19,6) | Y |  |  |
| 32 | VLR_UNIT_ICMS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 33 | VLR_UNIT_ICMSS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 34 | VLR_UNIT_FCP_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 35 | VLR_UNIT_ICMSS_REST_SAI | NUMBER(19,6) | Y |  |  |
| 36 | VLR_UNIT_FCP_REST_SAI | NUMBER(19,6) | Y |  |  |
| 37 | VLR_UNIT_ICMSS_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 38 | VLR_UNIT_FCP_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 39 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 40 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, USERNAME

---

## TMP_X3007_DOCTO_FISCAL_RT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | VARCHAR2(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_MUN_FT_GER_IBS_CBS | NUMBER(7) | Y |  |  |
| 15 | TIPO_CHAVE_DFE | NUMBER(1) | N |  |  |
| 16 | DESC_CHAVE_DFE | VARCHAR2(255) | Y |  |  |
| 17 | FINALIDADE_EMISSAO_NFE | NUMBER(1) | Y |  |  |
| 18 | FINALIDADE_EMISSAO_NFSE | NUMBER(1) | Y |  |  |
| 19 | TIPO_NF_DEBITO | VARCHAR2(2) | Y |  |  |
| 20 | TIPO_NF_CREDITO | VARCHAR2(2) | Y |  |  |
| 21 | IND_OPER_FINAL | NUMBER(1) | Y |  |  |
| 22 | IND_OPER_USO_CONS_PESSOAL | NUMBER(1) | Y |  |  |
| 23 | IND_OPER_FORNECIMENTO | VARCHAR2(10) | Y |  |  |
| 24 | IND_DESTINATARIO_SERVICO | NUMBER(1) | Y |  |  |
| 25 | IND_COMPRA_MOMENTO_OPER | NUMBER(1) | Y |  |  |
| 26 | IND_INTERM | NUMBER(1) | Y |  |  |
| 27 | IND_COMPRA_GOVERN | NUMBER(1) | Y |  |  |
| 28 | TIPO_OPERACAO | NUMBER(1) | Y |  |  |
| 29 | TIPO_ENTE_GOVERN | NUMBER(1) | Y |  |  |
| 30 | PERC_RED_ALIQ_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 31 | CST_IS | VARCHAR2(3) | Y |  |  |
| 32 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 33 | BC_IS | NUMBER(17,2) | Y |  |  |
| 34 | ALIQ_IS | NUMBER(7,4) | Y |  |  |
| 35 | ALIQ_ESP_UNID_MED_APR_IS | NUMBER(7,4) | Y |  |  |
| 36 | VLR_IS | NUMBER(17,2) | Y |  |  |
| 37 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 38 | QTD_TRIB_IS | NUMBER(15,4) | Y |  |  |
| 39 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 40 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 41 | BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 42 | VLR_MON_DOCREF_N_INC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 43 | ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 44 | VLR_IBS_UF | NUMBER(17,2) | Y |  |  |
| 45 | PERC_DIF_IBS_UF | NUMBER(7,4) | Y |  |  |
| 46 | VLR_DIF_IBS_UF | NUMBER(17,2) | Y |  |  |
| 47 | VLR_TRIB_DEV_IBS_UF | NUMBER(17,2) | Y |  |  |
| 48 | PERC_RED_ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 49 | ALIQ_EFET_IBS_UF | NUMBER(7,4) | Y |  |  |
| 50 | ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 51 | VLR_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 52 | PERC_DIF_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 53 | VLR_DIF_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 54 | VLR_BRUTO_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 55 | VLR_TRIB_DEV_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 56 | PERC_RED_ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 57 | ALIQ_EFET_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 58 | ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 59 | VLR_CBS | NUMBER(17,2) | Y |  |  |
| 60 | PERC_DIF_CBS | NUMBER(7,4) | Y |  |  |
| 61 | VLR_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 62 | VLR_BRUTO_CBS | NUMBER(17,2) | Y |  |  |
| 63 | VLR_TRIB_DEV_CBS | NUMBER(17,2) | Y |  |  |
| 64 | PERC_RED_ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 65 | ALIQ_EFET_CBS | NUMBER(7,4) | Y |  |  |
| 66 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 67 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 68 | ALIQ_IBS_TRIB_REG_UF | NUMBER(7,4) | Y |  |  |
| 69 | VLR_TRIB_REG_TRIB_IBS_UF | NUMBER(17,2) | Y |  |  |
| 70 | ALIQ_TRIB_REG_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 71 | VLR_TRIB_REG_TRIB_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 72 | ALIQ_TRIB_REG_CBS | NUMBER(7,4) | Y |  |  |
| 73 | VLR_TRIB_REG_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 74 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 75 | PERC_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 76 | ALIQ_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 77 | VLR_CRED_PRES_IBS | NUMBER(17,2) | Y |  |  |
| 78 | VLR_CRED_PRES_C_SUS_IBS | NUMBER(17,2) | Y |  |  |
| 79 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 80 | PERC_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 81 | ALIQ_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 82 | VLR_CRED_PRES_CBS | NUMBER(17,2) | Y |  |  |
| 83 | VLR_CRED_PRES_C_SUS_CBS | NUMBER(17,2) | Y |  |  |
| 84 | QTD_TRIB_MONO_IBS_CBS | NUMBER(15,4) | Y |  |  |
| 85 | ALIQ_AD_REM_IBS | NUMBER(7,4) | Y |  |  |
| 86 | ALIQ_AD_REM_CBS | NUMBER(7,4) | Y |  |  |
| 87 | VLR_MONO_IBS | NUMBER(17,2) | Y |  |  |
| 88 | VLR_MONO_CBS | NUMBER(17,2) | Y |  |  |
| 89 | QTD_TRIB_RET_MONO_IBS_CBS | NUMBER(15,4) | Y |  |  |
| 90 | ALIQ_AD_REM_RET_IBS | NUMBER(7,4) | Y |  |  |
| 91 | VLR_MONO_RET_IBS | NUMBER(17,2) | Y |  |  |
| 92 | ALIQ_AD_REM_RET_CBS | NUMBER(7,4) | Y |  |  |
| 93 | VLR_MONO_RET_CBS | NUMBER(17,2) | Y |  |  |
| 94 | QTD_TRIB_RET_ANT_IBS_CBS | NUMBER(15,4) | Y |  |  |
| 95 | ALIQ_AD_REM_RET_ANT_IBS | NUMBER(7,4) | Y |  |  |
| 96 | VLR_RET_ANT_IBS | NUMBER(17,2) | Y |  |  |
| 97 | ALIQ_AD_REM_RET_ANT_CBS | NUMBER(7,4) | Y |  |  |
| 98 | VLR_RET_ANT_CBS | NUMBER(17,2) | Y |  |  |
| 99 | PERC_DIF_MONO_IBS | NUMBER(7,4) | Y |  |  |
| 100 | VLR_MONO_DIF_IBS | NUMBER(17,2) | Y |  |  |
| 101 | PERC_DIF_MONO_CBS | NUMBER(7,4) | Y |  |  |
| 102 | VLR_MONO_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 103 | ALIQ_IBS_UF_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 104 | VLR_IBS_UF_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 105 | ALIQ_IBS_MUN_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 106 | VLR_IBS_MUN_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 107 | ALIQ_CBS_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 108 | VLR_CBS_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 109 | CHAVE_DFE_REF | VARCHAR2(44) | Y |  |  |
| 110 | VLR_TOT_IS | NUMBER(17,2) | Y |  |  |
| 111 | VLR_TOT_BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 112 | VLR_TOT_DIF_IBS_UF | NUMBER(17,2) | Y |  |  |
| 113 | VLR_TOT_DEV_TRIB_IBS_UF | NUMBER(17,2) | Y |  |  |
| 114 | VLR_TOT_IBS_UF | NUMBER(17,2) | Y |  |  |
| 115 | VLR_TOT_DIF_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 116 | VLR_TOT_DEV_TRIB_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 117 | VLR_TOT_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 118 | VLR_TOT_IBS | NUMBER(17,2) | Y |  |  |
| 119 | VLR_TOT_CRED_PRES_IBS | NUMBER(17,2) | Y |  |  |
| 120 | VLR_TOT_CRED_PRES_C_SUS_IBS | NUMBER(17,2) | Y |  |  |
| 121 | VLR_TOT_CRED_PRES_CBS | NUMBER(17,2) | Y |  |  |
| 122 | VLR_TOT_CRED_PRES_C_SUS_CBS | NUMBER(17,2) | Y |  |  |
| 123 | VLR_TOT_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 124 | VLR_TOT_DEV_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 125 | VLR_TOT_CBS | NUMBER(17,2) | Y |  |  |
| 126 | TOT_MONO_IBS | NUMBER(17,2) | Y |  |  |
| 127 | TOT_MONO_CBS | NUMBER(17,2) | Y |  |  |
| 128 | TOT_MONO_RET_IBS | NUMBER(17,2) | Y |  |  |
| 129 | TOT_MONO_RET_CBS | NUMBER(17,2) | Y |  |  |
| 130 | TOT_MONO_RET_ANT_IBS | NUMBER(17,2) | Y |  |  |
| 131 | TOT_MONO_RET_ANT_CBS | NUMBER(17,2) | Y |  |  |
| 132 | VLR_TOT_NF_IBS_CBS_IS | NUMBER(17,2) | Y |  |  |
| 133 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 134 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 135 | UNID_MED_TRIBUT_IS | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, USERNAME

**Indexes**:
- IX_TMP_X3007_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X3007_USER: (USERNAME)

---

## TMP_X3008_ITENS_MERC_RT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 16 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 17 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 18 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 19 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 20 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 21 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 22 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 23 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 24 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 25 | CST_IS | VARCHAR2(3) | Y |  |  |
| 26 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 27 | BC_IS | NUMBER(17,2) | Y |  |  |
| 28 | ALIQ_IS | NUMBER(7,4) | Y |  |  |
| 29 | ALIQ_ESPEC_UNID_MED_APR_IS | NUMBER(7,4) | Y |  |  |
| 30 | VLR_IS | NUMBER(17,2) | Y |  |  |
| 31 | QTD_TRIB_IS | NUMBER(11,4) | Y |  |  |
| 32 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 33 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 34 | BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 35 | VLR_MON_DOCREF_N_INC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 36 | ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 37 | VLR_IBS_UF | NUMBER(17,2) | Y |  |  |
| 38 | PERC_DIF_IBS_UF | NUMBER(7,4) | Y |  |  |
| 39 | VLR_DIF_IBS_UF | NUMBER(17,2) | Y |  |  |
| 40 | VLR_TRIB_DEV_IBS_UF | NUMBER(17,2) | Y |  |  |
| 41 | PERC_RED_ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 42 | ALIQ_EFET_IBS_UF | NUMBER(7,4) | Y |  |  |
| 43 | ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 44 | VLR_CBS | NUMBER(17,2) | Y |  |  |
| 45 | PERC_DIF_CBS | NUMBER(7,4) | Y |  |  |
| 46 | VLR_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 47 | VLR_BRUTO_CBS | NUMBER(17,2) | Y |  |  |
| 48 | VLR_TRIB_DEV_CBS | NUMBER(17,2) | Y |  |  |
| 49 | PERC_RED_ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 50 | ALIQ_EFET_CBS | NUMBER(7,4) | Y |  |  |
| 51 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 52 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 53 | ALIQ_TRIB_REG_IBS_UF | NUMBER(7,4) | Y |  |  |
| 54 | VLR_TRIB_REG_TRIB_IBS_UF | NUMBER(17,2) | Y |  |  |
| 55 | ALIQ_TRIB_REG_CBS | NUMBER(7,4) | Y |  |  |
| 56 | VLR_TRIB_REG_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 57 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 58 | PERC_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 59 | ALIQ_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 60 | VLR_CRED_PRES_IBS | NUMBER(17,2) | Y |  |  |
| 61 | VLR_CRED_PRES_COND_SUSP_IBS | NUMBER(17,2) | Y |  |  |
| 62 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 63 | PERC_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 64 | ALIQ_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 65 | VLR_CRED_PRES_CBS | NUMBER(17,2) | Y |  |  |
| 66 | VLR_CRED_PRES_COND_SUSP_CBS | NUMBER(17,2) | Y |  |  |
| 67 | QTD_TRIB_MONO_IBS_CBS | NUMBER(11,4) | Y |  |  |
| 68 | ALIQ_AD_REM_IBS | NUMBER(7,4) | Y |  |  |
| 69 | ALIQ_AD_REM_CBS | NUMBER(7,4) | Y |  |  |
| 70 | VLR_MONO_IBS | NUMBER(17,2) | Y |  |  |
| 71 | VLR_MONO_CBS | NUMBER(17,2) | Y |  |  |
| 72 | QTD_TRIB_RET_MONO_IBS_CBS | NUMBER(11,4) | Y |  |  |
| 73 | ALIQ_AD_REM_RET_IBS | NUMBER(7,4) | Y |  |  |
| 74 | VLR_MONO_RET_IBS | NUMBER(17,2) | Y |  |  |
| 75 | ALIQ_AD_REM_RET_CBS | NUMBER(7,4) | Y |  |  |
| 76 | VLR_MONO_RET_CBS | NUMBER(17,2) | Y |  |  |
| 77 | QTD_TRIB_RET_ANT_IBS_CBS | NUMBER(11,4) | Y |  |  |
| 78 | ALIQ_AD_REM_RET_ANT_IBS | NUMBER(7,4) | Y |  |  |
| 79 | VLR_RET_ANT_IBS | NUMBER(17,2) | Y |  |  |
| 80 | ALIQ_AD_REM_RET_ANT_CBS | NUMBER(7,4) | Y |  |  |
| 81 | VLR_RET_ANT_CBS | NUMBER(17,2) | Y |  |  |
| 82 | PERC_DIF_MONO_IBS | NUMBER(7,4) | Y |  |  |
| 83 | VLR_MONO_DIF_IBS | NUMBER(17,2) | Y |  |  |
| 84 | PERC_DIF_MONO_CBS | NUMBER(7,4) | Y |  |  |
| 85 | VLR_MONO_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 86 | ALIQ_IBS_UF_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 87 | VLR_IBS_UF_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 88 | ALIQ_IBS_MUN_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 89 | VLR_IBS_MUN_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 90 | ALIQ_CBS_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 91 | VLR_CBS_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 92 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 93 | NUM_ITEM_DOC_REFERENCIADO | NUMBER(3) | Y |  |  |
| 94 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 95 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 96 | UNID_MED_TRIBUT_IS | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, USERNAME

**Indexes**:
- IX_TMP_X3008_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X3008_USER: (USERNAME)

---

## TMP_X3009_ITENS_SERV_RT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | VARCHAR2(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 15 | NUM_ITEM | NUMBER(5) | N |  |  |
| 16 | COD_MUN_FT_GER_IBS_CBS | NUMBER(7) | Y |  |  |
| 17 | CST_IS | VARCHAR2(3) | Y |  |  |
| 18 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 19 | BC_IS | NUMBER(17,2) | Y |  |  |
| 20 | ALIQ_IS | NUMBER(7,4) | Y |  |  |
| 21 | ALIQ_ESPEC_UNID_MED_APR_IS | NUMBER(7,4) | Y |  |  |
| 22 | VLR_IS | NUMBER(17,2) | Y |  |  |
| 23 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 24 | QTD_TRIB_IS | NUMBER(15,4) | Y |  |  |
| 25 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 26 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 27 | BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_MON_DOCREF_N_INC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 29 | ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 30 | VLR_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 31 | PERC_DIF_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 32 | VLR_DIF_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BRUTO_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 34 | VLR_TRIB_DEV_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 35 | PERC_RED_ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 36 | ALIQ_EFET_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 37 | ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 38 | VLR_CBS | NUMBER(17,2) | Y |  |  |
| 39 | VLR_BRUTO_CBS | NUMBER(17,2) | Y |  |  |
| 40 | VLR_TRIB_DEV_CBS | NUMBER(17,2) | Y |  |  |
| 41 | PERC_RED_ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 42 | ALIQ_EFET_CBS | NUMBER(7,4) | Y |  |  |
| 43 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 44 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 45 | ALIQ_TRIB_REG_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 46 | VLR_TRIB_REG_TRIB_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 47 | ALIQ_TRIB_REG_CBS | NUMBER(7,4) | Y |  |  |
| 48 | VLR_TRIB_REG_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 49 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 50 | PERC_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 51 | ALIQ_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 52 | VLR_CRED_PRES_IBS | NUMBER(17,2) | Y |  |  |
| 53 | VLR_CRED_PRES_COND_SUSP_IBS | NUMBER(17,2) | Y |  |  |
| 54 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 55 | PERC_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 56 | ALIQ_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 57 | VLR_CRED_PRES_CBS | NUMBER(17,2) | Y |  |  |
| 58 | VLR_CRED_PRES_COND_SUSP_CBS | NUMBER(17,2) | Y |  |  |
| 59 | ALIQ_IBS_UF_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 60 | VLR_IBS_UF_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 61 | ALIQ_IBS_MUN_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 62 | VLR_IBS_MUN_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 63 | ALIQ_CBS_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 64 | VLR_CBS_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 65 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 66 | NUM_ITEM_DOC_REFERENCIADO | NUMBER(3) | Y |  |  |
| 67 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 68 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 69 | UNID_MED_TRIBUT_IS | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_SERVICO, NUM_ITEM, USERNAME

**Indexes**:
- IX_TMP_X3009_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X3009_USER: (USERNAME)

---

## TMP_X308_INFO_COMP_ST_IT_M_DEV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | VARCHAR2(50) | N |  |  |
| 2 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 3 | USERNAME | VARCHAR2(50) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | DATA_FISCAL | DATE | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | N |  |  |
| 8 | NORM_DEV | CHAR(1) | N |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | IND_PRODUTO | CHAR(1) | N |  |  |
| 16 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 17 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 18 | NUM_ITEM | NUMBER(5) | N |  |  |
| 19 | ESPECIE_DOCTO_DEV | VARCHAR2(1) | Y |  |  |
| 20 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 21 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 22 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 23 | COD_DOCTO_REF | VARCHAR2(5) | Y |  |  |
| 24 | DATA_FISCAL_REF | DATE | Y |  |  |
| 25 | IND_FIS_JUR_REF | CHAR(1) | Y |  |  |
| 26 | COD_FIS_JUR_REF | VARCHAR2(14) | Y |  |  |
| 27 | COD_MODELO_REF | VARCHAR2(2) | Y |  |  |
| 28 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 29 | NUM_COO_REF | VARCHAR2(9) | Y |  |  |
| 30 | DATA_EMISSAO_REF | DATE | Y |  |  |
| 31 | NUM_EQUIP_REF | NUMBER(9) | Y |  |  |
| 32 | NUM_CUPOM_REF | VARCHAR2(6) | Y |  |  |
| 33 | NUM_ITEM_DOC_REF | NUMBER(5) | Y |  |  |
| 34 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 35 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 36 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 37 | IDENT_DOCTO_REF | NUMBER(12) | Y |  |  |
| 38 | IDENT_FIS_JUR_REF | NUMBER(12) | Y |  |  |
| 39 | IDENT_MODELO_REF | NUMBER(12) | Y |  |  |
| 40 | IDENT_CAIXA_ECF | NUMBER(12) | Y |  |  |
| 41 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 42 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 43 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 44 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 45 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 46 | VLR_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 47 | VLR_UNIT_BC_ICMSS_ENT | NUMBER(19,6) | Y |  |  |
| 48 | VLR_UNIT_ICMSS_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 49 | VLR_UNIT_FCP_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 50 | VLR_UNIT_ICMS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 51 | VLR_UNIT_ICMSS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 52 | VLR_UNIT_FCP_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 53 | VLR_UNIT_ICMS_OPER_SAI | NUMBER(19,6) | Y |  |  |
| 54 | VLR_UNIT_ICMSS_REST_SAI | NUMBER(19,6) | Y |  |  |
| 55 | VLR_UNIT_FCP_REST_SAI | NUMBER(19,6) | Y |  |  |
| 56 | VLR_UNIT_ICMSS_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 57 | VLR_UNIT_FCP_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 58 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 59 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: ID

**Indexes**:
- UK_TMP_X308_INF_COMP_ST_IT_M_D (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, ESPECIE_DOCTO_DEV, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, COD_DOCTO_REF, DATA_FISCAL_REF, IND_FIS_JUR_REF, COD_FIS_JUR_REF, COD_MODELO_REF, COD_CAIXA_ECF, NUM_COO_REF, DATA_EMISSAO_REF, NUM_EQUIP_REF, NUM_CUPOM_REF, NUM_ITEM_DOC_REF, USERNAME)

---

## TMP_X325_TRIB_ICMS_MONO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | PERC_B100 | NUMBER(7,4) | Y |  |  |
| 22 | PERC_GLP | NUMBER(7,4) | Y |  |  |
| 23 | PERC_GLGN_N | NUMBER(7,4) | Y |  |  |
| 24 | PERC_GLGN_I | NUMBER(7,4) | Y |  |  |
| 25 | IND_ORIGEM_COM | VARCHAR2(1) | Y |  |  |
| 26 | QTD_BC_MONO | NUMBER(17,6) | Y |  |  |
| 27 | ALIQ_AD_REM_ICMS | NUMBER(7,4) | Y |  |  |
| 28 | VLR_ICMS_MONO | NUMBER(17,2) | Y |  |  |
| 29 | QTD_BC_MONO_RETEN | NUMBER(17,6) | Y |  |  |
| 30 | ALIQ_AD_REM_ICMS_RETEN | NUMBER(7,4) | Y |  |  |
| 31 | VLR_ICMS_MONO_RETEN | NUMBER(17,2) | Y |  |  |
| 32 | PERC_RED_AD_REM | NUMBER(7,4) | Y |  |  |
| 33 | DSC_RED_AD_REM | VARCHAR2(1) | Y |  |  |
| 34 | VLR_ICMS_MONO_OP | NUMBER(17,2) | Y |  |  |
| 35 | PERC_DIF | NUMBER(7,4) | Y |  |  |
| 36 | VLR_ICMS_MONO_DIF | NUMBER(17,2) | Y |  |  |
| 37 | QTD_BC_MONO_RET | NUMBER(17,6) | Y |  |  |
| 38 | ALIQ_AD_REM_ICMS_RET | NUMBER(7,4) | Y |  |  |
| 39 | VLR_ICMS_MONO_RET | NUMBER(17,2) | Y |  |  |
| 40 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 41 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 42 | IND_CRED_ICMS | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, USERNAME

**Indexes**:
- IX_TMP_X325_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X325_USER: (USERNAME)

---

## TMP_X326_ORIG_ICMS_MONO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | IND_ORIG | VARCHAR2(1) | N |  |  |
| 22 | COD_UF_ORIG | VARCHAR2(2) | N |  |  |
| 23 | PERC_UF_ORIG | NUMBER(7,4) | Y |  |  |
| 24 | IDENT_UF_ORIG | NUMBER(12) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, IND_ORIG, COD_UF_ORIG, USERNAME

**Indexes**:
- IX_TMP_X326_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X326_USER: (USERNAME)

---

## TMP_X331_PROG_FIDEL_FAT_NFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | VARCHAR2(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 15 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 16 | QTD_PTS_PROG_FIDEL | VARCHAR2(20) | Y |  |  |
| 17 | DAT_AFER_PROG_FIDEL | DATE | Y |  |  |
| 18 | QTD_REGAT_PROG_FIDEL | VARCHAR2(20) | Y |  |  |
| 19 | DAT_REGAT_PROG_FIDEL | DATE | Y |  |  |
| 20 | ANO_MES_REFERENCIA_FAT | VARCHAR2(6) | Y |  |  |
| 21 | DAT_VENCTO | DATE | Y |  |  |
| 22 | COD_BARRAS | VARCHAR2(48) | Y |  |  |
| 23 | COD_DEBITO_AUTO | VARCHAR2(20) | Y |  |  |
| 24 | COD_BANCO_AUTO | VARCHAR2(5) | Y |  |  |
| 25 | COD_AGENCIA_AUTO | VARCHAR2(10) | Y |  |  |
| 26 | COD_QRCODE_PIX | VARCHAR2(2000) | Y |  |  |
| 27 | DATA_CONSUMO_INI | DATE | Y |  |  |
| 28 | DATA_CONSUMO_FIM | DATE | Y |  |  |
| 29 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 30 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, USERNAME

**Indexes**:
- IX_TMP_X331_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X331_USER: (USERNAME)

---

## TMP_X332_PROC_RESSARC_NFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | VLR_UNIT_PROC | NUMBER(21,8) | Y |  |  |
| 22 | QTD_FAT_PROC | NUMBER(15,4) | Y |  |  |
| 23 | VLR_ITEM_PROC | NUMBER(21,8) | Y |  |  |
| 24 | VLR_DESC_PROC | NUMBER(17,2) | Y |  |  |
| 25 | VLR_OUT_DESP_PROC | NUMBER(17,2) | Y |  |  |
| 26 | IND_DEV_PROC | VARCHAR2(1) | Y |  |  |
| 27 | VLR_BC_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ALIQ_ICMS_PROC | NUMBER(7,4) | Y |  |  |
| 29 | VLR_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 30 | VLR_PIS_PROC | NUMBER(17,2) | Y |  |  |
| 31 | VLR_COFINS_PROC | NUMBER(17,2) | Y |  |  |
| 32 | IND_TP_RESSARC | VARCHAR2(2) | Y |  |  |
| 33 | DATA_REF_RESSARC | DATE | Y |  |  |
| 34 | NUM_PROC_RESSARC | VARCHAR2(60) | Y |  |  |
| 35 | NUM_PROT_RESSARC | VARCHAR2(60) | Y |  |  |
| 36 | DSC_OBS_RESSARC | VARCHAR2(100) | Y |  |  |
| 37 | DSC_ADIC_RESSARC | VARCHAR2(500) | Y |  |  |
| 38 | VLR_FCP_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 39 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 40 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, USERNAME

**Indexes**:
- IX_TMP_X332_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X332_USER: (USERNAME)

---

## TMP_X333_PART_UF_DEST_NFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | N |  |  |
| 18 | UF_DESTINO | VARCHAR2(2) | N |  |  |
| 19 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 20 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 21 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 22 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 23 | VLR_BASE_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 24 | PERC_FCP_DEST | NUMBER(5,2) | Y |  |  |
| 25 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 26 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 27 | VLR_TRIB_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ICMS_UF_EMIT | NUMBER(17,2) | Y |  |  |
| 29 | COD_BENEF_FISCAL_DEST | VARCHAR2(10) | Y |  |  |
| 30 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, UF_DESTINO, USERNAME

**Indexes**:
- IX_TMP_X333_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X333_USER: (USERNAME)

---

## TMP_X334_FUND_TRIB_FED_NFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | VLR_PIS_RETIDO | NUMBER(23,8) | Y |  |  |
| 22 | VLR_COFINS_RETIDO | NUMBER(23,8) | Y |  |  |
| 23 | VLR_CSLL_RETIDO | NUMBER(23,8) | Y |  |  |
| 24 | VLR_BC_IRRF | NUMBER(23,8) | Y |  |  |
| 25 | VLR_IRRF_RETIDO | NUMBER(23,8) | Y |  |  |
| 26 | VLR_BC_FUST | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ALIQ_FUST | NUMBER(7,4) | Y |  |  |
| 28 | VLR_FUST | NUMBER(17,2) | Y |  |  |
| 29 | VLR_BC_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 30 | VLR_ALIQ_FUNTTEL | NUMBER(7,4) | Y |  |  |
| 31 | VLR_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 32 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, USERNAME

**Indexes**:
- IX_TMP_X334_ID: (ID_DOCTO_FISCAL)
- IX_TMP_X334_USER: (USERNAME)

---

## TMP_X44_ITENS_CHASSI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | N |  |  |
| 18 | NUM_CHASSI | VARCHAR2(17) | N |  |  |
| 19 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 20 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 21 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 22 | COD_COR | VARCHAR2(4) | Y |  |  |
| 23 | DSC_COR | VARCHAR2(40) | Y |  |  |
| 24 | DSC_POTENCIA | VARCHAR2(4) | Y |  |  |
| 25 | DSC_POTENCIA_CM3 | VARCHAR2(4) | Y |  |  |
| 26 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 27 | PESO_BRUTO | NUMBER(14,3) | Y |  |  |
| 28 | SERIE_VEIC | VARCHAR2(9) | Y |  |  |
| 29 | DSC_TP_COMBUSTIVEL | VARCHAR2(8) | Y |  |  |
| 30 | NUM_MOTOR | VARCHAR2(21) | Y |  |  |
| 31 | DSC_CMKG | VARCHAR2(9) | Y |  |  |
| 32 | DSC_DISTANCIA_EIXO | VARCHAR2(4) | Y |  |  |
| 33 | NUM_RENAVAM | NUMBER(14) | Y |  |  |
| 34 | NUM_MARCA_MODELO | NUMBER(6) | Y |  |  |
| 35 | NUM_ANO_MODELO | NUMBER(4) | Y |  |  |
| 36 | NUM_ANO_FABRIC | NUMBER(4) | Y |  |  |
| 37 | IND_TP_PINTURA | CHAR(1) | Y |  |  |
| 38 | NUM_TP_VEIC | NUMBER(2) | Y |  |  |
| 39 | NUM_ESPECIE_VEIC | NUMBER(1) | Y |  |  |
| 40 | IND_CONDICAO_VIN | CHAR(1) | Y |  |  |
| 41 | IND_CONDICAO_VEIC | CHAR(1) | Y |  |  |
| 42 | PLACA_VEICULO | VARCHAR2(7) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_PRODUTO, COD_PRODUTO, COD_UND_PADRAO, NUM_ITEM, NUM_CHASSI, USERNAME

---

## TMP_X502_VEIC_COMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_ESCR_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_FIS_JUR_TRANSP | CHAR(1) | N |  |  |
| 15 | COD_FIS_JUR_TRANSP | VARCHAR2(14) | N |  |  |
| 16 | PLACA_VEICULO | VARCHAR2(17) | N |  |  |
| 17 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 18 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 19 | IDENT_TRANSP | NUMBER(12) | Y |  |  |
| 20 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 21 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 22 | NUM_VOLUME | VARCHAR2(50) | Y |  |  |
| 23 | PESO_BRUTO | NUMBER(14,3) | Y |  |  |
| 24 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_FIS_JUR_TRANSP, COD_FIS_JUR_TRANSP, PLACA_VEICULO, USERNAME

---

## TMP_X50_TRANSP_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_ESCR_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IND_FIS_JUR_TRANSP | CHAR(1) | N |  |  |
| 15 | COD_FIS_JUR_TRANSP | VARCHAR2(14) | N |  |  |
| 16 | IDENT_VIA_TRANSP | NUMBER(12) | Y |  |  |
| 17 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 18 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 19 | IDENT_TRANSP | NUMBER(12) | Y |  |  |
| 20 | COD_VIA_TRANSP | VARCHAR2(5) | Y |  |  |
| 21 | QTD_VOLUMES | NUMBER(17,6) | Y |  |  |
| 22 | IDENT_VOLUME | NUMBER(12) | Y |  |  |
| 23 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 24 | PESO_BRUTO | NUMBER(14,3) | Y |  |  |
| 25 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 26 | DESPESA_FRETE | NUMBER(17,2) | Y |  |  |
| 27 | MODALIDADE_FRETE | CHAR(1) | Y |  |  |
| 28 | DESPESA_SEGURO | NUMBER(17,2) | Y |  |  |
| 29 | NUM_CFRETE_DESPAC | VARCHAR2(12) | Y |  |  |
| 30 | PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 31 | PRE_NUM_CONHEC | VARCHAR2(12) | Y |  |  |
| 32 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 33 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 34 | CNH_MOTORISTA | NUMBER(11) | Y |  |  |
| 35 | NOME_MOTORISTA | VARCHAR2(40) | Y |  |  |
| 36 | PLACA_CARRETA | VARCHAR2(7) | Y |  |  |
| 37 | DAT_ENT_VEIC | DATE | Y |  |  |
| 38 | HORA_ENT_VEIC | VARCHAR2(4) | Y |  |  |
| 39 | HORA_SAI_VEIC | VARCHAR2(4) | Y |  |  |
| 40 | ORDEM_CARREG | NUMBER(6) | Y |  |  |
| 41 | IDENT_UF_CAM | NUMBER(12) | Y |  |  |
| 42 | COD_UF_CAM | VARCHAR2(2) | Y |  |  |
| 43 | CIDADE_CAM | VARCHAR2(18) | Y |  |  |
| 44 | NUM_VIAGEM | NUMBER(15) | Y |  |  |
| 45 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 46 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 47 | IDENT_UF_VEIC | NUMBER(12) | Y |  |  |
| 48 | COD_UF_VEIC | VARCHAR2(2) | Y |  |  |
| 49 | PLACA_REBOQUE | VARCHAR2(17) | Y |  |  |
| 50 | IDENT_UF_REBOQ | NUMBER(12) | Y |  |  |
| 51 | COD_UF_REBOQ | VARCHAR2(2) | Y |  |  |
| 52 | MARCA_VOLUME | VARCHAR2(50) | Y |  |  |
| 53 | NUM_VOLUME | VARCHAR2(50) | Y |  |  |
| 54 | IDENT_FIS_JUR_CONSIG | NUMBER(12) | Y |  |  |
| 55 | IND_FIS_JUR_CONSIG | CHAR(1) | Y |  |  |
| 56 | COD_FIS_JUR_CONSIG | VARCHAR2(14) | Y |  |  |
| 57 | IDENT_FIS_JUR_REDESP | NUMBER(12) | Y |  |  |
| 58 | IND_FIS_JUR_REDESP | CHAR(1) | Y |  |  |
| 59 | COD_FIS_JUR_REDESP | VARCHAR2(14) | Y |  |  |
| 60 | IDENT_VEIC_TRANSP | NUMBER(12) | Y |  |  |
| 61 | COD_VEIC_TRANSP | VARCHAR2(6) | Y |  |  |
| 62 | IND_TP_NAVEGACAO | CHAR(1) | Y |  |  |
| 63 | IND_TARIFA_AEREA | CHAR(1) | Y |  |  |
| 64 | IND_NATUREZA_FRETE | CHAR(1) | Y |  |  |
| 65 | REGISTRO_OPERADOR | VARCHAR2(30) | Y |  |  |
| 66 | VLR_FRETE_PV | NUMBER(17,2) | Y |  |  |
| 67 | VLR_FRETE_LIQ | NUMBER(17,2) | Y |  |  |
| 68 | VLR_FRETE_BRUTO | NUMBER(17,2) | Y |  |  |
| 69 | VLR_FRETE_MM | NUMBER(17,2) | Y |  |  |
| 70 | VLR_SEC_CAT | NUMBER(17,2) | Y |  |  |
| 71 | VLR_DESPACHO | NUMBER(17,2) | Y |  |  |
| 72 | VLR_PEDAGIO | NUMBER(17,2) | Y |  |  |
| 73 | VLR_DESPESA_PORT | NUMBER(17,2) | Y |  |  |
| 74 | VLR_DESPESA_CARGA | NUMBER(17,2) | Y |  |  |
| 75 | VLR_PESO_TAXADO | NUMBER(17,2) | Y |  |  |
| 76 | VLR_TAXA_TERRESTRE | NUMBER(17,2) | Y |  |  |
| 77 | VLR_TAXA_REDESPACHO | NUMBER(17,2) | Y |  |  |
| 78 | VLR_TAXA_ADV | NUMBER(17,2) | Y |  |  |
| 79 | VLR_GRIS | NUMBER(17,2) | Y |  |  |
| 80 | VLR_TARIFA | NUMBER(17,2) | Y |  |  |
| 81 | COD_LINHA_TRANSP | VARCHAR2(10) | Y |  |  |
| 82 | DSC_LINHA_TRANSP | VARCHAR2(50) | Y |  |  |
| 83 | POLTRONA | VARCHAR2(10) | Y |  |  |
| 84 | AGENTE | VARCHAR2(30) | Y |  |  |
| 85 | IDENT_FIS_JUR_COLETA | NUMBER(12) | Y |  |  |
| 86 | IND_FIS_JUR_COLETA | CHAR(1) | Y |  |  |
| 87 | COD_FIS_JUR_COLETA | VARCHAR2(14) | Y |  |  |
| 88 | IDENT_FIS_JUR_ENTREGA | NUMBER(12) | Y |  |  |
| 89 | IND_FIS_JUR_ENTREGA | CHAR(1) | Y |  |  |
| 90 | COD_FIS_JUR_ENTREGA | VARCHAR2(14) | Y |  |  |
| 91 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 92 | MATRICULA | VARCHAR2(16) | Y |  |  |
| 93 | COD_AUTORIZ_SEFAZ | VARCHAR2(21) | Y |  |  |
| 94 | NUM_PASSE_FISCAL | VARCHAR2(20) | Y |  |  |
| 95 | TEMPERATURA | NUMBER(5,2) | Y |  |  |
| 96 | CPF_MOTORISTA | VARCHAR2(11) | Y |  |  |
| 97 | MODAL_FRETE_REDESP | CHAR(1) | Y |  |  |
| 98 | IND_VAGAO_BALSA | CHAR(1) | Y |  |  |
| 99 | COD_VAGAO_BALSA | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_FIS_JUR_TRANSP, COD_FIS_JUR_TRANSP, USERNAME

---

## TMP_X51_ITENS_FRETE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_ESCR_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_DOCTO_TRANSP | VARCHAR2(5) | N |  |  |
| 15 | NUM_DOCFIS_TRANSP | VARCHAR2(12) | N |  |  |
| 16 | SER_DOCFIS_TRANSP | VARCHAR2(3) | N |  |  |
| 17 | S_SER_DOCFIS_TRANS | VARCHAR2(2) | N |  |  |
| 18 | DATA_EMIS_TRANSP | DATE | N |  |  |
| 19 | CGC_CPF_REMET | VARCHAR2(14) | N |  |  |
| 20 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 21 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 22 | IDENT_DOCTO_TRANSP | NUMBER(12) | Y |  |  |
| 23 | VLR_TOT_DOCFIS | NUMBER(17,2) | Y |  |  |
| 24 | INSC_UF_REMET | VARCHAR2(14) | Y |  |  |
| 25 | RAZAO_REMET | VARCHAR2(70) | Y |  |  |
| 26 | MUNICIPIO_REMET | VARCHAR2(30) | Y |  |  |
| 27 | CEP_REMET | NUMBER(8) | Y |  |  |
| 28 | IDENT_ESTADO_REMET | NUMBER(12) | Y |  |  |
| 29 | COD_ESTADO_REMET | VARCHAR2(2) | Y |  |  |
| 30 | CPF_CGC_DEST | VARCHAR2(14) | Y |  |  |
| 31 | INSC_ESTADUAL_DEST | VARCHAR2(14) | Y |  |  |
| 32 | RAZAO_DEST | VARCHAR2(70) | Y |  |  |
| 33 | MUNICIPIO_DEST | VARCHAR2(30) | Y |  |  |
| 34 | CEP_DEST | NUMBER(8) | Y |  |  |
| 35 | IDENT_ESTADO_DEST | NUMBER(12) | Y |  |  |
| 36 | COD_ESTADO_DEST | VARCHAR2(2) | Y |  |  |
| 37 | DOCFIS_SIM_NAO | CHAR(1) | Y |  |  |
| 38 | IDENT_VIA_TRANSP | NUMBER(12) | Y |  |  |
| 39 | COD_VIA_TRANSP | VARCHAR2(5) | Y |  |  |
| 40 | QTD_VOLUME | NUMBER(17,6) | Y |  |  |
| 41 | IDENT_VOLUME | NUMBER(12) | Y |  |  |
| 42 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 43 | PESO_BRUTO | NUMBER(14,3) | Y |  |  |
| 44 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 45 | DESPESA_FRETE | NUMBER(17,2) | Y |  |  |
| 46 | MODALIDADE_FRETE | CHAR(1) | Y |  |  |
| 47 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 48 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 49 | OBSERVACAO_FRETE | VARCHAR2(45) | Y |  |  |
| 50 | IDENT_TRANSP | NUMBER(12) | Y |  |  |
| 51 | IND_FIS_JUR_TRANSP | CHAR(1) | Y |  |  |
| 52 | COD_FIS_JUR_TRANSP | VARCHAR2(14) | Y |  |  |
| 53 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 54 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 55 | COD_MUNIC_COLETA | NUMBER(5) | Y |  |  |
| 56 | COD_MUNIC_DEST | NUMBER(5) | Y |  |  |
| 57 | DISTANCIA_EM_KM | NUMBER(6) | Y |  |  |
| 58 | QTD_MERCADORIA | NUMBER(17,6) | Y |  |  |
| 59 | IND_FORMA_CALC | CHAR(1) | Y |  |  |
| 60 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 61 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 62 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 63 | NAT_VOLUME | VARCHAR2(30) | Y |  |  |
| 64 | VOLUME | VARCHAR2(30) | Y |  |  |
| 65 | MARCA_VOLUME | VARCHAR2(50) | Y |  |  |
| 66 | NUM_VOLUME | NUMBER(30) | Y |  |  |
| 67 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  |  |
| 68 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 69 | NUM_DESPACHO | VARCHAR2(12) | Y |  |  |
| 70 | CPF_CNPJ_COLETA | VARCHAR2(14) | Y |  |  |
| 71 | INSCR_EST_COLETA | VARCHAR2(14) | Y |  |  |
| 72 | CPF_CNPJ_ENTREGA | VARCHAR2(14) | Y |  |  |
| 73 | INSCR_EST_ENTREGA | VARCHAR2(14) | Y |  |  |
| 74 | COD_MUNIC_REMET | NUMBER(5) | Y |  |  |
| 75 | COD_MUNIC_ENTREGA | NUMBER(5) | Y |  |  |
| 76 | IDENT_ESTADO_COLETA | NUMBER(12) | Y |  |  |
| 77 | COD_ESTADO_COLETA | VARCHAR2(2) | Y |  |  |
| 78 | IDENT_ESTADO_ENTREGA | NUMBER(12) | Y |  |  |
| 79 | COD_ESTADO_ENTREGA | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_DOCTO_TRANSP, NUM_DOCFIS_TRANSP, SER_DOCFIS_TRANSP, S_SER_DOCFIS_TRANS, DATA_EMIS_TRANSP, CGC_CPF_REMET, USERNAME

---

## TMP_X701_VOO_PASSAG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IDENT_VOO | VARCHAR2(10) | N |  |  |
| 15 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 16 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 17 | IDENT_UF_DOCFIS_EMIT | NUMBER(12) | Y |  |  |
| 18 | COD_UF_DOCFIS_EMIT | VARCHAR2(2) | Y |  |  |
| 19 | QTD_PASSAG_VOO | NUMBER(4) | Y |  |  |
| 20 | IDENT_CONEXAO | VARCHAR2(10) | Y |  |  |
| 21 | IND_CLASSE | CHAR(1) | Y |  |  |
| 22 | NUM_POLTRONA | VARCHAR2(4) | Y |  |  |
| 23 | CPF_PARTICIPANTE | VARCHAR2(11) | Y |  |  |
| 24 | NOME_PARTICIPANTE | VARCHAR2(100) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_VOO, USERNAME

---

## TMP_X702_DESEMB_PASSAG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DOCTO_FISCAL | VARCHAR2(150) | N |  |  |
| 2 | USERNAME | VARCHAR2(50) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | IDENT_VOO | VARCHAR2(10) | N |  |  |
| 15 | COD_MUNICIPIO_ORIG | NUMBER(5) | N |  |  |
| 16 | COD_MUNICIPIO_DEST | NUMBER(5) | N |  |  |
| 17 | COD_UF_ORIG | VARCHAR2(2) | N |  |  |
| 18 | COD_UF_DEST | VARCHAR2(2) | N |  |  |
| 19 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 20 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 21 | IDENT_UF_ORIG | NUMBER(12) | Y |  |  |
| 22 | IDENT_UF_DEST | NUMBER(12) | Y |  |  |
| 23 | QTD_PASSAG_DEST | NUMBER(4) | Y |  |  |
| 24 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 25 | VLR_TAXA | NUMBER(17,2) | Y |  |  |
| 26 | VLR_DESC | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 30 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 31 | COD_IATA_ORIG | VARCHAR2(3) | Y |  |  |
| 32 | COD_IATA_DEST | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_VOO, COD_MUNICIPIO_ORIG, COD_MUNICIPIO_DEST, COD_UF_ORIG, COD_UF_DEST, USERNAME

---

