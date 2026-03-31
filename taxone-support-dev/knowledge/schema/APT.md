# Módulo: APT (APT) - 35 tabelas

## APT_ALIENACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CIAP | NUMBER(12) | N |  |  |
| 4 | DAT_OPER | DATE | N |  |  |
| 5 | TIPO_MOV | VARCHAR2(3) | N |  |  |
| 6 | ANO_REGISTRO | NUMBER(4) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | MODELO_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DAT_FISCAL | DATE | Y |  |  |
| 12 | DAT_SAIDA_BEM | DATE | Y |  |  |
| 13 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 14 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 15 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 16 | VLR_ALIENACAO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ESTORNO_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CRED_APROP | NUMBER(17,2) | Y |  |  |
| 19 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 20 | VLR_BASE_TRIB | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_ISENTAS | NUMBER(17,2) | Y |  |  |
| 22 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 23 | COD_INC | VARCHAR2(6) | Y |  |  |
| 24 | QTD_BENS_ALIENADOS | NUMBER(17,6) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 27 | IND_LEI | CHAR(1) | Y |  |  |
| 28 | TIPO_BAIXA | CHAR(1) | Y |  |  |
| 29 | VLR_ICMS_BX | NUMBER(17,2) | Y |  |  |
| 30 | VLR_DIFAL_BX | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ICMS_FRETE_BX | NUMBER(17,2) | Y |  |  |
| 32 | VLR_DIFAL_FRETE_BX | NUMBER(17,2) | Y |  |  |
| 33 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 34 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 35 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 36 | VLR_ICMSS_BX | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_CIAP, DAT_OPER, TIPO_MOV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- TIPO_MOV → APT_TIPO_MOV(TIPO_MOV)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- COD_EMPRESA, COD_ESTAB, NUM_CIAP → APT_AQUISICAO(COD_EMPRESA, COD_ESTAB, NUM_CIAP)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- MODELO_DOCFIS → APT_MODELO_DOCTO(MODELO_DOCFIS)

**Indexes**:
- IX_FK_SAF_0654: (IDENT_FIS_JUR)

---

## APT_AQUISICAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CIAP | NUMBER(12) | N |  |  |
| 4 | ANO_REGISTRO | NUMBER(4) | Y |  |  |
| 5 | DAT_OPER | DATE | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | DAT_FISCAL | DATE | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 12 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 13 | DESCR_BEM | VARCHAR2(50) | Y |  |  |
| 14 | COMPL_DESCR_BEM | VARCHAR2(50) | Y |  |  |
| 15 | MODELO_BEM | VARCHAR2(30) | Y |  |  |
| 16 | SERIE_BEM | VARCHAR2(30) | Y |  |  |
| 17 | PLAQUETA_BEM | VARCHAR2(30) | Y |  |  |
| 18 | VLR_AQUIS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | NUM_LRE | VARCHAR2(6) | Y |  |  |
| 21 | PAG_LRE | VARCHAR2(6) | Y |  |  |
| 22 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 23 | COD_INC | VARCHAR2(6) | Y |  |  |
| 24 | ST_ATIVO | CHAR(1) | Y |  |  |
| 25 | TIPO_MOV | VARCHAR2(3) | Y |  |  |
| 26 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 27 | IND_GERACAO | CHAR(1) | Y |  |  |
| 28 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 29 | IND_AQUIS_TRIB | CHAR(1) | Y |  |  |
| 30 | NUM_OFICIAL_CIAP | VARCHAR2(12) | Y |  |  |
| 31 | NUM_MESES_ESTORNO | NUMBER(3) | Y |  |  |
| 32 | QTD_BENS_ALIENADOS | NUMBER(17,6) | Y |  |  |
| 33 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 34 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 35 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 36 | IND_LEI | CHAR(1) | Y |  |  |
| 37 | VLR_CRED_DIF_ALIQ | NUMBER(17,2) | Y |  |  |
| 38 | VLR_CRED_MES1 | NUMBER(17,2) | Y |  |  |
| 39 | VLR_CRED_ICMS_CONV | NUMBER(17,6) | Y |  |  |
| 40 | VLR_CRDIFALIQ_CONV | NUMBER(17,6) | Y |  |  |
| 41 | VLR_CRED_MES1_CONV | NUMBER(17,6) | Y |  |  |
| 42 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 43 | NORM_DEV | CHAR(1) | Y |  |  |
| 44 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 45 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 46 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 47 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 48 | IDENT_PROJETO | NUMBER(12) | Y |  |  |
| 49 | IND_BAIXA_AUTO | CHAR(1) | Y |  |  |
| 50 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 51 | VLR_DIFAL_FRETE | NUMBER(17,2) | Y |  |  |
| 52 | VLR_ICMS_FRETE_CV | NUMBER(17,6) | Y |  |  |
| 53 | VLR_DIFAL_FRETE_CV | NUMBER(17,6) | Y |  |  |
| 54 | DAT_INTERN_AM | DATE | Y |  |  |
| 55 | LOCAL_BEM | VARCHAR2(150) | Y |  |  |
| 56 | DAT_EMISSAO | DATE | Y |  |  |
| 57 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 58 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 59 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 60 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 61 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 62 | VLR_ICMSS_CONV | NUMBER(17,6) | Y |  |  |
| 63 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 64 | USUARIO | VARCHAR2(40) | Y |  |  |
| 65 | DATA_INC_ALT | DATE | Y |  |  |
| 66 | ORIGEM_INC_ALT | CHAR(1) | Y |  |  |
| 67 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 68 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_CIAP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- TIPO_MOV → APT_TIPO_MOV(TIPO_MOV)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_PROJETO → X2016_PROJETO(IDENT_PROJETO)

**Indexes**:
- IX_APT_AQUISICAO: (COD_EMPRESA, COD_ESTAB, DAT_OPER)
- IX_APT_AQUIS_NF: (COD_EMPRESA, COD_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IX_APT_AQUIS_NFT: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM)
- IX_FK_SAF_0662: (IDENT_FIS_JUR)

---

## APT_BASE_REF_CALC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | VLR_TOT_OP_ISENTAS | NUMBER(17,2) | Y |  |  |
| 5 | VLR_TOT_OP_SAIDAS | NUMBER(17,2) | Y |  |  |
| 6 | COEFICIENTE | NUMBER(16,7) | Y |  |  |
| 7 | VLR_BASE_ESTORNO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_FRACAO_MENSAL | NUMBER(11,6) | Y |  |  |
| 9 | VLR_EST_OP_ISENTAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_EST_OP_SAIDAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_EST_MENSAL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TOT_TRANS_CRED | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TOT_TRANS_DEB | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_CALC_BEM_EXTEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | COD_BEM | VARCHAR2(60) | N |  |  |
| 5 | COD_INC | VARCHAR2(6) | N |  |  |
| 6 | NUM_PARCELA | NUMBER(3) | N |  |  |
| 7 | DATA_INI | DATE | Y |  |  |
| 8 | DATA_FIM | DATE | Y |  |  |
| 9 | VLR_PARC_APROP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_SAIDA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SAIDA_TRIB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PARCELA | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_BEM, COD_INC, NUM_PARCELA

---

## APT_CALC_CRED_EXT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | NUM_CIAP | NUMBER(12) | N |  |  |
| 5 | DAT_INI | DATE | N |  |  |
| 6 | DAT_FIN | DATE | N |  |  |
| 7 | NUM_PARCELA | NUMBER(3) | N |  |  |
| 8 | VLR_PARC_APROP | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_SAIDA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SAIDA_TRIB | NUMBER(17,2) | Y |  |  |
| 11 | VLR_PARCELA | NUMBER(17,2) | Y |  |  |
| 12 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 13 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 16 | PARCELA_SEQ | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, NUM_CIAP, NUM_PARCELA, COD_ESTAB_ORIG

---

## APT_CALC_CRED_EXT_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_CIAP | NUMBER(12) | N |  |  |
| 6 | DAT_INI | DATE | N |  |  |
| 7 | DAT_FIN | DATE | N |  |  |
| 8 | NUM_PARCELA | NUMBER(3) | N |  |  |
| 9 | VLR_PARC_APROP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_SAIDA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SAIDA_TRIB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PARCELA | NUMBER(17,2) | Y |  |  |
| 13 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, NUM_CIAP, NUM_PARCELA

---

## APT_CFO_ESTAB_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | DAT_INI_REGRA | DATE | N |  |  |
| 5 | DAT_FIN_REGRA | DATE | Y |  |  |
| 6 | NUM_PARC_AP | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, DAT_INI_REGRA

---

## APT_CFO_NATUR_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CFO | NUMBER(12) | N |  |  |
| 2 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |
| 3 | TIPO_MOV | VARCHAR2(3) | Y |  |  |

**PK**: IDENT_CFO, IDENT_NATUREZA_OP

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)

---

## APT_CFO_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | TIPO_MOV | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_CFO_UF_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | DAT_INI_REGRA | DATE | N |  |  |
| 5 | DAT_FIN_REGRA | DATE | Y |  |  |
| 6 | NUM_PARC_AP | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_CFO, DAT_INI_REGRA

---

## APT_CIAP_BEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CIAP | NUMBER(12) | N |  |  |
| 4 | COD_BEM | VARCHAR2(60) | N |  |  |
| 5 | COD_INC | VARCHAR2(6) | N |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_CIAP, COD_BEM, COD_INC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_CONTROLE_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | TIPO_OPERACAO | VARCHAR2(2) | N |  |  |
| 5 | MODELO | CHAR(1) | N |  |  |
| 6 | IND_APROVACAO | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | IND_LEI | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, TIPO_OPERACAO, MODELO, IND_LEI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_CRED_CFO_102

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | VLR_CRED_ICMS_DF | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_ICMSS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_CRED_NF_102

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO_REF | DATE | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUBSERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DAT_FISCAL | DATE | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 11 | VLR_CRED_ENTRADA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CRED_MENSAL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO_REF, DAT_APURACAO, NUM_DOCFIS, SERIE_DOCFIS, SUBSERIE_DOCFIS, DAT_FISCAL, IDENT_FIS_JUR, IDENT_DOCTO

---

## APT_CRED_NF_102_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO_REF | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | DAT_FISCAL | DATE | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 10 | DAT_OPER | DATE | N |  |  |
| 11 | VLR_CRED_ENTRADA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CRED_MENSAL | NUMBER(17,2) | Y |  |  |
| 13 | DAT_APUR_M01 | DATE | Y |  |  |
| 14 | VLR_CRED_M01 | NUMBER(17,2) | Y |  |  |
| 15 | DAT_APUR_M02 | DATE | Y |  |  |
| 16 | VLR_CRED_M02 | NUMBER(17,2) | Y |  |  |
| 17 | DAT_APUR_M03 | DATE | Y |  |  |
| 18 | VLR_CRED_M03 | NUMBER(17,2) | Y |  |  |
| 19 | DAT_APUR_M04 | DATE | Y |  |  |
| 20 | VLR_CRED_M04 | NUMBER(17,2) | Y |  |  |
| 21 | DAT_APUR_M05 | DATE | Y |  |  |
| 22 | VLR_CRED_M05 | NUMBER(17,2) | Y |  |  |
| 23 | DAT_APUR_M06 | DATE | Y |  |  |
| 24 | VLR_CRED_M06 | NUMBER(17,2) | Y |  |  |
| 25 | DAT_APUR_M07 | DATE | Y |  |  |
| 26 | VLR_CRED_M07 | NUMBER(17,2) | Y |  |  |
| 27 | DAT_APUR_M08 | DATE | Y |  |  |
| 28 | VLR_CRED_M08 | NUMBER(17,2) | Y |  |  |
| 29 | DAT_APUR_M09 | DATE | Y |  |  |
| 30 | VLR_CRED_M09 | NUMBER(17,2) | Y |  |  |
| 31 | DAT_APUR_M10 | DATE | Y |  |  |
| 32 | VLR_CRED_M10 | NUMBER(17,2) | Y |  |  |
| 33 | DAT_APUR_M11 | DATE | Y |  |  |
| 34 | VLR_CRED_M11 | NUMBER(17,2) | Y |  |  |
| 35 | DAT_APUR_M12 | DATE | Y |  |  |
| 36 | VLR_CRED_M12 | NUMBER(17,2) | Y |  |  |
| 37 | DAT_APUR_M13 | DATE | Y |  |  |
| 38 | VLR_CRED_M13 | NUMBER(17,2) | Y |  |  |
| 39 | DAT_APUR_M14 | DATE | Y |  |  |
| 40 | VLR_CRED_M14 | NUMBER(17,2) | Y |  |  |
| 41 | DAT_APUR_M15 | DATE | Y |  |  |
| 42 | VLR_CRED_M15 | NUMBER(17,2) | Y |  |  |
| 43 | DAT_APUR_M16 | DATE | Y |  |  |
| 44 | VLR_CRED_M16 | NUMBER(17,2) | Y |  |  |
| 45 | DAT_APUR_M17 | DATE | Y |  |  |
| 46 | VLR_CRED_M17 | NUMBER(17,2) | Y |  |  |
| 47 | DAT_APUR_M18 | DATE | Y |  |  |
| 48 | VLR_CRED_M18 | NUMBER(17,2) | Y |  |  |
| 49 | DAT_APUR_M19 | DATE | Y |  |  |
| 50 | VLR_CRED_M19 | NUMBER(17,2) | Y |  |  |
| 51 | DAT_APUR_M20 | DATE | Y |  |  |
| 52 | VLR_CRED_M20 | NUMBER(17,2) | Y |  |  |
| 53 | DAT_APUR_M21 | DATE | Y |  |  |
| 54 | VLR_CRED_M21 | NUMBER(17,2) | Y |  |  |
| 55 | DAT_APUR_M22 | DATE | Y |  |  |
| 56 | VLR_CRED_M22 | NUMBER(17,2) | Y |  |  |
| 57 | DAT_APUR_M23 | DATE | Y |  |  |
| 58 | VLR_CRED_M23 | NUMBER(17,2) | Y |  |  |
| 59 | DAT_APUR_M24 | DATE | Y |  |  |
| 60 | VLR_CRED_M24 | NUMBER(17,2) | Y |  |  |
| 61 | DAT_APUR_M25 | DATE | Y |  |  |
| 62 | VLR_CRED_M25 | NUMBER(17,2) | Y |  |  |
| 63 | DAT_APUR_M26 | DATE | Y |  |  |
| 64 | VLR_CRED_M26 | NUMBER(17,2) | Y |  |  |
| 65 | DAT_APUR_M27 | DATE | Y |  |  |
| 66 | VLR_CRED_M27 | NUMBER(17,2) | Y |  |  |
| 67 | DAT_APUR_M28 | DATE | Y |  |  |
| 68 | VLR_CRED_M28 | NUMBER(17,2) | Y |  |  |
| 69 | DAT_APUR_M29 | DATE | Y |  |  |
| 70 | VLR_CRED_M29 | NUMBER(17,2) | Y |  |  |
| 71 | DAT_APUR_M30 | DATE | Y |  |  |
| 72 | VLR_CRED_M30 | NUMBER(17,2) | Y |  |  |
| 73 | DAT_APUR_M31 | DATE | Y |  |  |
| 74 | VLR_CRED_M31 | NUMBER(17,2) | Y |  |  |
| 75 | DAT_APUR_M32 | DATE | Y |  |  |
| 76 | VLR_CRED_M32 | NUMBER(17,2) | Y |  |  |
| 77 | DAT_APUR_M33 | DATE | Y |  |  |
| 78 | VLR_CRED_M33 | NUMBER(17,2) | Y |  |  |
| 79 | DAT_APUR_M34 | DATE | Y |  |  |
| 80 | VLR_CRED_M34 | NUMBER(17,2) | Y |  |  |
| 81 | DAT_APUR_M35 | DATE | Y |  |  |
| 82 | VLR_CRED_M35 | NUMBER(17,2) | Y |  |  |
| 83 | DAT_APUR_M36 | DATE | Y |  |  |
| 84 | VLR_CRED_M36 | NUMBER(17,2) | Y |  |  |
| 85 | DAT_APUR_M37 | DATE | Y |  |  |
| 86 | VLR_CRED_M37 | NUMBER(17,2) | Y |  |  |
| 87 | DAT_APUR_M38 | DATE | Y |  |  |
| 88 | VLR_CRED_M38 | NUMBER(17,2) | Y |  |  |
| 89 | DAT_APUR_M39 | DATE | Y |  |  |
| 90 | VLR_CRED_M39 | NUMBER(17,2) | Y |  |  |
| 91 | DAT_APUR_M40 | DATE | Y |  |  |
| 92 | VLR_CRED_M40 | NUMBER(17,2) | Y |  |  |
| 93 | DAT_APUR_M41 | DATE | Y |  |  |
| 94 | VLR_CRED_M41 | NUMBER(17,2) | Y |  |  |
| 95 | DAT_APUR_M42 | DATE | Y |  |  |
| 96 | VLR_CRED_M42 | NUMBER(17,2) | Y |  |  |
| 97 | DAT_APUR_M43 | DATE | Y |  |  |
| 98 | VLR_CRED_M43 | NUMBER(17,2) | Y |  |  |
| 99 | DAT_APUR_M44 | DATE | Y |  |  |
| 100 | VLR_CRED_M44 | NUMBER(17,2) | Y |  |  |
| 101 | DAT_APUR_M45 | DATE | Y |  |  |
| 102 | VLR_CRED_M45 | NUMBER(17,2) | Y |  |  |
| 103 | DAT_APUR_M46 | DATE | Y |  |  |
| 104 | VLR_CRED_M46 | NUMBER(17,2) | Y |  |  |
| 105 | DAT_APUR_M47 | DATE | Y |  |  |
| 106 | VLR_CRED_M47 | NUMBER(17,2) | Y |  |  |
| 107 | DAT_APUR_M48 | DATE | Y |  |  |
| 108 | VLR_CRED_M48 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO_REF, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DAT_FISCAL, IDENT_FIS_JUR, IDENT_DOCTO, DAT_OPER

---

## APT_CRED_PR_102

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO_REF | DATE | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | NUM_CIAP | NUMBER(12) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUBSERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | DAT_ENTRADA | DATE | Y |  |  |
| 10 | NUM_DOCFIS_S | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS_S | VARCHAR2(3) | Y |  |  |
| 12 | SUBSERIE_DOCFIS_S | VARCHAR2(2) | Y |  |  |
| 13 | DAT_SAIDA | DATE | Y |  |  |
| 14 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 15 | DESCR_BEM | VARCHAR2(50) | Y |  |  |
| 16 | NUM_OFICIAL_CIAP | VARCHAR2(12) | Y |  |  |
| 17 | VLR_CRED_ENTRADA | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CRED_MENSAL | NUMBER(17,2) | Y |  |  |
| 19 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |

**Indexes**:
- IX_APT_CRED_PR_102: (COD_EMPRESA, COD_ESTAB, DAT_APURACAO_REF, DAT_APURACAO, NUM_CIAP)

---

## APT_DEM_BASE_CR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | NUM_CIAP | NUMBER(12) | N |  |  |
| 5 | IND_E_S | CHAR(1) | N |  |  |
| 6 | NUM_OFICIAL_CIAP | VARCHAR2(12) | Y |  |  |
| 7 | DAT_OPER | DATE | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | DSC_BEM | VARCHAR2(50) | Y |  |  |
| 12 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CRED_ICMS_CONV | NUMBER(17,6) | Y |  |  |
| 14 | VLR_CRED_MENSAL | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | COMPL_DESCR_BEM | VARCHAR2(50) | Y |  |  |
| 18 | PARCELA | NUMBER(3) | Y |  |  |
| 19 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 20 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 21 | TIPO_MOV | VARCHAR2(3) | N | ' ' |  |
| 22 | VLR_PASS_APROP | NUMBER(17,2) | Y |  |  |
| 23 | NUM_FRACAO | NUMBER(3) | Y |  |  |
| 24 | PARCELA_SEQ | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, NUM_CIAP, IND_E_S, DAT_OPER, TIPO_MOV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## APT_DEM_BASE_CR_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_CIAP | NUMBER(12) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | NUM_OFICIAL_CIAP | VARCHAR2(12) | Y |  |  |
| 8 | DAT_OPER | DATE | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DSC_BEM | VARCHAR2(50) | Y |  |  |
| 13 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CRED_ICMS_CONV | NUMBER(17,6) | Y |  |  |
| 15 | VLR_CRED_MENSAL | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | COMPL_DESCR_BEM | VARCHAR2(50) | Y |  |  |
| 19 | PARCELA | NUMBER(3) | Y |  |  |
| 20 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 21 | TIPO_MOV | VARCHAR2(3) | N | ' ' |  |
| 22 | VLR_PASS_APROP | NUMBER(17,2) | Y |  |  |
| 23 | NUM_FRACAO | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, NUM_CIAP, IND_E_S, DAT_OPER, TIPO_MOV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## APT_DEM_BASE_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REGISTRO | NUMBER(4) | N |  |  |
| 4 | NUM_CIAP | NUMBER(12) | N |  |  |
| 5 | DAT_OPER | DATE | N |  |  |
| 6 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ESTORNO_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ESTORNO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_EST_SALDO | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | IND_E_S | CHAR(1) | N | 'E' |  |
| 13 | COD_ESTAB_ORIG | VARCHAR2(6) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REGISTRO, NUM_CIAP, DAT_OPER, IND_E_S, COD_ESTAB_ORIG

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_DEM_CR_MENSAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | VLR_TOT_OP_TRIBUT | NUMBER(17,2) | Y |  |  |
| 5 | VLR_TOT_OP_SAIDAS | NUMBER(17,2) | Y |  |  |
| 6 | COEFICIENTE | NUMBER(16,7) | Y |  |  |
| 7 | VLR_TOT_APROPRIAR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT_CREDITO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_TRANSF_DB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_TRANSF_CR | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | VLR_TOT_CRED_PASS | NUMBER(17,2) | Y |  |  |
| 14 | DAT_OPER | DATE | Y |  |  |
| 15 | USUARIO | VARCHAR2(50) | Y |  |  |
| 16 | NUM_FRACAO | NUMBER(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, NUM_FRACAO

---

## APT_DEM_CR_MENSAL_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | VLR_TOT_OP_TRIBUT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TOT_OP_SAIDAS | NUMBER(17,2) | Y |  |  |
| 7 | COEFICIENTE | NUMBER(16,7) | Y |  |  |
| 8 | VLR_TOT_APROPRIAR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_CREDITO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_CRED_PASS | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | NUM_FRACAO | NUMBER(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, NUM_FRACAO

---

## APT_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MODELO | CHAR(1) | Y |  |  |
| 4 | IND_FRACAO_MENSAL | CHAR(1) | Y |  |  |
| 5 | PAGINA_MODELO_A | NUMBER(6) | Y |  |  |
| 6 | ITEM_APURACAO | VARCHAR2(5) | Y |  |  |
| 7 | ITEM_APURACAO_TE | VARCHAR2(5) | Y |  |  |
| 8 | ITEM_APURACAO_TS | VARCHAR2(5) | Y |  |  |
| 9 | DESCR_ITEM_1 | VARCHAR2(50) | Y |  |  |
| 10 | DESCR_ITEM_1_TE | VARCHAR2(50) | Y |  |  |
| 11 | DESCR_ITEM_1_TS | VARCHAR2(50) | Y |  |  |
| 12 | DESCR_ITEM_2 | VARCHAR2(50) | Y |  |  |
| 13 | DESCR_ITEM_2_TE | VARCHAR2(50) | Y |  |  |
| 14 | DESCR_ITEM_2_TS | VARCHAR2(50) | Y |  |  |
| 15 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 16 | COD_CLASSE_1 | VARCHAR2(3) | Y |  |  |
| 17 | COD_CLASSE_TE | VARCHAR2(3) | Y |  |  |
| 18 | COD_CLASSE_TS | VARCHAR2(3) | Y |  |  |
| 19 | IND_LEI | CHAR(1) | Y |  |  |
| 20 | IND_PERIODIC_102 | CHAR(1) | Y |  |  |
| 21 | COD_TP_LVR_102 | VARCHAR2(3) | Y |  |  |
| 22 | ITEM_AP_102 | VARCHAR2(5) | Y |  |  |
| 23 | ITEM_AP_TE_102 | VARCHAR2(5) | Y |  |  |
| 24 | ITEM_AP_TS_102 | VARCHAR2(5) | Y |  |  |
| 25 | DESCR_ITEM_102 | VARCHAR2(100) | Y |  |  |
| 26 | DESCR_ITEM_TE_102 | VARCHAR2(100) | Y |  |  |
| 27 | DESC_ITEM_TS_102 | VARCHAR2(100) | Y |  |  |
| 28 | COD_CLASSE_102 | VARCHAR2(3) | Y |  |  |
| 29 | COD_CLASSE_TS_102 | VARCHAR2(3) | Y |  |  |
| 30 | COD_CLASSE_TE_102 | VARCHAR2(3) | Y |  |  |
| 31 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 32 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 33 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 34 | GRUPO_OBS_LIVRO | VARCHAR2(9) | Y |  |  |
| 35 | COD_OBS_LIVRO | VARCHAR2(10) | Y |  |  |
| 36 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 37 | MODELO_102 | CHAR(1) | Y |  |  |
| 38 | PAGINA_MODELO_C | NUMBER(6) | Y |  |  |
| 39 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 40 | APROPRIA_DIF_ALIQ | CHAR(1) | Y |  |  |
| 41 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 42 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 43 | COD_AMP_LEG | VARCHAR2(10) | Y |  |  |
| 44 | COD_SUB_OCO | VARCHAR2(2) | Y |  |  |
| 45 | COD_AMP_LEG_TE | VARCHAR2(10) | Y |  |  |
| 46 | COD_SUB_OCO_TE | VARCHAR2(2) | Y |  |  |
| 47 | COD_AMP_LEG_TS | VARCHAR2(10) | Y |  |  |
| 48 | COD_SUB_OCO_TS | VARCHAR2(2) | Y |  |  |
| 49 | COD_AMP_LEG_102 | VARCHAR2(10) | Y |  |  |
| 50 | COD_SUB_OCO_102 | VARCHAR2(2) | Y |  |  |
| 51 | COD_AMP_LEG_TE_102 | VARCHAR2(10) | Y |  |  |
| 52 | COD_SUB_OCO_TE_102 | VARCHAR2(2) | Y |  |  |
| 53 | COD_AMP_LEG_TS_102 | VARCHAR2(10) | Y |  |  |
| 54 | COD_SUB_OCO_TS_102 | VARCHAR2(2) | Y |  |  |
| 55 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 56 | IND_CRED_MES_BAIXA | CHAR(1) | Y |  |  |
| 57 | TIPO_MOV | VARCHAR2(3) | Y |  |  |
| 58 | TIPO_MODELO_102 | CHAR(1) | Y |  |  |
| 59 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 60 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 61 | IND_LOCAL_BEM | CHAR(1) | Y |  |  |
| 62 | VALIDA_ETAPA_CIAP | CHAR(1) | Y | 'N' | Parametro para verificar se o usuario utilizara ou nao a validacao da ordem dos processos |
| 63 | LIM_PAG | NUMBER(3) | Y |  |  |
| 64 | LIVRO_UNICO_ANO | CHAR(1) | Y |  |  |
| 65 | NUM_PRIM_LIVRO | NUMBER(6) | Y |  |  |
| 66 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg E111/E220) -                              referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |
| 67 | COD_AJU_ICMS_TE_102 | VARCHAR2(8) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg E111/E220) -                              referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |
| 68 | COD_AJU_ICMS_TS_102 | VARCHAR2(8) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg E111/E220) -                              referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |
| 69 | IND_GER_AQUIS_ICMSS | CHAR(1) | Y |  |  |
| 70 | DAT_APROP_CRED_BEM | DATE | Y |  |  |
| 71 | IND_CRED_APUR_ICMS | CHAR(1) | Y | '1' |  |
| 72 | IND_PARCELA_SEQ | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO, ITEM_APURACAO → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_TIPO_LIVRO, ITEM_APURACAO_TE → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- TIPO_MOV → APT_TIPO_MOV(TIPO_MOV)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJU_ICMS_TE_102 → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJU_ICMS_TS_102 → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## APT_EST_MENS_ANO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | VLR_TOT_OP_ISENTAS | NUMBER(17,2) | Y |  |  |
| 5 | VLR_TOT_OP_SAIDAS | NUMBER(17,2) | Y |  |  |
| 6 | FAT_MENSAL | NUMBER(16,7) | Y |  |  |
| 7 | VLR_CRED_ENTRADA | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT_EST_MENSAL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_TRANS_CRED | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_TRANS_DEB | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_EST_ISENTAS | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | IND_LEI | CHAR(1) | N |  |  |
| 15 | VLR_CRED_ENTR_CONV | NUMBER(17,6) | Y |  |  |
| 16 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 17 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 18 | VLR_TOT_CRED_PASS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IND_LEI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_EST_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CIAP | NUMBER(12) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | FAT_MENSAL | NUMBER(16,7) | Y |  |  |
| 6 | VLR_CRED_ENTRADA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TOT_EST_MENSAL | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | IND_LEI | CHAR(1) | N |  |  |
| 11 | VLR_CRED_ENTR_CONV | NUMBER(17,6) | Y |  |  |
| 12 | COD_ESTAB_ORIG | VARCHAR2(6) | N | ' ' |  |
| 13 | VLR_CRED_POSSIVEL | NUMBER(17,2) | Y |  |  |
| 14 | DIAS_PRO_RATA | NUMBER(5) | Y |  |  |
| 15 | VLR_PASS_APROP | NUMBER(17,2) | Y |  |  |
| 16 | PARCELA_SEQ | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_CIAP, DAT_APURACAO, IND_LEI, COD_ESTAB_ORIG

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_APT_EST_SAIDA_ORIG: (COD_EMPRESA, COD_ESTAB_ORIG, NUM_CIAP, DAT_APURACAO, IND_LEI)

---

## APT_EST_SAIDA_A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CIAP | NUMBER(12) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | FAT_MENSAL | NUMBER(16,7) | Y |  |  |
| 6 | VLR_CRED_ENTRADA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TOT_EST_MENSAL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEDUCAO_EST | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SALDO_FINAL | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | IND_LEI | CHAR(1) | N |  |  |
| 13 | COD_ESTAB_ORIG | VARCHAR2(6) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_CIAP, DAT_APURACAO, IND_LEI, COD_ESTAB_ORIG

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_EXTCFO_ESTAB_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | DAT_INI_REGRA | DATE | N |  |  |
| 7 | DAT_FIN_REGRA | DATE | Y |  |  |
| 8 | NUM_PARC_AP | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, DAT_INI_REGRA

---

## APT_EXTCFO_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | TIPO_MOV | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_EXTCFO_UF_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | DAT_INI_REGRA | DATE | N |  |  |
| 7 | DAT_FIN_REGRA | DATE | Y |  |  |
| 8 | NUM_PARC_AP | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, DAT_INI_REGRA

---

## APT_IDENT_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CIAP | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_LIVRO_QUADRO5

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | NUM_CIAP | NUMBER(12) | N |  |  |
| 5 | PARCELA | NUMBER(2) | N |  |  |
| 6 | MESANO_PARC | VARCHAR2(8) | Y |  |  |
| 7 | FAT_MENSAL | NUMBER(16,7) | Y |  |  |
| 8 | VLR_CRED | NUMBER(17,2) | Y |  |  |
| 9 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, NUM_CIAP, PARCELA, COD_ESTAB_ORIG

---

## APT_MODELO_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MODELO_DOCFIS | VARCHAR2(2) | N |  |  |
| 2 | DESCR_MOD_DOCFIS | VARCHAR2(40) | Y |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | Y |  |  |

**PK**: MODELO_DOCFIS

---

## APT_NUM_LIVRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_OPER | NUMBER(4) | N |  |  |
| 4 | NUM_SEQ | NUMBER(6) | Y |  |  |
| 5 | NUM_SEQ_102 | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_OPER

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## APT_REL_CONF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_CIAP | NUMBER(12) | N |  |  |
| 6 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 7 | COD_INC | VARCHAR2(6) | Y |  |  |
| 8 | DESCR_BEM | VARCHAR2(100) | Y |  |  |
| 9 | DAT_OPER | DATE | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 13 | VLR_TOT_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PARCELA | NUMBER(3) | Y |  |  |
| 15 | VLR_CRED_PASS | NUMBER(17,2) | Y |  |  |
| 16 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 17 | USUARIO | VARCHAR2(40) | N |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 20 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 21 | PARCELA_SEQ | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, NUM_CIAP, COD_ESTAB_ORIG, USUARIO

---

## APT_REL_CONF_TOT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | VLR_TOT_OP_TRIBUT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TOT_OP_SAIDAS | NUMBER(17,2) | Y |  |  |
| 7 | COEFICIENTE | NUMBER(19,8) | Y |  |  |
| 8 | VLR_TOT_CRED_PASS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_CREDITO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUT_CRED | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | N |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, USUARIO

---

## APT_TIPO_MOV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_MOV | VARCHAR2(3) | N |  |  |
| 2 | DESCR_TIPO_MOV | VARCHAR2(50) | Y |  |  |
| 3 | IND_E_S | CHAR(1) | Y |  |  |
| 4 | IND_TRANSF | CHAR(1) | Y |  |  |

**PK**: TIPO_MOV

---

