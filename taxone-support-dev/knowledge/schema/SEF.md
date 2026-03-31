# Módulo: SEF (SEF) - 20 tabelas

## SEF_CAD_BEM
**Comment**: Tabela utilizada no SEF II - PE para armazenamento dos Bens movimentados, p/ geração do registro 0200.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_BEM | VARCHAR2(68) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, COD_BEM

---

## SEF_CAD_NAT_OP
**Comment**: Tabela utilizada no SEF II - PE para armazenamento dos códigos de natureza da operação, p/ geração do registro 0400.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 4 | COD_COP | VARCHAR2(4) | Y |  |  |

**PK**: PROC_ID, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## SEF_CAD_OBS
**Comment**: Tabela utilizada no SEF II - PE para armazenamento das informações complementares e das observações, p/ geração do registro 0450.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_OBSERVACAO | VARCHAR2(9) | N |  |  |
| 3 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |

**PK**: PROC_ID, GRUPO_OBSERVACAO, COD_OBSERVACAO

---

## SEF_CAD_OBS_NORMA
**Comment**: Tabela utilizada no SEF II - PE para armazenamento das observações mais a norma, p/ geração do registro 0455.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_OBSERVACAO | VARCHAR2(9) | N |  |  |
| 3 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 4 | DSC_NORMA | VARCHAR2(255) | N |  |  |

**PK**: PROC_ID, GRUPO_OBSERVACAO, COD_OBSERVACAO, DSC_NORMA

---

## SEF_CAD_PARTIC
**Comment**: Tabela utilizada no SEF II - PE para armazenamento para armazenamento das pessoas fis/jur, p/ geração do registro 0150.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 5 | IND_ICMSS | CHAR(1) | Y |  |  |

**PK**: PROC_ID, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

---

## SEF_CAD_PROD_SERV
**Comment**: Tabela utilizada no SEF II - PE para armazenamento dos Produtos e Serviços movimentados, p/ geração do registro 0200.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_PROD_SERV | VARCHAR2(9) | N |  |  |
| 3 | IND_PROD_SERV | CHAR(1) | N |  |  |
| 4 | COD_PROD_SERV | VARCHAR2(60) | N |  |  |

**PK**: PROC_ID, GRUPO_PROD_SERV, IND_PROD_SERV, COD_PROD_SERV

---

## SEF_CAPA_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | NUM_DOCFIS_FIN | VARCHAR2(12) | Y |  |  |
| 12 | COD_REG | VARCHAR2(4) | N |  |  |
| 13 | DT_DOC | DATE | Y |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COP | VARCHAR2(4) | Y |  |  |
| 16 | IND_OPER | CHAR(1) | Y |  |  |
| 17 | IND_EMIT | CHAR(1) | Y |  |  |
| 18 | NUM_LCTO | VARCHAR2(40) | Y |  |  |
| 19 | QTD_CANC | NUMBER(9) | Y |  |  |
| 20 | VL_CONT | NUMBER(17,2) | Y |  |  |
| 21 | VL_OP_ISS | NUMBER(17,2) | Y |  |  |
| 22 | VL_BC_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | VL_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | VL_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 25 | VL_ST_E | NUMBER(17,2) | Y |  |  |
| 26 | VL_ST_S | NUMBER(17,2) | Y |  |  |
| 27 | VL_AT | NUMBER(17,2) | Y |  |  |
| 28 | VL_ISNT_ICMS | NUMBER(17,2) | Y |  |  |
| 29 | VL_OUT_ICMS | NUMBER(17,2) | Y |  |  |
| 30 | VL_BC_IPI | NUMBER(17,2) | Y |  |  |
| 31 | VL_IPI | NUMBER(17,2) | Y |  |  |
| 32 | VL_ISNT_IPI | NUMBER(17,2) | Y |  |  |
| 33 | VL_OUT_IPI | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_REG

---

## SEF_DADOS_INICIAIS
**Comment**: Parametrização de dados iniciais, necessários para a geração do arquivo.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ASSIN_RESP | VARCHAR2(2) | Y |  |  |
| 4 | COD_CONT_RESP | VARCHAR2(2) | Y |  |  |
| 5 | IND_ESCRIT_ISS | CHAR(1) | Y |  |  |
| 6 | IND_ESCRIT_ICMS | CHAR(1) | Y |  |  |
| 7 | IND_REG_IMP_DF | CHAR(1) | Y |  |  |
| 8 | IND_REG_UTIL_DF | CHAR(1) | Y |  |  |
| 9 | IND_LIVRO_MC | CHAR(1) | Y |  |  |
| 10 | IND_REG_VEICULO | CHAR(1) | Y |  |  |
| 11 | IND_REG_INVENT | CHAR(1) | Y |  |  |
| 12 | IND_ESCRIT_CONT | CHAR(1) | Y |  |  |
| 13 | IND_OPER_ISS | CHAR(1) | Y |  |  |
| 14 | IND_RET_ISS | CHAR(1) | Y |  |  |
| 15 | IND_OPER_ICMS | CHAR(1) | Y |  |  |
| 16 | IND_OPER_ICMSS | CHAR(1) | Y |  |  |
| 17 | IND_ANTEC_ICMS | CHAR(1) | Y |  |  |
| 18 | IND_OPER_IPI | CHAR(1) | Y |  |  |
| 19 | IND_APRES_INV | CHAR(1) | Y |  |  |
| 20 | IND_NAT_SERV | CHAR(1) | Y |  |  |
| 21 | IND_BENEF_PRODEPE | CHAR(1) | Y |  |  |
| 22 | MES_ANO_ENTREGA | DATE | Y |  |  |
| 23 | GRUPO_MODELO | VARCHAR2(9) | Y |  |  |
| 24 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 25 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 26 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 27 | IND_PROD_PAPEL | CHAR(1) | Y |  |  |
| 28 | IND_CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 29 | NUM_CRED_GRAF | VARCHAR2(5) | Y |  |  |
| 30 | IDENT_ESTADO_GRAF | NUMBER(12) | Y |  |  |
| 31 | IND_COD_ITEM | CHAR(1) | Y | 'S' |  |
| 32 | IND_COD_PART | CHAR(1) | Y | 'S' |  |
| 33 | IND_VL_ICMS_E065 | CHAR(1) | Y | '1' |  |
| 34 | QTDE_MESES_ANT_DTFISC | NUMBER(2) | Y | 1 |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_ASSIN_RESP → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONT_RESP → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## SEF_DOCFIS_REF
**Comment**: Tabela utilizada no SEF II - PE para armazenamento dos documentos fiscais referenciados por observação, p/ geração do registro 0465.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_OBSERVACAO | VARCHAR2(9) | N |  |  |
| 3 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 4 | IND_OPER | NUMBER(1) | N |  |  |
| 5 | IND_EMIT | NUMBER(1) | N |  |  |
| 6 | COD_CNPJ | VARCHAR2(14) | N |  |  |
| 7 | COD_CPF | NUMBER(11) | N |  |  |
| 8 | UF | VARCHAR2(2) | Y |  |  |
| 9 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 10 | COD_MUNICIPIO | NUMBER(7) | Y |  |  |
| 11 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 12 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 13 | COD_SIT | NUMBER(2) | N |  |  |
| 14 | SERIE | VARCHAR2(3) | N |  |  |
| 15 | SUBSERIE | VARCHAR2(2) | N |  |  |
| 16 | CHV_NFE_CTE | VARCHAR2(80) | Y |  |  |
| 17 | NUM_DOC | NUMBER(12) | N |  |  |
| 18 | DT_DOC | DATE | N |  |  |
| 19 | VL_DOC | NUMBER(17,2) | Y |  |  |
| 20 | VL_ISS | NUMBER(17,2) | Y |  |  |
| 21 | VL_RT | NUMBER(17,2) | Y |  |  |
| 22 | VL_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | VL_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 24 | VL_AT | NUMBER(17,2) | Y |  |  |
| 25 | VL_IPI | NUMBER(17,2) | Y |  |  |
| 26 | VOLUME | NUMBER(17,2) | Y |  |  |
| 27 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 28 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |

**PK**: PROC_ID, GRUPO_OBSERVACAO, COD_OBSERVACAO, IND_OPER, IND_EMIT, DT_DOC, SERIE, SUBSERIE, NUM_DOC, COD_CNPJ, COD_CPF, COD_MODELO, COD_SIT

---

## SEF_ESTAB_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |

---

## SEF_IDENT_CAPA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |

---

## SEF_IDENT_ITENS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_SEF_IDENT_ITENS: (IDENT_DOCTO_FISCAL)

---

## SEF_INCENT_TMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 4 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 5 | VALIDADE_INICIAL | DATE | N |  |  |
| 6 | IND_GRP_ESP | CHAR(1) | N |  |  |
| 7 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 8 | PERC_ENTRADAS | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, SERIE_LIVRO, SUB_SERIE_LIVRO, VALIDADE_INICIAL, IND_GRP_ESP, COD_GRP_INCENT

---

## SEF_ITEM_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 12 | COD_REG | VARCHAR2(4) | N |  |  |
| 13 | DT_DOC | DATE | Y |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COP | VARCHAR2(4) | Y |  |  |
| 16 | IND_OPER | CHAR(1) | Y |  |  |
| 17 | IND_EMIT | CHAR(1) | Y |  |  |
| 18 | NUM_LCTO | VARCHAR2(40) | Y |  |  |
| 19 | VL_CONT | NUMBER(17,2) | Y |  |  |
| 20 | VL_OP_ISS | NUMBER(17,2) | Y |  |  |
| 21 | VL_BC_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | VL_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | VL_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 24 | VL_ST_E | NUMBER(17,2) | Y |  |  |
| 25 | VL_ST_S | NUMBER(17,2) | Y |  |  |
| 26 | VL_ISNT_ICMS | NUMBER(17,2) | Y |  |  |
| 27 | VL_OUT_ICMS | NUMBER(17,2) | Y |  |  |
| 28 | VL_BC_IPI | NUMBER(17,2) | Y |  |  |
| 29 | VL_IPI | NUMBER(17,2) | Y |  |  |
| 30 | VL_ISNT_IPI | NUMBER(17,2) | Y |  |  |
| 31 | VL_OUT_IPI | NUMBER(17,2) | Y |  |  |
| 32 | IND_IMUN | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, COD_REG

---

## SEF_REG_8040
**Comment**: Tabela Temporária p/ geração do registro 8040

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_QVA | CHAR(1) | N |  |  |
| 4 | DATA_INI | DATE | N |  |  |
| 5 | DATA_FIN | DATE | N |  |  |
| 6 | IND_CFOP | CHAR(1) | N |  |  |
| 7 | CFOP | VARCHAR2(4) | N |  |  |
| 8 | VL_CONT | NUMBER(17,2) | Y |  |  |
| 9 | VL_OP_ISS | NUMBER(17,2) | Y |  |  |
| 10 | VL_ICMS_ST | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_QVA, DATA_INI, DATA_FIN, IND_CFOP, CFOP

---

## SEF_REG_8165

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | VLR_CRED_INI | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR

---

## SEF_REG_8170

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | SEQUENCIAL | NUMBER(18) | N |  |  |
| 5 | IND_TIPO | CHAR(1) | Y |  |  |
| 6 | VLR_CRED | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROC | VARCHAR2(30) | Y |  |  |
| 8 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 9 | DSC_PROC | VARCHAR2(60) | Y |  |  |
| 10 | DSC_OBSERVACAO | VARCHAR2(255) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APUR → SEF_REG_8165(COD_EMPRESA, COD_ESTAB, DAT_APUR)

---

## SEF_REG_8180

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IND_RESPONS | CHAR(1) | N |  |  |
| 5 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 6 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 7 | VLR_DEBITO | NUMBER(17,2) | Y |  |  |
| 8 | DSC_OBSERVACAO | VARCHAR2(255) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, IND_RESPONS

**FKs**:
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## SEF_REG_E360

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_OBRIG | NUMBER(3) | N |  |  |
| 6 | PERIODO_REF | DATE | N |  |  |
| 7 | SEQUENCIAL | NUMBER(18) | N |  |  |
| 8 | DAT_VENC | DATE | Y |  |  |
| 9 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 10 | VLR_REC | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROC | VARCHAR2(30) | Y |  |  |
| 12 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 13 | DSC_PROC | VARCHAR2(60) | Y |  |  |
| 14 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, IDENT_ESTADO, COD_OBRIG, PERIODO_REF, SEQUENCIAL

**FKs**:
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_2580: (IDENT_OBSERVACAO)

---

## SEF_REG_E560

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | COD_OBRIG | VARCHAR2(4) | Y |  |  |
| 5 | PERIODO_REF | DATE | N |  |  |
| 6 | SEQUENCIAL | NUMBER(18) | N |  |  |
| 7 | DAT_VENC | DATE | Y |  |  |
| 8 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 9 | VLR_REC | NUMBER(17,2) | Y |  |  |
| 10 | NUM_DOC_VINC | VARCHAR2(25) | Y |  |  |
| 11 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 12 | DSC_PROC | VARCHAR2(60) | Y |  |  |
| 13 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, COD_RECEITA, PERIODO_REF, SEQUENCIAL

**FKs**:
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)

**Indexes**:
- IX_FK_SAF_2581: (IDENT_OBSERVACAO)

---

