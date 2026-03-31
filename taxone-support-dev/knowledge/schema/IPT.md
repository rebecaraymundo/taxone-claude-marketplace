# Módulo: IPT (IPT) - 38 tabelas

## IPT_AJUSTE_IPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_AJUSTE_IPI | VARCHAR2(3) | N |  |  |
| 2 | DSC_AJUSTE_IPI | VARCHAR2(350) | N |  |  |

**PK**: COD_AJUSTE_IPI

---

## IPT_BEB_ESP_MARCA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_MES_INI | NUMBER(6) | N |  |  |
| 4 | ESPECIE | VARCHAR2(30) | N |  |  |
| 5 | MARCA | VARCHAR2(30) | N |  |  |
| 6 | ANO_MES_FIM | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_MES_INI, ESPECIE, MARCA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IPT_BEB_PAR_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_SISTEMA | VARCHAR2(5) | N |  |  |
| 4 | NOM_SISTEMA | VARCHAR2(10) | Y |  |  |
| 5 | VERSAO_APLIC | VARCHAR2(3) | Y |  |  |
| 6 | IND_TP_ESTAB | CHAR(1) | Y |  |  |
| 7 | COD_REPRESENT | VARCHAR2(3) | Y |  |  |
| 8 | IND_ISENCAO | CHAR(1) | Y |  |  |
| 9 | IND_POCO_ARTES | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_SISTEMA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IPT_BEB_PAR_EXTCFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | COD_OPERACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IPT_CALEND_APUR
**Comment**: Controle de calendario para livro P8, OS 1292

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  | IDENT_CALEND_APUR |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  | COD_EMPRESA |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  | COD_ESTAB |
| 4 | IND_PERIODICIDADE | VARCHAR2(2) | Y |  | Indica a periodicidade (mensal, decendial, quinzenal etc) |
| 5 | DAT_APURACAO | DATE | Y |  | Data da apuracao/impressao de acordo com a periodicidade |
| 6 | IND_SITUACAO_APUR | CHAR(1) | Y |  | A = Aberto, F = Fechado |
| 7 | DSC_OBSERVACAO | LONG | Y |  |  |

**PK**: IDENT_CALEND_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → IPT_PRT_GERAL_APUR(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UX_CALEND_APUR (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IND_PERIODICIDADE)

---

## IPT_CALEND_APUR_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 5 | IND_PERIODICIDADE | VARCHAR2(2) | N |  |  |
| 6 | DAT_APURACAO | DATE | N |  |  |
| 7 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 8 | DSC_OBSERVACAO | LONG | Y |  |  |

**PK**: IDENT_CALEND_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → IPT_PRT_GERAL_APUR(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_CALEND_APUR_IES: (COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DAT_APURACAO, IND_PERIODICIDADE)

---

## IPT_CONS_CFOP_CST
**Comment**: Consolidação dos valores de IPI totalizados por CFOP e CST-IPI(campo 146 - Código de Tributação IPI da SAFX08.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_PERIODICIDADE | VARCHAR2(2) | N | 'ME' |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | COD_TRIB_IPI | VARCHAR2(2) | N | ' ' |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y | 0 |  |
| 9 | VLR_BASE_IPI | NUMBER(17,2) | Y | 0 |  |
| 10 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IND_PERIODICIDADE, COD_CFO, COD_TRIB_IPI

---

## IPT_CONS_CFOP_CST_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IND_PERIODICIDADE | VARCHAR2(2) | N | 'ME' |  |
| 7 | COD_CFO | VARCHAR2(4) | N |  |  |
| 8 | COD_TRIB_IPI | VARCHAR2(2) | N | ' ' |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y | 0 |  |
| 10 | VLR_BASE_IPI | NUMBER(17,2) | Y | 0 |  |
| 11 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IND_PERIODICIDADE, COD_CFO, COD_TRIB_IPI

---

## IPT_EMB_CONV_MED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 2 | COD_MED_ORIG | VARCHAR2(8) | N |  |  |
| 3 | COD_MEDIDA_DEST | VARCHAR2(8) | N |  |  |
| 4 | VLR_FATOR_CONV | NUMBER(17,3) | Y |  |  |

**PK**: GRUPO_MEDIDA, COD_MED_ORIG, COD_MEDIDA_DEST

---

## IPT_EMB_MM_ESP_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESP_PROD | VARCHAR2(2) | N |  |  |
| 2 | DSC_ESP_PROD | VARCHAR2(50) | Y |  |  |

**PK**: COD_ESP_PROD

---

## IPT_EMB_MM_NBM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_NBM | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_NBM

---

## IPT_EMB_MM_NCM_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_NCM | VARCHAR2(10) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | COD_ESP_NCM_PRD | VARCHAR2(3) | Y |  |  |
| 8 | DSC_ESP_NCM_PRD | VARCHAR2(50) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | IND_TIPO_IN | CHAR(1) | N | '2' | Recebe o codigo que identifica a IN (1 = 34/2000, 2 = 63/2001 e 3 = 359/2003), incluido na OS1174/V1R9.0 |

**PK**: COD_EMPRESA, COD_ESTAB, COD_NCM, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, IND_TIPO_IN

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IPT_EMB_MM_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | COD_ESP_PROD | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_ESP_PROD → IPT_EMB_MM_ESP_PRD(COD_ESP_PROD)

---

## IPT_EMB_NCM_MEDIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NCM | VARCHAR2(10) | N |  |  |
| 2 | COD_ESPECIE_NCM | NUMBER(3) | N |  |  |
| 3 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 4 | DAT_INI_VIGENCIA | DATE | N | TO_DATE('01/01/1900','DD/MM/YYYY') |  |

**PK**: COD_NCM, DAT_INI_VIGENCIA, COD_ESPECIE_NCM

**FKs**:
- COD_MEDIDA → IPT_EMB_UND_MEDIDA(COD_MEDIDA)

---

## IPT_EMB_UND_ESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 4 | COD_MEDIDA | VARCHAR2(8) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_MEDIDA, COD_MEDIDA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IPT_EMB_UND_MEDIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MEDIDA | VARCHAR2(8) | N |  |  |
| 2 | NUM_MEDIDA | VARCHAR2(2) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_MEDIDA

---

## IPT_GUIA_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_GUIA_RECOL | VARCHAR2(25) | N |  |  |
| 6 | DAT_VENCTO | DATE | Y |  |  |
| 7 | VAL_RECOL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## IPT_GUIA_REC_APUR
**Comment**: Tabela criada na emissao do livro P8 para multiplas priodicidades, OS 1292

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  | IDENT_CALEND_APUR |
| 2 | NUM_GUIA_REC | VARCHAR2(12) | N |  | NUM_GUIA_REC |
| 3 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  | IDENT_ORG_ARRECAD |
| 4 | DAT_ENTREGA | DATE | Y |  | DAT_ENTREGA |
| 5 | DAT_VENCTO | DATE | Y |  | DAT_VENCTO |
| 6 | VLR_GUIA_REC | NUMBER(17,2) | Y |  | VLR_GUIA_REC |
| 7 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  | DSC_LOCAL_ENTREGA |

**PK**: IDENT_CALEND_APUR, NUM_GUIA_REC

**FKs**:
- IDENT_CALEND_APUR → IPT_CALEND_APUR(IDENT_CALEND_APUR)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)

---

## IPT_GUIA_REC_APUR_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  |  |
| 2 | NUM_GUIA_REC | VARCHAR2(12) | N |  |  |
| 3 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |
| 4 | DAT_ENTREGA | DATE | Y |  |  |
| 5 | DAT_VENCTO | DATE | Y |  |  |
| 6 | VLR_GUIA_REC | NUMBER(17,2) | Y |  |  |
| 7 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |

**PK**: IDENT_CALEND_APUR, NUM_GUIA_REC

**FKs**:
- IDENT_CALEND_APUR → IPT_CALEND_APUR_IES(IDENT_CALEND_APUR)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)

---

## IPT_GUIA_REC_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | NUM_GUIA_RECOL | VARCHAR2(25) | N |  |  |
| 7 | DAT_VENCTO | DATE | Y |  |  |
| 8 | VAL_RECOL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_APUR_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)

---

## IPT_OBS_APUR
**Comment**: Tabela utilizada para geracao das observacoes do IPI Sub judice

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  |  |
| 2 | IND_MANUAL_AUTOMAT | CHAR(1) | N |  | Indicador de lancamento manual/automatico, a mesma tabela receber lancamentos do mesmo tipo: M = manual / A = automatico |
| 3 | DSC_OBSERVACAO | VARCHAR2(200) | N |  | Descricao da Observacao/Liminar do IPI-SJ |
| 4 | VLR_OBSERVACAO | NUMBER(17,2) | Y |  |  |
| 5 | IND_DEB_CRED | CHAR(1) | Y |  | Indicador de debito/credito do lancamento |

**PK**: IDENT_CALEND_APUR, IND_MANUAL_AUTOMAT, DSC_OBSERVACAO

**FKs**:
- IDENT_CALEND_APUR → IPT_CALEND_APUR(IDENT_CALEND_APUR)

---

## IPT_OBS_APUR_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  |  |
| 2 | IND_MANUAL_AUTOMAT | CHAR(1) | N |  |  |
| 3 | DSC_OBSERVACAO | VARCHAR2(200) | N |  |  |
| 4 | VLR_OBSERVACAO | NUMBER(17,2) | Y |  |  |
| 5 | IND_DEB_CRED | CHAR(1) | Y |  |  |

**PK**: IDENT_CALEND_APUR, IND_MANUAL_AUTOMAT, DSC_OBSERVACAO

**FKs**:
- IDENT_CALEND_APUR → IPT_CALEND_APUR_IES(IDENT_CALEND_APUR)

---

## IPT_P8_SJ_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_SJ | CHAR(1) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | COD_CFO | VARCHAR2(4) | N |  |  |
| 8 | DSC_LIMINAR | VARCHAR2(37) | N |  |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_NTRIBUT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IND_SJ, IND_E_S, COD_CFO, DSC_LIMINAR

---

## IPT_P8_SJ_COMP_LIM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | DSC_LIMINAR | VARCHAR2(37) | N |  |  |
| 6 | VLR_COMPLEMENTO | NUMBER(17,2) | Y |  |  |
| 7 | IND_DEB_CRED | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, DSC_LIMINAR

---

## IPT_P8_SJ_OBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | DSC_LIMINAR | VARCHAR2(37) | N |  |  |
| 6 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, DSC_LIMINAR

---

## IPT_PERDCOMP_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_APUR | DATE | N |  |  |
| 4 | DATA_FIM_APUR | DATE | N |  |  |
| 5 | CNPJ | VARCHAR2(14) | Y |  |  |
| 6 | SITUACAO_ESPECIAL | VARCHAR2(2) | Y |  |  |
| 7 | DATA_EVENTO | DATE | Y |  |  |
| 8 | PERCENTUAL | NUMBER(5,2) | Y |  |  |
| 9 | ANO_REFERENCIA | NUMBER(4) | Y |  |  |
| 10 | IND_TRIMESTRE | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI_APUR, DATA_FIM_APUR

---

## IPT_PRINCIPAL_APUR
**Comment**: Tabela principal de apuracao do livro P8 conforme IN SRF 394-04, OS 1292

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  | IDENT_CALEND_APUR |
| 2 | IND_ENTRADA_SAIDA | CHAR(1) | N |  | E = entrada / S = saida |
| 3 | COD_CFO | VARCHAR2(4) | N |  | COD_CFO |
| 4 | COMPL_CFOP | VARCHAR2(2) | N |  | COMPL_CFOP |
| 5 | VLR_CONTABIL | NUMBER(17,2) | Y |  | VLR_CONTABIL |
| 6 | VLR_BASE | NUMBER(17,2) | Y |  | VLR_BASE |
| 7 | VLR_TRIBUTO | NUMBER(17,2) | Y |  | VLR_TRIBUTO |
| 8 | VLR_NTRIBUTAVEL | NUMBER(17,2) | Y |  | VLR_NTRIBUTAVEL |
| 9 | VLR_OUTRAS | NUMBER(17,2) | Y |  | VLR_OUTRAS |

**PK**: IDENT_CALEND_APUR, IND_ENTRADA_SAIDA, COD_CFO, COMPL_CFOP

**FKs**:
- IDENT_CALEND_APUR → IPT_CALEND_APUR(IDENT_CALEND_APUR)

---

## IPT_PRINCIPAL_APUR_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  |  |
| 2 | IND_ENTRADA_SAIDA | CHAR(1) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | COMPL_CFOP | VARCHAR2(2) | N |  |  |
| 5 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_NTRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |

**PK**: IDENT_CALEND_APUR, IND_ENTRADA_SAIDA, COD_CFO, COMPL_CFOP

**FKs**:
- IDENT_CALEND_APUR → IPT_CALEND_APUR_IES(IDENT_CALEND_APUR)

---

## IPT_PRT_GERAL_APUR
**Comment**: Tabela criada para apuracao do IPI conforme IN SRF 394-04, OS 1292

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | COD_EMPRESA |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | COD_ESTAB |
| 3 | IND_DECENDIAL | CHAR(1) | Y |  | S ou N |
| 4 | IND_QUINZENAL | CHAR(1) | Y |  | S ou N |
| 5 | IND_CALC_ENTRADAS | CHAR(1) | Y |  | 1 = NCM, 2 = NCM/Produto e 3 = Proporcionalidade |
| 6 | MES_INI_APUR | NUMBER(2) | Y |  | Data que indicara o ponto de partida para o calculo das proporcionalidades das saidas |
| 7 | ANO_INI_APUR | NUMBER(4) | Y |  | Data que indicara o ponto de partida para o calculo das proporcionalidades das saidas |
| 8 | IND_PAR_CFOP | CHAR(1) | Y |  | S ou N |
| 9 | MES_INI_IN446 | NUMBER(2) | Y |  | Mes e Ano de inicio de vigencia para a apuracao segundo IN 446/04 |
| 10 | ANO_INI_IN446 | NUMBER(4) | Y |  |  |
| 11 | IND_MENSAL | CHAR(1) | Y | 'N' |  |
| 12 | TITULO_LIVRO_FISCAL | VARCHAR2(100) | Y | 'Livro Registro de Apuração do IPI - RAIPI - Mo... |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## IPT_RESUMO_APUR
**Comment**: Tabela de resumo da apuracao do livro P8, conforme OS 1292

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  | IDENT_CALEND_APUR |
| 2 | IND_TIPO_LINHA | CHAR(1) | N |  | Indica T = Total e D = Detalhe |
| 3 | COD_OPER_APUR | VARCHAR2(5) | N |  | COD_OPER_APUR |
| 4 | NUM_SEQUENCIAL | NUMBER(3) | N |  | Sequencial para inserção dos vários detalhes |
| 5 | DESCRICAO | VARCHAR2(200) | Y |  | DESCRICAO |
| 6 | VALOR_APURADO | NUMBER(17,2) | Y |  | VALOR_APURADO |
| 7 | IND_DIG_CALC | CHAR(1) | Y |  | IND_DIG_CALC |
| 8 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  | Código de ajuste da apuração do IPI de acordo com a Tabela de Códigos de Ajuste da Apuração do IPI (publicada pela RFB). Este campo é obrigatório para a geração do registro  "E530-Ajustes da Apuração do IPI"  do Sped Fiscal. |
| 9 | NUM_PROC | VARCHAR2(24) | Y |  | Número do documento vinculado ao ajuste, quando houver. |
| 10 | ORIGEM_PROC | CHAR(1) | Y |  | Origem do documento, de acordo com: 0 - Processo Judicial; 1 - Processo Administrativo; 2 - PER/DCOMP; 9 - Outros. |
| 11 | IDENT_NBM | NUMBER(12) | Y |  |  |

**PK**: IDENT_CALEND_APUR, IND_TIPO_LINHA, COD_OPER_APUR, NUM_SEQUENCIAL

**FKs**:
- IDENT_CALEND_APUR → IPT_CALEND_APUR(IDENT_CALEND_APUR)

---

## IPT_RESUMO_APUR_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CALEND_APUR | NUMBER(12) | N |  |  |
| 4 | IND_TIPO_LINHA | CHAR(1) | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | NUM_SEQUENCIAL | NUMBER(3) | N |  |  |
| 7 | DATA_FISCAL | DATE | N |  |  |
| 8 | MOVTO_E_S | CHAR(1) | N |  |  |
| 9 | NORM_DEV | CHAR(1) | N |  |  |
| 10 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 16 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 17 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CALEND_APUR, IND_TIPO_LINHA, COD_OPER_APUR, NUM_SEQUENCIAL, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## IPT_RESUMO_APUR_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CALEND_APUR | NUMBER(12) | N |  |  |
| 2 | IND_TIPO_LINHA | CHAR(1) | N |  |  |
| 3 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 4 | NUM_SEQUENCIAL | NUMBER(3) | N |  |  |
| 5 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 6 | VALOR_APURADO | NUMBER(17,2) | Y |  |  |
| 7 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 8 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  |  |
| 9 | NUM_PROC | VARCHAR2(24) | Y |  |  |
| 10 | ORIGEM_PROC | CHAR(1) | Y |  |  |

**PK**: IDENT_CALEND_APUR, IND_TIPO_LINHA, COD_OPER_APUR, NUM_SEQUENCIAL

**FKs**:
- IDENT_CALEND_APUR → IPT_CALEND_APUR_IES(IDENT_CALEND_APUR)

---

## IPT_RESUMO_APUR_IES_AJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | IDENT_CALEND_APUR | NUMBER(12) | N |  |  |
| 5 | IND_TIPO_LINHA | CHAR(1) | N |  |  |
| 6 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 7 | NUM_SEQUENCIAL | NUMBER(3) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | MOVTO_E_S | CHAR(1) | N |  |  |
| 10 | NORM_DEV | CHAR(1) | N |  |  |
| 11 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 13 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 14 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 15 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 17 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 18 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, IDENT_CALEND_APUR, IND_TIPO_LINHA, COD_OPER_APUR, NUM_SEQUENCIAL, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## IPT_ST_ACORDO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_ACORDO | CHAR(1) | N |  |  |
| 4 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 7 | NUM_SEQ | NUMBER(12) | N |  |  |
| 8 | NUM_ACORDO | VARCHAR2(15) | Y |  |  |
| 9 | ATO_DECLARATORIO | VARCHAR2(3) | Y |  |  |
| 10 | DAT_PEDIDO | DATE | Y |  |  |
| 11 | DAT_ACORDO | DATE | Y |  |  |
| 12 | DAT_INI_VALIDADE | DATE | Y |  |  |
| 13 | DAT_CANC_ACORDO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_ACORDO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_SEQ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IPT_ST_MOV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_OPERACAO | NUMBER(4) | N |  |  |
| 4 | TRIM_OPERACAO | NUMBER(1) | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | DAT_EMISSAO | DATE | N |  |  |
| 8 | DAT_FISCAL | DATE | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 14 | COD_NCM | VARCHAR2(10) | Y |  |  |
| 15 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 17 | VLR_UNIT | NUMBER(21,6) | Y |  |  |
| 18 | ALIQ_TRIBUTO_IPI | NUMBER(7,4) | Y |  |  |
| 19 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 20 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 21 | VLR_DESP_ACESS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_IPI_SUSPENSO | NUMBER(17,2) | Y |  |  |
| 23 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 27 | IDENT_CFO_NF | NUMBER(12) | Y |  |  |
| 28 | IND_NF_COMPL | CHAR(1) | Y |  |  |
| 29 | NUM_NF_ORIGINAL | VARCHAR2(12) | Y |  |  |
| 30 | SERIE_NF_ORIGINAL | VARCHAR2(3) | Y |  |  |
| 31 | DAT_NF_ORIGINAL | DATE | Y |  |  |
| 32 | IDENT_CFO_PROD | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_OPERACAO, TRIM_OPERACAO, MOVTO_E_S, IDENT_FIS_JUR, DAT_EMISSAO, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CFO_NF → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_CFO_PROD → X2012_COD_FISCAL(IDENT_CFO)

**Indexes**:
- IX_FK_SAF_1364: (IDENT_FIS_JUR)

---

## IPT_ST_PAR_MEDIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_UND_PADRAO | VARCHAR2(9) | N |  |  |
| 2 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 3 | COD_UND_PADRAO_MM | VARCHAR2(2) | Y |  |  |
| 4 | VALID_PAR_UND | DATE | N |  |  |

**PK**: GRUPO_UND_PADRAO, COD_UND_PADRAO, VALID_PAR_UND

---

## IPT_ST_PAR_NCM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_ACORDO | CHAR(1) | N |  |  |
| 4 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 7 | NUM_SEQ_ACORDO | NUMBER(12) | N |  |  |
| 8 | IND_TIPO_NCM | CHAR(1) | N |  |  |
| 9 | COD_NCM | VARCHAR2(10) | N |  |  |
| 10 | NUM_SEQ | NUMBER(12) | N |  |  |
| 11 | NUM_ACORDO | VARCHAR2(15) | Y |  |  |
| 12 | ATO_DECLARATORIO | VARCHAR2(3) | Y |  |  |
| 13 | DAT_PEDIDO | DATE | Y |  |  |
| 14 | DAT_ACORDO | DATE | Y |  |  |
| 15 | DAT_INI_VALIDADE | DATE | Y |  |  |
| 16 | DAT_CANC_ACORDO | DATE | Y |  |  |
| 17 | ALIQUOTA_IPI | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_ACORDO, GRUPO_FIS_JUR, COD_FIS_JUR, NUM_SEQ_ACORDO, IND_TIPO_NCM, COD_NCM, NUM_SEQ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, TIPO_ACORDO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_SEQ_ACORDO → IPT_ST_ACORDO(COD_EMPRESA, COD_ESTAB, TIPO_ACORDO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_SEQ)

---

## IPT_ST_PAR_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_ACORDO | CHAR(1) | N |  |  |
| 4 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 7 | NUM_SEQ_ACORDO | NUMBER(12) | N |  |  |
| 8 | IND_TIPO_PRODUTO | CHAR(1) | N |  |  |
| 9 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 10 | IND_PRODUTO | CHAR(1) | N |  |  |
| 11 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 12 | NUM_SEQ | NUMBER(12) | N |  |  |
| 13 | NUM_ACORDO | VARCHAR2(15) | Y |  |  |
| 14 | ATO_DECLARATORIO | VARCHAR2(3) | Y |  |  |
| 15 | DAT_PEDIDO | DATE | Y |  |  |
| 16 | DAT_ACORDO | DATE | Y |  |  |
| 17 | DAT_INI_VALIDADE | DATE | Y |  |  |
| 18 | DAT_CANC_ACORDO | DATE | Y |  |  |
| 19 | ALIQUOTA_IPI | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_ACORDO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_SEQ_ACORDO, IND_TIPO_PRODUTO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, NUM_SEQ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, TIPO_ACORDO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_SEQ_ACORDO → IPT_ST_ACORDO(COD_EMPRESA, COD_ESTAB, TIPO_ACORDO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_SEQ)

---

