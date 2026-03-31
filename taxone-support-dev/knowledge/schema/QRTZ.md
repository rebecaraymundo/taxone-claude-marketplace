# Módulo: QRTZ (QRTZ) - 11 tabelas

## QRTZ_BLOB_TRIGGERS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | TRIGGER_NAME | VARCHAR2(200) | N |  |  |
| 3 | TRIGGER_GROUP | VARCHAR2(200) | N |  |  |
| 4 | BLOB_DATA | BLOB | Y |  |  |

**PK**: SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP

**FKs**:
- SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP → QRTZ_TRIGGERS(SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP)

---

## QRTZ_CALENDARS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | CALENDAR_NAME | VARCHAR2(200) | N |  |  |
| 3 | CALENDAR | BLOB | N |  |  |

**PK**: SCHED_NAME, CALENDAR_NAME

---

## QRTZ_CRON_TRIGGERS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | TRIGGER_NAME | VARCHAR2(200) | N |  |  |
| 3 | TRIGGER_GROUP | VARCHAR2(200) | N |  |  |
| 4 | CRON_EXPRESSION | VARCHAR2(120) | N |  |  |
| 5 | TIME_ZONE_ID | VARCHAR2(80) | Y |  |  |

**PK**: SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP

**FKs**:
- SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP → QRTZ_TRIGGERS(SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP)

---

## QRTZ_FIRED_TRIGGERS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | ENTRY_ID | VARCHAR2(95) | N |  |  |
| 3 | TRIGGER_NAME | VARCHAR2(200) | N |  |  |
| 4 | TRIGGER_GROUP | VARCHAR2(200) | N |  |  |
| 5 | INSTANCE_NAME | VARCHAR2(200) | N |  |  |
| 6 | FIRED_TIME | NUMBER(13) | N |  |  |
| 7 | PRIORITY | NUMBER(13) | N |  |  |
| 8 | STATE | VARCHAR2(16) | N |  |  |
| 9 | JOB_NAME | VARCHAR2(200) | Y |  |  |
| 10 | JOB_GROUP | VARCHAR2(200) | Y |  |  |
| 11 | IS_NONCONCURRENT | VARCHAR2(1) | Y |  |  |
| 12 | REQUESTS_RECOVERY | VARCHAR2(1) | Y |  |  |

**PK**: SCHED_NAME, ENTRY_ID

**Indexes**:
- IDX_QRTZ_FT_INST_JOB_REQ_RCVRY: (SCHED_NAME, INSTANCE_NAME, REQUESTS_RECOVERY)
- IDX_QRTZ_FT_JG: (SCHED_NAME, JOB_GROUP)
- IDX_QRTZ_FT_J_G: (SCHED_NAME, JOB_NAME, JOB_GROUP)
- IDX_QRTZ_FT_TG: (SCHED_NAME, TRIGGER_GROUP)
- IDX_QRTZ_FT_TRIG_INST_NAME: (SCHED_NAME, INSTANCE_NAME)
- IDX_QRTZ_FT_T_G: (SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP)

---

## QRTZ_JOB_DETAILS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | JOB_NAME | VARCHAR2(200) | N |  |  |
| 3 | JOB_GROUP | VARCHAR2(200) | N |  |  |
| 4 | DESCRIPTION | VARCHAR2(250) | Y |  |  |
| 5 | JOB_CLASS_NAME | VARCHAR2(250) | N |  |  |
| 6 | IS_DURABLE | VARCHAR2(1) | N |  |  |
| 7 | IS_NONCONCURRENT | VARCHAR2(1) | N |  |  |
| 8 | IS_UPDATE_DATA | VARCHAR2(1) | N |  |  |
| 9 | REQUESTS_RECOVERY | VARCHAR2(1) | N |  |  |
| 10 | JOB_DATA | BLOB | Y |  |  |

**PK**: SCHED_NAME, JOB_NAME, JOB_GROUP

**Indexes**:
- IDX_QRTZ_J_GRP: (SCHED_NAME, JOB_GROUP)
- IDX_QRTZ_J_REQ_RECOVERY: (SCHED_NAME, REQUESTS_RECOVERY)

---

## QRTZ_LOCKS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | LOCK_NAME | VARCHAR2(40) | N |  |  |

**PK**: SCHED_NAME, LOCK_NAME

---

## QRTZ_PAUSED_TRIGGER_GRPS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | TRIGGER_GROUP | VARCHAR2(200) | N |  |  |

**PK**: SCHED_NAME, TRIGGER_GROUP

---

## QRTZ_SCHEDULER_STATE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | INSTANCE_NAME | VARCHAR2(200) | N |  |  |
| 3 | LAST_CHECKIN_TIME | NUMBER(13) | N |  |  |
| 4 | CHECKIN_INTERVAL | NUMBER(13) | N |  |  |

**PK**: SCHED_NAME, INSTANCE_NAME

---

## QRTZ_SIMPLE_TRIGGERS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | TRIGGER_NAME | VARCHAR2(200) | N |  |  |
| 3 | TRIGGER_GROUP | VARCHAR2(200) | N |  |  |
| 4 | REPEAT_COUNT | NUMBER(7) | N |  |  |
| 5 | REPEAT_INTERVAL | NUMBER(12) | N |  |  |
| 6 | TIMES_TRIGGERED | NUMBER(10) | N |  |  |

**PK**: SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP

**FKs**:
- SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP → QRTZ_TRIGGERS(SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP)

---

## QRTZ_SIMPROP_TRIGGERS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | TRIGGER_NAME | VARCHAR2(200) | N |  |  |
| 3 | TRIGGER_GROUP | VARCHAR2(200) | N |  |  |
| 4 | STR_PROP_1 | VARCHAR2(512) | Y |  |  |
| 5 | STR_PROP_2 | VARCHAR2(512) | Y |  |  |
| 6 | STR_PROP_3 | VARCHAR2(512) | Y |  |  |
| 7 | INT_PROP_1 | NUMBER(10) | Y |  |  |
| 8 | INT_PROP_2 | NUMBER(10) | Y |  |  |
| 9 | LONG_PROP_1 | NUMBER(13) | Y |  |  |
| 10 | LONG_PROP_2 | NUMBER(13) | Y |  |  |
| 11 | DEC_PROP_1 | NUMBER(13,4) | Y |  |  |
| 12 | DEC_PROP_2 | NUMBER(13,4) | Y |  |  |
| 13 | BOOL_PROP_1 | VARCHAR2(1) | Y |  |  |
| 14 | BOOL_PROP_2 | VARCHAR2(1) | Y |  |  |

**PK**: SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP

**FKs**:
- SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP → QRTZ_TRIGGERS(SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP)

---

## QRTZ_TRIGGERS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 2 | TRIGGER_NAME | VARCHAR2(200) | N |  |  |
| 3 | TRIGGER_GROUP | VARCHAR2(200) | N |  |  |
| 4 | JOB_NAME | VARCHAR2(200) | N |  |  |
| 5 | JOB_GROUP | VARCHAR2(200) | N |  |  |
| 6 | DESCRIPTION | VARCHAR2(250) | Y |  |  |
| 7 | NEXT_FIRE_TIME | NUMBER(13) | Y |  |  |
| 8 | PREV_FIRE_TIME | NUMBER(13) | Y |  |  |
| 9 | PRIORITY | NUMBER(13) | Y |  |  |
| 10 | TRIGGER_STATE | VARCHAR2(16) | N |  |  |
| 11 | TRIGGER_TYPE | VARCHAR2(8) | N |  |  |
| 12 | START_TIME | NUMBER(13) | N |  |  |
| 13 | END_TIME | NUMBER(13) | Y |  |  |
| 14 | CALENDAR_NAME | VARCHAR2(200) | Y |  |  |
| 15 | MISFIRE_INSTR | NUMBER(2) | Y |  |  |
| 16 | JOB_DATA | BLOB | Y |  |  |

**PK**: SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP

**FKs**:
- SCHED_NAME, JOB_NAME, JOB_GROUP → QRTZ_JOB_DETAILS(SCHED_NAME, JOB_NAME, JOB_GROUP)

**Indexes**:
- IDX_QRTZ_T_C: (SCHED_NAME, CALENDAR_NAME)
- IDX_QRTZ_T_G: (SCHED_NAME, TRIGGER_GROUP)
- IDX_QRTZ_T_J: (SCHED_NAME, JOB_NAME, JOB_GROUP)
- IDX_QRTZ_T_JG: (SCHED_NAME, JOB_GROUP)
- IDX_QRTZ_T_NEXT_FIRE_TIME: (SCHED_NAME, NEXT_FIRE_TIME)
- IDX_QRTZ_T_NFT_MISFIRE: (SCHED_NAME, MISFIRE_INSTR, NEXT_FIRE_TIME)
- IDX_QRTZ_T_NFT_ST: (SCHED_NAME, TRIGGER_STATE, NEXT_FIRE_TIME)
- IDX_QRTZ_T_NFT_ST_MISFIRE: (SCHED_NAME, MISFIRE_INSTR, NEXT_FIRE_TIME, TRIGGER_STATE)
- IDX_QRTZ_T_NFT_ST_MISFIRE_GRP: (SCHED_NAME, MISFIRE_INSTR, NEXT_FIRE_TIME, TRIGGER_GROUP, TRIGGER_STATE)
- IDX_QRTZ_T_N_G_STATE: (SCHED_NAME, TRIGGER_GROUP, TRIGGER_STATE)
- IDX_QRTZ_T_N_STATE: (SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP, TRIGGER_STATE)
- IDX_QRTZ_T_STATE: (SCHED_NAME, TRIGGER_STATE)

---

