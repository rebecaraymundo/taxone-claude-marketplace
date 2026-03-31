# Módulo: SPED (SPED) - 37 tabelas

## SPED_CONTADORES_WORK
**Comment**: Tabela de contadores I200/I250 para processamento paralelo - evita COUNT na lib_proc_saida

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  | ID do processo de execucao |
| 2 | CHUNK_ID | NUMBER | N |  | Identificador do chunk processado |
| 3 | DATA_INI | DATE | Y |  | Data inicial do chunk |
| 4 | DATA_FIM | DATE | Y |  | Data final do chunk |
| 5 | CNT_I200 | NUMBER | Y | 0 | Quantidade de registros I200 gerados no chunk |
| 6 | CNT_I250 | NUMBER | Y | 0 | Quantidade de registros I250 gerados no chunk |
| 7 | DATA_INSERT | DATE | Y | SYSDATE | Data de insercao do registro |

**Indexes**:
- IDX_SPED_CONTADORES_PROC: (PROC_ID)

---

## SPED_CONTAS_EMP_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_CONS | DATE | N |  |  |
| 4 | DATA_FIM_CONS | DATE | N |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | N |  |  |
| 6 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 7 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 8 | COD_CONTA_CONS | VARCHAR2(70) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI_CONS, DATA_FIM_CONS, COD_EMP_PART, GRUPO_CONTA, COD_CONTA

---

## SPED_CONTAS_REF
**Comment**: Tabela de Cadastro do Plano de Contas Referencial

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 2 | COD_CONTA_REF | VARCHAR2(30) | Y |  |  |
| 3 | VERSAO | VARCHAR2(6) | Y |  |  |
| 4 | COD_ENTIDADE_RESP | VARCHAR2(6) | Y |  | Entidade Responsável relacionada na view SPED_ENTIDADE_RESP_V |
| 5 | DESCRICAO | VARCHAR2(300) | Y |  |  |
| 6 | NIVEL | VARCHAR2(5) | Y |  |  |
| 7 | IND_CONTA | CHAR(1) | Y |  | S - sintética; A - analítica |
| 8 | IND_TIPO_CONTA | CHAR(1) | Y |  | 1 - Balanço Patrimonial; 2 - Demonstrativo de Resultado |
| 9 | DAT_VALIDADE_INI | DATE | Y |  |  |
| 10 | DAT_VALIDADE_FIM | DATE | Y |  |  |
| 11 | TITULOS | VARCHAR2(26) | Y |  |  |
| 12 | IND_CLASSIF_CONTA | VARCHAR2(1) | Y |  | Classificacao da Conta:  F - Fiscal; S - Societario; A - Ambas. |

**PK**: IDENT_CONTA_REF

**Indexes**:
- UK_SPED_CONTAS_REF (UNIQUE): (COD_CONTA_REF, VERSAO, COD_ENTIDADE_RESP)

---

## SPED_CONTAS_REF_CCUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 2 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 3 | IDENT_CUSTO | NUMBER(12) | N |  |  |

**PK**: IDENT_CONTA, IDENT_CONTA_REF, IDENT_CUSTO

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTA_REF → SPED_CONTAS_REF(IDENT_CONTA_REF)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)

**Indexes**:
- IX_SPED_CONTAS_REF_CCUSTO: (IDENT_CONTA, IDENT_CONTA_REF)
- IX_SPED_CONTAS_REF_CTA: (IDENT_CONTA)

---

## SPED_CONTAS_REF_EMP
**Comment**: Tabela de definição das Contas do Plano de Contas pertencentes ao Código de Aglutinação

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 2 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 3 | EXPRESSAO_CUSTO | VARCHAR2(2000) | Y |  |  |
| 4 | GRUPO_CUSTO | VARCHAR2(9) | Y |  |  |

**PK**: IDENT_CONTA, IDENT_CONTA_REF

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTA_REF → SPED_CONTAS_REF(IDENT_CONTA_REF)

**Indexes**:
- IX_SPED_CONTAS_REF_EMP: (IDENT_CONTA_REF)
- IX_SPED_CTA_REF_EMP_CTA: (IDENT_CONTA)

---

## SPED_CONT_DEM_CONTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | DESCRICAO | VARCHAR2(70) | Y |  |  |
| 5 | DATA_SALDO | DATE | N |  |  |
| 6 | IND_BALANCO_DRE | CHAR(1) | N |  |  |
| 7 | VLR_SALDO_CALC | NUMBER(19,2) | Y |  |  |
| 8 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 9 | VLR_SALDO_CALC_INI | NUMBER(19,2) | Y |  |  |
| 10 | IND_DEB_CRED_INI | CHAR(1) | Y |  |  |
| 11 | VLR_SALDO_CALC_MF | NUMBER(19,2) | Y |  |  |
| 12 | IND_DEB_CRED_MF | CHAR(1) | Y |  |  |
| 13 | VLR_SALDO_CALC_INI_MF | NUMBER(19,2) | Y |  |  |
| 14 | IND_DEB_CRED_INI_MF | CHAR(1) | Y |  |  |
| 15 | ORDEM | NUMBER(4) | Y |  |  |
| 16 | NIVEL | NUMBER(4) | Y |  |  |
| 17 | PROC_ID | NUMBER | Y |  |  |
| 18 | IND_TIP | CHAR(1) | Y |  |  |
| 19 | NOTAS_EXP_REF | VARCHAR2(30) | Y |  |  |
| 20 | IND_COD_AGL | CHAR(1) | Y |  |  |
| 21 | COD_AGL_SUP | VARCHAR2(70) | Y |  |  |
| 22 | IND_NATUREZA | CHAR(1) | Y |  |  |
| 23 | NUM_REFERENCIA | VARCHAR2(12) | Y |  |  |
| 24 | IND_GP_DRE | CHAR(1) | Y |  |  |
| 25 | DATA_INI_ECD | DATE | Y |  |  |
| 26 | DATA_FIM_ECD | DATE | Y |  |  |
| 27 | IND_CONFERENCIA | CHAR(1) | N | 'N' |  |
| 28 | DATA_SALDO_INI | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, DATA_SALDO, IND_BALANCO_DRE, IND_CONFERENCIA, DATA_SALDO_INI

---

## SPED_CONT_DEM_CONTAB_HIST_FAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | IND_BALANCO_DRE | CHAR(1) | N |  |  |
| 6 | COD_HIST_FAT | VARCHAR2(6) | N |  |  |
| 7 | DESC_FAT | VARCHAR2(100) | Y |  |  |
| 8 | VL_FAT_CONT | NUMBER(19,2) | Y |  |  |
| 9 | IND_DC_FAT | CHAR(1) | Y |  |  |
| 10 | VL_FAT_CONT_MF | NUMBER(19,2) | Y |  |  |
| 11 | IND_DC_FAT_MF | CHAR(1) | Y |  |  |
| 12 | IND_CONFERENCIA | CHAR(1) | N | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, DATA_SALDO, IND_BALANCO_DRE, IND_CONFERENCIA, COD_HIST_FAT

---

## SPED_CONT_J100_J150

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | VLR_SALDO_CALC | NUMBER(19,2) | Y |  |  |
| 6 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_CALC_INI | NUMBER(19,2) | Y |  |  |
| 8 | IND_DEB_CRED_INI | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, DATA_SALDO

---

## SPED_DADOS_AUDITOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NOME_AUDITOR | VARCHAR2(250) | Y |  |  |
| 4 | REGISTRO_CVM | VARCHAR2(250) | N |  |  |
| 5 | CPF_CNPJ_AUDITOR | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, REGISTRO_CVM

---

## SPED_DADOS_DEM_CONTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ID_TP_DEMONST | NUMBER(12) | N |  |  |
| 4 | IND_DEMONST | CHAR(1) | N |  | Pode conter os valores <1> ou <2> |
| 5 | DSC_CABEC_DEMONST | VARCHAR2(1000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ID_TP_DEMONST

---

## SPED_DADOS_DEM_CONTAB_ARQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ID_TP_DEMONST | NUMBER(12) | N |  |  |
| 4 | DSC_DIRETORIO | VARCHAR2(500) | N |  |  |
| 5 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 6 | PERIODO | NUMBER(2) | Y |  |  |
| 7 | ANO | NUMBER(4) | Y |  |  |
| 8 | STATUS_BD | CHAR(1) | Y |  |  |
| 9 | USUARIO | VARCHAR2(100) | Y |  |  |
| 10 | TPO_DOCTO | VARCHAR2(3) | Y |  |  |
| 11 | DSC_RTF | VARCHAR2(255) | Y |  |  |
| 12 | IND_J800_J801 | CHAR(1) | Y |  |  |
| 13 | COD_MOT_SUBST | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ID_TP_DEMONST, DSC_DIRETORIO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ID_TP_DEMONST → SPED_DADOS_DEM_CONTAB(COD_EMPRESA, COD_ESTAB, ID_TP_DEMONST)

---

## SPED_DADOS_DEM_CONTAB_ARQ_DET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ID_TP_DEMONST | NUMBER(12) | N |  |  |
| 4 | DSC_DIRETORIO | VARCHAR2(500) | N |  |  |
| 5 | ORD_LINHA | NUMBER(12) | N |  |  |
| 6 | LINHA | VARCHAR2(2000) | Y |  |  |
| 7 | COD_MOT_SUBST | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ID_TP_DEMONST, DSC_DIRETORIO, ORD_LINHA

---

## SPED_DADOS_DEM_CONTAB_ARQ_DT1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ID_TP_DEMONST | NUMBER(12) | N |  |  |
| 4 | DSC_DIRETORIO | VARCHAR2(500) | N |  |  |
| 5 | COD_MOT_SUBST | VARCHAR2(3) | Y |  |  |
| 6 | ARQUIVO | BLOB | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ID_TP_DEMONST, DSC_DIRETORIO

---

## SPED_DADOS_INI
**Comment**: Tabela de Paramentrização dos Dados Iniciais do Sped Contábil

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ENTIDADE_RESP | VARCHAR2(6) | Y |  | Entidade Responsável relacionada na view SPED_ENTIDADE_RESP_V |
| 4 | IND_GERA_PLANO_CONTAS | CHAR(1) | Y |  | C - completo; M - somente as contas movimentadas no período da geração |
| 5 | IND_GERA_CCUSTO | CHAR(1) | Y |  | S - quando não omitir centro de custo; N - quando omitir centro de custo |
| 6 | DSC_DIRETORIO | VARCHAR2(500) | Y |  |  |
| 7 | TITULO_B | CHAR(1) | Y |  |  |
| 8 | TITULO_D | CHAR(1) | Y |  |  |
| 9 | TITULO_I | CHAR(1) | Y |  |  |
| 10 | TITULO_F | CHAR(1) | Y |  |  |
| 11 | TITULO_A | CHAR(1) | Y |  |  |
| 12 | TITULO_C | CHAR(1) | Y |  |  |
| 13 | TITULO_T | CHAR(1) | Y |  |  |
| 14 | TITULO_S | CHAR(1) | Y |  |  |
| 15 | TITULO_E | CHAR(1) | Y |  |  |
| 16 | TITULO_R | CHAR(1) | Y |  |  |
| 17 | TITULO_L | CHAR(1) | Y |  |  |
| 18 | TITULO_M | CHAR(1) | Y |  |  |
| 19 | TITULO_N | CHAR(1) | Y |  |  |
| 20 | TITULO_Z | CHAR(1) | Y |  |  |
| 21 | TITULO_U | CHAR(1) | Y |  |  |
| 22 | TITULO_O | CHAR(1) | Y |  |  |
| 23 | TITULO_H | CHAR(1) | Y |  |  |
| 24 | TITULO_W | CHAR(1) | Y |  |  |
| 25 | TITULO_K | CHAR(1) | Y |  |  |
| 26 | TITULO_J | CHAR(1) | Y |  |  |
| 27 | TITULO_P | CHAR(1) | Y |  |  |
| 28 | DT_EX_SOCIAL | VARCHAR2(4) | Y |  |  |
| 29 | IND_EMP_GRD_PRT | CHAR(1) | Y |  |  |
| 30 | IND_GERA_SAFX169 | CHAR(1) | Y | 'N' |  |
| 31 | IND_TIPO_ECD | CHAR(1) | Y | '0' |  |
| 32 | IND_MOEDA_FUNC | CHAR(1) | Y | 'N' |  |
| 33 | IND_MOEDA_FUNC_BP_DRE | CHAR(1) | Y | 'N' | Gerar Balanco Patrimonial e DRE com base nos valores de Moeda Funcional |
| 34 | IND_ESCRIT_CONT_CONS | CHAR(1) | Y |  |  |
| 35 | IND_GERAR_CONT_RES | CHAR(1) | Y | 'N' |  |
| 36 | IND_GERA_COD_PART | CHAR(1) | Y | 'N' |  |
| 37 | IND_ORDENA_I050_IND_NAT | CHAR(1) | Y | 'N' |  |
| 38 | IND_CONTA_CCUSTO | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SPED_DADOS_SIGNATARIO
**Comment**: Tabela de Paramentrização dos Signatários - tela de Dados Iniciais do Sped Contábil

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 4 | COD_QUALIF_SPED | VARCHAR2(3) | Y |  | Código de qualificação do signatário, conforme tabela do Sped na view SPED_QUALIF_SIGNATARIO_V |
| 5 | IND_OBRIG | VARCHAR2(5) | N |  | Identificador da Obrigação a qual o signatário faz parte (ECD; FCONT) |
| 6 | IND_RESP_LEGAL | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_RESPONSAVEL, IND_OBRIG

**FKs**:
- COD_EMPRESA, COD_ESTAB → SPED_DADOS_INI(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## SPED_GERA_I020

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(12) | N |  |  |
| 2 | COD_LAYOUT | VARCHAR2(6) | Y |  |  |
| 3 | COD_PERFIL | VARCHAR2(3) | Y |  |  |
| 4 | COD_REG | VARCHAR2(4) | Y |  | Campo de codigo do registro. Registros a serem considerados: I050 - I200 - I250 |
| 5 | SEQ_CAMPO_ADD | NUMBER(3) | Y |  | Campo de sequencial do campo adicional |
| 6 | NOM_CAMPO_ADD | VARCHAR2(255) | Y |  | Campo contendo o nome do campo obrigatorio do registro I020 |
| 7 | DSC_CAMPO_ADD | VARCHAR2(255) | Y |  | Descricao do conteudo do campo obrigatorio do registro I020 |
| 8 | CAMPO_ADD_ORIG | VARCHAR2(255) | Y |  | Nome do campo origem da informacao |
| 9 | FORM_CAMPO_ADD | CHAR(1) | Y |  | Formato do campo obrigatorio do registro I020 |

**PK**: ID

**FKs**:
- COD_LAYOUT, COD_PERFIL → COTEPE_PERFIL(COD_LAYOUT, COD_PERFIL)

**Indexes**:
- UK_SPED_GERA_I020 (UNIQUE): (COD_LAYOUT, COD_PERFIL, COD_REG, SEQ_CAMPO_ADD)

---

## SPED_GERA_I310_I355
**Comment**: Tabela Temporária p/ auxliar a geração do I310 e I355

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_LANCTO | DATE | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 3 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 4 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 5 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ENCERRAMENTO | NUMBER(17,2) | Y |  |  |

**PK**: DATA_LANCTO, COD_CONTA, COD_CUSTO

---

## SPED_HIST_I075_WORK
**Comment**: Tabela de trabalho para registro I075 do SPED Contabil - Historico Padrao

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  | ID do processo de execucao |
| 2 | GRUPO_HISTPADRAO | VARCHAR2(9) | N |  | Grupo do historico padrao |
| 3 | COD_HISTPADRAO | VARCHAR2(20) | N |  | Codigo do historico padrao |

**Indexes**:
- IDX_SPED_HIST_I075_PROC: (PROC_ID)
- UK_SPED_HIST_I075_WORK (UNIQUE): (PROC_ID, GRUPO_HISTPADRAO, COD_HISTPADRAO)

---

## SPED_I050_WORK
**Comment**: Tabela de trabalho para registro I050 do SPED Contabil - Plano de Contas

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  | ID do processo de execucao |
| 2 | GRUPO_CONTA | VARCHAR2(9) | N |  | Grupo da conta contabil |
| 3 | COD_CONTA | VARCHAR2(70) | N |  | Codigo da conta contabil |

**Indexes**:
- IDX_SPED_I050_PROC: (PROC_ID)
- UK_SPED_I050_WORK (UNIQUE): (PROC_ID, GRUPO_CONTA, COD_CONTA)

---

## SPED_I100_WORK
**Comment**: Tabela de trabalho para registro I100 do SPED Contabil - Particionada por dia

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  | ID do processo de execucao |
| 2 | DATA_CHUNK | DATE | N |  | Data do chunk sendo processado (coluna de particionamento) |
| 3 | GRUPO_CUSTO | VARCHAR2(9) | N |  | Grupo do centro de custo |
| 4 | COD_CUSTO | VARCHAR2(50) | N |  | Codigo do centro de custo |

**Indexes**:
- IDX_SPED_I100_WORK_PROC: (PROC_ID, GRUPO_CUSTO, COD_CUSTO)

---

## SPED_I310_I355_WORK
**Comment**: Tabela de trabalho para registros I310/I355 do SPED Contabil - Particionada por dia

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  | ID do processo de execucao |
| 2 | DATA_LANCTO | DATE | N |  | Data do lancamento (coluna de particionamento) |
| 3 | COD_CONTA | VARCHAR2(40) | N |  | Codigo da conta contabil |
| 4 | GRUPO_CONTA | VARCHAR2(9) | N |  | Grupo da conta contabil |
| 5 | COD_CUSTO | VARCHAR2(50) | Y |  | Codigo do centro de custo |
| 6 | GRUPO_CUSTO | VARCHAR2(9) | Y |  | Grupo do centro de custo |
| 7 | VLR_TOT_DEB | NUMBER(18,2) | Y | 0 | Valor total de debitos |
| 8 | VLR_TOT_CRED | NUMBER(18,2) | Y | 0 | Valor total de creditos |
| 9 | VLR_ENCERRAMENTO | NUMBER(18,2) | Y |  | Valor de encerramento |
| 10 | VLR_TOT_DEB_MF | NUMBER(18,2) | Y | 0 | Valor total de debitos MF |
| 11 | VLR_TOT_CRED_MF | NUMBER(18,2) | Y | 0 | Valor total de creditos MF |
| 12 | VLR_ENCERRAMENTO_MF | NUMBER(18,2) | Y |  | Valor de encerramento MF |

**Indexes**:
- IDX_SPED_I310_I355_WORK_PROC: (PROC_ID, DATA_LANCTO, COD_CONTA, GRUPO_CONTA, COD_CUSTO, GRUPO_CUSTO)

---

## SPED_LIVRO_AUX
**Comment**: Tabela de cadastro dos livros auxiliares ao diário

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |
| 2 | DSC_LIVRO_AUX | VARCHAR2(100) | Y |  |  |
| 3 | COD_LAYOUT | VARCHAR2(6) | Y |  |  |
| 4 | COD_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | IND_TP_ESCRIT | CHAR(1) | Y |  |  |
| 6 | DSC_LIVRO_SPED | VARCHAR2(100) | Y |  |  |
| 7 | COD_HASH_AUX | VARCHAR2(100) | Y |  | Campo foi transportado para a tabela SPED_LIVRO_AUX_HIST (OS2338_IB/R31) |

**PK**: COD_LIVRO_AUX

**FKs**:
- COD_LAYOUT, COD_LIVRO → COTEPE_PERFIL(COD_LAYOUT, COD_PERFIL)

---

## SPED_LIVRO_AUX_CONTAS
**Comment**: Tabela de cadastro da contas para os livros auxiliares ao diário

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |
| 2 | IDENT_CONTA | NUMBER(12) | N |  |  |

**PK**: COD_LIVRO_AUX, IDENT_CONTA

**FKs**:
- COD_LIVRO_AUX → SPED_LIVRO_AUX(COD_LIVRO_AUX)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_SPED_LIVRO_AUX_CTA: (IDENT_CONTA)

---

## SPED_LIVRO_AUX_CTR
**Comment**: Tabela de cadastro do Controle das Obrigações dos livros auxiliares

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 4 | COD_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |
| 6 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 7 | NUM_ORD_ATU | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO, COD_LIVRO_AUX

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO → SPED_LIVRO_OFIC_CTR(COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO)
- COD_LIVRO_AUX → SPED_LIVRO_AUX(COD_LIVRO_AUX)

---

## SPED_LIVRO_AUX_HIST
**Comment**: Tabela do Histórico dos livros auxiliares - Controle das Obrigações

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 4 | COD_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |
| 6 | DT_GERACAO | DATE | N |  |  |
| 7 | DT_APUR_INI | DATE | Y |  |  |
| 8 | DT_APUR_FIM | DATE | Y |  |  |
| 9 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 10 | NUM_ORD_APUR | VARCHAR2(8) | Y |  |  |
| 11 | COD_HASH_AUT | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO, COD_LIVRO_AUX, DT_GERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO, COD_LIVRO_AUX → SPED_LIVRO_AUX_CTR(COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO, COD_LIVRO_AUX)

---

## SPED_LIVRO_NUMERO_ORD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 4 | COD_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |
| 6 | PERIODO_INI | DATE | N |  |  |
| 7 | PERIODO_FIM | DATE | N |  |  |
| 8 | NUM_ORD_ATU | VARCHAR2(8) | N |  |  |
| 9 | IND_DEM_CONTAB | CHAR(1) | Y |  |  |
| 10 | DATA_DEM_CONTAB | DATE | Y |  |  |
| 11 | IND_BALANCO | CHAR(1) | Y |  |  |
| 12 | IND_DRE | CHAR(1) | Y |  |  |
| 13 | IND_DLPA | CHAR(1) | Y |  |  |
| 14 | IND_DMPL | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO, COD_LIVRO_AUX, PERIODO_INI, PERIODO_FIM, NUM_ORD_ATU

---

## SPED_LIVRO_OFIC_CTR
**Comment**: Tabela de cadastro do Controle das Obrigações dos livros oficiais

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 4 | COD_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 6 | NUM_ORD_ATU | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO

**FKs**:
- COD_LAYOUT, COD_LIVRO → COTEPE_PERFIL(COD_LAYOUT, COD_PERFIL)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## SPED_LIVRO_OFIC_HIST
**Comment**: Tabela do Histórico dos livros oficiais - Controle das Obrigações

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 4 | COD_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DT_GERACAO | DATE | N |  |  |
| 6 | DT_APUR_INI | DATE | Y |  |  |
| 7 | DT_APUR_FIM | DATE | Y |  |  |
| 8 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 9 | NUM_ORD_APUR | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO, DT_GERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO → SPED_LIVRO_OFIC_CTR(COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO)

---

## SPED_LIVRO_RAZAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TAM_FONTE | NUMBER(2) | N |  |  |
| 4 | IND_TOT_GERAL | CHAR(1) | N |  |  |
| 5 | NUM_DEC | NUMBER(2) | N |  |  |
| 6 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LIVRO_AUX

**FKs**:
- COD_LIVRO_AUX → SPED_LIVRO_AUX(COD_LIVRO_AUX)

---

## SPED_LIVRO_RAZAO_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NOM_CAMPO | VARCHAR2(50) | N |  |  |
| 4 | ORD_CAMPO | NUMBER(2) | N |  |  |
| 5 | TP_CAMPO | CHAR(1) | N |  | Pode conter os seguintes valores <C> ou <N> |
| 6 | TAM_CAMPO | NUMBER(2) | N |  |  |
| 7 | LRG_CAMPO | NUMBER(2) | N |  |  |
| 8 | TIPO_IND | CHAR(1) | N |  | pode contar os seguintes valores <C>omum, <T>otalizador, <A>grupador  |
| 9 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NOM_CAMPO, ORD_CAMPO, COD_LIVRO_AUX

**FKs**:
- COD_LIVRO_AUX → SPED_LIVRO_AUX(COD_LIVRO_AUX)

---

## SPED_LIVRO_RAZAO_REL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_PER | VARCHAR2(2) | N |  |  |
| 4 | ANO_PER | VARCHAR2(4) | N |  |  |
| 5 | LINHA | NUMBER(12) | N |  |  |
| 6 | TEXTO | VARCHAR2(4000) | N |  |  |
| 7 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_PER, ANO_PER, LINHA, COD_LIVRO_AUX

**FKs**:
- COD_LIVRO_AUX → SPED_LIVRO_AUX(COD_LIVRO_AUX)

---

## SPED_PAR_AUX_SUBCONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |
| 4 | COD_LAYOUT_ECD | VARCHAR2(3) | N |  |  |
| 5 | COD_ITEM | VARCHAR2(3) | N |  |  |
| 6 | IND_TRATAMENTO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LIVRO_AUX, COD_LAYOUT_ECD, COD_ITEM

---

## SPED_PAR_REL
**Comment**: Tabela de Parametrizacao dos estabelecimentos a serem considerados nos Relatorios do Balanco Patrimonial e da Demonstracao de Resultado.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_SINTETICO | CHAR(1) | Y |  |  |
| 4 | IND_ANALITICO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## SPED_PAR_REL_AGLUT
**Comment**: Tabela de Parametrizacao dos Codigos de Aglutinacao a serem considerados nos Relatorios do Balanco Patrimonial e da Demonstracao de Resultado.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | IND_UTIL_AGLUT | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT → X2102_CONTAS_AGLUT(COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT)
- COD_EMPRESA, COD_ESTAB → SPED_PAR_REL(COD_EMPRESA, COD_ESTAB)

---

## SPED_PFJ_0150_WORK
**Comment**: Tabela de trabalho para registro 0150 do SPED Contabil - Pessoas Fisicas/Juridicas

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  | ID do processo de execucao |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  | Grupo da pessoa fisica/juridica |
| 3 | IND_FIS_JUR | VARCHAR2(1) | N |  | Indicador pessoa fisica (F) ou juridica (J) |
| 4 | COD_FIS_JUR | VARCHAR2(20) | N |  | Codigo da pessoa fisica/juridica |

**Indexes**:
- IDX_SPED_PFJ_0150_PROC: (PROC_ID)
- UK_SPED_PFJ_0150_WORK (UNIQUE): (PROC_ID, IND_FIS_JUR, COD_FIS_JUR)

---

## SPED_SUBCONTAS_CORRELATAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_CONTAS | VARCHAR2(9) | N |  | Grupo das Contas (Relacionamento Tabelas Grupos) |
| 2 | COD_CONTA | VARCHAR2(70) | N |  | Codigo da Conta Principal (SAFX2002) |
| 3 | COD_IDT | VARCHAR2(6) | Y |  | Grupo da Conta-SubConta (SPED Contabil) |
| 4 | COD_CONTA_SUB | VARCHAR2(70) | N |  | Codigo da Subconta correlta (SAFX2002) |
| 5 | COD_NAT_SUBCONTAS | VARCHAR2(2) | Y |  | Natureza da Subconta (SPED Contabil) |

**PK**: GRUPO_CONTAS, COD_CONTA, COD_CONTA_SUB

---

## SPED_TERMOS_LIVRO
**Comment**: Tabela de cadastro do termo de abertura e encerramento dos livros contábeis do SPED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_LIVRO | VARCHAR2(3) | N |  |  |
| 3 | TERMO_ABERTURA | VARCHAR2(4000) | Y |  |  |
| 4 | TERMO_ENCERRA | VARCHAR2(4000) | Y |  |  |
| 5 | DT_ATO_CONSTITUTIVO | DATE | Y |  |  |
| 6 | DT_ATO_CONVERSAO | DATE | Y |  |  |
| 7 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 8 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 9 | NOM_AUDITOR | VARCHAR2(100) | Y |  |  |
| 10 | COD_CVM_AUDITOR | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LAYOUT, COD_LIVRO

**FKs**:
- COD_LAYOUT, COD_LIVRO → COTEPE_PERFIL(COD_LAYOUT, COD_PERFIL)

---

