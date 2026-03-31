# Módulo: CMT (CMT) - 17 tabelas

## CMT_BALANCETE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTRUT_CONT | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_SALDO | DATE | N |  |  |
| 5 | COD_GRUPO_CONT | CHAR(1) | N |  |  |
| 6 | COD_SUBGRUPO_CONT | VARCHAR2(2) | N | ' ' |  |
| 7 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 8 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 9 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 10 | IND_SALDO_ANT | CHAR(1) | Y |  |  |
| 11 | VLR_DEB_MES | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CRED_MES | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SALDO_ATUAL | NUMBER(17,2) | Y |  |  |
| 14 | IND_SALDO_ATUAL | CHAR(1) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | COD_SUBGRUPO_CONT2 | VARCHAR2(2) | N | ' ' |  |
| 18 | COD_SUBGRUPO_CONT3 | VARCHAR2(2) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTRUT_CONT, COD_ESTAB, DAT_SALDO, COD_GRUPO_CONT, COD_SUBGRUPO_CONT, GRUPO_CONTA, COD_CONTA, COD_SUBGRUPO_CONT2, COD_SUBGRUPO_CONT3

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_ESTRUT_CONT, COD_GRUPO_CONT, COD_SUBGRUPO_CONT, COD_SUBGRUPO_CONT2, COD_SUBGRUPO_CONT3, GRUPO_CONTA, COD_CONTA → CMT_RELAC_GRUPO(COD_ESTRUT_CONT, COD_GRUPO_DEST, COD_SUBGRUPO_DEST, COD_SUBGRUPO_DEST2, COD_SUBGRUPO_DEST3, GRUPO_CONTA, COD_CONTA)

---

## CMT_DEMONSTR_EXERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_TIPO_LANCTO | CHAR(1) | N |  |  |
| 3 | COD_ESTR_AP | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURAC | DATE | N |  |  |
| 5 | NUM_ORDENACAO | NUMBER(12) | N |  |  |
| 6 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 7 | DSC_LANCTO | VARCHAR2(50) | Y |  |  |
| 8 | VLR_COLUNA_1 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_COLUNA_2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_COLUNA_3 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_COLUNA_4 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, IND_TIPO_LANCTO, COD_ESTR_AP, DAT_APURAC, NUM_ORDENACAO

**FKs**:
- COD_EMPRESA, COD_ESTR_AP → CMT_PAR_EXERC(COD_EMPRESA, COD_ESTR_AP)

---

## CMT_DIF_X40

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMPANHIA | VARCHAR2(10) | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE_X40 | CHAR(1) | Y |  |  |
| 6 | VLR_LANCTO_X40 | NUMBER(17,2) | Y |  |  |
| 7 | IND_DEB_CRE_X01 | CHAR(1) | Y |  |  |
| 8 | VLR_LANCTO_X01 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMPANHIA, IDENT_CONTA

---

## CMT_DIF_X41

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMPANHIA | VARCHAR2(10) | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_SALDO_INI_X41 | CHAR(1) | Y |  |  |
| 6 | VLR_SALDO_INI_X41 | NUMBER(17,2) | Y |  |  |
| 7 | IND_SALDO_INI_X02 | CHAR(1) | Y |  |  |
| 8 | VLR_SALDO_INI_X02 | NUMBER(17,2) | Y |  |  |
| 9 | IND_SALDO_FIM_X41 | CHAR(1) | Y |  |  |
| 10 | VLR_SALDO_FIM_X41 | NUMBER(17,2) | Y |  |  |
| 11 | IND_SALDO_FIM_X02 | CHAR(1) | Y |  |  |
| 12 | VLR_SALDO_FIM_X02 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TOT_CRE_X41 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOT_CRE_X02 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TOT_DEB_X41 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_DEB_X02 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMPANHIA, IDENT_CONTA

---

## CMT_ESTRUT_CONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTRUT_CONT | VARCHAR2(3) | N |  |  |
| 2 | DSC_ESTRUT_CONT | VARCHAR2(50) | Y |  |  |

**PK**: COD_ESTRUT_CONT

---

## CMT_ESTRUT_REL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | NUM_ITEM | NUMBER(3) | N |  |  |
| 3 | IND_TIPO_LINHA | CHAR(1) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(70) | Y |  |  |
| 6 | NOME_COLUNA_1 | VARCHAR2(20) | Y |  |  |
| 7 | NOME_COLUNA_2 | VARCHAR2(20) | Y |  |  |
| 8 | NOME_COLUNA_3 | VARCHAR2(20) | Y |  |  |
| 9 | VLR_COLUNA_1 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_COLUNA_2 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_COLUNA_3 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, NUM_ITEM

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## CMT_GRUPO_CONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTRUT_CONT | VARCHAR2(3) | N |  |  |
| 2 | COD_GRUPO_CONT | CHAR(1) | N |  |  |
| 3 | DSC_GRUPO_CONT | VARCHAR2(50) | Y |  |  |

**PK**: COD_ESTRUT_CONT, COD_GRUPO_CONT

**FKs**:
- COD_ESTRUT_CONT → CMT_ESTRUT_CONT(COD_ESTRUT_CONT)

---

## CMT_PAR_CONSOL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 2 | COD_OPERACAO | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 4 | HISTORICO | VARCHAR2(50) | Y |  |  |

**PK**: GRUPO_OPERACAO, COD_OPERACAO, COD_CONTA

---

## CMT_PAR_EXERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTR_AP | VARCHAR2(3) | N |  |  |
| 3 | DSC_ESTR_AP | VARCHAR2(100) | Y |  |  |
| 4 | OPERACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTR_AP

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## CMT_PAR_EXERC_AUT1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_TIPO_REL | CHAR(1) | N |  |  |
| 3 | COD_ITEM | VARCHAR2(10) | N |  |  |
| 4 | DSC_ITEM | VARCHAR2(50) | Y |  |  |
| 5 | IND_NIVEL | CHAR(1) | Y |  |  |
| 6 | IND_NATUREZA | CHAR(1) | Y |  |  |
| 7 | IND_OPERADOR | CHAR(1) | Y |  |  |
| 8 | IND_SALDO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, IND_TIPO_REL, COD_ITEM

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## CMT_PAR_EXERC_AUT2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_TIPO_REL | CHAR(1) | N |  |  |
| 3 | COD_ITEM | VARCHAR2(10) | N |  |  |
| 4 | COD_ITEM_FORMULA | VARCHAR2(10) | N |  |  |
| 5 | IND_OPER_FORMULA | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, IND_TIPO_REL, COD_ITEM, COD_ITEM_FORMULA

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## CMT_PAR_EXERC_AUT3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_TIPO_REL | CHAR(1) | N |  |  |
| 3 | COD_ITEM | VARCHAR2(10) | N |  |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 6 | IND_OPERADOR | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, IND_TIPO_REL, COD_ITEM, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## CMT_PAR_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 4 | COD_OPERACAO | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_OPERACAO, COD_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CMT_RELAC_GRUPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTRUT_CONT | VARCHAR2(3) | N |  |  |
| 2 | COD_GRUPO_DEST | CHAR(1) | N |  |  |
| 3 | COD_SUBGRUPO_DEST | VARCHAR2(2) | N | ' ' |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 6 | COD_GRUPO_OR | CHAR(1) | Y | ' ' |  |
| 7 | COD_SUBGRUPO_OR | VARCHAR2(2) | Y | ' ' |  |
| 8 | IND_TP_CONTA | CHAR(1) | Y |  |  |
| 9 | COD_SUBGRUPO_DEST2 | VARCHAR2(2) | N | ' ' |  |
| 10 | COD_SUBGRUPO_DEST3 | VARCHAR2(2) | N | ' ' |  |
| 11 | COD_SUBGRUPO_OR2 | VARCHAR2(2) | Y | ' ' |  |
| 12 | COD_SUBGRUPO_OR3 | VARCHAR2(2) | Y | ' ' |  |

**PK**: COD_ESTRUT_CONT, COD_GRUPO_DEST, COD_SUBGRUPO_DEST, COD_SUBGRUPO_DEST2, COD_SUBGRUPO_DEST3, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_ESTRUT_CONT, COD_GRUPO_DEST → CMT_GRUPO_CONT(COD_ESTRUT_CONT, COD_GRUPO_CONT)

**Indexes**:
- IX_CMT_RELAC_GRUPO: (COD_ESTRUT_CONT, COD_GRUPO_OR, COD_SUBGRUPO_OR, GRUPO_CONTA, COD_CONTA)

---

## CMT_REL_BAL_ESTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_SALDO | DATE | N |  |  |
| 4 | CHAVE_ORD | NUMBER(5) | N |  |  |
| 5 | IND_TIPO_LINHA | VARCHAR2(3) | Y |  |  |
| 6 | CONTA | VARCHAR2(1000) | Y |  |  |
| 7 | SALDO_ANTERIOR | NUMBER(17,2) | Y |  |  |
| 8 | DEB_MES | NUMBER(17,2) | Y |  |  |
| 9 | CRE_MES | NUMBER(17,2) | Y |  |  |
| 10 | SALDO_ATUAL | NUMBER(17,2) | Y |  |  |
| 11 | IND_SALDO_ANTERIOR | CHAR(1) | Y |  |  |
| 12 | IND_SALDO_ATUAL | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_SALDO, CHAVE_ORD

---

## CMT_RES_DEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_TIPO_REL | CHAR(1) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | SEQ_LINHA | NUMBER(3) | N |  |  |
| 5 | COD_ITEM | VARCHAR2(10) | Y |  |  |
| 6 | DSC_ITEM | VARCHAR2(50) | Y |  |  |
| 7 | VLR_SALDO | NUMBER(17,2) | Y |  |  |
| 8 | IND_TOTAL | CHAR(1) | Y |  |  |
| 9 | IND_RESULTADO | CHAR(1) | Y |  |  |
| 10 | IND_NIVEL | CHAR(1) | Y |  |  |
| 11 | IND_OPERADOR | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, IND_TIPO_REL, DAT_APURACAO, SEQ_LINHA

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## CMT_SUBGRUPO_CONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTRUT_CONT | VARCHAR2(3) | N |  |  |
| 2 | COD_GRUPO_CONT | CHAR(1) | N |  |  |
| 3 | COD_SUBGRUPO_CONT | VARCHAR2(2) | N |  |  |
| 4 | DSC_SUBGRUPO_CONT | VARCHAR2(50) | Y |  |  |
| 5 | COD_SUBGRUPO_CONT2 | VARCHAR2(2) | N | ' ' |  |
| 6 | COD_SUBGRUPO_CONT3 | VARCHAR2(2) | N | ' ' |  |
| 7 | DSC_SUBGRUPO_CONT2 | VARCHAR2(50) | Y |  |  |
| 8 | DSC_SUBGRUPO_CONT3 | VARCHAR2(50) | Y |  |  |

**PK**: COD_ESTRUT_CONT, COD_GRUPO_CONT, COD_SUBGRUPO_CONT, COD_SUBGRUPO_CONT2, COD_SUBGRUPO_CONT3

**FKs**:
- COD_ESTRUT_CONT, COD_GRUPO_CONT → CMT_GRUPO_CONT(COD_ESTRUT_CONT, COD_GRUPO_CONT)

---

