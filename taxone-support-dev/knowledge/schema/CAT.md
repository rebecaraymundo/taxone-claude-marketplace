# Módulo: CAT (CAT) - 19 tabelas

## CAT_ARQUIVOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOME_LOGICO_ARQ | VARCHAR2(8) | N |  |  |
| 2 | IND_LAYOUT | CHAR(1) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | NOME_CAMPO_TOT | VARCHAR2(40) | Y |  |  |
| 5 | NUM_PAG_LAY | NUMBER(2) | Y |  |  |
| 6 | IND_TIPO_IN | VARCHAR2(2) | Y |  |  |
| 7 | IND_VERSAO_LAYOUT | VARCHAR2(10) | N | ' ' |  |

**PK**: NOME_LOGICO_ARQ, IND_LAYOUT, IND_VERSAO_LAYOUT

---

## CAT_COLUNAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_TIPO_IN | VARCHAR2(2) | N |  |  |
| 2 | NOME_LOGICO_ARQ | VARCHAR2(8) | N |  |  |
| 3 | IND_LAYOUT | CHAR(1) | N |  |  |
| 4 | NUM_COLUNA | NUMBER(2) | N |  |  |
| 5 | DESCRICAO | VARCHAR2(70) | Y |  |  |
| 6 | POSICAO_INI | NUMBER(3) | Y |  |  |
| 7 | POSICAO_FIM | NUMBER(3) | Y |  |  |
| 8 | TIPO | CHAR(1) | Y |  |  |
| 9 | OBSERVACAO | VARCHAR2(255) | Y |  |  |
| 10 | IND_EXIG_NORMATIVA | CHAR(1) | Y |  |  |
| 11 | NUM_CAMPO | NUMBER(4) | Y |  |  |
| 12 | TABELA_ORIGEM | VARCHAR2(25) | Y |  |  |
| 13 | COLUNA_ORIGEM | VARCHAR2(25) | Y |  |  |
| 14 | IND_VERSAO_LAYOUT | VARCHAR2(10) | N | ' ' |  |

**PK**: IND_TIPO_IN, NOME_LOGICO_ARQ, IND_LAYOUT, NUM_COLUNA, IND_VERSAO_LAYOUT

---

## CAT_EMP_BR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | NOME_TABELA_BANCO | VARCHAR2(30) | N |  |  |
| 3 | PERIOD_BACKUP | NUMBER(2) | Y |  |  |
| 4 | IND_LIMPEZA | CHAR(1) | Y |  |  |
| 5 | OBSERVACAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, NOME_TABELA_BANCO

**FKs**:
- NOME_TABELA_BANCO → CAT_PRIOR_BR(NOME_TABELA_BANCO)

---

## CAT_ERRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ERRO | NUMBER(6) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 3 | MOTIVO | VARCHAR2(210) | Y |  |  |
| 4 | IND_ERRO_GRAVE | CHAR(1) | Y |  |  |
| 5 | IND_IMPRIME | CHAR(1) | Y |  |  |
| 6 | LOCALIZACAO | VARCHAR2(18) | Y |  |  |
| 7 | SOLICITA_IN68 | CHAR(1) | Y |  |  |
| 8 | SOLICITA_ICMS | CHAR(1) | Y |  |  |
| 9 | SOLICITA_MOD_UF | CHAR(1) | Y |  |  |
| 10 | SOLICITA_MOD_FED | CHAR(1) | Y |  |  |
| 11 | SOLICITA_MOD_MUN | CHAR(1) | Y |  |  |
| 12 | SOLICITA_CTR_IMP | CHAR(1) | Y |  |  |
| 13 | SOLICITA_MOD_DW | CHAR(1) | Y |  |  |
| 14 | NOME_COLUNA | VARCHAR2(40) | Y |  |  |
| 15 | SOLUCAO_ERRO | VARCHAR2(500) | Y |  |  |

**PK**: COD_ERRO

---

## CAT_FK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOM_FK | VARCHAR2(40) | N |  |  |
| 2 | DSC_TABELA | VARCHAR2(100) | Y |  |  |

**PK**: NOM_FK

---

## CAT_GRUPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 2 | DSC_GRUPO | VARCHAR2(40) | Y |  |  |

**PK**: GRUPO_ARQUIVO

---

## CAT_GRUPO_DIC_DADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO | VARCHAR2(5) | N |  |  |
| 2 | COD_CATEGORIA | VARCHAR2(30) | N |  |  |
| 3 | DESC_CATEGORIA | VARCHAR2(100) | Y |  |  |
| 4 | INF_COMPL | VARCHAR2(4000) | Y |  |  |

**PK**: COD_GRUPO, COD_CATEGORIA

**FKs**:
- COD_GRUPO → GRUPO_DIC_DADOS(COD_GRUPO)

---

## CAT_LAYOUT_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOM_TAB_WORK | VARCHAR2(8) | N |  |  |
| 2 | NUM_CAMPO | NUMBER(4) | N |  |  |
| 3 | PATCH | VARCHAR2(10) | N |  | Patch de criacao da tabela. |
| 4 | IND_OBRIG | VARCHAR2(1) | N |  | Indica se o campo e de preenchimento obrigatorio: S ou N. |
| 5 | DESCRICAO | VARCHAR2(300) | N |  |  |
| 6 | NOME_CAMPO | VARCHAR2(30) | N |  | Nome do campo no banco de dados. |
| 7 | TAMANHO | VARCHAR2(20) | N |  | Tamanho do campo, conforme manual de layout. ex: vlr 015V002, aliq 003V004 ou 001. |
| 8 | TIPO | VARCHAR2(1) | N |  | Informar A – Alfanumerico ou N - Numerico. |
| 9 | VERSAO | VARCHAR2(10) | Y |  | Versao do produto. |
| 10 | MFS_ALTERA | VARCHAR2(30) | Y |  | Numero da demanda do jira de alteracao da tabela. |
| 11 | IND_ALT | VARCHAR2(3) | Y |  | Indica o tipo de alteracao realizada na tabela, conforme abaixo. C/S – Criação de SAFX; M/S – Modifica Estrutura da SAFX; I/C – Inclusao de Campo em SAFX; A/N – Alteracao de Nome de Campo em SAFX; A/O – Alteracao do Campo Obrigatoriedade; C/C – Alteracao de Comentario do Campo; A/D – Alteracao do Campo Descricao; A/T – Alteracao do Campo Tamanho; T/C – Alteracao do Tipo de Campo; C/E – Critica de Erros |
| 12 | DSC_COMENTARIO | VARCHAR2(4000) | Y |  | Comentario com orientacoes para preenchimento do campo na importacao da tabela SAFX |

**PK**: NOM_TAB_WORK, NUM_CAMPO, PATCH

---

## CAT_LAYOUT_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOM_TAB_WORK | VARCHAR2(8) | N |  |  |
| 2 | NUM_CAMPO | NUMBER(4) | N |  |  |
| 3 | IND_OBRIG | VARCHAR2(1) | N |  | Indica se o campo e de preenchimento obrigatorio: S ou N. |
| 4 | DESCRICAO | VARCHAR2(300) | N |  |  |
| 5 | NOME_CAMPO | VARCHAR2(30) | N |  | Nome do campo no banco de dados. |
| 6 | TAMANHO | VARCHAR2(20) | N |  | Tamanho do campo, conforme manual de layout. ex: vlr 015V002, aliq 003V004 ou 001. |
| 7 | TIPO | VARCHAR2(1) | N |  | Informar A – Alfanumerico ou N - Numerico. |
| 8 | VERSAO | VARCHAR2(10) | Y |  | Versao do produto. |
| 9 | PATCH | VARCHAR2(10) | Y |  | Patch de criacao da tabela. |
| 10 | MFS_ORIGEM | VARCHAR2(30) | Y |  | Numero da demanda do jira de criacao da tabela. |
| 11 | COD_ERRO | VARCHAR2(100) | Y |  | Relacao dos códigos de erros tratados para o campo. |
| 12 | NOME_CAMPO_DEST | VARCHAR2(30) | Y |  | Campo que sera utilizado no processo exportacao. |
| 13 | DSC_COMENTARIO | VARCHAR2(4000) | Y |  | Comentario com orientacoes para preenchimento do campo na importacao da tabela SAFX |
| 14 | IND_VALID_OBI | VARCHAR2(1) | Y | 'N' |  |

**PK**: NOM_TAB_WORK, NUM_CAMPO

---

## CAT_MANUAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_MANUAL | VARCHAR2(1) | N |  |  |
| 2 | VERSAO | NUMBER(5) | N |  |  |
| 3 | COD_ARQUIVO | VARCHAR2(12) | N |  |  |
| 4 | TIPO_REGISTRO | VARCHAR2(4) | N |  |  |
| 5 | NUM_ITEM | NUMBER(4) | N |  |  |
| 6 | DSC_ARQUIVO | VARCHAR2(250) | Y |  |  |
| 7 | IND_QUEBRA_ARQ | CHAR(1) | Y |  |  |
| 8 | DSC_REGISTRO | VARCHAR2(50) | Y |  |  |
| 9 | DSC_CAMPO | VARCHAR2(250) | Y |  |  |
| 10 | TIPO_CAMPO | CHAR(1) | Y |  |  |
| 11 | TAM_CAMPO | NUMBER(3) | Y |  |  |
| 12 | TAM_DEC_CAMPO | NUMBER(2) | Y |  |  |
| 13 | IND_OB_CAMPO | CHAR(1) | Y |  |  |
| 14 | POS_CAMPO | NUMBER(4) | Y |  |  |
| 15 | NOM_TABELA | VARCHAR2(25) | Y |  |  |
| 16 | NOM_CAMPO | VARCHAR2(25) | Y |  |  |
| 17 | COD_ERRO | NUMBER(6) | Y |  |  |
| 18 | COMENTARIO | LONG | Y |  |  |

**PK**: IND_MANUAL, VERSAO, COD_ARQUIVO, TIPO_REGISTRO, NUM_ITEM

---

## CAT_MASC_IMPORT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSC_MASCARA | VARCHAR2(4) | N |  |  |
| 2 | DSC_ARQ_SAF | VARCHAR2(4) | N |  |  |
| 3 | DSC_ARQUIVOS | VARCHAR2(60) | Y |  |  |

**PK**: DSC_MASCARA, DSC_ARQ_SAF

---

## CAT_OBSERVACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OBSERVACAO | VARCHAR2(3) | N |  |  |
| 2 | OBSERVACAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_OBSERVACAO

---

## CAT_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CFO | NUMBER(12) | N |  |  |
| 4 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 5 | DESC_NOP | VARCHAR2(50) | Y |  |  |
| 6 | FUND_LEGAL_1 | VARCHAR2(60) | Y |  |  |
| 7 | FUND_LEGAL_2 | VARCHAR2(60) | Y |  |  |
| 8 | FUND_LEGAL_3 | VARCHAR2(60) | Y |  |  |
| 9 | FUND_LEGAL_4 | VARCHAR2(60) | Y |  |  |
| 10 | FUND_LEGAL_5 | VARCHAR2(60) | Y |  |  |
| 11 | DAT_VIGENCIA | DATE | Y |  |  |
| 12 | DAT_VALIDADE | DATE | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | TRIBUT_ICMS | VARCHAR2(1) | Y |  |  |
| 15 | TRIBUT_IPI | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## CAT_PACKAGE_MODULO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOME_OBJETO | VARCHAR2(200) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(1000) | Y |  |  |
| 3 | AGRUPAMENTO | VARCHAR2(100) | Y |  |  |
| 4 | MODULO | VARCHAR2(300) | Y |  |  |

**PK**: NOME_OBJETO

---

## CAT_PRIOR_BR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOME_TABELA_BANCO | VARCHAR2(30) | N |  |  |
| 2 | CLASSIFICACAO | VARCHAR2(2) | Y |  |  |
| 3 | DESC_TABELA | VARCHAR2(250) | Y |  |  |
| 4 | PRIOR_LIMPEZA | NUMBER(5) | Y |  |  |
| 5 | VERSAO | NUMBER(5,2) | Y |  |  |
| 6 | IND_TEM_ESTAB | CHAR(1) | Y |  |  |
| 7 | IND_TEM_PROCESSO | CHAR(1) | Y |  |  |
| 8 | NOM_COL_DATA_REF | VARCHAR2(18) | Y |  |  |
| 9 | IND_GERA_BCK_CD | CHAR(1) | Y |  |  |

**PK**: NOME_TABELA_BANCO

---

## CAT_PRIOR_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 2 | NUMERO_ARQUIVO | NUMBER(3) | N |  |  |
| 3 | DESCRICAO_ARQUIVO | VARCHAR2(50) | Y |  |  |
| 4 | NOM_TAB_WORK | VARCHAR2(8) | Y |  |  |
| 5 | IND_ESTAB_GRP | CHAR(1) | Y |  |  |
| 6 | IND_LIM_PERIODO | CHAR(1) | Y |  |  |
| 7 | IND_TAB_CARGA | CHAR(1) | Y |  |  |
| 8 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se a SAFX vai ser carregada/importada via funcionalidade do ATO COTEPE |
| 9 | IND_MULTI_LOAD | CHAR(1) | Y |  | Indica se a importacao da SAFX sera feita pelo processo linear ou multi job |
| 10 | NOM_TAB_DEF | VARCHAR2(100) | N |  | Nome da Tabela definitiva da respectiva SAFX importada também utilizada no processo multi job |
| 11 | DATA_REF_TAB_DEF | VARCHAR2(100) | Y |  | Nome do campo de data de referencia da respectiva SAFX importada pelo processo multi job |
| 12 | LEGISLACAO | VARCHAR2(300) | Y |  | LEGISLACAO a que a tabela esta vinculada (Aba Indice - Manual de Layout |
| 13 | OBJETIVO | VARCHAR2(4000) | N |  | OBJETIVO que orienta sobre a utilizacao da tabela (Aba Indice - Manual de Layout |
| 14 | IND_VALID_OBI | VARCHAR2(1) | Y | 'N' |  |

**PK**: GRUPO_ARQUIVO, NUMERO_ARQUIVO

**Indexes**:
- IX_CAT_PRIOR_IMP: (NOM_TAB_WORK)

---

## CAT_PROCESSO_AUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | OBJETO | VARCHAR2(35) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | Y |  |  |

**PK**: OBJETO

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## CAT_TABELAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TABELA | NUMBER(5) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | IND_ASSOCIACAO | CHAR(1) | Y |  |  |
| 4 | NOME_BD | VARCHAR2(30) | Y |  |  |

**PK**: COD_TABELA

---

## CAT_TABELAS_BCK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOME_BD_BCK | VARCHAR2(40) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(500) | Y |  |  |
| 3 | DSC_MODULO | VARCHAR2(40) | Y |  |  |
| 4 | NUM_OS | VARCHAR2(20) | Y |  |  |

**PK**: NOME_BD_BCK

---

