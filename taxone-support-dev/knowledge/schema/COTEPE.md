# Módulo: COTEPE (COTEPE) - 20 tabelas

## COTEPE_APUR_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | VLR_OUT_ICMS | NUMBER(17,2) | Y |  |  |
| 5 | VLR_ICMS_REC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APUR

---

## COTEPE_C625_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_CRZ | VARCHAR2(12) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | COD_ITEM | VARCHAR2(62) | N |  |  |
| 7 | UNID | VARCHAR2(8) | N |  |  |
| 8 | ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 9 | ECF_CX | VARCHAR2(6) | Y |  |  |
| 10 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 11 | QTD | NUMBER(17,2) | Y |  |  |
| 12 | QTD_CANC_I | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DOC | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DESC | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CANC | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ACMO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BC_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ISEN | NUMBER(17,2) | Y |  |  |
| 20 | VLR_NT | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ST | NUMBER(17,2) | Y |  |  |

**PK**: DATA_FISCAL, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_CRZ, COD_ITEM, UNID, ALIQ_ICMS

---

## COTEPE_D470_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MOD | VARCHAR2(2) | N |  |  |
| 4 | DT_DOC | DATE | N |  |  |
| 5 | SER | VARCHAR2(3) | N |  |  |
| 6 | SUB | VARCHAR2(3) | N |  |  |
| 7 | COD_MUN | NUMBER(7) | N |  |  |
| 8 | COD_CONS | NUMBER(2) | N |  |  |
| 9 | QTD_CONS | NUMBER | Y |  |  |
| 10 | QTD_CANC | NUMBER | Y |  |  |
| 11 | VL_DOC | NUMBER(17,2) | Y |  |  |
| 12 | VL_DESC | NUMBER(17,2) | Y |  |  |
| 13 | VL_SERV | NUMBER(17,2) | Y |  |  |
| 14 | VL_SERV_NT | NUMBER(17,2) | Y |  |  |
| 15 | VL_TERC | NUMBER(17,2) | Y |  |  |
| 16 | VL_DA | NUMBER(17,2) | Y |  |  |
| 17 | VL_BC_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | VL_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MOD, DT_DOC, SER, SUB, COD_MUN, COD_CONS

---

## COTEPE_D475_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MOD | VARCHAR2(2) | N |  |  |
| 4 | DT_DOC | DATE | N |  |  |
| 5 | SER | VARCHAR2(2) | N |  |  |
| 6 | SUB | VARCHAR2(3) | N |  |  |
| 7 | COD_MUN | NUMBER(7) | N |  |  |
| 8 | COD_CONS | NUMBER(2) | N |  |  |
| 9 | NUM_ITEM | NUMBER(5) | N |  |  |
| 10 | COD_ITEM | VARCHAR2(62) | Y |  |  |
| 11 | COD_CLASS | VARCHAR2(4) | Y |  |  |
| 12 | QTD | NUMBER | Y |  |  |
| 13 | UNID | VARCHAR2(8) | Y |  |  |
| 14 | VL_ITEM | NUMBER(17,2) | Y |  |  |
| 15 | VL_DESC_I | NUMBER(17,2) | Y |  |  |
| 16 | CST | VARCHAR2(3) | Y |  |  |
| 17 | CFOP | VARCHAR2(4) | Y |  |  |
| 18 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 19 | VL_BC_ICMS_I | NUMBER(17,2) | Y |  |  |
| 20 | VL_ICMS_I | NUMBER(17,2) | Y |  |  |
| 21 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MOD, DT_DOC, SER, SUB, COD_MUN, COD_CONS, NUM_ITEM

**Indexes**:
- IX_COTEPE_D475_TEMP: (COD_EMPRESA, COD_ESTAB, COD_MOD, DT_DOC, SER, SUB, COD_MUN, COD_CONS)

---

## COTEPE_D480_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MOD | VARCHAR2(2) | N |  |  |
| 4 | DT_DOC | DATE | N |  |  |
| 5 | SER | VARCHAR2(3) | N |  |  |
| 6 | SUB | VARCHAR2(3) | N |  |  |
| 7 | COD_MUN | NUMBER(7) | N |  |  |
| 8 | COD_CONS | NUMBER(2) | N |  |  |
| 9 | CST | VARCHAR2(3) | N |  |  |
| 10 | CFOP | VARCHAR2(4) | N |  |  |
| 11 | VL_CONT_P | NUMBER(17,2) | Y |  |  |
| 12 | VL_BC_ICMS_P | NUMBER(17,2) | Y |  |  |
| 13 | ALIQ_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VL_ICMS_P | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MOD, DT_DOC, SER, SUB, COD_MUN, COD_CONS, CST, CFOP

---

## COTEPE_DET_PERFIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 3 | COD_BLOCO | VARCHAR2(2) | N |  |  |
| 4 | COD_REGISTRO | VARCHAR2(7) | N |  |  |
| 5 | IND_RELAT_CONF | CHAR(1) | Y | 'N' |  |

**PK**: COD_LAYOUT, COD_PERFIL, COD_BLOCO, COD_REGISTRO

**FKs**:
- COD_LAYOUT, COD_PERFIL → COTEPE_PERFIL(COD_LAYOUT, COD_PERFIL)

---

## COTEPE_DOC_SIMP_ISS_UF
**Comment**: Tabela de Modelo de Documento Simplificado ISS por UF (Reg. A300/ A310/ A320/ A330/ B030)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, GRUPO_MODELO, COD_MODELO

---

## COTEPE_E100_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_OPER | VARCHAR2(1) | N |  |  |
| 4 | IND_EMIT | VARCHAR2(1) | N |  |  |
| 5 | COD_PART | VARCHAR2(16) | N |  |  |
| 6 | COD_MOD | VARCHAR2(2) | N |  |  |
| 7 | COD_SIT | VARCHAR2(2) | N |  |  |
| 8 | SER | VARCHAR2(3) | N |  |  |
| 9 | SUB | VARCHAR2(2) | N |  |  |
| 10 | COD_CONS | NUMBER(2) | N |  |  |
| 11 | NUM_DOC | VARCHAR2(12) | N |  |  |
| 12 | DT_DOC | DATE | N |  |  |
| 13 | NUM_LCTO | VARCHAR2(40) | Y |  |  |
| 14 | DT_E_S | DATE | Y |  |  |
| 15 | QTD_DOC | NUMBER(17,2) | Y |  |  |
| 16 | QTD_CANC | NUMBER(17,2) | Y |  |  |
| 17 | VL_CONT | NUMBER(17,2) | Y |  |  |
| 18 | VL_BC_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VL_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VL_ISNT_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VL_OUT_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | COD_INF_OBS | VARCHAR2(9) | Y |  |  |
| 23 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 24 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 25 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 26 | IE_PART | VARCHAR2(14) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_OPER, IND_EMIT, COD_PART, COD_MOD, COD_SIT, SER, SUB, COD_CONS, NUM_DOC, DT_DOC, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, IE_PART

---

## COTEPE_E105_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_OPER | VARCHAR2(1) | N |  |  |
| 4 | IND_EMIT | VARCHAR2(1) | N |  |  |
| 5 | COD_PART | VARCHAR2(16) | N |  |  |
| 6 | COD_MOD | VARCHAR2(2) | N |  |  |
| 7 | COD_SIT | VARCHAR2(2) | N |  |  |
| 8 | SER | VARCHAR2(3) | N |  |  |
| 9 | SUB | VARCHAR2(2) | N |  |  |
| 10 | COD_CONS | NUMBER(2) | N |  |  |
| 11 | NUM_DOC | VARCHAR2(12) | N |  |  |
| 12 | DT_DOC | DATE | N |  |  |
| 13 | CFOP | VARCHAR2(4) | N |  |  |
| 14 | VL_CONT_P | NUMBER(17,2) | Y |  |  |
| 15 | VL_BC_ICMS_P | NUMBER(17,2) | Y |  |  |
| 16 | ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 17 | VL_ICMS_P | NUMBER(17,2) | Y |  |  |
| 18 | VL_ISNT_ICMS_P | NUMBER(17,2) | Y |  |  |
| 19 | VL_OUT_ICMS_P | NUMBER(17,2) | Y |  |  |
| 20 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 21 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 22 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 23 | IE_PART | VARCHAR2(14) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_OPER, IND_EMIT, COD_PART, COD_MOD, COD_SIT, SER, SUB, COD_CONS, NUM_DOC, DT_DOC, CFOP, ALIQ_ICMS, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, IE_PART

---

## COTEPE_INF_COMPLEMENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO | DATE | N |  |  |
| 4 | VLR_N_ISS | NUMBER(17,2) | Y |  |  |
| 5 | VLR_ALUGUEL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_AGUA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ENERGIA | NUMBER(17,2) | Y |  |  |
| 8 | VLR_REMU_FUNC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_RPA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO

---

## COTEPE_LAYOUT_REGS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_REGISTRO | VARCHAR2(10) | N |  |  |
| 3 | COD_BLOCO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CATEGORIA | VARCHAR2(30) | Y |  |  |
| 5 | COD_GRUPO | VARCHAR2(5) | Y |  |  |
| 6 | QTDE_REGISTRO | NUMBER(15) | Y | 0 |  |

**PK**: PROC_ID, COD_REGISTRO

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## COTEPE_PERFIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 3 | DSC_PERFIL | VARCHAR2(100) | Y |  |  |
| 4 | IND_TP_APRESENT | VARCHAR2(1) | Y |  | Indica o perfil de apresentação do arquivo fiscal que será seguido pela Empresa, definido pela Receita Federal. |
| 5 | IDENT_VERBA_PORT63 | NUMBER(12) | Y |  |  |

**PK**: COD_LAYOUT, COD_PERFIL

---

## COTEPE_PERFIL_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_LAYOUT, COD_PERFIL, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_LAYOUT, COD_PERFIL → COTEPE_PERFIL(COD_LAYOUT, COD_PERFIL)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## COTEPE_PRODUTOS_G1_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | VALID_PRODUTO | DATE | N |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, VALID_PRODUTO

---

## COTEPE_PRODUTOS_G2_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | VALID_PRODUTO | DATE | N |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | DESCRICAO_UP | VARCHAR2(50) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, VALID_PRODUTO

---

## COTEPE_PRODUTOS_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## COTEPE_REDZ_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_CRZ | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | VLR_VENDA_BRUTA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_OPER_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OPER_ISENTA_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OPER_N_INCID_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OPER_DESC_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_OPER_ACRES_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_OPER_CANC_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_OPER_ISS_ST | NUMBER(17,2) | Y |  |  |
| 18 | VLR_OPER_ISENTA_ISS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_OPER_N_INCID_ISS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_OPER_DESC_ISS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_OPER_ACRES_ISS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_OPER_CANC_ISS | NUMBER(17,2) | Y |  |  |

**PK**: DATA_FISCAL, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_CRZ

---

## COTEPE_RES_CFO_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_OPER | VARCHAR2(1) | N |  |  |
| 4 | IND_EMIT | VARCHAR2(1) | N |  |  |
| 5 | COD_PART | VARCHAR2(16) | N |  |  |
| 6 | SER | VARCHAR2(3) | N |  |  |
| 7 | NUM_DOC | VARCHAR2(12) | N |  |  |
| 8 | DT_DOC | DATE | N |  |  |
| 9 | COD_MOD | VARCHAR2(2) | N |  |  |
| 10 | COD_CONS | VARCHAR2(2) | N |  |  |
| 11 | CFOP | VARCHAR2(4) | N |  |  |
| 12 | VL_CONT_P | NUMBER(17,2) | Y |  |  |
| 13 | VL_BC_ICMS_P | NUMBER(17,2) | Y |  |  |
| 14 | ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 15 | VL_ICMS_P | NUMBER(17,2) | Y |  |  |
| 16 | VL_ST_P | NUMBER(17,2) | Y |  |  |
| 17 | VL_COMPL_P | NUMBER(17,2) | Y |  |  |
| 18 | VL_ISNT_ICMS_P | NUMBER(17,2) | Y |  |  |
| 19 | VL_OUT_ICMS_P | NUMBER(17,2) | Y |  |  |
| 20 | VL_BC_IPI_P | NUMBER(17,2) | Y |  |  |
| 21 | VL_IPI_P | NUMBER(17,2) | Y |  |  |
| 22 | VL_ISNT_IPI_P | NUMBER(17,2) | Y |  |  |
| 23 | VL_OUT_IPI_P | NUMBER(17,2) | Y |  |  |
| 24 | COD_TRIB_IPI | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_OPER, IND_EMIT, COD_PART, SER, NUM_DOC, DT_DOC, COD_MOD, CFOP, COD_CONS, ALIQ_ICMS

---

## COTEPE_RES_CFO_TMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | CFOP | VARCHAR2(4) | N |  |  |
| 3 | VL_CONT_P | NUMBER(17,2) | Y |  |  |
| 4 | VL_BC_ICMS_P | NUMBER(17,2) | Y |  |  |
| 5 | VL_ICMS_P | NUMBER(17,2) | Y |  |  |
| 6 | VL_ST_P | NUMBER(17,2) | Y |  |  |
| 7 | VL_COMPL_P | NUMBER(17,2) | Y |  |  |
| 8 | VL_ISNT_ICMS_P | NUMBER(17,2) | Y |  |  |
| 9 | VL_OUT_ICMS_P | NUMBER(17,2) | Y |  |  |
| 10 | VL_BC_IPI_P | NUMBER(17,2) | Y |  |  |
| 11 | VL_IPI_P | NUMBER(17,2) | Y |  |  |
| 12 | VL_ISNT_IPI_P | NUMBER(17,2) | Y |  |  |
| 13 | VL_OUT_IPI_P | NUMBER(17,2) | Y |  |  |
| 14 | COD_TRIB_IPI | VARCHAR2(2) | Y |  |  |

**PK**: PROC_ID, CFOP

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## COTEPE_RES_UF_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | IND_OPER | NUMBER(1) | N |  |  |
| 3 | IDENT_UF | NUMBER(12) | N |  |  |
| 4 | UF | VARCHAR2(2) | N |  |  |
| 5 | VL_CONT | NUMBER(17,2) | Y |  |  |
| 6 | VL_BC_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VL_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VL_ST | NUMBER(17,2) | Y |  |  |
| 9 | VL_COMPL | NUMBER(17,2) | Y |  |  |
| 10 | VL_ISNT_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VL_OUT_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: PROC_ID, IND_OPER, IDENT_UF, UF

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

