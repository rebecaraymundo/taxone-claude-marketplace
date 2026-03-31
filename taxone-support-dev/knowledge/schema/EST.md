# Módulo: EST (Estadual) - 455 tabelas

## EST_ALC_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CFO | NUMBER(12) | N |  |  |
| 4 | IND_OPER_TRIBUTADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CFO

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_ALC_CFO_NATUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CFO | NUMBER(12) | N |  |  |
| 4 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |
| 5 | IND_OPER_TRIBUTADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CFO, IDENT_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)

---

## EST_ALC_DESC_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | DSC_MUNICIPIO | VARCHAR2(30) | N |  |  |
| 3 | IND_REDUCAO_FISCAL | CHAR(1) | Y |  |  |
| 4 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |

**PK**: IDENT_ESTADO, DSC_MUNICIPIO

**FKs**:
- COD_AREA_LIVR_COM → DWT_AREA_LIVR_COM(COD_AREA_LIVR_COM)

---

## EST_ALC_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MERCADO | VARCHAR2(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_MERCADO

---

## EST_ALC_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | IND_REDUCAO_FISCAL | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_ALC_ZFM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 8 | COD_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 9 | DATA_SAIDA | DATE | Y |  |  |
| 10 | DATA_CANCEL | DATE | Y |  |  |
| 11 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 12 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 13 | COD_MERCADO | VARCHAR2(2) | Y |  |  |
| 14 | NUM_CH | VARCHAR2(12) | Y |  |  |
| 15 | SERIE_CH | VARCHAR2(3) | Y |  |  |
| 16 | SUB_SERIE_CH | VARCHAR2(2) | Y |  |  |
| 17 | IDENT_TRANSP | NUMBER(12) | Y |  |  |
| 18 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_DESC_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_REDU_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_PARC_REDUZ | NUMBER(17,2) | Y |  |  |
| 24 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 26 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 27 | DATA_VISTORIA | DATE | Y |  |  |
| 28 | LOCAL_VISTORIA | VARCHAR2(30) | Y |  |  |
| 29 | DATA_INTERNACAO | DATE | Y |  |  |
| 30 | NUM_COMPROV | VARCHAR2(12) | Y |  |  |
| 31 | DATA_BAIXA | DATE | Y |  |  |
| 32 | NUM_COMPROV_BAIXA | VARCHAR2(12) | Y |  |  |
| 33 | DATA_COMUNIC | DATE | Y |  |  |
| 34 | IND_EMISSAO_CARTA | CHAR(1) | Y |  |  |
| 35 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 36 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 37 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |
| 38 | SITUACAO | CHAR(1) | Y |  |  |
| 39 | VLR_ESTORNO_ICMS | NUMBER(17,2) | Y |  |  |
| 40 | DAT_INTERN_IPI | DATE | Y |  |  |
| 41 | NUM_INTERN_IPI | VARCHAR2(12) | Y |  |  |
| 42 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_MERCADO → EST_ALC_MERC(COD_MERCADO)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- COD_AREA_LIVR_COM → DWT_AREA_LIVR_COM(COD_AREA_LIVR_COM)
- IDENT_TRANSP → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_0678: (IDENT_FIS_JUR)
- IX_FK_SAF_0719: (IDENT_TRANSP)

---

## EST_ALC_ZFM_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | IDENT_CFO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 9 | COD_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 10 | DATA_SAIDA | DATE | Y |  |  |
| 11 | DATA_CANCEL | DATE | Y |  |  |
| 12 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 13 | COD_MERCADO | VARCHAR2(2) | Y |  |  |
| 14 | NUM_CH | VARCHAR2(12) | Y |  |  |
| 15 | SERIE_CH | VARCHAR2(3) | Y |  |  |
| 16 | SUB_SERIE_CH | VARCHAR2(2) | Y |  |  |
| 17 | IDENT_TRANSP | NUMBER(12) | Y |  |  |
| 18 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_DESC_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_REDU_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_PARC_REDUZ | NUMBER(17,2) | Y |  |  |
| 24 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 26 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 27 | DATA_VISTORIA | DATE | Y |  |  |
| 28 | LOCAL_VISTORIA | VARCHAR2(30) | Y |  |  |
| 29 | DATA_INTERNACAO | DATE | Y |  |  |
| 30 | NUM_COMPROV | VARCHAR2(12) | Y |  |  |
| 31 | DATA_BAIXA | DATE | Y |  |  |
| 32 | NUM_COMPROV_BAIXA | VARCHAR2(12) | Y |  |  |
| 33 | DATA_COMUNIC | DATE | Y |  |  |
| 34 | IND_EMISSAO_CARTA | CHAR(1) | Y |  |  |
| 35 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 36 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 37 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |
| 38 | SITUACAO | CHAR(1) | Y |  |  |
| 39 | VLR_ESTORNO_ICMS | NUMBER(17,2) | Y |  |  |
| 40 | DAT_INTERN_IPI | DATE | Y |  |  |
| 41 | NUM_INTERN_IPI | VARCHAR2(12) | Y |  |  |
| 42 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → EST_ALC_ZFM(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_MERCADO → EST_ALC_MERC(COD_MERCADO)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- COD_AREA_LIVR_COM → DWT_AREA_LIVR_COM(COD_AREA_LIVR_COM)
- IDENT_TRANSP → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_EST_ALC_ZFM_CFO_04: (IDENT_FIS_JUR)
- IX_FK_EST_ALC_ZFM_CFO_09: (IDENT_TRANSP)

---

## EST_ALC_ZFM_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 8 | IND_PRODUTO | CHAR(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 12 | COD_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 13 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |
| 14 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 16 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 17 | VLR_PARC_REDUZ | NUMBER(17,2) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## EST_ALIQ_MED_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | VLR_ALIQ_MED_ICMS | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## EST_AL_CAT_DESPESA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DESPESA | VARCHAR2(3) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_DESPESA

---

## EST_AL_REG_41

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | DATE | Y |  |  |
| 4 | DATA_VENCIMENTO | DATE | N |  |  |
| 5 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 6 | VLR_RECEITA | NUMBER(14,2) | Y |  |  |
| 7 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_RECEITA_EST, DATA_VENCIMENTO

**Indexes**:
- IX_EST_AL_REG_41: (COD_EMPRESA, COD_ESTAB, IDENT_RECEITA_EST, DATA_REF)

---

## EST_AL_REG_41_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_VENCIMENTO | DATE | N |  |  |
| 4 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 5 | VLR_RECEITA | NUMBER(14,2) | Y |  |  |

---

## EST_AL_REG_42

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PAGAMENTO | DATE | N |  |  |
| 4 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 5 | VLR_TOTAL_PAGO | NUMBER(14,2) | Y |  |  |
| 6 | COD_AGENTE_ARREC | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PAGAMENTO, IDENT_RECEITA_EST

---

## EST_AL_REG_65

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_FISCAL | NUMBER(4) | N |  |  |
| 4 | DATA_BALANCO | DATE | Y |  |  |
| 5 | IND_LUCRO_BRUTO | CHAR(1) | Y |  |  |
| 6 | IND_SISTEMA_INVENT | CHAR(1) | Y |  |  |
| 7 | IND_CALCULO_ESTOQUE | CHAR(1) | Y |  |  |
| 8 | NUM_EMPREGADOS | NUMBER(5) | Y |  |  |
| 9 | VLR_OUTRAS_RECEITAS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_FISCAL

---

## EST_AL_REG_66

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_FISCAL | NUMBER(4) | N |  |  |
| 4 | VLR_SALDO_INI_01 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Ativo Circulante |
| 5 | VLR_SALDO_FIM_01 | NUMBER(17,2) | Y |  | Valor Saldo Final Ativo Circulante |
| 6 | VLR_SALDO_INI_02 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Disponibilidades |
| 7 | VLR_SALDO_FIM_02 | NUMBER(17,2) | Y |  | Valor Saldo Final Disponibilidades |
| 8 | VLR_SALDO_INI_03 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Clientes |
| 9 | VLR_SALDO_FIM_03 | NUMBER(17,2) | Y |  | Valor Saldo Final Clientes |
| 10 | VLR_SALDO_INI_04 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Outras Contas a Receber |
| 11 | VLR_SALDO_FIM_04 | NUMBER(17,2) | Y |  | Valor Saldo Final Outras Contas a Receber |
| 12 | VLR_SALDO_INI_05 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Ativo Permanente |
| 13 | VLR_SALDO_FIM_05 | NUMBER(17,2) | Y |  | Valor Saldo Final Ativo Permanente |
| 14 | VLR_SALDO_INI_06 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Ativo Imobilizado |
| 15 | VLR_SALDO_FIM_06 | NUMBER(17,2) | Y |  | Valor Saldo Final Ativo Imobilizado |
| 16 | VLR_SALDO_INI_07 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Passivo Circulante |
| 17 | VLR_SALDO_FIM_07 | NUMBER(17,2) | Y |  | Valor Saldo Final Passivo Circulante |
| 18 | VLR_SALDO_INI_08 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Fornecedores |
| 19 | VLR_SALDO_FIM_08 | NUMBER(17,2) | Y |  | Valor Saldo Final Fornecedores |
| 20 | VLR_SALDO_INI_09 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Emprestimos e Financiamentos |
| 21 | VLR_SALDO_FIM_09 | NUMBER(17,2) | Y |  | Valor Saldo Final Emprestimos e Financiamentos |
| 22 | VLR_SALDO_INI_10 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Outras Contas a Pagar |
| 23 | VLR_SALDO_FIM_10 | NUMBER(17,2) | Y |  | Valor Saldo Final Outras Contas a Pagar |
| 24 | VLR_SALDO_INI_11 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Patrimonio Liquido |
| 25 | VLR_SALDO_FIM_11 | NUMBER(17,2) | Y |  | Valor Saldo Final Patrimonio Liquido |
| 26 | VLR_SALDO_INI_12 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Total do Passivo |
| 27 | VLR_SALDO_FIM_12 | NUMBER(17,2) | Y |  | Valor Saldo Final Total do Passivo |
| 28 | VLR_SALDO_INI_13 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Lucro Bruto |
| 29 | VLR_SALDO_FIM_13 | NUMBER(17,2) | Y |  | Valor Saldo Final Lucro Bruto |
| 30 | VLR_SALDO_INI_14 | NUMBER(17,2) | Y |  | Valor Saldo Inicial Lucro Liquido |
| 31 | VLR_SALDO_FIM_14 | NUMBER(17,2) | Y |  | Valor Saldo Final Lucro Liquido |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_FISCAL

---

## EST_AL_REG_67

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_FISCAL | NUMBER(4) | N |  |  |
| 4 | NUM_MEDIDOR | VARCHAR2(8) | N |  |  |
| 5 | QTD_CONSUMO | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_FISCAL, NUM_MEDIDOR

---

## EST_AL_REG_68

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_FISCAL | NUMBER(4) | N |  |  |
| 4 | COD_DESPESA | VARCHAR2(3) | N |  |  |
| 5 | VLR_DESPESA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_FISCAL, COD_DESPESA

**FKs**:
- COD_DESPESA → EST_AL_CAT_DESPESA(COD_DESPESA)

---

## EST_AMP_LEGAL_DIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | DAT_VALIDADE | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO, COD_AMPARO_LEGAL, DAT_VALIDADE

**FKs**:
- IDENT_ESTADO, COD_AMPARO_LEGAL, DAT_VALIDADE → DWT_AMPARO_LEGAL(IDENT_ESTADO, COD_AMPARO_LEGAL, DAT_VALIDADE)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_AP_QUADRO_ESTOQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | N |  |  |
| 2 | IND_ESTOQ_DIAP | VARCHAR2(2) | N |  |  |
| 3 | CLASS_ITEM | VARCHAR2(2) | N | ' ' |  |

**PK**: IND_PRODUTO, IND_ESTOQ_DIAP

---

## EST_BA_DMA_APURAC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | VLR_SAIDA_TRIB | NUMBER(17,2) | Y |  |  |
| 7 | VLR_OUTROS_DEBITO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 9 | VLR_DIF_ALIQ | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOTAL_DEB | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ENT_TRIB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OUTROS_CREDITO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SUBTOTAL | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SCREDOR_PERANT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOTAL_CRED | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SCREDOR_PERSEG | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SALDO_DEVEDOR | NUMBER(17,2) | Y |  |  |
| 19 | VLR_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 20 | VLR_IMP_ARECOLHER | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_ST_ENT | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS_ST_SAI | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_IMPORT | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS_IMP_ACONS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_DIFERIMENTO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_IMP_RECOLHIDO | NUMBER(17,2) | Y |  |  |
| 27 | USUARIO | VARCHAR2(40) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC → EST_BA_DMA_GERAL(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC)

---

## EST_BA_DMA_CREDITO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | VLR_SALDO_ANT_EXP | NUMBER(17,2) | Y |  |  |
| 7 | VLR_EXPD_MES | NUMBER(17,2) | Y |  |  |
| 8 | VLR_EXPIND_MES | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_PG | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRANSF_ESTAB | NUMBER(17,2) | Y |  |  |
| 11 | VLR_IMP_MERC | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DENUNCIA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_AUT_FISCAL | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TRANSF | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DIFERIDO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ISENTO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_REDUCAO_BASE | NUMBER(17,2) | Y |  |  |
| 19 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 23 | VLR_ICMS_PG_OUT | NUMBER(17,2) | Y |  |  |
| 24 | VLR_IMP_MERC_OUT | NUMBER(17,2) | Y |  |  |
| 25 | VLR_DENUNCIA_OUT | NUMBER(17,2) | Y |  |  |
| 26 | VLR_AUT_FISCAL_OUT | NUMBER(17,2) | Y |  |  |
| 27 | VLR_TRANSF_OUT | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC → EST_BA_DMA_GERAL(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC)

---

## EST_BA_DMA_CS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 8 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC, IND_E_S, COD_MUNICIPIO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC → EST_BA_DMA_GERAL(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC)

---

## EST_BA_DMA_CS_VLR_MUN
**Comment**: Tabela utilizada na GIA BA para armazenamento do rateio entre os municipios

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 8 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC, IND_E_S, COD_MUNICIPIO

---

## EST_BA_DMA_DEDUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | VLR_ATIVO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CONSUMO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TRANSF_ATIVO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRANSF_CONSUMO | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 14 | VLR_INSUMO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC, IND_E_S

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC → EST_BA_DMA_GERAL(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC)

---

## EST_BA_DMA_DEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | Y |  |  |
| 4 | ANO_REF | VARCHAR2(4) | Y |  |  |
| 5 | IND_TABELA | CHAR(1) | N |  |  |
| 6 | IND_RETIFIC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_TABELA

---

## EST_BA_DMA_DET_E_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 7 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 8 | IND_E_S | CHAR(1) | N |  |  |
| 9 | COD_REGTO_ICMS | VARCHAR2(2) | N |  |  |
| 10 | COD_UF_OBRIG | VARCHAR2(2) | Y |  |  |
| 11 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC, COD_ESTADO, COD_DETALHE, IND_E_S, COD_REGTO_ICMS

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC, COD_ESTADO, COD_DETALHE, IND_E_S, COD_UF_OBRIG → EST_BA_DMA_E_S(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC, COD_ESTADO, COD_DETALHE, IND_E_S, COD_UF_OBRIG)

---

## EST_BA_DMA_ESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | DAT_APURAC | DATE | N |  |  |
| 7 | COD_NATUR_ESTOQ | VARCHAR2(2) | N |  |  |
| 8 | VLR_ESTOQ | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ESTOQ_NT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ESTOQ_OUTROS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_ESTOQ | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC, DAT_APURAC, COD_NATUR_ESTOQ

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC → EST_BA_DMA_GERAL(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC)

---

## EST_BA_DMA_E_S

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 7 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 8 | IND_E_S | CHAR(1) | N |  |  |
| 9 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 10 | VLR_CONTABIL_NC | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CONTABIL_C | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS_NC | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ICMS_C | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_COMPRAS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TRANSF | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_PET | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS_OUT | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC, COD_ESTADO, COD_DETALHE, IND_E_S, COD_UF_OBRIG

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC → EST_BA_DMA_GERAL(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC)
- COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE → EST_DETALHE(COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE)

---

## EST_BA_DMA_GERAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | IND_MOTIVO_BAIXA | CHAR(1) | Y |  |  |
| 7 | IND_ENQUADRAMENTO | CHAR(1) | Y |  |  |
| 8 | IND_MUDANCA_COND | CHAR(1) | Y |  |  |
| 9 | DAT_FIM_BALANCO | DATE | Y |  |  |
| 10 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 11 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |
| 12 | COD_INSPETORIA | VARCHAR2(2) | Y |  |  |
| 13 | IND_CONS_PERIODO | CHAR(1) | Y |  |  |
| 14 | QTD_FUNC | NUMBER(6) | Y |  |  |
| 15 | QTD_CONSUMO_KWH | NUMBER(7) | Y |  |  |
| 16 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 17 | IND_MODO_PREENCH | CHAR(1) | Y |  |  |
| 18 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 22 | DAT_INI_ESTOQ | DATE | Y |  |  |
| 23 | DAT_FIM_ESTOQ | DATE | Y |  |  |
| 24 | ANO_LAYOUT | NUMBER(4) | Y |  |  |
| 25 | DAT_VALIDADE_INI_ATIVIDADE | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_ATIVIDADE, DAT_VALIDADE_INI_ATIVIDADE → ATIV_ECONOMICA(COD_ATIVIDADE, DAT_VALIDADE_INI)

---

## EST_BA_DMA_ICMS_CR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | VLR_CRED_ATV_SUL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CRED_ATV_NORTE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_ATV_BA_EX | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_UC_SUL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_UC_NORTE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CRED_UC_BA_EX | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC → EST_BA_DMA_GERAL(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC)

---

## EST_BA_DMA_RESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | VARCHAR2(2) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFIC | CHAR(1) | N |  |  |
| 6 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 7 | NOM_RESPONSAVEL | VARCHAR2(35) | Y |  |  |
| 8 | NUM_CPF | VARCHAR2(11) | Y |  |  |
| 9 | NUM_CRC | VARCHAR2(15) | Y |  |  |
| 10 | COD_ESTADO_CRC | VARCHAR2(2) | Y |  |  |
| 11 | TP_LOGRADOURO | VARCHAR2(6) | Y |  |  |
| 12 | DSC_ENDERECO | VARCHAR2(50) | Y |  |  |
| 13 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 14 | DSC_BAIRRO | VARCHAR2(30) | Y |  |  |
| 15 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 16 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 17 | DSC_MUNICIPIO | VARCHAR2(30) | Y |  |  |
| 18 | NUM_CEP | NUMBER(8) | Y |  |  |
| 19 | NUM_TELEFONE | VARCHAR2(24) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC → EST_BA_DMA_GERAL(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_RETIFIC)
- COD_RESPONSAVEL → RESP_CONTADOR(COD_RESPONSAVEL)

---

## EST_CALC_LANC_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | IND_TP_CALC | CHAR(1) | Y |  |  |
| 5 | COD_PAR_LANCTO_01 | VARCHAR2(2) | Y |  |  |
| 6 | COD_PAR_LANCTO_02 | VARCHAR2(2) | Y |  |  |
| 7 | COD_PAR_LANCTO_03 | VARCHAR2(2) | Y |  |  |
| 8 | COD_PAR_LANCTO_04 | VARCHAR2(2) | Y |  |  |
| 9 | COD_PAR_LANCTO_05 | VARCHAR2(2) | Y |  |  |
| 10 | COD_PAR_LANCTO_06 | VARCHAR2(2) | Y |  |  |
| 11 | COD_PAR_LANCTO_07 | VARCHAR2(2) | Y |  |  |
| 12 | COD_PAR_LANCTO_08 | VARCHAR2(2) | Y |  |  |
| 13 | COD_PAR_LANCTO_09 | VARCHAR2(2) | Y |  |  |
| 14 | COD_PAR_LANCTO_10 | VARCHAR2(2) | Y |  |  |
| 15 | COD_PAR_LANCTO_11 | VARCHAR2(2) | Y |  |  |
| 16 | COD_PAR_LANCTO_12 | VARCHAR2(2) | Y |  |  |
| 17 | COD_PAR_LANCTO_13 | VARCHAR2(2) | Y |  |  |
| 18 | COD_PAR_LANCTO_14 | VARCHAR2(2) | Y |  |  |
| 19 | COD_PAR_LANCTO_15 | VARCHAR2(2) | Y |  |  |
| 20 | COD_PAR_LANCTO_16 | VARCHAR2(2) | Y |  |  |
| 21 | COD_PAR_LANCTO_17 | VARCHAR2(2) | Y |  |  |
| 22 | COD_PAR_LANCTO_18 | VARCHAR2(2) | Y |  |  |
| 23 | COD_PAR_LANCTO_19 | VARCHAR2(2) | Y |  |  |
| 24 | DAT_INVENTARIO | DATE | Y |  |  |
| 25 | IND_MUNIC_AOC | CHAR(1) | Y |  |  |
| 26 | COD_CLASSE_REL_04 | VARCHAR2(3) | Y |  |  |
| 27 | COD_REL_04 | VARCHAR2(10) | Y |  |  |
| 28 | IND_SELECAO_04 | CHAR(1) | Y |  |  |
| 29 | IND_PERIODO_04 | CHAR(1) | Y |  |  |
| 30 | COD_CLASSE_REL_09 | VARCHAR2(3) | Y |  |  |
| 31 | COD_REL_09 | VARCHAR2(10) | Y |  |  |
| 32 | COD_CLASSE_REL_12 | VARCHAR2(3) | Y |  |  |
| 33 | COD_REL_12 | VARCHAR2(10) | Y |  |  |
| 34 | COD_CLASSE_REL_13 | VARCHAR2(3) | Y |  |  |
| 35 | COD_REL_13 | VARCHAR2(10) | Y |  |  |
| 36 | IND_SELECAO_13 | CHAR(1) | Y |  |  |
| 37 | COD_CLASSE_REL_14 | VARCHAR2(3) | Y |  |  |
| 38 | COD_REL_14 | VARCHAR2(10) | Y |  |  |
| 39 | COD_CLASSE_REL_15 | VARCHAR2(3) | Y |  |  |
| 40 | COD_REL_15 | VARCHAR2(10) | Y |  |  |
| 41 | IND_SELECAO_15 | CHAR(1) | Y |  |  |
| 42 | IND_SELECAO_16 | CHAR(1) | Y |  |  |
| 43 | IND_SELECAO_17 | CHAR(1) | Y |  |  |
| 44 | IND_SALDO_17 | CHAR(1) | Y |  |  |
| 45 | COD_CLASSE_REL_18 | VARCHAR2(3) | Y |  |  |
| 46 | COD_REL_18 | VARCHAR2(10) | Y |  |  |
| 47 | IND_SELECAO_18 | CHAR(1) | Y |  |  |
| 48 | IND_SALDO_18 | CHAR(1) | Y |  |  |
| 49 | IND_SELECAO_19 | CHAR(1) | Y |  |  |
| 50 | IND_SALDO_19 | CHAR(1) | Y |  |  |
| 51 | COD_PAR_LANCTO_20 | VARCHAR2(2) | Y |  |  |
| 52 | COD_CLASSE_REL_20 | VARCHAR2(3) | Y |  |  |
| 53 | COD_REL_20 | VARCHAR2(10) | Y |  |  |
| 54 | COD_PAR_LANCTO_21 | VARCHAR2(2) | Y |  | Parametro para calculo do estorno de creditos outorgados, criado na OS1373 - V1R16 |
| 55 | COD_PAR_LANCTO_22 | VARCHAR2(2) | Y |  |  |
| 56 | IND_SELECAO_PFJ_04 | CHAR(1) | Y | 'S' | Indicador de utilizacao da parametrizacao de Pessoa Fis Jur para a Classe/Cod de Relatorio. Dominio: 'S', 'N' |
| 57 | IND_SELECAO_MED_04 | CHAR(1) | Y | '1' | Indicador de utilizacao da conversao de Unidade de Medida. Dominio: '1 - padrao','2 - por produto' |
| 58 | COD_PAR_LANCTO_23 | VARCHAR2(2) | Y |  | Parametro para calculo do Credito Presumido SC Decreto 1036 de 2008 |
| 59 | COD_CLASSE_REL_23 | VARCHAR2(3) | Y |  |  |
| 60 | COD_REL_23 | VARCHAR2(10) | Y |  |  |
| 61 | IND_SELECAO_23 | CHAR(1) | Y |  | Indicador de utilizacao da parametrizacao de Extensao CFOP para a Classe/Cod de Relatorio. Dominio: S, N |
| 62 | IND_PERIODO_23 | CHAR(1) | Y |  | Indicador do criterio de Periodo. Dominio: E - data da emissao, F - data fiscal |
| 63 | COD_PAR_LANCTO_24 | VARCHAR2(2) | Y |  | Parametro para Deducoes do ICMS Sub Judice (Port. CAT 187/10) |
| 64 | IND_SELECAO_10 | CHAR(1) | Y |  | Parametro para Credito Outorgado e Estorno de Credito Outorgado |
| 65 | IND_VALOR_CALCULO_04 | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## EST_CALC_LANC_IPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_CALC | CHAR(1) | Y |  |  |
| 4 | COD_PAR_LANCTO_01 | VARCHAR2(2) | Y |  |  |
| 5 | COD_PAR_LANCTO_02 | VARCHAR2(2) | Y |  |  |
| 6 | COD_PAR_LANCTO_03 | VARCHAR2(2) | Y |  |  |
| 7 | COD_PAR_LANCTO_04 | VARCHAR2(2) | Y |  |  |
| 8 | COD_PAR_LANCTO_05 | VARCHAR2(2) | Y |  |  |
| 9 | COD_PAR_LANCTO_06 | VARCHAR2(2) | Y |  |  |
| 10 | DAT_INVENTARIO | DATE | Y |  |  |
| 11 | IND_MUNIC_AOC | CHAR(1) | Y |  |  |
| 12 | IND_SELECAO_04 | CHAR(1) | Y |  |  |
| 13 | IND_SALDO_04 | CHAR(1) | Y |  |  |
| 14 | IND_SELECAO_05 | CHAR(1) | Y |  |  |
| 15 | IND_SALDO_05 | CHAR(1) | Y |  |  |
| 16 | COD_CLASSE_REL_05 | VARCHAR2(3) | Y |  |  |
| 17 | COD_REL_05 | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_CAT87_ADMIN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_EMPRESA_CREDEN | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB_CREDEN | VARCHAR2(6) | N |  |  |
| 5 | DATA_INCLUSAO | DATE | Y |  |  |
| 6 | NUM_CADASTRO_COM | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_EMPRESA_CREDEN, COD_ESTAB_CREDEN

---

## EST_CAT87_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## EST_CAT87_MEIO_PAGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MEIO_PAGTO | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MEIO_PAGTO

**FKs**:
- IDENT_MEIO_PAGTO → DWT_MEIO_PAGTO_ECF(IDENT_MEIO_PAGTO)

---

## EST_CAT87_OPER_TIPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 2 | COD_OPERACAO | VARCHAR2(6) | N |  |  |
| 3 | IND_TIPO_OPERACAO | CHAR(1) | N |  |  |

**PK**: GRUPO_OPERACAO, COD_OPERACAO

---

## EST_CAT87_REL_APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CAIXA_ECF | VARCHAR2(8) | N |  |  |
| 4 | NUM_COO | VARCHAR2(12) | N |  |  |
| 5 | NUM_COMPROVANTE | VARCHAR2(18) | N |  |  |
| 6 | DATA_EMISSAO | DATE | N |  |  |
| 7 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEBITO | NUMBER(17,2) | Y |  |  |
| 9 | CGC_ESTAB | VARCHAR2(15) | Y |  |  |
| 10 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CAIXA_ECF, NUM_COO, NUM_COMPROVANTE, DATA_EMISSAO

---

## EST_CE_AIDF_SEG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | COD_UF_OBRIG_OPER | VARCHAR2(2) | N |  |  |
| 6 | COD_OPERACAO | VARCHAR2(2) | N |  |  |
| 7 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 8 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 9 | COD_SITUACAO | VARCHAR2(2) | N |  |  |
| 10 | COD_TIPO_REGISTRO | VARCHAR2(2) | N |  |  |
| 11 | DAT_EMISSAO | DATE | N |  |  |
| 12 | NRO_AIDF_NF | VARCHAR2(12) | N |  |  |
| 13 | COD_TP_DISP_SEG | VARCHAR2(2) | N |  |  |
| 14 | NUM_CTR_DISP | NUMBER(10) | N |  |  |
| 15 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 16 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 20 | NUM_CAIXA | NUMBER(6) | N | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, COD_UF_OBRIG_OPER, COD_OPERACAO, IDENT_MODELO, COD_UF_OBRIG, COD_SITUACAO, COD_TIPO_REGISTRO, DAT_EMISSAO, NRO_AIDF_NF, NUM_CAIXA, COD_TP_DISP_SEG, NUM_CTR_DISP

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, COD_UF_OBRIG_OPER, COD_OPERACAO, IDENT_MODELO, COD_UF_OBRIG, COD_SITUACAO, COD_TIPO_REGISTRO, DAT_EMISSAO, NRO_AIDF_NF, NUM_CAIXA → EST_CE_REG_AIDF(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, COD_UF_OBRIG_OPER, COD_OPERACAO, IDENT_MODELO, COD_UF_OBRIG, COD_SITUACAO, COD_TIPO_REGISTRO, DAT_EMISSAO, NRO_AIDF_NF, NUM_CAIXA)

---

## EST_CE_APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CRED_ORIGEM | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_DEVIDO | NUMBER(17,2) | Y |  |  |
| 9 | OBSERVACAO | VARCHAR2(100) | Y |  |  |
| 10 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 11 | VLR_EST_CRED_NTRIB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_EST_CRED_OUTR | NUMBER(17,2) | Y |  |  |
| 13 | VLR_EST_CRED_BENS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_EST_MERC_RECEB | NUMBER(17,2) | Y |  |  |
| 15 | VLR_EST_DEB_OUTR | NUMBER(17,2) | Y |  |  |
| 16 | VLR_CPRES_MES | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CRED_INCFISCAL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CRED_ICMS_ANTC | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CRED_DIF_ALIQ | NUMBER(17,2) | Y |  |  |
| 20 | VLR_CRED_REST_INDB | NUMBER(17,2) | Y |  |  |
| 21 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 22 | VLR_CRED_ICMS_DIF | NUMBER(17,2) | Y |  |  |
| 23 | VLR_CRED_OUTROS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_CRED_IMP_ST | NUMBER(17,2) | Y |  |  |
| 25 | VLR_DEB_TRANSF | NUMBER(17,2) | Y |  |  |
| 26 | VLR_DEB_DIF_ALIQ | NUMBER(17,2) | Y |  |  |
| 27 | VLR_DEB_OUTROS | NUMBER(17,2) | Y |  |  |
| 28 | IND_COND_SALDO | CHAR(1) | Y |  |  |
| 29 | VLR_SALDO | NUMBER(17,2) | Y |  |  |
| 30 | VLR_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 31 | VLR_DEB_PER_ANT | NUMBER(17,2) | Y |  |  |
| 32 | VLR_SCREDOR_PERANT | NUMBER(17,2) | Y |  |  |
| 33 | VLR_DEB_PER_SEG | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ICMS_ST_ENT | NUMBER(17,2) | Y |  |  |
| 35 | VLR_ICMS_ST_E_INT | NUMBER(17,2) | Y |  |  |
| 36 | VLR_ICMS_ST_SAI | NUMBER(17,2) | Y |  |  |
| 37 | VLR_ICMS_ST_S_INT | NUMBER(17,2) | Y |  |  |
| 38 | VLR_ICMS_ANTECIP | NUMBER(17,2) | Y |  |  |
| 39 | VLR_ICMS_IMP | NUMBER(17,2) | Y |  |  |
| 40 | USUARIO | VARCHAR2(40) | Y |  |  |
| 41 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 42 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)

---

## EST_CE_DEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TABELA | VARCHAR2(2) | N |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_FINALIDADE | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TABELA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_CE_GERACAO_REG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | SEQ_REG | NUMBER(8) | N |  |  |
| 6 | COD_TIPO_REGISTRO | VARCHAR2(2) | Y |  |  |
| 7 | REGISTRO | VARCHAR2(300) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, SEQ_REG

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)

---

## EST_CE_REG10

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | NUM_TRANSMISSOR | VARCHAR2(20) | N |  |  |
| 3 | IND_TP_TRANSMISSOR | CHAR(1) | Y |  |  |
| 4 | NOM_TRANSMISSOR | VARCHAR2(40) | Y |  |  |
| 5 | NOM_CONTATO | VARCHAR2(20) | Y |  |  |
| 6 | DSC_CARGO | VARCHAR2(15) | Y |  |  |
| 7 | TELEFONE | VARCHAR2(12) | Y |  |  |
| 8 | FAX | VARCHAR2(12) | Y |  |  |
| 9 | ENDERECO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_ENDERECO | VARCHAR2(5) | Y |  |  |
| 11 | COMPL_ENDERECO | VARCHAR2(20) | Y |  |  |
| 12 | BAIRRO | VARCHAR2(15) | Y |  |  |
| 13 | CEP | NUMBER(8) | Y |  |  |
| 14 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 15 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 16 | EMAIL | VARCHAR2(50) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, NUM_TRANSMISSOR

---

## EST_CE_REG20

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | TELEFONE | VARCHAR2(12) | Y |  |  |
| 6 | FAX | VARCHAR2(12) | Y |  |  |
| 7 | ENDERECO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_ENDERECO | VARCHAR2(5) | Y |  |  |
| 9 | COMPL_ENDERECO | VARCHAR2(20) | Y |  |  |
| 10 | BAIRRO | VARCHAR2(30) | Y |  |  |
| 11 | CEP | NUMBER(8) | Y |  |  |
| 12 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 13 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 14 | EMAIL | VARCHAR2(50) | Y |  |  |
| 15 | DAT_INI_INFO_FISC | DATE | Y |  |  |
| 16 | DAT_FIM_INFO_FISC | DATE | Y |  |  |
| 17 | DAT_INVENTARIO | DATE | Y |  |  |
| 18 | IND_INVENTARIO | CHAR(1) | Y |  |  |
| 19 | IND_CONTRIB_IPI | CHAR(1) | Y |  |  |
| 20 | IND_CONTRIB_SUBST | CHAR(1) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 24 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 25 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_CE_REG21

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 6 | NUM_CONTADOR | VARCHAR2(20) | Y |  |  |
| 7 | IND_TP_CONTADOR | CHAR(1) | Y |  |  |
| 8 | NOM_CONTADOR | VARCHAR2(40) | Y |  |  |
| 9 | NUM_CRC | VARCHAR2(15) | Y |  |  |
| 10 | ENDERECO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_ENDERECO | VARCHAR2(5) | Y |  |  |
| 12 | COMPL_ENDERECO | VARCHAR2(20) | Y |  |  |
| 13 | BAIRRO | VARCHAR2(15) | Y |  |  |
| 14 | CEP | NUMBER(8) | Y |  |  |
| 15 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 16 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 17 | EMAIL | VARCHAR2(50) | Y |  |  |
| 18 | TELEFONE | VARCHAR2(12) | Y |  |  |
| 19 | FAX | VARCHAR2(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE

**FKs**:
- COD_RESPONSAVEL → RESP_CONTADOR(COD_RESPONSAVEL)
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)

---

## EST_CE_REG30

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | COD_NCM | VARCHAR2(20) | Y |  |  |
| 7 | IND_TP_PROD_SERV | CHAR(1) | Y |  |  |
| 8 | COD_UNIDADE | VARCHAR2(8) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## EST_CE_REG31

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | COD_EAN | VARCHAR2(14) | N |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO, COD_EAN

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO → EST_CE_REG30(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO)

---

## EST_CE_REG32

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | IDENT_MAT_PRIMA | NUMBER(12) | N |  |  |
| 7 | QTD_COMP_PROD | NUMBER(15,7) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO, IDENT_MAT_PRIMA

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO → EST_CE_REG30(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO)

---

## EST_CE_REG34

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | QTD_ESTOQUE | NUMBER(17,8) | Y |  |  |
| 7 | VLR_UNIT | NUMBER(17,8) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | COND_PRODUTO | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO, COND_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO → EST_CE_REG30(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_PRODUTO)

---

## EST_CE_REG36

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IND_TP_GNRE | CHAR(1) | N |  |  |
| 6 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 7 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 8 | INSC_UF | VARCHAR2(20) | Y |  |  |
| 9 | NUM_BANCO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_AGENCIA | VARCHAR2(5) | Y |  |  |
| 11 | NUM_DV_AGENCIA | VARCHAR2(2) | Y |  |  |
| 12 | NUM_AUTENTIC_GNRE | VARCHAR2(21) | Y |  |  |
| 13 | DAT_RECOLH | DATE | Y |  |  |
| 14 | DAT_VENCTO | DATE | Y |  |  |
| 15 | PERIODO_REF | NUMBER(6) | Y |  |  |
| 16 | VLR_PRINCIPAL | NUMBER(13,2) | Y |  |  |
| 17 | VLR_ATUAL_MONET | NUMBER(13,2) | Y |  |  |
| 18 | VLR_JUROS | NUMBER(13,2) | Y |  |  |
| 19 | VLR_MULTA | NUMBER(13,2) | Y |  |  |
| 20 | VLR_TOT_RECOLHER | NUMBER(13,2) | Y |  |  |
| 21 | NUM_CONVENIO | VARCHAR2(30) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 25 | COD_ESTADO | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IND_TP_GNRE, COD_GNRE, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)

---

## EST_CE_REG37

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_CONTA

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_EST_CE_REG37_CTA: (IDENT_CONTA)

---

## EST_CE_REG38

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | COD_CLASSE_TEL | VARCHAR2(30) | N |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, COD_CLASSE_TEL

**FKs**:
- COD_CLASSE_TEL → EST_CLASSE_TEL(COD_CLASSE_TEL)

---

## EST_CE_REG50

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO_REMET | NUMBER(12) | Y |  |  |
| 3 | COD_MUNIC_COLETA | NUMBER(5) | Y |  |  |
| 4 | IDENT_ESTADO_DEST | NUMBER(12) | Y |  |  |
| 5 | COD_MUNIC_DEST | NUMBER(5) | Y |  |  |
| 6 | DISTANCIA_EM_KM | NUMBER(6) | Y |  |  |
| 7 | QTDE_MERCADORIA | NUMBER(17,6) | Y |  |  |
| 8 | IND_UND_MEDIDA | CHAR(1) | Y |  |  |
| 9 | IND_FORMA_CALC | CHAR(1) | Y |  |  |
| 10 | PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 11 | COD_UF_VEICULO | VARCHAR2(2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: IDENT_CAPA

**FKs**:
- IDENT_CAPA → EST_CE_REG_CAPA(IDENT_CAPA)

---

## EST_CE_REG51

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | IDENT_MODELO_TRANS | NUMBER(12) | N |  |  |
| 3 | SER_DOCFIS_TRANSP | VARCHAR2(3) | N |  |  |
| 4 | S_SER_DOCFIS_TRANS | VARCHAR2(2) | N |  |  |
| 5 | NUM_DOCFIS_TRANSP | VARCHAR2(12) | N |  |  |
| 6 | DATA_EMIS_TRANSP | DATE | N |  |  |
| 7 | VLR_TOT_DOCFIS | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: IDENT_CAPA, IDENT_MODELO_TRANS, SER_DOCFIS_TRANSP, S_SER_DOCFIS_TRANS, NUM_DOCFIS_TRANSP, DATA_EMIS_TRANSP

**FKs**:
- IDENT_CAPA → EST_CE_REG50(IDENT_CAPA)

---

## EST_CE_REG60

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | NUM_ITEM | NUMBER(5) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 4 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 5 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 6 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 7 | QTD_UND_PADRAO | NUMBER(17,8) | Y |  |  |
| 8 | VLR_UNIT_UND_PAD | NUMBER(21,6) | Y |  |  |
| 9 | VLR_UNIT_BRUTO | NUMBER(19,4) | Y |  |  |
| 10 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 11 | COD_ST_NOTA | VARCHAR2(3) | Y |  |  |
| 12 | COD_ST_CUPOM | VARCHAR2(3) | Y |  |  |
| 13 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_AGREG | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_AGREG | NUMBER(17,2) | Y |  |  |
| 17 | COD_ICMS_AGREG | VARCHAR2(2) | Y |  |  |
| 18 | VLR_BASE_ICMS_IMP | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_IMPORT | NUMBER(17,2) | Y |  |  |
| 20 | COD_ICMS_IMPORT | VARCHAR2(2) | Y |  |  |
| 21 | COD_VLR_ICMS | VARCHAR2(2) | Y |  |  |
| 22 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ISENTO_IPI | NUMBER(17,2) | Y |  |  |
| 24 | VLR_OUTROS_IPI | NUMBER(17,2) | Y |  |  |
| 25 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 26 | COD_VLR_IPI | VARCHAR2(2) | Y |  |  |
| 27 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 30 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: IDENT_CAPA, NUM_ITEM

**FKs**:
- IDENT_CAPA → EST_CE_REG_CAPA(IDENT_CAPA)

---

## EST_CE_REG62

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | COD_COND_PARTICIP | VARCHAR2(2) | N |  |  |
| 3 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 4 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 5 | COD_FIS_JUR_PARTIC | VARCHAR2(14) | Y |  |  |
| 6 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 7 | INSC_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: IDENT_CAPA, COD_COND_PARTICIP

**FKs**:
- IDENT_CAPA → EST_CE_REG_CAPA(IDENT_CAPA)

---

## EST_CE_REG64

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | IND_FIS_JUR_TRANSP | CHAR(1) | Y |  |  |
| 3 | COD_TRANSP | VARCHAR2(14) | Y |  |  |
| 4 | COD_UF_TRANSP | VARCHAR2(2) | Y |  |  |
| 5 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 6 | PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 7 | COD_UF_VEICULO | VARCHAR2(2) | Y |  |  |

**PK**: IDENT_CAPA

**FKs**:
- IDENT_CAPA → EST_CE_REG_CAPA(IDENT_CAPA)

---

## EST_CE_REG66

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | COD_TP_DISP_SEG | VARCHAR2(2) | N |  |  |
| 3 | NUM_CTR_DISP | NUMBER(10) | N |  |  |
| 4 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 5 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: IDENT_CAPA, COD_TP_DISP_SEG, NUM_CTR_DISP

**FKs**:
- IDENT_CAPA → EST_CE_REG_CAPA(IDENT_CAPA)

---

## EST_CE_REG67

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | IND_FIS_JUR_EMIT | CHAR(1) | N |  |  |
| 3 | COD_EMITENTE | VARCHAR2(14) | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | IDENT_MODELO_REF | NUMBER(12) | N |  |  |
| 6 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 7 | S_SER_DOCFIS_REF | VARCHAR2(2) | N |  |  |
| 8 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 9 | COD_UF_OBRIG | VARCHAR2(2) | Y |  |  |
| 10 | COD_SITUACAO | VARCHAR2(2) | Y |  |  |
| 11 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 12 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 17 | NRO_AIDF_NF | VARCHAR2(12) | Y |  |  |
| 18 | OBSERVACAO | VARCHAR2(100) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 22 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 23 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 24 | SUB_SERIE_CRT_DISP | VARCHAR2(3) | Y |  |  |
| 25 | NUM_INI_CTR_DISP | NUMBER(10) | Y |  |  |
| 26 | NUM_FIM_CTR_DISP | NUMBER(10) | Y |  |  |

**PK**: IDENT_CAPA, IND_FIS_JUR_EMIT, COD_EMITENTE, COD_AMPARO_LEGAL, IDENT_MODELO_REF, SERIE_DOCFIS_REF, S_SER_DOCFIS_REF, NUM_DOCFIS_REF

**FKs**:
- IDENT_CAPA → EST_CE_REG_CAPA(IDENT_CAPA)
- COD_UF_OBRIG, COD_SITUACAO → EST_SIT_DOCFIS(COD_UF_OBRIG, COD_SITUACAO)

---

## EST_CE_REG69

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | QTD_ITEM_DOCFIS | NUMBER(4) | N |  |  |
| 3 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 4 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 5 | VLR_OUTRAS_DESP | NUMBER(17,2) | Y |  |  |
| 6 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_RETIDO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ANTECIP | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ANTECIP | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 17 | VLR_DIF_ALIQ_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS_IMP | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_IMPORT | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_IPI | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ISENTO_IPI | NUMBER(17,2) | Y |  |  |
| 22 | VLR_OUTROS_IPI | NUMBER(17,2) | Y |  |  |
| 23 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 24 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 25 | USUARIO | VARCHAR2(40) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: IDENT_CAPA, QTD_ITEM_DOCFIS

**FKs**:
- IDENT_CAPA → EST_CE_REG_CAPA(IDENT_CAPA)

---

## EST_CE_REG70

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | COD_UF_OBRIG_OPER | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(2) | Y |  |  |
| 11 | TELEFONE | VARCHAR2(12) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | DAT_EMISSAO | DATE | Y |  |  |
| 14 | DAT_ENT_SAI | DATE | Y |  |  |
| 15 | DAT_VENCTO | DATE | Y |  |  |
| 16 | PERIODO_REF | NUMBER(6) | Y |  |  |
| 17 | COD_CLASSE_USU | VARCHAR2(3) | Y |  |  |
| 18 | COD_COND_PARTICIP | VARCHAR2(2) | Y |  |  |
| 19 | COD_FIS_JUR_PARTIC | VARCHAR2(14) | Y |  |  |
| 20 | IND_TP_PARTICIP | CHAR(1) | Y |  |  |
| 21 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 22 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 23 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 24 | VLR_OUTRAS_DESP | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ABAT_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 28 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 29 | USUARIO | VARCHAR2(40) | Y |  |  |
| 30 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 31 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_FIS_JUR, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)
- COD_OPERACAO, COD_UF_OBRIG_OPER → EST_OPER_DOCFIS(COD_OPERACAO, COD_UF_OBRIG)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_EST_CE_REG70_CTA: (IDENT_CONTA)

---

## EST_CE_REG72

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | NUM_ITEM | NUMBER(5) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 7 | COD_CLASSE_TEL | VARCHAR2(30) | Y |  |  |
| 8 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 9 | PERIODO_REF | NUMBER(6) | Y |  |  |
| 10 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- COD_CLASSE_TEL → EST_CLASSE_TEL(COD_CLASSE_TEL)

---

## EST_CE_REG76

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_FATURA | VARCHAR2(10) | N |  |  |
| 9 | COD_UF_OBRIG_OPER | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(2) | Y |  |  |
| 11 | NUM_CONTA_ENERGIA | VARCHAR2(15) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | DAT_EMISSAO | DATE | Y |  |  |
| 14 | DAT_ENT_SAI | DATE | Y |  |  |
| 15 | DAT_VENCTO | DATE | Y |  |  |
| 16 | PERIODO_REF | NUMBER(6) | Y |  |  |
| 17 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 18 | COD_COND_PARTICIP | VARCHAR2(2) | Y |  |  |
| 19 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 20 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 21 | QTD_CONSUMO_KWH | NUMBER(10) | Y |  |  |
| 22 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 23 | VLR_CONSUMO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_OUTRAS_DESP | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ABAT_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 28 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 29 | VLR_TAXA_ENERGIA | NUMBER(17,2) | Y |  |  |
| 30 | COD_TARIFA | VARCHAR2(6) | Y |  |  |
| 31 | COD_INSCRICAO | VARCHAR2(40) | Y |  |  |
| 32 | USUARIO | VARCHAR2(40) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 34 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 35 | COD_FIS_JUR_PARTIC | VARCHAR2(14) | Y |  |  |
| 36 | IND_TP_PARTICIP | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_FIS_JUR, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_FATURA

**FKs**:
- COD_OPERACAO, COD_UF_OBRIG_OPER → EST_OPER_DOCFIS(COD_OPERACAO, COD_UF_OBRIG)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_EST_CE_REG76_CTA: (IDENT_CONTA)

---

## EST_CE_REG77

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_FATURA | VARCHAR2(10) | N |  |  |
| 9 | NUM_ITEM | NUMBER(5) | N |  |  |
| 10 | QTD_DEMANDA | NUMBER(10) | Y |  |  |
| 11 | VLR_DEMANDA | NUMBER(17,2) | Y |  |  |
| 12 | QTD_ENERGIA | NUMBER(10) | Y |  |  |
| 13 | VLR_ENERGIA | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_FIS_JUR, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_FATURA, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_FIS_JUR, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_FATURA → EST_CE_REG76(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_FIS_JUR, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_FATURA)

---

## EST_CE_REG80

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_DOCFIS_INI | VARCHAR2(12) | N |  |  |
| 9 | NRO_AIDF_NF | VARCHAR2(12) | N |  |  |
| 10 | COD_UF_OBRIG | VARCHAR2(2) | Y |  |  |
| 11 | COD_SITUACAO | VARCHAR2(2) | Y |  |  |
| 12 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, IDENT_MODELO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS_INI, NRO_AIDF_NF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)
- COD_UF_OBRIG, COD_SITUACAO → EST_SIT_DOCFIS(COD_UF_OBRIG, COD_SITUACAO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

---

## EST_CE_REG85

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_IMP_DEB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CONTABIL_OUT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS_OUT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_IMP_DEB_OUT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ISENTAS_OUT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CONTABIL_EXP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)

---

## EST_CE_REG_AIDF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_FINALIDADE | VARCHAR2(2) | N |  |  |
| 5 | COD_UF_OBRIG_OPER | VARCHAR2(2) | N |  |  |
| 6 | COD_OPERACAO | VARCHAR2(2) | N |  |  |
| 7 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 8 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 9 | COD_SITUACAO | VARCHAR2(2) | N |  |  |
| 10 | COD_TIPO_REGISTRO | VARCHAR2(2) | N |  |  |
| 11 | DAT_EMISSAO | DATE | N |  |  |
| 12 | NRO_AIDF_NF | VARCHAR2(12) | N |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 16 | NUM_CAIXA | NUMBER(6) | N | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, COD_UF_OBRIG_OPER, COD_OPERACAO, IDENT_MODELO, COD_UF_OBRIG, COD_SITUACAO, COD_TIPO_REGISTRO, DAT_EMISSAO, NRO_AIDF_NF, NUM_CAIXA

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)
- COD_OPERACAO, COD_UF_OBRIG_OPER → EST_OPER_DOCFIS(COD_OPERACAO, COD_UF_OBRIG)
- COD_UF_OBRIG, COD_SITUACAO → EST_SIT_DOCFIS(COD_UF_OBRIG, COD_SITUACAO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

---

## EST_CE_REG_CAPA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAPA | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_FINALIDADE | VARCHAR2(2) | Y |  |  |
| 6 | DATA_FISCAL | DATE | Y |  |  |
| 7 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 8 | NORM_DEV | CHAR(1) | Y |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 14 | COD_TIPO_REGISTRO | VARCHAR2(2) | Y |  |  |
| 15 | COD_UF_OBRIG_OPER | VARCHAR2(2) | Y |  |  |
| 16 | COD_OPERACAO | VARCHAR2(2) | Y |  |  |
| 17 | COD_UF_OBRIG | VARCHAR2(2) | Y |  |  |
| 18 | COD_SITUACAO | VARCHAR2(2) | Y |  |  |
| 19 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 20 | DAT_EMISSAO | DATE | Y |  |  |
| 21 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 22 | DAT_ENT_SAI | DATE | Y |  |  |
| 23 | NUM_CAIXA | NUMBER(6) | Y |  |  |
| 24 | IND_TP_FRETE | CHAR(1) | Y |  |  |
| 25 | IND_FATURA | CHAR(1) | Y |  |  |
| 26 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 27 | NRO_AIDF_NF | VARCHAR2(12) | Y |  |  |
| 28 | NUM_AUTENTIC_GNRE | VARCHAR2(20) | Y |  |  |
| 29 | COD_MUNIC_AGROP | NUMBER(7) | Y |  |  |
| 30 | USUARIO | VARCHAR2(40) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 32 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: IDENT_CAPA

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE → EST_CE_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE)
- COD_OPERACAO, COD_UF_OBRIG_OPER → EST_OPER_DOCFIS(COD_OPERACAO, COD_UF_OBRIG)
- COD_UF_OBRIG, COD_SITUACAO → EST_SIT_DOCFIS(COD_UF_OBRIG, COD_SITUACAO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_EST_CE_REG_CAPA (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_FINALIDADE, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_TIPO_REGISTRO, IDENT_CFO)
- IX_FK_SAF_1497: (IDENT_FIS_JUR)

---

## EST_CFO_CTRL_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | COD_CTRL_OPER | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_CTRL_OPER → EST_PAR_CTRL_OPER(COD_EMPRESA, COD_ESTAB, COD_CTRL_OPER)

---

## EST_CFO_DET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | IND_E_S | CHAR(1) | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 5 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 6 | IND_AQUIS_TRANSF | CHAR(1) | Y |  |  |

**PK**: COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE, COD_CFOP

**FKs**:
- COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE → EST_DETALHE(COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE)

---

## EST_CLASSE_TEL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSE_TEL | VARCHAR2(30) | N |  |  |
| 2 | DSC_CLASSE_TEL | VARCHAR2(60) | Y |  |  |

**PK**: COD_CLASSE_TEL

---

## EST_CPRES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | DATA_REF | DATE | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | VLR_BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 11 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | N |  |  |
| 12 | VLR_CALCULADO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CREDITADO | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PARCELAS | NUMBER(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, DATA_REF, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, ALIQ_TRIBUTO_ICMS, NUM_PARCELAS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_0774: (IDENT_FIS_JUR)

---

## EST_CPRES_PARC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | DATA_REF | DATE | N |  |  |
| 6 | DATA_CRED | DATE | N |  |  |
| 7 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, DATA_REF, DATA_CRED

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)

---

## EST_CTRL_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CTRL_OPER | VARCHAR2(3) | N |  |  |
| 2 | DSC_CTRL_OPER | VARCHAR2(50) | Y |  |  |

**PK**: COD_CTRL_OPER

---

## EST_CTRL_OPE_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CTRL_OPER | VARCHAR2(3) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | DATA_FISCAL | DATE | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS_RET | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS_RET | VARCHAR2(3) | N |  |  |
| 14 | SSERIE_DOCFIS_RET | VARCHAR2(2) | N |  |  |
| 15 | DATA_DOCFIS_RET | DATE | Y |  |  |
| 16 | DATA_RET | DATE | Y |  |  |
| 17 | VLR_CONTAB_RET | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TRIB_ICMS_RET | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_BASE1_RET | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ALIQ_ICMS_RET | NUMBER(7,4) | Y |  |  |
| 21 | VLR_TRIB_IPI_RET | NUMBER(17,2) | Y |  |  |
| 22 | VLR_IPI_BASE1_RET | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQ_IPI_RET | NUMBER(7,4) | Y |  |  |
| 24 | QUANTIDADE_RET | NUMBER(18,6) | Y |  |  |
| 25 | VLR_MAT_APLIC_RET | NUMBER(17,2) | Y |  |  |
| 26 | VLR_SERVICO_RET | NUMBER(17,2) | Y |  |  |
| 27 | USUARIO | VARCHAR2(40) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 30 | VLR_CONTAB_RET_PERDA | NUMBER(17,2) | Y |  |  |
| 31 | VLR_TRIB_ICMS_RET_PERDA | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMS_BASE1_RET_PERDA | NUMBER(17,2) | Y |  |  |
| 33 | VLR_TRIB_IPI_RET_PERDA | NUMBER(17,2) | Y |  |  |
| 34 | VLR_IPI_BASE1_RET_PERDA | NUMBER(17,2) | Y |  |  |
| 35 | QUANTIDADE_RET_PERDA | NUMBER(18,6) | Y |  |  |
| 36 | IDENT_CFO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CTRL_OPER, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, IDENT_PRODUTO, NUM_DOCFIS_RET, SERIE_DOCFIS_RET, SSERIE_DOCFIS_RET

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CTRL_OPER, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, IDENT_PRODUTO → EST_MOV_CTRL_OPER(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CTRL_OPER, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, IDENT_PRODUTO)

---

## EST_DAPI_MG_PRT_FEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | DATA_VALID | DATE | N |  |  |
| 3 | COD_AJUSTE_SPED_821 | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 4 | COD_AJUSTE_ICMS_822 | VARCHAR2(8) | Y |  | Código de Ajuste da Operação referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal) |
| 5 | COD_AJUSTE_SPED_901 | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 6 | COD_AJUSTE_ICMS_981 | VARCHAR2(8) | Y |  | Código de Ajuste da Operação referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal) |

**PK**: COD_EMPRESA, DATA_VALID

**FKs**:
- COD_AJUSTE_SPED_821 → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_ICMS_822 → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_SPED_901 → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_ICMS_981 → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## EST_DCIP_PAR_INCENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ATIVIDADE | NUMBER(7) | N |  |  |
| 4 | DESCR_LANCTO | VARCHAR2(150) | N |  |  |
| 5 | VLR_ALIQ_INCENT | NUMBER(7,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ATIVIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DCIP_PAR_MODELO_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 4 | COD_MODELO_SEFSC | NUMBER(3) | N |  |  |

**PK**: COD_EMPRESA, GRUPO_MODELO, COD_MODELO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## EST_DCIP_REG100

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | TIPO_REGISTRO | VARCHAR2(3) | N |  |  |
| 5 | TIPO_CREDITO | NUMBER(3) | N |  |  |
| 6 | VLR_CONTRIBUICAO | NUMBER(17,2) | Y |  |  |
| 7 | DETALHE | NUMBER(15) | Y |  |  |
| 8 | DESCR_LANCTO_REG100 | VARCHAR2(150) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, TIPO_REGISTRO, TIPO_CREDITO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DCIP_REG140

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | TIPO_REGISTRO | VARCHAR2(3) | N |  |  |
| 5 | TIPO_CREDITO | NUMBER(3) | N |  |  |
| 6 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |
| 7 | DETALHE | NUMBER(15) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, TIPO_REGISTRO, TIPO_CREDITO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DCIP_REG40

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | TIPO_REGISTRO | VARCHAR2(3) | N |  |  |
| 5 | TIPO_CREDITO | NUMBER(3) | N |  |  |
| 6 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |
| 7 | DETALHE | NUMBER(15) | N |  |  |
| 8 | DESCR_LANCTO_REG40 | VARCHAR2(150) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, TIPO_REGISTRO, TIPO_CREDITO, DETALHE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DCIP_REG60

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | TIPO_REGISTRO | VARCHAR2(3) | N |  |  |
| 5 | TIPO_CREDITO_PRES | NUMBER(3) | N |  |  |
| 6 | VLR_CREDITO_PRES | NUMBER(17,2) | Y |  |  |
| 7 | DETALHE_PRES | NUMBER(15) | Y |  |  |
| 8 | DESCR_LANCTO_REG60 | VARCHAR2(150) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, TIPO_REGISTRO, TIPO_CREDITO_PRES

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DCIP_REG80

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | TIPO_REGISTRO | VARCHAR2(3) | N |  |  |
| 5 | TIPO_CREDITO | NUMBER(3) | N |  |  |
| 6 | VLR_ESTORNO | NUMBER(17,2) | Y |  |  |
| 7 | DETALHE | NUMBER(15) | Y |  |  |
| 8 | DESCR_LANCTO_REG80 | VARCHAR2(150) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, TIPO_REGISTRO, TIPO_CREDITO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DEB_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_DETALHE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | IND_E_S | CHAR(1) | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 5 | DSC_DETALHE | VARCHAR2(50) | Y |  |  |

**PK**: COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE

---

## EST_DET_REGUL_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | IND_E_S | CHAR(1) | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 5 | COD_REGTO_ICMS | VARCHAR2(2) | N |  |  |

**PK**: COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE, COD_REGTO_ICMS

**FKs**:
- COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE → EST_DETALHE(COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_DETALHE)
- COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS → EST_REGUL_ICMS(COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS)

---

## EST_DE_PARA_MEDIDA_FCI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 2 | COD_MEDIDA | VARCHAR2(8) | N |  |  |
| 3 | COD_MEDIDA_FCI | VARCHAR2(6) | N |  |  |

**PK**: GRUPO_MEDIDA, COD_MEDIDA

---

## EST_DE_PARA_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO_OBRIG | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 3 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 4 | COD_MUNICIPIO_DEST | NUMBER(10) | Y |  |  |

**PK**: IDENT_ESTADO_OBRIG, IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_DE_PARA_TDOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | VALID_INICIAL | DATE | N |  |  |
| 3 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 4 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 5 | COD_DOCTO_DEST | VARCHAR2(5) | Y |  |  |
| 6 | DSC_DOCTO_DEST | VARCHAR2(50) | Y |  |  |
| 7 | IND_MODELO_1 | CHAR(1) | Y |  |  |
| 8 | IND_MODELO_1A | CHAR(1) | Y |  |  |

**PK**: COD_ESTADO_OBRIG, VALID_INICIAL, GRUPO_DOCTO, COD_DOCTO

---

## EST_DE_PARA_ZFM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 3 | COD_MUNICIPIO_MSAF | NUMBER(5) | N |  |  |
| 4 | COD_MUNICIPIO_DEST | NUMBER(8) | Y |  |  |

**PK**: COD_ESTADO_OBRIG, COD_ESTADO, COD_MUNICIPIO_MSAF

---

## EST_DIAPAP_INF_INI
**Comment**: Tabela para armazenar as Informacoes Iniciais da Declaracao da DIAP-AP.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | DATE | N |  |  |
| 4 | VLR_DISP_INI | NUMBER(17,2) | Y |  |  |
| 5 | VLR_DISP_FIM | NUMBER(17,2) | Y |  |  |
| 6 | NUM_FUNC_INI | NUMBER(4) | Y |  |  |
| 7 | NUM_FUNC_FIM | NUMBER(4) | Y |  |  |
| 8 | IND_MOVTO_E_S | CHAR(1) | Y |  |  |
| 9 | IND_REDUCAO_BC | CHAR(1) | Y |  |  |
| 10 | IND_OP_INTERESTADUAL | CHAR(1) | Y |  |  |
| 11 | IND_PERIODICIDADE | CHAR(1) | Y |  |  |
| 12 | VLR_DET_DIF_ALIQ_001 | NUMBER(17,2) | Y |  | Valor do Detalhamento Recolhido ou a recolher no prazo legal para a coluna Diferencial de Aliquota Imobilizado |
| 13 | VLR_DET_DIF_ALIQ_002 | NUMBER(17,2) | Y |  | Valor do Detalhamento Recolhido fora do prazo para a coluna Diferencial de Aliquota Imobilizado |
| 14 | VLR_DET_DIF_ALIQ_003 | NUMBER(17,2) | Y |  | Valor do Detalhamento Vencido e não recolhido para a coluna Diferencial de Aliquota Imobilizado |
| 15 | VLR_DET_DIF_ALIQ_004 | NUMBER(17,2) | Y |  | Valor do Detalhamento Benefício Fiscal para a coluna Diferencial de Aliquota Imobilizado |
| 16 | VLR_DET_DIF_ALIQ_005 | NUMBER(17,2) | Y |  | Valor do Detalhamento Recolhido ou a recolher no prazo legal para a coluna ICMS Diferencial de Aliquota Material de Consumo |
| 17 | VLR_DET_DIF_ALIQ_006 | NUMBER(17,2) | Y |  | Valor do Detalhamento Recolhido fora do prazo para a coluna ICMS Diferencial de Aliquota Material de Consumo |
| 18 | VLR_DET_DIF_ALIQ_007 | NUMBER(17,2) | Y |  | Valor do Detalhamento Vencido e não recolhido para a coluna de ICMS Diferencial de Aliquota Material de Consumo |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DIA_AM_CAPA_DOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | ANO_REFER | NUMBER(4) | N |  |  |
| 5 | MES_REFER | NUMBER(2) | N |  |  |
| 6 | NUM_AUTENTIC_NFE | VARCHAR2(44) | N |  |  |
| 7 | NUM_ORD_NOTA | NUMBER(6) | Y |  |  |
| 8 | QTDE_ITEM | NUMBER(3) | Y |  |  |
| 9 | IND_ORIGEM_DOC | CHAR(1) | Y |  |  |
| 10 | IND_RECONHEC | CHAR(1) | Y |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | IND_NF_INFORMADA | CHAR(1) | Y |  |  |
| 13 | DATA_DANFE | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REFER, MES_REFER, NUM_AUTENTIC_NFE

---

## EST_DIA_AM_DD_INIC
**Comment**: Parametrização de dados iniciais, necessários para a geração do arquivo.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESP | VARCHAR2(2) | Y |  |  |
| 4 | IND_COD_PROD | CHAR(1) | Y |  |  |
| 5 | IND_ESTAB_PIM | CHAR(1) | Y | 'N' |  |
| 6 | IND_PROD_ACABADO | VARCHAR2(1) | Y |  |  |
| 7 | IND_ORIGEM_PROD | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESP → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_DIA_AM_ITEM_DOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | ANO_REFER | NUMBER(4) | N |  |  |
| 5 | MES_REFER | NUMBER(2) | N |  |  |
| 6 | NUM_AUTENTIC_NFE | VARCHAR2(44) | N |  |  |
| 7 | NUM_ITEM | NUMBER(3) | N |  |  |
| 8 | COD_PROD_FORN | VARCHAR2(60) | Y |  |  |
| 9 | DSC_PROD_FORN | VARCHAR2(120) | Y |  |  |
| 10 | COD_EAN | NUMBER(14) | Y |  |  |
| 11 | COD_NCM | NUMBER(8) | Y |  |  |
| 12 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 13 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 14 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 16 | IND_TIPO_COD | CHAR(1) | Y |  |  |
| 17 | COD_DECLARADO | VARCHAR2(20) | Y |  |  |
| 18 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |
| 19 | IND_PROD_ACABADO | VARCHAR2(3) | Y |  |  |
| 20 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_MULTIPLICADOR | NUMBER(7,4) | Y |  |  |
| 22 | VLR_IMPOSTO | NUMBER(17,2) | Y |  |  |
| 23 | COD_CST | CHAR(1) | Y |  |  |
| 24 | GRUPO_PRODUTO_ACABADO | CHAR(1) | Y |  |  |
| 25 | IND_PRODUTO_ACABADO | CHAR(1) | Y |  |  |
| 26 | COD_PRODUTO_ACABADO | VARCHAR2(60) | Y |  |  |
| 27 | COD_NCM_ACABADO | VARCHAR2(10) | Y |  |  |
| 28 | COD_PAIS_DEST_ORIG | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REFER, MES_REFER, NUM_AUTENTIC_NFE, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REFER, MES_REFER, NUM_AUTENTIC_NFE → EST_DIA_AM_CAPA_DOC(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REFER, MES_REFER, NUM_AUTENTIC_NFE)
- COD_TRIB_PROD → PRT_COD_TRIB_AM(COD_TRIB_PROD)

---

## EST_DIA_AM_PAR_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |
| 7 | IND_COD_DECL | CHAR(1) | Y |  |  |
| 8 | COD_GGREM | VARCHAR2(15) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_TRIB_PROD → PRT_COD_TRIB_AM(COD_TRIB_PROD)

---

## EST_DIA_AM_PAR_PROD_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 7 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, INSC_ESTADUAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO → EST_DIA_AM_PAR_PROD(COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)

---

## EST_DIA_AM_PROD_ACAB_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | GRUPO_PRODUTO_ACAB | VARCHAR2(9) | N |  |  |
| 7 | IND_PRODUTO_ACAB | CHAR(1) | N |  |  |
| 8 | COD_PRODUTO_ACAB | VARCHAR2(60) | N |  |  |
| 9 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_PRODUTO_ACAB, IND_PRODUTO_ACAB, COD_PRODUTO_ACAB, INSC_ESTADUAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO → EST_DIA_AM_PAR_PROD(COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)

---

## EST_DIEFCE_DAE_IDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_DAE_IDA | VARCHAR2(3) | N |  |  |
| 4 | PERIODO_DAE_IDA | DATE | N |  |  |
| 5 | NUM_ARRECAD_INSC | VARCHAR2(15) | N |  |  |
| 6 | VLR_ARRECAD_INSC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_DAE_IDA, PERIODO_DAE_IDA, NUM_ARRECAD_INSC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DIEFCE_DD_INIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PROVIN_FDI | CHAR(1) | Y | 'N' | S - Sim; N - Não |
| 4 | VLR_PERC_FDI | NUMBER(17,2) | Y |  |  |
| 5 | DAT_VENCTO_FDI | DATE | Y |  |  |
| 6 | IND_TRANSMISSOR | VARCHAR2(2) | Y |  | 11 - CGF (Estabelecimento); 12 - CGF Matriz (CE); 20 - CNPJ; 30 - CPF |
| 7 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 8 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 9 | IND_ORIGEM_INVENT | CHAR(1) | Y |  | A - Automático; M - Manual |
| 10 | IND_INVENT_PRD_NCM | CHAR(1) | Y |  | 1 - Produto; 2 - NCM |
| 11 | IND_GER_VENDA_AMB | CHAR(1) | Y | 'N' |  |
| 12 | IND_TP_REGIME | VARCHAR2(2) | Y | '01' |  |
| 13 | IND_GERA_REG_MES | CHAR(1) | Y | 'N' |  |
| 14 | IND_GERA_REG_STQ | CHAR(1) | Y | 'N' |  |
| 15 | IND_JUST_DOC_FIS | CHAR(1) | Y |  |  |
| 16 | IND_JUST_COD_PROD | CHAR(1) | Y | 'E' |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONTADOR → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_DIEFCE_GNRE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO_FAV | NUMBER(12) | N |  |  |
| 5 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 6 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 7 | INSC_UF_DEST | VARCHAR2(18) | Y |  |  |
| 8 | IDENT_ESTADO_ORIG | NUMBER(12) | Y |  |  |
| 9 | NUM_BANCO | VARCHAR2(3) | Y |  |  |
| 10 | NUM_AGENCIA | VARCHAR2(6) | Y |  |  |
| 11 | NUM_AUTENTIC_GNRE | VARCHAR2(20) | Y |  |  |
| 12 | DAT_RECOLH | DATE | Y |  |  |
| 13 | DAT_VENCTO | DATE | Y |  |  |
| 14 | PERIODO_REF | DATE | Y |  |  |
| 15 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ATUAL_MONET | NUMBER(17,2) | Y |  |  |
| 17 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOT_RECOLHER | NUMBER(17,2) | Y |  |  |
| 20 | NUM_CONVENIO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO_FAV, COD_GNRE, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)

---

## EST_DIEFCE_INVENTARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INVENTARIO | DATE | N |  |  |
| 4 | VLR_INVENTARIO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INVENTARIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DIEFCE_LEX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO | DATE | N |  |  |
| 4 | PERIODO_EXTEMPOR | DATE | N |  |  |
| 5 | VLR_EXTEMPOR | NUMBER(17,2) | Y |  |  |
| 6 | OBS_EXTEMPOR | VARCHAR2(255) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO, PERIODO_EXTEMPOR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DIEFCE_PRI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_PRI | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | VALOR | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER | Y | 0 | Numero que identifica rotina processada |
| 8 | IND_DIG_CALC | CHAR(1) | Y | 1 | Identifica origem do registro: 1 - Digitado; 2 - Gerado/Calculado; 3 - Alterado após gerado ou calculado |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_PRI, IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_DIEFCE_VIR
**Comment**: Tabela auxiliar à geração do registro VIR da DIEF-CE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | Código da empresa |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | Código do estabelecimento |
| 3 | PER_LANCTO | DATE | N |  | Período do lançamento |
| 4 | VLR_ANT_REC | NUMBER(17,2) | Y |  | Valor do ICMS antecipado a recolher |
| 5 | VLR_DIF_ALIQ | NUMBER(17,2) | Y |  | Valor do ICMS diferencial de alíquota a recolher |
| 6 | VLR_ST_ENT | NUMBER(17,2) | Y |  | Valor do ICMS substituição tributária nas entradas a recolher |

**PK**: COD_EMPRESA, COD_ESTAB, PER_LANCTO

---

## EST_DIEFSC_DD_INIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_EXERCICIO | NUMBER(4) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | Y |  |  |
| 5 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 6 | NUM_EMPREGADOS | NUMBER(4) | Y |  |  |
| 7 | IND_ESPECIE | CHAR(1) | Y |  |  |
| 8 | VLR_RECEITA_BRUTA | NUMBER(19,2) | Y |  |  |
| 9 | VLR_PRO_LABORE | NUMBER(19,2) | Y |  |  |
| 10 | VLR_COMISSAO_SAL | NUMBER(19,2) | Y |  |  |
| 11 | VLR_COMB_LUBRIF | NUMBER(19,2) | Y |  |  |
| 12 | VLR_ENC_SOCIAIS | NUMBER(19,2) | Y |  |  |
| 13 | VLR_TRIB_FED | NUMBER(19,2) | Y |  |  |
| 14 | VLR_TRIB_EST | NUMBER(19,2) | Y |  |  |
| 15 | VLR_TRIB_MUN | NUMBER(19,2) | Y |  |  |
| 16 | VLR_AGUA_TEL | NUMBER(19,2) | Y |  |  |
| 17 | VLR_ENERG_ELET | NUMBER(19,2) | Y |  |  |
| 18 | VLR_ALUGUEL | NUMBER(19,2) | Y |  |  |
| 19 | VLR_SERV_PROF | NUMBER(19,2) | Y |  |  |
| 20 | VLR_SEGUROS | NUMBER(19,2) | Y |  |  |
| 21 | VLR_FRETE_CAR | NUMBER(19,2) | Y |  |  |
| 22 | VLR_DESP_FINANC | NUMBER(19,2) | Y |  |  |
| 23 | VLR_OUT_DESP | NUMBER(19,2) | Y |  |  |
| 24 | VLR_SUBSIDIO_E_GOV | NUMBER(19,2) | Y |  |  |
| 25 | VLR_SUBSIDIO_S_GOV | NUMBER(19,2) | Y |  |  |
| 26 | VLR_EXC_ISS_ENT | NUMBER(19,2) | Y |  |  |
| 27 | VLR_EXC_ISS_SAI | NUMBER(19,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_EXERCICIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_DIEF_ES_CRED_ACUMULA
**Comment**: Tabela criada para atendimento aos registros F e G - Creditos Acumulados no Mês e Detalher

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO | DATE | N |  |  |
| 4 | NUM_SEQ_DETALHE | NUMBER(3) | N |  | Sequencial único identificador dos registros de detalhe. |
| 5 | IND_ESPECIE_MOV | CHAR(1) | Y |  | Valores assumidos: 1 - Transporte do Mês Anterior, 2 - Recebimento por Transferência, 3 - Saídas para Exterior, 4 - Prestação para o Exterior, 5 - Outros Créditos Gerados, 6 - Reincorporação |
| 6 | DSC_OUTROS_CRED | VARCHAR2(60) | Y |  |  |
| 7 | IND_TP_DETALHE | CHAR(1) | Y |  | Valores assumidos: T - Transferência, R - Recebimento, C - Utilização por Compensação |
| 8 | IND_NATUREZA_OP | VARCHAR2(2) | Y |  |  |
| 9 | DSC_OUTRAS_SIT | VARCHAR2(60) | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO, NUM_SEQ_DETALHE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_2117: (IDENT_FIS_JUR)

---

## EST_DIEF_ES_INF_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO | DATE | N |  |  |
| 4 | VLR_DIF_ALIQUOTA | NUMBER(17,2) | Y |  |  |
| 5 | VLR_FUNDAP | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ESTIM_SUPERM | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ESTIM_ATACAD | NUMBER(17,2) | Y |  |  |
| 8 | DESC_OUTR_ICMS | VARCHAR2(30) | Y |  |  |
| 9 | VLR_OUTR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | DESC_OUTR_DESPES | VARCHAR2(30) | Y |  |  |
| 11 | VLR_OUTR_DESPES | NUMBER(17,2) | Y |  |  |
| 12 | DESC_OUTR_ICMS_1 | VARCHAR2(30) | Y |  |  |
| 13 | VLR_OUTR_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 14 | DESC_OUTR_ICMS_2 | VARCHAR2(30) | Y |  |  |
| 15 | VLR_OUTR_ICMS_2 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DIEF_ES_OPER_SIT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_OPER | VARCHAR2(2) | N |  |  |
| 4 | GRUPO_SITUACAO_B | VARCHAR2(9) | N |  |  |
| 5 | COD_SITUACAO_B | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_OPER, GRUPO_SITUACAO_B, COD_SITUACAO_B

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DIEF_ES_VENCIMENTOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO | DATE | N |  |  |
| 4 | LINHA | NUMBER(2) | N |  |  |
| 5 | COD_RECEITA | VARCHAR2(4) | Y |  |  |
| 6 | DAT_VENCIMENTO | DATE | Y |  |  |
| 7 | VLR_VENCIMENTO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO, LINHA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DIF_TO_DD_ANUAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFER | NUMBER(4) | N |  |  |
| 4 | IND_CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 5 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 6 | VLR_SALDO_FIM | NUMBER(17,2) | Y |  |  |
| 7 | VLR_PATRIM_LIQ | NUMBER(17,2) | Y |  |  |
| 8 | IND_MUD_DOMIC | CHAR(1) | Y |  |  |
| 9 | DATA_INI_ATUAL | DATE | Y |  |  |
| 10 | DATA_FIM_ATUAL | DATE | Y |  |  |
| 11 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 12 | COD_MUNIC_B | NUMBER(5) | Y |  |  |
| 13 | DATA_INI_B | DATE | Y |  |  |
| 14 | DATA_FIM_B | DATE | Y |  |  |
| 15 | COD_MUNIC_C | NUMBER(5) | Y |  |  |
| 16 | DATA_INI_C | DATE | Y |  |  |
| 17 | DATA_FIM_C | DATE | Y |  |  |
| 18 | COD_MUNIC_D | NUMBER(5) | Y |  |  |
| 19 | DATA_INI_D | DATE | Y |  |  |
| 20 | DATA_FIM_D | DATE | Y |  |  |
| 21 | COD_MUNIC_E | NUMBER(5) | Y |  |  |
| 22 | DATA_INI_E | DATE | Y |  |  |
| 23 | DATA_FIM_E | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFER

**FKs**:
- IDENT_ESTADO, COD_MUNIC_B → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_ESTADO, COD_MUNIC_C → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_ESTADO, COD_MUNIC_D → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_ESTADO, COD_MUNIC_E → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_DIF_TO_DD_INIC
**Comment**: Parametrização de dados iniciais, necessários para a geração do arquivo.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_SIMPLES_NAC | CHAR(1) | Y |  |  |
| 4 | IND_FINALIDADE | CHAR(1) | Y |  |  |
| 5 | IND_TIPO_ESCRIT | CHAR(1) | Y |  |  |
| 6 | COD_RESP | VARCHAR2(2) | Y |  |  |
| 7 | COD_CONT_RESP | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESP → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONT_RESP → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_DIMP_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VLR_TOT_MES | NUMBER(17,2) | Y |  |  |
| 4 | QTD_TOT_TRANSACOES | NUMBER(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## EST_DMD_BA_DD_INIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESP | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESP → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_DMD_BA_PAR_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PRODUTO_DMD | VARCHAR2(5) | Y |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DMD_BA_PAR_EXTCFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PRODUTO_DMD | VARCHAR2(5) | Y |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DMD_BA_PAR_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_PRODUTO_DMD | VARCHAR2(5) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO_INI | VARCHAR2(60) | N |  |  |
| 8 | COD_PRODUTO_FIM | VARCHAR2(60) | Y |  |  |
| 9 | IND_EXCECAO | CHAR(1) | Y |  |  |
| 10 | NUM_HABILIT | VARCHAR2(12) | Y |  |  |
| 11 | IND_STATUS_PROD | CHAR(1) | Y |  |  |
| 12 | DATA_REF_BAIXA | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_PRODUTO_DMD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DMD_BA_PAR_PROD_EXC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_PRODUTO_DMD | VARCHAR2(5) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO_INI | VARCHAR2(60) | N |  |  |
| 8 | COD_PRODUTO_EXC | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_PRODUTO_DMD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI, COD_PRODUTO_EXC

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_PRODUTO_DMD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI → EST_DMD_BA_PAR_PROD(COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_PRODUTO_DMD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO_INI)

---

## EST_DOT_ES_DET_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_DET | VARCHAR2(2) | N |  |  |
| 4 | MES_ANO_OPERACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | COD_MUNICIPIO_DEST | NUMBER(10) | N |  |  |
| 7 | VLR_APURADO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DISTRIB | NUMBER(17,2) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_TP_DET, MES_ANO_OPERACAO, IDENT_ESTADO, COD_MUNICIPIO_DEST

---

## EST_DOT_ES_QUADROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_OPERACAO | DATE | N |  |  |
| 4 | DATA_FIM_OPERACAO | DATE | N |  |  |
| 5 | IND_QUADRO | CHAR(1) | N |  |  |
| 6 | IND_TIPO | VARCHAR2(2) | N |  |  |
| 7 | IDENT_CFO | NUMBER(12) | N |  |  |
| 8 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 9 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 10 | VLR_APURADO | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI_OPERACAO, DATA_FIM_OPERACAO, IND_QUADRO, IND_TIPO, IDENT_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## EST_DOT_ES_QUAD_C_D

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_GERACAO | NUMBER(4) | N |  |  |
| 4 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 5 | DSC_INF_COMPL | VARCHAR2(500) | Y |  |  |
| 6 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_GERACAO

---

## EST_DPIGO_DD_INIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | DATE | N |  |  |
| 4 | PERC_FINANC | NUMBER(3) | Y |  |  |
| 5 | VLR_ICMS_MEDIA | NUMBER(17,2) | Y |  |  |
| 6 | SLD_DEV_N_BENEF | NUMBER(17,2) | Y |  |  |
| 7 | SLD_CRED_N_BENEF | NUMBER(17,2) | Y |  |  |
| 8 | SLD_CRED_N_FINANC | NUMBER(17,2) | Y |  |  |
| 9 | SLD_DEV_N_CONTRIB | NUMBER(17,2) | Y |  |  |
| 10 | SLD_DEV_CONTRIB | NUMBER(17,2) | Y |  |  |
| 11 | DISPONIBILIDADE_INICIAL | NUMBER(17,2) | Y |  |  |
| 12 | DISPONIBILIDADE_FINAL | NUMBER(17,2) | Y |  |  |
| 13 | EMPREGADOS_INICIAL | NUMBER(16) | Y |  |  |
| 14 | EMPREGADOS_FINAL | NUMBER(16) | Y |  |  |
| 15 | TARE_PARTE_N_BENEF | NUMBER(17,2) | Y |  |  |
| 16 | TARE_ICMS_MEDIA | NUMBER(17,2) | Y |  |  |
| 17 | TARE_PARTE_N_FINANC | NUMBER(17,2) | Y |  |  |
| 18 | TARE_ESP_PARTE_N_BENEF | NUMBER(17,2) | Y |  |  |
| 19 | TARE_ESP_ICMS_MEDIA | NUMBER(17,2) | Y |  |  |
| 20 | TARE_ESP_PARTE_N_FINANC | NUMBER(17,2) | Y |  |  |
| 21 | TIPO_ESCRITA | NUMBER(1) | Y |  |  |
| 22 | DEPOSITO_JUDICIAL | NUMBER(17,2) | Y |  |  |
| 23 | IND_PROTEGE | NUMBER(1) | Y |  |  |
| 24 | RECEITAS_OPERAC | NUMBER(17,2) | Y |  |  |
| 25 | RECEITAS_N_OPERAC | NUMBER(17,2) | Y |  |  |
| 26 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 27 | SLD_DEV_PERIODO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CONTADOR → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_DPIGO_OBR_PRINC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | VARCHAR2(6) | N |  |  |
| 4 | COD_DETALHAMENTO | NUMBER(2) | N |  |  |
| 5 | COD_APURACAO | NUMBER(3) | Y |  |  |
| 6 | VLR_ICMS_APURADO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REF, COD_DETALHAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_DPIGO_PROD_ALCOOL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | VARCHAR2(6) | N |  |  |
| 4 | DIA | NUMBER(2) | N |  |  |
| 5 | VLR_ALCOOL_ANIDRO | NUMBER(17) | Y |  |  |
| 6 | VLR_ALCOOL_HIDRA | NUMBER(17) | Y |  |  |
| 7 | VLR_ACUCAR | NUMBER(17) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REF, DIA

---

## EST_DPIGO_PROTEGE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | VARCHAR2(6) | N |  |  |
| 4 | SEQUENCIAL | NUMBER(12) | N |  |  |
| 5 | DISP_ANEXO_RCTE | VARCHAR2(2) | Y |  |  |
| 6 | NUM_TARE | VARCHAR2(18) | Y |  |  |
| 7 | VLR_REDUCAO_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REF, SEQUENCIAL

---

## EST_DSC_MUN_N_AMOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | DSC_MUNICIPIO | VARCHAR2(30) | N |  |  |
| 3 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |

**PK**: IDENT_ESTADO, DSC_MUNICIPIO

---

## EST_DUB_CAD_BENEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESPECIE | VARCHAR2(2) | N |  |  |
| 4 | IND_TIPO_CALC | VARCHAR2(2) | N |  |  |
| 5 | COD_ATO_LEGAL | VARCHAR2(2) | Y |  |  |
| 6 | NUMERO_ANO | VARCHAR2(12) | Y |  |  |
| 7 | DATA_INI | DATE | Y |  |  |
| 8 | GRUPO_OBSERVACAO | VARCHAR2(9) | N | ' ' |  |
| 9 | COD_OBSERVACAO | VARCHAR2(8) | N | ' ' |  |
| 10 | VLR_PERC | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESPECIE, IND_TIPO_CALC, GRUPO_OBSERVACAO, COD_OBSERVACAO

**FKs**:
- COD_ATO_LEGAL, NUMERO_ANO, COD_ESPECIE, DATA_INI → PRT_CAD_BENEF_ICMS(COD_ATO_LEGAL, NUMERO_ANO, COD_ESPECIE, DATA_INI)

---

## EST_DUB_CALC_BENEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESPECIE | VARCHAR2(2) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | COD_ATO_LEGAL | VARCHAR2(2) | N |  |  |
| 13 | NUMERO_ANO | VARCHAR2(12) | N |  |  |
| 14 | DATA_INI | DATE | N |  |  |
| 15 | IND_TIPO_CALC | VARCHAR2(2) | Y |  |  |
| 16 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 18 | VLR_PERC | NUMBER(7,4) | N |  |  |
| 19 | VLR_ICMS_DEB | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESPECIE, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_ATO_LEGAL, NUMERO_ANO, DATA_INI, VLR_PERC

---

## EST_DUB_CALC_BENEF_CR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESPECIE | VARCHAR2(2) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 13 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 14 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 15 | COD_ATO_LEGAL | VARCHAR2(2) | Y |  |  |
| 16 | NUMERO_ANO | VARCHAR2(12) | Y |  |  |
| 17 | DATA_INI | DATE | Y |  |  |
| 18 | IND_TIPO_CALC | VARCHAR2(2) | Y |  |  |
| 19 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_PERC_C | NUMBER(7,4) | Y |  |  |
| 21 | VLR_ICMS_DEB_C | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESPECIE, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_CFOP, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## EST_DUB_CALC_BENEF_DIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESPECIE | VARCHAR2(2) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | COD_ATO_LEGAL | VARCHAR2(2) | N |  |  |
| 13 | NUMERO_ANO | VARCHAR2(12) | N |  |  |
| 14 | DATA_INI | DATE | N |  |  |
| 15 | IND_TIPO_CALC | VARCHAR2(2) | Y |  |  |
| 16 | VLR_BEM | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SAIDA | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 19 | VLR_PERC | NUMBER(7,4) | Y |  |  |
| 20 | VLR_ICMS_DEB | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESPECIE, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_ATO_LEGAL, NUMERO_ANO, DATA_INI

---

## EST_DUB_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 4 | IND_TIPO_BENEF | VARCHAR2(1) | Y | '1' |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_DUB_PAR_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESPECIE | VARCHAR2(2) | N |  |  |
| 4 | IND_TIPO_CALC | VARCHAR2(2) | N |  |  |
| 5 | GRUPO_OBSERVACAO | VARCHAR2(9) | N |  |  |
| 6 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 7 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 8 | GRUPO_SITUACAO_A | VARCHAR2(9) | N |  |  |
| 9 | COD_SITUACAO_A | VARCHAR2(1) | N |  |  |
| 10 | GRUPO_SITUACAO_B | VARCHAR2(9) | N |  |  |
| 11 | COD_SITUACAO_B | VARCHAR2(2) | N |  |  |
| 12 | VLR_PERC | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESPECIE, IND_TIPO_CALC, GRUPO_OBSERVACAO, COD_OBSERVACAO, COD_ESTADO, GRUPO_SITUACAO_A, COD_SITUACAO_A, GRUPO_SITUACAO_B, COD_SITUACAO_B

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_ESPECIE, IND_TIPO_CALC, GRUPO_OBSERVACAO, COD_OBSERVACAO → EST_DUB_CAD_BENEF(COD_EMPRESA, COD_ESTAB, COD_ESPECIE, IND_TIPO_CALC, GRUPO_OBSERVACAO, COD_OBSERVACAO)

---

## EST_DUB_PAR_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 4 | IND_TIPO_CALC | VARCHAR2(2) | Y |  |  |
| 5 | COD_ATO_LEGAL | VARCHAR2(2) | Y |  |  |
| 6 | NUMERO_ANO | VARCHAR2(12) | Y |  |  |
| 7 | COD_ESPECIE | VARCHAR2(2) | Y |  |  |
| 8 | DATA_INI | DATE | Y |  |  |
| 9 | VLR_PERC | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFOP

---

## EST_DUB_PAR_EXTCFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | IND_TIPO_CALC | VARCHAR2(2) | Y |  |  |
| 7 | COD_ATO_LEGAL | VARCHAR2(2) | Y |  |  |
| 8 | NUMERO_ANO | VARCHAR2(12) | Y |  |  |
| 9 | COD_ESPECIE | VARCHAR2(2) | Y |  |  |
| 10 | DATA_INI | DATE | Y |  |  |
| 11 | VLR_PERC | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFOP, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## EST_DUB_PAR_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESPECIE | VARCHAR2(2) | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESPECIE, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## EST_DUB_PAR_PROD_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_CFOP_NAT | CHAR(1) | N |  |  |
| 4 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 7 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 8 | IND_PRODUTO | CHAR(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_CFOP_NAT, COD_CFOP, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## EST_EXT_CTRL_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | COD_CTRL_OPER | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_CTRL_OPER → EST_PAR_CTRL_OPER(COD_EMPRESA, COD_ESTAB, COD_CTRL_OPER)

---

## EST_FCI_CALC_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | COD_MEDIDA_FCI | VARCHAR2(6) | N |  |  |
| 6 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 7 | IDENT_SUBPRODUTO | NUMBER(12) | N |  |  |
| 8 | IDENT_REF_PROD | NUMBER(12) | N |  |  |
| 9 | IND_NIVEL | NUMBER(3) | N |  |  |
| 10 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 11 | COD_MEDIDA_SUB | VARCHAR2(8) | Y |  |  |
| 12 | VLR_MED_IMP | NUMBER(17,2) | Y |  |  |
| 13 | QTD_INSUMO | NUMBER(17,6) | Y |  |  |
| 14 | QTD_PRODUTO | NUMBER(17,6) | Y |  |  |
| 15 | VLR_PARC_IMP | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO, COD_MEDIDA_FCI, IDENT_INSUMO, IDENT_SUBPRODUTO, IDENT_REF_PROD, IND_NIVEL

---

## EST_FCI_LISTA_TECNICA_REL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 7 | DATA_MOVTO | DATE | N |  |  |
| 8 | GRUPO_PRODUTO_ACAB | VARCHAR2(9) | Y |  |  |
| 9 | IND_PRODUTO_ACAB | CHAR(1) | Y |  |  |
| 10 | COD_PRODUTO_ACAB | VARCHAR2(60) | Y |  |  |
| 11 | ARVORE_LISTA | LONG | Y |  |  |
| 12 | GRUPO_PRODUTO_COMP | VARCHAR2(9) | Y |  |  |
| 13 | IND_PRODUTO_COMP | CHAR(1) | Y |  |  |
| 14 | COD_PRODUTO_COMP | VARCHAR2(60) | Y |  |  |
| 15 | CRITICA | VARCHAR2(450) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_MOVTO

---

## EST_FCI_MOV_PROD_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | COD_MEDIDA_FCI | VARCHAR2(6) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | DATA_FISCAL | DATE | Y |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 15 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO, COD_MEDIDA_FCI, NUM_DOCFIS, SERIE_DOCFIS, NUM_ITEM

---

## EST_FCI_PROD_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | VLR_MEDIO_IMP | NUMBER(17,2) | Y |  |  |
| 6 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO

---

## EST_FCI_PROD_IMP_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | DATA_FISCAL | DATE | Y |  |  |
| 10 | NUM_ITEM | NUMBER(5) | N |  |  |
| 11 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 12 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 13 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 14 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 15 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 16 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 17 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ADUANEIRO | NUMBER(17,2) | Y |  |  |
| 21 | VLR_CALCULO | NUMBER(17,2) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 24 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 25 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 26 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, NUM_ITEM

---

## EST_FCI_PROD_NAC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 6 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 7 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 8 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO

---

## EST_FCI_PROD_NAC_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | DATA_FISCAL | DATE | Y |  |  |
| 10 | NUM_ITEM | NUMBER(5) | N |  |  |
| 11 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 12 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 13 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 14 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 15 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 16 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 17 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, NUM_ITEM

---

## EST_GIA_INFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 5 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 6 | IND_DIG_CAL | CHAR(1) | Y |  |  |
| 7 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 8 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | N |  |  |
| 9 | IDENT_ESTADO | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CLASSE, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCORR, IDENT_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_GIA_INFO_INCE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 5 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | N |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 8 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 9 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 10 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CLASSE, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCORR, IDENT_ESTADO, SERIE_LIVRO, SUB_SERIE_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_GIA_RECEITA_MES
**Comment**: Tabela que pode ser usada em obrigações estaduais, mensais, para armazenar o valor de outros receitas do mês.  Está sendo usada na DIEF-PA.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | VLR_OUTR_RECEITA | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ESTOQ_VENDA_INI | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ESTOQ_USO_INI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ESTOQ_TERCEIRO_INI | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ESTOQ_VENDA_FIM | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ESTOQ_USO_FIM | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ESTOQ_TERCEIRO_FIM | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_DIFERENCIADO | NUMBER(17,2) | Y |  | Campo preenchido caso a Empresa possua um termo de acordo a SEFAZ autorizando um tratamento Diferenciado do ICMS |
| 13 | VLR_ICMS_DIF_ST_INT | NUMBER(17,2) | Y |  | Campo preenchido caso a Empresa possua um termo de acordo a SEFAZ autorizando um tratamento Diferenciado do ICMS-ST Interno |
| 14 | VLR_ICMS_GLOSA | NUMBER(17,2) | Y |  | Campo preenchido com o valor da guia de recolhimento gerada pelo Fisco para compras de mercadorias de outros estados pela Empresa |
| 15 | VLR_INCENT_LEI_6489 | NUMBER(17,2) | Y |  | Campo preenchido com o valor do Incentivo Financeiro concedido pela Lei Num 6.489/2002 |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_GIA_RECOLH_ICMS
**Comment**: Tabela que pode ser usada em obrigações estaduais, mensais, para armazenar por código de receita estadual, o valor do recolhimento do ICMS. Está sendo usada na DIEF-PA.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 6 | VLR_RECOLH_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RESSARC | NUMBER(17,2) | Y |  |  |
| 8 | MES_RECOLH | NUMBER(2) | N |  |  |
| 9 | ANO_RECOLH | NUMBER(4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, MES_RECOLH, ANO_RECOLH, IDENT_RECEITA_EST

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF → EST_GIA_RECEITA_MES(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF)

---

## EST_GIA_SC_SEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | COD_SEF | VARCHAR2(5) | N |  |  |
| 5 | VLR_SEF | NUMBER(17,2) | Y |  |  |
| 6 | DSC_SEF | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, COD_SEF

---

## EST_GIA_SP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IND_TP_GIA | CHAR(1) | Y |  |  |
| 5 | MES_REF | NUMBER(2) | Y |  |  |
| 6 | ANO_REF | NUMBER(4) | Y |  |  |
| 7 | IND_TP_REGIME | VARCHAR2(2) | Y |  |  |
| 8 | IND_DECENDIO | CHAR(1) | Y |  |  |
| 9 | IND_TP_OPER | CHAR(1) | Y |  |  |
| 10 | IND_TP_MOVTO | CHAR(1) | Y |  |  |
| 11 | VLR_FATUR_MES | NUMBER(16,2) | Y |  |  |
| 12 | VLR_UFESP_PER | NUMBER(16,3) | Y |  |  |
| 13 | VLR_OUT_DEDUC | NUMBER(16,3) | Y |  |  |
| 14 | NUM_EMPREG_PROD | NUMBER(8) | Y |  |  |
| 15 | NUM_EMPREG_OUTROS | NUMBER(8) | Y |  |  |
| 16 | DSC_MOT_SUBST | VARCHAR2(44) | Y |  |  |
| 17 | IND_GIA_ANT_DISQ | CHAR(1) | Y |  |  |
| 18 | DAT_UFESP | DATE | Y |  |  |
| 19 | VLR_UFESP | NUMBER(16,2) | Y |  |  |
| 20 | STATUS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

---

## EST_GNRE_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 6 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 7 | DATA_FISCAL | DATE | N |  |  |
| 8 | MOVTO_E_S | CHAR(1) | N |  |  |
| 9 | NORM_DEV | CHAR(1) | N |  |  |
| 10 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | IND_ENT_SAI | CHAR(1) | Y |  |  |
| 16 | NUM_AUTENTIC_GNRE | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, COD_GNRE, SEQUENCIAL, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

**Indexes**:
- IX_EST_GNRE_DOCFIS_01: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## EST_GNRE_FORNEC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_GNRE | VARCHAR2(7) | N |  |  |
| 6 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 7 | NUM_DOCTO_ORIG | VARCHAR2(20) | Y |  |  |
| 8 | PERIODO_REF | NUMBER(6) | Y |  |  |
| 9 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ATUAL_MONET | NUMBER(17,2) | Y |  |  |
| 11 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TOT_RECOLHER | NUMBER(17,2) | Y |  |  |
| 14 | DAT_VENCTO | DATE | Y |  |  |
| 15 | NUM_CONVENIO | VARCHAR2(50) | Y |  |  |
| 16 | INSC_UF_ORIG | VARCHAR2(18) | Y |  |  |
| 17 | NUM_BANCO | VARCHAR2(3) | Y |  |  |
| 18 | NUM_AGENCIA | VARCHAR2(6) | Y |  |  |
| 19 | NUM_AUTENTIC_GNRE | VARCHAR2(20) | Y |  |  |
| 20 | DAT_RECOLH | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, COD_GNRE, SEQUENCIAL

**FKs**:
- COD_GNRE → ICT_COD_GNRE(COD_GNRE)

---

## EST_GO_GIA_R01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | TOT_REG02 | NUMBER(12) | Y |  |  |
| 6 | TOT_REG03 | NUMBER(12) | Y |  |  |
| 7 | TOT_REG04 | NUMBER(12) | Y |  |  |
| 8 | TOT_REG05 | NUMBER(12) | Y |  |  |
| 9 | TOT_REG06 | NUMBER(12) | Y |  |  |
| 10 | TOT_REG07 | NUMBER(12) | Y |  |  |
| 11 | TOT_TOT_NF | NUMBER(17,2) | Y |  |  |
| 12 | TOT_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | TOT_VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | TOT_VLR_ISENTA | NUMBER(17,2) | Y |  |  |
| 15 | TOT_VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_GO_GIA_R02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 10 | TEL_CLIENTE | VARCHAR2(15) | Y |  |  |
| 11 | NUM_CICLO | VARCHAR2(7) | Y |  |  |
| 12 | DAT_SAIDA | DATE | Y |  |  |
| 13 | DAT_VENCTO | DATE | Y |  |  |
| 14 | COD_USU_FINAL | VARCHAR2(10) | Y |  |  |
| 15 | VLR_TOT_NF | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ISENTA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 20 | SITUACAO | CHAR(1) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA → EST_GO_GIA_R01(COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

**Indexes**:
- IX_FK_SAF_1841: (IDENT_FIS_JUR)

---

## EST_GO_GIA_R03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | NUM_ITEM | NUMBER(5) | N |  |  |
| 10 | IDENT_CFOP | NUMBER(12) | Y |  |  |
| 11 | CLASSE_USUARIO | VARCHAR2(3) | Y |  |  |
| 12 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 13 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 16 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ISENTA | NUMBER(17,2) | Y |  |  |
| 18 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 19 | USUARIO | VARCHAR2(40) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → EST_GO_GIA_R02(COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_CFOP → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## EST_GO_GIA_R05

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | DATA_INICIAL | DATE | Y |  |  |
| 7 | DATA_FINAL | DATE | Y |  |  |
| 8 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISENTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA → EST_GO_GIA_R01(COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## EST_GO_GIA_R06

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | TEL_CLIENTE | VARCHAR2(15) | Y |  |  |
| 7 | COD_USU_FINAL | VARCHAR2(10) | Y |  |  |
| 8 | CID_TEL | VARCHAR2(25) | Y |  |  |
| 9 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 10 | NUM_CICLO | VARCHAR2(7) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA → EST_GO_GIA_R01(COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1846: (IDENT_FIS_JUR)

---

## EST_GO_GIA_R07

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | TEL_CLIENTE | VARCHAR2(15) | N |  |  |
| 6 | COD_SERVICO | VARCHAR2(14) | N |  |  |
| 7 | END_TEL | VARCHAR2(60) | Y |  |  |
| 8 | CID_TEL | VARCHAR2(25) | Y |  |  |
| 9 | LEITURA_INI | NUMBER(6) | Y |  |  |
| 10 | LEITURA_FINAL | NUMBER(6) | Y |  |  |
| 11 | QTD_PULSO | NUMBER(6) | Y |  |  |
| 12 | QTD_CREDITO | NUMBER(6) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, TEL_CLIENTE, COD_SERVICO

---

## EST_GUIA_REC_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 6 | NUM_GUIA | NUMBER(12) | N |  |  |
| 7 | DAT_GUIA | DATE | N |  |  |
| 8 | NUM_SEQ | NUMBER(3) | N |  |  |
| 9 | VLR_IMPOSTO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ACRESC | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DEDUC | NUMBER(17,2) | Y |  |  |
| 15 | VLR_LIQ | NUMBER(17,2) | Y |  |  |
| 16 | DAT_PAGTO | DATE | Y |  |  |
| 17 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO, IDENT_RECEITA_EST, NUM_GUIA, DAT_GUIA, NUM_SEQ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)

---

## EST_ICMS_AMOC_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_ESTADO_ORIG | NUMBER(12) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | VLR_ALIQ_ICMS_ENV | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_ESTADO_ORIG, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## EST_ICMS_PRO_IMPRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | VLR_ALIQ_MED_ICMS | NUMBER(7,4) | Y |  |  |
| 5 | ALIQ_DI_ICMS_RS | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_ISIMP_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PRT_OPER | VARCHAR2(1) | Y |  |  |
| 4 | IND_QTD_MOV | CHAR(1) | Y | 'N' |  |
| 5 | IND_DESCONS_NF_DEV | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_LANCTO_P9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_PAR_LANCTO | VARCHAR2(2) | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | DSC_ITEM_APUR | VARCHAR2(200) | Y |  |  |
| 7 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 8 | VLR_ESTORNO | NUMBER(17,2) | Y |  |  |
| 9 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 10 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 11 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 12 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 13 | IND_TIPO_LANC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_PAR_LANCTO, COD_OPER_APUR

**FKs**:
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_LANCTO_P9_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_PAR_LANCTO | VARCHAR2(2) | N |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 6 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 7 | DATA_FISCAL | DATE | N |  |  |
| 8 | MOVTO_E_S | CHAR(1) | N |  |  |
| 9 | NORM_DEV | CHAR(1) | N |  |  |
| 10 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 17 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 18 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 19 | VLR_ESTORNO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_PAR_LANCTO, COD_OPER_APUR, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## EST_LA_AT_ALIEN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FIM | DATE | N |  |  |
| 4 | NUM_DOC_SAI | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOC_SAI | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOC_SAI | VARCHAR2(2) | N |  |  |
| 7 | DAT_FISCAL_SAI | DATE | N |  |  |
| 8 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 9 | IND_PRODUTO | CHAR(1) | N |  |  |
| 10 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 11 | GRUPO_MEDIDA_SAI | VARCHAR2(9) | Y |  |  |
| 12 | COD_MEDIDA_SAI | VARCHAR2(8) | Y |  |  |
| 13 | QTD_PRD_SAI | NUMBER(17,6) | Y |  |  |
| 14 | VLR_ICMS_SAI | NUMBER(17,2) | Y |  |  |
| 15 | NUM_DOC_EN | VARCHAR2(12) | Y |  |  |
| 16 | SERIE_DOC_EN | VARCHAR2(3) | Y |  |  |
| 17 | SUB_SERIE_DOC_EN | VARCHAR2(2) | Y |  |  |
| 18 | DAT_FISCAL_EN | DATE | Y |  |  |
| 19 | GRUPO_MEDIDA_EN | VARCHAR2(9) | Y |  |  |
| 20 | COD_MEDIDA_EN | VARCHAR2(8) | Y |  |  |
| 21 | QTD_PRD_EN | NUMBER(17,6) | Y |  |  |
| 22 | VLR_ICMS_EN | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_CRED | NUMBER(17,2) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FIM, NUM_DOC_SAI, SERIE_DOC_SAI, SUB_SERIE_DOC_SAI, DAT_FISCAL_SAI, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_LA_VD_DV_UCONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FIM | DATE | N |  |  |
| 4 | NUM_DOC_SAI | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOC_SAI | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOC_SAI | VARCHAR2(2) | N |  |  |
| 7 | DAT_FISCAL_SAI | DATE | N |  |  |
| 8 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 9 | IND_PRODUTO | CHAR(1) | N |  |  |
| 10 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 11 | GRUPO_MEDIDA_SAI | VARCHAR2(9) | Y |  |  |
| 12 | COD_MEDIDA_SAI | VARCHAR2(8) | Y |  |  |
| 13 | QTD_PRD_SAI | NUMBER(17,6) | Y |  |  |
| 14 | VLR_CONTAB_SAI | NUMBER(17,2) | Y |  |  |
| 15 | NUM_DOC_EN | VARCHAR2(12) | Y |  |  |
| 16 | SERIE_DOC_EN | VARCHAR2(3) | Y |  |  |
| 17 | SUB_SERIE_DOC_EN | VARCHAR2(2) | Y |  |  |
| 18 | DAT_FISCAL_EN | DATE | Y |  |  |
| 19 | GRUPO_FIS_JUR_EN | VARCHAR2(9) | Y |  |  |
| 20 | IND_FIS_JUR_EN | CHAR(1) | Y |  |  |
| 21 | COD_FIS_JUR_EN | VARCHAR2(14) | Y |  |  |
| 22 | GRUPO_MEDIDA_EN | VARCHAR2(9) | Y |  |  |
| 23 | COD_MEDIDA_EN | VARCHAR2(8) | Y |  |  |
| 24 | QTD_PRD_EN | NUMBER(17,6) | Y |  |  |
| 25 | VLR_CONTAB_EN | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMS_EN | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ICMS_CRED | NUMBER(17,2) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FIM, NUM_DOC_SAI, SERIE_DOC_SAI, SUB_SERIE_DOC_SAI, DAT_FISCAL_SAI, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_MG_CAE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CAE | VARCHAR2(7) | N |  |  |
| 2 | COD_DESMEMBRAMENTO | VARCHAR2(2) | N |  |  |
| 3 | DESC_CAE | VARCHAR2(100) | Y |  |  |

**PK**: COD_CAE, COD_DESMEMBRAMENTO

---

## EST_MG_CNAE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ATIVIDADE | NUMBER(7) | N |  |  |
| 4 | COD_DESMEMBRAMENTO | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ATIVIDADE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_MG_GIA_CAFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | MES_REF | VARCHAR2(2) | N |  |  |
| 6 | DIA_FIM_REF | VARCHAR2(2) | N |  |  |
| 7 | DIA_INICIO_REF | VARCHAR2(2) | N |  |  |
| 8 | COD_CAMPO | VARCHAR2(3) | N |  |  |
| 9 | VALOR | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INICIO_REF, COD_CAMPO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INICIO_REF → EST_MG_GIA_LIN00(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF)

---

## EST_MG_GIA_DET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LINHA | VARCHAR2(2) | N |  |  |
| 4 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 5 | ANO_REF | VARCHAR2(4) | N |  |  |
| 6 | MES_REF | VARCHAR2(2) | N |  |  |
| 7 | DIA_FIM_REF | VARCHAR2(2) | N |  |  |
| 8 | DIA_INI_REF | VARCHAR2(2) | N |  |  |
| 9 | COD_CAMPO | VARCHAR2(3) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | IND_PROD_RURAL | CHAR(1) | Y |  |  |
| 12 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 13 | DT_EMISSAO | DATE | Y |  |  |
| 14 | DT_FISCAL | DATE | Y |  |  |
| 15 | VALOR | NUMBER(17,2) | Y |  |  |
| 16 | COD_AMPARO_LEGAL | VARCHAR2(10) | N | ' ' |  |
| 17 | JUSTIFICATIVA | VARCHAR2(60) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(13) | Y |  |  |
| 20 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 21 | INSC_EST_REM_DEST | VARCHAR2(14) | N |  |  |
| 22 | SERIE_DOCFIS | VARCHAR2(3) | N | 0 |  |
| 23 | AUTO_INFRACAO | VARCHAR2(13) | N | ' ' |  |
| 24 | MOTIVO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LINHA, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF, COD_CAMPO, NUM_DOCFIS, INSC_EST_REM_DEST, SERIE_DOCFIS, AUTO_INFRACAO, COD_AMPARO_LEGAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF, COD_CAMPO → EST_MG_GIA_LIN10(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF, COD_CAMPO)

---

## EST_MG_GIA_LIN00

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | MES_REF | VARCHAR2(2) | N |  |  |
| 6 | DIA_FIM_REF | VARCHAR2(2) | N |  |  |
| 7 | DIA_INI_REF | VARCHAR2(2) | N |  |  |
| 8 | COD_MOD_DAPI | VARCHAR2(2) | Y |  |  |
| 9 | IND_DAPI_SUBST | CHAR(1) | Y |  |  |
| 10 | COD_CAE | VARCHAR2(7) | Y |  |  |
| 11 | COD_DESMEMBRAMENTO | VARCHAR2(2) | Y |  |  |
| 12 | COD_REGIME | VARCHAR2(2) | Y |  |  |
| 13 | IND_REG_ESP_FISCAL | CHAR(1) | Y |  |  |
| 14 | DT_LIM_PAGTO | DATE | Y |  |  |
| 15 | IND_FUNDESE | CHAR(1) | Y |  |  |
| 16 | VERSAO | VARCHAR2(3) | Y |  |  |
| 17 | TOT_LINHA_20 | NUMBER(3) | Y |  |  |
| 18 | TOT_LINHA_21 | NUMBER(3) | Y |  |  |
| 19 | TOT_LINHA_22 | NUMBER(3) | Y |  |  |
| 20 | TOT_LINHAS | NUMBER(4) | Y |  |  |
| 21 | TOT_CAMPOS_VALOR | NUMBER(17,2) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 25 | IND_CAFE | CHAR(1) | Y |  |  |
| 26 | TOT_LINHA_24 | NUMBER(3) | Y |  |  |
| 27 | TOT_LINHA_27 | NUMBER(3) | Y |  |  |
| 28 | TOT_LINHA_28 | NUMBER(3) | Y |  |  |
| 29 | VLR_INCENT_CULTURA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF

**FKs**:
- COD_REGIME → EST_MG_REG_RECOL(COD_REGIME)

---

## EST_MG_GIA_LIN10

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | MES_REF | VARCHAR2(2) | N |  |  |
| 6 | DIA_FIM_REF | VARCHAR2(2) | N |  |  |
| 7 | DIA_INI_REF | VARCHAR2(2) | N |  |  |
| 8 | COD_CAMPO | VARCHAR2(5) | N |  |  |
| 9 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ICMS_NTRIB | NUMBER(17,2) | Y |  |  |
| 15 | VLR_PARC_CALC_REDUC | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DIFERIDO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF, COD_CAMPO

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF → EST_MG_GIA_LIN00(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF)

---

## EST_MG_GIA_LIN23

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | MES_REF | VARCHAR2(2) | N |  |  |
| 6 | DIA_FIM_REF | VARCHAR2(2) | N |  |  |
| 7 | DIA_INI_REF | VARCHAR2(2) | N |  |  |
| 8 | COD_CAMPO | VARCHAR2(3) | N |  |  |
| 9 | VLR_SALDO_PER_ANT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_INCENTIVO_CULTURA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_DED_INCENTIVO_CULTURA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_LIMITE | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SALDO_CREDOR_PER_SEG | NUMBER(17,2) | Y |  |  |
| 14 | VLR_COMPENSACAO_CREDITO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TOTAL_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 16 | VLR_UTIL_CREDITO_RECEBIDO | NUMBER(17,2) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 20 | ALIQ_DEDUC_INCENT_CULT | NUMBER(7,4) | Y |  |  |
| 21 | VLR_EST_INCENTIVO_CULTURA | NUMBER(17,2) | Y |  |  |
| 22 | VLR_SALDO_PER_ESPORTE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_INCENTIVO_ESPORTE | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TOT_DED_ESPORTE | NUMBER(17,2) | Y |  |  |
| 25 | VLR_LIMITE_ESPORTE | NUMBER(17,2) | Y |  |  |
| 26 | VLR_SALDO_PER_SEG_ESPORTE | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ALIQ_DED_ESPORTE | NUMBER(7,4) | Y |  |  |
| 28 | VLR_EST_SALDO_ESPORTE | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, DIA_FIM_REF, DIA_INI_REF, COD_CAMPO

---

## EST_MG_OPER_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | NUMBER(3) | N |  |  |
| 2 | DT_INI_VIGENCIA | DATE | N |  |  |
| 3 | DT_FIM_VIGENCIA | DATE | Y |  |  |
| 4 | IND_ENT_SAI | CHAR(1) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: COD_OPERACAO, DT_INI_VIGENCIA, IND_ENT_SAI, COD_CFO

---

## EST_MG_OPER_CFO_NOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | NUMBER(3) | N |  |  |
| 2 | DT_INI_VIGENCIA | DATE | N |  |  |
| 3 | DT_FIM_VIGENCIA | DATE | Y |  |  |
| 4 | IND_ENT_SAI | CHAR(1) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_OPERACAO, DT_INI_VIGENCIA, IND_ENT_SAI, COD_CFO, COD_NATUREZA_OP

---

## EST_MG_OUT_ENT_CALC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | EXERCICIO | VARCHAR2(4) | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | PERC_PARTICIPACAO | NUMBER(5,2) | Y |  |  |
| 7 | VLR_PARTICIPACAO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, EXERCICIO, IDENT_ESTADO, COD_MUNICIPIO

---

## EST_MG_OUT_ENT_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | EXERCICIO | NUMBER(4) | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | VALOR_OPER | NUMBER(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, EXERCICIO, IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_MG_REG_RECOL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_REGIME | VARCHAR2(2) | N |  |  |
| 2 | DESC_REGIME | VARCHAR2(50) | Y |  |  |
| 3 | PERCENTUAL | NUMBER(7,3) | Y |  |  |

**PK**: COD_REGIME

---

## EST_MG_REL_DEMONST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | ANO_REF | VARCHAR2(4) | N |  |  |
| 5 | MES_REF | VARCHAR2(2) | N |  |  |
| 6 | TIPO_OPERACAO | CHAR(1) | N |  |  |
| 7 | COD_OPERACAO | NUMBER(3) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IND_OPERACAO | CHAR(1) | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS_NTRIB | NUMBER(17,2) | Y |  |  |
| 19 | VLR_PARC_CALC_REDUC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_DIFERIDO | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, ANO_REF, MES_REF, TIPO_OPERACAO, COD_OPERACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## EST_MM_COTEPE_INIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 4 | COD_TECNICO | VARCHAR2(2) | Y |  |  |
| 5 | IND_TIPO_ESCRITURACAO | CHAR(1) | Y |  | G - Diario Geral; A - Diario Auxiliar |
| 6 | IND_ORIGEM_INVENTARIO | CHAR(1) | Y |  | P - Produto; N - NCM |
| 7 | NUM_CPF_CONTRIBUINTE | VARCHAR2(11) | Y |  | CPF do representante do estabelecimento, informado no reg 0000 |
| 8 | IND_ICMS_RETIDO | CHAR(1) | Y |  |  |
| 9 | IND_DATA_LIMITE | NUMBER(2) | Y |  | 1 - 1 mes; 2 - 2 meses; 3 - 3 meses; 4 - 4 meses; 5 - 5 meses; 6 - 6 meses; 12 - 1 ano |
| 10 | IND_VLR_DIF_ALIQ | CHAR(1) | Y |  | Indicador para escolha se o valor do diferencial de aliquota sera recuperado a partir da apuracao ou dos documentos fiscais |
| 11 | IND_GERA_ECF_SAFX991 | CHAR(1) | Y |  |  |
| 12 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  |  |
| 13 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 14 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 15 | IND_ALINHA_COD_NCM | CHAR(1) | Y |  |  |
| 16 | IND_DESC_IND_PROD | CHAR(1) | Y | 'N' |  |
| 17 | IND_DESC_IND_PESSOA | CHAR(1) | Y | 'N' |  |
| 18 | QTDE_MESES_ANT_DTFISC | NUMBER(2) | Y | 1 |  |
| 19 | IND_VAL_FECP | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CONTADOR → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_TECNICO → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_MOV_CONSIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | TIPO_OPERACAO | CHAR(1) | N |  |  |
| 5 | DT_OPERACAO | DATE | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | NUM_ITEM | NUMBER(5) | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 12 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 14 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 15 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 16 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 19 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ISENTO_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 23 | ALIQ_TRIBUTO_IPI | NUMBER(7,4) | Y |  |  |
| 24 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ISENTO_IPI | NUMBER(17,2) | Y |  |  |
| 26 | VLR_OUTROS_IPI | NUMBER(17,2) | Y |  |  |
| 27 | COD_NCM | VARCHAR2(10) | Y |  |  |
| 28 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 29 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 30 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 31 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 32 | USUARIO | VARCHAR2(40) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 34 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 35 | IDENT_DOCFIS | NUMBER(12) | Y |  |  |
| 36 | IDENT_ITEM_MERC | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, TIPO_OPERACAO, DT_OPERACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_SAF_1353: (IDENT_FIS_JUR)

---

## EST_MOV_CTRL_FECH

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FECH | DATE | N |  |  |
| 4 | IND_STATUS | CHAR(1) | Y |  |  |
| 5 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FECH

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_MOV_CTRL_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CTRL_OPER | VARCHAR2(3) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | DATA_FISCAL | DATE | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_BASE1 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 17 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 18 | VLR_IPI_BASE1 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 20 | IDENT_NCM | NUMBER(12) | Y |  |  |
| 21 | QUANTIDADE | NUMBER(18,6) | Y |  |  |
| 22 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 23 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 24 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 25 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  |  |
| 26 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  |  |
| 27 | SSERIE_DOCFIS_RET | VARCHAR2(2) | Y |  |  |
| 28 | DATA_DOCFIS_RET | DATE | Y |  |  |
| 29 | DATA_RET | DATE | Y |  |  |
| 30 | VLR_CONTAB_RET | NUMBER(17,2) | Y |  |  |
| 31 | VLR_TRIB_ICMS_RET | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMS_BASE1_RET | NUMBER(17,2) | Y |  |  |
| 33 | VLR_ALIQ_ICMS_RET | NUMBER(7,4) | Y |  |  |
| 34 | VLR_TRIB_IPI_RET | NUMBER(17,2) | Y |  |  |
| 35 | VLR_IPI_BASE1_RET | NUMBER(17,2) | Y |  |  |
| 36 | VLR_ALIQ_IPI_RET | NUMBER(7,4) | Y |  |  |
| 37 | QUANTIDADE_RET | NUMBER(18,6) | Y |  |  |
| 38 | VLR_MAT_APLIC | NUMBER(17,2) | Y |  |  |
| 39 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 40 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 41 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 42 | USUARIO | VARCHAR2(40) | Y |  |  |
| 43 | VLR_QTD_AJUSTE | NUMBER(17,2) | Y |  |  |
| 44 | PRAZO_PRORROG | NUMBER(5) | Y |  |  |
| 45 | DSC_MOTIVO | VARCHAR2(50) | Y |  |  |
| 46 | IND_GER | CHAR(1) | Y |  |  |
| 47 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 48 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 49 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 50 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 51 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 52 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CTRL_OPER, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_FISCAL, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CTRL_OPER → EST_CTRL_OPER(COD_CTRL_OPER)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NCM → X2043_COD_NBM(IDENT_NBM)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)

**Indexes**:
- IX_FK_SAF_1065: (IDENT_FIS_JUR)

---

## EST_MOV_CTRL_RET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CTRL_OPER | VARCHAR2(3) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS_RET | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS_RET | VARCHAR2(3) | N |  |  |
| 9 | SSERIE_DOCFIS_RET | VARCHAR2(2) | N |  |  |
| 10 | DATA_FISCAL | DATE | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | DATA_DOCFIS_RET | DATE | Y |  |  |
| 13 | DATA_RET | DATE | Y |  |  |
| 14 | VLR_CONTAB_RET | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIB_ICMS_RET | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_BASE1_RET | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ALIQ_ICMS_RET | NUMBER(7,4) | Y |  |  |
| 18 | VLR_TRIB_IPI_RET | NUMBER(17,2) | Y |  |  |
| 19 | VLR_IPI_BASE1_RET | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ALIQ_IPI_RET | NUMBER(7,4) | Y |  |  |
| 21 | QUANTIDADE_RET | NUMBER(18,6) | Y |  |  |
| 22 | VLR_MAT_APLIC_RET | NUMBER(17,2) | Y |  |  |
| 23 | VLR_SERVICO_RET | NUMBER(17,2) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 27 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 28 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 29 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 30 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 31 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 32 | IDENT_CFO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CTRL_OPER, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS_RET, SERIE_DOCFIS_RET, SSERIE_DOCFIS_RET, DATA_FISCAL, IDENT_PRODUTO

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## EST_MS_GIA_R00

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA_INI | NUMBER(2) | N |  |  |
| 5 | MES_REFERENCIA_FIM | NUMBER(2) | N |  |  |
| 6 | IND_TIPO_GIA | VARCHAR2(1) | N |  |  |
| 7 | IND_TIPO_GIA_SUBSTITUTA | VARCHAR2(1) | Y |  |  |
| 8 | ANO_SUBST | NUMBER(4) | Y |  |  |
| 9 | MES_SUBST_INI | NUMBER(2) | Y |  |  |
| 10 | MES_SUBST_FIM | NUMBER(2) | Y |  |  |
| 11 | IND_TIPO_GIA_SUBST | VARCHAR2(1) | Y |  |  |
| 12 | IND_FORMA_ENTREGA | VARCHAR2(1) | Y |  |  |
| 13 | ANO_MUDANCA | NUMBER(4) | Y |  |  |
| 14 | MES_MUDANCA | NUMBER(2) | Y |  |  |
| 15 | IND_JUSTIFICATIVA | VARCHAR2(1) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA_INI, MES_REFERENCIA_FIM, IND_TIPO_GIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_MS_GIA_R01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 7 | VLR_CARGA_TRIB_LIQ | NUMBER(17,2) | N |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, COD_CFO, COD_ESTADO, VLR_CARGA_TRIB_LIQ

---

## EST_MS_GIA_R02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | VLR_DEB_IMPOSTO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_DEB_OUTROS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CRED_BC_CP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_ESTORNO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SUB_TOTAL_DB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_IMPOSTO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SALDO_CRED_ANT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CRED_OUTROS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DEB_ESTORNO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SUB_TOTAL_CR | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SALDO_DEVEDOR | NUMBER(17,2) | Y |  |  |
| 16 | VLR_SALDO_CREDOR | NUMBER(17,2) | Y |  |  |
| 17 | VLR_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 18 | VLR_IMP_RECOLHER | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CRED_TRANSP | NUMBER(17,2) | Y |  |  |
| 20 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

---

## EST_MS_GIA_R03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SALDO_CR_ANT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEVOLUCOES | NUMBER(17,2) | Y |  |  |
| 9 | VLR_IMP_RECOLHER | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SALDO_CR_TR | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CRED_OUTROS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMSS_TR | NUMBER(17,2) | Y |  |  |
| 13 | VLR_IMP_DEV_TR | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

---

## EST_MS_GIA_R04

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | VLR_ALIQ_X | NUMBER(7,4) | Y |  |  |
| 6 | VLR_ALIQ_Y | NUMBER(7,4) | Y |  |  |
| 7 | VLR_BASE_X | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_Y | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TRIB_X | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIB_Y | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

---

## EST_MS_GIA_R05

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | VLR_ICMS_1_INI | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_2_INI | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS_3_INI | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMSS_INI | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_1_FIM | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_2_FIM | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_3_FIM | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMSS_FIM | NUMBER(17,2) | Y |  |  |
| 13 | COD_JUS_ICMS_1_INI | VARCHAR2(30) | Y |  |  |
| 14 | COD_JUS_ICMS_2_INI | VARCHAR2(30) | Y |  |  |
| 15 | COD_JUS_ICMS_3_INI | VARCHAR2(30) | Y |  |  |
| 16 | COD_JUS_ICMSS_INI | VARCHAR2(30) | Y |  |  |
| 17 | COD_JUS_ICMS_1_FIM | VARCHAR2(30) | Y |  |  |
| 18 | COD_JUS_ICMS_2_FIM | VARCHAR2(30) | Y |  |  |
| 19 | COD_JUS_ICMS_3_FIM | VARCHAR2(30) | Y |  |  |
| 20 | COD_JUS_ICMSS_FIM | VARCHAR2(30) | Y |  |  |
| 21 | DSC_JUS_ICMS_1_INI | VARCHAR2(30) | Y |  |  |
| 22 | DSC_JUS_ICMS_2_INI | VARCHAR2(30) | Y |  |  |
| 23 | DSC_JUS_ICMS_3_INI | VARCHAR2(30) | Y |  |  |
| 24 | DSC_JUS_ICMSS_INI | VARCHAR2(30) | Y |  |  |
| 25 | DSC_JUS_ICMS_1_FIM | VARCHAR2(30) | Y |  |  |
| 26 | DSC_JUS_ICMS_2_FIM | VARCHAR2(30) | Y |  |  |
| 27 | DSC_JUS_ICMS_3_FIM | VARCHAR2(30) | Y |  |  |
| 28 | DSC_JUS_ICMSS_FIM | VARCHAR2(30) | Y |  |  |
| 29 | USUARIO | VARCHAR2(40) | Y |  |  |
| 30 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 31 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

---

## EST_MS_GIA_R08

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | QTD_FUNCIONARIO | NUMBER(7) | Y |  |  |
| 6 | VLR_DESP_FOLHA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ENC_TRAB | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

---

## EST_MS_GIA_R09

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | Y |  |  |
| 5 | DAT_BALANCO | DATE | Y |  |  |
| 6 | VLR_CIRC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DISP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CONT_REC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_EST_MERC | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTR_EST | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTR_ATIVO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_REAL_LPRAZO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CONT_REC_LPRAZO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_OUTR_CONT_REAL | NUMBER(17,2) | Y |  |  |
| 15 | VLR_PERMANENTE | NUMBER(17,2) | Y |  |  |
| 16 | VLR_INVEST | NUMBER(17,2) | Y |  |  |
| 17 | VLR_IMOB_LIQ | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DIRERIDO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOT_GERAL_AT | NUMBER(17,2) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA

---

## EST_MS_GIA_R10

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | VLR_CIRC | NUMBER(17,2) | Y |  |  |
| 6 | VLR_FORNEC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_EMPR_FINANC | NUMBER(17,2) | Y |  |  |
| 8 | VLR_OUTR_ATIVO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_EXIG_LPRAZO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_RES_EXERC_FUT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_PATR_LIQ | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CAPIT_SOCIAL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_OUTR_PATR_LIQ | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOT_GERAL_PASS | NUMBER(17,2) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

---

## EST_MS_GIA_R11

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | VLR_RECEITA_BRUTA | NUMBER(17,2) | Y |  |  |
| 6 | VLR_DEV_ABAT_IMP | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RECEITA_LIQ | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CUSTO_MERC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_LUCRO_BRUTO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DESP_OPER | NUMBER(17,2) | Y |  |  |
| 11 | VLR_LUC_PRE_OPER | NUMBER(17,2) | Y |  |  |
| 12 | VLR_RECEITA_NOPER | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DESPESA_NOPER | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SALDO_CORR_MON | NUMBER(17,2) | Y |  |  |
| 15 | VLR_RES_ANTES_IR | NUMBER(17,2) | Y |  |  |
| 16 | VLR_PROVISAO_IR | NUMBER(17,2) | Y |  |  |
| 17 | VLR_RES_APOS_IR | NUMBER(17,2) | Y |  |  |
| 18 | VLR_PARTIC_CONTR | NUMBER(17,2) | Y |  |  |
| 19 | VLR_LUC_PRE | NUMBER(17,2) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

---

## EST_MS_GIA_R13

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_SALDO_CRED_ANT | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SALDO_CRED_PRO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SALDO_CRED_REC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_DEBITO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_IMP_REC_PRO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_IMP_REC_REC | NUMBER(17,2) | Y |  |  |
| 12 | VLR_SALDO_CRE_TRA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_IMP_RECOLHER | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA

---

## EST_MS_GIA_R15

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | IND_E_S | CHAR(1) | N |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 7 | VLR_PETROLEO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ENERGIA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, IND_E_S, COD_ESTADO

---

## EST_MS_GIA_R51

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | COD_CLASSE_OFICIAL | VARCHAR2(2) | N |  |  |
| 6 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, COD_CLASSE_OFICIAL

---

## EST_MS_GIA_R52

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | COD_CLASSE_OFICIAL | VARCHAR2(2) | N |  |  |
| 6 | NUM_CERTIFICADO | VARCHAR2(40) | N |  |  |
| 7 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, COD_CLASSE_OFICIAL, NUM_CERTIFICADO

---

## EST_MUNIC_N_AMOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_OPER_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | COD_OPERACAO | VARCHAR2(2) | N |  |  |
| 3 | DSC_OPERACAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_OPERACAO, COD_UF_OBRIG

---

## EST_PAR_CONSIG_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | DT_INI_VALIDADE | DATE | N |  |  |
| 3 | DT_FIM_VALIDADE | DATE | Y |  |  |

**PK**: IDENT_ESTADO, DT_INI_VALIDADE

---

## EST_PAR_CONV_GNRE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N | 'CON' |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | DIA_VENCTO | NUMBER(2) | Y |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N | 0 |  |
| 7 | COD_GNRE | VARCHAR2(7) | N | ' ' |  |
| 8 | COD_PRODUTO | VARCHAR2(2) | Y |  |  |
| 9 | NRO_BANCO | VARCHAR2(3) | Y |  |  |
| 10 | NRO_AGENCIA | VARCHAR2(6) | Y |  |  |
| 11 | IND_PERIODO | CHAR(1) | Y |  | 1- Mensal 2- Quinzenal 3- Decendial 4- SemanaL 5- Diária |
| 12 | IND_CRITERIO | CHAR(1) | Y |  | 1- Dias úteis 2- Dias corridos (antecipar quando vencimento não cair em dia útil) 3- Dias corridos (postergar quando vencimento não cair em dia útil) 4- Dias fixos (antecipar quando vencimento não cair em dia útil) 5- Dias fixos (postergar quando vencimento não cair em dia útil)  |
| 13 | NUM_DIAS | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, IDENT_ESTADO, COD_GNRE

**FKs**:
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PAR_CPRES_PAUTA
**Comment**: Tabela de Cadastro da Pauta de Preco MInimo de Frete - Lancamentos Automaticos ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TARIFA | VARCHAR2(3) | N |  |  |
| 2 | VALID_TARIFA | DATE | N |  |  |
| 3 | NUM_DISTANCIA_INI | NUMBER(4) | N |  |  |
| 4 | NUM_DISTANCIA_FIM | NUMBER(4) | N |  |  |
| 5 | VLR_CARGA_COMUM | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CARGA_MUDANCA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CARGA_FRIGOR | NUMBER(17,2) | Y |  |  |

**PK**: COD_TARIFA, VALID_TARIFA

**Indexes**:
- IX_EST_PAR_CPRES_PAUTA: (NUM_DISTANCIA_INI, NUM_DISTANCIA_FIM, VALID_TARIFA)

---

## EST_PAR_CTRL_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CTRL_OPER | VARCHAR2(3) | N |  |  |
| 4 | IND_ICMS_DESTAC_E | CHAR(1) | Y |  |  |
| 5 | IND_ICMS_DESTAC_S | CHAR(1) | Y |  |  |
| 6 | IND_IPI_DESC_E | CHAR(1) | Y |  |  |
| 7 | IND_IPI_DESC_S | CHAR(1) | Y |  |  |
| 8 | PRAZO_INCID_ICMS | NUMBER(3) | Y |  |  |
| 9 | PRAZO_INCID_IPI | NUMBER(3) | Y |  |  |
| 10 | IND_TP_OPER_ORIG | CHAR(1) | Y |  |  |
| 11 | IND_DATA_LIMITE | CHAR(1) | Y | 'N' |  |
| 12 | DATA_LIMITE | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CTRL_OPER

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CTRL_OPER → EST_CTRL_OPER(COD_CTRL_OPER)

---

## EST_PAR_DADOS_ACS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_ICMSS_OUTRAS | CHAR(1) | Y |  |  |
| 4 | IND_MUNIC_COD_DSC | CHAR(1) | Y |  |  |
| 5 | IND_ESTOQ_PRD_NBM | CHAR(1) | Y |  |  |
| 6 | IND_UF_PFJ_NF | CHAR(1) | Y |  |  |
| 7 | IND_C_FINAL_CFO_NF | CHAR(1) | Y |  |  |
| 8 | IND_MODELO_CIAP | CHAR(1) | Y |  |  |
| 9 | IND_MUNIC_PONTO_CONS | CHAR(1) | Y |  |  |
| 10 | IND_CONSID_NF_SERV | CHAR(1) | Y |  |  |
| 11 | IND_DESCONTO | VARCHAR2(1) | Y |  |  |
| 12 | IND_FECEP_ST | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PAR_DIPAMB_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_DIPAM_B | NUMBER(2) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | IND_TRIBUTADO | CHAR(1) | Y |  |  |
| 6 | IND_CALCULO | CHAR(1) | Y |  |  |
| 7 | IND_LANCA_NF_ESCRIT | VARCHAR2(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_DIPAM_B, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_DIPAM_B → EST_SP_DIPAM_B(COD_DIPAM)

---

## EST_PAR_DIPAMB_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_DIPAM_B | NUMBER(2) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 7 | IND_TRIBUTADO | CHAR(1) | Y |  |  |
| 8 | IND_CALCULO | CHAR(1) | Y |  |  |
| 9 | IND_LANCA_NF_ESCRIT | VARCHAR2(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_DIPAM_B, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_DIPAM_B → EST_SP_DIPAM_B(COD_DIPAM)

---

## EST_PAR_GER_C176

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_OPER_APUR_CRED | VARCHAR2(5) | Y |  |  |
| 4 | DSC_LANC_CRED | VARCHAR2(150) | Y |  |  |
| 5 | COD_CLASSE_CRED | VARCHAR2(3) | Y |  |  |
| 6 | COD_AMP_LEGAL_CRED | VARCHAR2(10) | Y |  |  |
| 7 | COD_SUB_OCORR_CRED | VARCHAR2(2) | Y |  |  |
| 8 | COD_AJUSTE_ICMS_CRED | VARCHAR2(8) | Y |  |  |
| 9 | COD_OPER_APUR_EST | VARCHAR2(5) | Y |  |  |
| 10 | DSC_LANC_EST | VARCHAR2(150) | Y |  |  |
| 11 | COD_CLASSE_EST | VARCHAR2(3) | Y |  |  |
| 12 | COD_AMP_LEGAL_EST | VARCHAR2(10) | Y |  |  |
| 13 | COD_SUB_OCORR_EST | VARCHAR2(2) | Y |  |  |
| 14 | COD_AJUSTE_ICMS_EST | VARCHAR2(8) | Y |  |  |
| 15 | IDENT_ESTADO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## EST_PAR_LANCTO_P9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PAR_LANCTO | VARCHAR2(2) | N |  |  |
| 2 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 3 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 4 | DSC_PAR_LANCTO | VARCHAR2(50) | Y |  |  |
| 5 | DSC_ITEM_APUR | VARCHAR2(200) | Y |  |  |
| 6 | COD_OPER_APUR_1 | VARCHAR2(5) | Y |  |  |
| 7 | DSC_ITEM_APUR_1 | VARCHAR2(200) | Y |  |  |
| 8 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 9 | COD_CLASSE_1 | VARCHAR2(3) | Y |  |  |
| 10 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 11 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 12 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 13 | COD_AMPARO_LEGAL_1 | VARCHAR2(10) | Y |  |  |
| 14 | COD_SUB_IT_OCORR_1 | VARCHAR2(2) | Y |  |  |
| 15 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg E111/E220) -                              referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |
| 16 | COD_AJUSTE_ICMS_1 | VARCHAR2(8) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg E111/E220) -                              referente aos Códigos de Ajustes de ICT_AJUSTE_ICMS |
| 17 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 18 | COD_AJUSTE_SPED_1 | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 19 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 20 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 21 | COD_OBSERVACAO | VARCHAR2(9) | Y |  |  |

**PK**: COD_PAR_LANCTO, COD_TIPO_LIVRO

**FKs**:
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_TIPO_LIVRO, COD_OPER_APUR_1 → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_1 → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_SPED_1 → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## EST_PAR_MT_CLASSE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 2 | IND_DETALHAMENTO | CHAR(1) | N |  |  |
| 3 | COD_TIPO_DET | NUMBER(4) | Y |  |  |

**PK**: COD_CLASSE, IND_DETALHAMENTO

**FKs**:
- COD_CLASSE → PRT_CLASSE_MSAF(COD_CLASSE)

---

## EST_PAR_REL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 2 | COD_REL | VARCHAR2(10) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | DSC_REL | VARCHAR2(50) | Y |  |  |

**PK**: CLASSE_REL, COD_REL

---

## EST_PAR_REL_ALEGAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, IDENT_ESTADO, COD_AMPARO_LEGAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)

---

## EST_PAR_REL_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)

---

## EST_PAR_REL_CONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 6 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)

---

## EST_PAR_REL_EXTCFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 7 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 8 | DAT_INICIO | DATE | Y |  |  |
| 9 | DAT_FIM | DATE | Y |  |  |
| 10 | PERC_RECUPERADO | NUMBER(7,3) | Y |  |  |
| 11 | NUM_PARCELAS | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)

---

## EST_PAR_REL_FISJUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DISTANCIA_REAL | NUMBER(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_0740: (IDENT_FIS_JUR)

---

## EST_PAR_REL_NBM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | COD_NBM | VARCHAR2(10) | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | DAT_INICIO | DATE | Y |  |  |
| 8 | DAT_FIM | DATE | Y |  |  |
| 9 | PERC_RECUPERACAO | NUMBER(7,3) | Y |  |  |
| 10 | NUM_PARCELAS | NUMBER(2) | Y |  |  |
| 11 | IND_VENDA | VARCHAR2(2) | Y |  |  |
| 12 | IND_ATEND_PROTOCOLO | CHAR(1) | Y |  |  |
| 13 | IND_CARGA | CHAR(1) | Y |  |  |
| 14 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 15 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, COD_NBM, IDENT_ESTADO

---

## EST_PAR_REL_NBM_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | Y |  |  |
| 4 | COD_REL | VARCHAR2(10) | Y |  |  |
| 5 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 7 | DAT_INICIO | DATE | Y |  |  |
| 8 | DAT_FIM | DATE | Y |  |  |
| 9 | PERC_RECUPERACAO | NUMBER(7,3) | Y |  |  |
| 10 | NUM_PARCELAS | NUMBER(2) | Y |  |  |
| 11 | IND_VENDA | VARCHAR2(2) | Y |  |  |
| 12 | IND_ATEND_PROTOCOLO | CHAR(1) | Y |  |  |

---

## EST_PAR_REL_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 6 | COD_OPERACAO | VARCHAR2(9) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, GRUPO_OPERACAO, COD_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PAR_REL_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DAT_INICIO | DATE | Y |  |  |
| 9 | DAT_FIM | DATE | Y |  |  |
| 10 | PERC_RECUPERACAO | NUMBER(7,3) | Y |  |  |
| 11 | NUM_PARCELAS | NUMBER(2) | Y |  |  |
| 12 | IND_CARGA | CHAR(1) | Y |  |  |
| 13 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 14 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)

---

## EST_PAR_REL_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CLASSE_REL | VARCHAR2(3) | N |  |  |
| 4 | COD_REL | VARCHAR2(10) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CLASSE_REL, COD_REL, IDENT_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- CLASSE_REL, COD_REL → EST_PAR_REL(CLASSE_REL, COD_REL)

---

## EST_PAR_RES_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_TOTALIZ | NUMBER(2) | N |  |  |
| 3 | IDENT_CFO_INIC | NUMBER(12) | Y |  |  |
| 4 | IDENT_CFO_FINAL | NUMBER(12) | Y |  |  |
| 5 | DSC_OPERACAO | VARCHAR2(18) | Y |  |  |

**PK**: IDENT_ESTADO, COD_TOTALIZ

**FKs**:
- IDENT_CFO_INIC → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_CFO_FINAL → X2012_COD_FISCAL(IDENT_CFO)

---

## EST_PAR_RET_DET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_DET_OPERACAO | NUMBER(12) | N |  |  |
| 4 | PERC_REDUCAO_A_DEB | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_DET_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → EST_PAR_RET_TRANSP(COD_EMPRESA, COD_ESTAB)
- IDENT_DET_OPERACAO → DETALHE_OPERACAO(IDENT_DET_OPERACAO)

---

## EST_PAR_RET_TRANSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_APUR_A_CRED | CHAR(1) | Y |  |  |
| 4 | IND_APUR_A_DEB | CHAR(1) | Y |  |  |
| 5 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 6 | FATOR_CALC | NUMBER(9,4) | Y |  |  |
| 7 | IND_BASE_CALC | CHAR(1) | Y |  |  |
| 8 | IND_TIPO_PAR_UTLZ | CHAR(1) | Y |  |  |
| 9 | IND_ALIQ_UTIL | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PAR_SERV_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | IND_SERV | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PAR_SERV_NAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 5 | IND_SERV | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PAR_SISIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PERFIL | VARCHAR2(2) | N |  |  |
| 4 | DSC_PERFIL | VARCHAR2(50) | Y |  |  |
| 5 | IND_REG_10 | CHAR(1) | Y |  |  |
| 6 | IND_REG_20 | CHAR(1) | Y |  |  |
| 7 | IND_REG_21 | CHAR(1) | Y |  |  |
| 8 | IND_REG_30 | CHAR(1) | Y |  |  |
| 9 | IND_REG_31 | CHAR(1) | Y |  |  |
| 10 | IND_REG_32 | CHAR(1) | Y |  |  |
| 11 | IND_REG_34 | CHAR(1) | Y |  |  |
| 12 | IND_REG_36 | CHAR(1) | Y |  |  |
| 13 | IND_REG_37 | CHAR(1) | Y |  |  |
| 14 | IND_REG_38 | CHAR(1) | Y |  |  |
| 15 | IND_REG_40 | CHAR(1) | Y |  |  |
| 16 | IND_REG_41 | CHAR(1) | Y |  |  |
| 17 | IND_REG_42 | CHAR(1) | Y |  |  |
| 18 | IND_REG_50 | CHAR(1) | Y |  |  |
| 19 | IND_REG_51 | CHAR(1) | Y |  |  |
| 20 | IND_REG_60 | CHAR(1) | Y |  |  |
| 21 | IND_REG_62 | CHAR(1) | Y |  |  |
| 22 | IND_REG_67 | CHAR(1) | Y |  |  |
| 23 | IND_REG_66 | CHAR(1) | Y |  |  |
| 24 | IND_REG_69 | CHAR(1) | Y |  |  |
| 25 | IND_REG_70 | CHAR(1) | Y |  |  |
| 26 | IND_REG_72 | CHAR(1) | Y |  |  |
| 27 | IND_REG_76 | CHAR(1) | Y |  |  |
| 28 | IND_REG_77 | CHAR(1) | Y |  |  |
| 29 | IND_REG_80 | CHAR(1) | Y |  |  |
| 30 | IND_REG_APUR | CHAR(1) | Y |  |  |
| 31 | IND_REG_43 | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PERFIL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PA_DIEF_ESTAB
**Comment**: Cadastro dos Dados do Contribuinte - atendimento a DIEF-PA (versão 2005)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VALID_INI | DATE | N |  |  |
| 4 | IND_TP_TRIBUTACAO | CHAR(1) | Y |  |  1 - lucro presumido, 3 - lucro real |
| 5 | IND_TP_ESCRITURACAO | CHAR(1) | Y |  | 1 - caixa, 2 - escrituracao contabil |
| 6 | IND_SERVICO_ICMS | CHAR(1) | Y |  | 1 - sim, 2 - nao |
| 7 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 8 | IND_ESCRIT_ESTQ_MES | CHAR(1) | Y |  | 1 - SIM; 2 - NÃO |

**PK**: COD_EMPRESA, COD_ESTAB, VALID_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CONTADOR → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_PA_DIEF_REG_ANUAL
**Comment**: Manutenção dos Dados Anuais - atendimento a DIEF-PA (versão 2005)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | VLR_DESP_PROLABORE | NUMBER(17,2) | Y |  |  |
| 6 | VLR_DESP_SALARIO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DESP_ENCARGO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DESP_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_DESP_OUTR_IMP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DESP_FRETE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DESP_ENERGIA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DESP_ALUGUEL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DESP_FINANC | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DESP_OUTRAS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ESTOQ_INI_VEND_ANT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ESTOQ_INI_CONS_ANT | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ESTOQ_INI_TERC_ANT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ESTOQ_FIM_VEND_ANT | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ESTOQ_FIM_CONS_ANT | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ESTOQ_FIM_TERC_ANT | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ESTOQ_INI_VEND_ATU | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ESTOQ_INI_CONS_ATU | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ESTOQ_INI_TERC_ATU | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ESTOQ_FIM_VEND_ATU | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ESTOQ_FIM_CONS_ATU | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ESTOQ_FIM_TERC_ATU | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PB_GIM_DET01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 6 | IND_NORMAL_RET | CHAR(1) | N |  |  |
| 7 | VLR_CRED_ENT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_ATIV_IMOB | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 10 | ICMS_ANT_RECOL | NUMBER(17,2) | Y |  |  |
| 11 | ICMS_ANT_ARECOL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CRED_OUTROS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CREDOR_MES_ANT | NUMBER(17,2) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, COD_DETALHE, IND_NORMAL_RET

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PB_GIM_DET02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 6 | IND_NORMAL_RET | CHAR(1) | N |  |  |
| 7 | VLR_DEB_SAIDA | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TRANSF_CRED | NUMBER(17,2) | Y |  |  |
| 9 | VLR_DEB_OUTROS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 11 | ICMS_ST_ENT_RECOL | NUMBER(17,2) | Y |  |  |
| 12 | ICMS_ST_ENT_ARECOL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ST_SAI_RECOL | NUMBER(17,2) | Y |  |  |
| 14 | ICMS_ST_SAI_RECOL | NUMBER(17,2) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, COD_DETALHE, IND_NORMAL_RET

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PB_GIM_DET03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 6 | IND_NORMAL_RET | CHAR(1) | N |  |  |
| 7 | IND_NATUR_TRANSF | CHAR(1) | N |  |  |
| 8 | VLR_TRANSF | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 13 | INSC_EST_ORIGEM | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, COD_DETALHE, IND_NORMAL_RET, IND_NATUR_TRANSF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PB_GIM_DET04

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 6 | IND_NORMAL_RET | CHAR(1) | N |  |  |
| 7 | ICMS_DFALIQ_ARECOL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_IMP_OUTRAS_UF | NUMBER(17,2) | Y |  |  |
| 9 | EMAIL_CONTRIB | VARCHAR2(40) | Y |  |  |
| 10 | DAT_INI_ATIV_EMPR | DATE | Y |  |  |
| 11 | VERSAO_PGM | VARCHAR2(4) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 15 | IND_REG_PAGTO | CHAR(1) | Y | '1' |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, COD_DETALHE, IND_NORMAL_RET

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PB_GIM_DET05

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 6 | IND_NORMAL_RET | CHAR(1) | N |  |  |
| 7 | NUM_CPF_CGC | VARCHAR2(14) | Y |  |  |
| 8 | NUM_CRC | VARCHAR2(10) | Y |  |  |
| 9 | NOME_CONTADOR | VARCHAR2(40) | Y |  |  |
| 10 | TEL_CONTADOR | VARCHAR2(12) | Y |  |  |
| 11 | EMAIL_CONTADOR | VARCHAR2(40) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 15 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, COD_DETALHE, IND_NORMAL_RET

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_CONTADOR(COD_RESPONSAVEL)

---

## EST_PB_GIM_DET06

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 6 | IND_NORMAL_RET | CHAR(1) | N |  |  |
| 7 | VLR_ESTOQUE_TRIB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ESTOQUE_NTRIB | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ESTOQUE_ICMSST | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SALDO_CAIXA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SALDO_BCO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DESP_PESSOAL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_IMP_OUTROS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DESP_GERAIS | NUMBER(17,2) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, COD_DETALHE, IND_NORMAL_RET

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PB_GIM_DET15
**Comment**: GIM PB - registro 88 detalhe 15 - Crédito Presumido

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 6 | IND_NORMAL_RET | CHAR(1) | N |  |  |
| 7 | VLR_CPRES_OUTROS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CPRES_TARE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CPRES_RICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CPRES_FAIN | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 14 | VLR_CPRES_HABIT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CPRES_EDUC | NUMBER(17,2) | Y |  |  |
| 16 | VLR_CPRES_GPLACA | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CPRES_FIC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, COD_DETALHE, IND_NORMAL_RET

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PB_GIM_DET16
**Comment**: GIM PB - registro 88 detalhe 16 - Deduções FUNCEP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | COD_DETALHE | VARCHAR2(2) | N |  |  |
| 6 | IND_NORMAL_RET | CHAR(1) | N |  |  |
| 7 | VLR_FUNCEP_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_FUNCEP_ICMSS_SAI | NUMBER(17,2) | Y |  |  |
| 9 | VLR_FUNCEP_ICMSS_ENT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_FUNCEP_FONTE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_FUNCEP_DIFALIQ | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, COD_DETALHE, IND_NORMAL_RET

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PB_GIM_DET29

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | COD_MUNICIPIO | NUMBER(10) | N |  |  |
| 7 | VLR_ADICIONADO | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, IDENT_ESTADO, COD_MUNICIPIO

---

## EST_PB_GIM_DET30

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | VARCHAR2(4) | N |  |  |
| 4 | MES_REF | VARCHAR2(2) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | NUMERO_RECIBO | VARCHAR2(32) | Y |  |  |
| 7 | IND_SITUACAO | CHAR(1) | Y |  |  |
| 8 | DATA_SITUACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, IDENT_ESTADO

---

## EST_PB_GIM_UF_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 3 | DAT_INI_VIGENCIA | DATE | N |  |  |
| 4 | DAT_FIM_VIGENCIA | DATE | Y |  |  |

**PK**: COD_ESTADO, COD_CFOP, DAT_INI_VIGENCIA

---

## EST_PE_GIA_DETCDEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 8 | VLR_RECEITA | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM, IDENT_RECEITA_EST

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## EST_PE_GIA_DET_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | COD_CFO | VARCHAR2(4) | N |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_DET_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 8 | SERIE_EQUIPAMENTO | VARCHAR2(15) | Y |  |  |
| 9 | VLR_GT | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM, COD_EQUIPAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)
- COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO → X2099_EQUIPAMENTO(COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO)

---

## EST_PE_GIA_DET_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 8 | DAT_VENCIMENTO | DATE | N |  |  |
| 9 | IND_FLAG_QUAD | CHAR(1) | Y |  |  |
| 10 | VLR_RECOLH | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM, IDENT_RECEITA_EST, DAT_VENCIMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## EST_PE_GIA_INF_GER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | IND_SUBSTITUTA | CHAR(1) | Y |  |  |
| 8 | IND_MOVIMENTO | CHAR(1) | Y |  |  |
| 9 | NOM_INCENTIVO | VARCHAR2(10) | Y |  |  |
| 10 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 11 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONTADOR → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_PE_GIA_QUADRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | IND_ENT_SAI | CHAR(1) | N |  |  |
| 8 | IND_TP_TOTAL | CHAR(1) | N |  |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM, IND_ENT_SAI, IND_TP_TOTAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_QUADR_C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 8 | COD_OPER | CHAR(1) | N |  |  |
| 9 | IND_ENT_SAI | CHAR(1) | N |  |  |
| 10 | DSC_MUNIC | VARCHAR2(50) | Y |  |  |
| 11 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM, COD_MUNICIPIO, COD_OPER, IND_ENT_SAI

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_QUADR_D

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | DAT_BALANCO | DATE | Y |  |  |
| 8 | VLR_ESTOQ_INI | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ESTOQ_FIM | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ESTOQ_INI_NT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ESTOQ_FIM_NT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ESTOQ_DIF | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ESTOQ_DIF_NT | NUMBER(17,2) | Y |  |  |
| 14 | NUM_EMPREGADO | NUMBER(11) | Y |  |  |
| 15 | QTD_CONS_ENERGIA | NUMBER(11) | Y |  |  |
| 16 | VLR_DISPONIB | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CLIENTE | NUMBER(17,2) | Y |  |  |
| 18 | VLR_FORNECEDOR | NUMBER(17,2) | Y |  |  |
| 19 | VLR_EMPR_FINANC | NUMBER(17,2) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_QUADR_E

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_ICMS_FONT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_ICMSS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTROS_CRED | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SALDO_DEV | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOTAL_CRED | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DEDUCAO_INV | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DEDUCAO_OUT | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS_RECOLHER | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DEB_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_OUTROS_DEB | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ESTORNO_CRED | NUMBER(17,2) | Y |  |  |
| 21 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 22 | VLR_TOTAL_DEB | NUMBER(17,2) | Y |  |  |
| 23 | VLR_CRED_PRESUM | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TRANSF_CRED_E | NUMBER(17,2) | Y |  |  |
| 25 | VLR_RESTITUI_ICMS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_OUTR_HIP_CRED | NUMBER(17,2) | Y |  |  |
| 27 | VLR_TRANSF_CRED_S | NUMBER(17,2) | Y |  |  |
| 28 | VLR_OUTR_HIP_DEB | NUMBER(17,2) | Y |  |  |
| 29 | VLR_COMPENS_DEB | NUMBER(17,2) | Y |  |  |
| 30 | VLR_BENS_ATIVO | NUMBER(17,2) | Y |  |  |
| 31 | VLR_OUTR_HIP_EST | NUMBER(17,2) | Y |  |  |
| 32 | USUARIO | VARCHAR2(40) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 34 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_QUADR_F

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | VLR_SALDO_CRED_ANT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SALDO_CRED_ATU | NUMBER(17,2) | Y |  |  |
| 9 | VLR_IMP_CRED_ENT_D | NUMBER(17,2) | Y |  |  |
| 10 | VLR_IMP_CRED_ENT_F | NUMBER(17,2) | Y |  |  |
| 11 | VLR_IMP_CRED_SAI_D | NUMBER(17,2) | Y |  |  |
| 12 | VLR_IMP_CRED_SAI_F | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ABAT_DIVIDA | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_QUADR_G

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | VLR_ENTRADA | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SAIDA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ESTORNO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ESTORNO_ISENTA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ESTORNO_SAIDA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TOT_ESTORNO | NUMBER(17,2) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_QUADR_H

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | VLR_ICMS_MERC_IMP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_NORMAL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMSS_OUT_UF | NUMBER(17,2) | Y |  |  |
| 10 | VLR_PARC_NINCENT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SALDO_INCENT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PARC_MUNIC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_PARC_INCENT | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOT_OUTR_RECOL | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SAIDA_C_LIB | NUMBER(17,2) | Y |  |  |
| 16 | VLR_SAIDA_S_LIB | NUMBER(17,2) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_QUADR_I

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 6 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 7 | IND_ORIGEM | CHAR(1) | N |  |  |
| 8 | VLR_ENERGIA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_COMUNICACAO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTR_USO_CONS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ATIVO_FIXO | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM, IND_ORIGEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM → EST_PE_GIA_INF_GER(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, SERIE_GIAM, SUB_SERIE_GIAM)

---

## EST_PE_GIA_QUAD_C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | COD_OPER | CHAR(1) | N |  |  |
| 7 | DSC_MUNIC | VARCHAR2(50) | Y |  |  |
| 8 | IND_ENT_SAI | CHAR(1) | Y |  |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_MUNICIPIO, COD_OPER

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_PROD_NAT_ESTOQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_NATUR_ESTOQ | VARCHAR2(2) | N |  |  |

**PK**: COD_UF_OBRIG, IND_PRODUTO, COD_NATUR_ESTOQ

---

## EST_PRT_CFO_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | IND_ICMS | CHAR(1) | N |  |  |
| 3 | COD_CFOP | VARCHAR2(4) | N |  |  |

**PK**: COD_UF_OBRIG, IND_ICMS, COD_CFOP

---

## EST_PR_DFC_Q19

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_BASE | NUMBER(4) | N |  |  |
| 4 | VLR_CONTABIL | NUMBER(15) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_BASE

---

## EST_PR_GIA_R1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | IND_TIPO_GIA | NUMBER(2) | Y |  |  |
| 6 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 7 | VLR_ESTOQUE | NUMBER(17,2) | Y |  |  |
| 8 | NUM_FUNCIONARIO | NUMBER(5) | Y |  |  |
| 9 | VLR_FOLHA_PAGTO | NUMBER(17,2) | Y |  |  |
| 10 | NUM_REG_TIPO2 | NUMBER(2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

---

## EST_PR_GIA_R2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | NUM_LINHA | NUMBER(4) | N |  |  |
| 6 | VLR_LINHA | NUMBER(17,2) | Y |  |  |
| 7 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, NUM_LINHA

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → EST_PR_GIA_R1(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_REGUL_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | IND_E_S | CHAR(1) | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | COD_REGTO_ICMS | VARCHAR2(2) | N |  |  |
| 5 | COD_CFOP | VARCHAR2(4) | N |  |  |

**PK**: COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS, COD_CFOP

**FKs**:
- COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS → EST_REGUL_ICMS(COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS)

---

## EST_REGUL_CFO_NOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | IND_E_S | CHAR(1) | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | COD_REGTO_ICMS | VARCHAR2(2) | N |  |  |
| 5 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 6 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 7 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS, COD_CFOP, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS, COD_CFOP → EST_REGUL_CFO(COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS, COD_CFOP)

---

## EST_REGUL_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | IND_E_S | CHAR(1) | N |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 4 | COD_REGTO_ICMS | VARCHAR2(2) | N |  |  |
| 5 | DSC_REGTO_ICMS | VARCHAR2(100) | Y |  |  |

**PK**: COD_UF_OBRIG, IND_E_S, COD_ESTADO, COD_REGTO_ICMS

---

## EST_RES_ALIQ_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | VLR_ALIQ | NUMBER(7,3) | N |  |  |
| 5 | IND_E_S | CHAR(1) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, VLR_ALIQ, IND_E_S

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RES_AMP_LEGAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 8 | VLR_BASE1 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE3 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO, COD_TRIBUTO, IDENT_ESTADO, COD_AMPARO_LEGAL

---

## EST_RES_AP_ICMS_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | VLR_DEB_SAIDA | NUMBER(17,2) | Y |  |  |
| 5 | VLR_DEB_OUTROS | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CRED_ESTORNO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SUB_TOTAL_DB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_ENTRADAS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_OUTROS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DEB_ESTORNO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SUB_TOTAL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_SALDO_CREDOR | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SUB_TOTAL_CR | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SALDO_DEVEDOR | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 16 | VLR_IMP_RECOLHER | NUMBER(17,2) | Y |  |  |
| 17 | VLR_PROX_PER_SAL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DEB_TRANSF | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 20 | VLR_DEB_DALIQ_AP | NUMBER(17,2) | Y |  |  |
| 21 | VLR_DEB_DALIQ_MC | NUMBER(17,2) | Y |  |  |
| 22 | VLR_CRED_DALIQ_AP | NUMBER(17,2) | Y |  |  |
| 23 | VLR_CRED_DALIQ_MC | NUMBER(17,2) | Y |  |  |
| 24 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMSS_PER_ANT | NUMBER(17,2) | Y |  |  |
| 27 | VLR_CRED_ICMSS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RES_CFO_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_CFO | NUMBER(12) | N |  |  |
| 5 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS_SNT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 13 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CONTAB_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CONTAB_ICMSS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## EST_RES_CFO_ALI_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_CFO | NUMBER(12) | N |  |  |
| 5 | VLR_ALIQ | NUMBER(7,3) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS_SNT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_CFO, VLR_ALIQ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## EST_RES_CFO_UF_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | IDENT_CFO | NUMBER(12) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS_SNT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_S_NAPROPR | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CONTABIL_NC | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ICMS_NC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS_S_PET | NUMBER(17,2) | Y |  |  |
| 18 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 19 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_OUTR_IMPOSTOS | NUMBER(17,2) | Y |  | Campo calculado de acordo com o indicador de IPI incluso: Se indicador de IPI incluso marcado e Vlr. Contábil menor que Soma das bases, Outros Impostos será a soma do Vlr.IPI e IPI não destacado; Caso contrário, se o Valor Contábil for igual ao somatório das bases, "Outros Impostos" será zero. Para o caso em que flag de IPI Incluso não estiver marcado, mantemos a regra estudada na OS 2353 |
| 21 | VLR_ICMS_NC | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ICMS_ST_AP | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_S_AP | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS_S_SP | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMS_S_PET_SP | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMS_S_SUBSTITUTO | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ICMS_S_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 28 | VLR_IPI_DEV | NUMBER(17,2) | Y |  |  |
| 29 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 30 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ICMS_S_NAPROPR_PET | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMS_S_SUBSTITUTO_PET | NUMBER(17,2) | Y |  |  |
| 33 | VLR_ICMS_S_SUBSTITUIDO_PET | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ICMS_MONO | NUMBER(17,2) | Y |  |  |
| 35 | VLR_ICMS_S_MONO | NUMBER(17,2) | Y |  |  |
| 36 | VLR_BASE_OUTRAS_MONO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## EST_RES_CFO_UF_AL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | IDENT_CFO | NUMBER(12) | N |  |  |
| 6 | VLR_ALIQ | NUMBER(7) | N |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS_SNT | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_S_NAPROPR | NUMBER(17,2) | Y |  |  |
| 16 | VLR_CONTABIL_NC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ICMS_NC | NUMBER(17,2) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, IDENT_CFO, VLR_ALIQ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## EST_RES_COMPL_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | COMPL_CFO | VARCHAR2(2) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ICMS1 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS3 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ST_NCRED | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_RETIDO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DIF_ALIQ | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO, COMPL_CFO

---

## EST_RES_ESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | VLR_ESTOQ | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CUSTO_ESTOQ | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ESTOQ_NT | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CUSTO_ESTOQ_NT | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, GRUPO_CONTAGEM, IND_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RES_ESTOQUE_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | VLR_ESTOQ | NUMBER(17,2) | Y |  |  |
| 5 | VLR_CUSTO_ESTOQ | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ESTOQ_NT | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CUSTO_ESTOQ_NT | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RES_EXTCFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS1 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS2 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS3 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ST_NCRED | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_RETIDO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMSS_NCRED | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## EST_RES_EXTCFO_MUN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_CFO | NUMBER(12) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 8 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS1 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS2 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS3 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ST_NCRED | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_RETIDO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS_PET | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS_OUT | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CONTABIL_NC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_CONTABIL_C | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_ICMS_NC | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ICMS_C | NUMBER(17,2) | Y |  |  |
| 23 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y | 0 |  |
| 24 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y | 0 |  |
| 25 | VLR_TRIB_IPI | NUMBER(17,2) | Y | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, IDENT_ESTADO, COD_MUNICIPIO

---

## EST_RES_EXTCFO_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_CFO | NUMBER(12) | N |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS1 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS2 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS3 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ST_NCRED | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_RETIDO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_PET | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS_OUT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CONTABIL_C | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CONTABIL_NC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_ICMS_C | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_ICMS_NC | NUMBER(17,2) | Y |  |  |
| 22 | VLR_TRIB_IPI | NUMBER(17,2) | Y |  | Criada para atender o chamado 29308 |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, IDENT_ESTADO

---

## EST_RES_IMPORT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 5 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | DATA_EMISSAO | DATE | Y |  |  |
| 10 | IDENT_CFO | NUMBER(12) | N |  |  |
| 11 | DATA_DI | DATE | Y |  |  |
| 12 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 13 | VLR_CONTAB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_PG | NUMBER(17,2) | Y |  |  |
| 17 | DAT_PAGTO | DATE | Y |  |  |
| 18 | NUM_CONTROLE | VARCHAR2(15) | Y |  |  |
| 19 | NUM_GUIA_IMP | VARCHAR2(15) | Y |  |  |
| 20 | ORG_RECOLH | VARCHAR2(50) | Y |  |  |
| 21 | DAT_ENTREGA | DATE | Y |  |  |
| 22 | LOC_ENTREGA | VARCHAR2(100) | Y |  |  |
| 23 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_DOCTO, IDENT_FIS_JUR, DATA_FISCAL, IDENT_CFO

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)

**Indexes**:
- IX_FK_SAF_1051: (IDENT_FIS_JUR)

---

## EST_RES_MUNIC_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | DSC_MUNICIPIO | VARCHAR2(50) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS_SNT | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 15 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 16 | IND_TP_GER_MUNIC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, DSC_MUNICIPIO, IND_E_S

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RES_MUNIC_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | IND_E_S | VARCHAR2(1) | N |  |  |
| 7 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 8 | IND_PRODUTO | CHAR(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 10 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ISEN_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_OUTR_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, COD_ESTADO, COD_MUNICIPIO, IND_E_S, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## EST_RES_MUN_AGRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | DSC_MUNICIPIO | VARCHAR2(50) | N |  |  |
| 6 | IND_E_S | CHAR(1) | N |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS_SNT | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 15 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 16 | IND_TP_GER_MUNIC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, DSC_MUNICIPIO, IND_E_S

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RES_PAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | COD_PAIS | VARCHAR2(3) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 12 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 13 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO, COD_PAIS

---

## EST_RES_REGIAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_REGIAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ICMS1 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ICMS3 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ST_NCRED | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_RETIDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_REGIAO, COD_CFO

---

## EST_RES_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | IND_E_S | CHAR(1) | N |  |  |
| 6 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 7 | COD_PARAM | NUMBER(3) | N |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, IND_E_S, COD_MUNICIPIO, COD_PARAM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PARAM → PRT_PAR2_MSAF(COD_PARAM)

---

## EST_RES_SER_CFO_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | SERIE_GIAM | VARCHAR2(1) | N |  |  |
| 5 | SUB_SERIE_GIAM | VARCHAR2(2) | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | IDENT_CFO | NUMBER(12) | N |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_ICMS_SNT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_S_NAPROPR | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 18 | BASE_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 19 | BASE_ISENTA_IPI | NUMBER(17,2) | Y |  |  |
| 20 | BASE_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, SERIE_GIAM, SUB_SERIE_GIAM, IDENT_ESTADO, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## EST_RES_UF_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | IND_E_S | CHAR(1) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ICMS_SNT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_PET | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_OUT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_CONTABIL_C | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CONTABIL_NC | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS_C | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_ICMS_NC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS_PETROLEO | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_ENERGIA | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_OUTRAS_C | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_OUTRAS_NC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC, IDENT_ESTADO, IND_E_S

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RJ_DECLAN_COD
**Comment**: Tabela dos Codigos Especificos da Declan

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_CODIGO | CHAR(1) | N |  | Indica o tipo de codigo: 1-Ajustes do Valor Adicionado, 2-Distribuicao do Valor Adicionado |
| 2 | CODIGO | NUMBER(5) | N |  | Codigo especifico utilizado na obrigacao |
| 3 | DESCRICAO | VARCHAR2(120) | Y |  |  |
| 4 | DETALHE | CHAR(1) | Y |  | Indica o tipo de ajuste do valor adicionado: 1-Entrada,2-Saida,3-Estoque,4-Outros |

**PK**: TIPO_CODIGO, CODIGO

---

## EST_RJ_DECLAN_COD_MODELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_CODIGO | CHAR(1) | N |  |  |
| 2 | CODIGO | NUMBER(5) | N |  |  |
| 3 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  |  |

**PK**: TIPO_CODIGO, CODIGO, GRUPO_MODELO, COD_MODELO

**FKs**:
- TIPO_CODIGO, CODIGO → EST_RJ_DECLAN_COD(TIPO_CODIGO, CODIGO)

---

## EST_RJ_DECLAN_PAR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | TIPO_OPERACAO_1 | CHAR(1) | Y |  |  |
| 5 | TIPO_OPERACAO_2 | CHAR(1) | Y |  |  |
| 6 | TIPO_ATIVIDADE_1 | CHAR(1) | Y |  |  |
| 7 | TIPO_ATIVIDADE_2 | CHAR(1) | Y |  |  |
| 8 | SITUACAO_ESP_1 | CHAR(1) | Y |  |  |
| 9 | SITUACAO_ESP_2 | CHAR(1) | Y |  |  |
| 10 | SITUACAO_ESP_3 | CHAR(1) | Y |  |  |
| 11 | ESTAB_UNICO_PRINC | CHAR(1) | Y |  |  |
| 12 | COD_REPRESENTANTE | VARCHAR2(2) | Y |  |  |
| 13 | COD_CONTABILISTA | VARCHAR2(2) | Y |  |  |
| 14 | TIPO_APUR_ESTOQUE | CHAR(1) | Y |  | Indica como os valores do estoque serao apurados: 1-Manual, 2-Calculado |
| 15 | IND_EMPR_SEM_MOV | CHAR(1) | Y |  | Indicador de Receita Bruta da Empresa sem movto no período (Quadro G): S-Sem movto, N-Com movto |
| 16 | TIPO_APUR_IPI_MP | CHAR(1) | Y |  | Indica como os valores do IPI serao apurados: 1-Manual, 2-Calculado. |
| 17 | TIPO_APUR_IPI_INTEGRA_ICMS | CHAR(1) | Y |  | Indica como os valores do IPI serao apurados: 1-Manual, 2-Calculado. |
| 18 | TIPO_APUR_IPI_NINTEGRA_ICMS | CHAR(1) | Y |  | Indica como os valores do IPI serao apurados: 1-Manual, 2-Calculado. |
| 19 | TIPO_APUR_IMPORTACAO | CHAR(1) | Y |  | Indica como os valores do IPI serao apurados: 1-Manual, 2-Calculado. |
| 20 | IND_ESTAB_UNICO_NAC | CHAR(1) | Y |  |  |
| 21 | IND_ESTAB_SEM_MOV | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_REPRESENTANTE → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONTABILISTA → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_RJ_DECLAN_QDE
**Comment**: Tabela dos Quadros D e E da Declan

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | TIPO_CODIGO | CHAR(1) | N |  | Indica o tipo de codigo: 1-Ajustes do Valor Adicionado, 2-Distribuicao do Valor Adicionado |
| 5 | CODIGO | NUMBER(5) | N |  | Codigo especifico utilizado na obrigacao |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | COD_MUNICIPIO | NUMBER(5) | N |  | Codigo IBGE do Municipio do RJ (usado somente para o tipo codigo = 2, para tipo 1, sera sempre = 0) |
| 8 | VALOR | NUMBER(17,2) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | NUM_PROC | VARCHAR2(18) | Y |  |  |
| 12 | DSC_LOCAL_DISTRIB | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, TIPO_CODIGO, CODIGO, IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- TIPO_CODIGO, CODIGO → EST_RJ_DECLAN_COD(TIPO_CODIGO, CODIGO)

---

## EST_RJ_DECLAN_QFG
**Comment**: Tabela dos Quadros F e G da Declan

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | QUADRO | CHAR(1) | N |  | Indicador do quadro: 1-Quadro F (Receita Bruta Estabelecimento), 2-Quadro G (Rec Bruta Empresa) |
| 5 | VLR_REC_APUR_01 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_REC_APUR_02 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_REC_APUR_03 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_REC_APUR_04 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_REC_APUR_05 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_REC_APUR_06 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_REC_APUR_07 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_REC_APUR_08 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_REC_APUR_09 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_REC_APUR_10 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_REC_APUR_11 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_REC_APUR_12 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_REC_DIG_01 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_REC_DIG_02 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_REC_DIG_03 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_REC_DIG_04 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_REC_DIG_05 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_REC_DIG_06 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_REC_DIG_07 | NUMBER(17,2) | Y |  |  |
| 24 | VLR_REC_DIG_08 | NUMBER(17,2) | Y |  |  |
| 25 | VLR_REC_DIG_09 | NUMBER(17,2) | Y |  |  |
| 26 | VLR_REC_DIG_10 | NUMBER(17,2) | Y |  |  |
| 27 | VLR_REC_DIG_11 | NUMBER(17,2) | Y |  |  |
| 28 | VLR_REC_DIG_12 | NUMBER(17,2) | Y |  |  |
| 29 | VLR_VENDAS_ST_01 | NUMBER(17,2) | Y |  |  |
| 30 | VLR_VENDAS_ST_02 | NUMBER(17,2) | Y |  |  |
| 31 | VLR_VENDAS_ST_03 | NUMBER(17,2) | Y |  |  |
| 32 | VLR_VENDAS_ST_04 | NUMBER(17,2) | Y |  |  |
| 33 | VLR_VENDAS_ST_05 | NUMBER(17,2) | Y |  |  |
| 34 | VLR_VENDAS_ST_06 | NUMBER(17,2) | Y |  |  |
| 35 | VLR_VENDAS_ST_07 | NUMBER(17,2) | Y |  |  |
| 36 | VLR_VENDAS_ST_08 | NUMBER(17,2) | Y |  |  |
| 37 | VLR_VENDAS_ST_09 | NUMBER(17,2) | Y |  |  |
| 38 | VLR_VENDAS_ST_10 | NUMBER(17,2) | Y |  |  |
| 39 | VLR_VENDAS_ST_11 | NUMBER(17,2) | Y |  |  |
| 40 | VLR_VENDAS_ST_12 | NUMBER(17,2) | Y |  |  |
| 41 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 42 | VLR_REC_DED_01 | NUMBER(17,2) | Y |  |  |
| 43 | VLR_REC_DED_02 | NUMBER(17,2) | Y |  |  |
| 44 | VLR_REC_DED_03 | NUMBER(17,2) | Y |  |  |
| 45 | VLR_REC_DED_04 | NUMBER(17,2) | Y |  |  |
| 46 | VLR_REC_DED_05 | NUMBER(17,2) | Y |  |  |
| 47 | VLR_REC_DED_06 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_REC_DED_07 | NUMBER(17,2) | Y |  |  |
| 49 | VLR_REC_DED_08 | NUMBER(17,2) | Y |  |  |
| 50 | VLR_REC_DED_09 | NUMBER(17,2) | Y |  |  |
| 51 | VLR_REC_DED_10 | NUMBER(17,2) | Y |  |  |
| 52 | VLR_REC_DED_11 | NUMBER(17,2) | Y |  |  |
| 53 | VLR_REC_DED_12 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, QUADRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RJ_GIA_R0110

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | DSC_OBS | VARCHAR2(2000) | Y |  |  |
| 6 | DSC_OBS_ST | VARCHAR2(2000) | Y |  |  |
| 7 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SALDO_ANT_ST | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SALDO_ANT_SCE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_ENER_SCE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_EST_PROV_SCE | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PROV_SCE | NUMBER(17,2) | Y |  |  |
| 13 | IND_SEM_MOV_PROP | CHAR(1) | Y |  |  |
| 14 | IND_SEM_MOV_ST | CHAR(1) | Y |  |  |
| 15 | IND_SEM_MOV_OUTRO | CHAR(1) | Y |  |  |
| 16 | IND_SEM_MOV_ZFM | CHAR(1) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R0123

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | IND_E_S | CHAR(1) | Y |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ST | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

**Indexes**:
- IX_EST_RJ_GIAR0123: (COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, IND_E_S)

---

## EST_RJ_GIA_R01_S03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_SALDO_DEV | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_OUTRAS_SAI | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_RECOLH | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SALDO_CRED | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_FINAL | NUMBER(17,2) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R01_S04

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | DSC_OBSERVACAO | VARCHAR2(2000) | Y |  |  |
| 6 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R01_S12

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | IND_SUBTIPO_REG | NUMBER(1) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTROS_CRE_DEB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ESTORNO_CRE_DEB | NUMBER(17,2) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, IND_SUBTIPO_REG

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R0210

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ISENTA_OUTRAS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_ST_PET | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_ST_OUT | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R0220

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 6 | VLR_CONTABIL_NC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CONTABIL_C | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_NC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_C | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ISENTA_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R0230

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | COD_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 11 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PARC_REDUZ | NUMBER(17,2) | Y |  |  |
| 13 | COD_MUNICIPIO_DEST | NUMBER(8) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R0240

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | DADO_COMPL1 | VARCHAR2(100) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | VLR_COMPENSADO | NUMBER(17,2) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_AMPARO_LEGAL, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R0250

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | DADO_COMPL1 | VARCHAR2(100) | Y |  |  |
| 7 | VLR_COMPENSADO | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_SEQUENCIAL | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_AMPARO_LEGAL, NUM_SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R0260

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | DADO_COMPL1 | VARCHAR2(100) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | NUM_PROCESSO_GIA | NUMBER(20) | Y |  |  |
| 12 | ANO_PROCESSO_GIA | NUMBER(4) | Y |  |  |
| 13 | VLR_RECEBIDO | NUMBER(17,2) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_AMPARO_LEGAL, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R0270

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | COD_AMPLEGAL_DEST | VARCHAR2(10) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | DADO_COMPL1 | VARCHAR2(100) | Y |  |  |
| 9 | DADO_COMPL1_DEST | VARCHAR2(100) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 13 | NUM_PROCESSO_GIA | NUMBER(20) | Y |  |  |
| 14 | ANO_PROCESSO_GIA | NUMBER(4) | Y |  |  |
| 15 | VLR_TRANSFERIDO | NUMBER(17,2) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_AMPARO_LEGAL, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

---

## EST_RJ_GIA_R02_03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | IND_TIPO_REG | NUMBER(1) | Y |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

**Indexes**:
- IX_EST_RJ_R02_03: (COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, IND_TIPO_REG)

---

## EST_RJ_GIA_R04_08

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | COD_SUB_ITEM_OCOR | VARCHAR2(2) | N |  |  |
| 7 | IND_TIPO_REG | NUMBER(1) | N |  |  |
| 8 | VLR_DEB_CRED_DEDUC | NUMBER(17,2) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCOR, IND_TIPO_REG

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

**Indexes**:
- IX_EST_RJ_R04_08: (COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, IND_TIPO_REG)

---

## EST_RJ_GIA_R140_2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | COD_SUB_ITEM_OCOR | VARCHAR2(2) | N |  |  |
| 7 | IND_TIPO_REG | VARCHAR2(4) | Y |  |  |
| 8 | DADO_COMPL1 | VARCHAR2(120) | Y |  |  |
| 9 | DADO_COMPL2 | VARCHAR2(120) | Y |  |  |
| 10 | DADO_COMPL3 | VARCHAR2(120) | Y |  |  |
| 11 | DADO_COMPL4 | VARCHAR2(120) | Y |  |  |
| 12 | DADO_COMPL5 | VARCHAR2(120) | Y |  |  |
| 13 | DESCR_COMPL | VARCHAR2(150) | Y |  |  |
| 14 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | NUM_SEQUENCIAL | NUMBER(12) | N | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCOR, NUM_SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO → ESP_RJ_GIA_APUR(COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO)

**Indexes**:
- IX_ESTRJ_GIAR140_2: (COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, IND_TIPO_REG)

---

## EST_RN_INF_FISCAL
**Comment**: Tabela do módulo Informativo Fiscal - RN. Armazena os dados demonstrados nos relatórios dos Modelos I e II.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | IND_MODELO | CHAR(1) | N |  | Dominio: 1 - modelo I; 2 -  modelo II |
| 6 | SEQ_LINHA | NUMBER(2) | N |  | Sequencial por modelo, que identifica a linha do relatório. Ex: Modelo I Linha 01 - seq_linha = 1; Linha 1.1 - seq_linha = 2; Linha 1.2 - seq_linha = 3 |
| 7 | DSC_LINHA | VARCHAR2(100) | Y |  | descrição da linha apresentada no relatório. Ex Modelo I Linha 01 - dsc_linha = 01. Estoque Inicial de Mercadorias |
| 8 | VLR_LINHA | NUMBER(17,2) | Y |  | valor da linha apresentado no relatório |
| 9 | DSC_GRUPO | VARCHAR2(50) | Y |  | descrição do grupo de linhas apresentado no relatório. Ex: ENTRADAS, SAIDAS, VALOR ADICIONADO, OUTRAS INFORMAÇÕES |
| 10 | NUM_NIVEL | NUMBER(1) | Y |  | representa a hierarquia que as linhas são apresentadas no relatório. Domino: 1, 2, 3. Ex: Modelo II Linha 01 - num_nivel = 1; Linha 1.1 - num_nivel = 2; Linha 1.1.1 - num_nivel = 3 |
| 11 | IND_PREENCHIMENTO | CHAR(1) | Y |  | indica a forma de preenchimento do valor. Dominio: G - gerado; D - digitado via manutenção, N - nem gerado, nem digitado (linha sem valor). |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, IND_MODELO, SEQ_LINHA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_RO_INF_CLASSE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | INF_COMPLEMENTAR | VARCHAR2(2) | N |  |  |
| 2 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 3 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 4 | COD_RECEITA | VARCHAR2(4) | Y |  |  |

**PK**: INF_COMPLEMENTAR, COD_OPER_APUR, COD_CLASSE

---

## EST_RO_REC_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_OPER | CHAR(1) | N |  |  |
| 4 | COD_RECEITA | VARCHAR2(4) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | Y |  |  |

---

## EST_RO_REG_TIPO9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | VLR_CMP_01 | NUMBER(17,2) | Y |  |  |
| 5 | VLR_CMP_02 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CMP_03 | NUMBER(17,2) | Y |  |  |
| 7 | COD_RECEITA | VARCHAR2(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

---

## EST_RO_REG_TIPO90

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | GUIA_LANCAMENTO | NUMBER(14) | N |  |  |
| 5 | PARCELA | VARCHAR2(2) | Y |  |  |
| 6 | COD_RECEITA | VARCHAR2(4) | Y |  |  |
| 7 | IND_RETIFIC | CHAR(1) | Y |  |  |
| 8 | VLR_CREDITO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, GUIA_LANCAMENTO

---

## EST_RR_GIM_INFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | IND_SUBSTITUTA | VARCHAR2(1) | Y |  |  |
| 6 | DDD | VARCHAR2(5) | Y |  |  |
| 7 | TELEFONE | VARCHAR2(10) | Y |  |  |
| 8 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 9 | DSC_LOCAL_DATA | VARCHAR2(50) | Y |  |  |
| 10 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

---

## EST_RR_GIM_QUADRO_F

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | NUM_LINHA | NUMBER(1) | N |  |  |
| 6 | DSC_LINHA | VARCHAR2(20) | Y |  |  |
| 7 | COD_LINHA | VARCHAR2(4) | Y |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CREDITOS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, NUM_LINHA

---

## EST_RR_GIM_QUADRO_G

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | NUM_LINHA | NUMBER(1) | N |  |  |
| 6 | DSC_CREDITOS | VARCHAR2(35) | Y |  |  |
| 7 | VLR_CREDITOS | NUMBER(17,2) | Y |  |  |
| 8 | DSC_DEBITOS | VARCHAR2(35) | Y |  |  |
| 9 | VLR_DEBITOS | NUMBER(17,2) | Y |  |  |
| 10 | COD_LINHA | VARCHAR2(2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, NUM_LINHA

---

## EST_RR_GIM_QUADRO_H

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | NUM_LINHA | NUMBER(1) | N |  |  |
| 6 | DSC_RECEITA | VARCHAR2(25) | Y |  |  |
| 7 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 8 | VLR_RECEITA | NUMBER(17,2) | Y |  |  |
| 9 | COD_LINHA | VARCHAR2(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, NUM_LINHA

---

## EST_RR_GIM_QUADRO_I_J

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | NUM_LINHA | NUMBER(1) | N |  |  |
| 6 | IND_QUADRO | VARCHAR2(1) | N |  |  |
| 7 | DSC_COLUNA | VARCHAR2(20) | Y |  |  |
| 8 | VLR_COLUNA | NUMBER(17,2) | Y |  |  |
| 9 | COD_LINHA | VARCHAR2(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, NUM_LINHA, IND_QUADRO

---

## EST_RS_GIA_ANEXO1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CREDITOS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | VLR_EXCLUIDAS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO10

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | PERIODO_APUR_PAGTO | NUMBER(4) | N |  |  |
| 6 | DATA_VENCTO | DATE | N |  |  |
| 7 | VLR_ICMS_RECOLHER | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMSS_RECOLHER | NUMBER(17,2) | Y |  |  |
| 9 | INSC_EST_CENTRAL | VARCHAR2(14) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | VLR_ICMS_AMP | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ST_AMP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, PERIODO_APUR_PAGTO, DATA_VENCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO11

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 6 | VLR_ENTRADAS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SAIDAS | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO12

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_PAIS_RS | VARCHAR2(3) | N |  |  |
| 6 | VLR_ENTRADAS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SAIDAS | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_PAIS_RS

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO14

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_AMP_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | DSC_ANEXO | VARCHAR2(60) | N |  |  |
| 7 | VLR_OUT_CRED | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_AMP_LEGAL, DSC_ANEXO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO15

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_AMP_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | DSC_ANEXO | VARCHAR2(60) | N |  |  |
| 7 | VLR_OUT_DEB | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_AMP_LEGAL, DSC_ANEXO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO16

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 7 | COD_NATUREZA | VARCHAR2(2) | N |  | Dominio: 01 - Transporte, 02 - Energia Eletrica Distribuicao, 03 - Comunicacao, 04- Agua, 05 - Vendas fora do Estabelecimento, 06 - Energia Eletrica Geracao, 09 - Regime Especial. |
| 8 | NUM_ATO_DECL | VARCHAR2(8) | N |  |  |
| 9 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CUSTO | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, IDENT_ESTADO, COD_MUNICIPIO, COD_NATUREZA, NUM_ATO_DECL

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_RS_GIA_ANEXO1C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | COD_AJUSTE | VARCHAR2(3) | N |  |  |
| 7 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 8 | DSC_ESPECIF | VARCHAR2(60) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO, COD_AJUSTE

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO → EST_RS_GIA_ANEXO1(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO)

---

## EST_RS_GIA_ANEXO2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | INSC_EST_REMETENTE | VARCHAR2(14) | N |  |  |
| 6 | COD_AMP_LEGAL | VARCHAR2(10) | N |  |  |
| 7 | VLR_CREDITOS | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, INSC_EST_REMETENTE, COD_AMP_LEGAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_AMP_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | VLR_CREDITOS | NUMBER(17,2) | Y |  |  |
| 7 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | COD_CHP_LIC | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_AMP_LEGAL, COD_CHP_LIC

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO3A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_AMP_LEGAL | VARCHAR2(10) | N |  |  |
| 6 | IND_ABS | CHAR(1) | N |  |  |
| 7 | AUT_BONUS_SUPL | NUMBER(9) | N |  |  |
| 8 | NUM_PARCELA | NUMBER(2) | N |  |  |
| 9 | INSC_EST_ORIGEM | VARCHAR2(14) | Y |  |  |
| 10 | VLR_CREDITOS | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_AMP_LEGAL, IND_ABS, AUT_BONUS_SUPL, NUM_PARCELA

---

## EST_RS_GIA_ANEXO4

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | PERIODO_APUR_PAGTO | NUMBER(10) | N |  |  |
| 6 | DATA_VENCTO | DATE | Y |  |  |
| 7 | VLR_DEVIDO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_PAGTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, PERIODO_APUR_PAGTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO5

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEBITOS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | VLR_EXCLUIDAS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO5A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | COD_AMP_LEGAL | VARCHAR2(10) | N |  |  |
| 7 | VLR_SAIDAS_ISENTAS | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO, COD_AMP_LEGAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO → EST_RS_GIA_ANEXO5(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO)

---

## EST_RS_GIA_ANEXO5B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | COD_AMP_LEGAL | VARCHAR2(10) | N |  |  |
| 7 | VLR_OUTRAS_SAIDAS | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO, COD_AMP_LEGAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO → EST_RS_GIA_ANEXO5(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO)

---

## EST_RS_GIA_ANEXO5C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | COD_AJUSTE | VARCHAR2(3) | N |  |  |
| 7 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 8 | DSC_ESPECIF | VARCHAR2(60) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO, COD_AJUSTE

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO → EST_RS_GIA_ANEXO5(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO)

---

## EST_RS_GIA_ANEXO6

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | INSC_EST_DESTINO | VARCHAR2(14) | N |  |  |
| 6 | COD_AMP_LEGAL | VARCHAR2(10) | N |  |  |
| 7 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, INSC_EST_DESTINO, COD_AMP_LEGAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO7

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | VLR_CRED_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 6 | VLR_OUTROS_CRED | NUMBER(17,2) | Y |  |  |
| 7 | DSC_OUTROS_CRED | VARCHAR2(60) | Y |  |  |
| 8 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 9 | VLR_DEB_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTROS_DEB | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 12 | DSC_OUTROS_DEB | VARCHAR2(60) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO7A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CRED_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → EST_RS_GIA_ANEXO7(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO7B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | VLR_BASE_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DEB_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 8 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → EST_RS_GIA_ANEXO7(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO8

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | PERIODO_APUR_PAGTO | NUMBER(4) | N |  |  |
| 6 | DATA_VENCTO | DATE | N |  |  |
| 7 | VLR_PAGTOS_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_PAGTOS_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 9 | INSC_EST_CENTRAL | VARCHAR2(14) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | VLR_ICMS_AMP | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ST_AMP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, PERIODO_APUR_PAGTO, DATA_VENCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_ANEXO9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | DIA_VENCTO | NUMBER(2) | N |  |  |
| 6 | VLR_ICMS_N_PG | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMSS_N_PG | NUMBER(17,2) | Y |  |  |
| 8 | INSC_EST_CENTRAL | VARCHAR2(14) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | VLR_ICMS_AMP | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS_ST_AMP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, DIA_VENCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_QUAD_A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | VLR_CRED_ENTRADAS | NUMBER(17,2) | Y |  |  |
| 6 | VLR_CRED_IMPORT | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_PRES | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_PG_INDEV | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTROS_CRED | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 12 | DSC_OUTROS_CRED | VARCHAR2(60) | Y |  |  |
| 13 | VLR_DEB_SAIDAS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DEB_IMPORT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DEB_RESP_COMP | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DEB_TRANSF | NUMBER(17,2) | Y |  |  |
| 17 | VLR_DEB_COMP | NUMBER(17,2) | Y |  |  |
| 18 | VLR_OUTROS_DEB | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 20 | DSC_OUTROS_DEB | VARCHAR2(60) | Y |  |  |
| 21 | IND_OPER_ICMS_ST | CHAR(1) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_QUAD_B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | VLR_SLD_CRED_ANT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ATUALIZ_MONET | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SLD_CRED_ACU | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DEDUC_EPP_ANT | NUMBER(17,2) | Y |  |  |
| 9 | VLR_PAGTOS_MES | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DEB_VENC_N_PG | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_ST_N_COMP | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_PROPRIO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DEDUC_EPP | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SLD_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CRED_N_COMP | NUMBER(17,2) | Y |  |  |
| 16 | VLR_SLD_ICMSS_TRAN | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SLD_ICMS_TRAN | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SLD_DEV_ACUM | NUMBER(17,2) | Y |  |  |
| 19 | DEDUC_EPP_TRANSP | NUMBER(17,2) | Y |  |  |
| 20 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | VLR_FUNDO_AMP | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS_AMP | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMS_ST_AMP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_QUAD_C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | VLR_FATURAMENTO | NUMBER(17,2) | Y |  |  |
| 6 | QTD_FUNCIONARIOS | NUMBER(6) | Y |  |  |
| 7 | VLR_FOLHA_PAGTO | NUMBER(17,2) | Y |  |  |
| 8 | CONSUMO_ENERGIA | NUMBER(9) | Y |  |  |
| 9 | VLR_CRED_ATIVO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_USO_CONS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OPER_INTERNA_E | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OPER_INTERNA_S | NUMBER(17,2) | Y |  |  |
| 13 | VLR_OPER_INTERES_E | NUMBER(17,2) | Y |  |  |
| 14 | VLR_OPER_INTERES_S | NUMBER(17,2) | Y |  |  |
| 15 | VLR_OPER_EXTER_E | NUMBER(17,2) | Y |  |  |
| 16 | VLR_OPER_EXTER_S | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TOT_ENTRADAS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TOT_SAIDAS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_PG_MES_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_PG_MES_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 21 | TRANSP_PROX_MES | CHAR(1) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_QUAD_E
**Comment**: Manutencao dos Profissionais Liberais para a geracao dos modulos municipais - SAFMUNIC.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | VLR_EST_INI_TRIB | NUMBER(17,2) | Y |  |  |
| 6 | VLR_EST_INI_ISEN | NUMBER(17,2) | Y |  |  |
| 7 | VLR_EST_INI_ESTAB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_EST_INI_TERC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_EST_FIM_TRIB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_EST_FIM_ISEN | NUMBER(17,2) | Y |  |  |
| 11 | VLR_EST_FIM_ESTAB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_EST_FIM_TERC | NUMBER(17,2) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_GIA_REG_OBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | DSC_OBS | VARCHAR2(4000) | Y |  |  |
| 6 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO → ESP_RS_GIA_APUR(COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO)

---

## EST_RS_PAR_COD_AJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ANEXO | VARCHAR2(2) | N |  |  |
| 4 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 5 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ANEXO, COD_AJUSTE_SPED

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## EST_SC_COD_INF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_SEF | VARCHAR2(6) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(250) | Y |  |  |

**PK**: COD_SEF

---

## EST_SC_COD_RECEITA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 2 | IND_TIPO_RECOL | CHAR(1) | Y |  |  |
| 3 | IND_TIPO_RECEITA | VARCHAR2(2) | Y |  |  |

**PK**: IDENT_RECEITA_EST

**FKs**:
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## EST_SC_DIEF_TAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TP_TAB | CHAR(1) | N |  |  |
| 4 | COD_TAB | VARCHAR2(3) | N |  |  |
| 5 | DSC_COD | VARCHAR2(50) | Y |  |  |
| 6 | COD_INDICE | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TP_TAB, COD_TAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_INDICE → Y2046_INDICE(COD_INDICE)

---

## EST_SC_DIME_BENEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_BENEF_TTD | VARCHAR2(4) | N |  |  |
| 2 | DSC_BENEF_TTD | VARCHAR2(200) | Y |  |  |

**PK**: COD_BENEF_TTD

---

## EST_SC_DIME_CC_IME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | QUADRO | VARCHAR2(3) | N |  |  |
| 4 | ITEM | VARCHAR2(3) | N |  |  |
| 5 | DATA_VALID | DATE | N |  |  |
| 6 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 7 | EXPRESSAO_SQL | VARCHAR2(4000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, QUADRO, ITEM, DATA_VALID

---

## EST_SC_DIME_CC_IME_PARC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | QUADRO | VARCHAR2(3) | N |  |  |
| 4 | ITEM | VARCHAR2(3) | N |  |  |
| 5 | DATA_VALID | DATE | N |  |  |
| 6 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 7 | OPERANDO | CHAR(1) | Y |  |  |
| 8 | PARCELA | VARCHAR2(80) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, QUADRO, ITEM, DATA_VALID, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, QUADRO, ITEM, DATA_VALID → EST_SC_DIME_CC_IME(COD_EMPRESA, COD_ESTAB, QUADRO, ITEM, DATA_VALID)

---

## EST_SC_DIME_CONC_BENEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_BENEF_TTD | VARCHAR2(4) | N |  |  |
| 4 | NUM_CONCESSAO | VARCHAR2(15) | N |  |  |
| 5 | DAT_INI_VALID | DATE | N |  |  |
| 6 | DAT_FIM_VALID | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_BENEF_TTD, NUM_CONCESSAO, DAT_INI_VALID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_BENEF_TTD → EST_SC_DIME_BENEF(COD_BENEF_TTD)

---

## EST_SC_DIME_DD_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES | NUMBER(2) | N |  |  |
| 4 | ANO | NUMBER(4) | N |  |  |
| 5 | IND_TP_DECLARACAO | CHAR(1) | Y |  |  |
| 6 | IND_REG_APUR | CHAR(1) | Y |  |  |
| 7 | IND_PORTE_EMP | CHAR(1) | Y |  |  |
| 8 | IND_APUR_CONS | CHAR(1) | Y |  |  |
| 9 | IND_APUR_CENTR | CHAR(1) | Y |  |  |
| 10 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |
| 11 | IND_ESCR_CONTAB | CHAR(1) | Y |  |  |
| 12 | IND_MOVIMENTO | CHAR(1) | Y |  |  |
| 13 | NUM_EMPREGADOS | NUMBER(5) | Y |  |  |
| 14 | VLR_DEB_FAT_GER | NUMBER(17,2) | Y |  |  |
| 15 | VLR_OUT_DEB_EVENT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_PERC_CR_AQUIS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_PROD_EXPORT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_PROD_ISENTA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_PROD_DIFERIDO | NUMBER(17,2) | Y |  |  |
| 20 | VLR_PGTO_EMPREG | NUMBER(17,2) | Y |  |  |
| 21 | VLR_MEDIA_ANT | NUMBER(17,2) | Y |  |  |
| 22 | VLR_INC_Q45_I | NUMBER(17,2) | Y |  |  |
| 23 | VLR_RECIBO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_INC_Q45_III | NUMBER(17,2) | Y |  |  |
| 25 | VLR_SERV_ISS_E | NUMBER(17,2) | Y |  |  |
| 26 | VLR_SERV_ISS_S | NUMBER(17,2) | Y |  |  |
| 27 | VLR_SUBSIDIO_GOV | NUMBER(17,2) | Y |  |  |
| 28 | VLR_RECEITA_BRT_Q80 | NUMBER(17,2) | Y |  |  |
| 29 | VLR_RECEITA_BRT_Q90 | NUMBER(17,2) | Y |  |  |
| 30 | VLR_ESTOQ_INI_Q80 | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ESTOQ_FIN_Q80 | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ESTOQ_INI_Q90 | NUMBER(17,2) | Y |  |  |
| 33 | VLR_ESTOQ_FIN_Q90 | NUMBER(17,2) | Y |  |  |
| 34 | VLR_DEB_FAT_GER_11_065 | NUMBER(17,2) | Y |  |  |
| 35 | VLR_DEB_FAT_GER_11_073 | NUMBER(17,2) | Y |  |  |
| 36 | VLR_INC_ENT_MERC | NUMBER(17,2) | Y |  |  |
| 37 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 38 | VLR_PROD_ISENTA_18 | NUMBER(17,2) | Y |  |  |
| 39 | VLR_PROD_DIFERIDA_19 | NUMBER(17,2) | Y |  |  |
| 40 | VLR_OUT_DED_997 | NUMBER(17,2) | Y |  |  |
| 41 | VAL_PAGTO_ANTEC_Q13 | NUMBER(17,2) | Y |  |  |
| 42 | VLR_CRED_SUBST_Q09 | NUMBER(17,2) | Y |  |  |
| 43 | VLR_CRED_ANTEC_Q09 | NUMBER(17,2) | Y |  |  |
| 44 | VLR_DEB_SUBST_Q09 | NUMBER(17,2) | Y |  |  |
| 45 | VLR_CRED_PRES_Q14 | NUMBER(17,2) | Y |  |  |
| 46 | VLR_DEB_CP_Q14 | NUMBER(17,2) | Y |  |  |
| 47 | VLR_SALDO_CRED_Q14 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_OUT_CRED_Q09 | NUMBER(17,2) | Y |  |  |
| 49 | VLR_DEB_CRED_PRES_Q14 | NUMBER(17,2) | Y |  |  |
| 50 | VLR_RESSARC_ICMS_ST_Q11 | NUMBER(17,2) | Y |  |  |
| 51 | VLR_CRED_SEQ_998 | NUMBER(17,2) | Y |  |  |
| 52 | IND_CONS_AJUST_COMPL | CHAR(1) | Y | 'S' |  |
| 53 | VLR_REMESSA_EXP_Q41 | NUMBER(17,2) | Y |  |  |
| 54 | COD_REGIME_ESPECIAL_Q46 | VARCHAR2(15) | Y |  |  |
| 55 | VLR_CREDITO_Q46 | NUMBER(17,2) | Y |  |  |
| 56 | VLR_FUNDES_Q16 | NUMBER(17,2) | Y |  |  |
| 57 | VLR_FUNDO_SOCIAL_Q16 | NUMBER(17,2) | Y |  |  |
| 58 | VLR_IRPJ_Q85 | NUMBER(17,2) | Y |  |  |
| 59 | VLR_FIA_EST_Q85 | NUMBER(17,2) | Y |  |  |
| 60 | VLR_FIA_MUN_Q85 | NUMBER(17,2) | Y |  |  |
| 61 | VLR_FEI_EST_Q85 | NUMBER(17,2) | Y |  |  |
| 62 | VLR_FEI_MUN_Q85 | NUMBER(17,2) | Y |  |  |
| 63 | VLR_DEV_MERC_Q11 | NUMBER(17,2) | Y |  |  |
| 64 | VLR_OUT_DEB_11_074 | NUMBER(17,2) | Y |  |  |
| 65 | VLR_DEB_ESP_11_899 | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES, ANO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_SC_DIME_LAYOUT_IME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | QUADRO | VARCHAR2(3) | N |  |  |
| 2 | ITEM | VARCHAR2(3) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(150) | Y |  |  |

**PK**: QUADRO, ITEM

---

## EST_SC_DIME_PAR_ME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | VARCHAR2(4) | N |  |  |
| 4 | DT_INVENT_INI_EA | DATE | Y |  |  |
| 5 | DT_INVENT_FIM_EA | DATE | Y |  |  |
| 6 | IND_TIPO_INVENT_EA | CHAR(1) | Y |  |  |
| 7 | DT_SALDO_EA | DATE | Y |  |  |
| 8 | DT_INVENT_INI_EC | DATE | Y |  |  |
| 9 | DT_INVENT_FIM_EC | DATE | Y |  |  |
| 10 | IND_TIPO_INVENT_EC | CHAR(1) | Y |  |  |
| 11 | DT_SALDO_EC | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CALENDARIO

---

## EST_SC_DIME_QUAD_16

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | DATE | N |  |  |
| 4 | VLR_FUMDES | NUMBER(17,2) | Y |  |  |
| 5 | VLR_FUMDES_PER_ANT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_FUMDES_DEV | NUMBER(17,2) | Y |  |  |
| 7 | VLR_FUMDES_CRED | NUMBER(17,2) | Y |  |  |
| 8 | VLR_FUMDES_RECOL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_FUN_SOC | NUMBER(17,2) | Y |  |  |
| 10 | VLR_FUN_SOC_PER_ANT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_FUN_SOC_DEV | NUMBER(17,2) | Y |  |  |
| 12 | VLR_FUN_SOC_CRED | NUMBER(17,2) | Y |  |  |
| 13 | VLR_FUN_SOC_RECOL | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REF

---

## EST_SC_DIME_TIPO3

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO3_DCIP | VARCHAR2(4) | N |  |  |
| 2 | DSC_TIPO3_DCIP | VARCHAR2(300) | Y |  |  |
| 3 | DSC_COMPL | VARCHAR2(500) | Y |  |  |
| 4 | DAT_INI_VALID | DATE | Y |  |  |
| 5 | DAT_FIM_VALID | DATE | Y |  |  |

**PK**: COD_TIPO3_DCIP

---

## EST_SC_GUIA_RECOL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_COMPETENCIA | DATE | N |  |  |
| 4 | IND_NORMAL_SUBST | CHAR(1) | N |  |  |
| 5 | DAT_VENCIMENTO | DATE | N |  |  |
| 6 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 7 | VLR_RECEITA | NUMBER(17,2) | Y |  |  |
| 8 | COD_CLASS_VENCTO | VARCHAR2(10) | N |  |  |
| 9 | IND_ORIGEM | CHAR(1) | Y |  | Criado para atendimento à DIME-SC |
| 10 | NUM_ACORDO | NUMBER(15) | Y |  | Numero do Registro de Acordo de Tratamento Tributario Diferenciado ou Regime Especial |
| 11 | NUM_DISCRIMINACAO | NUMBER(12) | N |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y | '1' |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_COMPETENCIA, IND_NORMAL_SUBST, DAT_VENCIMENTO, IDENT_RECEITA_EST, COD_CLASS_VENCTO, NUM_DISCRIMINACAO

**FKs**:
- IDENT_RECEITA_EST → EST_SC_COD_RECEITA(IDENT_RECEITA_EST)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_SC_PAR_DIEF_AN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURAC | DATE | N |  |  |
| 4 | DAT_APURAC_INI | DATE | Y |  |  |
| 5 | DAT_APURAC_FIM | DATE | Y |  |  |
| 6 | IND_SUBSTITUTIVA | CHAR(1) | Y |  |  |
| 7 | IND_ESCR_FISCAL | CHAR(1) | Y |  |  |
| 8 | IND_LVR_FISCAL | CHAR(1) | Y |  |  |
| 9 | IND_NOTA_FISCAL | CHAR(1) | Y |  |  |
| 10 | IND_MICRO | CHAR(1) | Y |  |  |
| 11 | DAT_ENTREGA | DATE | Y |  |  |
| 12 | IND_QUADRO_T | CHAR(1) | Y |  |  |
| 13 | IND_REQUERIMENTO | CHAR(1) | Y |  |  |
| 14 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 15 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 16 | COD_CONTRIBUINTE | VARCHAR2(2) | Y |  |  |
| 17 | COD_CAE | VARCHAR2(5) | Y |  |  |
| 18 | IND_ESPECIE | CHAR(1) | Y |  |  |
| 19 | COD_EXERCICIO | VARCHAR2(4) | Y |  |  |
| 20 | NUM_EMP | NUMBER(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURAC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CONTADOR → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONTRIBUINTE → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_SC_PAR_GIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IND_NORMAL_SUBST | CHAR(1) | Y |  |  |
| 5 | VLR_RECOLHIMENTO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_OUTROS_DEBITO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CORRECAO_SALDO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_OUTROS_CREDITO | NUMBER(17,2) | Y |  |  |
| 9 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 10 | IND_CONTRIBUINTE | CHAR(1) | Y |  |  |
| 11 | DAT_INICIAL | DATE | Y |  |  |
| 12 | DAT_FINAL | DATE | Y |  |  |
| 13 | DSC_OBSERVACAO | VARCHAR2(255) | Y |  |  |
| 14 | VLR_FATURAMENTO | NUMBER(17,2) | Y |  |  |
| 15 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 16 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |
| 17 | DSC_MUNICIPIO | VARCHAR2(25) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_CONTADOR → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_SC_PAR_GIA_2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 5 | VLR_FATURAMENTO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_EST_CRED_CIAP | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DEB_AP_CONS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_AP_CONS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CPRES_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_INCENT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CRED_FATO_GER | NUMBER(17,2) | Y |  |  |
| 12 | VLR_RESSARC_ICMSS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ACRES_FINANC | NUMBER(17,2) | Y |  |  |
| 14 | IND_MOVTO | CHAR(1) | Y |  |  |
| 15 | NUM_EMPREG | NUMBER(5) | Y |  |  |
| 16 | VLR_DESPEZA_EMPREG | NUMBER(17,2) | Y |  |  |
| 17 | COD_PERIOD_APUR | VARCHAR2(2) | Y |  |  |
| 18 | COD_CLASS_VENCTO | VARCHAR2(10) | Y |  |  |
| 19 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 20 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |
| 21 | DSC_MUNICIPIO | VARCHAR2(25) | Y |  |  |
| 22 | VLR_CRED_DALIQ_AP | NUMBER(17,2) | Y |  |  |
| 23 | VLR_CRED_DALIQ_MC | NUMBER(17,2) | Y |  |  |
| 24 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 25 | VLR_DEB_DALIQ | NUMBER(17,2) | Y |  |  |
| 26 | VLR_EST_CRED | NUMBER(17,2) | Y |  |  |
| 27 | VLR_OUT_DEB | NUMBER(17,2) | Y |  |  |
| 28 | VLR_OUT_CRED | NUMBER(17,2) | Y |  |  |
| 29 | IND_REG_APUR | CHAR(1) | Y | '1' | Regime de Apuração |
| 30 | VLR_BASE_CALC_ST | NUMBER(17,2) | Y |  |  |
| 31 | VLR_IMP_RET_ST | NUMBER(17,2) | Y |  |  |
| 32 | VLR_CRED_PERANT_ST | NUMBER(17,2) | Y |  |  |
| 33 | VLR_CRED_ST | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

---

## EST_SC_PAR_RECEITA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_RECOL | CHAR(1) | N |  |  |
| 4 | IND_TP_RECEITA | VARCHAR2(2) | N |  |  |
| 5 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_TP_RECOL, IND_TP_RECEITA, IDENT_RECEITA_EST

**FKs**:
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_SC_REG47_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | VALOR_OPER | NUMBER(17,2) | Y |  |  |
| 7 | IND_QUADRO | VARCHAR2(2) | N | '47' |  |
| 8 | COD_TIPO_ATIV | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_ESTADO, COD_MUNICIPIO, IND_QUADRO, COD_TIPO_ATIV

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_SEFPE_MMAG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_GERACAO | DATE | Y |  |  |
| 5 | DATA_APURACAO | DATE | Y |  |  |
| 6 | COD_PERFIL | VARCHAR2(3) | Y |  |  |

**PK**: NUM_PROCESSO

---

## EST_SEFPE_OBRIG_RECOL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APURACAO | NUMBER(2) | N |  |  |
| 4 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 5 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 6 | DAT_VENCIMENTO | DATE | Y |  |  |
| 7 | IND_FLAG_DSCR | VARCHAR2(2) | Y |  |  |
| 8 | VLR_RECOLH | NUMBER(17,2) | Y |  |  |
| 9 | DESCRICAO | VARCHAR2(70) | Y |  |  |
| 10 | INSC_EST_REFER | VARCHAR2(14) | Y |  |  |
| 11 | NUM_DOCFIS_REFER | VARCHAR2(12) | Y |  |  |
| 12 | MOD_DOCFIS_REFER | VARCHAR2(2) | Y |  |  |
| 13 | DAT_DOCFIS_REFER | DATE | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 17 | ATO_NORMATIVO | VARCHAR2(20) | Y |  |  |
| 18 | NUM_ATO_NORMATIVO | NUMBER(5) | Y |  |  |
| 19 | ANO_ATO_NORMATIVO | NUMBER(4) | Y |  |  |
| 20 | CAPITULACAO_NORMA | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO, IDENT_RECEITA_EST

**FKs**:
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## EST_SEFPE_PAR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PRODEPE | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## EST_SEFPE_PAR_INC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_VALID | DATE | N |  |  |
| 4 | SERIE_LVR | VARCHAR2(3) | N |  |  |
| 5 | SUB_SERIE_LVR | VARCHAR2(2) | N |  |  |
| 6 | COD_APUR_SEF | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_VALID, SERIE_LVR, SUB_SERIE_LVR

---

## EST_SEFPE_PAR_INVENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | N |  |  |
| 2 | IND_TP_INVENT | CHAR(1) | Y |  |  |

**PK**: IND_PRODUTO

---

## EST_SEFPE_PRD_GEN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_ITEM | NUMBER(3) | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |

**PK**: GRUPO_PRODUTO, NUM_ITEM

---

## EST_SEFPE_REG_MMAG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 2 | TIPO_REGISTRO | VARCHAR2(4) | Y |  |  |
| 3 | SUBTIPO_REGISTRO | VARCHAR2(2) | Y |  |  |
| 4 | DETALHE_REGISTRO | VARCHAR2(2) | Y |  |  |
| 5 | SEQ_88 | NUMBER(12) | Y |  |  |
| 6 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | SERIE_EQUIPAMENTO | VARCHAR2(20) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 15 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 16 | REG_MEIO_MAG | VARCHAR2(300) | Y |  |  |
| 17 | SEQ_OBS | NUMBER(5) | Y |  |  |

**FKs**:
- NUM_PROCESSO → EST_SEFPE_MMAG(NUM_PROCESSO)

**Indexes**:
- IX_E_SEFPE_RG_MMAG: (NUM_PROCESSO)

---

## EST_SEFPE_TIPO88_30

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_PERIODO | DATE | N |  |  |
| 4 | CADASTRO | CHAR(1) | Y |  |  |
| 5 | SUBSTITUTO | CHAR(1) | Y |  |  |
| 6 | MOVIMENTO | CHAR(1) | Y |  |  |
| 7 | COD_CONTADOR | VARCHAR2(2) | Y |  |  |
| 8 | COD_RESP | VARCHAR2(2) | Y |  |  |
| 9 | VLR_ACUMULADO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_EXPORT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 12 | DAT_EXERC_FIN | DATE | Y |  |  |
| 13 | QTD_CONS_ENERGIA | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_PERIODO

---

## EST_SEFPE_TIPO_88

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | Y |  |  |
| 2 | TIPO_REGISTRO | VARCHAR2(4) | Y |  |  |
| 3 | SUBTIPO_REGISTRO | VARCHAR2(2) | Y |  |  |
| 4 | DETALHE_REGISTRO | VARCHAR2(2) | Y |  |  |
| 5 | REG_MEIO_MAG | VARCHAR2(300) | Y |  |  |

---

## EST_SE_DIC_CFO_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 5 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 6 | COD_CFO_ESTEND | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

---

## EST_SE_DIC_GRP_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_PROD_DIC | NUMBER(12) | N |  |  |
| 2 | GRP_PROD_DIC | VARCHAR2(9) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_GRP_PROD_DIC

**Indexes**:
- IX_ESTSE_DIC_GRPRD (UNIQUE): (GRP_PROD_DIC)

---

## EST_SE_DIC_IMP_DEV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APUR | NUMBER(2) | N |  |  |
| 4 | ANO_APUR | NUMBER(4) | N |  |  |
| 5 | VLR_ICMS_NORMAL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMSS_INT | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMSS_TRANSP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_ANT_CEF | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_ANT_MVA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_ANT_SMVA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DIFAL_CONS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DIFAL_IMOB | NUMBER(17,2) | Y |  |  |
| 13 | VLR_INCENT_PSDI | NUMBER(17,2) | Y |  |  |
| 14 | VLR_EST_DEB_ICMSS | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 17 | VLR_FUNDO_POBREZA | NUMBER(17,2) | Y |  |  |
| 18 | DESCRICAO | VARCHAR2(500) | Y |  |  |
| 19 | VLR_FUNDO_POBREZA_STI | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APUR, ANO_APUR

---

## EST_SE_DIC_INC_BEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APUR | NUMBER(2) | N |  |  |
| 4 | ANO_APUR | NUMBER(4) | N |  |  |
| 5 | IDENT_FIS_JUR_S | NUMBER(12) | N |  |  |
| 6 | IDENT_MODELO_S | NUMBER(12) | N |  |  |
| 7 | SERIE_DOCFIS_S | VARCHAR2(3) | N |  |  |
| 8 | NUM_DOCFIS_S | VARCHAR2(12) | N |  |  |
| 9 | NUM_ITEM_S | NUMBER(5) | N |  |  |
| 10 | IDENT_CFO_S | NUMBER(12) | Y |  |  |
| 11 | IDENT_FIS_JUR_E | NUMBER(12) | Y |  |  |
| 12 | IDENT_MODELO_E | NUMBER(12) | Y |  |  |
| 13 | SERIE_DOCFIS_E | VARCHAR2(3) | Y |  |  |
| 14 | NUM_DOCFIS_E | VARCHAR2(12) | Y |  |  |
| 15 | DATA_EMISSAO_E | DATE | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 17 | VLR_IMOBILIZADO | NUMBER(17,2) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APUR, ANO_APUR, IDENT_FIS_JUR_S, IDENT_MODELO_S, SERIE_DOCFIS_S, NUM_DOCFIS_S, NUM_ITEM_S

---

## EST_SE_DIC_INVENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_INVENT | NUMBER(4) | N |  |  |
| 4 | VLR_MAT_PRIMA_INI | NUMBER(17,2) | Y |  |  |
| 5 | VLR_MAT_PRIMA_FIM | NUMBER(17,2) | Y |  |  |
| 6 | VLR_PRD_ACAB_INI | NUMBER(17,2) | Y |  |  |
| 7 | VLR_PRD_ACAB_FIM | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ISENTAS_INI | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ISENTAS_FIM | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SUBST_INI | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SUBST_FIM | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PRD_PROC_INI | NUMBER(17,2) | Y |  |  |
| 13 | VLR_PRD_PROC_FIM | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_INVENT

---

## EST_SE_DIC_OBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_OBSERVACAO | VARCHAR2(9) | N |  |  |
| 2 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |

**PK**: GRUPO_OBSERVACAO, COD_OBSERVACAO

---

## EST_SE_DIC_PREST_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APUR | NUMBER(4) | N |  |  |
| 4 | MES_APUR | NUMBER(2) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | COD_MUNIC | NUMBER(5) | N |  |  |
| 7 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | IDENT_CFO | NUMBER(12) | N |  |  |
| 10 | COD_CFO_ESTEND | NUMBER(2) | N |  |  |
| 11 | COD_SERVICO | NUMBER(3) | N |  |  |
| 12 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 13 | NUM_DOCFIS_FIN | VARCHAR2(12) | Y |  |  |
| 14 | DAT_EMISSAO_INI | DATE | Y |  |  |
| 15 | DAT_EMISSAO_FIN | DATE | Y |  |  |
| 16 | QTDE_CONS | NUMBER(7) | Y |  |  |
| 17 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_NEGATIVO | NUMBER(17,2) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APUR, MES_APUR, IDENT_ESTADO, COD_MUNIC, IDENT_MODELO, SERIE_DOCFIS, IDENT_CFO, COD_CFO_ESTEND, COD_SERVICO

**FKs**:
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_ESTADO, COD_MUNIC → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_SE_DIC_RAT_MNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APUR | NUMBER(2) | N |  |  |
| 4 | ANO_APUR | NUMBER(4) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | VLR_PERC_RATEIO | NUMBER(5,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APUR, ANO_APUR, COD_MUNICIPIO

---

## EST_SE_DIC_R_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APUR | NUMBER(2) | N |  |  |
| 4 | ANO_APUR | NUMBER(4) | N |  |  |
| 5 | VLR_DEB_PSDI | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ESTORNO_CRE | NUMBER(17,2) | Y |  |  |
| 7 | VLR_OUTROS_DEB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_PRES | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SLD_ANT_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTROS_CRE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ESTORNO_DEB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CRED_IMOB | NUMBER(17,2) | Y |  |  |
| 14 | MES_QUITACAO | NUMBER(2) | Y |  |  |
| 15 | ANO_QUITACAO | NUMBER(4) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 18 | VLR_TRAN_CRED_ACU | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APUR, ANO_APUR

---

## EST_SE_DIC_R_FINAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APUR | NUMBER(2) | N |  |  |
| 4 | ANO_APUR | NUMBER(4) | N |  |  |
| 5 | VLR_SLD_INI_CAIXA | NUMBER(17,2) | Y |  |  |
| 6 | VLR_SLD_INI_BANC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_SLD_FIM_CAIXA | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SLD_FIM_BANC | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SLD_RECEB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SLD_RECEB_OUT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SLD_PAGAR | NUMBER(17,2) | Y |  |  |
| 12 | VLR_SLD_PAGAR_OUT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SLD_EMP_PFIS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SLD_EMP_PJUR | NUMBER(17,2) | Y |  |  |
| 15 | VLR_MOVTO_EMP_PFIS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_MOVTO_EMP_PJUR | NUMBER(17,2) | Y |  |  |
| 17 | VLR_RECEB_MES | NUMBER(17,2) | Y |  |  |
| 18 | VLR_PAGTO_MES | NUMBER(17,2) | Y |  |  |
| 19 | VLR_PAGTO_OUT | NUMBER(17,2) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APUR, ANO_APUR

---

## EST_SE_DIC_SRV_MUN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APUR | NUMBER(2) | N |  |  |
| 4 | ANO_APUR | NUMBER(4) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | COD_MUNIC_ADIC | VARCHAR2(5) | N |  |  |
| 7 | IDENT_CFO | VARCHAR2(4) | N |  |  |
| 8 | COD_CFO_ESTEND | VARCHAR2(2) | N |  |  |
| 9 | COD_SERVICO | VARCHAR2(3) | N |  |  |
| 10 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APUR, ANO_APUR, IDENT_ESTADO, COD_MUNIC_ADIC, IDENT_CFO, COD_CFO_ESTEND, COD_SERVICO

---

## EST_SE_DIC_TRAN_SC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APUR | NUMBER(2) | N |  |  |
| 4 | ANO_APUR | NUMBER(4) | N |  |  |
| 5 | VLR_TRAN_ACU_LVR | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TRAN_ACU_O_C | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ACU_AQ_BEM | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ACU_AQ_INS_MP | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ACU_PG_DEB | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ACU_PER_SEG | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | VLR_SLD_C_AC_LVRII | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APUR, ANO_APUR

---

## EST_SE_DIC_TRF_CD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_APUR | NUMBER(2) | N |  |  |
| 4 | ANO_APUR | NUMBER(4) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 11 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 12 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_APUR, ANO_APUR, DATA_EMISSAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR

---

## EST_SIS_PR_DD_INIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_CREDENCIAL | VARCHAR2(10) | Y |  |  |
| 4 | COD_RESP | VARCHAR2(2) | Y |  |  |
| 5 | COD_CONT_RESP | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESP → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONT_RESP → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_SIS_PR_QUADRO
**Comment**: Tabela do módulo SISCRED - PR. Armazena os dados demonstrados no Formulário.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_GERACAO | NUMBER(4) | N |  |  |
| 4 | MES_GERACAO | NUMBER(2) | N |  |  |
| 5 | SEQ_LINHA | NUMBER(2) | N |  | Sequencial que identifica a linha do relatório. Ex: Linha 1.1 - seq_linha = 1; Linha 1.1.1 - seq_linha = 2; Linha 1.1.2 - seq_linha = 3. |
| 6 | DSC_LINHA | VARCHAR2(120) | Y |  | Ddescrição da linha apresentada no relatório. Ex:  Linha 1.1 - dsc_linha = 1.1. APURAÇÃO DA ALÍQUOTA MÉDIA DO ICMS NAS ENTRADAS. |
| 7 | VLR_LINHA | NUMBER(17,2) | Y |  | Valor da linha apresentado no relatório. |
| 8 | DATA_INI_QUADRO | DATE | Y |  |  |
| 9 | DATA_FIM_QUADRO | DATE | Y |  |  |
| 10 | IND_QUADRO | CHAR(1) | Y |  | Código dos quadros apresentados no relatório. Ex: 1 (Quadro 1), 2 (Quadro 2), 3 (Quadro 3), 4 (Quadro 4). |
| 11 | DSC_QUADRO | VARCHAR2(70) | Y |  |  |
| 12 | NUM_NIVEL | NUMBER(1) | Y |  | Representa a hierarquia que as linhas são apresentadas no relatório. Domino: 1, 2. Ex: Linha 1.1 - num_nivel = 1; Linha 1.1.1 - num_nivel = 2. |
| 13 | IND_PREENCHIMENTO | CHAR(1) | Y |  | Indica a forma de preenchimento do valor. Dominio: G – gerado, D - digitado via manutenção, C – calculado, N - nem gerado, nem digitado (linha sem valor). |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_GERACAO, MES_GERACAO, SEQ_LINHA

---

## EST_SIT_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | COD_SITUACAO | VARCHAR2(2) | N |  |  |
| 3 | DSC_SITUACAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_UF_OBRIG, COD_SITUACAO

---

## EST_SP_AUX_REG20

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | DATE | Y |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 5 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 6 | DSC_AMPARO_LEGAL | VARCHAR2(100) | Y |  |  |
| 7 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 8 | IND_ICMS | CHAR(1) | Y |  |  |
| 9 | DSC_OCORRENCIA | VARCHAR2(300) | Y |  |  |

---

## EST_SP_CAT17_MM2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | CPF_CNPJ | VARCHAR2(14) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 9 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 10 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 11 | COD_COMPL_OP | VARCHAR2(2) | Y |  |  |
| 12 | QUANTIDADE | NUMBER(13,3) | Y |  |  |
| 13 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_VC | NUMBER(17,2) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 18 | CHASSI | VARCHAR2(17) | Y |  |  |
| 19 | MODELO_LIVRO | VARCHAR2(1) | Y |  |  |
| 20 | VLR_BASE_OP_PROP | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_EST_REM | NUMBER(17,2) | Y |  |  |
| 22 | DATA_APURACAO | DATE | Y |  |  |
| 23 | NUM_SEQ | NUMBER(3) | N |  |  |
| 24 | TIPO_MOVTO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, CPF_CNPJ, COD_PRODUTO, NUM_SEQ

---

## EST_SP_CAT17_MM3A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 5 | SERIE_EQUIPAMENTO | VARCHAR2(15) | Y |  |  |
| 6 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 7 | NUM_CUPOM_INICIAL | VARCHAR2(12) | Y |  |  |
| 8 | NUM_CUPOM_FINAL | VARCHAR2(12) | Y |  |  |
| 9 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |
| 10 | VLR_GT_INICIAL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_GT_FINAL | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO

---

## EST_SP_CAT17_MM3B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 5 | SITUACAO_TRIBUT | VARCHAR2(4) | N |  |  |
| 6 | VALOR | NUMBER(17,2) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO, SITUACAO_TRIBUT

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO → EST_SP_CAT17_MM3A(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO)

---

## EST_SP_CAT17_MM3C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | QUANTIDADE | NUMBER(13,3) | Y |  |  |
| 7 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_VC | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO → EST_SP_CAT17_MM3A(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO)

---

## EST_SP_CAT17_MM4

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | UNIDADE | VARCHAR2(8) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_PRODUTO

---

## EST_SP_CAT17_MM5

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | ALIQ_INTERNA | NUMBER(7,4) | N |  |  |
| 6 | DATA_INI | DATE | Y |  |  |
| 7 | DATA_FIM | DATE | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_PRODUTO, ALIQ_INTERNA

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_PRODUTO → EST_SP_CAT17_MM4(COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_PRODUTO)

---

## EST_SP_CAT17_MM6

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | DATA_INICIAL | DATE | Y |  |  |
| 5 | ESP_EQUIPAMENTO | VARCHAR2(50) | Y |  |  |
| 6 | DSC_MODELO | VARCHAR2(30) | Y |  |  |
| 7 | TIPO_MIDIA | CHAR(1) | Y |  |  |
| 8 | NUM_VOLUMES | NUMBER(5) | Y |  |  |
| 9 | TOT_REG_01 | NUMBER(9) | Y |  |  |
| 10 | TOT_REG_02 | NUMBER(9) | Y |  |  |
| 11 | TOT_REG_03 | NUMBER(9) | Y |  |  |
| 12 | TOT_REG_04 | NUMBER(9) | Y |  |  |
| 13 | TOT_REG_05 | NUMBER(9) | Y |  |  |
| 14 | TOT_REG_06 | NUMBER(9) | Y |  |  |
| 15 | TOT_REG_GERAL | NUMBER(9) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO

---

## EST_SP_CAT17_MOD_2
**Comment**: Tabela que armazena os dados do relatório Modelo II.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 6 | VLR_DIF_COMPL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_DIF_RESSARC | NUMBER(17,2) | Y |  |  |
| 8 | VLR_DIF_COMPENS | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_FIS_JUR, ALIQ_ICMS

---

## EST_SP_CAT17_MOD_4
**Comment**: Tabela que armazena os dados do relatório Modelo IV.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 6 | CHASSI | VARCHAR2(17) | N |  |  |
| 7 | DATA_FISCAL_E | DATE | N |  |  |
| 8 | NUM_DOCFIS_E | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS_E | VARCHAR2(3) | Y |  |  |
| 10 | VLR_BASE_SUBST | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 12 | DATA_FISCAL_S | DATE | N |  |  |
| 13 | NUM_DOCFIS_S | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS_S | VARCHAR2(3) | Y |  |  |
| 15 | VLR_SAI_COM_S | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_S_VC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_E_VC | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_EST_REM | NUMBER(17,2) | Y |  |  |
| 19 | VLR_COMPL_IMP | NUMBER(17,2) | Y |  |  |
| 20 | VLR_TOTAL_EXC | NUMBER(17,2) | Y |  |  |
| 21 | VLR_PARC_RESSARC | NUMBER(17,2) | Y |  |  |
| 22 | VLR_PARC_COMPENS | NUMBER(17,2) | Y |  |  |
| 23 | ORDEM | NUMBER(2) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_FIS_JUR, ALIQ_ICMS, CHASSI, DATA_FISCAL_E, DATA_FISCAL_S

---

## EST_SP_CAT17_VEIC_APUR
**Comment**: Tabela que armazena os valores referentes a veículos que serão lançados na apuração.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | VLR_SALDO_COMPL | NUMBER(17,2) | Y |  |  |
| 5 | VLR_SALDO_RESSARC | NUMBER(17,2) | Y |  |  |
| 6 | VLR_SALDO_COMPENS | NUMBER(17,2) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO

---

## EST_SP_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | REG_TRIB | VARCHAR2(2) | Y |  |  |
| 4 | FORN_SOFT | VARCHAR2(14) | Y |  |  |
| 5 | IND_SUBST_ICMSS | VARCHAR2(1) | Y |  |  |
| 6 | IND_VAL_OUTRAS | VARCHAR2(1) | Y |  |  |
| 7 | IND_PRT_CFOP | VARCHAR2(1) | Y |  |  |
| 8 | IND_PRT_NAT | VARCHAR2(1) | Y |  |  |
| 9 | IND_AMPARO | VARCHAR2(1) | Y |  |  |
| 10 | IND_PRT_CLASSE | VARCHAR2(1) | Y |  |  |
| 11 | IND_AMP_APUR | VARCHAR2(1) | Y |  |  |
| 12 | IND_REG_31 | VARCHAR2(1) | Y |  |  |
| 13 | IND_DES_VAL_OUTRAS_IMP | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## EST_SP_DIPAM_25

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_DIPAM_B | NUMBER(2) | N |  |  |
| 5 | COD_MUNICIPIO_DEST | NUMBER(5) | N |  |  |
| 6 | DSC_MUNICIPIO_DEST | VARCHAR2(50) | Y |  |  |
| 7 | VLR_SAIDA_PER | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SUBJUD_PER | NUMBER(17,2) | Y |  |  |
| 9 | VLR_SAIDA_FORA_PER | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SUBJUD_FORA_PER | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_LIQ | NUMBER(17,2) | Y |  |  |
| 12 | VLR_RATEIO_MUNIC | NUMBER(9,7) | Y |  |  |
| 13 | VLR_TOT_VA | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOT_ENT | NUMBER(17,2) | Y |  |  |
| 15 | VLR_VA_DIPAM | NUMBER(17,2) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_DIPAM_B, COD_MUNICIPIO_DEST

---

## EST_SP_DIPAM_B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DIPAM | NUMBER(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(250) | Y |  |  |
| 3 | CABECALHO | VARCHAR2(250) | Y |  |  |

**PK**: COD_DIPAM

---

## EST_SP_GIA_REG05

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | CNPJ_FORN_SOFT | VARCHAR2(14) | Y |  |  |
| 5 | REG_TRIB | VARCHAR2(2) | Y |  |  |
| 6 | IND_TIPO_GIA | VARCHAR2(2) | Y |  |  |
| 7 | IND_MOVTO | CHAR(1) | Y |  |  |
| 8 | IND_TRANSMITIDO | CHAR(1) | Y |  |  |
| 9 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SALDO_ANT_ST | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_SP_GIA_REG10

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTR_IMPOSTOS | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 15 | VLR_ST_SUBSTITUTO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ST_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO → EST_SP_GIA_REG05(COD_EMPRESA, COD_ESTAB, DAT_APURACAO)

---

## EST_SP_GIA_REG14

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | COD_UF | VARCHAR2(2) | N |  |  |
| 6 | VLR_CONTABIL_1 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CONTABIL_2 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PETR_ENERG_ST | NUMBER(17,2) | Y |  |  |
| 13 | VLR_OUTROS_ST | NUMBER(17,2) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 17 | VLR_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO, COD_UF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO → EST_SP_GIA_REG10(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO)

---

## EST_SP_GIA_REG18

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | COD_UF | VARCHAR2(2) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | DATA_EMISSAO | DATE | N |  |  |
| 10 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 11 | CNPJ_DEST | VARCHAR2(14) | Y |  |  |
| 12 | COD_MUNIC_DEST | NUMBER(5) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO, COD_UF, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_EMISSAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO, COD_UF → EST_SP_GIA_REG14(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CFO, COD_UF)

---

## EST_SP_GIA_REG20

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | SEQUENCIA | NUMBER(12) | N |  |  |
| 6 | DSC_AMPARO_LEGAL | VARCHAR2(100) | Y |  |  |
| 7 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 8 | IND_ICMS | CHAR(1) | Y |  |  |
| 9 | DSC_OCORRENCIA | VARCHAR2(300) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO → EST_SP_GIA_REG05(COD_EMPRESA, COD_ESTAB, DAT_APURACAO)

---

## EST_SP_GIA_REG25

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | SEQUENCIA | NUMBER(12) | N |  |  |
| 6 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA → EST_SP_GIA_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA)

---

## EST_SP_GIA_REG2627

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | SEQUENCIA | NUMBER(12) | N |  |  |
| 6 | TIPO_REGISTRO | VARCHAR2(2) | N |  |  |
| 7 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | VALOR | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA, TIPO_REGISTRO, INSC_ESTADUAL, NUM_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA → EST_SP_GIA_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA)

---

## EST_SP_GIA_REG28

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | SEQUENCIA | NUMBER(12) | N |  |  |
| 6 | COD_AUTORIZACAO | VARCHAR2(12) | N |  |  |
| 7 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA, COD_AUTORIZACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA → EST_SP_GIA_REG20(COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_AMPARO_LEGAL, SEQUENCIA)

---

## EST_SP_GIA_REG30

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | COD_DIPAM_B | NUMBER(2) | N |  |  |
| 5 | COD_MUNICIPIO_DEST | NUMBER(5) | N |  |  |
| 6 | DAT_DIPAM_B | DATE | Y |  |  |
| 7 | VALOR_DIPAM_B | NUMBER(17,2) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_DIPAM_B, COD_MUNICIPIO_DEST

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO → EST_SP_GIA_REG05(COD_EMPRESA, COD_ESTAB, DAT_APURACAO)

---

## EST_SP_GIA_REG31

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | NUM_REG_EXP | VARCHAR2(12) | N |  |  |
| 5 | USUARIO | VARCHAR2(40) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, NUM_REG_EXP

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_APURACAO → EST_SP_GIA_REG05(COD_EMPRESA, COD_ESTAB, DAT_APURACAO)

---

## EST_ST_MG_MEDIA_POND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_GER | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | QTD_CONV_INI | NUMBER(17,6) | Y |  |  |
| 9 | VLR_ICMS_INI_MP | NUMBER(19,6) | Y |  |  |
| 10 | VLR_ICMS_ST_INI_MP | NUMBER(19,6) | Y |  |  |
| 11 | VLR_BC_ST_INI_MP | NUMBER(19,6) | Y |  |  |
| 12 | VLR_FECEP_ST_INI_MP | NUMBER(19,6) | Y |  |  |
| 13 | QTD_CONV_ENT_MP | NUMBER(17,6) | Y |  |  |
| 14 | VLR_ICMS_ENT_MP | NUMBER(19,6) | Y |  |  |
| 15 | VLR_ICMS_ST_ENT_MP | NUMBER(19,6) | Y |  |  |
| 16 | VLR_BC_ST_ENT_MP | NUMBER(19,6) | Y |  |  |
| 17 | VLR_FECEP_ST_ENT_MP | NUMBER(19,6) | Y |  |  |
| 18 | QTD_CONV_DEV_ENT_MP | NUMBER(17,6) | Y |  |  |
| 19 | VLR_ICMS_DEV_ENT_MP | NUMBER(19,6) | Y |  |  |
| 20 | VLR_ICMS_ST_DEV_ENT_MP | NUMBER(19,6) | Y |  |  |
| 21 | VLR_BC_ST_DEV_ENT_MP | NUMBER(19,6) | Y |  |  |
| 22 | VLR_FECEP_ST_DEV_ENT_MP | NUMBER(19,6) | Y |  |  |
| 23 | QTD_CONV_FIM | NUMBER(17,6) | Y |  |  |
| 24 | VLR_ICMS_FIM_MP | NUMBER(19,6) | Y |  |  |
| 25 | VLR_ICMS_ST_FIM_MP | NUMBER(19,6) | Y |  |  |
| 26 | VLR_BC_ST_FIM_MP | NUMBER(19,6) | Y |  |  |
| 27 | VLR_FECEP_ST_FIM_MP | NUMBER(19,6) | Y |  |  |
| 28 | VLR_UNIT_ICMS_FIM_MP | NUMBER(19,6) | Y |  |  |
| 29 | VLR_UNIT_ICMS_ST_FIM_MP | NUMBER(19,6) | Y |  |  |
| 30 | VLR_UNIT_BC_ST_FIM_MP | NUMBER(19,6) | Y |  |  |
| 31 | VLR_UNIT_FECEP_ST_FIM_MP | NUMBER(19,6) | Y |  |  |
| 32 | VLR_UNIT_ICMS_ST_FECEP_FIM_MP | NUMBER(19,6) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 34 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, DATA, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**Indexes**:
- IX_EST_ST_MG_MEDIA_POND: (DATA, COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)

---

## EST_ST_MG_NF_SAI

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
| 11 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 12 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 13 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 14 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 15 | VLR_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 16 | COD_MOTIVO_SAI | VARCHAR2(5) | Y |  |  |
| 17 | VLR_UNIT_ICMS_OPER_SAI | NUMBER(19,6) | Y |  |  |
| 18 | VLR_UNIT_ICMS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_ICMSS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 20 | VLR_UNIT_FCP_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 21 | VLR_UNIT_ICMSS_REST_SAI | NUMBER(19,6) | Y |  |  |
| 22 | VLR_UNIT_FCP_REST_SAI | NUMBER(19,6) | Y |  |  |
| 23 | VLR_UNIT_ICMSS_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 24 | VLR_UNIT_FCP_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 25 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 26 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 27 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 28 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 29 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 30 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 31 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 32 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 33 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 34 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 35 | DATA_EMISSAO | DATE | Y |  |  |
| 36 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 37 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 38 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 39 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 40 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 41 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 42 | IDENT_MEDIDA_PROD | NUMBER(12) | Y |  |  |
| 43 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 44 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 45 | VLR_BASE_REDU_ICMSS | NUMBER(17,2) | Y |  |  |
| 46 | VLR_BASE_ICMS_CONV | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## EST_ST_MG_SALDO_MED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 8 | VLR_MED_UNIT_ICMS | NUMBER(19,6) | Y |  |  |
| 9 | VLR_MED_UNIT_BC_ICMSS | NUMBER(19,6) | Y |  |  |
| 10 | VLR_MED_UNIT_ICMSS | NUMBER(19,6) | Y |  |  |
| 11 | VLR_MED_UNIT_FECP | NUMBER(19,6) | Y |  |  |
| 12 | VLR_MED_UNIT_ICMSS_FECEP | NUMBER(21,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## EST_ST_PR_APUR_RESSARC_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | VLR_RESSARC_ST_1200 | NUMBER(17,2) | Y |  |  |
| 5 | VLR_COMPL_ST_1200 | NUMBER(17,2) | Y |  |  |
| 6 | VLR_RESSARC_ST_1300 | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RESSARC_ST_1400 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_RESSARC_ST_1500 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_RESSARC_FECOP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_COMPL_FECOP | NUMBER(17,2) | Y |  |  |
| 11 | OPCAO_R1200 | VARCHAR2(1) | Y |  |  |
| 12 | OPCAO_R1300 | VARCHAR2(1) | Y |  |  |
| 13 | OPCAO_R1400 | VARCHAR2(1) | Y |  |  |
| 14 | OPCAO_R1500 | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO

---

## EST_ST_PR_CALC_TOT_ENT_SAI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | IND_TIPO_REG | VARCHAR2(4) | N |  |  |
| 7 | QTD_TOT_ENTRADA_E | NUMBER(17,3) | Y |  |  |
| 8 | MENOR_VL_UNIT_ITEM_E | NUMBER(17,2) | Y |  |  |
| 9 | VL_BC_ICMSST_UNIT_MED_E | NUMBER(17,2) | Y |  |  |
| 10 | VL_TOT_ICMS_SUPORT_E | NUMBER(17,2) | Y |  |  |
| 11 | VL_UNIT_MED_ICMS_SUPORT_E | NUMBER(17,2) | Y |  |  |
| 12 | QTD_TRANSF_E | NUMBER(17,3) | Y |  |  |
| 13 | QTD_TOT_SAIDA_S | NUMBER(17,3) | Y |  |  |
| 14 | VL_TOT_ICMS_EFETIVO_S | NUMBER(17,2) | Y |  |  |
| 15 | VL_CONFRONTO_ICMS_ENTRADA_S | NUMBER(17,2) | Y |  |  |
| 16 | RESULT_RECUPERAR_RESSARCIR_S | NUMBER(17,2) | Y |  |  |
| 17 | RESULT_COMPLEMENTAR_S | NUMBER(17,2) | Y |  |  |
| 18 | APUR_ICMSST_RECUP_RESSARCIR_S | NUMBER(17,2) | Y |  |  |
| 19 | APUR_ICMSST_COMPLEMENTAR_S | NUMBER(17,2) | Y |  |  |
| 20 | APUR_FECOP_RESSARCIR_S | NUMBER(17,2) | Y |  |  |
| 21 | APUR_FECOP_COMPLEMENTAR_S | NUMBER(17,2) | Y |  |  |
| 22 | VL_ICMSST_UNIT_ENTR_S | NUMBER(17,2) | Y |  |  |
| 23 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 24 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 25 | ORIGEM_ALIQ | VARCHAR2(3) | Y |  |  |
| 26 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 27 | MVA | NUMBER(9,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO, IND_PRODUTO, COD_PRODUTO, IND_TIPO_REG

---

## EST_ST_PR_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_REG_ESPECIAL | VARCHAR2(10) | Y |  |  |
| 4 | COD_ESTAB_CD | VARCHAR2(6) | Y |  |  |
| 5 | IND_COD_PROD | VARCHAR2(1) | Y |  |  |
| 6 | IND_DESC_PROD | VARCHAR2(1) | Y |  |  |
| 7 | IND_NGER_SLD_NEG | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB_CD → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_ST_PR_NF_ENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 4 | DATA_PERIODO | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 10 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 14 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 15 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | N |  |  |
| 17 | MOVTO_E_S | CHAR(1) | N |  |  |
| 18 | NORM_DEV | CHAR(1) | Y |  |  |
| 19 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 20 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 21 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 22 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 23 | DATA_EMISSAO | DATE | Y |  |  |
| 24 | DATA_SAIDA_REC | DATE | Y |  |  |
| 25 | IND_TIPO_REG | VARCHAR2(4) | N |  |  |
| 26 | IND_NOTA_DEVOL | CHAR(1) | Y |  |  |
| 27 | COD_RESP_RET | CHAR(1) | Y |  |  |
| 28 | GRUPO_SITUACAO_A | VARCHAR2(9) | Y |  |  |
| 29 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 30 | GRUPO_SITUACAO_B | VARCHAR2(9) | Y |  |  |
| 31 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 32 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 33 | CFOP | VARCHAR2(4) | Y |  |  |
| 34 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 35 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 36 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 37 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 38 | QUANTIDADE | NUMBER(17,5) | Y |  |  |
| 39 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 40 | QUANTIDADE_CONV | NUMBER(17,5) | Y |  |  |
| 41 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 42 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 43 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 44 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 45 | VLR_UNITARIO | NUMBER(17,2) | Y |  |  |
| 46 | VLR_UNITARIO_CONV | NUMBER(17,2) | Y |  |  |
| 47 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 48 | ALIQ_ICMSS | NUMBER(7,4) | Y |  |  |
| 49 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 50 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 51 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 52 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 53 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 54 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 55 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 56 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 57 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 58 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 59 | NUM_AUTENTIC_NFE_REF | VARCHAR2(80) | Y |  |  |
| 60 | NUM_ITEM_REF | NUMBER(5) | Y |  |  |
| 61 | VL_BC_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 62 | VL_ICMS_SUPORT_ENTR | NUMBER(17,2) | Y |  |  |
| 63 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 64 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 65 | IND_SIMPLES_NAC | VARCHAR2(1) | Y |  |  |
| 66 | IND_SALDO_NEGATIVO | VARCHAR2(1) | Y |  |  |
| 67 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 68 | IND_TP_DOC_ARREC | VARCHAR2(1) | Y |  |  |
| 69 | NUM_GUIA_RECOL | VARCHAR2(16) | Y |  |  |
| 70 | DAT_EMISSAO_GUIA | DATE | Y |  |  |
| 71 | DAT_PAGTO_GUIA | DATE | Y |  |  |
| 72 | COD_ESTADO_RECEITA_EST | VARCHAR2(2) | Y |  |  |
| 73 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 74 | VLR_GUIA_RECOL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTAB_ORIG, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_FISCAL, GRUPO_DOCTO, COD_DOCTO, SERIE_DOCFIS, NUM_DOCFIS, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_ITEM, MOVTO_E_S, IND_TIPO_REG

**Indexes**:
- IX_EST_ST_PR_NF_ENT: (COD_EMPRESA, COD_ESTAB, DATA_PERIODO)

---

## EST_ST_PR_NF_SAI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 4 | DATA_PERIODO | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 10 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 14 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 15 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | N |  |  |
| 17 | MOVTO_E_S | CHAR(1) | N |  |  |
| 18 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 19 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 20 | DATA_EMISSAO | DATE | Y |  |  |
| 21 | DATA_SAIDA_REC | DATE | Y |  |  |
| 22 | IND_TIPO_SAIDA | VARCHAR2(2) | Y |  |  |
| 23 | IND_NOTA_DEVOL | CHAR(1) | Y |  |  |
| 24 | CFOP | VARCHAR2(4) | Y |  |  |
| 25 | QUANTIDADE | NUMBER(17,5) | Y |  |  |
| 26 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 27 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 28 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 29 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 30 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 31 | QUANTIDADE_CONV | NUMBER(17,5) | Y |  |  |
| 32 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 33 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 34 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 35 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 36 | VLR_VENDA | NUMBER(17,2) | Y |  |  |
| 37 | VLR_CRED_SIMPLES_NAC | NUMBER(17,2) | Y |  |  |
| 38 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 39 | IND_TIPO_REG | VARCHAR2(4) | Y |  |  |
| 40 | COD_RESP_RET | VARCHAR2(1) | Y |  |  |
| 41 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 42 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 43 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 44 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 45 | VLR_BASE_ICMSS_INT | NUMBER(17,2) | Y |  |  |
| 46 | ALIQ_ICMSS | NUMBER(7,4) | Y |  |  |
| 47 | VLR_ICMSS_CALC | NUMBER(17,2) | Y |  |  |
| 48 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 49 | COD_DOC_ARREC | VARCHAR2(1) | Y |  |  |
| 50 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 51 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 52 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 53 | NORM_DEV | CHAR(1) | Y |  |  |
| 54 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 55 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 56 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 57 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 58 | NUM_AUTENTIC_NFE_COMP | VARCHAR2(80) | Y |  |  |
| 59 | NUM_ITEM_NFE_COMP | NUMBER(5) | Y |  |  |
| 60 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 61 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 62 | CST_ICMS | VARCHAR2(3) | Y |  |  |
| 63 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 64 | ORIGEM_ALIQ | VARCHAR2(3) | Y |  |  |
| 65 | COD_CEST | VARCHAR2(7) | Y |  |  |
| 66 | IND_SALDO_NEGATIVO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTAB_ORIG, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_FISCAL, GRUPO_DOCTO, COD_DOCTO, SERIE_DOCFIS, NUM_DOCFIS, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_ITEM, MOVTO_E_S

**Indexes**:
- IX_EST_ST_PR_NF_SAI: (COD_EMPRESA, COD_ESTAB, DATA_PERIODO)

---

## EST_ST_PR_X08_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 5 | DATA_FISCAL | DATE | Y |  |  |
| 6 | DATA_EMISSAO | DATE | Y |  |  |
| 7 | DATA_SAIDA_REC | DATE | Y |  |  |
| 8 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 9 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 10 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 15 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 16 | SITUACAO | VARCHAR2(1) | Y |  |  |
| 17 | IND_SITUACAO_ESP | VARCHAR2(1) | Y |  |  |
| 18 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 19 | DISCRI_ITEM | VARCHAR2(46) | Y |  |  |
| 20 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 21 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 22 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 23 | IDENT_MEDIDA_ITEM | NUMBER(12) | Y |  |  |
| 24 | IDENT_UND_PADRAO_ITEM | NUMBER(12) | Y |  |  |
| 25 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 26 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 27 | VLR_CREDITO_MVA_SN | NUMBER(17,2) | Y |  |  |
| 28 | IND_SITUACAO_ESP_ST | VARCHAR2(1) | Y |  |  |
| 29 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 30 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 32 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 33 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 34 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 35 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 36 | IND_TP_DOC_ARREC | VARCHAR2(1) | Y |  |  |
| 37 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 38 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 39 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 40 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 41 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 42 | DAT_DI | DATE | Y |  |  |
| 43 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 44 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 45 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 46 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 47 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 48 | IND_SIMPLES_NAC | VARCHAR2(1) | Y |  |  |
| 49 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 50 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 51 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 52 | VALID_PRODUTO | DATE | Y |  |  |
| 53 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 54 | COD_CEST | VARCHAR2(7) | Y |  |  |
| 55 | IDENT_NBM_PROD | NUMBER(12) | Y |  |  |
| 56 | IDENT_MEDIDA_PROD | NUMBER(12) | Y |  |  |
| 57 | IDENT_UND_PADRAO_PROD | NUMBER(12) | Y |  |  |
| 58 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 59 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 60 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 61 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 62 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 63 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 64 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 65 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 66 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 67 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 68 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 69 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 70 | IDENT_ESTADO | NUMBER | Y |  |  |
| 71 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 72 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 73 | IND_FORNEC_ICMSS | VARCHAR2(1) | Y |  |  |
| 74 | ALIQ_TRIBUTO_ICMS | NUMBER | Y |  |  |
| 75 | ALIQ_TRIBUTO_ICMSS | NUMBER | Y |  |  |
| 76 | VLR_TRIBUTO_ICMS | NUMBER | Y |  |  |
| 77 | VLR_TRIBUTO_ICMSS | NUMBER | Y |  |  |
| 78 | VLR_BASE_ICMS_1 | NUMBER | Y |  |  |
| 79 | VLR_BASE_ICMSS | NUMBER | Y |  |  |
| 80 | VLR_BASE_REDU_ICMSS | NUMBER | Y |  |  |
| 81 | GRUPO_SITUACAO_A | VARCHAR2(9) | Y |  |  |
| 82 | COD_SITUACAO_A | VARCHAR2(1) | Y |  |  |
| 83 | GRUPO_SITUACAO_B | VARCHAR2(9) | Y |  |  |
| 84 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 85 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 86 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 87 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 88 | IND_NOTA_DEVOL | VARCHAR2(1) | Y |  |  |
| 89 | COD_RESP_RET | VARCHAR2(1) | Y |  |  |
| 90 | IND_TIPO_REG | VARCHAR2(4) | Y |  |  |
| 91 | COD_PARAM | NUMBER(3) | Y |  |  |
| 92 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 93 | NUM_GUIA_RECOL | VARCHAR2(16) | Y |  |  |
| 94 | DAT_EMISSAO_GUIA | DATE | Y |  |  |
| 95 | DAT_PAGTO_GUIA | DATE | Y |  |  |
| 96 | COD_ESTADO_RECEITA_EST | VARCHAR2(2) | Y |  |  |
| 97 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 98 | VLR_GUIA_RECOL | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_EST_ST_PR_X08_TEMP: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- IX_EST_ST_PR_X08_TEMP_1: (COD_PRODUTO, IND_PRODUTO, GRUPO_PRODUTO)
- IX_EST_ST_PR_X08_TEMP_2: (GRUPO_PRODUTO, COD_EMPRESA, COD_ESTAB, IND_PRODUTO, COD_PRODUTO)
- IX_EST_ST_PR_X08_TEMP_3: (IDENT_NBM_PROD)

---

## EST_ST_RS_DADOS_INI
**Comment**: Parametrizacao dos Dados Iniciais - Ressarcimento RS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_SUB_APUR | VARCHAR2(1) | Y |  | Valores assumidos: 1, 2, 3, 4, 5, 6. |
| 4 | IND_VAREJISTA | VARCHAR2(1) | Y |  | Valores assumidos: S, N |
| 5 | COD_OPER_APUR_SAIDA_CF | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Saidas de Mercadorias destinadas a Consumidor Final deste Estado (Tabela origem OPERACAO_APURACAO) |
| 6 | DSC_ITEM_APUR_SAIDA_CF | VARCHAR2(150) | Y |  |  |
| 7 | COD_AJUSTE_ICMS_SAIDA_CF | VARCHAR2(8) | Y |  |  |
| 8 | COD_OPER_APUR_SAIDA_UF | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Saidas de Mercadorias destinadas outros Estados ou isentas ou nao tributadas (Tabela origem OPERACAO_APURACAO) |
| 9 | DSC_ITEM_APUR_SAIDA_UF | VARCHAR2(150) | Y |  |  |
| 10 | COD_AJUSTE_ICMS_SAIDA_UF | VARCHAR2(8) | Y |  |  |
| 11 | COD_OPER_APUR_ENTR | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Entrada de Mercadorias (Tabela origem OPERACAO_APURACAO) |
| 12 | DSC_ITEM_APUR_ENTR | VARCHAR2(150) | Y |  |  |
| 13 | COD_AJUSTE_ICMS_ENTR | VARCHAR2(8) | Y |  |  |
| 14 | COD_OPER_APUR_RESS_SUB | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Valor a Restituir na Sub-apuracao (Tabela origem OPERACAO_APURACAO) |
| 15 | DSC_ITEM_APUR_RESS_SUB | VARCHAR2(150) | Y |  |  |
| 16 | COD_AJUSTE_ICMS_RESS_SUB | VARCHAR2(8) | Y |  |  |
| 17 | COD_OPER_APUR_COMPL_SUB | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Valor a Complementar na Sub-apuracao (Tabela origem OPERACAO_APURACAO) |
| 18 | DSC_ITEM_APUR_COMPL_SUB | VARCHAR2(150) | Y |  |  |
| 19 | COD_AJUSTE_ICMS_COMPL_SUB | VARCHAR2(8) | Y |  |  |
| 20 | COD_OPER_APUR_RESS_P9 | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Valor a Restituir na Apuracao do ICMS-ST (Tabela origem OPERACAO_APURACAO) |
| 21 | DSC_ITEM_APUR_RESS_P9 | VARCHAR2(150) | Y |  |  |
| 22 | COD_AJUSTE_ICMS_RESS_P9 | VARCHAR2(8) | Y |  |  |
| 23 | COD_OPER_APUR_COMPL_P9 | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Valor a Complementar na Apuracao do ICMS-ST (Tabela origem OPERACAO_APURACAO) |
| 24 | DSC_ITEM_APUR_COMPL_P9 | VARCHAR2(150) | Y |  |  |
| 25 | COD_AJUSTE_ICMS_COMPL_P9 | VARCHAR2(8) | Y |  |  |
| 26 | COD_OPER_APUR_ESTOQ | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Mercadorias em Estoque (Tabela origem OPERACAO_APURACAO) |
| 27 | DSC_ITEM_APUR_ESTOQ | VARCHAR2(150) | Y |  |  |
| 28 | COD_AJUSTE_ICMS_ESTOQ | VARCHAR2(8) | Y |  |  |
| 29 | COD_OPER_APUR_DEV_SAI | VARCHAR2(5) | Y |  | Codigo da Operacao da Apuracao para Devolucao de Saidas Destinadas a Consumidor Final (Tabela origem OPERACAO_APURACAO) |
| 30 | DSC_ITEM_APUR_DEV_SAI | VARCHAR2(150) | Y |  |  |
| 31 | COD_AJUSTE_ICMS_DEV_SAI | VARCHAR2(8) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_AJUSTE_ICMS_ENTR → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_SAIDA_CF → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_SAIDA_UF → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_RESS_SUB → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_COMPL_SUB → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_RESS_P9 → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_COMPL_P9 → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_ESTOQ → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_DEV_SAI → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## EST_ST_RS_DADOS_INI_IN87

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_FECEP | VARCHAR2(1) | Y | 'N' | Valores assumidos: S, N. |
| 4 | IND_DEV_C186 | VARCHAR2(1) | Y | 'I' | Valores assumidos: I, N. |
| 5 | DAT_DEV_C186 | DATE | Y | TO_DATE('31/12/2020', 'DD/MM/YYYY') |  |
| 6 | IND_VAREJISTA | VARCHAR2(1) | Y | 'S' |  |
| 7 | IDENT_NAT_ESTOQUE | NUMBER(12) | Y |  |  |
| 8 | COD_OPER_APUR_COMPL | VARCHAR2(5) | Y | '002' |  |
| 9 | DSC_ITEM_APUR_COMPL | VARCHAR2(150) | Y |  |  |
| 10 | COD_AJUSTE_ICMS_COMPL | VARCHAR2(8) | Y |  |  |
| 11 | COD_OPER_APUR_REST_ST | VARCHAR2(5) | Y | '006' |  |
| 12 | DSC_ITEM_APUR_REST_ST | VARCHAR2(150) | Y |  |  |
| 13 | COD_AJUSTE_ICMS_REST_ST | VARCHAR2(8) | Y |  |  |
| 14 | COD_OPER_APUR_REST_IC | VARCHAR2(5) | Y | '006' |  |
| 15 | DSC_ITEM_APUR_REST_IC | VARCHAR2(150) | Y |  |  |
| 16 | COD_AJUSTE_ICMS_REST_IC | VARCHAR2(8) | Y |  |  |
| 17 | COD_OPER_APUR_ESTORNO | VARCHAR2(5) | Y | '003' |  |
| 18 | DSC_ITEM_APUR_ESTORNO | VARCHAR2(150) | Y |  |  |
| 19 | COD_AJUSTE_ICMS_ESTORNO | VARCHAR2(8) | Y |  |  |
| 20 | COD_OPER_APUR_COMPENS | VARCHAR2(5) | Y | '006' |  |
| 21 | DSC_ITEM_APUR_COMPENS | VARCHAR2(150) | Y |  |  |
| 22 | COD_AJUSTE_ICMS_COMPENS | VARCHAR2(8) | Y |  |  |
| 23 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 24 | IND_NGER_SLD_NEG | VARCHAR2(1) | Y |  | Valores assumidos: S, N. |
| 25 | IND_FECEP_ST_NDEST_NESCR | VARCHAR2(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_AJUSTE_ICMS_COMPENS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_COMPL → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_ESTORNO → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_REST_IC → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_ICMS_REST_ST → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_ST_RS_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_GER | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 5 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 6 | NUM_COO | VARCHAR2(9) | N |  |  |
| 7 | DATA_EMISSAO | DATE | N |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 9 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 10 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 11 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 12 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 13 | VLR_UNIT_ICMS_OPER_CONV | NUMBER(19,6) | Y |  |  |
| 14 | VLR_UNIT_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 15 | VLR_UNIT_ICMS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 16 | VLR_UNIT_ICMSS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 17 | VLR_UNIT_FCPS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 18 | VLR_UNIT_ICMSS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_FCPS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 20 | VLR_UNIT_ICMSS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 21 | VLR_UNIT_FCPS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 22 | GRUPO_PROD_CF | VARCHAR2(9) | Y |  |  |
| 23 | IND_PROD_CF | CHAR(1) | Y |  |  |
| 24 | COD_PROD_CF | VARCHAR2(60) | Y |  |  |
| 25 | COD_MEDIDA_PROD_CF | VARCHAR2(8) | Y |  |  |
| 26 | COD_NBM_PROD_CF | VARCHAR2(10) | Y |  |  |
| 27 | COD_CEST_PROD_CF | VARCHAR2(7) | Y |  |  |
| 28 | GRUPO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 29 | IND_PROD_PRINC | CHAR(1) | Y |  |  |
| 30 | COD_PROD_PRINC | VARCHAR2(60) | Y |  |  |
| 31 | COD_MEDIDA_PROD_PRINC | VARCHAR2(8) | Y |  |  |
| 32 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |
| 33 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 34 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 35 | QTD_CF | NUMBER(17,6) | Y |  |  |
| 36 | COD_MEDIDA_CF | VARCHAR2(8) | Y |  |  |
| 37 | FAT_CONV_CF | NUMBER(17,6) | Y |  |  |
| 38 | QTD_CONV_CF | NUMBER(17,6) | Y |  |  |
| 39 | VLR_LIQ_ITEM | NUMBER(17,2) | Y |  |  |
| 40 | VLR_BC_ICMS_CF | NUMBER(19,6) | Y |  |  |
| 41 | VLR_UNIT_ICMS_SAI | NUMBER(21,8) | Y |  |  |
| 42 | VLR_UNIT_ICMS_ST_SAI | NUMBER(21,8) | Y |  |  |
| 43 | VLR_UNIT_BC_ST_SAI | NUMBER(21,8) | Y |  |  |
| 44 | VLR_UNIT_FECEP_ST_SAI | NUMBER(21,8) | Y |  |  |
| 45 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 46 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 47 | VLR_UNIT_ICMS_ST_FECEP_SAI | NUMBER(21,8) | Y |  |  |
| 48 | DSC_OBS | VARCHAR2(350) | Y |  |  |
| 49 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, IDENT_MODELO, IDENT_CAIXA_ECF, NUM_COO, DATA_EMISSAO, IDENT_PRODUTO

---

## EST_ST_RS_MEDIA_POND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_GER | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | QTD_CONV_INI | NUMBER(17,6) | Y |  |  |
| 9 | VLR_ICMS_INI_MP | NUMBER(21,8) | Y |  |  |
| 10 | VLR_ICMS_ST_INI_MP | NUMBER(21,8) | Y |  |  |
| 11 | VLR_BC_ST_INI_MP | NUMBER(21,8) | Y |  |  |
| 12 | VLR_FECEP_ST_INI_MP | NUMBER(21,8) | Y |  |  |
| 13 | QTD_CONV_DEV_SAI_MP | NUMBER(17,6) | Y |  |  |
| 14 | VLR_ICMS_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 15 | VLR_ICMS_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 16 | VLR_BC_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 17 | VLR_FECEP_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 18 | QTD_CONV_ENT_MP | NUMBER(17,6) | Y |  |  |
| 19 | VLR_ICMS_ENT_MP | NUMBER(21,8) | Y |  |  |
| 20 | VLR_ICMS_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 21 | VLR_BC_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 22 | VLR_FECEP_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 23 | QTD_CONV_DEV_ENT_MP | NUMBER(17,6) | Y |  |  |
| 24 | VLR_ICMS_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 25 | VLR_ICMS_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 26 | VLR_BC_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 27 | VLR_FECEP_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 28 | QTD_CONV_FIM | NUMBER(17,6) | Y |  |  |
| 29 | VLR_ICMS_FIM_MP | NUMBER(21,8) | Y |  |  |
| 30 | VLR_ICMS_ST_FIM_MP | NUMBER(21,8) | Y |  |  |
| 31 | VLR_BC_ST_FIM_MP | NUMBER(21,8) | Y |  |  |
| 32 | VLR_FECEP_ST_FIM_MP | NUMBER(21,8) | Y |  |  |
| 33 | VLR_UNIT_ICMS_FIM_MP | NUMBER(21,8) | Y |  |  |
| 34 | VLR_UNIT_ICMS_ST_FIM_MP | NUMBER(21,8) | Y |  |  |
| 35 | VLR_UNIT_BC_ST_FIM_MP | NUMBER(21,8) | Y |  |  |
| 36 | VLR_UNIT_FECEP_ST_FIM_MP | NUMBER(21,8) | Y |  |  |
| 37 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 38 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 39 | VLR_UNIT_ICMS_ST_FECEP_FIM_MP | NUMBER(21,8) | Y |  |  |
| 40 | QTD_CONV_SAI_DIA | NUMBER(17,6) | Y |  |  |
| 41 | QTD_CONV_SAI_MP | NUMBER(17,6) | Y |  |  |
| 42 | IND_UTIL_DEV_ZERA | VARCHAR2(1) | Y |  |  |
| 43 | QTD_CONV_DEV_ZERA | NUMBER(17,6) | Y |  |  |
| 44 | VLR_ICMS_DEV_ZERA | NUMBER(21,8) | Y |  |  |
| 45 | VLR_ICMS_ST_DEV_ZERA | NUMBER(21,8) | Y |  |  |
| 46 | VLR_BC_ST_DEV_ZERA | NUMBER(21,8) | Y |  |  |
| 47 | VLR_FECEP_ST_DEV_ZERA | NUMBER(21,8) | Y |  |  |
| 48 | VLR_ICMS_ST_FECEP_DEV_ZERA | NUMBER(21,8) | Y |  |  |
| 49 | IND_SALDO_NEGATIVO | VARCHAR2(1) | Y |  | Valores assumidos: S, N. |

**PK**: COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, DATA, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**Indexes**:
- IX_EST_ST_RS_MEDIA_POND_01: (COD_ESTAB_GER, COD_ESTAB, DATA, IND_GRAVACAO, COD_EMPRESA)
- IX_EST_ST_RS_MEDIA_POND_02: (COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)
- IX_EST_ST_RS_MEDIA_POND_03: (COD_EMPRESA, COD_ESTAB, COD_ESTAB_GER, DATA)

---

## EST_ST_RS_NF_DEV_ENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_GER | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_FISCAL | DATE | Y |  |  |
| 5 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 6 | NORM_DEV | CHAR(1) | Y |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 13 | ESPECIE_DOCTO_DEV | VARCHAR2(1) | Y |  |  |
| 14 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 15 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 16 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 17 | IDENT_DOCTO_REF | NUMBER(12) | Y |  |  |
| 18 | DATA_FISCAL_REF | DATE | Y |  |  |
| 19 | IDENT_FIS_JUR_REF | NUMBER(12) | Y |  |  |
| 20 | NUM_ITEM_DOC_REF | NUMBER(5) | Y |  |  |
| 21 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 22 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 23 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 24 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 25 | VLR_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 26 | VLR_UNIT_BC_ICMSS_ENT | NUMBER(19,6) | Y |  |  |
| 27 | VLR_UNIT_ICMSS_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 28 | VLR_UNIT_FCP_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 29 | GRUPO_PROD_NF_DEV | VARCHAR2(9) | Y |  |  |
| 30 | IND_PROD_NF_DEV | CHAR(1) | Y |  |  |
| 31 | COD_PROD_NF_DEV | VARCHAR2(60) | Y |  |  |
| 32 | COD_MEDIDA_PROD_NF_DEV | VARCHAR2(8) | Y |  |  |
| 33 | COD_NBM_PROD_NF_DEV | VARCHAR2(10) | Y |  |  |
| 34 | COD_CEST_PROD_NF_DEV | VARCHAR2(7) | Y |  |  |
| 35 | GRUPO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 36 | IND_PROD_PRINC | CHAR(1) | Y |  |  |
| 37 | COD_PROD_PRINC | VARCHAR2(60) | Y |  |  |
| 38 | COD_MEDIDA_PROD_PRINC | VARCHAR2(8) | Y |  |  |
| 39 | QTD_NF_DEV | NUMBER(17,6) | Y |  |  |
| 40 | QTD_CONV_X08_NF_DEV | NUMBER(17,6) | Y |  |  |
| 41 | COD_MEDIDA_NF_DEV | VARCHAR2(8) | Y |  |  |
| 42 | FAT_CONV_NF_DEV | NUMBER(17,6) | Y |  |  |
| 43 | QTD_CONV_NF_DEV | NUMBER(17,6) | Y |  |  |
| 44 | QTD_NF_ENT | NUMBER(17,6) | Y |  |  |
| 45 | QTD_CONV_X08_NF_ENT | NUMBER(17,6) | Y |  |  |
| 46 | COD_MEDIDA_NF_ENT | VARCHAR2(8) | Y |  |  |
| 47 | FAT_CONV_NF_ENT | NUMBER(17,6) | Y |  |  |
| 48 | QTD_CONV_NF_ENT | NUMBER(17,6) | Y |  |  |
| 49 | VLR_CONTAB_ENT | NUMBER(17,2) | Y |  |  |
| 50 | VLR_ICMS_ENT | NUMBER(17,2) | Y |  |  |
| 51 | VLR_BC_ST_ENT | NUMBER(17,2) | Y |  |  |
| 52 | VLR_ICMS_ST_ENT | NUMBER(17,2) | Y |  |  |
| 53 | VLR_FECEP_ST_ENT | NUMBER(17,2) | Y |  |  |
| 54 | VLR_UNIT_ICMS_INV | NUMBER(19,6) | Y |  |  |
| 55 | VLR_UNIT_ICMS_ST_INV | NUMBER(19,6) | Y |  |  |
| 56 | VLR_UNIT_BC_ST_INV | NUMBER(19,6) | Y |  |  |
| 57 | VLR_UNIT_FECEP_ST_INV | NUMBER(19,6) | Y |  |  |
| 58 | QTD_CONV_DEV_ENT_MP | NUMBER(17,6) | Y |  |  |
| 59 | VLR_UNIT_ICMS_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 60 | VLR_UNIT_ICMS_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 61 | VLR_UNIT_BC_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 62 | VLR_UNIT_FECEP_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 63 | VLR_ICMS_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 64 | VLR_ICMS_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 65 | VLR_BC_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 66 | VLR_FECEP_ST_DEV_ENT_MP | NUMBER(21,8) | Y |  |  |
| 67 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 68 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**Indexes**:
- IX_EST_ST_RS_NF_DEV_ENT_02: (COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, COD_PROD_PRINC, GRUPO_PROD_PRINC, IND_PROD_PRINC, DATA_FISCAL)
- UK_EST_ST_RS_NF_DEV_ENT (UNIQUE): (COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, ESPECIE_DOCTO_DEV, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, IDENT_DOCTO_REF, DATA_FISCAL_REF, IDENT_FIS_JUR_REF, NUM_ITEM_DOC_REF)

---

## EST_ST_RS_NF_DEV_SAI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_GER | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_FISCAL | DATE | Y |  |  |
| 5 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 6 | NORM_DEV | CHAR(1) | Y |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 13 | ESPECIE_DOCTO_DEV | VARCHAR2(1) | Y |  |  |
| 14 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 15 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 16 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 17 | IDENT_DOCTO_REF | NUMBER(12) | Y |  |  |
| 18 | DATA_FISCAL_REF | DATE | Y |  |  |
| 19 | IDENT_FIS_JUR_REF | NUMBER(12) | Y |  |  |
| 20 | IDENT_MODELO_REF | NUMBER(12) | Y |  |  |
| 21 | IDENT_CAIXA_ECF | NUMBER(12) | Y |  |  |
| 22 | NUM_COO_REF | VARCHAR2(9) | Y |  |  |
| 23 | DATA_EMISSAO_REF | DATE | Y |  |  |
| 24 | NUM_EQUIP_REF | NUMBER(9) | Y |  |  |
| 25 | NUM_CUPOM_REF | VARCHAR2(6) | Y |  |  |
| 26 | NUM_ITEM_DOC_REF | NUMBER(5) | Y |  |  |
| 27 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 28 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 29 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 30 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 31 | VLR_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 32 | VLR_UNIT_ICMS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 33 | VLR_UNIT_ICMSS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 34 | VLR_UNIT_FCP_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 35 | VLR_UNIT_ICMS_OPER_SAI | NUMBER(19,6) | Y |  |  |
| 36 | VLR_UNIT_ICMSS_REST_SAI | NUMBER(19,6) | Y |  |  |
| 37 | VLR_UNIT_FCP_REST_SAI | NUMBER(19,6) | Y |  |  |
| 38 | VLR_UNIT_ICMSS_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 39 | VLR_UNIT_FCP_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 40 | GRUPO_PROD_NF_DEV | VARCHAR2(9) | Y |  |  |
| 41 | IND_PROD_NF_DEV | CHAR(1) | Y |  |  |
| 42 | COD_PROD_NF_DEV | VARCHAR2(60) | Y |  |  |
| 43 | COD_MEDIDA_PROD_NF_DEV | VARCHAR2(8) | Y |  |  |
| 44 | COD_NBM_PROD_NF_DEV | VARCHAR2(10) | Y |  |  |
| 45 | COD_CEST_PROD_NF_DEV | VARCHAR2(7) | Y |  |  |
| 46 | GRUPO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 47 | IND_PROD_PRINC | CHAR(1) | Y |  |  |
| 48 | COD_PROD_PRINC | VARCHAR2(60) | Y |  |  |
| 49 | COD_MEDIDA_PROD_PRINC | VARCHAR2(8) | Y |  |  |
| 50 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |
| 51 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 52 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 53 | QTD_NF_DEV | NUMBER(17,6) | Y |  |  |
| 54 | QTD_CONV_X08_NF_DEV | NUMBER(17,6) | Y |  |  |
| 55 | COD_MEDIDA_NF_DEV | VARCHAR2(8) | Y |  |  |
| 56 | FAT_CONV_NF_DEV | NUMBER(17,6) | Y |  |  |
| 57 | QTD_CONV_NF_DEV | NUMBER(17,6) | Y |  |  |
| 58 | QTD_REF_DEV | NUMBER(17,6) | Y |  |  |
| 59 | QTD_CONV_REF_DEV | NUMBER(17,6) | Y |  |  |
| 60 | QTD_NF_SAI | NUMBER(17,6) | Y |  |  |
| 61 | QTD_CONV_X08_NF_SAI | NUMBER(17,6) | Y |  |  |
| 62 | COD_MEDIDA_NF_SAI | VARCHAR2(8) | Y |  |  |
| 63 | FAT_CONV_NF_SAI | NUMBER(17,6) | Y |  |  |
| 64 | QTD_CONV_NF_SAI | NUMBER(17,6) | Y |  |  |
| 65 | VLR_CONTAB_SAI | NUMBER(17,2) | Y |  |  |
| 66 | VLR_BC_ICMS_SAI | NUMBER(19,6) | Y |  |  |
| 67 | QTD_CUPOM | NUMBER(17,6) | Y |  |  |
| 68 | COD_MEDIDA_NF_CUPOM | VARCHAR2(8) | Y |  |  |
| 69 | FAT_CONV_NF_CUPOM | NUMBER(17,6) | Y |  |  |
| 70 | QTD_CONV_NF_CUPOM | NUMBER(17,6) | Y |  |  |
| 71 | VLR_CONTAB_CUPOM | NUMBER(17,2) | Y |  |  |
| 72 | VLR_BC_ICMS_CUPOM | NUMBER(19,6) | Y |  |  |
| 73 | VLR_UNIT_ICMS_SAI | NUMBER(21,8) | Y |  |  |
| 74 | VLR_UNIT_ICMS_ST_SAI | NUMBER(21,8) | Y |  |  |
| 75 | VLR_UNIT_BC_ST_SAI | NUMBER(21,8) | Y |  |  |
| 76 | VLR_UNIT_FECEP_ST_SAI | NUMBER(21,8) | Y |  |  |
| 77 | NUM_DOCFIS_NF_ENT | VARCHAR2(12) | Y |  |  |
| 78 | SERIE_DOCFIS_NF_ENT | VARCHAR2(3) | Y |  |  |
| 79 | SUB_SERIE_DOCFIS_NF_ENT | VARCHAR2(2) | Y |  |  |
| 80 | DATA_FISCAL_NF_ENT | DATE | Y |  |  |
| 81 | NUM_ITEM_NF_ENT | NUMBER(5) | Y |  |  |
| 82 | QTD_NF_ENT | NUMBER(17,6) | Y |  |  |
| 83 | QTD_CONV_X08_NF_ENT | NUMBER(17,6) | Y |  |  |
| 84 | COD_MEDIDA_NF_ENT | VARCHAR2(8) | Y |  |  |
| 85 | FAT_CONV_NF_ENT | NUMBER(17,6) | Y |  |  |
| 86 | QTD_CONV_NF_ENT | NUMBER(17,6) | Y |  |  |
| 87 | VLR_ICMS_NF_ENT | NUMBER(17,2) | Y |  |  |
| 88 | VLR_ICMS_ST_NF_ENT | NUMBER(17,2) | Y |  |  |
| 89 | VLR_BC_ST_NF_ENT | NUMBER(17,2) | Y |  |  |
| 90 | VLR_FECEP_ST_NF_ENT | NUMBER(17,2) | Y |  |  |
| 91 | QTD_CONV_DEV_SAI_MP | NUMBER(17,6) | Y |  |  |
| 92 | VLR_UNIT_ICMS_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 93 | VLR_UNIT_ICMS_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 94 | VLR_UNIT_BC_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 95 | VLR_UNIT_FECEP_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 96 | VLR_ICMS_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 97 | VLR_ICMS_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 98 | VLR_BC_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 99 | VLR_FECEP_ST_DEV_SAI_MP | NUMBER(21,8) | Y |  |  |
| 100 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 101 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 102 | VLR_UNIT_ICMS_ST_FECEP_SAI | NUMBER(21,8) | Y |  |  |
| 103 | COD_PARAM | NUMBER(3) | Y |  |  |
| 104 | DSC_OBS | VARCHAR2(350) | Y |  |  |
| 105 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |

**Indexes**:
- UK_EST_ST_RS_NF_DEV_SAI (UNIQUE): (COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, ESPECIE_DOCTO_DEV, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, IDENT_DOCTO_REF, DATA_FISCAL_REF, IDENT_FIS_JUR_REF, IDENT_MODELO_REF, IDENT_CAIXA_ECF, NUM_COO_REF, DATA_EMISSAO_REF, NUM_EQUIP_REF, NUM_CUPOM_REF, NUM_ITEM_DOC_REF)

---

## EST_ST_RS_NF_ENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_GER | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 13 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 14 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 15 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 16 | VLR_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 17 | IND_RESP_RET_ENT | VARCHAR2(1) | Y |  |  |
| 18 | VLR_UNIT_BC_ICMSS_ENT | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_ICMSS_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 20 | VLR_UNIT_FCP_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 21 | GRUPO_PROD_NF | VARCHAR2(9) | Y |  |  |
| 22 | IND_PROD_NF | CHAR(1) | Y |  |  |
| 23 | COD_PROD_NF | VARCHAR2(60) | Y |  |  |
| 24 | COD_MEDIDA_PROD_NF | VARCHAR2(8) | Y |  |  |
| 25 | COD_NBM_PROD_NF | VARCHAR2(10) | Y |  |  |
| 26 | COD_CEST_PROD_NF | VARCHAR2(7) | Y |  |  |
| 27 | GRUPO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 28 | IND_PROD_PRINC | CHAR(1) | Y |  |  |
| 29 | COD_PROD_PRINC | VARCHAR2(60) | Y |  |  |
| 30 | COD_MEDIDA_PROD_PRINC | VARCHAR2(8) | Y |  |  |
| 31 | QTD_NF_ENT | NUMBER(17,6) | Y |  |  |
| 32 | QTD_CONV_X08_NF_ENT | NUMBER(17,6) | Y |  |  |
| 33 | COD_MEDIDA_NF_ENT | VARCHAR2(8) | Y |  |  |
| 34 | FAT_CONV_NF_ENT | NUMBER(17,6) | Y |  |  |
| 35 | QTD_CONV_NF_ENT | NUMBER(17,6) | Y |  |  |
| 36 | VLR_CONTAB_ENT | NUMBER(17,2) | Y |  |  |
| 37 | VLR_ICMS_ENT | NUMBER(17,2) | Y |  |  |
| 38 | VLR_BC_ST_ENT | NUMBER(17,2) | Y |  |  |
| 39 | VLR_ICMS_ST_ENT | NUMBER(17,2) | Y |  |  |
| 40 | VLR_FECEP_ST_ENT | NUMBER(17,2) | Y |  |  |
| 41 | QTD_CONV_ENT_MP | NUMBER(17,6) | Y |  |  |
| 42 | VLR_UNIT_ICMS_ENT_MP | NUMBER(21,8) | Y |  |  |
| 43 | VLR_UNIT_ICMS_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 44 | VLR_UNIT_BC_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 45 | VLR_UNIT_FECEP_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 46 | VLR_ICMS_ENT_MP | NUMBER(21,8) | Y |  |  |
| 47 | VLR_ICMS_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 48 | VLR_BC_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 49 | VLR_FECEP_ST_ENT_MP | NUMBER(21,8) | Y |  |  |
| 50 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 51 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**Indexes**:
- IX_EST_ST_RS_NF_ENT_01: (COD_EMPRESA, COD_ESTAB, COD_ESTAB_GER, DATA_FISCAL)
- IX_EST_ST_RS_NF_ENT_02: (COD_EMPRESA, COD_ESTAB, GRUPO_PROD_PRINC, IND_PROD_PRINC, COD_PROD_PRINC, DATA_FISCAL)

---

## EST_ST_RS_NF_SAI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_GER | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 13 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 14 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 15 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 16 | VLR_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 17 | COD_MOTIVO_SAI | VARCHAR2(5) | Y |  |  |
| 18 | VLR_UNIT_ICMS_OPER_SAI | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_ICMS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 20 | VLR_UNIT_ICMSS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 21 | VLR_UNIT_FCP_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 22 | VLR_UNIT_ICMSS_REST_SAI | NUMBER(19,6) | Y |  |  |
| 23 | VLR_UNIT_FCP_REST_SAI | NUMBER(19,6) | Y |  |  |
| 24 | VLR_UNIT_ICMSS_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 25 | VLR_UNIT_FCP_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 26 | GRUPO_PROD_NF | VARCHAR2(9) | Y |  |  |
| 27 | IND_PROD_NF | CHAR(1) | Y |  |  |
| 28 | COD_PROD_NF | VARCHAR2(60) | Y |  |  |
| 29 | COD_MEDIDA_PROD_NF | VARCHAR2(8) | Y |  |  |
| 30 | COD_NBM_PROD_NF | VARCHAR2(10) | Y |  |  |
| 31 | COD_CEST_PROD_NF | VARCHAR2(7) | Y |  |  |
| 32 | GRUPO_PROD_PRINC | VARCHAR2(9) | Y |  |  |
| 33 | IND_PROD_PRINC | CHAR(1) | Y |  |  |
| 34 | COD_PROD_PRINC | VARCHAR2(60) | Y |  |  |
| 35 | COD_MEDIDA_PROD_PRINC | VARCHAR2(8) | Y |  |  |
| 36 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |
| 37 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 38 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 39 | QTD_NF_SAI | NUMBER(17,6) | Y |  |  |
| 40 | QTD_CONV_X08_NF_SAI | NUMBER(17,6) | Y |  |  |
| 41 | COD_MEDIDA_NF_SAI | VARCHAR2(8) | Y |  |  |
| 42 | FAT_CONV_NF_SAI | NUMBER(17,6) | Y |  |  |
| 43 | QTD_CONV_NF_SAI | NUMBER(17,6) | Y |  |  |
| 44 | VLR_CONTAB_SAI | NUMBER(17,2) | Y |  |  |
| 45 | VLR_BC_ICMS_SAI | NUMBER(19,6) | Y |  |  |
| 46 | VLR_UNIT_ICMS_SAI | NUMBER(21,8) | Y |  |  |
| 47 | VLR_UNIT_ICMS_ST_SAI | NUMBER(21,8) | Y |  |  |
| 48 | VLR_UNIT_BC_ST_SAI | NUMBER(21,8) | Y |  |  |
| 49 | VLR_UNIT_FECEP_ST_SAI | NUMBER(21,8) | Y |  |  |
| 50 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 51 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 52 | VLR_UNIT_ICMS_ST_FECEP_SAI | NUMBER(21,8) | Y |  |  |
| 53 | DSC_OBS | VARCHAR2(350) | Y |  |  |
| 54 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**Indexes**:
- IX_EST_ST_RS_NF_SAI_01: (COD_EMPRESA, COD_ESTAB_GER, COD_ESTAB, GRUPO_PROD_NF, IND_PROD_NF, COD_PROD_NF)

---

## EST_ST_RS_PROD_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | VALID_INICIAL | DATE | N |  |  |
| 5 | VALID_FINAL | DATE | Y |  |  |
| 6 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 7 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |
| 8 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, VALID_INICIAL

---

## EST_ST_SC_APUR_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | VLR_ST_RESTITUIR | NUMBER(17,2) | Y |  |  |
| 5 | VLR_ST_COMPLEMENTAR | NUMBER(17,3) | Y |  |  |
| 6 | VLR_ST_RESTITUICAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ST_RESSARCIMENTO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ST_COMPLEMENTO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMS_OP_PROPRIA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CREDITO_APUR | NUMBER(17,2) | Y |  |  |
| 11 | VLR_COMPLEMENTO_APUR | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO

---

## EST_ST_SC_APUR_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | DESCR_PROD | VARCHAR2(50) | Y |  |  |
| 8 | QTD_VENDA_CF | NUMBER(17,5) | Y |  |  |
| 9 | VLR_VENDA_CF | NUMBER(17,2) | Y |  |  |
| 10 | VLR_MEDIO_UNIT_CF | NUMBER(17,3) | Y |  |  |
| 11 | VLR_BASE_ST_PROP | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ST_DIF_MAIOR | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ST_DIF_MENOR | NUMBER(17,2) | Y |  |  |
| 14 | ALIQ_ICMSS_EF | NUMBER(7,4) | Y |  |  |
| 15 | VLR_ICMS_ST_REST | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS_ST_COMP | NUMBER(17,2) | Y |  |  |
| 17 | QTD_OUTRAS_UF | NUMBER(17,5) | Y |  |  |
| 18 | VLR_ICMS_OUTRAS_UF | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS_ST_OUTRAS_UF | NUMBER(17,2) | Y |  |  |
| 20 | QTD_VENDA_SIMPLES_NAC | NUMBER(17,5) | Y |  |  |
| 21 | VLR_CRED_SIMPLES_NAC | NUMBER(17,2) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## EST_ST_SC_CONV_MEDIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 8 | COD_MEDIDA_ORIG | VARCHAR2(8) | N |  |  |
| 9 | COD_MEDIDA_DEST | VARCHAR2(8) | N |  |  |
| 10 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_MEDIDA, COD_MEDIDA_ORIG, COD_MEDIDA_DEST

---

## EST_ST_SC_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PERFIL | VARCHAR2(1) | N |  |  |
| 4 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 5 | IND_COD_PROD | VARCHAR2(1) | Y |  |  |
| 6 | IND_DESC_PROD | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_ST_SC_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 4 | DATA_PERIODO | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | GRUPO_MEDIDA_ECF | VARCHAR2(9) | N |  |  |
| 9 | COD_MEDIDA_ECF | VARCHAR2(8) | N |  |  |
| 10 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | QUANTIDADE | NUMBER(17,5) | Y |  |  |
| 13 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 14 | QUANTIDADE_CONV | NUMBER(17,5) | Y |  |  |
| 15 | VLR_VENDA | NUMBER(17,2) | Y |  |  |
| 16 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 17 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 18 | IND_TIPO_REG | VARCHAR2(4) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | ALIQ_ICMSS_EF | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTAB_ORIG, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_MEDIDA_ECF, COD_MEDIDA_ECF

---

## EST_ST_SC_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 4 | DATA_PERIODO | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 10 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 14 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 15 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | N |  |  |
| 17 | MOVTO_E_S | CHAR(1) | N |  |  |
| 18 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 19 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 20 | DATA_EMISSAO | DATE | Y |  |  |
| 21 | DATA_SAIDA_REC | DATE | Y |  |  |
| 22 | IND_TIPO_SAIDA | VARCHAR2(2) | Y |  |  |
| 23 | IND_NOTA_DEVOL | CHAR(1) | Y |  |  |
| 24 | CFOP | VARCHAR2(4) | Y |  |  |
| 25 | QUANTIDADE | NUMBER(17,5) | Y |  |  |
| 26 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 27 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 28 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 29 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 30 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 31 | QUANTIDADE_CONV | NUMBER(17,5) | Y |  |  |
| 32 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 33 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 34 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 35 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 36 | VLR_VENDA | NUMBER(17,2) | Y |  |  |
| 37 | VLR_CRED_SIMPLES_NAC | NUMBER(17,2) | Y |  |  |
| 38 | ALIQ_INTERNA | NUMBER(7,4) | Y |  |  |
| 39 | IND_TIPO_REG | VARCHAR2(4) | Y |  |  |
| 40 | COD_RESP_RET | VARCHAR2(1) | Y |  |  |
| 41 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 42 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 43 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 44 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 45 | VLR_BASE_ICMSS_INT | NUMBER(17,2) | Y |  |  |
| 46 | ALIQ_ICMSS | NUMBER(7,4) | Y |  |  |
| 47 | ALIQ_ICMSS_EF | NUMBER(7,4) | Y |  |  |
| 48 | VLR_ICMSS_CALC | NUMBER(17,2) | Y |  |  |
| 49 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 50 | COD_DOC_ARREC | VARCHAR2(1) | Y |  |  |
| 51 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 52 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 53 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 54 | NORM_DEV | CHAR(1) | Y |  |  |
| 55 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 56 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 57 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 58 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |

**Indexes**:
- IX_EST_ST_SC_NF_01: (COD_EMPRESA, COD_ESTAB, DATA_PERIODO, IND_TIPO_REG)
- UK_EST_ST_SC_NF (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_ESTAB_ORIG, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_FISCAL, GRUPO_DOCTO, COD_DOCTO, SERIE_DOCFIS, NUM_DOCFIS, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_ITEM, MOVTO_E_S, IND_NOTA_DEVOL)

---

## EST_ST_SC_NF_AJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 4 | DATA_PERIODO | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 10 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 14 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 15 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | N |  |  |
| 17 | MOVTO_E_S | CHAR(1) | N |  |  |
| 18 | NUM_AUTENTIC_NFE_AJ | VARCHAR2(80) | N |  |  |
| 19 | NUM_ITEM_NFE_AJ | NUMBER(5) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTAB_ORIG, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_FISCAL, GRUPO_DOCTO, COD_DOCTO, SERIE_DOCFIS, NUM_DOCFIS, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_ITEM, MOVTO_E_S, NUM_AUTENTIC_NFE_AJ, NUM_ITEM_NFE_AJ

---

## EST_ST_SC_NF_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 4 | DATA_PERIODO | DATE | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |
| 9 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 10 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 14 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 15 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 16 | NUM_ITEM | NUMBER(5) | N |  |  |
| 17 | MOVTO_E_S | CHAR(1) | N |  |  |
| 18 | NUM_AUTENTIC_NFE_COMP | VARCHAR2(80) | N |  |  |
| 19 | NUM_ITEM_NFE_COMP | NUMBER(5) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTAB_ORIG, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_FISCAL, GRUPO_DOCTO, COD_DOCTO, SERIE_DOCFIS, NUM_DOCFIS, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_ITEM, MOVTO_E_S, NUM_AUTENTIC_NFE_COMP, NUM_ITEM_NFE_COMP

---

## EST_ST_SC_VLR_UNIT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | QUANTIDADE_TOTAL | NUMBER(17,5) | Y |  |  |
| 8 | VLR_BASE_INT_ST | NUMBER(17,2) | Y |  |  |
| 9 | VLR_MEDIO_UNIT_BASE_ST | NUMBER(17,3) | Y |  |  |
| 10 | VLR_TOTAL_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_MEDIO_UNIT_ICMS | NUMBER(17,3) | Y |  |  |
| 12 | VLR_TOTAL_ST | NUMBER(17,2) | Y |  |  |
| 13 | VLR_MEDIO_UNIT_ST | NUMBER(17,3) | Y |  |  |
| 14 | DESCR_PROD | VARCHAR2(50) | Y |  |  |
| 15 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 16 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 17 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 18 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | QUANTIDADE_TOTAL_2121 | NUMBER(17,5) | Y |  |  |
| 21 | QUANTIDADE_TOTAL_MERC_2121 | NUMBER(17,5) | Y |  |  |
| 22 | VLR_BASE_INT_ST_VLM_2121 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_MEDIO_UNIT_ST_2121 | NUMBER(17,3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## EST_ST_SP_DADOS_INICIAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_COD_ITEM | CHAR(1) | Y |  |  |
| 4 | IND_COD_PFJ | CHAR(1) | Y |  |  |
| 5 | IND_GER_REG_0205 | VARCHAR2(1) | Y |  |  |
| 6 | IND_GER_ECF_CONSOL | VARCHAR2(1) | Y |  |  |
| 7 | IND_NGER_SLD_NEG | VARCHAR2(1) | Y |  |  |
| 8 | IND_FECEP | VARCHAR2(1) | Y | 'N' | Valores assumidos: S, N. |
| 9 | IND_GER_0150_CNPJ | CHAR(1) | Y |  |  |
| 10 | IND_VL_CONF_SAI_TPC_33613 | VARCHAR2(1) | Y | 'N' |  |
| 11 | IND_OPER_VENDA_CF | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## EST_ST_SP_DWT_TMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | DATE | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 9 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 10 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 11 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 15 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 17 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 21 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS | NUMBER(17,2) | Y |  |  |

---

## EST_ST_SP_NOTA_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | NUM_SERIE_ECF | VARCHAR2(21) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | NUM_ITEM | NUMBER(5) | N |  |  |
| 12 | MOVTO_E_S | CHAR(1) | N |  |  |
| 13 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 14 | IND_ORIGEM_MOV | CHAR(1) | Y |  |  |
| 15 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 16 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 17 | IND_NOTA_DEVOL | CHAR(1) | Y |  |  |
| 18 | CFOP | VARCHAR2(4) | Y |  |  |
| 19 | COD_ENQ_LEGAL | CHAR(1) | Y |  |  |
| 20 | NUM_ORDEM | NUMBER(9) | Y |  |  |
| 21 | QUANTIDADE | NUMBER(17,3) | Y |  |  |
| 22 | VLR_ICMS_ENT | NUMBER(17,2) | Y |  |  |
| 23 | VLR_UNIT | NUMBER(19,6) | Y |  |  |
| 24 | VLR_SAIDA | NUMBER(17,2) | Y |  |  |
| 25 | VLR_CONF_SAIDA | NUMBER(17,2) | Y |  |  |
| 26 | VLR_CONF_ENT | NUMBER(17,2) | Y |  |  |
| 27 | QTDE_SALDO | NUMBER(17,3) | Y |  |  |
| 28 | VLR_UNIT_SALDO | NUMBER(19,6) | Y |  |  |
| 29 | VLR_TOT_SALDO | NUMBER(17,2) | Y |  |  |
| 30 | VLR_RESSARC | NUMBER(17,2) | Y |  |  |
| 31 | VLR_COMPL | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMS_PROP | NUMBER(17,2) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 34 | COD_ESTAB_ORIG | VARCHAR2(6) | N |  |  |
| 35 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 36 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 37 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 38 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 39 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 40 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 41 | VLR_CONF_SAIDA_ORIG | NUMBER(17,2) | Y |  |  |
| 42 | VLR_CONF_ENT_ORIG | NUMBER(17,2) | Y |  |  |
| 43 | IND_SALDO_NEGATIVO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO, IDENT_PRODUTO, DATA_FISCAL, NUM_SERIE_ECF, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, NUM_ITEM, MOVTO_E_S, COD_ESTAB_ORIG

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_EST_SP_NOTA_ECF: (COD_EMPRESA, COD_ESTAB, DATA_PERIODO, COD_ENQ_LEGAL)
- IX_EST_SP_NT_ECF_02: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, NUM_ITEM, IDENT_PRODUTO, IDENT_FIS_JUR, DATA_PERIODO)
- IX_FK_SAF_3131: (IDENT_FIS_JUR)

---

## EST_ST_SP_NOTA_ECF_CONF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | NUM_SERIE_ECF | VARCHAR2(21) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | NUM_ITEM | NUMBER(5) | N |  |  |
| 12 | MOVTO_E_S | CHAR(1) | N |  |  |
| 13 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 14 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 15 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | N |  |  |
| 16 | DATA_FISCAL_REF | DATE | N |  |  |
| 17 | IDENT_DOCTO_REF | NUMBER(12) | N |  |  |
| 18 | IDENT_FIS_JUR_REF | NUMBER(12) | N |  |  |
| 19 | NUM_ITEM_REF | NUMBER(5) | N |  |  |
| 20 | QUANTIDADE | NUMBER(17,3) | Y |  |  |
| 21 | COD_ENQ_LEGAL | CHAR(1) | Y |  |  |
| 22 | IDENT_PRODUTO_REF | NUMBER(12) | Y |  |  |
| 23 | COD_ESTAB_REF | VARCHAR2(6) | Y |  |  |
| 24 | QUANTIDADE_REF | NUMBER(17,3) | Y |  |  |
| 25 | QUANTIDADE_REF_CONV | NUMBER(17,3) | Y |  |  |
| 26 | VLR_ICMS_REF | NUMBER(17,2) | Y |  |  |
| 27 | QUANTIDADE_REF_UTIL | NUMBER(17,3) | Y |  |  |
| 28 | VLR_MEDIO_CALC | NUMBER(17,2) | Y |  |  |
| 29 | VLR_CONF_NF | NUMBER(17,2) | Y |  |  |
| 30 | QUANTIDADE_DEV_REF | NUMBER(17,3) | Y |  |  |
| 31 | COD_EMPRESA_ENT | VARCHAR2(3) | Y |  |  |
| 32 | COD_ESTAB_ENT | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO, IDENT_PRODUTO, DATA_FISCAL, NUM_SERIE_ECF, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, NUM_ITEM, MOVTO_E_S, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, DATA_FISCAL_REF, IDENT_DOCTO_REF, IDENT_FIS_JUR_REF, NUM_ITEM_REF

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_EST_ST_SP_NF_ECF_C_01: (COD_EMPRESA, COD_ESTAB, DATA_PERIODO, IDENT_PRODUTO, DATA_FISCAL, NUM_SERIE_ECF, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, NUM_ITEM, MOVTO_E_S)
- IX_FK_SAF_3162: (IDENT_FIS_JUR)

---

## EST_ST_SP_NOTA_ECF_ENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PERIODO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | NUM_SERIE_ECF | VARCHAR2(21) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | NUM_ITEM | NUMBER(5) | N |  |  |
| 12 | MOVTO_E_S | CHAR(1) | N |  |  |
| 13 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 14 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 15 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | N |  |  |
| 16 | DATA_FISCAL_REF | DATE | N |  |  |
| 17 | IDENT_DOCTO_REF | NUMBER(12) | N |  |  |
| 18 | IDENT_FIS_JUR_REF | NUMBER(12) | N |  |  |
| 19 | NUM_ITEM_REF | NUMBER(5) | N |  |  |
| 20 | QUANTIDADE | NUMBER(17,3) | Y |  |  |
| 21 | COD_ENQ_LEGAL | CHAR(1) | Y |  |  |
| 22 | IDENT_PRODUTO_REF | NUMBER(12) | Y |  |  |
| 23 | COD_ESTAB_REF | VARCHAR2(6) | Y |  |  |
| 24 | QUANTIDADE_REF | NUMBER(17,3) | Y |  |  |
| 25 | QUANTIDADE_REF_CONV | NUMBER(17,3) | Y |  |  |
| 26 | VLR_ICMS_REF | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ICMSS_REF | NUMBER(17,2) | Y |  |  |
| 28 | VLR_ICMSS_FECEP_REF | NUMBER(17,2) | Y |  |  |
| 29 | QUANTIDADE_REF_UTIL | NUMBER(17,3) | Y |  |  |
| 30 | VLR_MEDIO_ICMS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_MEDIO_ICMSS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_MEDIO_ICMSS_FECEP | NUMBER(17,2) | Y |  |  |
| 33 | VLR_MEDIO_TOTAL | NUMBER(17,2) | Y |  |  |
| 34 | COD_EMPRESA_ENT | VARCHAR2(3) | Y |  |  |
| 35 | COD_ESTAB_ENT | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PERIODO, IDENT_PRODUTO, DATA_FISCAL, NUM_SERIE_ECF, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, NUM_ITEM, MOVTO_E_S, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, DATA_FISCAL_REF, IDENT_DOCTO_REF, IDENT_FIS_JUR_REF, NUM_ITEM_REF

---

## EST_ST_SP_X192_TMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | DATE | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 12 | IND_TIPO_REF | CHAR(1) | Y |  |  |
| 13 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 15 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 16 | DATA_FISCAL_REF | DATE | Y |  |  |
| 17 | IDENT_FIS_JUR_REF | NUMBER(12) | Y |  |  |
| 18 | NUM_ITEM_REF | NUMBER(5) | Y |  |  |
| 19 | QTD_DEVOL | NUMBER(17,6) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 22 | NUM_AUTENTIC_NFE_REF | VARCHAR2(80) | Y |  |  |
| 23 | NUM_CNPJ_NFE_REF | VARCHAR2(14) | Y |  |  |

---

## EST_TO_DADOS_INICIAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PORTADOR_TARE | CHAR(1) | Y |  |  |
| 4 | NUM_TARE | VARCHAR2(20) | Y |  |  |
| 5 | DATA_VENC_TARE | DATE | Y |  |  |
| 6 | IND_TIPO_ESCRIT | CHAR(1) | Y |  |  |
| 7 | IND_USUARIO_ECF | CHAR(1) | Y |  |  |
| 8 | COD_DECLARANTE | VARCHAR2(2) | Y |  |  |
| 9 | COD_CONTABILISTA | VARCHAR2(2) | Y |  |  |
| 10 | IND_OPT_SIMPLES_NAC | CHAR(1) | Y |  |  |
| 11 | CONSIDERA_ULT_7DIG_NF | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_DECLARANTE → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_CONTABILISTA → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EST_TO_DADOS_MENSAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | VLR_SALDO_INI | NUMBER(14,2) | Y |  |  |
| 6 | VLR_SALDO_FIM | NUMBER(14,2) | Y |  |  |
| 7 | IND_MUDANCA_DOMICILIO | CHAR(1) | Y |  |  |
| 8 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 9 | COD_MUNIC_ANT | NUMBER(5) | Y |  |  |
| 10 | DATA_INI_ANT | DATE | Y |  |  |
| 11 | DATA_FIM_ANT | DATE | Y |  |  |
| 12 | DATA_INI_ATUAL | DATE | Y |  |  |
| 13 | DATA_FIM_ATUAL | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, COD_MUNIC_ANT → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EST_TO_DIF_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 6 | VLR_DIF_ALIQ_ANT | NUMBER(14,2) | Y |  |  |
| 7 | VLR_DIF_ALIQ_PER | NUMBER(14,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, COD_TIPO_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## EST_TO_DIF_ALIQ_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | IND_TP_DOM_FISCAL | CHAR(1) | N |  |  |
| 8 | VLR_CONTABIL | NUMBER(14,2) | Y |  |  |
| 9 | VLR_BASE_CALC | NUMBER(14,2) | Y |  |  |
| 10 | VLR_DIF_ALIQ | NUMBER(14,2) | Y |  |  |
| 11 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | ALIQ_DIFERENCA | NUMBER(7,4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, COD_TIPO_LIVRO, IDENT_ESTADO, IND_TP_DOM_FISCAL, ALIQ_DIFERENCA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)
- COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, COD_TIPO_LIVRO → EST_TO_DIF_ALIQ(COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, COD_TIPO_LIVRO)

---

## EST_TO_ICMS_RECOLHER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_REF | NUMBER(2) | N |  |  |
| 4 | ANO_REF | NUMBER(4) | N |  |  |
| 5 | IND_TIPO_ICMS | CHAR(1) | N |  |  |
| 6 | DAT_VENCIMENTO | DATE | N |  |  |
| 7 | VLR_ICMS_RECOLHER | NUMBER(14,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_REF, ANO_REF, IND_TIPO_ICMS, DAT_VENCIMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EST_UF_AMOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | IND_INCENT_MANAUS | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO

---

## EST_UF_CAE_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_UF | VARCHAR2(2) | N |  |  |
| 4 | COD_CAE | VARCHAR2(7) | N |  |  |
| 5 | COD_DESMEMBRAMENTO | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_UF, COD_CAE, COD_DESMEMBRAMENTO

---

## EST_UF_CFO_SIT
**Comment**: TABELA DE CADASTROS DE SITUAÇÃO DE CFOPS POR UF, EX GMB-RS. TACES 51

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF | VARCHAR2(2) | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | N |  |  |
| 3 | IND_VLR_CONTABIL | VARCHAR2(1) | Y |  |  |
| 4 | IND_BASE_CALC | VARCHAR2(1) | Y |  |  |
| 5 | IND_ISENTA | VARCHAR2(1) | Y |  |  |
| 6 | IND_OUTRAS | VARCHAR2(1) | Y |  |  |
| 7 | IND_EXCLUIDA | VARCHAR2(1) | Y |  |  |
| 8 | CALC_E | VARCHAR2(2) | Y |  |  |
| 9 | IND_OBS | VARCHAR2(1) | Y |  |  |

**PK**: COD_UF, COD_CFO

---

## EST_UF_CLASSE_GIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | COD_CLASSE | VARCHAR2(3) | N |  |  |

**PK**: COD_ESTADO, COD_CLASSE

**FKs**:
- COD_CLASSE → PRT_CLASSE_MSAF(COD_CLASSE)

---

## EST_UF_CONF_SEFAZ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DIFERENCIAL_ALIQ | NUMBER(7) | N |  |  |
| 9 | VALOR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 11 | NOTIFICA_SEFAZ | VARCHAR2(14) | Y |  |  |
| 12 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IDENT_CFO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DIFERENCIAL_ALIQ

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

---

## EST_UF_REGIAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UF_OBRIG | VARCHAR2(2) | N |  |  |
| 2 | COD_REGIAO | VARCHAR2(2) | Y |  |  |
| 3 | COD_UF_REGIAO | VARCHAR2(2) | N |  |  |

**PK**: COD_UF_OBRIG, COD_UF_REGIAO

---

## EST_UND_PADRAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_UND_PADRAO | VARCHAR2(8) | N |  |  |
| 3 | DSC_UND_PADRAO | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_ESTADO, COD_UND_PADRAO

---

## EST_UTIL_PER_C176

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_UTIL | DATE | N |  |  |
| 4 | VLR_ICMS_RECUP | NUMBER(17,2) | Y |  |  |
| 5 | VLR_ICMS_ESTORNO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_RESSARC | NUMBER(17,2) | Y |  |  |
| 7 | IND_RECUP_RESSARC | CHAR(1) | Y |  | 1- Valor do ICMS a recuperar, 2- Valor do ICMS a ressarcir. |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_UTIL

---

## EST_VAFMG_DD_INIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_EXERCICIO | NUMBER(4) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | Y |  |  |
| 5 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 6 | TP_CONTRIB | CHAR(1) | Y |  |  |
| 7 | VLR_GER_ENERG_ELET | NUMBER(19,2) | Y |  |  |
| 8 | VLR_AJU_TRANSF_ENT | NUMBER(19,2) | Y |  |  |
| 9 | VLR_AUT_DEN_ENT | NUMBER(19,2) | Y |  |  |
| 10 | VLR_TANSP_TOMADO | NUMBER(19,2) | Y |  |  |
| 11 | VLR_AJU_TRANSF_SAI | NUMBER(19,2) | Y |  |  |
| 12 | VLR_AUT_DEN_SAI | NUMBER(19,2) | Y |  |  |
| 13 | VLR_COOPERATIVA | NUMBER(19,2) | Y |  |  |
| 14 | VLR_EXVAF_OUT_ENT | NUMBER(19,2) | Y |  |  |
| 15 | VLR_EXVAF_OUT_SAI | NUMBER(19,2) | Y |  |  |
| 16 | VLR_VAF_OUT_ENT | NUMBER(19,2) | Y |  |  |
| 17 | IND_PERFIL_APRESENT | VARCHAR2(1) | Y |  |  |
| 18 | VLR_SUB_SRV_TRAN_ENT | NUMBER(19,2) | Y |  |  |
| 19 | VLR_AJUSTE_ENT | NUMBER(19,2) | Y |  |  |
| 20 | VLR_EXTRAORD_ENT | NUMBER(19,2) | Y |  |  |
| 21 | VLR_AJUSTE_SAI | NUMBER(19,2) | Y |  |  |
| 22 | VLR_EXTRAORD_SAI | NUMBER(19,2) | Y |  |  |
| 23 | MES_MUDANCA | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_EXERCICIO

---

