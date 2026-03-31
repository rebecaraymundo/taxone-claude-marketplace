# Módulo: DIMOB (DIMOB) - 14 tabelas

## DIMOB_DADOS_INICIAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CNPJ_DECLARANTE | NUMBER | N |  |  |
| 2 | NOME_EMPRESARIAL | VARCHAR2(60) | Y |  |  |
| 3 | CPF_RESPONSAVEL_RFB | VARCHAR2(11) | Y |  |  |
| 4 | ENDERECO_CONTRIBUINTE | VARCHAR2(120) | Y |  |  |
| 5 | UF_CONTRIBUINTE | VARCHAR2(2) | Y |  |  |
| 6 | CODIGO_MUNICIPIO_CONTRIBUINTE | VARCHAR2(4) | Y |  |  |

**PK**: CNPJ_DECLARANTE

---

## DIMOB_ESTADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CODIGO_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | N |  |  |

**PK**: CODIGO_ESTADO

---

## DIMOB_EVENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_EVENTO | NUMBER | N |  |  |
| 2 | DESC_EVENTO | VARCHAR2(50) | N |  |  |

**PK**: ID_EVENTO

---

## DIMOB_FICHA_LOCACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CNPJ_DECLARANTE | NUMBER | N |  |  |
| 2 | ANO_CALENDARIO | VARCHAR2(4) | N |  |  |
| 3 | SEQUENCIAL_LOCACAO | NUMBER | N | 1 |  |
| 4 | CPF_CNPJ_LOCADOR | VARCHAR2(14) | Y |  |  |
| 5 | NOME_LOCADOR | VARCHAR2(60) | Y |  |  |
| 6 | CPF_CNPJ_LOCATARIO | VARCHAR2(14) | Y |  |  |
| 7 | NOME_LOCATARIO | VARCHAR2(60) | Y |  |  |
| 8 | NUMERO_CONTRATO | VARCHAR2(6) | Y |  |  |
| 9 | DATA_CONTRATO | DATE | Y |  |  |
| 10 | VALOR_ALUGUEL_JAN | NUMBER(12,2) | Y | 0 |  |
| 11 | VALOR_COMISSAO_JAN | NUMBER(12,2) | Y | 0 |  |
| 12 | VALOR_IMPOSTO_JAN | NUMBER(12,2) | Y | 0 |  |
| 13 | VALOR_ALUGUEL_FEV | NUMBER(12,2) | Y | 0 |  |
| 14 | VALOR_COMISSAO_FEV | NUMBER(12,2) | Y | 0 |  |
| 15 | VALOR_IMPOSTO_FEV | NUMBER(12,2) | Y | 0 |  |
| 16 | VALOR_ALUGUEL_MAR | NUMBER(12,2) | Y | 0 |  |
| 17 | VALOR_COMISSAO_MAR | NUMBER(12,2) | Y | 0 |  |
| 18 | VALOR_IMPOSTO_MAR | NUMBER(12,2) | Y | 0 |  |
| 19 | VALOR_ALUGUEL_ABR | NUMBER(12,2) | Y | 0 |  |
| 20 | VALOR_COMISSAO_ABR | NUMBER(12,2) | Y | 0 |  |
| 21 | VALOR_IMPOSTO_ABR | NUMBER(12,2) | Y | 0 |  |
| 22 | VALOR_ALUGUEL_MAI | NUMBER(12,2) | Y | 0 |  |
| 23 | VALOR_COMISSAO_MAI | NUMBER(12,2) | Y | 0 |  |
| 24 | VALOR_IMPOSTO_MAI | NUMBER(12,2) | Y | 0 |  |
| 25 | VALOR_ALUGUEL_JUN | NUMBER(12,2) | Y | 0 |  |
| 26 | VALOR_COMISSAO_JUN | NUMBER(12,2) | Y | 0 |  |
| 27 | VALOR_IMPOSTO_JUN | NUMBER(12,2) | Y | 0 |  |
| 28 | VALOR_ALUGUEL_JUL | NUMBER(12,2) | Y | 0 |  |
| 29 | VALOR_COMISSAO_JUL | NUMBER(12,2) | Y | 0 |  |
| 30 | VALOR_IMPOSTO_JUL | NUMBER(12,2) | Y | 0 |  |
| 31 | VALOR_ALUGUEL_AGO | NUMBER(12,2) | Y | 0 |  |
| 32 | VALOR_COMISSAO_AGO | NUMBER(12,2) | Y | 0 |  |
| 33 | VALOR_IMPOSTO_AGO | NUMBER(12,2) | Y | 0 |  |
| 34 | VALOR_ALUGUEL_SET | NUMBER(12,2) | Y | 0 |  |
| 35 | VALOR_COMISSAO_SET | NUMBER(12,2) | Y | 0 |  |
| 36 | VALOR_IMPOSTO_SET | NUMBER(12,2) | Y | 0 |  |
| 37 | VALOR_ALUGUEL_OUT | NUMBER(12,2) | Y | 0 |  |
| 38 | VALOR_COMISSAO_OUT | NUMBER(12,2) | Y | 0 |  |
| 39 | VALOR_IMPOSTO_OUT | NUMBER(12,2) | Y | 0 |  |
| 40 | VALOR_ALUGUEL_NOV | NUMBER(12,2) | Y | 0 |  |
| 41 | VALOR_COMISSAO_NOV | NUMBER(12,2) | Y | 0 |  |
| 42 | VALOR_IMPOSTO_NOV | NUMBER(12,2) | Y | 0 |  |
| 43 | VALOR_ALUGUEL_DEZ | NUMBER(12,2) | Y | 0 |  |
| 44 | VALOR_COMISSAO_DEZ | NUMBER(12,2) | Y | 0 |  |
| 45 | VALOR_IMPOSTO_DEZ | NUMBER(12,2) | Y | 0 |  |
| 46 | TIPO_IMOVEL | VARCHAR2(1) | Y |  |  |
| 47 | ENDERECO_IMOVEL | VARCHAR2(60) | Y |  |  |
| 48 | CEP | VARCHAR2(8) | Y |  |  |
| 49 | CODIGO_MUNICIPIO_IMOVEL | VARCHAR2(4) | Y |  |  |
| 50 | UF | VARCHAR2(2) | Y |  |  |

**PK**: CNPJ_DECLARANTE, ANO_CALENDARIO, SEQUENCIAL_LOCACAO

**FKs**:
- CNPJ_DECLARANTE → DIMOB_DADOS_INICIAIS(CNPJ_DECLARANTE)

---

## DIMOB_GERACAO_MIDIA_LOG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ | NUMBER | N |  |  |
| 2 | ORDEM | NUMBER | N |  |  |
| 3 | DATA_HORA | TIMESTAMP(6) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(2000) | N |  |  |
| 5 | ID_SEVERIDADE | NUMBER | N |  |  |

**PK**: SEQ, ORDEM

---

## DIMOB_IMPORTACAO_LOG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_IMPORTACAO_LOG | NUMBER | N |  |  |
| 2 | DATA_HORA | TIMESTAMP(6) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(2048) | Y |  |  |
| 4 | ID_SEVERUDADE | NUMBER | Y |  |  |
| 5 | ID_IMPORTACAO_MIDIA | NUMBER | N |  |  |

**PK**: ID_IMPORTACAO_MIDIA

---

## DIMOB_IMPORTACAO_MIDIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_IMPORTACAO_MIDIA | NUMBER | N |  |  |
| 2 | DATA_IMPORTACAO | TIMESTAMP(6) | Y |  |  |
| 3 | STATUS | NUMBER | Y |  |  |
| 4 | LOG | VARCHAR2(2048) | Y |  |  |
| 5 | CNPJ_DECLARANTE | NUMBER(15) | Y |  |  |

**PK**: ID_IMPORTACAO_MIDIA

---

## DIMOB_INC_CONST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CNPJ_DECLARANTE | NUMBER(14) | N |  |  |
| 2 | ANO_CALENDARIO | VARCHAR2(4) | N |  |  |
| 3 | SEQUENCIAL | NUMBER | N | 1 |  |
| 4 | CNPJ_CPF_COMPRADOR | VARCHAR2(14) | Y |  |  |
| 5 | NOME_COMPRADOR | VARCHAR2(60) | Y |  |  |
| 6 | NUMERO_CONTRATO | VARCHAR2(6) | Y |  |  |
| 7 | DATA_CONTRATO | DATE | Y |  |  |
| 8 | VALOR_OPERACAO | NUMBER(12,2) | Y | 0 |  |
| 9 | VALOR_PAGO_ANO | NUMBER(12,2) | Y | 0 |  |
| 10 | TIPO_IMOVEL | VARCHAR2(1) | Y |  |  |
| 11 | ENDERECO | VARCHAR2(60) | Y |  |  |
| 12 | CEP | VARCHAR2(8) | Y |  |  |
| 13 | CODIGO_MUNICIPIO_IMOVEL | VARCHAR2(4) | Y |  |  |
| 14 | UF | VARCHAR2(2) | Y |  |  |

**PK**: CNPJ_DECLARANTE, ANO_CALENDARIO, SEQUENCIAL

**FKs**:
- CNPJ_DECLARANTE → DIMOB_DADOS_INICIAIS(CNPJ_DECLARANTE)

---

## DIMOB_INTERMEDIACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CNPJ_DECLARANTE | NUMBER(14) | N |  |  |
| 2 | ANO_CALENDARIO | VARCHAR2(4) | N |  |  |
| 3 | SEQUENCIAL | NUMBER(5) | N | 1 |  |
| 4 | CNPJ_CPF_VENDEDOR | VARCHAR2(14) | N |  |  |
| 5 | NOME_VENDEDOR | VARCHAR2(60) | N |  |  |
| 6 | CNPJ_CPF_COMPRADOR | VARCHAR2(14) | N |  |  |
| 7 | NOME_COMPRADOR | VARCHAR2(60) | N |  |  |
| 8 | NUMERO_CONTRATO | VARCHAR2(20) | N |  |  |
| 9 | DATA_CONTRATO | DATE | N |  |  |
| 10 | TIPO_IMOVEL | VARCHAR2(20) | N |  |  |
| 11 | VALOR_VENDA | NUMBER(12,2) | N | 0 |  |
| 12 | VALOR_COMISSAO | NUMBER(12,2) | N | 0 |  |
| 13 | ENDERECO | VARCHAR2(60) | N |  |  |
| 14 | UF | VARCHAR2(2) | N |  |  |
| 15 | CODIGO_MUNICIPIO_IMOVEL | VARCHAR2(4) | N |  |  |
| 16 | CEP | VARCHAR2(8) | N |  |  |

**PK**: CNPJ_DECLARANTE, ANO_CALENDARIO, SEQUENCIAL

**FKs**:
- CNPJ_DECLARANTE → DIMOB_DADOS_INICIAIS(CNPJ_DECLARANTE)

---

## DIMOB_LICENCA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ | NUMBER | N |  |  |
| 2 | DATA_GRAVACAO | DATE | Y |  |  |
| 3 | LICENCA | BLOB | Y |  |  |

**PK**: SEQ

---

## DIMOB_LOGIN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(10) | N |  |  |
| 2 | SENHA | VARCHAR2(10) | N |  |  |
| 3 | NOME | VARCHAR2(20) | Y |  |  |
| 4 | SOBRENOME | VARCHAR2(20) | Y |  |  |

**PK**: USUARIO

---

## DIMOB_MIDIA_DIGITAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ | NUMBER | N |  |  |
| 2 | CNPJ_DECLARANTE | NUMBER | N |  |  |
| 3 | DATA_HORA | TIMESTAMP(6) | Y |  |  |
| 4 | USUARIO | VARCHAR2(20) | N |  |  |
| 5 | STATUS | NUMBER | N |  |  |
| 6 | FLAG_RETIFICADORA | NUMBER | N |  |  |
| 7 | ANO_CALENDARIO | VARCHAR2(4) | N |  |  |
| 8 | NUMERO_RECIBO | NUMBER(10) | Y |  |  |
| 9 | SITUACAO_ESPECIAL | NUMBER | Y |  |  |
| 10 | ID_MOTIVO | NUMBER | Y |  |  |
| 11 | DATA_SITUACAO_ESPECIAL | DATE | Y |  |  |
| 12 | ARQUIVO | BLOB | Y |  |  |
| 13 | ARQUIVO_REPORT | BLOB | Y |  |  |

**PK**: SEQ

**FKs**:
- USUARIO → DIMOB_LOGIN(USUARIO)

---

## DIMOB_MUNICIPIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CODIGO_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | CODIGO_MUNICIPIO | NUMBER | N |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | N |  |  |

**PK**: CODIGO_ESTADO, CODIGO_MUNICIPIO

**FKs**:
- CODIGO_ESTADO → DIMOB_ESTADO(CODIGO_ESTADO)

---

## DIMOB_PARAMETROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER | N |  |  |
| 2 | ANO | NUMBER | N |  |  |
| 3 | NUMERO_RECIBO | NUMBER | Y |  |  |
| 4 | DATA_EVENTO | DATE | Y |  |  |
| 5 | ID_EVENTO | NUMBER | Y |  |  |
| 6 | RETIFICADORA | CHAR(1) | Y |  |  |
| 7 | SITUACAO_ESPECIAL | CHAR(1) | Y |  |  |

**PK**: ID

**FKs**:
- ID_EVENTO → DIMOB_EVENTO(ID_EVENTO)

---

