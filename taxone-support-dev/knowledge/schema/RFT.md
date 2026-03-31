# Módulo: RFT (RFT) - 13 tabelas

## RFT_MOVESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 7 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 8 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 9 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 10 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 11 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 12 | CUSTO_UNIT | NUMBER(18,6) | Y |  |  |
| 13 | CUSTO_ITEM | NUMBER(17,2) | Y |  |  |
| 14 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 15 | RAZAO_SOCIAL_EMPRESA | VARCHAR2(70) | Y |  |  |
| 16 | RAZAO_SOCIAL_ESTAB | VARCHAR2(100) | Y |  |  |
| 17 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 18 | CGC | VARCHAR2(14) | Y |  |  |
| 19 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 20 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 21 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 22 | PROC_ID | NUMBER | Y |  |  |
| 23 | NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 24 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 25 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 26 | NUM_ITEM | NUMBER(5) | Y |  |  |

**Indexes**:
- IX_RFT_MOVESTOQUE: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO)

---

## RFT_MOV_AUX_AF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | VLR_SLD_INI | NUMBER(17,2) | Y |  |  |
| 6 | VLR_AQUISICOES | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DEPRECIACAO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_COR_MONET | NUMBER(17,2) | Y |  |  |
| 9 | VLR_RESIDUAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRF_ADICAO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRF_BAIXA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ALTERACAO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SLD_FIN | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_CONTA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_RFT_MOV_AUX_AF_CTA: (IDENT_CONTA)

---

## RFT_MOV_AUX_PATR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 6 | VLR_AQUISICAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DEPRECIACAO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CORR_MONET | NUMBER(17,2) | Y |  |  |
| 9 | VLR_RESIDUAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRANSF_ADIC | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRANSF_BAIXA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ALTERACAO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SALDO_FIM | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | IND_TP_CONTA | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_CONTA

**Indexes**:
- IX_RFT_M_A_PATR_02: (COD_EMPRESA, COD_ESTAB, DAT_APURAC)

---

## RFT_MOV_DET_PROD

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
| 11 | NUM_ITEM | NUMBER(5) | N |  |  |
| 12 | IND_PRODUTO | CHAR(1) | N |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 14 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 15 | DATA_EMISSAO | DATE | Y |  |  |
| 16 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 17 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 18 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 19 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 20 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 21 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 22 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 23 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 24 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 25 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 26 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 27 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 28 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 29 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 31 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_BASE_RED | NUMBER(17,2) | Y |  |  |
| 33 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 34 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 35 | VLR_SUBST_ICMS | NUMBER(17,2) | Y |  |  |
| 36 | VLR_BASE_ISENTAS | NUMBER(17,2) | Y |  |  |
| 37 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 38 | DIF_ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 39 | VLR_DIFAL | NUMBER(17,2) | Y |  |  |
| 40 | DSC_OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 41 | USUARIO | VARCHAR2(40) | Y |  |  |
| 42 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 43 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 44 | NUM_SEQ | NUMBER(12) | Y |  |  |
| 45 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 46 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 47 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 48 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 49 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 50 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 51 | VLR_ISENTA_IPI | NUMBER(17,2) | Y |  |  |
| 52 | VLR_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |
| 53 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 54 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 55 | DSC_UND_PADRAO | VARCHAR2(50) | Y |  |  |
| 56 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 57 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 58 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 59 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 60 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 61 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 62 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 63 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 64 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 65 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 66 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 67 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 68 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 69 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 70 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 71 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 72 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 73 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 74 | COD_TRIB_IPI | VARCHAR2(2) | Y | 'N' |  |
| 75 | IND_CRED_ESTIMULO | CHAR(1) | Y | 'N' |  |
| 76 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 77 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 78 | VLR_ALIQ_SUB_ICMS | NUMBER(7,4) | Y |  |  |
| 79 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 80 | VLR_FECP_ICMS | NUMBER(17,2) | Y |  |  |
| 81 | VLR_FECP_DIFALIQ | NUMBER(17,2) | Y |  |  |
| 82 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 83 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  |  |
| 84 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 85 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 86 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 87 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 88 | DESC_MUNICIPIO | VARCHAR2(50) | Y |  |  |
| 89 | COD_BENEFICIO | VARCHAR2(10) | Y |  |  |
| 90 | INSC_ESTAD_SUBSTIT | VARCHAR2(14) | Y |  |  |
| 91 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 92 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 93 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM, IND_PRODUTO, COD_PRODUTO

**Indexes**:
- IX_RFT_MOV_DET_PROD: (DATA_FISCAL, NUM_PROCESSO, NUM_SEQ)

---

## RFT_MOV_DET_PROD_PARM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | NOME | VARCHAR2(20) | N |  |  |
| 3 | CODIGO | VARCHAR2(20) | N |  |  |

**PK**: PROC_ID, NOME, CODIGO

---

## RFT_MOV_RES_AF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_TIPO_MOVPATR | NUMBER(12) | N |  |  |
| 5 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 6 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_TIPO_MOVPATR, IDENT_CONTA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_TIPO_MOVPATR → X2022_TIPO_MOVPATR(IDENT_TIPO_MOVPATR)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_RFT_MOV_RES_AF_CTA: (IDENT_CONTA)

---

## RFT_PARFOLSINT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 2 | IND_FOL | VARCHAR2(2) | N |  |  |
| 3 | IND_NAT_VERBA | VARCHAR2(2) | Y |  |  |

**PK**: IDENT_VERBA, IND_FOL

---

## RFT_PAR_CONSOLID

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONSOLID | VARCHAR2(2) | N |  |  |
| 4 | GRUPO_TIPO_MOVPATR | VARCHAR2(9) | N |  |  |
| 5 | COD_TIPO_MOVPATR | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONSOLID, GRUPO_TIPO_MOVPATR, COD_TIPO_MOVPATR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_CONSOLID → RFT_TP_CONSOLID(COD_EMPRESA, COD_ESTAB, COD_CONSOLID)

---

## RFT_PISCOFINS_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | IND_INCID_PIS | CHAR(1) | Y |  |  |
| 5 | IND_INCID_COFINS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RFT_PISCOFINS_EXT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | IND_INCID_PIS | CHAR(1) | Y |  |  |
| 7 | IND_INCID_COFINS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RFT_TOT_ECF_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DT_FISCAL | DATE | N |  |  |
| 4 | VLR_TOT_ECF | NUMBER(17,2) | Y |  |  |
| 5 | VLR_TOT_NF | NUMBER(17,2) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DT_FISCAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RFT_TP_CONSOLID

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONSOLID | VARCHAR2(2) | N |  |  |
| 4 | DSC_1 | VARCHAR2(15) | Y |  |  |
| 5 | DSC_2 | VARCHAR2(15) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONSOLID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RFT_TP_MOVTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_TIPO_MOVPATR | NUMBER(12) | N |  |  |
| 5 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 6 | VLR_MOVTO | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_TIPO_MOVPATR, IDENT_CONTA

---

