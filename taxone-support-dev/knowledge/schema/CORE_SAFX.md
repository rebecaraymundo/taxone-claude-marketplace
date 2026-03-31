# Módulo: SAFX (Interface/Staging) - 451 tabelas

## SAFX01

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 4 | CONTA_DEB_CRED | VARCHAR2(70) | Y |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 7 | VLR_LANCTO | VARCHAR2(19) | Y |  |  |
| 8 | CONTRA_PART | VARCHAR2(70) | Y |  |  |
| 9 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 10 | CENTRO_DESPESA | VARCHAR2(20) | Y |  |  |
| 11 | HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 12 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 13 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 14 | COD_INDICE_CONV | VARCHAR2(10) | Y |  |  |
| 15 | VLR_OPER_IND | VARCHAR2(20) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 18 | TIPO_LANCTO | CHAR(1) | Y |  | N - Normal; E - Encerramento |
| 19 | IND_PFJ_EMPRESA | CHAR(1) | Y |  |  |
| 20 | COD_PFJ_EMPRESA | VARCHAR2(14) | Y |  |  |
| 21 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 22 | IDENTIF_LANC_RES | VARCHAR2(128) | Y |  |  |
| 23 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 24 | IDENTIF_SALDO | VARCHAR2(128) | Y |  |  |
| 25 | DSC_RESERVADO1 | VARCHAR2(19) | Y |  |  |
| 26 | DSC_RESERVADO2 | VARCHAR2(19) | Y |  |  |
| 27 | DSC_RESERVADO3 | VARCHAR2(19) | Y |  |  |
| 28 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 29 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 30 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 31 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 32 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 34 | DAT_LANCTO_EXTEMP | VARCHAR2(8) | Y |  |  |
| 35 | PST_ID | NUMBER | Y |  |  |
| 36 | COD_EVENTO_DESIF | VARCHAR2(3) | Y |  |  |
| 37 | COD_ESTADO_ORIG | VARCHAR2(2) | Y |  |  |
| 38 | COD_MUNIC_ORIG | VARCHAR2(5) | Y |  |  |
| 39 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 40 | CHAVE_SAFX01 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX01: (CHAVE_SAFX01)
- IX_SAFX01: (DAT_GRAVACAO)
- IX_SAFX01_1: (COD_EMPRESA, COD_ESTAB, DATA_OPERACAO, NUM_PROCESSO, NUM_LOTE)
- IX_SAFX01_LOTE: (NUM_LOTE)

---

## SAFX02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | DATA_SALDO | VARCHAR2(8) | Y |  |  |
| 5 | VLR_SALDO_INI | VARCHAR2(19) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | VARCHAR2(19) | Y |  |  |
| 8 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 9 | VLR_TOT_CRE | VARCHAR2(19) | Y |  |  |
| 10 | VLR_TOT_DEB | VARCHAR2(19) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | IDENTIF_SALDO | VARCHAR2(128) | Y |  |  |
| 13 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX02 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX02: (CHAVE_SAFX02)
- IX_SAFX02: (DAT_GRAVACAO)
- IX_SAFX02_LOTE: (NUM_LOTE)

---

## SAFX03

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 12 | DATA_VENCTO | VARCHAR2(8) | Y |  |  |
| 13 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 14 | VLR_MOVTO | VARCHAR2(17) | Y |  |  |
| 15 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 16 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 17 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 18 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 19 | VLR_MOVTO_CONV | VARCHAR2(18) | Y |  |  |
| 20 | VLR_TOT_DOCTO | VARCHAR2(17) | Y |  |  |
| 21 | NUM_DOC_COMPENS | VARCHAR2(15) | Y |  |  |
| 22 | COD_CENTRO_RESP | VARCHAR2(20) | Y |  |  |
| 23 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 24 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 25 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 26 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 27 | DATA_FATOR_GERADOR | VARCHAR2(8) | Y |  |  |
| 28 | DATA_INI_COMPET | VARCHAR2(8) | Y |  |  |
| 29 | DATA_FIM_COMPET | VARCHAR2(8) | Y |  |  |
| 30 | VLR_BRUTO | VARCHAR2(17) | Y |  |  |
| 31 | VLR_DEDUCAO | VARCHAR2(17) | Y |  |  |
| 32 | ALIQ_TRIBUTO | VARCHAR2(7) | Y |  |  |
| 33 | DAT_GRAVACAO | DATE | Y |  |  |
| 34 | HISTORICO | VARCHAR2(50) | Y |  |  |
| 35 | IND_TIPO_TITULO | VARCHAR2(2) | Y |  |  |
| 36 | DSC_COMPL_TITULO | VARCHAR2(50) | Y |  |  |
| 37 | QTDE_PARCELA | VARCHAR2(3) | Y |  |  |
| 38 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 39 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 40 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 41 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 42 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 43 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 44 | VLR_RET | VARCHAR2(17) | Y |  |  |
| 45 | VLR_N_RET | VARCHAR2(17) | Y |  |  |
| 46 | PST_ID | NUMBER | Y |  |  |
| 47 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 48 | CHAVE_SAFX03 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX03: (CHAVE_SAFX03)
- IX_SAFX03: (DAT_GRAVACAO)
- IX_SAFX03_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX03_LOTE: (NUM_LOTE)

---

## SAFX04

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 2 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 3 | DATA_X04 | VARCHAR2(8) | Y |  |  |
| 4 | IND_CONTEM_COD | CHAR(1) | Y |  |  |
| 5 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 6 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 7 | COD_ATIVIDADE | VARCHAR2(7) | Y |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 9 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 10 | INSC_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 11 | NOME_FANTASIA | VARCHAR2(50) | Y |  |  |
| 12 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 13 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 14 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 15 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 16 | CIDADE | VARCHAR2(30) | Y |  |  |
| 17 | DISTRITO | VARCHAR2(20) | Y |  |  |
| 18 | SUB_DISTRITO | VARCHAR2(20) | Y |  |  |
| 19 | UF | VARCHAR2(2) | Y |  |  |
| 20 | CEP | VARCHAR2(8) | Y |  |  |
| 21 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 22 | DDD | VARCHAR2(5) | Y |  |  |
| 23 | TELEFONE | VARCHAR2(10) | Y |  |  |
| 24 | FAX | VARCHAR2(10) | Y |  |  |
| 25 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 26 | IND_CLASSE_PFJ | VARCHAR2(2) | Y |  |  |
| 27 | IND_CLASSE_EMP | VARCHAR2(2) | Y |  |  |
| 28 | IND_PFJ_CONTRIB | CHAR(1) | Y |  |  |
| 29 | DAT_GRAVACAO | DATE | Y |  |  |
| 30 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 31 | CEI | VARCHAR2(15) | Y |  |  |
| 32 | IND_CLIENTE_SID | CHAR(1) | Y |  |  |
| 33 | CPF_CNPJ_INV | VARCHAR2(14) | Y |  |  |
| 34 | IND_SCP | CHAR(1) | Y |  |  |
| 35 | COD_CBO | VARCHAR2(10) | Y |  |  |
| 36 | PIS_PASEP | VARCHAR2(11) | Y |  |  |
| 37 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  |  |
| 38 | OCORRENCIA_TRAB | VARCHAR2(2) | Y |  |  |
| 39 | CX_POSTAL | VARCHAR2(20) | Y |  |  |
| 40 | NUM_CEP_CX_POSTAL | VARCHAR2(8) | Y |  |  |
| 41 | E_MAIL | VARCHAR2(60) | Y |  |  |
| 42 | IND_FOME_ZERO | CHAR(1) | Y |  |  |
| 43 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 44 | TP_LOGRADOURO | VARCHAR2(10) | Y |  | Campo criado para atender a DIM São Luis. |
| 45 | IND_SIMPLES_NAC | CHAR(1) | Y |  | Campo criado para atender a DIM São Luis. |
| 46 | TP_BAIRRO | VARCHAR2(10) | Y |  |  |
| 47 | DATA_NASC_AUTONOMO | VARCHAR2(8) | Y |  |  |
| 48 | IMP_RENDA_DEPEND | VARCHAR2(2) | Y |  |  |
| 49 | SAL_FAMILIA_DEPEND | VARCHAR2(2) | Y |  |  |
| 50 | COD_FUNCAO_AUTONOMO | VARCHAR2(10) | Y |  |  |
| 51 | IND_INCENTIVO_CULTURAL | CHAR(1) | Y |  |  |
| 52 | IND_CLIENTE_LIVRE | CHAR(1) | Y |  |  |
| 53 | PASSAPORTE | VARCHAR2(20) | Y |  |  |
| 54 | DATA_MOLESTIA | VARCHAR2(8) | Y |  |  |
| 55 | NUM_ID_FISCAL | VARCHAR2(30) | Y |  |  |
| 56 | TP_FONTE_PAGADORA | VARCHAR2(3) | Y |  |  |
| 57 | DSC_PROVINCIA_EX | VARCHAR2(40) | Y |  |  |
| 58 | NUM_ALVARA | VARCHAR2(11) | Y |  |  |
| 59 | COD_INSTAL_ANP | VARCHAR2(7) | Y |  |  |
| 60 | NUM_CR | VARCHAR2(10) | Y |  |  |
| 61 | IND_IDENTIF_FISCAL | CHAR(1) | Y |  |  |
| 62 | NUM_CAEPF | VARCHAR2(15) | Y |  |  |
| 63 | DATA_PREST_SERV | VARCHAR2(8) | Y |  |  |
| 64 | IND_CONCILIACAO | CHAR(1) | Y |  |  |
| 65 | BAIRRO_II | VARCHAR2(60) | Y |  |  |
| 66 | NOM_CONTATO | VARCHAR2(100) | Y |  |  |
| 67 | ENDERECO_WEB | VARCHAR2(200) | Y |  |  |
| 68 | COD_CATEG_TRAB | VARCHAR2(3) | Y |  |  |
| 69 | IND_NAT_ATIVIDADE | CHAR(1) | Y |  |  |
| 70 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 71 | CPF_SP | VARCHAR2(14) | Y |  | Informar o CPF do Proprietário da Fazenda SP (Sao Paulo) |
| 72 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 73 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 74 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 75 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 76 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 77 | VLR_RESERVADO6 | VARCHAR2(17) | Y |  |  |
| 78 | VLR_RESERVADO7 | VARCHAR2(17) | Y |  |  |
| 79 | VLR_RESERVADO8 | VARCHAR2(17) | Y |  |  |
| 80 | IND_ISENTO_IMUNE | VARCHAR2(1) | Y |  | Informações sobre isenção e imunidade: 1 - Não isenta/não imune; 2- Instituição de educação e de assistência social sem fins lucrativos, a que se refere o art. 12 da Lei nº 9.532, de 10 de dezembro de 1997; 3- Instituição de caráter filantrópico, recreativo, cultural, científico e às associações civis, a que se refere o art. 15 da Lei nº 9.532, de 1997. |
| 81 | IND_CONTRIB_ICMS | VARCHAR2(1) | Y |  | Informações sobre contribuinte ICMS: 1 – Contribuinte do ICMS; 2 – Contribuinte Isento de Inscrição no Cadastro de Contribuintes do ICMS; 9 – Não Contribuinte. |
| 82 | PST_ID | NUMBER | Y |  |  |
| 83 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 84 | IND_PRODUTOR_RURAL | VARCHAR2(1) | Y |  |  |
| 85 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 86 | NUM_ID_OUTROS | VARCHAR2(20) | Y |  |  |
| 87 | COD_ID_ASSINANTE | VARCHAR2(15) | Y |  |  |
| 88 | IND_TP_ASSINANTE | VARCHAR2(2) | Y |  |  |
| 89 | ENDERECO_ENTREGA | VARCHAR2(60) | Y |  |  |
| 90 | NUM_ENDERECO_ENTREGA | VARCHAR2(60) | Y |  |  |
| 91 | COMPL_ENDERECO_ENTREGA | VARCHAR2(60) | Y |  |  |
| 92 | BAIRRO_ENTREGA | VARCHAR2(60) | Y |  |  |
| 93 | COD_MUNICIPIO_ENTREGA | VARCHAR2(5) | Y |  |  |
| 94 | CEP_ENTREGA | VARCHAR2(8) | Y |  |  |
| 95 | COD_UF_ENTREGA | VARCHAR2(2) | Y |  |  |
| 96 | DDD_ENTREGA | VARCHAR2(5) | Y |  |  |
| 97 | TELEFONE_ENTREGA | VARCHAR2(10) | Y |  |  |
| 98 | EMAIL_ENTREGA | VARCHAR2(60) | Y |  |  |
| 99 | CHAVE_SAFX04 | VARCHAR2(4000) | Y | NVL("IND_FIS_JUR",'@')\|\|NVL("COD_FIS_JUR",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX04: (CHAVE_SAFX04)
- IX_SAFX04: (DAT_GRAVACAO)
- IX_SAFX04_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX04_LOTE: (NUM_LOTE)

---

## SAFX05

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 12 | DATA_VENCTO | VARCHAR2(8) | Y |  |  |
| 13 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 14 | VLR_MOVTO | VARCHAR2(17) | Y |  |  |
| 15 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 16 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 17 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 18 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 19 | VLR_MOVTO_CONV | VARCHAR2(18) | Y |  |  |
| 20 | VLR_TOT_DOCTO | VARCHAR2(17) | Y |  |  |
| 21 | NUM_DOCTO_COMPENS | VARCHAR2(15) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | HISTORICO | VARCHAR2(50) | Y |  |  |
| 24 | OBSERVACAO | VARCHAR2(20) | Y |  |  |
| 25 | IND_TIPO_TITULO | VARCHAR2(2) | Y |  |  |
| 26 | DSC_COMPL_TITULO | VARCHAR2(50) | Y |  |  |
| 27 | QTDE_PARCELA | VARCHAR2(3) | Y |  |  |
| 28 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 29 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 30 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 31 | IND_FIS_JUR_DMED | CHAR(1) | Y |  |  |
| 32 | COD_FIS_JUR_DMED | VARCHAR2(14) | Y |  |  |
| 33 | PST_ID | NUMBER | Y |  |  |
| 34 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 35 | CHAVE_SAFX05 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX05: (CHAVE_SAFX05)
- IX_SAFX05: (DAT_GRAVACAO)
- IX_SAFX05_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX05_LOTE: (NUM_LOTE)

---

## SAFX06

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_GRP_COMB | VARCHAR2(2) | Y |  |  |
| 5 | IND_PERDA_GANHO | CHAR(1) | Y |  |  |
| 6 | QTD_COMB | VARCHAR2(17) | Y |  |  |
| 7 | QTD_GAS_A | VARCHAR2(17) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | QTD_EAC | VARCHAR2(17) | Y |  |  |
| 12 | CHAVE_SAFX06 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX06: (CHAVE_SAFX06)
- IX_SAFX06_LOTE: (NUM_LOTE)

---

## SAFX07

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | IDENT_FIS_JUR | CHAR(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 12 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 13 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 16 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 17 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 18 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 19 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 20 | DATA_SAIDA_REC | VARCHAR2(8) | Y |  |  |
| 21 | INSC_ESTAD_SUBSTIT | VARCHAR2(14) | Y |  |  |
| 22 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 23 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 24 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 25 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 26 | VLR_OUTRAS | VARCHAR2(17) | Y |  |  |
| 27 | VLR_BASE_DIF_FRETE | VARCHAR2(17) | Y |  |  |
| 28 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 29 | CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 30 | SITUACAO | CHAR(1) | Y |  |  |
| 31 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 32 | VLR_NOTA_CONV | VARCHAR2(18) | Y |  |  |
| 33 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 34 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 35 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 36 | DIF_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 37 | OBS_ICMS | VARCHAR2(45) | Y |  |  |
| 38 | COD_APUR_ICMS | VARCHAR2(5) | Y |  |  |
| 39 | VLR_ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 40 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 41 | OBS_IPI | VARCHAR2(45) | Y |  |  |
| 42 | COD_APUR_IPI | VARCHAR2(5) | Y |  |  |
| 43 | VLR_ALIQ_IR | VARCHAR2(7) | Y |  |  |
| 44 | VLR_IR | VARCHAR2(17) | Y |  |  |
| 45 | VLR_ALIQ_ISS | VARCHAR2(7) | Y |  |  |
| 46 | VLR_ISS | VARCHAR2(17) | Y |  |  |
| 47 | VLR_ALIQ_SUB_ICMS | VARCHAR2(7) | Y |  |  |
| 48 | VLR_SUBST_ICMS | VARCHAR2(17) | Y |  |  |
| 49 | OBS_SUBST_ICMS | VARCHAR2(45) | Y |  |  |
| 50 | COD_APUR_SUB_ICMS | VARCHAR2(5) | Y |  |  |
| 51 | BASE_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 52 | BASE_ISEN_ICMS | VARCHAR2(17) | Y |  |  |
| 53 | BASE_OUTR_ICMS | VARCHAR2(17) | Y |  |  |
| 54 | BASE_REDU_ICMS | VARCHAR2(17) | Y |  |  |
| 55 | BASE_TRIB_IPI | VARCHAR2(17) | Y |  |  |
| 56 | BASE_ISEN_IPI | VARCHAR2(17) | Y |  |  |
| 57 | BASE_OUTR_IPI | VARCHAR2(17) | Y |  |  |
| 58 | BASE_REDU_IPI | VARCHAR2(17) | Y |  |  |
| 59 | BASE_TRIB_IR | VARCHAR2(17) | Y |  |  |
| 60 | BASE_ISEN_IR | VARCHAR2(17) | Y |  |  |
| 61 | BASE_TRIB_ISS | VARCHAR2(17) | Y |  |  |
| 62 | BASE_ISEN_ISS | VARCHAR2(17) | Y |  |  |
| 63 | BASE_REAL_TERC_ISS | VARCHAR2(17) | Y |  |  |
| 64 | BASE_SUB_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 65 | NUM_MAQ_REG | VARCHAR2(6) | Y |  |  |
| 66 | NUM_CUPON_FISC | VARCHAR2(6) | Y |  |  |
| 67 | IND_MODELO_CUPOM | VARCHAR2(2) | Y |  |  |
| 68 | VLR_CONTAB_COMPL | VARCHAR2(17) | Y |  |  |
| 69 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 70 | VLR_ALIQ_DESTINO | VARCHAR2(7) | Y |  |  |
| 71 | VLR_OUTROS1 | VARCHAR2(17) | Y |  |  |
| 72 | VLR_OUTROS2 | VARCHAR2(17) | Y |  |  |
| 73 | VLR_OUTROS3 | VARCHAR2(17) | Y |  |  |
| 74 | VLR_OUTROS4 | VARCHAR2(17) | Y |  |  |
| 75 | VLR_OUTROS5 | VARCHAR2(17) | Y |  |  |
| 76 | VLR_ALIQ_OUTROS1 | VARCHAR2(7) | Y |  |  |
| 77 | VLR_ALIQ_OUTROS2 | VARCHAR2(7) | Y |  |  |
| 78 | IND_NF_ESPECIAL | CHAR(1) | Y |  |  |
| 79 | IND_TP_FRETE | CHAR(1) | Y |  |  |
| 80 | COD_MUNICIPIO | VARCHAR2(7) | Y |  |  |
| 81 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 82 | DAT_DI | VARCHAR2(8) | Y |  |  |
| 83 | VLR_TOM_SERVICO | VARCHAR2(17) | Y |  |  |
| 84 | DAT_ESCR_EXTEMP | VARCHAR2(8) | Y |  |  |
| 85 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 86 | COD_REGIAO | VARCHAR2(2) | Y |  |  |
| 87 | DAT_AUTENTIC | VARCHAR2(8) | Y |  |  |
| 88 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 89 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 90 | VLR_ICMS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 91 | VLR_IPI_NDESTAC | VARCHAR2(17) | Y |  |  |
| 92 | VLR_BASE_INSS | VARCHAR2(17) | Y |  |  |
| 93 | VLR_ALIQ_INSS | VARCHAR2(7) | Y |  |  |
| 94 | VLR_INSS_RETIDO | VARCHAR2(17) | Y |  |  |
| 95 | VLR_MAT_APLIC_ISS | VARCHAR2(17) | Y |  |  |
| 96 | VLR_SUBEMPR_ISS | VARCHAR2(17) | Y |  |  |
| 97 | IND_MUNIC_ISS | CHAR(1) | Y |  |  |
| 98 | IND_CLASSE_OP_ISS | CHAR(1) | Y |  |  |
| 99 | DAT_FATO_GERADOR | VARCHAR2(8) | Y |  |  |
| 100 | DAT_CANCELAMENTO | VARCHAR2(8) | Y |  |  |
| 101 | NUM_PAGINA | VARCHAR2(6) | Y |  |  |
| 102 | NUM_LIVRO | VARCHAR2(6) | Y |  |  |
| 103 | NRO_AIDF_NF | VARCHAR2(12) | Y |  |  |
| 104 | DAT_VALID_DOC_AIDF | VARCHAR2(8) | Y |  |  |
| 105 | IND_FATURA | CHAR(1) | Y |  |  |
| 106 | COD_QUITACAO | VARCHAR2(5) | Y |  |  |
| 107 | NUM_SELO_CONT_ICMS | VARCHAR2(12) | Y |  |  |
| 108 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 109 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 110 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 111 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 112 | BASE_ICMS_ORIGDEST | VARCHAR2(17) | Y |  |  |
| 113 | VLR_ICMS_ORIGDEST | VARCHAR2(17) | Y |  |  |
| 114 | ALIQ_ICMS_ORIGDEST | VARCHAR2(7) | Y |  |  |
| 115 | VLR_DESC_CONDIC | VARCHAR2(17) | Y |  |  |
| 116 | VLR_BASE_ISE_ICMSS | VARCHAR2(17) | Y |  |  |
| 117 | VLR_BASE_OUT_ICMSS | VARCHAR2(17) | Y |  |  |
| 118 | VLR_RED_BASE_ICMSS | VARCHAR2(17) | Y |  |  |
| 119 | PERC_RED_BASE_ICMS | VARCHAR2(7) | Y |  |  |
| 120 | IND_FISJUR_CPDIR | CHAR(1) | Y |  |  |
| 121 | COD_FISJUR_CPDIR | VARCHAR2(14) | Y |  |  |
| 122 | IND_MEDIDAJUDICIAL | CHAR(1) | Y |  |  |
| 123 | UF_ORIG_DEST | VARCHAR2(2) | Y |  |  |
| 124 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  |  |
| 125 | DAT_GRAVACAO | DATE | Y |  |  |
| 126 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 127 | NUM_CTR_DISP | VARCHAR2(10) | Y |  |  |
| 128 | NUM_FIM_DOCTO | VARCHAR2(12) | Y |  |  |
| 129 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 130 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 131 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 132 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 133 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 134 | COD_PAGTO_INSS | VARCHAR2(4) | Y |  |  |
| 135 | DAT_INTERN_AM | VARCHAR2(8) | Y |  |  |
| 136 | IND_FISJUR_LSG | CHAR(1) | Y |  |  |
| 137 | COD_FISJUR_LSG | VARCHAR2(14) | Y |  |  |
| 138 | COMPROV_EXP | VARCHAR2(15) | Y |  |  |
| 139 | NUM_FINAL_CRT_DISP | VARCHAR2(12) | Y |  |  |
| 140 | NUM_ALVARA | VARCHAR2(8) | Y |  |  |
| 141 | NOTIFICA_SEFAZ | VARCHAR2(14) | Y |  |  |
| 142 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 143 | IND_NOTA_SERVICO | CHAR(1) | Y |  |  |
| 144 | COD_MOTIVO | VARCHAR2(10) | Y |  |  |
| 145 | COD_AMPARO | VARCHAR2(10) | Y |  |  |
| 146 | UF_AMPARO_LEGAL | VARCHAR2(2) | Y |  |  |
| 147 | SEQ_ARQ | NUMBER(20) | Y |  |  |
| 148 | OBS_COMPL_MOTIVO | VARCHAR2(100) | Y |  |  |
| 149 | IND_TP_RET | CHAR(1) | Y |  |  |
| 150 | IND_TP_TOMADOR | CHAR(1) | Y |  |  |
| 151 | COD_ANTEC_ST | VARCHAR2(1) | Y |  |  |
| 152 | CNPJ_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 153 | UF_ARMAZ_ORIG | VARCHAR2(2) | Y |  |  |
| 154 | INS_EST_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 155 | CNPJ_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 156 | UF_ARMAZ_DEST | VARCHAR2(2) | Y |  |  |
| 157 | INS_EST_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 158 | OBS_INF_ADIC_NF | VARCHAR2(250) | Y |  |  |
| 159 | VLR_BASE_INSS_2 | VARCHAR2(17) | Y |  |  |
| 160 | VLR_ALIQ_INSS_2 | VARCHAR2(7) | Y |  |  |
| 161 | VLR_INSS_RETIDO_2 | VARCHAR2(17) | Y |  |  |
| 162 | COD_PAGTO_INSS_2 | VARCHAR2(4) | Y |  |  |
| 163 | VLR_BASE_PIS_ST | VARCHAR2(17) | Y |  |  |
| 164 | VLR_ALIQ_PIS_ST | VARCHAR2(7) | Y |  |  |
| 165 | VLR_PIS_ST | VARCHAR2(17) | Y |  |  |
| 166 | VLR_BASE_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 167 | VLR_ALIQ_COFINS_ST | VARCHAR2(7) | Y |  |  |
| 168 | VLR_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 169 | VLR_BASE_CSLL | VARCHAR2(17) | Y |  |  |
| 170 | VLR_ALIQ_CSLL | VARCHAR2(7) | Y |  |  |
| 171 | VLR_CSLL | VARCHAR2(17) | Y |  |  |
| 172 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 173 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 174 | BASE_ICMSS_SUBSTITUIDO | VARCHAR2(17) | Y |  |  |
| 175 | VLR_ICMSS_SUBSTITUIDO | VARCHAR2(17) | Y |  |  |
| 176 | COD_CEI | VARCHAR2(15) | Y |  |  |
| 177 | VLR_JUROS_INSS | VARCHAR2(17) | Y |  |  |
| 178 | VLR_MULTA_INSS | VARCHAR2(17) | Y |  |  |
| 179 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 180 | VLR_ICMSS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 181 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 182 | DAT_PGTO_GNRE_DARJ | VARCHAR2(8) | Y |  |  |
| 183 | DT_PAGTO_NF | VARCHAR2(8) | Y |  |  |
| 184 | HORA_SAIDA | VARCHAR2(6) | Y |  |  |
| 185 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  |  |
| 186 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 187 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 188 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 189 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |
| 190 | COD_MUNICIPIO_ORIG | VARCHAR2(5) | Y |  |  |
| 191 | COD_MUNICIPIO_DEST | VARCHAR2(5) | Y |  |  |
| 192 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 193 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 194 | VLR_MAT_PROP | VARCHAR2(17) | Y |  |  |
| 195 | VLR_MAT_TERC | VARCHAR2(17) | Y |  |  |
| 196 | VLR_BASE_ISS_RETIDO | VARCHAR2(17) | Y |  |  |
| 197 | VLR_ISS_RETIDO | VARCHAR2(17) | Y |  |  |
| 198 | VLR_DEDUCAO_ISS | VARCHAR2(17) | Y |  |  |
| 199 | COD_MUNIC_ARMAZ_ORIG | VARCHAR2(5) | Y |  |  |
| 200 | INS_MUNIC_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 201 | COD_MUNIC_ARMAZ_DEST | VARCHAR2(5) | Y |  |  |
| 202 | INS_MUNIC_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 203 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 204 | COD_CLASSE_CONSUMO | VARCHAR2(2) | Y |  |  |
| 205 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 206 | NUM_CONTRATO | VARCHAR2(14) | Y |  |  |
| 207 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  |  |
| 208 | COD_TP_UTIL | VARCHAR2(2) | Y |  |  |
| 209 | GRUPO_TENSAO | VARCHAR2(2) | Y |  |  |
| 210 | DATA_CONSUMO_INI | VARCHAR2(8) | Y |  |  |
| 211 | DATA_CONSUMO_FIM | VARCHAR2(8) | Y |  |  |
| 212 | DATA_CONSUMO_LEIT | VARCHAR2(8) | Y |  |  |
| 213 | QTD_CONTRATADA_PONTA | VARCHAR2(17) | Y |  |  |
| 214 | QTD_CONTRATADA_FPONTA | VARCHAR2(17) | Y |  |  |
| 215 | QTD_CONSUMO_TOTAL | VARCHAR2(17) | Y |  |  |
| 216 | UF_CONSUMO | VARCHAR2(2) | Y |  |  |
| 217 | COD_MUNIC_CONSUMO | VARCHAR2(5) | Y |  |  |
| 218 | COD_OPER_ESP_ST | CHAR(1) | Y |  |  |
| 219 | ATO_NORMATIVO | VARCHAR2(20) | Y |  | SEF-PE: Ato Normativo |
| 220 | NUM_ATO_NORMATIVO | VARCHAR2(5) | Y |  | SEF-PE: Número do Ato Normativo |
| 221 | ANO_ATO_NORMATIVO | VARCHAR2(4) | Y |  | SEF-PE: Ano do Ato Normativo |
| 222 | CAPITULACAO_NORMA | VARCHAR2(30) | Y |  | SEF-PE: Capitulação da Norma |
| 223 | VLR_OUTRAS_ENTID | VARCHAR2(17) | Y |  | Valor de outras Entidades |
| 224 | VLR_TERCEIROS | VARCHAR2(17) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 225 | IND_TP_COMPL_ICMS | VARCHAR2(2) | Y |  |  |
| 226 | VLR_BASE_CIDE | VARCHAR2(17) | Y |  |  |
| 227 | VLR_ALIQ_CIDE | VARCHAR2(7) | Y |  |  |
| 228 | VLR_CIDE | VARCHAR2(17) | Y |  |  |
| 229 | COD_VERIFIC_NFE | VARCHAR2(60) | Y |  |  |
| 230 | COD_TP_RPS_NFE | VARCHAR2(5) | Y |  |  |
| 231 | NUM_RPS_NFE | VARCHAR2(12) | Y |  |  |
| 232 | SERIE_RPS_NFE | VARCHAR2(5) | Y |  |  |
| 233 | DAT_EMISSAO_RPS_NFE | VARCHAR2(8) | Y |  |  |
| 234 | DSC_SERVICO_NFE | VARCHAR2(1000) | Y |  |  |
| 235 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 236 | NUM_DV_NFE | CHAR(1) | Y |  |  |
| 237 | MODELO_NF_DMS | VARCHAR2(3) | Y |  | Modelo da Nota Fiscal para a série U ou M em atendimento a DMS Campo Grande - Mato Grosso do Sul. |
| 238 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 239 | VLR_COMISSAO | VARCHAR2(17) | Y |  |  |
| 240 | IND_NFE_DENEG_INUT | CHAR(1) | Y |  |  |
| 241 | IND_NF_REG_ESPECIAL | CHAR(1) | Y |  |  |
| 242 | VLR_ABAT_NTRIBUTADO | VARCHAR2(17) | Y |  |  |
| 243 | VLR_OUTROS_ICMS | VARCHAR2(17) | Y |  | Campo criado para gerar o registro 90 da DAPI MG, recuperando as informações da Apuração do ICMS automaticamente. |
| 244 | HORA_EMISSAO | VARCHAR2(6) | Y |  |  |
| 245 | OBS_DADOS_FATURA | VARCHAR2(256) | Y |  |  |
| 246 | HORA_SAIDA_REC | VARCHAR2(6) | Y |  |  |
| 247 | IND_FIS_CONCES | CHAR(1) | Y |  |  |
| 248 | COD_FIS_CONCES | VARCHAR2(14) | Y |  |  |
| 249 | COD_AUTENTIC | VARCHAR2(32) | Y |  | Codigo de Autenticação utilizado para Portaria CAT44 - SP |
| 250 | IND_PORT_CAT44 | CHAR(1) | Y |  | Indicador se o regiastro vai ser utilizadona CAT44 ou  não |
| 251 | VLR_BASE_INSS_RURAL | VARCHAR2(17) | Y |  |  |
| 252 | VLR_ALIQ_INSS_RURAL | VARCHAR2(7) | Y |  |  |
| 253 | VLR_INSS_RURAL | VARCHAR2(17) | Y |  |  |
| 254 | COD_CLASSE_CONSUMO_SEF_PE | VARCHAR2(2) | Y |  |  |
| 255 | VLR_PIS_RETIDO | VARCHAR2(17) | Y |  |  |
| 256 | VLR_COFINS_RETIDO | VARCHAR2(17) | Y |  |  |
| 257 | DAT_LANC_PIS_COFINS | VARCHAR2(8) | Y |  |  |
| 258 | IND_PIS_COFINS_EXTEMP | VARCHAR2(1) | Y |  |  |
| 259 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 260 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 261 | IND_NAT_FRETE | CHAR(1) | Y |  |  |
| 262 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  |  |
| 263 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 264 | IND_VENDA_CANC | CHAR(1) | Y |  |  |
| 265 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 266 | IND_NF_CONTINGENCIA | VARCHAR2(1) | Y |  |  |
| 267 | VLR_ACRESCIMO | VARCHAR2(17) | Y |  |  |
| 268 | VLR_ANTECIP_TRIB | VARCHAR2(17) | Y |  |  |
| 269 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |
| 270 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 271 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 272 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 273 | NUM_NFTS | VARCHAR2(12) | Y |  |  |
| 274 | IND_NF_VENDA_TERCEIROS | CHAR(1) | Y |  | Indicador de Nota Fiscal de Venda de Mercadoria Emitida por Terceiros |
| 275 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 276 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 277 | DSC_RESERVADO6 | VARCHAR2(17) | Y |  |  |
| 278 | DSC_RESERVADO7 | VARCHAR2(17) | Y |  |  |
| 279 | DSC_RESERVADO8 | VARCHAR2(17) | Y |  |  |
| 280 | IDENTIF_DOCFIS | VARCHAR2(128) | Y |  |  |
| 281 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 282 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 283 | IND_PREST_SERV | CHAR(1) | Y |  |  |
| 284 | IND_TIPO_PROC | CHAR(1) | Y |  |  |
| 285 | NUM_PROC_JUR | VARCHAR2(20) | Y |  |  |
| 286 | IND_DEC_PROC | CHAR(1) | Y |  |  |
| 287 | IND_TIPO_AQUIS | CHAR(1) | Y |  |  |
| 288 | VLR_DESC_GILRAT | VARCHAR2(17) | Y |  |  |
| 289 | VLR_DESC_SENAR | VARCHAR2(17) | Y |  |  |
| 290 | CNPJ_SUBEMPREITEIRO | VARCHAR2(14) | Y |  |  |
| 291 | CNPJ_CPF_PROPRIETARIO_CNO | VARCHAR2(14) | Y |  |  |
| 292 | VLR_RET_SUBEMPREITADO | VARCHAR2(17) | Y |  |  |
| 293 | NUM_DOCFIS_SERV | VARCHAR2(60) | Y |  |  |
| 294 | VLR_FCP_UF_DEST | VARCHAR2(17) | Y |  |  |
| 295 | VLR_ICMS_UF_DEST | VARCHAR2(17) | Y |  |  |
| 296 | VLR_ICMS_UF_ORIG | VARCHAR2(17) | Y |  |  |
| 297 | VLR_CONTRIB_PREV | VARCHAR2(17) | Y |  |  |
| 298 | VLR_GILRAT | VARCHAR2(17) | Y |  |  |
| 299 | VLR_CONTRIB_SENAR | VARCHAR2(17) | Y |  |  |
| 300 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 301 | NUM_CERTIF_QUAL | VARCHAR2(10) | Y |  |  |
| 302 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 303 | DATA_TRAB | VARCHAR2(8) | Y | CASE  WHEN ("DATA_SAIDA_REC" IS NULL OR "DATA_S... |  |
| 304 | OBS_REINF | VARCHAR2(250) | Y |  |  |
| 305 | VLR_TOT_ADIC | VARCHAR2(17) | Y |  |  |
| 306 | VLR_RET_SERV | VARCHAR2(17) | Y |  |  |
| 307 | VLR_SERV_15 | VARCHAR2(17) | Y |  |  |
| 308 | VLR_SERV_20 | VARCHAR2(17) | Y |  |  |
| 309 | VLR_SERV_25 | VARCHAR2(17) | Y |  |  |
| 310 | VLR_IPI_DEV | VARCHAR2(17) | Y |  |  |
| 311 | VLR_SEST | VARCHAR2(17) | Y |  |  |
| 312 | VLR_SENAT | VARCHAR2(17) | Y |  |  |
| 313 | IND_FIN_EMISSAO_NFE | VARCHAR2(1) | Y |  |  |
| 314 | NUM_AUTENTIC_NFE_SUBST | VARCHAR2(80) | Y |  |  |
| 315 | PST_ID | NUMBER | Y |  |  |
| 316 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 317 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 318 | IND_TRIB_PRODUTOR_CP | VARCHAR2(1) | Y |  | Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária. 1 - Sobre a comercialização da sua produção; 2 - Sobre a folha de pagamento. Valores Válidos: 1, 2.  |
| 319 | COD_MODELO_NFE_SUBST | VARCHAR2(2) | Y |  |  |
| 320 | COD_AUTENTIC_NFE_SUBST | VARCHAR2(32) | Y |  |  |
| 321 | VLR_ENERGIA_INJ | VARCHAR2(17) | Y |  |  |
| 322 | VLR_OUTRAS_DED | VARCHAR2(17) | Y |  |  |
| 323 | IND_TP_FAT_NFE | VARCHAR2(1) | Y |  |  |
| 324 | IND_TP_AMB_NFE | VARCHAR2(1) | Y |  |  |
| 325 | COD_NF_NFE | VARCHAR2(7) | Y |  |  |
| 326 | IND_PRE_PAGO | VARCHAR2(1) | Y |  |  |
| 327 | IND_SESSAO_REDE | VARCHAR2(1) | Y |  |  |
| 328 | DAT_INI_CONTRATO | VARCHAR2(8) | Y |  |  |
| 329 | DAT_FIM_CONTRATO | VARCHAR2(8) | Y |  |  |
| 330 | NUM_TERMINAL_TEL | VARCHAR2(12) | Y |  |  |
| 331 | UF_TERMINAL_TEL | VARCHAR2(2) | Y |  |  |
| 332 | VLR_ICMS_DESONERADO | VARCHAR2(17) | Y |  |  |
| 333 | VLR_FCP | VARCHAR2(17) | Y |  |  |
| 334 | VLR_FUNTTEL | VARCHAR2(17) | Y |  |  |
| 335 | VLR_FUST | VARCHAR2(17) | Y |  |  |
| 336 | CNPJ_DOWNLOAD | VARCHAR2(14) | Y |  |  |
| 337 | CPF_DOWNLOAD | VARCHAR2(11) | Y |  |  |
| 338 | VLR_CSLL_RETIDO | VARCHAR2(17) | Y |  |  |
| 339 | VLR_IRRF_RETIDO | VARCHAR2(17) | Y |  |  |
| 340 | INSC_EST_VIRTUAL | VARCHAR2(14) | Y |  |  |
| 341 | PERIOD_APUR_SUBST | VARCHAR2(6) | Y |  |  |
| 342 | COD_MOTIVO_SUBST | VARCHAR2(2) | Y |  |  |
| 343 | COD_AUTENTIC_COF | VARCHAR2(44) | Y |  |  |
| 344 | CNPJ_EMIT_FATURAMENTO | VARCHAR2(14) | Y |  |  |
| 345 | UF_EMIT_FATURAMENTO | VARCHAR2(2) | Y |  |  |
| 346 | CNPJ_EMIT_COF | VARCHAR2(14) | Y |  |  |
| 347 | COD_MODELO_COF | VARCHAR2(2) | Y |  |  |
| 348 | SERIE_DOCFIS_COF | VARCHAR2(3) | Y |  |  |
| 349 | NUM_DOCFIS_COF | VARCHAR2(12) | Y |  |  |
| 350 | ANO_MES_COF | VARCHAR2(6) | Y |  |  |
| 351 | COD_HASH_COF | VARCHAR2(32) | Y |  |  |
| 352 | CHAVE_SAFX07 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX07: (CHAVE_SAFX07)
- IX_SAFX07: (DAT_GRAVACAO)
- IX_SAFX07_1: (COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, MOVTO_E_S)
- IX_SAFX07_2: (COD_EMPRESA, COD_ESTAB, DATA_SAIDA_REC, MOVTO_E_S)
- IX_SAFX07_3: (COD_EMPRESA, COD_ESTAB, DATA_TRAB, NUM_PROCESSO)
- IX_SAFX07_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX07_LOTE: (NUM_LOTE)

---

## SAFX08

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_BEM_PATR | CHAR(1) | Y |  |  |
| 13 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 14 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 15 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 16 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 17 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 18 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 19 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 20 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 21 | DESCRICAO_COMPL | VARCHAR2(255) | Y |  |  |
| 22 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 23 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 24 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 25 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 26 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 27 | VLR_UNIT | VARCHAR2(19) | Y |  |  |
| 28 | VLR_ITEM | VARCHAR2(17) | Y |  |  |
| 29 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 30 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 31 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 32 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 33 | IND_IPI_INCLUSO | CHAR(1) | Y |  |  |
| 34 | NUM_ROMANEIO | VARCHAR2(12) | Y |  |  |
| 35 | DATA_ROMANEIO | VARCHAR2(8) | Y |  |  |
| 36 | PESO_LIQUIDO | VARCHAR2(14) | Y |  |  |
| 37 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 38 | VLR_ITEM_CONVER | VARCHAR2(17) | Y |  |  |
| 39 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 40 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 41 | VLR_OUTRAS | VARCHAR2(17) | Y |  |  |
| 42 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 43 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 44 | DIF_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 45 | OBS_ICMS | VARCHAR2(45) | Y |  |  |
| 46 | COD_APUR_ICMS | VARCHAR2(5) | Y |  |  |
| 47 | VLR_ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 48 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 49 | OBS_IPI | VARCHAR2(45) | Y |  |  |
| 50 | COD_APUR_IPI | VARCHAR2(5) | Y |  |  |
| 51 | VLR_ALIQ_SUB_ICMS | VARCHAR2(7) | Y |  |  |
| 52 | VLR_SUBST_ICMS | VARCHAR2(17) | Y |  |  |
| 53 | OBS_SUBST_ICMS | VARCHAR2(45) | Y |  |  |
| 54 | COD_APUR_SUB_ICMS | VARCHAR2(5) | Y |  |  |
| 55 | TRIB_ICMS | CHAR(1) | Y |  |  |
| 56 | BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 57 | BASE_REDU_ICMS | VARCHAR2(17) | Y |  |  |
| 58 | TRIB_IPI | CHAR(1) | Y |  |  |
| 59 | BASE_IPI | VARCHAR2(17) | Y |  |  |
| 60 | BASE_REDU_IPI | VARCHAR2(17) | Y |  |  |
| 61 | BASE_SUB_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 62 | VLR_CONTAB_COMPL | VARCHAR2(17) | Y |  |  |
| 63 | VLR_ALIQ_DESTINO | VARCHAR2(7) | Y |  |  |
| 64 | VLR_OUTROS1 | VARCHAR2(17) | Y |  |  |
| 65 | VLR_OUTROS2 | VARCHAR2(17) | Y |  |  |
| 66 | VLR_OUTROS3 | VARCHAR2(17) | Y |  |  |
| 67 | VLR_OUTROS4 | VARCHAR2(17) | Y |  |  |
| 68 | VLR_OUTROS5 | VARCHAR2(17) | Y |  |  |
| 69 | VLR_ALIQ_OUTROS1 | VARCHAR2(7) | Y |  |  |
| 70 | VLR_ALIQ_OUTROS2 | VARCHAR2(7) | Y |  |  |
| 71 | VLR_CONTAB_ITEM | VARCHAR2(17) | Y |  |  |
| 72 | COD_OBS_VCONT_COMP | VARCHAR2(10) | Y |  |  |
| 73 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 74 | VLR_OUTROS_ICMS | VARCHAR2(17) | Y |  |  |
| 75 | VLR_OUTROS_IPI | VARCHAR2(17) | Y |  |  |
| 76 | NUM_ATO_CONCES | VARCHAR2(15) | Y |  |  |
| 77 | DAT_EMBARQUE | VARCHAR2(8) | Y |  |  |
| 78 | NUM_REG_EXP | VARCHAR2(12) | Y |  |  |
| 79 | NUM_DESP_EXP | VARCHAR2(11) | Y |  |  |
| 80 | VLR_TOM_SERVICO | VARCHAR2(17) | Y |  |  |
| 81 | VLR_DESP_MOEDA_EXP | VARCHAR2(17) | Y |  |  |
| 82 | COD_MOEDA_NEGOC | VARCHAR2(10) | Y |  |  |
| 83 | COD_PAIS_DEST_ORIG | VARCHAR2(3) | Y |  |  |
| 84 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 85 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 86 | VLR_ICMS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 87 | VLR_IPI_NDESTAC | VARCHAR2(17) | Y |  |  |
| 88 | TRIB_ICMS_AUX | CHAR(1) | Y |  |  |
| 89 | BASE_ICMS_AUX | VARCHAR2(17) | Y |  |  |
| 90 | TRIB_IPI_AUX | CHAR(1) | Y |  |  |
| 91 | BASE_IPI_AUX | VARCHAR2(17) | Y |  |  |
| 92 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 93 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 94 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 95 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 96 | BASE_ICMS_ORIGDEST | VARCHAR2(17) | Y |  |  |
| 97 | VLR_ICMS_ORIGDEST | VARCHAR2(17) | Y |  |  |
| 98 | ALIQ_ICMS_ORIGDEST | VARCHAR2(7) | Y |  |  |
| 99 | VLR_DESC_CONDIC | VARCHAR2(17) | Y |  |  |
| 100 | TRIB_ICMSS | CHAR(1) | Y |  |  |
| 101 | BASE_REDU_ICMSS | VARCHAR2(17) | Y |  |  |
| 102 | VLR_CUSTO_TRANSF | VARCHAR2(17) | Y |  |  |
| 103 | PERC_RED_BASE_ICMS | VARCHAR2(7) | Y |  |  |
| 104 | QTD_EMBARCADA | VARCHAR2(17) | Y |  |  |
| 105 | DAT_REGISTRO_EXP | VARCHAR2(8) | Y |  |  |
| 106 | DAT_DESPACHO | VARCHAR2(8) | Y |  |  |
| 107 | DAT_AVERBACAO | VARCHAR2(8) | Y |  |  |
| 108 | DAT_DI | VARCHAR2(8) | Y |  |  |
| 109 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 110 | DAT_GRAVACAO | DATE | Y |  |  |
| 111 | DSC_MOT_OCOR | VARCHAR2(45) | Y |  |  |
| 112 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 113 | VLR_BASE_ICMS_ORIG | VARCHAR2(17) | Y |  |  |
| 114 | VLR_TRIB_ICMS_ORIG | VARCHAR2(17) | Y |  |  |
| 115 | VLR_BASE_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 116 | VLR_TRIB_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 117 | VLR_PERC_PRES_ICMS | VARCHAR2(7) | Y |  |  |
| 118 | VLR_PRECO_BASE_ST | VARCHAR2(17) | Y |  |  |
| 119 | COD_OPER_OIL | VARCHAR2(10) | Y |  |  |
| 120 | COD_DCR | VARCHAR2(15) | Y |  |  |
| 121 | COD_PROJETO | VARCHAR2(20) | Y |  |  |
| 122 | IND_MOV_FIS | CHAR(1) | Y |  |  |
| 123 | CHASSI | VARCHAR2(17) | Y |  |  |
| 124 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 125 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 126 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 127 | VLR_BASE_PIS_ST | VARCHAR2(17) | Y |  |  |
| 128 | VLR_ALIQ_PIS_ST | VARCHAR2(7) | Y |  |  |
| 129 | VLR_PIS_ST | VARCHAR2(17) | Y |  |  |
| 130 | VLR_BASE_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 131 | VLR_ALIQ_COFINS_ST | VARCHAR2(7) | Y |  |  |
| 132 | VLR_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 133 | VLR_BASE_CSLL | VARCHAR2(17) | Y |  |  |
| 134 | VLR_ALIQ_CSLL | VARCHAR2(7) | Y |  |  |
| 135 | VLR_CSLL | VARCHAR2(17) | Y |  |  |
| 136 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 137 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 138 | IND_FORNEC_ICMSS | CHAR(1) | Y |  |  |
| 139 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 140 | VLR_ICMSS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 141 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 142 | DAT_PGTO_GNRE_DARJ | VARCHAR2(8) | Y |  |  |
| 143 | VLR_CUSTO_UNIT | VARCHAR2(17) | Y |  |  |
| 144 | VLR_FATOR_CONV | VARCHAR2(17) | Y |  |  |
| 145 | QUANTIDADE_CONV | VARCHAR2(17) | Y |  |  |
| 146 | VLR_FECP_ICMS | VARCHAR2(17) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 147 | VLR_FECP_DIFALIQ | VARCHAR2(17) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 148 | VLR_FECP_ICMS_ST | VARCHAR2(17) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 149 | VLR_FECP_FONTE | VARCHAR2(17) | Y |  | Campo utilizado para lancamento do valor do FUNCEP ref a Regime Fonte - GIM-PB |
| 150 | TRIB_ICMSS_AUX2 | CHAR(1) | Y |  |  |
| 151 | BASE_ICMSS_AUX2 | VARCHAR2(17) | Y |  |  |
| 152 | VLR_BASE_ICMSS_N_ESCRIT | VARCHAR2(17) | Y |  | Valor base do ICMS-ST não escriturado |
| 153 | VLR_ICMSS_N_ESCRIT | VARCHAR2(17) | Y |  | Valor do ICMS-ST não escriturado |
| 154 | COD_TRIB_IPI | VARCHAR2(2) | Y |  |  |
| 155 | LOTE_MEDICAMENTO | VARCHAR2(50) | Y |  |  |
| 156 | VALID_MEDICAMENTO | VARCHAR2(8) | Y |  |  |
| 157 | IND_BASE_MEDICAMENTO | CHAR(1) | Y |  |  |
| 158 | VLR_PRECO_MEDICAMENTO | VARCHAR2(17) | Y |  |  |
| 159 | IND_TIPO_ARMA | CHAR(1) | Y |  |  |
| 160 | NUM_SERIE_ARMA | VARCHAR2(50) | Y |  |  |
| 161 | NUM_CANO_ARMA | VARCHAR2(50) | Y |  |  |
| 162 | DSC_ARMA | VARCHAR2(100) | Y |  |  |
| 163 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 164 | COD_EX_NCM | VARCHAR2(2) | Y |  |  |
| 165 | COD_EX_IMP | VARCHAR2(2) | Y |  |  |
| 166 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 167 | CNPJ_OPERADORA | VARCHAR2(14) | Y |  |  |
| 168 | CPF_OPERADORA | VARCHAR2(14) | Y |  |  |
| 169 | UF_OPERADORA | VARCHAR2(2) | Y |  |  |
| 170 | INS_EST_OPERADORA | VARCHAR2(14) | Y |  |  |
| 171 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 172 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  |  |
| 173 | VLR_TERCEIROS | VARCHAR2(17) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 174 | VLR_PRECO_SUGER | VARCHAR2(17) | Y |  | Valor do preco sugerido do produto - Meio Magnetico - Reg78 - CAT 90 - SP |
| 175 | VLR_BASE_CIDE | VARCHAR2(17) | Y |  |  |
| 176 | VLR_ALIQ_CIDE | VARCHAR2(7) | Y |  |  |
| 177 | VLR_CIDE | VARCHAR2(17) | Y |  |  |
| 178 | COD_OPER_ESP_ST | VARCHAR2(2) | Y |  |  |
| 179 | VLR_COMISSAO | VARCHAR2(17) | Y |  |  |
| 180 | VLR_ICMS_FRETE | VARCHAR2(17) | Y |  |  |
| 181 | VLR_DIFAL_FRETE | VARCHAR2(17) | Y |  |  |
| 182 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' | Indicador para verificar se os valores de PIS/COFINS estao destacados no documentos fiscal |
| 183 | COD_ENQUAD_IPI | VARCHAR2(3) | Y |  |  |
| 184 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 185 | QTD_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 186 | VLR_ALIQ_PIS_R | VARCHAR2(19) | Y |  |  |
| 187 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 188 | QTD_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 189 | VLR_ALIQ_COFINS_R | VARCHAR2(19) | Y |  |  |
| 190 | ITEM_PORT_TARE | VARCHAR2(2) | Y |  |  |
| 191 | VLR_FUNRURAL | VARCHAR2(17) | Y |  | Campo criado para gerar o registro 88NFRA do sintegra. |
| 192 | IND_TP_PROD_MEDIC | CHAR(1) | Y |  |  |
| 193 | VLR_CUSTO_DCA | VARCHAR2(17) | Y |  |  |
| 194 | COD_TP_LANCTO | VARCHAR2(6) | Y |  |  |
| 195 | VLR_PERC_CRED_OUT | VARCHAR2(7) | Y |  |  |
| 196 | VLR_CRED_OUT | VARCHAR2(17) | Y |  |  |
| 197 | VLR_ICMS_DCA | VARCHAR2(17) | Y |  |  |
| 198 | VLR_PIS_EXP | VARCHAR2(17) | Y |  |  |
| 199 | VLR_PIS_TRIB | VARCHAR2(17) | Y |  |  |
| 200 | VLR_PIS_N_TRIB | VARCHAR2(17) | Y |  |  |
| 201 | VLR_COFINS_EXP | VARCHAR2(17) | Y |  |  |
| 202 | VLR_COFINS_TRIB | VARCHAR2(17) | Y |  |  |
| 203 | VLR_COFINS_N_TRIB | VARCHAR2(17) | Y |  |  |
| 204 | COD_ENQ_LEGAL | VARCHAR2(4) | Y |  |  |
| 205 | DAT_LANC_PIS_COFINS | VARCHAR2(8) | Y |  |  |
| 206 | IND_PIS_COFINS_EXTEMP | VARCHAR2(1) | Y |  |  |
| 207 | IND_NATUREZA_FRETE | VARCHAR2(1) | Y |  |  |
| 208 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 209 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 210 | VLR_ACRESCIMO | VARCHAR2(17) | Y |  |  |
| 211 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |
| 212 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 213 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 214 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 215 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |
| 216 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 217 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 218 | DSC_RESERVADO6 | VARCHAR2(17) | Y |  |  |
| 219 | DSC_RESERVADO7 | VARCHAR2(17) | Y |  |  |
| 220 | DSC_RESERVADO8 | VARCHAR2(17) | Y |  |  |
| 221 | INDICE_PROD_ACAB | VARCHAR2(3) | Y |  |  |
| 222 | VLR_BASE_DIA_AM | VARCHAR2(17) | Y |  |  |
| 223 | VLR_ALIQ_DIA_AM | VARCHAR2(7) | Y |  |  |
| 224 | VLR_ICMS_DIA_AM | VARCHAR2(17) | Y |  |  |
| 225 | VLR_ADUANEIRO | VARCHAR2(17) | Y |  |  |
| 226 | COD_SITUACAO_PIS_ST | VARCHAR2(2) | Y |  |  |
| 227 | COD_SITUACAO_COFINS_ST | VARCHAR2(2) | Y |  |  |
| 228 | VLR_ALIQ_DCIP | VARCHAR2(7) | Y |  |  |
| 229 | NUM_LI | VARCHAR2(10) | Y |  |  |
| 230 | VLR_FCP_UF_DEST | VARCHAR2(17) | Y |  |  |
| 231 | VLR_ICMS_UF_DEST | VARCHAR2(17) | Y |  |  |
| 232 | VLR_ICMS_UF_ORIG | VARCHAR2(17) | Y |  |  |
| 233 | VLR_DIF_DUB | VARCHAR2(17) | Y |  |  |
| 234 | VLR_ICMS_NAO_DEST | VARCHAR2(17) | Y |  |  |
| 235 | VLR_BASE_ICMS_NAO_DEST | VARCHAR2(17) | Y |  |  |
| 236 | VLR_ALIQ_ICMS_NAO_DEST | VARCHAR2(7) | Y |  |  |
| 237 | IND_MOTIVO_RES | CHAR(1) | Y |  |  |
| 238 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  |  |
| 239 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  |  |
| 240 | NUM_AUTENTIC_NFE_RET | VARCHAR2(80) | Y |  |  |
| 241 | NUM_ITEM_RET | VARCHAR2(5) | Y |  |  |
| 242 | IND_FIS_JUR_RET | CHAR(1) | Y |  |  |
| 243 | COD_FIS_JUR_RET | VARCHAR2(14) | Y |  |  |
| 244 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 245 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 246 | COD_CFO_DCIP | VARCHAR2(4) | Y |  |  |
| 247 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 248 | VLR_BASE_INSS | VARCHAR2(17) | Y |  |  |
| 249 | VLR_INSS_RETIDO | VARCHAR2(17) | Y |  |  |
| 250 | VLR_TOT_ADIC | VARCHAR2(17) | Y |  |  |
| 251 | VLR_N_RET_PRINC | VARCHAR2(17) | Y |  |  |
| 252 | VLR_N_RET_ADIC | VARCHAR2(17) | Y |  |  |
| 253 | VLR_ALIQ_INSS | VARCHAR2(7) | Y |  |  |
| 254 | VLR_RET_SERV | VARCHAR2(17) | Y |  |  |
| 255 | VLR_SERV_15 | VARCHAR2(17) | Y |  |  |
| 256 | VLR_SERV_20 | VARCHAR2(17) | Y |  |  |
| 257 | VLR_SERV_25 | VARCHAR2(17) | Y |  |  |
| 258 | IND_TP_PROC_ADJ_PRINC | VARCHAR2(1) | Y |  |  |
| 259 | NUM_PROC_ADJ_PRINC | VARCHAR2(21) | Y |  |  |
| 260 | COD_SUSP_PRINC | VARCHAR2(14) | Y |  |  |
| 261 | IND_TP_PROC_ADJ_ADIC | VARCHAR2(1) | Y |  |  |
| 262 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 263 | COD_SUSP_ADIC | VARCHAR2(14) | Y |  |  |
| 264 | VLR_IPI_DEV | VARCHAR2(17) | Y |  |  |
| 265 | COD_BENEFICIO | VARCHAR2(10) | Y |  |  |
| 266 | VLR_ABAT_NTRIBUTADO | VARCHAR2(17) | Y |  |  |
| 267 | VLR_CREDITO_MVA_SN | VARCHAR2(17) | Y |  |  |
| 268 | VLR_DESONERADO_ICMS | VARCHAR2(17) | Y |  | Informar o valor desonerado do ICMS.  Este valor será apresentado através de código da tabela 5.2 "Tabela de Informações Adicionais da Apuração - Valores Declaratórios" para apresentação nos registros E115 e 1925. Conforme Resolução Sefaz 13 de 14/02/2019 - RJ. |
| 269 | VLR_DIFERIDO_ICMS | VARCHAR2(17) | Y |  | Informar o valor diferido do ICMS.  Este valor será apresentado através de código da tabela 5.2 "Tabela de Informações Adicionais da Apuração - Valores Declaratórios" para apresentação nos registros E115 e 1925. Conforme Resolução Sefaz 13 de 14/02/2019 - RJ. |
| 270 | PST_ID | NUMBER | Y |  |  |
| 271 | VLR_EXC_BC_PIS | VARCHAR2(17) | Y |  |  |
| 272 | VLR_EXC_BC_COFINS | VARCHAR2(17) | Y |  |  |
| 273 | SEQ_ARQ | NUMBER(20) | Y |  |  |
| 274 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 275 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 276 | VLR_FECP_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 277 | COD_GRUPO_CCLASS | VARCHAR2(3) | Y |  |  |
| 278 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 279 | COD_AUTENTIC_NFE_ANT | VARCHAR2(44) | Y |  |  |
| 280 | NUM_ITEM_NFE_ANT | VARCHAR2(4) | Y |  |  |
| 281 | COD_CCLASS | VARCHAR2(7) | Y |  |  |
| 282 | CNPJ_OPER_LD | VARCHAR2(14) | Y |  |  |
| 283 | DAT_EXPIRA_CRED | VARCHAR2(8) | Y |  |  |
| 284 | IND_DEVOLUCAO | VARCHAR2(1) | Y |  |  |
| 285 | TIPO_ITEM | VARCHAR2(1) | Y |  |  |
| 286 | IND_PRODUTO_ACABADO | VARCHAR2(1) | Y |  |  |
| 287 | COD_PRODUTO_ACABADO | VARCHAR2(60) | Y |  |  |
| 288 | IND_NF_ANT | VARCHAR2(1) | Y |  |  |
| 289 | NUM_GUIA_RECOL | VARCHAR2(16) | Y |  |  |
| 290 | DAT_EMISSAO_GUIA | VARCHAR2(8) | Y |  |  |
| 291 | DAT_PAGTO_GUIA | VARCHAR2(8) | Y |  |  |
| 292 | COD_ESTADO_RECEITA_EST | VARCHAR2(2) | Y |  |  |
| 293 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 294 | VLR_GUIA_RECOL | VARCHAR2(17) | Y |  |  |
| 295 | CHAVE_SAFX08 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |
| 296 | QTD_PROD_20C | VARCHAR2(17) | Y |  |  |

**Indexes**:
- IX_CHAVE_SAFX08: (CHAVE_SAFX08)
- IX_SAFX08: (DAT_GRAVACAO)
- IX_SAFX08_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX08_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX08_LOTE: (NUM_LOTE)

---

## SAFX09

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 13 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 14 | VLR_SERVICO | VARCHAR2(17) | Y |  |  |
| 15 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 16 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 17 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 18 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 19 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 20 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 21 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 22 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 23 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 24 | VLR_SERVICO_CONV | VARCHAR2(18) | Y |  |  |
| 25 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 26 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 27 | DIF_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 28 | OBS_ICMS | VARCHAR2(45) | Y |  |  |
| 29 | COD_APUR_ICMS | VARCHAR2(5) | Y |  |  |
| 30 | VLR_ALIQ_IR | VARCHAR2(7) | Y |  |  |
| 31 | VLR_IR | VARCHAR2(17) | Y |  |  |
| 32 | VLR_ALIQ_ISS | VARCHAR2(7) | Y |  |  |
| 33 | VLR_ISS | VARCHAR2(17) | Y |  |  |
| 34 | TRIB_ICMS | CHAR(1) | Y |  |  |
| 35 | BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 36 | TRIB_IR | CHAR(1) | Y |  |  |
| 37 | BASE_IR | VARCHAR2(17) | Y |  |  |
| 38 | TRIB_ISS | CHAR(1) | Y |  |  |
| 39 | BASE_ISS | VARCHAR2(17) | Y |  |  |
| 40 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 41 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 42 | DAT_GRAVACAO | DATE | Y |  |  |
| 43 | COMPL_ISENCAO | VARCHAR2(5) | Y |  |  |
| 44 | VLR_BASE_CSLL | VARCHAR2(17) | Y |  |  |
| 45 | VLR_ALIQ_CSLL | VARCHAR2(7) | Y |  |  |
| 46 | VLR_CSLL | VARCHAR2(17) | Y |  |  |
| 47 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 48 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 49 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 50 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 51 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 52 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 53 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 54 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 55 | COD_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 56 | VLR_MAT_PROP | VARCHAR2(17) | Y |  |  |
| 57 | VLR_MAT_TERC | VARCHAR2(17) | Y |  |  |
| 58 | VLR_BASE_ISS_RETIDO | VARCHAR2(17) | Y |  |  |
| 59 | VLR_ISS_RETIDO | VARCHAR2(17) | Y |  |  |
| 60 | VLR_DEDUCAO_ISS | VARCHAR2(17) | Y |  |  |
| 61 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 62 | VLR_SUBEMPR_ISS | VARCHAR2(17) | Y |  |  |
| 63 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 64 | VLR_OUT_DESP | VARCHAR2(17) | Y |  |  |
| 65 | VLR_BASE_CIDE | VARCHAR2(17) | Y |  |  |
| 66 | VLR_ALIQ_CIDE | VARCHAR2(7) | Y |  |  |
| 67 | VLR_CIDE | VARCHAR2(17) | Y |  |  |
| 68 | VLR_COMISSAO | VARCHAR2(17) | Y |  |  |
| 69 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' | Indicador para verificar se os valores de PIS/COFINS estao destacados no documentos fiscal |
| 70 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 71 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 72 | VLR_PIS_EXP | VARCHAR2(17) | Y |  |  |
| 73 | VLR_PIS_TRIB | VARCHAR2(17) | Y |  |  |
| 74 | VLR_PIS_N_TRIB | VARCHAR2(17) | Y |  |  |
| 75 | VLR_COFINS_EXP | VARCHAR2(17) | Y |  |  |
| 76 | VLR_COFINS_TRIB | VARCHAR2(17) | Y |  |  |
| 77 | VLR_COFINS_N_TRIB | VARCHAR2(17) | Y |  |  |
| 78 | VLR_PIS_RETIDO | VARCHAR2(17) | Y |  |  |
| 79 | VLR_COFINS_RETIDO | VARCHAR2(17) | Y |  |  |
| 80 | DAT_LANC_PIS_COFINS | VARCHAR2(8) | Y |  |  |
| 81 | IND_PIS_COFINS_EXTEMP | VARCHAR2(1) | Y |  |  |
| 82 | IND_LOCAL_EXEC_SERV | VARCHAR2(1) | Y |  |  |
| 83 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 84 | VLR_BASE_INSS | VARCHAR2(17) | Y |  |  |
| 85 | VLR_ALIQ_INSS | VARCHAR2(7) | Y |  |  |
| 86 | VLR_INSS_RETIDO | VARCHAR2(17) | Y |  |  |
| 87 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 88 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 89 | VLR_ACRESCIMO | VARCHAR2(17) | Y |  |  |
| 90 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 91 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 92 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 93 | COD_NBS | VARCHAR2(9) | Y |  |  |
| 94 | VLR_TOT_ADIC | VARCHAR2(17) | Y |  |  |
| 95 | VLR_TOT_RET | VARCHAR2(17) | Y |  |  |
| 96 | VLR_DEDUCAO_NF | VARCHAR2(17) | Y |  |  |
| 97 | VLR_RET_NF | VARCHAR2(17) | Y |  |  |
| 98 | VLR_RET_SERV | VARCHAR2(17) | Y |  |  |
| 99 | VLR_ALIQ_ISS_RETIDO | VARCHAR2(7) | Y |  |  |
| 100 | COD_SIT_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 101 | VLR_N_RET_PRINC | VARCHAR2(17) | Y |  |  |
| 102 | VLR_N_RET_ADIC | VARCHAR2(17) | Y |  |  |
| 103 | VLR_DED_ALIM | VARCHAR2(17) | Y |  |  |
| 104 | VLR_DED_TRANS | VARCHAR2(17) | Y |  |  |
| 105 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 106 | NUM_PROC_ADJ_PRINC | VARCHAR2(21) | Y |  |  |
| 107 | COD_SUSP_PRINC | VARCHAR2(14) | Y |  |  |
| 108 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 109 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 110 | COD_SUSP_ADIC | VARCHAR2(14) | Y |  |  |
| 111 | VLR_SERV_15 | VARCHAR2(17) | Y |  |  |
| 112 | VLR_SERV_20 | VARCHAR2(17) | Y |  |  |
| 113 | VLR_SERV_25 | VARCHAR2(17) | Y |  |  |
| 114 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 115 | VLR_ABAT_NTRIBUTADO | VARCHAR2(17) | Y |  |  |
| 116 | COD_ATIV_RJ | VARCHAR2(7) | Y |  |  |
| 117 | PST_ID | NUMBER | Y |  |  |
| 118 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 119 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 120 | DSC_RESERVADO6 | VARCHAR2(17) | Y |  |  |
| 121 | DSC_RESERVADO7 | VARCHAR2(17) | Y |  |  |
| 122 | DSC_RESERVADO8 | VARCHAR2(17) | Y |  |  |
| 123 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 124 | SEQ_ARQ | NUMBER(20) | Y |  |  |
| 125 | CHAVE_SAFX09 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX09: (CHAVE_SAFX09)
- IX_SAFX09: (DAT_GRAVACAO)
- IX_SAFX09_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX09_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX09_LOTE: (NUM_LOTE)

---

## SAFX10

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 8 | NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 14 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 15 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 16 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 17 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 18 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 19 | SERIE_ITEM | VARCHAR2(15) | Y |  |  |
| 20 | QTD_MOVTO | VARCHAR2(17) | Y |  |  |
| 21 | PRECO_UNIT | VARCHAR2(18) | Y |  |  |
| 22 | PRECO_ITEM | VARCHAR2(17) | Y |  |  |
| 23 | CUSTO_UNIT | VARCHAR2(18) | Y |  |  |
| 24 | CUSTO_ITEM | VARCHAR2(17) | Y |  |  |
| 25 | COD_CONTA_CRED | VARCHAR2(70) | Y |  |  |
| 26 | COD_CONTA_DEBITO | VARCHAR2(70) | Y |  |  |
| 27 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 28 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 29 | COD_ENT_SAIDA | CHAR(1) | Y |  |  |
| 30 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 31 | OBS_ESTOQUE | VARCHAR2(45) | Y |  |  |
| 32 | DATA_ESCRITA_FIS | VARCHAR2(8) | Y |  |  |
| 33 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 34 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 35 | IND_INSUMO | VARCHAR2(1) | Y |  |  |
| 36 | COD_LEGENDA | VARCHAR2(5) | Y |  |  |
| 37 | NUM_ORDEM | VARCHAR2(30) | Y |  |  |
| 38 | NUM_DOCFIS_OFIC | VARCHAR2(12) | Y |  |  |
| 39 | SERIE_DOCFIS_OFIC | VARCHAR2(3) | Y |  |  |
| 40 | S_SERIE_DOCFIS_OFIC | VARCHAR2(2) | Y |  |  |
| 41 | DAT_GRAVACAO | DATE | Y |  |  |
| 42 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 43 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 44 | IND_TP_MOVTO | CHAR(1) | Y |  |  |
| 45 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 46 | IND_PRODUTO_RASTRO | VARCHAR2(1) | Y |  |  |
| 47 | COD_PRODUTO_RASTRO | VARCHAR2(60) | Y |  |  |
| 48 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 49 | DATA_DISP | VARCHAR2(8) | Y |  |  |
| 50 | IND_DOC_OPER | CHAR(1) | Y |  |  |
| 51 | IND_TP_DOC_INTERNO | VARCHAR2(30) | Y |  |  |
| 52 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 53 | IND_REDESIGNACAO | CHAR(1) | Y |  | Indicador de Redesignação ATO COTEPE - REG H220 |
| 54 | IND_PRODUTO_ORI | CHAR(1) | Y |  |  |
| 55 | COD_PRODUTO_ORI | VARCHAR2(60) | Y |  |  |
| 56 | VLR_CUSTO_DCA | VARCHAR2(17) | Y |  |  |
| 57 | VLR_OUT_TRIB_NCUMUL | VARCHAR2(17) | Y |  |  |
| 58 | COD_TP_LANCTO | VARCHAR2(6) | Y |  |  |
| 59 | VLR_ICMS_DCA | VARCHAR2(17) | Y |  |  |
| 60 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 61 | DSC_FINALIDADE | VARCHAR2(255) | Y |  |  |
| 62 | COD_TIPO_MOV_EST | VARCHAR2(2) | Y |  |  |
| 63 | COD_MEDIDA_ORI | VARCHAR2(8) | Y |  |  |
| 64 | COD_NIVEL_PRODUTO | VARCHAR2(3) | Y |  |  |
| 65 | QTD_INSUMO | VARCHAR2(17) | Y |  |  |
| 66 | PST_ID | NUMBER | Y |  |  |
| 67 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 68 | IND_CF | CHAR(1) | Y |  |  |
| 69 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 70 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 71 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 72 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 73 | CHAVE_SAFX10 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX10: (CHAVE_SAFX10)
- IX_SAFX10: (DAT_GRAVACAO)
- IX_SAFX10_1: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO)
- IX_SAFX10_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX10_LOTE: (NUM_LOTE)

---

## SAFX100

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 2 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 4 | DATA_PRODUTO | VARCHAR2(8) | Y |  |  |
| 5 | DAT_VIGENCIA_INI | VARCHAR2(8) | Y |  |  |
| 6 | DAT_VIGENCIA_FIM | VARCHAR2(8) | Y |  |  |
| 7 | ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 8 | PERC_BASE_RED_ICMS | VARCHAR2(7) | Y |  |  |
| 9 | VLR_BASE_ICMSS | VARCHAR2(17) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX100 | VARCHAR2(4000) | Y | NVL("COD_ESTADO",'@')\|\|NVL("IND_PRODUTO",'@')\|\|... |  |

**Indexes**:
- IX_CHAVE_SAFX100: (CHAVE_SAFX100)
- IX_SAFX100_02: (DAT_VIGENCIA_INI, COD_ESTADO)
- IX_SAFX100_LOTE: (NUM_LOTE)

---

## SAFX101

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
| 14 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | TIPO_LANCTO | CHAR(1) | Y |  | N - Normal; E - Encerramento |
| 17 | IND_PFJ_EMPRESA | CHAR(1) | Y |  |  |
| 18 | COD_PFJ_EMPRESA | VARCHAR2(14) | Y |  |  |
| 19 | DAT_LANCTO_EXTEMP | VARCHAR2(8) | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX101 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX101: (CHAVE_SAFX101)
- IX_SAFX101: (DAT_GRAVACAO)
- IX_SAFX101_LOTE: (NUM_LOTE)

---

## SAFX102

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | DATA_SALDO | VARCHAR2(8) | Y |  |  |
| 5 | VLR_SALDO_INI | VARCHAR2(17) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | VARCHAR2(17) | Y |  |  |
| 8 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 9 | VLR_TOT_CRE | VARCHAR2(17) | Y |  |  |
| 10 | VLR_TOT_DEB | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX102 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX102: (CHAVE_SAFX102)
- IX_SAFX102: (DAT_GRAVACAO)
- IX_SAFX102_LOTE: (NUM_LOTE)

---

## SAFX103

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_RE | VARCHAR2(15) | Y |  |  |
| 4 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 5 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 11 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 12 | DAT_EMISSAO | VARCHAR2(8) | Y |  |  |
| 13 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 14 | QTD_EXPORTADA | VARCHAR2(17) | Y |  |  |
| 15 | VLR_UNIT_PRODUTO | VARCHAR2(21) | Y |  |  |
| 16 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 17 | COD_RELAC | CHAR(1) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | IND_PROD_N_INDUSTR | CHAR(1) | Y |  |  |
| 20 | NUM_MEMO_EXP | VARCHAR2(50) | Y |  |  |
| 21 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 22 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 23 | IND_MOVTO | CHAR(1) | Y |  |  |
| 24 | IND_COMPROV_OPER | VARCHAR2(1) | Y |  |  |
| 25 | DAT_FISCAL_EXP | VARCHAR2(8) | Y |  |  |
| 26 | NUM_DOCFIS_EXP | VARCHAR2(12) | Y |  |  |
| 27 | SERIE_DOCFIS_EXP | VARCHAR2(3) | Y |  |  |
| 28 | NUM_DDE_EXP | VARCHAR2(14) | Y |  |  |
| 29 | COD_TP_LANCTO | VARCHAR2(6) | Y |  |  |
| 30 | PST_ID | NUMBER | Y |  |  |
| 31 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 32 | CHAVE_SAFX103 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX103: (CHAVE_SAFX103)
- IX_SAFX103: (DAT_GRAVACAO)
- IX_SAFX103_LOTE: (NUM_LOTE)

---

## SAFX104

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_REGISTRO | CHAR(1) | Y |  |  |
| 2 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | VALID_INICIAL | VARCHAR2(8) | Y |  |  |
| 6 | ALIQ_INTERNA | VARCHAR2(7) | Y |  |  |
| 7 | IND_PRODUTO_ASS | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO_ASS | VARCHAR2(60) | Y |  |  |
| 9 | MODELO_LIVRO | VARCHAR2(1) | Y | '3' |  |
| 10 | VALID_FINAL | VARCHAR2(8) | Y |  |  |
| 11 | PRC_REDUCAO_BC | VARCHAR2(7) | Y |  |  |
| 12 | RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 13 | RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 14 | RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 15 | RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 16 | RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 17 | RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 18 | RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 19 | RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 20 | ALIQ_FCP | VARCHAR2(7) | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 23 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 24 | DAT_GRAVACAO | DATE | Y |  |  |
| 25 | CHAVE_SAFX104 | VARCHAR2(4000) | Y | NVL("TIPO_REGISTRO",'@')\|\|NVL("COD_ESTADO",'@')... |  |

**Indexes**:
- IX_CHAVE_SAFX104: (CHAVE_SAFX104)
- IX_SAFX104_LOTE: (NUM_LOTE)

---

## SAFX105

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_CONSIDERA | VARCHAR2(2) | Y |  |  |
| 4 | ANO_CONSIDERA | VARCHAR2(4) | Y |  |  |
| 5 | DAT_REF_INI | VARCHAR2(8) | Y |  |  |
| 6 | DAT_REF_FIM | VARCHAR2(8) | Y |  |  |
| 7 | RECEITAS_SERV | VARCHAR2(17) | Y |  |  |
| 8 | EMPRESTIMOS_BANCARIOS | VARCHAR2(17) | Y |  |  |
| 9 | AUMENTO_CAPITAL_DINHEIRO | VARCHAR2(17) | Y |  |  |
| 10 | RECEITAS_FINANCEIRAS | VARCHAR2(17) | Y |  |  |
| 11 | OUTROS_INGRESSOS_RECURSO | VARCHAR2(17) | Y |  |  |
| 12 | PRO_LABORE | VARCHAR2(17) | Y |  |  |
| 13 | COMISSOES_SALARIOS_ORDENADOS | VARCHAR2(17) | Y |  |  |
| 14 | ENCARGOS_SOCIAIS | VARCHAR2(17) | Y |  |  |
| 15 | HONORARIOS_CONTABEIS | VARCHAR2(17) | Y |  |  |
| 16 | COMBUSTIVEIS_LUBRIFICANTES | VARCHAR2(17) | Y |  |  |
| 17 | TRIBUTOS_FEDERAIS | VARCHAR2(17) | Y |  |  |
| 18 | TRIBUTOS_ESTADUAIS | VARCHAR2(17) | Y |  |  |
| 19 | TRIBUTOS_MUNICIPAIS | VARCHAR2(17) | Y |  |  |
| 20 | AGUA_TELEFONE | VARCHAR2(17) | Y |  |  |
| 21 | ENERGIA | VARCHAR2(17) | Y |  |  |
| 22 | ALUGUEL_CONDOMINIO | VARCHAR2(17) | Y |  |  |
| 23 | SERVICOS_PROFISSIONAIS | VARCHAR2(17) | Y |  |  |
| 24 | SEGUROS | VARCHAR2(17) | Y |  |  |
| 25 | PAGAMENTO_EMPRESTIMOS | VARCHAR2(17) | Y |  |  |
| 26 | DESPESAS_BANCARIAS | VARCHAR2(17) | Y |  |  |
| 27 | OUTRAS_DESPESAS_PAGAMENTOS | VARCHAR2(17) | Y |  |  |
| 28 | SALDO_CAIXA_INI | VARCHAR2(17) | Y |  |  |
| 29 | SALDO_CAIXA_FIM | VARCHAR2(17) | Y |  |  |
| 30 | SALDO_BANCO_INI | VARCHAR2(17) | Y |  |  |
| 31 | SALDO_BANCO_FIM | VARCHAR2(17) | Y |  |  |
| 32 | FORNEC_A_PAGAR_INI | VARCHAR2(17) | Y |  |  |
| 33 | FORNEC_A_PAGAR_FIM | VARCHAR2(17) | Y |  |  |
| 34 | DUPLIC_A_RECEBER_INI | VARCHAR2(17) | Y |  |  |
| 35 | DUPLIC_A_RECEBER_FIM | VARCHAR2(17) | Y |  |  |
| 36 | DAT_GRAVACAO | DATE | Y |  |  |
| 37 | PST_ID | NUMBER | Y |  |  |
| 38 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 39 | CHAVE_SAFX105 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX105: (CHAVE_SAFX105)
- IX_SAFX105_LOTE: (NUM_LOTE)

---

## SAFX106

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_ENTREGA | VARCHAR2(8) | Y |  |  |
| 4 | NRO_AIDF | VARCHAR2(60) | Y |  |  |
| 5 | COD_SITUACAO | VARCHAR2(2) | Y |  |  |
| 6 | DAT_MOVTO | VARCHAR2(8) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 9 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 10 | NUM_CTR_DISP_INI | VARCHAR2(12) | Y |  |  |
| 11 | NUM_CTR_DISP_FIM | VARCHAR2(12) | Y |  |  |
| 12 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 13 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 15 | SUB_SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 16 | COD_OPERACAO | VARCHAR2(2) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 19 | DAT_AIDF | VARCHAR2(8) | Y |  |  |
| 20 | COD_ESTADO_AIDF | VARCHAR2(2) | Y |  |  |
| 21 | COD_MUNICIPIO_AIDF | VARCHAR2(5) | Y |  |  |
| 22 | COD_MODELO_GRAF | VARCHAR2(2) | Y |  |  |
| 23 | NUM_DOCFIS_GRAF | VARCHAR2(12) | Y |  |  |
| 24 | SERIE_DOCFIS_GRAF | VARCHAR2(3) | Y |  |  |
| 25 | SUBSERIE_DOCFIS_GRAF | VARCHAR2(2) | Y |  |  |
| 26 | PST_ID | NUMBER | Y |  |  |
| 27 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 28 | CHAVE_SAFX106 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX106: (CHAVE_SAFX106)
- IX_SAFX106_LOTE: (NUM_LOTE)

---

## SAFX107

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUMERO | VARCHAR2(20) | Y |  |  |
| 4 | DT_DISPONIB | VARCHAR2(8) | Y |  |  |
| 5 | HR_DISPONIB | VARCHAR2(6) | Y |  |  |
| 6 | TEL_ACESSO | VARCHAR2(15) | Y |  |  |
| 7 | NUM_LOTE_PIN | VARCHAR2(20) | Y |  |  |
| 8 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 10 | DATA_DOCFIS_REF | VARCHAR2(8) | Y |  |  |
| 11 | VLR_ATIVACAO | VARCHAR2(17) | Y |  |  |
| 12 | VLR_TOTAL | VARCHAR2(17) | Y |  |  |
| 13 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 14 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX107 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX107: (CHAVE_SAFX107)
- IX_SAFX107_LOTE: (NUM_LOTE)

---

## SAFX108

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | Y |  |  |
| 4 | COD_OP | VARCHAR2(30) | Y |  |  |
| 5 | IND_PRODUTO_OP | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO_OP | VARCHAR2(60) | Y |  |  |
| 7 | DT_INI_OP | VARCHAR2(8) | Y |  |  |
| 8 | DT_FIM_OP | VARCHAR2(8) | Y |  |  |
| 9 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 10 | QTD_PRODUZIDO | VARCHAR2(17) | Y |  |  |
| 11 | IND_APUR_CUSTO | CHAR(1) | Y |  |  |
| 12 | VLR_TOT_CUSTO | VARCHAR2(17) | Y |  |  |
| 13 | QTD_TRANSF | VARCHAR2(17) | Y |  |  |
| 14 | VLR_TRANSF | VARCHAR2(17) | Y |  |  |
| 15 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 16 | VLR_CUSTO_DCA | VARCHAR2(17) | Y |  |  |
| 17 | VLR_ICMS_DCA | VARCHAR2(17) | Y |  |  |
| 18 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | INDICA SE O REGISTRO FOI CARREGADO PELA FUNCIONALIDADE DO ATO COTEPE |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | COD_PROCESSO_PRODUCAO | VARCHAR2(10) | Y |  |  |
| 21 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 22 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 26 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 27 | DSC_RESERVADO6 | VARCHAR2(17) | Y |  |  |
| 28 | DSC_RESERVADO7 | VARCHAR2(17) | Y |  |  |
| 29 | DSC_RESERVADO8 | VARCHAR2(17) | Y |  |  |
| 30 | IND_TP_ORDEM | CHAR(1) | Y |  |  |
| 31 | QTD_ORIGEM | VARCHAR2(17) | Y |  |  |
| 32 | DT_SAIDA_ESTQ | VARCHAR2(8) | Y |  |  |
| 33 | QTD_SAIDA_ESTQ | VARCHAR2(17) | Y |  |  |
| 34 | DT_RET_ESTQ | VARCHAR2(8) | Y |  |  |
| 35 | QTD_RET_ESTQ | VARCHAR2(17) | Y |  |  |
| 36 | PST_ID | NUMBER | Y |  |  |
| 37 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 38 | CHAVE_SAFX108 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX108: (CHAVE_SAFX108)
- IX_SAFX108: (DAT_GRAVACAO)
- IX_SAFX108_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX108_LOTE: (NUM_LOTE)

---

## SAFX109

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | Y |  |  |
| 4 | COD_OP | VARCHAR2(30) | Y |  |  |
| 5 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | DT_SAIDA | VARCHAR2(8) | Y |  |  |
| 9 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 10 | QTD_PRODUZIDO | VARCHAR2(17) | Y |  |  |
| 11 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 12 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 15 | IND_PRODUTO_OP | CHAR(1) | Y |  |  |
| 16 | COD_PRODUTO_OP | VARCHAR2(60) | Y |  |  |
| 17 | VLR_CUSTO_DCA | VARCHAR2(17) | Y |  |  |
| 18 | VLR_ICMS_DCA | VARCHAR2(17) | Y |  |  |
| 19 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 20 | IND_INSUMO_SUBST | CHAR(1) | Y |  |  |
| 21 | COD_INSUMO_SUBST | VARCHAR2(60) | Y |  |  |
| 22 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 26 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 27 | DSC_RESERVADO6 | VARCHAR2(17) | Y |  |  |
| 28 | DSC_RESERVADO7 | VARCHAR2(17) | Y |  |  |
| 29 | DSC_RESERVADO8 | VARCHAR2(17) | Y |  |  |
| 30 | QTD_DESTINO | VARCHAR2(17) | Y |  |  |
| 31 | QTD_REPROC | VARCHAR2(17) | Y |  |  |
| 32 | QTD_RETORNADA | VARCHAR2(17) | Y |  |  |
| 33 | PST_ID | NUMBER | Y |  |  |
| 34 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 35 | CHAVE_SAFX109 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX109: (CHAVE_SAFX109)
- IX_SAFX109: (DAT_GRAVACAO)
- IX_SAFX109_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX109_LOTE: (NUM_LOTE)

---

## SAFX11

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | COD_TIPO_MOVPATR | VARCHAR2(3) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 7 | COD_INC | VARCHAR2(6) | Y |  |  |
| 8 | VLR_MOVTO | VARCHAR2(17) | Y |  |  |
| 9 | COD_INDICE | VARCHAR2(17) | Y |  |  |
| 10 | VLR_EM_INDICE | VARCHAR2(18) | Y |  |  |
| 11 | BASE_CM | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX11 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX11: (CHAVE_SAFX11)
- IX_SAFX11: (DAT_GRAVACAO)
- IX_SAFX11_LOTE: (NUM_LOTE)

---

## SAFX110

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO_DOCFIS | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO_DOCFIS | VARCHAR2(60) | Y |  |  |
| 14 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 15 | NUM_ROMANEIO | VARCHAR2(12) | Y |  |  |
| 16 | NUM_ITEM_ROMANEIO | VARCHAR2(5) | Y |  |  |
| 17 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 18 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 19 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 20 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 21 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 22 | PRECO_TOTAL | VARCHAR2(17) | Y |  |  |
| 23 | DAT_GRAVACAO | DATE | Y |  |  |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | CHAVE_SAFX110 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX110: (CHAVE_SAFX110)
- IX_SAFX110_LOTE: (NUM_LOTE)

---

## SAFX111

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRP_COMB | VARCHAR2(2) | Y |  |  |
| 2 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 3 | VALID_BASE_ST | VARCHAR2(8) | Y |  |  |
| 4 | IND_REGRA_BASE_ST | CHAR(1) | Y |  |  |
| 5 | VLR_REGRA_BASE_ST | VARCHAR2(11) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | VLR_REGR_REDUCAO_BASE | VARCHAR2(11) | Y |  |  |
| 8 | FATOR_CONV_VOLUME | VARCHAR2(7) | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX111 | VARCHAR2(4000) | Y | NVL("COD_GRP_COMB",'@')\|\|NVL("COD_ESTADO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX111: (CHAVE_SAFX111)
- IX_SAFX111_LOTE: (NUM_LOTE)

---

## SAFX112

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 13 | IND_ICOMPL_LANCTO | CHAR(1) | Y |  |  |
| 14 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | VINCULACAO | CHAR(1) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | DSC_INFO_FISCO | VARCHAR2(2000) | Y |  |  |
| 20 | DSC_INFO_CONTRIB | VARCHAR2(3000) | Y |  |  |
| 21 | CHAVE_SAFX112 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX112: (CHAVE_SAFX112)
- IX_SAFX112_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX112_LOTE: (NUM_LOTE)

---

## SAFX113

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 13 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 14 | DSC_COMP_AJUSTE | VARCHAR2(255) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 17 | ALIQUOTA_ICMS | VARCHAR2(7) | Y |  |  |
| 18 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_OUTROS | VARCHAR2(17) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX113 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX113: (CHAVE_SAFX113)
- IX_SAFX113_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX113_LOTE: (NUM_LOTE)

---

## SAFX114

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 13 | NUM_PROCESSO | VARCHAR2(60) | Y |  |  |
| 14 | ORIG_PROCESSO | CHAR(1) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX114 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX114: (CHAVE_SAFX114)
- IX_SAFX114_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX114_LOTE: (NUM_LOTE)

---

## SAFX115

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 13 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 14 | UF | VARCHAR2(2) | Y |  |  |
| 15 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 16 | COD_AUTEN_BANC | VARCHAR2(100) | Y |  |  |
| 17 | VLR_TOT_DOC_ARREC | VARCHAR2(17) | Y |  |  |
| 18 | DATA_VENC_DOC_ARREC | VARCHAR2(8) | Y |  |  |
| 19 | DATA_PGTO_DOC_ARREC | VARCHAR2(8) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX115 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX115: (CHAVE_SAFX115)
- IX_SAFX115_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX115_LOTE: (NUM_LOTE)

---

## SAFX116

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 13 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 15 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 16 | MOVTO_E_S_REF | CHAR(1) | Y |  |  |
| 17 | IND_FIS_JUR_REF | CHAR(1) | Y |  |  |
| 18 | COD_FIS_JUR_REF | VARCHAR2(14) | Y |  |  |
| 19 | DATA_FISCAL_REF | VARCHAR2(8) | Y |  |  |
| 20 | COD_MODELO_REF | VARCHAR2(2) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX116 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX116: (CHAVE_SAFX116)
- IX_SAFX116_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX116_LOTE: (NUM_LOTE)

---

## SAFX117

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 13 | COD_EQUIPAMENTO | VARCHAR2(9) | Y |  |  |
| 14 | NUM_DOC | VARCHAR2(12) | Y |  |  |
| 15 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 16 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | COD_FABRICACAO_ECF | VARCHAR2(21) | Y |  |  |
| 19 | NUM_CHAVE_CFE | VARCHAR2(80) | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX117 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX117: (CHAVE_SAFX117)
- IX_SAFX117_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX117_LOTE: (NUM_LOTE)

---

## SAFX118

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 13 | VIA_TRANSP | VARCHAR2(5) | Y |  |  |
| 14 | UF_COLETA | VARCHAR2(2) | Y |  |  |
| 15 | MUNIC_COLETA | VARCHAR2(5) | Y |  |  |
| 16 | CNPJ_COLETA | VARCHAR2(14) | Y |  |  |
| 17 | IE_COLETA | VARCHAR2(14) | Y |  |  |
| 18 | UF_ENTREGA | VARCHAR2(2) | Y |  |  |
| 19 | MUNIC_ENTREGA | VARCHAR2(5) | Y |  |  |
| 20 | CNPJ_ENTREGA | VARCHAR2(14) | Y |  |  |
| 21 | IE_ENTREGA | VARCHAR2(14) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX118 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX118: (CHAVE_SAFX118)
- IX_SAFX118_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX118_LOTE: (NUM_LOTE)

---

## SAFX119

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | NUM_FAB_LOTE | VARCHAR2(50) | Y |  |  |
| 17 | QTD_LOTE | VARCHAR2(17) | Y |  |  |
| 18 | DAT_FABRIC | VARCHAR2(8) | Y |  |  |
| 19 | DAT_VALIDADE | VARCHAR2(8) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX119 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX119: (CHAVE_SAFX119)
- IX_SAFX119_LOTE: (NUM_LOTE)

---

## SAFX12

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 4 | COD_INC | VARCHAR2(6) | Y |  |  |
| 5 | DATA_SUSPENSAO | VARCHAR2(8) | Y |  |  |
| 6 | DATA_RETORNO | VARCHAR2(8) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX12 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX12: (CHAVE_SAFX12)
- IX_SAFX12: (DAT_GRAVACAO)
- IX_SAFX12_LOTE: (NUM_LOTE)

---

## SAFX120

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | NUM_SERIE_FABRIC | VARCHAR2(50) | Y |  |  |
| 17 | DSC_COMPLEM | VARCHAR2(150) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX120 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX120: (CHAVE_SAFX120)
- IX_SAFX120_LOTE: (NUM_LOTE)

---

## SAFX121

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_BOMBA | VARCHAR2(10) | Y |  |  |
| 4 | DAT_LACRE | VARCHAR2(8) | Y |  |  |
| 5 | NUM_LACRE | VARCHAR2(20) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX121 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX121: (CHAVE_SAFX121)
- IX_SAFX121: (DAT_GRAVACAO)
- IX_SAFX121_LOTE: (NUM_LOTE)

---

## SAFX122

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_TANQUE | VARCHAR2(10) | Y |  |  |
| 4 | NUM_BOMBA | VARCHAR2(10) | Y |  |  |
| 5 | NUM_BICO | VARCHAR2(10) | Y |  |  |
| 6 | DAT_MOVTO | VARCHAR2(8) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX122 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX122: (CHAVE_SAFX122)
- IX_SAFX122: (DAT_GRAVACAO)
- IX_SAFX122_LOTE: (NUM_LOTE)

---

## SAFX123

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | NUM_TANQUE | VARCHAR2(10) | Y |  |  |
| 5 | QTD_ESTOQ_INI | VARCHAR2(17) | Y |  |  |
| 6 | QTD_ENTRADA | VARCHAR2(17) | Y |  |  |
| 7 | QTD_SAIDA | VARCHAR2(17) | Y |  |  |
| 8 | QTD_PERDA | VARCHAR2(17) | Y |  |  |
| 9 | QTD_GANHO | VARCHAR2(17) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX123 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX123: (CHAVE_SAFX123)
- IX_SAFX123: (DAT_GRAVACAO)
- IX_SAFX123_LOTE: (NUM_LOTE)

---

## SAFX124

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | NUM_BOMBA | VARCHAR2(10) | Y |  |  |
| 5 | NUM_BICO | VARCHAR2(10) | Y |  |  |
| 6 | NUM_SEQ | VARCHAR2(2) | Y |  |  |
| 7 | NUM_INTERV | VARCHAR2(12) | Y |  |  |
| 8 | MOT_INTERV | VARCHAR2(255) | Y |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 11 | CPF_RESP | VARCHAR2(11) | Y |  |  |
| 12 | QTD_CONT_INI | VARCHAR2(17) | Y |  |  |
| 13 | QTD_CONT_FINAL | VARCHAR2(17) | Y |  |  |
| 14 | QTD_AFERICAO | VARCHAR2(17) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | NOM_RESP | VARCHAR2(50) | Y |  |  |
| 17 | VLR_CONTABIL | VARCHAR2(17) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX124 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX124: (CHAVE_SAFX124)
- IX_SAFX124: (DAT_GRAVACAO)
- IX_SAFX124_LOTE: (NUM_LOTE)

---

## SAFX125

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | NUM_TANQUE | VARCHAR2(10) | Y |  |  |
| 17 | QTD_COMB | VARCHAR2(17) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX125 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX125: (CHAVE_SAFX125)
- IX_SAFX125: (DAT_GRAVACAO)
- IX_SAFX125_LOTE: (NUM_LOTE)

---

## SAFX126

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | VLR_TOT_CRED | VARCHAR2(17) | Y |  |  |
| 7 | VLR_TOT_DEB | VARCHAR2(17) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | VLR_FAT_ICMS | VARCHAR2(17) | Y |  |  |
| 10 | VLR_EST_ICMS | VARCHAR2(17) | Y |  |  |
| 11 | VLR_FAT_ISS | VARCHAR2(17) | Y |  |  |
| 12 | VLR_EST_ISS | VARCHAR2(17) | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX126 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX126: (CHAVE_SAFX126)
- IX_SAFX126: (DAT_GRAVACAO)
- IX_SAFX126_LOTE: (NUM_LOTE)

---

## SAFX127

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_OBRIGACAO | VARCHAR2(2) | Y |  |  |
| 2 | COD_ING_ATIVO | VARCHAR2(35) | Y |  |  |
| 3 | DSC_ING_ATIVO | VARCHAR2(100) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX127 | VARCHAR2(4000) | Y | NVL("TIPO_OBRIGACAO",'@')\|\|NVL("COD_ING_ATIVO",... |  |

**Indexes**:
- IX_CHAVE_SAFX127: (CHAVE_SAFX127)
- IX_SAFX127: (DAT_GRAVACAO)
- IX_SAFX127_LOTE: (NUM_LOTE)

---

## SAFX128

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 3 | COD_MEDIDA_ORIG | VARCHAR2(8) | Y |  |  |
| 4 | COD_MEDIDA_DEST | VARCHAR2(8) | Y |  |  |
| 5 | VLR_FATOR_CONV | VARCHAR2(17) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX128 | VARCHAR2(4000) | Y | NVL("IND_PRODUTO",'@')\|\|NVL("COD_PRODUTO",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX128: (CHAVE_SAFX128)
- IX_SAFX128: (DAT_GRAVACAO)
- IX_SAFX128_LOTE: (NUM_LOTE)

---

## SAFX129

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
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 18 | TIPO_LANCTO | VARCHAR2(2) | Y |  | N - Normal/Expurgo; F - Fiscal; TR - Transferencia de Saldos; TF - Transferencia de Saldos Fiscais;   TS- Transferencia de Saldos Societarios;  EF - Encerramento Fiscal; IF - Inicializacao de Saldo Fiscal e   IS - Inicializacao de Saldo Societario |
| 19 | IND_PFJ_EMPRESA | CHAR(1) | Y |  |  |
| 20 | COD_PFJ_EMPRESA | VARCHAR2(14) | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX129 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX129: (CHAVE_SAFX129)
- IX_SAFX129: (DAT_GRAVACAO)
- IX_SAFX129_LOTE: (NUM_LOTE)

---

## SAFX13

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 4 | COD_INC | VARCHAR2(6) | Y |  |  |
| 5 | VALID_BEM | VARCHAR2(8) | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 7 | COD_CONTA_CM | VARCHAR2(70) | Y |  |  |
| 8 | DATA_AQUIS | VARCHAR2(8) | Y |  |  |
| 9 | VLR_AQUIS | VARCHAR2(17) | Y |  |  |
| 10 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 11 | COD_CONTA_DEPR | VARCHAR2(70) | Y |  |  |
| 12 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 13 | COD_DESPESA | VARCHAR2(20) | Y |  |  |
| 14 | CODT_DOCTO | VARCHAR2(5) | Y |  |  |
| 15 | IDENT_SIT_BEM | VARCHAR2(3) | Y |  |  |
| 16 | COD_BEM_ORIG | VARCHAR2(60) | Y |  |  |
| 17 | COD_INC_ORIG | VARCHAR2(6) | Y |  |  |
| 18 | DATA_BAIXA | VARCHAR2(8) | Y |  |  |
| 19 | DATA_INI_CM | VARCHAR2(8) | Y |  |  |
| 20 | DATA_INI_DEPR | VARCHAR2(8) | Y |  |  |
| 21 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 22 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 23 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 24 | SERIE_BEM | VARCHAR2(15) | Y |  |  |
| 25 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 26 | TAXA_DEPR | VARCHAR2(8) | Y |  |  |
| 27 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 28 | VLR_EM_INDICE | VARCHAR2(18) | Y |  |  |
| 29 | DAT_GRAVACAO | DATE | Y |  |  |
| 30 | IND_NAT_BEM | CHAR(1) | Y |  |  |
| 31 | VLR_AQUIS_REAL | VARCHAR2(17) | Y |  |  |
| 32 | VLR_DEPR_ACUM | VARCHAR2(17) | Y |  |  |
| 33 | VLR_DEPR_LANC | VARCHAR2(17) | Y |  |  |
| 34 | IND_GERA_P7 | CHAR(1) | Y |  |  |
| 35 | TIPO_BEM | CHAR(1) | Y |  |  |
| 36 | VIDA_UTIL | VARCHAR2(3) | Y |  |  |
| 37 | IND_BEM_ORI_ATIVO | CHAR(1) | Y |  |  |
| 38 | DSC_FUNCAO | VARCHAR2(150) | Y |  |  |
| 39 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 40 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 41 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 42 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 43 | IND_COD_ALTERN | CHAR(1) | Y |  |  |
| 44 | IND_CRED_PIS_COFINS | CHAR(1) | Y |  |  |
| 45 | IND_PARCELA | VARCHAR2(3) | Y |  |  |
| 46 | IND_OPER_CRED | CHAR(1) | Y |  |  |
| 47 | COD_GRUPO_BEM | VARCHAR2(9) | Y |  |  |
| 48 | IND_UTIL_BEM | CHAR(1) | Y |  |  |
| 49 | VLR_DEP_AMORT_EXC | VARCHAR2(17) | Y |  |  |
| 50 | VLR_PARCELA_DEP_MES | VARCHAR2(17) | Y |  |  |
| 51 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 52 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 53 | COD_GRP_PROD | VARCHAR2(12) | Y |  |  |
| 54 | DATA_INI_CRED | VARCHAR2(8) | Y |  |  |
| 55 | NUM_PARC_APROP | VARCHAR2(3) | Y |  |  |
| 56 | DATA_CONCLUSAO_BRESULT | VARCHAR2(8) | Y |  |  |
| 57 | IND_IMP | VARCHAR2(1) | Y |  |  |
| 58 | IND_SERV_MERC | VARCHAR2(1) | Y |  |  |
| 59 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 60 | PST_ID | NUMBER | Y |  |  |
| 61 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 62 | CHAVE_SAFX13 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX13: (CHAVE_SAFX13)
- IX_SAFX13: (DAT_GRAVACAO)
- IX_SAFX13_LOTE: (NUM_LOTE)

---

## SAFX130

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 5 | NUM_DOCFIS_FIN | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | DATA_REF | VARCHAR2(8) | Y |  |  |
| 9 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 10 | IND_SITUACAO | CHAR(1) | Y |  |  |
| 11 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 14 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX130 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_130: (DAT_GRAVACAO)
- IX_CHAVE_SAFX130: (CHAVE_SAFX130)
- IX_SAFX130_LOTE: (NUM_LOTE)

---

## SAFX131

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | COD_TP_LANCTO | VARCHAR2(6) | Y |  |  |
| 9 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | DESC_HISTORICO | VARCHAR2(50) | Y |  |  |
| 14 | QTD_PRODUTO | VARCHAR2(17) | Y |  |  |
| 15 | VLR_PERC_RATEIO | VARCHAR2(7) | Y |  |  |
| 16 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 17 | VLR_OUT_CONTRIB | VARCHAR2(17) | Y |  |  |
| 18 | VLR_CUSTO_DCA | VARCHAR2(17) | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | CHAVE_SAFX131 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX131: (CHAVE_SAFX131)
- IX_SAFX131_LOTE: (NUM_LOTE)

---

## SAFX132

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_REFERENCIA | VARCHAR2(8) | Y |  |  |
| 4 | VLR_CUSTO_DCA | VARCHAR2(17) | Y |  |  |
| 5 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 6 | COD_PROCESSO_PRODUCAO | VARCHAR2(10) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX132 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX132: (CHAVE_SAFX132)
- IX_SAFX132_LOTE: (NUM_LOTE)

---

## SAFX133

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_INI_APUR | VARCHAR2(8) | Y |  |  |
| 4 | DAT_FIN_APUR | VARCHAR2(8) | Y |  |  |
| 5 | VLR_SALDO_INI | VARCHAR2(17) | Y |  |  |
| 6 | VLR_SOM_PARC | VARCHAR2(17) | Y |  |  |
| 7 | VLR_TRIB_EXP | VARCHAR2(17) | Y |  |  |
| 8 | VLR_TOTAL | VARCHAR2(17) | Y |  |  |
| 9 | IND_PER_SAI | VARCHAR2(11) | Y |  |  |
| 10 | VLR_ICMS_APROP | VARCHAR2(17) | Y |  |  |
| 11 | VLR_SOM_ICMS | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX133 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX133: (CHAVE_SAFX133)
- IX_SAFX133_LOTE: (NUM_LOTE)

---

## SAFX134

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_INI_APUR | VARCHAR2(8) | Y |  |  |
| 4 | DAT_FIN_APUR | VARCHAR2(8) | Y |  |  |
| 5 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 6 | COD_INC | VARCHAR2(6) | Y |  |  |
| 7 | DAT_MOV | VARCHAR2(8) | Y |  |  |
| 8 | COD_TIPO_MOV | VARCHAR2(2) | Y |  |  |
| 9 | VLR_ICMS_OP | VARCHAR2(17) | Y |  |  |
| 10 | VLR_ICMS_ST | VARCHAR2(17) | Y |  |  |
| 11 | VLR_ICMS_FRETE | VARCHAR2(17) | Y |  |  |
| 12 | VLR_ICMS_DIF | VARCHAR2(17) | Y |  |  |
| 13 | NUM_PARCELA | VARCHAR2(3) | Y |  |  |
| 14 | VLR_PARC_PASS | VARCHAR2(17) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX134 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX134: (CHAVE_SAFX134)
- IX_SAFX134_LOTE: (NUM_LOTE)

---

## SAFX135

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_INI_APUR | VARCHAR2(8) | Y |  |  |
| 4 | DAT_FIN_APUR | VARCHAR2(8) | Y |  |  |
| 5 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 6 | COD_INC | VARCHAR2(6) | Y |  |  |
| 7 | DAT_MOV | VARCHAR2(8) | Y |  |  |
| 8 | COD_TIPO_MOV | VARCHAR2(2) | Y |  |  |
| 9 | IND_EMIT | CHAR(1) | Y |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 12 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 13 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 15 | DAT_DOC | VARCHAR2(8) | Y |  |  |
| 16 | NUM_CHAVE_NFE | VARCHAR2(44) | Y |  |  |
| 17 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 18 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 19 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 23 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 24 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 25 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 26 | VLR_ICMS_ST | VARCHAR2(17) | Y |  |  |
| 27 | VLR_ICMS_FRETE | VARCHAR2(17) | Y |  |  |
| 28 | VLR_ICMS_DIFAL | VARCHAR2(17) | Y |  |  |
| 29 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 30 | CHAVE_SAFX135 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX135: (CHAVE_SAFX135)
- IX_SAFX135_LOTE: (NUM_LOTE)

---

## SAFX136

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_INI_APUR | VARCHAR2(8) | Y |  |  |
| 4 | DAT_FIN_APUR | VARCHAR2(8) | Y |  |  |
| 5 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 6 | COD_INC | VARCHAR2(6) | Y |  |  |
| 7 | DAT_MOV | VARCHAR2(8) | Y |  |  |
| 8 | COD_TIPO_MOV | VARCHAR2(2) | Y |  |  |
| 9 | DAT_INI_PARC | VARCHAR2(8) | Y |  |  |
| 10 | DAT_FIN_PARC | VARCHAR2(8) | Y |  |  |
| 11 | NUM_PARCELA | VARCHAR2(3) | Y |  |  |
| 12 | VLR_PARC_PASS | VARCHAR2(17) | Y |  |  |
| 13 | VLR_TRIB_OC | VARCHAR2(17) | Y |  |  |
| 14 | VLR_TOTAL | VARCHAR2(17) | Y |  |  |
| 15 | IND_PER_SAI | VARCHAR2(11) | Y |  |  |
| 16 | VLR_PARC_APROP | VARCHAR2(17) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX136 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX136: (CHAVE_SAFX136)
- IX_SAFX136_LOTE: (NUM_LOTE)

---

## SAFX137

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 8 | NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 14 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 15 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 16 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 17 | IND_PRODUTO_PERDA | CHAR(1) | Y |  |  |
| 18 | COD_PRODUTO_PERDA | VARCHAR2(60) | Y |  |  |
| 19 | QTD_RESULT_PERDA | VARCHAR2(17) | Y |  |  |
| 20 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | PST_ID | NUMBER | Y |  |  |
| 23 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 24 | CHAVE_SAFX137 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX137: (CHAVE_SAFX137)
- IX_SAFX137: (DAT_GRAVACAO)
- IX_SAFX137_LOTE: (NUM_LOTE)

---

## SAFX138

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 13 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 14 | NUM_DOC | VARCHAR2(12) | Y |  |  |
| 15 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 16 | NUM_DOC_ITEM | VARCHAR2(12) | Y |  |  |
| 17 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 18 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 19 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 20 | NUM_RELATORIO | VARCHAR2(6) | Y |  |  |
| 21 | DATA_RELATORIO | VARCHAR2(8) | Y |  |  |
| 22 | CNPJ_CGC | VARCHAR2(14) | Y |  |  |
| 23 | VLR_MERCADORIA | VARCHAR2(17) | Y |  |  |
| 24 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 25 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 26 | DAT_GRAVACAO | DATE | Y |  |  |
| 27 | PST_ID | NUMBER | Y |  |  |
| 28 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 29 | CHAVE_SAFX138 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_138: (DAT_GRAVACAO)
- IX_CHAVE_SAFX138: (CHAVE_SAFX138)
- IX_SAFX138_LOTE: (NUM_LOTE)

---

## SAFX139

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | Y |  |  |
| 4 | COD_OP | VARCHAR2(30) | Y |  |  |
| 5 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 6 | IND_PRODUTO_OP | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO_OP | VARCHAR2(60) | Y |  |  |
| 8 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 9 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 10 | DATA_SAIDA | VARCHAR2(8) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | QTD_UTILIZADA | VARCHAR2(17) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX139 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX139: (CHAVE_SAFX139)
- IX_SAFX139_LOTE: (NUM_LOTE)

---

## SAFX14

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 5 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 6 | IND_FOLHA | VARCHAR2(2) | Y |  |  |
| 7 | VLR_BRUTO | VARCHAR2(17) | Y |  |  |
| 8 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 9 | VLR_OUTROS_DESC | VARCHAR2(17) | Y |  |  |
| 10 | VLR_DEDUCAO_TAB | VARCHAR2(17) | Y |  |  |
| 11 | VLR_BASE_IRRF | VARCHAR2(17) | Y |  |  |
| 12 | VLR_IRRF | VARCHAR2(17) | Y |  |  |
| 13 | VLR_DIF_IRRF | VARCHAR2(17) | Y |  |  |
| 14 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX14 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX14: (CHAVE_SAFX14)
- IX_SAFX14: (DAT_GRAVACAO)
- IX_SAFX14_LOTE: (NUM_LOTE)

---

## SAFX140

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_NORM_DEV | CHAR(1) | Y |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 8 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 10 | DSC_HISTORICO | VARCHAR2(255) | Y |  |  |
| 11 | IND_PRODUTO_RES | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO_RES | VARCHAR2(60) | Y |  |  |
| 13 | COD_OP | VARCHAR2(30) | Y |  |  |
| 14 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX140 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX140: (CHAVE_SAFX140)
- IX_SAFX140_LOTE: (NUM_LOTE)

---

## SAFX141

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_NORM_DEV | CHAR(1) | Y |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | IND_PRODUTO_RES | CHAR(1) | Y |  |  |
| 10 | COD_PRODUTO_RES | VARCHAR2(60) | Y |  |  |
| 11 | IND_PRODUTO_AGREG | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO_AGREG | VARCHAR2(60) | Y |  |  |
| 13 | IND_MAT_MAO | CHAR(1) | Y |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COD_TP_LANCTO | VARCHAR2(6) | Y |  |  |
| 16 | VLR_CUSTO_DCA | VARCHAR2(17) | Y |  |  |
| 17 | VLR_ICMS_DCA | VARCHAR2(17) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX141 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX141: (CHAVE_SAFX141)
- IX_SAFX141_LOTE: (NUM_LOTE)

---

## SAFX142

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 2 | UN_VENDA | VARCHAR2(8) | Y |  |  |
| 3 | FATOR_VENDA | VARCHAR2(9) | Y |  |  |
| 4 | TIPO_TRIBUTACAO_IPI | VARCHAR2(1) | Y |  |  |
| 5 | ALIQUOTA_IPI | VARCHAR2(5) | Y |  |  |
| 6 | VALOR_IPI | VARCHAR2(13) | Y |  |  |
| 7 | CATEGORIA_ICMS | VARCHAR2(14) | Y |  |  |
| 8 | TIPO_TRIBUTACAO_ISS | VARCHAR2(1) | Y |  |  |
| 9 | VALOR_UNIT_BASE_ISS | VARCHAR2(12) | Y |  |  |
| 10 | ALIQUOTA_ISS | VARCHAR2(5) | Y |  |  |
| 11 | CLASSIF_ISS | VARCHAR2(1) | Y |  |  |
| 12 | TAB_SUBST_TRIB | VARCHAR2(5) | Y |  |  |
| 13 | CODIGO_DCR | VARCHAR2(15) | Y |  |  |
| 14 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 15 | CUBAGEM | VARCHAR2(8) | Y |  |  |
| 16 | PESO_LIQUIDO | VARCHAR2(13) | Y |  |  |
| 17 | PESO_BRUTO | VARCHAR2(13) | Y |  |  |
| 18 | SUBST_TRIB_ENTRADA | VARCHAR2(1) | Y |  |  |
| 19 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 20 | CUSTO | VARCHAR2(17) | Y |  |  |
| 21 | PRECO_TRANSF | VARCHAR2(17) | Y |  |  |
| 22 | PRECO_VENDA | VARCHAR2(17) | Y |  |  |
| 23 | DAT_GRAVACAO | DATE | Y |  |  |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 26 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 27 | CHAVE_SAFX142 | VARCHAR2(4000) | Y | NVL("COD_PRODUTO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX142: (CHAVE_SAFX142)
- IX_SAFX142_LOTE: (NUM_LOTE)

---

## SAFX143

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | VARCHAR2(8) | N |  |  |
| 4 | IND_PRODUTO | VARCHAR2(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 7 | VLR_CUSTO_PRODUCAO | VARCHAR2(17) | Y |  |  |
| 8 | VLR_CUSTO_ESTOQUE | VARCHAR2(17) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX143 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX143: (CHAVE_SAFX143)
- IX_SAFX143_LOTE: (NUM_LOTE)

---

## SAFX144

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_SIT_TRIB_PIS | VARCHAR2(2) | Y |  |  |
| 4 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 5 | COD_SIT_TRIB_COFINS | VARCHAR2(2) | Y |  |  |
| 6 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 7 | COD_REC_DED_EXC | VARCHAR2(5) | Y |  |  |
| 8 | COD_ATRIBUTO | VARCHAR2(3) | Y |  |  |
| 9 | COD_REC_DED_EXC_COMPL | VARCHAR2(20) | Y |  |  |
| 10 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 11 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | DAT_VIG_INI | VARCHAR2(8) | Y |  |  |
| 14 | DAT_VIG_FIM | VARCHAR2(8) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX144 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX144: (CHAVE_SAFX144)
- IX_SAFX144_LOTE: (NUM_LOTE)

---

## SAFX145

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_REC_RET | VARCHAR2(8) | Y |  |  |
| 4 | IND_NAT_REC | CHAR(1) | Y |  |  |
| 5 | COD_RET_FONTE | VARCHAR2(2) | Y |  |  |
| 6 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | VLR_RECEBIDO | VARCHAR2(19) | Y |  |  |
| 9 | VLR_TOT_RET_FONTE | VARCHAR2(17) | Y |  |  |
| 10 | VLR_RET_FONTE_PIS | VARCHAR2(17) | Y |  |  |
| 11 | VLR_RET_FONTE_COFINS | VARCHAR2(17) | Y |  |  |
| 12 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 13 | IND_COND_PJ_DECL | CHAR(1) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 18 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 19 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 20 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 21 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 22 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | CHAVE_SAFX145 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX145: (CHAVE_SAFX145)
- IX_SAFX145_LOTE: (NUM_LOTE)

---

## SAFX146

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_OBRIG | VARCHAR2(2) | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO_INI | VARCHAR2(60) | Y |  |  |
| 6 | COD_PRODUTO_FIM | VARCHAR2(60) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | COD_GRP_INCENT | VARCHAR2(5) | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX146 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX146: (CHAVE_SAFX146)
- IX_SAFX146_LOTE: (NUM_LOTE)

---

## SAFX147

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | DATA_OPER | VARCHAR2(8) | Y |  |  |
| 9 | VLR_OPER | VARCHAR2(17) | Y |  |  |
| 10 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 11 | VLR_ALIQ_PIS | VARCHAR2(12) | Y |  |  |
| 12 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 13 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 14 | VLR_ALIQ_COFINS | VARCHAR2(12) | Y |  |  |
| 15 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 16 | IND_ORIGEM_CRED | VARCHAR2(2) | Y |  |  |
| 17 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 18 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 19 | DESC_COMPL | VARCHAR2(255) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | NUM_DOCTO | VARCHAR2(12) | Y |  |  |
| 22 | SERIE | VARCHAR2(3) | Y |  |  |
| 23 | SUB_SERIE | VARCHAR2(3) | Y |  |  |
| 24 | NUM_LANCTO | VARCHAR2(40) | Y |  |  |
| 25 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 26 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 27 | PST_ID | NUMBER | Y |  |  |
| 28 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 29 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 30 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 31 | CHAVE_SAFX147 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX147: (CHAVE_SAFX147)
- IX_SAFX147_LOTE: (NUM_LOTE)

---

## SAFX148

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_OPER_CRED | CHAR(1) | Y |  |  |
| 4 | COD_GRUPO_BEM | VARCHAR2(9) | Y |  |  |
| 5 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 6 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 7 | DATA_LANCTO | VARCHAR2(8) | Y |  |  |
| 8 | IND_ORIGEM_CRED_BEM | CHAR(1) | Y |  |  |
| 9 | IND_UTIL_BEM | CHAR(1) | Y |  |  |
| 10 | VLR_DEP_AMORT | VARCHAR2(17) | Y |  |  |
| 11 | VLR_DEP_AMORT_EXC | VARCHAR2(17) | Y |  |  |
| 12 | MES_ANO_AQUIS_BEM | VARCHAR2(6) | Y |  |  |
| 13 | VLR_BEM_ATIVO_IMOB | VARCHAR2(17) | Y |  |  |
| 14 | VLR_PARCELA_DEP_MES | VARCHAR2(17) | Y |  |  |
| 15 | VLR_BASE_CRED_PISPASEP | VARCHAR2(17) | Y |  |  |
| 16 | IND_PARCELA | CHAR(1) | Y |  |  |
| 17 | DESC_COMPL_BEM | VARCHAR2(255) | Y |  |  |
| 18 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 19 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_ALIQ_PIS | VARCHAR2(12) | Y |  |  |
| 21 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 22 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 23 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 24 | VLR_ALIQ_COFINS | VARCHAR2(12) | Y |  |  |
| 25 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 26 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 27 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 28 | DAT_GRAVACAO | DATE | Y |  |  |
| 29 | IND_CREDPIS_MSAF | CHAR(1) | Y |  |  |
| 30 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 31 | PST_ID | NUMBER | Y |  |  |
| 32 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 33 | NUM_PARC_CREDPIS | VARCHAR2(3) | Y |  |  |
| 34 | DATA_BAIXA | VARCHAR2(8) | Y |  |  |
| 35 | IND_MOTIVO_BAIXA | VARCHAR2(1) | Y |  |  |
| 36 | CHAVE_SAFX148 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX148: (CHAVE_SAFX148)
- IX_SAFX148_LOTE: (NUM_LOTE)

---

## SAFX149

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_UNID_IMOB | VARCHAR2(11) | Y |  |  |
| 4 | DATA_VENDA_UNID_IMOB | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_OPERACAO | VARCHAR2(2) | Y |  |  |
| 6 | NUM_CONTRATO | VARCHAR2(90) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | INF_COMPL | VARCHAR2(90) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX149 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX149: (CHAVE_SAFX149)
- IX_SAFX149_LOTE: (NUM_LOTE)

---

## SAFX15

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | DATA_FUNC | VARCHAR2(8) | Y |  |  |
| 5 | NOME | VARCHAR2(70) | Y |  |  |
| 6 | COD_NACAO | VARCHAR2(2) | Y |  |  |
| 7 | DATA_ADMISSAO | VARCHAR2(8) | Y |  |  |
| 8 | COD_FUNCAO | VARCHAR2(10) | Y |  |  |
| 9 | SEXO | CHAR(1) | Y |  |  |
| 10 | MUNICIPIO_NASC | VARCHAR2(30) | Y |  |  |
| 11 | COD_UF_NATURAL | VARCHAR2(2) | Y |  |  |
| 12 | CPF | VARCHAR2(14) | Y |  |  |
| 13 | COD_ESTADO_CIVIL | CHAR(1) | Y |  |  |
| 14 | COD_INSTRUCAO | VARCHAR2(2) | Y |  |  |
| 15 | IND_PIS_PASEP | CHAR(1) | Y |  |  |
| 16 | PIS_PASEP | VARCHAR2(11) | Y |  |  |
| 17 | DATA_PIS_PASEP | VARCHAR2(8) | Y |  |  |
| 18 | CART_PROF | VARCHAR2(11) | Y |  |  |
| 19 | SERIE_CART_PROF | VARCHAR2(7) | Y |  |  |
| 20 | COD_UF_CART_PROF | VARCHAR2(2) | Y |  |  |
| 21 | DATA_EXP_CART_PROF | VARCHAR2(8) | Y |  |  |
| 22 | VALID_CART_PROF | VARCHAR2(8) | Y |  |  |
| 23 | DATA_NASC | VARCHAR2(8) | Y |  |  |
| 24 | NOME_PAI | VARCHAR2(50) | Y |  |  |
| 25 | NOME_MAE | VARCHAR2(50) | Y |  |  |
| 26 | CART_IDENTIDADE | VARCHAR2(15) | Y |  |  |
| 27 | COD_UF_CART_IDEN | VARCHAR2(2) | Y |  |  |
| 28 | DATA_EMIS_CART_ID | VARCHAR2(8) | Y |  |  |
| 29 | ORGAO_EMISSOR | VARCHAR2(10) | Y |  |  |
| 30 | VALID_CART_IDENT | VARCHAR2(8) | Y |  |  |
| 31 | TIPO_VISTO | VARCHAR2(2) | Y |  |  |
| 32 | COD_CONSELHO | VARCHAR2(10) | Y |  |  |
| 33 | NUM_REG_CONSELHO | VARCHAR2(10) | Y |  |  |
| 34 | DATA_REG_CONSELHO | VARCHAR2(8) | Y |  |  |
| 35 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 36 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 37 | COMPL_ENDERECO | VARCHAR2(10) | Y |  |  |
| 38 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 39 | MUNICIPIO | VARCHAR2(30) | Y |  |  |
| 40 | CEP | VARCHAR2(8) | Y |  |  |
| 41 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 42 | ANO_CHEGADA | VARCHAR2(4) | Y |  |  |
| 43 | COD_ADMISSAO | VARCHAR2(1) | Y |  |  |
| 44 | COD_CAUSA_DESLIG | VARCHAR2(2) | Y |  |  |
| 45 | DATA_DEMISSAO | VARCHAR2(8) | Y |  |  |
| 46 | COD_VINCULO_EMP | VARCHAR2(2) | Y |  |  |
| 47 | DATA_OPCAO | VARCHAR2(8) | Y |  |  |
| 48 | JORNADA_SEMANAL | VARCHAR2(4) | Y |  |  |
| 49 | COD_TURNO | VARCHAR2(5) | Y |  |  |
| 50 | COD_TIPO_SALARIO | VARCHAR2(1) | Y |  |  |
| 51 | SALARIO_BASE | VARCHAR2(17) | Y |  |  |
| 52 | ADIC_PERICUL | VARCHAR2(5) | Y |  |  |
| 53 | ADIC_INSALUBRIDADE | VARCHAR2(5) | Y |  |  |
| 54 | ADIC_OUTROS | VARCHAR2(5) | Y |  |  |
| 55 | NUM_DEPEND | VARCHAR2(2) | Y |  |  |
| 56 | NUM_REGISTRO | VARCHAR2(14) | Y |  |  |
| 57 | NUM_MATRICULA | VARCHAR2(8) | Y |  |  |
| 58 | COD_CBO | VARCHAR2(10) | Y |  |  |
| 59 | COD_SINDICATO | VARCHAR2(5) | Y |  |  |
| 60 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 61 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 62 | DAT_GRAVACAO | DATE | Y |  |  |
| 63 | NUM_DEP_SAL_FAM | VARCHAR2(2) | Y |  |  |
| 64 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  |  |
| 65 | DATA_VALID | VARCHAR2(8) | Y |  |  |
| 66 | E_MAIL | VARCHAR2(50) | Y |  |  |
| 67 | OCORRENCIA_TRAB | VARCHAR2(2) | Y |  |  |
| 68 | IND_ESTAGIARIO | CHAR(1) | Y |  |  |
| 69 | MES_ANO_SAIDA_PAIS | VARCHAR2(6) | Y |  |  |
| 70 | MES_ANO_RET_PAIS | VARCHAR2(6) | Y |  |  |
| 71 | DATA_MOLESTIA | VARCHAR2(8) | Y |  |  |
| 72 | COD_OPER_SAUDE | VARCHAR2(4) | Y |  |  |
| 73 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 74 | NUM_ID_FISCAL | VARCHAR2(30) | Y |  |  |
| 75 | DDD | VARCHAR2(4) | Y |  |  |
| 76 | TELEFONE | VARCHAR2(11) | Y |  |  |
| 77 | DSC_PROVINCIA_EX | VARCHAR2(40) | Y |  |  |
| 78 | PST_ID | NUMBER | Y |  |  |
| 79 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 80 | CHAVE_SAFX15 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX15: (CHAVE_SAFX15)
- IX_SAFX15: (DAT_GRAVACAO)
- IX_SAFX15_LOTE: (NUM_LOTE)

---

## SAFX150

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_UNID_IMOB | VARCHAR2(11) | Y |  |  |
| 4 | DATA_VENDA_UNID_IMOB | VARCHAR2(8) | Y |  |  |
| 5 | COMPETENCIA | VARCHAR2(6) | Y |  |  |
| 6 | VLR_TOT_VENDA_UNID_IMOB | VARCHAR2(17) | Y |  |  |
| 7 | VLR_REC_ACUM_MES_ANT | VARCHAR2(17) | Y |  |  |
| 8 | VLR_TOT_REC_MES_ESCRIT | VARCHAR2(17) | Y |  |  |
| 9 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 10 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 11 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 12 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 13 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 14 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 15 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 16 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX150 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX150: (CHAVE_SAFX150)
- IX_SAFX150_LOTE: (NUM_LOTE)

---

## SAFX151

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_UNID_IMOB | VARCHAR2(11) | Y |  |  |
| 4 | DATA_VENDA_UNID_IMOB | VARCHAR2(8) | Y |  |  |
| 5 | COMPETENCIA | VARCHAR2(6) | Y |  |  |
| 6 | VLR_TOT_CUSTO_MES_ANT | VARCHAR2(17) | Y |  |  |
| 7 | VLR_TOT_CUSTO_MES | VARCHAR2(17) | Y |  |  |
| 8 | VLR_PARC_S_CRED_ACUM | VARCHAR2(17) | Y |  |  |
| 9 | VLR_BASE_CRED_CUSTO | VARCHAR2(17) | Y |  |  |
| 10 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 11 | VLR_TOT_CRED_ACUM_PIS | VARCHAR2(17) | Y |  |  |
| 12 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 13 | VLR_PARC_CRED_DESC_PIS | VARCHAR2(17) | Y |  |  |
| 14 | VLR_PARC_ADESC_PIS | VARCHAR2(17) | Y |  |  |
| 15 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 16 | VLR_TOT_CRED_ACUM_COFINS | VARCHAR2(17) | Y |  |  |
| 17 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 18 | VLR_PARC_CRED_DESC_COFINS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_PARC_ADESC_COFINS | VARCHAR2(17) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX151 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX151: (CHAVE_SAFX151)
- IX_SAFX151_LOTE: (NUM_LOTE)

---

## SAFX152

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_UNID_IMOB | VARCHAR2(11) | Y |  |  |
| 4 | DATA_VENDA_UNID_IMOB | VARCHAR2(8) | Y |  |  |
| 5 | COMPETENCIA | VARCHAR2(6) | Y |  |  |
| 6 | VLR_TOT_CUSTO_ORC | VARCHAR2(17) | Y |  |  |
| 7 | VLR_AQ_SERV_NPAG_CONTRIB | VARCHAR2(17) | Y |  |  |
| 8 | VLR_BASE_CRED_ORC | VARCHAR2(17) | Y |  |  |
| 9 | VLR_BASE_CRED_ORC_PROP | VARCHAR2(17) | Y |  |  |
| 10 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 11 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 12 | VLR_CRED_UTIL_PIS | VARCHAR2(17) | Y |  |  |
| 13 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 14 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 15 | VLR_CRED_UTIL_COFINS | VARCHAR2(17) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX152 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX152: (CHAVE_SAFX152)
- IX_SAFX152_LOTE: (NUM_LOTE)

---

## SAFX153

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_PRODUCAO | VARCHAR2(8) | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 7 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 10 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 11 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 12 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 13 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 14 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 15 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 16 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 17 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX153 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX153: (CHAVE_SAFX153)
- IX_SAFX153_LOTE: (NUM_LOTE)

---

## SAFX154

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_PRODUCAO | VARCHAR2(8) | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | DAT_CONSUMO | VARCHAR2(8) | Y |  |  |
| 7 | IND_PRODUTO_INS | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO_INS | VARCHAR2(60) | Y |  |  |
| 9 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 10 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | IND_PRODUTO_SUB | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO_SUB | VARCHAR2(60) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 17 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 18 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 19 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 20 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 21 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 22 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | CHAVE_SAFX154 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX154: (CHAVE_SAFX154)
- IX_SAFX154_LOTE: (NUM_LOTE)

---

## SAFX155

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | NUM_ORDEM | VARCHAR2(5) | Y |  |  |
| 13 | NUM_DOCFIS_MODAL | VARCHAR2(9) | Y |  |  |
| 14 | SERIE_DOCFIS_MODAL | VARCHAR2(4) | Y |  |  |
| 15 | SUB_SERIE_DOCFIS_MODAL | VARCHAR2(3) | Y |  |  |
| 16 | COD_MODELO_MODAL | VARCHAR2(2) | Y |  |  |
| 17 | DATA_EMISSAO_MODAL | VARCHAR2(8) | Y |  |  |
| 18 | VLR_TOTAL_MODAL | VARCHAR2(17) | Y |  |  |
| 19 | CNPJ_CPF_EMIT | VARCHAR2(14) | Y |  |  |
| 20 | UF_EMIT | VARCHAR2(2) | Y |  |  |
| 21 | IE_EMIT | VARCHAR2(14) | Y |  |  |
| 22 | UF_ORIG | VARCHAR2(2) | Y |  |  |
| 23 | COD_MUNIC_ORIG | VARCHAR2(7) | Y |  |  |
| 24 | CNPJ_CPF_TOM | VARCHAR2(14) | Y |  |  |
| 25 | UF_TOM | VARCHAR2(2) | Y |  |  |
| 26 | IE_TOM | VARCHAR2(14) | Y |  |  |
| 27 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 28 | COD_MUNIC_DEST | VARCHAR2(7) | Y |  |  |
| 29 | DAT_GRAVACAO | DATE | Y |  |  |
| 30 | PST_ID | NUMBER | Y |  |  |
| 31 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 32 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 33 | CHAVE_SAFX155 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX155: (CHAVE_SAFX155)
- IX_SAFX155_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX155_LOTE: (NUM_LOTE)

---

## SAFX156

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 4 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 5 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX156 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX156: (CHAVE_SAFX156)
- IX_SAFX156_LOTE: (NUM_LOTE)

---

## SAFX157

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_ESPECIE | VARCHAR2(3) | Y |  |  |
| 13 | COD_OBRA_ORIGEM | VARCHAR2(15) | Y |  |  |
| 14 | COD_OBRA_DESTINO | VARCHAR2(15) | Y |  |  |
| 15 | VLR_USO_CONSUMO | VARCHAR2(15) | Y |  |  |
| 16 | VLR_INCORPORADO | VARCHAR2(15) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | CHAVE_SAFX157 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX157: (CHAVE_SAFX157)
- IX_SAFX157_LOTE: (NUM_LOTE)

---

## SAFX158

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_BEM_PATR | CHAR(1) | Y |  |  |
| 13 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 14 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 15 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 16 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 17 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 18 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 19 | DAT_LANC_PIS_COFINS | VARCHAR2(8) | Y |  |  |
| 20 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 21 | IND_NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 22 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 23 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 24 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 25 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 26 | QTD_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 27 | VLR_ALIQ_PIS_R | VARCHAR2(19) | Y |  |  |
| 28 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 29 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 30 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 31 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 32 | QTD_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 33 | VLR_ALIQ_COFINS_R | VARCHAR2(19) | Y |  |  |
| 34 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 35 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 36 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 37 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 38 | DAT_GRAVACAO | DATE | Y |  |  |
| 39 | PST_ID | NUMBER | Y |  |  |
| 40 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 41 | CHAVE_SAFX158 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX158: (CHAVE_SAFX158)
- IX_SAFX158_LOTE: (NUM_LOTE)

---

## SAFX159

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 13 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 14 | DAT_LANC_PIS_COFINS | VARCHAR2(8) | Y |  |  |
| 15 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 16 | IND_NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 17 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 18 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 19 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 21 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 22 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 23 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 24 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 25 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 26 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 27 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 28 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 29 | DAT_GRAVACAO | DATE | Y |  |  |
| 30 | PST_ID | NUMBER | Y |  |  |
| 31 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 32 | CHAVE_SAFX159 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX159: (CHAVE_SAFX159)
- IX_SAFX159_LOTE: (NUM_LOTE)

---

## SAFX16

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(2) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 7 | QTD_FABR | VARCHAR2(17) | Y |  |  |
| 8 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 9 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 10 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 11 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 12 | PERC_PERDA | VARCHAR2(7) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX16 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX16: (CHAVE_SAFX16)
- IX_SAFX16: (DAT_GRAVACAO)
- IX_SAFX16_LOTE: (NUM_LOTE)

---

## SAFX160

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | DATA_OPER | VARCHAR2(8) | Y |  |  |
| 9 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 10 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 11 | NUM_DOCTO | VARCHAR2(12) | Y |  |  |
| 12 | SERIE | VARCHAR2(3) | Y |  |  |
| 13 | SUB_SERIE | VARCHAR2(3) | Y |  |  |
| 14 | NUM_LANCTO | VARCHAR2(40) | Y |  |  |
| 15 | NUM_PROC_REF | VARCHAR2(20) | Y |  |  |
| 16 | ORIG_PROCESSO | VARCHAR2(1) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX160 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX160: (CHAVE_SAFX160)

---

## SAFX161

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_UF | VARCHAR2(2) | Y |  |  |
| 5 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | IND_TIPO_RECEITA | CHAR(1) | Y |  |  |
| 9 | DATA_DOC_INICIAL | VARCHAR2(8) | Y |  |  |
| 10 | DATA_DOC_FINAL | VARCHAR2(8) | Y |  |  |
| 11 | QTD_DOC_CONS | VARCHAR2(7) | Y |  |  |
| 12 | VLR_DOC | VARCHAR2(17) | Y |  |  |
| 13 | VLR_DESC | VARCHAR2(17) | Y |  |  |
| 14 | VLR_SERV | VARCHAR2(17) | Y |  |  |
| 15 | VLR_SERV_NT | VARCHAR2(17) | Y |  |  |
| 16 | VLR_TERC | VARCHAR2(17) | Y |  |  |
| 17 | VLR_DESP_ACS | VARCHAR2(17) | Y |  |  |
| 18 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 21 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | CHAVE_SAFX161 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX161: (CHAVE_SAFX161)
- IX_SAFX161_LOTE: (NUM_LOTE)

---

## SAFX162

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_UF | VARCHAR2(2) | Y |  |  |
| 5 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | IND_TIPO_RECEITA | CHAR(1) | Y |  |  |
| 9 | DATA_DOC_INICIAL | VARCHAR2(8) | Y |  |  |
| 10 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  |  |
| 11 | VLR_ITEM | VARCHAR2(17) | Y |  |  |
| 12 | VLR_DESC | VARCHAR2(17) | Y |  |  |
| 13 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 14 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 15 | VLR_ALIQ_PIS | VARCHAR2(12) | Y |  |  |
| 16 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 17 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 18 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_ALIQ_COFINS | VARCHAR2(12) | Y |  |  |
| 20 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 21 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX162 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX162: (CHAVE_SAFX162)
- IX_SAFX162_LOTE: (NUM_LOTE)

---

## SAFX163

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURAC | VARCHAR2(8) | Y |  |  |
| 4 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 5 | COD_GNRE | VARCHAR2(7) | Y |  |  |
| 6 | SEQUENCIAL | VARCHAR2(4) | Y |  |  |
| 7 | NUM_DOCTO_ORIG | VARCHAR2(20) | Y |  |  |
| 8 | PERIODO_REF | VARCHAR2(20) | Y |  |  |
| 9 | VLR_PRINCIPAL | VARCHAR2(17) | Y |  |  |
| 10 | VLR_ATUAL_MONET | VARCHAR2(17) | Y |  |  |
| 11 | VLR_JUROS | VARCHAR2(17) | Y |  |  |
| 12 | VLR_MULTA | VARCHAR2(17) | Y |  |  |
| 13 | VLR_TOT_RECOLHER | VARCHAR2(17) | Y |  |  |
| 14 | DAT_VENCTO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_CONVENIO | VARCHAR2(50) | Y |  |  |
| 16 | INSC_UF_FAVORECIDA | VARCHAR2(18) | Y |  |  |
| 17 | INFO_COMPL | VARCHAR2(70) | Y |  |  |
| 18 | INFO_COMPL_1 | VARCHAR2(70) | Y |  |  |
| 19 | INFO_COMPL_2 | VARCHAR2(70) | Y |  |  |
| 20 | INFO_COMPL_3 | VARCHAR2(70) | Y |  |  |
| 21 | NRO_BANCO | VARCHAR2(3) | Y |  |  |
| 22 | NRO_AGENCIA | VARCHAR2(6) | Y |  |  |
| 23 | NUM_AUTENTIC_GNRE | VARCHAR2(64) | Y |  |  |
| 24 | COD_ESTADO_FAV | VARCHAR2(2) | Y |  |  |
| 25 | DAT_RECOLH | VARCHAR2(8) | Y |  |  |
| 26 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 27 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 28 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 29 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 30 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 31 | COD_DEB_ICMS | VARCHAR2(3) | Y |  |  |
| 32 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 33 | PST_ID | NUMBER | Y |  |  |
| 34 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 35 | DAT_GRAVACAO | DATE | Y |  |  |
| 36 | CHAVE_SAFX163 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX163: (CHAVE_SAFX163)
- IX_SAFX163_LOTE: (NUM_LOTE)

---

## SAFX164

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MARCA_COM | VARCHAR2(6) | Y |  |  |
| 2 | TIPO_OBRIGACAO | VARCHAR2(2) | Y |  |  |
| 3 | COD_ING_ATIVO | VARCHAR2(35) | Y |  |  |
| 4 | DAT_VALID | VARCHAR2(8) | Y |  |  |
| 5 | PERC_CONCENT | VARCHAR2(7) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX164 | VARCHAR2(4000) | Y | NVL("COD_MARCA_COM",'@')\|\|NVL("TIPO_OBRIGACAO",... |  |

**Indexes**:
- IX_CHAVE_SAFX164: (CHAVE_SAFX164)
- IX_SAFX164_LOTE: (NUM_LOTE)

---

## SAFX165

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_EMPREENDIMENTO | VARCHAR2(9) | Y |  |  |
| 4 | ALIQ_REC | VARCHAR2(6) | Y |  |  |
| 5 | DATA_REC_UNI | VARCHAR2(8) | Y |  |  |
| 6 | DATA_APURACAO | VARCHAR2(8) | Y |  |  |
| 7 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 8 | INC_IMOB | VARCHAR2(90) | Y |  |  |
| 9 | VLR_RECEB_REC | VARCHAR2(15) | Y |  |  |
| 10 | VLR_FIN_REC | VARCHAR2(15) | Y |  |  |
| 11 | VLR_BASE_REC | VARCHAR2(15) | Y |  |  |
| 12 | VLR_REC_UNI | VARCHAR2(15) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX165 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX165: (CHAVE_SAFX165)
- IX_SAFX165: (DAT_GRAVACAO)
- IX_SAFX165_LOTE: (NUM_LOTE)

---

## SAFX168

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_ANO_COMPETENCIA | VARCHAR2(6) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 12 | DATA_OPER | VARCHAR2(8) | Y |  |  |
| 13 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 14 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 15 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 16 | VLR_OPER | VARCHAR2(17) | Y |  |  |
| 17 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 18 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 19 | IND_ORIG_CRED | CHAR(1) | Y |  |  |
| 20 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 21 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 22 | QUANT_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 23 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 24 | VLR_ALIQ_PIS_QUANT | VARCHAR2(19) | Y |  |  |
| 25 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 26 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 27 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 28 | QUANT_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 29 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 30 | VLR_ALIQ_COFINS_QUANT | VARCHAR2(19) | Y |  |  |
| 31 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 32 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 33 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 34 | PERIODO_ESCRIT | VARCHAR2(6) | Y |  |  |
| 35 | DESC_COMPL | VARCHAR2(255) | Y |  |  |
| 36 | DAT_GRAVACAO | DATE | Y |  |  |
| 37 | PST_ID | NUMBER | Y |  |  |
| 38 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 39 | CHAVE_SAFX168 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX168: (CHAVE_SAFX168)
- IX_SAFX168_LOTE: (NUM_LOTE)

---

## SAFX169

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 5 | DATA_SALDO | VARCHAR2(8) | Y |  |  |
| 6 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FINAL | VARCHAR2(17) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX169 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX169: (CHAVE_SAFX169)
- IX_SAFX169_LOTE: (NUM_LOTE)

---

## SAFX17

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(2) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | IND_INSUMO | VARCHAR2(2) | Y |  |  |
| 7 | COD_INSUMO | VARCHAR2(60) | Y |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | QTD_USADA | VARCHAR2(17) | Y |  |  |
| 10 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 11 | PERC_PERDA | VARCHAR2(7) | Y |  |  |
| 12 | DAT_FIM | VARCHAR2(8) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | QTD_MAX_UTILIZADA | VARCHAR2(17) | Y |  |  |
| 15 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 16 | TPO_VARIACAO | VARCHAR2(1) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX17 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX17: (CHAVE_SAFX17)
- IX_SAFX17: (DAT_GRAVACAO)
- IX_SAFX17_LOTE: (NUM_LOTE)

---

## SAFX170

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(2) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | IND_INSUMO | VARCHAR2(2) | Y |  |  |
| 7 | COD_INSUMO | VARCHAR2(60) | Y |  |  |
| 8 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | QTD_MIN_UTILIZADA | VARCHAR2(17) | Y |  |  |
| 11 | QTD_MAX_UTILIZADA | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX170 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX170: (CHAVE_SAFX170)
- IX_SAFX170_LOTE: (NUM_LOTE)

---

## SAFX175

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_DECL | VARCHAR2(6) | Y |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 7 | DAT_EMISSAO | VARCHAR2(8) | Y |  |  |
| 8 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 10 | NUM_ITEM | VARCHAR2(7) | Y |  |  |
| 11 | NUM_DOCFIS_RES | VARCHAR2(12) | Y |  |  |
| 12 | SERIE_DOCFIS_RES | VARCHAR2(3) | Y |  |  |
| 13 | SUB_SERIE_DOCFIS_RES | VARCHAR2(2) | Y |  |  |
| 14 | NUM_ITEM_RES | VARCHAR2(7) | Y |  |  |
| 15 | DAT_EMISSAO_RES | VARCHAR2(8) | Y |  |  |
| 16 | IND_TIPO_INF | CHAR(1) | Y |  |  |
| 17 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 18 | COD_MODELO_RES | VARCHAR2(2) | Y |  |  |
| 19 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |
| 20 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  |  |
| 21 | VLR_TOT_NF | VARCHAR2(17) | Y |  |  |
| 22 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 23 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 24 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 25 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 26 | VLR_TOT_ITEM | VARCHAR2(17) | Y |  |  |
| 27 | VLR_BASE_ICMS_IT | VARCHAR2(17) | Y |  |  |
| 28 | VLR_ICMS_IT | VARCHAR2(17) | Y |  |  |
| 29 | MOTIVO_ESTORNO | VARCHAR2(200) | Y |  |  |
| 30 | NUM_RECLAMACAO | VARCHAR2(20) | Y |  |  |
| 31 | VLR_ICMS_ESTORNO | VARCHAR2(17) | Y |  |  |
| 32 | HIPOTESE_ESTORNO | CHAR(1) | Y |  |  |
| 33 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 34 | DAT_GRAVACAO | DATE | Y |  |  |
| 35 | PST_ID | NUMBER | Y |  |  |
| 36 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 37 | CHAVE_SAFX175 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX175: (CHAVE_SAFX175)
- IX_SAFX175_LOTE: (NUM_LOTE)

---

## SAFX176

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_VALIDADE | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 6 | IND_TP_OPER | CHAR(1) | Y |  |  |
| 7 | COD_TRIB_PIS | VARCHAR2(2) | Y |  |  |
| 8 | COD_TRIB_COFINS | VARCHAR2(2) | Y |  |  |
| 9 | NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 10 | VLR_ALIQ_PIS | VARCHAR2(12) | Y |  |  |
| 11 | VLR_ALIQ_COFINS | VARCHAR2(12) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 16 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 17 | CHAVE_SAFX176 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX176: (CHAVE_SAFX176)
- IX_SAFX176: (DAT_GRAVACAO)
- IX_SAFX176_LOTE: (NUM_LOTE)

---

## SAFX179

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_LIVRO_AUX | VARCHAR2(3) | Y |  |  |
| 4 | COD_NAT_SUBCONTAS | VARCHAR2(2) | Y |  |  |
| 5 | COD_CONTA_SUB | VARCHAR2(70) | Y |  |  |
| 6 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 7 | COD_CNPJ_INV | VARCHAR2(14) | Y |  |  |
| 8 | COD_ITEM_ATIV_PAS | VARCHAR2(10) | Y |  |  |
| 9 | COD_INDIV_BEM | VARCHAR2(60) | Y |  |  |
| 10 | DATA_CONTAB_ITEM | VARCHAR2(8) | Y |  |  |
| 11 | DATA_LANCTO | VARCHAR2(8) | Y |  |  |
| 12 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 13 | DSC_RESUM_ITEM | VARCHAR2(50) | Y |  |  |
| 14 | QTD_INIC_ITEM | VARCHAR2(17) | Y |  |  |
| 15 | VLR_SALDO_INI_CONTA | VARCHAR2(17) | Y |  |  |
| 16 | IND_SALDO_INI_CONTA | CHAR(1) | Y |  |  |
| 17 | VLR_PARC_ITEM | VARCHAR2(17) | Y |  |  |
| 18 | IND_PARC_ITEM | CHAR(1) | Y |  |  |
| 19 | VLR_SALDO_FIN_CONTA | VARCHAR2(17) | Y |  |  |
| 20 | IND_SALDO_FIN_CONTA | CHAR(1) | Y |  |  |
| 21 | VLR_SALDO_INI_SUBCONTA | VARCHAR2(17) | Y |  |  |
| 22 | IND_SALDO_INI_SUBCONTA | CHAR(1) | Y |  |  |
| 23 | VLR_DEB_SUBCONTA | VARCHAR2(17) | Y |  |  |
| 24 | VLR_CRED_SUBCONTA | VARCHAR2(17) | Y |  |  |
| 25 | VLR_SALDO_FIN_SUBCONTA | VARCHAR2(17) | Y |  |  |
| 26 | IND_SALDO_FIN_SUBCONTA | CHAR(1) | Y |  |  |
| 27 | VLR_LANCTO | VARCHAR2(17) | Y |  |  |
| 28 | IND_LANCTO | CHAR(1) | Y |  |  |
| 29 | IND_REG_INI | CHAR(1) | Y |  |  |
| 30 | DAT_GRAVACAO | DATE | Y |  |  |
| 31 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 32 | PST_ID | NUMBER | Y |  |  |
| 33 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 34 | CHAVE_SAFX179 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX179: (CHAVE_SAFX179)
- IX_SAFX179_LOTE: (NUM_LOTE)

---

## SAFX18

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(2) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | IND_EMBALAGEM | VARCHAR2(2) | Y |  |  |
| 7 | EMBALAGEM | VARCHAR2(60) | Y |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | QTD_USADA | VARCHAR2(17) | Y |  |  |
| 10 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 11 | PERC_PERDA | VARCHAR2(7) | Y |  |  |
| 12 | DAT_FIM | VARCHAR2(8) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | QTD_MAX_UTILIZADA | VARCHAR2(17) | Y |  |  |
| 15 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 16 | TPO_VARIACAO | VARCHAR2(1) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX18 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX18: (CHAVE_SAFX18)
- IX_SAFX18: (DAT_GRAVACAO)
- IX_SAFX18_LOTE: (NUM_LOTE)

---

## SAFX180

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(2) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | IND_EMBALAGEM | VARCHAR2(2) | Y |  |  |
| 7 | COD_EMBALAGEM | VARCHAR2(60) | Y |  |  |
| 8 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | QTD_MIN_UTILIZADA | VARCHAR2(17) | Y |  |  |
| 11 | QTD_MAX_UTILIZADA | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX180 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX180: (CHAVE_SAFX180)
- IX_SAFX180_LOTE: (NUM_LOTE)

---

## SAFX181

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_CALENDARIO | VARCHAR2(4) | Y |  |  |
| 4 | ANO_REFERENCIA | VARCHAR2(4) | Y |  |  |
| 5 | COD_RETENCAO | VARCHAR2(4) | Y |  |  |
| 6 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 7 | PROC_REQ | VARCHAR2(20) | Y |  |  |
| 8 | IND_RRA | CHAR(1) | Y |  |  |
| 9 | NATUREZA_RRA | VARCHAR2(50) | Y |  |  |
| 10 | CPF_CGC_RESP_JUR | VARCHAR2(14) | Y |  |  |
| 11 | NOME_RESP_JUR | VARCHAR2(150) | Y |  |  |
| 12 | IND_BENEF_MOLESTIA | CHAR(1) | Y |  |  |
| 13 | DATA_MOLESTIA | VARCHAR2(8) | Y |  |  |
| 14 | VALOR_REND_1 | VARCHAR2(15) | Y |  |  |
| 15 | VALOR_REND_ISENT_1 | VARCHAR2(15) | Y |  |  |
| 16 | VALOR_PREV_OFC_1 | VARCHAR2(15) | Y |  |  |
| 17 | VALOR_PENSAO_1 | VARCHAR2(15) | Y |  |  |
| 18 | IRRF_RETIDO_1 | VARCHAR2(15) | Y |  |  |
| 19 | VALOR_DESP_JUD_1 | VARCHAR2(15) | Y |  |  |
| 20 | QTD_MESES_1 | VARCHAR2(4) | Y |  |  |
| 21 | VALOR_REND_2 | VARCHAR2(15) | Y |  |  |
| 22 | VALOR_REND_ISENT_2 | VARCHAR2(15) | Y |  |  |
| 23 | VALOR_PREV_OFC_2 | VARCHAR2(15) | Y |  |  |
| 24 | VALOR_PENSAO_2 | VARCHAR2(15) | Y |  |  |
| 25 | IRRF_RETIDO_2 | VARCHAR2(15) | Y |  |  |
| 26 | VALOR_DESP_JUD_2 | VARCHAR2(15) | Y |  |  |
| 27 | QTD_MESES_2 | VARCHAR2(4) | Y |  |  |
| 28 | VALOR_REND_3 | VARCHAR2(15) | Y |  |  |
| 29 | VALOR_REND_ISENT_3 | VARCHAR2(15) | Y |  |  |
| 30 | VALOR_PREV_OFC_3 | VARCHAR2(15) | Y |  |  |
| 31 | VALOR_PENSAO_3 | VARCHAR2(15) | Y |  |  |
| 32 | IRRF_RETIDO_3 | VARCHAR2(15) | Y |  |  |
| 33 | VALOR_DESP_JUD_3 | VARCHAR2(15) | Y |  |  |
| 34 | QTD_MESES_3 | VARCHAR2(4) | Y |  |  |
| 35 | VALOR_REND_4 | VARCHAR2(15) | Y |  |  |
| 36 | VALOR_REND_ISENT_4 | VARCHAR2(15) | Y |  |  |
| 37 | VALOR_PREV_OFC_4 | VARCHAR2(15) | Y |  |  |
| 38 | VALOR_PENSAO_4 | VARCHAR2(15) | Y |  |  |
| 39 | IRRF_RETIDO_4 | VARCHAR2(15) | Y |  |  |
| 40 | VALOR_DESP_JUD_4 | VARCHAR2(15) | Y |  |  |
| 41 | QTD_MESES_4 | VARCHAR2(4) | Y |  |  |
| 42 | VALOR_REND_5 | VARCHAR2(15) | Y |  |  |
| 43 | VALOR_REND_ISENT_5 | VARCHAR2(15) | Y |  |  |
| 44 | VALOR_PREV_OFC_5 | VARCHAR2(15) | Y |  |  |
| 45 | VALOR_PENSAO_5 | VARCHAR2(15) | Y |  |  |
| 46 | IRRF_RETIDO_5 | VARCHAR2(15) | Y |  |  |
| 47 | VALOR_DESP_JUD_5 | VARCHAR2(15) | Y |  |  |
| 48 | QTD_MESES_5 | VARCHAR2(4) | Y |  |  |
| 49 | VALOR_REND_6 | VARCHAR2(15) | Y |  |  |
| 50 | VALOR_REND_ISENT_6 | VARCHAR2(15) | Y |  |  |
| 51 | VALOR_PREV_OFC_6 | VARCHAR2(15) | Y |  |  |
| 52 | VALOR_PENSAO_6 | VARCHAR2(15) | Y |  |  |
| 53 | IRRF_RETIDO_6 | VARCHAR2(15) | Y |  |  |
| 54 | VALOR_DESP_JUD_6 | VARCHAR2(15) | Y |  |  |
| 55 | QTD_MESES_6 | VARCHAR2(4) | Y |  |  |
| 56 | VALOR_REND_7 | VARCHAR2(15) | Y |  |  |
| 57 | VALOR_REND_ISENT_7 | VARCHAR2(15) | Y |  |  |
| 58 | VALOR_PREV_OFC_7 | VARCHAR2(15) | Y |  |  |
| 59 | VALOR_PENSAO_7 | VARCHAR2(15) | Y |  |  |
| 60 | IRRF_RETIDO_7 | VARCHAR2(15) | Y |  |  |
| 61 | VALOR_DESP_JUD_7 | VARCHAR2(15) | Y |  |  |
| 62 | QTD_MESES_7 | VARCHAR2(4) | Y |  |  |
| 63 | VALOR_REND_8 | VARCHAR2(15) | Y |  |  |
| 64 | VALOR_REND_ISENT_8 | VARCHAR2(15) | Y |  |  |
| 65 | VALOR_PREV_OFC_8 | VARCHAR2(15) | Y |  |  |
| 66 | VALOR_PENSAO_8 | VARCHAR2(15) | Y |  |  |
| 67 | IRRF_RETIDO_8 | VARCHAR2(15) | Y |  |  |
| 68 | VALOR_DESP_JUD_8 | VARCHAR2(15) | Y |  |  |
| 69 | QTD_MESES_8 | VARCHAR2(4) | Y |  |  |
| 70 | VALOR_REND_9 | VARCHAR2(15) | Y |  |  |
| 71 | VALOR_REND_ISENT_9 | VARCHAR2(15) | Y |  |  |
| 72 | VALOR_PREV_OFC_9 | VARCHAR2(15) | Y |  |  |
| 73 | VALOR_PENSAO_9 | VARCHAR2(15) | Y |  |  |
| 74 | IRRF_RETIDO_9 | VARCHAR2(15) | Y |  |  |
| 75 | VALOR_DESP_JUD_9 | VARCHAR2(15) | Y |  |  |
| 76 | QTD_MESES_9 | VARCHAR2(4) | Y |  |  |
| 77 | VALOR_REND_10 | VARCHAR2(15) | Y |  |  |
| 78 | VALOR_REND_ISENT_10 | VARCHAR2(15) | Y |  |  |
| 79 | VALOR_PREV_OFC_10 | VARCHAR2(15) | Y |  |  |
| 80 | VALOR_PENSAO_10 | VARCHAR2(15) | Y |  |  |
| 81 | IRRF_RETIDO_10 | VARCHAR2(15) | Y |  |  |
| 82 | VALOR_DESP_JUD_10 | VARCHAR2(15) | Y |  |  |
| 83 | QTD_MESES_10 | VARCHAR2(4) | Y |  |  |
| 84 | VALOR_REND_11 | VARCHAR2(15) | Y |  |  |
| 85 | VALOR_REND_ISENT_11 | VARCHAR2(15) | Y |  |  |
| 86 | VALOR_PREV_OFC_11 | VARCHAR2(15) | Y |  |  |
| 87 | VALOR_PENSAO_11 | VARCHAR2(15) | Y |  |  |
| 88 | IRRF_RETIDO_11 | VARCHAR2(15) | Y |  |  |
| 89 | VALOR_DESP_JUD_11 | VARCHAR2(15) | Y |  |  |
| 90 | QTD_MESES_11 | VARCHAR2(4) | Y |  |  |
| 91 | VALOR_REND_12 | VARCHAR2(15) | Y |  |  |
| 92 | VALOR_REND_ISENT_12 | VARCHAR2(15) | Y |  |  |
| 93 | VALOR_PREV_OFC_12 | VARCHAR2(15) | Y |  |  |
| 94 | VALOR_PENSAO_12 | VARCHAR2(15) | Y |  |  |
| 95 | IRRF_RETIDO_12 | VARCHAR2(15) | Y |  |  |
| 96 | VALOR_DESP_JUD_12 | VARCHAR2(15) | Y |  |  |
| 97 | QTD_MESES_12 | VARCHAR2(4) | Y |  |  |
| 98 | VALOR_REND_13 | VARCHAR2(15) | Y |  |  |
| 99 | VALOR_REND_ISENT_13 | VARCHAR2(15) | Y |  |  |
| 100 | VALOR_PREV_OFC_13 | VARCHAR2(15) | Y |  |  |
| 101 | VALOR_PENSAO_13 | VARCHAR2(15) | Y |  |  |
| 102 | IRRF_RETIDO_13 | VARCHAR2(15) | Y |  |  |
| 103 | VALOR_DESP_JUD_13 | VARCHAR2(15) | Y |  |  |
| 104 | DAT_GRAVACAO | DATE | Y |  |  |
| 105 | PST_ID | NUMBER | Y |  |  |
| 106 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 107 | VLR_JUROS_MORA | VARCHAR2(15) | Y |  |  |
| 108 | CHAVE_SAFX181 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("ANO_CALENDARIO",'@... |  |

**Indexes**:
- IX_CHAVE_SAFX181: (CHAVE_SAFX181)
- IX_SAFX181_LOTE: (NUM_LOTE)

---

## SAFX182

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_ENTRADA | VARCHAR2(8) | Y |  |  |
| 4 | HORA_ENTRADA | VARCHAR2(6) | Y |  |  |
| 5 | PLACA_VEICULO | VARCHAR2(7) | Y |  |  |
| 6 | DSC_MARCA | VARCHAR2(20) | Y |  |  |
| 7 | DSC_MODELO | VARCHAR2(20) | Y |  |  |
| 8 | NUM_ANO_FABRIC | VARCHAR2(4) | Y |  |  |
| 9 | NUM_CHASSI | VARCHAR2(28) | Y |  |  |
| 10 | NUM_MOTOR | VARCHAR2(28) | Y |  |  |
| 11 | DSC_COMPL | VARCHAR2(255) | Y |  |  |
| 12 | IND_PROP | CHAR(1) | Y |  |  |
| 13 | COD_ESTADO_ORIG | VARCHAR2(2) | Y |  |  |
| 14 | COD_ESTADO_REG | VARCHAR2(2) | Y |  |  |
| 15 | COD_MUNIC_REG | VARCHAR2(5) | Y |  |  |
| 16 | IND_FIS_JUR_ENT | CHAR(1) | Y |  |  |
| 17 | COD_FIS_JUR_ENT | VARCHAR2(14) | Y |  |  |
| 18 | IND_TP_NEG | CHAR(1) | Y |  |  |
| 19 | VLR_VEICULO | VARCHAR2(17) | Y |  |  |
| 20 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 21 | DAT_SAIDA | VARCHAR2(8) | Y |  |  |
| 22 | IND_FIS_JUR_SAI | CHAR(1) | Y |  |  |
| 23 | COD_FIS_JUR_SAI | VARCHAR2(14) | Y |  |  |
| 24 | VLR_OPERACAO | VARCHAR2(17) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |
| 26 | PST_ID | NUMBER | Y |  |  |
| 27 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 28 | CHAVE_SAFX182 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX182: (CHAVE_SAFX182)
- IX_SAFX182_LOTE: (NUM_LOTE)

---

## SAFX183

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_TP_REGIME | CHAR(1) | Y |  |  |
| 4 | IND_COMP_REC | VARCHAR2(2) | Y |  |  |
| 5 | DESC_COMPL_COMP_REC | VARCHAR2(255) | Y |  |  |
| 6 | NUM_DOCTO | VARCHAR2(12) | Y |  |  |
| 7 | SERIE | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE | VARCHAR2(2) | Y |  |  |
| 9 | NUM_LANCTO | VARCHAR2(40) | Y |  |  |
| 10 | DATA_OPER | VARCHAR2(8) | Y |  |  |
| 11 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 16 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 17 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 18 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 19 | DESC_COMPL | VARCHAR2(255) | Y |  |  |
| 20 | VLR_RECEITA | VARCHAR2(17) | Y |  |  |
| 21 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 22 | VLR_ALIQ_PIS | VARCHAR2(12) | Y |  |  |
| 23 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 24 | VLR_ALIQ_PIS_R | VARCHAR2(19) | Y |  |  |
| 25 | QTD_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 26 | VLR_DESC_PIS | VARCHAR2(17) | Y |  |  |
| 27 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 28 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 29 | VLR_ALIQ_COFINS | VARCHAR2(12) | Y |  |  |
| 30 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 31 | VLR_ALIQ_COFINS_R | VARCHAR2(19) | Y |  |  |
| 32 | QTD_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 33 | VLR_DESC_COFINS | VARCHAR2(17) | Y |  |  |
| 34 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 35 | DAT_GRAVACAO | DATE | Y |  |  |
| 36 | COD_SIT_DOCTO | CHAR(1) | Y |  |  |
| 37 | IND_TP_FATURA | CHAR(1) | Y |  |  |
| 38 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 39 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 40 | PST_ID | NUMBER | Y |  |  |
| 41 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 42 | CHAVE_SAFX183 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX183: (CHAVE_SAFX183)
- IX_SAFX183_LOTE: (NUM_LOTE)

---

## SAFX185

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 4 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 5 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 6 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 7 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 8 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 9 | VLR_REC_BRT | VARCHAR2(17) | Y |  |  |
| 10 | VLR_REC_BRT_ATIV | VARCHAR2(17) | Y |  |  |
| 11 | VLR_REC_BRT_DEMAIS_ATIV | VARCHAR2(17) | Y |  |  |
| 12 | VLR_EXC_REC_BRT | VARCHAR2(17) | Y |  |  |
| 13 | VLR_BASE_CONT_PREV | VARCHAR2(17) | Y |  |  |
| 14 | VLR_ALIQ_CONT_PREV | VARCHAR2(12) | Y |  |  |
| 15 | VLR_CONT_PREV | VARCHAR2(17) | Y |  |  |
| 16 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX185 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX185: (CHAVE_SAFX185)
- IX_SAFX185_LOTE: (NUM_LOTE)

---

## SAFX187

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_TP_REGIME | CHAR(1) | Y |  |  |
| 4 | IND_COMP_REC | VARCHAR2(2) | Y |  |  |
| 5 | DESC_COMPL_COMP_REC | VARCHAR2(255) | Y |  |  |
| 6 | NUM_DOCTO | VARCHAR2(12) | Y |  |  |
| 7 | SERIE | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE | VARCHAR2(2) | Y |  |  |
| 9 | NUM_LANCTO | VARCHAR2(40) | Y |  |  |
| 10 | DATA_OPER | VARCHAR2(8) | Y |  |  |
| 11 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 16 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 17 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 18 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 19 | DESC_COMPL | VARCHAR2(255) | Y |  |  |
| 20 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 21 | VLR_ALIQ_PIS | VARCHAR2(12) | Y |  |  |
| 22 | VLR_ALIQ_PIS_R | VARCHAR2(19) | Y |  |  |
| 23 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 24 | VLR_ALIQ_COFINS | VARCHAR2(12) | Y |  |  |
| 25 | VLR_ALIQ_COFINS_R | VARCHAR2(19) | Y |  |  |
| 26 | MES_ANO_COMPETENCIA | VARCHAR2(6) | Y |  |  |
| 27 | VLR_RECEITA_RECEB | VARCHAR2(17) | Y |  |  |
| 28 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 29 | QTD_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 30 | VLR_DESC_PIS | VARCHAR2(17) | Y |  |  |
| 31 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 32 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 33 | QTD_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 34 | VLR_DESC_COFINS | VARCHAR2(17) | Y |  |  |
| 35 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 36 | DAT_GRAVACAO | DATE | Y |  |  |
| 37 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 38 | PST_ID | NUMBER | Y |  |  |
| 39 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 40 | CHAVE_SAFX187 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX187: (CHAVE_SAFX187)
- IX_SAFX187_LOTE: (NUM_LOTE)

---

## SAFX188

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 5 | COD_CONTA_ANT | VARCHAR2(70) | Y |  |  |
| 6 | CENTRO_CUSTO_ANT | VARCHAR2(50) | Y |  |  |
| 7 | VLR_SALDO_INI | VARCHAR2(19) | Y |  |  |
| 8 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX188 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX188: (CHAVE_SAFX188)
- IX_SAFX188_LOTE: (NUM_LOTE)

---

## SAFX189

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 5 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 6 | COD_CONTA_ANT | VARCHAR2(70) | Y |  |  |
| 7 | CENTRO_CUSTO_ANT | VARCHAR2(50) | Y |  |  |
| 8 | VLR_SALDO_INI | VARCHAR2(19) | Y |  |  |
| 9 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX189 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX189: (CHAVE_SAFX189)
- IX_SAFX189_LOTE: (NUM_LOTE)

---

## SAFX19

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 4 | DATA_VENCTO | VARCHAR2(8) | Y |  |  |
| 5 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 6 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 7 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 8 | VLR_RECEITA | VARCHAR2(17) | Y |  |  |
| 9 | VLR_CORRECAO | VARCHAR2(17) | Y |  |  |
| 10 | VLR_MULTA | VARCHAR2(17) | Y |  |  |
| 11 | VLR_JUROS | VARCHAR2(17) | Y |  |  |
| 12 | VLR_TOTAL | VARCHAR2(17) | Y |  |  |
| 13 | NUM_REFERENCIA | VARCHAR2(12) | Y |  |  |
| 14 | NUM_PROCESSO_BASE | VARCHAR2(12) | Y |  |  |
| 15 | VLR_BASE_CALCULO | VARCHAR2(17) | Y |  |  |
| 16 | ALIQ_INCIDENCIA | VARCHAR2(7) | Y |  |  |
| 17 | OBS_DARF | VARCHAR2(45) | Y |  |  |
| 18 | BANCO | VARCHAR2(3) | Y |  |  |
| 19 | AGENCIA | VARCHAR2(5) | Y |  |  |
| 20 | DATA_ARRECADACAO | VARCHAR2(8) | Y |  |  |
| 21 | NUM_PAGAMENTO | VARCHAR2(12) | Y |  |  |
| 22 | EXERCICIO | VARCHAR2(4) | Y |  |  |
| 23 | DAT_GRAVACAO | DATE | Y |  |  |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | CHAVE_SAFX19 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX19: (CHAVE_SAFX19)
- IX_SAFX19: (DAT_GRAVACAO)
- IX_SAFX19_LOTE: (NUM_LOTE)

---

## SAFX190

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_UF | VARCHAR2(2) | Y |  |  |
| 5 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | COD_CLASSE_CONSUMO | VARCHAR2(2) | Y |  |  |
| 9 | DATA_DOCTO | VARCHAR2(8) | Y |  |  |
| 10 | QTD_DOCTOS | VARCHAR2(15) | Y |  |  |
| 11 | QTD_DOCTOS_CANC | VARCHAR2(15) | Y |  |  |
| 12 | VLR_TOTAL | VARCHAR2(17) | Y |  |  |
| 13 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 14 | QTD_CONSUMO_TOTAL | VARCHAR2(15) | Y |  |  |
| 15 | VLR_FORNECIMENTO | VARCHAR2(17) | Y |  |  |
| 16 | VLR_SERV_N_TRIB | VARCHAR2(17) | Y |  |  |
| 17 | VLR_COBR_TERCEIRO | VARCHAR2(17) | Y |  |  |
| 18 | VLR_DESP_ACS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 21 | VLR_BASE_ICMSS | VARCHAR2(17) | Y |  |  |
| 22 | VLR_ICMSS | VARCHAR2(17) | Y |  |  |
| 23 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 24 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |
| 26 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 27 | PST_ID | NUMBER | Y |  |  |
| 28 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 29 | CHAVE_SAFX190 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX190: (CHAVE_SAFX190)
- IX_SAFX190_LOTE: (NUM_LOTE)

---

## SAFX191

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_UF | VARCHAR2(2) | Y |  |  |
| 5 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | COD_CLASSE_CONSUMO | VARCHAR2(2) | Y |  |  |
| 9 | DATA_DOCTO | VARCHAR2(8) | Y |  |  |
| 10 | VLR_TOTAL_ITEM | VARCHAR2(17) | Y |  |  |
| 11 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 12 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 13 | VLR_ALIQ_PIS | VARCHAR2(8) | Y |  |  |
| 14 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 15 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 16 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 17 | VLR_ALIQ_COFINS | VARCHAR2(8) | Y |  |  |
| 18 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 19 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX191 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX191: (CHAVE_SAFX191)
- IX_SAFX191_LOTE: (NUM_LOTE)

---

## SAFX192

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | IND_TIPO_REF | CHAR(1) | Y |  |  |
| 17 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 18 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 19 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 20 | DATA_FISCAL_REF | VARCHAR2(8) | Y |  |  |
| 21 | IND_FIS_JUR_REF | CHAR(1) | Y |  |  |
| 22 | COD_FIS_JUR_REF | VARCHAR2(14) | Y |  |  |
| 23 | NUM_ITEM_REF | VARCHAR2(5) | Y |  |  |
| 24 | QTD_DEVOL | VARCHAR2(17) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |
| 26 | PST_ID | NUMBER | Y |  |  |
| 27 | NUM_AUTENTIC_NFE_REF | VARCHAR2(80) | Y |  |  |
| 28 | NUM_CNPJ_NFE_REF | VARCHAR2(14) | Y |  |  |
| 29 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 30 | COD_MODELO_REF | VARCHAR2(2) | Y |  |  |
| 31 | COD_CAIXA_ECF_REF | VARCHAR2(3) | Y |  |  |
| 32 | NUM_COO_REF | VARCHAR2(9) | Y |  |  |
| 33 | DATA_EMISSAO_REF | VARCHAR2(8) | Y |  |  |
| 34 | CHAVE_SAFX192 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX192: (CHAVE_SAFX192)
- IX_SAFX192_LOTE: (NUM_LOTE)

---

## SAFX193

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_ANO_COMP | VARCHAR2(8) | Y |  |  |
| 4 | IND_NAT_DED | CHAR(1) | Y |  |  |
| 5 | IND_ORIGEM_DED | VARCHAR2(2) | Y |  |  |
| 6 | CNPJ | VARCHAR2(14) | Y |  |  |
| 7 | VLR_DED_PIS | VARCHAR2(17) | Y |  |  |
| 8 | VLR_DED_COFINS | VARCHAR2(17) | Y |  |  |
| 9 | VLR_BC_OPER | VARCHAR2(17) | Y |  |  |
| 10 | INF_COMPL | VARCHAR2(90) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX193 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX193: (CHAVE_SAFX193)
- IX_SAFX193_LOTE: (NUM_LOTE)

---

## SAFX194

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | DATA_FISCAL_REF | VARCHAR2(8) | Y |  |  |
| 17 | MOVTO_E_S_REF | CHAR(1) | Y |  |  |
| 18 | NORM_DEV_REF | CHAR(1) | Y |  |  |
| 19 | COD_DOCTO_REF | VARCHAR2(5) | Y |  |  |
| 20 | IND_FIS_JUR_REF | CHAR(1) | Y |  |  |
| 21 | COD_FIS_JUR_REF | VARCHAR2(14) | Y |  |  |
| 22 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 23 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 24 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 25 | IND_PRODUTO_REF | CHAR(1) | Y |  |  |
| 26 | COD_PRODUTO_REF | VARCHAR2(60) | Y |  |  |
| 27 | COD_UND_PADRAO_REF | VARCHAR2(8) | Y |  |  |
| 28 | NUM_ITEM_REF | VARCHAR2(5) | Y |  |  |
| 29 | QTD_INSUMO | VARCHAR2(17) | Y |  |  |
| 30 | DAT_GRAVACAO | DATE | Y |  |  |
| 31 | PST_ID | NUMBER | Y |  |  |
| 32 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 33 | CHAVE_SAFX194 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX194: (CHAVE_SAFX194)
- IX_SAFX194: (DAT_GRAVACAO)
- IX_SAFX194_LOTE: (NUM_LOTE)

---

## SAFX195

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_REF | VARCHAR2(4) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | VLR_POUP_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 7 | VLR_POUP_ANO_REF | VARCHAR2(17) | Y |  |  |
| 8 | VLR_POUP_REND | VARCHAR2(17) | Y |  |  |
| 9 | VLR_LUCRO_DIV_REND | VARCHAR2(17) | Y |  |  |
| 10 | VLR_DEMAIS_REND_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 11 | VLR_DEMAIS_REND_ANO_REF | VARCHAR2(17) | Y |  |  |
| 12 | VLR_DEMAIS_REND_R | VARCHAR2(17) | Y |  |  |
| 13 | VLR_FUND_INV_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 14 | VLR_FUND_INV_ANO_REF | VARCHAR2(17) | Y |  |  |
| 15 | VLR_FUND_INV_ANO_REND | VARCHAR2(17) | Y |  |  |
| 16 | VLR_REND_FIXA_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 17 | VLR_REND_FIXA_ANO_REF | VARCHAR2(17) | Y |  |  |
| 18 | VLR_REND_FIXA_ANO_REND | VARCHAR2(17) | Y |  |  |
| 19 | VLR_TIT_CAP_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 20 | VLR_TIT_CAP_ANO_REF | VARCHAR2(17) | Y |  |  |
| 21 | VLR_TIT_CAP_ANO_REND | VARCHAR2(17) | Y |  |  |
| 22 | VLR_JCP_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 23 | VLR_JCP_ANO_REF | VARCHAR2(17) | Y |  |  |
| 24 | VLR_JCP_ANO_REND | VARCHAR2(17) | Y |  |  |
| 25 | VLR_SWAP_REND | VARCHAR2(17) | Y |  |  |
| 26 | VLR_PREV_REND | VARCHAR2(17) | Y |  |  |
| 27 | VLR_DEMAIS_REND_EXC_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 28 | VLR_DEMAIS_REND_EXC_ANO_REF | VARCHAR2(17) | Y |  |  |
| 29 | VLR_DEMAIS_REND_EXC_ANO_REND | VARCHAR2(17) | Y |  |  |
| 30 | VLR_DEP_CC_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 31 | VLR_DEP_CC_ANO_REF | VARCHAR2(17) | Y |  |  |
| 32 | VLR_PREMIOS_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 33 | VLR_PREMIOS_ANO_REF | VARCHAR2(17) | Y |  |  |
| 34 | VLR_FUNDOS_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 35 | VLR_FUNDOS_ANO_REF | VARCHAR2(17) | Y |  |  |
| 36 | VLR_DEMAIS_CRED_ANO_ANT | VARCHAR2(17) | Y |  |  |
| 37 | VLR_DEMAIS_CRED_ANO_REF | VARCHAR2(17) | Y |  |  |
| 38 | DAT_GRAVACAO | DATE | Y |  |  |
| 39 | PST_ID | NUMBER | Y |  |  |
| 40 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 41 | CHAVE_SAFX195 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX195: (CHAVE_SAFX195)
- IX_SAFX195_LOTE: (NUM_LOTE)

---

## SAFX196

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
| 32 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
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
| 73 | ROWID_S | NUMBER | Y |  |  |
| 74 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 75 | PST_ID | NUMBER | Y |  |  |
| 76 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 77 | DAT_GRAVACAO | DATE | Y |  |  |
| 78 | CHAVE_SAFX196 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX196: (CHAVE_SAFX196)
- IX_SAFX196_LOTE: (NUM_LOTE)

---

## SAFX197

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_CONTRATO | VARCHAR2(6) | Y |  |  |
| 4 | IND_TP_CONTRATO | CHAR(1) | Y |  |  |
| 5 | DAT_CONTRATO | VARCHAR2(8) | Y |  |  |
| 6 | COD_UNID_IMOB | VARCHAR2(11) | Y |  |  |
| 7 | IND_FIS_JUR_COMPR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR_COMPR | VARCHAR2(14) | Y |  |  |
| 9 | IND_FIS_JUR_VEND | CHAR(1) | Y |  |  |
| 10 | COD_FIS_JUR_VEND | VARCHAR2(14) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX197 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX197: (CHAVE_SAFX197)
- IX_SAFX197_LOTE: (NUM_LOTE)

---

## SAFX198

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_CONTRATO | VARCHAR2(6) | Y |  |  |
| 4 | DAT_OPERACAO | VARCHAR2(8) | Y |  |  |
| 5 | VLR_OPERACAO | VARCHAR2(17) | Y |  |  |
| 6 | VLR_COMISSAO | VARCHAR2(17) | Y |  |  |
| 7 | VLR_IMPOSTO_RET | VARCHAR2(17) | Y |  |  |
| 8 | VLR_PAGO_ANO | VARCHAR2(17) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | IND_FIS_JUR_COMPR | CHAR(1) | Y |  |  |
| 11 | COD_FIS_JUR_COMPR | VARCHAR2(14) | Y |  |  |
| 12 | IND_FIS_JUR_VEND | CHAR(1) | Y |  |  |
| 13 | COD_FIS_JUR_VEND | VARCHAR2(14) | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX198 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX198: (CHAVE_SAFX198)
- IX_SAFX198_LOTE: (NUM_LOTE)

---

## SAFX199

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |
| 6 | IND_COD_DECL | CHAR(1) | Y |  |  |
| 7 | COD_GGREM | VARCHAR2(15) | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | CHAVE_SAFX199 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX199: (CHAVE_SAFX199)
- IX_SAFX199_LOTE: (NUM_LOTE)

---

## SAFX200

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 6 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | CHAVE_SAFX200 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX200: (CHAVE_SAFX200)
- IX_SAFX200_LOTE: (NUM_LOTE)

---

## SAFX2001

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 2 | DATA_X2001 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | IND_TP_OP | CHAR(1) | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2001 | VARCHAR2(4000) | Y | NVL("COD_OPERACAO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2001: (CHAVE_SAFX2001)
- IX_SAFX2001: (DAT_GRAVACAO)
- IX_SAFX2001_LOTE: (NUM_LOTE)

---

## SAFX2002

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 2 | DATA_X2002 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | IND_CONTA | CHAR(1) | Y |  |  |
| 5 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | COD_CONTA_SINT | VARCHAR2(70) | Y |  |  |
| 8 | IND_NATUREZA | CHAR(1) | Y |  | 0 - Compensação;1 - Ativo; 2 - Passivo; 3 - Despesa; 4 - Receita; 5 - Mutações Ativas; 6 - Mutações Passivas; 7 - Patrimonio Liquido; 8 - Custo; 9 - Outros |
| 9 | NIVEL | VARCHAR2(5) | Y |  | Nivel da conta |
| 10 | IND_LANCTO_GLOBAL | CHAR(1) | Y |  | Indica se a conta recebe lançamentos globais ou não |
| 11 | SEQ_ARQ | NUMBER(20) | Y |  |  |
| 12 | COD_CONTA_ANL_TOT | VARCHAR2(70) | Y |  | Código da Conta Analítica Totalizadora - IN86 (atendimento SINCO - SAFR102) |
| 13 | COD_CONTA_PADRAO | VARCHAR2(70) | Y |  |  |
| 14 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 15 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 16 | IND_SITUACAO | CHAR(1) | Y | 'A' |  |
| 17 | IND_CONTA_CONSOLID | CHAR(1) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | DESC_DETALHADA | VARCHAR2(600) | Y |  |  |
| 20 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX2002 | VARCHAR2(4000) | Y | NVL("COD_CONTA",'@')\|\|NVL("IND_CONTA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2002: (CHAVE_SAFX2002)
- IX_SAFX2002: (DAT_GRAVACAO)
- IX_SAFX2002_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX2002_LOTE: (NUM_LOTE)

---

## SAFX2003

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 2 | DATA_X2003 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | IND_CTRL_INVEST | CHAR(1) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | COD_CUSTO_SPED | VARCHAR2(28) | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2003 | VARCHAR2(4000) | Y | NVL("COD_CUSTO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2003: (CHAVE_SAFX2003)
- IX_SAFX2003: (DAT_GRAVACAO)
- IX_SAFX2003_LOTE: (NUM_LOTE)

---

## SAFX2004

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DESPESA | VARCHAR2(20) | Y |  |  |
| 2 | DATA_X2004 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2004 | VARCHAR2(4000) | Y | NVL("COD_DESPESA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2004: (CHAVE_SAFX2004)
- IX_SAFX2004: (DAT_GRAVACAO)
- IX_SAFX2004_LOTE: (NUM_LOTE)

---

## SAFX2005

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 2 | DATA_X2005 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | IND_DOCTO_FISCAL | CHAR(1) | Y |  |  |
| 5 | OBS_CANCEL_P2 | VARCHAR2(32) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | IND_CLASS_OBRIG | CHAR(1) | Y |  |  |
| 8 | IND_NF_ELETRONICA | CHAR(1) | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX2005 | VARCHAR2(4000) | Y | NVL("COD_DOCTO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2005: (CHAVE_SAFX2005)
- IX_SAFX2005: (DAT_GRAVACAO)
- IX_SAFX2005_LOTE: (NUM_LOTE)

---

## SAFX2006

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 2 | DATA_X2006 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | ENT_SAI | CHAR(1) | Y |  |  |
| 6 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 7 | COD_NATUREZA_OP_SPED | VARCHAR2(10) | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX2006 | VARCHAR2(4000) | Y | NVL("COD_NATUREZA_OP",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2006: (CHAVE_SAFX2006)
- IX_SAFX2006: (DAT_GRAVACAO)
- IX_SAFX2006_LOTE: (NUM_LOTE)

---

## SAFX2007

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 2 | DATA_X2007 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | IND_UNID_FRAC | CHAR(1) | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2007 | VARCHAR2(4000) | Y | NVL("COD_MEDIDA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2007: (CHAVE_SAFX2007)
- IX_SAFX2007: (DAT_GRAVACAO)
- IX_SAFX2007_LOTE: (NUM_LOTE)

---

## SAFX2008

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LEGENDA | VARCHAR2(5) | Y |  |  |
| 2 | DATA_X2008 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2008 | VARCHAR2(4000) | Y | NVL("COD_LEGENDA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2008: (CHAVE_SAFX2008)
- IX_SAFX2008: (DAT_GRAVACAO)
- IX_SAFX2008_LOTE: (NUM_LOTE)

---

## SAFX2009

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 2 | DATA_X2009 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(500) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 6 | TIPO_OBSERVACAO | CHAR(1) | Y | 1 |  |
| 7 | COD_OBS_LEI_5005 | VARCHAR2(25) | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 12 | CHAVE_SAFX2009 | VARCHAR2(4000) | Y | NVL("COD_OBSERVACAO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2009: (CHAVE_SAFX2009)
- IX_SAFX2009: (DAT_GRAVACAO)
- IX_SAFX2009_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX2009_LOTE: (NUM_LOTE)

---

## SAFX201

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_EQUIP | VARCHAR2(9) | Y |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | Y |  |  |
| 5 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 6 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 7 | IND_SITUACAO_CUPOM | VARCHAR2(2) | Y |  |  |
| 8 | NOME_CLIENTE | VARCHAR2(60) | Y |  |  |
| 9 | CPF_CNPJ_CLIENTE | VARCHAR2(14) | Y |  |  |
| 10 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 11 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 12 | VLR_DESC | VARCHAR2(17) | Y |  |  |
| 13 | VLR_ACRES | VARCHAR2(17) | Y |  |  |
| 14 | VLR_TOT_LIQ | VARCHAR2(17) | Y |  |  |
| 15 | VLR_DESP_ACS | VARCHAR2(17) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 19 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 20 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 21 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 22 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 26 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 27 | CHAVE_SAFX201 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX201: (CHAVE_SAFX201)
- IX_SAFX201_LOTE: (NUM_LOTE)

---

## SAFX2010

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 2 | DATA_X2010 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2010 | VARCHAR2(4000) | Y | NVL("COD_ESTOQUE",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2010: (CHAVE_SAFX2010)
- IX_SAFX2010: (DAT_GRAVACAO)
- IX_SAFX2010_LOTE: (NUM_LOTE)

---

## SAFX2011

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_SIT_BEM | VARCHAR2(3) | Y |  |  |
| 2 | DATA_X2011 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | IND_NAT_BEM | CHAR(1) | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2011 | VARCHAR2(4000) | Y | NVL("COD_SIT_BEM",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2011: (CHAVE_SAFX2011)
- IX_SAFX2011: (DAT_GRAVACAO)
- IX_SAFX2011_LOTE: (NUM_LOTE)

---

## SAFX2012

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 2 | DATA_CFO | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | IND_AGREGADOR | CHAR(1) | Y |  |  |
| 5 | COD_CFO_AGREG | VARCHAR2(4) | Y |  |  |
| 6 | COD_CFO_RELAC | VARCHAR2(4) | Y |  |  |
| 7 | IND_DETALHE_CFO | CHAR(1) | Y |  |  |
| 8 | NAT_OPERACAO | VARCHAR2(3) | Y |  |  |
| 9 | IND_OPERACAO | CHAR(1) | Y |  |  |
| 10 | IND_MERCADO | CHAR(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX2012 | VARCHAR2(4000) | Y | NVL("COD_CFO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2012: (CHAVE_SAFX2012)
- IX_SAFX2012: (DAT_GRAVACAO)
- IX_SAFX2012_LOTE: (NUM_LOTE)

---

## SAFX2013

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 3 | DATA_PRODUTO | VARCHAR2(8) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 6 | COD_NCM | VARCHAR2(10) | Y |  |  |
| 7 | COD_NALADI | VARCHAR2(10) | Y |  |  |
| 8 | IND_REGIDO_SUBST | CHAR(1) | Y |  |  |
| 9 | IND_CONTROLE_SELO | CHAR(1) | Y |  |  |
| 10 | GRUPO_SELO | VARCHAR2(6) | Y |  |  |
| 11 | SUB_GRUPO_SELO | VARCHAR2(6) | Y |  |  |
| 12 | COR_SELO | VARCHAR2(15) | Y |  |  |
| 13 | SERIE_SELO | VARCHAR2(3) | Y |  |  |
| 14 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 15 | COD_GRUPO_PROD | VARCHAR2(5) | Y |  |  |
| 16 | COD_GRP_INCENT | VARCHAR2(5) | Y |  |  |
| 17 | COD_GRUPO_ST | VARCHAR2(2) | Y |  |  |
| 18 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 19 | IND_INCID_ICMS_SER | CHAR(1) | Y |  |  |
| 20 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 21 | VLR_PESO_UNIT_KG | VARCHAR2(13) | Y |  |  |
| 22 | DESCR_DETALHADA | VARCHAR2(250) | Y |  |  |
| 23 | IND_FABRIC_ESTAB | CHAR(1) | Y |  |  |
| 24 | FATOR_CONVERSAO | VARCHAR2(17) | Y |  |  |
| 25 | IND_CLASSIF_ICMSS | CHAR(1) | Y |  |  |
| 26 | DAT_GRAVACAO | DATE | Y |  |  |
| 27 | DSC_MODELO | VARCHAR2(80) | Y |  |  |
| 28 | ORIGEM | CHAR(1) | Y |  |  |
| 29 | COD_GRP_PROD | VARCHAR2(12) | Y |  |  |
| 30 | IND_INCID_PIS | CHAR(1) | Y |  |  |
| 31 | ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 32 | IND_INCID_COFINS | CHAR(1) | Y |  |  |
| 33 | ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 34 | IND_FUNRURAL | CHAR(1) | Y |  |  |
| 35 | IND_PETR_ENERG | CHAR(1) | Y |  |  |
| 36 | IND_PRD_INCENTIV | CHAR(1) | Y |  |  |
| 37 | IND_ICMS_DIFERIDO | CHAR(1) | Y |  |  |
| 38 | CAPAC_VOLUM | VARCHAR2(5) | Y |  |  |
| 39 | ESPECIE_DNF | VARCHAR2(3) | Y |  |  |
| 40 | CLAS_ITEM | VARCHAR2(2) | Y |  |  |
| 41 | COD_BARRAS | VARCHAR2(60) | Y |  |  |
| 42 | COD_ANP | VARCHAR2(12) | Y |  |  |
| 43 | IND_ANT_PROD | CHAR(1) | Y |  |  |
| 44 | COD_ANT_ITEM | VARCHAR2(35) | Y |  |  |
| 45 | DAT_ALT_CODIGO | VARCHAR2(8) | Y |  |  |
| 46 | CLAS_ENQUAD_IPI | VARCHAR2(5) | Y |  |  |
| 47 | MATERIAL_RESULT_PERDA | CHAR(1) | Y |  |  |
| 48 | DSC_FINALIDADE | VARCHAR2(255) | Y |  |  |
| 49 | QTD_CAP_MAX_ARMAZ | VARCHAR2(17) | Y |  |  |
| 50 | IND_ATIVO_SAICS | CHAR(1) | Y |  |  |
| 51 | IND_TAB_INCIDENCIA | VARCHAR2(2) | Y |  |  |
| 52 | COD_GRUPO | VARCHAR2(2) | Y |  |  |
| 53 | MARCA_COMERCIAL | VARCHAR2(60) | Y |  |  |
| 54 | IND_CARAC_PRODUTO | VARCHAR2(1) | Y |  |  |
| 55 | COD_CEST | VARCHAR2(7) | Y |  |  |
| 56 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 57 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 58 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 59 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 60 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 61 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 62 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 63 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 64 | PST_ID | NUMBER | Y |  |  |
| 65 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 66 | IND_INC_RICMS_PR | VARCHAR2(1) | Y |  |  |
| 67 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 68 | CHAVE_SAFX2013 | VARCHAR2(4000) | Y | NVL("IND_PRODUTO",'@')\|\|NVL("COD_PRODUTO",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX2013: (CHAVE_SAFX2013)
- IX_SAFX2013: (DAT_GRAVACAO)
- IX_SAFX2013_LOTE: (NUM_LOTE)

---

## SAFX2014

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_QUITACAO | VARCHAR2(5) | Y |  |  |
| 2 | DATA_X2014 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | NUM_DIAS | VARCHAR2(3) | Y |  |  |
| 5 | VLR_TAXA_MES_ANO | VARCHAR2(7) | Y |  |  |
| 6 | IND_UTILIZ_MES_ANO | CHAR(1) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX2014 | VARCHAR2(4000) | Y | NVL("COD_QUITACAO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2014: (CHAVE_SAFX2014)
- IX_SAFX2014: (DAT_GRAVACAO)
- IX_SAFX2014_LOTE: (NUM_LOTE)

---

## SAFX2015

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OPER_OIL | VARCHAR2(10) | Y |  |  |
| 2 | DAT_X2015 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2015 | VARCHAR2(4000) | Y | NVL("COD_OPER_OIL",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2015: (CHAVE_SAFX2015)
- IX_SAFX2015_LOTE: (NUM_LOTE)

---

## SAFX2016

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PROJETO | VARCHAR2(20) | Y |  |  |
| 2 | DAT_X2016 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | DAT_INI | VARCHAR2(8) | Y |  |  |
| 5 | DAT_FIM | VARCHAR2(8) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | VLR_TOT_PROJETO | VARCHAR2(17) | Y |  |  |
| 8 | VLR_SALDO_PROJETO | VARCHAR2(17) | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX2016 | VARCHAR2(4000) | Y | NVL("COD_PROJETO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2016: (CHAVE_SAFX2016)
- IX_SAFX2016_LOTE: (NUM_LOTE)

---

## SAFX2017

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 2 | DATA_X2017 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | IND_UNID_FRAC | CHAR(1) | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2017 | VARCHAR2(4000) | Y | NVL("COD_UND_PADRAO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2017: (CHAVE_SAFX2017)
- IX_SAFX2017: (DAT_GRAVACAO)
- IX_SAFX2017_LOTE: (NUM_LOTE)

---

## SAFX2018

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 2 | DATA_X2018 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | IND_TP_SERVICO | CHAR(1) | Y |  |  |
| 5 | IND_MAT_SERV | CHAR(1) | Y |  |  |
| 6 | IND_CONTRATO | CHAR(1) | Y |  |  |
| 7 | IND_SERVICOS_TERC | CHAR(1) | Y |  |  |
| 8 | COD_NAT_SERV | VARCHAR2(35) | Y |  |  |
| 9 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 12 | INSS | CHAR(1) | Y |  |  |
| 13 | ISS | CHAR(1) | Y |  |  |
| 14 | IRRF | CHAR(1) | Y |  |  |
| 15 | ALIQUOTA_INSS | VARCHAR2(8) | Y |  |  |
| 16 | ALIQUOTA_ISS | VARCHAR2(8) | Y |  |  |
| 17 | ALIQUOTA_IRRF | VARCHAR2(8) | Y |  |  |
| 18 | VLR_ALIQ_INSC | VARCHAR2(7) | Y |  |  |
| 19 | VLR_ALIQ_S_INSC | VARCHAR2(7) | Y |  |  |
| 20 | VLR_PERC_FRETE_AUT | VARCHAR2(17) | Y |  |  |
| 21 | COD_SERV_LEI_116 | VARCHAR2(4) | Y |  |  |
| 22 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 23 | IND_DEDUCAO | CHAR(1) | Y |  | 1-(40%)Serviço de recapeamento asfáltico e pavimentação; 2-(30%)Serviço de construção civil, obras hidráulicas, outras semelhantes e Serviço de construção de imóveis (notas emitidas a partir de 14/11/2000 - Decreto 18.698/00); 3-(25%)Serviço de Conservação de imóveis (notas emitidas até 13/11/2000); 4-(10%)Serviço de Terraplanagem; 5-SEM qualquer dedução; 6-COM dedução através de Mapas de Materiais e Subempreitadas;  |
| 24 | COD_ATIVIDADE | VARCHAR2(7) | Y |  |  |
| 25 | COD_NAT_SERV_SPED | VARCHAR2(60) | Y |  |  |
| 26 | DESC_NAT_SERV_SPED | VARCHAR2(100) | Y |  |  |
| 27 | PST_ID | NUMBER | Y |  |  |
| 28 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 29 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 30 | CHAVE_SAFX2018 | VARCHAR2(4000) | Y | NVL("COD_SERVICO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2018: (CHAVE_SAFX2018)
- IX_SAFX2018: (DAT_GRAVACAO)
- IX_SAFX2018_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX2018_LOTE: (NUM_LOTE)

---

## SAFX2019

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 2 | DATA_X2019 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | IND_INCID_REINF | CHAR(1) | Y |  |  |
| 6 | IND_CLASSIF_REINF | CHAR(1) | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2019 | VARCHAR2(4000) | Y | NVL("COD_DARF",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2019: (CHAVE_SAFX2019)
- IX_SAFX2019: (DAT_GRAVACAO)
- IX_SAFX2019_LOTE: (NUM_LOTE)

---

## SAFX202

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_EQUIP | VARCHAR2(9) | Y |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | Y |  |  |
| 5 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 6 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 7 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 10 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 11 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 12 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 13 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 14 | QTDE | VARCHAR2(17) | Y |  |  |
| 15 | VLR_UNIT | VARCHAR2(19) | Y |  |  |
| 16 | VLR_ITEM | VARCHAR2(17) | Y |  |  |
| 17 | VLR_DESC | VARCHAR2(17) | Y |  |  |
| 18 | VLR_ACRES | VARCHAR2(17) | Y |  |  |
| 19 | VLR_TOT_LIQ | VARCHAR2(17) | Y |  |  |
| 20 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 21 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 22 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 23 | COD_SIT_TRIB_PIS | VARCHAR2(2) | Y |  |  |
| 24 | QTD_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 25 | VLR_ALIQ_PIS_R | VARCHAR2(19) | Y |  |  |
| 26 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 27 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 28 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 29 | COD_SIT_TRIB_COFINS | VARCHAR2(2) | Y |  |  |
| 30 | QTD_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 31 | VLR_ALIQ_COFINS_R | VARCHAR2(19) | Y |  |  |
| 32 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 33 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 34 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 35 | VLR_BASE_PIS_ST | VARCHAR2(17) | Y |  |  |
| 36 | VLR_PIS_ST | VARCHAR2(17) | Y |  |  |
| 37 | VLR_ALIQ_PIS_ST | VARCHAR2(7) | Y |  |  |
| 38 | VLR_BASE_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 39 | VLR_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 40 | VLR_ALIQ_COFINS_ST | VARCHAR2(7) | Y |  |  |
| 41 | VLR_DESP_ACS | VARCHAR2(17) | Y |  |  |
| 42 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 43 | DAT_GRAVACAO | DATE | Y |  |  |
| 44 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 45 | VLR_EXC_BASE_PISCOFINS | VARCHAR2(17) | Y |  |  |
| 46 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 47 | PST_ID | NUMBER | Y |  |  |
| 48 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 49 | CHAVE_SAFX202 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX202: (CHAVE_SAFX202)
- IX_SAFX202_LOTE: (NUM_LOTE)

---

## SAFX2020

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 2 | DATA_X2020 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2020 | VARCHAR2(4000) | Y | NVL("COD_HISTPADRAO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2020: (CHAVE_SAFX2020)
- IX_SAFX2020: (DAT_GRAVACAO)
- IX_SAFX2020_LOTE: (NUM_LOTE)

---

## SAFX2021

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 2 | DATA_X2021 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2021 | VARCHAR2(4000) | Y | NVL("COD_ALMOX",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2021: (CHAVE_SAFX2021)
- IX_SAFX2021: (DAT_GRAVACAO)
- IX_SAFX2021_LOTE: (NUM_LOTE)

---

## SAFX2022

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_MOVPATR | VARCHAR2(3) | Y |  |  |
| 2 | DATA_X2022 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | IND_SINAL_MOVTO | CHAR(1) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2022 | VARCHAR2(4000) | Y | NVL("COD_TIPO_MOVPATR",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2022: (CHAVE_SAFX2022)
- IX_SAFX2022: (DAT_GRAVACAO)
- IX_SAFX2022_LOTE: (NUM_LOTE)

---

## SAFX2023

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 2 | DATA_X2023 | VARCHAR2(8) | Y |  |  |
| 3 | IND_VERBA | CHAR(1) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | INCID_RAIS | CHAR(1) | Y |  |  |
| 6 | INCID_DIRF | CHAR(1) | Y |  |  |
| 7 | TRIB_IR | CHAR(1) | Y |  |  |
| 8 | COMPOE_SAL | CHAR(1) | Y |  |  |
| 9 | COD_CONTA_CRED | VARCHAR2(70) | Y |  |  |
| 10 | COD_CONTA_DEB | VARCHAR2(70) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | IND_DECIMO_TERC | CHAR(1) | Y |  |  |
| 13 | INCID_INSS | CHAR(1) | Y |  |  |
| 14 | IND_IN86_IN89 | CHAR(1) | Y | 'S' |  |
| 15 | IND_PREV_SOCIAL | VARCHAR2(2) | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX2023 | VARCHAR2(4000) | Y | NVL("COD_VERBA",'@')\|\|NVL("IND_VERBA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2023: (CHAVE_SAFX2023)
- IX_SAFX2023: (DAT_GRAVACAO)
- IX_SAFX2023_LOTE: (NUM_LOTE)

---

## SAFX2024

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 2 | DATA_X2024 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2024 | VARCHAR2(4000) | Y | NVL("COD_MODELO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2024: (CHAVE_SAFX2024)
- IX_SAFX2024: (DAT_GRAVACAO)
- IX_SAFX2024_LOTE: (NUM_LOTE)

---

## SAFX2025

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MARCA_COM | VARCHAR2(6) | Y |  |  |
| 2 | DATA_X2025 | VARCHAR2(8) | Y |  |  |
| 3 | DSC_MARCA_COM | VARCHAR2(50) | Y |  |  |
| 4 | NUM_REGISTRO | VARCHAR2(15) | Y |  |  |
| 5 | DSC_CLASS_AMBIE | VARCHAR2(3) | Y |  |  |
| 6 | DSC_CLASS_TOXIC | VARCHAR2(3) | Y |  |  |
| 7 | IND_CLASSE_USO | VARCHAR2(2) | Y |  |  |
| 8 | DSC_OUTRAS | VARCHAR2(100) | Y |  |  |
| 9 | UF_REGISTRO | VARCHAR2(2) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX2025 | VARCHAR2(4000) | Y | NVL("COD_MARCA_COM",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2025: (CHAVE_SAFX2025)
- IX_SAFX2025: (DAT_GRAVACAO)
- IX_SAFX2025_LOTE: (NUM_LOTE)

---

## SAFX2027

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ADMISSAO | VARCHAR2(1) | Y |  |  |
| 2 | DATA_X2027 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2027 | VARCHAR2(4000) | Y | NVL("COD_ADMISSAO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2027: (CHAVE_SAFX2027)
- IX_SAFX2027: (DAT_GRAVACAO)
- IX_SAFX2027_LOTE: (NUM_LOTE)

---

## SAFX2028

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CAUSA_DESLIG | VARCHAR2(2) | Y |  |  |
| 2 | DATA_X2028 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2028 | VARCHAR2(4000) | Y | NVL("COD_CAUSA_DESLIG",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2028: (CHAVE_SAFX2028)
- IX_SAFX2028: (DAT_GRAVACAO)
- IX_SAFX2028_LOTE: (NUM_LOTE)

---

## SAFX2029

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CBO | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2029 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2029 | VARCHAR2(4000) | Y | NVL("COD_CBO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2029: (CHAVE_SAFX2029)
- IX_SAFX2029: (DAT_GRAVACAO)
- IX_SAFX2029_LOTE: (NUM_LOTE)

---

## SAFX203

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_SIT_TRIB_PIS | VARCHAR2(2) | Y |  |  |
| 5 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 6 | COD_SIT_TRIB_COFINS | VARCHAR2(2) | Y |  |  |
| 7 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 8 | COD_REC_DED_EXC | VARCHAR2(5) | Y |  |  |
| 9 | COD_ATRIBUTO | VARCHAR2(3) | Y |  |  |
| 10 | COD_REC_DED_EXC_COMPL | VARCHAR2(20) | Y |  |  |
| 11 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 12 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 13 | VLR_AJUSTE | VARCHAR2(17) | Y |  |  |
| 14 | IND_AJUSTE | CHAR(1) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX203 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX203: (CHAVE_SAFX203)
- IX_SAFX203_LOTE: (NUM_LOTE)

---

## SAFX2030

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VINCULO_EMP | VARCHAR2(2) | Y |  |  |
| 2 | DATA_X2030 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | IND_VINC_EMPREG | CHAR(1) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2030 | VARCHAR2(4000) | Y | NVL("COD_VINCULO_EMP",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2030: (CHAVE_SAFX2030)
- IX_SAFX2030: (DAT_GRAVACAO)
- IX_SAFX2030_LOTE: (NUM_LOTE)

---

## SAFX2031

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INSTRUCAO | VARCHAR2(2) | Y |  |  |
| 2 | DATA_X2031 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2031 | VARCHAR2(4000) | Y | NVL("COD_INSTRUCAO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2031: (CHAVE_SAFX2031)
- IX_SAFX2031: (DAT_GRAVACAO)
- IX_SAFX2031_LOTE: (NUM_LOTE)

---

## SAFX2032

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_SALARIO | VARCHAR2(1) | Y |  |  |
| 2 | DATA_X2032 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2032 | VARCHAR2(4000) | Y | NVL("COD_TIPO_SALARIO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2032: (CHAVE_SAFX2032)
- IX_SAFX2032: (DAT_GRAVACAO)
- IX_SAFX2032_LOTE: (NUM_LOTE)

---

## SAFX2033

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO_CIVIL | VARCHAR2(1) | Y |  |  |
| 2 | DATA_X2033 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2033 | VARCHAR2(4000) | Y | NVL("COD_ESTADO_CIVIL",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2033: (CHAVE_SAFX2033)
- IX_SAFX2033: (DAT_GRAVACAO)
- IX_SAFX2033_LOTE: (NUM_LOTE)

---

## SAFX2034

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_OCORRENCIA | VARCHAR2(2) | Y |  |  |
| 2 | DATA_X2034 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | COD_MODULO | VARCHAR2(2) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2034 | VARCHAR2(4000) | Y | NVL("COD_OCORRENCIA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2034: (CHAVE_SAFX2034)
- IX_SAFX2034: (DAT_GRAVACAO)
- IX_SAFX2034_LOTE: (NUM_LOTE)

---

## SAFX2035

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIPO_DEPEND | VARCHAR2(2) | Y |  |  |
| 2 | DATA_X2035 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | INCIDENCIA_IR | CHAR(1) | Y |  |  |
| 5 | INCIDENCIA_SF | CHAR(1) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2035 | VARCHAR2(4000) | Y | NVL("COD_TIPO_DEPEND",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2035: (CHAVE_SAFX2035)
- IX_SAFX2035: (DAT_GRAVACAO)
- IX_SAFX2035_LOTE: (NUM_LOTE)

---

## SAFX2036

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_FUNCAO | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2036 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2036 | VARCHAR2(4000) | Y | NVL("COD_FUNCAO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2036: (CHAVE_SAFX2036)
- IX_SAFX2036: (DAT_GRAVACAO)
- IX_SAFX2036_LOTE: (NUM_LOTE)

---

## SAFX2037

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2037 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | COD_SETOR_SUP | VARCHAR2(10) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | VALID_FINAL | VARCHAR2(8) | Y |  |  |
| 7 | TIPO_LOTACAO_TRIB | VARCHAR2(2) | Y |  |  |
| 8 | TIPO_INSC_LOTACAO | CHAR(1) | Y |  |  |
| 9 | NUM_INSC_LOTACAO | VARCHAR2(15) | Y |  |  |
| 10 | COD_FPAS | VARCHAR2(3) | Y |  |  |
| 11 | COD_TERCEIROS | VARCHAR2(4) | Y |  |  |
| 12 | COD_COMB_TERCEIROS | VARCHAR2(4) | Y |  |  |
| 13 | COD_TERCEIROS_PROCESSO | VARCHAR2(4) | Y |  |  |
| 14 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 15 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 16 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | ALIQ_GILRAT | VARCHAR2(1) | Y |  |  |
| 21 | VLR_FAP | VARCHAR2(5) | Y |  |  |
| 22 | CHAVE_SAFX2037 | VARCHAR2(4000) | Y | NVL("COD_SETOR",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2037: (CHAVE_SAFX2037)
- IX_SAFX2037: (DAT_GRAVACAO)
- IX_SAFX2037_LOTE: (NUM_LOTE)

---

## SAFX204

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_EQUIP | VARCHAR2(9) | Y |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | Y |  |  |
| 5 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 6 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 7 | NUM_COMP_PAG | VARCHAR2(18) | Y |  |  |
| 8 | IND_NAT_OPER | CHAR(1) | Y |  |  |
| 9 | VLR_OPERACAO | VARCHAR2(17) | Y |  |  |
| 10 | CEP | VARCHAR2(8) | Y |  |  |
| 11 | NUM_PONTO_VENDA | VARCHAR2(8) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX204 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX204: (CHAVE_SAFX204)
- IX_SAFX204_LOTE: (NUM_LOTE)

---

## SAFX2042

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2042 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2042 | VARCHAR2(4000) | Y | NVL("COD_VOLUME",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2042: (CHAVE_SAFX2042)
- IX_SAFX2042: (DAT_GRAVACAO)
- IX_SAFX2042_LOTE: (NUM_LOTE)

---

## SAFX2043

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 2 | DATA_NBM | VARCHAR2(8) | Y |  |  |
| 3 | IND_TRIB_NBM | CHAR(1) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 6 | SECAO_IPI | VARCHAR2(2) | Y |  |  |
| 7 | NOTA_SECAO_IPI | VARCHAR2(2) | Y |  |  |
| 8 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 9 | GRUPO_APURAC | VARCHAR2(5) | Y |  |  |
| 10 | IND_INCIDENCIA | CHAR(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | EX_IPI | VARCHAR2(3) | Y |  |  |
| 16 | CHAVE_SAFX2043 | VARCHAR2(4000) | Y | NVL("COD_NBM",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2043: (CHAVE_SAFX2043)
- IX_SAFX2043: (DAT_GRAVACAO)
- IX_SAFX2043_LOTE: (NUM_LOTE)

---

## SAFX2044

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 2 | DATA_X2044 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2044 | VARCHAR2(4000) | Y | NVL("COD_FEDERAL",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2044: (CHAVE_SAFX2044)
- IX_SAFX2044: (DAT_GRAVACAO)
- IX_SAFX2044_LOTE: (NUM_LOTE)

---

## SAFX2045

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NCM | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2045 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | ALIQUOTA_NCM | VARCHAR2(7) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2045 | VARCHAR2(4000) | Y | NVL("COD_NCM",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2045: (CHAVE_SAFX2045)
- IX_SAFX2045: (DAT_GRAVACAO)
- IX_SAFX2045_LOTE: (NUM_LOTE)

---

## SAFX2047

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VIA_TRANSP | VARCHAR2(5) | Y |  |  |
| 2 | DATA_X2047 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | COD_VIA_TRANSP_SP | VARCHAR2(5) | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2047 | VARCHAR2(4000) | Y | NVL("COD_VIA_TRANSP",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2047: (CHAVE_SAFX2047)
- IX_SAFX2047: (DAT_GRAVACAO)
- IX_SAFX2047_LOTE: (NUM_LOTE)

---

## SAFX2048

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_SINDICATO | VARCHAR2(5) | Y |  |  |
| 2 | DATA_X2048 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | MUNICIPIO | VARCHAR2(20) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | CNPJ_SINDICATO | VARCHAR2(14) | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2048 | VARCHAR2(4000) | Y | NVL("COD_SINDICATO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2048: (CHAVE_SAFX2048)
- IX_SAFX2048: (DAT_GRAVACAO)
- IX_SAFX2048_LOTE: (NUM_LOTE)

---

## SAFX2049

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_VEIC_TRANSP | VARCHAR2(6) | Y |  |  |
| 2 | DATA_X2049 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | MARCA_VEIC | VARCHAR2(30) | Y |  |  |
| 5 | MODELO_VEIC | VARCHAR2(30) | Y |  |  |
| 6 | ANO_VEIC | VARCHAR2(4) | Y |  |  |
| 7 | CERTIFICADO_VEIC | VARCHAR2(30) | Y |  |  |
| 8 | UF_CERTIFICADO | VARCHAR2(2) | Y |  |  |
| 9 | PLACA_VEIC | VARCHAR2(17) | Y |  |  |
| 10 | UF_PLACA | VARCHAR2(2) | Y |  |  |
| 11 | IND_VEIC_AQUAVIARIO | CHAR(1) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX2049 | VARCHAR2(4000) | Y | NVL("COD_VEIC_TRANSP",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2049: (CHAVE_SAFX2049)
- IX_SAFX2049: (DAT_GRAVACAO)
- IX_SAFX2049_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX2049_LOTE: (NUM_LOTE)

---

## SAFX205

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 13 | NUM_COMP_PAG | VARCHAR2(18) | Y |  |  |
| 14 | IND_NAT_OPER | CHAR(1) | Y |  |  |
| 15 | VLR_OPERACAO | VARCHAR2(17) | Y |  |  |
| 16 | CEP | VARCHAR2(8) | Y |  |  |
| 17 | NUM_PONTO_VENDA | VARCHAR2(8) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX205 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX205: (CHAVE_SAFX205)
- IX_SAFX205_LOTE: (NUM_LOTE)

---

## SAFX2050
**Comment**: Produtos Incentivados - ICMS - ZFM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  | Código da Empresa |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  | Código do Estabelecimento |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | Y |  | Inscrição Estadual do Estabelecimento na ZFM |
| 4 | COD_LINHA_PRD | VARCHAR2(5) | Y |  | Linha de Incentivo a qual pertence o produto incentivado |
| 5 | IND_PRODUTO | CHAR(1) | Y |  | Indicador do Produto |
| 6 | COD_PRODUTO | VARCHAR2(60) | Y |  | Código do Produto |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2050 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2050: (CHAVE_SAFX2050)
- IX_SAFX2050_LOTE: (NUM_LOTE)

---

## SAFX2051

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_POSTO | VARCHAR2(6) | Y |  |  |
| 3 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 4 | CNPJ | VARCHAR2(14) | Y |  |  |
| 5 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 6 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 7 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 8 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 9 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 10 | UF | VARCHAR2(2) | Y |  |  |
| 11 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 12 | CEP | VARCHAR2(8) | Y |  |  |
| 13 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 14 | IND_ATENDIMENTO | CHAR(1) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX2051 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_POSTO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2051: (CHAVE_SAFX2051)
- IX_SAFX2051_LOTE: (NUM_LOTE)
- IX_X2051: (DAT_GRAVACAO)

---

## SAFX2053

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_GRUPO_BEM | VARCHAR2(9) | Y |  |  |
| 4 | DATA_VALID_GRUPO | VARCHAR2(8) | Y |  |  |
| 5 | IND_IDENT_GRUPO | VARCHAR2(2) | Y |  |  |
| 6 | DESC_COMPL_GRUPO | VARCHAR2(255) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX2053 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2053: (CHAVE_SAFX2053)
- IX_SAFX2053: (DAT_GRAVACAO)
- IX_SAFX2053_LOTE: (NUM_LOTE)

---

## SAFX2054

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_UNID_IMOB | VARCHAR2(11) | Y |  |  |
| 4 | DATA_INI_VALID | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_UNID_IMOB | VARCHAR2(2) | Y |  |  |
| 6 | ID_NOME_EMPR | VARCHAR2(255) | Y |  |  |
| 7 | DESC_RES_UNID_IMOB | VARCHAR2(90) | Y |  |  |
| 8 | IND_NAT_EMPR | VARCHAR2(1) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | IND_TP_IMOVEL | CHAR(1) | Y |  |  |
| 11 | ENDERECO | VARCHAR2(60) | Y |  |  |
| 12 | COD_UF | VARCHAR2(2) | Y |  |  |
| 13 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 14 | CEP | VARCHAR2(8) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX2054 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2054: (CHAVE_SAFX2054)
- IX_SAFX2054_LOTE: (NUM_LOTE)

---

## SAFX2055

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NBS | VARCHAR2(9) | Y |  |  |
| 2 | DATA_X2055 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(255) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2055 | VARCHAR2(4000) | Y | NVL("COD_NBS",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2055: (CHAVE_SAFX2055)
- IX_SAFX2055_LOTE: (NUM_LOTE)

---

## SAFX2056

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_HIST_FATO_CONTABIL | VARCHAR2(6) | Y |  |  |
| 2 | DATA_X2056 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2056 | VARCHAR2(4000) | Y | NVL("COD_HIST_FATO_CONTABIL",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2056: (CHAVE_SAFX2056)
- IX_SAFX2056_LOTE: (NUM_LOTE)

---

## SAFX2057

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 4 | DATA_X2057 | VARCHAR2(8) | Y |  |  |
| 5 | DSC_SCP | VARCHAR2(100) | Y |  |  |
| 6 | DSC_INF_COMPL | VARCHAR2(100) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | DATA_VALID_FIM | VARCHAR2(8) | Y |  |  |
| 9 | IND_DIRF | CHAR(1) | Y | 'N' |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX2057 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2057: (CHAVE_SAFX2057)
- IX_SAFX2057_LOTE: (NUM_LOTE)

---

## SAFX2058

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 2 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 3 | VALID_PROC_ADJ_INI | VARCHAR2(8) | Y |  |  |
| 4 | VALID_PROC_ADJ_FIM | VARCHAR2(8) | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 7 | COD_VARA | VARCHAR2(4) | Y |  |  |
| 8 | IND_AUTORIA | CHAR(1) | Y |  |  |
| 9 | IND_REINF | CHAR(1) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | IND_INCIDENCIA_ESOCIAL | CHAR(1) | Y |  |  |
| 12 | IND_MATERIA_PROC | VARCHAR2(2) | Y |  |  |
| 13 | IND_ABRANGENCIA_PROC | CHAR(1) | Y |  |  |
| 14 | DSC_OBSERVACAO | VARCHAR2(255) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX2058 | VARCHAR2(4000) | Y | NVL("IND_TP_PROC_ADJ",'@')\|\|NVL("NUM_PROC_ADJ",... |  |

**Indexes**:
- IX_CHAVE_SAFX2058: (CHAVE_SAFX2058)
- IX_SAFX2058: (DAT_GRAVACAO)
- IX_SAFX2058_LOTE: (NUM_LOTE)

---

## SAFX2059

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 2 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 3 | VALID_PROC_ADJ_INI | VARCHAR2(8) | Y |  |  |
| 4 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 5 | IND_SUSP | VARCHAR2(2) | Y |  |  |
| 6 | DAT_DECISAO | VARCHAR2(8) | Y |  |  |
| 7 | IND_DEPOSITO | CHAR(1) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX2059 | VARCHAR2(4000) | Y | NVL("IND_TP_PROC_ADJ",'@')\|\|NVL("NUM_PROC_ADJ",... |  |

**Indexes**:
- IX_CHAVE_SAFX2059: (CHAVE_SAFX2059)
- IX_SAFX2059: (DAT_GRAVACAO)
- IX_SAFX2059_LOTE: (NUM_LOTE)

---

## SAFX206

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | COD_CARACT | VARCHAR2(3) | Y |  |  |
| 17 | NUM_BOLETIM_CONF | VARCHAR2(35) | Y |  |  |
| 18 | COD_METODO | VARCHAR2(3) | Y |  |  |
| 19 | COD_VAL_CARACT | VARCHAR2(20) | Y |  |  |
| 20 | VAL_MASSA_ESPEC | VARCHAR2(19) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | PST_ID | NUMBER | Y |  |  |
| 23 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 24 | CHAVE_SAFX206 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX206: (CHAVE_SAFX206)
- IX_SAFX206_LOTE: (NUM_LOTE)

---

## SAFX2060

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_TANQUE | VARCHAR2(10) | Y |  |  |
| 4 | DAT_X2060 | VARCHAR2(8) | Y |  |  |
| 5 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 7 | QTD_CAPAC | VARCHAR2(17) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | VLR_UNIT_PRD | VARCHAR2(18) | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX2060 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2060: (CHAVE_SAFX2060)
- IX_SAFX2060: (DAT_GRAVACAO)
- IX_SAFX2060_LOTE: (NUM_LOTE)

---

## SAFX2061

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_BOMBA | VARCHAR2(10) | Y |  |  |
| 4 | DAT_X2061 | VARCHAR2(8) | Y |  |  |
| 5 | SERIE_BOMBA | VARCHAR2(12) | Y |  |  |
| 6 | FABRICANTE | VARCHAR2(80) | Y |  |  |
| 7 | DSC_MODELO | VARCHAR2(20) | Y |  |  |
| 8 | IND_TP_MEDICAO | CHAR(1) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | CNPJ_FABRICANTE | VARCHAR2(14) | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX2061 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2061: (CHAVE_SAFX2061)
- IX_SAFX2061: (DAT_GRAVACAO)
- IX_SAFX2061_LOTE: (NUM_LOTE)

---

## SAFX2062

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_BOMBA | VARCHAR2(10) | Y |  |  |
| 4 | NUM_BICO | VARCHAR2(10) | Y |  |  |
| 5 | DAT_X2062 | VARCHAR2(8) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2062 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2062: (CHAVE_SAFX2062)
- IX_SAFX2062: (DAT_GRAVACAO)
- IX_SAFX2062_LOTE: (NUM_LOTE)

---

## SAFX2063

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 2 | COD_INF_ADIC | VARCHAR2(8) | Y |  |  |
| 3 | DSC_INF | VARCHAR2(250) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 7 | CHAVE_SAFX2063 | VARCHAR2(4000) | Y | NVL("COD_ESTADO",'@')\|\|NVL("COD_INF_ADIC",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2063: (CHAVE_SAFX2063)

---

## SAFX2064

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_MATRIZ_FILIAL | VARCHAR2(1) | Y |  |  |
| 4 | COD_CLASSE | VARCHAR2(2) | Y |  |  |
| 5 | CGC | VARCHAR2(14) | Y |  |  |
| 6 | COD_ATIVIDADE | VARCHAR2(7) | Y |  |  |
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
| 18 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 19 | CEP | VARCHAR2(8) | Y |  |  |
| 20 | DDD | VARCHAR2(5) | Y |  |  |
| 21 | TELEFONE | VARCHAR2(10) | Y |  |  |
| 22 | FAX | VARCHAR2(10) | Y |  |  |
| 23 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 24 | IND_VENDA_AMB | VARCHAR2(1) | Y |  |  |
| 25 | IND_DIRF_CENTRAL | VARCHAR2(1) | Y |  |  |
| 26 | TP_LOGRADOURO | VARCHAR2(3) | Y |  |  |
| 27 | ITENS_NOTA | VARCHAR2(2) | Y |  |  |
| 28 | IMPRIME | VARCHAR2(1) | Y |  |  |
| 29 | MULT_SERIE_S | VARCHAR2(1) | Y |  |  |
| 30 | NUM_PPVI_SN | VARCHAR2(1) | Y |  |  |
| 31 | SEQ_UNICO | VARCHAR2(1) | Y |  |  |
| 32 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 33 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 34 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 35 | IND_ST_NCONTRIB | VARCHAR2(1) | Y |  |  |
| 36 | MARGEM_ST_NCONTRIB | VARCHAR2(5) | Y |  |  |
| 37 | COD_MUNIC_ISS | VARCHAR2(7) | Y |  |  |
| 38 | COD_TP_RECOLH | VARCHAR2(3) | Y |  |  |
| 39 | IND_FORMA_ABAT | VARCHAR2(1) | Y |  |  |
| 40 | IND_NUMERACAO | VARCHAR2(1) | Y |  |  |
| 41 | EMAIL | VARCHAR2(50) | Y |  |  |
| 42 | IND_NBM_IEST | VARCHAR2(1) | Y |  |  |
| 43 | IND_CONTRIB_IPI | VARCHAR2(1) | Y |  |  |
| 44 | IND_CONTRIB_SUB | VARCHAR2(1) | Y |  |  |
| 45 | DAT_INI_ATIVIDADE | VARCHAR2(8) | Y |  |  |
| 46 | IND_APROVADOR | VARCHAR2(1) | Y |  |  |
| 47 | INSC_DF | VARCHAR2(14) | Y |  |  |
| 48 | IND_IMUNE | VARCHAR2(1) | Y |  |  |
| 49 | IND_ISENTO | VARCHAR2(1) | Y |  |  |
| 50 | IND_ESCR_CONTAB | VARCHAR2(1) | Y |  |  |
| 51 | DATA_JUCEMAT | VARCHAR2(8) | Y |  |  |
| 52 | DATA_SEFAZ | VARCHAR2(8) | Y |  |  |
| 53 | IND_SECUNDARIO | VARCHAR2(1) | Y |  |  |
| 54 | IND_IPI_SJ | VARCHAR2(1) | Y |  |  |
| 55 | IND_IPISJ_REGRA_RB | VARCHAR2(1) | Y |  |  |
| 56 | DT_ENCERRAMENTO | VARCHAR2(8) | Y |  |  |
| 57 | CEI_PORT63 | VARCHAR2(12) | Y |  |  |
| 58 | INSC_PORT63 | VARCHAR2(12) | Y |  |  |
| 59 | NUM_THREADS_MMAG | VARCHAR2(22) | Y |  |  |
| 60 | CX_POSTAL | VARCHAR2(20) | Y |  |  |
| 61 | NUM_CEP_CX_POSTAL | VARCHAR2(22) | Y |  |  |
| 62 | COD_BENEF_ICMS | VARCHAR2(5) | Y |  |  |
| 63 | COD_BENEF_ISS | VARCHAR2(5) | Y |  |  |
| 64 | NUM_PROTOCOLO | VARCHAR2(10) | Y |  |  |
| 65 | DATA_PROTOCOLO | VARCHAR2(8) | Y |  |  |
| 66 | DATA_CISAO | VARCHAR2(8) | Y |  |  |
| 67 | DATA_FUSAO | VARCHAR2(8) | Y |  |  |
| 68 | DATA_INCORPORACAO | VARCHAR2(8) | Y |  |  |
| 69 | DAT_VALIDADE_INI_ATIVIDADE | VARCHAR2(8) | Y |  |  |
| 70 | IND_ATIVIDADE | VARCHAR2(1) | Y |  |  |
| 71 | IND_APUR_ICMS | VARCHAR2(1) | Y |  |  |
| 72 | IND_APUR_IPI | VARCHAR2(1) | Y |  |  |
| 73 | IND_CONV_ICMS | VARCHAR2(1) | Y |  |  |
| 74 | DAT_OPERACAO | VARCHAR2(8) | Y |  |  |
| 75 | USUARIO | VARCHAR2(40) | Y |  |  |
| 76 | IND_ISS | VARCHAR2(2) | Y |  |  |
| 77 | IND_ATIV_BASE_CALC_REDUZ | VARCHAR2(2) | Y |  |  |
| 78 | TIPO_ASSINANTE | VARCHAR2(1) | Y |  |  |
| 79 | NAT_PESSOA_JUR | VARCHAR2(2) | Y |  |  |
| 80 | COD_INST_FINANC | VARCHAR2(10) | Y |  |  |
| 81 | IND_CONTRIB_EQ_CCIVIL | VARCHAR2(1) | Y |  |  |
| 82 | NUM_ALVARA | VARCHAR2(11) | Y |  |  |
| 83 | IND_INST_FINANCEIRA | VARCHAR2(1) | Y |  |  |
| 84 | IND_REG_APUR_CONT_PREV | VARCHAR2(1) | Y |  |  |
| 85 | CERTIFICADO_DIGITAL | VARCHAR2(200) | Y |  |  |
| 86 | COD_ARI_ANP | VARCHAR2(10) | Y |  |  |
| 87 | COD_INSTAL_ANP | VARCHAR2(7) | Y |  |  |
| 88 | COMPL_ENDERECO_EFD | VARCHAR2(60) | Y |  |  |
| 89 | IND_ATIV_FINANCEIRA | VARCHAR2(1) | Y |  |  |
| 90 | DSC_INF_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |
| 91 | RAZAO_SOCIAL_COMPL | VARCHAR2(250) | Y |  |  |
| 92 | BAIRRO_COMPL | VARCHAR2(60) | Y |  |  |
| 93 | COD_MOBILIARIO | VARCHAR2(9) | Y |  |  |
| 94 | DAT_TRANSF_SEDE | VARCHAR2(8) | Y |  |  |
| 95 | DAT_TRANSF | VARCHAR2(8) | Y |  |  |
| 96 | IND_CLAS_ESTAB | VARCHAR2(2) | Y |  |  |
| 97 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 98 | PST_ID | NUMBER | Y |  |  |
| 99 | DAT_GRAVACAO | DATE | Y |  |  |
| 100 | COD_NAT_JUR | VARCHAR2(4) | Y |  |  |
| 101 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 102 | CHAVE_SAFX2064 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2064: (CHAVE_SAFX2064)
- IX_SAFX2064: (DAT_GRAVACAO)
- IX_SAFX2064_LOTE: (NUM_LOTE)

---

## SAFX207

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 5 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 6 | IND_FOLHA | VARCHAR2(2) | Y |  |  |
| 7 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 8 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 9 | CNPJ_PREVIDENCIA | VARCHAR2(14) | Y |  |  |
| 10 | DSC_NOME_PREVIDENCIA | VARCHAR2(150) | Y |  |  |
| 11 | IND_TP_PREVIDENCIA | VARCHAR2(2) | Y |  |  |
| 12 | VLR_VERBA | VARCHAR2(17) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX207 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX207: (CHAVE_SAFX207)
- IX_SAFX207: (DAT_GRAVACAO)
- IX_SAFX207_LOTE: (NUM_LOTE)

---

## SAFX208

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 5 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 6 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 7 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 8 | CPF_CNPJ_PREST_SERV | VARCHAR2(14) | Y |  |  |
| 9 | DSC_PREST_SERV | VARCHAR2(150) | Y |  |  |
| 10 | VLR_REEMBOLSO | VARCHAR2(17) | Y |  |  |
| 11 | VLR_REEMBOLSO_ANT | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX208 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX208: (CHAVE_SAFX208)
- IX_SAFX208: (DAT_GRAVACAO)
- IX_SAFX208_LOTE: (NUM_LOTE)

---

## SAFX2080

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 2 | DATA_X2080 | VARCHAR2(8) | Y |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2080 | VARCHAR2(4000) | Y | NVL("COD_RECEITA_EST",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2080: (CHAVE_SAFX2080)
- IX_SAFX2080: (DAT_GRAVACAO)
- IX_SAFX2080_LOTE: (NUM_LOTE)

---

## SAFX2081

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 2 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 3 | DATA_X2081 | VARCHAR2(8) | Y |  |  |
| 4 | IND_APLICACAO | VARCHAR2(1) | Y |  |  |
| 5 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 6 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX2081 | VARCHAR2(4000) | Y | NVL("COD_CFO",'@')\|\|NVL("COD_NATUREZA_OP",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2081: (CHAVE_SAFX2081)
- IX_SAFX2081: (DAT_GRAVACAO)
- IX_SAFX2081_LOTE: (NUM_LOTE)

---

## SAFX2082

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONSELHO | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2082 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | REGIAO | VARCHAR2(3) | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2082 | VARCHAR2(4000) | Y | NVL("COD_CONSELHO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2082: (CHAVE_SAFX2082)
- IX_SAFX2082: (DAT_GRAVACAO)
- IX_SAFX2082_LOTE: (NUM_LOTE)

---

## SAFX2083

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NALADI | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2083 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2083 | VARCHAR2(4000) | Y | NVL("COD_NALADI",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2083: (CHAVE_SAFX2083)
- IX_SAFX2083: (DAT_GRAVACAO)
- IX_SAFX2083_LOTE: (NUM_LOTE)

---

## SAFX2084

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NAT_DIPI | VARCHAR2(3) | Y |  |  |
| 2 | DATA_X2084 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2084 | VARCHAR2(4000) | Y | NVL("COD_NAT_DIPI",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2084: (CHAVE_SAFX2084)
- IX_SAFX2084: (DAT_GRAVACAO)
- IX_SAFX2084_LOTE: (NUM_LOTE)

---

## SAFX2085

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TURNO | VARCHAR2(5) | Y |  |  |
| 2 | DATA_TURNO | VARCHAR2(8) | Y |  |  |
| 3 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2085 | VARCHAR2(4000) | Y | NVL("COD_TURNO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2085: (CHAVE_SAFX2085)
- IX_SAFX2085_LOTE: (NUM_LOTE)

---

## SAFX2086

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 2 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 3 | DSC_COD_AJUSTE_SPED | VARCHAR2(300) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 7 | CHAVE_SAFX2086 | VARCHAR2(4000) | Y | NVL("COD_ESTADO",'@')\|\|NVL("COD_AJUSTE_SPED",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2086: (CHAVE_SAFX2086)
- IX_SAFX2086_LOTE: (NUM_LOTE)

---

## SAFX2087
**Comment**: Cadastro de Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | DATA_X2087 | VARCHAR2(8) | Y |  |  |
| 6 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  |  |
| 7 | COD_FABRICACAO_ECF | VARCHAR2(21) | Y |  |  |
| 8 | IND_MF_ADICIONAL | CHAR(1) | Y |  |  |
| 9 | COD_TIPO_ECF | VARCHAR2(7) | Y |  |  |
| 10 | COD_MARCA_ECF | VARCHAR2(30) | Y |  |  |
| 11 | COD_MODELO_ECF | VARCHAR2(30) | Y |  |  |
| 12 | NUM_APLIC | VARCHAR2(2) | Y |  |  |
| 13 | DSC_NOME_APLIC | VARCHAR2(40) | Y |  |  |
| 14 | DSC_VERSAO_APLIC | VARCHAR2(10) | Y |  |  |
| 15 | IND_FIS_JUR_APLIC | CHAR(1) | Y |  |  |
| 16 | COD_FIS_JUR_APLIC | VARCHAR2(14) | Y |  |  |
| 17 | DSC_LINHA1_APLIC | VARCHAR2(42) | Y |  |  |
| 18 | DSC_LINHA2_APLIC | VARCHAR2(42) | Y |  |  |
| 19 | DSC_VERSAO_SB | VARCHAR2(10) | Y |  |  |
| 20 | DATA_GRAVACAO_SB | VARCHAR2(8) | Y |  |  |
| 21 | HORA_GRAVACAO_SB | VARCHAR2(6) | Y |  |  |
| 22 | NUM_USU | VARCHAR2(2) | Y |  |  |
| 23 | DATA_CADASTRO_USU | VARCHAR2(8) | Y |  |  |
| 24 | HORA_CADASTRO_USU | VARCHAR2(6) | Y |  |  |
| 25 | IND_DESCONTO_ISS | CHAR(1) | Y |  |  |
| 26 | IND_TIPO_DESCONTO | CHAR(1) | Y |  |  |
| 27 | IND_TIPO_ACRESCIMO | CHAR(1) | Y |  |  |
| 28 | IND_ORD_DESC_ACRES | CHAR(1) | Y |  |  |
| 29 | DSC_VERSAO_BIBLIOTECA | VARCHAR2(8) | Y |  |  |
| 30 | COD_GERACAO_ARQ | VARCHAR2(3) | Y |  |  |
| 31 | DSC_VERSAO_COTEPE | VARCHAR2(15) | Y |  |  |
| 32 | IND_ARREDONDA_TRUNCA | CHAR(1) | Y |  |  |
| 33 | NUM_DEC_QTDE | VARCHAR2(1) | Y |  |  |
| 34 | NUM_DEC_VLR_UNIT | VARCHAR2(1) | Y |  |  |
| 35 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 36 | NUM_CRO | VARCHAR2(6) | Y |  |  |
| 37 | VLR_GT_TOTAL | VARCHAR2(17) | Y |  |  |
| 38 | DAT_GRAVACAO | DATE | Y |  |  |
| 39 | NUM_COO_FIM_REI | VARCHAR2(9) | Y |  |  |
| 40 | NUM_APF | VARCHAR2(9) | Y |  |  |
| 41 | DAT_APF | VARCHAR2(8) | Y |  |  |
| 42 | PST_ID | NUMBER | Y |  |  |
| 43 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 44 | CHAVE_SAFX2087 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2087: (CHAVE_SAFX2087)
- IX_SAFX2087: (DAT_GRAVACAO)
- IX_SAFX2087_LOTE: (NUM_LOTE)

---

## SAFX2088

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ORG_ARRECAD | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2088 | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2088 | VARCHAR2(4000) | Y | NVL("COD_ORG_ARRECAD",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2088: (CHAVE_SAFX2088)
- IX_SAFX2088: (DAT_GRAVACAO)
- IX_SAFX2088_LOTE: (NUM_LOTE)

---

## SAFX2089

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | IND_ALCOOLICA | VARCHAR2(1) | Y |  |  |
| 6 | COD_COMP_NBM | VARCHAR2(4) | Y |  |  |
| 7 | VLR_PAUTA | VARCHAR2(19) | Y |  |  |
| 8 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX2089 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2089: (CHAVE_SAFX2089)
- IX_SAFX2089: (DAT_GRAVACAO)
- IX_SAFX2089_LOTE: (NUM_LOTE)

---

## SAFX209

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 5 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 6 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 7 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 8 | COD_DEPEND | VARCHAR2(2) | Y |  |  |
| 9 | CPF_CNPJ_PREST_SERV | VARCHAR2(14) | Y |  |  |
| 10 | DSC_PREST_SERV | VARCHAR2(150) | Y |  |  |
| 11 | VLR_REEMBOLSO | VARCHAR2(17) | Y |  |  |
| 12 | VLR_REEMBOLSO_ANT | VARCHAR2(17) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX209 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX209: (CHAVE_SAFX209)
- IX_SAFX209: (DAT_GRAVACAO)
- IX_SAFX209_LOTE: (NUM_LOTE)

---

## SAFX2090

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | IND_INSUMO | CHAR(1) | Y |  |  |
| 6 | COD_INSUMO | VARCHAR2(60) | Y |  |  |
| 7 | DT_VALID_CUSTO | VARCHAR2(8) | Y |  |  |
| 8 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 9 | CUSTO_MEDIO | VARCHAR2(18) | Y |  |  |
| 10 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX2090 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2090: (CHAVE_SAFX2090)
- IX_SAFX2090: (DAT_GRAVACAO)
- IX_SAFX2090_LOTE: (NUM_LOTE)

---

## SAFX2091

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 2 | COD_NCM | VARCHAR2(10) | Y |  |  |
| 3 | DAT_GRAVACAO | DATE | Y |  |  |
| 4 | PST_ID | NUMBER | Y |  |  |
| 5 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 6 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 7 | CHAVE_SAFX2091 | VARCHAR2(4000) | Y | NVL("COD_NBM",'@')\|\|NVL("COD_NCM",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2091: (CHAVE_SAFX2091)
- IX_SAFX2091: (DAT_GRAVACAO)
- IX_SAFX2091_LOTE: (NUM_LOTE)

---

## SAFX2092

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 2 | COD_NALADI | VARCHAR2(10) | Y |  |  |
| 3 | DAT_GRAVACAO | DATE | Y |  |  |
| 4 | PST_ID | NUMBER | Y |  |  |
| 5 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 6 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 7 | CHAVE_SAFX2092 | VARCHAR2(4000) | Y | NVL("COD_NBM",'@')\|\|NVL("COD_NALADI",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2092: (CHAVE_SAFX2092)
- IX_SAFX2092: (DAT_GRAVACAO)
- IX_SAFX2092_LOTE: (NUM_LOTE)

---

## SAFX2093

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | IND_MAT_PRIMA | CHAR(1) | Y |  |  |
| 6 | COD_MAT_PRIMA | VARCHAR2(60) | Y |  |  |
| 7 | QTD_AUTORIZ | VARCHAR2(17) | Y |  |  |
| 8 | QTD_TOTAL | VARCHAR2(17) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 11 | IND_UTILIZ_SISIF | CHAR(1) | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX2093 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2093: (CHAVE_SAFX2093)
- IX_SAFX2093: (DAT_GRAVACAO)
- IX_SAFX2093_LOTE: (NUM_LOTE)

---

## SAFX2094

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CENTRO_RESP | VARCHAR2(20) | Y |  |  |
| 2 | DATA_X2094 | VARCHAR2(8) | Y |  |  |
| 3 | DSC_CENTRO_RESP | VARCHAR2(50) | Y |  |  |
| 4 | DAT_GRAVACAO | DATE | Y |  |  |
| 5 | PST_ID | NUMBER | Y |  |  |
| 6 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2094 | VARCHAR2(4000) | Y | NVL("COD_CENTRO_RESP",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2094: (CHAVE_SAFX2094)
- IX_SAFX2094: (DAT_GRAVACAO)
- IX_SAFX2094_LOTE: (NUM_LOTE)

---

## SAFX2095

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_UNID_NEGOC | VARCHAR2(20) | Y |  |  |
| 2 | DATA_X2095 | VARCHAR2(8) | Y |  |  |
| 3 | DSC_UNID_NEGOC | VARCHAR2(50) | Y |  |  |
| 4 | NOM_RESP | VARCHAR2(50) | Y |  |  |
| 5 | COD_MATRICULA | VARCHAR2(15) | Y |  |  |
| 6 | EMAIL_INT | VARCHAR2(50) | Y |  |  |
| 7 | EMAIL_EXT | VARCHAR2(50) | Y |  |  |
| 8 | NUM_TEL | VARCHAR2(10) | Y |  |  |
| 9 | NUM_FAX | VARCHAR2(10) | Y |  |  |
| 10 | NUM_CARRIE | VARCHAR2(10) | Y |  |  |
| 11 | COD_EMPR_RESP | VARCHAR2(3) | Y |  |  |
| 12 | COD_ESTAB_RESP | VARCHAR2(6) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX2095 | VARCHAR2(4000) | Y | NVL("COD_UNID_NEGOC",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2095: (CHAVE_SAFX2095)
- IX_SAFX2095: (DAT_GRAVACAO)
- IX_SAFX2095_LOTE: (NUM_LOTE)

---

## SAFX2096

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_AREA_NEGOC | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X2096 | VARCHAR2(8) | Y |  |  |
| 3 | DSC_AREA_NEGOC | VARCHAR2(50) | Y |  |  |
| 4 | NOM_RESP | VARCHAR2(50) | Y |  |  |
| 5 | COD_MATRICULA | VARCHAR2(15) | Y |  |  |
| 6 | EMAIL_INT | VARCHAR2(50) | Y |  |  |
| 7 | EMAIL_EXT | VARCHAR2(50) | Y |  |  |
| 8 | NUM_TEL | VARCHAR2(10) | Y |  |  |
| 9 | NUM_FAX | VARCHAR2(10) | Y |  |  |
| 10 | NUM_CARRIE | VARCHAR2(10) | Y |  |  |
| 11 | COD_EMPR_RESP | VARCHAR2(3) | Y |  |  |
| 12 | COD_ESTAB_RESP | VARCHAR2(6) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX2096 | VARCHAR2(4000) | Y | NVL("COD_AREA_NEGOC",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2096: (CHAVE_SAFX2096)
- IX_SAFX2096: (DAT_GRAVACAO)
- IX_SAFX2096_LOTE: (NUM_LOTE)

---

## SAFX2097

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_ISS | VARCHAR2(7) | Y |  |  |
| 2 | DSC_MUNIC_ISS | VARCHAR2(50) | Y |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 4 | COD_MUNIC_MSAF | VARCHAR2(5) | Y |  |  |
| 5 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |
| 6 | NOM_PREFEITURA | VARCHAR2(50) | Y |  |  |
| 7 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 8 | CEP | VARCHAR2(8) | Y |  |  |
| 9 | CONTATO | VARCHAR2(50) | Y |  |  |
| 10 | DIA_VENCTO | VARCHAR2(2) | Y |  |  |
| 11 | COD_BANCO_REC | VARCHAR2(3) | Y |  |  |
| 12 | NUM_AG_REC | VARCHAR2(7) | Y |  |  |
| 13 | NUM_CONTA_REC | VARCHAR2(18) | Y |  |  |
| 14 | DSC_FORMA_REC | VARCHAR2(30) | Y |  |  |
| 15 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |
| 16 | IND_PERMIT_ABAT | CHAR(1) | Y |  |  |
| 17 | OBS_ISS1 | VARCHAR2(120) | Y |  |  |
| 18 | OBS_ISS2 | VARCHAR2(120) | Y |  |  |
| 19 | VLR_LIM_RECOLH | VARCHAR2(17) | Y |  |  |
| 20 | IND_FORMA_CALC_ISS | CHAR(1) | Y |  |  |
| 21 | IND_RESUMO_ALIQ | CHAR(1) | Y |  |  |
| 22 | IND_DEM_DEB_CRED | CHAR(1) | Y |  |  |
| 23 | IND_EQUIPARADO_CC | CHAR(1) | Y |  |  |
| 24 | IND_ISS_TERCEIROS | CHAR(1) | Y |  |  |
| 25 | IND_CRED_NF_CANC | CHAR(1) | Y |  |  |
| 26 | IND_APUR_DT_FATGER | CHAR(1) | Y |  |  |
| 27 | IND_EMIT_GUIA_REC | CHAR(1) | Y |  |  |
| 28 | IND_TP_SERV_SUBST | CHAR(1) | Y |  |  |
| 29 | LIM_CRED_PER_APUR | VARCHAR2(17) | Y |  |  |
| 30 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 31 | COD_RECEITA | VARCHAR2(5) | Y |  |  |
| 32 | DIA_VENCIMENTO | VARCHAR2(2) | Y |  |  |
| 33 | VLR_TAXA_EXPED | VARCHAR2(17) | Y |  |  |
| 34 | TITULO_GUIA_01 | VARCHAR2(60) | Y |  |  |
| 35 | TITULO_GUIA_02 | VARCHAR2(60) | Y |  |  |
| 36 | TITULO_GUIA_03 | VARCHAR2(60) | Y |  |  |
| 37 | TITULO_GUIA_04 | VARCHAR2(60) | Y |  |  |
| 38 | VLR_MORA_DIA | VARCHAR2(17) | Y |  |  |
| 39 | VLR_MORA_PERC_MES | VARCHAR2(8) | Y |  |  |
| 40 | VLR_MULTA_DIA | VARCHAR2(17) | Y |  |  |
| 41 | VLR_MULTA_PERC_MES | VARCHAR2(7) | Y |  |  |
| 42 | OBS_NF | VARCHAR2(250) | Y |  |  |
| 43 | DAT_GRAVACAO | DATE | Y |  |  |
| 44 | IND_EXIGE_COMP | CHAR(1) | Y |  |  |
| 45 | VLR_ALIQ_SERV_EQ | VARCHAR2(7) | Y |  |  |
| 46 | IND_NF_CANC | CHAR(1) | Y |  |  |
| 47 | VLR_ALIQ_ISS_TERC | VARCHAR2(7) | Y |  |  |
| 48 | TITULO_LVR | VARCHAR2(120) | Y |  |  |
| 49 | DSC_REG_ESPEC_LVR | VARCHAR2(120) | Y |  |  |
| 50 | IND_INSC_DF_LVR | CHAR(1) | Y |  |  |
| 51 | IND_FORMATO_GERAL | CHAR(1) | Y |  |  |
| 52 | COD_FORMATO_GERAL | VARCHAR2(3) | Y |  |  |
| 53 | IND_FORMATO_ESP | CHAR(1) | Y |  |  |
| 54 | COD_FORMATO_ESP | VARCHAR2(5) | Y |  |  |
| 55 | DATA_VALID_INI | VARCHAR2(8) | Y |  |  |
| 56 | DATA_VALID_FIM | VARCHAR2(8) | Y |  |  |
| 57 | IND_GER_L116 | CHAR(1) | Y | '1' | 1 - CODIGO NATUREZA DE SERVICO / 2 - CODIGO SERVICO L116/03 |
| 58 | IND_LCTO_COMPL_CR_DED | CHAR(1) | Y |  |  |
| 59 | IND_GER_ALIQ_NF | CHAR(1) | Y |  |  |
| 60 | PST_ID | NUMBER | Y |  |  |
| 61 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 62 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 63 | IND_VENC_FERIADO | VARCHAR2(1) | Y |  |  |
| 64 | CHAVE_SAFX2097 | VARCHAR2(4000) | Y | NVL("COD_MUNIC_ISS",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2097: (CHAVE_SAFX2097)
- IX_SAFX2097_LOTE: (NUM_LOTE)

---

## SAFX2098

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_ISS | VARCHAR2(7) | Y |  |  |
| 2 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 3 | DAT_VALID_ALIQ | VARCHAR2(8) | Y |  |  |
| 4 | VLR_ALIQ_SERVICO | VARCHAR2(7) | Y |  |  |
| 5 | IND_TOM_TRIBUT_ISS | CHAR(1) | Y |  |  |
| 6 | IND_SUBSTITUIDO_ISS | CHAR(1) | Y |  |  |
| 7 | COD_SERVICO_MUNIC | VARCHAR2(5) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX2098 | VARCHAR2(4000) | Y | NVL("COD_MUNIC_ISS",'@')\|\|NVL("COD_SERVICO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2098: (CHAVE_SAFX2098)
- IX_SAFX2098: (DAT_GRAVACAO)
- IX_SAFX2098_LOTE: (NUM_LOTE)

---

## SAFX2099

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 4 | SERIE_EQUIPAMENTO | VARCHAR2(20) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX2099 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2099: (CHAVE_SAFX2099)
- IX_SAFX2099: (DAT_GRAVACAO)
- IX_SAFX2099_LOTE: (NUM_LOTE)

---

## SAFX21

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 5 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 6 | IND_FOLHA | VARCHAR2(2) | Y |  |  |
| 7 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 8 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 9 | VLR_VERBA | VARCHAR2(17) | Y |  |  |
| 10 | QTD_HORAS | VARCHAR2(7) | Y |  |  |
| 11 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 14 | TP_RENDIMENTO | VARCHAR2(3) | Y |  |  |
| 15 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX21 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX21: (CHAVE_SAFX21)
- IX_SAFX21: (DAT_GRAVACAO)
- IX_SAFX21_LOTE: (NUM_LOTE)

---

## SAFX210

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 4 | SEQUENCIAL | VARCHAR2(5) | Y |  |  |
| 5 | TIPO_ECF | VARCHAR2(5) | Y |  |  |
| 6 | VLR_GT_FINAL | VARCHAR2(17) | Y |  |  |
| 7 | NUM_CRO | VARCHAR2(6) | Y |  |  |
| 8 | DATA_INTERVENCAO | VARCHAR2(8) | Y |  |  |
| 9 | IND_INTERVENCAO | CHAR(1) | Y |  |  |
| 10 | IND_PERDA | CHAR(1) | Y |  |  |
| 11 | IND_MOTIVO | CHAR(1) | Y |  |  |
| 12 | MEMORIA_ANT | VARCHAR2(16) | Y |  |  |
| 13 | MEMORIA_NOVA | VARCHAR2(16) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX210 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX210: (CHAVE_SAFX210)
- IX_SAFX210: (DAT_GRAVACAO)
- IX_SAFX210_LOTE: (NUM_LOTE)

---

## SAFX2101

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 2 | IND_CONTA | CHAR(1) | Y |  |  |
| 3 | COD_CONTA_REF | VARCHAR2(30) | Y |  |  |
| 4 | VERSAO_REF | VARCHAR2(6) | Y |  |  |
| 5 | COD_ENTIDADE_RESP | VARCHAR2(6) | Y |  |  |
| 6 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX2101 | VARCHAR2(4000) | Y | NVL("COD_CONTA",'@')\|\|NVL("IND_CONTA",'@')\|\|NVL... |  |

**Indexes**:
- IX_CHAVE_SAFX2101: (CHAVE_SAFX2101)
- IX_SAFX2101_LOTE: (NUM_LOTE)

---

## SAFX2102

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | Y |  |  |
| 4 | NUM_ORD | VARCHAR2(4) | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 6 | IND_BALANCO_DRE | CHAR(1) | Y |  |  |
| 7 | IND_NATUREZA | CHAR(1) | Y |  |  |
| 8 | IND_CLASSIF_DRE | CHAR(1) | Y |  |  |
| 9 | NIVEL | VARCHAR2(5) | Y |  |  |
| 10 | EXPRESSAO_ORD | VARCHAR2(4000) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX2102 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2102: (CHAVE_SAFX2102)
- IX_SAFX2102: (DAT_GRAVACAO)
- IX_SAFX2102_LOTE: (NUM_LOTE)
- IX_SAFX2102_ORDER: (COD_EMPRESA, COD_ESTAB, IND_BALANCO_DRE, IND_NATUREZA, NIVEL)

---

## SAFX2103

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2103 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2103: (CHAVE_SAFX2103)
- IX_SAFX2103: (DAT_GRAVACAO)
- IX_SAFX2103_LOTE: (NUM_LOTE)

---

## SAFX2104

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | Y |  |  |
| 4 | IND_UTIL_AGLUT | VARCHAR2(1) | Y |  |  |
| 5 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 6 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 7 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 8 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 9 | COD_HIST_FATO_CONTABIL | VARCHAR2(6) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX2104 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2104: (CHAVE_SAFX2104)
- IX_SAFX2104_LOTE: (NUM_LOTE)

---

## SAFX2105

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 2 | COD_IDT | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA_SUB | VARCHAR2(70) | Y |  |  |
| 4 | COD_NAT_SUBCONTAS | VARCHAR2(2) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2105 | VARCHAR2(4000) | Y | NVL("COD_CONTA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2105: (CHAVE_SAFX2105)
- IX_SAFX2105: (DAT_GRAVACAO)
- IX_SAFX2105_LOTE: (NUM_LOTE)

---

## SAFX2106
**Comment**: Tabela Mestre da Parametrizacao da Tabela Dinamica com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PAR_DYNTB | VARCHAR2(14) | Y |  |  |
| 2 | DAT_PAR_DYNTB | VARCHAR2(8) | Y |  |  |
| 3 | COD_VERSION | VARCHAR2(5) | Y |  |  |
| 4 | DSC_PAR_DYNTB | VARCHAR2(100) | Y |  |  |
| 5 | COD_RECORD | VARCHAR2(8) | Y |  |  |
| 6 | COD_ITEM | VARCHAR2(10) | Y |  |  |
| 7 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 8 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 9 | PCT_GROSS_REV_CTA | VARCHAR2(7) | Y |  |  |
| 10 | PCT_GROSS_REV_CC | VARCHAR2(7) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX2106 | VARCHAR2(4000) | Y | NVL("COD_PAR_DYNTB",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2106: (CHAVE_SAFX2106)
- IX_SAFX2106_LOTE: (NUM_LOTE)

---

## SAFX2107
**Comment**: Tabela Mestre da Parametrizacao do Plano Referencial com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PAR_REF | VARCHAR2(14) | Y |  |  |
| 2 | DAT_PAR_REF | VARCHAR2(8) | Y |  |  |
| 3 | COD_VERSION | VARCHAR2(5) | Y |  |  |
| 4 | DSC_PAR_REF | VARCHAR2(100) | Y |  |  |
| 5 | COD_RECORD | VARCHAR2(8) | Y |  |  |
| 6 | COD_CTA_REF | VARCHAR2(30) | Y |  |  |
| 7 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 8 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX2107 | VARCHAR2(4000) | Y | NVL("COD_PAR_REF",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2107: (CHAVE_SAFX2107)
- IX_SAFX2107_LOTE: (NUM_LOTE)

---

## SAFX2108

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_SERV_ESOCIAL | VARCHAR2(9) | Y |  |  |
| 4 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2108 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2108: (CHAVE_SAFX2108)
- IX_SAFX2108: (DAT_GRAVACAO)
- IX_SAFX2108_LOTE: (NUM_LOTE)

---

## SAFX2109

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_REPASSE | CHAR(1) | Y |  |  |
| 4 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2109 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2109: (CHAVE_SAFX2109)
- IX_SAFX2109: (DAT_GRAVACAO)
- IX_SAFX2109_LOTE: (NUM_LOTE)

---

## SAFX211

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 5 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 6 | IND_FOLHA | VARCHAR2(2) | Y |  |  |
| 7 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 8 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 9 | NUM_SEQ_FOLHA | VARCHAR2(3) | Y |  |  |
| 10 | IND_FIS_JUR_TOM | CHAR(1) | Y |  |  |
| 11 | COD_FIS_JUR_TOM | VARCHAR2(14) | Y |  |  |
| 12 | VLR_VERBA | VARCHAR2(17) | Y |  |  |
| 13 | QTD_HORAS | VARCHAR2(7) | Y |  |  |
| 14 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 15 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX211 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX211: (CHAVE_SAFX211)
- IX_SAFX211: (DAT_GRAVACAO)
- IX_SAFX211_LOTE: (NUM_LOTE)

---

## SAFX2110

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_REPASSE | CHAR(1) | Y |  |  |
| 4 | COD_OPERACAO | VARCHAR2(9) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2110 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2110: (CHAVE_SAFX2110)
- IX_SAFX2110: (DAT_GRAVACAO)
- IX_SAFX2110_LOTE: (NUM_LOTE)

---

## SAFX2111

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 4 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 5 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2111 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2111: (CHAVE_SAFX2111)
- IX_SAFX2111: (DAT_GRAVACAO)
- IX_SAFX2111_LOTE: (NUM_LOTE)

---

## SAFX2112

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 4 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 5 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2112 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2112: (CHAVE_SAFX2112)
- IX_SAFX2112: (DAT_GRAVACAO)
- IX_SAFX2112_LOTE: (NUM_LOTE)

---

## SAFX2113

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 4 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 5 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 6 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 7 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 8 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 9 | COD_SUSP_PRINC | VARCHAR2(14) | Y |  |  |
| 10 | VLR_ALIQ_CONT_PREV | VARCHAR2(12) | Y |  |  |
| 11 | VLR_PREV_EXIG_SUSP | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX2113 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2113: (CHAVE_SAFX2113)
- IX_SAFX2113: (DAT_GRAVACAO)
- IX_SAFX2113_LOTE: (NUM_LOTE)

---

## SAFX2114

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TAB_RUBRICA | VARCHAR2(8) | Y |  |  |
| 2 | COD_RUBRICA | VARCHAR2(30) | Y |  |  |
| 3 | VALID_INI | VARCHAR2(8) | Y |  |  |
| 4 | VALID_FIM | VARCHAR2(8) | Y |  |  |
| 5 | DESC_RUBRICA | VARCHAR2(100) | Y |  |  |
| 6 | COD_NAT_RUBRICA | VARCHAR2(4) | Y |  |  |
| 7 | TIPO_RUBRICA | CHAR(1) | Y |  |  |
| 8 | TIPO_INCID_TRIB_CP | VARCHAR2(1) | Y |  |  |
| 9 | COD_INCID_TRIB_CP | VARCHAR2(4) | Y |  |  |
| 10 | TIPO_INCID_TRIB_IRRF | VARCHAR2(1) | Y |  |  |
| 11 | COD_INCID_TRIB_IRRF | VARCHAR2(4) | Y |  |  |
| 12 | IND_TP_PROC_ADJ_CP | CHAR(1) | Y |  |  |
| 13 | NUM_PROC_ADJ_CP | VARCHAR2(21) | Y |  |  |
| 14 | COD_SUSP_CP | VARCHAR2(14) | Y |  |  |
| 15 | EXTENSAO_CP | CHAR(1) | Y |  |  |
| 16 | IND_TP_PROC_ADJ_IRRF | CHAR(1) | Y |  |  |
| 17 | NUM_PROC_ADJ_IRRF | VARCHAR2(21) | Y |  |  |
| 18 | COD_SUSP_IRRF | VARCHAR2(14) | Y |  |  |
| 19 | OBS_RUBRICA | VARCHAR2(255) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX2114 | VARCHAR2(4000) | Y | NVL("COD_TAB_RUBRICA",'@')\|\|NVL("COD_RUBRICA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2114: (CHAVE_SAFX2114)
- IX_SAFX2114: (DAT_GRAVACAO)
- IX_SAFX2114_LOTE: (NUM_LOTE)

---

## SAFX2116

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 2 | VALID_INI | VARCHAR2(8) | Y |  |  |
| 3 | VALID_FIM | VARCHAR2(8) | Y |  |  |
| 4 | COD_TRIB_DESIF | VARCHAR2(15) | Y |  |  |
| 5 | IND_RECOLH_FONTE | VARCHAR2(1) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX2116 | VARCHAR2(4000) | Y | NVL("COD_CONTA",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX2116: (CHAVE_SAFX2116)
- IX_SAFX2116_LOTE: (NUM_LOTE)

---

## SAFX2117

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NAT_REND | VARCHAR2(9) | Y |  |  |
| 2 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 3 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 5 | COD_SERVICO_NAT_REND | VARCHAR2(10) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX2117 | VARCHAR2(4000) | Y | NVL("COD_NAT_REND",'@')\|\|NVL("IND_FIS_JUR",'@')... |  |

**Indexes**:
- IX_CHAVE_SAFX2117: (CHAVE_SAFX2117)

---

## SAFX2118

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UF | VARCHAR2(2) | Y |  |  |
| 2 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 3 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 5 | COD_TABELA_DES | VARCHAR2(2) | Y |  |  |
| 6 | COD_PARAM_DES | VARCHAR2(2) | Y |  |  |
| 7 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX2118 | VARCHAR2(4000) | Y | NVL("COD_MUNICIPIO",'@')\|\|NVL("COD_TABELA_DES",... |  |

**Indexes**:
- IX_CHAVE_SAFX2118: (CHAVE_SAFX2118)
- IX_SAFX2118_LOTE: (NUM_LOTE)

---

## SAFX2119

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | TIPO_PARAM | VARCHAR2(1) | Y |  |  |
| 4 | DATA_VALID_INI | VARCHAR2(8) | Y |  |  |
| 5 | DATA_VALID_FIM | VARCHAR2(8) | Y |  |  |
| 6 | COD_CST_PIS_COFINS | VARCHAR2(2) | Y |  |  |
| 7 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | COD_NBM_INI | VARCHAR2(10) | Y |  |  |
| 10 | COD_NBM_FIM | VARCHAR2(10) | Y |  |  |
| 11 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 12 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 15 | ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 16 | ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 17 | VLR_PIS | VARCHAR2(19) | Y |  |  |
| 18 | VLR_COFINS | VARCHAR2(19) | Y |  |  |
| 19 | DESCRICAO | VARCHAR2(400) | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | CHAVE_SAFX2119 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX2119: (CHAVE_SAFX2119)
- IX_SAFX2119: (DAT_GRAVACAO)
- IX_SAFX2119_LOTE: (NUM_LOTE)

---

## SAFX212

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 5 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 6 | IND_FOLHA | VARCHAR2(2) | Y |  |  |
| 7 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 8 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 9 | COD_DEPEND | VARCHAR2(2) | Y |  |  |
| 10 | VLR_VERBA | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX212 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX212: (CHAVE_SAFX212)
- IX_SAFX212: (DAT_GRAVACAO)
- IX_SAFX212_LOTE: (NUM_LOTE)

---

## SAFX213

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | COD_CSP | VARCHAR2(2) | Y |  |  |
| 10 | NUM_DOCFIS_COF | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS_COF | VARCHAR2(3) | Y |  |  |
| 12 | NOME_PRESTADORA | VARCHAR2(10) | Y |  |  |
| 13 | VLR_TOT_DOCTO | VARCHAR2(17) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | CHAVE_SAFX213 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX213: (CHAVE_SAFX213)
- IX_SAFX213_LOTE: (NUM_LOTE)

---

## SAFX214

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_REFERENCIA | VARCHAR2(8) | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | COD_MEDIDA_FCI | VARCHAR2(6) | Y |  |  |
| 7 | VLR_SAIDA | VARCHAR2(17) | Y |  |  |
| 8 | VLR_PARC_IMP | VARCHAR2(17) | Y |  |  |
| 9 | PERC_CONT_IMP | VARCHAR2(6) | Y |  |  |
| 10 | NUM_FCI | VARCHAR2(36) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX214 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX214: (CHAVE_SAFX214)
- IX_SAFX214_LOTE: (NUM_LOTE)

---

## SAFX215

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 6 | IND_PRODUTO_ACAB | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO_ACAB | VARCHAR2(60) | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | CHAVE_SAFX215 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX215: (CHAVE_SAFX215)
- IX_SAFX215_LOTE: (NUM_LOTE)

---

## SAFX216

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 8 | NUM_DISCRIMINACAO | VARCHAR2(12) | Y |  |  |
| 9 | VAL_ITEM_DISCRIM | VARCHAR2(17) | Y |  |  |
| 10 | DSC_ITEM_APURACAO | VARCHAR2(150) | Y |  |  |
| 11 | COD_CLASSE | VARCHAR2(3) | Y |  |  |
| 12 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 13 | COD_SUB_ITEM_OCORR | VARCHAR2(2) | Y |  |  |
| 14 | NUM_CERTIFICADO | VARCHAR2(40) | Y |  |  |
| 15 | COD_REGIME_ESPECIAL | VARCHAR2(15) | Y |  |  |
| 16 | COD_ORIGEM | VARCHAR2(2) | Y |  |  |
| 17 | NUM_PROC | VARCHAR2(24) | Y |  |  |
| 18 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 19 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 20 | COD_AJUSTE | VARCHAR2(3) | Y |  |  |
| 21 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 22 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 23 | IND_TIPO_LANC | CHAR(1) | Y |  |  |
| 24 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 25 | IND_EST_DEB_CONV | CHAR(1) | Y |  |  |
| 26 | COD_ESTADO_CONV | VARCHAR2(2) | Y |  |  |
| 27 | COD_AJ_ICMS_CONV | VARCHAR2(8) | Y |  |  |
| 28 | COD_AJUSTE_SEF | VARCHAR2(3) | Y |  |  |
| 29 | COD_CHP_LIC | VARCHAR2(12) | Y |  |  |
| 30 | COD_MOT_EST | VARCHAR2(2) | Y |  |  |
| 31 | NUM_AUTO_INFRACAO | VARCHAR2(13) | Y |  |  |
| 32 | DAT_GRAVACAO | DATE | Y |  |  |
| 33 | COD_AJUSTE_IPI | VARCHAR2(3) | Y |  |  |
| 34 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 35 | PST_ID | NUMBER | Y |  |  |
| 36 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 37 | CHAVE_SAFX216 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX216: (CHAVE_SAFX216)
- IX_SAFX216_LOTE: (NUM_LOTE)

---

## SAFX217

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 8 | NUM_DISCRIMINACAO | VARCHAR2(12) | Y |  |  |
| 9 | SEQ_PROC_ARRECAD | VARCHAR2(12) | Y |  |  |
| 10 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 11 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 12 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 13 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 14 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 15 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX217 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX217: (CHAVE_SAFX217)
- IX_SAFX217_LOTE: (NUM_LOTE)

---

## SAFX218

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 8 | NUM_DISCRIMINACAO | VARCHAR2(12) | Y |  |  |
| 9 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 10 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 11 | NORM_DEV | CHAR(1) | Y |  |  |
| 12 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 16 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 17 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 18 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 19 | VLR_AJUSTE | VARCHAR2(17) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | NUM_SEQUENCIAL | VARCHAR2(5) | Y |  |  |
| 22 | PST_ID | NUMBER | Y |  |  |
| 23 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 24 | CHAVE_SAFX218 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX218: (CHAVE_SAFX218)
- IX_SAFX218_LOTE: (NUM_LOTE)

---

## SAFX219

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 8 | NUM_DISCRIMINACAO | VARCHAR2(12) | Y |  |  |
| 9 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 10 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 11 | NORM_DEV | CHAR(1) | Y |  |  |
| 12 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 16 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 17 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 18 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 19 | IND_ICOMPL_LANCTO | CHAR(1) | Y |  |  |
| 20 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 21 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX219 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX219: (CHAVE_SAFX219)
- IX_SAFX219_LOTE: (NUM_LOTE)

---

## SAFX22

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | DAT_OCOR | VARCHAR2(8) | Y |  |  |
| 5 | NUM_OCOR | CHAR(1) | Y |  |  |
| 6 | IND_TIPO | CHAR(1) | Y |  |  |
| 7 | CPF | VARCHAR2(11) | Y |  |  |
| 8 | NOME | VARCHAR2(50) | Y |  |  |
| 9 | VLR_PENSAO | VARCHAR2(17) | Y |  |  |
| 10 | NUM_PROC_JUD | VARCHAR2(15) | Y |  |  |
| 11 | DAT_DECISAO | VARCHAR2(8) | Y |  |  |
| 12 | TRIB_JUST | VARCHAR2(5) | Y |  |  |
| 13 | VARA_JUDICIAL | VARCHAR2(2) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | VLR_PENSAO_13 | VARCHAR2(17) | Y |  | Valor da pensão sobre o 13 salário |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | DSC_OUTROS | VARCHAR2(100) | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX22 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX22: (CHAVE_SAFX22)
- IX_SAFX22: (DAT_GRAVACAO)
- IX_SAFX22_LOTE: (NUM_LOTE)

---

## SAFX220

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 8 | NUM_DISCRIMINACAO | VARCHAR2(12) | Y |  |  |
| 9 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 12 | VLR_ESTORNO | VARCHAR2(17) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX220 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX220: (CHAVE_SAFX220)
- IX_SAFX220_LOTE: (NUM_LOTE)

---

## SAFX221

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REFER | VARCHAR2(6) | Y |  |  |
| 4 | VLR_REC_AUFER | VARCHAR2(17) | Y |  |  |
| 5 | QTDE_PROF_HAB | VARCHAR2(6) | Y |  |  |
| 6 | VLR_ISS_RECOLHER | VARCHAR2(17) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX221 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX221: (CHAVE_SAFX221)
- IX_SAFX221_LOTE: (NUM_LOTE)

---

## SAFX222

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REFER | VARCHAR2(6) | Y |  |  |
| 4 | NUM_CPF | VARCHAR2(11) | Y |  |  |
| 5 | IND_HABILITACAO | CHAR(1) | Y |  |  |
| 6 | IND_ESCOLARIDADE | CHAR(1) | Y |  |  |
| 7 | IND_PARTIC_SOCIET | CHAR(1) | Y |  |  |
| 8 | DSC_NOME_PROF | VARCHAR2(60) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX222 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX222: (CHAVE_SAFX222)
- IX_SAFX222_LOTE: (NUM_LOTE)

---

## SAFX223

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | NUM_GUIA_RECOL | VARCHAR2(30) | Y |  |  |
| 7 | VAL_GUIA_RECOL | VARCHAR2(17) | Y |  |  |
| 8 | DAT_VENCTO | VARCHAR2(8) | Y |  |  |
| 9 | MES_ANO_REF | VARCHAR2(6) | Y |  |  |
| 10 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 11 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 12 | DSC_COMPLEMENTAR | VARCHAR2(250) | Y |  |  |
| 13 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 14 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 15 | DSC_PROC | VARCHAR2(250) | Y |  |  |
| 16 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 17 | COD_DEB_ICMS | VARCHAR2(3) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX223 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX223: (CHAVE_SAFX223)
- IX_SAFX223_LOTE: (NUM_LOTE)

---

## SAFX224

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 5 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | NUM_GUIA_RECOL | VARCHAR2(30) | Y |  |  |
| 8 | VAL_GUIA_RECOL | VARCHAR2(17) | Y |  |  |
| 9 | DAT_VENCTO | VARCHAR2(8) | Y |  |  |
| 10 | MES_ANO_REF | VARCHAR2(6) | Y |  |  |
| 11 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 12 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 13 | DSC_COMPLEMENTAR | VARCHAR2(250) | Y |  |  |
| 14 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 15 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 16 | DSC_PROC | VARCHAR2(250) | Y |  |  |
| 17 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 18 | COD_DEB_ICMS | VARCHAR2(3) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX224 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX224: (CHAVE_SAFX224)
- IX_SAFX224_LOTE: (NUM_LOTE)

---

## SAFX225

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 7 | VLR_LANCTO | VARCHAR2(17) | Y |  |  |
| 8 | CONTRA_PART | VARCHAR2(70) | Y |  |  |
| 9 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 10 | HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 11 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 12 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 13 | TIPO_LANCTO | CHAR(1) | Y |  |  |
| 14 | IND_PFJ_VINC | CHAR(1) | Y |  |  |
| 15 | COD_PFJ_VINC | VARCHAR2(14) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | DAT_LANCTO_EXTEMP | VARCHAR2(8) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX225 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX225: (CHAVE_SAFX225)
- IX_SAFX225_LOTE: (NUM_LOTE)

---

## SAFX226

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 5 | VLR_SALDO_INI | VARCHAR2(17) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | VARCHAR2(17) | Y |  |  |
| 8 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 9 | VLR_TOT_CRE | VARCHAR2(17) | Y |  |  |
| 10 | VLR_TOT_DEB | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX226 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX226: (CHAVE_SAFX226)
- IX_SAFX226_LOTE: (NUM_LOTE)

---

## SAFX227

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_SALDO | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 6 | VLR_SALDO_INI | VARCHAR2(17) | Y |  |  |
| 7 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 8 | VLR_SALDO_FIM | VARCHAR2(17) | Y |  |  |
| 9 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 10 | VLR_TOT_CRE | VARCHAR2(17) | Y |  |  |
| 11 | VLR_TOT_DEB | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX227 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX227: (CHAVE_SAFX227)
- IX_SAFX227_LOTE: (NUM_LOTE)

---

## SAFX228

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 7 | VLR_LANCTO | VARCHAR2(17) | Y |  |  |
| 8 | CONTRA_PART | VARCHAR2(70) | Y |  |  |
| 9 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 10 | HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 11 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 12 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 13 | TIPO_LANCTO | CHAR(1) | Y |  |  |
| 14 | IND_PFJ_VINC | CHAR(1) | Y |  |  |
| 15 | COD_PFJ_VINC | VARCHAR2(14) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | DAT_LANCTO_EXTEMP | VARCHAR2(8) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX228 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX228: (CHAVE_SAFX228)
- IX_SAFX228_LOTE: (NUM_LOTE)

---

## SAFX229

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 5 | VLR_SALDO_INI | VARCHAR2(17) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | VARCHAR2(17) | Y |  |  |
| 8 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 9 | VLR_TOT_CRE | VARCHAR2(17) | Y |  |  |
| 10 | VLR_TOT_DEB | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX229 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX229: (CHAVE_SAFX229)
- IX_SAFX229_LOTE: (NUM_LOTE)

---

## SAFX23

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 3 | DAT_PRODUTO | VARCHAR2(8) | Y |  |  |
| 4 | COD_EAN | VARCHAR2(14) | Y |  |  |
| 5 | DAT_COD_EAN | VARCHAR2(8) | Y |  |  |
| 6 | TIPO_COD_EAN | VARCHAR2(5) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX23 | VARCHAR2(4000) | Y | NVL("IND_PRODUTO",'@')\|\|NVL("COD_PRODUTO",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX23: (CHAVE_SAFX23)
- IX_SAFX23_LOTE: (NUM_LOTE)

---

## SAFX230

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 5 | COD_CONTA_ANT | VARCHAR2(70) | Y |  |  |
| 6 | CENTRO_CUSTO_ANT | VARCHAR2(50) | Y |  |  |
| 7 | VLR_SALDO_INI | VARCHAR2(17) | Y |  |  |
| 8 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX230 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX230: (CHAVE_SAFX230)
- IX_SAFX230_LOTE: (NUM_LOTE)

---

## SAFX231

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 5 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 6 | COD_CONTA_ANT | VARCHAR2(70) | Y |  |  |
| 7 | CENTRO_CUSTO_ANT | VARCHAR2(50) | Y |  |  |
| 8 | VLR_SALDO_INI | VARCHAR2(17) | Y |  |  |
| 9 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX231 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX231: (CHAVE_SAFX231)
- IX_SAFX231_LOTE: (NUM_LOTE)

---

## SAFX232

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 5 | DATA_SALDO | VARCHAR2(8) | Y |  |  |
| 6 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | VARCHAR2(17) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX232 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX232: (CHAVE_SAFX232)
- IX_SAFX232_LOTE: (NUM_LOTE)

---

## SAFX233

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 5 | COD_INC | VARCHAR2(6) | Y |  |  |
| 6 | DATA_ATIV_BEM | VARCHAR2(8) | Y |  |  |
| 7 | IND_TIPO_MOV | VARCHAR2(2) | Y |  |  |
| 8 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 9 | VLR_ICMSS | VARCHAR2(17) | Y |  |  |
| 10 | VLR_ICMS_FRETE | VARCHAR2(17) | Y |  |  |
| 11 | VLR_ICMS_DIFAL | VARCHAR2(17) | Y |  |  |
| 12 | NUM_PARCELA | VARCHAR2(3) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | DATA_BAIXA | VARCHAR2(8) | Y |  |  |
| 15 | IND_TIPO_BAIXA | VARCHAR2(2) | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX233 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX233: (CHAVE_SAFX233)
- IX_SAFX233_LOTE: (NUM_LOTE)

---

## SAFX234

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 5 | COD_INC | VARCHAR2(6) | Y |  |  |
| 6 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 11 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 12 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 13 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 14 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | IND_E_S | CHAR(1) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 20 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 21 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 22 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 23 | VLR_ICMS_ST | VARCHAR2(17) | Y |  |  |
| 24 | VLR_ICMS_FRETE | VARCHAR2(17) | Y |  |  |
| 25 | VLR_ICMS_DIFAL | VARCHAR2(17) | Y |  |  |
| 26 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 27 | CHAVE_SAFX234 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX234: (CHAVE_SAFX234)
- IX_SAFX234_LOTE: (NUM_LOTE)

---

## SAFX235

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | Y |  |  |
| 4 | IND_TP_CORRECAO | VARCHAR2(2) | Y |  |  |
| 5 | IND_PRODUTO_OP | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO_OP | VARCHAR2(60) | Y |  |  |
| 7 | DAT_INI_APUR | VARCHAR2(8) | Y |  |  |
| 8 | DAT_FIM_APUR | VARCHAR2(8) | Y |  |  |
| 9 | COD_OP | VARCHAR2(30) | Y |  |  |
| 10 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 11 | DAT_ESTQ_FIM | VARCHAR2(8) | Y |  |  |
| 12 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 16 | QTD_CORRECAO | VARCHAR2(17) | Y |  |  |
| 17 | IND_POS_NEG | CHAR(1) | Y |  |  |
| 18 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX235 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX235: (CHAVE_SAFX235)
- IX_SAFX235_LOTE: (NUM_LOTE)

---

## SAFX236

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | Y |  |  |
| 4 | IND_TP_CORRECAO | VARCHAR2(2) | Y |  |  |
| 5 | IND_PRODUTO_OP | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO_OP | VARCHAR2(60) | Y |  |  |
| 7 | DAT_INI_APUR | VARCHAR2(8) | Y |  |  |
| 8 | DAT_FIM_APUR | VARCHAR2(8) | Y |  |  |
| 9 | COD_OP | VARCHAR2(30) | Y |  |  |
| 10 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 11 | DAT_ESTQ_FIM | VARCHAR2(8) | Y |  |  |
| 12 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | IND_PRODUTO_INS | CHAR(1) | Y |  |  |
| 16 | COD_PRODUTO_INS | VARCHAR2(60) | Y |  |  |
| 17 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 18 | QTD_CORRECAO | VARCHAR2(17) | Y |  |  |
| 19 | IND_POS_NEG | CHAR(1) | Y |  |  |
| 20 | IND_PRODUTO_SUBST | CHAR(1) | Y |  |  |
| 21 | COD_PRODUTO_SUBST | VARCHAR2(60) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX236 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX236: (CHAVE_SAFX236)
- IX_SAFX236_LOTE: (NUM_LOTE)

---

## SAFX237

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_VALID | VARCHAR2(8) | Y |  |  |
| 6 | TIPO_DO_ITEM | VARCHAR2(2) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX237 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX237: (CHAVE_SAFX237)
- IX_SAFX237_LOTE: (NUM_LOTE)

---

## SAFX238

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_NBM | VARCHAR2(4) | Y |  |  |
| 4 | DATA_VALID | VARCHAR2(8) | Y |  |  |
| 5 | TIPO_DO_ITEM | VARCHAR2(2) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX238 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX238: (CHAVE_SAFX238)
- IX_SAFX238_LOTE: (NUM_LOTE)

---

## SAFX239

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 4 | DATA_VALID | VARCHAR2(8) | Y |  |  |
| 5 | TIPO_DO_ITEM | VARCHAR2(2) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX239 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX239: (CHAVE_SAFX239)
- IX_SAFX239_LOTE: (NUM_LOTE)

---

## SAFX24

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 3 | DAT_PRODUTO | VARCHAR2(8) | Y |  |  |
| 4 | COD_UND_PAD_ORIG | VARCHAR2(8) | Y |  |  |
| 5 | COD_UND_PAD_DEST | VARCHAR2(8) | Y |  |  |
| 6 | VLR_FATOR_CONV | VARCHAR2(17) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX24 | VARCHAR2(4000) | Y | NVL("IND_PRODUTO",'@')\|\|NVL("COD_PRODUTO",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX24: (CHAVE_SAFX24)
- IX_SAFX24_LOTE: (NUM_LOTE)

---

## SAFX240

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI_CONS | VARCHAR2(8) | Y |  |  |
| 4 | DATA_FIM_CONS | VARCHAR2(8) | Y |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | Y |  |  |
| 6 | NOME_EMP_PART | VARCHAR2(100) | Y |  |  |
| 7 | CNPJ | VARCHAR2(14) | Y |  |  |
| 8 | IND_EVENTO | CHAR(1) | Y |  |  |
| 9 | PERC_PART_TOT | VARCHAR2(8) | Y |  |  |
| 10 | PERC_CONS | VARCHAR2(8) | Y |  |  |
| 11 | DATA_INI_EMP | VARCHAR2(8) | Y |  |  |
| 12 | DATA_FIM_EMP | VARCHAR2(8) | Y |  |  |
| 13 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX240 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX240: (CHAVE_SAFX240)
- IX_SAFX240_LOTE: (NUM_LOTE)

---

## SAFX241

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI_CONS | VARCHAR2(8) | Y |  |  |
| 4 | DATA_FIM_CONS | VARCHAR2(8) | Y |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | Y |  |  |
| 6 | IND_EVENTO_OPER | CHAR(1) | Y |  |  |
| 7 | COD_EMP_OPER | VARCHAR2(4) | Y |  |  |
| 8 | DATA_EVENTO | VARCHAR2(8) | Y |  |  |
| 9 | IND_COND_PART | CHAR(1) | Y |  |  |
| 10 | PERC_PART_EMP | VARCHAR2(8) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX241 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX241: (CHAVE_SAFX241)
- IX_SAFX241_LOTE: (NUM_LOTE)

---

## SAFX242

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_SALDO_CONS | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | VLR_AGLUTINADO | VARCHAR2(17) | Y |  |  |
| 6 | IND_AGLUTINADO | CHAR(1) | Y |  |  |
| 7 | VLR_ELIMINACAO | VARCHAR2(17) | Y |  |  |
| 8 | IND_ELIMINACAO | CHAR(1) | Y |  |  |
| 9 | VLR_CONSOLIDADO | VARCHAR2(17) | Y |  |  |
| 10 | IND_CONSOLIDADO | CHAR(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX242 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX242: (CHAVE_SAFX242)
- IX_SAFX242_LOTE: (NUM_LOTE)

---

## SAFX243

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_SALDO_CONS | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | Y |  |  |
| 6 | VLR_ELIMINADO_TOT | VARCHAR2(17) | Y |  |  |
| 7 | IND_ELIMINADO_TOT | CHAR(1) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX243 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX243: (CHAVE_SAFX243)
- IX_SAFX243_LOTE: (NUM_LOTE)

---

## SAFX244

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_SALDO_CONS | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | Y |  |  |
| 6 | COD_EMP_CONTRAP | VARCHAR2(4) | Y |  |  |
| 7 | COD_CONTA_CONTRAP | VARCHAR2(70) | Y |  |  |
| 8 | VLR_CONTRAPARTIDA | VARCHAR2(17) | Y |  |  |
| 9 | IND_CONTRAPARTIDA | CHAR(1) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX244 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX244: (CHAVE_SAFX244)
- IX_SAFX244_LOTE: (NUM_LOTE)

---

## SAFX245

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 4 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 5 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 6 | SEQUENCIAL | VARCHAR2(4) | Y |  |  |
| 7 | COD_INF_ADIC | VARCHAR2(8) | Y |  |  |
| 8 | VLR_INF_ADIC | VARCHAR2(17) | Y |  |  |
| 9 | DSC_COMPL | VARCHAR2(200) | Y |  |  |
| 10 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX245 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX245: (CHAVE_SAFX245)
- IX_SAFX245_LOTE: (NUM_LOTE)

---

## SAFX246

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_OPERACAO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | IND_TP_SERVICO | VARCHAR2(4) | Y |  |  |
| 7 | COD_OPERACAO | VARCHAR2(60) | Y |  |  |
| 8 | DSC_PRODUTO | VARCHAR2(150) | Y |  |  |
| 9 | VLR_TOT_OP | VARCHAR2(17) | Y |  |  |
| 10 | IND_TP_PAGTO | VARCHAR2(2) | Y |  |  |
| 11 | COD_UF | VARCHAR2(2) | Y |  |  |
| 12 | DAT_INI_CONTRATO | VARCHAR2(8) | Y |  |  |
| 13 | DAT_FIM_CONTRATO | VARCHAR2(8) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_COMISSAO | VARCHAR2(1) | Y |  |  |
| 17 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 18 | QUANTIDADE | VARCHAR2(15) | Y |  |  |
| 19 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 20 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX246 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX246: (CHAVE_SAFX246)
- IX_SAFX246_LOTE: (NUM_LOTE)

---

## SAFX247

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_COMP | VARCHAR2(4) | Y |  |  |
| 4 | MES_COMP | VARCHAR2(2) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | ID_DEM_PAG | VARCHAR2(30) | Y |  |  |
| 8 | IND_DESCONTO | CHAR(1) | Y |  |  |
| 9 | IND_PAG_TOTAL | CHAR(1) | Y |  |  |
| 10 | DAT_PAG | VARCHAR2(8) | Y |  |  |
| 11 | TIPO_PAG | VARCHAR2(2) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | COD_CBO | VARCHAR2(10) | Y |  |  |
| 14 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX247 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX247: (CHAVE_SAFX247)
- IX_SAFX247: (DAT_GRAVACAO)
- IX_SAFX247_LOTE: (NUM_LOTE)

---

## SAFX248

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_COMP | VARCHAR2(4) | Y |  |  |
| 4 | MES_COMP | VARCHAR2(2) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | ID_DEM_PAG | VARCHAR2(30) | Y |  |  |
| 8 | COD_TAB_RUBRICA | VARCHAR2(8) | Y |  |  |
| 9 | COD_RUBRICA | VARCHAR2(30) | Y |  |  |
| 10 | QTDE_REF | VARCHAR2(6) | Y |  |  |
| 11 | FATOR_CALC | VARCHAR2(5) | Y |  |  |
| 12 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 13 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 14 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 15 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 16 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX248 | VARCHAR2(98) | Y | "COD_EMPRESA"\|\|"COD_ESTAB"\|\|"ANO_COMP"\|\|"MES_CO... |  |

**Indexes**:
- IX_SAFX248: (DAT_GRAVACAO)
- IX_SAFX248_LOTE: (NUM_LOTE)

---

## SAFX249

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_COMP | VARCHAR2(4) | Y |  |  |
| 4 | MES_COMP | VARCHAR2(2) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | ID_DEM_PAG | VARCHAR2(30) | Y |  |  |
| 8 | DAT_PAG | VARCHAR2(8) | Y |  |  |
| 9 | COD_TAB_RUBRICA | VARCHAR2(8) | Y |  |  |
| 10 | COD_RUBRICA | VARCHAR2(30) | Y |  |  |
| 11 | TIPO_PAG | VARCHAR2(2) | Y |  |  |
| 12 | QTDE_REF | VARCHAR2(6) | Y |  |  |
| 13 | FATOR_CALC | VARCHAR2(5) | Y |  |  |
| 14 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 15 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX249 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX249: (CHAVE_SAFX249)
- IX_SAFX249: (DAT_GRAVACAO)
- IX_SAFX249_LOTE: (NUM_LOTE)

---

## SAFX25

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CONTRATO | VARCHAR2(14) | Y |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 3 | IND_ABATIMENTO | CHAR(1) | Y |  |  |
| 4 | COD_MUNIC_ISS | VARCHAR2(7) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX25 | VARCHAR2(4000) | Y | NVL("COD_CONTRATO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX25: (CHAVE_SAFX25)
- IX_SAFX25: (DAT_GRAVACAO)
- IX_SAFX25_LOTE: (NUM_LOTE)

---

## SAFX250

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_COMP | VARCHAR2(4) | Y |  |  |
| 4 | MES_COMP | VARCHAR2(2) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | ID_DEM_PAG | VARCHAR2(30) | Y |  |  |
| 8 | CPF_CNPJ_EMPREGADOR | VARCHAR2(14) | Y |  |  |
| 9 | COD_CATEG_TRAB | VARCHAR2(3) | Y |  |  |
| 10 | VLR_REMUNERACAO | VARCHAR2(17) | Y |  |  |
| 11 | VLR_RET | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX250 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX250: (CHAVE_SAFX250)
- IX_SAFX250: (DAT_GRAVACAO)
- IX_SAFX250_LOTE: (NUM_LOTE)

---

## SAFX251

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_REF | VARCHAR2(4) | Y |  |  |
| 4 | MES_REF | VARCHAR2(2) | Y |  |  |
| 5 | COD_SINDICATO | VARCHAR2(5) | Y |  |  |
| 6 | TP_CONTRIB | CHAR(1) | Y |  |  |
| 7 | VLR_CONTRIB | VARCHAR2(17) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX251 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX251: (CHAVE_SAFX251)
- IX_SAFX251_LOTE: (NUM_LOTE)

---

## SAFX252

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 4 | COD_ATIV_CONT_PREV | VARCHAR2(8) | Y |  |  |
| 5 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 6 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 7 | IND_AJ_REINF | VARCHAR2(1) | Y |  |  |
| 8 | COD_AJ_REINF | VARCHAR2(2) | Y |  |  |
| 9 | VL_AJ_REINF | VARCHAR2(17) | Y |  |  |
| 10 | DSC_AJ_REINF | VARCHAR2(20) | Y |  |  |
| 11 | DT_REF_REINF | VARCHAR2(6) | Y |  |  |
| 12 | VLR_ALIQ_CONT_PREV | VARCHAR2(12) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX252 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX252: (CHAVE_SAFX252)
- IX_SAFX252: (DAT_GRAVACAO)
- IX_SAFX252_LOTE: (NUM_LOTE)

---

## SAFX253

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_TERMINAL_TEL | VARCHAR2(15) | Y |  |  |
| 10 | VLR_TOT_FATURA | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | UF_TERMINAL_TEL | VARCHAR2(2) | Y |  |  |
| 15 | CHAVE_SAFX253 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX253: (CHAVE_SAFX253)
- IX_SAFX253_LOTE: (NUM_LOTE)

---

## SAFX254

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | NUM_TERMINAL_TEL | VARCHAR2(15) | Y |  |  |
| 13 | VLR_TOT_FATURA | VARCHAR2(17) | Y |  |  |
| 14 | UF_TERMINAL_TEL | VARCHAR2(2) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX254 | VARCHAR2(4000) | Y | NVL("DATA_FISCAL",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX254: (CHAVE_SAFX254)
- IX_SAFX254: (DAT_GRAVACAO)
- IX_SAFX254_LOTE: (NUM_LOTE)

---

## SAFX257

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_BALANCO_DRE | VARCHAR2(1) | Y |  |  |
| 4 | COD_CONTA_AGLUT | VARCHAR2(70) | Y |  |  |
| 5 | DATA_DEMONSTRACAO | VARCHAR2(8) | Y |  |  |
| 6 | NOTA_EXPLICATIVA | VARCHAR2(255) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | NUM_REFERENCIA | VARCHAR2(12) | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX257 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX257: (CHAVE_SAFX257)
- IX_SAFX257_LOTE: (NUM_LOTE)

---

## SAFX259

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_FAT_COM | VARCHAR2(20) | Y |  |  |
| 4 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | VLR_TOT_FAT | VARCHAR2(17) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 10 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 11 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 12 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 13 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 14 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 15 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 16 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX259 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX259: (CHAVE_SAFX259)
- IX_SAFX259_LOTE: (NUM_LOTE)

---

## SAFX26

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_SALDO | VARCHAR2(8) | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | QTD_SALDO | VARCHAR2(13) | Y |  |  |
| 7 | VLR_TOT | VARCHAR2(13) | Y |  |  |
| 8 | VLR_UNIT | VARCHAR2(15) | Y |  |  |
| 9 | ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | VLR_TOT_ICMS | VARCHAR2(13) | Y |  |  |
| 12 | VLR_UNIT_BC_ICMS | VARCHAR2(15) | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX26 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX26: (CHAVE_SAFX26)
- IX_SAFX26: (DAT_GRAVACAO)
- IX_SAFX26_LOTE: (NUM_LOTE)

---

## SAFX260

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_FAT_COM | VARCHAR2(20) | Y |  |  |
| 4 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | NUM_ITEM | VARCHAR2(7) | Y |  |  |
| 8 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 10 | IND_ORIGEM_ITEM | CHAR(1) | Y |  |  |
| 11 | IND_FIS_JUR_TERC | CHAR(1) | Y |  |  |
| 12 | COD_FIS_JUR_TERC | VARCHAR2(14) | Y |  |  |
| 13 | DATA_EMISSAO_NF | VARCHAR2(8) | Y |  |  |
| 14 | COD_MODELO_NF | VARCHAR2(2) | Y |  |  |
| 15 | SERIE_NF | VARCHAR2(3) | Y |  |  |
| 16 | NUMERO_NF | VARCHAR2(12) | Y |  |  |
| 17 | VLR_TOT_NF | VARCHAR2(17) | Y |  |  |
| 18 | VLR_ITEM | VARCHAR2(17) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 21 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 22 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 23 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 26 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 27 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 28 | PST_ID | NUMBER | Y |  |  |
| 29 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 30 | CHAVE_SAFX260 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX260: (CHAVE_SAFX260)
- IX_SAFX260_LOTE: (NUM_LOTE)

---

## SAFX261

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_TERMINAL | VARCHAR2(15) | Y |  |  |
| 4 | IND_FIS_JUR_USU | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR_USU | VARCHAR2(14) | Y |  |  |
| 6 | DATA_RECARGA | VARCHAR2(8) | Y |  |  |
| 7 | IND_FIS_JUR_VEND | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR_VEND | VARCHAR2(14) | Y |  |  |
| 9 | IND_FIS_JUR_RESP | CHAR(1) | Y |  |  |
| 10 | COD_FIS_JUR_RESP | VARCHAR2(14) | Y |  |  |
| 11 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | VLR_TOT_RECARGA | VARCHAR2(17) | Y |  |  |
| 14 | VLR_DEDUCAO | VARCHAR2(17) | Y |  |  |
| 15 | VLR_ANTEC_CRED | VARCHAR2(17) | Y |  |  |
| 16 | VLR_MULTA | VARCHAR2(17) | Y |  |  |
| 17 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 18 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 19 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX261 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX261: (CHAVE_SAFX261)
- IX_SAFX261_LOTE: (NUM_LOTE)

---

## SAFX262

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI_CONS | VARCHAR2(8) | Y |  |  |
| 4 | DATA_FIM_CONS | VARCHAR2(8) | Y |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | Y |  |  |
| 6 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | COD_CONTA_CONS | VARCHAR2(70) | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX262 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX262: (CHAVE_SAFX262)
- IX_SAFX262_LOTE: (NUM_LOTE)

---

## SAFX263

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 13 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 14 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 15 | VLR_PREV_EXIG_SUSP | VARCHAR2(17) | Y |  |  |
| 16 | VLR_GIBRAT_EXIG_SUSP | VARCHAR2(17) | Y |  |  |
| 17 | VLR_SENAR_EXIG_SUSP | VARCHAR2(17) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | IND_EVENTO | CHAR(1) | Y | '5' |  |
| 20 | IND_PRINC_ADIC | CHAR(1) | Y | ' ' |  |
| 21 | VLR_N_RET | VARCHAR2(17) | Y |  |  |
| 22 | IND_TP_PROC_JUD | VARCHAR2(1) | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX263 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX263: (CHAVE_SAFX263)
- IX_SAFX263_LOTE: (NUM_LOTE)

---

## SAFX264

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MES_ANO_APUR | VARCHAR2(6) | Y |  |  |
| 4 | DATA_REFER | VARCHAR2(8) | Y |  |  |
| 5 | IND_NATUREZA | VARCHAR2(2) | Y |  |  |
| 6 | IND_APROP_AJUSTE | VARCHAR2(2) | Y |  |  |
| 7 | CNPJ | VARCHAR2(14) | Y |  |  |
| 8 | VLR_TOT_AJUSTE | VARCHAR2(17) | Y |  |  |
| 9 | VLR_AJ_CST01 | VARCHAR2(17) | Y |  |  |
| 10 | VLR_AJ_CST02 | VARCHAR2(17) | Y |  |  |
| 11 | VLR_AJ_CST03 | VARCHAR2(17) | Y |  |  |
| 12 | VLR_AJ_CST04 | VARCHAR2(17) | Y |  |  |
| 13 | VLR_AJ_CST05 | VARCHAR2(17) | Y |  |  |
| 14 | VLR_AJ_CST06 | VARCHAR2(17) | Y |  |  |
| 15 | VLR_AJ_CST07 | VARCHAR2(17) | Y |  |  |
| 16 | VLR_AJ_CST08 | VARCHAR2(17) | Y |  |  |
| 17 | VLR_AJ_CST09 | VARCHAR2(17) | Y |  |  |
| 18 | VLR_AJ_CST49 | VARCHAR2(17) | Y |  |  |
| 19 | VLR_AJ_CST99 | VARCHAR2(17) | Y |  |  |
| 20 | NUM_RECIBO | VARCHAR2(80) | Y |  |  |
| 21 | DSC_INF_COMPL | VARCHAR2(100) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX264 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX264: (CHAVE_SAFX264)
- IX_SAFX264_LOTE: (NUM_LOTE)

---

## SAFX265

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_SALDO | VARCHAR2(8) | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | QTD_SALDO | VARCHAR2(17) | Y |  |  |
| 7 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 8 | VLR_UNIT | VARCHAR2(19) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX265 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX265: (CHAVE_SAFX265)
- IX_SAFX265_LOTE: (NUM_LOTE)

---

## SAFX266

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REFER | VARCHAR2(6) | Y |  |  |
| 4 | IND_PROD_CONJ | CHAR(1) | Y |  |  |
| 5 | DATA_PROD | VARCHAR2(8) | Y |  |  |
| 6 | COD_OP | VARCHAR2(30) | Y |  |  |
| 7 | DATA_INI_OP | VARCHAR2(8) | Y |  |  |
| 8 | DATA_FIM_OP | VARCHAR2(8) | Y |  |  |
| 9 | IND_INDUST_TERC | CHAR(1) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX266 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX266: (CHAVE_SAFX266)
- IX_SAFX266_LOTE: (NUM_LOTE)

---

## SAFX267

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REFER | VARCHAR2(6) | Y |  |  |
| 4 | IND_PROD_CONJ | CHAR(1) | Y |  |  |
| 5 | DATA_PROD | VARCHAR2(8) | Y |  |  |
| 6 | COD_OP | VARCHAR2(30) | Y |  |  |
| 7 | DATA_INI_OP | VARCHAR2(8) | Y |  |  |
| 8 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 10 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX267 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX267: (CHAVE_SAFX267)
- IX_SAFX267_LOTE: (NUM_LOTE)

---

## SAFX268

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REFER | VARCHAR2(6) | Y |  |  |
| 4 | IND_PROD_CONJ | CHAR(1) | Y |  |  |
| 5 | DATA_PROD | VARCHAR2(8) | Y |  |  |
| 6 | COD_OP | VARCHAR2(30) | Y |  |  |
| 7 | DATA_INI_OP | VARCHAR2(8) | Y |  |  |
| 8 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 10 | QTDE_CONS | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX268 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX268: (CHAVE_SAFX268)
- IX_SAFX268_LOTE: (NUM_LOTE)

---

## SAFX269

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_APUR | VARCHAR2(6) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | COD_COSIF | VARCHAR2(30) | Y |  |  |
| 6 | COD_SERV_LEI_116 | VARCHAR2(4) | Y |  |  |
| 7 | VLR_ALIQ_ISS | VARCHAR2(7) | Y |  |  |
| 8 | QTD_OCOR | VARCHAR2(5) | Y |  |  |
| 9 | VLR_CONTABIL | VARCHAR2(17) | Y |  |  |
| 10 | VLR_BASE_ISS | VARCHAR2(17) | Y |  |  |
| 11 | VLR_ISS | VARCHAR2(17) | Y |  |  |
| 12 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX269 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX269: (CHAVE_SAFX269)
- IX_SAFX269_LOTE: (NUM_LOTE)

---

## SAFX27

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 10 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 11 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 12 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 13 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COD_COMPL_OP | VARCHAR2(2) | Y |  |  |
| 16 | VLR_BASE_RET | VARCHAR2(17) | Y |  |  |
| 17 | QTD_E_S | VARCHAR2(13) | Y |  |  |
| 18 | VLR_UNIT_SAIDA | VARCHAR2(18) | Y |  |  |
| 19 | VLR_SAI_USU_FINAL | VARCHAR2(17) | Y |  |  |
| 20 | VLR_NAO_RALIZ | VARCHAR2(17) | Y |  |  |
| 21 | VLR_ISENTAS | VARCHAR2(17) | Y |  |  |
| 22 | VLR_SAI_OUT_UF | VARCHAR2(17) | Y |  |  |
| 23 | VLR_SAI_COM_S | VARCHAR2(17) | Y |  |  |
| 24 | VLR_BASE_S_VC | VARCHAR2(17) | Y |  |  |
| 25 | VLR_BASE_E_VC | VARCHAR2(17) | Y |  |  |
| 26 | QTD_SALDOS | VARCHAR2(13) | Y |  |  |
| 27 | VLR_UNIT_SALDO | VARCHAR2(18) | Y |  |  |
| 28 | VLR_TOT_SALDO | VARCHAR2(17) | Y |  |  |
| 29 | ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 30 | VLR_ICMS_RET | VARCHAR2(17) | Y |  |  |
| 31 | DAT_GRAVACAO | DATE | Y |  |  |
| 32 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 33 | IND_PRODUTO_PAI | CHAR(1) | Y |  |  |
| 34 | COD_PRODUTO_PAI | VARCHAR2(60) | Y |  |  |
| 35 | CHASSI | VARCHAR2(17) | Y |  |  |
| 36 | MODELO_LIVRO | VARCHAR2(1) | Y |  |  |
| 37 | VLR_BASE_OP_PROP | VARCHAR2(17) | Y |  |  |
| 38 | VLR_BASE_EST_REM | VARCHAR2(17) | Y |  |  |
| 39 | COD_PARAM_GER | VARCHAR2(3) | Y |  |  |
| 40 | IND_NF_COMPL | CHAR(1) | Y |  |  |
| 41 | VLR_COMPL | VARCHAR2(17) | Y |  |  |
| 42 | IND_CALC_SALD | CHAR(1) | Y |  |  |
| 43 | VLR_BASE_IC_VC | VARCHAR2(17) | Y |  |  |
| 44 | VLR_TOT_SD_IC | VARCHAR2(17) | Y |  |  |
| 45 | VLR_UNIT_SD_IC | VARCHAR2(18) | Y |  |  |
| 46 | PST_ID | NUMBER | Y |  |  |
| 47 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 48 | CHAVE_SAFX27 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX27: (CHAVE_SAFX27)
- IX_SAFX27: (DAT_GRAVACAO)
- IX_SAFX27_LOTE: (NUM_LOTE)

---

## SAFX270

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_APUR | VARCHAR2(6) | Y |  |  |
| 4 | IND_TIPO_DED | VARCHAR2(1) | Y |  |  |
| 5 | IND_OBRIG | VARCHAR2(1) | Y |  |  |
| 6 | VLR_DEDUCAO | VARCHAR2(17) | Y |  |  |
| 7 | NUM_PROC | VARCHAR2(24) | Y |  |  |
| 8 | ORIGEM_PROC | VARCHAR2(1) | Y |  |  |
| 9 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 10 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX270 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX270: (CHAVE_SAFX270)
- IX_SAFX270_LOTE: (NUM_LOTE)

---

## SAFX271

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | TIP_DOCTO | VARCHAR2(5) | Y |  |  |
| 5 | TIP_MOV_ES | VARCHAR2(1) | Y |  |  |
| 6 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | NUM_PROC | VARCHAR2(21) | Y |  |  |
| 14 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 15 | VLR_CONT_PREV_N_RET | VARCHAR2(17) | Y |  |  |
| 16 | VLR_GILRAT_N_RET | VARCHAR2(17) | Y |  |  |
| 17 | VLR_SENAR_N_RET | VARCHAR2(17) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | IND_TP_PROC_JUD | VARCHAR2(1) | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX271 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX271: (CHAVE_SAFX271)
- IX_SAFX271: (DAT_GRAVACAO)
- IX_SAFX271_LOTE: (NUM_LOTE)

---

## SAFX272

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 6 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 7 | COD_INF_ADIC | VARCHAR2(8) | Y |  |  |
| 8 | DSC_COMPL | VARCHAR2(200) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX272 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX272: (CHAVE_SAFX272)
- IX_SAFX272_LOTE: (NUM_LOTE)

---

## SAFX273

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 4 | INSCRICAO_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 5 | NUM_JUNTA_COMER | VARCHAR2(14) | Y |  |  |
| 6 | DAT_DESPACHO | VARCHAR2(8) | Y |  |  |
| 7 | NIRE | VARCHAR2(15) | Y |  |  |
| 8 | IND_SITUACAO | VARCHAR2(1) | Y |  |  |
| 9 | INSC_EST_ESPECIAL | VARCHAR2(14) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX273 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX273: (CHAVE_SAFX273)
- IX_SAFX273_LOTE: (NUM_LOTE)

---

## SAFX274

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APUR_INI | VARCHAR2(8) | Y |  |  |
| 4 | DAT_APUR_FIM | VARCHAR2(8) | Y |  |  |
| 5 | COD_PIS_COFINS | VARCHAR2(10) | Y |  |  |
| 6 | COD_CRED | VARCHAR2(3) | Y |  |  |
| 7 | IND_CRED_ORI | VARCHAR2(1) | Y |  |  |
| 8 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 9 | CNPJ_SUC | VARCHAR2(14) | Y |  |  |
| 10 | VLR_CRED_APUR | VARCHAR2(17) | Y |  |  |
| 11 | VLR_CRED_APUR_EXTEMP | VARCHAR2(17) | Y |  |  |
| 12 | VLR_CRED_UTIL_DESC | VARCHAR2(17) | Y |  |  |
| 13 | VLR_CRED_UTIL_PER | VARCHAR2(17) | Y |  |  |
| 14 | VLR_CRED_UTIL_DCOMP | VARCHAR2(17) | Y |  |  |
| 15 | VLR_CRED_UTIL_TRANS | VARCHAR2(17) | Y |  |  |
| 16 | VLR_CRED_UTIL_OUT | VARCHAR2(17) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX274 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX274: (CHAVE_SAFX274)
- IX_SAFX274: (DAT_GRAVACAO)
- IX_SAFX274_LOTE: (NUM_LOTE)

---

## SAFX275

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 2 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 3 | DATA_X04 | VARCHAR2(8) | Y |  |  |
| 4 | DAT_VIG_INI | VARCHAR2(8) | Y |  |  |
| 5 | DAT_VIG_FIM | VARCHAR2(8) | Y |  |  |
| 6 | CPF_DEP | VARCHAR2(11) | Y |  |  |
| 7 | NOME_DEP | VARCHAR2(60) | Y |  |  |
| 8 | DAT_NASC_DEP | VARCHAR2(8) | Y |  |  |
| 9 | IND_REL_DEP | VARCHAR2(2) | Y |  |  |
| 10 | DSC_DEP | VARCHAR2(60) | Y |  |  |
| 11 | IND_PENSAO | VARCHAR2(1) | Y |  |  |
| 12 | IND_PLANO | VARCHAR2(1) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX275 | VARCHAR2(4000) | Y | NVL("IND_FIS_JUR",'@')\|\|NVL("COD_FIS_JUR",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX275: (CHAVE_SAFX275)
- IX_SAFX275: (DAT_GRAVACAO)
- IX_SAFX275_LOTE: (NUM_LOTE)

---

## SAFX276

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 2 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 3 | DATA_X04 | VARCHAR2(8) | Y |  |  |
| 4 | NUM_CNPJ | VARCHAR2(14) | Y |  |  |
| 5 | IND_MOVTO | VARCHAR2(1) | Y |  |  |
| 6 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 7 | TP_INSC | VARCHAR2(1) | Y |  |  |
| 8 | NR_INSC | VARCHAR2(14) | Y |  |  |
| 9 | VLR_DED_REND_TRIB | VARCHAR2(17) | Y |  |  |
| 10 | VLR_REEMB_PER | VARCHAR2(17) | Y |  |  |
| 11 | VLR_REEMB_PER_ANT | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX276 | VARCHAR2(4000) | Y | NVL("IND_FIS_JUR",'@')\|\|NVL("COD_FIS_JUR",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX276: (CHAVE_SAFX276)
- IX_SAFX276: (DAT_GRAVACAO)
- IX_SAFX276_LOTE: (NUM_LOTE)

---

## SAFX277

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 2 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 3 | DATA_X04 | VARCHAR2(8) | Y |  |  |
| 4 | DAT_VIG_INI | VARCHAR2(8) | Y |  |  |
| 5 | CPF_DEP | VARCHAR2(11) | Y |  |  |
| 6 | NUM_CNPJ | VARCHAR2(14) | Y |  |  |
| 7 | IND_MOVTO | VARCHAR2(1) | Y |  |  |
| 8 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 9 | TP_INSC | VARCHAR2(1) | Y |  |  |
| 10 | NR_INSC | VARCHAR2(14) | Y |  |  |
| 11 | VLR_DED_REND_TRIB | VARCHAR2(17) | Y |  |  |
| 12 | VLR_REEMB_PER | VARCHAR2(17) | Y |  |  |
| 13 | VLR_REEMB_PER_ANT | VARCHAR2(17) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX277 | VARCHAR2(4000) | Y | NVL("IND_FIS_JUR",'@')\|\|NVL("COD_FIS_JUR",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX277: (CHAVE_SAFX277)
- IX_SAFX277: (DAT_GRAVACAO)
- IX_SAFX277_LOTE: (NUM_LOTE)

---

## SAFX278

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 6 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 7 | IND_PRODUTO_ASS | VARCHAR2(1) | Y |  |  |
| 8 | COD_PRODUTO_ASS | VARCHAR2(60) | Y |  |  |
| 9 | QTD_CONTIDA | VARCHAR2(17) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX278 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX278: (CHAVE_SAFX278)

---

## SAFX279

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  | Código da Empresa |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  | Código do Estabelecimento |
| 3 | DAT_MOV | VARCHAR2(8) | Y |  | Data do fato gerador ou pagamento/crédito |
| 4 | COD_NAT_REND | VARCHAR2(5) | Y |  | Natureza dos rendimentos pagos a beneficiários não identificados, conforme opções a seguir: 1 - Rendimentos do trabalho ou 9 - Demais rendimentos. |
| 5 | VLR_LIQ | VARCHAR2(17) | Y |  | Valor líquido do pagamento. |
| 6 | VLR_REAJ | VARCHAR2(17) | Y |  | Valor reajustado, considerado como valor bruto da base de cálculo do IRRF. |
| 7 | VLR_IR | VARCHAR2(17) | Y |  | Valor do Imposto de Renda Retido na Fonte |
| 8 | DESCR | VARCHAR2(200) | Y |  | Descrição do pagamento. |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | DATA_ESCR_CONT | VARCHAR2(8) | Y |  |  |
| 13 | CHAVE_SAFX279 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX279: (CHAVE_SAFX279)
- IX_SAFX279_LOTE: (NUM_LOTE)

---

## SAFX28

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 5 | NUM_CUPOM_INI | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_CUPOM_INI | VARCHAR2(3) | Y |  |  |
| 7 | SUBSERIE_CUPOM_INI | VARCHAR2(2) | Y |  |  |
| 8 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 9 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |
| 10 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 11 | VLR_GT_INICIAL | VARCHAR2(17) | Y |  |  |
| 12 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 13 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 14 | VLR_ICMS_ST | VARCHAR2(17) | Y |  |  |
| 15 | VLR_B_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 16 | VLR_B_ISENTA_ICMS | VARCHAR2(17) | Y |  |  |
| 17 | VLR_B_OUTRAS_ICMS | VARCHAR2(17) | Y |  |  |
| 18 | VLR_B_RED_ICMS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_B_ICMS_ST | VARCHAR2(17) | Y |  |  |
| 20 | VLR_CANCELADO | VARCHAR2(17) | Y |  |  |
| 21 | NUM_CUPOM_FIM | VARCHAR2(12) | Y |  |  |
| 22 | SERIE_CUPOM_FIM | VARCHAR2(3) | Y |  |  |
| 23 | SUBSERIE_CUPOM_FIM | VARCHAR2(2) | Y |  |  |
| 24 | VLR_GT_FINAL | VARCHAR2(17) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |
| 26 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 27 | NUM_CRO | VARCHAR2(3) | Y |  |  |
| 28 | NUM_MP_RESUMO | VARCHAR2(12) | Y |  |  |
| 29 | NUM_LANCTO_CONTABIL | VARCHAR2(12) | Y |  | número do lançamento contábil - ato cotepe 70/05 |
| 30 | COD_OBSERVACAO | VARCHAR2(8) | Y |  | código da observação da x2009_observacao - ato cotepe 70/05 |
| 31 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 32 | PST_ID | NUMBER | Y |  |  |
| 33 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 34 | CHAVE_SAFX28 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX28: (CHAVE_SAFX28)
- IX_SAFX28: (DAT_GRAVACAO)
- IX_SAFX28_LOTE: (NUM_LOTE)

---

## SAFX280

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | SEQUENCIAL | VARCHAR2(5) | Y |  |  |
| 5 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 7 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 8 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 9 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 10 | VLR_ALIQUOTA_PRODUTO | VARCHAR2(7) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 13 | VLR_PRODUTO_LIQ | VARCHAR2(17) | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX280 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX280: (CHAVE_SAFX280)
- IX_SAFX280_LOTE: (NUM_LOTE)

---

## SAFX281

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 5 | NUM_CUPOM | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_CUPOM | VARCHAR2(3) | Y |  |  |
| 7 | SUBSERIE_CUPOM | VARCHAR2(2) | Y |  |  |
| 8 | NUM_ITEM_CUPOM | VARCHAR2(5) | Y |  |  |
| 9 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 10 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 11 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 12 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 13 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 14 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 15 | VLR_ALIQUOTA_PRODUTO | VARCHAR2(7) | Y |  |  |
| 16 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 19 | VLR_LIQUIDO_PROD | VARCHAR2(17) | Y |  |  |
| 20 | IND_CANCELAMENTO | CHAR(1) | Y |  |  |
| 21 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 22 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 23 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 24 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  |  |
| 25 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 26 | COD_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 27 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 28 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 29 | VLR_BASE_ISS | VARCHAR2(17) | Y |  |  |
| 30 | VLR_ALIQUOTA_ISS | VARCHAR2(7) | Y |  |  |
| 31 | VLR_ISS | VARCHAR2(17) | Y |  |  |
| 32 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 33 | IND_FIS_JUR | CHAR(1) | Y |  | Campo identificador da pessoa física jurídica do Cupom |
| 34 | COD_FIS_JUR | VARCHAR2(14) | Y |  | Campo codigo da pessoa física jurídica do Cupom |
| 35 | CPF_CNPJ_ADQUIRENTE | VARCHAR2(14) | Y |  |  |
| 36 | PST_ID | NUMBER | Y |  |  |
| 37 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 38 | CHAVE_SAFX281 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX281: (CHAVE_SAFX281)
- IX_SAFX281_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX281_LOTE: (NUM_LOTE)

---

## SAFX282

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_MOV | VARCHAR2(8) | Y |  |  |
| 4 | COD_NAT_REND | VARCHAR2(5) | Y |  |  |
| 5 | IND_TP_PROC_ADJ | VARCHAR2(1) | Y |  |  |
| 6 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 7 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 8 | VLR_BASE_EXIG_SUSP_IR | VARCHAR2(17) | Y |  |  |
| 9 | VLR_RET_NEFE_IR | VARCHAR2(17) | Y |  |  |
| 10 | VLR_DEP_JUD_IR | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX282 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX282: (CHAVE_SAFX282)
- IX_SAFX282_LOTE: (NUM_LOTE)

---

## SAFX283

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_RECEBIMENTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_NAT_REND | VARCHAR2(5) | Y |  |  |
| 7 | OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 8 | VLR_BRUTO | VARCHAR2(17) | Y |  |  |
| 9 | VLR_BASE_IR | VARCHAR2(17) | Y |  |  |
| 10 | VLR_IR | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX283 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX283: (CHAVE_SAFX283)
- IX_SAFX283_LOTE: (NUM_LOTE)

---

## SAFX284

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_RECEBIMENTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_NAT_REND | VARCHAR2(5) | Y |  |  |
| 7 | IND_TP_PROC_ADJ | VARCHAR2(1) | Y |  |  |
| 8 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 9 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 10 | VLR_BASE_EXIG_SUSP_IR | VARCHAR2(17) | Y |  |  |
| 11 | VLR_RET_NEFE_IR | VARCHAR2(17) | Y |  |  |
| 12 | VLR_DEP_JUD_IR | VARCHAR2(17) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX284 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX284: (CHAVE_SAFX284)
- IX_SAFX284_LOTE: (NUM_LOTE)

---

## SAFX285

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_EQUIP | VARCHAR2(9) | Y |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | Y |  |  |
| 5 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 6 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 7 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX285 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX285: (CHAVE_SAFX285)

---

## SAFX286

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_EQUIP | VARCHAR2(9) | Y |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | Y |  |  |
| 5 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 6 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 7 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 8 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 9 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 10 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 11 | ALIQUOTA_ICMS | VARCHAR2(7) | Y |  |  |
| 12 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 13 | VLR_OUTROS | VARCHAR2(17) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX286 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX286: (CHAVE_SAFX286)

---

## SAFX29

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 5 | SEQUENCIAL | VARCHAR2(5) | Y |  |  |
| 6 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 7 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 8 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 9 | VLR_ALIQ_OPER | VARCHAR2(7) | Y |  |  |
| 10 | VLR_OPER | VARCHAR2(17) | Y |  |  |
| 11 | COD_TRIB_OPER | CHAR(1) | Y |  |  |
| 12 | VLR_BASE_OPER | VARCHAR2(17) | Y |  |  |
| 13 | VLR_BASE_RED_OPER | VARCHAR2(17) | Y |  |  |
| 14 | VLR_CONTAB_OPER | VARCHAR2(17) | Y |  |  |
| 15 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 16 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 17 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX29 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX29: (CHAVE_SAFX29)
- IX_SAFX29: (DAT_GRAVACAO)
- IX_SAFX29_LOTE: (NUM_LOTE)

---

## SAFX291

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 5 | SEQUENCIAL | VARCHAR2(5) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 9 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 10 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 11 | VLR_ALIQUOTA_PRODUTO | VARCHAR2(7) | Y |  |  |
| 12 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | VLR_PRODUTO_LIQ | VARCHAR2(17) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX291 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX291: (CHAVE_SAFX291)
- IX_SAFX291_LOTE: (NUM_LOTE)

---

## SAFX292

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 5 | SEQUENCIAL | VARCHAR2(5) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 9 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 10 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 11 | VLR_ALIQUOTA_PRODUTO | VARCHAR2(7) | Y |  |  |
| 12 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 15 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | VLR_PRODUTO_LIQ | VARCHAR2(17) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX292 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX292: (CHAVE_SAFX292)
- IX_SAFX292_LOTE: (NUM_LOTE)

---

## SAFX293

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 10 | IND_ICOMPL_LANCTO | CHAR(1) | Y |  |  |
| 11 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | DSC_INFO_FISCO | VARCHAR2(2000) | Y |  |  |
| 16 | DSC_INFO_CONTRIB | VARCHAR2(3000) | Y |  |  |
| 17 | CHAVE_SAFX293 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX293: (CHAVE_SAFX293)
- IX_SAFX293: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL)
- IX_SAFX293_1: (DAT_GRAVACAO)
- IX_SAFX293_LOTE: (NUM_LOTE)

---

## SAFX294

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | COD_OBS_LANCTO_FISCAL | VARCHAR2(8) | Y |  |  |
| 10 | IND_ICOMPL_LANCTO | CHAR(1) | Y |  |  |
| 11 | COD_AJUSTE_SPED | VARCHAR2(10) | Y |  |  |
| 12 | DSC_COMP_AJUSTE | VARCHAR2(255) | Y |  |  |
| 13 | NUM_ITEM | VARCHAR2(7) | Y |  |  |
| 14 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 15 | ALIQUOTA_ICMS | VARCHAR2(7) | Y |  |  |
| 16 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 17 | VLR_OUTROS | VARCHAR2(17) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX294 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX294: (CHAVE_SAFX294)
- IX_SAFX294: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL)
- IX_SAFX294_1: (DAT_GRAVACAO)
- IX_SAFX294_LOTE: (NUM_LOTE)

---

## SAFX295

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_GERACAO | VARCHAR2(8) | Y |  |  |
| 4 | NUM_PROC_REF | VARCHAR2(20) | Y |  |  |
| 5 | NUM_SEQUENCIAL | VARCHAR2(6) | Y |  |  |
| 6 | REG_REFERENCIA | VARCHAR2(4) | Y |  |  |
| 7 | NUM_CHAVE_NFE | VARCHAR2(90) | Y |  |  |
| 8 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 10 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 11 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 12 | DATA_OPER | VARCHAR2(8) | Y |  |  |
| 13 | VLR_OPER_ITEM | VARCHAR2(17) | Y |  |  |
| 14 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 15 | VLR_BC_PIS | VARCHAR2(19) | Y |  |  |
| 16 | ALIQ_PIS | VARCHAR2(12) | Y |  |  |
| 17 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 18 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 19 | VLR_BC_COFINS | VARCHAR2(19) | Y |  |  |
| 20 | ALIQ_COFINS | VARCHAR2(12) | Y |  |  |
| 21 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 22 | COD_SIT_PIS_SUSP | VARCHAR2(2) | Y |  |  |
| 23 | VLR_BC_PIS_SUSP | VARCHAR2(19) | Y |  |  |
| 24 | ALIQ_PIS_SUSP | VARCHAR2(12) | Y |  |  |
| 25 | VLR_PIS_SUSP | VARCHAR2(17) | Y |  |  |
| 26 | COD_SIT_COFINS_SUSP | VARCHAR2(2) | Y |  |  |
| 27 | VLR_BC_COFINS_SUSP | VARCHAR2(19) | Y |  |  |
| 28 | ALIQ_COFINS_SUSP | VARCHAR2(12) | Y |  |  |
| 29 | VLR_COFINS_SUSP | VARCHAR2(17) | Y |  |  |
| 30 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 31 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 32 | DSC_DOCUMENTO | VARCHAR2(255) | Y |  |  |
| 33 | DAT_GRAVACAO | DATE | Y |  |  |
| 34 | PST_ID | NUMBER | Y |  |  |
| 35 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 36 | CHAVE_SAFX295 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX295: (CHAVE_SAFX295)
- IX_SAFX295_LOTE: (NUM_LOTE)

---

## SAFX296

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | QTD_CONV | VARCHAR2(17) | Y |  |  |
| 17 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 18 | VLR_UNIT_CONV | VARCHAR2(19) | Y |  |  |
| 19 | VLR_ICMS_CONV | VARCHAR2(19) | Y |  |  |
| 20 | IND_RESP_RET_ENT | VARCHAR2(1) | Y |  |  |
| 21 | VLR_UNIT_BC_ICMSS_ENT | VARCHAR2(19) | Y |  |  |
| 22 | VLR_UNIT_ICMSS_CONV_ENT | VARCHAR2(19) | Y |  |  |
| 23 | VLR_UNIT_FCP_CONV_ENT | VARCHAR2(19) | Y |  |  |
| 24 | COD_MOTIVO_SAI | VARCHAR2(5) | Y |  |  |
| 25 | VLR_UNIT_ICMS_OPER_SAI | VARCHAR2(19) | Y |  |  |
| 26 | VLR_UNIT_ICMS_ESTQ_SAI | VARCHAR2(19) | Y |  |  |
| 27 | VLR_UNIT_ICMSS_ESTQ_SAI | VARCHAR2(19) | Y |  |  |
| 28 | VLR_UNIT_FCP_ESTQ_SAI | VARCHAR2(19) | Y |  |  |
| 29 | VLR_UNIT_ICMSS_REST_SAI | VARCHAR2(19) | Y |  |  |
| 30 | VLR_UNIT_FCP_REST_SAI | VARCHAR2(19) | Y |  |  |
| 31 | VLR_UNIT_ICMSS_COMPL_SAI | VARCHAR2(19) | Y |  |  |
| 32 | VLR_UNIT_FCP_COMPL_SAI | VARCHAR2(19) | Y |  |  |
| 33 | DAT_GRAVACAO | DATE | Y |  |  |
| 34 | PST_ID | NUMBER | Y |  |  |
| 35 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 36 | CHAVE_SAFX296 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX296: (CHAVE_SAFX296)
- IX_SAFX296_LOTE: (NUM_LOTE)

---

## SAFX297

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 6 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 7 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 10 | QTD_CONV | VARCHAR2(17) | Y |  |  |
| 11 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 12 | VLR_UNIT_CONV | VARCHAR2(19) | Y |  |  |
| 13 | VLR_UNIT_ICMS_OPER_CONV | VARCHAR2(19) | Y |  |  |
| 14 | VLR_UNIT_ICMS_CONV | VARCHAR2(19) | Y |  |  |
| 15 | VLR_UNIT_ICMS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 16 | VLR_UNIT_ICMSS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 17 | VLR_UNIT_FCPS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 18 | VLR_UNIT_ICMSS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 19 | VLR_UNIT_FCPS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 20 | VLR_UNIT_ICMSS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 21 | VLR_UNIT_FCPS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX297 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX297: (CHAVE_SAFX297)
- IX_SAFX297: (DAT_GRAVACAO)
- IX_SAFX297_LOTE: (NUM_LOTE)

---

## SAFX298

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_EQUIP | VARCHAR2(9) | Y |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | Y |  |  |
| 5 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 6 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 7 | COD_MOTIVO_SAI | VARCHAR2(5) | Y |  |  |
| 8 | QTD_CONV | VARCHAR2(17) | Y |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | VLR_UNIT_CONV | VARCHAR2(19) | Y |  |  |
| 11 | VLR_UNIT_ICMS_OPER_CONV | VARCHAR2(19) | Y |  |  |
| 12 | VLR_UNIT_ICMS_CONV | VARCHAR2(19) | Y |  |  |
| 13 | VLR_UNIT_ICMS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 14 | VLR_UNIT_ICMSS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 15 | VLR_UNIT_FCPS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 16 | VLR_UNIT_ICMSS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 17 | VLR_UNIT_FCPS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 18 | VLR_UNIT_ICMSS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 19 | VLR_UNIT_FCPS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX298 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX298: (CHAVE_SAFX298)
- IX_SAFX298: (DAT_GRAVACAO)
- IX_SAFX298_LOTE: (NUM_LOTE)

---

## SAFX299

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 5 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 6 | NUM_DOCFIS_INI | VARCHAR2(12) | Y |  |  |
| 7 | NUM_DOCFIS_FIN | VARCHAR2(12) | Y |  |  |
| 8 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 9 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 10 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 11 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 15 | QTD_CONV | VARCHAR2(17) | Y |  |  |
| 16 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 17 | VLR_UNIT_CONV | VARCHAR2(19) | Y |  |  |
| 18 | VLR_UNIT_ICMS_OPER_CONV | VARCHAR2(19) | Y |  |  |
| 19 | VLR_UNIT_ICMS_CONV | VARCHAR2(19) | Y |  |  |
| 20 | VLR_UNIT_ICMS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 21 | VLR_UNIT_ICMSS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 22 | VLR_UNIT_FCPS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 23 | VLR_UNIT_ICMSS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 24 | VLR_UNIT_FCPS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 25 | VLR_UNIT_ICMSS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 26 | VLR_UNIT_FCPS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 27 | DAT_GRAVACAO | DATE | Y |  |  |
| 28 | PST_ID | NUMBER | Y |  |  |
| 29 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 30 | CHAVE_SAFX299 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX299: (CHAVE_SAFX299)
- IX_SAFX299: (DAT_GRAVACAO)
- IX_SAFX299_LOTE: (NUM_LOTE)

---

## SAFX30

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 5 | IND_EVENTO | CHAR(1) | Y |  |  |
| 6 | COD_EVENTO | VARCHAR2(2) | Y |  |  |
| 7 | VLR_ALIQ_12 | VARCHAR2(17) | Y |  |  |
| 8 | VLR_ALIQ_18 | VARCHAR2(17) | Y |  |  |
| 9 | VLR_ALIQ_25 | VARCHAR2(17) | Y |  |  |
| 10 | VLR_ALIQ_OUT | VARCHAR2(17) | Y |  |  |
| 11 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX30 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX30: (CHAVE_SAFX30)
- IX_SAFX30: (DAT_GRAVACAO)
- IX_SAFX30_LOTE: (NUM_LOTE)

---

## SAFX300

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 12 | NUM_DOCFIS_NF | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS_NF | VARCHAR2(3) | Y |  |  |
| 14 | SUB_SERIE_DOCFIS_NF | VARCHAR2(2) | Y |  |  |
| 15 | DATA_FISCAL_NF | VARCHAR2(8) | Y |  |  |
| 16 | MOVTO_E_S_NF | CHAR(1) | Y |  |  |
| 17 | NORM_DEV_NF | CHAR(1) | Y |  |  |
| 18 | COD_DOCTO_NF | VARCHAR2(5) | Y |  |  |
| 19 | IND_FIS_JUR_NF | CHAR(1) | Y |  |  |
| 20 | COD_FIS_JUR_NF | VARCHAR2(14) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | PST_ID | NUMBER | Y |  |  |
| 23 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 24 | CHAVE_SAFX300 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX300: (CHAVE_SAFX300)
- IX_SAFX300: (DAT_GRAVACAO)
- IX_SAFX300_LOTE: (NUM_LOTE)

---

## SAFX3007

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_MUN_FT_GER_IBS_CBS | VARCHAR2(7) | Y |  |  |
| 13 | TIPO_CHAVE_DFE | VARCHAR2(1) | Y |  |  |
| 14 | DESC_CHAVE_DFE | VARCHAR2(255) | Y |  |  |
| 15 | FINALIDADE_EMISSAO_NFE | VARCHAR2(1) | Y |  |  |
| 16 | FINALIDADE_EMISSAO_NFSE | VARCHAR2(1) | Y |  |  |
| 17 | TIPO_NF_DEBITO | VARCHAR2(2) | Y |  |  |
| 18 | TIPO_NF_CREDITO | VARCHAR2(2) | Y |  |  |
| 19 | IND_OPER_FINAL | VARCHAR2(1) | Y |  |  |
| 20 | IND_OPER_USO_CONS_PESSOAL | VARCHAR2(1) | Y |  |  |
| 21 | IND_OPER_FORNECIMENTO | VARCHAR2(10) | Y |  |  |
| 22 | IND_DESTINATARIO_SERVICO | VARCHAR2(1) | Y |  |  |
| 23 | IND_COMPRA_MOMENTO_OPER | VARCHAR2(1) | Y |  |  |
| 24 | IND_INTERM | VARCHAR2(1) | Y |  |  |
| 25 | IND_COMPRA_GOVERN | VARCHAR2(1) | Y |  |  |
| 26 | TIPO_OPERACAO | VARCHAR2(1) | Y |  |  |
| 27 | TIPO_ENTE_GOVERN | VARCHAR2(1) | Y |  |  |
| 28 | PERC_RED_ALIQ_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 29 | CST_IS | VARCHAR2(3) | Y |  |  |
| 30 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 31 | BC_IS | VARCHAR2(17) | Y |  |  |
| 32 | ALIQ_IS | VARCHAR2(7) | Y |  |  |
| 33 | ALIQ_ESP_UNID_MED_APR_IS | VARCHAR2(7) | Y |  |  |
| 34 | VLR_IS | VARCHAR2(17) | Y |  |  |
| 35 | UNID_MED_TRIBUT_IS | VARCHAR2(8) | Y |  |  |
| 36 | QTD_TRIB_IS | VARCHAR2(15) | Y |  |  |
| 37 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 38 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 39 | BC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 40 | VLR_MON_DOCREF_N_INC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 41 | ALIQ_IBS_UF | VARCHAR2(7) | Y |  |  |
| 42 | VLR_IBS_UF | VARCHAR2(17) | Y |  |  |
| 43 | PERC_DIF_IBS_UF | VARCHAR2(7) | Y |  |  |
| 44 | VLR_DIF_IBS_UF | VARCHAR2(17) | Y |  |  |
| 45 | VLR_TRIB_DEV_IBS_UF | VARCHAR2(17) | Y |  |  |
| 46 | PERC_RED_ALIQ_IBS_UF | VARCHAR2(7) | Y |  |  |
| 47 | ALIQ_EFET_IBS_UF | VARCHAR2(7) | Y |  |  |
| 48 | ALIQ_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 49 | VLR_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 50 | PERC_DIF_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 51 | VLR_DIF_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 52 | VLR_BRUTO_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 53 | VLR_TRIB_DEV_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 54 | PERC_RED_ALIQ_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 55 | ALIQ_EFET_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 56 | ALIQ_CBS | VARCHAR2(7) | Y |  |  |
| 57 | VLR_CBS | VARCHAR2(17) | Y |  |  |
| 58 | PERC_DIF_CBS | VARCHAR2(7) | Y |  |  |
| 59 | VLR_DIF_CBS | VARCHAR2(17) | Y |  |  |
| 60 | VLR_BRUTO_CBS | VARCHAR2(17) | Y |  |  |
| 61 | VLR_TRIB_DEV_CBS | VARCHAR2(17) | Y |  |  |
| 62 | PERC_RED_ALIQ_CBS | VARCHAR2(7) | Y |  |  |
| 63 | ALIQ_EFET_CBS | VARCHAR2(7) | Y |  |  |
| 64 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 65 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 66 | ALIQ_IBS_TRIB_REG_UF | VARCHAR2(7) | Y |  |  |
| 67 | VLR_TRIB_REG_TRIB_IBS_UF | VARCHAR2(17) | Y |  |  |
| 68 | ALIQ_TRIB_REG_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 69 | VLR_TRIB_REG_TRIB_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 70 | ALIQ_TRIB_REG_CBS | VARCHAR2(7) | Y |  |  |
| 71 | VLR_TRIB_REG_TRIB_CBS | VARCHAR2(17) | Y |  |  |
| 72 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 73 | PERC_CRED_PRES_IBS | VARCHAR2(7) | Y |  |  |
| 74 | ALIQ_CRED_PRES_IBS | VARCHAR2(7) | Y |  |  |
| 75 | VLR_CRED_PRES_IBS | VARCHAR2(17) | Y |  |  |
| 76 | VLR_CRED_PRES_C_SUS_IBS | VARCHAR2(17) | Y |  |  |
| 77 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 78 | PERC_CRED_PRES_CBS | VARCHAR2(7) | Y |  |  |
| 79 | ALIQ_CRED_PRES_CBS | VARCHAR2(7) | Y |  |  |
| 80 | VLR_CRED_PRES_CBS | VARCHAR2(17) | Y |  |  |
| 81 | VLR_CRED_PRES_C_SUS_CBS | VARCHAR2(17) | Y |  |  |
| 82 | QTD_TRIB_MONO_IBS_CBS | VARCHAR2(15) | Y |  |  |
| 83 | ALIQ_AD_REM_IBS | VARCHAR2(7) | Y |  |  |
| 84 | ALIQ_AD_REM_CBS | VARCHAR2(7) | Y |  |  |
| 85 | VLR_MONO_IBS | VARCHAR2(17) | Y |  |  |
| 86 | VLR_MONO_CBS | VARCHAR2(17) | Y |  |  |
| 87 | QTD_TRIB_RET_MONO_IBS_CBS | VARCHAR2(15) | Y |  |  |
| 88 | ALIQ_AD_REM_RET_IBS | VARCHAR2(7) | Y |  |  |
| 89 | VLR_MONO_RET_IBS | VARCHAR2(17) | Y |  |  |
| 90 | ALIQ_AD_REM_RET_CBS | VARCHAR2(7) | Y |  |  |
| 91 | VLR_MONO_RET_CBS | VARCHAR2(17) | Y |  |  |
| 92 | QTD_TRIB_RET_ANT_IBS_CBS | VARCHAR2(15) | Y |  |  |
| 93 | ALIQ_AD_REM_RET_ANT_IBS | VARCHAR2(7) | Y |  |  |
| 94 | VLR_RET_ANT_IBS | VARCHAR2(17) | Y |  |  |
| 95 | ALIQ_AD_REM_RET_ANT_CBS | VARCHAR2(7) | Y |  |  |
| 96 | VLR_RET_ANT_CBS | VARCHAR2(17) | Y |  |  |
| 97 | PERC_DIF_MONO_IBS | VARCHAR2(7) | Y |  |  |
| 98 | VLR_MONO_DIF_IBS | VARCHAR2(17) | Y |  |  |
| 99 | PERC_DIF_MONO_CBS | VARCHAR2(7) | Y |  |  |
| 100 | VLR_MONO_DIF_CBS | VARCHAR2(17) | Y |  |  |
| 101 | ALIQ_IBS_UF_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 102 | VLR_IBS_UF_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 103 | ALIQ_IBS_MUN_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 104 | VLR_IBS_MUN_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 105 | ALIQ_CBS_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 106 | VLR_CBS_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 107 | CHAVE_DFE_REF | VARCHAR2(44) | Y |  |  |
| 108 | VLR_TOT_IS | VARCHAR2(17) | Y |  |  |
| 109 | VLR_TOT_BC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 110 | VLR_TOT_DIF_IBS_UF | VARCHAR2(17) | Y |  |  |
| 111 | VLR_TOT_DEV_TRIB_IBS_UF | VARCHAR2(17) | Y |  |  |
| 112 | VLR_TOT_IBS_UF | VARCHAR2(17) | Y |  |  |
| 113 | VLR_TOT_DIF_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 114 | VLR_TOT_DEV_TRIB_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 115 | VLR_TOT_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 116 | VLR_TOT_IBS | VARCHAR2(17) | Y |  |  |
| 117 | VLR_TOT_CRED_PRES_IBS | VARCHAR2(17) | Y |  |  |
| 118 | VLR_TOT_CRED_PRES_C_SUS_IBS | VARCHAR2(17) | Y |  |  |
| 119 | VLR_TOT_CRED_PRES_CBS | VARCHAR2(17) | Y |  |  |
| 120 | VLR_TOT_CRED_PRES_C_SUS_CBS | VARCHAR2(17) | Y |  |  |
| 121 | VLR_TOT_DIF_CBS | VARCHAR2(17) | Y |  |  |
| 122 | VLR_TOT_DEV_TRIB_CBS | VARCHAR2(17) | Y |  |  |
| 123 | VLR_TOT_CBS | VARCHAR2(17) | Y |  |  |
| 124 | TOT_MONO_IBS | VARCHAR2(17) | Y |  |  |
| 125 | TOT_MONO_CBS | VARCHAR2(17) | Y |  |  |
| 126 | TOT_MONO_RET_IBS | VARCHAR2(17) | Y |  |  |
| 127 | TOT_MONO_RET_CBS | VARCHAR2(17) | Y |  |  |
| 128 | TOT_MONO_RET_ANT_IBS | VARCHAR2(17) | Y |  |  |
| 129 | TOT_MONO_RET_ANT_CBS | VARCHAR2(17) | Y |  |  |
| 130 | VLR_TOT_NF_IBS_CBS_IS | VARCHAR2(17) | Y |  |  |
| 131 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 132 | PST_ID | NUMBER | Y |  |  |
| 133 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 134 | DAT_GRAVACAO | DATE | Y |  |  |
| 135 | CHAVE_SAFX3007 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX3007: (CHAVE_SAFX3007)
- IX_SAFX3007: (DAT_GRAVACAO)
- IX_SAFX3007_LOTE: (NUM_LOTE)

---

## SAFX3008

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_BEM_PATR | VARCHAR2(1) | Y |  |  |
| 13 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 14 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 15 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 16 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 17 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 18 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 19 | CST_IS | VARCHAR2(3) | Y |  |  |
| 20 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 21 | BC_IS | VARCHAR2(17) | Y |  |  |
| 22 | ALIQ_IS | VARCHAR2(7) | Y |  |  |
| 23 | ALIQ_ESPEC_UNID_MED_APR_IS | VARCHAR2(7) | Y |  |  |
| 24 | VLR_IS | VARCHAR2(17) | Y |  |  |
| 25 | UNID_MED_TRIBUT_IS | VARCHAR2(8) | Y |  |  |
| 26 | QTD_TRIB_IS | VARCHAR2(15) | Y |  |  |
| 27 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 28 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 29 | BC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 30 | VLR_MON_DOCREF_N_INC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 31 | ALIQ_IBS_UF | VARCHAR2(7) | Y |  |  |
| 32 | VLR_IBS_UF | VARCHAR2(17) | Y |  |  |
| 33 | PERC_DIF_IBS_UF | VARCHAR2(7) | Y |  |  |
| 34 | VLR_DIF_IBS_UF | VARCHAR2(17) | Y |  |  |
| 35 | VLR_TRIB_DEV_IBS_UF | VARCHAR2(17) | Y |  |  |
| 36 | PERC_RED_ALIQ_IBS_UF | VARCHAR2(7) | Y |  |  |
| 37 | ALIQ_EFET_IBS_UF | VARCHAR2(7) | Y |  |  |
| 38 | ALIQ_CBS | VARCHAR2(7) | Y |  |  |
| 39 | VLR_CBS | VARCHAR2(17) | Y |  |  |
| 40 | PERC_DIF_CBS | VARCHAR2(7) | Y |  |  |
| 41 | VLR_DIF_CBS | VARCHAR2(17) | Y |  |  |
| 42 | VLR_BRUTO_CBS | VARCHAR2(17) | Y |  |  |
| 43 | VLR_TRIB_DEV_CBS | VARCHAR2(17) | Y |  |  |
| 44 | PERC_RED_ALIQ_CBS | VARCHAR2(7) | Y |  |  |
| 45 | ALIQ_EFET_CBS | VARCHAR2(7) | Y |  |  |
| 46 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 47 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 48 | ALIQ_TRIB_REG_IBS_UF | VARCHAR2(7) | Y |  |  |
| 49 | VLR_TRIB_REG_TRIB_IBS_UF | VARCHAR2(17) | Y |  |  |
| 50 | ALIQ_TRIB_REG_CBS | VARCHAR2(7) | Y |  |  |
| 51 | VLR_TRIB_REG_TRIB_CBS | VARCHAR2(17) | Y |  |  |
| 52 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 53 | PERC_CRED_PRES_IBS | VARCHAR2(7) | Y |  |  |
| 54 | ALIQ_CRED_PRES_IBS | VARCHAR2(7) | Y |  |  |
| 55 | VLR_CRED_PRES_IBS | VARCHAR2(17) | Y |  |  |
| 56 | VLR_CRED_PRES_COND_SUSP_IBS | VARCHAR2(17) | Y |  |  |
| 57 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 58 | PERC_CRED_PRES_CBS | VARCHAR2(7) | Y |  |  |
| 59 | ALIQ_CRED_PRES_CBS | VARCHAR2(7) | Y |  |  |
| 60 | VLR_CRED_PRES_CBS | VARCHAR2(17) | Y |  |  |
| 61 | VLR_CRED_PRES_COND_SUSP_CBS | VARCHAR2(17) | Y |  |  |
| 62 | QTD_TRIB_MONO_IBS_CBS | VARCHAR2(15) | Y |  |  |
| 63 | ALIQ_AD_REM_IBS | VARCHAR2(7) | Y |  |  |
| 64 | ALIQ_AD_REM_CBS | VARCHAR2(7) | Y |  |  |
| 65 | VLR_MONO_IBS | VARCHAR2(17) | Y |  |  |
| 66 | VLR_MONO_CBS | VARCHAR2(17) | Y |  |  |
| 67 | QTD_TRIB_RET_MONO_IBS_CBS | VARCHAR2(15) | Y |  |  |
| 68 | ALIQ_AD_REM_RET_IBS | VARCHAR2(7) | Y |  |  |
| 69 | VLR_MONO_RET_IBS | VARCHAR2(17) | Y |  |  |
| 70 | ALIQ_AD_REM_RET_CBS | VARCHAR2(7) | Y |  |  |
| 71 | VLR_MONO_RET_CBS | VARCHAR2(17) | Y |  |  |
| 72 | QTD_TRIB_RET_ANT_IBS_CBS | VARCHAR2(15) | Y |  |  |
| 73 | ALIQ_AD_REM_RET_ANT_IBS | VARCHAR2(7) | Y |  |  |
| 74 | VLR_RET_ANT_IBS | VARCHAR2(17) | Y |  |  |
| 75 | ALIQ_AD_REM_RET_ANT_CBS | VARCHAR2(7) | Y |  |  |
| 76 | VLR_RET_ANT_CBS | VARCHAR2(17) | Y |  |  |
| 77 | PERC_DIF_MONO_IBS | VARCHAR2(7) | Y |  |  |
| 78 | VLR_MONO_DIF_IBS | VARCHAR2(17) | Y |  |  |
| 79 | PERC_DIF_MONO_CBS | VARCHAR2(7) | Y |  |  |
| 80 | VLR_MONO_DIF_CBS | VARCHAR2(17) | Y |  |  |
| 81 | ALIQ_IBS_UF_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 82 | VLR_IBS_UF_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 83 | ALIQ_IBS_MUN_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 84 | VLR_IBS_MUN_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 85 | ALIQ_CBS_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 86 | VLR_CBS_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 87 | VLR_TOT_ITEM | VARCHAR2(17) | Y |  |  |
| 88 | NUM_ITEM_DOC_REFERENCIADO | VARCHAR2(3) | Y |  |  |
| 89 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 90 | PST_ID | NUMBER | Y |  |  |
| 91 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 92 | DAT_GRAVACAO | DATE | Y |  |  |
| 93 | CHAVE_SAFX3008 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX3008: (CHAVE_SAFX3008)
- IX_SAFX3008: (DAT_GRAVACAO)
- IX_SAFX3008_LOTE: (NUM_LOTE)

---

## SAFX3009

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 13 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 14 | COD_MUN_FT_GER_IBS_CBS | VARCHAR2(7) | Y |  |  |
| 15 | CST_IS | VARCHAR2(3) | Y |  |  |
| 16 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 17 | BC_IS | VARCHAR2(17) | Y |  |  |
| 18 | ALIQ_IS | VARCHAR2(7) | Y |  |  |
| 19 | ALIQ_ESPEC_UNID_MED_APR_IS | VARCHAR2(7) | Y |  |  |
| 20 | VLR_IS | VARCHAR2(17) | Y |  |  |
| 21 | UNID_MED_TRIBUT_IS | VARCHAR2(8) | Y |  |  |
| 22 | QTD_TRIB_IS | VARCHAR2(15) | Y |  |  |
| 23 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 24 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 25 | BC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 26 | VLR_MON_DOCREF_N_INC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 27 | ALIQ_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 28 | VLR_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 29 | PERC_DIF_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 30 | VLR_DIF_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 31 | VLR_BRUTO_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 32 | VLR_TRIB_DEV_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 33 | PERC_RED_ALIQ_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 34 | ALIQ_EFET_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 35 | ALIQ_CBS | VARCHAR2(7) | Y |  |  |
| 36 | VLR_CBS | VARCHAR2(17) | Y |  |  |
| 37 | VLR_BRUTO_CBS | VARCHAR2(17) | Y |  |  |
| 38 | VLR_TRIB_DEV_CBS | VARCHAR2(17) | Y |  |  |
| 39 | PERC_RED_ALIQ_CBS | VARCHAR2(7) | Y |  |  |
| 40 | ALIQ_EFET_CBS | VARCHAR2(7) | Y |  |  |
| 41 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 42 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 43 | ALIQ_TRIB_REG_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 44 | VLR_TRIB_REG_TRIB_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 45 | ALIQ_TRIB_REG_CBS | VARCHAR2(7) | Y |  |  |
| 46 | VLR_TRIB_REG_TRIB_CBS | VARCHAR2(17) | Y |  |  |
| 47 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 48 | PERC_CRED_PRES_IBS | VARCHAR2(7) | Y |  |  |
| 49 | ALIQ_CRED_PRES_IBS | VARCHAR2(7) | Y |  |  |
| 50 | VLR_CRED_PRES_IBS | VARCHAR2(17) | Y |  |  |
| 51 | VLR_CRED_PRES_COND_SUSP_IBS | VARCHAR2(17) | Y |  |  |
| 52 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 53 | PERC_CRED_PRES_CBS | VARCHAR2(7) | Y |  |  |
| 54 | ALIQ_CRED_PRES_CBS | VARCHAR2(7) | Y |  |  |
| 55 | VLR_CRED_PRES_CBS | VARCHAR2(17) | Y |  |  |
| 56 | VLR_CRED_PRES_COND_SUSP_CBS | VARCHAR2(17) | Y |  |  |
| 57 | ALIQ_IBS_UF_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 58 | VLR_IBS_UF_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 59 | ALIQ_IBS_MUN_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 60 | VLR_IBS_MUN_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 61 | ALIQ_CBS_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 62 | VLR_CBS_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 63 | VLR_TOT_ITEM | VARCHAR2(17) | Y |  |  |
| 64 | NUM_ITEM_DOC_REFERENCIADO | VARCHAR2(3) | Y |  |  |
| 65 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 66 | PST_ID | NUMBER | Y |  |  |
| 67 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 68 | DAT_GRAVACAO | DATE | Y |  |  |
| 69 | CHAVE_SAFX3009 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX3009: (CHAVE_SAFX3009)
- IX_SAFX3009: (DAT_GRAVACAO)
- IX_SAFX3009_LOTE: (NUM_LOTE)

---

## SAFX301

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 12 | NUM_PARCELA | VARCHAR2(3) | Y |  |  |
| 13 | DATA_VENCTO | VARCHAR2(8) | Y |  |  |
| 14 | VLR_PARCELA | VARCHAR2(17) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | VLR_JUROS | VARCHAR2(17) | Y |  |  |
| 17 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 18 | VLR_IRRF | VARCHAR2(17) | Y |  |  |
| 19 | DATA_PGTO | VARCHAR2(8) | Y |  |  |
| 20 | IND_PGTO | CHAR(1) | Y |  |  |
| 21 | DESC_PGTO | VARCHAR2(100) | Y |  |  |
| 22 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 23 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | CHAVE_SAFX301 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX301: (CHAVE_SAFX301)
- IX_SAFX301: (DAT_GRAVACAO)
- IX_SAFX301_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX301_LOTE: (NUM_LOTE)

---

## SAFX302

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | NUM_CRZ | VARCHAR2(6) | Y |  |  |
| 6 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 7 | COD_TOTALIZADOR_ECF | VARCHAR2(7) | Y |  |  |
| 8 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 10 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 11 | QTD_CONV | VARCHAR2(17) | Y |  |  |
| 12 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 13 | VLR_UNIT_CONV | VARCHAR2(19) | Y |  |  |
| 14 | VLR_UNIT_ICMS_OPER_CONV | VARCHAR2(19) | Y |  |  |
| 15 | VLR_UNIT_ICMS_CONV | VARCHAR2(19) | Y |  |  |
| 16 | VLR_UNIT_ICMS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 17 | VLR_UNIT_ICMSS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 18 | VLR_UNIT_FCPS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 19 | VLR_UNIT_ICMSS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 20 | VLR_UNIT_FCPS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 21 | VLR_UNIT_ICMSS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 22 | VLR_UNIT_FCPS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 23 | DAT_GRAVACAO | DATE | Y |  |  |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | CHAVE_SAFX302 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX302: (CHAVE_SAFX302)
- IX_SAFX302: (DAT_GRAVACAO)
- IX_SAFX302_LOTE: (NUM_LOTE)

---

## SAFX303

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | NUM_EQUIP | VARCHAR2(9) | Y |  |  |
| 5 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 9 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 10 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 11 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 12 | QTD_CONV | VARCHAR2(17) | Y |  |  |
| 13 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 14 | VLR_UNIT_CONV | VARCHAR2(19) | Y |  |  |
| 15 | VLR_UNIT_ICMS_OPER_CONV | VARCHAR2(19) | Y |  |  |
| 16 | VLR_UNIT_ICMS_CONV | VARCHAR2(19) | Y |  |  |
| 17 | VLR_UNIT_ICMS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 18 | VLR_UNIT_ICMSS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 19 | VLR_UNIT_FCPS_ESTQ_CONV | VARCHAR2(19) | Y |  |  |
| 20 | VLR_UNIT_ICMSS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 21 | VLR_UNIT_FCPS_REST_CONV | VARCHAR2(19) | Y |  |  |
| 22 | VLR_UNIT_ICMSS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 23 | VLR_UNIT_FCPS_COMPL_CONV | VARCHAR2(19) | Y |  |  |
| 24 | DAT_GRAVACAO | DATE | Y |  |  |
| 25 | PST_ID | NUMBER | Y |  |  |
| 26 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 27 | CHAVE_SAFX303 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX303: (CHAVE_SAFX303)
- IX_SAFX303: (DAT_GRAVACAO)
- IX_SAFX303_LOTE: (NUM_LOTE)

---

## SAFX304

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 5 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 6 | VLR_ICMS_ST_REST | VARCHAR2(17) | Y |  |  |
| 7 | VLR_FCP_ST_REST | VARCHAR2(17) | Y |  |  |
| 8 | VLR_ICMS_ST_COMP | VARCHAR2(17) | Y |  |  |
| 9 | VLR_FCP_ST_COMP | VARCHAR2(17) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX304 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX304: (CHAVE_SAFX304)
- IX_SAFX304_LOTE: (NUM_LOTE)
- SAFX304: (DAT_GRAVACAO)

---

## SAFX3042

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | VLR_TOT_BC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 10 | VLR_TOT_DIF_IBS_UF | VARCHAR2(17) | Y |  |  |
| 11 | VLR_TOT_DEV_TRIB_IBS_UF | VARCHAR2(17) | Y |  |  |
| 12 | VLR_TOT_IBS_UF | VARCHAR2(17) | Y |  |  |
| 13 | VLR_TOT_DIF_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 14 | VLR_TOT_DEV_TRIB_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 15 | VLR_TOT_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 16 | VLR_TOT_IBS | VARCHAR2(17) | Y |  |  |
| 17 | VLR_TOT_DIF_CBS | VARCHAR2(17) | Y |  |  |
| 18 | VLR_TOT_DEV_TRIB_CBS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_TOT_CBS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_TOT_TRIB_REG_IBS_UF | VARCHAR2(17) | Y |  |  |
| 21 | VLR_TOT_TRIB_REG_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 22 | VLR_TOT_TRIB_REG_CBS | VARCHAR2(17) | Y |  |  |
| 23 | VLR_TOT_IBS_UF_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 24 | VLR_TOT_IBS_MUN_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 25 | VLR_TOT_CBS_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 26 | VLR_TOT_IBS_ESTORNADO | VARCHAR2(17) | Y |  |  |
| 27 | VLR_TOT_CBS_ESTORNADO | VARCHAR2(17) | Y |  |  |
| 28 | TIPO_ENTE_GOVERN | VARCHAR2(1) | Y |  |  |
| 29 | PERC_RED_ALIQ_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 30 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 31 | PST_ID | NUMBER | Y |  |  |
| 32 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 33 | DAT_GRAVACAO | DATE | Y |  |  |
| 34 | CHAVE_SAFX3042 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX3042: (CHAVE_SAFX3042)
- IX_SAFX3042: (DAT_GRAVACAO)
- IX_SAFX3042_LOTE: (NUM_LOTE)

---

## SAFX3043

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_ITEM | VARCHAR2(7) | Y |  |  |
| 10 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 11 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 12 | IND_DOACAO | VARCHAR2(1) | Y |  |  |
| 13 | BC_IBS_CBS | VARCHAR2(17) | Y |  |  |
| 14 | ALIQ_IBS_UF | VARCHAR2(7) | Y |  |  |
| 15 | PERC_DIF_IBS_UF | VARCHAR2(7) | Y |  |  |
| 16 | VLR_DIF_IBS_UF | VARCHAR2(17) | Y |  |  |
| 17 | VLR_TRIB_DEV_IBS_UF | VARCHAR2(17) | Y |  |  |
| 18 | PERC_RED_ALIQ_IBS_UF | VARCHAR2(7) | Y |  |  |
| 19 | ALIQ_EFET_IBS_UF | VARCHAR2(7) | Y |  |  |
| 20 | VLR_IBS_UF | VARCHAR2(17) | Y |  |  |
| 21 | ALIQ_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 22 | PERC_DIF_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 23 | VLR_DIF_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 24 | VLR_TRIB_DEV_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 25 | PERC_RED_ALIQ_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 26 | ALIQ_EFET_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 27 | VLR_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 28 | TOT_IBS_ITEM | VARCHAR2(17) | Y |  |  |
| 29 | ALIQ_CBS | VARCHAR2(7) | Y |  |  |
| 30 | PERC_DIF_CBS | VARCHAR2(7) | Y |  |  |
| 31 | VLR_DIF_CBS | VARCHAR2(17) | Y |  |  |
| 32 | VLR_TRIB_DEV_CBS | VARCHAR2(17) | Y |  |  |
| 33 | PERC_RED_ALIQ_CBS | VARCHAR2(7) | Y |  |  |
| 34 | ALIQ_EFET_CBS | VARCHAR2(7) | Y |  |  |
| 35 | VLR_CBS | VARCHAR2(17) | Y |  |  |
| 36 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 37 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 38 | ALIQ_TRIB_REG_IBS_UF | VARCHAR2(7) | Y |  |  |
| 39 | VLR_TRIB_REG_IBS_UF | VARCHAR2(17) | Y |  |  |
| 40 | ALIQ_TRIB_REG_IBS_MUN | VARCHAR2(7) | Y |  |  |
| 41 | VLR_TRIB_REG_IBS_MUN | VARCHAR2(17) | Y |  |  |
| 42 | ALIQ_TRIB_REG_CBS | VARCHAR2(7) | Y |  |  |
| 43 | VLR_TRIB_REG_CBS | VARCHAR2(17) | Y |  |  |
| 44 | ALIQ_IBS_UF_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 45 | VLR_IBS_UF_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 46 | ALIQ_IBS_MUN_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 47 | VLR_IBS_MUN_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 48 | ALIQ_CBS_COMPRA_GOVERN | VARCHAR2(7) | Y |  |  |
| 49 | VLR_CBS_COMPRA_GOVERN | VARCHAR2(17) | Y |  |  |
| 50 | IBS_ESTORNADO | VARCHAR2(17) | Y |  |  |
| 51 | CBS_ESTORNADO | VARCHAR2(17) | Y |  |  |
| 52 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 53 | PST_ID | NUMBER | Y |  |  |
| 54 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 55 | DAT_GRAVACAO | DATE | Y |  |  |
| 56 | CHAVE_SAFX3043 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX3043: (CHAVE_SAFX3043)
- IX_SAFX3043: (DAT_GRAVACAO)
- IX_SAFX3043_LOTE: (NUM_LOTE)

---

## SAFX305

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | NUM_GUIA_RECOL | VARCHAR2(30) | Y |  |  |
| 7 | DAT_GUIA_RECOL | VARCHAR2(8) | Y |  |  |
| 8 | VAL_GUIA_RECOL | VARCHAR2(17) | Y |  |  |
| 9 | DAT_ENTREGA | VARCHAR2(8) | Y |  |  |
| 10 | DSC_LOCAL_ENTREGA | VARCHAR2(25) | Y |  |  |
| 11 | COD_ORG_ARRECAD | VARCHAR2(10) | Y |  |  |
| 12 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 13 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 14 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 15 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 16 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 17 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 18 | DSC_COMPLEMENTAR | VARCHAR2(100) | Y |  |  |
| 19 | DAT_VENCTO | VARCHAR2(8) | Y |  |  |
| 20 | MES_ANO_REF | VARCHAR2(6) | Y |  |  |
| 21 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 22 | IND_GUIA_CONV | CHAR(1) | Y |  |  |
| 23 | COD_ESTADO_CONV | VARCHAR2(2) | Y |  |  |
| 24 | IND_TIPO_DOC_ARREC | CHAR(1) | Y |  |  |
| 25 | NUM_AUTENTIC | VARCHAR2(25) | Y |  |  |
| 26 | VAL_DOC_ORIG | VARCHAR2(17) | Y |  |  |
| 27 | VAL_DESCONTO | VARCHAR2(17) | Y |  |  |
| 28 | VAL_MULTA_MORA | VARCHAR2(17) | Y |  |  |
| 29 | VAL_JUROS | VARCHAR2(17) | Y |  |  |
| 30 | VAL_MULTA | VARCHAR2(17) | Y |  |  |
| 31 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 32 | COD_DEB_ICMS | VARCHAR2(3) | Y |  |  |
| 33 | DAT_GRAVACAO | DATE | Y |  |  |
| 34 | PST_ID | NUMBER | Y |  |  |
| 35 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 36 | CHAVE_SAFX305 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX305: (CHAVE_SAFX305)
- IX_SAFX305_LOTE: (NUM_LOTE)

---

## SAFX306

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | VLR_ALIQ_INT | VARCHAR2(7) | Y |  |  |
| 6 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 7 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 8 | IND_FCP | CHAR(1) | Y |  |  |
| 9 | ALIQ_FCP | VARCHAR2(7) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | PRC_REDUCAO_BC | VARCHAR2(7) | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | TIPO_REGISTRO | VARCHAR2(1) | Y |  |  |
| 15 | IND_PRODUTO_ASS | VARCHAR2(1) | Y |  |  |
| 16 | COD_PRODUTO_ASS | VARCHAR2(60) | Y |  |  |
| 17 | CHAVE_SAFX306 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX306: (CHAVE_SAFX306)
- IX_SAFX306_LOTE: (NUM_LOTE)

---

## SAFX307

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 4 | VLR_ALIQ_INT | VARCHAR2(7) | Y |  |  |
| 5 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 6 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 7 | IND_FCP | CHAR(1) | Y |  |  |
| 8 | ALIQ_FCP | VARCHAR2(7) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | PRC_REDUCAO_BC | VARCHAR2(7) | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX307 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX307: (CHAVE_SAFX307)
- IX_SAFX307_LOTE: (NUM_LOTE)

---

## SAFX308

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | ESPECIE_DOCTO_DEV | VARCHAR2(1) | Y |  |  |
| 17 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 18 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 19 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 20 | COD_DOCTO_REF | VARCHAR2(5) | Y |  |  |
| 21 | DATA_FISCAL_REF | VARCHAR2(8) | Y |  |  |
| 22 | IND_FIS_JUR_REF | VARCHAR2(1) | Y |  |  |
| 23 | COD_FIS_JUR_REF | VARCHAR2(14) | Y |  |  |
| 24 | COD_MODELO_REF | VARCHAR2(2) | Y |  |  |
| 25 | COD_CAIXA_ECF_REF | VARCHAR2(3) | Y |  |  |
| 26 | NUM_COO_REF | VARCHAR2(9) | Y |  |  |
| 27 | DATA_EMISSAO_REF | VARCHAR2(8) | Y |  |  |
| 28 | NUM_EQUIP_REF | VARCHAR2(9) | Y |  |  |
| 29 | NUM_CUPOM_REF | VARCHAR2(6) | Y |  |  |
| 30 | NUM_ITEM_DOC_REF | VARCHAR2(5) | Y |  |  |
| 31 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 32 | QTD_CONV | VARCHAR2(17) | Y |  |  |
| 33 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 34 | VLR_UNIT_CONV | VARCHAR2(19) | Y |  |  |
| 35 | VLR_ICMS_CONV | VARCHAR2(19) | Y |  |  |
| 36 | VLR_UNIT_BC_ICMSS_ENT | VARCHAR2(19) | Y |  |  |
| 37 | VLR_UNIT_ICMSS_CONV_ENT | VARCHAR2(19) | Y |  |  |
| 38 | VLR_UNIT_FCP_CONV_ENT | VARCHAR2(19) | Y |  |  |
| 39 | VLR_UNIT_ICMS_ESTQ_SAI | VARCHAR2(19) | Y |  |  |
| 40 | VLR_UNIT_ICMSS_ESTQ_SAI | VARCHAR2(19) | Y |  |  |
| 41 | VLR_UNIT_FCP_ESTQ_SAI | VARCHAR2(19) | Y |  |  |
| 42 | VLR_UNIT_ICMS_OPER_SAI | VARCHAR2(19) | Y |  |  |
| 43 | VLR_UNIT_ICMSS_REST_SAI | VARCHAR2(19) | Y |  |  |
| 44 | VLR_UNIT_FCP_REST_SAI | VARCHAR2(19) | Y |  |  |
| 45 | VLR_UNIT_ICMSS_COMPL_SAI | VARCHAR2(19) | Y |  |  |
| 46 | VLR_UNIT_FCP_COMPL_SAI | VARCHAR2(19) | Y |  |  |
| 47 | DAT_GRAVACAO | DATE | Y |  |  |
| 48 | PST_ID | NUMBER | Y |  |  |
| 49 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 50 | CHAVE_SAFX308 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX308: (CHAVE_SAFX308)

---

## SAFX309

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | NUM_DISCRIMINACAO | VARCHAR2(12) | Y |  |  |
| 8 | COD_AJUSTE_ICMS | VARCHAR2(8) | Y |  |  |
| 9 | VAL_DEBITO | VARCHAR2(17) | Y |  |  |
| 10 | DSC_DEBITO | VARCHAR2(250) | Y |  |  |
| 11 | IND_SUB_APUR | CHAR(1) | Y |  |  |
| 12 | IND_EST_DEB_CONV | CHAR(1) | Y |  |  |
| 13 | COD_ESTADO_CONV | VARCHAR2(2) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX309 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX309: (CHAVE_SAFX309)
- IX_SAFX309_LOTE: (NUM_LOTE)

---

## SAFX31

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTRUT_CONT | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | DAT_SALDO | VARCHAR2(8) | Y |  |  |
| 5 | COD_GRUPO_CONT | CHAR(1) | Y |  |  |
| 6 | COD_SUBGRUPO_CONT | VARCHAR2(2) | Y |  |  |
| 7 | COD_CONTA | VARCHAR2(6) | Y |  |  |
| 8 | VLR_SALDO_ANT | VARCHAR2(17) | Y |  |  |
| 9 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |

**Indexes**:
- IX_SAFX31: (DAT_GRAVACAO)

---

## SAFX310

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | NUM_DISCRIMINACAO | VARCHAR2(12) | Y |  |  |
| 8 | SEQ_PROC_ARRECAD | VARCHAR2(12) | Y |  |  |
| 9 | NUM_DOC_ARRECAD | VARCHAR2(50) | Y |  |  |
| 10 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 11 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 12 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 13 | DSC_COMPLEMENTAR | VARCHAR2(150) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX310 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX310: (CHAVE_SAFX310)
- IX_SAFX310_LOTE: (NUM_LOTE)

---

## SAFX311

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | IND_TP_APUR | CHAR(1) | Y |  |  |
| 6 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 7 | NUM_DISCRIMINACAO | VARCHAR2(12) | Y |  |  |
| 8 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 9 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 10 | NORM_DEV | CHAR(1) | Y |  |  |
| 11 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 12 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 13 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 14 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 15 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 16 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 17 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 18 | VLR_AJUSTE | VARCHAR2(17) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX311 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX311: (CHAVE_SAFX311)
- IX_SAFX311_LOTE: (NUM_LOTE)

---

## SAFX312

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MCAPT | VARCHAR2(36) | Y |  |  |
| 4 | NUM_LOG | VARCHAR2(36) | Y |  |  |
| 5 | IND_TP_TECN | CHAR(1) | Y |  |  |
| 6 | IND_TERM_PROP | CHAR(1) | Y |  |  |
| 7 | DSC_MARCA | VARCHAR2(50) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | IND_SMARTPOS | VARCHAR2(1) | Y |  |  |
| 12 | CHAVE_SAFX312 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX312: (CHAVE_SAFX312)
- IX_SAFX312: (DAT_GRAVACAO)
- IX_SAFX312_LOTE: (NUM_LOTE)

---

## SAFX313

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DT_OP | VARCHAR2(8) | Y |  |  |
| 4 | IND_IP_PAR | VARCHAR2(1) | Y |  |  |
| 5 | COD_IP_PAR | VARCHAR2(14) | Y |  |  |
| 6 | IND_COD_CLIENTE | VARCHAR2(1) | Y |  |  |
| 7 | COD_CLIENTE | VARCHAR2(14) | Y |  |  |
| 8 | IND_COMEX | VARCHAR2(1) | Y |  |  |
| 9 | IND_EXTEMP | VARCHAR2(1) | Y |  |  |
| 10 | COD_MCAPT | VARCHAR2(36) | Y |  |  |
| 11 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 12 | QTD_TOT | VARCHAR2(10) | Y |  |  |
| 13 | CNPJ_ADQUI | VARCHAR2(14) | Y |  |  |
| 14 | NSU | VARCHAR2(30) | Y |  |  |
| 15 | COD_AUT | VARCHAR2(60) | Y |  |  |
| 16 | ID_TRANSAC | VARCHAR2(60) | Y |  |  |
| 17 | IND_SPLIT | VARCHAR2(1) | Y |  |  |
| 18 | BANDEIRA | VARCHAR2(10) | Y |  |  |
| 19 | HORA | VARCHAR2(6) | Y |  |  |
| 20 | VLR_OP | VARCHAR2(17) | Y |  |  |
| 21 | IND_OPER_NAT_PAG | VARCHAR2(1) | Y |  |  |
| 22 | GEO | VARCHAR2(15) | Y |  |  |
| 23 | CHAVE_NF | VARCHAR2(80) | Y |  |  |
| 24 | CNPJ_CPF_DEST | VARCHAR2(14) | Y |  |  |
| 25 | ID_DEST | VARCHAR2(30) | Y |  |  |
| 26 | SITUACAO | VARCHAR2(1) | Y |  |  |
| 27 | DT_CANCELAMENTO | VARCHAR2(8) | Y |  |  |
| 28 | TIPO_CANCELAMENTO | VARCHAR2(1) | Y |  |  |
| 29 | VLR_CANCELAMENTO | VARCHAR2(17) | Y |  |  |
| 30 | COD_CHAVE_NFSE | VARCHAR2(44) | Y |  |  |
| 31 | COD_CHAVE_DCE | VARCHAR2(44) | Y |  |  |
| 32 | IND_SUB | VARCHAR2(1) | Y |  |  |
| 33 | UF_ORIGEM | VARCHAR2(2) | Y |  |  |
| 34 | CNPJ_ORIGEM | VARCHAR2(14) | Y |  |  |
| 35 | ID_TRANSAC_COMPL | VARCHAR2(60) | Y |  |  |
| 36 | DAT_GRAVACAO | DATE | Y |  |  |
| 37 | PST_ID | NUMBER | Y |  |  |
| 38 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 39 | IND_NAT_JUR | VARCHAR2(1) | Y |  |  |
| 40 | IND_TP_PIX | VARCHAR2(1) | Y |  |  |
| 41 | ID_PEDIDO | VARCHAR2(255) | Y |  |  |
| 42 | IND_NAO_GERA_REG | VARCHAR2(1) | Y |  |  |
| 43 | DSC_MOTIVO_NAO_GERA_REG | VARCHAR2(255) | Y |  |  |
| 44 | DT_LIQUIDACAO | VARCHAR2(8) | Y |  |  |
| 45 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 46 | IND_TP_REL | VARCHAR2(1) | Y |  |  |
| 47 | IND_INFO_SELLER | VARCHAR2(1) | Y |  |  |
| 48 | ID_SELLER | VARCHAR2(255) | Y |  |  |
| 49 | QTD_CANCELAMENTO | VARCHAR2(10) | Y |  |  |
| 50 | CHAVE_SAFX313 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX313: (CHAVE_SAFX313)
- IX_SAFX313: (DAT_GRAVACAO)
- IX_SAFX313_LOTE: (NUM_LOTE)

---

## SAFX314

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 5 | TP_AUTORIZ | CHAR(1) | Y |  |  |
| 6 | TP_TRANSAC | CHAR(1) | Y |  |  |
| 7 | DT_INI_AUT | VARCHAR2(8) | Y |  |  |
| 8 | DT_FIM_AUT | VARCHAR2(8) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX314 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX314: (CHAVE_SAFX314)
- IX_SAFX314: (DAT_GRAVACAO)
- IX_SAFX314_LOTE: (NUM_LOTE)

---

## SAFX315

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 5 | DAT_VALIDADE | VARCHAR2(8) | Y |  |  |
| 6 | CNPJ_VAN | VARCHAR2(14) | Y |  |  |
| 7 | RAZAO_SOCIAL_VAN | VARCHAR2(70) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX315 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX315: (CHAVE_SAFX315)
- IX_SAFX315: (DAT_GRAVACAO)
- IX_SAFX315_LOTE: (NUM_LOTE)

---

## SAFX316

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | CNPJ_VAN | VARCHAR2(14) | Y |  |  |
| 4 | DAT_PERIODO | VARCHAR2(8) | Y |  |  |
| 5 | QTD | VARCHAR2(10) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | VLR_TRANS | VARCHAR2(17) | Y |  |  |
| 10 | CHAVE_SAFX316 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX316: (CHAVE_SAFX316)
- IX_SAFX316: (DAT_GRAVACAO)
- IX_SAFX316_LOTE: (NUM_LOTE)

---

## SAFX317

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | IND_FIS_JUR_IT | CHAR(1) | Y |  |  |
| 7 | COD_FIS_JUR_IT | VARCHAR2(14) | Y |  |  |
| 8 | VLR_TOT_OP_ICMS | VARCHAR2(17) | Y |  |  |
| 9 | VLR_TOT_OP_ISS | VARCHAR2(17) | Y |  |  |
| 10 | VLR_TOT_OP_OUTR | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX317 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX317: (CHAVE_SAFX317)
- IX_SAFX317: (DAT_GRAVACAO)
- IX_SAFX317_LOTE: (NUM_LOTE)

---

## SAFX318

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 3 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 4 | COD_BARRA | VARCHAR2(255) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX318 | VARCHAR2(4000) | Y | NVL("IND_PRODUTO",'@')\|\|NVL("COD_PRODUTO",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX318: (CHAVE_SAFX318)
- IX_SAFX318: (DAT_GRAVACAO)
- IX_SAFX318_LOTE: (NUM_LOTE)

---

## SAFX319

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 4 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 5 | COD_AJUSTE | VARCHAR2(8) | Y |  |  |
| 6 | VLR_SALDO_ANT | VARCHAR2(17) | Y |  |  |
| 7 | VLR_TOT_CRED_MES | VARCHAR2(17) | Y |  |  |
| 8 | VLR_CRED_TRANSF | VARCHAR2(17) | Y |  |  |
| 9 | VLR_CRED_PERIODO | VARCHAR2(17) | Y |  |  |
| 10 | VLR_CRED_TRANSP | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX319 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX319: (CHAVE_SAFX319)
- IX_SAFX319: (DAT_GRAVACAO)
- IX_SAFX319_LOTE: (NUM_LOTE)

---

## SAFX32

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | DSC_ARQUIVO | VARCHAR2(20) | Y |  |  |
| 5 | QTD_REGISTROS | VARCHAR2(8) | Y |  |  |
| 6 | VLR_TOTAL | VARCHAR2(17) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX32 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX32: (CHAVE_SAFX32)
- IX_SAFX32: (DAT_GRAVACAO)
- IX_SAFX32_LOTE: (NUM_LOTE)

---

## SAFX320

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 4 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 5 | COD_AJUSTE | VARCHAR2(8) | Y |  |  |
| 6 | TP_UTIL_CRED | VARCHAR2(4) | Y |  |  |
| 7 | NUM_DOC | VARCHAR2(24) | Y |  |  |
| 8 | VLR_TOT_CRED | VARCHAR2(17) | Y |  |  |
| 9 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX320 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX320: (CHAVE_SAFX320)
- IX_SAFX320: (DAT_GRAVACAO)
- IX_SAFX320_LOTE: (NUM_LOTE)

---

## SAFX321

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_REF | VARCHAR2(8) | Y |  |  |
| 4 | COD_BENEF_TTD | VARCHAR2(4) | Y |  |  |
| 5 | NUM_CONCESSAO | VARCHAR2(15) | Y |  |  |
| 6 | COD_TIPO3_DCIP | VARCHAR2(4) | Y |  |  |
| 7 | VLR_BC_PREST | VARCHAR2(17) | Y |  |  |
| 8 | VLR_ICMS_PREST | VARCHAR2(17) | Y |  |  |
| 9 | COD_FUMDES | CHAR(1) | Y |  |  |
| 10 | VLR_FUMDES | VARCHAR2(17) | Y |  |  |
| 11 | COD_FUN_SOC | CHAR(1) | Y |  |  |
| 12 | VLR_FUN_SOC | VARCHAR2(17) | Y |  |  |
| 13 | VLR_BC_DEV | VARCHAR2(17) | Y |  |  |
| 14 | VLR_ICMS_DEV | VARCHAR2(17) | Y |  |  |
| 15 | VLR_FUMDES_DEV | VARCHAR2(17) | Y |  |  |
| 16 | VLR_FUN_SOC_DEV | VARCHAR2(17) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX321 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX321: (CHAVE_SAFX321)

---

## SAFX322

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 3 | VALID_INICIAL | VARCHAR2(8) | Y |  |  |
| 4 | COD_PRODUTO_OBRIG | VARCHAR2(60) | Y |  |  |
| 5 | VLR_ENC_CARAC | VARCHAR2(10) | Y |  |  |
| 6 | COD_VASILHAME | VARCHAR2(3) | Y |  |  |
| 7 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | VALID_FINAL | VARCHAR2(8) | Y |  |  |
| 12 | CHAVE_SAFX322 | VARCHAR2(4000) | Y | NVL("IND_PRODUTO",'@')\|\|NVL("COD_PRODUTO",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX322: (CHAVE_SAFX322)
- IX_SAFX322: (DAT_GRAVACAO)
- IX_SAFX322_LOTE: (NUM_LOTE)

---

## SAFX323

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INVENTARIO | VARCHAR2(8) | Y |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 5 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 7 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 8 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 9 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 10 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 11 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 12 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 13 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 14 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 15 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 16 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 17 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 18 | VLR_UNIT | VARCHAR2(18) | Y |  |  |
| 19 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 20 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 21 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 22 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 23 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 26 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 27 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 28 | DAT_GRAVACAO | DATE | Y |  |  |
| 29 | PST_ID | NUMBER | Y |  |  |
| 30 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 31 | CHAVE_SAFX323 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX323: (CHAVE_SAFX323)
- IX_SAFX323: (DAT_GRAVACAO)
- IX_SAFX323_LOTE: (NUM_LOTE)

---

## SAFX324

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MCAPT | VARCHAR2(36) | Y |  |  |
| 4 | IND_COD_CLIENTE | VARCHAR2(1) | Y |  |  |
| 5 | COD_CLIENTE | VARCHAR2(14) | Y |  |  |
| 6 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 7 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 8 | DAT_GRAVACAO | DATE | Y |  |  |
| 9 | PST_ID | NUMBER | Y |  |  |
| 10 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 11 | CHAVE_SAFX324 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX324: (CHAVE_SAFX324)
- IX_SAFX324: (DAT_GRAVACAO)
- IX_SAFX324_LOTE: (NUM_LOTE)

---

## SAFX325

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | PERC_B100 | VARCHAR2(7) | Y |  |  |
| 17 | PERC_GLP | VARCHAR2(7) | Y |  |  |
| 18 | PERC_GLGN_N | VARCHAR2(7) | Y |  |  |
| 19 | PERC_GLGN_I | VARCHAR2(7) | Y |  |  |
| 20 | IND_ORIGEM_COM | VARCHAR2(1) | Y |  |  |
| 21 | QTD_BC_MONO | VARCHAR2(17) | Y |  |  |
| 22 | ALIQ_AD_REM_ICMS | VARCHAR2(7) | Y |  |  |
| 23 | VLR_ICMS_MONO | VARCHAR2(17) | Y |  |  |
| 24 | QTD_BC_MONO_RETEN | VARCHAR2(17) | Y |  |  |
| 25 | ALIQ_AD_REM_ICMS_RETEN | VARCHAR2(7) | Y |  |  |
| 26 | VLR_ICMS_MONO_RETEN | VARCHAR2(17) | Y |  |  |
| 27 | PERC_RED_AD_REM | VARCHAR2(7) | Y |  |  |
| 28 | DSC_RED_AD_REM | VARCHAR2(1) | Y |  |  |
| 29 | VLR_ICMS_MONO_OP | VARCHAR2(17) | Y |  |  |
| 30 | PERC_DIF | VARCHAR2(7) | Y |  |  |
| 31 | VLR_ICMS_MONO_DIF | VARCHAR2(17) | Y |  |  |
| 32 | QTD_BC_MONO_RET | VARCHAR2(17) | Y |  |  |
| 33 | ALIQ_AD_REM_ICMS_RET | VARCHAR2(7) | Y |  |  |
| 34 | VLR_ICMS_MONO_RET | VARCHAR2(17) | Y |  |  |
| 35 | DAT_GRAVACAO | DATE | Y |  |  |
| 36 | PST_ID | NUMBER | Y |  |  |
| 37 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 38 | IND_CRED_ICMS | VARCHAR2(1) | Y |  |  |
| 39 | CHAVE_SAFX325 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX325: (CHAVE_SAFX325)
- IX_SAFX325: (DAT_GRAVACAO)
- IX_SAFX325_LOTE: (NUM_LOTE)

---

## SAFX326

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | IND_ORIG | VARCHAR2(1) | Y |  |  |
| 17 | COD_UF_ORIG | VARCHAR2(2) | Y |  |  |
| 18 | PERC_UF_ORIG | VARCHAR2(7) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX326 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX326: (CHAVE_SAFX326)
- IX_SAFX326: (DAT_GRAVACAO)
- IX_SAFX326_LOTE: (NUM_LOTE)

---

## SAFX327

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL_SAI | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S_SAI | CHAR(1) | Y |  |  |
| 5 | NORM_DEV_SAI | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO_SAI | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR_SAI | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR_SAI | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS_SAI | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS_SAI | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS_SAI | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO_SAI | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO_SAI | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO_SAI | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM_SAI | VARCHAR2(5) | Y |  |  |
| 16 | NUM_SEQ_ENT | VARCHAR2(8) | Y |  |  |
| 17 | NUM_DOCFIS_REF_SAI | VARCHAR2(12) | Y |  |  |
| 18 | SERIE_DOCFIS_REF_SAI | VARCHAR2(3) | Y |  |  |
| 19 | SSERIE_DOCFIS_REF_SAI | VARCHAR2(2) | Y |  |  |
| 20 | DATA_REF_SAI | VARCHAR2(8) | Y |  |  |
| 21 | QUANTIDADE_SAI | VARCHAR2(17) | Y |  |  |
| 22 | DATA_FISCAL_ENT | VARCHAR2(8) | Y |  |  |
| 23 | MOVTO_E_S_ENT | CHAR(1) | Y |  |  |
| 24 | NORM_DEV_ENT | CHAR(1) | Y |  |  |
| 25 | COD_DOCTO_ENT | VARCHAR2(5) | Y |  |  |
| 26 | IND_FIS_JUR_ENT | VARCHAR2(1) | Y |  |  |
| 27 | COD_FIS_JUR_ENT | VARCHAR2(14) | Y |  |  |
| 28 | NUM_DOCFIS_ENT | VARCHAR2(12) | Y |  |  |
| 29 | SERIE_DOCFIS_ENT | VARCHAR2(3) | Y |  |  |
| 30 | SUB_SERIE_DOCFIS_ENT | VARCHAR2(2) | Y |  |  |
| 31 | IND_PRODUTO_ENT | CHAR(1) | Y |  |  |
| 32 | COD_PRODUTO_ENT | VARCHAR2(60) | Y |  |  |
| 33 | COD_UND_PADRAO_ENT | VARCHAR2(8) | Y |  |  |
| 34 | NUM_ITEM_ENT | VARCHAR2(5) | Y |  |  |
| 35 | COD_MODELO_ENT | VARCHAR2(2) | Y |  |  |
| 36 | DATA_SAIDA_REC_ENT | VARCHAR2(8) | Y |  |  |
| 37 | DATA_EMISSAO_ENT | VARCHAR2(8) | Y |  |  |
| 38 | QUANTIDADE_ENT | VARCHAR2(17) | Y |  |  |
| 39 | VLR_UNIT_ENT | VARCHAR2(19) | Y |  |  |
| 40 | VLR_BASE_ICMSS_ENT | VARCHAR2(17) | Y |  |  |
| 41 | VLR_BASE_ICMSS_N_ESCRIT_ENT | VARCHAR2(17) | Y |  |  |
| 42 | VLR_BASE_ICMS_ORIG_ENT | VARCHAR2(17) | Y |  |  |
| 43 | DATA_EMISSAO_SAI | VARCHAR2(8) | Y |  |  |
| 44 | COD_CFO_SAI | VARCHAR2(4) | Y |  |  |
| 45 | COD_NAT_OP_SAI | VARCHAR2(3) | Y |  |  |
| 46 | COD_CFO_ENT | VARCHAR2(4) | Y |  |  |
| 47 | COD_NAT_OP_ENT | VARCHAR2(3) | Y |  |  |
| 48 | VLR_PRECO_ENT | VARCHAR2(19) | Y |  |  |
| 49 | VLR_FRETE_ENT | VARCHAR2(17) | Y |  |  |
| 50 | VLR_SEGURO_ENT | VARCHAR2(17) | Y |  |  |
| 51 | VLR_OUT_DEP_ENT | VARCHAR2(17) | Y |  |  |
| 52 | VLR_ALIQ_ICMS_ENT | VARCHAR2(7) | Y |  |  |
| 53 | VLR_ALIQ_ICMSS_ENT | VARCHAR2(7) | Y |  |  |
| 54 | VLR_UNIT_MERC_ENT | VARCHAR2(19) | Y |  |  |
| 55 | VLR_BASE_ST_ENT | VARCHAR2(18) | Y |  |  |
| 56 | DESC_PRODUTO_SAI | VARCHAR2(50) | Y |  |  |
| 57 | NUM_AUTENTIC_NFE_ENT | VARCHAR2(80) | Y |  |  |
| 58 | VLR_BC_ICMS_OP_PROP | VARCHAR2(17) | Y |  |  |
| 59 | VLR_ALIQ_ICMS_ULT_ENT | VARCHAR2(7) | Y |  |  |
| 60 | VLR_BC_ICMS_ULT_ENT | VARCHAR2(17) | Y |  |  |
| 61 | VLR_ICMS_ULT_ENT | VARCHAR2(18) | Y |  |  |
| 62 | VLR_ALIQ_ST_ULT_ENT | VARCHAR2(7) | Y |  |  |
| 63 | VLR_RESSARC | VARCHAR2(18) | Y |  |  |
| 64 | COD_RESP_RET | CHAR(1) | Y |  |  |
| 65 | IND_MOTIVO_RESSARC | CHAR(1) | Y |  |  |
| 66 | NUM_AUTENTIC_NFE_RET | VARCHAR2(80) | Y |  |  |
| 67 | IND_FIS_JUR_RET | VARCHAR2(1) | Y |  |  |
| 68 | COD_FIS_JUR_RET | VARCHAR2(14) | Y |  |  |
| 69 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  |  |
| 70 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  |  |
| 71 | NUM_ITEM_RET | VARCHAR2(5) | Y |  |  |
| 72 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 73 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 74 | COD_MEDIDA_SAI | VARCHAR2(8) | Y |  |  |
| 75 | VLR_BASE_ICMS_N_DEST | VARCHAR2(17) | Y |  |  |
| 76 | VLR_BASE_ICMS_OUTRAS | VARCHAR2(17) | Y |  |  |
| 77 | VLR_UNIT_RES_FCP_ST | VARCHAR2(17) | Y |  |  |
| 78 | DAT_GRAVACAO | DATE | Y |  |  |
| 79 | PST_ID | NUMBER | Y |  |  |
| 80 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 81 | CHAVE_SAFX327 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX327: (CHAVE_SAFX327)
- IX_SAFX327: (DAT_GRAVACAO)
- IX_SAFX327_LOTE: (NUM_LOTE)

---

## SAFX328

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_ESTADO_DESTINO | VARCHAR2(2) | Y |  |  |
| 5 | COD_TAG | VARCHAR2(6) | Y |  |  |
| 6 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | COD_ESTADO_QUAD | VARCHAR2(2) | Y |  |  |
| 9 | DAT_REF | VARCHAR2(8) | Y |  |  |
| 10 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 11 | COMUNIC_REF | VARCHAR2(80) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX328 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX328: (CHAVE_SAFX328)

---

## SAFX329

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_DCR | VARCHAR2(15) | Y |  |  |
| 4 | DATA_VALID | VARCHAR2(8) | Y |  |  |
| 5 | DATA_RECEB | VARCHAR2(8) | Y |  |  |
| 6 | NUM_PROTOCOLO | VARCHAR2(15) | Y |  |  |
| 7 | NUM_CONTROLE | VARCHAR2(15) | Y |  |  |
| 8 | COD_RESPONSAVEL | VARCHAR2(2) | Y |  |  |
| 9 | DENOM_PRODUTO | VARCHAR2(50) | Y |  |  |
| 10 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 11 | PESO_BRUTO | VARCHAR2(13) | Y |  |  |
| 12 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 13 | PROC_PRODUTIVO | VARCHAR2(100) | Y |  |  |
| 14 | VLR_SALAR_USS | VARCHAR2(17) | Y |  |  |
| 15 | VLR_ENCARG_USS | VARCHAR2(17) | Y |  |  |
| 16 | IND_COEFIC_RED | VARCHAR2(1) | Y |  |  |
| 17 | IND_TIPO_DCR | VARCHAR2(1) | Y |  |  |
| 18 | NUM_DCR_ANT | VARCHAR2(15) | Y |  |  |
| 19 | NUM_PROC_ANT | VARCHAR2(15) | Y |  |  |
| 20 | VLR_COEF_RED | VARCHAR2(7) | Y |  |  |
| 21 | PESO_LIQUIDO | VARCHAR2(13) | Y |  |  |
| 22 | DSC_DCR | VARCHAR2(50) | Y |  |  |
| 23 | DAT_GRAVACAO | DATE | Y |  |  |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | CHAVE_SAFX329 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX329: (CHAVE_SAFX329)
- IX_SAFX329: (DAT_GRAVACAO)
- IX_SAFX329_LOTE: (NUM_LOTE)

---

## SAFX330

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_DCR | VARCHAR2(15) | Y |  |  |
| 4 | DATA_VALID | VARCHAR2(8) | Y |  |  |
| 5 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 6 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 7 | VLR_VENDA_USS | VARCHAR2(17) | Y |  |  |
| 8 | VLR_IMPOST_USS | VARCHAR2(17) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX330 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX330: (CHAVE_SAFX330)
- IX_SAFX330: (DAT_GRAVACAO)
- IX_SAFX330_LOTE: (NUM_LOTE)

---

## SAFX331

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | QTD_PTS_PROG_FIDEL | VARCHAR2(20) | Y |  |  |
| 13 | DAT_AFER_PROG_FIDEL | VARCHAR2(8) | Y |  |  |
| 14 | QTD_REGAT_PROG_FIDEL | VARCHAR2(20) | Y |  |  |
| 15 | DAT_REGAT_PROG_FIDEL | VARCHAR2(8) | Y |  |  |
| 16 | ANO_MES_REFERENCIA_FAT | VARCHAR2(6) | Y |  |  |
| 17 | DAT_VENCTO | VARCHAR2(8) | Y |  |  |
| 18 | COD_BARRAS | VARCHAR2(48) | Y |  |  |
| 19 | COD_DEBITO_AUTO | VARCHAR2(20) | Y |  |  |
| 20 | COD_BANCO_AUTO | VARCHAR2(5) | Y |  |  |
| 21 | COD_AGENCIA_AUTO | VARCHAR2(10) | Y |  |  |
| 22 | COD_QRCODE_PIX | VARCHAR2(2000) | Y |  |  |
| 23 | DATA_CONSUMO_INI | VARCHAR2(8) | Y |  |  |
| 24 | DATA_CONSUMO_FIM | VARCHAR2(8) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |
| 26 | PST_ID | NUMBER | Y |  |  |
| 27 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 28 | CHAVE_SAFX331 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX331: (CHAVE_SAFX331)
- IX_SAFX331: (DAT_GRAVACAO)
- IX_SAFX331_LOTE: (NUM_LOTE)

---

## SAFX332

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | VLR_UNIT_PROC | VARCHAR2(21) | Y |  |  |
| 17 | QTD_FAT_PROC | VARCHAR2(15) | Y |  |  |
| 18 | VLR_ITEM_PROC | VARCHAR2(21) | Y |  |  |
| 19 | VLR_DESC_PROC | VARCHAR2(17) | Y |  |  |
| 20 | VLR_OUT_DESP_PROC | VARCHAR2(17) | Y |  |  |
| 21 | IND_DEV_PROC | VARCHAR2(1) | Y |  |  |
| 22 | VLR_BC_ICMS_PROC | VARCHAR2(17) | Y |  |  |
| 23 | VLR_ALIQ_ICMS_PROC | VARCHAR2(7) | Y |  |  |
| 24 | VLR_ICMS_PROC | VARCHAR2(17) | Y |  |  |
| 25 | VLR_PIS_PROC | VARCHAR2(17) | Y |  |  |
| 26 | VLR_COFINS_PROC | VARCHAR2(17) | Y |  |  |
| 27 | IND_TP_RESSARC | VARCHAR2(2) | Y |  |  |
| 28 | DATA_REF_RESSARC | VARCHAR2(8) | Y |  |  |
| 29 | NUM_PROC_RESSARC | VARCHAR2(60) | Y |  |  |
| 30 | NUM_PROT_RESSARC | VARCHAR2(60) | Y |  |  |
| 31 | DSC_OBS_RESSARC | VARCHAR2(100) | Y |  |  |
| 32 | DSC_ADIC_RESSARC | VARCHAR2(500) | Y |  |  |
| 33 | VLR_FCP_ICMS_PROC | VARCHAR2(17) | Y |  |  |
| 34 | DAT_GRAVACAO | DATE | Y |  |  |
| 35 | PST_ID | NUMBER | Y |  |  |
| 36 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 37 | CHAVE_SAFX332 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX332: (CHAVE_SAFX332)
- IX_SAFX332: (DAT_GRAVACAO)
- IX_SAFX332_LOTE: (NUM_LOTE)

---

## SAFX333

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 17 | VLR_BASE_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 18 | PERC_FCP_DEST | VARCHAR2(5) | Y |  |  |
| 19 | VLR_ALIQ_DESTINO | VARCHAR2(7) | Y |  |  |
| 20 | VLR_FCP_UF_DEST | VARCHAR2(17) | Y |  |  |
| 21 | VLR_TRIB_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 22 | VLR_ICMS_UF_EMIT | VARCHAR2(17) | Y |  |  |
| 23 | COD_BENEF_FISCAL_DEST | VARCHAR2(10) | Y |  |  |
| 24 | DAT_GRAVACAO | DATE | Y |  |  |
| 25 | PST_ID | NUMBER | Y |  |  |
| 26 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 27 | CHAVE_SAFX333 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX333: (CHAVE_SAFX333)
- IX_SAFX333: (DAT_GRAVACAO)
- IX_SAFX333_LOTE: (NUM_LOTE)

---

## SAFX334

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | VLR_PIS_RETIDO | VARCHAR2(23) | Y |  |  |
| 17 | VLR_COFINS_RETIDO | VARCHAR2(23) | Y |  |  |
| 18 | VLR_CSLL_RETIDO | VARCHAR2(23) | Y |  |  |
| 19 | VLR_BC_IRRF | VARCHAR2(23) | Y |  |  |
| 20 | VLR_IRRF_RETIDO | VARCHAR2(23) | Y |  |  |
| 21 | VLR_BC_FUST | VARCHAR2(17) | Y |  |  |
| 22 | VLR_ALIQ_FUST | VARCHAR2(7) | Y |  |  |
| 23 | VLR_FUST | VARCHAR2(17) | Y |  |  |
| 24 | VLR_BC_FUNTTEL | VARCHAR2(17) | Y |  |  |
| 25 | VLR_ALIQ_FUNTTEL | VARCHAR2(7) | Y |  |  |
| 26 | VLR_FUNTTEL | VARCHAR2(17) | Y |  |  |
| 27 | DAT_GRAVACAO | DATE | Y |  |  |
| 28 | PST_ID | NUMBER | Y |  |  |
| 29 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 30 | CHAVE_SAFX334 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX334: (CHAVE_SAFX334)
- IX_SAFX334: (DAT_GRAVACAO)
- IX_SAFX334_LOTE: (NUM_LOTE)

---

## SAFX335

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 15 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 16 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 17 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 18 | VLR_ITEM | VARCHAR2(17) | Y |  |  |
| 19 | COD_SITUACAO_A | VARCHAR2(1) | Y |  |  |
| 20 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 21 | VLR_EST_ITEM | VARCHAR2(17) | Y |  |  |
| 22 | VLR_ALIQ_CRE_OUTORG | VARCHAR2(7) | Y |  |  |
| 23 | VLR_BRUTO_CRE_OUTORG | VARCHAR2(17) | Y |  |  |
| 24 | PRC_ESTORNO | VARCHAR2(7) | Y |  |  |
| 25 | VLR_ESTORNO_OUTORG_ITEM | VARCHAR2(17) | Y |  |  |
| 26 | VLR_LIQUIDO_CRE_OUTORG | VARCHAR2(17) | Y |  |  |
| 27 | OBSERVACAO | VARCHAR2(100) | Y |  |  |
| 28 | DAT_GRAVACAO | DATE | Y |  |  |
| 29 | PST_ID | NUMBER | Y |  |  |
| 30 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 31 | CHAVE_SAFX335 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX335: (CHAVE_SAFX335)
- IX_SAFX335_DAT_GRAVACAO: (DAT_GRAVACAO)
- IX_SAFX335_LOTE: (NUM_LOTE)

---

## SAFX336

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | Y |  |  |
| 4 | COD_OPER_OBRIG | VARCHAR2(10) | Y |  |  |
| 5 | COD_PRODUTO_OBRIG | VARCHAR2(60) | Y |  |  |
| 6 | QTDE_ANP | VARCHAR2(15) | Y |  |  |
| 7 | QTDE_KG | VARCHAR2(15) | Y |  |  |
| 8 | IND_FIS_JUR_TERC | VARCHAR2(1) | Y |  |  |
| 9 | COD_FIS_JUR_TERC | VARCHAR2(14) | Y |  |  |
| 10 | UF_COLETA | VARCHAR2(2) | Y |  |  |
| 11 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 12 | COD_CNAE_OBRIG | VARCHAR2(10) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX336 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX336: (CHAVE_SAFX336)
- IX_SAFX336: (DAT_GRAVACAO)
- IX_SAFX336_LOTE: (NUM_LOTE)

---

## SAFX337

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 4 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 5 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX337 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX337: (CHAVE_SAFX337)
- IX_SAFX337: (DAT_GRAVACAO)
- IX_SAFX337_LOTE: (NUM_LOTE)

---

## SAFX338

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | VARCHAR2(8) | Y |  |  |
| 2 | UF | VARCHAR2(2) | Y |  |  |
| 3 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | Y |  |  |
| 5 | COD_CIDADE_OBRIG | VARCHAR2(8) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX338 | VARCHAR2(4000) | Y | NVL("VALID_INICIAL",'@')\|\|NVL("UF",'@')\|\|NVL("C... |  |

**Indexes**:
- IX_CHAVE_SAFX338: (CHAVE_SAFX338)
- IX_SAFX338: (DAT_GRAVACAO)
- IX_SAFX338_LOTE: (NUM_LOTE)

---

## SAFX339

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | VARCHAR2(8) | Y |  |  |
| 2 | COD_ATIVIDADE | VARCHAR2(7) | Y |  |  |
| 3 | COD_MODULO | VARCHAR2(8) | Y |  |  |
| 4 | COD_CNAE_OBRIG | VARCHAR2(10) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 8 | CHAVE_SAFX339 | VARCHAR2(4000) | Y | NVL("VALID_INICIAL",'@')\|\|NVL("COD_ATIVIDADE",'... |  |

**Indexes**:
- IX_CHAVE_SAFX339: (CHAVE_SAFX339)
- IX_SAFX339: (DAT_GRAVACAO)
- IX_SAFX339_LOTE: (NUM_LOTE)

---

## SAFX34

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 8 | NUM_DOCTO | VARCHAR2(15) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 14 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 15 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 16 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 17 | IND_PRODUTO_INS | CHAR(1) | Y |  |  |
| 18 | COD_PRODUTO_INS | VARCHAR2(60) | Y |  |  |
| 19 | COD_UND_PAD_INS | VARCHAR2(8) | Y |  |  |
| 20 | QTD_MOVTO_INS | VARCHAR2(17) | Y |  |  |
| 21 | CUSTO_UNIT_INS | VARCHAR2(18) | Y |  |  |
| 22 | COD_LEGENDA_INS | VARCHAR2(5) | Y |  |  |
| 23 | DAT_GRAVACAO | DATE | Y |  |  |
| 24 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 25 | NUM_DOCTO_INS | VARCHAR2(15) | Y |  |  |
| 26 | PST_ID | NUMBER | Y |  |  |
| 27 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 28 | CHAVE_SAFX34 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX34: (CHAVE_SAFX34)
- IX_SAFX34: (DAT_GRAVACAO)
- IX_SAFX34_LOTE: (NUM_LOTE)

---

## SAFX340

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VALID_INICIAL | VARCHAR2(8) | Y |  |  |
| 2 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 4 | COD_MODULO | VARCHAR2(8) | Y |  |  |
| 5 | COD_OPER_OBRIG | VARCHAR2(10) | Y |  |  |
| 6 | IND_DESTINACAO | VARCHAR2(1) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX340 | VARCHAR2(4000) | Y | NVL("VALID_INICIAL",'@')\|\|NVL("COD_CFO",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX340: (CHAVE_SAFX340)
- IX_SAFX340: (DAT_GRAVACAO)
- IX_SAFX340_LOTE: (NUM_LOTE)

---

## SAFX341

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INI | VARCHAR2(8) | Y |  |  |
| 4 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 5 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 6 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 7 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 8 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 9 | COD_ITEM_PART_MUN | VARCHAR2(60) | Y |  |  |
| 10 | VLR_AGREG_INF | VARCHAR2(17) | Y |  |  |
| 11 | VLR_DED_INF | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX341 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX341: (CHAVE_SAFX341)
- IX_SAFX341: (DAT_GRAVACAO)
- IX_SAFX341_LOTE: (NUM_LOTE)

---

## SAFX342

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 4 | PERIODO | VARCHAR2(8) | Y |  |  |
| 5 | NUM_GUIA_PAG | VARCHAR2(30) | Y |  |  |
| 6 | DAT_GUIA_PAG | VARCHAR2(8) | Y |  |  |
| 7 | COD_ARRECADACAO | VARCHAR2(20) | Y |  |  |
| 8 | COD_RECEITA | VARCHAR2(20) | Y |  |  |
| 9 | DET_RECEITA | VARCHAR2(20) | Y |  |  |
| 10 | NUM_DOC_ORIGEM | VARCHAR2(20) | Y |  |  |
| 11 | SERIE | VARCHAR2(3) | Y |  |  |
| 12 | UF_FAVORECIDA | VARCHAR2(2) | Y |  |  |
| 13 | CNPJ_FAVORECIDO | VARCHAR2(14) | Y |  |  |
| 14 | IE_FAVORECIDA | VARCHAR2(30) | Y |  |  |
| 15 | VLR_PRINCIPAL | VARCHAR2(17) | Y |  |  |
| 16 | DATA_VENCIMENTO | VARCHAR2(8) | Y |  |  |
| 17 | DATA_PAGAMENTO | VARCHAR2(8) | Y |  |  |
| 18 | VLR_MULTA | VARCHAR2(17) | Y |  |  |
| 19 | VLR_JUROS | VARCHAR2(17) | Y |  |  |
| 20 | INFO_COMPLEMENTAR | VARCHAR2(300) | Y |  |  |
| 21 | VLR_FECP | VARCHAR2(17) | Y |  |  |
| 22 | VLR_FECP_JUROS | VARCHAR2(17) | Y |  |  |
| 23 | VLR_FECP_MULTA | VARCHAR2(17) | Y |  |  |
| 24 | CONVENIO | VARCHAR2(50) | Y |  |  |
| 25 | COD_PRODUTO | VARCHAR2(5) | Y |  |  |
| 26 | CHAVE_DFE | VARCHAR2(44) | Y |  |  |
| 27 | CAD_PART | VARCHAR2(14) | Y |  |  |
| 28 | COD_PARTICIPANTE | VARCHAR2(60) | Y |  |  |
| 29 | DATA_VALID | VARCHAR2(8) | Y |  |  |
| 30 | CNPJ | VARCHAR2(14) | Y |  |  |
| 31 | CPF | VARCHAR2(11) | Y |  |  |
| 32 | ID_ESTRANGEIRO | VARCHAR2(20) | Y |  |  |
| 33 | RAZAO_SOCIAL | VARCHAR2(255) | Y |  |  |
| 34 | NOME_FANTASIA | VARCHAR2(255) | Y |  |  |
| 35 | ENDERECO | VARCHAR2(60) | Y |  |  |
| 36 | NUMERO | VARCHAR2(10) | Y |  |  |
| 37 | COMPLEMENTO | VARCHAR2(60) | Y |  |  |
| 38 | BAIRRO | VARCHAR2(60) | Y |  |  |
| 39 | CEP | VARCHAR2(8) | Y |  |  |
| 40 | COD_MUNICIPIO | VARCHAR2(7) | Y |  |  |
| 41 | UF | VARCHAR2(2) | Y |  |  |
| 42 | COD_PAIS | VARCHAR2(5) | Y |  |  |
| 43 | DDD | VARCHAR2(2) | Y |  |  |
| 44 | TELEFONE | VARCHAR2(9) | Y |  |  |
| 45 | EMAIL | VARCHAR2(60) | Y |  |  |
| 46 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 47 | INSC_MUNICIPAL | VARCHAR2(15) | Y |  |  |
| 48 | SUFRAMA | VARCHAR2(9) | Y |  |  |
| 49 | COD_MUN_FAVORECIDO | VARCHAR2(7) | Y |  |  |
| 50 | VLR_OUTROS | VARCHAR2(17) | Y |  |  |
| 51 | VLR_BASE_CALC | VARCHAR2(17) | Y |  |  |
| 52 | CAMPOS_EXTRAS | VARCHAR2(500) | Y |  |  |
| 53 | GRUPO_IMPOSTO | VARCHAR2(30) | Y |  |  |
| 54 | USUARIO | VARCHAR2(100) | Y |  |  |
| 55 | STATUS | VARCHAR2(30) | Y |  |  |
| 56 | NUM_PROCESSO | VARCHAR2(12) | Y |  |  |
| 57 | DAT_GRAVACAO | DATE | Y |  |  |
| 58 | PST_ID | NUMBER | Y |  |  |
| 59 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 60 | CHAVE_SAFX342 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX342: (CHAVE_SAFX342)
- IX_SAFX342_LOTE: (NUM_LOTE)

---

## SAFX343

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | UF | VARCHAR2(2) | Y |  |  |
| 4 | GRUPO_IMPOSTO | VARCHAR2(10) | Y |  |  |
| 5 | IMPOSTO | VARCHAR2(30) | Y |  |  |
| 6 | REFERENCIA | VARCHAR2(16) | Y |  |  |
| 7 | LOCAL_NEGOCIO | VARCHAR2(4) | Y |  |  |
| 8 | DIVISAO | VARCHAR2(4) | Y |  |  |
| 9 | CENTRO | VARCHAR2(4) | Y |  |  |
| 10 | COD_AJUSTE | VARCHAR2(8) | Y |  |  |
| 11 | DESCRICAO_AJUSTE | VARCHAR2(300) | Y |  |  |
| 12 | CHAVE_LANCTO_D | VARCHAR2(2) | Y |  |  |
| 13 | COD_CONTA_D | VARCHAR2(70) | Y |  |  |
| 14 | DESCRICAO_CONTA_D | VARCHAR2(50) | Y |  |  |
| 15 | IND_SITUACAO_D | VARCHAR2(1) | Y |  |  |
| 16 | IND_NATUREZA_D | VARCHAR2(1) | Y |  |  |
| 17 | CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 18 | DESCRICAO_CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 19 | CENTRO_LUCRO_D | VARCHAR2(25) | Y |  |  |
| 20 | TEXTO_D | VARCHAR2(20) | Y |  |  |
| 21 | OBSERVACAO_D | VARCHAR2(20) | Y |  |  |
| 22 | CHAVE_LANCTO_C | VARCHAR2(2) | Y |  |  |
| 23 | COD_CONTA_C | VARCHAR2(70) | Y |  |  |
| 24 | DESCRICAO_CONTA_C | VARCHAR2(50) | Y |  |  |
| 25 | IND_SITUACAO_C | VARCHAR2(1) | Y |  |  |
| 26 | IND_NATUREZA_C | VARCHAR2(1) | Y |  |  |
| 27 | CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 28 | DESCRICAO_CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 29 | CENTRO_LUCRO_C | VARCHAR2(25) | Y |  |  |
| 30 | TEXTO_C | VARCHAR2(20) | Y |  |  |
| 31 | OBSERVACAO_C | VARCHAR2(20) | Y |  |  |
| 32 | USUARIO | VARCHAR2(100) | Y |  |  |
| 33 | DATA_PARAMETRO | VARCHAR2(8) | Y |  |  |
| 34 | DAT_GRAVACAO | DATE | Y |  |  |
| 35 | PST_ID | NUMBER | Y |  |  |
| 36 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 37 | CHAVE_SAFX343 | VARCHAR2(57) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX343: (CHAVE_SAFX343)
- IX_SAFX343: (DAT_GRAVACAO)
- IX_SAFX343_LOTE: (NUM_LOTE)

---

## SAFX344

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | UF | VARCHAR2(2) | Y |  |  |
| 4 | REFERENCIA | VARCHAR2(16) | Y |  |  |
| 5 | GRUPO_IMPOSTO | VARCHAR2(10) | Y |  |  |
| 6 | IMPOSTO | VARCHAR2(30) | Y |  |  |
| 7 | LOCAL_NEGOCIO | VARCHAR2(4) | Y |  |  |
| 8 | DIVISAO | VARCHAR2(4) | Y |  |  |
| 9 | CENTRO | VARCHAR2(4) | Y |  |  |
| 10 | COD_TIPO_LIVRO | VARCHAR2(3) | Y |  |  |
| 11 | OUTROS_LANCAMENTOS_CONTABEIS | VARCHAR2(50) | Y |  |  |
| 12 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 13 | COD_OPER_APUR | VARCHAR2(5) | Y |  |  |
| 14 | CHAVE_LANCTO_D | VARCHAR2(2) | Y |  |  |
| 15 | COD_CONTA_D | VARCHAR2(70) | Y |  |  |
| 16 | DESCRICAO_CONTA_D | VARCHAR2(50) | Y |  |  |
| 17 | IND_SITUACAO_D | VARCHAR2(1) | Y |  |  |
| 18 | IND_NATUREZA_D | VARCHAR2(1) | Y |  |  |
| 19 | CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 20 | CENTRO_LUCRO_D | VARCHAR2(25) | Y |  |  |
| 21 | TEXTO_D | VARCHAR2(20) | Y |  |  |
| 22 | OBSERVACAO_D | VARCHAR2(20) | Y |  |  |
| 23 | CHAVE_LANCTO_C | VARCHAR2(2) | Y |  |  |
| 24 | COD_CONTA_C | VARCHAR2(70) | Y |  |  |
| 25 | DESCRICAO_CONTA_C | VARCHAR2(50) | Y |  |  |
| 26 | IND_SITUACAO_C | VARCHAR2(1) | Y |  |  |
| 27 | IND_NATUREZA_C | VARCHAR2(1) | Y |  |  |
| 28 | CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 29 | CENTRO_LUCRO_C | VARCHAR2(25) | Y |  |  |
| 30 | TEXTO_C | VARCHAR2(20) | Y |  |  |
| 31 | OBSERVACAO_C | VARCHAR2(20) | Y |  |  |
| 32 | USUARIO | VARCHAR2(100) | Y |  |  |
| 33 | DATA_PARAMETRO | VARCHAR2(8) | Y |  |  |
| 34 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 35 | PST_ID | NUMBER | Y |  |  |
| 36 | DAT_GRAVACAO | DATE | Y |  |  |
| 37 | CHAVE_SAFX344 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX344: (CHAVE_SAFX344)
- IX_SAFX344: (DAT_GRAVACAO)
- IX_SAFX344_LOTE: (NUM_LOTE)

---

## SAFX345

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | CHAVE_ID | VARCHAR2(50) | Y |  |  |
| 4 | GRUPO_IMPOSTO | VARCHAR2(10) | Y |  |  |
| 5 | IMPOSTO | VARCHAR2(30) | Y |  |  |
| 6 | UF | VARCHAR2(2) | Y |  |  |
| 7 | PERIODO | VARCHAR2(2) | Y |  |  |
| 8 | EXERCICIO | VARCHAR2(4) | Y |  |  |
| 9 | REFERENCIA | VARCHAR2(16) | Y |  |  |
| 10 | LOCAL_NEGOCIO | VARCHAR2(4) | Y |  |  |
| 11 | DIVISAO | VARCHAR2(4) | Y |  |  |
| 12 | CENTRO | VARCHAR2(4) | Y |  |  |
| 13 | COD_AJUSTE | VARCHAR2(8) | Y |  |  |
| 14 | DESCRICAO_AJUSTE | VARCHAR2(300) | Y |  |  |
| 15 | CHAVE_LANCTO_D | VARCHAR2(9) | Y |  |  |
| 16 | COD_CONTA_D | VARCHAR2(70) | Y |  |  |
| 17 | DESCRICAO_CONTA_D | VARCHAR2(50) | Y |  |  |
| 18 | MONTANTE_D | VARCHAR2(19) | Y |  |  |
| 19 | CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 20 | DESCRICAO_CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 21 | CENTRO_LUCRO_D | VARCHAR2(25) | Y |  |  |
| 22 | TEXTO_D | VARCHAR2(20) | Y |  |  |
| 23 | OBSERVACAO_D | VARCHAR2(20) | Y |  |  |
| 24 | CHAVE_LANCTO_C | VARCHAR2(9) | Y |  |  |
| 25 | COD_CONTA_C | VARCHAR2(70) | Y |  |  |
| 26 | DESCRICAO_CONTA_C | VARCHAR2(50) | Y |  |  |
| 27 | MONTANTE_C | VARCHAR2(19) | Y |  |  |
| 28 | CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 29 | DESCRICAO_CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 30 | CENTRO_LUCRO_C | VARCHAR2(25) | Y |  |  |
| 31 | TEXTO_C | VARCHAR2(20) | Y |  |  |
| 32 | OBSERVACAO_C | VARCHAR2(20) | Y |  |  |
| 33 | USUARIO | VARCHAR2(100) | Y |  |  |
| 34 | CNPJ | VARCHAR2(14) | Y |  |  |
| 35 | DT_DOCTO | VARCHAR2(8) | Y |  |  |
| 36 | DT_LANCTO | VARCHAR2(8) | Y |  |  |
| 37 | DAT_GRAVACAO | DATE | Y |  |  |
| 38 | PST_ID | NUMBER | Y |  |  |
| 39 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 40 | CHAVE_SAFX345 | VARCHAR2(65) | Y | NVL("GRUPO_IMPOSTO",'@')\|\|NVL("IMPOSTO",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX345: (CHAVE_SAFX345)
- IX_SAFX345: (DAT_GRAVACAO)
- IX_SAFX345_LOTE: (NUM_LOTE)

---

## SAFX346

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(8) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | PERIODO | VARCHAR2(8) | Y |  |  |
| 4 | ID_GUIA | VARCHAR2(38) | Y |  |  |
| 5 | ID_TITULO | VARCHAR2(38) | Y |  |  |
| 6 | CNPJ_EMPRESA | VARCHAR2(14) | Y |  |  |
| 7 | INSC_SUBSTITUTA | VARCHAR2(30) | Y |  |  |
| 8 | TIPO_INSC_SUBSTITUTA | VARCHAR2(300) | Y |  |  |
| 9 | TIPO_PAGTO | VARCHAR2(4000) | Y |  |  |
| 10 | COD_RECEITA | VARCHAR2(20) | Y |  |  |
| 11 | DET_RECEITA | VARCHAR2(20) | Y |  |  |
| 12 | GRUPO_IMPOSTO | VARCHAR2(30) | Y |  |  |
| 13 | UF_FAVORECIDA | VARCHAR2(2) | Y |  |  |
| 14 | COD_DOC | VARCHAR2(38) | Y |  |  |
| 15 | NUM_DOC_ORIGEM | VARCHAR2(20) | Y |  |  |
| 16 | SERIE | VARCHAR2(3) | Y |  |  |
| 17 | CHAVE_NF | VARCHAR2(44) | Y |  |  |
| 18 | IND_CANCELAMENTO | VARCHAR2(1) | Y |  |  |
| 19 | INFO_CANCELAMENTO | VARCHAR2(4000) | Y |  |  |
| 20 | STATUS | VARCHAR2(38) | Y |  |  |
| 21 | DSC_STATUS | VARCHAR2(4000) | Y |  |  |
| 22 | VLR_PRINCIPAL | VARCHAR2(19) | Y |  |  |
| 23 | VLR_FECP | VARCHAR2(19) | Y |  |  |
| 24 | VLR_JUROS | VARCHAR2(19) | Y |  |  |
| 25 | VLR_MULTA | VARCHAR2(19) | Y |  |  |
| 26 | VLR_ATUAL_MONETARIA | VARCHAR2(19) | Y |  |  |
| 27 | VLR_OUTROS | VARCHAR2(19) | Y |  |  |
| 28 | VLR_FECP_JUROS | VARCHAR2(19) | Y |  |  |
| 29 | VLR_MULTA_FECP | VARCHAR2(19) | Y |  |  |
| 30 | VLR_TOTAL | VARCHAR2(19) | Y |  |  |
| 31 | COD_PRODUTO | VARCHAR2(5) | Y |  |  |
| 32 | CONVENIO | VARCHAR2(50) | Y |  |  |
| 33 | CNPJ_FAVORECIDO | VARCHAR2(14) | Y |  |  |
| 34 | INSC_ESTADUAL_FAVORECIDO | VARCHAR2(30) | Y |  |  |
| 35 | CPF_FAVORECIDO | VARCHAR2(14) | Y |  |  |
| 36 | INFO_COMPL_DOCUMENTO | VARCHAR2(4000) | Y |  |  |
| 37 | IND_ERRO | VARCHAR2(1) | Y |  |  |
| 38 | MENSAGEM_ERRO | VARCHAR2(4000) | Y |  |  |
| 39 | DATA_VENCTO | VARCHAR2(8) | Y |  |  |
| 40 | DATA_VENCTO_ORIGINAL | VARCHAR2(8) | Y |  |  |
| 41 | COD_BARRAS | VARCHAR2(4000) | Y |  |  |
| 42 | NUM_CONTROLE | VARCHAR2(4000) | Y |  |  |
| 43 | DATA_SEFAZ | VARCHAR2(8) | Y |  |  |
| 44 | ID_PAGTO | VARCHAR2(38) | Y |  |  |
| 45 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 46 | NUM_AUTENTICACAO | VARCHAR2(4000) | Y |  |  |
| 47 | ID_PAGADOR | VARCHAR2(38) | Y |  |  |
| 48 | CNPJ_PAGADOR | VARCHAR2(14) | Y |  |  |
| 49 | COD_BANCO | VARCHAR2(3) | Y |  |  |
| 50 | AGENCIA | VARCHAR2(5) | Y |  |  |
| 51 | DIG_AGENCIA | VARCHAR2(2) | Y |  |  |
| 52 | CONTA_CORRENTE | VARCHAR2(15) | Y |  |  |
| 53 | DIG_CONTA_CORRENTE | VARCHAR2(2) | Y |  |  |
| 54 | REGRA_PAGAMENTO | VARCHAR2(4000) | Y |  |  |
| 55 | PDF_GUIA | VARCHAR2(4000) | Y |  |  |
| 56 | CAMPO_EXTRA | VARCHAR2(4000) | Y |  |  |
| 57 | QR_CODE_PIX | VARCHAR2(4000) | Y |  |  |
| 58 | LOGIN_USUARIO | VARCHAR2(4000) | Y |  |  |
| 59 | DAT_DEBITO | VARCHAR2(8) | Y |  |  |
| 60 | TOTAL_ELEMENTOS | VARCHAR2(38) | Y |  |  |
| 61 | TOTAL_PAGINAS | VARCHAR2(38) | Y |  |  |
| 62 | TAMANHO | VARCHAR2(38) | Y |  |  |
| 63 | NUMERO | VARCHAR2(38) | Y |  |  |
| 64 | NUMERO_ELEMENTOS | VARCHAR2(38) | Y |  |  |
| 65 | ULTIMO | VARCHAR2(38) | Y |  |  |
| 66 | PRIMEIRO | VARCHAR2(38) | Y |  |  |
| 67 | ORDENACAO | VARCHAR2(38) | Y |  |  |
| 68 | DAT_GRAVACAO | DATE | Y |  |  |
| 69 | PST_ID | NUMBER | Y |  |  |
| 70 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 71 | CHAVE_SAFX346 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX346: (CHAVE_SAFX346)
- IX_SAFX346_LOTE: (NUM_LOTE)

---

## SAFX347

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | CHAVE_ID | VARCHAR2(50) | Y |  |  |
| 4 | PERIODO | VARCHAR2(2) | Y |  |  |
| 5 | EXERCICIO | VARCHAR2(4) | Y |  |  |
| 6 | DT_DOCTO | VARCHAR2(8) | Y |  |  |
| 7 | DT_LANCTO | VARCHAR2(8) | Y |  |  |
| 8 | UF | VARCHAR2(2) | Y |  |  |
| 9 | REFERENCIA | VARCHAR2(16) | Y |  |  |
| 10 | LOCAL_NEGOCIO | VARCHAR2(4) | Y |  |  |
| 11 | DIVISAO | VARCHAR2(4) | Y |  |  |
| 12 | CENTRO | VARCHAR2(4) | Y |  |  |
| 13 | GRUPO_IMPOSTO | VARCHAR2(10) | Y |  |  |
| 14 | IMPOSTO | VARCHAR2(20) | Y |  |  |
| 15 | COD_AJUSTE | VARCHAR2(15) | Y |  |  |
| 16 | DESCRICAO_AJUSTE | VARCHAR2(50) | Y |  |  |
| 17 | CHAVE_LANCTO_D | VARCHAR2(2) | Y |  |  |
| 18 | COD_CONTA_D | VARCHAR2(70) | Y |  |  |
| 19 | DESCRICAO_CONTA_D | VARCHAR2(50) | Y |  |  |
| 20 | MONTANTE_D | VARCHAR2(17) | Y |  |  |
| 21 | CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 22 | DESCRICAO_CENTRO_CUSTO_D | VARCHAR2(50) | Y |  |  |
| 23 | CENTRO_LUCRO_D | VARCHAR2(20) | Y |  |  |
| 24 | TEXTO_D | VARCHAR2(20) | Y |  |  |
| 25 | OBSERVACAO_D | VARCHAR2(20) | Y |  |  |
| 26 | CHAVE_LANCTO_C | VARCHAR2(2) | Y |  |  |
| 27 | COD_CONTA_C | VARCHAR2(70) | Y |  |  |
| 28 | DESCRICAO_CONTA_C | VARCHAR2(50) | Y |  |  |
| 29 | MONTANTE_C | VARCHAR2(17) | Y |  |  |
| 30 | CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 31 | DESCRICAO_CENTRO_CUSTO_C | VARCHAR2(50) | Y |  |  |
| 32 | CENTRO_LUCRO_C | VARCHAR2(20) | Y |  |  |
| 33 | TEXTO_C | VARCHAR2(20) | Y |  |  |
| 34 | OBSERVACAO_C | VARCHAR2(20) | Y |  |  |
| 35 | USUARIO | VARCHAR2(100) | Y |  |  |
| 36 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 37 | PST_ID | NUMBER | Y |  |  |
| 38 | DAT_GRAVACAO | DATE | Y |  |  |
| 39 | NRO_DOC_CONTABIL | VARCHAR2(10) | Y |  |  |
| 40 | CHAVE_SAFX347 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX347: (CHAVE_SAFX347)
- IX_SAFX347: (DAT_GRAVACAO)
- IX_SAFX347_LOTE: (NUM_LOTE)

---

## SAFX35

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 10 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 11 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 12 | TIPO_DESTINACAO | VARCHAR2(2) | Y |  |  |
| 13 | COD_PRAZO | VARCHAR2(3) | Y |  |  |
| 14 | COD_UNID_NEGOC | VARCHAR2(20) | Y |  |  |
| 15 | COD_FISJUR_TRANSP | VARCHAR2(14) | Y |  |  |
| 16 | IND_FISJUR_TRANSP | CHAR(1) | Y |  |  |
| 17 | COD_VIA_TRANSPORTE | VARCHAR2(5) | Y |  |  |
| 18 | IND_EMITE_DEST | CHAR(1) | Y |  |  |
| 19 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 20 | DATA_REC_SAIDA | VARCHAR2(8) | Y |  |  |
| 21 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 22 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 23 | VLR_OUTROS | VARCHAR2(17) | Y |  |  |
| 24 | TEXTO_LIVRE | VARCHAR2(300) | Y |  |  |
| 25 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 26 | VLR_INDICE | VARCHAR2(17) | Y |  |  |
| 27 | PESO_LIQUIDO | VARCHAR2(13) | Y |  |  |
| 28 | PESO_BRUTO | VARCHAR2(13) | Y |  |  |
| 29 | VOLUME | VARCHAR2(13) | Y |  |  |
| 30 | DAT_PREV_FAT | VARCHAR2(8) | Y |  |  |
| 31 | IND_FISJUR_ENTREGA | CHAR(1) | Y |  |  |
| 32 | COD_FISJUR_ENTREGA | VARCHAR2(14) | Y |  |  |
| 33 | DAT_GRAVACAO | DATE | Y |  |  |
| 34 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 35 | IND_EMIT_TRANSP | CHAR(1) | Y |  |  |
| 36 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 37 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 38 | DATA_DI | VARCHAR2(8) | Y |  |  |
| 39 | NUM_NOTIF_ZFM | VARCHAR2(12) | Y |  |  |
| 40 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 41 | DATA_APROVACAO | VARCHAR2(8) | Y |  |  |
| 42 | IND_FATURA | CHAR(1) | Y |  |  |
| 43 | PST_ID | NUMBER | Y |  |  |
| 44 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 45 | CHAVE_SAFX35 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX35: (CHAVE_SAFX35)
- IX_SAFX35: (DAT_GRAVACAO)
- IX_SAFX35_LOTE: (NUM_LOTE)

---

## SAFX36

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 11 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 14 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 15 | TIPO_DESTINACAO | VARCHAR2(2) | Y |  |  |
| 16 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 17 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 18 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 19 | PERC_DESCONTO | VARCHAR2(7) | Y |  |  |
| 20 | COD_PROJETO | VARCHAR2(10) | Y |  |  |
| 21 | VLR_PRECO_SUGER | VARCHAR2(17) | Y |  |  |
| 22 | VLR_CUSTO_MEDIO | VARCHAR2(17) | Y |  |  |
| 23 | VLR_ULT_ENTRADA | VARCHAR2(17) | Y |  |  |
| 24 | VLR_TOT_ITEM | VARCHAR2(17) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |
| 26 | DSC_ITEM | VARCHAR2(300) | Y |  |  |
| 27 | IND_ITEM_CAD | CHAR(1) | Y |  |  |
| 28 | QTD_ATENDIDA | VARCHAR2(17) | Y |  |  |
| 29 | QTD_ATENDER | VARCHAR2(17) | Y |  |  |
| 30 | VLR_UNIT_ATEND | VARCHAR2(17) | Y |  |  |
| 31 | VLR_DESCONTO_ATEND | VARCHAR2(17) | Y |  |  |
| 32 | VLR_TOT_ITEM_ATEND | VARCHAR2(17) | Y |  |  |
| 33 | VLR_PRECO_SUGER_AT | VARCHAR2(17) | Y |  |  |
| 34 | VLR_CUSTO_MEDIO_AT | VARCHAR2(17) | Y |  |  |
| 35 | VLR_ULT_ENTRADA_AT | VARCHAR2(17) | Y |  |  |
| 36 | ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 37 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 38 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 39 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 40 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 41 | COD_AMPARO | VARCHAR2(10) | Y |  |  |
| 42 | COD_AMPAROST | VARCHAR2(10) | Y |  |  |
| 43 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 44 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 45 | IND_MOV_FIS | CHAR(1) | Y |  |  |
| 46 | PST_ID | NUMBER | Y |  |  |
| 47 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 48 | CHAVE_SAFX36 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX36: (CHAVE_SAFX36)
- IX_SAFX36: (DAT_GRAVACAO)
- IX_SAFX36_LOTE: (NUM_LOTE)

---

## SAFX37

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 2 | DSC_CANAL_DISTRIB | VARCHAR2(100) | Y |  |  |
| 3 | CEI | VARCHAR2(12) | Y |  |  |
| 4 | DATA_ABERTURA | VARCHAR2(8) | Y |  |  |
| 5 | DATA_ENCERRAMENTO | VARCHAR2(8) | Y |  |  |
| 6 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | NATUREZA_OBRA | VARCHAR2(100) | Y |  |  |
| 9 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 10 | CEP | VARCHAR2(8) | Y |  |  |
| 11 | NUM_IMOVEL | VARCHAR2(10) | Y |  |  |
| 12 | NUM_COMPL | VARCHAR2(45) | Y |  |  |
| 13 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 14 | DATA_CONTRATACAO | VARCHAR2(8) | Y |  |  |
| 15 | REG_CARTORIO | VARCHAR2(100) | Y |  |  |
| 16 | VLR_TOT_OBRA | VARCHAR2(17) | Y |  |  |
| 17 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 18 | COD_ART | VARCHAR2(15) | Y |  |  |
| 19 | ENDERECO | VARCHAR2(100) | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX37 | VARCHAR2(4000) | Y | NVL("COD_CANAL_DISTRIB",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX37: (CHAVE_SAFX37)
- IX_SAFX37_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX37_LOTE: (NUM_LOTE)

---

## SAFX38

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 2 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 3 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 4 | DATA_X38 | VARCHAR2(8) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX38 | VARCHAR2(4000) | Y | NVL("IND_FIS_JUR",'@')\|\|NVL("COD_FIS_JUR",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX38: (CHAVE_SAFX38)
- IX_SAFX38_LOTE: (NUM_LOTE)

---

## SAFX39

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 3 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 4 | DATA_VALID_INI | VARCHAR2(8) | Y |  |  |
| 5 | IND_TIPO_RELAC | CHAR(1) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 8 | DATA_VALID_FIM | VARCHAR2(8) | Y |  |  |
| 9 | IND_TIPO_RELAC_SPED | VARCHAR2(2) | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX39 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("IND_FIS_JUR",'@')\|... |  |

**Indexes**:
- IX_CHAVE_SAFX39: (CHAVE_SAFX39)
- IX_SAFX39: (DAT_GRAVACAO)
- IX_SAFX39_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX39_LOTE: (NUM_LOTE)

---

## SAFX40

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_COMPANHIA | VARCHAR2(10) | Y |  |  |
| 4 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 5 | CONTA_DEB_CRED | VARCHAR2(70) | Y |  |  |
| 6 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 7 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 8 | VLR_LANCTO | VARCHAR2(17) | Y |  |  |
| 9 | CONTRA_PART | VARCHAR2(70) | Y |  |  |
| 10 | CENTRO_CUSTO | VARCHAR2(50) | Y |  |  |
| 11 | CENTRO_DESPESA | VARCHAR2(20) | Y |  |  |
| 12 | HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 13 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 14 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 15 | COD_INDICE_CONV | VARCHAR2(10) | Y |  |  |
| 16 | VLR_OPER_IND | VARCHAR2(18) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX40 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX40: (CHAVE_SAFX40)
- IX_SAFX40: (DAT_GRAVACAO)
- IX_SAFX40_LOTE: (NUM_LOTE)

---

## SAFX41

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_COMPANHIA | VARCHAR2(10) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | DATA_SALDO | VARCHAR2(8) | Y |  |  |
| 6 | VLR_SALDO_INI | VARCHAR2(17) | Y |  |  |
| 7 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 8 | VLR_SALDO_FIM | VARCHAR2(17) | Y |  |  |
| 9 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 10 | VLR_TOT_CRE | VARCHAR2(17) | Y |  |  |
| 11 | VLR_TOT_DEB | VARCHAR2(17) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX41 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX41: (CHAVE_SAFX41)
- IX_SAFX41: (DAT_GRAVACAO)
- IX_SAFX41_LOTE: (NUM_LOTE)

---

## SAFX42

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | IND_TP_REGISTRO | CHAR(1) | Y |  |  |
| 10 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 11 | DAT_SAIDA | VARCHAR2(8) | Y |  |  |
| 12 | COD_CLASSE_USU | VARCHAR2(3) | Y |  |  |
| 13 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 14 | IND_TP_RECEITA | CHAR(1) | Y |  |  |
| 15 | TEL_CLIENTE | VARCHAR2(15) | Y |  |  |
| 16 | VLR_SERVICO | VARCHAR2(17) | Y |  |  |
| 17 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 18 | VLR_OUTRAS_DESP | VARCHAR2(17) | Y |  |  |
| 19 | VLR_ABAT_DEDUCAO | VARCHAR2(17) | Y |  |  |
| 20 | VLR_TOT_PAGAR | VARCHAR2(17) | Y |  |  |
| 21 | SITUACAO | CHAR(1) | Y |  |  |
| 22 | VLR_BASE_ICMS_1 | VARCHAR2(17) | Y |  |  |
| 23 | VLR_BASE_ICMS_2 | VARCHAR2(17) | Y |  |  |
| 24 | VLR_BASE_ICMS_3 | VARCHAR2(17) | Y |  |  |
| 25 | VLR_BASE_ICMS_4 | VARCHAR2(17) | Y |  |  |
| 26 | VLR_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 27 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 28 | VLR_BASE_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 29 | VLR_TRIB_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 30 | VLR_ALIQ_ICMS_DEST | VARCHAR2(7) | Y |  |  |
| 31 | TEL_USU | VARCHAR2(15) | Y |  |  |
| 32 | DAT_VENCTO | VARCHAR2(8) | Y |  |  |
| 33 | MES_REFERENCIA | VARCHAR2(2) | Y |  |  |
| 34 | ANO_REFERENCIA | VARCHAR2(4) | Y |  |  |
| 35 | COD_LOCALIDADE | VARCHAR2(10) | Y |  |  |
| 36 | COD_ESTADO_DEST | VARCHAR2(2) | Y |  |  |
| 37 | COND_PARTICIPANTE | VARCHAR2(2) | Y |  |  |
| 38 | COD_PARTICIPANTE | VARCHAR2(2) | Y |  |  |
| 39 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 40 | COD_OP_TELECOM | VARCHAR2(2) | Y |  |  |
| 41 | COD_USU_FINAL | VARCHAR2(10) | Y |  |  |
| 42 | COD_BARRAS | VARCHAR2(48) | Y |  |  |
| 43 | NUM_CICLO | VARCHAR2(7) | Y |  |  |
| 44 | VLR_SUBST_TRIB | VARCHAR2(17) | Y |  |  |
| 45 | VLR_BASE_SUB_TRIB | VARCHAR2(17) | Y |  |  |
| 46 | OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 47 | DAT_GRAVACAO | DATE | Y |  |  |
| 48 | VLR_DESC_COND | VARCHAR2(17) | Y |  |  |
| 49 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |
| 50 | COD_TP_UTIL | VARCHAR2(2) | Y |  |  |
| 51 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 52 | BASE_ISEN_ISS | VARCHAR2(17) | Y |  |  |
| 53 | BASE_REAL_TERC_ISS | VARCHAR2(17) | Y |  |  |
| 54 | COD_MUNIC_ISS | VARCHAR2(7) | Y |  |  |
| 55 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 56 | DAT_FATO_GERADOR | VARCHAR2(8) | Y |  |  |
| 57 | DAT_CANCELAMENTO | VARCHAR2(8) | Y |  |  |
| 58 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 59 | GRUPO_TENSAO | VARCHAR2(2) | Y |  |  |
| 60 | CONTA_CONSUMO | VARCHAR2(10) | Y |  |  |
| 61 | UF_TEL_CLIENTE | VARCHAR2(2) | Y |  |  |
| 62 | IND_CONVENIO_115 | CHAR(1) | Y |  |  |
| 63 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 64 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  |  |
| 65 | COD_CLASSE_CONSUMO | VARCHAR2(2) | Y |  |  |
| 66 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 67 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 68 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 69 | NUM_CONTRATO | VARCHAR2(20) | Y |  |  |
| 70 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  |  |
| 71 | DATA_CONSUMO_INI | VARCHAR2(8) | Y |  |  |
| 72 | DATA_CONSUMO_FIM | VARCHAR2(8) | Y |  |  |
| 73 | DATA_CONSUMO_LEIT | VARCHAR2(8) | Y |  |  |
| 74 | QTD_CONTRATADA_PONTA | VARCHAR2(17) | Y |  |  |
| 75 | QTD_CONTRATADA_FPONTA | VARCHAR2(17) | Y |  |  |
| 76 | QTD_CONSUMO_TOTAL | VARCHAR2(17) | Y |  |  |
| 77 | UF_CONSUMO | VARCHAR2(2) | Y |  |  |
| 78 | COD_MUNIC_CONSUMO | VARCHAR2(5) | Y |  |  |
| 79 | VLR_TERCEIROS | VARCHAR2(17) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 80 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 81 | NUM_NFCEE_SUBST | VARCHAR2(12) | Y |  | Campo com as mesmas características do Número da Nota Fiscal, receberá informação do número do Documento Fiscal que Substituiu o Documento emitido de forma errônea. |
| 82 | SERIE_NFCEE_SUBST | VARCHAR2(3) | Y |  | Campo com as mesmas características da Série da Nota Fiscal, receberá informação do número da Série que Substituiu o Documento emitido de forma errônea. |
| 83 | HIPOTESE_ESTORNO | VARCHAR2(1) | Y |  | (1)Erro ocorrido no faturamento do Produto ou na emissão do Documento Fiscal, (2)Erro na Medição, Faturamento ou tarifação do produto., (3)Formalização de discordância do consumidor, (4)Cobrança em Duplicidade |
| 84 | MOTIVO_ESTORNO | VARCHAR2(200) | Y |  | Campo de texto Livre que irá detalhar a hipótese de estorno do Documento Fiscal. |
| 85 | IND_NF_REG_ESP | CHAR(1) | Y |  |  |
| 86 | IND_NF_ESP | CHAR(1) | Y |  |  |
| 87 | IND_CONS_FINAL | CHAR(1) | Y |  | Campo identificador de consumidor final(S/N) |
| 88 | NUM_MEDIDOR | VARCHAR2(12) | Y |  |  |
| 89 | COD_CLASSE_CONSUMO_SEF_PE | VARCHAR2(2) | Y |  |  |
| 90 | DSC_AUTOR_ACAO | VARCHAR2(70) | Y |  |  |
| 91 | NUM_PROC_ACAO | VARCHAR2(24) | Y |  |  |
| 92 | NUM_VARA_ACAO | VARCHAR2(2) | Y |  |  |
| 93 | DAT_ACAO | VARCHAR2(8) | Y |  |  |
| 94 | VLR_DEPOSITO | VARCHAR2(17) | Y |  |  |
| 95 | DAT_DEPOSITO | VARCHAR2(8) | Y |  |  |
| 96 | COD_BANCO | VARCHAR2(3) | Y |  |  |
| 97 | NUM_AGENCIA_ACAO | VARCHAR2(6) | Y |  |  |
| 98 | NUM_CONTA_ACAO | VARCHAR2(18) | Y |  |  |
| 99 | NUM_LANCTO_CONTABIL | VARCHAR2(40) | Y |  |  |
| 100 | NUM_DOCFIS_RESSARC | VARCHAR2(12) | Y |  |  |
| 101 | SERIE_DOCFIS_RESSARC | VARCHAR2(3) | Y |  |  |
| 102 | COD_MODELO_RESSARC | VARCHAR2(2) | Y |  |  |
| 103 | DAT_EMISSAO_RESSARC | VARCHAR2(8) | Y |  |  |
| 104 | IDENTIF_DOCFIS_UT | VARCHAR2(128) | Y |  |  |
| 105 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 106 | DAT_EMIS_NFCEE_SUBST | VARCHAR2(8) | Y |  |  |
| 107 | DAT_VENCTO_NFCEE_SUBST | VARCHAR2(8) | Y |  |  |
| 108 | VLR_TOT_NFCEE_SUBST | VARCHAR2(17) | Y |  |  |
| 109 | VLR_BASE_NFCEE_SUBST | VARCHAR2(17) | Y |  |  |
| 110 | VLR_ICMS_NFCEE_SUBST | VARCHAR2(17) | Y |  |  |
| 111 | NUM_ITEM_RESSARC | VARCHAR2(3) | Y |  |  |
| 112 | QTD_ENERGIA_INJ | VARCHAR2(17) | Y |  |  |
| 113 | VLR_ENERGIA_INJ | VARCHAR2(17) | Y |  |  |
| 114 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 115 | COD_TP_CLIENTE | VARCHAR2(2) | Y |  |  |
| 116 | COD_SUBCLASSE_CONSUMO | VARCHAR2(2) | Y |  |  |
| 117 | NUM_TERMINAL_TEL | VARCHAR2(15) | Y |  |  |
| 118 | NUM_FAT_COM | VARCHAR2(20) | Y |  |  |
| 119 | VLR_TOTAL_FAT | VARCHAR2(17) | Y |  |  |
| 120 | DAT_CONS_ANT_LEIT | VARCHAR2(8) | Y |  |  |
| 121 | NUM_DOCFIS_SUBST | VARCHAR2(12) | Y |  |  |
| 122 | SERIE_DOCFIS_SUBST | VARCHAR2(3) | Y |  |  |
| 123 | COD_MODELO_SUBST | VARCHAR2(2) | Y |  |  |
| 124 | DAT_EMIS_SUBST | VARCHAR2(8) | Y |  |  |
| 125 | PERIOD_APUR_SUBST | VARCHAR2(6) | Y |  |  |
| 126 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 127 | DAT_EMISSAO_NFE | VARCHAR2(8) | Y |  |  |
| 128 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 129 | IND_FIN_EMISSAO_NFE | VARCHAR2(1) | Y |  |  |
| 130 | NUM_AUTENTIC_NFE_SUBST | VARCHAR2(80) | Y |  |  |
| 131 | PST_ID | NUMBER | Y |  |  |
| 132 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 133 | COD_AUTENTIC_NFE_SUBST | VARCHAR2(32) | Y |  |  |
| 134 | VLR_OUTRAS_DED | VARCHAR2(17) | Y |  |  |
| 135 | IND_TP_FAT_NFE | VARCHAR2(1) | Y |  |  |
| 136 | IND_TP_AMB_NFE | VARCHAR2(1) | Y |  |  |
| 137 | COD_NF_NFE | VARCHAR2(7) | Y |  |  |
| 138 | COD_DV_NFE | VARCHAR2(1) | Y |  |  |
| 139 | IND_PRE_PAGO | VARCHAR2(1) | Y |  |  |
| 140 | IND_SESSAO_REDE | VARCHAR2(1) | Y |  |  |
| 141 | DAT_INI_CONTRATO | VARCHAR2(8) | Y |  |  |
| 142 | DAT_FIM_CONTRATO | VARCHAR2(8) | Y |  |  |
| 143 | UF_TERMINAL_TEL | VARCHAR2(2) | Y |  |  |
| 144 | COD_MOTIVO_SUBST | VARCHAR2(2) | Y |  |  |
| 145 | VLR_ICMS_DESONERADO | VARCHAR2(17) | Y |  |  |
| 146 | VLR_FCP | VARCHAR2(17) | Y |  |  |
| 147 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 148 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 149 | VLR_FUNTTEL | VARCHAR2(17) | Y |  |  |
| 150 | VLR_FUST | VARCHAR2(17) | Y |  |  |
| 151 | VLR_PIS_RETIDO | VARCHAR2(17) | Y |  |  |
| 152 | VLR_COFINS_RETIDO | VARCHAR2(17) | Y |  |  |
| 153 | VLR_CSLL_RETIDO | VARCHAR2(17) | Y |  |  |
| 154 | VLR_IRRF_RETIDO | VARCHAR2(17) | Y |  |  |
| 155 | QTD_PTS_PROG_FIDEL | VARCHAR2(20) | Y |  |  |
| 156 | DAT_AFER_PROG_FIDEL | VARCHAR2(8) | Y |  |  |
| 157 | QTD_REGAT_PROG_FIDEL | VARCHAR2(20) | Y |  |  |
| 158 | DAT_REGAT_PROG_FIDEL | VARCHAR2(8) | Y |  |  |
| 159 | COD_QRCODE_PIX | VARCHAR2(2000) | Y |  |  |
| 160 | CNPJ_EMIT_FATURAMENTO | VARCHAR2(14) | Y |  |  |
| 161 | UF_EMIT_FATURAMENTO | VARCHAR2(2) | Y |  |  |
| 162 | CNPJ_DOWNLOAD | VARCHAR2(14) | Y |  |  |
| 163 | CPF_DOWNLOAD | VARCHAR2(11) | Y |  |  |
| 164 | COD_DEBITO_AUTO | VARCHAR2(30) | Y |  |  |
| 165 | COD_BANCO_AUTO | VARCHAR2(10) | Y |  |  |
| 166 | COD_AGENCIA_AUTO | VARCHAR2(15) | Y |  |  |
| 167 | COD_AUTENTIC_COF | VARCHAR2(44) | Y |  |  |
| 168 | CNPJ_EMIT_COF | VARCHAR2(14) | Y |  |  |
| 169 | COD_MODELO_COF | VARCHAR2(2) | Y |  |  |
| 170 | SERIE_DOCFIS_COF | VARCHAR2(3) | Y |  |  |
| 171 | NUM_DOCFIS_COF | VARCHAR2(12) | Y |  |  |
| 172 | ANO_MES_COF | VARCHAR2(6) | Y |  |  |
| 173 | COD_HASH_COF | VARCHAR2(32) | Y |  |  |
| 174 | CHAVE_SAFX42 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |
| 175 | SEQ_ARQ | NUMBER(20) | Y |  |  |

**Indexes**:
- IX_CHAVE_SAFX42: (CHAVE_SAFX42)
- IX_SAFX42: (DAT_GRAVACAO)
- IX_SAFX42_1: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL, NUM_PROCESSO)
- IX_SAFX42_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX42_LOTE: (NUM_LOTE)

---

## SAFX43

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_ITEM | VARCHAR2(7) | Y |  |  |
| 10 | IND_TP_REGISTRO | CHAR(1) | Y |  |  |
| 11 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | DAT_SERVICO | VARCHAR2(8) | Y |  |  |
| 15 | HR_SERVICO | VARCHAR2(6) | Y |  |  |
| 16 | TM_DURACAO | VARCHAR2(8) | Y |  |  |
| 17 | TEL_DESTINO | VARCHAR2(15) | Y |  |  |
| 18 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 19 | VLR_SERVICO | VARCHAR2(17) | Y |  |  |
| 20 | IND_ADIC_DESC | CHAR(1) | Y |  |  |
| 21 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 22 | VLR_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 23 | VLR_BASE_ICMS_1 | VARCHAR2(17) | Y |  |  |
| 24 | VLR_BASE_ICMS_2 | VARCHAR2(17) | Y |  |  |
| 25 | VLR_BASE_ICMS_3 | VARCHAR2(17) | Y |  |  |
| 26 | VLR_BASE_ICMS_4 | VARCHAR2(17) | Y |  |  |
| 27 | VLR_BASE_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 28 | VLR_TRIB_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 29 | VLR_ALIQ_ICMS_DEST | VARCHAR2(7) | Y |  |  |
| 30 | DSC_PRD_SERV | VARCHAR2(50) | Y |  |  |
| 31 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 32 | COD_SIT_TRIB_A | CHAR(1) | Y |  |  |
| 33 | COD_SIT_TRIB_B | VARCHAR2(2) | Y |  |  |
| 34 | COD_CLASS_SERV | CHAR(1) | Y |  |  |
| 35 | TEL_ACESSO | VARCHAR2(15) | Y |  |  |
| 36 | VLR_BASE_ISS | VARCHAR2(17) | Y |  |  |
| 37 | VLR_ALIQ_ISS | VARCHAR2(7) | Y |  |  |
| 38 | VLR_ISS | VARCHAR2(17) | Y |  |  |
| 39 | VLR_SUBST_TRIB | VARCHAR2(17) | Y |  |  |
| 40 | VLR_BASE_SUB_TRIB | VARCHAR2(17) | Y |  |  |
| 41 | DAT_GRAVACAO | DATE | Y |  |  |
| 42 | VLR_DESC_COND | VARCHAR2(17) | Y |  |  |
| 43 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  |  |
| 44 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 45 | QTD_CONTRATADA | VARCHAR2(17) | Y |  |  |
| 46 | QTD_FORNECIDA | VARCHAR2(17) | Y |  |  |
| 47 | VLR_OUTRAS_DESP | VARCHAR2(17) | Y |  |  |
| 48 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 49 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 50 | VLR_BASE_ISS_2 | VARCHAR2(17) | Y |  |  |
| 51 | VLR_BASE_ISS_3 | VARCHAR2(17) | Y |  |  |
| 52 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 53 | CNPJ_OPERADORA | VARCHAR2(14) | Y |  |  |
| 54 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 55 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 56 | CPF_OPERADORA | VARCHAR2(14) | Y |  |  |
| 57 | UF_OPERADORA | VARCHAR2(2) | Y |  |  |
| 58 | INS_EST_OPERADORA | VARCHAR2(14) | Y |  |  |
| 59 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 60 | VLR_UNIT | VARCHAR2(19) | Y |  |  |
| 61 | IND_SERV_PPAGO | CHAR(1) | Y |  |  |
| 62 | NUM_CARTAO_PPAGO | VARCHAR2(20) | Y |  |  |
| 63 | COD_MODALIDADE_PPAGO | VARCHAR2(2) | Y |  |  |
| 64 | HORA_DISP_CRED_PPAGO | VARCHAR2(6) | Y |  |  |
| 65 | DATA_DISP_CRED_PPAGO | VARCHAR2(8) | Y |  |  |
| 66 | UF_ACESSO | VARCHAR2(2) | Y |  |  |
| 67 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 68 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 69 | DATA_DOCFIS_REF | VARCHAR2(8) | Y |  |  |
| 70 | AG_ARREC | VARCHAR2(20) | Y |  |  |
| 71 | UF_RECARGA | VARCHAR2(2) | Y |  |  |
| 72 | DT_PRIM_RECARGA | VARCHAR2(8) | Y |  |  |
| 73 | HR_PRIM_RECARGA | VARCHAR2(6) | Y |  |  |
| 74 | DT_ULT_RECARGA | VARCHAR2(8) | Y |  |  |
| 75 | HR_ULT_RECARGA | VARCHAR2(6) | Y |  |  |
| 76 | NUM_LOTE_PIN | VARCHAR2(20) | Y |  |  |
| 77 | VLR_TERCEIROS | VARCHAR2(17) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 78 | COD_CLASS_IT_CTP | VARCHAR2(3) | Y |  | Cod. Classificacao do Item p/ ATO COTEPE - REG C750 |
| 79 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 80 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 81 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 82 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 83 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 84 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 85 | IND_FIS_RECEITA | CHAR(1) | Y |  |  |
| 86 | COD_FIS_RECEITA | VARCHAR2(14) | Y |  |  |
| 87 | VLR_ALIQ_ICMS_ST | VARCHAR2(7) | Y |  |  |
| 88 | IND_TP_SERV | CHAR(1) | Y |  |  |
| 89 | DAT_INIC_SERV | VARCHAR2(8) | Y |  |  |
| 90 | DAT_FINAL_SERV | VARCHAR2(8) | Y |  |  |
| 91 | COD_AREA_TERM_FAT | VARCHAR2(14) | Y |  |  |
| 92 | COD_TERM_FAT | VARCHAR2(20) | Y |  |  |
| 93 | COD_OBS_VCONT_COMP | VARCHAR2(10) | Y |  | Código do Amparo/Texto/Ocorrência para ICMS Próprio |
| 94 | VLR_ICMS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 95 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 96 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 97 | IND_TP_REC_PIS_COFINS | CHAR(1) | Y |  |  |
| 98 | IND_TIPO_JUD | CHAR(1) | Y |  |  |
| 99 | VLR_BASE_ICMS_JUD | VARCHAR2(17) | Y |  |  |
| 100 | VLR_ICMS_JUD | VARCHAR2(17) | Y |  |  |
| 101 | VLR_ICMS_EST_RET | VARCHAR2(17) | Y |  |  |
| 102 | HIPOTESE_ESTORNO | VARCHAR2(1) | Y |  |  |
| 103 | MOTIVO_ESTORNO | VARCHAR2(200) | Y |  |  |
| 104 | NUM_CTRL_RECL | VARCHAR2(20) | Y |  |  |
| 105 | VLR_ICMS_FECEP | VARCHAR2(17) | Y |  |  |
| 106 | VLR_ALIQ_ICMS_FECEP | VARCHAR2(7) | Y |  |  |
| 107 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 108 | VLR_BC_ICMS_UF | VARCHAR2(17) | Y |  |  |
| 109 | VLR_ICMS_UF | VARCHAR2(17) | Y |  |  |
| 110 | VLR_ACUM_DE_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 111 | VLR_ACUM_DE_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 112 | NUM_ITEM_REAL | VARCHAR2(7) | Y |  |  |
| 113 | NUM_CONTRATO | VARCHAR2(15) | Y |  |  |
| 114 | QTD_FATURADA | VARCHAR2(17) | Y |  |  |
| 115 | VLR_TARIFA | VARCHAR2(21) | Y |  |  |
| 116 | IND_TIPO_RED | VARCHAR2(2) | Y |  |  |
| 117 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 118 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 119 | VLR_ICMS_ST_FECEP | VARCHAR2(17) | Y |  |  |
| 120 | PST_ID | NUMBER | Y |  |  |
| 121 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 122 | VLR_SERV_N_TRIB | VARCHAR2(17) | Y |  |  |
| 123 | COD_GRUPO_CCLASS | VARCHAR2(3) | Y |  |  |
| 124 | VLR_OUTRAS_DED | VARCHAR2(17) | Y |  |  |
| 125 | VLR_ENERGIA_COMP | VARCHAR2(17) | Y |  |  |
| 126 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 127 | COD_AUTENTIC_NFE_ANT | VARCHAR2(44) | Y |  |  |
| 128 | NUM_ITEM_NFE_ANT | VARCHAR2(3) | Y |  |  |
| 129 | COD_CCLASS | VARCHAR2(7) | Y |  |  |
| 130 | CPNPJ_OPER_LD | VARCHAR2(14) | Y |  |  |
| 131 | DAT_EXPIRA_CRED | VARCHAR2(8) | Y |  |  |
| 132 | PERC_RED_BC | VARCHAR2(5) | Y |  |  |
| 133 | VLR_ICMS_DESONERADO | VARCHAR2(17) | Y |  |  |
| 134 | COD_BENEF_FISCAL | VARCHAR2(10) | Y |  |  |
| 135 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 136 | PERC_FCP_DEST | VARCHAR2(5) | Y |  |  |
| 137 | VLR_FCP_DEST | VARCHAR2(17) | Y |  |  |
| 138 | VLR_ICMS_UF_EMIT | VARCHAR2(17) | Y |  |  |
| 139 | COD_BENEF_FISCAL_DEST | VARCHAR2(10) | Y |  |  |
| 140 | VLR_BC_FUST | VARCHAR2(17) | Y |  |  |
| 141 | VLR_ALIQ_FUST | VARCHAR2(7) | Y |  |  |
| 142 | VLR_FUST | VARCHAR2(17) | Y |  |  |
| 143 | VLR_BC_FUNTTEL | VARCHAR2(17) | Y |  |  |
| 144 | VLR_ALIQ_FUNTTEL | VARCHAR2(7) | Y |  |  |
| 145 | VLR_FUNTTEL | VARCHAR2(17) | Y |  |  |
| 146 | VLR_PIS_RETIDO | VARCHAR2(23) | Y |  |  |
| 147 | VLR_COFINS_RETIDO | VARCHAR2(23) | Y |  |  |
| 148 | VLR_CSLL_RETIDO | VARCHAR2(23) | Y |  |  |
| 149 | VLR_BC_IRRF | VARCHAR2(23) | Y |  |  |
| 150 | VLR_IRRF_RETIDO | VARCHAR2(23) | Y |  |  |
| 151 | VLR_UNIT_PROC | VARCHAR2(23) | Y |  |  |
| 152 | QTD_FAT_PROC | VARCHAR2(19) | Y |  |  |
| 153 | VLR_ITEM_PROC | VARCHAR2(23) | Y |  |  |
| 154 | VLR_DESC_PROC | VARCHAR2(17) | Y |  |  |
| 155 | VLR_OUT_DESP_PROC | VARCHAR2(17) | Y |  |  |
| 156 | IND_DEV_PROC | VARCHAR2(1) | Y |  |  |
| 157 | VLR_BC_ICMS_PROC | VARCHAR2(17) | Y |  |  |
| 158 | VLR_ALIQ_ICMS_PROC | VARCHAR2(7) | Y |  |  |
| 159 | VLR_ICMS_PROC | VARCHAR2(17) | Y |  |  |
| 160 | VLR_PIS_PROC | VARCHAR2(17) | Y |  |  |
| 161 | VLR_COFINS_PROC | VARCHAR2(17) | Y |  |  |
| 162 | IND_TP_RESSARC | VARCHAR2(2) | Y |  |  |
| 163 | DATA_REF_RESSARC | VARCHAR2(8) | Y |  |  |
| 164 | NUM_PROC_RESSARC | VARCHAR2(60) | Y |  |  |
| 165 | NUM_PROT_RESSARC | VARCHAR2(60) | Y |  |  |
| 166 | DSC_OBS_RESSARC | VARCHAR2(100) | Y |  |  |
| 167 | DSC_ADIC_RESSARC | VARCHAR2(500) | Y |  |  |
| 168 | IND_NF_ANT | VARCHAR2(1) | Y |  |  |
| 169 | VLR_FCP_ICMS_PROC | VARCHAR2(17) | Y |  |  |
| 170 | CHAVE_SAFX43 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |
| 171 | SEQ_ARQ | NUMBER(20) | Y |  |  |

**Indexes**:
- IX_CHAVE_SAFX43: (CHAVE_SAFX43)
- IX_SAFX43: (DAT_GRAVACAO)
- IX_SAFX43_1: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL, NUM_PROCESSO)
- IX_SAFX43_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX43_LOTE: (NUM_LOTE)

---

## SAFX431

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_ITEM | VARCHAR2(7) | Y |  |  |
| 10 | IND_ITEM_DED | CHAR(1) | Y |  |  |
| 11 | NUM_ITEM_CONSOL | VARCHAR2(7) | Y |  |  |
| 12 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 13 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 14 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 15 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 16 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 17 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 18 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  |  |
| 19 | QTD_CONTRATADA | VARCHAR2(17) | Y |  |  |
| 20 | QTD_FORNECIDA | VARCHAR2(17) | Y |  |  |
| 21 | VLR_SERVICO | VARCHAR2(17) | Y |  |  |
| 22 | VLR_OUTRAS_DESP | VARCHAR2(17) | Y |  |  |
| 23 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 24 | VLR_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 25 | VLR_BASE_ICMS_1 | VARCHAR2(17) | Y |  |  |
| 26 | VLR_BASE_ICMS_2 | VARCHAR2(17) | Y |  |  |
| 27 | VLR_BASE_ICMS_3 | VARCHAR2(17) | Y |  |  |
| 28 | VLR_BASE_ICMS_4 | VARCHAR2(17) | Y |  |  |
| 29 | DSC_PRD_SERV | VARCHAR2(50) | Y |  |  |
| 30 | DAT_GRAVACAO | DATE | Y |  |  |
| 31 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 32 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 33 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 34 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 35 | IND_DESC_JUD | CHAR(1) | Y |  |  |
| 36 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 37 | PST_ID | NUMBER | Y |  |  |
| 38 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 39 | CHAVE_SAFX431 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX431: (CHAVE_SAFX431)
- IX_SAFX431_LOTE: (NUM_LOTE)

---

## SAFX432

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | NUM_ITEM | VARCHAR2(7) | Y |  |  |
| 10 | IND_TP_PROCESSO | CHAR(1) | Y |  |  |
| 11 | NUM_PROCESSO_NF | VARCHAR2(60) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | CHAVE_SAFX432 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX432: (CHAVE_SAFX432)
- IX_SAFX432: (DAT_GRAVACAO)
- IX_SAFX432_LOTE: (NUM_LOTE)

---

## SAFX433

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | NUM_INSTAL_INJ | VARCHAR2(12) | Y |  |  |
| 5 | DAT_REF_INJ | VARCHAR2(8) | Y |  |  |
| 6 | COD_POSTO_INJ | VARCHAR2(2) | Y |  |  |
| 7 | VLR_TARIFA_INJ | VARCHAR2(11) | Y |  |  |
| 8 | QTD_ENERGIA_INI | VARCHAR2(13) | Y |  |  |
| 9 | QTD_ENERGIA_INJ | VARCHAR2(12) | Y |  |  |
| 10 | QTD_ENERGIA_SAI | VARCHAR2(12) | Y |  |  |
| 11 | QTD_ENERGIA_FIM | VARCHAR2(13) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | CHAVE_SAFX433 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX433: (CHAVE_SAFX433)
- IX_SAFX433: (DAT_GRAVACAO)
- IX_SAFX433_LOTE: (NUM_LOTE)

---

## SAFX44

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 15 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 16 | NUM_CHASSI | VARCHAR2(17) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | COD_COR | VARCHAR2(4) | Y |  |  |
| 19 | DSC_COR | VARCHAR2(40) | Y |  |  |
| 20 | DSC_POTENCIA | VARCHAR2(4) | Y |  |  |
| 21 | DSC_POTENCIA_CM3 | VARCHAR2(4) | Y |  |  |
| 22 | PESO_LIQUIDO | VARCHAR2(14) | Y |  |  |
| 23 | PESO_BRUTO | VARCHAR2(14) | Y |  |  |
| 24 | SERIE_VEIC | VARCHAR2(9) | Y |  |  |
| 25 | DSC_TP_COMBUSTIVEL | VARCHAR2(8) | Y |  |  |
| 26 | NUM_MOTOR | VARCHAR2(21) | Y |  |  |
| 27 | DSC_CMKG | VARCHAR2(9) | Y |  |  |
| 28 | DSC_DISTANCIA_EIXO | VARCHAR2(4) | Y |  |  |
| 29 | NUM_RENAVAM | VARCHAR2(14) | Y |  |  |
| 30 | NUM_MARCA_MODELO | VARCHAR2(6) | Y |  |  |
| 31 | NUM_ANO_MODELO | VARCHAR2(4) | Y |  |  |
| 32 | NUM_ANO_FABRIC | VARCHAR2(4) | Y |  |  |
| 33 | IND_TP_PINTURA | CHAR(1) | Y |  |  |
| 34 | NUM_TP_VEIC | VARCHAR2(2) | Y |  |  |
| 35 | NUM_ESPECIE_VEIC | VARCHAR2(1) | Y |  |  |
| 36 | IND_CONDICAO_VIN | CHAR(1) | Y |  |  |
| 37 | IND_CONDICAO_VEIC | CHAR(1) | Y |  |  |
| 38 | PLACA_VEICULO | VARCHAR2(7) | Y |  |  |
| 39 | PST_ID | NUMBER | Y |  |  |
| 40 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 41 | CHAVE_SAFX44 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX44: (CHAVE_SAFX44)
- IX_SAFX44: (DAT_GRAVACAO)
- IX_SAFX44_LOTE: (NUM_LOTE)

---

## SAFX45

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 5 | COD_PARAM | VARCHAR2(3) | Y |  |  |
| 6 | DAT_GRAVACAO | DATE | Y |  |  |
| 7 | PST_ID | NUMBER | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX45 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX45: (CHAVE_SAFX45)
- IX_SAFX45_LOTE: (NUM_LOTE)

---

## SAFX46

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_ENTRADA_RE | VARCHAR2(8) | Y |  |  |
| 4 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 8 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 9 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 11 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(5) | Y |  |  |
| 13 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 14 | DATA_SAIDA_MINUTA | VARCHAR2(8) | Y |  |  |
| 15 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 16 | IND_FISJUR_TRANSP | CHAR(1) | Y |  |  |
| 17 | COD_FISJUR_TRANSP | VARCHAR2(14) | Y |  |  |
| 18 | DAT_INTERN_AM | VARCHAR2(8) | Y |  |  |
| 19 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 20 | PLACA_VEICULO | VARCHAR2(10) | Y |  |  |
| 21 | NUM_MINUTA | VARCHAR2(12) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | PST_ID | NUMBER | Y |  |  |
| 24 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 25 | CHAVE_SAFX46 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX46: (CHAVE_SAFX46)
- IX_SAFX46_01: (DAT_GRAVACAO)
- IX_SAFX46_LOTE: (NUM_LOTE)

---

## SAFX47

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_DI | VARCHAR2(8) | Y |  |  |
| 4 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 5 | DATA_DESEMB_ADUAN | VARCHAR2(8) | Y |  |  |
| 6 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 7 | DAT_GRAVACAO | DATE | Y |  |  |
| 8 | PST_ID | NUMBER | Y |  |  |
| 9 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 10 | CHAVE_SAFX47 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX47: (CHAVE_SAFX47)
- IX_SAFX47: (DAT_GRAVACAO)
- IX_SAFX47_LOTE: (NUM_LOTE)

---

## SAFX48

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_RE | VARCHAR2(8) | Y |  |  |
| 4 | NUM_RE | VARCHAR2(15) | Y |  |  |
| 5 | DAT_NF | VARCHAR2(8) | Y |  |  |
| 6 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_NF | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_NF | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_NF | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 14 | DAT_SAIDA | VARCHAR2(8) | Y |  |  |
| 15 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 16 | COD_EX | VARCHAR2(3) | Y |  |  |
| 17 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 18 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 19 | COD_MEDIDA_COM | VARCHAR2(8) | Y |  |  |
| 20 | AG_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 21 | ANO_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 22 | NUM_ATO_CONCES | VARCHAR2(6) | Y |  |  |
| 23 | DIG_ATO_CONCES | VARCHAR2(1) | Y |  |  |
| 24 | PESO_BRUTO | VARCHAR2(17) | Y |  |  |
| 25 | PESO_LIQUIDO | VARCHAR2(17) | Y |  |  |
| 26 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 27 | QTD_UND_MED | VARCHAR2(17) | Y |  |  |
| 28 | QTD_UND_COM | VARCHAR2(17) | Y |  |  |
| 29 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 30 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 31 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 32 | VLR_DESP_ACRESC | VARCHAR2(17) | Y |  |  |
| 33 | VLR_DESP_COMIS | VARCHAR2(17) | Y |  |  |
| 34 | VLR_DESP_ARMAZ | VARCHAR2(17) | Y |  |  |
| 35 | VLR_DESP_ROYAL | VARCHAR2(17) | Y |  |  |
| 36 | VLR_DEDUCAO | VARCHAR2(17) | Y |  |  |
| 37 | VLR_NF | VARCHAR2(17) | Y |  |  |
| 38 | BASE_IPI | VARCHAR2(17) | Y |  |  |
| 39 | VLR_ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 40 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 41 | VLR_ISENTA_IPI | VARCHAR2(17) | Y |  |  |
| 42 | VLR_OUTRAS_IPI | VARCHAR2(17) | Y |  |  |
| 43 | BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 44 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 45 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 46 | VLR_ISENTA_ICMS | VARCHAR2(17) | Y |  |  |
| 47 | VLR_OUTRAS_ICMS | VARCHAR2(17) | Y |  |  |
| 48 | BASE_IE | VARCHAR2(17) | Y |  |  |
| 49 | VLR_ALIQ_IE | VARCHAR2(7) | Y |  |  |
| 50 | VLR_IE | VARCHAR2(17) | Y |  |  |
| 51 | NUM_DDE_DSE | VARCHAR2(14) | Y |  |  |
| 52 | DAT_DDE_DSE | VARCHAR2(8) | Y |  |  |
| 53 | VLR_DESPACHO | VARCHAR2(17) | Y |  |  |
| 54 | DAT_EMBARQUE | VARCHAR2(8) | Y |  |  |
| 55 | DAT_AVERBACAO | VARCHAR2(8) | Y |  |  |
| 56 | PAIS_DEST | VARCHAR2(3) | Y |  |  |
| 57 | MOEDA_OPER | VARCHAR2(10) | Y |  |  |
| 58 | VLR_LIQ_MERC | VARCHAR2(17) | Y |  |  |
| 59 | VLR_MERC_DOLAR | VARCHAR2(17) | Y |  |  |
| 60 | VLR_MERC_MOEDA | VARCHAR2(17) | Y |  |  |
| 61 | NUM_FAT_COM | VARCHAR2(12) | Y |  |  |
| 62 | DAT_FAT_COM | VARCHAR2(8) | Y |  |  |
| 63 | OBS | VARCHAR2(120) | Y |  |  |
| 64 | IND_TP_OP | CHAR(1) | Y |  |  |
| 65 | IND_PRD_SER_DIR | CHAR(1) | Y |  |  |
| 66 | PRECO_MED_UNIT | VARCHAR2(17) | Y |  |  |
| 67 | IND_AJUSTE_EFET | CHAR(1) | Y |  |  |
| 68 | IND_MET_AJUSTE | CHAR(1) | Y |  |  |
| 69 | VLR_AJUSTE | VARCHAR2(17) | Y |  |  |
| 70 | IND_COND_PES | CHAR(1) | Y |  |  |
| 71 | IND_TP_VENDA | VARCHAR2(2) | Y |  |  |
| 72 | CNPJ_ESTAB_BENEF | VARCHAR2(14) | Y |  |  |
| 73 | COMP_EXPORT | VARCHAR2(15) | Y |  |  |
| 74 | DAT_GRAVACAO | DATE | Y |  |  |
| 75 | DAT_COMP_EXPORT | VARCHAR2(8) | Y |  |  |
| 76 | NUM_CONHEC_EMB | VARCHAR2(18) | Y |  |  |
| 77 | DAT_CONHEC_EMB | VARCHAR2(8) | Y |  |  |
| 78 | COD_TP_CONHEC | VARCHAR2(2) | Y |  |  |
| 79 | IND_AVERBACAO | CHAR(1) | Y |  |  |
| 80 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 81 | IND_FIS_JUR_EXP | CHAR(1) | Y |  |  |
| 82 | COD_FIS_JUR_EXP | VARCHAR2(14) | Y |  |  |
| 83 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 84 | VLR_REINTEGRA | VARCHAR2(17) | Y |  |  |
| 85 | IND_EXP_SERVICO | CHAR(1) | Y |  |  |
| 86 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 87 | IND_CLASS_SEGURO | CHAR(1) | Y |  |  |
| 88 | IND_CLASS_FRETE | CHAR(1) | Y |  |  |
| 89 | IND_CLASS_ACRES | CHAR(1) | Y |  |  |
| 90 | IND_CLASS_COMIS | CHAR(1) | Y |  |  |
| 91 | IND_CLASS_ARMAZ | CHAR(1) | Y |  |  |
| 92 | IND_CLASS_ROYALTIES | CHAR(1) | Y |  |  |
| 93 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 94 | PST_ID | NUMBER | Y |  |  |
| 95 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 96 | CHAVE_SAFX48 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX48: (CHAVE_SAFX48)
- IX_SAFX48_LOTE: (NUM_LOTE)

---

## SAFX481

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_RE_OPER | VARCHAR2(8) | Y |  |  |
| 4 | NUM_RE_OPER | VARCHAR2(15) | Y |  |  |
| 5 | DAT_NF_OPER | VARCHAR2(8) | Y |  |  |
| 6 | IND_FIS_JUR_OPER | CHAR(1) | Y |  |  |
| 7 | COD_FIS_JUR_OPER | VARCHAR2(14) | Y |  |  |
| 8 | NUM_NF_OPER | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_NF_OPER | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_NF_OPER | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO_OPER | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO_OPER | VARCHAR2(60) | Y |  |  |
| 13 | NUM_ITEM_OPER | VARCHAR2(5) | Y |  |  |
| 14 | NUM_RE_REM | VARCHAR2(15) | Y |  |  |
| 15 | DAT_FISCAL_REM | VARCHAR2(8) | Y |  |  |
| 16 | IND_FIS_JUR_REM | CHAR(1) | Y |  |  |
| 17 | COD_FIS_JUR_REM | VARCHAR2(14) | Y |  |  |
| 18 | NUM_DOCFIS_REM | VARCHAR2(12) | Y |  |  |
| 19 | SERIE_DOCFIS_REM | VARCHAR2(3) | Y |  |  |
| 20 | SUB_SERIE_DOCFIS_REM | VARCHAR2(2) | Y |  |  |
| 21 | IND_PRODUTO_REM | CHAR(1) | Y |  |  |
| 22 | COD_PRODUTO_REM | VARCHAR2(60) | Y |  |  |
| 23 | QTD_EXPORTADA | VARCHAR2(17) | Y |  |  |
| 24 | IND_EXP_SIMPL | CHAR(1) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |
| 26 | NUM_CONHEC_EMB_OPER | VARCHAR2(18) | Y |  |  |
| 27 | NUM_MEMO_EXP_REM | VARCHAR2(50) | Y |  |  |
| 28 | PST_ID | NUMBER | Y |  |  |
| 29 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 30 | CHAVE_SAFX481 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX481: (CHAVE_SAFX481)
- IX_SAFX481_LOTE: (NUM_LOTE)

---

## SAFX49

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_DI | VARCHAR2(8) | Y |  |  |
| 4 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 5 | DAT_NF | VARCHAR2(8) | Y |  |  |
| 6 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_NF | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_NF | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_NF | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 14 | DAT_ENTRADA | VARCHAR2(8) | Y |  |  |
| 15 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 16 | COD_EX | VARCHAR2(3) | Y |  |  |
| 17 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 18 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 19 | COD_MEDIDA_COM | VARCHAR2(8) | Y |  |  |
| 20 | AG_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 21 | ANO_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 22 | NUM_ATO_CONCES | VARCHAR2(20) | Y |  |  |
| 23 | DIG_ATO_CONCES | VARCHAR2(1) | Y |  |  |
| 24 | PESO_BRUTO | VARCHAR2(17) | Y |  |  |
| 25 | PESO_LIQUIDO | VARCHAR2(17) | Y |  |  |
| 26 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 27 | QTD_UND_MED | VARCHAR2(17) | Y |  |  |
| 28 | QTD_UND_COM | VARCHAR2(17) | Y |  |  |
| 29 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 30 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 31 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 32 | VLR_DESP_ADUAN | VARCHAR2(17) | Y |  |  |
| 33 | VLR_DESP_ACRESC | VARCHAR2(17) | Y |  |  |
| 34 | VLR_DEDUCAO | VARCHAR2(17) | Y |  |  |
| 35 | VLR_NF | VARCHAR2(17) | Y |  |  |
| 36 | BASE_IPI | VARCHAR2(17) | Y |  |  |
| 37 | VLR_ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 38 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 39 | VLR_ISENTA_IPI | VARCHAR2(17) | Y |  |  |
| 40 | VLR_OUTRAS_IPI | VARCHAR2(17) | Y |  |  |
| 41 | BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 42 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 43 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 44 | VLR_ISENTA_ICMS | VARCHAR2(17) | Y |  |  |
| 45 | VLR_OUTRAS_ICMS | VARCHAR2(17) | Y |  |  |
| 46 | BASE_II | VARCHAR2(17) | Y |  |  |
| 47 | VLR_ALIQ_II | VARCHAR2(7) | Y |  |  |
| 48 | VLR_II | VARCHAR2(17) | Y |  |  |
| 49 | PAIS_ORIG | VARCHAR2(3) | Y |  |  |
| 50 | MOEDA_ORIG | VARCHAR2(10) | Y |  |  |
| 51 | VLR_LIQ_MERC | VARCHAR2(17) | Y |  |  |
| 52 | VLR_MERC_DOLAR | VARCHAR2(17) | Y |  |  |
| 53 | VLR_MERC_MOEDA | VARCHAR2(17) | Y |  |  |
| 54 | OBS | VARCHAR2(120) | Y |  |  |
| 55 | IND_TP_OP | CHAR(1) | Y |  |  |
| 56 | IND_PRD_SER_DIR | CHAR(1) | Y |  |  |
| 57 | IND_AJUSTE_EFET | CHAR(1) | Y |  |  |
| 58 | IND_MET_AJUSTE | CHAR(1) | Y |  |  |
| 59 | VLR_AJUSTE | VARCHAR2(17) | Y |  |  |
| 60 | IND_COND_PES | CHAR(1) | Y |  |  |
| 61 | DAT_GRAVACAO | DATE | Y |  |  |
| 62 | MOEDA_OP_FRETE | VARCHAR2(10) | Y |  |  |
| 63 | VLR_FRETE_MOEDA | VARCHAR2(17) | Y |  |  |
| 64 | MOEDA_OP_SEGURO | VARCHAR2(10) | Y |  |  |
| 65 | VLR_SEGURO_MOEDA | VARCHAR2(17) | Y |  |  |
| 66 | VLR_UNIT_REAL | VARCHAR2(17) | Y |  |  |
| 67 | COD_FORN_ORIG | VARCHAR2(14) | Y |  |  |
| 68 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 69 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 70 | VLR_IOF | VARCHAR2(17) | Y |  |  |
| 71 | VLR_ADUAN_SEM_ICMS | VARCHAR2(17) | Y |  |  |
| 72 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 73 | DAT_DESEMBARACO | VARCHAR2(8) | Y |  | Data do Desembaraço ATO COTEPE - REG C060 |
| 74 | TIPO_DI | CHAR(1) | Y |  |  |
| 75 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 76 | PST_ID | NUMBER | Y |  |  |
| 77 | INCOTERM | VARCHAR2(5) | Y |  |  |
| 78 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 79 | IND_TP_INTERMEDIO | VARCHAR2(1) | Y |  |  |
| 80 | CHAVE_SAFX49 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX49: (CHAVE_SAFX49)
- IX_SAFX49_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX49_LOTE: (NUM_LOTE)

---

## SAFX50

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_FIS_TRANSP | CHAR(1) | Y |  |  |
| 13 | COD_FIS_TRANSP | VARCHAR2(14) | Y |  |  |
| 14 | MODALIDADE_FRETE | CHAR(1) | Y |  |  |
| 15 | COD_VIA_TRANSP | VARCHAR2(5) | Y |  |  |
| 16 | QTD_VOLUMES | VARCHAR2(17) | Y |  |  |
| 17 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 18 | PESO_BRUTO | VARCHAR2(14) | Y |  |  |
| 19 | PESO_LIQUIDO | VARCHAR2(14) | Y |  |  |
| 20 | DESPESA_FRETE | VARCHAR2(17) | Y |  |  |
| 21 | DESPESA_SEGURO | VARCHAR2(17) | Y |  |  |
| 22 | NUM_CFRETE_DESPAC | VARCHAR2(12) | Y |  |  |
| 23 | PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 24 | DAT_GRAVACAO | DATE | Y |  |  |
| 25 | CNH_MOTORISTA | VARCHAR2(11) | Y |  |  |
| 26 | NOME_MOTORISTA | VARCHAR2(40) | Y |  |  |
| 27 | PLACA_CARRETA | VARCHAR2(7) | Y |  |  |
| 28 | DAT_ENT_VEIC | VARCHAR2(8) | Y |  |  |
| 29 | HORA_ENT_VEIC | VARCHAR2(4) | Y |  |  |
| 30 | HORA_SAI_VEIC | VARCHAR2(4) | Y |  |  |
| 31 | ORDEM_CARREG | VARCHAR2(6) | Y |  |  |
| 32 | UF_CAM | VARCHAR2(2) | Y |  |  |
| 33 | CIDADE_CAM | VARCHAR2(18) | Y |  |  |
| 34 | NUM_VIAGEM | VARCHAR2(15) | Y |  |  |
| 35 | VLR_BASE_ICMSS | VARCHAR2(17) | Y |  |  |
| 36 | VLR_ICMSS | VARCHAR2(17) | Y |  |  |
| 37 | UF_VEIC | VARCHAR2(2) | Y |  |  |
| 38 | PLACA_REBOQUE | VARCHAR2(17) | Y |  |  |
| 39 | UF_REBOQ | VARCHAR2(2) | Y |  |  |
| 40 | MARCA_VOLUME | VARCHAR2(50) | Y |  |  |
| 41 | NUM_VOLUME | VARCHAR2(50) | Y |  |  |
| 42 | IND_FIS_JUR_CONSIG | CHAR(1) | Y |  |  |
| 43 | COD_FIS_JUR_CONSIG | VARCHAR2(14) | Y |  |  |
| 44 | IND_FIS_JUR_REDESP | CHAR(1) | Y |  |  |
| 45 | COD_FIS_JUR_REDESP | VARCHAR2(14) | Y |  |  |
| 46 | COD_VEIC_TRANSP | VARCHAR2(6) | Y |  |  |
| 47 | IND_TP_NAVEGACAO | CHAR(1) | Y |  |  |
| 48 | IND_TARIFA_AEREA | CHAR(1) | Y |  |  |
| 49 | IND_NATUREZA_FRETE | CHAR(1) | Y |  |  |
| 50 | REGISTRO_OPERADOR | VARCHAR2(30) | Y |  |  |
| 51 | VLR_FRETE_PV | VARCHAR2(17) | Y |  |  |
| 52 | VLR_FRETE_LIQ | VARCHAR2(17) | Y |  |  |
| 53 | VLR_FRETE_BRUTO | VARCHAR2(17) | Y |  |  |
| 54 | VLR_FRETE_MM | VARCHAR2(17) | Y |  |  |
| 55 | VLR_SEC_CAT | VARCHAR2(17) | Y |  |  |
| 56 | VLR_DESPACHO | VARCHAR2(17) | Y |  |  |
| 57 | VLR_PEDAGIO | VARCHAR2(17) | Y |  |  |
| 58 | VLR_DESPESA_PORT | VARCHAR2(17) | Y |  |  |
| 59 | VLR_DESPESA_CARGA | VARCHAR2(17) | Y |  |  |
| 60 | VLR_PESO_TAXADO | VARCHAR2(17) | Y |  |  |
| 61 | VLR_TAXA_TERRESTRE | VARCHAR2(17) | Y |  |  |
| 62 | VLR_TAXA_REDESPACHO | VARCHAR2(17) | Y |  |  |
| 63 | VLR_TAXA_ADV | VARCHAR2(17) | Y |  |  |
| 64 | VLR_GRIS | VARCHAR2(17) | Y |  |  |
| 65 | VLR_TARIFA | VARCHAR2(17) | Y |  |  |
| 66 | COD_LINHA_TRANSP | VARCHAR2(10) | Y |  |  |
| 67 | DSC_LINHA_TRANSP | VARCHAR2(50) | Y |  |  |
| 68 | POLTRONA | VARCHAR2(10) | Y |  |  |
| 69 | AGENTE | VARCHAR2(30) | Y |  |  |
| 70 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 71 | VLR_OUTROS | VARCHAR2(17) | Y |  | Data do Desembaraço ATO COTEPE - REG D050, D060, D070, D080 E D210 |
| 72 | MATRICULA | VARCHAR2(16) | Y |  |  |
| 73 | COD_AUTORIZ_SEFAZ | VARCHAR2(21) | Y |  |  |
| 74 | NUM_PASSE_FISCAL | VARCHAR2(20) | Y |  |  |
| 75 | TEMPERATURA | VARCHAR2(5) | Y |  |  |
| 76 | CPF_MOTORISTA | VARCHAR2(11) | Y |  |  |
| 77 | MODAL_FRETE_REDESP | CHAR(1) | Y |  |  |
| 78 | IND_VAGAO_BALSA | CHAR(1) | Y |  |  |
| 79 | COD_VAGAO_BALSA | VARCHAR2(20) | Y |  |  |
| 80 | PST_ID | NUMBER | Y |  |  |
| 81 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 82 | CHAVE_SAFX50 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX50: (CHAVE_SAFX50)
- IX_SAFX50: (DAT_GRAVACAO)
- IX_SAFX50_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX50_LOTE: (NUM_LOTE)

---

## SAFX500

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 12 | NUM_DOCFIS_NF | VARCHAR2(12) | Y |  |  |
| 13 | SERIE_DOCFIS_NF | VARCHAR2(3) | Y |  |  |
| 14 | SUB_SERIE_DOCFIS_NF | VARCHAR2(2) | Y |  |  |
| 15 | DATA_FISCAL_NF | VARCHAR2(8) | Y |  |  |
| 16 | MOVTO_E_S_NF | CHAR(1) | Y |  |  |
| 17 | NORM_DEV_NF | CHAR(1) | Y |  |  |
| 18 | COD_DOCTO_NF | VARCHAR2(5) | Y |  |  |
| 19 | IND_FIS_JUR_NF | CHAR(1) | Y |  |  |
| 20 | COD_FIS_JUR_NF | VARCHAR2(14) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | PST_ID | NUMBER | Y |  |  |
| 23 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 24 | CHAVE_SAFX500 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX500: (CHAVE_SAFX500)
- IX_SAFX500: (DAT_GRAVACAO)
- IX_SAFX500_LOTE: (NUM_LOTE)

---

## SAFX501

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 12 | NUM_PARCELA | VARCHAR2(3) | Y |  |  |
| 13 | DATA_VENCTO | VARCHAR2(8) | Y |  |  |
| 14 | VLR_PARCELA | VARCHAR2(17) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | VLR_JUROS | VARCHAR2(17) | Y |  |  |
| 17 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 18 | VLR_IRRF | VARCHAR2(17) | Y |  |  |
| 19 | DATA_PGTO | VARCHAR2(8) | Y |  |  |
| 20 | IND_PGTO | CHAR(1) | Y |  |  |
| 21 | DESC_PGTO | VARCHAR2(100) | Y |  |  |
| 22 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 23 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 24 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 25 | VLR_DESC_PIS | VARCHAR2(17) | Y |  |  |
| 26 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 27 | QTD_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 28 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 29 | VLR_ALIQ_PIS_R | VARCHAR2(19) | Y |  |  |
| 30 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 31 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 32 | VLR_DESC_COFINS | VARCHAR2(17) | Y |  |  |
| 33 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 34 | QTD_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 35 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 36 | VLR_ALIQ_COFINS_R | VARCHAR2(19) | Y |  |  |
| 37 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 38 | PST_ID | NUMBER | Y |  |  |
| 39 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 40 | CHAVE_SAFX501 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX501: (CHAVE_SAFX501)
- IX_SAFX501: (DAT_GRAVACAO)
- IX_SAFX501_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX501_LOTE: (NUM_LOTE)

---

## SAFX502

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_FIS_TRANSP | CHAR(1) | Y |  |  |
| 13 | COD_FIS_TRANSP | VARCHAR2(14) | Y |  |  |
| 14 | PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 15 | UF_VEIC | VARCHAR2(2) | Y |  |  |
| 16 | NUM_VOLUME | VARCHAR2(50) | Y |  |  |
| 17 | PESO_BRUTO | VARCHAR2(14) | Y |  |  |
| 18 | PESO_LIQUIDO | VARCHAR2(14) | Y |  |  |
| 19 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 20 | DAT_GRAVACAO | DATE | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX502 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX502: (CHAVE_SAFX502)
- IX_SAFX502: (DAT_GRAVACAO)
- IX_SAFX502_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX502_LOTE: (NUM_LOTE)

---

## SAFX51

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_ESCR_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_DOCTO_TRANSP | VARCHAR2(5) | Y |  |  |
| 13 | NUM_DOCFIS_TRANSP | VARCHAR2(12) | Y |  |  |
| 14 | SER_DOCFIS_TRANSP | VARCHAR2(3) | Y |  |  |
| 15 | SSER_DOCFIS_TRANSP | VARCHAR2(2) | Y |  |  |
| 16 | DATA_EMIS_TRANSP | VARCHAR2(8) | Y |  |  |
| 17 | CGC_CPF_REMET | VARCHAR2(14) | Y |  |  |
| 18 | MODALIDADE_FRETE | CHAR(1) | Y |  |  |
| 19 | VLR_TOT_DOCFIS | VARCHAR2(17) | Y |  |  |
| 20 | INSC_UF_REMET | VARCHAR2(14) | Y |  |  |
| 21 | RAZAO_REMET | VARCHAR2(70) | Y |  |  |
| 22 | MUNICIPIO_REMET | VARCHAR2(30) | Y |  |  |
| 23 | CEP_REMET | VARCHAR2(8) | Y |  |  |
| 24 | COD_ESTADO_REMET | VARCHAR2(2) | Y |  |  |
| 25 | CPF_CGC_DEST | VARCHAR2(14) | Y |  |  |
| 26 | INSC_ESTADUAL_DEST | VARCHAR2(14) | Y |  |  |
| 27 | RAZAO_DEST | VARCHAR2(70) | Y |  |  |
| 28 | MUNICIPIO_DEST | VARCHAR2(30) | Y |  |  |
| 29 | CEP_DEST | VARCHAR2(8) | Y |  |  |
| 30 | COD_ESTADO_DEST | VARCHAR2(2) | Y |  |  |
| 31 | DOCFIS_SIM_NAO | CHAR(1) | Y |  |  |
| 32 | COD_VIA_TRANSP | VARCHAR2(5) | Y |  |  |
| 33 | QTD_VOLUME | VARCHAR2(17) | Y |  |  |
| 34 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 35 | PESO_BRUTO | VARCHAR2(14) | Y |  |  |
| 36 | PESO_LIQUIDO | VARCHAR2(14) | Y |  |  |
| 37 | DESPESA_FRETE | VARCHAR2(17) | Y |  |  |
| 38 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 39 | OBSERVACAO_FRETE | VARCHAR2(45) | Y |  |  |
| 40 | IND_FIS_JUR_TRANSP | CHAR(1) | Y |  |  |
| 41 | COD_TRANSP | VARCHAR2(14) | Y |  |  |
| 42 | COD_MUNIC_COLETA | VARCHAR2(5) | Y |  |  |
| 43 | COD_MUNIC_DEST | VARCHAR2(5) | Y |  |  |
| 44 | DISTANCIA_EM_KM | VARCHAR2(6) | Y |  |  |
| 45 | QTD_MERCADORIA | VARCHAR2(17) | Y |  |  |
| 46 | IND_FORMA_CALC | CHAR(1) | Y |  |  |
| 47 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 48 | DAT_GRAVACAO | DATE | Y |  |  |
| 49 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 50 | NAT_VOLUME | VARCHAR2(30) | Y |  |  |
| 51 | VOLUME | VARCHAR2(30) | Y |  |  |
| 52 | MARCA_VOLUME | VARCHAR2(50) | Y |  |  |
| 53 | NUM_VOLUME | VARCHAR2(30) | Y |  |  |
| 54 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 55 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 56 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 57 | NUM_DESPACHO | VARCHAR2(12) | Y |  |  |
| 58 | CPF_CNPJ_COLETA | VARCHAR2(14) | Y |  |  |
| 59 | INSCR_EST_COLETA | VARCHAR2(14) | Y |  |  |
| 60 | CPF_CNPJ_ENTREGA | VARCHAR2(14) | Y |  |  |
| 61 | INSCR_EST_ENTREGA | VARCHAR2(14) | Y |  |  |
| 62 | COD_MUNIC_REMET | VARCHAR2(5) | Y |  |  |
| 63 | COD_MUNIC_ENTREGA | VARCHAR2(5) | Y |  |  |
| 64 | COD_ESTADO_COLETA | VARCHAR2(2) | Y |  |  |
| 65 | COD_ESTADO_ENTREGA | VARCHAR2(2) | Y |  |  |
| 66 | PST_ID | NUMBER | Y |  |  |
| 67 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 68 | CHAVE_SAFX51 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX51: (CHAVE_SAFX51)
- IX_SAFX51: (DAT_GRAVACAO)
- IX_SAFX51_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX51_LOTE: (NUM_LOTE)

---

## SAFX52

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INVENTARIO | VARCHAR2(8) | Y |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 5 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 9 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 10 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 11 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 12 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 13 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 14 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 15 | VLR_UNIT | VARCHAR2(18) | Y |  |  |
| 16 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 17 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 18 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 19 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 20 | DESCRICAO_RIPI | VARCHAR2(25) | Y |  |  |
| 21 | VLR_ICMS_MEDIO | VARCHAR2(18) | Y |  |  |
| 22 | VLR_ICMSS_MEDIO | VARCHAR2(18) | Y |  |  |
| 23 | DAT_GRAVACAO | DATE | Y |  |  |
| 24 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 25 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 26 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 27 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 28 | VLR_BASE_ISENTO | VARCHAR2(17) | Y |  |  |
| 29 | VLR_BASE_OUTRAS | VARCHAR2(17) | Y |  |  |
| 30 | VLR_BASE_ICMSS | VARCHAR2(17) | Y |  |  |
| 31 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 32 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 33 | VLR_CUSTO_DCA | VARCHAR2(17) | Y |  |  |
| 34 | IND_PRODUTO_RASTRO | CHAR(1) | Y |  |  |
| 35 | COD_PRODUTO_RASTRO | VARCHAR2(60) | Y |  |  |
| 36 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 37 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 38 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 39 | VLR_TRIB_NC | VARCHAR2(17) | Y |  |  |
| 40 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 41 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 42 | IND_MOT_INV | VARCHAR2(2) | Y |  |  |
| 43 | IND_SIT_TRIB | CHAR(1) | Y |  |  |
| 44 | VLR_IR | VARCHAR2(17) | Y |  |  |
| 45 | VLR_BASE_ICMSS_MEDIO | VARCHAR2(18) | Y |  |  |
| 46 | VLR_FCP_MEDIO | VARCHAR2(18) | Y |  |  |
| 47 | PST_ID | NUMBER | Y |  |  |
| 48 | VLR_RESERVADO1 | VARCHAR2(17) | Y |  |  |
| 49 | VLR_RESERVADO2 | VARCHAR2(17) | Y |  |  |
| 50 | VLR_RESERVADO3 | VARCHAR2(17) | Y |  |  |
| 51 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 52 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 53 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 54 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 55 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 56 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 57 | CHAVE_SAFX52 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX52: (CHAVE_SAFX52)
- IX_SAFX52: (DAT_GRAVACAO)
- IX_SAFX52_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX52_LOTE: (NUM_LOTE)

---

## SAFX520

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INVENTARIO | VARCHAR2(8) | Y |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 5 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 6 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 7 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 8 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 9 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 10 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 11 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 12 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 16 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 17 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 18 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX520 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX520: (CHAVE_SAFX520)
- IX_SAFX520: (DAT_GRAVACAO)
- IX_SAFX520_LOTE: (NUM_LOTE)

---

## SAFX53

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 12 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 13 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 14 | VLR_BRUTO | VARCHAR2(17) | Y |  |  |
| 15 | VLR_IR_RETIDO | VARCHAR2(17) | Y |  |  |
| 16 | VLR_DEDUCAO | VARCHAR2(17) | Y |  |  |
| 17 | ALIQUOTA | VARCHAR2(5) | Y |  |  |
| 18 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 19 | NUM_AP | VARCHAR2(10) | Y |  |  |
| 20 | IND_TIPO_QUITACAO | CHAR(1) | Y |  |  |
| 21 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 22 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 23 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 24 | DATA_INI_COMPET | VARCHAR2(8) | Y |  |  |
| 25 | DATA_FIM_COMPET | VARCHAR2(8) | Y |  |  |
| 26 | DATA_FATO_GERADOR | VARCHAR2(8) | Y |  |  |
| 27 | DATA_VENCTO | VARCHAR2(8) | Y |  |  |
| 28 | COD_CENTRO_RESP | VARCHAR2(20) | Y |  |  |
| 29 | VLR_PREV_PRIVADA | VARCHAR2(17) | Y |  |  |
| 30 | VLR_PENS_ALIMENT | VARCHAR2(17) | Y |  |  |
| 31 | DSC_PENS_ALIMENT | VARCHAR2(50) | Y |  |  |
| 32 | VLR_SALARIO_FAM | VARCHAR2(17) | Y |  |  |
| 33 | VLR_APOSENT_ISENTA | VARCHAR2(17) | Y |  |  |
| 34 | VLR_AJUDA_CUSTO | VARCHAR2(17) | Y |  |  |
| 35 | VLR_PENS_INVALID | VARCHAR2(17) | Y |  |  |
| 36 | VLR_LUCRO_PJ | VARCHAR2(17) | Y |  |  |
| 37 | VLR_OUTROS_SOCIO | VARCHAR2(17) | Y |  |  |
| 38 | VLR_OUTROS_DIRF | VARCHAR2(17) | Y |  |  |
| 39 | DSC_OUTROS_DIRF | VARCHAR2(50) | Y |  |  |
| 40 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 41 | DAT_GRAVACAO | DATE | Y |  |  |
| 42 | VLR_DED_INSS_TERC | VARCHAR2(17) | Y |  |  |
| 43 | VLR_DED_DEP_TERC | VARCHAR2(17) | Y |  |  |
| 44 | VLR_OUTROS_TRIB_EXCL | VARCHAR2(17) | Y |  |  |
| 45 | NUM_REF | VARCHAR2(17) | Y |  |  |
| 46 | NUM_REF_CORRESP | VARCHAR2(2) | Y |  |  |
| 47 | VLR_SALARIO_13 | VARCHAR2(17) | Y |  |  |
| 48 | VLR_TRIBUTO_13 | VARCHAR2(17) | Y |  |  |
| 49 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 50 | TP_RENDIMENTO | VARCHAR2(3) | Y |  |  |
| 51 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |
| 52 | OBSERVACAO | VARCHAR2(50) | Y |  |  |
| 53 | DATA_CANCELAMENTO | VARCHAR2(8) | Y |  |  |
| 54 | IND_CANCELAMENTO | CHAR(1) | Y |  |  |
| 55 | DATA_RETIFICACAO | VARCHAR2(8) | Y |  |  |
| 56 | NUM_VOUCHER | VARCHAR2(50) | Y |  |  |
| 57 | IND_ESTORNO | CHAR(1) | Y |  |  |
| 58 | DATA_ESTORNO | VARCHAR2(8) | Y |  |  |
| 59 | VLR_VOLUNTARIO_COPA | VARCHAR2(17) | Y |  |  |
| 60 | VLR_VOLUNTARIO_COPA_13 | VARCHAR2(17) | Y |  |  |
| 61 | VLR_BOLSA_MEDICO_RESID | VARCHAR2(17) | Y |  |  |
| 62 | VLR_BOLSA_MEDICO_RESID_13 | VARCHAR2(17) | Y |  |  |
| 63 | VLR_DEP_JUD | VARCHAR2(17) | Y |  |  |
| 64 | NUM_CNPJ_OPER | CHAR(14) | Y |  |  |
| 65 | VLR_PG_TITULAR | VARCHAR2(17) | Y |  |  |
| 66 | IND_TIPO_ISENCAO | VARCHAR2(2) | Y |  |  |
| 67 | DSC_RENDIMENTO | VARCHAR2(100) | Y |  |  |
| 68 | COD_NAT_REND | VARCHAR2(9) | Y |  |  |
| 69 | CNPJ_FUND_INV | VARCHAR2(14) | Y |  |  |
| 70 | NOME_FUND_INV | VARCHAR2(150) | Y |  |  |
| 71 | NUM_INSC_PREV | VARCHAR2(14) | Y |  |  |
| 72 | NUM_INSC_FAPI | VARCHAR2(14) | Y |  |  |
| 73 | NOME_FAPI | VARCHAR2(150) | Y |  |  |
| 74 | VLR_FAPI | VARCHAR2(17) | Y |  |  |
| 75 | NUM_INSC_FUNPRESP | VARCHAR2(14) | Y |  |  |
| 76 | NOME_FUNPRESP | VARCHAR2(150) | Y |  |  |
| 77 | VLR_FUNPRESP | VARCHAR2(17) | Y |  |  |
| 78 | NUM_INSC_CONTRIB | VARCHAR2(14) | Y |  |  |
| 79 | NOME_CONTRIB | VARCHAR2(150) | Y |  |  |
| 80 | VLR_CONTRIB | VARCHAR2(17) | Y |  |  |
| 81 | REG_ANS | VARCHAR2(6) | Y |  |  |
| 82 | VLR_BASE_EXIG_SUSP | VARCHAR2(17) | Y |  |  |
| 83 | VLR_RET_IRRF | VARCHAR2(17) | Y |  |  |
| 84 | VLR_DED_IR_EXIG_SUSP | VARCHAR2(17) | Y |  |  |
| 85 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 86 | VLR_BASE_EXIG_SUSP_PIS | VARCHAR2(17) | Y |  |  |
| 87 | VLR_RET_NEFE_IRRF_PIS | VARCHAR2(17) | Y |  |  |
| 88 | VLR_DEP_JUD_PIS | VARCHAR2(17) | Y |  |  |
| 89 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 90 | VLR_BASE_EXIG_SUSP_COFINS | VARCHAR2(17) | Y |  |  |
| 91 | VLR_RET_NEFE_IRRF_COFINS | VARCHAR2(17) | Y |  |  |
| 92 | VLR_DEP_JUD_COFINS | VARCHAR2(17) | Y |  |  |
| 93 | VLR_CSLL | VARCHAR2(17) | Y |  |  |
| 94 | VLR_BASE_EXIG_SUSP_CSLL | VARCHAR2(17) | Y |  |  |
| 95 | VLR_RET_NEFE_IRRF_CSLL | VARCHAR2(17) | Y |  |  |
| 96 | VLR_DEP_JUD_CSLL | VARCHAR2(17) | Y |  |  |
| 97 | CNPJ_SCP | VARCHAR2(14) | Y |  |  |
| 98 | PERCENTUAL_SCP | VARCHAR2(7) | Y |  |  |
| 99 | TP_FONTE_PAGADORA | VARCHAR2(3) | Y |  |  |
| 100 | PST_ID | NUMBER | Y |  |  |
| 101 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 102 | VLR_APOSENT_ISENTA_13 | VARCHAR2(17) | Y |  |  |
| 103 | VLR_JUROS_MORA | VARCHAR2(17) | Y |  |  |
| 104 | VLR_RESG_PREV_COMPL | VARCHAR2(17) | Y |  |  |
| 105 | VLR_REND_S_RET_IR | VARCHAR2(17) | Y |  |  |
| 106 | COD_SERVICO_NAT_REND | VARCHAR2(10) | Y |  |  |
| 107 | DATA_ESCR_CONT | VARCHAR2(8) | Y |  |  |
| 108 | VLR_DESC_SIMPL_MENSAL | VARCHAR2(17) | Y |  |  |
| 109 | VLR_BASE | VARCHAR2(17) | Y |  |  |
| 110 | CHAVE_SAFX53 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX53: (CHAVE_SAFX53)
- IX_SAFX53: (DAT_GRAVACAO)
- IX_SAFX53_LOTE: (NUM_LOTE)

---

## SAFX531

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 12 | IND_TIPO_REND | CHAR(1) | Y |  |  |
| 13 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 14 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 15 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 16 | VLR_DESP_JUD | VARCHAR2(17) | Y |  |  |
| 17 | VLR_DESP_ADVOGADO | VARCHAR2(17) | Y |  |  |
| 18 | DSC_NAT_REND | VARCHAR2(50) | Y |  |  |
| 19 | QTDE_MESES | VARCHAR2(5) | Y |  |  |
| 20 | IND_ORIG_REC | CHAR(1) | Y |  |  |
| 21 | NUM_CNPJ_ORIG_REC | VARCHAR2(14) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | DSC_PROC_JUD | VARCHAR2(50) | Y |  |  |
| 24 | PST_ID | NUMBER | Y |  |  |
| 25 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 26 | VLR_N_RETIDO_IR | VARCHAR2(17) | Y |  |  |
| 27 | VLR_DEP_JUD_IR | VARCHAR2(17) | Y |  |  |
| 28 | VLR_COMP_ANO_CAL_IR | VARCHAR2(17) | Y |  |  |
| 29 | VLR_COMP_ANO_ANT_IR | VARCHAR2(17) | Y |  |  |
| 30 | VLR_REND_EXIG_SUSP_IR | VARCHAR2(17) | Y |  |  |
| 31 | VLR_BASE_SUSP_IR | VARCHAR2(17) | Y |  |  |
| 32 | VLR_BASE_SUSP_CSLL | VARCHAR2(17) | Y |  |  |
| 33 | VLR_N_CSLL | VARCHAR2(17) | Y |  |  |
| 34 | VLR_DEP_CSLL | VARCHAR2(17) | Y |  |  |
| 35 | VLR_BASE_SUSP_COFINS | VARCHAR2(17) | Y |  |  |
| 36 | VLR_N_COFINS | VARCHAR2(17) | Y |  |  |
| 37 | VLR_DEP_COFINS | VARCHAR2(17) | Y |  |  |
| 38 | VLR_BASE_SUSP_PIS_PASEP | VARCHAR2(17) | Y |  |  |
| 39 | VLR_N_PIS_PASEP | VARCHAR2(17) | Y |  |  |
| 40 | VLR_DEP_PIS_PASEP | VARCHAR2(17) | Y |  |  |
| 41 | CHAVE_SAFX531 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX531: (CHAVE_SAFX531)
- IX_SAFX531_LOTE: (NUM_LOTE)

---

## SAFX532

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 12 | IND_TIPO_REND | CHAR(1) | Y |  |  |
| 13 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 14 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 15 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 16 | CPF_CNPJ_ADVOGADO | VARCHAR2(14) | Y |  |  |
| 17 | VLR_DESP_ADVOGADO | VARCHAR2(17) | Y |  |  |
| 18 | DAT_GRAVACAO | DATE | Y |  |  |
| 19 | PST_ID | NUMBER | Y |  |  |
| 20 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 21 | CHAVE_SAFX532 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX532: (CHAVE_SAFX532)
- IX_SAFX532_LOTE: (NUM_LOTE)

---

## SAFX533

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | ANO_COMPETENCIA | VARCHAR2(4) | Y |  |  |
| 12 | MES_COMPETENCIA | VARCHAR2(2) | Y |  |  |
| 13 | IND_IMUNE_ISENTO | VARCHAR2(1) | Y |  |  |
| 14 | VLR_RENDIMENTO | VARCHAR2(17) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 18 | CHAVE_SAFX533 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX533: (CHAVE_SAFX533)
- IX_SAFX533: (DAT_GRAVACAO)
- IX_SAFX533_LOTE: (NUM_LOTE)

---

## SAFX534

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 12 | IND_TIPO_REND | VARCHAR2(1) | Y |  |  |
| 13 | IND_TP_PROC_ADJ | VARCHAR2(1) | Y |  |  |
| 14 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 15 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 16 | NUM_SEQ | VARCHAR2(2) | Y |  |  |
| 17 | IND_TP_DEDUCAO | VARCHAR2(2) | Y |  |  |
| 18 | VLR_DED_EXIG_SUSP | VARCHAR2(17) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX534 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX534: (CHAVE_SAFX534)
- IX_SAFX534_LOTE: (NUM_LOTE)

---

## SAFX535

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 12 | IND_TIPO_REND | VARCHAR2(1) | Y |  |  |
| 13 | IND_TP_PROC_ADJ | VARCHAR2(1) | Y |  |  |
| 14 | NUM_PROC_ADJ | VARCHAR2(21) | Y |  |  |
| 15 | COD_SUSP | VARCHAR2(14) | Y |  |  |
| 16 | NUM_SEQ | VARCHAR2(2) | Y |  |  |
| 17 | CPF_DEP | VARCHAR2(11) | Y |  |  |
| 18 | VLR_DEPEN_SUSP | VARCHAR2(17) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | CHAVE_SAFX535 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX535: (CHAVE_SAFX535)
- IX_SAFX535_LOTE: (NUM_LOTE)

---

## SAFX536

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 11 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 12 | CPF_DEP | VARCHAR2(11) | Y |  |  |
| 13 | VLR_DEPEN | VARCHAR2(17) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX536 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX536: (CHAVE_SAFX536)
- IX_SAFX536_LOTE: (NUM_LOTE)

---

## SAFX537

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | GRP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 5 | ANO_PERIOD_APUR | VARCHAR2(4) | Y |  |  |
| 6 | MES_PERIOD_APUR | VARCHAR2(2) | Y |  |  |
| 7 | DIA_PERIOD_APUR | VARCHAR2(2) | Y |  |  |
| 8 | VLR_DEBITO | VARCHAR2(17) | Y |  |  |
| 9 | IND_BALANCO_REDUC | VARCHAR2(1) | Y |  |  |
| 10 | QTD_QUOTAS | VARCHAR2(2) | Y |  |  |
| 11 | STATUS_OPER | VARCHAR2(1) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX537 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX537: (CHAVE_SAFX537)
- IX_SAFX537_LOTE: (NUM_LOTE)

---

## SAFX538

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 4 | COD_INC | VARCHAR2(6) | Y |  |  |
| 5 | IND_PARCELA | VARCHAR2(3) | Y |  |  |
| 6 | DATA_INI_CRED | VARCHAR2(8) | Y |  |  |
| 7 | DATA_FIM_CRED | VARCHAR2(8) | Y |  |  |
| 8 | IND_BAIXA | VARCHAR2(1) | Y |  |  |
| 9 | DATA_BAIXA | VARCHAR2(8) | Y |  |  |
| 10 | IND_MOTIVO_BAIXA | VARCHAR2(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX538 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX538: (CHAVE_SAFX538)
- IX_SAFX538_DAT_GRAVACAO: (DAT_GRAVACAO)
- IX_SAFX538_LOTE: (NUM_LOTE)

---

## SAFX539

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | GRP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 5 | ANO_PERIOD_APUR | VARCHAR2(4) | Y |  |  |
| 6 | MES_PERIOD_APUR | VARCHAR2(2) | Y |  |  |
| 7 | DIA_PERIOD_APUR | VARCHAR2(2) | Y |  |  |
| 8 | TIPO_PAGAMENTO | VARCHAR2(1) | Y |  |  |
| 9 | SEQ_NUM | VARCHAR2(5) | Y |  |  |
| 10 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 11 | CPF_CNPJ_DARF | VARCHAR2(14) | Y |  |  |
| 12 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 13 | DAT_VENCTO | VARCHAR2(8) | Y |  |  |
| 14 | DAT_QUITACAO | VARCHAR2(8) | Y |  |  |
| 15 | VLR_PRINCIPAL | VARCHAR2(17) | Y |  |  |
| 16 | VLR_MULTA | VARCHAR2(17) | Y |  |  |
| 17 | VLR_JUROS | VARCHAR2(17) | Y |  |  |
| 18 | VLR_OPERACAO | VARCHAR2(17) | Y |  |  |
| 19 | NUM_REFERENCIA | VARCHAR2(17) | Y |  |  |
| 20 | IND_FORM_PEDIDO | VARCHAR2(1) | Y |  |  |
| 21 | COD_PROCESSO | VARCHAR2(24) | Y |  |  |
| 22 | IND_MOT_SUSP | VARCHAR2(2) | Y |  |  |
| 23 | COD_VARA | VARCHAR2(2) | Y |  |  |
| 24 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 25 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 26 | IND_DEPOSITO | VARCHAR2(1) | Y |  |  |
| 27 | NUM_IDENT_DEP | VARCHAR2(20) | Y |  |  |
| 28 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 29 | PST_ID | NUMBER | Y |  |  |
| 30 | DAT_GRAVACAO | DATE | Y |  |  |
| 31 | CHAVE_SAFX539 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX539: (CHAVE_SAFX539)
- IX_SAFX539: (DAT_GRAVACAO)
- IX_SAFX539_LOTE: (NUM_LOTE)

---

## SAFX54

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | COD_OCORRENCIA | VARCHAR2(2) | Y |  |  |
| 5 | DATA_OCORRENCIA | VARCHAR2(8) | Y |  |  |
| 6 | COD_SINDICATO | VARCHAR2(5) | Y |  |  |
| 7 | COD_FUNCAO | VARCHAR2(10) | Y |  |  |
| 8 | DATA_INI_REF | VARCHAR2(8) | Y |  |  |
| 9 | DATA_FIM_REF | VARCHAR2(8) | Y |  |  |
| 10 | DATA_INI_OCORR | VARCHAR2(8) | Y |  |  |
| 11 | DATA_FIM_OCORR | VARCHAR2(8) | Y |  |  |
| 12 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 13 | VLR_OCORRENCIA | VARCHAR2(17) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX54 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX54: (CHAVE_SAFX54)
- IX_SAFX54: (DAT_GRAVACAO)
- IX_SAFX54_LOTE: (NUM_LOTE)

---

## SAFX540

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APUR_INI | VARCHAR2(8) | Y |  |  |
| 4 | DAT_APUR_FIM | VARCHAR2(8) | Y |  |  |
| 5 | COD_PIS_COFINS | VARCHAR2(10) | Y |  |  |
| 6 | COD_RET_FONTE | VARCHAR2(2) | Y |  |  |
| 7 | IND_NAT_REC | VARCHAR2(1) | Y |  |  |
| 8 | IND_COND_PJ_DECL | VARCHAR2(1) | Y |  |  |
| 9 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 10 | VLR_RET_APUR | VARCHAR2(17) | Y |  |  |
| 11 | VLR_RET_UTIL_DED | VARCHAR2(17) | Y |  |  |
| 12 | VLR_RET_UTIL_PER | VARCHAR2(17) | Y |  |  |
| 13 | VLR_RET_UTIL_DCOMP | VARCHAR2(17) | Y |  |  |
| 14 | VLR_RET_DISP | VARCHAR2(17) | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | PST_ID | NUMBER | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | CHAVE_SAFX540 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX540: (CHAVE_SAFX540)
- IX_SAFX540: (DAT_GRAVACAO)
- IX_SAFX540_LOTE: (NUM_LOTE)

---

## SAFX55

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | Y |  |  |
| 4 | COD_DEPEND | VARCHAR2(2) | Y |  |  |
| 5 | DATA_FUNC | VARCHAR2(8) | Y |  |  |
| 6 | COD_TIPO_DEPEND | VARCHAR2(2) | Y |  |  |
| 7 | NOME | VARCHAR2(50) | Y |  |  |
| 8 | DATA_NASC | VARCHAR2(8) | Y |  |  |
| 9 | DATA_FIM_IR | VARCHAR2(8) | Y |  |  |
| 10 | DATA_FIM_SF | VARCHAR2(8) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | NUM_CPF | VARCHAR2(11) | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX55 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX55: (CHAVE_SAFX55)
- IX_SAFX55: (DAT_GRAVACAO)
- IX_SAFX55_LOTE: (NUM_LOTE)

---

## SAFX56

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 2 | DATA_X56 | VARCHAR2(8) | Y |  |  |
| 3 | VLR_INDICE | VARCHAR2(14) | Y |  |  |
| 4 | DATA_FIM | VARCHAR2(8) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX56 | VARCHAR2(4000) | Y | NVL("COD_INDICE",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX56: (CHAVE_SAFX56)
- IX_SAFX56: (DAT_GRAVACAO)
- IX_SAFX56_LOTE: (NUM_LOTE)

---

## SAFX57

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 4 | NORM_DEV | VARCHAR2(1) | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 12 | COD_CLASS_DOC_FIS | VARCHAR2(1) | Y |  |  |
| 13 | DATA_OPER | VARCHAR2(8) | Y |  |  |
| 14 | NUM_LANCTO | VARCHAR2(12) | Y |  |  |
| 15 | IND_DEB_CRED | VARCHAR2(1) | Y |  |  |
| 16 | VLR_LANCTO | VARCHAR2(17) | Y |  |  |
| 17 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 18 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 19 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 20 | HISTORICO | VARCHAR2(100) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | PST_ID | NUMBER | Y |  |  |
| 23 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 24 | CHAVE_SAFX57 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX57: (CHAVE_SAFX57)
- IX_SAFX57_LOTE: (NUM_LOTE)

---

## SAFX58

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_GRP_PROD | VARCHAR2(12) | Y |  |  |
| 2 | VALID_COD_GRUPO | VARCHAR2(8) | Y |  |  |
| 3 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 4 | GRP_PROD_DIC | VARCHAR2(9) | Y |  |  |
| 5 | DAT_GRAVACAO | DATE | Y |  |  |
| 6 | PST_ID | NUMBER | Y |  |  |
| 7 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 8 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 9 | CHAVE_SAFX58 | VARCHAR2(4000) | Y | NVL("COD_GRP_PROD",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX58: (CHAVE_SAFX58)
- IX_SAFX58_LOTE: (NUM_LOTE)

---

## SAFX59

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | NUM_CONHEC | VARCHAR2(12) | Y |  |  |
| 5 | SERIE_CONHEC | VARCHAR2(3) | Y |  |  |
| 6 | SUB_SERIE_CONHEC | VARCHAR2(2) | Y |  |  |
| 7 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | VLR_CONHEC | VARCHAR2(17) | Y |  |  |
| 10 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 11 | COD_TRIBUTACAO | VARCHAR2(1) | Y |  |  |
| 12 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 13 | VLR_ALIQ_ICMS | VARCHAR2(11) | Y |  |  |
| 14 | VLR_ICMS_DEB | VARCHAR2(17) | Y |  |  |
| 15 | VLR_ICMS_CRED | VARCHAR2(17) | Y |  |  |
| 16 | VLR_REDUCAO | VARCHAR2(17) | Y |  |  |
| 17 | DATA_EMISS_CONHEC | VARCHAR2(8) | Y |  |  |
| 18 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 19 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 20 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 21 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 22 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 23 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 24 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 25 | S_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 26 | NUM_LOTE | VARCHAR2(6) | Y |  |  |
| 27 | COD_UF_ORIGEM | VARCHAR2(2) | Y |  |  |
| 28 | COD_UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 29 | DAT_GRAVACAO | DATE | Y |  |  |
| 30 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 31 | VLR_OUTRAS_ICMS | VARCHAR2(17) | Y |  |  |
| 32 | MODALIDADE_FRETE | VARCHAR2(1) | Y |  |  |
| 33 | SITUACAO | VARCHAR2(1) | Y |  |  |
| 34 | COD_DET_OPERACAO | VARCHAR2(5) | Y |  |  |
| 35 | PST_ID | NUMBER | Y |  |  |
| 36 | NUM_LOTE_CARGA | VARCHAR2(80) | Y |  |  |
| 37 | CHAVE_SAFX59 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX59: (CHAVE_SAFX59)
- IX_SAFX59: (DAT_GRAVACAO)
- IX_SAFX59_LOTE: (NUM_LOTE_CARGA)

---

## SAFX60

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_REFERENCIA | VARCHAR2(4) | Y |  |  |
| 4 | MES_REFERENCIA | VARCHAR2(2) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | NUM_TEL | VARCHAR2(15) | Y |  |  |
| 8 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 10 | END_TEL | VARCHAR2(60) | Y |  |  |
| 11 | CID_TEL | VARCHAR2(25) | Y |  |  |
| 12 | LEITURA_INICIAL | VARCHAR2(6) | Y |  |  |
| 13 | LEITURA_FINAL | VARCHAR2(6) | Y |  |  |
| 14 | QTD_PULSO | VARCHAR2(6) | Y |  |  |
| 15 | QTD_CREDITO | VARCHAR2(6) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX60 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX60: (CHAVE_SAFX60)
- IX_SAFX60_LOTE: (NUM_LOTE)

---

## SAFX62

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INVENTARIO | VARCHAR2(8) | Y |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | Y |  |  |
| 5 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 6 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 7 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 8 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 11 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 12 | VLR_UNIT | VARCHAR2(18) | Y |  |  |
| 13 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 14 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 15 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 18 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 19 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_BASE_ISENTO | VARCHAR2(17) | Y |  |  |
| 21 | VLR_BASE_OUTRAS | VARCHAR2(17) | Y |  |  |
| 22 | VLR_BASE_ICMSS | VARCHAR2(17) | Y |  |  |
| 23 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 24 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 25 | PST_ID | NUMBER | Y |  |  |
| 26 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 27 | CHAVE_SAFX62 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX62: (CHAVE_SAFX62)
- IX_SAFX62: (DAT_GRAVACAO)
- IX_SAFX62_COTEPE: (IND_ATO_COTEPE)
- IX_SAFX62_LOTE: (NUM_LOTE)

---

## SAFX63

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | TIP_DOCTO | VARCHAR2(5) | Y |  |  |
| 5 | TIP_MOV_ES | VARCHAR2(1) | Y |  |  |
| 6 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | COD_NAT_OP | VARCHAR2(3) | Y |  |  |
| 15 | COD_UF | VARCHAR2(2) | Y |  |  |
| 16 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 17 | TP_OPERAC | VARCHAR2(6) | Y |  |  |
| 18 | OBS | VARCHAR2(45) | Y |  |  |
| 19 | VLR_DOCFIS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_PROD | VARCHAR2(17) | Y |  |  |
| 21 | COD_TRIB | VARCHAR2(1) | Y |  |  |
| 22 | BASE_INSS | VARCHAR2(17) | Y |  |  |
| 23 | ALIQ_CONTR | VARCHAR2(7) | Y |  |  |
| 24 | VLR_CONTR | VARCHAR2(17) | Y |  |  |
| 25 | DAT_GRAVACAO | DATE | Y |  |  |
| 26 | ALIQ_SENAR | VARCHAR2(7) | Y |  |  |
| 27 | VLR_SENAR | VARCHAR2(17) | Y |  |  |
| 28 | IND_SIT_ESP | VARCHAR2(2) | Y |  |  |
| 29 | IND_TIPO_DEP | VARCHAR2(2) | Y |  |  |
| 30 | NUM_PROC_SIT | VARCHAR2(50) | Y |  |  |
| 31 | VLR_GILRAT | VARCHAR2(17) | Y |  | Informar o valor do GILRAT |
| 32 | ALIQ_GILRAT | VARCHAR2(7) | Y |  | Informar o valor da aliquota do GILRAT |
| 33 | IND_TIPO_AQUIS | VARCHAR2(1) | Y |  | Valores Válidos: 1, 2, 3, 4, 5, 6 |
| 34 | PST_ID | NUMBER | Y |  |  |
| 35 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 36 | IND_TRIB_PRODUTOR_CP | VARCHAR2(1) | Y |  | Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária. 1 - Sobre a comercialização da sua produção; 2 - Sobre a folha de pagamento. Valores Válidos: 1, 2.  |
| 37 | CHAVE_SAFX63 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX63: (CHAVE_SAFX63)
- IX_SAFX63: (DAT_GRAVACAO)
- IX_SAFX63_LOTE: (NUM_LOTE)

---

## SAFX64

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 5 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | COD_TRIBUTACAO | VARCHAR2(1) | Y |  |  |
| 11 | VLR_BASE | VARCHAR2(17) | Y |  |  |
| 12 | ALIQ_TRIBUTO | VARCHAR2(7) | Y |  |  |
| 13 | VLR_AFRMM | VARCHAR2(17) | Y |  |  |
| 14 | VLR_REDUCAO_BASE | VARCHAR2(17) | Y |  |  |
| 15 | COD_DET_OPERACAO | VARCHAR2(5) | Y |  |  |
| 16 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX64 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX64: (CHAVE_SAFX64)
- IX_SAFX64: (DAT_GRAVACAO)
- IX_SAFX64_LOTE: (NUM_LOTE)

---

## SAFX65

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 7 | IND_ETIQ_PROD | CHAR(1) | Y |  |  |
| 8 | COD_ETIQ_PROD | VARCHAR2(60) | Y |  |  |
| 9 | MES_ANO_APUR | VARCHAR2(6) | Y |  |  |
| 10 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 11 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 12 | IND_VENDA | CHAR(1) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | COD_PAIS_DEST | VARCHAR2(3) | Y |  |  |
| 16 | NUM_EMBARQUE | VARCHAR2(12) | Y |  |  |
| 17 | DAT_EMBARQUE | VARCHAR2(8) | Y |  |  |
| 18 | NRO_DESPACHO | VARCHAR2(11) | Y |  |  |
| 19 | VLR_DESP_MOEDA_EST | VARCHAR2(17) | Y |  |  |
| 20 | COD_MOEDA | VARCHAR2(10) | Y |  |  |
| 21 | NRO_REG_EXPORT | VARCHAR2(15) | Y |  |  |
| 22 | CGC_ESTAB_BENEF | VARCHAR2(14) | Y |  |  |
| 23 | NUM_FAT_COMERC | VARCHAR2(12) | Y |  |  |
| 24 | DAT_FAT_COMERC | VARCHAR2(8) | Y |  |  |
| 25 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 26 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 27 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 28 | PESO_LIQUIDO | VARCHAR2(17) | Y |  |  |
| 29 | PESO_BRUTO | VARCHAR2(17) | Y |  |  |
| 30 | DAT_SAIDA | VARCHAR2(8) | Y |  |  |
| 31 | DAT_GRAVACAO | DATE | Y |  |  |
| 32 | PST_ID | NUMBER | Y |  |  |
| 33 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 34 | CHAVE_SAFX65 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX65: (CHAVE_SAFX65)
- IX_SAFX65: (DAT_GRAVACAO)
- IX_SAFX65_LOTE: (NUM_LOTE)

---

## SAFX66

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_GRUPO_SELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_SUB_GRUPO_SELO | VARCHAR2(2) | Y |  |  |
| 5 | COR_SELO | VARCHAR2(15) | Y |  |  |
| 6 | SERIE_SELO | VARCHAR2(3) | Y |  |  |
| 7 | TIPO_OPERACAO | CHAR(1) | Y |  |  |
| 8 | DATA_OPERACAO | VARCHAR2(8) | Y |  |  |
| 9 | NRO_GUIA | VARCHAR2(12) | Y |  |  |
| 10 | DATA_GUIA | VARCHAR2(8) | Y |  |  |
| 11 | QTDE_OPERACAO | VARCHAR2(11) | Y |  |  |
| 12 | NRO_INICIAL | VARCHAR2(12) | Y |  |  |
| 13 | NRO_FINAL | VARCHAR2(12) | Y |  |  |
| 14 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 15 | DATA_VALIDADE | VARCHAR2(8) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX66 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX66: (CHAVE_SAFX66)
- IX_SAFX66: (DAT_GRAVACAO)
- IX_SAFX66_LOTE: (NUM_LOTE)

---

## SAFX67

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_INVENTARIO | VARCHAR2(8) | Y |  |  |
| 4 | COD_GRUPO_SELO | VARCHAR2(2) | Y |  |  |
| 5 | COD_SUBGRUPO_SELO | VARCHAR2(2) | Y |  |  |
| 6 | COR_SELO | VARCHAR2(15) | Y |  |  |
| 7 | SERIE_SELO | VARCHAR2(3) | Y |  |  |
| 8 | QTDE_INVENT_SELO | VARCHAR2(11) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | PST_ID | NUMBER | Y |  |  |
| 11 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 12 | CHAVE_SAFX67 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX67: (CHAVE_SAFX67)
- IX_SAFX67: (DAT_GRAVACAO)
- IX_SAFX67_LOTE: (NUM_LOTE)

---

## SAFX68

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_ENTREGA | VARCHAR2(8) | Y |  |  |
| 4 | NRO_AIDF | VARCHAR2(12) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | COD_DOCTO_CONF | VARCHAR2(5) | Y |  |  |
| 8 | FORMATO_DOC | VARCHAR2(30) | Y |  |  |
| 9 | SERIE_DOC | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOC | VARCHAR2(2) | Y |  |  |
| 11 | NRO_INICIAL | VARCHAR2(12) | Y |  |  |
| 12 | NRO_FINAL | VARCHAR2(12) | Y |  |  |
| 13 | IND_TIPO_FORMA | CHAR(1) | Y |  |  |
| 14 | ESPECIE | VARCHAR2(10) | Y |  |  |
| 15 | QTD_DOCTO | VARCHAR2(12) | Y |  |  |
| 16 | QTD_BLOCOS | VARCHAR2(12) | Y |  |  |
| 17 | QTD_DOCTO_BLOCOS | VARCHAR2(12) | Y |  |  |
| 18 | NRO_VIAS | VARCHAR2(1) | Y |  |  |
| 19 | IND_AIDF_UNICA | CHAR(1) | Y |  |  |
| 20 | NRO_CGF | VARCHAR2(14) | Y |  |  |
| 21 | NRO_FORM_AIDF | VARCHAR2(14) | Y |  |  |
| 22 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 23 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 24 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 25 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 26 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 27 | DAT_GRAVACAO | DATE | Y |  |  |
| 28 | DATA_AUTORIZACAO_AIDF | VARCHAR2(8) | Y |  | Campo criado para atender a DES BH. |
| 29 | VALIDADE_AIDF | VARCHAR2(8) | Y |  | Campo criado para atender a DES BH. |
| 30 | PST_ID | NUMBER | Y |  |  |
| 31 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 32 | CHAVE_SAFX68 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX68: (CHAVE_SAFX68)
- IX_SAFX68: (DAT_GRAVACAO)
- IX_SAFX68_LOTE: (NUM_LOTE)

---

## SAFX69

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_ESTORNO | VARCHAR2(2) | Y |  |  |
| 4 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | IND_INSUMO | CHAR(1) | Y |  |  |
| 7 | COD_INSUMO | VARCHAR2(60) | Y |  |  |
| 8 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 9 | QTDE_CONSUMIDA | VARCHAR2(18) | Y |  |  |
| 10 | FATOR_CONSUMO | VARCHAR2(10) | Y |  |  |
| 11 | VLR_CONS_UNITARIO | VARCHAR2(17) | Y |  |  |
| 12 | VLR_UNITARIO | VARCHAR2(17) | Y |  |  |
| 13 | VLR_TOTAL | VARCHAR2(17) | Y |  |  |
| 14 | ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 15 | VLR_ESTORNO | VARCHAR2(17) | Y |  |  |
| 16 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 17 | VLR_PRODUCAO_MES | VARCHAR2(17) | Y |  |  |
| 18 | VLR_FATURA_MES | VARCHAR2(17) | Y |  |  |
| 19 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 20 | COD_DET_OPERACAO | VARCHAR2(5) | Y |  |  |
| 21 | DAT_GRAVACAO | DATE | Y |  |  |
| 22 | PST_ID | NUMBER | Y |  |  |
| 23 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 24 | CHAVE_SAFX69 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX69: (CHAVE_SAFX69)
- IX_SAFX69: (DAT_GRAVACAO)
- IX_SAFX69_LOTE: (NUM_LOTE)

---

## SAFX70

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 7 | TIPO_OPERACAO | VARCHAR2(2) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 12 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 13 | TIPO_VISTO | VARCHAR2(6) | Y |  |  |
| 14 | QUANT_MOVTO | VARCHAR2(17) | Y |  |  |
| 15 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 16 | TIPO | VARCHAR2(6) | Y |  |  |
| 17 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 18 | REFERENCIA | VARCHAR2(45) | Y |  |  |
| 19 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 20 | ESPECIFICA_MAT | VARCHAR2(1) | Y |  |  |
| 21 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 22 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 23 | GUIA_TRAFEGO | VARCHAR2(40) | Y |  |  |
| 24 | DAT_GRAVACAO | DATE | Y |  |  |
| 25 | NUM_RECEITA | VARCHAR2(15) | Y |  |  |
| 26 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 27 | NUM_REG_EXP_IMP | VARCHAR2(15) | Y |  |  |
| 28 | IND_FIS_JUR_TRANSP | CHAR(1) | Y |  |  |
| 29 | COD_FIS_JUR_TRANSP | VARCHAR2(14) | Y |  |  |
| 30 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 31 | IND_FIS_JUR_ARMAZEM | VARCHAR2(1) | Y |  |  |
| 32 | COD_FIS_JUR_ARMAZEM | VARCHAR2(14) | Y |  |  |
| 33 | IND_TP_FRETE | VARCHAR2(1) | Y |  |  |
| 34 | PST_ID | NUMBER | Y |  |  |
| 35 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 36 | DAT_EMBARQUE | VARCHAR2(8) | Y |  |  |
| 37 | DAT_CONHEC_EMB | VARCHAR2(8) | Y |  |  |
| 38 | IND_FIS_JUR_ENTREGA | VARCHAR2(1) | Y |  |  |
| 39 | COD_FIS_JUR_ENTREGA | VARCHAR2(14) | Y |  |  |
| 40 | IND_FIS_JUR_ADQ | VARCHAR2(1) | Y |  |  |
| 41 | COD_FIS_JUR_ADQ | VARCHAR2(14) | Y |  |  |
| 42 | CHAVE_SAFX70 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX70: (CHAVE_SAFX70)
- IX_SAFX70: (DAT_GRAVACAO)
- IX_SAFX70_LOTE: (NUM_LOTE)

---

## SAFX700

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 7 | TIPO_OPERACAO | VARCHAR2(2) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 12 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 13 | NUM_FAB_LOTE | VARCHAR2(50) | Y |  |  |
| 14 | QTD_LOTE | VARCHAR2(17) | Y |  |  |
| 15 | DAT_FABRIC | VARCHAR2(8) | Y |  |  |
| 16 | DAT_VALIDADE | VARCHAR2(8) | Y |  |  |
| 17 | DAT_GRAVACAO | DATE | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX700 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX700: (CHAVE_SAFX700)
- IX_SAFX700_LOTE: (NUM_LOTE)

---

## SAFX701

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | IDENT_FIS_JUR | CHAR(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 12 | IDENT_VOO | VARCHAR2(10) | Y |  |  |
| 13 | UF_DOCFIS_EMIT | VARCHAR2(2) | Y |  |  |
| 14 | QTD_PASSAG_VOO | VARCHAR2(4) | Y |  |  |
| 15 | IDENT_CONEXAO | VARCHAR2(10) | Y |  |  |
| 16 | IND_CLASSE | CHAR(1) | Y |  |  |
| 17 | NUM_POLTRONA | VARCHAR2(4) | Y |  |  |
| 18 | CPF_PARTICIPANTE | VARCHAR2(11) | Y |  |  |
| 19 | NOME_PARTICIPANTE | VARCHAR2(100) | Y |  |  |
| 20 | PST_ID | NUMBER | Y |  |  |
| 21 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | CHAVE_SAFX701 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX701: (CHAVE_SAFX701)
- IX_SAFX701_LOTE: (NUM_LOTE)

---

## SAFX702

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | IDENT_FIS_JUR | CHAR(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 12 | IDENT_VOO | VARCHAR2(10) | Y |  |  |
| 13 | UF_ORIGEM | VARCHAR2(2) | Y |  |  |
| 14 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 15 | COD_MUNICIPIO_ORIG | VARCHAR2(5) | Y |  |  |
| 16 | COD_MUNICIPIO_DEST | VARCHAR2(5) | Y |  |  |
| 17 | QTD_PASSAG_DEST | VARCHAR2(4) | Y |  |  |
| 18 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 19 | VLR_TAXA | VARCHAR2(17) | Y |  |  |
| 20 | VLR_DESC | VARCHAR2(17) | Y |  |  |
| 21 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 22 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 23 | COD_IATA_ORIG | VARCHAR2(3) | Y |  |  |
| 24 | COD_IATA_DEST | VARCHAR2(3) | Y |  |  |
| 25 | PST_ID | NUMBER | Y |  |  |
| 26 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 27 | DAT_GRAVACAO | DATE | Y |  |  |
| 28 | CHAVE_SAFX702 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX702: (CHAVE_SAFX702)
- IX_SAFX702_LOTE: (NUM_LOTE)

---

## SAFX71

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_OBRIGACAO | VARCHAR2(2) | Y |  |  |
| 2 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 4 | IND_PSICOTROPICO | CHAR(1) | Y |  |  |
| 5 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 6 | DSC_PROD | VARCHAR2(50) | Y |  |  |
| 7 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 8 | COD_VENDA | VARCHAR2(35) | Y |  |  |
| 9 | COD_CLASS_PRD | VARCHAR2(15) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | NUM_REGISTRO | VARCHAR2(10) | Y |  |  |
| 12 | DSC_CONCENTRACAO | VARCHAR2(15) | Y |  |  |
| 13 | DSC_FORMULACAO | VARCHAR2(40) | Y |  |  |
| 14 | DSC_ORG_FED | VARCHAR2(40) | Y |  |  |
| 15 | PESO_VOLUME | VARCHAR2(20) | Y |  |  |
| 16 | COD_ING_ATIVO_PRIN | VARCHAR2(35) | Y |  |  |
| 17 | MARCA_COMERCIAL | VARCHAR2(6) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX71 | VARCHAR2(4000) | Y | NVL("TIPO_OBRIGACAO",'@')\|\|NVL("IND_PRODUTO",'@... |  |

**Indexes**:
- IX_CHAVE_SAFX71: (CHAVE_SAFX71)
- IX_SAFX71: (DAT_GRAVACAO)
- IX_SAFX71_LOTE: (NUM_LOTE)

---

## SAFX72

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 4 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 6 | QUANT_SALDO | VARCHAR2(17) | Y |  |  |
| 7 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 8 | TIPO | VARCHAR2(6) | Y |  |  |
| 9 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 10 | ESPECIFICA_MAT | VARCHAR2(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX72 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX72: (CHAVE_SAFX72)
- IX_SAFX72: (DAT_GRAVACAO)
- IX_SAFX72_LOTE: (NUM_LOTE)

---

## SAFX75

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 5 | NUM_REFERENCIA | VARCHAR2(15) | Y |  |  |
| 6 | DT_INI_APURACAO | VARCHAR2(8) | Y |  |  |
| 7 | VLR_RECEITA_ACUM | VARCHAR2(17) | Y |  |  |
| 8 | DATA_VENCTO | VARCHAR2(8) | Y |  |  |
| 9 | VLR_PRINCIPAL | VARCHAR2(17) | Y |  |  |
| 10 | VLR_MULTA | VARCHAR2(17) | Y |  |  |
| 11 | VLR_JUROS | VARCHAR2(17) | Y |  |  |
| 12 | VLR_TOTAL | VARCHAR2(17) | Y |  |  |
| 13 | DATA_PAGTO | VARCHAR2(8) | Y |  |  |
| 14 | NUM_PROCESSO_ADM | VARCHAR2(24) | Y |  |  |
| 15 | VLR_BASE | VARCHAR2(17) | Y |  |  |
| 16 | ALIQ_TRIBUTO | VARCHAR2(7) | Y |  |  |
| 17 | OBSERVACAO | VARCHAR2(180) | Y |  |  |
| 18 | NRO_BANCO | VARCHAR2(3) | Y |  |  |
| 19 | NRO_AGENCIA | VARCHAR2(5) | Y |  |  |
| 20 | NRO_PAGTO | VARCHAR2(14) | Y |  |  |
| 21 | SIT_PROCESSO | VARCHAR2(6) | Y |  |  |
| 22 | DAT_GRAVACAO | DATE | Y |  |  |
| 23 | DATA_ENV_BCO | VARCHAR2(8) | Y |  |  |
| 24 | AUTENT_BANCARIA | VARCHAR2(50) | Y |  |  |
| 25 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 26 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 27 | NUM_QUOTA | VARCHAR2(2) | Y |  |  |
| 28 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 29 | DATA_APURACAO_COMPL | VARCHAR2(8) | Y |  |  |
| 30 | NRO_REFERENCIA_COMPL | VARCHAR2(15) | Y |  |  |
| 31 | PST_ID | NUMBER | Y |  |  |
| 32 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 33 | CHAVE_SAFX75 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX75: (CHAVE_SAFX75)
- IX_SAFX75: (DAT_GRAVACAO)
- IX_SAFX75_LOTE: (NUM_LOTE)

---

## SAFX76

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 7 | IND_ETIQ_PROD | CHAR(1) | Y |  |  |
| 8 | COD_ETIQ_PROD | VARCHAR2(60) | Y |  |  |
| 9 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 10 | NUM_EMBARQUE | VARCHAR2(12) | Y |  |  |
| 11 | DATA_EMBARQUE | VARCHAR2(8) | Y |  |  |
| 12 | NUM_DESPACHO | VARCHAR2(11) | Y |  |  |
| 13 | VLR_DESPACHO | VARCHAR2(17) | Y |  |  |
| 14 | COD_MOEDA | VARCHAR2(10) | Y |  |  |
| 15 | NUM_REG_EXP | VARCHAR2(15) | Y |  |  |
| 16 | IND_FIS_JUR_AQ | CHAR(1) | Y |  |  |
| 17 | COD_FIS_JUR_AQ | VARCHAR2(14) | Y |  |  |
| 18 | IND_FIS_JUR_VE | CHAR(1) | Y |  |  |
| 19 | COD_FIS_JUR_VE | VARCHAR2(14) | Y |  |  |
| 20 | IND_TOTAL_PARCIAL | CHAR(1) | Y |  |  |
| 21 | VLR_PARCIAL | VARCHAR2(17) | Y |  |  |
| 22 | COD_PAIS_DEST | VARCHAR2(3) | Y |  |  |
| 23 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 24 | IND_COMPRA_VENDA | CHAR(1) | Y |  |  |
| 25 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 26 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 27 | DAT_GRAVACAO | DATE | Y |  |  |
| 28 | PST_ID | NUMBER | Y |  |  |
| 29 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 30 | CHAVE_SAFX76 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX76: (CHAVE_SAFX76)
- IX_SAFX76: (DAT_GRAVACAO)
- IX_SAFX76_LOTE: (NUM_LOTE)

---

## SAFX77

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_CONTROLE | CHAR(1) | Y |  |  |
| 4 | NUM_CONTROLE | VARCHAR2(15) | Y |  |  |
| 5 | IND_COD_CONTROLE | CHAR(1) | Y |  |  |
| 6 | NUM_COD_CONTROLE | VARCHAR2(60) | Y |  |  |
| 7 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | AGE_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 16 | ANO_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 17 | NUM_ATO_CONCES | VARCHAR2(6) | Y |  |  |
| 18 | DIG_VER_ATO_CONCES | CHAR(1) | Y |  |  |
| 19 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 20 | PESO_BRUTO | VARCHAR2(17) | Y |  |  |
| 21 | PESO_LIQUIDO | VARCHAR2(17) | Y |  |  |
| 22 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 23 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 24 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 25 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 26 | VLR_OUTRAS | VARCHAR2(17) | Y |  |  |
| 27 | VLR_TOT_MERC_EMB | VARCHAR2(17) | Y |  |  |
| 28 | VLR_TOT_MERC | VARCHAR2(17) | Y |  |  |
| 29 | VLR_TOT_MERC_DOLAR | VARCHAR2(17) | Y |  |  |
| 30 | IND_MERCADO | CHAR(1) | Y |  |  |
| 31 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 32 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 33 | COD_MOEDA | VARCHAR2(10) | Y |  |  |
| 34 | NUM_DECL_IMPORT | VARCHAR2(12) | Y |  |  |
| 35 | DATA_DECL_IMPORT | VARCHAR2(8) | Y |  |  |
| 36 | OBS_COMPLEMENTAR | VARCHAR2(200) | Y |  |  |
| 37 | DAT_GRAVACAO | DATE | Y |  |  |
| 38 | PST_ID | NUMBER | Y |  |  |
| 39 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 40 | CHAVE_SAFX77 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX77: (CHAVE_SAFX77)
- IX_SAFX77: (DAT_GRAVACAO)
- IX_SAFX77_LOTE: (NUM_LOTE)

---

## SAFX78

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_CONTROLE | CHAR(1) | Y |  |  |
| 4 | NUM_CONTROLE | VARCHAR2(15) | Y |  |  |
| 5 | IND_COD_CONTROLE | CHAR(1) | Y |  |  |
| 6 | NUM_COD_CONTROLE | VARCHAR2(60) | Y |  |  |
| 7 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 12 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | AGE_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 16 | ANO_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 17 | NUM_ATO_CONCES | VARCHAR2(6) | Y |  |  |
| 18 | DIG_VER_ATO_CONCES | CHAR(1) | Y |  |  |
| 19 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 20 | PESO_BRUTO | VARCHAR2(17) | Y |  |  |
| 21 | PESO_LIQUIDO | VARCHAR2(17) | Y |  |  |
| 22 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 23 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 24 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 25 | VLR_COMISSAO | VARCHAR2(17) | Y |  |  |
| 26 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 27 | VLR_DEDUCOES | VARCHAR2(17) | Y |  |  |
| 28 | VLR_TOT_MERC_EMB | VARCHAR2(17) | Y |  |  |
| 29 | VLR_TOT_MERC | VARCHAR2(17) | Y |  |  |
| 30 | VLR_TOT_MERC_DOLAR | VARCHAR2(17) | Y |  |  |
| 31 | IND_MERCADO | CHAR(1) | Y |  |  |
| 32 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 33 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 34 | COD_MOEDA | VARCHAR2(10) | Y |  |  |
| 35 | NUM_REG_EXP | VARCHAR2(15) | Y |  |  |
| 36 | DATA_EMBARQUE | VARCHAR2(8) | Y |  |  |
| 37 | NUM_DESPACHO | VARCHAR2(11) | Y |  |  |
| 38 | VLR_DESPACHO | VARCHAR2(17) | Y |  |  |
| 39 | OBS_COMPLEMENTAR | VARCHAR2(200) | Y |  |  |
| 40 | DAT_GRAVACAO | DATE | Y |  |  |
| 41 | PST_ID | NUMBER | Y |  |  |
| 42 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 43 | CHAVE_SAFX78 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX78: (CHAVE_SAFX78)
- IX_SAFX78: (DAT_GRAVACAO)
- IX_SAFX78_LOTE: (NUM_LOTE)

---

## SAFX79

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PAG_REC | CHAR(1) | Y |  |  |
| 4 | DAT_SALDO | VARCHAR2(8) | Y |  |  |
| 5 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 6 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 7 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 8 | VLR_SALDO_CONTAB | VARCHAR2(17) | Y |  |  |
| 9 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX79 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX79: (CHAVE_SAFX79)
- IX_SAFX79: (DAT_GRAVACAO)
- IX_SAFX79_LOTE: (NUM_LOTE)

---

## SAFX80

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_SALDO | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 6 | VLR_SALDO_CONT_ANT | VARCHAR2(19) | Y |  |  |
| 7 | IND_DEB_CRED_ANT | CHAR(1) | Y |  |  |
| 8 | VLR_TOT_DEB | VARCHAR2(19) | Y |  |  |
| 9 | VLR_TOT_CRED | VARCHAR2(19) | Y |  |  |
| 10 | VLR_SALDO_CONT_ATU | VARCHAR2(19) | Y |  |  |
| 11 | IND_DEB_CRED_ATU | CHAR(1) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | IDENTIF_SALDO | VARCHAR2(128) | Y |  |  |
| 14 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX80 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX80: (CHAVE_SAFX80)
- IX_SAFX80: (DAT_GRAVACAO)
- IX_SAFX80_LOTE: (NUM_LOTE)

---

## SAFX81

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_SALDO | VARCHAR2(8) | Y |  |  |
| 4 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 5 | COD_SUB_CONTA | VARCHAR2(70) | Y |  |  |
| 6 | VLR_SALDO_CONT_ANT | VARCHAR2(17) | Y |  |  |
| 7 | IND_DEB_CRED_ANT | CHAR(1) | Y |  |  |
| 8 | VLR_TOT_DEB | VARCHAR2(17) | Y |  |  |
| 9 | VLR_TOT_CRED | VARCHAR2(17) | Y |  |  |
| 10 | VLR_SALDO_CONT_ATU | VARCHAR2(17) | Y |  |  |
| 11 | IND_DEB_CRED_ATU | CHAR(1) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX81 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX81: (CHAVE_SAFX81)
- IX_SAFX81: (DAT_GRAVACAO)
- IX_SAFX81_LOTE: (NUM_LOTE)

---

## SAFX82

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_CIAP | VARCHAR2(12) | Y |  |  |
| 4 | ANO_REGISTRO | VARCHAR2(4) | Y |  |  |
| 5 | DAT_OPER | VARCHAR2(8) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 10 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 11 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 12 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 13 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 14 | DESCR_BEM | VARCHAR2(50) | Y |  |  |
| 15 | COMPL_DESCR_BEM | VARCHAR2(50) | Y |  |  |
| 16 | MODELO_BEM | VARCHAR2(30) | Y |  |  |
| 17 | SERIE_BEM | VARCHAR2(30) | Y |  |  |
| 18 | PLAQUETA_BEM | VARCHAR2(30) | Y |  |  |
| 19 | VLR_AQUIS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_CRED_ICMS | VARCHAR2(17) | Y |  |  |
| 21 | NUM_LRE | VARCHAR2(6) | Y |  |  |
| 22 | PAG_LRE | VARCHAR2(6) | Y |  |  |
| 23 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 24 | COD_INC | VARCHAR2(6) | Y |  |  |
| 25 | ST_ATIVO | CHAR(1) | Y |  |  |
| 26 | TIPO_MOV | VARCHAR2(3) | Y |  |  |
| 27 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 28 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 29 | IND_AQUIS_TRIB | CHAR(1) | Y |  |  |
| 30 | NUM_OFICIAL_CIAP | VARCHAR2(12) | Y |  |  |
| 31 | NUM_MESES_ESTORNO | VARCHAR2(3) | Y |  |  |
| 32 | QTD_BENS_ALIENADOS | VARCHAR2(17) | Y |  |  |
| 33 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 34 | IND_LEI | CHAR(1) | Y |  |  |
| 35 | VLR_CRED_DIF_ALIQ | VARCHAR2(17) | Y |  |  |
| 36 | VLR_CRED_ICMS_CONV | VARCHAR2(17) | Y |  |  |
| 37 | VLR_CRDIFALIQ_CONV | VARCHAR2(17) | Y |  |  |
| 38 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 39 | NORM_DEV | CHAR(1) | Y |  |  |
| 40 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 41 | DAT_GRAVACAO | DATE | Y |  |  |
| 42 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 43 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 44 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 45 | COD_PROJETO | VARCHAR2(20) | Y |  |  |
| 46 | VLR_ICMS_FRETE | VARCHAR2(17) | Y |  |  |
| 47 | VLR_DIFAL_FRETE | VARCHAR2(17) | Y |  |  |
| 48 | VLR_ICMS_FRETE_CV | VARCHAR2(17) | Y |  |  |
| 49 | VLR_DIFAL_FRETE_CV | VARCHAR2(17) | Y |  |  |
| 50 | DAT_INTERN_AM | VARCHAR2(8) | Y |  |  |
| 51 | LOCAL_BEM | VARCHAR2(150) | Y |  |  |
| 52 | DAT_EMISSAO | VARCHAR2(8) | Y |  |  |
| 53 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 54 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 55 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 56 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 57 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 58 | VLR_ICMSS | VARCHAR2(17) | Y |  |  |
| 59 | VLR_ICMSS_CONV | VARCHAR2(17) | Y |  |  |
| 60 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 61 | PST_ID | NUMBER | Y |  |  |
| 62 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 63 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 64 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 65 | CHAVE_SAFX82 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX82: (CHAVE_SAFX82)
- IX_SAFX82: (DAT_GRAVACAO)
- IX_SAFX82_LOTE: (NUM_LOTE)

---

## SAFX83

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_CIAP | VARCHAR2(12) | Y |  |  |
| 4 | DAT_OPER | VARCHAR2(8) | Y |  |  |
| 5 | TIPO_MOV | VARCHAR2(3) | Y |  |  |
| 6 | ANO_REGISTRO | VARCHAR2(4) | Y |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | MODELO_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 12 | DAT_SAIDA_BEM | VARCHAR2(8) | Y |  |  |
| 13 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 14 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 15 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 16 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 17 | VLR_ALIENACAO | VARCHAR2(17) | Y |  |  |
| 18 | VLR_ESTORNO_ICMS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_CRED_APROP | VARCHAR2(17) | Y |  |  |
| 20 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 21 | VLR_BASE_TRIB | VARCHAR2(17) | Y |  |  |
| 22 | VLR_BASE_ISENTAS | VARCHAR2(17) | Y |  |  |
| 23 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 24 | COD_INC | VARCHAR2(6) | Y |  |  |
| 25 | QTD_BENS_ALIENADOS | VARCHAR2(17) | Y |  |  |
| 26 | IND_LEI | CHAR(1) | Y |  |  |
| 27 | DAT_GRAVACAO | DATE | Y |  |  |
| 28 | TIPO_BAIXA | CHAR(1) | Y |  |  |
| 29 | VLR_ICMS_BX | VARCHAR2(17) | Y |  |  |
| 30 | VLR_DIFAL_BX | VARCHAR2(17) | Y |  |  |
| 31 | VLR_ICMS_FRETE_BX | VARCHAR2(17) | Y |  |  |
| 32 | VLR_DIFAL_FRETE_BX | VARCHAR2(17) | Y |  |  |
| 33 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 34 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 35 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 36 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 37 | VLR_ICMSS_BX | VARCHAR2(17) | Y |  |  |
| 38 | PST_ID | NUMBER | Y |  |  |
| 39 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 40 | CHAVE_SAFX83 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX83: (CHAVE_SAFX83)
- IX_SAFX83: (DAT_GRAVACAO)
- IX_SAFX83_LOTE: (NUM_LOTE)

---

## SAFX84

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | VLR_TOT_OP_ISENTAS | VARCHAR2(17) | Y |  |  |
| 5 | VLR_TOT_OP_SAIDAS | VARCHAR2(17) | Y |  |  |
| 6 | COEFICIENTE | VARCHAR2(16) | Y |  |  |
| 7 | VLR_BASE_ESTORNO | VARCHAR2(17) | Y |  |  |
| 8 | VLR_FRACAO_MENSAL | VARCHAR2(11) | Y |  |  |
| 9 | VLR_EST_OP_ISENTAS | VARCHAR2(17) | Y |  |  |
| 10 | VLR_EST_OP_SAIDAS | VARCHAR2(17) | Y |  |  |
| 11 | VLR_TOT_EST_MENSAL | VARCHAR2(17) | Y |  |  |
| 12 | VLR_TOT_TRANS_CRED | VARCHAR2(17) | Y |  |  |
| 13 | VLR_TOT_TRANS_DEB | VARCHAR2(17) | Y |  |  |
| 14 | DAT_GRAVACAO | DATE | Y |  |  |
| 15 | PST_ID | NUMBER | Y |  |  |
| 16 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 17 | CHAVE_SAFX84 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX84: (CHAVE_SAFX84)
- IX_SAFX84: (DAT_GRAVACAO)
- IX_SAFX84_LOTE: (NUM_LOTE)

---

## SAFX85

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | ANO_REGISTRO | VARCHAR2(4) | Y |  |  |
| 4 | NUM_CIAP | VARCHAR2(12) | Y |  |  |
| 5 | DAT_OPER | VARCHAR2(8) | Y |  |  |
| 6 | VLR_CRED_ICMS | VARCHAR2(17) | Y |  |  |
| 7 | VLR_ESTORNO_ICMS | VARCHAR2(17) | Y |  |  |
| 8 | VLR_BASE_ESTORNO | VARCHAR2(17) | Y |  |  |
| 9 | VLR_BASE_EST_SALDO | VARCHAR2(17) | Y |  |  |
| 10 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 11 | COD_INC | VARCHAR2(6) | Y |  |  |
| 12 | DAT_GRAVACAO | DATE | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX85 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX85: (CHAVE_SAFX85)
- IX_SAFX85: (DAT_GRAVACAO)
- IX_SAFX85_LOTE: (NUM_LOTE)

---

## SAFX86

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 4 | VLR_TOT_OP_ISENTAS | VARCHAR2(17) | Y |  |  |
| 5 | VLR_TOT_OP_SAIDAS | VARCHAR2(17) | Y |  |  |
| 6 | FAT_MENSAL | VARCHAR2(16) | Y |  |  |
| 7 | VLR_CRED_ENTRADA | VARCHAR2(17) | Y |  |  |
| 8 | VLR_TOT_EST_MENSAL | VARCHAR2(17) | Y |  |  |
| 9 | VLR_TOT_TRANS_CRED | VARCHAR2(17) | Y |  |  |
| 10 | VLR_TOT_TRANS_DEB | VARCHAR2(17) | Y |  |  |
| 11 | VLR_TOT_EST_ISENTAS | VARCHAR2(17) | Y |  |  |
| 12 | IND_LEI | CHAR(1) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX86 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX86: (CHAVE_SAFX86)
- IX_SAFX86: (DAT_GRAVACAO)
- IX_SAFX86_LOTE: (NUM_LOTE)

---

## SAFX87

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_CIAP | VARCHAR2(12) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | FAT_MENSAL | VARCHAR2(16) | Y |  |  |
| 6 | VLR_CRED_ENTRADA | VARCHAR2(17) | Y |  |  |
| 7 | VLR_TOT_EST_MENSAL | VARCHAR2(17) | Y |  |  |
| 8 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 9 | COD_INC | VARCHAR2(6) | Y |  |  |
| 10 | IND_LEI | CHAR(1) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 14 | CHAVE_SAFX87 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX87: (CHAVE_SAFX87)
- IX_SAFX87: (DAT_GRAVACAO)
- IX_SAFX87_LOTE: (NUM_LOTE)

---

## SAFX88

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | NUM_CIAP | VARCHAR2(12) | Y |  |  |
| 4 | DAT_APURACAO | VARCHAR2(8) | Y |  |  |
| 5 | FAT_MENSAL | VARCHAR2(16) | Y |  |  |
| 6 | VLR_CRED_ENTRADA | VARCHAR2(17) | Y |  |  |
| 7 | VLR_TOT_EST_MENSAL | VARCHAR2(17) | Y |  |  |
| 8 | VLR_DEDUCAO_EST | VARCHAR2(17) | Y |  |  |
| 9 | VLR_SALDO_FINAL | VARCHAR2(17) | Y |  |  |
| 10 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 11 | COD_INC | VARCHAR2(6) | Y |  |  |
| 12 | IND_LEI | CHAR(1) | Y |  |  |
| 13 | DAT_GRAVACAO | DATE | Y |  |  |
| 14 | PST_ID | NUMBER | Y |  |  |
| 15 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 16 | CHAVE_SAFX88 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX88: (CHAVE_SAFX88)
- IX_SAFX88: (DAT_GRAVACAO)
- IX_SAFX88_LOTE: (NUM_LOTE)

---

## SAFX90

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 4 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 5 | IND_TRIB_INCENT | VARCHAR2(1) | Y |  |  |
| 6 | COD_CLASSE_OPER | VARCHAR2(1) | Y |  |  |
| 7 | DAT_MOVTO | VARCHAR2(8) | Y |  |  |
| 8 | TP_ORIGEM | VARCHAR2(2) | Y |  |  |
| 9 | DOCTO_ORIGEM | VARCHAR2(25) | Y |  |  |
| 10 | REF_ORIGEM | VARCHAR2(5) | Y |  |  |
| 11 | COD_AREA_NEGOC | VARCHAR2(10) | Y |  |  |
| 12 | COD_UNID_NEGOC | VARCHAR2(20) | Y |  |  |
| 13 | COD_CENTRO_RESP | VARCHAR2(20) | Y |  |  |
| 14 | COD_LOCALIDADE | VARCHAR2(5) | Y |  |  |
| 15 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 16 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 17 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 18 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 19 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 20 | IND_MERCADO | VARCHAR2(1) | Y |  |  |
| 21 | IND_DEB_CRED | VARCHAR2(1) | Y |  |  |
| 22 | COD_INDICE_CORREC | VARCHAR2(10) | Y |  |  |
| 23 | VLR_MOVTO | VARCHAR2(17) | Y |  |  |
| 24 | VLR_PRINC_REC | VARCHAR2(17) | Y |  |  |
| 25 | VLR_JUROS | VARCHAR2(17) | Y |  |  |
| 26 | VLR_MULTA_MORAT | VARCHAR2(17) | Y |  |  |
| 27 | VLR_MULTA_INFRAC | VARCHAR2(17) | Y |  |  |
| 28 | VLR_CORRECAO | VARCHAR2(17) | Y |  |  |
| 29 | VLR_DEDUCOES | VARCHAR2(17) | Y |  |  |
| 30 | VLR_COMPENS | VARCHAR2(17) | Y |  |  |
| 31 | VLR_TOT_REC | VARCHAR2(17) | Y |  |  |
| 32 | DAT_INI_COMPET | VARCHAR2(8) | Y |  |  |
| 33 | DAT_FIM_COMPET | VARCHAR2(8) | Y |  |  |
| 34 | DAT_APURAC_INI | VARCHAR2(8) | Y |  |  |
| 35 | DAT_APURAC_FIM | VARCHAR2(8) | Y |  |  |
| 36 | DAT_VENCTO | VARCHAR2(8) | Y |  |  |
| 37 | VLR_IND_ATUALIZ | VARCHAR2(9) | Y |  |  |
| 38 | VLR_RECOLH | VARCHAR2(17) | Y |  |  |
| 39 | DAT_RECOLH | VARCHAR2(8) | Y |  |  |
| 40 | ORG_ARRECAD | VARCHAR2(30) | Y |  |  |
| 41 | OBS | VARCHAR2(320) | Y |  |  |
| 42 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 43 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 44 | COD_ARREC_ESTAD | VARCHAR2(4) | Y |  |  |
| 45 | COD_ARREC_MUNIC | VARCHAR2(4) | Y |  |  |
| 46 | IND_PROD_PROPRIO | CHAR(1) | Y |  |  |
| 47 | DAT_GRAVACAO | DATE | Y |  |  |
| 48 | PST_ID | NUMBER | Y |  |  |
| 49 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 50 | CHAVE_SAFX90 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX90: (CHAVE_SAFX90)
- IX_SAFX90: (DAT_GRAVACAO)
- IX_SAFX90_LOTE: (NUM_LOTE)

---

## SAFX91

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DAT_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 5 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 10 | VLR_ALIQ_ISS | VARCHAR2(7) | Y |  |  |
| 11 | VLR_ISS | VARCHAR2(17) | Y |  |  |
| 12 | VLR_SALDO_ISS | VARCHAR2(17) | Y |  |  |
| 13 | DAT_EMISSAO | VARCHAR2(8) | Y |  |  |
| 14 | NUM_CONTRATO | VARCHAR2(14) | Y |  |  |
| 15 | COD_MUNIC_ISS | VARCHAR2(7) | Y |  |  |
| 16 | COD_OBRA | VARCHAR2(15) | Y |  |  |
| 17 | DAT_APROP_ABAT | VARCHAR2(8) | Y |  |  |
| 18 | IND_SITUACAO_ABAT | CHAR(1) | Y |  |  |
| 19 | DAT_GRAVACAO | DATE | Y |  |  |
| 20 | IND_COMPROVANTE | CHAR(1) | Y |  |  |
| 21 | PST_ID | NUMBER | Y |  |  |
| 22 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 23 | CHAVE_SAFX91 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX91: (CHAVE_SAFX91)
- IX_SAFX91: (DAT_GRAVACAO)
- IX_SAFX91_LOTE: (NUM_LOTE)

---

## SAFX92

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 4 | NORM_DEV | CHAR(1) | Y |  |  |
| 5 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 6 | IDENT_FIS_JUR | CHAR(1) | Y |  |  |
| 7 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 12 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 13 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 16 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 17 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 18 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 19 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 20 | DATA_SAIDA_REC | VARCHAR2(8) | Y |  |  |
| 21 | INSC_ESTAD_SUBSTIT | VARCHAR2(14) | Y |  |  |
| 22 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 23 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 24 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 25 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 26 | VLR_OUTRAS | VARCHAR2(17) | Y |  |  |
| 27 | VLR_BASE_DIF_FRETE | VARCHAR2(17) | Y |  |  |
| 28 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 29 | CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 30 | SITUACAO | CHAR(1) | Y |  |  |
| 31 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 32 | VLR_NOTA_CONV | VARCHAR2(18) | Y |  |  |
| 33 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 34 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 35 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 36 | DIF_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 37 | OBS_ICMS | VARCHAR2(45) | Y |  |  |
| 38 | COD_APUR_ICMS | VARCHAR2(5) | Y |  |  |
| 39 | VLR_ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 40 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 41 | OBS_IPI | VARCHAR2(45) | Y |  |  |
| 42 | COD_APUR_IPI | VARCHAR2(5) | Y |  |  |
| 43 | VLR_ALIQ_IR | VARCHAR2(7) | Y |  |  |
| 44 | VLR_IR | VARCHAR2(17) | Y |  |  |
| 45 | VLR_ALIQ_ISS | VARCHAR2(7) | Y |  |  |
| 46 | VLR_ISS | VARCHAR2(17) | Y |  |  |
| 47 | VLR_ALIQ_SUB_ICMS | VARCHAR2(7) | Y |  |  |
| 48 | VLR_SUBST_ICMS | VARCHAR2(17) | Y |  |  |
| 49 | OBS_SUBST_ICMS | VARCHAR2(45) | Y |  |  |
| 50 | COD_APUR_SUB_ICMS | VARCHAR2(5) | Y |  |  |
| 51 | BASE_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 52 | BASE_ISEN_ICMS | VARCHAR2(17) | Y |  |  |
| 53 | BASE_OUTR_ICMS | VARCHAR2(17) | Y |  |  |
| 54 | BASE_REDU_ICMS | VARCHAR2(17) | Y |  |  |
| 55 | BASE_TRIB_IPI | VARCHAR2(17) | Y |  |  |
| 56 | BASE_ISEN_IPI | VARCHAR2(17) | Y |  |  |
| 57 | BASE_OUTR_IPI | VARCHAR2(17) | Y |  |  |
| 58 | BASE_REDU_IPI | VARCHAR2(17) | Y |  |  |
| 59 | BASE_TRIB_IR | VARCHAR2(17) | Y |  |  |
| 60 | BASE_ISEN_IR | VARCHAR2(17) | Y |  |  |
| 61 | BASE_TRIB_ISS | VARCHAR2(17) | Y |  |  |
| 62 | BASE_ISEN_ISS | VARCHAR2(17) | Y |  |  |
| 63 | BASE_REAL_TERC_ISS | VARCHAR2(17) | Y |  |  |
| 64 | BASE_SUB_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 65 | NUM_MAQ_REG | VARCHAR2(6) | Y |  |  |
| 66 | NUM_CUPON_FISC | VARCHAR2(6) | Y |  |  |
| 67 | IND_MODELO_CUPOM | VARCHAR2(2) | Y |  |  |
| 68 | VLR_CONTAB_COMPL | VARCHAR2(17) | Y |  |  |
| 69 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 70 | VLR_ALIQ_DESTINO | VARCHAR2(7) | Y |  |  |
| 71 | VLR_OUTROS1 | VARCHAR2(17) | Y |  |  |
| 72 | VLR_OUTROS2 | VARCHAR2(17) | Y |  |  |
| 73 | VLR_OUTROS3 | VARCHAR2(17) | Y |  |  |
| 74 | VLR_OUTROS4 | VARCHAR2(17) | Y |  |  |
| 75 | VLR_OUTROS5 | VARCHAR2(17) | Y |  |  |
| 76 | VLR_ALIQ_OUTROS1 | VARCHAR2(7) | Y |  |  |
| 77 | VLR_ALIQ_OUTROS2 | VARCHAR2(7) | Y |  |  |
| 78 | IND_NF_ESPECIAL | CHAR(1) | Y |  |  |
| 79 | IND_TP_FRETE | CHAR(1) | Y |  |  |
| 80 | COD_MUNICIPIO | VARCHAR2(6) | Y |  |  |
| 81 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 82 | DAT_DI | VARCHAR2(8) | Y |  |  |
| 83 | VLR_TOM_SERVICO | VARCHAR2(17) | Y |  |  |
| 84 | DAT_ESCR_EXTEMP | VARCHAR2(8) | Y |  |  |
| 85 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 86 | COD_REGIAO | VARCHAR2(2) | Y |  |  |
| 87 | DAT_AUTENTIC | VARCHAR2(8) | Y |  |  |
| 88 | COD_CANAL_DISTRIB | VARCHAR2(10) | Y |  |  |
| 89 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 90 | VLR_ICMS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 91 | VLR_IPI_NDESTAC | VARCHAR2(17) | Y |  |  |
| 92 | VLR_BASE_INSS | VARCHAR2(17) | Y |  |  |
| 93 | VLR_ALIQ_INSS | VARCHAR2(7) | Y |  |  |
| 94 | VLR_INSS_RETIDO | VARCHAR2(17) | Y |  |  |
| 95 | VLR_MAT_APLIC_ISS | VARCHAR2(17) | Y |  |  |
| 96 | VLR_SUBEMPR_ISS | VARCHAR2(17) | Y |  |  |
| 97 | IND_MUNIC_ISS | CHAR(1) | Y |  |  |
| 98 | IND_CLASSE_OP_ISS | CHAR(1) | Y |  |  |
| 99 | DAT_FATO_GERADOR | VARCHAR2(8) | Y |  |  |
| 100 | DAT_CANCELAMENTO | VARCHAR2(8) | Y |  |  |
| 101 | NUM_PAGINA | VARCHAR2(6) | Y |  |  |
| 102 | NUM_LIVRO | VARCHAR2(6) | Y |  |  |
| 103 | NRO_AIDF_NF | VARCHAR2(12) | Y |  |  |
| 104 | DAT_VALID_DOC_AIDF | VARCHAR2(8) | Y |  |  |
| 105 | IND_FATURA | CHAR(1) | Y |  |  |
| 106 | COD_QUITACAO | VARCHAR2(5) | Y |  |  |
| 107 | NUM_SELO_CONT_ICMS | VARCHAR2(12) | Y |  |  |
| 108 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 109 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 110 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 111 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 112 | BASE_ICMS_ORIGDEST | VARCHAR2(17) | Y |  |  |
| 113 | VLR_ICMS_ORIGDEST | VARCHAR2(17) | Y |  |  |
| 114 | ALIQ_ICMS_ORIGDEST | VARCHAR2(7) | Y |  |  |
| 115 | VLR_DESC_CONDIC | VARCHAR2(17) | Y |  |  |
| 116 | VLR_BASE_ISE_ICMSS | VARCHAR2(17) | Y |  |  |
| 117 | VLR_BASE_OUT_ICMSS | VARCHAR2(17) | Y |  |  |
| 118 | VLR_RED_BASE_ICMSS | VARCHAR2(17) | Y |  |  |
| 119 | PERC_RED_BASE_ICMS | VARCHAR2(7) | Y |  |  |
| 120 | IND_FISJUR_CPDIR | CHAR(1) | Y |  |  |
| 121 | COD_FISJUR_CPDIR | VARCHAR2(14) | Y |  |  |
| 122 | IND_MEDIDAJUDICIAL | CHAR(1) | Y |  |  |
| 123 | UF_ORIG_DEST | VARCHAR2(2) | Y |  |  |
| 124 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  |  |
| 125 | DAT_GRAVACAO | DATE | Y |  |  |
| 126 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 127 | NUM_CTR_DISP | VARCHAR2(10) | Y |  |  |
| 128 | NUM_FIM_DOCTO | VARCHAR2(12) | Y |  |  |
| 129 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 130 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 131 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 132 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 133 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 134 | COD_PAGTO_INSS | VARCHAR2(4) | Y |  |  |
| 135 | DAT_INTERN_AM | VARCHAR2(8) | Y |  |  |
| 136 | IND_FISJUR_LSG | CHAR(1) | Y |  |  |
| 137 | COD_FISJUR_LSG | VARCHAR2(14) | Y |  |  |
| 138 | COMPROV_EXP | VARCHAR2(15) | Y |  |  |
| 139 | NUM_FINAL_CRT_DISP | NUMBER(12) | Y |  |  |
| 140 | NUM_ALVARA | VARCHAR2(8) | Y |  |  |
| 141 | NOTIFICA_SEFAZ | VARCHAR2(14) | Y |  |  |
| 142 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 143 | IND_NOTA_SERVICO | CHAR(1) | Y |  |  |
| 144 | COD_MOTIVO | VARCHAR2(10) | Y |  |  |
| 145 | COD_AMPARO | VARCHAR2(10) | Y |  |  |
| 146 | UF_AMPARO_LEGAL | VARCHAR2(2) | Y |  |  |
| 147 | OBS_COMPL_MOTIVO | VARCHAR2(100) | Y |  |  |
| 148 | IND_TP_RET | CHAR(1) | Y |  |  |
| 149 | IND_TP_TOMADOR | CHAR(1) | Y |  |  |
| 150 | COD_ANTEC_ST | VARCHAR2(1) | Y |  |  |
| 151 | CNPJ_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 152 | UF_ARMAZ_ORIG | VARCHAR2(2) | Y |  |  |
| 153 | INS_EST_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 154 | CNPJ_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 155 | UF_ARMAZ_DEST | VARCHAR2(2) | Y |  |  |
| 156 | INS_EST_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 157 | OBS_INF_ADIC_NF | VARCHAR2(250) | Y |  |  |
| 158 | VLR_BASE_INSS_2 | VARCHAR2(17) | Y |  |  |
| 159 | VLR_ALIQ_INSS_2 | VARCHAR2(7) | Y |  |  |
| 160 | VLR_INSS_RETIDO_2 | VARCHAR2(17) | Y |  |  |
| 161 | COD_PAGTO_INSS_2 | VARCHAR2(4) | Y |  |  |
| 162 | VLR_BASE_PIS_ST | VARCHAR2(17) | Y |  |  |
| 163 | VLR_ALIQ_PIS_ST | VARCHAR2(7) | Y |  |  |
| 164 | VLR_PIS_ST | VARCHAR2(17) | Y |  |  |
| 165 | VLR_BASE_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 166 | VLR_ALIQ_COFINS_ST | VARCHAR2(7) | Y |  |  |
| 167 | VLR_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 168 | VLR_BASE_CSLL | VARCHAR2(17) | Y |  |  |
| 169 | VLR_ALIQ_CSLL | VARCHAR2(7) | Y |  |  |
| 170 | VLR_CSLL | VARCHAR2(17) | Y |  |  |
| 171 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 172 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 173 | BASE_ICMSS_SUBSTITUIDO | VARCHAR2(17) | Y |  |  |
| 174 | VLR_ICMSS_SUBSTITUIDO | VARCHAR2(17) | Y |  |  |
| 175 | COD_CEI | VARCHAR2(12) | Y |  |  |
| 176 | VLR_JUROS_INSS | VARCHAR2(17) | Y |  |  |
| 177 | VLR_MULTA_INSS | VARCHAR2(17) | Y |  |  |
| 178 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 179 | VLR_ICMSS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 180 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 181 | DAT_PGTO_GNRE_DARJ | VARCHAR2(8) | Y |  |  |
| 182 | DT_PAGTO_NF | VARCHAR2(8) | Y |  |  |
| 183 | HORA_SAIDA | VARCHAR2(6) | Y |  |  |
| 184 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  |  |
| 185 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 186 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 187 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 188 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |
| 189 | COD_MUNICIPIO_ORIG | VARCHAR2(5) | Y |  |  |
| 190 | COD_MUNICIPIO_DEST | VARCHAR2(5) | Y |  |  |
| 191 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 192 | NUM_LANCAMENTO | VARCHAR2(12) | Y |  |  |
| 193 | VLR_MAT_PROP | VARCHAR2(17) | Y |  |  |
| 194 | VLR_MAT_TERC | VARCHAR2(17) | Y |  |  |
| 195 | VLR_BASE_ISS_RETIDO | VARCHAR2(17) | Y |  |  |
| 196 | VLR_ISS_RETIDO | VARCHAR2(17) | Y |  |  |
| 197 | VLR_DEDUCAO_ISS | VARCHAR2(17) | Y |  |  |
| 198 | COD_MUNIC_ARMAZ_ORIG | VARCHAR2(5) | Y |  |  |
| 199 | INS_MUNIC_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 200 | COD_MUNIC_ARMAZ_DEST | VARCHAR2(5) | Y |  |  |
| 201 | INS_MUNIC_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 202 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 203 | COD_CLASSE_CONSUMO | VARCHAR2(2) | Y |  |  |
| 204 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 205 | NUM_CONTRATO | VARCHAR2(14) | Y |  |  |
| 206 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  |  |
| 207 | COD_TP_UTIL | VARCHAR2(2) | Y |  |  |
| 208 | GRUPO_TENSAO | VARCHAR2(2) | Y |  |  |
| 209 | DATA_CONSUMO_INI | VARCHAR2(8) | Y |  |  |
| 210 | DATA_CONSUMO_FIM | VARCHAR2(8) | Y |  |  |
| 211 | DATA_CONSUMO_LEIT | VARCHAR2(8) | Y |  |  |
| 212 | QTD_CONTRATADA_PONTA | VARCHAR2(17) | Y |  |  |
| 213 | QTD_CONTRATADA_FPONTA | VARCHAR2(17) | Y |  |  |
| 214 | QTD_CONSUMO_TOTAL | VARCHAR2(17) | Y |  |  |
| 215 | UF_CONSUMO | VARCHAR2(2) | Y |  |  |
| 216 | COD_MUNIC_CONSUMO | VARCHAR2(5) | Y |  |  |
| 217 | COD_OPER_ESP_ST | CHAR(1) | Y |  |  |
| 218 | ATO_NORMATIVO | VARCHAR2(20) | Y |  | SEF-PE: Ato Normativo |
| 219 | NUM_ATO_NORMATIVO | VARCHAR2(5) | Y |  | SEF-PE: Número do Ato Normativo |
| 220 | ANO_ATO_NORMATIVO | VARCHAR2(4) | Y |  | SEF-PE: Ano do Ato Normativo |
| 221 | CAPITULACAO_NORMA | VARCHAR2(30) | Y |  | SEF-PE: Capitulação da Norma |
| 222 | VLR_OUTRAS_ENTID | VARCHAR2(17) | Y |  |  |
| 223 | VLR_TERCEIROS | VARCHAR2(17) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 224 | IND_TP_COMPL_ICMS | VARCHAR2(2) | Y |  |  |
| 225 | VLR_BASE_CIDE | VARCHAR2(17) | Y |  |  |
| 226 | VLR_ALIQ_CIDE | VARCHAR2(7) | Y |  |  |
| 227 | VLR_CIDE | VARCHAR2(17) | Y |  |  |
| 228 | COD_VERIFIC_NFE | VARCHAR2(8) | Y |  |  |
| 229 | COD_TP_RPS_NFE | VARCHAR2(5) | Y |  |  |
| 230 | NUM_RPS_NFE | VARCHAR2(12) | Y |  |  |
| 231 | SERIE_RPS_NFE | VARCHAR2(5) | Y |  |  |
| 232 | DAT_EMISSAO_RPS_NFE | VARCHAR2(8) | Y |  |  |
| 233 | DSC_SERVICO_NFE | VARCHAR2(1000) | Y |  |  |
| 234 | NUM_AUTENTIC_NFE | VARCHAR2(9) | Y |  |  |
| 235 | NUM_DV_NFE | CHAR(1) | Y |  |  |
| 236 | MODELO_NF_DMS | VARCHAR2(1) | Y |  | Modelo da Nota Fiscal para a série U ou M em atendimento a DMS Campo Grande - Mato Grosso do Sul. |
| 237 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 238 | VLR_COMISSAO | VARCHAR2(17) | Y |  |  |
| 239 | IND_NFE_DENEG_INUT | CHAR(1) | Y |  |  |
| 240 | IND_NF_REG_ESPECIAL | CHAR(1) | Y |  |  |
| 241 | VLR_ABAT_NTRIBUTADO | VARCHAR2(17) | Y |  |  |
| 242 | VLR_OUTROS_ICMS | VARCHAR2(17) | Y |  | Campo criado para gerar o registro 90 da DAPI MG, recuperando as informações da Apuração do ICMS automaticamente. |
| 243 | HORA_EMISSAO | VARCHAR2(6) | Y |  |  |
| 244 | OBS_DADOS_FATURA | VARCHAR2(256) | Y |  |  |
| 245 | HORA_SAIDA_REC | VARCHAR2(6) | Y |  |  |
| 246 | IND_FIS_CONCES | CHAR(1) | Y |  |  |
| 247 | COD_FIS_CONCES | VARCHAR2(14) | Y |  |  |
| 248 | PST_ID | NUMBER | Y |  |  |

**Indexes**:
- IX_SAFX92: (DAT_GRAVACAO)
- IX_SAFX92_1: (COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, MOVTO_E_S)
- IX_SAFX92_2: (COD_EMPRESA, COD_ESTAB, DATA_SAIDA_REC, MOVTO_E_S)
- IX_SAFX92_COTEPE: (IND_ATO_COTEPE)

---

## SAFX93

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IND_BEM_PATR | CHAR(1) | Y |  |  |
| 13 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 14 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 15 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 16 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 17 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 18 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 19 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 20 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 21 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 22 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 23 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 24 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 25 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 26 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 27 | VLR_UNIT | VARCHAR2(19) | Y |  |  |
| 28 | VLR_ITEM | VARCHAR2(17) | Y |  |  |
| 29 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 30 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 31 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 32 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 33 | IND_IPI_INCLUSO | CHAR(1) | Y |  |  |
| 34 | NUM_ROMANEIO | VARCHAR2(12) | Y |  |  |
| 35 | DATA_ROMANEIO | VARCHAR2(8) | Y |  |  |
| 36 | PESO_LIQUIDO | VARCHAR2(14) | Y |  |  |
| 37 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 38 | VLR_ITEM_CONVER | VARCHAR2(17) | Y |  |  |
| 39 | VLR_FRETE | VARCHAR2(17) | Y |  |  |
| 40 | VLR_SEGURO | VARCHAR2(17) | Y |  |  |
| 41 | VLR_OUTRAS | VARCHAR2(17) | Y |  |  |
| 42 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 43 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 44 | DIF_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 45 | OBS_ICMS | VARCHAR2(45) | Y |  |  |
| 46 | COD_APUR_ICMS | VARCHAR2(5) | Y |  |  |
| 47 | VLR_ALIQ_IPI | VARCHAR2(7) | Y |  |  |
| 48 | VLR_IPI | VARCHAR2(17) | Y |  |  |
| 49 | OBS_IPI | VARCHAR2(45) | Y |  |  |
| 50 | COD_APUR_IPI | VARCHAR2(5) | Y |  |  |
| 51 | VLR_ALIQ_SUB_ICMS | VARCHAR2(7) | Y |  |  |
| 52 | VLR_SUBST_ICMS | VARCHAR2(17) | Y |  |  |
| 53 | OBS_SUBST_ICMS | VARCHAR2(45) | Y |  |  |
| 54 | COD_APUR_SUB_ICMS | VARCHAR2(5) | Y |  |  |
| 55 | TRIB_ICMS | CHAR(1) | Y |  |  |
| 56 | BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 57 | BASE_REDU_ICMS | VARCHAR2(17) | Y |  |  |
| 58 | TRIB_IPI | CHAR(1) | Y |  |  |
| 59 | BASE_IPI | VARCHAR2(17) | Y |  |  |
| 60 | BASE_REDU_IPI | VARCHAR2(17) | Y |  |  |
| 61 | BASE_SUB_TRIB_ICMS | VARCHAR2(17) | Y |  |  |
| 62 | VLR_CONTAB_COMPL | VARCHAR2(17) | Y |  |  |
| 63 | VLR_ALIQ_DESTINO | VARCHAR2(7) | Y |  |  |
| 64 | VLR_OUTROS1 | VARCHAR2(17) | Y |  |  |
| 65 | VLR_OUTROS2 | VARCHAR2(17) | Y |  |  |
| 66 | VLR_OUTROS3 | VARCHAR2(17) | Y |  |  |
| 67 | VLR_OUTROS4 | VARCHAR2(17) | Y |  |  |
| 68 | VLR_OUTROS5 | VARCHAR2(17) | Y |  |  |
| 69 | VLR_ALIQ_OUTROS1 | VARCHAR2(7) | Y |  |  |
| 70 | VLR_ALIQ_OUTROS2 | VARCHAR2(7) | Y |  |  |
| 71 | VLR_CONTAB_ITEM | VARCHAR2(17) | Y |  |  |
| 72 | COD_OBS_VCONT_COMP | VARCHAR2(10) | Y |  |  |
| 73 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 74 | VLR_OUTROS_ICMS | VARCHAR2(17) | Y |  |  |
| 75 | VLR_OUTROS_IPI | VARCHAR2(17) | Y |  |  |
| 76 | NUM_ATO_CONCES | VARCHAR2(15) | Y |  |  |
| 77 | DAT_EMBARQUE | VARCHAR2(8) | Y |  |  |
| 78 | NUM_REG_EXP | VARCHAR2(12) | Y |  |  |
| 79 | NUM_DESP_EXP | VARCHAR2(11) | Y |  |  |
| 80 | VLR_TOM_SERVICO | VARCHAR2(17) | Y |  |  |
| 81 | VLR_DESP_MOEDA_EXP | VARCHAR2(17) | Y |  |  |
| 82 | COD_MOEDA_NEGOC | VARCHAR2(10) | Y |  |  |
| 83 | COD_PAIS_DEST_ORIG | VARCHAR2(3) | Y |  |  |
| 84 | IND_CRED_ICMSS | CHAR(1) | Y |  |  |
| 85 | COD_TRIB_INT | VARCHAR2(5) | Y |  |  |
| 86 | VLR_ICMS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 87 | VLR_IPI_NDESTAC | VARCHAR2(17) | Y |  |  |
| 88 | TRIB_ICMS_AUX | CHAR(1) | Y |  |  |
| 89 | BASE_ICMS_AUX | VARCHAR2(17) | Y |  |  |
| 90 | TRIB_IPI_AUX | CHAR(1) | Y |  |  |
| 91 | BASE_IPI_AUX | VARCHAR2(17) | Y |  |  |
| 92 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 93 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 94 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 95 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 96 | BASE_ICMS_ORIGDEST | VARCHAR2(17) | Y |  |  |
| 97 | VLR_ICMS_ORIGDEST | VARCHAR2(17) | Y |  |  |
| 98 | ALIQ_ICMS_ORIGDEST | VARCHAR2(7) | Y |  |  |
| 99 | VLR_DESC_CONDIC | VARCHAR2(17) | Y |  |  |
| 100 | TRIB_ICMSS | CHAR(1) | Y |  |  |
| 101 | BASE_REDU_ICMSS | VARCHAR2(17) | Y |  |  |
| 102 | VLR_CUSTO_TRANSF | VARCHAR2(17) | Y |  |  |
| 103 | PERC_RED_BASE_ICMS | VARCHAR2(7) | Y |  |  |
| 104 | QTD_EMBARCADA | VARCHAR2(17) | Y |  |  |
| 105 | DAT_REGISTRO_EXP | VARCHAR2(8) | Y |  |  |
| 106 | DAT_DESPACHO | VARCHAR2(8) | Y |  |  |
| 107 | DAT_AVERBACAO | VARCHAR2(8) | Y |  |  |
| 108 | DAT_DI | VARCHAR2(8) | Y |  |  |
| 109 | NUM_DEC_IMP_REF | VARCHAR2(12) | Y |  |  |
| 110 | DAT_GRAVACAO | DATE | Y |  |  |
| 111 | DSC_MOT_OCOR | VARCHAR2(45) | Y |  |  |
| 112 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 113 | VLR_BASE_ICMS_ORIG | VARCHAR2(17) | Y |  |  |
| 114 | VLR_TRIB_ICMS_ORIG | VARCHAR2(17) | Y |  |  |
| 115 | VLR_BASE_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 116 | VLR_TRIB_ICMS_DEST | VARCHAR2(17) | Y |  |  |
| 117 | VLR_PERC_PRES_ICMS | VARCHAR2(7) | Y |  |  |
| 118 | VLR_PRECO_BASE_ST | VARCHAR2(17) | Y |  |  |
| 119 | COD_OPER_OIL | VARCHAR2(10) | Y |  |  |
| 120 | COD_DCR | VARCHAR2(9) | Y |  |  |
| 121 | COD_PROJETO | VARCHAR2(20) | Y |  |  |
| 122 | IND_MOV_FIS | CHAR(1) | Y |  |  |
| 123 | CHASSI | VARCHAR2(17) | Y |  |  |
| 124 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 125 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 126 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 127 | VLR_BASE_PIS_ST | VARCHAR2(17) | Y |  |  |
| 128 | VLR_ALIQ_PIS_ST | VARCHAR2(7) | Y |  |  |
| 129 | VLR_PIS_ST | VARCHAR2(17) | Y |  |  |
| 130 | VLR_BASE_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 131 | VLR_ALIQ_COFINS_ST | VARCHAR2(7) | Y |  |  |
| 132 | VLR_COFINS_ST | VARCHAR2(17) | Y |  |  |
| 133 | VLR_BASE_CSLL | VARCHAR2(17) | Y |  |  |
| 134 | VLR_ALIQ_CSLL | VARCHAR2(7) | Y |  |  |
| 135 | VLR_CSLL | VARCHAR2(17) | Y |  |  |
| 136 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 137 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 138 | IND_FORNEC_ICMSS | CHAR(1) | Y |  |  |
| 139 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  |  |
| 140 | VLR_ICMSS_NDESTAC | VARCHAR2(17) | Y |  |  |
| 141 | IND_DOCTO_REC | CHAR(1) | Y |  |  |
| 142 | DAT_PGTO_GNRE_DARJ | VARCHAR2(8) | Y |  |  |
| 143 | VLR_CUSTO_UNIT | VARCHAR2(17) | Y |  |  |
| 144 | VLR_FATOR_CONV | VARCHAR2(17) | Y |  |  |
| 145 | QUANTIDADE_CONV | VARCHAR2(17) | Y |  |  |
| 146 | VLR_FECP_ICMS | VARCHAR2(17) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 147 | VLR_FECP_DIFALIQ | VARCHAR2(17) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 148 | VLR_FECP_ICMS_ST | VARCHAR2(17) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 149 | VLR_FECP_FONTE | VARCHAR2(17) | Y |  | Campo utilizado para lancamento do valor do FUNCEP ref a Regime Fonte - GIM-PB |
| 150 | TRIB_ICMSS_AUX2 | CHAR(1) | Y |  |  |
| 151 | BASE_ICMSS_AUX2 | VARCHAR2(17) | Y |  |  |
| 152 | VLR_BASE_ICMSS_N_ESCRIT | VARCHAR2(17) | Y |  | Valor base do ICMS-ST não escriturado |
| 153 | VLR_ICMSS_N_ESCRIT | VARCHAR2(17) | Y |  | Valor do ICMS-ST não escriturado |
| 154 | COD_TRIB_IPI | VARCHAR2(2) | Y |  |  |
| 155 | LOTE_MEDICAMENTO | VARCHAR2(50) | Y |  |  |
| 156 | VALID_MEDICAMENTO | VARCHAR2(8) | Y |  |  |
| 157 | IND_BASE_MEDICAMENTO | CHAR(1) | Y |  |  |
| 158 | VLR_PRECO_MEDICAMENTO | VARCHAR2(17) | Y |  |  |
| 159 | IND_TIPO_ARMA | CHAR(1) | Y |  |  |
| 160 | NUM_SERIE_ARMA | VARCHAR2(50) | Y |  |  |
| 161 | NUM_CANO_ARMA | VARCHAR2(50) | Y |  |  |
| 162 | DSC_ARMA | VARCHAR2(100) | Y |  |  |
| 163 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 164 | COD_EX_NCM | VARCHAR2(2) | Y |  |  |
| 165 | COD_EX_IMP | VARCHAR2(2) | Y |  |  |
| 166 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 167 | CNPJ_OPERADORA | VARCHAR2(14) | Y |  |  |
| 168 | CPF_OPERADORA | VARCHAR2(14) | Y |  |  |
| 169 | UF_OPERADORA | VARCHAR2(2) | Y |  |  |
| 170 | INS_EST_OPERADORA | VARCHAR2(14) | Y |  |  |
| 171 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  |  |
| 172 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  |  |
| 173 | VLR_TERCEIROS | VARCHAR2(17) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 174 | VLR_PRECO_SUGER | VARCHAR2(17) | Y |  | Valor do preco sugerido do produto - Meio Magnetico - Reg78 - CAT 90 - SP |
| 175 | VLR_BASE_CIDE | VARCHAR2(17) | Y |  |  |
| 176 | VLR_ALIQ_CIDE | VARCHAR2(7) | Y |  |  |
| 177 | VLR_CIDE | VARCHAR2(17) | Y |  |  |
| 178 | COD_OPER_ESP_ST | VARCHAR2(2) | Y |  |  |
| 179 | VLR_COMISSAO | VARCHAR2(17) | Y |  |  |
| 180 | VLR_ICMS_FRETE | VARCHAR2(17) | Y |  |  |
| 181 | VLR_DIFAL_FRETE | VARCHAR2(17) | Y |  |  |
| 182 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' | Indicador para verificar se os valores de PIS/COFINS estao destacados no documentos fiscal |
| 183 | COD_ENQUAD_IPI | VARCHAR2(3) | Y |  |  |
| 184 | COD_SITUACAO_PIS | VARCHAR2(2) | Y |  |  |
| 185 | QTD_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 186 | VLR_ALIQ_PIS_R | VARCHAR2(19) | Y |  |  |
| 187 | COD_SITUACAO_COFINS | VARCHAR2(2) | Y |  |  |
| 188 | QTD_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 189 | VLR_ALIQ_COFINS_R | VARCHAR2(19) | Y |  |  |
| 190 | ITEM_PORT_TARE | VARCHAR2(2) | Y |  |  |
| 191 | VLR_FUNRURAL | VARCHAR2(17) | Y |  |  |
| 192 | IND_TP_PROD_MEDIC | CHAR(1) | Y |  |  |
| 193 | PST_ID | NUMBER | Y |  |  |

**Indexes**:
- IX_SAFX93: (DAT_GRAVACAO)
- IX_SAFX93_1: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_SAFX93_COTEPE: (IND_ATO_COTEPE)

---

## SAFX94

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 13 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 14 | VLR_SERVICO | VARCHAR2(17) | Y |  |  |
| 15 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 16 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 17 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 18 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 19 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 20 | VLR_UNIT | VARCHAR2(17) | Y |  |  |
| 21 | VLR_DESCONTO | VARCHAR2(17) | Y |  |  |
| 22 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 23 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 24 | VLR_SERVICO_CONV | VARCHAR2(18) | Y |  |  |
| 25 | VLR_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 26 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 27 | DIF_ALIQ_ICMS | VARCHAR2(7) | Y |  |  |
| 28 | OBS_ICMS | VARCHAR2(45) | Y |  |  |
| 29 | COD_APUR_ICMS | VARCHAR2(5) | Y |  |  |
| 30 | VLR_ALIQ_IR | VARCHAR2(7) | Y |  |  |
| 31 | VLR_IR | VARCHAR2(17) | Y |  |  |
| 32 | VLR_ALIQ_ISS | VARCHAR2(7) | Y |  |  |
| 33 | VLR_ISS | VARCHAR2(17) | Y |  |  |
| 34 | TRIB_ICMS | CHAR(1) | Y |  |  |
| 35 | BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 36 | TRIB_IR | CHAR(1) | Y |  |  |
| 37 | BASE_IR | VARCHAR2(17) | Y |  |  |
| 38 | TRIB_ISS | CHAR(1) | Y |  |  |
| 39 | BASE_ISS | VARCHAR2(17) | Y |  |  |
| 40 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 41 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 42 | DAT_GRAVACAO | DATE | Y |  |  |
| 43 | COMPL_ISENCAO | VARCHAR2(5) | Y |  |  |
| 44 | VLR_BASE_CSLL | VARCHAR2(17) | Y |  |  |
| 45 | VLR_ALIQ_CSLL | VARCHAR2(7) | Y |  |  |
| 46 | VLR_CSLL | VARCHAR2(17) | Y |  |  |
| 47 | VLR_BASE_PIS | VARCHAR2(17) | Y |  |  |
| 48 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 49 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 50 | VLR_BASE_COFINS | VARCHAR2(17) | Y |  |  |
| 51 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 52 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 53 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 54 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 55 | COD_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 56 | VLR_MAT_PROP | VARCHAR2(17) | Y |  |  |
| 57 | VLR_MAT_TERC | VARCHAR2(17) | Y |  |  |
| 58 | VLR_BASE_ISS_RETIDO | VARCHAR2(17) | Y |  |  |
| 59 | VLR_ISS_RETIDO | VARCHAR2(17) | Y |  |  |
| 60 | VLR_DEDUCAO_ISS | VARCHAR2(17) | Y |  |  |
| 61 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 62 | VLR_SUBEMPR_ISS | VARCHAR2(17) | Y |  |  |
| 63 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 64 | VLR_OUT_DESP | VARCHAR2(17) | Y |  |  |
| 65 | VLR_BASE_CIDE | VARCHAR2(17) | Y |  |  |
| 66 | VLR_ALIQ_CIDE | VARCHAR2(7) | Y |  |  |
| 67 | VLR_CIDE | VARCHAR2(17) | Y |  |  |
| 68 | VLR_COMISSAO | VARCHAR2(17) | Y |  |  |
| 69 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' | Indicador para verificar se os valores de PIS/COFINS estao destacados no documentos fiscal |
| 70 | PST_ID | NUMBER | Y |  |  |

**Indexes**:
- IX_SAFX94: (DAT_GRAVACAO)
- IX_SAFX94_COTEPE: (IND_ATO_COTEPE)

---

## SAFX95

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_ESCR_FISCAL | VARCHAR2(8) | Y |  |  |
| 4 | MOVTO_E_S | CHAR(1) | Y |  |  |
| 5 | NORM_DEV | CHAR(1) | Y |  |  |
| 6 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 7 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 8 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | COD_DOCTO_TRANSP | VARCHAR2(5) | Y |  |  |
| 13 | NUM_DOCFIS_TRANSP | VARCHAR2(12) | Y |  |  |
| 14 | SER_DOCFIS_TRANSP | VARCHAR2(3) | Y |  |  |
| 15 | SSER_DOCFIS_TRANSP | VARCHAR2(2) | Y |  |  |
| 16 | DATA_EMIS_TRANSP | VARCHAR2(8) | Y |  |  |
| 17 | CGC_CPF_REMET | VARCHAR2(14) | Y |  |  |
| 18 | MODALIDADE_FRETE | CHAR(1) | Y |  |  |
| 19 | VLR_TOT_DOCFIS | VARCHAR2(17) | Y |  |  |
| 20 | INSC_UF_REMET | VARCHAR2(14) | Y |  |  |
| 21 | RAZAO_REMET | VARCHAR2(70) | Y |  |  |
| 22 | MUNICIPIO_REMET | VARCHAR2(30) | Y |  |  |
| 23 | CEP_REMET | VARCHAR2(8) | Y |  |  |
| 24 | COD_ESTADO_REMET | VARCHAR2(2) | Y |  |  |
| 25 | CPF_CGC_DEST | VARCHAR2(14) | Y |  |  |
| 26 | INSC_ESTADUAL_DEST | VARCHAR2(14) | Y |  |  |
| 27 | RAZAO_DEST | VARCHAR2(70) | Y |  |  |
| 28 | MUNICIPIO_DEST | VARCHAR2(30) | Y |  |  |
| 29 | CEP_DEST | VARCHAR2(8) | Y |  |  |
| 30 | COD_ESTADO_DEST | VARCHAR2(2) | Y |  |  |
| 31 | DOCFIS_SIM_NAO | CHAR(1) | Y |  |  |
| 32 | COD_VIA_TRANSP | VARCHAR2(5) | Y |  |  |
| 33 | QTD_VOLUME | VARCHAR2(17) | Y |  |  |
| 34 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 35 | PESO_BRUTO | VARCHAR2(14) | Y |  |  |
| 36 | PESO_LIQUIDO | VARCHAR2(14) | Y |  |  |
| 37 | DESPESA_FRETE | VARCHAR2(17) | Y |  |  |
| 38 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 39 | OBSERVACAO_FRETE | VARCHAR2(45) | Y |  |  |
| 40 | IND_FIS_JUR_TRANSP | CHAR(1) | Y |  |  |
| 41 | COD_TRANSP | VARCHAR2(14) | Y |  |  |
| 42 | COD_MUNIC_COLETA | VARCHAR2(5) | Y |  |  |
| 43 | COD_MUNIC_DEST | VARCHAR2(5) | Y |  |  |
| 44 | DISTANCIA_EM_KM | VARCHAR2(6) | Y |  |  |
| 45 | QTD_MERCADORIA | VARCHAR2(17) | Y |  |  |
| 46 | IND_FORMA_CALC | CHAR(1) | Y |  |  |
| 47 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 48 | DAT_GRAVACAO | DATE | Y |  |  |
| 49 | VLR_PRODUTO | VARCHAR2(17) | Y |  |  |
| 50 | NAT_VOLUME | VARCHAR2(30) | Y |  |  |
| 51 | VOLUME | VARCHAR2(30) | Y |  |  |
| 52 | MARCA_VOLUME | VARCHAR2(50) | Y |  |  |
| 53 | NUM_VOLUME | VARCHAR2(30) | Y |  |  |
| 54 | IND_ATO_COTEPE | CHAR(1) | Y | 'N' | Indica se o registro foi carregado pela funcionalidade do Ato Cotepe |
| 55 | VLR_BASE_CIDE | VARCHAR2(17) | Y |  |  |
| 56 | VLR_ALIQ_CIDE | VARCHAR2(7) | Y |  |  |
| 57 | VLR_CIDE | VARCHAR2(17) | Y |  |  |
| 58 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 59 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 60 | PST_ID | NUMBER | Y |  |  |

**Indexes**:
- IX_SAFX95: (DAT_GRAVACAO)
- IX_SAFX95_COTEPE: (IND_ATO_COTEPE)

---

## SAFX96

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 2 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 3 | VALID_GRP_COMB_PRD | VARCHAR2(8) | Y |  |  |
| 4 | COD_GRP_COMB | VARCHAR2(2) | Y |  |  |
| 5 | FATOR_CONV_GAS_A | VARCHAR2(7) | Y |  |  |
| 6 | FATOR_PERDA | VARCHAR2(7) | Y |  |  |
| 7 | FATOR_GANHO | VARCHAR2(7) | Y |  |  |
| 8 | COD_PROD_OFICIAL | VARCHAR2(10) | Y |  |  |
| 9 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 10 | DAT_GRAVACAO | DATE | Y |  |  |
| 11 | FATOR_DIV_GAS_A | VARCHAR2(7) | Y |  |  |
| 12 | PST_ID | NUMBER | Y |  |  |
| 13 | MASC_ARQUIVO | VARCHAR2(4) | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX96 | VARCHAR2(4000) | Y | NVL("IND_PRODUTO",'@')\|\|NVL("COD_PRODUTO",'@') |  |

**Indexes**:
- IX_CHAVE_SAFX96: (CHAVE_SAFX96)
- IX_SAFX96_LOTE: (NUM_LOTE)

---

## SAFX97

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_ENTREGA | VARCHAR2(8) | Y |  |  |
| 4 | NRO_AIDF | VARCHAR2(12) | Y |  |  |
| 5 | COD_SITUACAO | VARCHAR2(2) | Y |  |  |
| 6 | DAT_OCOR | VARCHAR2(8) | Y |  |  |
| 7 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 8 | NUM_CTR_DISP_INI | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 11 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 12 | NUM_CTR_DISP_FIM | VARCHAR2(12) | Y |  |  |
| 13 | COD_OPERACAO | VARCHAR2(2) | Y |  |  |
| 14 | COD_TIPO_REGISTRO | VARCHAR2(2) | Y |  |  |
| 15 | DAT_GRAVACAO | DATE | Y |  |  |
| 16 | NUM_CAIXA | VARCHAR2(6) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX97 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX97: (CHAVE_SAFX97)
- IX_SAFX97_LOTE: (NUM_LOTE)

---

## SAFX98

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_PRODUTO | VARCHAR2(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | DATA_MOVTO | VARCHAR2(8) | Y |  |  |
| 6 | MOVTO_E_S | VARCHAR2(1) | Y |  |  |
| 7 | TIPO_OPERACAO | VARCHAR2(2) | Y |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 12 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 13 | TIPO_VISTO | VARCHAR2(6) | Y |  |  |
| 14 | QUANT_MOVTO | VARCHAR2(17) | Y |  |  |
| 15 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 16 | TIPO | VARCHAR2(6) | Y |  |  |
| 17 | COD_ESTADO | VARCHAR2(2) | Y |  |  |
| 18 | REFERENCIA | VARCHAR2(45) | Y |  |  |
| 19 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 20 | ESPECIFICA_MAT | VARCHAR2(1) | Y |  |  |
| 21 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 22 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 23 | GUIA_TRAFEGO | VARCHAR2(40) | Y |  |  |
| 24 | DAT_GRAVACAO | DATE | Y |  |  |
| 25 | NUM_RECEITA | VARCHAR2(15) | Y |  |  |
| 26 | VLR_TOT_NOTA | VARCHAR2(17) | Y |  |  |
| 27 | PST_ID | NUMBER | Y |  |  |
| 28 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 29 | CHAVE_SAFX98 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX98: (CHAVE_SAFX98)
- IX_SAFX98_LOTE: (NUM_LOTE)

---

## SAFX99
**Comment**: Parametrização do Totalizador Parcial do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | IND_TIPO_OBRIG | CHAR(1) | Y |  |  |
| 6 | COD_TOTALIZADOR_ECF | VARCHAR2(7) | Y |  |  |
| 7 | DATA_X99 | VARCHAR2(8) | Y |  |  |
| 8 | COD_TOTALIZADOR_OBRIG | VARCHAR2(7) | Y |  |  |
| 9 | DAT_GRAVACAO | DATE | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | PST_ID | NUMBER | Y |  |  |
| 12 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 13 | CHAVE_SAFX99 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX99: (CHAVE_SAFX99)
- IX_SAFX99: (DAT_GRAVACAO)
- IX_SAFX99_LOTE: (NUM_LOTE)

---

## SAFX991
**Comment**: Movimento da Redução Z (Capa) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | NUM_CRZ | VARCHAR2(6) | Y |  |  |
| 6 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 7 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 8 | NUM_CRO | VARCHAR2(6) | Y |  |  |
| 9 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 10 | HORA_EMISSAO | VARCHAR2(6) | Y |  |  |
| 11 | NUM_COO_INI | VARCHAR2(9) | Y |  |  |
| 12 | NUM_COO_FIM | VARCHAR2(9) | Y |  |  |
| 13 | VLR_GT_INI | VARCHAR2(17) | Y |  |  |
| 14 | VLR_GT_FIM | VARCHAR2(17) | Y |  |  |
| 15 | VLR_VENDA_BRUTA | VARCHAR2(17) | Y |  |  |
| 16 | VLR_VENDA_LIQ | VARCHAR2(17) | Y |  |  |
| 17 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 18 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 19 | VLR_BASE_ICMS | VARCHAR2(17) | Y |  |  |
| 20 | VLR_TRIBUTO_ICMS | VARCHAR2(17) | Y |  |  |
| 21 | VLR_OPER_ICMS_ST | VARCHAR2(17) | Y |  |  |
| 22 | VLR_OPER_ISENTA_ICMS | VARCHAR2(17) | Y |  |  |
| 23 | VLR_OPER_N_INCID_ICMS | VARCHAR2(17) | Y |  |  |
| 24 | VLR_OPER_DESC_ICMS | VARCHAR2(17) | Y |  |  |
| 25 | VLR_OPER_ACRES_ICMS | VARCHAR2(17) | Y |  |  |
| 26 | VLR_OPER_CANC_ICMS | VARCHAR2(17) | Y |  |  |
| 27 | VLR_OPER_IOF | VARCHAR2(17) | Y |  |  |
| 28 | VLR_BASE_ISS | VARCHAR2(17) | Y |  |  |
| 29 | VLR_TRIBUTO_ISS | VARCHAR2(17) | Y |  |  |
| 30 | VLR_OPER_ISS_ST | VARCHAR2(17) | Y |  |  |
| 31 | VLR_OPER_ISENTA_ISS | VARCHAR2(17) | Y |  |  |
| 32 | VLR_OPER_N_INCID_ISS | VARCHAR2(17) | Y |  |  |
| 33 | VLR_OPER_DESC_ISS | VARCHAR2(17) | Y |  |  |
| 34 | VLR_OPER_ACRES_ISS | VARCHAR2(17) | Y |  |  |
| 35 | VLR_OPER_CANC_ISS | VARCHAR2(17) | Y |  |  |
| 36 | VLR_OPER_N_FISCAL | VARCHAR2(17) | Y |  |  |
| 37 | VLR_OPER_DESC_N_FISCAL | VARCHAR2(17) | Y |  |  |
| 38 | VLR_OPER_ACRES_N_FISCAL | VARCHAR2(17) | Y |  |  |
| 39 | VLR_OPER_CANC_N_FISCAL | VARCHAR2(17) | Y |  |  |
| 40 | DAT_GRAVACAO | DATE | Y |  |  |
| 41 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 42 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 43 | PST_ID | NUMBER | Y |  |  |
| 44 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 45 | CHAVE_SAFX991 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX991: (CHAVE_SAFX991)
- IX_SAFX991: (DAT_GRAVACAO)
- IX_SAFX991_LOTE: (NUM_LOTE)

---

## SAFX992
**Comment**: Movimento da Redução Z (Item) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | NUM_CRZ | VARCHAR2(6) | Y |  |  |
| 6 | DATA_FISCAL | VARCHAR2(8) | Y |  |  |
| 7 | COD_TOTALIZADOR_ECF | VARCHAR2(7) | Y |  |  |
| 8 | VLR_OPER | VARCHAR2(17) | Y |  |  |
| 9 | VLR_BASE | VARCHAR2(17) | Y |  |  |
| 10 | VLR_TRIBUTO | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | PST_ID | NUMBER | Y |  |  |
| 14 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 15 | CHAVE_SAFX992 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX992: (CHAVE_SAFX992)
- IX_SAFX992: (DAT_GRAVACAO)
- IX_SAFX992_LOTE: (NUM_LOTE)

---

## SAFX993
**Comment**: Movimento de Cupom (Capa) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 6 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 7 | NOME_CLIENTE | VARCHAR2(40) | Y |  |  |
| 8 | CPF_CNPJ_CLIENTE | VARCHAR2(14) | Y |  |  |
| 9 | IND_TIPO_CUPOM | CHAR(1) | Y |  |  |
| 10 | IND_SITUACAO_CUPOM | CHAR(1) | Y |  |  |
| 11 | COD_DENOMINACAO | VARCHAR2(2) | Y |  |  |
| 12 | NUM_COO_VINCULADO | VARCHAR2(9) | Y |  |  |
| 13 | NUM_CCF_CVC_CBP | VARCHAR2(9) | Y |  |  |
| 14 | NUM_GNF | VARCHAR2(9) | Y |  |  |
| 15 | NUM_GRG | VARCHAR2(9) | Y |  |  |
| 16 | NUM_CDC | VARCHAR2(6) | Y |  |  |
| 17 | NUM_CRZ | VARCHAR2(6) | Y |  |  |
| 18 | DATA_EMISSAO_FIM | VARCHAR2(8) | Y |  |  |
| 19 | HORA_EMISSAO_FIM | VARCHAR2(6) | Y |  |  |
| 20 | UF | VARCHAR2(2) | Y |  |  |
| 21 | COD_MUNICIPIO | VARCHAR2(5) | Y |  |  |
| 22 | VLR_LIQ_ITEM | VARCHAR2(17) | Y |  |  |
| 23 | VLR_DESC_CAPA | VARCHAR2(17) | Y |  |  |
| 24 | VLR_ACRES_CAPA | VARCHAR2(17) | Y |  |  |
| 25 | VLR_TOTAL_LIQ | VARCHAR2(17) | Y |  |  |
| 26 | VLR_ACRES_CAPA_CANC | VARCHAR2(17) | Y |  |  |
| 27 | VLR_IOF | VARCHAR2(17) | Y |  |  |
| 28 | DAT_GRAVACAO | DATE | Y |  |  |
| 29 | DSC_CHAVE_CFE | VARCHAR2(80) | Y |  |  |
| 30 | NUM_CONTADOR_CFE | VARCHAR2(9) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 32 | PST_ID | NUMBER | Y |  |  |
| 33 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 34 | CHAVE_SAFX993 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX993: (CHAVE_SAFX993)
- IX_SAFX993: (DAT_GRAVACAO)
- IX_SAFX993_LOTE: (NUM_LOTE)

---

## SAFX994
**Comment**: Movimento de Cupom (Item) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 6 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 7 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 8 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 10 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 11 | IND_SITUACAO_ITEM | CHAR(1) | Y |  |  |
| 12 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 13 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COD_TOTALIZADOR_ECF | VARCHAR2(7) | Y |  |  |
| 16 | QTDE | VARCHAR2(17) | Y |  |  |
| 17 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 18 | VLR_UNIT | VARCHAR2(19) | Y |  |  |
| 19 | VLR_ITEM | VARCHAR2(17) | Y |  |  |
| 20 | VLR_DESC | VARCHAR2(17) | Y |  |  |
| 21 | VLR_ACRES | VARCHAR2(17) | Y |  |  |
| 22 | VLR_LIQ_ITEM | VARCHAR2(17) | Y |  |  |
| 23 | QTDE_CANC | VARCHAR2(17) | Y |  |  |
| 24 | VLR_ITEM_CANC | VARCHAR2(17) | Y |  |  |
| 25 | VLR_ACRES_CANC | VARCHAR2(17) | Y |  |  |
| 26 | VLR_PIS | VARCHAR2(17) | Y |  |  |
| 27 | VLR_COFINS | VARCHAR2(17) | Y |  |  |
| 28 | VLR_BASE | VARCHAR2(17) | Y |  |  |
| 29 | VLR_TRIBUTO | VARCHAR2(17) | Y |  |  |
| 30 | DAT_GRAVACAO | DATE | Y |  |  |
| 31 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 32 | COD_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 33 | COD_SIT_TRIB_PIS | VARCHAR2(2) | Y |  |  |
| 34 | VLR_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 35 | VLR_ALIQ_PIS | VARCHAR2(7) | Y |  |  |
| 36 | COD_SIT_TRIB_COFINS | VARCHAR2(2) | Y |  |  |
| 37 | VLR_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 38 | VLR_ALIQ_COFINS | VARCHAR2(7) | Y |  |  |
| 39 | QTD_BASE_PIS | VARCHAR2(18) | Y |  |  |
| 40 | VLR_ALIQ_ESPEC_PIS | VARCHAR2(19) | Y |  |  |
| 41 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 42 | QTD_BASE_COFINS | VARCHAR2(18) | Y |  |  |
| 43 | VLR_ALIQ_ESPEC_COFINS | VARCHAR2(19) | Y |  |  |
| 44 | COD_NAT_REC | VARCHAR2(3) | Y |  |  |
| 45 | COD_SCP | VARCHAR2(14) | Y |  |  |
| 46 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 47 | PST_ID | NUMBER | Y |  |  |
| 48 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 49 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 50 | CHAVE_SAFX994 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX994: (CHAVE_SAFX994)
- IX_SAFX994: (DAT_GRAVACAO)
- IX_SAFX994_LOTE: (NUM_LOTE)

---

## SAFX995
**Comment**: Movimento de Cupom (Pagamento) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 6 | DATA_EMISSAO | VARCHAR2(8) | Y |  |  |
| 7 | COD_MEIO_PAGTO | VARCHAR2(2) | Y |  |  |
| 8 | VLR_PAGO | VARCHAR2(17) | Y |  |  |
| 9 | IND_ESTORNO | CHAR(1) | Y |  |  |
| 10 | VLR_ESTORNO | VARCHAR2(17) | Y |  |  |
| 11 | DAT_GRAVACAO | DATE | Y |  |  |
| 12 | NUM_COMPROVANTE | VARCHAR2(18) | Y |  |  |
| 13 | IND_NAT_OPERACAO | CHAR(1) | Y |  |  |
| 14 | IND_TIPO_OPERACAO | CHAR(1) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | CEP | VARCHAR2(8) | Y |  |  |
| 17 | PST_ID | NUMBER | Y |  |  |
| 18 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 19 | CHAVE_SAFX995 | VARCHAR2(4000) | Y | NVL("COD_EMPRESA",'@')\|\|NVL("COD_ESTAB",'@')\|\|N... |  |

**Indexes**:
- IX_CHAVE_SAFX995: (CHAVE_SAFX995)
- IX_SAFX995: (DAT_GRAVACAO)
- IX_SAFX995_LOTE: (NUM_LOTE)

---

## SAFX996

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | COD_CAIXA_ECF | VARCHAR2(3) | Y |  |  |
| 5 | COD_TOTALIZADOR_ECF | VARCHAR2(7) | Y |  |  |
| 6 | VALID_TOTALIZADOR_ECF | VARCHAR2(8) | Y |  |  |
| 7 | DSC_TOTALIZADOR_ECF | VARCHAR2(50) | Y |  |  |
| 8 | NUM_SEQ_TOTALIZADOR | VARCHAR2(2) | Y |  |  |
| 9 | DSC_SIT_TRIBUTARIA | VARCHAR2(50) | Y |  |  |
| 10 | VLR_ALIQ | VARCHAR2(7) | Y |  |  |
| 11 | COD_SITUACAO_A | CHAR(1) | Y |  |  |
| 12 | COD_SITUACAO_B | VARCHAR2(2) | Y |  |  |
| 13 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 14 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 15 | COD_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 16 | DAT_GRAVACAO | DATE | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | PST_ID | NUMBER | Y |  |  |
| 19 | NUM_LOTE | VARCHAR2(80) | Y |  |  |
| 20 | CHAVE_SAFX996 | VARCHAR2(4000) | Y | NVL("COD_MODELO",'@')\|\|NVL("COD_CAIXA_ECF",'@')... |  |

**Indexes**:
- IX_CHAVE_SAFX996: (CHAVE_SAFX996)
- IX_SAFX996_LOTE: (NUM_LOTE)

---

