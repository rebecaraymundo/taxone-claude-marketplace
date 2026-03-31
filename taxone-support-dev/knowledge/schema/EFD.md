# Módulo: EFD (EFD) - 73 tabelas

## EFD_AJUSTES_AUTO_ALIQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_AJUSTES_AUTO_ALIQ | NUMBER(9) | N | null |  |
| 2 | ID_AJUSTES_AUTO_REGRAS | NUMBER(9) | N |  |  |
| 3 | COD_REG | VARCHAR2(10) | N |  |  |
| 4 | VLR_ALIQ | NUMBER(7,4) | N |  |  |

**FKs**:
- ID_AJUSTES_AUTO_REGRAS → EFD_AJUSTES_AUTO_REGRAS(ID_AJUSTES_AUTO_REGRAS)

**Indexes**:
- UK_EFD_AJUSTES_AUTO_ALIQ (UNIQUE): (ID_AJUSTES_AUTO_REGRAS, COD_REG, VLR_ALIQ)

---

## EFD_AJUSTES_AUTO_CFOP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_AJUSTES_AUTO_CFOP | NUMBER(9) | N | null |  |
| 2 | ID_AJUSTES_AUTO_REGRAS | NUMBER(9) | N |  |  |
| 3 | COD_CFOP | VARCHAR2(8) | N |  |  |

**FKs**:
- ID_AJUSTES_AUTO_REGRAS → EFD_AJUSTES_AUTO_REGRAS(ID_AJUSTES_AUTO_REGRAS)

---

## EFD_AJUSTES_AUTO_CST
**Comment**: Armazena os códigos CSTs das regras parametrizadas

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_AJUSTES_AUTO_CST | NUMBER(9) | N | null | Identificador da tabela |
| 2 | ID_AJUSTES_AUTO_REGRAS | NUMBER(9) | N |  | ID da tabela EFD_AJUSTES_AUTO_REGRAS |
| 3 | COD_PIS_COFINS | VARCHAR2(10) | N |  |  |
| 4 | COD_CST | NUMBER(2) | N |  | Codigo do CST do PIS/COFINS |

**PK**: ID_AJUSTES_AUTO_CST

**FKs**:
- ID_AJUSTES_AUTO_REGRAS → EFD_AJUSTES_AUTO_REGRAS(ID_AJUSTES_AUTO_REGRAS)

**Indexes**:
- UK_EFD_AJUSTES_AUTO_CST (UNIQUE): (ID_AJUSTES_AUTO_REGRAS, COD_PIS_COFINS, COD_CST)

---

## EFD_AJUSTES_AUTO_REGRAS
**Comment**: Regras parametrizadas para utilização na rotina de ajustes automáticos

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_AJUSTES_AUTO_REGRAS | NUMBER(9) | N | null | Identificador da tabela |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | Código da Empresa |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | Codigo do Estabelecimento |
| 4 | IDENT_SCP | NUMBER(12) | Y |  | Identificador da tabela X2057_COD_SCP |
| 5 | NOM_REGRA | VARCHAR2(100) | N |  | Nome da Regra |
| 6 | DET_REGRA | VARCHAR2(500) | Y |  | Detalhes da Regra |
| 7 | COD_CREDITO | VARCHAR2(3) | N |  | Código do Crédito a ser utilizado para geração do registro de ajuste |
| 8 | COD_AJUSTE | VARCHAR2(2) | N |  | Código do Ajuste a ser utilizado na geração do registro de ajuste |
| 9 | MOVTO_E_S | VARCHAR2(1) | Y |  | Indicador de movimento da nota fiscal. Entre os valores possíveis está o "9", equivalente a uma nota fiscal de saída. |
| 10 | NORM_DEV | VARCHAR2(1) | Y |  | Se se trata de uma nota fiscal Normal ou Devolução (1-Normal, 2-Devolução) |
| 11 | CFOP_CFOP_EXT_TAG | VARCHAR2(1) | N | 'C' |  |

**PK**: ID_AJUSTES_AUTO_REGRAS

**Indexes**:
- UK_EFD_AJUSTES_AUTO_REGRAS (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_SCP, NOM_REGRA)

---

## EFD_APURACAO_ASSISTIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_AJUSTE | VARCHAR2(8) | N |  |  |
| 3 | DESC_CPL_AJUSTE | VARCHAR2(150) | Y |  |  |
| 4 | COD_INF_ADIC | VARCHAR2(8) | N |  |  |
| 5 | DSC_CPL_INF | VARCHAR2(150) | Y |  |  |
| 6 | COD_AJUSTE_SUB | VARCHAR2(8) | N |  |  |

**PK**: IDENT_ESTADO

---

## EFD_BEM_CIAP
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos Bens, p/ geração do registro G126.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI | DATE | N |  |  |
| 4 | DAT_FIN | DATE | N |  |  |
| 5 | COD_BEM | VARCHAR2(60) | N |  |  |
| 6 | COD_INC | VARCHAR2(6) | N |  |  |
| 7 | DAT_MOV | DATE | N |  |  |
| 8 | TIPO_MOV | VARCHAR2(2) | Y |  |  |
| 9 | NUM_CIAP | NUMBER(12) | N |  |  |
| 10 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |
| 11 | NUM_PARC | NUMBER(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI, DAT_FIN, COD_BEM, COD_INC, DAT_MOV, NUM_CIAP

---

## EFD_C197_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_FISCAL | DATE | N |  |  |
| 2 | UF | VARCHAR2(2) | N |  |  |
| 3 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |

**PK**: UF, DATA_FISCAL

---

## EFD_C597_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_FISCAL | DATE | N |  |  |
| 2 | UF | VARCHAR2(2) | N |  |  |
| 3 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |

**PK**: UF, DATA_FISCAL

---

## EFD_CAD_BEM
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos Bens movimentados, p/ geração do registro 0200.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_BEM | VARCHAR2(68) | N |  |  |
| 5 | COD_BEM_REAL | VARCHAR2(68) | Y |  |  |
| 6 | COD_INC_REAL | VARCHAR2(6) | Y |  |  |
| 7 | VALID_BEM | DATE | Y |  |  |
| 8 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 9 | UNID_INV | VARCHAR2(8) | Y |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, COD_BEM

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

**Indexes**:
- IX_EFD_CAD_BEM: (PROC_ID, COD_EMPRESA, COD_ESTAB, COD_BEM_REAL, COD_INC_REAL)

---

## EFD_CAD_BEM_CIAP
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos Bens, p/ geração do registro 0300.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_BEM | VARCHAR2(68) | N |  |  |
| 5 | COD_INC | VARCHAR2(6) | N |  |  |
| 6 | NUM_PARCELA | NUMBER(3) | Y |  |  |
| 7 | IND_COD_PRNC | CHAR(1) | Y |  |  |
| 8 | IND_ST_ATIVO | CHAR(1) | Y |  |  |
| 9 | NUM_PARC_AP | NUMBER(2) | Y |  |  |
| 10 | COD_BEM_ORIG | VARCHAR2(68) | Y |  |  |
| 11 | COD_INC_ORIG | VARCHAR2(6) | Y |  |  |
| 12 | TIPO_BEM | CHAR(1) | Y |  |  |
| 13 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 14 | DSC_FUNCAO | VARCHAR2(150) | Y |  |  |
| 15 | VIDA_UTIL | NUMBER(3) | Y |  |  |
| 16 | IDENT_CONTA_CM | NUMBER(12) | Y |  |  |
| 17 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 18 | VALID_BEM | DATE | Y |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_CAD_BEM_MED
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos Bens com todas as medidas (medida da x2007) movimentadas, p/ geração do registro 0220.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_BEM | VARCHAR2(68) | N |  |  |
| 3 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 4 | COD_MEDIDA | VARCHAR2(8) | N |  |  |

**PK**: PROC_ID, COD_BEM, GRUPO_MEDIDA, COD_MEDIDA

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_CAD_CCUSTO
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos Centros de custo, p/ geração do registro 0600.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 3 | COD_CUSTO | VARCHAR2(50) | N |  |  |

**PK**: PROC_ID, GRUPO_CUSTO, COD_CUSTO

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_CAD_CONTA
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento das Contas movimentadas, p/ geração do registro 0500.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | N |  |  |

**PK**: PROC_ID, GRUPO_CONTA, COD_CONTA

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_CAD_INSC_EST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 5 | IND_GER_1400 | CHAR(1) | Y | '1' |  |
| 6 | IND_VA_PROD | CHAR(1) | Y | 'N' |  |
| 7 | IND_PAR_PROD_1400 | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO

---

## EFD_CAD_MED
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos códigos de medida (medida da x2007, ou a medida padrão da x2017), p/ geração do registro 0190.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 3 | COD_MEDIDA | VARCHAR2(8) | N |  |  |
| 4 | IND_TAB_ORIGEM | VARCHAR2(5) | Y |  | Indicador da tabela origem da medida. Domínio: X2007: medida da X2007_MEDIDA; X2017: unidade padrão da X2017_UND_PADRAO. |

**PK**: PROC_ID, GRUPO_MEDIDA, COD_MEDIDA

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_CAD_NAT_OP
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos códigos de natureza da operação, p/ geração do registro 0400.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |

**PK**: PROC_ID, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_CAD_OBS
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento das informações complementares e das observações de lançamento do docto fiscal, p/ geração dos registros 0450 e 0460.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_OBSERVACAO | VARCHAR2(9) | N |  |  |
| 3 | COD_OBSERVACAO | VARCHAR2(8) | N |  |  |
| 4 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 5 | DESC_C790 | VARCHAR2(100) | Y |  |  |

**PK**: PROC_ID, GRUPO_OBSERVACAO, COD_OBSERVACAO, IND_ICOMPL_LANCTO

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_CAD_PARTIC
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento para armazenamento das pessoas fis/jur, p/ geração do registro 0150.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N | 0 |  |
| 6 | IND_GERA_0175_2NF | CHAR(1) | Y |  |  |
| 7 | DATA_NF | DATE | Y |  |  |
| 8 | COD_UF | NUMBER(2) | Y |  |  |
| 9 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

**Indexes**:
- IX_EFD_CAD_PARTIC: (PROC_ID, IND_FIS_JUR, COD_FIS_JUR)
- UK_EFD_CAD_PARTIC (UNIQUE): (PROC_ID, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, COD_UF, COD_MUNICIPIO)

---

## EFD_CAD_PROD_MED
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos Produtos com todas as medidas (medida da x2007) movimentadas, p/ geração do registro 0220.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 6 | COD_MEDIDA | VARCHAR2(8) | N |  |  |

**PK**: PROC_ID, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_MEDIDA, COD_MEDIDA

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_CAD_PROD_SERV
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos Produtos e Serviços movimentados, p/ geração do registro 0200.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | GRUPO_PROD_SERV | VARCHAR2(9) | N |  |  |
| 3 | IND_PROD_SERV | CHAR(1) | N |  |  |
| 4 | COD_PROD_SERV | VARCHAR2(60) | N |  |  |
| 5 | IND_INSUMO | CHAR(1) | Y |  |  |
| 6 | IND_REG_0210 | CHAR(1) | Y |  |  |
| 7 | IND_IPI_DESTACADO | CHAR(1) | Y | 'N' |  |

**PK**: PROC_ID, GRUPO_PROD_SERV, IND_PROD_SERV, COD_PROD_SERV

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

**Indexes**:
- IX_EFD_CAD_PROD_SERV_01: (PROC_ID)

---

## EFD_CAPA_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | PK da X07_DOCTO_FISCAL. |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | PK da X07_DOCTO_FISCAL. |
| 3 | DATA_FISCAL | DATE | N |  | PK da X07_DOCTO_FISCAL. |
| 4 | MOVTO_E_S | CHAR(1) | N |  | PK da X07_DOCTO_FISCAL. |
| 5 | NORM_DEV | CHAR(1) | N |  | PK da X07_DOCTO_FISCAL. |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  | PK da X07_DOCTO_FISCAL. |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  | PK da X07_DOCTO_FISCAL. |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  | PK da X07_DOCTO_FISCAL. |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  | PK da X07_DOCTO_FISCAL. |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  | PK da X07_DOCTO_FISCAL. |
| 11 | DATA_SAIDA_REC | DATE | Y |  | Data de Entrada/Saída do registro C100 - DT_E_S - ID_CAMPO = 9.  |
| 12 | DATA_EMISSAO | DATE | Y |  | Data de Emissão do Documento Fiscal - C100 - DT_DOC - ID_CAMPO = 8.   Campo usado p/ compor a chave de ordenação dos registros filhos do C100, já que faz parte da chave de ordenação do C100. Será usado também na geração dos registros de fatura (C140 e C141). |
| 13 | DAT_ESCR_EXTEMP | DATE | Y |  | Data Extemporânea do Documento Fiscal.   Será usado como filtro na geração dos registros filhos do C100, juntamente com a DATA_FISCAL. |
| 14 | IND_OPER | CHAR(1) | Y |  | Indicador do Tipo de Operação do C100 - ID_CAMPO = 1. Campo usado p/ compor a chave de ordenação dos registros filhos do C100, já que faz parte da chave de ordenação do C100. |
| 15 | IND_EMIT | CHAR(1) | Y |  | Indicador do Emitente do C100 - ID_CAMPO = 2. Campo usado p/ compor a chave de ordenação dos registros filhos do C100, já que faz parte da chave de ordenação do C100. |
| 16 | COD_PART | VARCHAR2(60) | Y |  | Código do Participante do C100 - ID_CAMPO = 3. Campo usado p/ compor a chave de ordenação dos registros filhos do C100, já que faz parte da chave de ordenação do C100. |
| 17 | COD_MOD | VARCHAR2(2) | Y |  | Código do Modelo do Documento Fiscal - C100 - ID_CAMPO = 4 (COD_MODELO_COTEPE da X07_DOCTO_FISCAL). |
| 18 | IND_PAGTO | CHAR(1) | Y |  | Indicador do Tipo de Pagamento do C100 - ID_CAMPO = 12. Será usado na geração dos registros de fatura (C140 e C141). |
| 19 | COD_ANP | NUMBER(12) | Y |  | Código do Produto na ANP da X2013_PRODUTO.  Será usada na geração do C165. |
| 20 | SIT_ESCRITURA_ESPECIAL | VARCHAR2(300) | Y |  | Descrição das Situações Especiais da NF que exigem tratamento diferenciado na gravação dos registros do Sped. |
| 21 | COD_CFO | VARCHAR2(4) | Y |  | Campo será usado para geração do D160, D161, D162 |
| 22 | IDENT_FIS_CONCES | NUMBER(12) | Y |  | Campo será usado para geração do C175 |
| 23 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  | Campo será usado para geração do C175 |
| 24 | COD_UF_ST | VARCHAR2(2) | Y |  | Campo será usado para geração do D210 |
| 25 | SIT_NFE_CONTRIBUINTE | CHAR(1) | Y |  | Campo será usado para geração do C100, e informa se é uma Nota Fiscal Eletrônica Emitida pelo Contribuinte |
| 26 | COD_ESTADO_ORIG | VARCHAR2(2) | Y |  | Campo será usado para geração do C105 |
| 27 | COD_ESTADO_DEST | VARCHAR2(2) | Y |  | Campo será usado para geração do C105 |
| 28 | IDENT_FIS_LSG | NUMBER(12) | Y |  | Campo será usado para geração do C105 |
| 29 | V_DATA_TRAB | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**Indexes**:
- IX_EFD_CAPA_DOCFIS: (COD_EMPRESA, COD_ESTAB, V_DATA_TRAB, MOVTO_E_S, COD_MOD, IND_PAGTO)

---

## EFD_CAPA_REDUCAO_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | Pk da Redução Z (X991_CAPA_REDUCAO_ECF). |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | Pk da Redução Z (X991_CAPA_REDUCAO_ECF). |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  | Pk da Redução Z (X991_CAPA_REDUCAO_ECF). |
| 4 | NUM_CRZ | VARCHAR2(6) | N |  | Pk da Redução Z (X991_CAPA_REDUCAO_ECF). |
| 5 | DATA_FISCAL | DATE | N |  | Pk da Redução Z (X991_CAPA_REDUCAO_ECF). |
| 6 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Dados do Equipamento ECF (X2087_EQUIPAMENTO_ECF). |
| 7 | COD_MODELO_ECF | VARCHAR2(30) | Y |  | Dados do Equipamento ECF (X2087_EQUIPAMENTO_ECF). |
| 8 | COD_FABRICACAO_ECF | VARCHAR2(21) | Y |  | Dados do Equipamento ECF (X2087_EQUIPAMENTO_ECF). |
| 9 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  | Dados do Equipamento ECF (X2087_EQUIPAMENTO_ECF). |
| 10 | COD_MODELO | VARCHAR2(2) | Y |  | Dados do Equipamento ECF (X2087_EQUIPAMENTO_ECF). |
| 11 | NUM_COO_INI | VARCHAR2(9) | Y |  | Dados da Redução Z (X991_CAPA_REDUCAO_ECF). |
| 12 | NUM_COO_FIM | VARCHAR2(9) | Y |  | Dados da Redução Z (X991_CAPA_REDUCAO_ECF). |
| 13 | SIT_ESCRITURA_ESPECIAL | VARCHAR2(300) | Y |  | Descrição das Situações Especiais da Redução Z que exigem tratamento diferenciado na gravação dos registros do Sped. |
| 14 | NUM_COO_FIM_REI | VARCHAR2(9) | Y |  | Dados do Equipamento ECF (X2087_EQUIPAMENTO_ECF). |

**PK**: DATA_FISCAL, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_CRZ

**Indexes**:
- IX_EFD_CAPA_REDUCAO_ECF: (DATA_FISCAL, COD_ESTAB, COD_CAIXA_ECF, COD_MODELO, COD_EMPRESA, NUM_CRZ)

---

## EFD_D737_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_FISCAL | DATE | N |  |  |
| 2 | UF | VARCHAR2(2) | N |  |  |
| 3 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 4 | ORIGEM | VARCHAR2(3) | Y |  |  |

**PK**: UF, DATA_FISCAL

---

## EFD_DADOS_INICIAIS_ESTAB
**Comment**: Parametrização de dados gerais ou dados iniciais, necessários para a geração do arquivo.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 4 | IND_NAT_SERV | CHAR(1) | Y |  |  |
| 5 | IND_VA_PROD | CHAR(1) | Y |  | Indicador para calculo do  valor agregado considerando o Produto,                              ou seja, por Produto/Municipio - registro 1400 |
| 6 | IND_PAG_RECEB | CHAR(1) | Y |  |  |
| 7 | IND_DESCR_PROD | CHAR(1) | Y |  |  |
| 8 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 9 | IND_GER_CIAP | CHAR(1) | Y |  |  |
| 10 | IND_GER_BEM | CHAR(1) | Y |  |  |
| 11 | DSC_SUB_AP1 | VARCHAR2(150) | Y |  |  |
| 12 | DSC_SUB_AP2 | VARCHAR2(150) | Y |  |  |
| 13 | DSC_SUB_AP3 | VARCHAR2(150) | Y |  |  |
| 14 | IND_CIAP_IE | CHAR(1) | Y |  |  |
| 15 | IND_CONV_52 | CHAR(1) | Y |  |  |
| 16 | IND_COD_ITEM | CHAR(1) | Y |  |  |
| 17 | GRUPO_PRODUTO_TR | VARCHAR2(9) | Y |  |  |
| 18 | IND_PRODUTO_TR | CHAR(1) | Y |  |  |
| 19 | COD_PRODUTO_TR | VARCHAR2(60) | Y |  |  |
| 20 | IND_GER_CHV_NFE | CHAR(1) | Y |  |  |
| 21 | IND_NF_TRANSF_CRED_DEB_MS | CHAR(1) | Y |  |  |
| 22 | IND_SIT08_ICMS | CHAR(1) | Y |  |  |
| 23 | IND_SIT08_ICMSS | CHAR(1) | Y |  |  |
| 24 | IND_SIT08_IPI | CHAR(1) | Y |  |  |
| 25 | IND_SIT08_PISCOF | CHAR(1) | Y |  |  |
| 26 | IND_SIT08_PISCOF_ST | CHAR(1) | Y |  |  |
| 27 | IND_GER_C110_C120 | CHAR(1) | Y |  |  |
| 28 | DSC_SUB_AP4 | VARCHAR2(150) | Y |  |  |
| 29 | DSC_SUB_AP5 | VARCHAR2(150) | Y |  |  |
| 30 | DSC_SUB_AP6 | VARCHAR2(150) | Y |  |  |
| 31 | IND_CALC_VL_ICMS_C490 | CHAR(1) | Y | 1 |  |
| 32 | IND_GER_1400 | CHAR(1) | Y |  |  |
| 33 | IND_PAR_PROD_1400 | CHAR(1) | Y |  |  |
| 34 | VLR_PERC_1400 | NUMBER(7,4) | Y |  |  |
| 35 | IND_COD_PFJ | CHAR(1) | Y |  |  |
| 36 | IND_ORD_OP_K230 | CHAR(1) | Y |  |  |
| 37 | IND_GER_1391 | CHAR(1) | Y |  |  |
| 38 | IND_ORD_OP_K210 | CHAR(1) | Y |  |  |
| 39 | IND_ORD_OP_K260 | CHAR(1) | Y |  |  |
| 40 | IND_COD_DIF_K | CHAR(1) | Y | 'S' |  |
| 41 | IND_EE | CHAR(1) | Y | 'C' |  |
| 42 | IND_GER_PER_ANT_BL_G | CHAR(1) | Y | 'N' |  |
| 43 | IND_TRANSF_UF_IEU | CHAR(1) | Y | 'N' |  |
| 44 | IND_GER_C500_C600 | CHAR(1) | Y | 'N' |  |
| 45 | IND_INIBE_PIS_COFINS | CHAR(1) | Y | 'N' |  |
| 46 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 47 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 48 | IND_ORD_OP_K290 | CHAR(1) | Y | 'N' |  |
| 49 | IND_PF_1400 | CHAR(1) | Y | 'N' |  |
| 50 | IND_EMP_AGUA_DMA_BA | CHAR(1) | Y | 'N' |  |
| 51 | IND_NFC_E | CHAR(1) | Y | 'N' |  |
| 52 | IND_PRD_ISEN_EE | CHAR(1) | Y | 'N' |  |
| 53 | IND_PRD_DESC_EE | CHAR(1) | Y | 'N' |  |
| 54 | IND_ALINHA_COD_INF | CHAR(1) | Y | 'D' | D = Direita; E = Esquerda |
| 55 | IND_COD_BENEFICIO | CHAR(1) | Y |  |  |
| 56 | IND_LVR_APUR_INC_E110 | CHAR(1) | Y | 'N' |  |
| 57 | IND_VLR_SERV_N_TRIB_C500 | CHAR(1) | Y | 'N' |  |
| 58 | IND_INSC_ESTADUAL_0015 | CHAR(1) | Y | 'N' |  |
| 59 | IND_COD_SIT_C100 | VARCHAR2(2) | Y | '08' |  |
| 60 | IND_COD_REC_RJ_E250 | CHAR(1) | Y | 'N' |  |
| 61 | IND_GER_6_7_G110 | CHAR(1) | Y | 'N' |  |
| 62 | IND_TOT_INVENT_H005 | CHAR(1) | Y | 'N' |  |
| 63 | IND_UNID_INV_0200 | CHAR(1) | Y | 'N' |  |
| 64 | IND_TP_LEIAUTE_K010 | VARCHAR2(1) | Y | '1' | Valores assumidos: 0, 1, 2. |
| 65 | IND_GER_K230_0 | VARCHAR2(1) | Y | 'N' | Valores assumidos: S, N. |
| 66 | IND_SEPARADOR_I | VARCHAR2(1) | Y | 'S' | Valores assumidos: S, N. |
| 67 | IND_GER_MOD66_C700 | VARCHAR2(1) | Y |  | Valores assumidos: S, N. |
| 68 | IND_H005_MOT_INV | CHAR(1) | Y | 'N' |  |
| 69 | IND_PAR_PROD_E115 | VARCHAR2(1) | Y |  |  |
| 70 | IND_CONS_NF3E_CANC_C500 | CHAR(1) | Y | 'N' |  |
| 71 | IND_VL_DOC_TRANSF | CHAR(1) | Y | 'N' |  |
| 72 | COD_ESTAB_0221 | VARCHAR2(6) | Y |  |  |
| 73 | IND_DESCON_VLR_OUT_C590_C790 | CHAR(1) | Y | 'N' |  |
| 74 | IND_GER_EC87_0150 | VARCHAR2(1) | Y |  |  |
| 75 | IND_ESTORNO_1391 | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)

---

## EFD_DADOS_INICIAIS_FINANC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | N |  |  |
| 4 | IND_UTIL_MANUAL_DESC | CHAR(1) | Y | 'N' | Indica se os Descontos e Deduções são informados manualmente. S = Sim; N = Não |
| 5 | IND_UTIL_SLD_CC | CHAR(1) | Y | 'N' | Indica se geracao utilizara tambem saldos contabeis(safx80) |
| 6 | IND_PER_ENCER | CHAR(1) | Y | 'A' | Indica o perÃ­odo de encerramento <A>nual, <T>rimestral ou <S>emestral |
| 7 | IND_GER_M350 | CHAR(1) | Y |  |  |
| 8 | IND_GER_0110 | CHAR(1) | Y | '1' |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

---

## EFD_DADOS_INICIAIS_PISCOF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 4 | IND_INC_TRIB | CHAR(1) | Y |  |  |
| 5 | IND_MET_APROP | CHAR(1) | Y |  |  |
| 6 | IND_TIPO_CONTRIB | CHAR(1) | Y |  |  |
| 7 | IND_APURACAO | CHAR(1) | Y |  |  |
| 8 | IND_DESC_DET_PROD | CHAR(1) | Y |  |  |
| 9 | IND_TIPO_APRESENTACAO | CHAR(1) | Y |  |  |
| 10 | IND_COD_TP_CRED_TACES71 | CHAR(1) | Y |  |  |
| 11 | IND_GRAVAR_NAT_SERV | CHAR(1) | Y | 'N' | S = Grava a natureza do servico; N = Grava o codigo do servico |
| 12 | IND_SELECAO_OPER_CRED | CHAR(1) | Y | 'E' | E = Data de emissao; L = Data de lancamento |
| 13 | IND_TP_PARAM_F100 | CHAR(1) | Y | 'D' | D = Tipo de Documento; C = Conta contabil |
| 14 | IND_GER_X161_X162 | CHAR(1) | Y | 'N' | S = Sim; N = Não |
| 15 | IND_TP_PARAM_NAT_REC | CHAR(1) | Y | 'P' | P = A partir da parametrização; N = A partir da nota fiscal |
| 16 | IND_NAT_BASE_CRED_POR_DOC | CHAR(1) | Y | 'N' |  |
| 17 | IND_GER_X190_X191 | CHAR(1) | Y | 'N' |  |
| 18 | IND_ALINHA_COD_INF | CHAR(1) | Y | 'D' | D = Direita; E = Esquerda |
| 19 | IND_UTIL_MANUAL_DESC | CHAR(1) | Y | 'N' | Indica se os Descontos e Deduções são informados manualmente. S = Sim; N = Não |
| 20 | IND_GER_X168 | CHAR(1) | Y | 'N' | Indica se os registros 1101 e 1501 serao gerados a partir dos dados da SAFX168 (Sim) ou SAFX158 e SAFX159 (Nao) |
| 21 | IND_GER_BLOCO_0_CENTR | CHAR(1) | Y | 'N' | Indica se os registros de cadastro do bloco serão gravados de forma centralizada no estabelecimeno matriz ou separadamente conforme a movimentação. |
| 22 | IND_COD_ITEM | CHAR(1) | Y | 'S' | Indica se o codigo do Item deve conter tambem o indicador. |
| 23 | IND_REG_TRIB | CHAR(1) | Y | '1' | 1 - Lucro Real; 2 – Lucro Presumido |
| 24 | IND_CRIT_ESCR_APUR | CHAR(1) | Y |  |  |
| 25 | IND_CRIT_DET_RF525 | CHAR(1) | Y |  |  |
| 26 | IND_GER_NF_CLASS_7 | CHAR(1) | Y | 'N' | Indica se as notas fiscais de mercadoria com classificacao 7 devem ser geradas. |
| 27 | QTDE_MESES_ANT_DTEMIS | NUMBER(2) | Y | 1 |  |
| 28 | IND_GER_0145 | CHAR(1) | Y | 'S' |  |
| 29 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 30 | IND_GER_CONS_SAT_CFE | CHAR(1) | Y |  |  |
| 31 | IND_DEM_REG_DET | CHAR(1) | Y |  |  |
| 32 | IND_DATA_BUSCA | CHAR(1) | Y |  |  |
| 33 | IND_CAPA_ITEM | CHAR(1) | Y | 'C' |  |
| 34 | IND_COD_PFJ | CHAR(1) | Y |  |  |
| 35 | COD_ENTIDADE_RESP | VARCHAR2(6) | Y |  |  |
| 36 | VERSAO | VARCHAR2(6) | Y |  |  |
| 37 | IND_GER_X183_X187 | CHAR(1) | Y | 'N' |  |
| 38 | IND_CST_M400_M800 | CHAR(1) | Y | 'N' |  |
| 39 | IND_CONTROL_CRED | CHAR(1) | Y | 'N' |  |
| 40 | IND_MODELO_55 | CHAR(1) | Y | 'N' |  |
| 41 | IND_NF_DEV_COMPRA_POST_ENTRADA | CHAR(1) | Y | 'S' | Indica se deve gerar NF de devolucao de compra posterior a NF de entrada |
| 42 | IND_VL_EXCL_MP_1159 | VARCHAR2(1) | Y | 'N' |  |
| 43 | ID_DADOS_INI_PISCOF | NUMBER | N | null |  |
| 44 | IND_AUTO_RATEIO | VARCHAR2(1) | Y |  |  |
| 45 | COD_NAO_CUMULATIVO_PIS | VARCHAR2(6) | Y |  |  |
| 46 | COD_CUMULATIVO_PIS | VARCHAR2(6) | Y |  |  |
| 47 | COD_NAO_CUMULATIVO_COFINS | VARCHAR2(6) | Y |  |  |
| 48 | COD_CUMULATIVO_COFINS | VARCHAR2(6) | Y |  |  |
| 49 | IND_CONSID_ICMS_NESCR | CHAR(1) | Y | 'N' |  |
| 50 | IND_AUTO_RATEIO_F100 | CHAR(1) | Y | 'S' |  |
| 51 | IND_AJT_CRED_RAT_PROP_REC_CUM | CHAR(1) | Y | 'N' |  |
| 52 | IND_NF_ENTR_CANC_MOD55 | VARCHAR2(1) | Y | 'S' |  |

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)

**Indexes**:
- UK_EFD_DADOS_INICIAIS_PISCOF (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_SCP)
- UK_EFD_DADOS_INICIAIS_PISCOF_1 (UNIQUE): (ID_DADOS_INI_PISCOF)

---

## EFD_DED_CLIENTE_CAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | DAT_INI | DATE | N |  |  |
| 5 | DAT_FIM | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 8 | VLR_APUR | NUMBER(17,2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI, DAT_FIM, IDENT_ESTADO, COD_MUNICIPIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## EFD_DOCFIS_RESSARC_DEV_GV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL_DEV | DATE | N |  |  |
| 4 | MOVTO_E_S_DEV | CHAR(1) | N |  |  |
| 5 | NORM_DEV_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO_DEV | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR_DEV | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS_DEV | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS_DEV | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS_DEV | VARCHAR2(2) | N |  |  |
| 11 | DISCRI_ITEM_DEV | VARCHAR2(76) | N |  |  |
| 12 | NUM_SEQ_DEV | NUMBER(5) | N |  |  |
| 13 | NUM_ITEM_DEV | NUMBER(5) | Y |  |  |
| 14 | QUANTIDADE_DEV | NUMBER(17,6) | Y |  |  |
| 15 | IND_FIS_JUR_DEV | CHAR(1) | Y |  |  |
| 16 | COD_FIS_JUR_DEV | VARCHAR2(14) | Y |  |  |
| 17 | COD_CFO_DEV | VARCHAR2(4) | Y |  |  |
| 18 | COD_NAT_OP_DEV | VARCHAR2(3) | Y |  |  |
| 19 | GRUPO_PRODUTO_DEV | VARCHAR2(9) | Y |  |  |
| 20 | IND_PRODUTO_DEV | CHAR(1) | Y |  |  |
| 21 | COD_PRODUTO_DEV | VARCHAR2(60) | Y |  |  |
| 22 | DESC_PRODUTO_DEV | VARCHAR2(50) | Y |  |  |
| 23 | GRUPO_MEDIDA_DEV | VARCHAR2(9) | Y |  |  |
| 24 | COD_MEDIDA_DEV | VARCHAR2(8) | Y |  |  |
| 25 | IND_TIPO_REF | CHAR(1) | Y |  |  |
| 26 | QUANT_X192_DEV | NUMBER(17,6) | Y |  |  |
| 27 | DATA_FISCAL_SAI | DATE | Y |  |  |
| 28 | MOVTO_E_S_SAI | CHAR(1) | Y |  |  |
| 29 | NORM_DEV_SAI | CHAR(1) | Y |  |  |
| 30 | IDENT_DOCTO_SAI | NUMBER(12) | Y |  |  |
| 31 | IDENT_FIS_JUR_SAI | NUMBER(12) | Y |  |  |
| 32 | NUM_DOCFIS_SAI | VARCHAR2(12) | Y |  |  |
| 33 | SERIE_DOCFIS_SAI | VARCHAR2(3) | Y |  |  |
| 34 | SUB_SERIE_DOCFIS_SAI | VARCHAR2(2) | Y |  |  |
| 35 | DISCRI_ITEM_SAI | VARCHAR2(76) | Y |  |  |
| 36 | NUM_ITEM_SAI | NUMBER(5) | Y |  |  |
| 37 | IND_FIS_JUR_SAI | CHAR(1) | Y |  |  |
| 38 | COD_FIS_JUR_SAI | VARCHAR2(14) | Y |  |  |
| 39 | COD_CFO_SAI | VARCHAR2(4) | Y |  |  |
| 40 | COD_NAT_OP_SAI | VARCHAR2(3) | Y |  |  |
| 41 | QUANTIDADE_SAI | NUMBER(17,6) | Y |  |  |
| 42 | COD_AJ_RES_SAI | VARCHAR2(10) | Y |  |  |
| 43 | VLR_BASE_AJ_RES_SAI | NUMBER(17,2) | Y |  |  |
| 44 | VLR_ALIQ_AJ_RES_SAI | NUMBER(7,4) | Y |  |  |
| 45 | VLR_AJ_RES_SAI | NUMBER(17,2) | Y |  |  |
| 46 | COD_AJ_CRED_SAI | VARCHAR2(10) | Y |  |  |
| 47 | VLR_BASE_AJ_CRED_SAI | NUMBER(17,2) | Y |  |  |
| 48 | VLR_ALIQ_AJ_CRED_SAI | NUMBER(7,4) | Y |  |  |
| 49 | VLR_AJ_CRED_SAI | NUMBER(17,2) | Y |  |  |
| 50 | COD_AJ_RES_DEV | VARCHAR2(10) | Y |  |  |
| 51 | VLR_BASE_AJ_RES_DEV | NUMBER(17,2) | Y |  |  |
| 52 | VLR_AJ_RES_DEV | NUMBER(17,2) | Y |  |  |
| 53 | TOT_VLR_BASE_AJ_RES_DEV | NUMBER(17,2) | Y |  |  |
| 54 | TOT_VLR_AJ_RES_DEV | NUMBER(17,2) | Y |  |  |
| 55 | COD_AJ_CRED_DEV | VARCHAR2(10) | Y |  |  |
| 56 | VLR_BASE_AJ_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 57 | VLR_AJ_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 58 | TOT_VLR_BASE_AJ_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 59 | TOT_VLR_AJ_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 60 | VLR_AJ_RES_DEV_ESTAB | NUMBER(17,2) | Y |  |  |
| 61 | VLR_AJ_CRED_DEV_ESTAB | NUMBER(17,2) | Y |  |  |
| 62 | PROC_ID | NUMBER | Y |  |  |
| 63 | NUM_LINHA | NUMBER(10) | Y |  |  |
| 64 | NUM_ORDEM_PRODUTO | NUMBER(10) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL_DEV, MOVTO_E_S_DEV, NORM_DEV_DEV, IDENT_DOCTO_DEV, IDENT_FIS_JUR_DEV, NUM_DOCFIS_DEV, SERIE_DOCFIS_DEV, SUB_SERIE_DOCFIS_DEV, DISCRI_ITEM_DEV, NUM_SEQ_DEV

---

## EFD_DOCFIS_RESSARC_GV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL_SAI | DATE | N |  |  |
| 4 | MOVTO_E_S_SAI | CHAR(1) | N |  |  |
| 5 | NORM_DEV_SAI | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO_SAI | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR_SAI | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS_SAI | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS_SAI | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS_SAI | VARCHAR2(2) | N |  |  |
| 11 | DISCRI_ITEM_SAI | VARCHAR2(76) | N |  |  |
| 12 | NUM_SEQ_ENT | NUMBER(5) | N |  |  |
| 13 | NUM_DOCFIS_REF_SAI | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS_REF_SAI | VARCHAR2(3) | Y |  |  |
| 15 | SSERIE_DOCFIS_REF_SAI | VARCHAR2(2) | Y |  |  |
| 16 | DATA_REF_SAI | DATE | Y |  |  |
| 17 | NUM_ITEM_SAI | NUMBER(5) | Y |  |  |
| 18 | QUANTIDADE_SAI | NUMBER(17,6) | Y |  |  |
| 19 | GRUPO_PRODUTO_SAI | VARCHAR2(9) | Y |  |  |
| 20 | IND_PRODUTO_SAI | CHAR(1) | Y |  |  |
| 21 | COD_PRODUTO_SAI | VARCHAR2(60) | Y |  |  |
| 22 | DATA_FISCAL_ENT | DATE | Y |  |  |
| 23 | MOVTO_E_S_ENT | CHAR(1) | Y |  |  |
| 24 | NORM_DEV_ENT | CHAR(1) | Y |  |  |
| 25 | IDENT_DOCTO_ENT | NUMBER(12) | Y |  |  |
| 26 | IDENT_FIS_JUR_ENT | NUMBER(12) | Y |  |  |
| 27 | NUM_DOCFIS_ENT | VARCHAR2(12) | Y |  |  |
| 28 | SERIE_DOCFIS_ENT | VARCHAR2(3) | Y |  |  |
| 29 | SUB_SERIE_DOCFIS_ENT | VARCHAR2(2) | Y |  |  |
| 30 | DISCRI_ITEM_ENT | VARCHAR2(76) | Y |  |  |
| 31 | IDENT_MODELO_ENT | NUMBER(12) | Y |  |  |
| 32 | DATA_SAIDA_REC_ENT | DATE | Y |  |  |
| 33 | DATA_EMISSAO_ENT | DATE | Y |  |  |
| 34 | NUM_ITEM_ENT | NUMBER(5) | Y |  |  |
| 35 | QUANTIDADE_ENT | NUMBER(17,6) | Y |  |  |
| 36 | VLR_UNIT_ENT | NUMBER(19,4) | Y |  |  |
| 37 | VLR_BASE_ICMSS_ENT | NUMBER(17,2) | Y |  |  |
| 38 | VLR_BASE_ICMSS_N_ESCRIT_ENT | NUMBER(17,2) | Y |  |  |
| 39 | VLR_BASE_ICMS_ORIG_ENT | NUMBER(17,2) | Y |  |  |
| 40 | IND_DIG_CALCULADO | CHAR(1) | Y |  |  |
| 41 | PROC_ID | NUMBER | Y |  |  |
| 42 | DATA_EMISSAO_SAI | DATE | Y |  |  |
| 43 | COD_CFO_SAI | VARCHAR2(4) | Y |  |  |
| 44 | COD_NAT_OP_SAI | VARCHAR2(3) | Y |  |  |
| 45 | COD_CFO_ENT | VARCHAR2(4) | Y |  |  |
| 46 | COD_NAT_OP_ENT | VARCHAR2(3) | Y |  |  |
| 47 | VLR_PRECO_ENT | NUMBER(19,4) | Y |  |  |
| 48 | VLR_FRETE_ENT | NUMBER(17,2) | Y |  |  |
| 49 | VLR_SEGURO_ENT | NUMBER(17,2) | Y |  |  |
| 50 | VLR_OUT_DEP_ENT | NUMBER(17,2) | Y |  |  |
| 51 | VLR_ALIQ_ICMS_ENT | NUMBER(7,4) | Y |  |  |
| 52 | VLR_ALIQ_ICMSS_ENT | NUMBER(7,4) | Y |  |  |
| 53 | VLR_UNIT_MERC_ENT | NUMBER(19,4) | Y |  |  |
| 54 | VLR_BASE_ST_ENT | NUMBER(17,3) | Y |  |  |
| 55 | COD_AJ_RES | VARCHAR2(10) | Y |  |  |
| 56 | VLR_BASE_AJ_RES | NUMBER(17,2) | Y |  |  |
| 57 | VLR_ALIQ_AJ_RES | NUMBER(7,4) | Y |  |  |
| 58 | VLR_AJ_RES | NUMBER(17,2) | Y |  |  |
| 59 | COD_AJ_CRED | VARCHAR2(10) | Y |  |  |
| 60 | VLR_BASE_AJ_CRED | NUMBER(17,2) | Y |  |  |
| 61 | VLR_ALIQ_AJ_CRED | NUMBER(7,4) | Y |  |  |
| 62 | VLR_AJ_CRED | NUMBER(17,2) | Y |  |  |
| 63 | DESC_PRODUTO_SAI | VARCHAR2(50) | Y |  |  |
| 64 | NUM_AUTENTIC_NFE_ENT | VARCHAR2(80) | Y |  |  |
| 65 | VLR_BC_ICMS_OP_PROP | NUMBER(17,2) | Y |  |  |
| 66 | VLR_ALIQ_ICMS_ULT_ENT | NUMBER(7,4) | Y |  |  |
| 67 | VLR_BC_ICMS_ULT_ENT | NUMBER(17,2) | Y |  |  |
| 68 | VLR_ICMS_ULT_ENT | NUMBER(17,3) | Y |  |  |
| 69 | VLR_ALIQ_ST_ULT_ENT | NUMBER(7,4) | Y |  |  |
| 70 | VLR_RESSARC | NUMBER(17,3) | Y |  |  |
| 71 | COD_RESP_RET | CHAR(1) | Y |  |  |
| 72 | IND_MOTIVO_RESSARC | CHAR(1) | Y |  |  |
| 73 | NUM_AUTENTIC_NFE_RET | VARCHAR2(80) | Y |  |  |
| 74 | IDENT_FIS_JUR_RET | NUMBER(12) | Y |  |  |
| 75 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  |  |
| 76 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  |  |
| 77 | NUM_ITEM_RET | NUMBER(5) | Y |  |  |
| 78 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 79 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 80 | GRUPO_MEDIDA_SAI | VARCHAR2(9) | Y |  |  |
| 81 | COD_MEDIDA_SAI | VARCHAR2(8) | Y |  |  |
| 82 | VLR_BASE_ICMS_N_DEST | NUMBER(17,2) | Y |  |  |
| 83 | VLR_BASE_ICMS_OUTRAS | NUMBER(17,2) | Y |  |  |
| 84 | IND_GRAVA_EFD | CHAR(1) | Y |  |  |
| 85 | VLR_ICMS_RECUP | NUMBER(17,2) | Y |  |  |
| 86 | VLR_ICMS_ESTORNO | NUMBER(17,2) | Y |  |  |
| 87 | VLR_ICMS_RESSARC | NUMBER(17,2) | Y |  |  |
| 88 | VLR_UNIT_RES_FCP_ST | NUMBER(17,2) | Y |  |  |
| 89 | NUM_LINHA | NUMBER(10) | Y |  |  |
| 90 | NUM_ORDEM_PRODUTO | NUMBER(10) | Y |  |  |

**PK**: DATA_FISCAL_SAI, COD_ESTAB, COD_EMPRESA, MOVTO_E_S_SAI, NORM_DEV_SAI, IDENT_DOCTO_SAI, IDENT_FIS_JUR_SAI, NUM_DOCFIS_SAI, SERIE_DOCFIS_SAI, SUB_SERIE_DOCFIS_SAI, DISCRI_ITEM_SAI, NUM_SEQ_ENT

---

## EFD_ESTAB_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

---

## EFD_EXP_SERVICO
**Comment**: Tabela utilizada no SPED FISCAL para armazenamento dos registros de exportação que possuem um serviço relacionado.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IND_DOC | CHAR(1) | N |  |  |
| 5 | NRO_DE | VARCHAR2(14) | N |  |  |
| 6 | DT_DE | DATE | N |  |  |
| 7 | NAT_EXP | CHAR(1) | N |  |  |
| 8 | NRO_RE | VARCHAR2(12) | N |  |  |
| 9 | DT_RE | DATE | N |  |  |
| 10 | CHC_EMB | VARCHAR2(18) | N |  |  |
| 11 | DT_CHC | DATE | N |  |  |
| 12 | DT_AVB | DATE | N |  |  |
| 13 | TP_CHC | VARCHAR2(2) | N |  |  |
| 14 | PAIS | VARCHAR2(3) | N |  |  |
| 15 | COD_MOD | VARCHAR2(2) | Y |  |  |
| 16 | SERIE | VARCHAR2(3) | Y |  |  |
| 17 | NUM_DOC | VARCHAR2(9) | Y |  |  |
| 18 | CHV_NFE | VARCHAR2(44) | Y |  |  |
| 19 | DT_DOC | DATE | Y |  |  |
| 20 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 21 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 22 | SUB_SERIE | VARCHAR2(2) | Y |  |  |

**PK**: PROC_ID, COD_EMPRESA, COD_ESTAB, IND_DOC, NRO_DE, DT_DE, NAT_EXP, NRO_RE, DT_RE, CHC_EMB, DT_CHC, DT_AVB, TP_CHC, PAIS

**FKs**:
- PROC_ID → LIB_PROCESSO(PROC_ID)

---

## EFD_IDENT_CAPA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_EFD_IDENT_CAPA: (IDENT_DOCTO_FISCAL)

---

## EFD_IDENT_ITENS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO_FISCAL | NUMBER(12) | Y |  |  |

**Indexes**:
- IX_EFD_IDENT_ITENS: (IDENT_DOCTO_FISCAL)

---

## EFD_INF_ADIC_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_INF_ADIC | VARCHAR2(8) | N |  |  |
| 3 | DSC_INF | VARCHAR2(250) | Y |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 6 | IND_NAO_DSC_COMPL | VARCHAR2(1) | Y | 'N' |  |
| 7 | IND_NAO_VLR_INF_ADIC | VARCHAR2(1) | Y | 'N' |  |

**PK**: COD_INF_ADIC

---

## EFD_ITEM_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | PK da X08_ITENS_MERC. |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | PK da X08_ITENS_MERC. |
| 3 | DATA_FISCAL | DATE | N |  | PK da X08_ITENS_MERC. |
| 4 | MOVTO_E_S | CHAR(1) | N |  | PK da X08_ITENS_MERC. |
| 5 | NORM_DEV | CHAR(1) | N |  | PK da X08_ITENS_MERC. |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  | PK da X08_ITENS_MERC. |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  | PK da X08_ITENS_MERC. |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  | PK da X08_ITENS_MERC. |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  | PK da X08_ITENS_MERC. |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  | PK da X08_ITENS_MERC. |
| 11 | DISCRI_ITEM | VARCHAR2(76) | N |  | PK da X08_ITENS_MERC. |
| 12 | IND_PRODUTO | CHAR(1) | Y |  | Caso seja produto, será preenchido com o Ind_Produto da X2013_Produto. Caso seja bem, será preenchido com B. |
| 13 | COD_PRODUTO | VARCHAR2(62) | Y |  | Caso seja produto, será preenchido com o Cod_Produto da X2013_Produto. Caso seja bem, será preenchido com Cod_Bem da X13_Bem_Ativo. |
| 14 | DATA_REF | DATE | Y |  | Campo será usado na geração do registro C176 |
| 15 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  | Campo será usado na geração do registro C176 |
| 16 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  | Campo será usado na geração do registro C176 |
| 17 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  | Campo será usado na geração do registro C176 |
| 18 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 19 | IND_TIPO_ARMA | CHAR(1) | Y |  | Campo será usado na geração do registro C174. |
| 20 | IND_TP_PROD_MEDIC | CHAR(1) | Y |  | Campo será usado na geração do registro C173. |
| 21 | VLR_PRECO_MEDICAMENTO | NUMBER(17,2) | Y |  | Campo será usado na geração do registro C173. |
| 22 | IND_BASE_MEDICAMENTO | CHAR(1) | Y |  | Campo será usado na geração do registro C173. |
| 23 | IDENT_CFO | NUMBER(12) | Y |  | Campo será usado na geração do registro C175 |
| 24 | COD_ITEM | VARCHAR2(62) | Y |  | Campos da Chave de Ordenação do C170, será usado na geração dos registros C173, C174, C175 |
| 25 | NUM_ITEM | NUMBER(5) | Y |  | Campos da Chave de Ordenação do C170, será usado na geração dos registros C173, C174, C175 |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## EFD_ITEM_DOCFIS_RESSARC
**Comment**: Tabela criada para armazenar NF de Saida com direito a Ressarcimento, relacionada as N notas fiscais de Entrada. Tabela é gravada pela geracao da EFD_SPED_RESSARC_FPROC. Tabela é lida para gerar o C176

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. PK da NF de Entrada. |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. PK da NF de Entrada. |
| 3 | DATA_FISCAL_SAI | DATE | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. |
| 4 | MOVTO_E_S_SAI | CHAR(1) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. |
| 5 | NORM_DEV_SAI | CHAR(1) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. |
| 6 | IDENT_DOCTO_SAI | NUMBER(12) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. |
| 7 | IDENT_FIS_JUR_SAI | NUMBER(12) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. |
| 8 | NUM_DOCFIS_SAI | VARCHAR2(12) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. |
| 9 | SERIE_DOCFIS_SAI | VARCHAR2(3) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. |
| 10 | SUB_SERIE_DOCFIS_SAI | VARCHAR2(2) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK. |
| 11 | DISCRI_ITEM_SAI | VARCHAR2(76) | N |  | NF de Saida com Direito a Ressarcimento: Campo da PK do Item de Mercadoria. |
| 12 | NUM_SEQ_ENT | NUMBER(5) | N |  | Sequencial por Item da NF de Saida com Direito a Ressarcimento, ja que este Item pode se referenciar a 0, 1 ou N itens da Nota de Entrada |
| 13 | NUM_DOCFIS_REF_SAI | VARCHAR2(12) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Numero da NF de Referencia. Quando preenchido, é o Numero da NF de Entrada. |
| 14 | SERIE_DOCFIS_REF_SAI | VARCHAR2(3) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Serie da NF de Referencia. Quando preenchido, é a Serie da NF de Entrada. |
| 15 | SSERIE_DOCFIS_REF_SAI | VARCHAR2(2) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Sub-Serie da NF de Referencia. Quando preenchido, é a Sub-Serie da NF de Entrada. |
| 16 | DATA_REF_SAI | DATE | Y |  | NF de Saida com Direito a Ressarcimento: Campo Data da NF de Referencia. Quando preenchido, é a Data Emissao da NF de Entrada. |
| 17 | NUM_ITEM_SAI | NUMBER(5) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Número do Item de mercadoria. |
| 18 | QUANTIDADE_SAI | NUMBER(17,6) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Quantidade do Item de mercadoria. |
| 19 | GRUPO_PRODUTO_SAI | VARCHAR2(9) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Grupo Produto do Item de mercadoria. |
| 20 | IND_PRODUTO_SAI | CHAR(1) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Indicador Produto do Item de mercadoria. |
| 21 | COD_PRODUTO_SAI | VARCHAR2(60) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Código Produto do Item de mercadoria. |
| 22 | DATA_FISCAL_ENT | DATE | Y |  | NF de Entrada: Campo da PK. |
| 23 | MOVTO_E_S_ENT | CHAR(1) | Y |  | NF de Entrada: Campo da PK. |
| 24 | NORM_DEV_ENT | CHAR(1) | Y |  | NF de Entrada: Campo da PK. |
| 25 | IDENT_DOCTO_ENT | NUMBER(12) | Y |  | NF de Entrada: Campo da PK. |
| 26 | IDENT_FIS_JUR_ENT | NUMBER(12) | Y |  | NF de Entrada: Campo da PK. |
| 27 | NUM_DOCFIS_ENT | VARCHAR2(12) | Y |  | NF de Entrada: Campo da PK. |
| 28 | SERIE_DOCFIS_ENT | VARCHAR2(3) | Y |  | NF de Entrada: Campo da PK. |
| 29 | SUB_SERIE_DOCFIS_ENT | VARCHAR2(2) | Y |  | NF de Entrada: Campo da PK. |
| 30 | DISCRI_ITEM_ENT | VARCHAR2(76) | Y |  | NF de Entrada: Campo da PK do Item de Mercadoria. |
| 31 | IDENT_MODELO_ENT | NUMBER(12) | Y |  | NF de Entrada: Campo Modelo. |
| 32 | DATA_SAIDA_REC_ENT | DATE | Y |  | NF de Entrada: Campo Data de Saida/Recebimento. |
| 33 | DATA_EMISSAO_ENT | DATE | Y |  | NF de Entrada: Campo Data de Emissao. |
| 34 | NUM_ITEM_ENT | NUMBER(5) | Y |  | NF de Entrada: Campo Número do Item de mercadoria. |
| 35 | QUANTIDADE_ENT | NUMBER(17,6) | Y |  | NF de Entrada: Campo Quantidade do Item de mercadoria. |
| 36 | VLR_UNIT_ENT | NUMBER(19,4) | Y |  | NF de Entrada: Campo Valor Unitário do Item de mercadoria. |
| 37 | VLR_BASE_ICMSS_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor da Base Tributada do ICMS-ST do Item de mercadoria. |
| 38 | VLR_BASE_ICMSS_N_ESCRIT_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor de Base ICMS-ST nao escriturado do Item de mercadoria. |
| 39 | VLR_BASE_ICMS_ORIG_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Base Calculo Carga Tributaria Origem ICMS do Item de mercadoria. |
| 40 | IND_DIG_CALCULADO | CHAR(1) | Y |  | 1 - Digitado, 2 - Gerado, 3 - Gerado/Alterado por manutenção |
| 41 | PROC_ID | NUMBER | Y |  | Número do processo do framework |
| 42 | DATA_EMISSAO_SAI | DATE | Y |  | NF de Saida com Direito a Ressarcimento: Campo data de emissao. |
| 43 | COD_CFO_SAI | VARCHAR2(4) | Y |  | NF de Saida com Direito a Ressarcimento: Campo CFOP. |
| 44 | COD_NAT_OP_SAI | VARCHAR2(3) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Natureza de Operacao. |
| 45 | COD_CFO_ENT | VARCHAR2(4) | Y |  | NF de Entrada: Campo CFOP. |
| 46 | COD_NAT_OP_ENT | VARCHAR2(3) | Y |  | NF de Entrada: Campo Natureza de Operacao. |
| 47 | VLR_PRECO_ENT | NUMBER(19,4) | Y |  | NF de Entrada: Campo Preco Unitario. |
| 48 | VLR_FRETE_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor do Frete. |
| 49 | VLR_SEGURO_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor Seguro. |
| 50 | VLR_OUT_DEP_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor Outras Despesas. |
| 51 | VLR_ALIQ_ICMS_ENT | NUMBER(7,4) | Y |  | NF de Entrada: Campo Aliquota ICMS. |
| 52 | VLR_ALIQ_ICMSS_ENT | NUMBER(7,4) | Y |  | NF de Entrada: Campo Aliquota ICMS ST. |
| 53 | VLR_UNIT_MERC_ENT | NUMBER(19,4) | Y |  | NF de Entrada: Campo Valor Unitario da Mercadoria - C176. |
| 54 | VLR_BASE_ST_ENT | NUMBER(18,3) | Y |  | NF de Entrada: Campo Valor Base ICMS ST - C176. |
| 55 | COD_AJ_RES | VARCHAR2(10) | Y |  | NF de Entrada: Campo Codigo de ajuste Ressarcimento. |
| 56 | VLR_BASE_AJ_RES | NUMBER(17,2) | Y |  | NF de Entrada: Campo Base de Calculo Ressarcimento. |
| 57 | VLR_ALIQ_AJ_RES | NUMBER(7,4) | Y |  | NF de Entrada: Campo Valor da Aliquota Ressarcimento. |
| 58 | VLR_AJ_RES | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor do Ajuste Ressarcimento. |
| 59 | COD_AJ_CRED | VARCHAR2(10) | Y |  | NF de Entrada: Campo Codigo de ajuste Credito. |
| 60 | VLR_BASE_AJ_CRED | NUMBER(17,2) | Y |  | NF de Entrada: Campo Base de Calculo Credito. |
| 61 | VLR_ALIQ_AJ_CRED | NUMBER(7,4) | Y |  | NF de Entrada: Campo Valor da Aliquota Credito. |
| 62 | VLR_AJ_CRED | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor do Ajuste Credito. |
| 63 | DESC_PRODUTO_SAI | VARCHAR2(50) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Descricao Produto. |
| 64 | NUM_AUTENTIC_NFE_ENT | VARCHAR2(80) | Y |  | Número da chave da NFe relativo à última entrada. |
| 65 | VLR_BC_ICMS_OP_PROP | NUMBER(17,2) | Y |  | Valor unitário da base de cálculo da operação própria do remetente. |
| 66 | VLR_ALIQ_ICMS_ULT_ENT | NUMBER(7,4) | Y |  | Alíquota do ICMS aplicável à última entrada da mercadoria. |
| 67 | VLR_BC_ICMS_ULT_ENT | NUMBER(17,2) | Y |  | Valor unitário da base de cálculo do ICMS relativo à última entrada da mercadoria. |
| 68 | VLR_ICMS_ULT_ENT | NUMBER(18,3) | Y |  | Valor unitário do crédito de ICMS sobre operações próprias do remetente, relativo à última entrada da mercadoria. |
| 69 | VLR_ALIQ_ST_ULT_ENT | NUMBER(7,4) | Y |  | Alíquota do ICMS ST relativa à última entrada da mercadoria. |
| 70 | VLR_RESSARC | NUMBER(18,3) | Y |  | Valor unitário do ressarcimento. |
| 71 | COD_RESP_RET | CHAR(1) | Y |  | Código que indica o responsável pela retenção do ICMS-ST. 1-Remetente Diret;  2-Remetente Indireto; 3-Próprio declarante. |
| 72 | IND_MOTIVO_RESSARC | CHAR(1) | Y |  | Código do motivo do ressarcimento. 1 – Venda para outra UF; 2 – Saída amparada por isenção ou não incidência; 3 – Perda ou deterioração; 4 – Furto ou roubo; 9 – Outros. |
| 73 | NUM_AUTENTIC_NFE_RET | VARCHAR2(80) | Y |  | Número da chave da NF-e emitida pelo substituto. |
| 74 | IDENT_FIS_JUR_RET | NUMBER(12) | Y |  | Código do participante do emitente da NF-e em que houve a retenção do ICMS-ST. |
| 75 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  | Série da NF-e em que houve a retenção do ICMS-ST. |
| 76 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  | Número da NF-e em que houve a retenção do ICMS-ST. |
| 77 | NUM_ITEM_RET | NUMBER(5) | Y |  | Número do item na NF-e em que houve a retenção do ICMS-ST. |
| 78 | IND_TP_DOC_ARREC | CHAR(1) | Y |  | Código do modelo do documento de arrecadação. 0 - documento estadual de arrecadação; 1 – GNRE. |
| 79 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  | Número do documento de arrecadação estadual. |
| 80 | GRUPO_MEDIDA_SAI | VARCHAR2(9) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Grupo Medida do Item de mercadoria. |
| 81 | COD_MEDIDA_SAI | VARCHAR2(8) | Y |  | NF de Saida com Direito a Ressarcimento: Campo Código Medida do Item de mercadoria. |
| 82 | VLR_BASE_ICMS_N_DEST | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor de Base ICMS Nao Destacado do Item de mercadoria. |
| 83 | VLR_BASE_ICMS_OUTRAS | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor de Base ICMS Outras Item de mercadoria. |
| 84 | IND_GRAVA_EFD | CHAR(1) | Y | 'S' | NF de Saida: Indicador de Gravação na EFD |
| 85 | VLR_ICMS_RECUP | NUMBER(17,2) | Y | 0 | NF de Saida com Direito a Ressarcimento: Campo Valor do ICMS a recuperar. |
| 86 | VLR_ICMS_ESTORNO | NUMBER(17,2) | Y | 0 | NF de Saida com Direito a Ressarcimento: Campo Valor do Estorno. |
| 87 | VLR_ICMS_RESSARC | NUMBER(17,2) | Y | 0 | NF de Saida com Direito a Ressarcimento: Campo Valor do ICMS a ressarcir. |
| 88 | VLR_UNIT_RES_FCP_ST | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor Unitario do Ressarcimento Parcial ou Completo. |
| 89 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 90 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |

**PK**: DATA_FISCAL_SAI, COD_ESTAB, COD_EMPRESA, MOVTO_E_S_SAI, NORM_DEV_SAI, IDENT_DOCTO_SAI, IDENT_FIS_JUR_SAI, NUM_DOCFIS_SAI, SERIE_DOCFIS_SAI, SUB_SERIE_DOCFIS_SAI, DISCRI_ITEM_SAI, NUM_SEQ_ENT

---

## EFD_ITEM_DOCFIS_RESSARC_DEV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL_DEV | DATE | N |  |  |
| 4 | MOVTO_E_S_DEV | CHAR(1) | N |  |  |
| 5 | NORM_DEV_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO_DEV | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR_DEV | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS_DEV | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS_DEV | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS_DEV | VARCHAR2(2) | N |  |  |
| 11 | DISCRI_ITEM_DEV | VARCHAR2(76) | N |  |  |
| 12 | NUM_SEQ_DEV | NUMBER(5) | N |  |  |
| 13 | NUM_ITEM_DEV | NUMBER(5) | Y |  |  |
| 14 | QUANTIDADE_DEV | NUMBER(17,6) | Y |  |  |
| 15 | IND_FIS_JUR_DEV | CHAR(1) | Y |  |  |
| 16 | COD_FIS_JUR_DEV | VARCHAR2(14) | Y |  |  |
| 17 | COD_CFO_DEV | VARCHAR2(4) | Y |  |  |
| 18 | COD_NAT_OP_DEV | VARCHAR2(3) | Y |  |  |
| 19 | GRUPO_PRODUTO_DEV | VARCHAR2(9) | Y |  |  |
| 20 | IND_PRODUTO_DEV | CHAR(1) | Y |  |  |
| 21 | COD_PRODUTO_DEV | VARCHAR2(60) | Y |  |  |
| 22 | DESC_PRODUTO_DEV | VARCHAR2(50) | Y |  |  |
| 23 | GRUPO_MEDIDA_DEV | VARCHAR2(9) | Y |  |  |
| 24 | COD_MEDIDA_DEV | VARCHAR2(8) | Y |  |  |
| 25 | IND_TIPO_REF | CHAR(1) | Y |  |  |
| 26 | QUANT_X192_DEV | NUMBER(17,6) | Y |  |  |
| 27 | DATA_FISCAL_SAI | DATE | Y |  |  |
| 28 | MOVTO_E_S_SAI | CHAR(1) | Y |  |  |
| 29 | NORM_DEV_SAI | CHAR(1) | Y |  |  |
| 30 | IDENT_DOCTO_SAI | NUMBER(12) | Y |  |  |
| 31 | IDENT_FIS_JUR_SAI | NUMBER(12) | Y |  |  |
| 32 | NUM_DOCFIS_SAI | VARCHAR2(12) | Y |  |  |
| 33 | SERIE_DOCFIS_SAI | VARCHAR2(3) | Y |  |  |
| 34 | SUB_SERIE_DOCFIS_SAI | VARCHAR2(2) | Y |  |  |
| 35 | DISCRI_ITEM_SAI | VARCHAR2(76) | Y |  |  |
| 36 | NUM_ITEM_SAI | NUMBER(5) | Y |  |  |
| 37 | IND_FIS_JUR_SAI | CHAR(1) | Y |  |  |
| 38 | COD_FIS_JUR_SAI | VARCHAR2(14) | Y |  |  |
| 39 | COD_CFO_SAI | VARCHAR2(4) | Y |  |  |
| 40 | COD_NAT_OP_SAI | VARCHAR2(3) | Y |  |  |
| 41 | QUANTIDADE_SAI | NUMBER(17,6) | Y |  |  |
| 42 | COD_AJ_RES_SAI | VARCHAR2(10) | Y |  |  |
| 43 | VLR_BASE_AJ_RES_SAI | NUMBER(17,2) | Y |  |  |
| 44 | VLR_ALIQ_AJ_RES_SAI | NUMBER(7,4) | Y |  |  |
| 45 | VLR_AJ_RES_SAI | NUMBER(17,2) | Y |  |  |
| 46 | COD_AJ_CRED_SAI | VARCHAR2(10) | Y |  |  |
| 47 | VLR_BASE_AJ_CRED_SAI | NUMBER(17,2) | Y |  |  |
| 48 | VLR_ALIQ_AJ_CRED_SAI | NUMBER(7,4) | Y |  |  |
| 49 | VLR_AJ_CRED_SAI | NUMBER(17,2) | Y |  |  |
| 50 | COD_AJ_RES_DEV | VARCHAR2(10) | Y |  |  |
| 51 | VLR_BASE_AJ_RES_DEV | NUMBER(17,2) | Y |  |  |
| 52 | VLR_AJ_RES_DEV | NUMBER(17,2) | Y |  |  |
| 53 | TOT_VLR_BASE_AJ_RES_DEV | NUMBER(17,2) | Y |  |  |
| 54 | TOT_VLR_AJ_RES_DEV | NUMBER(17,2) | Y |  |  |
| 55 | COD_AJ_CRED_DEV | VARCHAR2(10) | Y |  |  |
| 56 | VLR_BASE_AJ_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 57 | VLR_AJ_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 58 | TOT_VLR_BASE_AJ_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 59 | TOT_VLR_AJ_CRED_DEV | NUMBER(17,2) | Y |  |  |
| 60 | VLR_AJ_RES_DEV_ESTAB | NUMBER(17,2) | Y |  |  |
| 61 | VLR_AJ_CRED_DEV_ESTAB | NUMBER(17,2) | Y |  |  |
| 62 | PROC_ID | NUMBER | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL_DEV, MOVTO_E_S_DEV, NORM_DEV_DEV, IDENT_DOCTO_DEV, IDENT_FIS_JUR_DEV, NUM_DOCFIS_DEV, SERIE_DOCFIS_DEV, SUB_SERIE_DOCFIS_DEV, DISCRI_ITEM_DEV, NUM_SEQ_DEV

---

## EFD_ITEM_DOCFIS_RESSARC_TEMP
**Comment**: Tabela Temporaria que armazena as NFs de Entrada durante o processamento da EFD_SPED_RESSARC_FPROC. Tabela criada somente auxiliar a geracao da EFD_SPED_RESSARC_FPROC.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | NF de Entrada: Campo da PK. |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | NF de Entrada: Campo da PK. |
| 3 | DATA_FISCAL | DATE | N |  | NF de Entrada: Campo da PK. |
| 4 | MOVTO_E_S | CHAR(1) | N |  | NF de Entrada: Campo da PK. |
| 5 | NORM_DEV | CHAR(1) | N |  | NF de Entrada: Campo da PK. |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  | NF de Entrada: Campo da PK. |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  | NF de Entrada: Campo da PK. |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  | NF de Entrada: Campo da PK. |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  | NF de Entrada: Campo da PK. |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  | NF de Entrada: Campo da PK. |
| 11 | DISCRI_ITEM | VARCHAR2(76) | N |  | NF de Entrada: Campo da PK do Item de Mercadoria. |
| 12 | IDENT_MODELO | NUMBER(12) | Y |  | NF de Entrada: Campo Modelo. |
| 13 | DATA_SAIDA_REC | DATE | Y |  | NF de Entrada: Campo Data de Saida/Recebimento. |
| 14 | DATA_EMISSAO | DATE | Y |  | NF de Entrada: Campo Data de Emissao. |
| 15 | NUM_ITEM | NUMBER(5) | Y |  | NF de Entrada: Campo Numero do Item de mercadoria. |
| 16 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  | NF de Entrada: Campo Grupo Produto do Item de mercadoria. |
| 17 | IND_PRODUTO | CHAR(1) | Y |  | NF de Entrada: Campo Indicador Produto do Item de mercadoria. |
| 18 | COD_PRODUTO | VARCHAR2(60) | Y |  | NF de Entrada: Campo Codigo Produto do Item de mercadoria. |
| 19 | QUANTIDADE | NUMBER(17,6) | Y |  | NF de Entrada: Campo Quantidade do Item de mercadoria. |
| 20 | VLR_UNIT | NUMBER(19,4) | Y |  | NF de Entrada: Campo Valor Unitario do Item de mercadoria. |
| 21 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor da Base Tributada do ICMS-ST do Item de mercadoria. |
| 22 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor de Base ICMS-ST nao escriturado do Item de mercadoria. |
| 23 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  | NF de Entrada: Campo Base Calculo Carga Tributaria Origem ICMS do Item de mercadoria. |
| 24 | IND_NF_REFERENCIADA | CHAR(1) | Y |  | Indica se a NF de Entrada e referenciada por uma NF de Saida com Direito a Ressarcimento. Dominio: S, N. |
| 25 | COD_CFO_ENT | VARCHAR2(4) | Y |  | NF de Entrada: Campo CFOP. |
| 26 | COD_NAT_OP_ENT | VARCHAR2(3) | Y |  | NF de Entrada: Campo Natureza de Operacao. |
| 27 | VLR_PRECO_ENT | NUMBER(19,4) | Y |  | NF de Entrada: Campo Preco Unitario. |
| 28 | VLR_FRETE_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor do Frete. |
| 29 | VLR_SEGURO_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor Seguro. |
| 30 | VLR_OUT_DEP_ENT | NUMBER(17,2) | Y |  | NF de Entrada: Campo Valor Outras Despesas. |
| 31 | VLR_ALIQ_ICMS_ENT | NUMBER(7,4) | Y |  | NF de Entrada: Campo Aliquota ICMS. |
| 32 | VLR_ALIQ_ICMSS_ENT | NUMBER(7,4) | Y |  | NF de Entrada: Campo Aliquota ICMS ST. |
| 33 | VLR_UNIT_MERC_ENT | NUMBER(19,4) | Y |  | NF de Entrada: Campo Valor Unitario da Mercadoria - C176. |
| 34 | VLR_BASE_ST_ENT | NUMBER(18,3) | Y |  | NF de Entrada: Campo Valor Base ICMS ST - C176. |
| 35 | NUM_AUTENTIC_NFE_ENT | VARCHAR2(80) | Y |  |  |
| 36 | VLR_BASE_ICMS_ENT | NUMBER(17,2) | Y |  |  |
| 37 | VLR_BASE_ICMS_OUT_ENT | NUMBER(17,2) | Y |  |  |
| 38 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 39 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 40 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 41 | VLR_BC_ICMS_OP_PROP | NUMBER(17,2) | Y |  |  |
| 42 | VLR_ALIQ_ICMS_ULT_ENT | NUMBER(7,4) | Y |  |  |
| 43 | IND_FORNEC_ICMSS | CHAR(1) | Y |  |  |
| 44 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 45 | IND_MOTIVO_RESSARC | CHAR(1) | Y |  |  |
| 46 | NUM_AUTENTIC_NFE_RET | VARCHAR2(80) | Y |  |  |
| 47 | IDENT_FIS_JUR_RET | NUMBER(12) | Y |  |  |
| 48 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  |  |
| 49 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  |  |
| 50 | NUM_ITEM_RET | NUMBER(5) | Y |  |  |
| 51 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 52 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 53 | GRUPO_MEDIDA_ENT | VARCHAR2(50) | Y |  |  |
| 54 | COD_MEDIDA_ENT | VARCHAR2(8) | Y |  |  |
| 55 | VLR_UNIT_RES_FCP_ST | NUMBER(17,2) | Y |  |  |
| 56 | COD_EMPRESA_ORIG | VARCHAR2(3) | Y |  |  |
| 57 | COD_ESTAB_ORIG | VARCHAR2(6) | Y |  |  |

**PK**: DATA_FISCAL, COD_ESTAB, COD_EMPRESA, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**Indexes**:
- IX_EFD_RESSARC_TEMP_01: (COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_FISCAL, SYS_NC00056$)

---

## EFD_PAR_BLOCO_H

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_GERACAO | DATE | N |  |  |
| 4 | DATA_INVENT | DATE | N |  |  |
| 5 | DESC_LEGIS | VARCHAR2(150) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_GERACAO, DATA_INVENT

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_CFO_E115

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ANEXO | VARCHAR2(6) | N |  |  |
| 4 | COD_INF_ADIC | VARCHAR2(8) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | IND_VAL_REC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ANEXO, COD_INF_ADIC, COD_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_CST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | COD_PARAM | NUMBER(3) | N |  |  |
| 5 | COD_SITUACAO_B | CHAR(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, COD_PARAM, COD_SITUACAO_B

---

## EFD_PAR_CST_E115

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRUPO | VARCHAR2(9) | N |  |  |
| 4 | COD_INF_ADIC | VARCHAR2(8) | N |  |  |
| 5 | COD_SITUACAO_B | CHAR(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRUPO, COD_INF_ADIC, COD_SITUACAO_B

---

## EFD_PAR_EXTCFO_E115

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ANEXO | VARCHAR2(6) | N |  |  |
| 4 | COD_INF_ADIC | VARCHAR2(8) | N |  |  |
| 5 | COD_CFO | VARCHAR2(4) | N |  |  |
| 6 | GRUPO_NATUREZA_OP | VARCHAR2(9) | N |  |  |
| 7 | COD_NATUREZA_OP | VARCHAR2(3) | N |  |  |
| 8 | IND_VAL_REC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ANEXO, COD_INF_ADIC, COD_CFO, GRUPO_NATUREZA_OP, COD_NATUREZA_OP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_GER_C176

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 4 | COD_OBSERVACAO_RES | VARCHAR2(8) | Y |  |  |
| 5 | COD_AJUSTE_SPED_RES | VARCHAR2(10) | Y |  |  |
| 6 | DSC_COMPL_RES | VARCHAR2(250) | Y |  |  |
| 7 | COD_OBSERVACAO_CRED | VARCHAR2(8) | Y |  |  |
| 8 | COD_AJUSTE_SPED_CRED | VARCHAR2(10) | Y |  |  |
| 9 | DSC_COMPL_CRED | VARCHAR2(250) | Y |  |  |
| 10 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 11 | COD_OPER_APUR_RES | VARCHAR2(5) | Y |  |  |
| 12 | DSC_LANC_RES | VARCHAR2(150) | Y |  |  |
| 13 | COD_CLASSE_RES | VARCHAR2(3) | Y |  |  |
| 14 | COD_AMP_LEGAL_RES | VARCHAR2(10) | Y |  |  |
| 15 | COD_SUB_OCORR_RES | VARCHAR2(2) | Y |  |  |
| 16 | COD_OPER_APUR_CRED | VARCHAR2(5) | Y |  |  |
| 17 | DSC_LANC_CRED | VARCHAR2(150) | Y |  |  |
| 18 | COD_CLASSE_CRED | VARCHAR2(3) | Y |  |  |
| 19 | COD_AMP_LEGAL_CRED | VARCHAR2(10) | Y |  |  |
| 20 | COD_SUB_OCORR_CRED | VARCHAR2(2) | Y |  |  |
| 21 | COD_OPER_APUR_EST | VARCHAR2(5) | Y |  |  |
| 22 | DSC_LANC_EST | VARCHAR2(150) | Y |  |  |
| 23 | COD_CLASSE_EST | VARCHAR2(3) | Y |  |  |
| 24 | COD_AMP_LEGAL_EST | VARCHAR2(10) | Y |  |  |
| 25 | COD_SUB_OCORR_EST | VARCHAR2(2) | Y |  |  |
| 26 | COD_AJUSTE_ICMS_EST | VARCHAR2(8) | Y |  |  |
| 27 | COD_OBS_RES_DEV | VARCHAR2(8) | Y |  |  |
| 28 | COD_AJ_SPED_RES_DEV | VARCHAR2(10) | Y |  |  |
| 29 | DSC_COMPL_RES_DEV | VARCHAR2(250) | Y |  |  |
| 30 | COD_OBS_CRED_DEV | VARCHAR2(8) | Y |  |  |
| 31 | COD_AJ_SPED_CRED_DEV | VARCHAR2(10) | Y |  |  |
| 32 | DSC_COMPL_CRED_DEV | VARCHAR2(250) | Y |  |  |
| 33 | COD_OPER_APUR_RES_DEV | VARCHAR2(5) | Y |  |  |
| 34 | DSC_LANC_RES_DEV | VARCHAR2(150) | Y |  |  |
| 35 | COD_CLASSE_RES_DEV | VARCHAR2(3) | Y |  |  |
| 36 | COD_AMP_LEGAL_RES_DEV | VARCHAR2(10) | Y |  |  |
| 37 | COD_SUB_OCORR_RES_DEV | VARCHAR2(2) | Y |  |  |
| 38 | COD_OPER_APUR_CRED_DEV | VARCHAR2(5) | Y |  |  |
| 39 | DSC_LANC_CRED_DEV | VARCHAR2(150) | Y |  |  |
| 40 | COD_CLASSE_CRED_DEV | VARCHAR2(3) | Y |  |  |
| 41 | COD_AMP_LEGAL_CRED_DEV | VARCHAR2(10) | Y |  |  |
| 42 | COD_SUB_OCORR_CRED_DEV | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_AJUSTE_SPED_RES → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_SPED_CRED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_ICMS_EST → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## EFD_PAR_INC_SUB_APUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_VALID | DATE | N |  |  |
| 4 | SERIE_INC | VARCHAR2(3) | N |  |  |
| 5 | SUB_SERIE_INC | VARCHAR2(2) | N |  |  |
| 6 | COD_SUB_APUR_EFD | VARCHAR2(2) | Y |  |  |
| 7 | IND_E110 | CHAR(1) | Y | 'N' |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_VALID, SERIE_INC, SUB_SERIE_INC

---

## EFD_PAR_IND_PROD_0200

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
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, DATA_VALID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_MICRO_GER

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_PARAM | NUMBER(3) | N |  |  |
| 4 | COD_CFO | VARCHAR2(4) | N |  |  |
| 5 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 6 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 8 | COD_SITUACAO_B | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_PARAM, COD_CFO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_SITUACAO_B

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_NBM_C176

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_NBM | VARCHAR2(10) | N |  |  |
| 4 | VLR_ALIQ_INT | NUMBER(7,4) | N |  |  |
| 5 | DATA_INI | DATE | N |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | IND_FCP | VARCHAR2(1) | Y |  |  |
| 8 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 11 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_NBM, VLR_ALIQ_INT, DATA_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_EFD_PAR_NBM_C176_1: (COD_EMPRESA, COD_ESTAB, DATA_INI)
- IX_EFD_PAR_NBM_C176_2: (COD_NBM)

---

## EFD_PAR_NBM_C178

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 5 | COD_NBM | VARCHAR2(10) | N |  |  |
| 6 | DATA_INI | DATE | N |  |  |
| 7 | DATA_FIM | DATE | Y |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | VLR_UNID | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, COD_MODELO, COD_NBM, DATA_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_NCM_0200

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_NBM | VARCHAR2(4) | N |  |  |
| 4 | DATA_VALID | DATE | N |  |  |
| 5 | TIPO_DO_ITEM | VARCHAR2(2) | Y |  |  |
| 6 | USUARIO | VARCHAR2(40) | Y |  |  |
| 7 | DAT_OPERACAO | DATE | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_NBM, DATA_VALID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_PROD_0200

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
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DATA_VALID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_PROD_0221

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | DATA_INI | DATE | N |  |  |
| 7 | DATA_FIM | DATE | Y |  |  |
| 8 | QTD_CONTIDA | NUMBER(17,6) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, DATA_INI

---

## EFD_PAR_PROD_0221_ASS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | DATA_INI | DATE | N |  |  |
| 7 | IND_PRODUTO_ASS | VARCHAR2(1) | N |  |  |
| 8 | COD_PRODUTO_ASS | VARCHAR2(60) | N |  |  |
| 9 | QTD_CONTIDA | NUMBER(17,6) | N |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, DATA_INI, IND_PRODUTO_ASS, COD_PRODUTO_ASS

**FKs**:
- COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, DATA_INI → EFD_PAR_PROD_0221(COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, DATA_INI)

---

## EFD_PAR_PROD_C176

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | VLR_ALIQ_INT | NUMBER(7,4) | N |  |  |
| 7 | DATA_INI | DATE | N |  |  |
| 8 | DATA_FIM | DATE | Y |  |  |
| 9 | IND_FCP | VARCHAR2(1) | Y |  |  |
| 10 | ALIQ_FCP | NUMBER(7,4) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 13 | PRC_REDUCAO_BC | NUMBER(7,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, VLR_ALIQ_INT, DATA_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_EFD_PAR_PROD_C176_1: (COD_EMPRESA, COD_ESTAB, GRUPO, DATA_INI)

---

## EFD_PAR_PROD_C176_ASS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | VLR_ALIQ_INT | NUMBER(7,4) | N |  |  |
| 7 | DATA_INI | DATE | N | TO_DATE('01/01/1900','DD/MM/YYYY') |  |
| 8 | IND_PRODUTO_ASS | CHAR(1) | N |  |  |
| 9 | COD_PRODUTO_ASS | VARCHAR2(60) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, VLR_ALIQ_INT, DATA_INI, IND_PRODUTO_ASS, COD_PRODUTO_ASS

**FKs**:
- COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, VLR_ALIQ_INT, DATA_INI → EFD_PAR_PROD_C176(COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, VLR_ALIQ_INT, DATA_INI)

---

## EFD_PAR_PROD_C178

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 5 | IND_PRODUTO | CHAR(1) | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 7 | DATA_INI | DATE | N |  |  |
| 8 | DATA_FIM | DATE | Y |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | VLR_UNID | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, COD_MODELO, IND_PRODUTO, COD_PRODUTO, DATA_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_PAR_PROD_CST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | COD_SITUACAO_B | CHAR(2) | N |  |  |
| 7 | COD_PARAM | NUMBER(3) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, COD_SITUACAO_B, COD_PARAM

---

## EFD_PAR_RESSARC_MG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 4 | COD_OBSERVACAO_RES | VARCHAR2(8) | Y |  |  |
| 5 | COD_AJUSTE_SPED_RES | VARCHAR2(10) | Y |  |  |
| 6 | COD_AJUSTE_SPED_EST_FEM | VARCHAR2(10) | Y |  |  |
| 7 | COD_AJUSTE_SPED_INFO_FEM | VARCHAR2(10) | Y |  |  |
| 8 | COD_OBSERVACAO_COMPL | VARCHAR2(8) | Y |  |  |
| 9 | COD_AJUSTE_SPED_COMPL | VARCHAR2(10) | Y |  |  |
| 10 | COD_OPER_APUR_RES | VARCHAR2(5) | Y |  |  |
| 11 | DSC_LANC_RES | VARCHAR2(150) | Y |  |  |
| 12 | COD_CLASSE_RES | VARCHAR2(3) | Y |  |  |
| 13 | COD_OPER_APUR_EST_FEM | VARCHAR2(5) | Y |  |  |
| 14 | DSC_LANC_EST_FEM | VARCHAR2(150) | Y |  |  |
| 15 | COD_OPER_APUR_COMPL | VARCHAR2(5) | Y |  |  |
| 16 | DSC_LANC_COMPL | VARCHAR2(150) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_AJUSTE_SPED_RES → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_SPED_EST_FEM → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_SPED_INFO_FEM → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- COD_AJUSTE_SPED_COMPL → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)

---

## EFD_PROD_0205

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_PROD | VARCHAR2(9) | N |  |  |
| 4 | IND_PROD | CHAR(1) | N |  |  |
| 5 | COD_PROD | VARCHAR2(60) | N |  |  |
| 6 | DATA_INI_VALID | DATE | N |  |  |
| 7 | DATA_FIM_VALID | DATE | N |  |  |
| 8 | DATA_GER | DATE | N |  |  |
| 9 | COD_LAYOUT | VARCHAR2(6) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_PROD, IND_PROD, COD_PROD, DATA_INI_VALID, DATA_FIM_VALID, DATA_GER, COD_LAYOUT

---

## EFD_PROD_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 4 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 5 | VALID_PRODUTO | DATE | Y |  |  |

**PK**: IDENT_PRODUTO

**Indexes**:
- IX_EFD_PROD_TEMP: (IND_PRODUTO, COD_PRODUTO, GRUPO_PRODUTO, VALID_PRODUTO)

---

## EFD_REG_1200

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | COD_AJUSTE | VARCHAR2(8) | N |  |  |
| 6 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TOT_CRED_MES | NUMBER(17,2) | Y |  |  |
| 8 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_PERIODO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_TRANSP | NUMBER(17,2) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |
| 12 | DAT_OPERACAO | DATE | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, COD_AJUSTE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_AJUSTE → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## EFD_REG_1200_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_INI | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | COD_AJUSTE | VARCHAR2(8) | N |  |  |
| 7 | VLR_SALDO_ANT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT_CRED_MES | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CRED_TRANSF | NUMBER(17,2) | Y |  |  |
| 10 | VLR_CRED_PERIODO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_CRED_TRANSP | NUMBER(17,2) | Y |  |  |
| 12 | USUARIO | VARCHAR2(40) | Y |  |  |
| 13 | DAT_OPERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INI, DATA_FIM, COD_AJUSTE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_AJUSTE → ICT_AJUSTE_ICMS(COD_AJUSTE_ICMS)

---

## EFD_REG_1210

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | COD_AJUSTE | VARCHAR2(8) | N |  |  |
| 6 | TP_UTIL_CRED | VARCHAR2(4) | N |  |  |
| 7 | NUM_DOC | VARCHAR2(24) | N |  |  |
| 8 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | DAT_OPERACAO | DATE | Y |  |  |
| 11 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, COD_AJUSTE, TP_UTIL_CRED, NUM_DOC

**FKs**:
- TP_UTIL_CRED → EFD_TIPO_CRED(TP_UTIL_CRED)
- COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, COD_AJUSTE → EFD_REG_1200(COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, COD_AJUSTE)

---

## EFD_REG_1210_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_INI | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | COD_AJUSTE | VARCHAR2(8) | N |  |  |
| 7 | TP_UTIL_CRED | VARCHAR2(4) | N |  |  |
| 8 | NUM_DOC | VARCHAR2(24) | N |  |  |
| 9 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | DAT_OPERACAO | DATE | Y |  |  |
| 12 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INI, DATA_FIM, COD_AJUSTE, TP_UTIL_CRED, NUM_DOC

**FKs**:
- TP_UTIL_CRED → EFD_TIPO_CRED(TP_UTIL_CRED)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INI, DATA_FIM, COD_AJUSTE → EFD_REG_1200_IES(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INI, DATA_FIM, COD_AJUSTE)

---

## EFD_REG_1400

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 6 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 7 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 8 | IND_PRODUTO | CHAR(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 10 | VLR_AGREG_CALC | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DED_CALC | NUMBER(17,2) | Y |  |  |
| 12 | VLR_AGREG_INF | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DED_INF | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 15 | DATA_INF | DATE | Y |  |  |
| 16 | COD_ITEM_PART_MUN | VARCHAR2(60) | N |  |  |
| 17 | VLR_AGREG_CONV52 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DED_CONV52 | NUMBER(17,2) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, COD_ESTADO, COD_MUNICIPIO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_ITEM_PART_MUN

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_EFD_REG_1400: (COD_ESTAB, DATA_FIM, DATA_INI, COD_EMPRESA)

---

## EFD_REG_B420

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | COD_SERV_LEI_116 | VARCHAR2(4) | N |  |  |
| 6 | ALIQ_TRIBUTO_ISS | NUMBER(7,4) | N |  |  |
| 7 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, COD_SERV_LEI_116, ALIQ_TRIBUTO_ISS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_REG_B440

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | IND_OPER | VARCHAR2(1) | N |  |  |
| 6 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, IND_OPER, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR

---

## EFD_REG_B470

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_MAT_TERC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_MAT_PROP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_DED | NUMBER(17,2) | Y |  |  |
| 11 | VLR_BASE_ISS_1 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ISS_REC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ISS_RETIDO_REC | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ISS_RECOLHER | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_REG_E115

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | DATA_FIM | DATE | N |  |  |
| 5 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 6 | COD_INF_ADIC | VARCHAR2(8) | N |  |  |
| 7 | VLR_INF_ADIC | NUMBER(17,2) | Y |  |  |
| 8 | DSC_COMPL | VARCHAR2(200) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | DAT_OPERACAO | DATE | Y |  |  |
| 11 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, DATA_FIM, SEQUENCIAL

**FKs**:
- COD_INF_ADIC → EFD_INF_ADIC_APUR(COD_INF_ADIC)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_REG_E115_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | DATA_INI | DATE | N |  |  |
| 5 | DATA_FIM | DATE | N |  |  |
| 6 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 7 | COD_INF_ADIC | VARCHAR2(8) | N |  |  |
| 8 | VLR_INF_ADIC | NUMBER(17,2) | Y |  |  |
| 9 | DSC_COMPL | VARCHAR2(200) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | DAT_OPERACAO | DATE | Y |  |  |
| 12 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, DATA_INI, DATA_FIM, SEQUENCIAL

**FKs**:
- COD_INF_ADIC → EFD_INF_ADIC_APUR(COD_INF_ADIC)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFD_REG_NFCE
**Comment**: Tabela de Totalizacao das Notas Eletronicas (Apuracao Assistida â€“ RS)

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APUR | DATE | N |  |  |
| 4 | IND_SUB_APUR | VARCHAR2(1) | N |  |  |
| 5 | COD_REGISTRO | VARCHAR2(7) | N |  |  |
| 6 | SEQUENCIAL | NUMBER(4) | N |  |  |
| 7 | COD_AJUSTE | VARCHAR2(8) | Y |  |  |
| 8 | DSC_COMPL | VARCHAR2(200) | Y |  |  |
| 9 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 10 | USUARIO | VARCHAR2(40) | Y |  |  |
| 11 | DAT_OPERACAO | DATE | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APUR, IND_SUB_APUR, COD_REGISTRO, SEQUENCIAL

---

## EFD_SALDO_CONV52

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | VL_SLD_CREDOR | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APUR, IDENT_ESTADO

---

## EFD_TIPO_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | TP_UTIL_CRED | VARCHAR2(4) | N |  |  |
| 3 | DSC_CRED | VARCHAR2(100) | Y |  |  |

**PK**: TP_UTIL_CRED

---

