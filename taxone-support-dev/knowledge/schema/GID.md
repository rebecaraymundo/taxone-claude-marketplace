# Módulo: GID (GID) - 14 tabelas

## GID_CONTAS_EST_LALUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANO_LALUR | NUMBER(4) | N |  |  |
| 2 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 3 | DSC_CONTA_LALUR | VARCHAR2(255) | Y |  |  |
| 4 | TIPO_CONTA | NUMBER(1) | Y |  |  |
| 5 | IND_GERACAO_GID | CHAR(1) | Y |  |  |
| 6 | IND_NATUREZA_LALUR | CHAR(1) | Y |  | 3 - Despesa; 4 - Receita |

**PK**: ANO_LALUR, COD_CONTA_LALUR

---

## GID_CONTAS_LALUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANO_LALUR | NUMBER(4) | N |  |  |
| 2 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 3 | DSC_CONTA_LALUR | VARCHAR2(255) | Y |  |  |
| 4 | TIPO_LANC | NUMBER(2) | Y |  |  |
| 5 | TIPO_CONTA | NUMBER(1) | Y |  |  |
| 6 | IND_GERACAO_GID | CHAR(1) | Y |  |  |

**PK**: ANO_LALUR, COD_CONTA_LALUR

---

## GID_CONTAS_LALUR_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANO_LALUR | NUMBER(4) | Y |  |  |
| 2 | COD_CONTA_LALUR | VARCHAR2(3) | Y |  |  |
| 3 | DSC_CONTA_LALUR | VARCHAR2(255) | Y |  |  |
| 4 | TIPO_LANC | NUMBER(2) | Y |  |  |
| 5 | TIPO_CONTA | NUMBER(1) | Y |  |  |
| 6 | IND_GERACAO_GID | CHAR(1) | Y |  |  |

---

## GID_CONTAS_PROVISAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | VLR_ADICAO | NUMBER(17,2) | Y | 0 |  |
| 6 | VLR_EXCLUSAO | NUMBER(17,2) | Y | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_LALUR, DATA_SALDO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## GID_CONTAS_PROVISAO_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | VLR_ADICAO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_EXCLUSAO | NUMBER(17,2) | Y |  |  |

---

## GID_MAN_NUM_ORD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_PER | DATE | N |  |  |
| 4 | DATA_FIM_PER | DATE | N |  |  |
| 5 | NUM_ORD | VARCHAR2(8) | N |  |  |
| 6 | ANO | NUMBER(4) | Y |  |  |
| 7 | PER_INI | NUMBER(2) | Y |  |  |
| 8 | PER_FIM | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI_PER, DATA_FIM_PER, NUM_ORD

---

## GID_PAR_VIEWS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | PERIODICIDADE | CHAR(1) | N |  |  |
| 3 | ENCERRAMENTO | CHAR(1) | N |  |  |
| 4 | QTD_ANO | NUMBER(2) | Y |  |  |
| 5 | IND_UTIL_CC | CHAR(1) | Y | 'N' | Indicador de utilizacao de Centro de Custo |

**PK**: COD_EMPRESA

---

## GID_RELAC_CONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 5 | DSC_CONTA_LALUR | VARCHAR2(255) | Y |  |  |
| 6 | TIPO_LANC | NUMBER(2) | Y |  |  |
| 7 | COD_MSAF | VARCHAR2(20) | Y |  |  |
| 8 | DSC_MSAF | VARCHAR2(255) | Y |  |  |
| 9 | TIPO_SALDO | CHAR(1) | Y |  |  |
| 10 | PARTE_A | CHAR(1) | Y |  |  |
| 11 | PARTE_B | CHAR(1) | Y |  |  |
| 12 | IND_ATIVO | CHAR(1) | Y |  |  |
| 13 | ANO_LALUR | NUMBER(4) | N | 2004 |  |
| 14 | IND_CONTA_REDUZIDA | CHAR(1) | Y | 'N' |  |
| 15 | IND_PROVISAO_REVERSAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_LALUR, COD_CONTA_LALUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- GRUPO_CONTA → GRUPO_ESTAB(GRUPO_ESTAB)

---

## GID_RELAC_CONTAS_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA_LALUR | VARCHAR2(3) | Y |  |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 5 | DSC_CONTA_LALUR | VARCHAR2(255) | Y |  |  |
| 6 | TIPO_LANC | NUMBER(2) | Y |  |  |
| 7 | COD_MSAF | VARCHAR2(20) | Y |  |  |
| 8 | DSC_MSAF | VARCHAR2(255) | Y |  |  |
| 9 | EXPRESSAO | VARCHAR2(3000) | Y |  |  |
| 10 | TIPO_SALDO | CHAR(1) | Y |  |  |
| 11 | PARTE_A | CHAR(1) | Y |  |  |
| 12 | PARTE_B | CHAR(1) | Y |  |  |
| 13 | IND_ATIVO | CHAR(1) | Y |  |  |
| 14 | EXPRESSAO_PLSQL | VARCHAR2(4000) | Y |  |  |
| 15 | ANO_LALUR | NUMBER(4) | Y |  |  |
| 16 | IND_CONTA_REDUZIDA | CHAR(1) | Y |  |  |

---

## GID_RELAC_CONTAS_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA_LALUR | VARCHAR2(3) | Y |  |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 5 | DSC_CONTA_LALUR | VARCHAR2(255) | Y |  |  |
| 6 | TIPO_LANC | NUMBER(2) | Y |  |  |
| 7 | COD_MSAF | VARCHAR2(20) | Y |  |  |
| 8 | DSC_MSAF | VARCHAR2(255) | Y |  |  |
| 9 | TIPO_SALDO | CHAR(1) | Y |  |  |
| 10 | PARTE_A | CHAR(1) | Y |  |  |
| 11 | PARTE_B | CHAR(1) | Y |  |  |
| 12 | IND_ATIVO | CHAR(1) | Y |  |  |
| 13 | ANO_LALUR | NUMBER(4) | Y |  |  |
| 14 | IND_CONTA_REDUZIDA | CHAR(1) | Y |  |  |
| 15 | IND_PROVISAO_REVERSAO | CHAR(1) | Y |  |  |

---

## GID_RELAC_CONTAS_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_LALUR | NUMBER(4) | N |  |  |
| 4 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 5 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 6 | IND_ATIVO | CHAR(1) | Y |  |  |
| 7 | IND_CONTA_REDUZIDA | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_LALUR, COD_CONTA_LALUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- GRUPO_CONTA → GRUPO_ESTAB(GRUPO_ESTAB)
- ANO_LALUR, COD_CONTA_LALUR → GID_CONTAS_EST_LALUR(ANO_LALUR, COD_CONTA_LALUR)

---

## GID_RELAC_CONTAS_PARCELAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_LALUR | NUMBER(4) | N |  |  |
| 4 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 5 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 6 | OPERANDO | CHAR(1) | Y |  |  |
| 7 | PARCELA | VARCHAR2(80) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_LALUR, COD_CONTA_LALUR, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, ANO_LALUR, COD_CONTA_LALUR → GID_RELAC_CONTAS(COD_EMPRESA, COD_ESTAB, ANO_LALUR, COD_CONTA_LALUR)

---

## GID_RELAC_CONTAS_PARCELAS_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_LALUR | NUMBER(4) | N |  |  |
| 4 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 5 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 6 | OPERANDO | CHAR(1) | Y |  |  |
| 7 | PARCELA | VARCHAR2(80) | N |  |  |

---

## GID_RELAC_CONTAS_PARCELAS_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_LALUR | NUMBER(4) | N |  |  |
| 4 | COD_CONTA_LALUR | VARCHAR2(3) | N |  |  |
| 5 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 6 | OPERANDO | CHAR(1) | Y |  |  |
| 7 | PARCELA | VARCHAR2(80) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_LALUR, COD_CONTA_LALUR, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, ANO_LALUR, COD_CONTA_LALUR → GID_RELAC_CONTAS_EST(COD_EMPRESA, COD_ESTAB, ANO_LALUR, COD_CONTA_LALUR)

---

