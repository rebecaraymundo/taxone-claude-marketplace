# Módulo: DAC (DAC) - 11 tabelas

## DAC_GRUPO_PRODUTOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_ALIQUOTA_PROD | VARCHAR2(1) | N |  |  |
| 2 | GRUPO_PRODUTO_DACON | VARCHAR2(2) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: TIPO_ALIQUOTA_PROD, GRUPO_PRODUTO_DACON

---

## DAC_LINHAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_LINHA | NUMBER(3) | N |  |  |
| 2 | DSC_LINHA | VARCHAR2(100) | Y |  |  |
| 3 | MERCADO | CHAR(1) | Y |  |  |
| 4 | IND_VALOR | CHAR(1) | Y |  |  |

**PK**: NUM_LINHA

---

## DAC_LINHAS_COFINS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_LINHA | NUMBER(3) | N |  |  |
| 2 | COD_PARAM | NUMBER(3) | N |  |  |

**PK**: NUM_LINHA, COD_PARAM

**FKs**:
- NUM_LINHA → DAC_LINHAS(NUM_LINHA)

---

## DAC_LINHAS_PIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_LINHA | NUMBER(3) | N |  |  |
| 2 | COD_PARAM | NUMBER(3) | N |  |  |

**PK**: NUM_LINHA, COD_PARAM

**FKs**:
- NUM_LINHA → DAC_LINHAS(NUM_LINHA)

---

## DAC_LINHAS_VALOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | MES_ANO | DATE | N |  |  |
| 3 | NUM_LINHA | NUMBER(3) | N |  |  |
| 4 | VALOR | NUMBER(17,2) | Y | 0 |  |
| 5 | VALOR_EXTERNO | NUMBER(17,2) | Y | 0 |  |

**PK**: COD_EMPRESA, MES_ANO, NUM_LINHA

**FKs**:
- NUM_LINHA → DAC_LINHAS(NUM_LINHA)

---

## DAC_LINHA_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | NUM_LINHA | NUMBER(3) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | MERCADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, NUM_LINHA, COD_CFO

**FKs**:
- NUM_LINHA → DAC_LINHAS(NUM_LINHA)

---

## DAC_LINHA_CONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | NUM_LINHA | NUMBER(3) | N |  |  |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | MERCADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, NUM_LINHA, GRUPO_CONTA, COD_CONTA

**FKs**:
- NUM_LINHA → DAC_LINHAS(NUM_LINHA)

---

## DAC_LINHA_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | NUM_LINHA | NUMBER(3) | N |  |  |
| 3 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 4 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 5 | MERCADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, NUM_LINHA, GRUPO_SERVICO, COD_SERVICO

**FKs**:
- NUM_LINHA → DAC_LINHAS(NUM_LINHA)

---

## DAC_PARAM_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VERSAO | VARCHAR2(30) | N |  |  |
| 2 | NUM_FICHA | VARCHAR2(3) | N |  |  |
| 3 | NUM_LINHA | NUMBER(2) | N |  |  |
| 4 | IND_DET_SEPAR | CHAR(1) | N |  |  |
| 5 | TIPO_ORIGEN_CRED | VARCHAR2(2) | N |  |  |

**PK**: VERSAO, NUM_FICHA, NUM_LINHA, IND_DET_SEPAR, TIPO_ORIGEN_CRED

---

## DAC_PRODUTOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PRODUTO_DACON | VARCHAR2(10) | N |  |  |
| 2 | GRUPO_PRODUTO_DACON | VARCHAR2(2) | Y |  |  |
| 3 | TIPO_ALIQUOTA_PROD | VARCHAR2(1) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_PRODUTO_DACON

**FKs**:
- TIPO_ALIQUOTA_PROD, GRUPO_PRODUTO_DACON → DAC_GRUPO_PRODUTOS(TIPO_ALIQUOTA_PROD, GRUPO_PRODUTO_DACON)

---

## DAC_VALOR_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | VERSAO | VARCHAR2(30) | N |  |  |
| 3 | MESANO | NUMBER(6) | N |  |  |
| 4 | TIPO_ORIGEM_CRED | VARCHAR2(2) | N |  |  |
| 5 | TRIBUTO | VARCHAR2(6) | N |  | P - Pis , C - Cofins |
| 6 | MESANO_USO | NUMBER(6) | Y |  |  |
| 7 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |
| 8 | SEQUENCIAL | NUMBER(2) | N | 1 |  |
| 9 | IND_TP_UTIL_CRED | CHAR(1) | N | 'T' |  |

**PK**: COD_EMPRESA, VERSAO, MESANO, TIPO_ORIGEM_CRED, TRIBUTO, SEQUENCIAL

---

