# Módulo: MUN (MUN) - 18 tabelas

## MUN_CANOAS_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PREST_SERV_PROPRIO | CHAR(1) | Y |  |  |
| 4 | IND_PREST_SERV_FINANC | CHAR(1) | Y |  |  |
| 5 | IND_PREST_SERV_SN | CHAR(1) | Y |  |  |
| 6 | IND_TOMAD_SERV | CHAR(1) | Y |  |  |
| 7 | DATA_INC_SIMPLES | DATE | Y |  |  |
| 8 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## MUN_ESTAB_CENTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## MUN_MANUT_DEDUCAO_MAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IND_ESPECIE | VARCHAR2(3) | Y |  |  |
| 12 | COD_OBRA_ORIGEM | VARCHAR2(15) | Y |  |  |
| 13 | COD_OBRA_DESTINO | VARCHAR2(15) | Y |  |  |
| 14 | VLR_USO_CONSUMO | NUMBER(15,2) | Y |  |  |
| 15 | VLR_INCORPORADO | NUMBER(15,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## MUN_MANUT_DEDUCAO_PROJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 4 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 5 | NUM_PROJETO | VARCHAR2(8) | N |  |  |
| 6 | NOME_PROJETO | VARCHAR2(35) | Y |  |  |
| 7 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_COMPETENCIA, ANO_COMPETENCIA, NUM_PROJETO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## MUN_MANUT_DESIF_0430
**Comment**: Tabela de Manutencao do registro 0430 da DESIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 6 | DSC_DEDUCAO | VARCHAR2(255) | Y |  |  |
| 7 | VLR_INCENT | NUMBER(17,2) | Y |  |  |
| 8 | DSC_INCENT | VARCHAR2(255) | Y |  |  |
| 9 | IND_MOT_N_EXIG | VARCHAR2(1) | Y |  |  |
| 10 | NUM_PROC_N_EXIG | VARCHAR2(20) | Y |  |  |
| 11 | IND_DESDOBRA_CMISTA | VARCHAR2(1) | Y |  |  |
| 12 | COD_TRIB_DESIF | VARCHAR2(15) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, IDENT_CONTA

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_MUN_MANUT_DESIF_CTA: (IDENT_CONTA)

---

## MUN_MANUT_DESIF_0440
**Comment**: Tabela de Manutencao do registro 0440 da DESIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | ALIQ | NUMBER(5,2) | N |  |  |
| 5 | COD_TRIB_DESIF | VARCHAR2(15) | Y |  |  |
| 6 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 7 | DSC_DEDUCAO | VARCHAR2(255) | Y |  |  |
| 8 | VLR_INCENT | NUMBER(17,2) | Y |  |  |
| 9 | DSC_INCENT | VARCHAR2(255) | Y |  |  |
| 10 | VLR_COMPENSACAO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISSQN_RECOLH | NUMBER(17,2) | Y |  |  |
| 12 | IND_MOT_N_EXIG | VARCHAR2(1) | Y |  |  |
| 13 | NUM_PROC_N_EXIG | VARCHAR2(20) | Y |  |  |

**FKs**:
- COD_TRIB_DESIF → CAD_TRIB_DESIF(COD_TRIB_DESIF)

**Indexes**:
- UK_MUN_MANUT_DESIF_0440 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_APUR, ALIQ, COD_TRIB_DESIF)

---

## MUN_MANUT_DESIF_0440_COMP
**Comment**: Tabela de Manutencao do registro 0440 da DESIF, detalhamento da compensacao

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | ALIQ | NUMBER(5,2) | N |  |  |
| 5 | COD_TRIB_DESIF | VARCHAR2(15) | Y |  |  |
| 6 | DAT_COMPENSACAO | DATE | N |  |  |
| 7 | VLR_COMPENSACAO | NUMBER(17,2) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APUR, ALIQ, COD_TRIB_DESIF → MUN_MANUT_DESIF_0440(COD_EMPRESA, COD_ESTAB, DAT_APUR, ALIQ, COD_TRIB_DESIF)

**Indexes**:
- UK_MUN_MANUT_DESIF_0440_COMP (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_APUR, ALIQ, COD_TRIB_DESIF, DAT_COMPENSACAO)

---

## MUN_MANUT_DESPESA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 4 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 5 | MES_DESPESA | NUMBER(2) | N |  |  |
| 6 | VLR_AGUA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ENERGIA_ELETRICA | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TELEFONE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ALUGUEL_IPTU | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CIM | NUMBER(17,2) | Y |  |  |
| 11 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SIMPLES | NUMBER(17,2) | Y |  |  |
| 15 | VLR_FOLHA_PAGTO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_INSS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_FGTS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_VALE_TRANSP | NUMBER(17,2) | Y |  |  |
| 19 | VLR_PRO_LABORE | NUMBER(17,2) | Y |  |  |
| 20 | VLR_MAT_EXPEDIENTE | NUMBER(17,2) | Y |  |  |
| 21 | VLR_SERV_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 22 | VLR_COMBUSTIVEL | NUMBER(17,2) | Y |  |  |
| 23 | VLR_DESPESA_FINANC | NUMBER(17,2) | Y |  |  |
| 24 | VLR_CONDOMINIO | NUMBER(17,2) | Y |  |  |
| 25 | VLR_SERV_CONTABIL | NUMBER(17,2) | Y |  |  |
| 26 | VLR_MAT_APLICADO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_COMPETENCIA, ANO_COMPETENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## MUN_MANUT_INF_ECONOM
**Comment**: Manutencao das Informacoes Economicas para a geracao dos modulos municipais - SAFMUNIC.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_GERACAO | NUMBER(4) | N |  |  |
| 4 | VLR_TOTAL_DESPESA | NUMBER(17,2) | Y |  |  |
| 5 | VLR_OUTRAS_RECEITAS | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ATIVO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_PASSIVO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_PATRIMONIO_LIQ | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CAPITAL_SOCIAL | NUMBER(17,2) | Y |  |  |
| 10 | NUM_EMPREGADOS_INI | NUMBER(10) | Y |  |  |
| 11 | NUM_EMPREGADOS_FIM | NUMBER(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_GERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## MUN_MANUT_PROF_LIBERAL
**Comment**: Manutencao dos Profissionais Liberais para a geracao dos modulos municipais - SAFMUNIC.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CPF | VARCHAR2(11) | N |  |  |
| 4 | NOME | VARCHAR2(40) | Y |  |  |
| 5 | DSC_HABILITACAO | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_CPF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## MUN_MANUT_RECEITA
**Comment**: Manutencao das Receitas para a geracao dos modulos municipais - SAFMUNIC.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | IND_TIPO_RECEITA | CHAR(1) | N |  | Indica o tipo de receita. Dominio: I – Industria, C – Comercio, O - Outros. |
| 6 | VLR_FATURAMENTO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, IND_TIPO_RECEITA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## MUN_MANUT_SOCIOS
**Comment**: Manutencao do Cadastro de Socios para a geracao dos modulos municipais - SAFMUNIC.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CPF_CNPJ | VARCHAR2(14) | N |  |  |
| 4 | NOME | VARCHAR2(100) | Y |  |  |
| 5 | ENDERECO | VARCHAR2(100) | Y |  |  |
| 6 | NUM_ENDERECO | VARCHAR2(8) | Y |  |  |
| 7 | COMPL_ENDERECO | VARCHAR2(50) | Y |  |  |
| 8 | BAIRRO | VARCHAR2(70) | Y |  |  |
| 9 | CIDADE | VARCHAR2(70) | Y |  |  |
| 10 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 11 | CEP | NUMBER(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_CPF_CNPJ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## MUN_PARNAMIRIM_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## MUN_RATEIO_DESIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | COD_TRIB_DESIF | VARCHAR2(15) | N |  |  |
| 6 | VLR_TOT_CRE_INF | NUMBER(19,2) | Y |  |  |
| 7 | VLR_TOT_DEB_INF | NUMBER(19,2) | Y |  |  |
| 8 | VLR_RECEITA_INF | NUMBER(19,2) | Y |  |  |
| 9 | VLR_ISS_RET_INF | NUMBER(19,2) | Y |  |  |
| 10 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 11 | DSC_DEDUCAO | VARCHAR2(255) | Y |  |  |
| 12 | VLR_INCENT | NUMBER(17,2) | Y |  |  |
| 13 | DSC_INCENT | VARCHAR2(255) | Y |  |  |
| 14 | IND_MOT_N_EXIG | VARCHAR2(1) | Y |  |  |
| 15 | NUM_PROC_N_EXIG | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO, COD_TRIB_DESIF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

---

## MUN_REMESSA_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 4 | IND_SERV_PREST | CHAR(1) | N |  |  |
| 5 | IND_SIMPLES_NAC | CHAR(1) | Y |  |  |
| 6 | ALIQ_SIMPLES_NAC | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## MUN_SIGAMWEB_DADOS_INI
**Comment**: Parametrização dos dados iniciais para os módulos municipais atendidos pelo validador SIGAM WEB.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | NUM_FUNC | NUMBER(6) | Y |  |  |
| 6 | VLR_FOLHA_PAGTO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_FATURAMENTO | NUMBER(17,2) | Y |  |  |
| 8 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## MUN_SIGIS_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 4 | NOME_PREFEITURA | VARCHAR2(50) | Y |  |  |
| 5 | CNPJ_PREFEITURA | VARCHAR2(14) | Y |  |  |
| 6 | IND_PROPRIO | CHAR(1) | Y |  |  |
| 7 | NOM_SOFTWARE | VARCHAR2(10) | Y |  |  |
| 8 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 9 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

**Indexes**:
- UK_MUN_SIGIS_DADOS_INI (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_ESTADO, COD_MUNICIPIO)

---

## MUN_TIPO_ESCRIT_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_SERVICO | CHAR(1) | N |  |  |
| 4 | COD_SERV_LEI_116 | VARCHAR2(4) | N |  |  |
| 5 | DAT_VALID_INI | DATE | N |  |  |
| 6 | DAT_VALID_FIM | DATE | Y |  |  |
| 7 | COD_TIPO_ESCRIT | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_SERVICO, COD_SERV_LEI_116, DAT_VALID_INI

---

