# Módulo: SAICS (SAICS) - 16 tabelas

## SAICS_COD_CHAVE
**Comment**: Contem o conjunto de registros de codigos chave do SAICS previstos no arquivo TFIX82

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CHAVE | NUMBER(2) | N |  |  |
| 2 | COD_MODELO_DOCTO | VARCHAR2(2) | N |  |  |
| 3 | DESCRICAO_MODELO | VARCHAR2(60) | N |  |  |

**PK**: COD_CHAVE

---

## SAICS_COD_CHAVE_TDOCTO
**Comment**: Tabela que contem a relação entre tipos de documentos e codigos chave do SAICS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 2 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 3 | COD_CHAVE | NUMBER(2) | N |  | Codigo de chave utilizado no modulo SAICS |

**PK**: GRUPO_DOCTO, COD_DOCTO

**FKs**:
- COD_CHAVE → SAICS_COD_CHAVE(COD_CHAVE)

---

## SAICS_COD_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_DSC_PRODUTO | CHAR(1) | N |  |  |
| 2 | COD_SUG_PRODUTO | VARCHAR2(60) | N |  |  |
| 3 | GRUPO_UND_PADRAO | VARCHAR2(9) | N |  |  |
| 4 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |

**PK**: IND_DSC_PRODUTO

---

## SAICS_ENQUAD_LEGAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ENQ_LEGAL | NUMBER(4) | N |  |  |
| 3 | COD_DESCRICAO | VARCHAR2(2) | Y |  |  |
| 4 | NUM_ANEXO | VARCHAR2(5) | Y |  |  |
| 5 | NUM_ARTIGO | VARCHAR2(5) | Y |  |  |
| 6 | NUM_INCISO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_ALINEA | VARCHAR2(2) | Y |  |  |
| 8 | NUM_PARAGRAFO | VARCHAR2(2) | Y |  |  |
| 9 | NUM_ITEM | VARCHAR2(2) | Y |  |  |
| 10 | NUM_LETRA | VARCHAR2(2) | Y |  |  |
| 11 | DSC_INFO_COMPL | VARCHAR2(255) | Y |  |  |

**PK**: COD_EMPRESA, COD_ENQ_LEGAL

---

## SAICS_FICHA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_FICHA | VARCHAR2(2) | N |  |  |
| 2 | DESC_FICHA | VARCHAR2(200) | Y |  |  |

**PK**: COD_FICHA

---

## SAICS_NAT_ESTOQUE_FICHA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_NAT_ESTOQUE | VARCHAR2(9) | N |  |  |
| 2 | COD_NAT_ESTOQUE | VARCHAR2(2) | N |  |  |
| 3 | COD_FICHA | VARCHAR2(2) | N |  |  |

**PK**: GRUPO_NAT_ESTOQUE, COD_NAT_ESTOQUE, COD_FICHA

---

## SAICS_PAR_CALC_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_AJUSTE_ICMS | VARCHAR2(8) | N |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

**Indexes**:
- PK_SAICS_PAR_CALC_ALIQ (UNIQUE): (COD_ESTAB, COD_EMPRESA, COD_AJUSTE_ICMS)

---

## SAICS_PRECO_MEDIO_UNIT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PRD_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | VLR_TOTAL_VENDAS | NUMBER(17,2) | Y |  |  |
| 6 | QTD_TOTAL_VENDAS | NUMBER(17,6) | Y |  |  |
| 7 | VLR_PRECO_MEDIO_UNIT | NUMBER(17,6) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PRD_REFERENCIA, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## SAICS_PROCESSO_PRODUCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PROCESSO_PRODUCAO | VARCHAR2(10) | N |  |  |
| 4 | DAT_VALIDADE | DATE | N |  |  |
| 5 | DSC_PROCESSO_PRODUCAO | VARCHAR2(60) | Y |  |  |
| 6 | IND_STATUS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PROCESSO_PRODUCAO, DAT_VALIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SAICS_REL_CONFERENCIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_FICHA | VARCHAR2(2) | N |  |  |
| 3 | CHAVE_QUEBRA | VARCHAR2(100) | N |  |  |
| 4 | CHAVE_ORDENACAO | VARCHAR2(255) | N |  |  |
| 5 | NOME_COLUNA | VARCHAR2(50) | Y |  |  |
| 6 | VALOR | VARCHAR2(255) | Y |  |  |

**Indexes**:
- IX_SAICS_REL_CONFERENCIA_01: (PROC_ID, COD_FICHA)
- IX_SAICS_REL_CONFERENCIA_02: (PROC_ID, COD_FICHA, CHAVE_QUEBRA)
- IX_SAICS_REL_CONFERENCIA_03: (PROC_ID, COD_FICHA, CHAVE_QUEBRA, CHAVE_ORDENACAO, NOME_COLUNA)

---

## SAICS_SALDO_FINAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_DSC_PRODUTO | CHAR(1) | N |  |  |
| 4 | MES_SALDO | NUMBER(2) | N |  |  |
| 5 | ANO_SALDO | NUMBER(4) | N |  |  |
| 6 | VLR_CUSTO | NUMBER(15,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(15,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_DSC_PRODUTO, MES_SALDO, ANO_SALDO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SAICS_TEMPO_MAX_PRODUCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VALID_INICIAL | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | QTD_TEMPO_MAX_PRODUCAO | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, VALID_INICIAL, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SAICS_TEMPO_MAX_PROD_CONJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VALID_INICIAL | DATE | N |  |  |
| 4 | COD_PROCESSO_PRODUCAO | VARCHAR2(10) | N |  |  |
| 5 | QTD_TEMPO_MAX_PRODUCAO | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, VALID_INICIAL, COD_PROCESSO_PRODUCAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SAICS_TP_LANCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TP_LANCTO | NUMBER(6) | N |  |  |
| 2 | DSC_TP_LANCTO | VARCHAR2(255) | Y |  |  |

**PK**: COD_TP_LANCTO

---

## SAICS_TP_LANCTO_REG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_TP_LANCTO | NUMBER(6) | N |  |  |
| 3 | COD_REG_DCA | NUMBER(4) | N |  |  |
| 4 | IND_MOVTO | CHAR(1) | N |  |  |
| 5 | COD_FICHA | VARCHAR2(2) | N |  |  |
| 6 | IND_NORM_DEV | VARCHAR2(1) | Y |  |  |

**PK**: COD_LAYOUT, COD_TP_LANCTO, COD_REG_DCA, IND_MOVTO

---

## SAICS_VALOR_AGREG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_VALIDADE | DATE | N |  |  |
| 4 | VLR_IVA | NUMBER(17,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_VALIDADE

---

