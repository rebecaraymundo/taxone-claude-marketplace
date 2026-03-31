# Módulo: ITEM (ITEM) - 27 tabelas

## ITEM_APURAC_CALC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | VAL_APURACAO | NUMBER(17,2) | Y |  |  |
| 7 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 8 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  |  |
| 9 | ID_GER | NUMBER(12) | Y |  |  |
| 10 | SEQ_GER_ARQ | NUMBER(12) | Y |  |  |
| 11 | TXT_GER_ARQ | VARCHAR2(4000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

---

## ITEM_APURAC_DIFAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | NUM_SEQ | NUMBER(12) | N |  |  |
| 7 | VLR_LANC | NUMBER(17,2) | Y |  |  |
| 8 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 9 | DSC_LANC | VARCHAR2(250) | Y |  |  |
| 10 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 11 | COD_PROD_GNRE | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ITEM_APURAC_DIFAL_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | NUM_SEQ | NUMBER(12) | N |  |  |
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

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, IDENT_ESTADO, NUM_SEQ, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ → ITEM_APURAC_DIFAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ)

---

## ITEM_APURAC_DIFAL_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | NUM_ITEM | NUMBER(5) | N |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | IND_PRODUTO | CHAR(1) | N | ' ' |  |
| 16 | COD_PRODUTO | VARCHAR2(60) | N | ' ' |  |
| 17 | DATA_EMISSAO | DATE | Y |  |  |
| 18 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 19 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 20 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 21 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 22 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(13) | N |  |  |
| 26 | USUARIO | VARCHAR2(40) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM, IND_PRODUTO, COD_PRODUTO, NUM_PROCESSO, USUARIO

**Indexes**:
- IX_ITEM_APURAC_DIFAL_NF_01: (COD_EMPRESA, COD_ESTAB, NUM_PROCESSO, USUARIO)

---

## ITEM_APURAC_DIFAL_NF_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_INI | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | DATA_FISCAL | DATE | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | N |  |  |
| 8 | NORM_DEV | CHAR(1) | N |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | NUM_ITEM | NUMBER(5) | N |  |  |
| 15 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 16 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 17 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 18 | DATA_EMISSAO | DATE | Y |  |  |
| 19 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 20 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 21 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 22 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 23 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(13) | N |  |  |
| 27 | USUARIO | VARCHAR2(40) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INI, DATA_FIM, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM, NUM_PROCESSO, USUARIO

---

## ITEM_APURAC_DIFAL_PROC
**Comment**: Tabela que armazena os processos e documentos de arrecadação relacionados ao Lançamento Complementar da Apuração do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | NUM_SEQ | NUMBER(12) | N |  |  |
| 7 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 8 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  | Número do Documento de Arrecadação vinculado ao lançamento contábil. |
| 9 | NUM_PROC | VARCHAR2(60) | Y |  | Número do Processo vinculado ao lançamento contábil. |
| 10 | ORIGEM_PROC | CHAR(1) | Y |  | Origem do processo, de acordo com: 0 - Sefaz; 1 - Justiça Federal; 2 - Justiça Estadual; 9 - Outros. |
| 11 | DSC_PROCESSO | VARCHAR2(250) | Y |  | Descrição do Processo vinculado ao lançamento contábil. |
| 12 | DSC_COMPLEMENTAR | VARCHAR2(250) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ → ITEM_APURAC_DIFAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ)

---

## ITEM_APURAC_DISCR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | VAL_ITEM_DISCRIM | NUMBER(17,2) | Y |  |  |
| 8 | IND_TIPO_DEDUCAO | CHAR(1) | Y |  |  |
| 9 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 10 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 11 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 12 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 13 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 14 | NUM_CERTIFICADO | VARCHAR2(40) | Y |  |  |
| 15 | COD_REGIME_ESPECIAL | VARCHAR2(15) | Y |  | Código do regime especial para o Estado de Santa Catarina, registro 46 da DIME |
| 16 | COD_ORIGEM | VARCHAR2(2) | Y |  | Código da origem para o Estado de Santa Catarina, registro 46 da DIME |
| 17 | NUM_PROC | VARCHAR2(24) | Y |  |  |
| 18 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 19 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 20 | COD_AJUSTE | VARCHAR2(3) | Y |  | Campo criado p/ o Código de Ajuste do Ato Cotepe 70, nos lançamentos da Apuração do ICMS. Foi reutilizado pelo Sped Fiscal, para povoar o Código de Ajuste IPI, nos lançamentos da Apuração do IPI |
| 21 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 22 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  |  |
| 23 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Código de Ajuste Sped Fiscal. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 24 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 25 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 26 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 27 | IND_EST_DEB_CONV | CHAR(1) | Y |  |  |
| 28 | IDENT_ESTADO_CONV | NUMBER(12) | Y |  |  |
| 29 | COD_AJ_ICMS_CONV | VARCHAR2(8) | Y |  |  |
| 30 | COD_AJUSTE_SEF | NUMBER(3) | Y |  |  |
| 31 | COD_CHP_LIC | NUMBER(12) | Y |  |  |
| 32 | COD_MOT_EST | VARCHAR2(2) | Y |  |  |
| 33 | NUM_AUTO_INFRACAO | VARCHAR2(13) | Y |  |  |
| 34 | IND_TRANSF_CENTR | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJ_ICMS_CONV → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ITEM_APURAC_DISCR_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
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
| 19 | NUM_SEQUENCIAL | NUMBER(5) | N | 1 |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, COD_OPER_APUR, NUM_DISCRIMINACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO → ITEM_APURAC_DISCR(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO)

---

## ITEM_APURAC_DISCR_DAPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | DATA_FISCAL | DATE | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | VLR_ESTORNO | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO → ITEM_APURAC_DISCR(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO)

---

## ITEM_APURAC_DISCR_PROC
**Comment**: Tabela que armazena os processos e documentos de arrecadação relacionados ao Lançamento Complementar da Apuração do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 8 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  | Número do Documento de Arrecadação vinculado ao lançamento contábil. |
| 9 | NUM_PROC | VARCHAR2(60) | Y |  | Número do Processo vinculado ao lançamento contábil. |
| 10 | ORIGEM_PROC | CHAR(1) | Y |  | Origem do processo, de acordo com: 0 - Sefaz; 1 - Justiça Federal; 2 - Justiça Estadual; 9 - Outros. |
| 11 | DSC_PROC | VARCHAR2(50) | Y |  | Descrição do Processo vinculado ao lançamento contábil. |
| 12 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 13 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, COD_OPER_APUR, NUM_DISCRIMINACAO, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO → ITEM_APURAC_DISCR(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_2166: (IDENT_OBSERVACAO)

---

## ITEM_APURAC_DISCR_X113

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
| 15 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 16 | DAT_APURACAO | DATE | Y |  |  |
| 17 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 18 | NUM_DISCRIMINACAO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_AJUSTE_SPED, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO → ITEM_APURAC_DISCR(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO)

**Indexes**:
- IX_ITEM_APURAC_DISCR_X113: (DAT_APURACAO, COD_TIPO_LIVRO, COD_OPER_APUR, NUM_DISCRIMINACAO, COD_ESTAB, COD_EMPRESA)

---

## ITEM_APURAC_SUBRS
**Comment**: Tabela de Ajustes SUB-APURACAO do Ressarcimento RS (Registro 1921 - Sped Fiscal)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | Codigo do Livro da Apuracao do ICMS. Valores: 108, 165 |
| 5 | IND_SUB_APUR | VARCHAR2(1) | N |  | Identificador da Sub-apuracao do ICMS. Valores assumidos: 1, 2, 3, 4, 5, 6. |
| 6 | COD_OPER_APUR | VARCHAR2(5) | N |  | Codigo da Operacao da Apuracao (002 - Outros Debitos, 003 - Estorno de Credito, 006 - Outros Creditos, 007 - Estorno de Debitos, 012 - Deducoes) |
| 7 | NUM_DISCRIMINACAO | NUMBER(12) | N |  | Numero do Lancamento |
| 8 | VAL_ITEM_DISCRIM | NUMBER(17,2) | Y |  | Valor do Lancamento |
| 9 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  | Descricao do Lancamento |
| 10 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Código de Ajuste Sped Fiscal. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 11 | IND_TIPO_LANC | CHAR(1) | Y |  | Valores Assumidos: 1, 2, 3 |
| 12 | IND_DIG_CALCULADO | CHAR(1) | Y |  | Identifica a geracao que deu origem ao lancamento. Valores Assumidos: 2 - Geracao da saida a Consumidor Final, 3 - Geracao da saida para outras UFs, 4 - Geracao das Entradas |
| 13 | NUM_PROCESSO | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_TIPO_LIVRO, IND_SUB_APUR, COD_OPER_APUR, NUM_DISCRIMINACAO

**FKs**:
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## ITEM_APURAC_SUBRS_AJUSTE
**Comment**: Tabela de Identificacao do Documento Fiscal dos Ajuste da Sub-Apuracao RS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_AJUSTE | NUMBER(12) | N |  | Sequence |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 6 | IND_SUB_APUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 8 | NUM_DISCRIMINACAO | NUMBER(12) | Y |  |  |
| 9 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 10 | DATA_FISCAL | DATE | Y |  |  |
| 11 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 12 | NORM_DEV | CHAR(1) | Y |  |  |
| 13 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 14 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 15 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 16 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 17 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 18 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 19 | ID_REG_AJUSTE_REF | NUMBER(12) | Y |  | Idenficador do registro de ajuste referente a nota de saida. Preenchido pela nota de entrada. |
| 20 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 21 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  | Numero do documento fiscal de referencia. Preenchido pela nota de saida referenciando uma nota de entrada |
| 22 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  | Serie do documento fiscal de referencia. Preenchido pela nota de saida referenciando uma nota de entrada |
| 23 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  | Sub-serie do documento fiscal de referencia. Preenchido pela nota de saida referenciando uma nota de entrada |
| 24 | DAT_DI | DATE | Y |  | Data de emissao do documento fiscal de referencia. Preenchido pela nota de saida referenciando uma nota de entrada |
| 25 | COD_MODELO | VARCHAR2(2) | Y |  |  Modelo da nota. Preencher tanto para nota de saida quanto para entrada |
| 26 | COD_CFO | VARCHAR2(4) | Y |  | CFOP item da nota. Preencher tanto para nota de saida quanto para entrada |
| 27 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  | Natureza de Operacao do item da nota. Preencher tanto para nota de saida quanto para entrada |
| 28 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  | Produto do item da nota. Preencher tanto para nota de saida quanto para entrada |
| 29 | IND_PRODUTO | CHAR(1) | Y |  | Produto do item da nota. Preencher tanto para nota de saida quanto para entrada |
| 30 | COD_PRODUTO | VARCHAR2(60) | Y |  | Produto do item da nota. Preencher tanto para nota de saida quanto para entrada |
| 31 | DSC_PRODUTO | VARCHAR2(50) | Y |  | Produto do item da nota. Preencher tanto para nota de saida quanto para entrada |
| 32 | GRUPO_MEDIDA_ORIG | VARCHAR2(9) | Y |  | Unidade de medida do item da nota. Preencher tanto para nota de saida quanto para entrada. |
| 33 | COD_MEDIDA_ORIG | VARCHAR2(8) | Y |  | Unidade de medida do item da nota. Preencher tanto para nota de saida quanto para entrada. |
| 34 | GRUPO_MEDIDA_DEST | VARCHAR2(9) | Y |  | Unidade de medida do Cadastro do Produto da nota de Saida. Preencher tanto para nota de saida quanto para entrada. Mas sempre com a Unidade de Medida do cadastro do produto referenciado pela nota de saida. |
| 35 | COD_MEDIDA_DEST | VARCHAR2(8) | Y |  | Unidade de medida do Cadastro do Produto da nota de Saida. Preencher tanto para nota de saida quanto para entrada. Mas sempre com a Unidade de Medida do cadastro do produto referenciado pela nota de saida. |
| 36 | FAT_CONV | NUMBER(17,6) | Y |  | Fator de Conversa de Medidas aplicado ao item da nota. Preencher tanto para nota de saida quanto para entrada. |
| 37 | QTDE_ITEM | NUMBER(17,6) | Y |  | Quantidade do item da nota. Preencher tanto para nota de saida quanto para entrada. |
| 38 | QTDE_CONV | NUMBER(17,6) | Y |  | Quantidade Convertida do item da nota. Preencher tanto para nota de saida quanto para entrada. |
| 39 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  | Percentual de Reducao da Base de Calculo parametrizada para o produto do item da nota de saida. |
| 40 | ALIQ_INTERNA | NUMBER(7,4) | Y |  | Aliquota Interna parametrizada para o produto do item da nota de saida. |
| 41 | ALIQ_FCP | NUMBER(7,4) | Y |  | Aliquota FCP parametrizada para o produto do item da nota de saida. |
| 42 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  | Valor contabil do item da nota de saida. |
| 43 | VLR_BASE_CALC | NUMBER(17,2) | Y |  | Valor da base de calculo calculada com o valor contabil aplicado o percentual de reducao. Preencher para nota de saida. |
| 44 | VLR_ICMS | NUMBER(17,2) | Y |  | Valor do ICMS próprio (destacado ou não) do item da nota de entrada. |
| 45 | VLR_ICMS_ST | NUMBER(17,2) | Y |  | Valor do ICMS-ST (destacado ou não) do item da nota de entrada. |
| 46 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  | Valor do FECP-ST do item da nota de entrada. |
| 47 | VLR_UNIT | NUMBER(17,2) | Y |  | Valor unitario calculado para o item da nota de entrada. |
| 48 | VLR_AJUSTE | NUMBER(17,2) | Y |  | Valor do Ajuste calculado tanto para os itens das notas de entrada e saida. |
| 49 | IND_DIG_CALCULADO | CHAR(1) | Y |  | 2 – lançamento gerado via processo de geração da saida a Consumidor Final. 3 – lançamento gerado via processo de geração das entradas. |
| 50 | NUM_PROCESSO | NUMBER | Y |  |  |
| 51 | GRUPO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 52 | IND_PROD_PRINC | CHAR(1) | Y |  |  |
| 53 | COD_PROD_PRINC | VARCHAR2(60) | Y |  |  |

**PK**: ID_REG_AJUSTE

**FKs**:
- ID_REG_AJUSTE_REF → ITEM_APURAC_SUBRS_AJUSTE(ID_REG_AJUSTE)

**Indexes**:
- IX_ITEM_APURAC_SUBRS_01: (ID_REG_AJUSTE_REF)
- UK_ITEM_APURAC_SUBRS_AJ (UNIQUE): (DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, IND_SUB_APUR, COD_OPER_APUR, NUM_DISCRIMINACAO, COD_ESTAB_ORIG, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, ID_REG_AJUSTE_REF)

---

## ITEM_APURAC_SUBRS_INVENT
**Comment**: Tabela de Identificacao de Produtos Inventariados da Sub-Apuracao RS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_INVENT | NUMBER(12) | N |  | Sequence |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 6 | IND_SUB_APUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 8 | NUM_DISCRIMINACAO | NUMBER(12) | Y |  |  |
| 9 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 10 | DATA_INVENTARIO | DATE | Y |  |  |
| 11 | GRUPO_CONTAGEM | VARCHAR2(1) | Y |  |  |
| 12 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 13 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 14 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 15 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 16 | GRUPO_NAT_ESTOQUE | VARCHAR2(9) | Y |  |  |
| 17 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 18 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | IND_DIG_CALCULADO | VARCHAR2(1) | Y |  | 6 â€“ lancamento gerado via processo de geracao da parcela do credito das mercadorias em estoque |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: ID_REG_INVENT

---

## ITEM_APURAC_SUBST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | IND_UF | CHAR(1) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 9 | VAL_ITEM_DISCRIM | NUMBER(17,2) | Y |  |  |
| 10 | IND_TIPO_DEDUCAO | CHAR(1) | Y |  |  |
| 11 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 12 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 13 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 14 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 15 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 16 | IND_DIG_CALCULADO | CHAR(1) | Y | '1' |  |
| 17 | NUM_PROC | VARCHAR2(14) | Y |  |  |
| 18 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 19 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 20 | COD_AJUSTE | VARCHAR2(3) | Y |  | Campo criado p/ o Código de Ajuste do Ato Cotepe 70, nos lançamentos da Apuração do ICMS. Foi reutilizado pelo Sped Fiscal, para povoar o Código de Ajuste IPI, nos lançamentos da Apuração do IPI |
| 21 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 22 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Código de Ajuste Sped Fiscal. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 23 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 24 | COD_AJUSTE_SEF | NUMBER(3) | Y |  |  |
| 25 | COD_PROD_GNRE | NUMBER(3) | Y |  |  |
| 26 | COD_REGIME_ESPECIAL | VARCHAR2(15) | Y |  | Código do regime especial para o Estado de Santa Catarina, registro 46 da DIME |
| 27 | COD_ORIGEM | VARCHAR2(2) | Y |  | Código da origem para o Estado de Santa Catarina, registro 46 da DIME |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_PROD_GNRE → ICT_GNRE_OL_CLAS_PROD(COD_PROD_GNRE)

---

## ITEM_APURAC_SUBST_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | IND_UF | CHAR(1) | N |  |  |
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

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO → ITEM_APURAC_SUBST(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO)

---

## ITEM_APURAC_SUBST_PROC
**Comment**: Tabela que armazena os processos e documentos de arrecadação relacionados ao Lançamento Complementar da Apuração do ICMS-ST (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | IND_UF | CHAR(1) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 9 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 10 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  | Número do Documento de Arrecadação vinculado ao lançamento contábil. |
| 11 | NUM_PROC | VARCHAR2(60) | Y |  | Número do Processo vinculado ao lançamento contábil. |
| 12 | ORIGEM_PROC | CHAR(1) | Y |  | Origem do processo, de acordo com: 0 - Sefaz; 1 - Justiça Federal; 2 - Justiça Estadual; 9 - Outros. |
| 13 | DSC_PROC | VARCHAR2(50) | Y |  | Descrição do Processo vinculado ao lançamento contábil. |
| 14 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 15 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |

**PK**: DAT_APURACAO, COD_ESTAB, COD_EMPRESA, COD_TIPO_LIVRO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO → ITEM_APURAC_SUBST(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_2168: (IDENT_OBSERVACAO)

---

## ITEM_APURAC_SUBST_X113

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
| 15 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 16 | DAT_APURACAO | DATE | Y |  |  |
| 17 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 18 | IND_UF | CHAR(1) | Y |  |  |
| 19 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 20 | NUM_DISCRIMINACAO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_AJUSTE_SPED, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO → ITEM_APURAC_SUBST(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO)

**Indexes**:
- IX_ITEM_APURAC_SUBST_X113: (DAT_APURACAO, COD_TIPO_LIVRO, IDENT_ESTADO, IND_UF, COD_OPER_APUR, NUM_DISCRIMINACAO, COD_ESTAB, COD_EMPRESA)

---

## ITEM_APUR_DIFAL_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | NUM_SEQ | NUMBER(12) | N |  |  |
| 8 | VLR_LANC | NUMBER(17,2) | Y |  |  |
| 9 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 10 | DSC_LANC | VARCHAR2(250) | Y |  |  |
| 11 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_APUR_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ITEM_APUR_DIFAL_IES_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | NUM_SEQ | NUMBER(12) | N |  |  |
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

**PK**: DAT_APURACAO, COD_ESTAB, INSC_ESTADUAL, COD_EMPRESA, COD_TIPO_LIVRO, IDENT_ESTADO, NUM_SEQ, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ → ITEM_APUR_DIFAL_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ)

---

## ITEM_APUR_DIFAL_IES_PROC
**Comment**: Tabela que armazena os processos e documentos de arrecadação relacionados ao Lançamento Complementar da Apuração do ICMS (Criada para atendimento ao SPED Fiscal).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | NUM_SEQ | NUMBER(12) | N |  |  |
| 8 | SEQ_PROC_ARRECAD | NUMBER(12) | N |  |  |
| 9 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  Número do Documento de Arrecadação vinculado ao lançamento contábil. |
| 10 | NUM_PROC | VARCHAR2(60) | Y |  | Número do Processo vinculado ao lançamento contábil. |
| 11 | ORIGEM_PROC | CHAR(1) | Y |  | Origem do processo, de acordo com: 0 - Sefaz; 1 - Justiça Federal; 2 - Justiça Estadual; 9 - Outros. |
| 12 | DSC_PROCESSO | VARCHAR2(250) | Y |  | Descrição do Processo vinculado ao lançamento contábil. |
| 13 | DSC_COMPLEMENTAR | VARCHAR2(250) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ, SEQ_PROC_ARRECAD

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ → ITEM_APUR_DIFAL_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_SEQ)

---

## ITEM_AP_CALC_SJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | VAL_APURACAO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

---

## ITEM_AP_DISCR_SJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 7 | VAL_ITEM_DISCRIM | NUMBER(17,2) | Y |  |  |
| 8 | IND_TIPO_DEDUCAO | CHAR(1) | Y |  |  |
| 9 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 10 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_OPER_APUR, NUM_DISCRIMINACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

---

## ITEM_DWT_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ROW_ID_CAPA | ROWID | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_FISCAL | DATE | Y |  |  |
| 5 | DATA_EMISSAO | DATE | Y |  |  |
| 6 | DATA_SAIDA_REC | DATE | Y |  |  |
| 7 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 8 | NORM_DEV | CHAR(1) | Y |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 14 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 15 | SITUACAO | CHAR(1) | Y |  |  |
| 16 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 17 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 18 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 19 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 22 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 23 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 24 | IDENT_MEDIDA_ITEM | NUMBER(12) | Y |  |  |
| 25 | IDENT_UND_PADRAO_ITEM | NUMBER(12) | Y |  |  |
| 26 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 27 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 28 | VLR_CREDITO_MVA_SN | NUMBER(17,2) | Y |  |  |
| 29 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 30 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 35 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 36 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 37 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 38 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 39 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 40 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 41 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 42 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 43 | DAT_DI | DATE | Y |  |  |
| 44 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 45 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 46 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 47 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 48 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 49 | IND_SIMPLES_NAC | CHAR(1) | Y |  |  |
| 50 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 51 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 52 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 53 | VALID_PRODUTO | DATE | Y |  |  |
| 54 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 55 | COD_CEST | VARCHAR2(7) | Y |  |  |
| 56 | IDENT_NBM_PROD | NUMBER(12) | Y |  |  |
| 57 | IDENT_MEDIDA_PROD | NUMBER(12) | Y |  |  |
| 58 | IDENT_UND_PADRAO_PROD | NUMBER(12) | Y |  |  |
| 59 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 60 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 61 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 62 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 63 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 64 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 65 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 66 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 67 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 68 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 69 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 70 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 71 | IDENT_ESTADO | NUMBER | Y |  |  |
| 72 | IND_FORNEC_ICMSS | CHAR(1) | Y |  |  |
| 73 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 74 | ALIQ_TRIBUTO_ICMSS | NUMBER(7,4) | Y |  |  |
| 75 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 76 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 77 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 78 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 79 | VLR_BASE_REDU_ICMSS | NUMBER(17,2) | Y |  |  |
| 80 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 81 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 82 | GRUPO_SITUACAO_A | VARCHAR2(9) | Y |  |  |
| 83 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 84 | GRUPO_SITUACAO_B | VARCHAR2(9) | Y |  |  |
| 85 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 86 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 87 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 88 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 89 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 90 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 91 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 92 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 93 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 94 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 95 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 96 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 97 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 98 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  |  |
| 99 | COD_PARAM | NUMBER(3) | Y |  |  |
| 100 | IND_NOTA_DEVOL | CHAR(1) | Y |  |  |
| 101 | COD_RESP_RET | CHAR(1) | Y |  |  |
| 102 | IND_TIPO_REG | CHAR(4) | Y |  |  |
| 103 | GRUPO_PRODUTO_PRINC | VARCHAR2(9) | Y |  |  |
| 104 | IND_PRODUTO_PRINC | CHAR(1) | Y |  |  |
| 105 | COD_PRODUTO_PRINC | VARCHAR2(60) | Y |  |  |
| 106 | IDENT_MEDIDA_PRINC | NUMBER(12) | Y |  |  |
| 107 | GRUPO_MEDIDA_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 108 | COD_MEDIDA_PROD_PRINC | VARCHAR2(8) | Y |  |  |
| 109 | GRUPO_UND_PADRAO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 110 | COD_UND_PADRAO_PROD_PRINC | VARCHAR2(8) | Y |  |  |

**Indexes**:
- IDX_ITEM_DWT_DOCUMENTO: (COD_EMPRESA, COD_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, NUM_ITEM)
- IDX_ITEM_DWT_ORDENACAO: (COD_EMPRESA, COD_ESTAB, IND_TIPO_REG, GRUPO_PRODUTO_PRINC, IND_PRODUTO_PRINC, COD_PRODUTO_PRINC, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO)
- IDX_ITEM_DWT_PRINCIPAL: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IND_TIPO_REG, GRUPO_PRODUTO_PRINC, IND_PRODUTO_PRINC, COD_PRODUTO_PRINC)

---

## ITEM_NFEM_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | CGC_CPF | VARCHAR2(16) | Y |  |  |
| 4 | IE | VARCHAR2(14) | Y |  |  |
| 5 | UF | CHAR(2) | Y |  |  |
| 6 | TP_LOC | CHAR(2) | Y |  |  |
| 7 | LOCALIDADE | VARCHAR2(10) | Y |  |  |
| 8 | MOD_DOC | CHAR(3) | Y |  |  |
| 9 | TDOC_COD | CHAR(5) | Y |  |  |
| 10 | IND_CANC | CHAR(1) | Y |  |  |
| 11 | IND_SIT | CHAR(1) | Y |  |  |
| 12 | IND_TRIB_SUBSTRIB | CHAR(1) | Y |  |  |
| 13 | VAL_ISEN_SUBSTRIB | NUMBER | Y |  |  |
| 14 | VAL_OUTR_SUBSTRIB | NUMBER | Y |  |  |
| 15 | INFEM_SERIE | VARCHAR2(5) | N |  |  |
| 16 | INFEM_NUM | VARCHAR2(15) | N |  |  |
| 17 | INFEM_DTEMIS | DATE | N |  |  |
| 18 | INFEM_DTENTR | DATE | Y |  |  |
| 19 | CATG_COD | CHAR(2) | N |  |  |
| 20 | CADG_COD | VARCHAR2(16) | N |  |  |
| 21 | INFEM_NUM_ITEM | VARCHAR2(5) | N |  |  |
| 22 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 23 | UNID_COD_VENDA | CHAR(3) | Y |  |  |
| 24 | INFEM_DSC | VARCHAR2(150) | Y |  |  |
| 25 | CCUS_COD | VARCHAR2(28) | Y |  |  |
| 26 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 27 | CNBM_COD | VARCHAR2(10) | Y |  |  |
| 28 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 29 | UNID_COD_PADRAO | CHAR(3) | Y |  |  |
| 30 | INFEM_QTD | NUMBER | Y |  |  |
| 31 | INFEM_PES_LIQ | NUMBER | Y |  |  |
| 32 | INFEM_VAL_PRECOUNIT | NUMBER | Y |  |  |
| 33 | INFEM_VAL_PRECOTOT | NUMBER | Y |  |  |
| 34 | INFEM_VAL_DESC | NUMBER | Y |  |  |
| 35 | INFEM_NUM_ROMA | VARCHAR2(12) | Y |  |  |
| 36 | INFEM_DAT_ROMA | DATE | Y |  |  |
| 37 | INFEM_VAL_FRETE | NUMBER | Y |  |  |
| 38 | INFEM_VAL_SEGUR | NUMBER | Y |  |  |
| 39 | INFEM_VAL_DESP | NUMBER | Y |  |  |
| 40 | FEDE_COD | VARCHAR2(5) | Y |  |  |
| 41 | INFEM_TRIBIPI | CHAR(1) | Y |  |  |
| 42 | INFEM_ALIQ_IPI | NUMBER | Y |  |  |
| 43 | INFEM_BAS_IPI | NUMBER | Y |  |  |
| 44 | INFEM_VAL_IPI | NUMBER | Y |  |  |
| 45 | ESTA_COD | CHAR(1) | Y |  |  |
| 46 | ESTB_COD | CHAR(2) | Y |  |  |
| 47 | INFEM_TRIBICM | CHAR(1) | Y |  |  |
| 48 | INFEM_ALIQ_ICMS | NUMBER | Y |  |  |
| 49 | INFEM_BAS_ICMS | NUMBER | Y |  |  |
| 50 | INFEM_VAL_ICMS | NUMBER | Y |  |  |
| 51 | INFEM_BASSUBST_ICMS | NUMBER | Y |  |  |
| 52 | INFEM_VALSUBST_ICMS | NUMBER | Y |  |  |
| 53 | INFEM_VAL_REDICMS | NUMBER | Y |  |  |
| 54 | INFEM_ALIQ_DIFICMS | NUMBER | Y |  |  |
| 55 | INFEM_ISENTA_IPI | NUMBER | Y |  |  |
| 56 | INFEM_ISENTA_ICMS | NUMBER | Y |  |  |
| 57 | INFEM_OUTRA_IPI | NUMBER | Y |  |  |
| 58 | INFEM_OUTRA_ICMS | NUMBER | Y |  |  |
| 59 | INFEM_VAL_CONT | NUMBER | Y |  |  |
| 60 | INFEM_COD_CONT | VARCHAR2(28) | Y |  |  |
| 61 | INFEM_RURAL | CHAR(1) | Y |  |  |
| 62 | INFEM_PETROLEO | CHAR(1) | Y |  |  |
| 63 | INFEM_CHASSI | VARCHAR2(22) | Y |  |  |
| 64 | INFEM_IND_MOV | CHAR(1) | Y |  |  |
| 65 | INFEM_VAL_REDIPI | NUMBER | Y |  |  |
| 66 | NUM01 | NUMBER | Y |  |  |
| 67 | NUM02 | NUMBER | Y |  |  |
| 68 | NUM03 | NUMBER | Y |  |  |
| 69 | VAR01 | VARCHAR2(150) | Y |  |  |
| 70 | VAR02 | VARCHAR2(150) | Y |  |  |
| 71 | VAR03 | VARCHAR2(150) | Y |  |  |
| 72 | VAR04 | VARCHAR2(150) | Y |  |  |
| 73 | VAR05 | VARCHAR2(150) | Y |  |  |
| 74 | UNIN_COD | VARCHAR2(9) | Y |  |  |
| 75 | TIPI_COD | CHAR(2) | Y |  |  |
| 76 | LIPI_COD | CHAR(3) | Y |  |  |
| 77 | INFEM_ALIQ_ST | NUMBER | Y |  |  |
| 78 | INFEM_IND_NAT | CHAR(1) | Y |  |  |
| 79 | INFEM_SIMPLES_NAC | CHAR(3) | Y |  |  |
| 80 | CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, INFEM_NUM, INFEM_SERIE, CADG_COD, INFEM_NUM_ITEM, CATG_COD, INFEM_DTEMIS

**Indexes**:
- ITEM_NFEM_MERCI2: (EMPS_COD, FILI_COD, INFEM_DTENTR, CADG_COD, INFEM_NUM, INFEM_SERIE, INFEM_NUM_ITEM)
- ITEM_NFEM_MERCI3: (EMPS_COD, FILI_COD, CATG_COD, CADG_COD, INFEM_DTENTR, INFEM_NUM, INFEM_NUM_ITEM)

---

## ITEM_NFSD_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | CGC_CPF | VARCHAR2(16) | Y |  |  |
| 4 | IE | VARCHAR2(14) | Y |  |  |
| 5 | UF | CHAR(2) | Y |  |  |
| 6 | TP_LOC | CHAR(2) | Y |  |  |
| 7 | LOCALIDADE | VARCHAR2(10) | Y |  |  |
| 8 | MOD_DOC | CHAR(3) | Y |  |  |
| 9 | TDOC_COD | CHAR(5) | Y |  |  |
| 10 | IND_CANC | CHAR(1) | Y |  |  |
| 11 | IND_SIT | CHAR(1) | Y |  |  |
| 12 | IND_TRIB_SUBSTRIB | CHAR(1) | Y |  |  |
| 13 | VAL_ISEN_SUBSTRIB | NUMBER | Y |  |  |
| 14 | VAL_OUTR_SUBSTRIB | NUMBER | Y |  |  |
| 15 | INFSM_SERIE | VARCHAR2(5) | N |  |  |
| 16 | INFSM_NUM | VARCHAR2(15) | N |  |  |
| 17 | INFSM_DTEMISS | DATE | N |  |  |
| 18 | CATG_COD | CHAR(2) | Y |  |  |
| 19 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 20 | INFSM_NUM_ITEM | VARCHAR2(5) | N |  |  |
| 21 | MATE_COD | VARCHAR2(60) | Y |  |  |
| 22 | UNID_COD_VENDA | CHAR(3) | Y |  |  |
| 23 | INFSM_DSC | VARCHAR2(150) | Y |  |  |
| 24 | CCUS_COD | VARCHAR2(28) | Y |  |  |
| 25 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 26 | NOPE_COD | VARCHAR2(6) | Y |  |  |
| 27 | CNBM_COD | VARCHAR2(10) | Y |  |  |
| 28 | UNID_COD | CHAR(3) | Y |  |  |
| 29 | INFSM_QTD | NUMBER | Y |  |  |
| 30 | INFSM_PES_LIQ | NUMBER | Y |  |  |
| 31 | INFSM_VAL_PRECOUNIT | NUMBER | Y |  |  |
| 32 | INFSM_VAL_PRECOTOT | NUMBER | Y |  |  |
| 33 | INFSM_VAL_DESC | NUMBER | Y |  |  |
| 34 | INFSM_NUM_ROMA | VARCHAR2(12) | Y |  |  |
| 35 | INFSM_DAT_ROMA | DATE | Y |  |  |
| 36 | INFSM_VAL_FRETE | NUMBER | Y |  |  |
| 37 | INFSM_VAL_SEGUR | NUMBER | Y |  |  |
| 38 | INFSM_VAL_DESP | NUMBER | Y |  |  |
| 39 | FEDE_COD | VARCHAR2(5) | Y |  |  |
| 40 | INFSM_TRIBIPI | CHAR(1) | Y |  |  |
| 41 | INFSM_ALIQ_IPI | NUMBER | Y |  |  |
| 42 | INFSM_BAS_IPI | NUMBER | Y |  |  |
| 43 | INFSM_VAL_IPI | NUMBER | Y |  |  |
| 44 | ESTA_COD | CHAR(1) | Y |  |  |
| 45 | ESTB_COD | CHAR(2) | Y |  |  |
| 46 | INFSM_TRIBICM | CHAR(1) | Y |  |  |
| 47 | INFSM_ALIQ_ICMS | NUMBER | Y |  |  |
| 48 | INFSM_BAS_ICMS | NUMBER | Y |  |  |
| 49 | INFSM_VAL_ICMS | NUMBER | Y |  |  |
| 50 | INFSM_BASSUBST_ICMS | NUMBER | Y |  |  |
| 51 | INFSM_VALSUBST_ICMS | NUMBER | Y |  |  |
| 52 | INFSM_VAL_REDICMS | NUMBER | Y |  |  |
| 53 | INFSM_ALIQ_DIFICMS | NUMBER | Y |  |  |
| 54 | INFSM_ISENTA_IPI | NUMBER | Y |  |  |
| 55 | INFSM_ISENTA_ICMS | NUMBER | Y |  |  |
| 56 | INFSM_OUTRA_IPI | NUMBER | Y |  |  |
| 57 | INFSM_OUTRA_ICMS | NUMBER | Y |  |  |
| 58 | INFSM_VAL_CONT | NUMBER | Y |  |  |
| 59 | INFSM_COD_CONT | VARCHAR2(28) | Y |  |  |
| 60 | INFSM_ICMS_FRETE | NUMBER | Y |  |  |
| 61 | INFSM_CHASSI | VARCHAR2(22) | Y |  |  |
| 62 | INFSM_IND_MOV | CHAR(1) | Y |  |  |
| 63 | INFSM_VAL_REDIPI | NUMBER | Y |  |  |
| 64 | NUM01 | NUMBER | Y |  |  |
| 65 | NUM02 | NUMBER | Y |  |  |
| 66 | NUM03 | NUMBER | Y |  |  |
| 67 | VAR01 | VARCHAR2(150) | Y |  |  |
| 68 | VAR02 | VARCHAR2(150) | Y |  |  |
| 69 | VAR03 | VARCHAR2(150) | Y |  |  |
| 70 | VAR04 | VARCHAR2(150) | Y |  |  |
| 71 | VAR05 | VARCHAR2(150) | Y |  |  |
| 72 | UNIN_COD | VARCHAR2(9) | Y |  |  |
| 73 | TIPI_COD | CHAR(2) | Y |  |  |
| 74 | LIPI_COD | CHAR(3) | Y |  |  |
| 75 | INFSM_ALIQ_ST | NUMBER | Y |  |  |
| 76 | CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, INFSM_SERIE, INFSM_NUM, INFSM_NUM_ITEM, INFSM_DTEMISS

**Indexes**:
- ITEM_NFSD_MERCI2: (EMPS_COD, FILI_COD, INFSM_DTEMISS, INFSM_NUM, INFSM_SERIE, CFOP_COD, UF, IND_CANC, INFSM_ALIQ_IPI, INFSM_ALIQ_ICMS)
- ITEM_NFSD_MERCI3: (EMPS_COD, FILI_COD, MATE_COD, INFSM_DTEMISS, CFOP_COD)

---

## ITEM_X_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ROW_ID_CAPA | ROWID | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_FISCAL | DATE | Y |  |  |
| 5 | DATA_EMISSAO | DATE | Y |  |  |
| 6 | DATA_SAIDA_REC | DATE | Y |  |  |
| 7 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 8 | NORM_DEV | CHAR(1) | Y |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 14 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 15 | SITUACAO | CHAR(1) | Y |  |  |
| 16 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 17 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 18 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 19 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 22 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 23 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 24 | IDENT_MEDIDA_ITEM | NUMBER(12) | Y |  |  |
| 25 | IDENT_UND_PADRAO_ITEM | NUMBER(12) | Y |  |  |
| 26 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 27 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 28 | VLR_CREDITO_MVA_SN | NUMBER(17,2) | Y |  |  |
| 29 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 30 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 35 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 36 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 37 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 38 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 39 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 40 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 41 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 42 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 43 | DAT_DI | DATE | Y |  |  |
| 44 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 45 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 46 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 47 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 48 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 49 | IND_SIMPLES_NAC | CHAR(1) | Y |  |  |
| 50 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 51 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 52 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 53 | VALID_PRODUTO | DATE | Y |  |  |
| 54 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 55 | COD_CEST | VARCHAR2(7) | Y |  |  |
| 56 | IDENT_NBM_PROD | NUMBER(12) | Y |  |  |
| 57 | IDENT_MEDIDA_PROD | NUMBER(12) | Y |  |  |
| 58 | IDENT_UND_PADRAO_PROD | NUMBER(12) | Y |  |  |
| 59 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 60 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 61 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 62 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 63 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 64 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 65 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 66 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 67 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 68 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 69 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 70 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 71 | IDENT_ESTADO | NUMBER | Y |  |  |
| 72 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 73 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 74 | IND_FORNEC_ICMSS | CHAR(1) | Y |  |  |
| 75 | ALIQ_TRIBUTO_ICMS | NUMBER | Y |  |  |
| 76 | ALIQ_TRIBUTO_ICMSS | NUMBER | Y |  |  |
| 77 | VLR_TRIBUTO_ICMS | NUMBER | Y |  |  |
| 78 | VLR_TRIBUTO_ICMSS | NUMBER | Y |  |  |
| 79 | VLR_BASE_ICMS_1 | NUMBER | Y |  |  |
| 80 | VLR_BASE_ICMSS | NUMBER | Y |  |  |
| 81 | VLR_BASE_REDU_ICMSS | NUMBER | Y |  |  |
| 82 | GRUPO_SITUACAO_A | VARCHAR2(9) | Y |  |  |
| 83 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 84 | GRUPO_SITUACAO_B | VARCHAR2(9) | Y |  |  |
| 85 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 86 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 87 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 88 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 89 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 90 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 91 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 92 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 93 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 94 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 95 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 96 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 97 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 98 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  |  |
| 99 | COD_PARAM | NUMBER(3) | Y |  |  |
| 100 | IND_NOTA_DEVOL | CHAR(1) | Y |  |  |
| 101 | COD_RESP_RET | CHAR(1) | Y |  |  |
| 102 | IND_TIPO_REG | CHAR(4) | Y |  |  |
| 103 | GRUPO_PRODUTO_PRINC | VARCHAR2(9) | Y |  |  |
| 104 | IND_PRODUTO_PRINC | CHAR(1) | Y |  |  |
| 105 | COD_PRODUTO_PRINC | VARCHAR2(60) | Y |  |  |
| 106 | IDENT_MEDIDA_PRINC | NUMBER(12) | Y |  |  |
| 107 | GRUPO_MEDIDA_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 108 | COD_MEDIDA_PROD_PRINC | VARCHAR2(8) | Y |  |  |
| 109 | GRUPO_UND_PADRAO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 110 | COD_UND_PADRAO_PROD_PRINC | VARCHAR2(8) | Y |  |  |

**Indexes**:
- IDX_ITEM_X_ORDENACAO: (COD_EMPRESA, COD_ESTAB, IND_TIPO_REG, GRUPO_PRODUTO_PRINC, IND_PRODUTO_PRINC, COD_PRODUTO_PRINC, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO)
- IDX_ITEM_X_PRINCIPAL: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IND_TIPO_REG, GRUPO_PRODUTO_PRINC, IND_PRODUTO_PRINC, COD_PRODUTO_PRINC)

---

