# Módulo: ESOCIAL (ESOCIAL) - 49 tabelas

## ESOCIAL_ARQUIVO_XSD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ARQUIVO | NUMBER(22) | N |  |  |
| 2 | TIPO_EVENTO | VARCHAR2(50) | Y |  |  |
| 3 | DESCRICAO_EVENTO | VARCHAR2(50) | Y |  |  |
| 4 | COD_VERSAO_LAYOUT | VARCHAR2(12) | Y |  |  |
| 5 | ARQUIVO | BLOB | Y |  |  |
| 6 | DAT_ULT_ATUALIZA | DATE | Y |  | Data da ultima atualizacao da respectiva view |

**PK**: ID_ARQUIVO

---

## ESOCIAL_CAD_RUBRICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_RUBRICA | VARCHAR2(9) | N |  |  |
| 4 | COD_TAB_RUBRICA | VARCHAR2(8) | N |  |  |
| 5 | COD_RUBRICA | VARCHAR2(30) | N |  |  |
| 6 | VALID_INI | DATE | N |  |  |
| 7 | VALID_FIM | DATE | Y |  |  |
| 8 | DESC_RUBRICA | VARCHAR2(100) | N |  |  |
| 9 | COD_NAT_RUBRICA | VARCHAR2(4) | N |  |  |
| 10 | TIPO_RUBRICA | VARCHAR2(1) | N |  |  |
| 11 | TIPO_INCID_TRIB_CP | VARCHAR2(1) | Y |  |  |
| 12 | COD_INCID_TRIB_CP | VARCHAR2(2) | Y |  |  |
| 13 | TIPO_INCID_TRIB_IRRF | VARCHAR2(1) | Y |  |  |
| 14 | COD_INCID_TRIB_IRRF | VARCHAR2(2) | Y |  |  |
| 15 | IND_TP_PROC_ADJ_CP | VARCHAR2(1) | Y |  |  |
| 16 | IDENT_PROC_ADJ_CP | NUMBER(12) | Y |  |  |
| 17 | IDENT_SUSP_TBT_CP | NUMBER(12) | Y |  |  |
| 18 | EXTENSAO_CP | VARCHAR2(1) | Y |  |  |
| 19 | IND_TP_PROC_ADJ_IRRF | VARCHAR2(1) | Y |  |  |
| 20 | IDENT_PROC_ADJ_IRRF | NUMBER(12) | Y |  |  |
| 21 | IDENT_SUSP_TBT_IRRF | NUMBER(12) | Y |  |  |
| 22 | OBS_RUBRICA | VARCHAR2(255) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: GRUPO_RUBRICA, COD_TAB_RUBRICA, COD_RUBRICA, VALID_INI

---

## ESOCIAL_CAD_RUBRICA_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ESOCIAL_CAD_RUBRICA_HIST | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_RUBRICA | VARCHAR2(9) | N |  |  |
| 5 | COD_TAB_RUBRICA | VARCHAR2(8) | N |  |  |
| 6 | COD_RUBRICA | VARCHAR2(30) | N |  |  |
| 7 | VALID_INI | DATE | N |  |  |
| 8 | DAT_OCORRENCIA | TIMESTAMP(6) | N |  |  |
| 9 | VALID_FIM | DATE | Y |  |  |
| 10 | DESC_RUBRICA | VARCHAR2(100) | N |  |  |
| 11 | COD_NAT_RUBRICA | VARCHAR2(4) | N |  |  |
| 12 | TIPO_RUBRICA | VARCHAR2(1) | N |  |  |
| 13 | TIPO_INCID_TRIB_CP | VARCHAR2(1) | Y |  |  |
| 14 | COD_INCID_TRIB_CP | VARCHAR2(4) | Y |  |  |
| 15 | TIPO_INCID_TRIB_IRRF | VARCHAR2(1) | Y |  |  |
| 16 | COD_INCID_TRIB_IRRF | VARCHAR2(4) | Y |  |  |
| 17 | IND_TP_PROC_ADJ_CP | VARCHAR2(1) | Y |  |  |
| 18 | IDENT_PROC_ADJ_CP | NUMBER(12) | Y |  |  |
| 19 | IDENT_SUSP_TBT_CP | NUMBER(12) | Y |  |  |
| 20 | EXTENSAO_CP | VARCHAR2(1) | Y |  |  |
| 21 | IND_TP_PROC_ADJ_IRRF | VARCHAR2(1) | Y |  |  |
| 22 | IDENT_PROC_ADJ_IRRF | NUMBER(12) | Y |  |  |
| 23 | IDENT_SUSP_TBT_IRRF | NUMBER(12) | Y |  |  |
| 24 | OBS_RUBRICA | VARCHAR2(255) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 27 | IND_STATUS | VARCHAR2(1) | Y |  |  |
| 28 | IND_DELETE | VARCHAR2(1) | Y |  |  |

**PK**: ID_ESOCIAL_CAD_RUBRICA_HIST

---

## ESOCIAL_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_AMB | CHAR(1) | Y | '1' |  |
| 4 | VLR_DEDUCAO_S1210 | NUMBER(17,2) | Y |  |  |
| 5 | IND_ORIGEM_X63 | VARCHAR2(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## ESOCIAL_INF_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VALID_INI | DATE | N |  |  |
| 4 | VALID_FIM | DATE | Y |  |  |
| 5 | ALIQ_GILRAT | NUMBER(5,4) | Y |  |  |
| 6 | IND_TP_PROC_ADJ_GILRAT | CHAR(1) | Y |  |  |
| 7 | IDENT_PROC_ADJ_GILRAT | NUMBER(12) | Y |  |  |
| 8 | IDENT_SUSP_TBT_GILRAT | NUMBER(12) | Y |  |  |
| 9 | VLR_FAP | NUMBER(5,4) | Y |  |  |
| 10 | IND_TP_PROC_ADJ_FAP | CHAR(1) | Y |  |  |
| 11 | IDENT_PROC_ADJ_FAP | NUMBER(12) | Y |  |  |
| 12 | IDENT_SUSP_TBT_FAP | NUMBER(12) | Y |  |  |
| 13 | IND_CONTROLE_PONTO | CHAR(1) | Y |  |  |
| 14 | IND_APRENDIZ | CHAR(1) | Y |  |  |
| 15 | IND_TP_PROC_ADJ_APRENDIZ | CHAR(1) | Y |  |  |
| 16 | IDENT_PROC_ADJ_APRENDIZ | NUMBER(12) | Y |  |  |
| 17 | IND_CONTRATACAO | CHAR(1) | Y |  |  |
| 18 | CNPJ_CONTRATACAO | VARCHAR2(14) | Y |  |  |
| 19 | IND_CONTRATACAO_DEFIC | CHAR(1) | Y |  |  |
| 20 | IND_TP_PROC_ADJ_DEFIC | CHAR(1) | Y |  |  |
| 21 | IDENT_PROC_ADJ_DEFIC | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, VALID_INI

---

## ESOCIAL_INF_ESTAB_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ESOCIAL_INF_ESTAB_HIST | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | VALID_INI | DATE | N |  |  |
| 5 | DAT_OCORRENCIA | TIMESTAMP(6) | N |  |  |
| 6 | VALID_FIM | DATE | Y |  |  |
| 7 | ALIQ_GILRAT | NUMBER(5,4) | Y |  |  |
| 8 | IND_TP_PROC_ADJ_GILRAT | CHAR(1) | Y |  |  |
| 9 | IDENT_PROC_ADJ_GILRAT | NUMBER(12) | Y |  |  |
| 10 | IDENT_SUSP_TBT_GILRAT | NUMBER(12) | Y |  |  |
| 11 | VLR_FAP | NUMBER(5,4) | Y |  |  |
| 12 | IND_TP_PROC_ADJ_FAP | CHAR(1) | Y |  |  |
| 13 | IDENT_PROC_ADJ_FAP | NUMBER(12) | Y |  |  |
| 14 | IDENT_SUSP_TBT_FAP | NUMBER(12) | Y |  |  |
| 15 | IND_CONTROLE_PONTO | CHAR(1) | Y |  |  |
| 16 | IND_APRENDIZ | CHAR(1) | Y |  |  |
| 17 | IND_TP_PROC_ADJ_APRENDIZ | CHAR(1) | Y |  |  |
| 18 | IDENT_PROC_ADJ_APRENDIZ | NUMBER(12) | Y |  |  |
| 19 | IND_CONTRATACAO | CHAR(1) | Y |  |  |
| 20 | CNPJ_CONTRATACAO | VARCHAR2(14) | Y |  |  |
| 21 | IND_CONTRATACAO_DEFIC | CHAR(1) | Y |  |  |
| 22 | IND_TP_PROC_ADJ_DEFIC | CHAR(1) | Y |  |  |
| 23 | IDENT_PROC_ADJ_DEFIC | NUMBER(12) | Y |  |  |
| 24 | IND_STATUS | CHAR(1) | Y |  |  |
| 25 | IND_DELETE | CHAR(1) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: ID_ESOCIAL_INF_ESTAB_HIST

**Indexes**:
- UK_ESOCIAL_INF_ESTAB_HIST_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, VALID_INI, DAT_OCORRENCIA)

---

## ESOCIAL_PAINEL_ARG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_EVENTO | VARCHAR2(50) | Y |  |  |
| 4 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 5 | CPF | VARCHAR2(11) | Y |  |  |

**Indexes**:
- IX_ESOCIAL_PAINEL_ARG_01: (COD_EMPRESA, COD_ESTAB, TIPO_EVENTO, COD_STATUS_PAINEL)

---

## ESOCIAL_PAR_SETOR_ESTAB
**Comment**: Tabela de Parametrizacao do Setor por Estabelecimento do ESOCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_SETOR | VARCHAR2(9) | N |  |  |
| 4 | COD_SETOR | VARCHAR2(10) | N |  |  |
| 5 | VALID_SETOR | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_SETOR, COD_SETOR, VALID_SETOR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ESOCIAL_PGER_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_APUR | DATE | N |  |  |
| 5 | COD_VERSAO | VARCHAR2(20) | N |  |  |
| 6 | IND_STATUS | CHAR(1) | Y |  |  |
| 7 | PROC_ID | NUMBER(12) | Y |  |  |
| 8 | IND_S1200 | CHAR(1) | Y |  |  |
| 9 | IND_S1210 | CHAR(1) | Y |  |  |
| 10 | IND_S1300 | CHAR(1) | Y |  |  |
| 11 | IND_S1250 | CHAR(1) | Y |  |  |

**PK**: ID_PGER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_ESOCIAL_PGER_APUR_001 (UNIQUE): (ID_PGER_APUR, COD_EMPRESA, COD_ESTAB, DAT_APUR, COD_VERSAO)

---

## ESOCIAL_PGER_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_ESTAB | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IND_S1005 | CHAR(1) | Y |  |  |
| 5 | IND_S1010 | CHAR(1) | Y |  |  |
| 6 | IND_S1020 | CHAR(1) | Y |  |  |
| 7 | IND_S1070 | CHAR(1) | Y |  |  |
| 8 | COD_VERSAO | VARCHAR2(20) | N | 'v02_04_00' |  |

**PK**: ID_PGER_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_ESOCIAL_PGER_ESTAB_001 (UNIQUE): (ID_PGER_ESTAB, COD_EMPRESA, COD_ESTAB, COD_VERSAO)

---

## ESOCIAL_PGER_LOG_MSG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_LOG_MSG | NUMBER(22) | N |  |  |
| 2 | ID_OC | NUMBER(12) | Y |  |  |
| 3 | TIPO_EVENTO | VARCHAR2(50) | Y |  |  |
| 4 | IND_LOG_MSG | CHAR(1) | Y |  |  |
| 5 | DAT_CRIACAO | DATE | Y |  |  |
| 6 | PROTOCOLO_ONESOURCE | VARCHAR2(36) | Y |  |  |
| 7 | STATUS_PROC | VARCHAR2(8) | Y |  |  |
| 8 | XML_ENVIO_RETORNO | CLOB | Y |  |  |
| 9 | COD_MENSAGEM_ONESOURCE | VARCHAR2(8) | Y |  |  |
| 10 | DES_MENSAGEM_ONESOURCE | VARCHAR2(4000) | Y |  |  |
| 11 | ID_EVENTO_ONESOURCE | VARCHAR2(36) | Y |  |  |
| 12 | RECIBO_ONESOURCE | VARCHAR2(52) | Y |  |  |
| 13 | HASH_ONESOURCE | VARCHAR2(44) | Y |  |  |
| 14 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |
| 15 | LIDO | CHAR(1) | Y |  |  |
| 16 | DESC_PROC_ERRO | VARCHAR2(200) | Y |  |  |
| 17 | ID_STG_EVENTOS_ESOCIAL_IN | NUMBER(22) | Y |  |  |

**PK**: ID_PGER_LOG_MSG

**Indexes**:
- IX_ESOCIAL_PGER_LOG_MSG: (LIDO)
- IX_ESOCIAL_PGER_LOG_MSG_01: (ID_OC)
- IX_ESOCIAL_PGER_LOG_MSG_2: (IND_LOG_MSG)
- IX_ESOCIAL_PGER_LOG_MSG_3: (ID_STG_EVENTOS_ESOCIAL_OUT)

---

## ESOCIAL_PGER_S1005_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_S1005_ESTAB | NUMBER(12) | N |  |  |
| 2 | ID_PGER_ESTAB | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | N |  |  |
| 4 | NUM_INSCRICAO | VARCHAR2(14) | N |  |  |
| 5 | VALID_INI | DATE | N |  |  |
| 6 | VALID_FIM | DATE | Y |  |  |

**PK**: ID_PGER_S1005_ESTAB

**FKs**:
- ID_PGER_ESTAB → ESOCIAL_PGER_ESTAB(ID_PGER_ESTAB)

**Indexes**:
- UK_ESOCIAL_S1005_ESTAB_001 (UNIQUE): (ID_PGER_S1005_ESTAB, ID_PGER_ESTAB, TP_INSCRICAO, NUM_INSCRICAO, VALID_INI)

---

## ESOCIAL_PGER_S1005_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1005_OC | NUMBER(12) | N |  |  |
| 2 | ID_PGER_S1005_ESTAB | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_OPER | CHAR(1) | Y |  |  |
| 5 | IND_STATUS | CHAR(1) | Y |  |  |
| 6 | PROC_ID | NUMBER(12) | Y |  |  |
| 7 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 8 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 9 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 10 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 11 | COD_VERSAO_LAYOUT | VARCHAR2(12) | Y |  |  |
| 12 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 13 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |
| 14 | CNAE_PREP | NUMBER(7) | Y |  |  |
| 15 | ALIQ_GILRAT | NUMBER(5,4) | Y |  |  |
| 16 | VLR_FAP | NUMBER(5,4) | Y |  |  |
| 17 | ALIQ_RAT_AJUSTE | NUMBER(5,4) | Y |  |  |
| 18 | IND_TP_PROC_ADJ_GILRAT | CHAR(1) | Y |  |  |
| 19 | NUM_PROC_ADJ_GILRAT | VARCHAR2(21) | Y |  |  |
| 20 | COD_SUSP_TBT_GILRAT | VARCHAR2(14) | Y |  |  |
| 21 | IND_TP_PROC_ADJ_FAP | CHAR(1) | Y |  |  |
| 22 | NUM_PROC_ADJ_FAP | VARCHAR2(21) | Y |  |  |
| 23 | COD_SUSP_TBT_FAP | VARCHAR2(14) | Y |  |  |
| 24 | IND_CONTROLE_PONTO | CHAR(1) | Y |  |  |
| 25 | IND_APRENDIZ | CHAR(1) | Y |  |  |
| 26 | NUM_PROC_ADJ_APRENDIZ | VARCHAR2(21) | Y |  |  |
| 27 | IND_CONTRATACAO | CHAR(1) | Y |  |  |
| 28 | CNPJ_CONTRATACAO | VARCHAR2(14) | Y |  |  |
| 29 | IND_CONTRATACAO_DEFIC | CHAR(1) | Y |  |  |
| 30 | NUM_PROC_ADJ_DEFIC | VARCHAR2(21) | Y |  |  |
| 31 | ID_ESOCIAL_INF_ESTAB_HIST | NUMBER(12) | Y |  |  |
| 32 | VALID_FIM | DATE | Y |  |  |
| 33 | VALID_FIM_NV | DATE | Y |  |  |
| 34 | IND_VALID_NV | CHAR(1) | Y |  |  |

**PK**: ID_S1005_OC

**FKs**:
- ID_PGER_S1005_ESTAB → ESOCIAL_PGER_S1005_ESTAB(ID_PGER_S1005_ESTAB)

**Indexes**:
- IX_ESOCIAL_PGER_S1005_OC_01: (ID_PGER_S1005_ESTAB)
- UK_ESOCIAL_PGER_S1005_OC_001 (UNIQUE): (ID_S1005_OC, ID_PGER_S1005_ESTAB, DAT_OCORRENCIA)

---

## ESOCIAL_PGER_S1010_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1010_OC | NUMBER(12) | N |  |  |
| 2 | ID_PGER_S1010_RUBRICA | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_OPER | CHAR(1) | Y |  |  |
| 5 | IND_STATUS | CHAR(1) | Y |  |  |
| 6 | PROC_ID | NUMBER(12) | Y |  |  |
| 7 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 8 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 9 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 10 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 11 | COD_VERSAO_LAYOUT | VARCHAR2(12) | Y |  |  |
| 12 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 13 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |
| 14 | DESC_RUBRICA | VARCHAR2(100) | Y |  |  |
| 15 | COD_NAT_RUBRICA | VARCHAR2(4) | Y |  |  |
| 16 | TIPO_RUBRICA | CHAR(1) | Y |  |  |
| 17 | COD_INCID_TRIB_CP | VARCHAR2(4) | Y |  |  |
| 18 | COD_INCID_TRIB_IRRF | VARCHAR2(4) | Y |  |  |
| 19 | COD_INCID_FGTS | VARCHAR2(2) | Y | '00' |  |
| 20 | COD_INCID_SIND | VARCHAR2(2) | Y | '00' |  |
| 21 | OBS_RUBRICA | VARCHAR2(255) | Y |  |  |
| 22 | IND_TP_PROC_ADJ_CP | CHAR(1) | Y |  |  |
| 23 | NUM_PROC_ADJ_CP | VARCHAR2(21) | Y |  |  |
| 24 | COD_SUSP_TBT_CP | VARCHAR2(14) | Y |  |  |
| 25 | EXTENSAO_CP | CHAR(1) | Y |  |  |
| 26 | NUM_PROC_ADJ_IRRF | VARCHAR2(21) | Y |  |  |
| 27 | COD_SUSP_TBT_IRRF | VARCHAR2(14) | Y |  |  |
| 28 | ID_ESOCIAL_CAD_RUBRICA_HIST | NUMBER(12) | Y |  |  |
| 29 | VALID_FIM | DATE | Y |  |  |
| 30 | VALID_FIM_NV | DATE | Y |  |  |
| 31 | IND_VALID_NV | VARCHAR2(1) | Y |  |  |

**PK**: ID_S1010_OC

**FKs**:
- ID_PGER_S1010_RUBRICA → ESOCIAL_PGER_S1010_RUBRICA(ID_PGER_S1010_RUBRICA)

**Indexes**:
- UK_ESOCIAL_PGER_S1010_OC_001 (UNIQUE): (ID_S1010_OC, ID_PGER_S1010_RUBRICA, DAT_OCORRENCIA)

---

## ESOCIAL_PGER_S1010_RUBRICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_S1010_RUBRICA | NUMBER(12) | N |  |  |
| 2 | ID_PGER_ESTAB | NUMBER(12) | N |  |  |
| 3 | COD_RUBRICA | VARCHAR2(30) | N |  |  |
| 4 | COD_TAB_RUBRICA | VARCHAR2(8) | N |  |  |
| 5 | VALID_INI | DATE | N |  |  |
| 6 | VALID_FIM | DATE | Y |  |  |

**PK**: ID_PGER_S1010_RUBRICA

**FKs**:
- ID_PGER_ESTAB → ESOCIAL_PGER_ESTAB(ID_PGER_ESTAB)

**Indexes**:
- UK_ESOCIAL_S1010_RUBRICA_001 (UNIQUE): (ID_PGER_S1010_RUBRICA, ID_PGER_ESTAB, COD_RUBRICA, COD_TAB_RUBRICA, VALID_INI)

---

## ESOCIAL_PGER_S1020_LOTACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_S1020_LOTACAO | NUMBER(12) | N |  |  |
| 2 | ID_PGER_ESTAB | NUMBER(12) | N |  |  |
| 3 | COD_LOTACAO | VARCHAR2(30) | N |  |  |
| 4 | VALID_INI | DATE | N |  |  |
| 5 | VALID_FIM | DATE | Y |  |  |

**PK**: ID_PGER_S1020_LOTACAO

**FKs**:
- ID_PGER_ESTAB → ESOCIAL_PGER_ESTAB(ID_PGER_ESTAB)

**Indexes**:
- UK_ESOCIAL_S1020_LOTACAO_001 (UNIQUE): (ID_PGER_S1020_LOTACAO, ID_PGER_ESTAB, COD_LOTACAO, VALID_INI)

---

## ESOCIAL_PGER_S1020_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1020_OC | NUMBER(12) | N |  |  |
| 2 | ID_PGER_S1020_LOTACAO | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_OPER | CHAR(1) | Y |  |  |
| 5 | IND_STATUS | CHAR(1) | Y |  |  |
| 6 | PROC_ID | NUMBER(12) | Y |  |  |
| 7 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 8 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 9 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 10 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 11 | COD_VERSAO_LAYOUT | VARCHAR2(12) | Y |  |  |
| 12 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 13 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |
| 14 | TIPO_LOTACAO_TRIB | VARCHAR2(2) | Y |  |  |
| 15 | TIPO_INSC_LOTACAO | CHAR(1) | Y |  |  |
| 16 | NUM_INSC_LOTACAO | VARCHAR2(15) | Y |  |  |
| 17 | COD_FPAS | VARCHAR2(3) | Y |  |  |
| 18 | COD_TERCEIROS | VARCHAR2(4) | Y |  |  |
| 19 | COD_COMB_TERCEIROS | VARCHAR2(4) | Y |  |  |
| 20 | COD_TERCEIROS_PROCESSO | VARCHAR2(4) | Y |  |  |
| 21 | NUM_PROC_ADJ_TERCEIRO | VARCHAR2(21) | Y |  |  |
| 22 | COD_SUSP_TBT_TERCEIRO | VARCHAR2(14) | Y |  |  |
| 23 | ID_X2037_SETOR_HIST | NUMBER(12) | Y |  |  |
| 24 | VALID_FIM | DATE | Y |  |  |
| 25 | VALID_FIM_NV | DATE | Y |  |  |
| 26 | IND_VALID_NV | VARCHAR2(1) | Y |  |  |
| 27 | ALIQ_GILRAT | VARCHAR2(1) | Y |  |  |
| 28 | VLR_FAP | NUMBER(5,4) | Y |  |  |

**PK**: ID_S1020_OC

**FKs**:
- ID_PGER_S1020_LOTACAO → ESOCIAL_PGER_S1020_LOTACAO(ID_PGER_S1020_LOTACAO)

**Indexes**:
- UK_ESOCIAL_S1020_OC_001 (UNIQUE): (ID_S1020_OC, ID_PGER_S1020_LOTACAO, DAT_OCORRENCIA)

---

## ESOCIAL_PGER_S1070_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1070_OC | NUMBER(12) | N |  |  |
| 2 | ID_PGER_PROC_ADJ | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_OPER | CHAR(1) | Y |  |  |
| 5 | IND_STATUS | CHAR(1) | Y |  |  |
| 6 | PROC_ID | NUMBER(12) | Y |  |  |
| 7 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 8 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 9 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 10 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 11 | COD_VERSAO_LAYOUT | VARCHAR2(12) | Y |  |  |
| 12 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 13 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |
| 14 | IND_AUTORIA | CHAR(1) | Y |  |  |
| 15 | UF_VARA | VARCHAR2(2) | Y |  |  |
| 16 | COD_MUNICIPIO | VARCHAR2(7) | Y |  |  |
| 17 | COD_VARA | VARCHAR2(4) | Y |  |  |
| 18 | IND_MATERIA_PROC | VARCHAR2(2) | Y |  |  |
| 19 | IDENT_PROC_ADJ_HIST | NUMBER(12) | Y |  |  |
| 20 | VALID_FIM | DATE | Y |  |  |
| 21 | VALID_FIM_NV | DATE | Y |  |  |
| 22 | IND_VALID_NV | VARCHAR2(1) | Y |  |  |

**PK**: ID_S1070_OC

**FKs**:
- ID_PGER_PROC_ADJ → ESOCIAL_PGER_S1070_PROC_ADJ(ID_PGER_PROC_ADJ)

**Indexes**:
- UK_REINF_PGER_S10REIN70_OC_001 (UNIQUE): (ID_S1070_OC, ID_PGER_PROC_ADJ, DAT_OCORRENCIA)

---

## ESOCIAL_PGER_S1070_PROC_ADJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_PROC_ADJ | NUMBER(12) | N |  |  |
| 2 | ID_PGER_ESTAB | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 5 | VALID_PROC_ADJ_INI | DATE | N |  |  |
| 6 | VALID_PROC_ADJ_FIM | DATE | Y |  |  |
| 7 | DSC_OBSERVACAO | VARCHAR2(255) | Y |  |  |

**PK**: ID_PGER_PROC_ADJ

**FKs**:
- ID_PGER_ESTAB → ESOCIAL_PGER_ESTAB(ID_PGER_ESTAB)

**Indexes**:
- UK_ESOCIAL_PGER_S1070_PROC_001 (UNIQUE): (ID_PGER_PROC_ADJ, ID_PGER_ESTAB, IND_TP_PROC_ADJ, NUM_PROC_ADJ, VALID_PROC_ADJ_INI)

---

## ESOCIAL_PGER_S1070_SUSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1070_SUSP | NUMBER(12) | N |  |  |
| 2 | ID_S1070_OC | NUMBER(12) | N |  |  |
| 3 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 4 | IND_SUSP | VARCHAR2(2) | Y |  |  |
| 5 | DAT_DECISAO | DATE | Y |  |  |
| 6 | IND_DEPOSITO | CHAR(1) | Y |  |  |

**PK**: ID_S1070_SUSP

**FKs**:
- ID_S1070_OC → ESOCIAL_PGER_S1070_OC(ID_S1070_OC)

**Indexes**:
- UK_REINF_PGER_S1070_SUSP_001 (UNIQUE): (ID_S1070_SUSP, ID_S1070_OC)

---

## ESOCIAL_PGER_S1200_DMDEV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_DMDEV | NUMBER(12) | N |  |  |
| 2 | ID_S1200_OC | NUMBER(12) | N |  |  |
| 3 | ID_DEM_PAG | VARCHAR2(30) | N |  |  |
| 4 | COD_CATEG_TRAB | VARCHAR2(3) | Y |  |  |
| 5 | COD_CBO | VARCHAR2(10) | Y |  |  |

**PK**: ID_S1200_DMDEV

**FKs**:
- ID_S1200_OC → ESOCIAL_PGER_S1200_OC(ID_S1200_OC)

**Indexes**:
- UK_ESOCIAL_PGER_S1200_DMDEV (UNIQUE): (ID_S1200_DMDEV, ID_S1200_OC, ID_DEM_PAG)

---

## ESOCIAL_PGER_S1200_EMPREGADOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_EMP | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(15) | N |  |  |

**PK**: ID_S1200_EMP

**FKs**:
- ID_PGER_APUR → ESOCIAL_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_ESOCIAL_PGER_S1200_EMP_001 (UNIQUE): (ID_S1200_EMP, ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## ESOCIAL_PGER_S1200_INFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_INFO | NUMBER(12) | N |  |  |
| 2 | ID_S1200_OC | NUMBER(12) | N |  |  |
| 3 | NOME_TRABALHADOR | VARCHAR2(70) | Y |  |  |
| 4 | DATA_NASC | DATE | Y |  |  |
| 5 | COD_CBO | VARCHAR2(10) | Y |  |  |
| 6 | IND_NAT_ATIVIDADE | CHAR(1) | Y |  |  |
| 7 | QTDE_DIAS | VARCHAR2(2) | Y |  |  |

**PK**: ID_S1200_INFO

**FKs**:
- ID_S1200_OC → ESOCIAL_PGER_S1200_OC(ID_S1200_OC)

---

## ESOCIAL_PGER_S1200_LOTACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_LOTACAO | NUMBER(12) | N |  |  |
| 2 | ID_S1200_OC | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | Y |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(15) | Y |  |  |
| 5 | COD_LOTACAO | VARCHAR2(30) | Y |  |  |
| 6 | QTDE_DIAS | VARCHAR2(2) | Y |  |  |
| 7 | ID_S1200_DMDEV | NUMBER(12) | Y |  |  |

**PK**: ID_S1200_LOTACAO

**FKs**:
- ID_S1200_OC → ESOCIAL_PGER_S1200_OC(ID_S1200_OC)

---

## ESOCIAL_PGER_S1200_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_OC | NUMBER(12) | N |  |  |
| 2 | ID_S1200_TRAB | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(12) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |
| 15 | IND_MV | CHAR(1) | Y |  |  |

**PK**: ID_S1200_OC

**FKs**:
- ID_S1200_TRAB → ESOCIAL_PGER_S1200_TRAB(ID_S1200_TRAB)

**Indexes**:
- UK_ESOCIAL_PGER_S1200_OC_001 (UNIQUE): (ID_S1200_OC, ID_S1200_TRAB, DAT_OCORRENCIA)

---

## ESOCIAL_PGER_S1200_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_PROC | NUMBER(12) | N |  |  |
| 2 | ID_S1200_OC | NUMBER(12) | N |  |  |
| 3 | IND_TP_TRIB | CHAR(1) | Y |  |  |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  |  |

**PK**: ID_S1200_PROC

**FKs**:
- ID_S1200_OC → ESOCIAL_PGER_S1200_OC(ID_S1200_OC)

---

## ESOCIAL_PGER_S1200_REMUN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_REMUN | NUMBER(12) | N |  |  |
| 2 | ID_S1200_OC | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | Y |  |  |
| 4 | CPF_CNPJ_EMPREGADOR | VARCHAR2(15) | Y |  |  |
| 5 | COD_CATEG_TRAB | VARCHAR2(3) | Y |  |  |
| 6 | VLR_REMUNERACAO | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1200_REMUN

**FKs**:
- ID_S1200_OC → ESOCIAL_PGER_S1200_OC(ID_S1200_OC)

---

## ESOCIAL_PGER_S1200_RUBRICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_RUBRICA | NUMBER(12) | N |  |  |
| 2 | ID_S1200_DMDEV | NUMBER(12) | N |  |  |
| 3 | COD_RUBRICA | VARCHAR2(30) | Y |  |  |
| 4 | COD_TAB_RUBRICA | VARCHAR2(8) | Y |  |  |
| 5 | QTDE_REF | NUMBER(6,2) | Y |  |  |
| 6 | FATOR_CALC | NUMBER(5,2) | Y |  |  |
| 7 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1200_RUBRICA

**FKs**:
- ID_S1200_DMDEV → ESOCIAL_PGER_S1200_DMDEV(ID_S1200_DMDEV)

---

## ESOCIAL_PGER_S1200_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1200_TRAB | NUMBER(12) | N |  |  |
| 2 | ID_S1200_EMP | NUMBER(12) | N |  |  |
| 3 | CPF_TRABALHADOR | VARCHAR2(11) | Y |  |  |
| 4 | NIS_TRABALHADOR | VARCHAR2(11) | Y |  |  |
| 5 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 6 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |

**PK**: ID_S1200_TRAB

**FKs**:
- ID_S1200_EMP → ESOCIAL_PGER_S1200_EMPREGADOR(ID_S1200_EMP)

**Indexes**:
- UK_ESOCIAL_PGER_S1200_TRAB (UNIQUE): (ID_S1200_TRAB, ID_S1200_EMP, IND_FIS_JUR, COD_FIS_JUR)

---

## ESOCIAL_PGER_S1210_BENEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1210_BENEF | NUMBER(12) | N |  |  |
| 2 | ID_S1210_EMP | NUMBER(12) | N |  |  |
| 3 | CPF_BENEFICIARIO | VARCHAR2(11) | Y |  |  |
| 4 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |

**PK**: ID_S1210_BENEF

**FKs**:
- ID_S1210_EMP → ESOCIAL_PGER_S1210_EMPREGADOR(ID_S1210_EMP)

**Indexes**:
- UK_ESOCIAL_PGER_S1210_BENEF (UNIQUE): (ID_S1210_BENEF, ID_S1210_EMP, IND_FIS_JUR, COD_FIS_JUR)

---

## ESOCIAL_PGER_S1210_DET_PAGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1210_DET_PAGTO | NUMBER(12) | N |  |  |
| 2 | ID_S1210_INFO_PAGTO | NUMBER(12) | N |  |  |
| 3 | PER_REF | VARCHAR2(7) | Y |  |  |
| 4 | ID_DEM_PAGTO | VARCHAR2(30) | N |  |  |
| 5 | IND_PAG_TOTAL | CHAR(1) | N |  |  |
| 6 | VLR_LIQ | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1210_DET_PAGTO

**FKs**:
- ID_S1210_INFO_PAGTO → ESOCIAL_PGER_S1210_INFO_PAGTO(ID_S1210_INFO_PAGTO)

**Indexes**:
- UK_ESOCIAL_S1210_DET_PAG_001 (UNIQUE): (ID_S1210_DET_PAGTO, ID_S1210_INFO_PAGTO, ID_DEM_PAGTO, IND_PAG_TOTAL)

---

## ESOCIAL_PGER_S1210_EMPREGADOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1210_EMP | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(15) | N |  |  |

**PK**: ID_S1210_EMP

**FKs**:
- ID_PGER_APUR → ESOCIAL_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_ESOCIAL_PGER_S1210_EMP_001 (UNIQUE): (ID_S1210_EMP, ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## ESOCIAL_PGER_S1210_INFO_PAGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1210_INFO_PAGTO | NUMBER(12) | N |  |  |
| 2 | ID_S1210_OC | NUMBER(12) | N |  |  |
| 3 | DAT_PAGTO | DATE | Y |  |  |
| 4 | TP_PAGTO | VARCHAR2(2) | Y |  |  |
| 5 | IND_RES_BR | CHAR(1) | Y |  |  |

**PK**: ID_S1210_INFO_PAGTO

**FKs**:
- ID_S1210_OC → ESOCIAL_PGER_S1210_OC(ID_S1210_OC)

---

## ESOCIAL_PGER_S1210_INF_PAG_EXT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1210_INFO_PAG_EXT | NUMBER(12) | N |  |  |
| 2 | ID_S1210_OC | NUMBER(12) | N |  |  |
| 3 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 4 | IND_IDENTIF_FISCAL | CHAR(1) | Y |  |  |
| 5 | NUM_ID_FISCAL | VARCHAR2(30) | Y |  |  |
| 6 | ENDERECO | VARCHAR2(80) | Y |  |  |
| 7 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 8 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 9 | BAIRRO | VARCHAR2(60) | Y |  |  |
| 10 | CIDADE | VARCHAR2(50) | Y |  |  |
| 11 | CEP | VARCHAR2(12) | Y |  |  |

**PK**: ID_S1210_INFO_PAG_EXT

**FKs**:
- ID_S1210_OC → ESOCIAL_PGER_S1210_OC(ID_S1210_OC)

---

## ESOCIAL_PGER_S1210_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1210_OC | NUMBER(12) | N |  |  |
| 2 | ID_S1210_BENEF | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(12) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |
| 15 | VLR_DED_DEP | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1210_OC

**FKs**:
- ID_S1210_BENEF → ESOCIAL_PGER_S1210_BENEF(ID_S1210_BENEF)

**Indexes**:
- UK_ESOCIAL_PGER_S1210_OC_001 (UNIQUE): (ID_S1210_OC, ID_S1210_BENEF, DAT_OCORRENCIA)

---

## ESOCIAL_PGER_S1210_PAGTO_PARC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1210_PAGTO_PARC | NUMBER(12) | N |  |  |
| 2 | ID_S1210_DET_PAGTO | NUMBER(12) | N |  |  |
| 3 | COD_RUBRICA | VARCHAR2(30) | Y |  |  |
| 4 | COD_TAB_RUBRICA | VARCHAR2(8) | Y |  |  |
| 5 | QTDE_REF | NUMBER(6,2) | Y |  |  |
| 6 | FATOR_CALC | NUMBER(5,2) | Y |  |  |
| 7 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1210_PAGTO_PARC

**FKs**:
- ID_S1210_DET_PAGTO → ESOCIAL_PGER_S1210_DET_PAGTO(ID_S1210_DET_PAGTO)

---

## ESOCIAL_PGER_S1210_PAGTO_TOT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1210_PAGTO_TOT | NUMBER(12) | N |  |  |
| 2 | ID_S1210_DET_PAGTO | NUMBER(12) | N |  |  |
| 3 | COD_RUBRICA | VARCHAR2(30) | Y |  |  |
| 4 | COD_TAB_RUBRICA | VARCHAR2(8) | Y |  |  |
| 5 | QTDE_REF | NUMBER(6,2) | Y |  |  |
| 6 | FATOR_CALC | NUMBER(5,2) | Y |  |  |
| 7 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1210_PAGTO_TOT

**FKs**:
- ID_S1210_DET_PAGTO → ESOCIAL_PGER_S1210_DET_PAGTO(ID_S1210_DET_PAGTO)

---

## ESOCIAL_PGER_S1250_AQUIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1250_AQUIS | NUMBER(12) | N |  |  |
| 2 | ID_S1250_OC | NUMBER(12) | N |  |  |
| 3 | IND_AQUIS | VARCHAR2(1) | N |  |  |
| 4 | VLR_TOT_AQUIS | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1250_AQUIS

**FKs**:
- ID_S1250_OC → ESOCIAL_PGER_S1250_OC(ID_S1250_OC)

**Indexes**:
- UK_ESOCIAL_PGER_S1250_AQUIS_1 (UNIQUE): (ID_S1250_OC, IND_AQUIS)

---

## ESOCIAL_PGER_S1250_EMPREGADOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1250_EMP | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(15) | N |  |  |

**PK**: ID_S1250_EMP

**FKs**:
- ID_PGER_APUR → ESOCIAL_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_ESOCIAL_PGER_S1250_EMP_001 (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## ESOCIAL_PGER_S1250_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1250_NF | NUMBER(12) | N |  |  |
| 2 | ID_S1250_PRODUTOR | NUMBER(12) | N |  |  |
| 3 | SERIE_DOCTO | VARCHAR2(5) | N |  |  |
| 4 | NUM_DOCTO | VARCHAR2(14) | N |  |  |
| 5 | DATA_EMISSAO | DATE | Y |  |  |
| 6 | VLR_BRUTO_NF | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CP_DESC_PR_NF | NUMBER(17,2) | Y |  |  |
| 8 | VLR_RAT_DESC_PR_NF | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SENAR_DESC_NF | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1250_NF

**FKs**:
- ID_S1250_PRODUTOR → ESOCIAL_PGER_S1250_PRODUTOR(ID_S1250_PRODUTOR)

**Indexes**:
- UK_ESOCIAL_PGER_S1250_NF_01 (UNIQUE): (ID_S1250_PRODUTOR, SERIE_DOCTO, NUM_DOCTO)

---

## ESOCIAL_PGER_S1250_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1250_OC | NUMBER(12) | N |  |  |
| 2 | ID_S1250_EMP | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |

**PK**: ID_S1250_OC

**FKs**:
- ID_S1250_EMP → ESOCIAL_PGER_S1250_EMPREGADOR(ID_S1250_EMP)

**Indexes**:
- UK_ESOCIAL_PGER_S1250_OC_001 (UNIQUE): (ID_S1250_EMP, DAT_OCORRENCIA)

---

## ESOCIAL_PGER_S1250_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1250_PROC | NUMBER(12) | N |  |  |
| 2 | ID_S1250_PRODUTOR | NUMBER(12) | N |  |  |
| 3 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 4 | COD_SUSP | VARCHAR2(14) | N |  |  |
| 5 | VLR_CPN_NRET | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RAT_NRET | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SENAR_NRET | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1250_PROC

**FKs**:
- ID_S1250_PRODUTOR → ESOCIAL_PGER_S1250_PRODUTOR(ID_S1250_PRODUTOR)

**Indexes**:
- UK_ESOCIAL_PGER_S1250_PROC_01 (UNIQUE): (ID_S1250_PRODUTOR, NUM_PROC_ADJ, COD_SUSP)

---

## ESOCIAL_PGER_S1250_PROC_COL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1250_PROC_COL | NUMBER(12) | N |  |  |
| 2 | ID_S1250_AQUIS | NUMBER(12) | N |  |  |
| 3 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 4 | COD_SUSP | VARCHAR2(14) | N |  |  |
| 5 | VLR_CPN_NRET | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RAT_NRET | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SENAR_NRET | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1250_PROC_COL

**FKs**:
- ID_S1250_AQUIS → ESOCIAL_PGER_S1250_AQUIS(ID_S1250_AQUIS)

**Indexes**:
- UK_ESOC_PGER_S1250_PROC_COL_01 (UNIQUE): (ID_S1250_AQUIS, NUM_PROC_ADJ, COD_SUSP)

---

## ESOCIAL_PGER_S1250_PRODUTOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1250_PRODUTOR | NUMBER(12) | N |  |  |
| 2 | ID_S1250_AQUIS | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO_PROD | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO_PROD | VARCHAR2(14) | N |  |  |
| 5 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CP_DESC_PR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RAT_DESC_PR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SENAR_DESC | NUMBER(17,2) | Y |  |  |
| 9 | IND_OPC_CP | VARCHAR2(1) | Y |  |  |

**PK**: ID_S1250_PRODUTOR

**FKs**:
- ID_S1250_AQUIS → ESOCIAL_PGER_S1250_AQUIS(ID_S1250_AQUIS)

**Indexes**:
- UK_ESOCIAL_PGER_S1250_PRO_01 (UNIQUE): (ID_S1250_AQUIS, TP_INSCRICAO_PROD, NR_INSCRICAO_PROD)

---

## ESOCIAL_PGER_S1300_CONTRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1300_CONTRIB | NUMBER(12) | N |  |  |
| 2 | ID_S1300_OC | NUMBER(12) | N |  |  |
| 3 | CNPJ_CONTRIB_SIND | VARCHAR2(14) | Y |  |  |
| 4 | TP_CONTRIB | CHAR(1) | Y |  |  |
| 5 | VLR_CNPJ_CONTRIB | NUMBER(17,2) | Y |  |  |

**PK**: ID_S1300_CONTRIB

**FKs**:
- ID_S1300_OC → ESOCIAL_PGER_S1300_OC(ID_S1300_OC)

---

## ESOCIAL_PGER_S1300_EMPREGADOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1300_EMP | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(15) | N |  |  |

**PK**: ID_S1300_EMP

**FKs**:
- ID_PGER_APUR → ESOCIAL_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_ESOCIAL_PGER_S1300_EMP_001 (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## ESOCIAL_PGER_S1300_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S1300_OC | NUMBER(12) | N |  |  |
| 2 | ID_S1300_EMP | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  |  |

**PK**: ID_S1300_OC

**FKs**:
- ID_S1300_EMP → ESOCIAL_PGER_S1300_EMPREGADOR(ID_S1300_EMP)

**Indexes**:
- UK_ESOCIAL_PGER_S1300_OC_001 (UNIQUE): (ID_S1300_EMP, DAT_OCORRENCIA)

---

## ESOCIAL_PGER_S3000_EVT
**Comment**: Tabela de Exclusao de Eventos - S3000

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S3000_EVT | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_ESOCIAL_PGER_S3000_EVT |
| 2 | ID_OC_EXCL | NUMBER(12) | N |  | Identificador da Ocorrencia do evento que esta sendo excluido. |
| 3 | TIPO_EVENTO_EXCL | VARCHAR2(50) | N |  | Tipo do evento que esta sendo excluido (S-1200 ).  (S-3000 - infoExclusao - tpEvento) |
| 4 | TP_INSCRICAO | VARCHAR2(2) | Y |  | Código correspondente ao tipo de inscrição |
| 5 | NR_INSCRICAO | VARCHAR2(15) | Y |  | Número de inscrição do contribuinte |
| 6 | CPF_TRABALHADOR | VARCHAR2(11) | Y |  | Preencher com o número do CPF do trabalhador. |
| 7 | NIS_TRABALHADOR | VARCHAR2(11) | Y |  | Preencher com o Número de Identificação Social - NIS, |

**PK**: ID_S3000_EVT

**Indexes**:
- UK_ESOCIAL_PGER_S3000_EVT_001 (UNIQUE): (TIPO_EVENTO_EXCL, ID_OC_EXCL)

---

## ESOCIAL_PGER_S3000_OC
**Comment**: Tabela de Ocorrencias do registro S3000.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_S3000_OC | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_ESOCIAL_PGER_S3000_OC |
| 2 | ID_PGER_EVT | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | DAT_OCORRENCIA | DATE | N |  | Data de Ocorrencia |
| 4 | IND_STATUS | CHAR(1) | Y |  | Status de Controle das Ocorrências.  Dominio ESOCIAL_STATUS_PGER_V |
| 5 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificaão nica do evento (R2098 - evtReabreEvPer- id, R2099 - evtFechaEvPer- id). |
| 7 | IND_OPER | CHAR(1) | Y |  | Nao se aplica ao evento S-3000. |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  | Nao se aplica ao evento S-3000. |
| 9 | IND_TP_AMB | CHAR(1) | Y |  | Identificacao do ambiente (S3000 - ideEvento - tpAmb). Dominio 1 - Producao 2 - Producao restrita - dados reais; 3 - Producao restrita - dados ficticios. |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  | Processo de Emissao do Evento (S3000 - ideEvento - procEmi). Dominio 1 - Aplicativo do contribuinte; 2 - Aplicativo governamental. |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  | Versao do Processo de Emissao do Evento. (S3000 - ideEvento - verProc). Informar a versao do aplicativo emissor do evento. |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(12) | Y |  | Versao do Layout do EFD-ESOCIAL. Dominio ESOCIAL_VERSAO_LAYOUT_V. "v01_00_00". |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  | Status Apresentado no Painel de Eventos, campo Situacao. Dominio ESOCIAL_STATUS_PAINEL_V. |
| 14 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_ESOCIAL_OUT. |
| 15 | NUM_RECIBO_EXCL | VARCHAR2(52) | Y |  | Numero do recibo do evento que esta sendo excluido. (S-3000 - infoExclusao - nrRecEvt) |
| 16 | DAT_APUR | DATE | Y |  | Período de referencia do evento que esta sendo excluido. (S-3000 - infoExclusao - perApur) |

**PK**: ID_S3000_OC

**FKs**:
- ID_PGER_EVT → ESOCIAL_PGER_S3000_EVT(ID_S3000_EVT)

**Indexes**:
- UK_ESOCIAL_PGER_S3000_OC_001 (UNIQUE): (ID_PGER_EVT, DAT_OCORRENCIA)

---

