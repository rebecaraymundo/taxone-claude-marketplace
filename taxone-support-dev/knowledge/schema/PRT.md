# Módulo: PRT (PRT) - 197 tabelas

## PRT_AJUSTE_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_AJUSTE | VARCHAR2(3) | Y |  |  |
| 2 | DSC_AJUSTE | VARCHAR2(500) | Y |  |  |

---

## PRT_AJUSTE_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_AJUSTE_SPED

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## PRT_AMPARO_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCORR, COD_CFO

---

## PRT_AMPARO_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 8 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCORR, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## PRT_APUR_IPI_LANCTO_AUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PRT_APUR_IPI_LANCTO_AUT | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  |  |
| 5 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 6 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 7 | DSC_LANCAMENTO | VARCHAR2(200) | Y |  |  |
| 8 | IND_VLR_IPI | VARCHAR2(1) | Y |  |  |
| 9 | IND_VLR_OUTROS_IPI | VARCHAR2(1) | Y |  |  |
| 10 | IND_VLR_IPI_NDESTAC | VARCHAR2(1) | Y |  |  |
| 11 | IND_IND_IPI_NDESTAC_DF | VARCHAR2(1) | Y |  |  |
| 12 | IND_VLR_IPI_DEV | VARCHAR2(1) | Y |  |  |
| 13 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 14 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |

**PK**: ID_PRT_APUR_IPI_LANCTO_AUT

**FKs**:
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- UK_PRT_APUR_IPI_LANCTO_AUT (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_AJUSTE_IPI, COD_TIPO_LIVRO)

---

## PRT_APUR_LANCTO_AUT_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PRT_APUR_IPI_LANCTO_AUT | NUMBER(12) | N |  |  |
| 2 | IDENT_CFO | NUMBER(12) | N |  |  |

**PK**: ID_PRT_APUR_IPI_LANCTO_AUT, IDENT_CFO

**FKs**:
- ID_PRT_APUR_IPI_LANCTO_AUT → PRT_APUR_IPI_LANCTO_AUT(ID_PRT_APUR_IPI_LANCTO_AUT)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## PRT_APUR_LANCTO_AUT_NAT_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PRT_APUR_IPI_LANCTO_AUT | NUMBER(12) | N |  |  |
| 2 | IDENT_CFO | NUMBER(12) | N |  |  |
| 3 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |

**PK**: ID_PRT_APUR_IPI_LANCTO_AUT, IDENT_CFO, IDENT_NATUREZA_OP

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- ID_PRT_APUR_IPI_LANCTO_AUT → PRT_APUR_IPI_LANCTO_AUT(ID_PRT_APUR_IPI_LANCTO_AUT)

---

## PRT_APUR_LANCTO_AUT_NBM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PRT_APUR_IPI_LANCTO_AUT | NUMBER(12) | Y |  |  |
| 2 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 3 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 4 | IDENT_NBM | NUMBER(12) | Y |  |  |

**FKs**:
- ID_PRT_APUR_IPI_LANCTO_AUT → PRT_APUR_IPI_LANCTO_AUT(ID_PRT_APUR_IPI_LANCTO_AUT)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)

**Indexes**:
- UK_PRT_APUR_LANCTO_AUT_NBM (UNIQUE): (ID_PRT_APUR_IPI_LANCTO_AUT, IDENT_CFO, IDENT_NATUREZA_OP, IDENT_NBM)

---

## PRT_APUR_LANCTO_AUT_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PRT_APUR_IPI_LANCTO_AUT | NUMBER(12) | Y |  |  |
| 2 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 3 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |

**FKs**:
- ID_PRT_APUR_IPI_LANCTO_AUT → PRT_APUR_IPI_LANCTO_AUT(ID_PRT_APUR_IPI_LANCTO_AUT)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)

**Indexes**:
- UK_PRT_APUR_LANCTO_AUT_PROD (UNIQUE): (ID_PRT_APUR_IPI_LANCTO_AUT, IDENT_CFO, IDENT_NATUREZA_OP, IDENT_PRODUTO)

---

## PRT_ARRECAD_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_ARRECAD | VARCHAR2(3) | N |  |  |
| 3 | DSC_ARRECAD | VARCHAR2(40) | Y |  |  |

**PK**: COD_MODULO, COD_ARRECAD

---

## PRT_ATIV_ECONOMICA_MSAF_OBRIG
**Comment**: Tabela de parametrizacao Atividade Economica do Mastersaf por Codigo CTISS das Obrigacoes Municipais.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_ATIVIDADE | NUMBER(7) | N |  | Referente ao COD_ATIVIDADE da tabela ATIV_ECONOMICA (CNAE) |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | COD_CTISS_OBRIG | VARCHAR2(9) | Y |  |  |

**PK**: VALID_INICIAL, COD_ATIVIDADE, COD_MODULO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_ATIV_MSAF_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | COD_CNAE | NUMBER(7) | N |  |  |
| 4 | COD_CNAE_OBRIG | NUMBER(9) | N |  |  |

**PK**: VALID_INICIAL, COD_MODULO, COD_CNAE

---

## PRT_ATIV_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_CNAE_OBRIG | NUMBER(9) | N |  |  |
| 3 | DSC_CNAE_OBRIG | VARCHAR2(500) | Y |  |  |

**PK**: COD_MODULO, COD_CNAE_OBRIG

---

## PRT_BALANCO_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_CLASSE_BALANCO | VARCHAR2(9) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_CLASSE_BALANCO

**FKs**:
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)
- COD_CLASSE_BALANCO → DWT_CLASSE_BALANCO(COD_CLASSE_BALANCO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_BENEF_FISCAL_OBRIG
**Comment**: Tabela de cadastro de codigos dos Beneficios Fiscais das obrigacoes, ex NF Carioca. TFIX122

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_BENEF_FISCAL | VARCHAR2(10) | N |  |  |
| 3 | DSC_BENEF_FISCAL | VARCHAR2(150) | Y |  |  |

**PK**: COD_MODULO, COD_BENEF_FISCAL

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_CAD_BENEF_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ATO_LEGAL | VARCHAR2(2) | N |  |  |
| 2 | NUMERO_ANO | VARCHAR2(12) | N |  |  |
| 3 | COD_ESPECIE | VARCHAR2(2) | N |  |  |
| 4 | DATA_INI | DATE | N |  |  |
| 5 | DATA_FIM | DATE | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(1100) | Y |  |  |

**PK**: COD_ATO_LEGAL, NUMERO_ANO, COD_ESPECIE, DATA_INI

---

## PRT_CAD_CNPJ_IRPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TABELA | VARCHAR2(10) | N |  |  |
| 2 | GRUPO | VARCHAR2(9) | N |  |  |
| 3 | CNPJ_IRPJ | VARCHAR2(14) | N |  |  |
| 4 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: COD_TABELA, GRUPO

---

## PRT_CAD_CNPJ_IRPJ_EMPRESA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_TABELA | VARCHAR2(10) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | CNPJ_IRPJ | VARCHAR2(14) | N |  |  |
| 5 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_TABELA, GRUPO

---

## PRT_CALC_LINHA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | NUM_LINHA | NUMBER(4) | N |  |  |
| 3 | DAT_VIGENCIA | DATE | N |  |  |
| 4 | NUM_LINHA_COMP | NUMBER(4) | N |  |  |
| 5 | DAT_VIG_COMP | DATE | N |  |  |
| 6 | COD_TP_OPER | CHAR(1) | Y |  |  |

**PK**: COD_ESTADO, NUM_LINHA, DAT_VIGENCIA, NUM_LINHA_COMP, DAT_VIG_COMP

**FKs**:
- COD_ESTADO, NUM_LINHA, DAT_VIGENCIA → PRT_LINHA_UF_MSAF(COD_ESTADO, NUM_LINHA, DAT_VIGENCIA)

---

## PRT_CALC_RECOL_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 2 | IND_TP_DATA | CHAR(1) | Y |  |  |
| 3 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 4 | IND_TP_CONT_DIA | CHAR(2) | Y |  |  |
| 5 | NUM_DIA | NUMBER(2) | Y |  |  |
| 6 | IND_TP_NF | CHAR(1) | N |  |  |

**PK**: COD_MUNIC_ISS, IND_TP_NF

---

## PRT_CANAIS_DISTRIB_MSAF_OBRIG
**Comment**: Tabela de parametrizacao dos Canais de Distribuicao/Obras (DWT_CANAIS_DISTRIB) por sequenciais definidos por cada obrigacao municipal.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_CANAL_DISTRIB | VARCHAR2(10) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | SEQ_OBRIG | VARCHAR2(9) | Y |  |  |

**PK**: VALID_INICIAL, COD_CANAL_DISTRIB, COD_MODULO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- COD_CANAL_DISTRIB → DWT_CANAIS_DISTRIB(COD_CANAL_DISTRIB)

---

## PRT_CARACTERISTICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CARACT | VARCHAR2(3) | N |  |  |
| 2 | DATA_INI_VALID | DATE | N |  |  |
| 3 | DATA_FIM_VALID | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 5 | COD_UNIDADE | VARCHAR2(15) | Y |  |  |

**PK**: COD_CARACT, DATA_INI_VALID

---

## PRT_CATEGORIA_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_VALID | DATE | N |  |  |
| 2 | COD_CATEGORIA | VARCHAR2(2) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 4 | IND_AUTONOMO | CHAR(1) | Y |  |  |

**PK**: DATA_VALID, COD_CATEGORIA

---

## PRT_CATEG_TRAB_ESOCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CATEG_TRAB | VARCHAR2(3) | N |  |  |
| 2 | DSC_CATEG_TRAB | VARCHAR2(250) | Y |  |  |

**PK**: COD_CATEG_TRAB

---

## PRT_CENTRAL_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PARAM | NUMBER(3) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | ESTAB_CENTRAL | VARCHAR2(6) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_PARAM, COD_EMPRESA, ESTAB_CENTRAL, COD_ESTAB

**FKs**:
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_CFOP_MOT_AJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 2 | COD_AJUSTE | VARCHAR2(3) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | Y |  |  |

**PK**: COD_CFOP, COD_AJUSTE, DATA_INI

---

## PRT_CFO_AJUSTES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | IND_AJ_REINF | CHAR(1) | N |  |  |
| 5 | COD_AJ_REINF | VARCHAR2(2) | Y |  |  |
| 6 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, IND_AJ_REINF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_CFO_LINHA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | NUM_LINHA | NUMBER(4) | N |  |  |
| 3 | DAT_VIGENCIA | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: COD_ESTADO, NUM_LINHA, DAT_VIGENCIA, COD_CFO

**FKs**:
- COD_ESTADO, NUM_LINHA, DAT_VIGENCIA → PRT_LINHA_UF_MSAF(COD_ESTADO, NUM_LINHA, DAT_VIGENCIA)

**Indexes**:
- IX_PRT_CFO_LINHA: (COD_ESTADO, NUM_LINHA, DAT_VIGENCIA)

---

## PRT_CFO_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | IND_DESTINACAO | VARCHAR2(2) | Y |  |  |
| 6 | COD_NBM | VARCHAR2(10) | N | ' ' |  |
| 7 | IND_LANCA_NF_ESCRIT | VARCHAR2(1) | Y | 'N' |  |
| 8 | IND_VLR_CONTABIL | CHAR(1) | Y | 'S' |  |
| 9 | IND_VLR_CONTABIL_ICMSS | CHAR(1) | Y | 'N' |  |
| 10 | IND_BASE_TRIBUTADA | CHAR(1) | Y | 'N' |  |
| 11 | IND_BASE_ISENTA | CHAR(1) | Y | 'N' |  |
| 12 | IND_BASE_OUTRAS | CHAR(1) | Y | 'N' |  |
| 13 | IND_BASE_REDUCAO | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_CFO, COD_NBM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

**Indexes**:
- IDX_PRT_CFO_PARAM: (COD_PARAM, COD_CFO, IND_DESTINACAO)

---

## PRT_CFO_UF_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | COD_OBS_LIVRO | VARCHAR2(10) | Y |  |  |
| 6 | IND_VLR_CONF | CHAR(1) | Y |  |  |
| 7 | IND_VLR_CONTABIL | CHAR(1) | Y | 'S' |  |
| 8 | IND_BASE_TRIBUTADA | CHAR(1) | Y | 'N' |  |
| 9 | IND_BASE_ISENTA | CHAR(1) | Y | 'N' |  |
| 10 | IND_BASE_OUTRAS | CHAR(1) | Y | 'N' |  |
| 11 | IND_BASE_REDUCAO | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_PARAM, COD_CFO

---

## PRT_CFO_VAMB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | IND_VLR_CONTAB | CHAR(1) | Y |  |  |
| 5 | IND_TRIB_ICMS | CHAR(1) | Y |  |  |
| 6 | IND_ICMS_BASE1 | CHAR(1) | Y |  |  |
| 7 | IND_ICMS_BASE2 | CHAR(1) | Y |  |  |
| 8 | IND_ICMS_BASE3 | CHAR(1) | Y |  |  |
| 9 | IND_ICMS_BASE4 | CHAR(1) | Y |  |  |
| 10 | IND_TRIB_IPI | CHAR(1) | Y |  |  |
| 11 | IND_IPI_BASE1 | CHAR(1) | Y |  |  |
| 12 | IND_IPI_BASE2 | CHAR(1) | Y |  |  |
| 13 | IND_IPI_BASE3 | CHAR(1) | Y |  |  |
| 14 | IND_IPI_BASE4 | CHAR(1) | Y |  |  |
| 15 | IND_CFO_VENDA_AMB | CHAR(1) | Y | 'N' |  |
| 16 | IND_TP_CFO_VENDA_AMB | CHAR(1) | Y |  | 1 - Resumo; 2 - Emitidas fora de Estabelecimento |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_CIDADE_MSAF_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 5 | COD_CIDADE_OBRIG | VARCHAR2(7) | Y |  |  |

**PK**: VALID_INICIAL, IDENT_ESTADO, COD_MUNICIPIO, COD_MODULO

---

## PRT_CIDADE_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_CIDADE_OBRIG | VARCHAR2(7) | N |  |  |
| 3 | DSC_CIDADE_OBRIG | VARCHAR2(60) | Y |  |  |

**PK**: COD_MODULO, COD_CIDADE_OBRIG

---

## PRT_CLASSE_LINHA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | NUM_LINHA | NUMBER(4) | N |  |  |
| 3 | DAT_VIGENCIA | DATE | N |  |  |
| 4 | COD_CLASSE | VARCHAR2(3) | N |  |  |

**PK**: COD_ESTADO, NUM_LINHA, DAT_VIGENCIA, COD_CLASSE

**FKs**:
- COD_ESTADO, NUM_LINHA, DAT_VIGENCIA → PRT_LINHA_UF_MSAF(COD_ESTADO, NUM_LINHA, DAT_VIGENCIA)
- COD_CLASSE → PRT_CLASSE_MSAF(COD_CLASSE)

---

## PRT_CLASSE_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 2 | DSC_CLASSE | VARCHAR2(100) | Y |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | Y |  |  |

**PK**: COD_CLASSE

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_CLASSE_OPER_PREST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CPO | VARCHAR2(4) | N |  |  |
| 2 | DAT_VALID_INI | DATE | N |  |  |
| 3 | DAT_VALID_FIM | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(70) | Y |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: COD_CPO, DAT_VALID_INI, COD_CFO

---

## PRT_CLASSE_UF_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 3 | DSC_OBRIGACAO | VARCHAR2(60) | Y |  |  |
| 4 | COD_CLASSE_OFICIAL | VARCHAR2(3) | Y |  |  |

**PK**: IDENT_ESTADO, COD_CLASSE

**FKs**:
- COD_CLASSE → PRT_CLASSE_MSAF(COD_CLASSE)

---

## PRT_CLASSE_VENCIMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_CLASSE_VENC | VARCHAR2(5) | N |  |  |
| 3 | DAT_INI_VIGENCIA | DATE | N |  |  |
| 4 | TP_CLASSE | VARCHAR2(100) | Y |  |  |
| 5 | DSC_CLASSE | VARCHAR2(200) | Y |  |  |
| 6 | DSC_DISPOSITIVO | VARCHAR2(100) | Y |  |  |
| 7 | DAT_FIM_VIGENCIA | DATE | Y |  |  |

**PK**: IDENT_ESTADO, COD_CLASSE_VENC, DAT_INI_VIGENCIA

---

## PRT_CLASS_CEST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_ATUALIZACAO | DATE | N |  |  |
| 2 | COD_CEST | VARCHAR2(7) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(800) | N |  |  |

**PK**: DATA_ATUALIZACAO, COD_CEST

---

## PRT_CNAE_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ATIV_CNAE_DESFLO | NUMBER(11) | N |  |  |
| 2 | VALID_CNAE | DATE | N |  |  |
| 3 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |

**PK**: COD_ATIV_CNAE_DESFLO, VALID_CNAE

---

## PRT_CNAE_MSAF_OBRIG
**Comment**: Tabela de parametrizacao Atividade Economica (CNAE) do Mastersaf por CNAE das Obrigacoes.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_ATIVIDADE | NUMBER(7) | N |  | Referente ao COD_ATIVIDADE da tabela ATIV_ECONOMICA (CNAE) |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | IDENT_CNAE_OBRIG | NUMBER(12) | Y |  |  |

**PK**: VALID_INICIAL, COD_ATIVIDADE, COD_MODULO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_CNAE_OBRIG → PRT_CNAE_OBRIG(IDENT_CNAE_OBRIG)

---

## PRT_CNAE_OBRIG
**Comment**: Código de CNAE das Obrigacoes - TFIX119.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CNAE_OBRIG | NUMBER(12) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | COD_CNAE_OBRIG | VARCHAR2(10) | N |  |  |
| 4 | VALID_INI_CNAE_OBRIG | DATE | N |  |  |
| 5 | VALID_FIM_CNAE_OBRIG | DATE | Y |  |  |
| 6 | DSC_CNAE_OBRIG | VARCHAR2(200) | Y |  |  |

**PK**: IDENT_CNAE_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

**Indexes**:
- UK_PRT_CNAE_OBRIG (UNIQUE): (COD_MODULO, COD_CNAE_OBRIG, VALID_INI_CNAE_OBRIG)

---

## PRT_COD_ALIQ_MSAF_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | VLR_ALIQUOTA | NUMBER(7,4) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | COD_ALIQ_OBRIG | VARCHAR2(3) | Y |  |  |

**PK**: VALID_INICIAL, VLR_ALIQUOTA, COD_MODULO

---

## PRT_COD_ALIQ_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_ALIQ_OBRIG | VARCHAR2(3) | N |  |  |
| 3 | DSC_ALIQ_OBRIG | VARCHAR2(60) | Y |  |  |

**PK**: COD_MODULO, COD_ALIQ_OBRIG

---

## PRT_COD_PART_MUN_EFD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | COD_PART_MUN | VARCHAR2(60) | N |  |  |
| 3 | DSC_PART_MUN | VARCHAR2(250) | Y |  |  |
| 4 | COD_TABELA | VARCHAR2(10) | Y |  |  |

**PK**: COD_ESTADO, COD_PART_MUN

---

## PRT_COD_PROD_DMD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PRODUTO_DMD | VARCHAR2(5) | N |  |  |
| 2 | DATA_VALID | DATE | N |  |  |
| 3 | DSC_PRODUTO | VARCHAR2(100) | Y |  |  |
| 4 | COD_MEDIDA | VARCHAR2(6) | Y |  |  |

**PK**: COD_PRODUTO_DMD, DATA_VALID

---

## PRT_COD_TRIB_AM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIB_PROD | VARCHAR2(4) | N |  |  |
| 2 | DSC_TRIB_PROD | VARCHAR2(100) | Y |  |  |

**PK**: COD_TRIB_PROD

---

## PRT_COD_TRIB_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 4 | IDENT_SERV_LEI_116 | NUMBER(12) | N |  |  |
| 5 | COD_TRIBUTACAO_MUNIC | VARCHAR2(12) | N |  |  |
| 6 | DATA_INI | DATE | N |  |  |
| 7 | DATA_FIM | DATE | Y |  |  |

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO, COD_TRIBUTACAO_MUNIC → CAD_TRIBUTACAO_MUNIC(IDENT_ESTADO, COD_MUNICIPIO, COD_TRIBUTACAO_MUNIC)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)

**Indexes**:
- UK_PRT_COD_TRIB_MUNIC (UNIQUE): (IDENT_ESTADO, COD_MUNICIPIO, IDENT_SERVICO, IDENT_SERV_LEI_116, DATA_INI)

---

## PRT_CONTAS_REF_MSAF
**Comment**: Tabela de Parametrizacao do Plano de Contas Referencial para uma lista de parametros especifica por modulo MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 2 | IND_BALANCETE_MENSAL | CHAR(1) | Y |  |  |
| 3 | IND_RES_BALANCETE | CHAR(1) | Y |  |  |
| 4 | IND_TOTALIZADORA | CHAR(1) | Y |  |  |

**PK**: IDENT_CONTA_REF

**FKs**:
- IDENT_CONTA_REF → SPED_CONTAS_REF(IDENT_CONTA_REF)

---

## PRT_CONTA_LANCTO_DESIF
**Comment**: Tabela de Parametrizacao do Plano de Contas Empresa x Partidas dos Lancamentos DESIF.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 3 | VALID_INI | DATE | N |  |  |
| 4 | VALID_FIM | DATE | Y |  |  |
| 5 | IND_MODULO1 | VARCHAR2(1) | Y |  |  |
| 6 | IND_MODULO4 | VARCHAR2(1) | Y |  |  |

**PK**: GRUPO_CONTA, COD_CONTA, VALID_INI

---

## PRT_CONTA_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_CONTA_PSERV_DESIF
**Comment**: Tabela de Parametrizacao do Plano de Contas Empresa x Produtos e Servicos DESIF.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 3 | VALID_INI | DATE | N |  |  |
| 4 | VALID_FIM | DATE | Y |  |  |
| 5 | COD_PSERV_DESIF | VARCHAR2(4) | N |  |  |
| 6 | DSC_COMPL | VARCHAR2(250) | Y |  |  |

**PK**: GRUPO_CONTA, COD_CONTA, VALID_INI

**FKs**:
- COD_PSERV_DESIF → CAD_PSERV_DESIF(COD_PSERV_DESIF)

---

## PRT_CONTA_TARIFA_DESIF
**Comment**: Tabela de Parametrizacao do Plano de Contas Empresa x Tarifas Bancarias DESIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 3 | VALID_INI | DATE | N |  |  |
| 4 | VALID_FIM | DATE | Y |  |  |
| 5 | COD_TARIFA_DESIF | VARCHAR2(4) | N |  |  |
| 6 | VLR_UNIT_TARIFA | NUMBER(8,2) | Y |  |  |
| 7 | VLR_PERCENT_TARIFA | NUMBER(5,2) | Y |  |  |

**PK**: GRUPO_CONTA, COD_CONTA, VALID_INI

**FKs**:
- COD_TARIFA_DESIF → CAD_TARIFA_DESIF(COD_TARIFA_DESIF)

---

## PRT_CPROC_FILE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PREFIXO | VARCHAR2(60) | N |  |  |
| 2 | NOME_PACKAGE | VARCHAR2(60) | N |  |  |

**PK**: PREFIXO

---

## PRT_CTL_COMMIT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | NUM_OPERACAO | NUMBER(15) | N |  |  |

**PK**: NUM_PROCESSO, NUM_OPERACAO

---

## PRT_DACON_EMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_PROPORCIONA | CHAR(1) | Y | 'N' |  |
| 3 | REGIME | VARCHAR2(1) | Y |  |  |
| 4 | IND_ALIQS_DIFERENCIADAS | VARCHAR2(1) | Y |  |  |
| 5 | IND_ALIQS_POR_UNIDADE | VARCHAR2(1) | Y |  |  |
| 6 | IND_FICHA_LINHA_SEM_REGRA | VARCHAR2(1) | Y | 'N' | Indicador para processamento de ficha/linha sem regra associada ( zerada ) |
| 7 | QUALIFICACAO | VARCHAR2(2) | Y |  |  |
| 8 | TIPO_ENTIDADE | VARCHAR2(2) | Y |  |  |
| 9 | INCLUSAO_SIMPLES | VARCHAR2(2) | Y |  |  |
| 10 | DATA_INCLUSAO | DATE | Y |  |  |
| 11 | APUR_CRED_OPER_IMP | VARCHAR2(1) | Y |  |  |
| 12 | IND_ALIQS_DIFERENCIADAS_ST | VARCHAR2(1) | Y |  |  |
| 13 | IND_ALIQS_POR_UNIDADE_ST | VARCHAR2(1) | Y |  |  |
| 14 | ADICAO_CONTRIB | VARCHAR2(1) | Y |  |  |
| 15 | DIFERIMENTO_CONTRIB | VARCHAR2(1) | Y |  |  |
| 16 | CRED_TRANSF_MES | VARCHAR2(1) | Y |  |  |
| 17 | CONTRIB_CRED_DIFERIDO_TRANSF | VARCHAR2(1) | Y |  |  |
| 18 | DESCONTO_CRED_TRANSF_PJ | VARCHAR2(1) | Y |  |  |
| 19 | METODO_DETERMINADO_CRED | VARCHAR2(1) | Y |  |  |
| 20 | NATUREZA_JURIDICA | NUMBER(4) | Y |  |  |
| 21 | SITUACAO_ESPECIAL | VARCHAR2(2) | Y |  |  |
| 22 | DATA_EVENTO | DATE | Y |  |  |
| 23 | DESENQUADRAMENTO | NUMBER(1) | Y |  |  |
| 24 | DATA_DESENQUADRAMENTO | DATE | Y |  |  |
| 25 | TP_LOGRADOURO | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA

---

## PRT_DARF_ESOCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_DARF | VARCHAR2(9) | N |  |  |
| 4 | COD_DARF | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_DARF, COD_DARF

---

## PRT_DATAMART_AUTOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_AUTOMATICO | CHAR(1) | Y |  |  |
| 4 | IND_FECEP | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_DATA_FISCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_DDSNATAL_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 2 | COD_DOCTO_DDS | VARCHAR2(2) | N |  |  |
| 3 | VALID_DOCTO | DATE | N |  |  |

**PK**: COD_DOCTO, VALID_DOCTO

---

## PRT_DESCUIABA_MODELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 2 | VALID_MODELO | DATE | N |  |  |
| 3 | COD_MODELO_DES | VARCHAR2(2) | N |  |  |

**PK**: COD_MODELO, VALID_MODELO

---

## PRT_DIRETORIOS_IRPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TABELA | VARCHAR2(10) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(40) | N |  |  |
| 5 | DIRECTORY_NAME | VARCHAR2(30) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TABELA

**FKs**:
- COD_MODULO, DIRECTORY_NAME → PRT_DIRETORIOS_SERVIDOR(COD_MODULO, DIRECTORY_NAME)

---

## PRT_DIRETORIOS_SERVIDOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(40) | N |  |  |
| 2 | DIRECTORY_NAME | VARCHAR2(30) | N |  |  |
| 3 | DIRECTORY_PATH | VARCHAR2(4000) | N |  |  |

**PK**: COD_MODULO, DIRECTORY_NAME

---

## PRT_EXTCFO_AJUSTES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | IND_AJ_REINF | CHAR(1) | N |  |  |
| 7 | COD_AJ_REINF | VARCHAR2(2) | Y |  |  |
| 8 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 9 | COD_RECEITA | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, IND_AJ_REINF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_EXTCFO_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 7 | IND_DESTINACAO | VARCHAR2(2) | Y |  |  |
| 8 | COD_NBM | VARCHAR2(10) | N | ' ' |  |
| 9 | IND_LANCA_NF_ESCRIT | VARCHAR2(1) | Y | 'N' |  |
| 10 | IND_VLR_CONTABIL | CHAR(1) | Y | 'S' |  |
| 11 | IND_VLR_CONTABIL_ICMSS | CHAR(1) | Y | 'N' |  |
| 12 | IND_BASE_TRIBUTADA | CHAR(1) | Y | 'N' |  |
| 13 | IND_BASE_ISENTA | CHAR(1) | Y | 'N' |  |
| 14 | IND_BASE_OUTRAS | CHAR(1) | Y | 'N' |  |
| 15 | IND_BASE_REDUCAO | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, COD_NBM

**FKs**:
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_EXTCFO_UF_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 7 | COD_OBS_LIVRO | VARCHAR2(10) | Y |  |  |
| 8 | IND_VLR_CONF | CHAR(1) | Y |  |  |
| 9 | IND_VLR_CONTABIL | CHAR(1) | Y | 'S' |  |
| 10 | IND_BASE_TRIBUTADA | CHAR(1) | Y | 'N' |  |
| 11 | IND_BASE_ISENTA | CHAR(1) | Y | 'N' |  |
| 12 | IND_BASE_OUTRAS | CHAR(1) | Y | 'N' |  |
| 13 | IND_BASE_REDUCAO | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_PARAM, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## PRT_EXTCFO_VAMB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | IND_VLR_CONTAB | CHAR(1) | Y |  |  |
| 7 | IND_TRIB_ICMS | CHAR(1) | Y |  |  |
| 8 | IND_ICMS_BASE1 | CHAR(1) | Y |  |  |
| 9 | IND_ICMS_BASE2 | CHAR(1) | Y |  |  |
| 10 | IND_ICMS_BASE3 | CHAR(1) | Y |  |  |
| 11 | IND_ICMS_BASE4 | CHAR(1) | Y |  |  |
| 12 | IND_TRIB_IPI | CHAR(1) | Y |  |  |
| 13 | IND_IPI_BASE1 | CHAR(1) | Y |  |  |
| 14 | IND_IPI_BASE2 | CHAR(1) | Y |  |  |
| 15 | IND_IPI_BASE3 | CHAR(1) | Y |  |  |
| 16 | IND_IPI_BASE4 | CHAR(1) | Y |  |  |
| 17 | IND_EXTCFO_VENDA_AMB | CHAR(1) | Y | 'N' |  |
| 18 | IND_TP_EXTCFO_VENDA_AMB | CHAR(1) | Y |  | 1 - Resumo; 2 - Emitidas fora de Estabelecimento |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_FECHA_GRP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRUPO | NUMBER(5) | N |  |  |
| 4 | DT_FECHAMENTO | DATE | Y |  |  |
| 5 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRUPO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_GRUPO → BRT_GRUPO(COD_GRUPO)

---

## PRT_FECHA_GRP_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_GRUPO | NUMBER(5) | Y |  |  |
| 4 | DT_OPERACAO | DATE | Y |  |  |
| 5 | DT_FECHAMENTO | DATE | Y |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_PRT_FEC_GRP_HST: (COD_EMPRESA, COD_ESTAB, COD_GRUPO, DT_OPERACAO)

---

## PRT_FTP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_FTP | VARCHAR2(20) | N |  |  |
| 2 | USUARIO | VARCHAR2(40) | N |  |  |
| 3 | DAT_ENVIO_FTP | DATE | Y |  |  |
| 4 | IND_ENVIO | VARCHAR2(10) | Y |  | OK - sucesso no envio de dados; ERRO - tentou enviar, mas ocorreu erro durante o processo; NENVIAR - optou por nao enviar, so recebera mensagem de envio dentro de 4 meses |

**PK**: COD_FTP, USUARIO

---

## PRT_GISS_CTBA_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 2 | COD_DOCTO_GISS | VARCHAR2(1) | Y |  |  |
| 3 | VALID_DOCTO | DATE | N |  |  |

**PK**: COD_DOCTO, VALID_DOCTO

---

## PRT_GISS_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | IND_PONTUACAO | CHAR(1) | Y |  | Indicador para formatação do campo COD_SERV_LEI_116 com  ponto para separar casas decimais |
| 5 | IND_ZEROS_ESQUERDA | CHAR(1) | Y |  | Indicador para formatação do campo COD_SERV_LEI_116 com zeros à esquerda para complementar 4 dígitos |
| 6 | IND_DESC_NFE_SAIDA | CHAR(1) | Y |  | Indicador para descartar notas fiscais eletrônica de saída |
| 7 | IND_DESC_NFE_ENTRADA | CHAR(1) | Y |  | Indicador para descartar notas fiscais eletrônica de entrada |
| 8 | IND_ZEROS_APOS | CHAR(1) | Y |  |  |
| 9 | IND_ZEROS_DIREITA | CHAR(1) | Y |  |  |
| 10 | IND_TIPO_ARQUIVO | CHAR(1) | Y |  | T para arquivo TXT. D para arquivo DAT. |
| 11 | IND_TIPO_COD_SERV | CHAR(1) | Y | '1' |  |
| 12 | IND_ZEROS_ESQUERDA_SEIS_DIG | CHAR(1) | Y | '0' | Indicador para formatação do campo COD_SERV_LEI_116 com zeros à esquerda para complementar 6 dígitos |
| 13 | IND_COD_ESTAB_ARQ | CHAR(1) | Y | 'N' |  |
| 14 | IND_ZERO_ESQUERDA_NF | CHAR(1) | Y |  |  |
| 15 | IND_ZERO_DIREITA_NF | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## PRT_GRUPO_LIVRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO | NUMBER(5) | N |  |  |
| 2 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |

**PK**: COD_GRUPO, COD_TIPO_LIVRO

**FKs**:
- COD_GRUPO → BRT_GRUPO(COD_GRUPO)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## PRT_GRUPO_TAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO | NUMBER(5) | N |  |  |
| 2 | NOME_TABELA | VARCHAR2(30) | N |  |  |

**PK**: COD_GRUPO, NOME_TABELA

**FKs**:
- COD_GRUPO, NOME_TABELA → BRT_GRUPO_TAB(COD_GRUPO, NOME_TABELA_BANCO)

---

## PRT_IDENTIFICA_NAT_REND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NAT_REND | VARCHAR2(9) | Y |  |  |
| 2 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 3 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 5 | COD_SERVICO_NAT_REND | VARCHAR2(10) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**Indexes**:
- UK_PRT_IDENTIFICA_NAT_REND (UNIQUE): (COD_NAT_REND, IND_FIS_JUR, COD_FIS_JUR, COD_RECEITA, COD_SERVICO_NAT_REND)

---

## PRT_IDENT_DMART

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NOME_TABELA | VARCHAR2(40) | N |  |  |
| 4 | IDENT_TABELA | NUMBER(12) | Y |  |  |
| 5 | IND_UTILIZACAO | CHAR(1) | Y |  |  |
| 6 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NOME_TABELA

---

## PRT_IDENT_DMART_PERIODO
**Comment**: Tabela para controle de concorrencia por período na equalização. ( OS2141 )

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NOME_TABELA | VARCHAR2(40) | N |  |  |
| 4 | DATA_INI | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NOME_TABELA, DATA_INI, DATA_FIM

---

## PRT_IDENT_ESTAB_SCP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TIPO_SCP | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_ID_APOS_ESP_ESOCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 4 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 5 | IND_APOSENT_ESP | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_SERVICO, COD_SERVICO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_ID_TIPO_SERV_ESOCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_SERV_ESOCIAL | VARCHAR2(9) | N |  |  |
| 4 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 5 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 6 | IND_APOSENT_ESP | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_SERVICO, COD_SERVICO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_ID_TIPO_SERV_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_SERV_ESOCIAL | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_INCID_TRIBUT_ESOCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_INCID_TRIB | VARCHAR2(1) | N |  |  |
| 2 | COD_INCID_TRIB | VARCHAR2(4) | N |  |  |
| 3 | DSC_INCID_TRIB | VARCHAR2(150) | Y |  |  |

**PK**: TIPO_INCID_TRIB, COD_INCID_TRIB

---

## PRT_IND_PROD_MSAF
**Comment**: Tabela de Parametrização de Indicador de Produto para algum Cod. Paramêtro MasterSAF definido da TFIX31.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  | Indicador de Produto da SAFX2013 |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, IND_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_INSTALACAO_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INSTALACAO | VARCHAR2(7) | N |  |  |
| 2 | VALID_INICIAL | DATE | N |  |  |
| 3 | DSC_TP_INSTALACAO | VARCHAR2(200) | Y |  |  |
| 4 | VALID_FINAL | DATE | Y |  |  |

**PK**: COD_INSTALACAO, VALID_INICIAL

---

## PRT_INTEGRA_IRPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TAB_ARQ | CHAR(1) | Y |  | (A)rquivo - (T)abela |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_JUROS_MULTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INDICE_SELIC | VARCHAR2(10) | Y |  |  |
| 2 | PERC_MULT_D_DARF | NUMBER(7,4) | Y |  |  |
| 3 | PERC_LIM_DARF | NUMBER(7,4) | Y |  |  |
| 4 | PC_INSS_MES_1_SGFIP | NUMBER(7,4) | Y |  |  |
| 5 | PC_INSS_MES_2_SGFIP | NUMBER(7,4) | Y |  |  |
| 6 | PC_INSS_MES_3_SGFIP | NUMBER(7,4) | Y |  |  |
| 7 | PC_INSS_MES_1_CGFIP | NUMBER(7,4) | Y |  |  |
| 8 | PC_INSS_MES_2_CGFIP | NUMBER(7,4) | Y |  |  |
| 9 | PC_INSS_MES_3_CGFIP | NUMBER(7,4) | Y |  |  |
| 10 | COD_PAGTO_INSS | VARCHAR2(4) | Y |  | Código de pagto. de INSS para tratamento de desporto e contratos de patrocínio |
| 11 | IND_REGRA_PAR_INSS | CHAR(1) | Y | 'P' | Indicador da forma de parametrização a ser utilizada na geração das retenções de INSS |
| 12 | IND_CONS_EMPRESA | CHAR(1) | Y | 'N' | Indicador de consolidação das retenções de INSS por Empresa, caso seja escolhida esta opção a GPS será gerada em nome da Matriz |
| 13 | DIA_LIMITE_RECEB | NUMBER(2) | Y | 10 | Dia limite para consideracao dos DF nas retencoes e consolidacoes de INSS |
| 14 | IND_RET_COOPER | CHAR(1) | Y | 'N' | Indicador se as retenções de cooperativas serão consideradas como estabelecimento avulso nas consolidações |
| 15 | IND_CALC_MULTAS_GPS | CHAR(1) | Y | '2' |  |
| 16 | PERC_MULT_D_GPS_1 | NUMBER(7,4) | Y |  |  |
| 17 | PERC_MULT_D_GPS_2 | NUMBER(7,4) | Y |  |  |
| 18 | PERC_LIM_GPS_1 | NUMBER(7,4) | Y |  |  |
| 19 | PERC_LIM_GPS_2 | NUMBER(7,4) | Y |  |  |
| 20 | IND_GERACAO_DARF | CHAR(1) | Y | '0' |  |
| 21 | VLR_MIN_DARF | NUMBER(17,2) | Y |  |  |
| 22 | IND_ESTORNO_DT_RET | CHAR(1) | Y | 'N' |  |

**FKs**:
- COD_INDICE_SELIC → Y2046_INDICE(COD_INDICE)
- COD_PAGTO_INSS → IRT_COD_PG_INSS(COD_PAGTO)

---

## PRT_LANCTO_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | NUM_LANCTO | VARCHAR2(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, NUM_LANCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_LEVEL_LOG_SES_PSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_ID | DATE | N |  |  |
| 2 | LOG_LEVEL | VARCHAR2(10) | Y |  | Contem o indicador dos niveis de log que deverao ser catalogados no DATADOG. Os valores possiveis sao: OFF, FATAL, ERROR, WARN, INFO, DEBUG, ALL. Os niveis pela ordem sao: OFF    (10) FATAL  (20) ERROR  (30) WARN   (40) INFO   (50) DEBUG  (60) ALL    (70) |
| 3 | SESSION_ID | NUMBER | Y |  |  |
| 4 | PSP_ID | VARCHAR2(30) | Y |  |  |
| 5 | VALIDADE_EM_MIN | NUMBER | Y |  |  |

**Indexes**:
- UK_PRT_LEVEL_LOG_SES_PSP (UNIQUE): (DATA_ID, SESSION_ID, PSP_ID)

---

## PRT_LINHA_UF_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | NUM_LINHA | NUMBER(4) | N |  |  |
| 3 | DAT_VIGENCIA | DATE | N |  |  |
| 4 | DSC_LINHA | VARCHAR2(90) | Y |  |  |
| 5 | IND_TP_PAR | CHAR(1) | Y |  |  |
| 6 | IND_VALOR | CHAR(1) | Y |  |  |

**PK**: COD_ESTADO, NUM_LINHA, DAT_VIGENCIA

---

## PRT_LIVRO_AUX_SUBCONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT_ECD | VARCHAR2(3) | N |  |  |
| 2 | COD_ITEM | VARCHAR2(3) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 4 | IND_FORMATO | CHAR(1) | Y |  |  |

**PK**: COD_LAYOUT_ECD, COD_ITEM

---

## PRT_LOCAL_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_LOCAL | VARCHAR2(6) | N |  |  |
| 3 | DSC_LOCAL | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_LOCAL

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## PRT_METODO_AFERICAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_METODO | VARCHAR2(3) | N |  |  |
| 2 | DATA_INI_VALID | DATE | N |  |  |
| 3 | DATA_FIM_VALID | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_METODO, DATA_INI_VALID

---

## PRT_MODELO_MSAF_OBRIG
**Comment**: Tabela de parametrizacao dos codigos de modelos MasterSAF (x2024_modelo_docto) por codigos das series especificas de obrigacoes (PRT_SERIE_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 5 | COD_SERIE_OBRIG | VARCHAR2(10) | Y |  |  |

**PK**: VALID_INICIAL, GRUPO_MODELO, COD_MODELO, COD_MODULO

**FKs**:
- COD_MODULO, COD_SERIE_OBRIG → PRT_SERIE_OBRIG(COD_MODULO, COD_SERIE_OBRIG)

---

## PRT_MODELO_MUNIC_MSAF_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 7 | COD_SERIE_OBRIG | VARCHAR2(10) | Y |  |  |

**PK**: VALID_INICIAL, COD_MODULO, GRUPO_MODELO, COD_MODELO, IDENT_ESTADO, COD_MUNICIPIO

---

## PRT_MODELO_TERMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODELO | VARCHAR2(5) | N |  |  |
| 2 | NUM_LINHA_DW | NUMBER(4) | N |  |  |
| 3 | DESC_LINHA_DW | VARCHAR2(2000) | Y |  |  |

**PK**: COD_MODELO, NUM_LINHA_DW

**FKs**:
- COD_MODELO → EFT_MODELO_NF(COD_MODELO)

---

## PRT_MODULOS_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | DSC_MODULO | VARCHAR2(30) | Y |  |  |

**PK**: COD_MODULO

---

## PRT_MODULOS_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNIC | NUMBER(7) | N |  |  |
| 4 | IND_SERV | CHAR(1) | N |  | Indica se o municipio/uf utilizara a lei 116 ou ira usar a parametrização de serviços |

**PK**: IDENT_ESTADO, COD_MUNIC

---

## PRT_MODULO_ESTADUAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | COD_GERACAO | VARCHAR2(30) | N |  |  |
| 4 | IND_PAR_CFOP_SAI | CHAR(1) | Y |  |  |
| 5 | IND_PAR_NAT_SAI | CHAR(1) | Y |  |  |
| 6 | IND_PAR_CFOP_ENT | CHAR(1) | Y |  |  |
| 7 | IND_PAR_NAT_ENT | CHAR(1) | Y |  |  |
| 8 | IND_PAR_CFOP_REC | CHAR(1) | Y |  |  |
| 9 | IND_PAR_NAT_REC | CHAR(1) | Y |  |  |
| 10 | IND_PAR_PROD | CHAR(1) | Y |  |  |
| 11 | IND_PAR_NCM | CHAR(1) | Y |  |  |
| 12 | IND_PAR_LANC | CHAR(1) | Y |  |  |
| 13 | IND_GER_C176 | CHAR(1) | Y |  |  |
| 14 | IND_GER_UTIL | CHAR(1) | Y |  |  |
| 15 | IND_REL_ANEXO1 | CHAR(1) | Y |  |  |
| 16 | IND_REL_ANEXO2 | CHAR(1) | Y |  |  |
| 17 | IND_REL_ANEXO3 | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MODULO, COD_GERACAO

---

## PRT_MOTIVO_AJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_AJUSTE | VARCHAR2(3) | N |  |  |
| 2 | DATA_INI | DATE | N |  |  |
| 3 | DESC_AJUSTE | VARCHAR2(100) | Y |  |  |
| 4 | REC_MOTIVO | CHAR(1) | Y |  |  |
| 5 | DATA_FIM | DATE | Y |  |  |

**PK**: COD_AJUSTE, DATA_INI

---

## PRT_MSAF_LOGO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | LOGOTIPO | BLOB | Y |  |  |
| 4 | EXTENSAO | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_MUNIC_OBRIG_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | VALID_INICIAL | DATE | N |  |  |
| 3 | COD_UF_MSAF | VARCHAR2(2) | N |  |  |
| 4 | COD_MUNIC_MSAF | NUMBER(5) | N |  |  |
| 5 | COD_UF_OBRIG | VARCHAR2(2) | Y |  |  |
| 6 | COD_MUNIC_OBRIG | NUMBER(6) | Y |  |  |
| 7 | DSC_MUNIC_OBRIG | VARCHAR2(50) | Y |  |  |

**PK**: COD_MODULO, VALID_INICIAL, COD_UF_MSAF, COD_MUNIC_MSAF

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_MUNIC_SIAFI
**Comment**: Tabela para armazenar o relacionamento entre os codigos dos Municipios MSAF (IBGE) com os do SIAFI.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_MSAF | NUMBER(5) | N |  |  |
| 2 | COD_UF_MSAF | VARCHAR2(2) | N |  |  |
| 3 | VALID_INICIAL | DATE | N |  |  |
| 4 | COD_MUNIC_SIAFI | VARCHAR2(5) | Y |  |  |
| 5 | COD_UF_SIAFI | VARCHAR2(2) | Y |  |  |

**PK**: COD_MUNIC_MSAF, COD_UF_MSAF, VALID_INICIAL

**FKs**:
- COD_MUNIC_SIAFI, COD_UF_SIAFI → MUNICIPIO_SIAFI(COD_MUNIC_SIAFI, COD_UF_SIAFI)

---

## PRT_MUN_DEFINICAO_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | IND_NF_DENTRO_MUN_TOMAD | VARCHAR2(1) | Y |  | indica se a geração irá considerar notas fiscais dentro do município para tomadores de serviço |
| 4 | IND_NF_FORA_MUN_TOMAD | VARCHAR2(1) | Y |  | indica se a geração irá considerar notas fiscais fora do município para tomadores de serviço |
| 5 | IND_NF_DENTRO_MUN_PREST | VARCHAR2(1) | Y |  | indica se a geração irá considerar notas fiscais dentro do município para prestadores de serviço |
| 6 | IND_NF_FORA_MUN_PREST | VARCHAR2(1) | Y |  | indica se a geração irá considerar notas fiscais fora do município para prestadores de serviço |

**PK**: IDENT_ESTADO, COD_MUNICIPIO

---

## PRT_MVA_CEST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CEST | VARCHAR2(7) | N |  |  |
| 2 | VLR_MVA | NUMBER(17,2) | Y |  |  |
| 3 | DATA_INICIO_VALID | DATE | N |  |  |

**PK**: COD_CEST, DATA_INICIO_VALID

---

## PRT_NAT_OP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NAT_OP | VARCHAR2(5) | N |  |  |
| 2 | NUM_ORDEM | NUMBER(3) | N |  |  |
| 3 | DSC_CONTA | VARCHAR2(50) | Y |  |  |
| 4 | DSC_NAT_OP | VARCHAR2(255) | Y |  |  |

**PK**: COD_NAT_OP, NUM_ORDEM

---

## PRT_NAT_RUBRICA_ESOCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NAT_RUBRICA | VARCHAR2(4) | N |  |  |
| 2 | DSC_NAT_RUBRICA | VARCHAR2(100) | Y |  |  |

**PK**: COD_NAT_RUBRICA

---

## PRT_NBM_ATIV_CONT_PREV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_NBM | VARCHAR2(10) | N |  |  |
| 4 | COD_ATIV_CONT_PREV | VARCHAR2(8) | N |  |  |
| 5 | COD_RECEITA | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_NBM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_NBM_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_NBM | VARCHAR2(10) | N |  |  |
| 5 | IND_RED_BASE | CHAR(1) | Y |  |  |
| 6 | VLR_ALIQ_RED | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_NBM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

**Indexes**:
- IDX_PRT_NBM_PARAM: (COD_PARAM, COD_NBM)

---

## PRT_NBM_VIGENCIA_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_NBM | VARCHAR2(10) | N |  |  |
| 5 | DATA_VIGENCIA_INI | DATE | N |  |  |
| 6 | DATA_VIGENCIA_FIM | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_NBM, DATA_VIGENCIA_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_NFTS_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TIPO_COD_SERV | CHAR(1) | Y | '1' |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_NOTA_C_S_RETENCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_VALIDADOR | VARCHAR2(20) | N |  |  |
| 3 | IND_RETENCAO | VARCHAR2(1) | N |  |  |
| 4 | IND_NOTA_DEST | VARCHAR2(1) | Y | 'N' | Indicador de nota de destino |

**PK**: COD_EMPRESA, COD_VALIDADOR

**Indexes**:
- IX_PRT_NOTA_C_S_RETENCAO: (COD_VALIDADOR, COD_EMPRESA)

---

## PRT_NUM_DOCFIS_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INICIO | DATE | Y |  |  |
| 4 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_OBS_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | DAT_MOVTO | DATE | N |  |  |
| 5 | OBS | VARCHAR2(255) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, DAT_MOVTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_OPER_ESTAB_OBRIG
**Comment**: Tabela de mapeamento de codigos de operaÃ§Ãµes MasterSAF (x2001_operacao) por codigos de operaÃ§oes especificos de obrigacoes (PRT_OPER_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VALID_INICIAL | DATE | N |  |  |
| 4 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 5 | COD_OPERACAO | VARCHAR2(6) | N |  |  |
| 6 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 7 | IDENT_OPER_OBRIG | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, VALID_INICIAL, GRUPO_OPERACAO, COD_OPERACAO, COD_MODULO, IDENT_OPER_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_OPER_OBRIG → PRT_OPER_OBRIG(IDENT_OPER_OBRIG)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_OPER_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 5 | COD_OPERACAO | VARCHAR2(9) | N |  |  |
| 6 | NUM_CAMPO_REG0 | NUMBER(2) | Y |  |  |
| 7 | IND_TIPO_MOV | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, GRUPO_OPERACAO, COD_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_OPER_MSAF_OBRIG
**Comment**: Tabela de mapeamento de c¢digos de operações MasterSAF (x2001_operacao) por codigos de operaçoes especificos de obrigacoes (PRT_OPER_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 3 | COD_OPERACAO | VARCHAR2(6) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 5 | IDENT_OPER_OBRIG | NUMBER(12) | N |  |  |

**PK**: VALID_INICIAL, GRUPO_OPERACAO, COD_OPERACAO, COD_MODULO, IDENT_OPER_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_OPER_OBRIG → PRT_OPER_OBRIG(IDENT_OPER_OBRIG)

---

## PRT_OPER_OBRIG
**Comment**: Código de Operações das Obrigacoes - TFIX116

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_OPER_OBRIG | NUMBER(12) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | COD_OPER_OBRIG | VARCHAR2(10) | N |  |  |
| 4 | VALID_INI_OPER_OBRIG | DATE | N |  |  |
| 5 | VALID_FIM_OPER_OBRIG | DATE | Y |  |  |
| 6 | DSC_OPER_OBRIG | VARCHAR2(100) | Y |  |  |
| 7 | IND_TIPO_OPER | CHAR(1) | Y |  |  |
| 8 | IND_REGULAR | CHAR(1) | Y |  |  |

**PK**: IDENT_OPER_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

**Indexes**:
- UK_PRT_OPER_OBRIG (UNIQUE): (COD_MODULO, COD_OPER_OBRIG, VALID_INI_OPER_OBRIG)

---

## PRT_OPER_OBRIG_CFO
**Comment**: Tabela de mapeamento dos c¢digos CFOP (x2012_cod_fiscal) por codigos de operaçoes especificos de obrigacoes (PRT_OPER_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | IDENT_OPER_OBRIG | NUMBER(12) | N |  |  |
| 5 | IND_DESTINACAO | CHAR(1) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: VALID_INICIAL, COD_CFO, COD_MODULO, IDENT_OPER_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_OPER_OBRIG → PRT_OPER_OBRIG(IDENT_OPER_OBRIG)

---

## PRT_OPER_OBRIG_EXTCFO
**Comment**: Tabela de mapeamento dos c¢digos Extensao CFOP (x2081_extensao_cfo) por codigos de operaçoes especificos de obrigacoes (PRT_OPER_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |
| 3 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 4 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 5 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 6 | IDENT_OPER_OBRIG | NUMBER(12) | N |  |  |
| 7 | IND_DESTINACAO | CHAR(1) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: VALID_INICIAL, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, COD_MODULO, IDENT_OPER_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_OPER_OBRIG → PRT_OPER_OBRIG(IDENT_OPER_OBRIG)

---

## PRT_OPER_OBRIG_GRPCONT
**Comment**: Tabela de mapeamento dos Grupos de Contagem do Inventário (x52_invent_produto) por codigos de operaçoes especificos de obrigacoes (PRT_OPER_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | IDENT_OPER_OBRIG | NUMBER(12) | Y |  |  |

**PK**: VALID_INICIAL, GRUPO_CONTAGEM, COD_MODULO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_OPER_OBRIG → PRT_OPER_OBRIG(IDENT_OPER_OBRIG)

---

## PRT_OPER_OBRIG_TOT
**Comment**: Tabela de definição dos codigos totalizadores de operaçoes especificos de obrigacoes (PRT_OPER_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | IDENT_OPER_OBRIG | NUMBER(12) | N |  |  |
| 3 | IDENT_OPER_OBRIG_TOT | NUMBER(12) | N |  |  |

**PK**: VALID_INICIAL, IDENT_OPER_OBRIG, IDENT_OPER_OBRIG_TOT

**FKs**:
- IDENT_OPER_OBRIG_TOT → PRT_OPER_OBRIG(IDENT_OPER_OBRIG)
- IDENT_OPER_OBRIG → PRT_OPER_OBRIG(IDENT_OPER_OBRIG)

---

## PRT_PAIS_MSAF_OBRIG
**Comment**: Tabela de parametrizacao dos Códigos de Países do Mastersaf por Códigos de Países das Obrigacoes.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_PAIS | VARCHAR2(3) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | IDENT_PAIS_OBRIG | NUMBER(12) | Y |  |  |

**PK**: VALID_INICIAL, COD_PAIS, COD_MODULO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- COD_PAIS → PAIS(COD_PAIS)
- IDENT_PAIS_OBRIG → PRT_PAIS_OBRIG(IDENT_PAIS_OBRIG)

---

## PRT_PAIS_OBRIG
**Comment**: Tabela de Códigos de Países das Obrigacoes - TFIX120

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAIS_OBRIG | NUMBER(12) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | COD_PAIS_OBRIG | VARCHAR2(10) | N |  |  |
| 4 | VALID_INI_PAIS_OBRIG | DATE | N |  |  |
| 5 | VALID_FIM_PAIS_OBRIG | DATE | Y |  |  |
| 6 | DSC_PAIS_OBRIG | VARCHAR2(60) | Y |  |  |

**PK**: IDENT_PAIS_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

**Indexes**:
- UK_PRT_PAIS_OBRIG (UNIQUE): (COD_MODULO, COD_PAIS_OBRIG, VALID_INI_PAIS_OBRIG)

---

## PRT_PAR2_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PARAM | NUMBER(3) | N |  |  |
| 2 | DSC_PARAM | VARCHAR2(100) | Y |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | Y |  |  |
| 4 | IND_CFOP_NAT | CHAR(1) | Y |  |  |
| 5 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 6 | IND_NCM | CHAR(1) | Y |  |  |
| 7 | IND_SERVICO | CHAR(1) | Y |  |  |
| 8 | IND_OPERACAO | CHAR(1) | Y |  |  |
| 9 | IND_CONTA | CHAR(1) | Y |  |  |
| 10 | IND_TRIB_INT | CHAR(1) | Y |  |  |
| 11 | IND_PFJ | CHAR(1) | Y |  |  |
| 12 | IND_PFJ_ATIVIDADE | CHAR(1) | Y |  |  |
| 13 | IND_ESTADO | CHAR(1) | Y |  |  |
| 14 | IND_CLASSE_BALANCO | CHAR(1) | Y |  |  |
| 15 | IND_IND_PRODUTO | CHAR(1) | Y |  | Indica parâmetro usando na PRT_IND_PRODUTO_MSAF. |

**PK**: COD_PARAM

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_PAR3_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_BASE_DIF_ALIQ | CHAR(1) | Y |  |  |
| 4 | IND_GRAVA_HIST_NF | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_PAR4_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_CONTROLE_SENHA | VARCHAR2(1) | Y |  |  |
| 2 | VALID_SENHA | NUMBER(5) | Y |  |  |
| 3 | IND_REUTILIZA_SENHA | VARCHAR2(1) | Y |  |  |
| 4 | REUTILIZA_SENHA | NUMBER(5) | Y |  |  |
| 5 | IND_TIME_OUT | VARCHAR2(1) | Y |  |  |
| 6 | TIME_OUT | NUMBER(5) | Y |  |  |
| 7 | IND_SENHA_FORTE | CHAR(1) | Y | 'N' |  |
| 8 | IND_BLOQ_SENHA | CHAR(1) | Y | 'S' |  |
| 9 | DIAS_INATIVIDADE | NUMBER(5) | Y | 90 |  |
| 10 | IND_MIN_SENHA | CHAR(1) | Y | 'S' |  |
| 11 | NUM_MIN_SENHA | NUMBER(3) | Y | 6 |  |
| 12 | IND_N_ERRO_LOGIN | CHAR(1) | Y | 'S' |  |
| 13 | NUM_ERRO_LOGIN | NUMBER(3) | Y | 5 |  |
| 14 | IND_SENHA_DERIVADA | CHAR(1) | Y | 'N' |  |
| 15 | IND_SENHA_SEQUENCIA | CHAR(1) | Y | 'N' |  |
| 16 | IND_SENHA_PARAMETRIZADA | CHAR(1) | Y | 'N' |  |
| 17 | IND_BLOQ_ACESSO | CHAR(1) | Y | 'N' |  |

---

## PRT_PAR4_PASSWORD_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PALAVRA_SENHA | VARCHAR2(20) | N |  |  |

**PK**: PALAVRA_SENHA

---

## PRT_PAR_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_BANCO | VARCHAR2(10) | N |  |  |
| 2 | NUM_OP_COMMIT | NUMBER(15) | Y |  |  |
| 3 | IND_SERVIDOR_HELP | CHAR(1) | N | 'I' |  |
| 4 | NUM_THREAD | NUMBER(3) | Y |  |  |
| 5 | IND_IMP_DOCFIS_MULTI_LOAD | CHAR(1) | Y | 'S' |  |
| 6 | IND_ENVIRONMENT | VARCHAR2(20) | Y |  |  |
| 7 | IND_ACCESS_CP_T1 | CHAR(1) | Y |  |  |
| 8 | IND_TST_UNIT | CHAR(1) | Y | 'N' |  |
| 9 | IND_FUNCTION_ENABLED | CHAR(1) | Y | 'N' |  |
| 10 | QTD_LINHAS_RETRIEVE | NUMBER(10) | Y | 7000 |  |
| 11 | IND_DMART_EXPRESS | CHAR(1) | Y | 'N' |  |
| 12 | COD_EMP_CARGA_LOG | VARCHAR2(3) | Y |  |  |
| 13 | IND_VALID_IMPORT | CHAR(1) | Y | 'N' |  |
| 14 | DB_OWNER | VARCHAR2(100) | Y |  |  |
| 15 | NUM_THREAD_FRW | NUMBER(3) | Y | 0 |  |
| 16 | PERCENT_MAX_UTIL_T1 | NUMBER(3) | Y | 0 |  |
| 17 | NUM_MAX_PROC_EXEC_T1 | NUMBER(5) | Y | 0 |  |
| 18 | IND_CORRIGE_STS_FILA | CHAR(1) | Y | 'N' |  |
| 19 | DATA_ULT_CORRIGE_FILA | DATE | Y |  |  |
| 20 | IND_CADENCIA_CORRIGE_FILA | NUMBER(3) | Y | 1 |  |
| 21 | IND_AUDIT_TABLE_T1 | CHAR(1) | Y | 'N' |  |
| 22 | IND_LEVEL_LOG_DATADOG | VARCHAR2(10) | Y | 'INFO' | Contem o indicador dos niveis de log que deverao ser catalogados no DATADOG. Os valores possiveis sao: OFF, FATAL, ERROR, WARN, INFO, DEBUG, ALL. Os niveis pela ordem sao: OFF    (10) FATAL  (20) ERROR  (30) WARN   (40) INFO   (50) DEBUG  (60) ALL    (70) |
| 23 | QTDE_REGS_SAFX_THREAD | NUMBER(12) | Y | 500000 | Valor minimo para considerar a importacao em threads das SAFXs habilitadas como multiload. <0> significa que esta desligado e nao fara multithread |
| 24 | DT_ULT_ALTERACAO | DATE | Y |  |  |
| 25 | USR_ULT_ALTERACAO | VARCHAR2(128) | Y |  |  |
| 26 | IND_CTRL_DATAMART_AUTOM | NUMBER | Y | 0 |  |
| 27 | TIMEOUT_LOCK | NUMBER(12) | Y | 300 | Valor descrito em segundos para determinar a qtde de tempo q uma sessao pode ficar em lock |

**PK**: COD_BANCO

---

## PRT_PAR_OPER_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PARAM | NUMBER(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | TPO_CFO | VARCHAR2(1) | N |  |  |
| 4 | TPO_DED | VARCHAR2(1) | N |  |  |

**PK**: COD_PARAM, TPO_CFO, TPO_DED

**FKs**:
- IDENT_ESTADO → ESTADO(IDENT_ESTADO)

---

## PRT_PERC_PROD_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | DAT_INI_VALID | DATE | N |  |  |
| 5 | PERC_ST | NUMBER(7,4) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DAT_INI_VALID

---

## PRT_PERDCOMP_DOCFIS

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
| 11 | CNPJ_SUCEDIDA | VARCHAR2(14) | Y |  |  |
| 12 | CNPJ_DETENT_CRED | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## PRT_PERIODO_VMCA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | IND_INTERVALO | CHAR(1) | N |  |  |
| 3 | DATA_INI_PER | DATE | Y |  |  |
| 4 | DATA_FIM_PER | DATE | Y |  |  |
| 5 | PER_MESES | NUMBER(3) | Y |  |  |
| 6 | ULTIMA_ATUALIZACAO | TIMESTAMP(6) WITH TIME ZONE | Y |  |  |
| 7 | DATA_INI_PER_ULT_ATUAL | DATE | Y |  |  |
| 8 | DATA_FIM_PER_ULT_ATUAL | DATE | Y |  |  |

**PK**: ID

---

## PRT_PFJ_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | COD_PARAM | NUMBER(3) | N |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y | '4' |  |

**PK**: COD_PARAM, COD_FIS_JUR, IND_FIS_JUR, GRUPO_FIS_JUR, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_PORT63_AUTONOMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(12) | N |  |  |
| 2 | DATA_INC_REG | DATE | N |  |  |
| 3 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 4 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 5 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 6 | COD_CAMPO | VARCHAR2(3) | N |  |  |
| 7 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 8 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 9 | IND_BC_IRRF | VARCHAR2(2) | Y |  |  |

**PK**: ID

**FKs**:
- COD_LAYOUT, COD_PERFIL → COTEPE_PERFIL(COD_LAYOUT, COD_PERFIL)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_VERBA → X2023_VERBAS(IDENT_VERBA)

**Indexes**:
- IX_PRT_PORT63_AUTONOMO (UNIQUE): (DATA_INC_REG, COD_LAYOUT, COD_PERFIL, IDENT_VERBA)
- IX_PRT_PORT63_AUT_CTA: (IDENT_CONTA)

---

## PRT_PORTOALEGRE_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 2 | COD_DOCTO_ISSQN | VARCHAR2(2) | N |  |  |
| 3 | VALID_DOCTO | DATE | N |  |  |
| 4 | IND_TIPO_RELAC | CHAR(1) | N |  | 1 - Tipo de Documento Normal; 2 - Tipo de Documento com Deducao de Material |

**PK**: COD_DOCTO, VALID_DOCTO, IND_TIPO_RELAC

---

## PRT_PRD_MSAF_SERC_V
**Comment**: Tabela contendo as informações de relacionamento entre os produtos SERC e os produtos MSAF.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROD_SERC | VARCHAR2(9) | N |  | Código do produto na tabela SERC |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | N |  | Grupo do produto referente ao cadastro de produtos MSAF  |
| 3 | IND_PRODUTO | CHAR(1) | N |  | Indicador do Produto referente ao cadastro de produtos MSAF  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  | Código do Produto referente ao cadastro de produtos MSAF  |
| 5 | VALID_INICIAL | DATE | N |  | Data Inicial da validade do relacionamento  |
| 6 | VALID_FINAL | DATE | Y |  | Data Final   da validade do relacionamento  |

**PK**: COD_PROD_SERC, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, VALID_INICIAL

**FKs**:
- COD_PROD_SERC → PRT_PRD_SERC(COD_PROD_SERC)

---

## PRT_PRD_OBRIG
**Comment**: Tabela de cadastro de codigos de produto especificos de obrigacoes, ex DIEF-PA, DAC-AL. TACES 50

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_PRODUTO_OBRIG | VARCHAR2(60) | N |  |  |
| 3 | DSC_PRODUTO_OBRIG | VARCHAR2(50) | Y |  |  |
| 4 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 5 | TP_PRODUTO | VARCHAR2(50) | N |  |  |

**PK**: COD_MODULO, COD_PRODUTO_OBRIG, TP_PRODUTO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_PRD_OBRIG_MSAF
**Comment**: Tabela de mapeamento de c¢digos de produtos MasterSAF (x2013_produto) por codigos de produtos especificos de obrigacoes (PRT_PRD_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 6 | COD_PRODUTO_OBRIG | VARCHAR2(60) | Y |  |  |
| 7 | TP_PRODUTO | VARCHAR2(50) | Y |  |  |

**PK**: VALID_INICIAL, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_MODULO

---

## PRT_PRD_SERC
**Comment**: Tabela contendo as informações de cadastro de produtos SERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROD_SERC | VARCHAR2(9) | N |  | código do produto na tabela SERC |
| 2 | DESC_PROD_SERC | VARCHAR2(100) | Y |  | descrição do produto na tabela SERC |

**PK**: COD_PROD_SERC

---

## PRT_PRD_TRB_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF | VARCHAR2(2) | Y |  |  |
| 2 | TP_TRIB | VARCHAR2(2) | Y |  |  |
| 3 | DAT_INI_VAL | DATE | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | DAT_FIM_VAL | DATE | Y |  |  |
| 7 | IND_GRUPO | CHAR(1) | Y |  |  |

**Indexes**:
- PRT_PRD_TRB_ICM (UNIQUE): (COD_UF, TP_TRIB, DAT_INI_VAL, IND_PRODUTO, COD_PRODUTO)

---

## PRT_PROD_EXC_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO_INI | VARCHAR2(60) | N |  |  |
| 7 | COD_PRODUTO_EXC | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI, COD_PRODUTO_EXC

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_PARAM, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI → PRT_PROD_MSAF(COD_EMPRESA, COD_ESTAB, COD_PARAM, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI)

---

## PRT_PROD_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO_INI | VARCHAR2(60) | N |  |  |
| 7 | COD_PRODUTO_FIM | VARCHAR2(60) | Y |  |  |
| 8 | IND_EXCECAO | CHAR(1) | Y |  |  |
| 9 | COD_GRP_INCENT | VARCHAR2(5) | Y |  |  |
| 10 | TIPO_CODIGO_DECLAN | CHAR(1) | Y |  | Parametrização dos produtos x Distribuição do Valor Adicionado - Declan RJ |
| 11 | CODIGO_DECLAN | NUMBER(5) | Y |  | Parametrização dos produtos x Distribuição do Valor Adicionado - Declan RJ |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT → ICT_GRP_INCENT(COD_EMPRESA, COD_ESTAB, COD_GRP_INCENT)
- TIPO_CODIGO_DECLAN, CODIGO_DECLAN → EST_RJ_DECLAN_COD(TIPO_CODIGO, CODIGO)

---

## PRT_PROD_MSAF_OBRIG
**Comment**: Tabela de mapeamento de c¢digos de produtos MasterSAF (x2013_produto) por codigos de produtos especificos de obrigacoes (PRT_PROD_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 6 | IDENT_PRODUTO_OBRIG | NUMBER(12) | Y |  |  |
| 7 | VLR_ENC_CARAC | VARCHAR2(10) | Y |  |  |
| 8 | COD_VASILHAME | VARCHAR2(2) | Y |  |  |
| 9 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 10 | VALID_FINAL | DATE | Y |  |  |

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_PRODUTO_OBRIG → PRT_PROD_OBRIG(IDENT_PRODUTO_OBRIG)

**Indexes**:
- UK_PRT_PROD_MSAF_OBRIG (UNIQUE): (VALID_INICIAL, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_MODULO, TP_AVALIACAO)

---

## PRT_PROD_OBRIG
**Comment**: Código de Produtos das Obrigacoes com Validade - TFIX117

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PRODUTO_OBRIG | NUMBER(12) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | COD_PRODUTO_OBRIG | VARCHAR2(60) | N |  |  |
| 4 | VALID_INI_PRODUTO_OBRIG | DATE | N |  |  |
| 5 | VALID_FIM_PRODUTO_OBRIG | DATE | Y |  |  |
| 6 | DSC_PRODUTO_OBRIG | VARCHAR2(100) | Y |  |  |
| 7 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |

**PK**: IDENT_PRODUTO_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

**Indexes**:
- UK_PRT_PROD_OBRIG (UNIQUE): (COD_MODULO, COD_PRODUTO_OBRIG, VALID_INI_PRODUTO_OBRIG)

---

## PRT_PROD_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PARAM | CHAR(1) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | VLR_ALIQ_INT | NUMBER(7,4) | N |  |  |
| 8 | DATA_INI | DATE | N |  |  |
| 9 | DATA_FIM | DATE | Y |  |  |
| 10 | IND_FCP | CHAR(1) | Y |  |  |
| 11 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 12 | NUM_PROCESSO | VARCHAR2(20) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |
| 15 | IND_PRODUTO_PRINC | CHAR(1) | N |  |  |
| 16 | COD_PRODUTO_PRINC | VARCHAR2(60) | N |  |  |
| 17 | IDENT_MEDIDA_PRINC | NUMBER(12) | Y |  |  |
| 18 | IDENT_UND_PADRAO_PRINC | NUMBER(12) | Y |  |  |

**Indexes**:
- IDX_PRT_PROD_LOOKUP: (COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO)
- IDX_PRT_PROD_PARAM: (COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, IND_PARAM)

---

## PRT_REC_SLD_IRPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_APURACAO | CHAR(1) | Y |  | (A)nual - (T)rimestral |
| 4 | IND_ENCERRAMENTO | CHAR(1) | Y |  | (A)nual - (S)emestral - (T)rimestral |
| 5 | IND_CONTA_CONTAB_CC | CHAR(1) | Y |  |  |
| 6 | IND_OMITIR_CENTRO_CUSTO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_REL_CAMPO
**Comment**: Parametrizacao dos campos para composicao dos relatorios dinamicos

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REL | NUMBER(12) | N |  |  |
| 2 | ID_CAMPO | NUMBER(12) | N |  |  |
| 3 | NOM_CAMPO_REL | VARCHAR2(100) | Y |  | Nome a ser considerado para a coluna do relatorio, definida pelo usuario |
| 4 | ID_GRP_REL | NUMBER(12) | Y |  |  |
| 5 | ID_TAB_GRP | NUMBER(12) | Y |  |  |
| 6 | ID_CAMPO_GRP | NUMBER(12) | Y |  |  |
| 7 | IND_DET_GRUPO | CHAR(1) | Y |  | D:Detalhe; G: Grupo.  Indicador se o campo faz parte do detalhe ou do grupamento do relatorio |
| 8 | NUM_POSICAO_DET | NUMBER(2) | Y |  | Posicao da coluna que faz parte do detalhe do relatorio |
| 9 | NUM_ORDEM | NUMBER(2) | Y |  | Ordenacao dos campos do relatorio, definida pelo usuario. Monta o ORDER BY da query do relatorio |
| 10 | NUM_ORDEM_DET_GRUPO | NUMBER(2) | Y |  | 1: Grupo; 2: Detalhe. Indicador da ordem entre detalhe e grupamento, Monta ORDER BY da query do relatório, composto primeiro pelos campos de grupamento e em seguida pelos de detalhe. |
| 11 | IND_TOT_GRUPO | CHAR(1) | Y |  | Indica se o campo de valor sera totalizado no grupamento do relatorio |

**PK**: ID_REL, ID_CAMPO

**FKs**:
- ID_REL → PRT_REL_DEF(ID_REL)
- ID_GRP_REL, ID_TAB_GRP, ID_CAMPO_GRP → CAD_GRP_REL_CAMPO(ID_GRP_REL, ID_TAB_GRP, ID_CAMPO_GRP)

---

## PRT_REL_DEF
**Comment**: Parametrizacao dos relatorios dinamicos

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REL | NUMBER(12) | N |  |  |
| 2 | COD_REL | VARCHAR2(5) | Y |  |  |
| 3 | DSC_REL | VARCHAR2(100) | Y |  | Descricao considerada no cabecalho do relatorio |
| 4 | ID_GRP_REL | NUMBER(12) | Y |  | Identificação do cadastro de Grupo de Relatorios (CAD_GRP_REL) |
| 5 | IND_QUEBRA_PAG | CHAR(1) | Y |  | Considerado na montagem do relatorio para indicar a necessidade de quebra de pagina por agrupamento. |
| 6 | IND_RETRATO_PAISAGEM | CHAR(1) | Y |  | R: retrato; P: paisagem |
| 7 | DSC_DETALHADA | VARCHAR2(400) | Y |  |  |

**PK**: ID_REL

**FKs**:
- ID_GRP_REL → CAD_GRP_REL(ID_GRP_REL)

---

## PRT_RJ_GIA_AMPARO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 2 | COD_AMPARO_GIA | NUMBER(5) | Y |  |  |

**PK**: COD_AMPARO_LEGAL

---

## PRT_RJ_GIA_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | COD_ESTADO_GIA | NUMBER(3) | Y |  |  |

**PK**: COD_ESTADO

---

## PRT_RJ_IDENT_AIDF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_AIDF | VARCHAR2(12) | N |  |  |
| 4 | IDENT_AIDF | VARCHAR2(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_AIDF

---

## PRT_SERIE_MODELO_MSAF_OBRIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 3 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 5 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 6 | COD_SERIE_OBRIG | VARCHAR2(10) | Y |  |  |

**PK**: VALID_INICIAL, SERIE_DOCFIS, GRUPO_MODELO, COD_MODELO, COD_MODULO

---

## PRT_SERIE_MSAF_OBRIG
**Comment**: Tabela de parametrizacao das series dos documentos fiscais do MasterSAF por codigos das series especificas de obrigacoes (PRT_SERIE_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | COD_SERIE_OBRIG | VARCHAR2(10) | Y |  |  |

**PK**: VALID_INICIAL, SERIE_DOCFIS, COD_MODULO

**FKs**:
- COD_MODULO, COD_SERIE_OBRIG → PRT_SERIE_OBRIG(COD_MODULO, COD_SERIE_OBRIG)

---

## PRT_SERIE_OBRIG
**Comment**: Tabela de cadastro de codigos das series especificas de obrigacoes, ex DMS-TERESINA, DMS-PALMAS. Taces xxxx

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_SERIE_OBRIG | VARCHAR2(10) | N |  |  |
| 3 | DSC_SERIE_OBRIG | VARCHAR2(60) | Y |  |  |
| 4 | IND_SERIE_MODELO | CHAR(1) | Y |  |  |

**PK**: COD_MODULO, COD_SERIE_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_SERVICO_BENEF_FISCAL
**Comment**: Tabela de parametrizacao do Servicos Msaf (X2018_SERVICOS) por Beneficio Fiscal definido por cada obrigacao municipal.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 3 | COD_SERVICO | VARCHAR2(5) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 5 | COD_BENEF_FISCAL | VARCHAR2(10) | Y |  |  |

**PK**: VALID_INICIAL, GRUPO_SERVICO, COD_SERVICO, COD_MODULO

**FKs**:
- COD_MODULO, COD_BENEF_FISCAL → PRT_BENEF_FISCAL_OBRIG(COD_MODULO, COD_BENEF_FISCAL)

---

## PRT_SERVICO_CONTAS_REF
**Comment**: Tabela de Parametrizacao do Plano de Contas Referencial x Servicos da Lei Complementar 116/03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 4 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 5 | COD_SERV_LEI_116 | VARCHAR2(4) | N |  | Codigo do Servico da Lei 116/03 - tabela referenciada DWT_SERVICO_LEI_116 |
| 6 | IND_RECOLH | CHAR(1) | Y |  |  |
| 7 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |

**PK**: VALID_INICIAL, IDENT_ESTADO, COD_MUNICIPIO, IDENT_CONTA_REF

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_CONTA_REF → SPED_CONTAS_REF(IDENT_CONTA_REF)

---

## PRT_SERVICO_FIS_JUR_DESBH
**Comment**: Tabela de parametrizacao Classificacao de Servicos por Pessoa Fis/Jur da DES BH. Modulo Parametros para Municipio.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | COD_TABELA_DES | VARCHAR2(3) | N |  | Lista de Tabelas especifica da DES BH. Dominio view: DES_BH_TABELA_V |
| 7 | COD_PARAM_DES | VARCHAR2(3) | N |  | Lista de parametros especifica da DES BH. Cada Codigo de Tabela da DES BH possui sua lista de parametros. Dominio view: DES_BH_PARAM_V |
| 8 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 9 | COD_SERVICO | VARCHAR2(4) | N |  | Codigo Servico do cadastro do Mastersaf - SAFX2018. |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, COD_TABELA_DES, COD_PARAM_DES, GRUPO_SERVICO, COD_SERVICO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## PRT_SERVICO_FIS_JUR_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | COD_PARAM | NUMBER(3) | N |  |  |
| 6 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 7 | COD_SERVICO | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_MUNICIPIO, COD_PARAM, IDENT_FIS_JUR, GRUPO_SERVICO, COD_SERVICO

**FKs**:
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_SERVICO_LEI_116_OBRIG
**Comment**: Tabela de parametrizacao da relacao entre os Codigos de Servico da Lei 116 (DWT_SERVICO_LEI_116) e servicos das obrigacoes municipais (PRT_SERVICO_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | COD_SERV_LEI_116 | VARCHAR2(4) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | COD_SERVICO_OBRIG | VARCHAR2(20) | Y |  |  |

**PK**: VALID_INICIAL, COD_SERV_LEI_116, COD_MODULO

**FKs**:
- COD_MODULO, COD_SERVICO_OBRIG → PRT_SERVICO_OBRIG(COD_MODULO, COD_SERVICO_OBRIG)

---

## PRT_SERVICO_MSAF_OBRIG
**Comment**: Tabela de parametrizacao dos tipos de servico MasterSAF (x2018_servicos) por servicos especificos de obrigacoes (PRT_SERVICO_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 3 | COD_SERVICO | VARCHAR2(5) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 5 | COD_SERVICO_OBRIG | VARCHAR2(20) | Y |  |  |

**PK**: VALID_INICIAL, GRUPO_SERVICO, COD_SERVICO, COD_MODULO

**FKs**:
- COD_MODULO, COD_SERVICO_OBRIG → PRT_SERVICO_OBRIG(COD_MODULO, COD_SERVICO_OBRIG)

---

## PRT_SERVICO_MUNIC_DESBH
**Comment**: Tabela de parametrizacao Classificacao de Servicos por Municipio da DES BH. Modulo Parametros para Municipio.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | COD_TABELA_DES | VARCHAR2(3) | N |  | Lista de Tabelas especifica da DES BH. Dominio view: DES_BH_TABELA_V |
| 4 | COD_PARAM_DES | VARCHAR2(3) | N |  | Lista de parametros especifica da DES BH. Cada Codigo de Tabela da DES BH possui sua lista de parametros. Dominio view: DES_BH_PARAM_V |
| 5 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 6 | COD_SERVICO | VARCHAR2(4) | N |  | Codigo Servico do cadastro do Mastersaf - SAFX2018. |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, COD_TABELA_DES, COD_PARAM_DES, GRUPO_SERVICO, COD_SERVICO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## PRT_SERVICO_MUNIC_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | COD_PARAM | NUMBER(3) | N |  |  |
| 5 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 6 | COD_SERVICO | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_MUNICIPIO, COD_PARAM, GRUPO_SERVICO, COD_SERVICO

**FKs**:
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_SERVICO_OBRIG
**Comment**: Tabela de cadastro de codigos dos tipos de servicos especificos de obrigacoes, ex NF Carioca. TFIX85

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_SERVICO_OBRIG | VARCHAR2(20) | N |  |  |
| 3 | DSC_SERVICO_OBRIG | VARCHAR2(1000) | Y |  |  |

**PK**: COD_MODULO, COD_SERVICO_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_SERV_AJUSTES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 4 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 5 | IND_AJ_REINF | CHAR(1) | N |  |  |
| 6 | COD_AJ_REINF | VARCHAR2(2) | Y |  |  |
| 7 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 8 | COD_RECEITA | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_SERVICO, COD_SERVICO, IND_AJ_REINF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PRT_SERV_LEI_116_GISS
**Comment**: Tabela de parametrizacao da relacao entre os Codigos de Servico da Lei 116 (DWT_SERVICO_LEI_116) e os Codigos de Servicos Municipais GISS ONLINE (SERV_MUNIC_GISS).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_SERVICO | DATE | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 4 | COD_SERV_LEI_116 | VARCHAR2(4) | N |  |  |
| 5 | COD_SERVICO_GISS | VARCHAR2(10) | N |  |  |
| 6 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |

**PK**: VALID_SERVICO, IDENT_ESTADO, COD_MUNICIPIO, COD_SERV_LEI_116

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## PRT_SERV_LEI_116_VETADO
**Comment**: Tabela de parametrizacao dos Codigos de Servico da Lei 116 (DWT_SERVICO_LEI_116) vetados pelo municipio da obrigacao.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | COD_SERV_LEI_116 | VARCHAR2(4) | N |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, COD_SERV_LEI_116

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## PRT_SERV_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 5 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 6 | COD_COMPLEMENTAR | VARCHAR2(10) | Y |  |  |
| 7 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 8 | COD_RECEITA | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, GRUPO_SERVICO, COD_SERVICO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_SERV_MUNIC_GISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 4 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 5 | COD_SERVICO_GISS | VARCHAR2(10) | Y |  |  |
| 6 | VALID_SERVICO | DATE | N |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_MUNICIPIO, IDENT_SERVICO, VALID_SERVICO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## PRT_STRING

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 2 | FUNCIONALIDADE | VARCHAR2(255) | N |  |  |
| 3 | VALOR | VARCHAR2(255) | N |  |  |
| 4 | DAT_GRAVACAO | DATE | Y | sysdate |  |

**PK**: COD_USUARIO, FUNCIONALIDADE, VALOR

**Indexes**:
- IX_PRT_STRING_01: (COD_USUARIO, DAT_GRAVACAO)

---

## PRT_SUBCLASSE_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 2 | COD_SUBCLASSE_CONSUMO | VARCHAR2(2) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(200) | Y |  |  |

**PK**: COD_MODELO, COD_SUBCLASSE_CONSUMO

---

## PRT_TIPO_CLIENTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 2 | COD_TP_CLIENTE | VARCHAR2(2) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(200) | Y |  |  |

**PK**: COD_MODELO, COD_TP_CLIENTE

---

## PRT_TIPO_CONHECIMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO | VARCHAR2(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(30) | Y |  |  |

**PK**: COD_TIPO

---

## PRT_TIPO_DOCTO_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 3 | COD_DOCTO_MUNIC | VARCHAR2(5) | N |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, COD_DOCTO_MUNIC

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## PRT_TIPO_SERV_ESOCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TIPO_SERV_ESOCIAL | NUMBER(12) | N |  |  |
| 2 | COD_TIPO_SERV_ESOCIAL | VARCHAR2(9) | N |  |  |
| 3 | DATA_INI_VIGENCIA | DATE | N |  |  |
| 4 | DSC_TIPO_SERV_ESOCIAL | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_TIPO_SERV_ESOCIAL

**Indexes**:
- UK_TP_SERV_ESOC (UNIQUE): (COD_TIPO_SERV_ESOCIAL, DATA_INI_VIGENCIA)

---

## PRT_TP_BAIRRO_MSAF_OBRIG
**Comment**: Tabela de parametrizacao dos bairros MasterSAF por tipos de bairros especificos das obrigacoes (PRT_TP_BAIRRO_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | TP_BAIRRO | VARCHAR2(25) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | COD_TP_BAIRRO_OBRIG | VARCHAR2(25) | Y |  |  |

**PK**: VALID_INICIAL, TP_BAIRRO, COD_MODULO

**FKs**:
- COD_MODULO, COD_TP_BAIRRO_OBRIG → PRT_TP_BAIRRO_OBRIG(COD_MODULO, COD_TP_BAIRRO_OBRIG)

---

## PRT_TP_BAIRRO_OBRIG
**Comment**: Tabela de cadastro dos tipos de bairros especificos das obrigacoes. TFIX110

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_TP_BAIRRO_OBRIG | VARCHAR2(25) | N |  |  |
| 3 | DSC_TP_BAIRRO_OBRIG | VARCHAR2(60) | Y |  |  |

**PK**: COD_MODULO, COD_TP_BAIRRO_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_TP_DOCTO_MSAF_OBRIG
**Comment**: Tabela de parametrizacao dos tipos de documento MasterSAF (x2005_tipo_docto) por tipos de documento especificos de obrigacoes (PRT_TP_DOCTO_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 3 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 5 | COD_TP_DOCTO_OBRIG | VARCHAR2(10) | Y |  |  |

**PK**: VALID_INICIAL, GRUPO_DOCTO, COD_DOCTO, COD_MODULO

**FKs**:
- COD_MODULO, COD_TP_DOCTO_OBRIG → PRT_TP_DOCTO_OBRIG(COD_MODULO, COD_TP_DOCTO_OBRIG)

---

## PRT_TP_DOCTO_OBRIG
**Comment**: Tabela de cadastro de codigos dos tipos de documentos especificos de obrigacoes, ex ISISS-VITORIA, DMS-PALMAS. TFIX84

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_TP_DOCTO_OBRIG | VARCHAR2(10) | N |  |  |
| 3 | DSC_TP_DOCTO_OBRIG | VARCHAR2(60) | Y |  |  |

**PK**: COD_MODULO, COD_TP_DOCTO_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_TP_LOGRADOURO_MSAF_OBRIG
**Comment**: Tabela de parametrizacao dos logradouros MasterSAF por tipos de logradouros especificos das obrigacoes (PRT_TP_LOGRADOURO_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | TP_LOGRADOURO | VARCHAR2(25) | N |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 4 | COD_TP_LOGRADOURO_OBRIG | VARCHAR2(25) | Y |  |  |

**PK**: VALID_INICIAL, TP_LOGRADOURO, COD_MODULO

**FKs**:
- COD_MODULO, COD_TP_LOGRADOURO_OBRIG → PRT_TP_LOGRADOURO_OBRIG(COD_MODULO, COD_TP_LOGRADOURO_OBRIG)

---

## PRT_TP_LOGRADOURO_OBRIG
**Comment**: Tabela de cadastro dos tipos de logradouros especificos das obrigacoes. TFIX109

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | COD_TP_LOGRADOURO_OBRIG | VARCHAR2(25) | N |  |  |
| 3 | DSC_TP_LOGRADOURO_OBRIG | VARCHAR2(60) | Y |  |  |

**PK**: COD_MODULO, COD_TP_LOGRADOURO_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_TRIBUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 2 | VALID_TRIBUTO | DATE | N |  |  |
| 3 | VLR_MIN_RECOLH | NUMBER(17,2) | Y |  |  |
| 4 | VLR_MIN_ENQ | NUMBER(17,2) | Y |  |  |
| 5 | VLR_MIN_RET | NUMBER(17,2) | Y |  |  |

**PK**: COD_TRIBUTO, VALID_TRIBUTO

---

## PRT_TRIBUT_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_TRIB_INT | NUMBER(5) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_TRIB_INT

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_UF_AMPARO_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 3 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: IDENT_ESTADO, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCORR, COD_CFO

---

## PRT_UF_AMPARO_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 3 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: IDENT_ESTADO, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCORR, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## PRT_UF_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | COD_PARAM | NUMBER(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTADO, COD_PARAM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## PRT_UF_OBRIG_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 2 | VALID_INICIAL | DATE | N |  |  |
| 3 | COD_UF_MSAF | VARCHAR2(2) | N |  |  |
| 4 | COD_UF_OBRIG | VARCHAR2(2) | Y |  |  |
| 5 | DSC_UF_OBRIG | VARCHAR2(50) | Y |  |  |

**PK**: COD_MODULO, VALID_INICIAL, COD_UF_MSAF

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## PRT_UND_MEDIDA_FCI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MEDIDA_FCI | VARCHAR2(6) | N |  |  |
| 2 | DATA_VALIDADE | DATE | N |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_MEDIDA_FCI, DATA_VALIDADE

---

## PRT_VALIDADOR
**Comment**: Tabela de Cadastro dos Validadores das Obrigacoes Municipais, referente a TFIX115.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VALIDADOR | VARCHAR2(20) | N |  |  |
| 2 | IND_MODELO_MSAF_MODELO | CHAR(1) | Y |  |  |
| 3 | IND_MODELO_MSAF_SERIE | CHAR(1) | Y |  |  |
| 4 | IND_TP_BAIRRO_MSAF_TP_BAIRRO | CHAR(1) | Y |  |  |
| 5 | IND_CIDADE_MSAF_CIDADE | CHAR(1) | Y |  |  |
| 6 | IND_ALIQUOTA_MSAF_ALIQUOTA | CHAR(1) | Y |  |  |
| 7 | IND_TP_DOCTO_MSAF_TP_DOCTO | CHAR(1) | Y |  |  |
| 8 | IND_TP_DOCTO_MSAF_ESPECIE | CHAR(1) | Y |  |  |
| 9 | IND_TP_LOGRAD_MSAF_TP_LOGRAD | CHAR(1) | Y |  |  |
| 10 | IND_SERIE_MSAF_SERIE | CHAR(1) | Y |  |  |
| 11 | IND_SERVICO_MSAF_ATIVIDADE | CHAR(1) | Y |  |  |
| 12 | IND_SERVICO_MSAF_SERVICO | CHAR(1) | Y |  |  |
| 13 | IND_ATIV_MSAF_COD_CTISS | CHAR(1) | Y |  |  |
| 14 | IND_SERIE_MODELO_MSAF_SERIE | CHAR(1) | Y |  |  |
| 15 | IND_MODELO_MUNIC_MSAF_MODELO | CHAR(1) | Y |  |  |
| 16 | IND_ATIV_MUNIC_MSAF_ATIVIDADE | CHAR(1) | Y |  |  |
| 17 | IND_CANAL_DISTRIB_OBRAS_SEQ | CHAR(1) | Y |  |  |
| 18 | IND_CENTRALIZA_ESTAB | CHAR(1) | Y |  |  |
| 19 | NOM_FRAMEWORK | VARCHAR2(100) | Y |  | Nome do framework utilizado |

**PK**: COD_VALIDADOR

---

## PRT_VALIDADOR_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | COD_VALIDADOR | VARCHAR2(20) | N |  |  |
| 4 | VALID_VALIDADOR | DATE | N |  |  |
| 5 | DESC_VALIDADOR | VARCHAR2(500) | N |  |  |
| 6 | COD_MODULO | VARCHAR2(8) | Y |  |  |
| 7 | IND_GERA_BANCO | CHAR(1) | Y |  | Indica se a geração do meio magnético bancos ficará disponivel para o municipio/uf. |
| 8 | IND_MANUT_DEDUCAO | CHAR(1) | Y |  | Indica se a manutenção das deduções ficará disponivel para o municipio/uf. |
| 9 | IND_MANUT_SIGAMWEB | CHAR(1) | Y |  | Indica se a manutenção dos dados iniciais do validador SIGAM WEB ficará disponivel para o municipio/uf.  Referente a tabela MUN_SIGAMWEB_DADOS_INI |
| 10 | IND_MANUT_RECEITA | CHAR(1) | Y |  | Indica se a manutenção das receitas ficará disponivel para o municipio/uf. |
| 11 | IND_MANUT_PROF_LIBERAL | CHAR(1) | Y |  | Indica se a manutenção dos profissionais liberais ficará disponivel para o municipio/uf. |
| 12 | IND_MANUT_BANCO | CHAR(1) | Y |  | Indica se a manutenção dos dados cadastrais bancos ficará disponivel para o municipio/uf. |
| 13 | IND_GERA_RPS | CHAR(1) | Y |  | Indica se a geração do meio magnético RPS ficará disponivel para o municipio/uf. Criado inicialmente para atendimento a Sta Barbara DOeste |
| 14 | IND_MANUT_SOCIOS | CHAR(1) | Y |  | Indica se a manutencao dos socios ficara disponivel para o municipio/uf. |
| 15 | IND_MANUT_INF_ECONOM | CHAR(1) | Y |  | Indica se a manutencao das informacoes economicas ficara disponivel para o municipio/uf. |
| 16 | IND_ESTAB_CCONTAB | CHAR(1) | Y |  |  |
| 17 | IND_ESTAB_SCONTAB | CHAR(1) | Y |  |  |
| 18 | IND_GERA_CC | CHAR(1) | Y |  | Indicador de geração do meio magnético de Entradas de Serviços (Const. Civil/Utilities/Telecom) |
| 19 | VALID_FINAL | DATE | Y |  | Data final de validade do validador para um determinado municipio. Campo deve ser preenchido quando houver mais de um validador para um municipio. |
| 20 | IND_GERA_ASSINATURA | CHAR(1) | Y |  | Indica se a geracao da assinatura digital em arquivos xml ficara disponivel para o municipio/uf. |
| 21 | IND_MANUT_CANOAS | CHAR(1) | Y |  | Indica se a manutenção dos dados iniciais do validador CANOAS ficara disponivel para o municipio/uf. Referente a tabela MUN_CANOAS_DADOS_INI |
| 22 | IND_MANUT_REMESSA | CHAR(1) | Y |  | Indica se a manutenção dos dados iniciais do validador REMESSA ficará disponivel para o municipio/uf.  Referente a tabela MUN_REMESSA_DADOS_INI |
| 23 | IND_MANUT_DESPESA | CHAR(1) | Y |  | Indica se a manutenção das despesas ficará disponivel para o municipio/uf.  Criado para atender ao validador REMESSA. Referente a tabela MUN_MANUT_DESPESA |
| 24 | IND_MANUT_DEDUCAO_PROJ | CHAR(1) | Y |  | Indica se a manutenção das deduções (Projeto) ficará disponivel para o municipio/uf.  Criado para atender ao validador REMESSA. Referente a tabela MUN_MANUT_DEDUCAO_PROJ |
| 25 | IND_MANUT_SIGIS | CHAR(1) | Y |  | Indica se a manutenção dos dados iniciais do validador SIGIS ficará disponivel para o municipio/uf.  Referente a tabela IND_MANUT_SIGIS |
| 26 | IND_MANUT_PARNAMIRIM | CHAR(1) | Y |  | Indica se a manutenção dos dados iniciais do validador PARNAMIRIM ficará disponÍvel para o municipio/uf.  Referente a tabela IND_MANUT_PARNAMIRIM |
| 27 | IND_MANUT_MAT_BETHA | CHAR(1) | Y |  |  |
| 28 | IND_GERA_CADASTRO | CHAR(1) | Y |  |  |
| 29 | IND_MANUT_DESIF_0430 | CHAR(1) | Y |  |  |
| 30 | IND_MANUT_DESIF_0440 | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, COD_VALIDADOR, VALID_VALIDADOR

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## PRT_VALIDADOR_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VALIDADOR | VARCHAR2(20) | N |  |  |
| 2 | IND_GERA_CC | CHAR(1) | Y |  |  |
| 3 | IND_GERA_BANCOS | CHAR(1) | Y |  |  |
| 4 | IND_MANUT_DEDUCAO | CHAR(1) | Y |  |  |
| 5 | IND_MANUT_MAT_BETHA | CHAR(1) | Y |  |  |

**PK**: COD_VALIDADOR

---

## PRT_VAL_SAFX196

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_SISTEMA_ORIGEM | NUMBER(38) | N |  |  |
| 2 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 3 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 4 | IND_DATA_DOC | CHAR(1) | Y |  |  |
| 5 | IND_DATA_EMIS | CHAR(1) | Y |  |  |
| 6 | IND_DATA_MOV | CHAR(1) | Y |  |  |
| 7 | GRUPO | VARCHAR2(9) | Y |  |  |
| 8 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 10 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 11 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 12 | NORM_DEV | CHAR(1) | Y |  |  |
| 13 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 14 | COD_MODELO | VARCHAR2(2) | Y |  |  |

**PK**: ID_SISTEMA_ORIGEM

**FKs**:
- ID_SISTEMA_ORIGEM → SISTEMA_ORIGEM(ID)

---

## PRT_VASILHAME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VASILHAME | VARCHAR2(3) | N |  |  |
| 2 | DATA_INI_VALID | DATE | N |  |  |
| 3 | DATA_FIM_VALID | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_VASILHAME, DATA_INI_VALID

---

## PRT_VEIC_TRANSP_MSAF_OBRIG
**Comment**: Tabela de parametrizacao dos Veiculos de Transporte MasterSAF (x2049_veic_transp) por codigos de Veiculos de Transportes especificos de obrigacoes (PRT_VEIC_TRANSP_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_VEIC_TRANSP | VARCHAR2(9) | N |  |  |
| 3 | COD_VEIC_TRANSP | VARCHAR2(6) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 5 | IDENT_VEIC_TRANSP_OBRIG | NUMBER(12) | Y |  |  |

**PK**: VALID_INICIAL, GRUPO_VEIC_TRANSP, COD_VEIC_TRANSP, COD_MODULO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_VEIC_TRANSP_OBRIG → PRT_VEIC_TRANSP_OBRIG(IDENT_VEIC_TRANSP_OBRIG)

---

## PRT_VEIC_TRANSP_OBRIG
**Comment**: Tabela de Cadastro de Veiculo de Transporte das Obrigacoes - TFIX118

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_VEIC_TRANSP_OBRIG | NUMBER(12) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | COD_VEIC_TRANSP_OBRIG | VARCHAR2(10) | N |  |  |
| 4 | TP_VEIC_TRANSP_OBRIG | CHAR(1) | N |  |  |
| 5 | VALID_INI_VEIC_TRANSP_OBRIG | DATE | N |  |  |
| 6 | VALID_FIM_VEIC_TRANSP_OBRIG | DATE | Y |  |  |
| 7 | DSC_VEIC_TRANSP_OBRIG | VARCHAR2(60) | Y |  |  |
| 8 | DSC_TP_VEIC_TRANSP_OBRIG | VARCHAR2(60) | Y |  |  |

**PK**: IDENT_VEIC_TRANSP_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

**Indexes**:
- UK_PRT_VEIC_TRANSP_OBRIG (UNIQUE): (COD_MODULO, COD_VEIC_TRANSP_OBRIG, TP_VEIC_TRANSP_OBRIG, VALID_INI_VEIC_TRANSP_OBRIG)

---

## PRT_VERSO_INF_REND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DSC_FUNDO_FOLHA | VARCHAR2(70) | Y |  | Texto para impressÃ£o no fundo da folha. |
| 4 | IND_COR_FUNDO | CHAR(1) | Y | 'P' | Cor de fundo do EndereÃ§o do Remetente e DestinatÃ¡rio. DomÃ­nio: P - Preto; B - Branco. |

**PK**: COD_EMPRESA, COD_ESTAB

---

## PRT_VIA_TRANSP_MSAF_OBRIG
**Comment**: Tabela de parametrizacao das Vias de Transporte MasterSAF (x2047_via_transp) por codigos de Vias de Transportes especificos de obrigacoes (PRT_VIA_TRANSP_OBRIG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | DATE | N |  |  |
| 2 | GRUPO_VIA_TRANSP | VARCHAR2(9) | N |  |  |
| 3 | COD_VIA_TRANSPORTE | VARCHAR2(5) | N |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 5 | IDENT_VIA_TRANSP_OBRIG | NUMBER(12) | Y |  |  |
| 6 | IND_SERV_ACORD | CHAR(1) | Y |  |  |

**PK**: VALID_INICIAL, GRUPO_VIA_TRANSP, COD_VIA_TRANSPORTE, COD_MODULO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)
- IDENT_VIA_TRANSP_OBRIG → PRT_VIA_TRANSP_OBRIG(IDENT_VIA_TRANSP_OBRIG)

---

## PRT_VIA_TRANSP_OBRIG
**Comment**: Tabela de Cadastro de Via de Transporte das Obrigacoes - TFIX121

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_VIA_TRANSP_OBRIG | NUMBER(12) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(8) | N |  |  |
| 3 | COD_VIA_TRANSP_OBRIG | VARCHAR2(10) | N |  |  |
| 4 | VALID_INI_VIA_TRANSP_OBRIG | DATE | N |  |  |
| 5 | VALID_FIM_VIA_TRANSP_OBRIG | DATE | Y |  |  |
| 6 | DSC_VIA_TRANSP_OBRIG | VARCHAR2(60) | Y |  |  |

**PK**: IDENT_VIA_TRANSP_OBRIG

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

**Indexes**:
- UK_PRT_VIA_TRANSP_OBRIG (UNIQUE): (COD_MODULO, COD_VIA_TRANSP_OBRIG, VALID_INI_VIA_TRANSP_OBRIG)

---

