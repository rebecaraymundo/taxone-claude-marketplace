# Módulo: EFA (EFA) - 17 tabelas

## EFA_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_CARTA | VARCHAR2(12) | N |  |  |
| 2 | SEQ | NUMBER(6) | N |  |  |
| 3 | USUARIO | VARCHAR2(40) | N |  |  |
| 4 | QUANTIDADE | NUMBER(5) | Y |  |  |
| 5 | UNC | VARCHAR2(5) | Y |  |  |
| 6 | OCORRENCIA | VARCHAR2(40) | Y |  |  |
| 7 | VALOR | NUMBER(10,2) | Y |  |  |
| 8 | FATURADO | NUMBER(10,2) | Y |  |  |
| 9 | DIFERENCA | NUMBER(10,2) | Y |  |  |

**PK**: NUM_CARTA, SEQ, USUARIO

---

## EFA_CONTABILIZA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOC_FIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 12 | DATA_CONTABIL | DATE | N |  |  |
| 13 | HISTORICO | VARCHAR2(4) | N |  |  |
| 14 | TIPO_DOCUMENTO | VARCHAR2(3) | N |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 16 | REF_ORIGEM | VARCHAR2(20) | Y |  |  |
| 17 | REF_DESTINO | VARCHAR2(20) | Y |  |  |
| 18 | REF_OPERACAO | VARCHAR2(20) | Y |  |  |
| 19 | REF_PRODUTO | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOC_FIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, DATA_CONTABIL, HISTORICO, TIPO_DOCUMENTO, COD_PRODUTO

---

## EFA_EMISSAO_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 2 | NOTA | VARCHAR2(12) | N |  |  |
| 3 | USUARIO | VARCHAR2(40) | N |  |  |
| 4 | PROGRAMA | VARCHAR2(3) | N |  |  |
| 5 | SEQUENCIA | NUMBER(10) | N |  |  |
| 6 | DESCRICAO | VARCHAR2(300) | Y |  |  |
| 7 | UNIDADE | VARCHAR2(8) | Y |  |  |
| 8 | QUANTIDADE | NUMBER(13,3) | Y |  |  |
| 9 | PRECO_UNITARIO | NUMBER(13,2) | Y |  |  |
| 10 | COD_NBM | VARCHAR2(20) | Y |  |  |
| 11 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 12 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 13 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 15 | VLR_TOTAL | NUMBER(13,2) | Y |  |  |
| 16 | DESCONTO | NUMBER(8,4) | Y |  |  |
| 17 | COD_CFOP | VARCHAR2(4) | Y |  |  |
| 18 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 19 | DESTINACAO | NUMBER(1) | Y |  |  |
| 20 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 21 | REF_CONTABIL | VARCHAR2(20) | Y |  |  |
| 22 | CLASS_ICMS | CHAR(1) | Y |  |  |
| 23 | SUBST_TRIB_ENT | CHAR(1) | Y |  |  |
| 24 | IND_BEM_PATR | CHAR(1) | Y |  |  |
| 25 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 26 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 27 | NUM_ITEM | NUMBER(5) | N | 99999 |  |
| 28 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 29 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 30 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 31 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 32 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 33 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 34 | VLR_ITEM | VARCHAR2(17) | Y |  |  |
| 35 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 36 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 37 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 38 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 39 | IND_IPI_INCLUSO | CHAR(1) | Y |  |  |
| 40 | NUM_ROMANEIO | VARCHAR2(12) | Y |  |  |
| 41 | DATA_ROMANEIO | VARCHAR2(8) | Y |  |  |
| 42 | PESO_LIQUIDO | VARCHAR2(14) | Y |  |  |
| 43 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 44 | VLR_ITEM_CONVER | VARCHAR2(17) | Y |  |  |
| 45 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 46 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 47 | VLR_OUTRAS | VARCHAR2(17) | Y |  |  |
| 48 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 49 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 50 | DIF_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 51 | OBS_ICMS | VARCHAR2(45) | Y |  |  |
| 52 | COD_APUR_ICMS | VARCHAR2(5) | Y |  |  |
| 53 | VLR_ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 54 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 55 | OBS_IPI | VARCHAR2(45) | Y |  |  |
| 56 | COD_APUR_IPI | VARCHAR2(5) | Y |  |  |
| 57 | VLR_ALIQ_SUB_ICMS | VARCHAR2(7) | Y |  |  |
| 58 | VLR_SUBST_ICMS | VARCHAR2(17) | Y |  |  |
| 59 | OBS_SUBST_ICMS | VARCHAR2(45) | Y |  |  |
| 60 | COD_APUR_SUB_ICMS | VARCHAR2(5) | Y |  |  |
| 61 | TRIB_ICMS | CHAR(1) | Y |  |  |
| 62 | BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 63 | BASE_REDU_ICMS | VARCHAR2(17) | Y |  |  |
| 64 | TRIB_IPI | CHAR(1) | Y |  |  |
| 65 | BASE_IPI | VARCHAR2(17) | Y |  |  |
| 66 | BASE_REDU_IPI | VARCHAR2(17) | Y |  |  |
| 67 | BASE_SUB_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 68 | VLR_CONTAB_COMPL | VARCHAR2(17) | Y |  |  |
| 69 | VLR_ALIQ_DESTINO | VARCHAR2(7) | Y |  |  |
| 70 | VLR_OUTROS1 | VARCHAR2(17) | Y |  |  |
| 71 | VLR_OUTROS2 | VARCHAR2(17) | Y |  |  |
| 72 | VLR_OUTROS3 | VARCHAR2(17) | Y |  |  |
| 73 | VLR_OUTROS4 | VARCHAR2(17) | Y |  |  |
| 74 | VLR_OUTROS5 | VARCHAR2(17) | Y |  |  |
| 75 | VLR_ALIQ_OUTROS1 | VARCHAR2(7) | Y |  |  |
| 76 | VLR_ALIQ_OUTROS2 | VARCHAR2(7) | Y |  |  |
| 77 | VLR_CONTAB_ITEM | VARCHAR2(17) | Y |  |  |
| 78 | COD_OBS_VCONT_COMP | VARCHAR2(10) | Y |  |  |
| 79 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 80 | VLR_OUTROS_ICMS | VARCHAR2(17) | Y |  |  |
| 81 | VLR_OUTROS_IPI | VARCHAR2(17) | Y |  |  |
| 82 | NUM_ATO_CONCES | VARCHAR2(15) | Y |  |  |
| 83 | DAT_EMBARQUE | VARCHAR2(8) | Y |  |  |
| 84 | NUM_REG_EXP | VARCHAR2(12) | Y |  |  |
| 85 | NUM_DESP_EXP | VARCHAR2(11) | Y |  |  |
| 86 | VLR_TOM_SERVICO | VARCHAR2(17) | Y |  |  |
| 87 | VLR_DESP_MOEDA_EXP | VARCHAR2(17) | Y |  |  |
| 88 | COD_MOEDA_NEGOC | VARCHAR2(10) | Y |  |  |
| 89 | COD_PAIS_DEST_ORIG | VARCHAR2(3) | Y |  |  |
| 90 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 91 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 92 | VLR_ICMS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 93 | VLR_IPI_NDESTAC | VARCHAR2(17) | Y |  |  |
| 94 | TRIB_ICMS_AUX | CHAR(1) | Y |  |  |
| 95 | BASE_ICMS_AUX | VARCHAR2(17) | Y |  |  |
| 96 | TRIB_IPI_AUX | CHAR(1) | Y |  |  |
| 97 | BASE_IPI_AUX | VARCHAR2(17) | Y |  |  |
| 98 | COD_PROJETO | VARCHAR2(10) | Y |  |  |
| 99 | UNIDADE_NEGOCIO | VARCHAR2(20) | Y |  |  |
| 100 | TIPO_SERVICO | VARCHAR2(4) | Y |  |  |
| 101 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 102 | VLR_PRECO_SUGER | NUMBER(17,2) | Y |  |  |
| 103 | TAB_SUBST_TRIB | VARCHAR2(5) | Y |  |  |
| 104 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 105 | IDENT_FEDERAL | NUMBER(12) | Y |  |  |
| 106 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 107 | COD_AMPARO_LEGALST | VARCHAR2(10) | Y |  |  |
| 108 | IND_MOV_FIS | CHAR(1) | Y |  |  |

**PK**: COD_PRODUTO, NOTA, USUARIO, PROGRAMA, SEQUENCIA, NUM_ITEM

**FKs**:
- IDENT_FEDERAL → X2044_SIT_TRIB_FED(IDENT_FEDERAL)

---

## EFA_IMP_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_NOTA | VARCHAR2(12) | N |  |  |
| 4 | SERIE_NOTA | VARCHAR2(3) | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | PROGRAMA | VARCHAR2(3) | N |  |  |
| 7 | USUARIO | VARCHAR2(40) | N |  |  |
| 8 | SUB_SERIE_NOTA | VARCHAR2(2) | Y |  |  |
| 9 | DATA_EMISSAO | DATE | Y |  |  |
| 10 | CONVENIO | VARCHAR2(14) | Y |  |  |
| 11 | DESC_CLI | VARCHAR2(70) | Y |  |  |
| 12 | ENDERECO_CLI | VARCHAR2(50) | Y |  |  |
| 13 | CGC_CLI | VARCHAR2(18) | Y |  |  |
| 14 | INSC_ESTADUAL_CLI | VARCHAR2(14) | Y |  |  |
| 15 | BAIRRO_CLI | VARCHAR2(25) | Y |  |  |
| 16 | CIDADE_CLI | VARCHAR2(30) | Y |  |  |
| 17 | ESTADO_CLI | VARCHAR2(2) | Y |  |  |
| 18 | CEP_CLI | VARCHAR2(10) | Y |  |  |
| 19 | TELEFONE_CLI | VARCHAR2(14) | Y |  |  |
| 20 | DESC_TRANSP | VARCHAR2(70) | Y |  |  |
| 21 | CGC_TRANSP | VARCHAR2(18) | Y |  |  |
| 22 | ENDERECO_TRANSP | VARCHAR2(50) | Y |  |  |
| 23 | CIDADE_TRANSP | VARCHAR2(30) | Y |  |  |
| 24 | EMITENTE_DESTINATARIO | VARCHAR2(1) | Y |  |  |
| 25 | ESTADO_TRANSP | VARCHAR2(2) | Y |  |  |
| 26 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 27 | PESO_BRUTO_TOTAL | NUMBER(13,3) | Y |  |  |
| 28 | PESO_LIQUIDO_TOTAL | NUMBER(13,3) | Y |  |  |
| 29 | BASE_ICMS | NUMBER(13,2) | Y |  |  |
| 30 | VALOR_ICMS | NUMBER(13,2) | Y |  |  |
| 31 | BASE_ICMS_SUBST | NUMBER(13,2) | Y |  |  |
| 32 | VALOR_ICMS_SUBST | NUMBER(13,2) | Y |  |  |
| 33 | VALOR_TOTAL_ITENS | NUMBER(13,2) | Y |  |  |
| 34 | VALOR_FRETE | NUMBER(13,2) | Y |  |  |
| 35 | VALOR_SEGURO | NUMBER(13,2) | Y |  |  |
| 36 | VALOR_OUTROS | NUMBER(13,2) | Y |  |  |
| 37 | VALOR_IPI_TOTAL | NUMBER(13,2) | Y |  |  |
| 38 | VALOR_TOTAL_NOTA | NUMBER(13,2) | Y |  |  |
| 39 | TEXTO_LEGAL | VARCHAR2(300) | Y |  |  |
| 40 | TEXTO_LEGAL_FAT | VARCHAR2(120) | Y |  |  |
| 41 | TEXTO_LEGAL_CATEGORIA | VARCHAR2(120) | Y |  |  |
| 42 | QUANTIDADE | NUMBER(13,3) | Y |  |  |
| 43 | ESPECIE | VARCHAR2(15) | Y |  |  |
| 44 | LOJA | VARCHAR2(10) | Y |  |  |
| 45 | DEPARTAMENTO | VARCHAR2(5) | Y |  |  |
| 46 | CFOP | VARCHAR2(6) | Y |  |  |
| 47 | NAT_OP | VARCHAR2(3) | Y |  |  |
| 48 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 49 | IMPRESSO | VARCHAR2(1) | Y |  |  |
| 50 | VLR_ICMS_DEST | VARCHAR2(40) | Y |  |  |
| 51 | BS_ICMS_DEST | VARCHAR2(40) | Y |  |  |
| 52 | VLR_ICMS_DEDUZIDO | VARCHAR2(40) | Y |  |  |
| 53 | VLR_ICMSS_TXT | VARCHAR2(40) | Y |  |  |
| 54 | BS_ICMSS_TXT | VARCHAR2(40) | Y |  |  |
| 55 | EXTERIOR_TXT | VARCHAR2(60) | Y |  |  |
| 56 | VOLUME | NUMBER(13,3) | Y |  |  |
| 57 | COD_CFOP | VARCHAR2(6) | Y |  |  |
| 58 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 59 | DATA_VENCIMENTO | DATE | Y |  |  |
| 60 | ALIQ_ISS | NUMBER(8,4) | Y |  |  |
| 61 | VALOR_ISS | NUMBER(17,2) | Y |  |  |
| 62 | ALIQ_INSS | NUMBER(8,4) | Y |  |  |
| 63 | VALOR_INSS | NUMBER(17,2) | Y |  |  |
| 64 | ALIQ_IR | NUMBER(8,4) | Y |  |  |
| 65 | VALOR_IR | NUMBER(17,2) | Y |  |  |
| 66 | INSC_MUNICIPAL_CLI | VARCHAR2(14) | Y |  |  |
| 67 | COD_NAT_SERVICO | VARCHAR2(10) | Y |  |  |
| 68 | DESCR_NAT_SERVICO | VARCHAR2(30) | Y |  |  |
| 69 | IND_SERV_MERC | CHAR(1) | Y |  |  |
| 70 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 71 | NUM_VIA | NUMBER(5) | Y |  |  |
| 72 | OBS_NF | VARCHAR2(250) | Y |  |  |
| 73 | DESC_ENTREGA | VARCHAR2(70) | Y |  |  |
| 74 | ENDERECO_ENTREGA | VARCHAR2(70) | Y |  |  |
| 75 | CGC_ENTREGA | VARCHAR2(18) | Y |  |  |
| 76 | BAIRRO_ENTREGA | VARCHAR2(25) | Y |  |  |
| 77 | CIDADE_ENTREGA | VARCHAR2(30) | Y |  |  |
| 78 | ESTADO_ENTREGA | VARCHAR2(2) | Y |  |  |
| 79 | CEP_ENTREGA | VARCHAR2(10) | Y |  |  |
| 80 | TELEFONE_ENTREGA | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_NOTA, SERIE_NOTA, MOVTO_E_S, PROGRAMA, USUARIO

---

## EFA_IMP_DOCFIS_IT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_NOTA | VARCHAR2(12) | N |  |  |
| 4 | SERIE_NOTA | VARCHAR2(3) | N |  |  |
| 5 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 6 | PROGRAMA | VARCHAR2(3) | N |  |  |
| 7 | USUARIO | VARCHAR2(40) | N |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 9 | DESCRICAO | VARCHAR2(300) | Y |  |  |
| 10 | SUB_SERIE_NOTA | VARCHAR2(2) | Y |  |  |
| 11 | QUANTIDADE | NUMBER(13,3) | Y |  |  |
| 12 | COD_FISCAL | VARCHAR2(6) | Y |  |  |
| 13 | PRECO | NUMBER(13,4) | Y |  |  |
| 14 | VALOR_MERC | NUMBER(13,2) | Y |  |  |
| 15 | PERC_IPI | NUMBER(13,2) | Y |  |  |
| 16 | VALOR_IPI | NUMBER(13,2) | Y |  |  |
| 17 | CLASS_FISCAL | VARCHAR2(10) | Y |  |  |
| 18 | UN_VENDA | VARCHAR2(3) | Y |  |  |
| 19 | VALOR_TOTAL | NUMBER(13,2) | Y |  |  |
| 20 | CLASS_IPI | VARCHAR2(1) | Y |  |  |
| 21 | ALIQ_IPI | NUMBER(8,4) | Y |  |  |
| 22 | CLASS_ICMS | VARCHAR2(1) | Y |  |  |
| 23 | ALIQ_ICMS | NUMBER(8,4) | Y |  |  |
| 24 | ICMS_ESPECIAL | NUMBER(8,4) | Y |  |  |
| 25 | ALIQ_INTERNA_ICMS | NUMBER(8,4) | Y |  |  |
| 26 | CLASS_ISS | VARCHAR2(1) | Y |  |  |
| 27 | ALIQ_ISS | NUMBER(8,4) | Y |  |  |
| 28 | VLR_BASE_ISS | NUMBER(13,2) | Y |  |  |
| 29 | PESO_LIQ | NUMBER(13,2) | Y |  |  |
| 30 | PESO_BRUTO | NUMBER(13,2) | Y |  |  |
| 31 | CUBAGEM | NUMBER(13,2) | Y |  |  |
| 32 | SUBST_TRIBUTACAO | VARCHAR2(6) | Y |  |  |
| 33 | ORIGEM | VARCHAR2(1) | Y |  |  |
| 34 | MARGEM | NUMBER(5,2) | Y |  |  |
| 35 | TIPO_BASE | VARCHAR2(1) | Y |  |  |
| 36 | TIPO_CALCULO | VARCHAR2(1) | Y |  |  |
| 37 | COD_SITUACAO_A | VARCHAR2(1) | Y |  |  |
| 38 | PRECO_SUGERIDO | NUMBER(13,2) | Y |  |  |
| 39 | CUSTO_MEDIO | NUMBER(13,2) | Y |  |  |
| 40 | PRECO_ULT_ENTRADA | NUMBER(13,2) | Y |  |  |
| 41 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 42 | STATUS | VARCHAR2(1) | Y |  |  |
| 43 | IMPRESSO | VARCHAR2(1) | Y |  |  |
| 44 | BS_ICMS_TXT | VARCHAR2(15) | Y |  |  |
| 45 | ICMS_ENT | NUMBER(13,2) | Y |  |  |
| 46 | ICMSS_ENT | NUMBER(13,2) | Y |  |  |
| 47 | REDUCAO_ICMS | NUMBER(13,2) | Y |  |  |
| 48 | BS_IPI_TXT | VARCHAR2(15) | Y |  |  |
| 49 | PV_TXT | VARCHAR2(15) | Y |  |  |
| 50 | DESCONTO | NUMBER(13,2) | Y |  |  |
| 51 | UN_TRANSPORTE | VARCHAR2(3) | Y |  |  |
| 52 | VOL_CONVER | NUMBER(13,3) | Y |  |  |
| 53 | COD_PROJETO | VARCHAR2(10) | Y |  |  |
| 54 | UNIDADE_NEGOCIO | VARCHAR2(20) | Y |  |  |
| 55 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 56 | COD_CFOP | VARCHAR2(6) | Y |  |  |
| 57 | COD_CONTABIL | VARCHAR2(20) | Y |  |  |
| 58 | PRODUTO_X08 | VARCHAR2(20) | Y |  |  |
| 59 | DESCRICAO2 | VARCHAR2(50) | Y |  |  |
| 60 | TIPO_SERVICO | VARCHAR2(4) | Y |  |  |
| 61 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 62 | IND_IMPRIME_VLR | CHAR(1) | Y |  |  |
| 63 | IND_SERV_MERC | CHAR(1) | Y |  |  |
| 64 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 65 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 66 | NUM_ITEM | NUMBER(5) | N | 99999 |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_NOTA, SERIE_NOTA, MOVTO_E_S, PROGRAMA, USUARIO, COD_PRODUTO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, NUM_NOTA, SERIE_NOTA, MOVTO_E_S, PROGRAMA, USUARIO → EFA_IMP_DOCFIS(COD_EMPRESA, COD_ESTAB, NUM_NOTA, SERIE_NOTA, MOVTO_E_S, PROGRAMA, USUARIO)

---

## EFA_ITEM_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 13 | IND_PRODUTO | CHAR(1) | N |  |  |
| 14 | NUM_ITEM | NUMBER(5) | N |  |  |
| 15 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 16 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 17 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 18 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 19 | DESCRICAO_COMPL | VARCHAR2(300) | Y |  |  |
| 20 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 21 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 22 | QUANTIDADE | NUMBER(17,3) | Y |  |  |
| 23 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 24 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 25 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 27 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 28 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 29 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 30 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 31 | IND_IPI_INCLUSO | CHAR(1) | Y |  |  |
| 32 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 33 | VLR_ITEM_CONVER | NUMBER(17,2) | Y |  |  |
| 34 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 35 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 36 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 37 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 38 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 39 | DIF_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 40 | OBS_ICMS | VARCHAR2(45) | Y |  |  |
| 41 | COD_APUR_ICMS | VARCHAR2(5) | Y |  |  |
| 42 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 43 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 44 | OBS_IPI | VARCHAR2(45) | Y |  |  |
| 45 | COD_APUR_IPI | VARCHAR2(5) | Y |  |  |
| 46 | VLR_ALIQ_SUB_ICMS | NUMBER(7,4) | Y |  |  |
| 47 | VLR_SUBST_ICMS | NUMBER(17,2) | Y |  |  |
| 48 | OBS_SUBST_ICMS | VARCHAR2(45) | Y |  |  |
| 49 | COD_APUR_SUB_ICMS | VARCHAR2(5) | Y |  |  |
| 50 | TRIB_ICMS | CHAR(1) | Y |  |  |
| 51 | BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 52 | BASE_REDU_ICMS | NUMBER(17,2) | Y |  |  |
| 53 | TRIB_IPI | CHAR(1) | Y |  |  |
| 54 | BASE_IPI | NUMBER(17,2) | Y |  |  |
| 55 | BASE_REDU_IPI | NUMBER(17,2) | Y |  |  |
| 56 | BASE_SUB_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 57 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 58 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 59 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 60 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 61 | VLR_OUTROS3 | NUMBER(17,2) | Y |  |  |
| 62 | VLR_OUTROS4 | NUMBER(17,2) | Y |  |  |
| 63 | VLR_OUTROS5 | NUMBER(17,2) | Y |  |  |
| 64 | VLR_ALIQ_OUTROS1 | NUMBER(7,4) | Y |  |  |
| 65 | VLR_ALIQ_OUTROS2 | NUMBER(7,4) | Y |  |  |
| 66 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 67 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  |  |
| 68 | VLR_OUTROS_IPI | NUMBER(17,2) | Y |  |  |
| 69 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 70 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 71 | TRIB_ICMS_AUX | CHAR(1) | Y |  |  |
| 72 | BASE_ICMS_AUX | NUMBER(17,2) | Y |  |  |
| 73 | TRIB_IPI_AUX | CHAR(1) | Y |  |  |
| 74 | BASE_IPI_AUX | NUMBER(17,2) | Y |  |  |
| 75 | BS_ICMS_TXT | VARCHAR2(15) | Y |  |  |
| 76 | BS_IPI_TXT | VARCHAR2(15) | Y |  |  |
| 77 | PV_TXT | VARCHAR2(15) | Y |  |  |
| 78 | VOL_CONVER | NUMBER(17,3) | Y |  |  |
| 79 | COD_PROJETO | VARCHAR2(10) | Y |  |  |
| 80 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 81 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 82 | ALIQ_ICMS_NDESTAC | NUMBER(7,4) | Y |  |  |
| 83 | ALIQ_IPI_NDESTAC | NUMBER(7,4) | Y |  |  |
| 84 | IND_ITEM_CAD | CHAR(1) | Y |  |  |
| 85 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 86 | TEXTO_LEGAL_IPI | VARCHAR2(120) | Y |  |  |
| 87 | TEXTO_LEGAL_CATEG | VARCHAR2(120) | Y |  |  |
| 88 | IDENT_FEDERAL | NUMBER(12) | Y |  |  |
| 89 | TRIB_SUBST_ICMS | CHAR(1) | Y |  |  |
| 90 | BASE_REDU_ICMSS | NUMBER(17,2) | Y |  |  |
| 91 | TEXTO_LEGAL_ST | VARCHAR2(120) | Y |  |  |
| 92 | COD_DCR | VARCHAR2(15) | Y |  |  |
| 93 | IND_MOV_FIS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_FIS_JUR, IND_FIS_JUR, COD_DOCTO, COD_PRODUTO, IND_PRODUTO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_FIS_JUR, IND_FIS_JUR, COD_DOCTO, COD_PRODUTO, IND_PRODUTO, NUM_ITEM → EFT_ITEM(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_FIS_JUR, IND_FIS_JUR, COD_DOCTO, COD_PRODUTO, IND_PRODUTO, NUM_ITEM)

---

## EFA_ITEM_RPA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | USUARIO | VARCHAR2(40) | N |  |  |
| 13 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 14 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 15 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 17 | DATA_VENCTO | DATE | Y |  |  |
| 18 | VLR_PENSAO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 21 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQ_IRRF | NUMBER(7,4) | Y |  |  |
| 24 | VLR_IRRF | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_IRRF | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 27 | VLR_INSS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, USUARIO, COD_SERVICO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFA_ITEM_RPA_CALC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 13 | USUARIO | VARCHAR2(40) | N |  |  |
| 14 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 15 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 17 | DATA_VENCTO | DATE | Y |  |  |
| 18 | VLR_PENSAO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_IRRF | NUMBER(17,2) | Y |  |  |
| 21 | ALIQ_IRRF | NUMBER(7,4) | Y |  |  |
| 22 | VLR_IRRF | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 24 | ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 25 | VLR_INSS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_LIQUIDO | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 28 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 29 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, COD_SERVICO, USUARIO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, USUARIO → EFA_RPA_CALC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUBSERIE_DOCFIS, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, USUARIO)

---

## EFA_ITENS_RF_CPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 2 | NOTA | VARCHAR2(12) | N |  |  |
| 3 | USUARIO | VARCHAR2(40) | N |  |  |
| 4 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 5 | COD_TRIBUTACAO | NUMBER(1) | N |  |  |
| 6 | SEQUENCIA | NUMBER(10) | N |  |  |
| 7 | PROGRAMA | VARCHAR2(3) | Y |  |  |
| 8 | BASE | NUMBER(13,2) | Y |  |  |
| 9 | ALIQUOTA | NUMBER(8,4) | Y |  |  |
| 10 | VALOR | NUMBER(13,2) | Y |  |  |
| 11 | OBSERVACAO | VARCHAR2(300) | Y |  |  |

**PK**: COD_PRODUTO, NOTA, USUARIO, COD_TRIBUTO, COD_TRIBUTACAO, SEQUENCIA

---

## EFA_PESSOA_FIS_JUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 5 | IND_APOSENTADO | CHAR(1) | Y |  |  |
| 6 | NUM_DEP | NUMBER(2) | Y |  |  |
| 7 | NUM_RG | VARCHAR2(15) | Y |  |  |
| 8 | ORGAO_RG | VARCHAR2(5) | Y |  |  |
| 9 | VALID_RG | DATE | Y |  |  |
| 10 | INSC_INSS | VARCHAR2(14) | Y |  |  |
| 11 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 12 | VLR_SAL_CONTRIB | NUMBER(17,2) | Y |  |  |
| 13 | IND_TP_PRESTADOR | CHAR(1) | Y |  |  |
| 14 | VLR_CONTRIB_SIND | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_FIS_JUR, COD_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFA_RELAT_FISCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 5 | SUBSERIE_DOCFIS | VARCHAR2(1) | N |  |  |
| 6 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 7 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 8 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 9 | COD_TRIBUTACAO | VARCHAR2(1) | N |  |  |
| 10 | DATA_FISCAL | DATE | N |  |  |
| 11 | ALIQ_TRIBUTO | NUMBER(8,4) | N |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 13 | USUARIO | VARCHAR2(40) | N |  |  |
| 14 | BASE_TRIBUTO | NUMBER(13,2) | Y |  |  |
| 15 | VLR_TRIBUTO | NUMBER(13,2) | Y |  |  |
| 16 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 17 | VLR_ICMS_TRIB | NUMBER(13,2) | Y |  |  |
| 18 | VLR_IPI | NUMBER(13,2) | Y |  |  |
| 19 | VLR_ICMS_OUTRAS | NUMBER(13,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, SUBSERIE_DOCFIS, MOVTO_E_S, NORM_DEV, COD_TRIBUTO, COD_TRIBUTACAO, DATA_FISCAL, ALIQ_TRIBUTO, IDENT_FIS_JUR, USUARIO

**Indexes**:
- IN_EFA_RELAT_FISCAL: (USUARIO)

---

## EFA_RELAT_LANCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | TIPO_DOCUMENTO | VARCHAR2(2) | N |  |  |
| 4 | REF_ORIGEM | VARCHAR2(20) | N |  |  |
| 5 | REF_DESTINO | VARCHAR2(20) | N |  |  |
| 6 | REF_OPERACAO | VARCHAR2(20) | N |  |  |
| 7 | REF_PRODUTO | VARCHAR2(20) | N |  |  |
| 8 | NUM_COLUNA | NUMBER(3) | N |  |  |
| 9 | NUM_LANCTO | NUMBER(2) | N |  |  |
| 10 | LINHA | NUMBER(2) | N |  |  |
| 11 | REF_PRAZO | VARCHAR2(20) | Y |  |  |
| 12 | CONTA_CONTABIL | VARCHAR2(20) | Y |  |  |
| 13 | DESCRICAO | VARCHAR2(40) | Y |  |  |
| 14 | DSC_CONTA_CONTABIL | VARCHAR2(50) | Y |  |  |
| 15 | SINAL | VARCHAR2(1) | Y |  |  |
| 16 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 17 | COD_CONTABIL_OR | VARCHAR2(40) | Y |  |  |
| 18 | COD_CONTAB_DEST | VARCHAR2(40) | Y |  |  |
| 19 | COD_CONTAB_OPER | VARCHAR2(40) | Y |  |  |
| 20 | COD_CONTAB_PROD | VARCHAR2(40) | Y |  |  |
| 21 | COD_CONTAB_PRAZO | VARCHAR2(40) | Y |  |  |
| 22 | CAMPO | NUMBER(3) | Y |  |  |
| 23 | TEXTO | VARCHAR2(100) | Y |  |  |
| 24 | ORIGEM_CONTA | VARCHAR2(1) | Y |  |  |
| 25 | ORIGEM_CENT_CUSTO | VARCHAR2(1) | Y |  |  |
| 26 | DSC_CAMPO | VARCHAR2(40) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, TIPO_DOCUMENTO, REF_ORIGEM, REF_DESTINO, REF_OPERACAO, REF_PRODUTO, NUM_COLUNA, NUM_LANCTO, LINHA

---

## EFA_RELAT_SRF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_DOCFIS | VARCHAR2(6) | N |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | COD_PRODUTO | VARCHAR2(14) | N |  |  |
| 7 | USUARIO | VARCHAR2(40) | N |  |  |
| 8 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 9 | QUANTIDADE | NUMBER(15,3) | Y |  |  |
| 10 | VALOR_ITEM | NUMBER(13,2) | Y |  |  |
| 11 | CODIGO_DCR | VARCHAR2(15) | Y |  |  |
| 12 | COD_TRANSPORTADORA | VARCHAR2(14) | Y |  |  |
| 13 | DESC_TRANSPORTADORA | VARCHAR2(50) | Y |  |  |
| 14 | VOLUME | NUMBER(15,3) | Y |  |  |
| 15 | REPRESENTANTE | VARCHAR2(80) | Y |  |  |
| 16 | NUM_RELACAO | NUMBER(6) | Y |  |  |
| 17 | ANO_RELACAO | NUMBER(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, DATA_FISCAL, COD_PRODUTO, USUARIO

---

## EFA_RETIFICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | SEQ | NUMBER(2) | N |  |  |
| 2 | NUM_NOTIFICA | VARCHAR2(12) | N |  |  |
| 3 | PROGRAMA | VARCHAR2(5) | N |  |  |
| 4 | USUARIO | VARCHAR2(40) | N |  |  |
| 5 | CODIGO | NUMBER(2) | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(60) | Y |  |  |
| 7 | RETIFICACAO | VARCHAR2(60) | Y |  |  |

**PK**: SEQ, NUM_NOTIFICA, PROGRAMA, USUARIO

---

## EFA_RPA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | USUARIO | VARCHAR2(40) | N |  |  |
| 13 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 14 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 15 | DATA_EMISSAO | DATE | Y |  |  |
| 16 | COD_CLASS_CONTABIL | VARCHAR2(10) | Y |  |  |
| 17 | NUM_DEP | NUMBER(2) | Y |  |  |
| 18 | IND_APOSENTADO | CHAR(1) | Y |  |  |
| 19 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 20 | OBSERVACAO | VARCHAR2(250) | Y |  |  |
| 21 | DATA_PAGAMENTO | DATE | Y |  |  |
| 22 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 23 | VLR_SAL_CONTRIB | NUMBER(17,2) | Y |  |  |
| 24 | IND_TP_PRESTADOR | CHAR(1) | Y |  |  |
| 25 | IND_CALC_ISS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, USUARIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## EFA_RPA_CALC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUBSERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | N |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 12 | USUARIO | VARCHAR2(40) | N |  |  |
| 13 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 14 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 15 | DATA_EMISSAO | DATE | Y |  |  |
| 16 | COD_CLASS_CONTABIL | VARCHAR2(10) | Y |  |  |
| 17 | VLR_DESC_DEP | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DESC_APOS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 20 | OBSERVACAO | VARCHAR2(250) | Y |  |  |
| 21 | DATA_PAGAMENTO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, SUBSERIE_DOCFIS, COD_DOCTO, IND_FIS_JUR, COD_FIS_JUR, USUARIO

---

## EFA_TP_TRANSAC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_TRANSACAO | VARCHAR2(5) | N |  |  |
| 2 | USUARIO | VARCHAR2(40) | N |  |  |

**PK**: TIPO_TRANSACAO, USUARIO

---

