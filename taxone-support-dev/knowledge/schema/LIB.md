# Módulo: LIB (LIB) - 31 tabelas

## LIB_CONTROLE_ACESSO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SESSION_ID | NUMBER | N |  |  |
| 2 | PARAMS | VARCHAR2(4000) | Y |  |  |

**PK**: SESSION_ID

---

## LIB_LIC_MODULOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(40) | N |  |  |
| 3 | CHAVE_ORDENACAO | VARCHAR2(15) | Y |  | Coluna utilizada para garantir a recuperação dos modulos na ordem do arquivo |

**PK**: COD_EMPRESA, COD_MODULO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## LIB_LIC_MODULO_COMPONENTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(40) | N |  |  |
| 2 | APLICACAO | VARCHAR2(100) | N |  |  |

**PK**: COD_MODULO, APLICACAO

---

## LIB_LIC_MODULO_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_MODULO | VARCHAR2(40) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | CHAVE_LIBERACAO | VARCHAR2(500) | Y |  |  |
| 5 | IND_TRATAMENTO | VARCHAR2(3) | N |  | Tratamento para os estabelecimentos gravados. "MUN" para os estabelecmentos do municipio da GISS, "OUT" para estabelecimentos fora do municipio da GISS |
| 6 | ORDENACAO | VARCHAR2(15) | Y |  |  |

**PK**: COD_EMPRESA, COD_MODULO, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_MODULO → LIB_LIC_MODULOS(COD_EMPRESA, COD_MODULO)

---

## LIB_PROCESSO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | SP_NOME | VARCHAR2(30) | Y |  |  |
| 3 | VERSAO | VARCHAR2(30) | Y |  |  |
| 4 | DATA_INICIO | DATE | Y |  |  |
| 5 | DATA_FIM | DATE | Y |  |  |
| 6 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 7 | SITUACAO | VARCHAR2(30) | Y |  |  |
| 8 | TIPO | VARCHAR2(30) | Y |  |  |
| 9 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 10 | DESCRICAO | VARCHAR2(4000) | Y |  |  |
| 11 | IND_PROG | CHAR(1) | Y |  |  |
| 12 | PROC_ID_ORIG | NUMBER | Y |  |  |
| 13 | NUM_JOB | NUMBER | Y |  |  |
| 14 | APLICACAO | VARCHAR2(100) | Y |  |  |
| 15 | ID_CPROC | NUMBER(12) | Y |  |  |
| 16 | DATA_FILA_INIC | DATE | Y |  |  |
| 17 | DATA_FILA_FIM | DATE | Y |  |  |
| 18 | PROC_ID_TEMP | NUMBER | Y |  |  |

**PK**: PROC_ID

**Indexes**:
- IX_LIB_PROCESSO_01: (SP_NOME, DATA_INICIO, COD_EMPRESA, COD_USUARIO, SITUACAO)

---

## LIB_PROCESSO_LOG
**Comment**: Tabela de histÃ³rico da tabela LIB_PROCESSO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | CLIENTE | VARCHAR2(50) | N |  |  |
| 3 | SP_NOME | VARCHAR2(30) | Y |  |  |
| 4 | VERSAO | VARCHAR2(30) | Y |  |  |
| 5 | DATA_INICIO | DATE | Y |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 8 | SITUACAO | VARCHAR2(30) | Y |  |  |
| 9 | TIPO | VARCHAR2(30) | Y |  |  |
| 10 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 11 | DESCRICAO | VARCHAR2(300) | Y |  |  |
| 12 | IND_PROG | CHAR(1) | Y |  |  |
| 13 | PROC_ID_ORIG | NUMBER | Y |  |  |
| 14 | NUM_JOB | NUMBER | Y |  |  |
| 15 | APLICACAO | VARCHAR2(100) | Y |  |  |
| 16 | QTD_REGISTROS_PROC | NUMBER | Y |  |  |
| 17 | QTD_LINHAS_LOG | NUMBER | Y |  |  |
| 18 | ORIGEM | VARCHAR2(30) | Y |  |  |
| 19 | TABELA_ORIGEM | VARCHAR2(12) | N | 'LIB_PROCESSO' |  |
| 20 | DATA_FILA_INIC | DATE | Y |  |  |
| 21 | DATA_FILA_FIM | DATE | Y |  |  |
| 22 | CNPJ_CONTRATANTE | VARCHAR2(20) | Y |  |  |
| 23 | CNPJ | VARCHAR2(20) | Y |  |  |

**PK**: PROC_ID, CLIENTE, TABELA_ORIGEM

---

## LIB_PROC_CAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCCAB_ID | NUMBER | N |  |  |
| 2 | PROC_ID | NUMBER | Y |  |  |
| 3 | TIPO | VARCHAR2(30) | Y |  |  |
| 4 | LINHA | NUMBER | Y |  |  |
| 5 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 6 | TIPO_REL | NUMBER | Y | 1 |  |

**PK**: PROCCAB_ID

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

**Indexes**:
- IX_LIB_PROC_CAB_01: (PROC_ID)

---

## LIB_PROC_CONCILIACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER | N |  |  |
| 2 | ID_PROCESS_TENANT | NUMBER | N |  |  |
| 3 | NOME_AUDITORIA | VARCHAR2(255) | N |  |  |
| 4 | RESULTADO | NUMBER(1) | N |  |  |

**PK**: ID

---

## LIB_PROC_FTP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CODIGO_AREA_FTP | VARCHAR2(30) | Y |  |  |
| 2 | SERVIDOR_FTP | VARCHAR2(100) | Y |  |  |
| 3 | USUARIO_FTP | VARCHAR2(20) | Y |  |  |
| 4 | SENHA_FTP | VARCHAR2(20) | Y |  |  |

---

## LIB_PROC_LOG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCLOG_ID | NUMBER | N |  |  |
| 2 | PROC_ID | NUMBER | Y |  |  |
| 3 | DATA | DATE | Y |  |  |
| 4 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 5 | NIVEL | NUMBER(15) | Y |  |  |

**PK**: PROCLOG_ID

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

**Indexes**:
- IX_LIB_PROC_LOG_01: (PROC_ID)

---

## LIB_PROC_MAPA_RES_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | PERIODO_INI | DATE | Y |  |  |
| 6 | PERIODO_FIM | DATE | Y |  |  |
| 7 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 8 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 9 | DATA | DATE | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 12 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 16 | NUM_CRZ | VARCHAR2(6) | Y |  |  |
| 17 | VLR_TOTAL_ECF | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS_ECF | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_ECF | NUMBER(17,2) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID, GRUPO_MODELO, COD_MODELO, DATA

---

## LIB_PROC_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCPARAM_ID | NUMBER | N |  |  |
| 2 | PROC_ID | NUMBER | Y |  |  |
| 3 | NOME | VARCHAR2(255) | Y |  |  |
| 4 | VALOR | VARCHAR2(4000) | Y |  |  |
| 5 | TIPO | VARCHAR2(30) | Y |  |  |
| 6 | APRESENTA | CHAR(1) | Y | 'S' |  |
| 7 | VALOR_APRESENTA | VARCHAR2(255) | Y |  |  |
| 8 | ID_PARAM | NUMBER(12) | Y |  |  |

**PK**: PROCPARAM_ID

**Indexes**:
- IX_LIB_PROC_PARAM_01: (PROC_ID)

---

## LIB_PROC_PARAM_LOG
**Comment**: Tabela de histÃ³rico da tabela LIB_PROC_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCPARAM_ID | NUMBER | N |  |  |
| 2 | PROC_ID | NUMBER | N |  |  |
| 3 | CLIENTE | VARCHAR2(50) | N |  |  |
| 4 | NOME | VARCHAR2(255) | Y |  |  |
| 5 | VALOR | VARCHAR2(4000) | Y |  |  |
| 6 | TIPO | VARCHAR2(30) | Y |  |  |
| 7 | APRESENTA | CHAR(1) | Y |  |  |
| 8 | VALOR_APRESENTA | VARCHAR2(255) | Y |  |  |

---

## LIB_PROC_PROGRAMACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCPRG_ID | CHAR(18) | N |  |  |
| 2 | PROC_ID | NUMBER | Y |  |  |
| 3 | DATA_PREVISTA | DATE | Y |  |  |
| 4 | INTERVALO | VARCHAR2(2000) | Y |  |  |

**PK**: PROCPRG_ID

**Indexes**:
- IX_LIB_PROC_PROGRAMACAO_01: (PROC_ID)

---

## LIB_PROC_QUERY_REL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | QUERY | CLOB | Y |  |  |
| 4 | DSC_REL | VARCHAR2(4000) | Y |  |  |

**PK**: PROC_ID, PROCREL_ID

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## LIB_PROC_REL_CONV132

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | DATA_INI | DATE | Y |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 9 | CEP | NUMBER(8) | Y |  |  |
| 10 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 11 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 12 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 13 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 14 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 15 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 16 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 17 | CIDADE | VARCHAR2(30) | Y |  |  |
| 18 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 19 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 20 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 21 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 22 | DATA_EMISSAO | DATE | Y |  |  |
| 23 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 24 | NUM_MARCA_MODELO | NUMBER(6) | Y |  |  |
| 25 | DSC_COR | VARCHAR2(40) | Y |  |  |
| 26 | NUM_CHASSI | VARCHAR2(17) | Y |  |  |
| 27 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 28 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 29 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 31 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 33 | VLR_TRIBUTO_ICMSS_C | NUMBER(17,2) | Y |  |  |
| 34 | VLR_TRIBUTO_ICMSS_D | NUMBER(17,2) | Y |  |  |
| 35 | IND_ORIGEM | CHAR(1) | Y |  |  |
| 36 | IND_GNRE | CHAR(1) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID

---

## LIB_PROC_REL_IND_SUFR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | DATA_INI | DATE | Y |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | IND_PROD_NCM | CHAR(1) | Y |  |  |
| 8 | CODIGO | VARCHAR2(60) | Y |  |  |
| 9 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 10 | COD_GRUPO_PROD | VARCHAR2(5) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | QTD_LOCAL | NUMBER(17,6) | Y |  |  |
| 13 | QTD_NACIONAL | NUMBER(17,6) | Y |  |  |
| 14 | QTD_EXTERIOR | NUMBER(17,6) | Y |  |  |
| 15 | QTD_TOTAL | NUMBER(17,6) | Y |  |  |
| 16 | VLR_LOCAL | NUMBER(17,2) | Y |  |  |
| 17 | VLR_NACIONAL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_EXTERIOR | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID

---

## LIB_PROC_REL_PORT63_RPF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | DATA_INI | DATE | Y |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | CPF | VARCHAR2(11) | Y |  |  |
| 8 | NOME | VARCHAR2(70) | Y |  |  |
| 9 | DATA_NASC | DATE | Y |  |  |
| 10 | PIS_PASEP | VARCHAR2(11) | Y |  |  |
| 11 | DATA_ADMISSAO | DATE | Y |  |  |
| 12 | DATA_DEMISSAO | DATE | Y |  |  |
| 13 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 14 | DSC_SETOR | VARCHAR2(50) | Y |  |  |
| 15 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 16 | DSC_VERBA | VARCHAR2(50) | Y |  |  |
| 17 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 18 | DSC_CUSTO | VARCHAR2(50) | Y |  |  |
| 19 | IND_FOLHA | VARCHAR2(100) | Y |  |  |
| 20 | NUM_MATRICULA | VARCHAR2(8) | Y |  |  |
| 21 | DATA_PAGTO | DATE | Y |  |  |
| 22 | COD_CBO | VARCHAR2(10) | Y |  |  |
| 23 | DSC_FUNCAO | VARCHAR2(50) | Y |  |  |
| 24 | VLR_VERBA | NUMBER(17,2) | Y |  |  |
| 25 | IND_VERBA | VARCHAR2(100) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

**Indexes**:
- IX_LIB_PROC_REL_01: (PROC_ID)

---

## LIB_PROC_REL_PORT63_RPFA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | DATA_INI | DATE | Y |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | CPF | VARCHAR2(14) | Y |  |  |
| 8 | NOME | VARCHAR2(70) | Y |  |  |
| 9 | DATA_NASC | DATE | Y |  |  |
| 10 | PIS_PASEP | VARCHAR2(11) | Y |  |  |
| 11 | DATA_ADMISSAO | DATE | Y |  |  |
| 12 | DATA_DEMISSAO | DATE | Y |  |  |
| 13 | NUM_REGISTRO | VARCHAR2(14) | Y |  |  |
| 14 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 15 | DSC_SETOR | VARCHAR2(50) | Y |  |  |
| 16 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 17 | DSC_VERBA | VARCHAR2(50) | Y |  |  |
| 18 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 19 | DSC_CUSTO | VARCHAR2(50) | Y |  |  |
| 20 | IND_FOLHA | VARCHAR2(24) | Y |  |  |
| 21 | NUM_MATRICULA | VARCHAR2(8) | Y |  |  |
| 22 | DATA_PAGTO | DATE | Y |  |  |
| 23 | DAT_COMPETENCIA | DATE | Y |  |  |
| 24 | COD_CBO | VARCHAR2(10) | Y |  |  |
| 25 | COD_FUNCAO | VARCHAR2(10) | Y |  |  |
| 26 | DSC_FUNCAO | VARCHAR2(50) | Y |  |  |
| 27 | TIPO_TRABALHADOR | VARCHAR2(12) | Y |  |  |
| 28 | VLR_VERBA | NUMBER(17,2) | Y |  |  |
| 29 | IND_VERBA | VARCHAR2(23) | Y |  |  |
| 30 | TIPO_VERBA | CHAR(1) | Y |  |  |
| 31 | INCID_DIRF | CHAR(1) | Y |  |  |
| 32 | INCID_INSS | CHAR(1) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID

**Indexes**:
- IX_LIB_PROC_REL_RPFA_01: (PROC_ID)

---

## LIB_PROC_REL_RES_APROP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | PERIODO_REF_INI | DATE | Y |  |  |
| 6 | PERIODO_REF_FIM | DATE | Y |  |  |
| 7 | TIPO_MODELO_102 | CHAR(1) | Y |  |  |
| 8 | IND_PERIODIC_102 | CHAR(1) | Y |  |  |
| 9 | DAT_APURACAO | DATE | Y |  |  |
| 10 | VLR_TOT_OP_TRIBUT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_OP_SAIDAS | NUMBER(17,2) | Y |  |  |
| 12 | COEFICIENTE | NUMBER(16,7) | Y |  |  |
| 13 | VLR_TOT_APROPRIAR | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOT_CREDITO | NUMBER(17,2) | Y |  |  |
| 15 | NUM_FRACAO | NUMBER(3) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID

---

## LIB_PROC_REL_RES_BEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | PERIODO_REF | DATE | Y |  |  |
| 6 | TIPO_MODELO_102 | VARCHAR2(1) | Y |  |  |
| 7 | CODIGO | VARCHAR2(25) | Y |  |  |
| 8 | DATA_ENTRADA | DATE | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | DESCRICAO | VARCHAR2(105) | Y |  |  |
| 13 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ENTRADA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SAIDA | NUMBER(17,2) | Y |  |  |
| 16 | VLR_SALDO_ACUM | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | DATA_SAIDA | DATE | Y |  |  |
| 19 | NUM_PARCELA | NUMBER(3) | Y |  |  |
| 20 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 21 | VLR_TOT_BASE | NUMBER(17,2) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID

---

## LIB_PROC_REL_SALDO_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | DATA_SALDO | DATE | Y |  |  |
| 6 | DATA_INI | DATE | Y |  |  |
| 7 | DATA_FIM | DATE | Y |  |  |
| 8 | DATA_ULT_CALC | DATE | Y |  |  |
| 9 | DESC_CIAP | VARCHAR2(200) | Y |  |  |
| 10 | DATA_OPER | DATE | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CRED_APROP | NUMBER(17,2) | Y |  |  |
| 16 | NUM_ALT_PARC | VARCHAR2(7) | Y |  |  |
| 17 | VLR_ICMS_BX | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CRED_DEDUZ | NUMBER(17,2) | Y |  |  |
| 19 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 20 | NUM_PARC_CRED | NUMBER(3) | Y |  |  |
| 21 | VLR_CURTO_PRAZO | NUMBER(17,2) | Y |  |  |
| 22 | VLR_LONGO_PRAZO | NUMBER(17,2) | Y |  |  |
| 23 | VLR_CRED_PASS | NUMBER(17,2) | Y |  |  |
| 24 | IND_LEGENDA | VARCHAR2(2) | Y |  |  |
| 25 | VLR_RESIDUAL | NUMBER(17,2) | Y |  |  |
| 26 | VLR_CRED_MENSAL | NUMBER(17,2) | Y |  |  |
| 27 | VLR_PASS_APROP | NUMBER(17,2) | Y |  |  |
| 28 | NUM_CIAP | NUMBER(12) | Y |  |  |
| 29 | VLR_RESIDUAL_PERIODO | NUMBER(17,2) | Y |  |  |
| 30 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 31 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 32 | COD_INC | VARCHAR2(60) | Y |  |  |
| 33 | RAZAO_SOCIAL_ESTAB | VARCHAR2(100) | Y |  |  |
| 34 | CGC_ESTAB | VARCHAR2(14) | Y |  |  |
| 35 | PERIODO_COM_MOVIMENTO | VARCHAR2(50) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID

**Indexes**:
- IX_LIB_PROC_REL_SALDO_CRED: (PROC_ID, COD_EMPRESA, COD_ESTAB)

---

## LIB_PROC_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCSAIDA_ID | NUMBER | N |  |  |
| 2 | PROC_ID | NUMBER | Y |  |  |
| 3 | PAG | NUMBER(15) | Y |  |  |
| 4 | LINHA | NUMBER(15) | Y |  |  |
| 5 | TEXTO | VARCHAR2(4000) | Y |  |  |
| 6 | TIPO | NUMBER | Y |  |  |
| 7 | CHAVE_ORDENACAO | VARCHAR2(500) | Y |  |  |
| 8 | DSC_PARTICAO | VARCHAR2(50) | Y |  |  |

**PK**: PROCSAIDA_ID

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

**Indexes**:
- IX_LIB_PROC_SAIDA_01: (PROC_ID, TIPO, PAG, LINHA, CHAVE_ORDENACAO)

---

## LIB_PROC_SAIDA_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCSAIDA_ID | NUMBER | N |  |  |
| 2 | SEQUENCIAL | NUMBER | N |  |  |
| 3 | TEXTO | VARCHAR2(4000) | Y |  |  |

**PK**: PROCSAIDA_ID, SEQUENCIAL

**FKs**:
- PROCSAIDA_ID → LIB_PROC_SAIDA(PROCSAIDA_ID)

---

## LIB_PROC_SALDO_CRED_CLA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_SALDO | DATE | Y |  |  |
| 5 | DATA_INI | DATE | Y |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | DATA_ULT_CALC | DATE | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_APROP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_BX | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CRED_PASS | NUMBER(17,2) | Y |  |  |

**PK**: PROC_ID

---

## LIB_PROC_SALDO_CRED_CLA_DET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCREL_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | NUM_CIAP | VARCHAR2(20) | Y |  |  |
| 4 | DESC_CIAP | VARCHAR2(105) | Y |  |  |
| 5 | DATA_OPER | DATE | Y |  |  |
| 6 | DATA_FISCAL | DATE | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_APROP | NUMBER(17,2) | Y |  |  |
| 11 | NUM_ULT_PARC | VARCHAR2(7) | Y |  |  |
| 12 | VLR_ICMS_BX | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CRED_PASS | NUMBER(17,2) | Y |  |  |

**PK**: PROCREL_ID, PROC_ID

---

## LIB_PROC_TIPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | TIPO | NUMBER | N |  |  |
| 3 | TITULO | VARCHAR2(100) | Y |  |  |
| 4 | TIPO_ARQ | NUMBER | Y |  |  |
| 5 | MAXROWS | NUMBER | Y |  |  |
| 6 | MAXCOLS | NUMBER | Y |  |  |
| 7 | FONT_HEIGHT | NUMBER | Y |  |  |
| 8 | FILE_NAME | VARCHAR2(50) | Y |  |  |

**PK**: PROC_ID, TIPO

---

## LIB_PROC_XML

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ_ID | NUMBER(12) | N |  |  |
| 2 | XML | XMLTYPE | Y |  |  |
| 3 | XML_B | BLOB | Y |  |  |
| 4 | NOME_ARQ | VARCHAR2(4000) | Y |  |  |

**PK**: SEQ_ID

---

## LIB_PROG_AUTOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROGAUT_ID | NUMBER | N |  |  |
| 2 | IND_ATIVO | CHAR(1) | Y |  |  |
| 3 | DIAS_MES | VARCHAR2(100) | Y |  |  |
| 4 | DIAS_SEMANA | VARCHAR2(15) | Y |  |  |
| 5 | OBJETO | VARCHAR2(30) | Y |  |  |
| 6 | DESC_OBJETO | VARCHAR2(100) | Y |  |  |
| 7 | DESC_PROG | VARCHAR2(100) | Y |  |  |
| 8 | PERIODICIDADE | CHAR(1) | Y |  | Periodicidade de execucao da programacao: D-diaria, S-semanal, Q-quinzenal, M-mensal |
| 9 | OPCAO_DIA | CHAR(1) | Y |  | 1-Todos os dias  2-Durante a semana |
| 10 | PARAMETROS | VARCHAR2(200) | Y |  | String que contem a relacao dos parametros especificos da obrigacao para a geração batch |
| 11 | GERA_EMPRESA | CHAR(1) | Y |  | Indica se a geracao será por Empresa ou por Estabelecimento |

**PK**: PROGAUT_ID

**Indexes**:
- IX_PROG_AUTOM (UNIQUE): (OBJETO, DESC_PROG)

---

## LIB_PROG_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROGESTAB_ID | NUMBER | N |  |  |
| 2 | PROGAUT_ID | NUMBER | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |

**PK**: PROGESTAB_ID

**Indexes**:
- IX_PROG_ESTAB (UNIQUE): (PROGAUT_ID, COD_EMPRESA, COD_ESTAB)

---

## LIB_PROG_HISTOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROGHISTOR_ID | NUMBER | N |  |  |
| 2 | DT_EXECUCAO | DATE | Y |  |  |
| 3 | OBJETO | VARCHAR2(30) | Y |  |  |
| 4 | DESC_OBJETO | VARCHAR2(100) | Y |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | JOB_ORACLE | NUMBER | Y |  |  |
| 8 | PROCID | NUMBER | Y |  | Numero do processo na LIB_PROCESSO (Framework) |
| 9 | IND_CONCLUIDO | CHAR(1) | Y |  |  |
| 10 | PROGAUT_ID | NUMBER | Y | 0 | Identificador da programacao executada |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  | Numero do processo na LOG_PROCESSO |

**PK**: PROGHISTOR_ID

**Indexes**:
- IX_PROG_HISTOR: (DT_EXECUCAO, OBJETO, COD_EMPRESA, COD_ESTAB, PROGAUT_ID)

---

