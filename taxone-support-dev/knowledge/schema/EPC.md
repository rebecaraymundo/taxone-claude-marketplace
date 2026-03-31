# Módulo: EPC (EFD PIS/COFINS) - 88 tabelas

## EPC_AJT_REST_PARAMETRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VLR_ALIQ_PIS | NUMBER(7,4) | N |  |  |
| 4 | VLR_ALIQ_COFINS | NUMBER(7,4) | N |  |  |
| 5 | COD_CREDITO | VARCHAR2(3) | N |  |  |
| 6 | COD_AJ | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, VLR_ALIQ_PIS, VLR_ALIQ_COFINS

---

## EPC_AJUSTE_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_REF | DATE | Y |  |  |
| 4 | REG_AJUSTE | VARCHAR2(2) | Y |  |  |
| 5 | TIPO_AJUSTE | CHAR(1) | Y |  |  |
| 6 | COD_AJUSTE | VARCHAR2(2) | Y |  |  |
| 7 | NUM_PROC_ATO_CONC | VARCHAR2(30) | Y |  |  |
| 8 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 9 | DSC_AJUSTE | VARCHAR2(255) | Y |  |  |
| 10 | IDENT_SCP | NUMBER(12) | Y |  |  |

**FKs**:
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- UK_EPC_AJUSTE_APUR (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_REF, REG_AJUSTE, TIPO_AJUSTE, COD_AJUSTE, NUM_PROC_ATO_CONC, IDENT_SCP)

---

## EPC_APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APUR_INI | DATE | N |  |  |
| 6 | DAT_APUR_FIM | DATE | N |  |  |
| 7 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 8 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 9 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 10 | DSC_OBS | VARCHAR2(255) | Y |  |  |
| 11 | DAT_REALIZACAO | DATE | Y |  |  |
| 12 | COD_PERFIL | VARCHAR2(3) | Y |  |  |
| 13 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: ID_REG

**FKs**:
- COD_LAYOUT → CAD_LAYOUT(COD_LAYOUT)

**Indexes**:
- IU_EPC_APURACAO (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_SCP)

---

## EPC_APURACAO_ARQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | ID_SEQ | NUMBER(12) | N |  |  |
| 3 | ARQUIVO_TEXTO | BLOB | N |  |  |

**PK**: ID_REG, ID_SEQ

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

---

## EPC_APUR_CRED_DISP
**Comment**: Tabela do EFD-PIS-COFINS que armazena os créditos disponiveis do Pis e Cofins para serem utilizados em escriturações posteriores. Tais creditos são gerados a partir dos registros M100, quando o credito foi utilizado parcialmente e 1101, com os creditos extemporaneos. A cada escrituracao subsequente que utiliza o crédito, o saldo do credito disponivel é recalculado.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_CRED_DISP | NUMBER(12) | N |  | sequencial unico |
| 2 | ID_REG | NUMBER(12) | N |  | identificador da apuracao que gerou o credito |
| 3 | COD_PIS_COFINS | VARCHAR2(10) | N |  | codigo que identifica se o crédito apurado é do PIS ou do COFINS. Dominio: PIS, COFINS |
| 4 | COD_CRED | VARCHAR2(3) | N |  | Codigo do Tipo do Credito - origem EPC_COD_CRED_TRANS - TFIX93 |
| 5 | IND_CRED_ORI | CHAR(1) | N |  | Indicador de Origem do Credito. Dominio: 0 - operacoes proprias; 1 - incorporacao, cisao, fusao |
| 6 | CNPJ_SUC | VARCHAR2(14) | N |  | CNPJ da Pessoa Juricia cedente do credito. Preenchida quando IND_CRED_ORI = 1 |
| 7 | VLR_CRED_APUR | NUMBER(17,2) | Y |  | Valor do Credito Apurado - Originario do M100. |
| 8 | VLR_CRED_APUR_EXTEMP | NUMBER(17,2) | Y |  | Valor do Credito Extemporaneo Apurado - Originario do 1101. |
| 9 | VLR_CRED_UTIL_DESC | NUMBER(17,2) | Y |  | valor total do credito utilizado para desconto na contribuicao. Credito utilizado na propria apuracao que gerou o credito e em apurações subsequentes. |
| 10 | VLR_CRED_UTIL_PER | NUMBER(17,2) | Y |  | valor total do credito utilizado por pedido de ressarcimento. Credito utilizado na propria apuracao que gerou o credito e em apurações subsequentes. |
| 11 | VLR_CRED_UTIL_DCOMP | NUMBER(17,2) | Y |  | valor total do credito utilizado por declaracao de compensacao intermediaria. Credito utilizado na propria apuracao que gerou o credito e em apurações subsequentes. |
| 12 | VLR_CRED_UTIL_TRANS | NUMBER(17,2) | Y |  | valor total do credito utilizado em transferencia de cisao, fusao ou incorporacao. Credito utilizado na propria apuracao que gerou o credito e em apurações subsequentes. |
| 13 | VLR_CRED_UTIL_OUT | NUMBER(17,2) | Y |  | valor total do credito utilizado em outras formas. Credito utilizado na propria apuracao que gerou o credito e em apurações subsequentes. |
| 14 | VLR_CRED_DISP | NUMBER(17,2) | Y |  | Valor do Credito Disponivel para ser utilizado (VLR_CRED_APUR + VLR_CRED_APUR_EXTEMP - VLR_CRED_UTIL). |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  | Indicador de Gravacao. Dominio: 4 - incluido manualmente; 6 - gerado pelo sistema. |
| 16 | PER_APU_CRED | VARCHAR2(7) | N |  |  |
| 17 | IND_CANCELA | CHAR(1) | Y | 'N' |  |

**PK**: ID_REG_CRED_DISP

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

**Indexes**:
- IU_EPC_APUR_CRED_DISP (UNIQUE): (ID_REG, COD_PIS_COFINS, COD_CRED, IND_CRED_ORI, CNPJ_SUC, PER_APU_CRED)

---

## EPC_APUR_RET_DISP
**Comment**: Tabela do EFD-PIS-COFINS que armazena os valores retidos na fonte do Pis e Cofins, que estao disponiveis para serem utilizados em escrituracoes posteriores. Tais retencoes sao geradas a partir dos registros F600. A cada escrituracao subsequente que utiliza o valor da retencao, o saldo do valor da retencao disponivel é recalculado.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_RET_DISP | NUMBER(12) | N |  | sequencial unico |
| 2 | ID_REG | NUMBER(12) | N |  | identificador da apuracao que gerou o valor da retencao |
| 3 | COD_PIS_COFINS | VARCHAR2(10) | N |  | codigo que identifica se o valor da retencao apurado é do PIS ou do COFINS. Dominio: PIS, COFINS |
| 4 | COD_RET_FONTE | VARCHAR2(2) | N |  | Codigo Indicador de Natureza da Retencao na Fonte. Origem X145_CONTRIB_RET_FONTE, campo COD_RET_FONTE. Dominio: 01, 02, 03, 04, 05, 99. |
| 5 | IND_NAT_REC | CHAR(1) | N |  | Indicador da Natureza da Receita. Origem X145_CONTRIB_RET_FONTE, campo IND_NAT_REC. Dominio: 0 - receita nao cumulativa; 1 - receita cumulativa. |
| 6 | IND_COND_PJ_DECL | CHAR(1) | N |  | Indicador da condicao da pessoa juridica declarante. Origem X145_CONTRIB_RET_FONTE, campo IND_COND_PJ_DECL. Dominio: 0 – Beneficiaria da Retencao/Recolhimento; 1- Responsavel pela Retencao/Recolhimento |
| 7 | VLR_RET_APUR | NUMBER(17,2) | Y |  | Valor da Retencao Apurado - Originario do F600. Origem X145_CONTRIB_RET_FONTE, campos VLR_RET_FONTE_PIS e VLR_RET_FONTE_COFINS. |
| 8 | VLR_RET_UTIL_DED | NUMBER(17,2) | Y |  | valor total da retencao utilizado para deducao na contribuicao. Valor da retencao utilizado na propria apuracao que gerou a retencao e em apurações subsequentes. |
| 9 | VLR_RET_UTIL_PER | NUMBER(17,2) | Y |  | valor total da retencao utilizado por pedido de restituicao. Valor da retencao utilizado em apurações subsequentes à apuracao que gerou a retencao. |
| 10 | VLR_RET_UTIL_DCOMP | NUMBER(17,2) | Y |  | valor total da retencao utilizado por declaracao de compensacao. Valor da retencao utilizado em apurações subsequentes à apuracao que gerou a retencao. |
| 11 | VLR_RET_DISP | NUMBER(17,2) | Y |  | Valor da Retencao Disponivel para ser utilizado (VLR_RET_APUR - VLR_RET_UTIL_DED - VLR_RET_UTIL_PER - VLR_RET_UTIL_DCOMP). |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  | Indicador de Gravacao. Dominio: 4 - incluido manualmente; 6 - gerado pelo sistema. |
| 13 | IND_CANCELA | CHAR(1) | Y | 'N' |  |

**PK**: ID_REG_RET_DISP

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

**Indexes**:
- IU_EPC_APUR_RET_DISP (UNIQUE): (ID_REG, COD_PIS_COFINS, COD_RET_FONTE, IND_NAT_REC, IND_COND_PJ_DECL)

---

## EPC_CAD_BEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_BEM | VARCHAR2(68) | N |  |  |
| 5 | COD_BEM_REAL | VARCHAR2(68) | Y |  |  |
| 6 | COD_INC_REAL | VARCHAR2(6) | Y |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, COD_BEM

**Indexes**:
- IX_EPC_CAD_BEM: (PROC_ID, COD_EMPRESA, COD_ESTAB, COD_BEM_REAL, COD_INC_REAL)

---

## EPC_CAD_CCUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 5 | COD_CUSTO | VARCHAR2(50) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, GRUPO_CUSTO, COD_CUSTO

---

## EPC_CAD_CONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PROC_ID, GRUPO_CONTA, COD_CONTA

**Indexes**:
- IX_EPC_CAD_CONTA_01: (PROC_ID, COD_CONTA, GRUPO_CONTA)

---

## EPC_CAD_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB

---

## EPC_CAD_MED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 5 | COD_MEDIDA | VARCHAR2(8) | N |  |  |
| 6 | IND_TAB_ORIGEM | VARCHAR2(5) | Y |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, GRUPO_MEDIDA, COD_MEDIDA

---

## EPC_CAD_NAT_OP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(10) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## EPC_CAD_OBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_OBSERVACAO | VARCHAR2(9) | N |  |  |
| 5 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 6 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, GRUPO_OBSERVACAO, COD_OBSERVACAO, IND_ICOMPL_LANCTO

---

## EPC_CAD_PARTIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(15) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

**Indexes**:
- IX_EPC_CAD_PARTIC: (PROC_ID, IND_FIS_JUR, COD_FIS_JUR)

---

## EPC_CAD_PROD_REFRI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_MEDIDA, COD_MEDIDA

---

## EPC_CAD_PROD_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | PROD_SERV | VARCHAR2(1) | N |  |  |
| 5 | GRUPO_PROD_SERV | VARCHAR2(9) | N |  |  |
| 6 | IND_PROD_SERV | VARCHAR2(1) | N |  |  |
| 7 | COD_PROD_SERV | VARCHAR2(60) | N |  |  |
| 8 | IND_NFC_E | VARCHAR2(1) | Y |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, PROD_SERV, GRUPO_PROD_SERV, IND_PROD_SERV, COD_PROD_SERV

**Indexes**:
- IDX_EPC_PROD_GRUPO: (PROC_ID, COD_EMPRESA, COD_ESTAB, GRUPO_PROD_SERV, COD_PROD_SERV)

---

## EPC_CAPA_REDUCAO_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_CRZ | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  |  |
| 7 | COD_MODELO_ECF | VARCHAR2(30) | Y |  |  |
| 8 | COD_FABRICACAO_ECF | VARCHAR2(20) | Y |  |  |
| 9 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 10 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 11 | NUM_COO_INI | VARCHAR2(9) | Y |  |  |
| 12 | NUM_COO_FIM | VARCHAR2(9) | Y |  |  |
| 13 | SIT_ESCRITURA_ESPECIAL | VARCHAR2(300) | Y |  |  |
| 14 | NUM_COO_FIM_REI | VARCHAR2(9) | Y |  |  |

**PK**: DATA_FISCAL, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_CRZ

**Indexes**:
- IX_EPC_CAPA_REDUCAO_ECF: (DATA_FISCAL, COD_ESTAB, COD_CAIXA_ECF, COD_MODELO, COD_EMPRESA, NUM_CRZ)

---

## EPC_COD_CRED_TRANS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CRED_TRANS | VARCHAR2(3) | N |  |  |
| 2 | DSC_CRED_TRANS | VARCHAR2(150) | Y |  |  |

**PK**: COD_CRED_TRANS

---

## EPC_CRED_INC_FUS_CIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_ANO_CRED | DATE | Y |  |  |
| 4 | IND_NAT_EVENTO | VARCHAR2(2) | Y |  |  |
| 5 | DATA_EVENTO | DATE | Y |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 7 | COD_CRED_TRANS | VARCHAR2(3) | Y |  |  |
| 8 | VLR_CRED_TRANSF_PIS | NUMBER(17,2) | Y |  |  |
| 9 | PERC_CRED_ORIG_TRANSF | NUMBER(8,2) | Y |  |  |
| 10 | VLR_CRED_TRANSF_COFINS | NUMBER(17,2) | Y |  |  |
| 11 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 12 | DAT_APROP_CRED | DATE | Y |  |  |
| 13 | V_DATA_CRED | DATE | Y | NVL("DAT_APROP_CRED","DATA_EVENTO") |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CRED_TRANS → EPC_COD_CRED_TRANS(COD_CRED_TRANS)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_EPC_CRED_INC_VIRTUAL: (COD_EMPRESA, COD_ESTAB, V_DATA_CRED, IND_NAT_EVENTO, IDENT_FIS_JUR, COD_CRED_TRANS, IDENT_SCP)
- IX_FK_SAF_2470: (IDENT_FIS_JUR)
- UK_EPC_CRED_INC_FUS_CIS (UNIQUE): (COD_EMPRESA, COD_ESTAB, MES_ANO_CRED, IND_NAT_EVENTO, IDENT_FIS_JUR, COD_CRED_TRANS, IDENT_SCP)

---

## EPC_CRED_PRES_ESTOQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_ANO_UTIL_CRED | VARCHAR2(6) | Y |  |  |
| 4 | VLR_TOT_ESTOQUE | NUMBER(17,2) | Y |  |  |
| 5 | VLR_PARCELA_SEM_CRED | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE_CALCULO_CRED | NUMBER(17,2) | Y |  |  |
| 7 | VLR_MES_CREDITO | NUMBER(17,2) | Y |  |  |
| 8 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 9 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 10 | VLR_MES_CPA_PIS | NUMBER(17,2) | Y |  |  |
| 11 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 12 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 13 | VLR_MES_CPA_COFINS | NUMBER(17,2) | Y |  |  |
| 14 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 15 | DESC_ESTOQUE | VARCHAR2(150) | Y |  |  |
| 16 | IDENT_SCP | NUMBER(12) | Y |  |  |

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_EPC_CRED_PRES_CONTA: (IDENT_CONTA)
- UK_PISCOF_CP_ESTOQ_F150 (UNIQUE): (COD_EMPRESA, COD_ESTAB, MES_ANO_UTIL_CRED, COD_SIT_PIS, COD_SIT_COFINS, IDENT_CONTA, IDENT_SCP)

---

## EPC_CRED_UTIL
**Comment**: Tabela do EFD-PIS-COFINS que armazena os créditos utilizados do Pis e Cofins, provenientes de apuracoes anteriores ao periodo da apuracao atual (ID_REG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_CRED_UTIL | NUMBER(12) | N |  | sequencial unico |
| 2 | ID_REG | NUMBER(12) | N |  | identificador da apuracao que está utilizando o credito |
| 3 | ID_REG_CRED_DISP | NUMBER(12) | N |  | Identificador do credito disponivel que está sendo utilizado. Apuracao que dispoe do credito é anterior a que está utilizando o credito(ID_REG). |
| 4 | VLR_CRED_UTIL_DESC | NUMBER(17,2) | Y |  | valor total do credito utilizado para desconto na contribuicao. |
| 5 | VLR_CRED_UTIL_PER | NUMBER(17,2) | Y |  | valor total do credito utilizado por pedido de ressarcimento. |
| 6 | VLR_CRED_UTIL_DCOMP | NUMBER(17,2) | Y |  | valor total do credito utilizado por declaracao de compensacao intermediaria. |
| 7 | VLR_CRED_UTIL_TRANS | NUMBER(17,2) | Y |  | valor total do credito utilizado em transferencia de cisao, fusao ou incorporacao. |
| 8 | VLR_CRED_UTIL_OUT | NUMBER(17,2) | Y |  | valor total do credito utilizado em outras formas. |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: ID_REG_CRED_UTIL

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)
- ID_REG_CRED_DISP → EPC_APUR_CRED_DISP(ID_REG_CRED_DISP)

**Indexes**:
- IU_EPC_CRED_UTIL (UNIQUE): (ID_REG, ID_REG_CRED_DISP)

---

## EPC_DADOS_LUCRO_PRES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | DICIONARIO_ORIGEM | VARCHAR2(5) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | COD_MOD | VARCHAR2(2) | N |  |  |
| 6 | SERIE | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE | VARCHAR2(2) | N |  |  |
| 8 | COD_SIT | VARCHAR2(2) | N |  |  |
| 9 | CST_PIS | VARCHAR2(2) | N |  |  |
| 10 | CST_COFINS | VARCHAR2(2) | N |  |  |
| 11 | CFOP | VARCHAR2(4) | N |  |  |
| 12 | COD_CTA | VARCHAR2(70) | N |  |  |
| 13 | IND_TIPO_ALIQ | CHAR(1) | N |  |  |
| 14 | ALIQ_PIS | NUMBER(19,4) | N |  |  |
| 15 | ALIQ_COFINS | NUMBER(19,4) | N |  |  |
| 16 | INFO_COMPL | VARCHAR2(255) | N |  |  |
| 17 | NUM_DOC_INI | VARCHAR2(15) | Y |  |  |
| 18 | NUM_DOC_FIM | VARCHAR2(15) | Y |  |  |
| 19 | NUM_CUPOM_INI | VARCHAR2(6) | Y |  |  |
| 20 | NUM_CUPOM_FIM | VARCHAR2(6) | Y |  |  |
| 21 | VL_TOT_REC | NUMBER(17,2) | Y |  |  |
| 22 | QUANT_DOC | NUMBER(7) | Y |  |  |
| 23 | VL_DESC_PIS | NUMBER(17,2) | Y |  |  |
| 24 | VL_BC_PIS | NUMBER(18,3) | Y |  |  |
| 25 | VL_PIS | NUMBER(17,2) | Y |  |  |
| 26 | VL_DESC_COFINS | NUMBER(17,2) | Y |  |  |
| 27 | VL_BC_COFINS | NUMBER(18,3) | Y |  |  |
| 28 | VL_COFINS | NUMBER(17,2) | Y |  |  |
| 29 | VL_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 30 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |

**PK**: ID_REG, DICIONARIO_ORIGEM, COD_EMPRESA, COD_ESTAB, COD_MOD, SERIE, SUB_SERIE, COD_SIT, CST_PIS, CST_COFINS, CFOP, GRUPO_CONTA, COD_CTA, IND_TIPO_ALIQ, ALIQ_PIS, ALIQ_COFINS, INFO_COMPL

---

## EPC_DAD_LUC_PRES_PROC_RF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | DICIONARIO_ORIGEM | VARCHAR2(5) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | COD_MOD | VARCHAR2(2) | N |  |  |
| 6 | COD_SIT | VARCHAR2(2) | N |  |  |
| 7 | CST_PIS | VARCHAR2(2) | N |  |  |
| 8 | CST_COFINS | VARCHAR2(2) | N |  |  |
| 9 | CFOP | VARCHAR2(4) | N |  |  |
| 10 | COD_CTA | VARCHAR2(70) | N |  |  |
| 11 | IND_TIPO_ALIQ | CHAR(1) | N |  |  |
| 12 | ALIQ_PIS | NUMBER(19,4) | N |  |  |
| 13 | ALIQ_COFINS | NUMBER(19,4) | N |  |  |
| 14 | INFO_COMPL | VARCHAR2(255) | N |  |  |
| 15 | NUM_PROC | VARCHAR2(20) | N |  |  |
| 16 | IND_PROC | CHAR(1) | Y |  |  |

**PK**: ID_REG, DICIONARIO_ORIGEM, COD_EMPRESA, COD_ESTAB, COD_MOD, COD_SIT, CST_PIS, CST_COFINS, CFOP, COD_CTA, IND_TIPO_ALIQ, ALIQ_PIS, ALIQ_COFINS, NUM_PROC, INFO_COMPL

---

## EPC_DEDUCOES_DIVERSAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_ANO_COMP | DATE | N |  |  |
| 4 | IND_NAT_DED | CHAR(1) | N |  |  |
| 5 | IND_ORIGEM_DED | VARCHAR2(2) | N |  |  |
| 6 | CNPJ | VARCHAR2(14) | N |  |  |
| 7 | VLR_DED_PIS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DED_COFINS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BC_OPER | NUMBER(17,2) | Y |  |  |
| 10 | INF_COMPL | VARCHAR2(90) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | IDENT_SCP | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_ANO_COMP, IND_NAT_DED, IND_ORIGEM_DED, CNPJ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

---

## EPC_DEM_APUR_PIS_COFINS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_DEM | NUMBER(12) | N |  |  |
| 2 | ID_REG | NUMBER(12) | Y |  |  |
| 3 | ID_REG_M100_M500 | NUMBER(12) | Y |  |  |
| 4 | ID_REG_M105_M505 | NUMBER(12) | Y |  |  |
| 5 | ID_REG_M200_M600 | NUMBER(12) | Y |  |  |
| 6 | ID_REG_M210_M610 | NUMBER(12) | Y |  |  |
| 7 | COD_REGISTRO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LINHA | NUMBER(12) | Y |  |  |
| 9 | NUM_DOC | VARCHAR2(60) | Y |  |  |
| 10 | SER | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE | VARCHAR2(2) | Y |  |  |
| 12 | COD_PART | VARCHAR2(17) | Y |  |  |
| 13 | VL_DOC | NUMBER(17,2) | Y |  |  |
| 14 | VL_REC_BRT | NUMBER(17,2) | Y |  |  |
| 15 | VL_OPER | NUMBER(17,2) | Y |  |  |
| 16 | VL_TOT_REC | NUMBER(17,2) | Y |  |  |
| 17 | IND_CRED_ORI | CHAR(1) | Y |  |  |
| 18 | CFOP | VARCHAR2(4) | Y |  |  |
| 19 | NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 20 | COD_ITEM | VARCHAR2(62) | Y |  |  |
| 21 | VL_ITEM | NUMBER(17,2) | Y |  |  |
| 22 | CST_PIS | VARCHAR2(2) | Y |  |  |
| 23 | VL_BC_PIS | NUMBER(17,2) | Y |  |  |
| 24 | ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 25 | QUANT_BC_PIS | NUMBER(18,3) | Y |  |  |
| 26 | ALIQ_PIS_QUANT | NUMBER(19,4) | Y |  |  |
| 27 | VL_PIS | NUMBER(17,2) | Y |  |  |
| 28 | CST_COFINS | VARCHAR2(2) | Y |  |  |
| 29 | VL_BC_COFINS | NUMBER(17,2) | Y |  |  |
| 30 | ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 31 | QUANT_BC_COFINS | NUMBER(18,3) | Y |  |  |
| 32 | ALIQ_COFINS_QUANT | NUMBER(19,4) | Y |  |  |
| 33 | VL_COFINS | NUMBER(17,2) | Y |  |  |
| 34 | VL_PERC_RATEIO | NUMBER(12,6) | Y |  |  |
| 35 | VL_BC_PIS_RATEIO | NUMBER(17,2) | Y |  |  |
| 36 | QUANT_BC_PIS_RATEIO | NUMBER(18,3) | Y |  |  |
| 37 | VL_PIS_RATEIO | NUMBER(17,2) | Y |  |  |
| 38 | VL_BC_COFINS_RATEIO | NUMBER(17,2) | Y |  |  |
| 39 | QUANT_BC_COFINS_RATEIO | NUMBER(18,3) | Y |  |  |
| 40 | VL_COFINS_RATEIO | NUMBER(17,2) | Y |  |  |
| 41 | ID_REG_M400_M800 | NUMBER(12) | Y |  |  |
| 42 | ID_REG_M410_M810 | NUMBER(12) | Y |  |  |
| 43 | COD_NCM | VARCHAR2(10) | Y |  | Código do NCM |
| 44 | NOME_PART | VARCHAR2(70) | Y |  |  |
| 45 | COD_UNID_IMOB | VARCHAR2(11) | Y |  |  |
| 46 | COD_ADQUIRINTE | VARCHAR2(17) | Y |  |  |

**PK**: ID_REG_DEM

**Indexes**:
- IX_EPC_DEM_APUR_ID_REG: (ID_REG)
- IX_EPC_DEM_APUR_PIS_COFINS_01: (ID_REG_M200_M600, ID_REG_M210_M610)
- IX_EPC_DEM_APUR_PIS_COFINS_02: (ID_REG_M100_M500, ID_REG_M105_M505)
- IX_EPC_DEM_APUR_PIS_COFINS_03: (ID_REG_M400_M800, ID_REG_M410_M810)

---

## EPC_DET_REC_REG_CAIXA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | DICIONARIO_ORIGEM | VARCHAR2(5) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | COD_MOD | VARCHAR2(2) | N |  |  |
| 6 | IND_REC | VARCHAR2(2) | N |  |  |
| 7 | CNPJ_PARTICIPANTE | VARCHAR2(14) | N |  |  |
| 8 | NUM_DOC | VARCHAR2(60) | N |  |  |
| 9 | COD_ITEM | VARCHAR2(62) | N |  |  |
| 10 | CFOP | VARCHAR2(4) | N |  |  |
| 11 | CST_PIS | VARCHAR2(2) | N |  |  |
| 12 | CST_COFINS | VARCHAR2(2) | N |  |  |
| 13 | COD_CTA | VARCHAR2(70) | N |  |  |
| 14 | IND_TIPO_ALIQ | CHAR(1) | N |  |  |
| 15 | ALIQ_PIS | NUMBER(19,4) | N |  |  |
| 16 | ALIQ_COFINS | NUMBER(19,4) | N |  |  |
| 17 | INFO_COMPL | VARCHAR2(255) | N |  |  |
| 18 | VL_REC_DET | NUMBER(17,2) | Y |  |  |
| 19 | VL_DESC_PIS | NUMBER(17,2) | Y |  |  |
| 20 | VL_BC_PIS | NUMBER(17,2) | Y |  |  |
| 21 | VL_PIS | NUMBER(17,2) | Y |  |  |
| 22 | VL_DESC_COFINS | NUMBER(17,2) | Y |  |  |
| 23 | VL_BC_COFINS | NUMBER(17,2) | Y |  |  |
| 24 | VL_COFINS | NUMBER(17,2) | Y |  |  |
| 25 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 26 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 27 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 28 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 29 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 30 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |

**PK**: ID_REG, DICIONARIO_ORIGEM, COD_EMPRESA, COD_ESTAB, COD_MOD, IND_REC, CNPJ_PARTICIPANTE, NUM_DOC, COD_ITEM, CFOP, CST_PIS, CST_COFINS, COD_CTA, IND_TIPO_ALIQ, ALIQ_PIS, ALIQ_COFINS, INFO_COMPL

---

## EPC_DEV_VENDAS_REG_CUM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 3 | IDENT_ITEM_MERC | NUMBER(12) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | DATA_FISCAL | DATE | N |  |  |
| 10 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 11 | IND_PRODUTO | CHAR(1) | N |  |  |
| 12 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 13 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 14 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 15 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 16 | COD_SITUACAO_PIS_REF | NUMBER(2) | Y |  |  |
| 17 | VLR_PIS_REF | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_PIS_REF | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ALIQ_PIS_REF | NUMBER(7,4) | Y |  |  |
| 20 | COD_SITUACAO_COFINS_REF | NUMBER(2) | Y |  |  |
| 21 | VLR_COFINS_REF | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_COFINS_REF | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQ_COFINS_REF | NUMBER(7,4) | Y |  |  |
| 24 | IND_AJUSTE | CHAR(1) | Y |  |  |

**PK**: ID_REG, IDENT_DOCTO, IDENT_ITEM_MERC

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

---

## EPC_ESTAB_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |

---

## EPC_FOLHA_SALARIOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_ANO_APURACAO | DATE | Y |  |  |
| 4 | VLR_TOT_FOLHA_SALARIOS | NUMBER(17,2) | Y |  |  |
| 5 | VLR_TOT_EXCL_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TOT_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ALIQ_PIS_FOLHA_SAL | NUMBER(7,4) | Y |  |  |
| 8 | VLR_TOT_COFINS_FOLHA_SAL | NUMBER(17,2) | Y |  |  |
| 9 | IDENT_SCP | NUMBER(12) | Y |  |  |

**FKs**:
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- UK_EPC_FOLHA_SALARIOS (UNIQUE): (COD_EMPRESA, COD_ESTAB, MES_ANO_APURACAO, IDENT_SCP)

---

## EPC_IDENT_NAT_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_CST_PIS_COFINS | NUMBER(2) | N |  |  |
| 5 | COD_NAT_REC | NUMBER(3) | N |  |  |
| 6 | DATA_VALID_INI | DATE | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 8 | IDENT_NBM_INI | NUMBER(12) | Y |  |  |
| 9 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 10 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 11 | ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 12 | ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_PIS | NUMBER(19,4) | Y |  |  |
| 14 | VLR_COFINS | NUMBER(19,4) | Y |  |  |
| 15 | DATA_VALID_FIM | DATE | Y |  |  |
| 16 | IDENT_NBM_FIM | NUMBER(12) | Y |  |  |
| 17 | TIPO_PARAM | CHAR(1) | Y |  |  |
| 18 | DESCRICAO | VARCHAR2(400) | Y |  |  |
| 19 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: ID_REG

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NBM_INI → X2043_COD_NBM(IDENT_NBM)
- IDENT_NBM_FIM → X2043_COD_NBM(IDENT_NBM)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

**Indexes**:
- IX_EPC_IDENT_NAT_CONTA: (IDENT_CONTA)
- IX_EPC_IDENT_NAT_REC (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_CST_PIS_COFINS, DATA_VALID_INI, IDENT_PRODUTO, IDENT_NBM_INI, IDENT_SERVICO, IDENT_CFO, ALIQ_PIS, ALIQ_COFINS, VLR_PIS, VLR_COFINS, IDENT_CONTA)

---

## EPC_LINHAS_ARQUIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_ARQ | NUMBER(12) | Y |  |  |
| 2 | ID_REG | NUMBER(12) | Y |  |  |
| 3 | COD_BLOCO | VARCHAR2(2) | Y |  |  |
| 4 | COD_REGISTRO | VARCHAR2(4) | Y |  |  |
| 5 | DADOS_COMPL_REG | VARCHAR2(300) | Y |  |  |
| 6 | CHAVE_ORDENACAO | VARCHAR2(500) | Y |  |  |
| 7 | TEXTO | VARCHAR2(2000) | Y |  |  |

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

**Indexes**:
- IX_EPC_GERACAO: (COD_REGISTRO, COD_BLOCO, ID_REG)
- IX_EPC_LHARQ_COD_REG: (COD_BLOCO, COD_REGISTRO)
- IX_EPC_LINHAS_ARQUIVO: (ID_REG)

---

## EPC_LOG_SRV_S_NBC
**Comment**: Utilizada na geracao do log de servicos nao parametrizados com Natureza da Base do Credito

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 4 | COD_SERVICO | VARCHAR2(60) | N |  |  |
| 5 | IND_POSSUI_NAT_BCRED | VARCHAR2(1) | Y |  | Utilizado quando parametro de verificacao de preenchimento da nat_base_cred para servicos esta marcado. Estara preenchido qdo servico "S" para quando possui nat_base_cred e "N" para quando nao possui. Os logs serao gerados para os servicos que este indicador seja igual a "N" |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_SERVICO, COD_SERVICO

---

## EPC_PARAM_TP_CONTRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_TP_CONTRIB | VARCHAR2(2) | Y |  |  |
| 4 | COD_CST | NUMBER(2) | Y |  |  |
| 5 | COD_INC_TRIB | CHAR(1) | Y |  |  |
| 6 | IND_ALIQUOTA | CHAR(1) | Y |  |  |
| 7 | OP_ALIQ_PIS | VARCHAR2(1000) | Y |  |  |
| 8 | ALIQ_PIS | NUMBER(18,4) | Y |  |  |
| 9 | OP_ALIQ_COFINS | VARCHAR2(1000) | Y |  |  |
| 10 | ALIQ_COFINS | NUMBER(18,4) | Y |  |  |
| 11 | OP_VL_PIS | VARCHAR2(1000) | Y |  |  |
| 12 | VL_PIS | VARCHAR2(1000) | Y |  |  |
| 13 | OP_VL_COFINS | VARCHAR2(1000) | Y |  |  |
| 14 | VL_COFINS | VARCHAR2(1000) | Y |  |  |
| 15 | VALIDADE_INI | DATE | Y |  |  |
| 16 | VALIDADE_FIM | DATE | Y |  |  |
| 17 | IND_PARAM | CHAR(1) | Y |  |  |

**PK**: ID_REG

---

## EPC_PARAM_TP_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_TP_CRED | VARCHAR2(3) | Y |  |  |
| 4 | COD_CST | NUMBER(2) | Y |  |  |
| 5 | IND_ALIQUOTA | CHAR(1) | Y |  |  |
| 6 | ALIQ_PIS | NUMBER(18,4) | Y |  |  |
| 7 | ALIQ_COFINS | NUMBER(18,4) | Y |  |  |
| 8 | OP_ORIGEM | VARCHAR2(50) | Y |  |  |
| 9 | ORIGEM | VARCHAR2(50) | Y |  |  |
| 10 | OP_BASE_CREDITO | VARCHAR2(50) | Y |  |  |
| 11 | BASE_CREDITO | VARCHAR2(50) | Y |  |  |
| 12 | OP_PARTICIPANTE | VARCHAR2(50) | Y |  |  |
| 13 | PARTICIPANTE | VARCHAR2(50) | Y |  |  |
| 14 | OP_CFOP | VARCHAR2(50) | Y |  |  |
| 15 | CFOP | VARCHAR2(50) | Y |  |  |
| 16 | VALIDADE_INI | DATE | Y |  |  |
| 17 | VALIDADE_FIM | DATE | Y |  |  |
| 18 | IND_PARAM | CHAR(1) | Y |  |  |
| 19 | OP_ALIQ_PIS_COFINS | VARCHAR2(50) | Y |  |  |

**PK**: ID_REG

**Indexes**:
- IX_EPC_PARAM_TP_CRED: (IND_PARAM, COD_EMPRESA)

---

## EPC_PAR_CONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_CC | NUMBER(12) | N |  |  |
| 2 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 3 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 4 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 5 | DAT_VIG_INI | DATE | N |  |  |
| 6 | DAT_VIG_FIM | DATE | Y |  |  |

**PK**: IDENT_PAR_CC, IDENT_CONTA, DAT_VIG_INI

**FKs**:
- IDENT_PAR_CC → EPC_PAR_CONTA_CONTABIL(IDENT_PAR_CC)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_EPC_PAR_CTA: (IDENT_CONTA)

---

## EPC_PAR_CONTAS_FS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_FS | NUMBER(12) | N |  |  |
| 2 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**FKs**:
- IDENT_PAR_FS → EPC_PAR_FOLHA_SALARIO(IDENT_PAR_FS)

---

## EPC_PAR_CONTA_CONTABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_CC | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_SIT_TRIB_PIS | NUMBER(2) | N |  |  |
| 5 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 6 | COD_SIT_TRIB_COFINS | NUMBER(2) | N |  |  |
| 7 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 8 | COD_REC_DED_EXC | VARCHAR2(5) | N |  |  |
| 9 | COD_ATRIBUTO | VARCHAR2(3) | N | ' ' |  |
| 10 | COD_REC_DED_EXC_COMPL | VARCHAR2(20) | N |  |  |
| 11 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_CC

**Indexes**:
- IX_EPC_PAR_CONTA_CONTABIL (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_SIT_TRIB_PIS, COD_SIT_TRIB_COFINS, COD_REC_DED_EXC, COD_ATRIBUTO, COD_REC_DED_EXC_COMPL, COD_NAT_REC)

---

## EPC_PAR_CST_CONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_CADASTRO | DATE | N |  |  |
| 4 | IND_GER_CST | CHAR(1) | N |  |  |
| 5 | COD_CST | NUMBER(2) | N |  |  |
| 6 | GRUPO | VARCHAR2(9) | N |  |  |
| 7 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_CADASTRO, IND_GER_CST, COD_CST

---

## EPC_PAR_DSC_COMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DSC_COMP | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TRIB_PIS | NUMBER(2) | Y |  |  |
| 5 | COD_TRIB_COFINS | NUMBER(2) | Y |  |  |
| 6 | ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 7 | ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 8 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 9 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 10 | COD_TP_CRED | VARCHAR2(3) | Y |  |  |
| 11 | NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 12 | VALIDADE_INI | DATE | Y |  |  |
| 13 | DESC_COMPL | VARCHAR2(60) | Y |  |  |

**PK**: IDENT_DSC_COMP

**Indexes**:
- UK_EPC_PAR_DSC_COMP (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TRIB_PIS, COD_TRIB_COFINS, ALIQ_PIS, ALIQ_COFINS, VLR_ALIQ_PIS, VLR_ALIQ_COFINS, COD_TP_CRED, NAT_BC_CRED, VALIDADE_INI)

---

## EPC_PAR_DSC_COMP_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TP_CRED | VARCHAR2(3) | N |  |  |
| 4 | NAT_BC_CRED | VARCHAR2(2) | N |  |  |
| 5 | VALIDADE_INI | DATE | N |  |  |
| 6 | DESC_COMPL | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TP_CRED, NAT_BC_CRED, VALIDADE_INI

---

## EPC_PAR_FOLHA_SALARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_FS | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IND_VALOR | CHAR(1) | Y | '1' |  |
| 5 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_FS

---

## EPC_PAR_IND_PROD_0200

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | DATA_VALID | DATE | N |  |  |
| 6 | TIPO_DO_ITEM | VARCHAR2(2) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | DAT_OPERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, DATA_VALID

---

## EPC_PAR_NCM_0200

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_NBM | VARCHAR2(4) | N |  |  |
| 4 | DATA_VALID | DATE | N |  |  |
| 5 | TIPO_DO_ITEM | VARCHAR2(2) | Y |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |
| 7 | DAT_OPERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_NBM, DATA_VALID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EPC_PAR_PROD_0200

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | DATA_VALID | DATE | N |  |  |
| 7 | TIPO_DO_ITEM | VARCHAR2(2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | DAT_OPERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_VALID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EPC_PER_DISPENSADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 3 | MES_DISPENSA | VARCHAR2(2) | N |  |  |
| 4 | IND_DISPENSA | CHAR(1) | N |  |  |
| 5 | INF_COMP | VARCHAR2(90) | Y |  |  |
| 6 | MES_APRESENT | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, ANO_CALENDARIO, MES_APRESENT, MES_DISPENSA

---

## EPC_PROC_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | N |  |  |
| 2 | GRUPO_PROC_REF | VARCHAR2(9) | N |  |  |
| 3 | NUM_PROC_REF | VARCHAR2(20) | N |  |  |

**PK**: PROC_ID, GRUPO_PROC_REF, NUM_PROC_REF

---

## EPC_RATEIO_CRED_COMUM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | DATA_COMPET | DATE | Y |  |  |
| 3 | VLR_REC_NC_TRIB_MEC_INT | NUMBER(17,2) | Y |  |  |
| 4 | VLR_REC_NC_NTRIB_MEC_INT | NUMBER(17,2) | Y |  |  |
| 5 | VLR_REC_NC_EXPORT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_REC_BRUTA_CUM | NUMBER(17,2) | Y |  |  |
| 7 | VLR_REC_BRUTA_TOT | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IDENT_SCP | NUMBER(12) | Y |  |  |

**FKs**:
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- UK_EPC_RATEIO_CRED_COMUM (UNIQUE): (COD_EMPRESA, DATA_COMPET, IDENT_SCP)

---

## EPC_RECEITA_BRUTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | REC_TOTAL_BLOCO_A | NUMBER(17,2) | Y |  |  |
| 5 | REC_NRB_BLOCO_A | NUMBER(17,2) | Y |  |  |
| 6 | REC_TOTAL_BLOCO_C | NUMBER(17,2) | Y |  |  |
| 7 | REC_NRB_BLOCO_C | NUMBER(17,2) | Y |  |  |
| 8 | REC_TOTAL_BLOCO_D | NUMBER(17,2) | Y |  |  |
| 9 | REC_NRB_BLOCO_D | NUMBER(17,2) | Y |  |  |
| 10 | REC_TOTAL_BLOCO_F | NUMBER(17,2) | Y |  |  |
| 11 | REC_NRB_BLOCO_F | NUMBER(17,2) | Y |  |  |
| 12 | REC_TOTAL_BLOCO_I | NUMBER(17,2) | Y |  |  |
| 13 | REC_NRB_BLOCO_I | NUMBER(17,2) | Y |  |  |
| 14 | REC_TOTAL_BLOCO_1 | NUMBER(17,2) | Y |  |  |
| 15 | REC_NRB_BLOCO_1 | NUMBER(17,2) | Y |  |  |
| 16 | REC_TOTAL_PERIODO | NUMBER(17,2) | Y |  |  |
| 17 | REC_TOTAL_NRB_PERIODO | NUMBER(17,2) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**Indexes**:
- UK_EPC_RECEITA_BRUTA (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_APUR)

---

## EPC_REC_DED_EXC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_REC_DED_EXC | VARCHAR2(5) | N |  |  |
| 2 | COD_ATRIBUTO | VARCHAR2(3) | N | ' ' |  |
| 3 | DESCRICAO | VARCHAR2(500) | N |  |  |
| 4 | TIPO_CODIGO | CHAR(1) | Y |  |  |
| 5 | FATOR | NUMBER(7,4) | Y |  |  |
| 6 | APLICABILIDADE | CHAR(1) | Y |  |  |

**PK**: COD_REC_DED_EXC, COD_ATRIBUTO

---

## EPC_REC_DED_EXC_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_REC_DED_EXC_COMPL | VARCHAR2(20) | N |  |  |
| 2 | DATA_VALIDADE | DATE | N |  |  |
| 3 | DESCRICAO | VARCHAR2(500) | N |  |  |

**PK**: COD_REC_DED_EXC_COMPL

---

## EPC_REG_AJT_1100_1500
**Comment**: Tabela do EFD-PIS-COFINS que armazena os registros 1100 e 1500.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_1100_1500 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REG_AJT_1100_1500 |
| 2 | ID_REG | NUMBER(12) | N |  | identificador da apuracao - EPC_APURACAO |
| 3 | COD_REG | VARCHAR2(10) | N |  | Campo 01 do reg 1100/1500 - codigo identificador do registro. Dominio: 1100, 1500 |
| 4 | PER_APU_CRED | VARCHAR2(7) | N |  | Campo 02 do reg 1100/1500 - Periodo de Apuracao (MM/AAAA) |
| 5 | ORIG_CRED | VARCHAR2(2) | N |  | Campo 03 do reg 1100/1500 - Indicador de Origem do Credito. Dominio: 01 - operacoes proprias; 02 - credito transferido por pessoa juridica sucedida |
| 6 | CNPJ_SUC | VARCHAR2(14) | N |  | Campo 04 do reg 1100/1500 - CNPJ da Pessoa Juricia cedente do credito. Preenchida quando ORIG_CRED = 02 |
| 7 | COD_CRED | VARCHAR2(3) | N |  | Campo 05 do reg 1100/1500 - Codigo do Tipo do Credito - origem EPC_COD_CRED_TRANS - TFIX93 |
| 8 | VL_CRED_APU | NUMBER(17,2) | Y |  | Campo 06 do reg 1100/1500 - Valor do Credito Apurado. |
| 9 | VL_CRED_EXT_APU | NUMBER(17,2) | Y |  | Campo 07 do reg 1100/1500 - Valor do Credito Extemporaneo Apurado. |
| 10 | VL_TOT_CRED_APU | NUMBER(17,2) | Y |  | Campo 08 do reg 1100/1500 - Valor Total do Credito Apurado. |
| 11 | VL_CRED_DESC_PA_ANT | NUMBER(17,2) | Y |  |  |
| 12 | VL_CRED_PER_PA_ANT | NUMBER(17,2) | Y |  |  |
| 13 | VL_CRED_DCOMP_PA_ANT | NUMBER(17,2) | Y |  |  |
| 14 | SD_CRED_DISP_EFD | NUMBER(17,2) | Y |  |  |
| 15 | VL_CRED_DESC_EFD | NUMBER(17,2) | Y |  |  |
| 16 | VL_CRED_PER_EFD | NUMBER(17,2) | Y |  |  |
| 17 | VL_CRED_DCOMP_EFD | NUMBER(17,2) | Y |  |  |
| 18 | VL_CRED_TRANS | NUMBER(17,2) | Y |  |  |
| 19 | VL_CRED_OUT | NUMBER(17,2) | Y |  |  |
| 20 | SLD_CRED_FIM | NUMBER(17,2) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  | Indicador de Gravacao. Dominio: 4 - incluido manualmente; 6 - gerado pelo sistema. |
| 22 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 23 | PER_APURADO | VARCHAR2(7) | Y |  |  |

**PK**: ID_REG_1100_1500

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

**Indexes**:
- IU_EPC_REG_AJT_1100_1500 (UNIQUE): (ID_REG, COD_REG, PER_APU_CRED, ORIG_CRED, CNPJ_SUC, COD_CRED)

---

## EPC_REG_AJT_I100

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_I100 | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_CST_PIS_COFINS | NUMBER(2) | N |  |  |
| 5 | VLR_RECEITA | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TOT_GERAL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TOT_ESPEC | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_CALC_PIS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 10 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_CALC_COFINS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 14 | DSC_INF_COMPL | VARCHAR2(150) | Y |  |  |
| 15 | DAT_INI | DATE | Y |  |  |
| 16 | DAT_FIM | DATE | Y |  |  |

**PK**: ID_REG_I100

---

## EPC_REG_AJT_I199

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_I100 | NUMBER(12) | N |  |  |
| 2 | ID_REG_I199 | NUMBER(12) | N |  |  |
| 3 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 4 | ORIG_PROCESSO | CHAR(1) | Y |  |  |

**PK**: ID_REG_I199

**FKs**:
- ID_REG_I100 → EPC_REG_AJT_I100(ID_REG_I100)
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)

---

## EPC_REG_AJT_I200

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_I100 | NUMBER(12) | N |  |  |
| 2 | ID_REG_I200 | NUMBER(12) | N |  |  |
| 3 | NUM_CAMPO | VARCHAR2(2) | N |  |  |
| 4 | COD_REC_DED_EXC | VARCHAR2(5) | Y |  |  |
| 5 | VLR_DETALHADO | NUMBER(17,2) | Y |  |  |
| 6 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 7 | DSC_INF_COMPL | VARCHAR2(150) | Y |  |  |
| 8 | COD_ATRIBUTO | VARCHAR2(3) | Y |  |  |

**PK**: ID_REG_I200

**FKs**:
- ID_REG_I100 → EPC_REG_AJT_I100(ID_REG_I100)
- COD_REC_DED_EXC, COD_ATRIBUTO → EPC_REC_DED_EXC(COD_REC_DED_EXC, COD_ATRIBUTO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_EPC_REG_AJT_I200_CTA: (IDENT_CONTA)

---

## EPC_REG_AJT_I299

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_I200 | NUMBER(12) | N |  |  |
| 2 | ID_REG_I299 | NUMBER(12) | N |  |  |
| 3 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 4 | ORIG_PROCESSO | CHAR(1) | Y |  |  |

**PK**: ID_REG_I299

**FKs**:
- ID_REG_I200 → EPC_REG_AJT_I200(ID_REG_I200)
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)

---

## EPC_REG_AJT_I300

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_I200 | NUMBER(12) | N |  |  |
| 2 | ID_REG_I300 | NUMBER(12) | N |  |  |
| 3 | COD_REC_DED_EXC_COMPL | VARCHAR2(20) | Y |  |  |
| 4 | VLR_DETALHADO | NUMBER(17,2) | Y |  |  |
| 5 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 6 | DSC_INF_COMPL | VARCHAR2(150) | Y |  |  |

**PK**: ID_REG_I300

**FKs**:
- ID_REG_I200 → EPC_REG_AJT_I200(ID_REG_I200)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_EPC_REG_AJT_I300_CTA: (IDENT_CONTA)

---

## EPC_REG_AJT_I399

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_I300 | NUMBER(12) | N |  |  |
| 2 | ID_REG_I399 | NUMBER(12) | N |  |  |
| 3 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 4 | ORIG_PROCESSO | CHAR(1) | Y |  |  |

**PK**: ID_REG_I399

**FKs**:
- ID_REG_I300 → EPC_REG_AJT_I300(ID_REG_I300)
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)

---

## EPC_REG_AJT_M100_M500

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | ID_REG_M100_M500 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | Y |  |  |
| 4 | COD_CRED | VARCHAR2(3) | Y |  |  |
| 5 | IND_CRED_ORI | CHAR(1) | Y |  |  |
| 6 | IND_DESC_CRED | CHAR(1) | Y |  |  |
| 7 | VL_BC | NUMBER(17,2) | Y |  |  |
| 8 | ALIQ | NUMBER(7,4) | Y |  |  |
| 9 | QUANT_BC | NUMBER(18,3) | Y |  |  |
| 10 | ALIQ_QUANT | NUMBER(19,4) | Y |  |  |
| 11 | VL_CRED | NUMBER(17,2) | Y |  |  |
| 12 | VL_AJUS_ACRES | NUMBER(17,2) | Y |  |  |
| 13 | VL_AJUS_REDUC | NUMBER(17,2) | Y |  |  |
| 14 | VL_CRED_DIF | NUMBER(17,2) | Y |  |  |
| 15 | VL_CRED_DISP | NUMBER(17,2) | Y |  |  |
| 16 | VL_CRED_DESC | NUMBER(17,2) | Y |  |  |
| 17 | SLD_CRED | NUMBER(17,2) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 19 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M100_M500

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

---

## EPC_REG_AJT_M105_M505

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M100_M500 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M105_M505 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | Y |  |  |
| 4 | NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 5 | COD_CST | VARCHAR2(3) | Y |  |  |
| 6 | VL_BC_TOT | NUMBER(17,2) | Y |  |  |
| 7 | VL_BC_CUM | NUMBER(17,2) | Y |  |  |
| 8 | VL_BC_NC | NUMBER(17,2) | Y |  |  |
| 9 | VL_BC | NUMBER(17,2) | Y |  |  |
| 10 | QUANT_BC_TOT | NUMBER(18,3) | Y |  |  |
| 11 | QUANT_BC | NUMBER(18,3) | Y |  |  |
| 12 | DSC_CRED | VARCHAR2(60) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 14 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M105_M505

**FKs**:
- ID_REG_M100_M500 → EPC_REG_AJT_M100_M500(ID_REG_M100_M500)

---

## EPC_REG_AJT_M110_M510

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M100_M500 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M110_M510 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | Y |  |  |
| 4 | IND_AJ | CHAR(1) | Y |  |  |
| 5 | COD_AJ | VARCHAR2(2) | Y |  |  |
| 6 | DT_REF | DATE | Y |  |  |
| 7 | VL_AJ | NUMBER(17,2) | Y |  |  |
| 8 | NUM_DOC | VARCHAR2(100) | Y |  |  |
| 9 | DSC_AJ | VARCHAR2(400) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 11 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M110_M510

**FKs**:
- ID_REG_M100_M500 → EPC_REG_AJT_M100_M500(ID_REG_M100_M500)

**Indexes**:
- IDX_EPC_REG_AJT_M110_M51001: (ID_REG_M100_M500)

---

## EPC_REG_AJT_M115_M515

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M110_M510 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M115_M515 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(3) | N |  |  |
| 4 | VL_DET | NUMBER(17,2) | Y |  |  |
| 5 | COD_CST | VARCHAR2(3) | Y |  |  |
| 6 | VL_BC_DET | NUMBER(17,3) | Y |  |  |
| 7 | ALIQ_DET | NUMBER(8,4) | Y |  |  |
| 8 | DT_OPER | DATE | Y |  |  |
| 9 | DSC_OPER | VARCHAR2(400) | Y |  |  |
| 10 | COD_CTA | VARCHAR2(70) | Y |  |  |
| 11 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 12 | DSC_INF_COMP | VARCHAR2(400) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M115_M515

**FKs**:
- ID_REG_M110_M510 → EPC_REG_AJT_M110_M510(ID_REG_M110_M510)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IU_EPC_REG_AJT_M115_M515 (UNIQUE): (ID_REG_M110_M510, COD_REG, VL_DET, COD_CST, ALIQ_DET, DT_OPER, IDENT_CONTA)
- IX_EPC_REG_AJT_M115_CTA: (IDENT_CONTA)

---

## EPC_REG_AJT_M200_M600

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | ID_REG_M200_M600 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | Y |  |  |
| 4 | VL_TOT_CONT_NC_PER | NUMBER(17,2) | Y |  |  |
| 5 | VL_TOT_CRED_DESC | NUMBER(17,2) | Y |  |  |
| 6 | VL_TOT_CRED_DESC_ANT | NUMBER(17,2) | Y |  |  |
| 7 | VL_TOT_CONT_NC_DEV | NUMBER(17,2) | Y |  |  |
| 8 | VL_RET_NC | NUMBER(17,2) | Y |  |  |
| 9 | VL_OUT_DED_NC | NUMBER(17,2) | Y |  |  |
| 10 | VL_CONT_NC_REC | NUMBER(17,2) | Y |  |  |
| 11 | VL_TOT_CONT_CUM_PER | NUMBER(17,2) | Y |  |  |
| 12 | VL_RET_CUM | NUMBER(17,2) | Y |  |  |
| 13 | VL_OUT_DED_CUM | NUMBER(17,2) | Y |  |  |
| 14 | VL_CONT_CUM_REC | NUMBER(17,2) | Y |  |  |
| 15 | VL_TOT_CONT_REC | NUMBER(17,2) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 17 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 18 | ID_GER | NUMBER(12) | Y |  |  |
| 19 | SEQ_GER_ARQ | NUMBER(12) | Y |  |  |
| 20 | TXT_GER_ARQ | VARCHAR2(4000) | Y |  |  |

**PK**: ID_REG_M200_M600

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

---

## EPC_REG_AJT_M205_M605

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M200_M600 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M205_M605 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | NUM_CAMPO | VARCHAR2(2) | N |  |  |
| 5 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 6 | VL_DEB | NUMBER(17,2) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 8 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M205_M605

**FKs**:
- ID_REG_M200_M600 → EPC_REG_AJT_M200_M600(ID_REG_M200_M600)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)

---

## EPC_REG_AJT_M210_M610

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M200_M600 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M210_M610 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | COD_CONT | VARCHAR2(4) | N |  |  |
| 5 | VL_REC_BRT | NUMBER(17,2) | Y |  |  |
| 6 | VL_BC_CONT | NUMBER(17,2) | Y |  |  |
| 7 | ALIQ_PIS | NUMBER(8,4) | Y |  |  |
| 8 | QUANT_BC_PIS | NUMBER(17,3) | Y |  |  |
| 9 | ALIQ_PIS_QUANT | NUMBER(19,4) | Y |  |  |
| 10 | VL_CONT_APUR | NUMBER(17,2) | Y |  |  |
| 11 | VL_AJUS_ACRES | NUMBER(17,2) | Y |  |  |
| 12 | VL_AJUS_REDUC | NUMBER(17,2) | Y |  |  |
| 13 | VL_CONT_DIFER | NUMBER(17,2) | Y |  |  |
| 14 | VL_CONT_DIFER_ANT | NUMBER(17,2) | Y |  |  |
| 15 | VL_CONT_PER | NUMBER(17,2) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 17 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 18 | VL_AJUS_ACRES_BC | NUMBER(17,2) | Y |  |  |
| 19 | VL_AJUS_REDUC_BC | NUMBER(17,2) | Y |  |  |
| 20 | VL_BC_CONT_AJUS | NUMBER(17,2) | Y |  |  |

**PK**: ID_REG_M210_M610

**FKs**:
- ID_REG_M200_M600 → EPC_REG_AJT_M200_M600(ID_REG_M200_M600)

---

## EPC_REG_AJT_M211_M611

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M210_M610 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M211_M611 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | IND_TIP_COOP | VARCHAR2(2) | N |  |  |
| 5 | VL_BC_CONT_ANT_EXC_COOP | NUMBER(17,2) | N |  |  |
| 6 | VL_EXC_COOP_GER | NUMBER(17,2) | N |  |  |
| 7 | VL_EXC_ESP_COOP | NUMBER(17,2) | N |  |  |
| 8 | VL_BC_CONT | NUMBER(17,2) | N |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 10 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M211_M611

**FKs**:
- ID_REG_M210_M610 → EPC_REG_AJT_M210_M610(ID_REG_M210_M610)

**Indexes**:
- IU_EPC_REG_AJT_M211_M611 (UNIQUE): (ID_REG_M210_M610, COD_REG, IND_TIP_COOP)

---

## EPC_REG_AJT_M215_M615

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M210_M610 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M215_M615 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | IND_AJ_BC | VARCHAR2(1) | N |  |  |
| 5 | VL_AJ_BC | NUMBER(17,2) | N |  |  |
| 6 | COD_AJ | VARCHAR2(2) | N |  |  |
| 7 | NUM_PROC | VARCHAR2(100) | Y |  |  |
| 8 | DSC_AJ_BC | VARCHAR2(400) | Y |  |  |
| 9 | DT_REF | DATE | Y |  |  |
| 10 | COD_CTA | VARCHAR2(70) | Y |  |  |
| 11 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 12 | CNPJ | VARCHAR2(14) | Y |  |  |
| 13 | DSC_INF_COMP | VARCHAR2(400) | Y |  |  |
| 14 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 15 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M215_M615

**FKs**:
- ID_REG_M210_M610 → EPC_REG_AJT_M210_M610(ID_REG_M210_M610)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IU_EPC_REG_AJT_M215_M615: (ID_REG_M210_M610, COD_REG, IND_AJ_BC, COD_AJ, NUM_PROC)
- IX_EPC_REG_AJT_M215_CTA: (IDENT_CONTA)

---

## EPC_REG_AJT_M220_M620

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M210_M610 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M220_M620 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | IND_AJ | CHAR(1) | Y |  |  |
| 5 | VL_AJ | NUMBER(17,2) | Y |  |  |
| 6 | COD_AJ | VARCHAR2(10) | Y |  |  |
| 7 | NUM_DOC | VARCHAR2(100) | Y |  |  |
| 8 | DESCR_AJ | VARCHAR2(400) | Y |  |  |
| 9 | DT_REF | DATE | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 11 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 12 | IND_AJUST | CHAR(1) | Y |  |  |

**PK**: ID_REG_M220_M620

**FKs**:
- ID_REG_M210_M610 → EPC_REG_AJT_M210_M610(ID_REG_M210_M610)

---

## EPC_REG_AJT_M225_M625

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M220_M620 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M225_M625 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | VL_DET | NUMBER(17,2) | Y |  |  |
| 5 | COD_CST | VARCHAR2(3) | Y |  |  |
| 6 | VL_BC_DET | NUMBER(17,3) | Y |  |  |
| 7 | ALIQ_DET | NUMBER(8,4) | Y |  |  |
| 8 | DT_OPER | DATE | Y |  |  |
| 9 | DSC_OPER | VARCHAR2(400) | Y |  |  |
| 10 | COD_CTA | VARCHAR2(70) | Y |  |  |
| 11 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 12 | DSC_INF_COMP | VARCHAR2(400) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 15 | IND_AJUST | CHAR(1) | Y |  |  |

**PK**: ID_REG_M225_M625

**FKs**:
- ID_REG_M220_M620 → EPC_REG_AJT_M220_M620(ID_REG_M220_M620)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IU_EPC_REG_AJT_M225_M625 (UNIQUE): (ID_REG_M220_M620, COD_REG, VL_DET, COD_CST, ALIQ_DET, DT_OPER, IDENT_CONTA, DSC_OPER, DSC_INF_COMP)
- IX_EPC_REG_AJT_M225_CTA: (IDENT_CONTA)

---

## EPC_REG_AJT_M230_M630

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M210_M610 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M230_M630 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | CNPJ | VARCHAR2(14) | N |  |  |
| 5 | VL_VEND | NUMBER(17,2) | N |  |  |
| 6 | VL_NAO_RECEB | NUMBER(17,2) | N |  |  |
| 7 | VL_CONT_DIF | NUMBER(17,2) | N |  |  |
| 8 | VL_CRED_DIF | NUMBER(17,2) | N |  |  |
| 9 | COD_CRED | VARCHAR2(3) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 11 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M230_M630

**FKs**:
- ID_REG_M210_M610 → EPC_REG_AJT_M210_M610(ID_REG_M210_M610)

**Indexes**:
- IU_EPC_REG_AJT_M230_M630 (UNIQUE): (ID_REG_M210_M610, COD_REG, CNPJ, COD_CRED)

---

## EPC_REG_AJT_M300_M700
**Comment**: Tabela do EFD-PIS-COFINS que armazena os registros M300 e M700. O registro M300 não é filho do M210. Assim como o M700        não é filho do M610. Apesar disto, a tabela foi criada como filha do M210_M610, pois ha uma consolidacao do M300 no M210 - campo 12 e        do M700 no M610 - campo 12.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M210_M610 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M300_M700 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REG_AJT_M300_M700. |
| 3 | COD_REG | VARCHAR2(10) | N |  | Campo obrigatorio que fazer parte da chave lógica (ID_REG_M210_M610, COD_REG, PER_APUR, DT_RECEB, NAT_CRED_DESC). Dominio: 300, 700 |
| 4 | PER_APUR | DATE | N |  | Campo obrigatorio que fazer parte da chave lógica (ID_REG_M210_M610, COD_REG, PER_APUR, DT_RECEB, NAT_CRED_DESC). |
| 5 | DT_RECEB | DATE | Y |  | Campo nao obrigatorio que fazer parte da chave lógica (ID_REG_M210_M610, COD_REG, PER_APUR, DT_RECEB, NAT_CRED_DESC). |
| 6 | NAT_CRED_DESC | VARCHAR2(2) | Y |  | Campo nao e obrigatorio que fazer parte da chave lógica (ID_REG_M210_M610, COD_REG, PER_APUR, DT_RECEB, NAT_CRED_DESC). |
| 7 | VL_CONT_APUR_DIFER | NUMBER(17,2) | Y |  |  |
| 8 | VL_CRED_DESC_DIFER | NUMBER(17,2) | Y |  |  |
| 9 | VL_CONT_DIFER_ANT | NUMBER(17,2) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 11 | TEXTO | VARCHAR2(100) | Y |  |  |

**PK**: ID_REG_M300_M700

**FKs**:
- ID_REG_M210_M610 → EPC_REG_AJT_M210_M610(ID_REG_M210_M610)

**Indexes**:
- IU_EPC_REG_AJT_M300_M700 (UNIQUE): (ID_REG_M210_M610, COD_REG, PER_APUR, DT_RECEB, NAT_CRED_DESC)

---

## EPC_REG_AJT_M400_M800

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG | NUMBER(12) | N |  |  |
| 2 | ID_REG_M400_M800 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | Y |  |  |
| 4 | COD_CST | VARCHAR2(3) | Y |  |  |
| 5 | VL_TOT_REC | NUMBER(17,2) | Y |  |  |
| 6 | COD_CTA | VARCHAR2(60) | Y |  |  |
| 7 | DESC_COMPL | VARCHAR2(60) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 9 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M400_M800

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

---

## EPC_REG_AJT_M410_M810

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M400_M800 | NUMBER(12) | N |  |  |
| 2 | ID_REG_M410_M810 | NUMBER(12) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | NAT_REC | VARCHAR2(4) | Y |  |  |
| 5 | VL_REC | NUMBER(17,2) | Y |  |  |
| 6 | COD_CTA | VARCHAR2(60) | Y |  |  |
| 7 | DESC_COMPL | VARCHAR2(60) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | N |  |  |
| 9 | TEXTO | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_M410_M810

**FKs**:
- ID_REG_M400_M800 → EPC_REG_AJT_M400_M800(ID_REG_M400_M800)

---

## EPC_REG_AJT_P210

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_COMPETENCIA | DATE | Y |  |  |
| 4 | PERIODO_REF | DATE | Y |  |  |
| 5 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 6 | IND_AJ | CHAR(1) | Y |  |  |
| 7 | VL_AJ | NUMBER(17,2) | Y |  |  |
| 8 | COD_AJ | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOC | VARCHAR2(100) | Y |  |  |
| 10 | DSC_AJ | VARCHAR2(400) | Y |  |  |
| 11 | DT_REF | DATE | Y |  |  |
| 12 | IDENT_SCP | NUMBER(12) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)

**Indexes**:
- UK_EPC_REG_AJT_P210 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_COMPETENCIA, PERIODO_REF, COD_RECEITA, IND_AJ, COD_AJ, NUM_DOC, IDENT_SCP)

---

## EPC_REG_LINHAS_ARQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_ARQ | NUMBER(12) | N |  |  |
| 2 | SEQ_EXEC | VARCHAR2(80) | N |  |  |
| 3 | ID_REG | NUMBER(12) | N |  |  |
| 4 | COD_REG | VARCHAR2(10) | Y |  |  |
| 5 | NOME_ARQ | VARCHAR2(100) | Y |  |  |
| 6 | LINHA_ARQ | VARCHAR2(2000) | Y |  |  |

**PK**: ID_REG_ARQ

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

**Indexes**:
- IX_EPC_REG_LINHAS_ARQ: (SEQ_EXEC, ID_REG, COD_REG)

---

## EPC_REG_TOT_CNPJ_M100_M500
**Comment**: Tabela do EFD-PIS-COFINS, filha da EPC_REG_AJT_M100_M500 que totaliza por CNPJ os valores dos créditos dos registros M100 e M500.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_M100_M500 | NUMBER(12) | N |  |  |
| 2 | CNPJ | VARCHAR2(14) | N |  |  |
| 3 | IND_DESC_CRED | CHAR(1) | Y |  |  |
| 4 | VL_CRED | NUMBER(17,2) | Y |  |  |
| 5 | VL_AJUS_ACRES | NUMBER(17,2) | Y |  |  |
| 6 | VL_AJUS_REDUC | NUMBER(17,2) | Y |  |  |
| 7 | VL_CRED_DIF | NUMBER(17,2) | Y |  |  |
| 8 | VL_CRED_DISP | NUMBER(17,2) | Y |  |  |
| 9 | VL_CRED_DESC | NUMBER(17,2) | Y |  |  |
| 10 | SLD_CRED | NUMBER(17,2) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: ID_REG_M100_M500, CNPJ

**FKs**:
- ID_REG_M100_M500 → EPC_REG_AJT_M100_M500(ID_REG_M100_M500)

---

## EPC_REG_TOT_RET_F600
**Comment**: Tabela do EFD-PIS-COFINS que totalizados por Natureza da Retencao, Natureza da Receita e Condicao da PJ Declarante, os valores retidos na fonte do Pis e Cofins gerados no registro F600.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_TOT_RET | NUMBER(12) | N |  | sequencial unico |
| 2 | ID_REG | NUMBER(12) | N |  | identificador da apuracao que gerou o valor da retencao |
| 3 | COD_PIS_COFINS | VARCHAR2(10) | N |  | codigo que identifica se o valor da retencao apurado é do PIS ou do COFINS. Dominio: PIS, COFINS |
| 4 | COD_RET_FONTE | VARCHAR2(2) | N |  | Codigo Indicador de Natureza da Retencao na Fonte. Origem X145_CONTRIB_RET_FONTE, campo COD_RET_FONTE. Dominio: 01, 02, 03, 04, 05, 99. |
| 5 | IND_NAT_REC | CHAR(1) | N |  | Indicador da Natureza da Receita. Origem X145_CONTRIB_RET_FONTE, campo IND_NAT_REC. Dominio: 0 - receita nao cumulativa; 1 - receita cumulativa. |
| 6 | IND_COND_PJ_DECL | CHAR(1) | N |  | Indicador da condicao da pessoa juridica declarante. Origem X145_CONTRIB_RET_FONTE, campo IND_COND_PJ_DECL. Dominio: 0 – Beneficiaria da Retencao/Recolhimento; 1- Responsavel pela Retencao/Recolhimento |
| 7 | VLR_RET_APUR | NUMBER(17,2) | Y |  | Valor da Retencao Apurado - Originario do F600. Origem X145_CONTRIB_RET_FONTE, campos VLR_RET_FONTE_PIS e VLR_RET_FONTE_COFINS. |
| 8 | VLR_RET_UTIL_DED | NUMBER(17,2) | Y |  | valor total da retencao utilizado para deducao na contribuicao. Valor da retencao utilizado na propria apuracao que gerou a retencao. |
| 9 | VLR_RET_DISP | NUMBER(17,2) | Y |  | Valor da Retencao Disponivel para ser utilizado (VLR_RET_APUR - VLR_RET_UTIL_DED). |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  | Indicador de Gravacao. Dominio: 4 - incluido manualmente; 6 - gerado pelo sistema. |

**PK**: ID_REG_TOT_RET

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)

**Indexes**:
- IU_EPC_REG_TOT_RET_F600 (UNIQUE): (ID_REG, COD_PIS_COFINS, COD_RET_FONTE, IND_NAT_REC, IND_COND_PJ_DECL)

---

## EPC_REST_AJT_M110_M510
**Comment**: Tabela de restauracao dos registros M110 e M510 

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M110_M510 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REST_AJT_M110_M510 |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | empresa referente a apuracao - EPC_APURACAO |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | estabelecimento referente a apuracao - EPC_APURACAO |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | tipo de livro referente a apuracao - EPC_APURACAO |
| 5 | DAT_APUR_INI | DATE | N |  | data inicial referente a apuracao - EPC_APURACAO |
| 6 | DAT_APUR_FIM | DATE | N |  | data final referente a apuracao - EPC_APURACAO |
| 7 | COD_REG_M100_M500 | VARCHAR2(10) | Y |  | codigo do registro pai M100, M500 - EPC_REG_AJT_M100_M500 |
| 8 | COD_CRED_M100_M500 | VARCHAR2(3) | Y |  | codigo do tipo de credito do registro pai M100, M500  - EPC_REG_AJT_M100_M500 |
| 9 | IND_CRED_ORI_M100_M500 | CHAR(1) | Y |  | indicador de origem do credito do registro pai M100, M500  - EPC_REG_AJT_M100_M500 |
| 10 | ALIQ_M100_M500 | NUMBER(7,4) | Y |  | alíquota do Pis/Cofins do registro pai M100, M500  - EPC_REG_AJT_M100_M500 |
| 11 | ALIQ_QUANT_M100_M500 | NUMBER(19,4) | Y |  | alíquota em reais do Pis/Cofins do registro pai M100, M500  - EPC_REG_AJT_M100_M500 |
| 12 | COD_REG | VARCHAR2(10) | Y |  | codigo dos registros M110, M510  - EPC_REG_AJT_M110_M510 |
| 13 | IND_AJ | CHAR(1) | Y |  | tipo de ajuste dos registros M110, M510  - EPC_REG_AJT_M110_M510 |
| 14 | COD_AJ | VARCHAR2(2) | Y |  | codigo do ajuste dos registros M110, M510  - EPC_REG_AJT_M110_M510 |
| 15 | DT_REF | DATE | Y |  | data referencia dos registros M110, M510  - EPC_REG_AJT_M110_M510 |
| 16 | VL_AJ | NUMBER(17,2) | Y |  | valor do ajuste dos registros M110, M510  - EPC_REG_AJT_M110_M510 |
| 17 | NUM_DOC | VARCHAR2(100) | Y |  | numero do documento/processo dos registros M110, M510  - EPC_REG_AJT_M110_M510 |
| 18 | DSC_AJ | VARCHAR2(400) | Y |  | descricao resumida dos registros M110, M510  - EPC_REG_AJT_M110_M510 |
| 19 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 20 | IND_GRAVACAO | CHAR(1) | Y | '1' |  |
| 21 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: ID_REST_M110_M510

**Indexes**:
- IU_EPC_REST_AJT_M110_M510 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_REG_M100_M500, COD_CRED_M100_M500, IND_CRED_ORI_M100_M500, ALIQ_M100_M500, ALIQ_QUANT_M100_M500, COD_REG, IND_AJ, COD_AJ, NUM_DOC, DSC_AJ, COD_SCP)

---

## EPC_REST_AJT_M115_M515
**Comment**: Tabela de restauracao dos registros M115 e M515

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M115_M515 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REST_AJT_M115_M515 |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | empresa referente a apuracao - EPC_APURACAO |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | estabelecimento referente a apuracao - EPC_APURACAO |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | tipo de livro referente a apuracao - EPC_APURACAO |
| 5 | DAT_APUR_INI | DATE | N |  | data inicial referente a apuracao - EPC_APURACAO |
| 6 | DAT_APUR_FIM | DATE | N |  | data final referente a apuracao - EPC_APURACAO |
| 7 | COD_SCP | VARCHAR2(14) | Y |  | codigo SCP referente a apuracao - EPC_APURACAO |
| 8 | COD_REG_M110_M510 | VARCHAR2(10) | Y |  | codigo do registro pai M110, M510 - EPC_REG_AJT_M110_M510 |
| 9 | IND_AJ_M110_M510 | CHAR(1) | Y |  | indicador do ajuste de credito do registro pai M110, M510 - EPC_REG_AJT_M110_M510 |
| 10 | COD_AJ_M110_M510 | VARCHAR2(3) | Y |  | codigo do ajuste de credito do registro pai M110, M510 - EPC_REG_AJT_M110_M510 |
| 11 | NUM_DOC_M110_M510 | VARCHAR2(100) | Y |  | numero do documento do registro pai M110, M510 - EPC_REG_AJT_M110_M510 |
| 12 | DSC_AJ_M110_M510 | VARCHAR2(400) | Y |  | descricao do ajuste de credito do registro pai M110, M510 - EPC_REG_AJT_M110_M510 |
| 13 | COD_REG | VARCHAR2(3) | Y |  | codigo dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 14 | VL_DET | NUMBER(17,2) | Y |  | detalhamento do valor dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 15 | COD_CST | VARCHAR2(3) | Y |  | codigo de situacao tributaria dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 16 | VL_BC_DET | NUMBER(17,3) | Y |  | detalhamento da base de calculo dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 17 | ALIQ_DET | NUMBER(8,4) | Y |  | detalhamento da aliquota dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 18 | DT_OPER | DATE | Y |  | data de operacao dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 19 | DSC_OPER | VARCHAR2(400) | Y |  | descricao das operacoes dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 20 | IDENT_CONTA | NUMBER(12) | Y |  | identificador da conta dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 21 | DSC_INF_COMP | VARCHAR2(400) | Y |  | descricao de informacao complementar dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 22 | COD_CTA | VARCHAR2(70) | Y |  | codigo da conta dos registros M115, M515  - EPC_REG_AJT_M115_M515 |
| 23 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y | '1' |  |
| 25 | COD_CRED_M100_M500 | VARCHAR2(3) | Y |  | codigo do credito do registro pai M100, M500 - EPC_REG_AJT_M100_M500 |

**PK**: ID_REST_M115_M515

**Indexes**:
- IU_EPC_REST_AJT_M115_M515 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_SCP, COD_REG_M110_M510, IND_AJ_M110_M510, COD_AJ_M110_M510, NUM_DOC_M110_M510, DSC_AJ_M110_M510, VL_DET, COD_CST, ALIQ_DET, DT_OPER, IDENT_CONTA)

---

## EPC_REST_AJT_M205_M605
**Comment**: Tabela de restauracao dos registros M205 e M605

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M205_M605 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REST_AJT_M205_M605 |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | empresa referente a apuracao - EPC_APURACAO |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | estabelecimento referente a apuracao - EPC_APURACAO |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | tipo de livro referente a apuracao - EPC_APURACAO |
| 5 | DAT_APUR_INI | DATE | N |  | data inicial referente a apuracao - EPC_APURACAO |
| 6 | DAT_APUR_FIM | DATE | N |  | data final referente a apuracao - EPC_APURACAO |
| 7 | COD_SCP | VARCHAR2(14) | Y |  | codigo SCP referente a apuracao - EPC_APURACAO |
| 8 | COD_REG_M200_M600 | VARCHAR2(10) | Y |  | codigo do registro pai M200, M600 - EPC_REG_AJT_M200_M600 |
| 9 | COD_REG | VARCHAR2(3) | Y |  | codigo dos registros M205, M605  - EPC_REG_AJT_M205_M605 |
| 10 | NUM_CAMPO | VARCHAR2(2) | Y |  | numero do campo dos registros M205, M605  - EPC_REG_AJT_M205_M605 |
| 11 | COD_RECEITA | VARCHAR2(6) | Y |  | codigo de receita dos registros M205, M605  - EPC_REG_AJT_M205_M605 |
| 12 | VL_DEB | NUMBER(17,2) | Y |  | valor de debito dos registros M205, M605  - EPC_REG_AJT_M205_M605 |
| 13 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y | '1' |  |

**PK**: ID_REST_M205_M605

**Indexes**:
- IU_EPC_REST_AJT_M205_M605 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_SCP, COD_REG_M200_M600, NUM_CAMPO)

---

## EPC_REST_AJT_M211_M611
**Comment**: Tabela de restauracao dos registros M211 e M611.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M211_M611 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REST_AJT_M211_M611 |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | empresa referente a apuracao - EPC_APURACAO |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | estabelecimento referente a apuracao - EPC_APURACAO |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | tipo de livro referente a apuracao - EPC_APURACAO |
| 5 | DAT_APUR_INI | DATE | N |  | data inicial referente a apuracao - EPC_APURACAO |
| 6 | DAT_APUR_FIM | DATE | N |  | data final referente a apuracao - EPC_APURACAO |
| 7 | COD_REG_M210_M610 | VARCHAR2(10) | Y |  | codigo do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 8 | COD_CONT_M210_M610 | VARCHAR2(4) | Y |  | codigo da contribuicao do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 9 | ALIQ_M210_M610 | NUMBER(8,4) | Y |  | aliquota do Pis/Cofins do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 10 | ALIQ_QUANT_M210_M610 | NUMBER(19,4) | Y |  | aliquota em reais do Pis/Cofins do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 11 | COD_REG | VARCHAR2(10) | Y |  | codigo dos registros M211, M611  - EPC_REG_AJT_M211_M611 |
| 12 | IND_TIP_COOP | VARCHAR2(2) | Y |  |  |
| 13 | VL_BC_CONT_ANT_EXC_COOP | NUMBER(17,2) | Y |  |  |
| 14 | VL_EXC_COOP_GER | NUMBER(17,2) | Y |  |  |
| 15 | VL_EXC_ESP_COOP | NUMBER(17,2) | Y |  |  |
| 16 | VL_BC_CONT | NUMBER(17,2) | Y |  |  |
| 17 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 18 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: ID_REST_M211_M611

**Indexes**:
- IU_EPC_REST_AJT_M211_M611 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_REG_M210_M610, COD_CONT_M210_M610, ALIQ_M210_M610, ALIQ_QUANT_M210_M610, COD_REG, IND_TIP_COOP, COD_SCP)

---

## EPC_REST_AJT_M215_M615

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M215_M615 | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APUR_INI | DATE | N |  |  |
| 6 | DAT_APUR_FIM | DATE | N |  |  |
| 7 | COD_REG_M210_M610 | VARCHAR2(10) | Y |  |  |
| 8 | COD_CONT_M210_M610 | VARCHAR2(4) | Y |  |  |
| 9 | ALIQ_M210_M610 | NUMBER(8,4) | Y |  |  |
| 10 | ALIQ_QUANT_M210_M610 | NUMBER(19,4) | Y |  |  |
| 11 | COD_REG | VARCHAR2(10) | Y |  |  |
| 12 | IND_AJ_BC | VARCHAR2(1) | Y |  |  |
| 13 | VL_AJ_BC | NUMBER(17,2) | Y |  |  |
| 14 | COD_AJ | VARCHAR2(2) | Y |  |  |
| 15 | NUM_PROC | VARCHAR2(100) | Y |  |  |
| 16 | DSC_AJ_BC | VARCHAR2(400) | Y |  |  |
| 17 | DT_REF | DATE | Y |  |  |
| 18 | COD_CTA | VARCHAR2(70) | Y |  |  |
| 19 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 20 | CNPJ | VARCHAR2(14) | Y |  |  |
| 21 | DSC_INF_COMP | VARCHAR2(400) | Y |  |  |
| 22 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 23 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 24 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: ID_REST_M215_M615

**Indexes**:
- IU_EPC_REST_AJT_M215_M615: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_REG_M210_M610, COD_CONT_M210_M610, ALIQ_M210_M610, ALIQ_QUANT_M210_M610, COD_REG, IND_AJ_BC, COD_AJ, NUM_PROC, COD_SCP)

---

## EPC_REST_AJT_M220_M620
**Comment**: Tabela de restauracao dos registros M220 e M620.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M220_M620 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REST_AJT_M220_M620 |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | empresa referente a apuracao - EPC_APURACAO |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | estabelecimento referente a apuracao - EPC_APURACAO |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | tipo de livro referente a apuracao - EPC_APURACAO |
| 5 | DAT_APUR_INI | DATE | N |  | data inicial referente a apuracao - EPC_APURACAO |
| 6 | DAT_APUR_FIM | DATE | N |  | data final referente a apuracao - EPC_APURACAO |
| 7 | COD_REG_M210_M610 | VARCHAR2(10) | Y |  | codigo do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 8 | COD_CONT_M210_M610 | VARCHAR2(4) | Y |  | codigo da contribuicao do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 9 | ALIQ_M210_M610 | NUMBER(8,4) | Y |  | aliquota do Pis/Cofins do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 10 | ALIQ_QUANT_M210_M610 | NUMBER(19,4) | Y |  | aliquota em reais do Pis/Cofins do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 11 | COD_REG | VARCHAR2(10) | Y |  | codigo dos registros M220, M620  - EPC_REG_AJT_M220_M620 |
| 12 | IND_AJ | CHAR(1) | Y |  |  |
| 13 | VL_AJ | NUMBER(17,2) | Y |  |  |
| 14 | COD_AJ | VARCHAR2(10) | Y |  |  |
| 15 | NUM_DOC | VARCHAR2(100) | Y |  |  |
| 16 | DESCR_AJ | VARCHAR2(400) | Y |  |  |
| 17 | DT_REF | DATE | Y |  |  |
| 18 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 19 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: ID_REST_M220_M620

**Indexes**:
- IU_EPC_REST_AJT_M220_M620 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_REG_M210_M610, COD_CONT_M210_M610, ALIQ_M210_M610, ALIQ_QUANT_M210_M610, COD_REG, IND_AJ, COD_AJ, NUM_DOC, COD_SCP)

---

## EPC_REST_AJT_M225_M625
**Comment**: Tabela de restauracao dos registros M225 e M625

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M225_M625 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REST_AJT_M225_M625 |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | empresa referente a apuracao - EPC_APURACAO |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | estabelecimento referente a apuracao - EPC_APURACAO |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | tipo de livro referente a apuracao - EPC_APURACAO |
| 5 | DAT_APUR_INI | DATE | N |  | data inicial referente a apuracao - EPC_APURACAO |
| 6 | DAT_APUR_FIM | DATE | N |  | data final referente a apuracao - EPC_APURACAO |
| 7 | COD_SCP | VARCHAR2(14) | Y |  | codigo SCP referente a apuracao - EPC_APURACAO |
| 8 | COD_REG_M220_M620 | VARCHAR2(10) | Y |  | codigo do registro pai M220, M620 - EPC_REG_AJT_M220_M620 |
| 9 | IND_AJ_M220_M620 | CHAR(1) | Y |  | indicador do ajuste de credito do registro pai M220, M620 - EPC_REG_AJT_M220_M620 |
| 10 | COD_AJ_M220_M620 | VARCHAR2(2) | Y |  | codigo do ajuste de credito do registro pai M220, M620 - EPC_REG_AJT_M220_M620 |
| 11 | NUM_DOC_M220_M620 | VARCHAR2(100) | Y |  | numero do documento do registro pai M220, M620 - EPC_REG_AJT_M220_M620 |
| 12 | DSC_AJ_M220_M620 | VARCHAR2(400) | Y |  | numero do documento do registro pai M220, M620 - EPC_REG_AJT_M220_M620 |
| 13 | COD_REG | VARCHAR2(10) | Y |  | codigo dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 14 | VL_DET | NUMBER(17,2) | Y |  | detalhamento do valor dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 15 | COD_CST | VARCHAR2(3) | Y |  | codigo de situacao tributaria dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 16 | VL_BC_DET | NUMBER(17,3) | Y |  | detalhamento da base de calculo dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 17 | ALIQ_DET | NUMBER(8,4) | Y |  | detalhamento da aliquota dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 18 | DT_OPER | DATE | Y |  | data da operacao dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 19 | DSC_OPER | VARCHAR2(400) | Y |  | descricao das operacoes dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 20 | IDENT_CONTA | NUMBER(12) | Y |  | identificador da conta dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 21 | DSC_INF_COMP | VARCHAR2(400) | Y |  | descricao de informacao complementar dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 22 | COD_CTA | VARCHAR2(70) | Y |  | codigo da conta dos registros M225, M625  - EPC_REG_AJT_M225_M625 |
| 23 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y | '1' |  |

**PK**: ID_REST_M225_M625

**Indexes**:
- IU_EPC_REST_AJT_M225_M625: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_SCP, COD_REG_M220_M620, IND_AJ_M220_M620, COD_AJ_M220_M620, NUM_DOC_M220_M620, DSC_AJ_M220_M620, VL_DET, COD_CST, ALIQ_DET, DT_OPER, IDENT_CONTA)

---

## EPC_REST_AJT_M230_M630
**Comment**: Tabela de restauracao dos registros M230 e M630.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M230_M630 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REST_AJT_M230_M630 |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | empresa referente a apuracao - EPC_APURACAO |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | estabelecimento referente a apuracao - EPC_APURACAO |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | tipo de livro referente a apuracao - EPC_APURACAO |
| 5 | DAT_APUR_INI | DATE | N |  | data inicial referente a apuracao - EPC_APURACAO |
| 6 | DAT_APUR_FIM | DATE | N |  | data final referente a apuracao - EPC_APURACAO |
| 7 | COD_REG_M210_M610 | VARCHAR2(10) | Y |  | codigo do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 8 | COD_CONT_M210_M610 | VARCHAR2(4) | Y |  | codigo da contribuicao do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 9 | ALIQ_M210_M610 | NUMBER(8,4) | Y |  | aliquota do Pis/Cofins do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 10 | ALIQ_QUANT_M210_M610 | NUMBER(19,4) | Y |  | aliquota em reais do Pis/Cofins do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 11 | COD_REG | VARCHAR2(10) | Y |  | codigo dos registros M230, M630  - EPC_REG_AJT_M230_M630 |
| 12 | CNPJ | VARCHAR2(14) | Y |  |  |
| 13 | VL_VEND | NUMBER(17,2) | Y |  |  |
| 14 | VL_NAO_RECEB | NUMBER(17,2) | Y |  |  |
| 15 | VL_CONT_DIF | NUMBER(17,2) | Y |  |  |
| 16 | VL_CRED_DIF | NUMBER(17,2) | Y |  |  |
| 17 | COD_CRED | VARCHAR2(3) | Y |  |  |
| 18 | TEXTO | VARCHAR2(2000) | Y |  |  |
| 19 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: ID_REST_M230_M630

**Indexes**:
- IU_EPC_REST_AJT_M230_M630 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_REG_M210_M610, COD_CONT_M210_M610, ALIQ_M210_M610, ALIQ_QUANT_M210_M610, COD_REG, CNPJ, COD_CRED, COD_SCP)

---

## EPC_REST_AJT_M300_M700
**Comment**: Tabela de restauracao dos registros M300 e M700.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REST_M300_M700 | NUMBER(12) | N |  | sequencial unico controlado pela sequence SEQ_EPC_REST_AJT_M300_M700 |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | empresa referente a apuracao - EPC_APURACAO |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | estabelecimento referente a apuracao - EPC_APURACAO |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  | tipo de livro referente a apuracao - EPC_APURACAO |
| 5 | DAT_APUR_INI | DATE | N |  | data inicial referente a apuracao - EPC_APURACAO |
| 6 | DAT_APUR_FIM | DATE | N |  | data final referente a apuracao - EPC_APURACAO |
| 7 | COD_REG_M210_M610 | VARCHAR2(10) | Y |  | codigo do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 8 | COD_CONT_M210_M610 | VARCHAR2(4) | Y |  | codigo da contribuicao do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 9 | ALIQ_M210_M610 | NUMBER(8,4) | Y |  | aliquota do Pis/Cofins do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 10 | ALIQ_QUANT_M210_M610 | NUMBER(19,4) | Y |  | aliquota em reais do Pis/Cofins do registro pai M210, M610 - EPC_REG_AJT_M210_M610 |
| 11 | COD_REG | VARCHAR2(10) | Y |  | codigo dos registros M300, M700  - EPC_REG_AJT_M300_M700 |
| 12 | PER_APUR | DATE | Y |  |  |
| 13 | DT_RECEB | DATE | Y |  |  |
| 14 | NAT_CRED_DESC | VARCHAR2(2) | Y |  |  |
| 15 | VL_CONT_APUR_DIFER | NUMBER(17,2) | Y |  |  |
| 16 | VL_CRED_DESC_DIFER | NUMBER(17,2) | Y |  |  |
| 17 | VL_CONT_DIFER_ANT | NUMBER(17,2) | Y |  |  |
| 18 | COD_SCP | VARCHAR2(14) | Y |  |  |

**PK**: ID_REST_M300_M700

**Indexes**:
- IU_EPC_REST_AJT_M300_M700 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APUR_INI, DAT_APUR_FIM, COD_REG_M210_M610, COD_CONT_M210_M610, ALIQ_M210_M610, ALIQ_QUANT_M210_M610, COD_REG, PER_APUR, DT_RECEB, NAT_CRED_DESC, COD_SCP)

---

## EPC_RET_UTIL
**Comment**: Tabela do EFD-PIS-COFINS que armazena os valores retidos na fonte utilizados do Pis e Cofins, provenientes de apuracoes anteriores ao periodo da apuracao atual (ID_REG).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_REG_RET_UTIL | NUMBER(12) | N |  | sequencial unico |
| 2 | ID_REG | NUMBER(12) | N |  | identificador da apuracao que está utilizando o valor da retencao |
| 3 | ID_REG_RET_DISP | NUMBER(12) | N |  | identificador da retencao disponivel que está sendo utilizada. Apuracao que dispoe do valor da retencao na fonte é anterior a que está utilizando a retencao (ID_REG). |
| 4 | VLR_RET_UTIL_DED | NUMBER(17,2) | Y |  | valor da retencao utilizado para deducao na contribuicao. |
| 5 | VLR_RET_UTIL_PER | NUMBER(17,2) | Y |  | valor da retencao utilizado por pedido de restituicao. |
| 6 | VLR_RET_UTIL_DCOMP | NUMBER(17,2) | Y |  | valor da retencao utilizado por declaracao de compensacao. |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: ID_REG_RET_UTIL

**FKs**:
- ID_REG → EPC_APURACAO(ID_REG)
- ID_REG_RET_DISP → EPC_APUR_RET_DISP(ID_REG_RET_DISP)

**Indexes**:
- IU_EPC_RET_UTIL (UNIQUE): (ID_REG, ID_REG_RET_DISP)

---

## EPC_TP_DOC_CSTOPNAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_VALID | DATE | N |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 5 | TP_OPERACAO | CHAR(1) | Y |  |  |
| 6 | IND_TRIB_PIS | CHAR(1) | Y |  |  |
| 7 | COD_TRIB_PIS | NUMBER(2) | Y |  |  |
| 8 | IND_TRIB_COFINS | CHAR(1) | Y |  |  |
| 9 | COD_TRIB_COFINS | NUMBER(2) | Y |  |  |
| 10 | NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 11 | DT_VALID_PIS | DATE | Y |  |  |
| 12 | DT_VALID_COFINS | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_VALID, IDENT_DOCTO

**FKs**:
- IND_TRIB_COFINS, COD_TRIB_COFINS, DT_VALID_COFINS → Y2027_SIT_TRIBUTARIA(IND_TRIBUTACAO, COD_TRIBUTACAO, DATA_VALID)
- IND_TRIB_PIS, COD_TRIB_PIS, DT_VALID_PIS → Y2027_SIT_TRIBUTARIA(IND_TRIBUTACAO, COD_TRIBUTACAO, DATA_VALID)

---

## EPC_VALORES_RECEITAS_PREV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COMPETENCIA | DATE | N |  |  |
| 4 | IND_INCID_TRIB | CHAR(1) | Y |  |  |
| 5 | VLR_RECEITA_BRUTA_TOT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RECEITA_BRUTA_ATIV | NUMBER(17,2) | Y |  |  |
| 7 | VLR_REC_DEMAIS_ATIV | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COMPETENCIA

---

