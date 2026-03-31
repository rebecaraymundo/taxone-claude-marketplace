# Módulo: COT (COT) - 20 tabelas

## COT_BASE_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | GRUPO_COF | NUMBER(2) | Y |  |  |
| 3 | ANO_COMP | NUMBER(4) | Y |  |  |
| 4 | MES_COMP | NUMBER(2) | Y |  |  |
| 5 | IND_TIPO | NUMBER(2) | Y |  |  |
| 6 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 7 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 8 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 9 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 13 | ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 14 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_COF | NUMBER(17,2) | Y |  |  |
| 16 | ALIQ_COF | NUMBER(7,4) | Y |  |  |
| 17 | VLR_COF | NUMBER(17,2) | Y |  |  |
| 18 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 21 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 23 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |
| 24 | VLR_COFS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMSS_CF | NUMBER(17,2) | Y |  |  |
| 26 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_COT_BASE_CFO: (COD_EMPRESA, COD_ESTAB, GRUPO_COF, ANO_COMP, MES_COMP, IND_TIPO, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP)

---

## COT_BASE_CONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO_COMP | NUMBER(4) | N |  |  |
| 3 | MES_COMP | NUMBER(2) | N |  |  |
| 4 | IND_TIPO | NUMBER(2) | N |  |  |
| 5 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 6 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 7 | DAT_LANCTO | DATE | N |  |  |
| 8 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 9 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 10 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DEP_MES | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DESPESA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_COF | NUMBER(17,2) | Y |  |  |
| 14 | ALIQ_COF | NUMBER(7,4) | Y |  |  |
| 15 | VLR_COF | NUMBER(17,2) | Y |  |  |
| 16 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 17 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 18 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 21 | COD_ESTAB | VARCHAR2(6) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IND_TIPO, GRUPO_CONTA, COD_CONTA, DAT_LANCTO, IND_DEB_CRE, ARQUIVAMENTO

---

## COT_BASE_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | DATE | Y |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 5 | SEQUENCIAL | NUMBER(5) | Y |  |  |
| 6 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 7 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 10 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 11 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 12 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 13 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_COT_BASE_ECF: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO, SEQUENCIAL, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_TRIB_INT, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP)

---

## COT_BASE_MONTAD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | ANO_COMP | NUMBER(4) | Y |  |  |
| 3 | MES_COMP | NUMBER(2) | Y |  |  |
| 4 | IND_TIPO | NUMBER(2) | Y |  |  |
| 5 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 6 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 7 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 8 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 9 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ALIQ_RED | NUMBER(7,4) | Y |  |  |
| 14 | VLR_BASE_APUR | NUMBER(17,2) | Y |  |  |
| 15 | ALIQ_COF | NUMBER(7,4) | Y |  |  |
| 16 | VLR_COF | NUMBER(17,2) | Y |  |  |
| 17 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 20 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |
| 22 | VLR_COFS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMSS_CF | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_COT_BASE_MONTAD: (COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IND_TIPO, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, COD_NBM)

---

## COT_BASE_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | GRUPO_COF | NUMBER(2) | Y |  |  |
| 3 | ANO_COMP | NUMBER(4) | Y |  |  |
| 4 | MES_COMP | NUMBER(2) | Y |  |  |
| 5 | IND_TIPO | NUMBER(2) | Y |  |  |
| 6 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 7 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 8 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 9 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 10 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 11 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 12 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 13 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_COF | NUMBER(17,2) | Y |  |  |
| 17 | ALIQ_COF | NUMBER(7,4) | Y |  |  |
| 18 | VLR_COF | NUMBER(17,2) | Y |  |  |
| 19 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 22 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |
| 24 | VLR_COFS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMSS_CF | NUMBER(17,2) | Y |  |  |
| 26 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_COT_BASE_PROD: (COD_EMPRESA, COD_ESTAB, GRUPO_COF, ANO_COMP, MES_COMP, IND_TIPO, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, GRUPO_PRODUTO)

---

## COT_BASE_SERVICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | GRUPO_COF | NUMBER(2) | N |  |  |
| 3 | ANO_COMP | NUMBER(4) | N |  |  |
| 4 | MES_COMP | NUMBER(2) | N |  |  |
| 5 | IND_TIPO | NUMBER(2) | N |  |  |
| 6 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 7 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | DAT_DOC | DATE | N |  |  |
| 10 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_IRRF | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_COF | NUMBER(17,2) | Y |  |  |
| 14 | ALIQ_COF | NUMBER(7,4) | Y |  |  |
| 15 | VLR_COF | NUMBER(17,2) | Y |  |  |
| 16 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 17 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 20 | COD_ESTAB | VARCHAR2(6) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_COF, ANO_COMP, MES_COMP, IND_TIPO, GRUPO_SERVICO, COD_SERVICO, NUM_DOCFIS, DAT_DOC

---

## COT_CLASSE_REVPREV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMP | NUMBER(4) | N |  |  |
| 4 | MES_COMP | NUMBER(2) | N |  |  |
| 5 | GRUPO_MONOF | NUMBER(2) | N |  |  |
| 6 | CLASSE_COF | NUMBER(3) | N |  |  |
| 7 | VALID_CLASSE | DATE | N |  |  |
| 8 | VLR_BASE_COF | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, GRUPO_MONOF, CLASSE_COF, VALID_CLASSE

**FKs**:
- GRUPO_MONOF, CLASSE_COF, VALID_CLASSE → COT_GRP_CLASSE(GRUPO_MONOF, CLASSE_COF, VALID_CLASSE)

---

## COT_COMIS_MONTAD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | ANO_COMP | NUMBER(4) | Y |  |  |
| 3 | MES_COMP | NUMBER(2) | Y |  |  |
| 4 | VLR_COMIS | NUMBER(17,2) | Y |  |  |
| 5 | VLR_ICMS_COMIS | NUMBER(17,2) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |

**Indexes**:
- IX_COT_COMIS_MONTAD: (COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP)

---

## COT_CRED_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | DAT_INVENT | DATE | Y |  |  |
| 3 | VLR_SALDO_INV | NUMBER(17,2) | Y |  |  |
| 4 | VLR_INV_PROD | NUMBER(17,2) | Y |  |  |
| 5 | VLR_INV_PROD_EXC | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 7 | ALIQ_CRED | NUMBER(7,4) | Y |  |  |
| 8 | VLR_CRED | NUMBER(17,2) | Y |  |  |
| 9 | VLR_AVOS | NUMBER(17,2) | Y |  |  |
| 10 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |

**Indexes**:
- IX_COT_CRED_EST: (COD_EMPRESA, COD_ESTAB, DAT_INVENT)

---

## COT_DEM_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | ANO_COMP | NUMBER(4) | Y |  |  |
| 3 | MES_COMP | NUMBER(2) | Y |  |  |
| 4 | VLR_BASE_MERC | NUMBER(17,2) | Y |  |  |
| 5 | VLR_BASE_SERV | NUMBER(17,2) | Y |  |  |
| 6 | VLR_OUT_REC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ISENTA_ALIQ | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ATIVO_IMOB | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ATIVO_PERM | NUMBER(17,2) | Y |  |  |
| 10 | VLR_REC_AUF | NUMBER(17,2) | Y |  |  |
| 11 | VLR_PROD_EXC | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CANC_MERC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CANC_SERV | NUMBER(17,2) | Y |  |  |
| 14 | VLR_REV_PROV | NUMBER(17,2) | Y |  |  |
| 15 | VLR_EXP_MERC | NUMBER(17,2) | Y |  |  |
| 16 | VLR_PREST_PFJ | NUMBER(17,2) | Y |  |  |
| 17 | VLR_PREST_CONTA | NUMBER(17,2) | Y |  |  |
| 18 | VLR_VEND_EXP | NUMBER(17,2) | Y |  |  |
| 19 | VLR_AQUIS_BEM | NUMBER(17,2) | Y |  |  |
| 20 | VLR_AQUIS_FAB | NUMBER(17,2) | Y |  |  |
| 21 | VLR_AQUIS_SERV | NUMBER(17,2) | Y |  |  |
| 22 | VLR_CRED_EST | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ENER_ELET | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ALUG_MAQ | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ALUG_CONTA | NUMBER(17,2) | Y |  |  |
| 26 | VLR_DESP_FIN | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ENC_MAQ | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ENC_IMOV | NUMBER(17,2) | Y |  |  |
| 29 | VLR_BEM_DEV | NUMBER(17,2) | Y |  |  |
| 30 | VLR_BEM_INT | NUMBER(17,2) | Y |  |  |
| 31 | VLR_BEM_EXT | NUMBER(17,2) | Y |  |  |
| 32 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 33 | USUARIO | VARCHAR2(40) | Y |  |  |
| 34 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 35 | VLR_OPER_ISENTA | NUMBER(17,2) | Y |  |  |
| 36 | VLR_AQ_SERV_CON | NUMBER(17,2) | Y |  |  |
| 37 | VLR_DEV_COMP | NUMBER(17,2) | Y |  |  |
| 38 | VLR_BASE_ECF | NUMBER(17,2) | Y |  |  |
| 39 | VLR_BASE_SERV_C | NUMBER(17,2) | Y |  |  |
| 40 | VLR_CANC_SERV_C | NUMBER(17,2) | Y |  |  |
| 41 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |
| 42 | VLR_COF | NUMBER(17,2) | Y |  |  |
| 43 | VLR_BEM_DEV_ANT | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_COT_DEM_APUR: (COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP)

---

## COT_DEM_MONOFASICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMP | NUMBER(4) | N |  |  |
| 4 | MES_COMP | NUMBER(2) | N |  |  |
| 5 | SEQ_CLASSE | NUMBER(2) | N |  |  |
| 6 | COD_PARAM | NUMBER(3) | N |  |  |
| 7 | GRUPO_MONOF | NUMBER(2) | N |  |  |
| 8 | CLASSE_COF | NUMBER(3) | N |  |  |
| 9 | COD_NBM | VARCHAR2(10) | N |  |  |
| 10 | VLR_BASE_COF | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | VLR_COFS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMSS_CF | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, SEQ_CLASSE, COD_PARAM, GRUPO_MONOF, CLASSE_COF, COD_NBM

---

## COT_DOC_FRETE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | DATE | Y |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 10 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 11 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 14 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_COT_DOC_FRETE: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP)

---

## COT_DOC_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | DATE | Y |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 10 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 11 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 12 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 15 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 16 | DATA_EMISSAO | DATE | Y |  |  |
| 17 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 21 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | VLR_COFS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMSS_CF | NUMBER(17,2) | Y |  |  |
| 25 | DAT_DI | DATE | Y |  |  |
| 26 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_COT_DOC_MERC: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_NBM, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP)

---

## COT_DOC_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | DATE | Y |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | GRUPO_SERVICO | VARCHAR2(9) | Y |  |  |
| 10 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_IRRF | NUMBER(17,2) | Y |  |  |
| 15 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 18 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 19 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |

**Indexes**:
- IX_COT_DOC_SERV: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, GRUPO_SERVICO, COD_SERVICO)

---

## COT_GRP_CLASSE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_MONOF | NUMBER(2) | N |  |  |
| 2 | CLASSE_COF | NUMBER(3) | N |  |  |
| 3 | VALID_CLASSE | DATE | N |  |  |
| 4 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 5 | ALIQ_MONOFASICA | NUMBER(7,4) | Y |  |  |

**PK**: GRUPO_MONOF, CLASSE_COF, VALID_CLASSE

---

## COT_GRUPO_COF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_COF | NUMBER(2) | N |  |  |
| 2 | VALID_GRUPO | DATE | N |  |  |
| 3 | ALIQ_COF | NUMBER(7,4) | Y |  |  |
| 4 | ALIQ_CRED_INV | NUMBER(7,4) | Y |  |  |
| 5 | ALIQ_CRED_ALIM | NUMBER(7,4) | Y |  |  |

**PK**: GRUPO_COF, VALID_GRUPO

---

## COT_INF_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO_COMP | NUMBER(4) | N |  |  |
| 3 | MES_COMP | NUMBER(2) | N |  |  |
| 4 | VLR_COMP_DEB_COF | NUMBER(17,2) | Y |  |  |
| 5 | VLR_COMP_DEB_TR | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RES_ESP | NUMBER(17,2) | Y |  |  |
| 7 | DAT_PAGAM | DATE | Y |  |  |
| 8 | VLR_PAGAM | NUMBER(17,2) | Y |  |  |
| 9 | VLR_EST_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DEV_VEND | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SALD_CRED_AN | NUMBER(17,2) | Y |  |  |
| 12 | COD_ESTAB | VARCHAR2(6) | N | ' ' |  |
| 13 | VLR_DEV_VEND_ANT | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP

---

## COT_NBM_CLASSE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_MONOF | NUMBER(2) | N |  |  |
| 4 | CLASSE_COF | NUMBER(3) | N |  |  |
| 5 | VALID_CLASSE | DATE | N |  |  |
| 6 | COD_NBM | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_MONOF, CLASSE_COF, VALID_CLASSE, COD_NBM

**FKs**:
- GRUPO_MONOF, CLASSE_COF, VALID_CLASSE → COT_GRP_CLASSE(GRUPO_MONOF, CLASSE_COF, VALID_CLASSE)

---

## COT_PRT_GERAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | VLR_LIM_CRED_PR | NUMBER(17,2) | Y |  |  |
| 3 | IND_NCM_21 | CHAR(1) | Y |  |  |
| 4 | IND_NCM_23 | CHAR(1) | Y |  |  |
| 5 | IND_NCM_24 | CHAR(1) | Y |  |  |
| 6 | IND_NF_42 | CHAR(1) | Y |  |  |
| 7 | IND_NCM_812 | CHAR(1) | Y |  |  |
| 8 | IND_SALDO_815 | CHAR(1) | Y |  |  |
| 9 | IND_CONTA_815 | CHAR(1) | Y |  |  |
| 10 | IND_NCM_815 | CHAR(1) | Y |  |  |
| 11 | IND_DEV_VEND | CHAR(1) | Y |  |  |
| 12 | IND_COD_INDICE | CHAR(1) | Y |  |  |
| 13 | IND_NF_814 | CHAR(1) | Y |  |  |
| 14 | IND_DED_ICMS | CHAR(1) | Y |  |  |
| 15 | IND_DED_IPI | CHAR(1) | Y |  |  |
| 16 | IND_DED_ICMSS | CHAR(1) | Y |  |  |
| 17 | IND_DEV_COMP | CHAR(1) | Y |  |  |
| 18 | IND_CONS_IND | CHAR(1) | Y |  |  |
| 19 | COD_ESTAB | VARCHAR2(6) | N | ' ' |  |
| 20 | IND_CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 21 | IND_DED_COFS | CHAR(1) | Y |  |  |
| 22 | IND_DED_PIS_ST | CHAR(1) | Y | 'N' | Indicador de dedução do PIS-ST na base de calculo do COFINS, caso este campo seja S, o valor sera sempre deduzido da base |
| 23 | IND_DEV_VEND_ANT | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## COT_VEND_COM_EXP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | ANO_COMP | NUMBER(4) | Y |  |  |
| 3 | MES_COMP | NUMBER(2) | Y |  |  |
| 4 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 7 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 8 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 10 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 11 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_COF | NUMBER(17,2) | Y |  |  |
| 14 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 17 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |
| 19 | VLR_COFS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMSS_CF | NUMBER(17,2) | Y |  |  |
| 21 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_COT_VEND_COM_EX: (COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR)

---

