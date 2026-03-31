# Módulo: IRT (IRT) - 55 tabelas

## IRT_CEDULA_C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | ANO_BASE | NUMBER(4) | N |  |  |
| 4 | CPF | VARCHAR2(14) | N |  |  |
| 5 | CLASS_VERBA | CHAR(1) | N |  |  |
| 6 | CLASS_AD_DIM | VARCHAR2(2) | N |  |  |
| 7 | VALOR_1 | NUMBER(17,2) | Y |  |  |
| 8 | VALOR_2 | NUMBER(17,2) | Y |  |  |
| 9 | VALOR_3 | NUMBER(17,2) | Y |  |  |
| 10 | VALOR_4 | NUMBER(17,2) | Y |  |  |
| 11 | VALOR_5 | NUMBER(17,2) | Y |  |  |
| 12 | VALOR_6 | NUMBER(17,2) | Y |  |  |
| 13 | VALOR_7 | NUMBER(17,2) | Y |  |  |
| 14 | VALOR_8 | NUMBER(17,2) | Y |  |  |
| 15 | VALOR_9 | NUMBER(17,2) | Y |  |  |
| 16 | VALOR_10 | NUMBER(17,2) | Y |  |  |
| 17 | VALOR_11 | NUMBER(17,2) | Y |  |  |
| 18 | VALOR_12 | NUMBER(17,2) | Y |  |  |
| 19 | NOME_FUNC | VARCHAR2(70) | Y |  |  |
| 20 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 21 | GRUPO_CUSTO | VARCHAR2(9) | Y |  |  |
| 22 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 23 | GRUPO_SETOR | VARCHAR2(9) | Y |  |  |
| 24 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 25 | GRUPO_VINCULO_EMP | VARCHAR2(9) | Y |  |  |
| 26 | COD_VINCULO_EMP | VARCHAR2(2) | Y |  |  |
| 27 | DESC_VINCULO_EMP | VARCHAR2(100) | Y |  |  |
| 28 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 30 | IND_EXPATRIADO | CHAR(1) | Y |  |  |
| 31 | COD_ESTAB_ORIG | VARCHAR2(6) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, CPF, CLASS_VERBA, CLASS_AD_DIM, COD_FUNC, COD_ESTAB_ORIG

**FKs**:
- COD_EMPRESA, COD_ESTAB_CENTR → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_IRT_CEDULA_C: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, NOME_FUNC, COD_FUNC, CLASS_VERBA, CLASS_AD_DIM)
- IX_IRT_CEDULA_C_2: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, GRUPO_CUSTO, COD_CUSTO, NOME_FUNC, CLASS_VERBA, CLASS_AD_DIM)
- IX_IRT_CEDULA_C_3: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_FUNC, CLASS_VERBA, CLASS_AD_DIM)

---

## IRT_CEDULA_D

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | ANO_BASE | NUMBER(4) | N |  |  |
| 4 | CPF_CGC | VARCHAR2(40) | N |  |  |
| 5 | MES_BASE | NUMBER(2) | N |  |  |
| 6 | GRUPO_RETENCAO | VARCHAR2(9) | N |  |  |
| 7 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 8 | VALOR_REND | NUMBER(17,2) | Y |  |  |
| 9 | ALIQUOTA_IR | NUMBER(5,2) | N |  |  |
| 10 | IRRF_RETIDO | NUMBER(17,2) | Y |  |  |
| 11 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 13 | VALOR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 14 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 15 | VLR_PREV_PRIVADA | NUMBER(17,2) | Y |  |  |
| 16 | VLR_PENS_ALIMENT | NUMBER(17,2) | Y |  |  |
| 17 | DSC_PENS_ALIMENT | VARCHAR2(50) | Y |  |  |
| 18 | VLR_SALARIO_FAM | NUMBER(17,2) | Y |  |  |
| 19 | VLR_APOSENT_ISENTA | NUMBER(17,2) | Y |  |  |
| 20 | VLR_AJUDA_CUSTO | NUMBER(17,2) | Y |  |  |
| 21 | VLR_PENS_INVALID | NUMBER(17,2) | Y |  |  |
| 22 | VLR_LUCRO_PJ | NUMBER(17,2) | Y |  |  |
| 23 | VLR_OUTROS_SOCIO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_OUTROS_DIRF | NUMBER(17,2) | Y |  |  |
| 25 | DSC_OUTROS_DIRF | VARCHAR2(50) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | VLR_DED_INSS_TERC | NUMBER(17,2) | Y |  |  |
| 28 | VLR_DED_DEP_TERC | NUMBER(17,2) | Y |  |  |
| 29 | IND_TP_GERACAO | CHAR(1) | Y |  | 1 = GERAÇÃO DE RENDIMENTOS OUTROS - 2 = GERAÇÃO DE RENDIMENTOS CLIENTES |
| 30 | VLR_OUTROS_TRIB_EXCL | NUMBER(17,2) | Y |  |  |
| 31 | VLR_SALARIO_13 | NUMBER(17,2) | Y |  |  |
| 32 | VLR_TRIBUTO_13 | NUMBER(17,2) | Y |  |  |
| 33 | VLR_APOSENT_ISENTA_13 | NUMBER(17,2) | Y |  |  |
| 34 | VLR_JUROS_MORA | NUMBER(17,2) | Y |  |  |
| 35 | VLR_RESG_PREV_COMPL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, CPF_CGC, MES_BASE, GRUPO_RETENCAO, COD_RETENCAO, ALIQUOTA_IR

**FKs**:
- COD_EMPRESA, COD_ESTAB_CENTR → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1058: (IDENT_FIS_JUR)

---

## IRT_CENTRAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_RETENCAO | VARCHAR2(9) | N |  |  |
| 4 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 5 | DT_INI_CENTR | DATE | N |  |  |
| 6 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 7 | DT_FIM_CENTR | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, GRUPO_RETENCAO, COD_RETENCAO, DT_INI_CENTR, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB_CENTR → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IRT_COD_PG_INSS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PAGTO | VARCHAR2(4) | N |  |  |
| 2 | DSC_PAGTO | VARCHAR2(250) | Y |  |  |
| 3 | IND_AUTONOMO | CHAR(1) | Y |  |  |

**PK**: COD_PAGTO

---

## IRT_DADOS_INICIAIS_DIMOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 4 | COD_UF_SIAFI | VARCHAR2(2) | Y |  |  |
| 5 | COD_MUNIC_SIAFI | VARCHAR2(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_RESPONSAVEL → RESP_INFORMACAO(COD_RESPONSAVEL)
- COD_MUNIC_SIAFI, COD_UF_SIAFI → MUNICIPIO_SIAFI(COD_MUNIC_SIAFI, COD_UF_SIAFI)

---

## IRT_DIPJ_R01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 4 | IND_DECL_RETIFIC | CHAR(1) | Y |  |  |
| 5 | IND_SIT_ESPECIAL | CHAR(1) | Y |  |  |
| 6 | DATA_EVENTO | DATE | Y |  |  |
| 7 | PERIODO_INI | DATE | Y |  |  |
| 8 | PERIODO_FIM | DATE | Y |  |  |
| 9 | IND_FORMA_TRIB | CHAR(1) | Y |  |  |
| 10 | IND_QUALIF_JUR | CHAR(1) | Y |  |  |
| 11 | IND_APUR_IRPJ | CHAR(1) | Y |  |  |
| 12 | IND_TRIM_01 | CHAR(1) | Y |  |  |
| 13 | IND_TRIM_02 | CHAR(1) | Y |  |  |
| 14 | IND_TRIM_03 | CHAR(1) | Y |  |  |
| 15 | IND_TRIM_04 | CHAR(1) | Y |  |  |
| 16 | IND_APUR_INF_IPI | CHAR(1) | Y |  |  |
| 17 | IND_APUR_MES_IPI | CHAR(1) | Y |  |  |
| 18 | ULT_MES_APURAC | VARCHAR2(2) | Y |  |  |
| 19 | IND_ADM_FUNDOS | CHAR(1) | Y |  |  |
| 20 | IND_OPER_EXT | CHAR(1) | Y |  |  |
| 21 | IND_TRIB_FAVOR | CHAR(1) | Y |  |  |
| 22 | IND_PART_EXT | CHAR(1) | Y |  |  |
| 23 | IND_LUCRO_INFLA | CHAR(1) | Y |  |  |
| 24 | IND_LUCRO_EXPLO | CHAR(1) | Y |  |  |
| 25 | IND_ATIV_RURAL | CHAR(1) | Y |  |  |
| 26 | IND_TP_ENTIDADE | VARCHAR2(2) | Y |  |  |
| 27 | IND_DESENQUADRA | CHAR(1) | Y |  |  |
| 28 | DATA_DESENQUADRA | DATE | Y |  |  |
| 29 | IND_OPTANTE_REFIS | CHAR(1) | Y |  |  |
| 30 | IND_AP_IRPJ_CSLL1 | CHAR(1) | Y |  |  |
| 31 | IND_AP_IRPJ_CSLL2 | CHAR(1) | Y |  |  |
| 32 | IND_AP_IRPJ_CSLL3 | CHAR(1) | Y |  |  |
| 33 | IND_AP_IRPJ_CSLL4 | CHAR(1) | Y |  |  |
| 34 | IND_VND_COMB_ALDIF | CHAR(1) | Y |  |  |
| 35 | IND_ISENCAO_REDUC | CHAR(1) | Y |  |  |
| 36 | IND_OPTANTE_RET | CHAR(1) | Y |  |  |
| 37 | ATIVOS_EXTERIOR | CHAR(1) | Y |  |  |
| 38 | NUM_REC_DIPJ_RETIF | NUMBER(12) | Y |  |  |
| 39 | IND_COMBUSTIVEIS | CHAR(1) | Y |  |  |
| 40 | IND_PNEUMATICOS | CHAR(1) | Y |  |  |
| 41 | IND_MAQ_AGRICOLAS | CHAR(1) | Y |  |  |
| 42 | IND_FARMACEUTICOS | CHAR(1) | Y |  |  |
| 43 | IND_PERFUMARIA | CHAR(1) | Y |  |  |
| 44 | IND_PIS_CUM_NCUM | CHAR(1) | Y |  |  |
| 45 | IND_MET_CRED_PIS | CHAR(1) | Y |  |  |
| 46 | IND_OPTANTE_PAES | CHAR(1) | Y | '0' |  |
| 47 | IND_BEBIDAS | CHAR(1) | Y | '0' |  |
| 48 | IND_EMBALAGEM | CHAR(1) | Y | '0' |  |
| 49 | IND_AUTOPECAS | CHAR(1) | Y | '0' |  |
| 50 | IND_PROD_ZF_MANAUS | CHAR(1) | Y | '0' |  |
| 51 | IND_PAPEL_IMUNE | CHAR(1) | Y | '0' |  |
| 52 | IND_FINOR_FINAM_FUNRES | CHAR(1) | Y | '0' |  |
| 53 | IND_COLIG_CONTR | CHAR(1) | Y | '0' |  |
| 54 | IND_TEC_INFORM | CHAR(1) | Y | '0' |  |
| 55 | IND_ROYALTIES_REC | CHAR(1) | Y | '0' |  |
| 56 | IND_ROYALTIES_PAG | CHAR(1) | Y | '0' |  |
| 57 | IND_REND_REL_SERV | CHAR(1) | Y | '0' |  |
| 58 | IND_PAG_TIT_SERV | CHAR(1) | Y | '0' |  |
| 59 | IND_INOV_DES_TEC | CHAR(1) | Y | '0' |  |
| 60 | IND_CAPAC_INCL_DIG | CHAR(1) | Y | '0' |  |
| 61 | IND_HABIL_REPES_RECAP | CHAR(1) | Y | '0' |  |
| 62 | IND_POLO_IND_MANAUS | CHAR(1) | Y | '0' |  |
| 63 | IND_DOA_CAMP_ELEITORAL | CHAR(1) | Y | '0' |  |
| 64 | IND_PJ_COMERC_EXP | CHAR(1) | Y | 0 | Campo 40 - PJ Comercial Exportadora |
| 65 | IND_PJ_VENDA_COMERC_EXP | CHAR(1) | Y | 0 | Campo 41 - PJ Efetuou Vendas a Empresa Comercial Exportadora |
| 66 | VLR_TOT_VENDA_PJ | NUMBER(17,2) | Y |  | Campo 45 ¿ Valor Total da Receita de Vendas da PJ |
| 67 | IND_PJ_ALIQ_CSLL_15 | CHAR(1) | Y |  | PJ Sujeita á Alíquota da CSLL de 15% |
| 68 | IND_OPTANTE_RTT | CHAR(1) | Y |  | Optante pelo RTT |
| 69 | IND_PART_CONSORCIO | CHAR(1) | Y |  |  |
| 70 | IND_REND_REC_EXT | CHAR(1) | Y |  |  |
| 71 | IND_PAGAM_EXT | CHAR(1) | Y |  |  |
| 72 | IND_ZONA_EXP | CHAR(1) | Y |  |  |
| 73 | IND_AREA_LIVRE_COM | CHAR(1) | Y |  |  |
| 74 | IND_FORMA_ESCRIT | CHAR(1) | Y |  |  |
| 75 | IND_OP_REGRA_ART52 | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CALENDARIO

---

## IRT_DIPJ_R02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 4 | NOME_EMPRESARIAL | VARCHAR2(150) | Y |  |  |
| 5 | COD_NAT_JUR | VARCHAR2(4) | Y |  |  |
| 6 | CNAE | VARCHAR2(7) | Y |  |  |
| 7 | DSC_ENDERECO | VARCHAR2(150) | Y |  |  |
| 8 | NUM_ENDERECO | VARCHAR2(6) | Y |  |  |
| 9 | COMPL_ENDERECO | VARCHAR2(50) | Y |  |  |
| 10 | DSC_BAIRRO | VARCHAR2(50) | Y |  |  |
| 11 | DSC_MUNICIPIO | VARCHAR2(50) | Y |  |  |
| 12 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 13 | NUM_CEP | VARCHAR2(8) | Y |  |  |
| 14 | NUM_DDD | VARCHAR2(4) | Y |  |  |
| 15 | NUM_TELEFONE | VARCHAR2(12) | Y |  |  |
| 16 | DDD_FAX | VARCHAR2(4) | Y |  |  |
| 17 | NUM_FAX | VARCHAR2(12) | Y |  |  |
| 18 | CAIXA_POSTAL | VARCHAR2(6) | Y |  |  |
| 19 | UF_CAIXA_POSTAL | VARCHAR2(2) | Y |  |  |
| 20 | CEP_CAIXA_POSTAL | VARCHAR2(8) | Y |  |  |
| 21 | E_MAIL | VARCHAR2(115) | Y |  |  |
| 22 | COD_MUNIC | NUMBER(5) | Y |  |  |
| 23 | TP_LOGRADOURO | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CALENDARIO

---

## IRT_DIPJ_R03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 4 | NOME_REPRESENT | VARCHAR2(150) | Y |  |  |
| 5 | CPF_REPRESENT | VARCHAR2(11) | Y |  |  |
| 6 | DSC_ENDERECO | VARCHAR2(40) | Y |  |  |
| 7 | NUM_ENDERECO | VARCHAR2(6) | Y |  |  |
| 8 | COMPL_ENDERECO | VARCHAR2(21) | Y |  |  |
| 9 | DSC_BAIRRO | VARCHAR2(20) | Y |  |  |
| 10 | DSC_MUNICIPIO | VARCHAR2(50) | Y |  |  |
| 11 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 12 | NUM_CEP | VARCHAR2(8) | Y |  |  |
| 13 | NUM_DDD | VARCHAR2(4) | Y |  |  |
| 14 | NUM_TELEFONE | VARCHAR2(12) | Y |  |  |
| 15 | NUM_RAMAL | VARCHAR2(5) | Y |  |  |
| 16 | DDD_FAX | VARCHAR2(4) | Y |  |  |
| 17 | NUM_FAX | VARCHAR2(12) | Y |  |  |
| 18 | E_MAIL | VARCHAR2(115) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CALENDARIO

---

## IRT_DIPJ_R04

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 4 | NOME_RESPONS | VARCHAR2(150) | Y |  |  |
| 5 | CPF_RESPONSAVEL | VARCHAR2(11) | Y |  |  |
| 6 | CRC_RESPONSAVEL | VARCHAR2(15) | Y |  |  |
| 7 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 8 | NUM_DDD | VARCHAR2(4) | Y |  |  |
| 9 | NUM_TELEFONE | VARCHAR2(12) | Y |  |  |
| 10 | NUM_RAMAL | VARCHAR2(5) | Y |  |  |
| 11 | DDD_FAX | VARCHAR2(4) | Y |  |  |
| 12 | NUM_FAX | VARCHAR2(12) | Y |  |  |
| 13 | E_MAIL | VARCHAR2(115) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CALENDARIO

---

## IRT_DIPJ_R34

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 4 | IND_TIPO_ESTAB | VARCHAR2(2) | Y |  |  |
| 5 | IND_REG_ESP_ST | CHAR(1) | Y |  |  |
| 6 | IND_PROCESS_E | CHAR(1) | Y |  |  |
| 7 | DATA_AUTORIZACAO | DATE | Y |  |  |
| 8 | CNAE_FISCAL | NUMBER(7) | Y |  |  |
| 9 | DAT_ATIV_INICIAL | NUMBER(4) | Y |  |  |
| 10 | DAT_ATIV_FINAL | NUMBER(4) | Y |  |  |
| 11 | IND_IPI_DECENDIAL | CHAR(1) | Y |  |  |
| 12 | IND_IPI_QUINZENAL | CHAR(1) | Y |  |  |
| 13 | MES_INI_IPI_IN394 | NUMBER(2) | Y | 0 |  |
| 14 | MES_FIM_IPI_IN394 | NUMBER(2) | Y | 0 |  |
| 15 | DAT_VALIDADE_INI_ATIVIDADE | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_CALENDARIO

**FKs**:
- CNAE_FISCAL, DAT_VALIDADE_INI_ATIVIDADE → ATIV_ECONOMICA(COD_ATIVIDADE, DAT_VALIDADE_INI)

---

## IRT_DIRF_MM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |
| 3 | ANO_BASE | NUMBER(4) | Y |  |  |
| 4 | CGC_ESTAB_CENTR | VARCHAR2(14) | Y |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | Y |  | Identifica o tipo de beneficiário. Domínio: 1 - Pessoa Física; 2 - Pessoa Jurídica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo próprio código do cadastro. |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | Y |  |  |
| 8 | NOME_BENEF | VARCHAR2(60) | Y |  |  |
| 9 | SEI | CHAR(1) | Y |  |  |
| 10 | ALIQUOTA_IR | NUMBER(3,2) | Y |  |  |
| 11 | VALOR_REND_1 | NUMBER(15,2) | Y |  |  |
| 12 | VALOR_DEDUCOES_1 | NUMBER(15,2) | Y |  |  |
| 13 | IRRF_RETIDO_1 | NUMBER(15,2) | Y |  |  |
| 14 | VALOR_REND_2 | NUMBER(15,2) | Y |  |  |
| 15 | VALOR_DEDUCOES_2 | NUMBER(15,2) | Y |  |  |
| 16 | IRRF_RETIDO_2 | NUMBER(15,2) | Y |  |  |
| 17 | VALOR_REND_3 | NUMBER(15,2) | Y |  |  |
| 18 | VALOR_DEDUCOES_3 | NUMBER(15,2) | Y |  |  |
| 19 | IRRF_RETIDO_3 | NUMBER(15,2) | Y |  |  |
| 20 | VALOR_REND_4 | NUMBER(15,2) | Y |  |  |
| 21 | VALOR_DEDUCOES_4 | NUMBER(15,2) | Y |  |  |
| 22 | IRRF_RETIDO_4 | NUMBER(15,2) | Y |  |  |
| 23 | VALOR_REND_5 | NUMBER(15,2) | Y |  |  |
| 24 | VALOR_DEDUCOES_5 | NUMBER(15,2) | Y |  |  |
| 25 | IRRF_RETIDO_5 | NUMBER(15,2) | Y |  |  |
| 26 | VALOR_REND_6 | NUMBER(15,2) | Y |  |  |
| 27 | VALOR_DEDUCOES_6 | NUMBER(15,2) | Y |  |  |
| 28 | IRRF_RETIDO_6 | NUMBER(15,2) | Y |  |  |
| 29 | VALOR_REND_7 | NUMBER(15,2) | Y |  |  |
| 30 | VALOR_DEDUCOES_7 | NUMBER(15,2) | Y |  |  |
| 31 | IRRF_RETIDO_7 | NUMBER(15,2) | Y |  |  |
| 32 | VALOR_REND_8 | NUMBER(15,2) | Y |  |  |
| 33 | VALOR_DEDUCOES_8 | NUMBER(15,2) | Y |  |  |
| 34 | IRRF_RETIDO_8 | NUMBER(15,2) | Y |  |  |
| 35 | VALOR_REND_9 | NUMBER(15,2) | Y |  |  |
| 36 | VALOR_DEDUCOES_9 | NUMBER(15,2) | Y |  |  |
| 37 | IRRF_RETIDO_9 | NUMBER(15,2) | Y |  |  |
| 38 | VALOR_REND_10 | NUMBER(15,2) | Y |  |  |
| 39 | VALOR_DEDUCOES_10 | NUMBER(15,2) | Y |  |  |
| 40 | IRRF_RETIDO_10 | NUMBER(15,2) | Y |  |  |
| 41 | VALOR_REND_11 | NUMBER(15,2) | Y |  |  |
| 42 | VALOR_DEDUCOES_11 | NUMBER(15,2) | Y |  |  |
| 43 | IRRF_RETIDO_11 | NUMBER(15,2) | Y |  |  |
| 44 | VALOR_REND_12 | NUMBER(15,2) | Y |  |  |
| 45 | VALOR_DEDUCOES_12 | NUMBER(15,2) | Y |  |  |
| 46 | IRRF_RETIDO_12 | NUMBER(15,2) | Y |  |  |
| 47 | VALOR_REND_13 | NUMBER(15,2) | Y |  |  |
| 48 | VALOR_DEDUCOES_13 | NUMBER(15,2) | Y |  |  |
| 49 | IRRF_RETIDO_13 | NUMBER(15,2) | Y |  |  |
| 50 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 51 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 52 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 53 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 54 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 55 | VLR_OUT_TRIB_EXCL_1 | NUMBER(17,2) | Y |  |  |
| 56 | VLR_OUT_TRIB_EXCL_2 | NUMBER(17,2) | Y |  |  |
| 57 | VLR_OUT_TRIB_EXCL_3 | NUMBER(17,2) | Y |  |  |
| 58 | VLR_OUT_TRIB_EXCL_4 | NUMBER(17,2) | Y |  |  |
| 59 | VLR_OUT_TRIB_EXCL_5 | NUMBER(17,2) | Y |  |  |
| 60 | VLR_OUT_TRIB_EXCL_6 | NUMBER(17,2) | Y |  |  |
| 61 | VLR_OUT_TRIB_EXCL_7 | NUMBER(17,2) | Y |  |  |
| 62 | VLR_OUT_TRIB_EXCL_8 | NUMBER(17,2) | Y |  |  |
| 63 | VLR_OUT_TRIB_EXCL_9 | NUMBER(17,2) | Y |  |  |
| 64 | VLR_OUT_TRIB_EXCL_10 | NUMBER(17,2) | Y |  |  |
| 65 | VLR_OUT_TRIB_EXCL_11 | NUMBER(17,2) | Y |  |  |
| 66 | VLR_OUT_TRIB_EXCL_12 | NUMBER(17,2) | Y |  |  |
| 67 | VLR_OUT_TRIB_EXCL_13 | NUMBER(17,2) | Y |  |  |
| 68 | IND_EXT_ESP_SAI | CHAR(1) | Y |  |  |
| 69 | ANO_REF | NUMBER(4) | Y |  |  |
| 70 | DAT_EVENTO | DATE | Y |  |  |
| 71 | USUARIO | VARCHAR2(40) | Y |  |  |
| 72 | IND_SOCIO_OST | CHAR(1) | Y |  |  |
| 73 | DATA_MOLESTIA | DATE | Y |  |  |
| 74 | DSC_RIO | VARCHAR2(60) | Y |  |  |
| 75 | VLR_ISENTO_1 | NUMBER(15,2) | Y |  |  |
| 76 | VLR_ISENTO_2 | NUMBER(15,2) | Y |  |  |
| 77 | VLR_ISENTO_3 | NUMBER(15,2) | Y |  |  |
| 78 | VLR_ISENTO_4 | NUMBER(15,2) | Y |  |  |
| 79 | VLR_ISENTO_5 | NUMBER(15,2) | Y |  |  |
| 80 | VLR_ISENTO_6 | NUMBER(15,2) | Y |  |  |
| 81 | VLR_ISENTO_7 | NUMBER(15,2) | Y |  |  |
| 82 | VLR_ISENTO_8 | NUMBER(15,2) | Y |  |  |
| 83 | VLR_ISENTO_9 | NUMBER(15,2) | Y |  |  |
| 84 | VLR_ISENTO_10 | NUMBER(15,2) | Y |  |  |
| 85 | VLR_ISENTO_11 | NUMBER(15,2) | Y |  |  |
| 86 | VLR_ISENTO_12 | NUMBER(15,2) | Y |  |  |
| 87 | VLR_ISENTO_13 | NUMBER(15,2) | Y |  |  |
| 88 | COD_OPER_SAUDE | VARCHAR2(4) | Y |  |  |
| 89 | VLR_PG_SAUDE_1 | NUMBER(15,2) | Y |  |  |
| 90 | VLR_PG_SAUDE_2 | NUMBER(15,2) | Y |  |  |
| 91 | VLR_PG_SAUDE_3 | NUMBER(15,2) | Y |  |  |
| 92 | VLR_PG_SAUDE_4 | NUMBER(15,2) | Y |  |  |
| 93 | VLR_PG_SAUDE_5 | NUMBER(15,2) | Y |  |  |
| 94 | VLR_PG_SAUDE_6 | NUMBER(15,2) | Y |  |  |
| 95 | VLR_PG_SAUDE_7 | NUMBER(15,2) | Y |  |  |
| 96 | VLR_PG_SAUDE_8 | NUMBER(15,2) | Y |  |  |
| 97 | VLR_PG_SAUDE_9 | NUMBER(15,2) | Y |  |  |
| 98 | VLR_PG_SAUDE_10 | NUMBER(15,2) | Y |  |  |
| 99 | VLR_PG_SAUDE_11 | NUMBER(15,2) | Y |  |  |
| 100 | VLR_PG_SAUDE_12 | NUMBER(15,2) | Y |  |  |
| 101 | VLR_PG_SAUDE_13 | NUMBER(15,2) | Y |  |  |
| 102 | VLR_TOT_REND_EX | NUMBER(15,2) | Y |  |  |
| 103 | VLR_TOT_IRRF_EX | NUMBER(15,2) | Y |  |  |
| 104 | COD_PAIS_BENEF | VARCHAR2(3) | Y |  |  |
| 105 | NIF_BENEF | VARCHAR2(30) | Y |  |  |
| 106 | TP_FONTE_PAG_BENEF | VARCHAR2(3) | Y |  |  |
| 107 | ENDERECO_BENEF | VARCHAR2(50) | Y |  |  |
| 108 | NUM_ENDERECO_BENEF | VARCHAR2(10) | Y |  |  |
| 109 | COMPL_ENDERECO_BENEF | VARCHAR2(45) | Y |  |  |
| 110 | BAIRRO_BENEF | VARCHAR2(20) | Y |  |  |
| 111 | CEP_BENEF | VARCHAR2(8) | Y |  |  |
| 112 | CIDADE_BENEF | VARCHAR2(30) | Y |  |  |
| 113 | DSC_PROVINCIA_BENEF | VARCHAR2(40) | Y |  |  |
| 114 | DDD_BENEF | VARCHAR2(5) | Y |  |  |
| 115 | TELEFONE_BENEF | VARCHAR2(11) | Y |  |  |
| 116 | IND_DISP_NIF | CHAR(1) | Y |  |  |
| 117 | IND_PAIS_N_NIF | CHAR(1) | Y |  |  |
| 118 | VLR_DESC_SIMPL_MENSAL_1 | NUMBER(15,2) | Y |  |  |
| 119 | VLR_DESC_SIMPL_MENSAL_2 | NUMBER(15,2) | Y |  |  |
| 120 | VLR_DESC_SIMPL_MENSAL_3 | NUMBER(15,2) | Y |  |  |
| 121 | VLR_DESC_SIMPL_MENSAL_4 | NUMBER(15,2) | Y |  |  |
| 122 | VLR_DESC_SIMPL_MENSAL_5 | NUMBER(15,2) | Y |  |  |
| 123 | VLR_DESC_SIMPL_MENSAL_6 | NUMBER(15,2) | Y |  |  |
| 124 | VLR_DESC_SIMPL_MENSAL_7 | NUMBER(15,2) | Y |  |  |
| 125 | VLR_DESC_SIMPL_MENSAL_8 | NUMBER(15,2) | Y |  |  |
| 126 | VLR_DESC_SIMPL_MENSAL_9 | NUMBER(15,2) | Y |  |  |
| 127 | VLR_DESC_SIMPL_MENSAL_10 | NUMBER(15,2) | Y |  |  |
| 128 | VLR_DESC_SIMPL_MENSAL_11 | NUMBER(15,2) | Y |  |  |
| 129 | VLR_DESC_SIMPL_MENSAL_12 | NUMBER(15,2) | Y |  |  |
| 130 | VLR_DESC_SIMPL_MENSAL_13 | NUMBER(15,2) | Y |  |  |
| 131 | VLR_DED_EXIG_SUSP_1 | NUMBER(15,2) | Y |  |  |
| 132 | VLR_DED_EXIG_SUSP_2 | NUMBER(15,2) | Y |  |  |
| 133 | VLR_DED_EXIG_SUSP_3 | NUMBER(15,2) | Y |  |  |
| 134 | VLR_DED_EXIG_SUSP_4 | NUMBER(15,2) | Y |  |  |
| 135 | VLR_DED_EXIG_SUSP_5 | NUMBER(15,2) | Y |  |  |
| 136 | VLR_DED_EXIG_SUSP_6 | NUMBER(15,2) | Y |  |  |
| 137 | VLR_DED_EXIG_SUSP_7 | NUMBER(15,2) | Y |  |  |
| 138 | VLR_DED_EXIG_SUSP_8 | NUMBER(15,2) | Y |  |  |
| 139 | VLR_DED_EXIG_SUSP_9 | NUMBER(15,2) | Y |  |  |
| 140 | VLR_DED_EXIG_SUSP_10 | NUMBER(15,2) | Y |  |  |
| 141 | VLR_DED_EXIG_SUSP_11 | NUMBER(15,2) | Y |  |  |
| 142 | VLR_DED_EXIG_SUSP_12 | NUMBER(15,2) | Y |  |  |
| 143 | VLR_DED_EXIG_SUSP_13 | NUMBER(15,2) | Y |  |  |

**Indexes**:
- IX_IRT_DIRF_MM: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)
- IX_IRT_DIRF_MM2: (COD_EMPRESA, COD_ESTAB, ANO_BASE, COD_CTRL_INT)
- IX_IRT_DIRF_MM3: (NUM_PROCESSO)

---

## IRT_DIRF_MM_ANALITICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | ANO_BASE | NUMBER(4) | N |  |  |
| 4 | CGC_ESTAB_CENTR | VARCHAR2(14) | Y |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | Y |  | Identifica o tipo de beneficiário. Domínio: 1 - Pessoa Física; 2 - Pessoa Jurídica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo próprio código do cadastro. |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | Y |  |  |
| 8 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 9 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 10 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 11 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 12 | COD_CLAS_DIRF | CHAR(1) | N |  |  |
| 13 | VALOR_ANALITICO_1 | NUMBER(15,2) | Y |  |  |
| 14 | VALOR_ANALITICO_2 | NUMBER(15,2) | Y |  |  |
| 15 | VALOR_ANALITICO_3 | NUMBER(15,2) | Y |  |  |
| 16 | VALOR_ANALITICO_4 | NUMBER(15,2) | Y |  |  |
| 17 | VALOR_ANALITICO_5 | NUMBER(15,2) | Y |  |  |
| 18 | VALOR_ANALITICO_6 | NUMBER(15,2) | Y |  |  |
| 19 | VALOR_ANALITICO_7 | NUMBER(15,2) | Y |  |  |
| 20 | VALOR_ANALITICO_8 | NUMBER(15,2) | Y |  |  |
| 21 | VALOR_ANALITICO_9 | NUMBER(15,2) | Y |  |  |
| 22 | VALOR_ANALITICO_10 | NUMBER(15,2) | Y |  |  |
| 23 | VALOR_ANALITICO_11 | NUMBER(15,2) | Y |  |  |
| 24 | VALOR_ANALITICO_12 | NUMBER(15,2) | Y |  |  |
| 25 | VALOR_ANALITICO_13 | NUMBER(15,2) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_IRT_DIRF_MM_ANALITICO: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, IND_TP_LANCTO_DIRF, COD_CLAS_DIRF)
- IX_IRT_DIRF_MM_ANALITICO2: (COD_EMPRESA, COD_ESTAB, ANO_BASE, IND_TP_LANCTO_DIRF, COD_CLAS_DIRF, COD_CTRL_INT)
- IX_IRT_DIRF_MM_ANALITICO3: (NUM_PROCESSO)

---

## IRT_DIRF_MM_ANALITICO_VET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | ANO_BASE | NUMBER(4) | N |  |  |
| 4 | CGC_ESTAB_CENTR | VARCHAR2(14) | Y |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | Y |  |  |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 9 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 10 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 11 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 12 | COD_CLAS_DIRF | CHAR(1) | N |  |  |
| 13 | VALOR_ANALITICO_1 | NUMBER(15,2) | Y |  |  |
| 14 | VALOR_ANALITICO_2 | NUMBER(15,2) | Y |  |  |
| 15 | VALOR_ANALITICO_3 | NUMBER(15,2) | Y |  |  |
| 16 | VALOR_ANALITICO_4 | NUMBER(15,2) | Y |  |  |
| 17 | VALOR_ANALITICO_5 | NUMBER(15,2) | Y |  |  |
| 18 | VALOR_ANALITICO_6 | NUMBER(15,2) | Y |  |  |
| 19 | VALOR_ANALITICO_7 | NUMBER(15,2) | Y |  |  |
| 20 | VALOR_ANALITICO_8 | NUMBER(15,2) | Y |  |  |
| 21 | VALOR_ANALITICO_9 | NUMBER(15,2) | Y |  |  |
| 22 | VALOR_ANALITICO_10 | NUMBER(15,2) | Y |  |  |
| 23 | VALOR_ANALITICO_11 | NUMBER(15,2) | Y |  |  |
| 24 | VALOR_ANALITICO_12 | NUMBER(15,2) | Y |  |  |
| 25 | VALOR_ANALITICO_13 | NUMBER(15,2) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: CPF_CGC_BENEF, COD_RETENCAO, IND_TP_LANCTO_DIRF, COD_CLAS_DIRF

---

## IRT_DIRF_MM_DEPEND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiário. Domínio: 1 - Pessoa Física; 2 - Pessoa Jurídica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo próprio código do cadastro. |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 9 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 10 | CPF_DEPEND | VARCHAR2(11) | N |  |  |
| 11 | NOME_DEPEND | VARCHAR2(50) | N |  |  |
| 12 | DT_NASC_DEPEND | DATE | Y |  |  |
| 13 | COD_TIPO_DEPEND | VARCHAR2(2) | Y |  |  |
| 14 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 15 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 16 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 17 | VLR_PG_SAUDE_1 | NUMBER(15,2) | Y |  |  |
| 18 | VLR_PG_SAUDE_2 | NUMBER(15,2) | Y |  |  |
| 19 | VLR_PG_SAUDE_3 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_PG_SAUDE_4 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_PG_SAUDE_5 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_PG_SAUDE_6 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_PG_SAUDE_7 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_PG_SAUDE_8 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_PG_SAUDE_9 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_PG_SAUDE_10 | NUMBER(15,2) | Y |  |  |
| 27 | VLR_PG_SAUDE_11 | NUMBER(15,2) | Y |  |  |
| 28 | VLR_PG_SAUDE_12 | NUMBER(15,2) | Y |  |  |
| 29 | VLR_PG_SAUDE_13 | NUMBER(15,2) | Y |  |  |
| 30 | USUARIO | VARCHAR2(40) | Y |  |  |
| 31 | VLR_PENSAO_1 | NUMBER(15,2) | Y |  |  |
| 32 | VLR_PENSAO_2 | NUMBER(15,2) | Y |  |  |
| 33 | VLR_PENSAO_3 | NUMBER(15,2) | Y |  |  |
| 34 | VLR_PENSAO_4 | NUMBER(15,2) | Y |  |  |
| 35 | VLR_PENSAO_5 | NUMBER(15,2) | Y |  |  |
| 36 | VLR_PENSAO_6 | NUMBER(15,2) | Y |  |  |
| 37 | VLR_PENSAO_7 | NUMBER(15,2) | Y |  |  |
| 38 | VLR_PENSAO_8 | NUMBER(15,2) | Y |  |  |
| 39 | VLR_PENSAO_9 | NUMBER(15,2) | Y |  |  |
| 40 | VLR_PENSAO_10 | NUMBER(15,2) | Y |  |  |
| 41 | VLR_PENSAO_11 | NUMBER(15,2) | Y |  |  |
| 42 | VLR_PENSAO_12 | NUMBER(15,2) | Y |  |  |
| 43 | VLR_PENSAO_13 | NUMBER(15,2) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_RETENCAO, TIPO_BENEF, CPF_CGC_BENEF, IND_TP_LANCTO_DIRF, COD_OPER_SAUDE, CPF_DEPEND, NOME_DEPEND

**Indexes**:
- IX_IRT_DIRF_MM_DEPEND: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)

---

## IRT_DIRF_MM_DEPEND_VET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  |  |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 9 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 10 | CPF_DEPEND | VARCHAR2(11) | N |  |  |
| 11 | NOME_DEPEND | VARCHAR2(50) | N |  |  |
| 12 | DT_NASC_DEPEND | DATE | Y |  |  |
| 13 | COD_TIPO_DEPEND | VARCHAR2(2) | Y |  |  |
| 14 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 15 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 16 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 17 | VLR_PG_SAUDE_1 | NUMBER(15,2) | Y |  |  |
| 18 | VLR_PG_SAUDE_2 | NUMBER(15,2) | Y |  |  |
| 19 | VLR_PG_SAUDE_3 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_PG_SAUDE_4 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_PG_SAUDE_5 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_PG_SAUDE_6 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_PG_SAUDE_7 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_PG_SAUDE_8 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_PG_SAUDE_9 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_PG_SAUDE_10 | NUMBER(15,2) | Y |  |  |
| 27 | VLR_PG_SAUDE_11 | NUMBER(15,2) | Y |  |  |
| 28 | VLR_PG_SAUDE_12 | NUMBER(15,2) | Y |  |  |
| 29 | VLR_PG_SAUDE_13 | NUMBER(15,2) | Y |  |  |
| 30 | USUARIO | VARCHAR2(40) | Y |  |  |
| 31 | VLR_PENSAO_1 | NUMBER(15,2) | Y |  |  |
| 32 | VLR_PENSAO_2 | NUMBER(15,2) | Y |  |  |
| 33 | VLR_PENSAO_3 | NUMBER(15,2) | Y |  |  |
| 34 | VLR_PENSAO_4 | NUMBER(15,2) | Y |  |  |
| 35 | VLR_PENSAO_5 | NUMBER(15,2) | Y |  |  |
| 36 | VLR_PENSAO_6 | NUMBER(15,2) | Y |  |  |
| 37 | VLR_PENSAO_7 | NUMBER(15,2) | Y |  |  |
| 38 | VLR_PENSAO_8 | NUMBER(15,2) | Y |  |  |
| 39 | VLR_PENSAO_9 | NUMBER(15,2) | Y |  |  |
| 40 | VLR_PENSAO_10 | NUMBER(15,2) | Y |  |  |
| 41 | VLR_PENSAO_11 | NUMBER(15,2) | Y |  |  |
| 42 | VLR_PENSAO_12 | NUMBER(15,2) | Y |  |  |
| 43 | VLR_PENSAO_13 | NUMBER(15,2) | Y |  |  |

**PK**: CPF_CGC_BENEF, COD_RETENCAO, IND_TP_LANCTO_DIRF, COD_OPER_SAUDE, CPF_DEPEND, NOME_DEPEND

---

## IRT_DIRF_MM_EX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  |  |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 9 | DATA_PAGTO | DATE | N |  |  |
| 10 | TP_RENDIMENTO | VARCHAR2(3) | N |  |  |
| 11 | TP_TRIBUTACAO_IR | VARCHAR2(2) | N |  |  |
| 12 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 13 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 14 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 15 | VLR_REND_EX | NUMBER(15,2) | Y |  |  |
| 16 | VLR_IRRF_EX | NUMBER(15,2) | Y |  |  |
| 17 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_RETENCAO, TIPO_BENEF, CPF_CGC_BENEF, IND_TP_LANCTO_DIRF, DATA_PAGTO, TP_RENDIMENTO, TP_TRIBUTACAO_IR

**Indexes**:
- IX_IRT_DIRF_MM_EX: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)

---

## IRT_DIRF_MM_INF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiário. Domínio: 1 - Pessoa Física; 2 - Pessoa Jurídica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo próprio código do cadastro. |
| 6 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 7 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 8 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 9 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 10 | DSC_INF | VARCHAR2(200) | Y |  |  |
| 11 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, TIPO_BENEF, CPF_CGC_BENEF

**Indexes**:
- IX_IRT_DIRF_MM_INF: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)

---

## IRT_DIRF_MM_PREV
**Comment**: Tabela de Geracao da DIRF para o bloco de registros INFPC.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiÃ¡rio. DomÃ­nio: 1 - Pessoa FÃ­sica; 2 - Pessoa JurÃ­dica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo prÃ³prio cÃ³digo do cadastro. |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  | 0 - InformaÃ§Ãµes dos BeneficiÃ¡rios; 2 - BeneficiÃ¡rios com rendimento/imposto cuja tributaÃ§Ã£o estÃ¡ sob exigibilidade suspensa. |
| 9 | CNPJ_PREVIDENCIA | VARCHAR2(14) | N |  | CNPJ da Previdencia Complementar. Registro INFPC da DIRF. |
| 10 | IND_TP_PREVIDENCIA | VARCHAR2(2) | N |  | 01 - PrevidÃªncia Privada; 02 - FAPI; 03 - Fundo de PrevidÃªncia do Servidor PÃºblico; 04 - ContribuiÃ§Ã£o do Ente PÃºblico Patrocinador. Registros RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP. |
| 11 | DSC_NOME_PREVIDENCIA | VARCHAR2(150) | Y |  | Nome da Previdencia Complementar. Registro INFPC da DIRF. |
| 12 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 13 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 14 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 15 | VLR_PREV_1 | NUMBER(15,2) | Y |  |  |
| 16 | VLR_PREV_2 | NUMBER(15,2) | Y |  |  |
| 17 | VLR_PREV_3 | NUMBER(15,2) | Y |  |  |
| 18 | VLR_PREV_4 | NUMBER(15,2) | Y |  |  |
| 19 | VLR_PREV_5 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_PREV_6 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_PREV_7 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_PREV_8 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_PREV_9 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_PREV_10 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_PREV_11 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_PREV_12 | NUMBER(15,2) | Y |  |  |
| 27 | VLR_PREV_13 | NUMBER(15,2) | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_RETENCAO, TIPO_BENEF, CPF_CGC_BENEF, IND_TP_LANCTO_DIRF, CNPJ_PREVIDENCIA, IND_TP_PREVIDENCIA

**Indexes**:
- IX_IRT_DIRF_MM_PREV: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)

---

## IRT_DIRF_MM_PREV_VET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  |  |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 9 | CNPJ_PREVIDENCIA | VARCHAR2(14) | N |  |  |
| 10 | IND_TP_PREVIDENCIA | VARCHAR2(2) | N |  |  |
| 11 | DSC_NOME_PREVIDENCIA | VARCHAR2(150) | Y |  |  |
| 12 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 13 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 14 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 15 | VLR_PREV_1 | NUMBER(15,2) | Y |  |  |
| 16 | VLR_PREV_2 | NUMBER(15,2) | Y |  |  |
| 17 | VLR_PREV_3 | NUMBER(15,2) | Y |  |  |
| 18 | VLR_PREV_4 | NUMBER(15,2) | Y |  |  |
| 19 | VLR_PREV_5 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_PREV_6 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_PREV_7 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_PREV_8 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_PREV_9 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_PREV_10 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_PREV_11 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_PREV_12 | NUMBER(15,2) | Y |  |  |
| 27 | VLR_PREV_13 | NUMBER(15,2) | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_RETENCAO, TIPO_BENEF, CPF_CGC_BENEF, IND_TP_LANCTO_DIRF, CNPJ_PREVIDENCIA, IND_TP_PREVIDENCIA

---

## IRT_DIRF_MM_REEMB
**Comment**: Tabela de Geracao da DIRF para o registro de reembolso do titular do plano de saÃºde â€“ coletivo empresarial (identificador RTPSE).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiÃ¡rio. DomÃ­nio: 1 - Pessoa FÃ­sica; 2 - Pessoa JurÃ­dica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo prÃ³prio cÃ³digo do cadastro. |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 9 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 10 | CPF_CNPJ_PREST_SERV | VARCHAR2(14) | N |  | CPF/CNPJ do prestador de serviÃ§o. Registro RTPSE da DIRF. |
| 11 | DSC_PREST_SERV | VARCHAR2(150) | Y |  | Nome do prestador de serviÃ§o. Registro RTPSE da DIRF. |
| 12 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 13 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 14 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 15 | VLR_REEMBOLSO_1 | NUMBER(15,2) | Y |  |  |
| 16 | VLR_REEMBOLSO_ANT_1 | NUMBER(15,2) | Y |  |  |
| 17 | VLR_REEMBOLSO_2 | NUMBER(15,2) | Y |  |  |
| 18 | VLR_REEMBOLSO_ANT_2 | NUMBER(15,2) | Y |  |  |
| 19 | VLR_REEMBOLSO_3 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_REEMBOLSO_ANT_3 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_REEMBOLSO_4 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_REEMBOLSO_ANT_4 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_REEMBOLSO_5 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_REEMBOLSO_ANT_5 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_REEMBOLSO_6 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_REEMBOLSO_ANT_6 | NUMBER(15,2) | Y |  |  |
| 27 | VLR_REEMBOLSO_7 | NUMBER(15,2) | Y |  |  |
| 28 | VLR_REEMBOLSO_ANT_7 | NUMBER(15,2) | Y |  |  |
| 29 | VLR_REEMBOLSO_8 | NUMBER(15,2) | Y |  |  |
| 30 | VLR_REEMBOLSO_ANT_8 | NUMBER(15,2) | Y |  |  |
| 31 | VLR_REEMBOLSO_9 | NUMBER(15,2) | Y |  |  |
| 32 | VLR_REEMBOLSO_ANT_9 | NUMBER(15,2) | Y |  |  |
| 33 | VLR_REEMBOLSO_10 | NUMBER(15,2) | Y |  |  |
| 34 | VLR_REEMBOLSO_ANT_10 | NUMBER(15,2) | Y |  |  |
| 35 | VLR_REEMBOLSO_11 | NUMBER(15,2) | Y |  |  |
| 36 | VLR_REEMBOLSO_ANT_11 | NUMBER(15,2) | Y |  |  |
| 37 | VLR_REEMBOLSO_12 | NUMBER(15,2) | Y |  |  |
| 38 | VLR_REEMBOLSO_ANT_12 | NUMBER(15,2) | Y |  |  |
| 39 | VLR_REEMBOLSO_13 | NUMBER(15,2) | Y |  |  |
| 40 | VLR_REEMBOLSO_ANT_13 | NUMBER(15,2) | Y |  |  |
| 41 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_RETENCAO, TIPO_BENEF, CPF_CGC_BENEF, IND_TP_LANCTO_DIRF, COD_OPER_SAUDE, CPF_CNPJ_PREST_SERV

**Indexes**:
- IX_IRT_DIRF_MM_REEMB: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)

---

## IRT_DIRF_MM_REEMB_DEP
**Comment**: Tabela de Geracao da DIRF para o registro de reembolso do dependente (identificador RDTPSE.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiÃ¡rio. DomÃ­nio: 1 - Pessoa FÃ­sica; 2 - Pessoa JurÃ­dica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo prÃ³prio cÃ³digo do cadastro. |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 9 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 10 | CPF_DEPEND | VARCHAR2(11) | N |  |  |
| 11 | NOME_DEPEND | VARCHAR2(50) | N |  |  |
| 12 | CPF_CNPJ_PREST_SERV | VARCHAR2(14) | N |  | CPF/CNPJ do prestador de serviÃ§o. Registro RDTPSE da DIRF. |
| 13 | DSC_PREST_SERV | VARCHAR2(150) | Y |  | Nome do prestador de serviÃ§o. Registro RDTPSE da DIRF. |
| 14 | DT_NASC_DEPEND | DATE | Y |  |  |
| 15 | COD_TIPO_DEPEND | VARCHAR2(2) | Y |  |  |
| 16 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 17 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 18 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 19 | VLR_REEMBOLSO_1 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_REEMBOLSO_ANT_1 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_REEMBOLSO_2 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_REEMBOLSO_ANT_2 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_REEMBOLSO_3 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_REEMBOLSO_ANT_3 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_REEMBOLSO_4 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_REEMBOLSO_ANT_4 | NUMBER(15,2) | Y |  |  |
| 27 | VLR_REEMBOLSO_5 | NUMBER(15,2) | Y |  |  |
| 28 | VLR_REEMBOLSO_ANT_5 | NUMBER(15,2) | Y |  |  |
| 29 | VLR_REEMBOLSO_6 | NUMBER(15,2) | Y |  |  |
| 30 | VLR_REEMBOLSO_ANT_6 | NUMBER(15,2) | Y |  |  |
| 31 | VLR_REEMBOLSO_7 | NUMBER(15,2) | Y |  |  |
| 32 | VLR_REEMBOLSO_ANT_7 | NUMBER(15,2) | Y |  |  |
| 33 | VLR_REEMBOLSO_8 | NUMBER(15,2) | Y |  |  |
| 34 | VLR_REEMBOLSO_ANT_8 | NUMBER(15,2) | Y |  |  |
| 35 | VLR_REEMBOLSO_9 | NUMBER(15,2) | Y |  |  |
| 36 | VLR_REEMBOLSO_ANT_9 | NUMBER(15,2) | Y |  |  |
| 37 | VLR_REEMBOLSO_10 | NUMBER(15,2) | Y |  |  |
| 38 | VLR_REEMBOLSO_ANT_10 | NUMBER(15,2) | Y |  |  |
| 39 | VLR_REEMBOLSO_11 | NUMBER(15,2) | Y |  |  |
| 40 | VLR_REEMBOLSO_ANT_11 | NUMBER(15,2) | Y |  |  |
| 41 | VLR_REEMBOLSO_12 | NUMBER(15,2) | Y |  |  |
| 42 | VLR_REEMBOLSO_ANT_12 | NUMBER(15,2) | Y |  |  |
| 43 | VLR_REEMBOLSO_13 | NUMBER(15,2) | Y |  |  |
| 44 | VLR_REEMBOLSO_ANT_13 | NUMBER(15,2) | Y |  |  |
| 45 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_RETENCAO, TIPO_BENEF, CPF_CGC_BENEF, IND_TP_LANCTO_DIRF, COD_OPER_SAUDE, CPF_DEPEND, NOME_DEPEND, CPF_CNPJ_PREST_SERV

**Indexes**:
- IX_IRT_DIRF_MM_REEMB_DEP: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)

---

## IRT_DIRF_MM_REEMB_DEP_VET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  |  |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 9 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 10 | CPF_DEPEND | VARCHAR2(11) | N |  |  |
| 11 | NOME_DEPEND | VARCHAR2(50) | N |  |  |
| 12 | CPF_CNPJ_PREST_SERV | VARCHAR2(14) | N |  |  |
| 13 | DSC_PREST_SERV | VARCHAR2(150) | Y |  |  |
| 14 | DT_NASC_DEPEND | DATE | Y |  |  |
| 15 | COD_TIPO_DEPEND | VARCHAR2(2) | Y |  |  |
| 16 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 17 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 18 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 19 | VLR_REEMBOLSO_1 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_REEMBOLSO_ANT_1 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_REEMBOLSO_2 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_REEMBOLSO_ANT_2 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_REEMBOLSO_3 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_REEMBOLSO_ANT_3 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_REEMBOLSO_4 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_REEMBOLSO_ANT_4 | NUMBER(15,2) | Y |  |  |
| 27 | VLR_REEMBOLSO_5 | NUMBER(15,2) | Y |  |  |
| 28 | VLR_REEMBOLSO_ANT_5 | NUMBER(15,2) | Y |  |  |
| 29 | VLR_REEMBOLSO_6 | NUMBER(15,2) | Y |  |  |
| 30 | VLR_REEMBOLSO_ANT_6 | NUMBER(15,2) | Y |  |  |
| 31 | VLR_REEMBOLSO_7 | NUMBER(15,2) | Y |  |  |
| 32 | VLR_REEMBOLSO_ANT_7 | NUMBER(15,2) | Y |  |  |
| 33 | VLR_REEMBOLSO_8 | NUMBER(15,2) | Y |  |  |
| 34 | VLR_REEMBOLSO_ANT_8 | NUMBER(15,2) | Y |  |  |
| 35 | VLR_REEMBOLSO_9 | NUMBER(15,2) | Y |  |  |
| 36 | VLR_REEMBOLSO_ANT_9 | NUMBER(15,2) | Y |  |  |
| 37 | VLR_REEMBOLSO_10 | NUMBER(15,2) | Y |  |  |
| 38 | VLR_REEMBOLSO_ANT_10 | NUMBER(15,2) | Y |  |  |
| 39 | VLR_REEMBOLSO_11 | NUMBER(15,2) | Y |  |  |
| 40 | VLR_REEMBOLSO_ANT_11 | NUMBER(15,2) | Y |  |  |
| 41 | VLR_REEMBOLSO_12 | NUMBER(15,2) | Y |  |  |
| 42 | VLR_REEMBOLSO_ANT_12 | NUMBER(15,2) | Y |  |  |
| 43 | VLR_REEMBOLSO_13 | NUMBER(15,2) | Y |  |  |
| 44 | VLR_REEMBOLSO_ANT_13 | NUMBER(15,2) | Y |  |  |
| 45 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_RETENCAO, TIPO_BENEF, CPF_CGC_BENEF, IND_TP_LANCTO_DIRF, COD_OPER_SAUDE, CPF_DEPEND, NOME_DEPEND, CPF_CNPJ_PREST_SERV

---

## IRT_DIRF_MM_REEMB_VET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  |  |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 8 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 9 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 10 | CPF_CNPJ_PREST_SERV | VARCHAR2(14) | N |  |  |
| 11 | DSC_PREST_SERV | VARCHAR2(150) | Y |  |  |
| 12 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 13 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 14 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 15 | VLR_REEMBOLSO_1 | NUMBER(15,2) | Y |  |  |
| 16 | VLR_REEMBOLSO_ANT_1 | NUMBER(15,2) | Y |  |  |
| 17 | VLR_REEMBOLSO_2 | NUMBER(15,2) | Y |  |  |
| 18 | VLR_REEMBOLSO_ANT_2 | NUMBER(15,2) | Y |  |  |
| 19 | VLR_REEMBOLSO_3 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_REEMBOLSO_ANT_3 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_REEMBOLSO_4 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_REEMBOLSO_ANT_4 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_REEMBOLSO_5 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_REEMBOLSO_ANT_5 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_REEMBOLSO_6 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_REEMBOLSO_ANT_6 | NUMBER(15,2) | Y |  |  |
| 27 | VLR_REEMBOLSO_7 | NUMBER(15,2) | Y |  |  |
| 28 | VLR_REEMBOLSO_ANT_7 | NUMBER(15,2) | Y |  |  |
| 29 | VLR_REEMBOLSO_8 | NUMBER(15,2) | Y |  |  |
| 30 | VLR_REEMBOLSO_ANT_8 | NUMBER(15,2) | Y |  |  |
| 31 | VLR_REEMBOLSO_9 | NUMBER(15,2) | Y |  |  |
| 32 | VLR_REEMBOLSO_ANT_9 | NUMBER(15,2) | Y |  |  |
| 33 | VLR_REEMBOLSO_10 | NUMBER(15,2) | Y |  |  |
| 34 | VLR_REEMBOLSO_ANT_10 | NUMBER(15,2) | Y |  |  |
| 35 | VLR_REEMBOLSO_11 | NUMBER(15,2) | Y |  |  |
| 36 | VLR_REEMBOLSO_ANT_11 | NUMBER(15,2) | Y |  |  |
| 37 | VLR_REEMBOLSO_12 | NUMBER(15,2) | Y |  |  |
| 38 | VLR_REEMBOLSO_ANT_12 | NUMBER(15,2) | Y |  |  |
| 39 | VLR_REEMBOLSO_13 | NUMBER(15,2) | Y |  |  |
| 40 | VLR_REEMBOLSO_ANT_13 | NUMBER(15,2) | Y |  |  |
| 41 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, COD_RETENCAO, TIPO_BENEF, CPF_CGC_BENEF, IND_TP_LANCTO_DIRF, COD_OPER_SAUDE, CPF_CNPJ_PREST_SERV

---

## IRT_DIRF_MM_RRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 4 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiário. Domínio: 1 - Pessoa Física; 2 - Pessoa Jurídica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo próprio código do cadastro. |
| 7 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 8 | VALID_FUNC | DATE | N |  |  |
| 9 | PROC_REQ | VARCHAR2(20) | N |  |  |
| 10 | IND_RRA | CHAR(1) | N |  |  |
| 11 | NATUREZA_RRA | VARCHAR2(50) | N |  |  |
| 12 | CPF_CGC_RESP_JUR | VARCHAR2(14) | Y |  |  |
| 13 | NOME_RESP_JUR | VARCHAR2(150) | Y |  |  |
| 14 | IND_BENEF_MOLESTIA | CHAR(1) | N |  |  |
| 15 | DATA_MOLESTIA | DATE | Y |  |  |
| 16 | VALOR_REND_1 | NUMBER(15,2) | Y |  |  |
| 17 | VALOR_REND_ISENT_1 | NUMBER(15,2) | Y |  |  |
| 18 | VALOR_PREV_OFC_1 | NUMBER(15,2) | Y |  |  |
| 19 | VALOR_PENSAO_1 | NUMBER(15,2) | Y |  |  |
| 20 | IRRF_RETIDO_1 | NUMBER(15,2) | Y |  |  |
| 21 | VALOR_DESP_JUD_1 | NUMBER(15,2) | Y |  |  |
| 22 | QTD_MESES_1 | NUMBER(4,1) | Y |  |  |
| 23 | VALOR_REND_2 | NUMBER(15,2) | Y |  |  |
| 24 | VALOR_REND_ISENT_2 | NUMBER(15,2) | Y |  |  |
| 25 | VALOR_PREV_OFC_2 | NUMBER(15,2) | Y |  |  |
| 26 | VALOR_PENSAO_2 | NUMBER(15,2) | Y |  |  |
| 27 | IRRF_RETIDO_2 | NUMBER(15,2) | Y |  |  |
| 28 | VALOR_DESP_JUD_2 | NUMBER(15,2) | Y |  |  |
| 29 | QTD_MESES_2 | NUMBER(4,1) | Y |  |  |
| 30 | VALOR_REND_3 | NUMBER(15,2) | Y |  |  |
| 31 | VALOR_REND_ISENT_3 | NUMBER(15,2) | Y |  |  |
| 32 | VALOR_PREV_OFC_3 | NUMBER(15,2) | Y |  |  |
| 33 | VALOR_PENSAO_3 | NUMBER(15,2) | Y |  |  |
| 34 | IRRF_RETIDO_3 | NUMBER(15,2) | Y |  |  |
| 35 | VALOR_DESP_JUD_3 | NUMBER(15,2) | Y |  |  |
| 36 | QTD_MESES_3 | NUMBER(4,1) | Y |  |  |
| 37 | VALOR_REND_4 | NUMBER(15,2) | Y |  |  |
| 38 | VALOR_REND_ISENT_4 | NUMBER(15,2) | Y |  |  |
| 39 | VALOR_PREV_OFC_4 | NUMBER(15,2) | Y |  |  |
| 40 | VALOR_PENSAO_4 | NUMBER(15,2) | Y |  |  |
| 41 | IRRF_RETIDO_4 | NUMBER(15,2) | Y |  |  |
| 42 | VALOR_DESP_JUD_4 | NUMBER(15,2) | Y |  |  |
| 43 | QTD_MESES_4 | NUMBER(4,1) | Y |  |  |
| 44 | VALOR_REND_5 | NUMBER(15,2) | Y |  |  |
| 45 | VALOR_REND_ISENT_5 | NUMBER(15,2) | Y |  |  |
| 46 | VALOR_PREV_OFC_5 | NUMBER(15,2) | Y |  |  |
| 47 | VALOR_PENSAO_5 | NUMBER(15,2) | Y |  |  |
| 48 | IRRF_RETIDO_5 | NUMBER(15,2) | Y |  |  |
| 49 | VALOR_DESP_JUD_5 | NUMBER(15,2) | Y |  |  |
| 50 | QTD_MESES_5 | NUMBER(4,1) | Y |  |  |
| 51 | VALOR_REND_6 | NUMBER(15,2) | Y |  |  |
| 52 | VALOR_REND_ISENT_6 | NUMBER(15,2) | Y |  |  |
| 53 | VALOR_PREV_OFC_6 | NUMBER(15,2) | Y |  |  |
| 54 | VALOR_PENSAO_6 | NUMBER(15,2) | Y |  |  |
| 55 | IRRF_RETIDO_6 | NUMBER(15,2) | Y |  |  |
| 56 | VALOR_DESP_JUD_6 | NUMBER(15,2) | Y |  |  |
| 57 | QTD_MESES_6 | NUMBER(4,1) | Y |  |  |
| 58 | VALOR_REND_7 | NUMBER(15,2) | Y |  |  |
| 59 | VALOR_REND_ISENT_7 | NUMBER(15,2) | Y |  |  |
| 60 | VALOR_PREV_OFC_7 | NUMBER(15,2) | Y |  |  |
| 61 | VALOR_PENSAO_7 | NUMBER(15,2) | Y |  |  |
| 62 | IRRF_RETIDO_7 | NUMBER(15,2) | Y |  |  |
| 63 | VALOR_DESP_JUD_7 | NUMBER(15,2) | Y |  |  |
| 64 | QTD_MESES_7 | NUMBER(4,1) | Y |  |  |
| 65 | VALOR_REND_8 | NUMBER(15,2) | Y |  |  |
| 66 | VALOR_REND_ISENT_8 | NUMBER(15,2) | Y |  |  |
| 67 | VALOR_PREV_OFC_8 | NUMBER(15,2) | Y |  |  |
| 68 | VALOR_PENSAO_8 | NUMBER(15,2) | Y |  |  |
| 69 | IRRF_RETIDO_8 | NUMBER(15,2) | Y |  |  |
| 70 | VALOR_DESP_JUD_8 | NUMBER(15,2) | Y |  |  |
| 71 | QTD_MESES_8 | NUMBER(4,1) | Y |  |  |
| 72 | VALOR_REND_9 | NUMBER(15,2) | Y |  |  |
| 73 | VALOR_REND_ISENT_9 | NUMBER(15,2) | Y |  |  |
| 74 | VALOR_PREV_OFC_9 | NUMBER(15,2) | Y |  |  |
| 75 | VALOR_PENSAO_9 | NUMBER(15,2) | Y |  |  |
| 76 | IRRF_RETIDO_9 | NUMBER(15,2) | Y |  |  |
| 77 | VALOR_DESP_JUD_9 | NUMBER(15,2) | Y |  |  |
| 78 | QTD_MESES_9 | NUMBER(4,1) | Y |  |  |
| 79 | VALOR_REND_10 | NUMBER(15,2) | Y |  |  |
| 80 | VALOR_REND_ISENT_10 | NUMBER(15,2) | Y |  |  |
| 81 | VALOR_PREV_OFC_10 | NUMBER(15,2) | Y |  |  |
| 82 | VALOR_PENSAO_10 | NUMBER(15,2) | Y |  |  |
| 83 | IRRF_RETIDO_10 | NUMBER(15,2) | Y |  |  |
| 84 | VALOR_DESP_JUD_10 | NUMBER(15,2) | Y |  |  |
| 85 | QTD_MESES_10 | NUMBER(4,1) | Y |  |  |
| 86 | VALOR_REND_11 | NUMBER(15,2) | Y |  |  |
| 87 | VALOR_REND_ISENT_11 | NUMBER(15,2) | Y |  |  |
| 88 | VALOR_PREV_OFC_11 | NUMBER(15,2) | Y |  |  |
| 89 | VALOR_PENSAO_11 | NUMBER(15,2) | Y |  |  |
| 90 | IRRF_RETIDO_11 | NUMBER(15,2) | Y |  |  |
| 91 | VALOR_DESP_JUD_11 | NUMBER(15,2) | Y |  |  |
| 92 | QTD_MESES_11 | NUMBER(4,1) | Y |  |  |
| 93 | VALOR_REND_12 | NUMBER(15,2) | Y |  |  |
| 94 | VALOR_REND_ISENT_12 | NUMBER(15,2) | Y |  |  |
| 95 | VALOR_PREV_OFC_12 | NUMBER(15,2) | Y |  |  |
| 96 | VALOR_PENSAO_12 | NUMBER(15,2) | Y |  |  |
| 97 | IRRF_RETIDO_12 | NUMBER(15,2) | Y |  |  |
| 98 | VALOR_DESP_JUD_12 | NUMBER(15,2) | Y |  |  |
| 99 | QTD_MESES_12 | NUMBER(4,1) | Y |  |  |
| 100 | VALOR_REND_13 | NUMBER(15,2) | Y |  |  |
| 101 | VALOR_REND_ISENT_13 | NUMBER(15,2) | Y |  |  |
| 102 | VALOR_PREV_OFC_13 | NUMBER(15,2) | Y |  |  |
| 103 | VALOR_PENSAO_13 | NUMBER(15,2) | Y |  |  |
| 104 | IRRF_RETIDO_13 | NUMBER(15,2) | Y |  |  |
| 105 | VALOR_DESP_JUD_13 | NUMBER(15,2) | Y |  |  |
| 106 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 107 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 108 | VALOR_PG_ADVOGADO | NUMBER(15,2) | Y |  | Valor pago para o advogado |
| 109 | VLR_JUROS_MORA | NUMBER(15,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, ANO_CALENDARIO, ANO_REFERENCIA, COD_RETENCAO, TIPO_BENEF, COD_FUNC, VALID_FUNC, PROC_REQ, IND_RRA, NATUREZA_RRA

**FKs**:
- COD_EMPRESA, COD_ESTAB_CENTR, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)

---

## IRT_DIRF_MM_RRA_DEP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 4 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiÃ¡rio. DomÃ­nio: 1 - Pessoa FÃ­sica; 2 - Pessoa JurÃ­dica; 3 - Pessoa residente no exterior, sem CPF-CGC, identificada pelo NIF; 4 - Pessoa residente no exterior, sem CPF-CGC e NIF, identificada pelo prÃ³prio cÃ³digo do cadastro. |
| 7 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 8 | VALID_FUNC | DATE | N |  |  |
| 9 | PROC_REQ | VARCHAR2(20) | N |  |  |
| 10 | IND_RRA | CHAR(1) | N |  |  |
| 11 | NATUREZA_RRA | VARCHAR2(50) | N |  |  |
| 12 | COD_DEPEND | NUMBER(2) | N |  | Codigo do dependente (X55_DEPEND_FUNC). |
| 13 | VALID_DEPEND | DATE | N |  | Validade do dependente (X55_DEPEND_FUNC). |
| 14 | VLR_PENSAO_1 | NUMBER(15,2) | Y |  |  |
| 15 | VLR_PENSAO_2 | NUMBER(15,2) | Y |  |  |
| 16 | VLR_PENSAO_3 | NUMBER(15,2) | Y |  |  |
| 17 | VLR_PENSAO_4 | NUMBER(15,2) | Y |  |  |
| 18 | VLR_PENSAO_5 | NUMBER(15,2) | Y |  |  |
| 19 | VLR_PENSAO_6 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_PENSAO_7 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_PENSAO_8 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_PENSAO_9 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_PENSAO_10 | NUMBER(15,2) | Y |  |  |
| 24 | VLR_PENSAO_11 | NUMBER(15,2) | Y |  |  |
| 25 | VLR_PENSAO_12 | NUMBER(15,2) | Y |  |  |
| 26 | VLR_PENSAO_13 | NUMBER(15,2) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, ANO_CALENDARIO, ANO_REFERENCIA, COD_RETENCAO, TIPO_BENEF, COD_FUNC, VALID_FUNC, PROC_REQ, IND_RRA, NATUREZA_RRA, COD_DEPEND, VALID_DEPEND

**FKs**:
- COD_EMPRESA, COD_ESTAB_CENTR, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)
- COD_EMPRESA, COD_ESTAB_CENTR, COD_FUNC, VALID_FUNC, COD_DEPEND, VALID_DEPEND → X55_DEPEND_FUNC(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, COD_DEPEND, VALID_DEPEND)
- COD_EMPRESA, COD_ESTAB_CENTR, ANO_CALENDARIO, ANO_REFERENCIA, COD_RETENCAO, TIPO_BENEF, COD_FUNC, VALID_FUNC, PROC_REQ, IND_RRA, NATUREZA_RRA → IRT_DIRF_MM_RRA(COD_EMPRESA, COD_ESTAB_CENTR, ANO_CALENDARIO, ANO_REFERENCIA, COD_RETENCAO, TIPO_BENEF, COD_FUNC, VALID_FUNC, PROC_REQ, IND_RRA, NATUREZA_RRA)

---

## IRT_DIRF_MM_SCP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 3 | ANO_CALENDARIO | NUMBER(4) | N |  |  |
| 4 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 5 | IDENT_SCP | NUMBER(22) | N |  | Identificador do Cadastro do SCP (X2057) - registro SCP da DIRF |
| 6 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiÃ¡rio. DomÃ­nio: 1 - Pessoa FÃ­sica; 2 - Pessoa JurÃ­dica |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | N |  | CNPJ ou CPF do Beneficiario - registros BPFSCP, BPFJCP da DIRF |
| 8 | NOME_BENEF | VARCHAR2(150) | Y |  |  |
| 9 | VALOR_PAGO_1 | NUMBER(15,2) | Y |  | Percentual de participacao no SCP - registro RISCP da DIRF |
| 10 | PERC_PARTIC | VARCHAR2(4) | Y |  | Percentual de participacao no SCP - registros BPFSCP, BPFJCP da DIRF |
| 11 | VALOR_PAGO_2 | NUMBER(15,2) | Y |  |  |
| 12 | VALOR_PAGO_3 | NUMBER(15,2) | Y |  |  |
| 13 | VALOR_PAGO_4 | NUMBER(15,2) | Y |  |  |
| 14 | VALOR_PAGO_5 | NUMBER(15,2) | Y |  |  |
| 15 | VALOR_PAGO_6 | NUMBER(15,2) | Y |  |  |
| 16 | VALOR_PAGO_7 | NUMBER(15,2) | Y |  |  |
| 17 | VALOR_PAGO_8 | NUMBER(15,2) | Y |  |  |
| 18 | VALOR_PAGO_9 | NUMBER(15,2) | Y |  |  |
| 19 | VALOR_PAGO_10 | NUMBER(15,2) | Y |  |  |
| 20 | VALOR_PAGO_11 | NUMBER(15,2) | Y |  |  |
| 21 | VALOR_PAGO_12 | NUMBER(15,2) | Y |  |  |
| 22 | VALOR_PAGO_13 | NUMBER(15,2) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB_CENTR, ANO_CALENDARIO, ANO_REFERENCIA, IDENT_SCP, TIPO_BENEF, CPF_CGC_BENEF

**FKs**:
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

---

## IRT_DIRF_MM_TRIBUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |
| 4 | CGC_ESTAB_CENTR | VARCHAR2(14) | Y |  |  |
| 5 | ANO_BASE | NUMBER(4) | Y |  |  |
| 6 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 7 | TIPO_BENEF | NUMBER(1) | Y |  |  |
| 8 | CPF_CGC_BENEF | VARCHAR2(40) | Y |  |  |
| 9 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 10 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 11 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 12 | ANO_REF | NUMBER(4) | Y |  |  |
| 13 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 14 | VALOR_REND_1 | NUMBER(15,2) | Y |  |  |
| 15 | VALOR_DEDUCOES_1 | NUMBER(15,2) | Y |  |  |
| 16 | IRRF_RETIDO_1 | NUMBER(15,2) | Y |  |  |
| 17 | VALOR_REND_2 | NUMBER(15,2) | Y |  |  |
| 18 | VALOR_DEDUCOES_2 | NUMBER(15,2) | Y |  |  |
| 19 | IRRF_RETIDO_2 | NUMBER(15,2) | Y |  |  |
| 20 | VALOR_REND_3 | NUMBER(15,2) | Y |  |  |
| 21 | VALOR_DEDUCOES_3 | NUMBER(15,2) | Y |  |  |
| 22 | IRRF_RETIDO_3 | NUMBER(15,2) | Y |  |  |
| 23 | VALOR_REND_4 | NUMBER(15,2) | Y |  |  |
| 24 | VALOR_DEDUCOES_4 | NUMBER(15,2) | Y |  |  |
| 25 | IRRF_RETIDO_4 | NUMBER(15,2) | Y |  |  |
| 26 | VALOR_REND_5 | NUMBER(15,2) | Y |  |  |
| 27 | VALOR_DEDUCOES_5 | NUMBER(15,2) | Y |  |  |
| 28 | IRRF_RETIDO_5 | NUMBER(15,2) | Y |  |  |
| 29 | VALOR_REND_6 | NUMBER(15,2) | Y |  |  |
| 30 | VALOR_DEDUCOES_6 | NUMBER(15,2) | Y |  |  |
| 31 | IRRF_RETIDO_6 | NUMBER(15,2) | Y |  |  |
| 32 | VALOR_REND_7 | NUMBER(15,2) | Y |  |  |
| 33 | VALOR_DEDUCOES_7 | NUMBER(15,2) | Y |  |  |
| 34 | IRRF_RETIDO_7 | NUMBER(15,2) | Y |  |  |
| 35 | VALOR_REND_8 | NUMBER(15,2) | Y |  |  |
| 36 | VALOR_DEDUCOES_8 | NUMBER(15,2) | Y |  |  |
| 37 | IRRF_RETIDO_8 | NUMBER(15,2) | Y |  |  |
| 38 | VALOR_REND_9 | NUMBER(15,2) | Y |  |  |
| 39 | VALOR_DEDUCOES_9 | NUMBER(15,2) | Y |  |  |
| 40 | IRRF_RETIDO_9 | NUMBER(15,2) | Y |  |  |
| 41 | VALOR_REND_10 | NUMBER(15,2) | Y |  |  |
| 42 | VALOR_DEDUCOES_10 | NUMBER(15,2) | Y |  |  |
| 43 | IRRF_RETIDO_10 | NUMBER(15,2) | Y |  |  |
| 44 | VALOR_REND_11 | NUMBER(15,2) | Y |  |  |
| 45 | VALOR_DEDUCOES_11 | NUMBER(15,2) | Y |  |  |
| 46 | IRRF_RETIDO_11 | NUMBER(15,2) | Y |  |  |
| 47 | VALOR_REND_12 | NUMBER(15,2) | Y |  |  |
| 48 | VALOR_DEDUCOES_12 | NUMBER(15,2) | Y |  |  |
| 49 | IRRF_RETIDO_12 | NUMBER(15,2) | Y |  |  |
| 50 | VALOR_REND_13 | NUMBER(15,2) | Y |  |  |
| 51 | VALOR_DEDUCOES_13 | NUMBER(15,2) | Y |  |  |
| 52 | IRRF_RETIDO_13 | NUMBER(15,2) | Y |  |  |
| 53 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 54 | VLR_OUT_TRIB_EXCL_1 | NUMBER(17,2) | Y |  |  |
| 55 | VLR_OUT_TRIB_EXCL_2 | NUMBER(17,2) | Y |  |  |
| 56 | VLR_OUT_TRIB_EXCL_3 | NUMBER(17,2) | Y |  |  |
| 57 | VLR_OUT_TRIB_EXCL_4 | NUMBER(17,2) | Y |  |  |
| 58 | VLR_OUT_TRIB_EXCL_5 | NUMBER(17,2) | Y |  |  |
| 59 | VLR_OUT_TRIB_EXCL_6 | NUMBER(17,2) | Y |  |  |
| 60 | VLR_OUT_TRIB_EXCL_7 | NUMBER(17,2) | Y |  |  |
| 61 | VLR_OUT_TRIB_EXCL_8 | NUMBER(17,2) | Y |  |  |
| 62 | VLR_OUT_TRIB_EXCL_9 | NUMBER(17,2) | Y |  |  |
| 63 | VLR_OUT_TRIB_EXCL_10 | NUMBER(17,2) | Y |  |  |
| 64 | VLR_OUT_TRIB_EXCL_11 | NUMBER(17,2) | Y |  |  |
| 65 | VLR_OUT_TRIB_EXCL_12 | NUMBER(17,2) | Y |  |  |
| 66 | VLR_OUT_TRIB_EXCL_13 | NUMBER(17,2) | Y |  |  |
| 67 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_IRT_DIRF_MM_TRIB1: (COD_EMPRESA, COD_ESTAB, ANO_BASE, COD_CTRL_INT)
- IX_IRT_DIRF_MM_TRIB2: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)
- IX_IRT_DIRF_MM_TRIB3: (NUM_PROCESSO)

---

## IRT_DIRF_MM_TRIBUTO_VET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |
| 4 | CGC_ESTAB_CENTR | VARCHAR2(14) | Y |  |  |
| 5 | ANO_BASE | NUMBER(4) | Y |  |  |
| 6 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 7 | TIPO_BENEF | NUMBER(1) | Y |  |  |
| 8 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 9 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 10 | ESP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 11 | IND_TP_LANCTO_DIRF | CHAR(1) | N |  |  |
| 12 | ANO_REF | NUMBER(4) | Y |  |  |
| 13 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 14 | VALOR_REND_1 | NUMBER(15,2) | Y |  |  |
| 15 | VALOR_DEDUCOES_1 | NUMBER(15,2) | Y |  |  |
| 16 | IRRF_RETIDO_1 | NUMBER(15,2) | Y |  |  |
| 17 | VALOR_REND_2 | NUMBER(15,2) | Y |  |  |
| 18 | VALOR_DEDUCOES_2 | NUMBER(15,2) | Y |  |  |
| 19 | IRRF_RETIDO_2 | NUMBER(15,2) | Y |  |  |
| 20 | VALOR_REND_3 | NUMBER(15,2) | Y |  |  |
| 21 | VALOR_DEDUCOES_3 | NUMBER(15,2) | Y |  |  |
| 22 | IRRF_RETIDO_3 | NUMBER(15,2) | Y |  |  |
| 23 | VALOR_REND_4 | NUMBER(15,2) | Y |  |  |
| 24 | VALOR_DEDUCOES_4 | NUMBER(15,2) | Y |  |  |
| 25 | IRRF_RETIDO_4 | NUMBER(15,2) | Y |  |  |
| 26 | VALOR_REND_5 | NUMBER(15,2) | Y |  |  |
| 27 | VALOR_DEDUCOES_5 | NUMBER(15,2) | Y |  |  |
| 28 | IRRF_RETIDO_5 | NUMBER(15,2) | Y |  |  |
| 29 | VALOR_REND_6 | NUMBER(15,2) | Y |  |  |
| 30 | VALOR_DEDUCOES_6 | NUMBER(15,2) | Y |  |  |
| 31 | IRRF_RETIDO_6 | NUMBER(15,2) | Y |  |  |
| 32 | VALOR_REND_7 | NUMBER(15,2) | Y |  |  |
| 33 | VALOR_DEDUCOES_7 | NUMBER(15,2) | Y |  |  |
| 34 | IRRF_RETIDO_7 | NUMBER(15,2) | Y |  |  |
| 35 | VALOR_REND_8 | NUMBER(15,2) | Y |  |  |
| 36 | VALOR_DEDUCOES_8 | NUMBER(15,2) | Y |  |  |
| 37 | IRRF_RETIDO_8 | NUMBER(15,2) | Y |  |  |
| 38 | VALOR_REND_9 | NUMBER(15,2) | Y |  |  |
| 39 | VALOR_DEDUCOES_9 | NUMBER(15,2) | Y |  |  |
| 40 | IRRF_RETIDO_9 | NUMBER(15,2) | Y |  |  |
| 41 | VALOR_REND_10 | NUMBER(15,2) | Y |  |  |
| 42 | VALOR_DEDUCOES_10 | NUMBER(15,2) | Y |  |  |
| 43 | IRRF_RETIDO_10 | NUMBER(15,2) | Y |  |  |
| 44 | VALOR_REND_11 | NUMBER(15,2) | Y |  |  |
| 45 | VALOR_DEDUCOES_11 | NUMBER(15,2) | Y |  |  |
| 46 | IRRF_RETIDO_11 | NUMBER(15,2) | Y |  |  |
| 47 | VALOR_REND_12 | NUMBER(15,2) | Y |  |  |
| 48 | VALOR_DEDUCOES_12 | NUMBER(15,2) | Y |  |  |
| 49 | IRRF_RETIDO_12 | NUMBER(15,2) | Y |  |  |
| 50 | VALOR_REND_13 | NUMBER(15,2) | Y |  |  |
| 51 | VALOR_DEDUCOES_13 | NUMBER(15,2) | Y |  |  |
| 52 | IRRF_RETIDO_13 | NUMBER(15,2) | Y |  |  |
| 53 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 54 | VLR_OUT_TRIB_EXCL_1 | NUMBER(17,2) | Y |  |  |
| 55 | VLR_OUT_TRIB_EXCL_2 | NUMBER(17,2) | Y |  |  |
| 56 | VLR_OUT_TRIB_EXCL_3 | NUMBER(17,2) | Y |  |  |
| 57 | VLR_OUT_TRIB_EXCL_4 | NUMBER(17,2) | Y |  |  |
| 58 | VLR_OUT_TRIB_EXCL_5 | NUMBER(17,2) | Y |  |  |
| 59 | VLR_OUT_TRIB_EXCL_6 | NUMBER(17,2) | Y |  |  |
| 60 | VLR_OUT_TRIB_EXCL_7 | NUMBER(17,2) | Y |  |  |
| 61 | VLR_OUT_TRIB_EXCL_8 | NUMBER(17,2) | Y |  |  |
| 62 | VLR_OUT_TRIB_EXCL_9 | NUMBER(17,2) | Y |  |  |
| 63 | VLR_OUT_TRIB_EXCL_10 | NUMBER(17,2) | Y |  |  |
| 64 | VLR_OUT_TRIB_EXCL_11 | NUMBER(17,2) | Y |  |  |
| 65 | VLR_OUT_TRIB_EXCL_12 | NUMBER(17,2) | Y |  |  |
| 66 | VLR_OUT_TRIB_EXCL_13 | NUMBER(17,2) | Y |  |  |
| 67 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: CPF_CGC_BENEF, COD_RETENCAO, IND_TP_LANCTO_DIRF, COD_TRIBUTO, ESP_TRIBUTO

---

## IRT_DIRF_MM_VET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB_CENTR | VARCHAR2(6) | Y |  |  |
| 3 | ANO_BASE | NUMBER(4) | Y |  |  |
| 4 | CGC_ESTAB_CENTR | VARCHAR2(14) | Y |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 6 | TIPO_BENEF | NUMBER(1) | Y |  |  |
| 7 | CPF_CGC_BENEF | VARCHAR2(40) | Y |  |  |
| 8 | NOME_BENEF | VARCHAR2(60) | Y |  |  |
| 9 | SEI | CHAR(1) | Y |  |  |
| 10 | ALIQUOTA_IR | NUMBER(3,2) | Y |  |  |
| 11 | VALOR_REND_1 | NUMBER(15,2) | Y |  |  |
| 12 | VALOR_DEDUCOES_1 | NUMBER(15,2) | Y |  |  |
| 13 | IRRF_RETIDO_1 | NUMBER(15,2) | Y |  |  |
| 14 | VALOR_REND_2 | NUMBER(15,2) | Y |  |  |
| 15 | VALOR_DEDUCOES_2 | NUMBER(15,2) | Y |  |  |
| 16 | IRRF_RETIDO_2 | NUMBER(15,2) | Y |  |  |
| 17 | VALOR_REND_3 | NUMBER(15,2) | Y |  |  |
| 18 | VALOR_DEDUCOES_3 | NUMBER(15,2) | Y |  |  |
| 19 | IRRF_RETIDO_3 | NUMBER(15,2) | Y |  |  |
| 20 | VALOR_REND_4 | NUMBER(15,2) | Y |  |  |
| 21 | VALOR_DEDUCOES_4 | NUMBER(15,2) | Y |  |  |
| 22 | IRRF_RETIDO_4 | NUMBER(15,2) | Y |  |  |
| 23 | VALOR_REND_5 | NUMBER(15,2) | Y |  |  |
| 24 | VALOR_DEDUCOES_5 | NUMBER(15,2) | Y |  |  |
| 25 | IRRF_RETIDO_5 | NUMBER(15,2) | Y |  |  |
| 26 | VALOR_REND_6 | NUMBER(15,2) | Y |  |  |
| 27 | VALOR_DEDUCOES_6 | NUMBER(15,2) | Y |  |  |
| 28 | IRRF_RETIDO_6 | NUMBER(15,2) | Y |  |  |
| 29 | VALOR_REND_7 | NUMBER(15,2) | Y |  |  |
| 30 | VALOR_DEDUCOES_7 | NUMBER(15,2) | Y |  |  |
| 31 | IRRF_RETIDO_7 | NUMBER(15,2) | Y |  |  |
| 32 | VALOR_REND_8 | NUMBER(15,2) | Y |  |  |
| 33 | VALOR_DEDUCOES_8 | NUMBER(15,2) | Y |  |  |
| 34 | IRRF_RETIDO_8 | NUMBER(15,2) | Y |  |  |
| 35 | VALOR_REND_9 | NUMBER(15,2) | Y |  |  |
| 36 | VALOR_DEDUCOES_9 | NUMBER(15,2) | Y |  |  |
| 37 | IRRF_RETIDO_9 | NUMBER(15,2) | Y |  |  |
| 38 | VALOR_REND_10 | NUMBER(15,2) | Y |  |  |
| 39 | VALOR_DEDUCOES_10 | NUMBER(15,2) | Y |  |  |
| 40 | IRRF_RETIDO_10 | NUMBER(15,2) | Y |  |  |
| 41 | VALOR_REND_11 | NUMBER(15,2) | Y |  |  |
| 42 | VALOR_DEDUCOES_11 | NUMBER(15,2) | Y |  |  |
| 43 | IRRF_RETIDO_11 | NUMBER(15,2) | Y |  |  |
| 44 | VALOR_REND_12 | NUMBER(15,2) | Y |  |  |
| 45 | VALOR_DEDUCOES_12 | NUMBER(15,2) | Y |  |  |
| 46 | IRRF_RETIDO_12 | NUMBER(15,2) | Y |  |  |
| 47 | VALOR_REND_13 | NUMBER(15,2) | Y |  |  |
| 48 | VALOR_DEDUCOES_13 | NUMBER(15,2) | Y |  |  |
| 49 | IRRF_RETIDO_13 | NUMBER(15,2) | Y |  |  |
| 50 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 51 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 52 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 53 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 54 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 55 | VLR_OUT_TRIB_EXCL_1 | NUMBER(17,2) | Y |  |  |
| 56 | VLR_OUT_TRIB_EXCL_2 | NUMBER(17,2) | Y |  |  |
| 57 | VLR_OUT_TRIB_EXCL_3 | NUMBER(17,2) | Y |  |  |
| 58 | VLR_OUT_TRIB_EXCL_4 | NUMBER(17,2) | Y |  |  |
| 59 | VLR_OUT_TRIB_EXCL_5 | NUMBER(17,2) | Y |  |  |
| 60 | VLR_OUT_TRIB_EXCL_6 | NUMBER(17,2) | Y |  |  |
| 61 | VLR_OUT_TRIB_EXCL_7 | NUMBER(17,2) | Y |  |  |
| 62 | VLR_OUT_TRIB_EXCL_8 | NUMBER(17,2) | Y |  |  |
| 63 | VLR_OUT_TRIB_EXCL_9 | NUMBER(17,2) | Y |  |  |
| 64 | VLR_OUT_TRIB_EXCL_10 | NUMBER(17,2) | Y |  |  |
| 65 | VLR_OUT_TRIB_EXCL_11 | NUMBER(17,2) | Y |  |  |
| 66 | VLR_OUT_TRIB_EXCL_12 | NUMBER(17,2) | Y |  |  |
| 67 | VLR_OUT_TRIB_EXCL_13 | NUMBER(17,2) | Y |  |  |
| 68 | IND_EXT_ESP_SAI | CHAR(1) | Y |  |  |
| 69 | ANO_REF | NUMBER(4) | Y |  |  |
| 70 | DAT_EVENTO | DATE | Y |  |  |
| 71 | USUARIO | VARCHAR2(40) | Y |  |  |
| 72 | IND_SOCIO_OST | CHAR(1) | Y |  |  |
| 73 | DATA_MOLESTIA | DATE | Y |  |  |
| 74 | DSC_RIO | VARCHAR2(60) | Y |  |  |
| 75 | VLR_ISENTO_1 | NUMBER(15,2) | Y |  |  |
| 76 | VLR_ISENTO_2 | NUMBER(15,2) | Y |  |  |
| 77 | VLR_ISENTO_3 | NUMBER(15,2) | Y |  |  |
| 78 | VLR_ISENTO_4 | NUMBER(15,2) | Y |  |  |
| 79 | VLR_ISENTO_5 | NUMBER(15,2) | Y |  |  |
| 80 | VLR_ISENTO_6 | NUMBER(15,2) | Y |  |  |
| 81 | VLR_ISENTO_7 | NUMBER(15,2) | Y |  |  |
| 82 | VLR_ISENTO_8 | NUMBER(15,2) | Y |  |  |
| 83 | VLR_ISENTO_9 | NUMBER(15,2) | Y |  |  |
| 84 | VLR_ISENTO_10 | NUMBER(15,2) | Y |  |  |
| 85 | VLR_ISENTO_11 | NUMBER(15,2) | Y |  |  |
| 86 | VLR_ISENTO_12 | NUMBER(15,2) | Y |  |  |
| 87 | VLR_ISENTO_13 | NUMBER(15,2) | Y |  |  |
| 88 | COD_OPER_SAUDE | VARCHAR2(4) | Y |  |  |
| 89 | VLR_PG_SAUDE_1 | NUMBER(15,2) | Y |  |  |
| 90 | VLR_PG_SAUDE_2 | NUMBER(15,2) | Y |  |  |
| 91 | VLR_PG_SAUDE_3 | NUMBER(15,2) | Y |  |  |
| 92 | VLR_PG_SAUDE_4 | NUMBER(15,2) | Y |  |  |
| 93 | VLR_PG_SAUDE_5 | NUMBER(15,2) | Y |  |  |
| 94 | VLR_PG_SAUDE_6 | NUMBER(15,2) | Y |  |  |
| 95 | VLR_PG_SAUDE_7 | NUMBER(15,2) | Y |  |  |
| 96 | VLR_PG_SAUDE_8 | NUMBER(15,2) | Y |  |  |
| 97 | VLR_PG_SAUDE_9 | NUMBER(15,2) | Y |  |  |
| 98 | VLR_PG_SAUDE_10 | NUMBER(15,2) | Y |  |  |
| 99 | VLR_PG_SAUDE_11 | NUMBER(15,2) | Y |  |  |
| 100 | VLR_PG_SAUDE_12 | NUMBER(15,2) | Y |  |  |
| 101 | VLR_PG_SAUDE_13 | NUMBER(15,2) | Y |  |  |
| 102 | VLR_TOT_REND_EX | NUMBER(15,2) | Y |  |  |
| 103 | VLR_TOT_IRRF_EX | NUMBER(15,2) | Y |  |  |
| 104 | COD_PAIS_BENEF | VARCHAR2(3) | Y |  |  |
| 105 | NIF_BENEF | VARCHAR2(30) | Y |  |  |
| 106 | TP_FONTE_PAG_BENEF | VARCHAR2(3) | Y |  |  |
| 107 | ENDERECO_BENEF | VARCHAR2(50) | Y |  |  |
| 108 | NUM_ENDERECO_BENEF | VARCHAR2(10) | Y |  |  |
| 109 | COMPL_ENDERECO_BENEF | VARCHAR2(45) | Y |  |  |
| 110 | BAIRRO_BENEF | VARCHAR2(20) | Y |  |  |
| 111 | CEP_BENEF | VARCHAR2(8) | Y |  |  |
| 112 | CIDADE_BENEF | VARCHAR2(30) | Y |  |  |
| 113 | DSC_PROVINCIA_BENEF | VARCHAR2(40) | Y |  |  |
| 114 | DDD_BENEF | VARCHAR2(5) | Y |  |  |
| 115 | TELEFONE_BENEF | VARCHAR2(11) | Y |  |  |
| 116 | IND_DISP_NIF | CHAR(1) | Y |  |  |
| 117 | IND_PAIS_N_NIF | CHAR(1) | Y |  |  |
| 118 | VLR_DESC_SIMPL_MENSAL_1 | NUMBER(15,2) | Y |  |  |
| 119 | VLR_DESC_SIMPL_MENSAL_2 | NUMBER(15,2) | Y |  |  |
| 120 | VLR_DESC_SIMPL_MENSAL_3 | NUMBER(15,2) | Y |  |  |
| 121 | VLR_DESC_SIMPL_MENSAL_4 | NUMBER(15,2) | Y |  |  |
| 122 | VLR_DESC_SIMPL_MENSAL_5 | NUMBER(15,2) | Y |  |  |
| 123 | VLR_DESC_SIMPL_MENSAL_6 | NUMBER(15,2) | Y |  |  |
| 124 | VLR_DESC_SIMPL_MENSAL_7 | NUMBER(15,2) | Y |  |  |
| 125 | VLR_DESC_SIMPL_MENSAL_8 | NUMBER(15,2) | Y |  |  |
| 126 | VLR_DESC_SIMPL_MENSAL_9 | NUMBER(15,2) | Y |  |  |
| 127 | VLR_DESC_SIMPL_MENSAL_10 | NUMBER(15,2) | Y |  |  |
| 128 | VLR_DESC_SIMPL_MENSAL_11 | NUMBER(15,2) | Y |  |  |
| 129 | VLR_DESC_SIMPL_MENSAL_12 | NUMBER(15,2) | Y |  |  |
| 130 | VLR_DESC_SIMPL_MENSAL_13 | NUMBER(15,2) | Y |  |  |
| 131 | VLR_DED_EXIG_SUSP_1 | NUMBER(15,2) | Y |  |  |
| 132 | VLR_DED_EXIG_SUSP_2 | NUMBER(15,2) | Y |  |  |
| 133 | VLR_DED_EXIG_SUSP_3 | NUMBER(15,2) | Y |  |  |
| 134 | VLR_DED_EXIG_SUSP_4 | NUMBER(15,2) | Y |  |  |
| 135 | VLR_DED_EXIG_SUSP_5 | NUMBER(15,2) | Y |  |  |
| 136 | VLR_DED_EXIG_SUSP_6 | NUMBER(15,2) | Y |  |  |
| 137 | VLR_DED_EXIG_SUSP_7 | NUMBER(15,2) | Y |  |  |
| 138 | VLR_DED_EXIG_SUSP_8 | NUMBER(15,2) | Y |  |  |
| 139 | VLR_DED_EXIG_SUSP_9 | NUMBER(15,2) | Y |  |  |
| 140 | VLR_DED_EXIG_SUSP_10 | NUMBER(15,2) | Y |  |  |
| 141 | VLR_DED_EXIG_SUSP_11 | NUMBER(15,2) | Y |  |  |
| 142 | VLR_DED_EXIG_SUSP_12 | NUMBER(15,2) | Y |  |  |
| 143 | VLR_DED_EXIG_SUSP_13 | NUMBER(15,2) | Y |  |  |

---

## IRT_DIRF_MM_VPEIM
**Comment**: Tabela de Geracao da DIRF para o bloco de registros VPEIM, RIMUM, RISEN.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB_CENTR | VARCHAR2(6) | N |  |  |
| 4 | ANO_BASE | NUMBER(4) | N |  |  |
| 5 | TIPO_BENEF | NUMBER(1) | N |  | Identifica o tipo de beneficiario. Dominio: 1 - Pessoa Fisica; 2 - Pessoa Juridica. |
| 6 | CPF_CGC_BENEF | VARCHAR2(40) | N |  |  |
| 7 | IND_IMUNE_ISENTO | CHAR(1) | N |  | 1 - Imune; 2 - Isento. |
| 8 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 9 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 10 | COD_BENEF | VARCHAR2(14) | Y |  |  |
| 11 | VLR_REND_1 | NUMBER(15,2) | Y |  |  |
| 12 | VLR_REND_2 | NUMBER(15,2) | Y |  |  |
| 13 | VLR_REND_3 | NUMBER(15,2) | Y |  |  |
| 14 | VLR_REND_4 | NUMBER(15,2) | Y |  |  |
| 15 | VLR_REND_5 | NUMBER(15,2) | Y |  |  |
| 16 | VLR_REND_6 | NUMBER(15,2) | Y |  |  |
| 17 | VLR_REND_7 | NUMBER(15,2) | Y |  |  |
| 18 | VLR_REND_8 | NUMBER(15,2) | Y |  |  |
| 19 | VLR_REND_9 | NUMBER(15,2) | Y |  |  |
| 20 | VLR_REND_10 | NUMBER(15,2) | Y |  |  |
| 21 | VLR_REND_11 | NUMBER(15,2) | Y |  |  |
| 22 | VLR_REND_12 | NUMBER(15,2) | Y |  |  |
| 23 | VLR_REND_13 | NUMBER(15,2) | Y |  |  |
| 24 | USUARIO | VARCHAR2(40) | Y |  |  |
| 25 | NOME_BENEF | VARCHAR2(150) | Y |  |  |

**PK**: NUM_PROCESSO, COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE, TIPO_BENEF, CPF_CGC_BENEF, IND_IMUNE_ISENTO

**Indexes**:
- IX_IRT_DIRF_MM_VPEIM: (COD_EMPRESA, COD_ESTAB_CENTR, ANO_BASE)

---

## IRT_ESTRANGEIRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | CPF_CGC | VARCHAR2(14) | N |  |  |
| 3 | IND_PFJ_FUNC | CHAR(1) | Y |  |  |
| 4 | DAT_ENTRADA_IR | DATE | Y |  |  |

**PK**: COD_EMPRESA, CPF_CGC

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

---

## IRT_FAIXA_RETENCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_VALIDADE | DATE | N |  |  |
| 2 | VLR_LIMITE | NUMBER(17,2) | N |  |  |
| 3 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |
| 4 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |

**PK**: DATA_VALIDADE, VLR_LIMITE

---

## IRT_GPS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 4 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 5 | COD_PAGTO | VARCHAR2(4) | N |  |  |
| 6 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 9 | SEQ_REGISTRO | NUMBER(3) | N |  |  |
| 10 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 11 | VLR_INSS | NUMBER(17,2) | Y |  |  |
| 12 | IND_OUTROS1 | CHAR(1) | Y |  |  |
| 13 | DSC_OUTROS1 | VARCHAR2(15) | Y |  |  |
| 14 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 15 | IND_OUTROS2 | CHAR(1) | Y |  |  |
| 16 | DSC_OUTROS2 | VARCHAR2(15) | Y |  |  |
| 17 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_OUTRAS_ENTID | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ATM | NUMBER(17,2) | Y |  |  |
| 20 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 22 | VLR_CORRECAO | NUMBER(17,2) | Y |  |  |
| 23 | VLR_TOT_RECOLH | NUMBER(17,2) | Y |  |  |
| 24 | VLR_EMPRESA | NUMBER(17,2) | Y |  |  |
| 25 | VLR_EMPREGADO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 27 | DAT_PAGTO | DATE | Y |  |  |
| 28 | VLR_PAGTO | NUMBER(17,2) | Y |  |  |
| 29 | COD_BANCO | VARCHAR2(4) | Y |  |  |
| 30 | COD_AGENCIA | VARCHAR2(5) | Y |  |  |
| 31 | DSC_PRACA | VARCHAR2(30) | Y |  |  |
| 32 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 33 | DAT_EXTEMP | DATE | Y |  |  |
| 34 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 35 | USUARIO | VARCHAR2(40) | Y |  |  |
| 36 | COD_CEI | VARCHAR2(12) | Y |  |  |
| 37 | DAT_ENVIO_BANC | DATE | Y |  |  |
| 38 | AUTENTIC_BANC | VARCHAR2(27) | Y |  |  |
| 39 | DAT_FISCAL | DATE | Y |  |  |
| 40 | STATUS_GUIA | CHAR(1) | Y |  |  |
| 41 | IND_FONTE_AVULSO | CHAR(1) | Y |  |  |
| 42 | ID_GER | NUMBER(12) | Y |  |  |
| 43 | SEQ_GER_ARQ | NUMBER(12) | Y |  |  |
| 44 | TXT_GER_ARQ | VARCHAR2(4000) | Y |  |  |
| 45 | DAT_FISCAL_REAL | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMPETENCIA, MES_COMPETENCIA, COD_PAGTO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, SEQ_REGISTRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_PAGTO → IRT_COD_PG_INSS(COD_PAGTO)

---

## IRT_INF_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | NUM_OCOR | NUMBER(1) | N |  |  |
| 5 | IND_TIPO | CHAR(1) | Y |  |  |
| 6 | CPF | VARCHAR2(11) | Y |  |  |
| 7 | NOME | VARCHAR2(50) | Y |  |  |
| 8 | NUM_PROC_JUD | VARCHAR2(15) | Y |  |  |
| 9 | DAT_DECISAO | DATE | Y |  |  |
| 10 | TRIB_JUST | VARCHAR2(5) | Y |  |  |
| 11 | VARA_JUDICIAL | VARCHAR2(2) | Y |  |  |
| 12 | VLR_PENSAO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, NUM_OCOR

---

## IRT_INSS_FATUR_CED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 8 | VLR_FATURAMENTO | NUMBER(17,2) | Y |  |  |
| 9 | IND_LIQUIDADO | CHAR(1) | Y | 'N' | Indicará quando o saldo for utilizado para lançamento na GPS. Até o momento em que for utilizado, este saldo será acumulado e transportado através dos meses apurados. |
| 10 | COD_PAGTO_INSS | VARCHAR2(4) | N |  |  |
| 11 | COD_CEI | VARCHAR2(12) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, MES_COMPETENCIA, ANO_COMPETENCIA, COD_PAGTO_INSS, COD_CEI

**FKs**:
- COD_PAGTO_INSS → IRT_COD_PG_INSS(COD_PAGTO)

---

## IRT_LIST_TRIB_FED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_COMP | DATE | N |  |  |
| 4 | DATA_FIM_COMP | DATE | N |  |  |
| 5 | CPF_CGC | VARCHAR2(14) | N |  |  |
| 6 | NUM_DOC | VARCHAR2(12) | N |  |  |
| 7 | SER_DOC | VARCHAR2(3) | N |  |  |
| 8 | SUB_DOC | VARCHAR2(2) | N |  |  |
| 9 | COD_DARF | VARCHAR2(4) | N |  |  |
| 10 | RAZAO_SOC | VARCHAR2(70) | Y |  |  |
| 11 | DT_MOVTO | DATE | Y |  |  |
| 12 | DT_FATO_GERADOR | DATE | Y |  |  |
| 13 | COD_TRIB | VARCHAR2(2) | Y |  |  |
| 14 | COD_ESPECIE | VARCHAR2(2) | Y |  |  |
| 15 | DSC_TRIB | VARCHAR2(100) | Y |  |  |
| 16 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 17 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 19 | ALIQUOTA | NUMBER(5,2) | Y |  |  |
| 20 | OBS | VARCHAR2(200) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI_COMP, DATA_FIM_COMP, CPF_CGC, NUM_DOC, SER_DOC, SUB_DOC, COD_DARF

---

## IRT_NOMENCLATURA_IN698

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | CLASS_DARF | CHAR(1) | N |  |  |
| 2 | CLASS_NUM_ORD | VARCHAR2(2) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |

**PK**: CLASS_DARF, CLASS_NUM_ORD

---

## IRT_PAR_CED_C

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_VERBA | VARCHAR2(9) | N |  |  |
| 4 | COD_VERBA | VARCHAR2(6) | N |  |  |
| 5 | CLASS_VERBA | CHAR(1) | Y |  |  |
| 6 | CLASS_AD_DIM | VARCHAR2(2) | Y |  |  |
| 7 | COD_CLAS_DIRF | CHAR(1) | Y |  |  |
| 8 | DESCRICAO | VARCHAR2(60) | Y |  |  |
| 9 | COD_OPER_SAUDE | VARCHAR2(4) | Y |  |  |
| 10 | IND_INCIDE_PLR | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_VERBA, COD_VERBA

**FKs**:
- CLASS_VERBA, CLASS_AD_DIM → DIRF_NOMENCLATURA(CLASS_VERBA, CLASS_AD_DIM)
- COD_OPER_SAUDE → DWT_OPERADORA_SAUDE(COD_OPER_SAUDE)

---

## IRT_PAR_COD_REC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_DARF | VARCHAR2(9) | N |  |  |
| 4 | COD_DARF | VARCHAR2(4) | N |  |  |
| 5 | CLASS_DARF | CHAR(1) | N |  |  |
| 6 | CLASS_NUM_ORD | VARCHAR2(2) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_DARF, COD_DARF

**FKs**:
- CLASS_DARF, CLASS_NUM_ORD → IRT_NOMENCLATURA_IN698(CLASS_DARF, CLASS_NUM_ORD)

---

## IRT_PAR_DARF_QUOTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_DARF | NUMBER(12) | N |  |  |
| 4 | QTD_MAX_QUOTAS | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_DARF

**FKs**:
- IDENT_DARF → X2019_COD_DARF(IDENT_DARF)

---

## IRT_PAR_DESCONTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_VALIDADE | DATE | N |  |  |
| 2 | VLR_DESCONTO_DEP | NUMBER(17,2) | Y |  |  |
| 3 | VLR_DESC_APOSEN | NUMBER(17,2) | Y |  |  |
| 4 | VLR_SAL_CONTRIB | NUMBER(17,2) | Y |  |  |
| 5 | VLR_MAXSAL_CONTRIB | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TX_INSS_EMPRESA | NUMBER(7,4) | Y |  |  |

**PK**: DATA_VALIDADE

---

## IRT_PAR_INSS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 2 | DIA_VENCTO | NUMBER(2) | Y |  |  |
| 3 | IND_CONSOLIDA | CHAR(1) | Y |  |  |
| 4 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 5 | IND_MOVTO | CHAR(1) | Y |  |  |
| 6 | IND_RET_EMISS_CPAG_CINDIVIDUAL | CHAR(1) | Y | 'N' | Considerar retencoes para emissao do Comprovante de Pagamento a Contribuinte Individual |

**PK**: COD_RETENCAO

---

## IRT_PAR_INSS_C_ALQ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RETENCAO | VARCHAR2(4) | N |  |  |
| 2 | VLR_ALIQ_INSS | NUMBER(11,4) | N |  | Este campo faz parte da chave, por motivos técnicos o mesmo foi criado como inteiro, no entanto será efetuado tratamento na janela para exibílio como decimal, a durante seu uso na procedure, o mesmo será recalculado. O número de casas decimais é de 4 dígitos. |
| 3 | DIA_VENCTO | NUMBER(2) | Y |  |  |
| 4 | IND_CONSOLIDA | CHAR(1) | Y |  |  |
| 5 | IND_MOVTO | CHAR(1) | Y |  |  |
| 6 | IND_RET_EMISS_CPAG_CINDIVIDUAL | CHAR(1) | Y | 'N' | Considerar retencoes para emissao do Comprovante de Pagamento a Contribuinte Individual |

**PK**: COD_RETENCAO, VLR_ALIQ_INSS

---

## IRT_PAR_RETENCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 4 | USUARIO | VARCHAR2(40) | Y |  |  |

**Indexes**:
- IX_IRT_PAR_RET: (USUARIO, COD_EMPRESA, COD_ESTAB, COD_RETENCAO)

---

## IRT_PAR_RET_INSS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | DATA_VALIDADE | DATE | N |  |  |
| 2 | VLR_TETO_FAIXA | NUMBER(17,2) | N |  |  |
| 3 | VLR_ALIQUOTA | NUMBER(7,4) | Y |  |  |

**PK**: DATA_VALIDADE, VLR_TETO_FAIXA

---

## IRT_PROG_RET

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PROG | NUMBER(12) | N |  |  |
| 2 | ANO_CALENDARIO | NUMBER(4) | Y |  |  |
| 3 | TIPO_CENTRALIZACAO | CHAR(1) | Y |  |  |
| 4 | IND_ABRANGENCIA | CHAR(1) | Y |  |  |
| 5 | IND_DED_CONTR_PREV | CHAR(1) | Y |  |  |
| 6 | IND_PARAM_OP | CHAR(1) | Y |  |  |
| 7 | DESC_PROG | VARCHAR2(50) | Y |  |  |
| 8 | DIA_EXECUCAO | NUMBER(2) | Y |  |  |
| 9 | ULT_DIA_MES | NUMBER(2) | Y |  |  |
| 10 | HORARIO | DATE | Y |  |  |
| 11 | IND_ATIVO | CHAR(1) | Y |  |  |

**PK**: ID_PROG

---

## IRT_PROG_RET_EMP_ESTAB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PROG | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |

**PK**: ID_PROG, COD_EMPRESA, COD_ESTAB

**FKs**:
- ID_PROG → IRT_PROG_RET(ID_PROG)

---

## IRT_REGIME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IND_REG_CAIXA_PFJ | CHAR(1) | Y |  |  |
| 3 | IND_REG_CAIXA_FUNC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA

---

## IRT_REL_IN698

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | NUMBER(4) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | CLASS_DARF | CHAR(1) | N |  |  |
| 6 | CLASS_NUM_ORD | VARCHAR2(2) | N |  |  |
| 7 | VLR_REND | NUMBER(17,2) | Y |  |  |
| 8 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ANO_REF | NUMBER(17,2) | Y |  |  |
| 11 | INFO_COMPL | VARCHAR2(70) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | USUARIO | VARCHAR2(40) | Y |  |  |
| 14 | VLR_DEMAIS_REND | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TIT_CAP_ANO_REND | NUMBER(17,2) | Y |  |  |
| 16 | VLR_PREV_REND | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IU_IRT_REL_IN698 (UNIQUE): (COD_EMPRESA, COD_ESTAB, ANO_REF, IDENT_FIS_JUR, CLASS_DARF, CLASS_NUM_ORD, NUM_PROCESSO)

---

## IRT_RETENCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 4 | VLR_ALIQ | NUMBER(5,2) | Y |  |  |
| 5 | DATA_PAGTO | DATE | Y |  |  |
| 6 | ANO_COMP | NUMBER(4) | Y |  |  |
| 7 | MES_COMP | NUMBER(2) | Y |  |  |
| 8 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 9 | NOME | VARCHAR2(70) | Y |  |  |
| 10 | NUM_AP | VARCHAR2(10) | Y |  |  |
| 11 | TP_QUITACAO | CHAR(1) | Y |  |  |
| 12 | VLR_TRIBUTAVEL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_RETIDO_CONV | NUMBER(17,2) | Y |  |  |
| 14 | VLR_RETIDO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 16 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 17 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 18 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | USUARIO | VARCHAR2(40) | Y |  |  |
| 21 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 22 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 23 | DESC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 24 | DSC_ABREV | VARCHAR2(15) | Y |  |  |
| 25 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 26 | DATA_INI_COMP | DATE | Y |  |  |
| 27 | DATA_FIM_COMP | DATE | Y |  |  |
| 28 | DAT_FATO_GERADOR | DATE | Y |  |  |
| 29 | VLR_DED_INSS_TERC | NUMBER(17,2) | Y |  |  |
| 30 | VLR_PREV_PRIVADA | NUMBER(17,2) | Y |  |  |
| 31 | VLR_DED_DEP_TERC | NUMBER(17,2) | Y |  |  |
| 32 | VLR_PENS_ALIMENT | NUMBER(17,2) | Y |  |  |
| 33 | SITUACAO | CHAR(1) | Y |  |  |
| 34 | DATA_VENCTO | DATE | Y |  |  |
| 35 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 36 | IND_ORIGEM_SAFX | VARCHAR2(10) | Y |  |  |
| 37 | VLR_REND_S_RET_IR | NUMBER(17,2) | Y |  |  |
| 38 | IND_TIPO_REND | VARCHAR2(1) | Y |  |  |
| 39 | IND_TP_PROC_ADJ | VARCHAR2(1) | Y |  |  |
| 40 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 41 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 42 | VLR_DESP_JUD_X531 | NUMBER(17,2) | Y |  |  |
| 43 | VLR_DESP_ADV_X531 | NUMBER(17,2) | Y |  |  |
| 44 | DSC_NAT_REND | VARCHAR2(50) | Y |  |  |
| 45 | IND_ORIG_REC | VARCHAR2(1) | Y |  |  |
| 46 | VLR_N_RETIDO_IR | NUMBER(17,2) | Y |  |  |
| 47 | VLR_DEP_JUD_IR | NUMBER(17,2) | Y |  |  |
| 48 | VLR_COMP_ANO_CAL_IR | NUMBER(17,2) | Y |  |  |
| 49 | VLR_COMP_ANO_ANT_IR | NUMBER(17,2) | Y |  |  |
| 50 | VLR_REND_EXIG_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 51 | VLR_BASE_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 52 | VLR_BASE_SUSP_CSLL | NUMBER(17,2) | Y |  |  |
| 53 | VLR_N_CSLL | NUMBER(17,2) | Y |  |  |
| 54 | VLR_DEP_CSLL | NUMBER(17,2) | Y |  |  |
| 55 | VLR_BASE_SUSP_COFINS | NUMBER(17,2) | Y |  |  |
| 56 | VLR_N_COFINS | NUMBER(17,2) | Y |  |  |
| 57 | VLR_DEP_COFINS | NUMBER(17,2) | Y |  |  |
| 58 | VLR_BASE_SUSP_PIS_PASEP | NUMBER(17,2) | Y |  |  |
| 59 | VLR_N_PIS_PASEP | NUMBER(17,2) | Y |  |  |
| 60 | VLR_DEP_PIS_PASEP | NUMBER(17,2) | Y |  |  |
| 61 | CPF_CNPJ_ADV_X532 | VARCHAR2(14) | Y |  |  |
| 62 | VLR_DESP_ADV_X532 | NUMBER(17,2) | Y |  |  |
| 63 | NUM_SEQ_X534 | NUMBER(2) | Y |  |  |
| 64 | IND_TP_DEDUCAO_X534 | VARCHAR2(1) | Y |  |  |
| 65 | VLR_DED_EXIG_SUSP_X534 | NUMBER(17,2) | Y |  |  |
| 66 | CPF_DEP_X535 | VARCHAR2(11) | Y |  |  |
| 67 | VLR_DEPEN_SUSP_X535 | NUMBER(17,2) | Y |  |  |
| 68 | CPF_DEP_X536 | VARCHAR2(11) | Y |  |  |
| 69 | VLR_DEPEN_X536 | NUMBER(17,2) | Y |  |  |
| 70 | NUM_ORD_X53 | NUMBER(17) | Y |  |  |
| 71 | NUM_ORD_X531 | NUMBER(17) | Y |  |  |
| 72 | NUM_ORD_X532 | NUMBER(17) | Y |  |  |
| 73 | NUM_ORD_X534 | NUMBER(17) | Y |  |  |
| 74 | NUM_ORD_X535 | NUMBER(17) | Y |  |  |
| 75 | NUM_ORD_X536 | NUMBER(17) | Y |  |  |
| 76 | COD_NAT_REND | VARCHAR2(9) | Y |  |  |
| 77 | COD_SERVICO_NAT_REND | VARCHAR2(10) | Y |  |  |
| 78 | VLR_DESC_SIMPL_MENSAL | NUMBER(17,2) | Y |  |  |
| 79 | DATA_ESCR_CONT | DATE | Y |  |  |
| 80 | VLR_BASE | NUMBER(17,2) | Y |  |  |

**Indexes**:
- IX1_IRT_RETENCAO: (COD_EMPRESA, COD_ESTAB, COD_RETENCAO, VLR_ALIQ, DATA_PAGTO, USUARIO)
- IX2_IRT_RETENCAO: (COD_EMPRESA, COD_ESTAB, COD_RETENCAO, VLR_ALIQ, ANO_COMP, MES_COMP, USUARIO)
- IX3_IRT_RETENCAO: (COD_EMPRESA, USUARIO)

---

## IRT_RET_ESTAB_SM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_PROCESSO | NUMBER(12) | N |  |  |
| 4 | USUARIO | VARCHAR2(40) | N |  |  |

---

## IRT_RET_INSS_CED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 8 | SEQ_REGISTRO | NUMBER(3) | N |  |  |
| 9 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 10 | DAT_RECOLHIMENTO | DATE | Y |  |  |
| 11 | VLR_SALDO_PROX_MES | NUMBER(17,2) | Y |  |  |
| 12 | STATUS_GUIA | CHAR(1) | Y |  |  |
| 13 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 14 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 15 | IND_TP_FIS_JUR | CHAR(1) | Y |  |  |
| 16 | IND_FONTE_AVULSO | CHAR(1) | Y |  |  |
| 17 | DAT_EXTEMP | DATE | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | COD_CEI | VARCHAR2(12) | Y |  |  |
| 21 | VLR_OUTRAS_ENTID | NUMBER(17,2) | Y |  |  |
| 22 | DAT_FISCAL | DATE | Y |  |  |
| 23 | DAT_FISCAL_REAL | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, MES_COMPETENCIA, ANO_COMPETENCIA, SEQ_REGISTRO, DAT_FISCAL_REAL

---

## IRT_RET_INSS_DF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | Y |  |  |
| 7 | ANO_COMPETENCIA | NUMBER(4) | Y |  |  |
| 8 | DAT_FISCAL | DATE | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 12 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 13 | VLR_SERVICOS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 15 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 16 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 17 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 18 | IND_TP_FIS_JUR | CHAR(1) | Y |  |  |
| 19 | IND_FONTE_AVULSO | CHAR(1) | Y |  |  |
| 20 | DAT_EXTEMP | DATE | Y |  |  |
| 21 | USUARIO | VARCHAR2(40) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 24 | DAT_EMISSAO | DATE | Y |  |  |
| 25 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 26 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 27 | COD_CEI | VARCHAR2(12) | Y |  |  |
| 28 | IND_GFIP | CHAR(1) | Y |  |  |
| 29 | IND_LANCTO_GPS | CHAR(1) | Y |  |  |
| 30 | DAT_FATO_GERADOR | DATE | Y |  |  |
| 31 | VLR_OUTRAS_ENTID | NUMBER(17,2) | Y |  |  |
| 32 | IND_RET_EMISS_CPAG_CINDIVIDUAL | CHAR(1) | Y |  | Considerar retencoes para emissao do Comprovante de Pagamento a Contribuinte Individual |
| 33 | IDX_ITEM | NUMBER(2) | N | 1 | Indice para consideração de mais de uma base de ISS |
| 34 | MOVTO_E_S_DF | CHAR(1) | Y |  |  |
| 35 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 36 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 37 | NORM_DEV | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDX_ITEM

---

## IRT_SEFIP_PARAM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_VIG | DATE | N |  |  |
| 4 | DATA_FIM_VIG | DATE | N |  |  |
| 5 | COD_PAGTO | VARCHAR2(4) | Y |  |  |
| 6 | COD_FPAS | VARCHAR2(3) | Y |  |  |
| 7 | COD_OUT_ENTIDADE | VARCHAR2(4) | Y |  |  |
| 8 | ALIQ_RAT | NUMBER(3,2) | Y |  |  |
| 9 | PERC_ISENCAO_FILANT | NUMBER(5,2) | Y |  |  |
| 10 | IND_REGRA_RET_OCOR | CHAR(1) | Y | 'N' |  |
| 11 | VLR_LIM_MAX_CONTRIB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_MAX_CONTRIB_RET | NUMBER(17,2) | Y |  |  |
| 13 | ALIQ_MAX_RECOLH | NUMBER(7,4) | Y |  |  |
| 14 | IND_CENTR_EMPRESA | CHAR(1) | Y | 'N' |  |
| 15 | IND_BASE_REMUNERACAO | CHAR(1) | Y | 'I' |  |
| 16 | IND_CATEGORIA_TRAB | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI_VIG, DATA_FIM_VIG

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## IRT_SEFIP_PARAM_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_VIG | DATE | N |  |  |
| 4 | DATA_FIM_VIG | DATE | N |  |  |
| 5 | COD_PAGTO | VARCHAR2(4) | Y |  |  |
| 6 | COD_FPAS | VARCHAR2(3) | Y |  |  |
| 7 | COD_OUT_ENTIDADE | VARCHAR2(4) | Y |  |  |
| 8 | ALIQ_RAT | NUMBER(3,2) | Y |  |  |
| 9 | PERC_ISENCAO_FILANT | NUMBER(5,2) | Y |  |  |
| 10 | IND_REGRA_RET_OCOR | CHAR(1) | Y |  |  |
| 11 | VLR_LIM_MAX_CONTRIB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_MAX_CONTRIB_RET | NUMBER(17,2) | Y |  |  |
| 13 | ALIQ_MAX_RECOLH | NUMBER(7,4) | Y |  |  |
| 14 | IND_CENTR_EMPRESA | CHAR(1) | Y |  |  |
| 15 | IND_BASE_REMUNERACAO | CHAR(1) | Y |  |  |

---

