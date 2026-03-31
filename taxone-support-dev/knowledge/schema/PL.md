# Módulo: PL (PL) - 28 tabelas

## PL_ADMIN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ADM_KEY | NUMBER | Y |  |  |
| 2 | ADM_LOGIN | VARCHAR2(40) | Y |  |  |
| 3 | ADM_PWD | VARCHAR2(20) | Y |  |  |
| 4 | ADM_NAME | VARCHAR2(40) | Y |  |  |
| 5 | ADM_PROMPT_COPY | VARCHAR2(1) | Y |  |  |
| 6 | ADM_PROMPT_DELETE | VARCHAR2(1) | Y |  |  |
| 7 | ADM_STATUS | NUMBER | Y |  |  |
| 8 | ADM_GRACE | NUMBER | Y |  |  |
| 9 | ADM_EXPIRE_DATE | VARCHAR2(8) | Y |  |  |

**Indexes**:
- PL_ADMIN1 (UNIQUE): (ADM_KEY)
- PL_ADMIN2 (UNIQUE): (ADM_LOGIN, ADM_PWD)

---

## PL_ADMIN_ADMROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ADM_KEY | NUMBER | Y |  |  |
| 2 | ADMROLE_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_ADM_ADMROLE1 (UNIQUE): (ADM_KEY, ADMROLE_KEY)

---

## PL_ADMROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ADMROLE_KEY | NUMBER | Y |  |  |
| 2 | ADMROLE_NAME | VARCHAR2(40) | Y |  |  |

**Indexes**:
- PL_ADMROLE1 (UNIQUE): (ADMROLE_KEY)

---

## PL_APP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | APP_NAME | VARCHAR2(100) | Y |  |  |
| 3 | APP_EXE | VARCHAR2(40) | Y |  |  |
| 4 | APP_STATUS | NUMBER | Y |  |  |
| 5 | APP_GRACE | NUMBER | Y |  |  |
| 6 | APP_COLOR | NUMBER | Y |  |  |
| 7 | APP_PWD_DAYS | NUMBER | Y |  |  |
| 8 | APP_USE_NETID | VARCHAR2(1) | Y |  |  |
| 9 | APP_USE_AUDIT | VARCHAR2(1) | Y |  |  |
| 10 | APP_SHOW_REG | VARCHAR2(1) | Y |  |  |
| 11 | APP_USE_LOGIN | VARCHAR2(1) | Y |  |  |
| 12 | APP_OBJ | VARCHAR2(40) | Y |  |  |
| 13 | APP_LIC | VARCHAR2(40) | Y |  |  |

**Indexes**:
- PL_APP1 (UNIQUE): (APP_KEY)
- PL_APP2 (UNIQUE): (APP_NAME)
- PL_APP3 (UNIQUE): (APP_OBJ, APP_LIC)

---

## PL_APP_DB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | DB_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_APP_DB1 (UNIQUE): (APP_KEY, DB_KEY)

---

## PL_APP_GRP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | GRP_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_APP_GRP1 (UNIQUE): (APP_KEY, GRP_KEY)

---

## PL_APP_USR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | USR_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_APP_USR1 (UNIQUE): (APP_KEY, USR_KEY)

---

## PL_AUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | AUD_KEY | NUMBER | Y |  |  |
| 2 | APP_KEY | NUMBER | Y |  |  |
| 3 | USR_KEY | NUMBER | Y |  |  |
| 4 | AUD_START_TIME | VARCHAR2(30) | Y |  |  |
| 5 | AUD_END_TIME | VARCHAR2(30) | Y |  |  |
| 6 | ACESSO_OK | CHAR(1) | Y |  |  |
| 7 | LOGIN_DIGITADO | VARCHAR2(60) | Y |  |  |
| 8 | USUARIO_WINDOWS | VARCHAR2(80) | Y |  |  |
| 9 | NOME_MAQUINA | VARCHAR2(80) | Y |  |  |

**Indexes**:
- PL_AUD1 (UNIQUE): (AUD_KEY)

---

## PL_AUDIT_MKT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USR_KEY | NUMBER | N |  |  |
| 2 | APP_KEY | NUMBER | N |  |  |
| 3 | FIRST_ACCESS | DATE | Y | sysdate |  |
| 4 | LAST_ACCESS | DATE | Y |  |  |
| 5 | QUANTITY | NUMBER | Y |  |  |

**PK**: USR_KEY, APP_KEY

---

## PL_AUD_ADM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | AUD_ADM_KEY | NUMBER | Y |  |  |
| 2 | AUD_START_TIME | VARCHAR2(30) | Y |  |  |
| 3 | AUD_END_TIME | VARCHAR2(30) | Y |  |  |
| 4 | LOGIN_DIGITADO | VARCHAR2(60) | Y |  |  |
| 5 | ACESSO_OK | CHAR(1) | Y |  |  |
| 6 | USUARIO_WINDOWS | VARCHAR2(80) | Y |  |  |
| 7 | NOME_MAQUINA | VARCHAR2(80) | Y |  |  |

**Indexes**:
- IX_AUD_ADM (UNIQUE): (AUD_ADM_KEY)

---

## PL_DB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DB_KEY | NUMBER | Y |  |  |
| 2 | DB_NAME | VARCHAR2(40) | Y |  |  |
| 3 | DB_DBMS | VARCHAR2(60) | Y |  |  |
| 4 | DB_DATABASE | VARCHAR2(60) | Y |  |  |
| 5 | DB_SERVER | VARCHAR2(60) | Y |  |  |
| 6 | DB_USERID | VARCHAR2(60) | Y |  |  |
| 7 | DB_DBPASS | VARCHAR2(60) | Y |  |  |
| 8 | DB_LOGID | VARCHAR2(60) | Y |  |  |
| 9 | DB_LOGPASS | VARCHAR2(60) | Y |  |  |
| 10 | DB_DBPARM | VARCHAR2(120) | Y | 'DISABLEBIND=1' |  |
| 11 | DB_LOCK | VARCHAR2(60) | Y |  |  |
| 12 | DB_COMMIT | VARCHAR2(60) | Y |  |  |
| 13 | STATUS | VARCHAR2(1) | Y | 'N' |  |

**Indexes**:
- PL_DB1 (UNIQUE): (DB_KEY)

---

## PL_GRP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRP_KEY | NUMBER | Y |  |  |
| 2 | GRP_NAME | VARCHAR2(256) | Y |  |  |

**Indexes**:
- PL_GRP1 (UNIQUE): (GRP_KEY)
- PL_GRP2 (UNIQUE): (GRP_NAME)

---

## PL_GRP_DB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRP_KEY | NUMBER | Y |  |  |
| 2 | DB_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_GRP_DB1 (UNIQUE): (GRP_KEY, DB_KEY)

---

## PL_GRP_ROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | GRP_KEY | NUMBER | Y |  |  |
| 3 | ROLE_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_GRP_ROLE1 (UNIQUE): (APP_KEY, GRP_KEY, ROLE_KEY)

---

## PL_GRP_USR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRP_KEY | NUMBER | Y |  |  |
| 2 | USR_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_GRP_USR1 (UNIQUE): (GRP_KEY, USR_KEY)

---

## PL_KEYS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ADM_KEY | NUMBER | Y |  |  |
| 2 | APP_KEY | NUMBER | Y |  |  |
| 3 | GRP_KEY | NUMBER | Y |  |  |
| 4 | USR_KEY | NUMBER | Y |  |  |
| 5 | DB_KEY | NUMBER | Y |  |  |
| 6 | ROLE_KEY | NUMBER | Y |  |  |
| 7 | OBJ_KEY | NUMBER | Y |  |  |
| 8 | AUD_KEY | NUMBER | Y |  |  |
| 9 | AUD_ADM_KEY | NUMBER | Y |  |  |

---

## PL_OBJ_ATTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | OBJ_KEY | NUMBER | Y |  |  |
| 3 | ROLE_KEY | NUMBER | Y |  |  |
| 4 | OBJ_BIT | NUMBER | Y |  |  |
| 5 | ROW_TYPE | CHAR(1) | Y |  |  |
| 6 | ROW_CRITERIA | VARCHAR2(254) | Y |  |  |

**Indexes**:
- PL_OBJ_ATTR1 (UNIQUE): (APP_KEY, OBJ_KEY, ROLE_KEY)

---

## PL_OBJ_REG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | OBJ_KEY | NUMBER | Y |  |  |
| 3 | OBJ_WINDOW | VARCHAR2(40) | Y |  |  |
| 4 | OBJ_NAME | VARCHAR2(1500) | Y |  |  |
| 5 | OBJ_DESC | VARCHAR2(100) | Y |  |  |
| 6 | OBJ_TYPE | NUMBER | Y |  |  |
| 7 | OBJ_TBLCOL | VARCHAR2(100) | Y |  |  |

**Indexes**:
- PL_OBJ_REG1 (UNIQUE): (OBJ_KEY)

---

## PL_PREF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PREF_APP_GRACE | NUMBER | Y |  |  |
| 2 | PREF_APP_COLOR | NUMBER | Y |  |  |
| 3 | PREF_APP_PWD_DAYS | NUMBER | Y |  |  |
| 4 | PREF_APP_USE_NETID | VARCHAR2(1) | Y |  |  |
| 5 | PREF_APP_USE_AUDIT | VARCHAR2(1) | Y |  |  |
| 6 | PREF_USE_ENCRYPT | VARCHAR2(1) | Y |  |  |
| 7 | PREF_PROMPT_COPY | VARCHAR2(1) | Y |  |  |
| 8 | PREF_PROMPT_DELETE | VARCHAR2(1) | Y |  |  |
| 9 | PREF_APP_USE_LOGIN | VARCHAR2(1) | Y |  |  |
| 10 | PREF_IND_SSO | VARCHAR2(1) | Y |  |  |
| 11 | PREF_IND_LDAP | VARCHAR2(1) | Y |  |  |
| 12 | PREF_URL_LDAP_SERVER | VARCHAR2(500) | Y |  |  |
| 13 | PREF_IND_SSL | VARCHAR2(1) | Y |  |  |
| 14 | PREF_LOGIN_MASTER_LDAP | VARCHAR2(256) | Y |  |  |
| 15 | PREF_PWD_MASTER_LDAP | VARCHAR2(256) | Y |  |  |
| 16 | PREF_PROFILE_NAME_LDAP | VARCHAR2(256) | Y |  |  |
| 17 | PREF_IND_PROF_LDAP | VARCHAR2(1) | Y |  |  |
| 18 | PREF_ALT_PORT | VARCHAR2(10) | Y |  |  |
| 19 | PREF_ALT_SEARCH_DOMAIN | VARCHAR2(500) | Y |  |  |
| 20 | PREF_IND_USE_SRCH_DOM | VARCHAR2(1) | Y |  |  |
| 21 | PREF_IND_USE_USR_DOM | VARCHAR2(1) | Y |  |  |

---

## PL_ROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | ROLE_KEY | NUMBER | Y |  |  |
| 3 | ROLE_NAME | VARCHAR2(40) | Y |  |  |

**Indexes**:
- PL_ROLE1 (UNIQUE): (ROLE_KEY, APP_KEY)

---

## PL_USR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USR_KEY | NUMBER | Y |  |  |
| 2 | USR_LOGIN | VARCHAR2(40) | Y |  |  |
| 3 | USR_PWD | VARCHAR2(50) | Y |  |  |
| 4 | USR_STATUS | NUMBER | Y |  |  |
| 5 | USR_FNAME | VARCHAR2(25) | Y |  |  |
| 6 | USR_LNAME | VARCHAR2(25) | Y |  |  |
| 7 | USR_NAME | VARCHAR2(40) | Y |  |  |
| 8 | USR_PWD_DATE | VARCHAR2(8) | Y |  |  |
| 9 | USR_EXPIRE_DATE | VARCHAR2(8) | Y |  |  |
| 10 | USR_DB_DEFAULT | NUMBER | Y |  |  |
| 11 | DT_ULT_ACESSO | DATE | Y |  |  |
| 12 | IND_TROCA_SENHA | CHAR(1) | Y | 'N' |  |
| 13 | NUM_ERRO_LOGIN | NUMBER(3) | Y | 0 |  |
| 14 | USR_ALLOW_TRACE | CHAR(1) | Y | 'N' | Indica se o usuario tem permissao de inicar/encerrar Trace |
| 15 | EMAIL | VARCHAR2(60) | Y |  |  |
| 16 | USR_BIRTH_DATE | DATE | Y |  |  |
| 17 | POPUP | CHAR(1) | Y | 'N' |  |
| 18 | SHOW_POPUP | CHAR(1) | Y | 'Y' |  |
| 19 | SHOW_POPUP_SPED | CHAR(1) | Y | 'Y' |  |
| 20 | SHOW_POPUP_GER_SPED | CHAR(1) | Y | 'Y' |  |
| 21 | SHOW_POPUP_PISCOF | CHAR(1) | Y | 'Y' |  |
| 22 | USR_MATRICULA | VARCHAR2(20) | Y |  |  |
| 23 | USR_CPF | VARCHAR2(11) | Y |  |  |
| 24 | PASSAPORTE | VARCHAR2(20) | Y |  |  |
| 25 | SHOW_DASH | CHAR(1) | Y | 'Y' |  |
| 26 | IND_BLOQ_ACESSO | CHAR(1) | Y | 'N' |  |
| 27 | SHOW_POPUP_PESQUISA | VARCHAR2(1) | Y | 'Y' |  |
| 28 | ADM_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_USR2 (UNIQUE): (USR_KEY)
- PL_USR3 (UNIQUE): (USR_LOGIN)

---

## PL_USR_ATTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USR_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_USR_ATTR1 (UNIQUE): (USR_KEY)

---

## PL_USR_AUDIT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USR_KEY | NUMBER | Y |  |  |
| 2 | USR_LOGIN | VARCHAR2(40) | Y |  |  |
| 3 | DT_REG | DATE | Y |  |  |
| 4 | USR_FNAME | VARCHAR2(25) | Y |  |  |
| 5 | USR_LNAME | VARCHAR2(25) | Y |  |  |
| 6 | ADM_KEY | NUMBER | Y |  |  |
| 7 | ADM_LOGIN | VARCHAR2(40) | Y |  |  |
| 8 | ADM_NAME | VARCHAR2(40) | Y |  |  |
| 9 | USR_STATUS | NUMBER | Y |  |  |
| 10 | USR_EXPIRE_DATE | VARCHAR2(8) | Y |  |  |
| 11 | USR_MODIFY | VARCHAR2(1) | Y |  |  |

---

## PL_USR_DB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USR_KEY | NUMBER | Y |  |  |
| 2 | DB_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_USR_DB1 (UNIQUE): (USR_KEY, DB_KEY)

---

## PL_USR_ROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | APP_KEY | NUMBER | Y |  |  |
| 2 | USR_KEY | NUMBER | Y |  |  |
| 3 | ROLE_KEY | NUMBER | Y |  |  |

**Indexes**:
- PL_USR_ROLE1 (UNIQUE): (APP_KEY, USR_KEY, ROLE_KEY)

---

## PL_USR_VALID

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USR_KEY | FLOAT | Y |  |  |
| 2 | USR_PWD | VARCHAR2(20) | Y |  |  |
| 3 | DAT_CAD_PWD | DATE | Y |  |  |
| 4 | DAT_VALID_PWD | DATE | Y |  |  |

---

## PL_VERIFICA_LDAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LOGIN | VARCHAR2(50) | N |  |  |
| 2 | PERFIL | VARCHAR2(50) | Y |  |  |
| 3 | MSG_ERR | VARCHAR2(500) | Y |  |  |

**PK**: LOGIN

---

## PL_VERIFICA_LDAP_GRP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LOGIN | VARCHAR2(50) | N |  |  |
| 2 | GROUPS | VARCHAR2(4000) | N |  |  |

**PK**: LOGIN, GROUPS

---

