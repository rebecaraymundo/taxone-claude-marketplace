# Módulo: SAF (SAF) - 24 tabelas

## SAF_BATFK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TB_ID | NUMBER(4) | N |  |  |
| 2 | FK_ID | NUMBER(4) | N |  |  |
| 3 | FK_NOME | VARCHAR2(45) | Y |  |  |
| 4 | TB_ID_REF | NUMBER(4) | Y |  |  |
| 5 | IX_ID_REF | NUMBER(4) | Y |  |  |

**PK**: TB_ID, FK_ID

**Indexes**:
- IX_SAF_BATFK (UNIQUE): (FK_NOME)

---

## SAF_BATFK_COL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TB_ID | NUMBER(4) | N |  |  |
| 2 | FK_ID | NUMBER(4) | N |  |  |
| 3 | COL_SEQ | NUMBER(4) | Y |  |  |
| 4 | COL_ID | NUMBER(4) | N |  |  |

**PK**: TB_ID, FK_ID, COL_ID

---

## SAF_BATFU

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FU_NOME | VARCHAR2(30) | N |  |  |
| 2 | NUM_LINHAS | NUMBER(4) | Y |  |  |

**PK**: FU_NOME

---

## SAF_BATIX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TB_ID | NUMBER(4) | N |  |  |
| 2 | IX_ID | NUMBER(4) | N |  |  |
| 3 | IX_NOME | VARCHAR2(40) | Y |  |  |
| 4 | UNIQUENESS | VARCHAR2(9) | Y |  |  |

**PK**: TB_ID, IX_ID

**Indexes**:
- IX_SAF_BATIX (UNIQUE): (IX_NOME)

---

## SAF_BATIX_COL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TB_ID | NUMBER(4) | N |  |  |
| 2 | IX_ID | NUMBER(4) | N |  |  |
| 3 | COL_SEQ | NUMBER(4) | Y |  |  |
| 4 | COL_ID | NUMBER(4) | N |  |  |

**PK**: TB_ID, IX_ID, COL_ID

---

## SAF_BATRES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | OBJ_TIPO | VARCHAR2(5) | Y |  |  |
| 2 | OBJ_NOME | VARCHAR2(25) | Y |  |  |
| 3 | ERRO | VARCHAR2(10) | Y |  |  |
| 4 | COLUNA | VARCHAR2(25) | Y |  |  |
| 5 | COL_BD | VARCHAR2(25) | Y |  |  |
| 6 | COL_MOD | VARCHAR2(25) | Y |  |  |

---

## SAF_BATSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SP_NOME | VARCHAR2(30) | N |  |  |
| 2 | NUM_LINHAS | NUMBER(4) | Y |  |  |

**PK**: SP_NOME

---

## SAF_BATTB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TB_ID | NUMBER(4) | N |  |  |
| 2 | TB_NOME | VARCHAR2(40) | Y |  |  |

**PK**: TB_ID

---

## SAF_BATTB_COL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TB_ID | NUMBER(4) | N |  |  |
| 2 | COL_ID | NUMBER(4) | N |  |  |
| 3 | COL_NOME | VARCHAR2(50) | Y |  |  |
| 4 | DATA_TYPE | VARCHAR2(128) | Y |  |  |
| 5 | DATA_LENGTH | NUMBER(4) | Y |  |  |
| 6 | DATA_PRECISION | NUMBER(4) | Y |  |  |
| 7 | DATA_SCALE | NUMBER(4) | Y |  |  |
| 8 | NULLABLE | CHAR(1) | Y |  |  |

**PK**: TB_ID, COL_ID

**Indexes**:
- IX_SAF_BATTB_COL (UNIQUE): (TB_ID, COL_NOME)

---

## SAF_BATTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TR_NOME | VARCHAR2(30) | N |  |  |
| 2 | TB_ID | NUMBER(4) | Y |  |  |
| 3 | TR_TIPO | VARCHAR2(16) | Y |  |  |
| 4 | TR_EVENTO | VARCHAR2(26) | Y |  |  |
| 5 | TR_STATUS | VARCHAR2(8) | Y |  |  |

**PK**: TR_NOME

---

## SAF_CONTROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSC_UPG | VARCHAR2(10) | N |  |  |
| 2 | DAT_SISTEMA | DATE | Y |  |  |
| 3 | DAT_ATUALIZ | DATE | Y |  |  |
| 4 | IND_FINAL | VARCHAR2(2) | Y |  |  |

**PK**: DSC_UPG

---

## SAF_CONTROLE_DICT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | OBJNAME | VARCHAR2(128) | Y |  |  |
| 2 | OBJTYPE | VARCHAR2(128) | Y |  |  |
| 3 | SUBOBJECTNAME | VARCHAR2(128) | Y |  |  |
| 4 | CONTROLE | NUMBER(30) | Y |  |  |

**Indexes**:
- IX_SAF_CONTROLE_DICT: (OBJNAME, SUBOBJECTNAME)

---

## SAF_CONTROLE_PATCH

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSC_PATCH | VARCHAR2(50) | N |  |  |
| 2 | DSC_UPG | VARCHAR2(15) | N |  |  |
| 3 | MODULO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_ATUALIZA | DATE | Y |  |  |
| 5 | DAT_PATCH | DATE | Y |  |  |
| 6 | PASS | VARCHAR2(22) | Y |  |  |
| 7 | NUM_PATCH | VARCHAR2(20) | Y |  |  |
| 8 | NUM_SPRINT | VARCHAR2(10) | Y |  |  |
| 9 | DESVINCULADO | CHAR(1) | Y | 'N' |  |

**PK**: DSC_PATCH, DSC_UPG

---

## SAF_CONTROLE_PATCH_TRG_AUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DSC_PATCH | VARCHAR2(50) | N |  |  |
| 2 | TABELA | VARCHAR2(100) | N |  |  |

**Indexes**:
- IX_SAF_CONTR_PATCH_TRG_AUD: (DSC_PATCH)
- UK_SAF_CONTR_PATCH_TRG_AUD (UNIQUE): (DSC_PATCH, TABELA)

---

## SAF_CONTROLE_PERF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | NUM_PROC | NUMBER(12) | N |  |  |
| 3 | PATCH | VARCHAR2(100) | N |  |  |
| 4 | FUNCIONALIDADE | VARCHAR2(4000) | Y |  |  |
| 5 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 7 | DT_INI | DATE | Y |  |  |
| 8 | DT_FIM | DATE | Y |  |  |
| 9 | DT_INI_GERACAO | DATE | Y |  |  |
| 10 | DT_FIM_GERACAO | DATE | Y |  |  |
| 11 | USUARIO | VARCHAR2(100) | Y |  |  |
| 12 | SITUACAO | VARCHAR2(100) | Y |  |  |
| 13 | QTDE_LINHAS | NUMBER(12) | Y |  |  |
| 14 | DT_FILA_INI | DATE | Y |  |  |
| 15 | DT_FILA_FIM | DATE | Y |  |  |

**PK**: ID_REG

**Indexes**:
- UK_SAF_CONTROLE_PERF (UNIQUE): (NUM_PROC, PATCH)

---

## SAF_DIC_INDICE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TABELA | VARCHAR2(30) | N |  | Campo destinado para discriminar o codigo da tabela no sistema |
| 2 | NOME | VARCHAR2(200) | N |  | Campo destinado para discriminar o nome da tabela no sistema |
| 3 | DSC_LEGISLACAO | VARCHAR2(4000) | Y |  | Campo destinado para discriminar as legislacoes que se utilizam da tabela |
| 4 | OBJ_TABELA | VARCHAR2(4000) | Y |  | Campo destinado para discriminar o objetivo da tabela |
| 5 | COD_TABELA_PAI | VARCHAR2(30) | Y |  |  |

**PK**: COD_TABELA

---

## SAF_DIC_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TABELA | VARCHAR2(30) | N |  |  |
| 2 | SEQ_ID | NUMBER(12) | N |  |  |
| 3 | NOME_CAMPO | VARCHAR2(50) | N |  |  |
| 4 | IND_OBRIG | CHAR(1) | Y |  |  |
| 5 | IND_PK | CHAR(1) | Y |  |  |
| 6 | DSC_CAMPO | VARCHAR2(200) | Y |  |  |
| 7 | COMENTARIO | VARCHAR2(4000) | Y |  |  |
| 8 | IND_TIPO | VARCHAR2(2) | N |  |  |
| 9 | TAMANHO | NUMBER(3) | N |  |  |
| 10 | NUM_DECIMAL | NUMBER(1) | Y |  |  |

**PK**: COD_TABELA, SEQ_ID, NOME_CAMPO

**FKs**:
- COD_TABELA → SAF_DIC_INDICE(COD_TABELA)

---

## SAF_DW_ACESSOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_SAF_DW_ACESSOS | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | NOME_MODULO | VARCHAR2(40) | Y |  |  |
| 4 | NOME_OBJETO | VARCHAR2(50) | Y |  |  |
| 5 | NUM_ACESSOS | NUMBER(6) | Y |  |  |
| 6 | DATA_ULT_ACESSO | DATE | Y |  |  |
| 7 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 8 | DSC_SPRINT | VARCHAR2(4) | Y |  |  |
| 9 | NUM_PERIODO | NUMBER(6) | Y |  |  |
| 10 | NOME_MODULO_MUNIC | VARCHAR2(100) | Y |  |  |

**PK**: ID_SAF_DW_ACESSOS

**Indexes**:
- IX_SAF_DW_ACESSOS_01: (NOME_OBJETO, DATA_ULT_ACESSO)

---

## SAF_ENCERRA_X02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 6 | VLR_TOT_CRE | NUMBER(19,2) | Y |  |  |
| 7 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 8 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 9 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 10 | VLR_SALDO_FIM | NUMBER(19,2) | Y |  |  |
| 11 | IND_SALDO_FIM | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO, IDENT_CONTA

---

## SAF_ENCERRA_X80

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_SALDO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 6 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 7 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 8 | VLR_TOT_CRE | NUMBER(19,2) | Y |  |  |
| 9 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 10 | VLR_SALDO_CONT_ANT | NUMBER(19,2) | Y |  |  |
| 11 | IND_DEB_CRED_ANT | CHAR(1) | Y |  |  |
| 12 | VLR_SALDO_CONT_ATU | NUMBER(19,2) | Y |  |  |
| 13 | IND_DEB_CRED_ATU | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_CUSTO

---

## SAF_LOCK_CONTROL
**Comment**: Tabela de controle para rastrear locks de aplicacaoo sem depender de GV$LOCK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LOCK_NAME | VARCHAR2(200) | N |  | Nome unico do lock (__MUTEX__ ou nome do processo) |
| 2 | USERNAME | VARCHAR2(100) | Y |  |  |
| 3 | PROC_ID | NUMBER(12) | N |  | ID do processo (lib_processo.proc_id) - 0 para MUTEX |
| 4 | SID | NUMBER | N |  | Session ID do Oracle |
| 5 | SERIAL# | NUMBER | N |  | Serial# da sessao |
| 6 | START_TIME | TIMESTAMP(6) | Y | SYSTIMESTAMP | Momento em que o lock foi adquirido |
| 7 | LAST_UPDATE | TIMESTAMP(6) | Y | SYSTIMESTAMP | Ultima atualizacao do lock (heartbeat) |
| 8 | STATUS | VARCHAR2(20) | Y | 'ACTIVE' | ACTIVE, RELEASED, EXPIRED |
| 9 | PROCESS_ID | VARCHAR2(100) | Y |  |  |
| 10 | MACHINE | VARCHAR2(100) | Y |  |  |
| 11 | PROGRAM | VARCHAR2(200) | Y |  |  |

**PK**: LOCK_NAME, PROC_ID, SID, SERIAL#

**Indexes**:
- IDX_LOCK_CTRL_STATUS: (STATUS, START_TIME)

---

## SAF_MANAGER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ITEM_MENU | NUMBER(12) | N |  |  |
| 2 | DESC_ITEM_MENU | VARCHAR2(100) | Y |  |  |
| 3 | IND_TIPO_MENU | CHAR(1) | Y |  |  |
| 4 | IND_PARAMETROS | CHAR(1) | Y |  |  |
| 5 | APLICACAO | VARCHAR2(100) | Y |  |  |
| 6 | IDENT_ITEM_PAI | NUMBER(12) | Y |  |  |
| 7 | SEQ_ORDENACAO | NUMBER(3) | Y |  |  |
| 8 | ICONE | VARCHAR2(30) | Y |  |  |
| 9 | IND_APRES_SEM_LIC | VARCHAR2(1) | Y | 'S' |  |
| 10 | DESC_RESUM_ITEM_MENU | VARCHAR2(1000) | Y |  |  |
| 11 | PATH | VARCHAR2(500) | Y |  |  |
| 12 | VERSAO | VARCHAR2(10) | Y |  |  |
| 13 | COD_MODULO_LIC | VARCHAR2(40) | Y |  | Descrição dos modulos para o licenciamento |
| 14 | IND_TAX_ONE | VARCHAR2(1) | Y | 'N' |  |
| 15 | IND_DW | VARCHAR2(1) | Y | 'N' |  |

**PK**: IDENT_ITEM_MENU

**FKs**:
- IDENT_ITEM_PAI → SAF_MANAGER(IDENT_ITEM_MENU)

---

## SAF_MANAGER_FAVORITO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | FLOAT | N |  |  |
| 2 | USR_KEY | FLOAT | N |  |  |

**PK**: APP_KEY, USR_KEY

---

## SAF_SEQ_NOTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_DOCFIS | NUMBER(12) | N |  |  |
| 2 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 3 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | COD_MODELO | VARCHAR2(2) | N |  |  |

**PK**: NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, MOVTO_E_S, COD_MODELO

---

