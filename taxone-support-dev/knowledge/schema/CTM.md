# Módulo: CTM (CTM) - 13 tabelas

## CTM_CONCILIACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 8 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 9 | IND_FIS_JUR | VARCHAR2(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 16 | VLR_TOT_NOTA_MSAF | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TOT_NOTA_CONC | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TOT_NOTA_DIF | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_MSAF | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS_CONC | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_DIF | NUMBER(17,2) | Y |  |  |
| 22 | COD_OCORRENCIA | NUMBER(2) | Y |  |  |
| 23 | VLR_TOT_MIN | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TOT_MAX | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMS_MIN | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMS_MAX | NUMBER(17,2) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, GRUPO_DOCTO, COD_DOCTO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CTM_CONF_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | DATE | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | COD_CFO_ANT | VARCHAR2(4) | Y |  |  |
| 10 | COD_CFO_NOVO | VARCHAR2(4) | Y |  |  |
| 11 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 12 | IND_HOMOLOG_UF | CHAR(1) | Y |  |  |
| 13 | OCORRENCIA | VARCHAR2(2) | Y |  |  |

**Indexes**:
- IX_CTM_CONF_NF: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## CTM_CONSIST_ANALIT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INTERFACE | NUMBER(3) | Y |  |  |
| 2 | COD_PROG | NUMBER(12) | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | DAT_IMPORT | DATE | Y |  |  |
| 6 | DAT_MOVTO | DATE | Y |  |  |
| 7 | COD_TABELA | VARCHAR2(8) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | COD_OCORRENCIA | NUMBER(2) | Y |  |  |
| 10 | QTD_REG_LIDOS | NUMBER(9) | Y |  |  |
| 11 | QTD_REG_GRAVADOS | NUMBER(9) | Y |  |  |
| 12 | QTD_REG_ERROS | NUMBER(9) | Y |  |  |
| 13 | QTD_REG_REPROC | NUMBER(9) | Y |  |  |
| 14 | QTD_REG_IGNORADOS | NUMBER(9) | Y |  |  |

**Indexes**:
- IX_CTM_CONSIST_ANALIT: (COD_INTERFACE, COD_PROG, COD_EMPRESA, COD_ESTAB, DAT_IMPORT)

---

## CTM_ESTAB_CENTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## CTM_ESTAB_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CTM_ESTORNO_DANOS
**Comment**: Tabela do Relatorio de Estorno Danos/Autoconsumo - Modulo Especifico da Schincariol

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_ESTORNO | DATE | N |  |  |
| 5 | SEQ_ESTORNO | NUMBER(3) | N |  |  |
| 6 | QTD_ESTORNO | NUMBER(17,6) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 12 | DATA_FISCAL | DATE | Y |  |  |
| 13 | DATA_EMISSAO | DATE | Y |  |  |
| 14 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 15 | NUM_ITEM | NUMBER(5) | N |  |  |
| 16 | IDENT_PRODUTO_NF | NUMBER(12) | Y |  |  |
| 17 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 18 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 19 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 21 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 23 | QUANTIDADE_EST | NUMBER(17,6) | Y |  |  |
| 24 | IDENT_UND_PADRAO_EST | NUMBER(12) | Y |  |  |
| 25 | VLR_ICMS_EST | NUMBER(17,2) | Y |  |  |
| 26 | VLR_IPI_EST | NUMBER(17,2) | Y |  |  |
| 27 | VLR_PIS_EST | NUMBER(17,2) | Y |  |  |
| 28 | VLR_COFINS_EST | NUMBER(17,2) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_ESTORNO, SEQ_ESTORNO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM

**Indexes**:
- IX_CTM_ESTORNO_DANOS: (NUM_PROCESSO)

---

## CTM_INTERFACE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INTERFACE | NUMBER(3) | N |  |  |
| 2 | DSC_INTERFACE | VARCHAR2(50) | Y |  |  |

**PK**: COD_INTERFACE

---

## CTM_IST_REL_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | SITUACAO | CHAR(1) | Y |  |  |
| 8 | ALIQ_ISS_NOTA | NUMBER(7,4) | Y |  |  |
| 9 | COD_NAT_SERV | VARCHAR2(35) | Y |  |  |
| 10 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 11 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 12 | DSC_MUNIC_ISS | VARCHAR2(50) | Y |  |  |
| 13 | ALIQ_ISS_MUNIC | NUMBER(7,4) | Y |  |  |
| 14 | DIA_VENCTO | NUMBER(2) | Y |  |  |
| 15 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |
| 16 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 17 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TAXA_EXPED | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ISS_DEVIDO | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## CTM_NAT_OP_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 4 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CTM_PAR_NAT_OP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 4 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CTM_PROG_INTERFACE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TABELA | VARCHAR2(8) | N |  |  |
| 5 | COD_INTERFACE | NUMBER(3) | Y |  |  |
| 6 | IND_DAT_INTERNA | VARCHAR2(1) | Y |  |  |
| 7 | IND_ESPECIAL | VARCHAR2(1) | Y |  |  |

**PK**: COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TABELA

**FKs**:
- COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TABELA → IBT_CONTROLE(COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TABELA)
- COD_INTERFACE → CTM_INTERFACE(COD_INTERFACE)

---

## CTM_UF_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |

**PK**: IDENT_ESTADO

---

## CTM_UF_COD_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_CFO_DE | VARCHAR2(4) | N |  |  |
| 3 | COD_CFO_PARA | VARCHAR2(4) | N |  |  |

**PK**: IDENT_ESTADO, COD_CFO_DE, COD_CFO_PARA

**FKs**:
- IDENT_ESTADO → CTM_UF_CFO(IDENT_ESTADO)

---

