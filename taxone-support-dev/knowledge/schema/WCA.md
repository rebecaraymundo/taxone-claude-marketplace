# Módulo: WCA (WCA) - 14 tabelas

## WCA_COLUNA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_COLUNA | NUMBER(38) | N |  |  |
| 2 | NOM_COLUNA | VARCHAR2(30) | N |  |  |
| 3 | DSC_COLUNA | VARCHAR2(200) | N |  |  |
| 4 | TIP_COLUNA | CHAR(1) | Y |  |  |
| 5 | IND_FORMATO | CHAR(1) | Y |  |  |
| 6 | TAMANHO | NUMBER(5) | Y |  |  |
| 7 | TIP_CAMPO_FILTRO | VARCHAR2(2) | N |  |  |

**PK**: ID_COLUNA

**Indexes**:
- IU_WCA_COLUNA (UNIQUE): (NOM_COLUNA)

---

## WCA_ITEM_COLUNA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 2 | ID_TABELA | NUMBER(38) | N |  |  |
| 3 | ID_COLUNA | NUMBER(38) | N |  |  |

**PK**: ID_REGRA_ITEM, ID_TABELA, ID_COLUNA

**FKs**:
- ID_REGRA_ITEM → WCA_REGRA_ITEM(ID_REGRA_ITEM)
- ID_TABELA, ID_COLUNA → WCA_TAB_COLUNA(ID_TABELA, ID_COLUNA)

---

## WCA_ITEM_EXPRESSAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 2 | ID_REGRA_ITEM_1 | NUMBER(38) | N |  |  |
| 3 | TIP_OPER | VARCHAR2(10) | N |  |  |
| 4 | ID_REGRA_ITEM_2 | NUMBER(38) | N |  |  |

**PK**: ID_REGRA_ITEM, ID_REGRA_ITEM_1, TIP_OPER, ID_REGRA_ITEM_2

**FKs**:
- ID_REGRA_ITEM_1 → WCA_REGRA_ITEM(ID_REGRA_ITEM)
- ID_REGRA_ITEM_2 → WCA_REGRA_ITEM(ID_REGRA_ITEM)
- ID_REGRA_ITEM → WCA_REGRA_ITEM(ID_REGRA_ITEM)

---

## WCA_ITEM_FILTRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 2 | ID_TABELA | NUMBER(38) | N |  |  |
| 3 | ID_COLUNA | NUMBER(38) | N |  |  |
| 4 | TIP_OPER | VARCHAR2(10) | N |  |  |
| 5 | VLR_FILTRO | VARCHAR2(70) | N |  |  |
| 6 | IND_AGRUPAR | CHAR(1) | N |  |  |

**PK**: ID_REGRA_ITEM, ID_TABELA, ID_COLUNA, TIP_OPER, VLR_FILTRO

**FKs**:
- ID_REGRA_ITEM → WCA_REGRA_ITEM(ID_REGRA_ITEM)
- ID_TABELA, ID_COLUNA → WCA_TAB_COLUNA(ID_TABELA, ID_COLUNA)

---

## WCA_ITEM_VALOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 2 | VLR_FIXO | VARCHAR2(70) | N |  |  |

**PK**: ID_REGRA_ITEM

**FKs**:
- ID_REGRA_ITEM → WCA_REGRA_ITEM(ID_REGRA_ITEM)

---

## WCA_MENSAGEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 2 | IND_TIPO | CHAR(1) | N |  |  |
| 3 | TEXTO_PADRAO | VARCHAR2(300) | N |  |  |
| 4 | TEXTO_CUSTOM | VARCHAR2(300) | Y |  |  |

**PK**: ID_REGRA_ITEM, IND_TIPO

**FKs**:
- ID_REGRA_ITEM → WCA_REGRA_ITEM(ID_REGRA_ITEM)

---

## WCA_REGRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REGRA | NUMBER(38) | N |  |  |
| 2 | COD_REGRA | VARCHAR2(4) | N |  |  |
| 3 | TIT_REGRA | VARCHAR2(200) | N |  |  |
| 4 | DATA_INICIAL | DATE | N |  |  |
| 5 | IND_ATIVA | CHAR(1) | N |  |  |
| 6 | IND_TIPO_FIXA | CHAR(1) | N |  |  |
| 7 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 8 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 9 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |

**PK**: ID_REGRA

**Indexes**:
- IU_WCA_REGRA (UNIQUE): (COD_REGRA)

---

## WCA_REGRA_GRUPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REGRA | NUMBER(38) | N |  |  |
| 2 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |

**PK**: ID_REGRA, GRUPO_CONTA

---

## WCA_REGRA_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 2 | COD_ITEM | VARCHAR2(30) | N |  |  |
| 3 | TIP_ITEM | CHAR(1) | N |  |  |
| 4 | ID_REGRA | NUMBER(38) | N |  |  |

**PK**: ID_REGRA_ITEM

**FKs**:
- ID_REGRA → WCA_REGRA(ID_REGRA)

**Indexes**:
- IU_WCA_REGRA_ITEM (UNIQUE): (COD_ITEM, TIP_ITEM, ID_REGRA)

---

## WCA_RESULT_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(38) | N |  |  |
| 2 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 3 | COD_SISTEMA_ORIG | VARCHAR2(4) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: PROC_ID, ID_REGRA_ITEM, COD_SISTEMA_ORIG, COD_CONTA

---

## WCA_RESULT_ITEM_MSG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(38) | N |  |  |
| 2 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 3 | COD_SISTEMA_ORIG | NUMBER(38) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | IND_TIPO | CHAR(1) | N |  |  |
| 6 | TEXTO | VARCHAR2(300) | N |  |  |

**PK**: PROC_ID, ID_REGRA_ITEM, COD_SISTEMA_ORIG, COD_CONTA, IND_TIPO

---

## WCA_RESULT_ITEM_VLR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(38) | N |  |  |
| 2 | ID_REGRA_ITEM | NUMBER(38) | N |  |  |
| 3 | COD_SISTEMA_ORIG | VARCHAR2(4) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | VLR_ITEM | NUMBER(17,4) | Y |  |  |

**PK**: PROC_ID, ID_REGRA_ITEM, COD_SISTEMA_ORIG, COD_CONTA

---

## WCA_TABELA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_TABELA | NUMBER(38) | N |  |  |
| 2 | NOM_TABELA | VARCHAR2(30) | N |  |  |
| 3 | DSC_TABELA | VARCHAR2(200) | N |  |  |
| 4 | DATA_INICIAL | DATE | Y |  |  |

**PK**: ID_TABELA

**Indexes**:
- IU_WCA_TABELA (UNIQUE): (NOM_TABELA)

---

## WCA_TAB_COLUNA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_TABELA | NUMBER(38) | N |  |  |
| 2 | ID_COLUNA | NUMBER(38) | N |  |  |
| 3 | NOM_TABELA_CAD | VARCHAR2(30) | Y |  |  |
| 4 | POSICAO | NUMBER(5) | Y |  |  |
| 5 | REGISTRO | VARCHAR2(10) | Y |  |  |
| 6 | INICIO | NUMBER(5) | Y |  |  |
| 7 | TAMANHO | NUMBER(5) | Y |  |  |
| 8 | DECIMAIS | NUMBER(1) | Y |  |  |
| 9 | TIP_COLUNA | CHAR(1) | Y |  |  |
| 10 | IND_FORMATO | CHAR(1) | Y |  |  |

**PK**: ID_TABELA, ID_COLUNA

**FKs**:
- ID_TABELA → WCA_TABELA(ID_TABELA)
- ID_COLUNA → WCA_COLUNA(ID_COLUNA)

---

