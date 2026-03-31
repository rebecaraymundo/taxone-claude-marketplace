# Módulo: IST (IST) - 49 tabelas

## IST_APCONT_F4ABAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 5 | COD_CONTRATO | VARCHAR2(14) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | IND_TP_FATUR | CHAR(1) | N |  |  |
| 11 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ISS_ABAT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ISS_ABAT_ACUM | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 17 | DAT_EMISSAO | DATE | Y |  |  |
| 18 | COD_OBRA | VARCHAR2(10) | Y |  |  |
| 19 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_MUNIC_ISS, COD_CONTRATO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TP_FATUR

---

## IST_APURAC_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IND_ENT_SAI_CANC | CHAR(1) | N |  |  |
| 7 | IND_TP_OPERACAO | CHAR(1) | N |  |  |
| 8 | DAT_FISCAL | DATE | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 12 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 13 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 14 | VLR_DOCTO_FISCAL | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 16 | ALIQUOTA_ISS | NUMBER(7,4) | Y |  |  |
| 17 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_OPER_ISENTA | NUMBER(17,2) | Y |  |  |
| 19 | IND_NF_NORM_CANC | CHAR(1) | Y |  |  |
| 20 | VLR_ISS_TERCEIROS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ISS_SUBST_TRIB | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ISSSUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 23 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 24 | COD_NAT_SERV | VARCHAR2(35) | Y |  |  |
| 25 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 26 | USUARIO | VARCHAR2(40) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_MUNICIPIO, DAT_APURACAO, IND_ENT_SAI_CANC, IND_TP_OPERACAO, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, IND_FIS_JUR, COD_FIS_JUR, COD_SERVICO

---

## IST_APUR_F1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IND_TP_SERVICO | CHAR(1) | N |  |  |
| 9 | IND_TP_FATUR | CHAR(1) | N |  |  |
| 10 | DAT_EMISSAO | DATE | Y |  |  |
| 11 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_ISS_BASE1 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ISS_BASE2 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISS_MATERIAL | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ISS_SERVICO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_SUB_EMPREIT | NUMBER(17,2) | Y |  |  |
| 20 | VLR_TOT_ISS | NUMBER(17,2) | Y |  |  |
| 21 | NUM_CONTRATO | VARCHAR2(14) | Y |  |  |
| 22 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 23 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 24 | COD_OBRA | VARCHAR2(10) | Y |  |  |
| 25 | SITUACAO | CHAR(1) | Y |  |  |
| 26 | OBS_NF | VARCHAR2(45) | Y |  |  |
| 27 | STATUS_APROPR | CHAR(1) | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 30 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TP_SERVICO, IND_TP_FATUR

**Indexes**:
- IX_IST_APUR_F1: (COD_MUNIC_ISS)

---

## IST_APUR_F3_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 5 | IND_TP_SERVICO | CHAR(1) | N |  |  |
| 6 | IND_TP_FATUR | CHAR(1) | N |  |  |
| 7 | COD_OBRA | VARCHAR2(10) | N |  |  |
| 8 | VLR_ALIQ_ISS | NUMBER(7,4) | N |  |  |
| 9 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISS_MATERIAL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ISS_SERVICO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SUB_EMPREIT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ISS_SUBEMPR | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_ISS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ISS_RECOLH | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ISS_MES_ANT | NUMBER(17,2) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_MUNIC_ISS, IND_TP_SERVICO, IND_TP_FATUR, COD_OBRA, VLR_ALIQ_ISS

---

## IST_APUR_F3_CONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 5 | NUM_CONTRATO | VARCHAR2(14) | N |  |  |
| 6 | VLR_ISS_SAIDAS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ISS_SUBEMPR | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_MUNIC_ISS, NUM_CONTRATO

---

## IST_APUR_F3_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 5 | IND_TP_SERVICO | CHAR(1) | N |  |  |
| 6 | IND_TP_FATUR | CHAR(1) | N |  |  |
| 7 | COD_OBRA | VARCHAR2(10) | N |  |  |
| 8 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ISS_MATERIAL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ISS_SERVICO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SUB_EMPREIT | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ISS_SUBEMPR | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TOT_ISS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISS_RECOLH | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ISS_N_RECOLH | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ISS_MES_ANT | NUMBER(17,2) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_MUNIC_ISS, IND_TP_SERVICO, IND_TP_FATUR, COD_OBRA

---

## IST_APUR_F4_ABAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | IND_TP_FATUR | CHAR(1) | N |  |  |
| 10 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 12 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ISS_ABAT | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ISS_ABAT_ACUM | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 16 | DAT_EMISSAO | DATE | Y |  |  |
| 17 | NUM_CONTRATO | VARCHAR2(14) | Y |  |  |
| 18 | COD_OBRA | VARCHAR2(10) | Y |  |  |
| 19 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_MUNIC_ISS, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TP_FATUR

---

## IST_APUR_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_ENT_SAI_CANC | CHAR(1) | N |  |  |
| 6 | IND_TP_OPERACAO | CHAR(1) | N |  |  |
| 7 | DAT_FISCAL | DATE | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 13 | VLR_DOCTO_FISCAL | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 15 | ALIQUOTA_ISS | NUMBER(7,4) | Y |  |  |
| 16 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_OPER_ISENTA | NUMBER(17,2) | Y |  |  |
| 18 | IND_NF_NORM_CANC | CHAR(1) | Y |  |  |
| 19 | VLR_ISS_TERCEIROS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ISS_SUBST_TRIB | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ISSSUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 22 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 23 | COD_NAT_SERV | VARCHAR2(35) | Y |  |  |
| 24 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 25 | USUARIO | VARCHAR2(40) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 28 | MODELO_DOCTO | VARCHAR2(2) | Y |  | INFORMAÇÃO DO COD_MODELO DA X2024_MODELO_DOCTO |
| 29 | CPF_CGC_FIS_JUR | VARCHAR2(14) | Y |  | CPF ou CGC da Pessoa Fis Jur da Nota Fiscal |
| 30 | INSC_MUNIC_FIS_JUR | VARCHAR2(14) | Y |  | Inscricao Estadual da Pessoa Fis Jur da Nota Fiscal |
| 31 | COD_MUNIC_PREST_SERV | NUMBER(7) | Y |  | Código do Município que prestou o serviço. |
| 32 | VLR_TOT_DOCTO | NUMBER(17,2) | Y |  | Armazena o Valor total do Documento (Valor Capa - Tratamento para São José dos Campos) |
| 33 | VLR_MAT_APLIC_ISS | NUMBER(17,2) | Y |  |  |
| 34 | VLR_MAT_PROP | NUMBER(17,2) | Y |  |  |
| 35 | VLR_MAT_TERC | NUMBER(17,2) | Y |  |  |
| 36 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 37 | DAT_EMISSAO | DATE | Y |  |  |
| 38 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 39 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 40 | DATA_SAIDA_REC | DATE | Y |  |  |
| 41 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  |  |
| 42 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, IND_ENT_SAI_CANC, IND_TP_OPERACAO, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, IND_FIS_JUR, COD_FIS_JUR, COD_SERVICO

---

## IST_AP_ISS_ST_RS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DSC_MUNIC_PREST | VARCHAR2(50) | Y |  |  |
| 9 | DATA_EMISSAO | DATE | Y |  |  |
| 10 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ALIQ_ISS | NUMBER(7,4) | N |  |  |
| 13 | VLR_TRIB_ISS | NUMBER(17,2) | Y |  |  |
| 14 | DSC_MUNIC_SERV | VARCHAR2(50) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, VLR_ALIQ_ISS

---

## IST_CONTA_CONTRATO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_COMPET | DATE | N |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 5 | COD_CONTRATO | VARCHAR2(14) | N |  |  |
| 6 | VLR_ISS_N_RECOLH | NUMBER(17,2) | Y |  |  |
| 7 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 8 | VLR_ISS_SALDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_COMPET, COD_MUNIC_ISS, COD_CONTRATO

**FKs**:
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)

---

## IST_CONTA_CORR_CRE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_EMISSAO | DATE | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 8 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 10 | VLR_DOCTO_FISCAL | NUMBER(17,2) | Y |  |  |
| 11 | BASE_CALC_TRIB | NUMBER(17,2) | Y |  |  |
| 12 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 13 | ALIQUOTA_ISS | NUMBER(7,4) | Y |  |  |
| 14 | BASE_CALC_ISENTA | NUMBER(17,2) | Y |  |  |
| 15 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 16 | DAT_CONTABILIZ_CRE | DATE | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_EMISSAO, SERIE_DOCFIS, NUM_DOCFIS, COD_SERVICO, IND_FIS_JUR, COD_FIS_JUR

---

## IST_CONTA_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_COMPET | DATE | N |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(12) | N |  |  |
| 5 | VLR_ISS_N_RECOLH | NUMBER(17,2) | Y |  |  |
| 6 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_COMPET, COD_MUNIC_ISS

---

## IST_FATUR_ANTECIP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_GUIA_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 6 | IND_TP_FATUR | CHAR(1) | N |  |  |
| 7 | COD_TP_RECOLH | VARCHAR2(3) | N |  |  |
| 8 | DAT_INI_COMPET | DATE | Y |  |  |
| 9 | DAT_FIM_COMPET | DATE | Y |  |  |
| 10 | VLR_ISS_RECOLH | NUMBER(17,2) | Y |  |  |
| 11 | DAT_VENCTO | DATE | Y |  |  |
| 12 | DAT_RECOLH | DATE | Y |  |  |
| 13 | NUM_GUIA_RECOLH | VARCHAR2(12) | Y |  |  |
| 14 | VLR_PRINC_RECOLH | NUMBER(17,2) | Y |  |  |
| 15 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 17 | VLR_EXTRAS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ABATIDO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_LIQ_RECOLH | NUMBER(17,2) | Y |  |  |
| 20 | COD_REC_MUNIC | VARCHAR2(4) | Y |  |  |
| 21 | DSC_ORG_ARRECAD | VARCHAR2(30) | Y |  |  |
| 22 | OBS | VARCHAR2(50) | Y |  |  |
| 23 | COD_BANCO | VARCHAR2(3) | Y |  |  |
| 24 | NUM_AGENCIA | VARCHAR2(7) | Y |  |  |
| 25 | NUM_CONTA | VARCHAR2(18) | Y |  |  |
| 26 | USUARIO | VARCHAR2(40) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_MUNIC_ISS, IND_TP_FATUR, COD_TP_RECOLH

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)
- COD_TP_RECOLH → IST_TIPO_RECOLH(COD_TP_RECOLH)

---

## IST_GUIA_RECOLH

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 5 | IND_TP_FATUR | CHAR(1) | N |  |  |
| 6 | COD_TP_RECOLH | VARCHAR2(3) | N |  |  |
| 7 | DAT_INI_COMPET | DATE | Y |  |  |
| 8 | DAT_FIM_COMPET | DATE | Y |  |  |
| 9 | VLR_ISS_RECOLH | NUMBER(17,2) | Y |  |  |
| 10 | DAT_VENCTO | DATE | Y |  |  |
| 11 | DAT_RECOLH | DATE | Y |  |  |
| 12 | NUM_GUIA_RECOLH | VARCHAR2(25) | Y |  |  |
| 13 | VLR_PRINC_RECOLH | NUMBER(17,2) | Y |  |  |
| 14 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 16 | VLR_EXTRAS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ABATIDO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_LIQ_RECOLH | NUMBER(17,2) | Y |  |  |
| 19 | COD_REC_MUNIC | VARCHAR2(4) | Y |  |  |
| 20 | DSC_ORG_ARRECAD | VARCHAR2(30) | Y |  |  |
| 21 | OBS | VARCHAR2(50) | Y |  |  |
| 22 | COD_BANCO | VARCHAR2(3) | Y |  |  |
| 23 | NUM_AGENCIA | VARCHAR2(7) | Y |  |  |
| 24 | NUM_CONTA | VARCHAR2(18) | Y |  |  |
| 25 | USUARIO | VARCHAR2(40) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 28 | DAT_PAGAMENTO | DATE | Y |  |  |
| 29 | COD_OBRIGACAO | VARCHAR2(2) | Y |  |  |
| 30 | NUM_PROC | VARCHAR2(14) | Y |  |  |
| 31 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 32 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 33 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 34 | DSC_RESERVADO_1 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_MUNIC_ISS, IND_TP_FATUR, COD_TP_RECOLH

**FKs**:
- COD_TP_RECOLH → IST_TIPO_RECOLH(COD_TP_RECOLH)
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_GUIA_RET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | NUMBER(4) | N |  |  |
| 4 | MES_REF | NUMBER(4) | N |  |  |
| 5 | VLR_ALIQ | NUMBER(7) | N |  |  |
| 6 | VLR_TOT_GUIA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, VLR_ALIQ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_LANC_DC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | ITEM_APURACAO | VARCHAR2(5) | N |  |  |
| 7 | ITEM_SEQUENCIA | NUMBER(3) | N |  |  |
| 8 | IND_LANCAMENTO | CHAR(1) | Y |  |  |
| 9 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 10 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 11 | DESCRICAO_LANC | VARCHAR2(90) | Y |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 14 | DAT_EMISSAO | DATE | Y |  |  |
| 15 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 16 | OBSERVACAO_CANC | VARCHAR2(90) | Y |  |  |
| 17 | VLR_CORRECAO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CORRIGIDO | NUMBER(17,2) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_MUNICIPIO, DAT_APURACAO, ITEM_APURACAO, ITEM_SEQUENCIA

---

## IST_LANC_OUTROS_DC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | ITEM_APURACAO | VARCHAR2(5) | N |  |  |
| 6 | ITEM_SEQUENCIA | NUMBER(3) | N |  |  |
| 7 | IND_LANCAMENTO | CHAR(1) | Y |  |  |
| 8 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 9 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 10 | DESCRICAO_LANC | VARCHAR2(90) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | DAT_EMISSAO | DATE | Y |  |  |
| 14 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 15 | OBSERVACAO_CANC | VARCHAR2(90) | Y |  |  |
| 16 | VLR_CORRECAO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CORRIGIDO | NUMBER(17,2) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_TP_CREDITO | CHAR(1) | Y |  |  |
| 21 | NUM_PROC | VARCHAR2(14) | Y |  |  |
| 22 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 23 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 24 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 25 | IND_TP_COMP | CHAR(1) | Y |  | Atendimento ao ATO COTEPE 70/05 - Registro B465 |
| 26 | VLR_CRED_PASS_COMP | NUMBER(17,2) | Y |  | Atendimento ao ATO COTEPE 70/05 - Registro B465 |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, ITEM_APURACAO, ITEM_SEQUENCIA

---

## IST_LAYOUT_LVR_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT_LVR_ISS | NUMBER(5) | N |  |  |
| 2 | DSC_LAYOUT_LVR_ISS | VARCHAR2(50) | Y |  |  |

**PK**: COD_LAYOUT_LVR_ISS

---

## IST_LVRRESALIQ_ESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_NAT_SERV | VARCHAR2(35) | N |  |  |
| 6 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 7 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 8 | VLR_DOCTO_FISCAL | NUMBER(17,2) | Y |  |  |
| 9 | BASE_CALC_TRIBUT | NUMBER(17,2) | Y |  |  |
| 10 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, COD_NAT_SERV, ALIQUOTA_ISS

---

## IST_LVR_ESPECIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 7 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 8 | DIA_NF | NUMBER(2) | N |  |  |
| 9 | SERIE_NF | VARCHAR2(3) | N |  |  |
| 10 | NUM_DOCFIS_INI | VARCHAR2(12) | N |  |  |
| 11 | NUM_DOCFIS_FIM | VARCHAR2(12) | N |  |  |
| 12 | COD_NAT_SERV | VARCHAR2(35) | N |  |  |
| 13 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 14 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 15 | BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_OPER_ISENTA | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_CALC_CANC | NUMBER(17,2) | Y |  |  |
| 19 | VLR_SERV_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 20 | VLR_SUBST_TRIBUT | NUMBER(17,2) | Y |  |  |
| 21 | VLR_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 22 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 23 | USUARIO | VARCHAR2(40) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_MUNICIPIO, DAT_APURACAO, ALIQUOTA_ISS, COD_SERVICO, DIA_NF, SERIE_NF, NUM_DOCFIS_INI, NUM_DOCFIS_FIM, COD_NAT_SERV

---

## IST_LVR_GERAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | DIA_NF | NUMBER(2) | N |  |  |
| 7 | SERIE_NF | VARCHAR2(3) | N |  |  |
| 8 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 9 | NUM_DOCFIS_INI | VARCHAR2(12) | N |  |  |
| 10 | NUM_DOCFIS_FIM | VARCHAR2(12) | N |  |  |
| 11 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 12 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 13 | BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_OPER_ISENTA | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_CALC_CANC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SERV_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SUBST_TRIBUT | NUMBER(17,2) | Y |  |  |
| 19 | VLR_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 20 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_MUNICIPIO, DAT_APURACAO, DIA_NF, SERIE_NF, ALIQUOTA_ISS, NUM_DOCFIS_INI, NUM_DOCFIS_FIM, COD_SERVICO

---

## IST_LVR_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | DIA_NF | NUMBER(2) | N |  |  |
| 6 | SERIE_NF | VARCHAR2(3) | N |  |  |
| 7 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 8 | NUM_DOCFIS_INI | VARCHAR2(12) | N |  |  |
| 9 | NUM_DOCFIS_FIM | VARCHAR2(12) | N |  |  |
| 10 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 11 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 12 | BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_OPER_ISENTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_CALC_CANC | NUMBER(17,2) | Y |  |  |
| 16 | VLR_SERV_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SUBST_TRIBUT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 19 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, DIA_NF, SERIE_NF, ALIQUOTA_ISS, NUM_DOCFIS_INI, NUM_DOCFIS_FIM, COD_SERVICO

---

## IST_LVR_ISS_CAMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | VLR_IMPOSTO_DEVIDO | NUMBER(17,2) | Y |  |  |
| 6 | DAT_RECOLHIMENTO | DATE | Y |  |  |
| 7 | BANCO | VARCHAR2(15) | Y |  |  |
| 8 | NUM_DOCUMENTO | VARCHAR2(15) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO

---

## IST_LVR_ISS_ESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 6 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 7 | DIA_NF | NUMBER(2) | N |  |  |
| 8 | SERIE_NF | VARCHAR2(3) | N |  |  |
| 9 | NUM_DOCFIS_INI | VARCHAR2(12) | N |  |  |
| 10 | NUM_DOCFIS_FIM | VARCHAR2(12) | N |  |  |
| 11 | COD_NAT_SERV | VARCHAR2(35) | N |  |  |
| 12 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 13 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 14 | BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_OPER_ISENTA | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_CALC_CANC | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SERV_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_SUBST_TRIBUT | NUMBER(17,2) | Y |  |  |
| 20 | VLR_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 21 | OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 25 | MODELO_DOCTO | VARCHAR2(2) | Y |  | INFORMAÇÃO DO COD_MODELO DA X2024_MODELO_DOCTO |
| 26 | CPF_CGC_FIS_JUR | VARCHAR2(14) | Y |  | CPF ou CGC da Pessoa Fis Jur da Nota Fiscal |
| 27 | INSC_MUNIC_FIS_JUR | VARCHAR2(14) | Y |  | Inscricao Estadual da Pessoa Fis Jur da Nota Fiscal |
| 28 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 29 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 30 | BASE_CALC_SUBSTITUIDO | NUMBER(17,2) | Y |  | Informação utilizada no layout oficial de Brasília |
| 31 | OBSERVACAO_AUX | VARCHAR2(200) | Y |  | Utilizado para imprimir informações em linhas diferentes do livro como, por exemplo, identificar notas canceladas e notas com iss retido separadamente |
| 32 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |
| 33 | VLR_SUBEMPREITADA | NUMBER(17,2) | Y |  |  |
| 34 | DIA_NF_EMISSAO | NUMBER(2) | Y |  |  |
| 35 | DAT_EMISSAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, ALIQUOTA_ISS, COD_SERVICO, DIA_NF, SERIE_NF, NUM_DOCFIS_INI, NUM_DOCFIS_FIM, COD_NAT_SERV, IND_FIS_JUR, COD_FIS_JUR

**Indexes**:
- IX_IST_LVRISS_ESP1: (COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, ALIQUOTA_ISS, DIA_NF, NUM_DOCFIS_INI, NUM_DOCFIS_FIM)
- IX_IST_LVRISS_ESP2: (COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, COD_SERVICO, DIA_NF, SERIE_NF, NUM_DOCFIS_INI, NUM_DOCFIS_FIM)
- IX_IST_LVRISS_ESP3: (COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, DIA_NF, SERIE_NF, NUM_DOCFIS_INI, NUM_DOCFIS_FIM)
- IX_IST_LVRISS_ESP4: (COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, DIA_NF, SERIE_NF, ALIQUOTA_ISS, NUM_DOCFIS_INI, NUM_DOCFIS_FIM)
- IX_IST_LVRISS_ESP5: (COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, COD_NAT_SERV, ALIQUOTA_ISS, DIA_NF, NUM_DOCFIS_INI, NUM_DOCFIS_FIM)

---

## IST_LVR_ISS_ESP_DF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | VLR_ALUGUEL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_AGUA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_PRO_LABORE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_PAGTO_FUNC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_PREV_SOCIAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISS_PROPRIO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SERV_ORG_PUB | NUMBER(17,2) | Y |  |  |
| 14 | DAT_VENCTO_PROP | DATE | Y |  |  |
| 15 | COD_BANCO_PROP | VARCHAR2(3) | Y |  |  |
| 16 | DAT_VENCTO_RET | DATE | Y |  |  |
| 17 | COD_BANCO_RET | VARCHAR2(3) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_LVR_ISS_ESP_MA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_GUIA_REC | NUMBER(16) | Y |  |  |
| 6 | NOME_BANCO_REC | VARCHAR2(30) | Y |  |  |
| 7 | VLR_ISS_RET | NUMBER(17,2) | Y |  |  |
| 8 | NUM_GUIA_RET | NUMBER(16) | Y |  |  |
| 9 | DAT_VENCTO_RET | DATE | Y |  |  |
| 10 | NOME_BANCO_RET | VARCHAR2(30) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_LVR_ISS_ESP_PV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | MES | VARCHAR2(2) | Y |  |  |
| 6 | ANO | VARCHAR2(4) | Y |  |  |
| 7 | INSC_MUNIC_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | CPF_CGC_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | DATA_SAIDA_REC | DATE | Y |  |  |
| 11 | VLR_TOT_DOCTO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 14 | ALIQUOTA_ISS | NUMBER(7,4) | N |  |  |
| 15 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISS_RETIDO_M | NUMBER(17,2) | Y |  |  |
| 17 | DATA_RECOLH_M | DATE | Y |  |  |
| 18 | NOME_BANCO_M | VARCHAR2(30) | Y |  |  |
| 19 | DAM_M | VARCHAR2(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, CPF_CGC_FIS_JUR, NUM_DOCFIS, ALIQUOTA_ISS

---

## IST_LVR_ISS_ESP_RJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | DIA_NF | NUMBER(2) | N |  |  |
| 5 | NUM_DOCFIS_INI_1 | VARCHAR2(12) | Y |  |  |
| 6 | NUM_DOCFIS_FIM_1 | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_NF_1 | VARCHAR2(3) | Y |  |  |
| 8 | ALIQUOTA_ISS_1 | NUMBER(7) | Y |  |  |
| 9 | COD_NAT_SERV_1 | VARCHAR2(10) | Y |  |  |
| 10 | BASE_CALC_ISS_TRIB_1 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_CALC_CANC_1 | NUMBER(17,2) | Y |  |  |
| 12 | NUM_DOCFIS_INI_2 | VARCHAR2(12) | Y |  |  |
| 13 | NUM_DOCFIS_FIM_2 | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_NF_2 | VARCHAR2(3) | Y |  |  |
| 15 | ALIQUOTA_ISS_2 | NUMBER(7) | Y |  |  |
| 16 | COD_NAT_SERV_2 | VARCHAR2(10) | Y |  |  |
| 17 | BASE_CALC_ISS_TRIB_2 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_CALC_CANC_2 | NUMBER(17,2) | Y |  |  |
| 19 | NUM_DOCFIS_INI_3 | VARCHAR2(12) | Y |  |  |
| 20 | NUM_DOCFIS_FIM_3 | VARCHAR2(12) | Y |  |  |
| 21 | SERIE_NF_3 | VARCHAR2(3) | Y |  |  |
| 22 | IND_SEPARA_ISEN | CHAR(1) | Y |  |  |
| 23 | COD_NAT_SERV_ISEN_1 | VARCHAR2(10) | Y |  |  |
| 24 | COD_NAT_SERV_ISEN_2 | VARCHAR2(10) | Y |  |  |
| 25 | COD_NAT_SERV_ISEN_3 | VARCHAR2(10) | Y |  |  |
| 26 | COD_NAT_SERV_ISEN_4 | VARCHAR2(10) | Y |  |  |
| 27 | BASE_CALC_ISS_ISEN | NUMBER(17,2) | Y |  |  |
| 28 | BASE_CALC_ISS_TERC | NUMBER(17,2) | Y |  |  |
| 29 | USUARIO | VARCHAR2(40) | Y |  |  |
| 30 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 31 | NUM_DOCFIS_INI_4 | VARCHAR2(12) | Y |  |  |
| 32 | NUM_DOCFIS_FIM_4 | VARCHAR2(12) | Y |  |  |
| 33 | SERIE_NF_4 | VARCHAR2(12) | Y |  |  |
| 34 | ALIQUOTA_ISS_4 | NUMBER(7) | Y |  |  |
| 35 | COD_NAT_SERV_4 | VARCHAR2(10) | Y |  |  |
| 36 | BASE_CALC_ISS_TRIB_4 | NUMBER(17,2) | Y |  |  |
| 37 | VLR_BASE_CALC_CANC_4 | NUMBER(17,2) | Y |  |  |
| 38 | OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 39 | OBSERVACAO_AUX | VARCHAR2(200) | Y |  | Utilizado para imprimir informações em linhas diferentes do livro como, por exemplo, identificar notas canceladas e notas com iss retido separadamente |
| 40 | OBSERVACAO_CAD | VARCHAR2(200) | Y |  |  |
| 41 | VLR_SERV_TERCEIRO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, DIA_NF

---

## IST_LVR_ISS_MOD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 8 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 9 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 10 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 11 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |
| 12 | VLR_IMPOSTO_DEVIDO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_IMPOSTO_RETIDO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SUBEMPREITADA | NUMBER(17,2) | Y |  |  |
| 16 | DESCRICAO_COMPL | VARCHAR2(500) | Y |  |  |
| 17 | SITUACAO | CHAR(1) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | COD_OPER_ISENTA | CHAR(1) | Y |  | 1 - operacao isenta executada no municipio do estabelecimento. 2 - operacao isenta executada em outro municipio |
| 21 | VLR_TOT_ISENTA | NUMBER(17,2) | Y |  |  |
| 22 | DSC_INF_COMPL | VARCHAR2(90) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, COD_TIPO_LIVRO

---

## IST_LVR_ISS_RJCOMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | DIA_NF | NUMBER(2) | N |  |  |
| 6 | NUM_DOCFIS_TRIB | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS_TRIB | VARCHAR2(3) | N |  |  |
| 8 | NUM_DOCFIS_COMP | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS_COMP | VARCHAR2(3) | N |  |  |
| 10 | IND_TOT_ISS_COMP | CHAR(1) | Y |  |  |
| 11 | BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 12 | BASE_CALC_CANC | NUMBER(17,2) | Y |  |  |
| 13 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 14 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ISS_COMP | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISS_RECOLHE | NUMBER(17,2) | Y |  |  |
| 17 | BASE_CALC_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ISS_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | VLR_ISENTA_N_TRIB | NUMBER(17,2) | Y |  |  |
| 21 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 22 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 23 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, DIA_NF, NUM_DOCFIS_TRIB, SERIE_DOCFIS_TRIB, NUM_DOCFIS_COMP, SERIE_DOCFIS_COMP, ALIQUOTA_ISS, COD_SERVICO, IND_FIS_JUR, COD_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_LVR_ISS_TOM_CAMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | DAT_VENCTO_REC | DATE | Y |  |  |
| 6 | NOME_BANCO_REC | VARCHAR2(30) | Y |  |  |
| 7 | NUM_GUIA_REC | NUMBER(16) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_LVR_M53_EQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_SERVICO | VARCHAR2(10) | Y |  |  |
| 6 | DAT_FISCAL | DATE | Y |  |  |
| 7 | IND_TP_SERVICO | CHAR(1) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 14 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 15 | IND_SITUACAO | CHAR(1) | Y |  |  |
| 16 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 17 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 18 | DSC_MUNIC_ISS | VARCHAR2(50) | Y |  |  |
| 19 | DSC_SERVICO | VARCHAR2(50) | Y |  |  |
| 20 | NOM_TOMADOR_SERV | VARCHAR2(70) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_IST_LVR_M53_EQ: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## IST_LVR_OBS_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | DIA_FISCAL | NUMBER(2) | N |  |  |
| 6 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, DIA_FISCAL

**FKs**:
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## IST_LVR_RES_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 6 | VLR_DOCTO_FISCAL | NUMBER(17,2) | Y |  |  |
| 7 | BASE_CALC_TRIBUT | NUMBER(17,2) | Y |  |  |
| 8 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, ALIQUOTA_ISS

---

## IST_OBRAS_RS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 10 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 11 | COD_OBRA | VARCHAR2(10) | Y |  |  |
| 12 | IND_INSSST_RET | CHAR(1) | Y |  |  |
| 13 | IND_INSSST_DOC_OK | CHAR(1) | Y |  |  |
| 14 | IND_ISS_RET | CHAR(1) | Y |  |  |
| 15 | IND_ISS_DOC_OK | CHAR(1) | Y |  |  |
| 16 | OBS | VARCHAR2(50) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**Indexes**:
- IX_OBRAS_RS: (NUM_PROCESSO)

---

## IST_PAR_EQUIPARADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_CALCISS_SUBEMP | CHAR(1) | Y |  |  |
| 4 | IND_MES_ANT_SUBEMP | CHAR(1) | Y |  |  |
| 5 | IND_TP_ALIQ | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_PAR_PRESTADOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |

**PK**: COD_MUNIC_ISS, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

**FKs**:
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)

---

## IST_RECOLHIM_ISSQN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ESTAB_CENTRAL | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | ALIQ_ISS | NUMBER(7,4) | N |  |  |
| 10 | BASE_ISS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 12 | COD_MUNICIPIO | NUMBER(7) | Y |  |  |
| 13 | DAT_EMISSAO | DATE | Y |  |  |
| 14 | DAT_ENVIO_BCO | DATE | Y |  |  |
| 15 | DT_RECOLHIMENTO | DATE | Y |  |  |
| 16 | DT_PAGTO_NF | DATE | Y |  |  |
| 17 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 18 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 21 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 22 | COD_SERV_LEI116 | VARCHAR2(4) | N |  |  |
| 23 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 25 | SITUACAO | VARCHAR2(1) | Y |  |  |
| 26 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 27 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 28 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 29 | DAT_VENCTO_FERIADO | DATE | Y |  | Data de vencimento calculada levando em consideração os feriados |
| 30 | DAT_VENCTO | DATE | Y |  | Data de vencimento original |

**PK**: COD_EMPRESA, ESTAB_CENTRAL, DATA_FISCAL, COD_ESTAB, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, ALIQ_ISS, COD_DOCTO, COD_SERV_LEI116

---

## IST_RES_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 7 | VLR_DOCTO_FISCAL | NUMBER(17,2) | Y |  |  |
| 8 | BASE_CALC_TRIBUT | NUMBER(17,2) | Y |  |  |
| 9 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_MUNICIPIO, DAT_APURACAO, ALIQUOTA_ISS

---

## IST_RES_ALIQ_ESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | COD_NAT_SERV | VARCHAR2(35) | N |  |  |
| 7 | ALIQUOTA_ISS | NUMBER(7) | N |  |  |
| 8 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 9 | VLR_DOCTO_FISCAL | NUMBER(17,2) | Y |  |  |
| 10 | BASE_CALC_TRIBUT | NUMBER(17,2) | Y |  |  |
| 11 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_MUNICIPIO, DAT_APURACAO, COD_NAT_SERV, ALIQUOTA_ISS

---

## IST_RES_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | ITEM_APURACAO | VARCHAR2(5) | N |  |  |
| 6 | VLR_ITEM_DEB | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ITEM_CRED | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SALDO | NUMBER(17,2) | Y |  |  |
| 9 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, ITEM_APURACAO

---

## IST_RES_APURAC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | ITEM_APURACAO | VARCHAR2(5) | N |  |  |
| 7 | VLR_ITEM_DEB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ITEM_CRED | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SALDO | NUMBER(17,2) | Y |  |  |
| 10 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_MUNICIPIO, DAT_APURACAO, ITEM_APURACAO

---

## IST_RES_M53_EQALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_SERVICO | VARCHAR2(10) | Y |  |  |
| 6 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 7 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 8 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SUB_EMPREIT | NUMBER(17,2) | Y |  |  |
| 10 | DSC_SERVICO | VARCHAR2(50) | Y |  |  |
| 11 | VLR_ISS_NORMAL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ISS_SUBEMPR | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_IST_RES_M53_EQALIQ: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## IST_RES_M53_EQMUN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_SERVICO | VARCHAR2(10) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 8 | DSC_MUNIC_ISS | VARCHAR2(50) | Y |  |  |
| 9 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 10 | DSC_SERVICO | VARCHAR2(50) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_IST_RES_M53_EQMUN: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## IST_RES_NF_CANC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | ALIQUOTA_ISS | NUMBER(7,4) | N |  |  |
| 6 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 7 | DAT_FISCAL | DATE | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | COD_NAT_SERV | VARCHAR2(35) | N |  |  |
| 11 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 12 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 13 | BASE_CALC_ISS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_OPER_ISENTA | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_CALC_CANC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SERV_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SUBST_TRIBUT | NUMBER(17,2) | Y |  |  |
| 19 | VLR_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 20 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | DAT_CANCELAMENTO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO, DAT_APURACAO, ALIQUOTA_ISS, COD_SERVICO, DAT_FISCAL, SERIE_DOCFIS, NUM_DOCFIS, COD_NAT_SERV

---

## IST_TEXTO_LEGAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 4 | DSC_TEXTO1 | VARCHAR2(100) | Y |  |  |
| 5 | DSC_TEXTO2 | VARCHAR2(100) | Y |  |  |
| 6 | DSC_TEXTO3 | VARCHAR2(100) | Y |  |  |
| 7 | DSC_TEXTO4 | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MUNICIPIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IST_TIPO_DOCTO_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 5 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 6 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 7 | COD_DOCTO_MUNIC | VARCHAR2(5) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, COD_DOCTO, COD_MODELO, GRUPO_DOCTO, GRUPO_MODELO

---

## IST_TIPO_RECOLH

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TP_RECOLH | VARCHAR2(3) | N |  |  |
| 2 | DSC_TP_RECOLH | VARCHAR2(50) | Y |  |  |

**PK**: COD_TP_RECOLH

---

