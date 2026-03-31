# Módulo: SCA (SCA) - 18 tabelas

## SCA_ANEXO_A_PF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 6 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 7 | QTD_ESTOQUE_ANT | NUMBER(17,6) | Y |  |  |
| 8 | QTD_PRODUCAO | NUMBER(17,6) | Y |  |  |
| 9 | QTD_TRANSFORMACAO | NUMBER(17,6) | Y |  |  |
| 10 | QTD_UTILIZACAO | NUMBER(17,6) | Y |  |  |
| 11 | QTD_AQUISICAO | NUMBER(17,6) | Y |  |  |
| 12 | QTD_VENDA | NUMBER(17,6) | Y |  |  |
| 13 | QTD_RECICLAGEM | NUMBER(17,6) | Y |  |  |
| 14 | QTD_REAPROVEITADA | NUMBER(17,6) | Y |  |  |
| 15 | QTD_IMPORTACAO | NUMBER(17,6) | Y |  |  |
| 16 | QTD_EXPORTACAO | NUMBER(17,6) | Y |  |  |
| 17 | QTD_PERDA | NUMBER(17,6) | Y |  |  |
| 18 | QTD_EVAPORACAO | NUMBER(17,6) | Y |  |  |
| 19 | QTD_ENTRADA_DIVERSA | NUMBER(17,6) | Y |  |  |
| 20 | QTD_SAIDA_DIVERSA | NUMBER(17,6) | Y |  |  |
| 21 | QTD_ESTOQUE_FIM | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, TIPO_OBRIGACAO, COD_CLASS_PRD

---

## SCA_ANEXO_B_PF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 6 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 7 | DATA_MOVTO | DATE | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | COD_CFO | VARCHAR2(4) | N |  |  |
| 11 | TIPO_OPERACAO | NUMBER(2) | Y |  |  |
| 12 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 13 | IDENT_FIS_JUR_TRANSP | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, TIPO_OBRIGACAO, COD_CLASS_PRD, DATA_MOVTO, NUM_DOCFIS, IDENT_FIS_JUR, COD_CFO

---

## SCA_ANEXO_C_PF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 6 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 7 | DATA_MOVTO | DATE | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | TIPO_OPERACAO | NUMBER(2) | N |  |  |
| 11 | NUM_REG_EXP_IMP | VARCHAR2(15) | N |  |  |
| 12 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 13 | IDENT_FIS_JUR_TRANSP | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, TIPO_OBRIGACAO, COD_CLASS_PRD, DATA_MOVTO, NUM_DOCFIS, IDENT_FIS_JUR, TIPO_OPERACAO, NUM_REG_EXP_IMP

---

## SCA_CLASS_PRD_MES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 4 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 5 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 6 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 7 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 8 | QTD_ESTOQUE_ANT | NUMBER(17,6) | Y |  |  |
| 9 | QTD_AQUISICAO | NUMBER(17,6) | Y |  |  |
| 10 | QTD_IMPORTADA | NUMBER(17,6) | Y |  |  |
| 11 | QTD_PRODUCAO | NUMBER(17,6) | Y |  |  |
| 12 | QTD_CONSUMO | NUMBER(17,6) | Y |  |  |
| 13 | QTD_VENDA | NUMBER(17,6) | Y |  |  |
| 14 | QTD_EXPORTACAO | NUMBER(17,6) | Y |  |  |
| 15 | QTD_EVAPORACAO | NUMBER(17,6) | Y |  |  |
| 16 | QTD_PERDA | NUMBER(17,6) | Y |  |  |
| 17 | QTD_ESTOQUE_FIM | NUMBER(17,6) | Y |  |  |
| 18 | QTD_PRODUCAO_BRUTA | NUMBER(17,6) | Y |  |  |
| 19 | QTD_PRODUCAO_LIQ | NUMBER(17,6) | Y |  |  |
| 20 | QTD_UTLZ_BRUTA | NUMBER(17,6) | Y |  |  |
| 21 | COD_INSCRICAO | VARCHAR2(40) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 23 | USUARIO | VARCHAR2(40) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO, ANO_REFERENCIA, MES_REFERENCIA, COD_CLASS_PRD

---

## SCA_CLASS_PRD_UTIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 4 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 5 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 6 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 7 | COD_UTILIZACAO | VARCHAR2(5) | N |  |  |
| 8 | QTD_UTILIZACAO | NUMBER(17,6) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO, ANO_REFERENCIA, MES_REFERENCIA, COD_CLASS_PRD, COD_UTILIZACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO, ANO_REFERENCIA, MES_REFERENCIA, COD_CLASS_PRD → SCA_CLASS_PRD_MES(COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO, ANO_REFERENCIA, MES_REFERENCIA, COD_CLASS_PRD)

---

## SCA_ESTOQUE_TRIM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 4 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 5 | TRIMESTRE | NUMBER(1) | N |  |  |
| 6 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 7 | IND_PRODUTO | CHAR(1) | N |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 9 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 10 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 11 | QTD_SALDO_ANT | NUMBER(17,6) | Y |  |  |
| 12 | QTD_ENTRADA | NUMBER(17,6) | Y |  |  |
| 13 | QTD_PRODUCAO | NUMBER(17,6) | Y |  |  |
| 14 | QTD_CONSUMO | NUMBER(17,6) | Y |  |  |
| 15 | QTD_SAIDAS | NUMBER(17,6) | Y |  |  |
| 16 | QTD_SALDO_ATU | NUMBER(17,6) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO, ANO_REFERENCIA, TRIMESTRE, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## SCA_ESTOQUE_TRIM_CLASS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 4 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 5 | TRIMESTRE | NUMBER(1) | N |  |  |
| 6 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 7 | DSC_CLASS_PRD | VARCHAR2(50) | Y |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | QTD_SALDO_ANT | NUMBER(17,6) | Y |  |  |
| 10 | QTD_ENTRADA | NUMBER(17,6) | Y |  |  |
| 11 | QTD_CONSUMO | NUMBER(17,6) | Y |  |  |
| 12 | QTD_SAIDAS | NUMBER(17,6) | Y |  |  |
| 13 | QTD_SALDO_ATU | NUMBER(17,6) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO, ANO_REFERENCIA, TRIMESTRE, COD_CLASS_PRD

---

## SCA_ESTOQUE_TRIM_MA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | TRIMESTRE | NUMBER(1) | N |  |  |
| 5 | GRUPO_MARCA_COM | VARCHAR2(9) | N |  |  |
| 6 | COD_MARCA_COM | NUMBER(6) | N |  |  |
| 7 | UF_DESTINO | VARCHAR2(2) | N |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | QTD_PRODUZIDO | NUMBER(17,6) | Y |  |  |
| 10 | QTD_ADQUIRIDO | NUMBER(17,6) | Y |  |  |
| 11 | QTD_IMPORTADO | NUMBER(17,6) | Y |  |  |
| 12 | QTD_COMERC | NUMBER(17,6) | Y |  |  |
| 13 | QTD_ESTOQUE | NUMBER(17,6) | Y |  |  |
| 14 | DATA_FIM_TRIM | DATE | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, TRIMESTRE, GRUPO_MARCA_COM, COD_MARCA_COM, UF_DESTINO

---

## SCA_ESTOQUE_TRIM_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 4 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 5 | TRIMESTRE | NUMBER(1) | N |  |  |
| 6 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | COD_OPER_OBRIG | NUMBER(2) | Y |  |  |
| 10 | DSC_CLASS_PRD | VARCHAR2(50) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 13 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 14 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 15 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 16 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 17 | CIDADE | VARCHAR2(30) | Y |  |  |
| 18 | COD_ESTADO_PAIS | VARCHAR2(3) | Y |  |  |
| 19 | CEP | NUMBER(8) | Y |  |  |
| 20 | QTD_SALDO_ANT | NUMBER(17,6) | Y |  |  |
| 21 | QTD_ENTRADA | NUMBER(17,6) | Y |  |  |
| 22 | QTD_CONSUMO | NUMBER(17,6) | Y |  |  |
| 23 | QTD_SALDO_ATU | NUMBER(17,6) | Y |  |  |
| 24 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 25 | USUARIO | VARCHAR2(40) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | NUM_CR | VARCHAR2(10) | Y |  |  |
| 28 | GUIA_TRAFEGO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO, ANO_REFERENCIA, TRIMESTRE, COD_CLASS_PRD, IDENT_FIS_JUR, NUM_DOCFIS

---

## SCA_IAMOV_FEEMA_MA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | IDENT_MARCA_COM | NUMBER(12) | N |  |  |
| 6 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 7 | IND_PRODUTO | CHAR(1) | N |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 9 | COD_PAIS | VARCHAR2(3) | N |  |  |
| 10 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 11 | COD_ING_ATIVO | VARCHAR2(35) | N |  |  |
| 12 | DSC_ING_ATIVO | VARCHAR2(100) | Y |  |  |
| 13 | QTD_SALDO_INI | NUMBER(17,6) | Y |  |  |
| 14 | QTD_SALDO_FIM | NUMBER(17,6) | Y |  |  |
| 15 | QTD_PRODUCAO | NUMBER(17,6) | Y |  |  |
| 16 | QTD_COMPRA_NAC | NUMBER(17,6) | Y |  |  |
| 17 | QTD_COMPRA_EXT | NUMBER(17,6) | Y |  |  |
| 18 | QTD_VENDA_INDUST | NUMBER(17,6) | Y |  |  |
| 19 | QTD_VENDA_CLIENTE | NUMBER(17,6) | Y |  |  |
| 20 | QTD_VENDA_EXT | NUMBER(17,6) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MARCA_COM, MES_REF, ANO_REF, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_PAIS, COD_ESTADO, COD_ING_ATIVO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SCA_IBAMA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 5 | DSC_UTILIZACAO | VARCHAR2(50) | Y |  |  |
| 6 | QTD_CONSUMO | NUMBER(17,6) | Y |  |  |
| 7 | QTD_SALDO_ATU | NUMBER(17,6) | Y |  |  |
| 8 | OBS1 | VARCHAR2(50) | Y |  |  |
| 9 | OBS2 | VARCHAR2(50) | Y |  |  |
| 10 | COD_INSCRICAO | VARCHAR2(40) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, COD_CLASS_PRD

---

## SCA_NFMOV_ANEXO5

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DATA_MOVTO | DATE | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 13 | TIPO_OPERACAO | NUMBER(2) | Y |  |  |
| 14 | QTD_SALDO_INI | NUMBER(17,6) | Y |  |  |
| 15 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 16 | QTD_SALDO_FIM | NUMBER(17,6) | Y |  |  |
| 17 | NUM_SEQUENCIA | NUMBER(5) | Y |  |  |
| 18 | NUM_RECEITA | NUMBER(15) | Y |  |  |
| 19 | DSC_PROD | VARCHAR2(50) | Y |  |  |
| 20 | DSC_ING_ATIVO | VARCHAR2(100) | Y |  |  |
| 21 | NUM_REGISTRO | NUMBER(10) | Y |  |  |
| 22 | DSC_ORG_FED | VARCHAR2(40) | Y |  |  |
| 23 | DSC_CONCENTRACAO | VARCHAR2(15) | Y |  |  |
| 24 | DSC_FORMULACAO | VARCHAR2(40) | Y |  |  |
| 25 | PESO_VOLUME | VARCHAR2(20) | Y |  |  |
| 26 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 27 | USUARIO | VARCHAR2(40) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_MOVTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1712: (IDENT_FIS_JUR)

---

## SCA_PRMOV_ANEXO4

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | QTD_MOVTO_VENDA | NUMBER(17,6) | Y |  |  |
| 10 | QTD_SALDO_FIM | NUMBER(17,6) | Y |  |  |
| 11 | DSC_PROD | VARCHAR2(50) | Y |  |  |
| 12 | DSC_ORG_FED | VARCHAR2(40) | Y |  |  |
| 13 | DSC_CONCENTRACAO | VARCHAR2(15) | Y |  |  |
| 14 | DSC_FORMULACAO | VARCHAR2(40) | Y |  |  |
| 15 | PESO_VOLUME | VARCHAR2(20) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SCA_PRMOV_FEEMA_MA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | IDENT_MARCA_COM | NUMBER(12) | N |  |  |
| 6 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 7 | IND_PRODUTO | CHAR(1) | N |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 9 | COD_PAIS | VARCHAR2(3) | N |  |  |
| 10 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 11 | DSC_PROD | VARCHAR2(50) | Y |  |  |
| 12 | QTD_SALDO_INI | NUMBER(17,6) | Y |  |  |
| 13 | QTD_SALDO_FIM | NUMBER(17,6) | Y |  |  |
| 14 | QTD_PRODUCAO | NUMBER(17,6) | Y |  |  |
| 15 | QTD_COMPRA_NAC | NUMBER(17,6) | Y |  |  |
| 16 | QTD_COMPRA_EXT | NUMBER(17,6) | Y |  |  |
| 17 | QTD_VENDA_INDUST | NUMBER(17,6) | Y |  |  |
| 18 | QTD_VENDA_CLIENTE | NUMBER(17,6) | Y |  |  |
| 19 | QTD_VENDA_EXT | NUMBER(17,6) | Y |  |  |
| 20 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IDENT_MARCA_COM, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_PAIS, COD_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SCA_RE_ESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DSC_CLASS_PRD | VARCHAR2(50) | Y |  |  |
| 9 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 10 | DSC_GRUPO_ANVISA | VARCHAR2(50) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | QTD_SALDO_INI | NUMBER(17,6) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APUR, COD_CLASS_PRD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**Indexes**:
- IX_SCA_RE_ESTOQUE: (DATA_APUR, COD_ESTAB, COD_EMPRESA, DSC_GRUPO_ANVISA)

---

## SCA_RE_MOVTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | NUM_SEQ_LINHA | NUMBER(12) | N |  |  |
| 9 | DATA_MOVTO | DATE | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 13 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 14 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 15 | DSC_CLASS_PRD | VARCHAR2(50) | Y |  |  |
| 16 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 17 | DSC_GRUPO_ANVISA | VARCHAR2(50) | Y |  |  |
| 18 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 19 | QTD_SALDO_INI | NUMBER(17,6) | Y |  |  |
| 20 | QTD_ENTRADA | NUMBER(17,6) | Y |  |  |
| 21 | QTD_SAIDA | NUMBER(17,6) | Y |  |  |
| 22 | QTD_PERDA | NUMBER(17,6) | Y |  |  |
| 23 | QTD_SALDO_FIM | NUMBER(17,6) | Y |  |  |
| 24 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 25 | USUARIO | VARCHAR2(40) | Y |  |  |
| 26 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APUR, COD_CLASS_PRD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, NUM_SEQ_LINHA

**Indexes**:
- IX_SCA_RE_MOVTO: (DATA_APUR, COD_ESTAB, COD_EMPRESA, DSC_GRUPO_ANVISA)

---

## SCA_RE_MOVTO_RMV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DATA_MOVTO | DATE | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 13 | NUM_FAB_LOTE | VARCHAR2(50) | N |  |  |
| 14 | DSC_CLASS_PRD | VARCHAR2(50) | Y |  |  |
| 15 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 16 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 17 | QTD_SAIDA | NUMBER(17,6) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APUR, COD_CLASS_PRD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_MOVTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, NUM_FAB_LOTE

---

## SCA_TERMOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 4 | DSC_ORG_RECEPTOR | VARCHAR2(60) | Y |  |  |
| 5 | IND_RAZAO_SOCIAL | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | COD_INSCRICAO | VARCHAR2(40) | Y |  |  |
| 8 | DAT_VALID_INSCR | DATE | Y |  |  |
| 9 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 10 | COD_RESPONSAVEL2 | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO

---

