# Módulo: SCI (SCI) - 12 tabelas

## SCI_CONF_INSUMO_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | DATA_PRODUTO | DATE | Y |  |  |
| 6 | DESCRICAO_PROD | VARCHAR2(50) | Y |  |  |
| 7 | CLAS_ITEM | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_PRODUTO, COD_PRODUTO

---

## SCI_CONF_INVENT_ESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | QTD_SALDO_INI | NUMBER(17,6) | Y |  |  |
| 6 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 7 | QTD_ENTRADA | NUMBER(17,6) | Y |  |  |
| 8 | VLR_ENTRADA | NUMBER(17,2) | Y |  |  |
| 9 | QTD_SAIDA | NUMBER(17,6) | Y |  |  |
| 10 | VLR_SAIDA | NUMBER(17,2) | Y |  |  |
| 11 | QTD_SALDO_FIM | NUMBER(17,6) | Y |  |  |
| 12 | VLR_SALDO_FIM | NUMBER(17,2) | Y |  |  |
| 13 | QTD_SALDO_CALC | NUMBER(17,6) | Y |  |  |
| 14 | VLR_SALDO_CALC | NUMBER(17,2) | Y |  |  |
| 15 | CLAS_ITEM | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_PRODUTO, COD_PRODUTO

---

## SCI_CONF_LISTA_TEC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | DATA_MOVTO | DATE | N |  |  |
| 6 | IND_PRODUTO_INS | VARCHAR2(1) | N |  |  |
| 7 | COD_PRODUTO_INS | VARCHAR2(60) | N |  |  |
| 8 | NUM_SEQ | NUMBER(2) | N |  |  |
| 9 | DESCRICAO_PROD | VARCHAR2(50) | Y |  |  |
| 10 | DESCRICAO_INS | VARCHAR2(50) | Y |  |  |
| 11 | CLAS_ITEM | NUMBER(2) | Y |  |  |
| 12 | CLAS_ITEM_INS | NUMBER(2) | Y |  |  |
| 13 | DSC_CRITICA | VARCHAR2(200) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_PRODUTO, COD_PRODUTO, DATA_MOVTO, IND_PRODUTO_INS, COD_PRODUTO_INS, NUM_SEQ

---

## SCI_CONF_MOV_NF_ESTOQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TIPO | VARCHAR2(1) | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | DATA_FISCAL | DATE | N |  |  |
| 14 | NUM_ITEM | NUMBER(5) | N |  |  |
| 15 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 16 | IDENT_DOCTO_X10 | NUMBER(12) | N |  |  |
| 17 | DATA_MOVTO | DATE | N |  |  |
| 18 | NUM_DOCFIS_X10 | VARCHAR2(12) | N |  |  |
| 19 | SERIE_DOCFIS_X10 | VARCHAR2(3) | N |  |  |
| 20 | SUB_SERIE_DOCFIS_X10 | VARCHAR2(3) | N |  |  |
| 21 | DISCRI_ESTOQUE | VARCHAR2(52) | N |  |  |
| 22 | DESCRICAO_PROD | VARCHAR2(50) | Y |  |  |
| 23 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 24 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 25 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 26 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 27 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 28 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 29 | QTDE_MOVTO | NUMBER(17,6) | Y |  |  |
| 30 | COD_MEDIDA_X10 | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_TIPO, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, IND_PRODUTO, COD_PRODUTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, NUM_ITEM, GRUPO_CONTAGEM, IDENT_DOCTO_X10, DATA_MOVTO, NUM_DOCFIS_X10, SERIE_DOCFIS_X10, SUB_SERIE_DOCFIS_X10, DISCRI_ESTOQUE

---

## SCI_CONF_NF_CLAS_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TIPO | VARCHAR2(1) | N |  |  1 - NF x Classificacao de Produto, 2 - Compras x Insumo |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | DATA_FISCAL | DATE | N |  |  |
| 14 | NUM_ITEM | NUMBER(5) | N |  |  |
| 15 | DESCRICAO_PROD | VARCHAR2(50) | Y |  |  |
| 16 | CLAS_ITEM | NUMBER(2) | Y |  |  |
| 17 | COD_CFO | VARCHAR2(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_TIPO, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, IND_PRODUTO, COD_PRODUTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, NUM_ITEM

---

## SCI_CONF_PRODUCAO_LISTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_OP | VARCHAR2(30) | N |  |  |
| 4 | COD_DIF_PRODUCAO | VARCHAR2(15) | N |  |  |
| 5 | DT_INI_OP | DATE | N |  |  |
| 6 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | SEQ_ITEM | NUMBER(10) | N |  |  |
| 9 | COD_UN_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 10 | QTD_PRODUZIDO | NUMBER(17,6) | Y |  |  |
| 11 | DATA_LISTA_TEC | DATE | Y |  |  |
| 12 | COD_UN_MEDIDA_LIST | VARCHAR2(8) | Y |  |  |
| 13 | QTD_FABR | NUMBER(17,6) | Y |  |  |
| 14 | IND_ITEM_PROD | VARCHAR2(1) | Y |  |  |
| 15 | COD_ITEM_PROD | VARCHAR2(60) | Y |  |  |
| 16 | COD_UNID_ITEM | VARCHAR2(8) | Y |  |  |
| 17 | QTD_ITEM_USADO | NUMBER(17,6) | Y |  |  |
| 18 | COD_UNID_ITEM_CONV | VARCHAR2(8) | Y |  |  |
| 19 | QTD_ITEM_USADO_CONV | NUMBER(17,6) | Y |  |  |
| 20 | COD_UNID_ITEM_NECES | VARCHAR2(8) | Y |  |  |
| 21 | QTD_ITEM_USADO_NECES | NUMBER(17,6) | Y |  |  |
| 22 | IND_SUBST | VARCHAR2(1) | Y |  |  |
| 23 | IND_ITEM_SUBST | VARCHAR2(1) | Y |  |  |
| 24 | COD_ITEM_SUBST | VARCHAR2(35) | Y |  |  |
| 25 | DSC_DIVERGENCIA | VARCHAR2(255) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_OP, COD_DIF_PRODUCAO, DT_INI_OP, IND_PRODUTO, COD_PRODUTO, SEQ_ITEM

---

## SCI_CONS_PERCENTUAL_PERDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_OP | VARCHAR2(30) | N |  |  |
| 4 | COD_DIF_PRODUCAO | VARCHAR2(15) | N |  |  |
| 5 | DT_INI_OP | DATE | N |  |  |
| 6 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | SEQ_ITEM | NUMBER(10) | N |  |  |
| 9 | COD_UN_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 10 | QTD_PRODUZIDO | NUMBER(17,6) | Y |  |  |
| 11 | DATA_LISTA_TEC | DATE | Y |  |  |
| 12 | COD_UN_MEDIDA_LIST | VARCHAR2(8) | Y |  |  |
| 13 | QTD_FABR | NUMBER(17,6) | Y |  |  |
| 14 | IND_ITEM_PROD | VARCHAR2(1) | Y |  |  |
| 15 | COD_ITEM_PROD | VARCHAR2(60) | Y |  |  |
| 16 | COD_UNID_ITEM | VARCHAR2(8) | Y |  |  |
| 17 | QTD_ITEM_USADO | NUMBER(17,6) | Y |  |  |
| 18 | COD_UNID_ITEM_CONV | VARCHAR2(8) | Y |  |  |
| 19 | QTD_ITEM_USADO_CONV | NUMBER(17,6) | Y |  |  |
| 20 | COD_UNID_ITEM_NECES | VARCHAR2(8) | Y |  |  |
| 21 | QTD_ITEM_USADO_NECES | NUMBER(17,6) | Y |  |  |
| 22 | PERC_PERDA | NUMBER(7,4) | Y |  |  |
| 23 | PERC_VAR_DIF_OCORR | NUMBER(7,4) | Y |  |  |
| 24 | DSC_DIVERGENCIA | VARCHAR2(255) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_OP, COD_DIF_PRODUCAO, DT_INI_OP, IND_PRODUTO, COD_PRODUTO, SEQ_ITEM

---

## SCI_PAR_MOV_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DSC_PERFIL | VARCHAR2(50) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DSC_PERFIL

---

## SCI_PAR_MOV_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSC_PERFIL | VARCHAR2(50) | N |  |  |
| 2 | DSC_RELATORIO | VARCHAR2(120) | Y |  |  |
| 3 | IND_TIPO_DOC | CHAR(1) | Y |  |  |
| 4 | IND_TIPO_MOVTO | CHAR(1) | Y |  |  |
| 5 | IND_TIPO_ENT_1 | CHAR(1) | Y |  |  |
| 6 | IND_TIPO_ENT_2 | CHAR(1) | Y |  |  |
| 7 | IND_TIPO_ENT_3 | CHAR(1) | Y |  |  |
| 8 | IND_TIPO_ENT_4 | CHAR(1) | Y |  |  |
| 9 | IND_TIPO_ENT_5 | CHAR(1) | Y |  |  |
| 10 | IND_TIPO_DATA | CHAR(1) | Y |  |  |
| 11 | IND_SELEC_OPER | CHAR(1) | Y |  |  |

**PK**: DSC_PERFIL

---

## SCI_PAR_MOV_NF_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSC_PERFIL | VARCHAR2(50) | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: DSC_PERFIL, COD_CFO

---

## SCI_PAR_MOV_NF_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSC_PERFIL | VARCHAR2(50) | N |  |  |
| 2 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 3 | COD_OPERACAO | VARCHAR2(6) | N |  |  |

**PK**: DSC_PERFIL, GRUPO_OPERACAO, COD_OPERACAO

---

## SCI_REL_MOV_NF_ESTOQ_QTD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TIPO | VARCHAR2(1) | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | DATA_FISCAL | DATE | N |  |  |
| 14 | NUM_ITEM | NUMBER(5) | N |  |  |
| 15 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 16 | DATA_MOVTO | DATE | N |  |  |
| 17 | DISCRI_ESTOQUE | VARCHAR2(52) | N |  |  |
| 18 | DESCRICAO_PROD | VARCHAR2(50) | Y |  |  |
| 19 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 20 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 21 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 22 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 23 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 24 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 25 | IND_TP_MOVTO | CHAR(1) | Y |  |  |
| 26 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 27 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 28 | COD_MEDIDA_X10 | VARCHAR2(8) | Y |  |  |
| 29 | QTD_CONVERTIDA | NUMBER(17,6) | Y |  |  |
| 30 | IND_SEM_COD_MEDIDA | NUMBER | Y |  |  |
| 31 | IND_ERRO_FATOR_CONV | NUMBER | Y |  |  |
| 32 | COD_USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_TIPO, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, IND_PRODUTO, COD_PRODUTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, NUM_ITEM, GRUPO_CONTAGEM, DATA_MOVTO, DISCRI_ESTOQUE

---

