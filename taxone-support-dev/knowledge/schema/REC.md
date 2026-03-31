# Módulo: REC (REC) - 28 tabelas

## REC_CIEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | INFEM_DTEMIS | DATE | Y |  |  |
| 7 | INFEM_SERIE | VARCHAR2(5) | Y |  |  |
| 8 | INFEM_NUM | VARCHAR2(15) | Y |  |  |
| 9 | INFEM_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 10 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 11 | CATG_COD | CHAR(2) | Y |  |  |
| 12 | CIEM_BAS_PISCOF | NUMBER | Y |  |  |
| 13 | CIEM_ALIQ_PIS | NUMBER | Y |  |  |
| 14 | CIEM_CRED_PIS | NUMBER | Y |  |  |
| 15 | CIEM_ALIQ_COF | NUMBER | Y |  |  |
| 16 | CIEM_CRED_COF | NUMBER | Y |  |  |
| 17 | CCTR_COD | VARCHAR2(20) | Y |  |  |
| 18 | TPIS_COD | CHAR(2) | Y |  |  |
| 19 | TCOF_COD | CHAR(2) | Y |  |  |
| 20 | CIEM_QTD_BC | NUMBER | Y |  |  |
| 21 | INFEM_DTENTR | DATE | Y |  |  |
| 22 | VAR01 | VARCHAR2(150) | Y |  |  |
| 23 | VAR02 | VARCHAR2(150) | Y |  |  |
| 24 | VAR03 | VARCHAR2(150) | Y |  |  |
| 25 | VAR04 | VARCHAR2(150) | Y |  |  |
| 26 | VAR05 | VARCHAR2(150) | Y |  |  |
| 27 | NUM01 | NUMBER | Y |  |  |
| 28 | NUM02 | NUMBER | Y |  |  |
| 29 | NUM03 | NUMBER | Y |  |  |
| 30 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 31 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_CLASSFISCALPROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | CNBM_COD | VARCHAR2(10) | N |  |  |
| 5 | CNBM_DAT_ATUA | DATE | N |  |  |
| 6 | CNBM_DSC | VARCHAR2(500) | Y |  |  |
| 7 | CNBM_ALIQ_IPI | NUMBER | Y |  |  |
| 8 | CNBM_APURA_IPI | CHAR(1) | Y |  |  |
| 9 | CNBM_PRAZ_RECOLH | CHAR(1) | Y |  |  |
| 10 | CNBM_IND_TRIB | CHAR(1) | Y |  |  |
| 11 | GTIP_GRUPO | CHAR(4) | Y |  |  |
| 12 | STIP_GRUPO | VARCHAR2(6) | Y |  |  |
| 13 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 14 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_CLIFOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 5 | CADG_DAT_ATUA | DATE | Y |  |  |
| 6 | CATG_COD | CHAR(2) | Y |  |  |
| 7 | PAIS_COD | CHAR(3) | Y |  |  |
| 8 | UNFE_SIG | CHAR(2) | Y |  |  |
| 9 | CADG_COD_CGCCPF | VARCHAR2(16) | Y |  |  |
| 10 | CADG_TIP | CHAR(1) | Y |  |  |
| 11 | CADG_COD_INSEST | VARCHAR2(14) | Y |  |  |
| 12 | CADG_COD_INSMUN | VARCHAR2(14) | Y |  |  |
| 13 | EQUIPAR_RURAL | CHAR(1) | Y |  |  |
| 14 | CADG_NOM | VARCHAR2(70) | Y |  |  |
| 15 | CADG_NOM_FANTASIA | VARCHAR2(70) | Y |  |  |
| 16 | CADG_END | VARCHAR2(70) | Y |  |  |
| 17 | CADG_END_NUM | NUMBER(12) | Y |  |  |
| 18 | CADG_END_COMP | VARCHAR2(45) | Y |  |  |
| 19 | CADG_END_BAIRRO | VARCHAR2(60) | Y |  |  |
| 20 | CADG_END_MUNIC | VARCHAR2(50) | Y |  |  |
| 21 | CADG_END_CEP | CHAR(8) | Y |  |  |
| 22 | CADG_IND_COLIGADA | CHAR(1) | Y |  |  |
| 23 | CADG_COD_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 24 | TP_LOC | CHAR(2) | Y |  |  |
| 25 | LOCA_COD | VARCHAR2(10) | Y |  |  |
| 26 | CADG_CEI | VARCHAR2(12) | Y |  |  |
| 27 | NUM01 | NUMBER | Y |  |  |
| 28 | NUM02 | NUMBER | Y |  |  |
| 29 | NUM03 | NUMBER | Y |  |  |
| 30 | VAR01 | VARCHAR2(150) | Y |  |  |
| 31 | VAR02 | VARCHAR2(150) | Y |  |  |
| 32 | VAR03 | VARCHAR2(150) | Y |  |  |
| 33 | VAR04 | VARCHAR2(150) | Y |  |  |
| 34 | VAR05 | VARCHAR2(150) | Y |  |  |
| 35 | CADG_NIT | VARCHAR2(11) | Y |  |  |
| 36 | CADG_CX_POST | VARCHAR2(12) | Y |  |  |
| 37 | CADG_CEP_CXP | CHAR(8) | Y |  |  |
| 38 | CADG_DDD_TEL | CHAR(4) | Y |  |  |
| 39 | CADG_TEL | VARCHAR2(8) | Y |  |  |
| 40 | CADG_DDD_FAX | CHAR(4) | Y |  |  |
| 41 | CADG_FAX | VARCHAR2(8) | Y |  |  |
| 42 | CADG_CLAS_RI | CHAR(2) | Y |  |  |
| 43 | MIBGE_COD_MUN | VARCHAR2(7) | Y |  |  |
| 44 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 45 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_COD_FIS_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 5 | CFOP_UF | CHAR(2) | Y |  |  |
| 6 | CFOP_DAT_ATUA | DATE | Y |  |  |
| 7 | CFOP_DSC | VARCHAR2(150) | Y |  |  |
| 8 | CFOP_IND_CONTR | CHAR(1) | Y |  |  |
| 9 | NUM01 | NUMBER | Y |  |  |
| 10 | NUM02 | NUMBER | Y |  |  |
| 11 | NUM03 | NUMBER | Y |  |  |
| 12 | VAR01 | VARCHAR2(150) | Y |  |  |
| 13 | VAR02 | VARCHAR2(150) | Y |  |  |
| 14 | VAR03 | VARCHAR2(150) | Y |  |  |
| 15 | VAR04 | VARCHAR2(150) | Y |  |  |
| 16 | VAR05 | VARCHAR2(150) | Y |  |  |
| 17 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 18 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_CTEX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | INFSM_SERIE | VARCHAR2(5) | Y |  |  |
| 7 | INFSM_NUM | VARCHAR2(15) | Y |  |  |
| 8 | INFSM_DTEMISS | DATE | Y |  |  |
| 9 | TAEX_COD_RE | VARCHAR2(15) | Y |  |  |
| 10 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 11 | CTEX_NF_REM | VARCHAR2(15) | Y |  |  |
| 12 | CTEX_SERIE_REM | VARCHAR2(5) | Y |  |  |
| 13 | CTEX_DTEMISS_REM | DATE | Y |  |  |
| 14 | CATG_COD | CHAR(2) | Y |  |  |
| 15 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 16 | MOD_COD | CHAR(3) | Y |  |  |
| 17 | CTEX_QTD_EXP | NUMBER | Y |  |  |
| 18 | CTEX_VAL_UNIT | NUMBER | Y |  |  |
| 19 | CTEX_TOT_EXP | NUMBER | Y |  |  |
| 20 | CTEX_NR_MEMO | VARCHAR2(20) | Y |  |  |
| 21 | CTEX_CHV_NFE | VARCHAR2(44) | Y |  |  |
| 22 | UNID_COD | CHAR(3) | Y |  |  |
| 23 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 24 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_CTRESTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | LSTQ_NUM | VARCHAR2(15) | Y |  |  |
| 7 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 8 | LSTQ_DAT | DATE | Y |  |  |
| 9 | TDOC_COD | CHAR(5) | Y |  |  |
| 10 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 11 | NSTQ_COD | VARCHAR2(5) | Y |  |  |
| 12 | LSTQ_QTD | NUMBER | Y |  |  |
| 13 | LSTQ_NUM_ARQ | VARCHAR2(40) | Y |  |  |
| 14 | INFEM_NUM | VARCHAR2(15) | Y |  |  |
| 15 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 16 | CCUS_COD | VARCHAR2(28) | Y |  |  |
| 17 | PCON_COD_CONTA | VARCHAR2(70) | Y |  |  |
| 18 | PCON_COD_CPART | VARCHAR2(70) | Y |  |  |
| 19 | LOCA_COD | CHAR(3) | Y |  |  |
| 20 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 21 | CATG_COD | CHAR(2) | Y |  |  |
| 22 | VAL_IPI | NUMBER | Y |  |  |
| 23 | LSTQ_VAL_UNIT | NUMBER | Y |  |  |
| 24 | LSTQ_VAL_TOT | NUMBER | Y |  |  |
| 25 | LSTQ_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 26 | LSTQ_VAL_CUSTTOT | NUMBER | Y |  |  |
| 27 | LSTQ_NUM_CSERV | VARCHAR2(14) | Y |  |  |
| 28 | LSTQ_NUM_SERIE | VARCHAR2(12) | Y |  |  |
| 29 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 30 | LSTQ_SERIE | VARCHAR2(5) | Y |  |  |
| 31 | LRE_LRS | NUMBER(6) | Y |  |  |
| 32 | OBS | VARCHAR2(150) | Y |  |  |
| 33 | LSTQ_NUM_LOTE | VARCHAR2(10) | Y |  |  |
| 34 | LSTQ_DIV | CHAR(4) | Y |  |  |
| 35 | LSTQ_DOC_EST | VARCHAR2(10) | Y |  |  |
| 36 | LSTQ_ITEM_EST | CHAR(4) | Y |  |  |
| 37 | LSTQ_ANO_DOC | CHAR(4) | Y |  |  |
| 38 | NUM01 | NUMBER | Y |  |  |
| 39 | NUM02 | NUMBER | Y |  |  |
| 40 | NUM03 | NUMBER | Y |  |  |
| 41 | VAR01 | VARCHAR2(150) | Y |  |  |
| 42 | VAR02 | VARCHAR2(150) | Y |  |  |
| 43 | VAR03 | VARCHAR2(150) | Y |  |  |
| 44 | VAR04 | VARCHAR2(150) | Y |  |  |
| 45 | VAR05 | VARCHAR2(150) | Y |  |  |
| 46 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 47 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_DFME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | MNFEM_SERIE | VARCHAR2(5) | Y |  |  |
| 7 | MNFEM_NUM | VARCHAR2(15) | Y |  |  |
| 8 | MNFEM_DTEMIS | DATE | Y |  |  |
| 9 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 10 | CATG_COD | CHAR(2) | Y |  |  |
| 11 | CICD_COD_INF | VARCHAR2(9) | Y |  |  |
| 12 | DFME_CADG_COD | VARCHAR2(16) | Y |  |  |
| 13 | DFME_CATG_COD | CHAR(2) | Y |  |  |
| 14 | DFME_SERIE | VARCHAR2(5) | Y |  |  |
| 15 | DFME_NUM_DOC | VARCHAR2(15) | Y |  |  |
| 16 | DFME_DT_DOC | DATE | Y |  |  |
| 17 | MNFEM_DTENTR | DATE | Y |  |  |
| 18 | DFME_IND_EMIT | CHAR(1) | Y |  |  |
| 19 | MDOC_COD | CHAR(3) | Y |  |  |
| 20 | DFME_DT_REF | DATE | Y |  |  |
| 21 | DFME_TP_OPE | CHAR(1) | Y |  |  |
| 22 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 23 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_FILIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | FILI_COD_CGC | VARCHAR2(16) | Y |  |  |
| 7 | UNFE_SIG | CHAR(2) | Y |  |  |
| 8 | FILI_COD_INSEST | VARCHAR2(14) | Y |  |  |
| 9 | FILI_COD_INSMUN | VARCHAR2(14) | Y |  |  |
| 10 | FILI_COD_ATIVECON | VARCHAR2(15) | Y |  |  |
| 11 | FILI_NOM | VARCHAR2(115) | Y |  |  |
| 12 | FILI_NOM_FANTASIA | VARCHAR2(70) | Y |  |  |
| 13 | FILI_END | VARCHAR2(70) | Y |  |  |
| 14 | FILI_END_NUM | NUMBER(12) | Y |  |  |
| 15 | FILI_END_COMP | VARCHAR2(45) | Y |  |  |
| 16 | FILI_END_BAIRRO | VARCHAR2(20) | Y |  |  |
| 17 | FILI_END_MUNIC | VARCHAR2(50) | Y |  |  |
| 18 | FILI_END_CEP | CHAR(8) | Y |  |  |
| 19 | FILI_COD_LOCAL | VARCHAR2(10) | Y |  |  |
| 20 | FILI_FAX | VARCHAR2(17) | Y |  |  |
| 21 | FILI_TEL | VARCHAR2(17) | Y |  |  |
| 22 | TP_LOC | CHAR(2) | Y |  |  |
| 23 | FILI_SETOR | CHAR(2) | Y |  |  |
| 24 | FILI_AUTOR | VARCHAR2(9) | Y |  |  |
| 25 | FILI_SANITARIA | VARCHAR2(50) | Y |  |  |
| 26 | FILI_LICEN | VARCHAR2(20) | Y |  |  |
| 27 | FILI_ESPEC | VARCHAR2(10) | Y |  |  |
| 28 | FILI_IND_RET_ISS | CHAR(1) | Y |  |  |
| 29 | FILI_COD_INSCEN | VARCHAR2(14) | Y |  |  |
| 30 | FILI_EMAIL | VARCHAR2(40) | Y |  |  |
| 31 | FILI_NAT_JUR | NUMBER(4) | Y |  |  |
| 32 | NUM01 | NUMBER | Y |  |  |
| 33 | NUM02 | NUMBER | Y |  |  |
| 34 | NUM03 | NUMBER | Y |  |  |
| 35 | VAR01 | VARCHAR2(150) | Y |  |  |
| 36 | VAR02 | VARCHAR2(150) | Y |  |  |
| 37 | VAR03 | VARCHAR2(150) | Y |  |  |
| 38 | VAR04 | VARCHAR2(150) | Y |  |  |
| 39 | VAR05 | VARCHAR2(150) | Y |  |  |
| 40 | FILI_CEI | VARCHAR2(12) | Y |  |  |
| 41 | FILI_NIT | VARCHAR2(11) | Y |  |  |
| 42 | FILI_SUFRAMA | VARCHAR2(9) | Y |  |  |
| 43 | FILI_MUN_IBGE | VARCHAR2(7) | Y |  |  |
| 44 | TPLD_COD | CHAR(2) | Y |  |  |
| 45 | FILI_NIRE | VARCHAR2(45) | Y |  |  |
| 46 | FILI_MATRIZ | CHAR(1) | Y |  |  |
| 47 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 48 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_GTIP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | GTIP_GRUPO | CHAR(4) | Y |  |  |
| 5 | GTIP_DESC1 | VARCHAR2(500) | Y |  |  |
| 6 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 7 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_IMPORTACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | MNFEM_SERIE | VARCHAR2(5) | Y |  |  |
| 7 | MNFEM_NUM | VARCHAR2(15) | Y |  |  |
| 8 | MNFEM_DTEMIS | DATE | Y |  |  |
| 9 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 10 | CATG_COD | CHAR(2) | Y |  |  |
| 11 | SEQ | NUMBER(2) | Y |  |  |
| 12 | MDOC_COD | CHAR(3) | Y |  |  |
| 13 | DATA_ENTR | DATE | Y |  |  |
| 14 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 15 | DATA_DES | DATE | Y |  |  |
| 16 | VAL_IMP | NUMBER | Y |  |  |
| 17 | TARE | VARCHAR2(60) | Y |  |  |
| 18 | NUM01 | NUMBER | Y |  |  |
| 19 | NUM02 | NUMBER | Y |  |  |
| 20 | NUM03 | NUMBER | Y |  |  |
| 21 | VAR01 | VARCHAR2(150) | Y |  |  |
| 22 | VAR02 | VARCHAR2(150) | Y |  |  |
| 23 | VAR03 | VARCHAR2(150) | Y |  |  |
| 24 | VAR04 | VARCHAR2(150) | Y |  |  |
| 25 | VAR05 | VARCHAR2(150) | Y |  |  |
| 26 | IMP_COD_DOC_IMP | CHAR(1) | Y |  |  |
| 27 | IMP_PIS | NUMBER | Y |  |  |
| 28 | IMP_COFINS | NUMBER | Y |  |  |
| 29 | NUM_ACDRAW | VARCHAR2(20) | Y |  |  |
| 30 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 31 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_INDU

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | INFEM_SERIE | VARCHAR2(5) | Y |  |  |
| 7 | INFEM_NUM | VARCHAR2(15) | Y |  |  |
| 8 | INFEM_DTENTR | DATE | N |  |  |
| 9 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 10 | CATG_COD | CHAR(2) | Y |  |  |
| 11 | INFEM_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 12 | INDU_SERIE | VARCHAR2(5) | Y |  |  |
| 13 | INDU_NUM | VARCHAR2(15) | Y |  |  |
| 14 | NDU_DTEMIS | DATE | Y |  |  |
| 15 | INDU_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | INDU_CADG_COD | VARCHAR2(16) | Y |  |  |
| 17 | INDU_CATG_COD | CHAR(2) | Y |  |  |
| 18 | INDU_QTD_INS_UNI | NUMBER | Y |  |  |
| 19 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 20 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_INVC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | INVE_DAT | DATE | Y |  |  |
| 7 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 8 | INVC_QTD | NUMBER | Y |  |  |
| 9 | INVC_QTD_ENTRADA | NUMBER | Y |  |  |
| 10 | INVC_QTD_SAIDA | NUMBER | Y |  |  |
| 11 | UNID_COD | CHAR(3) | Y |  |  |
| 12 | INVC_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 13 | INVC_VAL_CUSTTOT | NUMBER | Y |  |  |
| 14 | INVC_VAL_CUSTICMS | NUMBER | Y |  |  |
| 15 | INVC_VAL_CUSTFR | NUMBER | Y |  |  |
| 16 | INVC_VAL_CUSTFRIC | NUMBER | Y |  |  |
| 17 | INVC_VAL_CUSTMES | NUMBER | Y |  |  |
| 18 | INVC_VAL_ICMSMES | NUMBER | Y |  |  |
| 19 | INVC_VAL_CUSTOTMES | NUMBER | Y |  |  |
| 20 | INVC_VAL_ICMTOTMES | NUMBER | Y |  |  |
| 21 | INVC_VAL_CUSTTER | NUMBER | Y |  |  |
| 22 | INVC_VAL_ICMSTER | NUMBER | Y |  |  |
| 23 | INVC_QTD_FC3A | NUMBER | Y |  |  |
| 24 | INVC_QTD_FC3B | NUMBER | Y |  |  |
| 25 | INVC_QTD_FC3C | NUMBER | Y |  |  |
| 26 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 27 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_INVENTARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 7 | LOCA_COD | CHAR(3) | Y |  |  |
| 8 | INVE_DAT | DATE | Y |  |  |
| 9 | NSTQ_COD | VARCHAR2(5) | Y |  |  |
| 10 | CNBM_COD | VARCHAR2(10) | Y |  |  |
| 11 | INVE_QTD | NUMBER | Y |  |  |
| 12 | INVE_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 13 | INVE_VAL_CUSTTOT | NUMBER | Y |  |  |
| 14 | CCUS_COD | VARCHAR2(28) | Y |  |  |
| 15 | PCON_COD_CONTA | VARCHAR2(70) | Y |  |  |
| 16 | UNID_COD | CHAR(3) | Y |  |  |
| 17 | OBS | VARCHAR2(150) | Y |  |  |
| 18 | INVE_DIV | CHAR(4) | Y |  |  |
| 19 | NUM01 | NUMBER | Y |  |  |
| 20 | NUM02 | NUMBER | Y |  |  |
| 21 | NUM03 | NUMBER | Y |  |  |
| 22 | VAR01 | VARCHAR2(150) | Y |  |  |
| 23 | VAR02 | VARCHAR2(150) | Y |  |  |
| 24 | VAR03 | VARCHAR2(150) | Y |  |  |
| 25 | VAR04 | VARCHAR2(150) | Y |  |  |
| 26 | VAR05 | VARCHAR2(150) | Y |  |  |
| 27 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 28 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_ITMERCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | CGC_CPF | VARCHAR2(16) | Y |  |  |
| 7 | IE | VARCHAR2(14) | Y |  |  |
| 8 | UF | CHAR(2) | Y |  |  |
| 9 | TP_LOC | CHAR(2) | Y |  |  |
| 10 | LOCALIDADE | VARCHAR2(10) | Y |  |  |
| 11 | MOD_DOC | CHAR(3) | Y |  |  |
| 12 | TDOC_COD | CHAR(5) | Y |  |  |
| 13 | IND_CANC | CHAR(1) | Y |  |  |
| 14 | IND_SIT | CHAR(1) | Y |  |  |
| 15 | IND_TRIB_SUBSTRIB | CHAR(1) | Y |  |  |
| 16 | VAL_ISEN_SUBSTRIB | NUMBER | Y |  |  |
| 17 | VAL_OUTR_SUBSTRIB | NUMBER | Y |  |  |
| 18 | INFEM_SERIE | VARCHAR2(5) | Y |  |  |
| 19 | INFEM_NUM | VARCHAR2(15) | Y |  |  |
| 20 | INFEM_DTEMIS | DATE | Y |  |  |
| 21 | INFEM_DTENTR | DATE | Y |  |  |
| 22 | CATG_COD | CHAR(2) | Y |  |  |
| 23 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 24 | INFEM_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 25 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 26 | UNID_COD_VENDA | CHAR(3) | Y |  |  |
| 27 | INFEM_DSC | VARCHAR2(150) | Y |  |  |
| 28 | CCUS_COD | VARCHAR2(28) | Y |  |  |
| 29 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 30 | CNBM_COD | VARCHAR2(10) | Y |  |  |
| 31 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 32 | UNID_COD_PADRAO | CHAR(3) | Y |  |  |
| 33 | INFEM_QTD | NUMBER | Y |  |  |
| 34 | INFEM_PES_LIQ | NUMBER | Y |  |  |
| 35 | INFEM_VAL_PRECOUNIT | NUMBER | Y |  |  |
| 36 | INFEM_VAL_PRECOTOT | NUMBER | Y |  |  |
| 37 | INFEM_VAL_DESC | NUMBER | Y |  |  |
| 38 | INFEM_NUM_ROMA | VARCHAR2(12) | Y |  |  |
| 39 | INFEM_DAT_ROMA | DATE | Y |  |  |
| 40 | INFEM_VAL_FRETE | NUMBER | Y |  |  |
| 41 | INFEM_VAL_SEGUR | NUMBER | Y |  |  |
| 42 | INFEM_VAL_DESP | NUMBER | Y |  |  |
| 43 | FEDE_COD | VARCHAR2(5) | Y |  |  |
| 44 | INFEM_TRIBIPI | CHAR(1) | Y |  |  |
| 45 | INFEM_ALIQ_IPI | NUMBER | Y |  |  |
| 46 | INFEM_BAS_IPI | NUMBER | Y |  |  |
| 47 | INFEM_VAL_IPI | NUMBER | Y |  |  |
| 48 | ESTA_COD | CHAR(1) | Y |  |  |
| 49 | ESTB_COD | CHAR(2) | Y |  |  |
| 50 | INFEM_TRIBICM | CHAR(1) | Y |  |  |
| 51 | INFEM_ALIQ_ICMS | NUMBER | Y |  |  |
| 52 | INFEM_BAS_ICMS | NUMBER | Y |  |  |
| 53 | INFEM_VAL_ICMS | NUMBER | Y |  |  |
| 54 | INFEM_BASSUBST_ICMS | NUMBER | Y |  |  |
| 55 | INFEM_VALSUBST_ICMS | NUMBER | Y |  |  |
| 56 | INFEM_VAL_REDICMS | NUMBER | Y |  |  |
| 57 | INFEM_ALIQ_DIFICMS | NUMBER | Y |  |  |
| 58 | INFEM_ISENTA_IPI | NUMBER | Y |  |  |
| 59 | INFEM_ISENTA_ICMS | NUMBER | Y |  |  |
| 60 | INFEM_OUTRA_IPI | NUMBER | Y |  |  |
| 61 | INFEM_OUTRA_ICMS | NUMBER | Y |  |  |
| 62 | INFEM_VAL_CONT | NUMBER | Y |  |  |
| 63 | INFEM_COD_CONT | VARCHAR2(28) | Y |  |  |
| 64 | INFEM_RURAL | CHAR(1) | Y |  |  |
| 65 | INFEM_PETROLEO | CHAR(1) | Y |  |  |
| 66 | INFEM_CHASSI | VARCHAR2(22) | Y |  |  |
| 67 | INFEM_IND_MOV | CHAR(1) | Y |  |  |
| 68 | INFEM_VAL_REDIPI | NUMBER | Y |  |  |
| 69 | NUM01 | NUMBER | Y |  |  |
| 70 | NUM02 | NUMBER | Y |  |  |
| 71 | NUM03 | NUMBER | Y |  |  |
| 72 | VAR01 | VARCHAR2(150) | Y |  |  |
| 73 | VAR02 | VARCHAR2(150) | Y |  |  |
| 74 | VAR03 | VARCHAR2(150) | Y |  |  |
| 75 | VAR04 | VARCHAR2(150) | Y |  |  |
| 76 | VAR05 | VARCHAR2(150) | Y |  |  |
| 77 | UNIN_COD | VARCHAR2(9) | Y |  |  |
| 78 | TIPI_COD | CHAR(2) | Y |  |  |
| 79 | LIPI_COD | CHAR(3) | Y |  |  |
| 80 | INFEM_ALIQ_ST | NUMBER | Y |  |  |
| 81 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 82 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_ITMERCS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | CGC_CPF | VARCHAR2(16) | Y |  |  |
| 7 | IE | VARCHAR2(14) | Y |  |  |
| 8 | UF | CHAR(2) | Y |  |  |
| 9 | TP_LOC | CHAR(2) | Y |  |  |
| 10 | LOCALIDADE | VARCHAR2(10) | Y |  |  |
| 11 | MOD_DOC | CHAR(3) | Y |  |  |
| 12 | TDOC_COD | CHAR(5) | Y |  |  |
| 13 | IND_CANC | CHAR(1) | Y |  |  |
| 14 | IND_SIT | CHAR(1) | Y |  |  |
| 15 | IND_TRIB_SUBSTRIB | CHAR(1) | Y |  |  |
| 16 | VAL_ISEN_SUBSTRIB | NUMBER | Y |  |  |
| 17 | VAL_OUTR_SUBSTRIB | NUMBER | Y |  |  |
| 18 | INFSM_SERIE | VARCHAR2(5) | Y |  |  |
| 19 | INFSM_NUM | VARCHAR2(15) | Y |  |  |
| 20 | INFSM_DTEMISS | DATE | Y |  |  |
| 21 | CATG_COD | CHAR(2) | Y |  |  |
| 22 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 23 | INFSM_NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 24 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 25 | UNID_COD_VENDA | CHAR(3) | Y |  |  |
| 26 | INFSM_DSC | VARCHAR2(150) | Y |  |  |
| 27 | CCUS_COD | VARCHAR2(28) | Y |  |  |
| 28 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 29 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 30 | CNBM_COD | VARCHAR2(10) | Y |  |  |
| 31 | UNID_COD | CHAR(3) | Y |  |  |
| 32 | INFSM_QTD | NUMBER | Y |  |  |
| 33 | INFSM_PES_LIQ | NUMBER | Y |  |  |
| 34 | INFSM_VAL_PRECOUNIT | NUMBER | Y |  |  |
| 35 | INFSM_VAL_PRECOTOT | NUMBER | Y |  |  |
| 36 | INFSM_VAL_DESC | NUMBER | Y |  |  |
| 37 | INFSM_NUM_ROMA | VARCHAR2(12) | Y |  |  |
| 38 | INFSM_DAT_ROMA | DATE | Y |  |  |
| 39 | INFSM_VAL_FRETE | NUMBER | Y |  |  |
| 40 | INFSM_VAL_SEGUR | NUMBER | Y |  |  |
| 41 | INFSM_VAL_DESP | NUMBER | Y |  |  |
| 42 | FEDE_COD | VARCHAR2(5) | Y |  |  |
| 43 | INFSM_TRIBIPI | CHAR(1) | Y |  |  |
| 44 | INFSM_ALIQ_IPI | NUMBER | Y |  |  |
| 45 | INFSM_BAS_IPI | NUMBER | Y |  |  |
| 46 | INFSM_VAL_IPI | NUMBER | Y |  |  |
| 47 | ESTA_COD | CHAR(1) | Y |  |  |
| 48 | ESTB_COD | CHAR(2) | Y |  |  |
| 49 | INFSM_TRIBICM | CHAR(1) | Y |  |  |
| 50 | INFSM_ALIQ_ICMS | NUMBER | Y |  |  |
| 51 | INFSM_BAS_ICMS | NUMBER | Y |  |  |
| 52 | INFSM_VAL_ICMS | NUMBER | Y |  |  |
| 53 | INFSM_BASSUBST_ICMS | NUMBER | Y |  |  |
| 54 | INFSM_VALSUBST_ICMS | NUMBER | Y |  |  |
| 55 | INFSM_VAL_REDICMS | NUMBER | Y |  |  |
| 56 | INFSM_ALIQ_DIFICMS | NUMBER | Y |  |  |
| 57 | INFSM_ISENTA_IPI | NUMBER | Y |  |  |
| 58 | INFSM_ISENTA_ICMS | NUMBER | Y |  |  |
| 59 | INFSM_OUTRA_IPI | NUMBER | Y |  |  |
| 60 | INFSM_OUTRA_ICMS | NUMBER | Y |  |  |
| 61 | INFSM_VAL_CONT | NUMBER | Y |  |  |
| 62 | INFSM_COD_CONT | VARCHAR2(28) | Y |  |  |
| 63 | INFSM_ICMS_FRETE | NUMBER | Y |  |  |
| 64 | INFSM_CHASSI | VARCHAR2(22) | Y |  |  |
| 65 | INFSM_IND_MOV | CHAR(1) | Y |  |  |
| 66 | INFSM_VAL_REDIPI | NUMBER | Y |  |  |
| 67 | NUM01 | NUMBER | Y |  |  |
| 68 | NUM02 | NUMBER | Y |  |  |
| 69 | NUM03 | NUMBER | Y |  |  |
| 70 | VAR01 | VARCHAR2(150) | Y |  |  |
| 71 | VAR02 | VARCHAR2(150) | Y |  |  |
| 72 | VAR03 | VARCHAR2(150) | Y |  |  |
| 73 | VAR04 | VARCHAR2(150) | Y |  |  |
| 74 | VAR05 | VARCHAR2(150) | Y |  |  |
| 75 | UNIN_COD | VARCHAR2(9) | Y |  |  |
| 76 | TIPI_COD | CHAR(2) | Y |  |  |
| 77 | LIPI_COD | CHAR(3) | Y |  |  |
| 78 | INFSM_ALIQ_ST | NUMBER | Y |  |  |
| 79 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 80 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_LESC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | LSTQ_NUM | VARCHAR2(15) | Y |  |  |
| 7 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 8 | LSTQ_DAT | DATE | Y |  |  |
| 9 | TDOC_COD | CHAR(3) | Y |  |  |
| 10 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 11 | NSTQ_COD | VARCHAR2(5) | Y |  |  |
| 12 | LSTQ_QTD | NUMBER | Y |  |  |
| 13 | LSTQ_NUM_ARQ | VARCHAR2(40) | Y |  |  |
| 14 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 15 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 16 | LESC_NUM_ORDEM | VARCHAR2(40) | Y |  |  |
| 17 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 18 | LESC_COD_NIVEL | NUMBER(3) | Y |  |  |
| 19 | LESC_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 20 | LESC_VAL_CUSTICMS | NUMBER | Y |  |  |
| 21 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 22 | LESC_QTD_INS_UNI | NUMBER | Y |  |  |
| 23 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 24 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_MATERIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 7 | MATE_DAT_ATUA | DATE | Y |  |  |
| 8 | CMAT_COD | CHAR(1) | Y |  |  |
| 9 | CNBM_COD | VARCHAR2(10) | Y |  |  |
| 10 | UNID_COD | CHAR(3) | Y |  |  |
| 11 | MATE_DSC | VARCHAR2(150) | Y |  |  |
| 12 | IND_PETROLEO | CHAR(1) | Y |  |  |
| 13 | IND_EST | CHAR(1) | Y |  |  |
| 14 | IND_INV | CHAR(1) | Y |  |  |
| 15 | EAN1 | VARCHAR2(14) | Y |  |  |
| 16 | EAN2 | VARCHAR2(14) | Y |  |  |
| 17 | EAN3 | VARCHAR2(14) | Y |  |  |
| 18 | EAN4 | VARCHAR2(14) | Y |  |  |
| 19 | EAN5 | VARCHAR2(14) | Y |  |  |
| 20 | NUMITEM | CHAR(2) | Y |  |  |
| 21 | PROD_SISIF | CHAR(1) | Y |  |  |
| 22 | DCB_COD | VARCHAR2(10) | Y |  |  |
| 23 | PORT_COD | VARCHAR2(10) | Y |  |  |
| 24 | CAT95P_COD | CHAR(4) | Y |  |  |
| 25 | IN359_COD | CHAR(3) | Y |  |  |
| 26 | IN63_COD_ESP | CHAR(2) | Y |  |  |
| 27 | NUM01 | NUMBER | Y |  |  |
| 28 | NUM02 | NUMBER | Y |  |  |
| 29 | NUM03 | NUMBER | Y |  |  |
| 30 | VAR01 | VARCHAR2(150) | Y |  |  |
| 31 | VAR02 | VARCHAR2(150) | Y |  |  |
| 32 | VAR03 | VARCHAR2(150) | Y |  |  |
| 33 | VAR04 | VARCHAR2(150) | Y |  |  |
| 34 | VAR05 | VARCHAR2(150) | Y |  |  |
| 35 | MATE_TIPO_ITEM | CHAR(2) | Y |  |  |
| 36 | MATE_ANT_ITEM | VARCHAR2(20) | Y |  |  |
| 37 | CEIP_COD | VARCHAR2(5) | Y |  |  |
| 38 | MATE_COD_SELO | VARCHAR2(6) | Y |  |  |
| 39 | MATE_QTD_SELO | NUMBER(5) | Y |  |  |
| 40 | CPAN_COD_ANP | VARCHAR2(9) | Y |  |  |
| 41 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 42 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_MIBGE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | MIBGE_COD_MUN | VARCHAR2(7) | Y |  |  |
| 5 | UNFE_SIG | CHAR(2) | Y |  |  |
| 6 | MIBGE_DESC_MUN | VARCHAR2(50) | Y |  |  |
| 7 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 8 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_MSMERCS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | TDOC_COD | CHAR(3) | Y |  |  |
| 7 | MNFSM_SERIE | VARCHAR2(5) | Y |  |  |
| 8 | MNFSM_NUM | VARCHAR2(15) | Y |  |  |
| 9 | MNFSM_DTEMISS | DATE | Y |  |  |
| 10 | CATG_COD | CHAR(2) | Y |  |  |
| 11 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 12 | MNFSM_IND_CONT | VARCHAR2(5) | Y |  |  |
| 13 | MDOC_COD | CHAR(3) | Y |  |  |
| 14 | MNFSM_DTSAIDA | VARCHAR2(10) | Y |  |  |
| 15 | MNFSM_VAL_TOTPROD | NUMBER | Y |  |  |
| 16 | MNFSM_VAL_TOTNF | NUMBER | Y |  |  |
| 17 | MNFSM_VAL_DESC | NUMBER | Y |  |  |
| 18 | MNFSM_NUMNFREF | VARCHAR2(15) | Y |  |  |
| 19 | MNFSM_SERIENFREF | VARCHAR2(5) | Y |  |  |
| 20 | MNFSM_VAL_REDIPI | NUMBER | Y |  |  |
| 21 | MNFSM_VAL_TOTIPI | NUMBER | Y |  |  |
| 22 | MNFSM_INSEST_SUBST | VARCHAR2(14) | Y |  |  |
| 23 | MNFSM_OBSIPI | VARCHAR2(150) | Y |  |  |
| 24 | MNFSM_IND_CONTR | CHAR(1) | Y |  |  |
| 25 | MNFSM_IND_CANC | CHAR(1) | Y |  |  |
| 26 | MNFSM_AVISTA | CHAR(1) | Y |  |  |
| 27 | CADG_COD_TRANSP | VARCHAR2(16) | Y |  |  |
| 28 | TRANS_VAL_FRETE | NUMBER | Y |  |  |
| 29 | TRANS_VAL_SEGUR | NUMBER | Y |  |  |
| 30 | MFRT_COD | CHAR(3) | Y |  |  |
| 31 | TRANS_PES_BRUTO | NUMBER | Y |  |  |
| 32 | TRANS_PES_LIQ | NUMBER | Y |  |  |
| 33 | VTRP_COD | CHAR(3) | Y |  |  |
| 34 | TRANS_QTD_VOL | NUMBER | Y |  |  |
| 35 | EVOL_COD | CHAR(3) | Y |  |  |
| 36 | TRANS_IDENT | VARCHAR2(17) | Y |  |  |
| 37 | NUM01 | NUMBER | Y |  |  |
| 38 | NUM02 | NUMBER | Y |  |  |
| 39 | NUM03 | NUMBER | Y |  |  |
| 40 | VAR01 | VARCHAR2(150) | Y |  |  |
| 41 | VAR02 | VARCHAR2(150) | Y |  |  |
| 42 | VAR03 | VARCHAR2(150) | Y |  |  |
| 43 | VAR04 | VARCHAR2(150) | Y |  |  |
| 44 | VAR05 | VARCHAR2(150) | Y |  |  |
| 45 | MNFSM_REG | CHAR(1) | Y |  |  |
| 46 | MNFSM_DEN_IN | CHAR(1) | Y |  |  |
| 47 | MNFSM_CHV_NFE | CHAR(44) | Y |  |  |
| 48 | MNFSM_VL_ABAT_NT | NUMBER | Y |  |  |
| 49 | MNFSM_VL_OUT_DA | NUMBER | Y |  |  |
| 50 | MNFSM_VL_BC_ICMS | NUMBER | Y |  |  |
| 51 | MNFSM_VL_ICMS | NUMBER | Y |  |  |
| 52 | MNFSM_BC_ICMS_ST | NUMBER | Y |  |  |
| 53 | MNFSM_VL_ICMS_ST | NUMBER | Y |  |  |
| 54 | MNFSM_VL_IPI | NUMBER | Y |  |  |
| 55 | MNFSM_VL_PIS | NUMBER | Y |  |  |
| 56 | MNFSM_VL_COFINS | NUMBER | Y |  |  |
| 57 | MNFSM_VL_PIS_ST | NUMBER | Y |  |  |
| 58 | MNFSM_COFINS_ST | NUMBER | Y |  |  |
| 59 | MNFSM_IND_COMPL | CHAR(1) | Y |  |  |
| 60 | UNFE_SIG_VEICULO | CHAR(2) | Y |  |  |
| 61 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 62 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_NATUREZA_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 5 | NOPE_DAT_ATUA | DATE | Y |  |  |
| 6 | NOPE_DSC | VARCHAR2(150) | Y |  |  |
| 7 | NOPE_EXCALC_CL | CHAR(1) | Y |  |  |
| 8 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 9 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_PAISES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | PAIS_COD | CHAR(3) | Y |  |  |
| 5 | PAIS_DESC | VARCHAR2(150) | Y |  |  |
| 6 | PAIS_COD_DIPJ | CHAR(3) | Y |  |  |
| 7 | PAIS_COD_BCB | VARCHAR2(5) | Y |  |  |
| 8 | PAIS_COD_GIARS | CHAR(3) | Y |  |  |
| 9 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 10 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_PFI_DEPR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | PROD_DAT_ATUA | DATE | Y |  |  |
| 7 | PROD_NUM_PROC | VARCHAR2(40) | Y |  |  |
| 8 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 9 | ITEM_COD | VARCHAR2(60) | Y |  |  |
| 10 | QTD_INS_UNI | NUMBER | Y |  |  |
| 11 | VAL_PER_GAN | NUMBER | Y |  |  |
| 12 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 13 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_PFI_ESPR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | PROD_DAT_ATUA | DATE | Y |  |  |
| 7 | PROD_NUM_PROC | VARCHAR2(40) | Y |  |  |
| 8 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 9 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 10 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_STIP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | GTIP_GRUPO | CHAR(4) | Y |  |  |
| 5 | STIP_GRUPO | VARCHAR2(6) | Y |  |  |
| 6 | STIP_DESC1 | VARCHAR2(500) | Y |  |  |
| 7 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 8 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_TAEX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | INFSM_SERIE | VARCHAR2(5) | Y |  |  |
| 7 | INFSM_NUM | VARCHAR2(15) | Y |  |  |
| 8 | INFSM_DTEMISS | DATE | Y |  |  |
| 9 | TAEX_COD_RE | VARCHAR2(15) | Y |  |  |
| 10 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 11 | TAEX_COD_RELA | NUMBER(2) | Y |  |  |
| 12 | TAEX_DAT_RE | DATE | Y |  |  |
| 13 | TAEX_COD_DE | VARCHAR2(15) | Y |  |  |
| 14 | TAEX_DAT_DE | DATE | Y |  |  |
| 15 | TAEX_COD_AVERB | CHAR(1) | Y |  |  |
| 16 | TAEX_DSC_COEMB | VARCHAR2(18) | Y |  |  |
| 17 | TAEX_DAT_COEMB | DATE | Y |  |  |
| 18 | TDOC_COD | CHAR(2) | Y |  |  |
| 19 | TAEX_COD_PAIS | CHAR(4) | Y |  |  |
| 20 | TAEX_DSC_COMEX | VARCHAR2(8) | Y |  |  |
| 21 | TAEX_DAT_COMEX | DATE | Y |  |  |
| 22 | MDOC_COD | CHAR(3) | Y |  |  |
| 23 | TAEX_NEXP | CHAR(1) | Y |  |  |
| 24 | TAEX_DAT_AVERB | DATE | Y |  |  |
| 25 | NUM01 | NUMBER | Y |  |  |
| 26 | NUM02 | NUMBER | Y |  |  |
| 27 | NUM03 | NUMBER | Y |  |  |
| 28 | VAR01 | VARCHAR2(150) | Y |  |  |
| 29 | VAR02 | VARCHAR2(150) | Y |  |  |
| 30 | VAR03 | VARCHAR2(150) | Y |  |  |
| 31 | VAR04 | VARCHAR2(150) | Y |  |  |
| 32 | VAR05 | VARCHAR2(150) | Y |  |  |
| 33 | TAEX_IND_DOC | CHAR(1) | Y |  |  |
| 34 | TAEX_CHV_NFE | VARCHAR2(44) | Y |  |  |
| 35 | TAEX_MOEDA | VARCHAR2(10) | Y |  |  |
| 36 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 37 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_TIPODOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | TDOC_COD | CHAR(5) | Y |  |  |
| 5 | TDOC_NF | CHAR(1) | Y |  |  |
| 6 | TDOC_DAT_ATUA | DATE | Y |  |  |
| 7 | TDOC_DSC | VARCHAR2(150) | Y |  |  |
| 8 | TDOC_COD86 | CHAR(3) | Y |  |  |
| 9 | TDOC_CAT83 | CHAR(3) | Y |  |  |
| 10 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 11 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_TIPO_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 5 | TOPE_DAT_ATUA | DATE | Y |  |  |
| 6 | TOPE_DSC | VARCHAR2(150) | Y |  |  |
| 7 | TOPE_COD_ENTRA | CHAR(1) | Y |  |  |
| 8 | TOPE_COD_SAIDA | CHAR(1) | Y |  |  |
| 9 | IND_EST | CHAR(1) | Y |  |  |
| 10 | IND_INV | CHAR(1) | Y |  |  |
| 11 | TOPE_COD86 | CHAR(1) | Y |  |  |
| 12 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 13 | MSG_ERRO | VARCHAR2(150) | Y |  |  |
| 14 | TOPE_DEPREC | CHAR(1) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

## REC_UNI_CONV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | NUMERO_JOB | VARCHAR2(20) | N |  |  |
| 3 | INDICE | NUMBER | N |  |  |
| 4 | EMPS_COD | VARCHAR2(9) | Y |  |  |
| 5 | FILI_COD | VARCHAR2(9) | Y |  |  |
| 6 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 7 | UNID_COD | CHAR(3) | Y |  |  |
| 8 | MATE_DAT_ATUA | DATE | Y |  |  |
| 9 | UNID_COD_VENDA | CHAR(3) | Y |  |  |
| 10 | UNID_COD_CONV | CHAR(3) | Y |  |  |
| 11 | TP_FATOR | NUMBER | Y |  |  |
| 12 | UTILIZA | CHAR(2) | Y |  |  |
| 13 | COD_ERRO | VARCHAR2(20) | Y |  |  |
| 14 | MSG_ERRO | VARCHAR2(150) | Y |  |  |

**PK**: USUARIO, NUMERO_JOB, INDICE

---

