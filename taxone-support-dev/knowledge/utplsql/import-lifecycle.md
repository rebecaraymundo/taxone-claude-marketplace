# Import Lifecycle — SAFX → X Tables

## Overview

The TAX ONE import pipeline moves data from staging tables (SAFX) to definitive tables (X).
The import requires a **job infrastructure** (JOB_IMPORTACAO + DET_JOB_IMPORT) and produces
a **LOG_PROCESSO** for traceability. The utPLSQL utilities handle this lifecycle automatically.

## Lifecycle Steps

```
1. insere_job_importacao     → Creates JOB_IMPORTACAO record (returns NUM_JOB)
2. insere_det_job_import     → Registers which SAFX table/empresa/estab to import
3. SAF_IMPORTA_TAB_SUITE     → Executes import (creates LOG_PROCESSO internally)
4. [Assertions]              → Validate X table data and LOG_DET_PROC results
5. [Cleanup]                 → Remove test data (msaf_util_remove or DELETE)
```

## Procedure Signatures

### 1. MSAF_UTIL_INSERE.insere_job_importacao

Creates a job scheduling record. Returns `p_num_job` (OUT) used by subsequent calls.

```sql
MSAF_UTIL_INSERE.insere_job_importacao(
    p_tipo_job          => 'C',        -- 'C' = Carga
    p_status_job        => 'P',        -- 'P' = Pendente
    p_data_abertura     => SYSDATE,
    p_data_encerramento => SYSDATE,
    p_ind_ato_cotepe    => 'N',
    p_num_job           => v_num_job   -- OUT NUMBER
);
```

**Parameters:**
| Param | Type | Description | Typical Value |
|-------|------|-------------|---------------|
| p_tipo_job | CHAR | Job type: 'C'=Carga, 'E'=Exportação | 'C' |
| p_status_job | CHAR | Initial status: 'P'=Pendente | 'P' |
| p_data_abertura | DATE | Job open date | SYSDATE |
| p_data_encerramento | DATE | Job close date | SYSDATE |
| p_ind_ato_cotepe | CHAR | COTEPE indicator | 'N' |
| p_num_job | NUMBER (OUT) | Returned job ID | — |

### 2. MSAF_UTIL_INSERE.insere_det_job_import

Registers which SAFX table to import within the job. The `P_GRUPO_ARQUIVO` + `P_NUMERO_ARQUIVO`
identify the SAFX table in the system's file mapping (e.g., grupo=5, numero=1 = SAFX07).

```sql
MSAF_UTIL_INSERE.insere_det_job_import(
    P_NUM_JOB          => v_num_job,
    P_GRUPO_ARQUIVO    => 5,                                    -- File group
    P_NUMERO_ARQUIVO   => 1,                                    -- File number within group
    P_COD_EMPRESA      => '076',
    P_COD_ESTAB        => '001SP',
    P_DATA_INI         => TO_DATE('01032026','DDMMYYYY'),       -- Fiscal period start
    P_DATA_FIM         => TO_DATE('31032026','DDMMYYYY'),       -- Fiscal period end
    P_PERC_ERRO        => 100,                                  -- Error tolerance %
    P_IND_ABORTA_JOB   => 'N',
    P_STATUS           => 'P',
    P_IND_DROP_TAB     => 'N',
    P_DAT_INI_EXEC     => SYSDATE,
    P_DAT_FIM_EXEC     => SYSDATE,
    P_IND_PERIODO      => 'N',
    P_IND_SOBREPOR_REG => 'S',                                 -- Overwrite existing
    P_IND_LOG_X2013    => 'N',
    P_IND_VALID_X2013  => 'N'
);
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| P_NUM_JOB | NUMBER | required | Job ID from step 1 |
| P_GRUPO_ARQUIVO | NUMBER | required | File group (see table below) |
| P_NUMERO_ARQUIVO | NUMBER | required | File number in group |
| P_COD_EMPRESA | VARCHAR2 | NULL | Company code |
| P_COD_ESTAB | VARCHAR2 | NULL | Establishment code |
| P_DATA_INI | DATE | NULL | Fiscal period start |
| P_DATA_FIM | DATE | NULL | Fiscal period end |
| P_PERC_ERRO | NUMBER | NULL | Error tolerance (0-100) |
| P_IND_ABORTA_JOB | CHAR | NULL | Abort on error? |
| P_STATUS | CHAR | NULL | 'P'=Pendente |
| P_IND_DROP_TAB | CHAR | NULL | Drop staging after import? |
| P_DAT_INI_EXEC | DATE | NULL | Execution start |
| P_DAT_FIM_EXEC | DATE | NULL | Execution end |
| P_IND_PERIODO | CHAR | NULL | Period filter? |
| P_IND_SOBREPOR_REG | CHAR | NULL | Overwrite existing X records? |
| P_IND_LOG_X2013 | CHAR | NULL | Log X2013? |
| P_IND_VALID_X2013 | CHAR | NULL | Validate X2013? |

### 3. MSAF_UTIL.SAF_IMPORTA_TAB_SUITE

Wrapper that calls `SAF_IMPORTA_TAB` internally, creating LOG_PROCESSO and executing
all `SAF_IMP_X{NN}` procedures registered in the job.

```sql
MSAF_UTIL.SAF_IMPORTA_TAB_SUITE(
    P_NUM_JOB  => v_num_job,
    P_USUARIO  => 'test_user',
    P_PROC_INI => v_proc_ini,     -- OUT NUMBER (LOG_PROCESSO start)
    P_PROC_FIM => v_proc_fim,     -- OUT NUMBER (LOG_PROCESSO end)
    P_MENS_ERR => v_mens_err      -- OUT NUMBER (error count)
);
```

**What it does internally:**
1. Creates LOG_PROCESSO record
2. Creates LOG_DET_PROC entries
3. For each DET_JOB_IMPORT: calls `SAF_IMP_X{NN}` (e.g., SAF_IMP_X07, SAF_IMP_X3007)
4. Each `SAF_IMP_X{NN}` calls `OL_IMP_X{NN}` row-by-row
5. `OL_IMP_X{NN}` validates parent dependencies and inserts into X table

## GRUPO_ARQUIVO / NUMERO_ARQUIVO Mapping

The combination identifies which SAFX table to import. Common values from ut_job_safx* tests:

| GRUPO | NUMERO | SAFX Table | Notes |
|-------|--------|------------|-------|
| 5 | 1 | SAFX07 | Documento Fiscal (header) |
| 5 | 2 | SAFX08 | Item Documento Fiscal |
| 5 | 3 | SAFX09 | Serviço Documento Fiscal |
| 5 | ... | SAFX{NN} | Other document-related tables |

**To discover the correct GRUPO/NUMERO for a SAFX table:**
```sql
SELECT GRUPO_ARQUIVO, NUMERO_ARQUIVO, DESCRICAO
  FROM ARQUIVO
 WHERE DESCRICAO LIKE 'SAFX%'
 ORDER BY GRUPO_ARQUIVO, NUMERO_ARQUIVO;
```

## Complete Example: Import Test (ut_test_001 pattern)

```sql
CREATE OR REPLACE PACKAGE BODY ut_test_example IS

  v_num_job      NUMBER;
  v_proc_ini     NUMBER;
  v_proc_fim     NUMBER;
  v_mens_err     NUMBER;

  PROCEDURE ut_setup IS
  BEGIN
    -- Insert test data into SAFX staging table
    INSERT INTO SAFX07 (COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, ...)
    VALUES ('076', '01', '9', '1', ...);
    COMMIT;
  END ut_setup;

  PROCEDURE ut_teardown IS
  BEGIN
    -- Clean SAFX staging
    DELETE SAFX07 WHERE COD_EMPRESA = '076' AND COD_ESTAB = '01';
    -- Clean import scheduling
    DELETE HIST_EXPORT WHERE GRUPO_ARQUIVO = 5 AND NUMERO_ARQUIVO = 1;
    DELETE JOB_EXP_TAB WHERE GRUPO_ARQUIVO = 5 AND NUMERO_ARQUIVO = 1;
    COMMIT;
  END ut_teardown;

  PROCEDURE ut_test_001 IS
  BEGIN
    -- Step 1: Create job
    MSAF_UTIL_INSERE.insere_job_importacao(
        p_tipo_job => 'C', p_status_job => 'P',
        p_data_abertura => SYSDATE, p_data_encerramento => SYSDATE,
        p_ind_ato_cotepe => 'N', p_num_job => v_num_job);

    -- Step 2: Register SAFX table in job
    MSAF_UTIL_INSERE.insere_det_job_import(
        P_NUM_JOB => v_num_job, P_GRUPO_ARQUIVO => 5, P_NUMERO_ARQUIVO => 1,
        P_COD_EMPRESA => '076', P_COD_ESTAB => '01',
        P_DATA_INI => TO_DATE('01032026','DDMMYYYY'),
        P_DATA_FIM => TO_DATE('31032026','DDMMYYYY'),
        P_PERC_ERRO => 100, P_IND_ABORTA_JOB => 'N',
        P_STATUS => 'P', P_IND_DROP_TAB => 'N',
        P_DAT_INI_EXEC => SYSDATE, P_DAT_FIM_EXEC => SYSDATE,
        P_IND_PERIODO => 'N', P_IND_SOBREPOR_REG => 'S',
        P_IND_LOG_X2013 => 'N', P_IND_VALID_X2013 => 'N');

    -- Step 3: Execute import
    MSAF_UTIL.SAF_IMPORTA_TAB_SUITE(
        P_NUM_JOB => v_num_job, P_USUARIO => 'test_user',
        P_PROC_INI => v_proc_ini, P_PROC_FIM => v_proc_fim,
        P_MENS_ERR => v_mens_err);

    -- Step 4: Validate import log
    MSAF_UTIL_TESTA.testa_log_det_proc(
        p_num_processo => v_proc_ini,
        p_arq_result_esperado => 'expected_log.txt',
        p_arq_result_obtido   => 'obtained_log.txt',
        p_dir_result_esperado => '/path/esperado/',
        p_dir_result_obtido   => '/path/obtido/');

    -- Step 5: Validate X table data
    -- Use MSAF_UTIL_TESTA.testa_x{NN}_* or utAssert.eq for custom checks
    COMMIT;
  END ut_test_001;

END ut_test_example;
```

## Batch Import Alternative (SAF_IMPORTA_BAT_SUITE)

For testing Importação Batch (file-based import), use a different lifecycle:

```sql
-- 1. Create batch programming
MSAF_UTIL_INSERE.insere_ibt_prog(
    P_COD_EMPRESA => '076', P_COD_PROG => v_cod_prog,  -- OUT
    P_DSC_PROG => 'Batch import SAFX07', P_DSC_EXT_ARQ => 'TXT',
    P_IND_PERIOD => 1, P_DT_INI_EVENT => SYSDATE,
    P_DSC_DIRETORIO => '/path/to/files/', P_IND_LIM_PER => 'N',
    P_IND_ORD_IMP => 1, P_IND_ATO_COTEPE => 'N', ...);

-- 2. Register table control
MSAF_UTIL_INSERE.insere_ibt_controle(
    P_COD_PROG => v_cod_prog, P_COD_EMPRESA => '076', P_COD_ESTAB => '001',
    P_COD_TABELA => 'SAFX07', P_IND_UTILIZA_TAB => 'A',
    P_IND_DROP_TAB => 'N', P_IND_SOBREPOR_REG => 'S', ...);

-- 3. Execute batch import
MSAF_UTIL.SAF_IMPORTA_BAT_SUITE(
    p_cod_empresa => '076', p_cod_prog => v_cod_prog,
    p_data_proc => SYSDATE, p_ind_grava => 'N',
    p_ind_data => 'N', p_grava_log => 'N',
    p_dsc_diretorio => NULL, p_mens_err => v_mens_err);
```

## Parent Table Dependencies

Some X tables require parent records to exist. Key dependencies:

| X Table | Parent Required | Validated In |
|---------|----------------|--------------|
| X3007_DOCTO_FISCAL_RT | X07_DOCTO_FISCAL + X04_PESSOA_FIS_JUR + X2005_TIPO_DOCTO | OL_IMP_X3007 L437-460 |
| X08_ITEM_DOCTO_FISCAL | X07_DOCTO_FISCAL | OL_IMP_X08 |
| X09_SERVICO_DOCFIS | X07_DOCTO_FISCAL | OL_IMP_X09 |

**Implication for test data**: When testing import of child tables (e.g., SAFX3007), you must
first import parent tables (SAFX07) so that X07_DOCTO_FISCAL records exist. The job can
include multiple SAFX tables in the same run via multiple `insere_det_job_import` calls.

## Cleanup After Tests

Cleanup order matters due to FK constraints:

1. Delete child X records (X3007, X08, X09, etc.)
2. Delete parent X records (X07)
3. Delete LOG_DET_PROC / LOG_PROCESSO
4. Delete DET_JOB_IMPORT / JOB_IMPORTACAO
5. Delete SAFX staging data
6. Delete HIST_EXPORT / JOB_EXP_TAB (if batch)

Use `MSAF_UTIL_REMOVE.remove_*` procedures when available — they handle FK order internally.

## Source References

- `msaf_util.pck` L7700-7711: SAF_IMPORTA_TAB_SUITE
- `msaf_util_insere.pck` L2023-2028: insere_job_importacao
- `msaf_util_insere.pck` L304-319: insere_det_job_import
- `ut_job_safx0.pck` L253-307: ut_test_001 (canonical import test)
- `ut_job_safx0.pck` L313-368: ut_test_002 (batch import test)
