# Módulo: DIPI (DIPI) - 38 tabelas

## DIPI_APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | MES_DIPI | NUMBER(2) | N |  |  |
| 5 | NRO_DECENDIO | NUMBER(1) | N |  |  |
| 6 | TOT_DEBITOS | NUMBER(17,2) | Y |  |  |
| 7 | TOT_CREDITOS | NUMBER(17,2) | Y |  |  |
| 8 | SALDO_PER_ANT | NUMBER(17,2) | Y |  |  |
| 9 | SALDO_APURADO | NUMBER(17,2) | Y |  |  |
| 10 | IND_DEB_CRE | VARCHAR2(1) | Y |  |  |
| 11 | IND_PER_APURAC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, MES_DIPI, NRO_DECENDIO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_BEBIDAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO_COMPET | NUMBER(6) | N |  |  |
| 4 | COD_BEBIDA | VARCHAR2(5) | N |  |  |
| 5 | IND_ALCOOLICA | CHAR(1) | Y |  |  |
| 6 | VLR_IPI_UNID | NUMBER(19,4) | N |  |  |
| 7 | QTD_BEBIDA | NUMBER(17,6) | Y |  |  |
| 8 | VLR_DEB_IPI | NUMBER(17,2) | Y |  |  |
| 9 | DAT_APURAC | DATE | Y |  |  |
| 10 | MARCA | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO_COMPET, COD_BEBIDA, VLR_IPI_UNID

---

## DIPI_BEBIDAS_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_ANO_COMPET | NUMBER(6) | Y |  |  |
| 4 | COD_BEBIDA | VARCHAR2(5) | Y |  |  |
| 5 | IND_ALCOOLICA | CHAR(1) | Y |  |  |
| 6 | VLR_IPI_UNID | NUMBER(19,4) | Y |  |  |
| 7 | QTD_BEBIDA | NUMBER(17,6) | Y |  |  |
| 8 | VLR_DEB_IPI | NUMBER(17,2) | Y |  |  |
| 9 | DAT_APURAC | DATE | Y |  |  |
| 10 | MARCA | VARCHAR2(30) | Y |  |  |

---

## DIPI_BEB_CABECALHO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO_COMPET | NUMBER(6) | N |  |  |
| 4 | IND_EST_IND_EQUIP | CHAR(1) | Y |  |  |
| 5 | IND_DECL_NORM_RET | CHAR(1) | Y |  |  |
| 6 | QTD_ENERG_KWH | NUMBER(17,6) | Y |  |  |
| 7 | QTD_AGUA_KWH | NUMBER(17,6) | Y |  |  |
| 8 | COD_DECLARANTE | VARCHAR2(3) | Y |  |  |
| 9 | DAT_APURAC | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO_COMPET

---

## DIPI_BEB_CRED_IPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO_COMPET | NUMBER(6) | N |  |  |
| 4 | DSC_GRUPO_CRED | VARCHAR2(50) | N |  |  |
| 5 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |
| 6 | DAT_APURAC | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO_COMPET, DSC_GRUPO_CRED

---

## DIPI_BEB_CRED_NBM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO_PROD | VARCHAR2(2) | N |  |  |
| 2 | IDENT_NBM | NUMBER(12) | N |  |  |

**PK**: COD_GRUPO_PROD, IDENT_NBM

**FKs**:
- COD_GRUPO_PROD → DIPI_BEB_GR_CRED(COD_GRUPO_PROD)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)

---

## DIPI_BEB_CRED_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO_PROD | VARCHAR2(2) | N |  |  |
| 2 | IDENT_PRODUTO | NUMBER(12) | N |  |  |

**PK**: COD_GRUPO_PROD, IDENT_PRODUTO

**FKs**:
- COD_GRUPO_PROD → DIPI_BEB_GR_CRED(COD_GRUPO_PROD)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## DIPI_BEB_GR_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO_PROD | VARCHAR2(2) | N |  |  |
| 2 | DSC_NOMENCL | VARCHAR2(50) | Y |  |  |
| 3 | IND_PROD_NBM | CHAR(1) | Y |  |  |

**PK**: COD_GRUPO_PROD

---

## DIPI_BEB_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | CHAR(1) | N |  |  |
| 2 | IND_ALCOOLICA | CHAR(1) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 5 | DSC_OPER | VARCHAR2(50) | Y |  |  |

**PK**: COD_OPERACAO, IND_ALCOOLICA, COD_CFO

---

## DIPI_BEB_OPER_BK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | CHAR(1) | Y |  |  |
| 2 | IND_ALCOOLICA | CHAR(1) | Y |  |  |
| 3 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 5 | DSC_OPER | VARCHAR2(50) | Y |  |  |

---

## DIPI_BEB_OPER_EXT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | CHAR(1) | N |  |  |
| 2 | IND_ALCOOLICA | CHAR(1) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 7 | DSC_OPER | VARCHAR2(50) | Y |  |  |

**PK**: COD_OPERACAO, IND_ALCOOLICA, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## DIPI_BEB_PAUTA_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | IND_ALCOOLICA | CHAR(1) | Y |  |  |
| 5 | COD_COMP_NBM | VARCHAR2(4) | Y |  |  |
| 6 | VLR_PAUTA | NUMBER(19,4) | Y |  |  |
| 7 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 10 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 11 | MARCA | VARCHAR2(30) | Y |  |  |
| 12 | ESPECIE | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO

**FKs**:
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## DIPI_BEB_PFJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | CHAR(1) | N |  |  |
| 2 | IND_ALCOOLICA | CHAR(1) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | CPF_CGC | VARCHAR2(14) | N |  |  |

**PK**: COD_OPERACAO, IND_ALCOOLICA, COD_CFO, CPF_CGC

---

## DIPI_BEB_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | CHAR(1) | N |  |  |
| 2 | IND_ALCOOLICA | CHAR(1) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: COD_OPERACAO, IND_ALCOOLICA, COD_CFO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## DIPI_BEB_SELOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO_COMPET | NUMBER(6) | N |  |  |
| 4 | COD_SELO | NUMBER(2) | N |  |  |
| 5 | QTD_ADQUIRIDA | NUMBER(12) | Y |  |  |
| 6 | QTD_OUTRAS_ENTR | NUMBER(12) | Y |  |  |
| 7 | QTD_UTILIZADOS | NUMBER(12) | Y |  |  |
| 8 | QTD_OUTRAS_SAIDAS | NUMBER(12) | Y |  |  |
| 9 | QTD_SALDO | NUMBER(12) | Y |  |  |
| 10 | DAT_APURAC | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO_COMPET, COD_SELO

---

## DIPI_CLASSE_PAR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANO_VERSAO_DIPJ | NUMBER(4) | N |  |  |
| 2 | NUM_FICHA | NUMBER(2) | N |  |  |
| 3 | NUM_LINHA | NUMBER(2) | N |  |  |
| 4 | COD_CLASSE | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_PAR | CHAR(1) | N |  |  |
| 6 | NUM_COLUNA | VARCHAR2(6) | Y |  |  |
| 7 | DSC_FICHA | VARCHAR2(100) | Y |  |  |
| 8 | DSC_CLASSE | VARCHAR2(100) | Y |  |  |

**PK**: ANO_VERSAO_DIPJ, NUM_FICHA, NUM_LINHA, COD_CLASSE, IND_TP_PAR

---

## DIPI_CONTRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | NOME_CONTADOR | VARCHAR2(55) | Y |  |  |
| 5 | CPF_CONTADOR | VARCHAR2(11) | Y |  |  |
| 6 | CRC_CONTADOR | VARCHAR2(24) | Y |  |  |
| 7 | DDD_CONTADOR | VARCHAR2(4) | Y |  |  |
| 8 | TEL_CONTADOR | VARCHAR2(8) | Y |  |  |
| 9 | LOCAL_CONTADOR | VARCHAR2(30) | Y |  |  |
| 10 | REPRES_LEGAL | VARCHAR2(55) | Y |  |  |
| 11 | CPF_REPRES | VARCHAR2(11) | Y |  |  |
| 12 | DDD_REPRES | VARCHAR2(4) | Y |  |  |
| 13 | TEL_REPRES | VARCHAR2(8) | Y |  |  |
| 14 | LOCAL_REPRES | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_CRED_DEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | MES_DIPI | NUMBER(2) | N |  |  |
| 5 | N_ENT_INSUMO | NUMBER(17,2) | Y |  |  |
| 6 | N_ENT_COMER | NUMBER(17,2) | Y |  |  |
| 7 | E_ENT_INSUMO | NUMBER(17,2) | Y |  |  |
| 8 | E_ENT_COMER | NUMBER(17,2) | Y |  |  |
| 9 | DEV_VENDAS | NUMBER(17,2) | Y |  |  |
| 10 | OUTS_CREDITOS | NUMBER(17,2) | Y |  |  |
| 11 | TOT_DEM_CRED | NUMBER(17,2) | Y |  |  |
| 12 | CRE_PRES_IPI | NUMBER(17,2) | Y |  |  |
| 13 | INS_UTIL_FABRIC | NUMBER(17,2) | Y |  |  |
| 14 | INS_UTIL_FABRIC_MA | NUMBER(17,2) | Y |  |  |
| 15 | INS_UTIL_EXPORT | NUMBER(17,2) | Y |  |  |
| 16 | INS_VEN_SUSP_IPI | NUMBER(17,2) | Y |  |  |
| 17 | OUTS_CRED_INCEN | NUMBER(17,2) | Y |  |  |
| 18 | TOT_DEM_CRE_INCEN | NUMBER(17,2) | Y |  |  |
| 19 | N_PROD_EST | NUMBER(17,2) | Y |  |  |
| 20 | N_COMER_EST | NUMBER(17,2) | Y |  |  |
| 21 | OUTS_SAI_EST | NUMBER(17,2) | Y |  |  |
| 22 | ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 23 | RESSARC_CRED | NUMBER(17,2) | Y |  |  |
| 24 | OUTROS_DEB | NUMBER(17,2) | Y |  |  |
| 25 | TOT_DEM_DEB | NUMBER(17,2) | Y |  |  |
| 26 | VLR_CRED_REC_TRANS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_INS_PROD_POLIE | NUMBER(17,2) | Y |  |  |
| 28 | VLR_IND_PROD_INFO | NUMBER(17,2) | Y |  |  |
| 29 | VLR_CRED_CEXP | NUMBER(17,2) | Y |  |  |
| 30 | VLR_TRANS_CRED | NUMBER(17,2) | Y |  |  |
| 31 | DEV_VENDAS_EXT | NUMBER(17,2) | Y |  |  |
| 32 | DEV_COMPRAS | NUMBER(17,2) | Y |  |  |
| 33 | DEV_COMPRAS_EXT | NUMBER(17,2) | Y |  |  |
| 34 | ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 35 | RESSARC_CPRES | NUMBER(17,2) | Y |  |  |
| 36 | N_ENT_IND_OUT_EMP | NUMBER(17,2) | Y |  |  |
| 37 | N_SAI_IND_OUT_EMP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_DESTINATARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |
| 10 | IND_RELAC_INTER | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_FIS_JUR, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_DEST_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |
| 10 | IND_RELAC_INTER | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_FIS_JUR, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_0863: (IDENT_FIS_JUR)

---

## DIPI_ENTRADAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_NBM | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_NBM, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_ENTRADAS_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_NBM | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_NBM, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)

---

## DIPI_ENTRADAS_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_PRODUTO, MES_DIPI

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## DIPI_ENTR_PRD_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_PRODUTO, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## DIPI_E_S_PRD_NBM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_NBM | NUMBER(12) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | MES_DIPI | NUMBER(2) | N |  |  |
| 8 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 11 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_NBM, IDENT_PRODUTO, IND_E_S, MES_DIPI

**FKs**:
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## DIPI_E_S_PRD_NBM_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_NBM | NUMBER(12) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | MES_DIPI | NUMBER(2) | N |  |  |
| 8 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 11 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_NBM, IDENT_PRODUTO, IND_E_S, MES_DIPI

**FKs**:
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## DIPI_GERAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | SITUACAO_DIPI | CHAR(1) | Y |  |  |
| 5 | REG_ENGARRAFADOR | CHAR(1) | Y |  |  |
| 6 | NRO_REGISTRO | VARCHAR2(15) | Y |  |  |
| 7 | DATA_CONCESSAO | DATE | Y |  |  |
| 8 | CONVENIO_ICMS | CHAR(1) | Y |  |  |
| 9 | DATA_OPCAO | DATE | Y |  |  |
| 10 | CAIXA_POSTAL | NUMBER(6) | Y |  |  |
| 11 | DATA_ENTREGA | DATE | Y |  |  |
| 12 | IND_SUBSTITUTO | CHAR(1) | Y |  |  |
| 13 | IND_SUBSTITUIDO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIPI_HORAS_ENERGIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | PESSOAL_PROD | NUMBER(17,2) | Y |  |  |
| 5 | PESSOAL_FORA | NUMBER(17,2) | Y |  |  |
| 6 | ENERGIA_PROD | NUMBER(17,2) | Y |  |  |
| 7 | ENERGIA_ADQ | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_PAR_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSE | VARCHAR2(2) | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |
| 3 | IND_TP_PAR | CHAR(1) | N |  |  |
| 4 | ANO_VERSAO_DIPJ | NUMBER(4) | N |  |  |

**PK**: COD_CLASSE, COD_CFO, IND_TP_PAR, ANO_VERSAO_DIPJ

---

## DIPI_PAR_EXT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSE | VARCHAR2(2) | N |  |  |
| 2 | IND_TP_PAR | CHAR(1) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | ANO_VERSAO_DIPJ | NUMBER(4) | N |  |  |

**PK**: COD_CLASSE, IND_TP_PAR, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, ANO_VERSAO_DIPJ

---

## DIPI_REMETENTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |
| 10 | IND_RELAC_INTER | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_FIS_JUR, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_REMET_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |
| 10 | IND_RELAC_INTER | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_FIS_JUR, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_0909: (IDENT_FIS_JUR)

---

## DIPI_RES_ENTRADA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | MES_DIPI | NUMBER(2) | N |  |  |
| 5 | N_INS_C_CRED | NUMBER(17,2) | Y |  |  |
| 6 | N_MERC_C_CRED | NUMBER(17,2) | Y |  |  |
| 7 | N_OUT_C_CRED | NUMBER(17,2) | Y |  |  |
| 8 | E_INS_C_CRED | NUMBER(17,2) | Y |  |  |
| 9 | E_MERC_C_CRED | NUMBER(17,2) | Y |  |  |
| 10 | E_OUT_C_CRED | NUMBER(17,2) | Y |  |  |
| 11 | N_INS_S_CRED | NUMBER(17,2) | Y |  |  |
| 12 | N_MERC_S_CRED | NUMBER(17,2) | Y |  |  |
| 13 | N_OUT_S_CRED | NUMBER(17,2) | Y |  |  |
| 14 | E_INS_S_CRED | NUMBER(17,2) | Y |  |  |
| 15 | E_MERC_S_CRED | NUMBER(17,2) | Y |  |  |
| 16 | E_OUT_S_CRED | NUMBER(17,2) | Y |  |  |
| 17 | TOT_C_CRED | NUMBER(17,2) | Y |  |  |
| 18 | TOT_S_CRED | NUMBER(17,2) | Y |  |  |
| 19 | N_DEV_VENDA_CRE | NUMBER(17,2) | Y |  |  |
| 20 | N_DEV_VENDA_S_CRE | NUMBER(17,2) | Y |  |  |
| 21 | E_DEV_VENDA_CRE | NUMBER(17,2) | Y |  |  |
| 22 | E_DEV_VENDA_S_CRE | NUMBER(17,2) | Y |  |  |
| 23 | N_IND_OUT_EMP_CRE | NUMBER(17,2) | Y |  |  |
| 24 | N_IND_OUT_EMP_SCRE | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_RES_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | MES_DIPI | NUMBER(2) | N |  |  |
| 5 | N_PROD_DEB | NUMBER(17,2) | Y |  |  |
| 6 | N_COMER_DEB | NUMBER(17,2) | Y |  |  |
| 7 | N_OUT_DEB | NUMBER(17,2) | Y |  |  |
| 8 | N_PROD_S_DEB | NUMBER(17,2) | Y |  |  |
| 9 | N_COMER_S_DEB | NUMBER(17,2) | Y |  |  |
| 10 | N_OUT_S_DEB | NUMBER(17,2) | Y |  |  |
| 11 | E_PROD_S_DEB | NUMBER(17,2) | Y |  |  |
| 12 | E_COMER_S_DEB | NUMBER(17,2) | Y |  |  |
| 13 | E_OUT_S_DEB | NUMBER(17,2) | Y |  |  |
| 14 | TOT_C_DEB | NUMBER(17,2) | Y |  |  |
| 15 | TOT_S_DEB | NUMBER(17,2) | Y |  |  |
| 16 | N_DEV_COMPRA_DEB | NUMBER(17,2) | Y |  |  |
| 17 | N_DEV_COMPRA_S_DEB | NUMBER(17,2) | Y |  |  |
| 18 | E_DEV_COMPRA_S_DEB | NUMBER(17,2) | Y |  |  |
| 19 | N_IND_OUT_EMP_DEB | NUMBER(17,2) | Y |  |  |
| 20 | N_IND_OUT_EMP_SDEB | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_SAIDAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_NBM | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_NBM, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_DIPI → DIPI_GERAIS(COD_EMPRESA, COD_ESTAB, ANO_DIPI)

---

## DIPI_SAIDAS_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_NBM | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_NBM, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)

---

## DIPI_SAIDAS_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_PRODUTO, MES_DIPI

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## DIPI_SAIDAS_PRD_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_DIPI | NUMBER(4) | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | MES_DIPI | NUMBER(2) | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_DIPI, IDENT_PRODUTO, MES_DIPI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

