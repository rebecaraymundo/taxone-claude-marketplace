# Módulo: REINF (EFD-Reinf) - 133 tabelas

## REINF_ARQUIVO_XSD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ARQUIVO | NUMBER(22) | N |  | Identificador Unico - Sequence SEQ_REINF_ARQUIVO_XSD |
| 2 | TIPO_EVENTO | VARCHAR2(50) | Y |  | Preencher com o código que identifica o tipo do evento. Exemplo:R-1000, R-1070, R-2010, etc. |
| 3 | DESCRICAO_EVENTO | VARCHAR2(100) | Y |  |  |
| 4 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V. "v01_00_00". |
| 5 | ARQUIVO | BLOB | Y |  | Arquivo XSD. |
| 6 | DAT_ULT_ATUALIZA | DATE | Y |  | Data da ultima atualizacao da respectiva view |

**PK**: ID_ARQUIVO

---

## REINF_CONF_PREVIDENCIARIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_EMISSAO | DATE | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | NUM_ITEM | NUMBER(5) | N |  |  |
| 11 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 12 | IDENT_TIPO_SERV_ESOCIAL | NUMBER(12) | Y |  |  |
| 13 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 14 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 18 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 19 | IND_TIPO_PROC | CHAR(1) | Y |  |  |
| 20 | NUM_PROC_JUR | VARCHAR2(21) | Y |  |  |
| 21 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 22 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 23 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 24 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 25 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 26 | COD_PARAM | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, DATA_FISCAL, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM, COD_USUARIO

---

## REINF_CONF_PREV_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 5 | DISCRI_ATIV_CONT_PREV | VARCHAR2(90) | N |  |  |
| 6 | IND_AJ_REINF | CHAR(1) | N |  |  |
| 7 | COD_AJ_REINF | VARCHAR2(2) | N |  |  |
| 8 | VL_AJ_REINF | NUMBER(17,2) | Y |  |  |
| 9 | DSC_AJ_REINF | VARCHAR2(400) | Y |  |  |
| 10 | DT_REF_REINF | DATE | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV, IND_AJ_REINF, COD_AJ_REINF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV → X185_CONTRIB_PREV(COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV)

---

## REINF_CONF_PREV_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 5 | DISCRI_ATIV_CONT_PREV | VARCHAR2(90) | N |  |  |
| 6 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 7 | VLR_BRUTO_NOTA | NUMBER(17,2) | Y |  |  |
| 8 | DATA_FISCAL | DATE | Y |  |  |
| 9 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 10 | NORM_DEV | CHAR(1) | Y |  |  |
| 11 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 13 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 15 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 16 | DATA_EMISSAO | DATE | Y |  |  |
| 17 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 18 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV, IDENT_DOCTO_FISCAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV → X185_CONTRIB_PREV(COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV)

**Indexes**:
- IX_REINF_CONF_PREV_NF: (COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## REINF_CONF_X03_X07

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IDENT_OPERACAO | NUMBER(12) | N |  |  |
| 10 | IDENT_DARF | NUMBER(12) | N |  |  |
| 11 | COD_TRIBUTO_DESC | VARCHAR2(15) | Y |  |  |
| 12 | IND_EXIST_DOC | CHAR(1) | Y |  |  |
| 13 | COD_USUARIO | VARCHAR2(40) | N |  |  |
| 14 | VLR_BRUTO_X53 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIBUTO_X53 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BRUTO_X07 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TRIBUTO_X07 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, COD_USUARIO

**Indexes**:
- IX_REINF_CONF_X03_X07_1: (COD_USUARIO)

---

## REINF_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DADOS_INI | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_DADOS_INI |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | Estabelecimento Contribuinte |
| 4 | VALID_INI | DATE | N |  | Validade Inicial (primeiro dia do mes) |
| 5 | VALID_FIM | DATE | Y |  | Validade Final (último dia do mês) |
| 6 | COD_CLASSIF_TRIB | VARCHAR2(2) | N |  | Classificacao tributaria, conforme tabela 08 do REINF. (R1000 - classTrib) - DWT_CLASSIF_TRIB |
| 7 | IND_ESCRITURA_ECD | CHAR(1) | N |  | Indicativo da obrigatoriedade do contribuinte em fazer a sua escrituracao ECD (R1000 - indEscrituracao) Dominio : 0 - Nao faz; 1 - Empresa entrega a ECD. |
| 8 | IND_DESONERA_FOLHA | VARCHAR2(2) | N |  | Indicativo de Desoneracao da Folha pela CPRB  (R1000 - indDesoneracao) Dominio 0 - Nao Aplicavel; 1 - Empresa enquadrada nos termos da Lei 12.546/2011 e alteracoes. |
| 9 | IND_ACORDO_ISENCAO | CHAR(1) | N |  | Indicativo de acordo internacional de iseno de multa (R1000 - indAcordoIsenMulta) Dominio 0 - Sem acordo; 1 - Com acordo. |
| 10 | IND_SITUACAO_PJ | CHAR(1) | Y |  | Indicativo de situaão da Pessoa Jurdica ((R1000 - indSitPJ) Dominio  0 - Situação Normal; 1 - Extinção; 2 - Fusão; 3 - Cisão; 4 - Incorporação. |
| 11 | NOME_CONTATO | VARCHAR2(70) | N |  | Nome do Contato. (R1000 - nmCtt) |
| 12 | NUM_CPF | VARCHAR2(11) | N |  | CPF do Contato. (R1000 - cpfCtt) |
| 13 | NUM_TEL_FIXO | VARCHAR2(13) | Y |  | Telefone Fixo do Contato. (R1000 - foneFixo) |
| 14 | NUM_TEL_CEL | VARCHAR2(13) | Y |  | Telefone Celular do Contato. (R1000 - foneCel) |
| 15 | EMAIL | VARCHAR2(60) | Y |  | email do Contato. (R1000 - email) |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | DT_TRANSF_FINS_LUCR | DATE | Y |  | Data da transformação de entidade beneficente de assistência social isenta de contribuições sociais em sociedade com fins lucrativos. |
| 18 | IND_UNIAO | VARCHAR2(1) | Y |  | Indicativo de entidade vinculada a União. |
| 19 | IND_PERT_IRRF | VARCHAR2(1) | Y |  | Indicador de pertencimento do IRRF |

**PK**: ID_DADOS_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CLASSIF_TRIB → DWT_CLASSIF_TRIB(COD_CLASSIF_TRIB)

**Indexes**:
- UK_REINF_DADOS_INI_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, VALID_INI)

---

## REINF_DADOS_INICIAIS_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_R2040 | CHAR(1) | Y |  |  |
| 4 | IND_DESC_NF_VLR_RET_ZERADO | CHAR(1) | Y | 'N' |  |
| 5 | IND_TP_AMB | CHAR(1) | Y | '1' |  |
| 6 | IND_PROC_EMISSAO | CHAR(1) | Y | '1' |  |
| 7 | IND_DESC_RETENCAO_INF | CHAR(1) | Y | 'N' |  |
| 8 | IND_VALOR_CONTABIL | CHAR(1) | Y | '1' |  |
| 9 | IND_ORIGEM_X63 | VARCHAR2(1) | Y | 'N' |  |
| 10 | IND_GERA_DATA_EMISSAO | VARCHAR2(1) | Y | 'N' |  |
| 11 | IND_VALOR_R2055 | CHAR(1) | Y | '1' |  |
| 12 | IND_CONS_VLR_BRUTO_R4020 | VARCHAR2(1) | Y |  |  |
| 13 | IND_DATA_R4010_R4020 | VARCHAR2(1) | Y | '1' |  |
| 14 | IND_VBASE_IGUAL_VBRUTO_R4020 | VARCHAR2(1) | Y | 'S' |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## REINF_DADOS_INI_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DADOS_INI_HIST | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_DADOS_INI_HIST |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | Estabelecimento Contribuinte |
| 4 | VALID_INI | DATE | N |  | Validade Inicial (primeiro dia do mes) |
| 5 | DAT_OCORRENCIA | TIMESTAMP(6) | N |  | Data da Inclusão do historico |
| 6 | VALID_FIM | DATE | Y |  | Validade Final (último dia do mês) |
| 7 | COD_CLASSIF_TRIB | VARCHAR2(2) | N |  | Classificacao tributaria, conforme tabela 08 do REINF. (R1000 - classTrib) - DWT_CLASSIF_TRIB |
| 8 | IND_ESCRITURA_ECD | CHAR(1) | N |  | Indicativo da obrigatoriedade do contribuinte em fazer a sua escrituracao ECD (R1000 - indEscrituracao) Dominio : 0 - Nao faz; 1 - Empresa entrega a ECD. |
| 9 | IND_DESONERA_FOLHA | VARCHAR2(2) | N |  | Indicativo de Desoneracao da Folha pela CPRB  (R1000 - indDesoneracao) Dominio 0 - Nao Aplicavel; 1 - Empresa enquadrada nos termos da Lei 12.546/2011 e alteracoes. |
| 10 | IND_ACORDO_ISENCAO | CHAR(1) | N |  | Indicativo de acordo internacional de iseno de multa (R1000 - indAcordoIsenMulta) Dominio 0 - Sem acordo; 1 - Com acordo. |
| 11 | IND_SITUACAO_PJ | CHAR(1) | Y |  | Indicativo de situaão da Pessoa Jurdica ((R1000 - indSitPJ) Dominio  0 - Situação Normal; 1 - Extinção; 2 - Fusão; 3 - Cisão; 4 - Incorporação. |
| 12 | NOME_CONTATO | VARCHAR2(70) | N |  | Nome do Contato. (R1000 - nmCtt) |
| 13 | NUM_CPF | VARCHAR2(11) | N |  | CPF do Contato. (R1000 - cpfCtt) |
| 14 | NUM_TEL_FIXO | VARCHAR2(13) | Y |  | Telefone Fixo do Contato. (R1000 - foneFixo) |
| 15 | NUM_TEL_CEL | VARCHAR2(13) | Y |  | Telefone Celular do Contato. (R1000 - foneCel) |
| 16 | EMAIL | VARCHAR2(60) | Y |  | email do Contato. (R1000 - email) |
| 17 | IND_STATUS | CHAR(1) | Y |  | Dominio: view REINF_STATUS_DADOS_INI_HIST_V |
| 18 | IND_DELETE | CHAR(1) | Y |  | Dominio: S, N |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | DT_TRANSF_FINS_LUCR | DATE | Y |  | Data da transformação de entidade beneficente de assistência social isenta de contribuições sociais em sociedade com fins lucrativos. |
| 21 | IND_UNIAO | VARCHAR2(1) | Y |  | Indicativo de entidade vinculada a União. |
| 22 | IND_PERT_IRRF | VARCHAR2(1) | Y |  | Indicador de pertencimento do IRRF |

**PK**: ID_DADOS_INI_HIST

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_REINF_DADOS_INI_HIST_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, VALID_INI, DAT_OCORRENCIA)

---

## REINF_DADOS_INI_SOFT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DADOS_INI_SOFT | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_DADOS_INI_SOFT |
| 2 | ID_DADOS_INI | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | NUM_CNPJ | VARCHAR2(14) | N |  | CNPJ da Software House. (R1000 - cnpjSoftHouse) |
| 4 | RAZAO_SOCIAL | VARCHAR2(115) | N |  | Razao Social da Software House. (R1000 - nmRazao) |
| 5 | NOME_CONTATO | VARCHAR2(70) | N |  | Nome do Contato. (R1000 - nmCont) |
| 6 | NUM_TEL | VARCHAR2(13) | Y |  | Telefone do Contato. (R1000 - telefone) |
| 7 | EMAIL | VARCHAR2(60) | Y |  | email do Contato. (R1000 - email) |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: ID_DADOS_INI_SOFT

**FKs**:
- ID_DADOS_INI → REINF_DADOS_INI(ID_DADOS_INI)

**Indexes**:
- UK_REINF_DADOS_INI_SOFT_001 (UNIQUE): (ID_DADOS_INI, NUM_CNPJ)

---

## REINF_DADOS_INI_SOFT_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DADOS_INI_SOFT_HIST | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_DADOS_INI_SOFT_HIST |
| 2 | ID_DADOS_INI_HIST | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | NUM_CNPJ | VARCHAR2(14) | N |  | CNPJ da Software House. (R1000 - cnpjSoftHouse) |
| 4 | RAZAO_SOCIAL | VARCHAR2(115) | N |  | Razao Social da Software House. (R1000 - nmRazao) |
| 5 | NOME_CONTATO | VARCHAR2(70) | N |  | Nome do Contato. (R1000 - nmCont) |
| 6 | NUM_TEL | VARCHAR2(13) | Y |  | Telefone do Contato. (R1000 - telefone) |
| 7 | EMAIL | VARCHAR2(60) | Y |  | email do Contato. (R1000 - email) |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: ID_DADOS_INI_SOFT_HIST

**FKs**:
- ID_DADOS_INI_HIST → REINF_DADOS_INI_HIST(ID_DADOS_INI_HIST)

**Indexes**:
- UK_REINF_DADOS_INI_ST_HIST_001 (UNIQUE): (ID_DADOS_INI_HIST, NUM_CNPJ)

---

## REINF_DEDUCOES_R2050

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IND_COM | CHAR(1) | N |  |  |
| 5 | VLR_REC_BRT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CP_APUR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RAT_APUR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SENAR_APUR | NUMBER(17,2) | Y |  |  |
| 9 | IND_TIPO_AJUSTE | VARCHAR2(1) | N | '2' |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, IND_COM, IND_TIPO_AJUSTE

---

## REINF_DEDUCOES_R2050_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IND_COM | CHAR(1) | N |  |  |
| 5 | IND_TIPO_AJUSTE | VARCHAR2(1) | N | '2' |  |
| 6 | IDENT_PROC_ADJ | NUMBER(12) | N |  |  |
| 7 | IDENT_SUSP_TBT | NUMBER(12) | N |  |  |
| 8 | VLR_PREV_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 9 | VLR_GIBRAT_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SENAR_EXIG_SUSP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, IND_COM, IND_TIPO_AJUSTE, IDENT_PROC_ADJ, IDENT_SUSP_TBT

**Indexes**:
- IX_REINF_DEDUCOES_R2050_PROC: (COD_EMPRESA, COD_ESTAB, DAT_APUR, IND_COM, IND_TIPO_AJUSTE)

---

## REINF_ENTIDADE_R1050

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ENT_R1050 | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IND_CLASS_ENT_LIG | VARCHAR2(1) | N |  |  |
| 5 | NUM_CNPJ_LIG | VARCHAR2(14) | N |  |  |
| 6 | VALID_INI | DATE | N |  |  |
| 7 | VALID_FIM | DATE | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: ID_ENT_R1050

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_REINF_ENTIDADE_R1050_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, NUM_CNPJ_LIG, VALID_INI)

---

## REINF_ENTIDADE_R1050_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ENT_R1050_HIST | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IND_CLASS_ENT_LIG | VARCHAR2(1) | N |  |  |
| 5 | NUM_CNPJ_LIG | VARCHAR2(14) | N |  |  |
| 6 | VALID_INI | DATE | N |  |  |
| 7 | DAT_OCORRENCIA | TIMESTAMP(6) | N |  |  |
| 8 | VALID_FIM | DATE | Y |  |  |
| 9 | IND_STATUS | VARCHAR2(1) | Y |  |  |
| 10 | IND_DELETE | VARCHAR2(1) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: ID_ENT_R1050_HIST

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_REINF_ENTIDA_R1050_HIST_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, NUM_CNPJ_LIG, VALID_INI, DAT_OCORRENCIA)

---

## REINF_IMP_ARQUIVOS_XML_TMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOME_ARQ | VARCHAR2(255) | N |  |  |
| 2 | DIRECTORY_NAME | VARCHAR2(30) | Y |  |  |
| 3 | DIRECTORY_PATH | VARCHAR2(4000) | Y |  |  |

**PK**: NOME_ARQ

---

## REINF_PAINEL_ARG
**Comment**: Tabela com os argumentos de Estabelecimentos e Eventos da Consulta do Painel de Eventos.  

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  | Codigo da Empresa |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  | Codigo do Estabelecimento Contribuinte |
| 3 | TIPO_EVENTO | VARCHAR2(50) | Y |  | Preencher com o codigo que identifica o tipo do evento. Exemplo: R-1000, R-1070, R-2010, etc. |
| 4 | NR_INSCRICAO | VARCHAR2(14) | Y |  |  |
| 5 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 6 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | TIPO_REGISTRO | VARCHAR2(1) | Y |  | Valores válidos  1-tipo_evento / 2-cod_empresa+cod_estab / 3-cod_status_painel / 4-nr_inscricao+grupo_fis_jur+ind_fis_jur+cod_fis_jur+tipo_evento / 5-Todos prestadores selecionados |
| 10 | COD_FILIAL | VARCHAR2(6) | Y |  |  |

**Indexes**:
- IX_REINF_PAINEL_ARG_1: (TIPO_REGISTRO, COD_EMPRESA, COD_ESTAB, COD_FILIAL)
- IX_REINF_PAINEL_ARG_2: (TIPO_REGISTRO, NR_INSCRICAO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, TIPO_EVENTO)

---

## REINF_PARAM_REL_CONF_EVT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 2 | NUM_PROCESSO | NUMBER | Y |  |  |
| 3 | COD_EVENTO | VARCHAR2(10) | Y |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 6 | COD_ESTAB_DESC | VARCHAR2(6) | Y |  |  |
| 7 | DAT_GERACAO | DATE | Y |  |  |

**Indexes**:
- IX_TMP_PARAM_REL_REINF_EVT_1: (COD_USUARIO, COD_EVENTO, NUM_PROCESSO, COD_EMPRESA, COD_ESTAB, COD_ESTAB_DESC)

---

## REINF_PAR_CPRB_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | VLR_REC_BRT | NUMBER(17,2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## REINF_PGER_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_APUR | NUMBER(12) | N |  | Identificador unico. Sequence SEQ_REINF_PGER_APUR |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | Codigo da Empresa |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | Codigo do Estabelecimento Contribuinte R2010 - ideContribuinte |
| 4 | DAT_APUR | DATE | N |  | Data da Apuracao (ultimo dia do mes/ano). R2010 - perApur |
| 5 | IND_STATUS | CHAR(1) | Y |  |  |
| 6 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 7 | IND_R2010 | CHAR(1) | Y |  |  |
| 8 | IND_R2020 | CHAR(1) | Y |  |  |
| 9 | IND_R2050 | CHAR(1) | Y |  |  |
| 10 | IND_R2060 | CHAR(1) | Y |  |  |
| 11 | IND_R2070 | CHAR(1) | Y |  |  |
| 12 | IND_R2040 | CHAR(1) | Y |  |  |
| 13 | COD_VERSAO | VARCHAR2(20) | N | 'v1_02_00' |  |
| 14 | IND_SEM_MOVTO | VARCHAR2(1) | Y |  |  |
| 15 | COMP_SEM_MOVTO | DATE | Y |  |  |
| 16 | IND_TP_AMB | VARCHAR2(1) | N | '2' |  |
| 17 | DATA_SAIDA_REC_INI | DATE | Y |  |  |
| 18 | DATA_SAIDA_REC_FIM | DATE | Y |  |  |
| 19 | IND_R2055 | VARCHAR2(1) | Y |  |  |
| 20 | IND_R4040 | VARCHAR2(1) | Y |  |  |
| 21 | IND_R4080 | VARCHAR2(1) | Y |  |  |
| 22 | IND_FECH_REAB_R4000 | VARCHAR2(1) | Y |  |  |
| 23 | IND_R4010 | VARCHAR2(1) | Y |  |  |
| 24 | IND_R4020 | VARCHAR2(1) | Y |  |  |
| 25 | IND_CENTRALIZADO | VARCHAR2(1) | Y |  |  |

**PK**: ID_PGER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_REINF_PGER_APUR_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_APUR, COD_VERSAO, IND_TP_AMB)

---

## REINF_PGER_APUR_BCK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_APUR_V4 | NUMBER(12) | Y |  |  |
| 2 | ID_PGER_APUR_V5 | NUMBER(12) | Y |  |  |

---

## REINF_PGER_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_ESTAB | NUMBER(12) | N |  | Identificador unico. Sequence SEQ_REINF_PGER_ESTAB |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | Codigo da Empresa |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | Codigo do Estabelecimento Contribuinte R1000, R1070 - ideContribuinte |
| 4 | IND_R1000 | CHAR(1) | Y |  |  |
| 5 | IND_R1070 | CHAR(1) | Y |  |  |
| 6 | COD_VERSAO | VARCHAR2(20) | N | 'v1_02_00' |  |
| 7 | IND_TP_AMB | VARCHAR2(1) | N | '2' |  |
| 8 | IND_R1050 | VARCHAR2(1) | Y |  |  |

**PK**: ID_PGER_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_REINF_PGER_ESTAB_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_VERSAO, IND_TP_AMB)

---

## REINF_PGER_LIMPA_EVENTOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LIMPA_EVENTOS | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_LIMPA_EVENTOS |
| 2 | DAT_OCORRENCIA | DATE | N |  | Data de Ocorrencia |
| 3 | IND_OPER | CHAR(1) | Y |  | Dominio: L - Limpeza da base |
| 4 | IND_STATUS | CHAR(1) | Y |  | Status de Controle das OcorrÃªncias.  Dominio REINF_STATUS_PGER_V |
| 5 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 6 | ID_DADOS_INI_HIST | NUMBER(12) | Y |  | Identificador do Historico dos Dados Iniciais tabela REINF_DADOS_INI_HIST |
| 7 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificacao unica do evento ( evtInfoContri- id) |
| 8 | IND_TP_AMB | CHAR(1) | Y |  | Identificacao do ambiente (ideEvento - tpAmb). Dominio: 1 - Producao 2 - Producao restrita - dados reais 3 - Producao restrita - dados ficticios. |
| 9 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 10 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  | Versao do Processo de Emissao do Evento. (R1000 - ideEvento - verProc) |
| 11 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V. "v01_00_00". |
| 12 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  | Status Apresentado no Painel de Eventos, campo Situacao. Dominio REINF_STATUS_PAINEL_V. |
| 13 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_OUT. |
| 14 | NUM_INSCRICAO | VARCHAR2(14) | N |  | Numero cnpj contribuinte |
| 15 | ID_R1000_OC | NUMBER(12) | Y |  | Identificador da  REINF_PGER_R1000_OC  original que gerou evento de Limpeza |
| 16 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 17 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 18 | IND_OPER_R1000 | CHAR(1) | Y |  |  |
| 19 | COD_STATUS_PAINEL_R1000 | VARCHAR2(2) | Y |  |  |
| 20 | IND_TP_AMB_R1000 | CHAR(1) | Y |  |  |
| 21 | IND_PROC_EMISSAO_R1000 | CHAR(1) | Y |  |  |
| 22 | ID_EVENTO_R1000 | VARCHAR2(36) | Y |  |  |
| 23 | DAT_OCORRENCIA_R1000 | DATE | Y |  |  |
| 24 | ID_STG_OUT_R1000 | NUMBER(22) | Y |  | Identificador da  REINF_PGER_R1000_OC  original que gerou evento de Limpeza |

**PK**: ID_LIMPA_EVENTOS

---

## REINF_PGER_LOG_MSG
**Comment**: Tabela que armezena os XML do Evento enviado, e os Retornos do evento enviado.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_LOG_MSG | NUMBER(22) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_LOG_MSG |
| 2 | ID_OC | NUMBER(12) | Y |  | Identificador do registro nas tabelas de Ocorrências dos Eventos (REINF_PGER_R1000_OC, REINF_PGER_R1070_OC, REINF_PGER_R2010_OC,...) |
| 3 | TIPO_EVENTO | VARCHAR2(50) | Y |  | Preencher com o código que identifica o tipo do evento. Exemplo: R-1000, R-1070, R-2010, etc. |
| 4 | IND_LOG_MSG | CHAR(1) | Y |  | Dominio E - Envio R - Retorno OneSource |
| 5 | DAT_CRIACAO | DATE | Y |  | Data da inclusão do registro de log. Preencher este campo nos dois processos: - Geração do XML e envio para o OneSource. -  Recebimento do retorno do evento pelo OneSource. Neste caso gravar com o campo DT_CRIACAO da STG_EVENTOS_REINF_IN. |
| 6 | PROTOCOLO_ONESOURCE | VARCHAR2(36) | Y |  | Esse campo representa o protocolo que identifica o lote contendo os eventos. Preencher este campo no processo de Recebimento do retorno do evento pelo OneSource. Neste caso gravar com o campo PROTOCOLO_ONESOURCE da STG_EVENTOS_REINF_IN. |
| 7 | STATUS_PROC | VARCHAR2(8) | Y |  | Status do Onesource. Preencher este campo no processo de Recebimento do retorno do evento pelo OneSource. Neste caso gravar com o campo STATUS_PROC da STG_EVENTOS_REINF_IN. |
| 8 | XML_ENVIO_RETORNO | CLOB | Y |  | Preencher este campo nos dois processos: - Geração do XML e envio para o OneSource.  Neste caso, gravar o campo com o XML do Evento, que também será gravado na STG_EVENTOS_REINF_OUT, campo XML_ENVIO, para que o evento seja enviado para o OneSource. - Recebimento do retorno do evento pelo OneSource. Neste caso gravar o campo com o XML do Retorno do Evento (XML_RETORNO da STG_EVENTOS_REINF_IN). |
| 9 | COD_MENSAGEM_ONESOURCE | VARCHAR2(8) | Y |  | Codigo de Mensagem do Onesource. Preencher este campo no processo de Recebimento do retorno do evento pelo OneSource. Neste caso gravar com o campo COD_MENSAGEM_ONESOURCE da STG_EVENTOS_REINF_IN. |
| 10 | DES_MENSAGEM_ONESOURCE | VARCHAR2(4000) | Y |  | Descricao da Mensagem do Onesource. Preencher este campo no processo de Recebimento do retorno do evento pelo OneSource. Neste caso gravar com o campo DES_MENSAGEM_ONESOURCE da STG_EVENTOS_REINF_IN. |
| 11 | ID_EVENTO_ONESOURCE | VARCHAR2(36) | Y |  | ID do Evento do Onesource. Preencher este campo no processo de Recebimento do retorno do evento pelo OneSource. Neste caso gravar com o campo ID_EVENTO_ONESOURCE da STG_EVENTOS_REINF_IN. |
| 12 | RECIBO_ONESOURCE | VARCHAR2(52) | Y |  | Recibo Fisco do Onesource. Preencher este campo no processo de Recebimento do retorno do evento pelo OneSource. Neste caso gravar com o campo RECIBO_ONESOURCE da STG_EVENTOS_REINF_IN. |
| 13 | HASH_ONESOURCE | VARCHAR2(44) | Y |  | Hash Status do Onesource. Preencher este campo no processo de Recebimento do retorno do evento pelo OneSource. Neste caso gravar com o campo HASH_ONESOURCE da STG_EVENTOS_REINF_IN. |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_OUT. |
| 15 | LIDO | CHAR(1) | Y |  | Controle de Processamento (N - Não processado , P - Processando Registro , S - Registro Processado, E - Erro no processamento) |
| 16 | DESC_PROC_ERRO | VARCHAR2(200) | Y |  | Descrição erro do Processamento. |
| 17 | ID_STG_EVENTOS_REINF_IN | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_IN. |

**PK**: ID_PGER_LOG_MSG

**Indexes**:
- IX_REINF_PGER_LOG_MSG_01: (ID_OC, SYS_NC00018$)
- IX_REINF_PGER_LOG_MSG_02: (ID_STG_EVENTOS_REINF_OUT, IND_LOG_MSG)

---

## REINF_PGER_R1000_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R1000_COMPL | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R1000_COMPL |
| 2 | ID_R1000_OC | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | VALID_CONTRIB_FIM | DATE | Y |  | Validade Final (R1000 - fimValid) |
| 4 | VALID_CONTRIB_FIM_NV | DATE | Y |  | Nova Validade Final (R1000 - novaValidade - fimValid) |
| 5 | COD_CLASSIF_TRIB | VARCHAR2(2) | Y |  | Classificaco tributaria, conforme tabela 08 do REINF. (R1000 - classTrib) - DWT_CLASSIF_TRIB |
| 6 | IND_ESCRITURA_ECD | CHAR(1) | Y |  | Indicativo da obrigatoriedade do contribuinte em fazer a sua escrituracao ECD  (R1000 - indEscrituracao) Dominio: 0 - Nao faz; 1 - Empresa entrega a ECD. |
| 7 | IND_DESONERA_FOLHA | VARCHAR2(2) | Y |  | Indicativo de Desoneracao da Folha pela CPRB  (R1000 - indDesoneracao) Dominio: 0 - Nao Aplicavel; 1 - Empresa enquadrada nos termos da Lei 12.546/2011 e alteracoes. |
| 8 | IND_ACORDO_ISENCAO | CHAR(1) | Y |  | Indicativo de acordo internacional de iseno de multa (R1000 - indAcordoIsenMulta) Domnio:  0 - Sem acordo; 1 - Com acordo. |
| 9 | IND_SITUACAO_PJ | CHAR(1) | Y |  | Indicativo de situaão da Pessoa Jurdica ((R1000 - indSitPJ) Dominio: 0 - Situação Normal; 1 - Extincao; 2 - Fusao; 3 - Cisao; 4 - Incorporacao. |
| 10 | NOME_CONTATO | VARCHAR2(70) | Y |  | Nome do Contato. (R1000 - nmCtt) |
| 11 | NUM_CPF | VARCHAR2(11) | Y |  | CPF do Contato. (R1000 - cpfCtt) |
| 12 | NUM_TEL_FIXO | VARCHAR2(13) | Y |  | Telefone Fixo do Contato. (R1000 - foneFixo) |
| 13 | NUM_TEL_CEL | VARCHAR2(13) | Y |  | Telefone Celular do Contato. (R1000 - foneCel) |
| 14 | EMAIL | VARCHAR2(60) | Y |  | email do Contato. (R1000 - email) |
| 15 | IND_VALID_NV | CHAR(1) | Y |  | Campo indica que o evento de alteracao tera a tag novaValidade. Dominio: S - para ocorrencia com nova validade final; N - para ocorrencia sem nova validade final. |
| 16 | DT_TRANSF_FINS_LUCR | DATE | Y |  | Data da transformação de entidade beneficente de assistência social isenta de contribuições sociais em sociedade com fins lucrativos. |
| 17 | IND_UNIAO | VARCHAR2(1) | Y |  | Indicativo de entidade vinculada a União. |
| 18 | IND_PERT_IRRF | VARCHAR2(1) | Y |  |  |

**PK**: ID_R1000_COMPL

**FKs**:
- ID_R1000_OC → REINF_PGER_R1000_OC(ID_R1000_OC)

**Indexes**:
- UK_REINF_PGER_R1000_COMPL_001 (UNIQUE): (ID_R1000_OC)

---

## REINF_PGER_R1000_CONTRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_CONTRIB | NUMBER(12) | N |  | Identificador unico. Sequence SEQ_REINF_PGER_R1000_CONTRIB |
| 2 | ID_PGER_ESTAB | NUMBER(12) | N |  | Identificador do Registro Pai |
| 3 | TP_INSCRICAO | CHAR(1) | N |  | Tipo de Inscricao (R1000 - tpInsc) Dominio: 1 - CNPJ 2 - CPF |
| 4 | NUM_INSCRICAO | VARCHAR2(14) | N |  | Numero do Inscricao (R1000 - nrInsc) |
| 5 | VALID_CONTRIB_INI | DATE | N |  | Validade Inicial (R1000 - iniValid) |
| 6 | VALID_CONTRIB_FIM | DATE | Y |  | Validade Final (R1000 - fimValid) |

**PK**: ID_PGER_CONTRIB

**FKs**:
- ID_PGER_ESTAB → REINF_PGER_ESTAB(ID_PGER_ESTAB)

**Indexes**:
- UK_REINF_PGER_R1000_CONTR_001 (UNIQUE): (ID_PGER_ESTAB, TP_INSCRICAO, NUM_INSCRICAO, VALID_CONTRIB_INI)

---

## REINF_PGER_R1000_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R1000_OC | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R1000_OC |
| 2 | ID_PGER_CONTRIB | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | DAT_OCORRENCIA | DATE | N |  | Data de Ocorrencia |
| 4 | IND_OPER | CHAR(1) | Y |  | Dominio: I - Inclusao A - Alteracao E - Exclusao |
| 5 | IND_STATUS | CHAR(1) | Y |  | Status de Controle das Ocorrências.  Dominio REINF_STATUS_PGER_V |
| 6 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 7 | ID_DADOS_INI_HIST | NUMBER(12) | Y |  | Identificador do Historico dos Dados Iniciais (tabela REINF_DADOS_INI_HIST) |
| 8 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificacao unica do evento (R1000 - evtInfoContri- id) |
| 9 | IND_TP_AMB | CHAR(1) | Y |  | Identificacao do ambiente (R1000 - ideEvento - tpAmb). Dominio: 1 - Producao 2 - Producao restrita - dados reais; 3 - Producao restrita - dados ficticios. |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  | Processo de Emissao do Evento (R1000 - ideEvento - procEmi). Dominio: 1 - Aplicativo do contribuinte; 2 - Aplicativo governamental. |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  | Versao do Processo de Emissao do Evento. (R1000 - ideEvento - verProc). Informar a versao do aplicativo emissor do evento. |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  | Status Apresentado no Painel de Eventos, campo Situacao. Dominio REINF_STATUS_PAINEL_V. |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_OUT. |

**PK**: ID_R1000_OC

**FKs**:
- ID_PGER_CONTRIB → REINF_PGER_R1000_CONTRIB(ID_PGER_CONTRIB)
- ID_DADOS_INI_HIST → REINF_DADOS_INI_HIST(ID_DADOS_INI_HIST)

**Indexes**:
- UK_REINF_PGER_R1000_OC_001 (UNIQUE): (ID_PGER_CONTRIB, DAT_OCORRENCIA)

---

## REINF_PGER_R1000_SOFT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R1000_SOFT | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R1000_SOFT |
| 2 | ID_R1000_COMPL | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | NUM_CNPJ | VARCHAR2(14) | N |  | CNPJ da Software House. (R1000 - cnpjSoftHouse) |
| 4 | RAZAO_SOCIAL | VARCHAR2(115) | Y |  | Razao Social da Software House. (R1000 - nmRazao) |
| 5 | NOME_CONTATO | VARCHAR2(70) | Y |  | Nome do Contato. (R1000 - nmCont) |
| 6 | NUM_TEL | VARCHAR2(13) | Y |  | Telefone do Contato. (R1000 - telefone) |
| 7 | EMAIL | VARCHAR2(60) | Y |  | email do Contato. (R1000 - email) |

**PK**: ID_R1000_SOFT

**FKs**:
- ID_R1000_COMPL → REINF_PGER_R1000_COMPL(ID_R1000_COMPL)

**Indexes**:
- UK_REINF_PGER_R1000_SOFT_001 (UNIQUE): (ID_R1000_COMPL, NUM_CNPJ)

---

## REINF_PGER_R1050_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R1050_COMPL | NUMBER(12) | N |  |  |
| 2 | ID_R1050_OC | NUMBER(12) | N |  |  |
| 3 | VALID_FIM | DATE | Y |  |  |
| 4 | VALID_FIM_NV | DATE | Y |  |  |
| 5 | IND_CLASS_ENT_LIG | VARCHAR2(1) | Y |  |  |
| 6 | IND_VALID_NV | VARCHAR2(1) | Y |  |  |

**PK**: ID_R1050_COMPL

**FKs**:
- ID_R1050_OC → REINF_PGER_R1050_OC(ID_R1050_OC)

**Indexes**:
- UK_REINF_PGER_R1050_COMPL_001 (UNIQUE): (ID_R1050_COMPL, ID_R1050_OC)

---

## REINF_PGER_R1050_ENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_R1050_ENT | NUMBER(12) | N |  |  |
| 2 | ID_PGER_ESTAB | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | VARCHAR2(1) | N |  |  |
| 4 | NUM_INSCRICAO | VARCHAR2(14) | N |  |  |
| 5 | NUM_CNPJ_LIG | VARCHAR2(14) | N |  |  |
| 6 | VALID_INI | DATE | N |  |  |
| 7 | VALID_FIM | DATE | Y |  |  |

**PK**: ID_PGER_R1050_ENT

**FKs**:
- ID_PGER_ESTAB → REINF_PGER_ESTAB(ID_PGER_ESTAB)

**Indexes**:
- UK_REINF_PGER_R1050_ENT_001 (UNIQUE): (ID_PGER_ESTAB, TP_INSCRICAO, NUM_INSCRICAO, NUM_CNPJ_LIG, VALID_INI)

---

## REINF_PGER_R1050_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R1050_OC | NUMBER(12) | N |  |  |
| 2 | ID_PGER_R1050_ENT | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_OPER | VARCHAR2(1) | Y |  |  |
| 5 | IND_STATUS | VARCHAR2(1) | Y |  |  |
| 6 | PROC_ID | NUMBER(12) | Y |  |  |
| 7 | ID_ENT_R1050_HIST | NUMBER(12) | Y |  |  |
| 8 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 9 | IND_TP_AMB | VARCHAR2(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | VARCHAR2(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |

**PK**: ID_R1050_OC

**FKs**:
- ID_PGER_R1050_ENT → REINF_PGER_R1050_ENT(ID_PGER_R1050_ENT)
- ID_ENT_R1050_HIST → REINF_ENTIDADE_R1050_HIST(ID_ENT_R1050_HIST)

**Indexes**:
- UK_REINF_PGER_R1050_OC_001 (UNIQUE): (ID_PGER_R1050_ENT, DAT_OCORRENCIA)

---

## REINF_PGER_R1070_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R1070_COMPL | NUMBER(12) | N |  |  |
| 2 | ID_R1070_OC | NUMBER(12) | N |  |  |
| 3 | VALID_PROC_ADJ_FIM | DATE | Y |  |  |
| 4 | VALID_PROC_ADJ_FIM_NV | DATE | Y |  |  |
| 5 | UF_VARA | VARCHAR2(2) | Y |  |  |
| 6 | COD_MUNICIPIO | VARCHAR2(7) | Y |  |  |
| 7 | COD_VARA | VARCHAR2(4) | Y |  |  |
| 8 | IND_VALID_NV | CHAR(1) | Y |  |  |

**PK**: ID_R1070_COMPL

**FKs**:
- ID_R1070_OC → REINF_PGER_R1070_OC(ID_R1070_OC)

**Indexes**:
- UK_REINF_PGER_R1070_COMPL_001 (UNIQUE): (ID_R1070_COMPL, ID_R1070_OC)

---

## REINF_PGER_R1070_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R1070_OC | NUMBER(12) | N |  |  |
| 2 | ID_PGER_PROC_ADJ | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_OPER | CHAR(1) | Y |  |  |
| 5 | IND_STATUS | CHAR(1) | Y |  |  |
| 6 | IDENT_PROC_ADJ_HIST | NUMBER(12) | Y |  |  |
| 7 | PROC_ID | NUMBER(12) | Y |  |  |
| 8 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |

**PK**: ID_R1070_OC

**FKs**:
- ID_PGER_PROC_ADJ → REINF_PGER_R1070_PROC_ADJ(ID_PGER_PROC_ADJ)
- IDENT_PROC_ADJ_HIST → X2058_PROC_ADJ_HIST(IDENT_PROC_ADJ_HIST)

**Indexes**:
- UK_REINF_PGER_R1070_OC_001 (UNIQUE): (ID_R1070_OC, ID_PGER_PROC_ADJ, DAT_OCORRENCIA)

---

## REINF_PGER_R1070_PROC_ADJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PGER_PROC_ADJ | NUMBER(12) | N |  |  |
| 2 | ID_PGER_ESTAB | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 5 | VALID_PROC_ADJ_INI | DATE | N |  |  |
| 6 | VALID_PROC_ADJ_FIM | DATE | Y |  |  |
| 7 | IND_AUTORIA | CHAR(1) | Y |  |  |

**PK**: ID_PGER_PROC_ADJ

**FKs**:
- ID_PGER_ESTAB → REINF_PGER_ESTAB(ID_PGER_ESTAB)

**Indexes**:
- UK_REINF_PGER_R1070_PROC_001 (UNIQUE): (ID_PGER_PROC_ADJ, ID_PGER_ESTAB, IND_TP_PROC_ADJ, NUM_PROC_ADJ, VALID_PROC_ADJ_INI, IND_AUTORIA)

---

## REINF_PGER_R1070_SUSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R1070_SUSP | NUMBER(12) | N |  |  |
| 2 | ID_R1070_COMPL | NUMBER(12) | N |  |  |
| 3 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 4 | IND_SUSP | VARCHAR2(2) | Y |  |  |
| 5 | DAT_DECISAO | DATE | Y |  |  |
| 6 | IND_DEPOSITO | CHAR(1) | Y |  |  |

**PK**: ID_R1070_SUSP

**FKs**:
- ID_R1070_COMPL → REINF_PGER_R1070_COMPL(ID_R1070_COMPL)

**Indexes**:
- UK_REINF_PGER_R1070_SUSP_001 (UNIQUE): (ID_R1070_SUSP, ID_R1070_COMPL)

---

## REINF_PGER_R2010_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2010_NF | NUMBER(12) | N |  |  |
| 2 | ID_R2010_OC | NUMBER(12) | N |  |  |
| 3 | SERIE | VARCHAR2(3) | N |  |  |
| 4 | NUM_DOCTO | VARCHAR2(15) | N |  |  |
| 5 | DAT_EMISSAO_NF | DATE | Y |  |  |
| 6 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 7 | OBSERVACAO | VARCHAR2(250) | Y |  |  |
| 8 | IDENT_DOCTO_FISCAL | NUMBER(22) | Y |  |  |
| 9 | DATA_SAIDA_REC_NF | DATE | Y |  |  |

**PK**: ID_R2010_NF

**FKs**:
- ID_R2010_OC → REINF_PGER_R2010_OC(ID_R2010_OC)

**Indexes**:
- UK_REINF_PGER_R2010_NF_001 (UNIQUE): (ID_R2010_NF, ID_R2010_OC, SERIE, NUM_DOCTO)

---

## REINF_PGER_R2010_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2010_OC | NUMBER(12) | N |  |  |
| 2 | ID_R2010_PREST | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |
| 15 | IND_OBRA | CHAR(1) | Y |  |  |
| 16 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 18 | VLR_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 19 | VLR_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 21 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 22 | IND_CPRB | CHAR(1) | Y |  |  |
| 23 | DATA_SAIDA_REC_INI | DATE | Y |  |  |
| 24 | DATA_SAIDA_REC_FIM | DATE | Y |  |  |

**PK**: ID_R2010_OC

**FKs**:
- ID_R2010_PREST → REINF_PGER_R2010_PREST(ID_R2010_PREST)

**Indexes**:
- UK_REINF_PGER_R2010_OC_001 (UNIQUE): (ID_R2010_OC, ID_R2010_PREST, DAT_OCORRENCIA)

---

## REINF_PGER_R2010_PREST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2010_PREST | NUMBER(12) | N |  |  |
| 2 | ID_R2010_TOM | NUMBER(12) | N |  |  |
| 3 | CNPJ_PRESTADOR | VARCHAR2(14) | N |  |  |

**PK**: ID_R2010_PREST

**FKs**:
- ID_R2010_TOM → REINF_PGER_R2010_TOM(ID_R2010_TOM)

**Indexes**:
- UK_REINF_PGER_R2010_PREST_001 (UNIQUE): (ID_R2010_PREST, ID_R2010_TOM, CNPJ_PRESTADOR)

---

## REINF_PGER_R2010_PROC_ADIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2010_PROC_ADIC | NUMBER(12) | N |  |  |
| 2 | ID_R2010_OC | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 4 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 5 | COD_SUSP_ADIC | VARCHAR2(14) | Y |  |  |
| 6 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2010_PROC_ADIC

**FKs**:
- ID_R2010_OC → REINF_PGER_R2010_OC(ID_R2010_OC)

**Indexes**:
- UK_REINF_PGER_R2010_ADIC_001 (UNIQUE): (ID_R2010_PROC_ADIC, ID_R2010_OC)

---

## REINF_PGER_R2010_PROC_PRINC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2010_PROC_PRINC | NUMBER(12) | N |  |  |
| 2 | ID_R2010_OC | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 4 | NUM_PROC_ADJ_PRINC | VARCHAR2(21) | Y |  |  |
| 5 | COD_SUSP_PRINC | VARCHAR2(14) | Y |  |  |
| 6 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2010_PROC_PRINC

**FKs**:
- ID_R2010_OC → REINF_PGER_R2010_OC(ID_R2010_OC)

**Indexes**:
- UK_REINF_PGER_R2010_PRINC_001 (UNIQUE): (ID_R2010_PROC_PRINC, ID_R2010_OC)

---

## REINF_PGER_R2010_TOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2010_TOM | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2010_TOM |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | TP_INSCRICAO | CHAR(1) | N |  | Tipo de Inscricao (R2010 - ideEstabObra - tpInscEstab) Dominio: 1 - CNPJ 4 - CNO |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  | Tipo de Inscricao (R2010 - ideEstabObra - nrInscEstab) |

**PK**: ID_R2010_TOM

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R2010_TOM_001 (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## REINF_PGER_R2010_TP_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2010_TP_SERV | NUMBER(12) | N |  |  |
| 2 | ID_R2010_NF | NUMBER(12) | N |  |  |
| 3 | TP_SERVICO | NUMBER(9) | N |  |  |
| 4 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 5 | VLR_RETENCAO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RET_SUB | NUMBER(17,2) | Y |  |  |
| 7 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SERVICOS_15 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SERVICOS_20 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SERVICOS_25 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 12 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2010_TP_SERV

**FKs**:
- ID_R2010_NF → REINF_PGER_R2010_NF(ID_R2010_NF)

**Indexes**:
- UK_REINF_PGER_R2010_SERV_001 (UNIQUE): (ID_R2010_TP_SERV, ID_R2010_NF, TP_SERVICO)

---

## REINF_PGER_R2020_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2020_NF | NUMBER(12) | N |  |  |
| 2 | ID_R2020_OC | NUMBER(12) | N |  |  |
| 3 | SERIE | VARCHAR2(3) | N |  |  |
| 4 | NUM_DOCTO | VARCHAR2(15) | N |  |  |
| 5 | DAT_EMISSAO_NF | DATE | Y |  |  |
| 6 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 7 | OBSERVACAO | VARCHAR2(250) | Y |  |  |
| 8 | IDENT_DOCTO_FISCAL | NUMBER(22) | Y |  |  |

**PK**: ID_R2020_NF

**FKs**:
- ID_R2020_OC → REINF_PGER_R2020_OC(ID_R2020_OC)

**Indexes**:
- UK_REINF_PGER_R2020_NF_001 (UNIQUE): (ID_R2020_NF, ID_R2020_OC, SERIE, NUM_DOCTO)

---

## REINF_PGER_R2020_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2020_OC | NUMBER(12) | N |  |  |
| 2 | ID_R2020_TOM | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |
| 15 | IND_OBRA | CHAR(1) | Y |  |  |
| 16 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 18 | VLR_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 19 | VLR_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 21 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2020_OC

**FKs**:
- ID_R2020_TOM → REINF_PGER_R2020_TOM(ID_R2020_TOM)

**Indexes**:
- UK_REINF_PGER_R2020_OC_001 (UNIQUE): (ID_R2020_OC, ID_R2020_TOM, DAT_OCORRENCIA)

---

## REINF_PGER_R2020_PREST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2020_PREST | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2020_PREST |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | TP_INSCRICAO | CHAR(1) | N |  | Tipo de Inscricao (R2020 - ideEstabPrest - tpInscEstabPrest) Dominio: 1 - CNPJ |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  | Numero de Inscricao (R2020 - ideEstabPrest - nrInscEstabPrest) |

**PK**: ID_R2020_PREST

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R2020_PREST_001 (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## REINF_PGER_R2020_PROC_ADIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2020_PROC_ADIC | NUMBER(12) | N |  |  |
| 2 | ID_R2020_OC | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 4 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 5 | COD_SUSP_ADIC | VARCHAR2(14) | Y |  |  |
| 6 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2020_PROC_ADIC

**FKs**:
- ID_R2020_OC → REINF_PGER_R2020_OC(ID_R2020_OC)

**Indexes**:
- UK_REINF_PGER_R2020_ADIC_001 (UNIQUE): (ID_R2020_PROC_ADIC, ID_R2020_OC)

---

## REINF_PGER_R2020_PROC_PRINC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2020_PROC_PRINC | NUMBER(12) | N |  |  |
| 2 | ID_R2020_OC | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 4 | NUM_PROC_ADJ_PRINC | VARCHAR2(21) | Y |  |  |
| 5 | COD_SUSP_PRINC | VARCHAR2(14) | Y |  |  |
| 6 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2020_PROC_PRINC

**FKs**:
- ID_R2020_OC → REINF_PGER_R2020_OC(ID_R2020_OC)

**Indexes**:
- UK_REINF_PGER_R2020_PRINC_001 (UNIQUE): (ID_R2020_PROC_PRINC, ID_R2020_OC)

---

## REINF_PGER_R2020_TOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2020_TOM | NUMBER(12) | N |  |  |
| 2 | ID_R2020_PREST | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO_TOMADOR | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO_TOMADOR | VARCHAR2(14) | N |  |  |

**PK**: ID_R2020_TOM

**FKs**:
- ID_R2020_PREST → REINF_PGER_R2020_PREST(ID_R2020_PREST)

**Indexes**:
- UK_REINF_PGER_R2020_TOM_001 (UNIQUE): (ID_R2020_TOM, ID_R2020_PREST, TP_INSCRICAO_TOMADOR, NR_INSCRICAO_TOMADOR)

---

## REINF_PGER_R2020_TP_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2020_TP_SERV | NUMBER(12) | N |  |  |
| 2 | ID_R2020_NF | NUMBER(12) | N |  |  |
| 3 | TP_SERVICO | NUMBER(9) | N |  |  |
| 4 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 5 | VLR_RETENCAO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RET_SUB | NUMBER(17,2) | Y |  |  |
| 7 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SERVICOS_15 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SERVICOS_20 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SERVICOS_25 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 12 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2020_TP_SERV

**FKs**:
- ID_R2020_NF → REINF_PGER_R2020_NF(ID_R2020_NF)

**Indexes**:
- UK_REINF_PGER_R2020_SERV_001 (UNIQUE): (ID_R2020_TP_SERV, ID_R2020_NF, TP_SERVICO)

---

## REINF_PGER_R2040_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2040_ESTAB | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2040_ESTAB |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | TP_INSCRICAO | CHAR(1) | N |  | Tipo de Inscricao (R2040 - ideEstab - tpInscEstab) Dominio: 1 - CNPJ |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  | Numero de Inscricao (R2040 - ideEstab - nrInscEstab) |

**PK**: ID_R2040_ESTAB

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R2024_ESTAB_001 (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## REINF_PGER_R2040_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2040_OC | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2040_OC |
| 2 | ID_R2040_ESTAB | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | DAT_OCORRENCIA | DATE | N |  | Data de Ocorrencia |
| 4 | IND_STATUS | CHAR(1) | Y |  | Status de Controle das Ocorrencias. Dominio REINF_STATUS_PGER_V |
| 5 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificac?o unica do evento (R2020 - evtServPrest - id). |
| 7 | IND_OPER | CHAR(1) | Y |  | Identificao da Operacao (R2020 - ideEvento - indRetif). Dominio: 1 - Arquivo original  2 - Arquivo retificao. |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  | Numero do recibo do arquivo a ser retificado. (R2020 - ideEvento - nrRecibo). Preenchido quando o evento  de retificacao (IND_OPER = 2).  O numero do recibo do arquivo (evento) objeto da retificacao. |
| 9 | IND_TP_AMB | CHAR(1) | Y |  | Identificacao do ambiente (R2020 - ideEvento - tpAmb). Dominio 1 - Producao 2 - Producao restrita - dados reais; 3 - Producao restrita - dados ficticios. |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  | Processo de Emissao do Evento (R2020 - ideEvento - procEmi). Dominio 1 - Aplicativo do contribuinte; 2 - Aplicativo governamental. |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  | Versao do Processo de Emissao do Evento. (R2020 - ideEvento - verProc). Informar a versao do aplicativo emissor do evento. |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V. "v01_00_00". |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  | Status Apresentado no Painel de Eventos, campo Situacao. Dominio REINF_STATUS_PAINEL_V. |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_OUT. |

**PK**: ID_R2040_OC

**FKs**:
- ID_R2040_ESTAB → REINF_PGER_R2040_ESTAB(ID_R2040_ESTAB)

**Indexes**:
- UK_REINF_PGER_R2040_OC_001 (UNIQUE): (ID_R2040_ESTAB, DAT_OCORRENCIA)

---

## REINF_PGER_R2040_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2040_PROC | NUMBER(12) | N |  |  |
| 2 | ID_R2040_REPASSE | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 6 | VLR_N_RET | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2040_PROC

**FKs**:
- ID_R2040_REPASSE → REINF_PGER_R2040_REPASSE(ID_R2040_REPASSE)

**Indexes**:
- UK_REINF_PGER_R2040_PROC (UNIQUE): (ID_R2040_PROC, ID_R2040_REPASSE, IND_TP_PROC_ADJ, NUM_PROC_ADJ)

---

## REINF_PGER_R2040_REPASSE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2040_REPASSE | NUMBER(12) | N |  |  |
| 2 | ID_R2040_OC | NUMBER(12) | N |  |  |
| 3 | CNPJ_ASSOC_DESP | VARCHAR2(14) | N |  |  |
| 4 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 5 | VLR_RET | NUMBER(17,2) | Y |  |  |
| 6 | VLR_N_RET | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2040_REPASSE

**FKs**:
- ID_R2040_OC → REINF_PGER_R2040_OC(ID_R2040_OC)

**Indexes**:
- UK_REINF_PGER_R2040_REPASSE (UNIQUE): (ID_R2040_REPASSE, ID_R2040_OC, CNPJ_ASSOC_DESP)

---

## REINF_PGER_R2040_TP_REP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2040_TP_REP | NUMBER(12) | N |  |  |
| 2 | ID_R2040_REPASSE | NUMBER(12) | N |  |  |
| 3 | IND_TP_REP | CHAR(1) | N |  |  |
| 4 | DESC_RECURSO | VARCHAR2(21) | Y |  |  |
| 5 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RET | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2040_TP_REP

**FKs**:
- ID_R2040_REPASSE → REINF_PGER_R2040_REPASSE(ID_R2040_REPASSE)

**Indexes**:
- UK_REINF_PGER_R2040_TP_REP (UNIQUE): (ID_R2040_TP_REP, ID_R2040_REPASSE, IND_TP_REP)

---

## REINF_PGER_R2050_COM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2050_COM | NUMBER(12) | N |  |  |
| 2 | ID_R2050_OC | NUMBER(12) | N |  |  |
| 3 | IND_COM | CHAR(1) | N |  |  |
| 4 | VLR_REC_BRT | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2050_COM

**FKs**:
- ID_R2050_OC → REINF_PGER_R2050_OC(ID_R2050_OC)

**Indexes**:
- UK_REINF_PGER_R2050_COM_001 (UNIQUE): (ID_R2050_COM, ID_R2050_OC, IND_COM)

---

## REINF_PGER_R2050_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2050_ESTAB | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  |  |

**PK**: ID_R2050_ESTAB

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R2050_ESTAB (UNIQUE): (ID_R2050_ESTAB, ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## REINF_PGER_R2050_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2050_NF | NUMBER(12) | N |  |  |
| 2 | ID_R2050_COM | NUMBER(12) | N |  |  |
| 3 | SERIE | VARCHAR2(3) | N |  |  |
| 4 | NUM_DOCTO | VARCHAR2(12) | N |  |  |
| 5 | DAT_EMISSAO_NF | DATE | N |  |  |
| 6 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_RAT | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SENAR | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2050_NF

**FKs**:
- ID_R2050_COM → REINF_PGER_R2050_COM(ID_R2050_COM)

**Indexes**:
- UK_REINF_PGER_R2050_NF_001 (UNIQUE): (ID_R2050_NF, ID_R2050_COM, SERIE, NUM_DOCTO, DAT_EMISSAO_NF)

---

## REINF_PGER_R2050_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2050_OC | NUMBER(12) | N |  |  |
| 2 | ID_R2050_ESTAB | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |
| 15 | VLR_REC_BRT_TOT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_CP_APUR | NUMBER(17,2) | Y |  |  |
| 17 | VLR_RAT_APUR | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SENAR_APUR | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CP_SUSP_TOT | NUMBER(17,2) | Y |  |  |
| 20 | VLR_RAT_SUSP_TOT | NUMBER(17,2) | Y |  |  |
| 21 | VLR_SENAR_SUSP_TOT | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2050_OC

**FKs**:
- ID_R2050_ESTAB → REINF_PGER_R2050_ESTAB(ID_R2050_ESTAB)

**Indexes**:
- UK_REINF_PGER_R2050_OC_001 (UNIQUE): (ID_R2050_OC, ID_R2050_ESTAB, DAT_OCORRENCIA)

---

## REINF_PGER_R2050_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2050_PROC | NUMBER(12) | N |  |  |
| 2 | ID_R2050_COM | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 6 | VLR_CP_SUSP | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RAT_SUSP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SENAR_SUSP | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2050_PROC

**FKs**:
- ID_R2050_COM → REINF_PGER_R2050_COM(ID_R2050_COM)

**Indexes**:
- UK_REINF_PGER_R2050_PROC_001 (UNIQUE): (ID_R2050_PROC, ID_R2050_COM, IND_TP_PROC_ADJ, NUM_PROC_ADJ)

---

## REINF_PGER_R2055_DETAQUIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2055_DETAQUIS | NUMBER(12) | N |  |  |
| 2 | ID_R2055_PRODUTOR | NUMBER(12) | Y |  |  |
| 3 | IND_AQUIS | VARCHAR2(1) | Y |  |  |
| 4 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 5 | VLR_CP_DESC_PR | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RAT_DESC_PR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SENAR_DESC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2055_DETAQUIS

**FKs**:
- ID_R2055_PRODUTOR → REINF_PGER_R2055_PRODUTOR(ID_R2055_PRODUTOR)

**Indexes**:
- UK_REINF_PGER_R2055_DAQUIS_01 (UNIQUE): (ID_R2055_PRODUTOR, IND_AQUIS)

---

## REINF_PGER_R2055_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2055_ESTAB | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | Y |  |  |
| 3 | TP_INSCRICAO | VARCHAR2(1) | Y |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(15) | Y |  |  |

**PK**: ID_R2055_ESTAB

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R2055_ESTAB_01 (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## REINF_PGER_R2055_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2055_NF | NUMBER(12) | N |  |  |
| 2 | ID_R2055_DETAQUIS | NUMBER(12) | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | DATA_FISCAL | DATE | Y |  |  |
| 10 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 11 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 12 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CP_DESC_PR | NUMBER(17,2) | Y |  |  |
| 14 | VLR_RAT_DESC_PR | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SENAR_DESC | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2055_NF

**FKs**:
- ID_R2055_DETAQUIS → REINF_PGER_R2055_DETAQUIS(ID_R2055_DETAQUIS)

---

## REINF_PGER_R2055_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2055_OC | NUMBER(12) | N |  |  |
| 2 | ID_R2055_ESTAB | NUMBER(12) | Y |  |  |
| 3 | DAT_OCORRENCIA | DATE | Y |  |  |
| 4 | IND_STATUS | VARCHAR2(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | VARCHAR2(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | VARCHAR2(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | VARCHAR2(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | IND_RETIF_S1250 | VARCHAR2(1) | Y |  |  |
| 13 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 14 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 15 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |
| 16 | TP_INSCRICAO_PROD | VARCHAR2(1) | Y |  |  |
| 17 | NR_INSCRICAO_PROD | VARCHAR2(14) | Y |  |  |

**PK**: ID_R2055_OC

**FKs**:
- ID_R2055_ESTAB → REINF_PGER_R2055_ESTAB(ID_R2055_ESTAB)

**Indexes**:
- UK_REINF_PGER_R2055_OC_01 (UNIQUE): (ID_R2055_ESTAB, DAT_OCORRENCIA, TP_INSCRICAO_PROD, NR_INSCRICAO_PROD)

---

## REINF_PGER_R2055_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2055_PROC | NUMBER(12) | N |  |  |
| 2 | ID_R2055_DETAQUIS | NUMBER(12) | Y |  |  |
| 3 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 4 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 5 | VLR_CPN_NRET | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RAT_NRET | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SENAR_NRET | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2055_PROC

**FKs**:
- ID_R2055_DETAQUIS → REINF_PGER_R2055_DETAQUIS(ID_R2055_DETAQUIS)

**Indexes**:
- UK_REINF_PGER_R2055_PROC_01 (UNIQUE): (ID_R2055_DETAQUIS, NUM_PROC_ADJ, COD_SUSP)

---

## REINF_PGER_R2055_PRODUTOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2055_PRODUTOR | NUMBER(12) | N |  |  |
| 2 | ID_R2055_OC | NUMBER(12) | Y |  |  |
| 3 | TP_INSCRICAO_PROD | VARCHAR2(1) | Y |  |  |
| 4 | NR_INSCRICAO_PROD | VARCHAR2(14) | Y |  |  |
| 5 | IND_OPC_CP | VARCHAR2(1) | Y |  |  |

**PK**: ID_R2055_PRODUTOR

**FKs**:
- ID_R2055_OC → REINF_PGER_R2055_OC(ID_R2055_OC)

**Indexes**:
- UK_REINF_PGER_R2055_PROD_01 (UNIQUE): (ID_R2055_OC, TP_INSCRICAO_PROD, NR_INSCRICAO_PROD)

---

## REINF_PGER_R2060_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2060_AJUSTE | NUMBER(12) | N |  |  |
| 2 | ID_R2060_ATIV | NUMBER(12) | N |  |  |
| 3 | IND_TP_AJUSTE | CHAR(1) | N |  |  |
| 4 | COD_AJUSTE | VARCHAR2(2) | N |  |  |
| 5 | DAT_AJUSTE | DATE | Y |  |  |
| 6 | DSC_AJUSTE | VARCHAR2(400) | Y |  |  |
| 7 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2060_AJUSTE

**FKs**:
- ID_R2060_ATIV → REINF_PGER_R2060_ATIV(ID_R2060_ATIV)

---

## REINF_PGER_R2060_ATIV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2060_ATIV | NUMBER(12) | N |  |  |
| 2 | ID_R2060_OC | NUMBER(12) | N |  |  |
| 3 | COD_ATIV_ECON | VARCHAR2(8) | N |  |  |
| 4 | VLR_REC_BRT_ATIV | NUMBER(17,2) | Y |  |  |
| 5 | VLR_EXC_REC_BRT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ADIC_REC_BRT | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_CPRB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CPRB | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2060_ATIV

**FKs**:
- ID_R2060_OC → REINF_PGER_R2060_OC(ID_R2060_OC)

**Indexes**:
- UK_REINF_PGER_R2060_ATIV_001 (UNIQUE): (ID_R2060_ATIV, ID_R2060_OC, COD_ATIV_ECON)

---

## REINF_PGER_R2060_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2060_ESTAB | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2060_ESTAB |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | TP_INSCRICAO | CHAR(1) | N |  | Tipo de Inscricao (R2060 - ideEstab - tpInscEstab) Dominio: 1 - CNPJ |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  | Tipo de Inscricao (R2060 - ideEstab - nrInscEstab) |

**PK**: ID_R2060_ESTAB

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R2060_ESTAB_001 (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## REINF_PGER_R2060_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2060_NF | NUMBER(12) | N |  |  |
| 2 | ID_R2060_ATIV | NUMBER(12) | N |  |  |
| 3 | SERIE | VARCHAR2(3) | N |  |  |
| 4 | NUM_DOCTO | VARCHAR2(12) | N |  |  |
| 5 | DAT_EMISSAO_NF | DATE | N |  |  |
| 6 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2060_NF

**FKs**:
- ID_R2060_ATIV → REINF_PGER_R2060_ATIV(ID_R2060_ATIV)

**Indexes**:
- UK_REINF_PGER_R2060_NF_001 (UNIQUE): (ID_R2060_NF, ID_R2060_ATIV, SERIE, NUM_DOCTO, DAT_EMISSAO_NF)

---

## REINF_PGER_R2060_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2060_OC | NUMBER(12) | N |  |  |
| 2 | ID_R2060_ESTAB | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |
| 15 | VLR_REC_BRT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_CONT_PREV | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CONT_PREV_SUSP | NUMBER(17,2) | Y |  |  |

**PK**: ID_R2060_OC

**FKs**:
- ID_R2060_ESTAB → REINF_PGER_R2060_ESTAB(ID_R2060_ESTAB)

---

## REINF_PGER_R2060_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2060_PROC | NUMBER(12) | N |  |  |
| 2 | ID_R2060_OC | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 6 | VLR_CONT_PREV_SUSP_PROC | NUMBER(17,2) | Y |  |  |
| 7 | COD_ATIV_ECON | VARCHAR2(8) | Y |  |  |

**PK**: ID_R2060_PROC

**FKs**:
- ID_R2060_OC → REINF_PGER_R2060_OC(ID_R2060_OC)

**Indexes**:
- UK_REINF_PGER_R2060_PROC_001 (UNIQUE): (ID_R2060_PROC, ID_R2060_OC)

---

## REINF_PGER_R2070_ADV_JUD_BPF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_ADV_JUD_BPF | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_ADV_J_BPF |
| 2 | ID_R2070_INFO_JUD_BPF | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | TP_INSCRICAO_ADV | CHAR(1) | N |  | Tipo de Inscricao (evento R2070 - pagtoBPF - infoProcJudi - ideAdvog - tpInscricao) Dominio: 1 - Pessoa Juridica 2 - Pessoa Fisica |
| 4 | NR_INSCRICAO_ADV | VARCHAR2(14) | N |  | Numero de Inscricao (evento R2070 - pagtoBPF - infoProcJudi - ideAdvog - nrInscricao) |
| 5 | VLR_ADV | NUMBER(17,2) | Y |  | Valor de despesa com advogado (evento R2070 - pagtoBPF - infoProcJudi - ideAdvog - vlrAdvogado) |

**PK**: ID_R2070_ADV_JUD_BPF

**FKs**:
- ID_R2070_INFO_JUD_BPF → REINF_PGER_R2070_INFO_JUD_BPF(ID_R2070_INFO_JUD_BPF)

**Indexes**:
- UK_REINF_PGER_R2070_ADV_JUD_PF (UNIQUE): (ID_R2070_INFO_JUD_BPF, TP_INSCRICAO_ADV, NR_INSCRICAO_ADV)

---

## REINF_PGER_R2070_ADV_JUD_BPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_ADV_JUD_BPJ | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_ADV_J_BPJ |
| 2 | ID_R2070_INFO_JUD_BPJ | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | TP_INSCRICAO_ADV | CHAR(1) | N |  | Tipo de Inscricao (evento R2070 - pagtoBPJ - infoProcJudi - ideAdvog - tpInscricao) Dominio: 1 - Pessoa Jurdica 2 - Pessoa Fsica |
| 4 | NR_INSCRICAO_ADV | VARCHAR2(14) | N |  | Numero de Inscricao (evento R2070 - pagtoBPJ - infoProcJudi - ideAdvog - nrInscricao) |
| 5 | VLR_ADV | NUMBER(17,2) | Y |  | Valor de despesa com advogado (evento R2070 - pagtoBPJ - infoProcJudi - ideAdvog - vlrAdvogado) |

**PK**: ID_R2070_ADV_JUD_BPJ

**FKs**:
- ID_R2070_INFO_JUD_BPJ → REINF_PGER_R2070_INFO_JUD_BPJ(ID_R2070_INFO_JUD_BPJ)

**Indexes**:
- UK_REINF_PGER_R2070_ADV_JUD_PJ (UNIQUE): (ID_R2070_INFO_JUD_BPJ, TP_INSCRICAO_ADV, NR_INSCRICAO_ADV)

---

## REINF_PGER_R2070_ADV_RRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_ADV_RRA | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_ADV_RRA |
| 2 | ID_R2070_INFO_RRA | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | TP_INSCRICAO_ADV | CHAR(1) | N |  | Tipo de Inscricao (evento R2070 - pagtoBPF - infoRRA - ideAdvog - tpInscricao) Dominio: 1 - Pessoa Juridica 2 - Pessoa Fisica |
| 4 | NR_INSCRICAO_ADV | VARCHAR2(14) | N |  | Numero de Inscricao (evento R2070 - pagtoBPF - infoRRA - ideAdvog - nrInscricao) |
| 5 | VLR_ADV | NUMBER(17,2) | Y |  | Valor de despesa com advogado (evento R2070 - pagtoBPF - infoRRA - ideAdvog - vlrAdvogado) |

**PK**: ID_R2070_ADV_RRA

**FKs**:
- ID_R2070_INFO_RRA → REINF_PGER_R2070_INFO_RRA(ID_R2070_INFO_RRA)

**Indexes**:
- UK_REINF_PGER_R2070_ADV_RRA (UNIQUE): (ID_R2070_INFO_RRA, TP_INSCRICAO_ADV, NR_INSCRICAO_ADV)

---

## REINF_PGER_R2070_BENEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_BENEF | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_BENEF |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | COD_PAGTO | VARCHAR2(4) | N |  | Codigo de Pagamento (DARF) (evento R2070 - ideBeneficiario - codPagamento) |
| 4 | COD_BENEF | VARCHAR2(50) | N |  | Campo chave de identificacao do beneficiario. Campo nao pertence ao layout do evento R-2070 |
| 5 | IND_BENEF | CHAR(1) | Y |  | Indicador que classifica o beneficiario em PF, PJ, Exterior. Campo nao pertence ao layout do evento R-2070 Dominio: 1 - Beneficiario residente no Brasil - Pessoa Fisica 2 - Beneficiario residente no Brasil - Pessoa Juridica 3 - Beneficiario residente no exterior |
| 6 | TP_INSCRICAO | CHAR(1) | Y |  | Tipo de Beneficiario (evento R2070 - ideBeneficiario - tpInscBeneficiario): 1 - Pessoa Juriica 2 - Pessoa Fisica |
| 7 | NR_INSCRICAO | VARCHAR2(14) | Y |  | Numero de Inscricao do Beneficiario (evento R2070 - ideBeneficiario - nrInscBeneficiario). |

**PK**: ID_R2070_BENEF

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R2070_BENEF_001 (UNIQUE): (ID_PGER_APUR, COD_PAGTO, COD_BENEF)

---

## REINF_PGER_R2070_DEDUCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_DEDUCAO | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_DEDUCAO |
| 2 | ID_R2070_PAGTO_BPF | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | IND_TP_DEDUCAO | CHAR(1) | N |  | Indicativo do Tipo de Deducao. (evento R2070 - pagtoBPF - detDeducao - indTpDeducao) Dominio 1 - Previdência Oficial; 2 - Previdência Privada; 3 - Fapi; 4 - Funpresp; 5 - Pensão Alimentícia; 6 - Dependentes; |
| 4 | VLR_DEDUCAO | NUMBER(17,2) | Y |  | Valor da deducao da base de calculo. (evento R2070 - pagtoBPF - detDeducao - vlrDeducao) |

**PK**: ID_R2070_DEDUCAO

**FKs**:
- ID_R2070_PAGTO_BPF → REINF_PGER_R2070_PAGTO_BPF(ID_R2070_PAGTO_BPF)

**Indexes**:
- UK_REINF_PGER_R2070_DEDUCAO (UNIQUE): (ID_R2070_PAGTO_BPF, IND_TP_DEDUCAO)

---

## REINF_PGER_R2070_DET_COMPET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_COMP_JUD | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_DET_COMPE |
| 2 | ID_R2070_PAGTO_BPF | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | IND_PER_REF | CHAR(1) | N |  | Indicativo de periodo de referencia. (evento R2070 - pagtoBPF - detCompetencia - indPerReferencia) Dominio: 1 - Folha de Pagamento Mensal 2 - Folha do Decimo Terceiro Salario |
| 4 | ANO_PER_REF | VARCHAR2(4) | N |  | Ano do periodo de referencia. (evento R2070 - pagtoBPF - detCompetencia - perRefPagto) |
| 5 | MES_PER_REF | VARCHAR2(2) | Y |  | Mes do periodo de referencia. (evento R2070 - pagtoBPF - detCompetencia - perRefPagto) |
| 6 | VLR_REND | NUMBER(17,2) | Y |  | Valor do Rendimento Tributavel (evento R2070 - pagtoBPF - detCompetencia - vlrRendTributavel) |

**PK**: ID_R2070_COMP_JUD

**FKs**:
- ID_R2070_PAGTO_BPF → REINF_PGER_R2070_PAGTO_BPF(ID_R2070_PAGTO_BPF)

**Indexes**:
- UK_REINF_PGER_R2070_DET_COMP (UNIQUE): (ID_R2070_PAGTO_BPF, IND_PER_REF, ANO_PER_REF, MES_PER_REF)

---

## REINF_PGER_R2070_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_ESTAB | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_ESTAB |
| 2 | ID_R2070_OC | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | TP_INSCRICAO | CHAR(1) | N |  | Tipo de Inscrição do Estabelecimento (evento R2070 - ideEstab - tpInsc) |
| 4 | NUM_INSCRICAO | VARCHAR2(14) | N |  | Numero de Inscrição do Estabelecimento (evento R2070 - ideEstab - nrInsc) |

**PK**: ID_R2070_ESTAB

**FKs**:
- ID_R2070_OC → REINF_PGER_R2070_OC(ID_R2070_OC)

**Indexes**:
- UK_REINF_PGER_R2070_ESTAB_001 (UNIQUE): (ID_R2070_OC, TP_INSCRICAO, NUM_INSCRICAO)

---

## REINF_PGER_R2070_INFO_JUD_BPF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_INFO_JUD_BPF | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_INF_J_BPF |
| 2 | ID_R2070_PAGTO_BPF | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | NUM_PROC_ADJ | VARCHAR2(21) | N |  | (evento R2070 - pagtoBPF - infoProcJudi - nrProcJud) |
| 4 | COD_SUSP | VARCHAR2(14) | Y |  | (evento R2070 - pagtoBPF - infoProcJudi - codSusp) |
| 5 | IND_ORIG_REC | CHAR(1) | Y |  | Indicativo da origem dos recursos. (evento R2070 - pagtoBPF - infoProcJudi - indOrigemRecursos). Dominio: 1 - Recursos do proprio declarante 2 - Recursos de terceiros; |
| 6 | VLR_DESP_JUD | NUMBER(17,2) | Y |  | (evento R2070 - pagtoBPF - infoProcJudi - despProcJudi - vlrDespCustas) |
| 7 | VLR_DESP_ADVOGADO | NUMBER(17,2) | Y |  | (evento R2070 - pagtoBPF - infoProcJudi - despProcJudi - vlrDespAdvogados) |
| 8 | NUM_CNPJ_ORIG_REC | VARCHAR2(14) | Y |  | (evento R2070 - pagtoBPF - infoProcJudi - origemRecurso - cnpjOrigemRecursos) |

**PK**: ID_R2070_INFO_JUD_BPF

**FKs**:
- ID_R2070_PAGTO_BPF → REINF_PGER_R2070_PAGTO_BPF(ID_R2070_PAGTO_BPF)

**Indexes**:
- UK_REINF_PGER_R2070_INF_JUD_PF (UNIQUE): (ID_R2070_PAGTO_BPF, NUM_PROC_ADJ, COD_SUSP)

---

## REINF_PGER_R2070_INFO_JUD_BPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_INFO_JUD_BPJ | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_INF_J_BPJ |
| 2 | ID_R2070_PAGTO_BPJ | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | NUM_PROC_ADJ | VARCHAR2(21) | N |  | (evento R2070 - pagtoBPJ - infoProcJudi - nrProcJud) |
| 4 | COD_SUSP | VARCHAR2(14) | Y |  | (evento R2070 - pagtoBPJ - infoProcJudi - codSusp) |
| 5 | IND_ORIG_REC | CHAR(1) | Y |  | Indicativo da origem dos recursos. (evento R2070 - pagtoBPJ - infoProcJudi - indOrigemRecursos). Dominio: 1 - Recursos do proprio declarante 2 - Recursos de terceiros; |
| 6 | VLR_DESP_JUD | NUMBER(17,2) | Y |  | (evento R2070 - pagtoBPJ - infoProcJudi - despProcJudi - vlrDespCustas) |
| 7 | VLR_DESP_ADVOGADO | NUMBER(17,2) | Y |  | (evento R2070 - pagtoBPJ - infoProcJudi - despProcJudi - vlrDespAdvogados) |
| 8 | NUM_CNPJ_ORIG_REC | VARCHAR2(14) | Y |  | (evento R2070 - pagtoBPJ - infoProcJudi - origemRecurso - cnpjOrigemRecursos) |

**PK**: ID_R2070_INFO_JUD_BPJ

**FKs**:
- ID_R2070_PAGTO_BPJ → REINF_PGER_R2070_PAGTO_BPJ(ID_R2070_PAGTO_BPJ)

**Indexes**:
- UK_REINF_PGER_R2070_INF_JUD_PJ (UNIQUE): (ID_R2070_PAGTO_BPJ, NUM_PROC_ADJ, COD_SUSP)

---

## REINF_PGER_R2070_INFO_RRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_INFO_RRA | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_INFO_RRA |
| 2 | ID_R2070_PAGTO_BPF | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  | Tipo de Processo (evento R2070 - pagtoBPF - infoRRA - tpProcRRA). Dominio: 1 - Administrativo 2 - Judicial |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  | Numero do Processo (evento R2070 - pagtoBPF - infoRRA - nrProcRRA). |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  | (evento R2070 - pagtoBPF - infoRRA - codSusp). |
| 6 | DSC_NAT_REND | VARCHAR2(50) | Y |  | (evento R2070 - pagtoBPF - infoRRA - natRRA). |
| 7 | QTDE_MESES | NUMBER(5) | Y |  | (evento R2070 - pagtoBPF - infoRRA - qtdMesesRRA). |
| 8 | VLR_DESP_JUD | NUMBER(17,2) | Y |  | (evento R2070 - pagtoBPF - infoRRA - despProcJudicial - vlrDespCustas) |
| 9 | VLR_DESP_ADVOGADO | NUMBER(17,2) | Y |  | (evento R2070 - pagtoBPF -infoRRA - despProcJudicial - vlrDespAdvogados) |

**PK**: ID_R2070_INFO_RRA

**FKs**:
- ID_R2070_PAGTO_BPF → REINF_PGER_R2070_PAGTO_BPF(ID_R2070_PAGTO_BPF)

**Indexes**:
- UK_REINF_PGER_R2070_INFO_RRA (UNIQUE): (ID_R2070_PAGTO_BPF, IND_TP_PROC_ADJ, NUM_PROC_ADJ, COD_SUSP)

---

## REINF_PGER_R2070_ISENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_ISENTO | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_ISENTO |
| 2 | ID_R2070_PAGTO_BPF | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | IND_TP_ISENCAO | VARCHAR2(2) | N |  | Tipo de Isencao (evento R2070 - pagtoBPF - rendIsento - tpIsencao) Dominio: 1 - Parcela Isenta 65 anos; 2 - Diaria e Ajuda de Custo; 3 - Indenizacao e rescisao de contrato, inclusive a titulo de PDV; 4 - Abono pecuniario; 5 - Outros (especificar); 6 - Lucros e dividendos pagos a partir de 1996; 7 - Valores pagos a titular ou socio de microempresa ou empresa de pequeno porte, exceto pro-labore e alugueis; 8 - Pensao, aposentadoria ou reforma por molestia grave ou acidente em servico; 9 - Beneficios indiretos e/ou reembolso de despesas recebidas por voluntrio da copa do mundo ou da copa das confederacoes; 10 - Bolsa de estudo recebida por medico-residente; 11 - Complementacao de aposentadoria, correspondente as contribuicoes efetuadas no periodo de 01/01/1989 a 31/12/1995. |
| 4 | VLR_ISENCAO | NUMBER(17,2) | Y |  | Valor de Isencao (evento R2070 - pagtoBPF - rendIsento - vlrIsento) |
| 5 | DSC_RENDIMENTO | VARCHAR2(100) | Y |  | Descricao do Rendimento (evento R2070 - pagtoBPF - rendIsento - descRendimento) |

**PK**: ID_R2070_ISENTO

**FKs**:
- ID_R2070_PAGTO_BPF → REINF_PGER_R2070_PAGTO_BPF(ID_R2070_PAGTO_BPF)

**Indexes**:
- UK_REINF_PGER_R2070_ISENTO (UNIQUE): (ID_R2070_PAGTO_BPF, IND_TP_ISENCAO)

---

## REINF_PGER_R2070_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_OC | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_OC |
| 2 | ID_R2070_BENEF | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | DAT_OCORRENCIA | DATE | N |  | Data de Ocorrencia |
| 4 | IND_STATUS | CHAR(1) | Y |  | Status de Controle das Ocorrencias. Dominio REINF_STATUS_PGER_V |
| 5 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificac?o unica do evento (R2070 - evtPgtosDivs - id). |
| 7 | IND_OPER | CHAR(1) | Y |  | Identificao da Operacao (R2070 - ideEvento - indRetif). Dominio: 1 - Arquivo original  2 - Arquivo retificao. |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  | Numero do recibo do arquivo a ser retificado. (R2070 - ideEvento - nrRecibo). Preenchido quando o evento  de retificacao (IND_OPER = 2).  O numero do recibo do arquivo (evento) objeto da retificacao. |
| 9 | IND_TP_AMB | CHAR(1) | Y |  | Identificacao do ambiente (R2070 - ideEvento - tpAmb). Dominio 1 - Producao 2 - Producao restrita - dados reais; 3 - Producao restrita - dados ficticios. |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  | Processo de Emissao do Evento (R2070 - ideEvento - procEmi). Dominio 1 - Aplicativo do contribuinte; 2 - Aplicativo governamental. |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  | Versao do Processo de Emissao do Evento. (R2070 - ideEvento - verProc). Informar a versao do aplicativo emissor do evento. |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V. "v01_00_00". |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  | Status Apresentado no Painel de Eventos, campo Situacao. Dominio REINF_STATUS_PAINEL_V. |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_OUT. |
| 15 | NOME_BENEF | VARCHAR2(150) | Y |  | Nome ou Razao Social do Beneficiario (evento R2070 - ideBeneficiario - nomeRazaoBeneficiario). |
| 16 | DAT_MOLESTIA | DATE | Y |  | Data do laudo da moletia grave (evento R2070 - ideBeneficiario - dadosMolestiaGrave - dtLaudo). |

**PK**: ID_R2070_OC

**FKs**:
- ID_R2070_BENEF → REINF_PGER_R2070_BENEF(ID_R2070_BENEF)

**Indexes**:
- UK_REINF_PGER_R2070_OC_001 (UNIQUE): (ID_R2070_BENEF, DAT_OCORRENCIA)

---

## REINF_PGER_R2070_PAGTO_BPF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_PAGTO_BPF | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_PAGTO_BPF |
| 2 | ID_R2070_ESTAB | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | DAT_PAGTO | DATE | Y |  | Data de Pagamento (evento R2070 - pagtoBPF - dtPagto) |
| 4 | IND_SUSP_EXIG | CHAR(1) | N |  | Indicativo de Exigibilidade Suspensa. (evento R2070 - pagtoBPF - indSuspExigibilidade) Dominio: S - Sim N - Nao |
| 5 | IND_DEC_TERC | CHAR(1) | N |  | Indicativo de Decimo Terceiro. (evento R2070 - pagtoBPF - indDecTerceiro) Dominio: S - Sim N - Nao |
| 6 | VLR_REND | NUMBER(17,2) | Y |  | Valor do rendimento tributavel (evento R2070 - pagtoBPF - vlrRendTributavel). |
| 7 | VLR_IRRF | NUMBER(17,2) | Y |  | Valor do Imposto Retido na Fonte. (evento R2070 - pagtoBPF - vlrIRRF). |
| 8 | VLR_COMP_JUD_CALEND | NUMBER(17,2) | Y |  | Compensacao Judicial do ano calendario (evento R2070 - pagtoBPF - compJudicial - vlrCompAnoCalendario). |
| 9 | VLR_COMP_JUD_ANTERIOR | NUMBER(17,2) | Y |  | Compensacao Judicial do anos anteriores (evento R2070 - pagtoBPF - compJudicial - vlrcompAnosAnteriores). |
| 10 | VLR_DEP_JUD | NUMBER(17,2) | Y |  | Valor do Deposito Judicial (evento R2070 - pagtoBPF - depJudicial - vlrDepJudicial). |

**PK**: ID_R2070_PAGTO_BPF

**FKs**:
- ID_R2070_ESTAB → REINF_PGER_R2070_ESTAB(ID_R2070_ESTAB)

**Indexes**:
- UK_REINF_PGER_R2070_PAGTO_BPF (UNIQUE): (ID_R2070_ESTAB, DAT_PAGTO, IND_SUSP_EXIG, IND_DEC_TERC)

---

## REINF_PGER_R2070_PAGTO_BPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_PAGTO_BPJ | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_PAGTO_BPJ |
| 2 | ID_R2070_ESTAB | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | DAT_PAGTO | DATE | Y |  | (evento R2070 - pagtoBPJ - dtPagto) |
| 4 | VLR_REND | NUMBER(17,2) | Y |  | (evento R2070 - pagtoBPJ - vlrRendTributavel) |
| 5 | VLR_IRRF | NUMBER(17,2) | Y |  | (evento R2070 - pagtoBPJ - vlrRet) |

**PK**: ID_R2070_PAGTO_BPJ

**FKs**:
- ID_R2070_ESTAB → REINF_PGER_R2070_ESTAB(ID_R2070_ESTAB)

**Indexes**:
- UK_REINF_PGER_R2070_PAGTO_BPJ (UNIQUE): (ID_R2070_ESTAB, DAT_PAGTO)

---

## REINF_PGER_R2070_PAGTO_EX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_PAGTO_EX | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_PAGTO_EX |
| 2 | ID_R2070_ESTAB | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | DAT_PAGTO | DATE | Y |  | (evento R2070 - pagtoResidExterior - dtPagto) |
| 4 | TP_RENDIMENTO | VARCHAR2(3) | Y |  | (evento R2070 - pagtoResidExterior - tpRendimento) |
| 5 | TP_FORMA_TRIBUTACAO | VARCHAR2(2) | Y |  | (evento R2070 - pagtoResidExterior - formaTributacao) |
| 6 | VLR_PAGTO | NUMBER(17,2) | Y |  | (evento R2070 - pagtoResidExterior - vlrPgto) |
| 7 | VLR_IRRF | NUMBER(17,2) | Y |  | (evento R2070 - pagtoResidExterior - vlrRet) |

**PK**: ID_R2070_PAGTO_EX

**FKs**:
- ID_R2070_ESTAB → REINF_PGER_R2070_ESTAB(ID_R2070_ESTAB)

**Indexes**:
- UK_REINF_PGER_R2070_PAGTO_EX (UNIQUE): (ID_R2070_ESTAB, DAT_PAGTO, TP_RENDIMENTO)

---

## REINF_PGER_R2070_RESID_EX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2070_RESID_EX | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2070_RESID_EX |
| 2 | ID_R2070_OC | NUMBER(12) | N |  | Identificador do registro pai |
| 3 | COD_PAIS | VARCHAR2(3) | Y |  | Codigo do Pais (evento R2070 - dadosResidExterior- dadosEndereco - paisResid). |
| 4 | DSC_LOGRADOURO | VARCHAR2(80) | Y |  | (evento R2070 - dadosResidExterior- dadosEndereco - descLogradouro). |
| 5 | NUM_LOGRADOURO | VARCHAR2(10) | Y |  | (evento R2070 - dadosResidExterior- dadosEndereco - nrLograd). |
| 6 | DSC_COMPLEMENTO | VARCHAR2(45) | Y |  | (evento R2070 - dadosResidExterior- dadosEndereco - complemento). |
| 7 | BAIRRO | VARCHAR2(60) | Y |  | (evento R2070 - dadosResidExterior- dadosEndereco - bairro). |
| 8 | CIDADE | VARCHAR2(30) | Y |  | (evento R2070 - dadosResidExterior- dadosEndereco - cidade). |
| 9 | COD_POSTAL | VARCHAR2(12) | Y |  | (evento R2070 - dadosResidExterior- dadosEndereco - codPostal). |
| 10 | IND_NIF | CHAR(1) | Y |  | Indicativo do Numero de IdentificacaoFiscal.  (evento R2070 - dadosResidExterior- dadosFiscais- indNIF). Dominio: 1 - Beneficirio com NIF; 2 - Beneficirio dispensado do NIF; 3 - Pas no exige NIF. |
| 11 | NUM_NIF | VARCHAR2(30) | Y |  | Numero de IdentificacaoFiscal - NIF. (evento R2070 - dadosResidExterior- dadosFiscais- nifBenef). |
| 12 | TP_FONTE_PAGADORA | VARCHAR2(3) | Y |  | (evento R2070 - dadosResidExterior- dadosFiscais- relFontePagadora). |

**PK**: ID_R2070_RESID_EX

**FKs**:
- ID_R2070_OC → REINF_PGER_R2070_OC(ID_R2070_OC)

**Indexes**:
- UK_REINF_PGER_R2070_RESID_EX (UNIQUE): (ID_R2070_OC)

---

## REINF_PGER_R2098_R2099_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2098_R2099_OC | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2098_R2099_OC |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | DAT_OCORRENCIA | DATE | N |  | Data de Ocorrencia |
| 4 | IND_STATUS | CHAR(1) | Y |  | Status de Controle das Ocorrências.  Dominio REINF_STATUS_PGER_V |
| 5 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificaão nica do evento (R2098 - evtReabreEvPer- id, R2099 - evtFechaEvPer- id). |
| 7 | IND_OPER | CHAR(1) | Y |  | Nao se aplica aos eventos R-2098, R-2099. |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  | Nao se aplica aos eventos R-2098, R-2099. |
| 9 | IND_TP_AMB | CHAR(1) | Y |  | Identificacao do ambiente (R2098, R2099 - ideEvento - tpAmb). Dominio 1 - Producao 2 - Producao restrita - dados reais; 3 - Producao restrita - dados ficticios. |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  | Processo de Emissao do Evento (R2098, R2099 - ideEvento - procEmi). Dominio 1 - Aplicativo do contribuinte; 2 - Aplicativo governamental. |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  | Versao do Processo de Emissao do Evento. (R2098, R2099 - ideEvento - verProc). Informar a versao do aplicativo emissor do evento. |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V. "v01_00_00". |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  | Status Apresentado no Painel de Eventos, campo Situacao. Dominio REINF_STATUS_PAINEL_V. |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_OUT. |
| 15 | TIPO_EVENTO | VARCHAR2(50) | Y |  | Dominio: R-2098,  R-2099 |

**PK**: ID_R2098_R2099_OC

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R2098_R2099_OC (UNIQUE): (ID_PGER_APUR, DAT_OCORRENCIA)

---

## REINF_PGER_R2099_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R2099_COMPL | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R2099_COMPL |
| 2 | ID_R2098_R2099_OC | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | NOME_CONTATO | VARCHAR2(70) | Y |  | Nome do Contato Responsvel pela Informaão. (R2099 - nmResp) |
| 4 | NUM_CPF | VARCHAR2(11) | Y |  | CPF do Contato Responsável pela Informação. (R2099 - cpfResp) |
| 5 | NUM_TEL | VARCHAR2(13) | Y |  | Telefone do Contato Responsvel pela Informação. (R2099 - telefone) |
| 6 | EMAIL | VARCHAR2(60) | Y |  | email do Contato Responsável pela Informação. (R2099 - email) |
| 7 | IND_EVT_SERV_TM | CHAR(1) | Y |  | (R2099 - evtServTm) |
| 8 | IND_EVT_SERV_PR | CHAR(1) | Y |  | (R2099 - evtServPr) |
| 9 | IND_EVT_ASS_DESP_REC | CHAR(1) | Y |  | (R2099 - evtAssDespRec) |
| 10 | IND_EVT_ASS_DESP_REP | CHAR(1) | Y |  | (R2099 - evtAssDespRep) |
| 11 | IND_EVT_COM_PROD | CHAR(1) | Y |  | (R2099 - evtComProd) |
| 12 | IND_EVT_CPRB | CHAR(1) | Y |  | (R-2099 - evtCPRB) |
| 13 | IND_EVT_PGTOS | CHAR(1) | Y |  | (R-2099 - evtPgtos) |
| 14 | COMP_SEM_MOVTO | VARCHAR2(7) | Y |  |  |
| 15 | IND_EVT_AQUIS | VARCHAR2(1) | Y |  | (R2099 - evtAquis) |

**PK**: ID_R2099_COMPL

**FKs**:
- ID_R2098_R2099_OC → REINF_PGER_R2098_R2099_OC(ID_R2098_R2099_OC)

**Indexes**:
- UK_REINF_PGER_R2099_COMPL_001 (UNIQUE): (ID_R2098_R2099_OC)

---

## REINF_PGER_R4010_ADV_PROC_JUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_ADV_PROC_JUD | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_PROC_JUD | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO_ADV | VARCHAR2(1) | Y |  |  |
| 4 | NR_INSCRICAO_ADV | VARCHAR2(14) | Y |  |  |
| 5 | VLR_ADV | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_ADV_PROC_JUD

**FKs**:
- ID_R4010_INFO_PROC_JUD → REINF_PGER_R4010_INFO_PROC_JUD(ID_R4010_INFO_PROC_JUD)

**Indexes**:
- UK_REINF_PGER_R4010_ADV_PRO_JD (UNIQUE): (ID_R4010_INFO_PROC_JUD, TP_INSCRICAO_ADV, NR_INSCRICAO_ADV)

---

## REINF_PGER_R4010_ADV_RRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_ADV_RRA | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_RRA | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO_ADV | VARCHAR2(1) | Y |  |  |
| 4 | NR_INSCRICAO_ADV | VARCHAR2(14) | Y |  |  |
| 5 | VLR_ADV | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_ADV_RRA

**FKs**:
- ID_R4010_INFO_RRA → REINF_PGER_R4010_INFO_RRA(ID_R4010_INFO_RRA)

**Indexes**:
- UK_REINF_PGER_R4010_ADV_RRA (UNIQUE): (ID_R4010_INFO_RRA, TP_INSCRICAO_ADV, NR_INSCRICAO_ADV)

---

## REINF_PGER_R4010_BENEF_PEN_DET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_BENEF_PEN_DET | NUMBER(12) | N |  |  |
| 2 | ID_R4010_DET_DED | NUMBER(12) | N |  |  |
| 3 | NUM_CPF_DEP | VARCHAR2(11) | Y |  |  |
| 4 | VLR_DEDUCAO_DEP | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_BENEF_PEN_DET

**FKs**:
- ID_R4010_DET_DED → REINF_PGER_R4010_DET_DED(ID_R4010_DET_DED)

**Indexes**:
- UK_REINF_PGER_R4010_BEN_PEN_DT (UNIQUE): (ID_R4010_DET_DED, NUM_CPF_DEP)

---

## REINF_PGER_R4010_BENE_PEN_SUSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_BENEF_PEN_SUSP | NUMBER(12) | N |  |  |
| 2 | ID_R4010_DED_SUSP | NUMBER(12) | N |  |  |
| 3 | NUM_CPF_DEP | VARCHAR2(11) | Y |  |  |
| 4 | VLR_DEP_SUSP | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_BENEF_PEN_SUSP

**FKs**:
- ID_R4010_DED_SUSP → REINF_PGER_R4010_DED_SUSP(ID_R4010_DED_SUSP)

**Indexes**:
- UK_REINF_PGER_R4010_BEN_PEN_SU (UNIQUE): (ID_R4010_DED_SUSP, NUM_CPF_DEP)

---

## REINF_PGER_R4010_DED_SUSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_DED_SUSP | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_PROC_RET | NUMBER(12) | N |  |  |
| 3 | IND_TP_DEDUCAO | NUMBER(2) | Y |  |  |
| 4 | VLR_DED_SUSP | NUMBER(17,2) | Y |  |  |
| 5 | IND_TP_BENEF_DED | NUMBER(1) | Y |  |  |

**PK**: ID_R4010_DED_SUSP

**FKs**:
- ID_R4010_INFO_PROC_RET → REINF_PGER_R4010_INFO_PROC_RET(ID_R4010_INFO_PROC_RET)

**Indexes**:
- UK_REINF_PGER_R4010_DED_SUSP (UNIQUE): (ID_R4010_INFO_PROC_RET, IND_TP_DEDUCAO, IND_TP_BENEF_DED)

---

## REINF_PGER_R4010_DET_DED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_DET_DED | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_PAGTO | NUMBER(12) | N |  |  |
| 3 | IND_TP_DEDUCAO | VARCHAR2(1) | Y |  |  |
| 4 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 5 | IND_INFO_ENTID | VARCHAR2(1) | Y |  |  |
| 6 | NUM_INSC_PREV_COMPL | VARCHAR2(14) | Y |  |  |
| 7 | VLR_FUNPRESP | NUMBER(17,2) | Y |  |  |
| 8 | IND_TP_BENEF_DED | NUMBER(1) | Y |  |  |

**PK**: ID_R4010_DET_DED

**FKs**:
- ID_R4010_INFO_PAGTO → REINF_PGER_R4010_INFO_PAGTO(ID_R4010_INFO_PAGTO)

**Indexes**:
- UK_REINF_PGER_R4010_DET_DED (UNIQUE): (ID_R4010_INFO_PAGTO, IND_TP_DEDUCAO, IND_INFO_ENTID, NUM_INSC_PREV_COMPL, IND_TP_BENEF_DED)

---

## REINF_PGER_R4010_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_ESTAB | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | VARCHAR2(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |

**PK**: ID_R4010_ESTAB

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R4010_ESTAB (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO, COD_ESTAB)

---

## REINF_PGER_R4010_IDENT_DEP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_IDENT_DEP | NUMBER(12) | N |  |  |
| 2 | ID_R4010_OC | NUMBER(12) | N |  |  |
| 3 | NUM_CPF_DEP | VARCHAR2(11) | Y |  |  |
| 4 | IND_REL_DEP | VARCHAR2(2) | Y |  |  |
| 5 | DSC_DEP | VARCHAR2(30) | Y |  |  |

**PK**: ID_R4010_IDENT_DEP

**FKs**:
- ID_R4010_OC → REINF_PGER_R4010_OC(ID_R4010_OC)

**Indexes**:
- UK_REINF_PGER_R4010_IDENT_DEP (UNIQUE): (ID_R4010_OC, NUM_CPF_DEP, IND_REL_DEP)

---

## REINF_PGER_R4010_IDENT_OPSAUDE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_IDENT_OPSAUDE | NUMBER(12) | N |  |  |
| 2 | ID_R4010_OC | NUMBER(12) | N |  |  |
| 3 | NUM_CNPJ | VARCHAR2(14) | Y |  |  |
| 4 | NUM_REG_ANS | VARCHAR2(6) | Y |  |  |
| 5 | VLR_SAUDE | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_IDENT_OPSAUDE

**FKs**:
- ID_R4010_OC → REINF_PGER_R4010_OC(ID_R4010_OC)

**Indexes**:
- UK_REINF_PGER_R4010_ID_OPSAUDE (UNIQUE): (ID_R4010_OC, NUM_CNPJ, NUM_REG_ANS)

---

## REINF_PGER_R4010_IDENT_PAGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_IDENT_PAGTO | NUMBER(12) | N |  |  |
| 2 | ID_R4010_OC | NUMBER(12) | N |  |  |
| 3 | COD_NAT_REND | VARCHAR2(5) | Y |  |  |
| 4 | OBSERVACAO | VARCHAR2(200) | Y |  |  |

**PK**: ID_R4010_IDENT_PAGTO

**FKs**:
- ID_R4010_OC → REINF_PGER_R4010_OC(ID_R4010_OC)

**Indexes**:
- UK_REINF_PGER_R4010_ID_PAGTO (UNIQUE): (ID_R4010_OC, COD_NAT_REND, OBSERVACAO)

---

## REINF_PGER_R4010_INFO_DEP_PL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_INFO_DEP_PL | NUMBER(12) | N |  |  |
| 2 | ID_R4010_IDENT_OPSAUDE | NUMBER(12) | N |  |  |
| 3 | NUM_CPF_DEP | VARCHAR2(11) | Y |  |  |
| 4 | VLR_SAUDE | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_INFO_DEP_PL

**FKs**:
- ID_R4010_IDENT_OPSAUDE → REINF_PGER_R4010_IDENT_OPSAUDE(ID_R4010_IDENT_OPSAUDE)

**Indexes**:
- UK_REINF_PGER_R4010_IN_DEP_PL (UNIQUE): (ID_R4010_IDENT_OPSAUDE, NUM_CPF_DEP)

---

## REINF_PGER_R4010_INFO_PAGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_INFO_PAGTO | NUMBER(12) | N |  |  |
| 2 | ID_R4010_IDENT_PAGTO | NUMBER(12) | N |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | DSC_COMP_FP | VARCHAR2(7) | Y |  |  |
| 5 | IND_DEC_TERC | VARCHAR2(1) | Y |  |  |
| 6 | VLR_REND_BRUTO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_REND_TRIB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 9 | IND_RRA | VARCHAR2(1) | Y |  |  |
| 10 | IND_FCI_SCP | VARCHAR2(1) | Y |  |  |
| 11 | NUM_INSCR_FCI_SCP | VARCHAR2(14) | Y |  |  |
| 12 | PERCENTUAL_SCP | NUMBER(5,1) | Y |  |  |
| 13 | IND_JUD | VARCHAR2(1) | Y |  |  |
| 14 | COD_PAIS_RESID_EXT | VARCHAR2(3) | Y |  |  |
| 15 | DATA_ESCR_CONT | DATE | Y |  |  |
| 16 | OBSERVACAO | VARCHAR2(200) | Y |  |  |

**PK**: ID_R4010_INFO_PAGTO

**FKs**:
- ID_R4010_IDENT_PAGTO → REINF_PGER_R4010_IDENT_PAGTO(ID_R4010_IDENT_PAGTO)

**Indexes**:
- UK_REINF_PGER_R4010_INFO_PAGTO (UNIQUE): (ID_R4010_IDENT_PAGTO, DATA_MOVTO, DSC_COMP_FP, IND_DEC_TERC, IND_RRA, IND_FCI_SCP, NUM_INSCR_FCI_SCP, PERCENTUAL_SCP, IND_JUD, COD_PAIS_RESID_EXT, DATA_ESCR_CONT, OBSERVACAO)

---

## REINF_PGER_R4010_INFO_PAGTO_EX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_INFO_PAGTO_EX | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_PAGTO | NUMBER(12) | N |  |  |
| 3 | IND_IDENT_FISCAL | NUMBER(1) | Y |  |  |
| 4 | NUM_IDENT_FISCAL | VARCHAR2(30) | Y |  |  |
| 5 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |
| 6 | DSC_LOGRADOURO | VARCHAR2(80) | Y |  |  |
| 7 | NUM_LOGRADOURO | VARCHAR2(10) | Y |  |  |
| 8 | DSC_COMPLEMENTO | VARCHAR2(30) | Y |  |  |
| 9 | BAIRRO | VARCHAR2(60) | Y |  |  |
| 10 | CIDADE | VARCHAR2(40) | Y |  |  |
| 11 | ESTADO | VARCHAR2(40) | Y |  |  |
| 12 | COD_POSTAL | VARCHAR2(12) | Y |  |  |
| 13 | TELEFONE | VARCHAR2(15) | Y |  |  |

**PK**: ID_R4010_INFO_PAGTO_EX

**FKs**:
- ID_R4010_INFO_PAGTO → REINF_PGER_R4010_INFO_PAGTO(ID_R4010_INFO_PAGTO)

**Indexes**:
- UK_REINF_PGER_R4010_IN_PAG_EX (UNIQUE): (ID_R4010_INFO_PAGTO, IND_IDENT_FISCAL, NUM_IDENT_FISCAL, TP_TRIBUTACAO_IR, DSC_LOGRADOURO, NUM_LOGRADOURO, DSC_COMPLEMENTO, BAIRRO, CIDADE, ESTADO, COD_POSTAL, TELEFONE)

---

## REINF_PGER_R4010_INFO_PROC_JUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_INFO_PROC_JUD | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_PAGTO | NUMBER(12) | N |  |  |
| 3 | NUM_PROC_JUD | VARCHAR2(21) | Y |  |  |
| 4 | IND_ORIG_REC | VARCHAR2(1) | Y |  |  |
| 5 | NUM_CNPJ_ORIG_REC | VARCHAR2(14) | Y |  |  |
| 6 | DSC_PROC_JUD | VARCHAR2(50) | Y |  |  |
| 7 | VLR_DESP_CUSTAS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DESP_ADV | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_INFO_PROC_JUD

**FKs**:
- ID_R4010_INFO_PAGTO → REINF_PGER_R4010_INFO_PAGTO(ID_R4010_INFO_PAGTO)

**Indexes**:
- UK_REINF_PGER_R4010_IN_PRO_JUD (UNIQUE): (ID_R4010_INFO_PAGTO)

---

## REINF_PGER_R4010_INFO_PROC_RET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_INFO_PROC_RET | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_PAGTO | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_RET | NUMBER(1) | Y |  |  |
| 4 | NUM_PROC_RET | VARCHAR2(21) | Y |  |  |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 6 | VLR_NAO_RETIDO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DEP_JUDICIAL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CMP_ANO_CAL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CMP_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_REND_SUSP | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_INFO_PROC_RET

**FKs**:
- ID_R4010_INFO_PAGTO → REINF_PGER_R4010_INFO_PAGTO(ID_R4010_INFO_PAGTO)

**Indexes**:
- UK_REINF_PGER_R4010_IN_PRO_RET (UNIQUE): (ID_R4010_INFO_PAGTO, IND_TP_PROC_RET, NUM_PROC_RET, COD_SUSP)

---

## REINF_PGER_R4010_INFO_REEMB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_INFO_REEMB | NUMBER(12) | N |  |  |
| 2 | ID_R4010_IDENT_OPSAUDE | NUMBER(12) | N |  |  |
| 3 | IND_TP_INSCRICAO | NUMBER(1) | Y |  |  |
| 4 | NUM_INSCRICAO | VARCHAR2(14) | Y |  |  |
| 5 | VLR_REEMBOLSO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_REEMB_ANT | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_INFO_REEMB

**FKs**:
- ID_R4010_IDENT_OPSAUDE → REINF_PGER_R4010_IDENT_OPSAUDE(ID_R4010_IDENT_OPSAUDE)

**Indexes**:
- UK_REINF_PGER_R4010_INFO_REEMB (UNIQUE): (ID_R4010_IDENT_OPSAUDE, IND_TP_INSCRICAO, NUM_INSCRICAO)

---

## REINF_PGER_R4010_INFO_REEMB_PL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_INFO_REEMB_PL | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_DEP_PL | NUMBER(12) | N |  |  |
| 3 | IND_TP_INSCRICAO | VARCHAR2(1) | Y |  |  |
| 4 | NUM_INSCRICAO | VARCHAR2(14) | Y |  |  |
| 5 | VLR_REEMBOLSO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_REEMB_ANT | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_INFO_REEMB_PL

**FKs**:
- ID_R4010_INFO_DEP_PL → REINF_PGER_R4010_INFO_DEP_PL(ID_R4010_INFO_DEP_PL)

**Indexes**:
- UK_REINF_PGER_R4010_IN_REE_PL (UNIQUE): (ID_R4010_INFO_DEP_PL, IND_TP_INSCRICAO, NUM_INSCRICAO)

---

## REINF_PGER_R4010_INFO_RRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_INFO_RRA | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_PAGTO | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_RRA | VARCHAR2(1) | Y |  |  |
| 4 | NUM_PROC_RRA | VARCHAR2(21) | Y |  |  |
| 5 | IND_ORIG_REC | VARCHAR2(1) | Y |  |  |
| 6 | DSC_RRA | VARCHAR2(50) | Y |  |  |
| 7 | QTD_MESES_RRA | NUMBER(5,1) | Y |  |  |
| 8 | NUM_CNPJ_ORIG_REC | VARCHAR2(14) | Y |  |  |
| 9 | VLR_DESP_CUSTAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DESP_ADV | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4010_INFO_RRA

**FKs**:
- ID_R4010_INFO_PAGTO → REINF_PGER_R4010_INFO_PAGTO(ID_R4010_INFO_PAGTO)

**Indexes**:
- UK_REINF_PGER_R4010_INFO_RRA (UNIQUE): (ID_R4010_INFO_PAGTO)

---

## REINF_PGER_R4010_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_OC | NUMBER(12) | N |  |  |
| 2 | ID_R4010_ESTAB | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | VARCHAR2(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | VARCHAR2(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | VARCHAR2(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | VARCHAR2(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |
| 15 | NUM_CPF_BENEF | VARCHAR2(14) | Y |  |  |
| 16 | GRUPO_CPF_BENEF | VARCHAR2(9) | Y |  |  |
| 17 | IND_CPF_BENEF | VARCHAR2(1) | Y |  |  |
| 18 | COD_CPF_BENEF | VARCHAR2(14) | Y |  |  |
| 19 | NOM_BENEF | VARCHAR2(70) | Y |  |  |
| 20 | IDENT_EVENTO_ADICIONAL | VARCHAR2(8) | Y |  |  |
| 21 | NUM_CPF_BENEF_V | VARCHAR2(14) | Y | NVL("NUM_CPF_BENEF",' ') |  |

**PK**: ID_R4010_OC

**FKs**:
- ID_R4010_ESTAB → REINF_PGER_R4010_ESTAB(ID_R4010_ESTAB)

**Indexes**:
- IX_REINF_PGER_R4010_OC_1: (ID_EVENTO, IND_TP_AMB, IND_STATUS)
- IX_REINF_PGER_R4010_OC_2: (NUM_CPF_BENEF_V, ID_R4010_ESTAB)
- IX_REINF_PGER_R4010_OC_3: (ID_R4010_ESTAB, NUM_CPF_BENEF_V, SYS_NC00022$, SYS_NC00023$, SYS_NC00024$, SYS_NC00025$)
- UK_REINF_PGER_R4010_OC (UNIQUE): (ID_R4010_ESTAB, NUM_CPF_BENEF, GRUPO_CPF_BENEF, IND_CPF_BENEF, COD_CPF_BENEF, DAT_OCORRENCIA, IDENT_EVENTO_ADICIONAL)

---

## REINF_PGER_R4010_REND_ISENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4010_REND_ISENTO | NUMBER(12) | N |  |  |
| 2 | ID_R4010_INFO_PAGTO | NUMBER(12) | N |  |  |
| 3 | IND_TP_ISENCAO | NUMBER(2) | Y |  |  |
| 4 | VLR_ISENCAO | NUMBER(17,2) | Y |  |  |
| 5 | DSC_RENDIMENTO | VARCHAR2(100) | Y |  |  |
| 6 | DATA_LAUDO | DATE | Y |  |  |

**PK**: ID_R4010_REND_ISENTO

**FKs**:
- ID_R4010_INFO_PAGTO → REINF_PGER_R4010_INFO_PAGTO(ID_R4010_INFO_PAGTO)

**Indexes**:
- UK_REINF_PGER_R4010_REND_ISENT (UNIQUE): (ID_R4010_INFO_PAGTO, IND_TP_ISENCAO, DATA_LAUDO)

---

## REINF_PGER_R4020_ADV_PROC_JUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_ADV_PROC_JUD | NUMBER(12) | N |  |  |
| 2 | ID_R4020_DESP_PROC_JUD | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO_ADV | VARCHAR2(1) | Y |  |  |
| 4 | NR_INSCRICAO_ADV | VARCHAR2(14) | Y |  |  |
| 5 | VLR_ADV | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4020_ADV_PROC_JUD

**FKs**:
- ID_R4020_DESP_PROC_JUD → REINF_PGER_R4020_DESP_PROC_JUD(ID_R4020_DESP_PROC_JUD)

**Indexes**:
- UK_REINF_PGER_R4020_ADV_PRO_JU (UNIQUE): (ID_R4020_DESP_PROC_JUD, TP_INSCRICAO_ADV, NR_INSCRICAO_ADV)

---

## REINF_PGER_R4020_DESP_PROC_JUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_DESP_PROC_JUD | NUMBER(12) | N |  |  |
| 2 | ID_R4020_INFO_PROC_JUD | NUMBER(12) | N |  |  |
| 3 | VLR_DESP_CUSTAS | NUMBER(17,2) | Y |  |  |
| 4 | VLR_DESP_ADV | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4020_DESP_PROC_JUD

**FKs**:
- ID_R4020_INFO_PROC_JUD → REINF_PGER_R4020_INFO_PROC_JUD(ID_R4020_INFO_PROC_JUD)

**Indexes**:
- UK_REINF_PGER_R4020_DE_PRO_JUD (UNIQUE): (ID_R4020_INFO_PROC_JUD, VLR_DESP_CUSTAS, VLR_DESP_ADV)

---

## REINF_PGER_R4020_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_ESTAB | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | VARCHAR2(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |

**PK**: ID_R4020_ESTAB

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R4020_ESTAB (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO, COD_ESTAB)

---

## REINF_PGER_R4020_IDENT_PGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_IDENT_PGTO | NUMBER(12) | N |  |  |
| 2 | ID_R4020_OC | NUMBER(12) | N |  |  |
| 3 | COD_NAT_REND | VARCHAR2(5) | Y |  |  |
| 4 | OBSERVACAO | VARCHAR2(200) | Y |  |  |

**PK**: ID_R4020_IDENT_PGTO

**FKs**:
- ID_R4020_OC → REINF_PGER_R4020_OC(ID_R4020_OC)

**Indexes**:
- UK_REINF_PGER_R4020_IDENT_PGTO (UNIQUE): (ID_R4020_OC, COD_NAT_REND)

---

## REINF_PGER_R4020_INFO_PGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_INFO_PGTO | NUMBER(12) | N |  |  |
| 2 | ID_R4020_IDENT_PGTO | NUMBER(12) | N |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 5 | IND_FCI_SCP | VARCHAR2(1) | Y |  |  |
| 6 | NUM_INSCR_FCI_SCP | VARCHAR2(14) | Y |  |  |
| 7 | PERCENTUAL_SCP | NUMBER(5,1) | Y |  |  |
| 8 | IND_JUD | VARCHAR2(1) | Y |  |  |
| 9 | COD_PAIS_RESID_EXT | VARCHAR2(3) | Y |  |  |
| 10 | DATA_ESCR_CONT | DATE | Y |  |  |
| 11 | OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 12 | IND_REGRA_AGREGADO | VARCHAR2(1) | Y |  |  |

**PK**: ID_R4020_INFO_PGTO

**FKs**:
- ID_R4020_IDENT_PGTO → REINF_PGER_R4020_IDENT_PGTO(ID_R4020_IDENT_PGTO)

**Indexes**:
- UK_REINF_PGER_R4020_INFO_PGTO (UNIQUE): (ID_R4020_IDENT_PGTO, DATA_MOVTO, VLR_BRUTO, IND_FCI_SCP, NUM_INSCR_FCI_SCP, PERCENTUAL_SCP, IND_JUD, COD_PAIS_RESID_EXT, DATA_ESCR_CONT, OBSERVACAO, IND_REGRA_AGREGADO)

---

## REINF_PGER_R4020_INFO_PGTO_EXT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_INFO_PGTO_EXT | NUMBER(12) | N |  |  |
| 2 | ID_R4020_INFO_PGTO | NUMBER(12) | N |  |  |
| 3 | IND_IDENT_FISCAL | NUMBER(1) | Y |  |  |
| 4 | NUM_IDENT_FISCAL | VARCHAR2(30) | Y |  |  |
| 5 | COD_REL_FONTE_PAG | VARCHAR2(3) | Y |  |  |
| 6 | COD_FORMA_TRIB | VARCHAR2(2) | Y |  |  |
| 7 | DSC_LOGRADOURO | VARCHAR2(80) | Y |  |  |
| 8 | NUM_LOGRADOURO | VARCHAR2(10) | Y |  |  |
| 9 | DSC_COMPLEMENTO | VARCHAR2(30) | Y |  |  |
| 10 | BAIRRO | VARCHAR2(60) | Y |  |  |
| 11 | CIDADE | VARCHAR2(40) | Y |  |  |
| 12 | ESTADO | VARCHAR2(40) | Y |  |  |
| 13 | COD_POSTAL | VARCHAR2(12) | Y |  |  |
| 14 | TELEFONE | VARCHAR2(15) | Y |  |  |

**PK**: ID_R4020_INFO_PGTO_EXT

**FKs**:
- ID_R4020_INFO_PGTO → REINF_PGER_R4020_INFO_PGTO(ID_R4020_INFO_PGTO)

**Indexes**:
- UK_REINF_PGER_R4020_IN_PGT_EXT (UNIQUE): (ID_R4020_INFO_PGTO, IND_IDENT_FISCAL, NUM_IDENT_FISCAL, COD_REL_FONTE_PAG, COD_FORMA_TRIB, DSC_LOGRADOURO, NUM_LOGRADOURO, DSC_COMPLEMENTO, BAIRRO, CIDADE, ESTADO, COD_POSTAL, TELEFONE)

---

## REINF_PGER_R4020_INFO_PROC_JUD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_INFO_PROC_JUD | NUMBER(12) | N |  |  |
| 2 | ID_R4020_INFO_PGTO | NUMBER(12) | N |  |  |
| 3 | NUM_PROC_JUD | VARCHAR2(21) | Y |  |  |
| 4 | IND_ORIG_REC | VARCHAR2(1) | Y |  |  |
| 5 | NUM_CNPJ_ORIG_REC | VARCHAR2(14) | Y |  |  |
| 6 | DSC_PROC_JUD | VARCHAR2(50) | Y |  |  |

**PK**: ID_R4020_INFO_PROC_JUD

**FKs**:
- ID_R4020_INFO_PGTO → REINF_PGER_R4020_INFO_PGTO(ID_R4020_INFO_PGTO)

**Indexes**:
- UK_REINF_PGER_R4020_IN_PRO_JUD (UNIQUE): (ID_R4020_INFO_PGTO, NUM_PROC_JUD, IND_ORIG_REC)

---

## REINF_PGER_R4020_INFO_PROC_RET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_INFO_PROC_RET | NUMBER(12) | N |  |  |
| 2 | ID_R4020_INFO_PGTO | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_RET | NUMBER(1) | Y |  |  |
| 4 | NUM_PROC_RET | VARCHAR2(21) | Y |  |  |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 6 | VLR_BASE_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_N_IR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEP_IR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_SUSP_CSLL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_N_CSLL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DEP_CSLL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_SUSP_COFINS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_N_COFINS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DEP_COFINS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_SUSP_PP | NUMBER(17,2) | Y |  |  |
| 16 | VLR_N_PP | NUMBER(17,2) | Y |  |  |
| 17 | VLR_DEP_PP | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4020_INFO_PROC_RET

**FKs**:
- ID_R4020_INFO_PGTO → REINF_PGER_R4020_INFO_PGTO(ID_R4020_INFO_PGTO)

**Indexes**:
- UK_REINF_PGER_R4020_IN_PRO_RET (UNIQUE): (ID_R4020_INFO_PGTO, IND_TP_PROC_RET, NUM_PROC_RET, COD_SUSP)

---

## REINF_PGER_R4020_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_OC | NUMBER(12) | N |  |  |
| 2 | ID_R4020_ESTAB | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | VARCHAR2(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | VARCHAR2(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | VARCHAR2(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | VARCHAR2(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |
| 15 | NUM_CNPJ_BENEF | VARCHAR2(14) | Y |  |  |
| 16 | GRUPO_CNPJ_BENEF | VARCHAR2(9) | Y |  |  |
| 17 | IND_CNPJ_BENEF | VARCHAR2(1) | Y |  |  |
| 18 | COD_CNPJ_BENEF | VARCHAR2(14) | Y |  |  |
| 19 | NOM_BENEF | VARCHAR2(70) | Y |  |  |
| 20 | IND_ISEN_IMUN_BENEF | VARCHAR2(1) | Y |  |  |
| 21 | IDENT_EVENTO_ADICIONAL | VARCHAR2(8) | Y |  |  |

**PK**: ID_R4020_OC

**FKs**:
- ID_R4020_ESTAB → REINF_PGER_R4020_ESTAB(ID_R4020_ESTAB)

**Indexes**:
- IX_REINF_PGER_R4020_OC_1: (ID_EVENTO, IND_TP_AMB, IND_STATUS)
- UK_REINF_PGER_R4020_OC (UNIQUE): (ID_R4020_ESTAB, DAT_OCORRENCIA, NUM_CNPJ_BENEF, GRUPO_CNPJ_BENEF, IND_CNPJ_BENEF, COD_CNPJ_BENEF, IDENT_EVENTO_ADICIONAL)

---

## REINF_PGER_R4020_RETENCOES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4020_RETENCOES | NUMBER(12) | N |  |  |
| 2 | ID_R4020_INFO_PGTO | NUMBER(12) | N |  |  |
| 3 | VLR_BASE_IR | NUMBER(17,2) | Y |  |  |
| 4 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 5 | VLR_BASE_AGREG | NUMBER(17,2) | Y |  |  |
| 6 | VLR_AGREG | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_PP | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PP | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4020_RETENCOES

**FKs**:
- ID_R4020_INFO_PGTO → REINF_PGER_R4020_INFO_PGTO(ID_R4020_INFO_PGTO)

**Indexes**:
- UK_REINF_PGER_R4020_RETENCOES (UNIQUE): (ID_R4020_INFO_PGTO)

---

## REINF_PGER_R4040_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4040_ESTAB | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  |  |
| 5 | IDENT_EVENTO_ADICIONAL | VARCHAR2(8) | Y |  |  |

**PK**: ID_R4040_ESTAB

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R4040_ESTAB (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO, IDENT_EVENTO_ADICIONAL)

---

## REINF_PGER_R4040_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4040_NAT | NUMBER(12) | N |  |  |
| 2 | ID_R4040_OC | NUMBER(12) | N |  |  |
| 3 | COD_NAT_REND | VARCHAR2(5) | N |  |  |

**PK**: ID_R4040_NAT

**FKs**:
- ID_R4040_OC → REINF_PGER_R4040_OC(ID_R4040_OC)

**Indexes**:
- UK_REINF_PGER_R4040_NAT_001 (UNIQUE): (ID_R4040_OC, COD_NAT_REND)

---

## REINF_PGER_R4040_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4040_OC | NUMBER(12) | N |  |  |
| 2 | ID_R4040_ESTAB | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | PROC_ID | NUMBER(12) | Y |  |  |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 7 | IND_OPER | CHAR(1) | Y |  |  |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 9 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |

**PK**: ID_R4040_OC

**FKs**:
- ID_R4040_ESTAB → REINF_PGER_R4040_ESTAB(ID_R4040_ESTAB)

**Indexes**:
- UK_REINF_PGER_R4040_OC_001 (UNIQUE): (ID_R4040_ESTAB, DAT_OCORRENCIA)

---

## REINF_PGER_R4040_PGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4040_PGTO | NUMBER(12) | N |  |  |
| 2 | ID_R4040_NAT | NUMBER(12) | N |  |  |
| 3 | DAT_MOV | DATE | N |  |  |
| 4 | VLR_LIQ | NUMBER(17,2) | Y |  |  |
| 5 | VLR_REAJ | NUMBER(17,2) | Y |  |  |
| 6 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 7 | DESCR | VARCHAR2(200) | Y |  |  |
| 8 | DATA_ESCR_CONT | DATE | Y |  |  |

**PK**: ID_R4040_PGTO

**FKs**:
- ID_R4040_NAT → REINF_PGER_R4040_NAT(ID_R4040_NAT)

**Indexes**:
- UK_REINF_PGER_R4040_PGTO_001 (UNIQUE): (ID_R4040_NAT, DAT_MOV)

---

## REINF_PGER_R4040_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4040_PROC | NUMBER(12) | N |  |  |
| 2 | ID_R4040_PGTO | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 6 | VLR_BASE_EXIG_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RET_NEFE_IR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEP_JUD_IR | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4040_PROC

**FKs**:
- ID_R4040_PGTO → REINF_PGER_R4040_PGTO(ID_R4040_PGTO)

**Indexes**:
- UK_REINF_PGER_R4040_PROC_001 (UNIQUE): (ID_R4040_PGTO, IND_TP_PROC_ADJ, NUM_PROC_ADJ)

---

## REINF_PGER_R4080_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4080_ESTAB | NUMBER(12) | N |  |  |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  |  |
| 3 | TP_INSCRICAO | CHAR(1) | N |  |  |
| 4 | NR_INSCRICAO | VARCHAR2(14) | N |  |  |

**PK**: ID_R4080_ESTAB

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R4080_ESTAB (UNIQUE): (ID_PGER_APUR, TP_INSCRICAO, NR_INSCRICAO)

---

## REINF_PGER_R4080_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4080_NAT | NUMBER(12) | N |  |  |
| 2 | ID_R4080_OC | NUMBER(12) | N |  |  |
| 3 | COD_NAT_REND | VARCHAR2(5) | N |  |  |
| 4 | OBSERVACAO | VARCHAR2(200) | Y |  |  |

**PK**: ID_R4080_NAT

**FKs**:
- ID_R4080_OC → REINF_PGER_R4080_OC(ID_R4080_OC)

**Indexes**:
- UK_REINF_PGER_R4080_NAT_001 (UNIQUE): (ID_R4080_OC, COD_NAT_REND, OBSERVACAO)

---

## REINF_PGER_R4080_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4080_OC | NUMBER(12) | N |  |  |
| 2 | ID_R4080_ESTAB | NUMBER(12) | N |  |  |
| 3 | DAT_OCORRENCIA | DATE | N |  |  |
| 4 | NR_INSCRICAO_FONT | VARCHAR2(14) | N |  |  |
| 5 | IND_STATUS | CHAR(1) | Y |  |  |
| 6 | PROC_ID | NUMBER(12) | Y |  |  |
| 7 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 8 | IND_OPER | CHAR(1) | Y |  |  |
| 9 | NUM_RECIBO | VARCHAR2(52) | Y |  |  |
| 10 | IND_TP_AMB | CHAR(1) | Y |  |  |
| 11 | IND_PROC_EMISSAO | CHAR(1) | Y |  |  |
| 12 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  |  |
| 13 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |
| 14 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  |  |
| 15 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  |  |

**PK**: ID_R4080_OC

**FKs**:
- ID_R4080_ESTAB → REINF_PGER_R4080_ESTAB(ID_R4080_ESTAB)

**Indexes**:
- UK_REINF_PGER_R4080_OC_001 (UNIQUE): (ID_R4080_ESTAB, NR_INSCRICAO_FONT, DAT_OCORRENCIA)

---

## REINF_PGER_R4080_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4080_PROC | NUMBER(12) | N |  |  |
| 2 | ID_R4080_REC | NUMBER(12) | N |  |  |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | N |  |  |
| 5 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 6 | VLR_BASE_EXIG_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RET_NEFE_IR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEP_JUD_IR | NUMBER(17,2) | Y |  |  |

**PK**: ID_R4080_PROC

**FKs**:
- ID_R4080_REC → REINF_PGER_R4080_REC(ID_R4080_REC)

**Indexes**:
- UK_REINF_PGER_R4080_PROC_001 (UNIQUE): (ID_R4080_REC, IND_TP_PROC_ADJ, NUM_PROC_ADJ)

---

## REINF_PGER_R4080_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4080_REC | NUMBER(12) | N |  |  |
| 2 | ID_R4080_NAT | NUMBER(12) | N |  |  |
| 3 | DAT_RECEBIMENTO | DATE | N |  |  |
| 4 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 5 | VLR_BASE_IR | NUMBER(17,2) | Y |  |  |
| 6 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 7 | OBSERVACAO | VARCHAR2(200) | Y |  |  |

**PK**: ID_R4080_REC

**FKs**:
- ID_R4080_NAT → REINF_PGER_R4080_NAT(ID_R4080_NAT)

**Indexes**:
- UK_REINF_PGER_R4080_REC_001 (UNIQUE): (ID_R4080_NAT, DAT_RECEBIMENTO)

---

## REINF_PGER_R4099_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4099_COMPL | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R4099_COMPL |
| 2 | ID_R4099_OC | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | NOME_CONTATO | VARCHAR2(70) | Y |  | Nome do Contato Responsvel pela Informaão. (R4099 - nmResp) |
| 4 | NUM_CPF | VARCHAR2(11) | Y |  | CPF do Contato Responsável pela Informação. (R4099 - cpfResp) |
| 5 | NUM_TEL | VARCHAR2(13) | Y |  | Telefone do Contato Responsvel pela Informação. (R4099 - telefone) |
| 6 | EMAIL | VARCHAR2(60) | Y |  | email do Contato Responsável pela Informação. (R4099 - email) |

**PK**: ID_R4099_COMPL

**FKs**:
- ID_R4099_OC → REINF_PGER_R4099_OC(ID_R4099_OC)

**Indexes**:
- UK_REINF_PGER_R4099_COMPL_001 (UNIQUE): (ID_R4099_OC)

---

## REINF_PGER_R4099_OC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R4099_OC | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R4099_OC |
| 2 | ID_PGER_APUR | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | DAT_OCORRENCIA | DATE | N |  | Data de Ocorrencia |
| 4 | IND_STATUS | VARCHAR2(1) | Y |  | Status de Controle das Ocorrências.  Dominio REINF_STATUS_PGER_V |
| 5 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificação única do evento (R4099 - evtFech - id). |
| 7 | IND_OPER | VARCHAR2(1) | Y |  | Nao se aplica ao evento R-4099. |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  | Nao se aplica ao evento R-4099. |
| 9 | IND_TP_AMB | VARCHAR2(1) | Y |  | Identificacao do ambiente (R4099 - ideEvento - tpAmb). Dominio 1 - Producao 2 - Producao restrita.  |
| 10 | IND_PROC_EMISSAO | VARCHAR2(1) | Y |  | Processo de Emissao do Evento (R4099 - ideEvento - procEmi). Dominio 1 - Aplicativo do contribuinte; 2 - Aplicativo governamental. |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  | Versao do Processo de Emissao do Evento. (R4099 - ideEvento - verProc). Informar a versao do aplicativo emissor do evento. |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V. "v02_01_01". |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  | Status Apresentado no Painel de Eventos, campo Situacao. Dominio REINF_STATUS_PAINEL_V. |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_OUT. |
| 15 | IND_FECH_RET | VARCHAR2(1) | Y |  | Dominio: 0 - Fechamento, 1 - Reabertura |

**PK**: ID_R4099_OC

**FKs**:
- ID_PGER_APUR → REINF_PGER_APUR(ID_PGER_APUR)

**Indexes**:
- UK_REINF_PGER_R4099_OC_001 (UNIQUE): (ID_PGER_APUR, DAT_OCORRENCIA)

---

## REINF_PGER_R9000_EVT
**Comment**: Tabela de Exclusao de Eventos - R9000

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R9000_EVT | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R9000_EVT |
| 2 | ID_PGER_ESTAB | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | ID_OC_EXCL | NUMBER(12) | N |  | Identificador da Ocorrencia do evento que esta sendo excluido. |
| 4 | TIPO_EVENTO_EXCL | VARCHAR2(50) | N |  | Tipo do evento que esta sendo excluido (R-2010 a R-2070 e R-3010).  (R-9000 - infoExclusao - tpEvento) |

**PK**: ID_R9000_EVT

**FKs**:
- ID_PGER_ESTAB → REINF_PGER_ESTAB(ID_PGER_ESTAB)

**Indexes**:
- UK_REINF_PGER_R9000_EVT_001 (UNIQUE): (ID_PGER_ESTAB, TIPO_EVENTO_EXCL, ID_OC_EXCL)

---

## REINF_PGER_R9000_OC
**Comment**: Tabela de Ocorrencias do registro R9000.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_R9000_OC | NUMBER(12) | N |  | Identificador Unico - Sequence SEQ_REINF_PGER_R9000_OC |
| 2 | ID_PGER_EVT | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | DAT_OCORRENCIA | DATE | N |  | Data de Ocorrencia |
| 4 | IND_STATUS | CHAR(1) | Y |  | Status de Controle das Ocorrências.  Dominio REINF_STATUS_PGER_V |
| 5 | PROC_ID | NUMBER(12) | Y |  | Numero do Processo da Pre-Geracao gravado na LIB_PROCESSO. |
| 6 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificaão nica do evento (R2098 - evtReabreEvPer- id, R2099 - evtFechaEvPer- id). |
| 7 | IND_OPER | CHAR(1) | Y |  | Nao se aplica ao evento R-9000. |
| 8 | NUM_RECIBO | VARCHAR2(52) | Y |  | Nao se aplica ao evento R-9000. |
| 9 | IND_TP_AMB | CHAR(1) | Y |  | Identificacao do ambiente (R9000 - ideEvento - tpAmb). Dominio 1 - Producao 2 - Producao restrita - dados reais; 3 - Producao restrita - dados ficticios. |
| 10 | IND_PROC_EMISSAO | CHAR(1) | Y |  | Processo de Emissao do Evento (R9000 - ideEvento - procEmi). Dominio 1 - Aplicativo do contribuinte; 2 - Aplicativo governamental. |
| 11 | COD_VERSAO_PROC | VARCHAR2(20) | Y |  | Versao do Processo de Emissao do Evento. (R9000 - ideEvento - verProc). Informar a versao do aplicativo emissor do evento. |
| 12 | COD_VERSAO_LAYOUT | VARCHAR2(10) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V. "v01_00_00". |
| 13 | COD_STATUS_PAINEL | VARCHAR2(2) | Y |  | Status Apresentado no Painel de Eventos, campo Situacao. Dominio REINF_STATUS_PAINEL_V. |
| 14 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | Y |  | Identificador da tabela STG_EVENTOS_REINF_OUT. |
| 15 | NUM_RECIBO_EXCL | VARCHAR2(52) | Y |  | Numero do recibo do evento que esta sendo excluido. (R-9000 - infoExclusao - nrRecEvt) |
| 16 | DAT_APUR | DATE | Y |  | Período de referencia do evento que esta sendo excluido. (R-9000 - infoExclusao - perApur) |

**PK**: ID_R9000_OC

**FKs**:
- ID_PGER_EVT → REINF_PGER_R9000_EVT(ID_R9000_EVT)

**Indexes**:
- UK_REINF_PGER_R9000_OC_001 (UNIQUE): (ID_PGER_EVT, DAT_OCORRENCIA)

---

## REINF_XML_IMP_R4000

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ID_EVENTO | VARCHAR2(36) | N |  |  |
| 4 | DAT_APUR | DATE | Y |  |  |
| 5 | IND_TP_AMB | VARCHAR2(1) | Y |  |  |
| 6 | TPO_EVENTO | VARCHAR2(50) | Y |  |  |
| 7 | TPO_INSC_CONTRIB | VARCHAR2(1) | Y |  |  |
| 8 | NUM_INSC_CONTRIB | VARCHAR2(14) | Y |  |  |
| 9 | TPO_INSC_ESTAB | VARCHAR2(1) | Y |  |  |
| 10 | NUM_INSC_ESTAB | VARCHAR2(14) | Y |  |  |
| 11 | NUM_CNPJ_BENEF | VARCHAR2(14) | Y |  |  |
| 12 | DSC_NOME_BENEF | VARCHAR2(70) | Y |  |  |
| 13 | COD_VERSAO | VARCHAR2(10) | Y |  |  |
| 14 | DSC_EVENTO_ADIC | VARCHAR2(8) | Y |  |  |
| 15 | COD_ESTAB_DESCENTR | VARCHAR2(6) | Y |  |  |
| 16 | DSC_ARQ_IMPORTACAO | VARCHAR2(255) | Y |  |  |
| 17 | XML | XMLTYPE | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ID_EVENTO

**Indexes**:
- IX_REINF_XML_IMP_R4000_1: (COD_EMPRESA, COD_ESTAB, DAT_APUR, IND_TP_AMB, COD_VERSAO, TPO_EVENTO, NUM_CNPJ_BENEF, ID_EVENTO)

---

