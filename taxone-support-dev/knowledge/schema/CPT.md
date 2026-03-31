# Módulo: CPT (CPT) - 35 tabelas

## CPT_AP_CENTRAL_CI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPR_CENTRAL | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURAC | VARCHAR2(4) | N |  |  |
| 4 | MES_APURAC | VARCHAR2(2) | N |  |  |
| 5 | VLR_REC_EXP_ACUM | NUMBER(17,2) | Y |  |  |
| 6 | VLR_REC_OPER_ACUM | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CUSTO_ACUM | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CUSTO_EXCL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CUSTO_ADIC | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CPRES_ACUM | NUMBER(17,2) | Y |  |  |
| 11 | VLR_NEG_MES_ANT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_COMP_IPI | NUMBER(17,2) | Y |  |  |
| 13 | VLR_RES_ANO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_RES_REC_ANO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SALDO_NEG | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DED_SALDO_MES | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SALDO_NEG_MES | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SALDO_CP_MES | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CPRES_MES | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPR_CENTRAL, COD_ESTAB_CENTRAL, ANO_APURAC, MES_APURAC

**FKs**:
- COD_EMPR_CENTRAL, COD_ESTAB_CENTRAL → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CPT_AP_CENTRAL_CNI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPR_CENTRAL | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURAC | VARCHAR2(4) | N |  |  |
| 4 | MES_APURAC | VARCHAR2(2) | N |  |  |
| 5 | VLR_AQUIS_CDIR_C | NUMBER(17,2) | Y |  |  |
| 6 | VLR_AQUIS_TOT_C | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ESTOQUE_INI_M | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ESTOQUE_FIM_M | NUMBER(17,2) | Y |  |  |
| 9 | VLR_AQUIS_CDIR_M | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SAIDA_N_PRD_M | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRANSF_REC_M | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TRANSF_EFET_M | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CUSTO_M_C | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CUSTO_A_C | NUMBER(17,2) | Y |  |  |
| 15 | VLR_REC_EXP_ACUM | NUMBER(17,2) | Y |  |  |
| 16 | VLR_REC_OPER_ACUM | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CUSTO_ACUM | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CUSTO_EXCL | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CUSTO_ADIC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_CPRES_ACUM | NUMBER(17,2) | Y |  |  |
| 21 | VLR_NEG_MES_ANT | NUMBER(17,2) | Y |  |  |
| 22 | VLR_COMP_IPI | NUMBER(17,2) | Y |  |  |
| 23 | VLR_RES_ANO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_RES_REC_ANO | NUMBER(17,2) | Y |  |  |
| 25 | VLR_SALDO_NEG | NUMBER(17,2) | Y |  |  |
| 26 | VLR_DED_SALDO_MES | NUMBER(17,2) | Y |  |  |
| 27 | VLR_SALDO_NEG_MES | NUMBER(17,2) | Y |  |  |
| 28 | VLR_SALDO_CP_MES | NUMBER(17,2) | Y |  |  |
| 29 | VLR_CPRES_MES | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPR_CENTRAL, COD_ESTAB_CENTRAL, ANO_APURAC, MES_APURAC

**FKs**:
- COD_EMPR_CENTRAL, COD_ESTAB_CENTRAL → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CPT_AP_ESTAB_CI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURAC | VARCHAR2(4) | N |  |  |
| 4 | MES_APURAC | VARCHAR2(2) | N |  |  |
| 5 | VLR_RECEITA_EXP | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CUSTO_AC_PROD | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CUSTO_EXCLUIDO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CUSTO_ADIC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURAC, MES_APURAC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CPT_AP_ESTAB_CNI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURAC | VARCHAR2(4) | N |  |  |
| 4 | MES_APURAC | VARCHAR2(2) | N |  |  |
| 5 | VLR_REC_EXP_ACUM | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ESTOQ_INI_M | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ESTOQUE_FIM_M | NUMBER(17,2) | Y |  |  |
| 8 | VLR_AQUIS_CDIR_M | NUMBER(17,2) | Y |  |  |
| 9 | VLR_AQUIS_TOT_M | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SAIDA_N_PRD_M | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CUSTO_EXCL_M | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CUSTO_ADIC_M | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURAC, MES_APURAC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CPT_CLASSE_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | VARCHAR2(2) | N |  |  |
| 2 | CLASSE_REL | VARCHAR2(3) | Y |  |  |
| 3 | COD_REL | VARCHAR2(10) | Y |  |  |
| 4 | IND_TIPO_PAR | VARCHAR2(2) | Y |  |  |

**PK**: COD_OPERACAO

**FKs**:
- COD_OPERACAO → CPT_OPERACAO(COD_OPERACAO)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)

---

## CPT_CLASSE_VLR_MES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | VLR_JAN | NUMBER(17,2) | Y |  |  |
| 6 | VLR_FEV | NUMBER(17,2) | Y |  |  |
| 7 | VLR_MAR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ABR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_MAI | NUMBER(17,2) | Y |  |  |
| 10 | VLR_JUN | NUMBER(17,2) | Y |  |  |
| 11 | VLR_JUL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_AGO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SET | NUMBER(17,2) | Y |  |  |
| 14 | VLR_OUT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_NOV | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DEZ | NUMBER(17,2) | Y |  |  |
| 17 | IND_GERACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CLASSE, ANO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CLASSE → PRT_CLASSE_MSAF(COD_CLASSE)

---

## CPT_CONTAS_VLR_MES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 6 | ANO | NUMBER(4) | N |  |  |
| 7 | VLR_JAN | NUMBER(17,2) | Y |  |  |
| 8 | VLR_FEV | NUMBER(17,2) | Y |  |  |
| 9 | VLR_MAR | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ABR | NUMBER(17,2) | Y |  |  |
| 11 | VLR_MAI | NUMBER(17,2) | Y |  |  |
| 12 | VLR_JUN | NUMBER(17,2) | Y |  |  |
| 13 | VLR_JUL | NUMBER(17,2) | Y |  |  |
| 14 | VLR_AGO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SET | NUMBER(17,2) | Y |  |  |
| 16 | VLR_OUT | NUMBER(17,2) | Y |  |  |
| 17 | VLR_NOV | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DEZ | NUMBER(17,2) | Y |  |  |
| 19 | IND_GERACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CLASSE, GRUPO_CONTA, COD_CONTA, ANO

**FKs**:
- COD_CLASSE, GRUPO_CONTA, COD_CONTA → CPT_PAR_CONTAS(COD_CLASSE, GRUPO_CONTA, COD_CONTA)

---

## CPT_CP_FD_TRANSF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STEP | NUMBER(12) | Y |  | Identificador da entidade CP_STEPS. Tabela Origem: CPT_CP_STEPS. |
| 2 | ID_FD_TRANSF | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_CP_FD_TRANSF) |
| 3 | ID_FIELD | NUMBER(12) | Y |  | Identificador da entidade FIELD. Tabela Origem: CPT_DS_FIELDS. |
| 4 | ORDER_EXEC_TRANSF | NUMBER(4) | Y |  | Ordenacao para execucao das formulas de cada campo. |
| 5 | FORMULA | VARCHAR2(4000) | Y |  | Conjunto de informacoes que deverao ser processados na execucao do passo. Estas informacoes podem ser valores fixos, formulas simples ou formulas que dependem de outros campos. |
| 6 | IS_FORMULA | VARCHAR2(1) | Y |  | Indicador que representa se o campo formula representa apenas uma coluna ou uma expressao. (S)im (representa uma formula) ou (N)ao (representa uma coluna). |

**PK**: ID_FD_TRANSF

**FKs**:
- ID_FIELD → CPT_DS_FIELDS(ID_FIELD)
- ID_STEP → CPT_CP_STEPS(ID_STEP)

---

## CPT_CP_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_CPROC | NUMBER(12) | Y |  | Identificador da entidade CUSTOM_PROCESS. Tabela Origem: CPT_CUSTOM_PROCESS. |
| 2 | ID_PARAM | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_CP_PARAM) |
| 3 | IND_PARAM | VARCHAR2(1) | Y |  | Indicador do parametro (F)ixo ou (T)ela (default). Caso o indicador seja F, o Campo <value> da tabela CPT_CP_PARAM_STEP devera ser preenchido e na tela de execucao devera estar visivel porem inibido para alteracao, caso contrario o usuario devera preencher o valor do parametro na tela de execucao apenas. |
| 4 | LABEL | VARCHAR2(255) | Y |  | Descricao da etiqueta que o parametro tera na tela de execucao. Este campo vira preenchido automaticamente com o conteudo do campo <name_fd_param> da tabela CPT_DS_FIELDS mas podera sofrer alteracao do usuario. |
| 5 | CONTROL | VARCHAR2(50) | Y |  | Indicador do tipo de controle que sera associado ao parametro. Dominio: (MultiSelect), (TextBox) default, (ComboBox), (ListBox) ou (RadioButton). |
| 6 | MANDATORY | VARCHAR2(1) | Y |  | Indicador se o parametro devera sempre ser preenchido ou nao na tela de execucao. Domínio: (S)im ou (N)ao default. |
| 7 | DEF_VALUE | VARCHAR2(255) | Y |  | Valor que aparecera como default na abertura da tela de excucao. |
| 8 | MASK | VARCHAR2(255) | Y |  | Formato de mascara a ser aplicada no parametro na tela de execucao. Os Valores pre-definidos serao: DD/MM/YYYY, MM/YYYY, 9,999.99, 9,999.999, 9,999.9999, ###.###.###-##, ###.###.###/####-## |
| 9 | SHOWN_LIST_PARAM | VARCHAR2(1) | Y |  | Indicador se o parametro sera mostrado na listagem do log do processo. Dominio (S)im default ou (N)ao. |
| 10 | ENABLED | VARCHAR2(255) | Y |  | Indicador se o campo estara aberto ou nao para insercao de dado. Este campo recebera uma formula que podera ser dependencia de valor de um outro parametro anterior ou nao e retorne um booleano. ex.: :1 = ABC. |
| 11 | IND_ORDER_PARAM | NUMBER(3) | Y |  | Contem a ordenacao do parametro na tela de execucao |

**PK**: ID_PARAM

**FKs**:
- ID_CPROC → CPT_CUSTOM_PROCESS(ID_CPROC)

---

## CPT_CP_PARAM_LISTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PARAM | NUMBER(12) | Y |  | Identificador da entidade CP_PARAM. Tabela Origem: CPT_CP_PARAM. |
| 2 | ID_PARAM_LISTA | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_CP_PARAM_LISTA). |
| 3 | VALUE_KEY | VARCHAR2(4000) | Y |  | Valor individual para listas do tipo MULTISELECT ou cod\|valor para o tipo LISTBOX, neste caso a sintaxe deverá ser sempre cod=valor. |

**PK**: ID_PARAM_LISTA

**FKs**:
- ID_PARAM → CPT_CP_PARAM(ID_PARAM)

---

## CPT_CP_PARAM_STEP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STEP | NUMBER(12) | Y |  | Identificador da entidade CP_STEPS. Tabela Origem: CPT_CP_STEPS. |
| 2 | ID_PARAM | NUMBER(12) | Y |  | Identificador da entidade CP_PARAM. Tabela Origem: CPT_CP_PARAM. |
| 3 | ID_PARAM_STEP | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_CP_PARAM_STEP). |
| 4 | ID_FIELD | NUMBER(12) | Y |  | Identificador da entidade FIELDS. Tabela Origem: CPT_DS_FIELDS. |
| 5 | VALUE | VARCHAR2(255) | Y |  | Valor do parametro quando o campo CPT_CP_PARAM.IND_PARAM = (F)ixo |

**PK**: ID_PARAM_STEP

**FKs**:
- ID_PARAM → CPT_CP_PARAM(ID_PARAM)
- ID_FIELD → CPT_DS_FIELDS(ID_FIELD)
- ID_STEP → CPT_CP_STEPS(ID_STEP)

---

## CPT_CP_STEPS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_CPROC | NUMBER(12) | Y |  | Identificador da entidade CUSTOM_PROCESS. Tabela Origem: CPT_CUSTOM_PROCESS. |
| 2 | ID_STEP | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_CP_STEPS). |
| 3 | EXEC_ORDER | NUMBER(3) | Y |  | Indicador com o numero de ordem para execucao do passo. |
| 4 | IND_STEP | VARCHAR2(100) | Y |  | Indicador da atividade que o passo ira realizar: (1) Atualizacao dos dados; (2) Exportacao dos dados selecionados; (3) Report; (4) Resolucao |
| 5 | DSC_STEP | VARCHAR2(1000) | Y |  | Descricao do passo. |
| 6 | ID_DS | NUMBER(12) | Y |  | Identificador da entidade DATASOURCE. Tabela Origem: CPT_DS. |
| 7 | ID_STEP_CONNECT | NUMBER(12) | Y |  | Identificador da entidade CP_STEPS. Tabela Origem: CPT_CP_STEPS. |

**PK**: ID_STEP

**FKs**:
- ID_CPROC → CPT_CUSTOM_PROCESS(ID_CPROC)
- ID_DS → CPT_DS(ID_DS)
- ID_STEP_CONNECT → CPT_CP_STEPS(ID_STEP)

---

## CPT_CP_STEP_RESULTSET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_RESULTSET | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_CP_STEP_RESULTSET) |
| 2 | ID_STEP | NUMBER(12) | N |  | Identificador da entidade CP_STEPS. Tabela Origem: CPT_CP_STEPS. |
| 3 | PROC_ID | NUMBER(12) | N |  | Identificador da entidade LIB_PROCESSO. Tabela Origem: LIB_PROCESSO. |
| 4 | ID_ROWID_ORIG_1 | ROWID | Y |  |  |
| 5 | ID_ROWID_ORIG_2 | ROWID | Y |  |  |
| 6 | ID_ROWID_ORIG_3 | ROWID | Y |  |  |
| 7 | ID_ROWID_ORIG_4 | ROWID | Y |  |  |
| 8 | ID_ROWID_ORIG_5 | ROWID | Y |  |  |
| 9 | ID_ROWID_ORIG_6 | ROWID | Y |  |  |
| 10 | ID_ROWID_ORIG_7 | ROWID | Y |  |  |
| 11 | ID_ROWID_ORIG_8 | ROWID | Y |  |  |
| 12 | ID_ROWID_ORIG_9 | ROWID | Y |  |  |
| 13 | ID_ROWID_ORIG_10 | ROWID | Y |  |  |
| 14 | ID_ROWID_ORIG_11 | ROWID | Y |  |  |
| 15 | ID_ROWID_ORIG_12 | ROWID | Y |  |  |
| 16 | ID_ROWID_ORIG_13 | ROWID | Y |  |  |
| 17 | ID_ROWID_ORIG_14 | ROWID | Y |  |  |
| 18 | ID_ROWID_ORIG_15 | ROWID | Y |  |  |
| 19 | ID_ROWID_ORIG_16 | ROWID | Y |  |  |
| 20 | ID_ROWID_ORIG_17 | ROWID | Y |  |  |
| 21 | ID_ROWID_ORIG_18 | ROWID | Y |  |  |
| 22 | ID_ROWID_ORIG_19 | ROWID | Y |  |  |
| 23 | ID_ROWID_ORIG_20 | ROWID | Y |  |  |
| 24 | FIELD1 | VARCHAR2(4000) | Y |  |  |
| 25 | FIELD2 | VARCHAR2(4000) | Y |  |  |
| 26 | FIELD3 | VARCHAR2(4000) | Y |  |  |
| 27 | FIELD4 | VARCHAR2(4000) | Y |  |  |
| 28 | FIELD5 | VARCHAR2(4000) | Y |  |  |
| 29 | FIELD6 | VARCHAR2(4000) | Y |  |  |
| 30 | FIELD7 | VARCHAR2(4000) | Y |  |  |
| 31 | FIELD8 | VARCHAR2(4000) | Y |  |  |
| 32 | FIELD9 | VARCHAR2(4000) | Y |  |  |
| 33 | FIELD10 | VARCHAR2(4000) | Y |  |  |
| 34 | FIELD11 | VARCHAR2(4000) | Y |  |  |
| 35 | FIELD12 | VARCHAR2(4000) | Y |  |  |
| 36 | FIELD13 | VARCHAR2(4000) | Y |  |  |
| 37 | FIELD14 | VARCHAR2(4000) | Y |  |  |
| 38 | FIELD15 | VARCHAR2(4000) | Y |  |  |
| 39 | FIELD16 | VARCHAR2(4000) | Y |  |  |
| 40 | FIELD17 | VARCHAR2(4000) | Y |  |  |
| 41 | FIELD18 | VARCHAR2(4000) | Y |  |  |
| 42 | FIELD19 | VARCHAR2(4000) | Y |  |  |
| 43 | FIELD20 | VARCHAR2(4000) | Y |  |  |
| 44 | FIELD21 | VARCHAR2(4000) | Y |  |  |
| 45 | FIELD22 | VARCHAR2(4000) | Y |  |  |
| 46 | FIELD23 | VARCHAR2(4000) | Y |  |  |
| 47 | FIELD24 | VARCHAR2(4000) | Y |  |  |
| 48 | FIELD25 | VARCHAR2(4000) | Y |  |  |
| 49 | FIELD26 | VARCHAR2(4000) | Y |  |  |
| 50 | FIELD27 | VARCHAR2(4000) | Y |  |  |
| 51 | FIELD28 | VARCHAR2(4000) | Y |  |  |
| 52 | FIELD29 | VARCHAR2(4000) | Y |  |  |
| 53 | FIELD30 | VARCHAR2(4000) | Y |  |  |
| 54 | FIELD31 | VARCHAR2(4000) | Y |  |  |
| 55 | FIELD32 | VARCHAR2(4000) | Y |  |  |
| 56 | FIELD33 | VARCHAR2(4000) | Y |  |  |
| 57 | FIELD34 | VARCHAR2(4000) | Y |  |  |
| 58 | FIELD35 | VARCHAR2(4000) | Y |  |  |
| 59 | FIELD36 | VARCHAR2(4000) | Y |  |  |
| 60 | FIELD37 | VARCHAR2(4000) | Y |  |  |
| 61 | FIELD38 | VARCHAR2(4000) | Y |  |  |
| 62 | FIELD39 | VARCHAR2(4000) | Y |  |  |
| 63 | FIELD40 | VARCHAR2(4000) | Y |  |  |
| 64 | FIELD41 | VARCHAR2(4000) | Y |  |  |
| 65 | FIELD42 | VARCHAR2(4000) | Y |  |  |
| 66 | FIELD43 | VARCHAR2(4000) | Y |  |  |
| 67 | FIELD44 | VARCHAR2(4000) | Y |  |  |
| 68 | FIELD45 | VARCHAR2(4000) | Y |  |  |
| 69 | FIELD46 | VARCHAR2(4000) | Y |  |  |
| 70 | FIELD47 | VARCHAR2(4000) | Y |  |  |
| 71 | FIELD48 | VARCHAR2(4000) | Y |  |  |
| 72 | FIELD49 | VARCHAR2(4000) | Y |  |  |
| 73 | FIELD50 | VARCHAR2(4000) | Y |  |  |
| 74 | FIELD51 | VARCHAR2(4000) | Y |  |  |
| 75 | FIELD52 | VARCHAR2(4000) | Y |  |  |
| 76 | FIELD53 | VARCHAR2(4000) | Y |  |  |
| 77 | FIELD54 | VARCHAR2(4000) | Y |  |  |
| 78 | FIELD55 | VARCHAR2(4000) | Y |  |  |
| 79 | FIELD56 | VARCHAR2(4000) | Y |  |  |
| 80 | FIELD57 | VARCHAR2(4000) | Y |  |  |
| 81 | FIELD58 | VARCHAR2(4000) | Y |  |  |
| 82 | FIELD59 | VARCHAR2(4000) | Y |  |  |

**PK**: ID_RESULTSET

**FKs**:
- ID_STEP → CPT_CP_STEPS(ID_STEP)
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## CPT_CP_STEP_STATS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_RSET_STATS | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_CP_STEP_STATS). |
| 2 | ID_STEP | NUMBER(12) | Y |  | Identificador da entidade CP_STEPS. Tabela Origem: CPT_CP_STEPS. |
| 3 | PROC_ID | NUMBER(12) | Y |  | Identificador da entidade LIB_PROCESSO. Tabela Origem: LIB_PROCESSO. |
| 4 | SQL_SUBMIT | CLOB | Y |  | Descricao da query executada para compor o resultado gravado na tabela temporaria CPT_CP_STEP_RESULTSET. |
| 5 | SQL_RESULTSET | CLOB | Y |  | Descricao da query para recuperar os dados contidos na tabela CPT_CP_STEP_RESULTSET. |
| 6 | DATE_INI | DATE | Y |  | Data_hora inicial da execução do passo. |
| 7 | DATE_END | DATE | Y |  | Data_hora final da execução do passo. |
| 8 | QT_REG_PROCESS | NUMBER(12) | Y |  | Quantidade de registros processados no passo. |
| 9 | QT_REG_UPD | NUMBER(12) | Y |  | Quantidade de registros atualizados no processo, qdo o passo for relacionado a atualizacao de dados. |

**PK**: ID_RSET_STATS

**FKs**:
- ID_STEP → CPT_CP_STEPS(ID_STEP)
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## CPT_CUSTOM_PROCESS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_CPROC | NUMBER(12) | N |  | identificador unico do registro na tabela (sequence seq_cpt_custom_process) |
| 2 | NAME_CPROC | VARCHAR2(30) | Y |  | nome do processo customizado, sera utilizado para identificar as execucoes realizadas na lib_processo |
| 3 | DSC_CPROC | VARCHAR2(2000) | Y |  | descricao do processo customizado |

**PK**: ID_CPROC

---

## CPT_DS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DS | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_DS) |
| 2 | NAME_DS | VARCHAR2(30) | Y |  | Nome do DataSource |
| 3 | DSC_DS | VARCHAR2(1000) | Y |  | Descricao do DataSource |
| 4 | SQL_DS | CLOB | Y |  | Representacao em SQL dos relacionamentos criados para o DataSource |
| 5 | STATUS_DS | VARCHAR2(1) | Y |  | Indica o status do DataSource: (V)alido ou (I)nvalido. Esta ligado ao sql_ds, caso possua um sql valido devera ser V caso contrario I |
| 6 | MSG_SQL_DS | VARCHAR2(4000) | Y |  | Descricao da mensagem de erro do SQL |

**PK**: ID_DS

---

## CPT_DS_CONDITIONALS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_COND | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_DS_CONDITIONALS) |
| 2 | ID_QUERY | NUMBER(12) | Y |  | Identificador da entidade QUERY. Tabela Origem: CPT_DS_QUERIES. |
| 3 | ID_FIELD | NUMBER(12) | Y |  | Identificador da entidade FIELD. Tabela Origem: CPT_DS_FIELDS. |
| 4 | ID_FIELD_JOIN | NUMBER(12) | Y |  | Identificador da entidade FIELD. Tabela Origem: CPT_DS_FIELDS. Este campo sera usado para joins entre tabelas |
| 5 | ID_TABLE | NUMBER(12) | Y |  | Identificador da entidade TABLE. Tabela Origem: CPT_DS_TABLES. |
| 6 | IND_CLAUSE | VARCHAR2(100) | Y |  | Indicador da clausula condicional que esta sendo aplicada. Podera ser: SELECT, FROM, WHERE, HAVING, GROUP BY. Esta clausulas possuem posicoes fixas na construcao da query |
| 7 | ORDER_CLAUSE | NUMBER(3) | Y |  | Ordenacao da linha dentro da clausula. |
| 8 | IND_RELATION_OPER | VARCHAR2(50) | Y |  | Indicador do operador condicional. Podera ser: =, >, <, >=, <=, <>, in, like, not in, not like |
| 9 | IND_LOGICAL_OPER | VARCHAR2(10) | Y |  | Indicador do operador logico. Podera ser: and, or. |
| 10 | DSC_LEFT_OPER | VARCHAR2(4000) | Y |  | Descritivo do conteudo que compoe a parte esquerda da sentenca condicional. |
| 11 | DSC_RIGHT_OPER | VARCHAR2(4000) | Y |  | Descritivo do conteudo que compoe a parte direita da sentenca condicional . |
| 12 | HAS_PARAM | CHAR(1) | Y |  | Indicador se a sentenca possui parametros ou nao. Dominio (S)im ou (N)ao. |
| 13 | FORMULA | VARCHAR2(4000) | Y |  | Descreve a condicao que o GROUP BY ou HAVING devera executar. Este campo so devera conter valor para os casos do campo IND_CLAUSE = (GROUP BY ou HAVING). |

**PK**: ID_COND

**FKs**:
- ID_FIELD → CPT_DS_FIELDS(ID_FIELD)
- ID_FIELD_JOIN → CPT_DS_FIELDS(ID_FIELD)
- ID_QUERY → CPT_DS_QUERIES(ID_QUERY)
- ID_TABLE → CPT_DS_TABLES(ID_TABLE)

**Indexes**:
- UK_CPT_DS_COND (UNIQUE): (ID_COND, ID_QUERY, IND_CLAUSE, ORDER_CLAUSE)

---

## CPT_DS_FIELDS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_FIELD | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_DS_FIELDS) |
| 2 | ID_QUERY | NUMBER(12) | Y |  | Identificador da entidade QUERY. Tabela Origem: CPT_DS_QUERIES. |
| 3 | ID_TABLE | NUMBER(12) | Y |  | Identificador da entidade TABLE. Tabela Origem: CPT_DS_TABLES. |
| 4 | NAME_FIELD | VARCHAR2(100) | Y |  | Nomenclatura da tabela representativa para o usuario. |
| 5 | NAME_FD_DB | VARCHAR2(30) | Y |  | Nome interno da tabela no Banco de Dados. |
| 6 | NAME_FD_PARAM | VARCHAR2(255) | Y |  | Etiqueta do campo tipo parametro que sera utilizada para aparecer na tela de cadastro dos parametros do processo. |
| 7 | TYPE | VARCHAR2(255) | Y |  | Tipo do campo. |
| 8 | IS_KEY | CHAR(1) | Y |  | Indicador se o campo e chave na tabela. (S)im ou (N)ao. |
| 9 | IS_COMPUTED | CHAR(1) | Y |  | Indicador se o campo e computado. Caso (S)im, o campo FORMULA ira descrever seu conteudo que podera ser calculado em tempo de execucao ou receber um valor fixo. |
| 10 | IS_SHOWN | CHAR(1) | Y |  | Indicador se o campo devera ser mostrado ou nao. |
| 11 | IS_AGGREGATE | CHAR(1) | Y |  | Indicador se o campo e um agregador de valores. Caso (S)im a funcao de agregacao sera descrita no campo FORMULA. |
| 12 | IS_PARAM | CHAR(1) | Y |  | Indicador se o campo e um parametro. |
| 13 | IS_UPDATEABLE | CHAR(1) | Y |  | Indicador do campo que podera ser atualizado. (S)im ou (N)ao. Este indicador devera estar ligado somente para campos da tabela que esta habilitada para atualizacao. |
| 14 | FORMULA | VARCHAR2(4000) | Y |  | Descreve a funcao ou agregacao que o campo devera executar. |
| 15 | NAME_LIST | VARCHAR2(255) | Y |  | Nome da Lista predefinida do TAX One. |

**PK**: ID_FIELD

**FKs**:
- ID_QUERY → CPT_DS_QUERIES(ID_QUERY)
- ID_TABLE → CPT_DS_TABLES(ID_TABLE)

---

## CPT_DS_QUERIES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_QUERY | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_DS_QUERIES) |
| 2 | ID_DS | NUMBER(12) | Y |  | Identificador da entidade DS(DataSource). Tabela Origem: CPT_DS. |
| 3 | IND_LOGICAL_OPER | VARCHAR2(20) | Y |  | Indicador que reprensentara o operador entre queries. Os indicadores possiveis sao: UNION, UNION ALL, MINUS e INTERSECT  |
| 4 | ID_QUERY_CONNECT | NUMBER(12) | Y |  | Identificador da entidade QUERY, representa sempre o relacionamento entre duas entidades QUERY este campo so devera estar preenchido quando IND_LOGICAL_OPER tambem estiver preenchido. |
| 5 | IS_DISTINCT | VARCHAR2(1) | Y |  | Indicador responsavel por representar na query se ela sera distinct ou nao. |

**PK**: ID_QUERY

**FKs**:
- ID_DS → CPT_DS(ID_DS)
- ID_QUERY_CONNECT → CPT_DS_QUERIES(ID_QUERY)

---

## CPT_DS_TABLES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_TABLE | NUMBER(12) | N |  | Identificador unico do registro na tabela (sequence SEQ_CPT_DS_TABLES) |
| 2 | ID_QUERY | NUMBER(12) | Y |  | Identificador da entidade QUERY. Tabela Origem: CPT_DS_QUERIES. |
| 3 | NAME_TABLE | VARCHAR2(100) | Y |  | Nomenclatura da tabela representativa para o usuario. |
| 4 | NAME_TB_DB | VARCHAR2(100) | Y |  | Nome interno da tabela no Banco de Dados. |
| 5 | DSC_TABLE | VARCHAR2(1000) | Y |  | Descricao da tabela representativa para o usuario. |
| 6 | IS_UPDATEABLE | CHAR(1) | Y |  | Indicador da tabela que podera ser atualizada. (S)im ou (N)ao. Este indicador devera estar ligado para apenas uma tabela. |

**PK**: ID_TABLE

**FKs**:
- ID_QUERY → CPT_DS_QUERIES(ID_QUERY)

---

## CPT_EMP_REG17_CI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | VLR_EXP_MES_ANT | NUMBER(14,2) | Y |  |  |
| 5 | VLR_CEXP_MES_ANT | NUMBER(14,2) | Y |  |  |
| 6 | VLR_TOTEXP_MES_ANT | NUMBER(14,2) | Y |  |  |
| 7 | VLR_EXP_MES | NUMBER(14,2) | Y |  |  |
| 8 | VLR_CEXP_MES | NUMBER(14,2) | Y |  |  |
| 9 | VLR_TOTEXP_MES | NUMBER(14,2) | Y |  |  |
| 10 | VLR_TOTEXP_AC_MES | NUMBER(14,2) | Y |  |  |
| 11 | VLR_RECBRUTA_M_ANT | NUMBER(14,2) | Y |  |  |
| 12 | VLR_RECBRUTA_MES | NUMBER(14,2) | Y |  |  |
| 13 | VLR_RECBRUT_AC_MES | NUMBER(14,2) | Y |  |  |
| 14 | VLR_REL_PERCENT | NUMBER(7,4) | Y |  |  |
| 15 | VLR_UTIL_PROD_MES | NUMBER(14,2) | Y |  |  |
| 16 | VLR_PROD_MES_NVEND | NUMBER(14,2) | Y |  |  |
| 17 | VLR_EXCL_ANO_ANT | NUMBER(14,2) | Y |  |  |
| 18 | VLR_PROD_MES | NUMBER(14,2) | Y |  |  |
| 19 | VLR_PROD_MES_ANT | NUMBER(14,2) | Y |  |  |
| 20 | VLR_PROD_AC_MES | NUMBER(14,2) | Y |  |  |
| 21 | VLR_BASE_AC_MES | NUMBER(14,2) | Y |  |  |
| 22 | VLR_CPRES_AC_MES | NUMBER(14,2) | Y |  |  |
| 23 | VLR_COMP_MATR_ANT | NUMBER(14,2) | Y |  |  |
| 24 | VLR_TRAN_OUT_M_ANT | NUMBER(14,2) | Y |  |  |
| 25 | VLR_PED_RESS_M_ANT | NUMBER(14,2) | Y |  |  |
| 26 | VLR_CPRES_MES_ANT | NUMBER(14,2) | Y |  |  |
| 27 | VLR_COMP_MATR_MES | NUMBER(14,2) | Y |  |  |
| 28 | VLR_TRANSF_OUTROS | NUMBER(14,2) | Y |  |  |
| 29 | VLR_PED_RESSARC | NUMBER(14,2) | Y |  |  |
| 30 | VLR_CPRES_MES | NUMBER(14,2) | Y |  |  |
| 31 | VLR_CPRES_AC_MES_2 | NUMBER(14,2) | Y |  |  |
| 32 | VLR_CP_M_ANT_DEDUC | NUMBER(14,2) | Y |  |  |
| 33 | VLR_CRE_NEG_M_ANT | NUMBER(14,2) | Y |  |  |
| 34 | VLR_CRE_NEG_MES | NUMBER(14,2) | Y |  |  |
| 35 | VLR_CRE_NEG_AC_MES | NUMBER(14,2) | Y |  |  |
| 36 | VLR_SAL_CPRES_MES | NUMBER(14,2) | Y |  |  |
| 37 | VLR_CRE_NEG_ULT_AP | NUMBER(14,2) | Y |  |  |
| 38 | VLR_SALCRE_NEG_MES | NUMBER(14,2) | Y |  |  |
| 39 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 40 | USUARIO | VARCHAR2(40) | Y |  |  |
| 41 | VLR_UTIL_COMB_MES | NUMBER(14,2) | Y |  |  |
| 42 | VLR_COMB_MES_ANT | NUMBER(14,2) | Y |  |  |
| 43 | VLR_COMB_MES_ACMES | NUMBER(14,2) | Y |  |  |
| 44 | VLR_COMB_EXCL_MES | NUMBER(14,2) | Y |  |  |
| 45 | VLR_COMB_ACRES_MES | NUMBER(14,2) | Y |  |  |
| 46 | VLR_COMB_MES | NUMBER(14,2) | Y |  |  |
| 47 | VLR_UTIL_ENER_MES | NUMBER(14,2) | Y |  |  |
| 48 | VLR_ENER_MES_ANT | NUMBER(14,2) | Y |  |  |
| 49 | VLR_ENER_MES_ACMES | NUMBER(14,2) | Y |  |  |
| 50 | VLR_ENER_EXCL_MES | NUMBER(14,2) | Y |  |  |
| 51 | VLR_ENER_ACRES_MES | NUMBER(14,2) | Y |  |  |
| 52 | VLR_ENER_MES | NUMBER(14,2) | Y |  |  |
| 53 | VLR_UTIL_SERV_MES | NUMBER(14,2) | Y |  |  |
| 54 | VLR_SERV_MES_ANT | NUMBER(14,2) | Y |  |  |
| 55 | VLR_SERV_MES_ACMES | NUMBER(14,2) | Y |  |  |
| 56 | VLR_SERV_EXCL_MES | NUMBER(14,2) | Y |  |  |
| 57 | VLR_SERV_ACRES_MES | NUMBER(14,2) | Y |  |  |
| 58 | VLR_SERV_MES | NUMBER(14,2) | Y |  |  |
| 59 | FATOR_APLIC | NUMBER(7,6) | Y |  |  |

**PK**: COD_EMPRESA, ANO_APURACAO, MES_APURACAO

---

## CPT_EMP_VLR_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | COD_OPERACAO | VARCHAR2(2) | N |  |  |
| 5 | VLR_MES | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ACUM_MES_ANT | NUMBER(17,2) | Y |  |  |
| 7 | FATOR_APLIC | NUMBER(7,6) | Y |  |  |
| 8 | PERC_APLIC | NUMBER(7,4) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, ANO_APURACAO, MES_APURACAO, COD_OPERACAO

---

## CPT_EST_CUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 7 | QTD_CONSUMO | NUMBER(17,6) | Y |  |  |
| 8 | VLR_CONSUMO | NUMBER(17,2) | Y |  |  |
| 9 | QTD_ENTRADAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ENTRADAS | NUMBER(17,2) | Y |  |  |
| 11 | QTD_EST_INI | NUMBER(17,6) | Y |  |  |
| 12 | VLR_EST_INI | NUMBER(17,2) | Y |  |  |
| 13 | QTD_EST_FIM_INF | NUMBER(17,6) | Y |  |  |
| 14 | VLR_EST_FIM_INF | NUMBER(17,2) | Y |  |  |
| 15 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, IDENT_PRODUTO, IDENT_INSUMO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_INSUMO → X2013_PRODUTO(IDENT_PRODUTO)

---

## CPT_ETIQUETAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | TRIM_APURACAO | NUMBER(1) | N |  |  |
| 5 | NUM_ARQUIVO | NUMBER(1) | N |  |  |
| 6 | DAT_GERACAO | DATE | Y |  |  |
| 7 | NUM_BYTES | NUMBER(10) | Y |  |  |
| 8 | NUM_REGISTROS | NUMBER(10) | Y |  |  |
| 9 | TOTALIZADOR | NUMBER(17,2) | Y |  |  |
| 10 | NUM_MIDIAS | NUMBER(3) | Y |  |  |
| 11 | NOM_ARQUIVO | VARCHAR2(12) | Y |  |  |
| 12 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, TRIM_APURACAO, NUM_ARQUIVO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CPT_INS_ARV_INS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ_PRD_INS | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | IND_PRD_INSUMO | CHAR(1) | Y |  |  |
| 5 | COD_PRD_INSUMO | VARCHAR2(60) | Y |  |  |
| 6 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 7 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: SEQ_PRD_INS

**Indexes**:
- IX_CPT_INS_ARV_INS (UNIQUE): (COD_EMPRESA, COD_ESTAB, IND_PRD_INSUMO, COD_PRD_INSUMO, USUARIO)

---

## CPT_INS_ARV_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ_PRD | NUMBER(12) | N |  |  |
| 2 | SEQ_PROD_INSUMO | NUMBER(12) | N |  |  |
| 3 | IND_PROD_INSUMO | CHAR(1) | Y |  |  |
| 4 | COD_PROD_INSUMO | VARCHAR2(60) | Y |  |  |
| 5 | DSC_INSUMO | VARCHAR2(50) | Y |  |  |
| 6 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: SEQ_PRD, SEQ_PROD_INSUMO

---

## CPT_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | VARCHAR2(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | IND_APURACAO | CHAR(1) | Y |  |  |

**PK**: COD_OPERACAO

---

## CPT_PAR_CONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 2 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 4 | IND_SOMA | CHAR(1) | Y |  |  |
| 5 | IND_APROPRIA | CHAR(1) | Y |  |  |

**PK**: COD_CLASSE, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_CLASSE → PRT_CLASSE_MSAF(COD_CLASSE)

---

## CPT_PAR_EMPRESA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_TIPO_APURACAO | CHAR(1) | Y |  |  |
| 3 | IND_TIPO_CALCULO | CHAR(1) | Y |  |  |
| 4 | VLR_PERC_APLICADO | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA

---

## CPT_PAR_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | VARCHAR2(2) | N |  |  |
| 2 | IND_TIPO_PAR | VARCHAR2(2) | N |  |  |
| 3 | VALOR_ORIGEM | VARCHAR2(150) | Y |  |  |

**PK**: COD_OPERACAO, IND_TIPO_PAR

**FKs**:
- COD_OPERACAO → CPT_OPERACAO(COD_OPERACAO)

---

## CPT_PRD_ARV_INS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ_PRD_INS | NUMBER(12) | N |  |  |
| 2 | SEQ_PRD | NUMBER(12) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 6 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: SEQ_PRD_INS, SEQ_PRD

---

## CPT_PRD_ARV_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ_PRD | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 7 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: SEQ_PRD

**Indexes**:
- IX_CPT_PRD_ARV_PRD (UNIQUE): (COD_EMPRESA, COD_ESTAB, IND_PRODUTO, COD_PRODUTO, USUARIO)

---

## CPT_RAT_CPRES_EXP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | VLR_EXP_MES | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CPRES_RAT_MES | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, ANO_APURACAO, MES_APURACAO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## CPT_REG17_CINTEGR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | VLR_EXP_MES_ANT | NUMBER(14,2) | Y |  |  |
| 6 | VLR_CEXP_MES_ANT | NUMBER(14,2) | Y |  |  |
| 7 | VLR_TOTEXP_MES_ANT | NUMBER(14,2) | Y |  |  |
| 8 | VLR_EXP_MES | NUMBER(14,2) | Y |  |  |
| 9 | VLR_CEXP_MES | NUMBER(14,2) | Y |  |  |
| 10 | VLR_TOTEXP_MES | NUMBER(14,2) | Y |  |  |
| 11 | VLR_TOTEXP_AC_MES | NUMBER(14,2) | Y |  |  |
| 12 | VLR_RECBRUTA_M_ANT | NUMBER(14,2) | Y |  |  |
| 13 | VLR_RECBRUTA_MES | NUMBER(14,2) | Y |  |  |
| 14 | VLR_RECBRUT_AC_MES | NUMBER(14,2) | Y |  |  |
| 15 | VLR_REL_PERCENT | NUMBER(7,4) | Y |  |  |
| 16 | VLR_UTIL_PROD_MES | NUMBER(14,2) | Y |  |  |
| 17 | VLR_PROD_MES_NVEND | NUMBER(14,2) | Y |  |  |
| 18 | VLR_EXCL_ANO_ANT | NUMBER(14,2) | Y |  |  |
| 19 | VLR_PROD_MES | NUMBER(14,2) | Y |  |  |
| 20 | VLR_PROD_MES_ANT | NUMBER(14,2) | Y |  |  |
| 21 | VLR_PROD_AC_MES | NUMBER(14,2) | Y |  |  |
| 22 | VLR_BASE_AC_MES | NUMBER(14,2) | Y |  |  |
| 23 | VLR_CPRES_AC_MES | NUMBER(14,2) | Y |  |  |
| 24 | VLR_COMP_MATR_ANT | NUMBER(14,2) | Y |  |  |
| 25 | VLR_TRAN_OUT_M_ANT | NUMBER(14,2) | Y |  |  |
| 26 | VLR_PED_RESS_M_ANT | NUMBER(14,2) | Y |  |  |
| 27 | VLR_CPRES_MES_ANT | NUMBER(14,2) | Y |  |  |
| 28 | VLR_COMP_MATR_MES | NUMBER(14,2) | Y |  |  |
| 29 | VLR_TRANSF_OUTROS | NUMBER(14,2) | Y |  |  |
| 30 | VLR_PED_RESSARC | NUMBER(14,2) | Y |  |  |
| 31 | VLR_CPRES_MES | NUMBER(14,2) | Y |  |  |
| 32 | VLR_CPRES_AC_MES_2 | NUMBER(14,2) | Y |  |  |
| 33 | VLR_CP_M_ANT_DEDUC | NUMBER(14,2) | Y |  |  |
| 34 | VLR_CRE_NEG_M_ANT | NUMBER(14,2) | Y |  |  |
| 35 | VLR_CRE_NEG_MES | NUMBER(14,2) | Y |  |  |
| 36 | VLR_CRE_NEG_AC_MES | NUMBER(14,2) | Y |  |  |
| 37 | VLR_SAL_CPRES_MES | NUMBER(14,2) | Y |  |  |
| 38 | VLR_CRE_NEG_ULT_AP | NUMBER(14,2) | Y |  |  |
| 39 | VLR_SALCRE_NEG_MES | NUMBER(14,2) | Y |  |  |
| 40 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 41 | USUARIO | VARCHAR2(40) | Y |  |  |
| 42 | IND_DIG_CALC | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## CPT_VLR_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_OPERACAO | VARCHAR2(2) | N |  |  |
| 6 | VLR_MES | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ACUM_MES_ANT | NUMBER(17,2) | Y |  |  |
| 8 | FATOR_APLIC | NUMBER(7,6) | Y |  |  |
| 9 | PERC_APLIC | NUMBER(7,4) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_OPERACAO → CPT_OPERACAO(COD_OPERACAO)

---

