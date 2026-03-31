# Módulo: GEMT (GEMT) - 13 tabelas

## GEMT_ARQUIVO_XML

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_GER | NUMBER(12) | N |  |  |
| 2 | DSC_DECLARACAO_XML | CLOB | Y |  |  |

**PK**: ID_GER

---

## GEMT_CARGA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LINHA_GEMT | VARCHAR2(4000) | Y |  |  |

---

## GEMT_DARF_CTA_CONTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_DARF | VARCHAR2(4) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_DARF, COD_CONTA

---

## GEMT_DET_CONT_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_CONTEUDO | NUMBER(4) | N |  |  |
| 2 | GRUPO_TRIBUTO | VARCHAR2(1) | N |  |  |
| 3 | DESC_CONT | VARCHAR2(250) | N |  |  |
| 4 | DESC_CONT_BD | VARCHAR2(250) | N |  |  |
| 5 | IND_PARAM_SELEC | VARCHAR2(1) | Y |  | Indicador se o campo do layout será utilizado ou não em parâmetros para seleção ( S ou N ). |
| 6 | TIPO_COL_BD | VARCHAR2(10) | Y |  |  |
| 7 | TAM_COL_BD | NUMBER(3) | Y |  |  |
| 8 | DEC_COL_BD | NUMBER(2) | Y |  |  |

**PK**: ID_CONTEUDO

---

## GEMT_GERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_GER | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_ARQ | VARCHAR2(5) | Y |  |  |
| 5 | COD_LAYOUT | VARCHAR2(3) | Y |  |  |
| 6 | GRUPO_TRIBUTO | VARCHAR2(1) | Y |  |  |
| 7 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | DATA_GER_INI | DATE | Y |  |  |
| 9 | DATA_GER_FIM | DATE | Y |  |  |
| 10 | NUM_LOTE | NUMBER(12) | Y |  |  |
| 11 | IND_SITUACAO_APUR | CHAR(1) | Y |  | (E)nviado - (P)ago - (C)ancelado |

**PK**: ID_GER

**Indexes**:
- UK_GEMT_GERACAO (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO, DATA_GER_INI, DATA_GER_FIM, NUM_LOTE)

---

## GEMT_GERACAO_DADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_GER | NUMBER(12) | N |  |  |
| 2 | LINHA_REG | NUMBER(12) | N |  |  |
| 3 | ORDEM_CAMPO | NUMBER(4) | N |  |  |
| 4 | TIPO | CHAR(1) | Y |  |  |
| 5 | CAMPO_DESC | VARCHAR2(100) | Y |  |  |
| 6 | CAMPO_ORIGEM | VARCHAR2(500) | Y |  |  |
| 7 | CAMPO_RETORNO | VARCHAR2(500) | Y |  |  |

**PK**: ID_GER, LINHA_REG, ORDEM_CAMPO

**FKs**:
- ID_GER → GEMT_GERACAO(ID_GER)

---

## GEMT_GERACAO_IMP_STATUS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_GER | NUMBER(12) | N |  |  |
| 2 | LINHA_REG | NUMBER(12) | N |  |  |
| 3 | STATUS_LINHA | CHAR(1) | Y |  |  |
| 4 | AUT_BANCARIA | VARCHAR2(100) | Y |  |  |

**PK**: ID_GER, LINHA_REG

**FKs**:
- ID_GER → GEMT_GERACAO(ID_GER)

---

## GEMT_LAYOUT_CAPA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_ARQ | VARCHAR2(5) | N |  |  |
| 2 | COD_LAYOUT | VARCHAR2(3) | N |  |  |
| 3 | DESC_LAYOUT | VARCHAR2(50) | Y |  |  |
| 4 | GRUPO_TRIBUTO | VARCHAR2(1) | N |  |  |
| 5 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 6 | IND_ATIVO | CHAR(1) | Y | 'S' |  |
| 7 | DSC_DECLARACAO_XML | VARCHAR2(255) | Y |  |  |

**PK**: COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO

**FKs**:
- COD_TIPO_ARQ → GEMT_TIPO_ARQUIVO(COD_TIPO_ARQ)

---

## GEMT_LAYOUT_DETALHE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_ARQ | VARCHAR2(5) | N |  |  |
| 2 | COD_LAYOUT | VARCHAR2(3) | N |  |  |
| 3 | GRUPO_TRIBUTO | VARCHAR2(1) | N |  |  |
| 4 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 5 | ORDEM_CAMPO | NUMBER(3) | N |  |  |
| 6 | DSC_CAMPO | VARCHAR2(100) | Y |  |  |
| 7 | TIPO | VARCHAR2(1) | Y |  |  |
| 8 | POS_INICIAL | NUMBER(5) | Y |  |  |
| 9 | POS_FINAL | NUMBER(5) | Y |  |  |
| 10 | TAMANHO | NUMBER(5) | Y |  |  |
| 11 | DECIMAIS | NUMBER(1) | Y |  |  |
| 12 | TEXTO_FIXO | VARCHAR2(50) | Y |  |  |
| 13 | ID_CONTEUDO | NUMBER(4) | Y |  |  |
| 14 | IND_AGRUPA | CHAR(1) | Y | 'N' |  |
| 15 | FORMATO_DATA | VARCHAR2(10) | Y |  |  |
| 16 | TIPO_TAG | NUMBER(1) | Y |  |  |
| 17 | NOME_TAG | VARCHAR2(100) | Y |  |  |
| 18 | NUM_TAG_PAI | NUMBER(2) | Y |  |  |
| 19 | SEQ_TAG | VARCHAR2(50) | Y |  |  |
| 20 | IND_MOSTRA_REL | CHAR(1) | Y | 'N' |  |
| 21 | IND_AGRUPA_RETORNO | CHAR(1) | Y | 'N' |  |
| 22 | IND_PAINEL | CHAR(1) | Y | 'N' |  |

**PK**: COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO, ORDEM_CAMPO

**FKs**:
- COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO → GEMT_LAYOUT_CAPA(COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO)

---

## GEMT_LAYOUT_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_ARQ | VARCHAR2(5) | N |  |  |
| 2 | COD_LAYOUT | VARCHAR2(3) | N |  |  |
| 3 | GRUPO_TRIBUTO | VARCHAR2(1) | N |  |  |
| 4 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO, COD_EMPRESA, COD_ESTAB

---

## GEMT_LAYOUT_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_ARQ | VARCHAR2(5) | N |  |  |
| 2 | COD_LAYOUT | VARCHAR2(3) | N |  |  |
| 3 | GRUPO_TRIBUTO | VARCHAR2(1) | N |  |  |
| 4 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 5 | ID_CONTEUDO | NUMBER(4) | N |  |  |
| 6 | IND_OP_LOGIC | VARCHAR2(3) | Y |  |  |
| 7 | IND_OP_COMPARA | VARCHAR2(2) | N |  |  |
| 8 | TEXTO_FIXO | VARCHAR2(50) | Y |  |  |
| 9 | DATA_FIXO | DATE | Y |  |  |
| 10 | NUMERO_FIXO | NUMBER(21,6) | Y |  |  |

**PK**: COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO, ID_CONTEUDO, IND_OP_COMPARA

**FKs**:
- COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO → GEMT_LAYOUT_CAPA(COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO)

---

## GEMT_LAYOUT_PERFIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_ARQ | VARCHAR2(5) | N |  |  |
| 2 | COD_LAYOUT | VARCHAR2(3) | N |  |  |
| 3 | GRUPO_TRIBUTO | VARCHAR2(1) | N |  |  |
| 4 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 5 | COD_PERFIL | VARCHAR2(3) | N |  |  |
| 6 | DSC_PERFIL | VARCHAR2(100) | N |  |  |

**PK**: COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO, COD_PERFIL

**FKs**:
- COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO → GEMT_LAYOUT_CAPA(COD_TIPO_ARQ, COD_LAYOUT, GRUPO_TRIBUTO, COD_TRIBUTO)

---

## GEMT_TIPO_ARQUIVO

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

