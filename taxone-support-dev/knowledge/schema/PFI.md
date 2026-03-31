# Módulo: PFI (PFI) - 95 tabelas

## PFI_AGEN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | AGEN_ID | NUMBER(20) | N |  |  |
| 2 | PROC_ID | NUMBER(20) | N |  |  |
| 3 | AGEN_DT_INI | DATE | Y |  |  |
| 4 | AGEN_DT_FIM | DATE | Y |  |  |
| 5 | AGEN_EMPS_COD | VARCHAR2(9) | Y |  |  |
| 6 | AGEN_FILI_COD | VARCHAR2(9) | Y |  |  |
| 7 | AGEN_INI | DATE | Y |  |  |
| 8 | AGEN_PERI | CHAR(1) | Y |  |  |
| 9 | AGEN_STAT | CHAR(1) | Y |  |  |
| 10 | AGEN_NOM_USU | VARCHAR2(40) | Y |  |  |
| 11 | AGEN_COD_SERVIDOR | VARCHAR2(255) | Y |  |  |
| 12 | AGEN_IND_CODITEM | CHAR(1) | Y |  |  |
| 13 | AGEN_IND_NUMDOCOFI | CHAR(1) | Y |  |  |
| 14 | AGEN_IND_CADG | CHAR(1) | Y |  |  |
| 15 | AGEN_IND_CODITEM_SAICS | CHAR(1) | Y |  |  |
| 16 | AGEN_IND_ATIVO_SAICS | CHAR(1) | Y |  |  |

**PK**: AGEN_ID

**FKs**:
- PROC_ID → PFI_PROC(PROC_ID)

---

## PFI_AGEP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | AGEN_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 3 | FILI_COD | VARCHAR2(9) | N |  |  |

**PK**: AGEN_ID, EMPS_COD, FILI_COD

**FKs**:
- AGEN_ID → PFI_AGEN(AGEN_ID)

---

## PFI_ALLC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ALLC_ID | NUMBER(9) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 3 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 4 | ALLC_MES_REF | NUMBER(4) | Y |  |  |
| 5 | ALLC_ANO_REF | NUMBER(4) | Y |  |  |
| 6 | ALLC_NUM_STATUS | NUMBER(2) | Y |  |  |

**PK**: ALLC_ID

---

## PFI_AUDI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | AUDI_ID | NUMBER(20) | N |  |  |
| 2 | AUDI_NOME | VARCHAR2(50) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | AUDI_DAT_INI | DATE | Y |  |  |
| 6 | AUDI_DAT_FIM | DATE | Y |  |  |
| 7 | AUDI_PRG | VARCHAR2(10) | Y |  |  |
| 8 | AUDI_ETP | VARCHAR2(7) | Y |  |  |
| 9 | AUDI_ARQ | BLOB | Y |  |  |
| 10 | AUDI_TIPO | VARCHAR2(5) | Y |  |  |
| 11 | AUDI_CONCLUIDA | CHAR(1) | Y |  |  |
| 12 | AUDI_STATUS | NUMBER | Y |  |  |

**PK**: AUDI_ID

---

## PFI_AUDI_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | CFOP_COD | VARCHAR2(6) | N |  |  |
| 4 | CHECAR | CHAR(1) | Y |  |  |
| 5 | IND_ES | CHAR(1) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, CFOP_COD

---

## PFI_CATG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CATG_COD | CHAR(2) | N |  |  |
| 2 | CATG_SUB | CHAR(2) | Y |  |  |
| 3 | CATG_DSC | VARCHAR2(20) | Y |  |  |

**PK**: CATG_COD

---

## PFI_CAUP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CAUP_DAT_ATUA | DATE | N |  |  |
| 2 | CADG_COD_CAT83 | VARCHAR2(16) | Y |  |  |
| 3 | CADG_COD_CGCCPF | VARCHAR2(16) | N |  |  |
| 4 | CADG_COD_INSEST | VARCHAR2(14) | N |  |  |

**PK**: CAUP_DAT_ATUA, CADG_COD_CGCCPF, CADG_COD_INSEST

---

## PFI_CFOP_CAT207

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CFOP_COD | VARCHAR2(6) | N |  |  |
| 2 | CHECAR | CHAR(1) | N | 1 |  |
| 3 | IND_E | CHAR(1) | N |  |  |
| 4 | IND_S | CHAR(1) | N |  |  |
| 5 | IND_P | CHAR(1) | N |  |  |

**PK**: CFOP_COD

---

## PFI_CICF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | CICF_DAT_ATUA | DATE | N |  |  |
| 4 | CICF_TIPO_ITEM | NUMBER(2) | N |  |  |
| 5 | CICF_IND_CF | CHAR(1) | N |  |  |

**PK**: EMPS_COD, FILI_COD, CICF_DAT_ATUA, CICF_TIPO_ITEM

---

## PFI_CODL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CODL_ID | NUMBER(20) | N |  |  |
| 2 | CODL_COD_OBRIG | VARCHAR2(10) | Y |  |  |
| 3 | CODL_COD | VARCHAR2(10) | Y |  |  |
| 4 | CODL_DSC | VARCHAR2(255) | Y |  |  |
| 5 | CODL_IND_NEGA | CHAR(1) | Y |  |  |
| 6 | CODL_IND_CALC | CHAR(1) | Y |  |  |
| 7 | CODL_IND_EXPA | CHAR(1) | Y |  |  |
| 8 | CODL_IND_ESTO | CHAR(1) | Y |  |  |

**PK**: CODL_ID

---

## PFI_COMA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MATE_COD | VARCHAR2(60) | N |  |  |
| 4 | CMAT_COD | CHAR(1) | N |  |  |
| 5 | COMA_DAT_ATUA | DATE | N |  |  |
| 6 | COMA_IND_CF | CHAR(1) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, MATE_COD, CMAT_COD, COMA_DAT_ATUA

---

## PFI_CRAE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CRAE_ID | NUMBER(20) | N |  |  |
| 2 | REAE_ID | NUMBER(20) | Y |  |  |
| 3 | CRAE_NUM_ORDEM | NUMBER(4) | Y |  |  |
| 4 | CRAE_NUM_TAMANHO | NUMBER(4) | Y |  |  |
| 5 | CRAE_QTD_DECIMAL | NUMBER(10) | Y |  |  |
| 6 | CRAE_TIP_CONTEUDO | NUMBER(2) | Y |  |  |
| 7 | CRAE_TIP_CAMPO | NUMBER(2) | Y |  |  |
| 8 | CRAE_IND_PRECISAO | CHAR(1) | Y |  |  |
| 9 | CRAE_NOM_CONTEUDO | VARCHAR2(80) | Y |  |  |
| 10 | CRAE_NOM_CAMPO | VARCHAR2(300) | Y |  |  |
| 11 | CRAE_USR | VARCHAR2(40) | Y |  |  |
| 12 | CRAE_DAT_ATUA | DATE | Y |  |  |

**PK**: CRAE_ID

**FKs**:
- REAE_ID → PFI_REAE(REAE_ID)

---

## PFI_CROU

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | CROU_MES_PROC | NUMBER(2) | N |  |  |
| 4 | CROU_ANO_PROC | NUMBER(4) | N |  |  |
| 5 | CROU_VAL_CRED_RAT | NUMBER(17,2) | N |  |  |
| 6 | CROU_VAL_MES | NUMBER | N | 0 |  |

**PK**: EMPS_COD, FILI_COD, CROU_MES_PROC, CROU_ANO_PROC

---

## PFI_DEPR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | PROD_DAT_ATUA | DATE | N |  |  |
| 4 | PROD_NUM_PROC | VARCHAR2(40) | N |  |  |
| 5 | PROD_COD | VARCHAR2(60) | N |  |  |
| 6 | ITEM_COD | VARCHAR2(60) | N |  |  |
| 7 | QTD_INS_UNI | NUMBER | Y |  |  |
| 8 | VAL_PER_GAN | NUMBER | Y |  |  |

**PK**: EMPS_COD, FILI_COD, PROD_DAT_ATUA, PROD_NUM_PROC, PROD_COD, ITEM_COD

**FKs**:
- EMPS_COD, FILI_COD, PROD_DAT_ATUA, PROD_NUM_PROC, PROD_COD → PFI_ESPR(EMPS_COD, FILI_COD, PROD_DAT_ATUA, PROD_NUM_PROC, PROD_COD)

---

## PFI_DEVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DEVO_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | DEVO_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 6 | DEVO_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 7 | DEVO_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 8 | DEVO_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 9 | DEVO_COD_CADG | VARCHAR2(16) | Y |  |  |
| 10 | DEVO_COD_CATG | CHAR(2) | Y |  |  |
| 11 | DEVO_DAT_EMISS | DATE | Y |  |  |
| 12 | DEVO_NUM_DOC_ORI | VARCHAR2(15) | Y |  |  |
| 13 | DEVO_COD_SER_ORI | VARCHAR2(5) | Y |  |  |
| 14 | DEVO_COD_CAD_ORI | VARCHAR2(16) | Y |  |  |
| 15 | DEVO_COD_CAT_ORI | CHAR(2) | Y |  |  |
| 16 | DEVO_DAT_EMI_ORI | DATE | Y |  |  |
| 17 | DEVO_TIP_DOC_ORI | NUMBER(3) | Y |  |  |
| 18 | DEVO_VAL_BAS_ORI | NUMBER | Y |  |  |
| 19 | DEVO_VAL_TOT_ORI | NUMBER | Y |  |  |
| 20 | DEVO_VAL_ICM_ORI | NUMBER | Y |  |  |
| 21 | DEVO_VAL_ICM_ACU | NUMBER | Y |  |  |
| 22 | DEVO_QTD_ORI | NUMBER | Y |  |  |

**PK**: DEVO_ID

**Indexes**:
- IX_PFI_DEVO1: (EXEC_ID, EMPS_COD, FILI_COD, DEVO_COD_CADG, DEVO_COD_CATG, DEVO_NUM_DOCTO, DEVO_COD_SERIE, DEVO_NUM_ITEM)

---

## PFI_DSFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSFE_ID | NUMBER(20) | N |  |  |
| 2 | PSFE_ID | NUMBER(20) | Y |  |  |
| 3 | UNFE_SIG | CHAR(2) | Y |  |  |
| 4 | DSFE_COD_ELEG | CHAR(4) | Y |  |  |
| 5 | DSFE_USR | VARCHAR2(40) | Y |  |  |
| 6 | DSFE_DAT_ATUA | DATE | Y |  |  |
| 7 | DSFE_ALIQ_ICMS | NUMBER | Y |  |  |
| 8 | DSFE_ESTA_COD | CHAR(1) | Y |  |  |
| 9 | DSFE_ESTB_COD | CHAR(2) | Y |  |  |

**PK**: DSFE_ID

**FKs**:
- PSFE_ID → PFI_PSFE(PSFE_ID)

---

## PFI_DSFN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSFN_ID | NUMBER(20) | N |  |  |
| 2 | PSFN_ID | NUMBER(20) | Y |  |  |
| 3 | FICH_ID | NUMBER(20) | Y |  |  |
| 4 | CODL_ID | NUMBER(20) | Y |  |  |
| 5 | DSFN_COD_ELEG | NUMBER(4) | Y |  |  |
| 6 | DSFN_IND_LANCTO | CHAR(1) | Y |  |  |
| 7 | DSFN_USR | VARCHAR2(40) | Y |  |  |
| 8 | DSFN_DAT_ATUA | DATE | Y |  |  |
| 9 | UNFE_SIG | CHAR(2) | Y |  |  |

**PK**: DSFN_ID

**FKs**:
- CODL_ID → PFI_CODL(CODL_ID)
- FICH_ID → PFI_FICH(FICH_ID)
- PSFN_ID → PFI_PSFN(PSFN_ID)

---

## PFI_DSFN_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSFN_ID | NUMBER(20) | N |  |  |
| 2 | PSFN_ID | NUMBER(20) | N |  |  |
| 3 | UNFE_SIG | CHAR(2) | Y |  |  |
| 4 | DSFN_COD_ELEG | NUMBER(20) | Y |  |  |
| 5 | DSFN_USR | VARCHAR2(40) | N |  |  |
| 6 | DSFN_DAT_ATUA | DATE | N |  |  |

**PK**: DSFN_ID

**FKs**:
- PSFN_ID → PFI_PSFN_S(PSFN_ID)

---

## PFI_EAUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | AUDI_ID | NUMBER(20) | N |  |  |
| 2 | EAUD_ITEM | VARCHAR2(7) | N |  |  |
| 3 | EAUD_CONCLUIDO | CHAR(1) | Y |  |  |

**PK**: AUDI_ID, EAUD_ITEM

**FKs**:
- AUDI_ID → PFI_AUDI(AUDI_ID)

---

## PFI_EPRC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MPCG_NOM_PROC | VARCHAR2(60) | N |  |  |
| 2 | MPCG_NUM_PROC | VARCHAR2(20) | N |  |  |
| 3 | MPCG_NOM_USU | VARCHAR2(40) | N |  |  |
| 4 | EPRC_ARQ | BLOB | Y |  |  |

**PK**: MPCG_NOM_PROC, MPCG_NUM_PROC, MPCG_NOM_USU

**FKs**:
- MPCG_NOM_PROC, MPCG_NUM_PROC, MPCG_NOM_USU → PFI_MPCG(MPCG_NOM_PROC, MPCG_NUM_PROC, MPCG_NOM_USU)

---

## PFI_ESPR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | PROD_DAT_ATUA | DATE | N |  |  |
| 4 | PROD_NUM_PROC | VARCHAR2(40) | N |  |  |
| 5 | PROD_COD | VARCHAR2(60) | N |  |  |

**PK**: EMPS_COD, FILI_COD, PROD_DAT_ATUA, PROD_NUM_PROC, PROD_COD

---

## PFI_ESTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ESTO_ID | NUMBER(9) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 3 | FILI_COD | VARCHAR2(9) | N |  |  |
| 4 | ESTO_MES_REF | NUMBER(2) | N |  |  |
| 5 | ESTO_ANO_REF | NUMBER(4) | N |  |  |
| 6 | ESTO_NUM_STATUS | NUMBER(2) | N |  |  |

**PK**: ESTO_ID

---

## PFI_EXCI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | CICF_DAT_ATUA | DATE | N |  |  |
| 4 | CICF_TIPO_ITEM | NUMBER(2) | N |  |  |
| 5 | MATE_COD | VARCHAR2(60) | N |  |  |
| 6 | CMAT_COD | CHAR(1) | N |  |  |

**PK**: EMPS_COD, FILI_COD, CICF_DAT_ATUA, CICF_TIPO_ITEM, MATE_COD, CMAT_COD

**FKs**:
- EMPS_COD, FILI_COD, CICF_DAT_ATUA, CICF_TIPO_ITEM → PFI_CICF(EMPS_COD, FILI_COD, CICF_DAT_ATUA, CICF_TIPO_ITEM)

---

## PFI_EXCO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EXCO_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 3 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 4 | EXCO_MES_REF | NUMBER(2) | Y |  |  |
| 5 | EXCO_ANO_REF | NUMBER(4) | Y |  |  |
| 6 | EXCO_IND_GERA | CHAR(1) | Y |  |  |
| 7 | EXCO_IND_ARQ | CHAR(1) | Y |  |  |
| 8 | EXCO_QTD_PROC | NUMBER(2) | Y |  |  |
| 9 | EXCO_QTD_PROCEXE | NUMBER(2) | Y |  |  |
| 10 | EXCO_NUM_STATUS | NUMBER(2) | Y |  |  |
| 11 | EXCO_DAT_INI_EXE | DATE | Y |  |  |
| 12 | EXCO_DAT_FIM_EXE | DATE | Y |  |  |
| 13 | EXCO_COD_LAYOUT | CHAR(2) | Y |  |  |
| 14 | EXCO_COD_FINAL | CHAR(2) | Y |  |  |
| 15 | EXCO_USR | VARCHAR2(40) | Y |  |  |
| 16 | EXCO_DAT_ATUA | DATE | Y |  |  |
| 17 | EXCO_ARQ | BLOB | Y |  |  |
| 18 | EXCO_DAT_AGEN | DATE | Y |  |  |
| 19 | EXCO_COD_SERVIDOR | VARCHAR2(255) | Y |  |  |
| 20 | EXCO_MSG_ERRO | VARCHAR2(300) | Y |  |  |

**PK**: EXCO_ID

---

## PFI_EXEC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EXEC_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 3 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 4 | EXEC_MES_REF | NUMBER(2) | Y |  |  |
| 5 | EXEC_ANO_REF | NUMBER(4) | Y |  |  |
| 6 | EXEC_IND_EXTR | CHAR(1) | Y |  |  |
| 7 | EXEC_IND_CALC | CHAR(1) | Y |  |  |
| 8 | EXEC_IND_DEMO | CHAR(1) | Y |  |  |
| 9 | EXEC_IND_ARQ | CHAR(1) | Y |  |  |
| 10 | EXEC_IND_PARAR | CHAR(1) | Y |  |  |
| 11 | EXEC_QTD_PROC | NUMBER(2) | Y |  |  |
| 12 | EXEC_QTD_PROCEXE | NUMBER(2) | Y |  |  |
| 13 | EXEC_NUM_STATUS | NUMBER(2) | Y |  |  |
| 14 | EXEC_DAT_INI_EXE | DATE | Y |  |  |
| 15 | EXEC_DAT_FIM_EXE | DATE | Y |  |  |
| 16 | EXEC_COD_LAYOUT | CHAR(2) | Y |  |  |
| 17 | EXEC_COD_FINAL | CHAR(2) | Y |  |  |
| 18 | EXEC_USR | VARCHAR2(40) | Y |  |  |
| 19 | EXEC_DAT_ATUA | DATE | Y |  |  |
| 20 | EXEC_ARQ | BLOB | Y |  |  |
| 21 | EXEC_DAT_AGEN | DATE | Y |  |  |
| 22 | EXEC_COD_SERVIDOR | VARCHAR2(255) | Y |  |  |
| 23 | EXEC_TIP_SITUACAO | CHAR(1) | Y |  |  |
| 24 | EXEC_IND_REG_0200 | CHAR(1) | Y |  |  |
| 25 | EXEC_COD_NIVEL | CHAR(1) | Y |  |  |
| 26 | EXEC_MSG_ERRO | VARCHAR2(300) | Y |  |  |

**PK**: EXEC_ID

---

## PFI_EXEC_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EXEC_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 3 | FILI_COD | VARCHAR2(9) | N |  |  |
| 4 | EXEC_MES_REF | NUMBER(2) | N |  |  |
| 5 | EXEC_ANO_REF | NUMBER(4) | N |  |  |
| 6 | EXEC_IND_EXTR | CHAR(1) | Y |  |  |
| 7 | EXEC_IND_CALC | CHAR(1) | Y |  |  |
| 8 | EXEC_IND_DEMO | CHAR(1) | Y |  |  |
| 9 | EXEC_IND_ARQ | CHAR(1) | Y |  |  |
| 10 | EXEC_IND_PARAR | CHAR(1) | Y |  |  |
| 11 | EXEC_QTD_PROC | NUMBER(2) | Y |  |  |
| 12 | EXEC_QTD_PROCEXE | NUMBER(2) | Y |  |  |
| 13 | EXEC_NUM_STATUS | NUMBER(2) | Y |  |  |
| 14 | EXEC_DAT_INI_EXE | DATE | N |  |  |
| 15 | EXEC_DAT_FIM_EXE | DATE | Y |  |  |
| 16 | EXEC_COD_LAYOUT | CHAR(2) | Y |  |  |
| 17 | EXEC_COD_FINAL | CHAR(2) | Y |  |  |
| 18 | EXEC_USR | VARCHAR2(40) | N |  |  |
| 19 | EXEC_DAT_ATUA | DATE | Y |  |  |
| 20 | EXEC_DAT_AGEN | DATE | Y |  |  |
| 21 | EXEC_COD_SERVIDOR | VARCHAR2(255) | Y |  |  |
| 22 | EXEC_TIP_SITUACAO | CHAR(1) | Y |  |  |
| 23 | EXEC_IND_REG_0200 | CHAR(1) | Y |  |  |
| 24 | EXEC_COD_NIVEL | CHAR(1) | Y |  |  |
| 25 | EXEC_MSG_ERRO | VARCHAR2(300) | Y |  |  |
| 26 | EXEC_ARQ | BLOB | Y |  |  |

**PK**: EXEC_ID

---

## PFI_EXPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EXPO_ID | NUMBER(20) | N |  |  |
| 2 | EXCO_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | EXPO_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | EXPO_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | EXPO_DAT_MOVTO | DATE | Y |  |  |
| 8 | EXPO_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | EXPO_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | EXPO_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | EXPO_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | EXPO_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | EXPO_NUM_DDEDSE | VARCHAR2(20) | Y |  |  |
| 14 | EXPO_COD_COMPR | VARCHAR2(3) | Y |  |  |
| 15 | EXPO_VAL_TOTAL | NUMBER | Y |  |  |
| 16 | EXPO_VAL_CUSTO | NUMBER | Y |  |  |
| 17 | EXPO_VAL_BASE | NUMBER | Y |  |  |
| 18 | EXPO_QTD | NUMBER | Y |  |  |
| 19 | EXPO_VAL_ICMS | NUMBER | Y |  |  |
| 20 | EXPO_PER_CRE | NUMBER | Y |  |  |
| 21 | EXPO_VAL_CRE | NUMBER | Y |  |  |
| 22 | EXPO_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | EXPO_VAL_CRE_COM | NUMBER | Y |  |  |
| 24 | EXPO_VAL_ICM_COM | NUMBER | Y |  |  |
| 25 | EXPO_VAL_CRE_ACU | NUMBER | Y |  |  |
| 26 | EXPO_DAT_EXPORT | DATE | Y |  |  |
| 27 | EXPO_DAT_AVERB | DATE | Y |  |  |
| 28 | EXPO_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 29 | EXPO_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 30 | EXPO_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 31 | EXPO_NUM_DI_DSI | VARCHAR2(12) | Y |  |  |
| 32 | EXPO_DAT_EMIS | DATE | Y |  |  |
| 33 | EXPO_NUM_DOC_EXP | VARCHAR2(15) | Y |  |  |
| 34 | EXPO_COD_SER_EXP | VARCHAR2(5) | Y |  |  |
| 35 | EXPO_NUM_DECLAR | VARCHAR2(15) | Y |  |  |
| 36 | EXPO_IND_VERIF | CHAR(1) | Y |  |  |
| 37 | EXPO_IND_ARQUIVO | CHAR(1) | Y |  |  |

**PK**: EXPO_ID

**FKs**:
- EXCO_ID → PFI_EXCO(EXCO_ID)

---

## PFI_FC1A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC1A_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC1A_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC1A_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC1A_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC1A_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC1A_COD_CFOP | NUMBER(4) | Y |  |  |
| 15 | FC1A_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 16 | FC1A_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 17 | FC1A_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 18 | FC1A_NUM_DI_DSI | VARCHAR2(12) | Y |  |  |
| 19 | FC1A_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 20 | FC1A_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 21 | FC1A_COD_FICHA | CHAR(2) | Y |  |  |
| 22 | FC1A_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 23 | FC1A_VAL_BASE | NUMBER | Y |  |  |
| 24 | FC1A_QTD_ENT | NUMBER | Y |  |  |
| 25 | FC1A_VAL_CUS_ENT | NUMBER | Y |  |  |
| 26 | FC1A_VAL_ICM_ENT | NUMBER | Y |  |  |
| 27 | FC1A_VAL_IPI_ENT | NUMBER | Y |  |  |
| 28 | FC1A_VAL_OUT_ENT | NUMBER | Y |  |  |
| 29 | FC1A_QTD_SAI | NUMBER | Y |  |  |
| 30 | FC1A_VAL_CUS_SAI | NUMBER | Y |  |  |
| 31 | FC1A_VAL_ICM_SAI | NUMBER | Y |  |  |
| 32 | FC1A_QTD_SLD | NUMBER | Y |  |  |
| 33 | FC1A_VAL_CUS_UNI | NUMBER | Y |  |  |
| 34 | FC1A_VAL_CUS_SLD | NUMBER | Y |  |  |
| 35 | FC1A_VAL_ICM_UNI | NUMBER | Y |  |  |
| 36 | FC1A_VAL_ICM_SLD | NUMBER | Y |  |  |
| 37 | FC1A_OBS | VARCHAR2(255) | Y |  |  |
| 38 | ETAPA | NUMBER(2) | Y |  |  |
| 39 | FC1A_CATG_COD | VARCHAR2(5) | Y |  |  |
| 40 | FC1A_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC1A_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC1A1: (EMPS_COD, FILI_COD, FC1A_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC1A2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC1A3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD, FC1A_DAT_MOVTO)
- IX_PFI_FC1A4: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC1B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC1B_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC1B_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC1B_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC1B_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC1B_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC1B_COD_CFOP | NUMBER(4) | Y |  |  |
| 15 | FC1B_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 16 | FC1B_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 17 | FC1B_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 18 | FC1B_NUM_DI_DSI | VARCHAR2(12) | Y |  |  |
| 19 | FC1B_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 20 | FC1B_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 21 | FC1B_COD_FICHA | CHAR(2) | Y |  |  |
| 22 | FC1B_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 23 | FC1B_VAL_BASE | NUMBER | Y |  |  |
| 24 | FC1B_VAL_CUS_ENT | NUMBER | Y |  |  |
| 25 | FC1B_VAL_ICM_ENT | NUMBER | Y |  |  |
| 26 | FC1B_VAL_IPI_ENT | NUMBER | Y |  |  |
| 27 | FC1B_VAL_OUT_ENT | NUMBER | Y |  |  |
| 28 | FC1B_VAL_CUS_SAI | NUMBER | Y |  |  |
| 29 | FC1B_VAL_ICM_SAI | NUMBER | Y |  |  |
| 30 | FC1B_VAL_CUS_SLD | NUMBER | Y |  |  |
| 31 | FC1B_VAL_ICM_SLD | NUMBER | Y |  |  |
| 32 | FC1B_OBS | VARCHAR2(255) | Y |  |  |
| 33 | ETAPA | NUMBER(2) | Y |  |  |
| 34 | FC1B_CATG_COD | VARCHAR2(5) | Y |  |  |
| 35 | FC1B_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC1B_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC1B1: (EMPS_COD, FILI_COD, FC1B_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC1B2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC1B3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC1C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC1C_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 7 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 8 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 9 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 10 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 11 | FC1C_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 12 | FC1C_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 13 | FC1C_DAT_MOVTO | DATE | Y |  |  |
| 14 | FC1C_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 15 | FC1C_COD_CFOP | NUMBER(4) | Y |  |  |
| 16 | FC1C_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 17 | FC1C_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 18 | FC1C_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 19 | FC1C_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 20 | FC1C_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 21 | FC1C_COD_FICHA | CHAR(2) | Y |  |  |
| 22 | FC1C_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 23 | FC1C_VAL_BASE | NUMBER | Y |  |  |
| 24 | FC1C_QTD_ENT | NUMBER | Y |  |  |
| 25 | FC1C_VAL_CUS_ENT | NUMBER | Y |  |  |
| 26 | FC1C_VAL_ICM_ENT | NUMBER | Y |  |  |
| 27 | FC1C_VAL_OUT_ENT | NUMBER | Y |  |  |
| 28 | FC1C_QTD_SAI | NUMBER | Y |  |  |
| 29 | FC1C_VAL_CUS_SAI | NUMBER | Y |  |  |
| 30 | FC1C_VAL_ICM_SAI | NUMBER | Y |  |  |
| 31 | FC1C_QTD_SLD | NUMBER | Y |  |  |
| 32 | FC1C_VAL_CUS_UNI | NUMBER | Y |  |  |
| 33 | FC1C_VAL_CUS_SLD | NUMBER | Y |  |  |
| 34 | FC1C_VAL_ICM_UNI | NUMBER | Y |  |  |
| 35 | FC1C_VAL_ICM_SLD | NUMBER | Y |  |  |
| 36 | FC1C_OBS | VARCHAR2(255) | Y |  |  |
| 37 | ETAPA | NUMBER(2) | Y |  |  |
| 38 | FC1C_CATG_COD | VARCHAR2(5) | Y |  |  |
| 39 | FC1C_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC1C_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC1C1: (EMPS_COD, FILI_COD, FC1C_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC1C2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC1C3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC1D

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC1D_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 7 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 8 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 9 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 10 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 11 | FC1D_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 12 | FC1D_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 13 | FC1D_DAT_MOVTO | DATE | Y |  |  |
| 14 | FC1D_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 15 | FC1D_COD_CFOP | NUMBER(4) | Y |  |  |
| 16 | FC1D_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 17 | FC1D_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 18 | FC1D_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 19 | FC1D_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 20 | FC1D_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 21 | FC1D_VAL_BASE | NUMBER | Y |  |  |
| 22 | FC1D_VAL_CUS_ENT | NUMBER | Y |  |  |
| 23 | FC1D_VAL_OUT_ENT | NUMBER | Y |  |  |
| 24 | FC1D_VAL_ICM_ENT | NUMBER | Y |  |  |
| 25 | FC1D_OBS | VARCHAR2(255) | Y |  |  |
| 26 | ETAPA | NUMBER(2) | Y |  |  |
| 27 | FC1D_CATG_COD | VARCHAR2(5) | Y |  |  |
| 28 | FC1D_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC1D_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC1D1: (EMPS_COD, FILI_COD, FC1D_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC1D2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC1D3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC1E

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC1E_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 7 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 8 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 9 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 10 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 11 | FC1E_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 12 | FC1E_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 13 | FC1E_DAT_MOVTO | DATE | Y |  |  |
| 14 | FC1E_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 15 | FC1E_COD_CFOP | NUMBER(4) | Y |  |  |
| 16 | FC1E_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 17 | FC1E_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 18 | FC1E_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 19 | FC1E_COD_REM | VARCHAR2(18) | Y |  |  |
| 20 | FC1E_COD_DEST | VARCHAR2(18) | Y |  |  |
| 21 | FC1E_COD_UF_ORI | VARCHAR2(2) | Y |  |  |
| 22 | FC1E_COD_UF_DES | VARCHAR2(2) | Y |  |  |
| 23 | FC1E_COD_TOMADOR | VARCHAR2(18) | Y |  |  |
| 24 | FC1E_ALI | NUMBER | Y |  |  |
| 25 | FC1E_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 26 | FC1E_VAL_BASE | NUMBER | Y |  |  |
| 27 | FC1E_VAL_CUS_ENT | NUMBER | Y |  |  |
| 28 | FC1E_VAL_ICM_ENT | NUMBER | Y |  |  |
| 29 | FC1E_VAL_CUS_SAI | NUMBER | Y |  |  |
| 30 | FC1E_VAL_ICM_SAI | NUMBER | Y |  |  |
| 31 | FC1E_OBS | VARCHAR2(255) | Y |  |  |
| 32 | ETAPA | NUMBER(2) | Y |  |  |
| 33 | FC1E_CATG_COD | VARCHAR2(5) | Y |  |  |
| 34 | FC1E_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC1E_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC1E1: (EMPS_COD, FILI_COD, FC1E_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC1E2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC1E3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC2A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC2A_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC2A_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC2A_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC2A_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC2A_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC2A_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 15 | FC2A_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 16 | FC2A_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 17 | FC2A_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 18 | FC2A_COD_FICHA | CHAR(2) | Y |  |  |
| 19 | FC2A_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 20 | FC2A_QTD_ENT | NUMBER | Y |  |  |
| 21 | FC2A_VAL_CUS_ENT | NUMBER | Y |  |  |
| 22 | FC2A_VAL_ICM_ENT | NUMBER | Y |  |  |
| 23 | FC2A_QTD_SAI | NUMBER | Y |  |  |
| 24 | FC2A_VAL_CUS_UNI | NUMBER | Y |  |  |
| 25 | FC2A_VAL_CUS_SAI | NUMBER | Y |  |  |
| 26 | FC2A_VAL_ICM_UNI | NUMBER | Y |  |  |
| 27 | FC2A_VAL_ICM_SAI | NUMBER | Y |  |  |
| 28 | FC2A_VAL_CUS_SLD | NUMBER | Y |  |  |
| 29 | FC2A_VAL_ICM_SLD | NUMBER | Y |  |  |
| 30 | FC2A_NUM_LLC | NUMBER(3) | Y |  |  |
| 31 | FC2A_IND_RATEIO | CHAR(1) | Y |  |  |
| 32 | FC2A_NUM_ORD_FAB | VARCHAR2(40) | Y |  |  |
| 33 | FC2A_COD_NSTQ | VARCHAR2(5) | Y |  |  |
| 34 | FC2A_OBS | VARCHAR2(255) | Y |  |  |
| 35 | FC2A_QTD_INS_UNI | NUMBER | Y |  |  |
| 36 | ETAPA | NUMBER(2) | Y |  |  |
| 37 | FC2A_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC2A_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC2A1: (EMPS_COD, FILI_COD, FC2A_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC2A2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC2A3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD, FC2A_NUM_ORD_FAB, FC2A_NUM_LLC)
- IX_PFI_FC2A4: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD, FC2A_NUM_ORD_FAB)

---

## PFI_FC2B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC2B_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC2B_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC2B_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC2B_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC2B_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC2B_COD_CFOP | NUMBER(4) | Y |  |  |
| 15 | FC2B_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 16 | FC2B_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 17 | FC2B_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 18 | FC2B_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 19 | FC2B_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 20 | FC2B_COD_FICHA | CHAR(2) | Y |  |  |
| 21 | FC2B_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 22 | FC2B_VAL_BASE | NUMBER | Y |  |  |
| 23 | FC2B_QTD_ENT | NUMBER | Y |  |  |
| 24 | FC2B_VAL_CUS_ENT | NUMBER | Y |  |  |
| 25 | FC2B_VAL_ICM_ENT | NUMBER | Y |  |  |
| 26 | FC2B_QTD_SAI | NUMBER | Y |  |  |
| 27 | FC2B_VAL_CUS_UNI | NUMBER | Y |  |  |
| 28 | FC2B_VAL_CUS_SAI | NUMBER | Y |  |  |
| 29 | FC2B_VAL_ICM_UNI | NUMBER | Y |  |  |
| 30 | FC2B_VAL_ICM_SAI | NUMBER | Y |  |  |
| 31 | FC2B_VAL_CUS_SLD | NUMBER | Y |  |  |
| 32 | FC2B_VAL_ICM_SLD | NUMBER | Y |  |  |
| 33 | FC2B_OBS | VARCHAR2(255) | Y |  |  |
| 34 | FC2B_NUM_LLC | NUMBER(3) | Y |  |  |
| 35 | FC2B_NUM_PEDIDO | VARCHAR2(40) | Y |  |  |
| 36 | FC2B_QTD_INS_UNI | NUMBER | Y |  |  |
| 37 | ETAPA | NUMBER(2) | Y |  |  |
| 38 | FC2B_CATG_COD | VARCHAR2(5) | Y |  |  |
| 39 | FC2B_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC2B_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC2B1: (EMPS_COD, FILI_COD, FC2B_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC2B2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC2B3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC2C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC2C_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC2C_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC2C_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC2C_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC2C_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC2C_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 15 | FC2C_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 16 | FC2C_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 17 | FC2C_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 18 | FC2C_COD_FICHA | CHAR(2) | Y |  |  |
| 19 | FC2C_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 20 | FC2C_QTD_ENT | NUMBER | Y |  |  |
| 21 | FC2C_VAL_CUS_ENT | NUMBER | Y |  |  |
| 22 | FC2C_VAL_ICM_ENT | NUMBER | Y |  |  |
| 23 | FC2C_QTD_SAI | NUMBER | Y |  |  |
| 24 | FC2C_VAL_CUS_SAI | NUMBER | Y |  |  |
| 25 | FC2C_VAL_ICM_SAI | NUMBER | Y |  |  |
| 26 | FC2C_VAL_CUS_SLD | NUMBER | Y |  |  |
| 27 | FC2C_VAL_ICM_SLD | NUMBER | Y |  |  |
| 28 | FC2C_OBS | VARCHAR2(255) | Y |  |  |
| 29 | ETAPA | NUMBER(2) | Y |  |  |
| 30 | FC2C_NUM_ORD_FAB | VARCHAR2(40) | Y |  |  |
| 31 | FC2C_NUM_LLC | NUMBER(3) | Y |  |  |
| 32 | FC2C_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC2C_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC2C1: (EMPS_COD, FILI_COD, FC2C_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC2C2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC2C3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC2D

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC2D_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 7 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 8 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 9 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 10 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 11 | FC2D_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 12 | FC2D_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 13 | FC2D_DAT_MOVTO | DATE | Y |  |  |
| 14 | FC2D_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 15 | FC2D_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 16 | FC2D_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 17 | FC2D_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 18 | FC2D_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 19 | FC2D_COD_FICHA | CHAR(2) | Y |  |  |
| 20 | FC2D_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 21 | FC2D_QTD_ENT | NUMBER | Y |  |  |
| 22 | FC2D_VAL_CUS_ENT | NUMBER | Y |  |  |
| 23 | FC2D_VAL_ICM_ENT | NUMBER | Y |  |  |
| 24 | FC2D_OBS | VARCHAR2(255) | Y |  |  |
| 25 | ETAPA | NUMBER(2) | Y |  |  |
| 26 | FC2D_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC2D_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC2D1: (EMPS_COD, FILI_COD, FC2D_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC2D2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC2D3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC2E

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC2E_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC2E_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC2E_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC2E_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC2E_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC2E_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 15 | FC2E_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 16 | FC2E_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 17 | FC2E_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 18 | FC2E_COD_FICHA | CHAR(2) | Y |  |  |
| 19 | FC2E_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 20 | FC2E_QTD_ENT | NUMBER | Y |  |  |
| 21 | FC2E_COD_UNID | VARCHAR2(6) | Y |  |  |
| 22 | FC2E_VAL_CUS_ENT | NUMBER | Y |  |  |
| 23 | FC2E_VAL_ICM_ENT | NUMBER | Y |  |  |
| 24 | FC2E_VAL_CUS_SAI | NUMBER | Y |  |  |
| 25 | FC2E_VAL_ICM_SAI | NUMBER | Y |  |  |
| 26 | FC2E_IND_FRETE | CHAR(1) | Y |  |  |
| 27 | FC2E_OBS | VARCHAR2(255) | Y |  |  |
| 28 | ETAPA | NUMBER(2) | Y |  |  |
| 29 | FC2E_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC2E_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC2E1: (EMPS_COD, FILI_COD, FC2E_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC2E2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC2E3: (EMPS_COD, FILI_COD, EXEC_ID, FC2E_IND_FRETE)
- IX_PFI_FC2E4: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC2F

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC2F_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC2F_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC2F_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC2F_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC2F_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC2F_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 15 | FC2F_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 16 | FC2F_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 17 | FC2F_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 18 | FC2F_COD_FICHA | CHAR(2) | Y |  |  |
| 19 | FC2F_COD_ITEM | VARCHAR2(65) | Y |  |  |
| 20 | FC2F_QTD_ENT | NUMBER | Y |  |  |
| 21 | FC2F_VAL_CUS_ENT | NUMBER | Y |  |  |
| 22 | FC2F_VAL_ICM_ENT | NUMBER | Y |  |  |
| 23 | FC2F_PER_SAI | NUMBER | Y |  |  |
| 24 | FC2F_QTD_SAI | NUMBER | Y |  |  |
| 25 | FC2F_VAL_CUS_SAI | NUMBER | Y |  |  |
| 26 | FC2F_VAL_ICM_SAI | NUMBER | Y |  |  |
| 27 | FC2F_OBS | VARCHAR2(255) | Y |  |  |
| 28 | ETAPA | NUMBER(2) | Y |  |  |
| 29 | FC2F_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC2F_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC2F1: (EMPS_COD, FILI_COD, FC2F_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC2F2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC2F3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC2G

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC2G_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC2G_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC2G_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC2G_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC2G_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC2G_COD_CFOP | NUMBER(4) | Y |  |  |
| 15 | FC2G_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 16 | FC2G_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 17 | FC2G_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 18 | FC2G_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 19 | FC2G_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 20 | FC2G_COD_FICHA | CHAR(2) | Y |  |  |
| 21 | FC2G_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 22 | FC2G_QTD_ENT | NUMBER | Y |  |  |
| 23 | FC2G_VAL_CUS_ENT | NUMBER | Y |  |  |
| 24 | FC2G_VAL_ICM_ENT | NUMBER | Y |  |  |
| 25 | FC2G_QTD_SAI | NUMBER | Y |  |  |
| 26 | FC2G_VAL_CUS_UNI | NUMBER | Y |  |  |
| 27 | FC2G_VAL_CUS_SAI | NUMBER | Y |  |  |
| 28 | FC2G_VAL_ICM_UNI | NUMBER | Y |  |  |
| 29 | FC2G_VAL_ICM_SAI | NUMBER | Y |  |  |
| 30 | FC2G_VAL_CUS_SLD | NUMBER | Y |  |  |
| 31 | FC2G_VAL_ICM_SLD | NUMBER | Y |  |  |
| 32 | FC2G_OBS | VARCHAR2(255) | Y |  |  |
| 33 | FC2G_NUM_LLC | NUMBER(3) | Y |  |  |
| 34 | FC2G_IND_RATEIO | CHAR(1) | Y |  |  |
| 35 | FC2G_COD_PROC | VARCHAR2(40) | Y |  |  |
| 36 | FC2G_COD_NSTQ | VARCHAR2(5) | Y |  |  |
| 37 | FC2G_QTD_INS_UNI | NUMBER | Y |  |  |
| 38 | FC2G_CATG_COD | VARCHAR2(5) | Y |  |  |
| 39 | FC2G_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 40 | ETAPA | NUMBER(2) | Y |  |  |
| 41 | FC2G_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC2G_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC2G1: (EMPS_COD, FILI_COD, FC2G_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC2G2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC2G3: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD, FC2G_COD_PROC, FC2G_NUM_LLC)
- IX_PFI_FC2G4: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD, FC2G_COD_PROC)

---

## PFI_FC3A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC3A_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC3A_COD_NSTQ | VARCHAR2(5) | Y |  |  |
| 11 | FC3A_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 12 | FC3A_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 13 | FC3A_DAT_MOVTO | DATE | Y |  |  |
| 14 | FC3A_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 15 | FC3A_COD_CFOP | NUMBER(4) | Y |  |  |
| 16 | FC3A_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 17 | FC3A_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 18 | FC3A_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 19 | FC3A_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 20 | FC3A_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 21 | FC3A_COD_FICHA | CHAR(2) | Y |  |  |
| 22 | FC3A_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 23 | FC3A_VAL_BASE | NUMBER | Y |  |  |
| 24 | FC3A_QTD_ENT | NUMBER | Y |  |  |
| 25 | FC3A_VAL_CUS_ENT | NUMBER | Y |  |  |
| 26 | FC3A_VAL_ICM_ENT | NUMBER | Y |  |  |
| 27 | FC3A_QTD_SAI | NUMBER | Y |  |  |
| 28 | FC3A_VAL_CUS_SAI | NUMBER | Y |  |  |
| 29 | FC3A_VAL_ICM_SAI | NUMBER | Y |  |  |
| 30 | FC3A_QTD_SLD | NUMBER | Y |  |  |
| 31 | FC3A_VAL_CUS_UNI | NUMBER | Y |  |  |
| 32 | FC3A_VAL_CUS_SLD | NUMBER | Y |  |  |
| 33 | FC3A_VAL_ICM_UNI | NUMBER | Y |  |  |
| 34 | FC3A_VAL_ICM_SLD | NUMBER | Y |  |  |
| 35 | FC3A_NUM_DOC_ORI | VARCHAR2(15) | Y |  |  |
| 36 | FC3A_COD_SER_ORI | VARCHAR2(5) | Y |  |  |
| 37 | FC3A_DAT_DOC_ORI | DATE | Y |  |  |
| 38 | FC3A_TIP_DOC_ORI | NUMBER(3) | Y |  |  |
| 39 | FC3A_OBS | VARCHAR2(255) | Y |  |  |
| 40 | ETAPA | NUMBER(2) | Y |  |  |
| 41 | FC3A_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 42 | FC3A_CATG_COD | VARCHAR2(5) | Y |  |  |
| 43 | FC3A_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC3A_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC3A1: (EMPS_COD, FILI_COD, FC3A_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC3A2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC3A3: (EMPS_COD, FILI_COD, EXEC_ID, FC3A_COD_LANCTO)
- IX_PFI_FC3A4: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC3B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC3B_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC3B_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC3B_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC3B_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC3B_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC3B_COD_CFOP | NUMBER(4) | Y |  |  |
| 15 | FC3B_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 16 | FC3B_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 17 | FC3B_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 18 | FC3B_NUM_DI_DSI | VARCHAR2(12) | Y |  |  |
| 19 | FC3B_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 20 | FC3B_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 21 | FC3B_COD_FICHA | CHAR(2) | Y |  |  |
| 22 | FC3B_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 23 | FC3B_VAL_BASE | NUMBER | Y |  |  |
| 24 | FC3B_QTD_ENT | NUMBER | Y |  |  |
| 25 | FC3B_VAL_CUS_ENT | NUMBER | Y |  |  |
| 26 | FC3B_VAL_ICM_ENT | NUMBER | Y |  |  |
| 27 | FC3B_VAL_IPI_ENT | NUMBER | Y |  |  |
| 28 | FC3B_VAL_OUT_ENT | NUMBER | Y |  |  |
| 29 | FC3B_QTD_SAI | NUMBER | Y |  |  |
| 30 | FC3B_VAL_CUS_SAI | NUMBER | Y |  |  |
| 31 | FC3B_VAL_ICM_SAI | NUMBER | Y |  |  |
| 32 | FC3B_QTD_SLD | NUMBER | Y |  |  |
| 33 | FC3B_VAL_CUS_UNI | NUMBER | Y |  |  |
| 34 | FC3B_VAL_CUS_SLD | NUMBER | Y |  |  |
| 35 | FC3B_VAL_ICM_UNI | NUMBER | Y |  |  |
| 36 | FC3B_VAL_ICM_SLD | NUMBER | Y |  |  |
| 37 | FC3B_NUM_DOC_ORI | VARCHAR2(15) | Y |  |  |
| 38 | FC3B_COD_SER_ORI | VARCHAR2(5) | Y |  |  |
| 39 | FC3B_DAT_DOC_ORI | DATE | Y |  |  |
| 40 | FC3B_TIP_DOC_ORI | NUMBER(3) | Y |  |  |
| 41 | FC3B_OBS | VARCHAR2(255) | Y |  |  |
| 42 | ETAPA | NUMBER(2) | Y |  |  |
| 43 | FC3B_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 44 | FC3B_CATG_COD | VARCHAR2(5) | Y |  |  |
| 45 | FC3B_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC3B_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC3B1: (EMPS_COD, FILI_COD, FC3B_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC3B2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC3B3: (EMPS_COD, FILI_COD, EXEC_ID, FC3B_COD_LANCTO)
- IX_PFI_FC3B4: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC3C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC3C_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 10 | FC3C_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 11 | FC3C_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 12 | FC3C_DAT_MOVTO | DATE | Y |  |  |
| 13 | FC3C_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 14 | FC3C_COD_CFOP | NUMBER(4) | Y |  |  |
| 15 | FC3C_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 16 | FC3C_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 17 | FC3C_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 18 | FC3C_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 19 | FC3C_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 20 | FC3C_VAL_BASE | NUMBER | Y |  |  |
| 21 | FC3C_QTD_ENT | NUMBER | Y |  |  |
| 22 | FC3C_VAL_CUS_ENT | NUMBER | Y |  |  |
| 23 | FC3C_VAL_ICM_ENT | NUMBER | Y |  |  |
| 24 | FC3C_QTD_SAI | NUMBER | Y |  |  |
| 25 | FC3C_VAL_CUS_SAI | NUMBER | Y |  |  |
| 26 | FC3C_VAL_ICM_SAI | NUMBER | Y |  |  |
| 27 | FC3C_QTD_SLD | NUMBER | Y |  |  |
| 28 | FC3C_VAL_CUS_SLD | NUMBER | Y |  |  |
| 29 | FC3C_VAL_ICM_SLD | NUMBER | Y |  |  |
| 30 | FC3C_NUM_DOC_ORI | VARCHAR2(15) | Y |  |  |
| 31 | FC3C_COD_SER_ORI | VARCHAR2(5) | Y |  |  |
| 32 | FC3C_DAT_DOC_ORI | DATE | Y |  |  |
| 33 | FC3C_TIP_DOC_ORI | NUMBER(3) | Y |  |  |
| 34 | FC3C_OBS | VARCHAR2(255) | Y |  |  |
| 35 | ETAPA | NUMBER(2) | Y |  |  |
| 36 | FC3C_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 37 | FC3C_CATG_COD | VARCHAR2(5) | Y |  |  |
| 38 | FC3C_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC3C_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC3C1: (EMPS_COD, FILI_COD, FC3C_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC3C2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC3C3: (EMPS_COD, FILI_COD, EXEC_ID, FC3C_COD_LANCTO)
- IX_PFI_FC3C4: (EXEC_ID, EMPS_COD, FILI_COD, PROD_COD)

---

## PFI_FC4A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC4A_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC4A_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC4A_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC4A_PER_RATEIO | NUMBER | Y |  |  |
| 8 | FC4A_VAL_CUS_ENE | NUMBER | Y |  |  |
| 9 | FC4A_VAL_ICM_ENE | NUMBER | Y |  |  |
| 10 | ETAPA | NUMBER(2) | Y |  |  |

**PK**: FC4A_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC4A1: (EMPS_COD, FILI_COD, EXEC_ID)

---

## PFI_FC4B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC4B_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC4B_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC4B_DSC_INSUMO | VARCHAR2(150) | Y |  |  |
| 7 | FC4B_COD_INSUMO | VARCHAR2(40) | Y |  |  |
| 8 | FC4B_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 9 | FC4B_QTD | NUMBER | Y |  |  |
| 10 | FC4B_VAL_PRECO | NUMBER | Y |  |  |
| 11 | FC4B_VAL_SAIDA | NUMBER | Y |  |  |
| 12 | FC4B_PER | NUMBER | Y |  |  |
| 13 | ETAPA | NUMBER(2) | Y |  |  |

**PK**: FC4B_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC4BI1: (EMPS_COD, FILI_COD, EXEC_ID)

---

## PFI_FC4C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC4C_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC4C_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC4C_TIP_RATEIO | CHAR(1) | Y |  |  |
| 7 | FC4C_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 8 | FC4C_PER | NUMBER | Y |  |  |
| 9 | FC4C_VAL_CUSTO | NUMBER | Y |  |  |
| 10 | FC4C_VAL_ICMS | NUMBER | Y |  |  |
| 11 | FC4C_DSC_OBS | VARCHAR2(255) | Y |  |  |
| 12 | ETAPA | NUMBER(2) | Y |  |  |

**PK**: FC4C_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC4CI1: (EMPS_COD, FILI_COD, EXEC_ID)

---

## PFI_FC5A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5A_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC5A_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5A_DSC_PRODUTO | VARCHAR2(150) | Y |  |  |
| 7 | FC5A_COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | FC5A_COD_UNID | VARCHAR2(6) | Y |  |  |
| 9 | FC5A_QTD_PRODUTO | NUMBER | Y |  |  |
| 10 | FC5A_COD_INSUMO | VARCHAR2(60) | Y |  |  |
| 11 | FC5A_QTD_INSUMO | NUMBER | Y |  |  |
| 12 | FC5A_QTD_UNID | NUMBER | Y |  |  |
| 13 | FC5A_VAL_CUS_UNI | NUMBER | Y |  |  |
| 14 | FC5A_VAL_CUS_TOT | NUMBER | Y |  |  |
| 15 | FC5A_VAL_ICM_UNI | NUMBER | Y |  |  |
| 16 | FC5A_VAL_ICM_TOT | NUMBER | Y |  |  |
| 17 | FC5A_QTD_PERDA | NUMBER | Y |  |  |
| 18 | FC5A_COD_NSTQ | VARCHAR2(5) | Y |  |  |
| 19 | FC5A_OBS | VARCHAR2(255) | Y |  |  |
| 20 | ETAPA | NUMBER(2) | Y |  |  |
| 21 | FC5A_NUM_ORD_FAB | VARCHAR2(40) | Y |  |  |
| 22 | FC5A_COD_FICHA | CHAR(2) | Y |  |  |

**PK**: FC5A_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC5A1: (EMPS_COD, FILI_COD, EXEC_ID)

---

## PFI_FC5B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5B_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 6 | FC5B_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 7 | FC5B_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC5B_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 9 | FC5B_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 10 | FC5B_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC5B_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 12 | FC5B_COD_CFOP | NUMBER(4) | Y |  |  |
| 13 | FC5B_COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 14 | FC5B_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 15 | FC5B_COD_FICHAPD | VARCHAR2(2) | Y |  |  |
| 16 | FC5B_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 17 | FC5B_QTD_ENT | NUMBER | Y |  |  |
| 18 | FC5B_QTD_SAI | NUMBER | Y |  |  |
| 19 | FC5B_VAL_ITEM | NUMBER | Y |  |  |
| 20 | FC5B_QTD_SLD | NUMBER | Y |  |  |
| 21 | ETAPA | NUMBER(2) | Y |  |  |
| 22 | FC5B_CATG_COD | VARCHAR2(5) | Y |  |  |
| 23 | FC5B_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC5B_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC5B1: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC5B2: (EMPS_COD, FILI_COD, EXEC_ID, PROD_COD)

---

## PFI_FC5C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5C_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC5C_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5C_COD_PARTIC | VARCHAR2(18) | Y |  |  |
| 7 | FC5C_DSC_NOME | VARCHAR2(150) | Y |  |  |
| 8 | FC5C_COD_PAIS | NUMBER(5) | Y |  |  |
| 9 | FC5C_COD_CPFCNPJ | VARCHAR2(16) | Y |  |  |
| 10 | FC5C_COD_IE | VARCHAR2(15) | Y |  |  |
| 11 | FC5C_COD_IE_ST | VARCHAR2(15) | Y |  |  |
| 12 | FC5C_END | VARCHAR2(70) | Y |  |  |
| 13 | FC5C_END_NUM | VARCHAR2(10) | Y |  |  |
| 14 | FC5C_END_COMPL | VARCHAR2(45) | Y |  |  |
| 15 | FC5C_END_BAIRRO | VARCHAR2(60) | Y |  |  |
| 16 | FC5C_END_CIDA | VARCHAR2(7) | Y |  |  |
| 17 | FC5C_END_CEP | NUMBER(8) | Y |  |  |
| 18 | FC5C_END_UF | VARCHAR2(2) | Y |  |  |
| 19 | FC5C_END_FONE | VARCHAR2(22) | Y |  |  |
| 20 | FC5C_OBS | VARCHAR2(255) | Y |  |  |
| 21 | ETAPA | NUMBER(2) | Y |  |  |

**PK**: FC5C_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC5C1: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC5C2: (FC5C_COD_PARTIC)

---

## PFI_FC5C_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5C_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC5C_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5C_COD_PARTIC | VARCHAR2(18) | Y |  |  |
| 7 | FC5C_DSC_NOME | VARCHAR2(150) | Y |  |  |
| 8 | FC5C_COD_PAIS | NUMBER(5) | Y |  |  |
| 9 | FC5C_COD_CPFCNPJ | VARCHAR2(16) | Y |  |  |
| 10 | FC5C_COD_IE | VARCHAR2(15) | Y |  |  |
| 11 | FC5C_END | VARCHAR2(70) | Y |  |  |
| 12 | FC5C_END_NUM | VARCHAR2(10) | Y |  |  |
| 13 | FC5C_END_COMPL | VARCHAR2(45) | Y |  |  |
| 14 | FC5C_END_BAIRRO | VARCHAR2(60) | Y |  |  |
| 15 | FC5C_END_CIDA | VARCHAR2(7) | Y |  |  |
| 16 | FC5C_END_CEP | NUMBER(8) | Y |  |  |
| 17 | FC5C_END_UF | VARCHAR2(2) | Y |  |  |
| 18 | FC5C_END_FONE | VARCHAR2(22) | Y |  |  |
| 19 | FC5C_OBS | VARCHAR2(255) | Y |  |  |

**PK**: FC5C_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

**Indexes**:
- IX_PFI_FC5C_S1: (EXEC_ID)

---

## PFI_FC5D

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5D_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC5D_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5D_COD_LEGAL | NUMBER(4) | Y |  |  |
| 7 | FC5D_COD_HIPOT | NUMBER(2) | Y |  |  |
| 8 | FC5D_DSC_ANEXO | VARCHAR2(20) | Y |  |  |
| 9 | FC5D_DSC_ARTIGO | VARCHAR2(20) | Y |  |  |
| 10 | FC5D_DSC_INCISO | VARCHAR2(20) | Y |  |  |
| 11 | FC5D_DSC_ALINEA | VARCHAR2(20) | Y |  |  |
| 12 | FC5D_DSC_PARAG | VARCHAR2(20) | Y |  |  |
| 13 | FC5D_DSC_ITEM | VARCHAR2(20) | Y |  |  |
| 14 | FC5D_DSC_LETRA | VARCHAR2(20) | Y |  |  |
| 15 | FC5D_OBS | VARCHAR2(255) | Y |  |  |
| 16 | ETAPA | NUMBER(2) | Y |  |  |

**PK**: FC5D_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC5D1: (EMPS_COD, FILI_COD, EXEC_ID)

---

## PFI_FC5D_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5D_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC5D_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5D_COD_LEGAL | NUMBER(4) | N |  |  |
| 7 | FC5D_COD_HIPOT | NUMBER(2) | Y |  |  |
| 8 | FC5D_DSC_ANEXO | VARCHAR2(20) | Y |  |  |
| 9 | FC5D_DSC_ARTIGO | VARCHAR2(20) | Y |  |  |
| 10 | FC5D_DSC_INCISO | VARCHAR2(20) | Y |  |  |
| 11 | FC5D_DSC_ALINEA | VARCHAR2(20) | Y |  |  |
| 12 | FC5D_DSC_PARAG | VARCHAR2(20) | Y |  |  |
| 13 | FC5D_DSC_ITEM | VARCHAR2(20) | Y |  |  |
| 14 | FC5D_DSC_LETRA | VARCHAR2(20) | Y |  |  |
| 15 | FC5D_OBS | VARCHAR2(255) | Y |  |  |

**PK**: FC5D_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

**Indexes**:
- IX_PFI_FC5D_S1: (EXEC_ID)

---

## PFI_FC5F

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5F_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC5F_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5F_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC5F_DSC_ITEM | VARCHAR2(150) | Y |  |  |
| 8 | FC5F_COD_UNID | VARCHAR2(6) | Y |  |  |
| 9 | FC5F_OBS | VARCHAR2(255) | Y |  |  |
| 10 | ETAPA | NUMBER(2) | Y |  |  |

**PK**: FC5F_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC5F1: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC5F2: (EXEC_ID, EMPS_COD, FILI_COD, FC5F_COD_ITEM)

---

## PFI_FC5G

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5G_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC5G_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5G_DSC_PROD | VARCHAR2(150) | Y |  |  |
| 7 | FC5G_COD_PROD | VARCHAR2(60) | Y |  |  |
| 8 | FC5G_COD_INSUMO | VARCHAR2(60) | Y |  |  |
| 9 | FC5G_NUM_LLC | NUMBER(3) | Y |  |  |
| 10 | FC5G_QTD | NUMBER | Y |  |  |
| 11 | FC5G_QTD_INS_UNI | NUMBER | Y |  |  |
| 12 | FC5G_VAL_CUSTO | NUMBER | Y |  |  |
| 13 | FC5G_VAL_ICMS | NUMBER | Y |  |  |
| 14 | FC5G_IND_CF | CHAR(1) | Y |  |  |
| 15 | FC5G_IND_RATEIO | CHAR(1) | Y |  |  |
| 16 | FC5G_NUM_ORD_FAB | VARCHAR2(40) | Y |  |  |
| 17 | FC5G_COD_NSTQ | VARCHAR2(5) | Y |  |  |
| 18 | FC5G_NUM_EXE_UTIL | NUMBER(20) | Y |  |  |
| 19 | FC5G_COD_FICHA | VARCHAR2(2) | Y |  |  |
| 20 | ETAPA | NUMBER(2) | Y |  |  |
| 21 | FC5G_REPARO | CHAR(1) | Y |  |  |

**PK**: FC5G_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC5G1: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC5G2: (EMPS_COD, FILI_COD, FC5G_DAT_LANCTO, FC5G_COD_PROD, FC5G_NUM_ORD_FAB, FC5G_NUM_EXE_UTIL)
- IX_PFI_FC5G3: (EMPS_COD, FILI_COD, FC5G_DAT_LANCTO, FC5G_NUM_ORD_FAB, FC5G_NUM_EXE_UTIL)

---

## PFI_FC5H

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5H_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC5H_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5H_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 7 | FC5H_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 8 | FC5H_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 9 | FC5H_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 10 | FC5H_DAT_EMIS | DATE | Y |  |  |
| 11 | FC5H_NUM_DOC_EXP | VARCHAR2(15) | Y |  |  |
| 12 | FC5H_COD_SER_EXP | VARCHAR2(5) | Y |  |  |
| 13 | FC5H_NU_DECLAR | VARCHAR2(15) | Y |  |  |
| 14 | FC5H_OBS | VARCHAR2(255) | Y |  |  |
| 15 | ETAPA | NUMBER(2) | Y |  |  |

**PK**: FC5H_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC5H1: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC5H2: (EXEC_ID, FC5H_NUM_LANCTO)

---

## PFI_FC5H_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5H_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC5H_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5H_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 7 | FC5H_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 8 | FC5H_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 9 | FC5H_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 10 | FC5H_DAT_EMIS | DATE | Y |  |  |
| 11 | FC5H_NUM_DOC_EXP | VARCHAR2(15) | Y |  |  |
| 12 | FC5H_COD_SER_EXP | VARCHAR2(5) | Y |  |  |
| 13 | FC5H_NU_DECLAR | VARCHAR2(15) | Y |  |  |
| 14 | FC5H_OBS | VARCHAR2(255) | Y |  |  |

**PK**: FC5H_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

**Indexes**:
- IX_PFI_FC5H_S1: (EXEC_ID)

---

## PFI_FC5I

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC5I_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC5I_DAT_LANCTO | DATE | Y |  |  |
| 6 | FC5I_COD_VEICULO | NUMBER(20) | Y |  |  |
| 7 | FC5I_COD_PLACA | VARCHAR2(7) | Y |  |  |
| 8 | FC5I_COD_CPFCNPJ | VARCHAR2(16) | Y |  |  |
| 9 | FC5I_COD_UF | VARCHAR2(2) | Y |  |  |
| 10 | FC5I_COD_CIDA | VARCHAR2(7) | Y |  |  |
| 11 | FC5I_COD_RENAVAM | VARCHAR2(20) | Y |  |  |
| 12 | FC5I_COD_MARCA | VARCHAR2(3) | Y |  |  |
| 13 | FC5I_DSC_MODELO | VARCHAR2(150) | Y |  |  |
| 14 | FC5I_NUM_ANO_FAB | NUMBER(4) | Y |  |  |
| 15 | FC5I_VAL_REND | NUMBER | Y |  |  |
| 16 | FC5I_OBS | VARCHAR2(255) | Y |  |  |
| 17 | ETAPA | NUMBER(2) | Y |  |  |

**PK**: FC5I_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC5I1: (EMPS_COD, FILI_COD, EXEC_ID)

---

## PFI_FC6A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6A_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC6A_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6A_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6A_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6A_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6A_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6A_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6A_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6A_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6A_VAL_TOTAL | NUMBER | Y |  |  |
| 14 | FC6A_VAL_BASE | NUMBER | Y |  |  |
| 15 | FC6A_QTD | NUMBER | Y |  |  |
| 16 | FC6A_ALI | NUMBER | Y |  |  |
| 17 | FC6A_VAL_ICM_DEB | NUMBER | Y |  |  |
| 18 | FC6A_VAL_CUSTO | NUMBER | Y |  |  |
| 19 | FC6A_VAL_ICMS | NUMBER | Y |  |  |
| 20 | FC6A_PER_CRE | NUMBER | Y |  |  |
| 21 | FC6A_VAL_CRE | NUMBER | Y |  |  |
| 22 | FC6A_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | FC6A_VAL_ICM_TOT | NUMBER | Y |  |  |
| 24 | FC6A_VAL_CRE_ACU | NUMBER | Y |  |  |
| 25 | ETAPA | NUMBER(2) | Y |  |  |
| 26 | FC6A_NUM_ITEM | VARCHAR2(5) | Y |  |  |

**PK**: FC6A_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC6A1: (EMPS_COD, FILI_COD, FC6A_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC6A2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC6A3: (EXEC_ID, EMPS_COD, FILI_COD, FC6A_DAT_MOVTO, FC6A_NUM_LANCTO)
- IX_PFI_FC6A4: (EMPS_COD, FILI_COD, FC6A_DAT_MOVTO)
- IX_PFI_FC6A5: (FC6A_COD_DEST)

---

## PFI_FC6A_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6A_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC6A_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6A_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6A_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6A_COD_CFOP | NUMBER(4) | N |  |  |
| 9 | FC6A_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6A_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6A_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6A_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6A_VAL_TOTAL | NUMBER | Y |  |  |
| 14 | FC6A_VAL_BASE | NUMBER | Y |  |  |
| 15 | FC6A_QTD | NUMBER | Y |  |  |
| 16 | FC6A_ALI | NUMBER | Y |  |  |
| 17 | FC6A_VAL_ICM_DEB | NUMBER | Y |  |  |
| 18 | FC6A_VAL_CUSTO | NUMBER | Y |  |  |
| 19 | FC6A_VAL_ICMS | NUMBER | Y |  |  |
| 20 | FC6A_PER_CRE | NUMBER | Y |  |  |
| 21 | FC6A_VAL_CRE | NUMBER | Y |  |  |
| 22 | FC6A_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | FC6A_VAL_ICM_TOT | NUMBER | Y |  |  |
| 24 | FC6A_VAL_CRE_ACU | NUMBER | Y |  |  |
| 25 | FC6A_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 26 | FC6A_TIP_DOC | CHAR(3) | Y |  |  |
| 27 | FC6A_IVA | NUMBER(15,4) | Y |  |  |
| 28 | FC6A_PER_MED | NUMBER(15,4) | Y |  |  |
| 29 | FC6A_CRE_EST | NUMBER(15,2) | Y |  |  |

**PK**: FC6A_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

---

## PFI_FC6B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6B_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC6B_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6B_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6B_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6B_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6B_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6B_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6B_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6B_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6B_VAL_TOTAL | NUMBER | Y |  |  |
| 14 | FC6B_VAL_BASE | NUMBER | Y |  |  |
| 15 | FC6B_QTD | NUMBER | Y |  |  |
| 16 | FC6B_ALI | NUMBER | Y |  |  |
| 17 | FC6B_VAL_ICM_DEB | NUMBER | Y |  |  |
| 18 | FC6B_VAL_CUSTO | NUMBER | Y |  |  |
| 19 | FC6B_VAL_ICMS | NUMBER | Y |  |  |
| 20 | FC6B_PER_CRE | NUMBER | Y |  |  |
| 21 | FC6B_VAL_CRE | NUMBER | Y |  |  |
| 22 | FC6B_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | FC6B_VAL_ICM_TOT | NUMBER | Y |  |  |
| 24 | FC6B_VAL_CRE_ACU | NUMBER | Y |  |  |
| 25 | ETAPA | NUMBER(2) | Y |  |  |
| 26 | FC6B_NUM_ITEM | VARCHAR2(5) | Y |  |  |

**PK**: FC6B_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC6B1: (EMPS_COD, FILI_COD, FC6B_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC6B2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC6B3: (EXEC_ID, EMPS_COD, FILI_COD, FC6B_DAT_MOVTO, FC6B_NUM_LANCTO)
- IX_PFI_FC6B4: (EMPS_COD, FILI_COD, FC6B_DAT_MOVTO)
- IX_PFI_FC6B5: (FC6B_COD_DEST)

---

## PFI_FC6B_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6B_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC6B_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6B_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6B_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6B_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6B_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6B_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6B_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6B_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6B_VAL_TOTAL | NUMBER | Y |  |  |
| 14 | FC6B_VAL_BASE | NUMBER | Y |  |  |
| 15 | FC6B_QTD | NUMBER | Y |  |  |
| 16 | FC6B_ALI | NUMBER | Y |  |  |
| 17 | FC6B_VAL_ICM_DEB | NUMBER | Y |  |  |
| 18 | FC6B_VAL_CUSTO | NUMBER | Y |  |  |
| 19 | FC6B_VAL_ICMS | NUMBER | Y |  |  |
| 20 | FC6B_PER_CRE | NUMBER | Y |  |  |
| 21 | FC6B_VAL_CRE | NUMBER | Y |  |  |
| 22 | FC6B_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | FC6B_VAL_ICM_TOT | NUMBER | Y |  |  |
| 24 | FC6B_VAL_CRE_ACU | NUMBER | Y |  |  |
| 25 | FC6B_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 26 | FC6B_TIP_DOC | CHAR(3) | Y |  |  |
| 27 | FC6B_IVA | NUMBER(15,4) | Y |  |  |
| 28 | FC6B_PER_MED | NUMBER(15,4) | Y |  |  |
| 29 | FC6B_CRE_EST | NUMBER(15,2) | Y |  |  |

**PK**: FC6B_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

---

## PFI_FC6C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6C_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC6C_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6C_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6C_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6C_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6C_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6C_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6C_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6C_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6C_NUM_DDEDSE | VARCHAR2(20) | Y |  |  |
| 14 | FC6C_COD_COMPR | VARCHAR2(3) | Y |  |  |
| 15 | FC6C_VAL_TOTAL | NUMBER | Y |  |  |
| 16 | FC6C_VAL_CUSTO | NUMBER | Y |  |  |
| 17 | FC6C_VAL_BASE | NUMBER | Y |  |  |
| 18 | FC6C_QTD | NUMBER | Y |  |  |
| 19 | FC6C_VAL_ICMS | NUMBER | Y |  |  |
| 20 | FC6C_PER_CRE | NUMBER | Y |  |  |
| 21 | FC6C_VAL_CRE | NUMBER | Y |  |  |
| 22 | FC6C_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | FC6C_VAL_CRE_COM | NUMBER | Y |  |  |
| 24 | FC6C_VAL_ICM_COM | NUMBER | Y |  |  |
| 25 | FC6C_VAL_CRE_ACU | NUMBER | Y |  |  |
| 26 | FC6C_DAT_EXPORT | DATE | Y |  |  |
| 27 | FC6C_DAT_AVERB | DATE | Y |  |  |
| 28 | FC6C_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 29 | ETAPA | NUMBER(2) | Y |  |  |
| 30 | FC6C_NUM_ITEM | VARCHAR2(5) | Y |  |  |

**PK**: FC6C_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC6C1: (EMPS_COD, FILI_COD, FC6C_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC6C2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC6C3: (EXEC_ID, EMPS_COD, FILI_COD, FC6C_DAT_MOVTO, FC6C_NUM_LANCTO)
- IX_PFI_FC6C4: (EMPS_COD, FILI_COD, FC6C_DAT_MOVTO)
- IX_PFI_FC6C5: (FC6C_COD_DEST)

---

## PFI_FC6C_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6C_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC6C_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6C_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6C_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6C_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6C_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6C_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6C_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6C_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6C_NUM_DDEDSE | VARCHAR2(20) | Y |  |  |
| 14 | FC6C_COD_COMPR | VARCHAR2(3) | Y |  |  |
| 15 | FC6C_VAL_TOTAL | NUMBER | Y |  |  |
| 16 | FC6C_VAL_CUSTO | NUMBER | Y |  |  |
| 17 | FC6C_VAL_BASE | NUMBER | Y |  |  |
| 18 | FC6C_QTD | NUMBER | Y |  |  |
| 19 | FC6C_VAL_ICMS | NUMBER | Y |  |  |
| 20 | FC6C_PER_CRE | NUMBER | Y |  |  |
| 21 | FC6C_VAL_CRE | NUMBER | Y |  |  |
| 22 | FC6C_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | FC6C_VAL_CRE_COM | NUMBER | Y |  |  |
| 24 | FC6C_VAL_ICM_COM | NUMBER | Y |  |  |
| 25 | FC6C_VAL_CRE_ACU | NUMBER | Y |  |  |
| 26 | FC6C_DAT_EXPORT | DATE | Y |  |  |
| 27 | FC6C_DAT_AVERB | DATE | Y |  |  |
| 28 | FC6C_COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 29 | FC6C_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 30 | FC6C_TIP_DOC | CHAR(3) | Y |  |  |
| 31 | FC6C_IVA | NUMBER(15,4) | Y |  |  |
| 32 | FC6C_PER_MED | NUMBER(15,4) | Y |  |  |
| 33 | FC6C_CRE_EST | NUMBER(15,2) | Y |  |  |

**PK**: FC6C_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

---

## PFI_FC6D

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6D_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC6D_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6D_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6D_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6D_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6D_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6D_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6D_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6D_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6D_COD_COMPR | VARCHAR2(3) | Y |  |  |
| 14 | FC6D_VAL_TOTAL | NUMBER | Y |  |  |
| 15 | FC6D_VAL_CUSTO | NUMBER | Y |  |  |
| 16 | FC6D_VAL_BASE | NUMBER | Y |  |  |
| 17 | FC6D_QTD | NUMBER | Y |  |  |
| 18 | FC6D_VAL_ICMS | NUMBER | Y |  |  |
| 19 | FC6D_PER_CRE_OUT | NUMBER | Y |  |  |
| 20 | FC6D_VAL_CRE_OUT | NUMBER | Y |  |  |
| 21 | FC6D_VAL_ICM_OUT | NUMBER | Y |  |  |
| 22 | FC6D_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | FC6D_VAL_CRE_ACU | NUMBER | Y |  |  |
| 24 | ETAPA | NUMBER(2) | Y |  |  |
| 25 | FC6D_NUM_ITEM | VARCHAR2(5) | Y |  |  |

**PK**: FC6D_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC6D1: (EMPS_COD, FILI_COD, FC6D_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC6D2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC6D3: (EXEC_ID, EMPS_COD, FILI_COD, FC6D_DAT_MOVTO, FC6D_NUM_LANCTO)
- IX_PFI_FC6D4: (EMPS_COD, FILI_COD, FC6D_DAT_MOVTO)
- IX_PFI_FC6D5: (FC6D_COD_DEST)

---

## PFI_FC6D_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6D_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC6D_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6D_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6D_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6D_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6D_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6D_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6D_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6D_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6D_COD_COMPR | VARCHAR2(3) | Y |  |  |
| 14 | FC6D_VAL_TOTAL | NUMBER | Y |  |  |
| 15 | FC6D_VAL_CUSTO | NUMBER | Y |  |  |
| 16 | FC6D_VAL_BASE | NUMBER | Y |  |  |
| 17 | FC6D_QTD | NUMBER | Y |  |  |
| 18 | FC6D_VAL_ICMS | NUMBER | Y |  |  |
| 19 | FC6D_PER_CRE_OUT | NUMBER | Y |  |  |
| 20 | FC6D_VAL_CRE_OUT | NUMBER | Y |  |  |
| 21 | FC6D_VAL_ICM_OUT | NUMBER | Y |  |  |
| 22 | FC6D_VAL_CRE_DES | NUMBER | Y |  |  |
| 23 | FC6D_VAL_CRE_ACU | NUMBER | Y |  |  |
| 24 | FC6D_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 25 | FC6D_TIP_DOC | CHAR(3) | Y |  |  |
| 26 | FC6D_IVA | NUMBER(15,4) | Y |  |  |
| 27 | FC6D_PER_MED | NUMBER(15,4) | Y |  |  |
| 28 | FC6D_CRE_EST | NUMBER(15,2) | Y |  |  |

**PK**: FC6D_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

---

## PFI_FC6E

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6E_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC6E_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6E_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6E_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6E_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6E_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6E_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6E_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6E_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6E_VAL_TOTAL | NUMBER | Y |  |  |
| 14 | FC6E_VAL_CUSTO | NUMBER | Y |  |  |
| 15 | FC6E_VAL_BASE | NUMBER | Y |  |  |
| 16 | FC6E_QTD | NUMBER | Y |  |  |
| 17 | FC6E_VAL_ICMS | NUMBER | Y |  |  |
| 18 | FC6E_PER_CRE | NUMBER | Y |  |  |
| 19 | FC6E_VAL_CRE | NUMBER | Y |  |  |
| 20 | FC6E_VAL_CRE_DES | NUMBER | Y |  |  |
| 21 | FC6E_VAL_CRE_ACU | NUMBER | Y |  |  |
| 22 | ETAPA | NUMBER(2) | Y |  |  |
| 23 | FC6E_NUM_ITEM | VARCHAR2(5) | Y |  |  |

**PK**: FC6E_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC6E1: (EMPS_COD, FILI_COD, FC6E_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC6E2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC6E3: (EXEC_ID, EMPS_COD, FILI_COD, FC6E_DAT_MOVTO, FC6E_NUM_LANCTO)
- IX_PFI_FC6E4: (EMPS_COD, FILI_COD, FC6E_DAT_MOVTO)
- IX_PFI_FC6E5: (FC6E_COD_DEST)

---

## PFI_FC6E_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6E_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC6E_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6E_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6E_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6E_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6E_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6E_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6E_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6E_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 13 | FC6E_VAL_TOTAL | NUMBER | Y |  |  |
| 14 | FC6E_VAL_CUSTO | NUMBER | Y |  |  |
| 15 | FC6E_VAL_BASE | NUMBER | Y |  |  |
| 16 | FC6E_QTD | NUMBER | Y |  |  |
| 17 | FC6E_VAL_ICMS | NUMBER | Y |  |  |
| 18 | FC6E_PER_CRE | NUMBER | Y |  |  |
| 19 | FC6E_VAL_CRE | NUMBER | Y |  |  |
| 20 | FC6E_VAL_CRE_DES | NUMBER | Y |  |  |
| 21 | FC6E_VAL_CRE_ACU | NUMBER | Y |  |  |
| 22 | FC6E_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 23 | FC6E_TIP_DOC | CHAR(3) | Y |  |  |
| 24 | FC6E_IVA | NUMBER(15,4) | Y |  |  |
| 25 | FC6E_PER_MED | NUMBER(15,4) | Y |  |  |
| 26 | FC6E_CRE_EST | NUMBER(15,2) | Y |  |  |

**PK**: FC6E_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

---

## PFI_FC6F

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6F_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC6F_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6F_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6F_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6F_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6F_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6F_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6F_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6F_VAL_TOTAL | NUMBER | Y |  |  |
| 13 | FC6F_VAL_BASE | NUMBER | Y |  |  |
| 14 | FC6F_QTD | NUMBER | Y |  |  |
| 15 | FC6F_ALI | NUMBER | Y |  |  |
| 16 | FC6F_VAL_ICM_DEB | NUMBER | Y |  |  |
| 17 | FC6F_VAL_CUSTO | NUMBER | Y |  |  |
| 18 | FC6F_VAL_ICMS | NUMBER | Y |  |  |
| 19 | FC6F_PER_CRE | NUMBER | Y |  |  |
| 20 | FC6F_VAL_CRE | NUMBER | Y |  |  |
| 21 | FC6F_VAL_CRE_DES | NUMBER | Y |  |  |
| 22 | FC6F_VAL_ICM_TOT | NUMBER | Y |  |  |
| 23 | FC6F_VAL_ICM_DEV | NUMBER | Y |  |  |
| 24 | ETAPA | NUMBER(2) | Y |  |  |
| 25 | FC6F_NUM_ITEM | VARCHAR2(5) | Y |  |  |

**PK**: FC6F_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC6F1: (EMPS_COD, FILI_COD, FC6F_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC6F2: (EMPS_COD, FILI_COD, EXEC_ID)
- IX_PFI_FC6F3: (EXEC_ID, EMPS_COD, FILI_COD, FC6F_DAT_MOVTO, FC6F_NUM_LANCTO)
- IX_PFI_FC6F4: (EMPS_COD, FILI_COD, FC6F_DAT_MOVTO)
- IX_PFI_FC6F5: (FC6F_COD_DEST)

---

## PFI_FC6F_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6F_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | FC6F_NUM_LANCTO | NUMBER(20) | Y |  |  |
| 6 | FC6F_COD_ITEM | VARCHAR2(60) | Y |  |  |
| 7 | FC6F_DAT_MOVTO | DATE | Y |  |  |
| 8 | FC6F_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6F_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 10 | FC6F_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6F_COD_DEST | VARCHAR2(18) | Y |  |  |
| 12 | FC6F_VAL_TOTAL | NUMBER | Y |  |  |
| 13 | FC6F_VAL_BASE | NUMBER | Y |  |  |
| 14 | FC6F_QTD | NUMBER | Y |  |  |
| 15 | FC6F_ALI | NUMBER | Y |  |  |
| 16 | FC6F_VAL_ICM_DEB | NUMBER | Y |  |  |
| 17 | FC6F_VAL_CUSTO | NUMBER | Y |  |  |
| 18 | FC6F_VAL_ICMS | NUMBER | Y |  |  |
| 19 | FC6F_PER_CRE | NUMBER | Y |  |  |
| 20 | FC6F_VAL_CRE | NUMBER | Y |  |  |
| 21 | FC6F_VAL_CRE_DES | NUMBER | Y |  |  |
| 22 | FC6F_VAL_ICM_TOT | NUMBER | Y |  |  |
| 23 | FC6F_VAL_ICM_DEV | NUMBER | Y |  |  |
| 24 | FC6F_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 25 | FC6F_TIP_DOC | CHAR(3) | Y |  |  |
| 26 | FC6F_NUM_DDEDSE | VARCHAR2(20) | Y |  |  |

**PK**: FC6F_ID

**FKs**:
- EXEC_ID → PFI_EXEC_S(EXEC_ID)

---

## PFI_FC6G

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6G_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC6G_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 6 | FC6G_DAT_MOVTO | DATE | Y |  |  |
| 7 | FC6G_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 8 | FC6G_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6G_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 10 | FC6G_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6G_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 12 | FC6G_COD_REM | VARCHAR2(18) | Y |  |  |
| 13 | FC6G_COD_DEST | VARCHAR2(18) | Y |  |  |
| 14 | FC6G_COD_UF_ORI | VARCHAR2(2) | Y |  |  |
| 15 | FC6G_COD_UF_DES | VARCHAR2(2) | Y |  |  |
| 16 | FC6G_COD_TOMADOR | VARCHAR2(18) | Y |  |  |
| 17 | FC6G_ALI | NUMBER | Y |  |  |
| 18 | FC6G_VAL_PRE_NGE | NUMBER | Y |  |  |
| 19 | FC6G_VAL_ICM_NGE | NUMBER | Y |  |  |
| 20 | FC6G_VAL_PRE_GE | NUMBER | Y |  |  |
| 21 | FC6G_VAL_ICM_GE | NUMBER | Y |  |  |
| 22 | FC6G_VAL_CRE_PR | NUMBER | Y |  |  |
| 23 | FC6G_VAL_CRE_ST | NUMBER | Y |  |  |
| 24 | FC6G_VAL_CRE_ACU | NUMBER | Y |  |  |
| 25 | FC6G_VAL_ICM_DEV | NUMBER | Y |  |  |
| 26 | ETAPA | NUMBER(2) | Y |  |  |
| 27 | FC6G_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC6G_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC6G1: (EMPS_COD, FILI_COD, FC6G_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC6G2: (EMPS_COD, FILI_COD, EXEC_ID)

---

## PFI_FC6H

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FC6H_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 4 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 5 | FC6H_NUM_ORDEM | NUMBER(20) | Y |  |  |
| 6 | FC6H_DAT_MOVTO | DATE | Y |  |  |
| 7 | FC6H_DSC_HIST | VARCHAR2(255) | Y |  |  |
| 8 | FC6H_COD_CFOP | NUMBER(4) | Y |  |  |
| 9 | FC6H_TIP_DOCTO | NUMBER(3) | Y |  |  |
| 10 | FC6H_COD_SERIE | VARCHAR2(5) | Y |  |  |
| 11 | FC6H_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 12 | FC6H_COD_REM | VARCHAR2(18) | Y |  |  |
| 13 | FC6H_COD_DEST | VARCHAR2(18) | Y |  |  |
| 14 | FC6H_COD_UF_ORI | VARCHAR2(2) | Y |  |  |
| 15 | FC6H_COD_UF_DES | VARCHAR2(2) | Y |  |  |
| 16 | FC6H_COD_TOMADOR | VARCHAR2(18) | Y |  |  |
| 17 | FC6H_COD_VEICULO | NUMBER(20) | Y |  |  |
| 18 | FC6H_NUM_KM | NUMBER | Y |  |  |
| 19 | FC6H_COD_CLASSIF | NUMBER(20) | Y |  |  |
| 20 | FC6H_ALI | NUMBER | Y |  |  |
| 21 | FC6H_VAL_PREST | NUMBER | Y |  |  |
| 22 | FC6H_VAL_ICMS_DEB | NUMBER | Y |  |  |
| 23 | FC6H_VAL_RATEIO | NUMBER | Y |  |  |
| 24 | FC6H_VAL_CUSTO | NUMBER | Y |  |  |
| 25 | FC6H_VAL_ICMS | NUMBER | Y |  |  |
| 26 | FC6H_VAL_CRED_ACU | NUMBER | Y |  |  |
| 27 | FC6H_VAL_ICMS_DEV | NUMBER | Y |  |  |
| 28 | ETAPA | NUMBER(2) | Y |  |  |
| 29 | FC6H_CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: FC6H_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

**Indexes**:
- IX_PFI_FC6H1: (EMPS_COD, FILI_COD, FC6H_DAT_MOVTO, EXEC_ID)
- IX_PFI_FC6H2: (EMPS_COD, FILI_COD, EXEC_ID)

---

## PFI_FICH

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FICH_ID | NUMBER(20) | N |  |  |
| 2 | FICH_COD_OBRIG | VARCHAR2(10) | Y |  |  |
| 3 | FICH_COD | VARCHAR2(2) | Y |  |  |
| 4 | FICH_DSC | VARCHAR2(200) | Y |  |  |
| 5 | FICH_IND_ATIVA | CHAR(1) | Y |  |  |

**PK**: FICH_ID

---

## PFI_GRID

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRID_COD_CAMPO | VARCHAR2(18) | N |  |  |
| 2 | GRID_NUM_ID | NUMBER(20) | Y |  |  |

**PK**: GRID_COD_CAMPO

---

## PFI_HAUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | HAUD_ID | VARCHAR2(20) | N |  |  |
| 2 | AUDI_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | HAUD_DAT_INI | DATE | N |  |  |
| 6 | HAUD_DAT_FIM | DATE | N |  |  |
| 7 | HAUD_TIPO | VARCHAR2(5) | N |  |  |
| 8 | HAUD_ETP | VARCHAR2(7) | N |  |  |
| 9 | HAUD_MSG_ERR | VARCHAR2(150) | N |  |  |
| 10 | HAUD_OBJ_ERR | VARCHAR2(300) | N |  |  |
| 11 | HAUD_OBJ_ERR_SER | BLOB | Y |  |  |

**PK**: HAUD_ID

**FKs**:
- AUDI_ID → PFI_AUDI(AUDI_ID)

---

## PFI_IVA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | COD_IVA | NUMBER(15,4) | N |  |  |
| 4 | DAT_INI | DATE | N |  |  |
| 5 | DAT_FIM | DATE | Y |  |  |

**PK**: EMPS_COD, FILI_COD, COD_IVA, DAT_INI

---

## PFI_LDAE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LDAE_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 3 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 4 | LDAE_COD_OBRIGACAO | VARCHAR2(10) | Y |  |  |
| 5 | LDAE_COD_VERSAO | VARCHAR2(2) | Y |  |  |
| 6 | LDAE_DSC_ARQUIVO | VARCHAR2(2) | Y |  |  |
| 7 | LDAE_USR | VARCHAR2(40) | Y |  |  |
| 8 | LDAE_DAT_ATUA | DATE | Y |  |  |

**PK**: LDAE_ID

---

## PFI_LOG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EXEC_ID | NUMBER | N |  |  |
| 2 | LOG_ORDEM | NUMBER | N |  |  |
| 3 | LOG_COD_PROC | CHAR(1) | N |  |  |
| 4 | LOG_PROC_MSG | CLOB | Y |  |  |

**PK**: EXEC_ID, LOG_ORDEM, LOG_COD_PROC

---

## PFI_MPCG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MPCG_NOM_PROC | VARCHAR2(60) | N |  |  |
| 2 | MPCG_NUM_PROC | VARCHAR2(20) | N |  |  |
| 3 | MPCG_NOM_USU | VARCHAR2(40) | N |  |  |
| 4 | AGEN_ID | NUMBER(20) | N |  |  |
| 5 | MPCG_TIP_REG | VARCHAR2(20) | Y |  |  |
| 6 | MPCG_STAT | VARCHAR2(40) | Y |  |  |
| 7 | MPCG_INI_EXEC | DATE | Y |  |  |
| 8 | MPCG_FIM_EXEC | DATE | Y |  |  |
| 9 | MPCG_PAR_EXEC_EMP | VARCHAR2(500) | Y |  |  |
| 10 | MPCG_PAR_EXEC_FIL | VARCHAR2(1200) | Y |  |  |
| 11 | MPCG_PAR_EXEC_DT_INI | DATE | Y |  |  |
| 12 | MPCG_PAR_EXEC_DT_FIM | DATE | Y |  |  |
| 13 | MPCG_AGEN_INI | DATE | Y |  |  |
| 14 | MPCG_AGEN_PER | CHAR(1) | Y |  |  |
| 15 | MPCG_REG_LIDOS | NUMBER(20) | Y |  |  |
| 16 | MPCG_REG_GRAV | NUMBER(20) | Y |  |  |
| 17 | MPCG_REG_REJ | NUMBER(20) | Y |  |  |
| 18 | MPCG_REG_ERRO | NUMBER(20) | Y |  |  |
| 19 | MPCG_HISTORICO | VARCHAR2(200) | Y |  |  |

**PK**: MPCG_NOM_PROC, MPCG_NUM_PROC, MPCG_NOM_USU

**FKs**:
- AGEN_ID → PFI_AGEN(AGEN_ID)

**Indexes**:
- IX_PFI_MPCG1: (MPCG_NOM_PROC)
- IX_PFI_MPCG2: (MPCG_NOM_USU)

---

## PFI_P221_NCM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | P221_NCM_ID | NUMBER(9) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 3 | FILI_COD | VARCHAR2(9) | N |  |  |
| 4 | CNBM_COD | VARCHAR2(10) | N |  |  |

**PK**: P221_NCM_ID

**Indexes**:
- UQ_PFI_P221_NCM_CNBM (UNIQUE): (EMPS_COD, FILI_COD, CNBM_COD)

---

## PFI_PAGE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | PAGE_IND_MAT_CTR | CHAR(1) | Y |  |  |
| 3 | PAGE_COD_EMP_MAT | VARCHAR2(9) | Y |  |  |
| 4 | PAGE_COD_FIL_MAT | VARCHAR2(9) | Y |  |  |
| 5 | PAGE_USR | VARCHAR2(40) | Y |  |  |
| 6 | PAGE_DAT_ATUA | DATE | Y |  |  |

**PK**: EMPS_COD

---

## PFI_PCEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MATE_COD | VARCHAR2(60) | N |  |  |
| 4 | PCEM_COD_OPEN1 | CHAR(10) | Y |  |  |
| 5 | PCEM_COD_OPEN2 | CHAR(10) | Y |  |  |
| 6 | PCEM_COD_OPEN3 | CHAR(10) | Y |  |  |
| 7 | PCEM_COD_OPEN4 | CHAR(10) | Y |  |  |
| 8 | PCEM_USR | VARCHAR2(40) | Y |  |  |
| 9 | PCEM_DAT_ATUA | DATE | Y |  |  |

**PK**: EMPS_COD, FILI_COD, MATE_COD

---

## PFI_PEXE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PEXE_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | PEXE_DAT_INI | DATE | Y |  |  |
| 4 | PEXE_DAT_FIM | DATE | Y |  |  |

**PK**: PEXE_ID

**FKs**:
- EXEC_ID → PFI_EXEC(EXEC_ID)

---

## PFI_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(20) | N |  |  |
| 2 | PROC_NOME | VARCHAR2(30) | Y |  |  |

**PK**: PROC_ID

---

## PFI_PROP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROP_NOME | VARCHAR2(50) | N |  |  |
| 2 | PROP_TIPO | CHAR(1) | N |  |  |
| 3 | PROP_VALOR_PARAM | VARCHAR2(20) | Y |  |  |
| 4 | PROP_IND_UTILIZA | CHAR(1) | Y |  |  |
| 5 | PROP_DSC | VARCHAR2(200) | Y |  |  |

**PK**: PROP_NOME

---

## PFI_PSFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PSFE_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 3 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 4 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 5 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 6 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 7 | PSFE_DSC_CAMPO | VARCHAR2(150) | Y |  |  |
| 8 | PSFE_NOM_CAMPO | VARCHAR2(60) | Y |  |  |
| 9 | PSFE_IND_LANCTO | CHAR(1) | Y |  |  |
| 10 | FICH_ID_1 | NUMBER(20) | N |  |  |
| 11 | FICH_ID_2 | NUMBER(20) | Y |  |  |
| 12 | CODL_ID | NUMBER(20) | Y |  |  |
| 13 | PSFE_IND_CALC_C | CHAR(1) | Y |  |  |
| 14 | PSFE_IND_LEGE | CHAR(1) | Y |  |  |
| 15 | PSFE_COD_ELEG | NUMBER(4) | Y |  |  |
| 16 | PSFE_USR | VARCHAR2(40) | Y |  |  |
| 17 | PSFE_DAT_ATUA | DATE | Y |  |  |
| 18 | PSFE_IND_CRED_OUTG | CHAR(1) | Y |  |  |
| 19 | PSFE_VAL_PERC_RAT | NUMBER(17,2) | Y |  |  |
| 20 | PSFE_IND_DES_ZER | CHAR(1) | Y |  |  |
| 21 | PSFE_IND_CF | CHAR(1) | Y |  |  |
| 22 | PSFE_IND_PCAT221 | CHAR(1) | Y |  |  |
| 23 | PSFE_IND_CRED_OUTG_A40 | CHAR(1) | Y |  |  |
| 24 | PSFE_VAL_PERC_A40 | NUMBER | Y |  |  |

**PK**: PSFE_ID

**FKs**:
- CODL_ID → PFI_CODL(CODL_ID)
- FICH_ID_1 → PFI_FICH(FICH_ID)
- FICH_ID_2 → PFI_FICH(FICH_ID)

**Indexes**:
- UQ_PFI_PSFE1 (UNIQUE): (EMPS_COD, FILI_COD, TOPE_COD, CFOP_COD, NOPE_COD, PSFE_DSC_CAMPO, PSFE_NOM_CAMPO, PSFE_IND_LANCTO, PSFE_IND_CF)

---

## PFI_PSFN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PSFN_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 3 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 4 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 5 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | PSFN_IND_RAT_C | CHAR(1) | Y |  |  |
| 7 | PSFN_USR | VARCHAR2(40) | Y |  |  |
| 8 | PSFN_DAT_ATUA | DATE | Y |  |  |
| 9 | PSFN_IND_PER_C | CHAR(1) | Y |  |  |
| 10 | PSFN_PER_NF_C | NUMBER | Y |  |  |
| 11 | PSFN_IND_RAT_F | CHAR(1) | Y |  |  |
| 12 | PSFN_IND_PER_E | CHAR(1) | Y |  |  |
| 13 | PSFN_PER_NF_E | NUMBER | Y |  |  |

**PK**: PSFN_ID

**Indexes**:
- UQ_PFI_PSFN1 (UNIQUE): (EMPS_COD, FILI_COD, CFOP_COD, NOPE_COD)

---

## PFI_PSFN_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PSFN_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 3 | FILI_COD | VARCHAR2(9) | N |  |  |
| 4 | CFOP_COD | VARCHAR2(6) | N |  |  |
| 5 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 6 | FICH_ID | NUMBER(20) | N |  |  |
| 7 | PSFN_IND_DEV | CHAR(1) | N |  |  |
| 8 | PSFN_USR | VARCHAR2(40) | N |  |  |
| 9 | PSFN_DAT_ATUA | DATE | N |  |  |

**PK**: PSFN_ID

---

## PFI_PVAA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | EXEC_ID | NUMBER(20) | N |  |  |
| 4 | PVAA_SEQ | NUMBER(9) | N |  |  |
| 5 | PVAA_COD_REG | VARCHAR2(20) | Y |  |  |
| 6 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 7 | PVAA_TIP_VALOR | CHAR(1) | Y |  |  |
| 8 | PVAA_VAL_CAMPO01 | NUMBER | Y |  |  |
| 9 | PVAA_VAL_CAMPO02 | NUMBER | Y |  |  |
| 10 | PVAA_VAL_CAMPO03 | NUMBER | Y |  |  |
| 11 | PVAA_VAL_CAMPO04 | NUMBER | Y |  |  |

**PK**: EMPS_COD, FILI_COD, EXEC_ID, PVAA_SEQ

---

## PFI_REAE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | REAE_ID | NUMBER(20) | N |  |  |
| 2 | LDAE_ID | NUMBER(20) | Y |  |  |
| 3 | REAE_ID_PARENT | NUMBER(20) | Y |  |  |
| 4 | REAE_NUM_NIVEL | NUMBER(2) | Y |  |  |
| 5 | REAE_COD_REGISTRO | CHAR(4) | Y |  |  |
| 6 | REAE_IND_MANDAT | CHAR(1) | Y |  |  |
| 7 | REAE_NUM_BLOCO | CHAR(1) | Y |  |  |
| 8 | REAE_NOM_FDADO | NUMBER(3) | Y |  |  |
| 9 | REAE_DSC_REGISTRO | VARCHAR2(255) | Y |  |  |
| 10 | REAE_USR | VARCHAR2(40) | Y |  |  |
| 11 | REAE_DAT_ATUA | DATE | Y |  |  |

**PK**: REAE_ID

**FKs**:
- LDAE_ID → PFI_LDAE(LDAE_ID)
- REAE_ID_PARENT → PFI_REAE(REAE_ID)

---

## PFI_RESU

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | RESU_ID | NUMBER(20) | N |  |  |
| 2 | VALI_ID | NUMBER(20) | Y |  |  |
| 3 | RESU_LINHA | NUMBER | Y |  |  |
| 4 | RESU_REGISTRO | VARCHAR2(4) | Y |  |  |
| 5 | RESU_CAMPO | VARCHAR2(30) | Y |  |  |
| 6 | RESU_MSG_ERRO | VARCHAR2(500) | Y |  |  |
| 7 | RESU_OBS | VARCHAR2(500) | Y |  |  |
| 8 | RESU_DIFERENCA | NUMBER | Y |  |  |
| 9 | RESU_TIPO | NUMBER(1) | Y |  |  |

**PK**: RESU_ID

---

## PFI_TMP_AGES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | AGEN_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 3 | FILI_COD | VARCHAR2(9) | N |  |  |

**PK**: AGEN_ID, EMPS_COD, FILI_COD

---

## PFI_UCAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UTAB_EMP | VARCHAR2(9) | N |  |  |
| 2 | UTAB_FIL | VARCHAR2(9) | N |  |  |
| 3 | STAB_COD | VARCHAR2(30) | N |  |  |
| 4 | UTAB_TIP_PROCESSO | CHAR(1) | N |  |  |
| 5 | UTAB_NUM_PROCESSO | NUMBER(2) | N |  |  |
| 6 | SCAM_COD | VARCHAR2(30) | N |  |  |
| 7 | UCAM_TIP_CAMPO | CHAR(2) | Y |  |  |
| 8 | UCAM_POS_INI | NUMBER(5) | Y |  |  |
| 9 | UCAM_NUM_TAM | NUMBER(5) | Y |  |  |
| 10 | UCAM_TIP_LAYOUT | VARCHAR2(30) | Y |  |  |
| 11 | UCAM_TIP_VALOR | CHAR(3) | Y |  |  |
| 12 | UCAM_IND_VALIDAR | CHAR(1) | Y |  |  |
| 13 | UCAM_USR | VARCHAR2(40) | Y |  |  |
| 14 | UCAM_DAT_ATUA | DATE | Y |  |  |
| 15 | UCAM_DSC_FIXO | VARCHAR2(255) | Y |  |  |

**PK**: UTAB_EMP, UTAB_FIL, STAB_COD, UTAB_TIP_PROCESSO, UTAB_NUM_PROCESSO, SCAM_COD

**FKs**:
- UTAB_EMP, UTAB_FIL, STAB_COD, UTAB_TIP_PROCESSO, UTAB_NUM_PROCESSO → PFI_UTAB(UTAB_EMP, UTAB_FIL, STAB_COD, UTAB_TIP_PROCESSO, UTAB_NUM_PROCESSO)

---

## PFI_UTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UTAB_EMP | VARCHAR2(9) | N |  |  |
| 2 | UTAB_FIL | VARCHAR2(9) | N |  |  |
| 3 | STAB_COD | VARCHAR2(30) | N |  |  |
| 4 | UTAB_TIP_PROCESSO | CHAR(1) | N |  |  |
| 5 | UTAB_NUM_PROCESSO | NUMBER(2) | N |  |  |
| 6 | UTAB_DSC_PROCESSO | VARCHAR2(20) | Y |  |  |
| 7 | UTAB_TIP_ARQUIVO | CHAR(3) | Y |  |  |
| 8 | UTAB_TIP_FORMATO | CHAR(1) | Y |  |  |
| 9 | UTAB_DSC_DELIMITA | CHAR(1) | Y |  |  |
| 10 | UTAB_NUM_INICIO | NUMBER(3) | Y |  |  |
| 11 | UTAB_IND_ATUALIZA | CHAR(1) | Y |  |  |
| 12 | UTAB_USR | VARCHAR2(40) | Y |  |  |
| 13 | UTAB_DAT_ATUA | DATE | Y |  |  |
| 14 | UTAB_NOM_ARQUIVO | VARCHAR2(255) | Y |  |  |

**PK**: UTAB_EMP, UTAB_FIL, STAB_COD, UTAB_TIP_PROCESSO, UTAB_NUM_PROCESSO

---

## PFI_VALI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALI_ID | NUMBER(20) | N |  |  |
| 2 | EXEC_ID | NUMBER(20) | Y |  |  |
| 3 | VALI_STATUS | NUMBER(2) | Y |  |  |
| 4 | VALI_QTD_LIN_B0 | NUMBER(7) | Y |  |  |
| 5 | VALI_QTD_ERRO_B0 | NUMBER(7) | Y |  |  |
| 6 | VALI_QTD_LIN_B5 | NUMBER(7) | Y |  |  |
| 7 | VALI_QTD_ERRO_B5 | NUMBER(7) | Y |  |  |
| 8 | VALI_QTD_LIN_B9 | NUMBER(7) | Y |  |  |
| 9 | VALI_QTD_ERRO_B9 | NUMBER(7) | Y |  |  |
| 10 | VALI_TIPO | NUMBER(1) | Y |  |  |
| 11 | EXCO_ID | NUMBER(20) | Y |  |  |
| 12 | VALI_MES_ANO_EXCO | VARCHAR2(6) | Y |  |  |

**PK**: VALI_ID

---

## PFI_VALI_CONF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | VALI_CONF_QTD_ERRO | NUMBER(5) | Y |  |  |
| 4 | VALI_CONF_DESVIO | NUMBER | Y |  |  |

**PK**: EMPS_COD, FILI_COD

---

## PFI_VSBD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VSBD_VERSAO | VARCHAR2(20) | N |  |  |
| 2 | VSBD_DATA_ATUA | DATE | N |  |  |

**PK**: VSBD_VERSAO, VSBD_DATA_ATUA

---

