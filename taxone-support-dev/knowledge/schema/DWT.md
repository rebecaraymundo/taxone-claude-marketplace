# Módulo: DWT (Dimensões/Lookup) - 68 tabelas

## DWT_AMPARO_LEGAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 3 | DAT_VALIDADE | DATE | N |  |  |
| 4 | DSC_AMPARO_LEGAL | VARCHAR2(100) | Y |  |  |
| 5 | DSC_OCORRENCIA | VARCHAR2(300) | Y |  |  |
| 6 | DAT_FIM_VALIDADE | DATE | Y |  |  |
| 7 | DADOS_COMPL1 | VARCHAR2(50) | Y |  |  |
| 8 | DADOS_COMPL2 | VARCHAR2(50) | Y |  |  |
| 9 | COD_RECEITA | VARCHAR2(5) | Y |  |  |
| 10 | IND_INCIDE_ICMS | CHAR(1) | Y |  |  |
| 11 | IND_INCIDE_IPI | CHAR(1) | Y |  |  |
| 12 | IND_INCIDE_ICMSS | CHAR(1) | Y |  |  |
| 13 | IND_TRIBUTO | CHAR(1) | Y |  |  |
| 14 | IND_CALC_NF | CHAR(1) | Y | 'N' |  |

**PK**: IDENT_ESTADO, COD_AMPARO_LEGAL, DAT_VALIDADE

**Indexes**:
- IX_DWT_AMPARO_LEGAL_01: (COD_AMPARO_LEGAL, DAT_VALIDADE)

---

## DWT_AREA_LIVR_COM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_AREA_LIVR_COM | VARCHAR2(10) | N |  |  |
| 2 | DSC_AREA_LIVR_COM | VARCHAR2(50) | Y |  |  |

**PK**: COD_AREA_LIVR_COM

---

## DWT_ATIV_CONT_PREV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ATIV_CONT_PREV | NUMBER(5) | N |  |  |
| 2 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 3 | DATA_INI_VIGENCIA | DATE | Y |  |  |
| 4 | DSC_ATIV_CONT_PREV | VARCHAR2(400) | Y |  |  |
| 5 | COD_NCM | VARCHAR2(10) | Y |  |  |
| 6 | ALIQUOTA | NUMBER(8,4) | Y |  |  |
| 7 | DAT_FIM_VIGENCIA | DATE | Y |  |  |
| 8 | IND_ATIVIDADE | CHAR(1) | Y |  |  |
| 9 | COD_CNAE | VARCHAR2(10) | Y |  |  |
| 10 | DAT_INI_ESCRIT | DATE | Y |  |  |
| 11 | COD_RECEITA | VARCHAR2(6) | Y |  |  |

**PK**: IDENT_ATIV_CONT_PREV

**Indexes**:
- UK_ATIV_CONT_PREV (UNIQUE): (COD_ATIV_CONT_PREV, DATA_INI_VIGENCIA)

---

## DWT_BALANCO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_BALANCO | DATE | N |  |  |
| 4 | IND_TP_BALANCO | CHAR(1) | N |  |  |
| 5 | IND_PERIODIC | CHAR(1) | N |  |  |
| 6 | COD_CLASSE_BALANCO | VARCHAR2(9) | N |  |  |
| 7 | VLR_CLASSE_BALANCO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_BALANCO, IND_TP_BALANCO, IND_PERIODIC, COD_CLASSE_BALANCO

**FKs**:
- COD_CLASSE_BALANCO → DWT_CLASSE_BALANCO(COD_CLASSE_BALANCO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DWT_BANCOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_BANCO | VARCHAR2(3) | N |  |  |
| 2 | DSC_BANCO | VARCHAR2(50) | N |  |  |

**PK**: COD_BANCO

---

## DWT_BENEFICIO_FISCAL
**Comment**: ATO COTEPE 70 tabela 6.6.1, 6.6.2 - Tabela de Beneficio Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_BENEF_FISCAL | NUMBER(12) | N |  |  |
| 2 | IND_TIPO_IMPOSTO | CHAR(1) | Y |  | 1 - ICMS; 2 - ISS |
| 3 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 4 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 5 | COD_BENEFICIO | VARCHAR2(5) | Y |  |  |
| 6 | DESC_BENEFICIO | VARCHAR2(300) | Y |  |  |

**PK**: IDENT_BENEF_FISCAL

---

## DWT_CANAIS_DISTRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CANAL_DISTRIB | VARCHAR2(15) | N |  |  |
| 2 | DSC_CANAL_DISTRIB | VARCHAR2(100) | Y |  |  |
| 3 | CEI | VARCHAR2(12) | Y |  |  |
| 4 | DATA_ABERTURA | DATE | Y |  |  |
| 5 | DATA_ENCERRAMENTO | DATE | Y |  |  |
| 6 | DESCRICAO_COMPL | VARCHAR2(255) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y | '4' |  |
| 9 | NATUREZA_OBRA | VARCHAR2(100) | Y |  | Ato Cotepe 70 - reg B700: natureza da obra contratada |
| 10 | IDENT_ESTADO | NUMBER(12) | Y |  | Ato Cotepe 70 - reg B700: UF onde está localizada a obra |
| 11 | CEP | NUMBER(8) | Y |  | Ato Cotepe 70 - reg B700: CEP onde está localizada a obra |
| 12 | NUM_IMOVEL | VARCHAR2(10) | Y |  | Ato Cotepe 70 - reg B700: Número do imóvel |
| 13 | NUM_COMPL | VARCHAR2(45) | Y |  | Ato Cotepe 70 - reg B700: Complemento do endereço da obra |
| 14 | BAIRRO | VARCHAR2(20) | Y |  | Ato Cotepe 70 - reg B700: Bairro onde está localizada a obra |
| 15 | DATA_CONTRATACAO | DATE | Y |  | Ato Cotepe 70 - reg B700: Data da contratação |
| 16 | REG_CARTORIO | VARCHAR2(100) | Y |  | Ato Cotepe 70 - reg B700: Registro da obra no cartório (nome do cartório, livro, folha) |
| 17 | VLR_TOT_OBRA | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg B700: Valor total da obra |
| 18 | COD_ART | VARCHAR2(15) | Y |  |  |
| 19 | ENDERECO | VARCHAR2(100) | Y |  |  |

**PK**: COD_CANAL_DISTRIB

---

## DWT_CAPA_ECF_PROC_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_COO | VARCHAR2(9) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 7 | ORIG_PROCESSO | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CAIXA_ECF, NUM_COO, DATA_EMISSAO, IDENT_PROC_REF, ORIG_PROCESSO

---

## DWT_CEP
**Comment**: Tabela de CEP dos Municipios

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CEP | NUMBER(5) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | COD_CEP_FINAL | NUMBER(5) | Y |  |  |

**PK**: COD_CEP, COD_MUNICIPIO

---

## DWT_CLASSE_AMPARO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_CLASSE | VARCHAR2(3) | N |  |  |
| 3 | COD_AMPARO_LEGAL | VARCHAR2(6) | Y |  |  |
| 4 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |

**PK**: IDENT_ESTADO, COD_CLASSE

**FKs**:
- COD_CLASSE → PRT_CLASSE_MSAF(COD_CLASSE)

---

## DWT_CLASSE_BALANCO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSE_BALANCO | VARCHAR2(9) | N |  |  |
| 2 | DSC_CLASSE_BALANCO | VARCHAR2(50) | Y |  |  |

**PK**: COD_CLASSE_BALANCO

---

## DWT_CLASSE_CONSUMO
**Comment**: ATO COTEPE 70 tabelas 4.4.1, 4.4.3, 4.4.4, 4.4.5 - Tabela de Classes de Consumo de Utilities

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CLASSE_CONSUMO | NUMBER(12) | N |  |  |
| 2 | COD_MODELO | VARCHAR2(2) | Y |  | Modelos de Documentos de Utilities: 06 - energia elétrica, 27 - água, 28 - gás, 21 - comunicação, 22 - telecomunicação. |
| 3 | COD_CLASSE_CONSUMO | VARCHAR2(2) | Y |  | Código das Classes de Consumo das tabelas 4.4.1, 4.4.3, 4.4.4, 4.4.5 do ATO COTEPE 70. |
| 4 | DSC_CLASSE_CONSUMO | VARCHAR2(120) | Y |  |  |
| 5 | IND_USO_CLASSE_CONSUMO | CHAR(1) | Y | '1' | Indica o assunto ao qual a classe de consumo se refere: 1 - SPED Fiscal, 2 - SEF-PE |

**PK**: IDENT_CLASSE_CONSUMO

**Indexes**:
- UK_CLASSE_CONSUMO (UNIQUE): (COD_MODELO, COD_CLASSE_CONSUMO, IND_USO_CLASSE_CONSUMO)

---

## DWT_CLASSIF_TRIB
**Comment**: Cadastro da Classificação Tributária (Tabela 08 do REINF)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSIF_TRIB | VARCHAR2(2) | N |  |  |
| 2 | DSC_CLASSIF_TRIB | VARCHAR2(150) | Y |  |  |
| 3 | COD_VERSAO_REINF | VARCHAR2(3) | Y |  | Versao do Layout do EFD-Reinf. Dominio REINF_VERSAO_LAYOUT_V |

**PK**: COD_CLASSIF_TRIB

---

## DWT_COD_AJUSTE_SPED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 3 | DSC_COD_AJUSTE_SPED | VARCHAR2(300) | Y |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_AJUSTE_SPED

---

## DWT_COD_FISCAL_SERV
**Comment**: Tabela 4.2.3 do Ato Cotepe 70-05

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CFPS | VARCHAR2(4) | N |  | Código CFPS |
| 2 | DSC_CFPS | VARCHAR2(230) | Y |  | Descrição CFPS |

**PK**: COD_CFPS

---

## DWT_COD_IATA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | COD_IATA | VARCHAR2(3) | N |  |  |
| 4 | DSC_AEROPORTO | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, COD_IATA

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## DWT_COD_MOTIVO_SPED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MOTIVO_SPED | VARCHAR2(5) | N |  |  |
| 3 | DSC_COD_MOTIVO_SPED | VARCHAR2(300) | Y |  |  |

**PK**: COD_MOTIVO_SPED

---

## DWT_COD_NAT_REND
**Comment**: Natureza de Rendimentos

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO_NAT_REND | VARCHAR2(2) | N |  | Código do Grupo da Natureza do Rendimento |
| 2 | COD_NAT_REND | VARCHAR2(9) | N |  | Código da Natureza do Rendimento |
| 3 | DESCRICAO | VARCHAR2(600) | Y |  | Natureza de Rendimento |
| 4 | IND_FCI | VARCHAR2(3) | Y |  | FCI |
| 5 | IND_DEC_TERC | VARCHAR2(3) | Y |  | 13º Décimo Terceiro |
| 6 | IND_RRA | VARCHAR2(3) | Y |  | RRA |
| 7 | TIPO_DEDUCAO | VARCHAR2(50) | N |  | Dedução |
| 8 | DESC_TIPO_DEDUCAO | VARCHAR2(600) | Y |  | Descrição Dedução |
| 9 | TIPO_ISENCAO | VARCHAR2(50) | N |  | Rendimento Isento |
| 10 | DESC_TIPO_ISENCAO | VARCHAR2(600) | Y |  | Descrição Rendimentos Isentos |
| 11 | TIPO_PAIS_EXT_PF | VARCHAR2(50) | Y |  | Pais Exterior PF |
| 12 | TIPO_PAIS_EXT_PJ | VARCHAR2(50) | Y |  | Pais Exterior PJ |
| 13 | TIPO_NAT_DECLAR | VARCHAR2(50) | Y |  | Natureza Permitida para o Declarante |
| 14 | TIPO_TRIBUTO | VARCHAR2(50) | N |  | Tributo |

**PK**: COD_GRUPO_NAT_REND, COD_NAT_REND, TIPO_DEDUCAO, TIPO_ISENCAO, TIPO_TRIBUTO

**Indexes**:
- IX_DWT_COD_NAT_REND: (COD_NAT_REND)

---

## DWT_COD_RECEITA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 2 | DSC_RECEITA | VARCHAR2(100) | Y |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 4 | IND_PERIODIC | CHAR(1) | Y |  |  |
| 5 | DAT_INI_VALID | DATE | Y |  |  |
| 6 | DAT_FIM_VALID | DATE | Y |  |  |
| 7 | IND_EMPRESA | VARCHAR2(1) | Y | 'S' | Indicado da Geração da DCTF - (S) Gerar pela Matriz(Empresa) / (N) Gera por Estabelecimento |
| 8 | IND_DEB_SCPINC_R10 | CHAR(1) | Y |  |  |

**PK**: COD_RECEITA

**FKs**:
- COD_TRIBUTO → DWT_TRIBUTO(COD_TRIBUTO)

---

## DWT_COD_SIT_TRIB_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_SIT_TRIB_ISS | VARCHAR2(2) | N |  |  |
| 2 | VALID_INICIAL | DATE | N |  |  |
| 3 | DESC_SIT_TRIB_ISS | VARCHAR2(200) | Y |  |  |

**PK**: COD_SIT_TRIB_ISS, VALID_INICIAL

---

## DWT_COMPANHIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMPANHIA | VARCHAR2(10) | N |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMPANHIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DWT_CONTABIL_BALANCETE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | COD_CONTA_PAI | VARCHAR2(70) | Y |  |  |
| 6 | MES_REF | DATE | N |  |  |
| 7 | IND_ANALITICO | NUMBER(1) | Y |  |  |
| 8 | DESC_CONTA | VARCHAR2(50) | Y |  |  |

**PK**: ID

---

## DWT_CONTABIL_RESUMIDO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | DATA_LANCTO | DATE | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 8 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 10 | DESC_HIST | VARCHAR2(50) | Y |  |  |
| 11 | DESC_CUSTO | VARCHAR2(50) | Y |  |  |
| 12 | DESC_CONTA | VARCHAR2(50) | Y |  |  |
| 13 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |

**PK**: ID

---

## DWT_CONTRATOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTRATO | VARCHAR2(14) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | IND_ABATIMENTO | CHAR(1) | Y |  |  |
| 4 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_CONTRATO

**FKs**:
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)

---

## DWT_CONV_MEDIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 2 | COD_MEDIDA_ORIG | VARCHAR2(8) | N |  |  |
| 3 | COD_MEDIDA_DEST | VARCHAR2(8) | N |  |  |
| 4 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |

**PK**: GRUPO_MEDIDA, COD_MEDIDA_ORIG, COD_MEDIDA_DEST

---

## DWT_CONV_MEDIDA2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 5 | COD_MEDIDA_ORIG | VARCHAR2(8) | N |  |  |
| 6 | COD_MEDIDA_DEST | VARCHAR2(8) | N |  |  |
| 7 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_MEDIDA, COD_MEDIDA_ORIG, COD_MEDIDA_DEST

**Indexes**:
- IX_DWT_CONV_MEDIDA2_01: (GRUPO_MEDIDA, COD_MEDIDA_ORIG, COD_MEDIDA_DEST)

---

## DWT_DEF_REGIAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_REGIAO | NUMBER(2) | N |  |  |
| 3 | DSC_REGIAO | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_ESTADO, COD_REGIAO

**FKs**:
- COD_REGIAO → DWT_REGIOES(COD_REGIAO)

---

## DWT_DOCTO_CONF

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
| 12 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 13 | IND_TP_DOC | CHAR(1) | Y |  |  |
| 14 | IND_TP_ERRO | CHAR(1) | Y |  |  |
| 15 | USUARIO | VARCHAR2(40) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## DWT_DOCTO_FISCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 14 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 15 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 16 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 17 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 18 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 19 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 20 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 21 | DATA_SAIDA_REC | DATE | Y |  |  |
| 22 | INSC_ESTAD_SUBSTIT | VARCHAR2(14) | Y |  |  |
| 23 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 25 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 26 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 27 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_BASE_DIF_FRETE | NUMBER(17,2) | Y |  |  |
| 29 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 30 | CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 31 | SITUACAO | CHAR(1) | Y |  |  |
| 32 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 33 | VLR_NOTA_CONV | NUMBER(18,4) | Y |  |  |
| 34 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 35 | IND_MODELO_CUPOM | VARCHAR2(2) | Y |  |  |
| 36 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 37 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 38 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 39 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 40 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 41 | VLR_OUTROS3 | NUMBER(17,2) | Y |  |  |
| 42 | VLR_OUTROS4 | NUMBER(17,2) | Y |  |  |
| 43 | VLR_OUTROS5 | NUMBER(17,2) | Y |  |  |
| 44 | VLR_ALIQ_OUTROS1 | NUMBER(7,4) | Y |  |  |
| 45 | VLR_ALIQ_OUTROS2 | NUMBER(7,4) | Y |  |  |
| 46 | IND_NF_ESPECIAL | CHAR(1) | Y |  |  |
| 47 | NUM_MAQUINA | NUMBER(6) | Y |  |  |
| 48 | NUM_CUPOM_FINAL | NUMBER(6) | Y |  |  |
| 49 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 50 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 51 | DIF_ALIQ_TRIB_ICMS | NUMBER(7,4) | Y |  |  |
| 52 | OBS_TRIBUTO_ICMS | VARCHAR2(45) | Y |  |  |
| 53 | IDENT_DET_OP_ICMS | NUMBER(12) | Y |  |  |
| 54 | ALIQ_TRIBUTO_IPI | NUMBER(7,4) | Y |  |  |
| 55 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 56 | OBS_TRIBUTO_IPI | VARCHAR2(45) | Y |  |  |
| 57 | IDENT_DET_OP_IPI | NUMBER(12) | Y |  |  |
| 58 | ALIQ_TRIBUTO_ICMSS | NUMBER(7,4) | Y |  |  |
| 59 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 60 | OBS_TRIBUTO_ICMSS | VARCHAR2(45) | Y |  |  |
| 61 | IDENT_DET_OP_ICMSS | NUMBER(12) | Y |  |  |
| 62 | ALIQ_TRIBUTO_IR | NUMBER(7,4) | Y |  |  |
| 63 | VLR_TRIBUTO_IR | NUMBER(17,2) | Y |  |  |
| 64 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |
| 65 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 66 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 67 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 68 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 69 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 70 | VLR_BASE_IPI_1 | NUMBER(17,2) | Y |  |  |
| 71 | VLR_BASE_IPI_2 | NUMBER(17,2) | Y |  |  |
| 72 | VLR_BASE_IPI_3 | NUMBER(17,2) | Y |  |  |
| 73 | VLR_BASE_IPI_4 | NUMBER(17,2) | Y |  |  |
| 74 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 75 | VLR_BASE_IR_1 | NUMBER(17,2) | Y |  |  |
| 76 | VLR_BASE_IR_2 | NUMBER(17,2) | Y |  |  |
| 77 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 78 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 79 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 80 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 81 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 82 | IND_TP_FRETE | CHAR(1) | Y |  |  |
| 83 | COD_MUNICIPIO | NUMBER(7) | Y |  |  |
| 84 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 85 | DAT_DI | DATE | Y |  |  |
| 86 | VLR_TOM_SERVICO | NUMBER(17,2) | Y |  |  |
| 87 | DAT_ESCR_EXTEMP | DATE | Y |  |  |
| 88 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 89 | COD_REGIAO | NUMBER(2) | Y |  |  |
| 90 | DAT_AUTENTIC | DATE | Y |  |  |
| 91 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 92 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 93 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 94 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 95 | VLR_TOT_IN | NUMBER(17,2) | Y |  |  |
| 96 | VLR_ICMS_IN | NUMBER(17,2) | Y |  |  |
| 97 | VLR_ICMS_B1_IN | NUMBER(17,2) | Y |  |  |
| 98 | VLR_ICMS_B2_IN | NUMBER(17,2) | Y |  |  |
| 99 | VLR_ICMS_B3_IN | NUMBER(17,2) | Y |  |  |
| 100 | VLR_ICMS_B4_IN | NUMBER(17,2) | Y |  |  |
| 101 | VLR_IPI_IN | NUMBER(17,2) | Y |  |  |
| 102 | VLR_IPI_B1_IN | NUMBER(17,2) | Y |  |  |
| 103 | VLR_IPI_B2_IN | NUMBER(17,2) | Y |  |  |
| 104 | VLR_IPI_B3_IN | NUMBER(17,2) | Y |  |  |
| 105 | VLR_IPI_B4_IN | NUMBER(17,2) | Y |  |  |
| 106 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 107 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 108 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 109 | VLR_MAT_APLIC_ISS | NUMBER(17,2) | Y |  |  |
| 110 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 111 | IND_MUNIC_ISS | CHAR(1) | Y |  |  |
| 112 | IND_CLASSE_OP_ISS | CHAR(1) | Y |  |  |
| 113 | DAT_FATO_GERADOR | DATE | Y |  |  |
| 114 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 115 | NUM_PAGINA | VARCHAR2(6) | Y |  |  |
| 116 | NUM_LIVRO | VARCHAR2(6) | Y |  |  |
| 117 | NRO_AIDF_NF | VARCHAR2(12) | Y |  |  |
| 118 | DAT_VALID_DOC_AIDF | DATE | Y |  |  |
| 119 | IND_FATURA | CHAR(1) | Y |  |  |
| 120 | IDENT_QUITACAO | NUMBER(12) | Y |  |  |
| 121 | NUM_SELO_CONT_ICMS | VARCHAR2(12) | Y |  |  |
| 122 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 123 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 124 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 125 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 126 | BASE_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 127 | VLR_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 128 | ALIQ_ICMS_ORIGDEST | NUMBER(7,4) | Y |  |  |
| 129 | VLR_DESC_CONDIC | NUMBER(17,2) | Y |  |  |
| 130 | VLR_BASE_ISE_ICMSS | NUMBER(17,2) | Y |  |  |
| 131 | VLR_BASE_OUT_ICMSS | NUMBER(17,2) | Y |  |  |
| 132 | VLR_RED_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 133 | PERC_RED_BASE_ICMS | NUMBER(7,4) | Y |  |  |
| 134 | IDENT_FISJUR_CPDIR | NUMBER(12) | Y |  |  |
| 135 | IND_MEDIDAJUDICIAL | CHAR(1) | Y |  |  |
| 136 | IDENT_UF_ORIG_DEST | NUMBER(12) | Y |  |  |
| 137 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  |  |
| 138 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 139 | NUM_CTR_DISP | NUMBER(10) | Y |  |  |
| 140 | NUM_FIM_DOCTO | VARCHAR2(12) | Y |  |  |
| 141 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 142 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 143 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 144 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 145 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 146 | COD_PAGTO_INSS | VARCHAR2(4) | Y |  |  |
| 147 | DAT_OPERACAO | DATE | Y |  |  |
| 148 | USUARIO | VARCHAR2(40) | Y |  |  |
| 149 | DAT_INTERN_AM | DATE | Y |  |  |
| 150 | IDENT_FISJUR_LSG | NUMBER(12) | Y |  |  |
| 151 | COMPROV_EXP | VARCHAR2(15) | Y |  |  |
| 152 | NUM_FINAL_CRT_DISP | NUMBER(12) | Y |  |  |
| 153 | NUM_ALVARA | VARCHAR2(8) | Y |  |  |
| 154 | NOTIFICA_SEFAZ | VARCHAR2(14) | Y |  |  |
| 155 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 156 | IND_NOTA_SERVICO | CHAR(1) | Y |  |  |
| 157 | COD_MOTIVO | VARCHAR2(10) | Y |  |  |
| 158 | COD_AMPARO | VARCHAR2(10) | Y |  |  |
| 159 | IDENT_ESTADO_AMPAR | NUMBER(12) | Y |  |  |
| 160 | OBS_COMPL_MOTIVO | VARCHAR2(100) | Y |  |  |
| 161 | IND_TP_RET | CHAR(1) | Y |  |  |
| 162 | IND_TP_TOMADOR | CHAR(1) | Y |  |  |
| 163 | COD_ANTEC_ST | CHAR(1) | Y |  |  |
| 164 | IND_TELECOM | CHAR(1) | Y |  |  |
| 165 | CNPJ_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 166 | IDENT_UF_ARMAZ_ORIG | NUMBER(12) | Y |  |  |
| 167 | INS_EST_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 168 | CNPJ_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 169 | IDENT_UF_ARMAZ_DEST | NUMBER(12) | Y |  |  |
| 170 | INS_EST_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 171 | OBS_INF_ADIC_NF | VARCHAR2(250) | Y |  |  |
| 172 | VLR_BASE_INSS_2 | NUMBER(17,2) | Y |  |  |
| 173 | VLR_ALIQ_INSS_2 | NUMBER(7,4) | Y |  |  |
| 174 | VLR_INSS_RETIDO_2 | NUMBER(17,2) | Y |  |  |
| 175 | COD_PAGTO_INSS_2 | VARCHAR2(4) | Y |  |  |
| 176 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 177 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 178 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 179 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 180 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 181 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 182 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 183 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 184 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 185 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 186 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 187 | BASE_ICMSS_SUBSTITUIDO | NUMBER(17,2) | Y |  | Base ICMS-S Substituído - Base de ICMSS informado pelo fornecedor na situação de substituído. |
| 188 | VLR_ICMSS_SUBSTITUIDO | NUMBER(17,2) | Y |  | Valor ICMS-S Substituído - Valor informado pelo fornecedor na situação de substituído. |
| 189 | COD_CEI | VARCHAR2(15) | Y |  |  |
| 190 | VLR_JUROS_INSS | NUMBER(17,2) | Y |  |  |
| 191 | VLR_MULTA_INSS | NUMBER(17,2) | Y |  |  |
| 192 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 193 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 194 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 195 | DAT_PGTO_GNRE_DARJ | DATE | Y |  |  |
| 196 | DT_PAGTO_NF | DATE | Y |  |  |
| 197 | IND_ORIGEM_INFO | CHAR(1) | Y | '0' | 0-Normal;1-Mapa Resumo |
| 198 | HORA_SAIDA | NUMBER(6) | Y |  | hora de saida das mercadorias - ato cotepe 35/05 |
| 199 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  | código da situação do doc. fiscal: 00 - lançamento regular, 01 - extemporâneo, 02 - cancelado, 03 - cancelamento de cupom fiscal anterior, 04 - extemporâneo cancelado, 05 - desfazimento de negócio, 06 - documento referenciado - ato cotepe 35/05 |
| 200 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 35/05 |
| 201 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 202 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 203 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |
| 204 | COD_MUNICIPIO_ORIG | NUMBER(5) | Y |  | ATO COTEPE 70 - reg D030: Município de origem do serviço. |
| 205 | COD_MUNICIPIO_DEST | NUMBER(5) | Y |  | ATO COTEPE 70 - reg D030: Município de destino do serviço. |
| 206 | COD_CFPS | VARCHAR2(4) | Y |  | ATO COTEPE 70 - reg A020: Código Fiscal de Prestação de Serviço. |
| 207 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  | ATO COTEPE 70 - reg B020: Número do Lançamento Contábil. |
| 208 | VLR_MAT_PROP | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do Material Próprio utilizado na prestação do serviço. |
| 209 | VLR_MAT_TERC | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do Material de Terceiros utilizado na prestação do serviço. |
| 210 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor da Base de Cálculo de Retenção de ISSQN. |
| 211 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do ISSQN retido pelo tomador. |
| 212 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg B020: Valor de dedução da base de cálculo do ISSQN. |
| 213 | COD_MUNIC_ARMAZ_ORIG | NUMBER(5) | Y |  | ATO COTEPE 70 - reg C255, D185: Município do armazém de origem - local de coleta. |
| 214 | INS_MUNIC_ARMAZ_ORIG | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C255, D185: Inscrição Municípal do armazém de origem - local de coleta. |
| 215 | COD_MUNIC_ARMAZ_DEST | NUMBER(5) | Y |  | ATO COTEPE 70 - reg C255, D185: Município do armazém de destino - local de entrega. |
| 216 | INS_MUNIC_ARMAZ_DEST | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C255, D185: Inscrição Municípal do armazém de destino - local de entrega. |
| 217 | IDENT_CLASSE_CONSUMO | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C700, D400 - UTILITIES: Código da Classe de Consumo  (energia elétrica, gás, água, telecomunicação, comunicação) - DWT_CLASSE_CONSUMO. |
| 218 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  | ATO COTEPE 70 - reg C700, D400 - UTILITIES: Especificação do Tipo de Receita (energia elétrica, gás, água, telecomunicação, comunicação). Valores Assumidos: 0 - Receita Própria - serviços prestados; 1 - Receita Própria - cobrança de débitos; 2 - Receita Própria - venda de mercadorias; 3 - Receita Própria - venda de serviço pré-pago; 4 - Outras Receitas Próprias; 5 - Receita de Terceiros (co-faturamento); 9 - Outras Receitas de Terceiros. |
| 219 | NUM_CONTRATO | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C705, D405 - UTILITIES: Número do Contrato, ou Código da Unidade de Consumo (energia elétrica), ou Identificação do Terminal Faturado (telecomunicação, comunicação). |
| 220 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg D405 - UTILITIES: Código da Área do Terminal Faturado (telecomunicação, comunicação). |
| 221 | COD_TP_UTIL | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C705, D405 - UTILITIES:Tipo de Ligação (energia elétrica), ou Tipo de Utilização (telecomunicação, comunicação). Preenchimento conforme tabela 11.2 do Convênio 115/133. |
| 222 | GRUPO_TENSAO | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES: Grupo de tensão (energia elétrica). Preenchimento conforme tabela 11.3 do Convênio 115/133. |
| 223 | DATA_CONSUMO_INI | DATE | Y |  | ATO COTEPE 70 - reg C705, D405 - UTILITIES: Data início do consumo de energia (energia elétrica), ou data início da prestação do serviço(telecomunicação, comunicação). |
| 224 | DATA_CONSUMO_FIM | DATE | Y |  | ATO COTEPE 70 - reg C705, D405 - UTILITIES: Data final do consumo de energia (energia elétrica), ou data final da prestação do serviço(telecomunicação, comunicação). |
| 225 | DATA_CONSUMO_LEIT | DATE | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES: Data da leitura do ponto de consumo (energia elétrica). |
| 226 | QTD_CONTRATADA_PONTA | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES: Demanda contratada Ponta, KW (energia elétrica). |
| 227 | QTD_CONTRATADA_FPONTA | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES:  Demanda contratada Fora-Ponta, KW (energia elétrica). |
| 228 | QTD_CONSUMO_TOTAL | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES: Consumo Total, KW(energia elétrica). |
| 229 | IDENT_UF_CONSUMO | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C770, D470 - UTILITIES: UF do Ponto de Consumo (energia elétrica, gás, água), ou UF do Terminal Faturado (telecomunicação, comunicação). |
| 230 | COD_MUNIC_CONSUMO | NUMBER(5) | Y |  | ATO COTEPE 70 - reg C770, D470 - UTILITIES: Município do Ponto de Consumo (energia elétrica, gás, água), ou Município do Terminal Faturado (telecomunicação, comunicação). |
| 231 | COD_OPER_ESP_ST | CHAR(1) | Y |  |  |
| 232 | ATO_NORMATIVO | VARCHAR2(20) | Y |  | SEF-PE: Ato Normativo |
| 233 | NUM_ATO_NORMATIVO | NUMBER(5) | Y |  | SEF-PE: Número do Ato Normativo |
| 234 | ANO_ATO_NORMATIVO | NUMBER(4) | Y |  | SEF-PE: Ano do Ato Normativo |
| 235 | CAPITULACAO_NORMA | VARCHAR2(30) | Y |  | SEF-PE: Capitulação da Norma |
| 236 | VLR_OUTRAS_ENTID | NUMBER(17,2) | Y |  | Valor de outras entidades |
| 237 | VLR_TERCEIROS | NUMBER(17,2) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 238 | IND_TP_COMPL_ICMS | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg E020: Ind Compl. |
| 239 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 240 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 241 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 242 | COD_VERIFIC_NFE | VARCHAR2(60) | Y |  | Codigo de verificacao da nota fiscal eletronica. |
| 243 | COD_TP_RPS_NFE | VARCHAR2(5) | Y |  | Codigo do tipo de RPS (recibo provisorio de servico) da nota fiscal eletronica. |
| 244 | NUM_RPS_NFE | NUMBER(12) | Y |  | Numero do RPS (recibo provisorio de servico) da nota fiscal eletronica. |
| 245 | SERIE_RPS_NFE | VARCHAR2(5) | Y |  | Serie do RPS (recibo provisorio de servico) da nota fiscal eletronica. |
| 246 | DAT_EMISSAO_RPS_NFE | DATE | Y |  | Data de Emissao do RPS (recibo provisorio de servico) da nota fiscal eletronica. |
| 247 | DSC_SERVICO_NFE | VARCHAR2(1000) | Y |  | Descricao dos servicos da nota fiscal eletronica. |
| 248 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  | Numero de autenticacao (hashcode) da nota fiscal eletronica de ICMS. |
| 249 | NUM_DV_NFE | NUMBER(1) | Y |  | Numero do dígito verificador da chave de acesso que compõe da nota fiscal eletronica de ICMS. |
| 250 | MODELO_NF_DMS | VARCHAR2(3) | Y |  | Modelo da Nota Fiscal para a série U ou M em atendimento a DMS Campo Grande - Mato Grosso do Sul. |
| 251 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 252 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 253 | IND_NFE_DENEG_INUT | NUMBER(1) | Y |  | NFE DENEGADA/INUTILIZADA |
| 254 | IND_NF_REG_ESPECIAL | VARCHAR2(1) | Y |  | NF BASEADA EM REGIME ESPECIAL OU NORMA ESPECIFICA |
| 255 | VLR_ABAT_NTRIBUTADO | NUMBER(15,2) | Y |  | VALOR ABATIMENTO NÃO TRIBUTADO |
| 256 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  | Campo criado para gerar o registro 90 da DAPI MG, recuperando as informações da Apuração do ICMS automaticamente. |
| 257 | HORA_EMISSAO | NUMBER(6) | Y |  | hora, minuto e segundo no qual a NF foi emitida |
| 258 | OBS_DADOS_FATURA | VARCHAR2(256) | Y |  | observação contida no campo dados da fatura das NFs Modelo 1 e 1A recebidas e emitidas |
| 259 | HORA_SAIDA_REC | NUMBER(6) | Y |  |  |
| 260 | IDENT_FIS_CONCES | NUMBER(12) | Y |  |  |
| 261 | COD_AUTENTIC | VARCHAR2(32) | Y |  | Codigo de Autenticação utilizado para Portaria CAT44 - SP |
| 262 | IND_PORT_CAT44 | CHAR(1) | Y |  | Indicador se o regiastro vai ser utilizadona CAT44 ou  não |
| 263 | NUM_AUTENTIC_NFE_AUX | NUMBER(9) | Y |  |  |
| 264 | VLR_BASE_INSS_RURAL | NUMBER(17,2) | Y |  |  |
| 265 | VLR_ALIQ_INSS_RURAL | NUMBER(7,4) | Y |  |  |
| 266 | VLR_INSS_RURAL | NUMBER(17,2) | Y |  |  |
| 267 | IDENT_CLASSE_CONSUMO_SEF_PE | NUMBER(12) | Y |  |  |
| 268 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 269 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 270 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 271 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 272 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 273 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 274 | IND_NAT_FRETE | CHAR(1) | Y |  |  |
| 275 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  |  |
| 276 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 277 | IND_VENDA_CANC | CHAR(1) | Y |  |  |
| 278 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 279 | IND_NF_CONTINGENCIA | VARCHAR2(1) | Y |  |  |
| 280 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 281 | VLR_ANTECIP_TRIB | NUMBER(17,2) | Y |  |  |
| 282 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |
| 283 | NUM_NFTS | VARCHAR2(12) | Y |  |  |
| 284 | IND_NF_VENDA_TERCEIROS | CHAR(1) | Y |  | Indicador de Nota Fiscal de Venda de Mercadoria Emitida por Terceiros |
| 285 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 286 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 287 | IND_PREST_SERV | CHAR(1) | Y |  |  |
| 288 | IND_TIPO_PROC | CHAR(1) | Y |  |  |
| 289 | NUM_PROC_JUR | VARCHAR2(20) | Y |  |  |
| 290 | IND_DEC_PROC | CHAR(1) | Y |  |  |
| 291 | IND_TIPO_AQUIS | CHAR(1) | Y |  |  |
| 292 | VLR_DESC_GILRAT | NUMBER(17,2) | Y |  |  |
| 293 | VLR_DESC_SENAR | NUMBER(17,2) | Y |  |  |
| 294 | CNPJ_SUBEMPREITEIRO | VARCHAR2(14) | Y |  |  |
| 295 | CNPJ_CPF_PROPRIETARIO_CNO | VARCHAR2(14) | Y |  |  |
| 296 | VLR_RET_SUBEMPREITADO | NUMBER(17,2) | Y |  |  |
| 297 | NUM_DOCFIS_SERV | VARCHAR2(60) | Y |  |  |
| 298 | V_DATA_TRAB | DATE | Y | NVL("DAT_ESCR_EXTEMP","DATA_FISCAL") |  |
| 299 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 300 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 301 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 302 | DATA_INDEMISS | DATE | Y | CASE  WHEN (("COD_CLASS_DOC_FIS"='2' OR "COD_CL... |  |
| 303 | DATA_INDEMISN | DATE | Y | CASE  WHEN "COD_CLASS_DOC_FIS"='1' THEN NVL("DA... |  |
| 304 | VLR_CONTRIB_PREV | NUMBER(17,2) | Y |  |  |
| 305 | VLR_GILRAT | NUMBER(17,2) | Y |  |  |
| 306 | VLR_CONTRIB_SENAR | NUMBER(17,2) | Y |  |  |
| 307 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 308 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 309 | NUM_CERTIF_QUAL | VARCHAR2(10) | Y |  |  |
| 310 | OBS_REINF | VARCHAR2(250) | Y |  |  |
| 311 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 312 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 313 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 314 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 315 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 316 | VLR_IPI_DEV | NUMBER(17,2) | Y |  |  |
| 317 | VLR_SEST | NUMBER(17,2) | Y |  |  |
| 318 | VLR_SENAT | NUMBER(17,2) | Y |  |  |
| 319 | IND_FIN_EMISSAO_NFE | VARCHAR2(1) | Y |  |  |
| 320 | NUM_AUTENTIC_NFE_SUBST | VARCHAR2(80) | Y |  |  |
| 321 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 322 | IND_TRIB_PRODUTOR_CP | VARCHAR2(1) | Y |  | Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária. 1 - Sobre a comercialização da sua produção; 2 - Sobre a folha de pagamento. Valores Válidos: 1, 2. |
| 323 | IDENT_MODELO_NFE_SUBST | NUMBER(12) | Y |  |  |
| 324 | COD_AUTENTIC_NFE_SUBST | VARCHAR2(32) | Y |  |  |
| 325 | VLR_ENERGIA_INJ | NUMBER(17,2) | Y |  |  |
| 326 | VLR_OUTRAS_DED | NUMBER(17,2) | Y |  |  |
| 327 | IND_TP_FAT_NFE | VARCHAR2(1) | Y |  |  |
| 328 | IND_TP_AMB_NFE | VARCHAR2(1) | Y |  |  |
| 329 | COD_NF_NFE | VARCHAR2(7) | Y |  |  |
| 330 | IND_PRE_PAGO | VARCHAR2(1) | Y |  |  |
| 331 | IND_SESSAO_REDE | VARCHAR2(1) | Y |  |  |
| 332 | DAT_INI_CONTRATO | DATE | Y |  |  |
| 333 | DAT_FIM_CONTRATO | DATE | Y |  |  |
| 334 | NUM_TERMINAL_TEL | VARCHAR2(12) | Y |  |  |
| 335 | IDENT_UF_TERMINAL_TEL | NUMBER(12) | Y |  |  |
| 336 | VLR_ICMS_DESONERADO | NUMBER(17,2) | Y |  |  |
| 337 | VLR_FCP | NUMBER(17,2) | Y |  |  |
| 338 | VLR_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 339 | VLR_FUST | NUMBER(17,2) | Y |  |  |
| 340 | CNPJ_DOWNLOAD | VARCHAR2(14) | Y |  |  |
| 341 | CPF_DOWNLOAD | VARCHAR2(11) | Y |  |  |
| 342 | VLR_CSLL_RETIDO | NUMBER(17,2) | Y |  |  |
| 343 | VLR_IRRF_RETIDO | NUMBER(17,2) | Y |  |  |
| 344 | INSC_EST_VIRTUAL | VARCHAR2(14) | Y |  |  |
| 345 | PERIOD_APUR_SUBST | VARCHAR2(6) | Y |  |  |
| 346 | COD_MOTIVO_SUBST | VARCHAR2(2) | Y |  |  |
| 347 | COD_AUTENTIC_COF | VARCHAR2(44) | Y |  |  |
| 348 | CNPJ_EMIT_FATURAMENTO | VARCHAR2(14) | Y |  |  |
| 349 | IDENT_UF_EMIT_FATURAMENTO | NUMBER(12) | Y |  |  |
| 350 | CNPJ_EMIT_COF | VARCHAR2(14) | Y |  |  |
| 351 | IDENT_MODELO_COF | NUMBER(12) | Y |  |  |
| 352 | SERIE_DOCFIS_COF | VARCHAR2(3) | Y |  |  |
| 353 | NUM_DOCFIS_COF | VARCHAR2(12) | Y |  |  |
| 354 | ANO_MES_COF | VARCHAR2(6) | Y |  |  |
| 355 | COD_HASH_COF | VARCHAR2(32) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_PAGTO_INSS_2 → IRT_COD_PG_INSS(COD_PAGTO)
- IDENT_CLASSE_CONSUMO_SEF_PE → DWT_CLASSE_CONSUMO(IDENT_CLASSE_CONSUMO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO_NFE_SUBST → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_UF_TERMINAL_TEL → ESTADO(IDENT_ESTADO)
- IDENT_UF_EMIT_FATURAMENTO → ESTADO(IDENT_ESTADO)

**Indexes**:
- IX_DATA_INDEMISN: (COD_EMPRESA, COD_ESTAB, DATA_INDEMISN)
- IX_DATA_INDEMISS: (COD_EMPRESA, COD_ESTAB, DATA_INDEMISS)
- IX_DWT_DOCTO_CONTA: (IDENT_CONTA)
- IX_DWT_DOCTO_DATA_FIS_SITU: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, SITUACAO)
- IX_DWT_DOCTO_EMIS: (COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IX_DWT_DOCTO_FIS (UNIQUE): (IDENT_DOCTO_FISCAL)
- IX_DWT_DOCTO_FISCAL: (NUM_AUTENTIC_NFE)
- IX_DWT_DOCTO_REFER: (COD_EMPRESA, COD_ESTAB, NUM_DOCFIS_REF, MOVTO_E_S, IDENT_FIS_JUR, IDENT_DOCTO, DATA_FISCAL)
- IX_DWT_DOCTO_VIRTUAL: (COD_EMPRESA, COD_ESTAB, V_DATA_TRAB, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IX_DWT_DOC_DATAS: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, DATA_EMISSAO, DAT_LANC_PIS_COFINS, DATA_SAIDA_REC, DAT_ESCR_EXTEMP, DAT_FATO_GERADOR, COD_CLASS_DOC_FIS, MOVTO_E_S, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_DOCTO)
- IX_DWT_DOC_FTGER: (COD_ESTAB, COD_EMPRESA, DAT_FATO_GERADOR, MOVTO_E_S, COD_CLASS_DOC_FIS, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IX_DWT_DOC_SAIREC: (DATA_SAIDA_REC, COD_ESTAB, COD_EMPRESA, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IX_EXA_CLASSDOCFIS: (COD_CLASS_DOC_FIS)
- IX_FK_SAF_2792: (IDENT_FIS_JUR)

---

## DWT_DOCTO_FISCAL_SPED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 14 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 15 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 16 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 17 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 18 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 19 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 20 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 21 | DATA_SAIDA_REC | DATE | Y |  |  |
| 22 | INSC_ESTAD_SUBSTIT | VARCHAR2(14) | Y |  |  |
| 23 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 25 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 26 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 27 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_BASE_DIF_FRETE | NUMBER(17,2) | Y |  |  |
| 29 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 30 | CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 31 | SITUACAO | CHAR(1) | Y |  |  |
| 32 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 33 | VLR_NOTA_CONV | NUMBER(18,4) | Y |  |  |
| 34 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 35 | IND_MODELO_CUPOM | VARCHAR2(2) | Y |  |  |
| 36 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 37 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 38 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 39 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 40 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 41 | VLR_OUTROS3 | NUMBER(17,2) | Y |  |  |
| 42 | VLR_OUTROS4 | NUMBER(17,2) | Y |  |  |
| 43 | VLR_OUTROS5 | NUMBER(17,2) | Y |  |  |
| 44 | VLR_ALIQ_OUTROS1 | NUMBER(7,4) | Y |  |  |
| 45 | VLR_ALIQ_OUTROS2 | NUMBER(7,4) | Y |  |  |
| 46 | IND_NF_ESPECIAL | CHAR(1) | Y |  |  |
| 47 | NUM_MAQUINA | NUMBER(6) | Y |  |  |
| 48 | NUM_CUPOM_FINAL | NUMBER(6) | Y |  |  |
| 49 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 50 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 51 | DIF_ALIQ_TRIB_ICMS | NUMBER(7,4) | Y |  |  |
| 52 | OBS_TRIBUTO_ICMS | VARCHAR2(45) | Y |  |  |
| 53 | IDENT_DET_OP_ICMS | NUMBER(12) | Y |  |  |
| 54 | ALIQ_TRIBUTO_IPI | NUMBER(7,4) | Y |  |  |
| 55 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 56 | OBS_TRIBUTO_IPI | VARCHAR2(45) | Y |  |  |
| 57 | IDENT_DET_OP_IPI | NUMBER(12) | Y |  |  |
| 58 | ALIQ_TRIBUTO_ICMSS | NUMBER(7,4) | Y |  |  |
| 59 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 60 | OBS_TRIBUTO_ICMSS | VARCHAR2(45) | Y |  |  |
| 61 | IDENT_DET_OP_ICMSS | NUMBER(12) | Y |  |  |
| 62 | ALIQ_TRIBUTO_IR | NUMBER(7,4) | Y |  |  |
| 63 | VLR_TRIBUTO_IR | NUMBER(17,2) | Y |  |  |
| 64 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |
| 65 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 66 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 67 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 68 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 69 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 70 | VLR_BASE_IPI_1 | NUMBER(17,2) | Y |  |  |
| 71 | VLR_BASE_IPI_2 | NUMBER(17,2) | Y |  |  |
| 72 | VLR_BASE_IPI_3 | NUMBER(17,2) | Y |  |  |
| 73 | VLR_BASE_IPI_4 | NUMBER(17,2) | Y |  |  |
| 74 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 75 | VLR_BASE_IR_1 | NUMBER(17,2) | Y |  |  |
| 76 | VLR_BASE_IR_2 | NUMBER(17,2) | Y |  |  |
| 77 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 78 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 79 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 80 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 81 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 82 | IND_TP_FRETE | CHAR(1) | Y |  |  |
| 83 | COD_MUNICIPIO | NUMBER(7) | Y |  |  |
| 84 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 85 | DAT_DI | DATE | Y |  |  |
| 86 | VLR_TOM_SERVICO | NUMBER(17,2) | Y |  |  |
| 87 | DAT_ESCR_EXTEMP | DATE | Y |  |  |
| 88 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 89 | COD_REGIAO | NUMBER(2) | Y |  |  |
| 90 | DAT_AUTENTIC | DATE | Y |  |  |
| 91 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 92 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 93 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 94 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 95 | VLR_TOT_IN | NUMBER(17,2) | Y |  |  |
| 96 | VLR_ICMS_IN | NUMBER(17,2) | Y |  |  |
| 97 | VLR_ICMS_B1_IN | NUMBER(17,2) | Y |  |  |
| 98 | VLR_ICMS_B2_IN | NUMBER(17,2) | Y |  |  |
| 99 | VLR_ICMS_B3_IN | NUMBER(17,2) | Y |  |  |
| 100 | VLR_ICMS_B4_IN | NUMBER(17,2) | Y |  |  |
| 101 | VLR_IPI_IN | NUMBER(17,2) | Y |  |  |
| 102 | VLR_IPI_B1_IN | NUMBER(17,2) | Y |  |  |
| 103 | VLR_IPI_B2_IN | NUMBER(17,2) | Y |  |  |
| 104 | VLR_IPI_B3_IN | NUMBER(17,2) | Y |  |  |
| 105 | VLR_IPI_B4_IN | NUMBER(17,2) | Y |  |  |
| 106 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 107 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 108 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 109 | VLR_MAT_APLIC_ISS | NUMBER(17,2) | Y |  |  |
| 110 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 111 | IND_MUNIC_ISS | CHAR(1) | Y |  |  |
| 112 | IND_CLASSE_OP_ISS | CHAR(1) | Y |  |  |
| 113 | DAT_FATO_GERADOR | DATE | Y |  |  |
| 114 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 115 | NUM_PAGINA | VARCHAR2(6) | Y |  |  |
| 116 | NUM_LIVRO | VARCHAR2(6) | Y |  |  |
| 117 | NRO_AIDF_NF | VARCHAR2(12) | Y |  |  |
| 118 | DAT_VALID_DOC_AIDF | DATE | Y |  |  |
| 119 | IND_FATURA | CHAR(1) | Y |  |  |
| 120 | IDENT_QUITACAO | NUMBER(12) | Y |  |  |
| 121 | NUM_SELO_CONT_ICMS | VARCHAR2(12) | Y |  |  |
| 122 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 123 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 124 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 125 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 126 | BASE_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 127 | VLR_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 128 | ALIQ_ICMS_ORIGDEST | NUMBER(7,4) | Y |  |  |
| 129 | VLR_DESC_CONDIC | NUMBER(17,2) | Y |  |  |
| 130 | VLR_BASE_ISE_ICMSS | NUMBER(17,2) | Y |  |  |
| 131 | VLR_BASE_OUT_ICMSS | NUMBER(17,2) | Y |  |  |
| 132 | VLR_RED_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 133 | PERC_RED_BASE_ICMS | NUMBER(7,4) | Y |  |  |
| 134 | IDENT_FISJUR_CPDIR | NUMBER(12) | Y |  |  |
| 135 | IND_MEDIDAJUDICIAL | CHAR(1) | Y |  |  |
| 136 | IDENT_UF_ORIG_DEST | NUMBER(12) | Y |  |  |
| 137 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  |  |
| 138 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 139 | NUM_CTR_DISP | NUMBER(10) | Y |  |  |
| 140 | NUM_FIM_DOCTO | VARCHAR2(12) | Y |  |  |
| 141 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 142 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 143 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 144 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 145 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 146 | COD_PAGTO_INSS | VARCHAR2(4) | Y |  |  |
| 147 | DAT_OPERACAO | DATE | Y |  |  |
| 148 | USUARIO | VARCHAR2(40) | Y |  |  |
| 149 | DAT_INTERN_AM | DATE | Y |  |  |
| 150 | IDENT_FISJUR_LSG | NUMBER(12) | Y |  |  |
| 151 | COMPROV_EXP | VARCHAR2(15) | Y |  |  |
| 152 | NUM_FINAL_CRT_DISP | NUMBER(12) | Y |  |  |
| 153 | NUM_ALVARA | VARCHAR2(8) | Y |  |  |
| 154 | NOTIFICA_SEFAZ | VARCHAR2(14) | Y |  |  |
| 155 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 156 | IND_NOTA_SERVICO | CHAR(1) | Y |  |  |
| 157 | COD_MOTIVO | VARCHAR2(10) | Y |  |  |
| 158 | COD_AMPARO | VARCHAR2(10) | Y |  |  |
| 159 | IDENT_ESTADO_AMPAR | NUMBER(12) | Y |  |  |
| 160 | OBS_COMPL_MOTIVO | VARCHAR2(100) | Y |  |  |
| 161 | IND_TP_RET | CHAR(1) | Y |  |  |
| 162 | IND_TP_TOMADOR | CHAR(1) | Y |  |  |
| 163 | COD_ANTEC_ST | CHAR(1) | Y |  |  |
| 164 | IND_TELECOM | CHAR(1) | Y |  |  |
| 165 | CNPJ_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 166 | IDENT_UF_ARMAZ_ORIG | NUMBER(12) | Y |  |  |
| 167 | INS_EST_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 168 | CNPJ_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 169 | IDENT_UF_ARMAZ_DEST | NUMBER(12) | Y |  |  |
| 170 | INS_EST_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 171 | OBS_INF_ADIC_NF | VARCHAR2(250) | Y |  |  |
| 172 | VLR_BASE_INSS_2 | NUMBER(17,2) | Y |  |  |
| 173 | VLR_ALIQ_INSS_2 | NUMBER(7,4) | Y |  |  |
| 174 | VLR_INSS_RETIDO_2 | NUMBER(17,2) | Y |  |  |
| 175 | COD_PAGTO_INSS_2 | VARCHAR2(4) | Y |  |  |
| 176 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 177 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 178 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 179 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 180 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 181 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 182 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 183 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 184 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 185 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 186 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 187 | BASE_ICMSS_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 188 | VLR_ICMSS_SUBSTITUIDO | NUMBER(17,2) | Y |  |  |
| 189 | COD_CEI | VARCHAR2(15) | Y |  |  |
| 190 | VLR_JUROS_INSS | NUMBER(17,2) | Y |  |  |
| 191 | VLR_MULTA_INSS | NUMBER(17,2) | Y |  |  |
| 192 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 193 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 194 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 195 | DAT_PGTO_GNRE_DARJ | DATE | Y |  |  |
| 196 | DT_PAGTO_NF | DATE | Y |  |  |
| 197 | IND_ORIGEM_INFO | CHAR(1) | Y | '0' |  |
| 198 | HORA_SAIDA | NUMBER(6) | Y |  |  |
| 199 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  |  |
| 200 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 201 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 202 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 203 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |
| 204 | COD_MUNICIPIO_ORIG | NUMBER(5) | Y |  |  |
| 205 | COD_MUNICIPIO_DEST | NUMBER(5) | Y |  |  |
| 206 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 207 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 208 | VLR_MAT_PROP | NUMBER(17,2) | Y |  |  |
| 209 | VLR_MAT_TERC | NUMBER(17,2) | Y |  |  |
| 210 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 211 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 212 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  |  |
| 213 | COD_MUNIC_ARMAZ_ORIG | NUMBER(5) | Y |  |  |
| 214 | INS_MUNIC_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 215 | COD_MUNIC_ARMAZ_DEST | NUMBER(5) | Y |  |  |
| 216 | INS_MUNIC_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 217 | IDENT_CLASSE_CONSUMO | NUMBER(12) | Y |  |  |
| 218 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 219 | NUM_CONTRATO | VARCHAR2(14) | Y |  |  |
| 220 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  |  |
| 221 | COD_TP_UTIL | VARCHAR2(2) | Y |  |  |
| 222 | GRUPO_TENSAO | VARCHAR2(2) | Y |  |  |
| 223 | DATA_CONSUMO_INI | DATE | Y |  |  |
| 224 | DATA_CONSUMO_FIM | DATE | Y |  |  |
| 225 | DATA_CONSUMO_LEIT | DATE | Y |  |  |
| 226 | QTD_CONTRATADA_PONTA | NUMBER(17,6) | Y |  |  |
| 227 | QTD_CONTRATADA_FPONTA | NUMBER(17,6) | Y |  |  |
| 228 | QTD_CONSUMO_TOTAL | NUMBER(17,6) | Y |  |  |
| 229 | IDENT_UF_CONSUMO | NUMBER(12) | Y |  |  |
| 230 | COD_MUNIC_CONSUMO | NUMBER(5) | Y |  |  |
| 231 | COD_OPER_ESP_ST | CHAR(1) | Y |  |  |
| 232 | ATO_NORMATIVO | VARCHAR2(20) | Y |  |  |
| 233 | NUM_ATO_NORMATIVO | NUMBER(5) | Y |  |  |
| 234 | ANO_ATO_NORMATIVO | NUMBER(4) | Y |  |  |
| 235 | CAPITULACAO_NORMA | VARCHAR2(30) | Y |  |  |
| 236 | VLR_OUTRAS_ENTID | NUMBER(17,2) | Y |  |  |
| 237 | VLR_TERCEIROS | NUMBER(17,2) | Y |  |  |
| 238 | IND_TP_COMPL_ICMS | VARCHAR2(2) | Y |  |  |
| 239 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 240 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 241 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 242 | COD_VERIFIC_NFE | VARCHAR2(60) | Y |  |  |
| 243 | COD_TP_RPS_NFE | VARCHAR2(5) | Y |  |  |
| 244 | NUM_RPS_NFE | NUMBER(12) | Y |  |  |
| 245 | SERIE_RPS_NFE | VARCHAR2(5) | Y |  |  |
| 246 | DAT_EMISSAO_RPS_NFE | DATE | Y |  |  |
| 247 | DSC_SERVICO_NFE | VARCHAR2(1000) | Y |  |  |
| 248 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 249 | NUM_DV_NFE | NUMBER(1) | Y |  |  |
| 250 | MODELO_NF_DMS | VARCHAR2(3) | Y |  |  |
| 251 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  |  |
| 252 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 253 | IND_NFE_DENEG_INUT | NUMBER(1) | Y |  |  |
| 254 | IND_NF_REG_ESPECIAL | VARCHAR2(1) | Y |  |  |
| 255 | VLR_ABAT_NTRIBUTADO | NUMBER(15,2) | Y |  |  |
| 256 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  |  |
| 257 | HORA_EMISSAO | NUMBER(6) | Y |  |  |
| 258 | OBS_DADOS_FATURA | VARCHAR2(256) | Y |  |  |
| 259 | HORA_SAIDA_REC | NUMBER(6) | Y |  |  |
| 260 | IDENT_FIS_CONCES | NUMBER(12) | Y |  |  |
| 261 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |
| 262 | IND_PORT_CAT44 | CHAR(1) | Y |  |  |
| 263 | NUM_AUTENTIC_NFE_AUX | NUMBER(9) | Y |  |  |
| 264 | VLR_BASE_INSS_RURAL | NUMBER(17,2) | Y |  |  |
| 265 | VLR_ALIQ_INSS_RURAL | NUMBER(7,4) | Y |  |  |
| 266 | VLR_INSS_RURAL | NUMBER(17,2) | Y |  |  |
| 267 | IDENT_CLASSE_CONSUMO_SEF_PE | NUMBER(12) | Y |  |  |
| 268 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 269 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 270 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 271 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 272 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 273 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 274 | IND_NAT_FRETE | CHAR(1) | Y |  |  |
| 275 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  |  |
| 276 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 277 | IND_VENDA_CANC | CHAR(1) | Y |  |  |
| 278 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 279 | IND_NF_CONTINGENCIA | VARCHAR2(1) | Y |  |  |
| 280 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 281 | VLR_ANTECIP_TRIB | NUMBER(17,2) | Y |  |  |
| 282 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |
| 283 | NUM_NFTS | VARCHAR2(12) | Y |  |  |
| 284 | IND_NF_VENDA_TERCEIROS | CHAR(1) | Y |  |  |
| 285 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 286 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 287 | IND_PREST_SERV | CHAR(1) | Y |  |  |
| 288 | IND_TIPO_PROC | CHAR(1) | Y |  |  |
| 289 | NUM_PROC_JUR | VARCHAR2(20) | Y |  |  |
| 290 | IND_DEC_PROC | CHAR(1) | Y |  |  |
| 291 | IND_TIPO_AQUIS | CHAR(1) | Y |  |  |
| 292 | VLR_DESC_GILRAT | NUMBER(17,2) | Y |  |  |
| 293 | VLR_DESC_SENAR | NUMBER(17,2) | Y |  |  |
| 294 | CNPJ_SUBEMPREITEIRO | VARCHAR2(14) | Y |  |  |
| 295 | CNPJ_CPF_PROPRIETARIO_CNO | VARCHAR2(14) | Y |  |  |
| 296 | VLR_RET_SUBEMPREITADO | NUMBER(17,2) | Y |  |  |
| 297 | NUM_DOCFIS_SERV | VARCHAR2(60) | Y |  |  |
| 298 | V_DATA_TRAB | DATE | N |  |  |
| 299 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 300 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 301 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 302 | DATA_INDEMISS | DATE | Y |  |  |
| 303 | DATA_INDEMISN | DATE | Y |  |  |
| 304 | VLR_CONTRIB_PREV | NUMBER(17,2) | Y |  |  |
| 305 | VLR_GILRAT | NUMBER(17,2) | Y |  |  |
| 306 | VLR_CONTRIB_SENAR | NUMBER(17,2) | Y |  |  |
| 307 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 308 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 309 | NUM_CERTIF_QUAL | VARCHAR2(10) | Y |  |  |
| 310 | OBS_REINF | VARCHAR2(250) | Y |  |  |
| 311 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 312 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 313 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 314 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 315 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 316 | VLR_IPI_DEV | NUMBER(17,2) | Y |  |  |
| 317 | VLR_SEST | NUMBER(17,2) | Y |  |  |
| 318 | VLR_SENAT | NUMBER(17,2) | Y |  |  |
| 319 | IND_FIN_EMISSAO_NFE | VARCHAR2(1) | Y |  |  |
| 320 | NUM_AUTENTIC_NFE_SUBST | VARCHAR2(80) | Y |  |  |
| 321 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 322 | IND_TRIB_PRODUTOR_CP | VARCHAR2(1) | Y |  |  |
| 323 | IDENT_MODELO_NFE_SUBST | NUMBER(12) | Y |  |  |
| 324 | COD_AUTENTIC_NFE_SUBST | VARCHAR2(32) | Y |  |  |
| 325 | VLR_ENERGIA_INJ | NUMBER(17,2) | Y |  |  |
| 326 | VLR_OUTRAS_DED | NUMBER(17,2) | Y |  |  |
| 327 | IND_TP_FAT_NFE | VARCHAR2(1) | Y |  |  |
| 328 | IND_TP_AMB_NFE | VARCHAR2(1) | Y |  |  |
| 329 | COD_NF_NFE | VARCHAR2(7) | Y |  |  |
| 330 | IND_PRE_PAGO | VARCHAR2(1) | Y |  |  |
| 331 | IND_SESSAO_REDE | VARCHAR2(1) | Y |  |  |
| 332 | DAT_INI_CONTRATO | DATE | Y |  |  |
| 333 | DAT_FIM_CONTRATO | DATE | Y |  |  |
| 334 | NUM_TERMINAL_TEL | VARCHAR2(12) | Y |  |  |
| 335 | IDENT_UF_TERMINAL_TEL | NUMBER(12) | Y |  |  |
| 336 | VLR_ICMS_DESONERADO | NUMBER(17,2) | Y |  |  |
| 337 | VLR_FCP | NUMBER(17,2) | Y |  |  |
| 338 | VLR_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 339 | VLR_FUST | NUMBER(17,2) | Y |  |  |
| 340 | CNPJ_DOWNLOAD | VARCHAR2(14) | Y |  |  |
| 341 | CPF_DOWNLOAD | VARCHAR2(11) | Y |  |  |
| 342 | VLR_CSLL_RETIDO | NUMBER(17,2) | Y |  |  |
| 343 | VLR_IRRF_RETIDO | NUMBER(17,2) | Y |  |  |
| 344 | INSC_EST_VIRTUAL | VARCHAR2(14) | Y |  |  |
| 345 | PERIOD_APUR_SUBST | VARCHAR2(6) | Y |  |  |
| 346 | COD_MOTIVO_SUBST | VARCHAR2(2) | Y |  |  |
| 347 | COD_AUTENTIC_COF | VARCHAR2(44) | Y |  |  |
| 348 | CNPJ_EMIT_FATURAMENTO | VARCHAR2(14) | Y |  |  |
| 349 | IDENT_UF_EMIT_FATURAMENTO | NUMBER(12) | Y |  |  |
| 350 | CNPJ_EMIT_COF | VARCHAR2(14) | Y |  |  |
| 351 | IDENT_MODELO_COF | NUMBER(12) | Y |  |  |
| 352 | SERIE_DOCFIS_COF | VARCHAR2(3) | Y |  |  |
| 353 | NUM_DOCFIS_COF | VARCHAR2(12) | Y |  |  |
| 354 | ANO_MES_COF | VARCHAR2(6) | Y |  |  |
| 355 | COD_HASH_COF | VARCHAR2(32) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**Indexes**:
- IX_DWT_DOCTO_VIRTUALSPED: (COD_EMPRESA, COD_ESTAB, V_DATA_TRAB, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## DWT_EPCDF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | Y |  |  |
| 2 | INDCAPAITEM | VARCHAR2(8) | Y |  |  |
| 3 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 6 | DATA_FISCAL | DATE | Y |  |  |
| 7 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 8 | NORM_DEV | CHAR(1) | Y |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 14 | NUM_MAX_ITEM | NUMBER | Y |  |  |
| 15 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 16 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 17 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 18 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 19 | SITUACAO | CHAR(1) | Y |  |  |
| 20 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 21 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 22 | DATA_EMISSAO | DATE | Y |  |  |
| 23 | DATA_SAIDA_REC | DATE | Y |  |  |
| 24 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 25 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 26 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 27 | IND_FATURA | CHAR(1) | Y |  |  |
| 28 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 29 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 30 | IND_TP_FRETE | CHAR(1) | Y |  |  |
| 31 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 32 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 33 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 34 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 35 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 36 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 37 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 38 | ALIQ_TRIBUTO_ICMS | NUMBER(15,3) | Y |  |  |
| 39 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 40 | IDENT_SITUACAO_A | NUMBER | Y |  |  |
| 41 | IDENT_SITUACAO_B | NUMBER | Y |  |  |
| 42 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 43 | ALIQ_TRIBUTO_ICMSS | NUMBER(15,3) | Y |  |  |
| 44 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 45 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 46 | COD_TRIB_IPI | VARCHAR2(2) | Y |  |  |
| 47 | VLR_BASE_IPI_1 | NUMBER(17,2) | Y |  |  |
| 48 | ALIQ_TRIBUTO_IPI | NUMBER(15,3) | Y |  |  |
| 49 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 50 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 51 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 52 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 53 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 54 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 55 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 56 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 57 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 58 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 59 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 60 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 61 | VLR_BASE_IR_1 | NUMBER(17,2) | Y |  |  |
| 62 | VLR_TRIBUTO_IR | NUMBER(17,2) | Y |  |  |
| 63 | ALIQ_TRIBUTO_IR | NUMBER(7,4) | Y |  |  |
| 64 | NUM_ITEM | NUMBER(3) | Y |  |  |
| 65 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 66 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 67 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 68 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 69 | COD_NAT_SERV | VARCHAR2(35) | Y |  |  |
| 70 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 71 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 72 | IND_MOV_FIS | CHAR(1) | Y |  |  |
| 73 | IDENT_NBM_NF | NUMBER(12) | Y |  |  |
| 74 | IDENT_NBM_PROD | NUMBER(12) | Y |  |  |
| 75 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 76 | IND_FOME_ZERO | CHAR(1) | Y |  |  |
| 77 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 78 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 79 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 80 | DESCRICAO_COMPL | VARCHAR2(255) | Y |  |  |
| 81 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 82 | CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 83 | CHAVE_NFSE | VARCHAR2(60) | Y |  |  |
| 84 | VLR_ABAT_NT | NUMBER(17,2) | Y |  |  |
| 85 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 86 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 87 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 88 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 89 | IND_NFE_DENEG_INUT | NUMBER(1) | Y |  |  |
| 90 | DAT_ESCR_EXTEMP | DATE | Y |  |  |
| 91 | IND_NF_REG_ESPECIAL | VARCHAR2(1) | Y |  |  |
| 92 | COD_ENQUAD_IPI | VARCHAR2(3) | Y |  |  |
| 93 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 94 | COD_SIT_PIS_ST | VARCHAR2(2) | Y |  |  |
| 95 | QTD_BASE_PIS | NUMBER(19,4) | Y |  |  |
| 96 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 97 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 98 | COD_SIT_COFINS_ST | VARCHAR2(2) | Y |  |  |
| 99 | QTD_BASE_COFINS | NUMBER(19,4) | Y |  |  |
| 100 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 101 | VLR_TERCEIROS | NUMBER(17,2) | Y |  |  |
| 102 | IDENT_OBSERVACAO_CAPA | NUMBER(12) | Y |  |  |
| 103 | IND_ORIGEM_INFO | CHAR(1) | Y |  |  |
| 104 | IDENT_ESTADO_PFJ | NUMBER(12) | Y |  |  |
| 105 | IDENT_CONTA_CAPA | NUMBER(12) | Y |  |  |
| 106 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 107 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 108 | IND_PIS_COFINS_EXT_CAPA | CHAR(1) | Y |  |  |
| 109 | DAT_LANC_PIS_COF_CAPA | DATE | Y |  |  |
| 110 | NUM_ACDRAW | CHAR(11) | Y |  |  |
| 111 | IND_NATUREZA_FRETE | CHAR(1) | Y |  |  |
| 112 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 113 | CPF_CNPJ_PFJ | VARCHAR2(14) | Y |  |  |
| 114 | DT_PAGTO_NF | DATE | Y |  |  |
| 115 | IND_LOCAL_EXEC_SERV | CHAR(1) | Y |  |  |
| 116 | COD_ATIVIDADE_PFJ | NUMBER(7) | Y |  |  |
| 117 | DAT_FATO_GERADOR | DATE | Y |  |  |
| 118 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 119 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 120 | IND_VENDA_CANC | CHAR(1) | Y |  |  |
| 121 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 122 | VLR_ALIQ_PIS_ST | NUMBER(17,2) | Y |  |  |
| 123 | VLR_ALIQ_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 124 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 125 | IND_NF_VENDA_TERCEIROS | CHAR(1) | Y |  |  |
| 126 | IND_CLIENTE_SID | CHAR(1) | Y |  |  |
| 127 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 128 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  |  |
| 129 | NUM_DOCFIS_SERV | VARCHAR2(60) | Y |  |  |
| 130 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 131 | DAT_DI | DATE | Y |  |  |
| 132 | EX_IPI | VARCHAR2(3) | Y |  |  |
| 133 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 134 | VLR_EXC_BC_PIS | NUMBER(15,2) | Y | 0.00 |  |
| 135 | VLR_EXC_BC_COFINS | NUMBER(15,2) | Y | 0.00 |  |
| 136 | VLR_DESCONTO_C100 | NUMBER(15,2) | Y | 0.00 |  |
| 137 | VLR_IPI_NDESTAC | NUMBER(15,2) | Y | 0.00 |  |
| 138 | VLR_ICMSS_NDESTAC | NUMBER(15,2) | Y | 0.00 |  |
| 139 | VLR_ICMSS_N_ESCRIT | NUMBER(15,2) | Y | 0.00 |  |
| 140 | VLR_ICMS_NDESTAC | NUMBER(15,2) | Y | 0.00 |  |

**Indexes**:
- IX_DWT_EPCDF: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_DWT_EPCDF_EMIS: (COD_EMPRESA, COD_ESTAB, DATA_EMISSAO)
- IX_DWT_EPCDF_LANCTO: (COD_EMPRESA, COD_ESTAB, DAT_LANC_PIS_COFINS)

---

## DWT_EPCNE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 5 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 6 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 7 | NORM_DEV | CHAR(1) | Y |  |  |
| 8 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 11 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 12 | SITUACAO | CHAR(1) | Y |  |  |
| 13 | DATA_FISCAL | DATE | Y |  |  |
| 14 | DATA_EMISSAO | DATE | Y |  |  |
| 15 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 16 | IND_PIS_COFINS_EXTEMP_ITEM | CHAR(1) | Y |  |  |
| 17 | DAT_LANC_PIS_COFINS_ITEM | DATE | Y |  |  |
| 18 | IND_PIS_COFINS_EXTEMP_CAPA | CHAR(1) | Y |  |  |
| 19 | DAT_LANC_PIS_COFINS_CAPA | DATE | Y |  |  |
| 20 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 21 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 22 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 23 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 24 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 25 | COD_NAT_SERV | VARCHAR2(35) | Y |  |  |
| 26 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 27 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 28 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 29 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 30 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 31 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 32 | VLR_EXC_BC_PIS | NUMBER(17,2) | Y |  |  |
| 33 | VLR_EXC_BC_COFINS | NUMBER(17,2) | Y |  |  |
| 34 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 35 | COD_SIT_PIS_ST | NUMBER(2) | Y |  |  |
| 36 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 37 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 38 | VLR_ALIQ_PIS_R | NUMBER(17,2) | Y |  |  |
| 39 | QTD_BASE_PIS | NUMBER(19,4) | Y |  |  |
| 40 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 41 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 42 | VLR_ALIQ_PIS_ST | NUMBER(17,2) | Y |  |  |
| 43 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 44 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 45 | COD_SIT_COFINS_ST | NUMBER(2) | Y |  |  |
| 46 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 47 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 48 | VLR_ALIQ_COFINS_R | NUMBER(17,2) | Y |  |  |
| 49 | QTD_BASE_COFINS | NUMBER(19,4) | Y |  |  |
| 50 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 51 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 52 | VLR_ALIQ_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 53 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 54 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 55 | IND_VENDA_CANC | CHAR(1) | Y |  |  |
| 56 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 57 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 58 | NUM_DOC_INI | VARCHAR2(12) | Y |  |  |
| 59 | NUM_DOC_FIM | VARCHAR2(12) | Y |  |  |
| 60 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 61 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 62 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 63 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 64 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |
| 65 | IDENT_ITEM_MERC | NUMBER(12) | Y |  |  |
| 66 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 67 | CLASS_ITEM | VARCHAR2(2) | Y |  |  |
| 68 | CLASS_ITEM_PRD | VARCHAR2(2) | Y |  |  |
| 69 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 70 | DAT_DI | DATE | Y |  |  |
| 71 | EX_IPI | VARCHAR2(3) | Y |  |  |

**Indexes**:
- IX_DWT_EPCNE: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_DWT_EPCNE_EMIS: (COD_EMPRESA, COD_ESTAB, DATA_EMISSAO)
- IX_DWT_EPCNE_LANCTO: (COD_EMPRESA, COD_ESTAB, DAT_LANC_PIS_COFINS_ITEM)

---

## DWT_EXC_DOCTO_FISCAL

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
| 11 | DATA_SAIDA_REC | DATE | Y |  |  |
| 12 | DATA_EXCLUSAO | DATE | N |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_EXCLUSAO

---

## DWT_FASE_PRODUCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FASE_PRODUCAO | VARCHAR2(20) | N |  |  |
| 4 | DAT_VALID_INI | DATE | N |  |  |
| 5 | DAT_VALID_FIM | DATE | Y |  |  |
| 6 | COD_LINHA | NUMBER(2) | N |  |  |
| 7 | COD_FASE | NUMBER(2) | N |  |  |
| 8 | COD_PROCESSO | NUMBER(2) | Y |  |  |
| 9 | DESCRICAO | VARCHAR2(255) | Y |  |  |
| 10 | NUM_ORDEM_EXECUCAO | NUMBER(2) | Y |  |  |
| 11 | QTD_CAP_MAX_PROD | NUMBER(17,6) | Y |  |  |
| 12 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 13 | IND_INDUSTR_TERC | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## DWT_FERIADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ANO | NUMBER(4) | N |  |  |
| 2 | MES | NUMBER(2) | N |  |  |
| 3 | DIA | NUMBER(2) | N |  |  |
| 4 | DSC_FERIADO | VARCHAR2(50) | Y |  |  |
| 5 | IND_FIXO | CHAR(1) | Y |  |  |
| 6 | IND_MUN_EST_FED | CHAR(1) | Y |  |  |
| 7 | IND_BANCARIO | CHAR(1) | Y |  |  |
| 8 | IDENT_ESTADO | NUMBER(12) | N | 0 |  |
| 9 | COD_MUNICIPIO | NUMBER(5) | N | 0 |  |

**PK**: DIA, MES, ANO, IDENT_ESTADO, COD_MUNICIPIO

---

## DWT_GRUPO_CCLASS
**Comment**: Tabela de Grupo cClass das Notas Fiscais Eletronicas

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODELO | VARCHAR2(2) | N |  | Modelos de Documento Fiscal (SAFX2024). |
| 2 | COD_GRUPO_CCLASS | VARCHAR2(3) | N |  | Codigo do Grupo cClass. |
| 3 | DSC_GRUPO_CCLASS | VARCHAR2(150) | Y |  |  |

**PK**: COD_MODELO, COD_GRUPO_CCLASS

---

## DWT_GRUPO_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO_ST | VARCHAR2(2) | N |  |  |
| 2 | DSC_GRUPO_ST | VARCHAR2(100) | Y |  |  |

**PK**: COD_GRUPO_ST

---

## DWT_HISTORICO_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USR_LOGIN | VARCHAR2(40) | N |  |  |
| 2 | DATA_ALTERACAO | DATE | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | MOVTO_E_S | CHAR(1) | N |  |  |
| 8 | DATA_EMISSAO | DATE | N |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_ITEM | NUMBER(5) | N |  |  |
| 12 | NOME_CAMPO | VARCHAR2(30) | N |  |  |
| 13 | CONTEUDO_ANT | VARCHAR2(255) | Y |  |  |
| 14 | CONTEUDO_NOVO | VARCHAR2(255) | Y |  |  |

**PK**: USR_LOGIN, DATA_ALTERACAO, COD_EMPRESA, COD_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, MOVTO_E_S, DATA_EMISSAO, IND_FIS_JUR, COD_FIS_JUR, NUM_ITEM, NOME_CAMPO

---

## DWT_ITEM_CFE_PROC_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_EQUIP | NUMBER(9) | N |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | NUM_ITEM | NUMBER(5) | N |  |  |
| 7 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 8 | ORIG_PROCESSO | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, NUM_ITEM, IDENT_PROC_REF, ORIG_PROCESSO

---

## DWT_ITEM_ECF_PROC_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_COO | VARCHAR2(9) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | NUM_ITEM | NUMBER(5) | N |  |  |
| 7 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 8 | ORIG_PROCESSO | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CAIXA_ECF, NUM_COO, DATA_EMISSAO, NUM_ITEM, IDENT_PROC_REF, ORIG_PROCESSO

---

## DWT_ITENS_CODS_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ROW_ID_CAPA | ROWID | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_FISCAL | DATE | Y |  |  |
| 5 | DATA_EMISSAO | DATE | Y |  |  |
| 6 | DATA_SAIDA_REC | DATE | Y |  |  |
| 7 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 8 | NORM_DEV | CHAR(1) | Y |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 14 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 15 | SITUACAO | CHAR(1) | Y |  |  |
| 16 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 17 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 18 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 19 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 22 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 23 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 24 | IDENT_MEDIDA_ITEM | NUMBER(12) | Y |  |  |
| 25 | IDENT_UND_PADRAO_ITEM | NUMBER(12) | Y |  |  |
| 26 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 27 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 28 | VLR_CREDITO_MVA_SN | NUMBER(17,2) | Y |  |  |
| 29 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 30 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 35 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 36 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 37 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 38 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 39 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 40 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 41 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 42 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 43 | DAT_DI | DATE | Y |  |  |
| 44 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 45 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 46 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 47 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 48 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 49 | IND_SIMPLES_NAC | CHAR(1) | Y |  |  |
| 50 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 51 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 52 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 53 | VALID_PRODUTO | DATE | Y |  |  |
| 54 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 55 | COD_CEST | VARCHAR2(7) | Y |  |  |
| 56 | IDENT_NBM_PROD | NUMBER(12) | Y |  |  |
| 57 | IDENT_MEDIDA_PROD | NUMBER(12) | Y |  |  |
| 58 | IDENT_UND_PADRAO_PROD | NUMBER(12) | Y |  |  |
| 59 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 60 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 61 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 62 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 63 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 64 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 65 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 66 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 67 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 68 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 69 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 70 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 71 | IDENT_ESTADO | NUMBER | Y |  |  |
| 72 | IND_FORNEC_ICMSS | CHAR(1) | Y |  |  |
| 73 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 74 | ALIQ_TRIBUTO_ICMSS | NUMBER(7,4) | Y |  |  |
| 75 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 76 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 77 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 78 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 79 | VLR_BASE_REDU_ICMSS | NUMBER(17,2) | Y |  |  |
| 80 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 81 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 82 | GRUPO_SITUACAO_A | VARCHAR2(9) | Y |  |  |
| 83 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 84 | GRUPO_SITUACAO_B | VARCHAR2(9) | Y |  |  |
| 85 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 86 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 87 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 88 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 89 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 90 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 91 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 92 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 93 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 94 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 95 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 96 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 97 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 98 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IDX_DWT_CODS_LOOKUP: (COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP)

---

## DWT_ITENS_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |
| 2 | IDENT_ITEM_MERC | NUMBER(12) | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 14 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 15 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 16 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 17 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 18 | VALID_BEM | DATE | Y |  |  |
| 19 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 20 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 21 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 22 | DESCRICAO_COMPL | VARCHAR2(255) | Y |  |  |
| 23 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 24 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 25 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 26 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 27 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 28 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 29 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 30 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 31 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 32 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 33 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 34 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 35 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 36 | IDENT_FEDERAL | NUMBER(12) | Y |  |  |
| 37 | IND_IPI_INCLUSO | CHAR(1) | Y |  |  |
| 38 | NUM_ROMANEIO | VARCHAR2(12) | Y |  |  |
| 39 | DATA_ROMANEIO | DATE | Y |  |  |
| 40 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 41 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 42 | VLR_ITEM_CONVER | NUMBER(17,2) | Y |  |  |
| 43 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 44 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 45 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 46 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 47 | VLR_OUTROS3 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_OUTROS4 | NUMBER(17,2) | Y |  |  |
| 49 | VLR_OUTROS5 | NUMBER(17,2) | Y |  |  |
| 50 | VLR_ALIQ_OUTROS1 | NUMBER(7,4) | Y |  |  |
| 51 | VLR_ALIQ_OUTROS2 | NUMBER(7,4) | Y |  |  |
| 52 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 53 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 54 | DIF_ALIQ_TRIB_ICMS | NUMBER(7,4) | Y |  |  |
| 55 | OBS_TRIBUTO_ICMS | VARCHAR2(45) | Y |  |  |
| 56 | IDENT_DET_OP_ICMS | NUMBER(12) | Y |  |  |
| 57 | ALIQ_TRIBUTO_IPI | NUMBER(7,4) | Y |  |  |
| 58 | VLR_TRIBUTO_IPI | NUMBER(17,2) | Y |  |  |
| 59 | OBS_TRIBUTO_IPI | VARCHAR2(45) | Y |  |  |
| 60 | IDENT_DET_OP_IPI | NUMBER(12) | Y |  |  |
| 61 | ALIQ_TRIBUTO_ICMSS | NUMBER(7,4) | Y |  |  |
| 62 | VLR_TRIBUTO_ICMSS | NUMBER(17,2) | Y |  |  |
| 63 | OBS_TRIBUTO_ICMSS | VARCHAR2(45) | Y |  |  |
| 64 | IDENT_DET_OP_ICMSS | NUMBER(12) | Y |  |  |
| 65 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 66 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 67 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 68 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 69 | VLR_BASE_IPI_1 | NUMBER(17,2) | Y |  |  |
| 70 | VLR_BASE_IPI_2 | NUMBER(17,2) | Y |  |  |
| 71 | VLR_BASE_IPI_3 | NUMBER(17,2) | Y |  |  |
| 72 | VLR_BASE_IPI_4 | NUMBER(17,2) | Y |  |  |
| 73 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 74 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 75 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 76 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 77 | COD_OBS_VCONT_COMP | VARCHAR2(10) | Y |  |  |
| 78 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 79 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  |  |
| 80 | VLR_OUTROS_IPI | NUMBER(17,2) | Y |  |  |
| 81 | IND_RESP_VCONT_ITM | CHAR(1) | Y |  |  |
| 82 | NUM_ATO_CONCES | VARCHAR2(15) | Y |  |  |
| 83 | DAT_EMBARQUE | DATE | Y |  |  |
| 84 | NUM_REG_EXP | VARCHAR2(12) | Y |  |  |
| 85 | NUM_DESP_EXP | VARCHAR2(11) | Y |  |  |
| 86 | VLR_TOM_SERVICO | NUMBER(17,2) | Y |  |  |
| 87 | VLR_DESP_MOEDA_EXP | NUMBER(17,2) | Y |  |  |
| 88 | COD_MOEDA_NEGOC | VARCHAR2(10) | Y |  |  |
| 89 | COD_PAIS_DEST_ORIG | VARCHAR2(3) | Y |  |  |
| 90 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 91 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 92 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 93 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 94 | VLR_CONT_IT_IN | NUMBER(17,2) | Y |  |  |
| 95 | VLR_ICMS_IN | NUMBER(17,2) | Y |  |  |
| 96 | VLR_ICMS_B1_IN | NUMBER(17,2) | Y |  |  |
| 97 | VLR_ICMS_B2_IN | NUMBER(17,2) | Y |  |  |
| 98 | VLR_ICMS_B3_IN | NUMBER(17,2) | Y |  |  |
| 99 | VLR_ICMS_B4_IN | NUMBER(17,2) | Y |  |  |
| 100 | VLR_IPI_IN | NUMBER(17,2) | Y |  |  |
| 101 | VLR_IPI_B1_IN | NUMBER(17,2) | Y |  |  |
| 102 | VLR_IPI_B2_IN | NUMBER(17,2) | Y |  |  |
| 103 | VLR_IPI_B3_IN | NUMBER(17,2) | Y |  |  |
| 104 | VLR_IPI_B4_IN | NUMBER(17,2) | Y |  |  |
| 105 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 106 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 107 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 108 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 109 | BASE_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 110 | VLR_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 111 | ALIQ_ICMS_ORIGDEST | NUMBER(7,4) | Y |  |  |
| 112 | VLR_DESC_CONDIC | NUMBER(17,2) | Y |  |  |
| 113 | VLR_BASE_ICMSS_2 | NUMBER(17,2) | Y |  |  |
| 114 | VLR_BASE_ICMSS_3 | NUMBER(17,2) | Y |  |  |
| 115 | VLR_BASE_ICMSS_4 | NUMBER(17,2) | Y |  |  |
| 116 | VLR_CUSTO_TRANSF | NUMBER(17,6) | Y |  |  |
| 117 | PERC_RED_BASE_ICMS | NUMBER(7,4) | Y |  |  |
| 118 | QTD_EMBARCADA | NUMBER(17,6) | Y |  |  |
| 119 | DAT_REGISTRO_EXP | DATE | Y |  |  |
| 120 | DAT_DESPACHO | DATE | Y |  |  |
| 121 | DAT_AVERBACAO | DATE | Y |  |  |
| 122 | DAT_DI | DATE | Y |  |  |
| 123 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 124 | DSC_MOT_OCOR | VARCHAR2(45) | Y |  |  |
| 125 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 126 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 127 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 128 | VLR_BASE_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 129 | VLR_TRIB_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 130 | VLR_PERC_PRES_ICMS | NUMBER(7,4) | Y |  |  |
| 131 | VLR_PRECO_BASE_ST | NUMBER(17,2) | Y |  |  |
| 132 | IDENT_OPER_OIL | NUMBER(12) | Y |  |  |
| 133 | COD_DCR | VARCHAR2(15) | Y |  |  |
| 134 | IDENT_PROJETO | NUMBER(12) | Y |  |  |
| 135 | DAT_OPERACAO | DATE | Y |  |  |
| 136 | USUARIO | VARCHAR2(40) | Y |  |  |
| 137 | IND_MOV_FIS | CHAR(1) | Y |  |  |
| 138 | CHASSI | VARCHAR2(17) | Y |  |  |
| 139 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 140 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 141 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 142 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 143 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 144 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 145 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 146 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 147 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 148 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 149 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 150 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 151 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 152 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 153 | IND_FORNEC_ICMSS | CHAR(1) | Y |  | Indicador de Situação de ICMSS do Fornedor - 1 = Substituto, 2 = Substituído |
| 154 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 155 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 156 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 157 | DAT_PGTO_GNRE_DARJ | DATE | Y |  |  |
| 158 | VLR_CUSTO_UNIT | NUMBER(17,2) | Y |  |  |
| 159 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 160 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 161 | VLR_FECP_ICMS | NUMBER(17,2) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 162 | VLR_FECP_DIFALIQ | NUMBER(17,2) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 163 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 164 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  | Campo utilizado para lancamento do valor do FUNCEP ref a Regime Fonte - GIM-PB |
| 165 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  | Valor base do ICMS-ST não escriturado |
| 166 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  | Valor do ICMS-ST não escriturado |
| 167 | COD_TRIB_IPI | VARCHAR2(2) | Y |  | código de tributação do IPI - CTIPI - ato cotepe 35/05 |
| 168 | LOTE_MEDICAMENTO | VARCHAR2(50) | Y |  | número do lote de fabricação do medicamento - ato cotepe 35/05 |
| 169 | VALID_MEDICAMENTO | DATE | Y |  | data de expedição da validade do medicamento - ato cotepe 35/05 |
| 170 | IND_BASE_MEDICAMENTO | CHAR(1) | Y |  | indicador do tipo da base de cálculo: 0 - BC ref ao preço tabelado ou preço máximo, 1 - BC ref à Lista Negativa, 2 - BC ref à Lista Positiva, 3 - BC ref à Lista Neutra  - ato cotepe 35/05 |
| 171 | VLR_PRECO_MEDICAMENTO | NUMBER(17,2) | Y |  | valor do preço tabelado ou do preço máximo do medicamento - ato cotepe 35/05 |
| 172 | IND_TIPO_ARMA | CHAR(1) | Y |  | indicador do tipo de arma: 0- uso permitido, 1 - uso restrito - ato cotepe 35/05 |
| 173 | NUM_SERIE_ARMA | VARCHAR2(50) | Y |  | numeração de série de fabricação da arma - ato cotepe 35/05 |
| 174 | NUM_CANO_ARMA | VARCHAR2(50) | Y |  | numeração de série de fabricação do cano - ato cotepe 35/05 |
| 175 | DSC_ARMA | VARCHAR2(100) | Y |  | descrição da arma - ato cotepe 35/05 |
| 176 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 35/05 |
| 177 | COD_EX_NCM | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C300: Código EX, conforme a TIPI. |
| 178 | COD_EX_IMP | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C300: Código EX do Imposto de Importação. |
| 179 | CNPJ_OPERADORA | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: CNPJ do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 180 | CPF_OPERADORA | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: CPF do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 181 | IDENT_UF_OPERADORA | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: UF do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 182 | INS_EST_OPERADORA | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: Inscrição Estadual do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 183 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: Especificação do Tipo de Receita (energia elétrica, gás, água, telecomunicação, comunicação). Valores Assumidos: 0 - Receita Própria - serviços prestados; 1 - Receita Própria - cobrança de débitos; 2 - Receita Própria - venda de mercadorias; 3 - Receita Própria - venda de serviço pré-pago; 4 - Outras Receitas Próprias; 5 - Receita de Terceiros (co-faturamento); 9 - Outras Receitas de Terceiros. |
| 184 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: Classificação do Item. Preenchimento conforme tabela 11.5 do Convênio 115/133 (energia elétrica, gás, água, telecomunicação, comunicação). |
| 185 | VLR_TERCEIROS | NUMBER(17,2) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 186 | VLR_PRECO_SUGER | NUMBER(17,2) | Y |  | Valor do preco sugerido do produto - Meio Magnetico - Reg78 - CAT 90 - SP |
| 187 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 188 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 189 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 190 | COD_OPER_ESP_ST | CHAR(1) | Y |  | Atendimento DIEF-PA. |
| 191 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 192 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 193 | VLR_DIFAL_FRETE | NUMBER(17,2) | Y |  |  |
| 194 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' | Indicador para verificar se os valores de PIS/COFINS estao destacados no documentos fiscal |
| 195 | COD_ENQUAD_IPI | VARCHAR2(3) | Y |  | Código de Enquadramento Legal do IPI |
| 196 | COD_SITUACAO_PIS | NUMBER(2) | Y |  | Codigo da Situação Tributaria do PIS |
| 197 | QTD_BASE_PIS | NUMBER(18,3) | Y |  | Quantidade de Base de Calculo do PIS |
| 198 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  | VALOR DA ALIQUOTA DO PIS EM REAIS |
| 199 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  | CODIGO DA SITUAÇÃO TRIBUTARIA DO COFINS |
| 200 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  | Quantidade de Base de Calculo do COFINS |
| 201 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  | VALOR DA ALIQUOTA DO COFINS EM REAIS |
| 202 | ITEM_PORT_TARE | VARCHAR2(2) | Y |  |  |
| 203 | VLR_FUNRURAL | NUMBER(17,2) | Y |  | Campo criado para gerar o registro 88NFRA do sintegra. |
| 204 | IND_TP_PROD_MEDIC | CHAR(1) | Y |  |  |
| 205 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 206 | COD_TP_LANCTO | NUMBER(6) | Y |  |  |
| 207 | VLR_PERC_CRED_OUT | NUMBER(7,4) | Y |  |  |
| 208 | VLR_CRED_OUT | NUMBER(17,2) | Y |  |  |
| 209 | VLR_ICMS_DCA | NUMBER(21,6) | Y |  |  |
| 210 | VLR_PIS_EXP | NUMBER(17,2) | Y |  |  |
| 211 | VLR_PIS_TRIB | NUMBER(17,2) | Y |  |  |
| 212 | VLR_PIS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 213 | VLR_COFINS_EXP | NUMBER(17,2) | Y |  |  |
| 214 | VLR_COFINS_TRIB | NUMBER(17,2) | Y |  |  |
| 215 | VLR_COFINS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 216 | COD_ENQ_LEGAL | NUMBER(4) | Y |  |  |
| 217 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |
| 218 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 219 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 220 | IND_NATUREZA_FRETE | CHAR(1) | Y |  |  |
| 221 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 222 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 223 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 224 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |
| 225 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |
| 226 | INDICE_PROD_ACAB | VARCHAR2(3) | Y |  |  |
| 227 | VLR_BASE_DIA_AM | NUMBER(17,2) | Y |  |  |
| 228 | VLR_ALIQ_DIA_AM | NUMBER(7,4) | Y |  |  |
| 229 | VLR_ICMS_DIA_AM | NUMBER(17,2) | Y |  |  |
| 230 | VLR_ADUANEIRO | NUMBER(17,2) | Y |  |  |
| 231 | COD_SITUACAO_PIS_ST | NUMBER(2) | Y |  |  |
| 232 | COD_SITUACAO_COFINS_ST | NUMBER(2) | Y |  |  |
| 233 | VLR_ALIQ_DCIP | NUMBER(7,4) | Y |  |  |
| 234 | NUM_LI | VARCHAR2(10) | Y |  |  |
| 235 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 236 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 237 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 238 | VLR_DIF_DUB | NUMBER(17,2) | Y |  |  |
| 239 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 240 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 241 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 242 | IND_MOTIVO_RES | CHAR(1) | Y |  |  |
| 243 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  |  |
| 244 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  |  |
| 245 | NUM_AUTENTIC_NFE_RET | VARCHAR2(80) | Y |  |  |
| 246 | NUM_ITEM_RET | NUMBER(5) | Y |  |  |
| 247 | IDENT_FIS_JUR_RET | NUMBER(12) | Y |  |  |
| 248 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 249 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 250 | IDENT_CFO_DCIP | NUMBER(12) | Y |  |  |
| 251 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 252 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 253 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 254 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 255 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 256 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 257 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 258 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 259 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 260 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 261 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 262 | IDENT_PROC_ADJ_PRINC | NUMBER(12) | Y |  |  |
| 263 | IDENT_SUSP_TBT_PRINC | NUMBER(12) | Y |  |  |
| 264 | NUM_PROC_ADJ_PRINC | VARCHAR2(21) | Y |  |  |
| 265 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 266 | IDENT_PROC_ADJ_ADIC | NUMBER(12) | Y |  |  |
| 267 | IDENT_SUSP_TBT_ADIC | NUMBER(12) | Y |  |  |
| 268 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 269 | VLR_IPI_DEV | NUMBER(17,2) | Y |  |  |
| 270 | COD_BENEFICIO | VARCHAR2(10) | Y |  |  |
| 271 | VLR_ABAT_NTRIBUTADO | NUMBER(17,2) | Y |  |  |
| 272 | VLR_CREDITO_MVA_SN | NUMBER(17,2) | Y |  |  |
| 273 | VLR_DESONERADO_ICMS | NUMBER(17,2) | Y |  | Informar o valor desonerado do ICMS.  Este valor será apresentado através de código da tabela 5.2 "Tabela de Informações Adicionais da Apuração - Valores Declaratórios" para apresentação nos registros E115 e 1925. Conforme Resolução Sefaz 13 de 14/02/2019 - RJ. |
| 274 | VLR_DIFERIDO_ICMS | NUMBER(17,2) | Y |  | Informar o valor diferido do ICMS.  Este valor será apresentado através de código da tabela 5.2 "Tabela de Informações Adicionais da Apuração - Valores Declaratórios" para apresentação nos registros E115 e 1925. Conforme Resolução Sefaz 13 de 14/02/2019 - RJ. |
| 275 | VLR_EXC_BC_PIS | NUMBER(17,2) | Y |  |  |
| 276 | VLR_EXC_BC_COFINS | NUMBER(17,2) | Y |  |  |
| 277 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 278 | VLR_FECP_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 279 | COD_GRUPO_CCLASS | VARCHAR2(3) | Y |  |  |
| 280 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 281 | COD_AUTENTIC_NFE_ANT | VARCHAR2(44) | Y |  |  |
| 282 | NUM_ITEM_NFE_ANT | VARCHAR2(4) | Y |  |  |
| 283 | COD_CCLASS | VARCHAR2(7) | Y |  |  |
| 284 | CNPJ_OPER_LD | VARCHAR2(14) | Y |  |  |
| 285 | DAT_EXPIRA_CRED | DATE | Y |  |  |
| 286 | IND_DEVOLUCAO | VARCHAR2(1) | Y |  |  |
| 287 | TIPO_ITEM | VARCHAR2(1) | Y |  |  |
| 288 | IDENT_PRODUTO_ACABADO | NUMBER(12) | Y |  |  |
| 289 | IND_NF_ANT | VARCHAR2(1) | Y |  |  |
| 290 | NUM_GUIA_RECOL | VARCHAR2(16) | Y |  |  |
| 291 | DAT_EMISSAO_GUIA | DATE | Y |  |  |
| 292 | DAT_PAGTO_GUIA | DATE | Y |  |  |
| 293 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 294 | VLR_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 295 | IND_SOMA_FECP_ICMS_ST | VARCHAR2(1) | Y |  |  |
| 296 | QTD_PROD_20C | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → DWT_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IDX_DWT_ITENS_MERC_PRODUTO: (IDENT_PRODUTO)
- IX_DWT_ITENS_MCONTA: (IDENT_CONTA)
- IX_DWT_ITENS_MERC (UNIQUE): (IDENT_DOCTO_FISCAL, IDENT_ITEM_MERC)
- IX_DWT_ITE_MERC_01: (DAT_EMBARQUE, COD_ESTAB, COD_EMPRESA)
- IX_DWT_ITE_MERC_02: (COD_EMPRESA, COD_ESTAB, CHASSI, DATA_FISCAL, MOVTO_E_S)
- IX_DWT_ITE_MERC_03: (COD_EMPRESA, COD_ESTAB, DAT_AVERBACAO, MOVTO_E_S)
- IX_DWT_ITE_MERC_DAT_LANC_P_C: (COD_EMPRESA, COD_ESTAB, DAT_LANC_PIS_COFINS)
- IX_DWT_ITE_MERC_SAICS: (IDENT_PRODUTO, DATA_FISCAL, COD_ESTAB, COD_EMPRESA, COD_TP_LANCTO, MOVTO_E_S)
- IX_FK_IDENTFISJUR: (IDENT_FIS_JUR)

---

## DWT_ITENS_MERC_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ROW_ID_CAPA | ROWID | Y |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DATA_FISCAL | DATE | Y |  |  |
| 5 | DATA_EMISSAO | DATE | Y |  |  |
| 6 | DATA_SAIDA_REC | DATE | Y |  |  |
| 7 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 8 | NORM_DEV | CHAR(1) | Y |  |  |
| 9 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 14 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 15 | SITUACAO | CHAR(1) | Y |  |  |
| 16 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 17 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 18 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 19 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 20 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 21 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 22 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 23 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 24 | IDENT_MEDIDA_ITEM | NUMBER(12) | Y |  |  |
| 25 | IDENT_UND_PADRAO_ITEM | NUMBER(12) | Y |  |  |
| 26 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 27 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 28 | VLR_CREDITO_MVA_SN | NUMBER(17,2) | Y |  |  |
| 29 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 30 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  |  |
| 35 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 36 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 37 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 38 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 39 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 40 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 41 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 42 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 43 | DAT_DI | DATE | Y |  |  |
| 44 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 45 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 46 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 47 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 48 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 49 | IND_SIMPLES_NAC | CHAR(1) | Y |  |  |
| 50 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 51 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 52 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 53 | VALID_PRODUTO | DATE | Y |  |  |
| 54 | DSC_PRODUTO | VARCHAR2(50) | Y |  |  |
| 55 | COD_CEST | VARCHAR2(7) | Y |  |  |
| 56 | IDENT_NBM_PROD | NUMBER(12) | Y |  |  |
| 57 | IDENT_MEDIDA_PROD | NUMBER(12) | Y |  |  |
| 58 | IDENT_UND_PADRAO_PROD | NUMBER(12) | Y |  |  |
| 59 | GRUPO_MEDIDA_PROD | VARCHAR2(9) | Y |  |  |
| 60 | COD_MEDIDA_PROD | VARCHAR2(8) | Y |  |  |
| 61 | GRUPO_UND_PADRAO_PROD | VARCHAR2(9) | Y |  |  |
| 62 | COD_UND_PADRAO_PROD | VARCHAR2(8) | Y |  |  |
| 63 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 64 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 65 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 66 | GRUPO_MEDIDA_ITEM | VARCHAR2(9) | Y |  |  |
| 67 | COD_MEDIDA_ITEM | VARCHAR2(8) | Y |  |  |
| 68 | GRUPO_UND_PADRAO_ITEM | VARCHAR2(9) | Y |  |  |
| 69 | COD_UND_PADRAO_ITEM | VARCHAR2(8) | Y |  |  |
| 70 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 71 | IDENT_ESTADO | NUMBER | Y |  |  |
| 72 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 73 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 74 | IND_FORNEC_ICMSS | CHAR(1) | Y |  |  |
| 75 | ALIQ_TRIBUTO_ICMS | NUMBER | Y |  |  |
| 76 | ALIQ_TRIBUTO_ICMSS | NUMBER | Y |  |  |
| 77 | VLR_TRIBUTO_ICMS | NUMBER | Y |  |  |
| 78 | VLR_TRIBUTO_ICMSS | NUMBER | Y |  |  |
| 79 | VLR_BASE_ICMS_1 | NUMBER | Y |  |  |
| 80 | VLR_BASE_ICMSS | NUMBER | Y |  |  |
| 81 | VLR_BASE_REDU_ICMSS | NUMBER | Y |  |  |
| 82 | GRUPO_SITUACAO_A | VARCHAR2(9) | Y |  |  |
| 83 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 84 | GRUPO_SITUACAO_B | VARCHAR2(9) | Y |  |  |
| 85 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 86 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 87 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 88 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 89 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 90 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 91 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 92 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 93 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 94 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 95 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 96 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 97 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 98 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IDX_DWT_MERC_PRINCIPAL: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, NUM_ITEM)

---

## DWT_ITENS_SERV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |
| 2 | IDENT_ITEM_SERV | NUMBER(12) | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | MOVTO_E_S | CHAR(1) | N |  |  |
| 7 | NORM_DEV | CHAR(1) | N |  |  |
| 8 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 14 | NUM_ITEM | NUMBER(5) | N |  |  |
| 15 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 16 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 17 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 18 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 19 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 20 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 21 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 22 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 23 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 24 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 25 | VLR_SERVICO_CONV | NUMBER(18,4) | Y |  |  |
| 26 | ALIQ_TRIBUTO_ICMS | NUMBER(7,4) | Y |  |  |
| 27 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 28 | DIF_ALIQ_TRIB_ICMS | NUMBER(7,4) | Y |  |  |
| 29 | OBS_TRIBUTO_ICMS | VARCHAR2(45) | Y |  |  |
| 30 | IDENT_DET_OP_ICMS | NUMBER(12) | Y |  |  |
| 31 | ALIQ_TRIBUTO_IR | NUMBER(7,4) | Y |  |  |
| 32 | VLR_TRIBUTO_IR | NUMBER(17,2) | Y |  |  |
| 33 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |
| 34 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 35 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 36 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 37 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 38 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 39 | VLR_BASE_IR_1 | NUMBER(17,2) | Y |  |  |
| 40 | VLR_BASE_IR_2 | NUMBER(17,2) | Y |  |  |
| 41 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 42 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 43 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 44 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 45 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 46 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 47 | DAT_OPERACAO | DATE | Y |  |  |
| 48 | USUARIO | VARCHAR2(40) | Y |  |  |
| 49 | COMPL_ISENCAO | VARCHAR2(5) | Y |  |  |
| 50 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 51 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 52 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 53 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 54 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 55 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 56 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 57 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 58 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 59 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 60 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 35/05 |
| 61 | COD_TRIB_ISS | VARCHAR2(2) | Y |  | Ato Cotepe 70/05 - código de tributação do ISS - CTISS - view TRIBUTACAO_ISS_V |
| 62 | VLR_MAT_PROP | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do Material Próprio utilizado na prestação do serviço. |
| 63 | VLR_MAT_TERC | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do Material de Terceiros utilizado na prestação do serviço. |
| 64 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor da Base de Cálculo de Retenção de ISSQN. |
| 65 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do ISSQN retido pelo tomador. |
| 66 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg B020: Valor de dedução da base de cálculo do ISSQN. |
| 67 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 68 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 69 | VLR_OUT_DESP | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020 |
| 70 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 71 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 72 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 73 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 74 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' | Indicador para verificar se os valores de PIS/COFINS estao destacados no documentos fiscal |
| 75 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 76 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 77 | VLR_PIS_EXP | NUMBER(17,2) | Y |  |  |
| 78 | VLR_PIS_TRIB | NUMBER(17,2) | Y |  |  |
| 79 | VLR_PIS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 80 | VLR_COFINS_EXP | NUMBER(17,2) | Y |  |  |
| 81 | VLR_COFINS_TRIB | NUMBER(17,2) | Y |  |  |
| 82 | VLR_COFINS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 83 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 84 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 85 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 86 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 87 | IND_LOCAL_EXEC_SERV | CHAR(1) | Y |  |  |
| 88 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 89 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 90 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 91 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 92 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 93 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 94 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 95 | IDENT_NBS | NUMBER(12) | Y |  |  |
| 96 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 97 | VLR_TOT_RET | NUMBER(17,2) | Y |  |  |
| 98 | VLR_DEDUCAO_NF | NUMBER(17,2) | Y |  |  |
| 99 | VLR_RET_NF | NUMBER(17,2) | Y |  |  |
| 100 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 101 | VLR_ALIQ_ISS_RETIDO | NUMBER(7,4) | Y |  |  |
| 102 | COD_SIT_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 103 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 104 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 105 | VLR_DED_ALIM | NUMBER(17,2) | Y |  |  |
| 106 | VLR_DED_TRANS | NUMBER(17,2) | Y |  |  |
| 107 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 108 | IDENT_PROC_ADJ_PRINC | NUMBER(12) | Y |  |  |
| 109 | IDENT_SUSP_TBT_PRINC | NUMBER(12) | Y |  |  |
| 110 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 111 | IDENT_PROC_ADJ_ADIC | NUMBER(12) | Y |  |  |
| 112 | IDENT_SUSP_TBT_ADIC | NUMBER(12) | Y |  |  |
| 113 | NUM_PROC_ADJ_PREST_PRINC | VARCHAR2(21) | Y |  |  |
| 114 | NUM_PROC_ADJ_PREST_ADIC | VARCHAR2(21) | Y |  |  |
| 115 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 116 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 117 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 118 | VLR_ABAT_NTRIBUTADO | NUMBER(17,2) | Y |  |  |
| 119 | COD_ATIV_RJ | NUMBER(7) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → DWT_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_DWT_ITENS_SCONTA: (IDENT_CONTA)
- IX_DWT_ITENS_SERV (UNIQUE): (IDENT_DOCTO_FISCAL, IDENT_ITEM_SERV)
- IX_DW_ITENS_SERV_01: (DATA_FISCAL, MOVTO_E_S, COD_ESTAB, COD_EMPRESA, IDENT_DOCTO_FISCAL)
- IX_DW_ITENS_SERV_02: (COD_EMPRESA, COD_ESTAB, DAT_LANC_PIS_COFINS)
- IX_FK_SAF_2796: (IDENT_FIS_JUR)

---

## DWT_LAYOUT_AJUSTE_MASSA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TABLE_NAME | VARCHAR2(20) | Y |  |  |
| 2 | ITEM | VARCHAR2(4) | Y |  |  |
| 3 | COLUMNS_NAME | VARCHAR2(100) | Y |  |  |
| 4 | PRIMARY_KEY | VARCHAR2(1) | Y |  |  |

---

## DWT_MARCA_MODELO_ECF
**Comment**: Cadastro de Marcas e Modelos do Equipamento Emissor de Cupom Fiscal conforme Anexo III pela Portaria CAT nº 122/07

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MARCA_ECF | VARCHAR2(30) | N |  |  |
| 2 | COD_MODELO_ECF | VARCHAR2(30) | N |  |  |
| 3 | COD_FABRICANTE | VARCHAR2(2) | Y |  |  |
| 4 | NUM_SEQ_MODELO | VARCHAR2(2) | Y |  |  |

**PK**: COD_MARCA_ECF, COD_MODELO_ECF

---

## DWT_MEIO_PAGTO_ECF
**Comment**: Cadastro dos Meios de Pagamento do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_MEIO_PAGTO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 5 | COD_MODELO | VARCHAR2(2) | N |  | Código do Modelo do documento (X2024_MODELO_DOCTO) emitido pelo ECF.Código do Modelo e Número do Caixa do ECF cadastrados na X2087_EQUIPAMENTO_ECF. |
| 6 | COD_CAIXA_ECF | VARCHAR2(3) | N |  | Número do Caixa do ECF cadastrado na X2087_EQUIPAMENTO_ECF. |
| 7 | COD_MEIO_PAGTO | VARCHAR2(2) | N |  |  |
| 8 | VALID_MEIO_PAGTO | DATE | N |  |  |
| 9 | DSC_MEIO_PAGTO | VARCHAR2(15) | Y |  |  |

**PK**: IDENT_MEIO_PAGTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_DWT_MEIO_PAGTO_ECF: (COD_ESTAB, COD_CAIXA_ECF, COD_MEIO_PAGTO, COD_EMPRESA, COD_MODELO, GRUPO_MODELO, VALID_MEIO_PAGTO)

---

## DWT_MODELO_MUNICIPAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNIC_MSAF | NUMBER(7) | N |  |  |
| 3 | COD_MODELO_NF | VARCHAR2(3) | N |  |  |
| 4 | DSC_MODELO_NF | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNIC_MSAF, COD_MODELO_NF

---

## DWT_NAT_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CST_PIS_COFINS | NUMBER(2) | N |  |  |
| 2 | COD_NAT_REC | NUMBER(3) | N |  |  |
| 3 | DAT_VALIDADE | DATE | N |  |  |
| 4 | DSC_NAT_REC | VARCHAR2(2000) | N |  |  |
| 5 | DAT_VALIDADE_FINAL | DATE | Y |  |  |

**PK**: COD_CST_PIS_COFINS, COD_NAT_REC, DAT_VALIDADE

---

## DWT_OPERADORA_SAUDE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 2 | NUM_CNPJ | VARCHAR2(14) | Y |  |  |
| 3 | NOM_EMPRESARIAL | VARCHAR2(150) | Y |  |  |
| 4 | NUM_REG_ANS | VARCHAR2(10) | Y |  |  |

**PK**: COD_OPER_SAUDE

---

## DWT_PFJ_CLASSE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 2 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 3 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 4 | IND_CLASSE | VARCHAR2(2) | N |  |  |

**PK**: GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, IND_CLASSE

---

## DWT_PFJ_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DWT_PROC_REF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 2 | GRUPO_PROC_REF | VARCHAR2(9) | N |  |  |
| 3 | NUM_PROC_REF | VARCHAR2(20) | N |  |  |
| 4 | VALID_PROC_REF | DATE | N |  |  |
| 5 | TP_PROC_REF | CHAR(1) | Y |  |  |
| 6 | DT_DECISAO | DATE | Y |  |  |
| 7 | NATUREZA_ACAO | NUMBER(2) | Y |  |  |
| 8 | SECAO_JUDICIARIA | VARCHAR2(100) | Y |  |  |
| 9 | VARA | VARCHAR2(2) | Y |  |  |
| 10 | DESC_RESUMIDA | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_PROC_REF

**FKs**:
- GRUPO_PROC_REF → GRUPO_ESTAB(GRUPO_ESTAB)

---

## DWT_PRODUTO_SEF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROD_SEF | VARCHAR2(14) | N |  |  |
| 2 | DESCR_PROD_SEF | VARCHAR2(50) | Y |  |  |
| 3 | UNID_PROD_SEF | VARCHAR2(3) | Y |  |  |

**PK**: COD_PROD_SEF

---

## DWT_REGIOES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_REGIAO | NUMBER(2) | N |  |  |
| 2 | DSC_REGIAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_REGIAO

---

## DWT_REL_CONF_PISCOF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCGER_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | TIPO_ORIGEM | VARCHAR2(2) | Y |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 6 | DATA_INI | DATE | Y |  |  |
| 7 | DATA_FIM | DATE | Y |  |  |
| 8 | PRODUTO | VARCHAR2(200) | Y |  |  |
| 9 | NUM_ITEM | NUMBER(3) | Y |  |  |
| 10 | QTDE_ITEM | NUMBER(17,6) | Y |  |  |
| 11 | VLR_UNIT_ITEM | NUMBER(19,4) | Y |  |  |
| 12 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 13 | CFOP | VARCHAR2(4) | Y |  |  |
| 14 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 17 | VLR_QTDE_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 18 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 19 | CST_PIS | VARCHAR2(200) | Y |  |  |
| 20 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 23 | VLR_QTDE_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 24 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 25 | CST_COFINS | VARCHAR2(200) | Y |  |  |
| 26 | DATA_DOC | DATE | Y |  |  |
| 27 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 28 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 29 | MODELO_DOC | VARCHAR2(200) | Y |  |  |
| 30 | NORM_DEV | VARCHAR2(200) | Y |  |  |
| 31 | TIPO_DOC | VARCHAR2(200) | Y |  |  |
| 32 | NUM_DOCFIS | VARCHAR2(200) | Y |  |  |
| 33 | UF_DOC | VARCHAR2(2) | Y |  |  |
| 34 | COD_FIS_JUR | VARCHAR2(200) | Y |  |  |
| 35 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |

**PK**: PROCGER_ID, PROC_ID

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

**Indexes**:
- IX_DWT_REL_CONF_PISCOF_01: (PROC_ID)

---

## DWT_REL_CONF_PISCOF_MSG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCGER_ID | NUMBER(12) | N |  |  |
| 2 | PROC_ID | NUMBER(12) | N |  |  |
| 3 | SEQ | NUMBER(12) | N |  |  |
| 4 | MSG | VARCHAR2(4000) | Y |  |  |

**PK**: PROCGER_ID, PROC_ID, SEQ

**FKs**:
- PROCGER_ID, PROC_ID → DWT_REL_CONF_PISCOF(PROCGER_ID, PROC_ID)

---

## DWT_SERVICO_LEI_116
**Comment**: Código de Serviço conforme lista Anexo I da Lei Complementar 116/03 - Ato Cotepe 70/05

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SERV_LEI_116 | NUMBER(12) | N |  |  |
| 2 | COD_SERV_LEI_116 | VARCHAR2(4) | Y |  |  |
| 3 | VALID_SERV_LEI_116 | DATE | Y |  |  |
| 4 | DSC_SERV_LEI_116 | VARCHAR2(100) | Y |  |  |
| 5 | TIPO_SERV_LEI_116 | CHAR(1) | Y |  |  |

**PK**: IDENT_SERV_LEI_116

**Indexes**:
- UK_SERV_LEI_116 (UNIQUE): (COD_SERV_LEI_116, VALID_SERV_LEI_116)

---

## DWT_SUB_AMP_LEGAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 3 | DAT_VALIDADE | DATE | N |  |  |
| 4 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | N |  |  |
| 5 | DSC_OCORRENCIA | VARCHAR2(100) | Y |  |  |
| 6 | DSC_LEGISLACAO | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_ESTADO, COD_AMPARO_LEGAL, DAT_VALIDADE, COD_SUB_ITEM_OCORR

**FKs**:
- IDENT_ESTADO, COD_AMPARO_LEGAL, DAT_VALIDADE → DWT_AMPARO_LEGAL(IDENT_ESTADO, COD_AMPARO_LEGAL, DAT_VALIDADE)

---

## DWT_TIPO_MOV_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_MOV_EST | VARCHAR2(2) | N |  |  |
| 2 | DAT_VALID_INI | DATE | N |  |  |
| 3 | DAT_VALID_FIM | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(70) | Y |  |  |
| 5 | IND_ENT_SAI | CHAR(1) | Y |  |  |

**PK**: COD_TIPO_MOV_EST, DAT_VALID_INI

---

## DWT_TOTALIZADOR_OBRIG_ECF
**Comment**: Parametrização do Totalizador Parcial definido nas obrigações fiscais. Ex: Redf e Sped-Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_TIPO_OBRIG | CHAR(1) | N |  | DOMÍNIO: 1 - REDF, 2 - EFD |
| 2 | COD_TOTALIZADOR_OBRIG | VARCHAR2(7) | N |  |  |
| 3 | DSC_TOTALIZADOR_OBRIG | VARCHAR2(50) | Y |  |  |
| 4 | IND_TIPO_OPER | CHAR(1) | Y |  | DOMÍNIO: 1-ICMS, 2-ISSQN, 3-NÃO FISCAL, 4-IOF |

**PK**: COD_TOTALIZADOR_OBRIG, IND_TIPO_OBRIG

**Indexes**:
- IX_DWT_TOTALIZADOR_OBRIG_ECF: (IND_TIPO_OBRIG, IND_TIPO_OPER, COD_TOTALIZADOR_OBRIG)

---

## DWT_TP_COD_EAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_COD_EAN | VARCHAR2(5) | N |  |  |
| 2 | DSC_EAN | VARCHAR2(50) | Y |  |  |

**PK**: TIPO_COD_EAN

---

## DWT_TRIBUTACAO_INT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIB_INT | NUMBER(5) | N |  |  |
| 2 | DSC_TRIB_INT | VARCHAR2(100) | Y |  |  |
| 3 | VLR_ALIQ_TRIB_INT | NUMBER(7,4) | Y |  |  |
| 4 | COD_TRIB_REL | VARCHAR2(5) | Y |  |  |
| 5 | COD_TRIB_MM | VARCHAR2(4) | Y |  |  |
| 6 | COD_TRIB_DIEF_CE | VARCHAR2(4) | Y |  |  |
| 7 | COD_TRIB_ATO_COTEPE | VARCHAR2(10) | Y |  |  |

**PK**: COD_TRIB_INT

---

## DWT_TRIBUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 2 | DSC_ABREV | VARCHAR2(15) | Y |  |  |
| 3 | DSC_COMPLETA | VARCHAR2(100) | Y |  |  |
| 4 | IND_IMPOSTO | CHAR(1) | Y |  |  |
| 5 | ORG_ARRECAD | VARCHAR2(30) | Y |  |  |

**PK**: COD_TRIBUTO

---

## DWT_TRIBUTO_ESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 2 | ESP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 3 | DSC_ESP_ABREV | VARCHAR2(15) | Y |  |  |
| 4 | DSC_ESP_COMPL | VARCHAR2(100) | Y |  |  |
| 5 | IND_AREA_NEG | CHAR(1) | Y |  |  |
| 6 | IND_ESTAB | CHAR(1) | Y |  |  |
| 7 | IND_UNID_NEG | CHAR(1) | Y |  |  |
| 8 | IND_CENTRO_RESP | CHAR(1) | Y |  |  |
| 9 | IND_LOCALIDADE | CHAR(1) | Y |  |  |
| 10 | IND_SERVICO | CHAR(1) | Y |  |  |
| 11 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 12 | IND_MERC_EXT_INT | CHAR(1) | Y |  |  |
| 13 | IND_UF | CHAR(1) | Y |  |  |
| 14 | IND_PAIS | CHAR(1) | Y |  |  |
| 15 | COD_REL | VARCHAR2(2) | Y |  |  |
| 16 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 17 | COD_ARREC_ESTAD | VARCHAR2(4) | Y |  |  |
| 18 | COD_ARREC_MUNIC | VARCHAR2(4) | Y |  |  |
| 19 | IND_DAT_COMP_AUT | CHAR(1) | Y |  |  |
| 20 | IND_PERIODIC | CHAR(1) | Y |  |  |

**PK**: COD_TRIBUTO, ESP_TRIBUTO

**FKs**:
- COD_TRIBUTO → DWT_TRIBUTO(COD_TRIBUTO)

---

## DWT_TRIB_ESP_REGRA
**Comment**: Tabela das Regras para Calculo do Vencimento dos DARFs

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 2 | ESP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 3 | DAT_VALIDADE_INI | DATE | N |  |  |
| 4 | IND_PERIODICIDADE | CHAR(1) | Y |  |  |
| 5 | NUM_DIAS_CORR_ANT | NUMBER(3) | Y |  |  |
| 6 | NUM_DIAS_CORR_POS | NUMBER(3) | Y |  |  |
| 7 | NUM_DIAS_UTEIS | NUMBER(3) | Y |  |  |
| 8 | IND_ULT_DIA_UTIL | CHAR(1) | Y |  |  |
| 9 | COD_DARF | VARCHAR2(4) | N |  |  |

**PK**: COD_TRIBUTO, ESP_TRIBUTO, DAT_VALIDADE_INI, COD_DARF

**FKs**:
- COD_TRIBUTO, ESP_TRIBUTO → DWT_TRIBUTO_ESP(COD_TRIBUTO, ESP_TRIBUTO)

---

## DWT_TRIB_TAXAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 2 | ESP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 3 | DAT_VALID | DATE | N |  |  |
| 4 | VLR_JUROS_DIA | NUMBER(7,4) | Y |  |  |
| 5 | VLR_JUROS_MES | NUMBER(7,4) | Y |  |  |
| 6 | VLR_MULTA_DIA | NUMBER(7,4) | Y |  |  |
| 7 | VLR_MULTA_MES | NUMBER(7,4) | Y |  |  |

**PK**: COD_TRIBUTO, ESP_TRIBUTO, DAT_VALID

---

## DWT_UF_REGIAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_REGIAO | NUMBER(2) | N |  |  |
| 3 | IDENT_ESTADO_REG | NUMBER(12) | N |  |  |
| 4 | ALIQ_ICMS_S | NUMBER(7,4) | Y |  |  |

**PK**: IDENT_ESTADO, COD_REGIAO, IDENT_ESTADO_REG

**FKs**:
- IDENT_ESTADO, COD_REGIAO → DWT_DEF_REGIAO(IDENT_ESTADO, COD_REGIAO)

---

