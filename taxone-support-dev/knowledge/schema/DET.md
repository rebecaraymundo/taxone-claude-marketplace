# Módulo: DET (DET) - 12 tabelas

## DET_CALC_DACON

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MESANO | NUMBER(6) | N |  |  |
| 4 | NUM_FICHA | VARCHAR2(3) | N |  |  |
| 5 | NUM_LINHA | NUMBER(2) | N |  |  |
| 6 | IND_DIG_CALC | NUMBER | N |  |  |
| 7 | IDENT_REGRA | NUMBER(12) | N |  |  |
| 8 | MERCADO | CHAR(1) | N |  |  |
| 9 | DETALHE | LONG | Y |  |  |
| 10 | VALOR | NUMBER(22,7) | Y |  |  |
| 11 | REGIME | VARCHAR2(1) | N |  |  |
| 12 | COD_PRODUTO_DACON | VARCHAR2(10) | N |  |  |
| 13 | NUM_FICHA_OLD | VARCHAR2(3) | Y |  |  |
| 14 | IDX_COL_VALOR | NUMBER | N | 1 |  |

**PK**: COD_EMPRESA, COD_ESTAB, MESANO, NUM_FICHA, COD_PRODUTO_DACON, NUM_LINHA, IND_DIG_CALC, IDENT_REGRA, MERCADO, REGIME, IDX_COL_VALOR

---

## DET_GRUPO_DIC_DADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO | VARCHAR2(5) | N |  |  |
| 2 | COD_CATEGORIA | VARCHAR2(30) | N |  |  |
| 3 | ID_CAMPO | NUMBER(3) | N |  |  |
| 4 | NOME_CAMPO | VARCHAR2(256) | Y |  |  |
| 5 | TAMANHO | NUMBER(5) | Y |  |  |
| 6 | DSC_CAMPO | VARCHAR2(4000) | Y |  |  |
| 7 | ORIGEM | VARCHAR2(100) | Y |  |  |
| 8 | LOCALIZACAO | VARCHAR2(500) | Y |  |  |

**PK**: COD_GRUPO, COD_CATEGORIA, ID_CAMPO

**FKs**:
- COD_GRUPO, COD_CATEGORIA → CAT_GRUPO_DIC_DADOS(COD_GRUPO, COD_CATEGORIA)

---

## DET_GRUPO_DIC_REGRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO | VARCHAR2(5) | N |  |  |
| 2 | COD_CATEGORIA | VARCHAR2(30) | N |  |  |
| 3 | ID_CAMPO | NUMBER(3) | N |  |  |
| 4 | COD_REGRA | NUMBER(5) | N |  |  |
| 5 | CONDICAO | VARCHAR2(500) | Y |  | Informa em que condições a regra será aplicada. Por exemplo, para uma regra de preenchimento obrigatório do campo, esta regra só será aplicada caso a condição seja atendida |

**PK**: COD_GRUPO, COD_CATEGORIA, ID_CAMPO, COD_REGRA

**FKs**:
- COD_GRUPO, COD_CATEGORIA, ID_CAMPO → DET_GRUPO_DIC_DADOS(COD_GRUPO, COD_CATEGORIA, ID_CAMPO)
- COD_REGRA → REGRA_VALID_DADOS(COD_REGRA)

---

## DET_JOB_BCK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | NUM_DET_JOB | NUMBER(3) | N |  |  |
| 3 | STATUS_DET_JOB | CHAR(1) | Y |  |  |
| 4 | NOME_TABELA_BANCO | VARCHAR2(30) | Y |  |  |
| 5 | DATA_EXEC_INI | DATE | Y |  |  |
| 6 | DATA_EXEC_FIM | DATE | Y |  |  |
| 7 | QTD_REGS_PROC | NUMBER(9) | Y |  |  |
| 8 | NUM_PROC_IMP | NUMBER(12) | Y |  |  |

**PK**: NUM_JOB, NUM_DET_JOB

**FKs**:
- NUM_JOB → JOB_BCK(NUM_JOB)

---

## DET_JOB_DROP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 3 | NUMERO_ARQUIVO | NUMBER(3) | N |  |  |
| 4 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 5 | STATUS | CHAR(1) | Y |  |  |
| 6 | QTD_REGISTROS | NUMBER(12) | Y |  |  |
| 7 | DAT_INI_EXEC | DATE | Y |  |  |
| 8 | DAT_FIM_EXEC | DATE | Y |  |  |
| 9 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 10 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 11 | IND_INICIALIZA | CHAR(1) | Y | 'N' |  |

**PK**: NUM_JOB, GRUPO_ARQUIVO, NUMERO_ARQUIVO

**FKs**:
- NUM_JOB → JOB_IMPORTACAO(NUM_JOB)

---

## DET_JOB_IMPORT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 3 | NUMERO_ARQUIVO | NUMBER(3) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 6 | DATA_INI | DATE | Y |  |  |
| 7 | DATA_FIM | DATE | Y |  |  |
| 8 | PERC_ERRO | NUMBER(3) | Y |  |  |
| 9 | IND_ABORTA_JOB | CHAR(1) | Y |  |  |
| 10 | STATUS | CHAR(1) | Y |  |  |
| 11 | IND_DROP_TAB | CHAR(1) | Y |  |  |
| 12 | DAT_INI_EXEC | DATE | Y |  |  |
| 13 | DAT_FIM_EXEC | DATE | Y |  |  |
| 14 | IND_PERIODO | CHAR(1) | Y |  |  |
| 15 | IND_SOBREPOR_REG | CHAR(1) | Y |  |  |
| 16 | IND_LOG_X2013 | CHAR(1) | Y |  |  |
| 17 | IND_VALID_X2013 | CHAR(1) | Y |  |  |
| 18 | IND_DATA_AVERB_X48 | CHAR(1) | Y |  |  |
| 19 | IND_GERA_X530 | CHAR(1) | Y |  |  |
| 20 | IND_GERA_X751 | CHAR(1) | Y |  |  |
| 21 | IND_VALID_CEP_X04 | CHAR(1) | Y |  |  |
| 22 | GRUPO_X188 | VARCHAR2(9) | Y |  |  |
| 23 | GRUPO_X189 | VARCHAR2(9) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_EXP_REG_ERRO | VARCHAR2(1) | Y |  |  |
| 26 | QTDE_REGS_DUPL | NUMBER(12) | Y |  |  |
| 27 | QTDE_REGS_SAFX | NUMBER(12) | Y |  |  |

**PK**: NUM_JOB, GRUPO_ARQUIVO, NUMERO_ARQUIVO

**FKs**:
- NUM_JOB → JOB_IMPORTACAO(NUM_JOB)

---

## DET_JOB_LOAD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 3 | NUMERO_ARQUIVO | NUMBER(3) | N |  |  |
| 4 | SEQUENCIA | NUMBER(4) | N |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | NOM_ARQUIVO | VARCHAR2(80) | Y |  |  |
| 8 | STATUS | CHAR(1) | Y |  |  |
| 9 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | QTD_REGISTROS | NUMBER(12) | Y |  |  |
| 11 | DAT_INI_EXEC | DATE | Y |  |  |
| 12 | DAT_FIM_EXEC | DATE | Y |  |  |

**PK**: NUM_JOB, GRUPO_ARQUIVO, NUMERO_ARQUIVO, SEQUENCIA

**FKs**:
- NUM_JOB → JOB_IMPORTACAO(NUM_JOB)

---

## DET_JOB_RESTORE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | NUM_DET_JOB | NUMBER(3) | N |  |  |
| 3 | STATUS_DET_JOB | CHAR(1) | Y |  |  |
| 4 | NOME_TABELA_BANCO | VARCHAR2(30) | Y |  |  |
| 5 | NUM_JOB_BCK | NUMBER(12) | Y |  |  |
| 6 | NUM_DET_JOB_BCK | NUMBER(3) | Y |  |  |
| 7 | DATA_REF_INI | DATE | Y |  |  |
| 8 | DATA_REF_FIM | DATE | Y |  |  |
| 9 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 10 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 11 | NOM_ARQ | VARCHAR2(60) | Y |  |  |
| 12 | QTD_REGS_ARQ | NUMBER(9) | Y |  |  |
| 13 | DATA_EXEC_INI | DATE | Y |  |  |
| 14 | DATA_EXEC_FIM | DATE | Y |  |  |
| 15 | QTD_REGS_PROC | NUMBER(9) | Y |  |  |
| 16 | NUM_VERSAO_DB | NUMBER(4) | Y |  |  |
| 17 | IND_OVERWRITE | CHAR(1) | Y |  |  |

**PK**: NUM_JOB, NUM_DET_JOB

**FKs**:
- NOME_TABELA_BANCO → CAT_PRIOR_BR(NOME_TABELA_BANCO)

---

## DET_PROC_GERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | NOME_LOGICO_ARQ | VARCHAR2(8) | N |  |  |
| 3 | IND_LAYOUT | CHAR(1) | Y |  |  |
| 4 | NOME_ARQ | VARCHAR2(50) | Y |  |  |
| 5 | STA_EMISSAO_DUMP | CHAR(1) | Y |  |  |
| 6 | STA_EMISSAO_ETIQ | CHAR(1) | Y |  |  |
| 7 | STA_EMISSAO_RELAT | CHAR(1) | Y |  |  |
| 8 | STA_EMISSAO_LAYOUT | CHAR(1) | Y |  |  |
| 9 | NUM_PAG_PRIM | NUMBER(2) | Y |  |  |
| 10 | NUM_PAG_FIM | NUMBER(2) | Y |  |  |
| 11 | TOTAL_CAMPO_TOT | NUMBER(18) | Y |  |  |
| 12 | NUM_VOLUMES | NUMBER(5) | Y |  |  |
| 13 | TOTAL_REG | NUMBER(12) | Y |  |  |
| 14 | CLAUSULA_SELECT | LONG | Y |  |  |
| 15 | NUM_PAG_LAY | NUMBER(2) | Y |  |  |

**PK**: NUM_PROCESSO, NOME_LOGICO_ARQ

---

## DET_PROC_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | NOM_ARQ | VARCHAR2(200) | Y |  |  |
| 4 | TOT_LIDOS | NUMBER(12) | Y |  |  |
| 5 | TOT_INS | NUMBER(12) | Y |  |  |
| 6 | TOT_ERR | NUMBER(12) | Y |  |  |
| 7 | TOT_ALT | NUMBER(12) | Y |  |  |
| 8 | TOT_IGNORADOS | NUMBER(12) | Y |  |  |
| 9 | DAT_ULT_ALT | DATE | Y |  |  |

**Indexes**:
- DET_PROC_IMP_X (UNIQUE): (NUM_PROCESSO)

---

## DET_PROC_IMP_C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_ARQUIVO | NUMBER(2) | Y |  |  |
| 5 | NOM_TAB_WORK | VARCHAR2(8) | Y |  |  |
| 6 | DAT_ULT_ATU | DATE | Y |  |  |
| 7 | DAT_INI | DATE | Y |  |  |
| 8 | DAT_FIM | DATE | Y |  |  |
| 9 | TOT_LIDOS | NUMBER(12) | Y |  |  |
| 10 | TOT_ERR | NUMBER(12) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB

---

## DET_REG_LAYOUT
**Comment**: Codigo da lista de valores oriunda da tabela CAD_LISTA_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_BLOCO | VARCHAR2(2) | N |  |  |
| 3 | COD_REGISTRO | VARCHAR2(7) | N |  |  |
| 4 | POSICAO | NUMBER(3) | N |  |  |
| 5 | NOME_CAMPO | VARCHAR2(30) | Y |  |  |
| 6 | POS_CHAVE | NUMBER(2) | Y |  |  |
| 7 | DSC_CAMPO | VARCHAR2(1000) | Y |  |  |
| 8 | TIPO | VARCHAR2(2) | Y |  |  |
| 9 | TAMANHO | NUMBER(5) | Y |  |  |
| 10 | DECIMAIS | NUMBER(1) | Y |  |  |
| 11 | TEXTO_FIXO | VARCHAR2(50) | Y |  |  |
| 12 | ID_CAMPO | NUMBER(3) | Y |  |  |
| 13 | POS_CHAVE_LOG | NUMBER(2) | Y |  | Customização da arquitetura original para atendimento ao Sped Fiscal. Mensagem de Log de Erro utiliza este campo ao invés do campo POS_CHAVE, para compor chave de identificação do registro no log de erro. |
| 14 | NOME_CAMPO_LOG | VARCHAR2(200) | Y |  | Customização da arquitetura original para atendimento ao Sped Fiscal. Mensagem de Log de Erro utiliza este campo ao invés do campo NOME_CAMPO, para determinar o nome do campo na chave de identificação do registro do log de erro. |
| 15 | TAM_LOG | NUMBER(5) | Y |  |  |
| 16 | DATA_INI_VIGENCIA | DATE | Y |  |  |
| 17 | DATA_FIM_VIGENCIA | DATE | Y |  |  |
| 18 | COD_LISTA_MSAF | VARCHAR2(100) | Y |  |  |

**PK**: COD_LAYOUT, COD_BLOCO, COD_REGISTRO, POSICAO

**FKs**:
- COD_LAYOUT, COD_BLOCO, COD_REGISTRO → CAD_REG_LAYOUT(COD_LAYOUT, COD_BLOCO, COD_REGISTRO)

---

