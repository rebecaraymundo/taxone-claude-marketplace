# Módulo: DIF (DIF) - 15 tabelas

## DIF_BEB_EST_INSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | DECENDIO | CHAR(1) | N |  |  |
| 6 | COD_INSUMO | NUMBER(3) | N |  |  |
| 7 | CAPACIDADE | NUMBER(5) | N |  |  |
| 8 | IDENT_NBM | NUMBER(12) | N |  |  |
| 9 | VLR_ESTOQ_INI | NUMBER(17,6) | Y |  |  |
| 10 | VLR_INS_ADQUIR | NUMBER(17,6) | Y |  |  |
| 11 | VLR_INS_REC_TRAN | NUMBER(17,6) | Y |  |  |
| 12 | VLR_INS_REC_IND | NUMBER(17,6) | Y |  |  |
| 13 | VLR_INS_OUTR_ENT | NUMBER(17,6) | Y |  |  |
| 14 | VLR_INS_UTILIZ | NUMBER(17,6) | Y |  |  |
| 15 | VLR_INS_INUTILIZ | NUMBER(17,6) | Y |  |  |
| 16 | VLR_INS_REVEND | NUMBER(17,6) | Y |  |  |
| 17 | VLR_INS_TRANSFER | NUMBER(17,6) | Y |  |  |
| 18 | VLR_INS_OUTR_SAI | NUMBER(17,6) | Y |  |  |
| 19 | VLR_ESTOQ_FINAL | NUMBER(17,6) | Y |  |  |
| 20 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, COD_INSUMO, CAPACIDADE, IDENT_NBM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_INSUMO → DIF_BEB_INSUMO(COD_INSUMO)

---

## DIF_BEB_EST_INSUMO_A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | DECENDIO | CHAR(1) | N |  |  |
| 6 | COD_INSUMO | NUMBER(3) | N |  |  |
| 7 | CAPACIDADE | NUMBER(5) | N |  |  |
| 8 | IDENT_NBM | NUMBER(12) | N |  |  |
| 9 | DATA_LANCAMENTO | DATE | N |  |  |
| 10 | VLR_ESTOQ_INI | NUMBER(17,6) | Y |  |  |
| 11 | VLR_INS_ADQUIR | NUMBER(17,6) | Y |  |  |
| 12 | VLR_INS_REC_TRAN | NUMBER(17,6) | Y |  |  |
| 13 | VLR_INS_REC_IND | NUMBER(17,6) | Y |  |  |
| 14 | VLR_INS_OUTR_ENT | NUMBER(17,6) | Y |  |  |
| 15 | VLR_INS_UTILIZ | NUMBER(17,6) | Y |  |  |
| 16 | VLR_INS_INUTILIZ | NUMBER(17,6) | Y |  |  |
| 17 | VLR_INS_REVEND | NUMBER(17,6) | Y |  |  |
| 18 | VLR_INS_TRANSFER | NUMBER(17,6) | Y |  |  |
| 19 | VLR_INS_OUTR_SAI | NUMBER(17,6) | Y |  |  |
| 20 | VLR_ESTOQ_FINAL | NUMBER(17,6) | Y |  |  |
| 21 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, COD_INSUMO, CAPACIDADE, IDENT_NBM, DATA_LANCAMENTO

**FKs**:
- COD_INSUMO → DIF_BEB_INSUMO(COD_INSUMO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIF_BEB_EST_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | DECENDIO | CHAR(1) | N |  |  |
| 6 | COD_SRF | NUMBER(6) | N |  |  |
| 7 | VLR_PRECO_MED | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ESTOQ_INI | NUMBER(17,6) | Y |  |  |
| 9 | VLR_PROD_ENV | NUMBER(17,6) | Y |  |  |
| 10 | VLR_PROD_REC_TRAN | NUMBER(17,6) | Y |  |  |
| 11 | VLR_PROD_DEV | NUMBER(17,6) | Y |  |  |
| 12 | VLR_PROD_OUTR_ENT | NUMBER(17,6) | Y |  |  |
| 13 | VLR_PROD_VEND | NUMBER(17,6) | Y |  |  |
| 14 | VLR_PROD_APREND | NUMBER(17,6) | Y |  |  |
| 15 | VLR_PROD_TRANSF | NUMBER(17,6) | Y |  |  |
| 16 | VLR_PROD_INUTILIZ | NUMBER(17,6) | Y |  |  |
| 17 | VLR_PROD_OUTR_SAI | NUMBER(17,6) | Y |  |  |
| 18 | VLR_ESTOQ_FINAL | NUMBER(17,6) | Y |  |  |
| 19 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, COD_SRF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIF_BEB_EST_PROD_A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | DECENDIO | CHAR(1) | N |  |  |
| 6 | COD_SRF | NUMBER(6) | N |  |  |
| 7 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 8 | IND_PRODUTO | CHAR(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 10 | DATA_LANCAMENTO | DATE | N |  |  |
| 11 | VLR_PRECO_MED | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ESTOQ_INI | NUMBER(17,6) | Y |  |  |
| 13 | VLR_PROD_ENV | NUMBER(17,6) | Y |  |  |
| 14 | VLR_PROD_REC_TRAN | NUMBER(17,6) | Y |  |  |
| 15 | VLR_PROD_DEV | NUMBER(17,6) | Y |  |  |
| 16 | VLR_PROD_OUTR_ENT | NUMBER(17,6) | Y |  |  |
| 17 | VLR_PROD_VEND | NUMBER(17,6) | Y |  |  |
| 18 | VLR_PROD_APREND | NUMBER(17,6) | Y |  |  |
| 19 | VLR_PROD_TRANSF | NUMBER(17,6) | Y |  |  |
| 20 | VLR_PROD_INUTILIZ | NUMBER(17,6) | Y |  |  |
| 21 | VLR_PROD_OUTR_SAI | NUMBER(17,6) | Y |  |  |
| 22 | VLR_ESTOQ_FINAL | NUMBER(17,6) | Y |  |  |
| 23 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, COD_SRF, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_LANCAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIF_BEB_INSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INSUMO | NUMBER(3) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(80) | Y |  |  |
| 3 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 4 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |

**PK**: COD_INSUMO

---

## DIF_BEB_ITEM_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | DECENDIO | CHAR(1) | N |  |  |
| 6 | IND_TIPO_NF | CHAR(1) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | DATA_EMISSAO | DATE | N |  |  |
| 11 | NUM_ITEM | NUMBER(5) | N |  |  |
| 12 | COD_INSUMO | NUMBER(3) | Y |  |  |
| 13 | CAPACIDADE | NUMBER(5) | Y |  |  |
| 14 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 15 | IDENT_CFOP | NUMBER(12) | Y |  |  |
| 16 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 17 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 18 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 19 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 20 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 21 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 23 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 24 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | USUARIO | VARCHAR2(40) | Y |  |  |
| 26 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, IND_TIPO_NF, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, DATA_EMISSAO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, IND_TIPO_NF, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, DATA_EMISSAO → DIF_BEB_NF(COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, IND_TIPO_NF, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, DATA_EMISSAO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1901: (IDENT_FIS_JUR)

---

## DIF_BEB_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | DECENDIO | CHAR(1) | N |  |  |
| 6 | IND_TIPO_NF | CHAR(1) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | DATA_EMISSAO | DATE | N |  |  |
| 11 | DATA_ENTRADA | DATE | Y |  |  |
| 12 | IDENT_CFOP | NUMBER(12) | Y |  |  |
| 13 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_PROD | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TOT_IPI | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TOT_NF | NUMBER(17,2) | Y |  |  |
| 19 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, IND_TIPO_NF, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, DATA_EMISSAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1899: (IDENT_FIS_JUR)

---

## DIF_BEB_PAR_EMPR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_TIPO_APUR | CHAR(1) | Y |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 4 | IND_NCM | CHAR(1) | Y |  |  |
| 5 | IND_CONV_MED | CHAR(1) | Y |  |  |
| 6 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 7 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 8 | IND_NCM_SEM_PROD | CHAR(1) | Y | 'N' | Recuperar movimentos de insumos de Notas Fiscais/Estoque, a partir de NCM, sem utilizar parametrização por produto |

**PK**: COD_EMPRESA

---

## DIF_BEB_PRD_INSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_INSUMO | NUMBER(3) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | CAPACIDADE | NUMBER(5) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_INSUMO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, CAPACIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIF_BEB_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | COD_SRF | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIF_BEB_PROD_EXC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | COD_PARAM | NUMBER(3) | N |  |  |
| 7 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 8 | COD_OPERACAO | VARCHAR2(9) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_PARAM, GRUPO_OPERACAO, COD_OPERACAO

---

## DIF_BEB_RESUMO_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | DECENDIO | CHAR(1) | N |  |  |
| 6 | IND_ENTRADA_SAIDA | CHAR(1) | N |  |  |
| 7 | IDENT_CFO | NUMBER(12) | N |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISENTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 13 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO, IND_ENTRADA_SAIDA, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## DIF_BEB_RES_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | DECENDIO | CHAR(1) | N |  |  |
| 6 | VLR_E_MERC_NAC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_E_MERC_EXT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_S_MERC_EXT | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTROS_CRED | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SUB_TOTAL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_SALDO_CRED_ANT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TOT_CRED_IMP | NUMBER(17,2) | Y |  |  |
| 14 | VLR_S_MERC_NAC | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 16 | VLR_RESS_CRED | NUMBER(17,2) | Y |  |  |
| 17 | VLR_OUTROS_DEB | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TOT_DEB_IMP | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOTAL_DEB | NUMBER(17,2) | Y |  |  |
| 20 | VLR_TOTAL_CRED | NUMBER(17,2) | Y |  |  |
| 21 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 22 | VLR_SALDO_DEV | NUMBER(17,2) | Y |  |  |
| 23 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO, DECENDIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIF_PAP_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO_INI | VARCHAR2(60) | N |  |  |
| 6 | COD_PRODUTO_FIM | VARCHAR2(60) | Y |  |  |
| 7 | IND_EXCECAO | CHAR(1) | Y |  |  |
| 8 | COD_TP_PROD | NUMBER(5) | Y |  |  |
| 9 | IND_TP_PROD | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIF_PAP_PROD_EXC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO_INI | VARCHAR2(60) | N |  |  |
| 6 | COD_PRODUTO_EXC | VARCHAR2(60) | N |  |  |
| 7 | COD_TP_PROD | NUMBER(5) | Y |  |  |
| 8 | IND_TP_PROD | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI, COD_PRODUTO_EXC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

