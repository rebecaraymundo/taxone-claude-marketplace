# Módulo: ICT (ICMS) - 301 tabelas

## ICT_ACUMULADO_INCE
**Comment**: Valores acumulados durante o periodo de validade da regra

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 4 | VALIDADE_INICIAL | DATE | N |  |  |
| 5 | MES_ANO | NUMBER(6) | N |  |  |
| 6 | VLR_REAL_MES | NUMBER(17,6) | Y |  |  |
| 7 | VLR_REAL_ACUMUL | NUMBER(19,6) | Y |  |  |
| 8 | VLR_META_ACUMUL | NUMBER(19,6) | Y |  |  |
| 9 | VLR_DIREITO_ACUMUL | NUMBER(19,6) | Y |  |  |
| 10 | VLR_USADO_ACUMUL | NUMBER(17,6) | Y |  |  |
| 11 | VLR_USADO_MES_CALC | NUMBER(17,6) | Y |  |  |
| 12 | VLR_USADO_MES | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, VALIDADE_INICIAL, MES_ANO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, VALIDADE_INICIAL → ICT_REGRA_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, VALIDADE_INICIAL)

---

## ICT_AGENCIA_GNRE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | NRO_BANCO | VARCHAR2(3) | N |  |  |
| 5 | NRO_AGENCIA | VARCHAR2(6) | N |  |  |
| 6 | NOM_AGENCIA | VARCHAR2(20) | Y |  |  |
| 7 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 8 | DAT_VALIDADE | DATE | Y |  |  |
| 9 | IND_BANCO_PREF | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO, NRO_BANCO, NRO_AGENCIA, COD_GNRE

---

## ICT_AJUSTE_ICMS
**Comment**: Tabela de Códigos de Ajustes p/ Lançamento na Apuração do ICMS e ICMS-ST (Tabela 5.1.1 do SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 2 | DSC_AJUSTE_ICMS | VARCHAR2(300) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |

**PK**: COD_AJUSTE_ICMS

---

## ICT_AJUSTE_INCENT
**Comment**: Tabela dos Ajustes do Beneficio por Grupo de Incentivo.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 4 | NUM_DECRETO_BF | VARCHAR2(5) | N |  |  |
| 5 | DAT_DECRETO_BF | DATE | N |  |  |
| 6 | IND_NAT_BF | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, NUM_DECRETO_BF, DAT_DECRETO_BF

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT → ICT_GRP_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT)

---

## ICT_ALC_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO_MSAF | NUMBER(5) | N |  |  |
| 3 | COD_MUNICIPIO_DEST | NUMBER(5) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO_MSAF

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO_MSAF → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## ICT_AM_ALIQ_FRETE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_VIA_TRANSP | VARCHAR2(9) | N |  |  |
| 4 | COD_VIA_TRANSPORTE | VARCHAR2(5) | N |  |  |
| 5 | VLR_ALIQ_AM | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_VIA_TRANSP, COD_VIA_TRANSPORTE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_AM_AP_CI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOC_FIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOC_FIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 8 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 9 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 10 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 11 | IND_PRODUTO | CHAR(1) | N |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 13 | VLR_TOT_NOTA | NUMBER(17) | Y |  |  |
| 14 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 15 | COD_LINHA_PRD | VARCHAR2(5) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 17 | COD_DCR | VARCHAR2(15) | Y |  |  |
| 18 | VLR_IMPOST_USS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_INDICE | NUMBER(14,6) | Y |  |  |
| 20 | DATA_COTACAO | DATE | Y |  |  |
| 21 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 22 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 23 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 24 | QTD_VOLUMES | NUMBER(17) | Y |  |  |
| 25 | DATA_FIM | DATE | Y |  |  |
| 26 | VLR_COEF_RED | NUMBER(7,4) | Y |  |  |
| 27 | USUARIO | VARCHAR2(40) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOC_FIS, SERIE_DOC_FIS, SUB_SERIE_DOCFIS, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)

---

## ICT_AM_AP_E_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, COD_LINHA_PRD, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_AP_INS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 6 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 7 | IND_PRODUTO | CHAR(1) | N |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 9 | GRUPO_INSUMO | VARCHAR2(9) | N |  |  |
| 10 | IND_INSUMO | CHAR(1) | N |  |  |
| 11 | COD_INSUMO | VARCHAR2(60) | N |  |  |
| 12 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, COD_LINHA_PRD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_INSUMO, IND_INSUMO, COD_INSUMO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, COD_LINHA_PRD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO → ICT_AM_AP_PRD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, COD_LINHA_PRD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)

---

## ICT_AM_AP_IT_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | DATA_FISCAL | DATE | N |  |  |
| 10 | MOVTO_E_S | CHAR(1) | N |  |  |
| 11 | NORM_DEV | CHAR(1) | N |  |  |
| 12 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 13 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 14 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 15 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 16 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 17 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 18 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 19 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 20 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 21 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 22 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 23 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 24 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_ICMS_TRIB | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE_ICMS_ISENT | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_ICMS_OUTR | NUMBER(17,2) | Y |  |  |
| 28 | ALIQ_TRIBUTO_ICMSS | NUMBER(7,4) | Y |  |  |
| 29 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_TAXA | NUMBER(7,4) | Y |  |  |
| 32 | VLR_CONTRIBUICAO | NUMBER(17,2) | Y |  |  |
| 33 | USUARIO | VARCHAR2(40) | Y |  |  |
| 34 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**Indexes**:
- UK_ICT_AM_AP_IT_NF (UNIQUE): (COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, COD_LINHA_PRD, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

---

## ICT_AM_AP_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | DAT_FISCAL | DATE | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | DSC_FIS_JUR | VARCHAR2(70) | N |  |  |
| 14 | DAT_EMISSAO | DATE | Y |  |  |
| 15 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TRIB_PRES | NUMBER(17,2) | Y |  |  |
| 18 | DAT_EXTEMP | DATE | Y |  |  |
| 19 | COD_CANAL_DISTRIB | VARCHAR2(10) | Y |  |  |
| 20 | NUM_NF_DEV | VARCHAR2(12) | Y |  |  |
| 21 | SERIE_NF_DEV | VARCHAR2(3) | Y |  |  |
| 22 | S_SERIE_NF_DEV | VARCHAR2(2) | Y |  |  |
| 23 | DATA_FISCAL_DEV | DATE | Y |  |  |
| 24 | VLR_CONTAB_DEV | NUMBER(17,2) | Y |  |  |
| 25 | VLR_NDESTAC_DEV | NUMBER(17,2) | Y |  |  |
| 26 | USUARIO | VARCHAR2(40) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, COD_LINHA_PRD, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DSC_FIS_JUR

---

## ICT_AM_AP_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 6 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 7 | IND_PRODUTO | CHAR(1) | N |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, COD_LINHA_PRD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_ARV_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_VALIDADE | DATE | N |  |  |
| 5 | NUM_DCR | VARCHAR2(9) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 8 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 9 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_VALIDADE, NUM_DCR, IDENT_PRODUTO, IDENT_INSUMO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)

---

## ICT_AM_CANAL_REG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | Y |  |  |
| 5 | COD_LINHA_PRD | VARCHAR2(5) | Y |  |  |
| 6 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 7 | DATA_FISCAL | DATE | Y |  |  |
| 8 | COD_CANAL_DISTRIB | VARCHAR2(10) | Y |  |  |
| 9 | COD_REGIAO | NUMBER(2) | Y |  |  |
| 10 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 11 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE1_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE1_IPI | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE1_ICMSS | NUMBER(17,2) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_ICTAM_CAN_REG (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_ESTRUT, COD_LINHA_PRD, COD_CFO, DATA_FISCAL, COD_CANAL_DISTRIB, COD_REGIAO)

---

## ICT_AM_CFO_AP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 5 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)

---

## ICT_AM_CFO_AP_DEV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 5 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)

---

## ICT_AM_CFO_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | IND_TIPO_CREDITO | CHAR(1) | N |  | 1-Credito Estimulo;2-Credito Presumido |
| 6 | IND_PARAM_CALCULO | CHAR(1) | N |  | 1-Valor Contabil;2-Base Tributada;3-Valor Icms;4-Base Outras;5-Base Isenta |
| 7 | ALIQUOTA | NUMBER(7,4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_CFO

---

## ICT_AM_CINFO_CCONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TP_OBRIG | VARCHAR2(3) | N |  |  |
| 4 | COD_TP_INFO | VARCHAR2(5) | N |  |  |
| 5 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 6 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TP_OBRIG, COD_TP_INFO, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TP_OBRIG, COD_TP_INFO → ICT_AM_CLASSE_INFO(COD_EMPRESA, COD_ESTAB, COD_TIPO_OBRIG, COD_TIPO_INFO)

---

## ICT_AM_CLASSE_INFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_OBRIG | VARCHAR2(3) | N |  |  |
| 4 | COD_TIPO_INFO | VARCHAR2(5) | N |  |  |
| 5 | DESCRICAO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_OBRIG, COD_TIPO_INFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_AM_COD_SEFAZ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_RECEITA_SEFAZ | VARCHAR2(5) | N |  |  |
| 3 | COD_COMP_APUR | VARCHAR2(2) | Y |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | Y |  |  |
| 5 | COD_ITEM_APUR | VARCHAR2(3) | Y |  |  |
| 6 | COD_CLASSE | VARCHAR2(3) | Y |  |  |

**PK**: IDENT_ESTADO, COD_RECEITA_SEFAZ

**FKs**:
- COD_CLASSE → PRT_CLASSE_MSAF(COD_CLASSE)

---

## ICT_AM_COMP_AP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMPONENTE | VARCHAR2(2) | N |  |  |
| 4 | DSC_COMPONENTE | VARCHAR2(100) | Y |  |  |
| 5 | COD_COMP_INC | VARCHAR2(2) | Y |  |  |
| 6 | COD_ESTRUT_INC | VARCHAR2(2) | Y |  |  |
| 7 | COD_ITEM_INC | VARCHAR2(3) | Y |  |  |
| 8 | COD_COMP_NINC | VARCHAR2(2) | Y |  |  |
| 9 | COD_ESTRUT_NINC | VARCHAR2(2) | Y |  |  |
| 10 | COD_ITEM_NINC | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMPONENTE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_AM_COMP_APURAC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_COMPONENTE | VARCHAR2(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 3 | IND_INCENT | CHAR(1) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 6 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 7 | IND_PAR_CFOP_NAT | CHAR(1) | Y |  |  |
| 8 | COD_COMP_APUR | VARCHAR2(2) | Y |  |  |
| 9 | COD_ESTRUT | VARCHAR2(2) | Y |  |  |
| 10 | COD_ITEM_APUR | VARCHAR2(3) | Y |  |  |
| 11 | IND_N_INCENT | CHAR(1) | Y |  |  |
| 12 | COD_TP_LIVRO_NINC | VARCHAR2(3) | Y |  |  |
| 13 | COD_OPER_APUR_NINC | VARCHAR2(5) | Y |  |  |
| 14 | COD_CLASSE_NINC | VARCHAR2(3) | Y |  |  |
| 15 | COD_COMP_NINC | VARCHAR2(2) | Y |  |  |
| 16 | COD_ESTRUT_NINC | VARCHAR2(2) | Y |  |  |
| 17 | COD_ITEM_APUR_NINC | VARCHAR2(3) | Y |  |  |
| 18 | DSC_APUR_INC | VARCHAR2(100) | Y |  |  |
| 19 | DSC_APUR_NINC | VARCHAR2(100) | Y |  |  |

**PK**: COD_COMPONENTE

---

## ICT_AM_COMP_INDUST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | COD_REGIAO | NUMBER(2) | N |  |  |
| 7 | COD_CFO | VARCHAR2(5) | N |  |  |
| 8 | ALIQUOTA | NUMBER(11,4) | N |  |  |
| 9 | DAT_MOVTO | DATE | N |  |  |
| 10 | VLR_CONTAB_INCENT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_INCENT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_INCENT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CONTAB_NINCENT | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_NINCENT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_NINCENT | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IDENT_ESTADO, COD_REGIAO, COD_CFO, ALIQUOTA, DAT_MOVTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_ESTADO, COD_REGIAO → DWT_DEF_REGIAO(IDENT_ESTADO, COD_REGIAO)

---

## ICT_AM_CTRANSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | DAT_EMISSAO | DATE | N |  |  |
| 10 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 12 | ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 13 | VLR_ICMS_RETIDO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CRED_PRESUMIDO | NUMBER(17,2) | Y |  |  |
| 15 | CNPJ_DEST | VARCHAR2(14) | Y |  |  |
| 16 | RAZAO_SOCIAL_DEST | VARCHAR2(60) | Y |  |  |
| 17 | INSC_ESTADUAL_DEST | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DAT_EMISSAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1577: (IDENT_FIS_JUR)

---

## ICT_AM_CTR_CI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_EMISSAO | DATE | N |  |  |
| 4 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 7 | SEQUENCIAL | NUMBER(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

---

## ICT_AM_CTR_INTERNA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | NUM_CONTROLE | NUMBER(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_DCR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_DCR | VARCHAR2(15) | N |  |  |
| 4 | DATA_VALID | DATE | N |  |  |
| 5 | DATA_RECEB | DATE | Y |  |  |
| 6 | NUM_PROTOCOLO | VARCHAR2(15) | Y |  |  |
| 7 | NUM_CONTROLE | VARCHAR2(15) | Y |  |  |
| 8 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 9 | DENOM_PRODUTO | VARCHAR2(50) | Y |  |  |
| 10 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 11 | PESO_BRUTO | NUMBER(13,4) | Y |  |  |
| 12 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 13 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 14 | PROC_PRODUTIVO | VARCHAR2(100) | Y |  |  |
| 15 | VLR_SALAR_USS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ENCARG_USS | NUMBER(17,2) | Y |  |  |
| 17 | IND_COEFIC_RED | CHAR(1) | Y |  |  |
| 18 | IND_TIPO_DCR | CHAR(1) | Y |  |  |
| 19 | NUM_DCR_ANT | VARCHAR2(15) | Y |  |  |
| 20 | NUM_PROC_ANT | VARCHAR2(15) | Y |  |  |
| 21 | VLR_COEF_RED | NUMBER(7,4) | Y |  |  |
| 22 | PESO_LIQUIDO | NUMBER(13,4) | Y |  |  |
| 23 | DSC_DCR | VARCHAR2(50) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_DCR, DATA_VALID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## ICT_AM_DCR_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_DCR | VARCHAR2(15) | N |  |  |
| 4 | DATA_VALID | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | VLR_VENDA_USS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_IMPOST_USS | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_DCR, DATA_VALID, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_DCR, DATA_VALID → ICT_AM_DCR(COD_EMPRESA, COD_ESTAB, COD_DCR, DATA_VALID)

---

## ICT_AM_DM_AP_ICM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 10 | ALIQUOTA | NUMBER(11,4) | N |  |  |
| 11 | VLR_BASE_CALC_ENT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_CRED | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_CALC_SAI | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_DEB | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_RETIT | NUMBER(17,2) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, COD_LINHA_PRD, ALIQUOTA

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)

---

## ICT_AM_DM_OP_NINC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | VLR_BASE_CALC_ENT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_CRED | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_CALC_SAI | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_DEB | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_N_INCEN | NUMBER(17,2) | Y |  |  |
| 14 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 15 | VLR_OUT_CRED | NUMBER(17,2) | Y |  |  |
| 16 | VLR_OUT_DEB | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SLD_CRED_ANT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SLD_PERIODO | NUMBER(17,2) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_ESTR_AP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMPONENTE | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 5 | DSC_ESTRUT | VARCHAR2(50) | Y |  |  |
| 6 | COD_COMP_INC | VARCHAR2(2) | Y |  |  |
| 7 | COD_ESTRUT_INC | VARCHAR2(2) | Y |  |  |
| 8 | COD_ITEM_INC | VARCHAR2(3) | Y |  |  |
| 9 | COD_COMP_NINC | VARCHAR2(2) | Y |  |  |
| 10 | COD_ESTRUT_NINC | VARCHAR2(2) | Y |  |  |
| 11 | COD_ITEM_NINC | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMPONENTE → ICT_AM_COMP_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE)

---

## ICT_AM_EST_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_EXTCFO_AP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 5 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 8 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)

---

## ICT_AM_EXTCFO_AP_DEV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 5 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 8 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)

---

## ICT_AM_EXTCFO_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 7 | IND_TIPO_CREDITO | CHAR(1) | N |  | 1-Credito Estimulo;2-Credito Presumido |
| 8 | IND_PARAM_CALCULO | CHAR(1) | N |  | 1-Valor Contabil;2-Base Tributada;3-Valor Icms;4-Base Outras;5-Base Isenta |
| 9 | ALIQUOTA | NUMBER(7,4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## ICT_AM_GER_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 6 | NORM_DEV | CHAR(1) | Y |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_HANAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 5 | QUANTIDADE | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)

---

## ICT_AM_ICMS_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_MOVTO | DATE | N |  |  |
| 5 | COD_SERV_ADUAN | VARCHAR2(4) | N |  |  |
| 6 | IND_CATEGORIA | CHAR(1) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 10 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 11 | ALIQ_CRED_FISCAL | NUMBER(7,4) | Y |  |  |
| 12 | ALIQ_IMPORT | NUMBER(7,4) | Y |  |  |
| 13 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_MOVTO, COD_SERV_ADUAN, IND_CATEGORIA, IDENT_FIS_JUR, NUM_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_SERV_ADUAN → ICT_AM_SERV_ADUAN(COD_EMPRESA, COD_ESTAB, COD_SERV_ADUAN)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

**Indexes**:
- IX_FK_SAF_1468: (IDENT_FIS_JUR)

---

## ICT_AM_IE_CENTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_EST_CENTRAL | VARCHAR2(14) | N |  |  |
| 4 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_EST_CENTRAL, INSC_ESTADUAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_EST_CENTRAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_INFO_COMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_VALIDADE | DATE | N |  |  |
| 5 | NUM_DCR | VARCHAR2(9) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | DAT_FISCAL | DATE | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | IND_TIPO_COMP | CHAR(1) | N |  |  |
| 14 | DAT_EMISSAO | DATE | Y |  |  |
| 15 | IND_REG_SUSPENSAO | CHAR(1) | Y |  |  |
| 16 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 17 | NUM_ADICAO | VARCHAR2(3) | Y |  |  |
| 18 | NUM_ITEM_ADICAO | VARCHAR2(3) | Y |  |  |
| 19 | IND_BASE_II | CHAR(1) | Y |  |  |
| 20 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 21 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 22 | QUANTIDADE | NUMBER(15,4) | Y |  |  |
| 23 | ALIQUOTA_II | NUMBER(7,4) | Y |  |  |
| 24 | IND_REDUCAO | CHAR(1) | Y |  |  |
| 25 | VLR_CUSTO_UNIT | NUMBER(15,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_VALIDADE, NUM_DCR, IDENT_PRODUTO, IDENT_INSUMO, IDENT_FIS_JUR, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TIPO_COMP

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)

**Indexes**:
- IX_FK_SAF_1626: (IDENT_FIS_JUR)

---

## ICT_AM_INFO_TRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_INF_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | VLR_OPER_CIF | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OPER_FOB | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_INF_VENDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | IDENT_QUITACAO | NUMBER(12) | N |  |  |
| 10 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_DEB | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, IDENT_QUITACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- IDENT_QUITACAO → X2014_QUITACAO(IDENT_QUITACAO)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_INS_NCOMUM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_INTERNACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_ESCRITA_FISCAL | DATE | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 10 | SEQUENCIAL | NUMBER(2) | N |  |  |
| 11 | DAT_NOTIFICACAO | DATE | Y |  |  |
| 12 | NUM_NOTIFICACAO | VARCHAR2(10) | Y |  |  |
| 13 | IDENT_ESTADO_ORIG | NUMBER(12) | Y |  |  |
| 14 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 15 | VLR_NF | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_CALC_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 18 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | COD_ICMS | VARCHAR2(4) | Y |  |  |
| 20 | DAT_VENCTO | DATE | Y |  |  |
| 21 | ANO_REFERENCIA | NUMBER(4) | Y |  |  |
| 22 | ANO_EXERCICIO | NUMBER(4) | Y |  |  |
| 23 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 24 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_CORRECAO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_TAXA_EXPEDIENTE | NUMBER(17,2) | Y |  |  |
| 27 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 28 | IND_TRANSP | CHAR(1) | Y |  |  |
| 29 | COD_TRANSP | VARCHAR2(14) | Y |  |  |
| 30 | DAT_PROTOCOLO | DATE | Y |  |  |
| 31 | NUM_PPVI | VARCHAR2(12) | Y |  |  |
| 32 | DAT_VISTORIA | DATE | Y |  |  |
| 33 | NUM_VISTORIA | VARCHAR2(14) | Y |  |  |
| 34 | IND_VIST_LIBERADA | CHAR(1) | Y |  |  |
| 35 | MES_REFERENCIA | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_ESCRITA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_FIS_JUR, COD_FIS_JUR, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_ESTADO_ORIG, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## ICT_AM_IT_CANAL_AP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 5 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 6 | COD_CANAL_DISTRIB | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, COD_CANAL_DISTRIB

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_CANAL_DISTRIB → DWT_CANAIS_DISTRIB(COD_CANAL_DISTRIB)

**Indexes**:
- IX_ICTAM_ITCAN_AP (UNIQUE): (COD_CANAL_DISTRIB)

---

## ICT_AM_IT_ESTR_AP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMPONENTE | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 5 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 6 | DSC_ITEM_APUR | VARCHAR2(50) | Y |  |  |
| 7 | COD_COMP_INC | VARCHAR2(2) | Y |  |  |
| 8 | COD_ESTRUT_INC | VARCHAR2(2) | Y |  |  |
| 9 | COD_ITEM_INC | VARCHAR2(3) | Y |  |  |
| 10 | COD_COMP_NINC | VARCHAR2(2) | Y |  |  |
| 11 | COD_ESTRUT_NINC | VARCHAR2(2) | Y |  |  |
| 12 | COD_ITEM_NINC | VARCHAR2(3) | Y |  |  |
| 13 | COD_TP_LIVRO | VARCHAR2(3) | Y |  |  |
| 14 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 15 | DSC_APUR | VARCHAR2(100) | Y |  |  |
| 16 | COD_CLASSE | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT → ICT_AM_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT)

---

## ICT_AM_LINHAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 5 | DSC_LINHA_PRD | VARCHAR2(50) | Y |  |  |
| 6 | VLR_PERC_REDUC | NUMBER(7,4) | Y |  |  |
| 7 | VLR_PERC_MAX | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_LINHAP_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | Y |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | IND_PRD_GEN | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)

---

## ICT_AM_LINHAP_TPPRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | Y |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 6 | COD_GRUPO_PROD | VARCHAR2(5) | N |  |  |

**PK**: COD_GRUPO_PROD, INSC_ESTADUAL, COD_ESTAB, COD_EMPRESA

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)

---

## ICT_AM_LOG_NF

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
| 11 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 12 | COD_COMPONENTE | VARCHAR2(2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## ICT_AM_MAO_OBRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_APURACAO | DATE | N |  |  |
| 5 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 6 | VLR_MAO_OBRA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_APURACAO, COD_LINHA_PRD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)

---

## ICT_AM_MOVTO_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TP_OBRIG | VARCHAR2(3) | N |  |  |
| 4 | COD_TP_INFO | VARCHAR2(5) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | QUANTIDADE | NUMBER(6) | Y |  |  |
| 7 | VALOR | NUMBER(17,2) | Y |  |  |
| 8 | DAT_RECOLHIMENTO | DATE | Y |  |  |
| 9 | LOCAL_RECOLHIMENTO | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TP_OBRIG, COD_TP_INFO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TP_OBRIG, COD_TP_INFO → ICT_AM_CLASSE_INFO(COD_EMPRESA, COD_ESTAB, COD_TIPO_OBRIG, COD_TIPO_INFO)

---

## ICT_AM_MPRES_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_APURACAO | DATE | N |  |  |
| 2 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | IND_INCENTIVO | CHAR(1) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | BASE_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | BASE_ISEN_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | BASE_OUTR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: DAT_APURACAO, INSC_ESTADUAL, COD_ESTAB, COD_EMPRESA, IND_INCENTIVO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_NF_PERIODO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 9 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_NF_SUFRAMA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_GER_INTERNACAO | DATE | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 10 | NUM_ITEM | NUMBER(5) | N |  |  |
| 11 | COD_LINHA_PRD | VARCHAR2(3) | Y |  |  |
| 12 | IDENT_VIA_TRANSP | NUMBER(12) | Y |  |  |
| 13 | DAT_EMISSAO_NF | DATE | Y |  |  |
| 14 | NUM_DCR | VARCHAR2(9) | Y |  |  |
| 15 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 16 | DAT_LIBERACAO | DATE | Y |  |  |
| 17 | VLR_QTD_MERC | NUMBER(17,6) | Y |  |  |
| 18 | VLR_INDICE | NUMBER(7,4) | Y |  |  |
| 19 | VLR_COEF_INDICE_II | NUMBER(7,4) | Y |  |  |
| 20 | VLR_COEF_II | NUMBER(7,4) | Y |  |  |
| 21 | VLR_II_CALCULADO | NUMBER(17,2) | Y |  |  |
| 22 | VLR_II_A_RECOLHER | NUMBER(17,2) | Y |  |  |
| 23 | DAT_DESEMBARACO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_GER_INTERNACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_PRODUTO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_VIA_TRANSP → X2047_VIA_TRANSP(IDENT_VIA_TRANSP)

**Indexes**:
- IX_FK_SAF_1573: (IDENT_FIS_JUR)

---

## ICT_AM_NF_TRANSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_CONHECIMENTO | VARCHAR2(12) | N |  |  |
| 7 | SERIE_CONHEC | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_CONHEC | VARCHAR2(2) | N |  |  |
| 9 | DAT_EMISSAO | DATE | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | VLR_TOTAL_MERC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IDENT_FIS_JUR, NUM_CONHECIMENTO, SERIE_CONHEC, SUB_SERIE_CONHEC, DAT_EMISSAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1581: (IDENT_FIS_JUR)

---

## ICT_AM_OPE_PREST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | IDENT_CFOP | NUMBER(12) | N |  |  |
| 10 | ALIQUOTA | NUMBER(11,4) | N |  |  |
| 11 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CRED_EXTEMP | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, IDENT_CFOP, ALIQUOTA

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- IDENT_CFOP → X2012_COD_FISCAL(IDENT_CFO)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_OP_ISENTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | IDENT_CFO | NUMBER(12) | N |  |  |
| 10 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_OUT_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 7 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 8 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_RETIFIC, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_PAR_DETOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 5 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 6 | GRUPO_DET_OPER | VARCHAR2(9) | N |  |  |
| 7 | COD_DET_OPERACAO | VARCHAR2(5) | N |  |  |
| 8 | IND_E_S | CHAR(1) | Y |  |  |
| 9 | PERC_CRED_PRES | NUMBER(7,4) | Y |  |  |
| 10 | PERC_RET_TOMADOR | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR, GRUPO_DET_OPER, COD_DET_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)

---

## ICT_AM_PAR_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 5 | DAT_VALIDADE | DATE | N |  |  |
| 6 | VLR_TAXA_FTI | NUMBER(7,4) | Y |  |  |
| 7 | VLR_TAXA_FTI_FATUR | NUMBER(7,4) | Y |  |  |
| 8 | VLT_TAXA_FMPES | NUMBER(7,4) | Y |  |  |
| 9 | VLR_LEI_HANAN | NUMBER(7,4) | Y |  |  |
| 10 | VLR_TAXA_CR_CPRES | NUMBER(7,4) | Y |  |  |
| 11 | VLR_TAXA_FTI_IMP | NUMBER(7,4) | Y |  |  |
| 12 | IND_TIPO_INCENT | VARCHAR2(2) | Y |  |  |
| 13 | VLR_TX_FTI_IMP_MP | NUMBER(7,4) | Y |  |  |
| 14 | VLR_TX_UEA | NUMBER(7,4) | Y |  |  |
| 15 | VLR_TX_UEA_FATUR | NUMBER(7,4) | Y |  |  |
| 16 | IND_CALC_ENT | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD, DAT_VALIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)

---

## ICT_AM_PAR_ESTAB_BCK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | Y |  |  |
| 5 | DAT_VALIDADE | DATE | Y |  |  |
| 6 | VLR_TAXA_FTI | NUMBER(7,4) | Y |  |  |
| 7 | VLR_TAXA_FTI_FATUR | NUMBER(7,4) | Y |  |  |
| 8 | VLT_TAXA_FMPES | NUMBER(7,4) | Y |  |  |
| 9 | VLR_LEI_HANAN | NUMBER(7,4) | Y |  |  |
| 10 | VLR_TAXA_CR_CPRES | NUMBER(7,4) | Y |  |  |
| 11 | VLR_TAXA_FTI_IMP | NUMBER(7,4) | Y |  |  |
| 12 | IND_TIPO_INCENT | VARCHAR2(2) | Y |  |  |
| 13 | VLR_TX_FTI_IMP_MP | NUMBER(7,4) | Y |  |  |
| 14 | VLR_TX_UEA | NUMBER(7,4) | Y |  |  |
| 15 | VLR_TX_UEA_FATUR | NUMBER(7,4) | Y |  |  |

---

## ICT_AM_PAR_GER_AJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 5 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 6 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 7 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 8 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 9 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 10 | DSC_COMP_OBS | VARCHAR2(500) | Y |  |  |
| 11 | IND_SUB_APUR | VARCHAR2(1) | Y |  |  |
| 12 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 13 | DSC_COMP_AJUSTE | VARCHAR2(255) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## ICT_AM_PAR_GER_DEB_ESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 5 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 6 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 7 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 8 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 9 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 10 | DSC_DEBITO | VARCHAR2(250) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ICT_AM_PAR_GER_GUIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 5 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 6 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 7 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 8 | IND_CRITERIO | VARCHAR2(1) | Y |  |  |
| 9 | NUM_DIAS | NUMBER(2) | Y |  |  |
| 10 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 11 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 12 | GRUPO_RECEITA_EST | VARCHAR2(9) | Y |  |  |
| 13 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 14 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 15 | DSC_COMPL | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)

---

## ICT_AM_PAR_GER_LANC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DSC_LANCAMENTO | VARCHAR2(100) | Y |  |  |
| 5 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 6 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 7 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 8 | COD_LINHA_PRD | VARCHAR2(5) | N | ' ' |  |
| 9 | DSC_LANCAMENTO_CIAP | VARCHAR2(100) | Y |  |  |
| 10 | COD_CLASSE_CIAP | VARCHAR2(3) | Y |  |  |
| 11 | COD_AJUSTE_ICMS_CIAP | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_CIAP → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ICT_AM_PAR_GER_LANC_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DSC_LANCAMENTO | VARCHAR2(100) | Y |  |  |
| 5 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 6 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 7 | IND_SUB_APUR | CHAR(1) | Y |  |  |

---

## ICT_AM_PAR_GER_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | COD_CFO_ENTR | VARCHAR2(4) | Y |  |  |
| 7 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | IND_MANUAL_AUT | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)

---

## ICT_AM_PAR_GER_VAL_DEC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 5 | COD_COMP_APUR | VARCHAR2(2) | N |  |  |
| 6 | COD_ESTRUT | VARCHAR2(2) | N |  |  |
| 7 | COD_ITEM_APUR | VARCHAR2(3) | N |  |  |
| 8 | COD_INF_ADIC | VARCHAR2(8) | Y |  |  |
| 9 | IND_VLR_ADIC | CHAR(1) | Y |  |  |
| 10 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 11 | DSC_COMPL | VARCHAR2(200) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)
- COD_EMPRESA, COD_ESTAB, COD_COMP_APUR, COD_ESTRUT, COD_ITEM_APUR → ICT_AM_IT_ESTR_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE, COD_ESTRUT, COD_ITEM_APUR)
- COD_INF_ADIC → EFD_INF_ADIC_APUR(COD_INF_ADIC)

---

## ICT_AM_PAR_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_COMPONENTE | VARCHAR2(2) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 8 | MOVTO_E_S | CHAR(1) | N |  |  |
| 9 | NORM_DEV | CHAR(1) | N |  |  |
| 10 | IND_GERA_NDOCTO | CHAR(1) | Y |  |  |
| 11 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 14 | IND_REPROCESSO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_COMPONENTE, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_DOCTO, MOVTO_E_S, NORM_DEV

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_EMPRESA, COD_ESTAB, COD_COMPONENTE → ICT_AM_COMP_AP(COD_EMPRESA, COD_ESTAB, COD_COMPONENTE)

---

## ICT_AM_PAR_TRANSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | IND_VIA_TRANSP | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

---

## ICT_AM_PR_ESTAB_CI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_CONV | CHAR(1) | Y |  |  |
| 4 | COD_INDICE | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## ICT_AM_REL_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_INICIO | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | IND_TIPO_CREDITO | CHAR(1) | N |  |  |
| 7 | IND_PARAM_CALCULO | CHAR(1) | N |  |  |
| 8 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 9 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 10 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 11 | BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 13 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_ICT_AM_REL_IES: (COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INICIO, DATA_FIM)

---

## ICT_AM_REL_IES_DIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_INICIO | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | IND_TIPO_CREDITO | CHAR(1) | N |  | 3-Credito Diferido |
| 7 | IND_PARAM_CALCULO | CHAR(1) | N |  | 1-Saidas Tributadas;2-Total Saidas Tributadas;3-Saidas c/Diferimento;4-Total Saidas c/Diferimento;5-Total Saidas;6-Credito Presumido;7-Proporcional Venda c/Direito a Beneficio |
| 8 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 9 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 10 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 11 | BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | PROPORCAO | NUMBER(7,4) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_ICT_AM_REL_IES_DIF: (COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INICIO, DATA_FIM)

---

## ICT_AM_REL_IES_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_INICIO | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | PERC_MAX_INCENT | NUMBER(7,4) | N |  |  |
| 7 | VLR_SAIDA_INCENT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_PR_VENDA_CRED | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_PRESUMIDO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_FRETE_OUTROS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CRED_CIAP | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CRED_ESTIMULO | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | COD_LINHA_PRD | VARCHAR2(5) | Y |  |  |
| 17 | VLR_LANCTO_CRED | NUMBER(17,2) | Y |  |  |
| 18 | VLR_LANCTO_DEB | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_ICT_AM_REL_IES_EST: (COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INICIO, DATA_FIM)

---

## ICT_AM_REL_IES_NF_PRES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_INICIO | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | DATA_FISCAL | DATE | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | N |  |  |
| 8 | NORM_DEV | CHAR(1) | N |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 16 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 17 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 18 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 19 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 20 | IND_TIPO_CREDITO | CHAR(1) | Y |  |  |
| 21 | IND_PARAM_CALCULO | CHAR(1) | Y |  |  |
| 22 | COD_LINHA_PRD | VARCHAR2(5) | Y |  |  |
| 23 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 24 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 25 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE_ICMS_TRIB | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_ICMS_ISENT | NUMBER(17,2) | Y |  |  |
| 28 | VLR_BASE_ICMS_OUTR | NUMBER(17,2) | Y |  |  |
| 29 | VLR_BASE_ICMS_PRES | NUMBER(17,2) | Y |  |  |
| 30 | ALIQ_ICMS_PRES | NUMBER(7,4) | Y |  |  |
| 31 | VLR_ICMS_PRES | NUMBER(17,2) | Y |  |  |
| 32 | USUARIO | VARCHAR2(40) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INICIO, DATA_FIM, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## ICT_AM_SERV_ADUAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_SERV_ADUAN | VARCHAR2(4) | N |  |  |
| 4 | DSC_SERV_ADUAN | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_SERV_ADUAN

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_AM_SLD_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_LINHA_PRD | VARCHAR2(5) | N |  |  |
| 6 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SLD_APUR | NUMBER(17,2) | Y |  |  |
| 9 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 10 | VLR_PERC_REST | NUMBER(7,4) | Y |  |  |
| 11 | VLR_ICMS_REST | NUMBER(17,2) | Y |  |  |
| 12 | VLR_SLD_FIM | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, COD_LINHA_PRD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_SUB_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DSC_SUB_AP1 | VARCHAR2(150) | Y |  |  |
| 5 | DSC_SUB_AP2 | VARCHAR2(150) | Y |  |  |
| 6 | DSC_SUB_AP3 | VARCHAR2(150) | Y |  |  |
| 7 | DSC_SUB_AP4 | VARCHAR2(150) | Y |  |  |
| 8 | DSC_SUB_AP5 | VARCHAR2(150) | Y |  |  |
| 9 | DSC_SUB_AP6 | VARCHAR2(150) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL

---

## ICT_AM_TAXA_PPVI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_VALIDADE | DATE | N |  |  |
| 2 | VLR_NF_INICIAL | NUMBER(17,2) | N |  |  |
| 3 | VLR_NF_FINAL | NUMBER(17,2) | N |  |  |
| 4 | TAXA_PPVI | NUMBER(11,4) | N |  |  |

**PK**: DAT_VALIDADE, VLR_NF_INICIAL, VLR_NF_FINAL, TAXA_PPVI

---

## ICT_AM_TOTAL_RATEI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_AM_VENDA_PRAZO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_QUITACAO | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_QUITACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_QUITACAO → X2014_QUITACAO(IDENT_QUITACAO)

---

## ICT_APDISC_ST_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 8 | IND_UF | CHAR(1) | N |  |  |
| 9 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 10 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 11 | VAL_ITEM_DISCRIM | NUMBER(17,2) | Y |  |  |
| 12 | IND_TIPO_DEDUCAO | CHAR(1) | Y |  |  |
| 13 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 14 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 15 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 16 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 17 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 18 | COD_AJUSTE_SEF | NUMBER(3) | Y |  |  |
| 19 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 20 | NUM_PROC | VARCHAR2(24) | Y |  |  |
| 21 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 22 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 23 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_2578: (IDENT_OBSERVACAO)

---

## ICT_APURACAO_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 8 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 9 | DAT_REALIZACAO | DATE | Y |  |  |
| 10 | DSC_OBSERVACAO | LONG | Y |  |  |
| 11 | DSC_OBS_SUBST | VARCHAR2(2000) | Y |  |  |
| 12 | DSC_OBS_FRETES | VARCHAR2(2000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO → ICT_OBRIGACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO)

---

## ICT_APURACAO_INCE_JN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 6 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 7 | DAT_APURACAO | DATE | Y |  |  |
| 8 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 9 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 10 | DAT_REALIZACAO | DATE | Y |  |  |
| 11 | DSC_OBSERVACAO | LONG | Y |  |  |
| 12 | DSC_OBS_SUBST | VARCHAR2(2000) | Y |  |  |
| 13 | DSC_OBS_FRETES | VARCHAR2(2000) | Y |  |  |
| 14 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: PROC_ID

**Indexes**:
- IX_ICT_APURACAO_INCE_JN: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_GRAVACAO)

---

## ICT_APURACAO_OBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_SEQUENCIAL | NUMBER(3) | N |  |  |
| 6 | DSC_OBSERVACAO | LONG | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ICT_APUR_DAICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_ITEM_DAICMS | VARCHAR2(5) | N |  |  |
| 6 | IND_TP_ATIV | CHAR(1) | Y |  |  |
| 7 | VLR_OPER | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_ITEM_DAICMS

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ICT_APUR_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 6 | DAT_APURACAO | DATE | Y |  |  |
| 7 | IND_ENTRADA_SAIDA | CHAR(1) | Y |  |  |
| 8 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_NTRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 14 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)

**Indexes**:
- IX_ICT_APU_INCE: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, IND_ENTRADA_SAIDA, COD_CFO)

---

## ICT_APUR_INSC_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 7 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 8 | DAT_REALIZACAO | DATE | Y |  |  |
| 9 | DSC_OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 10 | DSC_OBS_SUBST | VARCHAR2(200) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_CALEN_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ICT_APUR_INSC_EST_JN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 5 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 6 | DAT_APURACAO | DATE | Y |  |  |
| 7 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 8 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 9 | DAT_REALIZACAO | DATE | Y |  |  |
| 10 | DSC_OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 11 | DSC_OBS_SUBST | VARCHAR2(200) | Y |  |  |
| 12 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: PROC_ID

**Indexes**:
- IX_ICT_APUR_INSC_EST_JN: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_GRAVACAO)

---

## ICT_APUR_RECEITA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 5 | VLR_REC_BRUTA | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CANCELADOS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_APUR_ST_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 8 | IND_UF | CHAR(1) | N |  |  |
| 9 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 12 | IND_GER_AUTOM | CHAR(1) | Y |  |  |
| 13 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 14 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)

---

## ICT_APUR_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APUR | DATE | N |  |  |
| 5 | CLASSE_APUR | VARCHAR2(2) | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | SEQ_LANCTO | NUMBER(2) | N |  |  |
| 9 | DSC_LANCTO | VARCHAR2(150) | Y |  |  |
| 10 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 13 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 14 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR, CLASSE_APUR, IDENT_ESTADO, COD_OPER_APUR, SEQ_LANCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

---

## ICT_AP_CALC_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | VAL_APURACAO | NUMBER(17,2) | Y |  |  |
| 9 | COD_CLASSE | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, COD_OPER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

---

## ICT_AP_CFO_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IND_INCENTIVO | CHAR(1) | N |  |  |
| 7 | COD_CFO | VARCHAR2(4) | N |  |  |
| 8 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_1 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_2 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_3 | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_ENTRADA_SAIDA | CHAR(1) | Y |  |  |
| 15 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 16 | VLR_IPI_INTEGRA_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_IPI_NINTEGRA_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_CFO

---

## ICT_AP_DEM_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | COD_DET_PRODEPE | VARCHAR2(2) | N |  |  |
| 8 | PERCENTUAL_INCENT | NUMBER(7,4) | Y |  |  |
| 9 | VLR_DET_PRODEPE | NUMBER(17,2) | Y |  |  |
| 10 | COD_GRP_INCENT | VARCHAR2(5) | Y |  |  |
| 11 | VLR_TOTAL_SAI | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TOT_DEVOL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, COD_DET_PRODEPE

---

## ICT_AP_DISC_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 9 | VAL_ITEM_DISCRIM | NUMBER(17,2) | Y |  |  |
| 10 | IND_TIPO_DEDUCAO | CHAR(1) | Y |  |  |
| 11 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 12 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 13 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 14 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 15 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 16 | IND_CALCULA_CRED | CHAR(1) | Y | 'N' |  |
| 17 | COD_AJUSTE_SEF | NUMBER(3) | Y |  |  |
| 18 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 19 | NUM_PROC | VARCHAR2(24) | Y |  |  |
| 20 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 21 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 22 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 23 | IND_LANC_TRANSF_CRED | CHAR(1) | Y |  |  |
| 24 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 25 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_2577: (IDENT_OBSERVACAO)

---

## ICT_AP_UF_D_C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | SEQ_ITEM | NUMBER(2) | N |  |  |
| 6 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 7 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 8 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 9 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 10 | IDENT_ESTADO_ESTAB | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, IDENT_ESTADO, SEQ_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_CAD_ER_TELE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | COD_ERRO | NUMBER(6) | N |  |  |

**PK**: USUARIO, COD_ERRO

---

## ICT_CALEND_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | DAT_PREVISTA_REAL | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO → ICT_OBRIGACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO)

---

## ICT_CALEN_INSC_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | DAT_PREVISTA_REAL | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO → ICT_OBRIG_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO)

---

## ICT_CANA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO | NUMBER(4) | N |  |  |
| 4 | MES | NUMBER(2) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | DAT_FISCAL | DATE | N |  |  |
| 12 | ANO_SAFRA | NUMBER(4) | Y |  |  |
| 13 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 14 | QTD_PRODUTO | NUMBER(17,6) | Y |  |  |
| 15 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 16 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 17 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | N |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 22 | COD_CFO | VARCHAR2(4) | Y |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, ANO, MES, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DAT_FISCAL

---

## ICT_CANA_CFO_PFJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 6 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_CFO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

---

## ICT_CANA_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO | NUMBER(4) | N |  |  |
| 4 | MES | NUMBER(2) | N |  |  |
| 5 | VLR_DEB | NUMBER(17,2) | Y |  |  |
| 6 | DSC_DEB | VARCHAR2(60) | Y |  |  |
| 7 | VLR_CRED | NUMBER(17,2) | Y |  |  |
| 8 | DSC_CRED | VARCHAR2(60) | Y |  |  |
| 9 | OBS | VARCHAR2(250) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | N |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, ANO, MES

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_CANA_PFJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_CANA_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | COD_NBM | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**Indexes**:
- IX_ICT_CANA_PRD: (GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)

---

## ICT_CANA_VLR_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | DAT_PRECO | DATE | N |  |  |
| 7 | VLR_PRECO | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DAT_PRECO

**FKs**:
- COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO → ICT_CANA_PRD(COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)

---

## ICT_CLASS_PROD_SEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | COD_PROD_SEF | VARCHAR2(14) | N |  |  |

**PK**: COD_PRODUTO, IND_PRODUTO, GRUPO_PRODUTO, COD_PROD_SEF

**FKs**:
- COD_PROD_SEF → DWT_PRODUTO_SEF(COD_PROD_SEF)

---

## ICT_COD_DEB_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DEB_ICMS | NUMBER(3) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(120) | Y |  |  |
| 3 | DATA_VALID_INI | DATE | Y |  |  |
| 4 | DATA_VALID_FIN | DATE | Y |  |  |

**PK**: COD_DEB_ICMS

---

## ICT_COD_GNRE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_GNRE

---

## ICT_CONF_CAD_ERR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | COD_ERRO | NUMBER(6) | N |  |  |

**PK**: USUARIO, COD_ERRO

---

## ICT_CONF_CAD_ERR_TELE
**Comment**: Tabela de cadastro de erros para conferência ICMS - Telecomunicações

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(200) | N |  | Código do usuário |
| 2 | COD_ERRO | NUMBER(5) | N |  | Código do erro/crítica selecionada |

**PK**: USUARIO, COD_ERRO

**Indexes**:
- IDX_ICT_CONF_CAD_ERR_TELE_USU: (USUARIO)

---

## ICT_CONF_DF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 13 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 14 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 15 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 16 | COD_CLASS_DOCFIS | CHAR(1) | Y |  |  |
| 17 | SITUACAO | CHAR(1) | Y |  |  |
| 18 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_B1 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS_B2 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_B3 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS_B4 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_TRIB | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS_ALIQ | NUMBER(7,4) | Y |  |  |
| 25 | VLR_ICMS_DIF_ALIQ | NUMBER(7,4) | Y |  |  |
| 26 | VLR_IPI_B1 | NUMBER(17,2) | Y |  |  |
| 27 | VLR_IPI_B2 | NUMBER(17,2) | Y |  |  |
| 28 | VLR_IPI_B3 | NUMBER(17,2) | Y |  |  |
| 29 | VLR_IPI_B4 | NUMBER(17,2) | Y |  |  |
| 30 | VLR_IPI_TRIB | NUMBER(17,2) | Y |  |  |
| 31 | VLR_IPI_ALIQ | NUMBER(7,4) | Y |  |  |
| 32 | IND_IPI_INCLUSO | VARCHAR2(1) | Y |  |  |
| 33 | VLR_ICMS_S_B1 | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ICMS_S_TRIB | NUMBER(17,2) | Y |  |  |
| 35 | VLR_CONT_ICMS | NUMBER(17,2) | Y |  |  |
| 36 | VLR_CONT_IPI | NUMBER(17,2) | Y |  |  |
| 37 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 38 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 39 | VLR_CONT_ITEM_ICMS | NUMBER(17,2) | Y |  |  |
| 40 | VLR_CONT_ITEM_IPI | NUMBER(17,2) | Y |  |  |
| 41 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 42 | IND_NF_ESPECIAL | CHAR(1) | Y |  |  |
| 43 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 44 | VLR_CONT_TOT_ITENS | NUMBER(17,2) | Y |  |  |
| 45 | IND_RESP_VCONT_ITM | CHAR(1) | Y |  |  |
| 46 | SEQ_REG | NUMBER(12) | Y |  |  |
| 47 | VLR_ICMS_S_ALIQ | NUMBER(7,4) | Y |  |  |
| 48 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 49 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 50 | QTDE_ITEM | NUMBER(17,6) | Y |  |  |
| 51 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 52 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 53 | COD_ESTADO_ORIG | VARCHAR2(2) | Y |  |  |
| 54 | COD_ESTADO_DEST | VARCHAR2(2) | Y |  |  |
| 55 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**Indexes**:
- IX_ICT_CONF_DF: (USUARIO, SEQ_REG)

---

## ICT_CONF_ERR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | SEQ_REG | NUMBER(12) | N |  |  |
| 3 | COD_ERRO | NUMBER(6) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N | ' ' |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N | ' ' |  |

**PK**: USUARIO, SEQ_REG, COD_ERRO, COD_EMPRESA, COD_ESTAB

---

## ICT_CONF_ERR_TELE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | SEQ_REG | NUMBER(12) | N |  |  |
| 3 | COD_ERRO | NUMBER(6) | N |  |  |

**PK**: USUARIO, SEQ_REG, COD_ERRO

---

## ICT_CONF_OBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | SEQ_REG | NUMBER(12) | N |  |  |
| 3 | IND_CAPA_IT | CHAR(1) | N |  |  |
| 4 | COD_TRIB | VARCHAR2(6) | N |  |  |
| 5 | OBS_TRIB | VARCHAR2(45) | Y |  |  |
| 6 | COD_EMPRESA | VARCHAR2(3) | N | ' ' |  |
| 7 | COD_ESTAB | VARCHAR2(6) | N | ' ' |  |

**PK**: USUARIO, SEQ_REG, IND_CAPA_IT, COD_TRIB, COD_EMPRESA, COD_ESTAB

---

## ICT_CONF_TELE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | NUM_ITEM | NUMBER(7) | N |  |  |
| 10 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 11 | SITUACAO | CHAR(1) | Y |  |  |
| 12 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 14 | VLR_OUTRAS_DESP | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ABAT_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_PAGAR | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS_B1 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS_B2 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_B3 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS_B4 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_TRIB | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS_ALIQ | NUMBER(7,4) | Y |  |  |
| 23 | VLR_BASE_ICMS_DEST | NUMBER(7,4) | Y |  |  |
| 24 | VLR_TRIB_ICMS_DEST | NUMBER(7,4) | Y |  |  |
| 25 | VLR_ALIQ_ICMS_DEST | NUMBER(7,4) | Y |  |  |
| 26 | VLR_SUBST_TRIB | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_SUB_TRIB | NUMBER(17,2) | Y |  |  |
| 28 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 29 | VLR_ALIQ_ISS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_DESC_COND | NUMBER(17,2) | Y |  |  |
| 32 | SEQ_REG | NUMBER(12) | Y |  |  |
| 33 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 34 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 35 | VLR_CONT_ITEM | NUMBER(17,2) | Y |  |  |
| 36 | VLR_CONT_ITEM_TOT | NUMBER(17,2) | Y |  |  |
| 37 | VLR_CONT_ICMS | NUMBER(17,2) | Y |  |  |
| 38 | VLR_CONT_ICMS_TOT | NUMBER(17,2) | Y |  |  |
| 39 | VLR_ADIC_DESC | NUMBER(17,2) | Y |  |  |
| 40 | VLR_SERVICO_TOT | NUMBER(17,2) | Y |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM

---

## ICT_CONTROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(8) | N |  |  |
| 5 | MODELO | CHAR(1) | N |  | Modelos dos livros que estão cadastrados na ICT_PAR_MODELO_LIVRO. |
| 6 | IND_CONSOLIDA_P2 | CHAR(1) | Y |  | Parametro especifico dos livros 102 e 104, que indica se o livro foi consolidado (S/N) |
| 7 | IND_ICMS_RETIDO | CHAR(1) | Y |  | Parametro especifico do livro 002, que indica o tratamento do ICMS Retido na base outras (S/N) |

**PK**: COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, MODELO

**FKs**:
- COD_EMPRESA, COD_PROG → ICT_PROG(COD_EMPRESA, COD_PROG)

---

## ICT_CPRES_IT_PORT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | NUM_IT_PORT | NUMBER(2) | N |  |  |
| 3 | DSC_PORT | VARCHAR2(100) | Y |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 5 | COD_GRUPO_PROD | VARCHAR2(5) | Y |  |  |
| 6 | VLR_ALIQ | NUMBER(7,4) | N |  |  |
| 7 | VLR_ALIQ_CPRES | NUMBER(7,4) | Y |  |  |
| 8 | VLR_ALIQ_EST | NUMBER(7,4) | Y |  |  |

**PK**: IDENT_ESTADO, NUM_IT_PORT, VLR_ALIQ

---

## ICT_CPRES_MOV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | NUM_IT_PORT | NUMBER(2) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | VLR_ALIQ | NUMBER(7,4) | N |  |  |
| 8 | VLR_ALIQ_CPRES | NUMBER(7,4) | N |  |  |
| 9 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_CALC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_CPRES | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, IDENT_ESTADO, NUM_IT_PORT, COD_CFO, VLR_ALIQ, VLR_ALIQ_CPRES

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, NUM_IT_PORT, VLR_ALIQ → ICT_CPRES_IT_PORT(IDENT_ESTADO, NUM_IT_PORT, VLR_ALIQ)

---

## ICT_C_CONTAB_P3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | DATE | Y |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 5 | VLR_ESTOQUE_CR | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ESTOQUE_DB | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 9 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 10 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 11 | VLR_SALDO_FIM | NUMBER(17,2) | Y |  |  |
| 12 | IND_SALDO_FIM | CHAR(1) | Y |  |  |

**Indexes**:
- IX_ICT_C_CONTAB_P3_1: (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_CONTA)
- IX_ICT_C_CONTAB_P3_2: (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_CONTA, INSC_ESTADUAL)

---

## ICT_C_CONTAB_P7

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N | ' ' |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | VLR_INVENT | NUMBER(17,2) | Y |  |  |
| 6 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_CONTA

---

## ICT_DEBITO_ESP
**Comment**: Tabela que armazena os Débitos Especiais do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 6 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 7 | VAL_DEBITO | NUMBER(17,2) | Y |  |  |
| 8 | DSC_DEBITO | VARCHAR2(250) | Y |  |  |
| 9 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 10 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 11 | IND_EST_DEB_CONV | CHAR(1) | Y |  |  |
| 12 | IDENT_ESTADO_CONV | NUMBER(12) | Y |  |  |
| 13 | COD_AJ_ICMS_CONV | VARCHAR2(8) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ICT_DEBITO_ESP_AJ
**Comment**: Tabela que armazena os documentos fiscais vinculados relacionados ao Débito Especial do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 6 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 7 | DATA_FISCAL | DATE | N |  |  |
| 8 | MOVTO_E_S | CHAR(1) | N |  |  |
| 9 | NORM_DEV | CHAR(1) | N |  |  |
| 10 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 17 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 18 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, NUM_DISCRIMINACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO → ICT_DEBITO_ESP(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO)

---

## ICT_DEBITO_ESP_PROC
**Comment**: Tabela que armazena os processos e documentos de arrecadação relacionados ao Débito Especial do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 6 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 7 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 8 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 9 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 10 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 11 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 12 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |
| 13 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, NUM_DISCRIMINACAO, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO → ICT_DEBITO_ESP(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO)

---

## ICT_DEBITO_ESP_ST
**Comment**: Tabela que armazena os Débitos Especiais do ICMS-ST (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 8 | VAL_DEBITO | NUMBER(17,2) | Y |  |  |
| 9 | DSC_DEBITO | VARCHAR2(250) | Y |  |  |
| 10 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ICT_DEBITO_ESP_ST_AJ
**Comment**: Tabela que armazena os documentos fiscais vinculados relacionados ao Débito Especial do ICMS-ST (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | MOVTO_E_S | CHAR(1) | N |  |  |
| 10 | NORM_DEV | CHAR(1) | N |  |  |
| 11 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 13 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 14 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 15 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 16 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 18 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 19 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, IDENT_ESTADO, NUM_DISCRIMINACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO → ICT_DEBITO_ESP_ST(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO)

---

## ICT_DEBITO_ESP_ST_PROC
**Comment**: Tabela que armazena os processos e documentos de arrecadação relacionados ao Débito Especial do ICMS-ST (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 8 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 9 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 10 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 11 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 12 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 13 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |
| 14 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, IDENT_ESTADO, NUM_DISCRIMINACAO, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO → ICT_DEBITO_ESP_ST(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO)

---

## ICT_DEB_ESP_IES
**Comment**: Tabela que armazena os Débitos Especiais do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 8 | VAL_DEBITO | NUMBER(17,2) | Y |  |  |
| 9 | DSC_DEBITO | VARCHAR2(250) | Y |  |  |
| 10 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 11 | IND_SUB_APUR | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO

**FKs**:
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ICT_DEB_ESP_IES_AJ
**Comment**: Tabela que armazena os documentos fiscais vinculados relacionados ao Débito Especial do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | MOVTO_E_S | CHAR(1) | N |  |  |
| 10 | NORM_DEV | CHAR(1) | N |  |  |
| 11 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 13 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 14 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 15 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 16 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 17 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 18 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 19 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, INSC_ESTADUAL, COD_EMPRESA, COD_TIPO_LIVRO, NUM_DISCRIMINACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO → ICT_DEB_ESP_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO)

---

## ICT_DEB_ESP_IES_PROC
**Comment**: Tabela que armazena os processos e documentos de arrecadação relacionados ao Débito Especial do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 8 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 9 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 10 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 11 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 12 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 13 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, INSC_ESTADUAL, COD_EMPRESA, COD_TIPO_LIVRO, NUM_DISCRIMINACAO, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO → ICT_DEB_ESP_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_DISCRIMINACAO)

---

## ICT_DEB_ESP_ST_IES
**Comment**: Tabela que armazena os Débitos Especiais do ICMS-ST (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 8 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 9 | VAL_DEBITO | NUMBER(17,2) | Y |  |  |
| 10 | DSC_DEBITO | VARCHAR2(250) | Y |  |  |
| 11 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_APUR_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ICT_DEB_ESP_ST_IES_AJ
**Comment**: Tabela que armazena os documentos fiscais vinculados relacionados ao Débito Especial do ICMS-ST (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 8 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 9 | DATA_FISCAL | DATE | N |  |  |
| 10 | MOVTO_E_S | CHAR(1) | N |  |  |
| 11 | NORM_DEV | CHAR(1) | N |  |  |
| 12 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 13 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 14 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 15 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 16 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 17 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 18 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 19 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 20 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, INSC_ESTADUAL, COD_EMPRESA, COD_TIPO_LIVRO, IDENT_ESTADO, NUM_DISCRIMINACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO → ICT_DEB_ESP_ST_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO)

---

## ICT_DEB_ESP_ST_IES_PROC
**Comment**: Tabela que armazena os processos e documentos de arrecadação relacionados ao Débito Especial do ICMS-ST (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 8 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |
| 9 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 10 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 11 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 12 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 13 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 14 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, INSC_ESTADUAL, COD_EMPRESA, COD_TIPO_LIVRO, IDENT_ESTADO, NUM_DISCRIMINACAO, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO → ICT_DEB_ESP_ST_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_DISCRIMINACAO)

---

## ICT_DIF_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURAC | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | IND_TP_APURAC | CHAR(1) | N |  |  |
| 7 | NUM_ITEM_LANC | VARCHAR2(3) | N |  |  |
| 8 | NUM_SEQUENCIAL | VARCHAR2(12) | N |  |  |
| 9 | VLR_BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_IMPOSTO | NUMBER(17,2) | Y |  |  |
| 11 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 12 | DSC_LANC | VARCHAR2(50) | Y |  |  |
| 13 | VLR_ALIQ_ORIG | NUMBER(7,4) | Y |  |  |
| 14 | VLR_ALIQ_DEST | NUMBER(7,4) | Y |  |  |
| 15 | VLR_DIF_ALIQ | NUMBER(19,4) | Y |  |  |
| 16 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURAC, IDENT_ESTADO, IND_TP_APURAC, NUM_ITEM_LANC, NUM_SEQUENCIAL, IND_DEB_CRE

---

## ICT_DIF_ALIQ_DET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURAC | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | IND_TP_APURAC | CHAR(1) | N |  |  |
| 7 | NUM_ITEM_LANC | VARCHAR2(3) | N |  |  |
| 8 | NUM_SEQUENCIAL | VARCHAR2(12) | N |  |  |
| 9 | VLR_BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_IMPOSTO | NUMBER(17,2) | Y |  |  |
| 11 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 12 | DSC_LANC | VARCHAR2(50) | Y |  |  |
| 13 | VLR_ALIQ_ORIG | NUMBER(7,4) | N |  |  |
| 14 | VLR_ALIQ_DEST | NUMBER(7,4) | N |  |  |
| 15 | VLR_DIF_ALIQ | NUMBER(19,4) | N |  |  |
| 16 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURAC, IDENT_ESTADO, IND_TP_APURAC, NUM_ITEM_LANC, NUM_SEQUENCIAL, IND_DEB_CRE, VLR_ALIQ_ORIG, VLR_ALIQ_DEST, VLR_DIF_ALIQ

---

## ICT_DIF_ALIQ_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 8 | IND_TP_APURAC | CHAR(1) | N |  |  |
| 9 | NUM_ITEM_LANC | VARCHAR2(3) | N |  |  |
| 10 | NUM_SEQUENCIAL | VARCHAR2(3) | N |  |  |
| 11 | VLR_BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_IMPOSTO | NUMBER(17,2) | Y |  |  |
| 13 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 14 | DSC_LANC | VARCHAR2(50) | Y |  |  |
| 15 | VLR_ALIQ_ORIG | NUMBER(7,4) | Y |  |  |
| 16 | VLR_ALIQ_DEST | NUMBER(7,4) | Y |  |  |
| 17 | VLR_DIF_ALIQ | NUMBER(19,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_TP_APURAC, NUM_ITEM_LANC, NUM_SEQUENCIAL, IND_DEB_CRE

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)

---

## ICT_DIF_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_ESCR_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DAT_FISCAL | DATE | Y |  |  |
| 9 | VLR_NOTA_FISCAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | PERC | NUMBER(7,4) | Y |  |  |
| 13 | NUM_PARCELAS | NUMBER(3) | Y |  |  |
| 14 | VLR_PARCELA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_ESCR_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## ICT_EMIT_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 9 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 10 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |

**Indexes**:
- IX_ICT_EMIT_P1: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_FIS_JUR)

---

## ICT_ESTAB_IESTAD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | IND_CALC_ENT | CHAR(1) | Y | '1' |  |
| 5 | IND_CENTR_SPED | CHAR(1) | Y |  |  |
| 6 | IND_CLAS_ESTAB | VARCHAR2(2) | Y |  | Classificacao do Contribuinte do IPI para EFD-ICMS/IPI |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_ETAPA_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | NUM_LIVRO | VARCHAR2(6) | N |  |  |
| 8 | VRS_ETAPA | VARCHAR2(3) | N |  |  |
| 9 | NUM_PAGINA_INICIAL | VARCHAR2(6) | Y |  |  |
| 10 | NUM_PAGINA_FINAL | VARCHAR2(6) | Y |  |  |
| 11 | DAT_APUR_INI | DATE | Y |  |  |
| 12 | CALENDARIO | CHAR(1) | Y |  |  |
| 13 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ICMS1 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS2 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_ICMS3 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_IPI1 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_IPI2 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_IPI3 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 24 | IND_AUTENTIC_OK | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, NUM_LIVRO, VRS_ETAPA

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)

---

## ICT_ET_LV_INSC_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | NUM_LIVRO | VARCHAR2(6) | N |  |  |
| 7 | VRS_ETAPA | NUMBER(3) | N |  |  |
| 8 | NUM_PAGINA_INICIAL | VARCHAR2(6) | Y |  |  |
| 9 | NUM_PAGINA_FINAL | VARCHAR2(6) | Y |  |  |
| 10 | DAT_APUR_INI | DATE | Y |  |  |
| 11 | IND_CALENDARIO | CHAR(1) | Y |  |  |
| 12 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ICMS1 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ICMS2 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS3 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_IPI1 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_IPI2 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_IPI3 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 23 | IND_AUTENTIC_OK | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, NUM_LIVRO, VRS_ETAPA

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_CALEN_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ICT_EVENTO_AP_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | IND_EVENTO | CHAR(1) | N |  |  |
| 3 | COD_EVENTO | VARCHAR2(2) | N |  |  |
| 4 | DSC_EVENTO | VARCHAR2(150) | Y |  |  |

**PK**: IDENT_ESTADO, IND_EVENTO, COD_EVENTO

---

## ICT_FAIXA_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 4 | VALIDADE_INICIAL | DATE | N |  |  |
| 5 | SEQUENCIAL | NUMBER(2) | N |  |  |
| 6 | VLR_FAIXA_INI | NUMBER(17,6) | Y |  |  |
| 7 | VLR_FAIXA_FIM | NUMBER(17,6) | Y |  |  |
| 8 | PERCENTUAL_INCENT | NUMBER(7,4) | Y |  |  |
| 9 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 10 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 11 | IND_INCENTIVO_FRETE | CHAR(1) | Y |  |  |
| 12 | IND_OPER_INCENTIVADA | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, VALIDADE_INICIAL, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, VALIDADE_INICIAL → ICT_REGRA_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, VALIDADE_INICIAL)

---

## ICT_FATUR_DIRETO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 5 | VLR_BASE_ICMS_CRED | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_CRED | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS_DEB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_DEB | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SALDO_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_ESTADO

---

## ICT_FRETE_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CONHECIMENTO | VARCHAR2(12) | N |  |  |
| 4 | SERIE_CONHECIMENTO | VARCHAR2(3) | N |  |  |
| 5 | S_SERIE_CONHECIMENTO | VARCHAR2(2) | N |  |  |
| 6 | DT_CONHECIMENTO | DATE | N |  |  |
| 7 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 9 | S_SERIE_DOCFIS_REF | VARCHAR2(2) | N |  |  |
| 10 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 11 | PERCENTUAL_INCENT | NUMBER(7,4) | N |  |  |
| 12 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CALC_INCENT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_NOMINAL_INCENT | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 18 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_CONHECIMENTO, SERIE_CONHECIMENTO, S_SERIE_CONHECIMENTO, DT_CONHECIMENTO, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, S_SERIE_DOCFIS_REF, COD_GRP_INCENT, PERCENTUAL_INCENT

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT → ICT_GRP_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT)

---

## ICT_GIA_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | VLR_PRODUTOS | NUMBER(17,2) | Y |  |  |
| 6 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DESPESAS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_CPRES | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMSS_RET | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMSS_DEVOL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMSS_RESSARC | NUMBER(17,2) | Y |  |  |
| 14 | VLR_GIA_ST_MES_ANT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMSS_CRED | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMSS_RECOLHIM | NUMBER(17,2) | Y |  |  |
| 17 | OBS_COMPL | VARCHAR2(200) | Y |  |  |
| 18 | VLR_RESSARC | NUMBER(17,2) | Y |  |  |
| 19 | VLR_PAGTO_ANTECIP | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMSS_DEVIDO | NUMBER(17,2) | Y |  |  |
| 21 | VLR_REPASSE_COMB | NUMBER(17,2) | Y |  |  |
| 22 | IND_OPER_COMBUST | CHAR(1) | Y |  |  |
| 23 | IND_GIA_SUBSTIT | CHAR(1) | Y |  |  |
| 24 | IND_GIA_SEM_MOV | CHAR(1) | Y |  |  |
| 25 | DAT_VENCTO1 | DATE | Y |  |  |
| 26 | VLR_VENCTO1 | NUMBER(17,2) | Y |  |  |
| 27 | DAT_VENCTO2 | DATE | Y |  |  |
| 28 | VLR_VENCTO2 | NUMBER(17,2) | Y |  |  |
| 29 | DAT_VENCTO3 | DATE | Y |  |  |
| 30 | VLR_VENCTO3 | NUMBER(17,2) | Y |  |  |
| 31 | DAT_VENCTO4 | DATE | Y |  |  |
| 32 | VLR_VENCTO4 | NUMBER(17,2) | Y |  |  |
| 33 | DAT_VENCTO5 | DATE | Y |  |  |
| 34 | VLR_VENCTO5 | NUMBER(17,2) | Y |  |  |
| 35 | DAT_VENCTO6 | DATE | Y |  |  |
| 36 | VLR_VENCTO6 | NUMBER(17,2) | Y |  |  |
| 37 | USUARIO | VARCHAR2(40) | Y |  |  |
| 38 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 39 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 40 | VLR_OUT_CRED | NUMBER(17,2) | Y |  | criado para atendimento à DIME-SC |
| 41 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 42 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 43 | VLR_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 44 | VLR_OUT_DEB | NUMBER(17,2) | Y |  |  |
| 45 | VLR_VENCTO_FCP_1 | NUMBER(17,2) | Y |  |  |
| 46 | VLR_VENCTO_FCP_2 | NUMBER(17,2) | Y |  |  |
| 47 | VLR_VENCTO_FCP_3 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_VENCTO_FCP_4 | NUMBER(17,2) | Y |  |  |
| 49 | VLR_VENCTO_FCP_5 | NUMBER(17,2) | Y |  |  |
| 50 | VLR_VENCTO_FCP_6 | NUMBER(17,2) | Y |  |  |
| 51 | IND_EC8715_MOVIMENTO | CHAR(1) | Y |  |  |
| 52 | VLR_ICMS_DEV_UFDEST_EC8715 | NUMBER(17,2) | Y |  |  |
| 53 | VLR_DEV_ANULA_EC8715 | NUMBER(17,2) | Y |  |  |
| 54 | VLR_PAGTO_ANTECIP_EC8715 | NUMBER(17,2) | Y |  |  |
| 55 | VLR_TOT_ICMS_DEV_UFDEST_EC8715 | NUMBER(17,2) | Y |  |  |
| 56 | VLR_TOT_ICMS_FCP_EC8715 | NUMBER(17,2) | Y |  |  |
| 57 | IND_ALT_ICMSST | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_GIA_ST_ANEX1_2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | UF_FAVORECIDA | VARCHAR2(2) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DAT_EMISSAO | DATE | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 11 | IND_DEV_RES_ICMSS | CHAR(1) | Y |  |  |
| 12 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, UF_FAVORECIDA, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DAT_EMISSAO, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, UF_FAVORECIDA → ICP_GIA_ST_UF(COD_EMPRESA, COD_ESTAB, UF_FAVORECIDA)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1125: (IDENT_FIS_JUR)

---

## ICT_GIA_ST_ANEX3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | UF_FAVORECIDA | VARCHAR2(2) | N |  |  |
| 5 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 6 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIB_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, UF_FAVORECIDA, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, INSC_ESTADUAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, UF_FAVORECIDA → ICP_GIA_ST_UF(COD_EMPRESA, COD_ESTAB, UF_FAVORECIDA)

---

## ICT_GIA_ST_ANEX4

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | UF_FAVORECIDA | VARCHAR2(2) | N |  |  |
| 5 | DISCRI_ANEX4 | VARCHAR2(20) | N |  |  |
| 6 | DAT_VENCTO_DEV_UF_DEST | DATE | Y |  |  |
| 7 | VLR_ICMS_DEV | NUMBER(17,2) | Y |  |  |
| 8 | DAT_VENCTO_FCP | DATE | Y |  |  |
| 9 | VLR_ICMS_FCP | NUMBER(17,2) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, UF_FAVORECIDA, DISCRI_ANEX4

---

## ICT_GIA_ST_BK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | DATE | Y |  |  |
| 4 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 5 | VLR_PRODUTOS | NUMBER(17,2) | Y |  |  |
| 6 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DESPESAS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_CPRES | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMSS_RET | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMSS_DEVOL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMSS_RESSARC | NUMBER(17,2) | Y |  |  |
| 14 | VLR_GIA_ST_MES_ANT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMSS_CRED | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMSS_RECOLHIM | NUMBER(17,2) | Y |  |  |
| 17 | OBS_COMPL | VARCHAR2(200) | Y |  |  |
| 18 | VLR_RESSARC | NUMBER(17,2) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 20 | VLR_PAGTO_ANTECIP | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMSS_DEVIDO | NUMBER(17,2) | Y |  |  |
| 22 | VLR_REPASSE_COMB | NUMBER(17,2) | Y |  |  |
| 23 | USUARIO | VARCHAR2(40) | Y |  |  |

---

## ICT_GI_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMSS_PET_ENER | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMSS_OUTRO | NUMBER(17,2) | Y |  |  |
| 11 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 13 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 16 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |

**Indexes**:
- IX_ICT_GI_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO)

---

## ICT_GI_P1_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMSS_PET_ENER | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMSS_OUTRO | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 17 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ISENTAS_IPI | NUMBER(17,2) | Y |  |  |
| 19 | VLR_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |
| 20 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_GI_P1_M2 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_ESTADO, INSC_ESTADUAL)

---

## ICT_GI_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | VLR_CONT_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CONT_CONTR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_CONTR | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 12 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 14 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 17 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 18 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_GI_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO)

---

## ICT_GI_P2_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | VLR_CONT_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CONT_CONTR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_CONTR | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 15 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 18 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ISENTAS_IPI | NUMBER(17,2) | Y |  |  |
| 20 | VLR_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_ICT_GI_P2_M2 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_ESTADO, INSC_ESTADUAL)

---

## ICT_GNRE_CFG_DARE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 2 | COD_DARE | VARCHAR2(5) | Y |  |  |

**PK**: COD_GNRE

---

## ICT_GNRE_OL_CLAS_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROD_GNRE | NUMBER(3) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(200) | Y |  |  |

**PK**: COD_PROD_GNRE

---

## ICT_GNRE_OL_GUIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GNRE_OL_GUIA | NUMBER | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO_FAV | NUMBER(12) | N |  |  |
| 6 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 7 | COD_DET_RECEITA | VARCHAR2(6) | Y |  |  |
| 8 | COD_PROD_GNRE | NUMBER(3) | Y |  |  |
| 9 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 10 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 12 | DATA_VENC | DATE | Y |  |  |
| 13 | DATA_PAGTO | DATE | Y |  |  |
| 14 | TIPO_DOC_ORIG | NUMBER(2) | Y |  |  |
| 15 | NUM_DOCTO_ORIG | VARCHAR2(80) | Y |  |  |
| 16 | NUM_CONVENIO | VARCHAR2(50) | Y |  |  |
| 17 | IND_PERIODO_REF | CHAR(1) | Y |  |  |
| 18 | PERIODO_REF | VARCHAR2(6) | Y |  |  |
| 19 | NUM_PARCELA | NUMBER(3) | Y |  |  |
| 20 | IDENT_FIS_JUR_DEST | NUMBER(12) | Y |  |  |
| 21 | NUM_CAMPO_EXTRA1 | NUMBER(3) | Y |  |  |
| 22 | IND_CAMPO_EXTRA1 | CHAR(1) | Y |  |  |
| 23 | DSC_CAMPO_EXTRA1 | VARCHAR2(250) | Y |  |  |
| 24 | NUM_CAMPO_EXTRA2 | NUMBER(3) | Y |  |  |
| 25 | IND_CAMPO_EXTRA2 | CHAR(1) | Y |  |  |
| 26 | DSC_CAMPO_EXTRA2 | VARCHAR2(250) | Y |  |  |
| 27 | NUM_CAMPO_EXTRA3 | NUMBER(3) | Y |  |  |
| 28 | IND_CAMPO_EXTRA3 | CHAR(1) | Y |  |  |
| 29 | DSC_CAMPO_EXTRA3 | VARCHAR2(250) | Y |  |  |
| 30 | IND_ORIG_GUIA | CHAR(1) | Y |  |  |
| 31 | IND_GRAV_XML | CHAR(1) | Y |  |  |
| 32 | NUM_AUTENTIC_GNRE | VARCHAR2(64) | Y |  |  |
| 33 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 34 | NRO_BANCO | VARCHAR2(3) | Y |  |  |
| 35 | NRO_AGENCIA | VARCHAR2(6) | Y |  |  |
| 36 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 37 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 38 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 39 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 40 | INFO_COMPL | VARCHAR2(70) | Y |  |  |
| 41 | INFO_COMPL_1 | VARCHAR2(70) | Y |  |  |
| 42 | INFO_COMPL_2 | VARCHAR2(70) | Y |  |  |
| 43 | INFO_COMPL_3 | VARCHAR2(70) | Y |  |  |
| 44 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 45 | IND_APUR_REF | VARCHAR2(1) | Y | '1' |  |
| 46 | VLR_PRINCIPAL_FECP | NUMBER(17,2) | Y |  |  |
| 47 | VLR_TOTAL_FECP | NUMBER(17,2) | Y |  |  |
| 48 | VLR_GNRE | NUMBER(17,2) | Y |  |  |

**PK**: IDENT_GNRE_OL_GUIA

**FKs**:
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)
- COD_PROD_GNRE → ICT_GNRE_OL_CLAS_PROD(COD_PROD_GNRE)
- IDENT_FIS_JUR_DEST → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_2763: (IDENT_FIS_JUR_DEST)
- IX_FK_SAF_2764: (IDENT_OBSERVACAO)
- UK_ICT_GNRE_OL_GUIA (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_ESTADO_FAV, COD_GNRE, COD_DET_RECEITA, COD_PROD_GNRE, SEQUENCIAL)

---

## ICT_GNRE_OL_PROD_NBM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 3 | COD_PROD_GNRE | NUMBER(3) | N |  |  |
| 4 | COD_NBM | VARCHAR2(10) | N |  |  |

**PK**: IDENT_ESTADO, COD_GNRE, COD_PROD_GNRE, COD_NBM

**FKs**:
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)
- COD_PROD_GNRE → ICT_GNRE_OL_CLAS_PROD(COD_PROD_GNRE)

---

## ICT_GNRE_OL_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 3 | IND_DET_RECEITA | CHAR(1) | Y |  |  |
| 4 | COD_DET_RECEITA | VARCHAR2(6) | Y |  |  |
| 5 | IND_DET_PRODUTO | CHAR(1) | Y |  |  |
| 6 | IND_DOC | CHAR(1) | Y |  |  |
| 7 | IND_PERIODO | CHAR(1) | Y |  |  |
| 8 | IND_MES_ANO | CHAR(1) | Y |  |  |
| 9 | IND_DESTINATARIO | CHAR(1) | Y |  |  |
| 10 | IND_CAMPO_EXTRA | CHAR(1) | Y |  |  |
| 11 | NUM_CAMPO_EXTRA1 | NUMBER(3) | Y |  |  |
| 12 | NUM_CAMPO_EXTRA2 | NUMBER(3) | Y |  |  |
| 13 | NUM_CAMPO_EXTRA3 | NUMBER(3) | Y |  |  |
| 14 | IND_VALORES | CHAR(1) | Y |  |  |
| 15 | IND_DET_PROD_APUR | CHAR(1) | Y |  |  |
| 16 | COD_PROD_GNRE | NUMBER(3) | Y |  | Codigo de classificação do produto (Tabela origem ICT_GNRE_OL_CLAS_PROD) |

**PK**: IDENT_ESTADO, COD_GNRE

**FKs**:
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)

---

## ICT_GNRE_OL_UF_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 3 | COD_PROD_GNRE | NUMBER(3) | N |  |  |
| 4 | NUM_CONVENIO | VARCHAR2(10) | Y |  |  |
| 5 | IND_PERIOD_REC | CHAR(1) | Y |  |  |
| 6 | IND_DIAS_REC | CHAR(1) | Y |  |  |
| 7 | NUM_DIAS_VENC | NUMBER(2) | Y |  |  |

**PK**: IDENT_ESTADO, COD_GNRE, COD_PROD_GNRE

**FKs**:
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)
- COD_PROD_GNRE → ICT_GNRE_OL_CLAS_PROD(COD_PROD_GNRE)

---

## ICT_GNRE_OL_UF_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 3 | NUM_CONVENIO | VARCHAR2(10) | Y |  |  |
| 4 | IND_PERIOD_REC | CHAR(1) | Y |  |  |
| 5 | IND_DIAS_REC | CHAR(1) | Y |  |  |
| 6 | NUM_DIAS_VENC | NUMBER(2) | Y |  |  |

**PK**: IDENT_ESTADO, COD_GNRE

**FKs**:
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)

---

## ICT_GRP_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 4 | DSC_GRP_INCENT | VARCHAR2(50) | Y |  |  |
| 5 | IND_GRP_ESP | CHAR(1) | Y |  |  |
| 6 | IND_TP_CONV | CHAR(1) | Y |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 8 | DSC_OPER_APUR | VARCHAR2(150) | Y |  |  |
| 9 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 10 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 11 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 12 | COD_CFO_E | VARCHAR2(4) | Y |  |  |
| 13 | GRUPO_NATUREZA_OP_E | VARCHAR2(9) | Y |  |  |
| 14 | COD_NATUREZA_OP_E | VARCHAR2(3) | Y |  |  |
| 15 | COD_CFO_S | VARCHAR2(4) | Y |  |  |
| 16 | GRUPO_NATUREZA_OP_S | VARCHAR2(9) | Y |  |  |
| 17 | COD_NATUREZA_OP_S | VARCHAR2(3) | Y |  |  |
| 18 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 19 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 20 | PERC_LIMITE_SUCATA | NUMBER(7,4) | Y |  |  |
| 21 | COD_OPER_APUR_E | VARCHAR2(5) | Y |  |  |
| 22 | DSC_OPER_APUR_E | VARCHAR2(150) | Y |  |  |
| 23 | COD_CLASSE_E | VARCHAR2(3) | Y |  |  |
| 24 | COD_AMPARO_LEGAL_E | VARCHAR2(10) | Y |  |  |
| 25 | COD_SUB_ITEM_OCORR_E | VARCHAR2(2) | Y |  |  |
| 26 | COD_OPER_APUR_EST | VARCHAR2(5) | Y |  | Item da apuracao que sera gerado o lancamento do estorno de credito |
| 27 | DSC_OPER_APUR_EST | VARCHAR2(150) | Y |  |  |
| 28 | COD_CLASSE_EST | VARCHAR2(3) | Y |  |  |
| 29 | COD_AMP_LEGAL_EST | VARCHAR2(10) | Y |  |  |
| 30 | COD_SUBIT_OCORR_EST | VARCHAR2(2) | Y |  |  |
| 31 | IND_INCENTIVO_FRETE | CHAR(1) | Y |  |  |
| 32 | NUM_DECRETO_BF | VARCHAR2(5) | Y |  |  |
| 33 | DAT_DECRETO_BF | DATE | Y |  |  |
| 34 | IND_NAT_BF | CHAR(1) | Y |  |  |
| 35 | IND_ICMS_BF | CHAR(1) | Y |  |  |
| 36 | PRAZO_FRUICAO | NUMBER | Y |  |  |
| 37 | COD_AJUSTE_SEF | NUMBER(3) | Y |  |  |
| 38 | COD_AJUSTE_SEF_E | NUMBER(3) | Y |  |  |
| 39 | COD_AJUSTE_SEF_EST | NUMBER(3) | Y |  |  |
| 40 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 41 | COD_AJUSTE_ICMS_E | VARCHAR2(8) | Y |  |  |
| 42 | COD_AJUSTE_ICMS_EST | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_GUIA_GNRE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 6 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 7 | NUM_DOCTO_ORIG | VARCHAR2(20) | Y |  |  |
| 8 | PERIODO_REF | VARCHAR2(20) | Y |  |  |
| 9 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ATUAL_MONET | NUMBER(17,2) | Y |  |  |
| 11 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TOT_RECOLHER | NUMBER(17,2) | Y |  |  |
| 14 | DAT_VENCTO | DATE | Y |  |  |
| 15 | NUM_CONVENIO | VARCHAR2(50) | Y |  |  |
| 16 | INSC_UF_FAVORECIDA | VARCHAR2(18) | Y |  |  |
| 17 | INFO_COMPL | VARCHAR2(70) | Y |  |  |
| 18 | INFO_COMPL_1 | VARCHAR2(70) | Y |  |  |
| 19 | INFO_COMPL_2 | VARCHAR2(70) | Y |  |  |
| 20 | INFO_COMPL_3 | VARCHAR2(70) | Y |  |  |
| 21 | NRO_BANCO | VARCHAR2(3) | Y |  |  |
| 22 | NRO_AGENCIA | VARCHAR2(6) | Y |  |  |
| 23 | NUM_AUTENTIC_GNRE | VARCHAR2(64) | Y |  |  |
| 24 | IDENT_ESTADO_FAV | NUMBER(12) | Y |  |  |
| 25 | DAT_RECOLH | DATE | Y |  |  |
| 26 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 27 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 28 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 29 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 30 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 31 | COD_DEB_ICMS | NUMBER(3) | Y |  |  |
| 32 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, COD_GNRE, SEQUENCIAL

**FKs**:
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)
- COD_DEB_ICMS → ICT_COD_DEB_ICMS(COD_DEB_ICMS)

---

## ICT_GUIA_GNRE_CON

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 6 | SEQUENCIAL | NUMBER(12) | N |  |  |
| 7 | NUM_DOCTO | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | PERIODO_REF | VARCHAR2(20) | Y |  |  |
| 11 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ATUAL_MONET | NUMBER(17,2) | Y |  |  |
| 13 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TOT_RECOLHER | NUMBER(17,2) | Y |  |  |
| 16 | DAT_VENCTO | DATE | Y |  |  |
| 17 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 18 | COD_REL | VARCHAR2(10) | N |  |  |
| 19 | NUM_CONVENIO | VARCHAR2(50) | Y |  |  |
| 20 | INSC_UF_FAVORECIDA | VARCHAR2(18) | Y |  |  |
| 21 | INFO_COMPL | VARCHAR2(70) | Y |  |  |
| 22 | INFO_COMPL_1 | VARCHAR2(70) | Y |  |  |
| 23 | INFO_COMPL_2 | VARCHAR2(70) | Y |  |  |
| 24 | INFO_COMPL_3 | VARCHAR2(70) | Y |  |  |
| 25 | NRO_BANCO | VARCHAR2(3) | Y |  |  |
| 26 | NRO_AGENCIA | VARCHAR2(6) | Y |  |  |
| 27 | NUM_AUTENTIC_GNRE | VARCHAR2(64) | Y |  |  |
| 28 | IDENT_ESTADO_FAV | NUMBER(12) | Y |  |  |
| 29 | DAT_RECOLH | DATE | Y |  |  |
| 30 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 31 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 32 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 33 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 34 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 35 | IND_GNRE_GERADA | CHAR(1) | Y | 'N' | S- Sim N- Não |
| 36 | IDENT_GNRE_GERADA | NUMBER(12) | Y |  |  |
| 37 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 38 | COD_DEB_ICMS | NUMBER(3) | Y |  |  |
| 39 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, COD_GNRE, CLASSE_REL, COD_REL, SEQUENCIAL

**FKs**:
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)
- COD_DEB_ICMS → ICT_COD_DEB_ICMS(COD_DEB_ICMS)

---

## ICT_GUIA_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 4 | IDENT_ITENS_MERC | NUMBER(12) | N |  |  |
| 5 | DATA_FISCAL | DATE | Y |  |  |
| 6 | IND_E_S | CHAR(1) | Y |  |  |
| 7 | COD_GRP_INCENT | VARCHAR2(5) | Y |  |  |
| 8 | PERCENTUAL_INCENT | NUMBER(7,4) | Y |  |  |
| 9 | IND_INCENT | CHAR(1) | Y |  |  |
| 10 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 11 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 12 | COD_INF_ADIC | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_DOCTO_FISCAL, IDENT_ITENS_MERC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_ICT_GUIA_INCENT_01: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_GRP_INCENT)

---

## ICT_GUIA_REC_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | NUM_GUIA_RECOL | VARCHAR2(25) | N |  |  |
| 8 | DAT_GUIA_RECOL | DATE | Y |  |  |
| 9 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 10 | DAT_ENTREGA | DATE | Y |  |  |
| 11 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 12 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |
| 13 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 14 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 15 | IND_SJ | CHAR(1) | Y |  |  |
| 16 | MES_ANO_REF | DATE | Y |  |  |
| 17 | DAT_VENCTO | DATE | Y |  |  |
| 18 | DSC_COMPLEMENTAR | VARCHAR2(100) | Y |  |  |
| 19 | IND_TIPO_DOC_ARREC | CHAR(1) | Y |  |  |
| 20 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 21 | NUM_AUTENTIC | VARCHAR2(25) | Y |  |  |
| 22 | VAL_DOC_ORIG | NUMBER(17,2) | Y |  |  |
| 23 | VAL_DESCONTO | NUMBER(17,2) | Y |  |  |
| 24 | VAL_MULTA_MORA | NUMBER(17,2) | Y |  |  |
| 25 | VAL_JUROS | NUMBER(17,2) | Y |  |  |
| 26 | VAL_MULTA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## ICT_GUIA_ST_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | NUM_GUIA_RECOL | VARCHAR2(25) | N |  |  |
| 8 | DAT_GUIA_RECOL | DATE | Y |  |  |
| 9 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 10 | DAT_ENTREGA | DATE | Y |  |  |
| 11 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 12 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |
| 13 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 14 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 15 | MES_ANO_REF | DATE | Y |  |  |
| 16 | DAT_VENCTO | DATE | Y |  |  |
| 17 | DSC_COMPLEMENTAR | VARCHAR2(100) | Y |  |  |
| 18 | IND_TIPO_DOC_ARREC | CHAR(1) | Y |  |  |
| 19 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 20 | NUM_AUTENTIC | VARCHAR2(25) | Y |  |  |
| 21 | VAL_DOC_ORIG | NUMBER(17,2) | Y |  |  |
| 22 | VAL_DESCONTO | NUMBER(17,2) | Y |  |  |
| 23 | VAL_MULTA_MORA | NUMBER(17,2) | Y |  |  |
| 24 | VAL_JUROS | NUMBER(17,2) | Y |  |  |
| 25 | VAL_MULTA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## ICT_HISTORICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(8) | N |  |  |
| 5 | MODELO | CHAR(1) | N |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 7 | DAT_INI_PERIODO | DATE | Y |  |  |
| 8 | DAT_FIM_PERIODO | DATE | Y |  |  |
| 9 | DAT_INI_GERACAO | DATE | Y |  |  |
| 10 | DAT_FIM_GERACAO | DATE | Y |  |  |
| 11 | STATUS | NUMBER(2) | Y |  |  |
| 12 | IND_CONSOLIDA_P2 | CHAR(1) | Y |  | Parametro especifico dos livros 102 e 104, que indica se o livro foi consolidado (S/N) |

**PK**: COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, MODELO, NUM_PROCESSO

**FKs**:
- COD_EMPRESA, COD_PROG → ICT_PROG(COD_EMPRESA, COD_PROG)
- COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, MODELO → ICT_CONTROLE(COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, MODELO)

---

## ICT_HIST_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | VLR_PESO_QTD | NUMBER(17,6) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, DATA_FISCAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT → ICT_GRP_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT)

---

## ICT_ITDF_PAR2_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PARAM | NUMBER(3) | N |  |  |
| 2 | COD_ITEM_DF | VARCHAR2(2) | Y |  |  |

**PK**: COD_PARAM

**FKs**:
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## ICT_ITENS_DAICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ITEM_DAICMS | VARCHAR2(5) | N |  |  |
| 2 | IND_TP_ATIV | CHAR(1) | N |  |  |
| 3 | DSC_ITEM_DAICMS | VARCHAR2(50) | Y |  |  |

**PK**: COD_ITEM_DAICMS, IND_TP_ATIV

---

## ICT_IT_AP_CAL_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IND_INCENTIVO | CHAR(1) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | VLR_APURACAO | NUMBER(17,2) | Y |  |  |
| 9 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_OPER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_APUR_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

---

## ICT_IT_AP_DSCR_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IND_INCENTIVO | CHAR(1) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 9 | VLR_ITEM_DISCRIM | NUMBER(17,2) | Y |  |  |
| 10 | IND_TIPO_DEDUCAO | CHAR(1) | Y |  |  |
| 11 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Código de Ajuste (Sped Fiscal ¿ Reg E111/E220) ¿ referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |
| 16 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 17 | NUM_PROC | VARCHAR2(24) | Y |  |  |
| 18 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 19 | COD_AJUSTE | VARCHAR2(3) | Y |  |  |
| 20 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 21 | IND_CRED_ESTIMULO | CHAR(1) | Y | 'N' |  |
| 22 | COD_LINHA_PRD | VARCHAR2(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_APUR_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD → ICT_AM_LINHAP(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_LINHA_PRD)

---

## ICT_IT_AP_DSCR_IES_AJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IND_INCENTIVO | CHAR(1) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 9 | DATA_FISCAL | DATE | N |  |  |
| 10 | MOVTO_E_S | CHAR(1) | N |  |  |
| 11 | NORM_DEV | CHAR(1) | N |  |  |
| 12 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 13 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 14 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 15 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 16 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 17 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 18 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 19 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 20 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, INSC_ESTADUAL, COD_TIPO_LIVRO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO → ICT_IT_AP_DSCR_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO)

---

## ICT_IT_AP_DSCR_IES_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IND_INCENTIVO | CHAR(1) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 9 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 10 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 11 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 12 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 13 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 14 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, INSC_ESTADUAL, COD_TIPO_LIVRO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO → ICT_IT_AP_DSCR_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO)

---

## ICT_IT_AP_DSCR_IES_X113

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 16 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 17 | DAT_APURACAO | DATE | Y |  |  |
| 18 | IND_INCENTIVO | CHAR(1) | Y |  |  |
| 19 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 20 | NUM_DISCRIMINACAO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_AJUSTE_SPED, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO → ICT_IT_AP_DSCR_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO)

**Indexes**:
- IX_ICT_IT_AP_DSCR_IES_X113: (DAT_APURACAO, INSC_ESTADUAL, COD_TIPO_LIVRO, IND_INCENTIVO, COD_OPER_APUR, NUM_DISCRIMINACAO, COD_ESTAB, COD_EMPRESA)

---

## ICT_IT_AP_SUBS_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | IND_UF | CHAR(1) | N |  |  |
| 8 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 9 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 10 | VAL_ITEM_DISCRIM | NUMBER(17,2) | Y |  |  |
| 11 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 12 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 13 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 14 | IND_DIG_CALCULADO | CHAR(1) | Y | '1' |  |
| 15 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 16 | IND_TIPO_LANC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_APUR_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ICT_IT_AP_SUBS_IES_AJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | IND_UF | CHAR(1) | N |  |  |
| 8 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 9 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 10 | DATA_FISCAL | DATE | N |  |  |
| 11 | MOVTO_E_S | CHAR(1) | N |  |  |
| 12 | NORM_DEV | CHAR(1) | N |  |  |
| 13 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 14 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 15 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 16 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 17 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 18 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 19 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 20 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 21 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, INSC_ESTADUAL, COD_TIPO_LIVRO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO → ICT_IT_AP_SUBS_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO)

---

## ICT_IT_AP_SUBS_IES_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | IND_UF | CHAR(1) | N |  |  |
| 8 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 9 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 10 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 11 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 12 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 13 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 14 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 15 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, INSC_ESTADUAL, COD_TIPO_LIVRO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO → ICT_IT_AP_SUBS_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO)

---

## ICT_IT_AP_SUBS_IES_X113

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 16 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 17 | DAT_APURACAO | DATE | Y |  |  |
| 18 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 19 | IND_UF | CHAR(1) | Y |  |  |
| 20 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 21 | NUM_DISCRIMINACAO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_AJUSTE_SPED, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO → ICT_IT_AP_SUBS_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO)

**Indexes**:
- IX_ICT_IT_AP_SUBS_IES_X113: (DAT_APURACAO, INSC_ESTADUAL, COD_TIPO_LIVRO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO, COD_ESTAB, COD_EMPRESA)

---

## ICT_LVR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | TIPO_RESUMO | VARCHAR2(5) | Y |  |  |
| 8 | IND_MERC_SERV | CHAR(1) | Y |  |  |
| 9 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 10 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 11 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 12 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 13 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 16 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 17 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 18 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 19 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 20 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 21 | DATA_EMISSAO | DATE | Y |  |  |
| 22 | DATA_EMISSAO_FIM | DATE | Y |  |  |
| 23 | DATA_FISCAL | DATE | Y |  |  |
| 24 | DESC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 25 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 26 | DSC_TRIB_INT | VARCHAR2(100) | Y |  |  |
| 27 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 28 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 29 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 30 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 31 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 32 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |
| 33 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 34 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 35 | NORM_DEV | CHAR(1) | Y |  |  |
| 36 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 37 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 38 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 39 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 40 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 41 | SEQ_OBS | NUMBER(12) | Y |  |  |
| 42 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 43 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 44 | SITUACAO | CHAR(1) | Y |  |  |
| 45 | USUARIO | VARCHAR2(40) | Y |  |  |
| 46 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 47 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 48 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 49 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 50 | VLR_BASE1 | NUMBER(17,2) | Y |  |  |
| 51 | VLR_BASE2 | NUMBER(17,2) | Y |  |  |
| 52 | VLR_BASE3 | NUMBER(17,2) | Y |  |  |
| 53 | VLR_BASE4 | NUMBER(17,2) | Y |  |  |
| 54 | VLR_CONT_CONTR | NUMBER(17,2) | Y |  |  |
| 55 | VLR_CONT_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 56 | VLR_BASE_CONTR | NUMBER(17,2) | Y |  |  |
| 57 | VLR_BASE_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 58 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 59 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 60 | VLR_ISENTAS_ICMS | NUMBER(17,2) | Y |  |  |
| 61 | VLR_OUTRAS_ICMS | NUMBER(17,2) | Y |  |  |
| 62 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 63 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 64 | VLR_ISENTAS_IPI | NUMBER(17,2) | Y |  |  |
| 65 | VLR_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |
| 66 | VLR_ST | NUMBER(17,2) | Y |  |  |
| 67 | VLR_ST_D_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 68 | VLR_ST_DENTRO_UF | NUMBER(17,2) | Y |  |  |
| 69 | VLR_ST_F_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 70 | VLR_ST_FORA_UF | NUMBER(17,2) | Y |  |  |
| 71 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 72 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 73 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 74 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 75 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 76 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 77 | COD_TRIBUT_IPI | CHAR(1) | Y |  |  |
| 78 | VLR_ICMSS_PET_ENER | NUMBER(17,2) | Y |  |  |
| 79 | VLR_ICMSS_OUTROS_PRODS | NUMBER(17,2) | Y |  |  |
| 80 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 81 | RAZAO_SOCIAL_FIS_JUR | VARCHAR2(70) | Y |  |  |
| 82 | NUM_ITEM | NUMBER(5) | Y |  |  |

**Indexes**:
- ICT_LVR_5: (NUM_DOCFIS, IDENT_FIS_JUR, NUM_PROCESSO, DATA_FISCAL, COD_CFO, DAT_APURACAO, COD_ESTAB, SERIE_DOCFIS, USUARIO, COD_DOCTO, SUB_SERIE_DOCFIS, COD_EMPRESA, COD_TIPO_LIVRO, SITUACAO)
- IX_ICT_LVR: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, TIPO_RESUMO, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO, COD_TRIBUTO)
- IX_ICT_LVR_1: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, TIPO_RESUMO, SITUACAO)
- IX_ICT_LVR_2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL, NUM_PROCESSO)
- IX_ICT_LVR_3: (USUARIO, COD_EMPRESA, COD_ESTAB_CENTRAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, TIPO_RESUMO, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO, COD_TRIBUTO)
- IX_ICT_LVR_4: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, TIPO_RESUMO, SITUACAO)

---

## ICT_LVR_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SITUACAO | CHAR(1) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 17 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 18 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 19 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 20 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 21 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 22 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_REDUCAO_BASE | NUMBER(17,2) | Y |  |  |
| 24 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 25 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 26 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 27 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 28 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 30 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 31 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 32 | USUARIO | VARCHAR2(40) | Y |  |  |
| 33 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 34 | NORM_DEV | CHAR(1) | Y |  |  |
| 35 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 36 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 37 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 38 | VLR_TRIB_ICMSS_D | NUMBER(17,2) | Y |  |  |
| 39 | VLR_TRIB_ICMSS_R | NUMBER(17,2) | Y |  |  |
| 40 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 41 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 42 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_LVR_P1: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NRO_PROCESSO, IDENT_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO, TITULO_TRIBUTO, COD_TRIBUTACAO)

---

## ICT_LVR_P12

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | DATE | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 16 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 17 | VLR_NAO_TRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 18 | OBS_TRIBUTO | VARCHAR2(45) | Y |  |  |
| 19 | NRO_OBSERVACAO | NUMBER(5) | Y |  |  |
| 20 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 21 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 22 | IND_CONTEM_OBS | CHAR(1) | Y |  |  |
| 23 | VLR_BASE_ICMS_S | NUMBER(17,2) | Y |  |  |
| 24 | VLR_DESP_ACESS | NUMBER(17,2) | Y |  |  |

---

## ICT_LVR_P13

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI | DATE | Y |  |  |
| 4 | DATA_FIM | DATE | Y |  |  |
| 5 | DATA_FISCAL | DATE | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 13 | MODALIDADE_FRETE | CHAR(3) | Y |  |  |
| 14 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | COD_DOCTO_TRANSP | VARCHAR2(5) | Y |  |  |
| 17 | NUM_DOCFIS_TRANSP | VARCHAR2(12) | Y |  |  |
| 18 | SER_DOCFIS_TRANSP | VARCHAR2(3) | Y |  |  |
| 19 | S_SER_DOCFIS_TRANS | VARCHAR2(2) | Y |  |  |
| 20 | INSC_UF_REMET | VARCHAR2(14) | Y |  |  |
| 21 | RAZAO_REMET | VARCHAR2(70) | Y |  |  |
| 22 | CGC_CPF_REMET | VARCHAR2(14) | Y |  |  |
| 23 | INSC_ESTADUAL_DEST | VARCHAR2(14) | Y |  |  |
| 24 | RAZAO_DEST | VARCHAR2(70) | Y |  |  |
| 25 | CPF_CGC_DEST | VARCHAR2(14) | Y |  |  |
| 26 | DATA_EMISSAO_TRANS | DATE | Y |  |  |
| 27 | VLR_TOT_DOCFIS | NUMBER(17,2) | Y |  |  |
| 28 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 29 | CIDADE | VARCHAR2(30) | Y |  |  |
| 30 | CEP | VARCHAR2(8) | Y |  |  |
| 31 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 32 | OBS_FRETE | VARCHAR2(45) | Y |  |  |
| 33 | OBS_TRIB | VARCHAR2(45) | Y |  |  |
| 34 | NR_OBSERVACAO | NUMBER(12) | Y |  |  |
| 35 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 36 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 37 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 38 | DSC_ESTADO | VARCHAR2(50) | Y |  |  |

---

## ICT_LVR_P1A_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | SITUACAO | CHAR(1) | Y |  |  |
| 14 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 17 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 18 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 19 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 20 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 21 | COD_TRIBUTACAO | VARCHAR2(1) | Y |  |  |
| 22 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 24 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 25 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 28 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 29 | USUARIO | VARCHAR2(40) | Y |  |  |
| 30 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 31 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 32 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 33 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 34 | NORM_DEV | CHAR(1) | Y |  |  |
| 35 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 36 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 37 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 38 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 39 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_LVR_P1A_M2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO, COD_TRIBUTO, COD_TRIBUTACAO)

---

## ICT_LVR_P1A_M2_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | DATA_FISCAL | DATE | Y |  |  |
| 13 | DATA_EMISSAO | DATE | Y |  |  |
| 14 | SITUACAO | CHAR(1) | Y |  |  |
| 15 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 16 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 17 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 18 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 19 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 20 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 21 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 22 | COD_TRIBUTACAO | CHAR(1) | Y |  |  |
| 23 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 25 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 26 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 27 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 28 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 29 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 30 | USUARIO | VARCHAR2(40) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 32 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 33 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 34 | NORM_DEV | CHAR(1) | Y |  |  |
| 35 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 36 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 37 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_IC_LV_P1A_M2_UF: (USUARIO, COD_EMPRESA, COD_ESTAB_CENTRAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO, COD_TRIBUTO, COD_TRIBUTACAO)

---

## ICT_LVR_P1_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | SITUACAO | CHAR(1) | Y |  |  |
| 14 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 17 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 18 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 19 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 20 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 21 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 23 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | COD_TRIBUT_IPI | CHAR(1) | Y |  |  |
| 25 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 27 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 28 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 30 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 31 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 32 | USUARIO | VARCHAR2(40) | Y |  |  |
| 33 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 34 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 35 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 36 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 37 | NORM_DEV | CHAR(1) | Y |  |  |
| 38 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 39 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 40 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 41 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 42 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_LVR_P1_M2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO)

---

## ICT_LVR_P1_M2_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | DATA_FISCAL | DATE | Y |  |  |
| 13 | DATA_EMISSAO | DATE | Y |  |  |
| 14 | SITUACAO | CHAR(1) | Y |  |  |
| 15 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 16 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 17 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 18 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 19 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 20 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 21 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 22 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 24 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 25 | COD_TRIBUT_IPI | CHAR(1) | Y |  |  |
| 26 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 28 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 29 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 30 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 31 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 32 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 33 | USUARIO | VARCHAR2(40) | Y |  |  |
| 34 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 35 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 36 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 37 | NORM_DEV | CHAR(1) | Y |  |  |
| 38 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 39 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 40 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_LVR_P1_M2UF: (USUARIO, COD_EMPRESA, COD_ESTAB_CENTRAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO)

---

## ICT_LVR_P1_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 10 | ANO_FISCAL | NUMBER(4) | Y |  |  |
| 11 | MES_FISCAL | NUMBER(2) | Y |  |  |
| 12 | DECENDIO | NUMBER(1) | Y |  |  |
| 13 | DIA_FISCAL | NUMBER(2) | Y |  |  |
| 14 | SEQUENCIAL | NUMBER(6) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | DATA_EMISSAO | DATE | Y |  |  |
| 17 | CFOP | NUMBER(5) | Y |  |  |
| 18 | ATIVO_FIXO | CHAR(1) | Y |  |  |
| 19 | DATA_SAIDA_REC | DATE | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, MOVTO_E_S, IDENT_FIS_JUR, USUARIO

---

## ICT_LVR_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SITUACAO | CHAR(1) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 17 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 18 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 19 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 20 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 21 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 22 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_REDUCAO_BASE | NUMBER(17,2) | Y |  |  |
| 24 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 25 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 26 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 27 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 28 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 30 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 31 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 32 | USUARIO | VARCHAR2(40) | Y |  |  |
| 33 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 34 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 35 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 36 | NORM_DEV | CHAR(1) | Y |  |  |
| 37 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 38 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |
| 39 | LINHA | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_ICT_LVR_P2_1: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NRO_PROCESSO, IDENT_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO, TITULO_TRIBUTO, COD_TRIBUTACAO)
- IX_ICT_LVR_P2_2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NRO_PROCESSO, SITUACAO)

---

## ICT_LVR_P2_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 9 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 10 | SITUACAO | CHAR(1) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 15 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 16 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 17 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 18 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 19 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 20 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 22 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 23 | USUARIO | VARCHAR2(40) | Y |  |  |
| 24 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 25 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 26 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_LVR_P2_CONS: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NRO_PROCESSO, COD_DOCTO, NUM_DOCFIS_INI, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL)

---

## ICT_LVR_P2_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | SITUACAO | CHAR(1) | Y |  |  |
| 14 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 17 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 18 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 19 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 20 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 21 | VLR_BASE1 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 23 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_BASE2 | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE3 | NUMBER(17,2) | Y |  |  |
| 26 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 29 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 30 | USUARIO | VARCHAR2(40) | Y |  |  |
| 31 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 32 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 33 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 34 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 35 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 36 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 37 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 38 | NORM_DEV | CHAR(1) | Y |  |  |
| 39 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 40 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_ICT_LVR_P2_M2_1: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, SITUACAO)
- IX_ICT_LVR_P2_M2_2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL, NUM_PROCESSO)
- IX_ICT_LVR_P2_M2_3 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO, COD_TRIBUTO, VLR_ALIQUOTA, INSC_ESTADUAL, COD_TRIB_INT, COD_TRIB_REL, COMPL_CFOP, DATA_EMISSAO, COD_ESTADO)

---

## ICT_LVR_P2_M2_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 9 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 10 | SITUACAO | CHAR(1) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 15 | VLR_BASE1 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE2 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE3 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 19 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 20 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 23 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 26 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 27 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 28 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |

**Indexes**:
- IX_ICT_P2_M2_CONS: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, COD_DOCTO, NUM_DOCFIS_INI, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL)

---

## ICT_LVR_P2_M2_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 8 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | DATA_FISCAL | DATE | Y |  |  |
| 13 | DATA_EMISSAO | DATE | Y |  |  |
| 14 | SITUACAO | CHAR(1) | Y |  |  |
| 15 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 16 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 17 | NUM_AR | VARCHAR2(12) | Y |  |  |
| 18 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 19 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 20 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 21 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 22 | VLR_BASE1 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 24 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE2 | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE3 | NUMBER(17,2) | Y |  |  |
| 27 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 28 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 29 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 30 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 31 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 32 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 33 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 34 | USUARIO | VARCHAR2(40) | Y |  |  |
| 35 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 36 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 37 | DATA_EMISSAO_FIM | DATE | Y |  |  |

**Indexes**:
- IX_IC_LVR_P2_M2_UF: (USUARIO, COD_EMPRESA, COD_ESTAB_CENTRAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_PROCESSO, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, COD_CFO, COD_TRIBUTO)

---

## ICT_LVR_P3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 5 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 7 | IND_I_E_S | CHAR(1) | Y |  |  |
| 8 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 13 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 14 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 15 | COD_CFO | VARCHAR2(5) | Y |  |  |
| 16 | COD_ENT_SAI | CHAR(1) | Y |  |  |
| 17 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 18 | PRECO_ITEM | NUMBER(17,2) | Y |  |  |
| 19 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 20 | TOT_ESTOQUE | NUMBER(17,2) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | SEQ_OBS | NUMBER(12) | Y |  |  |
| 23 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 24 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 25 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 26 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 27 | CUSTO_MEDIO | NUMBER(17,2) | Y |  |  |
| 28 | IND_INSUMO | CHAR(1) | Y |  |  |
| 29 | IND_ORDENACAO | CHAR(1) | Y |  |  |
| 30 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 31 | NUM_DOCTO_INTERNO | VARCHAR2(15) | Y |  |  |
| 32 | SER_DOCTO_INTERNO | VARCHAR2(3) | Y |  |  |
| 33 | SSER_DOCTO_INTERN | VARCHAR2(2) | Y |  |  |
| 34 | GRUPO_ALMOX | VARCHAR2(9) | Y |  |  |
| 35 | DESCRICAO_ALMOX | VARCHAR2(50) | Y |  |  |
| 36 | COD_PRODUTO_DEST | VARCHAR2(60) | Y |  |  |
| 37 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 38 | ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 39 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 40 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 41 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |

**Indexes**:
- IX_ICT_LVR_P3: (COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, IND_I_E_S)
- IX_ICT_LVR_P3_2: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, IND_I_E_S)

---

## ICT_LVR_P3_INS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 5 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 7 | IND_I_E_S | CHAR(1) | Y |  |  |
| 8 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 13 | GRUPO_PRODUTO_INS | VARCHAR2(9) | Y |  |  |
| 14 | IND_PRODUTO_INS | CHAR(1) | Y |  |  |
| 15 | COD_PRODUTO_INS | VARCHAR2(60) | Y |  |  |
| 16 | DESCRICAO_INS | VARCHAR2(50) | Y |  |  |
| 17 | COD_UND_PAD_INS | VARCHAR2(8) | Y |  |  |
| 18 | QTD_MOVTO_INS | NUMBER(17,6) | Y |  |  |
| 19 | CUSTO_UNIT_INS | NUMBER(18,6) | Y |  |  |
| 20 | COD_LEGENDA_INS | VARCHAR2(5) | Y |  |  |
| 21 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 22 | NUM_DOCTO_INS | VARCHAR2(15) | Y |  |  |

---

## ICT_LVR_P3_LEG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | COD_NBM | VARCHAR2(10) | N |  |  |
| 8 | IND_I_E_S | CHAR(1) | N |  |  |
| 9 | COD_LEGENDA | VARCHAR2(5) | N |  |  |
| 10 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 11 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 12 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 13 | PRECO_ITEM | NUMBER(17,2) | Y |  |  |
| 14 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 15 | TOT_ESTOQUE | NUMBER(17,2) | Y |  |  |
| 16 | IND_ORDENACAO | CHAR(1) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_NBM, IND_I_E_S, COD_LEGENDA

---

## ICT_LVR_P7

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 6 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 7 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 10 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 13 | VLR_UNIT | NUMBER(18,6) | Y |  |  |
| 14 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 19 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 20 | DESCRICAO_RIPI | VARCHAR2(25) | Y |  |  |
| 21 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 22 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 23 | IND_SIT_TRIB | CHAR(1) | Y |  |  |

**Indexes**:
- IX_ICT_LVR_P7: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_ALMOX, GRUPO_CONTAGEM, IND_PRODUTO)
- IX_ICT_LVR_P7_1: (NUM_PROCESSO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, GRUPO_CONTAGEM, IND_PRODUTO, COD_PRODUTO, COD_NBM, COD_MEDIDA, VLR_UNIT)

---

## ICT_LVR_RE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_ENTRADA_RE | DATE | N |  |  |
| 4 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 5 | DSC_TIPO_DOCTO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | DATA_EMISSAO | DATE | N |  |  |
| 10 | COD_FIS_JUR_EMIT | VARCHAR2(14) | N |  |  |
| 11 | CPF_CGC_EMIT | VARCHAR2(14) | Y |  |  |
| 12 | INSC_EST_EMIT | VARCHAR2(14) | Y |  |  |
| 13 | RAZAO_SOCIAL_EMIT | VARCHAR2(70) | Y |  |  |
| 14 | COD_ESTADO_EMIT | VARCHAR2(2) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | DATA_SAIDA_MINUTA | DATE | Y |  |  |
| 17 | COD_FIS_JUR_TRAN | VARCHAR2(14) | Y |  |  |
| 18 | RAZAO_SOCIAL_TRAN | VARCHAR2(70) | Y |  |  |
| 19 | PLACA_VEICULO | VARCHAR2(10) | Y |  |  |
| 20 | NUM_MINUTA | VARCHAR2(12) | Y |  |  |
| 21 | DSC_OBS | VARCHAR2(255) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ENTRADA_RE, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_EMISSAO, COD_FIS_JUR_EMIT

---

## ICT_LVR_REIMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_REIMP | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DATA_PER_INI | DATE | Y |  |  |
| 6 | DATA_PER_FIM | DATE | Y |  |  |
| 7 | LST_REL | LONG | Y |  |  |
| 8 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 9 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 10 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 11 | IND_INCENTIVO | CHAR(1) | Y |  |  |

**PK**: IDENT_REIMP

**Indexes**:
- IX_ICT_LVR_REIMP (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DATA_PER_INI, DATA_PER_FIM, SERIE_LIVRO, SUB_SERIE_LIVRO, INSC_ESTADUAL)

---

## ICT_LVR_REIMP_REL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_REIMP | NUMBER(12) | N |  |  |
| 2 | SEQ_REL | NUMBER(3) | N |  |  |
| 3 | RELATORIO | BLOB | Y |  |  |
| 4 | DATAWINDOW | VARCHAR2(100) | Y |  |  |
| 5 | QUEBRA | CHAR(1) | Y |  |  |

**PK**: IDENT_REIMP, SEQ_REL

---

## ICT_LVR_REIMP_REL_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_REIMP | NUMBER(12) | N |  |  |
| 2 | SEQ_REL | NUMBER(3) | N |  |  |
| 3 | SEQ_REL_AUX | NUMBER(5) | N |  |  |
| 4 | RELATORIO | BLOB | Y |  |  |

**PK**: IDENT_REIMP, SEQ_REL, SEQ_REL_AUX

---

## ICT_MM_CONV115

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO | NUMBER(4) | N |  |  |
| 4 | TIPO_ARQUIVO | CHAR(1) | N |  |  |
| 5 | NOME_ARQUIVO | VARCHAR2(29) | N |  |  |
| 6 | VOLUME_ARQUIVO | NUMBER(3) | N |  |  |
| 7 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 10 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |
| 11 | NUM_DOCFIS_INI | NUMBER(9) | Y |  |  |
| 12 | DATA_EMISSAO_INI | DATE | Y |  |  |
| 13 | NUM_DOCFIS_FIM | NUMBER(9) | Y |  |  |
| 14 | DATA_EMISSAO_FIM | DATE | Y |  |  |
| 15 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_TRIB | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ISENTAS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_SUBST_TRIB | NUMBER(17,2) | Y | 0 |  |
| 21 | VLR_BASE_SUB_TRIB | NUMBER(17,2) | Y | 0 |  |
| 22 | DATA_VENCTO_INI | DATE | Y |  |  |
| 23 | DATA_VENCTO_FIM | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO

---

## ICT_MM_CONV115_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO | NUMBER(4) | N |  |  |
| 4 | TIPO_ARQUIVO | CHAR(1) | N |  |  |
| 5 | NOME_ARQUIVO | VARCHAR2(29) | N |  |  |
| 6 | VOLUME_ARQUIVO | NUMBER(3) | N |  |  |
| 7 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 8 | NOME_ARQUIVO_UF | VARCHAR2(29) | N |  |  |
| 9 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 12 | NUM_DOCFIS_INI | NUMBER(9) | Y |  |  |
| 13 | DATA_EMISSAO_INI | DATE | Y |  |  |
| 14 | NUM_DOCFIS_FIM | NUMBER(9) | Y |  |  |
| 15 | DATA_EMISSAO_FIM | DATE | Y |  |  |
| 16 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO, COD_ESTADO, NOME_ARQUIVO_UF

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO → ICT_MM_CONV115(COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO)

---

## ICT_MM_CONV115_UF_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO | NUMBER(4) | N |  |  |
| 4 | TIPO_ARQUIVO | CHAR(1) | N |  |  |
| 5 | NOME_ARQUIVO | VARCHAR2(29) | N |  |  |
| 6 | VOLUME_ARQUIVO | NUMBER(3) | N |  |  |
| 7 | COD_SITUACAO_A | CHAR(1) | N |  |  |
| 8 | COD_SITUACAO_B | VARCHAR2(2) | N |  |  |
| 9 | COD_CFO | VARCHAR2(4) | N |  |  |
| 10 | VLR_ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 11 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 12 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_SUB_TRIB | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SUBST_TRIB | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BC_ICMS_UF | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_UF | NUMBER(17,2) | Y |  |  |
| 20 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 21 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO, COD_SITUACAO_A, COD_SITUACAO_B, COD_CFO, VLR_ALIQ_ICMS, COD_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO → ICT_MM_CONV115(COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO)

---

## ICT_MM_CONV115_UF_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO | NUMBER(4) | N |  |  |
| 4 | TIPO_ARQUIVO | CHAR(1) | N |  |  |
| 5 | NOME_ARQUIVO | VARCHAR2(29) | N |  |  |
| 6 | VOLUME_ARQUIVO | NUMBER(3) | N |  |  |
| 7 | SEQ_REG | NUMBER(12) | N |  |  |
| 8 | IND_AGRUP | VARCHAR2(3) | Y |  |  |
| 9 | CODIGO | VARCHAR2(1000) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | VLR_ST | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 14 | COD_MODELO | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO, SEQ_REG

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO → ICT_MM_CONV115(COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO, COD_MODELO)

---

## ICT_MM_PORT44

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO | NUMBER(4) | N |  |  |
| 4 | TIPO_ARQUIVO | CHAR(1) | N |  |  |
| 5 | NOME_ARQUIVO | VARCHAR2(11) | N |  |  |
| 6 | VOLUME_ARQUIVO | NUMBER(3) | N |  |  |
| 7 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 10 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |
| 11 | NUM_DOCFIS_INI | NUMBER(9) | Y |  |  |
| 12 | DATA_EMISSAO_INI | DATE | Y |  |  |
| 13 | NUM_DOCFIS_FIM | NUMBER(9) | Y |  |  |
| 14 | DATA_EMISSAO_FIM | DATE | Y |  |  |
| 15 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_TRIB | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ISENTAS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_SUBST_TRIB | NUMBER(17,2) | Y | 0 |  |
| 21 | VLR_BASE_SUB_TRIB | NUMBER(17,2) | Y | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO, TIPO_ARQUIVO, NOME_ARQUIVO, VOLUME_ARQUIVO

---

## ICT_MM_REG88_RJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | DATA_REFER | DATE | N |  |  |
| 5 | VLR_ICMS_NORMAL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_IMP | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS_TOTAL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_UFIR_MES | NUMBER(17,4) | Y |  |  |
| 9 | VLR_TOTAL_UFIR | NUMBER(17,2) | Y |  |  |
| 10 | VLR_UFIR_DIA5 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_UFIR_DIA10 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_UFIR_DIA20 | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, DATA_REFER

---

## ICT_NF_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 5 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 6 | DAT_FISCAL | DATE | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | COD_CFO_ENTR | VARCHAR2(4) | Y |  |  |
| 10 | COD_CFO_SAIDA | VARCHAR2(4) | Y |  |  |
| 11 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DAT_FISCAL, IDENT_DOCTO, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_OBRIGACAO_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | IND_PERIODICIDADE | VARCHAR2(2) | Y |  |  |
| 7 | MAX_PRAZO_EMISSAO | NUMBER(3) | Y |  |  |
| 8 | MAX_PRAZ_APRES | NUMBER(3) | Y |  |  |
| 9 | IND_TER_ABE_FEC | CHAR(1) | Y |  |  |
| 10 | IND_ENFEIXAMENTO | CHAR(1) | Y |  |  |
| 11 | MAX_OSC_PERMITE | NUMBER(3) | Y |  |  |
| 12 | NUM_PROTOCOLO | VARCHAR2(40) | Y |  |  |
| 13 | DAT_LIB_PROT | DATE | Y |  |  |
| 14 | N_MESES | NUMBER(3) | Y |  |  |
| 15 | INICIAR | CHAR(1) | Y |  |  |
| 16 | MAX_CONT | NUMBER(7) | Y |  |  |
| 17 | LIVRO_I | NUMBER(6) | Y |  |  |
| 18 | PAGINA_I | NUMBER(6) | Y |  |  |
| 19 | DESLOC_I | NUMBER(6) | Y |  |  |
| 20 | IND_LIVRO_UNICO | CHAR(1) | Y |  |  |
| 21 | VLR_LIM_PAGINA | NUMBER(4) | Y |  |  |
| 22 | COMPLEMENTO_TERMO | VARCHAR2(240) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## ICT_OBRIG_INSC_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | IND_PERIODICIDADE | VARCHAR2(2) | Y |  |  |
| 6 | MAX_PRAZO_EMISSAO | NUMBER(3) | Y |  |  |
| 7 | MAX_PRAZ_APRES | NUMBER(3) | Y |  |  |
| 8 | IND_TER_ABE_FEC | CHAR(1) | Y |  |  |
| 9 | IND_ENFEIXAMENTO | CHAR(1) | Y |  |  |
| 10 | MAX_OSC_PERMITE | NUMBER(3) | Y |  |  |
| 11 | NUM_PROTOCOLO | VARCHAR2(40) | Y |  |  |
| 12 | DAT_LIB_PROT | DATE | Y |  |  |
| 13 | N_MESES | NUMBER(2) | Y |  |  |
| 14 | INICIAR | CHAR(1) | Y |  |  |
| 15 | MAX_CONT | NUMBER(7) | Y |  |  |
| 16 | LIVRO_I | NUMBER(6) | Y |  |  |
| 17 | PAGINA_I | NUMBER(6) | Y |  |  |
| 18 | DESLOC_I | NUMBER(6) | Y |  |  |
| 19 | IND_LIVRO_UNICO | CHAR(1) | Y |  |  |
| 20 | VLR_LIM_PAGINA | NUMBER(6) | Y |  |  |
| 21 | COMPLEMENTO_TERMO | VARCHAR2(240) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## ICT_OBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | NUM_REGISTRO | NUMBER(12) | Y |  |  |
| 13 | NUM_OBSERVACAO | NUMBER(12) | Y |  |  |
| 14 | DSC_OBSERVACAO1 | VARCHAR2(500) | Y |  |  |
| 15 | DSC_OBSERVACAO2 | VARCHAR2(500) | Y |  |  |
| 16 | DSC_OBSERVACAO3 | VARCHAR2(500) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_OBS: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)
- IX_ICT_OBS_2: (COD_EMPRESA, COD_ESTAB, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)

---

## ICT_OBS_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | DATA_FISCAL | DATE | Y |  |  |
| 11 | NRO_REGISTRO | NUMBER(12) | Y |  |  |
| 12 | NRO_OBSERVACAO | NUMBER(6) | Y |  |  |
| 13 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 14 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 15 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 16 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 18 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 21 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |

**Indexes**:
- IX_ICT_OBS_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL, USUARIO)
- IX_ICT_OBS_P1_2: (COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)

---

## ICT_OBS_P1_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | DATA_FISCAL | DATE | Y |  |  |
| 11 | NUM_REGISTRO | NUMBER(12) | Y |  |  |
| 12 | NUM_OBSERVACAO | NUMBER(6) | Y |  |  |
| 13 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 14 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 15 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_OBS_P1_M2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)
- IX_ICT_OBS_P1_M2_2: (COD_EMPRESA, COD_ESTAB, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)

---

## ICT_OBS_P1_M2_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | NUM_REGISTRO | NUMBER(12) | Y |  |  |
| 13 | NUM_OBSERVACAO | NUMBER(6) | Y |  |  |
| 14 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 15 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 16 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

---

## ICT_OBS_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | DATA_FISCAL | DATE | Y |  |  |
| 11 | NRO_REGISTRO | NUMBER(12) | Y |  |  |
| 12 | NRO_OBSERVACAO | NUMBER(6) | Y |  |  |
| 13 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 14 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 15 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 16 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 18 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 21 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |

**Indexes**:
- IX_ICT_OBS_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL, USUARIO)
- IX_ICT_OBS_P2_2: (COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)

---

## ICT_OBS_P2_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | NRO_OBSERVACAO | NUMBER(6) | Y |  |  |
| 6 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 7 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 8 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 9 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 11 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_ICT_OBS_P2_CONS: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO)

---

## ICT_OBS_P2_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | DATA_FISCAL | DATE | Y |  |  |
| 11 | NUM_REGISTRO | NUMBER(12) | Y |  |  |
| 12 | NUM_OBSERVACAO | NUMBER(6) | Y |  |  |
| 13 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 14 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 15 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_OBS_P2_M2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)
- IX_ICT_OBS_P2_M2_2: (COD_EMPRESA, COD_ESTAB, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)

---

## ICT_OBS_P2_M2_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | NUM_OBSERVACAO | NUMBER(6) | Y |  |  |
| 6 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 7 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 8 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 11 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_OBS_P2_M2_CONS: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO)

---

## ICT_OBS_P2_M2_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | NUM_REGISTRO | NUMBER(12) | Y |  |  |
| 13 | NUM_OBSERVACAO | NUMBER(6) | Y |  |  |
| 14 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 15 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 16 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

---

## ICT_OBS_P3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 5 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 7 | SEQ_OBS | NUMBER(12) | Y |  |  |
| 8 | DSC_OBS | VARCHAR2(45) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_OBS_P3: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, SEQ_OBS)
- IX_ICT_OBS_P3_02: (COD_EMPRESA, COD_ESTAB, SEQ_OBS)

---

## ICT_OBS_P7

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 6 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 7 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 10 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 11 | DSC_OBS | VARCHAR2(45) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_OBS_P7: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_ALMOX, GRUPO_CONTAGEM, IND_PRODUTO)

---

## ICT_P1_SJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | DAT_FISCAL | DATE | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | COD_PESSOA_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 11 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 12 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 13 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 14 | COD_TRIBUTACAO | CHAR(1) | Y |  |  |
| 15 | VLR_ALIQ | NUMBER(7,4) | Y |  |  |
| 16 | TP_LINHA | CHAR(1) | Y |  |  |
| 17 | DAT_EMISSAO | DATE | Y |  |  |
| 18 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 19 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 21 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 22 | OBS | VARCHAR2(70) | Y |  |  |
| 23 | LIMINAR | VARCHAR2(37) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | USUARIO | VARCHAR2(40) | Y |  |  |
| 26 | VLR_TRIBUTO_SJ | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX2_ICT_P1_SJ: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, USUARIO)
- IX3_ICT_P1_SJ: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_TRIBUTO, LIMINAR, COD_TRIBUTACAO)
- IX_ICT_P1_SJ: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, DAT_FISCAL, COD_DOCTO, SERIE, NUM_DOCFIS, COD_PESSOA_FIS_JUR, COD_CFO, COD_TRIBUTO, COD_TRIBUTACAO, VLR_ALIQ, TP_LINHA)

---

## ICT_P1_SJ_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | DATA_FISCAL | DATE | Y |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 13 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 14 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 15 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 16 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 17 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 19 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | COD_TRIBUT_IPI | VARCHAR2(4) | Y |  |  |
| 21 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 23 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TRIBUTO_SJ | NUMBER(17,2) | Y |  |  |
| 25 | OBSERVACAO | VARCHAR2(70) | Y |  |  |
| 26 | LIMINAR | VARCHAR2(37) | Y |  |  |
| 27 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_ICT_P1_SJ_M2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL, COD_CFO)

---

## ICT_P2_SJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | DAT_FISCAL | DATE | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE | VARCHAR2(2) | Y |  |  |
| 9 | TP_LINHA | CHAR(1) | Y |  |  |
| 10 | SEQ_TP_LINHA | NUMBER(3) | Y |  |  |
| 11 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 14 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 15 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 16 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 17 | S_REMESSA_1 | VARCHAR2(20) | Y |  |  |
| 18 | S_REMESSA_2 | VARCHAR2(20) | Y |  |  |
| 19 | S_REMESSA_3 | VARCHAR2(20) | Y |  |  |
| 20 | S_REMESSA_4 | VARCHAR2(20) | Y |  |  |
| 21 | S_REMESSA_5 | VARCHAR2(20) | Y |  |  |
| 22 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ALIQ | NUMBER(7,4) | Y |  |  |
| 25 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 28 | OBS_1 | VARCHAR2(45) | Y |  |  |
| 29 | OBS_2 | VARCHAR2(15) | Y |  |  |
| 30 | LIMINAR | VARCHAR2(37) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 32 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX2_ICT_P2_SJ: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, USUARIO)
- IX3_ICT_P2_SJ: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_TRIBUTO, LIMINAR)
- IX_ICT_P2_SJ: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, DAT_FISCAL, COD_DOCTO, SERIE, SUB_SERIE, TP_LINHA, SEQ_TP_LINHA, COD_ESTADO, COD_CFO, COD_TRIBUTO)

---

## ICT_PAR_APURAC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DSC_PARAM | VARCHAR2(50) | N |  |  |
| 4 | COD_TP_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 6 | NUM_SEQUENCIAL | VARCHAR2(3) | Y |  |  |
| 7 | DSC_TIT_AUX | VARCHAR2(50) | Y |  |  |
| 8 | COD_OPER_APUR_OUTR | VARCHAR2(5) | Y |  |  |
| 9 | NUM_SEQUENCIAL_OUT | VARCHAR2(3) | Y |  |  |
| 10 | DSC_TIT_AUX_OUTR | VARCHAR2(50) | Y |  |  |
| 11 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 12 | COD_CLASSE_OUTR | VARCHAR2(3) | Y |  |  |
| 13 | COD_AMP_LEGAL | VARCHAR2(10) | Y |  |  |
| 14 | COD_SUB_OCORR | VARCHAR2(2) | Y |  |  |
| 15 | COD_AMP_LEGAL_OUT | VARCHAR2(10) | Y |  |  |
| 16 | COD_SUB_OCORR_OUT | VARCHAR2(2) | Y |  |  |
| 17 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 18 | IND_TP_PAR | CHAR(1) | Y |  |  |
| 19 | IND_LANC_TRANSF | CHAR(1) | Y | 'N' | Indica o lançamento das notas de transferência nota a nota no Resumo da Apuração - P9. |
| 20 | COD_AJUSTE_IPI_DEB | VARCHAR2(3) | Y |  | Lançamento a Débito - Código de ajuste da apuração do IPI de acordo com a Tabela de Códigos de Ajuste da Apuração do IPI (publicada pela RFB). Este campo é obrigatório para a geração do registro  "E530-Ajustes da Apuração do IPI"  do Sped Fiscal. |
| 21 | COD_AJUSTE_IPI_CRED | VARCHAR2(3) | Y |  | Lançamento a Débito - Código de ajuste da apuração do IPI de acordo com a Tabela de Códigos de Ajuste da Apuração do IPI (publicada pela RFB). Este campo é obrigatório para a geração do registro  "E530-Ajustes da Apuração do IPI"  do Sped Fiscal. |
| 22 | COD_AJUSTE_ICMS_DEB | VARCHAR2(8) | Y |  | Código de Ajuste da Operação a Débito. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 23 | COD_AJUSTE_ICMS_CRED | VARCHAR2(8) | Y |  | Código de Ajuste da Operação a Créditto. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 24 | COD_AJUSTE_SPED_DEB | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 25 | COD_AJUSTE_SPED_CRED | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 26 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 27 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 28 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 29 | IND_CONSID_NF_CONJ_IPI | CHAR(1) | Y | 'N' | Indicador para considerar Itens de Serviço de Notas Conjugadas na apuração do IPI |
| 30 | IND_FORMA_LANC_VLRS | CHAR(1) | Y | '1' |  |
| 31 | COD_AJ_SPED_DEB_DIFAL | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) - referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 32 | COD_OBS_DEB_DIFAL | VARCHAR2(8) | Y |  |  |
| 33 | IND_TP_DEB_ESP | VARCHAR2(1) | Y | '1' |  |
| 34 | COD_AJUSTE_ICMS_DEB_E113 | VARCHAR2(8) | Y |  |  |
| 35 | DSC_OBS_DEB_DIFAL_E113 | VARCHAR2(250) | Y |  |  |
| 36 | IND_ASSOCIA_X113 | VARCHAR2(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, DSC_PARAM, COD_TP_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TP_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_TP_LIVRO, COD_OPER_APUR_OUTR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS_DEB → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_CRED → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_SPED_DEB → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_SPED_CRED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJ_SPED_DEB_DIFAL → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## ICT_PAR_APURAC_ST
**Comment**: Tabela de parametrização de lançamentos na apuração do ICMS. Criada para atendimento ao ICMS-ST, porém com opção de criação de novos códigos de parametrização, o objetivo será a futura substituição da tabela ICT_PAR_APURAC por esta.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | VARCHAR2(4) | N |  | Código criado pelo usuário para identificação do lançamento. |
| 4 | COD_TP_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DSC_PARAM | VARCHAR2(50) | Y |  |  |
| 6 | IND_PARAM | VARCHAR2(2) | Y |  | Indicador do tipo delançamento, através dele será possível identificar qual o objetivo do lançamento em questão. |
| 7 | COD_OPER_APUR_DEB | VARCHAR2(5) | Y |  |  |
| 8 | DSC_TIT_DEB | VARCHAR2(150) | Y |  |  |
| 9 | COD_OPER_APUR_CRED | VARCHAR2(5) | Y |  |  |
| 10 | DSC_TIT_CRED | VARCHAR2(150) | Y |  |  |
| 11 | COD_CLASSE_DEB | VARCHAR2(3) | Y |  |  |
| 12 | COD_AMP_LEGAL_DEB | VARCHAR2(10) | Y |  |  |
| 13 | COD_SUB_OCORR_DEB | VARCHAR2(2) | Y |  |  |
| 14 | COD_CLASSE_CRED | VARCHAR2(3) | Y |  |  |
| 15 | COD_AMP_LEGAL_CRED | VARCHAR2(10) | Y |  |  |
| 16 | COD_SUB_OCORR_CRED | VARCHAR2(2) | Y |  |  |
| 17 | COD_AJUSTE_ICMS_DEB | VARCHAR2(8) | Y |  | Código de Ajuste da Operação a Débito. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 18 | COD_AJUSTE_ICMS_CRED | VARCHAR2(8) | Y |  | Código de Ajuste da Operação a Créditto. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 19 | COD_AJUSTE_SPED_DEB | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 20 | COD_AJUSTE_SPED_CRED | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 21 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 22 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 23 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM

**FKs**:
- COD_TP_LIVRO, COD_OPER_APUR_DEB → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_TP_LIVRO, COD_OPER_APUR_CRED → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS_DEB → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_CRED → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_SPED_DEB → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_SPED_CRED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## ICT_PAR_AP_UF_D_C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | SEQ_ITEM | NUMBER(2) | N |  |  |
| 3 | IND_DEB_CRED | CHAR(1) | N |  |  |
| 4 | DSC_ITEM | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_ESTADO, SEQ_ITEM, IND_DEB_CRED

---

## ICT_PAR_CRED_PRES_TRANSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI | DATE | N |  |  |
| 4 | DAT_FIM | DATE | Y |  |  |
| 5 | VLR_PERCENTUAL | NUMBER(5,2) | Y |  |  |
| 6 | IND_VLR_00_TRIB | CHAR(1) | Y |  | 00 TRIBUTADA INTEGRAMENTE  -  %  sobre o Valor do ICMS. |
| 7 | IND_VLR_10_TRIB | CHAR(1) | Y |  | 10 TRIB. E C/ COBR. DO ICMS SUBST. TRIB. -  %  sobre o Vlr Imp. STFR. |
| 8 | IND_VLR_20_RED | CHAR(1) | Y |  | 20 RED. DA BASE DE CALCULO - %  sobre o Valor do ICMS. |
| 9 | IND_VLR_50_SUSP | CHAR(1) | Y |  | 50 SUSPENÇÃO - %  sobre o Valor do ICMS Não Escriturado. |
| 10 | IND_VLR_51_DIF | CHAR(1) | Y |  | 51 DIFERIMENTO - %  sobre o Valor do ICMS Não Escriturado. |
| 11 | IND_VLR_60_ANT | CHAR(1) | Y |  | 60 ICMS COBRADO ANTERIORMENTE POR ST - % sobre o Valor da Base Outras de ICMS-ST. |
| 12 | IND_VLR_70_RED | CHAR(1) | Y |  | 70 RED. BASE DE CALC E COBR. ICMS SUBST. TRIB. - % sobre o Vlr Imp. STFR. |
| 13 | IND_VLR_90_OUTRAS | CHAR(1) | Y |  | 90 OUTRAS - %  sobre o Valor do ICMS Não Escriturado. |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI

---

## ICT_PAR_ICMS_AM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DSC_PARAM | VARCHAR2(50) | N |  |  |
| 5 | IND_TP_PAR | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DSC_PARAM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## ICT_PAR_ICMS_E_OI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | VARCHAR2(2) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | IND_ORDEM_LIVRO | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_TIPO_LIVRO

---

## ICT_PAR_ICMS_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | DSC_PARAM | VARCHAR2(50) | N |  |  |
| 3 | IND_TP_PAR | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO, DSC_PARAM

---

## ICT_PAR_IMP_OBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_ENTRADA | CHAR(1) | Y |  |  |
| 4 | IND_TP_SAIDA | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_PAR_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 4 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | Y |  | Coluna relativa ao Lançamento do Crédito do CIAP |
| 6 | DSC_OPER_APUR | VARCHAR2(150) | Y |  | Coluna relativa ao Lançamento do Crédito do CIAP |
| 7 | COD_CLASSE | VARCHAR2(3) | Y |  | Coluna relativa ao Lançamento do Crédito do CIAP |
| 8 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  | Coluna relativa ao Lançamento do Crédito do CIAP |
| 9 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  | Coluna relativa ao Lançamento do Crédito do CIAP |
| 10 | PERC_FRETE_INCENT | NUMBER(7,4) | Y |  |  |
| 11 | COD_OPER_FRETE | VARCHAR2(5) | Y |  | Coluna relativa ao Lançamento do Incentivo de Frete |
| 12 | DSC_OPER_FRETE | VARCHAR2(150) | Y |  | Coluna relativa ao Lançamento do Incentivo de Frete |
| 13 | COD_CLASSE_FRETE | VARCHAR2(3) | Y |  | Coluna relativa ao Lançamento do Incentivo de Frete |
| 14 | COD_AMP_FRETE | VARCHAR2(10) | Y |  | Coluna relativa ao Lançamento do Incentivo de Frete |
| 15 | COD_SUB_AMP_FRETE | VARCHAR2(2) | Y |  | Coluna relativa ao Lançamento do Incentivo de Frete |
| 16 | IND_UTILIZA_LANC | CHAR(1) | Y | 'N' | Indicador de utilização dos lanctos a credito para compor a base de calculo do CP |
| 17 | PERCENTUAL_MINIMO | NUMBER(7,4) | Y |  | Percentual minimo de diferenca entre ICMS antes X ICMS apos incentivos. E usado na validacao e ajuste dos incentivos |
| 18 | VLR_ICMS_MINIMO | NUMBER(17,2) | Y |  | Valor minimo de recolhimento apos deducao dos incentivos. E usado na validacao e ajuste dos incentivos |
| 19 | IND_UTILIZA_SD_ANT | CHAR(1) | Y | 'N' | Indicador de utilização do sd credor do per ant para compor a base de calculo do CP |
| 20 | IND_UTILIZA_LANC_DB | CHAR(1) | Y | 'N' | Indicador de utilização dos lanctos a debito para compor a base de calculo do CP |
| 21 | IND_TP_UTIL_LANC_CR | CHAR(1) | Y |  | Indica se o valor dos lancamentos de credito (sd ant e outros) serao ou nao rateados na proporcao das saidas incent/nao incent do grupo |
| 22 | COD_OPER_RATEIO_S | VARCHAR2(5) | Y |  | Código de Apuração relativo ao Lançamento do Rateio do Crédito das Entradas - Livro não incentivado |
| 23 | COD_CLASSE_RATEIO_S | VARCHAR2(3) | Y |  | Código de Classe relativo ao Lançamento do Rateio do Crédito das Entradas - Livro não incentivado |
| 24 | COD_AMP_RATEIO_S | VARCHAR2(10) | Y |  | Código de Amparo legal relativo ao Lançamento do Rateio do Crédito das Entradas - Livro não incentivado |
| 25 | COD_SUB_AMP_RATEIO_S | VARCHAR2(2) | Y |  | Subitem do Amparo legal relativo ao Lançamento do Rateio do Crédito das Entradas - Livro não incentivado |
| 26 | COD_OPER_RATEIO_E | VARCHAR2(5) | Y |  | Código de Apuração relativo ao Lançamento do Rateio do Crédito das Entradas - Livro Incentivado |
| 27 | COD_CLASSE_RATEIO_E | VARCHAR2(3) | Y |  | Código de Classe relativo ao Lançamento do Rateio do Crédito das Entradas - Livro Incentivado |
| 28 | COD_AMP_RATEIO_E | VARCHAR2(10) | Y |  | Código de Amparo legal relativo ao Lançamento do Rateio do Crédito das Entradas - Livro Incentivado |
| 29 | COD_SUB_AMP_RATEIO_E | VARCHAR2(2) | Y |  | Subitem do Amparo legal relativo ao Lançamento do Rateio do Crédito das Entradas - Livro Incentivado |
| 30 | IND_DEV_RATEIO | CHAR(1) | Y |  |  |
| 31 | COD_AJUSTE_SEF | NUMBER(3) | Y |  | Código de Ajuste SEF relativo ao Lançamento do Crédito do CIAP |
| 32 | COD_AJUSTE_SEF_FRETE | NUMBER(3) | Y |  | Código de Ajuste SEF relativo ao Lançamento do Incentivo de Frete |
| 33 | COD_AJ_SEF_RATEIO_E | NUMBER(3) | Y |  | Código de Ajuste SEF relativo ao Lançamento do Rateio do Crédito das Entradas - Livro incentivado |
| 34 | COD_AJ_SEF_RATEIO_S | NUMBER(3) | Y |  | Código de Ajuste SEF relativo ao Lançamento do Rateio do Crédito das Entradas - Livro não incentivado |
| 35 | IND_BASE_CALC_INC | CHAR(1) | Y |  |  |
| 36 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 37 | COD_AJUSTE_ICMS_FRETE | VARCHAR2(8) | Y |  |  |
| 38 | COD_AJ_ICMS_RATEIO_E | VARCHAR2(8) | Y |  |  |
| 39 | COD_AJ_ICMS_RATEIO_S | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_PAR_MEIO_MAG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 2 | DSC_PERFIL | VARCHAR2(50) | Y |  |  |
| 3 | IND_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 4 | IND_TP_GERACAO | CHAR(1) | Y |  |  |
| 5 | IND_REG_10 | CHAR(1) | Y |  |  |
| 6 | IND_REG_11 | CHAR(1) | Y |  |  |
| 7 | IND_REG_50 | CHAR(1) | Y |  |  |
| 8 | IND_REG_51 | CHAR(1) | Y |  |  |
| 9 | IND_REG_53 | CHAR(1) | Y |  |  |
| 10 | IND_REG_54 | CHAR(1) | Y |  |  |
| 11 | IND_REG_55 | CHAR(1) | Y |  |  |
| 12 | IND_REG_56 | CHAR(1) | Y |  |  |
| 13 | IND_REG_60 | CHAR(1) | Y |  |  |
| 14 | IND_REG_61 | CHAR(1) | Y |  |  |
| 15 | IND_REG_69 | CHAR(1) | Y |  |  |
| 16 | IND_REG_70 | CHAR(1) | Y |  |  |
| 17 | IND_REG_71 | CHAR(1) | Y |  |  |
| 18 | IND_REG_75 | CHAR(1) | Y |  |  |
| 19 | IND_REG_78 | CHAR(1) | Y |  |  |
| 20 | IND_REG_79 | CHAR(1) | Y |  |  |
| 21 | IND_REG_80 | CHAR(1) | Y |  |  |
| 22 | IND_REG_90 | CHAR(1) | Y |  |  |
| 23 | IND_REG_88 | CHAR(1) | Y |  |  |
| 24 | IND_REG_M2 | CHAR(1) | Y |  |  |
| 25 | IND_PROD_REG50 | CHAR(1) | Y |  |  |
| 26 | IND_REG_51_VLR_ZER | CHAR(1) | Y |  |  |
| 27 | IND_PROD_REG53 | CHAR(1) | Y |  |  |
| 28 | IND_REG_53_VLR_ZER | CHAR(1) | Y |  |  |
| 29 | IND_REG53_SUBST_TRIB | CHAR(1) | Y |  |  |
| 30 | IND_PROD_CFOP | CHAR(1) | Y |  |  |
| 31 | IND_FILTRAR_CFO_REG88 | CHAR(1) | Y |  |  |
| 32 | IND_TELECOM | CHAR(1) | Y |  |  |
| 33 | IND_ENERGIA_ELETR | CHAR(1) | Y |  |  |
| 34 | IND_CONHEC_TRANSP | CHAR(1) | Y |  |  |
| 35 | IND_NF_SERV_TRANSP | CHAR(1) | Y |  |  |
| 36 | IND_SAI_REM_MERC | CHAR(1) | Y |  |  |
| 37 | IND_SAI_REAJ_PRECO | CHAR(1) | Y |  |  |
| 38 | IND_ENT_DEVOL_MERC | CHAR(1) | Y |  |  |
| 39 | IND_SAI_VENDA_GLOB | CHAR(1) | Y |  |  |
| 40 | IND_ENT_DEVOL_SIMB | CHAR(1) | Y |  |  |
| 41 | IND_FILTRAR_CFO_PROD | CHAR(1) | Y |  |  |
| 42 | IND_ICMS_RET_OUT | CHAR(1) | Y |  |  |
| 43 | IND_JUST_PROD | CHAR(1) | Y |  |  |
| 44 | IND_JUST_NBM | CHAR(1) | Y |  |  |
| 45 | IND_JUST_DOC_FIS | CHAR(1) | Y |  |  |
| 46 | IND_OPERACAO_E_S | CHAR(1) | Y |  |  |
| 47 | IND_REG_72 | CHAR(1) | Y |  |  |
| 48 | IND_REG_73 | CHAR(1) | Y |  |  |
| 49 | IND_REG_74 | CHAR(1) | Y |  |  |
| 50 | IND_AGRUP_PROD | CHAR(1) | Y |  |  |
| 51 | IND_ZERA_NF_CANCEL | CHAR(1) | Y |  |  |
| 52 | IND_NF_ENT_CANCEL | CHAR(1) | Y |  |  |
| 53 | IND_REG_88C | CHAR(1) | Y |  |  |
| 54 | IND_REG_88D | CHAR(1) | Y |  |  |
| 55 | IND_REG_88E | CHAR(1) | Y |  |  |
| 56 | IND_REG_88M | CHAR(1) | Y |  |  |
| 57 | IND_REG_88Q | CHAR(1) | Y |  |  |
| 58 | IND_REG_88T | CHAR(1) | Y |  |  |
| 59 | IND_ATACADISTA_DF | CHAR(1) | Y |  |  |
| 60 | IND_REG_88GT | CHAR(1) | Y |  |  |
| 61 | IND_REG_60RD | CHAR(1) | Y |  |  |
| 62 | IND_REG_60RM | CHAR(1) | Y |  |  |
| 63 | IND_REG_60I | CHAR(1) | Y |  |  |
| 64 | IND_REG_76 | CHAR(1) | Y |  |  |
| 65 | IND_REG_77 | CHAR(1) | Y |  |  |
| 66 | IND_GRP_ITEM_PRD | CHAR(1) | Y |  |  |
| 67 | IND_REG_61R_SE | CHAR(1) | Y | 'N' |  |
| 68 | IND_REG_88_SE | CHAR(1) | Y | 'N' |  |
| 69 | IND_TP_FIS_JUR | CHAR(1) | Y | 1 |  |
| 70 | IND_ZER_GLOBAL | CHAR(1) | Y | 'N' |  |
| 71 | IND_ZER_ACOM_ECF | CHAR(1) | Y | 'N' |  |
| 72 | IND_NGER_IT_CANC | CHAR(1) | Y | 'N' |  |
| 73 | IND_REG_88C_CAT95 | CHAR(1) | Y | 'N' |  |
| 74 | IND_REG_88D_CAT95 | CHAR(1) | Y | 'N' |  |
| 75 | IND_REG_88E_CAT95 | CHAR(1) | Y | 'N' |  |
| 76 | IND_REG_88M_CAT95 | CHAR(1) | Y | 'N' |  |
| 77 | IND_REG_88T_CAT95 | CHAR(1) | Y | 'N' |  |
| 78 | IND_GER_ARMAZ_CAT95 | CHAR(1) | Y | 'N' |  |
| 79 | IND_TELECOM_REGS50 | CHAR(1) | Y |  |  |
| 80 | IND_EXC_ST_SAPROP | CHAR(1) | Y | 'N' |  |
| 81 | IND_EXC_ST_VCONTAB | CHAR(1) | Y | 'N' |  |
| 82 | IND_REG_85 | CHAR(1) | Y | 'N' |  |
| 83 | IND_REG_86 | CHAR(1) | Y | 'N' |  |
| 84 | IND_PARAM_REG75 | CHAR(1) | Y | 'S' | Indicador de utilizacao da parametrizacao do registro 75 (safx100) |
| 85 | IND_REG_88EC_MS | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88 para informacao do responsavel contador  |
| 86 | IND_REG_88SF_MS | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88 para informacao do responsavel pelo software  |
| 87 | IND_AG_PROD_MED | CHAR(1) | Y | 'N' |  |
| 88 | IND_REG88STES | CHAR(1) | Y | 'N' |  |
| 89 | IND_REG88STITNF | CHAR(1) | Y | 'N' |  |
| 90 | IND_REG88TMA | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88TMA - Detalhamento de Prestacao pre-paga  |
| 91 | IND_REG88TMB | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88TMB - Recargas ON-LINE/ Credito Virtual  |
| 92 | IND_REG88TMC | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88TMC - Ativações sem Destaque do Imposto  |
| 93 | IND_SEMDESC | CHAR(1) | Y | 'S' | Indicador de composicao de valor de desconto no valor contabil |
| 94 | IND_REG78_CAT90 | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 78 - CAT 90 - SP |
| 95 | IND_REG_88ECF_MS | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88 ECF para informacao do cupom fiscal para empresas que não geram o registro 60 I |
| 96 | IND_REG_88IT_MS | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88 IT para informacao de intervencao tecnica |
| 97 | IND_REG_88E_SME_MS | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88 ENTRADAS - INCENTIVO FISCAL |
| 98 | IND_REG_88S_SMS_MS | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88 SAIDAS - INCENTIVO FISCAL |
| 99 | IND_REG_88GT_UTL | CHAR(1) | Y |  | Indicador de geracao do registro 88 GT a partir do movimento aberto (SAFX42/SAFX43) |
| 100 | IND_REG_88CB | CHAR(1) | Y | 'N' | Indicador de utilizacao do registro 88 de relacionamento entre produto SERC e produto MSAF  |
| 101 | IND_OP_INTER_88STITNF | CHAR(1) | Y | 'N' | Indicador de utilizacao para tratamento de operacoes interestaduais |
| 102 | IND_REG_88A | CHAR(1) | Y | 'N' | Indicador de utilização do registro 88A que contem informações de produtos controlados de contribuintes do estado do PR |
| 103 | IND_REG_88RDI_MS | CHAR(1) | Y | 'N' | OS-2533:Informações do Resumo Diário de Produção de Açúcar e Álcool. |
| 104 | IND_REG_88LRDPAA_MS | CHAR(1) | Y | 'N' | OS-2533:Informações do Livro Registro Diário de Produção de Álcool Anidro. |
| 105 | IND_REG_88LRPDAH_MS | CHAR(1) | Y | 'N' | OS-2533:Informações do Livro de Registro da Produção Diária de Álcool Hidratado. |
| 106 | IND_REG_88LRPDA_MS | CHAR(1) | Y | 'N' | OS-2533:Informações do Livro de Registro da Produção Diária de Açúcar. |
| 107 | IND_REG_88NFRA_MS | CHAR(1) | Y | 'N' | OS-2533:Informações da Nota Fiscal de Registro de Aquisição de Cana-de-Açúcar. |
| 108 | IND_REG_88NFRA0110_MS | CHAR(1) | Y | 'N' | OS-2533:Informações do dia 01 a 10 das Notas Fiscais de Registro de Aquisição de Cana-de-Açúcar. |
| 109 | IND_REG_88NFRA1120_MS | CHAR(1) | Y | 'N' | OS-2533:Informações do dia 11 a 20 das Notas Fiscais de Registro de Aquisição de Cana-de-Açúcar. |
| 110 | IND_REG_88NFRA2131_MS | CHAR(1) | Y | 'N' | OS-2533:Informações dos dias 21 a 31 das Notas Fiscais de Registro de Aquisição de Cana¿de-Açúcar. |
| 111 | IND_REG_57 | CHAR(1) | Y | 'N' |  |
| 112 | IND_NUM_ITEM | CHAR(1) | Y | 'N' | Indica se o número                             do item sera gerado automaticamente ou se utilizara o numero direto da base de dados |
| 113 | IND_REG_88EAN | CHAR(1) | Y | 'N' |  |
| 114 | IND_NS_CFO_SINIEF | CHAR(1) | Y | 'N' | Indicador para considerar NS com CFOP's do Ajuste SINIEF 03/04 |
| 115 | IND_REG_51CFO_SERV | CHAR(1) | Y | 'N' | Indicador para gerar reg.51 para CFOP's de serviço |
| 116 | IND_REG_998 | CHAR(1) | Y | 'N' |  |
| 117 | IND_REG_88DV | CHAR(1) | Y | 'N' |  |
| 118 | IND_REG_54_MOD_06 | CHAR(1) | Y | 'N' |  |
| 119 | IND_ZER_INVENT | CHAR(1) | Y | 'N' |  |
| 120 | IND_MP_01 | CHAR(1) | Y |  | Considerar notas fiscais geradas a partir de Mapa Resumo (Modelo 01) |
| 121 | IND_NF_RJ_REG54 | CHAR(1) | Y | 'N' | Considerar notas fiscais de ativo fixo e uso/consumo para UF RJ (Registro 54) |
| 122 | IND_ORIGEM_ECF | CHAR(1) | Y | 'N' |  Gerar os registros de ECF através da SAFX991 ... SAFX994 |
| 123 | IND_REG_88L36451_RJ | CHAR(1) | Y | 'N' |  |
| 124 | IND_GER_PEPSICO | CHAR(1) | Y | 'N' | Indicador para gerar os registros especificos da PEPSICO |
| 125 | IND_GER88_STES_STITNF_TRIB | CHAR(1) | Y | 'N' | Indicador para tratar a mudança na forma de tributação nos registros 88STES e 88STITNF. |
| 126 | IND_NF_ENT_CANCEL_EMISSAO_P | CHAR(1) | Y |  |  |

**PK**: COD_PERFIL

---

## ICT_PAR_MM_CAMPOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 2 | NOME_CAMPO | VARCHAR2(20) | N |  |  |
| 3 | VALOR_CAMPO | VARCHAR2(2) | Y |  |  |

**PK**: COD_PERFIL, NOME_CAMPO

**FKs**:
- COD_PERFIL → ICT_PAR_MEIO_MAG(COD_PERFIL)

---

## ICT_PAR_MM_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 4 | COD_CFO | VARCHAR2(5) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PERFIL, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_PERFIL → ICT_PAR_MM_ESTAB(COD_EMPRESA, COD_ESTAB, COD_PERFIL)

---

## ICT_PAR_MM_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PERFIL | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PERFIL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PERFIL → ICT_PAR_MEIO_MAG(COD_PERFIL)

---

## ICT_PAR_MM_EXTCFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 4 | COD_CFO | VARCHAR2(5) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PERFIL, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_PERFIL → ICT_PAR_MM_ESTAB(COD_EMPRESA, COD_ESTAB, COD_PERFIL)

---

## ICT_PAR_MM_FISJUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 4 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PERFIL, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_PERFIL → ICT_PAR_MM_ESTAB(COD_EMPRESA, COD_ESTAB, COD_PERFIL)

---

## ICT_PAR_MM_MODELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_REGISTRO | VARCHAR2(4) | N |  |  |
| 2 | MODELO_DOCTO | VARCHAR2(2) | N |  |  |
| 3 | IND_CONV_31 | CHAR(1) | Y |  |  |
| 4 | IND_CONV_69 | CHAR(1) | Y |  |  |
| 5 | IND_CONV_18 | CHAR(1) | Y |  |  |
| 6 | IND_CONV_12 | CHAR(1) | Y |  |  |

**PK**: TIPO_REGISTRO, MODELO_DOCTO

---

## ICT_PAR_MM_NCM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 4 | COD_NCM | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PERFIL, COD_NCM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_PERFIL → ICT_PAR_MM_ESTAB(COD_EMPRESA, COD_ESTAB, COD_PERFIL)

---

## ICT_PAR_MM_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | IND_NF_PRODUTOR | CHAR(1) | Y | '2' | 1 - Registro 50 e 2 - Registro 61 |
| 3 | IND_REG53_SAPROP | CHAR(1) | Y | 'N' | S - Sim e N - Não |
| 4 | IND_REG54_CFO_ALIQ | CHAR(1) | Y | 'N' | Grupamento dos Reg. 54 Especiais: S - Quebra por CFOP/Alíquota; N - Quebra por Nota Fiscal |
| 5 | IND_REG54ESP_ZERA_CST | CHAR(1) | Y | 'N' | Gera campo CST zerado no registro 54 Especial . |

**PK**: COD_ESTADO

---

## ICT_PAR_MODELO_LIVRO
**Comment**: Tabela pré-povoada pela fábrica, utilizada em duas funcionalidades: 1- Na Programação do Livro Batch p/ montagem dos livros e modelos apresentados na tela.. 2 - Na tela de emissão dos Livros,  dada a opção de menu da emissões de um livro, saber qual modelo que deverá ser gravado na ICA_PARAM_GER_APUR (necessário quando existe a opção na tela Apenas Emitir)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | COD_TIPO_LIVRO da tabela TIPO_LIVRO_FISCAL |
| 2 | ITEM_MENU_EMISSAO | VARCHAR2(15) | N |  | Opção de menu de emissão do livro: pode ser um sequencial criado por livro. No caso dos livros P3 (105) e P7 (118, 107) será gravado o conteúdo do campo MODELO da estrutura S_PARAM_CHAMADA que é passada como parâmetro no Open da janela de emissão.  O campo Modelo da S_PARAM_CHAMADA já identifica o item de emissão do P3 e do P7. |
| 3 | DSC_MENU_EMISSAO | VARCHAR2(150) | Y |  | Titulo da opção do menu de emissão do livro. |
| 4 | DSC_TIPO_LIVRO | VARCHAR2(50) | Y |  | Descrição no Tipo de Livro que será apresentada na tela de Programação Batch (deve ser preenchido com o NOM_OFICIAL da tabela TIPO_LIVRO_FISCAL). |
| 5 | MODELO | CHAR(1) | Y |  | Modelo gravado na ICT_CONTROLE (que deve ser o mesmo MODELO a ser gravado na ICA_PARAM_GER_APUR). |
| 6 | DSC_MODELO | VARCHAR2(100) | Y |  | Descrição do Modelo (Ajuste Sinief, Convênio ICMS,...) |
| 7 | COD_MODULO | VARCHAR2(8) | Y |  | COD_MODULO da tabela PRT_MODULOS_MSAF: 005 - ICMS, 010 - IPI |
| 8 | IND_EXIBE_PROG_BATCH | CHAR(1) | Y |  | Identifica os livros/modelos que serão apresentados na tela de  Programação dos Livros BATCH. |
| 9 | IND_EXIBE_MODELO | CHAR(1) | Y |  | Indica se o modelo do livro será apresentado na tela de Programação dos Livros BATCH.  |
| 10 | FORMATO_LIVRO | VARCHAR2(30) | Y |  |  |
| 11 | IND_TELECOM | CHAR(1) | Y |  |  |
| 12 | IND_OBS_VALOR_ST | CHAR(1) | Y |  |  |
| 13 | IND_RESUMO_OBSERVACOES | CHAR(1) | Y |  |  |
| 14 | IND_TRATA_ICMSS_N_ESCRIT | CHAR(1) | Y |  |  |
| 15 | IND_BASE_ST_N_ESCRIT_OBS | CHAR(1) | Y |  |  |

**PK**: COD_TIPO_LIVRO, ITEM_MENU_EMISSAO

**FKs**:
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## ICT_PAR_OBS_UF_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | VALID_PARAM | DATE | N |  |  |
| 5 | GRUPO_OBS_LIVRO | VARCHAR2(9) | Y |  |  |
| 6 | COD_OBS_LIVRO | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_CFO, VALID_PARAM

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## ICT_PAR_OBS_UF_SIT_ESP_ST
**Comment**: Tabela de Parametrização das Observações por UF/Situacao Especial ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | IND_SIT_ESP_ST | CHAR(1) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | VALID_PARAM | DATE | N |  |  |
| 6 | DESCRICAO | VARCHAR2(45) | N |  |  |
| 7 | DESCRICAO_1 | VARCHAR2(45) | Y |  |  |
| 8 | DESCRICAO_2 | VARCHAR2(45) | Y |  |  |
| 9 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg E111/E220) -                              referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |
| 10 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 11 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 12 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 13 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, IND_SIT_ESP_ST, COD_TIPO_LIVRO, VALID_PARAM

**FKs**:
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## ICT_PAR_TC_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 4 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 5 | COD_CFO_ENTR | VARCHAR2(4) | Y |  |  |
| 6 | COD_CFO_SAIDA | VARCHAR2(4) | Y |  |  |
| 7 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 8 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 9 | COD_CFO_ENTR_DEBITO | VARCHAR2(4) | Y |  |  |
| 10 | COD_CFO_SAIDA_DEBITO | VARCHAR2(4) | Y |  |  |
| 11 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 12 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)

---

## ICT_PAR_TC_ESTAB_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO_ENTR_CRED | VARCHAR2(9) | Y |  |  |
| 4 | IND_PRODUTO_ENTR_CRED | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO_ENTR_CRED | VARCHAR2(60) | Y |  |  |
| 6 | GRUPO_PRODUTO_SAIDA_CRED | VARCHAR2(9) | Y |  |  |
| 7 | IND_PRODUTO_SAIDA_CRED | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO_SAIDA_CRED | VARCHAR2(60) | Y |  |  |
| 9 | GRUPO_PRODUTO_ENTR_DEB | VARCHAR2(9) | Y |  |  |
| 10 | IND_PRODUTO_ENTR_DEB | CHAR(1) | Y |  |  |
| 11 | COD_PRODUTO_ENTR_DEB | VARCHAR2(60) | Y |  |  |
| 12 | GRUPO_PRODUTO_SAIDA_DEB | VARCHAR2(9) | Y |  |  |
| 13 | IND_PRODUTO_SAIDA_DEB | CHAR(1) | Y |  |  |
| 14 | COD_PRODUTO_SAIDA_DEB | VARCHAR2(60) | Y |  |  |
| 15 | GRUPO_UND_PADRAO | VARCHAR2(9) | Y |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 17 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 18 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 19 | COD_CFO_ENTR_CRED | VARCHAR2(4) | Y |  |  |
| 20 | COD_CFO_SAIDA_CRED | VARCHAR2(4) | Y |  |  |
| 21 | COD_CFO_ENTR_DEB | VARCHAR2(4) | Y |  |  |
| 22 | COD_CFO_SAIDA_DEB | VARCHAR2(4) | Y |  |  |
| 23 | GRUPO_NATUREZA_OP_ENTR_CRED | VARCHAR2(9) | Y |  |  |
| 24 | COD_NATUREZA_OP_ENTR_CRED | VARCHAR2(3) | Y |  |  |
| 25 | GRUPO_NATUREZA_OP_SAIDA_CRED | VARCHAR2(9) | Y |  |  |
| 26 | COD_NATUREZA_OP_SAIDA_CRED | VARCHAR2(3) | Y |  |  |
| 27 | GRUPO_NATUREZA_OP_ENTR_DEB | VARCHAR2(9) | Y |  |  |
| 28 | COD_NATUREZA_OP_ENTR_DEB | VARCHAR2(3) | Y |  |  |
| 29 | GRUPO_NATUREZA_OP_SAIDA_DEB | VARCHAR2(9) | Y |  |  |
| 30 | COD_NATUREZA_OP_SAIDA_DEB | VARCHAR2(3) | Y |  |  |
| 31 | GRUPO_OBSERVACAO_ENTR_CRED | VARCHAR2(9) | Y |  |  |
| 32 | COD_OBSERVACAO_ENTR_CRED | VARCHAR2(8) | Y |  |  |
| 33 | GRUPO_OBSERVACAO_SAIDA_CRED | VARCHAR2(9) | Y |  |  |
| 34 | COD_OBSERVACAO_SAIDA_CRED | VARCHAR2(8) | Y |  |  |
| 35 | GRUPO_OBSERVACAO_ENTR_DEB | VARCHAR2(9) | Y |  |  |
| 36 | COD_OBSERVACAO_ENTR_DEB | VARCHAR2(8) | Y |  |  |
| 37 | GRUPO_OBSERVACAO_SAIDA_DEB | VARCHAR2(9) | Y |  |  |
| 38 | COD_OBSERVACAO_SAIDA_DEB | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_PAR_TIPO_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 4 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 5 | COD_PARAM | VARCHAR2(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_DOCTO, COD_DOCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_PARAM → ICT_PAR_APURAC_ST(COD_EMPRESA, COD_ESTAB, COD_PARAM)

---

## ICT_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 3 | DESC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 4 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 5 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_IPI_1 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_IPI_2 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_IPI_3 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ICMSS_2 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ICMSS_3 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ST_DENTRO_UF | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ST_D_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ST_FORA_UF | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ST_F_UF_IMP_C | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_ICT_PROD (UNIQUE): (NUM_PROCESSO, COD_PRODUTO)

---

## ICT_PROD_P2_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | VLR_BASE_1 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_3 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 12 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_PROD_P2_M2 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_PRODUTO, TITULO_TRIBUTO, DESCRICAO, USUARIO)

---

## ICT_PROG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | DSC_PROG | VARCHAR2(50) | Y |  |  |
| 4 | IND_PERIOD | CHAR(1) | Y |  |  |
| 5 | DAT_INI_EVENT | DATE | Y |  |  |
| 6 | COD_PROG_SEMANAL | VARCHAR2(7) | Y |  |  |
| 7 | COD_PROG_MENSAL | VARCHAR2(64) | Y |  |  |
| 8 | DAT_INI_PERIODO | DATE | Y |  |  |
| 9 | DAT_FIM_PERIODO | DATE | Y |  |  |
| 10 | COD_MODULO | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_PROG

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## ICT_PR_EXTCFO_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 4 | COD_PARAM | NUMBER(3) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 7 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, COD_PARAM, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT → ICT_GRP_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## ICT_RATEIO_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PARAMETROS | NUMBER | N |  |  |
| 2 | ID_PARAM_ESTAB | NUMBER | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | VLR_CRED | NUMBER(17,2) | Y | 0 |  |

**PK**: ID_PARAMETROS, ID_PARAM_ESTAB, DAT_APURACAO, SERIE_LIVRO, SUB_SERIE_LIVRO

---

## ICT_REGRA_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 4 | VALIDADE_INICIAL | DATE | N |  |  |
| 5 | VALIDADE_FINAL | DATE | Y |  |  |
| 6 | IND_PESO_QTD | CHAR(1) | Y |  |  |
| 7 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 8 | IND_CONTROLE_FAIXA | CHAR(1) | Y |  |  |
| 9 | PERC_SAIDAS_INTEREST | NUMBER(7,4) | Y |  |  |
| 10 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 11 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 12 | PERC_ENTRADAS | NUMBER(7,4) | Y |  |  |
| 13 | IND_OPER_INCENT | CHAR(1) | Y | 'N' |  |
| 14 | IND_CONS_VLR_ITEM | CHAR(1) | Y | 'N' |  |
| 15 | IND_OPER_LVR_INCENT | VARCHAR2(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT, VALIDADE_INICIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT → ICT_GRP_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## ICT_REG_1920

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | IND_SUB_APUR | CHAR(1) | N |  |  |
| 5 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |
| 7 | DAT_OPERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APUR, IND_SUB_APUR

---

## ICT_REG_1920_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_APUR | DATE | N |  |  |
| 5 | IND_SUB_APUR | CHAR(1) | N |  |  |
| 6 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | DAT_OPERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_APUR, IND_SUB_APUR

---

## ICT_RES_ALIQ_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | IND_E_S | CHAR(1) | N |  |  |
| 8 | VLR_ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 13 | NRO_FOLHA | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO, IND_E_S, VLR_ALIQ_ICMS

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO → ICT_APURACAO_INCE(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, DAT_APURACAO)

---

## ICT_RES_ALIQ_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 10 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 13 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |

**Indexes**:
- IX_ICT_RES_ALIQ_P1: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, VLR_ALIQ_ICMS)

---

## ICT_RES_ALIQ_P1_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_ALIQ_P1_M2 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, VLR_ALIQ_ICMS, INSC_ESTADUAL)

---

## ICT_RES_ALIQ_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 10 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 13 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |

**Indexes**:
- IX_ICT_RES_ALIQ_P2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, VLR_ALIQ_ICMS)

---

## ICT_RES_ALIQ_P2_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_ALIQ_P2_M2 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, VLR_ALIQ_ICMS, INSC_ESTADUAL)

---

## ICT_RES_ALIQ_P9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_E_S | CHAR(1) | Y |  |  |
| 6 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 7 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 11 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

---

## ICT_RES_ALMOX_P3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | GRUPO_ALMOX | VARCHAR2(9) | Y |  |  |
| 5 | COD_ALMOX | VARCHAR2(35) | Y |  |  |
| 6 | DESCRICAO_ALMOX | VARCHAR2(50) | Y |  |  |
| 7 | SALDO_INICIAL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT_ENTRADA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_SAIDA | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

---

## ICT_RES_DAICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_E_S | CHAR(1) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | N |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_DIF_ALIQ | NUMBER(17,2) | Y |  |  |
| 14 | DIF_ALIQ_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_CALC_IMP | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_IMP | NUMBER(17,2) | Y |  |  |
| 17 | OBSERVACOES | VARCHAR2(50) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, COD_TIPO_LIVRO, DAT_APURACAO, IND_E_S, COD_CFO, ALIQ_TRIBUTO_ICMS

**FKs**:
- COD_EMPRESA, COD_ESTAB_CENTR, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ICT_RES_NAT_P7

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N | ' ' |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_NAT_ESTOQUE | NUMBER(12) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_NAT_ESTOQUE, IND_PRODUTO

---

## ICT_RES_OBS_LVR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | USUARIO | VARCHAR2(40) | N |  |  |
| 6 | NRO_PROCESSO | NUMBER(12) | N |  |  |
| 7 | IND_OBS | CHAR(1) | N |  |  |
| 8 | VALOR_APURADO | NUMBER(17,2) | Y |  |  |
| 9 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO, NRO_PROCESSO, IND_OBS

---

## ICT_RES_OBS_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | DATA_FISCAL | DATE | N |  |  |
| 11 | DATA_EMISSAO | DATE | N |  |  |
| 12 | USUARIO | VARCHAR2(40) | N |  |  |
| 13 | NRO_PROCESSO | NUMBER(12) | N |  |  |
| 14 | IND_OBS | CHAR(1) | N |  |  |
| 15 | VALOR_APURADO | NUMBER(17,2) | Y |  |  |
| 16 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL, DATA_EMISSAO, USUARIO, NRO_PROCESSO, IND_OBS

**Indexes**:
- IX1_ICT_RES_OBS_NF (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL, DATA_EMISSAO, USUARIO, NRO_PROCESSO, IND_OBS, INSC_ESTADUAL)

---

## ICT_SUB_APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | IND_SUB_APUR | CHAR(1) | N |  |  |
| 5 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 6 | VLR_AJ_DEB | NUMBER(17,2) | Y |  |  |
| 7 | VLR_OUT_DEB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 10 | VLR_AJ_CRED | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUT_CRED | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOT_DED | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DEB_ESP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APUR, IND_SUB_APUR

---

## ICT_SUB_APURACAO_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_APUR | DATE | N |  |  |
| 5 | IND_SUB_APUR | CHAR(1) | N |  |  |
| 6 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 7 | VLR_AJ_DEB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_OUT_DEB | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 11 | VLR_AJ_CRED | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OUT_CRED | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TOT_DED | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DEB_ESP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_APUR, IND_SUB_APUR

---

## ICT_SUB_APURACAO_RS
**Comment**: Tabela da SUB-APURACAO do Ressarcimento RS (Registro 1920 - Sped Fiscal)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | Codigo do Livro da Apuracao do ICMS. Valores: 108, 165 |
| 5 | IND_SUB_APUR | VARCHAR2(1) | N |  | Identificador da Sub-apuracao do ICMS. Valores assumidos: 1, 2, 3, 4, 5, 6. |
| 6 | VLR_TOT_DEB | NUMBER(17,2) | Y |  | Valor total dos debitos por Saidas e prestacoes com debito do imposto |
| 7 | VLR_OUT_DEB | NUMBER(17,2) | Y |  | Valor total de Ajustes a debito  |
| 8 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  | Valor total de Ajustes Estornos de creditos |
| 9 | VLR_TOT_CRED | NUMBER(17,2) | Y |  | Valor total dos creditos por Entradas e aquisicoes com credito do imposto |
| 10 | VLR_OUT_CRED | NUMBER(17,2) | Y |  | Valor total de Ajustes a credito |
| 11 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  | Valor total de Ajustes Estornos de Debitos |
| 12 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  | Valor total de Saldo credor do periodo anterior |
| 13 | VLR_SLD_APURADO | NUMBER(17,2) | Y |  | Valor do saldo devedor apurado |
| 14 | VLR_TOT_DED | NUMBER(17,2) | Y |  | Valor total de Deducoes |
| 15 | VL_ICMS_RECOLHER | NUMBER(17,2) | Y |  | Valor total de ICMS a recolher (09-10) |
| 16 | VL_SLD_CREDOR_TRANSP | NUMBER(17,2) | Y |  | Valor total de Saldo credor a transportar para o periodo seguinte |
| 17 | VLR_DEB_ESP | NUMBER(17,2) | Y |  | Valores recolhidos ou a recolher, extraapuracao. |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_TIPO_LIVRO, IND_SUB_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## ICT_TABREG80_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |
| 4 | COD_NATUREZA_OP | VARCHAR2(2) | Y |  |  |
| 5 | DSC_NATUREZA_OP | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, IDENT_NATUREZA_OP

---

## ICT_TABREG80_02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | IDENT_MEDIDA | NUMBER(12) | N |  |  |
| 4 | COD_MEDIDA | VARCHAR2(2) | Y |  |  |
| 5 | DSC_MEDIDA | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, IDENT_MEDIDA

---

## ICT_TABREG80_03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(6) | Y |  |  |
| 5 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, IDENT_PRODUTO

---

## ICT_TABREG80_04

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 4 | COD_DOCTO | VARCHAR2(2) | Y |  |  |
| 5 | DSC_DOCTO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, IDENT_DOCTO

---

## ICT_TC_CENTRALIZA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | DAT_EMISSAO | DATE | Y |  |  |
| 12 | IND_SALDO | CHAR(1) | Y |  |  |
| 13 | VLR_SALDO | NUMBER(17,2) | Y |  |  |
| 14 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 15 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, COD_TIPO_LIVRO, DAT_APURACAO, COD_ESTAB

---

## ICT_TC_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | VLR_TRANSF | NUMBER(17,2) | Y |  |  |
| 5 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 6 | IND_TRANSF | CHAR(1) | Y |  |  |
| 7 | COD_ESTAB_C | VARCHAR2(6) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | MOVTO_E_S_F | CHAR(1) | Y |  |  |
| 12 | MOVTO_E_S_C | CHAR(1) | Y |  |  |
| 13 | NORM_DEV | CHAR(1) | Y |  |  |
| 14 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 15 | IDENT_FIS_JUR_F | NUMBER(12) | Y |  |  |
| 16 | IDENT_FIS_JUR_C | NUMBER(12) | Y |  |  |
| 17 | NUM_DOCFIS_GER | VARCHAR2(12) | Y |  |  |
| 18 | SERIE_DOCFIS_GER | VARCHAR2(3) | Y |  |  |
| 19 | SSERIE_DOCFIS_GER | VARCHAR2(2) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | DAT_FISCAL | DATE | Y |  |  |
| 23 | DAT_FISCAL_GER | DATE | Y |  |  |
| 24 | VLR_TRANSF_GER | NUMBER(17,2) | Y |  |  |
| 25 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 26 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 27 | NUM_AUTENTIC_NFE_GER | VARCHAR2(80) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_TC_ESTAB: (COD_EMPRESA, COD_ESTAB_C, COD_ESTAB, DAT_APURAC)

---

## ICT_TC_ESTAB_CENTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |
| 4 | IND_GERA_LANCTO | CHAR(1) | Y |  |  |
| 5 | IND_CONTROLE_SALDO | CHAR(1) | Y |  |  |
| 6 | IND_CENTR_SLD_CAT115 | CHAR(1) | Y | 'N' | Indicador de Centralização de Saldos conforme Portaria Cat115 |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB_CENTR → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_TC_ESTAB_RJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CREDOR | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_DEVEDOR | VARCHAR2(6) | N |  |  |
| 4 | DAT_APURAC | DATE | N |  |  |
| 5 | VLR_TRANSF | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CREDOR_INI | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CREDOR_FIM | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEVEDOR_INI | NUMBER(17,2) | Y |  |  |
| 9 | VLR_DEVEDOR_FIM | NUMBER(17,2) | Y |  |  |
| 10 | IND_TRANSF_DEVEDOR | CHAR(1) | Y |  |  |
| 11 | IND_TRANSF_CREDOR | CHAR(1) | Y |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 15 | IND_GERACAO | CHAR(1) | Y |  |  |
| 16 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 17 | IDENT_FIS_JUR_C | NUMBER(12) | Y |  |  |
| 18 | IDENT_FIS_JUR_D | NUMBER(12) | Y |  |  |
| 19 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 20 | DAT_EMISSAO | DATE | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 24 | COD_ESTADO | VARCHAR2(2) | N | 'RJ' |  |

**PK**: COD_EMPRESA, COD_ESTADO, COD_ESTAB_CREDOR, COD_ESTAB_DEVEDOR, DAT_APURAC

---

## ICT_TC_REL_SALDOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | DAT_APURACAO | DATE | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | VLR_SALDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, DAT_APURACAO, COD_ESTADO, COD_ESTAB

---

## ICT_TOT_CFO_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 6 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 7 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 10 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 11 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 13 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 15 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 18 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 19 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 20 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 21 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_TOT_CFO_1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_CFO, TITULO_TRIBUTO, USUARIO)
- IX_ICT_TOT_CFO_2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO)

---

## ICT_TOT_CFO_P1A_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 6 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 9 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 10 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 15 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 16 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 17 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_CFO_P1A_M2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_CFO_SUP, COD_CFO, TITULO_TRIBUTO, COD_TRIBUTACAO)

---

## ICT_TOT_CFO_P1_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 6 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | COD_TRIBUT_IPI | CHAR(1) | Y |  |  |
| 12 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 13 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 17 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 18 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_CFO_P1_M2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_CFO_SUP, COD_CFO, COD_TRIBUT_ICMS)

---

## ICT_TOT_CFO_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 6 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 7 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 10 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 11 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 13 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 15 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 18 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 19 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 20 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 21 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_TOT_CFO2_1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_CFO, TITULO_TRIBUTO, USUARIO)
- IX_ICT_TOT_CFO2_2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO)

---

## ICT_TOT_CFO_P2_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 6 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 9 | VLR_BASE_1 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_2 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_3 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 16 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 17 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_CFO_P2_M2: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_CFO, COD_TRIBUTO)

---

## ICT_TOT_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 6 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 7 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 13 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 14 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | VLR_ST_DENTRO_UF | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ST_FORA_UF | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TOT_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOT_ST_RETIDO | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ST_D_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ST_F_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 22 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 23 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 24 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_TOT_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO)

---

## ICT_TOT_P1A_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 6 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 7 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_TOT_P1A_M2 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, TITULO_TRIBUTO, COD_TRIBUTACAO, IND_TIPO_TOTAL, INSC_ESTADUAL)

---

## ICT_TOT_P1_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 6 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 7 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 8 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | COD_TRIBUT_IPI | CHAR(1) | Y |  |  |
| 11 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 12 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_TOT_P1_M2 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_TRIBUT_ICMS, COD_TRIBUT_IPI, IND_TIPO_TOTAL, INSC_ESTADUAL)

---

## ICT_TOT_P1_SJ_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 6 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 7 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 8 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | COD_TRIBUT_IPI | VARCHAR2(4) | Y |  |  |
| 11 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 12 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TRIBUTO_SJ | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_ICT_TT_P1_SJ_M2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ICT_TOT_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 6 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 7 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 13 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 14 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 17 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 18 | IND_MERC_SERV | CHAR(1) | Y |  | Indica se o registro é de Mercadoria (M) ou Serviço (S) |

**Indexes**:
- IX_ICT_TOT_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, USUARIO)

---

## ICT_TOT_P2_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 6 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 7 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | VLR_BASE_1 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_3 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | VLR_ST_DENTRO_UF | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ST_FORA_UF | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ST_D_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ST_F_UF_IMP_C | NUMBER(17,2) | Y |  |  |
| 19 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_TOT_P2_M2 (UNIQUE): (USUARIO, IND_TIPO_TOTAL, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_TRIBUTO, INSC_ESTADUAL)

---

## ICT_TOT_P3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 6 | TOT_ESTOQUE | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_TOT_P3: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IND_PRODUTO)

---

## ICT_TOT_P7

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y | ' ' |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 11 | IDENT_CONTA | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_ICT_TOT_P7: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, GRUPO_CONTAGEM, IND_PRODUTO)

---

## ICT_TOT_SAIDA_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_APURACAO | DATE | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 5 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 6 | VLR_TOTAL_SAI | NUMBER(17,2) | Y |  |  |
| 7 | VLR_PERC_SAI | NUMBER(7,4) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_PERC_ICMS | NUMBER(7,4) | Y |  |  |
| 10 | COD_GRP_INCENT | VARCHAR2(5) | Y |  |  |
| 11 | PERCENTUAL_INCENT | NUMBER(7,4) | N | 0 |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, SERIE_LIVRO, SUB_SERIE_LIVRO, PERCENTUAL_INCENT

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICT_TOT_SAID_IN_BK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | DATE | Y |  |  |
| 4 | VLR_ICMS_TOT_SAI | NUMBER(17,2) | Y |  |  |
| 5 | VLR_ICMS_INCI_SAI | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_INCF_SAI | NUMBER(17,2) | Y |  |  |
| 7 | VLR_PERC_INCI_SAI | NUMBER(7,4) | Y |  |  |
| 8 | VLR_PERC_INCF_SAI | NUMBER(7,4) | Y |  |  |
| 9 | VLR_PERC_INCT_SAI | NUMBER(7,4) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

---

## ICT_TRIBINT_P1A_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 12 | DSC_TRIB_INT | VARCHAR2(100) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_TRIBINT_P1A (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_TRIB_REL, TITULO_TRIBUTO, COD_TRIBUTACAO, INSC_ESTADUAL)

---

## ICT_TRIB_INT_P1_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | COD_TRIBUT_ICMS | VARCHAR2(4) | Y |  |  |
| 8 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | COD_TRIBUT_IPI | CHAR(1) | Y |  |  |
| 11 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 12 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 13 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 14 | DSC_TRIB_INT | VARCHAR2(100) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_TRIB_INT_P1 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_TRIB_REL, COD_TRIBUT_ICMS, INSC_ESTADUAL)

---

## ICT_TRIB_INT_P2_M2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | VLR_BASE_1 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_3 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 12 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 13 | DSC_TRIB_INT | VARCHAR2(100) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_ICT_TRIB_INT_P2 (UNIQUE): (USUARIO, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_TRIB_REL, TITULO_TRIBUTO, INSC_ESTADUAL)

---

## ICT_VLR_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_GRP_INCENT | VARCHAR2(5) | N |  |  |
| 5 | PERCENTUAL_INCENT | NUMBER(7,4) | N |  |  |
| 6 | TIPO_INCENT | VARCHAR2(2) | N |  |  |
| 7 | VLR_BASE_CPRES | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CPRES | NUMBER(17,2) | Y |  | Valor do credito presumido calculado + ajustes realizados. Sera o valor definitivo lancado na apuracao |
| 9 | VLR_FAT_BRUTO | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DEB_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TOTAL_SAI | NUMBER(17,2) | Y |  |  |
| 14 | PERC_TOTAL_SAI | NUMBER(7,4) | Y |  |  |
| 15 | VLR_CRED_ICMS_LANC | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DEB_ICMS_LANC | NUMBER(17,2) | Y |  |  |
| 17 | SERIE_LIVRO | CHAR(1) | Y |  |  |
| 18 | SUB_SERIE_LIVRO | VARCHAR2(2) | Y |  |  |
| 19 | VLR_CPRES_CALC | NUMBER(17,2) | Y |  | Valor original do credito presumido calculado. Este valor NAO e alterado no ajuste. |
| 20 | VLR_ESTORNO | NUMBER(17,2) | Y |  | Valor do estorno calculado quando as vendas do periodo não atingirem a meta |
| 21 | VLR_CRED_ICMS_DEVOL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_GRP_INCENT, PERCENTUAL_INCENT, TIPO_INCENT

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT → ICT_GRP_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT)

---

