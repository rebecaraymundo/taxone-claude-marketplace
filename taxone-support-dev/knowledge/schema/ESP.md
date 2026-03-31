# Módulo: ESP (ESP) - 22 tabelas

## ESP_CLA_PARAM_SALDO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | DATA_REFERENCIA | DATE | N |  |  |
| 3 | COD_PARAM | NUMBER(4) | N |  |  |
| 4 | DSC_PARAM | VARCHAR2(20) | Y |  |  |

**PK**: NUM_PROCESSO, DATA_REFERENCIA, COD_PARAM

---

## ESP_CLA_SALDO_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | SEQUENCIA | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | DATA_REFERENCIA | DATE | Y |  |  |
| 6 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 7 | CGC | VARCHAR2(14) | Y |  |  |
| 8 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 9 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 10 | ANO_REGISTRO | NUMBER(4) | Y |  |  |
| 11 | NUM_CIAP | NUMBER(12) | Y |  |  |
| 12 | NUM_OFICIAL_CIAP | VARCHAR2(12) | Y |  |  |
| 13 | DSC_BEM | VARCHAR2(100) | Y |  |  |
| 14 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 15 | COD_INC | VARCHAR2(6) | Y |  |  |
| 16 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 17 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 18 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 19 | DAT_FISCAL | DATE | Y |  |  |
| 20 | DAT_OPERACAO | DATE | Y |  |  |
| 21 | TIPO_MOV | VARCHAR2(3) | Y |  |  |
| 22 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 23 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 24 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_CRED_DIF_ALIQ | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 27 | VLR_DIFAL_FRETE | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 29 | DAT_OPER_BX | DATE | Y |  |  |
| 30 | NUM_DOCFIS_BX | VARCHAR2(12) | Y |  |  |
| 31 | SERIE_DOCFIS_BX | VARCHAR2(3) | Y |  |  |
| 32 | SUB_SERIE_DOCFIS_BX | VARCHAR2(2) | Y |  |  |
| 33 | TIPO_MOV_BX | VARCHAR2(3) | Y |  |  |
| 34 | TIPO_BAIXA | CHAR(1) | Y |  |  |
| 35 | VLR_ESTORNO_ICMS | NUMBER(17,2) | Y |  |  |
| 36 | QTD_BENS_ALIENADOS | NUMBER(17,6) | Y |  |  |
| 37 | VLR_ICMS_BX | NUMBER(17,2) | Y |  |  |
| 38 | VLR_CRED_APROP | NUMBER(17,2) | Y |  |  |
| 39 | NUM_PARCELA | NUMBER(3) | Y |  |  |
| 40 | VLR_CRED_APROP_C | NUMBER(17,2) | Y |  |  |
| 41 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |

**PK**: NUM_PROCESSO, SEQUENCIA

---

## ESP_DF_GIM_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SEQ_GIM | NUMBER(3) | Y |  |  |
| 6 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 7 | IND_TP_GIM | CHAR(1) | Y |  |  |
| 8 | IND_SITUACAO | CHAR(1) | Y |  |  |
| 9 | DSC_INFO_PROG | VARCHAR2(25) | Y |  |  |
| 10 | DSC_OD_OUTROS | VARCHAR2(60) | Y |  |  |
| 11 | DSC_EC_OUTROS | VARCHAR2(60) | Y |  |  |
| 12 | DSC_OC_OUTROS | VARCHAR2(60) | Y |  |  |
| 13 | DSC_ED_OUTROS | VARCHAR2(60) | Y |  |  |
| 14 | DAT_FIM_ATIV | DATE | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## ESP_DF_GIM_RES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | MES_APURACAO | NUMBER(2) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | DAT_GERACAO | DATE | Y |  |  |
| 5 | QTD_DECL_NORM | NUMBER(4) | Y |  |  |
| 6 | QTD_DECL_RET | NUMBER(4) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, MES_APURACAO, ANO_APURACAO

---

## ESP_DF_GIM_RES2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | VLR_TRIB_APUR | NUMBER(17,2) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

---

## ESP_GIA_LINHA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 6 | NUM_LINHA | NUMBER(4) | N |  |  |
| 7 | DSC_LINHA | VARCHAR2(90) | Y |  |  |
| 8 | VLR_LINHA | NUMBER(17,2) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTADO, MES_APURACAO, ANO_APURACAO, NUM_LINHA

---

## ESP_LANCTO_P9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_OBRIG_ACESS | NUMBER(2) | N |  |  |
| 5 | COD_ITEM_APUR_CRED | VARCHAR2(5) | Y |  |  |
| 6 | DSC_APUR_CRED | VARCHAR2(200) | Y |  |  |
| 7 | COD_CLASSE_CRED | VARCHAR2(3) | Y |  |  |
| 8 | COD_ITEM_APUR_DEB | VARCHAR2(5) | Y |  |  |
| 9 | DSC_APUR_DEB | VARCHAR2(200) | Y |  |  |
| 10 | COD_CLASSE_DEB | VARCHAR2(3) | Y |  |  |
| 11 | COD_AMP_DEB | VARCHAR2(10) | Y |  |  |
| 12 | COD_SUB_ITEM_OC_DB | VARCHAR2(2) | Y |  |  |
| 13 | COD_AMP_CRED | VARCHAR2(10) | Y |  |  |
| 14 | COD_SUB_ITEM_OC_CR | VARCHAR2(2) | Y |  |  |
| 15 | COD_AJUSTE_ICMS_DB | VARCHAR2(8) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg E111/E220) -                              referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |
| 16 | COD_AJUSTE_ICMS_CR | VARCHAR2(8) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg E111/E220) -                              referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_TIPO_LIVRO, COD_OBRIG_ACESS

**FKs**:
- COD_AJUSTE_ICMS_DB → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_CR → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ESP_PI_GIM_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_ICMS_NORMAL | VARCHAR2(6) | Y |  |  |
| 6 | COD_ICMSS_ENTR | VARCHAR2(6) | Y |  |  |
| 7 | COD_ICMSS_SAIDA | VARCHAR2(6) | Y |  |  |
| 8 | COD_DIF_ALIQ | VARCHAR2(6) | Y |  |  |
| 9 | COD_ICMS_ANTEC | VARCHAR2(6) | Y |  |  |
| 10 | COD_ICMS_LIVRE1 | VARCHAR2(6) | Y |  |  |
| 11 | COD_ICMS_LIVRE2 | VARCHAR2(6) | Y |  |  |
| 12 | DSC_ICMS_LIVRE1 | VARCHAR2(18) | Y |  |  |
| 13 | DSC_ICMS_LIVRE2 | VARCHAR2(18) | Y |  |  |
| 14 | DAT_ICMS_NORMAL | DATE | Y |  |  |
| 15 | DAT_ICMSS_ENTR | DATE | Y |  |  |
| 16 | DAT_ICMSS_SAIDA | DATE | Y |  |  |
| 17 | DAT_DIF_ALIQ | DATE | Y |  |  |
| 18 | DAT_ICMS_ANTEC | DATE | Y |  |  |
| 19 | DAT_ICMS_LIVRE1 | DATE | Y |  |  |
| 20 | DAT_ICMS_LIVRE2 | DATE | Y |  |  |
| 21 | DAT_ESTOQUE | DATE | Y |  |  |
| 22 | DAT_APRESENT | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ESP_RJ_GIA_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 6 | IND_MOVIMENTO | CHAR(1) | Y |  |  |
| 7 | IND_OFICIO | CHAR(1) | Y |  |  |
| 8 | IND_TIPO_GIA | CHAR(1) | Y |  |  |
| 9 | SEQ_GIA_ICMS | NUMBER(3) | Y |  |  |
| 10 | SEQ_GIA_ICMSS | NUMBER(3) | Y |  |  |
| 11 | VLR_ICMS_PRAZO_ESP | NUMBER(17,2) | Y |  |  |
| 12 | IND_RETIFICADORA | CHAR(1) | Y |  |  |
| 13 | COD_CONTABILISTA | VARCHAR2(2) | Y |  |  |
| 14 | IND_O350006 | CHAR(1) | Y |  |  |
| 15 | IND_O350011 | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONTABILISTA → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## ESP_RJ_GIA_PRZ_ESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ORG_PRAZO_ESP | VARCHAR2(2) | Y |  |  |
| 4 | NUM_PROC_PRZ_ESP | VARCHAR2(8) | Y |  |  |
| 5 | ANO_PRAZO_ESP | NUMBER(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## ESP_RS_GIA_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | DIA_INICIAL_APUR | NUMBER(2) | Y |  |  |
| 6 | DIA_FINAL_APUR | NUMBER(2) | Y |  |  |
| 7 | IND_GIA_SUBSTITUTA | CHAR(1) | Y |  |  |
| 8 | IND_OPER_ICMS_ST | CHAR(1) | Y |  |  |
| 9 | COD_RESPONSAVEL | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ESP_RS_GIA_GER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_GIA_COMPLETA | CHAR(1) | Y |  |  |
| 4 | COD_ENTREGA_GIA | VARCHAR2(6) | Y |  |  |
| 5 | IND_IN_ATV_PERM | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ESP_RS_GIA_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |

**PK**: IDENT_ESTADO, COD_CFO, COD_NATUREZA_OP

---

## ESP_SP_CAT17_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CAE | NUMBER(5) | Y |  | Informacao utilizada no layout da Portaria 63/99. A partir da Portaria 99/2005, o registro 01 nao tem mais o CAE |
| 4 | E_MAIL | VARCHAR2(50) | Y |  |  |
| 5 | SITE | VARCHAR2(40) | Y |  |  |
| 6 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## ESP_SP_CEST_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | VARCHAR2(6) | N |  |  |
| 3 | COD_CEST | VARCHAR2(7) | N |  |  |
| 4 | VALID_INICIAL | DATE | N | TO_DATE('01/01/1900','DD/MM/YYYY') |  |
| 5 | VALID_FINAL | DATE | Y |  |  |
| 6 | ALIQ_INTERNA | NUMBER(7,4) | N |  |  |
| 7 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |
| 8 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_CEST, VALID_INICIAL

---

## ESP_SP_COMPL_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | COD_NATUREZA | VARCHAR2(3) | N |  |  |
| 5 | COD_COMPL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_CFO, COD_NATUREZA

---

## ESP_SP_GIA_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |
| 3 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 4 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |

**PK**: IDENT_ESTADO, COD_CFO

---

## ESP_SP_GIA_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 5 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |

**PK**: IDENT_ESTADO, COD_CFO, COD_NATUREZA_OP

---

## ESP_SP_NBM_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_NBM | VARCHAR2(10) | N |  |  |
| 4 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 5 | VALID_INICIAL | DATE | N | TO_DATE('01/01/1900','DD/MM/YYYY') |  |
| 6 | VALID_FINAL | DATE | Y |  |  |
| 7 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |
| 8 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, COD_NBM, VALID_INICIAL

---

## ESP_SP_PROD_NBM_CEST_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**Indexes**:
- IX_PROD_NBM_CEST_TEMP: (GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)

---

## ESP_SP_PROD_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 6 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 7 | VALID_INICIAL | DATE | N | TO_DATE('01/01/1900','DD/MM/YYYY') |  |
| 8 | MODELO_LIVRO | VARCHAR2(1) | Y | '3' |  |
| 9 | VALID_FINAL | DATE | Y |  |  |
| 10 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |
| 11 | RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 12 | RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 13 | RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 14 | RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 15 | RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 16 | RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 17 | RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 18 | RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 19 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, VALID_INICIAL

**Indexes**:
- IX_ESP_SP_PROD_ST_01: (COD_EMPRESA, IDENT_ESTADO, VALID_INICIAL)

---

## ESP_SP_PROD_ST_ASS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | IND_PRODUTO_ASS | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO_ASS | VARCHAR2(60) | N |  |  |
| 8 | VALID_INICIAL | DATE | N | TO_DATE('01/01/1900','DD/MM/YYYY') |  |

**PK**: COD_EMPRESA, IDENT_ESTADO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, VALID_INICIAL, IND_PRODUTO_ASS, COD_PRODUTO_ASS

**FKs**:
- COD_EMPRESA, IDENT_ESTADO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, VALID_INICIAL → ESP_SP_PROD_ST(COD_EMPRESA, IDENT_ESTADO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, VALID_INICIAL)

---

