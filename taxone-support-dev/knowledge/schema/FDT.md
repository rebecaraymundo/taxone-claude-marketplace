# Módulo: FDT (FDT) - 46 tabelas

## FDT_ALIQ_MED_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | VLR_ALIQ_MED_IPI | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## FDT_APF_AGRUP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_AGRUP_CONTA | VARCHAR2(10) | N |  |  |
| 4 | DSC_AGRUP_CONTA | VARCHAR2(60) | N |  |  |
| 5 | IND_CALC_OPER | CHAR(1) | Y | 'N' |  |
| 6 | IND_CALC_FINAN | CHAR(1) | Y | 'N' |  |
| 7 | TIPO_AGRUPAMENTO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_AGRUP_CONTA

---

## FDT_APF_AGRUP_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VLR_ALIQ_PIS | NUMBER(7,4) | N |  |  |
| 4 | VLR_ALIQ_COFINS | NUMBER(7,4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## FDT_APF_AGRUP_CONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | COD_AGRUP_CONTA | VARCHAR2(10) | N |  |  |
| 6 | IDENT_CONTA | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_AGRUP_CONTA → FDT_APF_AGRUP(COD_EMPRESA, COD_ESTAB, COD_AGRUP_CONTA)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_FDT_APF_AGRUP_CTA: (IDENT_CONTA)

---

## FDT_APF_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | MES_ANO_APUR | VARCHAR2(6) | N |  |  |
| 6 | COD_AGRUP_CONTA | VARCHAR2(10) | N |  |  |
| 7 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 8 | VLR_SALDO | NUMBER(17,2) | Y |  |  |
| 9 | IND_SALDO | CHAR(1) | Y |  |  |
| 10 | VLR_SALDO_AJUSTE | NUMBER(17,2) | Y |  |  |
| 11 | IND_SALDO_AJUSTE | CHAR(1) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_CONTA, COD_CONTA, MES_ANO_APUR

---

## FDT_ATO_CONCES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_AG_ATO_CONCES | VARCHAR2(4) | N |  |  |
| 4 | ANO_ATO_CONCES | VARCHAR2(4) | N |  |  |
| 5 | NUM_ATO_CONCES | VARCHAR2(6) | N |  |  |
| 6 | DIG_ATO_CONCES | CHAR(1) | N |  |  |
| 7 | COD_AG_CENTRAL | VARCHAR2(4) | Y |  |  |
| 8 | IND_MODAL_DRBK | CHAR(1) | Y |  |  |
| 9 | DSC_NOMEC_DRBK | VARCHAR2(50) | Y |  |  |
| 10 | IND_OPERAC_DRBK | CHAR(1) | Y |  |  |
| 11 | IND_TP_EMPRESA | CHAR(1) | Y |  |  |
| 12 | IND_OPERAC_INDUST | CHAR(1) | Y |  |  |
| 13 | DAT_PEDIDO | DATE | Y |  |  |
| 14 | DAT_INI_VIGENCIA | DATE | Y |  |  |
| 15 | DAT_FIM_VIGENCIA | DATE | Y |  |  |
| 16 | SITUACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_CAD_EMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_CEXP_PEXP | CHAR(1) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_CEXP_PEXP, IDENT_FIS_JUR

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_FK_SAF_0498: (IDENT_FIS_JUR)

---

## FDT_CFO_DRBK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CFO | NUMBER(12) | N |  |  |
| 2 | IND_E_S | CHAR(1) | Y |  |  |

**PK**: IDENT_CFO

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## FDT_COMPOS_NCM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_NBM | NUMBER(12) | N |  |  |
| 3 | IDENT_NBM_INSUMO | NUMBER(12) | N |  |  |
| 4 | COD_MEDIDA_COMPOS | VARCHAR2(8) | Y |  |  |
| 5 | QTD_INSUMOS | NUMBER(14,4) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_NBM, IDENT_NBM_INSUMO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_NBM_INSUMO → X2043_COD_NBM(IDENT_NBM)

---

## FDT_CONTROLE_DRBK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_AG_ATO_CONCES | VARCHAR2(4) | N |  |  |
| 4 | ANO_ATO_CONCES | VARCHAR2(4) | N |  |  |
| 5 | NUM_ATO_CONCES | VARCHAR2(6) | N |  |  |
| 6 | DIG_ATO_CONCES | CHAR(1) | N |  |  |
| 7 | IND_PROD_INSUMO | CHAR(1) | N |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 9 | ANO_MES_CONTROLE | VARCHAR2(6) | Y |  |  |
| 10 | QTD_INFORMADA | NUMBER(17,6) | Y |  |  |
| 11 | QTD_REALIZADA | NUMBER(17,6) | Y |  |  |
| 12 | COD_MEDIDA_CONTR | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES, IND_PROD_INSUMO, IDENT_PRODUTO

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES → FDT_ATO_CONCES(COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES)

---

## FDT_CPRES_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPR_CENTRAL | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPR_CENTRAL, COD_ESTAB_CENTRAL, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPR_CENTRAL, COD_ESTAB_CENTRAL → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_CPRES_PR_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_CUSTO_INTEGR | CHAR(1) | Y |  |  |
| 4 | COD_RESP_LEGAL | VARCHAR2(2) | Y |  |  |
| 5 | COD_RESP_PREENC | VARCHAR2(2) | Y |  |  |
| 6 | IND_CLASSE_ESTAB | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_DIRF_PROC_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROC | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | ANO_BASE | NUMBER(4) | Y |  |  |
| 4 | DAT_GERACAO | DATE | Y |  |  |
| 5 | IND_FORMA_APRES | VARCHAR2(2) | Y |  |  |
| 6 | TAM_MIDIA | NUMBER(6) | Y |  |  |
| 7 | DSC_DENSIDADE | VARCHAR2(10) | Y |  |  |
| 8 | COD_SOFT_SO | VARCHAR2(3) | Y |  |  |
| 9 | COD_EQUIP | VARCHAR2(3) | Y |  |  |
| 10 | COD_RESP_LEGAL | VARCHAR2(2) | Y |  |  |
| 11 | COD_RESP_TECNICO | VARCHAR2(2) | Y |  |  |
| 12 | NUM_VOLUMES | NUMBER(6) | Y |  |  |
| 13 | QTD_REG_TP_1 | NUMBER(6) | Y |  |  |
| 14 | QTD_REG_TP_1_S | NUMBER(6) | Y |  |  |
| 15 | QTD_REG_TP_1_E | NUMBER(6) | Y |  |  |
| 16 | QTD_REG_TP_1_I | NUMBER(6) | Y |  |  |
| 17 | QTD_REG_TP_2 | NUMBER(6) | Y |  |  |
| 18 | QTD_REG_TP_3 | NUMBER(6) | Y |  |  |
| 19 | TOT_REND | NUMBER(17,2) | Y |  |  |
| 20 | TOT_DEDUC | NUMBER(17,2) | Y |  |  |
| 21 | TOT_IRRF | NUMBER(17,2) | Y |  |  |
| 22 | DAT_INI_GERACAO | DATE | Y |  |  |
| 23 | DAT_FIM_GERACAO | DATE | Y |  |  |
| 24 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 25 | IND_ANO_RETENCAO | CHAR(1) | Y |  |  |
| 26 | IND_CENTRAL | CHAR(1) | Y |  |  |
| 27 | COD_NAT_DECLARANTE | VARCHAR2(2) | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |
| 29 | IND_SOCIO_OST | CHAR(1) | Y |  |  |
| 30 | IND_DEPOSITO_CRED | CHAR(1) | Y |  | Declarante depositário de crédito decorrente de decisão judicial |
| 31 | IND_FUNDO_INVEST | CHAR(1) | Y |  | Declarante de instituição administradora ou intermediadora de fundo ou clube de investimento |
| 32 | IND_REND_EXTERIOR | CHAR(1) | Y |  | Declarante de rendimentos pagos a residentes ou domiciliados no exterior |
| 33 | IND_PLANO_SAUDE | CHAR(1) | Y |  | Plano privado de assistência à saúde – coletivo empresarial |
| 34 | ANO_REF | NUMBER(4) | Y |  |  |
| 35 | IND_PAGTO_COPA | CHAR(1) | Y |  | Pagamentos relacionados à Copa das Confederações Fifa2013 e Copa do mundo Fifa2014 |
| 36 | COD_RESP_DECPJ | VARCHAR2(2) | Y |  |  |
| 37 | IND_PAGTO_OLIMP | CHAR(1) | Y |  | Pagamentos relacionados aos Jogos Olímpicos de 2016 e aos Jogos Paraolímpicos de 2016 |
| 38 | IND_CAPITAL_VOTO | CHAR(1) | Y |  |  |
| 39 | IND_DIR_PRIV | CHAR(1) | Y |  |  |

**PK**: NUM_PROC, COD_EMPRESA

**FKs**:
- COD_EQUIP, COD_SOFT_SO → SOFTWARE_EQUIP(COD_EQUIPAMENTO, COD_SOFTWARE)
- COD_RESP_TECNICO → RESP_TECNICO(COD_RESPONSAVEL)
- COD_RESP_LEGAL → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_RESP_DECPJ → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## FDT_DMED_DADOS_REL

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
| 9 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 10 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |
| 11 | IDENT_FIS_JUR_DMED | NUMBER(12) | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 14 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 15 | NUM_PARCELA | NUMBER(3) | N |  |  |
| 16 | DATA_VENCTO | DATE | Y |  |  |
| 17 | DATA_PGTO | DATE | Y |  |  |
| 18 | VLR_PARCELA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_MOVTO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_PARCELA

---

## FDT_DMED_DD_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESP_DECLAR | VARCHAR2(2) | Y |  |  |
| 4 | COD_RESP_EMP | VARCHAR2(2) | Y |  |  |
| 5 | IND_TIPO_DECLAR | CHAR(1) | Y |  |  |
| 6 | NUM_REG_ANS | VARCHAR2(6) | Y |  |  |
| 7 | NUM_CNES | VARCHAR2(7) | Y |  |  |
| 8 | IND_GER_DMED | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESP_DECLAR → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_RESP_EMP → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## FDT_DSC_MUN_N_AMOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | DSC_MUNICIPIO | VARCHAR2(30) | N |  |  |
| 3 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |

**PK**: IDENT_ESTADO, DSC_MUNICIPIO

---

## FDT_EST_CFO_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | CLASSE_APURACAO | CHAR(1) | N |  |  |
| 5 | IDENT_CFO | NUMBER(12) | N |  |  |
| 6 | COD_ITEM_APUR | VARCHAR2(5) | Y |  |  |
| 7 | DSC_ITEM_APUR | VARCHAR2(200) | Y |  |  |
| 8 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 9 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 10 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 11 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 12 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Código de Ajuste Sped Fiscal. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 13 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 14 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 15 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 16 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, CLASSE_APURACAO, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO → OBRIGACAO_FISCAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_TIPO_LIVRO, COD_ITEM_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## FDT_EST_CUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 5 | DT_VALID_CUSTO | DATE | N |  |  |
| 6 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 7 | CUSTO_MEDIO | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 11 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 12 | VLR_ALIQ_MED_ICMS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_ALIQ_MED_PIS | NUMBER(7,4) | Y |  |  |
| 14 | VLR_ALIQ_MED_COFINS | NUMBER(7,4) | Y |  |  |
| 15 | CM_COM_IMPOSTOS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_GERADO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, IDENT_INSUMO, DT_VALID_CUSTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_INSUMO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)

---

## FDT_EST_EXTCF_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | CLASSE_APURACAO | CHAR(1) | N |  |  |
| 5 | IDENT_CFO | NUMBER(12) | N |  |  |
| 6 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |
| 7 | COD_ITEM_APUR | VARCHAR2(5) | Y |  |  |
| 8 | DSC_ITEM_APUR | VARCHAR2(200) | Y |  |  |
| 9 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 10 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 11 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 12 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 13 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Código de Ajuste Sped Fiscal. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 14 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 15 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 16 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 17 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, CLASSE_APURACAO, IDENT_CFO, IDENT_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO → OBRIGACAO_FISCAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)
- COD_TIPO_LIVRO, COD_ITEM_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## FDT_GRUPO_NCM_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | GRUPO_NBM | VARCHAR2(5) | N |  |  |
| 3 | DSC_GRUPO | VARCHAR2(50) | Y |  |  |
| 4 | COD_MEDIDA_GRUPO | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, GRUPO_NBM

---

## FDT_GRUPO_NCM_02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | GRUPO_NBM | VARCHAR2(5) | N |  |  |
| 3 | IDENT_NBM | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, GRUPO_NBM, IDENT_NBM

**FKs**:
- COD_EMPRESA, GRUPO_NBM → FDT_GRUPO_NCM_01(COD_EMPRESA, GRUPO_NBM)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)

---

## FDT_IPI_DARF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | COD_DARF | VARCHAR2(4) | N |  |  |
| 5 | COD_NBM | VARCHAR2(10) | N |  |  |
| 6 | DATA_APURACAO | DATE | N |  |  |
| 7 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 8 | VLR_IPI | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_DARF, COD_NBM, DATA_APURACAO, MOVTO_E_S

---

## FDT_IPI_PRO_IMPRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_NBM | NUMBER(12) | N |  |  |
| 4 | VLR_ALIQ_MED_IPI | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_NBM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)

---

## FDT_LANCTO_P8

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_PAR_LANCTO | VARCHAR2(2) | N |  |  |
| 5 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 6 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 7 | DSC_ITEM_APUR | VARCHAR2(200) | Y |  |  |
| 8 | VLR_ESTORNO | NUMBER(17,2) | Y |  |  |
| 9 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  | Código de ajuste da apuração do IPI de acordo com a Tabela de Códigos de Ajuste da Apuração do IPI (publicada pela RFB). Este campo é obrigatório para a geração do registro  "E530-Ajustes da Apuração do IPI"  do Sped Fiscal. |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PAR_LANCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

---

## FDT_LANCTO_P8_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_PAR_LANCTO | VARCHAR2(2) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 14 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 15 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_PAR_LANCTO, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## FDT_MJUD_ALIQ_TPRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IND_TP_PRODUTO | CHAR(1) | N |  |  |
| 5 | VLR_ALIQ_MEDIA | NUMBER(7,4) | Y |  |  |
| 6 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 7 | COD_MEDIDA_1 | VARCHAR2(8) | Y |  |  |
| 8 | QTD_MEDIDA_1 | NUMBER(17,6) | Y |  |  |
| 9 | COD_MEDIDA_2 | VARCHAR2(8) | Y |  |  |
| 10 | QTD_MEDIDA_2 | NUMBER(17,6) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IND_TP_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MJUD_CRED_IPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IND_TP_PRODUTO | CHAR(1) | N |  |  |
| 5 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ALIQ_MEDIA | NUMBER(7,4) | Y |  |  |
| 7 | VLR_CRED_IPI | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IND_TP_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MJUD_ENTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 8 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | QTD_ENTRADA | NUMBER(17,6) | Y |  |  |
| 11 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 12 | COD_NCM | VARCHAR2(10) | Y |  |  |
| 13 | IND_AGUA | CHAR(1) | Y |  |  |
| 14 | VLR_PERC_AGUA | NUMBER(7,4) | Y |  |  |
| 15 | IND_CERV | CHAR(1) | Y |  |  |
| 16 | VLR_PERC_CERV | NUMBER(7,4) | Y |  |  |
| 17 | IND_REFR | CHAR(1) | Y |  |  |
| 18 | VLR_PERC_REFR | NUMBER(7,4) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | VLR_CRED_IPI_AGUA | NUMBER(17,2) | Y |  |  |
| 22 | VLR_CRED_IPI_CERV | NUMBER(17,2) | Y |  |  |
| 23 | VLR_CRED_IPI_REFR | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MJUD_INS_ESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | IND_AGUA | CHAR(1) | Y |  |  |
| 7 | IND_CERV | CHAR(1) | Y |  |  |
| 8 | IND_REFR | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## FDT_MJUD_PAR_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 4 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 5 | COD_MED_SAIDA_1 | VARCHAR2(8) | Y |  |  |
| 6 | COD_MED_SAIDA_2 | VARCHAR2(8) | Y |  |  |
| 7 | COD_MED_ENTRADA | VARCHAR2(8) | Y |  |  |
| 8 | IND_TP_PAR_SAIDA | CHAR(1) | Y |  |  |
| 9 | IND_TP_CONV_MED | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MJUD_PAR_GPRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | COD_GRUPO_PROD | VARCHAR2(9) | N |  |  |
| 5 | IND_TP_PRODUTO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, COD_GRUPO_PROD

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MJUD_PAR_NCM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_NCM | VARCHAR2(10) | N |  |  |
| 4 | IND_TP_PRODUTO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_NCM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MJUD_PAR_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | IND_TP_PRODUTO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MJUD_SAIDA_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | VLR_BASE_IPI1_A | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TRIB_IPI_A | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_IPI1_C | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TRIB_IPI_C | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_IPI1_R | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIB_IPI_R | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MJUD_SAIDA_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 8 | IND_TP_PRODUTO | CHAR(1) | Y |  |  |
| 9 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 10 | COD_MEDIDA_1 | VARCHAR2(8) | Y |  |  |
| 11 | QTD_MEDIDA_1 | NUMBER(17,6) | Y |  |  |
| 12 | COD_MEDIDA_2 | VARCHAR2(8) | Y |  |  |
| 13 | QTD_MEDIDA_2 | NUMBER(17,6) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_MUNIC_N_AMOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## FDT_PAR_LANCTO_P8

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PAR_LANCTO | VARCHAR2(2) | N |  |  |
| 2 | DSC_PAR_LANCTO | VARCHAR2(50) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 5 | DSC_ITEM_APUR | VARCHAR2(200) | Y |  |  |
| 6 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  | Código de ajuste da apuração do IPI de acordo com a Tabela de Códigos de Ajuste da Apuração do IPI (publicada pela RFB). Este campo é obrigatório para a geração do registro  "E530-Ajustes da Apuração do IPI"  do Sped Fiscal. |

**PK**: COD_PAR_LANCTO

**FKs**:
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

---

## FDT_PFJ_FUNRURAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 2 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 3 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 4 | IND_RET_INSS | CHAR(1) | Y |  |  |

**PK**: GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

---

## FDT_PFJ_SIT_FUNRURAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | DAT_INI | DATE | N |  |  |
| 7 | DAT_FIN | DATE | Y |  |  |
| 8 | IND_SIT_ESP | VARCHAR2(2) | Y |  |  |
| 9 | IND_TIPO_DEP | VARCHAR2(2) | Y |  |  |
| 10 | NUM_PROC_SIT | VARCHAR2(50) | Y |  |  |
| 11 | IND_DEP_FUNRURAL | VARCHAR2(1) | Y | 'N' | Indicador de Deposito Funrural |
| 12 | IND_DEP_SENAR | VARCHAR2(1) | Y | 'N' | Indicador de Deposito Senar |
| 13 | IND_DEP_GILRAT | VARCHAR2(1) | Y | 'N' | Indicador de Deposito Gilrat |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, DAT_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## FDT_PRD_FUNRURAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | IND_RET_INSS | CHAR(1) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## FDT_PROD_INSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_AG_ATO_CONCES | VARCHAR2(4) | N |  |  |
| 4 | ANO_ATO_CONCES | VARCHAR2(4) | N |  |  |
| 5 | NUM_ATO_CONCES | VARCHAR2(6) | N |  |  |
| 6 | DIG_ATO_CONCES | CHAR(1) | N |  |  |
| 7 | IND_PROD_INSUMO | CHAR(1) | N |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 9 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 10 | QTD_PROD_INSUMO | NUMBER(17,6) | Y |  |  |
| 11 | QTD_ATEND | NUMBER(17,6) | Y |  |  |
| 12 | DAT_ULT_ATUALIZ | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES, IND_PROD_INSUMO, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES → FDT_ATO_CONCES(COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)

---

## FDT_SC_PAR_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CFO | NUMBER(12) | N |  |  |
| 2 | COD_TP_OPER_SC | NUMBER(2) | Y |  |  |

**PK**: IDENT_CFO

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_TP_OPER_SC → FDT_SC_TIPO_OPER(COD_TP_OPER_SC)

---

## FDT_SC_PAR_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CFO | VARCHAR2(4) | N |  |  |
| 2 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 4 | COD_TP_OPER_SC | NUMBER(2) | N |  |  |

**PK**: COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_TP_OPER_SC → FDT_SC_TIPO_OPER(COD_TP_OPER_SC)

---

## FDT_SC_PAR_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_OPERACAO | NUMBER(12) | N |  |  |
| 2 | COD_TP_OPER_SC | NUMBER(2) | Y |  |  |

**PK**: IDENT_OPERACAO

**FKs**:
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- COD_TP_OPER_SC → FDT_SC_TIPO_OPER(COD_TP_OPER_SC)

---

## FDT_SC_TIPO_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TP_OPER_SC | NUMBER(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(60) | Y |  |  |
| 3 | IND_MOV | CHAR(1) | Y |  |  |

**PK**: COD_TP_OPER_SC

---

## FDT_UF_AMOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |

**PK**: IDENT_ESTADO

---

