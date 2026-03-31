# Módulo: MISC (Prefixos pequenos) - 546 tabelas

Prefixos agrupados (237): ACT, AJT, AJU, ALIQ, ALIQUOTA, ANP, APURACAO, ATIV, ATT, AUD, AUDIT, BENEFICIOS, BRT, CAD2003, CALC, CALEND, CATEG, CATEGORIA, CCRED, CDT, CENTRAL, CENTRO, CFAB, CFO, CICD, CIEM, CISM, CLAS, CLASSE, CLASSIF, CLI, COD, COMPL, CONNECTION, CONSOLID, CONV, CPP, CPROC, CREDPIS, CT, CTEX, CTRL, DADOS, DBCONNECTION, DCA, DDS, DECLARACAO, DES, DETALHE, DFME, DFMS, DGCA, DIFERIMENTO, DIM, DIPJ, DIRF, DMS, DST, DW, ECF, ELEG, EMISSAO, EMIT, EMP, EMPRESA, ENVIO, EQUIPAMENTO, ESA, ESDRA, ESPECIE, ESTAB, ESTABELECIMENTO, ESTADO, ETAPA, FCONT, FICHAS, FILIAL, FPAR, FPM, FRT, GI, GP, GRUPO, GTIP, GUIA, HIST, HISTORICO, IBT, ICA, ICEM, ICP, ICSM, IDENT, IMP, IMPORTACAO, IMT, INCENTIVO, INCID, INCIDENCIA, INDU, INFEM, INIC, INT, INVC, INVENTARIO, IPI, IRP, ITF, JOB, JS, LANCTO, LAYOUT, LEGE, LESC, LINHAS, LIPI, LIVRO, LOCALIZACAO, LOG, LVR, MATERIAL, MEIO, MESTRE, MIBGE, MIDIA, MIT, MMAG, MODALIDADE, MODELO, MODULO, MONITOR, MOV0001, MOV0002, MTT, MUNICIPIO, MUT, MV, NACIONALIDADE, NAT, NATUREZA, NOTA, OBRIGACAO, OBS, OBSERVACAO, OLSS, OMS, OP, OPERACAO, OTF, OUT, PACKAGE, PAGINA, PAIS, PAISES, PAR, PARAMETRO, PARAMETROS, PBCATCOL, PBCATEDT, PBCATFMT, PBCATTBL, PBCATVLD, PLANO, PLT, PR, PRECO, PROCESS, PROCESSO, PROTOCOLO, RCP, REG, REGISTRO, REGRA, RELAC, RELAT, RES, RESP, RESPONSAVEL, RESUMO, RGR, ROBOT, SAFE01, SAFE196, SC, SCT, SEC, SECAO, SEGURANCA, SERV, SISTEMA, SIT, SLD, SMTP, SOFTWARE, SPA, ST, STG, STIP, SUBGRUPO, SX07, SX08, SX09, SX3007, SX3008, SX3009, SX3042, SX3043, SX42, SX43, T1, TAB, TAEX, TB, TCOF, TEMP, TFT, TIPI, TIPO, TOTAL, TPIS, TPLD, TRANSF, TRIBUTACAO, TRIBUTO, UF, UNI, UNIDADE, UNIN, USUARIO, VIA, Y2025, Y2026, Y2027, Y2046, Y2085, Y2086, Y2087

## ACT_CAD_BEM
**Comment**: Tabela utilizada durante o processo de geração do Ato Cotepe 70 para armazenamento dos produtos e serviços movimentados

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_BEM | VARCHAR2(60) | N |  |  |
| 3 | COD_INC | VARCHAR2(6) | N |  |  |
| 4 | VALID_BEM | DATE | Y |  |  |
| 5 | COD_GEN | VARCHAR2(2) | Y |  |  |

**PK**: PROC_ID, COD_BEM, COD_INC

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## ACT_CAD_ITEM
**Comment**: Tabela utilizada durante o processo de geração do Ato Cotepe 70 para armazenamento dos produtos e serviços movimentados

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | IDENT_ITEM | NUMBER(12) | N |  |  |
| 3 | IND_PROD_SERV | CHAR(1) | N | 'P' |  |

**PK**: PROC_ID, IDENT_ITEM, IND_PROD_SERV

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## ACT_CAD_NAT_OP
**Comment**: Tabela utilizada durante o processo de geração do Ato Cotepe 70 para armazenamento dos códigos de natureza da operação

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: PROC_ID, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## ACT_CAD_OBRA
**Comment**: Tabela utilizada durante o processo de geração do Ato Cotepe 70

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 5 | COD_CANAL_DISTRIB | VARCHAR2(10) | N |  |  |

**PK**: PROC_ID, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, COD_CANAL_DISTRIB

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## ACT_CAD_OBS
**Comment**: Tabela utilizada durante o processo de geração do Ato Cotepe 70 para armazenamento das observações de doctos. fiscais

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_OBSERVACAO | VARCHAR2(9) | N |  |  |
| 3 | COD_OBSERVACAO | VARCHAR2(50) | N |  |  |
| 4 | COD_AMPARO_LEGAL | VARCHAR2(10) | N |  |  |
| 5 | IND_ORIGEM_OBS | CHAR(1) | Y |  |  |

**PK**: PROC_ID, GRUPO_OBSERVACAO, COD_OBSERVACAO, COD_AMPARO_LEGAL

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## ACT_CAD_PARTIC
**Comment**: Tabela utilizada durante o processo de geração do Ato Cotepe 70

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 5 | IE_SUBSTIT | VARCHAR2(14) | Y |  |  |

**PK**: PROC_ID, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## ACT_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PREG | VARCHAR2(10) | Y |  |  |
| 2 | PCODEMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | PCODESTAB | VARCHAR2(6) | Y |  |  |
| 4 | PDATAINI | DATE | Y |  |  |
| 5 | PDATAFIM | DATE | Y |  |  |
| 6 | PMUNESTAB | VARCHAR2(15) | Y |  |  |
| 7 | PGET_ECF | VARCHAR2(60) | Y |  |  |
| 8 | PGET_MOD | VARCHAR2(60) | Y |  |  |
| 9 | PGET_GDOC | VARCHAR2(15) | Y |  |  |
| 10 | PGET_CDOC | VARCHAR2(60) | Y |  |  |
| 11 | PIND_ESCR_SERV | VARCHAR2(1) | Y |  |  |
| 12 | PINDCENTR | VARCHAR2(1) | Y |  |  |
| 13 | PINDPARUF | VARCHAR2(1) | Y |  |  |
| 14 | PNUMPROC | NUMBER | Y |  |  |
| 15 | PLEIAUTE | VARCHAR2(6) | Y |  |  |
| 16 | PPERFIL | VARCHAR2(50) | Y |  |  |
| 17 | PINDDTEMISS | VARCHAR2(1) | Y |  |  |
| 18 | PINDCODITEM | VARCHAR2(1) | Y |  |  |
| 19 | PINDCODPART | VARCHAR2(1) | Y |  |  |

---

## AJT_CRED_RAT_PROP_REC_CUM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_AJT_CRED_RAT_PROP_REC_CUM | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TIP_CRED | VARCHAR2(3) | N |  |  |
| 5 | NAT_BASE_CRED | VARCHAR2(2) | N |  |  |
| 6 | VLR_ALIQ_PIS | NUMBER(7,4) | N |  |  |
| 7 | VLR_ALIQ_COFINS | NUMBER(7,4) | N |  |  |
| 8 | CST_PIS | NUMBER(2) | N |  |  |
| 9 | CST_COFINS | NUMBER(2) | N |  |  |

**Indexes**:
- UK_AJT_CRED_RAT_PROP_REC_CUM (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_TIP_CRED, NAT_BASE_CRED, VLR_ALIQ_PIS, VLR_ALIQ_COFINS, CST_PIS, CST_COFINS)

---

## AJU_OUTROS_CREDITOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | DTENTR | DATE | N |  |  |
| 4 | NUMDOC | VARCHAR2(15) | N |  |  |
| 5 | CADG_COD | VARCHAR2(16) | N |  |  |
| 6 | SERIE | VARCHAR2(5) | Y |  |  |
| 7 | CODAJUS | VARCHAR2(10) | Y |  |  |
| 8 | DESCRAJUS | VARCHAR2(250) | Y |  |  |
| 9 | VALAJUS | NUMBER | Y |  |  |

**PK**: EMPS_COD, FILI_COD, DTENTR, NUMDOC, CADG_COD

---

## ALIQUOTA_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 4 | UF_ORIGEM | VARCHAR2(2) | N |  |  |
| 5 | UF_DESTINO | VARCHAR2(2) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | DAT_VALIDADE_INI | DATE | N |  |  |
| 8 | IND_CRIT_APUR | CHAR(1) | Y |  |  |
| 9 | DAT_VALIDADE_FIM | DATE | Y |  |  |
| 10 | ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 11 | ALIQUOTA_OUTORGADA | NUMBER(7,4) | Y |  |  |
| 12 | ALIQUOTA_VLR_OPER | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, UF_ORIGEM, UF_DESTINO, COD_CFO, DAT_VALIDADE_INI

---

## ALIQUOTA_ESTADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 2 | IDENT_UF_ORIGEM | NUMBER(12) | N |  |  |
| 3 | IDENT_UF_DESTINO | NUMBER(12) | N |  |  |
| 4 | ALIQUOTA | NUMBER(7,4) | Y |  |  |

**PK**: COD_TRIBUTO, IDENT_UF_ORIGEM, IDENT_UF_DESTINO

**FKs**:
- COD_TRIBUTO → TRIBUTO(COD_TRIBUTO)

---

## ALIQUOTA_NCM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 4 | UF_ORIGEM | VARCHAR2(2) | N |  |  |
| 5 | UF_DESTINO | VARCHAR2(2) | N |  |  |
| 6 | DAT_VALIDADE_INI | DATE | N |  |  |
| 7 | COD_NCM | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, UF_ORIGEM, UF_DESTINO, DAT_VALIDADE_INI, COD_NCM

---

## ALIQUOTA_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 4 | UF_ORIGEM | VARCHAR2(2) | N |  |  |
| 5 | UF_DESTINO | VARCHAR2(2) | N |  |  |
| 6 | DAT_VALIDADE_INI | DATE | N |  |  |
| 7 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 8 | IND_PRODUTO | CHAR(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, UF_ORIGEM, UF_DESTINO, DAT_VALIDADE_INI, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## ALIQ_CFO_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 2 | IDENT_UF_ORIGEM | NUMBER(12) | N |  |  |
| 3 | IDENT_UF_DESTINO | NUMBER(12) | N |  |  |
| 4 | IDENT_CFO | NUMBER(12) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | ALIQUOTA | NUMBER(7,4) | Y |  |  |

**PK**: COD_TRIBUTO, IDENT_UF_ORIGEM, IDENT_UF_DESTINO, IDENT_CFO, IDENT_PRODUTO

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## ALIQ_CONTRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 4 | VALID_ALIQ_CONTRIB | DATE | N |  |  |
| 5 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, VALID_ALIQ_CONTRIB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ALIQ_EXTENSAO_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 4 | UF_ORIGEM | VARCHAR2(2) | N |  |  |
| 5 | UF_DESTINO | VARCHAR2(2) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 8 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 9 | DAT_VALIDADE_INI | DATE | N |  |  |
| 10 | IND_CRIT_APUR | CHAR(1) | Y |  |  |
| 11 | DAT_VALIDADE_FIM | DATE | Y |  |  |
| 12 | ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 13 | ALIQUOTA_OUTORGADA | NUMBER(7,4) | Y |  |  |
| 14 | ALIQUOTA_VLR_OPER | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, UF_ORIGEM, UF_DESTINO, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, DAT_VALIDADE_INI

---

## ALIQ_EXT_CFO_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 2 | IDENT_UF_ORIGEM | NUMBER(12) | N |  |  |
| 3 | IDENT_UF_DESTINO | NUMBER(12) | N |  |  |
| 4 | IDENT_CFO | NUMBER(12) | N |  |  |
| 5 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | ALIQUOTA | NUMBER(7,4) | Y |  |  |

**PK**: COD_TRIBUTO, IDENT_UF_ORIGEM, IDENT_UF_DESTINO, IDENT_CFO, IDENT_NATUREZA_OP, IDENT_PRODUTO

**FKs**:
- COD_TRIBUTO, IDENT_UF_ORIGEM, IDENT_UF_DESTINO, IDENT_CFO, IDENT_PRODUTO → ALIQ_CFO_PRODUTO(COD_TRIBUTO, IDENT_UF_ORIGEM, IDENT_UF_DESTINO, IDENT_CFO, IDENT_PRODUTO)

---

## ALIQ_MEDIA_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_BASE | NUMBER(2) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 6 | MES_MEDIA | NUMBER(2) | N |  |  |
| 7 | ANO_MEDIA | NUMBER(4) | N |  |  |
| 8 | VLR_TRIBUTADA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_MED_ALQ_COFINS | NUMBER(7,4) | Y |  |  |
| 14 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_MED_ALQ_PIS | NUMBER(7,4) | Y |  |  |
| 17 | VLR_BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CRED_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_MEDIA_ALIQ | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_BASE, ANO_BASE, COD_CFOP, MES_MEDIA, ANO_MEDIA

---

## ANP_TEMP_PRD_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_REF | VARCHAR2(6) | Y |  |  |
| 4 | COD_PROD | VARCHAR2(60) | Y |  |  |
| 5 | COD_OPER | VARCHAR2(20) | Y |  |  |
| 6 | QTD_PROD_ANP | NUMBER | Y |  |  |
| 7 | QTD_PROD_KG | NUMBER | Y |  |  |

---

## APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 6 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 7 | DAT_REALIZACAO | DATE | Y |  |  |
| 8 | DSC_OBSERVACAO | LONG | Y |  |  |
| 9 | DSC_OBS_SUBST | VARCHAR2(2000) | Y |  |  |
| 10 | DSC_OBS_FRETES | VARCHAR2(2000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO → OBRIGACAO_FISCAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO)

---

## APURACAO_JN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | DATE | Y |  |  |
| 6 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 7 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 8 | DAT_REALIZACAO | DATE | Y |  |  |
| 9 | DSC_OBSERVACAO | LONG | Y |  |  |
| 10 | DSC_OBS_SUBST | VARCHAR2(2000) | Y |  |  |
| 11 | DSC_OBS_FRETES | VARCHAR2(2000) | Y |  |  |
| 12 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: PROC_ID

**Indexes**:
- IX_APURACAO_JN: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_GRAVACAO)

---

## ATIV_ECONOMICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ATIVIDADE | NUMBER(7) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 3 | DAT_VALIDADE_INI | DATE | N | to_date('25/06/1998','dd/mm/yyyy') |  |

**PK**: COD_ATIVIDADE, DAT_VALIDADE_INI

---

## ATT_APURACAO_EMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 5 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 6 | DAT_REALIZACAO | DATE | Y |  |  |
| 7 | DSC_OBSERVACAO | LONG | Y |  |  |
| 8 | DSC_OBS_SUBST | VARCHAR2(2000) | Y |  |  |

**PK**: COD_EMPRESA, COD_TIPO_LIVRO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_TIPO_LIVRO → ATT_OBRIG_FIS_EMP(COD_EMPRESA, COD_TIPO_LIVRO)

---

## ATT_APURACAO_EMP_JN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_SITUACAO_APUR | CHAR(1) | Y |  |  |
| 6 | IND_VALID_APUR | CHAR(1) | Y |  |  |
| 7 | DAT_REALIZACAO | DATE | Y |  |  |
| 8 | DSC_OBSERVACAO | LONG | Y |  |  |
| 9 | DSC_OBS_SUBST | VARCHAR2(2000) | Y |  |  |
| 10 | COD_USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |

**PK**: PROC_ID

**Indexes**:
- IX_ATT_APURACAO_EMP_JN: (COD_EMPRESA, COD_TIPO_LIVRO, DAT_GRAVACAO)

---

## ATT_CAL_OBRIG_EMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | DAT_PREVISTA_REAL | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_TIPO_LIVRO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_TIPO_LIVRO → ATT_OBRIG_FIS_EMP(COD_EMPRESA, COD_TIPO_LIVRO)

---

## ATT_EMIS_LIVRO_EMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 3 | NUM_LIVRO | VARCHAR2(6) | Y |  |  |
| 4 | NUM_PAGINA_INICIAL | VARCHAR2(6) | Y |  |  |
| 5 | NUM_PAGINA_FINAL | VARCHAR2(6) | Y |  |  |
| 6 | DAT_APUR_INI | DATE | Y |  |  |
| 7 | DAT_APURACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_TIPO_LIVRO

**FKs**:
- COD_EMPRESA, COD_TIPO_LIVRO → ATT_OBRIG_FIS_EMP(COD_EMPRESA, COD_TIPO_LIVRO)

---

## ATT_OBRIG_FIS_EMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 3 | IND_PERIODICIDADE | VARCHAR2(2) | Y |  |  |
| 4 | MAX_PRAZO_EMISSAO | NUMBER(3) | Y |  |  |
| 5 | MAX_PRAZ_APRES | NUMBER(3) | Y |  |  |
| 6 | IND_TER_ABE_FEC | CHAR(1) | Y |  |  |
| 7 | IND_ENFEIXAMENTO | CHAR(1) | Y |  |  |
| 8 | MAX_OSC_PERMITE | NUMBER(3) | Y |  |  |
| 9 | NUM_PROTOCOLO | VARCHAR2(40) | Y |  |  |
| 10 | DAT_LIB_PROT | DATE | Y |  |  |
| 11 | N_MESES | NUMBER(3) | Y |  |  |
| 12 | INICIAR | CHAR(1) | Y |  |  |
| 13 | MAX_CONT | NUMBER(7) | Y |  |  |
| 14 | LIVRO_I | NUMBER(6) | Y |  |  |
| 15 | PAGINA_I | NUMBER(6) | Y |  |  |
| 16 | DESLOC_I | NUMBER(6) | Y |  |  |
| 17 | IND_LIVRO_UNICO | CHAR(1) | Y |  |  |
| 18 | VLR_LIM_PAGINA | NUMBER(4) | Y |  |  |
| 19 | COMPLEMENTO_TERMO | VARCHAR2(240) | Y |  |  |
| 20 | IND_CENTR_MARGEN | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_TIPO_LIVRO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## ATT_PFJ_MES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_PFJ | CHAR(1) | N |  |  |
| 4 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 7 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 8 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | N |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, IND_TP_PFJ, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

---

## ATT_PROD_MOVTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LANCTO | VARCHAR2(2) | N |  |  |
| 4 | IND_ICMS_IPI | CHAR(1) | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | NORM_DEV | CHAR(1) | N |  |  |
| 7 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 8 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 9 | DAT_MOVTO | DATE | N |  |  |
| 10 | NUM_DOCTO | VARCHAR2(15) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 14 | DISCRI_ESTOQUE | VARCHAR2(52) | N |  |  |
| 15 | NUM_ITEM | NUMBER(5) | N |  |  |
| 16 | QTD_MOVTO_TOT | NUMBER(17,6) | Y |  |  |
| 17 | QTD_MOVTO_UTIL | NUMBER(17,6) | Y |  |  |
| 18 | SALDO | NUMBER(17,6) | Y |  |  |
| 19 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 20 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 21 | VLR_ICMS_TOT | NUMBER(17,2) | Y |  |  |
| 22 | VLR_IPI_TOT | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_REL | NUMBER(17,2) | Y |  |  |
| 24 | VLR_IPI_REL | NUMBER(17,2) | Y |  |  |
| 25 | INS_COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 26 | INS_COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 27 | INS_MOVTO_E_S | CHAR(1) | Y |  |  |
| 28 | INS_NORM_DEV | CHAR(1) | Y |  |  |
| 29 | INS_GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 30 | INS_IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 31 | INS_DAT_MOVTO | DATE | Y |  |  |
| 32 | INS_NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 33 | INS_SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 34 | INS_SSERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 35 | INS_IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 36 | INS_DISCRI_ESTOQUE | VARCHAR2(52) | Y |  |  |
| 37 | INS_NUM_ITEM | NUMBER(5) | Y |  |  |
| 38 | NUM_DOCTO_ACAB | VARCHAR2(15) | N |  |  |
| 39 | SERIE_DOCFIS_ACAB | VARCHAR2(3) | N |  |  |
| 40 | SSERIE_DOCFIS_ACAB | VARCHAR2(2) | N |  |  |
| 41 | IDENT_PRODUTO_ACAB | NUMBER(12) | N |  |  |
| 42 | NUM_ITEM_ACAB | NUMBER(5) | N |  |  |
| 43 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 44 | USUARIO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LANCTO, IND_ICMS_IPI, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DAT_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM, NUM_DOCTO_ACAB, SERIE_DOCFIS_ACAB, SSERIE_DOCFIS_ACAB, IDENT_PRODUTO_ACAB, NUM_ITEM_ACAB

---

## ATT_RES_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_ENTRADA_SAIDA | CHAR(1) | Y |  |  |
| 6 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_NTRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 12 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 13 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  |  |
| 14 | VLR_IPI_INTEGRA_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_IPI_NINTEGRA_ICMS | NUMBER(17,2) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

**Indexes**:
- IX_ATT_RES_APUR: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_CFO)

---

## ATT_RES_APUR_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IND_ENTRADA_SAIDA | CHAR(1) | N |  |  |
| 6 | COD_CFO | VARCHAR2(4) | N |  |  |
| 7 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_NTRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 11 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 12 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 13 | VLR_IPI_INTEGRA_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_IPI_NINTEGRA_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## ATT_TOT_LIVROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_LIVRO | NUMBER(6) | N |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE1_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE2_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE3_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE1_IPI | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE2_IPI | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE3_IPI | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE1_ICMSS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_LIVRO

---

## AUDIT_T1_TABLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATAHORA | TIMESTAMP(6) | N |  |  |
| 2 | SESSAO | VARCHAR2(4000) | Y |  |  |
| 3 | TABELA | VARCHAR2(200) | Y |  |  |
| 4 | OPERACAO | VARCHAR2(100) | Y |  |  |
| 5 | ANTES | CLOB | Y |  |  |
| 6 | DEPOIS | CLOB | Y |  |  |
| 7 | RASTRO | VARCHAR2(4000) | Y |  |  |
| 8 | ID | VARCHAR2(4000) | Y |  |  |
| 9 | DATAREF | DATE | N |  |  |
| 10 | USUARIO | VARCHAR2(100) | Y |  |  |

**PK**: DATAREF, DATAHORA

**Indexes**:
- IX_AUDIT_T1_TABLE: (DATAREF, USUARIO, TABELA, OPERACAO, ID)

---

## AUD_OPER_TABLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATAHORA | TIMESTAMP(6) | Y |  |  |
| 2 | SESSAO | VARCHAR2(4000) | Y |  |  |
| 3 | TABELA | VARCHAR2(200) | Y |  |  |
| 4 | OPERACAO | VARCHAR2(100) | Y |  |  |
| 5 | ANTES | VARCHAR2(4000) | Y |  |  |
| 6 | DEPOIS | VARCHAR2(4000) | Y |  |  |
| 7 | RASTRO | VARCHAR2(4000) | Y |  |  |
| 8 | ID | VARCHAR2(4000) | Y |  |  |

**Indexes**:
- IX_AUD_OPER_TABLE: (TABELA, OPERACAO, ID, DATAHORA)

---

## BENEFICIOS_FISCAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_BENEF_FISCAL | NUMBER(12) | N |  |  |
| 4 | VALID_INICIAL | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_BENEF_FISCAL

---

## BRT_DET_JOB_EXC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_JOB_EXCLUSAO | NUMBER(12) | N |  |  |
| 2 | NUM_DET_JOB | NUMBER(3) | N |  |  |
| 3 | STATUS_DET_JOB | CHAR(1) | Y |  |  |
| 4 | DSC_TABELA_BANCO | VARCHAR2(30) | Y |  |  |
| 5 | DAT_EXEC_INI | DATE | Y |  |  |
| 6 | DAT_EXEC_FIM | DATE | Y |  |  |
| 7 | QTD_REGS_PROC | NUMBER(9) | Y |  |  |
| 8 | NUM_PROC_IMP | NUMBER(12) | Y |  |  |

**PK**: IDENT_JOB_EXCLUSAO, NUM_DET_JOB

---

## BRT_FECHAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRUPO | NUMBER(5) | N |  |  |
| 4 | ANO_FECH | NUMBER(4) | N |  |  |
| 5 | MES_FECH | NUMBER(2) | N |  |  |
| 6 | DT_FECH | DATE | Y |  |  |
| 7 | USU_FECH | VARCHAR2(40) | Y |  |  |
| 8 | DT_REAB | DATE | Y |  |  |
| 9 | USU_REAB | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRUPO, ANO_FECH, MES_FECH

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_GRUPO → BRT_GRUPO(COD_GRUPO)

---

## BRT_GRUPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO | NUMBER(5) | N |  |  |
| 2 | DSC_GRUPO | VARCHAR2(30) | Y |  |  |
| 3 | IND_SIS_USU | CHAR(1) | Y |  |  |

**PK**: COD_GRUPO

---

## BRT_GRUPO_TAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO | NUMBER(5) | N |  |  |
| 2 | NOME_TABELA_BANCO | VARCHAR2(30) | N |  |  |
| 3 | IND_ESPECIE | CHAR(1) | Y |  |  |

**PK**: COD_GRUPO, NOME_TABELA_BANCO

**FKs**:
- NOME_TABELA_BANCO → CAT_PRIOR_BR(NOME_TABELA_BANCO)
- COD_GRUPO → BRT_GRUPO(COD_GRUPO)

---

## BRT_JOB_BCK_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: NUM_JOB, COD_EMPRESA, COD_ESTAB

**FKs**:
- NUM_JOB → JOB_BCK(NUM_JOB)

---

## BRT_JOB_EXCLUSAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_JOB_EXCLUSAO | NUMBER(12) | N |  |  |
| 2 | STATUS_JOB | CHAR(1) | Y |  |  |
| 3 | DAT_PROG | DATE | Y |  |  |
| 4 | DAT_EXEC_INI | DATE | Y |  |  |
| 5 | DAT_EXEC_FIM | DATE | Y |  |  |
| 6 | DAT_REF_INI | DATE | Y |  |  |
| 7 | DAT_REF_FIM | DATE | Y |  |  |
| 8 | DSC_JOB | VARCHAR2(255) | Y |  |  |
| 9 | DSC_RESPONS_PROG | VARCHAR2(40) | Y |  |  |
| 10 | DSC_RESPONS_EXEC | VARCHAR2(40) | Y |  |  |
| 11 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 12 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 13 | DSC_DIR_WORK | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_JOB_EXCLUSAO, COD_EMPRESA, COD_ESTAB

---

## BRT_JOB_RES_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: NUM_JOB, COD_EMPRESA, COD_ESTAB

**FKs**:
- NUM_JOB → JOB_RESTORE(NUM_JOB)

---

## BRT_PADRAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PADRAO | NUMBER(2) | N |  |  |
| 3 | DSC_PADRAO | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_PADRAO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## BRT_PADRAO_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PADRAO | NUMBER(2) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA, COD_PADRAO, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_PADRAO → BRT_PADRAO(COD_EMPRESA, COD_PADRAO)

---

## BRT_PADRAO_GRUPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PADRAO | NUMBER(2) | N |  |  |
| 3 | COD_GRUPO | NUMBER(5) | N |  |  |

**PK**: COD_EMPRESA, COD_PADRAO, COD_GRUPO

**FKs**:
- COD_GRUPO → BRT_GRUPO(COD_GRUPO)
- COD_EMPRESA, COD_PADRAO → BRT_PADRAO(COD_EMPRESA, COD_PADRAO)

---

## CAD2003_EXCL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 2 | COD_CUSTO | VARCHAR2(50) | N |  | cod_cost_center  - TAX-BR |
| 3 | VALID_CUSTO | DATE | N |  | dat_insert_update  - TAX-BR |

**PK**: COD_CUSTO, VALID_CUSTO

---

## CALC_VALOR_DACON

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MESANO | NUMBER(6) | N |  |  |
| 4 | NUM_FICHA | VARCHAR2(3) | N |  |  |
| 5 | NUM_LINHA | NUMBER(2) | N |  |  |
| 6 | IND_DIG_CALC | NUMBER | N |  |  |
| 7 | VALOR | NUMBER(22,7) | Y |  |  |
| 8 | VLR_INTERNO | NUMBER(22,7) | Y |  |  |
| 9 | VLR_EXTERNO | NUMBER(22,7) | Y |  |  |
| 10 | OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 11 | VLR_CUMULATIVO | NUMBER(22,7) | Y |  |  |
| 12 | VLR_NAO_CUMULATIVO | NUMBER(22,7) | Y |  |  |
| 13 | COD_PRODUTO_DACON | VARCHAR2(10) | N |  |  |
| 14 | VLR_INTERNO_NAO_PROPORCIONAL | NUMBER(22,7) | Y |  |  |
| 15 | VLR_EXTERNO_NAO_PROPORCIONAL | NUMBER(22,7) | Y |  |  |
| 16 | NUM_FICHA_OLD | VARCHAR2(3) | Y |  |  |
| 17 | IDX_COL_VALOR | NUMBER | N | 1 |  |
| 18 | TIPO | CHAR(1) | Y |  |  |
| 19 | CNPJ | VARCHAR2(14) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB, MESANO, NUM_FICHA, COD_PRODUTO_DACON, NUM_LINHA, IND_DIG_CALC, IDX_COL_VALOR, CNPJ

---

## CALC_VALOR_RELAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MESANO | NUMBER(6) | N |  |  |
| 4 | RELATID | NUMBER | N |  |  |
| 5 | ITEMID | NUMBER | N |  |  |
| 6 | VALOR | NUMBER(20,5) | Y |  |  |
| 7 | OBSERVACAO | LONG | Y |  |  |
| 8 | IDENT_REGRA | NUMBER | N | 0 |  |
| 9 | IND_ERRO | CHAR(1) | Y | 'N' |  |
| 10 | IND_REG_INFORMADO | CHAR(1) | Y | 'C' | C - Valor Calculado, I - Valor Informado |
| 11 | IDX_COL_VALOR | NUMBER | N | 1 | índice responsável por identificar tanto um retorno quanto vários retornos de valor |
| 12 | OBSERVACAO_RELAT | VARCHAR2(155) | Y |  | Observacoes digitadas livremente pelo usuario |

**PK**: COD_EMPRESA, COD_ESTAB, MESANO, RELATID, ITEMID, IDENT_REGRA, IDX_COL_VALOR

---

## CALEND_OBRIGACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | DAT_PREVISTA_REAL | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO → OBRIGACAO_FISCAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO)

---

## CATEGORIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CATEGORIA | NUMBER(5) | N |  |  |
| 2 | DSC_CATEGORIA | VARCHAR2(50) | Y |  |  |

**PK**: COD_CATEGORIA

---

## CATEG_TAB_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CATEGORIA | NUMBER(5) | N |  |  |
| 2 | COD_TAB_PROC | NUMBER(5) | N |  |  |

**PK**: COD_CATEGORIA, COD_TAB_PROC

**FKs**:
- COD_CATEGORIA → CATEGORIA(COD_CATEGORIA)
- COD_TAB_PROC → TAB_PROC(COD_TAB_PROC)

---

## CCRED_PRES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CCRED_PRES | VARCHAR2(3) | N |  |  |
| 2 | DESC_CCRED_PRES | VARCHAR2(300) | N |  |  |
| 3 | LC_214_2025 | VARCHAR2(1500) | N |  |  |
| 4 | APROPRIA_VIA_NF | VARCHAR2(1) | N |  |  |
| 5 | APROPRIA_VIA_EVENTO | VARCHAR2(1) | N |  |  |
| 6 | IND_DEDUZ_CRED_PRES | VARCHAR2(1) | Y |  |  |
| 7 | IND_DEDUZ_CRED_PRES_CBS | VARCHAR2(1) | Y |  |  |
| 8 | IND_DEDUZ_CRED_PRES_IBS | VARCHAR2(1) | N |  |  |
| 9 | ALIQUOTA_CBS | VARCHAR2(50) | Y |  |  |
| 10 | ALIQUOTA_IBS | VARCHAR2(50) | Y |  |  |
| 11 | P_ALIQ_CRED_PRES_CBS | VARCHAR2(200) | Y |  |  |
| 12 | CCLASS_NOTA_REFER | VARCHAR2(50) | N |  |  |
| 13 | DT_INICIAL | DATE | N |  |  |
| 14 | DT_FIM | DATE | Y |  |  |

**Indexes**:
- IU_CCRED_PRES (UNIQUE): (CCRED_PRES, DT_INICIAL, DT_FIM)

---

## CDT_CAT_PROCED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROCED | VARCHAR2(8) | N |  |  |
| 2 | DSC_PROCED | VARCHAR2(250) | Y |  |  |
| 3 | NUM_VERSAO | NUMBER(5) | Y |  |  |
| 4 | IND_TEM_ESTAB | CHAR(1) | Y |  |  |
| 5 | IND_TEM_DATA | CHAR(1) | Y |  |  |

**PK**: COD_PROCED

---

## CDT_CONTROLE_MIDIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | COD_GRUPO | VARCHAR2(2) | N |  |  |
| 3 | SEQ_MIDIA | NUMBER(3) | N |  |  |
| 4 | DSC_GRUPO | VARCHAR2(30) | Y |  |  |
| 5 | DAT_INICIO | DATE | Y |  |  |
| 6 | DAT_FIM | DATE | Y |  |  |
| 7 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 8 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 9 | QTD_MIDIA | NUMBER(3) | Y |  |  |

**PK**: NUM_JOB, COD_GRUPO, SEQ_MIDIA

---

## CDT_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ | NUMBER | N |  |  |
| 2 | TP_REG | VARCHAR2(4) | Y |  |  |
| 3 | DADOS_DOCFIS | VARCHAR2(2000) | Y |  |  |
| 4 | DADOS_DOCFIS_COMPL | VARCHAR2(1000) | Y |  |  |

**PK**: SEQ

---

## CDT_JOB_BCK_01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | STATUS_JOB | CHAR(1) | Y |  |  |
| 3 | DAT_PROG | DATE | Y |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 6 | DAT_EXEC_INI | DATE | Y |  |  |
| 7 | DAT_EXEC_FIM | DATE | Y |  |  |
| 8 | DAT_REF_INI | DATE | Y |  |  |
| 9 | DAT_REF_FIM | DATE | Y |  |  |
| 10 | DSC_JOB | VARCHAR2(255) | Y |  |  |
| 11 | NOM_RESP_PROG | VARCHAR2(40) | Y |  |  |
| 12 | NOM_RESP_EXEC | VARCHAR2(40) | Y |  |  |
| 13 | NOM_DIR_WORK | VARCHAR2(60) | Y |  |  |
| 14 | NUM_TAM_ARQ | NUMBER(6) | Y |  |  |

**PK**: NUM_JOB

---

## CDT_JOB_BCK_02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | NUM_DET_JOB | NUMBER(3) | N |  |  |
| 3 | STATUS_DET_JOB | CHAR(1) | Y |  |  |
| 4 | COD_PROCED | VARCHAR2(8) | Y |  |  |
| 5 | DAT_EXEC_INI | DATE | Y |  |  |
| 6 | DAT_EXEC_FIM | DATE | Y |  |  |
| 7 | QTD_REGS_PROC | NUMBER(9) | Y |  |  |
| 8 | DSC_OBSERVACAO | VARCHAR2(50) | Y |  |  |

**PK**: NUM_JOB, NUM_DET_JOB

---

## CENTRAL_ESCRITURA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMP_CENTRAL | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTRAL | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO_CEN | VARCHAR2(3) | N |  |  |
| 4 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 5 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 6 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 7 | DAT_VIGENCIA | DATE | N |  |  |

**PK**: COD_EMP_CENTRAL, COD_ESTAB_CENTRAL, COD_TIPO_LIVRO_CEN, COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_VIGENCIA

**FKs**:
- COD_EMP_CENTRAL, COD_ESTAB_CENTRAL, COD_TIPO_LIVRO_CEN → OBRIGACAO_FISCAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO)
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO → OBRIGACAO_FISCAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO)

---

## CENTRAL_ESCRIT_CONTABIL
**Comment**: Tabela de Paramentrização da Central de Escrituração Contábil

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_CENTRAL | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB_CENTRAL → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_CENTRAL_ESCRIT_CONT: (COD_EMPRESA, COD_ESTAB_CENTRAL, COD_ESTAB)

---

## CENTRO_CUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | CCUS_COD | VARCHAR2(28) | N |  |  |
| 4 | CCUS_DAT_ATUA | DATE | N |  |  |
| 5 | CCUS_TIP | CHAR(1) | N |  |  |
| 6 | CCUS_DSC | VARCHAR2(150) | Y |  |  |
| 7 | IND_EST | CHAR(1) | Y |  |  |
| 8 | IND_INV | CHAR(1) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, CCUS_COD, CCUS_DAT_ATUA, CCUS_TIP

---

## CFAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CFAB_ID | NUMBER(20) | N |  |  |
| 2 | FC2X_ID | NUMBER(20) | N |  |  |
| 3 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 4 | FILI_COD | VARCHAR2(9) | N |  |  |
| 5 | EXEC_ID | NUMBER(20) | N |  |  |
| 6 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 7 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 8 | LSTQ_IND_LANCTO | CHAR(1) | Y |  |  |
| 9 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 10 | TOPE_COD | VARCHAR2(6) | Y |  |  |
| 11 | COD_CFOP | NUMBER(4) | Y |  |  |
| 12 | COD_FICHA | VARCHAR2(2) | N |  |  |
| 13 | COD_ITEM | VARCHAR2(60) | Y |  |  |
| 14 | COD_LANCTO | VARCHAR2(6) | Y |  |  |
| 15 | COD_NSTQ | VARCHAR2(5) | Y |  |  |
| 16 | COD_PROC | VARCHAR2(40) | Y |  |  |
| 17 | COD_REMDEST | VARCHAR2(18) | Y |  |  |
| 18 | COD_SERIE | VARCHAR2(5) | Y |  |  |
| 19 | DAT_MOVTO | DATE | Y |  |  |
| 20 | DSC_HIST | VARCHAR2(255) | Y |  |  |
| 21 | IND_RATEIO | CHAR(1) | Y |  |  |
| 22 | NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 23 | NUM_LANCTO | NUMBER(20) | Y |  |  |
| 24 | NUM_LLC | NUMBER(3) | Y |  |  |
| 25 | NUM_ORDEM | NUMBER(20) | Y |  |  |
| 26 | NUM_ORD_FAB | VARCHAR2(40) | Y |  |  |
| 27 | OBS | VARCHAR2(255) | Y |  |  |
| 28 | QTD_ENT | NUMBER | Y |  |  |
| 29 | QTD_INS_UNI | NUMBER | Y |  |  |
| 30 | QTD_SAI | NUMBER | Y |  |  |
| 31 | TIP_DOCTO | NUMBER(3) | Y |  |  |
| 32 | VAL_BASE | NUMBER | Y |  |  |
| 33 | VAL_CUS_ENT | NUMBER | Y |  |  |
| 34 | VAL_CUS_SAI | NUMBER | Y |  |  |
| 35 | VAL_CUS_SLD | NUMBER | Y |  |  |
| 36 | VAL_CUS_UNI | NUMBER | Y |  |  |
| 37 | VAL_ICM_ENT | NUMBER | Y |  |  |
| 38 | VAL_ICM_SAI | NUMBER | Y |  |  |
| 39 | VAL_ICM_SLD | NUMBER | Y |  |  |
| 40 | VAL_ICM_UNI | NUMBER | Y |  |  |
| 41 | NUM_ITEM | VARCHAR2(5) | Y |  |  |

**PK**: CFAB_ID

---

## CFO_NAT_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_PARAM | NUMBER(3) | Y |  |  |
| 4 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 5 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 6 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | Y |  |  |

**Indexes**:
- IDX_CFO_NAT_LOOKUP: (COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP, COD_EMPRESA, COD_ESTAB)

---

## CICD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CICD_DAT | DATE | N |  |  |
| 2 | CICD_COD_INF | VARCHAR2(9) | N |  |  |
| 3 | CICD_DSC | VARCHAR2(250) | Y |  |  |

**PK**: CICD_DAT, CICD_COD_INF

---

## CIEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | INFEM_DTEMIS | DATE | N |  |  |
| 4 | INFEM_SERIE | VARCHAR2(5) | N |  |  |
| 5 | INFEM_NUM | VARCHAR2(15) | N |  |  |
| 6 | INFEM_NUM_ITEM | VARCHAR2(5) | N |  |  |
| 7 | CADG_COD | VARCHAR2(16) | N |  |  |
| 8 | CATG_COD | CHAR(2) | N |  |  |
| 9 | CIEM_BAS_PISCOF | NUMBER | Y |  |  |
| 10 | CIEM_ALIQ_PIS | NUMBER | Y |  |  |
| 11 | CIEM_CRED_PIS | NUMBER | Y |  |  |
| 12 | CIEM_ALIQ_COF | NUMBER | Y |  |  |
| 13 | CIEM_CRED_COF | NUMBER | Y |  |  |
| 14 | CCTR_COD | VARCHAR2(20) | Y |  |  |
| 15 | TPIS_COD | CHAR(2) | Y |  |  |
| 16 | TCOF_COD | CHAR(2) | Y |  |  |
| 17 | CIEM_QTD_BC | NUMBER | Y |  |  |
| 18 | INFEM_DTENTR | DATE | Y |  |  |
| 19 | VAR01 | VARCHAR2(150) | Y |  |  |
| 20 | VAR02 | VARCHAR2(150) | Y |  |  |
| 21 | VAR03 | VARCHAR2(150) | Y |  |  |
| 22 | VAR04 | VARCHAR2(150) | Y |  |  |
| 23 | VAR05 | VARCHAR2(150) | Y |  |  |
| 24 | NUM01 | NUMBER | Y |  |  |
| 25 | NUM02 | NUMBER | Y |  |  |
| 26 | NUM03 | NUMBER | Y |  |  |

**PK**: EMPS_COD, FILI_COD, INFEM_DTEMIS, INFEM_SERIE, INFEM_NUM, INFEM_NUM_ITEM, CADG_COD, CATG_COD

---

## CISM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | INFSM_DTEMISS | DATE | N |  |  |
| 4 | INFSM_SERIE | VARCHAR2(5) | N |  |  |
| 5 | INFSM_NUM | VARCHAR2(15) | N |  |  |
| 6 | INFSM_NUM_ITEM | VARCHAR2(5) | N |  |  |
| 7 | CISM_BAS_PISCOF | NUMBER | Y |  |  |
| 8 | CISM_ALIQ_PIS | NUMBER | Y |  |  |
| 9 | CISM_DEB_PIS | NUMBER | Y |  |  |
| 10 | CISM_ALIQ_COF | NUMBER | Y |  |  |
| 11 | CISM_DEB_COF | NUMBER | Y |  |  |
| 12 | CCTR_COD | VARCHAR2(20) | Y |  |  |
| 13 | TPIS_COD | CHAR(2) | Y |  |  |
| 14 | TCOF_COD | CHAR(2) | Y |  |  |
| 15 | CISM_QTD_BC | NUMBER | Y |  |  |
| 16 | VAR01 | VARCHAR2(150) | Y |  |  |
| 17 | VAR02 | VARCHAR2(150) | Y |  |  |
| 18 | VAR03 | VARCHAR2(150) | Y |  |  |
| 19 | VAR04 | VARCHAR2(150) | Y |  |  |
| 20 | VAR05 | VARCHAR2(150) | Y |  |  |
| 21 | NUM01 | NUMBER | Y |  |  |
| 22 | NUM02 | NUMBER | Y |  |  |
| 23 | NUM03 | NUMBER | Y |  |  |
| 24 | CISM_RET_MERC | CHAR(1) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, INFSM_DTEMISS, INFSM_SERIE, INFSM_NUM, INFSM_NUM_ITEM

---

## CLASSE_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASSE_ESTAB | NUMBER(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_CLASSE_ESTAB

---

## CLASSIF_NBM_NALADI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NBM | NUMBER(12) | N |  |  |
| 2 | IDENT_NALADI | NUMBER(12) | N |  |  |
| 3 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 4 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_NBM, IDENT_NALADI

**FKs**:
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_NALADI → X2083_COD_NALADI(IDENT_NALADI)

---

## CLASSIF_NBM_NCM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NBM | NUMBER(12) | N |  |  |
| 2 | IDENT_NCM | NUMBER(12) | N |  |  |
| 3 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 4 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_NBM, IDENT_NCM

**FKs**:
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_NCM → X2045_COD_NCM(IDENT_NCM)

---

## CLAS_FISCAL_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CNBM_COD | VARCHAR2(10) | N |  |  |
| 2 | CNBM_DAT_ATUA | DATE | N |  |  |
| 3 | CNBM_DSC | VARCHAR2(500) | Y |  |  |
| 4 | CNBM_ALIQ_IPI | NUMBER | Y |  |  |
| 5 | CNBM_APURA_IPI | CHAR(1) | Y |  |  |
| 6 | CNBM_PRAZ_RECOLH | CHAR(1) | Y |  |  |
| 7 | CNBM_IND_TRIB | CHAR(1) | Y |  |  |
| 8 | GTIP_GRUPO | CHAR(4) | Y |  |  |
| 9 | STIP_GRUPO | VARCHAR2(6) | Y |  |  |

**PK**: CNBM_COD, CNBM_DAT_ATUA

**Indexes**:
- CLAS_FISCAL_PRODUTOI2: (CNBM_COD)

---

## CLI_FORNEC_TRANSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CADG_COD | VARCHAR2(16) | N |  |  |
| 2 | CADG_DAT_ATUA | DATE | N |  |  |
| 3 | CATG_COD | CHAR(2) | N |  |  |
| 4 | PAIS_COD | CHAR(3) | Y |  |  |
| 5 | UNFE_SIG | CHAR(2) | Y |  |  |
| 6 | CADG_COD_CGCCPF | VARCHAR2(16) | Y |  |  |
| 7 | CADG_TIP | CHAR(1) | Y |  |  |
| 8 | CADG_COD_INSEST | VARCHAR2(14) | Y |  |  |
| 9 | CADG_COD_INSMUN | VARCHAR2(14) | Y |  |  |
| 10 | EQUIPAR_RURAL | CHAR(1) | Y |  |  |
| 11 | CADG_NOM | VARCHAR2(70) | Y |  |  |
| 12 | CADG_NOM_FANTASIA | VARCHAR2(70) | Y |  |  |
| 13 | CADG_END | VARCHAR2(70) | Y |  |  |
| 14 | CADG_END_NUM | NUMBER(12) | Y |  |  |
| 15 | CADG_END_COMP | VARCHAR2(45) | Y |  |  |
| 16 | CADG_END_BAIRRO | VARCHAR2(60) | Y |  |  |
| 17 | CADG_END_MUNIC | VARCHAR2(50) | Y |  |  |
| 18 | CADG_END_CEP | CHAR(8) | Y |  |  |
| 19 | CADG_IND_COLIGADA | CHAR(1) | Y |  |  |
| 20 | CADG_COD_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 21 | TP_LOC | CHAR(2) | Y |  |  |
| 22 | LOCA_COD | VARCHAR2(10) | Y |  |  |
| 23 | CADG_CEI | VARCHAR2(12) | Y |  |  |
| 24 | NUM01 | NUMBER | Y |  |  |
| 25 | NUM02 | NUMBER | Y |  |  |
| 26 | NUM03 | NUMBER | Y |  |  |
| 27 | VAR01 | VARCHAR2(150) | Y |  |  |
| 28 | VAR02 | VARCHAR2(150) | Y |  |  |
| 29 | VAR03 | VARCHAR2(150) | Y |  |  |
| 30 | VAR04 | VARCHAR2(150) | Y |  |  |
| 31 | VAR05 | VARCHAR2(150) | Y |  |  |
| 32 | CADG_NIT | VARCHAR2(11) | Y |  |  |
| 33 | CADG_CX_POST | VARCHAR2(12) | Y |  |  |
| 34 | CADG_CEP_CXP | CHAR(8) | Y |  |  |
| 35 | CADG_DDD_TEL | CHAR(4) | Y |  |  |
| 36 | CADG_TEL | VARCHAR2(8) | Y |  |  |
| 37 | CADG_DDD_FAX | CHAR(4) | Y |  |  |
| 38 | CADG_FAX | VARCHAR2(8) | Y |  |  |
| 39 | CADG_CLAS_RI | CHAR(2) | Y |  |  |
| 40 | MIBGE_COD_MUN | VARCHAR2(7) | Y |  |  |

**PK**: CADG_COD, CATG_COD, CADG_DAT_ATUA

**Indexes**:
- CLI_FORNEC_TRANSPP2: (CADG_COD_CGCCPF)

---

## COD_CONV_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_TIPO_CODIGO | CHAR(1) | Y |  |  |
| 4 | ANO | NUMBER(4) | Y |  |  |
| 5 | MES | NUMBER(2) | Y |  |  |
| 6 | IDENT_CODIGO | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_COD_CONV_ICMS (UNIQUE): (COD_EMPRESA, COD_ESTAB, IND_TIPO_CODIGO, ANO, MES, IDENT_CODIGO)

---

## COD_FIS_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CFOP_COD | VARCHAR2(6) | N |  |  |
| 2 | CFOP_UF | CHAR(2) | N |  |  |
| 3 | CFOP_DAT_ATUA | DATE | N |  |  |
| 4 | CFOP_DSC | VARCHAR2(150) | Y |  |  |
| 5 | CFOP_IND_CONTR | CHAR(1) | Y |  |  |
| 6 | NUM01 | NUMBER | Y |  |  |
| 7 | NUM02 | NUMBER | Y |  |  |
| 8 | NUM03 | NUMBER | Y |  |  |
| 9 | VAR01 | VARCHAR2(150) | Y |  |  |
| 10 | VAR02 | VARCHAR2(150) | Y |  |  |
| 11 | VAR03 | VARCHAR2(150) | Y |  |  |
| 12 | VAR04 | VARCHAR2(150) | Y |  |  |
| 13 | VAR05 | VARCHAR2(150) | Y |  |  |

**PK**: CFOP_COD, CFOP_UF, CFOP_DAT_ATUA

**Indexes**:
- COD_FIS_OPERI2: (CFOP_COD)

---

## COD_IND_OPERACAO_CONSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_IND_OP | VARCHAR2(10) | N |  |  |
| 2 | ART_11 | VARCHAR2(20) | N |  |  |
| 3 | TIPO_OPERACAO | VARCHAR2(200) | N |  |  |
| 4 | CONSIDERA_LOCAL_OP | VARCHAR2(200) | N |  |  |
| 5 | CARACTERISTICA_FORN | VARCHAR2(200) | N |  |  |
| 6 | LOCAL_FORN_DFE | VARCHAR2(200) | N |  |  |
| 7 | DETALHES | VARCHAR2(800) | Y |  |  |

**PK**: COD_IND_OP

---

## COD_OBS_LIVRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_OBS_LIVRO | NUMBER(12) | N |  |  |
| 2 | GRUPO_OBS_LIVRO | VARCHAR2(9) | Y |  |  |
| 3 | COD_OBS_LIVRO | VARCHAR2(10) | Y |  |  |
| 4 | VALID_OBS_LIVRO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(45) | Y |  |  |
| 6 | DESCRICAO_1 | VARCHAR2(45) | Y |  |  |
| 7 | DESCRICAO_2 | VARCHAR2(45) | Y |  |  |

**PK**: IDENT_OBS_LIVRO

**FKs**:
- GRUPO_OBS_LIVRO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_OBS_LIVRO (UNIQUE): (GRUPO_OBS_LIVRO, COD_OBS_LIVRO, VALID_OBS_LIVRO)

---

## COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COMPL_TIPO | CHAR(2) | N |  |  |
| 2 | COMPL_COD | VARCHAR2(6) | N |  |  |
| 3 | COMPL_DAT_ATUA | DATE | N |  |  |
| 4 | COMPL_UF | CHAR(2) | Y |  |  |
| 5 | COMPL_DESC | VARCHAR2(150) | Y |  |  |
| 6 | COMPL_DAT_FIN | DATE | Y |  |  |
| 7 | COMPL_ALIQ | NUMBER | Y |  |  |

**PK**: COMPL_TIPO, COMPL_COD, COMPL_DAT_ATUA

---

## CONNECTION_CONFIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | TENANT_CODE | VARCHAR2(10) | N |  |  |
| 3 | USERNAME | VARCHAR2(30) | N |  |  |
| 4 | PASSWORD | VARCHAR2(255) | N |  |  |
| 5 | HOST | VARCHAR2(255) | Y |  |  |
| 6 | PORT | NUMBER(10) | Y |  |  |
| 7 | SERVICE | VARCHAR2(100) | Y |  |  |
| 8 | URL | VARCHAR2(500) | N |  |  |
| 9 | CREATED_AT | TIMESTAMP(6) WITH TIME ZONE | N | CURRENT_TIMESTAMP |  |
| 10 | CREATED_BY | VARCHAR2(128) | N |  |  |
| 11 | UPDATED_AT | TIMESTAMP(6) WITH TIME ZONE | Y |  |  |
| 12 | UPDATED_BY | VARCHAR2(128) | Y |  |  |
| 13 | MIN_POOL_SIZE | NUMBER(4) | N | 10 |  |
| 14 | MAX_POOL_SIZE | NUMBER(4) | N | 20 |  |
| 15 | MAX_WAIT_TIME | NUMBER(4) | N | 60 |  |
| 16 | IDLE_TIMEOUT | NUMBER(4) | N | 0 |  |
| 17 | URL_DR | VARCHAR2(500) | Y |  |  |
| 18 | CMCID | VARCHAR2(50) | Y |  |  |
| 19 | DBSCHEMA | VARCHAR2(50) | Y |  |  |
| 20 | DRIVER | VARCHAR2(255) | Y |  |  |
| 21 | POOL_MAX_ACTIVE | NUMBER(5) | Y |  |  |
| 22 | POOL_MAX_IDLE | NUMBER(5) | Y |  |  |
| 23 | POOL_MIN_IDLE | NUMBER(5) | Y |  |  |
| 24 | POOL_INITIAL_SIZE | NUMBER(5) | Y |  |  |
| 25 | POOL_MAX_WAIT | NUMBER(10) | Y |  |  |
| 26 | HOST_ONESOURCE | VARCHAR2(255) | Y |  |  |
| 27 | PORT_ONESOURCE | NUMBER(10) | Y |  |  |
| 28 | USERNAME_ONESOURCE | VARCHAR2(255) | Y |  |  |
| 29 | PASSWORD_ONESOURCE | VARCHAR2(255) | Y |  |  |
| 30 | DATADOG_APPLICATION_KEY | VARCHAR2(128) | Y |  |  |
| 31 | DATADOG_API_KEY | VARCHAR2(128) | Y |  |  |
| 32 | TOKEN_ONESOURCE | VARCHAR2(512) | Y |  |  |
| 33 | INTG_INTERDADOS | VARCHAR2(1) | Y |  |  |
| 34 | PROCESS_PRIORITY | NUMBER(4) | N | 999 |  |

**PK**: ID

**Indexes**:
- CONNECTION_CONFIG_UQ01 (UNIQUE): (TENANT_CODE, CMCID)

---

## CONSOLID_OBRIGACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_TIPO_CONSOL | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_TIPO_CONSOL

**FKs**:
- COD_TIPO_CONSOL → TIPO_CONSOLIDACAO(COD_TIPO_CONSOL)
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO → OBRIGACAO_FISCAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO)

---

## CONSOLID_OBRIG_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | COD_TIPO_CONSOL | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, COD_TIPO_CONSOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## CONSOLID_TP_LIVRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 2 | COD_TIPO_CONSOL | VARCHAR2(2) | N |  |  |

**PK**: COD_TIPO_LIVRO, COD_TIPO_CONSOL

**FKs**:
- COD_TIPO_LIVRO → TIPO_LIVRO_APURAC(COD_TIPO_LIVRO)
- COD_TIPO_CONSOL → TIPO_CONSOLIDACAO(COD_TIPO_CONSOL)

---

## CONV_DIFERIMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONVENIO | NUMBER(3) | N |  |  |
| 4 | DESC_1 | VARCHAR2(60) | Y |  |  |
| 5 | DESC_2 | VARCHAR2(60) | Y |  |  |
| 6 | DAT_VIGENCIA | DATE | Y |  |  |
| 7 | DAT_VALIDADE | DATE | Y |  |  |
| 8 | IND_CORRECAO | VARCHAR2(10) | Y |  |  |
| 9 | PRAZO_DIFERIDO | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONVENIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IND_CORRECAO → Y2046_INDICE(COD_INDICE)

---

## CPP_PARAM_COP
**Comment**: Tabela contendo as informações das parametrizações para cópia

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODULO | VARCHAR2(8) | N |  | identificador proveniente da tabela PRT_MODULOS_MSAF |
| 2 | ARQUIVO | VARCHAR2(8) | N |  | nome do arquivo que será utilizado para exportação/importação |
| 3 | DESC_ITEM_MENU | VARCHAR2(500) | Y |  | descrição do item de menu referente a parametrização |
| 4 | TP_DADOS | CHAR(1) | Y |  | tipo dos dados a serem considerados de acordo com o tipo de parametrização(1 - p/ empresa; 2 - p/ estab orig/dest; 3 - p/ todos os estabs) |
| 5 | GRUPO | VARCHAR2(4) | Y |  | corresponde aos quatro últimos dígitos do nome do arquivo principal. Separa os parâmetros em grupos. |
| 6 | ORD_GRUPO | NUMBER(3) | Y |  | ordenação do parâmetro dentro do grupo. Para os casos de hierarquia pai/filhos, caso o item seja o pai, este não possuirá informado a ordem. A ordem informada para o pai será 0. |
| 7 | NIVEL | NUMBER(3) | Y |  | hierarquia entre pai/filho dentro do grupo |
| 8 | ITEM_MENU | NUMBER | N | 1 | Um mesmo arquivo poderá ser gerado a partir de um ou mais itens de menu.(P.ex.: SAFP0139 - DWT_FERIADOS) |

**PK**: COD_MODULO, ARQUIVO, ITEM_MENU

**FKs**:
- COD_MODULO → PRT_MODULOS_MSAF(COD_MODULO)

---

## CPROC_FILE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | VARCHAR2(80) | N |  |  |
| 2 | NOME_ARQUIVO | VARCHAR2(60) | N |  |  |
| 3 | DATA_REQUEST | DATE | N |  |  |
| 4 | CONTEUDO | CLOB | Y |  |  |

**PK**: ID

---

## CREDPIS_CONTROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_BEM | VARCHAR2(60) | N |  |  |
| 4 | COD_INC | VARCHAR2(6) | N |  |  |
| 5 | IND_PARCELA | NUMBER(3) | N |  |  |
| 6 | DATA_INI_CRED | DATE | N |  |  |
| 7 | DATA_FIM_CRED | DATE | N |  |  |
| 8 | IND_BAIXA | CHAR(1) | N |  |  |
| 9 | DAT_BAIXA | DATE | Y |  |  |
| 10 | MOTIVO_BAIXA | CHAR(1) | Y |  |  |
| 11 | IND_BX_SAFX538 | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC

---

## CREDPIS_NBM_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_NBM | VARCHAR2(10) | N |  |  |
| 4 | IND_SERV_MERC | VARCHAR2(1) | N |  |  |
| 5 | DATA_VALID | DATE | N |  |  |
| 6 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 7 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |
| 9 | DAT_OPERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_NBM, IND_SERV_MERC, DATA_VALID

---

## CTEX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | INFSM_SERIE | VARCHAR2(5) | N |  |  |
| 4 | INFSM_NUM | VARCHAR2(15) | N |  |  |
| 5 | INFSM_DTEMISS | DATE | N |  |  |
| 6 | TAEX_COD_RE | VARCHAR2(15) | N |  |  |
| 7 | MATE_COD | VARCHAR2(60) | N |  |  |
| 8 | CTEX_NF_REM | VARCHAR2(15) | N |  |  |
| 9 | CTEX_SERIE_REM | VARCHAR2(5) | N |  |  |
| 10 | CTEX_DTEMISS_REM | DATE | N |  |  |
| 11 | CATG_COD | CHAR(2) | N |  |  |
| 12 | CADG_COD | VARCHAR2(16) | N |  |  |
| 13 | MOD_COD | CHAR(3) | Y |  |  |
| 14 | CTEX_QTD_EXP | NUMBER | Y |  |  |
| 15 | CTEX_VAL_UNIT | NUMBER | Y |  |  |
| 16 | CTEX_TOT_EXP | NUMBER | Y |  |  |
| 17 | CTEX_NR_MEMO | VARCHAR2(20) | Y |  |  |
| 18 | CTEX_CHV_NFE | VARCHAR2(44) | Y |  |  |
| 19 | UNID_COD | CHAR(3) | Y |  |  |
| 20 | INFSM_NUM_ITEM | VARCHAR2(5) | N |  |  |

**PK**: EMPS_COD, FILI_COD, INFSM_SERIE, INFSM_NUM, INFSM_DTEMISS, TAEX_COD_RE, MATE_COD, CTEX_NF_REM, CTEX_SERIE_REM, CTEX_DTEMISS_REM, CATG_COD, CADG_COD, INFSM_NUM_ITEM

---

## CTRL_COMPENSACAO_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_EVENTO | DATE | N |  |  |
| 2 | NRO_REFERENCIA_CRED | VARCHAR2(15) | N |  |  |
| 3 | NRO_REFERENCIA_DEB | VARCHAR2(15) | N |  |  |
| 4 | IND_COMP_VINC | CHAR(1) | N |  |  |
| 5 | VLR_PRINC_DEVIDO | NUMBER(17,2) | Y |  |  |
| 6 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_PRINC_DEVIDO_COMP | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ORIG_COMP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_COR_MONET_COMP | NUMBER(17,2) | Y |  |  |
| 11 | VLR_PRINC_RECOLHER | NUMBER(17,2) | Y |  |  |
| 12 | OBSERVACAO | VARCHAR2(50) | Y |  |  |
| 13 | USUARIO | VARCHAR2(50) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: DATA_EVENTO, NRO_REFERENCIA_CRED, NRO_REFERENCIA_DEB

---

## CTRL_MENU

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CGC | VARCHAR2(14) | N |  |  |
| 2 | MODULO | VARCHAR2(15) | N |  |  |
| 3 | NOME_MENU | VARCHAR2(50) | N |  |  |

**PK**: CGC, MODULO, NOME_MENU

---

## CT_AJUSTE_OUTLANCTO_CONTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | UF | VARCHAR2(2) | N |  |  |
| 4 | GRUPO_IMPOSTO | VARCHAR2(10) | N |  |  |
| 5 | IMPOSTO | VARCHAR2(30) | N |  |  |
| 6 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 7 | PERIODO | NUMBER(2) | N |  |  |
| 8 | EXERCICIO | NUMBER(4) | N |  |  |
| 9 | CHAVE_ID | VARCHAR2(30) | N |  |  |
| 10 | COD_AJUSTE | VARCHAR2(8) | Y |  |  |
| 11 | DESCRICAO_AJUSTE | VARCHAR2(300) | Y |  |  |
| 12 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 13 | DSC_OPER_APUR | VARCHAR2(100) | Y |  |  |
| 14 | REFERENCIA | VARCHAR2(16) | Y |  |  |
| 15 | DT_DOCTO | DATE | Y |  |  |
| 16 | DT_LANCTO | DATE | Y |  |  |
| 17 | LOCAL_NEGOCIO | VARCHAR2(4) | Y |  |  |
| 18 | DIVISAO | VARCHAR2(4) | Y |  |  |
| 19 | CENTRO | VARCHAR2(4) | Y |  |  |
| 20 | COD_CONTA_D | VARCHAR2(70) | Y |  |  |
| 21 | DESCRICAO_CONTA_D | VARCHAR2(50) | Y |  |  |
| 22 | IND_NATUREZA_D | VARCHAR2(1) | Y |  |  |
| 23 | IND_SITUACAO_D | VARCHAR2(1) | Y |  |  |
| 24 | CHAVE_LANCTO_D | VARCHAR2(9) | Y |  |  |
| 25 | CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 26 | DESCRICAO_CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 27 | CENTRO_LUCRO_D | NUMBER(25) | Y |  |  |
| 28 | TEXTO_D | VARCHAR2(20) | Y |  |  |
| 29 | OBSERVACAO_D | VARCHAR2(20) | Y |  |  |
| 30 | VALOR_D | NUMBER(17,2) | Y |  |  |
| 31 | COD_CONTA_C | VARCHAR2(70) | Y |  |  |
| 32 | DESCRICAO_CONTA_C | VARCHAR2(50) | Y |  |  |
| 33 | IND_NATUREZA_C | VARCHAR2(1) | Y |  |  |
| 34 | IND_SITUACAO_C | VARCHAR2(1) | Y |  |  |
| 35 | CHAVE_LANCTO_C | VARCHAR2(9) | Y |  |  |
| 36 | CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 37 | DESCRICAO_CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 38 | CENTRO_LUCRO_C | NUMBER(25) | Y |  |  |
| 39 | TEXTO_C | VARCHAR2(20) | Y |  |  |
| 40 | OBSERVACAO_C | VARCHAR2(20) | Y |  |  |
| 41 | VALOR_C | NUMBER(17,2) | Y |  |  |
| 42 | CNPJ_ESTAB | VARCHAR2(14) | Y |  |  |
| 43 | STATUS | VARCHAR2(30) | Y |  |  |
| 44 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 45 | USUARIO | VARCHAR2(100) | Y |  |  |
| 46 | DATA_PARAMETRO | DATE | Y |  |  |
| 47 | DATA_GRAVACAO | VARCHAR2(20) | Y |  |  |
| 48 | NRO_DOC_CONTABIL | NUMBER(10) | Y |  |  |
| 49 | TIPO_LANCTO_CONTABIL | VARCHAR2(50) | Y |  |  |

**PK**: CHAVE_ID

**Indexes**:
- UK_CT_AJUSTE_OUTLANCTO_CONTAB (UNIQUE): (COD_EMPRESA, COD_ESTAB, UF, GRUPO_IMPOSTO, IMPOSTO, COD_TIPO_LIVRO, PERIODO, EXERCICIO, COD_AJUSTE, COD_OPER_APUR, STATUS, NRO_DOC_CONTABIL)

---

## CT_ESTORNO_CONTABIL_AUTOMAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CHAVE_ID | VARCHAR2(50) | N |  |  |
| 4 | PERIODO | VARCHAR2(2) | N |  |  |
| 5 | EXERCICIO | VARCHAR2(4) | N |  |  |
| 6 | DT_DOCTO | DATE | Y |  |  |
| 7 | DT_LANCTO | DATE | Y |  |  |
| 8 | UF | VARCHAR2(2) | Y |  |  |
| 9 | REFERENCIA | VARCHAR2(16) | Y |  |  |
| 10 | LOCAL_NEGOCIO | VARCHAR2(4) | Y |  |  |
| 11 | DIVISAO | VARCHAR2(4) | Y |  |  |
| 12 | CENTRO | VARCHAR2(4) | Y |  |  |
| 13 | GRUPO_IMPOSTO | VARCHAR2(10) | N |  |  |
| 14 | IMPOSTO | VARCHAR2(20) | N |  |  |
| 15 | COD_AJUSTE | VARCHAR2(15) | N |  |  |
| 16 | DESCRICAO_AJUSTE | VARCHAR2(50) | N |  |  |
| 17 | CHAVE_LANCTO_D | VARCHAR2(2) | N |  |  |
| 18 | COD_CONTA_D | VARCHAR2(70) | N |  |  |
| 19 | DESCRICAO_CONTA_D | VARCHAR2(50) | N |  |  |
| 20 | MONTANTE_D | NUMBER(17,2) | N |  |  |
| 21 | CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 22 | DESCRICAO_CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 23 | CENTRO_LUCRO_D | VARCHAR2(20) | Y |  |  |
| 24 | TEXTO_D | VARCHAR2(20) | Y |  |  |
| 25 | OBSERVACAO_D | VARCHAR2(20) | Y |  |  |
| 26 | CHAVE_LANCTO_C | VARCHAR2(2) | N |  |  |
| 27 | COD_CONTA_C | VARCHAR2(70) | N |  |  |
| 28 | DESCRICAO_CONTA_C | VARCHAR2(50) | N |  |  |
| 29 | MONTANTE_C | NUMBER(17,2) | N |  |  |
| 30 | CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 31 | DESCRICAO_CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 32 | CENTRO_LUCRO_C | VARCHAR2(20) | Y |  |  |
| 33 | TEXTO_C | VARCHAR2(20) | Y |  |  |
| 34 | OBSERVACAO_C | VARCHAR2(20) | Y |  |  |
| 35 | USUARIO | VARCHAR2(100) | N |  |  |
| 36 | NRO_DOC_CONTABIL | NUMBER(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CHAVE_ID, PERIODO, EXERCICIO, GRUPO_IMPOSTO, IMPOSTO, COD_AJUSTE

---

## CT_PARAM_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | UF | VARCHAR2(2) | N |  |  |
| 4 | GRUPO_IMPOSTO | VARCHAR2(10) | N |  |  |
| 5 | IMPOSTO | VARCHAR2(30) | N |  |  |
| 6 | COD_AJUSTE | VARCHAR2(8) | N |  |  |
| 7 | DESCRICAO_AJUSTE | VARCHAR2(300) | Y |  |  |
| 8 | REFERENCIA | VARCHAR2(16) | Y |  |  |
| 9 | LOCAL_NEGOCIO | VARCHAR2(4) | Y |  |  |
| 10 | DIVISAO | VARCHAR2(4) | Y |  |  |
| 11 | CENTRO | VARCHAR2(4) | Y |  |  |
| 12 | COD_CONTA_D | VARCHAR2(70) | Y |  |  |
| 13 | DESCRICAO_CONTA_D | VARCHAR2(50) | Y |  |  |
| 14 | IND_NATUREZA_D | VARCHAR2(1) | Y |  |  |
| 15 | IND_SITUACAO_D | VARCHAR2(1) | Y |  |  |
| 16 | CHAVE_LANCTO_D | VARCHAR2(9) | Y |  |  |
| 17 | CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 18 | DESCRICAO_CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 19 | CENTRO_LUCRO_D | NUMBER(25) | Y |  |  |
| 20 | TEXTO_D | VARCHAR2(20) | Y |  |  |
| 21 | OBSERVACAO_D | VARCHAR2(20) | Y |  |  |
| 22 | COD_CONTA_C | VARCHAR2(70) | Y |  |  |
| 23 | DESCRICAO_CONTA_C | VARCHAR2(50) | Y |  |  |
| 24 | IND_NATUREZA_C | VARCHAR2(1) | Y |  |  |
| 25 | IND_SITUACAO_C | VARCHAR2(1) | Y |  |  |
| 26 | CHAVE_LANCTO_C | VARCHAR2(9) | Y |  |  |
| 27 | CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 28 | DESCRICAO_CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 29 | CENTRO_LUCRO_C | NUMBER(25) | Y |  |  |
| 30 | TEXTO_C | VARCHAR2(20) | Y |  |  |
| 31 | OBSERVACAO_C | VARCHAR2(20) | Y |  |  |
| 32 | USUARIO | VARCHAR2(100) | Y |  |  |
| 33 | DATA_PARAMETRO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_IMPOSTO, IMPOSTO, COD_AJUSTE

---

## CT_PARAM_OUT_LANCTOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | UF | VARCHAR2(2) | N |  |  |
| 4 | GRUPO_IMPOSTO | VARCHAR2(10) | N |  |  |
| 5 | IMPOSTO | VARCHAR2(30) | N |  |  |
| 6 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | DSC_OPER_APUR | VARCHAR2(100) | Y |  |  |
| 9 | REFERENCIA | VARCHAR2(16) | Y |  |  |
| 10 | LOCAL_NEGOCIO | VARCHAR2(4) | Y |  |  |
| 11 | DIVISAO | VARCHAR2(4) | Y |  |  |
| 12 | CENTRO | VARCHAR2(4) | Y |  |  |
| 13 | COD_CONTA_D | VARCHAR2(70) | Y |  |  |
| 14 | DESCRICAO_CONTA_D | VARCHAR2(50) | Y |  |  |
| 15 | IND_NATUREZA_D | VARCHAR2(1) | Y |  |  |
| 16 | IND_SITUACAO_D | VARCHAR2(1) | Y |  |  |
| 17 | CHAVE_LANCTO_D | VARCHAR2(2) | Y |  |  |
| 18 | CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 19 | DESCRICAO_CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 20 | CENTRO_LUCRO_D | NUMBER(25) | Y |  |  |
| 21 | TEXTO_D | VARCHAR2(20) | Y |  |  |
| 22 | OBSERVACAO_D | VARCHAR2(20) | Y |  |  |
| 23 | COD_CONTA_C | VARCHAR2(70) | Y |  |  |
| 24 | DESCRICAO_CONTA_C | VARCHAR2(50) | Y |  |  |
| 25 | IND_NATUREZA_C | VARCHAR2(1) | Y |  |  |
| 26 | IND_SITUACAO_C | VARCHAR2(1) | Y |  |  |
| 27 | CHAVE_LANCTO_C | VARCHAR2(2) | Y |  |  |
| 28 | CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 29 | DESCRICAO_CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 30 | CENTRO_LUCRO_C | NUMBER(25) | Y |  |  |
| 31 | TEXTO_C | VARCHAR2(20) | Y |  |  |
| 32 | OBSERVACAO_C | VARCHAR2(20) | Y |  |  |
| 33 | USUARIO | VARCHAR2(100) | Y |  |  |
| 34 | DATA_PARAMETRO | DATE | Y |  |  |
| 35 | OUTROS_LANCAMENTOS_CONTABEIS | VARCHAR2(50) | Y |  | Outros lançamentos contábeis |
| 36 | COD_NAT_REC | VARCHAR2(3) | Y |  | Código da natureza da receita |

**PK**: COD_EMPRESA, COD_ESTAB, UF, GRUPO_IMPOSTO, IMPOSTO, COD_TIPO_LIVRO, COD_OPER_APUR

---

## DADOS_DUMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | NOME_LOGICO_ARQ | VARCHAR2(8) | N |  |  |
| 3 | IND_ORDEM | CHAR(1) | N |  |  |
| 4 | NUM_REG | NUMBER(8) | N |  |  |
| 5 | REGISTRO | VARCHAR2(600) | Y |  |  |

**PK**: NUM_PROCESSO, NOME_LOGICO_ARQ, IND_ORDEM, NUM_REG

---

## DBCONNECTION

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER | N |  |  |
| 2 | USERNAME | VARCHAR2(45) | N |  |  |
| 3 | PASSWORD | VARCHAR2(45) | N |  |  |
| 4 | DRIVER | VARCHAR2(45) | N |  |  |
| 5 | URL | VARCHAR2(400) | Y |  |  |
| 6 | CLIENT | VARCHAR2(45) | Y |  |  |
| 7 | DBSCHEMA | VARCHAR2(45) | Y |  |  |

**PK**: ID

---

## DCA_DOCTO_FISCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | MES_BASE | NUMBER(2) | Y |  |  |
| 5 | ANO_BASE | NUMBER(4) | Y |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(30) | Y |  |  |
| 9 | COD_CFOP | VARCHAR2(4) | Y |  |  |
| 10 | DAT_EMISSAO | DATE | Y |  |  |
| 11 | DAT_EMBARQUE | DATE | Y |  |  |
| 12 | COMPROV_EXP | VARCHAR2(15) | Y |  |  |
| 13 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 14 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 15 | SIGLA_INCENTIVO | VARCHAR2(3) | Y |  |  |

**PK**: IDENT_DOCTO_FISCAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_DCA_DOCTO: (DAT_EMISSAO, COD_ESTAB, COD_EMPRESA)
- IX_DCA_DOCTO_MES: (MES_BASE, ANO_BASE, COD_ESTAB, COD_EMPRESA)

---

## DCA_ITENS_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | MES_BASE | NUMBER(2) | Y |  |  |
| 5 | ANO_BASE | NUMBER(4) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(30) | Y |  |  |
| 8 | COD_CFOP | VARCHAR2(4) | Y |  |  |
| 9 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 10 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 11 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 12 | IDENT_NBM | NUMBER(12) | Y |  |  |

**PK**: IDENT_DOCTO_FISCAL, IDENT_PRODUTO

**FKs**:
- IDENT_DOCTO_FISCAL → DCA_DOCTO_FISCAL(IDENT_DOCTO_FISCAL)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DCA_SERIE_NCONSID

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, SERIE_DOCFIS

---

## DDS_NATAL_DADOS_INICIAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 4 | IND_SERV_PREST | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_RESPONSAVEL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DDS_NATAL_DEDUCOES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 4 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 5 | NUM_PROJETO | VARCHAR2(7) | N |  |  |
| 6 | NOME_PROJETO | VARCHAR2(35) | Y |  |  |
| 7 | VLR_DEDUCAO | NUMBER(11,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_COMPETENCIA, ANO_COMPETENCIA, NUM_PROJETO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DDS_NATAL_DESPESAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 4 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 5 | MES_DESPESA | NUMBER(2) | N |  |  |
| 6 | VLR_AGUA | NUMBER(11,2) | Y |  |  |
| 7 | VLR_ENERGIA_ELETRICA | NUMBER(11,2) | Y |  |  |
| 8 | VLR_TELEFONE | NUMBER(11,2) | Y |  |  |
| 9 | VLR_ALUGUEL_IPTU | NUMBER(11,2) | Y |  |  |
| 10 | VLR_CIM | NUMBER(11,2) | Y |  |  |
| 11 | VLR_PIS | NUMBER(11,2) | Y |  |  |
| 12 | VLR_COFINS | NUMBER(11,2) | Y |  |  |
| 13 | VLR_ISS | NUMBER(11,2) | Y |  |  |
| 14 | VLR_SIMPLES | NUMBER(11,2) | Y |  |  |
| 15 | VLR_FOLHA_PAGTO | NUMBER(11,2) | Y |  |  |
| 16 | VLR_INSS | NUMBER(11,2) | Y |  |  |
| 17 | VLR_FGTS | NUMBER(11,2) | Y |  |  |
| 18 | VLR_VALE_TRANSP | NUMBER(11,2) | Y |  |  |
| 19 | VLR_PRO_LABORE | NUMBER(11,2) | Y |  |  |
| 20 | VLR_MAT_EXPEDIENTE | NUMBER(11,2) | Y |  |  |
| 21 | VLR_SERV_TERCEIRO | NUMBER(11,2) | Y |  |  |
| 22 | VLR_COMBUSTIVEL | NUMBER(11,2) | Y |  |  |
| 23 | VLR_DESPESA_FINANC | NUMBER(11,2) | Y |  |  |
| 24 | VLR_CONDOMINIO | NUMBER(11,2) | Y |  |  |
| 25 | VLR_SERV_CONTABIL | NUMBER(11,2) | Y |  |  |
| 26 | VLR_MAT_APLICADO | NUMBER(11,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_COMPETENCIA, ANO_COMPETENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DECLARACAO_DIPJ
**Comment**: Controle de declaracoes da DIPJ, OS 1344

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DECLARACAO | NUMBER(12) | N |  | IDENT_DECLARACAO |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  | COD_EMPRESA |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  | COD_ESTAB (Matriz) |
| 4 | VERSAO | VARCHAR2(4) | Y |  | Indica a versao da DIPJ para a declaracao importada (DIPJ2003, DIPJ2004 etc) |
| 5 | ANO_CALENDARIO | VARCHAR2(4) | Y |  | Ano da declaracao importada |
| 6 | IND_RETIFICADORA | CHAR(1) | Y |  | Indica se a declaracao e retificadora (0 = Nao, 1 = Sim) |
| 7 | SITUACAO | CHAR(1) | Y | '0' | 0 - Nao se Aplica,1 - Extincao, 2 - Fusao, 3 - Incorporacao/Incorporada, 4 - Incorporacao/Incorporadora, 5 - Cisao Total, 6 - Cisao Parcial. |
| 8 | DAT_EXTINCAO | DATE | Y |  | Data do Evento relacionado a coluna SITUACAO |

**PK**: IDENT_DECLARACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UX_DECLAR_DIPJ (UNIQUE): (COD_EMPRESA, COD_ESTAB, VERSAO, ANO_CALENDARIO, IND_RETIFICADORA)

---

## DES_DOCFIS_DEDUCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | CNPJ_CPF_ORIGEM | VARCHAR2(14) | N |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(5) | N |  |  |
| 8 | NUM_DOCFIS_DED | VARCHAR2(8) | N |  |  |
| 9 | CNPJ_CPF_DED | VARCHAR2(14) | N |  |  |
| 10 | IND_DEDUCAO | CHAR(1) | Y |  |  |
| 11 | RAZAO_SOCIAL_DEST | VARCHAR2(70) | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | COD_MUNICIPIO | NUMBER(7) | Y |  |  |
| 14 | VLR_DEDUCAO | NUMBER(15,2) | Y |  |  |
| 15 | DSC_MUNICIPIO | VARCHAR2(50) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |
| 18 | VLR_DOCFIS_DED | NUMBER(15,2) | Y |  |  |
| 19 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 20 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 21 | COD_ESTADO | VARCHAR2(2) | Y |  | Estado da Nota de Dedução |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, CNPJ_CPF_ORIGEM, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, NUM_DOCFIS_DED, CNPJ_CPF_DED

---

## DES_DOCFIS_ENTRADA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | CNPJ_CPF_ORIGEM | VARCHAR2(14) | N |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(8) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(5) | N |  |  |
| 8 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 9 | COD_SERVICO | VARCHAR2(5) | N |  |  |
| 10 | CNPJ_CPF_DESTINO | VARCHAR2(14) | N |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | VLR_DOCFIS | NUMBER(15,2) | Y |  |  |
| 13 | VLR_BASE_ISS | NUMBER(15,2) | Y |  |  |
| 14 | OBS_DOCFIS | VARCHAR2(200) | Y |  |  |
| 15 | DSC_MUNICIPIO | VARCHAR2(50) | Y |  |  |
| 16 | DSC_SERVICO | VARCHAR2(50) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | COD_ESTADO | VARCHAR2(2) | Y |  | Estado do Prestador |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, CNPJ_CPF_ORIGEM, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, COD_MUNICIPIO, COD_SERVICO, CNPJ_CPF_DESTINO

---

## DES_DOCFIS_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | CNPJ_CPF_ORIGEM | VARCHAR2(14) | N |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(8) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(5) | N |  |  |
| 8 | COD_MUNICIPIO | NUMBER(7) | N |  |  |
| 9 | COD_SERVICO | VARCHAR2(5) | N |  |  |
| 10 | CNPJ_CPF_DESTINO | VARCHAR2(14) | N |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | IND_SITUACAO | CHAR(1) | Y |  |  |
| 13 | VLR_DOCFIS | NUMBER(15,2) | Y |  |  |
| 14 | VLR_ISS | NUMBER(15,2) | Y |  |  |
| 15 | OBS_DOCFIS | VARCHAR2(200) | Y |  |  |
| 16 | NUM_DOCFIS_EXT | VARCHAR2(8) | Y |  |  |
| 17 | NUM_ALVARA | VARCHAR2(8) | Y |  |  |
| 18 | NUM_LIVRO57 | VARCHAR2(8) | Y |  |  |
| 19 | NUM_PAG_LIVRO57 | VARCHAR2(8) | Y |  |  |
| 20 | COMPL_ISENCAO | VARCHAR2(5) | Y |  |  |
| 21 | DSC_MUNICIPIO | VARCHAR2(50) | Y |  |  |
| 22 | DSC_SERVICO | VARCHAR2(50) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | COD_ESTADO | VARCHAR2(2) | Y |  | Estado da Nota Fiscal |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, CNPJ_CPF_ORIGEM, COD_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, COD_MUNICIPIO, COD_SERVICO, CNPJ_CPF_DESTINO

---

## DETALHE_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DET_OPERACAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_DET_OPER | VARCHAR2(9) | Y |  |  |
| 3 | COD_DET_OPERACAO | VARCHAR2(5) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 7 | TITULO_RELATORIO | VARCHAR2(50) | Y |  |  |
| 8 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 9 | IDENT_ESTADO_AMP | NUMBER(12) | Y |  |  |
| 10 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 11 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 12 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  | Código de ajuste da apuração do IPI de acordo com a Tabela de Códigos de Ajuste da Apuração do IPI (publicada pela RFB). Este campo é obrigatório para a geração do registro  "E530-Ajustes da Apuração do IPI"  do Sped Fiscal. |
| 13 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  | Código de Ajuste do ICMS/ICMS-ST Sped Fiscal. Referente ao Códigos de Ajustes da ICT_AJUSTE_ICMS(Tabela 5.1.1 do Sped Fiscal). |
| 14 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  | Codigo de Ajuste (Sped Fiscal - Reg C197) -                              referente aos Códigos de Ajustes de DWT_COD_AJUSTE_SPED |
| 15 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 16 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 17 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |

**PK**: IDENT_DET_OPERACAO

**FKs**:
- GRUPO_DET_OPER → GRUPO_ESTAB(GRUPO_ESTAB)
- COD_TIPO_LIVRO, COD_OPER_APUR → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_AJUSTE_ICMS → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

**Indexes**:
- IX_CHN_DET_OPER (UNIQUE): (GRUPO_DET_OPER, COD_DET_OPERACAO)

---

## DFME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MNFEM_SERIE | VARCHAR2(5) | N |  |  |
| 4 | MNFEM_NUM | VARCHAR2(15) | N |  |  |
| 5 | MNFEM_DTEMIS | DATE | N |  |  |
| 6 | CADG_COD | VARCHAR2(16) | N |  |  |
| 7 | CATG_COD | CHAR(2) | N |  |  |
| 8 | CICD_COD_INF | VARCHAR2(9) | N |  |  |
| 9 | DFME_CADG_COD | VARCHAR2(16) | N |  |  |
| 10 | DFME_CATG_COD | CHAR(2) | N |  |  |
| 11 | DFME_SERIE | VARCHAR2(5) | N |  |  |
| 12 | DFME_NUM_DOC | VARCHAR2(15) | N |  |  |
| 13 | DFME_DT_DOC | DATE | N |  |  |
| 14 | MNFEM_DTENTR | DATE | Y |  |  |
| 15 | DFME_IND_EMIT | CHAR(1) | Y |  |  |
| 16 | MDOC_COD | CHAR(3) | Y |  |  |
| 17 | DFME_DT_REF | DATE | Y |  |  |
| 18 | DFME_TP_OPE | CHAR(1) | Y |  |  |
| 19 | DFME_NUM_ITEM | VARCHAR2(5) | N |  |  |
| 20 | DFME_NUM_ITEM_REF | VARCHAR2(5) | N |  |  |

**PK**: EMPS_COD, FILI_COD, MNFEM_SERIE, MNFEM_NUM, MNFEM_DTEMIS, CADG_COD, CATG_COD, CICD_COD_INF, DFME_CADG_COD, DFME_CATG_COD, DFME_SERIE, DFME_NUM_DOC, DFME_DT_DOC, DFME_NUM_ITEM, DFME_NUM_ITEM_REF

---

## DFMS_PA_PAR_SERVICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SERVICO_DOCFIS | VARCHAR2(4) | N |  |  |
| 2 | SERVICO_DFMS | VARCHAR2(4) | Y |  |  |
| 3 | VALIDADE_SERVICO | DATE | N |  |  |

**PK**: SERVICO_DOCFIS, VALIDADE_SERVICO

---

## DGCA_APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PRD_REFERENCIA | DATE | N |  |  |
| 4 | TP_OPERACAO | NUMBER(3) | N |  |  |
| 5 | DSC_TP_OPERACAO | VARCHAR2(50) | Y |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ALIQ | NUMBER(17,2) | Y |  |  |
| 9 | VLR_IMPOSTO_DEB | NUMBER(17,2) | Y |  |  |
| 10 | IND_IVA | VARCHAR2(1) | Y |  |  |
| 11 | VLR_IVA | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PMC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CUSTO_ESTIMADO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_IMPOSTO_CRED | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CRED_ACUMUL | NUMBER(17,2) | Y |  |  |
| 16 | VLR_SALDO_GIA | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DIFERENCA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_CRED_APROP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PRD_REFERENCIA, TP_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DGCA_SALDO_CRED_ACUMUL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PRD_REFERENCIA | DATE | N |  |  |
| 4 | VLR_SALDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PRD_REFERENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DGCA_SALDO_CRED_GIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DGCA_SALDO_INI_CRED_ACUMUL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PRD_REFERENCIA | DATE | N |  |  |
| 4 | VLR_SALDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PRD_REFERENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DGCA_VALOR_CRED_OUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PRD_REFERENCIA | DATE | N |  |  |
| 4 | VLR_IMPOSTO_CRED | NUMBER(17,2) | Y |  |  |
| 5 | VLR_CRED_ACUMUL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PRD_REFERENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DIFERIMENTO_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | VAL_DIFERIDO | NUMBER(15,2) | Y |  |  |
| 6 | DAT_VENC | DATE | Y |  |  |
| 7 | OBSERVACAO | VARCHAR2(50) | Y |  |  |
| 8 | COD_CONVENIO | NUMBER(3) | Y |  |  |
| 9 | VAL_PAGO | NUMBER(15,2) | Y |  |  |
| 10 | VAL_PRINCIPAL | NUMBER(15,2) | Y |  |  |
| 11 | VAL_JUROS | NUMBER(15,2) | Y |  |  |
| 12 | VAL_MULTA | NUMBER(15,2) | Y |  |  |
| 13 | VAL_DESCONTO | NUMBER(15,2) | Y |  |  |
| 14 | VAL_CORRECAO | NUMBER(15,2) | Y |  |  |
| 15 | DAT_PAGTO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, DAT_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_CONVENIO → CONV_DIFERIMENTO(COD_EMPRESA, COD_ESTAB, COD_CONVENIO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TRIBUTO → TRIBUTO(COD_TRIBUTO)

---

## DIM_SL_PAR_SERVICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SERVICO_DOCFIS | VARCHAR2(4) | N |  |  |
| 2 | SERVICO_DIM | VARCHAR2(4) | N |  |  |
| 3 | VALID_SERVICO | DATE | N |  |  |

**PK**: SERVICO_DOCFIS, VALID_SERVICO

---

## DIPJ_MAN_FICHAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VERSAO_DIPJ | VARCHAR2(4) | N |  |  |
| 4 | ANO_CALENDARIO | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFICADORA | CHAR(1) | N |  |  |
| 6 | QUALIFICACAO_PJ | CHAR(1) | Y |  |  |
| 7 | FICHA | VARCHAR2(4) | N |  |  |
| 8 | CAMPO | NUMBER(3) | N |  |  |
| 9 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_PARC_NDEDUT | NUMBER(17,2) | Y |  |  |
| 11 | IND_ENTIDADE_IMUNE | CHAR(1) | Y |  |  |
| 12 | IND_PJ_CONTRIB_PREV | CHAR(1) | Y |  |  |
| 13 | COD_PAIS | VARCHAR2(3) | N | ' ' |  |
| 14 | IND_HOMEPAGE_DISP | CHAR(1) | Y |  |  |
| 15 | IND_SERVIDOR_DISP | CHAR(1) | Y |  |  |
| 16 | IND_FORMA_RECEB | CHAR(1) | Y |  |  |
| 17 | COD_NAT_OP | VARCHAR2(5) | N | ' ' |  |
| 18 | CNPJ_ESTAB | VARCHAR2(14) | N | ' ' |  |
| 19 | COD_ATIVIDADE | NUMBER(7) | N | 0 |  |
| 20 | NOME_EMPRESARIAL | VARCHAR2(150) | Y |  |  |
| 21 | IND_ORGAO_PUB | CHAR(1) | Y |  |  |
| 22 | COD_DARF | VARCHAR2(4) | N | ' ' |  |
| 23 | IND_PES_FIS_JUR | VARCHAR2(2) | N | ' ' |  |
| 24 | QUALIFICACAO | VARCHAR2(2) | Y |  |  |
| 25 | CPF_REPR_LEGAL | VARCHAR2(11) | Y |  |  |
| 26 | QUALIFICACAO_RL | CHAR(1) | Y |  |  |
| 27 | IND_ESCRIT_MM | CHAR(1) | Y |  |  |
| 28 | IND_ALTERACAO_CAPITAL | CHAR(1) | Y |  |  |
| 29 | IND_OPCAO_ESCRIT | CHAR(1) | Y |  |  |
| 30 | IND_AVALIACAO_ESTOQUES | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, VERSAO_DIPJ, ANO_CALENDARIO, IND_RETIFICADORA, FICHA, CAMPO, COD_PAIS, COD_NAT_OP, CNPJ_ESTAB, COD_ATIVIDADE, COD_DARF, IND_PES_FIS_JUR

---

## DIPJ_MAN_LUCR_PREJU_ACUM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VERSAO_DIPJ | VARCHAR2(4) | N |  |  |
| 4 | ANO_CALENDARIO | VARCHAR2(4) | N |  |  |
| 5 | IND_RETIFICADORA | CHAR(1) | N |  |  |
| 6 | BALAN_TRANS_FOLHAS | VARCHAR2(10) | Y |  |  |
| 7 | NUM_DIARIO | VARCHAR2(10) | Y |  |  |
| 8 | NUM_REG_DIARIO | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, VERSAO_DIPJ, ANO_CALENDARIO, IND_RETIFICADORA

---

## DIPJ_PAR_FICHAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | VERSAO_DIPJ | VARCHAR2(4) | N |  |  |
| 4 | QUALIFICACAO_PJ | CHAR(1) | Y |  |  |
| 5 | FICHA | VARCHAR2(4) | N |  |  |
| 6 | CAMPO | NUMBER(3) | N |  |  |
| 7 | EXPRESSAO_CONTA | CLOB | Y |  |  |
| 8 | EXPRESSAO_CCUSTO | CLOB | Y |  |  |
| 9 | EXPRESSAO_SQL | CLOB | Y |  |  |
| 10 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 11 | GRUPO_CCUSTO | VARCHAR2(9) | Y |  |  |
| 12 | IND_ATIVO | CHAR(1) | Y | 'S' |  |
| 13 | IND_CONTA_REDUZ | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, VERSAO_DIPJ, FICHA, CAMPO

---

## DIRF_NOMENCLATURA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CLASS_VERBA | CHAR(1) | N |  |  |
| 2 | CLASS_AD_DIM | VARCHAR2(2) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(150) | Y |  |  |

**PK**: CLASS_VERBA, CLASS_AD_DIM

---

## DMS_CAMP_PRT_TPDOC
**Comment**: Tabela para armazenar o relacionamento entre os Tipos de Documentos MSAF com os da DMS Campinas.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 2 | DAT_VALID | DATE | N |  |  |
| 3 | COD_TIPO_DOCTO | VARCHAR2(2) | Y |  |  |

**PK**: IDENT_DOCTO, DAT_VALID

---

## DMS_CG_PAR_SERIE
**Comment**: Tabela utilizada na parametrização do DE-PARA entre a Série do documento fiscal e a Série da DMS de Campo Grande - MS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 2 | SERIE_DMS | VARCHAR2(2) | Y |  |  |
| 3 | VALID_SERIE | DATE | N |  |  |

**PK**: SERIE_DOCFIS, VALID_SERIE

---

## DMS_DADOS_INI
**Comment**: Parametrizacao dos dados iniciais de alguns modulos municipais como DMS Campinas, DDS Fortaleza e DFMS Belem.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_UNID | CHAR(1) | Y |  |  |
| 4 | NOM_CONTATO | VARCHAR2(70) | Y |  |  |
| 5 | NUM_DDD | VARCHAR2(4) | Y |  |  |
| 6 | NUM_TELEFONE | VARCHAR2(8) | Y |  |  |
| 7 | NUM_RAMAL | VARCHAR2(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DMS_DEDUCAO_DOCFIS

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
| 11 | NUM_DOCFIS_DED | VARCHAR2(9) | N |  | Numero do documento de deducao |
| 12 | DATA_EMISSAO | DATE | N |  | Data de Emissao do documento de deducao |
| 13 | IND_DEDUCAO | CHAR(1) | N |  | Tipo de Deducao: M - Material, S - Subempreitada, I - Incentivo a cultura, A - servico, B - alimentacao, C - reembolso, D - outras deducoes, E - repasse. |
| 14 | VLR_DOCFIS_DED | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 17 | IDENT_FIS_JUR_DED | NUMBER(12) | Y |  | Pessoa Fis/Jur do documento de deducao |
| 18 | SERIE_DOCFIS_DED | VARCHAR2(3) | Y |  | Serie do documento de deducao |
| 19 | SUB_SERIE_DOCFIS_DED | VARCHAR2(2) | Y |  | Sub-serie do documento de deducao |
| 20 | IDENT_DOCTO_DED | NUMBER(12) | Y |  | Tipo Documento do documento de deducao |
| 21 | IND_SITUACAO_DED | CHAR(1) | Y |  | Situacao Operacao: A – Aquisicao de Material, T – Transferencia de Material |
| 22 | ALIQ_TRIB_ISS_DED | NUMBER(7,4) | Y |  | Aliquota |
| 23 | IND_ISS_RETIDO_DED | CHAR(1) | Y |  | ISS Retido: S, N |
| 24 | VLR_ISS_RETIDO_DED | NUMBER(17,2) | Y |  | Valor ISS Retido |
| 25 | DATA_RETENCAO_DED | DATE | Y |  | Data Retencao |
| 26 | OUTRAS_DED | VARCHAR2(200) | Y |  | Outras Deducoes |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS_DED, DATA_EMISSAO, IND_DEDUCAO

**FKs**:
- IDENT_DOCTO_DED → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR_DED → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_2632: (IDENT_FIS_JUR_DED)

---

## DMS_DOCFIS_DEDUCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 7 | CPF_CGC | VARCHAR2(14) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | NUM_DOCFIS_DED | VARCHAR2(9) | N |  |  |
| 12 | IND_DEDUCAO | CHAR(1) | Y |  |  |
| 13 | DATA_EMISSAO | DATE | Y |  |  |
| 14 | VLR_DOCFIS_DED | NUMBER(15,2) | Y |  |  |
| 15 | VLR_DEDUCAO | NUMBER(15,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, CPF_CGC, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS_DED

---

## DMS_MANAUS_DADOS_INI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_ALT_ENDERECO | CHAR(1) | Y |  |  |
| 4 | COD_RESPONSAVEL_LEGAL | VARCHAR2(2) | Y |  |  |
| 5 | COD_RESPONSAVEL_INFO | VARCHAR2(2) | Y |  |  |
| 6 | COD_BAIRRO | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL_LEGAL → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_RESPONSAVEL_INFO → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## DMS_MATERIAL_DOCFIS

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
| 11 | COD_MATERIAL | VARCHAR2(7) | N |  |  |
| 12 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 13 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_MATERIAL

---

## DMS_PALMAS_DADOS_INI
**Comment**: Parametrização dos dados iniciais da DMS Palmas.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | Y |  |  |
| 4 | DATA_FIM | DATE | Y |  |  |
| 5 | IND_RECOLHE_DAS | CHAR(1) | Y |  |  |
| 6 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## DST_DF_MM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | NUMBER(4) | N |  |  |
| 4 | MES_REF | NUMBER(2) | N |  |  |
| 5 | IND_TIPO | CHAR(1) | N |  |  |
| 6 | IND_SITUACAO | CHAR(1) | N |  |  |
| 7 | VLR_REC_BRUTA | NUMBER(11,2) | Y |  |  |
| 8 | VLR_DED_SUBEMPR | NUMBER(11,2) | Y |  |  |
| 9 | VLR_DED_MAT_EMPR | NUMBER(11,2) | Y |  |  |
| 10 | VLR_REC_NTRIB | NUMBER(11,2) | Y |  |  |
| 11 | VLR_BASE_ISS_05 | NUMBER(11,2) | Y |  |  |
| 12 | VLR_ISS_DEVIDO_05 | NUMBER(11,2) | Y |  |  |
| 13 | VLR_ISS_CONTR_05 | NUMBER(11,2) | Y |  |  |
| 14 | VLR_ISS_SUB_05 | NUMBER(11,2) | Y |  |  |
| 15 | VLR_BASE_ISS_01 | NUMBER(11,2) | Y |  |  |
| 16 | VLR_ISS_DEVIDO_01 | NUMBER(11,2) | Y |  |  |
| 17 | VLR_ISS_CONTR_01 | NUMBER(11,2) | Y |  |  |
| 18 | VLR_ISS_SUB_01 | NUMBER(11,2) | Y |  |  |
| 19 | VLR_BASE_ISS_02 | NUMBER(11,2) | Y |  |  |
| 20 | VLR_ISS_DEVIDO_02 | NUMBER(11,2) | Y |  |  |
| 21 | VLR_ISS_CONTR_02 | NUMBER(11,2) | Y |  |  |
| 22 | VLR_ISS_SUB_02 | NUMBER(11,2) | Y |  |  |
| 23 | VLR_BASE_ISS_5 | NUMBER(11,2) | Y |  |  |
| 24 | VLR_ISS_DEVIDO_5 | NUMBER(11,2) | Y |  |  |
| 25 | VLR_ISS_CONTR_5 | NUMBER(11,2) | Y |  |  |
| 26 | VLR_ISS_SUB_5 | NUMBER(11,2) | Y |  |  |
| 27 | VLR_BASE_ISS_10 | NUMBER(11,2) | Y |  |  |
| 28 | VLR_ISS_DEVIDO_10 | NUMBER(11,2) | Y |  |  |
| 29 | VLR_ISS_CONTR_10 | NUMBER(11,2) | Y |  |  |
| 30 | VLR_ISS_SUB_10 | NUMBER(11,2) | Y |  |  |
| 31 | VLR_BASE_ISS | NUMBER(11,2) | Y |  |  |
| 32 | VLR_ISS_DEVIDO | NUMBER(11,2) | Y |  |  |
| 33 | VLR_ISS_CONTR | NUMBER(11,2) | Y |  |  |
| 34 | VLR_ISS_COMPENSAR | NUMBER(11,2) | Y |  |  |
| 35 | VLR_ISS_SUB | NUMBER(11,2) | Y |  |  |
| 36 | VLR_BASE_ST_05 | NUMBER(11,2) | Y |  |  |
| 37 | VLR_ISS_DEVIDO_ST_05 | NUMBER(11,2) | Y |  |  |
| 38 | VLR_BASE_ST_01 | NUMBER(11,2) | Y |  |  |
| 39 | VLR_ISS_DEVIDO_ST_01 | NUMBER(11,2) | Y |  |  |
| 40 | VLR_BASE_ST_02 | NUMBER(11,2) | Y |  |  |
| 41 | VLR_ISS_DEVIDO_ST_02 | NUMBER(11,2) | Y |  |  |
| 42 | VLR_BASE_ST_5 | NUMBER(11,2) | Y |  |  |
| 43 | VLR_ISS_DEVIDO_ST_5 | NUMBER(11,2) | Y |  |  |
| 44 | VLR_BASE_ST_10 | NUMBER(11,2) | Y |  |  |
| 45 | VLR_ISS_DEVIDO_ST_10 | NUMBER(11,2) | Y |  |  |
| 46 | VLR_BASE_ST | NUMBER(11,2) | Y |  |  |
| 47 | VLR_ISS_DEVIDO_ST | NUMBER(11,2) | Y |  |  |
| 48 | VLR_PAGTO_NTRIB | NUMBER(11,2) | Y |  |  |
| 49 | VLR_DESPESAS | NUMBER(11,2) | Y |  |  |
| 50 | DATA_ENCERRAMENTO | DATE | Y |  |  |
| 51 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, IND_TIPO, IND_SITUACAO

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## DST_RE_MM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | CPF_CNPJ_DECLARAN | VARCHAR2(14) | Y |  |  |
| 4 | IND_E_S | CHAR(1) | Y |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | DATA_FISCAL | DATE | Y |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | IND_ARQUIVO | CHAR(1) | Y |  |  |
| 10 | CPF_CNPJ_FISJUR | VARCHAR2(14) | Y |  |  |
| 11 | RAZAO_FISJUR | VARCHAR2(70) | Y |  |  |
| 12 | IND_TP_RECOLHIMEN | CHAR(1) | Y |  |  |
| 13 | IND_TIPO_DOCTO | CHAR(1) | Y |  |  |
| 14 | IND_ISS_RETIDO | CHAR(1) | Y |  |  |
| 15 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_MATERIAL | NUMBER(17,2) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | DAT_PAGAMENTO | DATE | Y |  |  |
| 21 | IND_DOM_RECIFE | CHAR(1) | Y |  |  |
| 22 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 23 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 24 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |
| 25 | IND_DEDUCAO | CHAR(1) | Y |  |  |
| 26 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 28 | DATA_EMISSAO_MAPA | DATE | Y |  |  |
| 29 | SERIE_MAPA | VARCHAR2(3) | Y |  |  |
| 30 | SUB_SERIE_MAPA | VARCHAR2(2) | Y |  |  |
| 31 | NUM_MAPA | VARCHAR2(12) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_DST_RE_MM_01: (COD_EMPRESA, COD_ESTAB, CPF_CNPJ_DECLARAN, IND_E_S, NUM_DOCFIS, SERIE_DOCFIS, DATA_FISCAL, DATA_EMISSAO, IND_ARQUIVO)

---

## DST_SA_MM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | CNPJ_ESTAB | VARCHAR2(14) | Y |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 6 | SUBSERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 7 | DATA_FISCAL | DATE | Y |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | IND_ARQUIVO | CHAR(1) | Y |  |  |
| 10 | IND_TP_TABELA | VARCHAR2(2) | Y |  |  |
| 11 | IND_TP_SERVICO | VARCHAR2(2) | Y |  |  |
| 12 | SITUACAO | CHAR(1) | Y |  |  |
| 13 | COD_TP_DOCTO | VARCHAR2(5) | Y |  |  |
| 14 | IND_ISS_RETIDO | CHAR(1) | Y |  |  |
| 15 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 18 | ATIVIDADE | VARCHAR2(7) | Y |  |  |
| 19 | CPF_CNPJ_FISJUR | VARCHAR2(14) | Y |  |  |
| 20 | COD_MOTIVO | VARCHAR2(10) | Y |  |  |
| 21 | DSC_MOTIVO | VARCHAR2(100) | Y |  |  |
| 22 | NUM_NF_SUBST | VARCHAR2(12) | Y |  |  |
| 23 | SERIE_NF_SUBST | VARCHAR2(3) | Y |  |  |
| 24 | SSERIE_NF_SUBST | VARCHAR2(2) | Y |  |  |
| 25 | DT_EMIS_NFSUBST | DATE | Y |  |  |
| 26 | COD_TP_DOC_SUBST | VARCHAR2(5) | Y |  |  |
| 27 | NUM_OCORRENCIA | VARCHAR2(10) | Y |  |  |
| 28 | DATA_PUBLICACAO | DATE | Y |  |  |
| 29 | MUNICIPIO | VARCHAR2(6) | Y |  |  |
| 30 | USUARIO | VARCHAR2(40) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 32 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  | ECF - Campo utilizado no registro de Cupons Fiscais Emitidos |
| 33 | NUM_CONTADOR_Z | VARCHAR2(12) | Y |  | ECF - Campo utilizado no registro de Cupons Fiscais Emitidos |
| 34 | NUM_CUPOM_INI | VARCHAR2(12) | Y |  | ECF - Campo utilizado no registro de Cupons Fiscais Emitidos |
| 35 | NUM_CUPOM_FIM | VARCHAR2(12) | Y |  | ECF - Campo utilizado no registro de Cupons Fiscais Emitidos |
| 36 | BASE_CALC_ISS | NUMBER(17,2) | Y |  | ECF - Campo utilizado no registro de Cupons Fiscais Emitidos |
| 37 | IND_PREST_SIMPLES_NAC | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_DST_SA_MM_01: (COD_EMPRESA, COD_ESTAB, CNPJ_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, SUBSERIE_DOCFIS, DATA_FISCAL, DATA_EMISSAO, IND_ARQUIVO, IND_TP_TABELA)
- IX_DST_SA_MM_02: (COD_EMPRESA, COD_ESTAB, IND_TP_TABELA, DATA_FISCAL)

---

## DST_SA_PAR_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 2 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 3 | COD_DOCTO_ARQ | VARCHAR2(3) | Y |  |  |

**PK**: GRUPO_DOCTO, COD_DOCTO

---

## DW_EXPORTA_ARQUIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | SEQ_ARQUIVO | NUMBER(9) | N |  |  |
| 3 | NOME_ARQUIVO | VARCHAR2(50) | Y |  |  |
| 4 | BINARIO | BLOB | Y |  |  |

**PK**: PROC_ID, SEQ_ARQUIVO

---

## DW_IMPORTA_ARQUIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ_ARQUIVO | NUMBER(9) | N |  |  |
| 2 | NOME_ARQUIVO | VARCHAR2(300) | Y |  |  |
| 3 | BINARIO | BLOB | Y |  |  |
| 4 | COD_MODULO | VARCHAR2(40) | Y |  |  |
| 5 | DT_INCLUSAO | DATE | Y | sysdate |  |

**PK**: SEQ_ARQUIVO

---

## ECF_CAD_DYNTB
**Comment**: Tabela dinamica do ECF (TFIX87).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAD_DYNTB | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_ECF_CAD_DYNTB. |
| 2 | COD_VERSION | VARCHAR2(5) | N |  | Codigo da versao da tabela dinamica. |
| 3 | DAT_STARTUP_EFFECTIVE | DATE | N |  | Data de inicio da validade da versao da tabela dinamica. |
| 4 | DAT_END_EFFECTIVE | DATE | Y |  | Data fim da validade da versao da tabela dinamica. |
| 5 | DSC_VERSION | VARCHAR2(100) | Y |  | Descricao da versao da tabela dinamica. |

**PK**: IDENT_CAD_DYNTB

**Indexes**:
- UK_ECF_CAD_DYNTB_001 (UNIQUE): (COD_VERSION)

---

## ECF_CAD_DYNTB_IT
**Comment**: Contem a relacao de itens pertencentes a uma versao da tabela dinamica.(TFIX89)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAD_DYNTB_IT | NUMBER(12) | N |  | Identificador unico do registro na tabela.  Sequence SEQ_ECF_CAD_DYNTB_IT. |
| 2 | IDENT_CAD_DYNTB_RC | NUMBER(12) | N |  | Identificador do registro pertencente a versao da tabela dinamica. |
| 3 | COD_ITEM | VARCHAR2(10) | N |  | Codigo do item da tabela dinamica. |
| 4 | DAT_STARTUP_EFFECTIVE | DATE | N |  | Data inicial de validade do item da tabela dinamica. |
| 5 | DAT_END_EFFECTIVE | DATE | Y |  | Data final da validade do item da tabela dinamica. |
| 6 | DSC_ITEM | VARCHAR2(500) | N |  | Descricao do item da tabela dinamica. |
| 7 | NUM_ORDER | NUMBER(5) | N |  | Numero de ordenacao do item na tabela dinamica. |
| 8 | IND_ITEM_TYPE | VARCHAR2(3) | N |  | Tipo do item da tabela dinamica, podendo ser: R - Rotulo; E - Editavel; CA - Calculo Alteravel; CNA - Calculo Nao Alteravel. |
| 9 | IND_ITEM_FORMAT | VARCHAR2(2) | Y |  | Indicador de formato do campo, podendo ser:  A - Alfanumerico; N - Numerico; NS - Numerico Sinalizado. |
| 10 | NUM_LINE | NUMBER(5) | Y |  | Numero da linha da ECF. |
| 11 | TXT_FORMULA | VARCHAR2(4000) | Y |  | Formula de calculo do item da tabela dinamica. |
| 12 | IND_ENTRY_TYPE | CHAR(1) | Y |  | Indicador do tipo de lancamento, podendo ser:  A - Adicao;  E - Exlcusao; P - Compensacao de Prejuizos R - Rotulo; L - Lucro Liquido. |
| 13 | PCT_ACCOUNT_BAL | NUMBER(7,4) | Y |  | Percentual do Saldo a ser considerado no processo de importacao do saldo. |

**PK**: IDENT_CAD_DYNTB_IT

**FKs**:
- IDENT_CAD_DYNTB_RC → ECF_CAD_DYNTB_RC(IDENT_CAD_DYNTB_RC)

**Indexes**:
- UK_ECF_CAD_DYNTB_IT_001 (UNIQUE): (IDENT_CAD_DYNTB_RC, COD_ITEM, DAT_STARTUP_EFFECTIVE)

---

## ECF_CAD_DYNTB_RC
**Comment**: Contem a relacao de registros da versao da tabela dinamica (TFIX88).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAD_DYNTB_RC | NUMBER(12) | N |  | Identificador unico do registro na tabela.  Sequence SEQ_ECF_CAD_DYNTB_RC. |
| 2 | IDENT_CAD_DYNTB | NUMBER(12) | N |  | Identificador da versao da tabela dinamica. |
| 3 | COD_RECORD | VARCHAR2(8) | N |  | Codigo do registro pertencente a versao. |
| 4 | DSC_RECORD | VARCHAR2(200) | N |  | Descricao do registro da versao da tabela dinamica. |

**PK**: IDENT_CAD_DYNTB_RC

**FKs**:
- IDENT_CAD_DYNTB → ECF_CAD_DYNTB(IDENT_CAD_DYNTB)

**Indexes**:
- UK_ECF_CAD_DYNTB_RC_001 (UNIQUE): (IDENT_CAD_DYNTB, COD_RECORD)

---

## ECF_CAD_PLREF
**Comment**: Tabela de Cadastro do Plano de Contas Referencial - Versoes (TFIX90).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAD_PLREF | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_ECF_CAD_PLREF. |
| 2 | COD_VERSION | VARCHAR2(5) | N |  | Versao do Plano Referencial. |
| 3 | DAT_STARTUP_EFFECTIVE | DATE | N |  | Data de Inicio Validade. |
| 4 | DAT_END_EFFECTIVE | DATE | Y |  | Data de Fim de Validade. |
| 5 | DSC_VERSION | VARCHAR2(100) | Y |  | Descricao da versao do plano referencial. |

**PK**: IDENT_CAD_PLREF

**Indexes**:
- UK_ECF_CAD_PLREF_001 (UNIQUE): (COD_VERSION)

---

## ECF_CAD_PLREF_CTA
**Comment**: Tabela de Cadastro das Contas Referenciais do Plano de Contas Referencial (TFIX92).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAD_PLREF_CTA | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_ECF_CAD_PLREF_CTA. |
| 2 | IDENT_CAD_PLREF_RC | NUMBER(12) | N |  | Identificador do registro pai - Registro ECF do Plano Referencial. |
| 3 | COD_CTA_REF | VARCHAR2(30) | N |  | Codigo da Conta Referencial. |
| 4 | DAT_STARTUP_EFFECTIVE | DATE | N |  | Data de Inicio Validade. |
| 5 | DAT_END_EFFECTIVE | DATE | Y |  | Data de Fim de Validade. |
| 6 | DSC_CTA_REF | VARCHAR2(200) | N |  | Descricao da Conta Referencial. |
| 7 | NUM_ORDER | NUMBER(5) | Y |  | Numero de Ordem da Conta Referencial. |
| 8 | IND_CTA_TYPE | CHAR(1) | N |  | Tipo da Conta. Dominio:  S - Sintetica A - Analitica. |
| 9 | NUM_LEVEL | NUMBER(5) | Y |  | Nivel da Conta Referencial. Exemplo: 1 , 2 , 3. |
| 10 | COD_NAT_CTA | VARCHAR2(2) | Y |  | Natureza da Conta. Dominio:  01 - 02 - 03 -  04 -  05 -  |
| 11 | COD_CAD_PLREF_CTA_UP | VARCHAR2(30) | Y |  | Identificador da Conta Referencial Superiora. |

**PK**: IDENT_CAD_PLREF_CTA

**FKs**:
- IDENT_CAD_PLREF_RC → ECF_CAD_PLREF_RC(IDENT_CAD_PLREF_RC)

**Indexes**:
- UK_ECF_CAD_PLREF_CTA (UNIQUE): (COD_CTA_REF, IDENT_CAD_PLREF_RC)

---

## ECF_CAD_PLREF_RC
**Comment**: Tabela de Cadastro dos Registros ECF do Plano de Contas Referencial (TFIX91).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAD_PLREF_RC | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_ECF_CAD_PLREF_RC. |
| 2 | IDENT_CAD_PLREF | NUMBER(12) | N |  | Identificador do registro pai - Versao do Plano Referencial. |
| 3 | COD_RECORD | VARCHAR2(8) | N |  | Codigo do Registro ECF do Plano Referencial. |
| 4 | DSC_RECORD | VARCHAR2(200) | Y |  | Descricao do registro ECF do plano referencial. |

**PK**: IDENT_CAD_PLREF_RC

**FKs**:
- IDENT_CAD_PLREF → ECF_CAD_PLREF(IDENT_CAD_PLREF)

**Indexes**:
- UK_ECF_CAD_PLREF_RC_001 (UNIQUE): (IDENT_CAD_PLREF, COD_RECORD)

---

## ECF_CONTAS_CCUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 5 | COD_CUSTO | VARCHAR2(50) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, COD_CONTA, COD_CUSTO

---

## ELEG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | ELEG_COD_LEGAL | NUMBER(4) | N |  |  |
| 4 | ELEG_COD_HIPOT | NUMBER(2) | Y |  |  |
| 5 | ELEG_DSC_HIPOT | VARCHAR2(150) | Y |  |  |
| 6 | ELEG_DSC_ANEXO | VARCHAR2(20) | Y |  |  |
| 7 | ELEG_DSC_ARTIGO | VARCHAR2(20) | Y |  |  |
| 8 | ELEG_DSC_INCISO | VARCHAR2(20) | Y |  |  |
| 9 | ELEG_DSC_ALINEA | VARCHAR2(20) | Y |  |  |
| 10 | ELEG_DSC_PARAG | VARCHAR2(20) | Y |  |  |
| 11 | ELEG_DSC_ITEM | VARCHAR2(20) | Y |  |  |
| 12 | ELEG_DSC_LETRA | VARCHAR2(20) | Y |  |  |
| 13 | ELEG_OBS | VARCHAR2(255) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, ELEG_COD_LEGAL

---

## EMISSAO_LIVRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | NUM_LIVRO | VARCHAR2(6) | N |  |  |
| 5 | NUM_PAGINA_INICIAL | VARCHAR2(6) | Y |  |  |
| 6 | NUM_PAGINA_FINAL | VARCHAR2(6) | Y |  |  |
| 7 | DAT_APUR_INI | DATE | Y |  |  |
| 8 | DAT_APURACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, NUM_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO → OBRIGACAO_FISCAL(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO)

---

## EMIT_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_EMIT_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_FIS_JUR)

---

## EMPRESA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 3 | SENHA | VARCHAR2(75) | Y |  |  |
| 4 | CNPJ | VARCHAR2(14) | Y |  |  |
| 5 | CNPJ_CONTRATANTE | VARCHAR2(14) | Y |  |  |
| 6 | IND_VALIDA_CNPJ | CHAR(1) | Y | 'S' |  |
| 7 | DAT_EMISSAO_LIC | DATE | Y |  | Data de emissao do ultimo arquivo do licenciamento |
| 8 | VALIDADOR_SENHA_LIC | VARCHAR2(50) | Y |  | Senha validadora do licenciamento dos módulos  |
| 9 | DATA_1 | DATE | Y |  |  |
| 10 | ORDEM_LIC | NUMBER | Y |  | Ordem da empresa no arquivo do licenciamento |
| 11 | IND_GEROU_ARQ | CHAR(1) | Y | 'N' | ARQUIVO DE INFORMAÇÕES DA EMPRESA PARA SER ENVIADO A MASTERSAF |

**PK**: COD_EMPRESA

---

## EMPRESA_ESTAB_INCORP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA_INCORPORADORA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_INCORPORADORA | VARCHAR2(6) | N |  |  |
| 3 | COD_EMPRESA_INCORPORADA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB_INCORPORADA | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA_INCORPORADORA, COD_ESTAB_INCORPORADORA, COD_EMPRESA_INCORPORADA, COD_ESTAB_INCORPORADA

**FKs**:
- COD_EMPRESA_INCORPORADORA, COD_ESTAB_INCORPORADORA → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA_INCORPORADA, COD_ESTAB_INCORPORADA → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UK_EMPRESA_ESTAB_INCORP (UNIQUE): (COD_EMPRESA_INCORPORADA, COD_ESTAB_INCORPORADA)

---

## EMP_PRESUMIDO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO | NUMBER(4) | N |  |  |
| 3 | REC_EXPORT_ANO | NUMBER(17,2) | Y |  |  |
| 4 | REC_OP_BRUTA_ANO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, ANO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## ENVIO_INFORME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | ANO_BASE | NUMBER(4) | N |  |  |
| 4 | CPF_CGC | VARCHAR2(14) | N |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 6 | CNPJ_ESTAB | VARCHAR2(14) | Y |  |  |
| 7 | EMAIL | VARCHAR2(255) | Y |  |  |
| 8 | NOME_BENEFICIARIO | VARCHAR2(200) | Y |  |  |
| 9 | GRUPO_RETENCAO | VARCHAR2(9) | Y |  |  |
| 10 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 11 | COD_ESTADO | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, CPF_CGC, NUM_PROCESSO

---

## EQUIPAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EQUIPAMENTO | VARCHAR2(3) | N |  |  |
| 2 | ESP_EQUIPAMENTO | VARCHAR2(50) | Y |  |  |
| 3 | DSC_MODELO | VARCHAR2(30) | Y |  |  |

**PK**: COD_EQUIPAMENTO

---

## ESA_DF_GIM_MM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 6 | REG_MM1 | LONG | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

---

## ESA_PE_GIA_QC_REL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | COD_OPER | CHAR(1) | N |  |  |
| 7 | IND_RECUPERACAO | CHAR(1) | N |  |  |
| 8 | IDENT_DOCTO_FISCAL | NUMBER(12) | N |  |  |
| 9 | DSC_MUNIC | VARCHAR2(50) | Y |  |  |
| 10 | IND_ENT_SAI | CHAR(1) | Y |  |  |
| 11 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 12 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO, COD_MUNICIPIO, COD_OPER, IND_RECUPERACAO, IDENT_DOCTO_FISCAL

---

## ESA_PI_GIM_MM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 6 | REG_MM | VARCHAR2(2000) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, MES_APURACAO, ANO_APURACAO

---

## ESA_SP_CONF_SALDO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | VARCHAR2(40) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 7 | SALDO_INI | NUMBER(13,3) | Y |  |  |
| 8 | QTD_ENTRADA | NUMBER(13,3) | Y |  |  |
| 9 | QTD_SAIDA | NUMBER(13,3) | Y |  |  |
| 10 | SALDO_DIA | NUMBER(13,3) | Y |  |  |
| 11 | SALDO_FIM | NUMBER(13,3) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, COD_PRODUTO, DATA_FISCAL

---

## ESDRA_LICENSE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LICENCA | NUMBER(38) | N |  |  |
| 2 | DATA_EMISSAO | VARCHAR2(10) | Y |  |  |
| 3 | VALIDADOR_SENHA | VARCHAR2(14) | Y |  |  |
| 4 | CONTRATANTE_CNPJ | VARCHAR2(18) | Y |  |  |
| 5 | LICENCA_XML | CLOB | Y |  |  |

**PK**: ID_LICENCA

---

## ESDRA_MENU

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | ID_PROGRAM | NUMBER(38) | Y |  |  |
| 3 | NAME | VARCHAR2(255) | N |  |  |
| 4 | SEQUENCE | NUMBER | N |  |  |
| 5 | HEADER | NUMBER(1) | Y |  |  |
| 6 | CHILDLESS | NUMBER(1) | Y |  |  |
| 7 | ID_PARENT | NUMBER(38) | Y |  |  |

**PK**: ID

**FKs**:
- ID_PARENT → ESDRA_MENU(ID)
- ID_PROGRAM → ESDRA_PROGRAM(ID)

---

## ESDRA_PROGRAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | CODE | VARCHAR2(255) | N |  |  |
| 3 | NAME | VARCHAR2(255) | N |  |  |
| 4 | ROUTE | VARCHAR2(255) | N |  |  |
| 5 | DESCRIPTION | VARCHAR2(255) | N |  |  |
| 6 | HOTKEY | CHAR(1) | Y |  |  |
| 7 | DASHBOARD_NAME | VARCHAR2(255) | Y |  |  |
| 8 | DASHBOARD_HEIGHT | NUMBER | Y |  |  |

**PK**: ID

**Indexes**:
- ESDRA_UK_PROGRAM_CODE (UNIQUE): (CODE)

---

## ESDRA_PROGRAM_ROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PROGRAM | NUMBER(38) | N |  |  |
| 2 | ID_ROLE | NUMBER(38) | N |  |  |

**PK**: ID_PROGRAM, ID_ROLE

**FKs**:
- ID_PROGRAM → ESDRA_PROGRAM(ID)
- ID_ROLE → ESDRA_ROLE(ID_PERMISSAO)

---

## ESDRA_ROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PERMISSAO | NUMBER(38) | N |  |  |
| 2 | AUTHORITY | VARCHAR2(40) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(120) | Y |  |  |

**PK**: ID_PERMISSAO

---

## ESDRA_USER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_USUARIO | NUMBER(38) | N |  |  |
| 2 | USERNAME | VARCHAR2(100) | Y |  |  |
| 3 | NOME_COMPLETO | VARCHAR2(100) | Y |  |  |
| 4 | EMAIL | VARCHAR2(100) | Y |  |  |
| 5 | SALT | VARCHAR2(30) | Y |  |  |
| 6 | PASSWORD | VARCHAR2(80) | Y |  |  |
| 7 | ID_LICENCA | NUMBER(38) | Y |  |  |

**PK**: ID_USUARIO

**FKs**:
- ID_LICENCA → ESDRA_LICENSE(ID_LICENCA)

**Indexes**:
- ESDRA_UK_USER_EMAIL (UNIQUE): (EMAIL)
- ESDRA_UK_USER_USERNAME (UNIQUE): (USERNAME)

---

## ESDRA_USER_EXTENSIONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PARENT_ID | NUMBER(38) | N |  |  |
| 2 | COD_EMPRESA_ULTIMO_ACESSO | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB_ULTIMO_ACESSO | VARCHAR2(6) | Y |  |  |

**PK**: PARENT_ID

**FKs**:
- PARENT_ID → ESDRA_USER(ID_USUARIO)

---

## ESDRA_USER_EXT_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_USER_EXT | NUMBER(38) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: ID_USER_EXT, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- ID_USER_EXT → ESDRA_USER_EXTENSIONS(PARENT_ID)

---

## ESDRA_USER_EXT_SISTEMA_ORIGEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_USER_EXT | NUMBER(38) | N |  |  |
| 2 | ID_SISTEMA_ORIGEM | NUMBER(38) | N |  |  |

**PK**: ID_USER_EXT, ID_SISTEMA_ORIGEM

**FKs**:
- ID_SISTEMA_ORIGEM → SISTEMA_ORIGEM(ID)
- ID_USER_EXT → ESDRA_USER_EXTENSIONS(PARENT_ID)

---

## ESDRA_USER_ROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_USUARIO | NUMBER(38) | N |  |  |
| 2 | ID_PERMISSAO | NUMBER(38) | N |  |  |

**PK**: ID_USUARIO, ID_PERMISSAO

**FKs**:
- ID_PERMISSAO → ESDRA_ROLE(ID_PERMISSAO)
- ID_USUARIO → ESDRA_USER(ID_USUARIO)

---

## ESPECIE_VOLUME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EVOL_COD | CHAR(3) | N |  |  |
| 2 | EVOL_DAT_ATUA | DATE | N |  |  |
| 3 | EVOL_DSC | VARCHAR2(150) | Y |  |  |

**PK**: EVOL_COD, EVOL_DAT_ATUA

---

## ESTABELECIMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_MATRIZ_FILIAL | CHAR(1) | Y |  |  |
| 4 | COD_CLASSE | NUMBER(2) | Y |  |  |
| 5 | CGC | VARCHAR2(14) | Y |  |  |
| 6 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |
| 7 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 8 | INSC_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 9 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 10 | NOME_FANTASIA | VARCHAR2(50) | Y |  |  |
| 11 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 12 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 13 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 14 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 15 | CIDADE | VARCHAR2(30) | Y |  |  |
| 16 | DISTRITO | VARCHAR2(20) | Y |  |  |
| 17 | SUB_DISTRITO | VARCHAR2(20) | Y |  |  |
| 18 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 19 | CEP | NUMBER(8) | Y |  |  |
| 20 | DDD | VARCHAR2(5) | Y |  |  |
| 21 | TELEFONE | VARCHAR2(10) | Y |  |  |
| 22 | FAX | VARCHAR2(10) | Y |  |  |
| 23 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 24 | IND_VENDA_AMB | CHAR(1) | Y |  |  |
| 25 | IND_DIRF_CENTRAL | CHAR(1) | Y |  |  |
| 26 | TP_LOGRADOURO | VARCHAR2(3) | Y |  |  |
| 27 | ITENS_NOTA | NUMBER(2) | Y |  |  |
| 28 | IMPRIME | VARCHAR2(1) | Y |  |  |
| 29 | MULT_SERIE_S | VARCHAR2(1) | Y |  |  |
| 30 | NUM_PPVI_SN | VARCHAR2(1) | Y |  |  |
| 31 | SEQ_UNICO | VARCHAR2(1) | Y |  |  |
| 32 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 33 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 34 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 35 | IND_ST_NCONTRIB | CHAR(1) | Y |  |  |
| 36 | MARGEM_ST_NCONTRIB | NUMBER(5,2) | Y |  |  |
| 37 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 38 | COD_TP_RECOLH | VARCHAR2(3) | Y |  |  |
| 39 | IND_FORMA_ABAT | CHAR(1) | Y |  |  |
| 40 | IND_NUMERACAO | CHAR(1) | Y |  |  |
| 41 | EMAIL | VARCHAR2(50) | Y |  |  |
| 42 | IND_NBM_IEST | CHAR(1) | Y |  |  |
| 43 | IND_CONTRIB_IPI | CHAR(1) | Y |  |  |
| 44 | IND_CONTRIB_SUB | CHAR(1) | Y |  |  |
| 45 | DAT_INI_ATIVIDADE | DATE | Y |  |  |
| 46 | IND_APROVADOR | CHAR(1) | Y |  |  |
| 47 | INSC_DF | VARCHAR2(14) | Y |  |  |
| 48 | IND_IMUNE | CHAR(1) | Y | 'N' |  |
| 49 | IND_ISENTO | CHAR(1) | Y | 'N' |  |
| 50 | IND_ESCR_CONTAB | CHAR(1) | Y | 'N' |  |
| 51 | DATA_JUCEMAT | DATE | Y |  |  |
| 52 | DATA_SEFAZ | DATE | Y |  |  |
| 53 | IND_SECUNDARIO | CHAR(1) | Y | 'N' |  |
| 54 | IND_IPI_SJ | CHAR(1) | Y | 'N' |  |
| 55 | IND_IPISJ_REGRA_RB | CHAR(1) | Y | 'N' |  |
| 56 | DT_ENCERRAMENTO | DATE | Y |  |  |
| 57 | CEI_PORT63 | VARCHAR2(12) | Y |  |  |
| 58 | INSC_PORT63 | VARCHAR2(12) | Y |  |  |
| 59 | NUM_THREADS_MMAG | NUMBER | Y |  |  |
| 60 | CX_POSTAL | NUMBER(20) | Y |  |  |
| 61 | NUM_CEP_CX_POSTAL | NUMBER(8) | Y |  | código de endereçamento postal da caixa postal |
| 62 | COD_BENEF_ICMS | VARCHAR2(5) | Y |  | ATO COTEPE 70 - reg 0020 - Valores assumidos: DF001, PE001, PE002, PE003, SE001, TO001, TO002, TO003 |
| 63 | COD_BENEF_ISS | VARCHAR2(5) | Y |  | ATO COTEPE 70 - reg 0020 - Valores assumidos: DF001 |
| 64 | NUM_PROTOCOLO | NUMBER(10) | Y |  |  |
| 65 | DATA_PROTOCOLO | DATE | Y |  |  |
| 66 | DATA_CISAO | DATE | Y |  |  |
| 67 | DATA_FUSAO | DATE | Y |  |  |
| 68 | DATA_INCORPORACAO | DATE | Y |  |  |
| 69 | DAT_VALIDADE_INI_ATIVIDADE | DATE | Y |  |  |
| 70 | IND_ATIVIDADE | CHAR(1) | Y |  | 0 - Industriais ou Equiparado a Industrial, 1 – Outros, 2 – Prestador de servicos, 3 – Atividade de comercio, 4 – Atividade financeira, 5 Atividade imobiliaria, 6 – Entidade sujeita ao PIS/PASEP Folha de Salarios |
| 71 | IND_APUR_ICMS | CHAR(1) | Y |  | 1 - Apuracao Normal (livro 108), 2 - Apuracao por Inscricao Esdaual Unica (livro 165), 3 - Prodepe (livros 142/143) |
| 72 | IND_APUR_IPI | CHAR(1) | Y |  | 1 - Periodicidade unica  p/todos os produtos (livro 002), 2 - Periodicidade Decendial e Mensal ( IN SRF 446/04) |
| 73 | IND_CONV_ICMS | CHAR(1) | Y |  |  |
| 74 | DAT_OPERACAO | DATE | Y |  |  |
| 75 | USUARIO | VARCHAR2(40) | Y |  |  |
| 76 | IND_ISS | VARCHAR2(2) | Y |  |  |
| 77 | IND_ATIV_BASE_CALC_REDUZ | VARCHAR2(2) | Y |  |  |
| 78 | TIPO_ASSINANTE | VARCHAR2(1) | Y |  |  |
| 79 | NAT_PESSOA_JUR | VARCHAR2(2) | Y |  | Natureza de Pessoa Juridica: 00 - Sociedade Empresaria em Geral, 01 - Sociedade Cooperativa, 02 - Entidade sujeita ao PIS/PASEP exclusivamente Folha de Salarios |
| 80 | COD_INST_FINANC | VARCHAR2(10) | Y |  | Codigo do Banco ou Instituicao Financeira junto a Prefeitura. Codigo utilizado em diversas obrigações municipais, como no validador Betha. |
| 81 | IND_CONTRIB_EQ_CCIVIL | CHAR(1) | Y |  |  |
| 82 | NUM_ALVARA | VARCHAR2(11) | Y |  |  |
| 83 | IND_INST_FINANCEIRA | CHAR(1) | Y |  | Indicador para Instituicao Financeira: 1 - Sede com Contabilizacao Propria; 3 - Dependencia com Contabilizacao Propria; 5 – UAD – Unidade Administrativa Desmembrada com Contabilizacao Propria; 7 - Agencia |
| 84 | IND_REG_APUR_CONT_PREV | CHAR(1) | Y | '0' | EFD-PIS/COFINS - Registro 0145 - Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta |
| 85 | CERTIFICADO_DIGITAL | VARCHAR2(200) | Y |  |  |
| 86 | COD_ARI_ANP | VARCHAR2(10) | Y |  | Codigo do Agente Regulado Informante da ANP |
| 87 | COD_INSTAL_ANP | VARCHAR2(7) | Y |  | Codigo da Instalacao 1 da ANP |
| 88 | COMPL_ENDERECO_EFD | VARCHAR2(60) | Y |  |  |
| 89 | IND_ATIV_FINANCEIRA | CHAR(1) | Y |  |  |
| 90 | DSC_INF_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |
| 91 | RAZAO_SOCIAL_COMPL | VARCHAR2(250) | Y |  |  |
| 92 | BAIRRO_COMPL | VARCHAR2(60) | Y |  |  |
| 93 | COD_MOBILIARIO | NUMBER(9) | Y |  |  |
| 94 | DAT_TRANSF_SEDE | DATE | Y |  |  |
| 95 | DAT_TRANSF | DATE | Y |  |  |
| 96 | IND_CLAS_ESTAB | VARCHAR2(2) | Y |  | Classificação de Contribuintes do IPI |
| 97 | COD_NAT_JUR | VARCHAR2(4) | Y |  |  |
| 98 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)
- COD_CLASSE → CLASSE_ESTAB(COD_CLASSE_ESTAB)
- COD_ATIVIDADE, DAT_VALIDADE_INI_ATIVIDADE → ATIV_ECONOMICA(COD_ATIVIDADE, DAT_VALIDADE_INI)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- COD_TP_RECOLH → IST_TIPO_RECOLH(COD_TP_RECOLH)
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)

**Indexes**:
- IDX_ESTAB_APUR_IPI: (COD_EMPRESA, COD_ESTAB, IND_APUR_IPI)
- IX_TELAS: (COD_EMPRESA, COD_ESTAB, RAZAO_SOCIAL, IDENT_ESTADO)

---

## ESTAB_COMPOE_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_COMPOE_PRD | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## ESTAB_EXCL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI_ATIVIDADE | DATE | Y |  |  |
| 4 | CGC | VARCHAR2(14) | Y |  |  |
| 5 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 6 | IND_MATRIZ_FILIAL | CHAR(1) | Y |  |  |
| 7 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |
| 8 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 9 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 10 | CEP | NUMBER(8) | Y |  |  |
| 11 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 12 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |

---

## ESTADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DESTINATARIO | VARCHAR2(60) | Y |  |  |
| 5 | DEPARTAMENTO | VARCHAR2(60) | Y |  |  |
| 6 | CARGO | VARCHAR2(50) | Y |  |  |
| 7 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 8 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 9 | CEP | NUMBER(8) | Y |  |  |
| 10 | CIDADE | VARCHAR2(20) | Y |  |  |
| 11 | NUM_ESTADO | NUMBER(2) | Y |  |  |
| 12 | DIG_VERIFICADOR | NUMBER(1) | Y |  |  |
| 13 | COD_REGIAO | NUMBER(2) | Y |  |  |

**PK**: IDENT_ESTADO

**Indexes**:
- IX_CHAVE_NAT_UF (UNIQUE): (COD_ESTADO)
- IX_NUM_ESTADO (UNIQUE): (NUM_ESTADO)

---

## ETAPA_EMIS_LIVRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_LIVRO | VARCHAR2(6) | N |  |  |
| 6 | VRS_ETAPA | VARCHAR2(4) | N |  |  |
| 7 | NUM_PAGINA_INICIAL | VARCHAR2(6) | Y |  |  |
| 8 | NUM_PAGINA_FINAL | VARCHAR2(6) | Y |  |  |
| 9 | DAT_APUR_INI | DATE | Y |  |  |
| 10 | CALENDARIO | CHAR(1) | Y |  |  |
| 11 | IND_AUTENTIC_OK | CHAR(1) | Y |  |  |
| 12 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ICMS1 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ICMS2 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS3 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_IPI1 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_IPI2 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_IPI3 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, VRS_ETAPA, NUM_LIVRO

---

## ETAPA_EMIS_LVR_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FIM | DATE | N |  |  |
| 4 | VOLUME | VARCHAR2(3) | N |  |  |
| 5 | NUM_LIVRO | VARCHAR2(6) | N |  |  |
| 6 | NUM_PAGINA_INICIAL | VARCHAR2(6) | N |  |  |
| 7 | NUM_PAGINA_FINAL | VARCHAR2(6) | N |  |  |
| 8 | IND_EMISSAO | CHAR(1) | Y |  |  |
| 9 | DATA_INICIAL | DATE | Y |  |  |
| 10 | DAT_EMISSAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FIM, VOLUME, NUM_LIVRO, NUM_PAGINA_INICIAL, NUM_PAGINA_FINAL

---

## FCONT_IMP_INFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | ID_REG | VARCHAR2(6) | N |  |  |
| 6 | SEQ_REG | NUMBER(12) | N |  |  |
| 7 | ARQ_REF_IMP | VARCHAR2(1000) | Y |  |  |
| 8 | LIN_ARQ_REF_IMP | NUMBER(12) | Y |  |  |
| 9 | TXT_REG | VARCHAR2(4000) | Y |  |  |
| 10 | NUM_LANCTO | VARCHAR2(40) | Y |  |  |
| 11 | CONTA_CC | VARCHAR2(91) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, ID_REG, SEQ_REG

**Indexes**:
- IX_FCONT_IMP_INFO: (CONTA_CC)

---

## FCONT_MAN_LUCROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALEND | NUMBER(4) | N |  |  |
| 4 | IND_PERIODIC | VARCHAR2(3) | N |  |  |
| 5 | IND_LUCROC | VARCHAR2(2) | Y |  |  |
| 6 | VLR_LUCROC | NUMBER(17,2) | Y |  |  |
| 7 | FORMA_TRIB | VARCHAR2(1) | Y |  |  |
| 8 | TRIM_LUC_ARB | VARCHAR2(4) | Y |  |  |
| 9 | APUR_TRIM | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CALEND, IND_PERIODIC

---

## FCONT_PAR_IMP_LUCROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## FCONT_REL_BALAN_RES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 6 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 7 | COD_CONTA_REF | VARCHAR2(70) | N |  |  |
| 8 | DSC_CONTA | VARCHAR2(50) | Y |  |  |
| 9 | DSC_CUSTO | VARCHAR2(50) | Y |  |  |
| 10 | IND_SLD_CONTA | CHAR(1) | Y |  |  |
| 11 | SLD_CONTABIL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_INI_IF | NUMBER(17,2) | Y |  |  |
| 13 | IND_INI_IF | CHAR(1) | Y |  |  |
| 14 | VLR_INI_IS | NUMBER(17,2) | Y |  |  |
| 15 | IND_INI_IS | CHAR(1) | Y |  |  |
| 16 | VLR_TRANSF_TF | NUMBER(17,2) | Y |  |  |
| 17 | IND_TRANSF_TF | CHAR(1) | Y |  |  |
| 18 | VLR_TRANSF_TS | NUMBER(17,2) | Y |  |  |
| 19 | IND_TRANSF_TS | CHAR(1) | Y |  |  |
| 20 | VLR_TRANSF_TR | NUMBER(17,2) | Y |  |  |
| 21 | IND_TRANSF_TR | CHAR(1) | Y |  |  |
| 22 | VLR_EXPURGO | NUMBER(17,2) | Y |  |  |
| 23 | IND_EXPURGO | CHAR(1) | Y |  |  |
| 24 | VLR_INCLU | NUMBER(17,2) | Y |  |  |
| 25 | IND_INCLU | CHAR(1) | Y |  |  |
| 26 | VLR_ENCERRA_EF | NUMBER(17,2) | Y |  |  |
| 27 | IND_ENCERRA_EF | CHAR(1) | Y |  |  |
| 28 | SLD_FISCAL | NUMBER(17,2) | Y |  |  |
| 29 | IND_SLD_FISCAL | CHAR(1) | Y |  |  |
| 30 | SLD_SOCIETARIO | NUMBER(17,2) | Y |  |  |
| 31 | IND_SOCIETARIO | CHAR(1) | Y |  |  |
| 32 | VLR_DIF_SALDO | NUMBER(17,2) | Y |  |  |
| 33 | IND_DIF_SALDO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, COD_CONTA, COD_CUSTO, COD_CONTA_REF

---

## FCONT_REL_DEMONST_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | EXERCICIO | NUMBER(4) | N |  |  |
| 4 | PERIODO | VARCHAR2(3) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 6 | DSC_CONTA | VARCHAR2(50) | Y |  |  |
| 7 | VLR_EXPURGO | NUMBER(17,2) | Y |  |  |
| 8 | IND_EXPURGO | CHAR(1) | Y |  |  |
| 9 | VLR_INCL | NUMBER(17,2) | Y |  |  |
| 10 | IND_INCL | CHAR(1) | Y |  |  |
| 11 | VLR_LP_CONTA | NUMBER(17,2) | Y |  |  |
| 12 | IND_LP_CONTA | CHAR(1) | Y |  |  |
| 13 | VLR_LP_FISCAL | NUMBER(17,2) | Y |  |  |
| 14 | IND_LP_FISCAL | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, EXERCICIO, PERIODO, COD_CONTA

---

## FICHAS_DIPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PASTA | VARCHAR2(5) | Y |  |  |
| 2 | VERSAO | VARCHAR2(4) | N |  |  |
| 3 | TIPO | VARCHAR2(4) | N |  |  |
| 4 | FICHA | VARCHAR2(4) | N |  |  |
| 5 | QUALIFICACAO_PJ | VARCHAR2(1) | N |  |  |
| 6 | NOME | VARCHAR2(300) | Y |  |  |

**PK**: VERSAO, TIPO, FICHA, QUALIFICACAO_PJ

---

## FILIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | FILI_COD_CGC | VARCHAR2(16) | Y |  |  |
| 4 | UNFE_SIG | CHAR(2) | Y |  |  |
| 5 | FILI_COD_INSEST | VARCHAR2(14) | Y |  |  |
| 6 | FILI_COD_INSMUN | VARCHAR2(14) | Y |  |  |
| 7 | FILI_COD_ATIVECON | VARCHAR2(15) | Y |  |  |
| 8 | FILI_NOM | VARCHAR2(115) | Y |  |  |
| 9 | FILI_NOM_FANTASIA | VARCHAR2(70) | Y |  |  |
| 10 | FILI_END | VARCHAR2(70) | Y |  |  |
| 11 | FILI_END_NUM | NUMBER(12) | Y |  |  |
| 12 | FILI_END_COMP | VARCHAR2(45) | Y |  |  |
| 13 | FILI_END_BAIRRO | VARCHAR2(20) | Y |  |  |
| 14 | FILI_END_MUNIC | VARCHAR2(50) | Y |  |  |
| 15 | FILI_END_CEP | CHAR(8) | Y |  |  |
| 16 | FILI_COD_LOCAL | VARCHAR2(10) | Y |  |  |
| 17 | FILI_FAX | VARCHAR2(17) | Y |  |  |
| 18 | FILI_TEL | VARCHAR2(17) | Y |  |  |
| 19 | TP_LOC | CHAR(2) | Y |  |  |
| 20 | FILI_SETOR | CHAR(2) | Y |  |  |
| 21 | FILI_AUTOR | VARCHAR2(9) | Y |  |  |
| 22 | FILI_SANITARIA | VARCHAR2(50) | Y |  |  |
| 23 | FILI_LICEN | VARCHAR2(20) | Y |  |  |
| 24 | FILI_ESPEC | VARCHAR2(10) | Y |  |  |
| 25 | FILI_IND_RET_ISS | CHAR(1) | Y |  |  |
| 26 | FILI_COD_INSCEN | VARCHAR2(14) | Y |  |  |
| 27 | FILI_EMAIL | VARCHAR2(40) | Y |  |  |
| 28 | FILI_NAT_JUR | NUMBER(4) | Y |  |  |
| 29 | NUM01 | NUMBER | Y |  |  |
| 30 | NUM02 | NUMBER | Y |  |  |
| 31 | NUM03 | NUMBER | Y |  |  |
| 32 | VAR01 | VARCHAR2(150) | Y |  |  |
| 33 | VAR02 | VARCHAR2(150) | Y |  |  |
| 34 | VAR03 | VARCHAR2(150) | Y |  |  |
| 35 | VAR04 | VARCHAR2(150) | Y |  |  |
| 36 | VAR05 | VARCHAR2(150) | Y |  |  |
| 37 | FILI_CEI | VARCHAR2(12) | Y |  |  |
| 38 | FILI_NIT | VARCHAR2(11) | Y |  |  |
| 39 | FILI_SUFRAMA | VARCHAR2(9) | Y |  |  |
| 40 | FILI_MUN_IBGE | VARCHAR2(7) | Y |  |  |
| 41 | TPLD_COD | CHAR(2) | Y |  |  |
| 42 | FILI_NIRE | VARCHAR2(45) | Y |  |  |
| 43 | FILI_MATRIZ | CHAR(1) | Y |  |  |

**PK**: EMPS_COD, FILI_COD

---

## FPAR_CUSTOMIZADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PARAMETRO_CUSTOMIZADO | NUMBER | N |  |  |
| 2 | FRAMEWORK_PARAMETRO | VARCHAR2(50) | Y |  |  |
| 3 | IND_ATIVO | CHAR(1) | Y |  |  |

**PK**: ID_PARAMETRO_CUSTOMIZADO

**Indexes**:
- IX_FPAR_CUSTOMIZADO (UNIQUE): (FRAMEWORK_PARAMETRO)

---

## FPAR_PARAMETROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PARAMETROS | NUMBER | N |  |  |
| 2 | NOME_FRAMEWORK | VARCHAR2(30) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: ID_PARAMETROS

**Indexes**:
- IX_FPAR_PARAMETROS: (NOME_FRAMEWORK)
- IX_FPAR_PARAMETROS_AMBEV: (NOME_FRAMEWORK, ID_PARAMETROS)

---

## FPAR_PARAM_DET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PARAM_DET | NUMBER | N |  |  |
| 2 | ID_PARAMETRO | NUMBER | Y |  |  |
| 3 | NOME_PARAM | VARCHAR2(30) | Y |  |  |
| 4 | CONTEUDO | VARCHAR2(70) | Y | ' ' |  |
| 5 | VALOR | VARCHAR2(150) | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(300) | Y |  |  |

**PK**: ID_PARAM_DET

**FKs**:
- ID_PARAMETRO → FPAR_PARAMETROS(ID_PARAMETROS)

**Indexes**:
- IX_FPAR_PARAM_DET (UNIQUE): (ID_PARAMETRO, NOME_PARAM, CONTEUDO)

---

## FPAR_PARAM_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PARAM_ESTAB | NUMBER | N |  |  |
| 2 | ID_PARAMETROS | NUMBER | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |

**PK**: ID_PARAM_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- ID_PARAMETROS → FPAR_PARAMETROS(ID_PARAMETROS)

**Indexes**:
- IX_FPAR_PARAM_ESTAB (UNIQUE): (ID_PARAMETROS, COD_EMPRESA, COD_ESTAB)

---

## FPM_GO_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ITEM | NUMBER | N |  |  |
| 2 | DESCRICAO | VARCHAR2(300) | Y |  |  |
| 3 | STATUS | CHAR(1) | Y |  |  |
| 4 | COD_GRUPO | VARCHAR2(2) | Y |  |  |
| 5 | SINAL | CHAR(1) | Y |  |  |
| 6 | DSC_ITEM | VARCHAR2(5) | N | ' ' |  |

**PK**: COD_ITEM

---

## FPM_GO_VALOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | COD_ITEM | NUMBER | N |  |  |
| 5 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | IND_DIG_CALC | VARCHAR2(1) | Y |  |  |
| 9 | IND_TP_APURACAO | VARCHAR2(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_ITEM, IND_TP_APURACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_ITEM → FPM_GO_ITEM(COD_ITEM)

---

## FRT_HELP_TAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOM_MODULO | VARCHAR2(9) | N |  |  |
| 2 | NOM_TAB | VARCHAR2(20) | N |  |  |
| 3 | NOM_CAMPO | VARCHAR2(20) | N |  |  |
| 4 | SEQ_DSC | NUMBER(3) | N |  |  |
| 5 | DSC_TAB_CAMPO | VARCHAR2(60) | Y |  |  |
| 6 | DAT_ATUALIZ | DATE | Y |  |  |

**PK**: NOM_MODULO, NOM_TAB, NOM_CAMPO, SEQ_DSC

---

## FRT_PROCESSO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | SP_NOME | VARCHAR2(30) | Y |  |  |
| 3 | VERSAO | VARCHAR2(30) | Y |  |  |
| 4 | DATA_INICIO | DATE | Y |  |  |
| 5 | DATA_FIM | DATE | Y |  |  |
| 6 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 7 | SITUACAO | VARCHAR2(30) | Y |  |  |
| 8 | TIPO | VARCHAR2(30) | Y |  |  |
| 9 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 10 | DESCRICAO | VARCHAR2(300) | Y |  |  |
| 11 | IND_PROG | CHAR(1) | Y |  |  |
| 12 | PROC_ID_ORIG | NUMBER | Y |  |  |
| 13 | NUM_JOB | NUMBER | Y |  |  |
| 14 | APLICACAO | VARCHAR2(100) | Y |  |  |
| 15 | ID_CPROC | NUMBER(12) | Y |  |  |
| 16 | DATA_FILA_INIC | DATE | Y |  |  |
| 17 | DATA_FILA_FIM | DATE | Y |  |  |
| 18 | PROC_ID_TEMP | NUMBER | Y |  |  |

**PK**: PROC_ID

---

## FRT_PROC_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROCSAIDA_ID | NUMBER | N |  |  |
| 2 | PROC_ID | NUMBER | Y |  |  |
| 3 | PAG | NUMBER(15) | Y |  |  |
| 4 | LINHA | NUMBER(15) | Y |  |  |
| 5 | TEXTO | VARCHAR2(4000) | Y |  |  |
| 6 | TIPO | NUMBER | Y |  |  |
| 7 | CHAVE_ORDENACAO | VARCHAR2(500) | Y |  |  |
| 8 | DSC_PARTICAO | VARCHAR2(50) | Y |  |  |

**PK**: PROCSAIDA_ID

**FKs**:
- PROC_ID → FRT_PROCESSO(PROC_ID)

---

## GI_ICMS_ENTRADA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMSS_PET_ENER | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMSS_OUTRO | NUMBER(17,2) | Y |  |  |
| 11 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 13 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 14 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 15 | VLR_USO_CONSUMO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ATIVO_IMOB | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_GI_ICMS_ENTRADA: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, INSC_ESTADUAL)

---

## GI_ICMS_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | VLR_CONT_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CONT_CONTR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_NAO_CONTR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_CONTR | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 12 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 14 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 15 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_GI_ICMS_SAIDA: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, INSC_ESTADUAL)

---

## GP_DE_PARA_EMP_T1_SAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMP_T1 | VARCHAR2(3) | N |  | Código da empresa T1 |
| 2 | COD_EMP_ERP | VARCHAR2(10) | N |  | Código da empresa no ERP |
| 3 | NUM_PROCESSO | NUMBER(12) | Y |  | Número do processo |
| 4 | IND_GRAVACAO | CHAR(1) | Y |  | Indicador de gravação |

**PK**: COD_EMP_T1, COD_EMP_ERP

---

## GP_REGRA_IMPOSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | REGRA_IMPOSTO | VARCHAR2(100) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(800) | Y |  |  |
| 3 | GRUPO_IMPOSTO | VARCHAR2(30) | Y |  |  |
| 4 | NUM_REGRA | VARCHAR2(2) | Y |  |  |

**PK**: REGRA_IMPOSTO

---

## GP_TC_PARAM_UF_IMPOSTO_DOOTAX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UF_FAVORECIDA | VARCHAR2(10) | N |  |  |
| 2 | COD_ARRECADACAO | VARCHAR2(20) | N |  |  |
| 3 | COD_RECEITA | NUMBER(20) | N |  |  |
| 4 | DET_RECEITA | NUMBER(20) | Y |  |  |

**Indexes**:
- UK_GP_TC_PARAM_UF_IMPOSTO_DOOTAX (UNIQUE): (UF_FAVORECIDA, COD_ARRECADACAO, COD_RECEITA, DET_RECEITA)

---

## GRUPO_DADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | NOME | VARCHAR2(30) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(70) | N |  |  |

**PK**: ID

---

## GRUPO_DADOS_COLUNA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | NOME | VARCHAR2(30) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(70) | N |  |  |
| 4 | IND_FILTRO | NUMBER(1) | N |  |  |
| 5 | IND_TOTALIZACAO | NUMBER(1) | N |  |  |
| 6 | IND_AGRUPAMENTO | NUMBER(1) | N |  |  |
| 7 | IND_ORDENACAO | NUMBER(1) | N |  |  |
| 8 | TIPO_DADO_COLUNA | VARCHAR2(1) | N |  |  |
| 9 | TAMANHO_COLUNA | NUMBER(3) | Y |  |  |
| 10 | ID_GRUPO_DADOS | NUMBER(38) | N |  |  |

**PK**: ID

**FKs**:
- ID_GRUPO_DADOS → GRUPO_DADOS(ID)

---

## GRUPO_DIC_DADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO | VARCHAR2(5) | N |  |  |
| 2 | DSC_GRUPO | VARCHAR2(100) | Y |  |  |
| 3 | INF_COMPL | VARCHAR2(4000) | Y |  |  |

**PK**: COD_GRUPO

---

## GRUPO_EMPRESA_MAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_GRUPO | VARCHAR2(40) | Y |  |  |

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

**Indexes**:
- IDX_CHN_GRP_EMP (UNIQUE): (COD_EMPRESA, COD_GRUPO)

---

## GRUPO_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_ESTAB | VARCHAR2(9) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: GRUPO_ESTAB

---

## GRUPO_ESTAB_MAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_GRUPO | VARCHAR2(40) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IDX_CHN_GRP_ETB (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_GRUPO)

---

## GRUPO_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRUPO_PROD | NUMBER(12) | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 3 | COD_GRUPO_PROD | VARCHAR2(5) | Y |  |  |
| 4 | VALID_GRUPO_PROD | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IND_EXC_LIVRO | CHAR(1) | Y |  |  |

**PK**: IDENT_GRUPO_PROD

**FKs**:
- GRUPO_PRODUTO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_GRUPO_PRODUTO (UNIQUE): (GRUPO_PRODUTO, COD_GRUPO_PROD, VALID_GRUPO_PROD)

---

## GRUPO_SELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO_SELO | NUMBER(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_GRUPO_SELO

---

## GTIP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GTIP_GRUPO | CHAR(4) | N |  |  |
| 2 | GTIP_DESC1 | VARCHAR2(500) | Y |  |  |

**PK**: GTIP_GRUPO

---

## GUIA_GNR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_GUIA_RECOL | VARCHAR2(12) | N |  |  |
| 6 | SIGLA_UF | VARCHAR2(2) | N |  |  |
| 7 | DAT_GUIA_RECOL | DATE | Y |  |  |
| 8 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 9 | DAT_ENTREGA | DATE | Y |  |  |
| 10 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 11 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL, SIGLA_UF

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)

---

## GUIA_PAGAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | PERIODO | DATE | N |  |  |
| 5 | NUM_GUIA_PAG | VARCHAR2(30) | N |  |  |
| 6 | DAT_GUIA_PAG | DATE | N |  |  |
| 7 | COD_ARRECADACAO | VARCHAR2(20) | N |  |  |
| 8 | COD_RECEITA | NUMBER(20) | N |  |  |
| 9 | DET_RECEITA | NUMBER(20) | N |  |  |
| 10 | NUM_DOC_ORIGEM | VARCHAR2(20) | N |  |  |
| 11 | SERIE | VARCHAR2(3) | N |  |  |
| 12 | UF_FAVORECIDA | VARCHAR2(2) | N |  |  |
| 13 | CNPJ_FAVORECIDO | VARCHAR2(14) | N |  |  |
| 14 | IE_FAVORECIDA | VARCHAR2(30) | Y |  |  |
| 15 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 16 | DATA_VENCIMENTO | DATE | Y |  |  |
| 17 | DATA_PAGAMENTO | DATE | Y |  |  |
| 18 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 20 | INFO_COMPLEMENTAR | VARCHAR2(300) | Y |  |  |
| 21 | VLR_FECP | NUMBER(17,2) | Y |  |  |
| 22 | VLR_FECP_MULTA | NUMBER(17,2) | Y |  |  |
| 23 | VLR_FECP_JUROS | NUMBER(17,2) | Y |  |  |
| 24 | CONVENIO | VARCHAR2(50) | N |  |  |
| 25 | COD_PRODUTO | VARCHAR2(5) | N |  |  |
| 26 | CHAVE_DFE | VARCHAR2(44) | Y |  |  |
| 27 | CAD_PART | VARCHAR2(14) | Y |  |  |
| 28 | COD_MUN_FAVORECIDO | NUMBER(7) | N |  |  |
| 29 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 31 | CAMPOS_EXTRAS | VARCHAR2(500) | Y |  |  |
| 32 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 33 | GRUPO_IMPOSTO | VARCHAR2(30) | Y |  |  |
| 34 | USUARIO | VARCHAR2(100) | Y |  |  |
| 35 | DATA_LOG | VARCHAR2(20) | Y |  |  |
| 36 | STATUS | VARCHAR2(30) | Y |  |  |
| 37 | COD_PARTICIPANTE | VARCHAR2(60) | Y | null |  |
| 38 | DATA_VALID | DATE | Y | null |  |
| 39 | CNPJ | NUMBER(14) | Y | null |  |
| 40 | CPF | NUMBER(11) | Y | null |  |
| 41 | ID_ESTRANGEIRO | VARCHAR2(20) | Y | null |  |
| 42 | RAZAO_SOCIAL | VARCHAR2(255) | Y | null |  |
| 43 | NOME_FANTASIA | VARCHAR2(255) | Y | null |  |
| 44 | ENDERECO | VARCHAR2(60) | Y | null |  |
| 45 | NUMERO | VARCHAR2(10) | Y | null |  |
| 46 | COMPLEMENTO | VARCHAR2(60) | Y | null |  |
| 47 | BAIRRO | VARCHAR2(60) | Y | null |  |
| 48 | CEP | NUMBER(8) | Y | null |  |
| 49 | COD_MUNICIPIO | NUMBER(7) | Y | null |  |
| 50 | UF | VARCHAR2(2) | Y | null |  |
| 51 | COD_PAIS | NUMBER(5) | Y | null |  |
| 52 | DDD | NUMBER(2) | Y | null |  |
| 53 | TELEFONE | NUMBER(9) | Y | null |  |
| 54 | EMAIL | VARCHAR2(60) | Y | null |  |
| 55 | INSC_ESTADUAL | VARCHAR2(14) | Y | null |  |
| 56 | INSC_MUNICIPAL | VARCHAR2(15) | Y | null |  |
| 57 | SUFRAMA | VARCHAR2(9) | Y | null |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, PERIODO, NUM_GUIA_PAG, DAT_GUIA_PAG, COD_ARRECADACAO, COD_RECEITA, DET_RECEITA, NUM_DOC_ORIGEM, SERIE, UF_FAVORECIDA, CNPJ_FAVORECIDO, CONVENIO, COD_PRODUTO, COD_MUN_FAVORECIDO

---

## GUIA_PAGAMENTO_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(8) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO | DATE | N |  |  |
| 4 | ID_GUIA | NUMBER(38) | Y |  |  |
| 5 | ID_TITULO | NUMBER(38) | Y |  |  |
| 6 | CNPJ_EMPRESA | VARCHAR2(14) | N |  |  |
| 7 | INSC_SUBSTITUTA | VARCHAR2(30) | Y |  |  |
| 8 | TIPO_INSC_SUBSTITUTA | VARCHAR2(300) | Y |  |  |
| 9 | TIPO_PAGTO | VARCHAR2(4000) | Y |  |  |
| 10 | COD_RECEITA | NUMBER(20) | N |  |  |
| 11 | DET_RECEITA | NUMBER(20) | N |  |  |
| 12 | GRUPO_IMPOSTO | VARCHAR2(30) | N |  |  |
| 13 | UF_FAVORECIDA | VARCHAR2(2) | Y |  |  |
| 14 | COD_DOC | NUMBER(38) | Y |  |  |
| 15 | NUM_DOC_ORIGEM | VARCHAR2(20) | N |  |  |
| 16 | SERIE | VARCHAR2(3) | Y |  |  |
| 17 | CHAVE_NF | VARCHAR2(44) | Y |  |  |
| 18 | IND_CANCELAMENTO | VARCHAR2(1) | Y |  |  |
| 19 | INFO_CANCELAMENTO | VARCHAR2(4000) | Y |  |  |
| 20 | STATUS | NUMBER(38) | N |  |  |
| 21 | DSC_STATUS | VARCHAR2(4000) | Y |  |  |
| 22 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 23 | VLR_FECP | NUMBER(17,2) | Y |  |  |
| 24 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ATUAL_MONETARIA | NUMBER(17,2) | Y |  |  |
| 27 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_FECP_JUROS | NUMBER(17,2) | Y |  |  |
| 29 | VLR_MULTA_FECP | NUMBER(17,2) | Y |  |  |
| 30 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 31 | COD_PRODUTO | NUMBER(5) | Y |  |  |
| 32 | CONVENIO | VARCHAR2(50) | Y |  |  |
| 33 | CNPJ_FAVORECIDO | VARCHAR2(14) | Y |  |  |
| 34 | INSC_ESTADUAL_FAVORECIDO | VARCHAR2(30) | Y |  |  |
| 35 | CPF_FAVORECIDO | VARCHAR2(14) | Y |  |  |
| 36 | INFO_COMPL_DOCUMENTO | VARCHAR2(4000) | Y |  |  |
| 37 | IND_ERRO | VARCHAR2(1) | Y |  |  |
| 38 | MENSAGEM_ERRO | VARCHAR2(4000) | Y |  |  |
| 39 | DATA_VENCTO | DATE | Y |  |  |
| 40 | DATA_VENCTO_ORIGINAL | DATE | Y |  |  |
| 41 | COD_BARRAS | VARCHAR2(4000) | Y |  |  |
| 42 | NUM_CONTROLE | VARCHAR2(4000) | Y |  |  |
| 43 | DATA_SEFAZ | DATE | Y |  |  |
| 44 | ID_PAGTO | NUMBER(38) | Y |  |  |
| 45 | DATA_PAGTO | DATE | Y |  |  |
| 46 | NUM_AUTENTICACAO | VARCHAR2(4000) | Y |  |  |
| 47 | ID_PAGADOR | NUMBER(38) | Y |  |  |
| 48 | CNPJ_PAGADOR | VARCHAR2(14) | Y |  |  |
| 49 | COD_BANCO | NUMBER(3) | Y |  |  |
| 50 | AGENCIA | NUMBER(5) | Y |  |  |
| 51 | DIG_AGENCIA | NUMBER(2) | Y |  |  |
| 52 | CONTA_CORRENTE | NUMBER(15) | Y |  |  |
| 53 | DIG_CONTA_CORRENTE | NUMBER(2) | Y |  |  |
| 54 | REGRA_PAGAMENTO | VARCHAR2(4000) | Y |  |  |
| 55 | PDF_GUIA | VARCHAR2(4000) | Y |  |  |
| 56 | CAMPO_EXTRA | VARCHAR2(4000) | Y |  |  |
| 57 | QR_CODE_PIX | VARCHAR2(4000) | Y |  |  |
| 58 | LOGIN_USUARIO | VARCHAR2(4000) | Y |  |  |
| 59 | DAT_DEBITO | DATE | Y |  |  |
| 60 | TOTAL_ELEMENTOS | NUMBER(38) | Y |  |  |
| 61 | TOTAL_PAGINAS | NUMBER(38) | Y |  |  |
| 62 | TAMANHO | NUMBER(38) | Y |  |  |
| 63 | NUMERO | NUMBER(38) | Y |  |  |
| 64 | NUMERO_ELEMENTOS | NUMBER(38) | Y |  |  |
| 65 | ULTIMO | NUMBER(38) | Y |  |  |
| 66 | PRIMEIRO | NUMBER(38) | Y |  |  |
| 67 | ORDENACAO | NUMBER(38) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO, COD_RECEITA, DET_RECEITA, GRUPO_IMPOSTO, NUM_DOC_ORIGEM, STATUS

---

## GUIA_RECOLHIMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_GUIA_RECOL | VARCHAR2(30) | N |  |  |
| 6 | DAT_GUIA_RECOL | DATE | Y |  |  |
| 7 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 8 | DAT_ENTREGA | DATE | Y |  |  |
| 9 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 10 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |
| 11 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 12 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 13 | IND_SJ | CHAR(1) | Y |  |  |
| 14 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 15 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 16 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 17 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 18 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 19 | DSC_COMPLEMENTAR | VARCHAR2(100) | Y |  |  |
| 20 | DAT_VENCTO | DATE | Y |  |  |
| 21 | MES_ANO_REF | DATE | Y |  |  |
| 22 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 23 | IND_GUIA_CONV | CHAR(1) | Y |  |  |
| 24 | IDENT_ESTADO_CONV | NUMBER(12) | Y |  |  |
| 25 | IND_TIPO_DOC_ARREC | CHAR(1) | Y |  |  |
| 26 | NUM_AUTENTIC | VARCHAR2(25) | Y |  |  |
| 27 | VAL_DOC_ORIG | NUMBER(17,2) | Y |  |  |
| 28 | VAL_DESCONTO | NUMBER(17,2) | Y |  |  |
| 29 | VAL_MULTA_MORA | NUMBER(17,2) | Y |  |  |
| 30 | VAL_JUROS | NUMBER(17,2) | Y |  |  |
| 31 | VAL_MULTA | NUMBER(17,2) | Y |  |  |
| 32 | IDENT_ESTADO_CLASSE | NUMBER(12) | Y |  |  |
| 33 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 34 | COD_DEB_ICMS | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)
- COD_DEB_ICMS → ICT_COD_DEB_ICMS(COD_DEB_ICMS)

---

## GUIA_RECOL_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | NUM_GUIA_RECOL | VARCHAR2(25) | N |  |  |
| 7 | DAT_GUIA_RECOL | DATE | Y |  |  |
| 8 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 9 | DAT_ENTREGA | DATE | Y |  |  |
| 10 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 11 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |
| 12 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | IND_SJ | CHAR(1) | Y |  |  |
| 15 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 16 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 17 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 18 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 19 | DSC_COMPLEMENTAR | VARCHAR2(100) | Y |  |  |
| 20 | DAT_VENCTO | DATE | Y |  |  |
| 21 | MES_ANO_REF | DATE | Y |  |  |
| 22 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 23 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

---

## GUIA_REC_FRETES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_GUIA_RECOL | VARCHAR2(25) | N |  |  |
| 6 | DAT_GUIA_RECOL | DATE | Y |  |  |
| 7 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 8 | DAT_ENTREGA | DATE | Y |  |  |
| 9 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 10 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |
| 11 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 12 | IDENT_ESTADO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## GUIA_REC_SUBST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | NUM_GUIA_RECOL | VARCHAR2(25) | N |  |  |
| 6 | DAT_GUIA_RECOL | DATE | Y |  |  |
| 7 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 8 | DAT_ENTREGA | DATE | Y |  |  |
| 9 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 10 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |
| 11 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 12 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 13 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 14 | ORIGEM_PROC | VARCHAR2(1) | Y |  |  |
| 15 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 16 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 17 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 18 | DAT_VENCTO | DATE | Y |  |  |
| 19 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |
| 20 | MES_ANO_REF | DATE | Y |  |  |
| 21 | IND_TIPO_DOC_ARREC | CHAR(1) | Y |  |  |
| 22 | NUM_AUTENTIC | VARCHAR2(25) | Y |  |  |
| 23 | VAL_DOC_ORIG | NUMBER(17,2) | Y |  |  |
| 24 | VAL_DESCONTO | NUMBER(17,2) | Y |  |  |
| 25 | VAL_MULTA_MORA | NUMBER(17,2) | Y |  |  |
| 26 | VAL_JUROS | NUMBER(17,2) | Y |  |  |
| 27 | VAL_MULTA | NUMBER(17,2) | Y |  |  |
| 28 | IDENT_ESTADO_CLASSE | NUMBER(12) | Y |  |  |
| 29 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 30 | COD_DEB_ICMS | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)
- COD_DEB_ICMS → ICT_COD_DEB_ICMS(COD_DEB_ICMS)

---

## GUIA_REC_SUBST_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | NUM_GUIA_RECOL | VARCHAR2(25) | N |  |  |
| 7 | DAT_GUIA_RECOL | DATE | Y |  |  |
| 8 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 9 | DAT_ENTREGA | DATE | Y |  |  |
| 10 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 11 | IDENT_ORG_ARRECAD | NUMBER(12) | Y |  |  |
| 12 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 15 | ORIGEM_PROC | VARCHAR2(1) | Y |  |  |
| 16 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 17 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 18 | DAT_VENCTO | DATE | Y |  |  |
| 19 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |
| 20 | MES_ANO_REF | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_APUR_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)
- IDENT_ORG_ARRECAD → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)

---

## HISTORICO_RETENCAO_IRRF

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
| 11 | SEQUENCIAL | NUMBER(12) | N |  |  |
| 12 | DATA_ALTERACAO | DATE | Y |  |  |
| 13 | DADO_ANTIGO | VARCHAR2(500) | Y |  |  |
| 14 | DADO_NOVO | VARCHAR2(500) | Y |  |  |
| 15 | DSC_MOTIVO | VARCHAR2(100) | Y |  |  |
| 16 | COD_USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF → X53_RETENCAO_IRRF(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF)

---

## HIST_COMP_RETENCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CPF_CGC | VARCHAR2(14) | N |  |  |
| 4 | MES_CALENDARIO | NUMBER(2) | N |  | 1-12 = mensal, 0 = anual |
| 5 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 6 | DAT_ENVIO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CPF_CGC, MES_CALENDARIO, ANO_CALENDARIO

---

## HIST_EXPORT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 3 | NUMERO_ARQUIVO | NUMBER(3) | N |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 5 | QTD_REG_EXP | NUMBER(12) | Y |  |  |
| 6 | DAT_FIM_PROCESSO | DATE | Y |  |  |
| 7 | STATUS | NUMBER(1) | Y |  |  |
| 8 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 9 | COD_ESTAB | VARCHAR2(6) | Y |  |  |

**PK**: NUM_JOB, GRUPO_ARQUIVO, NUMERO_ARQUIVO, NUM_PROCESSO

**FKs**:
- NUM_JOB, GRUPO_ARQUIVO, NUMERO_ARQUIVO → JOB_EXP_TAB(NUM_JOB, GRUPO_ARQUIVO, NUMERO_ARQUIVO)

---

## HIST_INFORME_RENDIMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_FUNC_CLIENTE | CHAR(1) | N |  |  |
| 4 | COD_FUNC_CLIENTE | VARCHAR2(14) | N |  |  |
| 5 | CPF_CGC | VARCHAR2(14) | N |  |  |
| 6 | ANO_CALEND | NUMBER(4) | N |  |  |
| 7 | DAT_ENVIO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_FUNC_CLIENTE, COD_FUNC_CLIENTE, CPF_CGC, ANO_CALEND

---

## HIST_X750_REDARF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | IDENT_DARF | NUMBER(12) | N |  |  |
| 5 | NRO_REFERENCIA | VARCHAR2(15) | N |  |  |
| 6 | DATA_REDARF | DATE | N |  |  |
| 7 | COD_SOLICITA | VARCHAR2(2) | Y |  |  |
| 8 | MOTIVO | VARCHAR2(200) | Y |  |  |
| 9 | DATA_ARREC | DATE | Y |  |  |
| 10 | VLR_TOT_DARF | NUMBER(17,2) | Y |  |  |
| 11 | NRO_BANCO | NUMBER(3) | Y |  |  |
| 12 | NRO_AGENCIA | NUMBER(5) | Y |  |  |
| 13 | PERIODO_APUR | DATE | Y |  |  |
| 14 | DATA_APUR_REDARF | DATE | Y |  |  |
| 15 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 16 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 17 | NUM_REF_DARF | VARCHAR2(17) | Y |  |  |
| 18 | DATA_VENCTO | DATE | Y |  |  |
| 19 | VLR_PRINC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 21 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |
| 23 | NUM_QUOTA | NUMBER(2) | N |  |  |
| 24 | NUM_QUOTA_DARF | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA, DATA_REDARF

---

## HIST_X75_DCTF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | IDENT_DARF | NUMBER(12) | N |  |  |
| 5 | NRO_REFERENCIA | VARCHAR2(15) | N |  |  |
| 6 | DT_INI_APURACAO | DATE | Y |  |  |
| 7 | VLR_REC_ACUMUL | NUMBER(17,2) | Y |  |  |
| 8 | DATA_VENCTO | DATE | Y |  |  |
| 9 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 13 | DATA_PAGTO | DATE | Y |  |  |
| 14 | NRO_PROCESSO_ADM | VARCHAR2(24) | Y |  |  |
| 15 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 16 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 17 | OBSERVACAO | VARCHAR2(180) | Y |  |  |
| 18 | NRO_BANCO | NUMBER(3) | Y |  |  |
| 19 | NRO_AGENCIA | NUMBER(5) | Y |  |  |
| 20 | NRO_PAGTO | VARCHAR2(14) | Y |  |  |
| 21 | SIT_PROCESSO | VARCHAR2(6) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 24 | DATA_ENV_BCO | DATE | Y |  |  |
| 25 | AUTENT_BANCARIA | VARCHAR2(50) | Y |  |  |
| 26 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 27 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 28 | SITUACAO | CHAR(1) | Y |  |  |
| 29 | STATUS | CHAR(1) | Y |  |  |
| 30 | NUM_REF_DARF | VARCHAR2(17) | Y |  |  |
| 31 | IND_POR_EMPRESA | CHAR(1) | Y |  |  |
| 32 | NUM_QUOTA | NUMBER(2) | N |  |  |
| 33 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA

---

## IBT_CONTROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TABELA | VARCHAR2(8) | N |  |  |
| 5 | DSC_DIRETORIO | VARCHAR2(500) | Y |  |  |
| 6 | DT_ULT_IMP_OK | DATE | Y |  |  |
| 7 | IND_UTILIZA_TAB | CHAR(1) | Y |  |  |
| 8 | IND_DROP_TAB | CHAR(1) | Y |  |  |
| 9 | IND_SOBREPOR_REG | CHAR(1) | Y |  |  |
| 10 | IND_LOG_PROD | CHAR(1) | Y |  |  |
| 11 | IND_VALIDADE_X2013 | CHAR(1) | Y |  |  |
| 12 | IND_DATA_AVERB_X48 | CHAR(1) | Y |  |  |
| 13 | IND_GERA_X530 | CHAR(1) | Y |  |  |
| 14 | IND_GERA_X751 | CHAR(1) | Y |  |  |
| 15 | IND_VALID_CEP_X04 | CHAR(1) | Y |  |  |
| 16 | IND_XPRS_LOAD | CHAR(1) | Y |  |  |
| 17 | GRUPO_X188 | VARCHAR2(9) | Y |  |  |
| 18 | GRUPO_X189 | VARCHAR2(9) | Y |  |  |

**PK**: COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TABELA

---

## IBT_GER_IMP_GR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CONF | NUMBER(4) | N |  |  |
| 4 | MES_CONF | NUMBER(2) | N |  |  |
| 5 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 6 | DAT_CONF | DATE | Y |  |  |
| 7 | IND_STAT_CONF | CHAR(1) | Y |  |  |
| 8 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CONF, MES_CONF, GRUPO_ARQUIVO

---

## IBT_GER_IMP_TAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CONF | NUMBER(4) | N |  |  |
| 4 | MES_CONF | NUMBER(2) | N |  |  |
| 5 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 6 | NOME_TABELA | VARCHAR2(18) | N |  |  |
| 7 | NUM_PROC | NUMBER(12) | N |  |  |
| 8 | DAT_INI | DATE | Y |  |  |
| 9 | DAT_FIM | DATE | Y |  |  |
| 10 | DAT_EXEC | DATE | Y |  |  |
| 11 | QTD_REG | NUMBER(12) | Y |  |  |
| 12 | QTD_ERR | NUMBER(12) | Y |  |  |
| 13 | DAT_CONF | DATE | Y |  |  |
| 14 | IND_STATUS_ERR | CHAR(1) | Y |  |  |
| 15 | IND_STAT_CONF | CHAR(1) | Y |  |  |
| 16 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CONF, MES_CONF, GRUPO_ARQUIVO, NOME_TABELA, NUM_PROC

---

## IBT_GRP_VALID

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_VALID | NUMBER(4) | N |  |  |
| 4 | MES_VALID | NUMBER(2) | N |  |  |
| 5 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 6 | DAT_CONF | DATE | Y |  |  |
| 7 | IND_STATUS | CHAR(1) | Y |  |  |
| 8 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_VALID, MES_VALID, GRUPO_ARQUIVO

---

## IBT_HISTORICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TABELA | VARCHAR2(8) | N |  |  |
| 5 | DT_ARQUIVO | DATE | N |  |  |
| 6 | DT_IMPORT | DATE | N |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 8 | STATUS | NUMBER(2) | Y |  |  |

**PK**: COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TABELA, DT_ARQUIVO, DT_IMPORT, NUM_PROCESSO

---

## IBT_MASC_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MASC_IMP | VARCHAR2(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## IBT_PROG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | DSC_PROG | VARCHAR2(50) | Y |  |  |
| 4 | DSC_EXT_ARQ | VARCHAR2(3) | Y |  |  |
| 5 | IND_PERIOD | CHAR(1) | Y |  |  |
| 6 | DT_INI_EVENT | DATE | Y |  |  |
| 7 | DSC_DIRETORIO | VARCHAR2(500) | Y |  |  |
| 8 | COD_PROG_SEMANAL | VARCHAR2(7) | Y |  |  |
| 9 | COD_PROG_MENSAL | VARCHAR2(64) | Y |  |  |
| 10 | IND_LIM_PER | CHAR(1) | Y | 'N' |  |
| 11 | IND_ORD_IMP | CHAR(1) | Y | '1' |  |
| 12 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o job da importação batch vai ser processado via funcionalidade do ATO COTEPE |
| 13 | IND_LOG_X2013 | CHAR(1) | Y |  |  |
| 14 | DSC_ARQ_CONFIG | VARCHAR2(100) | Y |  |  |
| 15 | IND_DATA_AVERB_X48 | CHAR(1) | Y |  |  |
| 16 | IND_MULTI_EMPRESA | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_PROG

---

## IBT_TAB_VALID

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_VALID | NUMBER(4) | N |  |  |
| 4 | MES_VALID | NUMBER(2) | N |  |  |
| 5 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 6 | NOME_TABELA | VARCHAR2(18) | N |  |  |
| 7 | DAT_CONF | DATE | Y |  |  |
| 8 | IND_STATUS | CHAR(1) | Y |  |  |
| 9 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_VALID, MES_VALID, GRUPO_ARQUIVO, NOME_TABELA

---

## ICA_PARAM_GER_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROC_GER | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TP_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | IND_TP_APURAC | CHAR(1) | N |  |  |
| 6 | DAT_INI | DATE | Y |  |  |
| 7 | DAT_FIM | DATE | Y |  |  |
| 8 | IND_TERMO | CHAR(1) | Y |  |  |
| 9 | IND_ENFEIXAMENTO | CHAR(1) | Y |  |  |
| 10 | COD_PERIODICIDADE | VARCHAR2(2) | Y |  |  |
| 11 | NUM_MAX_OSCILACAO | NUMBER(3) | Y |  |  |
| 12 | NUM_PROC_ESTAB | NUMBER(12) | Y |  |  |
| 13 | IND_RESUMO_CFOP | CHAR(1) | Y |  |  |
| 14 | IND_GERA_EMITENTE | CHAR(1) | Y |  |  |
| 15 | IND_GERA_REMETENTE | CHAR(1) | Y |  |  |
| 16 | NUM_MESES | NUMBER(3) | Y |  |  |
| 17 | IND_INICIAR | CHAR(1) | Y |  |  |
| 18 | NUM_MAX_CONT | NUMBER(7) | Y |  |  |
| 19 | NUM_LIVRO_INI | NUMBER(10) | Y |  |  |
| 20 | NUM_PAGINA_INI | NUMBER(10) | Y |  |  |
| 21 | VLR_DESLOC_INI | NUMBER(10) | Y |  |  |
| 22 | NUM_LIVRO_USU | NUMBER(10) | Y |  |  |
| 23 | NUM_PAGINA_USU | NUMBER(10) | Y |  |  |
| 24 | VLR_DESLOC_USU | NUMBER(10) | Y |  |  |
| 25 | IND_GI | CHAR(1) | Y |  |  |
| 26 | IND_TP_PROCES | CHAR(1) | Y |  |  |
| 27 | IND_TP_DIF_ALIQ | CHAR(1) | Y |  |  |
| 28 | COD_OPER_1 | VARCHAR2(5) | Y |  |  |
| 29 | DSC_DET_1 | VARCHAR2(250) | Y |  |  |
| 30 | IND_REMOVE_CALC_1 | CHAR(1) | Y |  |  |
| 31 | COD_OPER_2 | VARCHAR2(5) | Y |  |  |
| 32 | DSC_DET_2 | VARCHAR2(250) | Y |  |  |
| 33 | IND_GRAVAR | CHAR(1) | Y |  |  |
| 34 | IND_IMPRIMIR | CHAR(1) | Y |  |  |
| 35 | STATUS_GER_1 | CHAR(1) | Y |  |  |
| 36 | STATUS_GER_2 | CHAR(1) | Y |  |  |
| 37 | STATUS_GRAV | CHAR(1) | Y |  |  |
| 38 | STATUS_IMP | CHAR(1) | Y |  |  |
| 39 | DAT_INVENTARIO | DATE | Y |  |  |
| 40 | DAT_SALDO_ANT | DATE | Y |  |  |
| 41 | NUM_VERSAO | VARCHAR2(4) | Y |  |  |
| 42 | NUM_FOLHAS_LIVROS | NUMBER(6) | Y |  |  |
| 43 | VLR_DESLOC_DESC | NUMBER(6) | Y |  |  |
| 44 | NOM_ARQUIVO | VARCHAR2(8) | Y |  |  |
| 45 | NOM_DIRETORIO | VARCHAR2(100) | Y |  |  |
| 46 | IND_SUBST | CHAR(1) | Y |  |  |
| 47 | IND_RES_ALIQ | VARCHAR2(1) | Y |  |  |
| 48 | IND_OBS_RED_BCALC | VARCHAR2(1) | Y |  |  |
| 49 | IND_NF_SERVICO | VARCHAR2(1) | Y |  |  |
| 50 | IND_UTIL_NF_CANCEL | VARCHAR2(1) | Y |  |  |
| 51 | IND_ICMS_RETIDO | VARCHAR2(1) | Y |  |  |
| 52 | IND_OBS_CAPA | CHAR(1) | Y |  |  |
| 53 | IND_TIPO_APUR | NUMBER(1) | Y |  |  |
| 54 | IND_CFO_NAT | CHAR(1) | Y |  |  |
| 55 | IND_LIVRO_UNICO | CHAR(1) | Y |  |  |
| 56 | IND_RES_TRIB_INT | CHAR(1) | Y |  |  |
| 57 | IND_OBS_DIF_ALIQ | CHAR(1) | Y |  |  |
| 58 | IND_ALIQ_IPI | CHAR(1) | Y |  |  |
| 59 | IND_RES_DEC | CHAR(1) | Y |  |  |
| 60 | IND_RES_QUINZ | CHAR(1) | Y |  |  |
| 61 | COD_CONTA_INI | VARCHAR2(70) | Y |  |  |
| 62 | COD_CONTA_FIM | VARCHAR2(70) | Y |  |  |
| 63 | IND_TIPO_REL | CHAR(1) | Y |  |  |
| 64 | IND_RES_BALANCETE | CHAR(1) | Y |  |  |
| 65 | IND_DEMONSTRATIVO | CHAR(1) | Y |  |  |
| 66 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 67 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 68 | IND_AUTENTIC | CHAR(1) | Y |  |  |
| 69 | IND_CRED_DEB | CHAR(1) | Y |  |  |
| 70 | IND_SUBST_FRETES | CHAR(1) | Y |  |  |
| 71 | STATUS_AUTENTIC | CHAR(1) | Y |  |  |
| 72 | ORDENACAO_IND_P3 | VARCHAR2(15) | Y |  |  |
| 73 | IND_RES_RECEITA | CHAR(1) | Y |  |  |
| 74 | IND_APUR_RESSAR_ST | CHAR(1) | Y |  |  |
| 75 | IND_OBS_UF_CFO | CHAR(1) | Y |  |  |
| 76 | IND_TP_CTA_ESTOQUE | CHAR(1) | Y |  |  |
| 77 | IND_OBS_ST_CR_P1 | CHAR(1) | Y |  |  |
| 78 | IND_OBS_ST_NCR_P1 | CHAR(1) | Y |  |  |
| 79 | IND_OBS_ST_CR_P2 | CHAR(1) | Y |  |  |
| 80 | IND_OBS_ST_NCR_P2 | CHAR(1) | Y |  |  |
| 81 | IND_OBS_DALIQ_P9 | CHAR(1) | Y |  |  |
| 82 | IND_LIVRO_FOLHA | CHAR(1) | Y |  |  |
| 83 | IND_RES_DALIQ_P9 | CHAR(1) | Y |  |  |
| 84 | IND_TP_RES_EMIT | CHAR(1) | Y |  |  |
| 85 | IND_TP_GI | CHAR(1) | Y |  |  |
| 86 | MODELO | CHAR(1) | Y |  |  |
| 87 | USUARIO | VARCHAR2(40) | Y |  |  |
| 88 | IND_OBS_IPI_NCR_P1 | CHAR(1) | Y |  |  |
| 89 | IND_SRF_EQ_IND | CHAR(1) | Y |  |  |
| 90 | IND_RES_PROD | CHAR(1) | Y |  |  |
| 91 | IND_VALORES_IPI | CHAR(1) | Y |  |  |
| 92 | DAT_INI_ST | DATE | Y |  |  |
| 93 | DAT_FIM_ST | DATE | Y |  |  |
| 94 | IND_MATERIAL | CHAR(1) | Y |  |  |
| 95 | IND_ISEN_MUNIC | CHAR(1) | Y |  |  |
| 96 | IND_RES_MUNIC | CHAR(1) | Y |  |  |
| 97 | IND_DED_SUB | CHAR(1) | Y |  |  |
| 98 | IND_OUT_MUNIC | CHAR(1) | Y |  |  |
| 99 | IND_ORDENACAO | CHAR(1) | Y |  |  |
| 100 | IND_GRAVAR_PDF | CHAR(1) | Y |  |  |
| 101 | IND_TP_CABECALHO | CHAR(1) | Y |  |  |
| 102 | IND_RES_CENTR_P9 | CHAR(1) | Y |  |  |
| 103 | IND_PROD_ACAB | CHAR(1) | Y |  |  |
| 104 | IND_PROD_INS | CHAR(1) | Y |  |  |
| 105 | IND_PROD_EMB | CHAR(1) | Y |  |  |
| 106 | IND_PROD_CONS | CHAR(1) | Y |  |  |
| 107 | IND_PROD_OUT | CHAR(1) | Y |  |  |
| 108 | IND_PROD_ELAB | CHAR(1) | Y |  |  |
| 109 | IND_PROD_INTER | CHAR(1) | Y |  |  |
| 110 | IND_PROD_MISC | CHAR(1) | Y |  |  |
| 111 | IND_BASE_INSENTA | CHAR(1) | Y |  |  |
| 112 | IND_OBS_FATUR | CHAR(1) | Y |  |  |
| 113 | IND_DSC_TOT_P9 | CHAR(1) | Y |  |  |
| 114 | IND_AP_ICMS_REC | CHAR(1) | Y |  |  |
| 115 | IND_RES_NF_ST | CHAR(1) | Y |  |  |
| 116 | IND_RES_FINANC | CHAR(1) | Y |  |  |
| 117 | IND_TOT_GERAL | CHAR(1) | Y |  |  |
| 118 | IND_TITULO_LVR | CHAR(1) | Y |  | Indicador de inclusao do titulo, gravado na X2097_MUNIC_ISS, no livro de ISS |
| 119 | IND_REG_ESPEC_LVR | CHAR(1) | Y |  | Indicador de inclusao do regime especial, gravado na X2097_MUNIC_ISS, no livro de ISS |
| 120 | IND_INSC_DF_LVR | CHAR(1) | Y |  | Indicador de Inscricao CF/DF, livros do ISS e ICMS |
| 121 | TITULO_LIVRO | VARCHAR2(100) | Y |  |  |
| 122 | IND_RES_OBS | CHAR(1) | Y |  | Indicador de geração de Resumo de Observação |
| 123 | IND_RES_NATUREZA | CHAR(1) | Y |  |  |
| 124 | IND_ITEM_ZERADO | CHAR(1) | Y |  | Indicador de Exibir Itens Zerados, referente ao parâmetro 63 - Exibir  Itens  Zerados (P7) da ICT_PAR_ICMS_UF |
| 125 | IND_ALMOXARIFADO | CHAR(1) | Y |  | Indicador de Classificar por Almoxarifado, referente ao parâmetro 62 - Classificar por almoxarifado (P7) da ICT_PAR_ICMS_UF |
| 126 | IND_CONSOLIDA_UF | CHAR(1) | Y |  | Indicador de Consolidado por UF, ref ao parâmetro 58 - Consolidado por UF (P2/P2A Consolidado) da ICT_PAR_ICMS_UF |
| 127 | IND_DISCR_DOCFIS | CHAR(1) | Y |  | Indicador de Discriminar Docs e Vlr Contábil p/ CFOP/Conta, ref ao parâmetro 59 - Discrimina Docs e Vlr Contábil por CFOP e Conta (P2/P2A Consolidado) da ICT_PAR_ICMS_UF |
| 128 | IND_EXIBE_COD_CONTABIL | CHAR(1) | Y |  | Indicador de Exibir Codificação Contábil, ref ao parâmetro 60 - Consolidado p/ Codificação Contábil (P2/P2A Consolidado) da ICT_PAR_ICMS_UF |
| 129 | IND_COD_TRIB_NFS | CHAR(1) | Y |  | Indicador de exibição do código de tributação para os casos de itens de serviços em notas mistas ref. ao parâmetro 64. |
| 130 | IND_TRIB_NFS | CHAR(1) | Y |  | Indicador de exibição da tributação para os casos de itens de serviços em notas mistas ref. ao parâmetro 64. |
| 131 | IND_TPDOC_FIND | CHAR(1) | Y |  |  |
| 132 | IND_PRODU_FIND | CHAR(1) | Y |  |  |
| 133 | IND_IMP_S_SLD_S_MOVTO | CHAR(1) | Y | 'N' | S - Não Imprime produto com saldo e sem movimentação (P3 Convênio ICMS) |
| 134 | IND_IMP_C_SLD_S_MOVTO | CHAR(1) | Y | 'N' |  |
| 135 | IND_NAO_RES_APUR | CHAR(1) | Y |  | S - Não gera o item Resumo da Apuração - P9 |
| 136 | IND_RES_APUR_SALDO | CHAR(1) | Y |  |  |
| 137 | IND_DISCR_DOCS_FIS_CFOP_P1_P1A | CHAR(1) | Y | 'N' |  |
| 138 | IND_DISCR_DOCS_FIS_CFOP_P2_P2A | CHAR(1) | Y | 'N' |  |
| 139 | IND_CABECALHO_S_P | CHAR(1) | Y | 'N' | S - Emissão do Livro Modelo P3 agrupado por NCM (Convênio ICMS 57/95)  |
| 140 | IND_P3_POR_NCM | CHAR(1) | Y | 'N' |  |
| 141 | IND_EXIBE_VAL_ZERADOS | CHAR(1) | Y |  | Indicador de Exibicao dos valores zerados na parte principal dos livros fis-cais (nao contempla P9 e P8) |
| 142 | IND_OBS_IPI_NESCR | CHAR(1) | Y |  |  |
| 143 | IND_OBS_LANC_COMPL | CHAR(1) | Y |  | Indicador ref ao parametro 87 - Considerar Observacoes de Informacoes Complementares da Nota (SAFX112) para livros (P1 e P2) da ICT_PAR_ICMS_UF |
| 144 | IND_RES_DALIQ_ORIG_DEST | CHAR(1) | Y | 'N' | Indicador ref ao parametro 91 - Apuracao do ICMS Diferencial de Aliquota UF Origem / Destino |
| 145 | IND_GRAVA_PDF_CSV_T1 | CHAR(1) | Y |  | Indicador para T1 voltado a escolha do output dos resumos(Pdf ou Csv) |

**PK**: NUM_PROC_GER, COD_EMPRESA, COD_ESTAB, COD_TP_LIVRO, IND_TP_APURAC

---

## ICA_PAR_GER_APU_AM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROC_GER | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 5 | COD_TP_LIVRO | VARCHAR2(3) | N |  |  |
| 6 | IND_TP_APURAC | CHAR(1) | N |  |  |
| 7 | DAT_INI | DATE | Y |  |  |
| 8 | DAT_FIM | DATE | Y |  |  |
| 9 | IND_TERMO | CHAR(1) | Y |  |  |
| 10 | IND_ENFEIXAMENTO | CHAR(1) | Y |  |  |
| 11 | COD_PERIODICIDADE | VARCHAR2(2) | Y |  |  |
| 12 | NUM_MAX_OSCILACAO | NUMBER(3) | Y |  |  |
| 13 | NUM_PROC_ESTAB | NUMBER(12) | Y |  |  |
| 14 | IND_RESUMO_CFOP | CHAR(1) | Y |  |  |
| 15 | IND_GERA_EMITENTE | CHAR(1) | Y |  |  |
| 16 | IND_GERA_REMETENTE | CHAR(1) | Y |  |  |
| 17 | NUM_MESES | NUMBER(3) | Y |  |  |
| 18 | IND_INICIAR | CHAR(1) | Y |  |  |
| 19 | NUM_MAX_CONT | NUMBER(7) | Y |  |  |
| 20 | NUM_LIVRO_INI | NUMBER(6) | Y |  |  |
| 21 | NUM_PAGINA_INI | NUMBER(6) | Y |  |  |
| 22 | VLR_DESLOC_INI | NUMBER(6) | Y |  |  |
| 23 | NUM_LIVRO_USU | NUMBER(6) | Y |  |  |
| 24 | NUM_PAGINA_USU | NUMBER(6) | Y |  |  |
| 25 | VLR_DESLOC_USU | NUMBER(6) | Y |  |  |
| 26 | IND_GI | CHAR(1) | Y |  |  |
| 27 | IND_TP_PROCES | CHAR(1) | Y |  |  |
| 28 | IND_TP_DIF_ALIQ | CHAR(1) | Y |  |  |
| 29 | COD_OPER_1 | VARCHAR2(5) | Y |  |  |
| 30 | DSC_DET_1 | VARCHAR2(250) | Y |  |  |
| 31 | IND_REMOVE_CALC_1 | CHAR(1) | Y |  |  |
| 32 | COD_OPER_2 | VARCHAR2(5) | Y |  |  |
| 33 | DSC_DET_2 | VARCHAR2(250) | Y |  |  |
| 34 | IND_GRAVAR | CHAR(1) | Y |  |  |
| 35 | IND_IMPRIMIR | CHAR(1) | Y |  |  |
| 36 | STATUS_GER_1 | CHAR(1) | Y |  |  |
| 37 | STATUS_GER_2 | CHAR(1) | Y |  |  |
| 38 | STATUS_GRAV | CHAR(1) | Y |  |  |
| 39 | STATUS_IMP | CHAR(1) | Y |  |  |
| 40 | DAT_INVENTARIO | DATE | Y |  |  |
| 41 | DAT_SALDO_ANT | DATE | Y |  |  |
| 42 | NUM_VERSAO | VARCHAR2(3) | Y |  |  |
| 43 | NUM_FOLHAS_LIVROS | NUMBER(6) | Y |  |  |
| 44 | VLR_DESLOC_DESC | NUMBER(6) | Y |  |  |
| 45 | NOM_ARQUIVO | VARCHAR2(8) | Y |  |  |
| 46 | NOM_DIRETORIO | VARCHAR2(100) | Y |  |  |
| 47 | IND_SUBST | CHAR(1) | Y |  |  |
| 48 | IND_RES_ALIQ | VARCHAR2(1) | Y |  |  |
| 49 | IND_OBS_RED_BCALC | VARCHAR2(1) | Y |  |  |
| 50 | IND_NF_SERVICO | VARCHAR2(1) | Y |  |  |
| 51 | IND_UTIL_NF_CANCEL | VARCHAR2(1) | Y |  |  |
| 52 | IND_ICMS_RETIDO | VARCHAR2(1) | Y |  |  |
| 53 | IND_OBS_CAPA | CHAR(1) | Y |  |  |
| 54 | IND_TIPO_APUR | NUMBER(1) | Y |  |  |
| 55 | IND_CFO_NAT | CHAR(1) | Y |  |  |
| 56 | IND_LIVRO_UNICO | CHAR(1) | Y |  |  |
| 57 | IND_RES_TRIB_INT | CHAR(1) | Y |  |  |
| 58 | IND_OBS_DIF_ALIQ | CHAR(1) | Y |  |  |
| 59 | IND_ALIQ_IPI | CHAR(1) | Y |  |  |
| 60 | IND_RES_DEC | CHAR(1) | Y |  |  |
| 61 | IND_RES_QUINZ | CHAR(1) | Y |  |  |
| 62 | COD_CONTA_INI | VARCHAR2(70) | Y |  |  |
| 63 | COD_CONTA_FIM | VARCHAR2(70) | Y |  |  |
| 64 | IND_TIPO_REL | CHAR(1) | Y |  |  |
| 65 | IND_RES_BALANCETE | CHAR(1) | Y |  |  |
| 66 | IND_DEMONSTRATIVO | CHAR(1) | Y |  |  |
| 67 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 68 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 69 | IND_AUTENTIC | CHAR(1) | Y |  |  |
| 70 | IND_CRED_DEB | CHAR(1) | Y |  |  |
| 71 | IND_SUBST_FRETES | CHAR(1) | Y |  |  |
| 72 | STATUS_AUTENTIC | CHAR(1) | Y |  |  |
| 73 | ORDENACAO_IND_P3 | VARCHAR2(15) | Y |  |  |
| 74 | IND_RES_RECEITA | CHAR(1) | Y |  |  |
| 75 | IND_APUR_RESSAR_ST | CHAR(1) | Y |  |  |
| 76 | IND_OBS_UF_CFO | CHAR(1) | Y |  |  |
| 77 | IND_TP_CTA_ESTOQUE | CHAR(1) | Y |  |  |
| 78 | IND_OBS_ST_CR_P1 | CHAR(1) | Y |  |  |
| 79 | IND_OBS_ST_NCR_P1 | CHAR(1) | Y |  |  |
| 80 | IND_OBS_ST_CR_P2 | CHAR(1) | Y |  |  |
| 81 | IND_OBS_ST_NCR_P2 | CHAR(1) | Y |  |  |
| 82 | IND_OBS_DALIQ_P9 | CHAR(1) | Y |  |  |
| 83 | IND_LIVRO_FOLHA | CHAR(1) | Y |  |  |
| 84 | IND_RES_DALIQ_P9 | CHAR(1) | Y |  |  |
| 85 | IND_TP_RES_EMIT | CHAR(1) | Y |  |  |
| 86 | IND_TP_GI | CHAR(1) | Y |  |  |
| 87 | MODELO | CHAR(1) | Y |  |  |
| 88 | USUARIO | VARCHAR2(40) | Y |  |  |
| 89 | IND_OBS_IPI_NCR_P1 | CHAR(1) | Y |  |  |
| 90 | IND_RES_PROD | CHAR(1) | Y |  |  |
| 91 | IND_SRF_EQ_IND | CHAR(1) | Y |  |  |
| 92 | IND_VALORES_IPI | CHAR(1) | Y |  |  |
| 93 | DAT_INI_ST | DATE | Y |  |  |
| 94 | DAT_FIM_ST | DATE | Y |  |  |
| 95 | IND_MATERIAL | CHAR(1) | Y |  |  |
| 96 | IND_ISEN_MUNIC | CHAR(1) | Y |  |  |
| 97 | IND_RES_MUNIC | CHAR(1) | Y |  |  |
| 98 | IND_DED_SUB | CHAR(1) | Y |  |  |
| 99 | IND_OUT_MUNIC | CHAR(1) | Y |  |  |
| 100 | IND_ORDENACAO | CHAR(1) | Y |  |  |
| 101 | IND_GRAVAR_PDF | CHAR(1) | Y |  |  |
| 102 | IND_INC_P9_AM | CHAR(1) | Y |  |  |
| 103 | IND_NINC_P9_AM | CHAR(1) | Y |  |  |
| 104 | IND_CONS_P9_AM | CHAR(1) | Y |  |  |
| 105 | IND_TOT_GERAL | CHAR(1) | Y |  |  |
| 106 | IND_TP_CABECALHO | CHAR(1) | Y |  |  |
| 107 | IND_CABECALHO_S_P | CHAR(1) | Y |  |  |
| 108 | IND_RES_DALIQ_ORIG_DEST | CHAR(1) | Y |  | Indicador ref ao parametro 31 - ApuraÃ§Ã£o do ICMS Diferencial de Aliquota UF Origem / Destino |

**PK**: NUM_PROC_GER, COD_EMPRESA, COD_ESTAB, COD_TP_LIVRO, IND_TP_APURAC, INSC_ESTADUAL

---

## ICA_PAR_GER_AP_PRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROC_GER | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TP_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 6 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 7 | IND_TP_APURAC | CHAR(1) | N |  |  |
| 8 | DAT_INI | DATE | Y |  |  |
| 9 | DAT_FIM | DATE | Y |  |  |
| 10 | IND_TERMO | CHAR(1) | Y |  |  |
| 11 | IND_ENFEIXAMENTO | CHAR(1) | Y |  |  |
| 12 | COD_PERIODICIDADE | VARCHAR2(2) | Y |  |  |
| 13 | NUM_MAX_OSCILACAO | NUMBER(3) | Y |  |  |
| 14 | NUM_PROC_ESTAB | NUMBER(12) | Y |  |  |
| 15 | IND_RESUMO_CFOP | CHAR(1) | Y |  |  |
| 16 | IND_GERA_EMITENTE | CHAR(1) | Y |  |  |
| 17 | IND_GERA_REMETENTE | CHAR(1) | Y |  |  |
| 18 | NUM_MESES | NUMBER(3) | Y |  |  |
| 19 | IND_INICIAR | CHAR(1) | Y |  |  |
| 20 | NUM_MAX_CONT | NUMBER(7) | Y |  |  |
| 21 | NUM_LIVRO_INI | NUMBER(6) | Y |  |  |
| 22 | NUM_PAGINA_INI | NUMBER(6) | Y |  |  |
| 23 | VLR_DESLOC_INI | NUMBER(6) | Y |  |  |
| 24 | NUM_LIVRO_USU | NUMBER(6) | Y |  |  |
| 25 | NUM_PAGINA_USU | NUMBER(6) | Y |  |  |
| 26 | VLR_DESLOC_USU | NUMBER(6) | Y |  |  |
| 27 | IND_GI | CHAR(1) | Y |  |  |
| 28 | IND_TP_PROCES | CHAR(1) | Y |  |  |
| 29 | IND_TP_DIF_ALIQ | CHAR(1) | Y |  |  |
| 30 | COD_OPER_1 | VARCHAR2(5) | Y |  |  |
| 31 | DSC_DET_1 | VARCHAR2(250) | Y |  |  |
| 32 | IND_REMOVE_CALC_1 | CHAR(1) | Y |  |  |
| 33 | COD_OPER_2 | VARCHAR2(5) | Y |  |  |
| 34 | DSC_DET_2 | VARCHAR2(250) | Y |  |  |
| 35 | IND_GRAVAR | CHAR(1) | Y |  |  |
| 36 | IND_IMPRIMIR | CHAR(1) | Y |  |  |
| 37 | STATUS_GER_1 | CHAR(1) | Y |  |  |
| 38 | STATUS_GER_2 | CHAR(1) | Y |  |  |
| 39 | STATUS_GRAV | CHAR(1) | Y |  |  |
| 40 | STATUS_IMP | CHAR(1) | Y |  |  |
| 41 | DAT_INVENTARIO | DATE | Y |  |  |
| 42 | DAT_SALDO_ANT | DATE | Y |  |  |
| 43 | NUM_VERSAO | VARCHAR2(3) | Y |  |  |
| 44 | NUM_FOLHAS_LIVROS | NUMBER(6) | Y |  |  |
| 45 | VLR_DESLOC_DESC | NUMBER(6) | Y |  |  |
| 46 | NOM_ARQUIVO | VARCHAR2(8) | Y |  |  |
| 47 | NOM_DIRETORIO | VARCHAR2(100) | Y |  |  |
| 48 | IND_SUBST | CHAR(1) | Y |  |  |
| 49 | IND_RES_ALIQ | VARCHAR2(1) | Y |  |  |
| 50 | IND_OBS_RED_BCALC | VARCHAR2(1) | Y |  |  |
| 51 | IND_NF_SERVICO | VARCHAR2(1) | Y |  |  |
| 52 | IND_UTIL_NF_CANCEL | VARCHAR2(1) | Y |  |  |
| 53 | IND_ICMS_RETIDO | VARCHAR2(1) | Y |  |  |
| 54 | IND_OBS_CAPA | CHAR(1) | Y |  |  |
| 55 | IND_TIPO_APUR | NUMBER(1) | Y |  |  |
| 56 | IND_CFO_NAT | CHAR(1) | Y |  |  |
| 57 | IND_LIVRO_UNICO | CHAR(1) | Y |  |  |
| 58 | IND_RES_TRIB_INT | CHAR(1) | Y |  |  |
| 59 | IND_OBS_DIF_ALIQ | CHAR(1) | Y |  |  |
| 60 | IND_ALIQ_IPI | CHAR(1) | Y |  |  |
| 61 | IND_RES_DEC | CHAR(1) | Y |  |  |
| 62 | IND_RES_QUINZ | CHAR(1) | Y |  |  |
| 63 | COD_CONTA_INI | VARCHAR2(70) | Y |  |  |
| 64 | COD_CONTA_FIM | VARCHAR2(70) | Y |  |  |
| 65 | IND_TIPO_REL | CHAR(1) | Y |  |  |
| 66 | IND_RES_BALANCETE | CHAR(1) | Y |  |  |
| 67 | IND_DEMONSTRATIVO | CHAR(1) | Y |  |  |
| 68 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 69 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 70 | IND_AUTENTIC | CHAR(1) | Y |  |  |
| 71 | IND_CRED_DEB | CHAR(1) | Y |  |  |
| 72 | IND_SUBST_FRETES | CHAR(1) | Y |  |  |
| 73 | STATUS_AUTENTIC | CHAR(1) | Y |  |  |
| 74 | ORDENACAO_IND_P3 | VARCHAR2(15) | Y |  |  |
| 75 | IND_RES_RECEITA | CHAR(1) | Y |  |  |
| 76 | IND_APUR_RESSAR_ST | CHAR(1) | Y |  |  |
| 77 | IND_OBS_UF_CFO | CHAR(1) | Y |  |  |
| 78 | IND_TP_CTA_ESTOQUE | CHAR(1) | Y |  |  |
| 79 | IND_OBS_ST_CR_P1 | CHAR(1) | Y |  |  |
| 80 | IND_OBS_ST_NCR_P1 | CHAR(1) | Y |  |  |
| 81 | IND_OBS_ST_CR_P2 | CHAR(1) | Y |  |  |
| 82 | IND_OBS_ST_NCR_P2 | CHAR(1) | Y |  |  |
| 83 | IND_OBS_DALIQ_P9 | CHAR(1) | Y |  |  |
| 84 | IND_LIVRO_FOLHA | CHAR(1) | Y |  |  |
| 85 | IND_RES_DALIQ_P9 | CHAR(1) | Y |  |  |
| 86 | IND_TP_RES_EMIT | CHAR(1) | Y |  |  |
| 87 | IND_TP_GI | CHAR(1) | Y |  |  |
| 88 | MODELO | CHAR(1) | Y |  |  |
| 89 | USUARIO | VARCHAR2(40) | Y |  |  |
| 90 | IND_OBS_IPI_NCR_P1 | CHAR(1) | Y |  |  |
| 91 | IND_RES_PROD | CHAR(1) | Y |  |  |
| 92 | IND_SRF_EQ_IND | CHAR(1) | Y |  |  |
| 93 | IND_VALORES_IPI | CHAR(1) | Y |  |  |
| 94 | DAT_INI_ST | DATE | Y |  |  |
| 95 | DAT_FIM_ST | DATE | Y |  |  |
| 96 | IND_MATERIAL | CHAR(1) | Y |  |  |
| 97 | IND_ISEN_MUNIC | CHAR(1) | Y |  |  |
| 98 | IND_RES_MUNIC | CHAR(1) | Y |  |  |
| 99 | IND_DED_SUB | CHAR(1) | Y |  |  |
| 100 | IND_OUT_MUNIC | CHAR(1) | Y |  |  |
| 101 | IND_ORDENACAO | CHAR(1) | Y |  |  |
| 102 | IND_GRAVAR_PDF | CHAR(1) | Y |  |  |
| 103 | IND_TP_CABECALHO | CHAR(1) | Y |  |  |
| 104 | IND_RES_CENTR_P9 | CHAR(1) | Y |  |  |
| 105 | IND_PROD_ACAB | CHAR(1) | Y |  |  |
| 106 | IND_PROD_INS | CHAR(1) | Y |  |  |
| 107 | IND_PROD_EMB | CHAR(1) | Y |  |  |
| 108 | IND_PROD_CONS | CHAR(1) | Y |  |  |
| 109 | IND_PROD_OUT | CHAR(1) | Y |  |  |
| 110 | IND_PROD_ELAB | CHAR(1) | Y |  |  |
| 111 | IND_PROD_INTER | CHAR(1) | Y |  |  |
| 112 | IND_PROD_MISC | CHAR(1) | Y |  |  |
| 113 | IND_BASE_INSENTA | CHAR(1) | Y |  |  |
| 114 | IND_DSC_TOT_P9 | CHAR(1) | Y |  |  |
| 115 | IND_OBS_FATUR | CHAR(1) | Y |  |  |
| 116 | IND_AP_ICMS_REC | CHAR(1) | Y |  |  |
| 117 | IND_RES_NF_ST | CHAR(1) | Y |  |  |
| 118 | IND_RES_FINANC | CHAR(1) | Y |  |  |
| 119 | IND_DEM_INCENT | CHAR(1) | Y |  |  |
| 120 | IND_TOT_GERAL | CHAR(1) | Y |  |  |

**PK**: NUM_PROC_GER, COD_EMPRESA, COD_ESTAB, COD_TP_LIVRO, SERIE_LIVRO, SUB_SERIE_LIVRO, IND_TP_APURAC

---

## ICEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MNFEM_SERIE | VARCHAR2(5) | N |  |  |
| 4 | MNFEM_NUM | VARCHAR2(15) | N |  |  |
| 5 | MNFEM_DTEMIS | DATE | N |  |  |
| 6 | CADG_COD | VARCHAR2(16) | N |  |  |
| 7 | CATG_COD | CHAR(2) | N |  |  |
| 8 | CICD_COD_INF | VARCHAR2(9) | N |  |  |
| 9 | MNFEM_DTENTR | DATE | Y |  |  |
| 10 | ICEM_TXT_COMP | VARCHAR2(250) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, MNFEM_SERIE, MNFEM_NUM, MNFEM_DTEMIS, CADG_COD, CATG_COD, CICD_COD_INF

---

## ICP_GIA_ST_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | UF_FAVORECIDA | VARCHAR2(2) | N |  |  |
| 4 | DIA_VENCTO1 | NUMBER(2) | Y |  |  |
| 5 | DIA_VENCTO2 | NUMBER(2) | Y |  |  |
| 6 | DIA_VENCTO3 | NUMBER(2) | Y |  |  |
| 7 | DIA_VENCTO4 | NUMBER(2) | Y |  |  |
| 8 | DIA_VENCTO5 | NUMBER(2) | Y |  |  |
| 9 | DIA_VENCTO6 | NUMBER(2) | Y |  |  |
| 10 | VERSAO | VARCHAR2(2) | Y |  |  |
| 11 | IND_UTIL_APUR_P9 | CHAR(1) | Y |  |  |
| 12 | IND_TOTALIZA_DEDUCAO | CHAR(1) | Y |  |  |
| 13 | IND_EMP_ENERG_ELET | CHAR(1) | Y |  |  |
| 14 | IND_CONSIDERAR_UF | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, UF_FAVORECIDA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICP_INSC_EST_CENTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB_CENTR → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ICP_TP_UTIL_CONV60

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CLASS_ITEM | VARCHAR2(4) | N |  |  |
| 2 | DAT_VALIDADE | DATE | N |  |  |
| 3 | COD_TP_UTIL | VARCHAR2(2) | Y |  |  |

**PK**: COD_CLASS_ITEM, DAT_VALIDADE

---

## ICSM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MNFSM_SERIE | VARCHAR2(5) | N |  |  |
| 4 | MNFSM_NUM | VARCHAR2(15) | N |  |  |
| 5 | MNFSM_DTEMISS | DATE | N |  |  |
| 6 | CICD_COD_INF | VARCHAR2(9) | N |  |  |
| 7 | ICSM_TXT_COMP | VARCHAR2(250) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, MNFSM_SERIE, MNFSM_NUM, MNFSM_DTEMISS, CICD_COD_INF

---

## IDENT_SUBSTITUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOME_TABELA | VARCHAR2(40) | N |  |  |
| 2 | NOME_COLUNA | VARCHAR2(40) | N |  |  |
| 3 | PROX_IDENT_SUBST | NUMBER(12) | Y |  |  |

**PK**: NOME_TABELA, NOME_COLUNA

---

## IMPORTACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MNFEM_SERIE | VARCHAR2(5) | N |  |  |
| 4 | MNFEM_NUM | VARCHAR2(15) | N |  |  |
| 5 | MNFEM_DTEMIS | DATE | N |  |  |
| 6 | CADG_COD | VARCHAR2(16) | N |  |  |
| 7 | CATG_COD | CHAR(2) | N |  |  |
| 8 | SEQ | NUMBER(2) | N |  |  |
| 9 | MDOC_COD | CHAR(3) | Y |  |  |
| 10 | DATA_ENTR | DATE | Y |  |  |
| 11 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 12 | DATA_DES | DATE | Y |  |  |
| 13 | VAL_IMP | NUMBER | Y |  |  |
| 14 | TARE | VARCHAR2(60) | Y |  |  |
| 15 | NUM01 | NUMBER | Y |  |  |
| 16 | NUM02 | NUMBER | Y |  |  |
| 17 | NUM03 | NUMBER | Y |  |  |
| 18 | VAR01 | VARCHAR2(150) | Y |  |  |
| 19 | VAR02 | VARCHAR2(150) | Y |  |  |
| 20 | VAR03 | VARCHAR2(150) | Y |  |  |
| 21 | VAR04 | VARCHAR2(150) | Y |  |  |
| 22 | VAR05 | VARCHAR2(150) | Y |  |  |
| 23 | IMP_COD_DOC_IMP | CHAR(1) | Y |  |  |
| 24 | IMP_PIS | NUMBER | Y |  |  |
| 25 | IMP_COFINS | NUMBER | Y |  |  |
| 26 | NUM_ACDRAW | VARCHAR2(20) | Y |  |  |

**PK**: EMPS_COD, SEQ, FILI_COD, MNFEM_SERIE, MNFEM_NUM, MNFEM_DTEMIS, CADG_COD, CATG_COD

---

## IMP_CALENDARIO_N_F

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_NAO_FUNC | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_NAO_FUNC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IMP_CATALOGO_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DSC_ARQUIVO | VARCHAR2(20) | N |  |  |
| 4 | PERIODICIDADE | CHAR(1) | Y |  |  |
| 5 | DIA_LIMITE | NUMBER(2) | Y |  |  |
| 6 | IND_TIPO_ARQUIVO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DSC_ARQUIVO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IMP_CONCILIACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 7 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 8 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 21 | VLR_INSS | NUMBER(17,2) | Y |  |  |
| 22 | BASE_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | BASE_ISEN_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | BASE_OUTR_ICMS | NUMBER(17,2) | Y |  |  |
| 25 | BASE_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 26 | BASE_ISEN_IPI | NUMBER(17,2) | Y |  |  |
| 27 | BASE_OUTR_IPI | NUMBER(17,2) | Y |  |  |
| 28 | BASE_TRIB_ISS | NUMBER(17,2) | Y |  |  |
| 29 | BASE_ISEN_ISS | NUMBER(17,2) | Y |  |  |
| 30 | BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 31 | BASE_INSS | NUMBER(17,2) | Y |  |  |
| 32 | COD_OCORRENCIA | NUMBER(2) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 34 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_DOCTO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IMP_CONSISTENCIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | DSC_ARQUIVO | VARCHAR2(20) | N |  |  |
| 5 | DATA_CONSISTENCIA | DATE | N |  |  |
| 6 | QTD_REG_INTERFACE | NUMBER(8) | Y |  |  |
| 7 | VLR_TOT_INTERFACE | NUMBER(17,2) | Y |  |  |
| 8 | QTD_REG_LIDOS | NUMBER(8) | Y |  |  |
| 9 | QTD_REG_GRAVADOS | NUMBER(8) | Y |  |  |
| 10 | QTD_REG_ERROS | NUMBER(8) | Y |  |  |
| 11 | QTD_REG_REPROC | NUMBER(8) | Y |  |  |
| 12 | QTD_REG_IGNORADOS | NUMBER(8) | Y |  |  |
| 13 | VLR_TOT_LIDOS | NUMBER(17,2) | Y |  |  |
| 14 | COD_OCORRENCIA | NUMBER(2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, DSC_ARQUIVO, DATA_CONSISTENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IMT_EMIT_DEST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 2 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 3 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 4 | CNPJ_EMPRESA | VARCHAR2(14) | N |  |  |
| 5 | CNPJ_ESTAB | VARCHAR2(14) | N |  |  |

**PK**: GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, CNPJ_EMPRESA, CNPJ_ESTAB

---

## IMT_NATUREZA_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 2 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(5) | N |  |  |
| 4 | CNPJ_EMPRESA | VARCHAR2(14) | N |  |  |
| 5 | CNPJ_ESTAB | VARCHAR2(14) | N |  |  |

**PK**: GRUPO_NATUREZA_OP, COD_CFOP, COD_NATUREZA_OP, CNPJ_EMPRESA, CNPJ_ESTAB

---

## IMT_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(72) | N |  |  |
| 4 | CNPJ_EMPRESA | VARCHAR2(14) | N |  |  |
| 5 | CNPJ_ESTAB | VARCHAR2(14) | N |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, CNPJ_EMPRESA, CNPJ_ESTAB

---

## IMT_SERVICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 2 | COD_SERVICO | VARCHAR2(47) | N |  |  |
| 3 | CNPJ_EMPRESA | VARCHAR2(14) | N |  |  |
| 4 | CNPJ_ESTAB | VARCHAR2(14) | N |  |  |

**PK**: GRUPO_SERVICO, COD_SERVICO, CNPJ_EMPRESA, CNPJ_ESTAB

---

## INCENTIVO_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SIGLA_INCENTIVO | VARCHAR2(3) | Y |  |  |
| 4 | COD_CFOP | VARCHAR2(4) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFOP

**FKs**:
- SIGLA_INCENTIVO → LINHAS_INCENTIVO(SIGLA_INCENTIVO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## INCENTIVO_LIV_COM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SIGLA_INCENTIVO | VARCHAR2(3) | Y |  |  |
| 4 | COD_AREA_LIVRE_COM | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_AREA_LIVRE_COM

**FKs**:
- SIGLA_INCENTIVO → LINHAS_INCENTIVO(SIGLA_INCENTIVO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## INCENTIVO_NAT_OPER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SIGLA_INCENTIVO | VARCHAR2(3) | Y |  |  |
| 4 | COD_CFOP | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_NAT_OPER | VARCHAR2(9) | N |  |  |
| 6 | COD_NAT_OPER | VARCHAR2(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFOP, GRUPO_NAT_OPER, COD_NAT_OPER

**FKs**:
- SIGLA_INCENTIVO → LINHAS_INCENTIVO(SIGLA_INCENTIVO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## INCENTIVO_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SIGLA_INCENTIVO | VARCHAR2(3) | Y |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, COD_PRODUTO, IND_PRODUTO

**FKs**:
- SIGLA_INCENTIVO → LINHAS_INCENTIVO(SIGLA_INCENTIVO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## INCIDENCIA_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 4 | IDENT_CFO | NUMBER(12) | N |  |  |
| 5 | IND_ACEITA_DIF | CHAR(1) | Y |  |  |
| 6 | IND_ACEITA_DEBCRE | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, IDENT_CFO

**FKs**:
- COD_TRIBUTO → TRIBUTO(COD_TRIBUTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## INCID_EXT_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 4 | IDENT_CFO | NUMBER(12) | N |  |  |
| 5 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |
| 6 | IND_ACEITA_DIF | CHAR(1) | Y |  |  |
| 7 | IND_ACEITA_DEBCRE | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, IDENT_CFO, IDENT_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, IDENT_CFO → INCIDENCIA_CFO(COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, IDENT_CFO)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)

---

## INDU

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | INDU_ID | NUMBER(20) | N |  |  |
| 2 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 3 | FILI_COD | VARCHAR2(9) | N |  |  |
| 4 | INFEM_SERIE | VARCHAR2(5) | N |  |  |
| 5 | INFEM_NUM | VARCHAR2(15) | N |  |  |
| 6 | CATG_COD | CHAR(2) | N |  |  |
| 7 | CADG_COD | VARCHAR2(16) | N |  |  |
| 8 | INFEM_NUM_ITEM | VARCHAR2(5) | N |  |  |
| 9 | INDU_SERIE | VARCHAR2(5) | N |  |  |
| 10 | INDU_NUM | VARCHAR2(15) | N |  |  |
| 11 | INDU_DTEMISS | DATE | N |  |  |
| 12 | INDU_NUM_ITEM | VARCHAR2(5) | N |  |  |
| 13 | INDU_CATG_COD | CHAR(2) | N |  |  |
| 14 | INDU_CADG_COD | VARCHAR2(16) | N |  |  |
| 15 | INFEM_DTENTR | DATE | Y |  |  |
| 16 | INDU_QTD_INS_UNI | NUMBER | Y |  |  |

**PK**: INDU_ID

---

## INFEM_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | INFEM_SERIE | VARCHAR2(5) | N |  |  |
| 4 | INFEM_NUM | VARCHAR2(15) | N |  |  |
| 5 | INFEM_DTEMIS | DATE | N |  |  |
| 6 | CATG_COD | CHAR(2) | N |  |  |
| 7 | CADG_COD | VARCHAR2(16) | N |  |  |
| 8 | INFEM_NUM_ITEM | VARCHAR2(5) | N |  |  |
| 9 | COMPL_TIPO | CHAR(2) | N |  |  |
| 10 | COMPL_COD | VARCHAR2(6) | N |  |  |

**PK**: EMPS_COD, FILI_COD, INFEM_SERIE, INFEM_NUM, INFEM_DTEMIS, CATG_COD, CADG_COD, INFEM_NUM_ITEM, COMPL_TIPO

---

## INIC_CATEGORIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | COD_CATEGORIA | NUMBER(5) | N |  |  |

**PK**: COD_EMPRESA, COD_PROG, COD_CATEGORIA

**FKs**:
- COD_EMPRESA, COD_PROG → INIC_PROG(COD_EMPRESA, COD_PROG)

---

## INIC_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA, COD_PROG, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_PROG → INIC_PROG(COD_EMPRESA, COD_PROG)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## INIC_HISTORICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_CATEGORIA | NUMBER(5) | N |  |  |
| 5 | COD_TAB_PROC | NUMBER(5) | N |  |  |
| 6 | DAT_EXECUCAO | DATE | N |  |  |
| 7 | QTD_REG_EXCLUI | NUMBER(12) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_PROG, COD_ESTAB, COD_CATEGORIA, COD_TAB_PROC, DAT_EXECUCAO

---

## INIC_PROG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | DSC_PROG | VARCHAR2(50) | Y |  |  |
| 4 | IND_PERIOD | CHAR(1) | Y |  |  |
| 5 | DT_INI_EVENT | DATE | Y |  |  |
| 6 | DIAS_EXCLUI | NUMBER(12) | Y |  |  |
| 7 | PROG_SEMANAL | VARCHAR2(7) | Y |  |  |
| 8 | PROG_MENSAL | VARCHAR2(64) | Y |  |  |

**PK**: COD_EMPRESA, COD_PROG

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## INT_CAT_ARQUIVOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ITEM | VARCHAR2(10) | N |  |  |
| 2 | NUM_ORDEM | NUMBER(2) | N |  |  |
| 3 | IND_TIP_IN | VARCHAR2(2) | N |  |  |
| 4 | NOM_LOGICO_ARQ | VARCHAR2(9) | Y |  |  |
| 5 | DSC_ITEM | VARCHAR2(100) | Y |  |  |
| 6 | NOM_CAMPO_TOT | VARCHAR2(50) | Y |  |  |
| 7 | NUM_PAG_LAY | NUMBER(2) | Y |  |  |
| 8 | NUM_ARQUIVO | VARCHAR2(10) | Y |  |  |
| 9 | IND_VERSAO_LAYOUT | VARCHAR2(10) | N | ' ' |  |

**PK**: COD_ITEM, NUM_ORDEM, IND_TIP_IN, IND_VERSAO_LAYOUT

---

## INT_DADOS_DUMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | IND_TIP_IN | CHAR(1) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | NOM_LOGICO_ARQ | VARCHAR2(9) | N |  |  |
| 6 | IND_ORDEM | CHAR(1) | N |  |  |
| 7 | NUM_REG | NUMBER(8) | N |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | DSC_CAMPOS | VARCHAR2(1000) | Y |  |  |

**PK**: COD_EMPRESA, COD_PROG, IND_TIP_IN, COD_ESTAB, NOM_LOGICO_ARQ, IND_ORDEM, NUM_REG

---

## INT_DET_PROG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | IND_TIP_IN | CHAR(1) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | NOM_LOGICO_ARQ | VARCHAR2(9) | N |  |  |
| 6 | SUFIXO_ARQUIVO | VARCHAR2(3) | Y |  |  |
| 7 | DATA_INI | DATE | Y |  |  |
| 8 | DATA_FIM | DATE | Y |  |  |
| 9 | NUM_REMESSA | VARCHAR2(4) | Y |  |  |
| 10 | NUM_REGIAO_FISCAL | VARCHAR2(2) | Y |  |  |
| 11 | NUM_DRF_RESPONSAVEL | VARCHAR2(5) | Y |  |  |
| 12 | COD_CONTA_INI | VARCHAR2(70) | Y |  |  |
| 13 | COD_CONTA_FIM | VARCHAR2(70) | Y |  |  |
| 14 | COD_PES_FISJUR_INI | VARCHAR2(14) | Y |  |  |
| 15 | COD_PES_FISJUR_FIM | VARCHAR2(14) | Y |  |  |
| 16 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 17 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 18 | NUM_DOCTO_INI | VARCHAR2(12) | Y |  |  |
| 19 | NUM_DOCTO_FIM | VARCHAR2(12) | Y |  |  |
| 20 | MOVTO_INI | CHAR(1) | Y |  |  |
| 21 | MOVTO_FIM | CHAR(1) | Y |  |  |
| 22 | COD_PRODUTO_INI | VARCHAR2(60) | Y |  |  |
| 23 | COD_PRODUTO_FIM | VARCHAR2(60) | Y |  |  |
| 24 | COD_BEM_INI | VARCHAR2(60) | Y |  |  |
| 25 | COD_INCORP_INI | VARCHAR2(6) | Y |  |  |
| 26 | COD_BEM_FIM | VARCHAR2(60) | Y |  |  |
| 27 | COD_INCORP_FIM | VARCHAR2(6) | Y |  |  |
| 28 | COD_FUNCIO_INI | VARCHAR2(14) | Y |  |  |
| 29 | COD_FUNCIO_FIM | VARCHAR2(14) | Y |  |  |
| 30 | COD_VERBA_INI | VARCHAR2(6) | Y |  |  |
| 31 | COD_VERBA_FIM | VARCHAR2(6) | Y |  |  |
| 32 | COD_DARF_INI | VARCHAR2(4) | Y |  |  |
| 33 | COD_DARF_FIM | VARCHAR2(4) | Y |  |  |
| 34 | COD_VERBA_INSS | VARCHAR2(6) | Y |  |  |
| 35 | COD_VERBPENS_ALIM | VARCHAR2(6) | Y |  |  |
| 36 | COD_VERBA_DEPEND | VARCHAR2(6) | Y |  |  |
| 37 | COD_VERBAMAIOR_65 | VARCHAR2(6) | Y |  |  |
| 38 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 39 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 40 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 41 | IND_GRACOD_CPFCNPJ | CHAR(1) | Y |  | Indicador de gravacao do codigo do participante. Dominio:  1 – Codigo PFJ, 2 -  CPF/CNPJ, 3 – Indicador + Codigo PFJ |
| 42 | IND_NOTA_CACELADA | CHAR(1) | Y |  |  |
| 43 | IND_SALDO_ABR_FECH | CHAR(1) | Y |  |  |
| 44 | COD_INVENT_PRODNBM | CHAR(1) | Y |  |  |
| 45 | NUM_RE_INI | VARCHAR2(15) | Y |  |  |
| 46 | NUM_RE_FIM | VARCHAR2(15) | Y |  |  |
| 47 | NUM_DDE_INI | VARCHAR2(12) | Y |  |  |
| 48 | NUM_DDE_FIM | VARCHAR2(12) | Y |  |  |
| 49 | NUM_DI_INI | VARCHAR2(15) | Y |  |  |
| 50 | NUM_DI_FIM | VARCHAR2(15) | Y |  |  |
| 51 | IND_CONS_NAT_EST | CHAR(1) | Y |  |  |
| 52 | IND_GERA_MERC | CHAR(1) | Y |  |  |
| 53 | IND_GERA_PJ_PF | CHAR(1) | Y |  |  |
| 54 | COD_SERVICO_INI | VARCHAR2(4) | Y |  |  |
| 55 | COD_SERVICO_FIM | VARCHAR2(4) | Y |  |  |
| 56 | IND_CUSTO_DESP | CHAR(1) | Y |  |  |
| 57 | IND_TP_OP | CHAR(1) | Y |  |  |
| 58 | IND_BASE_GERACAO | CHAR(1) | Y |  |  |
| 59 | IND_VERBA | CHAR(1) | Y |  |  |
| 60 | IND_NF_CANC | CHAR(1) | Y |  |  |
| 61 | COD_TIPO_MOVTO | VARCHAR2(3) | Y |  |  |
| 62 | IND_TP_GERACAO | CHAR(1) | Y |  |  |
| 63 | IND_ALINHAMENTO | CHAR(1) | Y | 'E' |  |
| 64 | IND_QTD_DIG_CFOP | NUMBER(2) | Y | 4 |  |
| 65 | IND_MOV_X42 | CHAR(1) | Y | 'N' |  |
| 66 | IND_SEM_DESC | CHAR(1) | Y | 'N' |  |
| 67 | IND_N_CONSID_NF_ISS | CHAR(1) | Y | 'N' |  |
| 68 | IND_CONS_NDESTAC | CHAR(1) | Y | 'N' | FLAG - CONSIDERAR VALOR DE ICMS/IPI/ICMS-ST NAP ESCRITURADO PARA GERACAO DO RESPECTIVO CAMPO DE VALOR DO IMPOSTO |
| 69 | IND_COD_SERV_NAT | CHAR(1) | Y | '1' | 1 - GERAR CODIGO DE SERVICO / 2 - GERAR CODIGO NATUREZA DE SERVICO SAFR81/SAFR83/SAFR92 |
| 70 | IND_GRAVA_PROD | CHAR(1) | Y |  | Indicador de gravacao do produto. Dominio: 1 – COdigo, 2 - Indicador + Codigo |
| 71 | IND_CENTRALIZADOR | CHAR(1) | Y | 'N' |  |
| 72 | IND_BEM_INDIV | CHAR(1) | Y | 'N' |  |
| 73 | IND_BEM_COMPONENTE | CHAR(1) | Y | 'N' |  |
| 74 | IND_BEM_RESULT | CHAR(1) | Y | 'N' |  |
| 75 | IND_DT_DEPREC | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_PROG, IND_TIP_IN, COD_ESTAB, NOM_LOGICO_ARQ

**FKs**:
- COD_EMPRESA, COD_PROG, IND_TIP_IN → INT_PROG(COD_EMPRESA, COD_PROG, IND_TIP_IN)

---

## INT_EXC_MODELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MODELO

---

## INT_HISTORICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_PROG | NUMBER(12) | Y |  |  |
| 4 | IND_TIP_IN | CHAR(1) | Y |  |  |
| 5 | NOM_LOGICO_ARQ | VARCHAR2(9) | Y |  |  |
| 6 | SUFIXO_ARQUIVO | VARCHAR2(2) | Y |  |  |
| 7 | NUM_PAG_LAYOUT | NUMBER(2) | Y |  |  |
| 8 | NUM_PAG_PRIM | NUMBER(2) | Y |  |  |
| 9 | NUM_PAG_FIM | NUMBER(2) | Y |  |  |
| 10 | NUM_VOLUMES | NUMBER(2) | Y |  |  |
| 11 | NUM_CAPACIDADE | NUMBER(12) | Y |  |  |
| 12 | COD_EQUIPAMENTO | VARCHAR2(3) | Y |  |  |
| 13 | COD_TIPO_MIDIA | VARCHAR2(3) | Y |  |  |
| 14 | COD_SOFTWARE | VARCHAR2(3) | Y |  |  |
| 15 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 16 | FATOR_BLOCO | NUMBER(5) | Y |  |  |
| 17 | TAM_BLOCO | NUMBER(5) | Y |  |  |
| 18 | TOT_REG | NUMBER(12) | Y |  |  |
| 19 | TOT_CAMPO_TOT | NUMBER(18) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | DATA_INI | DATE | Y |  |  |
| 22 | DATA_FIM | DATE | Y |  |  |
| 23 | DATA_EXEC | DATE | Y |  |  |
| 24 | NUM_REMESSA | VARCHAR2(4) | Y |  |  |
| 25 | NUM_REGIAO_FISCAL | VARCHAR2(2) | Y |  |  |
| 26 | NUM_DRF_RESP | VARCHAR2(5) | Y |  |  |
| 27 | COD_CONTA_INI | VARCHAR2(70) | Y |  |  |
| 28 | COD_CONTA_FIM | VARCHAR2(70) | Y |  |  |
| 29 | COD_PES_FISJUR_INI | VARCHAR2(14) | Y |  |  |
| 30 | COD_PES_FISJUR_FIM | VARCHAR2(14) | Y |  |  |
| 31 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 32 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 33 | NUM_DOCTO_INI | VARCHAR2(12) | Y |  |  |
| 34 | NUM_DOCTO_FIM | VARCHAR2(12) | Y |  |  |
| 35 | MOVTO_INI | CHAR(1) | Y |  |  |
| 36 | MOVTO_FIM | CHAR(1) | Y |  |  |
| 37 | COD_PRODUTO_INI | VARCHAR2(60) | Y |  |  |
| 38 | COD_PRODUTO_FIM | VARCHAR2(60) | Y |  |  |
| 39 | COD_BEM_INI | VARCHAR2(60) | Y |  |  |
| 40 | COD_INCORP_INI | VARCHAR2(6) | Y |  |  |
| 41 | COD_BEM_FIM | VARCHAR2(60) | Y |  |  |
| 42 | COD_INCORP_FIM | VARCHAR2(6) | Y |  |  |
| 43 | COD_FUNCIONA_INI | VARCHAR2(14) | Y |  |  |
| 44 | COD_FUNCIONA_FIM | VARCHAR2(14) | Y |  |  |
| 45 | COD_VERBA_INI | VARCHAR2(6) | Y |  |  |
| 46 | COD_VERBA_FIM | VARCHAR2(6) | Y |  |  |
| 47 | COD_DARF_INI | VARCHAR2(4) | Y |  |  |
| 48 | COD_DARF_FIM | VARCHAR2(4) | Y |  |  |
| 49 | COD_VERBA_INSS | VARCHAR2(6) | Y |  |  |
| 50 | COD_VERBAPENS_ALIM | VARCHAR2(6) | Y |  |  |
| 51 | COD_VERBA_DEPEND | VARCHAR2(6) | Y |  |  |
| 52 | COD_VERBAMAIOR_65 | VARCHAR2(6) | Y |  |  |
| 53 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 54 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 55 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 56 | GRAV_COD_CPF_CNPJ | CHAR(1) | Y |  |  |
| 57 | IND_NOTA_CACELADA | CHAR(1) | Y |  |  |
| 58 | IND_SALDO_ABR_FECH | CHAR(1) | Y |  |  |
| 59 | IND_INVENT_PRODNBM | CHAR(1) | Y |  |  |
| 60 | NUM_RE_INI | VARCHAR2(15) | Y |  |  |
| 61 | NUM_RE_FIM | VARCHAR2(15) | Y |  |  |
| 62 | NUM_DDE_INI | VARCHAR2(12) | Y |  |  |
| 63 | NUM_DDE_FIM | VARCHAR2(12) | Y |  |  |
| 64 | NUM_DI_INI | VARCHAR2(15) | Y |  |  |
| 65 | NUM_DI_FIM | VARCHAR2(15) | Y |  |  |
| 66 | IND_CONS_NAT_EST | CHAR(1) | Y |  |  |
| 67 | IND_GERA_MERC | CHAR(1) | Y |  |  |
| 68 | IND_GERA_PJ_PF | CHAR(1) | Y |  |  |
| 69 | COD_SERVICO_INI | VARCHAR2(4) | Y |  |  |
| 70 | COD_SERVICO_FIM | VARCHAR2(4) | Y |  |  |
| 71 | IND_CUSTO_DESP | CHAR(1) | Y |  |  |
| 72 | IND_VERSAO | CHAR(1) | Y |  |  |
| 73 | IND_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |

---

## INT_NF_CONJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OBRIG | CHAR(2) | N |  |  |
| 2 | DESCONSIDERA_NF_CONJ | CHAR(1) | N | 'N' |  |
| 3 | NAO_EXIBE_MSG_REPLIC | CHAR(1) | Y | 'N' |  |

**PK**: COD_OBRIG

---

## INT_PROG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | IND_TIP_IN | CHAR(1) | N |  |  |
| 4 | DSC_PROG | VARCHAR2(50) | Y |  |  |
| 5 | DSC_DIRETORIO | VARCHAR2(500) | Y |  |  |
| 6 | NUM_CAPACIDADE | NUMBER(12) | Y |  |  |
| 7 | NUM_CAPAC_OUTROS | NUMBER(12) | Y |  |  |
| 8 | COD_EQUIPAMENTO | VARCHAR2(3) | Y |  |  |
| 9 | COD_TIPO_MIDIA | VARCHAR2(3) | Y |  |  |
| 10 | COD_SOFTWARE | VARCHAR2(3) | Y |  |  |
| 11 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 12 | FATOR_BLOCO | NUMBER(5) | Y |  |  |
| 13 | TAM_BLOCO | NUMBER(5) | Y |  |  |
| 14 | STATUS_EXEC | CHAR(1) | Y |  |  |
| 15 | COD_RESP_TEC | VARCHAR2(2) | Y |  |  |
| 16 | IND_INC_COD_ARQ | CHAR(1) | Y | 'N' |  |
| 17 | IND_PRES_DIRET | CHAR(1) | Y | 'N' |  |
| 18 | IND_VERSAO | CHAR(1) | Y |  |  |
| 19 | IND_ARQ_SEPARADOS | CHAR(1) | Y | 'N' |  |
| 20 | DET_LOG_PROC_DOCFIS | CHAR(1) | Y |  |  |
| 21 | IND_NOME_ARQUIVO | VARCHAR2(1) | Y |  |  |
| 22 | IND_VERSAO_LAYOUT | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_PROG, IND_TIP_IN

---

## INT_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | IND_TIP_IN | CHAR(1) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | NOM_LOGICO_ARQ | VARCHAR2(9) | N |  |  |
| 6 | SUFIXO_ARQUIVO | VARCHAR2(2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | DATA_EXEC | DATE | Y |  |  |
| 9 | NUM_PAG_PRIM | NUMBER(2) | Y |  |  |
| 10 | NUM_PAG_ULT | NUMBER(2) | Y |  |  |
| 11 | NUM_VOLUMES | NUMBER(2) | Y |  |  |
| 12 | TOT_REG | NUMBER(12) | Y |  |  |
| 13 | TOT_CAMPO_TOT | NUMBER(18) | Y |  |  |
| 14 | DATA_INI | DATE | Y |  |  |
| 15 | DATA_FIM | DATE | Y |  |  |
| 16 | TAM_ARQUIVO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_PROG, IND_TIP_IN, COD_ESTAB, NOM_LOGICO_ARQ

---

## INT_SAIDA_GER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_PROG | NUMBER(12) | Y |  |  |
| 3 | IND_TIP_IN | CHAR(1) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | NOM_LOGICO_ARQ | VARCHAR2(9) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER | Y |  |  |
| 7 | DSC_CAMPOS | VARCHAR2(1000) | Y |  |  |
| 8 | CHAVE_ORIGEM | VARCHAR2(255) | Y |  |  |

**Indexes**:
- IX_INT_SAIDA_GER: (COD_EMPRESA, COD_PROG, IND_TIP_IN, COD_ESTAB, NOM_LOGICO_ARQ, CHAVE_ORIGEM)

---

## INVC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | INVE_DAT | DATE | N |  |  |
| 4 | MATE_COD | VARCHAR2(60) | N |  |  |
| 5 | INVC_QTD | NUMBER | Y |  |  |
| 6 | INVC_QTD_ENTRADA | NUMBER | Y |  |  |
| 7 | INVC_QTD_SAIDA | NUMBER | Y |  |  |
| 8 | UNID_COD | CHAR(3) | Y |  |  |
| 9 | INVC_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 10 | INVC_VAL_CUSTTOT | NUMBER | Y |  |  |
| 11 | INVC_VAL_CUSTICMS | NUMBER | Y |  |  |
| 12 | INVC_VAL_CUSTFR | NUMBER | Y |  |  |
| 13 | INVC_VAL_CUSTFRIC | NUMBER | Y |  |  |
| 14 | INVC_VAL_CUSTMES | NUMBER | Y |  |  |
| 15 | INVC_VAL_ICMSMES | NUMBER | Y |  |  |
| 16 | INVC_VAL_CUSTOTMES | NUMBER | Y |  |  |
| 17 | INVC_VAL_ICMTOTMES | NUMBER | Y |  |  |
| 18 | INVC_VAL_CUSTTER | NUMBER | Y |  |  |
| 19 | INVC_VAL_ICMSTER | NUMBER | Y |  |  |
| 20 | INVC_QTD_FC3A | NUMBER | Y |  |  |
| 21 | INVC_QTD_FC3B | NUMBER | Y |  |  |
| 22 | INVC_QTD_FC3C | NUMBER | Y |  |  |
| 23 | INVC_QTD_ENTRADA_3B | NUMBER | Y |  |  |
| 24 | INVC_QTD_SAIDA_3B | NUMBER | Y |  |  |
| 25 | INVC_VAL_CUSTUNIT_3B | NUMBER | Y |  |  |
| 26 | INVC_VAL_CUSTTOT_3B | NUMBER | Y |  |  |
| 27 | INVC_VAL_CUSTICMS_3B | NUMBER | Y |  |  |
| 28 | INVC_VAL_CUSTMES_3B | NUMBER | Y |  |  |
| 29 | INVC_VAL_CUSTOTMES_3B | NUMBER | Y |  |  |
| 30 | INVC_VAL_ICMSMES_3B | NUMBER | Y |  |  |
| 31 | INVC_VAL_ICMTOTMES_3B | NUMBER | Y |  |  |
| 32 | INVC_VAL_CUSTFR_3B | NUMBER | Y |  |  |
| 33 | INVC_VAL_CUSTFRIC_3B | NUMBER | Y |  |  |
| 34 | INVC_QTD_ENTRADA_3A | NUMBER | Y |  |  |
| 35 | INVC_QTD_SAIDA_3A | NUMBER | Y |  |  |
| 36 | INVC_VAL_CUSTUNIT_3A | NUMBER | Y |  |  |
| 37 | INVC_VAL_CUSTTOT_3A | NUMBER | Y |  |  |
| 38 | INVC_VAL_CUSTICMS_3A | NUMBER | Y |  |  |
| 39 | INVC_VAL_CUSTMES_3A | NUMBER | Y |  |  |
| 40 | INVC_VAL_CUSTOTMES_3A | NUMBER | Y |  |  |
| 41 | INVC_VAL_ICMSMES_3A | NUMBER | Y |  |  |
| 42 | INVC_VAL_ICMTOTMES_3A | NUMBER | Y |  |  |
| 43 | INVC_VAL_CUSTFR_3A | NUMBER | Y |  |  |
| 44 | INVC_VAL_CUSTFRIC_3A | NUMBER | Y |  |  |
| 45 | INVC_QTD_ENTRADA_3C | NUMBER | Y |  |  |
| 46 | INVC_QTD_SAIDA_3C | NUMBER | Y |  |  |
| 47 | INVC_VAL_CUSTUNIT_3C | NUMBER | Y |  |  |
| 48 | INVC_VAL_CUSTTOT_3C | NUMBER | Y |  |  |
| 49 | INVC_VAL_CUSTICMS_3C | NUMBER | Y |  |  |
| 50 | INVC_VAL_CUSTMES_3C | NUMBER | Y |  |  |
| 51 | INVC_VAL_CUSTOTMES_3C | NUMBER | Y |  |  |
| 52 | INVC_VAL_ICMSMES_3C | NUMBER | Y |  |  |
| 53 | INVC_VAL_ICMTOTMES_3C | NUMBER | Y |  |  |
| 54 | INVC_VAL_CUSTFR_3C | NUMBER | Y |  |  |
| 55 | INVC_VAL_CUSTFRIC_3C | NUMBER | Y |  |  |

**PK**: EMPS_COD, FILI_COD, INVE_DAT, MATE_COD

**Indexes**:
- IX_INVC1: (EMPS_COD, FILI_COD, INVE_DAT)
- IX_INVC2: (EMPS_COD, FILI_COD, INVE_DAT, INVC_QTD_ENTRADA, INVC_QTD_SAIDA)

---

## INVENTARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MATE_COD | VARCHAR2(60) | N |  |  |
| 4 | LOCA_COD | CHAR(3) | N |  |  |
| 5 | INVE_DAT | DATE | N |  |  |
| 6 | NSTQ_COD | VARCHAR2(5) | N |  |  |
| 7 | CNBM_COD | VARCHAR2(10) | N |  |  |
| 8 | INVE_QTD | NUMBER | Y |  |  |
| 9 | INVE_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 10 | INVE_VAL_CUSTTOT | NUMBER | Y |  |  |
| 11 | CCUS_COD | VARCHAR2(28) | N |  |  |
| 12 | PCON_COD_CONTA | VARCHAR2(70) | Y |  |  |
| 13 | UNID_COD | CHAR(3) | Y |  |  |
| 14 | OBS | VARCHAR2(150) | Y |  |  |
| 15 | INVE_DIV | CHAR(4) | Y |  |  |
| 16 | NUM01 | NUMBER | Y |  |  |
| 17 | NUM02 | NUMBER | Y |  |  |
| 18 | NUM03 | NUMBER | Y |  |  |
| 19 | VAR01 | VARCHAR2(150) | Y |  |  |
| 20 | VAR02 | VARCHAR2(150) | Y |  |  |
| 21 | VAR03 | VARCHAR2(150) | Y |  |  |
| 22 | VAR04 | VARCHAR2(150) | Y |  |  |
| 23 | VAR05 | VARCHAR2(150) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, MATE_COD, LOCA_COD, INVE_DAT, NSTQ_COD, CNBM_COD, CCUS_COD

**Indexes**:
- INVENTARIOI2: (EMPS_COD, FILI_COD, INVE_DAT, MATE_COD)

---

## IPI_INCENT_SAIDAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IND_TP_GERACAO | CHAR(1) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | COD_NBM | VARCHAR2(10) | N |  |  |
| 9 | QTD_PRODUTO | NUMBER(17,6) | Y |  |  |
| 10 | VLR_BASE2 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE3 | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | N |  |  |
| 14 | VLR_BASE_1 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_4 | NUMBER(17,2) | Y |  |  |

**PK**: USUARIO, COD_EMPRESA, COD_ESTAB, DAT_APUR, IND_TP_GERACAO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_NBM

---

## IRP_TP_INSS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_TP_FIS_JUR | CHAR(1) | N |  |  |
| 4 | VLR_ALIQ_INSS | NUMBER(11,4) | N |  |  |
| 5 | IND_FONTE_AVULSO | CHAR(1) | Y |  |  |
| 6 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 7 | IND_MOVTO | CHAR(1) | Y |  |  |
| 8 | IND_RET_EMISS_CPAG_CINDIVIDUAL | CHAR(1) | Y | 'N' | Considerar retencoes para emissao do Comprovante de Pagamento a Contribuinte Individual |

**PK**: COD_EMPRESA, COD_ESTAB, IND_TP_FIS_JUR, VLR_ALIQ_INSS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## ITF_MOV_PROD_FCI
**Comment**: Tabela utilizada pela Interface para controle do retorno das informações do FCI do DW para o EBS.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | COD_MEDIDA_FCI | VARCHAR2(6) | N |  |  |
| 6 | REGISTRATION_NUMBER | VARCHAR2(14) | Y |  | CNPJ do Estabelecimento |
| 7 | DAT_ATUALIZACAO | DATE | Y |  | Data de atualização produto ERP |
| 8 | FLG_STATUS | VARCHAR2(50) | Y |  | Status do registro no DW em relação ao ERP – N - nao processado ERP, S - processado ERP |
| 9 | RET_CODE | VARCHAR2(50) | Y |  | ERP API return code |
| 10 | RET_MESSAGE | VARCHAR2(50) | Y |  | ERP API return message |
| 11 | RET_USER | VARCHAR2(50) | Y |  | User run process |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO, COD_MEDIDA_FCI

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO, COD_MEDIDA_FCI → X214_MOV_PROD_FCI(COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO, COD_MEDIDA_FCI)

---

## JOB_BCK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | TIPO_JOB | CHAR(1) | Y |  |  |
| 3 | STATUS_JOB | CHAR(1) | Y |  |  |
| 4 | DATA_PROG | DATE | Y |  |  |
| 5 | DATA_EXEC_INI | DATE | Y |  |  |
| 6 | DATA_EXEC_FIM | DATE | Y |  |  |
| 7 | DATA_REF_INI | DATE | Y |  |  |
| 8 | DATA_REF_FIM | DATE | Y |  |  |
| 9 | DESCRICAO | VARCHAR2(255) | Y |  |  |
| 10 | RESPONS_PROG | VARCHAR2(40) | Y |  |  |
| 11 | RESPONS_EXEC | VARCHAR2(40) | Y |  |  |
| 12 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 13 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 14 | DIRETORIO_WORK | VARCHAR2(60) | Y |  |  |
| 15 | DSC_LOCAL | VARCHAR2(40) | Y |  |  |
| 16 | TP_BCK | CHAR(1) | Y |  |  |
| 17 | TP_MIDIA | CHAR(1) | Y |  |  |
| 18 | QTD_MIDIAS | NUMBER(5) | Y |  |  |
| 19 | QTD_COPIAS | NUMBER(5) | Y |  |  |
| 20 | TAM_MIDIAS | NUMBER(12,2) | Y |  |  |

**PK**: NUM_JOB

---

## JOB_DET_PROG_EXP_TAX_DECISION

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: ID_PROG, COD_EMPRESA, COD_ESTAB

**FKs**:
- ID_PROG → JOB_PROG_EXP_TAX_DECISION(ID_PROG)

---

## JOB_EXPORT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DAT_REFER_INI | DATE | Y |  |  |
| 5 | DAT_REFER_FIM | DATE | Y |  |  |
| 6 | IND_DAT_ARQ | CHAR(1) | Y |  |  |
| 7 | DSC_DIRETORIO | VARCHAR2(255) | Y |  |  |
| 8 | DAT_INI_JOB | DATE | Y |  |  |
| 9 | DAT_FIM_JOB | DATE | Y |  |  |
| 10 | STATUS | VARCHAR2(4) | Y |  |  |
| 11 | IND_TP_DIRETORIO | CHAR(1) | Y |  |  |

**PK**: NUM_JOB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## JOB_EXP_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DSC_DIRETORIO | VARCHAR2(255) | Y |  |  |

**PK**: NUM_JOB, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## JOB_EXP_TAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | GRUPO_ARQUIVO | NUMBER(2) | N |  |  |
| 3 | NUMERO_ARQUIVO | NUMBER(3) | N |  |  |
| 4 | DSC_DIRETORIO | VARCHAR2(255) | Y |  |  |
| 5 | IND_GERA_X530 | CHAR(1) | Y |  |  |
| 6 | IND_GERA_X751 | CHAR(1) | Y |  |  |
| 7 | IND_GERA_IRPJ | CHAR(1) | Y |  |  |

**PK**: NUM_JOB, GRUPO_ARQUIVO, NUMERO_ARQUIVO

**FKs**:
- NUM_JOB → JOB_EXPORT(NUM_JOB)
- GRUPO_ARQUIVO, NUMERO_ARQUIVO → CAT_PRIOR_IMP(GRUPO_ARQUIVO, NUMERO_ARQUIVO)

---

## JOB_HIST_PROG_EXP_TAX_DECISION

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_HORA_EXECUCAO | TIMESTAMP(6) | Y |  | Data e hora da execucao da programacao |
| 2 | ID_PROG | NUMBER(12) | Y |  | Identificador da programacao executada |
| 3 | PROC_ID | NUMBER(22) | Y |  | Identificador do processo gerado na tabela LIB_PROCESSO |
| 4 | COD_EMPRESA | VARCHAR2(3) | Y |  | Codigo da empresa exportada |
| 5 | COD_ESTAB | VARCHAR2(6) | Y |  | Codigo do estabelecimento exportado |
| 6 | IND_TIPO_PROCESSO | VARCHAR2(2) | Y |  | Tipo do processo de exportacao: 01 - Cadastro de Empresas 02 - Cadastro de Produtos 03 - Cadastro de Emitentes/Destinatarios 04 - Cadastro de Servicos 05 - Cadastro de Naturezas de Operacao 06 - Arquivo de Movimentacao Diaria 07 - Arquivo de Apuracao do ICMS/IPI 08 - Arquivo de Apuracao do ICMS-ST 09 - Arquivo de Apuracao da Cont. Social - Contribuicoes 10 - Arquivo de Apuracao da Cont. Social - Creditos. |
| 7 | DATA_INI_PER_EXPORT | DATE | Y |  | Data inicial do periodo exportado |
| 8 | DATA_FIN_PER_EXPORT | DATE | Y |  | Data final do periodo exportado |
| 9 | NOME_ARQUIVO | VARCHAR2(100) | Y |  | Nome do arquivo XML gerado |
| 10 | STATUS_EXPORT | VARCHAR2(5) | Y |  | Situacao da exportacao: OK / ERRO / AVISO |

**Indexes**:
- IX_JOB_HIST_PROG_EXP_TD: (DATA_HORA_EXECUCAO, ID_PROG, COD_EMPRESA, COD_ESTAB, IND_TIPO_PROCESSO)

---

## JOB_IMPORTACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | TIPO_JOB | CHAR(1) | Y |  |  |
| 3 | STATUS_JOB | CHAR(1) | Y |  |  |
| 4 | DATA_ABERTURA | DATE | Y |  |  |
| 5 | DATA_ENCERRAMENTO | DATE | Y |  |  |
| 6 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o job de carga/importação vai ser processado via funcionalidade do ATO COTEPE |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | TENANT_CODE | VARCHAR2(80) | Y |  |  |
| 9 | COD_PROG | NUMBER(12) | Y |  |  |

**PK**: NUM_JOB

---

## JOB_IMPORT_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_LOG_X2013 | VARCHAR2(1) | Y |  |  |
| 4 | IND_VALID_X2013 | VARCHAR2(1) | Y |  |  |
| 5 | IND_DATA_AVERB_X48 | VARCHAR2(1) | Y |  |  |
| 6 | IND_GERA_X530 | VARCHAR2(1) | Y |  |  |
| 7 | IND_GERA_X751 | VARCHAR2(1) | Y |  |  |
| 8 | IND_VALID_CEP_X04 | VARCHAR2(1) | Y |  |  |
| 9 | GRUPO_X188 | VARCHAR2(9) | Y |  |  |
| 10 | GRUPO_X189 | VARCHAR2(9) | Y |  |  |
| 11 | IND_SOBREPOR_REG | VARCHAR2(1) | Y | 'S' |  |
| 12 | IND_EXP_REG_ERRO | VARCHAR2(1) | Y |  |  |
| 13 | IND_DROP_TAB | VARCHAR2(1) | Y | 'T' |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## JOB_PROG_EXP_TAX_DECISION

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PROG | NUMBER(12) | N |  | Identificador da programacao |
| 2 | DSC_PROG | VARCHAR2(100) | Y |  | Nome da programacao |
| 3 | IND_SITUACAO | CHAR(1) | Y |  | Situacao da programacao A = Ativa / I = Inativa |
| 4 | DSC_DIRETORIO_GRAVACAO | VARCHAR2(255) | Y |  | Diretorio de saida dos arquivos XML |
| 5 | IND_PERIODICIDADE_PROG | CHAR(1) | Y |  | Tipo de periodicidade D = Diaria / S = Semanal / C = Decendial / M = Mensal |
| 6 | NUM_DIA_MES | NUMBER(2) | Y |  | Dia do mes no qual a programacao sera executada, valida somente para a periodicidade mensal |
| 7 | NUM_DIA_SEMANA | NUMBER(1) | Y |  | Dia da semana no qual a programacao sera executada, valida apenas para a periodicidade semanal |
| 8 | IND_PER_CORRESP | CHAR(1) | Y |  | Indicador do periodo correspondente a exportacao: C = Corrente / A = Anterior / N = varios periodos atras |
| 9 | QTD_PER_CORRESP | NUMBER(2) | Y |  | Quantidade de periodos a serem contados  |
| 10 | IND_APUR_ICMS | CHAR(1) | Y |  | Indica se serao gravados os arquivos de apuracao do ICMS e ICMS-ST (S/N) |
| 11 | IND_APUR_IPI | CHAR(1) | Y |  | Indica se serao gravados os arquivos de apuracao do IPI (S/N) |
| 12 | IND_APUR_CONTRIB | CHAR(1) | Y |  | Indica se serao gravados os arquivos de apuracao da contribuicao social (S/N) |
| 13 | IND_MOVTO_DIARIO | CHAR(1) | Y |  | Indica se serao gravados os arquivos de movimentacao diaria (S/N) |
| 14 | IND_MULTI_EMPRESA | CHAR(1) | Y |  | Indica se a exportacao sera feita multiempresa ou nao (S/N) |

**PK**: ID_PROG

---

## JOB_RESTORE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_JOB | NUMBER(12) | N |  |  |
| 2 | STATUS_JOB | CHAR(1) | Y |  |  |
| 3 | DATA_PROG | DATE | Y |  |  |
| 4 | DATA_EXEC_INI | DATE | Y |  |  |
| 5 | DATA_EXEC_FIM | DATE | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(255) | Y |  |  |
| 7 | RESPONS_PROG | VARCHAR2(40) | Y |  |  |
| 8 | RESPONS_EXEC | VARCHAR2(40) | Y |  |  |
| 9 | DIRETORIO_WORK | VARCHAR2(60) | Y |  |  |

**PK**: NUM_JOB

---

## JS_CONSTRAINTS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | OWNER | VARCHAR2(30) | Y |  |  |
| 2 | CONSTRAINT_NAME | VARCHAR2(30) | Y |  |  |
| 3 | TABLE_NAME | VARCHAR2(30) | Y |  |  |
| 4 | SEARCH_CONDITION | VARCHAR2(2000) | Y |  |  |

---

## JS_CONSTRAINTS_MIN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | OWNER | VARCHAR2(30) | Y |  |  |
| 2 | TABLE_NAME | VARCHAR2(30) | Y |  |  |
| 3 | SEARCH_CONDITION | VARCHAR2(2000) | Y |  |  |
| 4 | MIN_CONSTRAINT_NAME | VARCHAR2(30) | Y |  |  |
| 5 | CONSTRAINT_NAME | CHAR(32) | Y |  |  |

---

## LANCTO_ESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | LSTQ_NUM | VARCHAR2(15) | N |  |  |
| 4 | MATE_COD | VARCHAR2(60) | N |  |  |
| 5 | LSTQ_DAT | DATE | N |  |  |
| 6 | TDOC_COD | CHAR(5) | N |  |  |
| 7 | TOPE_COD | VARCHAR2(6) | N |  |  |
| 8 | NSTQ_COD | VARCHAR2(5) | N |  |  |
| 9 | LSTQ_QTD | NUMBER | N |  |  |
| 10 | LSTQ_NUM_ARQ | VARCHAR2(40) | N |  |  |
| 11 | INFEM_NUM | VARCHAR2(15) | Y |  |  |
| 12 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 13 | CCUS_COD | VARCHAR2(28) | Y |  |  |
| 14 | PCON_COD_CONTA | VARCHAR2(70) | Y |  |  |
| 15 | PCON_COD_CPART | VARCHAR2(70) | Y |  |  |
| 16 | LOCA_COD | CHAR(3) | Y |  |  |
| 17 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 18 | CATG_COD | CHAR(2) | Y |  |  |
| 19 | VAL_IPI | NUMBER | Y |  |  |
| 20 | LSTQ_VAL_UNIT | NUMBER | Y |  |  |
| 21 | LSTQ_VAL_TOT | NUMBER | Y |  |  |
| 22 | LSTQ_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 23 | LSTQ_VAL_CUSTTOT | NUMBER | Y |  |  |
| 24 | LSTQ_NUM_CSERV | VARCHAR2(14) | Y |  |  |
| 25 | LSTQ_NUM_SERIE | VARCHAR2(12) | Y |  |  |
| 26 | LSTQ_IND_LANCTO | CHAR(1) | N |  |  |
| 27 | LSTQ_SERIE | VARCHAR2(5) | Y |  |  |
| 28 | LRE_LRS | NUMBER(6) | Y |  |  |
| 29 | OBS | VARCHAR2(150) | Y |  |  |
| 30 | LSTQ_NUM_LOTE | VARCHAR2(10) | Y |  |  |
| 31 | LSTQ_DIV | CHAR(4) | Y |  |  |
| 32 | LSTQ_DOC_EST | VARCHAR2(10) | Y |  |  |
| 33 | LSTQ_ITEM_EST | CHAR(4) | Y |  |  |
| 34 | LSTQ_ANO_DOC | CHAR(4) | Y |  |  |
| 35 | NUM01 | NUMBER | Y |  |  |
| 36 | NUM02 | NUMBER | Y |  |  |
| 37 | NUM03 | NUMBER | Y |  |  |
| 38 | VAR01 | VARCHAR2(150) | Y |  |  |
| 39 | VAR02 | VARCHAR2(150) | Y |  |  |
| 40 | VAR03 | VARCHAR2(150) | Y |  |  |
| 41 | VAR04 | VARCHAR2(150) | Y |  |  |
| 42 | VAR05 | VARCHAR2(150) | Y |  |  |
| 43 | CH_ACESSO | VARCHAR2(80) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, LSTQ_NUM, MATE_COD, LSTQ_DAT, TDOC_COD, TOPE_COD, NSTQ_COD, LSTQ_QTD, LSTQ_NUM_ARQ, LSTQ_IND_LANCTO

**Indexes**:
- LANCTO_ESTOQUEI2: (EMPS_COD, FILI_COD, LSTQ_DAT, MATE_COD)
- LANCTO_ESTOQUEI3: (EMPS_COD, FILI_COD, LSTQ_IND_LANCTO, LSTQ_DAT)
- LANCTO_ESTOQUEI4: (EMPS_COD, FILI_COD, CATG_COD, CADG_COD, LSTQ_DAT, LSTQ_NUM, INFEM_NUM, CFOP_COD)

---

## LAYOUT_DIPJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VERSAO | VARCHAR2(4) | N |  |  |
| 2 | TIPO | VARCHAR2(4) | N |  |  |
| 3 | FICHA | VARCHAR2(4) | N |  |  |
| 4 | CAMPO | NUMBER(3) | N |  |  |
| 5 | POS_INI | NUMBER(6) | Y |  |  |
| 6 | TAMANHO | NUMBER(6) | Y |  |  |
| 7 | DESCRICAO | VARCHAR2(300) | Y |  |  |
| 8 | FORMATO_1 | VARCHAR2(10) | Y |  |  |
| 9 | FORMATO_2 | VARCHAR2(10) | Y |  |  |
| 10 | FORMATO_3 | VARCHAR2(10) | Y |  |  |
| 11 | MASCARA | VARCHAR2(50) | Y |  |  |
| 12 | FATOR_MASCARA | NUMBER | Y |  |  |
| 13 | DOMINIO | VARCHAR2(2000) | Y |  |  |
| 14 | IND_CAMPO_VALOR | VARCHAR2(1) | Y |  |  |

**PK**: VERSAO, TIPO, FICHA, CAMPO

---

## LEGE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | LSTQ_NUM | VARCHAR2(15) | N |  |  |
| 4 | MATE_COD | VARCHAR2(60) | N |  |  |
| 5 | LSTQ_DAT | DATE | N |  |  |
| 6 | TDOC_COD | CHAR(5) | N |  |  |
| 7 | TOPE_COD | VARCHAR2(6) | N |  |  |
| 8 | NSTQ_COD | VARCHAR2(5) | N |  |  |
| 9 | LSTQ_QTD | NUMBER | N |  |  |
| 10 | LSTQ_NUM_ARQ | VARCHAR2(40) | N |  |  |
| 11 | LSTQ_IND_LANCTO | CHAR(1) | N |  |  |
| 12 | INFEM_NUM | VARCHAR2(15) | Y |  |  |
| 13 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 14 | CATG_COD | CHAR(2) | Y |  |  |
| 15 | LSTQ_SERIE | VARCHAR2(5) | Y |  |  |
| 16 | CFOP_COD | VARCHAR2(6) | Y |  |  |
| 17 | CCUS_COD | VARCHAR2(28) | Y |  |  |
| 18 | PCON_COD_CONTA | VARCHAR2(70) | Y |  |  |
| 19 | PCON_COD_CPART | VARCHAR2(70) | Y |  |  |
| 20 | LOCA_COD | CHAR(3) | Y |  |  |
| 21 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 22 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 23 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 24 | LESC_NUM_ORDEM | VARCHAR2(40) | Y |  |  |
| 25 | LESC_COD_NIVEL | NUMBER(3) | Y |  |  |
| 26 | LESC_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 27 | LESC_VAL_CUSTICMS | NUMBER | Y |  |  |
| 28 | LESC_QTD_INS_UNI | NUMBER | Y |  |  |
| 29 | NUM01 | NUMBER | Y |  |  |
| 30 | NUM02 | NUMBER | Y |  |  |
| 31 | NUM03 | NUMBER | Y |  |  |
| 32 | VAR01 | VARCHAR2(150) | Y |  |  |
| 33 | VAR02 | VARCHAR2(150) | Y |  |  |
| 34 | VAR03 | VARCHAR2(150) | Y |  |  |
| 35 | VAR04 | VARCHAR2(150) | Y |  |  |
| 36 | VAR05 | VARCHAR2(150) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, LSTQ_NUM, MATE_COD, LSTQ_DAT, TDOC_COD, TOPE_COD, NSTQ_COD, LSTQ_QTD, LSTQ_NUM_ARQ, LSTQ_IND_LANCTO

**Indexes**:
- IX_LEGE1: (EMPS_COD, FILI_COD, LSTQ_DAT, LESC_IND_CF)

---

## LESC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | LSTQ_NUM | VARCHAR2(15) | N |  |  |
| 4 | MATE_COD | VARCHAR2(60) | N |  |  |
| 5 | LSTQ_DAT | DATE | N |  |  |
| 6 | TDOC_COD | CHAR(5) | N |  |  |
| 7 | TOPE_COD | VARCHAR2(6) | N |  |  |
| 8 | NSTQ_COD | VARCHAR2(5) | N |  |  |
| 9 | LSTQ_QTD | NUMBER | N |  |  |
| 10 | LSTQ_NUM_ARQ | VARCHAR2(40) | N |  |  |
| 11 | LSTQ_IND_LANCTO | CHAR(1) | N |  |  |
| 12 | PROD_COD | VARCHAR2(60) | Y |  |  |
| 13 | LESC_NUM_ORDEM | VARCHAR2(40) | Y |  |  |
| 14 | LESC_IND_CF | CHAR(1) | Y |  |  |
| 15 | LESC_COD_NIVEL | NUMBER(3) | Y |  |  |
| 16 | LESC_VAL_CUSTUNIT | NUMBER | Y |  |  |
| 17 | LESC_VAL_CUSTICMS | NUMBER | Y |  |  |
| 18 | LESC_IND_CIF_FOB | CHAR(1) | Y |  |  |
| 19 | LESC_QTD_INS_UNI | NUMBER | Y |  |  |
| 20 | IND_REDESIGNACAO | CHAR(1) | Y |  |  |
| 21 | MATE_COD_DEST | VARCHAR2(60) | Y |  |  |
| 22 | VLR_CUSTO_DCA | NUMBER | Y |  |  |
| 23 | VLR_ICMS_DCA | NUMBER | Y |  |  |

**PK**: EMPS_COD, FILI_COD, LSTQ_NUM, MATE_COD, LSTQ_DAT, TDOC_COD, TOPE_COD, NSTQ_COD, LSTQ_QTD, LSTQ_NUM_ARQ, LSTQ_IND_LANCTO

**Indexes**:
- LESCI2: (EMPS_COD, FILI_COD, LSTQ_DAT, LESC_IND_CF)

---

## LINHAS_INCENTIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SIGLA_INCENTIVO | VARCHAR2(3) | N |  |  |
| 2 | DESC_INCENTIVO | VARCHAR2(50) | Y |  |  |
| 3 | TIPO_INCENTIVO | CHAR(1) | Y |  |  |

**PK**: SIGLA_INCENTIVO

---

## LIPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LIPI_DAT | DATE | N |  |  |
| 2 | LIPI_COD | CHAR(3) | N |  |  |
| 3 | LIPI_DSC | VARCHAR2(150) | Y |  |  |

**PK**: LIPI_DAT, LIPI_COD

---

## LIVRO_LOCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TP_LOC | CHAR(2) | N |  |  |
| 2 | LOCA_COD | VARCHAR2(10) | N |  |  |
| 3 | LOCA_COR | VARCHAR2(10) | N |  |  |
| 4 | LOCA_DSC | VARCHAR2(150) | Y |  |  |
| 5 | LOCA_UF | CHAR(2) | N |  |  |

**PK**: TP_LOC, LOCA_COD, LOCA_COR, LOCA_UF

---

## LIVRO_SELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRUPO_SELO | NUMBER(2) | N |  |  |
| 4 | COD_SUBGRUPO_SELO | NUMBER(2) | N |  |  |
| 5 | COR_SELO | VARCHAR2(15) | N |  |  |
| 6 | SERIE_SELO | VARCHAR2(3) | N |  |  |
| 7 | DATA_REF | DATE | N |  |  |
| 8 | SEQUENCIAL | NUMBER(3) | N |  |  |
| 9 | OPERACAO | CHAR(1) | Y |  |  |
| 10 | NRO_GUIA | VARCHAR2(12) | Y |  |  |
| 11 | DATA_GUIA | DATE | Y |  |  |
| 12 | QUANTIDADE | NUMBER(11) | Y |  |  |
| 13 | NRO_INICIAL | NUMBER(12) | Y |  |  |
| 14 | NRO_FINAL | NUMBER(12) | Y |  |  |
| 15 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 16 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 17 | SALDO | NUMBER(11) | Y |  |  |
| 18 | OBSERVACAO | VARCHAR2(45) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRUPO_SELO, COD_SUBGRUPO_SELO, COR_SELO, SERIE_SELO, DATA_REF, SEQUENCIAL

---

## LOCALIZACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LOCA_COD | CHAR(3) | N |  |  |
| 2 | LOCA_DAT_ATUA | DATE | N |  |  |
| 3 | LOCA_DSC | VARCHAR2(150) | Y |  |  |
| 4 | IND_EST86 | CHAR(1) | Y |  |  |

**PK**: LOCA_COD, LOCA_DAT_ATUA

---

## LOG_DET_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | SEQUENCIA | NUMBER(12) | N |  |  |
| 3 | NUM_REG | NUMBER(12) | Y |  |  |
| 4 | MENS_ERRO | VARCHAR2(400) | Y |  |  |
| 5 | DADO_ERRO | VARCHAR2(500) | Y |  |  |
| 6 | MENS_COMPL | VARCHAR2(400) | Y |  |  |
| 7 | COD_ERRO | NUMBER(6) | Y |  |  |
| 8 | MENS_BANCO | VARCHAR2(200) | Y |  |  |
| 9 | LINHA_ARQUIVO | CLOB | Y |  |  |
| 10 | SOLUCAO_ERRO | VARCHAR2(500) | Y |  |  |

**PK**: NUM_PROCESSO, SEQUENCIA

---

## LOG_INSTALACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FUNCIONALIDADE | VARCHAR2(30) | N |  |  |
| 2 | ETAPA | NUMBER(22) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 4 | IND_STATUS | VARCHAR2(10) | Y |  |  |
| 5 | DT_EXEC | DATE | Y |  |  |
| 6 | PROC_ID | NUMBER(22) | Y |  |  |

**PK**: FUNCIONALIDADE, ETAPA

---

## LOG_PROCESSO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 5 | IND_PROCESSO | VARCHAR2(3) | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(8) | Y |  |  |
| 7 | VERSAO | VARCHAR2(10) | Y |  |  |
| 8 | STATUS | VARCHAR2(3) | Y |  |  |
| 9 | DATA_INI | DATE | Y |  |  |
| 10 | DATA_FIM | DATE | Y |  |  |
| 11 | DATA_INI_MOVTO | DATE | Y |  |  |
| 12 | DATA_FIM_MOVTO | DATE | Y |  |  |
| 13 | PERC_TOLERAVEL | NUMBER(5,2) | Y |  |  |
| 14 | COD_EQUIPAMENTO | VARCHAR2(3) | Y |  |  |
| 15 | COD_SOFTWARE | VARCHAR2(3) | Y |  |  |
| 16 | COD_TIPO_MIDIA | VARCHAR2(3) | Y |  |  |
| 17 | CAPACID_VOLUME | NUMBER(15,3) | Y |  |  |
| 18 | COD_RESP_GER | VARCHAR2(2) | Y |  |  |
| 19 | VAL_FATOR_BLOCO | NUMBER(5) | Y |  |  |
| 20 | VAL_TAM_BLOCO | NUMBER(5) | Y |  |  |

**PK**: NUM_PROCESSO

**FKs**:
- COD_EQUIPAMENTO, COD_SOFTWARE → SOFTWARE_EQUIP(COD_EQUIPAMENTO, COD_SOFTWARE)
- COD_TIPO_MIDIA → TIPO_MIDIA(COD_TIPO_MIDIA)

---

## LOG_PROCESSO_PARAM_JS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | LIMIT_BULK | NUMBER | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 5 | DATA_INIC | DATE | Y |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | DATA_FECHAMENTO | DATE | Y |  |  |
| 8 | IND_INS_DEL | VARCHAR2(2) | Y |  |  |
| 9 | IND_SP_REGISTRO | VARCHAR2(2) | Y |  |  |
| 10 | SEQ | NUMBER | Y |  |  |
| 11 | SEQ_ERRO | NUMBER | Y |  |  |
| 12 | IND_LIMITA_PER | VARCHAR2(2) | Y |  |  |
| 13 | COD_USUARIO | VARCHAR2(100) | Y |  |  |
| 14 | IND_ORIG_DADOS | VARCHAR2(2) | Y |  |  |
| 15 | QTD_INSERT | NUMBER(12) | Y |  |  |
| 16 | QTD_UPDATE | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | QTD_TOTAL | NUMBER(12) | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | IND_DROP_TAB | CHAR(1) | Y | 'S' |  |
| 21 | IND_PARALLEL | CHAR(1) | Y | 'S' |  |

**PK**: NUM_PROCESSO

**FKs**:
- NUM_PROCESSO → LOG_PROCESSO(NUM_PROCESSO)

---

## LVR_RAZAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | DATA_LANCTO | DATE | Y |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 7 | TXT_HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 8 | COD_HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 9 | DESCRICAO_HIST_PADRAO | VARCHAR2(50) | Y |  |  |
| 10 | COD_CONTA_CONTRA_PART | VARCHAR2(70) | Y |  |  |
| 11 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 12 | COD_DESPESA | VARCHAR2(20) | Y |  |  |
| 13 | VLR_LANCTO | NUMBER(19,2) | Y |  |  |
| 14 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 15 | IND_CONTA | CHAR(1) | Y |  |  |
| 16 | VLR_SD_INICIO | NUMBER(19,2) | Y |  |  |
| 17 | VLR_SD_INICIAL | NUMBER(19,2) | Y |  |  |
| 18 | VLR_SD_FIM | NUMBER(19,2) | Y |  |  |
| 19 | IND_SD_FIM | CHAR(1) | Y |  |  |
| 20 | CGC | VARCHAR2(14) | Y |  |  |
| 21 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 22 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 23 | IND_SD_INI | CHAR(1) | Y |  |  |

**Indexes**:
- IX_LVR_RAZAO: (COD_EMPRESA, COD_ESTAB, COD_CONTA)
- IX_LVR_RAZAO_2023: (COD_ESTAB, COD_EMPRESA, DATA_LANCTO)

---

## LVR_REIMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DATA_PER_INI | DATE | N |  |  |
| 5 | DATA_PER_FIM | DATE | N |  |  |
| 6 | PROC_ID | NUMBER(12) | Y |  |  |
| 7 | IMAGEM_REL | BLOB | Y |  |  |
| 8 | IMAGEM_PDF | BLOB | Y |  |  |
| 9 | IND_ORIG | VARCHAR2(10) | Y |  | Campo responsavel por conter a origem da atualizacao ou criacao do registro na tabela (REMISS: Origem a partir da emissao dos livros fiscais - UPLD: Origem a partir da funcionalidade de upload dos arquivos dos livros fiscais) |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DATA_PER_INI, DATA_PER_FIM

**Indexes**:
- IX_LVR_REIMP_01: (PROC_ID)

---

## LVR_REIMP_AM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | IND_INCENTIVO | CHAR(1) | N |  |  |
| 6 | DATA_PER_INI | DATE | N |  |  |
| 7 | DATA_PER_FIM | DATE | N |  |  |
| 8 | PROC_ID | NUMBER(12) | Y |  |  |
| 9 | IMAGEM_REL | BLOB | Y |  |  |
| 10 | IMAGEM_PDF | BLOB | Y |  |  |
| 11 | IND_ORIG | VARCHAR2(10) | Y |  | Campo responsavel por conter a origem da atualizacao ou criacao do registro na tabela (REMISS: Origem a partir da emissao dos livros fiscais - UPLD: Origem a partir da funcionalidade de upload dos arquivos dos livros fiscais) |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, IND_INCENTIVO, DATA_PER_INI, DATA_PER_FIM

**Indexes**:
- IX_LVR_REIMP_AM_01: (PROC_ID)

---

## LVR_REIMP_PRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DATA_PER_INI | DATE | N |  |  |
| 5 | DATA_PER_FIM | DATE | N |  |  |
| 6 | SERIE_LIVRO | CHAR(1) | N |  |  |
| 7 | SUB_SERIE_LIVRO | VARCHAR2(2) | N |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 9 | PROC_ID | NUMBER(12) | Y |  |  |
| 10 | IMAGEM_REL | BLOB | Y |  |  |
| 11 | IMAGEM_PDF | BLOB | Y |  |  |
| 12 | IND_ORIG | VARCHAR2(10) | Y |  | Campo responsavel por conter a origem da atualizacao ou criacao do registro na tabela (REMISS: Origem a partir da emissao dos livros fiscais - UPLD: Origem a partir da funcionalidade de upload dos arquivos dos livros fiscais) |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DATA_PER_INI, DATA_PER_FIM, SERIE_LIVRO, SUB_SERIE_LIVRO

**Indexes**:
- IX_LVR_REIMP_PRO_01: (PROC_ID)

---

## MATERIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MATE_COD | VARCHAR2(60) | N |  |  |
| 4 | MATE_DAT_ATUA | DATE | N |  |  |
| 5 | CMAT_COD | CHAR(1) | N |  |  |
| 6 | CNBM_COD | VARCHAR2(10) | Y |  |  |
| 7 | UNID_COD | CHAR(3) | Y |  |  |
| 8 | MATE_DSC | VARCHAR2(150) | Y |  |  |
| 9 | IND_PETROLEO | CHAR(1) | Y |  |  |
| 10 | IND_EST | CHAR(1) | Y |  |  |
| 11 | IND_INV | CHAR(1) | Y |  |  |
| 12 | EAN1 | VARCHAR2(14) | Y |  |  |
| 13 | EAN2 | VARCHAR2(14) | Y |  |  |
| 14 | EAN3 | VARCHAR2(14) | Y |  |  |
| 15 | EAN4 | VARCHAR2(14) | Y |  |  |
| 16 | EAN5 | VARCHAR2(14) | Y |  |  |
| 17 | NUMITEM | CHAR(2) | Y |  |  |
| 18 | PROD_SISIF | CHAR(1) | Y |  |  |
| 19 | DCB_COD | VARCHAR2(10) | Y |  |  |
| 20 | PORT_COD | VARCHAR2(10) | Y |  |  |
| 21 | CAT95P_COD | CHAR(4) | Y |  |  |
| 22 | IN359_COD | CHAR(3) | Y |  |  |
| 23 | IN63_COD_ESP | CHAR(2) | Y |  |  |
| 24 | NUM01 | NUMBER | Y |  |  |
| 25 | NUM02 | NUMBER | Y |  |  |
| 26 | NUM03 | NUMBER | Y |  |  |
| 27 | VAR01 | VARCHAR2(150) | Y |  |  |
| 28 | VAR02 | VARCHAR2(150) | Y |  |  |
| 29 | VAR03 | VARCHAR2(150) | Y |  |  |
| 30 | VAR04 | VARCHAR2(150) | Y |  |  |
| 31 | VAR05 | VARCHAR2(150) | Y |  |  |
| 32 | MATE_TIPO_ITEM | CHAR(2) | Y |  |  |
| 33 | MATE_ANT_ITEM | VARCHAR2(20) | Y |  |  |
| 34 | CEIP_COD | VARCHAR2(5) | Y |  |  |
| 35 | MATE_COD_SELO | VARCHAR2(6) | Y |  |  |
| 36 | MATE_QTD_SELO | NUMBER(5) | Y |  |  |
| 37 | CPAN_COD_ANP | VARCHAR2(9) | Y |  |  |
| 38 | MAT_INC_IPI | CHAR(2) | Y |  |  |
| 39 | MAT_COD_GRP | CHAR(2) | Y |  |  |
| 40 | MAT_MARCA | VARCHAR2(60) | Y |  |  |
| 41 | MAT_ALIQ_PRD | NUMBER | Y |  |  |
| 42 | MAT_IND_IMU | CHAR(1) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, MATE_COD, MATE_DAT_ATUA, CMAT_COD

**Indexes**:
- MATERIALI2: (EMPS_COD, MATE_COD, MATE_DAT_ATUA)

---

## MEIO_MAGNETICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 4 | DATA_GERACAO | DATE | Y |  |  |
| 5 | DATA_INICIAL | DATE | Y |  |  |
| 6 | DATA_FINAL | DATE | Y |  |  |
| 7 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 8 | PROC_ENTRA_UF_IG | CHAR(1) | Y |  |  |
| 9 | PROC_SAI_UF_IG | CHAR(1) | Y |  |  |
| 10 | PROC_ENTRA_UF_DI | CHAR(1) | Y |  |  |
| 11 | PROC_SAI_UF_DI | CHAR(1) | Y |  |  |
| 12 | TIPO_MIDIA | CHAR(1) | Y |  |  |
| 13 | ESPECIF_MIDIA | VARCHAR2(300) | Y |  |  |
| 14 | TAM_BLOCO | NUMBER(20) | Y |  |  |
| 15 | DENSIDADE_MIDIA | VARCHAR2(10) | Y |  |  |
| 16 | COD_EQUIPAMENTO | VARCHAR2(3) | Y |  |  |
| 17 | COD_SOFTWARE_SO | VARCHAR2(3) | Y |  |  |
| 18 | COD_SOFTWARE_LP | VARCHAR2(3) | Y |  |  |
| 19 | COD_SOFTWARE_BD | VARCHAR2(3) | Y |  |  |
| 20 | NUM_MIDIAS | NUMBER(5) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | COD_CONVENIO | VARCHAR2(5) | Y |  |  |
| 23 | IND_ATACADISTA_MG | CHAR(1) | Y |  |  |
| 24 | COD_PERFIL | VARCHAR2(3) | Y |  |  |
| 25 | PROC_ID | NUMBER | Y |  |  |

---

## MEIO_MAGNETICO_DIPJ
**Comment**: Repositorio do Meio Magnetico da DIPJ, OS 1344

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DECLARACAO | NUMBER(12) | N |  | IDENT_DECLARACAO |
| 2 | TIPO | VARCHAR2(4) | N |  | Identificador do Tipo da Ficha |
| 3 | FICHA | VARCHAR2(4) | N |  | Identificador da Ficha |
| 4 | SEQ_FICHA | NUMBER(12) | N |  | Auxiliar na ordenacao da Ficha |
| 5 | CNPJ_FILIAL | VARCHAR2(6) | N | ' ' | Para as fichas de IPI, as 6 ultimas posicoes do CNPJ da filial |
| 6 | IND_HEADER | CHAR(1) | Y | 'N' | Indica se linha HEADER da declaracao |
| 7 | REG_MEIO_MAGNETICO | VARCHAR2(2000) | Y |  | Linha ja formatada do Meio Magnetico da DIPJ |
| 8 | CHAVE_ORDENACAO | VARCHAR2(255) | Y |  |  |

**PK**: IDENT_DECLARACAO, TIPO, FICHA, SEQ_FICHA, CNPJ_FILIAL

**FKs**:
- IDENT_DECLARACAO → DECLARACAO_DIPJ(IDENT_DECLARACAO)

---

## MESTRE_NFEN_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | TDOC_COD | CHAR(5) | Y |  |  |
| 4 | MNFEM_SERIE | VARCHAR2(5) | N |  |  |
| 5 | MNFEM_NUM | VARCHAR2(15) | N |  |  |
| 6 | MNFEM_DTEMIS | DATE | N |  |  |
| 7 | MNFEM_IND_CONT | VARCHAR2(5) | Y |  |  |
| 8 | CATG_COD | CHAR(2) | N |  |  |
| 9 | CADG_COD | VARCHAR2(16) | N |  |  |
| 10 | MDOC_COD | CHAR(3) | Y |  |  |
| 11 | MNFEM_DTENTR | DATE | Y |  |  |
| 12 | MNFEM_VAL_TOT | NUMBER | Y |  |  |
| 13 | MNFEM_VAL_NF | NUMBER | Y |  |  |
| 14 | MNFEM_VAL_DESC | NUMBER | Y |  |  |
| 15 | MNFEM_NUM_NFREF | VARCHAR2(15) | Y |  |  |
| 16 | MNFEM_SERIE_NFREF | VARCHAR2(5) | Y |  |  |
| 17 | MNFEM_NUM_DECL | VARCHAR2(12) | Y |  |  |
| 18 | MNFEM_VAL_REDIPI | NUMBER | Y |  |  |
| 19 | MNFEM_VAL_TOTIPI | NUMBER | Y |  |  |
| 20 | MNFEM_INSEST_SUBST | VARCHAR2(14) | Y |  |  |
| 21 | MNFEM_OBSIPI | VARCHAR2(150) | Y |  |  |
| 22 | MNFEM_INDCONTR | CHAR(1) | Y |  |  |
| 23 | MNFEM_IND_CANC | CHAR(1) | Y |  |  |
| 24 | MNFEM_AVISTA | CHAR(1) | Y |  |  |
| 25 | MNFEM_NF_PROPRIA | CHAR(1) | Y |  |  |
| 26 | NUM01 | NUMBER | Y |  |  |
| 27 | NUM02 | NUMBER | Y |  |  |
| 28 | NUM03 | NUMBER | Y |  |  |
| 29 | VAR01 | VARCHAR2(150) | Y |  |  |
| 30 | VAR02 | VARCHAR2(150) | Y |  |  |
| 31 | VAR03 | VARCHAR2(150) | Y |  |  |
| 32 | VAR04 | VARCHAR2(150) | Y |  |  |
| 33 | VAR05 | VARCHAR2(150) | Y |  |  |
| 34 | MNFEM_REG | CHAR(1) | Y |  |  |
| 35 | MNFEM_CHV_NFE | VARCHAR2(44) | Y |  |  |
| 36 | MNFEM_VL_ABAT_NT | NUMBER | Y |  |  |
| 37 | MFRT_COD | CHAR(3) | Y |  |  |
| 38 | MNFEM_VL_FRT | NUMBER | Y |  |  |
| 39 | MNFEM_VL_SEG | NUMBER | Y |  |  |
| 40 | MNFEM_VL_OUT_DA | NUMBER | Y |  |  |
| 41 | MNFEM_VL_BC_ICMS | NUMBER | Y |  |  |
| 42 | MNFEM_VL_ICMS | NUMBER | Y |  |  |
| 43 | MNFEM_BC_ICMS_ST | NUMBER | Y |  |  |
| 44 | MNFEM_VL_ICMS_ST | NUMBER | Y |  |  |
| 45 | MNFEM_VL_PIS | NUMBER | Y |  |  |
| 46 | MNFEM_VL_COFINS | NUMBER | Y |  |  |
| 47 | MNFEM_VL_PIS_ST | NUMBER | Y |  |  |
| 48 | MNFEM_COFINS_ST | NUMBER | Y |  |  |
| 49 | MNFEM_IND_COMPL | CHAR(1) | Y |  |  |
| 50 | MNFEM_DEN_IN | CHAR(1) | Y |  |  |
| 51 | TRANS_PES_BRUTO | NUMBER | Y |  |  |
| 52 | TRANS_PES_LIQ | NUMBER | Y |  |  |
| 53 | TRANS_QTD_VOL | NUMBER | Y |  |  |
| 54 | MNFEM_HR_EMIS | VARCHAR2(6) | Y |  |  |
| 55 | MNFEM_TIP_ASSI | CHAR(2) | Y |  |  |
| 56 | MNFEM_TIP_UTIL | CHAR(2) | Y |  |  |
| 57 | MNFEM_GRP_TENS | CHAR(2) | Y |  |  |
| 58 | MNFEM_IND_EXTEMP | CHAR(1) | Y |  |  |
| 59 | MNFEM_DAT_EXTEMP | DATE | Y |  |  |
| 60 | MNFEM_TP_CTE | CHAR(1) | Y |  |  |
| 61 | MNFEM_NUM_DRWBCK | VARCHAR2(20) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, MNFEM_SERIE, MNFEM_NUM, MNFEM_DTEMIS, CADG_COD, CATG_COD

**Indexes**:
- MESTRE_NFEN_MERCI2: (EMPS_COD, FILI_COD, MNFEM_DTENTR)

---

## MESTRE_NFSD_MERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | TDOC_COD | CHAR(5) | Y |  |  |
| 4 | MNFSM_SERIE | VARCHAR2(5) | N |  |  |
| 5 | MNFSM_NUM | VARCHAR2(15) | N |  |  |
| 6 | MNFSM_DTEMISS | DATE | N |  |  |
| 7 | CATG_COD | CHAR(2) | N |  |  |
| 8 | CADG_COD | VARCHAR2(16) | Y |  |  |
| 9 | MNFSM_IND_CONT | VARCHAR2(5) | Y |  |  |
| 10 | MDOC_COD | CHAR(3) | Y |  |  |
| 11 | MNFSM_DTSAIDA | DATE | Y |  |  |
| 12 | MNFSM_VAL_TOTPROD | NUMBER | Y |  |  |
| 13 | MNFSM_VAL_TOTNF | NUMBER | Y |  |  |
| 14 | MNFSM_VAL_DESC | NUMBER | Y |  |  |
| 15 | MNFSM_NUMNFREF | VARCHAR2(15) | Y |  |  |
| 16 | MNFSM_SERIENFREF | VARCHAR2(5) | Y |  |  |
| 17 | MNFSM_VAL_REDIPI | NUMBER | Y |  |  |
| 18 | MNFSM_VAL_TOTIPI | NUMBER | Y |  |  |
| 19 | MNFSM_INSEST_SUBST | VARCHAR2(14) | Y |  |  |
| 20 | MNFSM_OBSIPI | VARCHAR2(150) | Y |  |  |
| 21 | MNFSM_IND_CONTR | CHAR(1) | Y |  |  |
| 22 | MNFSM_IND_CANC | CHAR(1) | Y |  |  |
| 23 | MNFSM_AVISTA | CHAR(1) | Y |  |  |
| 24 | CADG_COD_TRANSP | VARCHAR2(16) | Y |  |  |
| 25 | TRANS_VAL_FRETE | NUMBER | Y |  |  |
| 26 | TRANS_VAL_SEGUR | NUMBER | Y |  |  |
| 27 | MFRT_COD | CHAR(3) | Y |  |  |
| 28 | TRANS_PES_BRUTO | NUMBER | Y |  |  |
| 29 | TRANS_PES_LIQ | NUMBER | Y |  |  |
| 30 | VTRP_COD | CHAR(3) | Y |  |  |
| 31 | TRANS_QTD_VOL | NUMBER | Y |  |  |
| 32 | EVOL_COD | CHAR(3) | Y |  |  |
| 33 | TRANS_IDENT | VARCHAR2(17) | Y |  |  |
| 34 | NUM01 | NUMBER | Y |  |  |
| 35 | NUM02 | NUMBER | Y |  |  |
| 36 | NUM03 | NUMBER | Y |  |  |
| 37 | VAR01 | VARCHAR2(150) | Y |  |  |
| 38 | VAR02 | VARCHAR2(150) | Y |  |  |
| 39 | VAR03 | VARCHAR2(150) | Y |  |  |
| 40 | VAR04 | VARCHAR2(150) | Y |  |  |
| 41 | VAR05 | VARCHAR2(150) | Y |  |  |
| 42 | MNFSM_REG | CHAR(1) | Y |  |  |
| 43 | MNFSM_DEN_IN | CHAR(1) | Y |  |  |
| 44 | MNFSM_CHV_NFE | VARCHAR2(44) | Y |  |  |
| 45 | MNFSM_VL_ABAT_NT | NUMBER | Y |  |  |
| 46 | MNFSM_VL_OUT_DA | NUMBER | Y |  |  |
| 47 | MNFSM_VL_BC_ICMS | NUMBER | Y |  |  |
| 48 | MNFSM_VL_ICMS | NUMBER | Y |  |  |
| 49 | MNFSM_BC_ICMS_ST | NUMBER | Y |  |  |
| 50 | MNFSM_VL_ICMS_ST | NUMBER | Y |  |  |
| 51 | MNFSM_VL_IPI | NUMBER | Y |  |  |
| 52 | MNFSM_VL_PIS | NUMBER | Y |  |  |
| 53 | MNFSM_VL_COFINS | NUMBER | Y |  |  |
| 54 | MNFSM_VL_PIS_ST | NUMBER | Y |  |  |
| 55 | MNFSM_COFINS_ST | NUMBER | Y |  |  |
| 56 | MNFSM_IND_COMPL | CHAR(1) | Y |  |  |
| 57 | UNFE_SIG_VEICULO | CHAR(2) | Y |  |  |
| 58 | MNFSM_HR_EMIS | VARCHAR2(6) | Y |  |  |
| 59 | MNFSM_IND_EXTEMP | CHAR(1) | Y |  |  |
| 60 | MNFSM_DAT_EXTEMP | DATE | Y |  |  |
| 61 | MNFSM_DAT_COS | DATE | Y |  |  |
| 62 | CGC_CPF_REMET | VARCHAR2(16) | Y |  |  |
| 63 | CPF_CGC_DEST | VARCHAR2(16) | Y |  |  |
| 64 | COD_ESTADO_COLETA | VARCHAR2(2) | Y |  |  |
| 65 | COD_ESTADO_ENTREGA | VARCHAR2(2) | Y |  |  |
| 66 | COD_FIS_JUR | VARCHAR2(16) | Y |  |  |
| 67 | COD_VEIC_TRANSP | NUMBER | Y |  |  |
| 68 | DISTANCIA_EM_KM | NUMBER | Y |  |  |
| 69 | VLR_ALIQ_ICMS | NUMBER | Y |  |  |
| 70 | VLR_ITEM | NUMBER | Y |  |  |
| 71 | VLR_ICMS | NUMBER | Y |  |  |

**PK**: EMPS_COD, FILI_COD, MNFSM_SERIE, MNFSM_NUM, MNFSM_DTEMISS

---

## MIBGE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MIBGE_COD_MUN | VARCHAR2(7) | N |  |  |
| 2 | UNFE_SIG | CHAR(2) | Y |  |  |
| 3 | MIBGE_DESC_MUN | VARCHAR2(50) | Y |  |  |

**PK**: MIBGE_COD_MUN

---

## MIDIA_EQUIPAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EQUIPAMENTO | VARCHAR2(3) | N |  |  |
| 2 | COD_TIPO_MIDIA | VARCHAR2(3) | N |  |  |

**PK**: COD_EQUIPAMENTO, COD_TIPO_MIDIA

**FKs**:
- COD_EQUIPAMENTO → EQUIPAMENTO(COD_EQUIPAMENTO)
- COD_TIPO_MIDIA → TIPO_MIDIA(COD_TIPO_MIDIA)

---

## MIT_DADOS_ARQUIVO_JSON

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | ANO_COMPET | NUMBER(4) | N |  |  |
| 3 | TRIM_COMPET | VARCHAR2(2) | N |  |  |
| 4 | IND_TP_DECLARACAO | CHAR(1) | N |  |  |
| 5 | IND_PERIODICIDADE | VARCHAR2(2) | N |  |  |
| 6 | NUM_SEQUENCIA | NUMBER | N |  |  |
| 7 | COD_ESTAB_MATRIZ | VARCHAR2(6) | Y |  |  |
| 8 | ARQ_JSON | CLOB | N |  |  |
| 9 | DSC_NOME_ARQUIVO | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, ANO_COMPET, TRIM_COMPET, IND_TP_DECLARACAO, IND_PERIODICIDADE, NUM_SEQUENCIA

---

## MMAG_REGISTROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | TIPO_REGISTRO | VARCHAR2(4) | N |  |  |
| 3 | QUANTIDADE | NUMBER | Y |  |  |
| 4 | COD_ESTADO | VARCHAR2(2) | N | 'TD' |  |

**PK**: PROC_ID, TIPO_REGISTRO, COD_ESTADO

---

## MODALIDADE_FRETE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MFRT_COD | CHAR(3) | N |  |  |
| 2 | MFRT_DAT_ATUA | DATE | N |  |  |
| 3 | MFRT_DSC | VARCHAR2(150) | Y |  |  |

**PK**: MFRT_COD, MFRT_DAT_ATUA

**Indexes**:
- MODALIDADE_FRETEI2: (MFRT_COD)

---

## MODELO_DOCUMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | MDOC_COD | CHAR(3) | N |  |  |
| 2 | MDOC_DAT_ATUA | DATE | N |  |  |
| 3 | MDOC_DSC | VARCHAR2(150) | Y |  |  |
| 4 | MDOC_ESPECIE | VARCHAR2(6) | Y |  |  |
| 5 | MDOC_TIPO | CHAR(3) | N |  |  |

**PK**: MDOC_COD, MDOC_TIPO, MDOC_DAT_ATUA

---

## MODULO_FICHA_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_MODULO | NUMBER(12) | N |  |  |
| 2 | GRUPO_MODULO | VARCHAR2(9) | Y |  |  |
| 3 | COD_MODULO | VARCHAR2(2) | Y |  |  |
| 4 | VALID_MODULO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_MODULO

**FKs**:
- GRUPO_MODULO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_MOD_FCHFUNC (UNIQUE): (GRUPO_MODULO, COD_MODULO, VALID_MODULO)

---

## MONITOR_ARQ_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |

---

## MOV0001_CONTROL_EXCL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | num_fed_tax - TAX-BR |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | num_fed_tax - TAX-BR |
| 3 | DATA_LANCTO | DATE | N |  | dat_account_balance - TAX-BR |
| 4 | IDENT_CONTA | NUMBER(12) | N |  | cod_ledger_account - TAX-BR |
| 5 | IND_DEB_CRE | CHAR(1) | N |  | ind_account_entry_type - TAX-BR |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  | num_archiving - TAX-BR |
| 7 | NUM_LANCAMENTO | VARCHAR2(60) | Y |  |  |
| 8 | COD_CONTA | VARCHAR2(70) | Y |  | cod_ledger_account - TAX-BR |
| 9 | COD_CUSTO | VARCHAR2(50) | Y |  | cod_cost_center - TAX-BR |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO

---

## MOV0002_CONTROL_EXCL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | num_fed_tax - TAX-BR |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | num_fed_tax - TAX-BR |
| 3 | IDENT_CONTA | NUMBER(12) | N |  | cod_ledger_account - TAX-BR |
| 4 | DATA_SALDO | DATE | N |  | dat_account_balance - TAX-BR |
| 5 | IDENT_CUSTO | NUMBER(12) | N | 0 | cod_cost_center - TAX-BR |
| 6 | COD_CONTA | VARCHAR2(70) | Y |  | cod_ledger_account - TAX-BR |
| 7 | COD_CUSTO | VARCHAR2(50) | Y |  | cod_cost_center - TAX-BR |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO, IDENT_CUSTO

---

## MTT_CHUNK_JOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | ID_TASK | NUMBER(38) | N |  |  |
| 3 | STATUS | VARCHAR2(50) | N |  |  |
| 4 | JOB | VARCHAR2(100) | Y |  |  |
| 5 | LO_RID | VARCHAR2(4000) | Y |  |  |
| 6 | HI_RID | VARCHAR2(4000) | Y |  |  |
| 7 | DATE_INI_EXEC | DATE | Y |  |  |
| 8 | DATE_END_EXEC | DATE | Y |  |  |
| 9 | INI_SEQ_LOG_ERR | NUMBER | Y |  |  |

**PK**: ID, ID_TASK

**FKs**:
- ID_TASK → MTT_TASK(ID)

**Indexes**:
- UK_MTT_CHUNK_JOB (UNIQUE): (JOB)

---

## MTT_TASK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | TASK_NAME | VARCHAR2(100) | N |  |  |
| 3 | PROCESS_NUMBER | NUMBER(12) | N |  |  |

**PK**: ID

**Indexes**:
- UK_MTT_TASK (UNIQUE): (TASK_NAME)

---

## MUNICIPIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | COD_UF | NUMBER(2) | Y |  |  |
| 5 | COD_MUN_ESTADO | VARCHAR2(6) | Y |  |  |
| 6 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |
| 7 | COD_MUNIC_DIPJ | NUMBER(4) | Y |  |  |
| 8 | DESCRICAO_IBGE | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- COD_AREA_LIVR_COM → DWT_AREA_LIVR_COM(COD_AREA_LIVR_COM)

---

## MUNICIPIO_SIAFI
**Comment**: Tabela para armazenar o cadastro dos Municipios do SIAFI.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_SIAFI | VARCHAR2(5) | N |  |  |
| 2 | COD_UF_SIAFI | VARCHAR2(2) | N |  |  |
| 3 | CNPJ_SIAFI | VARCHAR2(14) | Y |  |  |
| 4 | DSC_MUNIC_SIAFI | VARCHAR2(100) | Y |  |  |

**PK**: COD_MUNIC_SIAFI, COD_UF_SIAFI

---

## MUT_SP_ALIQ_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 5 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, IDENT_DOCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## MUT_SP_GUIA_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 5 | DATA_REC_GUIA_1 | DATE | Y |  |  |
| 6 | VLR_REC_GUIA_1 | NUMBER(17,2) | Y |  |  |
| 7 | IDENT_ORG_ARRECAD1 | NUMBER(12) | Y |  |  |
| 8 | DATA_REC_GUIA_2 | DATE | Y |  |  |
| 9 | VLR_REC_GUIA_2 | NUMBER(17,2) | Y |  |  |
| 10 | IDENT_ORG_ARRECAD2 | NUMBER(12) | Y |  |  |
| 11 | OBS_GUIA_ISS | VARCHAR2(200) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, IDENT_SERVICO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- IDENT_ORG_ARRECAD1 → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)
- IDENT_ORG_ARRECAD2 → X2088_ORGAO_ARREC(IDENT_ORG_ARRECAD)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## MV_LAYOUT_SAFX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOM_TAB_WORK | VARCHAR2(8) | N |  |  |
| 2 | NUM_CAMPO | NUMBER(4) | N |  |  |
| 3 | IND_OBRIG | VARCHAR2(1) | N |  |  |
| 4 | NOME_CAMPO | VARCHAR2(30) | N |  |  |
| 5 | DATA_TYPE | VARCHAR2(128) | Y |  |  |
| 6 | DATA_LENGTH | NUMBER | N |  |  |
| 7 | GRUPO_ARQUIVO | NUMBER(2) | Y |  |  |
| 8 | NUMERO_ARQUIVO | NUMBER(3) | Y |  |  |
| 9 | IND_VALID_OBI_TABELA | VARCHAR2(1) | Y |  |  |
| 10 | IND_VALID_OBI_CAMPO | VARCHAR2(1) | Y |  |  |

**Indexes**:
- IDX_MV_LAYOUT_SAFX: (NOM_TAB_WORK)

---

## NACIONALIDADE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NACAO | NUMBER(12) | N |  |  |
| 2 | COD_NACAO | NUMBER(2) | Y |  |  |
| 3 | VALID_NACAO | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | IND_ESTRANGEIRO | CHAR(1) | Y |  |  |

**PK**: IDENT_NACAO

**Indexes**:
- IX_CHAVE_NAT_NACAO (UNIQUE): (COD_NACAO, VALID_NACAO)

---

## NATUREZA_ESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NSTQ_COD | VARCHAR2(5) | N |  |  |
| 2 | NSTQ_DAT_ATUA | DATE | N |  |  |
| 3 | NSTQ_DSC | VARCHAR2(150) | Y |  |  |
| 4 | IND_EST | CHAR(1) | Y |  |  |
| 5 | IND_INV | CHAR(1) | Y |  |  |
| 6 | IND_EST86 | CHAR(1) | Y |  |  |

**PK**: NSTQ_COD, NSTQ_DAT_ATUA

**Indexes**:
- NATUREZA_ESTOQUEI2: (NSTQ_COD)

---

## NATUREZA_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOPE_COD | VARCHAR2(10) | N |  |  |
| 2 | NOPE_DAT_ATUA | DATE | N |  |  |
| 3 | NOPE_DSC | VARCHAR2(150) | Y |  |  |
| 4 | NOPE_EXCALC_CL | CHAR(1) | Y |  |  |

**PK**: NOPE_COD, NOPE_DAT_ATUA

---

## NAT_JURIDICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NAT_JUR | VARCHAR2(4) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_NAT_JUR

---

## NOTA_SECAO_TIPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NOTA_TIPI | NUMBER(12) | N |  |  |
| 2 | COD_SECAO_TIPI | NUMBER(2) | Y |  |  |
| 3 | COD_NOTA_SEC_TIPI | NUMBER(2) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_NOTA_TIPI

**FKs**:
- COD_SECAO_TIPI → SECAO_TIPI(COD_SECAO_TIPI)

**Indexes**:
- IX_NOTA_SECAO_TIPI (UNIQUE): (COD_SECAO_TIPI, COD_NOTA_SEC_TIPI)

---

## OBRIGACAO_FISCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | IND_PERIODICIDADE | VARCHAR2(2) | Y |  |  |
| 5 | MAX_PRAZO_EMISSAO | NUMBER(3) | Y |  |  |
| 6 | MAX_PRAZ_APRES | NUMBER(3) | Y |  |  |
| 7 | IND_TER_ABE_FEC | CHAR(1) | Y |  |  |
| 8 | IND_ENFEIXAMENTO | CHAR(1) | Y |  |  |
| 9 | MAX_OSC_PERMITE | NUMBER(3) | Y |  |  |
| 10 | NUM_PROTOCOLO | VARCHAR2(40) | Y |  |  |
| 11 | DAT_LIB_PROT | DATE | Y |  |  |
| 12 | N_MESES | NUMBER(3) | Y |  |  |
| 13 | INICIAR | CHAR(1) | Y |  |  |
| 14 | MAX_CONT | NUMBER(7) | Y |  |  |
| 15 | LIVRO_I | NUMBER(6) | Y |  |  |
| 16 | PAGINA_I | NUMBER(6) | Y |  |  |
| 17 | DESLOC_I | NUMBER(6) | Y |  |  |
| 18 | IND_LIVRO_UNICO | CHAR(1) | Y |  |  |
| 19 | VLR_LIM_PAGINA | NUMBER(4) | Y |  |  |
| 20 | COMPLEMENTO_TERMO | VARCHAR2(240) | Y |  |  |
| 21 | TITULO_LIVRO | VARCHAR2(100) | Y |  | Caso esteja preenchido, será este o titulo lançado no livro fiscal no momento da emissão. Não são todos os livros que atendem a este parâmetro. |
| 22 | IND_CENTR_MARGEN | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## OBSERVACAO_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | DATA_FISCAL | DATE | Y |  |  |
| 11 | NRO_REGISTRO | NUMBER(12) | Y |  |  |
| 12 | NRO_OBSERVACAO | NUMBER(6) | Y |  |  |
| 13 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 14 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 15 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 16 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 18 | NRO_FOLHA | NUMBER(6) | Y |  |  |

**Indexes**:
- IX_OBS_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)

---

## OBSERVACAO_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | DATA_FISCAL | DATE | Y |  |  |
| 11 | NRO_REGISTRO | NUMBER(12) | Y |  |  |
| 12 | NRO_OBSERVACAO | NUMBER(6) | Y |  |  |
| 13 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 14 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 15 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 16 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 18 | NRO_FOLHA | NUMBER(6) | Y |  |  |

**Indexes**:
- IX_OBS_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_FISCAL)

---

## OBSERVACAO_P2_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | NRO_OBSERVACAO | NUMBER(6) | Y |  |  |
| 6 | DSC_OBSERVACAO1 | VARCHAR2(45) | Y |  |  |
| 7 | DSC_OBSERVACAO2 | VARCHAR2(45) | Y |  |  |
| 8 | DSC_OBSERVACAO3 | VARCHAR2(45) | Y |  |  |
| 9 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 11 | NRO_FOLHA | NUMBER(6) | Y |  |  |

**Indexes**:
- IX_OBS_P2_CONS: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## OBS_MOTIVO_NOTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 2 | COD_MOTIVO | VARCHAR2(10) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | IND_EXIGE_OBS | CHAR(1) | Y |  |  |

**PK**: COD_MUNIC_ISS, COD_MOTIVO

**FKs**:
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)

---

## OLSS_CONTROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TABELA | VARCHAR2(10) | N |  |  |
| 5 | NOM_ARQ | VARCHAR2(20) | Y |  |  |
| 6 | TAM_MAX_ARQ | NUMBER(8) | Y |  |  |
| 7 | DSC_DIRETORIO | VARCHAR2(500) | Y |  |  |
| 8 | DAT_ULT_EXP_OK | DATE | Y |  |  |
| 9 | IND_SALDO_INI_X02 | CHAR(1) | Y |  |  |

**PK**: COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TABELA

**FKs**:
- COD_EMPRESA, COD_PROG → OLSS_PROG(COD_EMPRESA, COD_PROG)

---

## OLSS_DE_PARA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_TIPO_IN | VARCHAR2(4) | N |  |  |
| 2 | NOME_LOGICO_ARQ | VARCHAR2(8) | N |  |  |
| 3 | IND_LAYOUT | CHAR(1) | N |  |  |
| 4 | NUM_COLUNA | NUMBER(2) | N |  |  |
| 5 | IND_MANUAL | VARCHAR2(1) | N |  |  |
| 6 | VERSAO | NUMBER(5) | N |  |  |
| 7 | COD_ARQUIVO | VARCHAR2(12) | N |  |  |
| 8 | TIPO_REGISTRO | VARCHAR2(4) | N |  |  |
| 9 | NUM_ITEM | NUMBER(4) | N |  |  |
| 10 | NUM_REGRA | NUMBER(3) | Y |  |  |
| 11 | REGRA_CONCAT | CHAR(1) | Y |  |  |

**PK**: IND_TIPO_IN, NOME_LOGICO_ARQ, IND_LAYOUT, NUM_COLUNA, IND_MANUAL, VERSAO, COD_ARQUIVO, TIPO_REGISTRO, NUM_ITEM

---

## OLSS_EBT_CONTROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PROG | NUMBER(12) | N |  |  |
| 4 | DAT_PROG | DATE | N |  |  |
| 5 | COD_TABELA | VARCHAR2(10) | N |  |  |
| 6 | IND_FECH_GRP | CHAR(1) | Y |  |  |
| 7 | IND_FECH_CALEND | CHAR(1) | Y |  |  |
| 8 | IND_COPIA | CHAR(1) | Y |  |  |
| 9 | IND_VALID_COPIA | CHAR(1) | Y |  |  |
| 10 | IND_CONFIRMA_EXCL | CHAR(1) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PROG, DAT_PROG, COD_TABELA

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_PROG, DAT_PROG → OLSS_EBT_PROG(COD_EMPRESA, COD_ESTAB, COD_PROG, DAT_PROG)

---

## OLSS_EBT_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PROG | NUMBER(12) | N |  |  |
| 4 | COD_TABELA | VARCHAR2(10) | N |  |  |
| 5 | DAT_PROG | DATE | N |  |  |
| 6 | DAT_INI_PERIODO | DATE | Y |  |  |
| 7 | DAT_FIM_PERIODO | DATE | Y |  |  |
| 8 | DSC_PROG | VARCHAR2(50) | Y |  |  |
| 9 | IND_FECH_GRP | CHAR(1) | Y |  |  |
| 10 | IND_FECH_CALEND | CHAR(1) | Y |  |  |
| 11 | IND_COPIA | CHAR(1) | Y |  |  |
| 12 | IND_VALID_COPIA | CHAR(1) | Y |  |  |
| 13 | IND_CONFIRMA_EXCL | CHAR(1) | Y |  |  |
| 14 | NUM_REG_EXCL | NUMBER(20) | Y |  |  |
| 15 | USUARIO_PROG | VARCHAR2(40) | Y |  |  |
| 16 | DAT_EXCL | DATE | Y |  |  |
| 17 | USUARIO_EXCL | VARCHAR2(40) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | STATUS | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PROG, COD_TABELA, DAT_PROG

---

## OLSS_EBT_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PROG_PAR | NUMBER(12) | N |  |  |
| 4 | COD_TABELA | VARCHAR2(10) | N |  |  |
| 5 | DSC_PARAM | VARCHAR2(50) | Y |  |  |
| 6 | DAT_PROG_PAR | DATE | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PROG_PAR, COD_TABELA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## OLSS_EBT_PROG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PROG | NUMBER(12) | N |  |  |
| 4 | DAT_PROG | DATE | N |  |  |
| 5 | DAT_INI_PERIODO | DATE | Y |  |  |
| 6 | DAT_FIM_PERIODO | DATE | Y |  |  |
| 7 | DSC_PROG | VARCHAR2(50) | Y |  |  |
| 8 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PROG, DAT_PROG

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## OLSS_HISTORICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_TABELA | VARCHAR2(10) | N |  |  |
| 5 | DAT_ARQUIVO | DATE | N |  |  |
| 6 | DAT_EXPORT | DATE | N |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | STATUS | NUMBER(2) | Y |  |  |
| 9 | IND_VALID_COPIA | CHAR(1) | Y |  |  |
| 10 | DAT_INI_PERIODO | DATE | Y |  |  |
| 11 | DAT_FIM_PERIODO | DATE | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_PROG, COD_EMPRESA, COD_ESTAB, COD_TABELA, DAT_ARQUIVO, DAT_EXPORT

**FKs**:
- COD_EMPRESA, COD_PROG → OLSS_PROG(COD_EMPRESA, COD_PROG)

---

## OLSS_MM_X42

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | VALID_FIS_JUR | DATE | N |  |  |
| 10 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 11 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | COD_MODELO_DOC | VARCHAR2(2) | Y |  |  |
| 14 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 21 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |
| 22 | SITUACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_FIS_JUR, COD_FIS_JUR, VALID_FIS_JUR

---

## OLSS_MM_X43

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | VALID_FIS_JUR | DATE | N |  |  |
| 10 | NUM_ITEM | NUMBER(5) | N |  |  |
| 11 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 12 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 14 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TRIB_ICMSS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_FIS_JUR, COD_FIS_JUR, VALID_FIS_JUR, NUM_ITEM

---

## OLSS_PROG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_PROG | NUMBER(12) | N |  |  |
| 3 | DSC_PROG | VARCHAR2(50) | Y |  |  |
| 4 | IND_PERIOD | CHAR(1) | Y |  |  |
| 5 | DT_INI_EVENT | DATE | Y |  |  |
| 6 | DSC_DIRETORIO | VARCHAR2(500) | Y |  |  |
| 7 | EXT_ARQ | VARCHAR2(3) | Y |  |  |
| 8 | TAM_MAX_ARQ | NUMBER(8) | Y |  |  |
| 9 | IND_ARQ_DATA | CHAR(1) | Y |  |  |
| 10 | COD_PROG_SEMANAL | VARCHAR2(7) | Y |  |  |
| 11 | COD_PROG_MENSAL | VARCHAR2(64) | Y |  |  |
| 12 | DAT_INI_PERIODO | DATE | Y |  |  |
| 13 | DAT_FIM_PERIODO | DATE | Y |  |  |
| 14 | IND_EXEC_NOK | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_PROG

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## OMS_INTG_CONTRACT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CONTRACT_ID | NUMBER | N |  |  |
| 2 | TABLE_ID | NUMBER | N |  |  |
| 3 | START_DATE | DATE | N |  |  |
| 4 | END_DATE | DATE | Y |  |  |
| 5 | SIGNATURE | VARCHAR2(128) | Y |  |  |
| 6 | ACTIVE | CHAR(1) | N | UPPER('N') |  |
| 7 | CREATED_AT | TIMESTAMP(6) | N | CURRENT_TIMESTAMP |  |
| 8 | UPDATED_AT | TIMESTAMP(6) | N | CURRENT_TIMESTAMP |  |

**PK**: CONTRACT_ID

**FKs**:
- TABLE_ID → OMS_INTG_TABLE(TABLE_ID)

**Indexes**:
- UK1_OMS_INTG_CONTRACT (UNIQUE): (SIGNATURE)
- UK2_OMS_INTG_CONTRACT (UNIQUE): (CONTRACT_ID, TABLE_ID)

---

## OMS_INTG_CONTRACT_COLS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CONTRACT_COL_ID | NUMBER | N |  |  |
| 2 | CONTRACT_ID | NUMBER | N |  |  |
| 3 | TABLE_ID | NUMBER | N |  |  |
| 4 | COLUMN_ID | NUMBER | N |  |  |
| 5 | COLUMN_NAME | VARCHAR2(128) | N |  |  |
| 6 | DATA_TYPE | VARCHAR2(128) | Y |  |  |
| 7 | DATA_LENGTH | NUMBER | N |  |  |
| 8 | DATA_PRECISION | NUMBER | Y |  |  |
| 9 | DATA_SCALE | NUMBER | Y |  |  |
| 10 | NULLABLE | CHAR(1) | N | UPPER('Y') |  |
| 11 | CREATED_AT | TIMESTAMP(6) | N | CURRENT_TIMESTAMP |  |
| 12 | UPDATED_AT | TIMESTAMP(6) | N | CURRENT_TIMESTAMP |  |

**PK**: CONTRACT_COL_ID

**FKs**:
- CONTRACT_ID → OMS_INTG_CONTRACT(CONTRACT_ID)
- TABLE_ID → OMS_INTG_TABLE(TABLE_ID)

**Indexes**:
- UK1_OMS_INTG_CONTRACT_COLS (UNIQUE): (CONTRACT_ID, TABLE_ID, COLUMN_ID)

---

## OMS_INTG_EXTRACTION

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EXTRACTION_ID | NUMBER | N |  |  |
| 2 | CONTRACT_ID | NUMBER | N |  |  |
| 3 | EXPECTED_ROWS | NUMBER | Y |  |  |
| 4 | EXTRACTED_ROWS | NUMBER | Y |  |  |
| 5 | STARTED_AT | TIMESTAMP(6) | N | CURRENT_TIMESTAMP |  |
| 6 | FINISHED_OK | CHAR(1) | N | UPPER('N') |  |
| 7 | FINISHED_AT | TIMESTAMP(6) | Y |  |  |

**PK**: EXTRACTION_ID

**FKs**:
- CONTRACT_ID → OMS_INTG_CONTRACT(CONTRACT_ID)

---

## OMS_INTG_IGNORED_COLS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TABLE_ID | NUMBER | N |  |  |
| 2 | COLUMN_ID | NUMBER | N |  |  |

**PK**: TABLE_ID, COLUMN_ID

**FKs**:
- TABLE_ID → OMS_INTG_TABLE(TABLE_ID)

---

## OMS_INTG_TABLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TABLE_ID | NUMBER | N |  |  |
| 2 | TABLE_NAME | VARCHAR2(128) | N |  |  |
| 3 | ROWS_LIMIT | NUMBER | N | -1 |  |
| 4 | CREATED_AT | TIMESTAMP(6) | N | CURRENT_TIMESTAMP |  |
| 5 | UPDATED_AT | TIMESTAMP(6) | N | CURRENT_TIMESTAMP |  |

**PK**: TABLE_ID

**Indexes**:
- UK1_OMS_INTG_TABLE (UNIQUE): (TABLE_NAME)

---

## OPERACAO_APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 2 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 3 | DSC_OPER_APUR | VARCHAR2(100) | Y |  |  |
| 4 | IND_DIG_DISCRIM | CHAR(1) | Y |  |  |
| 5 | IND_UTIL_TIPO_DED | CHAR(1) | Y |  |  |
| 6 | IND_TIPO_OPERACAO | CHAR(1) | Y |  |  |
| 7 | COD_OP_AP_SUB_TOT | VARCHAR2(5) | Y |  |  |
| 8 | COD_OP_AP_PER_ANT | VARCHAR2(5) | Y |  |  |
| 9 | COD_CLASSE | VARCHAR2(3) | Y |  |  |

**PK**: COD_TIPO_LIVRO, COD_OPER_APUR

**FKs**:
- COD_TIPO_LIVRO → TIPO_LIVRO_APURAC(COD_TIPO_LIVRO)
- COD_TIPO_LIVRO, COD_OP_AP_SUB_TOT → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)
- COD_TIPO_LIVRO, COD_OP_AP_PER_ANT → OPERACAO_APURACAO(COD_TIPO_LIVRO, COD_OPER_APUR)

**Indexes**:
- IX_OPER_DEFAULT: (COD_TIPO_LIVRO, IND_DIG_DISCRIM, IND_TIPO_OPERACAO)

---

## OP_INTERESTADO_P12

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
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS_S | NUMBER(17,2) | Y |  |  |
| 16 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 17 | VLR_NAO_TRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 18 | OBS_TRIBUTO | VARCHAR2(45) | Y |  |  |
| 19 | NRO_OBSERVACAO | NUMBER(5) | Y |  |  |
| 20 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 21 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 22 | IND_CONTEM_OBS | CHAR(1) | Y |  |  |
| 23 | VLR_BASE_ICMS_S | NUMBER(17,2) | Y |  |  |
| 24 | VLR_DESP_ACESS | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_OP_INTER_P12: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)

---

## OTF_COMP_RETENCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | CPF_CGC_FORNECEDOR | VARCHAR2(14) | N |  |  |
| 5 | RAZAO_SOCIAL_FORNECEDOR | VARCHAR2(70) | Y |  |  |
| 6 | EMAIL | VARCHAR2(255) | Y |  |  |
| 7 | CNPJ_ESTABELECIMENTO | VARCHAR2(14) | Y |  |  |
| 8 | GRUPO_RETENCAO | VARCHAR2(9) | Y |  |  |
| 9 | IND_MENSAGEM | VARCHAR2(1) | Y | 'N' | <S> para mensagem de desconsiderar o comprovante enviado anteriormente |
| 10 | COD_USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB, CPF_CGC_FORNECEDOR

---

## OUT_ATOCOTEPE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | REG | VARCHAR2(1000) | N |  |  |
| 2 | SQL | CLOB | Y |  |  |
| 3 | PARM | CLOB | Y |  |  |

---

## PACKAGE_EXECUTION_CONTROL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PACKAGE_NAME | VARCHAR2(100) | N |  |  |
| 2 | IS_RUNNING | CHAR(1) | Y |  |  |

**Indexes**:
- PK_PACKAGE_NAME (UNIQUE): (PACKAGE_NAME)

---

## PAGINA_LIVRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | SEQUENCIAL | NUMBER(7) | N |  |  |
| 5 | LIVRO | NUMBER(6) | Y |  |  |
| 6 | PAGINA | NUMBER(6) | Y |  |  |
| 7 | TERMO | CHAR(1) | Y |  |  |
| 8 | DESLOC | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, SEQUENCIAL

---

## PAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PAIS | VARCHAR2(3) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(35) | Y |  |  |
| 3 | DESCR_NACION | VARCHAR2(35) | Y |  |  |
| 4 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 5 | DIG_VERIFICADOR | NUMBER(1) | Y |  |  |
| 6 | COD_PAIS_GIA_RS | VARCHAR2(3) | Y |  |  |
| 7 | IND_TRIBUT_FAVOREC | CHAR(1) | Y |  |  |
| 8 | SIGLA_PAIS | VARCHAR2(3) | Y |  | BRA, USA,... |

**PK**: COD_PAIS

---

## PAISES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PAIS_COD | CHAR(3) | N |  |  |
| 2 | PAIS_DESC | VARCHAR2(150) | Y |  |  |
| 3 | PAIS_COD_DIPJ | CHAR(3) | Y |  |  |
| 4 | PAIS_COD_BCB | VARCHAR2(5) | Y |  |  |
| 5 | PAIS_COD_GIARS | CHAR(3) | Y |  |  |

**PK**: PAIS_COD

---

## PAIS_ESTADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_PAIS | VARCHAR2(3) | N |  |  |
| 3 | COD_PAIS_ESTADO | VARCHAR2(3) | Y |  |  |

**PK**: IDENT_ESTADO, COD_PAIS

**FKs**:
- COD_PAIS → PAIS(COD_PAIS)

---

## PARAMETROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VARIAVEL | VARCHAR2(30) | N |  |  |
| 2 | DSC_VARIAVEL | VARCHAR2(100) | Y |  |  |
| 3 | DSC_CONTEUDO | VARCHAR2(100) | Y |  |  |
| 4 | DSC_NATUREZA | CHAR(1) | Y |  |  |
| 5 | TAG_VARIAVEL | VARCHAR2(200) | Y |  |  |

**PK**: COD_VARIAVEL

---

## PARAMETRO_CONTABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | UTILIZA_Z | VARCHAR2(2) | Y |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |

**PK**: ID

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## PAR_PRD_CAT42_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | IDENT_MEDIDA | NUMBER(12) | N |  |  |
| 6 | QTDE_NF_SAIDA | NUMBER | Y |  |  |
| 7 | QTDE_NF_ENTR | NUMBER | Y |  |  |
| 8 | DATA_FISCAL | DATE | N |  |  |

**PK**: NUM_PROCESSO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, IDENT_MEDIDA, DATA_FISCAL

**Indexes**:
- IX_PAR_PRD_CAT42_TEMP: (GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, IDENT_MEDIDA, DATA_FISCAL)

---

## PBCATCOL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PBC_TNAM | VARCHAR2(60) | N |  |  |
| 2 | PBC_TID | NUMBER | Y |  |  |
| 3 | PBC_OWNR | VARCHAR2(60) | N |  |  |
| 4 | PBC_CNAM | VARCHAR2(60) | N |  |  |
| 5 | PBC_CID | NUMBER | Y |  |  |
| 6 | PBC_LABL | VARCHAR2(254) | Y |  |  |
| 7 | PBC_LPOS | NUMBER | Y |  |  |
| 8 | PBC_HDR | VARCHAR2(254) | Y |  |  |
| 9 | PBC_HPOS | NUMBER | Y |  |  |
| 10 | PBC_JTFY | NUMBER | Y |  |  |
| 11 | PBC_MASK | VARCHAR2(61) | Y |  |  |
| 12 | PBC_CASE | NUMBER | Y |  |  |
| 13 | PBC_HGHT | NUMBER | Y |  |  |
| 14 | PBC_WDTH | NUMBER | Y |  |  |
| 15 | PBC_PTRN | VARCHAR2(61) | Y |  |  |
| 16 | PBC_BMAP | CHAR(1) | Y |  |  |
| 17 | PBC_INIT | VARCHAR2(254) | Y |  |  |
| 18 | PBC_CMNT | VARCHAR2(254) | Y |  |  |
| 19 | PBC_EDIT | VARCHAR2(61) | Y |  |  |
| 20 | PBC_TAG | VARCHAR2(254) | Y |  |  |

**Indexes**:
- PBSYSCATCOLDICT_IDX (UNIQUE): (PBC_TNAM, PBC_OWNR, PBC_CNAM)

---

## PBCATEDT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PBE_NAME | VARCHAR2(60) | Y |  |  |
| 2 | PBE_EDIT | VARCHAR2(254) | Y |  |  |
| 3 | PBE_TYPE | NUMBER | Y |  |  |
| 4 | PBE_CNTR | NUMBER | Y |  |  |
| 5 | PBE_SEQN | NUMBER | Y |  |  |
| 6 | PBE_FLAG | NUMBER | Y |  |  |
| 7 | PBE_WORK | VARCHAR2(32) | Y |  |  |

**Indexes**:
- PBSYSPBE_IDX (UNIQUE): (PBE_NAME, PBE_SEQN)

---

## PBCATFMT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PBF_NAME | VARCHAR2(60) | Y |  |  |
| 2 | PBF_FRMT | VARCHAR2(254) | Y |  |  |
| 3 | PBF_TYPE | NUMBER | N |  |  |
| 4 | PBF_CNTR | NUMBER | Y |  |  |

**Indexes**:
- PBSYSCATFRMTS_IDX (UNIQUE): (PBF_NAME)

---

## PBCATTBL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PBT_TNAM | VARCHAR2(60) | N |  |  |
| 2 | PBT_TID | NUMBER | Y |  |  |
| 3 | PBT_OWNR | VARCHAR2(60) | N |  |  |
| 4 | PBD_FHGT | NUMBER | Y |  |  |
| 5 | PBD_FWGT | NUMBER | Y |  |  |
| 6 | PBD_FITL | CHAR(1) | Y |  |  |
| 7 | PBD_FUNL | CHAR(1) | Y |  |  |
| 8 | PBD_FCHR | NUMBER | Y |  |  |
| 9 | PBD_FPTC | NUMBER | Y |  |  |
| 10 | PBD_FFCE | VARCHAR2(36) | Y |  |  |
| 11 | PBH_FHGT | NUMBER | Y |  |  |
| 12 | PBH_FWGT | NUMBER | Y |  |  |
| 13 | PBH_FITL | CHAR(1) | Y |  |  |
| 14 | PBH_FUNL | CHAR(1) | Y |  |  |
| 15 | PBH_FCHR | NUMBER | Y |  |  |
| 16 | PBH_FPTC | NUMBER | Y |  |  |
| 17 | PBH_FFCE | VARCHAR2(36) | Y |  |  |
| 18 | PBL_FHGT | NUMBER | Y |  |  |
| 19 | PBL_FWGT | NUMBER | Y |  |  |
| 20 | PBL_FITL | CHAR(1) | Y |  |  |
| 21 | PBL_FUNL | CHAR(1) | Y |  |  |
| 22 | PBL_FCHR | NUMBER | Y |  |  |
| 23 | PBL_FPTC | NUMBER | Y |  |  |
| 24 | PBL_FFCE | VARCHAR2(36) | Y |  |  |
| 25 | PBT_CMNT | VARCHAR2(254) | Y |  |  |

**Indexes**:
- PBSYSCATPBT_IDX (UNIQUE): (PBT_TNAM, PBT_OWNR)

---

## PBCATVLD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PBV_NAME | VARCHAR2(60) | Y |  |  |
| 2 | PBV_VALD | VARCHAR2(254) | Y |  |  |
| 3 | PBV_TYPE | NUMBER | Y |  |  |
| 4 | PBV_CNTR | NUMBER | Y |  |  |
| 5 | PBV_MSG | VARCHAR2(254) | Y |  |  |

**Indexes**:
- PBSYSCATVLDS_IDX (UNIQUE): (PBV_NAME)

---

## PLANO_CONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | PCON_COD_CONTA | VARCHAR2(70) | N |  |  |
| 4 | PCON_DAT_ATUA | DATE | N |  |  |
| 5 | PCON_TIP_CONTA | CHAR(1) | Y |  |  |
| 6 | PCON_COD_CMASTER | VARCHAR2(70) | Y |  |  |
| 7 | PCON_DSC_CONTA | VARCHAR2(150) | Y |  |  |
| 8 | PCON_NIVEL | CHAR(1) | Y |  |  |
| 9 | NUM01 | NUMBER | Y |  |  |
| 10 | NUM02 | NUMBER | Y |  |  |
| 11 | NUM03 | NUMBER | Y |  |  |
| 12 | VAR01 | VARCHAR2(150) | Y |  |  |
| 13 | VAR02 | VARCHAR2(150) | Y |  |  |
| 14 | VAR03 | VARCHAR2(150) | Y |  |  |
| 15 | VAR04 | VARCHAR2(150) | Y |  |  |
| 16 | VAR05 | VARCHAR2(150) | Y |  |  |
| 17 | PCON_NIVEL_CON | NUMBER(2) | Y |  |  |
| 18 | PCON_TIP_ESCON | CHAR(1) | Y |  |  |
| 19 | PCON_DGERAL | VARCHAR2(28) | Y |  |  |
| 20 | PCON_NAT_CON | CHAR(1) | Y |  |  |

**PK**: EMPS_COD, FILI_COD, PCON_COD_CONTA, PCON_DAT_ATUA

**Indexes**:
- PLANO_CONTASI2: (EMPS_COD, PCON_COD_CMASTER, PCON_COD_CONTA, PCON_DAT_ATUA)

---

## PLT_ANEG_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_AREA_NEGOC | VARCHAR2(9) | N |  |  |
| 2 | COD_AREA_NEGOC | VARCHAR2(10) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: GRUPO_AREA_NEGOC, COD_AREA_NEGOC, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PLT_CALC_TRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 3 | ESP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 4 | DAT_APURAC | DATE | N |  |  |
| 5 | DAT_INI | DATE | Y |  |  |
| 6 | DAT_FIM | DATE | Y |  |  |
| 7 | DAT_EVENTO | DATE | Y |  |  |
| 8 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 9 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 10 | IND_TP_INFORM | CHAR(1) | Y |  |  |
| 11 | IND_SOMA | CHAR(1) | Y |  |  |
| 12 | VLR_BASE_CALC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ALIQ | NUMBER(7,4) | Y |  |  |
| 14 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_TRIBUTO, ESP_TRIBUTO, DAT_APURAC

**FKs**:
- COD_TRIBUTO, ESP_TRIBUTO → DWT_TRIBUTO_ESP(COD_TRIBUTO, ESP_TRIBUTO)

---

## PLT_EMIT_REL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_REL | VARCHAR2(2) | N |  |  |
| 2 | DSC_EMIT | VARCHAR2(50) | Y |  |  |

**PK**: COD_REL

---

## PLT_ESTAB_TRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 4 | ESP_TRIBUTO | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, ESP_TRIBUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## PLT_PAR_CONTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 3 | ESP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 4 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 6 | IND_TP_INFORM | CHAR(1) | Y |  |  |
| 7 | IND_SOMA | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_TRIBUTO, ESP_TRIBUTO, GRUPO_CONTA, COD_CONTA

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## PLT_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## PLT_SERVICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 2 | COD_SERVICO | VARCHAR2(4) | N |  |  |

**PK**: GRUPO_SERVICO, COD_SERVICO

---

## PLT_UNEG_CRESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_UNID_NEGOC | VARCHAR2(9) | N |  |  |
| 2 | COD_UNID_NEGOC | VARCHAR2(20) | N |  |  |
| 3 | GRUPO_CENTRO_RESP | VARCHAR2(9) | N |  |  |
| 4 | COD_CENTRO_RESP | VARCHAR2(20) | N |  |  |

**PK**: GRUPO_UNID_NEGOC, COD_UNID_NEGOC, GRUPO_CENTRO_RESP, COD_CENTRO_RESP

---

## PRECO_MEDIO_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PMEDS_DAT_ATUA | DATE | N |  |  |
| 2 | PMEDS_COD_INSUMO | VARCHAR2(40) | N |  |  |
| 3 | PMEDS_COD_ITEM | VARCHAR2(65) | N |  |  |
| 4 | PMEDS_VAL_SAI | NUMBER | Y |  |  |

**PK**: PMEDS_DAT_ATUA, PMEDS_COD_INSUMO, PMEDS_COD_ITEM

---

## PROCESSO_CUSTOMIZADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PROCESSO_CUSTOMIZADO | NUMBER(7) | N |  |  |
| 2 | NOME_PROCESSO | VARCHAR2(50) | Y |  |  |
| 3 | IND_ATIVO | CHAR(1) | Y |  |  |

**PK**: ID_PROCESSO_CUSTOMIZADO

---

## PROCESSO_GRUPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PROCESSO_CUSTOMIZADO | NUMBER(7) | N |  |  |
| 2 | GRP_KEY | NUMBER | N |  |  |
| 3 | USR_KEY | NUMBER | Y |  |  |

**PK**: ID_PROCESSO_CUSTOMIZADO, GRP_KEY

**FKs**:
- ID_PROCESSO_CUSTOMIZADO → PROCESSO_CUSTOMIZADO(ID_PROCESSO_CUSTOMIZADO)

---

## PROCESS_TENANT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PROCESS_TENANT | NUMBER(22) | N |  |  |
| 2 | SCHEDULE_DATE | DATE | Y |  |  |
| 3 | PROCESS | CLOB | Y |  |  |
| 4 | STATUS | VARCHAR2(1) | Y | '0' | Status = 0 (Nao Lido), Status = 1 (Executado), Status = 3 (Erro)  |
| 5 | PROCESS_TYPE | VARCHAR2(1) | Y | 'J' |  |

**PK**: ID_PROCESS_TENANT

---

## PROTOCOLO_CARGA_ARQUIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROTOCOLO | VARCHAR2(80) | N |  |  |
| 2 | STATUS | NUMBER(1) | N |  |  |
| 3 | DAT_REQUEST | DATE | N |  |  |
| 4 | CONTEUDO_ARQUIVO | CLOB | N |  |  |

**PK**: NUM_PROTOCOLO

---

## PR_INTERESTADO_P13

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI | DATE | Y |  |  |
| 4 | DATA_FIM | DATE | Y |  |  |
| 5 | DATA_FISCAL | DATE | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 13 | MODALIDADE_FRETE | CHAR(3) | Y |  |  |
| 14 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | COD_DOCTO_TRANSP | VARCHAR2(5) | Y |  |  |
| 17 | NUM_DOCFIS_TRANSP | VARCHAR2(12) | Y |  |  |
| 18 | SER_DOCFIS_TRANSP | VARCHAR2(3) | Y |  |  |
| 19 | S_SER_DOCFIS_TRANS | VARCHAR2(2) | Y |  |  |
| 20 | INSC_UF_REMET | VARCHAR2(14) | Y |  |  |
| 21 | RAZAO_REMET | VARCHAR2(70) | Y |  |  |
| 22 | CGC_CPF_REMET | VARCHAR2(14) | Y |  |  |
| 23 | INSC_ESTADUAL_DEST | VARCHAR2(14) | Y |  |  |
| 24 | RAZAO_DEST | VARCHAR2(70) | Y |  |  |
| 25 | CPF_CGC_DEST | VARCHAR2(14) | Y |  |  |
| 26 | DATA_EMISSAO_TRANS | DATE | Y |  |  |
| 27 | VLR_TOT_DOCFIS | NUMBER(17,2) | Y |  |  |
| 28 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 29 | CIDADE | VARCHAR2(30) | Y |  |  |
| 30 | CEP | VARCHAR2(8) | Y |  |  |
| 31 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 32 | OBS_FRETE | VARCHAR2(45) | Y |  |  |
| 33 | OBS_TRIB | VARCHAR2(45) | Y |  |  |
| 34 | NR_OBSERVACAO | NUMBER(12) | Y |  |  |
| 35 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 36 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 37 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 38 | DSC_ESTADO | VARCHAR2(50) | Y |  |  |

**Indexes**:
- IX_PRINTER_P13: (COD_EMPRESA, COD_ESTAB)
- IX_PR_P13: (COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM)

---

## RCP_CAD_MED
**Comment**: Tabela utilizada no RCP - MG para armazenamento dos códigos de medida (medida da x2007, ou a medida padrão da x2017), p/ geração do registro 0250.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 3 | COD_MEDIDA | VARCHAR2(8) | N |  |  |
| 4 | IND_TAB_ORIGEM | VARCHAR2(5) | Y |  | Indicador da tabela origem da medida. Domínio: X2007: medida da X2007_MEDIDA; X2017: unidade padrão da X2017_UND_PADRAO. |

**PK**: PROC_ID, GRUPO_MEDIDA, COD_MEDIDA

---

## RCP_CAD_PARTIC
**Comment**: Tabela utilizada no RCP - MG para armazenamento das pessoas fis/jur, p/ geração do registro 0150.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |

**PK**: PROC_ID, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

**Indexes**:
- IX_RCP_CAD_PARTIC: (PROC_ID, IND_FIS_JUR, COD_FIS_JUR)

---

## RCP_CAD_PROD
**Comment**: Tabela utilizada no RCP - MG para armazenamento dos Produtos, p/ geração do registro 0200.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | TIPO_ITEM | NUMBER(2) | Y |  |  |
| 6 | IND_INSUMO | CHAR(1) | Y |  |  |

**PK**: PROC_ID, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

---

## RCP_CONV_MED
**Comment**: Tabela utilizada no RCP - MG para armazenamento dos códigos de conversão de unidade de medida, p/ geração do registro 0220.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_ITEM | VARCHAR2(60) | N |  |  |
| 3 | GRUPO_MEDIDA_EST | VARCHAR2(9) | N |  |  |
| 4 | COD_MEDIDA_EST | VARCHAR2(8) | N |  |  |
| 5 | COD_ITEM_ORIGEM | VARCHAR2(60) | N |  |  |
| 6 | GRUPO_MEDIDA_ORI | VARCHAR2(9) | N |  |  |
| 7 | COD_MEDIDA_ORI | VARCHAR2(8) | N |  |  |
| 8 | IND_GERA_MSG | CHAR(1) | Y |  |  |

**PK**: PROC_ID, COD_ITEM, GRUPO_MEDIDA_EST, COD_MEDIDA_EST, COD_ITEM_ORIGEM, GRUPO_MEDIDA_ORI, COD_MEDIDA_ORI

---

## RCP_DADOS_INICIAIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_DESCR_PROD | CHAR(1) | Y |  |  |
| 4 | IND_DAT_SALDO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## RCP_FASE_CONV_MED
**Comment**: Tabela utilizada no RCPE - MG para armazenamento dos códigos de fase de produção, dos produtos e das medidas p/ geração do registro H265.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_FASE_PROD | VARCHAR2(20) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | CHAR(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, COD_FASE_PROD, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_MEDIDA, COD_MEDIDA

---

## RCP_FASE_PROD
**Comment**: Tabela utilizada no RCPE - MG para armazenamento dos códigos de fase de produção, p/ geração do registro H260.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_FASE_PROD | VARCHAR2(20) | N |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, COD_FASE_PROD

---

## RCP_REG_H200
**Comment**: Tabela utilizada no RCPE - MG para armazenamento dos registros a serem gerados no H200.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | IND_OPE | CHAR(1) | N |  |  |
| 8 | TIPO_MOV | VARCHAR2(2) | N |  |  |
| 9 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 10 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 11 | GRUPO_UND_PADRAO | VARCHAR2(9) | Y |  |  |
| 12 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 13 | IND_DOC_OPE | CHAR(1) | Y |  |  |
| 14 | DSC_FINALIDADE | VARCHAR2(255) | N | ' ' |  |
| 15 | QTD_CAP_MAX_ARMAZ | NUMBER(17,6) | Y |  |  |
| 16 | DATA_INI_H100 | DATE | Y |  |  |
| 17 | DATA_FIM_H100 | DATE | Y |  |  |
| 18 | VLR_TOT_INI | NUMBER(17,2) | Y |  |  |
| 19 | QUANTIDADE_INI | NUMBER(17,6) | Y |  |  |
| 20 | VLR_TOT_ENT | NUMBER(17,2) | Y |  |  |
| 21 | QUANTIDADE_ENT | NUMBER(17,6) | Y |  |  |
| 22 | VLR_TOT_SAI | NUMBER(17,2) | Y |  |  |
| 23 | QUANTIDADE_SAI | NUMBER(17,6) | Y |  |  |
| 24 | VLR_TOT_FIM | NUMBER(17,2) | Y |  |  |
| 25 | QUANTIDADE_FIM | NUMBER(17,6) | Y |  |  |
| 26 | PROC_ID | NUMBER | Y |  |  |
| 27 | CLAS_ITEM | VARCHAR2(2) | Y |  |  |

**PK**: DATA_MOVTO, COD_ESTAB, COD_EMPRESA, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, IND_OPE, TIPO_MOV, GRUPO_CUSTO, COD_CUSTO, DSC_FINALIDADE

---

## RCP_REG_H270

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI_APUR | DATE | N |  |  |
| 4 | DAT_FIM_APUR | DATE | N |  |  |
| 5 | DAT_INI_ERRO | DATE | N |  |  |
| 6 | DAT_FIM_ERRO | DATE | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 8 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 9 | QTDE_ACERTO_POS | NUMBER(17,3) | Y |  |  |
| 10 | QTDE_ACERTO_NEG | NUMBER(17,3) | Y |  |  |
| 11 | COD_FASE_PRODUCAO | VARCHAR2(20) | N |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | DAT_OPERACAO | DATE | Y |  |  |
| 14 | COD_ORDEM | VARCHAR2(15) | Y |  |  |
| 15 | COD_DIF_PROD | VARCHAR2(15) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIM_APUR, DAT_INI_ERRO, DAT_FIM_ERRO, IDENT_PRODUTO, COD_FASE_PRODUCAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## RCP_REG_H275

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI_APUR | DATE | N |  |  |
| 4 | DAT_FIM_APUR | DATE | N |  |  |
| 5 | DAT_INI_ERRO | DATE | N |  |  |
| 6 | DAT_FIM_ERRO | DATE | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 8 | COD_FASE_PRODUCAO | VARCHAR2(20) | N |  |  |
| 9 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 10 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 11 | QTDE_ACERTO_POS | NUMBER(17,3) | Y |  |  |
| 12 | QTDE_ACERTO_NEG | NUMBER(17,3) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | DAT_OPERACAO | DATE | Y |  |  |
| 15 | IDENT_INS_SUBST | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIM_APUR, DAT_INI_ERRO, DAT_FIM_ERRO, IDENT_PRODUTO, COD_FASE_PRODUCAO, IDENT_INSUMO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIM_APUR, DAT_INI_ERRO, DAT_FIM_ERRO, IDENT_PRODUTO, COD_FASE_PRODUCAO → RCP_REG_H270(COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIM_APUR, DAT_INI_ERRO, DAT_FIM_ERRO, IDENT_PRODUTO, COD_FASE_PRODUCAO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## REGISTRO_ESTADUAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 5 | NUM_JUNTA_COMER | VARCHAR2(14) | Y |  |  |
| 6 | DAT_DESPACHO | DATE | Y |  |  |
| 7 | NIRE | VARCHAR2(15) | Y |  |  |
| 8 | IND_SITUACAO | CHAR(1) | Y | '1' | Situação da Inscrição Normal = 1 / Suspensa = 2 |
| 9 | INSC_EST_ESPECIAL | VARCHAR2(14) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 12 | DAT_ENCERRAMENTO | DATE | Y |  |  |
| 13 | INSC_EST_VIRTUAL | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## REGISTRO_INSTITUICAO
**Comment**: Tabela de Paramentrização de Outras Inscrições Cadastrais da Empresa

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_INSTITUICAO | VARCHAR2(2) | N |  |  |
| 3 | INSCRICAO_INSTITUICAO | VARCHAR2(30) | N |  |  |

**PK**: COD_EMPRESA, COD_INSTITUICAO, INSCRICAO_INSTITUICAO

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## REGRA_VALID_DADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_REGRA | NUMBER(5) | N |  |  |
| 2 | CRITICIDADE | CHAR(1) | Y |  |  |
| 3 | TIPO_REGRA | NUMBER(2) | Y |  |  |
| 4 | TEXTO_REGRA | VARCHAR2(2000) | Y |  |  |

**PK**: COD_REGRA

---

## REG_ENTRADA_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SITUACAO | CHAR(1) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 17 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 18 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 19 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 20 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 21 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 22 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_REDUCAO_BASE | NUMBER(17,2) | Y |  |  |
| 24 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 25 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 26 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 27 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 28 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 30 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 31 | VLR_IPI_NEMBUT | NUMBER(17,2) | Y |  |  |
| 32 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 33 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 34 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 35 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 36 | NORM_DEV | CHAR(1) | Y |  |  |
| 37 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 38 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |

**Indexes**:
- IX_DOCAPURP1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, COD_CFO)
- IX_REG_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_CFO, COD_CFO, TITULO_TRIBUTO, COD_TRIBUTACAO)

---

## REG_SAIDA_CONS_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 9 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 10 | SITUACAO | CHAR(1) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 15 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 16 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 17 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 18 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 19 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 20 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 22 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 23 | IDENT_ESTADO | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_REG_CONS_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## REG_SAIDA_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SITUACAO | CHAR(1) | Y |  |  |
| 11 | DATA_FISCAL | DATE | Y |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 15 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 16 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 17 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 18 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 19 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 20 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 21 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 22 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_REDUCAO_BASE | NUMBER(17,2) | Y |  |  |
| 24 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 25 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 26 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 27 | SEQ_OBS | NUMBER(6) | Y |  |  |
| 28 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 30 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 31 | VLR_IPI_NEMBUT | NUMBER(17,2) | Y |  |  |
| 32 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 33 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 34 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 35 | CONTRIB_FINAL | CHAR(1) | Y |  |  |

**Indexes**:
- IX_DOCAPURP2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_FIS_JUR, COD_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, COD_CFO)
- IX_REG_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_CFO, SITUACAO)
- IX_REG_P2_2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_CFO, COD_CFO, TITULO_TRIBUTO, COD_TRIBUTACAO)

---

## RELAC_DACON_REGRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_FICHA | VARCHAR2(3) | N |  |  |
| 4 | NUM_LINHA | NUMBER(2) | N |  |  |
| 5 | IDENT_REGRA | NUMBER(12) | N |  |  |
| 6 | STATUS | CHAR(1) | Y |  |  |
| 7 | DT_INICIO | DATE | Y |  |  |
| 8 | IND_MAIS_MENOS | CHAR(1) | Y |  |  |
| 9 | MERCADO | CHAR(1) | N |  |  |
| 10 | IND_REG_RESULT | CHAR(1) | Y | 'N' |  |
| 11 | VERSAO | VARCHAR2(30) | N | 'VER. 01.00' |  |
| 12 | REGIME | VARCHAR2(1) | N | ' ' |  |
| 13 | COD_PRODUTO_DACON | VARCHAR2(10) | N |  |  |
| 14 | NUM_FICHA_OLD | VARCHAR2(3) | Y |  |  |
| 15 | IND_DET_SEPAR | CHAR(1) | N | ' ' |  |
| 16 | TIPO | CHAR(1) | Y |  |  |
| 17 | CNPJ | VARCHAR2(14) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB, VERSAO, NUM_FICHA, NUM_LINHA, IDENT_REGRA, IND_DET_SEPAR, MERCADO, REGIME, COD_PRODUTO_DACON, CNPJ

**FKs**:
- VERSAO, NUM_FICHA, NUM_LINHA → CAD_LINHA_DACON(VERSAO, NUM_FICHA, NUM_LINHA)

---

## RELAC_RELAT_REGRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | RELATID | NUMBER | N |  |  |
| 2 | ITEMID | NUMBER | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | IDENT_REGRA | NUMBER(12) | N |  |  |
| 6 | STATUS | CHAR(1) | Y |  |  |
| 7 | DT_INICIO | DATE | Y |  |  |
| 8 | IND_MAIS_MENOS | CHAR(1) | Y |  |  |
| 9 | IND_REG_RESULT | CHAR(1) | Y | 'N' |  |

**PK**: RELATID, ITEMID, COD_EMPRESA, COD_ESTAB, IDENT_REGRA

**FKs**:
- RELATID, ITEMID → CAD_RELAT_ITEM(RELATID, ITEMID)

---

## RELAC_TAB_GRUPO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TABELA | NUMBER(5) | N |  |  |
| 4 | VALID_INICIAL | DATE | N |  |  |
| 5 | GRUPO_ESTAB | VARCHAR2(9) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TABELA, VALID_INICIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TABELA → CAT_TABELAS(COD_TABELA)
- GRUPO_ESTAB → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IDX_RELAC_GRUPO_VALID: (COD_EMPRESA, COD_ESTAB, COD_TABELA, VALID_INICIAL, GRUPO_ESTAB)

---

## RELAT_APOIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | SITUACAO | NUMBER(1) | N |  |  |
| 5 | CODIGO | VARCHAR2(3) | N |  |  |
| 6 | DESCRICAO | VARCHAR2(70) | N |  |  |
| 7 | OBJETIVO | VARCHAR2(255) | Y |  |  |
| 8 | TIPO_EXECUCAO | CHAR(1) | N |  |  |
| 9 | QUEBRAR_PAG_AGRUPAMENTO | NUMBER(1) | N |  |  |
| 10 | ID_GRUPO_DADOS | NUMBER(38) | N |  |  |

**PK**: ID

**FKs**:
- ID_GRUPO_DADOS → GRUPO_DADOS(ID)

---

## RELAT_APOIO_AGRUPAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_RELAT_APOIO | NUMBER(38) | N |  |  |
| 2 | ID_COLUNA | NUMBER(38) | N |  |  |
| 3 | ORDEM_AGRUPAMENTO | NUMBER(2) | N |  |  |

**PK**: ID_RELAT_APOIO, ID_COLUNA

**FKs**:
- ID_RELAT_APOIO → RELAT_APOIO(ID)
- ID_COLUNA → GRUPO_DADOS_COLUNA(ID)

---

## RELAT_APOIO_EXEC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | ID_RELAT_APOIO | NUMBER(38) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | ORIENTACAO | CHAR(1) | N |  |  |
| 6 | FORMATO | CHAR(1) | N |  |  |
| 7 | DATA_AGENDAMENTO | TIMESTAMP(6) | N |  |  |
| 8 | DATA_EXECUCAO_INI | TIMESTAMP(6) | Y |  |  |
| 9 | DATA_EXECUCAO_FIM | TIMESTAMP(6) | Y |  |  |
| 10 | DATA_CADASTRAMENTO | DATE | Y |  |  |
| 11 | ID_RELAT_APOIO_EXEC_RESULT | NUMBER(38) | Y |  |  |
| 12 | JOB_NAME | VARCHAR2(200) | N |  |  |
| 13 | SCHED_NAME | VARCHAR2(120) | N |  |  |
| 14 | JOB_GROUP | VARCHAR2(200) | N |  |  |
| 15 | ID_USU_EXEC | NUMBER(38) | N |  |  |

**PK**: ID

**FKs**:
- ID_RELAT_APOIO → RELAT_APOIO(ID)
- ID_USU_EXEC → ESDRA_USER(ID_USUARIO)
- SCHED_NAME, JOB_NAME, JOB_GROUP → QRTZ_JOB_DETAILS(SCHED_NAME, JOB_NAME, JOB_GROUP)
- ID_RELAT_APOIO_EXEC_RESULT → RELAT_APOIO_EXEC_RESULT(ID)

---

## RELAT_APOIO_EXEC_PARAM_FILTROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_RELAT_APOIO_EXEC | NUMBER(38) | N |  |  |
| 2 | DATA_LANCAMENTO_DE | DATE | Y |  |  |
| 3 | DATA_LANCAMENTO_ATE | DATE | Y |  |  |
| 4 | DATA_EMISSAO_DE | DATE | Y |  |  |
| 5 | DATA_EMISSAO_ATE | DATE | Y |  |  |
| 6 | DATA_FISCAL_DE | DATE | Y |  |  |
| 7 | DATA_FISCAL_ATE | DATE | Y |  |  |
| 8 | DATA_MOVTO_FINANC_DE | DATE | Y |  |  |
| 9 | DATA_MOVTO_FINANC_ATE | DATE | Y |  |  |
| 10 | DATA_BAIXA_PAGTO_DE | DATE | Y |  |  |
| 11 | DATA_BAIXA_PAGTO_ATE | DATE | Y |  |  |
| 12 | CONTA_CONTAB_DE | VARCHAR2(70) | Y |  |  |
| 13 | CONTA_CONTAB_ATE | VARCHAR2(70) | Y |  |  |
| 14 | CENTRO_CUSTO_DE | VARCHAR2(50) | Y |  |  |
| 15 | CENTRO_CUSTO_ATE | VARCHAR2(50) | Y |  |  |
| 16 | CODIGO_PF_PJ | VARCHAR2(14) | Y |  |  |
| 17 | NUMERO_DOCTO_DE | VARCHAR2(12) | Y |  |  |
| 18 | NUMERO_DOCTO_ATE | VARCHAR2(12) | Y |  |  |
| 19 | UF | NUMBER(12) | Y |  |  |
| 20 | MUNICIPIO | NUMBER(5) | Y |  |  |
| 21 | SISTEMA_ORIG | NUMBER | Y |  |  |
| 22 | TIPO_DOCTO | VARCHAR2(20) | Y |  |  |

**PK**: ID_RELAT_APOIO_EXEC

**FKs**:
- ID_RELAT_APOIO_EXEC → RELAT_APOIO_EXEC(ID)

---

## RELAT_APOIO_EXEC_RESULT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | FILE_LOB | BLOB | N |  |  |

**PK**: ID

---

## RELAT_GIM_RR_QUADRO_F

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | LINHA1_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 6 | LINHA1_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 7 | LINHA1_COLUNA3 | NUMBER(1) | Y |  |  |
| 8 | LINHA1_COLUNA4 | NUMBER(17,2) | Y |  |  |
| 9 | LINHA1_COLUNA5 | NUMBER(1) | Y |  |  |
| 10 | LINHA1_COLUNA6 | NUMBER(17,2) | Y |  |  |
| 11 | LINHA1_COLUNA7 | NUMBER(1) | Y |  |  |
| 12 | LINHA1_COLUNA8 | NUMBER(17,2) | Y |  |  |
| 13 | LINHA1_COLUNA9 | NUMBER(1) | Y |  |  |
| 14 | LINHA2_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 15 | LINHA2_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 16 | LINHA2_COLUNA3 | NUMBER(1) | Y |  |  |
| 17 | LINHA2_COLUNA4 | NUMBER(17,2) | Y |  |  |
| 18 | LINHA2_COLUNA5 | NUMBER(1) | Y |  |  |
| 19 | LINHA2_COLUNA6 | NUMBER(17,2) | Y |  |  |
| 20 | LINHA2_COLUNA7 | NUMBER(1) | Y |  |  |
| 21 | LINHA2_COLUNA8 | NUMBER(17,2) | Y |  |  |
| 22 | LINHA2_COLUNA9 | NUMBER(1) | Y |  |  |
| 23 | LINHA3_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 24 | LINHA3_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 25 | LINHA3_COLUNA3 | NUMBER(1) | Y |  |  |
| 26 | LINHA3_COLUNA4 | NUMBER(17,2) | Y |  |  |
| 27 | LINHA3_COLUNA5 | NUMBER(1) | Y |  |  |
| 28 | LINHA3_COLUNA6 | NUMBER(17,2) | Y |  |  |
| 29 | LINHA3_COLUNA7 | NUMBER(1) | Y |  |  |
| 30 | LINHA3_COLUNA8 | NUMBER(17,2) | Y |  |  |
| 31 | LINHA3_COLUNA9 | NUMBER(1) | Y |  |  |
| 32 | LINHA4_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 33 | LINHA4_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 34 | LINHA4_COLUNA3 | NUMBER(1) | Y |  |  |
| 35 | LINHA4_COLUNA4 | NUMBER(17,2) | Y |  |  |
| 36 | LINHA4_COLUNA5 | NUMBER(1) | Y |  |  |
| 37 | LINHA4_COLUNA6 | NUMBER(17,2) | Y |  |  |
| 38 | LINHA4_COLUNA7 | NUMBER(1) | Y |  |  |
| 39 | LINHA4_COLUNA8 | NUMBER(17,2) | Y |  |  |
| 40 | LINHA4_COLUNA9 | NUMBER(1) | Y |  |  |
| 41 | LINHA5_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 42 | LINHA5_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 43 | LINHA5_COLUNA3 | NUMBER(1) | Y |  |  |
| 44 | LINHA5_COLUNA4 | NUMBER(17,2) | Y |  |  |
| 45 | LINHA5_COLUNA5 | NUMBER(1) | Y |  |  |
| 46 | LINHA5_COLUNA6 | NUMBER(17,2) | Y |  |  |
| 47 | LINHA5_COLUNA7 | NUMBER(1) | Y |  |  |
| 48 | LINHA5_COLUNA8 | NUMBER(17,2) | Y |  |  |
| 49 | LINHA5_COLUNA9 | NUMBER(1) | Y |  |  |
| 50 | LINHA6_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 51 | LINHA6_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 52 | LINHA6_COLUNA3 | NUMBER(1) | Y |  |  |
| 53 | LINHA6_COLUNA4 | NUMBER(17,2) | Y |  |  |
| 54 | LINHA6_COLUNA5 | NUMBER(1) | Y |  |  |
| 55 | LINHA6_COLUNA6 | NUMBER(17,2) | Y |  |  |
| 56 | LINHA6_COLUNA7 | NUMBER(1) | Y |  |  |
| 57 | LINHA6_COLUNA8 | NUMBER(17,2) | Y |  |  |
| 58 | LINHA6_COLUNA9 | NUMBER(1) | Y |  |  |
| 59 | LINHA7_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 60 | LINHA7_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 61 | LINHA7_COLUNA3 | NUMBER(1) | Y |  |  |
| 62 | LINHA7_COLUNA4 | NUMBER(17,2) | Y |  |  |
| 63 | LINHA7_COLUNA5 | NUMBER(1) | Y |  |  |
| 64 | LINHA7_COLUNA6 | NUMBER(17,2) | Y |  |  |
| 65 | LINHA7_COLUNA7 | NUMBER(1) | Y |  |  |
| 66 | LINHA7_COLUNA8 | NUMBER(17,2) | Y |  |  |
| 67 | LINHA7_COLUNA9 | NUMBER(1) | Y |  |  |
| 68 | LINHA8_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 69 | LINHA8_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 70 | LINHA8_COLUNA3 | NUMBER(1) | Y |  |  |
| 71 | LINHA8_COLUNA4 | NUMBER(17,2) | Y |  |  |
| 72 | LINHA8_COLUNA5 | NUMBER(1) | Y |  |  |
| 73 | LINHA8_COLUNA6 | NUMBER(17,2) | Y |  |  |
| 74 | LINHA8_COLUNA7 | NUMBER(1) | Y |  |  |
| 75 | LINHA8_COLUNA8 | NUMBER(17,2) | Y |  |  |
| 76 | LINHA8_COLUNA9 | NUMBER(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

---

## RELAT_GIM_RR_QUADRO_G

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | LINHA1_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 6 | LINHA1_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 7 | LINHA1_COLUNA3 | NUMBER(1) | Y |  |  |
| 8 | LINHA1_COLUNA4 | VARCHAR2(50) | Y |  |  |
| 9 | LINHA1_COLUNA5 | NUMBER(17,2) | Y |  |  |
| 10 | LINHA1_COLUNA6 | NUMBER(1) | Y |  |  |
| 11 | LINHA2_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 12 | LINHA2_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 13 | LINHA2_COLUNA3 | NUMBER(1) | Y |  |  |
| 14 | LINHA2_COLUNA4 | VARCHAR2(50) | Y |  |  |
| 15 | LINHA2_COLUNA5 | NUMBER(17,2) | Y |  |  |
| 16 | LINHA2_COLUNA6 | NUMBER(1) | Y |  |  |
| 17 | LINHA3_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 18 | LINHA3_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 19 | LINHA3_COLUNA3 | NUMBER(1) | Y |  |  |
| 20 | LINHA3_COLUNA4 | VARCHAR2(50) | Y |  |  |
| 21 | LINHA3_COLUNA5 | NUMBER(17,2) | Y |  |  |
| 22 | LINHA3_COLUNA6 | NUMBER(1) | Y |  |  |
| 23 | LINHA4_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 24 | LINHA4_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 25 | LINHA4_COLUNA3 | NUMBER(1) | Y |  |  |
| 26 | LINHA4_COLUNA4 | VARCHAR2(50) | Y |  |  |
| 27 | LINHA4_COLUNA5 | NUMBER(17,2) | Y |  |  |
| 28 | LINHA4_COLUNA6 | NUMBER(1) | Y |  |  |
| 29 | LINHA5_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 30 | LINHA5_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 31 | LINHA5_COLUNA3 | NUMBER(1) | Y |  |  |
| 32 | LINHA5_COLUNA4 | VARCHAR2(50) | Y |  |  |
| 33 | LINHA5_COLUNA5 | NUMBER(17,2) | Y |  |  |
| 34 | LINHA5_COLUNA6 | NUMBER(1) | Y |  |  |
| 35 | LINHA6_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 36 | LINHA6_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 37 | LINHA6_COLUNA3 | NUMBER(1) | Y |  |  |
| 38 | LINHA6_COLUNA4 | VARCHAR2(50) | Y |  |  |
| 39 | LINHA6_COLUNA5 | NUMBER(17,2) | Y |  |  |
| 40 | LINHA6_COLUNA6 | NUMBER(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

---

## RELAT_GIM_RR_QUADRO_H

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | LINHA1_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 6 | LINHA1_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 7 | LINHA1_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 8 | LINHA1_COLUNA4 | NUMBER(1) | Y |  |  |
| 9 | LINHA2_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 10 | LINHA2_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 11 | LINHA2_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 12 | LINHA2_COLUNA4 | NUMBER(1) | Y |  |  |
| 13 | LINHA3_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 14 | LINHA3_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 15 | LINHA3_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 16 | LINHA3_COLUNA4 | NUMBER(1) | Y |  |  |
| 17 | LINHA4_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 18 | LINHA4_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 19 | LINHA4_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 20 | LINHA4_COLUNA4 | NUMBER(1) | Y |  |  |
| 21 | LINHA5_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 22 | LINHA5_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 23 | LINHA5_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 24 | LINHA5_COLUNA4 | NUMBER(1) | Y |  |  |
| 25 | LINHA6_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 26 | LINHA6_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 27 | LINHA6_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 28 | LINHA6_COLUNA4 | NUMBER(1) | Y |  |  |
| 29 | LINHA7_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 30 | LINHA7_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 31 | LINHA7_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 32 | LINHA7_COLUNA4 | NUMBER(1) | Y |  |  |
| 33 | LINHA8_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 34 | LINHA8_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 35 | LINHA8_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 36 | LINHA8_COLUNA4 | NUMBER(1) | Y |  |  |
| 37 | LINHA9_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 38 | LINHA9_COLUNA2 | VARCHAR2(10) | Y |  |  |
| 39 | LINHA9_COLUNA3 | NUMBER(17,2) | Y |  |  |
| 40 | LINHA9_COLUNA4 | NUMBER(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

---

## RELAT_GIM_RR_QUADRO_I

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | LINHA1_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 6 | LINHA1_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 7 | LINHA1_COLUNA3 | NUMBER(1) | Y |  |  |
| 8 | LINHA2_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 9 | LINHA2_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 10 | LINHA2_COLUNA3 | NUMBER(1) | Y |  |  |
| 11 | LINHA3_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 12 | LINHA3_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 13 | LINHA3_COLUNA3 | NUMBER(1) | Y |  |  |
| 14 | LINHA4_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 15 | LINHA4_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 16 | LINHA4_COLUNA3 | NUMBER(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

---

## RELAT_GIM_RR_QUADRO_J

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_APURACAO | NUMBER(4) | N |  |  |
| 4 | MES_APURACAO | NUMBER(2) | N |  |  |
| 5 | LINHA1_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 6 | LINHA1_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 7 | LINHA1_COLUNA3 | NUMBER(1) | Y |  |  |
| 8 | LINHA2_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 9 | LINHA2_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 10 | LINHA2_COLUNA3 | NUMBER(1) | Y |  |  |
| 11 | LINHA3_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 12 | LINHA3_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 13 | LINHA3_COLUNA3 | NUMBER(1) | Y |  |  |
| 14 | LINHA4_COLUNA1 | VARCHAR2(50) | Y |  |  |
| 15 | LINHA4_COLUNA2 | NUMBER(17,2) | Y |  |  |
| 16 | LINHA4_COLUNA3 | NUMBER(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_APURACAO, MES_APURACAO

---

## RESPONSAVEL_LEGAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, COD_RESPONSAVEL

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## RESP_CONTADOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 2 | NUM_CRC | VARCHAR2(17) | Y |  |  |
| 3 | NUM_CPF | VARCHAR2(14) | Y |  |  |
| 4 | IDENT_ESTADO_CRC | NUMBER | Y |  |  |

**PK**: COD_RESPONSAVEL

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## RESP_CONTRIBUINTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 2 | DSC_CARGO | VARCHAR2(50) | Y |  |  |
| 3 | NUM_CPF | VARCHAR2(14) | Y |  |  |

**PK**: COD_RESPONSAVEL

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## RESP_FARMACEUTICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 2 | NUM_CRF | VARCHAR2(17) | Y |  |  |
| 3 | IDENT_ESTADO_CRF | NUMBER | Y |  |  |

**PK**: COD_RESPONSAVEL

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## RESP_INFORMACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 2 | NOM_RESPONSAVEL | VARCHAR2(50) | Y |  |  |
| 3 | NUM_DDD | VARCHAR2(4) | Y |  |  |
| 4 | NUM_TELEFONE | VARCHAR2(24) | Y |  |  |
| 5 | NUM_RAMAL | VARCHAR2(4) | Y |  |  |
| 6 | NUM_FAX | VARCHAR2(10) | Y |  |  |
| 7 | NUM_TELEX | VARCHAR2(10) | Y |  |  |
| 8 | IND_CATEGORIA | CHAR(1) | Y |  |  |
| 9 | TP_LOGRADOURO | VARCHAR2(6) | Y |  |  |
| 10 | DSC_ENDERECO | VARCHAR2(50) | Y |  |  |
| 11 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 12 | COMPL_ENDERECO | VARCHAR2(20) | Y |  |  |
| 13 | DSC_BAIRRO | VARCHAR2(30) | Y |  |  |
| 14 | NUM_CEP | NUMBER(8) | Y |  |  |
| 15 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 16 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 17 | E_MAIL | VARCHAR2(100) | Y |  |  |
| 18 | NUM_RG | VARCHAR2(15) | Y |  |  |
| 19 | ORGAO_EMISSOR_RG | VARCHAR2(10) | Y |  |  |
| 20 | NUM_CPF | VARCHAR2(11) | Y |  |  |
| 21 | DSC_CARGO | VARCHAR2(50) | Y |  |  |
| 22 | AG_POSTAL | VARCHAR2(50) | Y |  |  |
| 23 | CX_POSTAL | VARCHAR2(20) | Y |  |  |
| 24 | IDENT_ESTADO_RG | NUMBER(12) | Y |  |  |
| 25 | NUM_CEP_CX_POSTAL | VARCHAR2(8) | Y |  | Código de endereçamento postal da caixa postal |
| 26 | DAT_INI_PREST_SERV | DATE | Y |  | Data inicio da prestação de serviço do responsável pela informação |
| 27 | DAT_FIM_PREST_SERV | DATE | Y |  | Data de término da prestação de serviço do responsável pela informação |
| 28 | NUM_CPF_TECN_SOF | VARCHAR2(11) | Y |  | Número do CPF do responsável pelo software |
| 29 | IND_ATIVO | CHAR(1) | Y | 'A' | Indicador de responsavel Ativo(A) e Inativo(I) |
| 30 | IND_QUALIFICACAO | VARCHAR2(3) | Y |  |  |
| 31 | DT_CRC | DATE | Y |  |  |
| 32 | NUM_SEQ_CRC | VARCHAR2(20) | Y |  |  |

**PK**: COD_RESPONSAVEL

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## RESP_TECNICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 2 | DSC_CARGO | VARCHAR2(50) | Y |  |  |
| 3 | NUM_CPF | VARCHAR2(14) | Y |  |  |

**PK**: COD_RESPONSAVEL

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## RESUMO_APURACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_ENTRADA_SAIDA | CHAR(1) | Y |  |  |
| 6 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 7 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_NTRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

**Indexes**:
- IX_RESUMO_APURACAO_CTA: (IDENT_CONTA)
- IX_RESUM_APUR: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## RESUMO_APURACAO_AX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_ENTRADA_SAIDA | CHAR(1) | Y |  |  |
| 6 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 7 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_NTRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_RESUM_APUR_AX: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## RESUMO_APUR_DIFAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TOT_DEB_FCP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_CRED_FCP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_RES_DEV | NUMBER(17,2) | Y |  |  |
| 11 | VLR_RES_CRED | NUMBER(17,2) | Y |  |  |
| 12 | VLR_RES_DEV_FCP | NUMBER(17,2) | Y |  |  |
| 13 | VLR_RES_CRED_FCP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO

---

## RESUMO_APUR_DIFAL_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT_DEB_FCP | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_CRED_FCP | NUMBER(17,2) | Y |  |  |
| 11 | VLR_RES_DEV | NUMBER(17,2) | Y |  |  |
| 12 | VLR_RES_CRED | NUMBER(17,2) | Y |  |  |
| 13 | VLR_RES_DEV_FCP | NUMBER(17,2) | Y |  |  |
| 14 | VLR_RES_CRED_FCP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO

---

## RESUMO_APUR_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | IND_UF | CHAR(1) | N |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | IND_GER_AUTOM | CHAR(1) | Y |  |  |
| 11 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 12 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 14 | ID_GER | NUMBER(12) | Y |  |  |
| 15 | SEQ_GER_ARQ | NUMBER(12) | Y |  |  |
| 16 | TXT_GER_ARQ | VARCHAR2(4000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RESUMO_APUR_ST_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | IND_UF | CHAR(1) | N |  |  |
| 8 | COD_OPER_APUR | VARCHAR2(5) | N |  |  |
| 9 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 11 | IND_GER_AUTOM | CHAR(1) | N |  |  |
| 12 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 13 | VLR_BASE_ISENTA | NUMBER(17,2) | Y |  |  |
| 14 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, IND_UF, COD_OPER_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RES_ALIQ_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 10 | NRO_FOLHA | NUMBER(6) | Y |  |  |

**Indexes**:
- IX_RES_ALIQ_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, VLR_ALIQ_ICMS)

---

## RES_ALIQ_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 6 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 10 | NRO_FOLHA | NUMBER(6) | Y |  |  |

**Indexes**:
- IX_RES_ALIQ_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, VLR_ALIQ_ICMS)

---

## RES_ALIQ_P9

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_E_S | CHAR(1) | Y |  |  |
| 6 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 7 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 11 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 12 | ID_GER | NUMBER(12) | Y |  |  |
| 13 | SEQ_GER_ARQ | NUMBER(12) | Y |  |  |
| 14 | TXT_GER_ARQ | VARCHAR2(4000) | Y |  |  |

---

## RES_APUR_ST_CONV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | COD_CLASS_DOC_FIS | CHAR(1) | N |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 13 | CLASSE_REL | VARCHAR2(10) | N |  |  |
| 14 | COD_REL | VARCHAR2(10) | N |  |  |
| 15 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMSS_ISENTAS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMSS_OUTRAS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 19 | COD_OPER_CRED_DED | VARCHAR2(3) | Y |  |  |
| 20 | DAT_VENC | DATE | Y |  |  |
| 21 | IDENT_GNRE_GERADA | NUMBER(12) | Y |  |  |
| 22 | VLR_CRED | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_CLASS_DOC_FIS, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_ESTADO, CLASSE_REL, COD_REL

---

## RES_APUR_ST_CONV_ABAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | COD_CLASS_DOC_FIS | CHAR(1) | N |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 13 | CLASSE_REL | VARCHAR2(10) | N |  |  |
| 14 | COD_REL | VARCHAR2(10) | N |  |  |
| 15 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMSS_ISENTAS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMSS_OUTRAS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 19 | COD_OPER_CRED_DED | VARCHAR2(3) | Y |  |  |
| 20 | DAT_VENC | DATE | Y |  |  |
| 21 | IDENT_GNRE_GERADA | NUMBER(12) | Y |  |  |
| 22 | VLR_CRED | NUMBER(17,2) | Y |  |  |
| 23 | VLR_DEB | NUMBER(17,2) | Y |  |  |
| 24 | VLR_SLD_CRED | NUMBER(17,2) | Y |  |  |
| 25 | VLR_SLD_DEB | NUMBER(17,2) | Y |  |  |
| 26 | VLR_SLD | NUMBER(17,2) | Y |  |  |
| 27 | COD_CONV | VARCHAR2(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, COD_CLASS_DOC_FIS, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_ESTADO, CLASSE_REL, COD_REL

**Indexes**:
- IX_RES_APUR_ST_CONV_ABAT: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, CLASSE_REL, COD_REL, IDENT_GNRE_GERADA, IDENT_ESTADO)

---

## RES_APUR_ST_CONV_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | COD_CLASS_DOC_FIS | CHAR(1) | N |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 13 | CLASSE_REL | VARCHAR2(10) | N |  |  |
| 14 | COD_REL | VARCHAR2(3) | N |  |  |
| 15 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ICMSS_ISENTAS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMSS_OUTRAS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 19 | COD_OPER_CRED_DED | VARCHAR2(3) | Y |  |  |
| 20 | DAT_VENC | DATE | Y |  |  |
| 21 | IDENT_GNRE_GERADA | NUMBER(12) | Y |  |  |
| 22 | VLR_CRED | NUMBER(17,2) | Y |  |  |

---

## RGR_LISTA_VALOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PARAM | NUMBER(12) | N |  |  |
| 2 | VALOR | VARCHAR2(100) | N |  |  |

**PK**: IDENT_PARAM, VALOR

**FKs**:
- IDENT_PARAM → RGR_PARAMETRO(IDENT_PARAM)

---

## RGR_PARAMETRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PARAM | NUMBER(12) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 3 | PARAMETRO | VARCHAR2(30) | Y |  |  |
| 4 | IND_LIS_COL_VAL | CHAR(1) | Y |  |  |
| 5 | NOME_COLUNA | VARCHAR2(60) | Y |  |  |
| 6 | VALOR | NUMBER(19,4) | Y |  |  |
| 7 | IND_PADRAO_MSAF | CHAR(1) | Y | 'N' |  |

**PK**: IDENT_PARAM

---

## RGR_PESQUISA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PESQUISA | NUMBER(12) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 3 | CODIGO_PLSQL | LONG | Y |  |  |
| 4 | IND_PADRAO_MSAF | CHAR(1) | Y | 'N' |  |

**PK**: IDENT_PESQUISA

---

## RGR_REGRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_REGRA | NUMBER(12) | N |  |  |
| 2 | VALID_REGRA | DATE | N |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | IND_ORIGEM | CHAR(1) | Y |  |  |
| 5 | IDENT_PESQUISA | NUMBER(12) | Y |  |  |

**PK**: IDENT_REGRA, VALID_REGRA

**FKs**:
- IDENT_PESQUISA → RGR_PESQUISA(IDENT_PESQUISA)

---

## RGR_RELAC_PARAMETRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_REGRA | NUMBER(12) | N |  |  |
| 2 | VALID_REGRA | DATE | N |  |  |
| 3 | IDENT_PARAM | NUMBER(12) | N |  |  |

**PK**: IDENT_REGRA, VALID_REGRA, IDENT_PARAM

**FKs**:
- IDENT_REGRA, VALID_REGRA → RGR_REGRA(IDENT_REGRA, VALID_REGRA)
- IDENT_PARAM → RGR_PARAMETRO(IDENT_PARAM)

---

## RGR_VALIDACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PARAMETRO | VARCHAR2(30) | N |  |  |
| 2 | CODIGO_PLSQL | LONG | Y |  |  |
| 3 | IND_PADRAO_MSAF | VARCHAR2(1) | Y |  |  |

**PK**: PARAMETRO

---

## ROBOT_LOG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDSEQ | NUMBER(22) | Y |  |  |
| 2 | STATUS | CHAR(1) | Y |  |  |
| 3 | DSCTESTE | VARCHAR2(50) | Y |  |  |
| 4 | MODULO | VARCHAR2(50) | Y |  |  |
| 5 | DT_EXEC | DATE | Y |  |  |

---

## ROBOT_LOG_CH

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDSEQ | NUMBER(22) | Y |  |  |
| 2 | CHAMADO | VARCHAR2(50) | Y |  |  |
| 3 | STATUS | CHAR(1) | Y |  |  |
| 4 | MODULO | VARCHAR2(50) | Y |  |  |
| 5 | DT_EXEC | DATE | Y |  |  |

---

## SAFE01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 4 | CONTA_DEB_CRED | VARCHAR2(70) | Y |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 7 | VLR_LANCTO | VARCHAR2(17) | Y |  |  |
| 8 | CONTRA_PART | VARCHAR2(70) | Y |  |  |
| 9 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 10 | CENTRO_DESPESA | VARCHAR2(20) | Y |  |  |
| 11 | HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 12 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 13 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 14 | COD_INDICE_CONV | VARCHAR2(10) | Y |  |  |
| 15 | VLR_OPER_IND | VARCHAR2(18) | Y |  |  |
| 16 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 17 | TIPO_LANCTO | CHAR(1) | Y |  |  |
| 18 | IND_PFJ_EMPRESA | CHAR(1) | Y |  |  |
| 19 | COD_PFJ_EMPRESA | VARCHAR2(14) | Y |  |  |
| 20 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 21 | IDENTIF_LANC_RES | VARCHAR2(128) | Y |  |  |
| 22 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 23 | IDENTIF_SALDO | VARCHAR2(128) | Y |  |  |
| 24 | DSC_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 25 | DSC_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 26 | DSC_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 27 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 28 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 29 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 30 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 31 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

---

## SAFE196

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 4 | CONTA_DEB_CRED | VARCHAR2(70) | Y |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 7 | VLR_LANCTO | VARCHAR2(17) | Y |  |  |
| 8 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 13 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 14 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 15 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 16 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 17 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 18 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 19 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 20 | NORM_DEV | CHAR(1) | Y |  |  |
| 21 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 22 | VLR_OPERACAO | VARCHAR2(17) | Y |  |  |
| 23 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 24 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 25 | SITUACAO | CHAR(1) | Y |  |  |
| 26 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 27 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 28 | CONTRA_PART | VARCHAR2(70) | Y |  |  |
| 29 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 30 | HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 31 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 32 | NUM_LANCAMENTO | VARCHAR2(12) | Y |  |  |
| 33 | TIPO_LANCTO | CHAR(1) | Y |  |  |
| 34 | COD_TP_DOC_LANCTO | VARCHAR2(3) | Y |  |  |
| 35 | CENTRO_LUCRO | VARCHAR2(20) | Y |  |  |
| 36 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 37 | COD_DDD | VARCHAR2(5) | Y |  |  |
| 38 | NUM_CELULAR | VARCHAR2(15) | Y |  |  |
| 39 | VLR_ATIVACAO | VARCHAR2(17) | Y |  |  |
| 40 | CICLO | VARCHAR2(7) | Y |  |  |
| 41 | DSC_ATRIBUICAO | VARCHAR2(255) | Y |  |  |
| 42 | MOT_AJUSTE | VARCHAR2(6) | Y |  |  |
| 43 | TIPO_SERVICO | VARCHAR2(35) | Y |  |  |
| 44 | DET_TIPO_SERVICO | VARCHAR2(35) | Y |  |  |
| 45 | COD_MERCADO | VARCHAR2(3) | Y |  |  |
| 46 | TIPO_ATIV_FINANC | VARCHAR2(6) | Y |  |  |
| 47 | TIPO_ITEM_NF | CHAR(1) | Y |  |  |
| 48 | COD_BANCO | VARCHAR2(4) | Y |  |  |
| 49 | DSC_BANCO | VARCHAR2(50) | Y |  |  |
| 50 | TIPO_PAGTO | VARCHAR2(2) | Y |  |  |
| 51 | VLR_PAGTO | VARCHAR2(17) | Y |  |  |
| 52 | NUM_CLI_PAGTO | VARCHAR2(9) | Y |  |  |
| 53 | VLR_ATIVIDADE | VARCHAR2(17) | Y |  |  |
| 54 | NUM_FATURA | VARCHAR2(12) | Y |  |  |
| 55 | TIPO_ARRECADACAO | VARCHAR2(2) | Y |  |  |
| 56 | NUM_SEQ_ARQ | VARCHAR2(5) | Y |  |  |
| 57 | NUM_SEQ_PAGTO | VARCHAR2(6) | Y |  |  |
| 58 | VLR_SALDO_ATUAL | VARCHAR2(17) | Y |  |  |
| 59 | COD_BARRAS | VARCHAR2(44) | Y |  |  |
| 60 | MEIO_ARRECADACAO | CHAR(1) | Y |  |  |
| 61 | DATA_BAIXA | VARCHAR2(8) | Y |  |  |
| 62 | COD_ATIV_PAGTO | VARCHAR2(4) | Y |  |  |
| 63 | DSC_RESERVADO1 | VARCHAR2(128) | Y |  |  |
| 64 | DSC_RESERVADO2 | VARCHAR2(128) | Y |  |  |
| 65 | DSC_RESERVADO3 | VARCHAR2(128) | Y |  |  |
| 66 | DSC_RESERVADO4 | VARCHAR2(128) | Y |  |  |
| 67 | DSC_RESERVADO5 | VARCHAR2(128) | Y |  |  |
| 68 | DSC_RESERVADO6 | VARCHAR2(17) | Y |  |  |
| 69 | DSC_RESERVADO7 | VARCHAR2(17) | Y |  |  |
| 70 | DSC_RESERVADO8 | VARCHAR2(17) | Y |  |  |
| 71 | DSC_RESERVADO9 | VARCHAR2(17) | Y |  |  |
| 72 | DSC_RESERVADO10 | VARCHAR2(17) | Y |  |  |

---

## SCT_ANEXO4_PAISES_PF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ANEXO | NUMBER(2) | N |  |  |
| 2 | COD_PAIS | VARCHAR2(3) | N |  |  |

**PK**: COD_ANEXO, COD_PAIS

**FKs**:
- COD_PAIS → PAIS(COD_PAIS)

---

## SCT_CLASS_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 2 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 3 | DSC_CLASS_PRD | VARCHAR2(50) | Y |  |  |
| 4 | DSC_ESPECIFICACAO | VARCHAR2(50) | Y |  |  |
| 5 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 6 | PERC_CONCENT | NUMBER(5,2) | Y |  |  |
| 7 | DENSIDADE | NUMBER(5,2) | Y |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | COD_ANEXO | NUMBER(2) | Y |  |  |
| 10 | QTD_MIN_PF | NUMBER(17,6) | Y |  |  |
| 11 | COD_LISTA_ANVISA | VARCHAR2(2) | Y |  | Codigos dos medicamentos controlados pela ANVISA. Provenientes da view sc_lista_anvisa_v |
| 12 | COD_OFICIAL_PF | VARCHAR2(15) | Y |  | Codigos das listas I a VII da Policia Federal. |

**PK**: TIPO_OBRIGACAO, COD_CLASS_PRD

---

## SCT_OPER_OBRIG
**Comment**: Cadastros das operações dos movimentos para as operações das obrigações de substâncias controladas

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  | PC - Polícia Científica, ... |
| 2 | COD_OPER_SC | NUMBER(2) | N |  | Tipo de Operação presente nos movimentos, referente a FDT_SC_TIPO_OPER |
| 3 | COD_OPER_OBRIG | NUMBER(2) | Y |  | Operações definitas em cada obrigação, referente a SC_OPER_OBRIG_V |

**PK**: TIPO_OBRIGACAO, COD_OPER_SC

**FKs**:
- COD_OPER_SC → FDT_SC_TIPO_OPER(COD_TP_OPER_SC)

---

## SCT_SALDO_PERIODO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 5 | COD_CLASS_PRD | VARCHAR2(15) | N |  |  |
| 6 | QTD_SALDO | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, TIPO_OBRIGACAO, COD_CLASS_PRD

---

## SCT_TP_OBRIGACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 4 | IND_TERMO_ABERTURA | CHAR(1) | Y |  |  |
| 5 | COD_INSCRICAO | VARCHAR2(40) | Y |  |  |
| 6 | DAT_VALID_INSCR | DATE | Y |  |  |
| 7 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 8 | NUM_ALVARA | VARCHAR2(20) | Y |  |  |
| 9 | NUM_LICENCA_FUNC | VARCHAR2(20) | Y |  |  |
| 10 | NUM_AUTO_ESPECIAL | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_OBRIGACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## SCT_TP_UTILIZACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UTILIZACAO | VARCHAR2(5) | N |  |  |
| 2 | DSC_UTILIZACAO | VARCHAR2(50) | Y |  |  |
| 3 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_UTILIZACAO

---

## SC_PRE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_INI | DATE | Y |  |  |
| 2 | DATA_FIM | DATE | Y |  |  |
| 3 | IND_MOV_EMIS | VARCHAR2(2) | Y |  |  |
| 4 | PIND_COM_NACIO | VARCHAR2(2) | Y |  |  |
| 5 | PIND_COM_INTER | VARCHAR2(2) | Y |  |  |
| 6 | PIND_PRODUCAO | VARCHAR2(2) | Y |  |  |
| 7 | PIND_TRANSF | VARCHAR2(2) | Y |  |  |
| 8 | PIND_CONSUMO | VARCHAR2(2) | Y |  |  |
| 9 | PIND_FABRIC | VARCHAR2(2) | Y |  |  |
| 10 | PIND_TRANSP | VARCHAR2(2) | Y |  |  |
| 11 | PIND_ARMAZENAM | VARCHAR2(2) | Y |  |  |
| 12 | PIND_PROD | VARCHAR2(2) | Y |  |  |
| 13 | RAZAO_SOCIAL_EMPR | VARCHAR2(70) | Y |  |  |
| 14 | CGC_ESTAB | VARCHAR2(14) | Y |  |  |
| 15 | RAZAO_SOCIAL_ESTAB | VARCHAR2(100) | Y |  |  |
| 16 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 17 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 18 | DATA_MOVTO | DATE | Y |  |  |
| 19 | DATA_EMISSAO | DATE | Y |  |  |
| 20 | DATA_PERIODO | DATE | Y |  |  |
| 21 | ENTSAI | CHAR(1) | Y |  |  |
| 22 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 23 | TIPO_OPERACAO | NUMBER(2) | Y |  |  |
| 24 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 25 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 26 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 27 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 28 | IDENT_FIS_JUR_TRANSP | NUMBER(12) | Y |  |  |
| 29 | IDENT_FIS_JUR_ARMAZEM | NUMBER(12) | Y |  |  |
| 30 | IND_TP_FRETE | VARCHAR2(1) | Y |  |  |
| 31 | IND_TP_FRETE_MVN | VARCHAR2(1) | Y |  |  |
| 32 | IND_ENTREGA | VARCHAR2(1) | Y |  |  |
| 33 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 34 | NUM_REG_EXP_IMP | VARCHAR2(15) | Y |  |  |
| 35 | DAT_EMBARQUE | DATE | Y |  |  |
| 36 | DAT_CONHEC_EMB | DATE | Y |  |  |
| 37 | IDENT_FIS_JUR_ENTREGA | NUMBER(12) | Y |  |  |
| 38 | IDENT_FIS_JUR_ADQ | NUMBER(12) | Y |  |  |
| 39 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 40 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 41 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 42 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 43 | VALID_PRODUTO | DATE | Y |  |  |
| 44 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 45 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 46 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 47 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 48 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 49 | IND_ARMAZENAGEM | CHAR(1) | Y |  |  |
| 50 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 51 | COD_PAIS_OBRIG | VARCHAR2(10) | Y |  |  |
| 52 | GRUPO_FIS_JUR_TRANSP | VARCHAR2(9) | Y |  |  |
| 53 | IND_FIS_JUR_TRANSP | CHAR(1) | Y |  |  |
| 54 | COD_FIS_JUR_TRANSP | VARCHAR2(14) | Y |  |  |
| 55 | CPF_CGC_TRANSP | VARCHAR2(14) | Y |  |  |
| 56 | RAZAO_SOCIAL_TRANSP | VARCHAR2(70) | Y |  |  |
| 57 | ENDERECO_TRANSP | VARCHAR2(50) | Y |  |  |
| 58 | CEP_TRANSP | NUMBER(8) | Y |  |  |
| 59 | NUM_ENDERECO_TRANSP | VARCHAR2(10) | Y |  |  |
| 60 | COMPL_ENDERECO_TRANSP | VARCHAR2(45) | Y |  |  |
| 61 | BAIRRO_TRANSP | VARCHAR2(20) | Y |  |  |
| 62 | UF_TRANSP | VARCHAR2(2) | Y |  |  |
| 63 | COD_MUNICIPIO_TRANSP | NUMBER(5) | Y |  |  |
| 64 | COD_UF_MUNIC_TRANSP | NUMBER | Y |  |  |
| 65 | GRUPO_FIS_JUR_ARMAZEM | VARCHAR2(9) | Y |  |  |
| 66 | IND_FIS_JUR_ARMAZEM | CHAR(1) | Y |  |  |
| 67 | COD_FIS_JUR_ARMAZEM | VARCHAR2(14) | Y |  |  |
| 68 | CPF_CGC_ARMAZEM | VARCHAR2(14) | Y |  |  |
| 69 | RAZAO_SOCIAL_ARMAZEM | VARCHAR2(70) | Y |  |  |
| 70 | ENDERECO_ARMAZEM | VARCHAR2(50) | Y |  |  |
| 71 | CEP_ARMAZEM | NUMBER(8) | Y |  |  |
| 72 | NUM_ENDERECO_ARMAZEM | VARCHAR2(10) | Y |  |  |
| 73 | COMPL_ENDERECO_ARMAZEM | VARCHAR2(45) | Y |  |  |
| 74 | BAIRRO_ARMAZEM | VARCHAR2(20) | Y |  |  |
| 75 | UF_ARMAZEM | VARCHAR2(2) | Y |  |  |
| 76 | COD_MUNICIPIO_ARMAZEM | NUMBER(5) | Y |  |  |
| 77 | COD_UF_MUNIC_ARMAZEM | NUMBER | Y |  |  |
| 78 | GRUPO_FIS_JUR_TER | VARCHAR2(9) | Y |  |  |
| 79 | IND_FIS_JUR_TER | CHAR(1) | Y |  |  |
| 80 | COD_FIS_JUR_TER | VARCHAR2(14) | Y |  |  |
| 81 | CPF_CGC_TER | VARCHAR2(14) | Y |  |  |
| 82 | RAZAO_SOCIAL_TER | VARCHAR2(70) | Y |  |  |
| 83 | ENDERECO_TER | VARCHAR2(50) | Y |  |  |
| 84 | CEP_TER | NUMBER(8) | Y |  |  |
| 85 | NUM_ENDERECO_TER | VARCHAR2(10) | Y |  |  |
| 86 | COMPL_ENDERECO_TER | VARCHAR2(45) | Y |  |  |
| 87 | BAIRRO_TER | VARCHAR2(20) | Y |  |  |
| 88 | UF_TER | VARCHAR2(2) | Y |  |  |
| 89 | COD_MUNICIPIO_TER | NUMBER(5) | Y |  |  |
| 90 | COD_UF_MUNIC_TER | NUMBER | Y |  |  |
| 91 | GRUPO_FIS_JUR_ADQ | VARCHAR2(9) | Y |  |  |
| 92 | IND_FIS_JUR_ADQ | CHAR(1) | Y |  |  |
| 93 | COD_FIS_JUR_ADQ | VARCHAR2(14) | Y |  |  |
| 94 | CPF_CGC_ADQ | VARCHAR2(14) | Y |  |  |
| 95 | RAZAO_SOCIAL_ADQ | VARCHAR2(70) | Y |  |  |
| 96 | ENDERECO_ADQ | VARCHAR2(50) | Y |  |  |
| 97 | CEP_ADQ | NUMBER(8) | Y |  |  |
| 98 | NUM_ENDERECO_ADQ | VARCHAR2(10) | Y |  |  |
| 99 | COMPL_ENDERECO_ADQ | VARCHAR2(45) | Y |  |  |
| 100 | BAIRRO_ADQ | VARCHAR2(20) | Y |  |  |
| 101 | UF_ADQ | VARCHAR2(2) | Y |  |  |
| 102 | COD_MUNICIPIO_ADQ | NUMBER(5) | Y |  |  |
| 103 | COD_UF_MUNIC_ADQ | NUMBER | Y |  |  |
| 104 | COD_MEDIDA_CLASS | VARCHAR2(8) | Y |  |  |
| 105 | COD_MEDIDA_X70 | VARCHAR2(8) | Y |  |  |
| 106 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 107 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 108 | QTD_MOVTO | NUMBER | Y |  |  |
| 109 | TIPO_OBRIGACAO | VARCHAR2(2) | Y |  |  |
| 110 | COD_CLASS_PRD | VARCHAR2(15) | Y |  |  |
| 111 | COD_OFICIAL_PF | VARCHAR2(15) | Y |  |  |
| 112 | DSC_CLASS_PRD | VARCHAR2(50) | Y |  |  |
| 113 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 114 | PERC_CONCENT | NUMBER(5,2) | Y |  |  |
| 115 | DENSIDADE | NUMBER(5,2) | Y |  |  |
| 116 | COD_OPER_SC | NUMBER(2) | Y |  |  |
| 117 | COD_OPER_OBRIG_ORIG | NUMBER(2) | Y |  |  |
| 118 | COD_OPER_OBRIG | VARCHAR2(2) | Y |  |  |
| 119 | FATOR | NUMBER | Y |  |  |
| 120 | MSG_ERRO_PRE1 | VARCHAR2(4000) | Y |  |  |
| 121 | MSG_ERRO_PRE2 | VARCHAR2(4000) | Y |  |  |
| 122 | MSG_AVISO_PRE1 | VARCHAR2(4000) | Y |  |  |
| 123 | MSG_AVISO_PRE2 | VARCHAR2(4000) | Y |  |  |
| 124 | CHAVE | VARCHAR2(4000) | Y |  |  |

**Indexes**:
- IX_SC_PRE: (COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_PERIODO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, MOVTO_E_S, COD_OPER_OBRIG)

---

## SC_REG_MVI_A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_OPER_OBRIG | VARCHAR2(2) | Y |  |  |
| 4 | COD_PAIS_OBRIG | VARCHAR2(10) | Y |  |  |
| 5 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 6 | NUM_REG_EXP_IMP | VARCHAR2(15) | Y |  |  |
| 7 | DAT_EMBARQUE | DATE | Y |  |  |
| 8 | DAT_CONHEC_EMB | DATE | Y |  |  |
| 9 | NUM_RE | VARCHAR2(15) | Y |  |  |
| 10 | DAT_RE | DATE | Y |  |  |
| 11 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 12 | DAT_DI | DATE | Y |  |  |
| 13 | IND_ARMAZENAGEM | VARCHAR2(1) | Y |  |  |
| 14 | IND_TRANSPORTE | VARCHAR2(1) | Y |  |  |
| 15 | IND_ENTREGA | VARCHAR2(1) | Y |  |  |
| 16 | MSG_ERRO | VARCHAR2(4000) | Y |  |  |
| 17 | MSG_AVISO | VARCHAR2(4000) | Y |  |  |
| 18 | CHAVE | VARCHAR2(4000) | Y |  |  |
| 19 | TEXTO | VARCHAR2(4000) | Y |  |  |
| 20 | CHAVE_ORDENACAO | VARCHAR2(4000) | Y |  |  |
| 21 | REL | CHAR(3) | Y |  |  |

**Indexes**:
- IX_SC_REG_MVI_A: (COD_EMPRESA, COD_ESTAB, COD_OPER_OBRIG, COD_PAIS_OBRIG, RAZAO_SOCIAL, NUM_REG_EXP_IMP, DAT_EMBARQUE, DAT_CONHEC_EMB, NUM_RE, DAT_RE, NUM_DI, DAT_DI, IND_ARMAZENAGEM, IND_TRANSPORTE, IND_ENTREGA)

---

## SECAO_TIPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_SECAO_TIPI | NUMBER(2) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(100) | Y |  |  |

**PK**: COD_SECAO_TIPI

---

## SEC_ACCL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | OBJS_ID_OBJETO | NUMBER(19) | N |  |  |
| 2 | PAPE_ID_PAPEL | NUMBER(19) | N |  |  |
| 3 | PERM_ID_PERMISS | NUMBER(19) | N |  |  |

**PK**: OBJS_ID_OBJETO, PAPE_ID_PAPEL, PERM_ID_PERMISS

**FKs**:
- OBJS_ID_OBJETO → SEC_OBJS(OBJS_ID_OBJETO)
- PAPE_ID_PAPEL → SEC_PAPE(PAPE_ID_PAPEL)
- PERM_ID_PERMISS → SEC_PERM(PERM_ID_PERMISS)

---

## SEC_EMPR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPR_ID_EMPRESA | NUMBER(19) | N |  |  |
| 2 | EMPR_COD_EMPRESA | VARCHAR2(9) | N |  |  |
| 3 | EMPR_NUM_CNPJ | NUMBER(16) | Y |  |  |
| 4 | EMPR_COD_INSCEST | VARCHAR2(14) | Y |  |  |
| 5 | EMPR_COD_UF | CHAR(2) | Y |  |  |
| 6 | EMPR_COD_INSCMUN | VARCHAR2(14) | Y |  |  |
| 7 | EMPR_NOM_RAZSOC | VARCHAR2(150) | Y |  |  |
| 8 | EMPR_USR_ATUA | VARCHAR2(40) | N |  |  |
| 9 | EMPR_DAT_ATUA | DATE | N |  |  |

**PK**: EMPR_ID_EMPRESA

**Indexes**:
- UQ_SEC_EMPR1 (UNIQUE): (EMPR_COD_EMPRESA)

---

## SEC_FILI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FILI_ID_FILIAL | NUMBER(19) | N |  |  |
| 2 | FILI_COD_FILIAL | VARCHAR2(9) | N |  |  |
| 3 | EMPR_ID_EMPRESA | NUMBER(19) | N |  |  |
| 4 | FILI_NUM_CNPJ | NUMBER(16) | Y |  |  |
| 5 | FILI_COD_INSCEST | VARCHAR2(14) | Y |  |  |
| 6 | FILI_COD_UF | CHAR(2) | Y |  |  |
| 7 | FILI_COD_INSCMUN | VARCHAR2(14) | Y |  |  |
| 8 | FILI_NOM_RAZSOC | VARCHAR2(150) | Y |  |  |
| 9 | FILI_USR_ATUA | VARCHAR2(40) | N |  |  |
| 10 | FILI_DAT_ATUA | DATE | N |  |  |

**PK**: FILI_ID_FILIAL

**FKs**:
- EMPR_ID_EMPRESA → SEC_EMPR(EMPR_ID_EMPRESA)

**Indexes**:
- UQ_SEC_FILI1 (UNIQUE): (EMPR_ID_EMPRESA, FILI_COD_FILIAL)

---

## SEC_OBJS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | OBJS_ID_OBJETO | NUMBER(19) | N |  |  |
| 2 | OBJS_COD_OBJETO | VARCHAR2(20) | N |  |  |
| 3 | OBJS_DSC_OBJETO | VARCHAR2(250) | N |  |  |
| 4 | OBJS_USR_ATUA | VARCHAR2(40) | N |  |  |
| 5 | OBJS_DAT_ATUA | DATE | N |  |  |

**PK**: OBJS_ID_OBJETO

**Indexes**:
- UQ_SEC_OBJS1 (UNIQUE): (OBJS_COD_OBJETO)

---

## SEC_PAPE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PAPE_ID_PAPEL | NUMBER(19) | N |  |  |
| 2 | PAPE_COD_NOME | VARCHAR2(25) | N |  |  |
| 3 | PAPE_DSC_COD | VARCHAR2(250) | Y |  |  |
| 4 | PAPE_USR_ATUA | VARCHAR2(40) | N |  |  |
| 5 | PAPE_DAT_ATUA | DATE | N |  |  |

**PK**: PAPE_ID_PAPEL

---

## SEC_PERM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PERM_ID_PERMISS | NUMBER(19) | N |  |  |
| 2 | PERM_TIP_PERMISS | CHAR(1) | N |  |  |
| 3 | PERM_USR_ATUA | VARCHAR2(40) | N |  |  |
| 4 | PERM_DAT_ATUA | DATE | N |  |  |

**PK**: PERM_ID_PERMISS

**Indexes**:
- UQ_SEC_PERM1 (UNIQUE): (PERM_TIP_PERMISS)

---

## SEC_SEQU

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQU_COD_CAMPO | VARCHAR2(18) | N |  |  |
| 2 | SEQU_NUM_ID | NUMBER(19) | N |  |  |

**PK**: SEQU_COD_CAMPO, SEQU_NUM_ID

**Indexes**:
- UQ_SEC_SEQU1 (UNIQUE): (SEQU_COD_CAMPO)

---

## SEC_USPP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PAPE_ID_PAPEL | NUMBER(19) | N |  |  |
| 2 | USUA_ID_USUARIO | NUMBER(19) | N |  |  |
| 3 | FILI_ID_FILIAL | NUMBER(19) | N |  |  |
| 4 | USPP_USR_ATUA | VARCHAR2(40) | N |  |  |
| 5 | USPP_DAT_ATUA | DATE | N |  |  |

**PK**: PAPE_ID_PAPEL, USUA_ID_USUARIO, FILI_ID_FILIAL

**FKs**:
- FILI_ID_FILIAL → SEC_FILI(FILI_ID_FILIAL)
- PAPE_ID_PAPEL → SEC_PAPE(PAPE_ID_PAPEL)
- USUA_ID_USUARIO → SEC_USUA(USUA_ID_USUARIO)

---

## SEC_USUA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUA_ID_USUARIO | NUMBER(19) | N |  |  |
| 2 | USUA_NOM_LOGON | VARCHAR2(12) | N |  |  |
| 3 | USUA_NOM_PASSWD | VARCHAR2(44) | N |  |  |
| 4 | USUA_IND_CANCEL | CHAR(1) | N |  |  |
| 5 | USUA_NOM_NOMPROP | VARCHAR2(150) | Y |  |  |
| 6 | USUA_ACE_SEG | CHAR(1) | Y |  |  |
| 7 | USUA_USR_ATUA | VARCHAR2(40) | N |  |  |
| 8 | USUA_DAT_ATUA | DATE | N |  |  |

**PK**: USUA_ID_USUARIO

**Indexes**:
- UQ_SEQ_USUA1 (UNIQUE): (USUA_NOM_LOGON)

---

## SEGURANCA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | USUARIO | CHAR(40) | N |  |  |
| 2 | PASSWORD | CHAR(20) | N |  |  |
| 3 | NIVEL | CHAR(1) | Y |  |  |
| 4 | SETOR | VARCHAR2(25) | Y |  |  |
| 5 | DATA | DATE | Y |  |  |
| 6 | STATUS | CHAR(2) | Y |  |  |

**PK**: USUARIO

---

## SERV_MUNIC_GISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | COD_SERVICO_GISS | VARCHAR2(10) | N |  |  |
| 4 | VALID_SERVICO | DATE | N |  |  |
| 5 | DESC_SERVICO | VARCHAR2(500) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, COD_SERVICO_GISS, VALID_SERVICO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## SISTEMA_ORIGEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | CODIGO | VARCHAR2(4) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(60) | N |  |  |

**PK**: ID

**Indexes**:
- IU_SISTEMA_ORIGEM (UNIQUE): (CODIGO)

---

## SISTEMA_ORIGEM_EMPRESA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_SISTEMA_ORIGEM | NUMBER(38) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |

**PK**: ID_SISTEMA_ORIGEM, COD_EMPRESA

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)
- ID_SISTEMA_ORIGEM → SISTEMA_ORIGEM(ID)

---

## SISTEMA_ORIGEM_FILTRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | ID_SIS_ORIG | NUMBER(38) | Y |  |  |
| 3 | CONT_CONTA_CONT | NUMBER(1) | Y |  |  |
| 4 | CONT_NR_LANC | NUMBER(1) | Y |  |  |
| 5 | CONT_TIPO_DOC | NUMBER(1) | Y |  |  |
| 6 | FISC_TIPO_DOC | NUMBER(1) | Y |  |  |
| 7 | FISC_NR_DOC | NUMBER(1) | Y |  |  |
| 8 | FISC_COD_PF_PJ | NUMBER(1) | Y |  |  |

**PK**: ID

**FKs**:
- ID_SIS_ORIG → SISTEMA_ORIGEM(ID)

---

## SIT_TRIB_EST_A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ESTA_COD | CHAR(1) | N |  |  |
| 2 | ESTA_DAT_ATUA | DATE | N |  |  |
| 3 | ESTA_DSC | VARCHAR2(150) | Y |  |  |

**PK**: ESTA_COD, ESTA_DAT_ATUA

**Indexes**:
- SIT_TRIB_EST_AI2: (ESTA_COD)

---

## SIT_TRIB_EST_B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ESTB_COD | CHAR(2) | N |  |  |
| 2 | ESTB_DAT_ATUA | DATE | N |  |  |
| 3 | ESTB_DSC | VARCHAR2(150) | Y |  |  |

**PK**: ESTB_COD, ESTB_DAT_ATUA

**Indexes**:
- SIT_TRIB_EST_BI2: (ESTB_COD)

---

## SIT_TRIB_FED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | FEDE_COD | VARCHAR2(5) | N |  |  |
| 2 | FEDE_DAT_ATUA | DATE | N |  |  |
| 3 | FEDE_DSC | VARCHAR2(150) | Y |  |  |

**PK**: FEDE_COD, FEDE_DAT_ATUA

**Indexes**:
- SIT_TRIB_FEDI2: (FEDE_COD)

---

## SLD_COMPENSACAO_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_PAGTO | DATE | N |  |  |
| 4 | IDENT_DARF | NUMBER(12) | N |  |  |
| 5 | NRO_REFERENCIA_SLD | VARCHAR2(15) | N |  |  |
| 6 | DT_VENCTO | DATE | N |  |  |
| 7 | VLR_PGTO | NUMBER(17,2) | N |  |  |
| 8 | VLR_A_COMPENSAR | NUMBER(17,2) | N |  |  |
| 9 | VLR_COMPENSADO | NUMBER(17,2) | Y |  |  |
| 10 | OBSERVACAO | VARCHAR2(50) | Y |  |  |
| 11 | NRO_DOCTO_PAGTO | VARCHAR2(50) | Y |  |  |
| 12 | NUM_PROC_SLD | VARCHAR2(24) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | IND_ORIG_CREDITO | VARCHAR2(2) | Y |  |  |
| 15 | IND_TP_PROCESSO | NUMBER(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_PAGTO, IDENT_DARF, NRO_REFERENCIA_SLD, DT_VENCTO

---

## SMTP_USUARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SMTP | NUMBER(12) | N |  | Id da configuração |
| 2 | DSC_ALIAS | VARCHAR2(50) | Y |  | Nome de identificação da configuração |
| 3 | DSC_FROM | VARCHAR2(70) | Y |  | Descricao de quem envia |
| 4 | DSC_EMAIL_FROM | VARCHAR2(255) | Y |  | eMail de quem envia |
| 5 | DSC_SMTP_SERVER | VARCHAR2(255) | Y |  | Url do servidor SMTP |
| 6 | NUM_PORT | NUMBER(5) | Y |  | Porta do servidor |
| 7 | DSC_LOGIN | VARCHAR2(255) | Y |  | Usuario cadastrado no smtp com autorização de enviar |
| 8 | DSC_PASSWORD | VARCHAR2(100) | Y |  | Senha do usuário (informação criptografada) |
| 9 | IND_AUTHORITY | VARCHAR2(1) | Y |  | Indica se o servidor necessita de autenticação <S> <N> |
| 10 | IND_ENCRYPTION | VARCHAR2(1) | Y |  | Indica o tipo de criptografia utilizada pelo servidor 1-nenhum 2-SSL 3-TLS |
| 11 | DSC_STARTTLS | VARCHAR2(10) | Y |  | Indica a versão do TLS caso o IND_ENCRYPTION esteja com valor 3 |
| 12 | DAT_VALID | DATE | Y |  | Data de quando as configurações foram validadas no servidor pela ultima vez |
| 13 | COD_USUARIO | VARCHAR2(40) | Y |  | Descricão do usuário TR |
| 14 | IND_DEFAULT | VARCHAR2(1) | Y |  | Indica se a configuração é utilizada por padrão para o envio de emails |

**PK**: IDENT_SMTP

---

## SOFTWARE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_SOFTWARE | VARCHAR2(3) | N |  |  |
| 2 | DSC_SOFTWARE | VARCHAR2(50) | Y |  |  |
| 3 | IND_TIPO_SOFTWARE | CHAR(1) | Y |  |  |

**PK**: COD_SOFTWARE

---

## SOFTWARE_EQUIP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EQUIPAMENTO | VARCHAR2(3) | N |  |  |
| 2 | COD_SOFTWARE | VARCHAR2(3) | N |  |  |

**PK**: COD_EQUIPAMENTO, COD_SOFTWARE

**FKs**:
- COD_EQUIPAMENTO → EQUIPAMENTO(COD_EQUIPAMENTO)
- COD_SOFTWARE → SOFTWARE(COD_SOFTWARE)

---

## SPA_GRUPO_REGRAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_REGRA | VARCHAR2(3) | N |  |  |
| 2 | DSC_GRUPO_REGRA | VARCHAR2(255) | Y |  |  |

**PK**: GRUPO_REGRA

---

## SPA_RELAC_REGRAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_REGRA | VARCHAR2(3) | N |  |  |
| 2 | COD_REGRA | VARCHAR2(3) | N |  |  |
| 3 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 4 | DSC_REGRA | VARCHAR2(255) | Y |  |  |
| 5 | EXPRESSAO | VARCHAR2(3000) | Y |  |  |
| 6 | EXPRESSAO_PLSQL | VARCHAR2(4000) | Y |  |  |
| 7 | ESTAB_REGRA1 | VARCHAR2(4000) | Y |  |  |
| 8 | ESTAB_REGRA2 | VARCHAR2(4000) | Y |  |  |
| 9 | IND_ATIVO | CHAR(1) | Y |  |  |
| 10 | TIPO_INVENTARIO | CHAR(1) | Y |  | Parametro especifico para regra Inventario x Contabilidade, indica se o inventario sera por Produto (SAFX52) ou NBM (SAFX62) |

**PK**: GRUPO_REGRA, COD_REGRA

**FKs**:
- GRUPO_REGRA → SPA_GRUPO_REGRAS(GRUPO_REGRA)

---

## STG_ESOCIAL_INTEGRATOR
**Comment**: Tabela de Status do Integrador ESOCIAL Onesource

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_ESOCIAL_INTEGRATOR | NUMBER(22) | N |  |  |
| 2 | ALIAS | VARCHAR2(200) | Y |  |  |
| 3 | SERVIDOR | VARCHAR2(200) | Y |  |  |
| 4 | PROCESSO | VARCHAR2(200) | Y |  |  |
| 5 | VERSAO | VARCHAR2(30) | Y |  |  |
| 6 | OUTRAS_INFORMACOES | VARCHAR2(4000) | Y |  |  |
| 7 | DT_INICIO_PROCESSO | TIMESTAMP(6) | Y |  |  |
| 8 | DT_ULTIMO_RETORNO | TIMESTAMP(6) | Y |  |  |

**PK**: ID_STG_ESOCIAL_INTEGRATOR

---

## STG_EVENTOS_ESOCIAL_CONTROLE
**Comment**: Tabela de Controle do Integrador Onesource

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_EVENTOS_ESOCIAL_CONT | NUMBER(22) | N |  |  |
| 2 | ID_STG_EVENTOS_ESOCIAL_IN | NUMBER(22) | N |  |  |
| 3 | STATUS_PROC | VARCHAR2(8) | Y |  |  |
| 4 | PROCESSANDO | VARCHAR2(1) | Y |  | Campo de controle do Onesource. Caso tiver 0 ou null, não está processando, caso estiver com 1, está processando. |
| 5 | PROCESS_DATE | TIMESTAMP(6) | Y | CURRENT_TIMESTAMP |  |
| 6 | LIDO_INTEGRADOR | VARCHAR2(1) | Y | 'N' |  |

**PK**: ID_STG_EVENTOS_ESOCIAL_CONT

**FKs**:
- ID_STG_EVENTOS_ESOCIAL_IN → STG_EVENTOS_ESOCIAL_IN(ID_STG_EVENTOS_ESOCIAL_IN)

**Indexes**:
- FK_STG_EVT_ESOCIAL_CONTROLE_01: (ID_STG_EVENTOS_ESOCIAL_IN)

---

## STG_EVENTOS_ESOCIAL_IN
**Comment**: Esta tabela recebera o retorno do processamento do FISCO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_EVENTOS_ESOCIAL_IN | NUMBER(22) | N |  | Identificador Evento  |
| 2 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | N |  | Identificador Evento Enviado |
| 3 | PROTOCOLO_ONESOURCE | VARCHAR2(36) | Y |  | Esse campo representa o protocolo que identifica o lote contendo os eventos |
| 4 | STATUS_PROC | VARCHAR2(8) | Y |  | Status |
| 5 | XML_RETORNO | CLOB | Y |  | XML do Onesource |
| 6 | DT_CRIACAO | DATE | Y | SYSDATE |  |
| 7 | COD_MENSAGEM_ONESOURCE | VARCHAR2(8) | Y |  | Codigo de Mensagem do Onesource. |
| 8 | DES_MENSAGEM_ONESOURCE | VARCHAR2(4000) | Y |  | Descrição da Mensagem do Onesource. |
| 9 | ID_EVENTO_ONESOURCE | VARCHAR2(36) | Y |  | ID do Evento do Onesource |
| 10 | RECIBO_ONESOURCE | VARCHAR2(52) | Y |  | Recibo Fisco do Onesource |
| 11 | HASH_ONESOURCE | VARCHAR2(44) | Y |  | Hash Fiscal Status do Onesource |
| 12 | LIDO | VARCHAR2(1) | Y | 'N' | Campo de controle das soluções de origem[DW, GF E SMART]. o ONESOURCE sempre insere este campo como NULL. DW = N(ÃOPROCESSADO)/P(ROCESSANDO)/S(SIM-OK) |

**PK**: ID_STG_EVENTOS_ESOCIAL_IN

**FKs**:
- ID_STG_EVENTOS_ESOCIAL_OUT → STG_EVENTOS_ESOCIAL_OUT(ID_STG_EVENTOS_ESOCIAL_OUT)

**Indexes**:
- IDX_ID_STG_EVENTOS_ESOCIAL_OUT: (ID_STG_EVENTOS_ESOCIAL_OUT)

---

## STG_EVENTOS_ESOCIAL_OUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_EVENTOS_ESOCIAL_OUT | NUMBER(22) | N |  | Identificador da Tabela |
| 2 | TIPO_EVENTO | VARCHAR2(50) | Y |  | Conteudo gerado pela solução Fiscal Exemplo: S-1005 |
| 3 | XML_ENVIO | CLOB | Y |  | Arquivo xml gerado do evento  |
| 4 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificação da Origem do evento. Solução fiscal grava a informação. |
| 5 | LIDO | VARCHAR2(1) | Y |  | Campo é controlado pelo Onesource. Onde será considerado 0 ou NULL como um registro não enviado para a solução Onesource e 1 como registro já enviado |
| 6 | TIPO_AMBIENTE | VARCHAR2(1) | Y |  | Tipo do ambiente: 1 - Produção, 2 - Produção Restrita  |
| 7 | DT_CRIACAO | DATE | Y | SYSDATE | Data da da disponibilização do evento na tabela |

**PK**: ID_STG_EVENTOS_ESOCIAL_OUT

**Indexes**:
- IX_STG_EVENTOS_ESOCIAL_OUT_01: (ID_EVENTO)

---

## STG_EVENTOS_REINF_CONTROLE
**Comment**: Tabela de Controle do Integrador Onesource

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_EVENTOS_REINF_CONT | NUMBER(22) | N |  |  |
| 2 | ID_STG_EVENTOS_REINF_IN | NUMBER(22) | N |  |  |
| 3 | STATUS_PROC | VARCHAR2(8) | Y |  |  |
| 4 | PROCESSANDO | VARCHAR2(1) | Y |  | Campo de controle do Onesource. Caso tiver 0 ou null, não está processando, caso estiver com 1, está processando. |
| 5 | PROCESS_DATE | TIMESTAMP(6) | Y | CURRENT_TIMESTAMP |  |

**PK**: ID_STG_EVENTOS_REINF_CONT

**FKs**:
- ID_STG_EVENTOS_REINF_IN → STG_EVENTOS_REINF_IN(ID_STG_EVENTOS_REINF_IN)

**Indexes**:
- IDX_REINF_CONTROLE_PROC: (ID_STG_EVENTOS_REINF_IN, PROCESSANDO, STATUS_PROC, PROCESS_DATE)
- ID_STG_EVENTOS_REINF_IN: (ID_STG_EVENTOS_REINF_IN)

---

## STG_EVENTOS_REINF_IN
**Comment**: Esta tabela recebera o retorno do processamento do FISCO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_EVENTOS_REINF_IN | NUMBER(22) | N |  | Identificador Evento  |
| 2 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | N |  | Identificador Evento Enviado |
| 3 | PROTOCOLO_ONESOURCE | VARCHAR2(36) | Y |  | Esse campo representa o protocolo que identifica o lote contendo os eventos |
| 4 | STATUS_PROC | VARCHAR2(8) | Y |  | Status |
| 5 | XML_RETORNO | CLOB | Y |  | XML do Onesource |
| 6 | DT_CRIACAO | DATE | Y | SYSDATE |  |
| 7 | COD_MENSAGEM_ONESOURCE | VARCHAR2(8) | Y |  | Codigo de Mensagem do Onesource. |
| 8 | DES_MENSAGEM_ONESOURCE | VARCHAR2(4000) | Y |  | Descrição da Mensagem do Onesource. |
| 9 | ID_EVENTO_ONESOURCE | VARCHAR2(36) | Y |  | ID do Evento do Onesource |
| 10 | RECIBO_ONESOURCE | VARCHAR2(52) | Y |  | Recibo Fisco do Onesource |
| 11 | HASH_ONESOURCE | VARCHAR2(44) | Y |  | Hash Fiscal Status do Onesource |
| 12 | LIDO | VARCHAR2(1) | Y | 'N' | Campo de controle das soluções de origem[DW, GF E SMART]. o ONESOURCE sempre insere este campo como NULL. DW = N(ÃOPROCESSADO)/P(ROCESSANDO)/S(SIM-OK) |

**PK**: ID_STG_EVENTOS_REINF_IN

**FKs**:
- ID_STG_EVENTOS_REINF_OUT → STG_EVENTOS_REINF_OUT(ID_STG_EVENTOS_REINF_OUT)

**Indexes**:
- IDX_ID_STG_EVENTOS_REINF_OUT: (ID_STG_EVENTOS_REINF_OUT)
- IDX_REINF_IN_OUT_MAX: (ID_STG_EVENTOS_REINF_OUT, SYS_NC00013$)
- IX_EVENTOS_NLIDOS: (LIDO, ID_STG_EVENTOS_REINF_IN)
- IX_STGEVENTIN_IDDT: (ID_EVENTO_ONESOURCE, DT_CRIACAO)
- IX_STGEVENTIN_PROT: (PROTOCOLO_ONESOURCE)
- IX_STG_EVENTOS_REINF_IN_02: (ID_STG_EVENTOS_REINF_IN, ID_STG_EVENTOS_REINF_OUT)
- IX_STG_EVENTOS_REINF_IN_03: (ID_EVENTO_ONESOURCE)

---

## STG_EVENTOS_REINF_LEGADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_EVENTOS_REINF_LEGADO | NUMBER(22) | N |  |  |
| 2 | ID_EVENTO | VARCHAR2(36) | Y |  |  |
| 3 | TIPO_EVENTO | VARCHAR2(50) | Y |  |  |
| 4 | RECIBO_ONESOURCE | VARCHAR2(52) | Y |  |  |
| 5 | DT_CRIACAO | DATE | Y | SYSDATE |  |
| 6 | COD_MENSAGEM_ONESOURCE | VARCHAR2(8) | Y |  |  |
| 7 | DES_MENSAGEM_ONESOURCE | VARCHAR2(4000) | Y |  |  |
| 8 | LIDO | VARCHAR2(1) | Y |  |  |
| 9 | XML_EVENTO_ASSINADO | CLOB | Y |  |  |
| 10 | XML_LOTE_RETORNO | CLOB | Y |  |  |

**PK**: ID_STG_EVENTOS_REINF_LEGADO

**Indexes**:
- IX_STG_EV_REINF_LEG_01: (ID_EVENTO)

---

## STG_EVENTOS_REINF_OUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_EVENTOS_REINF_OUT | NUMBER(22) | N |  |  |
| 2 | TIPO_EVENTO | VARCHAR2(50) | Y |  | Conteudo gerado pela solução Fiscal. Exemplo: R-1000,R-1070.. etc   |
| 3 | XML_ENVIO | CLOB | Y |  |  |
| 4 | ID_EVENTO | VARCHAR2(36) | Y |  | Identificação da Origem do evento. Solução fiscal grava a informação. |
| 5 | LIDO | VARCHAR2(1) | Y | 0 | Campo é controlado pelo Onesource. Onde será considerado 0 ou NULL como um registro não enviado para a solução Onesource e 1 como registro já enviado |
| 6 | TIPO_AMBIENTE | VARCHAR2(1) | Y |  | Tipo do ambiente: 1 - Produção, 2 - Pré-produção - dados reais, 3 - Pré-produção - dados fictícios, 0 - Ignora o filtro  |
| 7 | DT_CRIACAO | DATE | Y | SYSDATE | Data da da disponibilização do evento na tabela  |
| 8 | NAFILA | VARCHAR2(1) | Y |  |  |

**PK**: ID_STG_EVENTOS_REINF_OUT

**Indexes**:
- IDX_REINF_OUT_LIDO: (LIDO)
- IDX_REINF_OUT_NAFILA_DT: (ID_STG_EVENTOS_REINF_OUT, TIPO_AMBIENTE, NAFILA, DT_CRIACAO)
- IDX_STG_EVENTOS_REINF_OUT_ID: (ID_EVENTO)

---

## STG_REINF_INTEGRATOR
**Comment**: Tabela de Status do Integrador Reinf Onesource.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_STG_REINF_INTEGRATOR | NUMBER(22) | N |  |  |
| 2 | ALIAS | VARCHAR2(200) | Y |  | Nome do Servidor. |
| 3 | SERVIDOR | VARCHAR2(200) | Y |  | Nome do Servidor. |
| 4 | PROCESSO | VARCHAR2(200) | Y |  | Processo. |
| 5 | VERSAO | VARCHAR2(30) | Y |  | Versão do Integrador do Onesource. |
| 6 | OUTRAS_INFORMACOES | VARCHAR2(4000) | Y |  | Dados de Inicialização do Integrador. |
| 7 | DT_INICIO_PROCESSO | TIMESTAMP(6) | Y |  | Data e hora que inicializou o Integrador. |
| 8 | DT_ULTIMO_RETORNO | TIMESTAMP(6) | Y |  | Data e Hora da ultima atualização de status. |
| 9 | TIPO_AMBIENTE | VARCHAR2(1) | Y |  |  |

**PK**: ID_STG_REINF_INTEGRATOR

---

## STIP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GTIP_GRUPO | CHAR(4) | N |  |  |
| 2 | STIP_GRUPO | VARCHAR2(6) | N |  |  |
| 3 | STIP_DESC1 | VARCHAR2(500) | Y |  |  |

**PK**: GTIP_GRUPO, STIP_GRUPO

---

## ST_CASO_TESTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROJETO | VARCHAR2(30) | N |  |  |
| 2 | COD_GRUPO_TESTE | VARCHAR2(30) | N |  |  |
| 3 | COD_CASO_TESTE | VARCHAR2(60) | N |  |  |
| 4 | DATA_TESTE | DATE | N |  |  |
| 5 | DSC_COMENTARIO | VARCHAR2(500) | Y |  |  |
| 6 | IND_TESTE_UNIT | VARCHAR2(1) | Y |  |  |
| 7 | PERC_COBERTURA | NUMBER(5,2) | Y |  |  |

**PK**: COD_PROJETO, COD_GRUPO_TESTE, COD_CASO_TESTE, DATA_TESTE

**Indexes**:
- IX_CASO_TESTE_01: (COD_PROJETO, COD_GRUPO_TESTE)

---

## ST_CASO_TESTE_COBERTURA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROJETO | VARCHAR2(30) | N |  |  |
| 2 | COD_GRUPO_TESTE | VARCHAR2(30) | N |  |  |
| 3 | COD_CASO_TESTE | VARCHAR2(60) | N |  |  |
| 4 | DATA_TESTE | DATE | N |  |  |
| 5 | NOME_FUNCAO | VARCHAR2(30) | N |  |  |
| 6 | STATUS | VARCHAR2(1) | Y |  |  |

**PK**: COD_PROJETO, COD_GRUPO_TESTE, COD_CASO_TESTE, DATA_TESTE, NOME_FUNCAO

---

## ST_CASO_TESTE_INATIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROJETO | VARCHAR2(30) | N |  |  |
| 2 | COD_GRUPO_TESTE | VARCHAR2(30) | N |  |  |
| 3 | COD_CASO_TESTE | VARCHAR2(30) | N |  |  |

**PK**: COD_PROJETO, COD_GRUPO_TESTE, COD_CASO_TESTE

---

## ST_CASO_TESTE_RESULT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROJETO | VARCHAR2(30) | N |  |  |
| 2 | COD_GRUPO_TESTE | VARCHAR2(30) | N |  |  |
| 3 | COD_CASO_TESTE | VARCHAR2(60) | N |  |  |
| 4 | DATA_TESTE | DATE | N |  |  |
| 5 | NUM_TESTE | NUMBER(10) | N |  |  |
| 6 | SEQ_TESTE | NUMBER(5) | N |  |  |
| 7 | DESCRICAO | VARCHAR2(500) | Y |  |  |
| 8 | LOGIN | VARCHAR2(30) | Y |  |  |
| 9 | STATUS | NUMBER(1) | Y |  |  |
| 10 | MSG_ERRO | VARCHAR2(500) | Y |  |  |
| 11 | DATA_INI | DATE | Y |  |  |
| 12 | DATA_FIM | DATE | Y |  |  |
| 13 | TEMPO_DURACAO | NUMBER(17) | Y |  |  |
| 14 | MSG_ERRO_CLOB | CLOB | Y |  |  |
| 15 | ARQ_ESPERADO | CLOB | Y |  |  |
| 16 | ARQ_OBTIDO | CLOB | Y |  |  |
| 17 | TIPO_ERRO | NUMBER(1) | Y |  |  |
| 18 | NOME_ARQ_ESPERADO | VARCHAR2(500) | Y |  |  |
| 19 | NOME_ARQ_OBTIDO | VARCHAR2(500) | Y |  |  |
| 20 | DSC_COMENTARIO | VARCHAR2(500) | Y |  |  |
| 21 | STATUS_ORIG | NUMBER(1) | Y |  |  |

**PK**: COD_PROJETO, COD_GRUPO_TESTE, COD_CASO_TESTE, DATA_TESTE, NUM_TESTE, SEQ_TESTE

**Indexes**:
- IX_ST_CASO_TESTE_RESULT: (COD_PROJETO, COD_GRUPO_TESTE)
- IX_ST_CASO_TESTE_RESULT_01: (COD_PROJETO)

---

## ST_GRUPO_TESTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROJETO | VARCHAR2(30) | N |  |  |
| 2 | COD_GRUPO_TESTE | VARCHAR2(30) | N |  |  |

**PK**: COD_PROJETO, COD_GRUPO_TESTE

---

## ST_PROJETO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROJETO | VARCHAR2(30) | N |  |  |
| 2 | DSC_PROJETO | VARCHAR2(50) | N |  |  |

**PK**: COD_PROJETO

---

## ST_USUARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LOGIN | VARCHAR2(30) | N |  |  |
| 2 | NOME | VARCHAR2(30) | Y |  |  |
| 3 | SENHA | VARCHAR2(15) | Y |  |  |
| 4 | IND_ADM | NUMBER(1) | Y |  |  |

**PK**: LOGIN

---

## ST_USUARIO_PROJETO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LOGIN | VARCHAR2(30) | N |  |  |
| 2 | COD_PROJETO | VARCHAR2(30) | N |  |  |

**PK**: LOGIN, COD_PROJETO

---

## SUBGRUPO_SELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRUPO_SELO | NUMBER(2) | N |  |  |
| 2 | COD_SUBGRUPO_SELO | NUMBER(2) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | COD_SELO | VARCHAR2(6) | Y |  |  |

**PK**: COD_GRUPO_SELO, COD_SUBGRUPO_SELO

**FKs**:
- COD_GRUPO_SELO → GRUPO_SELO(COD_GRUPO_SELO)

---

## SX07_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IND_OPERACAO | VARCHAR2(1) | N | 'I' | Indicador de Operacao: I - Insert, U - Update, D - Delete. |

**PK**: DAT_ALTERACAO, COD_ESTAB, COD_EMPRESA, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## SX08_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 13 | IND_OPERACAO | VARCHAR2(1) | N | 'I' |  |

---

## SX09_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 13 | NUM_ITEM | NUMBER(5) | N |  |  |
| 14 | IND_OPERACAO | VARCHAR2(1) | N | 'I' |  |

---

## SX3007_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IND_OPERACAO | VARCHAR2(1) | N | 'I' | Indicador de Operacao: I - Insert, U - Update, D - Delete. |

**PK**: DAT_ALTERACAO, COD_ESTAB, COD_EMPRESA, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## SX3008_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 13 | IND_OPERACAO | VARCHAR2(1) | N | 'I' | Indicador de Operacao: I - Insert, U - Update, D - Delete. |

**PK**: DAT_ALTERACAO, COD_ESTAB, COD_EMPRESA, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## SX3009_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_FISCAL | DATE | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | IDENT_SERVICO | NUMBER(5) | N |  |  |
| 13 | NUM_ITEM | NUMBER(4) | N |  |  |
| 14 | IND_OPERACAO | VARCHAR2(1) | N | 'I' | Indicador de Operacao: I - Insert, U - Update, D - Delete. |

**PK**: DAT_ALTERACAO, COD_ESTAB, COD_EMPRESA, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM

---

## SX3042_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_FISCAL | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IND_OPERACAO | VARCHAR2(1) | N | 'I' | Indicador de Operacao: I - Insert, U - Update, D - Delete. |

**PK**: DAT_ALTERACAO, COD_ESTAB, COD_EMPRESA, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## SX3043_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_FISCAL | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | NUM_ITEM | NUMBER(4) | N |  |  |
| 10 | IND_OPERACAO | VARCHAR2(1) | N | 'I' | Indicador de Operacao: I - Insert, U - Update, D - Delete. |

**PK**: DAT_ALTERACAO, COD_ESTAB, COD_EMPRESA, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM

---

## SX42_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_FISCAL | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IND_OPERACAO | VARCHAR2(1) | N | 'I' | Indicador de Operacao: I - Insert, U - Update, D - Delete. |

**PK**: DAT_ALTERACAO, COD_ESTAB, COD_EMPRESA, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

---

## SX43_DAT_ALTERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DAT_ALTERACAO | DATE | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DAT_FISCAL | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | NUM_ITEM | NUMBER(7) | N |  |  |
| 10 | IND_OPERACAO | VARCHAR2(1) | N | 'I' |  |

---

## T1_BR_CADASTRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | VARCHAR2(6) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 3 | DICIONARIO_ID | VARCHAR2(6) | Y |  |  |

**PK**: ID

**FKs**:
- DICIONARIO_ID → T1_BR_DICIONARIO(ID)

**Indexes**:
- IX_T1_BR_CADASTRO1: (DESCRICAO, ID)
- IX_T1_BR_CADASTRO2: (DICIONARIO_ID, ID)

---

## T1_BR_COLUNAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_CADASTRO | VARCHAR2(6) | N |  |  |
| 2 | ID | VARCHAR2(6) | N |  |  |
| 3 | NOME_TAB_BD | VARCHAR2(128) | Y |  |  |
| 4 | NOME_COLUNA | VARCHAR2(128) | Y |  |  |
| 5 | TIPO | VARCHAR2(20) | Y |  |  |
| 6 | AGRUPAMENTO | VARCHAR2(20) | Y |  |  |
| 7 | OPERADOR | VARCHAR2(20) | Y |  |  |
| 8 | VALOR | VARCHAR2(4000) | Y |  |  |
| 9 | ORDENACAO | VARCHAR2(20) | Y |  |  |

**PK**: ID_CADASTRO, ID

**FKs**:
- ID_CADASTRO → T1_BR_CADASTRO(ID)

**Indexes**:
- UX_T1_BR_COLUNAS (UNIQUE): (ID_CADASTRO, NOME_TAB_BD, NOME_COLUNA, TIPO, AGRUPAMENTO, OPERADOR)

---

## T1_BR_DADOS_ADIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_CADASTRO | VARCHAR2(6) | N |  |  |
| 2 | ID | VARCHAR2(6) | N |  |  |
| 3 | NOME_TABELA | VARCHAR2(4000) | Y |  |  |
| 4 | NOME_TAB_BD | VARCHAR2(128) | Y |  |  |
| 5 | CONSTRAINT_NAME | VARCHAR2(128) | Y |  |  |

**PK**: ID_CADASTRO, ID

**FKs**:
- ID_CADASTRO → T1_BR_CADASTRO(ID)

---

## T1_BR_DICIONARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | VARCHAR2(6) | N |  |  |
| 2 | NOME | VARCHAR2(200) | N |  |  |
| 3 | TABELAS | VARCHAR2(4000) | Y |  |  |
| 4 | SQL_CORE | VARCHAR2(4000) | Y |  |  |
| 5 | DT_ATUALIZACAO | DATE | Y |  |  |

**PK**: ID

**Indexes**:
- IX_T1_BR_DICIONARIO: (NOME, ID)

---

## T1_BR_DIC_FILTROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DICIONARIO | VARCHAR2(6) | N |  |  |
| 2 | ID | VARCHAR2(6) | N |  |  |
| 3 | NOME_TAB_BD | VARCHAR2(128) | N |  |  |
| 4 | NOME_COLUNA | VARCHAR2(128) | N |  |  |
| 5 | OPERADOR | VARCHAR2(20) | N |  |  |
| 6 | PARAMETRO | VARCHAR2(4000) | N |  |  |

**PK**: ID_DICIONARIO, ID

**FKs**:
- ID_DICIONARIO → T1_BR_DICIONARIO(ID)

**Indexes**:
- UK_DIC_FILTROS (UNIQUE): (ID_DICIONARIO, NOME_TAB_BD, NOME_COLUNA, OPERADOR)

---

## TAB_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TAB_PROC | NUMBER(5) | N |  |  |
| 2 | DSC_TAB_PROC | VARCHAR2(50) | Y |  |  |
| 3 | NOME_BD | VARCHAR2(30) | Y |  |  |
| 4 | COLUNA_DATA_INIC | VARCHAR2(20) | Y |  |  |

**PK**: COD_TAB_PROC

---

## TAEX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | INFSM_SERIE | VARCHAR2(5) | N |  |  |
| 4 | INFSM_NUM | VARCHAR2(15) | N |  |  |
| 5 | INFSM_DTEMISS | DATE | N |  |  |
| 6 | TAEX_COD_RE | VARCHAR2(15) | N |  |  |
| 7 | MATE_COD | VARCHAR2(60) | N |  |  |
| 8 | TAEX_COD_RELA | NUMBER(2) | Y |  |  |
| 9 | TAEX_DAT_RE | DATE | Y |  |  |
| 10 | TAEX_COD_DE | VARCHAR2(15) | Y |  |  |
| 11 | TAEX_DAT_DE | DATE | Y |  |  |
| 12 | TAEX_COD_AVERB | CHAR(1) | Y |  |  |
| 13 | TAEX_DSC_COEMB | VARCHAR2(18) | Y |  |  |
| 14 | TAEX_DAT_COEMB | DATE | Y |  |  |
| 15 | TDOC_COD | CHAR(2) | Y |  |  |
| 16 | TAEX_COD_PAIS | CHAR(4) | Y |  |  |
| 17 | TAEX_DSC_COMEX | VARCHAR2(8) | Y |  |  |
| 18 | TAEX_DAT_COMEX | DATE | Y |  |  |
| 19 | MDOC_COD | CHAR(3) | Y |  |  |
| 20 | TAEX_NEXP | CHAR(1) | Y |  |  |
| 21 | TAEX_DAT_AVERB | DATE | Y |  |  |
| 22 | NUM01 | NUMBER | Y |  |  |
| 23 | NUM02 | NUMBER | Y |  |  |
| 24 | NUM03 | NUMBER | Y |  |  |
| 25 | VAR01 | VARCHAR2(150) | Y |  |  |
| 26 | VAR02 | VARCHAR2(150) | Y |  |  |
| 27 | VAR03 | VARCHAR2(150) | Y |  |  |
| 28 | VAR04 | VARCHAR2(150) | Y |  |  |
| 29 | VAR05 | VARCHAR2(150) | Y |  |  |
| 30 | TAEX_IND_DOC | CHAR(1) | Y |  |  |
| 31 | TAEX_CHV_NFE | VARCHAR2(44) | Y |  |  |
| 32 | TAEX_MOEDA | VARCHAR2(10) | Y |  |  |
| 33 | INFSM_NUM_ITEM | VARCHAR2(5) | N |  |  |

**PK**: EMPS_COD, FILI_COD, INFSM_SERIE, INFSM_NUM, INFSM_DTEMISS, TAEX_COD_RE, MATE_COD, INFSM_NUM_ITEM

---

## TB_MSAF_LOTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_LOTE | VARCHAR2(20) | Y |  |  |
| 2 | COD_PIN | VARCHAR2(30) | Y |  |  |
| 3 | DATA_GERACAO | DATE | Y |  |  |
| 4 | DATA_ENVIO | DATE | Y |  |  |
| 5 | DATA_RETORNO | DATE | Y |  |  |

---

## TB_MSAF_NF_LOTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 8 | IDENT_CFO | NUMBER(12) | N |  |  |
| 9 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 10 | COD_CFO | VARCHAR2(4) | N |  |  |
| 11 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 15 | DATA_GERACAO | DATE | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(20) | Y |  |  |
| 17 | TIPO_NOTA | CHAR(1) | Y |  |  |
| 18 | CNPJ_TRANSP | VARCHAR2(20) | Y |  |  |
| 19 | STATUS | CHAR(1) | N |  |  |
| 20 | COD_PIN | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_MODELO, IDENT_CFO, COD_MODELO, COD_CFO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, STATUS

---

## TCOF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TCOF_DAT | DATE | N |  |  |
| 2 | TCOF_COD | CHAR(2) | N |  |  |
| 3 | TCOF_DSC | VARCHAR2(150) | Y |  |  |

**PK**: TCOF_DAT, TCOF_COD

---

## TEMP_ZERO_CALEND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COLUNA | CHAR(1) | Y |  |  |

---

## TFT_GUIA_CFEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 8 | TOT_QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 9 | VLR_TOT_OPER | NUMBER(17,2) | Y |  |  |
| 10 | VLR_FATUR_LIQ | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CFEM_RECOLHER | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 15 | DSC_PROD_SUBST | VARCHAR2(50) | Y |  |  |
| 16 | VLR_ALIQ_CFEM | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO, COD_MUNICIPIO, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## TFT_MOVTO_CFEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | COD_OPER_CFEM | CHAR(1) | N |  |  |
| 13 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 14 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 15 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 17 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TRIBUTO_PISCOFINS | NUMBER(17,2) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, IDENT_PRODUTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_OPER_CFEM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- IX_FK_SAF_1277: (IDENT_FIS_JUR)

---

## TFT_PAR_CFO_CFEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CFO | VARCHAR2(4) | N |  |  |
| 4 | COD_OPER_CFEM | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## TFT_PAR_OPER_CFEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_OPERACAO | VARCHAR2(9) | N |  |  |
| 4 | COD_OPERACAO | VARCHAR2(6) | N |  |  |
| 5 | COD_OPER_CFEM | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_OPERACAO, COD_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## TFT_PAR_PRD_CFEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | VLR_ALIQ_CFEM | NUMBER(7,4) | Y |  |  |
| 7 | COD_SUBSTANCIA | VARCHAR2(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, COD_SUBSTANCIA → TFT_PAR_SUBST_CFEM(COD_EMPRESA, COD_ESTAB, COD_SUBSTANCIA)

---

## TFT_PAR_SUBST_CFEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_SUBSTANCIA | VARCHAR2(5) | N |  |  |
| 4 | DSC_SUBSTANCIA | VARCHAR2(50) | Y |  |  |
| 5 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 6 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 7 | VLR_ALIQ_CFEM | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_SUBSTANCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## TFT_SEGURO_VENDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | SEQ_LINHA | NUMBER(2) | N |  |  |
| 8 | DSC_SEGURO | VARCHAR2(50) | Y |  |  |
| 9 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO, COD_MUNICIPIO, IDENT_PRODUTO, SEQ_LINHA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## TFT_TOT_OPER_CFEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | COD_SUBSTANCIA | VARCHAR2(5) | Y |  |  |
| 6 | IDENT_MEDIDA_PROD | NUMBER(12) | Y |  |  |
| 7 | IDENT_MEDIDA_SUBST | NUMBER(12) | Y |  |  |
| 8 | QTD_VENDA_PROD | NUMBER(17,6) | Y |  |  |
| 9 | QTD_VENDA_SUBST | NUMBER(17,6) | Y |  |  |
| 10 | VLR_VENDA | NUMBER(17,2) | Y |  |  |
| 11 | QTD_TRANSFORMACAO_PROD | NUMBER(17,6) | Y |  |  |
| 12 | QTD_TRANSFORMACAO_SUBST | NUMBER(17,6) | Y |  |  |
| 13 | VLR_TRANSFORMACAO | NUMBER(17,2) | Y |  |  |
| 14 | QTD_CONSUMO_PROD | NUMBER(17,6) | Y |  |  |
| 15 | QTD_CONSUMO_SUBST | NUMBER(17,6) | Y |  |  |
| 16 | VLR_CONSUMO | NUMBER(17,2) | Y |  |  |
| 17 | QTD_UTILIZACAO_PROD | NUMBER(17,6) | Y |  |  |
| 18 | QTD_UTILIZACAO_SUBST | NUMBER(17,6) | Y |  |  |
| 19 | VLR_UTILIZACAO | NUMBER(17,2) | Y |  |  |
| 20 | QTD_TOTAL_PROD | NUMBER(17,6) | Y |  |  |
| 21 | QTD_TOTAL_SUBST | NUMBER(17,6) | Y |  |  |
| 22 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA_PROD → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_MEDIDA_SUBST → X2007_MEDIDA(IDENT_MEDIDA)

---

## TFT_TRANSP_VENDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | SEQ_LINHA | NUMBER(2) | N |  |  |
| 8 | DSC_TRANSP | VARCHAR2(50) | Y |  |  |
| 9 | VLR_TRANSP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO, COD_MUNICIPIO, IDENT_PRODUTO, SEQ_LINHA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## TFT_TRIB_RECOL_MES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | IND_TP_TRIBUTO | CHAR(1) | N |  |  |
| 8 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 9 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO, COD_MUNICIPIO, IDENT_PRODUTO, IND_TP_TRIBUTO, COD_TRIBUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- COD_TRIBUTO → DWT_TRIBUTO(COD_TRIBUTO)

---

## TIPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPI_DAT | DATE | N |  |  |
| 2 | TIPI_COD | CHAR(2) | N |  |  |
| 3 | TIPI_DSC | VARCHAR2(150) | Y |  |  |

**PK**: TIPI_DAT, TIPI_COD

---

## TIPO_CONSOLIDACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_CONSOL | VARCHAR2(2) | N |  |  |
| 2 | DSC_TIPO_CONSOL | VARCHAR2(50) | Y |  |  |

**PK**: COD_TIPO_CONSOL

---

## TIPO_DOCUMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TDOC_COD | CHAR(5) | N |  |  |
| 2 | TDOC_NF | CHAR(1) | Y |  |  |
| 3 | TDOC_DAT_ATUA | DATE | N |  |  |
| 4 | TDOC_DSC | VARCHAR2(150) | Y |  |  |
| 5 | TDOC_COD86 | CHAR(3) | Y |  |  |
| 6 | TDOC_CAT83 | NUMBER(3) | Y |  |  |

**PK**: TDOC_COD, TDOC_DAT_ATUA

**Indexes**:
- TIPO_DOCUMENTOI2: (TDOC_COD)

---

## TIPO_DOCUMENTO_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TDOC_COD | CHAR(5) | Y |  |  |
| 2 | TDOC_NF | CHAR(1) | Y |  |  |
| 3 | TDOC_DAT_ATUA | DATE | Y |  |  |
| 4 | TDOC_DSC | VARCHAR2(150) | Y |  |  |
| 5 | TDOC_COD86 | CHAR(3) | Y |  |  |
| 6 | TDOC_CAT83 | CHAR(3) | Y |  |  |

---

## TIPO_ESTORNO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTORNO | VARCHAR2(2) | N |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTORNO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## TIPO_LIVRO_APURAC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 2 | IND_TRIBUTO | CHAR(1) | Y |  |  |

**PK**: COD_TIPO_LIVRO

**FKs**:
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## TIPO_LIVRO_FISCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 2 | NOM_OFICIAL | VARCHAR2(50) | Y |  |  |
| 3 | NOM_REDUZIDO | VARCHAR2(50) | Y |  |  |
| 4 | IND_MEIO_EMISSAO | CHAR(1) | Y |  |  |
| 5 | IND_ORGAO_RESP | CHAR(1) | Y |  |  |
| 6 | IND_CAT_TIPO_LIVRO | CHAR(1) | Y |  |  |
| 7 | VAL_LIMITE_PAGINA | NUMBER(4) | Y |  |  |
| 8 | IND_CENTR | CHAR(1) | Y |  |  |
| 9 | IND_ENT_SAI | CHAR(1) | Y |  |  |
| 10 | IND_IPI | CHAR(1) | Y |  |  |
| 11 | IND_INCENT1 | CHAR(1) | Y |  |  |
| 12 | IND_INCENT2 | CHAR(1) | Y |  |  |
| 13 | IND_INCENT3 | CHAR(1) | Y |  |  |
| 14 | IND_TEM_CONSOLIDADO | CHAR(1) | Y |  |  |
| 15 | IND_INCENT4 | CHAR(1) | Y |  |  |

**PK**: COD_TIPO_LIVRO

---

## TIPO_MIDIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_MIDIA | VARCHAR2(3) | N |  |  |
| 2 | DSC_TIPO_MIDIA | VARCHAR2(50) | Y |  |  |
| 3 | DSC_DENSIDADE | VARCHAR2(30) | Y |  |  |
| 4 | VAL_FATOR_BLOCO | NUMBER(5) | Y |  |  |
| 5 | VAL_TAM_BLOCO | NUMBER(5) | Y |  |  |

**PK**: COD_TIPO_MIDIA

---

## TIPO_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TOPE_COD | VARCHAR2(6) | N |  |  |
| 2 | TOPE_DAT_ATUA | DATE | N |  |  |
| 3 | TOPE_DSC | VARCHAR2(150) | Y |  |  |
| 4 | TOPE_COD_ENTRA | CHAR(1) | Y |  |  |
| 5 | TOPE_COD_SAIDA | CHAR(1) | Y |  |  |
| 6 | TOPE_DEPREC | CHAR(1) | Y |  |  |
| 7 | IND_EST | CHAR(1) | Y |  |  |
| 8 | IND_INV | CHAR(1) | Y |  |  |
| 9 | TOPE_COD86 | CHAR(1) | Y |  |  |

**PK**: TOPE_COD, TOPE_DAT_ATUA

**Indexes**:
- TIPO_OPERACAOI2: (TOPE_DAT_ATUA, TOPE_COD)

---

## TOTAL_CFO_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 6 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 7 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 10 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 11 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 13 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 15 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 16 | VLR_IPI_NEMBUT | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_CFO_TRIB_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_CFO, TITULO_TRIBUTO)
- IX_TOTAL_CFO_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## TOTAL_CFO_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 6 | COD_CFO_SUP | VARCHAR2(4) | Y |  |  |
| 7 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 8 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 9 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 10 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 11 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 13 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 15 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 16 | VLR_IPI_NEMBUT | NUMBER(17,2) | Y |  |  |
| 17 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX_CFO_TRIB_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_CFO, TITULO_TRIBUTO)
- IX_TOTAL_CFO_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## TOTAL_ENTRADA_P1

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 6 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 7 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 13 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 14 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |

**Indexes**:
- IX_TOTAL_P1: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## TOTAL_SAIDA_P2

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | DATE | Y |  |  |
| 5 | IND_PRIMEIRA_LINHA | CHAR(1) | Y |  |  |
| 6 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 7 | TITULO_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 9 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 11 | NRO_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | NRO_LIVRO | NUMBER(6) | Y |  |  |
| 13 | NRO_FOLHA | NUMBER(6) | Y |  |  |
| 14 | IND_TIPO_TOTAL | NUMBER(1) | Y |  |  |

**Indexes**:
- IX_TOTAL_P2: (COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)

---

## TPIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TPIS_DAT | DATE | N |  |  |
| 2 | TPIS_COD | CHAR(2) | N |  |  |
| 3 | TPIS_DSC | VARCHAR2(150) | Y |  |  |

**PK**: TPIS_DAT, TPIS_COD

---

## TPLD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TPLD_COD | CHAR(2) | N |  |  |
| 2 | TPLD_DSC | VARCHAR2(150) | Y |  |  |

**PK**: TPLD_COD

---

## TRANSF_DACON_REGRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VERSAO_ORIG | VARCHAR2(30) | Y |  |  |
| 2 | NUM_FICHA_ORIG | VARCHAR2(3) | Y |  |  |
| 3 | NUM_LINHA_ORIG | NUMBER(2) | Y |  |  |
| 4 | MERCADO_ORIG | CHAR(1) | Y |  |  |
| 5 | REGIME_ORIG | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO_DACON_ORIG | VARCHAR2(10) | Y |  |  |
| 7 | IND_DET_SEPAR_ORIG | CHAR(1) | Y |  |  |
| 8 | VERSAO_DEST | VARCHAR2(30) | Y |  |  |
| 9 | NUM_FICHA_DEST | VARCHAR2(3) | Y |  |  |
| 10 | NUM_LINHA_DEST | NUMBER(2) | Y |  |  |
| 11 | MERCADO_DEST | CHAR(1) | Y |  |  |
| 12 | REGIME_DEST | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO_DACON_DEST | VARCHAR2(10) | Y |  |  |
| 14 | IND_DET_SEPAR_DEST | CHAR(1) | Y |  |  |

---

## TRIBUTACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 2 | COD_TRIBUTACAO | NUMBER(1) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_TRIBUTO, COD_TRIBUTACAO

**FKs**:
- COD_TRIBUTO → TRIBUTO(COD_TRIBUTO)

---

## TRIBUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | TITULO | VARCHAR2(6) | Y |  |  |

**PK**: COD_TRIBUTO

---

## UF_ARRECADACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 2 | NRO_BANCO | VARCHAR2(3) | Y |  |  |
| 3 | NRO_AGENCIA | VARCHAR2(5) | Y |  |  |
| 4 | NRO_CONTA | VARCHAR2(18) | Y |  |  |
| 5 | NOM_BANCO | VARCHAR2(50) | Y |  |  |
| 6 | DIA_VENCTO | NUMBER(2) | Y |  |  |

**Indexes**:
- UF_ARRECADACAO_IX (UNIQUE): (IDENT_ESTADO)

---

## UF_CONVENIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | NRO_CONVENIO | VARCHAR2(30) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UF_CONV_IX (UNIQUE): (IDENT_ESTADO, NRO_CONVENIO)

---

## UF_FAV_TP_IMPOSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_IMPOSTO | VARCHAR2(20) | N |  |  |
| 4 | CAMPO_GUIA | VARCHAR2(20) | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | TIPO_IMPOSTO | VARCHAR2(40) | N |  |  |
| 7 | DIAS_VENCTO | VARCHAR2(2) | N |  |  |
| 8 | REGRA_IMPOSTO | VARCHAR2(40) | N |  |  |
| 9 | CONTEUDO_CAMPO_GUIA | VARCHAR2(800) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_IMPOSTO, CAMPO_GUIA, IDENT_ESTADO, TIPO_IMPOSTO, DIAS_VENCTO, REGRA_IMPOSTO

---

## UF_GUIA_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | NRO_GNR | VARCHAR2(12) | N |  |  |
| 5 | DATA_GNR | DATE | Y |  |  |
| 6 | NRO_BANCO | VARCHAR2(3) | Y |  |  |
| 7 | NRO_AGENCIA | VARCHAR2(6) | Y |  |  |
| 8 | NRO_CONTA | VARCHAR2(18) | Y |  |  |
| 9 | VLR_GNR | NUMBER(17,2) | Y |  |  |
| 10 | DATA_VENCTO | DATE | Y |  |  |
| 11 | MES_REFERENCIA | NUMBER(2) | Y |  |  |
| 12 | NRO_CONVENIO | VARCHAR2(30) | Y |  |  |
| 13 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 14 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 16 | VLR_OUTRO_ACRES | NUMBER(17,2) | Y |  |  |
| 17 | VLR_OUTRO_DECRES | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS_DEVIDO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_RESSARC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_DEVOLUCAO | NUMBER(17,2) | Y |  |  |
| 21 | DATA_REFERENCIA | DATE | Y |  |  |
| 22 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO, NRO_GNR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## UNIDADE_FEDERATIVA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UNFE_SIG | CHAR(2) | N |  |  |
| 2 | UNFE_DSC | VARCHAR2(150) | Y |  |  |

**PK**: UNFE_SIG

---

## UNIDADE_MEDIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UNID_COD | VARCHAR2(6) | N |  |  |
| 2 | UNID_DAT_ATUA | DATE | N |  |  |
| 3 | UNID_DSC | VARCHAR2(150) | Y |  |  |

**PK**: UNID_COD, UNID_DAT_ATUA

**Indexes**:
- UNIDADE_MEDIDAI2: (UNID_COD)

---

## UNIN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UNIN_COD | VARCHAR2(9) | N |  |  |
| 2 | UNIN_DAT_ATUA | DATE | N |  |  |
| 3 | UNIN_NOM | VARCHAR2(150) | Y |  |  |

**PK**: UNIN_COD, UNIN_DAT_ATUA

---

## UNI_CONV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EMPS_COD | VARCHAR2(9) | N |  |  |
| 2 | FILI_COD | VARCHAR2(9) | N |  |  |
| 3 | MATE_COD | VARCHAR2(60) | N |  |  |
| 4 | UNID_COD | CHAR(3) | N |  |  |
| 5 | MATE_DAT_ATUA | DATE | N |  |  |
| 6 | UNID_COD_VENDA | CHAR(3) | N |  |  |
| 7 | UNID_COD_CONV | CHAR(3) | Y |  |  |
| 8 | TP_FATOR | NUMBER | Y |  |  |
| 9 | UTILIZA | CHAR(2) | N |  |  |

**PK**: EMPS_COD, FILI_COD, MATE_COD, UNID_COD, MATE_DAT_ATUA, UNID_COD_VENDA, UTILIZA

---

## USUARIO_EMPRESA_MAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_USUARIO | VARCHAR2(40) | Y |  |  |

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

**Indexes**:
- IDX_CHN_USU_EMP (UNIQUE): (COD_EMPRESA, COD_USUARIO)

---

## USUARIO_ESTAB_MAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_USUARIO | VARCHAR2(40) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IDX_CHN_USU_ETB (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_USUARIO)

---

## VIA_TRANSPORTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VTRP_COD | CHAR(3) | N |  |  |
| 2 | VTRP_DAT_ATUA | DATE | N |  |  |
| 3 | VTRP_DSC | VARCHAR2(150) | Y |  |  |
| 4 | CAT95V_COD | CHAR(1) | Y |  |  |

**PK**: VTRP_COD, VTRP_DAT_ATUA

---

## Y2025_SIT_TRB_UF_A

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SITUACAO_A | NUMBER(12) | N |  |  |
| 2 | GRUPO_SITUACAO_A | VARCHAR2(9) | Y |  |  |
| 3 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 4 | VALID_SITUACAO_A | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_SITUACAO_A

**FKs**:
- GRUPO_SITUACAO_A → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_SIT_A (UNIQUE): (GRUPO_SITUACAO_A, COD_SITUACAO_A, VALID_SITUACAO_A)

---

## Y2026_SIT_TRB_UF_B

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SITUACAO_B | NUMBER(12) | N |  |  |
| 2 | GRUPO_SITUACAO_B | VARCHAR2(9) | Y |  |  |
| 3 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 4 | VALID_SITUACAO_B | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_SITUACAO_B

**FKs**:
- GRUPO_SITUACAO_B → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_SIT_B (UNIQUE): (GRUPO_SITUACAO_B, COD_SITUACAO_B, VALID_SITUACAO_B)

---

## Y2027_SIT_TRIBUTARIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_TRIBUTACAO | CHAR(1) | N |  |  |
| 2 | COD_TRIBUTACAO | NUMBER(2) | N |  |  |
| 3 | DATA_VALID | DATE | N |  |  |
| 4 | DSC_TRIBUTACAO | VARCHAR2(500) | Y |  |  |

**PK**: IND_TRIBUTACAO, COD_TRIBUTACAO, DATA_VALID

---

## Y2046_INDICE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INDICE | VARCHAR2(10) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |

**PK**: COD_INDICE

---

## Y2085_TURNO_TRAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TURNO | NUMBER(12) | N |  |  |
| 2 | GRUPO_TURNO | VARCHAR2(9) | Y |  |  |
| 3 | COD_TURNO | VARCHAR2(5) | Y |  |  |
| 4 | VALID_TURNO | DATE | Y |  |  |
| 5 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_TURNO

**FKs**:
- GRUPO_TURNO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_TURNO (UNIQUE): (GRUPO_TURNO, COD_TURNO, VALID_TURNO)

---

## Y2086_TURNO_DESC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TURNO | NUMBER(12) | N |  |  |
| 2 | DIA_DESCANSO | NUMBER(12) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_TURNO, DIA_DESCANSO

**FKs**:
- IDENT_TURNO → Y2085_TURNO_TRAB(IDENT_TURNO)

---

## Y2087_TURNO_JORN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TURNO | NUMBER(12) | N |  |  |
| 2 | JORNADA | NUMBER(12) | N |  |  |
| 3 | HORA_ENTRADA | DATE | Y |  |  |
| 4 | HORA_SAIDA | DATE | Y |  |  |
| 5 | HORA_SAIDA_REF | DATE | Y |  |  |
| 6 | HORA_VOLTA_REF | DATE | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_TURNO, JORNADA

**FKs**:
- IDENT_TURNO → Y2085_TURNO_TRAB(IDENT_TURNO)

---

