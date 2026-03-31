# Módulo: DCT (DCT) - 11 tabelas

## DCT_COMP_DEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | SEQ_CP_DEB | NUMBER(3) | N |  |  |
| 12 | IND_ORIG_CRED | VARCHAR2(2) | Y |  |  |
| 13 | VLR_CP_DEB | NUMBER(17,2) | Y |  |  |
| 14 | IND_TP_PROCESSO | NUMBER(1) | Y |  |  |
| 15 | COD_PROCESSO | VARCHAR2(24) | Y |  |  |
| 16 | IND_MED_JUDIC | NUMBER(1) | Y |  |  |
| 17 | COD_VARA | VARCHAR2(2) | Y |  |  |
| 18 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 19 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 20 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | CNPJ_FONTE_RET_SUC | VARCHAR2(14) | Y |  |  |
| 22 | ANO_RETENCAO | NUMBER(4) | Y |  |  |
| 23 | MES_RETENCAO | NUMBER(2) | Y |  |  |
| 24 | DAT_APUR_SAL_NEG | DATE | Y |  |  |
| 25 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 26 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |
| 27 | ID_QUOTA | NUMBER(2) | N | 0 |  |
| 28 | IND_DIG_CALC | CHAR(1) | Y | '2' |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR, SEQ_CP_DEB

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR → DCT_FICHA_DEB(COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## DCT_COMP_DEB_DARF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | SEQ_CP_DEB_DARF | NUMBER(3) | N |  |  |
| 12 | DAT_APURACAO | DATE | Y |  |  |
| 13 | IND_CPF_CNPJ | CHAR(1) | Y |  |  |
| 14 | CPF_CNPJ_DARF | VARCHAR2(14) | Y |  |  |
| 15 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 16 | DAT_VENCTO | DATE | Y |  |  |
| 17 | NUM_REFERENCIA | VARCHAR2(17) | Y |  |  |
| 18 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 19 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 20 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_CP_DEB | NUMBER(17,2) | Y |  |  |
| 22 | IND_TP_PROCESSO | NUMBER(1) | Y |  |  |
| 23 | COD_PROCESSO | VARCHAR2(24) | Y |  |  |
| 24 | IND_MED_JUDIC | NUMBER(1) | Y |  |  |
| 25 | COD_VARA | VARCHAR2(2) | Y |  |  |
| 26 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 27 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 28 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 29 | DAT_QUITACAO | DATE | Y |  |  |
| 30 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |
| 31 | ID_QUOTA | NUMBER(2) | N | 0 |  |
| 32 | IND_DIG_CALC | CHAR(1) | Y | '2' |  |
| 33 | NRO_REFERENCIA | VARCHAR2(17) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR, SEQ_CP_DEB_DARF

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR → DCT_FICHA_DEB(COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## DCT_DADOS_GERAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO_COMPET | NUMBER(4) | N |  |  |
| 3 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 4 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 5 | COD_ESTAB_MATRIZ | VARCHAR2(6) | Y |  |  |
| 6 | IND_TP_SITUACAO | NUMBER(1) | Y |  |  |
| 7 | ANO_CALEND | NUMBER(4) | Y |  |  |
| 8 | DAT_EVENTO | DATE | Y |  |  |
| 9 | COD_NAT_JUR | NUMBER(4) | Y |  |  |
| 10 | CNAE_FISCAL | NUMBER(7) | Y |  |  |
| 11 | DAT_INI_PERIODO | DATE | Y |  |  |
| 12 | DAT_FIM_PERIODO | DATE | Y |  |  |
| 13 | IND_QUALIF_PFJ | NUMBER(2) | Y |  |  |
| 14 | IND_TRIB_LUCRO | NUMBER(1) | Y |  |  |
| 15 | IND_EXP_PRD_TERC | NUMBER(1) | Y |  |  |
| 16 | IND_CPRES_IPI | NUMBER(1) | Y |  |  |
| 17 | IND_TP_CPRES_IPI | NUMBER(1) | Y |  |  |
| 18 | COD_REPRESENTANTE | VARCHAR2(2) | Y |  |  |
| 19 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 20 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | IND_RETIFIC | CHAR(1) | Y |  |  |
| 22 | IND_TP_CPRES_POST | NUMBER(1) | Y |  |  |
| 23 | IND_VERSAO | NUMBER(2) | Y |  | Assume os valores: 10 - DCTF 1.0 - Trimestral, 20 - DCTF 2.0 - Trimestral, 21 - DCTF 2.1 - Trimestral, 30 - DCTF 3.0 - Trimestral, 40 - DCTF 1.0 - Mensal, 50 - DCTF 1.0 - Semestral, 41- DCTF 1.3 - Mensal |
| 24 | IND_DEB_SCP | CHAR(1) | Y |  |  |
| 25 | IND_OP_RG_ESP_TRIB | CHAR(1) | Y |  |  |
| 26 | IND_PJ_INATIVO | CHAR(1) | Y |  | Usado na DCTF 3.0 trimestral,  DCTF Semestral e na DCTF Mensal 1.3 (2006) |
| 27 | IND_PJ_BALANC_SUSP | CHAR(1) | Y |  |  |
| 28 | IND_MES_BALANC_1 | CHAR(1) | Y |  | Usado na DCTF 3.0 trimestral e DCTF Semestral |
| 29 | IND_MES_BALANC_2 | CHAR(1) | Y |  | Usado na DCTF 3.0 trimestral e DCTF Semestral |
| 30 | IND_MES_BALANC_3 | CHAR(1) | Y |  | Usado na DCTF 3.0 trimestral e DCTF Semestral |
| 31 | NUM_RECIBO_RETIFIC | VARCHAR2(12) | Y |  |  |
| 32 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |
| 33 | IND_DCTF_S_ANO_ANT | CHAR(1) | Y |  | Usado na DCTF Mensal e Semestral |
| 34 | IND_MES_BALANC_4 | CHAR(1) | Y |  | Usado na DCTF Semestral |
| 35 | IND_MES_BALANC_5 | CHAR(1) | Y |  | Usado na DCTF Semestral |
| 36 | IND_MES_BALANC_6 | CHAR(1) | Y |  | Usado na DCTF Semestral |
| 37 | IND_TRIB_LUCRO_2 | NUMBER(1) | Y |  | Usado na DCTF Semestral |
| 38 | IND_DECL_DEFAULT | CHAR(1) | Y | 'N' | Indicador que substituiu a tabela DCT_DECL_DEFAULT. |
| 39 | IND_DEB_INC | CHAR(1) | Y |  |  |
| 40 | IND_INICIO_ATIV_MES_DECL | CHAR(1) | Y |  |  |
| 41 | TP_REC_VAR_MONETARIA | CHAR(1) | Y |  |  |
| 42 | TP_APUR_PIS_PASEP_COFINS | CHAR(1) | Y |  |  |
| 43 | IND_AUSENCIA_DEB_JAN | CHAR(1) | Y |  |  |
| 44 | IND_AUSENCIA_DEB_FEV | CHAR(1) | Y |  |  |
| 45 | IND_AUSENCIA_DEB_MAR | CHAR(1) | Y |  |  |
| 46 | IND_AUSENCIA_DEB_ABR | CHAR(1) | Y |  |  |
| 47 | IND_AUSENCIA_DEB_MAI | CHAR(1) | Y |  |  |
| 48 | IND_AUSENCIA_DEB_JUN | CHAR(1) | Y |  |  |
| 49 | IND_AUSENCIA_DEB_JUL | CHAR(1) | Y |  |  |
| 50 | IND_AUSENCIA_DEB_AGO | CHAR(1) | Y |  |  |
| 51 | IND_AUSENCIA_DEB_SET | CHAR(1) | Y |  |  |
| 52 | IND_AUSENCIA_DEB_OUT | CHAR(1) | Y |  |  |
| 53 | IND_AUSENCIA_DEB_NOV | CHAR(1) | Y |  |  |
| 54 | IND_AUSENCIA_DEB_DEZ | CHAR(1) | Y |  |  |
| 55 | IND_NUM_REF_DARF | CHAR(1) | Y | '0' |  |
| 56 | IND_DEB_SCPINC_R10 | CHAR(1) | Y |  |  |
| 57 | IND_SIT_PJ_DECLARACAO | CHAR(1) | Y |  |  |
| 58 | IND_LEI12973_2014 | CHAR(1) | Y |  |  |
| 59 | IND_OPT_SIMP_NAC | CHAR(1) | Y |  |  |
| 60 | IND_PJ_OPT_CPRB | CHAR(1) | Y |  |  |
| 61 | IND_PJ_INATIVA_MES_DECL | CHAR(1) | Y |  | PJ inativa no mes da declaracao |

**PK**: COD_EMPRESA, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB_MATRIZ → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DCT_DEDUCAO_DARF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | SEQ_DED_DARF | NUMBER(3) | N |  |  |
| 12 | DAT_APURACAO | DATE | Y |  |  |
| 13 | IND_CPF_CNPJ | CHAR(1) | Y |  |  |
| 14 | CPF_CNPJ_DARF | VARCHAR2(14) | Y |  |  |
| 15 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 16 | DAT_VENCTO | DATE | Y |  |  |
| 17 | NUM_REFERENCIA | VARCHAR2(17) | Y |  |  |
| 18 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 19 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 20 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_DEDUZIDO | NUMBER(17,2) | Y |  |  |
| 22 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | DAT_QUITACAO | DATE | Y |  |  |
| 24 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR, SEQ_DED_DARF

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR → DCT_FICHA_DEB(COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR)

---

## DCT_FICHA_DEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | IND_PERIODIC | CHAR(1) | Y |  | Periodicidade do cod_receita |
| 12 | NUM_IMOVEL | NUMBER(8) | Y |  |  |
| 13 | VLR_DEBITO | NUMBER(17,2) | Y |  |  |
| 14 | IND_BALANCO_REDUC | NUMBER(1) | Y |  | Campo Balanço Redução |
| 15 | QTD_QUOTAS | NUMBER(2) | Y |  | Campo Saldo Dividido. Assume os valores: 0 - Sem divisão de quotas, 1 - Com divisão de quotas |
| 16 | STATUS_OPER | CHAR(1) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 20 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |
| 21 | NUM_QUOTAS | NUMBER(2) | Y |  | Campo Quantidade de Quotas. Assume os valores 0, 1, 2. Usado na DCTF Semestral. |
| 22 | DAT_PERIOD_APUR | DATE | Y |  | Utilizado para excluir registros através da rotina de limpeza de movimentos |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR

**FKs**:
- COD_EMPRESA, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE → DCT_DADOS_GERAIS(COD_EMPRESA, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)

---

## DCT_FICHA_DEB_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 12 | NUM_IMOVEL | NUMBER(8) | Y |  |  |
| 13 | VLR_DEBITO | NUMBER(17,2) | Y |  |  |
| 14 | IND_BALANCO_REDUC | NUMBER(1) | Y |  |  |
| 15 | QTD_QUOTAS | NUMBER(2) | Y |  |  |
| 16 | STATUS_OPER | CHAR(1) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | VLR_PG_DEB | NUMBER(17,2) | Y |  | totalizador dos pagamentos referente a ficha de débito |
| 20 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR

---

## DCT_PAGTO_DEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | SEQ_PAGTO_DEB | NUMBER(5) | N |  |  |
| 12 | DAT_APURACAO | DATE | Y |  |  |
| 13 | IND_CPF_CNPJ | CHAR(1) | Y |  |  |
| 14 | CPF_CNPJ_DARF | VARCHAR2(14) | Y |  |  |
| 15 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 16 | DAT_VENCTO | DATE | Y |  |  |
| 17 | NUM_REFERENCIA | VARCHAR2(17) | Y |  |  |
| 18 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 19 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 20 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_PG_DEB | NUMBER(17,2) | Y |  |  |
| 22 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | DAT_QUITACAO | DATE | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y | 0 |  |
| 25 | IND_DIG_CALC | CHAR(1) | Y | '2' |  |
| 26 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |
| 27 | ID_QUOTA | NUMBER(2) | N | 0 |  |
| 28 | NRO_REFERENCIA | VARCHAR2(17) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR, SEQ_PAGTO_DEB

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR → DCT_FICHA_DEB(COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR)

---

## DCT_PAGTO_DEB_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | SEQ_PAGTO_DEB | NUMBER(5) | N |  |  |
| 12 | DAT_APURACAO | DATE | Y |  |  |
| 13 | IND_CPF_CNPJ | CHAR(1) | Y |  |  |
| 14 | CPF_CNPJ_DARF | VARCHAR2(14) | Y |  |  |
| 15 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 16 | DAT_VENCTO | DATE | Y |  |  |
| 17 | NUM_REFERENCIA | VARCHAR2(17) | Y |  |  |
| 18 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 19 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 20 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_PG_DEB | NUMBER(17,2) | Y |  |  |
| 22 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | DAT_QUITACAO | DATE | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |
| 26 | ID_QUOTA | NUMBER(2) | N | 0 |  |
| 27 | NRO_REFERENCIA | VARCHAR2(17) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR, SEQ_PAGTO_DEB

---

## DCT_PARC_DEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | VLR_PARC_DEB | NUMBER(17,2) | Y |  |  |
| 12 | COD_PROCESSO | VARCHAR2(23) | Y |  |  |
| 13 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |
| 15 | IND_FORM_PEDIDO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR → DCT_FICHA_DEB(COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR)

---

## DCT_PG_DEB_TDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | SEQ_PG_DEB_TDA | NUMBER(3) | N |  |  |
| 12 | VLR_PAG_DEB | NUMBER(17,2) | Y |  |  |
| 13 | IND_TP_PROCESSO | NUMBER(1) | Y |  |  |
| 14 | COD_PROCESSO | VARCHAR2(17) | Y |  |  |
| 15 | IND_MED_JUDIC | NUMBER(1) | Y |  |  |
| 16 | COD_VARA | VARCHAR2(2) | Y |  |  |
| 17 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 18 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 19 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR, SEQ_PG_DEB_TDA

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR → DCT_FICHA_DEB(COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## DCT_SUSP_DEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPET | NUMBER(4) | N |  |  |
| 4 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 6 | GRP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | ANO_PERIOD_APUR | NUMBER(4) | N |  |  |
| 9 | MES_PERIOD_APUR | NUMBER(2) | N |  |  |
| 10 | DIA_PERIOD_APUR | NUMBER(2) | N |  |  |
| 11 | SEQ_SUSP_DEB | NUMBER(3) | N |  |  |
| 12 | VLR_SUSP_DEB | NUMBER(17,2) | Y |  |  |
| 13 | COD_PROCESSO | VARCHAR2(24) | Y |  |  |
| 14 | IND_MOT_SUSP | NUMBER(2) | Y |  |  |
| 15 | COD_SECAO | VARCHAR2(2) | Y |  |  |
| 16 | COD_VARA | VARCHAR2(2) | Y |  |  |
| 17 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 18 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 19 | IND_DEPOSITO | NUMBER(1) | Y |  |  |
| 20 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | IND_AUTOR_ACAO | CHAR(1) | Y |  |  |
| 22 | NUM_IDENT_DEP | VARCHAR2(20) | Y |  |  |
| 23 | DAT_APUR_DEP | DATE | Y |  |  |
| 24 | CPF_CNPJ_DEP | VARCHAR2(14) | Y |  |  |
| 25 | COD_RECEITA_DEP | VARCHAR2(4) | Y |  |  |
| 26 | DATA_VENCTO_DEP | DATE | Y |  |  |
| 27 | VLR_PRINCIPAL_DEP | NUMBER(17,2) | Y |  |  |
| 28 | VLR_MULTA_DEP | NUMBER(17,2) | Y |  |  |
| 29 | VLR_JUROS_DEP | NUMBER(17,2) | Y |  |  |
| 30 | IND_PERIODICIDADE | VARCHAR2(2) | N |  | Assume os valores: 'T' - Trimestral, 'M' - Mensal, 'S' - Semestral |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR, SEQ_SUSP_DEB

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR → DCT_FICHA_DEB(COD_EMPRESA, COD_ESTAB, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, GRP_TRIBUTO, COD_RECEITA, ANO_PERIOD_APUR, MES_PERIOD_APUR, DIA_PERIOD_APUR)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

