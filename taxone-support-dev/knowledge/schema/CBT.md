# Módulo: CBT (CBT) - 55 tabelas

## CBT_ALIQ_GRP_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 4 | DAT_VALID_ALIQ | DATE | N | to_date('01011900','ddmmyyyy') |  |

**PK**: IDENT_GRP_COMB, IDENT_ESTADO, DAT_VALID_ALIQ

**FKs**:
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)

---

## CBT_ANEXO1M_QUADRO1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_PROD_SEF_CENTR | VARCHAR2(3) | N |  |  |
| 6 | IND_LINHA | VARCHAR2(2) | N |  |  |
| 7 | QTD_COMB | NUMBER(17,3) | Y |  |  |
| 8 | QTD_GAS_A | NUMBER(17,3) | Y |  |  |
| 9 | QTD_EAC | NUMBER(17,3) | Y |  |  |
| 10 | ALIQ_AD_REM_ICMS | NUMBER(7,4) | Y |  |  |
| 11 | VLR_GAS_A | NUMBER(17,2) | Y |  |  |
| 12 | VLR_EAC | NUMBER(17,2) | Y |  |  |
| 13 | COD_CATEGORIA_ESTAB | NUMBER(3) | Y |  |  |
| 14 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y | SYSDATE |  |
| 17 | PERIODO_COM_MOVIMENTO | VARCHAR2(3) | Y |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR, IND_LINHA

**Indexes**:
- IX_CBT_ANEXO1M_QUADRO1: (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR)

---

## CBT_ANEXO1M_QUADRO2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_PROD_SEF_CENTR | VARCHAR2(3) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | TIP_FORNEC | VARCHAR2(10) | Y |  |  |
| 8 | QTD_COMB_INI | NUMBER(17,3) | Y |  |  |
| 9 | QTD_COMB_ENT | NUMBER(17,3) | Y |  |  |
| 10 | QTD_COMB_TOT | NUMBER(17,3) | Y |  |  |
| 11 | PERC_COMB | NUMBER(9,6) | Y |  |  |
| 12 | QTD_COMB_FIM | NUMBER(17,3) | Y |  |  |
| 13 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y | SYSDATE |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR, IDENT_FIS_JUR

**Indexes**:
- IX_CBT_ANEXO1M_QUADRO2: (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR)

---

## CBT_ANEXO1M_QUADRO3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_PROD_SEF_CENTR | VARCHAR2(3) | N |  |  |
| 6 | DATA_FISCAL | DATE | N |  |  |
| 7 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 8 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_CFO | VARCHAR2(4) | N |  |  |
| 15 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 16 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 17 | QTD_COMB | NUMBER(17,3) | Y |  |  |
| 18 | QTD_GAS_A | NUMBER(17,3) | Y |  |  |
| 19 | QTD_EAC | NUMBER(17,3) | Y |  |  |
| 20 | ALIQ_AD_REM_ICMS | NUMBER(7,4) | Y |  |  |
| 21 | VLR_GAS_A | NUMBER(17,2) | Y |  |  |
| 22 | VLR_EAC | NUMBER(17,2) | Y |  |  |
| 23 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 24 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y | SYSDATE |  |

**Indexes**:
- IU_CBT_ANEXO1M_QUADRO3 (UNIQUE): (PROC_ID, COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_CFO, ALIQ_AD_REM_ICMS)
- IX_CBT_ANEXO1M_QUADRO3: (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR)

---

## CBT_ANEXO1M_QUADRO4

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_PROD_SEF_CENTR | VARCHAR2(3) | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | QTD_COMB | NUMBER(17,3) | Y |  |  |
| 8 | QTD_GAS_A | NUMBER(17,3) | Y |  |  |
| 9 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y | SYSDATE |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR, IDENT_ESTADO

**Indexes**:
- IX_CBT_ANEXO1M_QUADRO4: (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR)

---

## CBT_ANEXO1_QUADRO1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IND_LINHA | CHAR(1) | N |  |  |
| 3 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 4 | QTD_GAS_A | NUMBER(17,6) | Y |  |  |
| 5 | VLR_UNIT_MEDIO | NUMBER(11,6) | Y |  |  |
| 6 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IND_LINHA

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)

---

## CBT_ANEXO1_QUADRO2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 3 | QTD_COMB_INI | NUMBER(17,6) | Y |  |  |
| 4 | QTD_COMB_ENT | NUMBER(17,6) | Y |  |  |
| 5 | QTD_COMB_TOT | NUMBER(17,6) | Y |  |  |
| 6 | PERC_COMB | NUMBER(7,4) | Y |  |  |
| 7 | QTD_COMB_FIM | NUMBER(17,6) | Y |  |  |
| 8 | QTD_COMB_INI_AJUS | NUMBER(17,6) | Y |  |  |
| 9 | QTD_COMB_ENT_AJUS | NUMBER(17,6) | Y |  |  |
| 10 | QTD_COMB_TOT_AJUS | NUMBER(17,6) | Y |  |  |
| 11 | PERC_COMB_AJUS | NUMBER(7,4) | Y |  |  |
| 12 | QTD_COMB_FIM_AJUS | NUMBER(17,6) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IDENT_FIS_JUR

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1729: (IDENT_FIS_JUR)

---

## CBT_ANEXO1_QUADRO3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 3 | IDENT_ITEM_MERC | NUMBER(12) | N |  |  |
| 4 | IND_NORM_DEV | CHAR(1) | Y |  |  |
| 5 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 6 | QTD_GAS_A | NUMBER(17,6) | Y |  |  |
| 7 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 8 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 9 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | COD_PROD_OFICIAL | VARCHAR2(5) | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IDENT_DOCTO_FISCAL, IDENT_ITEM_MERC

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)

---

## CBT_ANEXO1_QUADRO4

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 4 | QTD_GAS_A | NUMBER(17,6) | Y |  |  |
| 5 | USUARIO | VARCHAR2(40) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 8 | IND_TIPO_OPER | CHAR(1) | N | 3 |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IDENT_ESTADO, IND_TIPO_OPER

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)

---

## CBT_ANEXO23_DEST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 7 | SEQUENCIAL | NUMBER(3) | N |  |  |
| 8 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 9 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 10 | DAT_INICIO | DATE | Y |  |  |
| 11 | DAT_FIM | DATE | Y |  |  |
| 12 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 13 | QTD_GAS_A | NUMBER(17,6) | Y |  |  |
| 14 | VLR_UNIT_MEDIO | NUMBER(11,6) | Y |  |  |
| 15 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 20 | VLR_ICMS_ST_COB | NUMBER(17,2) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | QTD_EAC | NUMBER(17,6) | Y |  |  |
| 23 | VLR_GAS_A | NUMBER(17,2) | Y |  |  |
| 24 | VLR_EAC | NUMBER(17,2) | Y |  |  |

**PK**: DAT_APURACAO, IDENT_GRP_COMB, SEQ_PERIODO, IND_PERIODICIDADE, IDENT_FIS_JUR, IDENT_ESTADO_DESTINO, SEQUENCIAL, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1741: (IDENT_FIS_JUR)

---

## CBT_ANEXO2M_QUADRO1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_PROD_SEF_CENTR | VARCHAR2(3) | N |  |  |
| 6 | IND_LINHA | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 8 | DATA_FISCAL | DATE | Y |  |  |
| 9 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 10 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 11 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 13 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 15 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 16 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 17 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 18 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 19 | QTD_COMB | NUMBER(17,3) | Y |  |  |
| 20 | QTD_GAS_A | NUMBER(17,3) | Y |  |  |
| 21 | QTD_EAC | NUMBER(17,3) | Y |  |  |
| 22 | ALIQ_AD_REM_ICMS | NUMBER(7,4) | Y |  |  |
| 23 | VLR_GAS_A | NUMBER(17,2) | Y |  |  |
| 24 | VLR_EAC | NUMBER(17,2) | Y |  |  |
| 25 | VLR_REPASSE_TOT | NUMBER(17,2) | Y |  |  |
| 26 | COD_CATEGORIA_ESTAB | NUMBER(3) | Y |  |  |
| 27 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 28 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 29 | DAT_GRAVACAO | DATE | Y | SYSDATE |  |
| 30 | PERIODO_COM_MOVIMENTO | VARCHAR2(3) | Y |  |  |

**Indexes**:
- IX_CBT_ANEXO2M_Q1_LIMP: (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR)
- IX_CBT_ANEXO2M_QUADRO1: (PROC_ID, COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PROD_SEF_CENTR, IND_LINHA, COD_ESTADO)

---

## CBT_ANEXO2_NF_EMIT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 6 | IDENT_ITEM_MERC | NUMBER(12) | N |  |  |
| 7 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 8 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 9 | IND_NORM_DEV | CHAR(1) | Y |  |  |
| 10 | IDENT_ESTADO_DESTINO | NUMBER(12) | Y |  |  |
| 11 | DAT_INICIO | DATE | Y |  |  |
| 12 | DAT_FIM | DATE | Y |  |  |
| 13 | IND_FRETE | CHAR(1) | Y |  |  |
| 14 | IND_DESTINACAO | CHAR(1) | Y |  |  |
| 15 | DSC_PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 16 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 17 | QTD_GAS_A | NUMBER(17,6) | Y |  |  |
| 18 | VLR_UNIT_PARTIDA | NUMBER(11,6) | Y |  |  |
| 19 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 20 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 21 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: DAT_APURACAO, IDENT_GRP_COMB, SEQ_PERIODO, IND_PERIODICIDADE, IDENT_DOCTO_FISCAL, IDENT_ITEM_MERC, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)

**Indexes**:
- IX_CBT_ANEXO2_NF: (DAT_APURACAO, IDENT_GRP_COMB, IDENT_ESTADO_DESTINO, COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO3_QUADR41

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 7 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 8 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 9 | PROPORCAO | NUMBER(7,4) | Y |  |  |
| 10 | QTD_COMB_TOT | NUMBER(17,6) | Y |  |  |
| 11 | QTD_COMB_PROP | NUMBER(17,6) | Y |  |  |
| 12 | QTD_GAS_A_PROP | NUMBER(17,6) | Y |  |  |
| 13 | VLR_UNIT_MEDIO | NUMBER(11,6) | Y |  |  |
| 14 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 15 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 16 | VLR_ICMS_ST_COB | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS_ST_DEV | NUMBER(17,2) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | SEQ_ALIQ_ICMS_ST | NUMBER(2) | N | 1 |  |

**PK**: DAT_APURACAO, IDENT_ESTADO_DESTINO, IDENT_FIS_JUR, SEQ_PERIODO, IND_PERIODICIDADE, IDENT_GRP_COMB, COD_EMPRESA, COD_ESTAB, SEQ_ALIQ_ICMS_ST

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- DAT_APURACAO, IDENT_ESTADO_DESTINO, IDENT_FIS_JUR, SEQ_PERIODO, IND_PERIODICIDADE, COD_EMPRESA, COD_ESTAB → CBT_ANEXO3_QUADRO2(DAT_APURACAO, IDENT_ESTADO_DESTINO, IDENT_FIS_JUR, SEQ_PERIODO, IND_PERIODICIDADE, COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_FK_SAF_1747: (IDENT_FIS_JUR)

---

## CBT_ANEXO3_QUADR42

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 7 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 8 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 9 | SEQUENCIAL | NUMBER(3) | N |  |  |
| 10 | PROPORCAO | NUMBER(7,4) | Y |  |  |
| 11 | QTD_COMB_TOT | NUMBER(17,6) | Y |  |  |
| 12 | QTD_COMB_PROP | NUMBER(17,6) | Y |  |  |
| 13 | QTD_GAS_A_PROP | NUMBER(17,6) | Y |  |  |
| 14 | VLR_UNIT_MEDIO | NUMBER(11,6) | Y |  |  |
| 15 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 16 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 17 | VLR_ICMS_ST_COB | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS_ST_DEV | NUMBER(17,2) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 22 | IDENT_FIS_JUR_CLI | NUMBER(12) | N | 0 |  |
| 23 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: DAT_APURACAO, IDENT_ESTADO_DESTINO, IDENT_FIS_JUR, SEQ_PERIODO, IND_PERIODICIDADE, IDENT_GRP_COMB, SEQUENCIAL, COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR_CLI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- DAT_APURACAO, IDENT_ESTADO_DESTINO, IDENT_FIS_JUR, SEQ_PERIODO, IND_PERIODICIDADE, COD_EMPRESA, COD_ESTAB → CBT_ANEXO3_QUADRO2(DAT_APURACAO, IDENT_ESTADO_DESTINO, IDENT_FIS_JUR, SEQ_PERIODO, IND_PERIODICIDADE, COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_FK_SAF_1752: (IDENT_FIS_JUR)

---

## CBT_ANEXO3_QUADRO2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 7 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 8 | DAT_INICIO | DATE | Y |  |  |
| 9 | DAT_FIM | DATE | Y |  |  |
| 10 | IND_SUBSTITUTO | CHAR(1) | Y |  |  |
| 11 | VLR_GNRE | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: DAT_APURACAO, IDENT_ESTADO_DESTINO, IDENT_FIS_JUR, SEQ_PERIODO, IND_PERIODICIDADE, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1744: (IDENT_FIS_JUR)

---

## CBT_ANEXO4_QUADRO2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 6 | IDENT_ITEM_MERC | NUMBER(12) | N |  |  |
| 7 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 8 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 9 | IND_NORM_DEV | CHAR(1) | Y |  |  |
| 10 | IDENT_ESTADO_ORIGEM | NUMBER(12) | Y |  |  |
| 11 | DAT_INICIO | DATE | Y |  |  |
| 12 | DAT_FIM | DATE | Y |  |  |
| 13 | IND_FRETE | CHAR(1) | Y |  |  |
| 14 | DSC_PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 15 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 16 | VLR_UNIT | NUMBER(11,6) | Y |  |  |
| 17 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 19 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 20 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 24 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: DAT_APURACAO, IDENT_GRP_COMB, SEQ_PERIODO, IND_PERIODICIDADE, IDENT_DOCTO_FISCAL, IDENT_ITEM_MERC, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)

**Indexes**:
- IX_CBT_ANEXO4_QUA2: (DAT_APURACAO, IDENT_GRP_COMB, IDENT_ESTADO_ORIGEM, COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO5_CLIENTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IDENT_FIS_JUR_CLI | NUMBER(12) | N |  |  |
| 6 | IDENT_ESTADO_ORIGEM | NUMBER(12) | N |  |  |
| 7 | CNPJ_FORN_AEAC_CLI | VARCHAR2(14) | N |  |  |
| 8 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 9 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 10 | DAT_INICIO | DATE | Y |  |  |
| 11 | DAT_FIM | DATE | Y |  |  |
| 12 | QTD_AEAC_TOT | NUMBER(17,6) | Y |  |  |
| 13 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 14 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 15 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, IDENT_GRP_COMB, IDENT_FIS_JUR_CLI, IDENT_ESTADO_ORIGEM, CNPJ_FORN_AEAC_CLI, SEQ_PERIODO, IND_PERIODICIDADE, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)
- IDENT_FIS_JUR_CLI → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1755: (IDENT_FIS_JUR_CLI)

---

## CBT_ANEXO5_QUADR41

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IDENT_ESTADO_ORIGEM | NUMBER(12) | N |  |  |
| 6 | IDENT_FIS_JUR_GAS_A | NUMBER(12) | N |  |  |
| 7 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 8 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 9 | IDENT_FIS_JUR_AEAC | NUMBER(12) | N |  |  |
| 10 | PROPORCAO | NUMBER(7,4) | Y |  |  |
| 11 | QTD_AEAC_TOT | NUMBER(17,6) | Y |  |  |
| 12 | QTD_AEAC_PROP | NUMBER(17,6) | Y |  |  |
| 13 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 14 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 15 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: DAT_APURACAO, IDENT_GRP_COMB, IDENT_ESTADO_ORIGEM, IDENT_FIS_JUR_GAS_A, SEQ_PERIODO, IND_PERIODICIDADE, IDENT_FIS_JUR_AEAC, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)
- IDENT_FIS_JUR_GAS_A → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1760: (IDENT_FIS_JUR_GAS_A)

---

## CBT_ANEXO5_QUADR42

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IDENT_ESTADO_ORIGEM | NUMBER(12) | N |  |  |
| 6 | IDENT_FIS_JUR_GAS_A | NUMBER(12) | N |  |  |
| 7 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 8 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 9 | IDENT_FIS_JUR_CLI | NUMBER(12) | N |  |  |
| 10 | CNPJ_FORN_AEAC_CLI | VARCHAR2(14) | N |  |  |
| 11 | PROPORCAO | NUMBER(7,4) | Y |  |  |
| 12 | QTD_AEAC_TOT | NUMBER(17,6) | Y |  |  |
| 13 | QTD_AEAC_PROP | NUMBER(17,6) | Y |  |  |
| 14 | VLR_BASE_ICMS_PROP | NUMBER(17,2) | Y |  |  |
| 15 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 16 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: DAT_APURACAO, IDENT_GRP_COMB, IDENT_ESTADO_ORIGEM, IDENT_FIS_JUR_GAS_A, SEQ_PERIODO, IND_PERIODICIDADE, IDENT_FIS_JUR_CLI, CNPJ_FORN_AEAC_CLI, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)
- IDENT_FIS_JUR_GAS_A → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1765: (IDENT_FIS_JUR_GAS_A)

---

## CBT_ANEXO5_QUADRO2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IDENT_ESTADO_ORIGEM | NUMBER(12) | N |  |  |
| 6 | IDENT_FIS_JUR_GAS_A | NUMBER(12) | N |  |  |
| 7 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 8 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 9 | DAT_INICIO | DATE | Y |  |  |
| 10 | DAT_FIM | DATE | Y |  |  |
| 11 | IDENT_GRP_COMB_GAS | NUMBER(12) | Y |  |  |
| 12 | IND_SUBSTITUTO | CHAR(1) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: DAT_APURACAO, IDENT_GRP_COMB, IDENT_ESTADO_ORIGEM, IDENT_FIS_JUR_GAS_A, SEQ_PERIODO, IND_PERIODICIDADE, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)
- IDENT_GRP_COMB_GAS → CBT_GRP_COMB(IDENT_GRP_COMB)
- IDENT_FIS_JUR_GAS_A → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1771: (IDENT_FIS_JUR_GAS_A)

---

## CBT_ANEXO6M_QUADR1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | VLR_ICMS_ST_111 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_ST_112 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS_ST_113 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_ST_114 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_ST_115 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_ST_116 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_ST_117 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_ST_121 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_ST_122 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ST_123 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_ST_124 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_ST_125 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS_ST_126 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS_ST_127 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_ST_128 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS_ST_129 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_ST_1210 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS_ST_1211 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_ST_1212 | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS_ST_1213 | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMS_ST_13 | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMS_ST_131 | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ICMS_ST_132 | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ICMS_ST_133 | NUMBER(17,2) | Y |  |  |
| 29 | USUARIO | VARCHAR2(40) | Y |  |  |
| 30 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 31 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 32 | VLR_ICMS_ST_1112 | NUMBER(17,2) | Y |  |  |
| 33 | VLR_ICMS_ST_1201 | NUMBER(17,2) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6M_QUADR2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | VLR_ICMS_ST_21 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_ST_22 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS_ST_23 | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6M_QUADR3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 6 | QTD_COMB | NUMBER(16) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_RET | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_TOT | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IDENT_GRP_COMB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6M_QUADR31_32

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | COD_TAG | VARCHAR2(6) | N |  |  |
| 6 | IDENT_ESTADO_QUAD | NUMBER(12) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(2) | N |  |  |
| 8 | QTD_COMB | NUMBER(16) | Y |  |  |
| 9 | VLR_ICMS_COB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_RET | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_TOT | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO_DESTINO, COD_TAG, IDENT_ESTADO_QUAD, COD_PRODUTO

---

## CBT_ANEXO6M_QUADR4A15

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | COD_TAG | VARCHAR2(6) | N |  |  |
| 6 | COD_QUADRO | VARCHAR2(2) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | IDENT_ESTADO_QUAD | NUMBER(12) | Y |  |  |
| 9 | DAT_REF | DATE | N |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | COMUNIC_REF | VARCHAR2(80) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_CBT_ANEXO6M_QUADR4A15 (UNIQUE): (DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, COD_TAG, COD_QUADRO, IDENT_FIS_JUR, IDENT_ESTADO_QUAD, DAT_REF)

---

## CBT_ANEXO6M_RELAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | COD_TAG | VARCHAR2(6) | N |  |  |
| 6 | COD_QUADRO | VARCHAR2(2) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | IDENT_ESTADO_QUAD | NUMBER(12) | Y |  |  |
| 9 | DAT_REF | DATE | N |  |  |
| 10 | IND_REPASSE_DEDUCAO | VARCHAR2(1) | Y |  |  |
| 11 | VLR_ICMS_ANX6M | NUMBER(17,2) | Y |  |  |
| 12 | ID_GRUPO | VARCHAR2(4) | Y |  |  |
| 13 | ANEXO_ORIGEM | VARCHAR2(10) | Y |  |  |
| 14 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 15 | UF_ORIGEM | VARCHAR2(2) | Y |  |  |
| 16 | UF_EMITENTE | VARCHAR2(2) | Y |  |  |
| 17 | CATEGORIA_EMITENTE | VARCHAR2(100) | Y |  |  |
| 18 | CNPJ_EMITENTE | VARCHAR2(14) | Y |  |  |
| 19 | RAZAO_SOCIAL_EMITENTE | VARCHAR2(300) | Y |  |  |
| 20 | CNPJ_DESTINATARIO | VARCHAR2(14) | Y |  |  |
| 21 | CNPJ_FORNECEDOR | VARCHAR2(14) | Y |  |  |
| 22 | UF_REPASSE | VARCHAR2(2) | Y |  |  |
| 23 | UF_DEDUCAO | VARCHAR2(2) | Y |  |  |
| 24 | VLR_ICMS_ANX_DISTRIB | NUMBER(17,2) | Y |  |  |
| 25 | DSC_DIG_CALC | VARCHAR2(1000) | Y |  |  |
| 26 | USUARIO | VARCHAR2(40) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO_DESTINO → ESTADO(IDENT_ESTADO)
- IDENT_ESTADO_QUAD → ESTADO(IDENT_ESTADO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- UK_CBT_ANEXO6M_RELAT (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO_DESTINO, COD_TAG, COD_QUADRO, IDENT_FIS_JUR, IDENT_ESTADO_QUAD, DAT_REF, ID_GRUPO)

---

## CBT_ANEXO6_QUADR1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | VLR_ICMS_ST_111 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_ST_112 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS_ST_113 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_ST_114 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_ST_121 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_ST_122 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_ST_123 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_ST_124 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_ST_125 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ST_126 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_ST_127 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_ST_128 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS_ST_129 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS_ST_1210 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_ST_1211 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS_ST_13 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_ST_131 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS_ST_132 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_ST_133 | NUMBER(17,2) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 27 | VLR_ICMS_ST_115 | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ICMS_ST_116 | NUMBER(17,2) | Y |  |  |
| 29 | VLR_ICMS_ST_1212 | NUMBER(17,2) | Y |  |  |
| 30 | VLR_ICMS_ST_1213 | NUMBER(17,2) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6_QUADR10

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IND_QUADRO | VARCHAR2(2) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IND_QUADRO, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6_QUADR14

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IND_QUADRO | VARCHAR2(2) | N |  |  |
| 6 | COD_ESTAB_TRANSF | VARCHAR2(6) | N |  |  |
| 7 | IDENT_ESTADO_QUAD | NUMBER(12) | Y |  |  |
| 8 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IND_QUADRO, COD_ESTAB_TRANSF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6_QUADR2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | VLR_ICMS_ST_21 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_ST_22 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS_ST_23 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_ST_24 | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6_QUADR3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 6 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 7 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_TOT | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IDENT_GRP_COMB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6_QUADR45

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IND_QUADRO | VARCHAR2(2) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | IDENT_ESTADO_QUAD | NUMBER(12) | Y |  |  |
| 8 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | COMUNIC_REF | VARCHAR2(80) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IND_QUADRO, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6_QUADR6

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IND_QUADRO | VARCHAR2(2) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | IDENT_ESTADO_QUAD | NUMBER(12) | N |  |  |
| 8 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | COMUNIC_REF | VARCHAR2(80) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IND_QUADRO, IDENT_FIS_JUR, IDENT_ESTADO_QUAD

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6_QUADR78

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IND_QUADRO | VARCHAR2(2) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | IDENT_ESTADO_QUAD | NUMBER(12) | N |  |  |
| 8 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | COMUNIC_REF | VARCHAR2(80) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IND_QUADRO, IDENT_FIS_JUR, IDENT_ESTADO_QUAD

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO6_QUADR9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IND_QUADRO | VARCHAR2(2) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | IDENT_ESTADO_QUAD | NUMBER(12) | N |  |  |
| 8 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | COMUNIC_REF | VARCHAR2(80) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IND_QUADRO, IDENT_FIS_JUR, IDENT_ESTADO_QUAD

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO7M_QUADR1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | VLR_ICMS_ST_11 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_ST_12 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS_ST_13 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_ST_14 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_ST_15 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_ST_16 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_ST_17 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_ST_18 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_ST_19 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ST_110 | NUMBER(17,2) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO7M_QUADR2A7

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | COD_TAG | VARCHAR2(6) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | IDENT_ESTADO_QUAD | NUMBER(12) | N |  |  |
| 8 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, COD_TAG, IDENT_FIS_JUR, IDENT_ESTADO_QUAD

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO7_QUADR1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | VLR_ICMS_ST_11 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_ST_12 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS_ST_13 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_ST_14 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_ST_15 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_ST_16 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_ST_17 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_ST_18 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_ST_19 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ST_110 | NUMBER(17,2) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO7_QUADR24

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IND_QUADRO | VARCHAR2(2) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | IDENT_ESTADO_QUAD | NUMBER(12) | Y |  |  |
| 8 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IND_QUADRO, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO7_QUADR57

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 5 | IND_QUADRO | VARCHAR2(2) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | IDENT_ESTADO_QUAD | NUMBER(12) | N |  |  |
| 8 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, IDENT_ESTADO_DESTINO, IND_QUADRO, IDENT_FIS_JUR, IDENT_ESTADO_QUAD

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_ANEXO8_QUADRO1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IND_LINHA | CHAR(2) | N |  |  |
| 3 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 4 | VLR_UNIT_MEDIO | NUMBER(11,6) | Y |  |  |
| 5 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ALIQ_MEDIA | NUMBER(5,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(13,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IND_LINHA

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)

---

## CBT_ANEXO8_QUADRO2_3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IND_LINHA | CHAR(1) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | QTD_GAS_C | NUMBER(17,6) | Y |  |  |
| 5 | QTD_GAS_A | NUMBER(17,6) | Y |  |  |
| 6 | QTD_MISTURA | NUMBER(17,6) | Y |  |  |
| 7 | QTD_PROP_AEAC | NUMBER(17,6) | Y |  |  |
| 8 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_REC | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IND_LINHA, IDENT_ESTADO

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)

---

## CBT_ANEXO8_QUADRO4_5

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 3 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 4 | IDENT_ITEM_MERC | NUMBER(12) | N |  |  |
| 5 | SEQ_PERIODO | NUMBER(2) | N |  |  |
| 6 | IND_PERIODICIDADE | CHAR(1) | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 8 | IND_NORM_DEV | CHAR(1) | Y |  |  |
| 9 | IDENT_ESTADO_ORIG_DEST | NUMBER(12) | Y |  |  |
| 10 | IND_FRETE | CHAR(1) | Y |  |  |
| 11 | DSC_PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 12 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 13 | VLR_UNIT | NUMBER(11,6) | Y |  |  |
| 14 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 16 | ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 17 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IDENT_GRP_COMB, IDENT_DOCTO_FISCAL, IDENT_ITEM_MERC, SEQ_PERIODO, IND_PERIODICIDADE

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)

**Indexes**:
- IX_CBT_ANEXO8_QUADRO4_5_01: (IDENT_GRP_ESTOQ, IDENT_GRP_COMB, MOVTO_E_S)

---

## CBT_ANEXO_ABC_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IND_ANEXO | CHAR(1) | N |  | Valores assumidos : A, B, C |
| 6 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 7 | IDENT_ITEM_MERC | NUMBER(12) | N |  |  |
| 8 | IND_E_S | CHAR(1) | Y |  | Valores assumidos : E, S |
| 9 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 10 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 11 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  | Valores assumidos : 1, 2, 3 |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | VLR_TRIBUTO_ICMS_GNRE | NUMBER(17,2) | Y |  | Valor apresentado no Anexo B - quadro2 (recebimentos) |
| 18 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  | Valor apresentado no Anexo B - quadro3 (remessas internas) |
| 19 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  | Valor apresentado no Anexo B - quadro3 (remessas internas) |
| 20 | IDENT_ESTADO_PFJ | NUMBER(12) | Y |  | Informação utilizada no Anexo B - quadro 5 |

**PK**: DAT_APURACAO, IDENT_GRP_COMB, COD_ESTAB, IND_ANEXO, COD_EMPRESA, IDENT_DOCTO_FISCAL, IDENT_ITEM_MERC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)

**Indexes**:
- IX_CBT_ANEXO_ABC_NF: (DAT_APURACAO, IDENT_GRP_COMB, COD_ESTAB, IND_ANEXO, IND_E_S, COD_EMPRESA, IDENT_ESTADO_PFJ)

---

## CBT_ANEXO_B_QUADRO1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IND_LINHA | CHAR(1) | N |  | Valores assumidos : 1 - Estoque Inicial, 2 - Entradas, 3 - Total Disponivel, 4 - Saidas, 5 - Estoque Final, 6 - Ganhos, 7 - Perdas |
| 3 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 4 | USUARIO | VARCHAR2(40) | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IND_LINHA

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)

---

## CBT_BASE_ST_GRP_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | VALID_BASE_ST | DATE | N |  |  |
| 4 | IND_REGRA_BASE_ST | CHAR(1) | Y |  |  |
| 5 | VLR_REGRA_BASE_ST | NUMBER(11,6) | Y |  |  |
| 6 | VLR_REGR_REDUCAO_BASE | NUMBER(11,6) | Y |  |  |
| 7 | FATOR_CONV_VOLUME | NUMBER(7,6) | Y |  |  |

**PK**: IDENT_GRP_COMB, IDENT_ESTADO, VALID_BASE_ST

**FKs**:
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)

---

## CBT_CARGA_ARQUIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_ANEXO | VARCHAR2(6) | N |  |  |
| 5 | ID_GRUPO | VARCHAR2(4) | N |  |  |
| 6 | MES_ANO | VARCHAR2(6) | Y |  |  |
| 7 | UF_DEST | VARCHAR2(2) | Y |  |  |
| 8 | UF_ORIG | VARCHAR2(2) | Y |  |  |
| 9 | UF_EMIT | VARCHAR2(2) | Y |  |  |
| 10 | CATEG_EMIT | VARCHAR2(6) | Y |  |  |
| 11 | CNPJ_EMIT | VARCHAR2(14) | Y |  |  |
| 12 | RAZ_SOCIAL_EMIT | VARCHAR2(100) | Y |  |  |
| 13 | CNPJ_DEST | VARCHAR2(14) | Y |  |  |
| 14 | CNPJ_FORNEC | VARCHAR2(14) | Y |  |  |
| 15 | VLR_31 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_32 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_35 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_42 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_43 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_51 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_52 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_58 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_59 | NUMBER(17,2) | Y |  |  |
| 24 | VLR_Q2 | NUMBER(17,2) | Y |  |  |
| 25 | VLR_Q3 | NUMBER(17,2) | Y |  |  |
| 26 | USUARIO | VARCHAR2(40) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_DIG_CALC | VARCHAR2(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_GRP_COMB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 2 | COD_GRP_COMB | VARCHAR2(2) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(30) | Y |  |  |
| 4 | IND_ANEXO1 | CHAR(1) | Y |  |  |
| 5 | IND_ANEXO2 | CHAR(1) | Y |  |  |
| 6 | IND_ANEXO3 | CHAR(1) | Y |  |  |
| 7 | IND_ANEXO4 | CHAR(1) | Y |  |  |
| 8 | IND_ANEXO5 | CHAR(1) | Y |  |  |
| 9 | IND_ANEXO6 | CHAR(1) | Y |  |  |
| 10 | IND_ANEXO7 | CHAR(1) | Y |  |  |
| 11 | COD_PROD_SEF | VARCHAR2(3) | Y |  |  |
| 12 | IND_ANEXO_A_RO | CHAR(1) | Y | 'N' |  |
| 13 | IND_ANEXO_B_RO | CHAR(1) | Y | 'N' |  |
| 14 | IND_ANEXO_C_RO | CHAR(1) | Y | 'N' |  |
| 15 | IND_ANEXO8 | CHAR(1) | Y |  |  |
| 16 | IND_ANEXO1M | VARCHAR2(1) | Y |  |  |
| 17 | IND_ANEXO2M | VARCHAR2(1) | Y |  |  |
| 18 | IND_ANEXO3M | VARCHAR2(1) | Y |  |  |
| 19 | IND_ANEXO4M | VARCHAR2(1) | Y |  |  |
| 20 | IND_ANEXO5M | VARCHAR2(1) | Y |  |  |
| 21 | IND_ANEXO6M | VARCHAR2(1) | Y |  |  |
| 22 | IND_ANEXO7M | VARCHAR2(1) | Y |  |  |

**PK**: IDENT_GRP_COMB

**Indexes**:
- UK_CBT_GRP_COMP (UNIQUE): (COD_GRP_COMB)

---

## CBT_GRP_ESTOQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_GRP_COMB | NUMBER(12) | Y |  |  |
| 6 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 7 | SEQ_PERIODO | NUMBER(2) | Y |  |  |
| 8 | IND_PERIODICIDADE | CHAR(1) | Y |  |  |
| 9 | DAT_INICIO | DATE | Y |  |  |
| 10 | DAT_FIM | DATE | Y |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 12 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 13 | QTD_GAS_A | NUMBER(17,6) | Y |  |  |
| 14 | VLR_UNIT_MEDIO | NUMBER(11,6) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | VLR_ALIQ_MEDIA | NUMBER(5,2) | Y |  |  |
| 20 | VLR_ICMS | NUMBER(13,2) | Y |  |  |
| 21 | QTD_EAC | NUMBER(17,6) | Y |  |  |
| 22 | VLR_GAS_A | NUMBER(13,2) | Y |  |  |

**PK**: IDENT_GRP_ESTOQ

**FKs**:
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_CBT_GRP_ESTOQ (UNIQUE): (DAT_APURACAO, IDENT_GRP_COMB, SEQ_PERIODO, IND_PERIODICIDADE, COD_EMPRESA, COD_ESTAB, GRUPO_CONTAGEM)

---

## CBT_GRP_PFJ_ESTOQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_ESTOQ | NUMBER(12) | N |  |  |
| 2 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 3 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 4 | USUARIO | VARCHAR2(40) | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | QTD_EAC | NUMBER(17,6) | Y |  |  |

**PK**: IDENT_GRP_ESTOQ, IDENT_FIS_JUR

**FKs**:
- IDENT_GRP_ESTOQ → CBT_GRP_ESTOQ(IDENT_GRP_ESTOQ)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1726: (IDENT_FIS_JUR)

---

## CBT_PAR_LANCTO_P9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ANEXO | VARCHAR2(2) | N |  |  |
| 4 | COD_QUADRO | VARCHAR2(2) | N |  |  |
| 5 | COD_ITEM | VARCHAR2(10) | N |  |  |
| 6 | IDENT_ESTADO_DESTINO | NUMBER(12) | N |  |  |
| 7 | IND_TP_APUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 9 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 10 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 11 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 12 | COD_OPER_APUR_NEG | VARCHAR2(5) | Y |  |  |
| 13 | DSC_ITEM_APURACAO_NEG | VARCHAR2(150) | Y |  |  |
| 14 | COD_AJUSTE_ICMS_NEG | VARCHAR2(8) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO_DESTINO → ESTADO(IDENT_ESTADO)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_TIPO_LIVRO, COD_OPER_APUR_NEG → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS_NEG → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

**Indexes**:
- PK_CBT_PAR_LANCTO_P9 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_ANEXO, COD_QUADRO, COD_ITEM, IDENT_ESTADO_DESTINO, COD_OPER_APUR)

---

## CBT_PRD_ICMS_MONO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROD_OFICIAL | VARCHAR2(10) | N |  |  |
| 2 | DAT_VALID_INI | DATE | N |  |  |
| 3 | DSC_PROD_OFICIAL | VARCHAR2(250) | Y |  |  |
| 4 | ALIQ_AD_REM_ICMS | NUMBER(7,4) | Y |  |  |
| 5 | DAT_VALID_FIM | DATE | Y |  |  |
| 6 | IND_BIOCOMB | VARCHAR2(1) | Y |  |  |

**PK**: COD_PROD_OFICIAL, DAT_VALID_INI

---

## CBT_PROD_SEF_CENTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ANEXO | VARCHAR2(8) | N |  |  |
| 2 | COD_PROD_SEF | VARCHAR2(3) | N |  |  |
| 3 | COD_PROD_SEF_CENTR | VARCHAR2(3) | N |  |  |
| 4 | DSC_PROD_SEF_CENTR | VARCHAR2(100) | N |  |  |

**PK**: COD_ANEXO, COD_PROD_SEF, COD_PROD_SEF_CENTR

---

## CBT_REGRA_COMB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VALID_REGRA_COMB | DATE | N |  |  |
| 4 | IND_BASE_ANEXO1 | CHAR(1) | Y |  |  |
| 5 | IND_BASE_ANEXO2 | CHAR(1) | Y |  |  |
| 6 | IND_BASE_ANEXO3 | CHAR(1) | Y |  |  |
| 7 | IND_MOV_FIS | CHAR(1) | Y |  |  |
| 8 | IND_AJ_REP_PROV | CHAR(1) | Y |  |  |
| 9 | IND_AJ_ICMS_REC | CHAR(1) | Y |  |  |
| 10 | IND_GERA_Q13 | VARCHAR2(1) | Y | 'S' |  |

**PK**: COD_EMPRESA, COD_ESTAB, VALID_REGRA_COMB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CBT_REG_EST_PFJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 5 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 6 | IND_SITUACAO | CHAR(1) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO, COD_FIS_JUR, IND_FIS_JUR, GRUPO_FIS_JUR

---

