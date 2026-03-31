# Módulo: EFT (EFT) - 41 tabelas

## EFT_CARTA_CORR_RF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_NOTA | VARCHAR2(12) | N |  |  |
| 2 | SERIE_NOTA | VARCHAR2(3) | N |  |  |
| 3 | SUBSERIE_NOTA | VARCHAR2(2) | N |  |  |
| 4 | NUM_NOTIFICACAO | VARCHAR2(12) | N |  |  |
| 5 | DATA_NOTIFICACAO | DATE | N |  |  |
| 6 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 7 | COD_ESTABELECIMENTO | VARCHAR2(6) | N |  |  |
| 8 | COD_RETIFICACAO | VARCHAR2(2) | N |  |  |
| 9 | SEQ | NUMBER(2) | N |  |  |
| 10 | DESC_RETIFICACAO | VARCHAR2(45) | Y |  |  |
| 11 | TIPO_CARTA | VARCHAR2(1) | Y |  |  |
| 12 | DESC_CODIGO | VARCHAR2(40) | Y |  |  |
| 13 | DATA_ENCERRAMENTO | DATE | Y |  |  |
| 14 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 15 | EMISSAO_NOTA | DATE | Y |  |  |

**PK**: NUM_NOTA, SERIE_NOTA, SUBSERIE_NOTA, NUM_NOTIFICACAO, DATA_NOTIFICACAO, COD_EMPRESA, COD_ESTABELECIMENTO, COD_RETIFICACAO, SEQ

---

## EFT_CARTA_RF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | REGULARIZACAO | VARCHAR2(12) | N |  |  |
| 2 | ANO_REGULARIZACAO | VARCHAR2(4) | N |  |  |
| 3 | USUARIO | VARCHAR2(40) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUBSERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | DATA_EMISSAO | DATE | Y |  |  |
| 10 | VALOR_TOTAL | NUMBER(17,2) | Y |  |  |
| 11 | BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 13 | VALOR_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | STATUS_CARTA | VARCHAR2(1) | Y |  |  |
| 15 | CGC_FORNECEDOR | VARCHAR2(14) | Y |  |  |
| 16 | OBSERVACAO | VARCHAR2(100) | Y |  |  |
| 17 | DATA_EMISSAO_NF | DATE | Y |  |  |
| 18 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 19 | CONTA_CONTABIL | VARCHAR2(20) | Y |  |  |
| 20 | COD_CFOP | VARCHAR2(6) | Y |  |  |
| 21 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 22 | BASE_IPI | NUMBER(17,2) | Y |  |  |
| 23 | ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 24 | VALOR_IPI | NUMBER(17,2) | Y |  |  |
| 25 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, REGULARIZACAO, ANO_REGULARIZACAO, USUARIO

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1325: (IDENT_FIS_JUR)

---

## EFT_CATEG_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CATEGORIA_ICMS | VARCHAR2(14) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(40) | Y |  |  |
| 3 | TIPO_TRIBUT_ICMS | CHAR(1) | Y |  |  |
| 4 | TEXTO_LEGAL | VARCHAR2(5) | Y |  |  |
| 5 | SIT_TRIB_ORIGEM | CHAR(1) | Y |  |  |
| 6 | ORIGEM | CHAR(1) | Y |  |  |
| 7 | PRODUTO_NACIONAL | CHAR(1) | Y |  |  |

**PK**: CATEGORIA_ICMS

---

## EFT_CATEG_ICMS_CPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CATEGORIA_ICMS | VARCHAR2(14) | N |  |  |
| 2 | UF_ORIGEM | VARCHAR2(2) | N |  |  |
| 3 | UF_DESTINO | VARCHAR2(2) | N |  |  |
| 4 | ALIQ_ICMS | NUMBER(5,2) | Y |  |  |
| 5 | REDUCAO_BASE | NUMBER(5,2) | Y |  |  |
| 6 | VALIDADE_REDUCAO | DATE | Y |  |  |
| 7 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |

**PK**: CATEGORIA_ICMS, UF_ORIGEM, UF_DESTINO

---

## EFT_CLASSIF_CONTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NORM_DEV | CHAR(1) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUBSERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | CENTRO_CUSTO | VARCHAR2(50) | N |  |  |
| 12 | CONTA_CONTABIL | VARCHAR2(20) | N |  |  |
| 13 | NUM_COLUNA | NUMBER(3) | N |  |  |
| 14 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 15 | NUM_ITEM | NUMBER(17) | Y |  |  |
| 16 | HISTORICO | VARCHAR2(40) | Y |  |  |
| 17 | VALOR | NUMBER(13,2) | Y |  |  |
| 18 | CAMPO | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, DATA_FISCAL, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUBSERIE_DOCFIS, CENTRO_CUSTO, CONTA_CONTABIL, NUM_COLUNA

---

## EFT_CODIGO_DCR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CODIGO | VARCHAR2(10) | N |  |  |
| 2 | NUMERO_DCR | VARCHAR2(15) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | INDICE | NUMBER(13,4) | Y |  |  |
| 5 | PESO_LIQUIDO | NUMBER(13,4) | Y |  |  |
| 6 | PESO_BRUTO | NUMBER(13,4) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | DATA_GER | DATE | Y |  |  |

**PK**: CODIGO

---

## EFT_COD_CONTABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CODIGO_CONTABIL | VARCHAR2(20) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | TIPO_CODIGO_CONTABIL | VARCHAR2(1) | Y |  |  |

**PK**: CODIGO_CONTABIL

---

## EFT_COD_CORRECAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CODIGO | NUMBER(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(40) | Y |  |  |

**PK**: CODIGO

---

## EFT_COLUNAS_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_DOCUMENTO | VARCHAR2(2) | N |  |  |
| 2 | NUM_COLUNA | NUMBER(3) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(40) | Y |  |  |
| 4 | TIPO_COLUNA | VARCHAR2(1) | Y |  |  |

**PK**: TIPO_DOCUMENTO, NUM_COLUNA

---

## EFT_COMPL_IMP

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
| 11 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 13 | S_SER_DOCFIS_REF | VARCHAR2(2) | N |  |  |
| 14 | DATA_FISCAL_REF | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, S_SER_DOCFIS_REF, DATA_FISCAL_REF

---

## EFT_CONTABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_DOCUMENTO | VARCHAR2(2) | N |  |  |
| 2 | PERIODO_INICIAL | DATE | N |  |  |
| 3 | PERIODO_FINAL | DATE | N |  |  |
| 4 | DOCUMENTO | VARCHAR2(30) | N |  |  |
| 5 | CONTA_CONTABIL | VARCHAR2(20) | N |  |  |
| 6 | SINAL | CHAR(1) | N |  |  |
| 7 | CENTRO_CUSTO | VARCHAR2(50) | N |  |  |
| 8 | SEQUENCIA | NUMBER(10) | N |  |  |
| 9 | VLR_CONTABIL | NUMBER(13,2) | Y |  |  |
| 10 | HISTORICO | VARCHAR2(100) | Y |  |  |
| 11 | DATA_MOVIMENTO | DATE | Y |  |  |
| 12 | IND_TRANSMISSAO | CHAR(1) | Y |  |  |

**PK**: TIPO_DOCUMENTO, PERIODO_INICIAL, PERIODO_FINAL, DOCUMENTO, CONTA_CONTABIL, SINAL, CENTRO_CUSTO, SEQUENCIA

---

## EFT_DADOS_RF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | REGULARIZACAO | VARCHAR2(12) | N |  |  |
| 4 | ANO_REGULARIZACAO | VARCHAR2(4) | N |  |  |
| 5 | SEQ_REG | NUMBER(5) | N |  |  |
| 6 | USUARIO | VARCHAR2(40) | N |  |  |
| 7 | UNIDADE | VARCHAR2(5) | Y |  |  |
| 8 | QUANTIDADE | NUMBER(17,3) | Y |  |  |
| 9 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 10 | PRECO_UNITARIO | NUMBER(17,2) | Y |  |  |
| 11 | PRECO_TOTAL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, REGULARIZACAO, ANO_REGULARIZACAO, SEQ_REG, USUARIO

---

## EFT_DEV_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NORM_DEV | CHAR(1) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUBSERIE_DOCFIS | CHAR(1) | N |  |  |
| 9 | IDENT_FISJUR | NUMBER(12) | N |  |  |
| 10 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 11 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 13 | SUBSERIE_DOCFIS_REF | VARCHAR2(1) | N |  |  |
| 14 | COD_EMPRESA_REF | VARCHAR2(3) | Y |  |  |
| 15 | COD_ESTAB_REF | VARCHAR2(6) | Y |  |  |
| 16 | MOVTO_E_S_REF | CHAR(1) | Y |  |  |
| 17 | NORM_DEV_REF | CHAR(1) | Y |  |  |
| 18 | DATA_FISCAL_REF | DATE | Y |  |  |
| 19 | IDENT_FISJUR_REF | NUMBER(12) | Y |  |  |
| 20 | IDENT_DOCTO_REF | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUBSERIE_DOCFIS, IDENT_FISJUR, IDENT_DOCTO, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUBSERIE_DOCFIS_REF

---

## EFT_DOCFIS_RF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTABELECIMENTO | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUBSERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 11 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 12 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 13 | CONTA_CONTABIL | VARCHAR2(20) | Y |  |  |
| 14 | DATA_VENCIMENTO | DATE | Y |  |  |
| 15 | SITUACAO | VARCHAR2(1) | Y |  |  |
| 16 | DATA_ALTERACAO | DATE | Y |  |  |
| 17 | ICMS_DEDUZIDO | NUMBER(13,2) | Y |  |  |
| 18 | OBSERVACAO | VARCHAR2(100) | Y |  |  |
| 19 | BS_ICMS_DEST | NUMBER(13,2) | Y |  |  |
| 20 | VLR_ICMS_DEST | NUMBER(13,2) | Y |  |  |
| 21 | ICMS_MAIOR | NUMBER(13,2) | Y |  |  |
| 22 | DEPARTAMENTO | VARCHAR2(3) | Y |  |  |
| 23 | BS_ICMSS_ENT | NUMBER(13,2) | Y |  |  |
| 24 | VLR_ICMSS_ENT | NUMBER(13,2) | Y |  |  |
| 25 | USUARIO | VARCHAR2(40) | Y |  |  |
| 26 | MULT_ALIQ | VARCHAR2(1) | Y |  |  |
| 27 | DIF_ALIQUOTA | NUMBER(13,2) | Y |  |  |
| 28 | DATA_ORIGINAL | DATE | Y |  |  |
| 29 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 30 | DATA_INDICE | DATE | Y |  |  |
| 31 | NUM_FATURA | VARCHAR2(10) | Y |  |  |
| 32 | VLR_INDICE | NUMBER(17,6) | Y |  |  |
| 33 | NUM_PPVI | VARCHAR2(10) | Y |  |  |
| 34 | PRAZO | VARCHAR2(3) | Y |  |  |
| 35 | STATUS | VARCHAR2(3) | Y |  |  |
| 36 | MARCA_SOLICITA_PAG | VARCHAR2(1) | Y |  |  |
| 37 | DATA_APROVACAO | DATE | Y |  |  |
| 38 | LIBERACAO | VARCHAR2(1) | Y |  |  |
| 39 | UNIDADE_NEGOCIO | VARCHAR2(20) | Y |  |  |
| 40 | VLR_FATURA | NUMBER(17,2) | Y |  |  |
| 41 | IND_TP_CALC_SERV | CHAR(1) | Y |  |  |
| 42 | NUM_NOTIF_ZFM | VARCHAR2(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTABELECIMENTO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUBSERIE_DOCFIS

---

## EFT_ESTAB_CPL_E

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SERIE_NOTA | VARCHAR2(3) | N |  |  |
| 4 | ULTIMA_NOTA | VARCHAR2(12) | Y |  |  |
| 5 | DATA_EMISSAO | DATE | Y |  |  |
| 6 | NUM_SELO_FISCAL | VARCHAR2(9) | Y |  |  |
| 7 | SERIE_SELO_FISCAL | VARCHAR2(3) | Y |  |  |
| 8 | COD_MODELO | VARCHAR2(5) | Y |  |  |
| 9 | QTD_MAXIMA_LINHA | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, SERIE_NOTA

**FKs**:
- COD_MODELO → EFT_MODELO_NF(COD_MODELO)

---

## EFT_ESTAB_CPL_RF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTABELECIMENTO | VARCHAR2(6) | Y |  |  |
| 3 | ULTIMA_CARTA | VARCHAR2(12) | Y |  |  |
| 4 | ULT_NF_COMPL | VARCHAR2(12) | Y |  |  |
| 5 | ULT_REGULARIZACAO | VARCHAR2(12) | Y |  |  |
| 6 | ANO_REGULARIZACAO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_REL_DCR | NUMBER(6) | Y |  |  |
| 8 | ANO_REL_DCR | NUMBER(4) | Y |  |  |

**Indexes**:
- P_EFT_ESTAB_CPL_RF (UNIQUE): (COD_EMPRESA, COD_ESTABELECIMENTO)

---

## EFT_ESTAB_CPL_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SERIE_NOTA | VARCHAR2(3) | N |  |  |
| 4 | ULTIMA_NOTA | VARCHAR2(12) | Y |  |  |
| 5 | DATA_EMISSAO | DATE | Y |  |  |
| 6 | NUM_SELO_FISCAL | VARCHAR2(9) | Y |  |  |
| 7 | SERIE_SELO_FISCAL | VARCHAR2(3) | Y |  |  |
| 8 | COD_MODELO | VARCHAR2(5) | Y |  |  |
| 9 | QTD_MAXIMA_LINHA | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, SERIE_NOTA

**FKs**:
- COD_MODELO → EFT_MODELO_NF(COD_MODELO)

---

## EFT_ESTAB_CPL_TRAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_DEST | VARCHAR2(6) | N |  |  |
| 4 | NUM_DIAS_PREV | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_ORIG, COD_ESTAB_DEST

**FKs**:
- COD_EMPRESA, COD_ESTAB_ORIG → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB_DEST → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFT_ESTAB_CTRL_NUM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 6 | DAT_EMISSAO | DATE | Y |  |  |
| 7 | NUM_SELO_FISCAL | VARCHAR2(9) | Y |  |  |
| 8 | SERIE_SELO_FISCAL | VARCHAR2(3) | Y |  |  |
| 9 | COD_MODELO | VARCHAR2(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, SERIE_DOCFIS, MOVTO_E_S

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFT_IMPRESSAO_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | NUM_NOTA | VARCHAR2(12) | N |  |  |
| 5 | SERIE_NOTA | VARCHAR2(3) | N |  |  |
| 6 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 7 | PROGRAMA | VARCHAR2(3) | N |  |  |
| 8 | USUARIO | VARCHAR2(40) | N |  |  |
| 9 | DESCRICAO | VARCHAR2(300) | Y |  |  |
| 10 | SUB_SERIE_NOTA | VARCHAR2(2) | Y |  |  |
| 11 | QUANTIDADE | NUMBER(13,3) | Y |  |  |
| 12 | COD_FISCAL | VARCHAR2(6) | Y |  |  |
| 13 | PRECO | NUMBER(13,4) | Y |  |  |
| 14 | VALOR_MERC | NUMBER(13,2) | Y |  |  |
| 15 | PERC_IPI | NUMBER(13,2) | Y |  |  |
| 16 | VALOR_IPI | NUMBER(13,2) | Y |  |  |
| 17 | CLASS_FISCAL | VARCHAR2(10) | Y |  |  |
| 18 | UN_VENDA | VARCHAR2(3) | Y |  |  |
| 19 | VALOR_TOTAL | NUMBER(13,2) | Y |  |  |
| 20 | CLASS_IPI | VARCHAR2(1) | Y |  |  |
| 21 | ALIQ_IPI | NUMBER(8,4) | Y |  |  |
| 22 | CLASS_ICMS | VARCHAR2(1) | Y |  |  |
| 23 | ALIQ_ICMS | NUMBER(8,4) | Y |  |  |
| 24 | ICMS_ESPECIAL | NUMBER(8,4) | Y |  |  |
| 25 | ALIQ_INTERNA_ICMS | NUMBER(8,4) | Y |  |  |
| 26 | CLASS_ISS | VARCHAR2(1) | Y |  |  |
| 27 | ALIQ_ISS | NUMBER(8,4) | Y |  |  |
| 28 | VLR_BASE_ISS | NUMBER(13,2) | Y |  |  |
| 29 | PESO_LIQ | NUMBER(15,4) | Y |  |  |
| 30 | PESO_BRUTO | NUMBER(15,4) | Y |  |  |
| 31 | CUBAGEM | NUMBER(13,2) | Y |  |  |
| 32 | SUBST_TRIBUTACAO | VARCHAR2(6) | Y |  |  |
| 33 | ORIGEM | VARCHAR2(1) | Y |  |  |
| 34 | MARGEM | NUMBER(5,2) | Y |  |  |
| 35 | TIPO_BASE | VARCHAR2(1) | Y |  |  |
| 36 | TIPO_CALCULO | VARCHAR2(1) | Y |  |  |
| 37 | COD_SITUACAO_A | VARCHAR2(1) | Y |  |  |
| 38 | PRECO_SUGERIDO | NUMBER(13,2) | Y |  |  |
| 39 | CUSTO_MEDIO | NUMBER(13,2) | Y |  |  |
| 40 | PRECO_ULT_ENTRADA | NUMBER(13,2) | Y |  |  |
| 41 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 42 | STATUS | VARCHAR2(1) | Y |  |  |
| 43 | IMPRESSO | VARCHAR2(1) | Y |  |  |
| 44 | BS_ICMS_TXT | VARCHAR2(15) | Y |  |  |
| 45 | ICMS_ENT | NUMBER(13,2) | Y |  |  |
| 46 | ICMSS_ENT | NUMBER(13,2) | Y |  |  |
| 47 | REDUCAO_ICMS | NUMBER(13,2) | Y |  |  |
| 48 | BS_IPI_TXT | VARCHAR2(15) | Y |  |  |
| 49 | PV_TXT | VARCHAR2(15) | Y |  |  |
| 50 | DESCONTO | NUMBER(13,2) | Y |  |  |
| 51 | UN_TRANSPORTE | VARCHAR2(3) | Y |  |  |
| 52 | VOL_CONVER | NUMBER(13,3) | Y |  |  |
| 53 | COD_PROJETO | VARCHAR2(10) | Y |  |  |
| 54 | UNIDADE_NEGOCIO | VARCHAR2(20) | Y |  |  |
| 55 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 56 | COD_CFOP | VARCHAR2(6) | Y |  |  |
| 57 | COD_CONTABIL | VARCHAR2(20) | Y |  |  |
| 58 | PRODUTO_X08 | VARCHAR2(20) | Y |  |  |
| 59 | DESCRICAO2 | VARCHAR2(50) | Y |  |  |
| 60 | TIPO_SERVICO | VARCHAR2(4) | Y |  |  |
| 61 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 62 | IND_IMPRIME_VLR | CHAR(1) | Y |  |  |
| 63 | IND_SERV_MERC | CHAR(1) | Y |  |  |
| 64 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 65 | ALIQ_ICMS_NDESTAC | NUMBER(7,4) | Y |  |  |
| 66 | ALIQ_IPI_NDESTAC | NUMBER(7,4) | Y |  |  |
| 67 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 68 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 69 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 70 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 71 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 72 | TEXTO_LEGAL_IPI | VARCHAR2(120) | Y |  |  |
| 73 | TEXTO_LEGAL_CATEG | VARCHAR2(120) | Y |  |  |
| 74 | IDENT_FEDERAL | NUMBER(12) | Y |  |  |
| 75 | TEXTO_LEGAL_CATST | VARCHAR2(120) | Y |  |  |
| 76 | COMPL_ISENCAO | VARCHAR2(5) | Y |  |  |
| 77 | NUM_ITEM | NUMBER(5) | N | 99999 |  |
| 78 | IND_MOV_FIS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PRODUTO, NUM_NOTA, SERIE_NOTA, MOVTO_E_S, PROGRAMA, USUARIO, NUM_ITEM

**FKs**:
- IDENT_FEDERAL → X2044_SIT_TRIB_FED(IDENT_FEDERAL)

---

## EFT_IMPRESSAO_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_NOTA | VARCHAR2(12) | N |  |  |
| 4 | SERIE_NOTA | VARCHAR2(3) | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | PROGRAMA | VARCHAR2(3) | N |  |  |
| 7 | USUARIO | VARCHAR2(40) | N |  |  |
| 8 | ALMOX | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_NOTA | VARCHAR2(2) | Y |  |  |
| 10 | DATA_EMISSAO | DATE | Y |  |  |
| 11 | CONVENIO | VARCHAR2(14) | Y |  |  |
| 12 | DESC_CLI | VARCHAR2(70) | Y |  |  |
| 13 | ENDERECO_CLI | VARCHAR2(50) | Y |  |  |
| 14 | CGC_CLI | VARCHAR2(18) | Y |  |  |
| 15 | INSC_ESTADUAL_CLI | VARCHAR2(14) | Y |  |  |
| 16 | BAIRRO_CLI | VARCHAR2(25) | Y |  |  |
| 17 | CIDADE_CLI | VARCHAR2(30) | Y |  |  |
| 18 | ESTADO_CLI | VARCHAR2(2) | Y |  |  |
| 19 | CEP_CLI | VARCHAR2(10) | Y |  |  |
| 20 | TELEFONE_CLI | VARCHAR2(14) | Y |  |  |
| 21 | DESC_TRANSP | VARCHAR2(70) | Y |  |  |
| 22 | CGC_TRANSP | VARCHAR2(18) | Y |  |  |
| 23 | ENDERECO_TRANSP | VARCHAR2(50) | Y |  |  |
| 24 | CIDADE_TRANSP | VARCHAR2(30) | Y |  |  |
| 25 | EMITENTE_DESTINATARIO | VARCHAR2(1) | Y |  |  |
| 26 | ESTADO_TRANSP | VARCHAR2(2) | Y |  |  |
| 27 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 28 | PESO_BRUTO_TOTAL | NUMBER(13,3) | Y |  |  |
| 29 | PESO_LIQUIDO_TOTAL | NUMBER(13,3) | Y |  |  |
| 30 | BASE_ICMS | NUMBER(13,2) | Y |  |  |
| 31 | VALOR_ICMS | NUMBER(13,2) | Y |  |  |
| 32 | BASE_ICMS_SUBST | NUMBER(13,2) | Y |  |  |
| 33 | VALOR_ICMS_SUBST | NUMBER(13,2) | Y |  |  |
| 34 | VALOR_TOTAL_ITENS | NUMBER(13,2) | Y |  |  |
| 35 | VALOR_FRETE | NUMBER(13,2) | Y |  |  |
| 36 | VALOR_SEGURO | NUMBER(13,2) | Y |  |  |
| 37 | VALOR_OUTROS | NUMBER(13,2) | Y |  |  |
| 38 | VALOR_IPI_TOTAL | NUMBER(13,2) | Y |  |  |
| 39 | VALOR_TOTAL_NOTA | NUMBER(13,2) | Y |  |  |
| 40 | TEXTO_LEGAL | VARCHAR2(300) | Y |  |  |
| 41 | TEXTO_LEGAL_FAT | VARCHAR2(120) | Y |  |  |
| 42 | TEXTO_LEGAL_CATEGORIA | VARCHAR2(120) | Y |  |  |
| 43 | QUANTIDADE | NUMBER(13,3) | Y |  |  |
| 44 | ESPECIE | VARCHAR2(15) | Y |  |  |
| 45 | LOJA | VARCHAR2(10) | Y |  |  |
| 46 | DEPARTAMENTO | VARCHAR2(5) | Y |  |  |
| 47 | CFOP | VARCHAR2(6) | Y |  |  |
| 48 | NAT_OP | VARCHAR2(3) | Y |  |  |
| 49 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 50 | IMPRESSO | VARCHAR2(1) | Y |  |  |
| 51 | VLR_ICMS_DEST | VARCHAR2(40) | Y |  |  |
| 52 | BS_ICMS_DEST | VARCHAR2(40) | Y |  |  |
| 53 | VLR_ICMS_DEDUZIDO | VARCHAR2(40) | Y |  |  |
| 54 | VLR_ICMSS_TXT | VARCHAR2(40) | Y |  |  |
| 55 | BS_ICMSS_TXT | VARCHAR2(40) | Y |  |  |
| 56 | EXTERIOR_TXT | VARCHAR2(60) | Y |  |  |
| 57 | VOLUME | NUMBER(13,3) | Y |  |  |
| 58 | COD_CFOP | VARCHAR2(6) | Y |  |  |
| 59 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 60 | DATA_VENCIMENTO | DATE | Y |  |  |
| 61 | ALIQ_ISS | NUMBER(8,4) | Y |  |  |
| 62 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 63 | ALIQ_INSS | NUMBER(8,4) | Y |  |  |
| 64 | VALOR_INSS | NUMBER(17,2) | Y |  |  |
| 65 | ALIQ_IR | NUMBER(8,4) | Y |  |  |
| 66 | VALOR_IR | NUMBER(17,2) | Y |  |  |
| 67 | INSC_MUNICIPAL_CLI | VARCHAR2(14) | Y |  |  |
| 68 | COD_NAT_SERVICO | VARCHAR2(10) | Y |  |  |
| 69 | DESCR_NAT_SERVICO | VARCHAR2(30) | Y |  |  |
| 70 | IND_SERV_MERC | CHAR(1) | Y |  |  |
| 71 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 72 | NUM_VIA | NUMBER(5) | Y |  |  |
| 73 | OBS_NF | VARCHAR2(400) | Y |  |  |
| 74 | DESC_ENTREGA | VARCHAR2(70) | Y |  |  |
| 75 | ENDERECO_ENTREGA | VARCHAR2(70) | Y |  |  |
| 76 | CGC_ENTREGA | VARCHAR2(18) | Y |  |  |
| 77 | BAIRRO_ENTREGA | VARCHAR2(25) | Y |  |  |
| 78 | CIDADE_ENTREGA | VARCHAR2(30) | Y |  |  |
| 79 | ESTADO_ENTREGA | VARCHAR2(2) | Y |  |  |
| 80 | CEP_ENTREGA | VARCHAR2(10) | Y |  |  |
| 81 | TELEFONE_ENTREGA | VARCHAR2(14) | Y |  |  |
| 82 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 83 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 84 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 85 | DATA_DI | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_NOTA, SERIE_NOTA, MOVTO_E_S, PROGRAMA, USUARIO

---

## EFT_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 13 | IND_PRODUTO | CHAR(1) | N |  |  |
| 14 | NUM_ITEM | NUMBER(5) | N |  |  |
| 15 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,3) | Y |  |  |
| 17 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 19 | PERC_DESCONTO | NUMBER(7,4) | Y |  |  |
| 20 | COD_PROJETO | VARCHAR2(10) | Y |  |  |
| 21 | VLR_PRECO_SUGER | NUMBER(17,2) | Y |  |  |
| 22 | VLR_CUSTO_MEDIO | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ULT_ENTRADA | NUMBER(17,2) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 26 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 27 | DSC_ITEM | VARCHAR2(300) | Y |  |  |
| 28 | IND_ITEM_CAD | CHAR(1) | Y |  |  |
| 29 | QTD_ATENDIDA | NUMBER(17,3) | Y |  |  |
| 30 | QTD_ATENDER | NUMBER(17,3) | Y |  |  |
| 31 | VLR_UNIT_ATEND | NUMBER(17,3) | Y |  |  |
| 32 | VLR_DESCONTO_ATEND | NUMBER(17,3) | Y |  |  |
| 33 | VLR_TOT_ITEM_ATEND | NUMBER(17,2) | Y |  |  |
| 34 | VLR_PRECO_SUGER_AT | NUMBER(17,2) | Y |  |  |
| 35 | VLR_CUSTO_MEDIO_AT | NUMBER(17,2) | Y |  |  |
| 36 | VLR_ULT_ENTRADA_AT | NUMBER(17,2) | Y |  |  |
| 37 | ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 38 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 39 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 40 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 41 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 42 | COD_AMPARO | VARCHAR2(10) | Y |  |  |
| 43 | COD_AMPAROST | VARCHAR2(10) | Y |  |  |
| 44 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 45 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 46 | IND_MOV_FIS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_FIS_JUR, IND_FIS_JUR, COD_DOCTO, COD_PRODUTO, IND_PRODUTO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_FIS_JUR, IND_FIS_JUR, COD_DOCTO → EFT_NF(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_FIS_JUR, IND_FIS_JUR, COD_DOCTO)

---

## EFT_ITENS_RF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOC_FIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 14 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 15 | COD_CFOP | VARCHAR2(4) | Y |  |  |
| 16 | REFERENCIA_CONTABIL | VARCHAR2(20) | Y |  |  |
| 17 | COD_CONTABIL | VARCHAR2(20) | Y |  |  |
| 18 | COD_PROJETO | VARCHAR2(10) | Y |  |  |
| 19 | NUM_ORDEM_COMPRA | VARCHAR2(12) | Y |  |  |
| 20 | NUMERO_LOTE | NUMBER(10) | Y |  |  |
| 21 | DIF_ALIQUOTA | NUMBER(15,2) | Y |  |  |
| 22 | DESCRICAO_ITEM | VARCHAR2(300) | Y |  |  |
| 23 | DIVISAO | VARCHAR2(10) | Y |  |  |
| 24 | INDICA_NOTA_SERVICO | VARCHAR2(1) | Y |  |  |
| 25 | UNIDADE_NEGOCIO | VARCHAR2(20) | Y |  |  |
| 26 | TIPO_SERVICO | VARCHAR2(4) | Y |  |  |
| 27 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 28 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 29 | IND_MOV_FIS | CHAR(1) | Y |  | Indicador de Movimentação Física |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOC_FIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, NUM_ITEM

---

## EFT_MODELO_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODELO | VARCHAR2(5) | N |  |  |
| 2 | DSC_MODELO_NF | VARCHAR2(50) | Y |  |  |
| 3 | IND_SERV_MERC | CHAR(1) | Y |  |  |

**PK**: COD_MODELO

---

## EFT_MODELO_NF_CPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODELO | VARCHAR2(5) | N |  |  |
| 2 | NUM_LIN_DATWIN | NUMBER(4) | N |  |  |
| 3 | DSC_LIN_DATWIN | VARCHAR2(2000) | Y |  |  |

**PK**: COD_MODELO, NUM_LIN_DATWIN

---

## EFT_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 12 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 13 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 14 | COD_PRAZO | VARCHAR2(3) | Y |  |  |
| 15 | COD_UNID_NEGOC | VARCHAR2(20) | Y |  |  |
| 16 | COD_FISJUR_TRANSP | VARCHAR2(14) | Y |  |  |
| 17 | IND_FISJUR_TRANSP | CHAR(1) | Y |  |  |
| 18 | COD_VIA_TRANSPORTE | VARCHAR2(5) | Y |  |  |
| 19 | IND_EMITE_DEST | CHAR(1) | Y |  |  |
| 20 | DATA_EMISSAO | DATE | Y |  |  |
| 21 | DATA_REC_SAIDA | DATE | Y |  |  |
| 22 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 25 | TEXTO_LIVRE | VARCHAR2(300) | Y |  |  |
| 26 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 27 | VLR_INDICE | NUMBER(17,6) | Y |  |  |
| 28 | IND_STATUS | CHAR(1) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 30 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 31 | PESO_LIQUIDO | NUMBER(13,3) | Y |  |  |
| 32 | PESO_BRUTO | NUMBER(13,3) | Y |  |  |
| 33 | VOLUME | NUMBER(13,3) | Y |  |  |
| 34 | DAT_PREV_FAT | DATE | Y |  |  |
| 35 | IND_FISJUR_ENTREGA | CHAR(1) | Y |  |  |
| 36 | COD_FISJUR_ENTREGA | VARCHAR2(14) | Y |  |  |
| 37 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 38 | IND_EMIT_TRANSP | CHAR(1) | Y |  |  |
| 39 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 40 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 41 | DATA_DI | VARCHAR2(8) | Y |  |  |
| 42 | NUM_NOTIF_ZFM | VARCHAR2(12) | Y |  |  |
| 43 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 44 | DATA_APROVACAO | DATE | Y |  |  |
| 45 | IND_FATURA | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_FIS_JUR, IND_FIS_JUR, COD_DOCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFT_NF_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ESTABELECIMENTO | VARCHAR2(6) | N |  |  |
| 3 | NUM_CARTA | VARCHAR2(12) | N |  |  |
| 4 | SEQ | NUMBER(6) | N |  |  |
| 5 | DATA | DATE | N |  |  |
| 6 | NUM_DOC_FIS | VARCHAR2(12) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 8 | CONTROLE | VARCHAR2(1) | Y |  |  |
| 9 | SERIE | VARCHAR2(3) | Y |  |  |
| 10 | SUBSERIE | VARCHAR2(2) | Y |  |  |
| 11 | TOTAL_NOTA | NUMBER(10,2) | Y |  |  |
| 12 | EMISSAO_NOTA | DATE | Y |  |  |
| 13 | PEDIDO | VARCHAR2(12) | Y |  |  |
| 14 | DATA_PEDIDO | DATE | Y |  |  |
| 15 | DIVERGENCIA | VARCHAR2(100) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(6) | Y |  |  |
| 17 | UNC | VARCHAR2(5) | Y |  |  |
| 18 | OCORRENCIA | VARCHAR2(40) | Y |  |  |
| 19 | VALOR_CERTO | NUMBER(10,2) | Y |  |  |
| 20 | FATURADO | NUMBER(10,2) | Y |  |  |
| 21 | DIFERENCA | NUMBER(10,2) | Y |  |  |

**PK**: EMPRESA, ESTABELECIMENTO, NUM_CARTA, SEQ, DATA

**Indexes**:
- IN_NF_COMPL: (NUM_DOC_FIS, SERIE, SUBSERIE, EMPRESA, ESTABELECIMENTO)

---

## EFT_PARAM_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 2 | NUM_VIA | NUMBER(5) | N |  |  |
| 3 | DSC_VIA | VARCHAR2(50) | Y |  |  |

**PK**: COD_MUNIC_ISS, NUM_VIA

**FKs**:
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)

---

## EFT_PRAZO_VENC_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PRAZO | VARCHAR2(3) | N |  |  |
| 2 | ATIVO | VARCHAR2(1) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(40) | Y |  |  |
| 5 | PRAZO_MEDIO | NUMBER(3) | Y |  |  |
| 6 | PRAZO_DUPLICATAS | NUMBER(3) | Y |  |  |
| 7 | DESC_PRAZO_DUPLIC | NUMBER(6,3) | Y |  |  |
| 8 | LIVRE_DEBITO | VARCHAR2(1) | Y |  |  |
| 9 | GERA_DUPLIC | VARCHAR2(1) | Y |  |  |
| 10 | DESDOBRA | VARCHAR2(1) | Y |  |  |
| 11 | DESC_ANTEC_PAGTO | NUMBER(6,4) | Y |  |  |
| 12 | GERENCIAL | VARCHAR2(1) | Y |  |  |
| 13 | FINANCIADO | VARCHAR2(1) | Y |  |  |
| 14 | BOLETA | VARCHAR2(1) | Y |  |  |
| 15 | BASE_CALC_VENCTO | VARCHAR2(1) | Y |  |  |
| 16 | TIPO_DATA_TITULO | VARCHAR2(1) | Y |  |  |
| 17 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 18 | TAXA_PRECO | NUMBER(6,4) | Y |  |  |
| 19 | BLOQUEIA_PEDIDO | CHAR(1) | Y |  |  |
| 20 | DESCONTO_VENCIMENTO | NUMBER(5,2) | Y |  |  |

**PK**: PRAZO

---

## EFT_PROJETO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROJETO | VARCHAR2(10) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | VALOR_PROJETO | NUMBER(13,2) | Y |  |  |
| 4 | SALDO_PROJETO | NUMBER(13,2) | Y |  |  |

**PK**: COD_PROJETO

---

## EFT_REF_CONTABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_DOCUMENTO | VARCHAR2(2) | N |  |  |
| 4 | REF_ORIGEM | VARCHAR2(20) | N |  |  |
| 5 | REF_DESTINO | VARCHAR2(20) | N |  |  |
| 6 | REF_OPERACAO | VARCHAR2(20) | N |  |  |
| 7 | REF_PRODUTO | VARCHAR2(20) | N |  |  |
| 8 | NUM_COLUNA | NUMBER(3) | N |  |  |
| 9 | NUM_LANCTO | NUMBER(2) | N |  |  |
| 10 | UNIDADE_NEGOCIO | VARCHAR2(20) | N |  |  |
| 11 | CONTA_CONTABIL | VARCHAR2(20) | Y |  |  |
| 12 | SINAL | CHAR(1) | Y |  |  |
| 13 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 14 | ORIGEM_CONTA | CHAR(1) | Y |  |  |
| 15 | ORIGEM_CENT_CUSTO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_DOCUMENTO, REF_ORIGEM, REF_DESTINO, REF_OPERACAO, REF_PRODUTO, NUM_COLUNA, NUM_LANCTO, UNIDADE_NEGOCIO

**FKs**:
- COD_EMPRESA, COD_ESTAB, TIPO_DOCUMENTO, REF_ORIGEM, REF_DESTINO, REF_OPERACAO, REF_PRODUTO, UNIDADE_NEGOCIO → EFT_REF_DESCRICAO(COD_EMPRESA, COD_ESTAB, TIPO_DOCUMENTO, REF_ORIGEM, REF_DESTINO, REF_OPERACAO, REF_PRODUTO, UNIDADE_NEGOCIO)

---

## EFT_REF_DESCRICAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_DOCUMENTO | VARCHAR2(2) | N |  |  |
| 4 | REF_ORIGEM | VARCHAR2(20) | N |  |  |
| 5 | REF_DESTINO | VARCHAR2(20) | N |  |  |
| 6 | REF_OPERACAO | VARCHAR2(20) | N |  |  |
| 7 | REF_PRODUTO | VARCHAR2(20) | N |  |  |
| 8 | UNIDADE_NEGOCIO | VARCHAR2(20) | N |  |  |
| 9 | DESCRICAO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_DOCUMENTO, REF_ORIGEM, REF_DESTINO, REF_OPERACAO, REF_PRODUTO, UNIDADE_NEGOCIO

---

## EFT_REF_HISTORICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_DOCUMENTO | VARCHAR2(2) | N |  |  |
| 4 | REF_ORIGEM | VARCHAR2(20) | N |  |  |
| 5 | REF_DESTINO | VARCHAR2(20) | N |  |  |
| 6 | REF_OPERACAO | VARCHAR2(20) | N |  |  |
| 7 | REF_PRODUTO | VARCHAR2(20) | N |  |  |
| 8 | NUM_COLUNA | NUMBER(3) | N |  |  |
| 9 | NUM_LANCTO | NUMBER(2) | N |  |  |
| 10 | UNIDADE_NEGOCIO | VARCHAR2(20) | N |  |  |
| 11 | LINHA | NUMBER(2) | N |  |  |
| 12 | CAMPO | NUMBER(3) | Y |  |  |
| 13 | TEXTO | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_DOCUMENTO, REF_ORIGEM, REF_DESTINO, REF_OPERACAO, REF_PRODUTO, NUM_COLUNA, NUM_LANCTO, UNIDADE_NEGOCIO, LINHA

**FKs**:
- COD_EMPRESA, COD_ESTAB, TIPO_DOCUMENTO, REF_ORIGEM, REF_DESTINO, REF_OPERACAO, REF_PRODUTO, NUM_COLUNA, NUM_LANCTO, UNIDADE_NEGOCIO → EFT_REF_CONTABIL(COD_EMPRESA, COD_ESTAB, TIPO_DOCUMENTO, REF_ORIGEM, REF_DESTINO, REF_OPERACAO, REF_PRODUTO, NUM_COLUNA, NUM_LANCTO, UNIDADE_NEGOCIO)

---

## EFT_TIT_PAGAR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | DISCRI_ITEM | NUMBER(32) | N |  |  |
| 11 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 12 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 13 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 14 | DATA_EMISSAO | DATE | Y |  |  |
| 15 | DATA_VENCTO | DATE | Y |  |  |
| 16 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 17 | VLR_MOVTO | NUMBER(17,2) | Y |  |  |
| 18 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 19 | VLR_MOVTO_CONV | NUMBER(18,4) | Y |  |  |
| 20 | VLR_TOT_DOCTO | NUMBER(17,2) | Y |  |  |
| 21 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 22 | NUM_DOC_COMPENS | VARCHAR2(15) | Y |  |  |
| 23 | COD_CENTRO_RESP | NUMBER(12) | Y |  |  |
| 24 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 25 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 26 | COD_RECEITA | VARCHAR2(5) | Y |  |  |
| 27 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 28 | DATA_FATOR_GERADOR | DATE | Y |  |  |
| 29 | DATA_INI_COMPET | DATE | Y |  |  |
| 30 | DATA_FIM_COMPET | DATE | Y |  |  |
| 31 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 32 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 33 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 34 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 35 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IND_FIS_JUR, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## EFT_TIT_RECEBER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | DISCRI_ITEM | NUMBER(32) | N |  |  |
| 11 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 12 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 13 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 14 | DATA_EMISSAO | DATE | Y |  |  |
| 15 | DATA_VENCTO | DATE | Y |  |  |
| 16 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 17 | VLR_MOVTO | NUMBER(17,2) | Y |  |  |
| 18 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 19 | VLR_MOVTO_CONV | NUMBER(18,4) | Y |  |  |
| 20 | VLR_TOT_DOCTO | NUMBER(17,2) | Y |  |  |
| 21 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 22 | NUM_DOCTO_COMPENS | VARCHAR2(15) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IND_FIS_JUR, COD_FIS_JUR, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## EFT_TP_DESTINACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_DESTINACAO | NUMBER(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(20) | Y |  |  |

**PK**: TIPO_DESTINACAO

---

## EFT_TP_TRANSAC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_TRANSACAO | VARCHAR2(5) | N |  |  |
| 2 | NATUREZA_OPERACAO | VARCHAR2(3) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(40) | Y |  |  |
| 4 | SHORTNAME | VARCHAR2(40) | Y |  |  |
| 5 | ATIVO | VARCHAR2(1) | Y |  |  |
| 6 | DATA_MOV | DATE | Y |  |  |

**PK**: TIPO_TRANSACAO

---

## EFT_TRANSITO_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 3 | ESTAB_DEST | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOC_FIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DATA_RECEB_PREV | DATE | Y |  |  |
| 13 | DATA_MOVTO | DATE | Y |  |  |
| 14 | STATUS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, ESTAB_ORIG, ESTAB_DEST, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOC_FIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, ESTAB_DEST → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, ESTAB_ORIG → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFT_TRANS_DEST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_TRANSACAO | VARCHAR2(5) | N |  |  |
| 2 | TIPO_DESTINACAO | NUMBER(2) | N |  |  |
| 3 | VALOR_COMERCIAL | VARCHAR2(1) | Y |  |  |
| 4 | VINCULADO_PEDIDO | VARCHAR2(1) | Y |  |  |
| 5 | SITUACAO_ICMS | VARCHAR2(1) | Y |  |  |
| 6 | TIPO_BASE_ICMS | VARCHAR2(1) | Y |  |  |
| 7 | REDUCAO_ICMS | NUMBER(8,4) | Y |  |  |
| 8 | INCIDE_SUBST_TRIBUTARIA | VARCHAR2(1) | Y |  |  |
| 9 | SITUACAO_IPI | VARCHAR2(1) | Y |  |  |
| 10 | TIPO_BASE_IPI | VARCHAR2(1) | Y |  |  |
| 11 | REDUCAO_IPI | NUMBER(8,4) | Y |  |  |
| 12 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 13 | TEXTO_LEGAL | VARCHAR2(4) | Y |  |  |
| 14 | CFOP | VARCHAR2(4) | Y |  |  |
| 15 | CFOP_S | VARCHAR2(4) | Y |  |  |
| 16 | TIPO_PRECO | VARCHAR2(1) | Y |  |  |
| 17 | ALTERACAO_IMPOSTOS | VARCHAR2(1) | Y |  |  |
| 18 | ATIVO | VARCHAR2(1) | Y |  |  |
| 19 | DATA_MOV | DATE | Y |  |  |
| 20 | TIPO_DOCUMENTO | VARCHAR2(5) | Y |  |  |
| 21 | CFOP2 | NUMBER(1) | Y |  |  |
| 22 | CFOP3 | NUMBER(1) | Y |  |  |
| 23 | CFOP4 | NUMBER(1) | Y |  |  |
| 24 | CFOP5 | NUMBER(1) | Y |  |  |
| 25 | PROCEDE_EXTERIOR | VARCHAR2(1) | Y |  |  |
| 26 | CFOP2_ST | NUMBER(1) | Y |  |  |
| 27 | CFOP3_ST | NUMBER(1) | Y |  |  |
| 28 | CFOP4_ST | NUMBER(1) | Y |  |  |
| 29 | CFOP5_ST | NUMBER(1) | Y |  |  |
| 30 | CFOP_E_ST | VARCHAR2(4) | Y |  |  |
| 31 | CFOP_S_ST | VARCHAR2(4) | Y |  |  |
| 32 | OPERACAO_FISCAL | VARCHAR2(1) | Y |  |  |
| 33 | DIFERENCIAL_ALIQ | VARCHAR2(1) | Y |  |  |
| 34 | ATUALIZA_CUSTO | VARCHAR2(1) | Y |  |  |
| 35 | ATIVO_FIXO | VARCHAR2(1) | Y |  |  |
| 36 | ITEM_CADASTRADO | VARCHAR2(1) | Y |  |  |
| 37 | NOTA_FISCAL_SERVICO | VARCHAR2(1) | Y |  |  |
| 38 | DEVOLUCAO | VARCHAR2(1) | Y |  |  |
| 39 | FUNRURAL | VARCHAR2(1) | Y |  |  |
| 40 | SEST_SENAT | VARCHAR2(1) | Y |  |  |
| 41 | IMPORTACAO | VARCHAR2(1) | Y |  |  |
| 42 | SUBST_TRIB_FRETE | VARCHAR2(1) | Y |  |  |
| 43 | ALIQUOTA_FUNRURAL | NUMBER(8,4) | Y |  |  |
| 44 | ALIQUOTA_SEST | NUMBER(8,4) | Y |  |  |
| 45 | ALIQUOTA_IMP | NUMBER(8,4) | Y |  |  |
| 46 | ALIQUOTA_SUBST | NUMBER(8,4) | Y |  |  |
| 47 | CODIGO_CONTABIL_C | VARCHAR2(20) | Y |  |  |
| 48 | IND_TRANSF | CHAR(1) | Y |  |  |
| 49 | SITUACAO_INSS | NUMBER(1) | Y |  |  |
| 50 | SITUACAO_ISS | NUMBER(1) | Y |  |  |
| 51 | SITUACAO_IRRF | NUMBER(1) | Y |  |  |
| 52 | COD_NAT_SERVICO | VARCHAR2(10) | Y |  |  |
| 53 | DESCR_NAT_SERVICO | VARCHAR2(30) | Y |  |  |
| 54 | DIG_CFO4_E | NUMBER(1) | Y |  |  |
| 55 | DIG_CFO5_E | NUMBER(1) | Y |  |  |
| 56 | DIG_CFO4_S | NUMBER(1) | Y |  |  |
| 57 | DIG_CFO5_S | NUMBER(1) | Y |  |  |
| 58 | DIG_CFO4_E_ST | NUMBER(1) | Y |  |  |
| 59 | DIG_CFO5_E_ST | NUMBER(1) | Y |  |  |
| 60 | DIG_CFO4_S_ST | NUMBER(1) | Y |  |  |
| 61 | DIG_CFO5_S_ST | NUMBER(1) | Y |  |  |
| 62 | IDENT_FEDERAL | NUMBER(12) | Y |  |  |
| 63 | SITUACAO_ICMS_ST | VARCHAR2(1) | Y |  |  |
| 64 | REDUCAO_ICMS_ST | NUMBER(8,4) | Y |  |  |
| 65 | IND_IMP_ICMS | CHAR(1) | Y |  |  |
| 66 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |

**PK**: TIPO_TRANSACAO, TIPO_DESTINACAO

**FKs**:
- IDENT_FEDERAL → X2044_SIT_TRIB_FED(IDENT_FEDERAL)

---

## EFT_TRIB_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TAB_SUBST_TRIB | VARCHAR2(5) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(40) | Y |  |  |
| 3 | ATIVO | VARCHAR2(1) | Y |  |  |

**PK**: TAB_SUBST_TRIB

---

## EFT_TRIB_ST_CPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TAB_SUBST_TRIB | VARCHAR2(5) | N |  |  |
| 2 | UF_ORIGEM | VARCHAR2(2) | N |  |  |
| 3 | UF_DESTINO | VARCHAR2(2) | N |  |  |
| 4 | TIPO_BASE | VARCHAR2(1) | Y |  |  |
| 5 | TIPO_CALCULO | VARCHAR2(1) | Y |  |  |
| 6 | MARGEM | NUMBER(5,2) | Y |  |  |

**PK**: TAB_SUBST_TRIB, UF_ORIGEM, UF_DESTINO

---

