# Módulo: GPE (GPE) - 19 tabelas

## GPE_ARQUIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ARQUIVO | NUMBER(12) | N |  |  |
| 2 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | COD_MUNIC | NUMBER(7) | N |  |  |
| 5 | DATA_INICIAL | DATE | N |  |  |
| 6 | ARQUIVO | BLOB | Y |  |  |
| 7 | NOME_ARQUIVO | VARCHAR2(400) | Y |  |  |
| 8 | DATA_GERACAO | DATE | Y |  |  |
| 9 | COD_USUARIO | VARCHAR2(30) | Y |  |  |
| 10 | IND_PROGRAMACAO | CHAR(1) | Y |  |  |

**PK**: ID_ARQUIVO

**FKs**:
- IDENT_ESTADO, COD_MUNIC, DATA_INICIAL → GPE_LAYOUT_MUNIC(IDENT_ESTADO, COD_MUNIC, DATA_INICIAL)

---

## GPE_CAMPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CAMPO | NUMBER(12) | N |  |  |
| 2 | DESC_CAMPO | VARCHAR2(100) | Y |  |  |
| 3 | TIPO | CHAR(1) | Y |  |  |
| 4 | IND_FORMATO | CHAR(1) | Y |  |  |
| 5 | TAMANHO | NUMBER(5) | Y |  |  |
| 6 | NOME_TABELA | VARCHAR2(50) | Y |  |  |
| 7 | IND_OBRIGATORIO | CHAR(1) | Y |  |  |

**PK**: COD_CAMPO

---

## GPE_CARGA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LINHA_GPE | VARCHAR2(4000) | Y |  |  |

---

## GPE_CONCILIACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNIC | NUMBER(7) | N |  |  |
| 4 | DATA_INICIAL | DATE | N |  |  |
| 5 | DATA_CONCILIACAO | DATE | N |  |  |
| 6 | CNPJ_CPF_PRESTADOR | VARCHAR2(14) | N |  |  |
| 7 | COD_SERVICO | VARCHAR2(20) | N |  |  |
| 8 | VALOR_SERVICO_TOTAL | NUMBER(17,2) | Y |  |  |
| 9 | VALOR_ISS_TOTAL | NUMBER(17,2) | Y |  |  |
| 10 | VALOR_SERVICO_TOTAL_NF | NUMBER(17,2) | Y |  |  |
| 11 | VALOR_ISS_TOTAL_NF | NUMBER(17,2) | Y |  |  |
| 12 | IND_BASE | CHAR(1) | Y |  |  |
| 13 | DAT_ENVIO | DATE | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO, CNPJ_CPF_PRESTADOR, COD_SERVICO

**FKs**:
- IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO → GPE_CONCILIACAO_STATUS(IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO)

---

## GPE_CONCILIACAO_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNIC | NUMBER(7) | N |  |  |
| 4 | DATA_INICIAL | DATE | N |  |  |
| 5 | DATA_CONCILIACAO | DATE | N |  |  |
| 6 | CNPJ_CPF_PRESTADOR | VARCHAR2(14) | N |  |  |
| 7 | COD_SERVICO_NF | VARCHAR2(4) | N |  |  |
| 8 | DATA_EMISSAO_NF | DATE | N |  |  |
| 9 | DATA_FISCAL_NF | DATE | N |  |  |
| 10 | NUM_DOCFIS_NF | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS_NF | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS_NF | VARCHAR2(2) | N |  |  |
| 13 | COD_SERVICO | VARCHAR2(20) | Y |  |  |
| 14 | COD_SERV_LEI116 | VARCHAR2(4) | Y |  |  |
| 15 | DESCRICAO_SERVICO_NF | VARCHAR2(50) | Y |  |  |
| 16 | ALIQUOTA_ISS_NF | NUMBER(7,4) | Y |  |  |
| 17 | VALOR_SERVICO_NF | NUMBER(17,2) | Y |  |  |
| 18 | VALOR_ISS_NF | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOT_NF | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_ISS_1_NF | NUMBER(17,2) | Y |  |  |
| 21 | VLR_DEDUCAO_ISS_NF | NUMBER(17,2) | Y |  |  |
| 22 | IND_CONCILIACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO, CNPJ_CPF_PRESTADOR, COD_SERVICO_NF, DATA_EMISSAO_NF, DATA_FISCAL_NF, NUM_DOCFIS_NF, SERIE_DOCFIS_NF, SUB_SERIE_DOCFIS_NF

---

## GPE_CONCILIACAO_NF_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNIC | NUMBER(7) | N |  |  |
| 4 | DATA_INICIAL | DATE | N |  |  |
| 5 | DATA_CONCILIACAO | DATE | N |  |  |
| 6 | CNPJ_CPF_PRESTADOR | VARCHAR2(14) | N |  |  |
| 7 | COD_SERVICO | VARCHAR2(20) | N |  |  |
| 8 | DATA_EMISSAO | DATE | N |  |  |
| 9 | DATA_FISCAL | DATE | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | ALIQUOTA_ISS | NUMBER(7,4) | Y |  |  |
| 14 | VALOR_SERVICO | NUMBER(17,2) | Y |  |  |
| 15 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  |  |
| 19 | ALIQUOTA_ISS_NF | NUMBER(7,4) | Y |  |  |
| 20 | VALOR_SERVICO_NF | NUMBER(17,2) | Y |  |  |
| 21 | VALOR_ISS_NF | NUMBER(17,2) | Y |  |  |
| 22 | VLR_TOT_NF | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ISS_1_NF | NUMBER(17,2) | Y |  |  |
| 24 | VLR_DEDUCAO_ISS_NF | NUMBER(17,2) | Y |  |  |
| 25 | IND_BASE | CHAR(1) | Y |  |  |
| 26 | DAT_ENVIO | DATE | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO, CNPJ_CPF_PRESTADOR, COD_SERVICO, DATA_EMISSAO, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO → GPE_CONCILIACAO_NF_NF_STATUS(IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO)

---

## GPE_CONCILIACAO_NF_NF_STATUS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNIC | NUMBER(7) | N |  |  |
| 4 | DATA_INICIAL | DATE | N |  |  |
| 5 | DATA_CONCILIACAO | DATE | N |  |  |
| 6 | STATUS | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO

---

## GPE_CONCILIACAO_STATUS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNIC | NUMBER(7) | N |  |  |
| 4 | DATA_INICIAL | DATE | N |  |  |
| 5 | DATA_CONCILIACAO | DATE | N |  |  |
| 6 | STATUS | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNIC, DATA_INICIAL, DATA_CONCILIACAO

---

## GPE_FECHAMENTO_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | NUM_NFTS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | IND_FILTRO | CHAR(1) | Y |  |  |
| 14 | DATA_EMISSAO | DATE | Y |  |  |
| 15 | DATA_FISCAL | DATE | N |  |  |
| 16 | DT_PAGTO_NF | DATE | Y |  |  |
| 17 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 18 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 19 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 20 | SITUACAO | CHAR(1) | Y |  |  |
| 21 | IND_TP_RET | CHAR(1) | Y |  |  |
| 22 | COD_MUNICIPIO | NUMBER(7) | Y |  |  |
| 23 | COD_CEI | VARCHAR2(12) | Y |  |  |
| 24 | IDENT_SERVICO | NUMBER(17) | N |  |  |
| 25 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 28 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 29 | VLR_TERCEIROS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_MAT_APLIC_ISS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_MAT_PROP | NUMBER(17,2) | Y |  |  |
| 33 | VLR_MAT_TERC | NUMBER(17,2) | Y |  |  |
| 34 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 35 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 36 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  |  |
| 37 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 38 | VLR_SERVICO_ITEM | NUMBER(17,2) | Y |  |  |
| 39 | ALIQ_TRIBUTO_ISS_ITEM | NUMBER(7,4) | Y |  |  |
| 40 | VLR_TRIBUTO_ISS_ITEM | NUMBER(17,2) | Y |  |  |
| 41 | VLR_BASE_ISS_1_ITEM | NUMBER(17,2) | Y |  |  |
| 42 | VLR_BASE_ISS_2_ITEM | NUMBER(17,2) | Y |  |  |
| 43 | VLR_BASE_ISS_3_ITEM | NUMBER(17,2) | Y |  |  |
| 44 | VLR_MAT_PROP_ITEM | NUMBER(17,2) | Y |  |  |
| 45 | VLR_MAT_TERC_ITEM | NUMBER(17,2) | Y |  |  |
| 46 | VLR_BASE_ISS_RETIDO_ITEM | NUMBER(17,2) | Y |  |  |
| 47 | VLR_ISS_RETIDO_ITEM | NUMBER(17,2) | Y |  |  |
| 48 | VLR_DEDUCAO_ISS_ITEM | NUMBER(17,2) | Y |  |  |
| 49 | VLR_SUBEMPR_ISS_ITEM | NUMBER(17,2) | Y |  |  |
| 50 | ID_GER | NUMBER(12) | Y |  |  |
| 51 | SEQ_GER_ARQ | NUMBER(12) | Y |  |  |
| 52 | TXT_GER_ARQ | VARCHAR2(4000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM

**FKs**:
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)

**Indexes**:
- IX_FK_SAF_2788: (IDENT_FIS_JUR)

---

## GPE_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | COD_TIPO_ARQ | VARCHAR2(5) | N |  |  |
| 3 | COD_LAYOUT | VARCHAR2(10) | N |  |  |
| 4 | DSC_LAYOUT | VARCHAR2(100) | N |  |  |

**PK**: ID_LAYOUT

**FKs**:
- COD_TIPO_ARQ → GPE_TIPO_ARQUIVO(COD_TIPO_ARQ)

---

## GPE_LAYOUT_CAMPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | COD_CAMPO | NUMBER(12) | N |  |  |
| 3 | REGISTRO | VARCHAR2(10) | N |  |  |
| 4 | ORDEM_CAMPO | NUMBER(3) | N |  |  |
| 5 | DSC_CAMPO | VARCHAR2(100) | Y |  |  |
| 6 | TIPO | VARCHAR2(1) | Y |  |  |
| 7 | POS_INICIAL | NUMBER(5) | Y |  |  |
| 8 | POS_FINAL | NUMBER(5) | Y |  |  |
| 9 | TAMANHO | NUMBER(5) | Y |  |  |
| 10 | DECIMAIS | NUMBER(1) | Y |  |  |
| 11 | TEXTO_FIXO | VARCHAR2(50) | Y |  |  |
| 12 | ID_CONTEUDO | NUMBER(4) | Y |  |  |
| 13 | FORMATO_DATA | VARCHAR2(10) | Y |  |  |
| 14 | TIPO_TAG | NUMBER(1) | Y |  |  |
| 15 | NOME_TAG | VARCHAR2(100) | Y |  |  |
| 16 | NUM_TAG_PAI | NUMBER(2) | Y |  |  |
| 17 | SEQ_TAG | VARCHAR2(50) | Y |  |  |
| 18 | IND_MOSTRA_REL | CHAR(1) | Y | 'N' |  |

**PK**: ID_LAYOUT, COD_CAMPO, REGISTRO, ORDEM_CAMPO

**FKs**:
- ID_LAYOUT → GPE_LAYOUT(ID_LAYOUT)

---

## GPE_LAYOUT_DADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT_DADOS | NUMBER(12) | N |  |  |
| 2 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | COD_MUNIC | NUMBER(7) | N |  |  |
| 5 | DATA_INICIAL | DATE | N |  |  |
| 6 | NOME_ARQ | VARCHAR2(100) | N |  |  |
| 7 | DATA_GERACAO | DATE | N |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | DATA_FISCAL | DATE | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 13 | CNPJ_CPF_PRESTADOR | VARCHAR2(14) | Y |  |  |
| 14 | INSC_MUNICIPAL_PRESTADOR | VARCHAR2(14) | Y |  |  |
| 15 | RAZAO_SOCIAL_PRESTADOR | VARCHAR2(75) | Y |  |  |
| 16 | COD_SERVICO | VARCHAR2(20) | Y |  |  |
| 17 | DESCRICAO_SERVICO | VARCHAR2(1000) | Y |  |  |
| 18 | ALIQUOTA_ISS | NUMBER(7,4) | Y |  |  |
| 19 | VALOR_SERVICO | NUMBER(17,2) | Y |  |  |
| 20 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 21 | DATA_CONCILIACAO | DATE | Y |  |  |
| 22 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 24 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  |  |
| 25 | IND_REJEITAR | CHAR(1) | Y |  |  |

**PK**: ID_LAYOUT_DADOS

---

## GPE_LAYOUT_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: ID_LAYOUT, COD_EMPRESA, COD_ESTAB

---

## GPE_LAYOUT_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LAYOUT | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNIC | NUMBER(7) | N |  |  |
| 4 | DATA_INICIAL | DATE | N |  |  |

**PK**: IDENT_ESTADO, COD_MUNIC, DATA_INICIAL

**FKs**:
- ID_LAYOUT → GPE_LAYOUT(ID_LAYOUT)
- IDENT_ESTADO, COD_MUNIC, DATA_INICIAL → GPE_PRT_MUNIC(IDENT_ESTADO, COD_MUNIC, DATA_INICIAL)

---

## GPE_MENSAGEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MENS | NUMBER(12) | N |  |  |
| 2 | DSC_MENS_1 | VARCHAR2(50) | Y |  |  |
| 3 | DSC_MENS_2 | VARCHAR2(50) | Y |  |  |
| 4 | DSC_MENS_3 | VARCHAR2(50) | Y |  |  |
| 5 | DSC_MENS_4 | VARCHAR2(50) | Y |  |  |

**PK**: COD_MENS

---

## GPE_PRT_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNIC | NUMBER(7) | N |  |  |
| 3 | DATA_INICIAL | DATE | N |  |  |
| 4 | VALOR_SERVICO_DP | NUMBER(17,2) | Y |  |  |
| 5 | VALOR_ISS_DP | NUMBER(17,2) | Y |  |  |
| 6 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 7 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(6) | Y |  |  |
| 10 | IND_RPS_COMPL | CHAR(1) | Y |  |  |
| 11 | IND_FORMATO | CHAR(1) | Y |  |  |
| 12 | IND_DIA | CHAR(1) | Y |  |  |
| 13 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 14 | IND_JUROS_MULTA | CHAR(1) | Y |  |  |
| 15 | LIM_DIA | NUMBER(2) | Y |  |  |
| 16 | VLR_MULTA | NUMBER(5,2) | Y |  |  |
| 17 | VLR_CORR_MON | NUMBER(5,2) | Y |  |  |
| 18 | VLR_JUROS | NUMBER(5,2) | Y |  |  |
| 19 | VLR_LIM_MULTA | NUMBER(5,2) | Y |  |  |
| 20 | IND_TIPO_DIA_TOTALIZ | CHAR(1) | Y | 'C' |  |
| 21 | IND_DATA | CHAR(1) | Y | 'E' |  |

**PK**: IDENT_ESTADO, COD_MUNIC, DATA_INICIAL

---

## GPE_PRT_PRESTADOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CNPJ_CPF_PRESTADOR | VARCHAR2(14) | N |  |  |
| 2 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |

**PK**: CNPJ_CPF_PRESTADOR

---

## GPE_STATUS_FECHAMENTO_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNIC | NUMBER(7) | N |  |  |
| 6 | IND_FILTRO | CHAR(1) | Y |  |  |
| 7 | IND_STATUS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## GPE_TIPO_ARQUIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_ARQ | VARCHAR2(5) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 3 | IND_TIPO_ARQ | VARCHAR2(1) | Y |  |  |
| 4 | SEPARADOR | VARCHAR2(1) | Y |  |  |
| 5 | IND_CAMPO_ALFA | VARCHAR2(1) | Y |  |  |
| 6 | IND_CAMPO_NUM | VARCHAR2(1) | Y |  |  |

**PK**: COD_TIPO_ARQ

---

