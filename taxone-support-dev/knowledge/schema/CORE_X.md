# Módulo: X (Transacionais X01-X11) - 415 tabelas

## X01_CONTABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_LANCTO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | IDENT_CONTRA_PART | NUMBER(12) | Y |  |  |
| 8 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 9 | IDENT_DESPESA | NUMBER(12) | Y |  |  |
| 10 | IDENT_HISTPADRAO | NUMBER(12) | Y |  |  |
| 11 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 12 | TXT_HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 13 | VLR_LANCTO | NUMBER(19,2) | Y |  |  |
| 14 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 15 | VLR_LANCTO_CONV | NUMBER(20,4) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 19 | TIPO_LANCTO | CHAR(1) | Y |  | N - Normal; E - Encerramento |
| 20 | IDENT_PFJ_EMPRESA | NUMBER(12) | Y |  |  |
| 21 | DATA_PFJ_EMPRESA | DATE | Y |  |  |
| 22 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 23 | IDENTIF_LANC_RES | VARCHAR2(128) | Y |  |  |
| 24 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 25 | IDENTIF_SALDO | VARCHAR2(128) | Y |  |  |
| 26 | DSC_RESERVADO1 | NUMBER(19,2) | Y |  |  |
| 27 | DSC_RESERVADO2 | NUMBER(19,2) | Y |  |  |
| 28 | DSC_RESERVADO3 | NUMBER(19,2) | Y |  |  |
| 29 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 30 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 31 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 32 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 33 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 34 | DAT_LANCTO_EXTEMP | DATE | Y |  |  |
| 35 | COD_EVENTO_DESIF | VARCHAR2(3) | Y |  |  |
| 36 | IDENT_ESTADO_ORIG | NUMBER(12) | Y |  |  |
| 37 | COD_MUNIC_ORIG | NUMBER(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO

**FKs**:
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_DESPESA → X2004_CENTRO_DESP(IDENT_DESPESA)
- IDENT_HISTPADRAO → X2020_HIST_PADRAO(IDENT_HISTPADRAO)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTRA_PART → X2002_PLANO_CONTAS(IDENT_CONTA)
- COD_EMPRESA, IDENT_PFJ_EMPRESA, DATA_PFJ_EMPRESA → X39_PFJ_EMPRESA(COD_EMPRESA, IDENT_FIS_JUR, DATA_VALID_INI)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- COD_EVENTO_DESIF → CAD_EVENTO_DESIF(COD_EVENTO_DESIF)
- IDENT_ESTADO_ORIG, COD_MUNIC_ORIG → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

**Indexes**:
- IX_X01_CONTABIL_01: (COD_EMPRESA, COD_ESTAB, DATA_LANCTO, ARQUIVAMENTO)
- IX_X01_CONTABIL_02: (COD_EMPRESA, COD_ESTAB, IDENT_CONTA, IDENT_CONTRA_PART, IDENT_CUSTO, IDENT_DESPESA, IDENT_HISTPADRAO, IDENT_OPERACAO, COD_INDICE, IDENT_PFJ_EMPRESA, IDENT_SERVICO, COD_EVENTO_DESIF, IDENT_ESTADO_ORIG, COD_MUNIC_ORIG)
- IX_X01_CONTABIL_CTA: (IDENT_CONTA)
- IX_X01_CONTAB_CTA_PART: (IDENT_CONTRA_PART)
- IX_X01_EMPR_DAT: (COD_EMPRESA, DATA_LANCTO, IDENT_CONTA)
- IX_X01_ENCERR: (COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, IDENT_CUSTO, VLR_LANCTO)

---

## X01_SELECTION

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_LANCTO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 8 | VLR_LANCTO | NUMBER(19,2) | Y |  |  |
| 9 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 10 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 11 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 12 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 13 | VLR_SALDO_INI | NUMBER | Y |  |  |
| 14 | VLR_SALDO_FIM | NUMBER | Y |  |  |
| 15 | IND_DEB_CRED_CONTA_INI | VARCHAR2(1) | Y |  |  |
| 16 | IND_DEB_CRED_CONTA_FIM | VARCHAR2(1) | Y |  |  |
| 17 | VLR_SALDO_INI_MF | NUMBER | Y |  |  |
| 18 | VLR_SALDO_FIM_MF | NUMBER | Y |  |  |
| 19 | IND_DEB_CRED_CONTA_INI_MF | VARCHAR2(1) | Y |  |  |
| 20 | IND_DEB_CRED_CONTA_FIM_MF | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_LANCTO, GRUPO_CONTA, COD_CONTA, GRUPO_CUSTO, COD_CUSTO

---

## X02_SALDOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | NUMBER(19,2) | Y |  |  |
| 8 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 9 | VLR_TOT_CRE | NUMBER(19,2) | Y |  |  |
| 10 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | IDENTIF_SALDO | VARCHAR2(128) | Y |  |  |
| 14 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X02_SALDOS_01: (COD_EMPRESA, COD_ESTAB, DATA_SALDO)
- IX_X02_SALDOS_CTA: (IDENT_CONTA)

---

## X03_TIT_PAGAR

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
| 10 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 11 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 12 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 13 | DATA_EMISSAO | DATE | Y |  |  |
| 14 | DATA_VENCTO | DATE | Y |  |  |
| 15 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 16 | VLR_MOVTO | NUMBER(17,2) | Y |  |  |
| 17 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 18 | VLR_MOVTO_CONV | NUMBER(18,4) | Y |  |  |
| 19 | VLR_TOT_DOCTO | NUMBER(17,2) | Y |  |  |
| 20 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 23 | NUM_DOC_COMPENS | VARCHAR2(15) | Y |  |  |
| 24 | IDENT_CENTRO_RESP | NUMBER(12) | Y |  |  |
| 25 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 26 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 27 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 28 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 29 | DATA_FATOR_GERADOR | DATE | Y |  |  |
| 30 | DATA_INI_COMPET | DATE | Y |  |  |
| 31 | DATA_FIM_COMPET | DATE | Y |  |  |
| 32 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 33 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 34 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 35 | HISTORICO | VARCHAR2(50) | Y |  |  |
| 36 | IND_TIPO_TITULO | VARCHAR2(2) | Y |  | indicador do tipo de título de crédito: 00 - duplicata, 01 - cheque, 02 - promissória, 03 - recibo, 99 - outros - ato cotepe 35/05 |
| 37 | DSC_COMPL_TITULO | VARCHAR2(50) | Y |  | descrição complementar do título de crédito - ato cotepe 35/05 |
| 38 | QTDE_PARCELA | NUMBER(3) | Y |  | quantidade de parcelas na X031_TIT_PAGAR_PARC - ato cotepe 35/05 |
| 39 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  | ATO COTEPE 70 - reg Z030 - Número do Lançamento Contábil |
| 40 | DATA_FISCAL_NF | DATE | Y |  | data fiscal da nota que originou o titulo a pagar |
| 41 | MOVTO_E_S_NF | CHAR(1) | Y |  | movimento da nota que originou o titulo a pagar |
| 42 | NORM_DEV_NF | CHAR(1) | Y |  | normal/devolucao da nota que originou o titulo a pagar |
| 43 | IDENT_DOCTO_NF | NUMBER(12) | Y |  | tipo de docto da nota que originou o titulo a pagar |
| 44 | IDENT_FIS_JUR_NF | NUMBER(12) | Y |  | pessoa fis/jur da nota que originou o titulo a pagar |
| 45 | NUM_DOCFIS_NF | VARCHAR2(12) | Y |  | numero da nota que originou o titulo a pagar |
| 46 | SERIE_DOCFIS_NF | VARCHAR2(3) | Y |  | serie da nota que originou o titulo a pagar |
| 47 | SUB_SERIE_DOCFIS_NF | VARCHAR2(2) | Y |  | subserie da nota que originou o titulo a pagar |
| 48 | IDENT_SETOR | NUMBER(12) | Y |  |  |
| 49 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 50 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 51 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 52 | VLR_RET | NUMBER(17,2) | Y |  |  |
| 53 | VLR_N_RET | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_CENTRO_RESP → X2094_CENTRO_RESP(IDENT_CENTRO_RESP)
- COD_TRIBUTO, ESP_TRIBUTO → DWT_TRIBUTO_ESP(COD_TRIBUTO, ESP_TRIBUTO)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)
- COD_TRIBUTO → DWT_TRIBUTO(COD_TRIBUTO)
- IDENT_DOCTO_NF → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR_NF → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_0283: (IDENT_FIS_JUR)
- IX_FK_SAF_2120: (IDENT_FIS_JUR_NF)
- IX_X03_NF_TIT: (NUM_DOCFIS_NF, DATA_FISCAL_NF, SERIE_DOCFIS_NF, SUB_SERIE_DOCFIS_NF, MOVTO_E_S_NF, IDENT_FIS_JUR_NF, IDENT_DOCTO_NF, COD_ESTAB, COD_EMPRESA)
- IX_X03_NF_TIT_01: (NUM_DOCFIS, DATA_EMISSAO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_DOCTO, COD_ESTAB, COD_EMPRESA)
- IX_X03_TIT_PAGAR_CTA: (IDENT_CONTA)

---

## X04_PESSOA_FIS_JUR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 2 | GRUPO_FIS_JUR | VARCHAR2(9) | Y |  |  |
| 3 | IND_FIS_JUR | CHAR(1) | Y |  |  |
| 4 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 5 | VALID_FIS_JUR | DATE | Y |  |  |
| 6 | CPF_CGC | VARCHAR2(14) | Y |  |  |
| 7 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |
| 8 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 9 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 10 | INSC_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 11 | IND_CONTEM_COD | CHAR(1) | Y |  |  |
| 12 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 13 | NOME_FANTASIA | VARCHAR2(50) | Y |  |  |
| 14 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 15 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 16 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 17 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 18 | CIDADE | VARCHAR2(30) | Y |  |  |
| 19 | DISTRITO | VARCHAR2(20) | Y |  |  |
| 20 | SUB_DISTRITO | VARCHAR2(20) | Y |  |  |
| 21 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 22 | CEP | NUMBER(8) | Y |  |  |
| 23 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 24 | DDD | VARCHAR2(5) | Y |  |  |
| 25 | TELEFONE | VARCHAR2(10) | Y |  |  |
| 26 | FAX | VARCHAR2(10) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 29 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 30 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 31 | IND_CLASSE_PFJ | VARCHAR2(2) | Y |  |  |
| 32 | IND_CLASSE_EMP | VARCHAR2(2) | Y |  |  |
| 33 | IND_PFJ_CONTRIB | CHAR(1) | Y |  |  |
| 34 | CEI | VARCHAR2(15) | Y |  |  |
| 35 | IND_CLIENTE_SID | CHAR(1) | Y |  |  |
| 36 | CPF_CNPJ_INV | VARCHAR2(14) | Y |  |  |
| 37 | IND_SCP | CHAR(1) | Y | 'N' |  |
| 38 | IDENT_CBO | NUMBER(12) | Y |  |  |
| 39 | PIS_PASEP | VARCHAR2(11) | Y |  | Numero pis/pasep solicitado pela obrigação SEFIP. |
| 40 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  | COD_CATEGORIA da tabela PRT_CATEGORIA_TRAB, solicitado pela obrigação SEFIP. |
| 41 | OCORRENCIA_TRAB | VARCHAR2(2) | Y |  | códigos de ocorrencias solicitados pela obrigação SEFIP. View com as ocorrências OCORRENCIA_TRAB_V |
| 42 | CX_POSTAL | NUMBER(20) | Y |  |  |
| 43 | NUM_CEP_CX_POSTAL | NUMBER(8) | Y |  | código de endereçamento postal da caixa postal |
| 44 | E_MAIL | VARCHAR2(60) | Y |  |  |
| 45 | IND_FOME_ZERO | CHAR(1) | Y |  | Ato Cotepe 70 reg C200: indicador de participante do programa fome zero. Valores: N, S |
| 46 | DAT_VALIDADE_INI_ATIVIDADE | DATE | Y |  |  |
| 47 | TP_LOGRADOURO | VARCHAR2(10) | Y |  | Campo criado para atender a DIM São Luis. |
| 48 | IND_SIMPLES_NAC | CHAR(1) | Y |  | Campo criado para atender a DIM São Luis. |
| 49 | TP_BAIRRO | VARCHAR2(10) | Y |  |  |
| 50 | IMP_RENDA_DEPEND | VARCHAR2(2) | Y |  |  |
| 51 | SAL_FAMILIA_DEPEND | VARCHAR2(2) | Y |  |  |
| 52 | IDENT_FUNCAO_AUTONOMO | NUMBER(12) | Y |  |  |
| 53 | DATA_NASC_AUTONOMO | DATE | Y |  |  |
| 54 | COD_FUNCAO_AUTONOMO | VARCHAR2(10) | Y |  |  |
| 55 | IND_INCENTIVO_CULTURAL | CHAR(1) | Y |  |  |
| 56 | IND_CLIENTE_LIVRE | CHAR(1) | Y |  |  |
| 57 | PASSAPORTE | VARCHAR2(20) | Y |  |  |
| 58 | DATA_MOLESTIA | DATE | Y |  |  |
| 59 | NUM_ID_FISCAL | VARCHAR2(30) | Y |  |  |
| 60 | TP_FONTE_PAGADORA | VARCHAR2(3) | Y |  |  |
| 61 | DSC_PROVINCIA_EX | VARCHAR2(40) | Y |  |  |
| 62 | NUM_ALVARA | VARCHAR2(11) | Y |  |  |
| 63 | COD_INSTAL_ANP | VARCHAR2(7) | Y |  | Codigo da Instalacao 2 da ANP |
| 64 | NUM_CR | VARCHAR2(10) | Y |  |  |
| 65 | IND_IDENTIF_FISCAL | CHAR(1) | Y |  |  |
| 66 | NUM_CAEPF | VARCHAR2(15) | Y |  |  |
| 67 | DATA_PREST_SERV | DATE | Y |  |  |
| 68 | IND_CONCILIACAO | CHAR(1) | Y |  |  |
| 69 | BAIRRO_II | VARCHAR2(60) | Y |  |  |
| 70 | NOM_CONTATO | VARCHAR2(100) | Y |  |  |
| 71 | ENDERECO_WEB | VARCHAR2(200) | Y |  |  |
| 72 | COD_CATEG_TRAB | VARCHAR2(3) | Y |  |  |
| 73 | IND_NAT_ATIVIDADE | CHAR(1) | Y |  |  |
| 74 | IDENT_SETOR | NUMBER(12) | Y |  |  |
| 75 | CPF_SP | VARCHAR2(14) | Y |  | Informar o CPF do Proprietário da Fazenda SP (Sao Paulo). |
| 76 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 77 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 78 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 79 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 80 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 81 | VLR_RESERVADO6 | NUMBER(19,2) | Y |  |  |
| 82 | VLR_RESERVADO7 | NUMBER(19,2) | Y |  |  |
| 83 | VLR_RESERVADO8 | NUMBER(19,2) | Y |  |  |
| 84 | IND_ISENTO_IMUNE | VARCHAR2(1) | Y |  | Informações sobre isenção e imunidade: 1 - Não isenta/não imune; 2- Instituição de educação e de assistência social sem fins lucrativos, a que se refere o art. 12 da Lei nº 9.532, de 10 de dezembro de 1997; 3- Instituição de caráter filantrópico, recreativo, cultural, científico e às associações civis, a que se refere o art. 15 da Lei nº 9.532, de 1997. |
| 85 | IND_CONTRIB_ICMS | VARCHAR2(1) | Y |  | Informações sobre contribuinte ICMS: 1 – Contribuinte do ICMS; 2 – Contribuinte Isento de Inscrição no Cadastro de Contribuintes do ICMS; 9 – Não Contribuinte. |
| 86 | IND_PRODUTOR_RURAL | VARCHAR2(1) | Y | 'N' |  |
| 87 | NUM_ID_OUTROS | VARCHAR2(20) | Y |  |  |
| 88 | COD_ID_ASSINANTE | VARCHAR2(15) | Y |  |  |
| 89 | IND_TP_ASSINANTE | VARCHAR2(2) | Y |  |  |
| 90 | ENDERECO_ENTREGA | VARCHAR2(60) | Y |  |  |
| 91 | NUM_ENDERECO_ENTREGA | VARCHAR2(60) | Y |  |  |
| 92 | COMPL_ENDERECO_ENTREGA | VARCHAR2(60) | Y |  |  |
| 93 | BAIRRO_ENTREGA | VARCHAR2(60) | Y |  |  |
| 94 | COD_MUNICIPIO_ENTREGA | NUMBER(5) | Y |  |  |
| 95 | CEP_ENTREGA | NUMBER(8) | Y |  |  |
| 96 | IDENT_UF_ENTREGA | NUMBER(12) | Y |  |  |
| 97 | DDD_ENTREGA | VARCHAR2(5) | Y |  |  |
| 98 | TELEFONE_ENTREGA | VARCHAR2(10) | Y |  |  |
| 99 | EMAIL_ENTREGA | VARCHAR2(60) | Y |  |  |

**PK**: IDENT_FIS_JUR

**FKs**:
- GRUPO_FIS_JUR → GRUPO_ESTAB(GRUPO_ESTAB)
- COD_ATIVIDADE, DAT_VALIDADE_INI_ATIVIDADE → ATIV_ECONOMICA(COD_ATIVIDADE, DAT_VALIDADE_INI)
- COD_PAIS → PAIS(COD_PAIS)
- IDENT_CBO → X2029_COD_CBO(IDENT_CBO)
- IDENT_UF_ENTREGA → ESTADO(IDENT_ESTADO)
- IDENT_UF_ENTREGA, COD_MUNICIPIO_ENTREGA → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

**Indexes**:
- IX_CHN_PES_FIS_JUR (UNIQUE): (GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, VALID_FIS_JUR)
- IX_X04_FIS_JUR: (IND_FIS_JUR, COD_FIS_JUR)
- IX_X04_PFJ_CPF_CGC: (CPF_CGC, VALID_FIS_JUR)

---

## X05_TIT_RECEBER

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
| 10 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 11 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 12 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 13 | DATA_EMISSAO | DATE | Y |  |  |
| 14 | DATA_VENCTO | DATE | Y |  |  |
| 15 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 16 | VLR_MOVTO | NUMBER(17,2) | Y |  |  |
| 17 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 18 | VLR_MOVTO_CONV | NUMBER(18,4) | Y |  |  |
| 19 | VLR_TOT_DOCTO | NUMBER(17,2) | Y |  |  |
| 20 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 23 | NUM_DOCTO_COMPENS | VARCHAR2(15) | Y |  |  |
| 24 | HISTORICO | VARCHAR2(50) | Y |  |  |
| 25 | OBSERVACAO | VARCHAR2(20) | Y |  |  |
| 26 | IND_TIPO_TITULO | VARCHAR2(2) | Y |  | indicador do tipo de título de crédito: 00 - duplicata, 01 - cheque, 02 - promissória, 03 - recibo, 99 - outros - ato cotepe 35/05 |
| 27 | DSC_COMPL_TITULO | VARCHAR2(50) | Y |  | descrição complementar do título de crédito - ato cotepe 35/05 |
| 28 | QTDE_PARCELA | NUMBER(3) | Y |  | quantidade de parcelas na X051_TIT_RECEBER_PARC - ato cotepe 35/05 |
| 29 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  | ATO COTEPE 70 - reg Z030 - Número do Lançamento Contábil |
| 30 | DATA_FISCAL_NF | DATE | Y |  | data fiscal da nota que originou o titulo a receber |
| 31 | MOVTO_E_S_NF | CHAR(1) | Y |  | movimento da nota que originou o titulo a receber |
| 32 | NORM_DEV_NF | CHAR(1) | Y |  | normal/devolucao da nota que originou o titulo a receber |
| 33 | IDENT_DOCTO_NF | NUMBER(12) | Y |  | tipo de docto da nota que originou o titulo a receber |
| 34 | IDENT_FIS_JUR_NF | NUMBER(12) | Y |  | pessoa fis/jur da nota que originou o titulo a receber |
| 35 | NUM_DOCFIS_NF | VARCHAR2(12) | Y |  | numero da nota que originou o titulo a receber |
| 36 | SERIE_DOCFIS_NF | VARCHAR2(3) | Y |  | serie da nota que originou o titulo a receber |
| 37 | SUB_SERIE_DOCFIS_NF | VARCHAR2(2) | Y |  | subserie da nota que originou o titulo a receber |
| 38 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 39 | IDENT_FIS_JUR_DMED | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_DOCTO_NF → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR_NF → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_FK_SAF_0295: (IDENT_FIS_JUR)
- IX_FK_SAF_2122: (IDENT_FIS_JUR_NF)
- IX_X05_NF_TIT: (NUM_DOCFIS_NF, DATA_FISCAL_NF, SERIE_DOCFIS_NF, SUB_SERIE_DOCFIS_NF, MOVTO_E_S_NF, IDENT_FIS_JUR_NF, IDENT_DOCTO_NF, COD_ESTAB, COD_EMPRESA)
- IX_X05_NF_TIT_01: (NUM_DOCFIS, DATA_EMISSAO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_DOCTO, COD_ESTAB, COD_EMPRESA)
- IX_X05_TIT_RECEBER_CTA: (IDENT_CONTA)

---

## X06_PERDA_GANHO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_GRP_COMB | NUMBER(12) | N |  |  |
| 5 | IND_PERDA_GANHO | CHAR(1) | N |  |  |
| 6 | QTD_COMB | NUMBER(17,6) | Y |  |  |
| 7 | QTD_GAS_A | NUMBER(17,6) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | QTD_EAC | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_GRP_COMB, IND_PERDA_GANHO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)

---

## X07_BASE_DOCFIS

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
| 11 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 12 | COD_TRIBUTACAO | NUMBER(1) | N |  |  |
| 13 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_TRIBUTO, COD_TRIBUTACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_TRIBUTO → X07_TRIB_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_TRIBUTO)
- COD_TRIBUTO, COD_TRIBUTACAO → TRIBUTACAO(COD_TRIBUTO, COD_TRIBUTACAO)

---

## X07_CUPOM_FISCAL

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
| 11 | NUM_MAQUINA | NUMBER(6) | Y |  |  |
| 12 | NUM_CUPOM_FINAL | NUMBER(6) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## X07_DOCTO_FISCAL

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
| 11 | DATA_EMISSAO | DATE | Y |  |  |
| 12 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 13 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 14 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 15 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 16 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 17 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 18 | S_SER_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 19 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 20 | DATA_SAIDA_REC | DATE | Y |  |  |
| 21 | INSC_ESTAD_SUBSTIT | VARCHAR2(14) | Y |  |  |
| 22 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 23 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 24 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 25 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_DIF_FRETE | NUMBER(17,2) | Y |  |  |
| 28 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 29 | CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 30 | SITUACAO | CHAR(1) | Y |  |  |
| 31 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 32 | VLR_NOTA_CONV | NUMBER(18,4) | Y |  |  |
| 33 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 34 | IND_MODELO_CUPOM | VARCHAR2(2) | Y |  |  |
| 35 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 36 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 37 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 38 | NUM_CONTROLE_DOCTO | VARCHAR2(12) | Y |  |  |
| 39 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 40 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 41 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 42 | VLR_OUTROS3 | NUMBER(17,2) | Y |  |  |
| 43 | VLR_OUTROS4 | NUMBER(17,2) | Y |  |  |
| 44 | VLR_OUTROS5 | NUMBER(17,2) | Y |  |  |
| 45 | VLR_ALIQ_OUTROS1 | NUMBER(7,4) | Y |  |  |
| 46 | VLR_ALIQ_OUTROS2 | NUMBER(7,4) | Y |  |  |
| 47 | IND_NF_ESPECIAL | CHAR(1) | Y |  |  |
| 48 | IND_TP_FRETE | CHAR(1) | Y |  |  |
| 49 | COD_MUNICIPIO | NUMBER(7) | Y |  |  |
| 50 | IND_TRANSF_CRED | CHAR(1) | Y |  |  |
| 51 | DAT_DI | DATE | Y |  |  |
| 52 | VLR_TOM_SERVICO | NUMBER(17,2) | Y |  |  |
| 53 | DAT_ESCR_EXTEMP | DATE | Y |  |  |
| 54 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 55 | COD_REGIAO | NUMBER(2) | Y |  |  |
| 56 | DAT_AUTENTIC | DATE | Y |  |  |
| 57 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 58 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 59 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 60 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 61 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 62 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 63 | VLR_MAT_APLIC_ISS | NUMBER(17,2) | Y |  |  |
| 64 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 65 | IND_MUNIC_ISS | CHAR(1) | Y |  |  |
| 66 | IND_CLASSE_OP_ISS | CHAR(1) | Y |  |  |
| 67 | DAT_FATO_GERADOR | DATE | Y |  |  |
| 68 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 69 | NUM_PAGINA | VARCHAR2(6) | Y |  |  |
| 70 | NUM_LIVRO | VARCHAR2(6) | Y |  |  |
| 71 | NRO_AIDF_NF | VARCHAR2(12) | Y |  |  |
| 72 | DAT_VALID_DOC_AIDF | DATE | Y |  |  |
| 73 | IND_FATURA | CHAR(1) | Y |  |  |
| 74 | IDENT_QUITACAO | NUMBER(12) | Y |  |  |
| 75 | NUM_SELO_CONT_ICMS | VARCHAR2(12) | Y |  |  |
| 76 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 77 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 78 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 79 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 80 | BASE_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 81 | VLR_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 82 | ALIQ_ICMS_ORIGDEST | NUMBER(7,4) | Y |  |  |
| 83 | VLR_DESC_CONDIC | NUMBER(17,2) | Y |  |  |
| 84 | PERC_RED_BASE_ICMS | NUMBER(7,4) | Y |  |  |
| 85 | IDENT_FISJUR_CPDIR | NUMBER(12) | Y |  |  |
| 86 | IND_MEDIDAJUDICIAL | CHAR(1) | Y |  |  |
| 87 | IDENT_UF_ORIG_DEST | NUMBER(12) | Y |  |  |
| 88 | IND_COMPRA_VENDA | VARCHAR2(2) | Y |  |  |
| 89 | COD_TP_DISP_SEG | VARCHAR2(2) | Y |  |  |
| 90 | NUM_CTR_DISP | NUMBER(10) | Y |  |  |
| 91 | NUM_FIM_DOCTO | VARCHAR2(12) | Y |  |  |
| 92 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 93 | SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 94 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | Y |  |  |
| 95 | IND_SITUACAO_ESP | CHAR(1) | Y |  |  |
| 96 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 97 | COD_PAGTO_INSS | VARCHAR2(4) | Y |  |  |
| 98 | DAT_OPERACAO | DATE | Y |  |  |
| 99 | USUARIO | VARCHAR2(40) | Y |  |  |
| 100 | DAT_INTERN_AM | DATE | Y |  |  |
| 101 | IDENT_FISJUR_LSG | NUMBER(12) | Y |  |  |
| 102 | COMPROV_EXP | VARCHAR2(15) | Y |  |  |
| 103 | NUM_FINAL_CRT_DISP | NUMBER(12) | Y |  |  |
| 104 | NUM_ALVARA | VARCHAR2(8) | Y |  |  |
| 105 | NOTIFICA_SEFAZ | VARCHAR2(14) | Y |  |  |
| 106 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 107 | COD_AMPARO | VARCHAR2(10) | Y |  |  |
| 108 | IDENT_ESTADO_AMPAR | NUMBER(12) | Y |  |  |
| 109 | IND_NOTA_SERVICO | CHAR(1) | Y |  |  |
| 110 | COD_MOTIVO | VARCHAR2(10) | Y |  |  |
| 111 | OBS_COMPL_MOTIVO | VARCHAR2(100) | Y |  |  |
| 112 | IND_TP_RET | CHAR(1) | Y |  |  |
| 113 | IND_TP_TOMADOR | CHAR(1) | Y |  |  |
| 114 | COD_ANTEC_ST | CHAR(1) | Y |  |  |
| 115 | CNPJ_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 116 | IDENT_UF_ARMAZ_ORIG | NUMBER(12) | Y |  |  |
| 117 | INS_EST_ARMAZ_ORIG | VARCHAR2(14) | Y |  |  |
| 118 | CNPJ_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 119 | IDENT_UF_ARMAZ_DEST | NUMBER(12) | Y |  |  |
| 120 | INS_EST_ARMAZ_DEST | VARCHAR2(14) | Y |  |  |
| 121 | OBS_INF_ADIC_NF | VARCHAR2(250) | Y |  |  |
| 122 | VLR_BASE_INSS_2 | NUMBER(17,2) | Y |  |  |
| 123 | VLR_ALIQ_INSS_2 | NUMBER(7,4) | Y |  |  |
| 124 | VLR_INSS_RETIDO_2 | NUMBER(17,2) | Y |  |  |
| 125 | COD_PAGTO_INSS_2 | VARCHAR2(4) | Y |  |  |
| 126 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 127 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 128 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 129 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 130 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 131 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 132 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 133 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 134 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 135 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 136 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 137 | BASE_ICMSS_SUBSTITUIDO | NUMBER(17,2) | Y |  | Base ICMS-S Substituído - Base de ICMSS informado pelo fornecedor na situação de substituído. |
| 138 | VLR_ICMSS_SUBSTITUIDO | NUMBER(17,2) | Y |  | Valor ICMS-S Substituído - Valor informado pelo fornecedor na situação de substituído. |
| 139 | COD_CEI | VARCHAR2(15) | Y |  |  |
| 140 | VLR_JUROS_INSS | NUMBER(17,2) | Y |  |  |
| 141 | VLR_MULTA_INSS | NUMBER(17,2) | Y |  |  |
| 142 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  | Indicador de situacao especial de subst. tributaria, utilizado no atendimento aos livros fiscais conforme Resolucao 119/04 do RJ. Os possiveis valores sao: 1 - NF art. 1º/2 - NF art. 2º e 3 - NF devoluacao ou remessa art. 4º |
| 143 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  | Valor de ICMS-S nao escriturado, este campo foi criado para atendimento dos livros ficais conforme a Resolucao 119/04 do RJ. |
| 144 | IND_DOCTO_REC | CHAR(1) | Y |  | Natureza do documento conforme Resolucao 119/04 do RJ, seus possiveis valores sao: 1 - DARJ/2 - GNRE. |
| 145 | DAT_PGTO_GNRE_DARJ | DATE | Y |  | Data de pagamento do respectivo DARJ ou GNRE conforme Resolucao 119/04 do RJ |
| 146 | DT_PAGTO_NF | DATE | Y |  |  |
| 147 | IND_ORIGEM_INFO | CHAR(1) | Y | '0' | 0-Normal;1-Mapa Resumo |
| 148 | NUM_CICLO | VARCHAR2(7) | Y |  | Numero do Ciclo para Mapa Resumo |
| 149 | HORA_SAIDA | NUMBER(6) | Y |  | hora de saida das mercadorias - ato cotepe 35/05 |
| 150 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  | código da situação do doc. fiscal: 00 - lançamento regular, 01 - extemporâneo, 02 - cancelado, 03 - cancelamento de cupom fiscal anterior, 04 - extemporâneo cancelado, 05 - desfazimento de negócio, 06 - documento referenciado - ato cotepe 35/05 |
| 151 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 35/05 |
| 152 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 153 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 154 | COD_MUNICIPIO_ORIG | NUMBER(5) | Y |  | ATO COTEPE 70 - reg D030: Município de origem do serviço. |
| 155 | COD_MUNICIPIO_DEST | NUMBER(5) | Y |  | ATO COTEPE 70 - reg D030: Município de destino do serviço. |
| 156 | COD_CFPS | VARCHAR2(4) | Y |  | ATO COTEPE 70 - reg A020: Código Fiscal de Prestação de Serviço. |
| 157 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  | ATO COTEPE 70 - reg B020: Número do Lançamento Contábil. |
| 158 | VLR_MAT_PROP | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do Material Próprio utilizado na prestação do serviço. |
| 159 | VLR_MAT_TERC | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do Material de Terceiros utilizado na prestação do serviço. |
| 160 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor da Base de Cálculo de Retenção de ISSQN. |
| 161 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do ISSQN retido pelo tomador. |
| 162 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg B020: Valor de dedução da base de cálculo do ISSQN. |
| 163 | COD_MUNIC_ARMAZ_ORIG | NUMBER(5) | Y |  | ATO COTEPE 70 - reg C255, D185: Município do armazém de origem - local de coleta. |
| 164 | INS_MUNIC_ARMAZ_ORIG | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C255, D185: Inscrição Municípal do armazém de origem - local de coleta. |
| 165 | COD_MUNIC_ARMAZ_DEST | NUMBER(5) | Y |  | ATO COTEPE 70 - reg C255, D185: Município do armazém de destino - local de entrega. |
| 166 | INS_MUNIC_ARMAZ_DEST | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C255, D185: Inscrição Municípal do armazém de destino - local de entrega. |
| 167 | IDENT_CLASSE_CONSUMO | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C700, D400 - UTILITIES: Código da Classe de Consumo  (energia elétrica, gás, água, telecomunicação, comunicação) - DWT_CLASSE_CONSUMO. |
| 168 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  | ATO COTEPE 70 - reg C700, D400 - UTILITIES: Especificação do Tipo de Receita (energia elétrica, gás, água, telecomunicação, comunicação). Valores Assumidos: 0 - Receita Própria - serviços prestados; 1 - Receita Própria - cobrança de débitos; 2 - Receita Própria - venda de mercadorias; 3 - Receita Própria - venda de serviço pré-pago; 4 - Outras Receitas Próprias; 5 - Receita de Terceiros (co-faturamento); 9 - Outras Receitas de Terceiros. |
| 169 | NUM_CONTRATO | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C705, D405 - UTILITIES: Número do Contrato, ou Código da Unidade de Consumo (energia elétrica), ou Identificação do Terminal Faturado (telecomunicação, comunicação). |
| 170 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg D405 - UTILITIES: Código da Área do Terminal Faturado (telecomunicação, comunicação). |
| 171 | COD_TP_UTIL | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C705, D405 - UTILITIES:Tipo de Ligação (energia elétrica), ou Tipo de Utilização (telecomunicação, comunicação). Preenchimento conforme tabela 11.2 do Convênio 115/133. |
| 172 | GRUPO_TENSAO | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES: Grupo de tensão (energia elétrica). Preenchimento conforme tabela 11.3 do Convênio 115/133. |
| 173 | DATA_CONSUMO_INI | DATE | Y |  | ATO COTEPE 70 - reg C705, D405 - UTILITIES: Data início do consumo de energia (energia elétrica), ou data início da prestação do serviço(telecomunicação, comunicação). |
| 174 | DATA_CONSUMO_FIM | DATE | Y |  | ATO COTEPE 70 - reg C705, D405 - UTILITIES: Data final do consumo de energia (energia elétrica), ou data final da prestação do serviço(telecomunicação, comunicação). |
| 175 | DATA_CONSUMO_LEIT | DATE | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES: Data da leitura do ponto de consumo (energia elétrica). |
| 176 | QTD_CONTRATADA_PONTA | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES: Demanda contratada Ponta, KW (energia elétrica). |
| 177 | QTD_CONTRATADA_FPONTA | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES:  Demanda contratada Fora-Ponta, KW (energia elétrica). |
| 178 | QTD_CONSUMO_TOTAL | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 - UTILITIES: Consumo Total, KW(energia elétrica). |
| 179 | IDENT_UF_CONSUMO | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C770, D470 - UTILITIES: UF do Ponto de Consumo (energia elétrica, gás, água), ou UF do Terminal Faturado (telecomunicação, comunicação). |
| 180 | COD_MUNIC_CONSUMO | NUMBER(5) | Y |  | ATO COTEPE 70 - reg C770, D470 - UTILITIES: Município do Ponto de Consumo (energia elétrica, gás, água), ou Município do Terminal Faturado (telecomunicação, comunicação). |
| 181 | COD_OPER_ESP_ST | CHAR(1) | Y |  | Atendimento DIEF-PA - Registro 88 Subtipo 23 (Numero da Operacao) |
| 182 | ATO_NORMATIVO | VARCHAR2(20) | Y |  | SEF-PE: Ato Normativo |
| 183 | NUM_ATO_NORMATIVO | NUMBER(5) | Y |  | SEF-PE: Número do Ato Normativo |
| 184 | ANO_ATO_NORMATIVO | NUMBER(4) | Y |  | SEF-PE: Ano do Ato Normativo |
| 185 | CAPITULACAO_NORMA | VARCHAR2(30) | Y |  | SEF-PE: Capitulação da Norma |
| 186 | VLR_OUTRAS_ENTID | NUMBER(17,2) | Y |  | Valor de outras Entidades |
| 187 | VLR_TERCEIROS | NUMBER(17,2) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 188 | IND_TP_COMPL_ICMS | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg E020: Ind Compl. |
| 189 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 190 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 191 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 192 | COD_VERIFIC_NFE | VARCHAR2(60) | Y |  | Codigo de verificacao da nota fiscal eletronica. |
| 193 | COD_TP_RPS_NFE | VARCHAR2(5) | Y |  | Codigo do tipo de RPS (recibo provisorio de servico) da nota fiscal eletronica. |
| 194 | NUM_RPS_NFE | NUMBER(12) | Y |  | Numero do RPS (recibo provisorio de servico) da nota fiscal eletronica. |
| 195 | SERIE_RPS_NFE | VARCHAR2(5) | Y |  | Serie do RPS (recibo provisorio de servico) da nota fiscal eletronica. |
| 196 | DAT_EMISSAO_RPS_NFE | DATE | Y |  | Data de Emissao do RPS (recibo provisorio de servico) da nota fiscal eletronica. |
| 197 | DSC_SERVICO_NFE | VARCHAR2(1000) | Y |  | Descricao dos servicos da nota fiscal eletronica. |
| 198 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  | Numero de autenticacao (hashcode) da nota fiscal eletronica de ICMS. |
| 199 | NUM_DV_NFE | NUMBER(1) | Y |  | Numero do dígito verificador da chave de acesso que compõe da nota fiscal eletronica de ICMS. |
| 200 | MODELO_NF_DMS | VARCHAR2(3) | Y |  | Modelo da Nota Fiscal para a série U ou M em atendimento a DMS Campo Grande - Mato Grosso do Sul. |
| 201 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 202 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 203 | IND_NFE_DENEG_INUT | NUMBER(1) | Y |  | NFE DENEGADA/INUTILIZADA |
| 204 | IND_NF_REG_ESPECIAL | VARCHAR2(1) | Y |  | NF BASEADA EM REGIME ESPECIAL OU NORMA ESPECIFICA |
| 205 | VLR_ABAT_NTRIBUTADO | NUMBER(17,2) | Y |  | VALOR ABATIMENTO NÃO TRIBUTADO |
| 206 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  | Campo criado para gerar o registro 90 da DAPI MG, recuperando as informações da Apuração do ICMS automaticamente. |
| 207 | HORA_EMISSAO | NUMBER(6) | Y |  | hora, minuto e segundo no qual a NF foi emitida |
| 208 | OBS_DADOS_FATURA | VARCHAR2(256) | Y |  | observação contida no campo dados da fatura das NFs Modelo 1 e 1A recebidas e emitidas |
| 209 | HORA_SAIDA_REC | NUMBER(6) | Y |  |  |
| 210 | IDENT_FIS_CONCES | NUMBER(12) | Y |  |  |
| 211 | COD_AUTENTIC | VARCHAR2(32) | Y |  | Codigo de Autenticação utilizado para Portaria CAT44 - SP |
| 212 | IND_PORT_CAT44 | CHAR(1) | Y |  | Indicador se o regiastro vai ser utilizadona CAT44 ou  não |
| 213 | NUM_AUTENTIC_NFE_AUX | NUMBER(9) | Y |  |  |
| 214 | VLR_BASE_INSS_RURAL | NUMBER(17,2) | Y |  |  |
| 215 | VLR_ALIQ_INSS_RURAL | NUMBER(7,4) | Y |  |  |
| 216 | VLR_INSS_RURAL | NUMBER(17,2) | Y |  |  |
| 217 | IDENT_CLASSE_CONSUMO_SEF_PE | NUMBER(12) | Y |  |  |
| 218 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 219 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 220 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 221 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 222 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 223 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 224 | IND_NAT_FRETE | CHAR(1) | Y |  |  |
| 225 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  |  |
| 226 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 227 | IND_VENDA_CANC | CHAR(1) | Y |  |  |
| 228 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 229 | IND_NF_CONTINGENCIA | VARCHAR2(1) | Y |  |  |
| 230 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 231 | VLR_ANTECIP_TRIB | NUMBER(17,2) | Y |  |  |
| 232 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 233 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 234 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 235 | NUM_NFTS | VARCHAR2(12) | Y |  |  |
| 236 | IND_NF_VENDA_TERCEIROS | CHAR(1) | Y |  | Indicador de Nota Fiscal de Venda de Mercadoria Emitida por Terceiros |
| 237 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 238 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 239 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 240 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 241 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 242 | IDENTIF_DOCFIS | VARCHAR2(128) | Y |  |  |
| 243 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 244 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 245 | IND_PREST_SERV | CHAR(1) | Y |  |  |
| 246 | IND_TIPO_PROC | CHAR(1) | Y |  |  |
| 247 | NUM_PROC_JUR | VARCHAR2(20) | Y |  |  |
| 248 | IND_DEC_PROC | CHAR(1) | Y |  |  |
| 249 | IND_TIPO_AQUIS | CHAR(1) | Y |  |  |
| 250 | VLR_DESC_GILRAT | NUMBER(17,2) | Y |  |  |
| 251 | VLR_DESC_SENAR | NUMBER(17,2) | Y |  |  |
| 252 | CNPJ_SUBEMPREITEIRO | VARCHAR2(14) | Y |  |  |
| 253 | CNPJ_CPF_PROPRIETARIO_CNO | VARCHAR2(14) | Y |  |  |
| 254 | VLR_RET_SUBEMPREITADO | NUMBER(17,2) | Y |  |  |
| 255 | NUM_DOCFIS_SERV | VARCHAR2(60) | Y |  |  |
| 256 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 257 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 258 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 259 | VLR_CONTRIB_PREV | NUMBER(17,2) | Y |  |  |
| 260 | VLR_GILRAT | NUMBER(17,2) | Y |  |  |
| 261 | VLR_CONTRIB_SENAR | NUMBER(17,2) | Y |  |  |
| 262 | CPF_CNPJ | VARCHAR2(14) | Y |  |  |
| 263 | NUM_CERTIF_QUAL | VARCHAR2(10) | Y |  |  |
| 264 | OBS_REINF | VARCHAR2(250) | Y |  |  |
| 265 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 266 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 267 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 268 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 269 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 270 | VLR_IPI_DEV | NUMBER(17,2) | Y |  |  |
| 271 | VLR_SEST | NUMBER(17,2) | Y |  |  |
| 272 | VLR_SENAT | NUMBER(17,2) | Y |  |  |
| 273 | IND_FIN_EMISSAO_NFE | VARCHAR2(1) | Y |  |  |
| 274 | NUM_AUTENTIC_NFE_SUBST | VARCHAR2(80) | Y |  |  |
| 275 | IND_VLR_ICMS_COB_ANT_ST | VARCHAR2(1) | Y |  |  |
| 276 | IND_TRIB_PRODUTOR_CP | VARCHAR2(1) | Y |  | Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária. 1 - Sobre a comercialização da sua produção; 2 - Sobre a folha de pagamento. Valores Válidos: 1, 2. |
| 277 | IDENT_MODELO_NFE_SUBST | NUMBER(12) | Y |  |  |
| 278 | COD_AUTENTIC_NFE_SUBST | VARCHAR2(32) | Y |  |  |
| 279 | VLR_ENERGIA_INJ | NUMBER(17,2) | Y |  |  |
| 280 | VLR_OUTRAS_DED | NUMBER(17,2) | Y |  |  |
| 281 | IND_TP_FAT_NFE | VARCHAR2(1) | Y |  |  |
| 282 | IND_TP_AMB_NFE | VARCHAR2(1) | Y |  |  |
| 283 | COD_NF_NFE | VARCHAR2(7) | Y |  |  |
| 284 | IND_PRE_PAGO | VARCHAR2(1) | Y |  |  |
| 285 | IND_SESSAO_REDE | VARCHAR2(1) | Y |  |  |
| 286 | DAT_INI_CONTRATO | DATE | Y |  |  |
| 287 | DAT_FIM_CONTRATO | DATE | Y |  |  |
| 288 | NUM_TERMINAL_TEL | VARCHAR2(12) | Y |  |  |
| 289 | IDENT_UF_TERMINAL_TEL | NUMBER(12) | Y |  |  |
| 290 | VLR_ICMS_DESONERADO | NUMBER(17,2) | Y |  |  |
| 291 | VLR_FCP | NUMBER(17,2) | Y |  |  |
| 292 | VLR_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 293 | VLR_FUST | NUMBER(17,2) | Y |  |  |
| 294 | CNPJ_DOWNLOAD | VARCHAR2(14) | Y |  |  |
| 295 | CPF_DOWNLOAD | VARCHAR2(11) | Y |  |  |
| 296 | VLR_CSLL_RETIDO | NUMBER(17,2) | Y |  |  |
| 297 | VLR_IRRF_RETIDO | NUMBER(17,2) | Y |  |  |
| 298 | INSC_EST_VIRTUAL | VARCHAR2(14) | Y |  |  |
| 299 | PERIOD_APUR_SUBST | VARCHAR2(6) | Y |  |  |
| 300 | COD_MOTIVO_SUBST | VARCHAR2(2) | Y |  |  |
| 301 | COD_AUTENTIC_COF | VARCHAR2(44) | Y |  |  |
| 302 | CNPJ_EMIT_FATURAMENTO | VARCHAR2(14) | Y |  |  |
| 303 | IDENT_UF_EMIT_FATURAMENTO | NUMBER(12) | Y |  |  |
| 304 | DAT_CRIACAO | DATE | Y |  |  |
| 305 | DAT_ALTERACAO | DATE | Y |  |  |
| 306 | CNPJ_EMIT_COF | VARCHAR2(14) | Y |  |  |
| 307 | IDENT_MODELO_COF | NUMBER(12) | Y |  |  |
| 308 | SERIE_DOCFIS_COF | VARCHAR2(3) | Y |  |  |
| 309 | NUM_DOCFIS_COF | VARCHAR2(12) | Y |  |  |
| 310 | ANO_MES_COF | VARCHAR2(6) | Y |  |  |
| 311 | COD_HASH_COF | VARCHAR2(32) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)
- COD_REGIAO → DWT_REGIOES(COD_REGIAO)
- COD_CANAL_DISTRIB → DWT_CANAIS_DISTRIB(COD_CANAL_DISTRIB)
- COD_MUNICIPIO → X2097_MUNIC_ISS(COD_MUNIC_ISS)
- IDENT_FISJUR_CPDIR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_QUITACAO → X2014_QUITACAO(IDENT_QUITACAO)
- COD_PAGTO_INSS_2 → IRT_COD_PG_INSS(COD_PAGTO)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_UF_ORIG_DEST, COD_MUNICIPIO_ORIG → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_UF_DESTINO, COD_MUNICIPIO_DEST → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- COD_CFPS → DWT_COD_FISCAL_SERV(COD_CFPS)
- IDENT_UF_ARMAZ_ORIG, COD_MUNIC_ARMAZ_ORIG → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_UF_ARMAZ_DEST, COD_MUNIC_ARMAZ_DEST → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_CLASSE_CONSUMO → DWT_CLASSE_CONSUMO(IDENT_CLASSE_CONSUMO)
- IDENT_UF_CONSUMO, COD_MUNIC_CONSUMO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_FIS_CONCES → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_CLASSE_CONSUMO_SEF_PE → DWT_CLASSE_CONSUMO(IDENT_CLASSE_CONSUMO)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)
- IDENT_MODELO_NFE_SUBST → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_UF_TERMINAL_TEL → ESTADO(IDENT_ESTADO)
- IDENT_UF_EMIT_FATURAMENTO → ESTADO(IDENT_ESTADO)

**Indexes**:
- IX_FK_SAF_0107: (IDENT_FIS_JUR)
- IX_FK_SAF_1223: (IDENT_FISJUR_CPDIR)
- IX_FK_SAF_2076: (IDENT_OBSERVACAO)
- IX_FK_SAF_2213: (IDENT_FIS_CONCES)
- IX_X07_DOCTO_CONTROL: (NUM_CONTROLE_DOCTO, COD_CLASS_DOC_FIS, COD_EMPRESA, COD_ESTAB, DATA_FISCAL)
- IX_X07_DOCTO_FISCAL_CTA: (IDENT_CONTA)

---

## X07_TRIB_DOCFIS

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
| 11 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 12 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 13 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 14 | DIF_ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 15 | OBS_TRIBUTO | VARCHAR2(45) | Y |  |  |
| 16 | IDENT_DET_OPERACAO | NUMBER(12) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 19 | IND_CRED_TRIBUTO | CHAR(1) | Y |  |  |
| 20 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_TRIBUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_TRIBUTO → TRIBUTO(COD_TRIBUTO)
- IDENT_DET_OPERACAO → DETALHE_OPERACAO(IDENT_DET_OPERACAO)

---

## X08_BASE_MERC

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
| 12 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 13 | COD_TRIBUTACAO | NUMBER(1) | N |  |  |
| 14 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, COD_TRIBUTO, COD_TRIBUTACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, COD_TRIBUTO → X08_TRIB_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, COD_TRIBUTO)
- COD_TRIBUTO, COD_TRIBUTACAO → TRIBUTACAO(COD_TRIBUTO, COD_TRIBUTACAO)

---

## X08_ITENS_MERC

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
| 12 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 13 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 14 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 15 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 16 | VALID_BEM | DATE | Y |  |  |
| 17 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 18 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 19 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 20 | DESCRICAO_COMPL | VARCHAR2(255) | Y |  |  |
| 21 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 22 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 23 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 24 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 25 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 26 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 27 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 28 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 29 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 30 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 31 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 32 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 33 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 34 | IDENT_FEDERAL | NUMBER(12) | Y |  |  |
| 35 | IND_IPI_INCLUSO | CHAR(1) | Y |  |  |
| 36 | NUM_ROMANEIO | VARCHAR2(12) | Y |  |  |
| 37 | DATA_ROMANEIO | DATE | Y |  |  |
| 38 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 39 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 40 | VLR_ITEM_CONVER | NUMBER(17,2) | Y |  |  |
| 41 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 42 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 43 | VLR_CONTAB_COMPL | NUMBER(17,2) | Y |  |  |
| 44 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 45 | VLR_OUTROS1 | NUMBER(17,2) | Y |  |  |
| 46 | VLR_OUTROS2 | NUMBER(17,2) | Y |  |  |
| 47 | VLR_OUTROS3 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_OUTROS4 | NUMBER(17,2) | Y |  |  |
| 49 | VLR_OUTROS5 | NUMBER(17,2) | Y |  |  |
| 50 | VLR_ALIQ_OUTROS1 | NUMBER(7,4) | Y |  |  |
| 51 | VLR_ALIQ_OUTROS2 | NUMBER(7,4) | Y |  |  |
| 52 | VLR_CONTAB_ITEM | NUMBER(17,2) | Y |  |  |
| 53 | COD_OBS_VCONT_COMP | VARCHAR2(10) | Y |  |  |
| 54 | COD_OBS_VCONT_ITEM | VARCHAR2(10) | Y |  |  |
| 55 | VLR_OUTROS_ICMS | NUMBER(17,2) | Y |  |  |
| 56 | VLR_OUTROS_IPI | NUMBER(17,2) | Y |  |  |
| 57 | IND_RESP_VCONT_ITM | CHAR(1) | Y |  |  |
| 58 | NUM_ATO_CONCES | VARCHAR2(15) | Y |  |  |
| 59 | DAT_EMBARQUE | DATE | Y |  |  |
| 60 | NUM_REG_EXP | VARCHAR2(12) | Y |  |  |
| 61 | NUM_DESP_EXP | VARCHAR2(11) | Y |  |  |
| 62 | VLR_TOM_SERVICO | NUMBER(17,2) | Y |  |  |
| 63 | VLR_DESP_MOEDA_EXP | NUMBER(17,2) | Y |  |  |
| 64 | COD_MOEDA_NEGOC | VARCHAR2(10) | Y |  |  |
| 65 | COD_PAIS_DEST_ORIG | VARCHAR2(3) | Y |  |  |
| 66 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 67 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 68 | VLR_IPI_NDESTAC | NUMBER(17,2) | Y |  |  |
| 69 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 70 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 71 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 72 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 73 | BASE_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 74 | VLR_ICMS_ORIGDEST | NUMBER(17,2) | Y |  |  |
| 75 | ALIQ_ICMS_ORIGDEST | NUMBER(7,4) | Y |  |  |
| 76 | VLR_DESC_CONDIC | NUMBER(17,2) | Y |  |  |
| 77 | VLR_CUSTO_TRANSF | NUMBER(17,6) | Y |  |  |
| 78 | PERC_RED_BASE_ICMS | NUMBER(7,4) | Y |  |  |
| 79 | QTD_EMBARCADA | NUMBER(17,6) | Y |  |  |
| 80 | DAT_REGISTRO_EXP | DATE | Y |  |  |
| 81 | DAT_DESPACHO | DATE | Y |  |  |
| 82 | DAT_AVERBACAO | DATE | Y |  |  |
| 83 | DAT_DI | DATE | Y |  |  |
| 84 | NUM_DEC_IMP_REF | VARCHAR2(15) | Y |  |  |
| 85 | DSC_MOT_OCOR | VARCHAR2(45) | Y |  |  |
| 86 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 87 | VLR_BASE_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 88 | VLR_TRIB_ICMS_ORIG | NUMBER(17,2) | Y |  |  |
| 89 | VLR_BASE_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 90 | VLR_TRIB_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 91 | VLR_PERC_PRES_ICMS | NUMBER(7,4) | Y |  |  |
| 92 | VLR_PRECO_BASE_ST | NUMBER(17,2) | Y |  |  |
| 93 | IDENT_OPER_OIL | NUMBER(12) | Y |  |  |
| 94 | COD_DCR | VARCHAR2(15) | Y |  |  |
| 95 | IDENT_PROJETO | NUMBER(12) | Y |  |  |
| 96 | DAT_OPERACAO | DATE | Y |  |  |
| 97 | USUARIO | VARCHAR2(40) | Y |  |  |
| 98 | IND_MOV_FIS | CHAR(1) | Y |  |  |
| 99 | CHASSI | VARCHAR2(17) | Y |  |  |
| 100 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 101 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 102 | SSERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 103 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 104 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 105 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 106 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 107 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 108 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 109 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 110 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 111 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 112 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 113 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 114 | IND_SITUACAO_ESP_ST | CHAR(1) | Y |  | Indicador de situacao especial de subst. tributaria, utilizado no atendimento aos livros fiscais conforme Resolucao 119/04 do RJ. Os possiveis valores sao: 1 - NF art. 1º/2 - NF art. 2º e 3 - NF devoluacao ou remessa art. 4º |
| 115 | VLR_ICMSS_NDESTAC | NUMBER(17,2) | Y |  | Valor de ICMS-S nao escriturado, este campo foi criado para atendimento dos livros ficais conforme a Resolucao 119/04 do RJ. |
| 116 | IND_DOCTO_REC | CHAR(1) | Y |  | Natureza do documento conforme Resolucao 119/04 do RJ, seus possiveis valores sao: 1 - DARJ/2 - GNRE. |
| 117 | DAT_PGTO_GNRE_DARJ | DATE | Y |  | Data de pagamento do respectivo DARJ ou GNRE conforme Resolucao 119/04 do RJ |
| 118 | VLR_CUSTO_UNIT | NUMBER(17,2) | Y |  |  |
| 119 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 120 | QUANTIDADE_CONV | NUMBER(17,6) | Y |  |  |
| 121 | VLR_FECP_ICMS | NUMBER(17,2) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 122 | VLR_FECP_DIFALIQ | NUMBER(17,2) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 123 | VLR_FECP_ICMS_ST | NUMBER(17,2) | Y |  | Campo utilizado para lancamento de amparo legal na GIA-RJ |
| 124 | VLR_FECP_FONTE | NUMBER(17,2) | Y |  | Campo utilizado para lancamento do valor do FUNCEP ref a Regime Fonte - GIM-PB |
| 125 | VLR_BASE_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  | Valor base do ICMS-ST não escriturado |
| 126 | VLR_ICMSS_N_ESCRIT | NUMBER(17,2) | Y |  | Valor do ICMS-ST não escriturado |
| 127 | VLR_AJUSTE_COND_PG | NUMBER(17,2) | Y |  |  |
| 128 | COD_TRIB_IPI | VARCHAR2(2) | Y |  | código de tributação do IPI - CTIPI - ato cotepe 35/05 |
| 129 | LOTE_MEDICAMENTO | VARCHAR2(50) | Y |  | número do lote de fabricação do medicamento - ato cotepe 35/05 |
| 130 | VALID_MEDICAMENTO | DATE | Y |  | data de expedição da validade do medicamento - ato cotepe 35/05 |
| 131 | IND_BASE_MEDICAMENTO | CHAR(1) | Y |  | indicador do tipo da base de cálculo: 0 - BC ref ao preço tabelado ou preço máximo, 1 - BC ref à Lista Negativa, 2 - BC ref à Lista Positiva, 3 - BC ref à Lista Neutra  - ato cotepe 35/05 |
| 132 | VLR_PRECO_MEDICAMENTO | NUMBER(17,2) | Y |  | valor do preço tabelado ou máximo do medicamento - ato cotepe 35/05 |
| 133 | IND_TIPO_ARMA | CHAR(1) | Y |  | indicador do tipo de arma: 0- uso permitido, 1 - uso restrito - ato cotepe 35/05 |
| 134 | NUM_SERIE_ARMA | VARCHAR2(50) | Y |  | numeração de série de fabricação da arma - ato cotepe 35/05 |
| 135 | NUM_CANO_ARMA | VARCHAR2(50) | Y |  | numeração de série de fabricação do cano - ato cotepe 35/05 |
| 136 | DSC_ARMA | VARCHAR2(100) | Y |  | descrição da arma - ato cotepe 35/05 |
| 137 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 35/05 |
| 138 | COD_EX_NCM | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C300: Código EX, conforme a TIPI. |
| 139 | COD_EX_IMP | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C300: Código EX do Imposto de Importação. |
| 140 | CNPJ_OPERADORA | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: CNPJ do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 141 | CPF_OPERADORA | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: CPF do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 142 | IDENT_UF_OPERADORA | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: UF do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 143 | INS_EST_OPERADORA | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: Inscrição Estadual do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 144 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: Especificação do Tipo de Receita (energia elétrica, gás, água, telecomunicação, comunicação). Valores Assumidos: 0 - Receita Própria - serviços prestados; 1 - Receita Própria - cobrança de débitos; 2 - Receita Própria - venda de mercadorias; 3 - Receita Própria - venda de serviço pré-pago; 4 - Outras Receitas Próprias; 5 - Receita de Terceiros (co-faturamento); 9 - Outras Receitas de Terceiros. |
| 145 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  | ATO COTEPE 70 - reg C750, D450 - UTILITIES: Classificação do Item. Preenchimento conforme tabela 11.5 do Convênio 115/133 (energia elétrica, gás, água, telecomunicação, comunicação). |
| 146 | VLR_TERCEIROS | NUMBER(17,2) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 147 | VLR_PRECO_SUGER | NUMBER(17,2) | Y |  | Valor do preco sugerido do produto - Meio Magnetico - Reg78 - CAT 90 - SP |
| 148 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 149 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 150 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 151 | COD_OPER_ESP_ST | CHAR(1) | Y |  | Atendimento DIEF-PA. |
| 152 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 153 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 154 | VLR_DIFAL_FRETE | NUMBER(17,2) | Y |  |  |
| 155 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' | Indicador para verificar se os valores de PIS/COFINS estao destacados no documentos fiscal |
| 156 | COD_ENQUAD_IPI | VARCHAR2(3) | Y |  | Código de Enquadramento Legal do IPI |
| 157 | COD_SITUACAO_PIS | NUMBER(2) | Y |  | Codigo da Situação Tributaria do PIS |
| 158 | QTD_BASE_PIS | NUMBER(18,3) | Y |  | Quantidade de Base de Calculo do PIS |
| 159 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  | VALOR DA ALIQUOTA DO PIS EM REAIS |
| 160 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  | CODIGO DA SITUAÇÃO TRIBUTARIA DO COFINS |
| 161 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  | Quantidade de Base de Calculo do COFINS |
| 162 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  | VALOR DA ALIQUOTA DO COFINS EM REAIS |
| 163 | ITEM_PORT_TARE | VARCHAR2(2) | Y |  |  |
| 164 | VLR_FUNRURAL | NUMBER(17,2) | Y |  | Campo criado para gerar o registro 88NFRA do sintegra. |
| 165 | IND_TP_PROD_MEDIC | CHAR(1) | Y |  |  |
| 166 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 167 | COD_TP_LANCTO | NUMBER(6) | Y |  |  |
| 168 | VLR_PERC_CRED_OUT | NUMBER(7,4) | Y |  |  |
| 169 | VLR_CRED_OUT | NUMBER(17,2) | Y |  |  |
| 170 | VLR_ICMS_DCA | NUMBER(21,6) | Y |  |  |
| 171 | VLR_PIS_EXP | NUMBER(17,2) | Y |  |  |
| 172 | VLR_PIS_TRIB | NUMBER(17,2) | Y |  |  |
| 173 | VLR_PIS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 174 | VLR_COFINS_EXP | NUMBER(17,2) | Y |  |  |
| 175 | VLR_COFINS_TRIB | NUMBER(17,2) | Y |  |  |
| 176 | VLR_COFINS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 177 | COD_ENQ_LEGAL | NUMBER(4) | Y |  |  |
| 178 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |
| 179 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 180 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 181 | IND_NATUREZA_FRETE | CHAR(1) | Y |  |  |
| 182 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 183 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 184 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 185 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 186 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 187 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 188 | COD_TRIB_PROD | VARCHAR2(4) | Y |  |  |
| 189 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 190 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 191 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 192 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 193 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 194 | INDICE_PROD_ACAB | VARCHAR2(3) | Y |  |  |
| 195 | VLR_BASE_DIA_AM | NUMBER(17,2) | Y |  |  |
| 196 | VLR_ALIQ_DIA_AM | NUMBER(7,4) | Y |  |  |
| 197 | VLR_ICMS_DIA_AM | NUMBER(17,2) | Y |  |  |
| 198 | VLR_ADUANEIRO | NUMBER(17,2) | Y |  |  |
| 199 | COD_SITUACAO_PIS_ST | NUMBER(2) | Y |  |  |
| 200 | COD_SITUACAO_COFINS_ST | NUMBER(2) | Y |  |  |
| 201 | VLR_ALIQ_DCIP | NUMBER(7,4) | Y |  |  |
| 202 | NUM_LI | VARCHAR2(10) | Y |  |  |
| 203 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 204 | VLR_ICMS_UF_DEST | NUMBER(17,2) | Y |  |  |
| 205 | VLR_ICMS_UF_ORIG | NUMBER(17,2) | Y |  |  |
| 206 | VLR_DIF_DUB | NUMBER(17,2) | Y |  |  |
| 207 | VLR_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 208 | VLR_BASE_ICMS_NAO_DEST | NUMBER(17,2) | Y |  |  |
| 209 | VLR_ALIQ_ICMS_NAO_DEST | NUMBER(7,4) | Y |  |  |
| 210 | IND_MOTIVO_RES | CHAR(1) | Y |  |  |
| 211 | NUM_DOCFIS_RET | VARCHAR2(12) | Y |  |  |
| 212 | SERIE_DOCFIS_RET | VARCHAR2(3) | Y |  |  |
| 213 | NUM_AUTENTIC_NFE_RET | VARCHAR2(80) | Y |  |  |
| 214 | NUM_ITEM_RET | NUMBER(5) | Y |  |  |
| 215 | IDENT_FIS_JUR_RET | NUMBER(12) | Y |  |  |
| 216 | IND_TP_DOC_ARREC | CHAR(1) | Y |  |  |
| 217 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 218 | IDENT_CFO_DCIP | NUMBER(12) | Y |  |  |
| 219 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 220 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 221 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 222 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 223 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 224 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 225 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 226 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 227 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 228 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 229 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 230 | IDENT_PROC_ADJ_PRINC | NUMBER(12) | Y |  |  |
| 231 | IDENT_SUSP_TBT_PRINC | NUMBER(12) | Y |  |  |
| 232 | NUM_PROC_ADJ_PRINC | VARCHAR2(21) | Y |  |  |
| 233 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 234 | IDENT_PROC_ADJ_ADIC | NUMBER(12) | Y |  |  |
| 235 | IDENT_SUSP_TBT_ADIC | NUMBER(12) | Y |  |  |
| 236 | NUM_PROC_ADJ_ADIC | VARCHAR2(21) | Y |  |  |
| 237 | VLR_IPI_DEV | NUMBER(17,2) | Y |  |  |
| 238 | COD_BENEFICIO | VARCHAR2(10) | Y |  |  |
| 239 | VLR_ABAT_NTRIBUTADO | NUMBER(17,2) | Y |  |  |
| 240 | VLR_CREDITO_MVA_SN | NUMBER(17,2) | Y |  |  |
| 241 | VLR_DESONERADO_ICMS | NUMBER(17,2) | Y |  | Informar o valor desonerado do ICMS.  Este valor será apresentado através de código da tabela 5.2 "Tabela de Informações Adicionais da Apuração - Valores Declaratórios" para apresentação nos registros E115 e 1925. Conforme Resolução Sefaz 13 de 14/02/2019 - RJ. |
| 242 | VLR_DIFERIDO_ICMS | NUMBER(17,2) | Y |  | Informar o valor diferido do ICMS.  Este valor será apresentado através de código da tabela 5.2 "Tabela de Informações Adicionais da Apuração - Valores Declaratórios" para apresentação nos registros E115 e 1925. Conforme Resolução Sefaz 13 de 14/02/2019 - RJ. |
| 243 | VLR_EXC_BC_PIS | NUMBER(17,2) | Y |  |  |
| 244 | VLR_EXC_BC_COFINS | NUMBER(17,2) | Y |  |  |
| 245 | COD_CSOSN | VARCHAR2(3) | Y |  |  |
| 246 | VLR_FECP_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 247 | COD_GRUPO_CCLASS | VARCHAR2(3) | Y |  |  |
| 248 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 249 | COD_AUTENTIC_NFE_ANT | VARCHAR2(44) | Y |  |  |
| 250 | NUM_ITEM_NFE_ANT | VARCHAR2(4) | Y |  |  |
| 251 | COD_CCLASS | VARCHAR2(7) | Y |  |  |
| 252 | CNPJ_OPER_LD | VARCHAR2(14) | Y |  |  |
| 253 | DAT_EXPIRA_CRED | DATE | Y |  |  |
| 254 | IND_DEVOLUCAO | VARCHAR2(1) | Y |  |  |
| 255 | TIPO_ITEM | VARCHAR2(1) | Y |  |  |
| 256 | IDENT_PRODUTO_ACABADO | NUMBER(12) | Y |  |  |
| 257 | DAT_CRIACAO | DATE | Y |  |  |
| 258 | DAT_ALTERACAO | DATE | Y |  |  |
| 259 | IND_NF_ANT | VARCHAR2(1) | Y |  |  |
| 260 | NUM_GUIA_RECOL | VARCHAR2(16) | Y |  |  |
| 261 | DAT_EMISSAO_GUIA | DATE | Y |  |  |
| 262 | DAT_PAGTO_GUIA | DATE | Y |  |  |
| 263 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 264 | VLR_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 265 | QTD_PROD_20C | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC_BEM, VALID_BEM → X13_BEM_ATIVO(COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM)
- IDENT_ALMOX → X2021_ALMOXARIFADO(IDENT_ALMOX)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- IDENT_FEDERAL → X2044_SIT_TRIB_FED(IDENT_FEDERAL)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)
- COD_PAIS_DEST_ORIG → PAIS(COD_PAIS)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_OPER_OIL → X2015_OPERACAO_OIL(IDENT_OPER_OIL)
- IDENT_PROJETO → X2016_PROJETO(IDENT_PROJETO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- COD_TRIB_PROD → PRT_COD_TRIB_AM(COD_TRIB_PROD)
- IDENT_FIS_JUR_RET → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_CFO_DCIP → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_PROC_ADJ_PRINC → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT_PRINC → X2059_SUSP_TBT(IDENT_SUSP_TBT)
- IDENT_PROC_ADJ_ADIC → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT_ADIC → X2059_SUSP_TBT(IDENT_SUSP_TBT)

**Indexes**:
- IX_FK_SAF_2077: (IDENT_OBSERVACAO)
- IX_FK_SAF_2953: (IDENT_FIS_JUR_RET)
- IX_X08_ITENS_MERC_CTA: (IDENT_CONTA)
- IX_X08_X13: (COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC_BEM, VALID_BEM)
- IX_X08_X2013: (IDENT_PRODUTO)

---

## X08_LOG_PRODUTO

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
| 12 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 13 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

---

## X08_TRIB_MERC

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
| 12 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 13 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 14 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 15 | DIF_ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 16 | OBS_TRIBUTO | VARCHAR2(45) | Y |  |  |
| 17 | IDENT_DET_OPERACAO | NUMBER(12) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 20 | IND_CRED_TRIBUTO | CHAR(1) | Y |  |  |
| 21 | IND_FORNEC_TRIBUTO | CHAR(1) | Y |  | Indicador de Situação de ICMSS do Fornedor - 1 = Substituto, 2 = Substituído |
| 22 | IND_IPI_NDESTAC_DF | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, COD_TRIBUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_TRIBUTO → TRIBUTO(COD_TRIBUTO)
- IDENT_DET_OPERACAO → DETALHE_OPERACAO(IDENT_DET_OPERACAO)

---

## X09_BASE_SERV

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
| 11 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 14 | COD_TRIBUTACAO | NUMBER(1) | N |  |  |
| 15 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM, COD_TRIBUTO, COD_TRIBUTACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM, COD_TRIBUTO → X09_TRIB_SERV(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM, COD_TRIBUTO)
- COD_TRIBUTO, COD_TRIBUTACAO → TRIBUTACAO(COD_TRIBUTO, COD_TRIBUTACAO)

---

## X09_ITENS_SERV

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
| 11 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 14 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 15 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 17 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 20 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 21 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 22 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 23 | VLR_SERVICO_CONV | NUMBER(18,4) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 26 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 27 | DAT_OPERACAO | DATE | Y |  |  |
| 28 | USUARIO | VARCHAR2(40) | Y |  |  |
| 29 | COMPL_ISENCAO | VARCHAR2(5) | Y |  |  |
| 30 | VLR_BASE_CSLL | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ALIQ_CSLL | NUMBER(7,4) | Y |  |  |
| 32 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 34 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 35 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 36 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 37 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 38 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 39 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 40 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 35/05 |
| 41 | COD_TRIB_ISS | VARCHAR2(2) | Y |  | Ato Cotepe 70/05 - código de tributação do ISS - CTISS - view TRIBUTACAO_ISS_V |
| 42 | VLR_MAT_PROP | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do Material Próprio utilizado na prestação do serviço. |
| 43 | VLR_MAT_TERC | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do Material de Terceiros utilizado na prestação do serviço. |
| 44 | VLR_BASE_ISS_RETIDO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor da Base de Cálculo de Retenção de ISSQN. |
| 45 | VLR_ISS_RETIDO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020: Valor do ISSQN retido pelo tomador. |
| 46 | VLR_DEDUCAO_ISS | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg B020: Valor de dedução da base de cálculo do ISSQN. |
| 47 | VLR_SUBEMPR_ISS | NUMBER(17,2) | Y |  |  |
| 48 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 49 | VLR_OUT_DESP | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg A020 |
| 50 | VLR_BASE_CIDE | NUMBER(17,2) | Y |  |  |
| 51 | VLR_ALIQ_CIDE | NUMBER(7,4) | Y |  |  |
| 52 | VLR_CIDE | NUMBER(17,2) | Y |  |  |
| 53 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 54 | IND_VLR_PIS_COFINS | CHAR(1) | Y | 'N' | Indicador para verificar se os valores de PIS/COFINS estao destacados no documentos fiscal |
| 55 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 56 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 57 | VLR_PIS_EXP | NUMBER(17,2) | Y |  |  |
| 58 | VLR_PIS_TRIB | NUMBER(17,2) | Y |  |  |
| 59 | VLR_PIS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 60 | VLR_COFINS_EXP | NUMBER(17,2) | Y |  |  |
| 61 | VLR_COFINS_TRIB | NUMBER(17,2) | Y |  |  |
| 62 | VLR_COFINS_N_TRIB | NUMBER(17,2) | Y |  |  |
| 63 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 64 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 65 | DAT_LANC_PIS_COFINS | DATE | Y |  |  |
| 66 | IND_PIS_COFINS_EXTEMP | CHAR(1) | Y |  |  |
| 67 | IND_LOCAL_EXEC_SERV | CHAR(1) | Y |  |  |
| 68 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 69 | VLR_BASE_INSS | NUMBER(17,2) | Y |  |  |
| 70 | VLR_ALIQ_INSS | NUMBER(7,4) | Y |  |  |
| 71 | VLR_INSS_RETIDO | NUMBER(17,2) | Y |  |  |
| 72 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 73 | IND_NAT_BASE_CRED | VARCHAR2(2) | Y |  |  |
| 74 | VLR_ACRESCIMO | NUMBER(17,2) | Y |  |  |
| 75 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 76 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 77 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 78 | IDENT_NBS | NUMBER(12) | Y |  |  |
| 79 | VLR_TOT_ADIC | NUMBER(17,2) | Y |  |  |
| 80 | VLR_TOT_RET | NUMBER(17,2) | Y |  |  |
| 81 | VLR_DEDUCAO_NF | NUMBER(17,2) | Y |  |  |
| 82 | VLR_RET_NF | NUMBER(17,2) | Y |  |  |
| 83 | VLR_RET_SERV | NUMBER(17,2) | Y |  |  |
| 84 | VLR_ALIQ_ISS_RETIDO | NUMBER(7,4) | Y |  |  |
| 85 | COD_SIT_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 86 | VLR_N_RET_PRINC | NUMBER(17,2) | Y |  |  |
| 87 | VLR_N_RET_ADIC | NUMBER(17,2) | Y |  |  |
| 88 | VLR_DED_ALIM | NUMBER(17,2) | Y |  |  |
| 89 | VLR_DED_TRANS | NUMBER(17,2) | Y |  |  |
| 90 | IND_TP_PROC_ADJ_PRINC | CHAR(1) | Y |  |  |
| 91 | IDENT_PROC_ADJ_PRINC | NUMBER(12) | Y |  |  |
| 92 | IDENT_SUSP_TBT_PRINC | NUMBER(12) | Y |  |  |
| 93 | IND_TP_PROC_ADJ_ADIC | CHAR(1) | Y |  |  |
| 94 | IDENT_PROC_ADJ_ADIC | NUMBER(12) | Y |  |  |
| 95 | IDENT_SUSP_TBT_ADIC | NUMBER(12) | Y |  |  |
| 96 | NUM_PROC_ADJ_PREST_PRINC | VARCHAR2(21) | Y |  |  |
| 97 | NUM_PROC_ADJ_PREST_ADIC | VARCHAR2(21) | Y |  |  |
| 98 | VLR_SERV_15 | NUMBER(17,2) | Y |  |  |
| 99 | VLR_SERV_20 | NUMBER(17,2) | Y |  |  |
| 100 | VLR_SERV_25 | NUMBER(17,2) | Y |  |  |
| 101 | VLR_ABAT_NTRIBUTADO | NUMBER(17,2) | Y |  |  |
| 102 | COD_ATIV_RJ | NUMBER(7) | Y |  |  |
| 103 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 104 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 105 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 106 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 107 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 108 | DAT_CRIACAO | DATE | Y |  |  |
| 109 | DAT_ALTERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_NBS → X2055_COD_NBS(IDENT_NBS)
- IDENT_PROC_ADJ_PRINC → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_PROC_ADJ_ADIC → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT_PRINC → X2059_SUSP_TBT(IDENT_SUSP_TBT)
- IDENT_SUSP_TBT_ADIC → X2059_SUSP_TBT(IDENT_SUSP_TBT)

**Indexes**:
- IX_FK_SAF_2078: (IDENT_OBSERVACAO)

---

## X09_TRIB_SERV

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
| 11 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | COD_TRIBUTO | VARCHAR2(6) | N |  |  |
| 14 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 15 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 16 | DIF_ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 17 | OBS_TRIBUTO | VARCHAR2(45) | Y |  |  |
| 18 | IDENT_DET_OPERACAO | NUMBER(12) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM, COD_TRIBUTO

**FKs**:
- COD_TRIBUTO → TRIBUTO(COD_TRIBUTO)
- IDENT_DET_OPERACAO → DETALHE_OPERACAO(IDENT_DET_OPERACAO)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM → X09_ITENS_SERV(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM)

---

## X100_PARAM_REG75MM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 3 | IND_PRODUTO | CHAR(1) | N |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 5 | DAT_VIGENCIA_INI | DATE | N |  |  |
| 6 | DAT_VIGENCIA_FIM | DATE | Y |  |  |
| 7 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 8 | PERC_BASE_RED_ICMS | NUMBER(7,4) | Y |  |  |
| 9 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_ESTADO, GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, DAT_VIGENCIA_INI

---

## X101_CONTABIL_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_LANCTO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | IDENT_CONTRA_PART | NUMBER(12) | Y |  |  |
| 8 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 9 | IDENT_DESPESA | NUMBER(12) | Y |  |  |
| 10 | IDENT_HISTPADRAO | NUMBER(12) | Y |  |  |
| 11 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 12 | TXT_HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 13 | VLR_LANCTO | NUMBER(19,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 16 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 17 | TIPO_LANCTO | CHAR(1) | Y |  | N - Normal; E - Encerramento |
| 18 | IDENT_PFJ_EMPRESA | NUMBER(12) | Y |  |  |
| 19 | DATA_PFJ_EMPRESA | DATE | Y |  |  |
| 20 | DAT_LANCTO_EXTEMP | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO

**FKs**:
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_DESPESA → X2004_CENTRO_DESP(IDENT_DESPESA)
- IDENT_HISTPADRAO → X2020_HIST_PADRAO(IDENT_HISTPADRAO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTRA_PART → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- COD_EMPRESA, IDENT_PFJ_EMPRESA, DATA_PFJ_EMPRESA → X39_PFJ_EMPRESA(COD_EMPRESA, IDENT_FIS_JUR, DATA_VALID_INI)

**Indexes**:
- IX_X101_CONTABIL_AUX_CTA: (IDENT_CONTRA_PART)
- IX_X101_CONTAB_AUX_CTA: (IDENT_CONTA)
- IX_X101_EMPR_DAT: (COD_EMPRESA, DATA_LANCTO, IDENT_CONTA)

---

## X102_SALDOS_AUX

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | NUMBER(19,2) | Y |  |  |
| 8 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 9 | VLR_TOT_CRE | NUMBER(19,2) | Y |  |  |
| 10 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X102_SALDOS_AUX: (COD_EMPRESA, COD_ESTAB, DATA_SALDO)
- IX_X102_SALDOS_AUX_CTA: (IDENT_CONTA)

---

## X103_REMESSA_EXP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_RE | VARCHAR2(15) | N |  |  |
| 4 | DAT_FISCAL | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 10 | DAT_EMISSAO | DATE | Y |  |  |
| 11 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 12 | QTD_EXPORTADA | NUMBER(17,3) | Y |  |  |
| 13 | VLR_UNIT_PRODUTO | NUMBER(21,6) | Y |  |  |
| 14 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 15 | COD_RELAC | CHAR(1) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | IND_PROD_N_INDUSTR | CHAR(1) | Y |  |  |
| 19 | NUM_MEMO_EXP | VARCHAR2(50) | N |  |  |
| 20 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 21 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 22 | IND_MOVTO | CHAR(1) | Y |  |  |
| 23 | IND_COMPROV_OPER | CHAR(1) | Y |  |  |
| 24 | DAT_FISCAL_EXP | DATE | Y |  |  |
| 25 | NUM_DOCFIS_EXP | VARCHAR2(12) | Y |  |  |
| 26 | SERIE_DOCFIS_EXP | VARCHAR2(3) | Y |  |  |
| 27 | NUM_DDE_EXP | VARCHAR2(14) | Y |  |  |
| 28 | COD_TP_LANCTO | NUMBER(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_RE, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, NUM_MEMO_EXP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- IX_FK_SAF_2008: (IDENT_FIS_JUR)
- IX_X103_REMESSA_EXP: (NUM_RE)

---

## X105_MOV_FINANC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MES_CONSIDERA | NUMBER(2) | N |  |  |
| 4 | ANO_CONSIDERA | NUMBER(4) | N |  |  |
| 5 | DAT_REF_INI | DATE | Y |  |  |
| 6 | DAT_REF_FIM | DATE | Y |  |  |
| 7 | RECEITAS_SERV | NUMBER(17,2) | Y |  |  |
| 8 | EMPRESTIMOS_BANCARIOS | NUMBER(17,2) | Y |  |  |
| 9 | AUMENTO_CAPITAL_DINHEIRO | NUMBER(17,2) | Y |  |  |
| 10 | RECEITAS_FINANCEIRAS | NUMBER(17,2) | Y |  |  |
| 11 | OUTROS_INGRESSOS_RECURSO | NUMBER(17,2) | Y |  |  |
| 12 | PRO_LABORE | NUMBER(17,2) | Y |  |  |
| 13 | COMISSOES_SALARIOS_ORDENADOS | NUMBER(17,2) | Y |  |  |
| 14 | ENCARGOS_SOCIAIS | NUMBER(17,2) | Y |  |  |
| 15 | HONORARIOS_CONTABEIS | NUMBER(17,2) | Y |  |  |
| 16 | COMBUSTIVEIS_LUBRIFICANTES | NUMBER(17,2) | Y |  |  |
| 17 | TRIBUTOS_FEDERAIS | NUMBER(17,2) | Y |  |  |
| 18 | TRIBUTOS_ESTADUAIS | NUMBER(17,2) | Y |  |  |
| 19 | TRIBUTOS_MUNICIPAIS | NUMBER(17,2) | Y |  |  |
| 20 | AGUA_TELEFONE | NUMBER(17,2) | Y |  |  |
| 21 | ENERGIA | NUMBER(17,2) | Y |  |  |
| 22 | ALUGUEL_CONDOMINIO | NUMBER(17,2) | Y |  |  |
| 23 | SERVICOS_PROFISSIONAIS | NUMBER(17,2) | Y |  |  |
| 24 | SEGUROS | NUMBER(17,2) | Y |  |  |
| 25 | PAGAMENTO_EMPRESTIMOS | NUMBER(17,2) | Y |  |  |
| 26 | DESPESAS_BANCARIAS | NUMBER(17,2) | Y |  |  |
| 27 | OUTRAS_DESPESAS_PAGAMENTOS | NUMBER(17,2) | Y |  |  |
| 28 | SALDO_CAIXA_INI | NUMBER(17,2) | Y |  |  |
| 29 | SALDO_CAIXA_FIM | NUMBER(17,2) | Y |  |  |
| 30 | SALDO_BANCO_INI | NUMBER(17,2) | Y |  |  |
| 31 | SALDO_BANCO_FIM | NUMBER(17,2) | Y |  |  |
| 32 | FORNEC_A_PAGAR_INI | NUMBER(17,2) | Y |  |  |
| 33 | FORNEC_A_PAGAR_FIM | NUMBER(17,2) | Y |  |  |
| 34 | DUPLIC_A_RECEBER_INI | NUMBER(17,2) | Y |  |  |
| 35 | DUPLIC_A_RECEBER_FIM | NUMBER(17,2) | Y |  |  |
| 36 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 37 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MES_CONSIDERA, ANO_CONSIDERA

---

## X106_MOVTO_AIDF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_ENTREGA | DATE | N |  |  |
| 4 | NRO_AIDF | VARCHAR2(60) | N |  |  |
| 5 | COD_SITUACAO | VARCHAR2(2) | N |  |  |
| 6 | DAT_MOVTO | DATE | N |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 9 | COD_TP_DISP_SEG | VARCHAR2(2) | N |  |  |
| 10 | NUM_DOCFIS_INI | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | NUM_CTR_DISP_INI | VARCHAR2(12) | N |  |  |
| 14 | NUM_DOCFIS_FIM | VARCHAR2(12) | Y |  |  |
| 15 | NUM_CTR_DISP_FIM | VARCHAR2(12) | Y |  |  |
| 16 | COD_OPERACAO | VARCHAR2(2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 19 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 20 | DAT_AIDF | DATE | Y |  |  |
| 21 | IDENT_ESTADO_AIDF | NUMBER(12) | Y |  |  |
| 22 | COD_MUNICIPIO_AIDF | NUMBER(5) | Y |  |  |
| 23 | IDENT_MODELO_GRAF | NUMBER | Y |  |  |
| 24 | NUM_DOCFIS_GRAF | VARCHAR2(12) | Y |  |  |
| 25 | SERIE_DOCFIS_GRAF | VARCHAR2(3) | Y |  |  |
| 26 | SUBSERIE_DOCFIS_GRAF | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ENTREGA, NRO_AIDF, COD_SITUACAO, DAT_MOVTO, IDENT_DOCTO, IDENT_MODELO, COD_TP_DISP_SEG, NUM_DOCFIS_INI, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_CTR_DISP_INI

**FKs**:
- IDENT_ESTADO_AIDF, COD_MUNICIPIO_AIDF → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## X107_TELECOM_SIMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUMERO | VARCHAR2(20) | N |  |  |
| 4 | DT_DISPONIB | DATE | N |  |  |
| 5 | HR_DISPONIB | NUMBER(6) | Y |  |  |
| 6 | TEL_ACESSO | VARCHAR2(15) | Y |  |  |
| 7 | NUM_LOTE_PIN | VARCHAR2(20) | Y |  |  |
| 8 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 10 | DATA_DOCFIS_REF | DATE | Y |  |  |
| 11 | VLR_ATIVACAO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUMERO, DT_DISPONIB

---

## X108_CAPA_OP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | N |  |  |
| 4 | COD_OP | VARCHAR2(30) | N |  |  |
| 5 | COD_DIF_PRODUCAO | VARCHAR2(15) | N |  |  |
| 6 | IDENT_PRODUTO_OP | NUMBER(12) | N |  |  |
| 7 | DT_INI_OP | DATE | Y |  |  |
| 8 | DT_FIM_OP | DATE | Y |  |  |
| 9 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 10 | QTD_PRODUZIDO | NUMBER(17,6) | Y |  |  |
| 11 | IND_APUR_CUSTO | CHAR(1) | Y | 'N' |  |
| 12 | VLR_TOT_CUSTO | NUMBER(17,2) | Y |  |  |
| 13 | QTD_TRANSF | NUMBER(17,6) | Y |  |  |
| 14 | VLR_TRANSF | NUMBER(17,2) | Y |  |  |
| 15 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 16 | VLR_ICMS_DCA | NUMBER(21,6) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 19 | COD_PROCESSO_PRODUCAO | VARCHAR2(10) | Y |  |  |
| 20 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |
| 21 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 22 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 26 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 27 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 28 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 29 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 30 | IND_TP_ORDEM | CHAR(1) | Y |  |  |
| 31 | QTD_ORIGEM | NUMBER(17,6) | Y |  |  |
| 32 | DT_SAIDA_ESTQ | DATE | Y |  |  |
| 33 | QTD_SAIDA_ESTQ | NUMBER(17,6) | Y |  |  |
| 34 | DT_RET_ESTQ | DATE | Y |  |  |
| 35 | QTD_RET_ESTQ | NUMBER(17,6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REF, COD_OP, COD_DIF_PRODUCAO, IDENT_PRODUTO_OP

---

## X109_ITEM_OP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | N |  |  |
| 4 | COD_OP | VARCHAR2(30) | N |  |  |
| 5 | COD_DIF_PRODUCAO | VARCHAR2(15) | N |  |  |
| 6 | IDENT_PRODUTO_OP | NUMBER(12) | N |  |  |
| 7 | NUM_ITEM | NUMBER(5) | N |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 9 | DT_SAIDA | DATE | Y |  |  |
| 10 | IDENT_UND_PADRAO | NUMBER(12) | N |  |  |
| 11 | QTD_PRODUZIDO | NUMBER(17,6) | Y |  |  |
| 12 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 14 | VLR_ICMS_DCA | NUMBER(21,6) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 18 | DAT_VALID_INI | DATE | Y |  |  |
| 19 | IDENT_INSUMO_SUBST | NUMBER(12) | Y |  |  |
| 20 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |
| 21 | DSC_RESERVADO1 | VARCHAR2(50) | Y |  |  |
| 22 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 26 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 27 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 28 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 29 | QTD_DESTINO | NUMBER(17,6) | Y |  |  |
| 30 | QTD_REPROC | NUMBER(17,6) | Y |  |  |
| 31 | QTD_RETORNADA | NUMBER(17,6) | Y |  |  |
| 32 | V_PERIODO_REFDT | DATE | Y | TO_DATE('01'\|\|"PERIODO_REF",'ddmmyyyy') |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REF, COD_OP, COD_DIF_PRODUCAO, IDENT_PRODUTO_OP, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI → DWT_FASE_PRODUCAO(COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI)
- IDENT_INSUMO_SUBST → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_109_ITEM_OP_01: (COD_EMPRESA, COD_ESTAB, PERIODO_REF)
- IX_109_ITEM_OP_02V: (COD_EMPRESA, COD_ESTAB, V_PERIODO_REFDT)

---

## X10_ESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NORM_DEV | CHAR(1) | N |  |  |
| 5 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | DATA_MOVTO | DATE | N |  |  |
| 8 | NUM_DOCTO | VARCHAR2(15) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | DISCRI_ESTOQUE | VARCHAR2(52) | N |  |  |
| 13 | NUM_ITEM | NUMBER(5) | N |  |  |
| 14 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 15 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 16 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 17 | IDENT_NAT_ESTOQUE | NUMBER(12) | Y |  |  |
| 18 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 19 | SERIE_ITEM | VARCHAR2(15) | Y |  |  |
| 20 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 21 | PRECO_UNIT | NUMBER(18,6) | Y |  |  |
| 22 | PRECO_ITEM | NUMBER(17,2) | Y |  |  |
| 23 | CUSTO_UNIT | NUMBER(18,6) | Y |  |  |
| 24 | CUSTO_ITEM | NUMBER(17,2) | Y |  |  |
| 25 | IDENT_CONTA_CRED | NUMBER(12) | Y |  |  |
| 26 | IDENT_CONTA_DEBITO | NUMBER(12) | Y |  |  |
| 27 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 28 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 29 | COD_ENT_SAIDA | CHAR(1) | Y |  |  |
| 30 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 31 | DATA_ESCRITA_FIS | DATE | Y |  |  |
| 32 | OBS_ESTOQUE | VARCHAR2(45) | Y |  |  |
| 33 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 34 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 35 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 36 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 37 | IND_INSUMO | CHAR(1) | Y |  |  |
| 38 | IDENT_LEGENDA | NUMBER(12) | Y |  |  |
| 39 | NUM_ORDEM | VARCHAR2(30) | Y |  |  |
| 40 | NUM_DOCFIS_OFIC | VARCHAR2(12) | Y |  |  |
| 41 | SERIE_DOCFIS_OFIC | VARCHAR2(3) | Y |  |  |
| 42 | S_SERIE_DOCFIS_OFIC | VARCHAR2(2) | Y |  |  |
| 43 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 44 | IND_TP_MOVTO | CHAR(1) | Y |  |  |
| 45 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 46 | IDENT_PROD_RASTRO | NUMBER(12) | Y |  |  |
| 47 | NUM_LIVRO | NUMBER(6) | Y |  |  |
| 48 | NUM_FOLHA | NUMBER(6) | Y |  |  |
| 49 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 50 | DATA_DISP | DATE | Y |  | ATO COTEPE 70 - reg H200: Data de disponibilidade para uso na produção. |
| 51 | IND_DOC_OPER | CHAR(1) | Y |  | ATO COTEPE 70 - rerg H200: Indicador do tipo de documento da movimentação: F - Documento Fiscal ; I - Documento Interno. |
| 52 | IND_TP_DOC_INTERNO | VARCHAR2(30) | Y |  | ATO COTEPE 70 - rerg H200: Tipo de Documento Interno. |
| 53 | IND_REDESIGNACAO | CHAR(1) | Y |  | Indicador de Redesignação ATO COTEPE - REG H220 |
| 54 | IDENT_PRODUTO_ORI | NUMBER(12) | Y |  |  |
| 55 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 56 | VLR_OUT_TRIB_NCUMUL | NUMBER(17,2) | Y |  |  |
| 57 | COD_TP_LANCTO | NUMBER(6) | Y |  |  |
| 58 | VLR_ICMS_DCA | NUMBER(21,6) | Y |  |  |
| 59 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 60 | DSC_FINALIDADE | VARCHAR2(255) | Y |  |  |
| 61 | COD_TIPO_MOV_EST | VARCHAR2(2) | Y |  |  |
| 62 | IDENT_MEDIDA_ORI | NUMBER(12) | Y |  |  |
| 63 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |
| 64 | COD_NIVEL_PRODUTO | NUMBER(3) | Y |  |  |
| 65 | QTD_INSUMO | NUMBER(17,6) | Y |  |  |
| 66 | IND_CF | CHAR(1) | Y |  |  |
| 67 | TP_AVALIACAO | VARCHAR2(10) | Y |  |  |
| 68 | VLR_RESERVADO1 | NUMBER(17,6) | Y |  |  |
| 69 | DSC_RESERVADO2 | VARCHAR2(50) | Y |  |  |
| 70 | DSC_RESERVADO3 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DATA_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM

**FKs**:
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- IDENT_ALMOX → X2021_ALMOXARIFADO(IDENT_ALMOX)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_NAT_ESTOQUE → X2010_NAT_ESTOQUE(IDENT_NAT_ESTOQUE)
- IDENT_CONTA_CRED → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTA_DEBITO → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_PROD_RASTRO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA_ORI → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- IND_SAF_0001: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IND_TP_MOVTO)
- IND_SAF_0002: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, NUM_ORDEM, IND_INSUMO)
- IND_SAF_0003: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, NUM_DOCTO, IND_INSUMO)
- IX_X10_ESTOQUE: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_PRODUTO)
- IX_X10_ESTOQUE1: (IDENT_PRODUTO)
- IX_X10_ESTOQUE2: (IDENT_FIS_JUR)
- IX_X10_ESTOQUE_CTA: (IDENT_CONTA_CRED)
- IX_X10_ESTOQUE_CTA_DEB: (IDENT_CONTA_DEBITO)
- IX_X10_NUM_ORDEM: (NUM_ORDEM, COD_DIF_PRODUCAO, COD_ESTAB, COD_EMPRESA)

---

## X10_LOG_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NORM_DEV | CHAR(1) | N |  |  |
| 5 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | DATA_MOVTO | DATE | N |  |  |
| 8 | NUM_DOCTO | VARCHAR2(15) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | DISCRI_ESTOQUE | VARCHAR2(52) | N |  |  |
| 13 | NUM_ITEM | NUMBER(5) | N |  |  |
| 14 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 15 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DATA_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM

---

## X110_ITEM_ROMANEIO

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
| 12 | IDENT_PRODUTO_DOCFIS | NUMBER(12) | Y |  |  |
| 13 | NUM_ROMANEIO | VARCHAR2(12) | N |  |  |
| 14 | NUM_ITEM_ROMANEIO | NUMBER(5) | N |  |  |
| 15 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 16 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 17 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 18 | PRECO_UNITARIO | NUMBER(17,2) | Y |  |  |
| 19 | PRECO_TOTAL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_ROMANEIO, NUM_ITEM_ROMANEIO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)

---

## X112_OBS_DOCFIS

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 16 | VINCULACAO | CHAR(1) | Y |  |  |
| 17 | DSC_INFO_FISCO | VARCHAR2(2000) | Y |  |  |
| 18 | DSC_INFO_CONTRIB | VARCHAR2(3000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO: (IDENT_OBSERVACAO)

---

## X113_AJUSTE_APUR

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 16 | DSC_COMP_AJUSTE | VARCHAR2(255) | Y |  |  |
| 17 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | ALIQUOTA_ICMS | NUMBER(7,4) | Y |  |  |
| 19 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_AJUSTE_SPED, DISCRI_ITEM

**FKs**:
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X112_OBS_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR_X113: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_X113: (IDENT_OBSERVACAO)

---

## X113_AJUSTE_APUR_DEB_ESP

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 14 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 15 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 16 | DSC_COMP_AJUSTE | VARCHAR2(255) | Y |  |  |
| 17 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | ALIQUOTA_ICMS | NUMBER(7,4) | Y |  |  |
| 19 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_AJUSTE_SPED, DISCRI_ITEM

---

## X114_PROC_REF

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | NUM_PROCESSO | VARCHAR2(60) | N |  |  |
| 14 | ORIG_PROCESSO | CHAR(1) | N |  |  |
| 15 | IDENT_PROC_REF | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, NUM_PROCESSO, ORIG_PROCESSO

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X112_OBS_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR_X114: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_X114: (IDENT_OBSERVACAO)

---

## X114_PROC_REF_ITEM

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | NUM_PROCESSO | VARCHAR2(24) | N |  |  |
| 14 | ORIG_PROCESSO | CHAR(1) | N |  |  |
| 15 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 16 | IDENT_PROC_REF | NUMBER(12) | Y |  |  |
| 17 | NUM_ITEM | NUMBER(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, NUM_PROCESSO, ORIG_PROCESSO, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X112_OBS_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)

**Indexes**:
- IX_X114_PROC_REF_ITEM_01: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

---

## X115_DOC_ARRCD_REF

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | IND_TP_DOC_ARREC | CHAR(1) | N |  |  |
| 14 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 15 | NUM_DOC_ARREC | VARCHAR2(50) | N |  |  |
| 16 | COD_AUTEN_BANC | VARCHAR2(100) | N |  |  |
| 17 | DATA_VENC_DOC_ARREC | DATE | N |  |  |
| 18 | VLR_TOT_DOC_ARREC | NUMBER(17,2) | N |  |  |
| 19 | DATA_PGTO_DOC_ARREC | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, IND_TP_DOC_ARREC, IDENT_ESTADO, NUM_DOC_ARREC, COD_AUTEN_BANC, DATA_VENC_DOC_ARREC

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X112_OBS_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR_X115: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_X115: (IDENT_OBSERVACAO)

---

## X116_DOCFIS_REF

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | DATA_FISCAL_REF | DATE | N |  |  |
| 14 | MOVTO_E_S_REF | CHAR(1) | N |  |  |
| 15 | IDENT_FIS_JUR_REF | NUMBER(12) | N |  |  |
| 16 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 17 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 18 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | N |  |  |
| 19 | IDENT_MODELO_REF | NUMBER(12) | N |  |  |
| 20 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, DATA_FISCAL_REF, MOVTO_E_S_REF, IDENT_FIS_JUR_REF, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF

**FKs**:
- IDENT_FIS_JUR_REF → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X112_OBS_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_MODELO_REF → X2024_MODELO_DOCTO(IDENT_MODELO)

**Indexes**:
- IX_FK_SAF_2691: (IDENT_FIS_JUR_REF)
- IX_FK_X04_PESSOA_FIS_JUR_X116: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_X116: (IDENT_OBSERVACAO)

---

## X117_CUPOM_REF

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | COD_EQUIPAMENTO | VARCHAR2(9) | N |  |  |
| 14 | NUM_DOC | VARCHAR2(12) | N |  |  |
| 15 | DATA_EMISSAO | DATE | N |  |  |
| 16 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 17 | COD_FABRICACAO_ECF | VARCHAR2(21) | Y |  |  |
| 18 | NUM_CHAVE_CFE | VARCHAR2(80) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_EQUIPAMENTO, NUM_DOC, DATA_EMISSAO

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X112_OBS_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR_X117: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_X117: (IDENT_OBSERVACAO)

---

## X118_COLETA_ENTRG

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | NUM_SEQ | NUMBER(3) | N |  |  |
| 14 | IDENT_VIA_TRANSP | NUMBER(12) | N |  |  |
| 15 | IDENT_UF_COLETA | NUMBER(12) | Y |  |  |
| 16 | COD_MUNIC_COLETA | NUMBER(12) | Y |  |  |
| 17 | CNPJ_COLETA | VARCHAR2(14) | Y |  |  |
| 18 | IE_COLETA | VARCHAR2(14) | Y |  |  |
| 19 | IDENT_UF_ENTREGA | NUMBER(12) | Y |  |  |
| 20 | COD_MUNIC_ENTREGA | NUMBER(12) | Y |  |  |
| 21 | CNPJ_ENTREGA | VARCHAR2(14) | Y |  |  |
| 22 | IE_ENTREGA | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, NUM_SEQ, IDENT_VIA_TRANSP

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X112_OBS_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR_X118: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_X118: (IDENT_OBSERVACAO)
- IX_X118_COLETA_ENTRG (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, IDENT_VIA_TRANSP, IDENT_UF_COLETA, COD_MUNIC_COLETA, IDENT_UF_ENTREGA, COD_MUNIC_ENTREGA)

---

## X119_ITENS_MEDICAMENTO

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
| 12 | NUM_FAB_LOTE | VARCHAR2(50) | N |  |  |
| 13 | QTD_LOTE | NUMBER(17,6) | Y |  |  |
| 14 | DAT_FABRIC | DATE | Y |  |  |
| 15 | DAT_VALIDADE | DATE | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_FAB_LOTE

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

---

## X11_MOVTO_BEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | IDENT_TIPO_MOVPATR | NUMBER(12) | N |  |  |
| 5 | DATA_MOVTO | DATE | N |  |  |
| 6 | COD_BEM | VARCHAR2(60) | N |  |  |
| 7 | COD_INC | VARCHAR2(6) | N |  |  |
| 8 | VALID_BEM | DATE | N |  |  |
| 9 | VLR_MOVTO | NUMBER(17,2) | Y |  |  |
| 10 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 11 | VLR_EM_INDICE | NUMBER(18,4) | Y |  |  |
| 12 | BASE_CM | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, IDENT_TIPO_MOVPATR, DATA_MOVTO, COD_BEM, COD_INC, VALID_BEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM → X13_BEM_ATIVO(COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_TIPO_MOVPATR → X2022_TIPO_MOVPATR(IDENT_TIPO_MOVPATR)
- COD_INDICE → Y2046_INDICE(COD_INDICE)

**Indexes**:
- IX_X11_MOVTO_B_01: (IDENT_CONTA)
- IX_X11_X13: (COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM)

---

## X120_ITENS_ARMA

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
| 12 | NUM_SERIE_FABRIC | VARCHAR2(50) | N |  |  |
| 13 | DSC_COMPLEM | VARCHAR2(150) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_SERIE_FABRIC

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

---

## X121_LACRE_BOMBA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_BOMBA | NUMBER(10) | N |  |  |
| 4 | DAT_LACRE | DATE | N |  |  |
| 5 | NUM_LACRE | VARCHAR2(20) | N |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_BOMBA, DAT_LACRE, NUM_LACRE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X122_TANQUE_BICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_TANQUE | NUMBER(10) | N |  |  |
| 4 | NUM_BOMBA | NUMBER(10) | N |  |  |
| 5 | NUM_BICO | NUMBER(10) | N |  |  |
| 6 | DAT_MOVTO | DATE | N |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_TANQUE, NUM_BOMBA, NUM_BICO, DAT_MOVTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X123_MOV_TANQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_MOVTO | DATE | N |  |  |
| 4 | IDENT_TANQUE | NUMBER(12) | N |  |  |
| 5 | QTD_ESTOQ_INI | NUMBER(17,6) | N |  |  |
| 6 | QTD_ENTRADA | NUMBER(17,6) | Y |  |  |
| 7 | QTD_SAIDA | NUMBER(17,6) | Y |  |  |
| 8 | QTD_PERDA | NUMBER(17,6) | Y |  |  |
| 9 | QTD_GANHO | NUMBER(17,6) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_MOVTO, IDENT_TANQUE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_TANQUE → X2060_TANQUE(IDENT_TANQUE)

---

## X124_VENDA_DIARIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_MOVTO | DATE | N |  |  |
| 4 | IDENT_BICO | NUMBER(12) | N |  |  |
| 5 | NUM_SEQ | NUMBER(2) | N |  |  |
| 6 | NUM_INTERV | NUMBER(12) | Y |  |  |
| 7 | MOT_INTERV | VARCHAR2(255) | Y |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 9 | CPF_RESP | VARCHAR2(11) | Y |  |  |
| 10 | QTD_CONT_INI | NUMBER(17,6) | N |  |  |
| 11 | QTD_CONT_FINAL | NUMBER(17,6) | N |  |  |
| 12 | QTD_AFERICAO | NUMBER(17,6) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | NOM_RESP | VARCHAR2(50) | Y |  |  |
| 16 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_MOVTO, IDENT_BICO, NUM_SEQ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_BICO → X2062_BICO(IDENT_BICO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_2228: (IDENT_FIS_JUR)

---

## X125_NFE_ARMAZ_COMB

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
| 12 | IDENT_TANQUE | NUMBER(12) | N |  |  |
| 13 | QTD_COMB | NUMBER(17,6) | N |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, IDENT_TANQUE

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- IDENT_TANQUE → X2060_TANQUE(IDENT_TANQUE)

---

## X126_VENDA_CARTAO_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 7 | USUARIO | VARCHAR2(40) | Y |  |  |
| 8 | DAT_OPERACAO | DATE | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 11 | VLR_FAT_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_EST_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_FAT_ISS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_EST_ISS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_2234: (IDENT_FIS_JUR)

---

## X127_ING_ATIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 2 | COD_ING_ATIVO | VARCHAR2(35) | N |  |  |
| 3 | DSC_ING_ATIVO | VARCHAR2(100) | Y |  |  |

**PK**: TIPO_OBRIGACAO, COD_ING_ATIVO

---

## X129_INCL_CONTABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_LANCTO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | IDENT_CONTRA_PART | NUMBER(12) | Y |  |  |
| 8 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 9 | IDENT_DESPESA | NUMBER(12) | Y |  |  |
| 10 | IDENT_HISTPADRAO | NUMBER(12) | Y |  |  |
| 11 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 12 | TXT_HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 13 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 14 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 15 | VLR_LANCTO_CONV | NUMBER(18,4) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 19 | TIPO_LANCTO | VARCHAR2(2) | Y |  | N - Normal/Expurgo; F - Fiscal; TR - Transferencia de Saldos; TF - Transferencia de Saldos Fiscais;   TS- Transferencia de Saldos Societarios;  EF - Encerramento Fiscal; IF - Inicializacao de Saldo Fiscal e   IS - Inicializacao de Saldo Societario |
| 20 | IDENT_PFJ_EMPRESA | NUMBER(12) | Y |  |  |
| 21 | DATA_PFJ_EMPRESA | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTRA_PART → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_DESPESA → X2004_CENTRO_DESP(IDENT_DESPESA)
- IDENT_HISTPADRAO → X2020_HIST_PADRAO(IDENT_HISTPADRAO)
- COD_EMPRESA, IDENT_PFJ_EMPRESA, DATA_PFJ_EMPRESA → X39_PFJ_EMPRESA(COD_EMPRESA, IDENT_FIS_JUR, DATA_VALID_INI)
- COD_INDICE → Y2046_INDICE(COD_INDICE)

**Indexes**:
- IX_X129_EMPR_DAT: (COD_EMPRESA, DATA_LANCTO, IDENT_CONTA)
- IX_X129_INCL_CONTABIL_CTA: (IDENT_CONTA)
- IX_X129_INCL_CONTAB_CTA_PART: (IDENT_CONTRA_PART)

---

## X12_SUSP_BEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_BEM | VARCHAR2(60) | N |  |  |
| 4 | COD_INC | VARCHAR2(6) | N |  |  |
| 5 | VALID_BEM | DATE | N |  |  |
| 6 | DATA_SUSPENSAO | DATE | N |  |  |
| 7 | DATA_RETORNO | DATE | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM, DATA_SUSPENSAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM → X13_BEM_ATIVO(COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM)

---

## X130_NFE_DENEGADA_INUTILIZADA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NUM_DOCFIS_INI | VARCHAR2(12) | N |  |  |
| 5 | NUM_DOCFIS_FIN | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DATA_REF | DATE | N |  |  |
| 9 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 10 | IND_SITUACAO | CHAR(1) | N |  |  |
| 11 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 15 | IDENT_SCP | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NUM_DOCFIS_INI, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_REF, IDENT_MODELO, IND_SITUACAO

**FKs**:
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

---

## X131_RATEIO_CUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | COD_TP_LANCTO | NUMBER(6) | N |  |  |
| 8 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 10 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 11 | DESC_HISTORICO | VARCHAR2(50) | Y |  |  |
| 12 | QTD_PRODUTO | NUMBER(17,6) | Y |  |  |
| 13 | VLR_PERC_RATEIO | NUMBER(7,4) | Y |  |  |
| 14 | VLR_ICMS | NUMBER(21,6) | Y |  |  |
| 15 | VLR_OUT_CONTRIB | NUMBER(17,2) | Y |  |  |
| 16 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 19 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, NUM_DOCFIS, SERIE_DOCFIS, IDENT_PRODUTO, COD_TP_LANCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X132_CUSTO_PROD_CONJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 5 | VLR_ICMS | NUMBER(21,6) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | COD_PROCESSO_PRODUCAO | VARCHAR2(10) | N |  |  |
| 9 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, COD_PROCESSO_PRODUCAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X133_SALDO_INI_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI_APUR | DATE | N |  |  |
| 4 | DAT_FIN_APUR | DATE | N |  |  |
| 5 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 6 | VLR_SOM_PARC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TRIB_EXP | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 9 | IND_PER_SAI | NUMBER(11,8) | Y |  |  |
| 10 | VLR_ICMS_APROP | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SOM_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X134_MOV_BEM_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI_APUR | DATE | N |  |  |
| 4 | DAT_FIN_APUR | DATE | N |  |  |
| 5 | COD_BEM | VARCHAR2(60) | N |  |  |
| 6 | COD_INC | VARCHAR2(6) | N |  |  |
| 7 | DAT_MOV | DATE | N |  |  |
| 8 | COD_TIPO_MOV | VARCHAR2(2) | N |  |  |
| 9 | VLR_ICMS_OP | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_DIF | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PARCELA | NUMBER(3) | Y |  |  |
| 14 | VLR_PARC_PASS | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR, COD_BEM, COD_INC, DAT_MOV, COD_TIPO_MOV

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR → X133_SALDO_INI_CIAP(COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR)

---

## X135_DOC_FIS_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI_APUR | DATE | N |  |  |
| 4 | DAT_FIN_APUR | DATE | N |  |  |
| 5 | COD_BEM | VARCHAR2(60) | N |  |  |
| 6 | COD_INC | VARCHAR2(6) | N |  |  |
| 7 | DAT_MOV | DATE | N |  |  |
| 8 | COD_TIPO_MOV | VARCHAR2(2) | N |  |  |
| 9 | IND_EMIT | CHAR(1) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 13 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 14 | DAT_DOC | DATE | N |  |  |
| 15 | NUM_CHAVE_NFE | VARCHAR2(44) | Y |  |  |
| 16 | NUM_ITEM | NUMBER(5) | N |  |  |
| 17 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 20 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 21 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 22 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 23 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMS_DIFAL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR, COD_BEM, COD_INC, DAT_MOV, COD_TIPO_MOV, IND_EMIT, IDENT_FIS_JUR, IDENT_MODELO, NUM_DOCFIS, SERIE_DOCFIS, DAT_DOC, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR, COD_BEM, COD_INC, DAT_MOV, COD_TIPO_MOV → X134_MOV_BEM_CIAP(COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR, COD_BEM, COD_INC, DAT_MOV, COD_TIPO_MOV)

---

## X136_OUT_CRED_CIAP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_INI_APUR | DATE | N |  |  |
| 4 | DAT_FIN_APUR | DATE | N |  |  |
| 5 | COD_BEM | VARCHAR2(60) | N |  |  |
| 6 | COD_INC | VARCHAR2(6) | N |  |  |
| 7 | DAT_MOV | DATE | N |  |  |
| 8 | COD_TIPO_MOV | VARCHAR2(2) | N |  |  |
| 9 | DAT_INI_PARC | DATE | N |  |  |
| 10 | DAT_FIN_PARC | DATE | N |  |  |
| 11 | NUM_PARCELA | NUMBER(3) | N |  |  |
| 12 | VLR_PARC_PASS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TRIB_OC | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 15 | IND_PER_SAI | NUMBER(11,8) | Y |  |  |
| 16 | VLR_PARC_APROP | NUMBER(17,2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR, COD_BEM, COD_INC, DAT_MOV, COD_TIPO_MOV, DAT_INI_PARC, DAT_FIN_PARC, NUM_PARCELA

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR, COD_BEM, COD_INC, DAT_MOV, COD_TIPO_MOV → X134_MOV_BEM_CIAP(COD_EMPRESA, COD_ESTAB, DAT_INI_APUR, DAT_FIN_APUR, COD_BEM, COD_INC, DAT_MOV, COD_TIPO_MOV)

---

## X137_PERDAS_SOBRAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NORM_DEV | CHAR(1) | N |  |  |
| 5 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | DATA_MOVTO | DATE | N |  |  |
| 8 | NUM_DOCTO | VARCHAR2(15) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | DISCRI_ESTOQUE | VARCHAR2(52) | N |  |  |
| 13 | NUM_ITEM | NUMBER(5) | N |  |  |
| 14 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 15 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 16 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 17 | IDENT_PRODUTO_PERDA | NUMBER(12) | N |  |  |
| 18 | QTD_RESULT_PERDA | NUMBER(17,6) | Y |  |  |
| 19 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DATA_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM, IDENT_PRODUTO_PERDA

**FKs**:
- COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DATA_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM → X10_ESTOQUE(COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DATA_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM)
- IDENT_PRODUTO_PERDA → X2013_PRODUTO(IDENT_PRODUTO)

---

## X138_ITEM_CUPOM_REF

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
| 11 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 12 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 13 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 14 | NUM_DOC | VARCHAR2(12) | N |  |  |
| 15 | DATA_EMISSAO | DATE | N |  |  |
| 16 | NUM_DOC_ITEM | VARCHAR2(12) | N |  |  |
| 17 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 18 | QUANTIDADE | NUMBER(17,3) | Y |  |  |
| 19 | NUM_RELATORIO | NUMBER(6) | Y |  |  |
| 20 | DATA_RELATORIO | DATE | Y |  |  |
| 21 | CNPJ_CGC | VARCHAR2(14) | Y |  |  |
| 22 | VLR_MERCADORIA | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ICMS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_EQUIPAMENTO, NUM_DOC, DATA_EMISSAO, NUM_DOC_ITEM

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X112_OBS_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_EQUIPAMENTO, NUM_DOC, DATA_EMISSAO → X117_CUPOM_REF(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_EQUIPAMENTO, NUM_DOC, DATA_EMISSAO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR_X138: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_X138: (IDENT_OBSERVACAO)

---

## X139_DET_ITEM_FASE_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | N |  |  |
| 4 | COD_OP | VARCHAR2(30) | N |  |  |
| 5 | COD_DIF_PRODUCAO | VARCHAR2(15) | N |  |  |
| 6 | IDENT_PRODUTO_OP | NUMBER(12) | N |  |  |
| 7 | NUM_ITEM | NUMBER(5) | N |  |  |
| 8 | COD_FASE_PRODUCAO | VARCHAR2(20) | N |  |  |
| 9 | DAT_VALID_INI | DATE | N |  |  |
| 10 | DT_SAIDA | DATE | N |  |  |
| 11 | IDENT_MEDIDA | NUMBER(12) | N |  |  |
| 12 | QTD_UTILIZADA | NUMBER(17,6) | N |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REF, COD_OP, COD_DIF_PRODUCAO, IDENT_PRODUTO_OP, NUM_ITEM, COD_FASE_PRODUCAO, DAT_VALID_INI, DT_SAIDA

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI → DWT_FASE_PRODUCAO(COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI)
- COD_EMPRESA, COD_ESTAB, PERIODO_REF, COD_OP, COD_DIF_PRODUCAO, IDENT_PRODUTO_OP, NUM_ITEM → X109_ITEM_OP(COD_EMPRESA, COD_ESTAB, PERIODO_REF, COD_OP, COD_DIF_PRODUCAO, IDENT_PRODUTO_OP, NUM_ITEM)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## X13_BEM_ATIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_BEM | VARCHAR2(60) | N |  |  |
| 4 | COD_INC | VARCHAR2(6) | N |  |  |
| 5 | VALID_BEM | DATE | N |  |  |
| 6 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 7 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 8 | IDENT_CONTA_CM | NUMBER(12) | Y |  |  |
| 9 | IDENT_CONTA_DEPR | NUMBER(12) | Y |  |  |
| 10 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 11 | IDENT_DESPESA | NUMBER(12) | Y |  |  |
| 12 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 13 | IDENT_SIT_BEM | NUMBER(12) | Y |  |  |
| 14 | COD_BEM_ORIG | VARCHAR2(60) | Y |  |  |
| 15 | COD_INC_ORIG | VARCHAR2(6) | Y |  |  |
| 16 | VALID_BEM_ORIG | DATE | Y |  |  |
| 17 | DATA_AQUIS | DATE | Y |  |  |
| 18 | DATA_BAIXA | DATE | Y |  |  |
| 19 | DATA_INI_CM | DATE | Y |  |  |
| 20 | DATA_INI_DEPR | DATE | Y |  |  |
| 21 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 22 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 23 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 24 | SERIE_BEM | VARCHAR2(15) | Y |  |  |
| 25 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 26 | TAXA_DEPR | NUMBER(8,4) | Y |  |  |
| 27 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 28 | VLR_EM_INDICE | NUMBER(18,4) | Y |  |  |
| 29 | VLR_AQUIS | NUMBER(17,2) | Y |  |  |
| 30 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 31 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 32 | IND_NAT_BEM | CHAR(1) | Y |  |  |
| 33 | VLR_AQUIS_REAL | NUMBER(17,2) | Y |  |  |
| 34 | VLR_DEPR_ACUM | NUMBER(17,2) | Y |  |  |
| 35 | VLR_DEPR_LANC | NUMBER(17,2) | Y |  |  |
| 36 | IND_GERA_P7 | CHAR(1) | Y |  |  |
| 37 | TIPO_BEM | CHAR(1) | Y |  |  |
| 38 | VIDA_UTIL | NUMBER(3) | Y |  |  |
| 39 | IND_BEM_ORI_ATIVO | CHAR(1) | Y |  |  |
| 40 | DSC_FUNCAO | VARCHAR2(150) | Y |  |  |
| 41 | DAT_FISCAL | DATE | Y |  |  |
| 42 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 43 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 44 | IND_COD_ALTERN | CHAR(1) | Y |  |  |
| 45 | IND_CRED_PIS_COFINS | CHAR(1) | Y |  |  |
| 46 | IND_PARCELA | VARCHAR2(3) | Y |  |  |
| 47 | IND_OPER_CRED | CHAR(1) | Y |  |  |
| 48 | IDENT_GRUPO_BEM | NUMBER(6) | Y |  |  |
| 49 | IND_UTIL_BEM | CHAR(1) | Y |  |  |
| 50 | VLR_DEP_AMORT_EXC | NUMBER(17,2) | Y |  |  |
| 51 | VLR_PARCELA_DEP_MES | NUMBER(17,2) | Y |  |  |
| 52 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 53 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 54 | IDENT_GRP_PROD | NUMBER(12) | Y |  |  |
| 55 | DATA_INI_CRED | DATE | Y |  |  |
| 56 | BCK_IND_PARCELA | VARCHAR2(3) | Y |  |  |
| 57 | NUM_PARC_APROP | NUMBER(3) | Y |  |  |
| 58 | DATA_CONCLUSAO_BRESULT | DATE | Y |  |  |
| 59 | IND_IMP | VARCHAR2(1) | Y |  |  |
| 60 | IND_SERV_MERC | VARCHAR2(1) | Y |  |  |
| 61 | IDENT_NBM | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_BEM_ORIG, COD_INC_ORIG, VALID_BEM_ORIG → X13_BEM_ATIVO(COD_EMPRESA, COD_ESTAB, COD_BEM, COD_INC, VALID_BEM)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_SIT_BEM → X2011_SIT_BEM(IDENT_SIT_BEM)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ALMOX → X2021_ALMOXARIFADO(IDENT_ALMOX)
- IDENT_CONTA_CM → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTA_DEPR → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_DESPESA → X2004_CENTRO_DESP(IDENT_DESPESA)

**Indexes**:
- IX_X13_BEM_ATIVO: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM)
- IX_X13_BEM_ATIVO_CTA: (IDENT_CONTA_DEPR)
- IX_X13_BEM_ATIVO_CTA_CM: (IDENT_CONTA_CM)
- IX_X13_X13: (COD_EMPRESA, COD_ESTAB, COD_BEM_ORIG, COD_INC_ORIG, VALID_BEM_ORIG)

---

## X140_MAPA_DIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IND_NORM_DEV | CHAR(1) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 9 | NUM_MAPA | NUMBER(12) | Y |  |  |
| 10 | DSC_HISTORICO | VARCHAR2(255) | Y |  |  |
| 11 | IDENT_PRODUTO_RES | NUMBER(12) | N |  |  |
| 12 | COD_OP | VARCHAR2(30) | Y |  |  |
| 13 | COD_DIF_PRODUCAO | VARCHAR2(15) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IND_NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_PRODUTO_RES

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_PRODUTO_RES → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_SAF_2390: (IDENT_FIS_JUR)

---

## X141_MAPA_DIST_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IND_NORM_DEV | CHAR(1) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | IDENT_PRODUTO_RES | NUMBER(12) | N |  |  |
| 9 | IDENT_PRODUTO_AGREG | NUMBER(12) | N |  |  |
| 10 | IND_MAT_MAO | CHAR(1) | Y |  |  |
| 11 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 12 | COD_TP_LANCTO | NUMBER(6) | N |  |  |
| 13 | VLR_ICMS_DCA | NUMBER(21,6) | Y |  |  |
| 14 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IND_NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_PRODUTO_RES, IDENT_PRODUTO_AGREG, COD_TP_LANCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IND_NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_PRODUTO_RES → X140_MAPA_DIST(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IND_NORM_DEV, NUM_DOCFIS, SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_PRODUTO_RES)
- IDENT_PRODUTO_AGREG → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_TP_LANCTO → SAICS_TP_LANCTO(COD_TP_LANCTO)

---

## X143_APURACAO_CUSTO_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 6 | VLR_CUSTO_PRODUCAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_CUSTO_ESTOQUE | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## X145_CONTRIB_RET_FONTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REC_RET | DATE | N |  |  |
| 4 | IND_NAT_REC | CHAR(1) | N |  |  |
| 5 | COD_RET_FONTE | VARCHAR2(2) | N |  |  |
| 6 | IDENT_FONTE_PAG | NUMBER(12) | N |  |  |
| 7 | VLR_RECEBIDO | NUMBER(19,4) | Y |  |  |
| 8 | VLR_TOT_RET_FONTE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_RET_FONTE_PIS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_RET_FONTE_COFINS | NUMBER(17,2) | Y |  |  |
| 11 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 12 | IND_COND_PJ_DECL | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 16 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 19 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 20 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 21 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 22 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REC_RET, COD_RET_FONTE, IDENT_FONTE_PAG, COD_RECEITA, IND_NAT_REC

**FKs**:
- IDENT_FONTE_PAG → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_FK_SAF_2467: (IDENT_FONTE_PAG)

---

## X147_OPER_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 6 | DATA_OPER | DATE | N |  |  |
| 7 | DISCRI_OPER | VARCHAR2(202) | N |  |  |
| 8 | VLR_OPER | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 11 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 14 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 15 | IND_ORIGEM_CRED | VARCHAR2(2) | Y |  |  |
| 16 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 17 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 18 | DESC_COMPL | VARCHAR2(255) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 21 | NUM_DOCTO | VARCHAR2(12) | N | ' ' |  |
| 22 | SERIE | VARCHAR2(3) | N | ' ' |  |
| 23 | SUB_SERIE | VARCHAR2(3) | N | ' ' |  |
| 24 | NUM_LANCTO | VARCHAR2(40) | N | ' ' |  |
| 25 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 26 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 27 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 28 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_DOCTO, DATA_OPER, DISCRI_OPER, NUM_DOCTO, SERIE, SUB_SERIE, NUM_LANCTO

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_FK_SAF_2458: (IDENT_FIS_JUR)
- IX_X147_OPER_CRED_CTA: (IDENT_CONTA)

---

## X148_BENS_ATIVO_IMOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_OPER_CRED | CHAR(1) | N |  |  |
| 4 | IDENT_GRUPO_BEM | NUMBER(6) | N |  |  |
| 5 | COD_BEM | VARCHAR2(60) | N |  |  |
| 6 | COD_INC_BEM | VARCHAR2(6) | N |  |  |
| 7 | DATA_LANCTO | DATE | N |  |  |
| 8 | IND_ORIGEM_CRED_BEM | CHAR(1) | N |  |  |
| 9 | IND_UTIL_BEM | CHAR(1) | Y |  |  |
| 10 | VLR_DEP_AMORT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DEP_AMORT_EXC | NUMBER(17,2) | Y |  |  |
| 12 | MES_ANO_AQUIS_BEM | VARCHAR2(6) | N |  |  |
| 13 | VLR_BEM_ATIVO_IMOB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_PARCELA_DEP_MES | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_CRED_PISPASEP | NUMBER(17,2) | Y |  |  |
| 16 | IND_PARCELA | CHAR(1) | Y |  |  |
| 17 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 18 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 20 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 21 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 22 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 24 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 25 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 26 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 27 | DESC_COMPL_BEM | VARCHAR2(255) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 30 | IND_CREDPIS_MSAF | CHAR(1) | Y |  |  |
| 31 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 32 | DISCRI_CONTA | CHAR(100) | N |  |  |
| 33 | NUM_PARC_CREDPIS | NUMBER(3) | Y |  |  |
| 34 | DATA_BAIXA | DATE | Y |  |  |
| 35 | IND_MOTIVO_BAIXA | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_OPER_CRED, IDENT_GRUPO_BEM, COD_BEM, COD_INC_BEM, DATA_LANCTO, MES_ANO_AQUIS_BEM, COD_SIT_PIS, COD_SIT_COFINS, IND_ORIGEM_CRED_BEM, DISCRI_CONTA

**FKs**:
- IDENT_GRUPO_BEM → X2053_GRUPO_BENS_ATIVO(IDENT_GRUPO_BEM)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_X148_BENS_ATIVO_IMOB_CTA: (IDENT_CONTA)

---

## X148_BENS_ATIVO_IMOB_BCK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_OPER_CRED | CHAR(1) | N |  |  |
| 4 | IDENT_GRUPO_BEM | NUMBER(6) | N |  |  |
| 5 | COD_BEM | VARCHAR2(60) | N |  |  |
| 6 | COD_INC_BEM | VARCHAR2(6) | N |  |  |
| 7 | DATA_LANCTO | DATE | N |  |  |
| 8 | IND_ORIGEM_CRED_BEM | CHAR(1) | Y |  |  |
| 9 | IND_UTIL_BEM | CHAR(1) | Y |  |  |
| 10 | VLR_DEP_AMORT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DEP_AMORT_EXC | NUMBER(17,2) | Y |  |  |
| 12 | MES_ANO_AQUIS_BEM | VARCHAR2(6) | N |  |  |
| 13 | VLR_BEM_ATIVO_IMOB | NUMBER(17,2) | Y |  |  |
| 14 | VLR_PARCELA_DEP_MES | NUMBER(17,2) | Y |  |  |
| 15 | VLR_BASE_CRED_PISPASEP | NUMBER(17,2) | Y |  |  |
| 16 | IND_PARCELA | CHAR(1) | Y |  |  |
| 17 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 18 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 20 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 21 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 22 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 24 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 25 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 26 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 27 | DESC_COMPL_BEM | VARCHAR2(255) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 30 | IND_CREDPIS_MSAF | CHAR(1) | Y |  |  |
| 31 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 32 | DISCRI_CONTA | CHAR(79) | Y |  |  |

---

## X149_UNID_IMOB_VEND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_UNID_IMOB | NUMBER(12) | N |  |  |
| 2 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 3 | DATA_VENDA_UNID_IMOB | DATE | N |  |  |
| 4 | IND_TP_OPERACAO | VARCHAR2(2) | Y |  |  |
| 5 | NUM_CONTRATO | VARCHAR2(90) | Y |  |  |
| 6 | INF_COMPL | VARCHAR2(90) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IDENT_SCP | NUMBER(12) | Y |  |  |

**PK**: IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB

**FKs**:
- IDENT_UNID_IMOB → X2054_UNID_IMOB(IDENT_UNID_IMOB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_FK_SAF_2480: (IDENT_FIS_JUR)

---

## X14_FOLHA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | IND_FOLHA | VARCHAR2(2) | N |  |  |
| 8 | DATA_PAGTO | DATE | Y |  |  |
| 9 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_OUTROS_DESC | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DEDUCAO_TAB | NUMBER(17,2) | Y |  |  |
| 12 | VLR_BASE_IRRF | NUMBER(17,2) | Y |  |  |
| 13 | VLR_IRRF | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DIF_IRRF | NUMBER(17,2) | Y |  |  |
| 15 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)

---

## X150_VAL_REC_UNID_IMOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_UNID_IMOB | NUMBER(12) | N |  |  |
| 2 | DATA_VENDA_UNID_IMOB | DATE | N |  |  |
| 3 | COMPETENCIA | VARCHAR2(6) | N |  |  |
| 4 | VLR_TOT_VENDA_UNID_IMOB | NUMBER(17,2) | Y |  |  |
| 5 | VLR_REC_ACUM_MES_ANT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_TOT_REC_MES_ESCRIT | NUMBER(17,2) | Y |  |  |
| 7 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 8 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 10 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 11 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 12 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 14 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | COD_NAT_REC | NUMBER(3) | Y |  |  |

**PK**: IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB, COMPETENCIA

**FKs**:
- IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB → X149_UNID_IMOB_VEND(IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB)

---

## X151_CUSTO_INC_UNID_IMOB_VEND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_UNID_IMOB | NUMBER(12) | N |  |  |
| 2 | DATA_VENDA_UNID_IMOB | DATE | N |  |  |
| 3 | COMPETENCIA | VARCHAR2(6) | N |  |  |
| 4 | VLR_TOT_CUSTO_MES_ANT | NUMBER(17,2) | Y |  |  |
| 5 | VLR_TOT_CUSTO_MES | NUMBER(17,2) | Y |  |  |
| 6 | VLR_PARC_S_CRED_ACUM | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_CRED_CUSTO | NUMBER(17,2) | Y |  |  |
| 8 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 9 | VLR_TOT_CRED_ACUM_PIS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 11 | VLR_PARC_CRED_DESC_PIS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_PARC_ADESC_PIS | NUMBER(17,2) | Y |  |  |
| 13 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 14 | VLR_TOT_CRED_ACUM_COFINS | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 16 | VLR_PARC_CRED_DESC_COFINS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_PARC_ADESC_COFINS | NUMBER(17,2) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB, COMPETENCIA, COD_SIT_PIS, COD_SIT_COFINS

**FKs**:
- IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB, COMPETENCIA → X150_VAL_REC_UNID_IMOB(IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB, COMPETENCIA)

---

## X152_CUSTO_ORC_UNID_IMOB_VEND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_UNID_IMOB | NUMBER(12) | N |  |  |
| 2 | DATA_VENDA_UNID_IMOB | DATE | N |  |  |
| 3 | COMPETENCIA | VARCHAR2(6) | N |  |  |
| 4 | VLR_TOT_CUSTO_ORC | NUMBER(17,2) | Y |  |  |
| 5 | VLR_AQ_SERV_NPAG_CONTRIB | NUMBER(17,2) | Y |  |  |
| 6 | VLR_BASE_CRED_ORC | NUMBER(17,2) | Y |  |  |
| 7 | VLR_BASE_CRED_ORC_PROP | NUMBER(17,2) | Y |  |  |
| 8 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 9 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 10 | VLR_CRED_UTIL_PIS | NUMBER(17,2) | Y |  |  |
| 11 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 12 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_CRED_UTIL_COFINS | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB, COMPETENCIA, COD_SIT_PIS, COD_SIT_COFINS

**FKs**:
- IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB, COMPETENCIA → X150_VAL_REC_UNID_IMOB(IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB, COMPETENCIA)

---

## X153_PROD_TERCEIROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_PRODUCAO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 6 | IDENT_MEDIDA | NUMBER(12) | N |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 10 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 13 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 14 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 15 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 16 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 17 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_PRODUCAO, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## X154_PROD_TERC_INSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_PRODUCAO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | DAT_CONSUMO | DATE | N |  |  |
| 6 | IDENT_PRODUTO_INS | NUMBER(12) | N |  |  |
| 7 | COD_FASE_PRODUCAO | VARCHAR2(20) | N |  |  |
| 8 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 9 | IDENT_MEDIDA | NUMBER(12) | N |  |  |
| 10 | IDENT_PRODUTO_SUB | NUMBER(12) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | NUM_ITEM | NUMBER(5) | N |  |  |
| 14 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 17 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 18 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 19 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 20 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 21 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_PRODUCAO, IDENT_PRODUTO, DAT_CONSUMO, IDENT_PRODUTO_INS, COD_FASE_PRODUCAO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_PRODUCAO, IDENT_PRODUTO → X153_PROD_TERCEIROS(COD_EMPRESA, COD_ESTAB, DAT_PRODUCAO, IDENT_PRODUTO)
- IDENT_PRODUTO_INS → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_PRODUTO_SUB → X2013_PRODUTO(IDENT_PRODUTO)

---

## X155_ITENS_MODAL

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
| 11 | NUM_ORDEM | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS_MODAL | VARCHAR2(9) | Y |  |  |
| 13 | SERIE_DOCFIS_MODAL | VARCHAR2(4) | Y |  |  |
| 14 | SUB_SERIE_DOCFIS_MODAL | VARCHAR2(3) | Y |  |  |
| 15 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 16 | DATA_EMISSAO_MODAL | DATE | Y |  |  |
| 17 | VLR_TOTAL_MODAL | NUMBER(17,2) | Y |  |  |
| 18 | CNPJ_CPF_EMIT | VARCHAR2(14) | Y |  |  |
| 19 | IDENT_UF_EMIT | NUMBER(12) | Y |  |  |
| 20 | IE_EMIT | VARCHAR2(14) | Y |  |  |
| 21 | IDENT_UF_ORIG | NUMBER(12) | Y |  |  |
| 22 | COD_MUNIC_ORIG | NUMBER(5) | Y |  |  |
| 23 | CNPJ_CPF_TOM | VARCHAR2(14) | Y |  |  |
| 24 | IDENT_UF_TOM | NUMBER(12) | Y |  |  |
| 25 | IE_TOM | VARCHAR2(14) | Y |  |  |
| 26 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 27 | COD_MUNIC_DEST | NUMBER(5) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ORDEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_UF_ORIG, COD_MUNIC_ORIG → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_UF_DESTINO, COD_MUNIC_DEST → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## X156_CAD_INSC_MUN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 4 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 5 | INSC_MUNICIPAL | VARCHAR2(14) | N |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_ESTADO, COD_MUNICIPIO, INSC_MUNICIPAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## X158_CRED_EXTEMP_ITEM_MERC

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
| 12 | DAT_LANC_PIS_COFINS | DATE | N |  |  |
| 13 | IND_PIS_COFINS_EXTEMP | CHAR(1) | N |  |  |
| 14 | IND_NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 15 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 16 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 17 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 19 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 20 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 21 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 22 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 23 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 25 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 26 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 27 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 28 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 29 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 30 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 32 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

---

## X159_CRED_EXTEMP_ITEM_SERV

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
| 11 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | DAT_LANC_PIS_COFINS | DATE | N |  |  |
| 14 | IND_PIS_COFINS_EXTEMP | CHAR(1) | N |  |  |
| 15 | IND_NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 17 | COD_SITUACAO_PIS | NUMBER(2) | Y |  |  |
| 18 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 20 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 21 | COD_SITUACAO_COFINS | NUMBER(2) | Y |  |  |
| 22 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 24 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 25 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 26 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 27 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM → X09_ITENS_SERV(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM)

---

## X15_FUNCIONARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | NOME | VARCHAR2(70) | Y |  |  |
| 6 | SEXO | CHAR(1) | Y |  |  |
| 7 | IDENT_NACAO | NUMBER(12) | Y |  |  |
| 8 | MUNICIPIO_NASC | VARCHAR2(30) | Y |  |  |
| 9 | IDENT_UF_NATURAL | NUMBER(12) | Y |  |  |
| 10 | CPF | VARCHAR2(14) | Y |  |  |
| 11 | IDENT_ESTADO_CIVIL | NUMBER(12) | Y |  |  |
| 12 | IDENT_INSTRUCAO | NUMBER(12) | Y |  |  |
| 13 | IND_PIS_PASEP | CHAR(1) | Y |  |  |
| 14 | PIS_PASEP | VARCHAR2(11) | Y |  |  |
| 15 | DATA_PIS_PASEP | DATE | Y |  |  |
| 16 | CART_PROF | NUMBER(11) | Y |  |  |
| 17 | SERIE_CART_PROF | VARCHAR2(7) | Y |  |  |
| 18 | IDENT_UF_CART_PROF | NUMBER(12) | Y |  |  |
| 19 | DATA_EXP_CART_PROF | DATE | Y |  |  |
| 20 | VALID_CART_PROF | DATE | Y |  |  |
| 21 | DATA_NASC | DATE | Y |  |  |
| 22 | NOME_PAI | VARCHAR2(50) | Y |  |  |
| 23 | NOME_MAE | VARCHAR2(50) | Y |  |  |
| 24 | CART_IDENTIDADE | VARCHAR2(15) | Y |  |  |
| 25 | IDENT_UF_CART_IDEN | NUMBER(12) | Y |  |  |
| 26 | DATA_EMIS_CART_ID | DATE | Y |  |  |
| 27 | ORGAO_EMISSOR | VARCHAR2(10) | Y |  |  |
| 28 | VALID_CART_IDENT | DATE | Y |  |  |
| 29 | TIPO_VISTO | VARCHAR2(2) | Y |  |  |
| 30 | IDENT_CONSELHO | NUMBER(12) | Y |  |  |
| 31 | NUM_REG_CONSELHO | NUMBER(10) | Y |  |  |
| 32 | DATA_REG_CONSELHO | DATE | Y |  |  |
| 33 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 34 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 35 | COMPL_ENDERECO | VARCHAR2(10) | Y |  |  |
| 36 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 37 | MUNICIPIO | VARCHAR2(30) | Y |  |  |
| 38 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 39 | CEP | NUMBER(8) | Y |  |  |
| 40 | ANO_CHEGADA | NUMBER(4) | Y |  |  |
| 41 | IDENT_ADMISSAO | NUMBER(12) | Y |  |  |
| 42 | DATA_ADMISSAO | DATE | Y |  |  |
| 43 | IDENT_CAUSA_DESLIG | NUMBER(12) | Y |  |  |
| 44 | DATA_DEMISSAO | DATE | Y |  |  |
| 45 | IDENT_VINCULO_EMP | NUMBER(12) | Y |  |  |
| 46 | DATA_OPCAO | DATE | Y |  |  |
| 47 | IDENT_TURNO | NUMBER(12) | Y |  |  |
| 48 | JORNADA_SEMANAL | NUMBER(4,2) | Y |  |  |
| 49 | IDENT_TIPO_SALARIO | NUMBER(12) | Y |  |  |
| 50 | SALARIO_BASE | NUMBER(17,2) | Y |  |  |
| 51 | ADIC_PERICUL | NUMBER(5,2) | Y |  |  |
| 52 | ADIC_INSALUBRIDADE | NUMBER(5,2) | Y |  |  |
| 53 | ADIC_OUTROS | NUMBER(5,2) | Y |  |  |
| 54 | NUM_DEPEND | NUMBER(2) | Y |  |  |
| 55 | NUM_REGISTRO | VARCHAR2(14) | Y |  |  |
| 56 | NUM_MATRICULA | VARCHAR2(8) | Y |  |  |
| 57 | IDENT_CBO | NUMBER(12) | Y |  |  |
| 58 | IDENT_FUNCAO | NUMBER(12) | Y |  |  |
| 59 | IDENT_SINDICATO | NUMBER(12) | Y |  |  |
| 60 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 61 | IDENT_SETOR | NUMBER(12) | Y |  |  |
| 62 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 63 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 64 | NUM_DEP_SAL_FAM | NUMBER(2) | Y |  |  |
| 65 | CATEGORIA_TRAB | VARCHAR2(2) | Y |  |  |
| 66 | DATA_VALID | DATE | Y |  |  |
| 67 | E_MAIL | VARCHAR2(50) | Y |  |  |
| 68 | OCORRENCIA_TRAB | VARCHAR2(2) | Y |  |  |
| 69 | IND_ESTAGIARIO | CHAR(1) | Y |  |  |
| 70 | MES_ANO_SAIDA_PAIS | NUMBER(6) | Y |  |  |
| 71 | MES_ANO_RET_PAIS | NUMBER(6) | Y |  |  |
| 72 | DATA_MOLESTIA | DATE | Y |  |  |
| 73 | COD_OPER_SAUDE | VARCHAR2(4) | Y |  |  |
| 74 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 75 | NUM_ID_FISCAL | VARCHAR2(30) | Y |  |  |
| 76 | DDD | VARCHAR2(4) | Y |  |  |
| 77 | TELEFONE | VARCHAR2(11) | Y |  |  |
| 78 | DSC_PROVINCIA_EX | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC

**FKs**:
- IDENT_TURNO → Y2085_TURNO_TRAB(IDENT_TURNO)
- IDENT_CAUSA_DESLIG → X2028_CAUSA_DESLIG(IDENT_CAUSA_DESLIG)
- IDENT_CBO → X2029_COD_CBO(IDENT_CBO)
- IDENT_VINCULO_EMP → X2030_VINC_EMPREG(IDENT_VINCULO_EMP)
- IDENT_INSTRUCAO → X2031_TIPO_INSTR(IDENT_INSTRUCAO)
- IDENT_TIPO_SALARIO → X2032_TIPO_SALARIO(IDENT_TIPO_SALARIO)
- IDENT_ESTADO_CIVIL → X2033_ESTADO_CIVIL(IDENT_ESTADO_CIVIL)
- IDENT_FUNCAO → X2036_FUNCAO(IDENT_FUNCAO)
- IDENT_SETOR → X2037_SETOR(IDENT_SETOR)
- IDENT_SINDICATO → X2048_SINDICATO(IDENT_SINDICATO)
- IDENT_CONSELHO → X2082_CONS_REGPROF(IDENT_CONSELHO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_NACAO → NACIONALIDADE(IDENT_NACAO)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_ADMISSAO → X2027_TIPO_ADMIS(IDENT_ADMISSAO)
- COD_OPER_SAUDE → DWT_OPERADORA_SAUDE(COD_OPER_SAUDE)
- COD_PAIS → PAIS(COD_PAIS)

**Indexes**:
- IX_X15_FUNC_CPF: (COD_EMPRESA, CPF)

---

## X160_PROC_REF_OPER_CRED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 4 | DATA_OPER | DATE | N |  |  |
| 5 | DISCRI_OPER | VARCHAR2(202) | N |  |  |
| 6 | NUM_DOCTO | VARCHAR2(12) | N | ' ' |  |
| 7 | SERIE | VARCHAR2(3) | N | ' ' |  |
| 8 | SUB_SERIE | VARCHAR2(2) | N | ' ' |  |
| 9 | NUM_LANCTO | VARCHAR2(40) | N | ' ' |  |
| 10 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 11 | ORIG_PROCESSO | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_DOCTO, DATA_OPER, DISCRI_OPER, NUM_DOCTO, SERIE, SUB_SERIE, NUM_LANCTO, IDENT_PROC_REF

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)
- COD_EMPRESA, COD_ESTAB, IDENT_DOCTO, DATA_OPER, DISCRI_OPER, NUM_DOCTO, SERIE, SUB_SERIE, NUM_LANCTO → X147_OPER_CRED(COD_EMPRESA, COD_ESTAB, IDENT_DOCTO, DATA_OPER, DISCRI_OPER, NUM_DOCTO, SERIE, SUB_SERIE, NUM_LANCTO)

---

## X161_DOC_TELECOM_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IND_TIPO_RECEITA | CHAR(1) | N |  |  |
| 9 | DATA_DOC_INICIAL | DATE | N |  |  |
| 10 | DATA_DOC_FINAL | DATE | Y |  |  |
| 11 | QTD_DOC_CONS | NUMBER(7) | Y |  |  |
| 12 | VLR_DOC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DESC | NUMBER(17,2) | Y |  |  |
| 14 | VLR_SERV | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SERV_NT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TERC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_DESP_ACS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 24 | IDENT_SCP | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TIPO_RECEITA, DATA_DOC_INICIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

---

## X162_ITM_TELECOM_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IND_TIPO_RECEITA | CHAR(1) | N |  |  |
| 9 | DATA_DOC_INICIAL | DATE | N |  |  |
| 10 | COD_CLASS_ITEM | VARCHAR2(4) | N |  |  |
| 11 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 12 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DESC | NUMBER(17,2) | Y |  |  |
| 14 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 15 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 17 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 18 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 19 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 21 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 22 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TIPO_RECEITA, DATA_DOC_INICIAL, COD_CLASS_ITEM, COD_SIT_PIS, COD_SIT_COFINS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TIPO_RECEITA, DATA_DOC_INICIAL → X161_DOC_TELECOM_CONS(COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TIPO_RECEITA, DATA_DOC_INICIAL)

---

## X164_ING_MARCA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_MARCA_COM | NUMBER(12) | N |  |  |
| 3 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 4 | COD_ING_ATIVO | VARCHAR2(35) | N |  |  |
| 5 | DAT_VALID | DATE | N |  |  |
| 6 | PERC_CONCENT | NUMBER(7,4) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_MARCA_COM, TIPO_OBRIGACAO, COD_ING_ATIVO, DAT_VALID

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)
- TIPO_OBRIGACAO, COD_ING_ATIVO → X127_ING_ATIVO(TIPO_OBRIGACAO, COD_ING_ATIVO)
- IDENT_MARCA_COM → X2025_MARCA_COMERC(IDENT_MARCA_COM)

---

## X165_INC_IMOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_EMPREENDIMENTO | VARCHAR2(9) | N |  |  |
| 4 | ALIQ_REC | NUMBER(6,2) | N |  |  |
| 5 | DATA_REC_UNI | DATE | Y |  |  |
| 6 | DATA_APURACAO | DATE | N |  |  |
| 7 | IDENT_DARF | NUMBER(12) | N |  |  |
| 8 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 9 | INC_IMOB | VARCHAR2(90) | N |  |  |
| 10 | VLR_RECEB_REC | NUMBER(15,2) | N |  |  |
| 11 | VLR_FIN_REC | NUMBER(15,2) | Y |  |  |
| 12 | VLR_BASE_REC | NUMBER(15,2) | N |  |  |
| 13 | VLR_REC_UNI | NUMBER(15,2) | N |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 16 | IDENT_SCP | NUMBER(12) | Y |  |  |

**FKs**:
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DARF → X2019_COD_DARF(IDENT_DARF)

**Indexes**:
- UK_X165_INC_IMOB (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_EMPREENDIMENTO, ALIQ_REC, DISCRI_ITEM, DATA_APURACAO, IDENT_DARF, IDENT_SCP)

---

## X166_PROC_REF_BENS_ATIV_BCK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | IND_OPER_CRED | CHAR(1) | Y |  |  |
| 4 | IDENT_GRUPO_BEM | NUMBER(6) | Y |  |  |
| 5 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 6 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 7 | DATA_LANCTO | DATE | Y |  |  |
| 8 | MES_ANO_AQUIS_BEM | VARCHAR2(6) | Y |  |  |
| 9 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 10 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 11 | IDENT_PROC_REF | NUMBER(12) | Y |  |  |
| 12 | ORIG_PROCESSO | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | IND_ORIGEM_CRED_BEM | CHAR(1) | Y |  |  |
| 16 | DISCRI_CONTA | CHAR(79) | Y |  |  |

---

## X166_PROC_REF_BENS_ATIV_IMOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_OPER_CRED | CHAR(1) | N |  |  |
| 4 | IDENT_GRUPO_BEM | NUMBER(6) | N |  |  |
| 5 | COD_BEM | VARCHAR2(60) | N |  |  |
| 6 | COD_INC_BEM | VARCHAR2(6) | N |  |  |
| 7 | DATA_LANCTO | DATE | N |  |  |
| 8 | MES_ANO_AQUIS_BEM | VARCHAR2(6) | N |  |  |
| 9 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 10 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 11 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 12 | ORIG_PROCESSO | CHAR(1) | N |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | IND_ORIGEM_CRED_BEM | CHAR(1) | N |  |  |
| 16 | DISCRI_CONTA | CHAR(100) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_OPER_CRED, IDENT_GRUPO_BEM, COD_BEM, COD_INC_BEM, DATA_LANCTO, MES_ANO_AQUIS_BEM, COD_SIT_PIS, COD_SIT_COFINS, IDENT_PROC_REF, ORIG_PROCESSO, IND_ORIGEM_CRED_BEM, DISCRI_CONTA

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)

---

## X167_PROC_REF_UND_IMOB_VEND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_UNID_IMOB | NUMBER(12) | N |  |  |
| 2 | DATA_VENDA_UNID_IMOB | DATE | N |  |  |
| 3 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 4 | ORIG_PROCESSO | CHAR(1) | N |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB, IDENT_PROC_REF, ORIG_PROCESSO

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)
- IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB → X149_UNID_IMOB_VEND(IDENT_UNID_IMOB, DATA_VENDA_UNID_IMOB)

---

## X168_CRED_EXTEMP_PIS_COFINS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CRED_EXTEMP | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_COMPETENCIA | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 7 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 11 | DATA_OPER | DATE | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 13 | DISCRI_ITEM | VARCHAR2(76) | Y |  |  |
| 14 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 15 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 16 | VLR_OPER | NUMBER(17,2) | N |  |  |
| 17 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 18 | IND_NAT_BASE_CRED | VARCHAR2(2) | N |  |  |
| 19 | IND_ORIG_CRED | CHAR(1) | N |  |  |
| 20 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 21 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 22 | QUANT_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 23 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 24 | VLR_ALIQ_PIS_QUANT | NUMBER(19,4) | Y |  |  |
| 25 | VLR_PIS | NUMBER(17,2) | N |  |  |
| 26 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 27 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 28 | QUANT_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 29 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 30 | VLR_ALIQ_COFINS_QUANT | NUMBER(19,4) | Y |  |  |
| 31 | VLR_COFINS | NUMBER(17,2) | N |  |  |
| 32 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 33 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 34 | PERIODO_ESCRIT | VARCHAR2(6) | Y |  |  |
| 35 | DESC_COMPL | VARCHAR2(255) | Y |  |  |
| 36 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 37 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_CRED_EXTEMP

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

**Indexes**:
- IX_FK_SAF_2587: (IDENT_FIS_JUR)
- IX_X168_CTA: (IDENT_CONTA)
- UIX_X168_CRED_EXT_PIS_COFINS (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_COMPETENCIA, IDENT_FIS_JUR, IDENT_PRODUTO, IDENT_SERVICO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS, DATA_OPER, NUM_ITEM, DISCRI_ITEM)

---

## X169_SALDO_ANTES_ENC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SALDO_ANT_ENC | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 6 | DATA_SALDO | DATE | N |  |  |
| 7 | IND_DEB_CRED | CHAR(1) | N |  |  |
| 8 | VLR_SALDO_FINAL | NUMBER(19,2) | N |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_SALDO_ANT_ENC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)

**Indexes**:
- IX_X169_CTA: (IDENT_CONTA)
- IX_X169_SALDO_ANTES_ENC (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_CONTA, IDENT_CUSTO, DATA_SALDO)

---

## X16_PROD_ACABADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_MOVTO | DATE | N |  |  |
| 5 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 6 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 7 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 8 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 9 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 10 | QTD_FABR | NUMBER(17,6) | Y |  |  |
| 11 | PERC_PERDA | NUMBER(7,4) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_ALMOX → X2021_ALMOXARIFADO(IDENT_ALMOX)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- IX_X16_PROD_ACABADO_CTA: (IDENT_CONTA)

---

## X170_INS_FASE_PRODUCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_MOVTO | DATE | N |  |  |
| 5 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 6 | COD_FASE_PRODUCAO | VARCHAR2(20) | N |  |  |
| 7 | DAT_VALID_INI | DATE | N |  |  |
| 8 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 9 | QTD_MIN_UTILIZADA | NUMBER(17,6) | Y |  |  |
| 10 | QTD_MAX_UTILIZADA | NUMBER(17,6) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, IDENT_INSUMO, COD_FASE_PRODUCAO, DAT_VALID_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, IDENT_INSUMO → X17_PROD_INSUMO(COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, IDENT_INSUMO)
- COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI → DWT_FASE_PRODUCAO(COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## X171_RATEIO_SLD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 6 | VLR_RATEIO_CRE | NUMBER(17,2) | Y |  |  |
| 7 | VLR_RATEIO_DEB | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO, IDENT_CONTA_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO → X02_SALDOS(COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO)

---

## X172_RATEIO_SLD_CCUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_SALDO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 6 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 7 | VLR_RATEIO_CRE | NUMBER(17,2) | Y |  |  |
| 8 | VLR_RATEIO_DEB | NUMBER(17,2) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_CUSTO, IDENT_CONTA_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_CUSTO → X80_SALDOS_CCUSTO(COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_CUSTO)

---

## X173_RATEIO_LANCTO_FCONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_LANCTO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 8 | VLR_RATEIO | NUMBER(17,2) | Y |  |  |
| 9 | IND_CONTABIL | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO, IDENT_CONTA_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO → X129_INCL_CONTABIL(COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO)

---

## X174_RATEIO_LANCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_LANCTO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 8 | VLR_RATEIO | NUMBER(17,2) | Y |  |  |
| 9 | IND_CONTABIL | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO, IDENT_CONTA_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO → X01_CONTABIL(COD_EMPRESA, COD_ESTAB, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO)

---

## X175_ESTORNO_DEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_DECL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | DAT_EMISSAO | DATE | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | NUM_ITEM | NUMBER(7) | N |  |  |
| 10 | NUM_DOCFIS_RES | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS_RES | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS_RES | VARCHAR2(2) | N |  |  |
| 13 | NUM_ITEM_RES | NUMBER(7) | N |  |  |
| 14 | DAT_EMISSAO_RES | DATE | N |  |  |
| 15 | IND_TIPO_INF | CHAR(1) | Y |  |  |
| 16 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 17 | IDENT_MODELO_RES | NUMBER(12) | Y |  |  |
| 18 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |
| 19 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  |  |
| 20 | VLR_TOT_NF | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 24 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_ICMS_IT | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ICMS_IT | NUMBER(17,2) | Y |  |  |
| 27 | MOTIVO_ESTORNO | VARCHAR2(200) | Y |  |  |
| 28 | NUM_RECLAMACAO | VARCHAR2(20) | Y |  |  |
| 29 | VLR_ICMS_ESTORNO | NUMBER(17,2) | Y |  |  |
| 30 | HIPOTESE_ESTORNO | CHAR(1) | Y |  |  |
| 31 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 32 | IND_STATUS | CHAR(1) | Y |  |  |
| 33 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 34 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_DECL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DAT_EMISSAO, IDENT_FIS_JUR, NUM_ITEM, NUM_DOCFIS_RES, SERIE_DOCFIS_RES, SUB_SERIE_DOCFIS_RES, NUM_ITEM_RES, DAT_EMISSAO_RES

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_MODELO_RES → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_SAF_2881: (IDENT_FIS_JUR)

---

## X176_PRT_CTA_CUSTO_F100

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PARAM | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_VALIDADE | DATE | N |  |  |
| 5 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 6 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 7 | IND_TP_OPER | CHAR(1) | Y |  |  |
| 8 | COD_TRIB_PIS | NUMBER(2) | Y |  |  |
| 9 | COD_TRIB_COFINS | NUMBER(2) | Y |  |  |
| 10 | NAT_BC_CRED | VARCHAR2(2) | Y |  |  |
| 11 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 12 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |

**PK**: IDENT_PARAM

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IU_X176_PRT_CTA_CUSTO_F100 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_VALIDADE, IDENT_CONTA, IDENT_CUSTO, IDENT_PRODUTO, IND_TP_OPER, COD_TRIB_PIS, COD_TRIB_COFINS)
- IX_X176_CTA: (IDENT_CONTA)

---

## X177_PROC_REF_DOC_EE_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_CLASSE_CONSUMO | NUMBER(12) | N |  |  |
| 9 | DATA_DOCTO | DATE | N |  |  |
| 10 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 11 | ORIG_PROCESSO | CHAR(1) | N |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO, IDENT_PROC_REF, ORIG_PROCESSO

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)
- COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO → X190_DOC_ENERG_CONS(COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO)

---

## X178_PROC_REF_CAPA_TELECOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 9 | ORIG_PROCESSO | CHAR(1) | N |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PROC_REF, ORIG_PROCESSO

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X42_CAPA_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## X179_LIVRO_AUX_SUBCONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_LIVRO_AUX | VARCHAR2(3) | N |  |  |
| 4 | COD_NAT_SUBCONTAS | VARCHAR2(2) | N |  |  |
| 5 | IDENT_CONTA_SUB | NUMBER(12) | N |  |  |
| 6 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 7 | COD_CNPJ_INV | VARCHAR2(14) | N |  |  |
| 8 | COD_ITEM_ATIV_PAS | VARCHAR2(10) | N |  |  |
| 9 | COD_INDIV_BEM | VARCHAR2(60) | N |  |  |
| 10 | DATA_CONTAB_ITEM | DATE | N |  |  |
| 11 | DATA_LANCTO | DATE | N |  |  |
| 12 | NUM_LANCAMENTO | VARCHAR2(40) | N |  |  |
| 13 | DSC_RESUM_ITEM | VARCHAR2(50) | Y |  |  |
| 14 | QTD_INIC_ITEM | NUMBER(19,2) | Y |  |  |
| 15 | VLR_SALDO_INI_CONTA | NUMBER(19,2) | Y |  |  |
| 16 | IND_SALDO_INI_CONTA | CHAR(1) | Y |  |  |
| 17 | VLR_PARC_ITEM | NUMBER(19,2) | Y |  |  |
| 18 | IND_PARC_ITEM | CHAR(1) | Y |  |  |
| 19 | VLR_SALDO_FIN_CONTA | NUMBER(19,2) | Y |  |  |
| 20 | IND_SALDO_FIN_CONTA | CHAR(1) | Y |  |  |
| 21 | VLR_SALDO_INI_SUBCONTA | NUMBER(19,2) | Y |  |  |
| 22 | IND_SALDO_INI_SUBCONTA | CHAR(1) | Y |  |  |
| 23 | VLR_DEB_SUBCONTA | NUMBER(19,2) | Y |  |  |
| 24 | VLR_CRED_SUBCONTA | NUMBER(19,2) | Y |  |  |
| 25 | VLR_SALDO_FIN_SUBCONTA | NUMBER(19,2) | Y |  |  |
| 26 | IND_SALDO_FIN_SUBCONTA | CHAR(1) | Y |  |  |
| 27 | VLR_LANCTO | NUMBER(19,2) | Y |  |  |
| 28 | IND_LANCTO | CHAR(1) | Y |  |  |
| 29 | IND_REG_INI | CHAR(1) | Y |  |  |
| 30 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 31 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 32 | ARQUIVAMENTO | VARCHAR2(50) | N | ' ' |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_LIVRO_AUX, COD_NAT_SUBCONTAS, IDENT_CONTA_SUB, IDENT_CUSTO, COD_CNPJ_INV, COD_ITEM_ATIV_PAS, COD_INDIV_BEM, DATA_CONTAB_ITEM, DATA_LANCTO, NUM_LANCAMENTO, ARQUIVAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA_SUB → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X179_CTA: (IDENT_CONTA_SUB)

---

## X17_PROD_INSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_MOVTO | DATE | N |  |  |
| 5 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 6 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 7 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 8 | QTD_USADA | NUMBER(17,6) | Y |  |  |
| 9 | PERC_PERDA | NUMBER(7,4) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | DAT_FIM | DATE | Y |  |  |
| 13 | QTD_MAX_UTILIZADA | NUMBER(17,6) | Y |  |  |
| 14 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 15 | DAT_VALID_INI | DATE | Y |  |  |
| 16 | TPO_VARIACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, IDENT_INSUMO

**FKs**:
- COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO → X16_PROD_ACABADO(COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO)
- IDENT_INSUMO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI → DWT_FASE_PRODUCAO(COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI)

---

## X180_EMB_FASE_PRODUCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_MOVTO | DATE | N |  |  |
| 5 | IDENT_EMBALAGEM | NUMBER(12) | N |  |  |
| 6 | COD_FASE_PRODUCAO | VARCHAR2(20) | N |  |  |
| 7 | DAT_VALID_INI | DATE | N |  |  |
| 8 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 9 | QTD_MIN_UTILIZADA | NUMBER(17,6) | Y |  |  |
| 10 | QTD_MAX_UTILIZADA | NUMBER(17,6) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, IDENT_EMBALAGEM, COD_FASE_PRODUCAO, DAT_VALID_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, IDENT_EMBALAGEM → X18_PROD_EMBALAG(COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, IDENT_EMBALAGEM)
- COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI → DWT_FASE_PRODUCAO(COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## X182_REG_MOV_VEICULO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_ENTRADA | DATE | N |  |  |
| 4 | HORA_ENTRADA | NUMBER(6) | N |  |  |
| 5 | PLACA_VEICULO | VARCHAR2(7) | N |  |  |
| 6 | DSC_MARCA | VARCHAR2(20) | N |  |  |
| 7 | DSC_MODELO | VARCHAR2(20) | N |  |  |
| 8 | NUM_ANO_FABRIC | NUMBER(4) | N |  |  |
| 9 | NUM_CHASSI | VARCHAR2(28) | N |  |  |
| 10 | NUM_MOTOR | VARCHAR2(28) | N |  |  |
| 11 | DSC_COMPL | VARCHAR2(255) | Y |  |  |
| 12 | IND_PROP | CHAR(1) | N |  |  |
| 13 | IDENT_ESTADO_ORIG | NUMBER(12) | N |  |  |
| 14 | IDENT_ESTADO_REG | NUMBER(12) | N |  |  |
| 15 | COD_MUNIC_REG | NUMBER(5) | N |  |  |
| 16 | IDENT_FIS_JUR_ENT | NUMBER(12) | N |  |  |
| 17 | IND_TP_NEG | CHAR(1) | N |  |  |
| 18 | VLR_VEICULO | NUMBER(17,2) | Y |  |  |
| 19 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 20 | DAT_SAIDA | DATE | Y |  |  |
| 21 | IDENT_FIS_JUR_SAI | NUMBER(12) | Y |  |  |
| 22 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_ENTRADA, HORA_ENTRADA, PLACA_VEICULO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO_REG, COD_MUNIC_REG → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_FIS_JUR_ENT → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_FIS_JUR_SAI → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_2614: (IDENT_FIS_JUR_ENT)
- IX_FK_SAF_2615: (IDENT_OBSERVACAO)
- IX_FK_SAF_2616: (IDENT_FIS_JUR_SAI)

---

## X183_PJ_APUR_LP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PJ_APUR_LP | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | IND_TP_REGIME | CHAR(1) | N |  |  |
| 5 | IND_COMP_REC | VARCHAR2(2) | Y |  |  |
| 6 | DESC_COMPL_COMP_REC | VARCHAR2(255) | Y |  |  |
| 7 | NUM_DOCTO | VARCHAR2(12) | Y |  |  |
| 8 | SERIE | VARCHAR2(3) | Y |  |  |
| 9 | SUB_SERIE | VARCHAR2(2) | Y |  |  |
| 10 | NUM_LANCTO | VARCHAR2(40) | Y |  |  |
| 11 | DATA_OPER | DATE | N |  |  |
| 12 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 13 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 14 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 15 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 16 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 17 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 18 | DISCRI_PJ_APUR | VARCHAR2(50) | N |  |  |
| 19 | DESC_COMPL | VARCHAR2(255) | Y |  |  |
| 20 | VLR_RECEITA | NUMBER(17,2) | N |  |  |
| 21 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 22 | VLR_ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 23 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 25 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 26 | VLR_DESC_PIS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 28 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 29 | VLR_ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 30 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 32 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 33 | VLR_DESC_COFINS | NUMBER(17,2) | Y |  |  |
| 34 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 35 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 36 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 37 | COD_SIT_DOCTO | CHAR(1) | Y |  |  |
| 38 | IND_TP_FATURA | CHAR(1) | Y |  |  |
| 39 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 40 | IDENT_SCP | NUMBER(12) | Y |  |  |

**PK**: IDENT_PJ_APUR_LP

**FKs**:
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_X183_IDENT_CONTA: (IDENT_CONTA)
- IX_X183_IDENT_FIS_JUR: (IDENT_FIS_JUR)
- IX_X183_IDENT_MODELO: (IDENT_MODELO)
- UIX_X183_PJ_APUR_LP (UNIQUE): (COD_EMPRESA, COD_ESTAB, IND_TP_REGIME, IND_COMP_REC, DESC_COMPL_COMP_REC, NUM_DOCTO, SERIE, SUB_SERIE, NUM_LANCTO, DATA_OPER, IDENT_MODELO, IDENT_CFO, IDENT_FIS_JUR, IDENT_PRODUTO, IDENT_CONTA, IDENT_CUSTO, DISCRI_PJ_APUR, DESC_COMPL, IDENT_SCP)

---

## X184_PROC_REF_PJ_APUR_LP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PJ_APUR_LP | NUMBER(12) | N |  |  |
| 2 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 3 | ORIG_PROCESSO | CHAR(1) | N |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PJ_APUR_LP, IDENT_PROC_REF, ORIG_PROCESSO

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)
- IDENT_PJ_APUR_LP → X183_PJ_APUR_LP(IDENT_PJ_APUR_LP)

---

## X185_CONTRIB_PREV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | N |  | Código da receita obtido da tabela DWT_COD_RECEITA; São considerados apenas os códigos do INSS (COD_TRIBUTO = 15). |
| 5 | DISCRI_ATIV_CONT_PREV | VARCHAR2(90) | N |  | Campo chave formado pela concatenação dos campos DWT_ATIV_CONT_PREV.COD_ATIV_CONT_PREV + X2002_PLANO_CONTAS.COD_CONTA + VLR_ALIQ_CONT_PREV |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | IDENT_ATIV_CONT_PREV | NUMBER(5) | Y |  | Relacionado com a TACES75 (DWT_ATIV_CONT_PREV) |
| 8 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 9 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 10 | VLR_REC_BRT | NUMBER(17,2) | Y |  | Valor da Receita Bruta Total |
| 11 | VLR_REC_BRT_ATIV | NUMBER(17,2) | Y |  | Valor da Receita Bruta do Estabelecimento, correspondente à atividade informada no campo IDENT_ATIV_CONT_PREV |
| 12 | VLR_REC_BRT_DEMAIS_ATIV | NUMBER(17,2) | Y |  | Valor da Receita de Demais Atividades |
| 13 | VLR_EXC_REC_BRT | NUMBER(17,2) | Y |  | Valor das Exclusões da Receita Bruta |
| 14 | VLR_BASE_CONT_PREV | NUMBER(17,2) | Y |  | Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta (VLR_REC_BRT_ATIV - VLR_EXC_REC_BRT) |
| 15 | VLR_ALIQ_CONT_PREV | NUMBER(12,4) | Y |  | Alíquota da Contribuição Previdenciária sobre a Receita Bruta |
| 16 | VLR_CONT_PREV | NUMBER(17,2) | Y |  | Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta (VLR_BASE_CONT_PREV * VLR_ALIQ_CONT_PREV/100) |
| 17 | DSC_COMPLEMENTAR | VARCHAR2(255) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 20 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 21 | VLR_BASE_CONT_PREV_REINF | NUMBER(17,2) | Y |  |  |
| 22 | VLR_CONT_PREV_REINF | NUMBER(17,2) | Y |  |  |
| 23 | VLR_AJUSTE_ADICAO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_AJUSTE_EXCLUSAO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ATIV_CONT_PREV → DWT_ATIV_CONT_PREV(IDENT_ATIV_CONT_PREV)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_X185_CTA: (IDENT_CONTA)

---

## X186_PROC_REF_CONTRIB_PREV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 5 | DISCRI_ATIV_CONT_PREV | VARCHAR2(90) | N |  |  |
| 6 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 7 | ORIG_PROCESSO | CHAR(1) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV, IDENT_PROC_REF

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)
- COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV → X185_CONTRIB_PREV(COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV)

---

## X187_PJ_APUR_LP_RECEB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PJ_APUR_LP | NUMBER(12) | N |  |  |
| 2 | IDENT_PJ_APUR_LP_RECEB | NUMBER(12) | N |  |  |
| 3 | MES_ANO_COMPETENCIA | VARCHAR2(6) | N |  |  |
| 4 | VLR_RECEITA_RECEB | NUMBER(17,2) | N |  |  |
| 5 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 6 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 7 | VLR_DESC_PIS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 10 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 11 | VLR_DESC_COFINS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PJ_APUR_LP_RECEB

**FKs**:
- IDENT_PJ_APUR_LP → X183_PJ_APUR_LP(IDENT_PJ_APUR_LP)

**Indexes**:
- UIX_X187_PJ_APUR_LP_RECEB (UNIQUE): (IDENT_PJ_APUR_LP, MES_ANO_COMPETENCIA)

---

## X188_TRANSF_SALDO_CONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | IDENT_CONTA_ANT | NUMBER(12) | N |  |  |
| 6 | IDENT_CUSTO_ANT | NUMBER(12) | Y |  |  |
| 7 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 8 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 11 | ID_X188 | NUMBER(38) | N |  |  |

**PK**: ID_X188

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTA_ANT → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO_ANT → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO → X02_SALDOS(COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO)

**Indexes**:
- IX_X188_CTA: (IDENT_CONTA)
- IX_X188_CTA_ANT: (IDENT_CONTA_ANT)
- UK_X188_TRANSF_SALDO_CONTA (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_SALDO, IDENT_CONTA_ANT, IDENT_CUSTO_ANT)

---

## X188_TRANSF_SALDO_CONTA_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_SALDO | DATE | N |  |  |
| 5 | IDENT_CONTA_ANT | NUMBER(12) | N |  |  |
| 6 | IDENT_CUSTO_ANT | NUMBER(12) | Y |  |  |
| 7 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 8 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 11 | ID_X188 | NUMBER(38) | Y |  |  |

---

## X189_TRANSF_SALDO_CUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 5 | DATA_SALDO | DATE | N |  |  |
| 6 | IDENT_CONTA_ANT | NUMBER(12) | N |  |  |
| 7 | IDENT_CUSTO_ANT | NUMBER(12) | Y |  |  |
| 8 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 9 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | ID_X189 | NUMBER(38) | N |  |  |

**PK**: ID_X189

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTA_ANT → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_CUSTO_ANT → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- COD_EMPRESA, COD_ESTAB, DATA_SALDO, IDENT_CONTA, IDENT_CUSTO → X80_SALDOS_CCUSTO(COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_CUSTO)

**Indexes**:
- IX_X189_CTA: (IDENT_CONTA)
- IX_X189_CTA_ANT: (IDENT_CONTA_ANT)
- UK_X189_TRANSF_SALDO_CUSTO (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_CONTA, IDENT_CUSTO, DATA_SALDO, IDENT_CONTA_ANT, IDENT_CUSTO_ANT)

---

## X189_TRANSF_SALDO_CUSTO_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 5 | DATA_SALDO | DATE | N |  |  |
| 6 | IDENT_CONTA_ANT | NUMBER(12) | N |  |  |
| 7 | IDENT_CUSTO_ANT | NUMBER(12) | Y |  |  |
| 8 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 9 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | ID_X189 | NUMBER(38) | Y |  |  |

---

## X18_PROD_EMBALAG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_MOVTO | DATE | N |  |  |
| 5 | IDENT_EMBALAGEM | NUMBER(12) | N |  |  |
| 6 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 7 | DESCRICAO_COMPL | VARCHAR2(50) | Y |  |  |
| 8 | QTD_USADA | NUMBER(17,6) | Y |  |  |
| 9 | PERC_PERDA | NUMBER(7,4) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | DAT_FIM | DATE | Y |  |  |
| 13 | QTD_MAX_UTILIZADA | NUMBER(17,6) | Y |  |  |
| 14 | COD_FASE_PRODUCAO | VARCHAR2(20) | Y |  |  |
| 15 | DAT_VALID_INI | DATE | Y |  |  |
| 16 | TPO_VARIACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, IDENT_EMBALAGEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO → X16_PROD_ACABADO(COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO)
- IDENT_EMBALAGEM → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI → DWT_FASE_PRODUCAO(COD_EMPRESA, COD_ESTAB, COD_FASE_PRODUCAO, DAT_VALID_INI)

---

## X190_DOC_ENERG_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_CLASSE_CONSUMO | NUMBER(12) | N |  |  |
| 9 | DATA_DOCTO | DATE | N |  |  |
| 10 | QTD_DOCTOS | NUMBER(15) | Y |  |  |
| 11 | QTD_DOCTOS_CANC | NUMBER(15) | Y |  |  |
| 12 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 13 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 14 | QTD_CONSUMO_TOTAL | NUMBER(15) | Y |  |  |
| 15 | VLR_FORNECIMENTO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_SERV_N_TRIB | NUMBER(17,2) | Y |  |  |
| 17 | VLR_COBR_TERCEIRO | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DESP_ACS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 27 | IDENT_SCP | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

---

## X191_ITM_ENERG_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_CLASSE_CONSUMO | NUMBER(12) | N |  |  |
| 9 | DATA_DOCTO | DATE | N |  |  |
| 10 | DISCRI_ITEM | VARCHAR2(76) | N |  |  |
| 11 | VLR_TOTAL_ITEM | NUMBER(17,2) | Y |  |  |
| 12 | COD_SIT_PIS | NUMBER(2) | N |  |  |
| 13 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ALIQ_PIS | NUMBER(8,4) | N |  |  |
| 15 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 16 | COD_SIT_COFINS | NUMBER(2) | N |  |  |
| 17 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ALIQ_COFINS | NUMBER(8,4) | N |  |  |
| 19 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 20 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO → X190_DOC_ENERG_CONS(COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

**Indexes**:
- UK_X191_ITM_COFINS (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO, COD_SIT_COFINS, VLR_ALIQ_COFINS, IDENT_CONTA)
- UK_X191_ITM_PIS (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_ESTADO, COD_MUNICIPIO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_CLASSE_CONSUMO, DATA_DOCTO, COD_SIT_PIS, VLR_ALIQ_PIS, IDENT_CONTA)

---

## X192_ITENS_MERC_REF

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
| 12 | IND_TIPO_REF | CHAR(1) | N |  |  |
| 13 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 15 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 16 | DATA_FISCAL_REF | DATE | Y |  |  |
| 17 | IDENT_FIS_JUR_REF | NUMBER(12) | Y |  |  |
| 18 | NUM_ITEM_REF | NUMBER(5) | N |  |  |
| 19 | QTD_DEVOL | NUMBER(17,6) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 22 | NUM_AUTENTIC_NFE_REF | VARCHAR2(80) | Y |  |  |
| 23 | NUM_CNPJ_NFE_REF | VARCHAR2(14) | Y |  |  |
| 24 | IDENT_CAIXA_ECF_REF | NUMBER(12) | Y |  |  |
| 25 | NUM_COO_REF | VARCHAR2(9) | Y |  |  |
| 26 | DATA_EMISSAO_REF | DATE | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- IDENT_CAIXA_ECF_REF → X2087_EQUIPAMENTO_ECF(IDENT_CAIXA_ECF)

**Indexes**:
- IX_X192_ITENS_MERC_REF_002: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, IND_TIPO_REF, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, DATA_FISCAL_REF, IDENT_FIS_JUR_REF, NUM_ITEM_REF)
- IX_X192_ITENS_MERC_REF_003: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- IX_X192_ITENS_MERC_REF_004: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL_REF, IND_TIPO_REF)
- UK_X192_ITENS_MERC_REF_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, IND_TIPO_REF, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, DATA_FISCAL_REF, IDENT_FIS_JUR_REF, NUM_ITEM_REF, NUM_AUTENTIC_NFE_REF, NUM_CNPJ_NFE_REF, IDENT_CAIXA_ECF_REF, NUM_COO_REF, DATA_EMISSAO_REF)

---

## X194_ITENS_REF

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
| 12 | DATA_FISCAL_REF | DATE | N |  |  |
| 13 | MOVTO_E_S_REF | CHAR(1) | N |  |  |
| 14 | NORM_DEV_REF | CHAR(1) | N |  |  |
| 15 | IDENT_DOCTO_REF | NUMBER(12) | N |  |  |
| 16 | IDENT_FIS_JUR_REF | NUMBER(12) | N |  |  |
| 17 | NUM_DOCFIS_REF | VARCHAR2(12) | N |  |  |
| 18 | SERIE_DOCFIS_REF | VARCHAR2(3) | N |  |  |
| 19 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | N |  |  |
| 20 | IDENT_PRODUTO_REF | NUMBER(12) | N |  |  |
| 21 | IDENT_UND_PADRAO_REF | NUMBER(12) | N |  |  |
| 22 | NUM_ITEM_REF | NUMBER(5) | N |  |  |
| 23 | QTD_INSUMO | NUMBER(17,6) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, DATA_FISCAL_REF, MOVTO_E_S_REF, NORM_DEV_REF, IDENT_DOCTO_REF, IDENT_FIS_JUR_REF, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, IDENT_PRODUTO_REF, IDENT_UND_PADRAO_REF, NUM_ITEM_REF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- IDENT_DOCTO_REF → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR_REF → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO_REF → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_UND_PADRAO_REF → X2017_UND_PADRAO(IDENT_UND_PADRAO)

**Indexes**:
- IX_FK_SAF_2646: (IDENT_FIS_JUR_REF)

---

## X195_INF_COMPL_IN698

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | NUMBER(4) | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | VLR_POUP_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 6 | VLR_POUP_ANO_REF | NUMBER(17,2) | Y |  |  |
| 7 | VLR_POUP_REND | NUMBER(17,2) | Y |  |  |
| 8 | VLR_LUCRO_DIV_REND | NUMBER(17,2) | Y |  |  |
| 9 | VLR_DEMAIS_REND_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DEMAIS_REND_ANO_REF | NUMBER(17,2) | Y |  |  |
| 11 | VLR_DEMAIS_REND_R | NUMBER(17,2) | Y |  |  |
| 12 | VLR_FUND_INV_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 13 | VLR_FUND_INV_ANO_REF | NUMBER(17,2) | Y |  |  |
| 14 | VLR_FUND_INV_ANO_REND | NUMBER(17,2) | Y |  |  |
| 15 | VLR_REND_FIXA_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 16 | VLR_REND_FIXA_ANO_REF | NUMBER(17,2) | Y |  |  |
| 17 | VLR_REND_FIXA_ANO_REND | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TIT_CAP_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TIT_CAP_ANO_REF | NUMBER(17,2) | Y |  |  |
| 20 | VLR_TIT_CAP_ANO_REND | NUMBER(17,2) | Y |  |  |
| 21 | VLR_JCP_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 22 | VLR_JCP_ANO_REF | NUMBER(17,2) | Y |  |  |
| 23 | VLR_JCP_ANO_REND | NUMBER(17,2) | Y |  |  |
| 24 | VLR_SWAP_REND | NUMBER(17,2) | Y |  |  |
| 25 | VLR_PREV_REND | NUMBER(17,2) | Y |  |  |
| 26 | VLR_DEMAIS_REND_EXC_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 27 | VLR_DEMAIS_REND_EXC_ANO_REF | NUMBER(17,2) | Y |  |  |
| 28 | VLR_DEMAIS_REND_EXC_ANO_REND | NUMBER(17,2) | Y |  |  |
| 29 | VLR_DEP_CC_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 30 | VLR_DEP_CC_ANO_REF | NUMBER(17,2) | Y |  |  |
| 31 | VLR_PREMIOS_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 32 | VLR_PREMIOS_ANO_REF | NUMBER(17,2) | Y |  |  |
| 33 | VLR_FUNDOS_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 34 | VLR_FUNDOS_ANO_REF | NUMBER(17,2) | Y |  |  |
| 35 | VLR_DEMAIS_CRED_ANO_ANT | NUMBER(17,2) | Y |  |  |
| 36 | VLR_DEMAIS_CRED_ANO_REF | NUMBER(17,2) | Y |  |  |
| 37 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 38 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, IDENT_FIS_JUR

---

## X196_CONTAB_ANALITICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(38) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_OPERACAO | DATE | N |  |  |
| 5 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 6 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 7 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 8 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 9 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 10 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 13 | NUM_ITEM | NUMBER(5) | N |  |  |
| 14 | DATA_FISCAL | DATE | N |  |  |
| 15 | DATA_EMISSAO | DATE | N |  |  |
| 16 | DATA_MOVTO | DATE | N |  |  |
| 17 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 18 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 19 | MOVTO_E_S | CHAR(1) | N |  |  |
| 20 | NORM_DEV | CHAR(1) | N |  |  |
| 21 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 22 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 23 | COD_CLASS_DOC_FIS | CHAR(1) | N |  |  |
| 24 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 25 | SITUACAO | CHAR(1) | Y |  |  |
| 26 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 27 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 28 | IDENT_CONTRA_PART | NUMBER(12) | Y |  |  |
| 29 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 30 | IDENT_HISTPADRAO | NUMBER(12) | Y |  |  |
| 31 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 32 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 33 | TIPO_LANCTO | CHAR(1) | Y |  |  |
| 34 | COD_TP_DOC_LANCTO | VARCHAR2(3) | Y |  |  |
| 35 | CENTRO_LUCRO | VARCHAR2(20) | Y |  |  |
| 36 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 37 | COD_DDD | VARCHAR2(5) | Y |  |  |
| 38 | NUM_CELULAR | VARCHAR2(15) | Y |  |  |
| 39 | VLR_ATIVACAO | NUMBER(17,2) | Y |  |  |
| 40 | CICLO | VARCHAR2(7) | Y |  |  |
| 41 | DSC_ATRIBUICAO | VARCHAR2(255) | Y |  |  |
| 42 | MOT_AJUSTE | VARCHAR2(6) | Y |  |  |
| 43 | TIPO_SERVICO | VARCHAR2(35) | Y |  |  |
| 44 | DET_TIPO_SERVICO | VARCHAR2(35) | Y |  |  |
| 45 | COD_MERCADO | VARCHAR2(3) | Y |  |  |
| 46 | TIPO_ATIV_FINANC | VARCHAR2(6) | Y |  |  |
| 47 | TIPO_ITEM_NF | CHAR(1) | N |  |  |
| 48 | COD_BANCO | VARCHAR2(4) | Y |  |  |
| 49 | DSC_BANCO | VARCHAR2(50) | Y |  |  |
| 50 | TIPO_PAGTO | VARCHAR2(2) | Y |  |  |
| 51 | VLR_PAGTO | NUMBER(17,2) | Y |  |  |
| 52 | NUM_CLI_PAGTO | NUMBER(9) | Y |  |  |
| 53 | VLR_ATIVIDADE | NUMBER(17,2) | Y |  |  |
| 54 | NUM_FATURA | VARCHAR2(12) | Y |  |  |
| 55 | TIPO_ARRECADACAO | VARCHAR2(2) | Y |  |  |
| 56 | NUM_SEQ_ARQ | NUMBER(5) | Y |  |  |
| 57 | NUM_SEQ_PAGTO | NUMBER(6) | Y |  |  |
| 58 | VLR_SALDO_ATUAL | NUMBER(17,2) | Y |  |  |
| 59 | COD_BARRAS | VARCHAR2(44) | Y |  |  |
| 60 | MEIO_ARRECADACAO | CHAR(1) | Y |  |  |
| 61 | DATA_BAIXA | DATE | Y |  |  |
| 62 | COD_ATIV_PAGTO | VARCHAR2(4) | Y |  |  |
| 63 | DSC_RESERVADO1 | VARCHAR2(128) | Y |  |  |
| 64 | DSC_RESERVADO2 | VARCHAR2(128) | Y |  |  |
| 65 | DSC_RESERVADO3 | VARCHAR2(128) | Y |  |  |
| 66 | DSC_RESERVADO4 | VARCHAR2(128) | Y |  |  |
| 67 | DSC_RESERVADO5 | VARCHAR2(128) | Y |  |  |
| 68 | DSC_RESERVADO6 | NUMBER(17,2) | Y |  |  |
| 69 | DSC_RESERVADO7 | NUMBER(17,2) | Y |  |  |
| 70 | DSC_RESERVADO8 | NUMBER(17,2) | Y |  |  |
| 71 | DSC_RESERVADO9 | NUMBER(17,2) | Y |  |  |
| 72 | DSC_RESERVADO10 | NUMBER(17,2) | Y |  |  |
| 73 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 74 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: ID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTRA_PART → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_HISTPADRAO → X2020_HIST_PADRAO(IDENT_HISTPADRAO)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- COD_PAIS → PAIS(COD_PAIS)

**Indexes**:
- IX_FK_SAF_2717: (IDENT_FIS_JUR)
- IX_X196_CTA: (IDENT_CONTA)
- IX_X196_CTA_PART: (IDENT_CONTRA_PART)
- UK_X196_CONTAB_ANALITICA (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_OPERACAO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM, DATA_FISCAL, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, MOVTO_E_S, NORM_DEV)

---

## X197_CONTRATOS_IMOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTRATO_IMOB | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | NUM_CONTRATO | VARCHAR2(6) | N |  |  |
| 5 | IND_TP_CONTRATO | CHAR(1) | N |  |  |
| 6 | DAT_CONTRATO | DATE | N |  |  |
| 7 | IDENT_UNID_IMOB | NUMBER(12) | N |  |  |
| 8 | IDENT_FIS_JUR_COMPR | NUMBER(12) | Y |  |  |
| 9 | IDENT_FIS_JUR_VEND | NUMBER(12) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_CONTRATO_IMOB

**FKs**:
- IDENT_UNID_IMOB → X2054_UNID_IMOB(IDENT_UNID_IMOB)
- IDENT_FIS_JUR_COMPR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_VEND → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_CONTRATOS_IMOB (UNIQUE): (COD_EMPRESA, COD_ESTAB, NUM_CONTRATO, IDENT_FIS_JUR_COMPR, IDENT_FIS_JUR_VEND)
- IX_FK_SAF_2701: (IDENT_FIS_JUR_COMPR)
- IX_FK_SAF_2702: (IDENT_FIS_JUR_VEND)

---

## X198_MOV_IMOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTRATO_IMOB | NUMBER(12) | N |  |  |
| 2 | IDENT_MOV_IMOB | NUMBER(12) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DAT_OPERACAO | DATE | N |  |  |
| 6 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 7 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_IMPOSTO_RET | NUMBER(17,2) | Y |  |  |
| 9 | VLR_PAGO_ANO | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | IDENT_FIS_JUR_COMPR | NUMBER(12) | Y |  |  |
| 13 | IDENT_FIS_JUR_VEND | NUMBER(12) | Y |  |  |

**PK**: IDENT_CONTRATO_IMOB, IDENT_MOV_IMOB

**FKs**:
- IDENT_FIS_JUR_COMPR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_VEND → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_2704I: (IDENT_FIS_JUR_COMPR)
- IX_FK_SAF_2705I: (IDENT_FIS_JUR_VEND)
- IX_X198_MOV_IMOB (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_CONTRATO_IMOB, DAT_OPERACAO, IDENT_FIS_JUR_COMPR, IDENT_FIS_JUR_VEND)

---

## X19_DARF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_DARF | NUMBER(12) | N |  |  |
| 4 | DATA_VENCTO | DATE | N |  |  |
| 5 | DATA_INI | DATE | Y |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | DATA_PAGTO | DATE | Y |  |  |
| 8 | VLR_RECEITA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_CORRECAO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 11 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 13 | NUM_REFERENCIA | VARCHAR2(12) | Y |  |  |
| 14 | NUM_PROCESSO_BASE | VARCHAR2(12) | Y |  |  |
| 15 | VLR_BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 16 | ALIQ_INCIDENCIA | NUMBER(7,4) | Y |  |  |
| 17 | OBS_DARF | VARCHAR2(45) | Y |  |  |
| 18 | BANCO | VARCHAR2(3) | Y |  |  |
| 19 | AGENCIA | VARCHAR2(5) | Y |  |  |
| 20 | DATA_ARRECADACAO | DATE | Y |  |  |
| 21 | NUM_PAGAMENTO | VARCHAR2(12) | Y |  |  |
| 22 | EXERCICIO | NUMBER(4) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_DARF, DATA_VENCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DARF → X2019_COD_DARF(IDENT_DARF)

---

## X2001_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_OPERACAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_OPERACAO | VARCHAR2(9) | Y |  |  |
| 3 | COD_OPERACAO | VARCHAR2(6) | Y |  |  |
| 4 | VALID_OPERACAO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | IND_IPI_EST_CRED | CHAR(1) | Y |  |  |
| 9 | IND_ICMS_EST_CRED | CHAR(1) | Y |  |  |
| 10 | IND_TP_OP | CHAR(1) | Y |  |  |

**PK**: IDENT_OPERACAO

**FKs**:
- GRUPO_OPERACAO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_OPERACAO (UNIQUE): (GRUPO_OPERACAO, COD_OPERACAO, VALID_OPERACAO)

---

## X2002_AGRUP_CONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_AGRUP | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(6) | N |  |  |
| 3 | COD_PRT | VARCHAR2(10) | N |  |  |
| 4 | COD_AGRUP | VARCHAR2(10) | N |  |  |
| 5 | NUM_ORDEM | NUMBER(6) | N |  |  |
| 6 | DESCRICAO | VARCHAR2(80) | Y |  |  |
| 7 | TP_COMPORTAMENTO | VARCHAR2(20) | Y |  |  |
| 8 | IND_BASE_IR | VARCHAR2(20) | Y |  |  |
| 9 | IND_BASE_PC | VARCHAR2(20) | Y |  |  |

**PK**: IDENT_AGRUP

**Indexes**:
- IX_X2002_AGRUP_CONTAS (UNIQUE): (COD_EMPRESA, COD_PRT, COD_AGRUP, NUM_ORDEM)

---

## X2002_CONTROL_EXCL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  | COD_LEDGER_ACCOUNT - TAX BR |
| 3 | VALID_CONTA | DATE | N |  | DAT_INSERT_UPDATE - TAX BR |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  | DSC_LEDGER_ACCOUNT - TAX BR |
| 5 | IND_NATUREZA | CHAR(1) | Y |  | IND_LEDGER_ACCT_NAT_TYPE - TAX BR |
| 6 | IND_CONTA | CHAR(1) | Y |  | IND_LEDGER_ACCOUNT_TYPE - TAX BR |
| 7 | NIVEL | VARCHAR2(5) | Y |  | NUM_LEDGER_ACCT_LEVEL - TAX BR |

**PK**: GRUPO_CONTA, COD_CONTA, VALID_CONTA

---

## X2002_PLANO_CONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 2 | GRUPO_CONTA | VARCHAR2(9) | Y |  |  |
| 3 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 4 | VALID_CONTA | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IND_CONTA | CHAR(1) | Y |  |  |
| 7 | COD_CONTA_REDUZ | VARCHAR2(10) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | IDENT_CONTA_SINT | NUMBER(12) | Y |  |  |
| 11 | IND_NATUREZA | CHAR(1) | Y |  | 0 - Compensação;1 - Ativo; 2 - Passivo; 3 - Despesa; 4 - Receita; 5 - Mutações Ativas; 6 - Mutações Passivas; 7 - Patrimonio Liquido; 8 - Custo; 9 - Outros |
| 12 | NIVEL | VARCHAR2(5) | Y |  | Nivel da conta |
| 13 | IND_LANCTO_GLOBAL | CHAR(1) | Y | 'N' | Indica se a conta recebe lançamentos globais ou não |
| 14 | IDENT_CONTA_ANL_TOT | NUMBER(12) | Y |  | Código da Conta Analítica Totalizadora - IN86 (atendimento SINCO - SAFR102) |
| 15 | COD_CONTA_PADRAO | VARCHAR2(70) | Y |  | ATO COTEPE 70 - reg I050: Código do grupo de conta de acordo com o plano de contas padrão da Receita Federal. |
| 16 | IDENT_CUSTO | NUMBER(12) | Y |  | Sped contábil |
| 17 | IND_SITUACAO | CHAR(1) | Y | 'A' |  A - ativo; I - inativo |
| 18 | IND_CONTA_CONSOLID | CHAR(1) | Y |  |  |
| 19 | DESC_DETALHADA | VARCHAR2(600) | Y |  |  |

**PK**: IDENT_CONTA

**FKs**:
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- GRUPO_CONTA → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_CONTA (UNIQUE): (GRUPO_CONTA, COD_CONTA, VALID_CONTA)
- IX_CONTA: (COD_CONTA)
- IX_CONTA_REDUZ: (GRUPO_CONTA, COD_CONTA, COD_CONTA_REDUZ, VALID_CONTA)
- IX_CONTA_SINT: (IDENT_CONTA_SINT)
- IX_X2002_SPEDC: (GRUPO_CONTA, COD_CONTA, VALID_CONTA, IDENT_CONTA_SINT)
- X2002_PLANO_CONTAS_ASJ: (IDENT_CONTA, IDENT_CONTA_SINT)

---

## X2002_RECUPERA_CONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(6) | N |  |  |
| 2 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 3 | IDENT_AGRUP | NUMBER(12) | N |  |  |
| 4 | IND_RECUPERA_VALOR | CHAR(1) | Y |  |  |
| 5 | IND_EXCECAO_BC | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_CONTA, IDENT_AGRUP

**FKs**:
- IDENT_AGRUP → X2002_AGRUP_CONTAS(IDENT_AGRUP)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

---

## X2003_CENTRO_CUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 2 | GRUPO_CUSTO | VARCHAR2(9) | Y |  |  |
| 3 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 4 | VALID_CUSTO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | IND_CTRL_INVEST | CHAR(1) | Y |  |  |
| 9 | COD_CUSTO_SPED | VARCHAR2(28) | Y |  |  |

**PK**: IDENT_CUSTO

**FKs**:
- GRUPO_CUSTO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_CUSTO (UNIQUE): (GRUPO_CUSTO, COD_CUSTO, VALID_CUSTO)

---

## X2004_CENTRO_DESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DESPESA | NUMBER(12) | N |  |  |
| 2 | GRUPO_DESPESA | VARCHAR2(9) | Y |  |  |
| 3 | COD_DESPESA | VARCHAR2(20) | Y |  |  |
| 4 | VALID_DESPESA | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_DESPESA

**FKs**:
- GRUPO_DESPESA → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_DESP (UNIQUE): (GRUPO_DESPESA, COD_DESPESA, VALID_DESPESA)

---

## X2005_TIPO_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 2 | GRUPO_DOCTO | VARCHAR2(9) | Y |  |  |
| 3 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 4 | VALID_DOCTO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IND_DOCTO_FISCAL | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | OBS_CANCEL_P2 | VARCHAR2(32) | Y |  |  |
| 10 | IND_CLASS_OBRIG | CHAR(1) | Y | 0 | Esta sendo usado para DIEF-CE, a fim de diferenciar através do tipo de DF NF e NF de Fatura e informar corretamente no meio magnético o modelo correto |
| 11 | IND_NF_ELETRONICA | CHAR(1) | Y | 'N' | indicador de tipo de documento para nota fiscal eletronica de servico ISSQN |

**PK**: IDENT_DOCTO

**FKs**:
- GRUPO_DOCTO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_DOCTO (UNIQUE): (GRUPO_DOCTO, COD_DOCTO, VALID_DOCTO)
- IX_X2005_TIPO_DOCTO: (COD_DOCTO)

---

## X2006_NATUREZA_OP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |
| 2 | GRUPO_NATUREZA_OP | VARCHAR2(9) | Y |  |  |
| 3 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 4 | VALID_NATUREZA_OP | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | ENT_SAI | VARCHAR2(1) | Y |  |  |
| 9 | IND_FIS_JUR | VARCHAR2(1) | Y |  |  |
| 10 | COD_NATUREZA_OP_SPED | VARCHAR2(10) | Y |  |  |

**PK**: IDENT_NATUREZA_OP

**FKs**:
- GRUPO_NATUREZA_OP → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_OP (UNIQUE): (GRUPO_NATUREZA_OP, COD_NATUREZA_OP, VALID_NATUREZA_OP)
- IX_X2006_GRP_VALID: (GRUPO_NATUREZA_OP, VALID_NATUREZA_OP)
- IX_X2006_NAT_OP: (COD_NATUREZA_OP)

---

## X2007_MEDIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_MEDIDA | NUMBER(12) | N |  |  |
| 2 | GRUPO_MEDIDA | VARCHAR2(9) | Y |  |  |
| 3 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 4 | VALID_MEDIDA | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | IND_UNID_FRAC | CHAR(1) | Y |  |  |

**PK**: IDENT_MEDIDA

**FKs**:
- GRUPO_MEDIDA → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_MEDIDA (UNIQUE): (GRUPO_MEDIDA, COD_MEDIDA, VALID_MEDIDA)

---

## X2008_LEGENDA_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_LEGENDA | NUMBER(12) | N |  |  |
| 2 | GRUPO_LEGENDA | VARCHAR2(9) | Y |  |  |
| 3 | COD_LEGENDA | VARCHAR2(5) | Y |  |  |
| 4 | VALID_LEGENDA | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_LEGENDA

**Indexes**:
- IX_X2008_LEGEN_PRD (UNIQUE): (GRUPO_LEGENDA, COD_LEGENDA, VALID_LEGENDA)

---

## X2009_OBSERVACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_OBSERVACAO | VARCHAR2(9) | Y |  |  |
| 3 | COD_OBSERVACAO | VARCHAR2(8) | Y |  |  |
| 4 | VALID_OBSERVACAO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(500) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | TIPO_OBSERVACAO | NUMBER(1) | Y | 1 | Informar o código da observação. Deverão ser codificadas todas as observações a serem utilizadas nas Informações Complementares dos documentos fiscais e também as observações dos lançamentos fiscais. 1 - Informação Complementar 2 - Lançamento Fiscal |
| 9 | COD_OBS_LEI_5005 | VARCHAR2(25) | Y |  |  |
| 10 | IDENT_CFO | NUMBER(12) | Y |  |  |

**PK**: IDENT_OBSERVACAO

**FKs**:
- GRUPO_OBSERVACAO → GRUPO_ESTAB(GRUPO_ESTAB)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

**Indexes**:
- IX_CHAVE_OBS (UNIQUE): (GRUPO_OBSERVACAO, COD_OBSERVACAO, VALID_OBSERVACAO)
- IX_X2009_COD_OBS: (COD_OBSERVACAO)

---

## X2010_NAT_ESTOQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NAT_ESTOQUE | NUMBER(12) | N |  |  |
| 2 | GRUPO_NAT_ESTOQUE | VARCHAR2(9) | Y |  |  |
| 3 | COD_NAT_ESTOQUE | VARCHAR2(2) | Y |  |  |
| 4 | VALID_NAT_ESTOQUE | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_NAT_ESTOQUE

**FKs**:
- GRUPO_NAT_ESTOQUE → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_ESTOQUE (UNIQUE): (GRUPO_NAT_ESTOQUE, COD_NAT_ESTOQUE, VALID_NAT_ESTOQUE)

---

## X2011_SIT_BEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SIT_BEM | NUMBER(12) | N |  |  |
| 2 | GRUPO_SIT_BEM | VARCHAR2(9) | Y |  |  |
| 3 | COD_SIT_BEM | VARCHAR2(3) | Y |  |  |
| 4 | VALID_SIT_BEM | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | IND_NAT_BEM | CHAR(1) | Y |  |  |

**PK**: IDENT_SIT_BEM

**FKs**:
- GRUPO_SIT_BEM → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_SIT_BEM (UNIQUE): (GRUPO_SIT_BEM, COD_SIT_BEM, VALID_SIT_BEM)

---

## X2012_COD_FISCAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CFO | NUMBER(12) | N |  |  |
| 2 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 3 | VALID_CFO | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | IND_AGREGADOR | CHAR(1) | Y |  |  |
| 6 | IDENT_CFO_AGREG | NUMBER(12) | Y |  |  |
| 7 | IDENT_CFO_RELAC | NUMBER(12) | Y |  |  |
| 8 | IDENT_NAT_DIPI | NUMBER(12) | Y |  |  |
| 9 | IND_DETALHE_CFO | CHAR(1) | Y |  |  |
| 10 | IND_OPERACAO | CHAR(1) | Y |  |  |
| 11 | IND_MERCADO | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | IND_IPI_EST_CRED | CHAR(1) | Y |  |  |
| 15 | IND_ICMS_EST_CRED | CHAR(1) | Y |  |  |
| 16 | IND_DRBK | CHAR(1) | Y |  |  |

**PK**: IDENT_CFO

**FKs**:
- IDENT_CFO_AGREG → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_CFO_RELAC → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NAT_DIPI → X2084_NAT_DIPI(IDENT_NAT_DIPI)

**Indexes**:
- IX_CHN_COD_FISCAL (UNIQUE): (COD_CFO, VALID_CFO)
- IX_X2012_COD_FISC: (COD_CFO)
- IX_X2012_COD_FISCAL_02: (IDENT_CFO, COD_CFO)

---

## X2013_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 3 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 4 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 5 | VALID_PRODUTO | DATE | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 7 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 8 | IND_REGIDO_SUBST | CHAR(1) | Y |  |  |
| 9 | IND_CONTROLE_SELO | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | IDENT_NCM | NUMBER(12) | Y |  |  |
| 13 | IDENT_NALADI | NUMBER(12) | Y |  |  |
| 14 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 15 | IDENT_GRUPO_PROD | NUMBER(12) | Y |  |  |
| 16 | IND_FUNRURAL | CHAR(1) | Y |  |  |
| 17 | IND_PETR_ENERG | CHAR(1) | Y |  |  |
| 18 | IND_PRD_INCENTIV | CHAR(1) | Y |  |  |
| 19 | IND_ICMS_DIFERIDO | CHAR(1) | Y |  |  |
| 20 | COD_GRP_INCENT | VARCHAR2(5) | Y |  |  |
| 21 | COD_GRUPO_ST | VARCHAR2(2) | Y |  |  |
| 22 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 23 | IND_INCID_ICMS_SER | CHAR(1) | Y |  |  |
| 24 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 25 | VLR_PESO_UNIT_KG | NUMBER(13,4) | Y |  |  |
| 26 | DESCR_DETALHADA | VARCHAR2(250) | Y |  |  |
| 27 | IND_FABRIC_ESTAB | CHAR(1) | Y |  |  |
| 28 | FATOR_CONVERSAO | NUMBER(17,6) | Y |  |  |
| 29 | IND_CLASSIF_ICMSS | CHAR(1) | Y |  |  |
| 30 | DSC_MODELO | VARCHAR2(80) | Y |  |  |
| 31 | ORIGEM | CHAR(1) | Y |  |  |
| 32 | IDENT_GRP_PROD | NUMBER(12) | Y |  |  |
| 33 | IND_INCID_PIS | CHAR(1) | Y |  |  |
| 34 | ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 35 | IND_INCID_COFINS | CHAR(1) | Y |  |  |
| 36 | ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 37 | CAPAC_VOLUM | NUMBER(5) | Y |  |  |
| 38 | ESPECIE_DNF | NUMBER(3) | Y |  |  |
| 39 | CLAS_ITEM | NUMBER(2) | Y |  | 00-Mercadoria para Revenda 01-Matéria Prima 03-Produto em Processo 04-Produto Acabado 05-Subproduto 06-Produto Intermediário 07-Material de Uso/Consumo 08-Ativo Imobilizado 09-Serviços 10-Outros Insumos 99-Outros |
| 40 | COD_BARRAS | VARCHAR2(60) | Y |  |  |
| 41 | COD_ANP | NUMBER(12) | Y |  |  |
| 42 | IND_ANT_PROD | CHAR(1) | Y |  |  |
| 43 | COD_ANT_ITEM | VARCHAR2(60) | Y |  |  |
| 44 | DAT_ALT_CODIGO | DATE | Y |  |  |
| 45 | CLAS_ENQUAD_IPI | VARCHAR2(5) | Y |  | CLASSE DE ENQUADRAMENTO DO IPI |
| 46 | MATERIAL_RESULT_PERDA | CHAR(1) | Y |  |  |
| 47 | DSC_FINALIDADE | VARCHAR2(255) | Y |  |  |
| 48 | QTD_CAP_MAX_ARMAZ | NUMBER(17,6) | Y |  |  |
| 49 | IND_ATIVO_SAICS | CHAR(1) | Y |  |  |
| 50 | IND_TAB_INCIDENCIA | VARCHAR2(2) | Y |  | Indicador da Natureza de Frete: 0 – Operacoes de vendas, com onus suportado pelo estabelecimento vendedor, 1 – Operacoes de vendas, com onus suportado pelo adquirente, 2 – Operacoes de compras (bens para revenda, materias primas e outros produtos, geradores de credito, 3 – Operacoes de compras (bens para revenda, materias primas e outros produtos, nao geradores de credito, 4 – Transferencia de produtos acabados entre estabelecimentos da pessoa juridica, 5 – Transferencia de produtos em elaboracao entre estabelecimentos da pessoa juridica, 9 – Outros |
| 51 | COD_GRUPO | VARCHAR2(2) | Y |  |  |
| 52 | MARCA_COMERCIAL | VARCHAR2(60) | Y |  |  |
| 53 | IND_CARAC_PRODUTO | VARCHAR2(1) | Y |  |  |
| 54 | COD_CEST | VARCHAR2(7) | Y |  |  |
| 55 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 56 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 57 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 58 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 59 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 60 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 61 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 62 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 63 | IND_INC_RICMS_PR | VARCHAR2(1) | Y | 'N' |  |

**PK**: IDENT_PRODUTO

**FKs**:
- GRUPO_PRODUTO → GRUPO_ESTAB(GRUPO_ESTAB)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_NBM, IDENT_NCM → CLASSIF_NBM_NCM(IDENT_NBM, IDENT_NCM)
- IDENT_NBM, IDENT_NALADI → CLASSIF_NBM_NALADI(IDENT_NBM, IDENT_NALADI)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_GRUPO_PROD → GRUPO_PRODUTO(IDENT_GRUPO_PROD)
- COD_GRUPO_ST → DWT_GRUPO_ST(COD_GRUPO_ST)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- IDENT_GRP_PROD → X58_SE_DIC_GRP_PRD(IDENT_GRP_PROD)

**Indexes**:
- IX_AMBEV_PRODUTO_SAP: (DSC_RESERVADO4)
- IX_CHN_PRODUTO (UNIQUE): (GRUPO_PRODUTO, COD_PRODUTO, VALID_PRODUTO, IND_PRODUTO)
- IX_X2013_PRODUTO: (IND_PRODUTO, COD_PRODUTO)
- IX_X2013_PRODUTO1: (COD_PRODUTO)
- IX_X2013_PRODUTO2: (COD_CEST)
- IX_X2013_PRODUTO3: (IDENT_NBM)
- IX_X2013_PRODUTO_01: (IND_PRODUTO, COD_PRODUTO, GRUPO_PRODUTO, IDENT_PRODUTO)
- IX_X2013_PRODUTO_02: (SYS_NC00085$)
- IX_X2013_PRODUTO_CTA: (IDENT_CONTA)

---

## X2013_PROD_CPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 2 | UN_VENDA | VARCHAR2(8) | Y |  |  |
| 3 | FATOR_VENDA | NUMBER(10,3) | Y |  |  |
| 4 | TIPO_TRIBUTACAO_IPI | VARCHAR2(1) | Y |  |  |
| 5 | ALIQUOTA_IPI | NUMBER(5,2) | Y |  |  |
| 6 | VALOR_IPI | NUMBER(13,2) | Y |  |  |
| 7 | CATEGORIA_ICMS | VARCHAR2(14) | Y |  |  |
| 8 | TIPO_TRIBUTACAO_ISS | VARCHAR2(1) | Y |  |  |
| 9 | VALOR_UNIT_BASE_ISS | NUMBER(12,4) | Y |  |  |
| 10 | ALIQUOTA_ISS | NUMBER(5,2) | Y |  |  |
| 11 | CLASSIF_ISS | VARCHAR2(1) | Y |  |  |
| 12 | TAB_SUBST_TRIB | VARCHAR2(5) | Y |  |  |
| 13 | CODIGO_DCR | VARCHAR2(15) | Y |  |  |
| 14 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 15 | CUBAGEM | NUMBER(8,4) | Y |  |  |
| 16 | PESO_LIQUIDO | NUMBER(13,4) | Y |  |  |
| 17 | PESO_BRUTO | NUMBER(13,4) | Y |  |  |
| 18 | SUBST_TRIB_ENTRADA | VARCHAR2(1) | Y |  |  |
| 19 | IDENT_FEDERAL | NUMBER(12) | Y |  |  |
| 20 | CUSTO | NUMBER(17,2) | Y |  |  |
| 21 | PRECO_TRANSF | NUMBER(17,2) | Y |  |  |
| 22 | PRECO_VENDA | NUMBER(17,2) | Y |  |  |

**PK**: COD_PRODUTO

**FKs**:
- IDENT_FEDERAL → X2044_SIT_TRIB_FED(IDENT_FEDERAL)

---

## X2013_PROD_CSELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 2 | COD_GRUPO_SELO | NUMBER(2) | Y |  |  |
| 3 | COD_SUBGRUPO_SELO | NUMBER(2) | Y |  |  |
| 4 | COR_SELO | VARCHAR2(15) | Y |  |  |
| 5 | SERIE_SELO | VARCHAR2(3) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PRODUTO

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- COD_GRUPO_SELO → GRUPO_SELO(COD_GRUPO_SELO)
- COD_GRUPO_SELO, COD_SUBGRUPO_SELO → SUBGRUPO_SELO(COD_GRUPO_SELO, COD_SUBGRUPO_SELO)

---

## X2014_QUITACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_QUITACAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_QUITACAO | VARCHAR2(9) | Y |  |  |
| 3 | COD_QUITACAO | VARCHAR2(5) | Y |  |  |
| 4 | VALID_QUITACAO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_DIAS | NUMBER(3) | Y |  |  |
| 7 | VLR_TAXA_MES_ANO | NUMBER(7,4) | Y |  |  |
| 8 | IND_UTILIZ_MES_ANO | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_QUITACAO

**Indexes**:
- IX_CHAVE_QUITACAO (UNIQUE): (GRUPO_QUITACAO, COD_QUITACAO, VALID_QUITACAO)

---

## X2015_OPERACAO_OIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_OPER_OIL | NUMBER(12) | N |  |  |
| 2 | GRUPO_OPER_OIL | VARCHAR2(9) | Y |  |  |
| 3 | COD_OPER_OIL | VARCHAR2(10) | Y |  |  |
| 4 | VALID_OPER_OIL | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_OPER_OIL

**Indexes**:
- IX_CHAVE_OPERACAO_OIL (UNIQUE): (GRUPO_OPER_OIL, COD_OPER_OIL, VALID_OPER_OIL)

---

## X2016_PROJETO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PROJETO | NUMBER(12) | N |  |  |
| 2 | GRUPO_PROJETO | VARCHAR2(9) | Y |  |  |
| 3 | COD_PROJETO | VARCHAR2(20) | Y |  |  |
| 4 | VALID_PROJETO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 6 | DAT_INI | DATE | Y |  |  |
| 7 | DAT_FIM | DATE | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | VLR_TOT_PROJETO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SALDO_PROJETO | NUMBER(17,2) | Y |  |  |

**PK**: IDENT_PROJETO

**Indexes**:
- IX_CHAVE_PROJETO (UNIQUE): (GRUPO_PROJETO, COD_PROJETO, VALID_PROJETO)

---

## X2017_UND_PADRAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_UND_PADRAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_UND_PADRAO | VARCHAR2(9) | Y |  |  |
| 3 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 4 | VALID_UND_PADRAO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | IND_UNID_FRAC | CHAR(1) | Y |  |  |

**PK**: IDENT_UND_PADRAO

**FKs**:
- GRUPO_UND_PADRAO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_UND_PADRAO (UNIQUE): (GRUPO_UND_PADRAO, COD_UND_PADRAO, VALID_UND_PADRAO)

---

## X2018_SERVICOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 2 | GRUPO_SERVICO | VARCHAR2(9) | Y |  |  |
| 3 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 4 | VALID_SERVICO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | IND_TP_SERVICO | CHAR(1) | Y |  |  |
| 9 | IND_MAT_SERV | CHAR(1) | Y |  |  |
| 10 | CODIGO_CONTABIL | VARCHAR2(20) | Y |  |  |
| 11 | INSS | CHAR(1) | Y |  |  |
| 12 | ISS | CHAR(1) | Y |  |  |
| 13 | IRRF | CHAR(1) | Y |  |  |
| 14 | ALIQUOTA_INSS | NUMBER(8,4) | Y |  |  |
| 15 | ALIQUOTA_ISS | NUMBER(8,4) | Y |  |  |
| 16 | ALIQUOTA_IRRF | NUMBER(8,4) | Y |  |  |
| 17 | IND_CONTRATO | CHAR(1) | Y |  |  |
| 18 | IND_SERVICOS_TERC | CHAR(1) | Y |  |  |
| 19 | COD_NAT_SERV | VARCHAR2(35) | Y |  |  |
| 20 | DESC_NAT_SERV | VARCHAR2(30) | Y |  |  |
| 21 | VLR_ALIQ_INSC | NUMBER(7,4) | Y |  |  |
| 22 | VLR_ALIQ_S_INSC | NUMBER(7,4) | Y |  |  |
| 23 | VLR_PERC_FRETE_AUT | NUMBER(19,2) | Y |  |  |
| 24 | IDENT_SERV_LEI_116 | NUMBER(12) | Y |  | Ato Cotepe 70/05 - reg 0200: referente a tabela DWT_SERVICO_LEI_116 |
| 25 | IND_DEDUCAO | CHAR(1) | Y |  | 1-(40%)Serviço de recapeamento asfáltico e pavimentação; 2-(30%)Serviço de construção civil, obras hidráulicas, outras semelhantes e Serviço de construção de imóveis (notas emitidas a partir de 14/11/2000 - Decreto 18.698/00); 3-(25%)Serviço de Conservação de imóveis (notas emitidas até 13/11/2000); 4-(10%)Serviço de Terraplanagem; 5-SEM qualquer dedução; 6-COM dedução através de Mapas de Materiais e Subempreitadas;  |
| 26 | COD_ATIVIDADE | NUMBER(7) | Y |  |  |
| 27 | DAT_VALIDADE_INI_ATIVIDADE | DATE | Y |  |  |
| 28 | COD_NAT_SERV_SPED | VARCHAR2(60) | Y |  |  |
| 29 | DESC_NAT_SERV_SPED | VARCHAR2(100) | Y |  |  |

**PK**: IDENT_SERVICO

**FKs**:
- GRUPO_SERVICO → GRUPO_ESTAB(GRUPO_ESTAB)
- IDENT_SERV_LEI_116 → DWT_SERVICO_LEI_116(IDENT_SERV_LEI_116)
- COD_ATIVIDADE, DAT_VALIDADE_INI_ATIVIDADE → ATIV_ECONOMICA(COD_ATIVIDADE, DAT_VALIDADE_INI)

**Indexes**:
- IX_CHN_SERVICO (UNIQUE): (GRUPO_SERVICO, COD_SERVICO, VALID_SERVICO)
- IX_X2018_SERVICOS: (GRUPO_SERVICO, COD_NAT_SERV, VALID_SERVICO)

---

## X2019_COD_DARF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DARF | NUMBER(12) | N |  |  |
| 2 | GRUPO_DARF | VARCHAR2(9) | Y |  |  |
| 3 | COD_DARF | VARCHAR2(4) | Y |  |  |
| 4 | VALID_DARF | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(200) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | IND_INCID_DIRF | CHAR(1) | Y | 'N' |  |
| 9 | IND_INCID_REINF | CHAR(1) | Y |  |  |
| 10 | IND_CLASSIF_REINF | CHAR(1) | Y |  |  |
| 11 | IND_INCID_DCTF | VARCHAR2(1) | Y |  |  |

**PK**: IDENT_DARF

**FKs**:
- GRUPO_DARF → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_DARF (UNIQUE): (GRUPO_DARF, COD_DARF, VALID_DARF)

---

## X201_CAPA_CUPOM_CFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_EQUIP | NUMBER(9) | N |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 7 | IND_SITUACAO_CUPOM | VARCHAR2(2) | N |  |  |
| 8 | NOME_CLIENTE | VARCHAR2(60) | Y |  |  |
| 9 | CPF_CNPJ_CLIENTE | VARCHAR2(14) | Y |  |  |
| 10 | NUM_AUTENTIC_NFE | VARCHAR2(80) | N |  |  |
| 11 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DESC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ACRES | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOT_LIQ | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DESP_ACS | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 21 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 22 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

**Indexes**:
- IX_X201_CAPA_CUPOM_01: (COD_EMPRESA, COD_ESTAB, DATA_EMISSAO)

---

## X2020_HIST_PADRAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_HISTPADRAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_HISTPADRAO | VARCHAR2(9) | Y |  |  |
| 3 | COD_HISTPADRAO | VARCHAR2(6) | Y |  |  |
| 4 | VALID_HISTPADRAO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_HISTPADRAO

**FKs**:
- GRUPO_HISTPADRAO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_HIST_PAD (UNIQUE): (GRUPO_HISTPADRAO, COD_HISTPADRAO, VALID_HISTPADRAO)

---

## X2021_ALMOXARIFADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ALMOX | NUMBER(12) | N |  |  |
| 2 | GRUPO_ALMOX | VARCHAR2(9) | Y |  |  |
| 3 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 4 | VALID_ALMOX | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_ALMOX

**FKs**:
- GRUPO_ALMOX → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_ALMOX (UNIQUE): (GRUPO_ALMOX, COD_ALMOX, VALID_ALMOX)

---

## X2022_TIPO_MOVPATR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TIPO_MOVPATR | NUMBER(12) | N |  |  |
| 2 | GRUPO_TIPO_MOVPATR | VARCHAR2(9) | Y |  |  |
| 3 | COD_TIPO_MOVPATR | VARCHAR2(3) | Y |  |  |
| 4 | VALID_TIPO_MOVPATR | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IND_SINAL_MOVTO | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_TIPO_MOVPATR

**FKs**:
- GRUPO_TIPO_MOVPATR → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_TP_MOVPATR (UNIQUE): (GRUPO_TIPO_MOVPATR, COD_TIPO_MOVPATR, VALID_TIPO_MOVPATR)

---

## X2023_VERBAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 2 | GRUPO_VERBA | VARCHAR2(9) | Y |  |  |
| 3 | COD_VERBA | VARCHAR2(6) | Y |  |  |
| 4 | VALID_VERBA | DATE | Y |  |  |
| 5 | IND_VERBA | CHAR(1) | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 7 | INCID_RAIS | CHAR(1) | Y |  |  |
| 8 | INCID_DIRF | CHAR(1) | Y |  |  |
| 9 | TRIB_IR | CHAR(1) | Y |  |  |
| 10 | COMPOE_SAL | CHAR(1) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | IDENT_CONTA_CRED | NUMBER(12) | Y |  |  |
| 14 | IDENT_CONTA_DEB | NUMBER(12) | Y |  |  |
| 15 | IND_DECIMO_TERC | CHAR(1) | Y |  |  |
| 16 | INCID_INSS | CHAR(1) | Y |  |  |
| 17 | IND_IN86_IN89 | CHAR(1) | Y | 'S' |  |
| 18 | IND_PREV_SOCIAL | VARCHAR2(2) | Y |  |  |

**PK**: IDENT_VERBA

**FKs**:
- GRUPO_VERBA → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_VERBA (UNIQUE): (GRUPO_VERBA, COD_VERBA, VALID_VERBA)

---

## X2024_MODELO_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 2 | GRUPO_MODELO | VARCHAR2(9) | Y |  |  |
| 3 | COD_MODELO | VARCHAR2(2) | Y |  |  |
| 4 | VALID_MODELO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_MODELO

**FKs**:
- GRUPO_MODELO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_MODELO_DOC (UNIQUE): (GRUPO_MODELO, COD_MODELO, VALID_MODELO)
- IX_X2024_MODELO_DOCTO_01: (IDENT_MODELO, COD_MODELO)
- IX_X2024_MODELO_DOCTO_COD: (COD_MODELO)

---

## X2025_MARCA_COMERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_MARCA_COM | NUMBER(12) | N |  |  |
| 2 | GRUPO_MARCA_COM | VARCHAR2(9) | N |  |  |
| 3 | COD_MARCA_COM | NUMBER(6) | N |  |  |
| 4 | VALID_MARCA_COM | DATE | N |  |  |
| 5 | DSC_MARCA_COM | VARCHAR2(50) | Y |  |  |
| 6 | NUM_REGISTRO | VARCHAR2(15) | Y |  |  |
| 7 | DSC_CLASS_AMBIE | VARCHAR2(3) | Y |  |  |
| 8 | DSC_CLASS_TOXIC | VARCHAR2(3) | Y |  |  |
| 9 | IND_CLASSE_USO | VARCHAR2(2) | Y |  |  |
| 10 | DSC_OUTRAS | VARCHAR2(100) | Y |  |  |
| 11 | UF_REGISTRO | VARCHAR2(2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_MARCA_COM

**FKs**:
- GRUPO_MARCA_COM → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_MARCA_COMERC: (GRUPO_MARCA_COM, COD_MARCA_COM, VALID_MARCA_COM)

---

## X2027_TIPO_ADMIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ADMISSAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_ADMISSAO | VARCHAR2(9) | Y |  |  |
| 3 | COD_ADMISSAO | CHAR(1) | Y |  |  |
| 4 | VALID_ADMISSAO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_ADMISSAO

**FKs**:
- GRUPO_ADMISSAO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_TP_ADMISSAO (UNIQUE): (GRUPO_ADMISSAO, COD_ADMISSAO, VALID_ADMISSAO)

---

## X2028_CAUSA_DESLIG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAUSA_DESLIG | NUMBER(12) | N |  |  |
| 2 | GRUPO_CAUSA_DESLIG | VARCHAR2(9) | Y |  |  |
| 3 | COD_CAUSA_DESLIG | VARCHAR2(2) | Y |  |  |
| 4 | VALID_CAUSA_DESLIG | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_CAUSA_DESLIG

**FKs**:
- GRUPO_CAUSA_DESLIG → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_CAUSA_DESL (UNIQUE): (GRUPO_CAUSA_DESLIG, COD_CAUSA_DESLIG, VALID_CAUSA_DESLIG)

---

## X2029_COD_CBO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CBO | NUMBER(12) | N |  |  |
| 2 | GRUPO_CBO | VARCHAR2(9) | Y |  |  |
| 3 | COD_CBO | VARCHAR2(10) | Y |  |  |
| 4 | VALID_CBO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_CBO

**FKs**:
- GRUPO_CBO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_CBO (UNIQUE): (GRUPO_CBO, COD_CBO, VALID_CBO)

---

## X202_ITEM_CUPOM_CFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_EQUIP | NUMBER(9) | N |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | NUM_ITEM | NUMBER(5) | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 8 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 9 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 10 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 11 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 12 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 13 | QTDE | NUMBER(17,6) | Y |  |  |
| 14 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 15 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 16 | VLR_DESC | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ACRES | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TOT_LIQ | NUMBER(17,2) | Y |  |  |
| 19 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 22 | COD_SIT_TRIB_PIS | NUMBER(2) | Y |  |  |
| 23 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 24 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 25 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 28 | COD_SIT_TRIB_COFINS | NUMBER(2) | Y |  |  |
| 29 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 30 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 31 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 33 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 34 | VLR_BASE_PIS_ST | NUMBER(17,2) | Y |  |  |
| 35 | VLR_PIS_ST | NUMBER(17,2) | Y |  |  |
| 36 | VLR_ALIQ_PIS_ST | NUMBER(7,4) | Y |  |  |
| 37 | VLR_BASE_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 38 | VLR_COFINS_ST | NUMBER(17,2) | Y |  |  |
| 39 | VLR_ALIQ_COFINS_ST | NUMBER(7,4) | Y |  |  |
| 40 | VLR_DESP_ACS | NUMBER(17,2) | Y |  |  |
| 41 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 42 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 43 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 44 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 45 | VLR_EXC_BASE_PISCOFINS | NUMBER(17,2) | Y |  |  |
| 46 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO → X201_CAPA_CUPOM_CFE(COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- IX_FK_SAF_2734: (IDENT_OBSERVACAO)
- IX_X202_ITEM_CUPOM_CTA: (IDENT_CONTA)

---

## X2030_VINC_EMPREG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_VINCULO_EMP | NUMBER(12) | N |  |  |
| 2 | GRUPO_VINCULO_EMP | VARCHAR2(9) | Y |  |  |
| 3 | COD_VINCULO_EMP | VARCHAR2(2) | Y |  |  |
| 4 | VALID_VINCULO_EMP | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | IND_VINC_EMPREG | CHAR(1) | Y |  |  |

**PK**: IDENT_VINCULO_EMP

**FKs**:
- GRUPO_VINCULO_EMP → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_VINCULO_EMP (UNIQUE): (GRUPO_VINCULO_EMP, COD_VINCULO_EMP, VALID_VINCULO_EMP)

---

## X2031_TIPO_INSTR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_INSTRUCAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_INSTRUCAO | VARCHAR2(9) | Y |  |  |
| 3 | COD_INSTRUCAO | VARCHAR2(2) | Y |  |  |
| 4 | VALID_INSTRUCAO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_INSTRUCAO

**FKs**:
- GRUPO_INSTRUCAO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_TP_INST (UNIQUE): (GRUPO_INSTRUCAO, COD_INSTRUCAO, VALID_INSTRUCAO)

---

## X2032_TIPO_SALARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TIPO_SALARIO | NUMBER(12) | N |  |  |
| 2 | GRUPO_TIPO_SALARIO | VARCHAR2(9) | Y |  |  |
| 3 | COD_TIPO_SALARIO | CHAR(1) | Y |  |  |
| 4 | VALID_TIPO_SALARIO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_TIPO_SALARIO

**FKs**:
- GRUPO_TIPO_SALARIO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_TP_SALARIO (UNIQUE): (GRUPO_TIPO_SALARIO, COD_TIPO_SALARIO, VALID_TIPO_SALARIO)

---

## X2033_ESTADO_CIVIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO_CIVIL | NUMBER(12) | N |  |  |
| 2 | GRUPO_ESTADO_CIVIL | VARCHAR2(9) | Y |  |  |
| 3 | COD_ESTADO_CIVIL | CHAR(1) | Y |  |  |
| 4 | VALID_ESTADO_CIVIL | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_ESTADO_CIVIL

**FKs**:
- GRUPO_ESTADO_CIVIL → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_EST_CIVIL (UNIQUE): (GRUPO_ESTADO_CIVIL, COD_ESTADO_CIVIL, VALID_ESTADO_CIVIL)

---

## X2034_COD_OCORR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_OCORRENCIA | NUMBER(12) | N |  |  |
| 2 | GRUPO_OCORRENCIA | VARCHAR2(9) | Y |  |  |
| 3 | COD_OCORRENCIA | VARCHAR2(2) | Y |  |  |
| 4 | VALID_OCORRENCIA | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IDENT_MODULO | NUMBER(12) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_OCORRENCIA

**FKs**:
- GRUPO_OCORRENCIA → GRUPO_ESTAB(GRUPO_ESTAB)
- IDENT_MODULO → MODULO_FICHA_FUNC(IDENT_MODULO)

**Indexes**:
- IX_CHN_COD_OCORR (UNIQUE): (GRUPO_OCORRENCIA, COD_OCORRENCIA, VALID_OCORRENCIA)

---

## X2035_TP_DEPEND

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TIPO_DEPEND | NUMBER(12) | N |  |  |
| 2 | GRUPO_TIPO_DEPEND | VARCHAR2(9) | Y |  |  |
| 3 | COD_TIPO_DEPEND | VARCHAR2(2) | Y |  |  |
| 4 | VALID_TIPO_DEPEND | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | INCIDENCIA_IR | CHAR(1) | Y |  |  |
| 7 | INCIDENCIA_SF | CHAR(1) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_TIPO_DEPEND

**FKs**:
- GRUPO_TIPO_DEPEND → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_TP_DEPEND (UNIQUE): (GRUPO_TIPO_DEPEND, COD_TIPO_DEPEND, VALID_TIPO_DEPEND)

---

## X2036_FUNCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_FUNCAO | NUMBER(12) | N |  |  |
| 2 | GRUPO_FUNCAO | VARCHAR2(9) | Y |  |  |
| 3 | COD_FUNCAO | VARCHAR2(10) | Y |  |  |
| 4 | VALID_FUNCAO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_FUNCAO

**FKs**:
- GRUPO_FUNCAO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_FUNCAO (UNIQUE): (GRUPO_FUNCAO, COD_FUNCAO, VALID_FUNCAO)

---

## X2037_SETOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SETOR | NUMBER(12) | N |  |  |
| 2 | GRUPO_SETOR | VARCHAR2(9) | Y |  |  |
| 3 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 4 | VALID_SETOR | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IDENT_SETOR_SUP | NUMBER(12) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | VALID_FINAL | DATE | Y |  |  |
| 10 | TIPO_LOTACAO_TRIB | VARCHAR2(2) | Y |  |  |
| 11 | TIPO_INSC_LOTACAO | CHAR(1) | Y |  |  |
| 12 | NUM_INSC_LOTACAO | VARCHAR2(15) | Y |  |  |
| 13 | COD_FPAS | VARCHAR2(3) | Y |  |  |
| 14 | COD_TERCEIROS | VARCHAR2(4) | Y |  |  |
| 15 | COD_COMB_TERCEIROS | VARCHAR2(4) | Y |  |  |
| 16 | COD_TERCEIROS_PROCESSO | VARCHAR2(4) | Y |  |  |
| 17 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 18 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 19 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 20 | ALIQ_GILRAT | VARCHAR2(1) | Y |  |  |
| 21 | VLR_FAP | NUMBER(5,4) | Y |  |  |

**PK**: IDENT_SETOR

**FKs**:
- IDENT_SETOR_SUP → X2037_SETOR(IDENT_SETOR)
- GRUPO_SETOR → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHAVE_NAT_SETOR (UNIQUE): (GRUPO_SETOR, COD_SETOR, VALID_SETOR)

---

## X2037_SETOR_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_X2037_SETOR_HIST | NUMBER(12) | N |  |  |
| 2 | GRUPO_SETOR | VARCHAR2(9) | Y |  |  |
| 3 | COD_SETOR | VARCHAR2(10) | Y |  |  |
| 4 | VALID_SETOR | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IDENT_SETOR_SUP | NUMBER(12) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | VALID_FINAL | DATE | Y |  |  |
| 10 | TIPO_LOTACAO_TRIB | VARCHAR2(2) | Y |  |  |
| 11 | TIPO_INSC_LOTACAO | CHAR(1) | Y |  |  |
| 12 | NUM_INSC_LOTACAO | VARCHAR2(15) | Y |  |  |
| 13 | COD_FPAS | VARCHAR2(3) | Y |  |  |
| 14 | COD_TERCEIROS | VARCHAR2(4) | Y |  |  |
| 15 | COD_COMB_TERCEIROS | VARCHAR2(4) | Y |  |  |
| 16 | COD_TERCEIROS_PROCESSO | VARCHAR2(4) | Y |  |  |
| 17 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 18 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 19 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 20 | DAT_OCORRENCIA | DATE | Y |  |  |
| 21 | IND_STATUS | CHAR(1) | Y |  |  |
| 22 | IND_DELETE | CHAR(1) | Y |  |  |
| 23 | ALIQ_GILRAT | VARCHAR2(1) | Y |  |  |
| 24 | VLR_FAP | NUMBER(5,4) | Y |  |  |

**PK**: ID_X2037_SETOR_HIST

**Indexes**:
- UK_X2037_SETOR_HIST (UNIQUE): (GRUPO_SETOR, COD_SETOR, VALID_SETOR, DAT_OCORRENCIA)

---

## X203_LANCTOS_AJUSTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_X203 | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_OPERACAO | DATE | N |  |  |
| 5 | COD_SIT_TRIB_PIS | NUMBER(2) | N |  |  |
| 6 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 7 | COD_SIT_TRIB_COFINS | NUMBER(2) | N |  |  |
| 8 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 9 | COD_REC_DED_EXC | VARCHAR2(5) | N |  |  |
| 10 | COD_ATRIBUTO | VARCHAR2(3) | N | ' ' |  |
| 11 | COD_REC_DED_EXC_COMPL | VARCHAR2(20) | N |  |  |
| 12 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 13 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 14 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 15 | IND_AJUSTE | CHAR(1) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_X203

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X203_LANCTOS_AJUSTE (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_OPERACAO, COD_SIT_TRIB_PIS, COD_SIT_TRIB_COFINS, COD_REC_DED_EXC, COD_ATRIBUTO, COD_REC_DED_EXC_COMPL, COD_NAT_REC, IDENT_CONTA)
- IX_X203_LANCTOS_AJUSTE_CTA: (IDENT_CONTA)

---

## X2042_ESP_VOLUME

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_VOLUME | NUMBER(12) | N |  |  |
| 2 | GRUPO_VOLUME | VARCHAR2(9) | Y |  |  |
| 3 | COD_VOLUME | VARCHAR2(10) | Y |  |  |
| 4 | VALID_VOLUME | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_VOLUME

**FKs**:
- GRUPO_VOLUME → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_ESP_VOL (UNIQUE): (GRUPO_VOLUME, COD_VOLUME, VALID_VOLUME)

---

## X2043_COD_NBM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NBM | NUMBER(12) | N |  |  |
| 2 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 3 | VALID_NBM | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | IND_TRIB_NBM | CHAR(1) | Y |  |  |
| 6 | ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 7 | IDENT_NOTA_TIPI | NUMBER(12) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 11 | GRUPO_APURAC | VARCHAR2(5) | Y |  |  |
| 12 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 13 | IND_INCIDENCIA | CHAR(1) | Y |  |  |
| 14 | EX_IPI | VARCHAR2(3) | Y |  |  |

**PK**: IDENT_NBM

**FKs**:
- IDENT_NOTA_TIPI → NOTA_SECAO_TIPI(IDENT_NOTA_TIPI)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- IX_CHN_COD_NBM (UNIQUE): (COD_NBM, VALID_NBM)
- IX_X2043_COD_NBM2: (COD_NBM)
- UK_X2043_COD_NBM (UNIQUE): (COD_NBM, VALID_NBM, EX_IPI)

---

## X2044_SIT_TRIB_FED

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_FEDERAL | NUMBER(12) | N |  |  |
| 2 | GRUPO_FEDERAL | VARCHAR2(9) | Y |  |  |
| 3 | COD_FEDERAL | VARCHAR2(5) | Y |  |  |
| 4 | VALID_FEDERAL | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_FEDERAL

**FKs**:
- GRUPO_FEDERAL → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_SITTRIB_FED (UNIQUE): (GRUPO_FEDERAL, COD_FEDERAL, VALID_FEDERAL)

---

## X2045_COD_NCM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NCM | NUMBER(12) | N |  |  |
| 2 | COD_NCM | VARCHAR2(10) | Y |  |  |
| 3 | VALID_NCM | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | ALIQUOTA_NCM | NUMBER(7,4) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_NCM

**Indexes**:
- IX_CHN_COD_NCM (UNIQUE): (COD_NCM, VALID_NCM)

---

## X2047_VIA_TRANSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_VIA_TRANSP | NUMBER(12) | N |  |  |
| 2 | GRUPO_VIA_TRANSP | VARCHAR2(9) | Y |  |  |
| 3 | COD_VIA_TRANSPORTE | VARCHAR2(5) | Y |  |  |
| 4 | VALID_VIA_TRANSP | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | COD_VIA_TRANSP_SP | VARCHAR2(5) | Y |  |  |

**PK**: IDENT_VIA_TRANSP

**FKs**:
- GRUPO_VIA_TRANSP → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_VIA_TRANSP (UNIQUE): (GRUPO_VIA_TRANSP, COD_VIA_TRANSPORTE, VALID_VIA_TRANSP)

---

## X2048_SINDICATO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SINDICATO | NUMBER(12) | N |  |  |
| 2 | GRUPO_SINDICATO | VARCHAR2(9) | Y |  |  |
| 3 | COD_SINDICATO | VARCHAR2(5) | Y |  |  |
| 4 | VALID_SINDICATO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | MUNICIPIO | VARCHAR2(20) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | CNPJ_SINDICATO | VARCHAR2(14) | Y |  |  |

**PK**: IDENT_SINDICATO

**FKs**:
- GRUPO_SINDICATO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_SINDICATO (UNIQUE): (GRUPO_SINDICATO, COD_SINDICATO, VALID_SINDICATO)

---

## X2049_VEIC_TRANSP
**Comment**: Tabela de Códigos de Veículos de Transporte, criada no Ato Cotepe 70/05.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_VEIC_TRANSP | NUMBER(12) | N |  |  |
| 2 | GRUPO_VEIC_TRANSP | VARCHAR2(9) | Y |  |  |
| 3 | COD_VEIC_TRANSP | VARCHAR2(6) | Y |  |  |
| 4 | VALID_VEIC_TRANSP | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | MARCA_VEIC | VARCHAR2(30) | Y |  |  |
| 7 | MODELO_VEIC | VARCHAR2(30) | Y |  |  |
| 8 | ANO_VEIC | NUMBER(4) | Y |  |  |
| 9 | CERTIFICADO_VEIC | VARCHAR2(30) | Y |  |  |
| 10 | IDENT_UF_CERTIFICADO | NUMBER(12) | Y |  |  |
| 11 | PLACA_VEIC | VARCHAR2(17) | Y |  |  |
| 12 | IDENT_UF_PLACA | NUMBER(12) | Y |  |  |
| 13 | IND_VEIC_AQUAVIARIO | CHAR(1) | Y |  | 0 - Embarcacao , 1 - empurrador/rebocador |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_VEIC_TRANSP

**Indexes**:
- UK_VEIC_TRANSP (UNIQUE): (GRUPO_VEIC_TRANSP, COD_VEIC_TRANSP, VALID_VEIC_TRANSP)

---

## X204_FORMA_PAGTO_CFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_EQUIP | NUMBER(9) | N |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | IDENT_OPERACAO | NUMBER(12) | N |  |  |
| 7 | NUM_COMP_PAG | VARCHAR2(18) | N |  |  |
| 8 | IND_NAT_OPER | CHAR(1) | Y |  |  |
| 9 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 10 | CEP | NUMBER(8) | Y |  |  |
| 11 | NUM_PONTO_VENDA | VARCHAR2(8) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, IDENT_OPERACAO, NUM_COMP_PAG

**FKs**:
- COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO → X201_CAPA_CUPOM_CFE(COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)

---

## X2051_POSTO_BANCARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_POSTO | VARCHAR2(6) | N |  |  |
| 3 | RAZAO_SOCIAL | VARCHAR2(100) | Y |  |  |
| 4 | CNPJ | VARCHAR2(14) | Y |  |  |
| 5 | INSC_MUNICIPAL | VARCHAR2(14) | Y |  |  |
| 6 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 7 | NUM_ENDERECO | VARCHAR2(10) | Y |  |  |
| 8 | COMPL_ENDERECO | VARCHAR2(45) | Y |  |  |
| 9 | BAIRRO | VARCHAR2(20) | Y |  |  |
| 10 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 11 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 12 | CEP | NUMBER(8) | Y |  |  |
| 13 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 14 | IND_ATENDIMENTO | CHAR(1) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_POSTO

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- COD_PAIS → PAIS(COD_PAIS)

---

## X2053_GRUPO_BENS_ATIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRUPO_BEM | NUMBER(6) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_GRUPO_BEM | VARCHAR2(9) | N |  |  |
| 5 | DATA_VALID_GRUPO | DATE | N |  |  |
| 6 | IND_IDENT_GRUPO | VARCHAR2(2) | N |  |  |
| 7 | DESC_COMPL_GRUPO | VARCHAR2(255) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_GRUPO_BEM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- UIX_GRUPO_BENS_ATIVO (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_GRUPO_BEM, DATA_VALID_GRUPO)

---

## X2054_UNID_IMOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_UNID_IMOB | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 4 | COD_UNID_IMOB | VARCHAR2(11) | Y |  |  |
| 5 | DATA_INI_VALID | DATE | Y |  |  |
| 6 | IND_TP_UNID_IMOB | VARCHAR2(2) | Y |  |  |
| 7 | ID_NOME_EMPR | VARCHAR2(255) | Y |  |  |
| 8 | DESC_RES_UNID_IMOB | VARCHAR2(90) | Y |  |  |
| 9 | IND_NAT_EMPR | VARCHAR2(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_TP_IMOVEL | CHAR(1) | Y |  |  |
| 12 | ENDERECO | VARCHAR2(60) | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 15 | CEP | NUMBER(8) | Y |  |  |

**PK**: IDENT_UNID_IMOB

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

**Indexes**:
- IX_UNID_IMOB (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_UNID_IMOB, DATA_INI_VALID)

---

## X2055_COD_NBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NBS | NUMBER(12) | N |  |  |
| 2 | COD_NBS | VARCHAR2(9) | Y |  |  |
| 3 | VALID_NBS | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(255) | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_NBS

---

## X2056_HIST_FATO_CONTABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_HIST_FATO_CONTABIL | NUMBER(12) | N |  |  |
| 2 | GRUPO_HIST_FATO_CONTABIL | VARCHAR2(9) | Y |  |  |
| 3 | COD_HIST_FATO_CONTABIL | VARCHAR2(6) | Y |  |  |
| 4 | VALID_HISTORICO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_HIST_FATO_CONTABIL

**FKs**:
- GRUPO_HIST_FATO_CONTABIL → GRUPO_ESTAB(GRUPO_ESTAB)

---

## X2057_COD_SCP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SCP | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | COD_SCP | VARCHAR2(14) | N |  |  |
| 5 | VALID_SCP | DATE | N |  |  |
| 6 | DSC_SCP | VARCHAR2(100) | Y |  |  |
| 7 | DSC_INF_COMPL | VARCHAR2(100) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | DATA_VALID_FIM | DATE | Y |  |  |
| 11 | IND_DIRF | CHAR(1) | Y | 'N' |  |

**PK**: IDENT_SCP

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_X2057_COD_SCP (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_SCP, VALID_SCP)

---

## X2058_PROC_ADJ

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PROC_ADJ | NUMBER(12) | N |  |  |
| 2 | GRUPO_PROC_ADJ | VARCHAR2(9) | N |  | Grupo do Processo |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  | Tipo do Processo. Dominio: 1 - Administrativo; 2 - Judicial; 4 - Processo FAP. |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | N |  | Numero do Processo Administrativo ou Judicial |
| 5 | VALID_PROC_ADJ_INI | DATE | N |  | Data Inicio Validade |
| 6 | VALID_PROC_ADJ_FIM | DATE | Y |  | Data Fim Validade |
| 7 | IDENT_ESTADO | NUMBER(12) | Y |  | UF da Vara |
| 8 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 9 | COD_VARA | VARCHAR2(4) | Y |  | Codigo de Identificacao da Vara |
| 10 | IND_AUTORIA | CHAR(1) | Y |  | Indicador da autoria da acao judicial. Dominio: 1 - Proprio contribuinte; 2 - Outra entidade, empresa ou empregado. |
| 11 | IND_REINF | CHAR(1) | Y |  | Indicativo do processo para geração do REINF. Domínio: S, N |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | IND_INCIDENCIA_ESOCIAL | CHAR(1) | Y |  |  |
| 15 | IND_MATERIA_PROC | VARCHAR2(2) | Y |  |  |
| 16 | IND_ABRANGENCIA_PROC | CHAR(1) | Y |  |  |
| 17 | DSC_OBSERVACAO | VARCHAR2(255) | Y |  | Observacao para o eSocial |

**PK**: IDENT_PROC_ADJ

**FKs**:
- GRUPO_PROC_ADJ → GRUPO_ESTAB(GRUPO_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

**Indexes**:
- UK_X2058_PROC_ADJ_001 (UNIQUE): (GRUPO_PROC_ADJ, IND_TP_PROC_ADJ, NUM_PROC_ADJ, VALID_PROC_ADJ_INI)

---

## X2058_PROC_ADJ_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PROC_ADJ_HIST | NUMBER(12) | N |  |  |
| 2 | GRUPO_PROC_ADJ | VARCHAR2(9) | N |  | Grupo do Processo |
| 3 | IND_TP_PROC_ADJ | CHAR(1) | N |  | Tipo do Processo. Dominio: 1 - Administrativo; 2 - Judicial. |
| 4 | NUM_PROC_ADJ | VARCHAR2(21) | N |  | Numero do Processo Administrativo ou Judicial |
| 5 | VALID_PROC_ADJ_INI | DATE | N |  | Data Inicio Validade |
| 6 | DAT_OCORRENCIA | TIMESTAMP(6) | N |  |  |
| 7 | VALID_PROC_ADJ_FIM | DATE | Y |  | Data Fim Validade |
| 8 | IDENT_ESTADO | NUMBER(12) | Y |  | UF da Vara |
| 9 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 10 | COD_VARA | VARCHAR2(4) | Y |  | Codigo de Identificacao da Vara |
| 11 | IND_AUTORIA | CHAR(1) | Y |  | Indicador da autoria da acao judicial. Dominio: 1 - Proprio contribuinte; 2 - Outra entidade, empresa ou empregado. |
| 12 | IND_STATUS | CHAR(1) | Y |  | DOMÍNIO: REINF_STATUS_X2058_HIST_V |
| 13 | IND_DELETE | CHAR(1) | Y |  | Dominio: S, N |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 16 | IND_REINF | VARCHAR2(1) | Y |  | Indicativo do processo para geraÃ§Ã£o do REINF. DomÃ­nio: S, N |
| 17 | IND_INCIDENCIA_ESOCIAL | VARCHAR2(1) | Y |  | Indicativo do processo para geraÃ§Ã£o do ESOACIAL. DomÃ­nio: S, N |
| 18 | IND_MATERIA_PROC | VARCHAR2(2) | Y |  |  |
| 19 | IND_ABRANGENCIA_PROC | VARCHAR2(1) | Y |  |  |
| 20 | DSC_OBSERVACAO | VARCHAR2(255) | Y |  |  |

**PK**: IDENT_PROC_ADJ_HIST

**FKs**:
- GRUPO_PROC_ADJ → GRUPO_ESTAB(GRUPO_ESTAB)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

**Indexes**:
- UK_X2058_PROC_ADJ_HIST_001 (UNIQUE): (GRUPO_PROC_ADJ, IND_TP_PROC_ADJ, NUM_PROC_ADJ, VALID_PROC_ADJ_INI, DAT_OCORRENCIA)

---

## X2059_SUSP_TBT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SUSP_TBT | NUMBER(12) | N |  |  |
| 2 | IDENT_PROC_ADJ | NUMBER(12) | N |  |  |
| 3 | COD_SUSP | VARCHAR2(14) | Y |  | Codigo do Indicativo de Suspensao. |
| 4 | IND_SUSP | VARCHAR2(2) | N |  | Indicativo de suspensao da exigibilidade. Dominio 01 - Liminar em Mandado de Segurana; 04 - Antecipacao de Tutela; 05 - Liminar em Medida Cautelar; 08 - Sentenc em Mandado de Segurana Favoravel ao Contribuinte; 09 - Sentenca em Acao Ordinaria Favoravel ao Contribuinte e Confirmada pelo TRF; 10 - Acordao do TRF Favoravel ao Contribuinte; 11 - Acordao do STJ em Recurso Especial Favoravel ao Contribuinte; 12 - Acordao do STF em Recurso Extraordinario Favoravel ao Contribuinte; 13 - Sentena 1a instancia nao transitada em julgado com efeito suspensivo; 90 - Decisao Definitiva a favor do contribuinte; 92 - Sem suspensao da exigibilidade. |
| 5 | DAT_DECISAO | DATE | N |  | Data da decisao, sentenca ou despacho administrativo. |
| 6 | IND_DEPOSITO | CHAR(1) | N |  | Indicativo de Deposito do Montante Integral. Dominio: S - Sim; N - No. |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_SUSP_TBT

**FKs**:
- IDENT_PROC_ADJ → X2058_PROC_ADJ(IDENT_PROC_ADJ)

**Indexes**:
- UK_X2059_SUSP_TBT_001 (UNIQUE): (IDENT_PROC_ADJ, COD_SUSP)

---

## X2059_SUSP_TBT_HIST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_SUSP_TBT_HIST | NUMBER(12) | N |  |  |
| 2 | IDENT_PROC_ADJ_HIST | NUMBER(12) | N |  |  |
| 3 | COD_SUSP | VARCHAR2(14) | Y |  | Codigo do Indicativo de Suspensao. |
| 4 | IND_SUSP | VARCHAR2(2) | N |  | Indicativo de suspensao da exigibilidade. Dominio 01 - Liminar em Mandado de Segurana; 04 - Antecipacao de Tutela; 05 - Liminar em Medida Cautelar; 08 - Sentenc em Mandado de Segurana Favoravel ao Contribuinte; 09 - Sentenca em Acao Ordinaria Favoravel ao Contribuinte e Confirmada pelo TRF; 10 - Acordao do TRF Favoravel ao Contribuinte; 11 - Acordao do STJ em Recurso Especial Favoravel ao Contribuinte; 12 - Acordao do STF em Recurso Extraordinario Favoravel ao Contribuinte; 13 - Sentena 1a instancia nao transitada em julgado com efeito suspensivo; 90 - Decisao Definitiva a favor do contribuinte; 92 - Sem suspensao da exigibilidade. |
| 5 | DAT_DECISAO | DATE | N |  | Data da decisao, sentenca ou despacho administrativo. |
| 6 | IND_DEPOSITO | CHAR(1) | N |  | Indicativo de Deposito do Montante Integral. Dominio: S - Sim; N - No. |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_SUSP_TBT_HIST

**FKs**:
- IDENT_PROC_ADJ_HIST → X2058_PROC_ADJ_HIST(IDENT_PROC_ADJ_HIST)

**Indexes**:
- UK_X2059_SUSP_TBT_HIST_001 (UNIQUE): (IDENT_PROC_ADJ_HIST, COD_SUSP)

---

## X205_FORMA_PAGTO_NFE

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
| 11 | IDENT_OPERACAO | NUMBER(12) | N |  |  |
| 12 | NUM_COMP_PAG | VARCHAR2(18) | N |  |  |
| 13 | IND_NAT_OPER | CHAR(1) | Y |  |  |
| 14 | VLR_OPERACAO | NUMBER(17,2) | Y |  |  |
| 15 | CEP | NUMBER(8) | Y |  |  |
| 16 | NUM_PONTO_VENDA | VARCHAR2(8) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, NUM_COMP_PAG

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)

---

## X2060_TANQUE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TANQUE | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | NUM_TANQUE | NUMBER(10) | N |  |  |
| 5 | VALID_TANQUE | DATE | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | QTD_CAPAC | NUMBER(17,6) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | VLR_UNIT_PRD | NUMBER(18,6) | Y |  |  |

**PK**: IDENT_TANQUE

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_X2060_TANQUE (UNIQUE): (COD_ESTAB, NUM_TANQUE, COD_EMPRESA, VALID_TANQUE)

---

## X2061_BOMBA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_BOMBA | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | NUM_BOMBA | NUMBER(10) | N |  |  |
| 5 | VALID_BOMBA | DATE | N |  |  |
| 6 | SERIE_BOMBA | VARCHAR2(12) | N |  |  |
| 7 | FABRICANTE | VARCHAR2(80) | N |  |  |
| 8 | DSC_MODELO | VARCHAR2(20) | N |  |  |
| 9 | IND_TP_MEDICAO | CHAR(1) | N |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | CNPJ_FABRICANTE | VARCHAR2(14) | Y |  |  |

**PK**: IDENT_BOMBA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_X2061_BOMBA (UNIQUE): (COD_ESTAB, NUM_BOMBA, COD_EMPRESA, VALID_BOMBA)

---

## X2062_BICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_BICO | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | NUM_BOMBA | NUMBER(10) | N |  |  |
| 5 | NUM_BICO | NUMBER(10) | N |  |  |
| 6 | VALID_BICO | DATE | N |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_BICO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_X2062_BICO (UNIQUE): (COD_ESTAB, NUM_BOMBA, NUM_BICO, COD_EMPRESA, VALID_BICO)

---

## X206_ITENS_BOLETIM_CONF

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
| 12 | COD_CARACT | VARCHAR2(3) | N |  |  |
| 13 | NUM_BOLETIM_CONF | VARCHAR2(35) | N |  |  |
| 14 | COD_METODO | VARCHAR2(3) | Y |  |  |
| 15 | COD_VAL_CARACT | VARCHAR2(20) | Y |  |  |
| 16 | VAL_MASSA_ESPEC | NUMBER(19,4) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, COD_CARACT

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

---

## X207_FICHA_FINANC_PREV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | IND_FOLHA | VARCHAR2(2) | N |  |  |
| 8 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 9 | DATA_PAGTO | DATE | N |  |  |
| 10 | CNPJ_PREVIDENCIA | VARCHAR2(14) | Y |  |  |
| 11 | DSC_NOME_PREVIDENCIA | VARCHAR2(150) | Y |  |  |
| 12 | IND_TP_PREVIDENCIA | VARCHAR2(2) | N |  | 01 - Previdencia Privada;02 - FAPI;03 - Fundo de Previdencia do Servidor Publico;04 - Contribuicao do Ente Publico Patrocinador. |
| 13 | VLR_VERBA | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO → X21_FICHA_FINANC(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO)
- IDENT_VERBA → X2023_VERBAS(IDENT_VERBA)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)

**Indexes**:
- UK_X207_FICHA_FINANC_PREV (UNIQUE): (COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO, CNPJ_PREVIDENCIA, IND_TP_PREVIDENCIA)

---

## X2080_COD_REC_UF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_RECEITA_EST | NUMBER(12) | N |  |  |
| 2 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 3 | GRUPO_RECEITA_EST | VARCHAR2(9) | Y |  |  |
| 4 | COD_RECEITA_EST | VARCHAR2(6) | Y |  |  |
| 5 | VALID_RECEITA_EST | DATE | Y |  |  |
| 6 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_RECEITA_EST

**FKs**:
- GRUPO_RECEITA_EST → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_X2080_REC_EST (UNIQUE): (IDENT_ESTADO, GRUPO_RECEITA_EST, COD_RECEITA_EST, VALID_RECEITA_EST)

---

## X2081_EXTENSAO_CFO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CFO | NUMBER(12) | N |  |  |
| 2 | IDENT_NATUREZA_OP | NUMBER(12) | N |  |  |
| 3 | IND_APLICACAO | CHAR(1) | Y |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 6 | IDENT_OBS_LV_ICMS | NUMBER(12) | Y |  |  |
| 7 | IDENT_OBS_LV_IPI | NUMBER(12) | Y |  |  |
| 8 | IDENT_DET_OP_ICMS | NUMBER(12) | Y |  |  |
| 9 | IDENT_DET_OP_IPI | NUMBER(12) | Y |  |  |
| 10 | IND_INCID_PIS | VARCHAR2(1) | Y |  |  |
| 11 | IND_INCID_COFINS | VARCHAR2(1) | Y |  |  |
| 12 | IND_ICMS_EST_CRED | CHAR(1) | Y |  |  |
| 13 | COMPL_CFOP | VARCHAR2(2) | Y |  |  |
| 14 | DSC_OPERACAO | VARCHAR2(50) | Y |  |  |

**PK**: IDENT_CFO, IDENT_NATUREZA_OP

**FKs**:
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- IDENT_OBS_LV_ICMS → COD_OBS_LIVRO(IDENT_OBS_LIVRO)
- IDENT_OBS_LV_IPI → COD_OBS_LIVRO(IDENT_OBS_LIVRO)

**Indexes**:
- IX_X2081_EXT_CFO_01: (IDENT_NATUREZA_OP)

---

## X2082_CONS_REGPROF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONSELHO | NUMBER(12) | N |  |  |
| 2 | GRUPO_CONSELHO | VARCHAR2(9) | Y |  |  |
| 3 | COD_CONSELHO | VARCHAR2(10) | Y |  |  |
| 4 | VALID_CONSELHO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | REGIAO | NUMBER(3) | Y |  |  |
| 7 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_CONSELHO

**FKs**:
- GRUPO_CONSELHO → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_CONSELHO (UNIQUE): (GRUPO_CONSELHO, COD_CONSELHO, VALID_CONSELHO)

---

## X2083_COD_NALADI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NALADI | NUMBER(12) | N |  |  |
| 2 | COD_NALADI | VARCHAR2(10) | Y |  |  |
| 3 | VALID_NALADI | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_NALADI

**Indexes**:
- IX_CHN_COD_NALADI (UNIQUE): (COD_NALADI, VALID_NALADI)

---

## X2084_NAT_DIPI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_NAT_DIPI | NUMBER(12) | N |  |  |
| 2 | COD_NAT_DIPI | VARCHAR2(3) | Y |  |  |
| 3 | VALID_NAT_DIPI | DATE | Y |  |  |
| 4 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_NAT_DIPI

**Indexes**:
- IX_CHAVE_NAT_IPI (UNIQUE): (COD_NAT_DIPI, VALID_NAT_DIPI)

---

## X2087_EQUIPAMENTO_ECF
**Comment**: Cadastro de Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 5 | COD_MODELO | VARCHAR2(2) | N |  | Código do Modelo do documento (X2024_MODELO_DOCTO) emitido pelo ECF. |
| 6 | COD_CAIXA_ECF | VARCHAR2(3) | N |  | Número do Caixa do ECF. |
| 7 | VALID_CAIXA_ECF | DATE | N |  |  |
| 8 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  |  |
| 9 | COD_FABRICACAO_ECF | VARCHAR2(21) | Y |  |  |
| 10 | IND_MF_ADICIONAL | CHAR(1) | Y |  |  |
| 11 | COD_TIPO_ECF | VARCHAR2(7) | Y |  | DOMÍNIO: ECF-MR, ECF-IF, ECF-PDV |
| 12 | COD_MARCA_ECF | VARCHAR2(30) | Y |  | CÓDIGO DA MARCA DO EQUIPAMENTO PROVENIENTE DA TABELA MARCA/MODELO ECF - DWT_MARCA_MODELO_ECF |
| 13 | COD_MODELO_ECF | VARCHAR2(30) | Y |  | CÓDIGO DO MODELO DO EQUIPAMENTO PROVENIENTE DA TABELA MARCA/MODELO ECF - DWT_MARCA_MODELO_ECF |
| 14 | NUM_APLIC | VARCHAR2(2) | Y |  |  |
| 15 | DSC_NOME_APLIC | VARCHAR2(40) | Y |  |  |
| 16 | DSC_VERSAO_APLIC | VARCHAR2(10) | Y |  |  |
| 17 | IDENT_FIS_JUR_APLIC | NUMBER(12) | Y |  |  |
| 18 | DSC_LINHA1_APLIC | VARCHAR2(42) | Y |  |  |
| 19 | DSC_LINHA2_APLIC | VARCHAR2(42) | Y |  |  |
| 20 | DSC_VERSAO_SB | VARCHAR2(10) | Y |  |  |
| 21 | DATA_GRAVACAO_SB | DATE | Y |  |  |
| 22 | HORA_GRAVACAO_SB | NUMBER(6) | Y |  | formato HHMMSS |
| 23 | NUM_USU | VARCHAR2(2) | Y |  |  |
| 24 | DATA_CADASTRO_USU | DATE | Y |  |  |
| 25 | HORA_CADASTRO_USU | NUMBER(6) | Y |  | formato HHMMSS |
| 26 | IND_DESCONTO_ISS | CHAR(1) | Y |  |  |
| 27 | IND_TIPO_DESCONTO | CHAR(1) | Y |  |  |
| 28 | IND_TIPO_ACRESCIMO | CHAR(1) | Y |  |  |
| 29 | IND_ORD_DESC_ACRES | CHAR(1) | Y |  |  |
| 30 | DSC_VERSAO_BIBLIOTECA | VARCHAR2(8) | Y |  |  |
| 31 | COD_GERACAO_ARQ | VARCHAR2(3) | Y |  | DOMÍNIO: RFD, APL, ALT |
| 32 | DSC_VERSAO_COTEPE | VARCHAR2(15) | Y |  |  |
| 33 | IND_ARREDONDA_TRUNCA | CHAR(1) | Y |  |  |
| 34 | NUM_DEC_QTDE | NUMBER(1) | Y |  |  |
| 35 | NUM_DEC_VLR_UNIT | NUMBER(1) | Y |  |  |
| 36 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 37 | NUM_CRO | VARCHAR2(6) | Y |  |  |
| 38 | VLR_GT_TOTAL | NUMBER(17,2) | Y |  |  |
| 39 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 40 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 41 | NUM_COO_FIM_REI | VARCHAR2(9) | Y |  |  |
| 42 | NUM_APF | VARCHAR2(9) | Y |  |  |
| 43 | DAT_APF | DATE | Y |  |  |

**PK**: IDENT_CAIXA_ECF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR_APLIC → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_MARCA_ECF, COD_MODELO_ECF → DWT_MARCA_MODELO_ECF(COD_MARCA_ECF, COD_MODELO_ECF)

**Indexes**:
- IX_FK_SAF_2185: (IDENT_FIS_JUR_APLIC)
- IX_X2087_EQUIP_ECF: (COD_ESTAB, COD_CAIXA_ECF, COD_EMPRESA, COD_MODELO, GRUPO_MODELO, VALID_CAIXA_ECF)

---

## X2088_ORGAO_ARREC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ORG_ARRECAD | NUMBER(12) | N |  |  |
| 2 | GRUPO_ORG_ARRECAD | VARCHAR2(9) | Y |  |  |
| 3 | COD_ORG_ARRECAD | VARCHAR2(10) | Y |  |  |
| 4 | VALID_ORG_ARRECAD | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_ORG_ARRECAD

**FKs**:
- GRUPO_ORG_ARRECAD → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- IX_CHN_ORG_ARRECAD (UNIQUE): (GRUPO_ORG_ARRECAD, COD_ORG_ARRECAD, VALID_ORG_ARRECAD)

---

## X208_REEMBOLSO_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 8 | DATA_PAGTO | DATE | N |  |  |
| 9 | CPF_CNPJ_PREST_SERV | VARCHAR2(14) | N |  |  |
| 10 | DSC_PREST_SERV | VARCHAR2(150) | N |  |  |
| 11 | VLR_REEMBOLSO | NUMBER(17,2) | Y |  |  |
| 12 | VLR_REEMBOLSO_ANT | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IDENT_VERBA, DATA_PAGTO, CPF_CNPJ_PREST_SERV

**FKs**:
- IDENT_VERBA → X2023_VERBAS(IDENT_VERBA)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)

---

## X2093_ARV_PRD_DRBK

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | IDENT_MAT_PRIMA | NUMBER(12) | N |  |  |
| 5 | QTD_AUTORIZ | NUMBER(17,6) | Y |  |  |
| 6 | QTD_TOTAL | NUMBER(17,6) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 10 | IND_UTILIZ_SISIF | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, IDENT_MAT_PRIMA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MAT_PRIMA → X2013_PRODUTO(IDENT_PRODUTO)

---

## X2094_CENTRO_RESP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CENTRO_RESP | NUMBER(12) | N |  |  |
| 2 | GRUPO_CENTRO_RESP | VARCHAR2(9) | Y |  |  |
| 3 | COD_CENTRO_RESP | VARCHAR2(20) | Y |  |  |
| 4 | VALID_CENTRO_RESP | DATE | Y |  |  |
| 5 | DSC_CENTRO_RESP | VARCHAR2(50) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_CENTRO_RESP

**Indexes**:
- IX_X2094_CENT_RESP (UNIQUE): (GRUPO_CENTRO_RESP, COD_CENTRO_RESP, VALID_CENTRO_RESP)

---

## X2095_UNID_NEGOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_UNID_NEGOC | NUMBER(12) | N |  |  |
| 2 | GRUPO_UNID_NEGOC | VARCHAR2(9) | Y |  |  |
| 3 | COD_UNID_NEGOC | VARCHAR2(20) | Y |  |  |
| 4 | VALID_UNID_NEGOC | DATE | Y |  |  |
| 5 | DSC_UNID_NEGOC | VARCHAR2(50) | Y |  |  |
| 6 | NOM_RESP | VARCHAR2(50) | Y |  |  |
| 7 | COD_MATRICULA | VARCHAR2(15) | Y |  |  |
| 8 | EMAIL_INT | VARCHAR2(50) | Y |  |  |
| 9 | EMAIL_EXT | VARCHAR2(50) | Y |  |  |
| 10 | NUM_TEL | VARCHAR2(10) | Y |  |  |
| 11 | NUM_FAX | VARCHAR2(10) | Y |  |  |
| 12 | NUM_CARRIE | VARCHAR2(10) | Y |  |  |
| 13 | COD_EMPR_RESP | VARCHAR2(3) | Y |  |  |
| 14 | COD_ESTAB_RESP | VARCHAR2(6) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_UNID_NEGOC

**FKs**:
- COD_EMPR_RESP, COD_ESTAB_RESP → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_X2095_UNID_NEG (UNIQUE): (GRUPO_UNID_NEGOC, COD_UNID_NEGOC, VALID_UNID_NEGOC)

---

## X2096_AREA_NEGOC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_AREA_NEGOC | NUMBER(12) | N |  |  |
| 2 | GRUPO_AREA_NEGOC | VARCHAR2(9) | Y |  |  |
| 3 | COD_AREA_NEGOC | VARCHAR2(10) | Y |  |  |
| 4 | VALID_AREA_NEGOC | DATE | Y |  |  |
| 5 | DSC_AREA_NEGOC | VARCHAR2(50) | Y |  |  |
| 6 | NOM_RESP | VARCHAR2(50) | Y |  |  |
| 7 | COD_MATRICULA | VARCHAR2(15) | Y |  |  |
| 8 | EMAIL_INT | VARCHAR2(50) | Y |  |  |
| 9 | EMAIL_EXT | VARCHAR2(50) | Y |  |  |
| 10 | NUM_TEL | VARCHAR2(10) | Y |  |  |
| 11 | NUM_FAX | VARCHAR2(10) | Y |  |  |
| 12 | NUM_CARRIE | VARCHAR2(10) | Y |  |  |
| 13 | COD_EMPR_RESP | VARCHAR2(3) | Y |  |  |
| 14 | COD_ESTAB_RESP | VARCHAR2(6) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_AREA_NEGOC

**FKs**:
- COD_EMPR_RESP, COD_ESTAB_RESP → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_X2096_AREA_NEG (UNIQUE): (GRUPO_AREA_NEGOC, COD_AREA_NEGOC, VALID_AREA_NEGOC)

---

## X2097_MUNIC_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 2 | DSC_MUNIC_ISS | VARCHAR2(50) | Y |  |  |
| 3 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 4 | COD_MUNIC_MSAF | NUMBER(5) | Y |  |  |
| 5 | COD_AREA_LIVR_COM | VARCHAR2(10) | Y |  |  |
| 6 | NOM_PREFEITURA | VARCHAR2(50) | Y |  |  |
| 7 | ENDERECO | VARCHAR2(50) | Y |  |  |
| 8 | CEP | NUMBER(8) | Y |  |  |
| 9 | CONTATO | VARCHAR2(50) | Y |  |  |
| 10 | DIA_VENCTO | NUMBER(2) | Y |  |  |
| 11 | COD_BANCO_REC | VARCHAR2(3) | Y |  |  |
| 12 | NUM_AG_REC | VARCHAR2(7) | Y |  |  |
| 13 | NUM_CONTA_REC | VARCHAR2(18) | Y |  |  |
| 14 | DSC_FORMA_REC | VARCHAR2(30) | Y |  |  |
| 15 | IND_SUBST_TRIB | CHAR(1) | Y |  |  |
| 16 | IND_PERMIT_ABAT | CHAR(1) | Y |  |  |
| 17 | OBS_ISS1 | VARCHAR2(120) | Y |  |  |
| 18 | OBS_ISS2 | VARCHAR2(120) | Y |  |  |
| 19 | VLR_LIM_RECOLH | NUMBER(17,2) | Y |  |  |
| 20 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | OBS_NF | VARCHAR2(250) | Y |  |  |
| 23 | IND_FORMA_CALC_ISS | CHAR(1) | Y |  |  |
| 24 | IND_RESUMO_ALIQ | CHAR(1) | Y |  |  |
| 25 | IND_DEM_DEB_CRED | CHAR(1) | Y |  |  |
| 26 | IND_EQUIPARADO_CC | CHAR(1) | Y |  |  |
| 27 | IND_ISS_TERCEIROS | CHAR(1) | Y |  |  |
| 28 | IND_CRED_NF_CANC | CHAR(1) | Y |  |  |
| 29 | IND_APUR_DT_FATGER | CHAR(1) | Y |  |  |
| 30 | IND_EMIT_GUIA_REC | CHAR(1) | Y |  |  |
| 31 | IND_TP_SERV_SUBST | CHAR(1) | Y |  |  |
| 32 | LIM_CRED_PER_APUR | NUMBER(17,2) | Y |  |  |
| 33 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 34 | COD_RECEITA | VARCHAR2(5) | Y |  |  |
| 35 | DIA_VENCIMENTO | NUMBER(2) | Y |  |  |
| 36 | VLR_TAXA_EXPED | NUMBER(17,2) | Y |  |  |
| 37 | TITULO_GUIA_01 | VARCHAR2(60) | Y |  |  |
| 38 | TITULO_GUIA_02 | VARCHAR2(60) | Y |  |  |
| 39 | TITULO_GUIA_03 | VARCHAR2(60) | Y |  |  |
| 40 | TITULO_GUIA_04 | VARCHAR2(60) | Y |  |  |
| 41 | VLR_MORA_DIA | NUMBER(17,2) | Y |  |  |
| 42 | VLR_MORA_PERC_MES | NUMBER(8,4) | Y |  |  |
| 43 | VLR_MULTA_DIA | NUMBER(17,2) | Y |  |  |
| 44 | VLR_MULTA_PERC_MES | NUMBER(7,4) | Y |  |  |
| 45 | IND_EXIGE_COMP | CHAR(1) | Y |  |  |
| 46 | VLR_ALIQ_SERV_EQ | NUMBER(7,4) | Y |  |  |
| 47 | IND_NF_CANC | CHAR(1) | Y |  |  |
| 48 | VLR_ALIQ_ISS_TERC | NUMBER(7,4) | Y |  |  |
| 49 | TITULO_LVR | VARCHAR2(120) | Y |  |  |
| 50 | DSC_REG_ESPEC_LVR | VARCHAR2(120) | Y |  |  |
| 51 | IND_INSC_DF_LVR | CHAR(1) | Y | 'N' |  |
| 52 | IND_FORMATO_GERAL | CHAR(1) | Y | 'S' |  |
| 53 | COD_FORMATO_GERAL | VARCHAR2(3) | Y | 'FGS' |  |
| 54 | IND_FORMATO_ESP | CHAR(1) | Y | 'N' |  |
| 55 | COD_FORMATO_ESP | NUMBER(5) | Y |  |  |
| 56 | IND_APUR_DAT_EMISSAO | CHAR(1) | Y | 'N' |  |
| 57 | DATA_VALID_INI | DATE | Y |  |  |
| 58 | DATA_VALID_FIM | DATE | Y |  |  |
| 59 | IND_GER_L116 | CHAR(1) | Y | '1' | 1 - CODIGO NATUREZA DE SERVICO / 2 - CODIGO SERVICO L116/03 |
| 60 | IND_LCTO_COMPL_CR_DED | CHAR(1) | Y |  |  |
| 61 | IND_GER_ALIQ_NF | CHAR(1) | Y | 'N' | Calcular                               Imposto Retido de Terceiros com base nos Documentos Fiscais |
| 62 | IND_VENC_FERIADO | VARCHAR2(1) | Y |  |  |

**PK**: COD_MUNIC_ISS

**FKs**:
- IDENT_ESTADO, COD_MUNIC_MSAF → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- COD_FORMATO_ESP → IST_LAYOUT_LVR_ISS(COD_LAYOUT_LVR_ISS)

**Indexes**:
- IX_X2097_MUNIC_ISS: (COD_MUNIC_ISS, IDENT_ESTADO, COD_BANCO_REC, DSC_MUNIC_ISS, ENDERECO, CEP, CONTATO)

---

## X2098_ALIQ_SERVICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNIC_ISS | NUMBER(7) | N |  |  |
| 2 | GRUPO_SERVICO | VARCHAR2(9) | N |  |  |
| 3 | COD_SERVICO | VARCHAR2(4) | N |  |  |
| 4 | DAT_VALID_ALIQ | DATE | N |  |  |
| 5 | VLR_ALIQ_SERVICO | NUMBER(7,4) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_TOM_TRIBUT_ISS | CHAR(1) | Y |  |  |
| 9 | IND_SUBSTITUIDO_ISS | CHAR(1) | Y |  |  |
| 10 | COD_SERVICO_MUNIC | VARCHAR2(5) | Y |  |  |

**PK**: COD_MUNIC_ISS, GRUPO_SERVICO, COD_SERVICO, DAT_VALID_ALIQ

**FKs**:
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)

---

## X2099_EQUIPAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 4 | SERIE_EQUIPAMENTO | VARCHAR2(20) | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO

---

## X209_REEMBOLSO_DEP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 8 | DATA_PAGTO | DATE | N |  |  |
| 9 | COD_DEPEND | NUMBER(2) | N |  |  |
| 10 | VALID_DEPEND | DATE | N |  |  |
| 11 | CPF_CNPJ_PREST_SERV | VARCHAR2(14) | N |  |  |
| 12 | DSC_PREST_SERV | VARCHAR2(150) | N |  |  |
| 13 | VLR_REEMBOLSO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_REEMBOLSO_ANT | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IDENT_VERBA, DATA_PAGTO, COD_DEPEND, VALID_DEPEND, CPF_CNPJ_PREST_SERV

**FKs**:
- IDENT_VERBA → X2023_VERBAS(IDENT_VERBA)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, COD_DEPEND, VALID_DEPEND → X55_DEPEND_FUNC(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, COD_DEPEND, VALID_DEPEND)

---

## X2101_CONTAS_REF_CCUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 2 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 3 | IDENT_CUSTO | NUMBER(12) | N |  |  |

**PK**: IDENT_CONTA, IDENT_CONTA_REF, IDENT_CUSTO

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X2101_CONTAS_REF_CTA: (IDENT_CONTA)

---

## X2101_CONTAS_REF_CCUSTO_FCONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 2 | IDENT_CONTA_REF | NUMBER(12) | N |  |  |
| 3 | IDENT_CUSTO | NUMBER(12) | N |  |  |

**PK**: IDENT_CONTA, IDENT_CONTA_REF, IDENT_CUSTO

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)

**Indexes**:
- IX_X2101_CONTAS_REF_CTA_FCONT: (IDENT_CONTA)

---

## X2102_CONTAS_AGLUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | NUM_ORD | NUMBER(4) | N |  |  |
| 5 | DESCRICAO | VARCHAR2(100) | N |  |  |
| 6 | IND_BALANCO_DRE | CHAR(1) | N |  |  |
| 7 | IND_NATUREZA | CHAR(1) | Y |  |  |
| 8 | IND_CLASSIF_DRE | CHAR(1) | Y |  |  |
| 9 | NIVEL | VARCHAR2(5) | N |  |  |
| 10 | EXPRESSAO_ORD | VARCHAR2(4000) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | IND_UTIL_AGLUT | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_X2102_CONTAS_AGLUT: (COD_EMPRESA, COD_ESTAB, IND_BALANCO_DRE)

---

## X2103_CONTAS_AGLUT_EMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 7 | IND_UTIL_AGLUT | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT, IDENT_CONTA

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT → X2102_CONTAS_AGLUT(COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT)

**Indexes**:
- IX_X2103_CONTAS_AGLUT_EMP: (IDENT_CONTA)

---

## X2103_CONTAS_AGLUT_EMP_CUSTOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | GRUPO_CUSTO | VARCHAR2(9) | N |  |  |
| 6 | COD_CUSTO | VARCHAR2(50) | N |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | IND_UTIL_AGLUT | VARCHAR2(10) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT, IDENT_CONTA, GRUPO_CUSTO, COD_CUSTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT, IDENT_CONTA → X2103_CONTAS_AGLUT_EMP(COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT, IDENT_CONTA)

---

## X2104_LANCTO_CONTAS_AGLUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 4 | IND_UTIL_AGLUT | VARCHAR2(10) | N |  |  |
| 5 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 6 | DATA_LANCTO | DATE | N |  |  |
| 7 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 8 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 9 | IDENT_HIST_FATO_CONTABIL | NUMBER(12) | N |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | COD_ESTAB_LANCTO | VARCHAR2(6) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT, IDENT_CONTA, DATA_LANCTO, IND_DEB_CRE, ARQUIVAMENTO, IDENT_HIST_FATO_CONTABIL

**FKs**:
- IDENT_HIST_FATO_CONTABIL → X2056_HIST_FATO_CONTABIL(IDENT_HIST_FATO_CONTABIL)
- COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT, IDENT_CONTA → X2103_CONTAS_AGLUT_EMP(COD_EMPRESA, COD_ESTAB, COD_CONTA_AGLUT, IND_UTIL_AGLUT, IDENT_CONTA)

---

## X2106_PAR_DYNTB
**Comment**: Tabela Mestre da Parametrizacao da Tabela Dinamica com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_DYNTB | NUMBER(12) | N |  | Identificador unico do registro na tabela. SEQ_X2106_PAR_DYNTB  |
| 2 | COD_PAR_DYNTB | VARCHAR2(14) | N |  | Codigo da Parametrizacao da Associacao Tabela Dinamica x Plano Empresa |
| 3 | DAT_STARTUP_EFFECTIVE | DATE | N |  | Data Inicio Validade |
| 4 | IDENT_CAD_DYNTB | NUMBER(12) | N |  | Identificador do Cadastro da Versao da Tabela Dinamica (tabela ECF_CAD_DYNTB). |
| 5 | DSC_PAR_DYNTB | VARCHAR2(100) | N |  | Descricao da Parametrizacao da Associacao Tabela Dinamica x Plano Empresa |
| 6 | GRUPO_ESTAB | VARCHAR2(9) | N |  | Codigo do Grupo de Estabelecimentos (tabela GRUPO_ESTAB) |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_DYNTB

**FKs**:
- IDENT_CAD_DYNTB → ECF_CAD_DYNTB(IDENT_CAD_DYNTB)
- GRUPO_ESTAB → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- UK_X2106_PAR_DYNTB_001 (UNIQUE): (IDENT_CAD_DYNTB, COD_PAR_DYNTB, DAT_STARTUP_EFFECTIVE)

---

## X2106_PAR_DYNTB_CC
**Comment**: Tabela dos Centros de Custo relacionados as Contas Contabeis associadas aos Itens da Tabela Dinamica - Parametrizacao da Tabela Dinamica com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_DYNTB_CC | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_X2106_PAR_DYNTB_CC. |
| 2 | IDENT_PAR_DYNTB_CTA | NUMBER(12) | N |  | Identificador Tabela das Contas Contabeis associadas na Parametrizacao. (tabela X2106_PAR_DYNTB_CTA). |
| 3 | GRUPO_CUSTO | VARCHAR2(9) | N |  | Grupo do Centro de Custo (tabela X2003_CENTRO_CUSTO). |
| 4 | COD_CUSTO | VARCHAR2(50) | N |  | Codigo do Centro de Custo (tabela X2003_CENTRO_CUSTO). |
| 5 | IDT_CUSTO | NUMBER(12) | N |  | Identificador do centro de custo (tabela X2003_CENTRO_CUSTO). |
| 6 | PCT_GROSS_REV | NUMBER(7,4) | Y |  | Percentual da Receita Bruta. |
| 7 | IDENT_PAR_DYNTB | NUMBER(12) | Y |  | Identificador da Tabela X2106_PAR_DYNTB. |
| 8 | IDENT_PAR_DYNTB_IT | NUMBER(12) | Y |  | Identificador da Tabela X2106_PAR_DYNTB_IT. |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_DYNTB_CC

**FKs**:
- IDT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_PAR_DYNTB_CTA → X2106_PAR_DYNTB_CTA(IDENT_PAR_DYNTB_CTA)
- IDENT_PAR_DYNTB → X2106_PAR_DYNTB(IDENT_PAR_DYNTB)
- IDENT_PAR_DYNTB_IT → X2106_PAR_DYNTB_IT(IDENT_PAR_DYNTB_IT)

**Indexes**:
- UK_X2106_PAR_DYNTB_CC_001 (UNIQUE): (IDENT_PAR_DYNTB_CTA, COD_CUSTO, GRUPO_CUSTO)

---

## X2106_PAR_DYNTB_CTA
**Comment**: Tabela das Contas Contabeis associadas aos Itens da Tabela Dinamica na Parametrizacao da Tabela Dinamica com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_DYNTB_CTA | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_X2106_PAR_DYNTB_CTA. |
| 2 | IDENT_PAR_DYNTB_IT | NUMBER(12) | N |  | Identificador da Tabela de Itens da Tabela Dinamica associados na Parametrizacao. (tabela X2106_PAR_DYNTB_IT). |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  | Grupo da Conta Contabil (tabela X2002_PLANO_CONTAS) |
| 4 | COD_CONTA | VARCHAR2(70) | N |  | Codigo da Conta Contabil (tabela X2002_PLANO_CONTAS) |
| 5 | IDENT_CONTA | NUMBER(12) | N |  | Identificador da conta contabil (tabela X2002_PLANO_CONTAS) |
| 6 | PCT_GROSS_REV | NUMBER(7,4) | Y |  | Percentual da Receita Bruta. |
| 7 | IDENT_PAR_DYNTB | NUMBER(12) | Y |  | Identificador da Tabela X2106_PAR_DYNTB. |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_DYNTB_CTA

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_PAR_DYNTB_IT → X2106_PAR_DYNTB_IT(IDENT_PAR_DYNTB_IT)
- IDENT_PAR_DYNTB → X2106_PAR_DYNTB(IDENT_PAR_DYNTB)

**Indexes**:
- IX_X2106_PAR_DYNTB_CTA: (IDENT_CONTA)
- UK_X2106_PAR_DYNTB_CTA_001 (UNIQUE): (IDENT_PAR_DYNTB_IT, COD_CONTA, GRUPO_CONTA)

---

## X2106_PAR_DYNTB_IT
**Comment**: Tabela dos Itens da Tabela Dinamica associados na Parametrizacao da Tabela Dinamica com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_DYNTB_IT | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_X2106_PAR_DYNTB_IT |
| 2 | IDENT_PAR_DYNTB | NUMBER(12) | N |  | Identificador do registro mestre da parametrizacao (tabela X2106_PAR_DYNTB) |
| 3 | IDENT_CAD_DYNTB_IT | NUMBER(12) | N |  | Identificador do Item da Tabela Dinamica (tabela ECF_CAD_DYNTB_IT). |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_DYNTB_IT

**FKs**:
- IDENT_CAD_DYNTB_IT → ECF_CAD_DYNTB_IT(IDENT_CAD_DYNTB_IT)
- IDENT_PAR_DYNTB → X2106_PAR_DYNTB(IDENT_PAR_DYNTB)

**Indexes**:
- UK_X2106_PAR_DYNTB_IT_001 (UNIQUE): (IDENT_PAR_DYNTB, IDENT_CAD_DYNTB_IT)

---

## X2107_PAR_PLREF
**Comment**: Tabela Mestre da Parametrizacao do Plano Referencial com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_PLREF | NUMBER(12) | N |  | Identificador unico do registro na tabela. SEQ_X2107_PAR_PLREF |
| 2 | COD_PAR_REF | VARCHAR2(14) | N |  | Codigo da Parametrizacao da Associacao Plano Referencial x Plano Empresa |
| 3 | DAT_STARTUP_EFFECTIVE | DATE | N |  | Data Inicio Validade |
| 4 | IDENT_CAD_PLREF | NUMBER(12) | N |  |  |
| 5 | DSC_PAR_REF | VARCHAR2(100) | N |  | Descricao da Parametrizacao da Associacao Plano Referencial x Plano Empresa |
| 6 | GRUPO_ESTAB | VARCHAR2(9) | N |  | Codigo do Grupo de Estabelecimentos (tabela GRUPO_ESTAB) |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_PLREF

**FKs**:
- IDENT_CAD_PLREF → ECF_CAD_PLREF(IDENT_CAD_PLREF)
- GRUPO_ESTAB → GRUPO_ESTAB(GRUPO_ESTAB)

**Indexes**:
- UK_X2107_PAR_PLREF_001 (UNIQUE): (IDENT_CAD_PLREF, COD_PAR_REF, DAT_STARTUP_EFFECTIVE)

---

## X2107_PAR_PLREF_CC
**Comment**: Tabela dos Centros de Custo relacionados as Contas Contabeis associadas as Contas Referenciais  - Parametrizacao do Plano Referencial com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_PLREF_CC | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_X2107_PAR_PLREF_CC. |
| 2 | IDENT_PAR_PLREF_CTA | NUMBER(12) | N |  | Identificador do Registro Pai. |
| 3 | GRUPO_CUSTO | VARCHAR2(9) | N |  | Grupo do Centro de Custo (tabela X2003_CENTRO_CUSTO). |
| 4 | COD_CUSTO | VARCHAR2(50) | N |  | Codigo do Centro de Custo (tabela X2003_CENTRO_CUSTO). |
| 5 | IDT_CUSTO | NUMBER(12) | N |  | Identificador do centro de custo (tabela X2003_CENTRO_CUSTO). |
| 6 | IDENT_PAR_PLREF | NUMBER(12) | Y |  | Identificador da Tabela X2107_PAR_PLREF |
| 7 | IDENT_PAR_PLREF_CREF | NUMBER(12) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_PLREF_CC

**FKs**:
- IDT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_PAR_PLREF_CTA → X2107_PAR_PLREF_CTA(IDENT_PAR_PLREF_CTA)
- IDENT_PAR_PLREF → X2107_PAR_PLREF(IDENT_PAR_PLREF)
- IDENT_PAR_PLREF_CREF → X2107_PAR_PLREF_CREF(IDENT_PAR_PLREF_CREF)

**Indexes**:
- UK_X2107_PAR_PLREF_CC_001 (UNIQUE): (IDENT_PAR_PLREF_CTA, COD_CUSTO, GRUPO_CUSTO)

---

## X2107_PAR_PLREF_CREF
**Comment**: Tabela de Contas Referenciais da Parametrizacao do  Plano Referencial com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_PLREF_CREF | NUMBER(12) | N |  | Identificador unico do registro na tabela. SEQ_X2107_PAR_PLREF_CREF. |
| 2 | IDENT_PAR_PLREF | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | IDENT_CAD_PLREF_CTA | NUMBER(12) | N |  | Identificador da Conta do Plano Referencial (tabela origem ECF_CAD_PLREF_CTA) |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_PLREF_CREF

**FKs**:
- IDENT_CAD_PLREF_CTA → ECF_CAD_PLREF_CTA(IDENT_CAD_PLREF_CTA)
- IDENT_PAR_PLREF → X2107_PAR_PLREF(IDENT_PAR_PLREF)

**Indexes**:
- UK_X2107_PAR_PLREF_CREF_001 (UNIQUE): (IDENT_CAD_PLREF_CTA, IDENT_PAR_PLREF)

---

## X2107_PAR_PLREF_CTA
**Comment**: Tabela das Contas Contabeis associadas as Contas Referenciais na Parametrizacao do  Plano Referencial com Plano de Contas da Empresa.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PAR_PLREF_CTA | NUMBER(12) | N |  | Identificador unico do registro na tabela. Sequence SEQ_X2107_PAR_PLREF_CTA. |
| 2 | IDENT_PAR_PLREF_CREF | NUMBER(12) | N |  | Identificador do registro pai. |
| 3 | GRUPO_CONTA | VARCHAR2(9) | N |  | Grupo da Conta Contabil (tabela X2002_PLANO_CONTAS) |
| 4 | COD_CONTA | VARCHAR2(70) | N |  | Codigo da Conta Contabil (tabela X2002_PLANO_CONTAS) |
| 5 | IDENT_CONTA | NUMBER(12) | N |  | Identificador da conta contabil (tabela X2002_PLANO_CONTAS) |
| 6 | IDENT_PAR_PLREF | NUMBER(12) | Y |  | Identificador da Tabela X2107_PAR_PLREF |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_PAR_PLREF_CTA

**FKs**:
- IDENT_PAR_PLREF_CREF → X2107_PAR_PLREF_CREF(IDENT_PAR_PLREF_CREF)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_PAR_PLREF → X2107_PAR_PLREF(IDENT_PAR_PLREF)

**Indexes**:
- IX_X2107_PAR_PLREF_CTA: (IDENT_CONTA)
- UK_X2107_PAR_PLREF_CTA_001 (UNIQUE): (IDENT_PAR_PLREF_CREF, COD_CONTA, GRUPO_CONTA)

---

## X210_ECF_INTERVENCAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 4 | SEQUENCIAL | NUMBER(5) | N |  |  |
| 5 | TIPO_ECF | VARCHAR2(5) | Y |  |  |
| 6 | VLR_GT_FINAL | NUMBER(17,2) | Y |  |  |
| 7 | NUM_CRO | NUMBER(6) | Y |  |  |
| 8 | DATA_INTERVENCAO | DATE | Y |  |  |
| 9 | IND_INTERVENCAO | CHAR(1) | Y |  |  |
| 10 | IND_PERDA | CHAR(1) | Y |  |  |
| 11 | IND_MOTIVO | CHAR(1) | Y |  |  |
| 12 | MEMORIA_ANT | VARCHAR2(16) | Y |  |  |
| 13 | MEMORIA_NOVA | VARCHAR2(16) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO → X2099_EQUIPAMENTO(COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO)

---

## X2113_INFOPROC_CPRB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI | DATE | N |  |  |
| 4 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 5 | DISCRI_ATIV_CONT_PREV | VARCHAR2(90) | N |  |  |
| 6 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 7 | IDENT_PROC_ADJ | NUMBER(12) | N |  |  |
| 8 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 9 | VLR_PREV_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV, IND_TP_PROC_ADJ, IDENT_PROC_ADJ

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV → X185_CONTRIB_PREV(COD_EMPRESA, COD_ESTAB, DATA_INI, COD_RECEITA, DISCRI_ATIV_CONT_PREV)

---

## X2114_CAD_RUBRICA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_RUBRICA | NUMBER(12) | N |  |  |
| 2 | GRUPO_RUBRICA | VARCHAR2(9) | N |  |  |
| 3 | COD_TAB_RUBRICA | VARCHAR2(8) | N |  |  |
| 4 | COD_RUBRICA | VARCHAR2(30) | N |  |  |
| 5 | VALID_INI | DATE | N |  |  |
| 6 | VALID_FIM | DATE | Y |  |  |
| 7 | DESC_RUBRICA | VARCHAR2(100) | N |  |  |
| 8 | COD_NAT_RUBRICA | VARCHAR2(4) | N |  |  |
| 9 | TIPO_RUBRICA | CHAR(1) | N |  |  |
| 10 | TIPO_INCID_TRIB_CP | VARCHAR2(1) | Y |  |  |
| 11 | COD_INCID_TRIB_CP | VARCHAR2(4) | Y |  |  |
| 12 | TIPO_INCID_TRIB_IRRF | VARCHAR2(1) | Y |  |  |
| 13 | COD_INCID_TRIB_IRRF | VARCHAR2(4) | Y |  |  |
| 14 | IND_TP_PROC_ADJ_CP | CHAR(1) | Y |  |  |
| 15 | IDENT_PROC_ADJ_CP | NUMBER(12) | Y |  |  |
| 16 | IDENT_SUSP_TBT_CP | NUMBER(12) | Y |  |  |
| 17 | EXTENSAO_CP | CHAR(1) | Y |  |  |
| 18 | IND_TP_PROC_ADJ_IRRF | CHAR(1) | Y |  |  |
| 19 | IDENT_PROC_ADJ_IRRF | NUMBER(12) | Y |  |  |
| 20 | IDENT_SUSP_TBT_IRRF | NUMBER(12) | Y |  |  |
| 21 | OBS_RUBRICA | VARCHAR2(255) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_RUBRICA

**FKs**:
- COD_NAT_RUBRICA → PRT_NAT_RUBRICA_ESOCIAL(COD_NAT_RUBRICA)
- TIPO_INCID_TRIB_CP, COD_INCID_TRIB_CP → PRT_INCID_TRIBUT_ESOCIAL(TIPO_INCID_TRIB, COD_INCID_TRIB)
- TIPO_INCID_TRIB_IRRF, COD_INCID_TRIB_IRRF → PRT_INCID_TRIBUT_ESOCIAL(TIPO_INCID_TRIB, COD_INCID_TRIB)
- IDENT_PROC_ADJ_CP → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_PROC_ADJ_IRRF → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT_CP → X2059_SUSP_TBT(IDENT_SUSP_TBT)
- IDENT_SUSP_TBT_IRRF → X2059_SUSP_TBT(IDENT_SUSP_TBT)

**Indexes**:
- IX_X2114_CAD_RUBRICA (UNIQUE): (IDENT_RUBRICA, GRUPO_RUBRICA, COD_TAB_RUBRICA, COD_RUBRICA, VALID_INI, DESC_RUBRICA, COD_NAT_RUBRICA, TIPO_RUBRICA)

---

## X2116_CONTA_TRIB_DESIF
**Comment**: Tabela de Parametrizacao do Plano de Contas Empresa x Codigos de Tributacao DESIF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_CONTA | VARCHAR2(9) | N |  |  |
| 2 | COD_CONTA | VARCHAR2(70) | N |  |  |
| 3 | VALID_INI | DATE | N |  |  |
| 4 | VALID_FIM | DATE | Y |  |  |
| 5 | COD_TRIB_DESIF | VARCHAR2(15) | Y |  |  |
| 6 | IND_RECOLH_FONTE | CHAR(1) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: GRUPO_CONTA, COD_CONTA, VALID_INI

**FKs**:
- COD_TRIB_DESIF → CAD_TRIB_DESIF(COD_TRIB_DESIF)

---

## X211_FICHA_FINANC_SERV_PREST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | IND_FOLHA | VARCHAR2(2) | N |  |  |
| 8 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 9 | DATA_PAGTO | DATE | N |  |  |
| 10 | NUM_SEQ_FOLHA | NUMBER(3) | N |  |  |
| 11 | IDENT_FIS_JUR_TOM | NUMBER(12) | Y |  |  |
| 12 | VLR_VERBA | NUMBER(17,2) | Y |  |  |
| 13 | QTD_HORAS | NUMBER(7,2) | Y |  |  |
| 14 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 15 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO, NUM_SEQ_FOLHA

**FKs**:
- IDENT_VERBA → X2023_VERBAS(IDENT_VERBA)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)
- IDENT_FIS_JUR_TOM → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO → X21_FICHA_FINANC(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO)

**Indexes**:
- IX_FK_SAF_2346: (IDENT_FIS_JUR_TOM)
- IX_X211_FICHA_FINANC_CTA: (IDENT_CONTA)
- IX_X211_FICHA_FINANC_SPREST: (COD_ESTAB, ANO_COMPETENCIA, MES_COMPETENCIA, COD_EMPRESA, COD_FUNC, VALID_FUNC, IND_FOLHA, IDENT_VERBA)

---

## X212_FICHA_FINANC_DEP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | IND_FOLHA | VARCHAR2(2) | N |  |  |
| 8 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 9 | DATA_PAGTO | DATE | N |  |  |
| 10 | COD_DEPEND | NUMBER(2) | N |  |  |
| 11 | VALID_DEPEND | DATE | N |  |  |
| 12 | VLR_VERBA | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO, COD_DEPEND, VALID_DEPEND

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO → X21_FICHA_FINANC(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, COD_DEPEND, VALID_DEPEND → X55_DEPEND_FUNC(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, COD_DEPEND, VALID_DEPEND)
- IDENT_VERBA → X2023_VERBAS(IDENT_VERBA)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)

---

## X213_DADOS_COFATURAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_EMISSAO | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | COD_CSP | NUMBER(2) | N |  |  |
| 9 | NUM_DOCFIS_COF | VARCHAR2(12) | N |  |  |
| 10 | SERIE_DOCFIS_COF | VARCHAR2(3) | N |  |  |
| 11 | NOME_PRESTADORA | VARCHAR2(10) | Y |  |  |
| 12 | VLR_TOT_DOCTO | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, COD_CSP, NUM_DOCFIS_COF, SERIE_DOCFIS_COF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X42_CAPA_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## X214_MOV_PROD_FCI

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REFERENCIA | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | COD_MEDIDA_FCI | VARCHAR2(6) | N |  |  |
| 6 | VLR_SAIDA | NUMBER(17,2) | Y |  |  |
| 7 | VLR_PARC_IMP | NUMBER(17,2) | Y |  |  |
| 8 | PERC_CONT_IMP | NUMBER(6,2) | Y |  |  |
| 9 | NUM_FCI | VARCHAR2(36) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | PERIODO_REF_SAIDA | DATE | Y |  |  |
| 13 | DATA_REF_CALC_SAIDA | DATE | Y |  |  |
| 14 | IND_REG_GER | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_REFERENCIA, IDENT_PRODUTO, COD_MEDIDA_FCI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## X21_FICHA_FINANC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | ANO_COMPETENCIA | NUMBER(4) | N |  |  |
| 6 | MES_COMPETENCIA | NUMBER(2) | N |  |  |
| 7 | IND_FOLHA | VARCHAR2(2) | N |  |  |
| 8 | IDENT_VERBA | NUMBER(12) | N |  |  |
| 9 | DATA_PAGTO | DATE | N |  |  |
| 10 | QTD_HORAS | NUMBER(7,2) | Y |  |  |
| 11 | VLR_VERBA | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 15 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 16 | TP_RENDIMENTO | VARCHAR2(3) | Y |  |  |
| 17 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA, DATA_PAGTO

**FKs**:
- IDENT_VERBA → X2023_VERBAS(IDENT_VERBA)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)

**Indexes**:
- IX_X21_FICHA_FINAN: (COD_EMPRESA, COD_FUNC, VALID_FUNC, ANO_COMPETENCIA, MES_COMPETENCIA, IND_FOLHA, IDENT_VERBA)

---

## X221_SOCIEDADE_UNIPROF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REFER | DATE | N |  |  |
| 4 | VLR_REC_AUFER | NUMBER(17,2) | Y |  |  |
| 5 | QTDE_PROF_HAB | NUMBER(6) | Y |  |  |
| 6 | VLR_ISS_RECOLHER | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REFER

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X222_PROFISSIONAL_HABIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REFER | DATE | N |  |  |
| 4 | NUM_CPF | VARCHAR2(11) | N |  |  |
| 5 | IND_HABILITACAO | CHAR(1) | Y |  |  |
| 6 | IND_ESCOLARIDADE | CHAR(1) | Y |  |  |
| 7 | IND_PARTIC_SOCIET | CHAR(1) | Y |  |  |
| 8 | DSC_NOME_PROF | VARCHAR2(60) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REFER, NUM_CPF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X223_GUIA_RECOL_DIFAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DAT_APURACAO | DATE | N |  |  |
| 5 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 6 | NUM_GUIA_RECOL | VARCHAR2(30) | N |  |  |
| 7 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 8 | DAT_VENCTO | DATE | Y |  |  |
| 9 | MES_ANO_REF | DATE | Y |  |  |
| 10 | COD_OBRIGACAO | VARCHAR2(3) | N |  |  |
| 11 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 12 | DSC_COMPLEMENTAR | VARCHAR2(250) | Y |  |  |
| 13 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 14 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 15 | DSC_PROC | VARCHAR2(250) | Y |  |  |
| 16 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 17 | COD_DEB_ICMS | NUMBER(3) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 20 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_GUIA_RECOL, COD_OBRIGACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO → APURACAO(COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DAT_APURACAO)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)
- COD_DEB_ICMS → ICT_COD_DEB_ICMS(COD_DEB_ICMS)

---

## X224_GUIA_REC_DIFAL_IES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | INSC_ESTADUAL | VARCHAR2(14) | N |  |  |
| 4 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 5 | DAT_APURACAO | DATE | N |  |  |
| 6 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 7 | NUM_GUIA_RECOL | VARCHAR2(30) | N |  |  |
| 8 | VAL_GUIA_RECOL | NUMBER(17,2) | Y |  |  |
| 9 | DAT_VENCTO | DATE | Y |  |  |
| 10 | MES_ANO_REF | DATE | Y |  |  |
| 11 | COD_OBRIGACAO | VARCHAR2(3) | Y |  |  |
| 12 | IDENT_RECEITA_EST | NUMBER(12) | Y |  |  |
| 13 | DSC_COMPLEMENTAR | VARCHAR2(250) | Y |  |  |
| 14 | NUM_PROC | VARCHAR2(60) | Y |  |  |
| 15 | ORIGEM_PROC | CHAR(1) | Y |  |  |
| 16 | DSC_PROC | VARCHAR2(250) | Y |  |  |
| 17 | COD_CLASSE_VENC | VARCHAR2(5) | Y |  |  |
| 18 | COD_DEB_ICMS | NUMBER(3) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO, IDENT_ESTADO, NUM_GUIA_RECOL

**FKs**:
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO → ICT_APUR_INSC_EST(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL, COD_TIPO_LIVRO, DAT_APURACAO)
- IDENT_RECEITA_EST → X2080_COD_REC_UF(IDENT_RECEITA_EST)
- COD_DEB_ICMS → ICT_COD_DEB_ICMS(COD_DEB_ICMS)

---

## X225_CONTABIL_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_OPERACAO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | VLR_LANCTO | NUMBER(19,2) | Y |  |  |
| 8 | IDENT_CONTRA_PART | NUMBER(12) | Y |  |  |
| 9 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_HISTPADRAO | NUMBER(12) | Y |  |  |
| 11 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 12 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 13 | TIPO_LANCTO | CHAR(1) | Y |  |  |
| 14 | IDENT_PFJ_VINC | NUMBER(12) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | DAT_LANCTO_EXTEMP | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_OPERACAO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTRA_PART → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_HISTPADRAO → X2020_HIST_PADRAO(IDENT_HISTPADRAO)
- IDENT_PFJ_VINC → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_2929: (IDENT_PFJ_VINC)
- IX_X225_CONTABIL_CTA: (IDENT_CONTA)
- IX_X225_CONTABIL_CTA_PART: (IDENT_CONTRA_PART)

---

## X226_SALDOS_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_OPERACAO | DATE | N |  |  |
| 5 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | NUMBER(19,2) | Y |  |  |
| 8 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 9 | VLR_TOT_CRE | NUMBER(19,2) | Y |  |  |
| 10 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X226_SALDOS_CTA: (IDENT_CONTA)

---

## X227_SALDOS_CCUSTO_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_SALDO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 6 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 7 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 8 | VLR_SALDO_FIM | NUMBER(19,2) | Y |  |  |
| 9 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 10 | VLR_TOT_CRE | NUMBER(19,2) | Y |  |  |
| 11 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_CUSTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)

**Indexes**:
- IX_X227_SALDOS_CCUSTO_CTA: (IDENT_CONTA)

---

## X228_CONTABIL_AUX_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_OPERACAO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 6 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 7 | VLR_LANCTO | NUMBER(19,2) | Y |  |  |
| 8 | IDENT_CONTRA_PART | NUMBER(12) | Y |  |  |
| 9 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_HISTPADRAO | NUMBER(12) | Y |  |  |
| 11 | HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 12 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  |  |
| 13 | TIPO_LANCTO | CHAR(1) | Y |  |  |
| 14 | IDENT_PFJ_VINC | NUMBER(12) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | DAT_LANCTO_EXTEMP | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_OPERACAO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTRA_PART → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_HISTPADRAO → X2020_HIST_PADRAO(IDENT_HISTPADRAO)
- IDENT_PFJ_VINC → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_2930: (IDENT_PFJ_VINC)
- IX_X228_CONTABIL_AUX_CTA: (IDENT_CONTA)
- IX_X228_CONTABIL_CTA_PART: (IDENT_CONTRA_PART)

---

## X229_SALDOS_AUX_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_OPERACAO | DATE | N |  |  |
| 5 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 6 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | NUMBER(19,2) | Y |  |  |
| 8 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 9 | VLR_TOT_CRE | NUMBER(19,2) | Y |  |  |
| 10 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X229_SALDOS_AUX_CTA: (IDENT_CONTA)

---

## X22_INF_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | NUM_OCOR | CHAR(1) | N |  |  |
| 5 | DAT_OCOR | DATE | N |  |  |
| 6 | IND_TIPO | CHAR(1) | Y |  |  |
| 7 | CPF | VARCHAR2(11) | Y |  |  |
| 8 | NOME | VARCHAR2(50) | Y |  |  |
| 9 | VLR_PENSAO | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROC_JUD | VARCHAR2(15) | Y |  |  |
| 11 | DAT_DECISAO | DATE | Y |  |  |
| 12 | TRIB_JUST | VARCHAR2(5) | Y |  |  |
| 13 | VARA_JUDICIAL | VARCHAR2(2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 16 | VLR_PENSAO_13 | NUMBER(17,2) | Y |  | Valor da pensão sobre o 13 salário |
| 17 | DSC_OUTROS | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, NUM_OCOR, DAT_OCOR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X230_TRANSF_SD_CONTA_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | DATA_OPERACAO | DATE | N |  |  |
| 5 | IDENT_CONTA_ANT | NUMBER(12) | N |  |  |
| 6 | IDENT_CUSTO_ANT | NUMBER(12) | Y |  |  |
| 7 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 8 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTA_ANT → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO_ANT → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_OPERACAO → X226_SALDOS_FUNC(COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_OPERACAO)

**Indexes**:
- IX_X230_TRANSF_SD_CTA: (IDENT_CONTA)
- IX_X230_TRANSF_SD_CTA_ANT: (IDENT_CONTA_ANT)
- UK_X230_TRANSF_SD_CONTA_FUNC (UNIQUE): (COD_EMPRESA, COD_ESTAB, IDENT_CONTA, DATA_OPERACAO, IDENT_CONTA_ANT, IDENT_CUSTO_ANT)

---

## X231_TRANSF_SD_CUSTO_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 5 | DATA_OPERACAO | DATE | N |  |  |
| 6 | IDENT_CONTA_ANT | NUMBER(12) | N |  |  |
| 7 | IDENT_CUSTO_ANT | NUMBER(12) | N |  |  |
| 8 | VLR_SALDO_INI | NUMBER(19,2) | Y |  |  |
| 9 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, IDENT_CUSTO, DATA_OPERACAO, IDENT_CONTA_ANT, IDENT_CUSTO_ANT

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_CONTA_ANT → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO_ANT → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- COD_EMPRESA, COD_ESTAB, DATA_OPERACAO, IDENT_CONTA, IDENT_CUSTO → X227_SALDOS_CCUSTO_FUNC(COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_CUSTO)

**Indexes**:
- IX_X231_TRANSF_SD_CTA: (IDENT_CONTA)
- IX_X231_TRANSF_SD_CTA_ANT: (IDENT_CONTA_ANT)

---

## X232_SALDO_ANTES_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 4 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 5 | DATA_SALDO | DATE | N |  |  |
| 6 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 7 | VLR_SALDO_FIM | NUMBER(19,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_CONTA, IDENT_CUSTO, DATA_SALDO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)

**Indexes**:
- IX_X232_SALDO_ANTES_CTA: (IDENT_CONTA)

---

## X233_BEM_EXTEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | COD_BEM | VARCHAR2(60) | N |  |  |
| 5 | COD_INC | VARCHAR2(6) | N |  |  |
| 6 | DATA_ATIV_BEM | DATE | Y |  |  |
| 7 | IND_TIPO_MOV | VARCHAR2(2) | Y |  |  |
| 8 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS_DIFAL | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PARCELA | NUMBER(3) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | DATA_BAIXA | DATE | Y |  |  |
| 16 | IND_TIPO_BAIXA | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_BEM, COD_INC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X234_BEM_EXTEMP_NF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | COD_BEM | VARCHAR2(60) | N |  |  |
| 5 | COD_INC | VARCHAR2(6) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | DATA_EMISSAO | DATE | N |  |  |
| 10 | NUM_ITEM | NUMBER(5) | N |  |  |
| 11 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 12 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 13 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 16 | IND_E_S | CHAR(1) | Y | 'E' |  |
| 17 | NUM_DOC_ARREC | VARCHAR2(50) | Y |  |  |
| 18 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 19 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 20 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 22 | VLR_ICMS_FRETE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ICMS_DIFAL | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_BEM, COD_INC, IDENT_FIS_JUR, DATA_EMISSAO, NUM_DOCFIS, SERIE_DOCFIS, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_BEM, COD_INC → X233_BEM_EXTEMP(COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_BEM, COD_INC)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_SAF_2935: (IDENT_FIS_JUR)

---

## X235_CAPA_COR_APONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | N |  |  |
| 4 | IND_TP_CORRECAO | VARCHAR2(2) | N |  |  |
| 5 | IDENT_PRODUTO_OP | NUMBER(12) | N |  |  |
| 6 | DAT_INI_APUR | DATE | N |  |  |
| 7 | DAT_FIM_APUR | DATE | N |  |  |
| 8 | COD_OP | VARCHAR2(30) | N |  |  |
| 9 | COD_DIF_PRODUCAO | VARCHAR2(15) | N |  |  |
| 10 | DAT_ESTQ_FIM | DATE | N |  |  |
| 11 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 13 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 14 | QTD_CORRECAO | NUMBER(17,6) | Y |  |  |
| 15 | IND_POS_NEG | CHAR(1) | Y |  |  |
| 16 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REF, IND_TP_CORRECAO, IDENT_PRODUTO_OP, DAT_INI_APUR, DAT_FIM_APUR, COD_OP, COD_DIF_PRODUCAO, DAT_ESTQ_FIM, GRUPO_CONTAGEM, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO_OP → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## X236_ITEM_COR_APONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | N |  |  |
| 4 | IND_TP_CORRECAO | VARCHAR2(2) | N |  |  |
| 5 | IDENT_PRODUTO_OP | NUMBER(12) | N |  |  |
| 6 | DAT_INI_APUR | DATE | N |  |  |
| 7 | DAT_FIM_APUR | DATE | N |  |  |
| 8 | COD_OP | VARCHAR2(30) | N |  |  |
| 9 | COD_DIF_PRODUCAO | VARCHAR2(15) | N |  |  |
| 10 | DAT_ESTQ_FIM | DATE | N |  |  |
| 11 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 13 | IDENT_PRODUTO_INS | NUMBER(12) | N |  |  |
| 14 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 15 | QTD_CORRECAO | NUMBER(17,6) | Y |  |  |
| 16 | IND_POS_NEG | CHAR(1) | Y |  |  |
| 17 | IDENT_PRODUTO_SUBST | NUMBER(12) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REF, IND_TP_CORRECAO, IDENT_PRODUTO_OP, DAT_INI_APUR, DAT_FIM_APUR, COD_OP, COD_DIF_PRODUCAO, DAT_ESTQ_FIM, GRUPO_CONTAGEM, IDENT_FIS_JUR, IDENT_PRODUTO_INS

**FKs**:
- COD_EMPRESA, COD_ESTAB, PERIODO_REF, IND_TP_CORRECAO, IDENT_PRODUTO_OP, DAT_INI_APUR, DAT_FIM_APUR, COD_OP, COD_DIF_PRODUCAO, DAT_ESTQ_FIM, GRUPO_CONTAGEM, IDENT_FIS_JUR → X235_CAPA_COR_APONT(COD_EMPRESA, COD_ESTAB, PERIODO_REF, IND_TP_CORRECAO, IDENT_PRODUTO_OP, DAT_INI_APUR, DAT_FIM_APUR, COD_OP, COD_DIF_PRODUCAO, DAT_ESTQ_FIM, GRUPO_CONTAGEM, IDENT_FIS_JUR)
- IDENT_PRODUTO_INS → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_PRODUTO_SUBST → X2013_PRODUTO(IDENT_PRODUTO)

---

## X23_PRODUTO_EAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | COD_EAN | VARCHAR2(14) | N |  |  |
| 5 | DAT_VALIDADE | DATE | Y |  |  |
| 6 | TIPO_COD_EAN | VARCHAR2(5) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, COD_EAN

**FKs**:
- TIPO_COD_EAN → DWT_TP_COD_EAN(TIPO_COD_EAN)

---

## X240_INF_EMPRESA_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_CONS | DATE | N |  |  |
| 4 | DATA_FIM_CONS | DATE | N |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | N |  |  |
| 6 | NOME_EMP_PART | VARCHAR2(100) | Y |  |  |
| 7 | CNPJ | VARCHAR2(14) | Y |  |  |
| 8 | IND_EVENTO | CHAR(1) | Y |  |  |
| 9 | PERC_PART_TOT | NUMBER(8,4) | Y |  |  |
| 10 | PERC_CONS | NUMBER(8,4) | Y |  |  |
| 11 | DATA_INI_EMP | DATE | Y |  |  |
| 12 | DATA_FIM_EMP | DATE | Y |  |  |
| 13 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI_CONS, DATA_FIM_CONS, COD_EMP_PART

**FKs**:
- COD_PAIS → PAIS(COD_PAIS)

---

## X241_INF_EMPRESA_PART

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INI_CONS | DATE | N |  |  |
| 4 | DATA_FIM_CONS | DATE | N |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | N |  |  |
| 6 | IND_EVENTO_OPER | CHAR(1) | N |  |  |
| 7 | COD_EMP_OPER | VARCHAR2(4) | N |  |  |
| 8 | DATA_EVENTO | DATE | Y |  |  |
| 9 | IND_COND_PART | CHAR(1) | Y |  |  |
| 10 | PERC_PART_EMP | NUMBER(8,4) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INI_CONS, DATA_FIM_CONS, COD_EMP_PART, IND_EVENTO_OPER, COD_EMP_OPER

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_INI_CONS, DATA_FIM_CONS, COD_EMP_PART → X240_INF_EMPRESA_CONS(COD_EMPRESA, COD_ESTAB, DATA_INI_CONS, DATA_FIM_CONS, COD_EMP_PART)

---

## X242_SALDO_CONTA_CONS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO_CONS | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | VLR_AGLUTINADO | NUMBER(19,2) | Y |  |  |
| 6 | IND_AGLUTINADO | CHAR(1) | Y |  |  |
| 7 | VLR_ELIMINACAO | NUMBER(19,2) | Y |  |  |
| 8 | IND_ELIMINACAO | CHAR(1) | Y |  |  |
| 9 | VLR_CONSOLIDADO | NUMBER(19,2) | Y |  |  |
| 10 | IND_CONSOLIDADO | CHAR(1) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO_CONS, IDENT_CONTA

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X242_SALDO_CONTA_CTA: (IDENT_CONTA)

---

## X243_PARCELA_VLR_ELIMINADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO_CONS | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | N |  |  |
| 6 | VLR_ELIMINADO_TOT | NUMBER(19,2) | Y |  |  |
| 7 | IND_ELIMINADO_TOT | CHAR(1) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO_CONS, IDENT_CONTA, COD_EMP_PART

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_SALDO_CONS, IDENT_CONTA → X242_SALDO_CONTA_CONS(COD_EMPRESA, COD_ESTAB, DATA_SALDO_CONS, IDENT_CONTA)

---

## X244_CONTRAPART_VLR_ELIM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO_CONS | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | COD_EMP_PART | VARCHAR2(4) | N |  |  |
| 6 | COD_EMP_CONTRAP | VARCHAR2(4) | N |  |  |
| 7 | IDENT_CONTA_CONTRAP | NUMBER(12) | N |  |  |
| 8 | VLR_CONTRAPARTIDA | NUMBER(19,2) | Y |  |  |
| 9 | IND_CONTRAPARTIDA | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO_CONS, IDENT_CONTA, COD_EMP_PART, COD_EMP_CONTRAP, IDENT_CONTA_CONTRAP

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_SALDO_CONS, IDENT_CONTA, COD_EMP_PART → X243_PARCELA_VLR_ELIMINADO(COD_EMPRESA, COD_ESTAB, DATA_SALDO_CONS, IDENT_CONTA, COD_EMP_PART)
- IDENT_CONTA_CONTRAP → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X244_CONTRAPART_VLR_CTA: (IDENT_CONTA_CONTRAP)

---

## X246_SERV_PREST_ECOMM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_OPERACAO | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | IND_TP_SERVICO | VARCHAR2(4) | N |  |  |
| 6 | COD_OPERACAO | VARCHAR2(60) | N |  |  |
| 7 | DSC_PRODUTO | VARCHAR2(150) | Y |  |  |
| 8 | VLR_TOT_OP | NUMBER(17,2) | Y |  |  |
| 9 | IND_TP_PAGTO | VARCHAR2(2) | Y |  |  |
| 10 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 11 | DAT_INI_CONTRATO | DATE | Y |  |  |
| 12 | DAT_FIM_CONTRATO | DATE | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | IND_COMISSAO | VARCHAR2(1) | Y |  |  |
| 16 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 17 | QUANTIDADE | NUMBER(15,4) | Y |  |  |
| 18 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 19 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_OPERACAO, IDENT_FIS_JUR, IND_TP_SERVICO, COD_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_3064: (IDENT_FIS_JUR)

---

## X247_PAG_AUTONOMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMP | NUMBER(4) | N |  |  |
| 4 | MES_COMP | NUMBER(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | ID_DEM_PAG | VARCHAR2(30) | N |  |  |
| 7 | IND_DESCONTO | CHAR(1) | Y |  |  |
| 8 | IND_PAG_TOTAL | CHAR(1) | Y |  |  |
| 9 | DAT_PAG | DATE | Y |  |  |
| 10 | TIPO_PAG | VARCHAR2(2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | IDENT_CBO | NUMBER(12) | Y |  |  |
| 14 | IDENT_SETOR | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_SETOR → X2037_SETOR(IDENT_SETOR)
- IDENT_CBO → X2029_COD_CBO(IDENT_CBO)

**Indexes**:
- IX_FK_SAF_3094: (IDENT_FIS_JUR)

---

## X248_PAG_AUTONOMO_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMP | NUMBER(4) | N |  |  |
| 4 | MES_COMP | NUMBER(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | ID_DEM_PAG | VARCHAR2(30) | N |  |  |
| 7 | IDENT_RUBRICA | NUMBER(12) | N |  |  |
| 8 | QTDE_REF | NUMBER(6,2) | Y |  |  |
| 9 | FATOR_CALC | NUMBER(5,2) | Y |  |  |
| 10 | VLR_UNIT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 12 | IND_TP_PROC_ADJ | CHAR(1) | Y |  |  |
| 13 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 14 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG, IDENT_RUBRICA

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG → X247_PAG_AUTONOMO(COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG)
- IDENT_RUBRICA → X2114_CAD_RUBRICA(IDENT_RUBRICA)
- IDENT_PROC_ADJ → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT → X2059_SUSP_TBT(IDENT_SUSP_TBT)

---

## X249_PAG_AUTONOMO_PARCIAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMP | NUMBER(4) | N |  |  |
| 4 | MES_COMP | NUMBER(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | ID_DEM_PAG | VARCHAR2(30) | N |  |  |
| 7 | DAT_PAG | DATE | N |  |  |
| 8 | IDENT_RUBRICA | NUMBER(12) | N |  |  |
| 9 | TIPO_PAG | VARCHAR2(2) | N |  |  |
| 10 | QTDE_REF | NUMBER(6,2) | N |  |  |
| 11 | FATOR_CALC | NUMBER(5,2) | N |  |  |
| 12 | VLR_UNIT | NUMBER(17,2) | N |  |  |
| 13 | VLR_TOT | NUMBER(17,2) | N |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG, DAT_PAG, IDENT_RUBRICA, TIPO_PAG

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG → X247_PAG_AUTONOMO(COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG)
- IDENT_RUBRICA → X2114_CAD_RUBRICA(IDENT_RUBRICA)

---

## X24_CONV_MEDIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | GRUPO_UND_PAD | VARCHAR2(9) | N |  |  |
| 5 | COD_UND_PAD_ORIG | VARCHAR2(8) | N |  |  |
| 6 | COD_UND_PAD_DEST | VARCHAR2(8) | Y |  |  |
| 7 | VLR_FATOR_CONV | NUMBER(17,6) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_UND_PAD, COD_UND_PAD_ORIG

---

## X250_OUTROS_VINCULOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_COMP | NUMBER(4) | N |  |  |
| 4 | MES_COMP | NUMBER(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | ID_DEM_PAG | VARCHAR2(30) | N |  |  |
| 7 | CPF_CNPJ_EMPREGADOR | VARCHAR2(14) | N |  |  |
| 8 | COD_CATEG_TRAB | VARCHAR2(3) | N |  |  |
| 9 | VLR_REMUNERACAO | NUMBER(17,2) | N |  |  |
| 10 | VLR_RET | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG, CPF_CNPJ_EMPREGADOR, COD_CATEG_TRAB

**FKs**:
- COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG → X247_PAG_AUTONOMO(COD_EMPRESA, COD_ESTAB, ANO_COMP, MES_COMP, IDENT_FIS_JUR, ID_DEM_PAG)
- COD_CATEG_TRAB → PRT_CATEG_TRAB_ESOCIAL(COD_CATEG_TRAB)

---

## X251_CONTRIB_SINDICAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REF | NUMBER(4) | N |  |  |
| 4 | MES_REF | NUMBER(2) | N |  |  |
| 5 | IDENT_SINDICATO | NUMBER(12) | N |  |  |
| 6 | TP_CONTRIB | CHAR(1) | N |  |  |
| 7 | VLR_CONTRIB | NUMBER(17,2) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REF, MES_REF, IDENT_SINDICATO, TP_CONTRIB

**FKs**:
- IDENT_SINDICATO → X2048_SINDICATO(IDENT_SINDICATO)

---

## X253_TERM_TELEFONICO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_TERMINAL_TEL | VARCHAR2(15) | N |  |  |
| 9 | VLR_TOT_FATURA | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | IDENT_UF_TERMINAL_TEL | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_TERMINAL_TEL

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X42_CAPA_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_UF_TERMINAL_TEL → ESTADO(IDENT_ESTADO)

---

## X254_TERM_TEL_NFE

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
| 11 | NUM_TERMINAL_TEL | VARCHAR2(15) | N |  |  |
| 12 | VLR_TOT_FATURA | NUMBER(17,2) | Y |  |  |
| 13 | IDENT_ESTADO_TERMINAL | NUMBER(12) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_TERMINAL_TEL

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_ESTADO_TERMINAL → ESTADO(IDENT_ESTADO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X257_NOTA_EXPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_BALANCO_DRE | CHAR(1) | N |  |  |
| 4 | COD_CONTA_AGLUT | VARCHAR2(70) | N |  |  |
| 5 | DATA_DEMONSTRACAO | DATE | N |  |  |
| 6 | NOTA_EXPLICATIVA | VARCHAR2(255) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | NUM_REFERENCIA | VARCHAR2(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_BALANCO_DRE, COD_CONTA_AGLUT, DATA_DEMONSTRACAO

---

## X259_FATURA_TELECOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_FAT_COM | VARCHAR2(20) | N |  |  |
| 4 | DATA_EMISSAO | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | VLR_TOT_FAT | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 12 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 13 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 14 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 15 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 16 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_FAT_COM, DATA_EMISSAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_3109: (IDENT_FIS_JUR)

---

## X259_FATURA_TELECOM_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_FAT_COM | VARCHAR2(20) | N |  |  |
| 4 | DATA_EMISSAO | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | VLR_TOT_FAT | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 9 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 12 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 13 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 14 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 15 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 16 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

---

## X260_ITEM_FATURA_TELECOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_FAT_COM | VARCHAR2(20) | N |  |  |
| 4 | DATA_EMISSAO | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | NUM_ITEM | NUMBER(7) | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 8 | IND_ORIGEM_ITEM | CHAR(1) | Y |  |  |
| 9 | IDENT_FIS_JUR_TERC | NUMBER(12) | Y |  |  |
| 10 | DATA_EMISSAO_NF | DATE | Y |  |  |
| 11 | IDENT_MODELO_NF | NUMBER(12) | Y |  |  |
| 12 | SERIE_NF | VARCHAR2(3) | Y |  |  |
| 13 | NUMERO_NF | VARCHAR2(12) | Y |  |  |
| 14 | VLR_TOT_NF | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 18 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 21 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 22 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_FAT_COM, DATA_EMISSAO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, NUM_FAT_COM, DATA_EMISSAO → X259_FATURA_TELECOM(COD_EMPRESA, COD_ESTAB, NUM_FAT_COM, DATA_EMISSAO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_FIS_JUR_TERC → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO_NF → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_3112: (IDENT_FIS_JUR_TERC)
- IX_FK_SAF_3223: (IDENT_FIS_JUR)

---

## X260_ITEM_FATURA_TELECOM_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_FAT_COM | VARCHAR2(20) | N |  |  |
| 4 | DATA_EMISSAO | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_ITEM | NUMBER(7) | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 8 | IND_ORIGEM_ITEM | CHAR(1) | Y |  |  |
| 9 | IDENT_FIS_JUR_TERC | NUMBER(12) | Y |  |  |
| 10 | DATA_EMISSAO_NF | DATE | Y |  |  |
| 11 | IDENT_MODELO_NF | NUMBER(12) | Y |  |  |
| 12 | SERIE_NF | VARCHAR2(3) | Y |  |  |
| 13 | NUMERO_NF | VARCHAR2(12) | Y |  |  |
| 14 | VLR_TOT_NF | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 21 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 22 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

---

## X261_CRED_TERMINAL_TEL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 5 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 6 | NUM_TERMINAL | VARCHAR2(15) | N |  |  |
| 7 | IDENT_FIS_JUR_USU | NUMBER(12) | N |  |  |
| 8 | DATA_RECARGA | DATE | N |  |  |
| 9 | DISCR_PRODUTO | VARCHAR2(80) | N | ' ' | Campo concatenado com indicador e cï¿½digo do produto  |
| 10 | IDENT_FIS_JUR_VEND | NUMBER(12) | Y |  |  |
| 11 | IDENT_FIS_JUR_RESP | NUMBER(12) | Y |  |  |
| 12 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 13 | VLR_TOT_RECARGA | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_ANTEC_CRED | NUMBER(17,2) | Y |  |  |
| 16 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_TERMINAL, IDENT_FIS_JUR_USU, DATA_RECARGA, DISCR_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR_USU → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_VEND → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_RESP → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_SAF_3115: (IDENT_FIS_JUR_USU)
- IX_FK_SAF_3116: (IDENT_FIS_JUR_VEND)
- IX_FK_SAF_3117: (IDENT_FIS_JUR_RESP)

---

## X261_CRED_TERMINAL_TEL_BKP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_TERMINAL | VARCHAR2(15) | N |  |  |
| 4 | IDENT_FIS_JUR_USU | NUMBER(12) | N |  |  |
| 5 | DATA_RECARGA | DATE | N |  |  |
| 6 | IDENT_FIS_JUR_VEND | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR_RESP | NUMBER(12) | Y |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 9 | VLR_TOT_RECARGA | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ANTEC_CRED | NUMBER(17,2) | Y |  |  |
| 12 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | DISCR_PRODUTO | VARCHAR2(80) | N |  |  |

---

## X263_DOCTO_PROC_SUSP

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
| 11 | IND_TP_PROC_ADJ | CHAR(1) | N |  |  |
| 12 | IDENT_PROC_ADJ | NUMBER(12) | N |  |  |
| 13 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 14 | VLR_PREV_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 15 | VLR_GIBRAT_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 16 | VLR_SENAR_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 19 | IND_EVENTO | CHAR(1) | N | '5' |  |
| 20 | IND_PRINC_ADIC | CHAR(1) | N | ' ' |  |
| 21 | VLR_N_RET | NUMBER(17,2) | Y |  |  |
| 22 | IND_TP_PROC_JUD | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_TP_PROC_ADJ, IDENT_PROC_ADJ, IND_EVENTO, IND_PRINC_ADIC

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_PROC_ADJ → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT → X2059_SUSP_TBT(IDENT_SUSP_TBT)

**Indexes**:
- IX_FK_SAF_3119: (IDENT_FIS_JUR)

---

## X264_DET_AJ_BC_VAL_EXTRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APUR | DATE | N |  |  |
| 4 | DATA_REFER | DATE | N |  |  |
| 5 | IND_NATUREZA | VARCHAR2(2) | N |  |  |
| 6 | IND_APROP_AJUSTE | VARCHAR2(2) | N |  |  |
| 7 | CNPJ | VARCHAR2(14) | N |  |  |
| 8 | VLR_TOT_AJUSTE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_AJ_CST01 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_AJ_CST02 | NUMBER(17,2) | Y |  |  |
| 11 | VLR_AJ_CST03 | NUMBER(17,2) | Y |  |  |
| 12 | VLR_AJ_CST04 | NUMBER(17,2) | Y |  |  |
| 13 | VLR_AJ_CST05 | NUMBER(17,2) | Y |  |  |
| 14 | VLR_AJ_CST06 | NUMBER(17,2) | Y |  |  |
| 15 | VLR_AJ_CST07 | NUMBER(17,2) | Y |  |  |
| 16 | VLR_AJ_CST08 | NUMBER(17,2) | Y |  |  |
| 17 | VLR_AJ_CST09 | NUMBER(17,2) | Y |  |  |
| 18 | VLR_AJ_CST49 | NUMBER(17,2) | Y |  |  |
| 19 | VLR_AJ_CST99 | NUMBER(17,2) | Y |  |  |
| 20 | NUM_RECIBO | VARCHAR2(80) | Y |  |  |
| 21 | DSC_INF_COMPL | VARCHAR2(100) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APUR, DATA_REFER, IND_NATUREZA, IND_APROP_AJUSTE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X265_SALDO_INI_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_SALDO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | QTD_SALDO | NUMBER(17,3) | Y |  |  |
| 6 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 7 | VLR_UNIT | NUMBER(19,6) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | VLR_RESSARC | NUMBER(17,2) | Y |  |  |
| 11 | VLR_COMPL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ICMS_PROP | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_SALDO, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## X266_PRODUCAO_CONJUNTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REFER | DATE | N |  |  |
| 4 | IND_PROD_CONJ | CHAR(1) | N |  |  |
| 5 | DATA_PROD | DATE | N |  |  |
| 6 | COD_OP | VARCHAR2(30) | N |  |  |
| 7 | DATA_INI_OP | DATE | N |  |  |
| 8 | DATA_FIM_OP | DATE | Y |  |  |
| 9 | IND_INDUST_TERC | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REFER, IND_PROD_CONJ, DATA_PROD, COD_OP, DATA_INI_OP

---

## X267_ITEM_PRODUZIDO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REFER | DATE | N |  |  |
| 4 | IND_PROD_CONJ | CHAR(1) | N |  |  |
| 5 | DATA_PROD | DATE | N |  |  |
| 6 | COD_OP | VARCHAR2(30) | N |  |  |
| 7 | DATA_INI_OP | DATE | N |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 9 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REFER, IND_PROD_CONJ, DATA_PROD, COD_OP, DATA_INI_OP, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, PERIODO_REFER, IND_PROD_CONJ, DATA_PROD, COD_OP, DATA_INI_OP → X266_PRODUCAO_CONJUNTA(COD_EMPRESA, COD_ESTAB, PERIODO_REFER, IND_PROD_CONJ, DATA_PROD, COD_OP, DATA_INI_OP)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## X268_ITEM_CONSUMIDO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REFER | DATE | N |  |  |
| 4 | IND_PROD_CONJ | CHAR(1) | N |  |  |
| 5 | DATA_PROD | DATE | N |  |  |
| 6 | COD_OP | VARCHAR2(30) | N |  |  |
| 7 | DATA_INI_OP | DATE | N |  |  |
| 8 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 9 | QTDE_CONS | NUMBER(17,6) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_REFER, IND_PROD_CONJ, DATA_PROD, COD_OP, DATA_INI_OP, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, PERIODO_REFER, IND_PROD_CONJ, DATA_PROD, COD_OP, DATA_INI_OP → X266_PRODUCAO_CONJUNTA(COD_EMPRESA, COD_ESTAB, PERIODO_REFER, IND_PROD_CONJ, DATA_PROD, COD_OP, DATA_INI_OP)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## X269_SERV_PREST_FINANC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_APUR | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IDENT_COSIF | NUMBER(12) | N |  |  |
| 6 | IDENT_SERV_LEI_116 | NUMBER(12) | N |  |  |
| 7 | VLR_ALIQ_ISS | NUMBER(7,4) | N |  |  |
| 8 | QTD_OCOR | NUMBER(5) | Y |  |  |
| 9 | VLR_CONTABIL | NUMBER(17,2) | Y |  |  |
| 10 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 12 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_APUR, IDENT_CONTA, IDENT_COSIF, IDENT_SERV_LEI_116, VLR_ALIQ_ISS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_SERV_LEI_116 → DWT_SERVICO_LEI_116(IDENT_SERV_LEI_116)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_3143: (IDENT_OBSERVACAO)
- IX_X269_SERV_PREST_CTA: (IDENT_CONTA)

---

## X26_SALDOS_EST_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_SALDO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | QTD_SALDO | NUMBER(13,3) | Y |  |  |
| 6 | VLR_TOT | NUMBER(13,2) | Y |  |  |
| 7 | VLR_UNIT | NUMBER(15,4) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 11 | VLR_TOT_ICMS | NUMBER(13,2) | Y |  |  |
| 12 | VLR_UNIT_BC_ICMS | NUMBER(15,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_PRODUTO

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_X26_SALDOS_EST_ST_01: (IDENT_PRODUTO)

---

## X270_DEDUCAO_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_APUR | DATE | N |  |  |
| 4 | IND_TIPO_DED | VARCHAR2(1) | N |  |  |
| 5 | IND_OBRIG | VARCHAR2(1) | N |  |  |
| 6 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROC | VARCHAR2(24) | Y |  |  |
| 8 | ORIGEM_PROC | VARCHAR2(1) | Y |  |  |
| 9 | DSC_PROC | VARCHAR2(50) | Y |  |  |
| 10 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, PERIODO_APUR, IND_TIPO_DED, IND_OBRIG

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_3145: (IDENT_OBSERVACAO)

---

## X271_RURAL_PROC_SUSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 5 | TIPO_MOV_ES | CHAR(1) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 11 | IDENT_PROC_ADJ | NUMBER(12) | N |  |  |
| 12 | IDENT_SUSP_TBT | NUMBER(12) | N |  |  |
| 13 | VLR_CONT_PREV_N_RET | NUMBER(17,2) | Y |  |  |
| 14 | VLR_GILRAT_N_RET | NUMBER(17,2) | Y |  |  |
| 15 | VLR_SENAR_N_RET | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 18 | IND_TP_PROC_JUD | VARCHAR2(1) | Y | '1' |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_DOCTO, TIPO_MOV_ES, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, IDENT_PROC_ADJ, IDENT_SUSP_TBT

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_DOCTO, TIPO_MOV_ES, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO → X63_FUNRURAL(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_DOCTO, TIPO_MOV_ES, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_PROC_ADJ → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_SAF_3148: (IDENT_FIS_JUR)

---

## X272_PAR_PROD_E115

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO | VARCHAR2(9) | N |  |  |
| 4 | IND_PRODUTO | CHAR(1) | N |  |  |
| 5 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 6 | DATA_INI | DATE | N |  |  |
| 7 | DATA_FIM | DATE | Y |  |  |
| 8 | COD_INF_ADIC | VARCHAR2(8) | N |  |  |
| 9 | DSC_COMPL | VARCHAR2(200) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, GRUPO, IND_PRODUTO, COD_PRODUTO, DATA_INI, COD_INF_ADIC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_INF_ADIC → EFD_INF_ADIC_APUR(COD_INF_ADIC)

---

## X275_DEPENDENTES_S_VINC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 2 | IDENT_DEP_FIS_JUR | NUMBER(12) | N |  |  |
| 3 | DAT_VIG_INI | DATE | N |  |  |
| 4 | DAT_VIG_FIM | DATE | Y |  |  |
| 5 | CPF_DEP | VARCHAR2(11) | N |  |  |
| 6 | NOME_DEP | VARCHAR2(60) | N |  |  |
| 7 | DAT_NASC_DEP | DATE | N |  |  |
| 8 | IND_REL_DEP | VARCHAR2(2) | N |  |  |
| 9 | DSC_DEP | VARCHAR2(60) | Y |  |  |
| 10 | IND_PENSAO | VARCHAR2(1) | Y | 'N' |  |
| 11 | IND_PLANO | VARCHAR2(1) | Y | 'N' |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: IDENT_DEP_FIS_JUR

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_3159: (IDENT_FIS_JUR)
- UK_X275_DEPENDENTES_S_VINC (UNIQUE): (IDENT_FIS_JUR, DAT_VIG_INI, CPF_DEP)

---

## X276_MOV_BENEF_TITULAR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 2 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 3 | IND_MOVTO | VARCHAR2(1) | N |  |  |
| 4 | DATA_PAGTO | DATE | N |  |  |
| 5 | TP_INSC | VARCHAR2(1) | Y |  |  |
| 6 | NR_INSC | VARCHAR2(14) | N |  |  |
| 7 | VLR_DED_REND_TRIB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_REEMB_PER | NUMBER(17,2) | Y |  |  |
| 9 | VLR_REEMB_PER_ANT | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: IDENT_FIS_JUR, COD_OPER_SAUDE, DATA_PAGTO, IND_MOVTO, NR_INSC

**FKs**:
- COD_OPER_SAUDE → DWT_OPERADORA_SAUDE(COD_OPER_SAUDE)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_X276_TITULAR: (IDENT_FIS_JUR)

---

## X277_MOV_BENEF_DEPENDENTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_DEP_FIS_JUR | NUMBER(12) | N |  |  |
| 2 | COD_OPER_SAUDE | VARCHAR2(4) | N |  |  |
| 3 | IND_MOVTO | VARCHAR2(1) | N |  |  |
| 4 | DATA_PAGTO | DATE | N |  |  |
| 5 | TP_INSC | VARCHAR2(1) | Y |  |  |
| 6 | NR_INSC | VARCHAR2(14) | N |  |  |
| 7 | VLR_DED_REND_TRIB | NUMBER(17,2) | Y |  |  |
| 8 | VLR_REEMB_PER | NUMBER(17,2) | Y |  |  |
| 9 | VLR_REEMB_PER_ANT | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: IDENT_DEP_FIS_JUR, COD_OPER_SAUDE, DATA_PAGTO, IND_MOVTO, NR_INSC

**FKs**:
- IDENT_DEP_FIS_JUR → X275_DEPENDENTES_S_VINC(IDENT_DEP_FIS_JUR)
- COD_OPER_SAUDE → DWT_OPERADORA_SAUDE(COD_OPER_SAUDE)

---

## X279_RET_BENEF_NAO_IDENT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | Código da Empresa |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | Código do Estabelecimento |
| 3 | DAT_MOV | DATE | N |  | Data do fato gerador ou pagamento/crédito |
| 4 | COD_NAT_REND | VARCHAR2(5) | N |  | Natureza dos rendimentos pagos a beneficiários não identificados, conforme opções a seguir: 1 - Rendimentos do trabalho ou 9 - Demais rendimentos. |
| 5 | VLR_LIQ | NUMBER(17,2) | Y |  | Valor líquido do pagamento. |
| 6 | VLR_REAJ | NUMBER(17,2) | Y |  | Valor reajustado, considerado como valor bruto da base de cálculo do IRRF. |
| 7 | VLR_IR | NUMBER(17,2) | Y |  | Valor do Imposto de Renda Retido na Fonte |
| 8 | DESCR | VARCHAR2(200) | Y |  | Descrição do pagamento.  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 11 | DATA_ESCR_CONT | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_MOV, COD_NAT_REND

---

## X27_MOV_EST_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 9 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 10 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 11 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 12 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 13 | COD_COMPL_OP | VARCHAR2(2) | Y |  |  |
| 14 | VLR_BASE_RET | NUMBER(17,2) | Y |  |  |
| 15 | QTD_E_S | NUMBER(13,3) | Y |  |  |
| 16 | VLR_UNIT_SAIDA | NUMBER(18,4) | Y |  |  |
| 17 | VLR_SAI_USU_FINAL | NUMBER(17,2) | Y |  |  |
| 18 | VLR_NAO_RALIZ | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ISENTAS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_SAI_OUT_UF | NUMBER(17,2) | Y |  |  |
| 21 | VLR_SAI_COM_S | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_S_VC | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_E_VC | NUMBER(17,2) | Y |  |  |
| 24 | QTD_SALDOS | NUMBER(13,3) | Y |  |  |
| 25 | VLR_UNIT_SALDO | NUMBER(18,4) | Y |  |  |
| 26 | VLR_TOT_SALDO | NUMBER(17,2) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 29 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 30 | VLR_ICMS_RET | NUMBER(17,2) | Y |  |  |
| 31 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 32 | IDENT_PRODUTO_PAI | NUMBER(12) | Y |  |  |
| 33 | CHASSI | VARCHAR2(17) | Y |  |  |
| 34 | MODELO_LIVRO | VARCHAR2(1) | Y | '3' |  |
| 35 | VLR_BASE_OP_PROP | NUMBER(17,2) | Y |  |  |
| 36 | VLR_BASE_EST_REM | NUMBER(17,2) | Y |  |  |
| 37 | COD_PARAM_GER | NUMBER(3) | Y |  |  |
| 38 | IND_NF_COMPL | CHAR(1) | Y | 'N' |  |
| 39 | VLR_COMPL | NUMBER(17,2) | Y |  |  |
| 40 | IND_CALC_SALD | CHAR(1) | Y | 'N' |  |
| 41 | VLR_BASE_IC_VC | NUMBER(17,2) | Y |  |  |
| 42 | VLR_TOT_SD_IC | NUMBER(17,2) | Y |  |  |
| 43 | VLR_UNIT_SD_IC | NUMBER(18,4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, IDENT_PRODUTO

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO → X2099_EQUIPAMENTO(COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)

**Indexes**:
- IX_FK_SAF_1093: (IDENT_FIS_JUR)
- IX_X27_MOV_EST_ST_01: (COD_EMPRESA, COD_ESTAB, MODELO_LIVRO, CHASSI, DATA_FISCAL, MOVTO_E_S)
- IX_X27_MOV_EST_ST_02: (COD_EMPRESA, COD_ESTAB, MODELO_LIVRO, DATA_FISCAL, MOVTO_E_S)
- IX_X27_MOV_EST_ST_03: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, IDENT_PRODUTO, IDENT_PRODUTO_PAI)
- IX_X27_MOV_EST_ST_06: (IDENT_PRODUTO_PAI, COD_ESTAB, COD_EMPRESA, MODELO_LIVRO)

---

## X280_PROD_MES_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | SEQUENCIAL | NUMBER(5) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | QUANTIDADE | NUMBER(17,4) | Y |  |  |
| 7 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ALIQUOTA_PRODUTO | NUMBER(7,4) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 13 | VLR_PRODUTO_LIQ | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, SEQUENCIAL, IDENT_PRODUTO

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)

---

## X281_ITEM_NOTA_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_EMISSAO | DATE | N |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 5 | NUM_CUPOM | VARCHAR2(12) | N |  |  |
| 6 | SERIE_CUPOM | VARCHAR2(3) | N |  |  |
| 7 | SUBSERIE_CUPOM | VARCHAR2(2) | N |  |  |
| 8 | NUM_ITEM_CUPOM | NUMBER(5) | N |  |  |
| 9 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 10 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 11 | QUANTIDADE | NUMBER(17,4) | Y |  |  |
| 12 | VLR_PRODUTO | NUMBER(17,4) | Y |  |  |
| 13 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ALIQUOTA_PRODUTO | NUMBER(7,4) | Y |  |  |
| 15 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 19 | VLR_LIQUIDO_PROD | NUMBER(17,2) | Y |  | Utilizado na geração dos registros 60I do meio magnético |
| 20 | IND_CANCELAMENTO | CHAR(1) | Y | '1' | Situação de cancelamento: 1 = Normal / 2 = Cancelado / 3 = Item de Cancelamento |
| 21 | IDENT_CFO | NUMBER(12) | Y |  | Utilizado para o registro CFC da DIEF-CE - Cupom Fiscal |
| 22 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  | Utilizado para o registro CFC da DIEF-CE - Cupom Fiscal |
| 23 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg A350 : Código da situação do doc. fiscal: 00 - regular, 01 - extemporâneo, 02 - cancelado, 03 - cancelamento de cupom fiscal anterior, 04 - extemporâneo cancelado, 05 - desfazimento, 06 - doc referenciado - SITUACAO_DOCFIS_V |
| 24 | COD_CFPS | VARCHAR2(4) | Y |  | ATO COTEPE 70 - reg A350 : Código Fiscal de Prestação de Serviço. |
| 25 | COD_TRIB_ISS | VARCHAR2(2) | Y |  | Ato Cotepe 70 - reg A360 : código de tributação do ISS - CTISS - view TRIBUTACAO_ISS_V |
| 26 | IDENT_SITUACAO_A | NUMBER(12) | Y |  | Ato Cotepe 70 - reg C605 : Situação Tributária A. |
| 27 | IDENT_SITUACAO_B | NUMBER(12) | Y |  | Ato Cotepe 70 - reg C605 : Situação Tributária B. |
| 28 | VLR_BASE_ISS | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg A350, A360 : Base de Cálculo do ISS. |
| 29 | VLR_ALIQUOTA_ISS | NUMBER(7,4) | Y |  | Ato Cotepe 70 - reg A360 : Alíquota do ISS. |
| 30 | VLR_ISS | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg A350, A360 : Valor do ISS. |
| 31 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 32 | IDENT_FIS_JUR | NUMBER(12) | Y |  | Campo identificador da pessoa física jurídica do Cupom |
| 33 | CPF_CNPJ_ADQUIRENTE | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, COD_EQUIPAMENTO, NUM_CUPOM, SERIE_CUPOM, SUBSERIE_CUPOM, NUM_ITEM_CUPOM, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, COD_EQUIPAMENTO → X28_CAPA_ECF(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)
- COD_CFPS → DWT_COD_FISCAL_SERV(COD_CFPS)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)

---

## X282_BENF_N_IDENTIF_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_MOV | DATE | N |  |  |
| 4 | COD_NAT_REND | VARCHAR2(5) | N |  |  |
| 5 | IDENT_PROC_ADJ | NUMBER(12) | N |  |  |
| 6 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 7 | VLR_BASE_EXIG_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 8 | VLR_RET_NEFE_IR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_DEP_JUD_IR | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_MOV, COD_NAT_REND → X279_RET_BENEF_NAO_IDENT(COD_EMPRESA, COD_ESTAB, DAT_MOV, COD_NAT_REND)
- IDENT_PROC_ADJ → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT → X2059_SUSP_TBT(IDENT_SUSP_TBT)

**Indexes**:
- UK_X282_BENF_N_IDENTIF_PRO_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_MOV, COD_NAT_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT)

---

## X283_RETENCAO_RECEBIMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_RECEBIMENTO | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | COD_NAT_REND | VARCHAR2(5) | N |  |  |
| 6 | OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 7 | VLR_BRUTO | NUMBER(17,2) | N |  |  |
| 8 | VLR_BASE_IR | NUMBER(17,2) | N |  |  |
| 9 | VLR_IR | NUMBER(17,2) | N |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_RECEBIMENTO, IDENT_FIS_JUR, COD_NAT_REND

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X284_NRET_IMP_DEP_JUD_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_RECEBIMENTO | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | COD_NAT_REND | VARCHAR2(5) | N |  |  |
| 6 | IDENT_PROC_ADJ | NUMBER(12) | N |  |  |
| 7 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 8 | VLR_BASE_EXIG_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 9 | VLR_RET_NEFE_IR | NUMBER(17,2) | Y |  |  |
| 10 | VLR_DEP_JUD_IR | NUMBER(17,2) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_RECEBIMENTO, IDENT_FIS_JUR, COD_NAT_REND → X283_RETENCAO_RECEBIMENTO(COD_EMPRESA, COD_ESTAB, DAT_RECEBIMENTO, IDENT_FIS_JUR, COD_NAT_REND)
- IDENT_PROC_ADJ → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT → X2059_SUSP_TBT(IDENT_SUSP_TBT)

**Indexes**:
- UK_X284_NRET_IMP_DEP_JU_PR_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_RECEBIMENTO, IDENT_FIS_JUR, COD_NAT_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT)

---

## X285_OBS_AJ_CUPOM_SAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_EQUIP | NUMBER(9) | N |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 7 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, IDENT_OBSERVACAO

**FKs**:
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO → X201_CAPA_CUPOM_CFE(COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO)

---

## X286_OBS_AJ_CUPOM_SAT_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_EQUIP | NUMBER(9) | N |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 7 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 8 | NUM_ITEM | NUMBER(5) | Y |  |  |
| 9 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 10 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | ALIQUOTA_ICMS | NUMBER(7,4) | Y |  |  |
| 12 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 13 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**FKs**:
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, IDENT_OBSERVACAO → X285_OBS_AJ_CUPOM_SAT(COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, IDENT_OBSERVACAO)

**Indexes**:
- UK_X286_OBS_AJ_CUPOM_SAT_ITEM (UNIQUE): (COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, IDENT_OBSERVACAO, COD_AJUSTE_SPED, NUM_ITEM)

---

## X28_CAPA_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 5 | NUM_CUPOM_INI | VARCHAR2(12) | Y |  |  |
| 6 | SERIE_CUPOM_INI | VARCHAR2(3) | Y |  |  |
| 7 | SUBSERIE_CUPOM_INI | VARCHAR2(2) | Y |  |  |
| 8 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 9 | NUM_CONT_REDUC | VARCHAR2(12) | Y |  |  |
| 10 | DATA_EMISSAO | DATE | Y |  |  |
| 11 | VLR_GT_INICIAL | NUMBER(17,2) | Y |  |  |
| 12 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 13 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 15 | VLR_B_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_B_ISENTA_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_B_OUTRAS_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_B_RED_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_B_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 20 | VLR_CANCELADO | NUMBER(17,2) | Y |  |  |
| 21 | NUM_CUPOM_FIM | VARCHAR2(12) | Y |  |  |
| 22 | SERIE_CUPOM_FIM | VARCHAR2(3) | Y |  |  |
| 23 | SUBSERIE_CUPOM_FIM | VARCHAR2(2) | Y |  |  |
| 24 | VLR_GT_FINAL | NUMBER(17,2) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 27 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 28 | NUM_CRO | NUMBER(3) | Y |  |  |
| 29 | NUM_MP_RESUMO | VARCHAR2(12) | Y |  |  |
| 30 | NUM_LANCTO_CONTABIL | VARCHAR2(12) | Y |  | número do lançamento contábil - ato cotepe 70/05 |
| 31 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 70/05 |
| 32 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO → X2099_EQUIPAMENTO(COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_2141: (IDENT_OBSERVACAO)
- IX_X28_CAPA_ECF_CTA: (IDENT_CONTA)

---

## X291_PRODUTO_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 5 | SEQUENCIAL | NUMBER(5) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | QUANTIDADE | NUMBER(17,4) | Y |  |  |
| 8 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ALIQUOTA_PRODUTO | NUMBER(7,4) | Y |  |  |
| 11 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | VLR_PRODUTO_LIQ | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO, SEQUENCIAL, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO, SEQUENCIAL → X29_ITEM_ECF(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO, SEQUENCIAL)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

---

## X292_PRODUTO_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 5 | SEQUENCIAL | NUMBER(5) | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | QUANTIDADE | NUMBER(17,4) | Y |  |  |
| 8 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ALIQUOTA_PROD | NUMBER(7,4) | Y |  |  |
| 11 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 13 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 14 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | VLR_PRODUTO_LIQ | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO, SEQUENCIAL, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO → X2099_EQUIPAMENTO(COD_EMPRESA, COD_ESTAB, COD_EQUIPAMENTO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)

**Indexes**:
- IX_X292_PRO_ECF_01: (IDENT_CFO, IDENT_NATUREZA_OP, COD_TRIB_INT)

---

## X293_OBS_DOCFIS_UTILITIES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 9 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 10 | DSC_COMPLEMENTAR | VARCHAR2(500) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | DSC_INFO_FISCO | VARCHAR2(2000) | Y |  |  |
| 14 | DSC_INFO_CONTRIB | VARCHAR2(3000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X42_CAPA_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR_UTIL: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_UTIL: (IDENT_OBSERVACAO)

---

## X294_AJUSTE_APUR_UTILITIES

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IDENT_OBSERVACAO | NUMBER(12) | N |  |  |
| 9 | IND_ICOMPL_LANCTO | CHAR(1) | N |  |  |
| 10 | COD_AJUSTE_SPED | VARCHAR2(10) | N |  |  |
| 11 | NUM_ITEM | NUMBER(7) | N |  |  |
| 12 | DSC_COMP_AJUSTE | VARCHAR2(255) | Y |  |  |
| 13 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 14 | ALIQUOTA_ICMS | NUMBER(7,4) | Y |  |  |
| 15 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_OUTROS | NUMBER(17,2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO, COD_AJUSTE_SPED, NUM_ITEM

**FKs**:
- COD_AJUSTE_SPED → DWT_COD_AJUSTE_SPED(COD_AJUSTE_SPED)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO → X293_OBS_DOCFIS_UTILITIES(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OBSERVACAO, IND_ICOMPL_LANCTO)

**Indexes**:
- IX_FK_X04_PESSOA_FIS_JUR_X294: (IDENT_FIS_JUR)
- IX_FK_X2009_OBSERVACAO_X294: (IDENT_OBSERVACAO)

---

## X295_DET_EXIG_SUSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_GERACAO | DATE | N |  |  |
| 4 | IDENT_PROC_REF | NUMBER(12) | N |  |  |
| 5 | NUM_SEQUENCIAL | NUMBER(6) | N |  |  |
| 6 | REG_REFERENCIA | VARCHAR2(4) | Y |  |  |
| 7 | NUM_AUTENTIC_NFE | VARCHAR2(90) | Y |  |  |
| 8 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 9 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 10 | DATA_OPER | DATE | Y |  |  |
| 11 | VLR_OPER_ITEM | NUMBER(17,2) | Y |  |  |
| 12 | COD_SIT_PIS | VARCHAR2(2) | Y |  |  |
| 13 | VLR_BC_PIS | NUMBER(19,4) | Y |  |  |
| 14 | ALIQ_PIS | NUMBER(12,4) | Y |  |  |
| 15 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 16 | COD_SIT_COFINS | VARCHAR2(2) | Y |  |  |
| 17 | VLR_BC_COFINS | NUMBER(19,4) | Y |  |  |
| 18 | ALIQ_COFINS | NUMBER(12,4) | Y |  |  |
| 19 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 20 | COD_SIT_PIS_SUSP | VARCHAR2(2) | Y |  |  |
| 21 | VLR_BC_PIS_SUSP | NUMBER(19,4) | Y |  |  |
| 22 | ALIQ_PIS_SUSP | NUMBER(12,4) | Y |  |  |
| 23 | VLR_PIS_SUSP | NUMBER(17,2) | Y |  |  |
| 24 | COD_SIT_COFINS_SUSP | VARCHAR2(2) | Y |  |  |
| 25 | VLR_BC_COFINS_SUSP | NUMBER(19,4) | Y |  |  |
| 26 | ALIQ_COFINS_SUSP | NUMBER(12,4) | Y |  |  |
| 27 | VLR_COFINS_SUSP | NUMBER(17,2) | Y |  |  |
| 28 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 29 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 30 | DSC_DOCUMENTO | VARCHAR2(255) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 32 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_GERACAO, IDENT_PROC_REF, NUM_SEQUENCIAL

**FKs**:
- IDENT_PROC_REF → DWT_PROC_REF(IDENT_PROC_REF)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)

**Indexes**:
- IX_FK_SAF_3170: (IDENT_FIS_JUR)
- IX_X295_DET_EXIG_SUSP_CTA: (IDENT_CONTA)

---

## X296_INFO_COMPL_ST_ITENS_MERC

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
| 16 | IND_RESP_RET_ENT | VARCHAR2(1) | Y |  |  |
| 17 | VLR_UNIT_BC_ICMSS_ENT | NUMBER(19,6) | Y |  |  |
| 18 | VLR_UNIT_ICMSS_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_FCP_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 20 | COD_MOTIVO_SAI | VARCHAR2(5) | Y |  |  |
| 21 | VLR_UNIT_ICMS_OPER_SAI | NUMBER(19,6) | Y |  |  |
| 22 | VLR_UNIT_ICMS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 23 | VLR_UNIT_ICMSS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 24 | VLR_UNIT_FCP_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 25 | VLR_UNIT_ICMSS_REST_SAI | NUMBER(19,6) | Y |  |  |
| 26 | VLR_UNIT_FCP_REST_SAI | NUMBER(19,6) | Y |  |  |
| 27 | VLR_UNIT_ICMSS_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 28 | VLR_UNIT_FCP_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 30 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_MOTIVO_SAI → DWT_COD_MOTIVO_SPED(COD_MOTIVO_SPED)

---

## X297_INF_COMP_ST_CUPOM_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 4 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 5 | NUM_COO | VARCHAR2(9) | N |  |  |
| 6 | DATA_EMISSAO | DATE | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 8 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 9 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 10 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 11 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 12 | VLR_UNIT_ICMS_OPER_CONV | NUMBER(19,6) | Y |  |  |
| 13 | VLR_UNIT_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 14 | VLR_UNIT_ICMS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 15 | VLR_UNIT_ICMSS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 16 | VLR_UNIT_FCPS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 17 | VLR_UNIT_ICMSS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 18 | VLR_UNIT_FCPS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_ICMSS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 20 | VLR_UNIT_FCPS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_CAIXA_ECF, NUM_COO, DATA_EMISSAO, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CAIXA_ECF → X2087_EQUIPAMENTO_ECF(IDENT_CAIXA_ECF)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO → X993_CAPA_CUPOM_ECF(DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO)
- COD_MOTIVO → DWT_COD_MOTIVO_SPED(COD_MOTIVO_SPED)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

---

## X298_INFO_COMP_ST_IT_CUPOM_CFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | NUM_EQUIP | NUMBER(9) | N |  |  |
| 4 | NUM_CUPOM | VARCHAR2(6) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | NUM_ITEM | NUMBER(5) | N |  |  |
| 7 | COD_MOTIVO_SAI | VARCHAR2(5) | Y |  |  |
| 8 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 9 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 10 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 11 | VLR_UNIT_ICMS_OPER_CONV | NUMBER(19,6) | Y |  |  |
| 12 | VLR_UNIT_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 13 | VLR_UNIT_ICMS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 14 | VLR_UNIT_ICMSS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 15 | VLR_UNIT_FCPS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 16 | VLR_UNIT_ICMSS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 17 | VLR_UNIT_FCPS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 18 | VLR_UNIT_ICMSS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_FCPS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, NUM_ITEM

**FKs**:
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, NUM_ITEM → X202_ITEM_CUPOM_CFE(COD_EMPRESA, COD_ESTAB, NUM_EQUIP, NUM_CUPOM, DATA_EMISSAO, NUM_ITEM)
- COD_MOTIVO_SAI → DWT_COD_MOTIVO_SPED(COD_MOTIVO_SPED)

---

## X299_INF_COMP_ST_RES_MOD_02

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_EMISSAO | DATE | N |  |  |
| 4 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 5 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 6 | NUM_DOCFIS_INI | VARCHAR2(12) | N |  |  |
| 7 | NUM_DOCFIS_FIN | VARCHAR2(12) | N |  |  |
| 8 | IDENT_SITUACAO_A | NUMBER(12) | N |  |  |
| 9 | IDENT_SITUACAO_B | NUMBER(12) | N |  |  |
| 10 | IDENT_CFO | NUMBER(12) | N |  |  |
| 11 | VLR_ALIQ_ICMS | NUMBER(7,4) | N |  |  |
| 12 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 13 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 14 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 15 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 16 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 17 | VLR_UNIT_ICMS_OPER_CONV | NUMBER(19,6) | Y |  |  |
| 18 | VLR_UNIT_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_ICMS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 20 | VLR_UNIT_ICMSS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 21 | VLR_UNIT_FCPS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 22 | VLR_UNIT_ICMSS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 23 | VLR_UNIT_FCPS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 24 | VLR_UNIT_ICMSS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 25 | VLR_UNIT_FCPS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_EMISSAO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS_INI, NUM_DOCFIS_FIN, IDENT_SITUACAO_A, IDENT_SITUACAO_B, IDENT_CFO, VLR_ALIQ_ICMS, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- COD_MOTIVO → DWT_COD_MOTIVO_SPED(COD_MOTIVO_SPED)

---

## X29_ITEM_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | COD_EQUIPAMENTO | VARCHAR2(6) | N |  |  |
| 5 | SEQUENCIAL | NUMBER(5) | N |  |  |
| 6 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 7 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 8 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ALIQ_OPER | NUMBER(7,4) | Y |  |  |
| 10 | VLR_OPER | NUMBER(17,2) | Y |  |  |
| 11 | COD_TRIB_OPER | CHAR(1) | Y |  |  |
| 12 | VLR_BASE_OPER | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BASE_RED_OPER | NUMBER(17,2) | Y |  |  |
| 14 | VLR_CONTAB_OPER | NUMBER(17,2) | Y |  |  |
| 15 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |
| 16 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 17 | COD_TRIB_INT | NUMBER(5) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO, SEQUENCIAL

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO → X28_CAPA_ECF(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, COD_EQUIPAMENTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- COD_TRIB_INT → DWT_TRIBUTACAO_INT(COD_TRIB_INT)

---

## X3007_DOCTO_FISCAL_RT

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
| 11 | COD_MUN_FT_GER_IBS_CBS | NUMBER(7) | Y |  |  |
| 12 | TIPO_CHAVE_DFE | NUMBER(1) | N |  |  |
| 13 | DESC_CHAVE_DFE | VARCHAR2(255) | Y |  |  |
| 14 | FINALIDADE_EMISSAO_NFE | NUMBER(1) | Y |  |  |
| 15 | FINALIDADE_EMISSAO_NFSE | NUMBER(1) | Y |  |  |
| 16 | TIPO_NF_DEBITO | VARCHAR2(2) | Y |  |  |
| 17 | TIPO_NF_CREDITO | VARCHAR2(2) | Y |  |  |
| 18 | IND_OPER_FINAL | NUMBER(1) | Y |  |  |
| 19 | IND_OPER_USO_CONS_PESSOAL | NUMBER(1) | Y |  |  |
| 20 | IND_OPER_FORNECIMENTO | VARCHAR2(10) | Y |  |  |
| 21 | IND_DESTINATARIO_SERVICO | NUMBER(1) | Y |  |  |
| 22 | IND_COMPRA_MOMENTO_OPER | NUMBER(1) | Y |  |  |
| 23 | IND_INTERM | NUMBER(1) | Y |  |  |
| 24 | IND_COMPRA_GOVERN | NUMBER(1) | Y |  |  |
| 25 | TIPO_OPERACAO | NUMBER(1) | Y |  |  |
| 26 | TIPO_ENTE_GOVERN | NUMBER(1) | Y |  |  |
| 27 | PERC_RED_ALIQ_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 28 | CST_IS | VARCHAR2(3) | Y |  |  |
| 29 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 30 | BC_IS | NUMBER(17,2) | Y |  |  |
| 31 | ALIQ_IS | NUMBER(7,4) | Y |  |  |
| 32 | ALIQ_ESP_UNID_MED_APR_IS | NUMBER(7,4) | Y |  |  |
| 33 | VLR_IS | NUMBER(17,2) | Y |  |  |
| 34 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 35 | QTD_TRIB_IS | NUMBER(15,4) | Y |  |  |
| 36 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 37 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 38 | BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 39 | VLR_MON_DOCREF_N_INC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 40 | ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 41 | VLR_IBS_UF | NUMBER(17,2) | Y |  |  |
| 42 | PERC_DIF_IBS_UF | NUMBER(7,4) | Y |  |  |
| 43 | VLR_DIF_IBS_UF | NUMBER(17,2) | Y |  |  |
| 44 | VLR_TRIB_DEV_IBS_UF | NUMBER(17,2) | Y |  |  |
| 45 | PERC_RED_ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 46 | ALIQ_EFET_IBS_UF | NUMBER(7,4) | Y |  |  |
| 47 | ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 48 | VLR_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 49 | PERC_DIF_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 50 | VLR_DIF_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 51 | VLR_BRUTO_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 52 | VLR_TRIB_DEV_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 53 | PERC_RED_ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 54 | ALIQ_EFET_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 55 | ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 56 | VLR_CBS | NUMBER(17,2) | Y |  |  |
| 57 | PERC_DIF_CBS | NUMBER(7,4) | Y |  |  |
| 58 | VLR_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 59 | VLR_BRUTO_CBS | NUMBER(17,2) | Y |  |  |
| 60 | VLR_TRIB_DEV_CBS | NUMBER(17,2) | Y |  |  |
| 61 | PERC_RED_ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 62 | ALIQ_EFET_CBS | NUMBER(7,4) | Y |  |  |
| 63 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 64 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 65 | ALIQ_IBS_TRIB_REG_UF | NUMBER(7,4) | Y |  |  |
| 66 | VLR_TRIB_REG_TRIB_IBS_UF | NUMBER(17,2) | Y |  |  |
| 67 | ALIQ_TRIB_REG_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 68 | VLR_TRIB_REG_TRIB_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 69 | ALIQ_TRIB_REG_CBS | NUMBER(7,4) | Y |  |  |
| 70 | VLR_TRIB_REG_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 71 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 72 | PERC_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 73 | ALIQ_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 74 | VLR_CRED_PRES_IBS | NUMBER(17,2) | Y |  |  |
| 75 | VLR_CRED_PRES_C_SUS_IBS | NUMBER(17,2) | Y |  |  |
| 76 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 77 | PERC_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 78 | ALIQ_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 79 | VLR_CRED_PRES_CBS | NUMBER(17,2) | Y |  |  |
| 80 | VLR_CRED_PRES_C_SUS_CBS | NUMBER(17,2) | Y |  |  |
| 81 | QTD_TRIB_MONO_IBS_CBS | NUMBER(15,4) | Y |  |  |
| 82 | ALIQ_AD_REM_IBS | NUMBER(7,4) | Y |  |  |
| 83 | ALIQ_AD_REM_CBS | NUMBER(7,4) | Y |  |  |
| 84 | VLR_MONO_IBS | NUMBER(17,2) | Y |  |  |
| 85 | VLR_MONO_CBS | NUMBER(17,2) | Y |  |  |
| 86 | QTD_TRIB_RET_MONO_IBS_CBS | NUMBER(15,4) | Y |  |  |
| 87 | ALIQ_AD_REM_RET_IBS | NUMBER(7,4) | Y |  |  |
| 88 | VLR_MONO_RET_IBS | NUMBER(17,2) | Y |  |  |
| 89 | ALIQ_AD_REM_RET_CBS | NUMBER(7,4) | Y |  |  |
| 90 | VLR_MONO_RET_CBS | NUMBER(17,2) | Y |  |  |
| 91 | QTD_TRIB_RET_ANT_IBS_CBS | NUMBER(15,4) | Y |  |  |
| 92 | ALIQ_AD_REM_RET_ANT_IBS | NUMBER(7,4) | Y |  |  |
| 93 | VLR_RET_ANT_IBS | NUMBER(17,2) | Y |  |  |
| 94 | ALIQ_AD_REM_RET_ANT_CBS | NUMBER(7,4) | Y |  |  |
| 95 | VLR_RET_ANT_CBS | NUMBER(17,2) | Y |  |  |
| 96 | PERC_DIF_MONO_IBS | NUMBER(7,4) | Y |  |  |
| 97 | VLR_MONO_DIF_IBS | NUMBER(17,2) | Y |  |  |
| 98 | PERC_DIF_MONO_CBS | NUMBER(7,4) | Y |  |  |
| 99 | VLR_MONO_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 100 | ALIQ_IBS_UF_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 101 | VLR_IBS_UF_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 102 | ALIQ_IBS_MUN_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 103 | VLR_IBS_MUN_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 104 | ALIQ_CBS_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 105 | VLR_CBS_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 106 | CHAVE_DFE_REF | VARCHAR2(44) | Y |  |  |
| 107 | VLR_TOT_IS | NUMBER(17,2) | Y |  |  |
| 108 | VLR_TOT_BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 109 | VLR_TOT_DIF_IBS_UF | NUMBER(17,2) | Y |  |  |
| 110 | VLR_TOT_DEV_TRIB_IBS_UF | NUMBER(17,2) | Y |  |  |
| 111 | VLR_TOT_IBS_UF | NUMBER(17,2) | Y |  |  |
| 112 | VLR_TOT_DIF_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 113 | VLR_TOT_DEV_TRIB_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 114 | VLR_TOT_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 115 | VLR_TOT_IBS | NUMBER(17,2) | Y |  |  |
| 116 | VLR_TOT_CRED_PRES_IBS | NUMBER(17,2) | Y |  |  |
| 117 | VLR_TOT_CRED_PRES_C_SUS_IBS | NUMBER(17,2) | Y |  |  |
| 118 | VLR_TOT_CRED_PRES_CBS | NUMBER(17,2) | Y |  |  |
| 119 | VLR_TOT_CRED_PRES_C_SUS_CBS | NUMBER(17,2) | Y |  |  |
| 120 | VLR_TOT_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 121 | VLR_TOT_DEV_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 122 | VLR_TOT_CBS | NUMBER(17,2) | Y |  |  |
| 123 | TOT_MONO_IBS | NUMBER(17,2) | Y |  |  |
| 124 | TOT_MONO_CBS | NUMBER(17,2) | Y |  |  |
| 125 | TOT_MONO_RET_IBS | NUMBER(17,2) | Y |  |  |
| 126 | TOT_MONO_RET_CBS | NUMBER(17,2) | Y |  |  |
| 127 | TOT_MONO_RET_ANT_IBS | NUMBER(17,2) | Y |  |  |
| 128 | TOT_MONO_RET_ANT_CBS | NUMBER(17,2) | Y |  |  |
| 129 | VLR_TOT_NF_IBS_CBS_IS | NUMBER(17,2) | Y |  |  |
| 130 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 131 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 132 | DAT_CRIACAO | DATE | Y |  |  |
| 133 | DAT_ALTERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- CST_IBS_CBS → CAD_CST_IBS_CBS(COD_CST_IBS_CBS)
- CCLASS_IBS_CBS → CAD_CCLASS_TRIB(COD_CCLASS_TRIB)
- CST_TRIB_REG_IBS_CBS → CAD_CST_IBS_CBS(COD_CST_IBS_CBS)
- CCLASS_TRIB_REG_IBS_CBS → CAD_CCLASS_TRIB(COD_CCLASS_TRIB)

---

## X3008_ITENS_MERC_RT

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
| 12 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 13 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 14 | COD_BEM | VARCHAR2(60) | Y |  |  |
| 15 | COD_INC_BEM | VARCHAR2(6) | Y |  |  |
| 16 | NUM_ITEM | VARCHAR2(5) | Y |  |  |
| 17 | CST_IS | VARCHAR2(3) | Y |  |  |
| 18 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 19 | BC_IS | NUMBER(17,2) | Y |  |  |
| 20 | ALIQ_IS | NUMBER(7,4) | Y |  |  |
| 21 | ALIQ_ESPEC_UNID_MED_APR_IS | NUMBER(7,4) | Y |  |  |
| 22 | VLR_IS | NUMBER(17,2) | Y |  |  |
| 23 | IDENT_UNID_MED_TRIBUT_IS | NUMBER(12) | Y |  |  |
| 24 | QTD_TRIB_IS | NUMBER(11,4) | Y |  |  |
| 25 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 26 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 27 | BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_MON_DOCREF_N_INC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 29 | ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 30 | VLR_IBS_UF | NUMBER(17,2) | Y |  |  |
| 31 | PERC_DIF_IBS_UF | NUMBER(7,4) | Y |  |  |
| 32 | VLR_DIF_IBS_UF | NUMBER(17,2) | Y |  |  |
| 33 | VLR_TRIB_DEV_IBS_UF | NUMBER(17,2) | Y |  |  |
| 34 | PERC_RED_ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 35 | ALIQ_EFET_IBS_UF | NUMBER(7,4) | Y |  |  |
| 36 | ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 37 | VLR_CBS | NUMBER(17,2) | Y |  |  |
| 38 | PERC_DIF_CBS | NUMBER(7,4) | Y |  |  |
| 39 | VLR_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 40 | VLR_BRUTO_CBS | NUMBER(17,2) | Y |  |  |
| 41 | VLR_TRIB_DEV_CBS | NUMBER(17,2) | Y |  |  |
| 42 | PERC_RED_ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 43 | ALIQ_EFET_CBS | NUMBER(7,4) | Y |  |  |
| 44 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 45 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 46 | ALIQ_TRIB_REG_IBS_UF | NUMBER(7,4) | Y |  |  |
| 47 | VLR_TRIB_REG_TRIB_IBS_UF | NUMBER(17,2) | Y |  |  |
| 48 | ALIQ_TRIB_REG_CBS | NUMBER(7,4) | Y |  |  |
| 49 | VLR_TRIB_REG_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 50 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 51 | PERC_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 52 | ALIQ_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 53 | VLR_CRED_PRES_IBS | NUMBER(17,2) | Y |  |  |
| 54 | VLR_CRED_PRES_COND_SUSP_IBS | NUMBER(17,2) | Y |  |  |
| 55 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 56 | PERC_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 57 | ALIQ_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 58 | VLR_CRED_PRES_CBS | NUMBER(17,2) | Y |  |  |
| 59 | VLR_CRED_PRES_COND_SUSP_CBS | NUMBER(17,2) | Y |  |  |
| 60 | QTD_TRIB_MONO_IBS_CBS | NUMBER(11,4) | Y |  |  |
| 61 | ALIQ_AD_REM_IBS | NUMBER(7,4) | Y |  |  |
| 62 | ALIQ_AD_REM_CBS | NUMBER(7,4) | Y |  |  |
| 63 | VLR_MONO_IBS | NUMBER(17,2) | Y |  |  |
| 64 | VLR_MONO_CBS | NUMBER(17,2) | Y |  |  |
| 65 | QTD_TRIB_RET_MONO_IBS_CBS | NUMBER(11,4) | Y |  |  |
| 66 | ALIQ_AD_REM_RET_IBS | NUMBER(7,4) | Y |  |  |
| 67 | VLR_MONO_RET_IBS | NUMBER(17,2) | Y |  |  |
| 68 | ALIQ_AD_REM_RET_CBS | NUMBER(7,4) | Y |  |  |
| 69 | VLR_MONO_RET_CBS | NUMBER(17,2) | Y |  |  |
| 70 | QTD_TRIB_RET_ANT_IBS_CBS | NUMBER(11,4) | Y |  |  |
| 71 | ALIQ_AD_REM_RET_ANT_IBS | NUMBER(7,4) | Y |  |  |
| 72 | VLR_RET_ANT_IBS | NUMBER(17,2) | Y |  |  |
| 73 | ALIQ_AD_REM_RET_ANT_CBS | NUMBER(7,4) | Y |  |  |
| 74 | VLR_RET_ANT_CBS | NUMBER(17,2) | Y |  |  |
| 75 | PERC_DIF_MONO_IBS | NUMBER(7,4) | Y |  |  |
| 76 | VLR_MONO_DIF_IBS | NUMBER(17,2) | Y |  |  |
| 77 | PERC_DIF_MONO_CBS | NUMBER(7,4) | Y |  |  |
| 78 | VLR_MONO_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 79 | ALIQ_IBS_UF_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 80 | VLR_IBS_UF_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 81 | ALIQ_IBS_MUN_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 82 | VLR_IBS_MUN_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 83 | ALIQ_CBS_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 84 | VLR_CBS_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 85 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 86 | NUM_ITEM_DOC_REFERENCIADO | NUMBER(3) | Y |  |  |
| 87 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 88 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 89 | DAT_CRIACAO | DATE | Y |  |  |
| 90 | DAT_ALTERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- CST_IBS_CBS → CAD_CST_IBS_CBS(COD_CST_IBS_CBS)
- CCLASS_IBS_CBS → CAD_CCLASS_TRIB(COD_CCLASS_TRIB)
- CST_TRIB_REG_IBS_CBS → CAD_CST_IBS_CBS(COD_CST_IBS_CBS)
- CCLASS_TRIB_REG_IBS_CBS → CAD_CCLASS_TRIB(COD_CCLASS_TRIB)

---

## X3009_ITENS_SERV_RT

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
| 11 | IDENT_SERVICO | NUMBER(12) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N |  |  |
| 13 | COD_MUN_FT_GER_IBS_CBS | NUMBER(7) | Y |  |  |
| 14 | CST_IS | VARCHAR2(3) | Y |  |  |
| 15 | CCLASS_IS | VARCHAR2(6) | Y |  |  |
| 16 | BC_IS | NUMBER(17,2) | Y |  |  |
| 17 | ALIQ_IS | NUMBER(7,4) | Y |  |  |
| 18 | ALIQ_ESPEC_UNID_MED_APR_IS | NUMBER(7,4) | Y |  |  |
| 19 | VLR_IS | NUMBER(17,2) | Y |  |  |
| 20 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 21 | QTD_TRIB_IS | NUMBER(15,4) | Y |  |  |
| 22 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 23 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 24 | BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_MON_DOCREF_N_INC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 26 | ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 27 | VLR_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 28 | PERC_DIF_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 29 | VLR_DIF_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 30 | VLR_BRUTO_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 31 | VLR_TRIB_DEV_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 32 | PERC_RED_ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 33 | ALIQ_EFET_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 34 | ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 35 | VLR_CBS | NUMBER(17,2) | Y |  |  |
| 36 | VLR_BRUTO_CBS | NUMBER(17,2) | Y |  |  |
| 37 | VLR_TRIB_DEV_CBS | NUMBER(17,2) | Y |  |  |
| 38 | PERC_RED_ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 39 | ALIQ_EFET_CBS | NUMBER(7,4) | Y |  |  |
| 40 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 41 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 42 | ALIQ_TRIB_REG_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 43 | VLR_TRIB_REG_TRIB_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 44 | ALIQ_TRIB_REG_CBS | NUMBER(7,4) | Y |  |  |
| 45 | VLR_TRIB_REG_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 46 | CCLASS_CRED_PRES_IBS | VARCHAR2(3) | Y |  |  |
| 47 | PERC_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 48 | ALIQ_CRED_PRES_IBS | NUMBER(7,4) | Y |  |  |
| 49 | VLR_CRED_PRES_IBS | NUMBER(17,2) | Y |  |  |
| 50 | VLR_CRED_PRES_COND_SUSP_IBS | NUMBER(17,2) | Y |  |  |
| 51 | CCLASS_CRED_PRES_CBS | VARCHAR2(3) | Y |  |  |
| 52 | PERC_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 53 | ALIQ_CRED_PRES_CBS | NUMBER(7,4) | Y |  |  |
| 54 | VLR_CRED_PRES_CBS | NUMBER(17,2) | Y |  |  |
| 55 | VLR_CRED_PRES_COND_SUSP_CBS | NUMBER(17,2) | Y |  |  |
| 56 | ALIQ_IBS_UF_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 57 | VLR_IBS_UF_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 58 | ALIQ_IBS_MUN_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 59 | VLR_IBS_MUN_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 60 | ALIQ_CBS_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 61 | VLR_CBS_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 62 | VLR_TOT_ITEM | NUMBER(17,2) | Y |  |  |
| 63 | NUM_ITEM_DOC_REFERENCIADO | NUMBER(3) | Y |  |  |
| 64 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 65 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 66 | DAT_CRIACAO | DATE | Y |  |  |
| 67 | DAT_ALTERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM → X09_ITENS_SERV(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_SERVICO, NUM_ITEM)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- CST_IBS_CBS → CAD_CST_IBS_CBS(COD_CST_IBS_CBS)
- CCLASS_IBS_CBS → CAD_CCLASS_TRIB(COD_CCLASS_TRIB)
- CST_TRIB_REG_IBS_CBS → CAD_CST_IBS_CBS(COD_CST_IBS_CBS)
- CCLASS_TRIB_REG_IBS_CBS → CAD_CCLASS_TRIB(COD_CCLASS_TRIB)

---

## X300_TIT_PAGAR_DOC

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
| 10 | NUM_DOCFIS_NF | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS_NF | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS_NF | VARCHAR2(2) | N |  |  |
| 13 | DATA_FISCAL_NF | DATE | N |  |  |
| 14 | MOVTO_E_S_NF | CHAR(1) | N |  |  |
| 15 | NORM_DEV_NF | CHAR(1) | N |  |  |
| 16 | IDENT_DOCTO_NF | NUMBER(12) | N |  |  |
| 17 | IDENT_FIS_JUR_NF | NUMBER(12) | N |  |  |
| 18 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 19 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_DOCFIS_NF, SERIE_DOCFIS_NF, SUB_SERIE_DOCFIS_NF, DATA_FISCAL_NF, MOVTO_E_S_NF, NORM_DEV_NF, IDENT_DOCTO_NF, IDENT_FIS_JUR_NF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X03_TIT_PAGAR(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

---

## X301_TIT_PAGAR_PARC

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
| 10 | NUM_PARCELA | NUMBER(3) | N |  |  |
| 11 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 12 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 13 | DATA_VENCTO | DATE | Y |  |  |
| 14 | VLR_PARCELA | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | VLR_JUROS | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg Z035 - Valor dos Juros/Multa pagos |
| 18 | VLR_DESCONTO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg Z035 - Valor de Desconto recebido |
| 19 | VLR_IRRF | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg Z035 - Valor do IR |
| 20 | DATA_PGTO | DATE | Y |  | ATO COTEPE 70 - reg Z035 - Data de pagamento da parcela |
| 21 | IND_PGTO | CHAR(1) | Y |  | ATO COTEPE 70 - reg Z035 - Indicador da forma de pagamento. Valores: 0, 1, 2, 3, 4, 5, 9 |
| 22 | DESC_PGTO | VARCHAR2(100) | Y |  | ATO COTEPE 70 - reg Z035 - Descricao complementar da forma de pagamento |
| 23 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  | ATO COTEPE 70 - reg Z035 - Número do Lançamento Contábil |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_PARCELA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X03_TIT_PAGAR(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

**Indexes**:
- IX_FK_SAF_2064: (IDENT_FIS_JUR)

---

## X302_INF_COMP_ST_RES_IT_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 4 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 5 | NUM_CRZ | VARCHAR2(6) | N |  |  |
| 6 | DATA_FISCAL | DATE | N |  |  |
| 7 | IDENT_TOTALIZADOR_ECF | NUMBER(12) | N |  |  |
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
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MODELO, IDENT_CAIXA_ECF, NUM_CRZ, DATA_FISCAL, IDENT_TOTALIZADOR_ECF, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CAIXA_ECF → X2087_EQUIPAMENTO_ECF(IDENT_CAIXA_ECF)
- IDENT_TOTALIZADOR_ECF → X996_TOTALIZADOR_PARCIAL_ECF(IDENT_TOTALIZADOR_ECF)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- COD_MOTIVO → DWT_COD_MOTIVO_SPED(COD_MOTIVO_SPED)

---

## X303_INF_COMP_ST_RES_CUPOM_CFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 4 | NUM_EQUIP | NUMBER(9) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 7 | IDENT_SITUACAO_A | NUMBER(12) | N |  |  |
| 8 | IDENT_SITUACAO_B | NUMBER(12) | N |  |  |
| 9 | IDENT_CFO | NUMBER(12) | N |  |  |
| 10 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 11 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 12 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 13 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 14 | VLR_UNIT_ICMS_OPER_CONV | NUMBER(19,6) | Y |  |  |
| 15 | VLR_UNIT_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 16 | VLR_UNIT_ICMS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 17 | VLR_UNIT_ICMSS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 18 | VLR_UNIT_FCPS_ESTQ_CONV | NUMBER(19,6) | Y |  |  |
| 19 | VLR_UNIT_ICMSS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 20 | VLR_UNIT_FCPS_REST_CONV | NUMBER(19,6) | Y |  |  |
| 21 | VLR_UNIT_ICMSS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 22 | VLR_UNIT_FCPS_COMPL_CONV | NUMBER(19,6) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_MODELO, NUM_EQUIP, DATA_EMISSAO, IDENT_PRODUTO, IDENT_SITUACAO_A, IDENT_SITUACAO_B, IDENT_CFO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- COD_MOTIVO → DWT_COD_MOTIVO_SPED(COD_MOTIVO_SPED)

---

## X3042_CAPA_TELECOM_RT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | VLR_TOT_BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_DIF_IBS_UF | NUMBER(17,2) | Y |  |  |
| 10 | VLR_TOT_DEV_TRIB_IBS_UF | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_IBS_UF | NUMBER(17,2) | Y |  |  |
| 12 | VLR_TOT_DIF_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 13 | VLR_TOT_DEV_TRIB_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 14 | VLR_TOT_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 15 | VLR_TOT_IBS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TOT_DEV_TRIB_CBS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TOT_CBS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOT_TRIB_REG_IBS_UF | NUMBER(17,2) | Y |  |  |
| 20 | VLR_TOT_TRIB_REG_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 21 | VLR_TOT_TRIB_REG_CBS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_TOT_IBS_UF_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 23 | VLR_TOT_IBS_MUN_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TOT_CBS_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 25 | VLR_TOT_IBS_ESTORNADO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_TOT_CBS_ESTORNADO | NUMBER(17,2) | Y |  |  |
| 27 | TIPO_ENTE_GOVERN | NUMBER(1) | Y |  |  |
| 28 | PERC_RED_ALIQ_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 29 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 30 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 31 | DAT_CRIACAO | DATE | Y |  |  |
| 32 | DAT_ALTERACAO | DATE | Y |  |  |

**PK**: DAT_FISCAL, COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X42_CAPA_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

**Indexes**:
- IX01_X3042_CAPA_TELECOM_RT: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## X3043_ITEM_TELECOM_RT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_ITEM | NUMBER(7) | N |  |  |
| 9 | CST_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 10 | CCLASS_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 11 | IND_DOACAO | VARCHAR2(1) | Y |  |  |
| 12 | BC_IBS_CBS | NUMBER(17,2) | Y |  |  |
| 13 | ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 14 | PERC_DIF_IBS_UF | NUMBER(7,4) | Y |  |  |
| 15 | VLR_DIF_IBS_UF | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TRIB_DEV_IBS_UF | NUMBER(17,2) | Y |  |  |
| 17 | PERC_RED_ALIQ_IBS_UF | NUMBER(7,4) | Y |  |  |
| 18 | ALIQ_EFET_IBS_UF | NUMBER(7,4) | Y |  |  |
| 19 | VLR_IBS_UF | NUMBER(17,2) | Y |  |  |
| 20 | ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 21 | PERC_DIF_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 22 | VLR_DIF_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 23 | VLR_TRIB_DEV_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 24 | PERC_RED_ALIQ_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 25 | ALIQ_EFET_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 26 | VLR_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 27 | TOT_IBS_ITEM | NUMBER(17,2) | Y |  |  |
| 28 | ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 29 | PERC_DIF_CBS | NUMBER(7,4) | Y |  |  |
| 30 | VLR_DIF_CBS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_TRIB_DEV_CBS | NUMBER(17,2) | Y |  |  |
| 32 | PERC_RED_ALIQ_CBS | NUMBER(7,4) | Y |  |  |
| 33 | ALIQ_EFET_CBS | NUMBER(7,4) | Y |  |  |
| 34 | VLR_CBS | NUMBER(17,2) | Y |  |  |
| 35 | CST_TRIB_REG_IBS_CBS | VARCHAR2(3) | Y |  |  |
| 36 | CCLASS_TRIB_REG_IBS_CBS | VARCHAR2(6) | Y |  |  |
| 37 | ALIQ_TRIB_REG_IBS_UF | NUMBER(7,4) | Y |  |  |
| 38 | VLR_TRIB_REG_IBS_UF | NUMBER(17,2) | Y |  |  |
| 39 | ALIQ_TRIB_REG_IBS_MUN | NUMBER(7,4) | Y |  |  |
| 40 | VLR_TRIB_REG_IBS_MUN | NUMBER(17,2) | Y |  |  |
| 41 | ALIQ_TRIB_REG_CBS | NUMBER(7,4) | Y |  |  |
| 42 | VLR_TRIB_REG_CBS | NUMBER(17,2) | Y |  |  |
| 43 | ALIQ_IBS_UF_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 44 | VLR_IBS_UF_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 45 | ALIQ_IBS_MUN_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 46 | VLR_IBS_MUN_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 47 | ALIQ_CBS_COMPRA_GOVERN | NUMBER(7,4) | Y |  |  |
| 48 | VLR_CBS_COMPRA_GOVERN | NUMBER(17,2) | Y |  |  |
| 49 | IBS_ESTORNADO | NUMBER(17,2) | Y |  |  |
| 50 | CBS_ESTORNADO | NUMBER(17,2) | Y |  |  |
| 51 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 52 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 53 | DAT_CRIACAO | DATE | Y |  |  |
| 54 | DAT_ALTERACAO | DATE | Y |  |  |

**PK**: DAT_FISCAL, COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM → X43_ITEM_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM)

**Indexes**:
- IX01_X3043_ITEM_TELECOM_RT: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM)

---

## X304_SALDO_CONS_RES_COMP_ICMS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | COD_MOTIVO | VARCHAR2(5) | N |  |  |
| 5 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 6 | VLR_ICMS_ST_REST | NUMBER(17,2) | Y |  |  |
| 7 | VLR_FCP_ST_REST | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_ST_COMP | NUMBER(17,2) | Y |  |  |
| 9 | VLR_FCP_ST_COMP | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, COD_MOTIVO

**FKs**:
- COD_MOTIVO → DWT_COD_MOTIVO_SPED(COD_MOTIVO_SPED)

---

## X308_INFO_COMPL_ST_IT_MERC_DEV

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
| 12 | ESPECIE_DOCTO_DEV | VARCHAR2(1) | Y |  |  |
| 13 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 14 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 15 | SUB_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 16 | IDENT_DOCTO_REF | NUMBER(12) | Y |  |  |
| 17 | DATA_FISCAL_REF | DATE | Y |  |  |
| 18 | IDENT_FIS_JUR_REF | NUMBER(12) | Y |  |  |
| 19 | IDENT_MODELO_REF | NUMBER(12) | Y |  |  |
| 20 | IDENT_CAIXA_ECF | NUMBER(12) | Y |  |  |
| 21 | NUM_COO_REF | VARCHAR2(9) | Y |  |  |
| 22 | DATA_EMISSAO_REF | DATE | Y |  |  |
| 23 | NUM_EQUIP_REF | NUMBER(9) | Y |  |  |
| 24 | NUM_CUPOM_REF | VARCHAR2(6) | Y |  |  |
| 25 | NUM_ITEM_DOC_REF | NUMBER(5) | Y |  |  |
| 26 | COD_MOTIVO | VARCHAR2(5) | Y |  |  |
| 27 | QTD_CONV | NUMBER(17,6) | Y |  |  |
| 28 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 29 | VLR_UNIT_CONV | NUMBER(19,6) | Y |  |  |
| 30 | VLR_ICMS_CONV | NUMBER(19,6) | Y |  |  |
| 31 | VLR_UNIT_BC_ICMSS_ENT | NUMBER(19,6) | Y |  |  |
| 32 | VLR_UNIT_ICMSS_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 33 | VLR_UNIT_FCP_CONV_ENT | NUMBER(19,6) | Y |  |  |
| 34 | VLR_UNIT_ICMS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 35 | VLR_UNIT_ICMSS_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 36 | VLR_UNIT_FCP_ESTQ_SAI | NUMBER(19,6) | Y |  |  |
| 37 | VLR_UNIT_ICMS_OPER_SAI | NUMBER(19,6) | Y |  |  |
| 38 | VLR_UNIT_ICMSS_REST_SAI | NUMBER(19,6) | Y |  |  |
| 39 | VLR_UNIT_FCP_REST_SAI | NUMBER(19,6) | Y |  |  |
| 40 | VLR_UNIT_ICMSS_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 41 | VLR_UNIT_FCP_COMPL_SAI | NUMBER(19,6) | Y |  |  |
| 42 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 43 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_MOTIVO → DWT_COD_MOTIVO_SPED(COD_MOTIVO_SPED)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- UK_X308_INFO_COMPL_ST_DEV (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, ESPECIE_DOCTO_DEV, NUM_DOCFIS_REF, SERIE_DOCFIS_REF, SUB_SERIE_DOCFIS_REF, IDENT_DOCTO_REF, DATA_FISCAL_REF, IDENT_FIS_JUR_REF, IDENT_MODELO_REF, IDENT_CAIXA_ECF, NUM_COO_REF, DATA_EMISSAO_REF, NUM_EQUIP_REF, NUM_CUPOM_REF, NUM_ITEM_DOC_REF)

---

## X30_ESTOQUE_ICM_ST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 5 | IND_EVENTO | CHAR(1) | N |  |  |
| 6 | COD_EVENTO | VARCHAR2(2) | N |  |  |
| 7 | VLR_ALIQ_12 | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ALIQ_18 | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ALIQ_25 | NUMBER(17,2) | Y |  |  |
| 10 | VLR_ALIQ_OUT | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, IDENT_ESTADO, IND_EVENTO, COD_EVENTO

**FKs**:
- IDENT_ESTADO, IND_EVENTO, COD_EVENTO → ICT_EVENTO_AP_ST(IDENT_ESTADO, IND_EVENTO, COD_EVENTO)

---

## X312_DIMP_MCAPT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MCAPT | VARCHAR2(36) | N |  |  |
| 4 | NUM_LOG | VARCHAR2(36) | Y |  |  |
| 5 | IND_TP_TECN | CHAR(1) | Y |  |  |
| 6 | IND_TERM_PROP | CHAR(1) | Y |  |  |
| 7 | DSC_MARCA | VARCHAR2(50) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 10 | IND_SMARTPOS | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MCAPT

---

## X313_DIMP_MOV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_OPER | DATE | N |  |  |
| 4 | IDENT_PARCEIRA | NUMBER(12) | Y |  |  |
| 5 | IDENT_CLIENTE | NUMBER(12) | N |  |  |
| 6 | IND_COMEX | CHAR(1) | N |  |  |
| 7 | IND_EXTEMP | CHAR(1) | N |  |  |
| 8 | COD_MCAPT | VARCHAR2(36) | N |  |  |
| 9 | VLR_TOTAL | NUMBER(17,2) | N |  |  |
| 10 | QTD_TOTAL | NUMBER(10) | N |  |  |
| 11 | CNPJ_ADQUI | VARCHAR2(14) | Y |  |  |
| 12 | SEQ_NSU | VARCHAR2(30) | Y |  |  |
| 13 | COD_AUTORIZACAO | VARCHAR2(60) | Y |  |  |
| 14 | ID_TRANSACAO | VARCHAR2(60) | Y |  |  |
| 15 | IND_SPLIT | CHAR(1) | N |  |  |
| 16 | BANDEIRA | VARCHAR2(10) | Y |  |  |
| 17 | HORA | VARCHAR2(6) | N |  |  |
| 18 | VLR_OPER | NUMBER(17,2) | N |  |  |
| 19 | IND_OPER_NAT_PAG | CHAR(2) | N |  |  |
| 20 | COD_GEO | VARCHAR2(15) | Y |  |  |
| 21 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 22 | CNPJ_CPF_DEST | VARCHAR2(14) | Y |  |  |
| 23 | COD_DEST | VARCHAR2(30) | Y |  |  |
| 24 | SITUACAO | CHAR(1) | N |  |  |
| 25 | DT_CANCELAMENTO | DATE | Y |  |  |
| 26 | TIPO_CANCELAMENTO | CHAR(1) | Y |  |  |
| 27 | VLR_CANCELAMENTO | NUMBER(17,2) | Y |  |  |
| 28 | COD_CHAVE_NFSE | VARCHAR2(44) | Y |  |  |
| 29 | COD_CHAVE_DCE | VARCHAR2(44) | Y |  |  |
| 30 | IND_SUB | VARCHAR2(1) | N |  |  |
| 31 | UF_ORIGEM | VARCHAR2(2) | Y |  |  |
| 32 | CNPJ_ORIGEM | VARCHAR2(14) | Y |  |  |
| 33 | ID_TRANSAC_COMPL | VARCHAR2(60) | Y |  |  |
| 34 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 35 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 36 | IND_NAT_JUR | VARCHAR2(1) | Y |  | Natureza JurÃ­dica de Origem da OperaÃ§Ã£o (0 â€“ CPF (PF), 1 â€“ CNPJ (PJ)) |
| 37 | IND_TP_PIX | VARCHAR2(1) | Y |  | Indicador do Tipo de Pix (0 â€“ DinÃ¢mico, 1 â€“ EstÃ¡tico) |
| 38 | ID_PEDIDO | VARCHAR2(255) | Y |  | Identificador do Pedido |
| 39 | IND_NAO_GERA_REG | VARCHAR2(1) | Y |  | Indicador p/ NÃ£o Gerar Registro 1500. Preencher esse campo com S, caso a transaÃ§Ã£o nÃ£o deva ser considerada para geraÃ§Ã£o do registro 1500. |
| 40 | DSC_MOTIVO_NAO_GERA_REG | VARCHAR2(255) | Y |  | Descrever o motivo pelo qual a transaÃ§Ã£o nÃ£o deve ser considerada na geraÃ§Ã£o do registro 1500. |
| 41 | DT_LIQUIDACAO | DATE | Y |  |  |
| 42 | UF_DESTINO | VARCHAR2(2) | Y |  |  |
| 43 | IND_TP_REL | VARCHAR2(1) | Y |  |  |
| 44 | IND_INFO_SELLER | VARCHAR2(1) | Y |  |  |
| 45 | ID_SELLER | VARCHAR2(255) | Y |  |  |
| 46 | QTD_CANCELAMENTO | NUMBER(10) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_MCAPT → X312_DIMP_MCAPT(COD_EMPRESA, COD_ESTAB, COD_MCAPT)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CLIENTE → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- UK_X313_DIMP_MOV_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DAT_OPER, IDENT_CLIENTE, SITUACAO, HORA, COD_MCAPT, ID_TRANSACAO)

---

## X314_DIMP_AUTORIZACAO_IP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_FIS_JUR | NUMBER(14) | N |  |  |
| 4 | TP_AUTORIZ | CHAR(1) | N |  |  |
| 5 | TP_TRANSAC | CHAR(1) | N |  |  |
| 6 | DT_INI_AUT | DATE | N |  |  |
| 7 | DT_FIM_AUT | DATE | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 9 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DT_INI_AUT, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X315_DIMP_VAN_CLIENTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_FIS_JUR | NUMBER(14) | N |  |  |
| 4 | DAT_VALIDADE | DATE | N |  |  |
| 5 | CNPJ_VAN | VARCHAR2(14) | N |  |  |
| 6 | RAZAO_SOCIAL_VAN | VARCHAR2(70) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, DAT_VALIDADE, CNPJ_VAN

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X316_DIMP_TRANSACOES_VAN

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | CNPJ_VAN | VARCHAR2(14) | N |  |  |
| 4 | DAT_PERIODO | DATE | N |  |  |
| 5 | QTD | NUMBER(10) | Y |  |  |
| 6 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 7 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 8 | VLR_TRANS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, CNPJ_VAN, DAT_PERIODO

---

## X317_OPER_PAGTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 5 | IDENT_FIS_JUR_IT | NUMBER(12) | Y |  |  |
| 6 | VLR_TOT_OP_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | VLR_TOT_OP_ISS | NUMBER(17,2) | Y |  |  |
| 8 | VLR_TOT_OP_OUTR | NUMBER(17,2) | Y |  |  |
| 9 | USUARIO | VARCHAR2(40) | Y |  |  |
| 10 | DAT_OPERACAO | DATE | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_IT → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- UK_X317_OPER_PAGTO (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_FIS_JUR_IT)

---

## X318_COD_BARRA_COMERC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | GRUPO_PRODUTO | VARCHAR2(9) | N |  |  |
| 2 | IND_PRODUTO | CHAR(1) | N |  |  |
| 3 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 4 | GRUPO_MEDIDA | VARCHAR2(9) | N |  |  |
| 5 | COD_MEDIDA | VARCHAR2(8) | N |  |  |
| 6 | COD_BARRA | VARCHAR2(255) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO, GRUPO_MEDIDA, COD_MEDIDA

---

## X321_SC_DIME_QUAD_15

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_REF | DATE | N |  |  |
| 4 | COD_BENEF_TTD | VARCHAR2(4) | Y |  |  |
| 5 | NUM_CONCESSAO | VARCHAR2(15) | Y |  |  |
| 6 | COD_TIPO3_DCIP | VARCHAR2(4) | Y |  |  |
| 7 | VLR_BC_PREST | NUMBER(17,2) | Y |  |  |
| 8 | VLR_ICMS_PREST | NUMBER(17,2) | Y |  |  |
| 9 | COD_FUMDES | CHAR(1) | Y |  |  |
| 10 | VLR_FUMDES | NUMBER(17,2) | Y |  |  |
| 11 | COD_FUN_SOC | CHAR(1) | Y |  |  |
| 12 | VLR_FUN_SOC | NUMBER(17,2) | Y |  |  |
| 13 | VLR_BC_DEV | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_DEV | NUMBER(17,2) | Y |  |  |
| 15 | VLR_FUMDES_DEV | NUMBER(17,2) | Y |  |  |
| 16 | VLR_FUN_SOC_DEV | NUMBER(17,2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_BENEF_TTD → EST_SC_DIME_BENEF(COD_BENEF_TTD)
- COD_TIPO3_DCIP → EST_SC_DIME_TIPO3(COD_TIPO3_DCIP)

**Indexes**:
- UK_X321_SC_DIME_QUAD_15 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_REF, COD_BENEF_TTD, NUM_CONCESSAO, COD_TIPO3_DCIP)

---

## X323_INVENT_PROD_AVAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INVENTARIO | DATE | N |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | TP_AVALIACAO | VARCHAR2(10) | N |  |  |
| 7 | IDENT_NAT_ESTOQUE | NUMBER(12) | N |  |  |
| 8 | DISCRI_INVENTARIO | VARCHAR2(74) | N |  |  |
| 9 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 10 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 11 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 12 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 13 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 14 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 15 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 16 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 17 | VLR_UNIT | NUMBER(18,6) | Y |  |  |
| 18 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 19 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 20 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 21 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 22 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 23 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 24 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 25 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 26 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, GRUPO_CONTAGEM, IDENT_PRODUTO, TP_AVALIACAO, IDENT_NAT_ESTOQUE, DISCRI_INVENTARIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NAT_ESTOQUE → X2010_NAT_ESTOQUE(IDENT_NAT_ESTOQUE)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- IDENT_ALMOX → X2021_ALMOXARIFADO(IDENT_ALMOX)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## X324_DIMP_TITULAR_CTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_MCAPT | VARCHAR2(36) | N |  |  |
| 4 | IDENT_CLIENTE | NUMBER(12) | N |  |  |
| 5 | DATA_INI | DATE | N |  |  |
| 6 | DATA_FIM | DATE | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_MCAPT, IDENT_CLIENTE, DATA_INI

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_MCAPT → X312_DIMP_MCAPT(COD_EMPRESA, COD_ESTAB, COD_MCAPT)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CLIENTE → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X325_TRIB_ICMS_MONO

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
| 12 | PERC_B100 | NUMBER(7,4) | Y |  |  |
| 13 | PERC_GLP | NUMBER(7,4) | Y |  |  |
| 14 | PERC_GLGN_N | NUMBER(7,4) | Y |  |  |
| 15 | PERC_GLGN_I | NUMBER(7,4) | Y |  |  |
| 16 | IND_ORIGEM_COM | VARCHAR2(1) | Y |  |  |
| 17 | QTD_BC_MONO | NUMBER(17,6) | Y |  |  |
| 18 | ALIQ_AD_REM_ICMS | NUMBER(7,4) | Y |  |  |
| 19 | VLR_ICMS_MONO | NUMBER(17,2) | Y |  |  |
| 20 | QTD_BC_MONO_RETEN | NUMBER(17,6) | Y |  |  |
| 21 | ALIQ_AD_REM_ICMS_RETEN | NUMBER(7,4) | Y |  |  |
| 22 | VLR_ICMS_MONO_RETEN | NUMBER(17,2) | Y |  |  |
| 23 | PERC_RED_AD_REM | NUMBER(7,4) | Y |  |  |
| 24 | DSC_RED_AD_REM | VARCHAR2(1) | Y |  |  |
| 25 | VLR_ICMS_MONO_OP | NUMBER(17,2) | Y |  |  |
| 26 | PERC_DIF | NUMBER(7,4) | Y |  |  |
| 27 | VLR_ICMS_MONO_DIF | NUMBER(17,2) | Y |  |  |
| 28 | QTD_BC_MONO_RET | NUMBER(17,6) | Y |  |  |
| 29 | ALIQ_AD_REM_ICMS_RET | NUMBER(7,4) | Y |  |  |
| 30 | VLR_ICMS_MONO_RET | NUMBER(17,2) | Y |  |  |
| 31 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 32 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 33 | IND_CRED_ICMS | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X326_ORIG_ICMS_MONO

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
| 12 | IND_ORIG | VARCHAR2(1) | N |  |  |
| 13 | IDENT_UF_ORIG | NUMBER(12) | N |  |  |
| 14 | PERC_UF_ORIG | NUMBER(7,4) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, IND_ORIG, IDENT_UF_ORIG

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_UF_ORIG → ESTADO(IDENT_ESTADO)

**Indexes**:
- IDX_X326_ORIG_ICMS_MONO_ESTADO: (IDENT_UF_ORIG)

---

## X32_ARQUIVO_IMPORT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | DSC_ARQUIVO | VARCHAR2(20) | N |  |  |
| 5 | QTD_REGISTROS | NUMBER(8) | Y |  |  |
| 6 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 7 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 8 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, DSC_ARQUIVO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X331_PROG_FIDEL_FAT_NFE

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
| 11 | QTD_PTS_PROG_FIDEL | VARCHAR2(20) | Y |  |  |
| 12 | DAT_AFER_PROG_FIDEL | DATE | Y |  |  |
| 13 | QTD_REGAT_PROG_FIDEL | VARCHAR2(20) | Y |  |  |
| 14 | DAT_REGAT_PROG_FIDEL | DATE | Y |  |  |
| 15 | ANO_MES_REFERENCIA_FAT | VARCHAR2(6) | Y |  |  |
| 16 | DAT_VENCTO | DATE | Y |  |  |
| 17 | COD_BARRAS | VARCHAR2(48) | Y |  |  |
| 18 | COD_DEBITO_AUTO | VARCHAR2(20) | Y |  |  |
| 19 | COD_BANCO_AUTO | VARCHAR2(5) | Y |  |  |
| 20 | COD_AGENCIA_AUTO | VARCHAR2(10) | Y |  |  |
| 21 | COD_QRCODE_PIX | VARCHAR2(2000) | Y |  |  |
| 22 | DATA_CONSUMO_INI | DATE | Y |  |  |
| 23 | DATA_CONSUMO_FIM | DATE | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X332_PROC_RESSARC_NFE

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
| 12 | VLR_UNIT_PROC | NUMBER(21,8) | Y |  |  |
| 13 | QTD_FAT_PROC | NUMBER(15,4) | Y |  |  |
| 14 | VLR_ITEM_PROC | NUMBER(21,8) | Y |  |  |
| 15 | VLR_DESC_PROC | NUMBER(17,2) | Y |  |  |
| 16 | VLR_OUT_DESP_PROC | NUMBER(17,2) | Y |  |  |
| 17 | IND_DEV_PROC | VARCHAR2(1) | Y |  |  |
| 18 | VLR_BC_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ALIQ_ICMS_PROC | NUMBER(7,4) | Y |  |  |
| 20 | VLR_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 21 | VLR_PIS_PROC | NUMBER(17,2) | Y |  |  |
| 22 | VLR_COFINS_PROC | NUMBER(17,2) | Y |  |  |
| 23 | IND_TP_RESSARC | VARCHAR2(2) | Y |  |  |
| 24 | DATA_REF_RESSARC | DATE | Y |  |  |
| 25 | NUM_PROC_RESSARC | VARCHAR2(60) | Y |  |  |
| 26 | NUM_PROT_RESSARC | VARCHAR2(60) | Y |  |  |
| 27 | DSC_OBS_RESSARC | VARCHAR2(100) | Y |  |  |
| 28 | DSC_ADIC_RESSARC | VARCHAR2(500) | Y |  |  |
| 29 | VLR_FCP_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 30 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 31 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X333_PART_UF_DEST_NFE

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
| 12 | IDENT_UF_DESTINO | NUMBER(12) | N |  |  |
| 13 | VLR_BASE_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 14 | PERC_FCP_DEST | NUMBER(5,2) | Y |  |  |
| 15 | VLR_ALIQ_DESTINO | NUMBER(7,4) | Y |  |  |
| 16 | VLR_FCP_UF_DEST | NUMBER(17,2) | Y |  |  |
| 17 | VLR_TRIB_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ICMS_UF_EMIT | NUMBER(17,2) | Y |  |  |
| 19 | COD_BENEF_FISCAL_DEST | VARCHAR2(10) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, IDENT_UF_DESTINO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_UF_DESTINO → ESTADO(IDENT_ESTADO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X334_FUND_TRIB_FED_NFE

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
| 12 | VLR_PIS_RETIDO | NUMBER(23,8) | Y |  |  |
| 13 | VLR_COFINS_RETIDO | NUMBER(23,8) | Y |  |  |
| 14 | VLR_CSLL_RETIDO | NUMBER(23,8) | Y |  |  |
| 15 | VLR_BC_IRRF | NUMBER(23,8) | Y |  |  |
| 16 | VLR_IRRF_RETIDO | NUMBER(23,8) | Y |  |  |
| 17 | VLR_BC_FUST | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ALIQ_FUST | NUMBER(7,4) | Y |  |  |
| 19 | VLR_FUST | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BC_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ALIQ_FUNTTEL | NUMBER(7,4) | Y |  |  |
| 22 | VLR_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

---

## X335_CREDIT_OUTORG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | NUM_ITEM | NUMBER(5) | N | 1 |  |
| 13 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 14 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 15 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 16 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 17 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 18 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 19 | VLR_EST_ITEM | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ALIQ_CRE_OUTORG | NUMBER(7,4) | Y |  |  |
| 21 | VLR_BRUTO_CRE_OUTORG | NUMBER(17,2) | Y |  |  |
| 22 | PRC_ESTORNO | NUMBER(7,4) | Y |  |  |
| 23 | VLR_ESTORNO_OUTORG_ITEM | NUMBER(17,2) | Y |  |  |
| 24 | VLR_LIQUIDO_CRE_OUTORG | NUMBER(17,2) | Y |  |  |
| 25 | OBSERVACAO | VARCHAR2(100) | Y |  |  |
| 26 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, NUM_ITEM

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)

---

## X336_PROD_DISP_COLETA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | PERIODO_REF | VARCHAR2(6) | N |  |  |
| 4 | IDENT_OPER_OBRIG | NUMBER(12) | Y |  |  |
| 5 | IDENT_PRODUTO_OBRIG | NUMBER(12) | Y |  |  |
| 6 | QTDE_ANP | NUMBER(15,4) | Y |  |  |
| 7 | QTDE_KG | NUMBER(15,4) | Y |  |  |
| 8 | IDENT_FIS_JUR_TERC | NUMBER(12) | Y |  |  |
| 9 | IDENT_ESTADO_COLETA | NUMBER(12) | Y |  |  |
| 10 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 11 | IDENT_CNAE_OBRIG | NUMBER(12) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR_TERC → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_ESTADO_COLETA → ESTADO(IDENT_ESTADO)
- IDENT_ESTADO_COLETA, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_PRODUTO_OBRIG → PRT_PROD_OBRIG(IDENT_PRODUTO_OBRIG)
- IDENT_OPER_OBRIG → PRT_OPER_OBRIG(IDENT_OPER_OBRIG)
- IDENT_CNAE_OBRIG → PRT_CNAE_OBRIG(IDENT_CNAE_OBRIG)

**Indexes**:
- UK_X336_PROD_DISP_COLETA (UNIQUE): (COD_EMPRESA, COD_ESTAB, PERIODO_REF, IDENT_OPER_OBRIG, IDENT_PRODUTO_OBRIG, IDENT_FIS_JUR_TERC, IDENT_ESTADO_COLETA, COD_MUNICIPIO)

---

## X33_BASE_CONCILIA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 5 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 6 | GRUPO_DOCTO | VARCHAR2(9) | N |  |  |
| 7 | COD_DOCTO | VARCHAR2(5) | N |  |  |
| 8 | GRUPO_FIS_JUR | VARCHAR2(9) | N |  |  |
| 9 | IND_FIS_JUR | VARCHAR2(1) | N |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | N |  |  |
| 11 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 12 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | COD_CFO | VARCHAR2(4) | Y |  |  |
| 15 | COD_NATUREZA_OP | VARCHAR2(3) | Y |  |  |
| 16 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 17 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 22 | VLR_INSS | NUMBER(17,2) | Y |  |  |
| 23 | BASE_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | BASE_ISEN_ICMS | NUMBER(17,2) | Y |  |  |
| 25 | BASE_OUTR_ICMS | NUMBER(17,2) | Y |  |  |
| 26 | BASE_TRIB_IPI | NUMBER(17,2) | Y |  |  |
| 27 | BASE_ISEN_IPI | NUMBER(17,2) | Y |  |  |
| 28 | BASE_OUTR_IPI | NUMBER(17,2) | Y |  |  |
| 29 | BASE_TRIB_ISS | NUMBER(17,2) | Y |  |  |
| 30 | BASE_ISEN_ISS | NUMBER(17,2) | Y |  |  |
| 31 | BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 32 | BASE_INSS | NUMBER(17,2) | Y |  |  |
| 33 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 34 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, GRUPO_DOCTO, COD_DOCTO, GRUPO_FIS_JUR, IND_FIS_JUR, COD_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## X34_MOVTO_INSUMO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NORM_DEV | CHAR(1) | N |  |  |
| 5 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | DATA_MOVTO | DATE | N |  |  |
| 8 | NUM_DOCTO | VARCHAR2(15) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 12 | DISCRI_ESTOQUE | VARCHAR2(52) | N |  |  |
| 13 | NUM_ITEM | NUMBER(5) | N |  |  |
| 14 | IDENT_PRODUTO_INS | NUMBER(12) | N |  |  |
| 15 | IDENT_UND_PAD_INS | NUMBER(12) | Y |  |  |
| 16 | QTD_MOVTO_INS | NUMBER(17,6) | Y |  |  |
| 17 | CUSTO_UNIT_INS | NUMBER(18,6) | Y |  |  |
| 18 | IDENT_LEGENDA_INS | NUMBER(12) | Y |  |  |
| 19 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 20 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 21 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 24 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 25 | NUM_DOCTO_INS | VARCHAR2(15) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DATA_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM, IDENT_PRODUTO_INS

**FKs**:
- COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DATA_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM → X10_ESTOQUE(COD_EMPRESA, COD_ESTAB, MOVTO_E_S, NORM_DEV, GRUPO_CONTAGEM, IDENT_DOCTO, DATA_MOVTO, NUM_DOCTO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO, DISCRI_ESTOQUE, NUM_ITEM)
- IDENT_PRODUTO_INS → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_UND_PAD_INS → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- IDENT_LEGENDA_INS → X2008_LEGENDA_PRD(IDENT_LEGENDA)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)

---

## X38_FORNECEDOR_OBRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 2 | COD_CANAL_DISTRIB | VARCHAR2(15) | N |  |  |
| 3 | VALID_FORNEC_OBRA | DATE | Y |  |  |
| 4 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 5 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_FIS_JUR, COD_CANAL_DISTRIB

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_CANAL_DISTRIB → DWT_CANAIS_DISTRIB(COD_CANAL_DISTRIB)

**Indexes**:
- IX_FK_SAF_1965: (IDENT_FIS_JUR)

---

## X39_PFJ_EMPRESA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 3 | DATA_VALID_INI | DATE | N |  |  |
| 4 | IND_TIPO_RELAC | CHAR(1) | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 7 | DATA_VALID_FIM | DATE | Y |  |  |
| 8 | IND_TIPO_RELAC_SPED | VARCHAR2(2) | Y |  |  |

**PK**: COD_EMPRESA, IDENT_FIS_JUR, DATA_VALID_INI

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_EMPRESA → EMPRESA(COD_EMPRESA)

**Indexes**:
- IX_FK_SAF_2086: (IDENT_FIS_JUR)

---

## X40_CONTABIL_COMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMPANHIA | VARCHAR2(10) | N |  |  |
| 4 | DATA_LANCTO | DATE | N |  |  |
| 5 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 6 | IND_DEB_CRE | CHAR(1) | N |  |  |
| 7 | ARQUIVAMENTO | VARCHAR2(50) | N |  |  |
| 8 | IDENT_CONTRA_PART | NUMBER(12) | Y |  |  |
| 9 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_DESPESA | NUMBER(12) | Y |  |  |
| 11 | IDENT_HISTPADRAO | NUMBER(12) | Y |  |  |
| 12 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 13 | TXT_HISTCOMPL | VARCHAR2(255) | Y |  |  |
| 14 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 15 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 16 | VLR_LANCTO_CONV | NUMBER(18,4) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMPANHIA, DATA_LANCTO, IDENT_CONTA, IND_DEB_CRE, ARQUIVAMENTO

**FKs**:
- COD_EMPRESA, COD_ESTAB, COD_COMPANHIA → DWT_COMPANHIA(COD_EMPRESA, COD_ESTAB, COD_COMPANHIA)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CONTRA_PART → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_DESPESA → X2004_CENTRO_DESP(IDENT_DESPESA)
- IDENT_HISTPADRAO → X2020_HIST_PADRAO(IDENT_HISTPADRAO)
- COD_INDICE → Y2046_INDICE(COD_INDICE)

**Indexes**:
- IX_X40_CONTABIL_CTA: (IDENT_CONTA)
- IX_X40_CONTABIL_CTA_PART: (IDENT_CONTRA_PART)

---

## X41_SALDOS_COMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_COMPANHIA | VARCHAR2(10) | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | DATA_SALDO | DATE | N |  |  |
| 6 | VLR_SALDO_INI | NUMBER(17,2) | Y |  |  |
| 7 | IND_SALDO_INI | CHAR(1) | Y |  |  |
| 8 | VLR_SALDO_FIM | NUMBER(17,2) | Y |  |  |
| 9 | IND_SALDO_FIM | CHAR(1) | Y |  |  |
| 10 | VLR_TOT_CRE | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_COMPANHIA, IDENT_CONTA, DATA_SALDO

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- COD_EMPRESA, COD_ESTAB, COD_COMPANHIA → DWT_COMPANHIA(COD_EMPRESA, COD_ESTAB, COD_COMPANHIA)

**Indexes**:
- IX_X41_SALDOS_COMP: (COD_EMPRESA, COD_COMPANHIA, DATA_SALDO)
- IX_X41_SALDOS_CTA: (IDENT_CONTA)

---

## X42_CAPA_TELECOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | IND_TP_REGISTRO | CHAR(1) | Y |  |  |
| 9 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 10 | DAT_SAIDA | DATE | Y |  |  |
| 11 | COD_CLASSE_USU | VARCHAR2(3) | Y |  |  |
| 12 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 13 | IND_TP_RECEITA | CHAR(1) | Y |  |  |
| 14 | TEL_CLIENTE | VARCHAR2(15) | Y |  |  |
| 15 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 17 | VLR_OUTRAS_DESP | NUMBER(17,2) | Y |  |  |
| 18 | VLR_ABAT_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TOT_PAGAR | NUMBER(17,2) | Y |  |  |
| 20 | SITUACAO | CHAR(1) | Y |  |  |
| 21 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 24 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 25 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 27 | VLR_BASE_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 28 | VLR_TRIB_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 29 | VLR_ALIQ_ICMS_DEST | NUMBER(7,4) | Y |  |  |
| 30 | TEL_USU | VARCHAR2(15) | Y |  |  |
| 31 | DAT_VENCTO | DATE | Y |  |  |
| 32 | MES_REFERENCIA | NUMBER(2) | Y |  |  |
| 33 | ANO_REFERENCIA | NUMBER(4) | Y |  |  |
| 34 | COD_LOCALIDADE | VARCHAR2(10) | Y |  |  |
| 35 | IDENT_ESTADO_DEST | NUMBER(12) | Y |  |  |
| 36 | COND_PARTICIPANTE | VARCHAR2(2) | Y |  |  |
| 37 | COD_PARTICIPANTE | VARCHAR2(2) | Y |  |  |
| 38 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 39 | COD_OP_TELECOM | VARCHAR2(2) | Y |  |  |
| 40 | COD_USU_FINAL | VARCHAR2(10) | Y |  |  |
| 41 | COD_BARRAS | VARCHAR2(48) | Y |  |  |
| 42 | NUM_CICLO | VARCHAR2(7) | Y |  |  |
| 43 | VLR_SUBST_TRIB | NUMBER(17,2) | Y |  |  |
| 44 | VLR_BASE_SUB_TRIB | NUMBER(17,2) | Y |  |  |
| 45 | OBSERVACAO | VARCHAR2(200) | Y |  |  |
| 46 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 47 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 48 | VLR_DESC_COND | NUMBER(17,2) | Y |  |  |
| 49 | COD_AUTENTIC | VARCHAR2(32) | Y |  |  |
| 50 | COD_TP_UTIL | VARCHAR2(2) | Y |  | CONVENIO 115, ATO COTEPE 70 - reg C705, D405 :Tipo de Ligação (energia elétrica), ou Tipo de Utilização (telecomunicação, comunicação). Preenchimento conforme tabela 11.2 do Convênio 115/133. |
| 51 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 52 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 53 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 54 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 55 | COD_CANAL_DISTRIB | VARCHAR2(15) | Y |  |  |
| 56 | DAT_FATO_GERADOR | DATE | Y |  |  |
| 57 | DAT_CANCELAMENTO | DATE | Y |  |  |
| 58 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 59 | GRUPO_TENSAO | VARCHAR2(2) | Y |  | CONVENIO 115, ATO COTEPE 70 - reg C705 : Grupo de tensão (energia elétrica). Preenchimento conforme tabela 11.3 do Convênio 115/133. |
| 60 | CONTA_CONSUMO | VARCHAR2(10) | Y |  |  |
| 61 | UF_TEL_CLIENTE | VARCHAR2(2) | Y |  |  |
| 62 | IND_CONVENIO_115 | CHAR(1) | Y |  |  |
| 63 | COD_SIT_DOCFIS | VARCHAR2(2) | Y |  | ATO COTEPE 70 - reg C700, D400 : Código da situação do doc. fiscal: 00 - regular, 01 - extemporâneo, 02 - cancelado, 03 - cancelamento de cupom fiscal anterior, 04 - extemporâneo cancelado, 05 - desfazimento, 06 - doc referenciado - SITUACAO_DOCFIS_V |
| 64 | IDENT_CLASSE_CONSUMO | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C700, D400 : Código da Classe de Consumo  (energia elétrica, gás, água, telecomunicação, comunicação) - DWT_CLASSE_CONSUMO. |
| 65 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C700, D400 : Natureza de Operação  (energia elétrica, gás, telecomunicação, comunicação). |
| 66 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  | ATO COTEPE 70 - reg C700, D400 : Especificação do Tipo de Receita (energia elétrica, gás, água, telecomunicação, comunicação). Valores Assumidos: 0 - Receita Própria - serviços prestados; 1 - Receita Própria - cobrança de débitos; 2 - Receita Própria - venda de mercadorias; 3 - Receita Própria - venda de serviço pré-pago; 4 - Outras Receitas Próprias; 5 - Receita de Terceiros (co-faturamento); 9 - Outras Receitas de Terceiros. |
| 67 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C700, D400 :  código da observação da x2009_observacao (energia elétrica, gás, telecomunicação, comunicação). |
| 68 | NUM_CONTRATO | VARCHAR2(20) | Y |  | ATO COTEPE 70 - reg C705, D405 : Número do Contrato, ou Código da Unidade de Consumo (energia elétrica), ou Identificação do Terminal Faturado (telecomunicação, comunicação). |
| 69 | COD_AREA_TERMINAL | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg D405 : Código da Área do Terminal Faturado (telecomunicação, comunicação). |
| 70 | DATA_CONSUMO_INI | DATE | Y |  | ATO COTEPE 70 - reg C705, D405 : Data início do consumo de energia (energia elétrica), ou data início da prestação do serviço (telecomunicação, comunicação). |
| 71 | DATA_CONSUMO_FIM | DATE | Y |  | ATO COTEPE 70 - reg C705, D405 : Data final do consumo de energia (energia elétrica), ou data final da prestação do serviço (telecomunicação, comunicação). |
| 72 | DATA_CONSUMO_LEIT | DATE | Y |  | ATO COTEPE 70 - reg C705 : Data da leitura do ponto de consumo (energia elétrica). |
| 73 | QTD_CONTRATADA_PONTA | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 : Demanda contratada Ponta, KW (energia elétrica). |
| 74 | QTD_CONTRATADA_FPONTA | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 :  Demanda contratada Fora-Ponta, KW (energia elétrica). |
| 75 | QTD_CONSUMO_TOTAL | NUMBER(17,6) | Y |  | ATO COTEPE 70 - reg C705 : Consumo Total, KW(energia elétrica). |
| 76 | IDENT_UF_CONSUMO | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C770, D470 : UF do Ponto de Consumo (energia elétrica, gás, água), ou UF do Terminal Faturado (telecomunicação, comunicação). |
| 77 | COD_MUNIC_CONSUMO | NUMBER(5) | Y |  | ATO COTEPE 70 - reg C770, D470 : Município do Ponto de Consumo (energia elétrica, gás, água), ou Município do Terminal Faturado (telecomunicação, comunicação). |
| 78 | VLR_TERCEIROS | NUMBER(17,2) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 79 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 80 | NUM_NFCEE_SUBST | VARCHAR2(12) | Y |  | Campo com as mesmas características do Número da Nota Fiscal, receberá informação do número do Documento Fiscal que Substituiu o Documento emitido de forma errônea. |
| 81 | SERIE_NFCEE_SUBST | VARCHAR2(3) | Y |  | Campo com as mesmas características da Série da Nota Fiscal, receberá informação do número da Série que Substituiu o Documento emitido de forma errônea. |
| 82 | HIPOTESE_ESTORNO | VARCHAR2(1) | Y |  | (1)Erro ocorrido no faturamento do Produto ou na emissão do Documento Fiscal, (2)Erro na Medição, Faturamento ou tarifação do produto., (3)Formalização de discordância do consumidor, (4)Cobrança em Duplicidade |
| 83 | MOTIVO_ESTORNO | VARCHAR2(200) | Y |  | Campo de texto Livre que irá detalhar a hipótese de estorno do Documento Fiscal. |
| 84 | IND_NF_REG_ESP | CHAR(1) | Y |  |  |
| 85 | IND_NF_ESP | CHAR(1) | Y |  |  |
| 86 | IND_CONS_FINAL | CHAR(1) | Y |  | Campo identificador de consumidor final(S/N) |
| 87 | NUM_MEDIDOR | VARCHAR2(12) | Y |  |  |
| 88 | IDENT_CLASSE_CONSUMO_SEF_PE | NUMBER(12) | Y |  |  |
| 89 | DSC_AUTOR_ACAO | VARCHAR2(70) | Y |  |  |
| 90 | NUM_PROC_ACAO | VARCHAR2(24) | Y |  |  |
| 91 | NUM_VARA_ACAO | VARCHAR2(2) | Y |  |  |
| 92 | DAT_ACAO | DATE | Y |  |  |
| 93 | VLR_DEPOSITO | NUMBER(17,2) | Y |  |  |
| 94 | DAT_DEPOSITO | DATE | Y |  |  |
| 95 | COD_BANCO | VARCHAR2(3) | Y |  |  |
| 96 | NUM_AGENCIA_ACAO | VARCHAR2(6) | Y |  |  |
| 97 | NUM_CONTA_ACAO | VARCHAR2(18) | Y |  |  |
| 98 | NUM_LANCTO_CONTABIL | VARCHAR2(40) | Y |  |  |
| 99 | NUM_DOCFIS_RESSARC | VARCHAR2(12) | Y |  |  |
| 100 | SERIE_DOCFIS_RESSARC | VARCHAR2(3) | Y |  |  |
| 101 | IDENT_MODELO_RESSARC | NUMBER(12) | Y |  |  |
| 102 | DAT_EMISSAO_RESSARC | DATE | Y |  |  |
| 103 | IDENTIF_DOCFIS_UT | VARCHAR2(128) | Y |  |  |
| 104 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |
| 105 | DAT_EMIS_NFCEE_SUBST | DATE | Y |  |  |
| 106 | DAT_VENCTO_NFCEE_SUBST | DATE | Y |  |  |
| 107 | VLR_TOT_NFCEE_SUBST | NUMBER(17,2) | Y |  |  |
| 108 | VLR_BASE_NFCEE_SUBST | NUMBER(17,2) | Y |  |  |
| 109 | VLR_ICMS_NFCEE_SUBST | NUMBER(17,2) | Y |  |  |
| 110 | NUM_ITEM_RESSARC | NUMBER(3) | Y |  |  |
| 111 | QTD_ENERGIA_INJ | NUMBER(17,6) | Y |  |  |
| 112 | VLR_ENERGIA_INJ | NUMBER(17,2) | Y |  |  |
| 113 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 114 | COD_TP_CLIENTE | VARCHAR2(2) | Y |  |  |
| 115 | COD_SUBCLASSE_CONSUMO | VARCHAR2(2) | Y |  |  |
| 116 | NUM_TERMINAL_TEL | VARCHAR2(15) | Y |  |  |
| 117 | NUM_FAT_COM | VARCHAR2(20) | Y |  |  |
| 118 | VLR_TOTAL_FAT | NUMBER(17,2) | Y |  |  |
| 119 | DAT_CONS_ANT_LEIT | DATE | Y |  |  |
| 120 | NUM_DOCFIS_SUBST | VARCHAR2(12) | Y |  |  |
| 121 | SERIE_DOCFIS_SUBST | VARCHAR2(3) | Y |  |  |
| 122 | IDENT_MODELO_SUBST | NUMBER(12) | Y |  |  |
| 123 | DAT_EMIS_SUBST | DATE | Y |  |  |
| 124 | PERIOD_APUR_SUBST | DATE | Y |  |  |
| 125 | NUM_AUTENTIC_NFE | VARCHAR2(80) | Y |  |  |
| 126 | DAT_EMISSAO_NFE | DATE | Y |  |  |
| 127 | IND_FIN_EMISSAO_NFE | VARCHAR2(1) | Y |  |  |
| 128 | NUM_AUTENTIC_NFE_SUBST | VARCHAR2(80) | Y |  |  |
| 129 | COD_AUTENTIC_NFE_SUBST | VARCHAR2(32) | Y |  |  |
| 130 | VLR_OUTRAS_DED | NUMBER(17,2) | Y |  |  |
| 131 | IND_TP_FAT_NFE | VARCHAR2(1) | Y |  |  |
| 132 | IND_TP_AMB_NFE | VARCHAR2(1) | Y |  |  |
| 133 | COD_NF_NFE | VARCHAR2(7) | Y |  |  |
| 134 | COD_DV_NFE | VARCHAR2(1) | Y |  |  |
| 135 | IND_PRE_PAGO | VARCHAR2(1) | Y |  |  |
| 136 | IND_SESSAO_REDE | VARCHAR2(1) | Y |  |  |
| 137 | DAT_INI_CONTRATO | DATE | Y |  |  |
| 138 | DAT_FIM_CONTRATO | DATE | Y |  |  |
| 139 | IDENT_UF_TERMINAL_TEL | NUMBER(12) | Y |  |  |
| 140 | COD_MOTIVO_SUBST | VARCHAR2(2) | Y |  |  |
| 141 | VLR_ICMS_DESONERADO | NUMBER(17,2) | Y |  |  |
| 142 | VLR_FCP | NUMBER(17,2) | Y |  |  |
| 143 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 144 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 145 | VLR_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 146 | VLR_FUST | NUMBER(17,2) | Y |  |  |
| 147 | VLR_PIS_RETIDO | NUMBER(17,2) | Y |  |  |
| 148 | VLR_COFINS_RETIDO | NUMBER(17,2) | Y |  |  |
| 149 | VLR_CSLL_RETIDO | NUMBER(17,2) | Y |  |  |
| 150 | VLR_IRRF_RETIDO | NUMBER(17,2) | Y |  |  |
| 151 | QTD_PTS_PROG_FIDEL | NUMBER(20) | Y |  |  |
| 152 | DAT_AFER_PROG_FIDEL | DATE | Y |  |  |
| 153 | QTD_REGAT_PROG_FIDEL | NUMBER(20) | Y |  |  |
| 154 | DAT_REGAT_PROG_FIDEL | DATE | Y |  |  |
| 155 | COD_QRCODE_PIX | VARCHAR2(2000) | Y |  |  |
| 156 | CNPJ_EMIT_FATURAMENTO | VARCHAR2(14) | Y |  |  |
| 157 | IDENT_UF_EMIT_FATURAMENTO | NUMBER(12) | Y |  |  |
| 158 | CNPJ_DOWNLOAD | VARCHAR2(14) | Y |  |  |
| 159 | CPF_DOWNLOAD | VARCHAR2(11) | Y |  |  |
| 160 | COD_DEBITO_AUTO | VARCHAR2(30) | Y |  |  |
| 161 | COD_BANCO_AUTO | VARCHAR2(10) | Y |  |  |
| 162 | COD_AGENCIA_AUTO | VARCHAR2(15) | Y |  |  |
| 163 | COD_AUTENTIC_COF | VARCHAR2(44) | Y |  |  |
| 164 | CNPJ_EMIT_COF | VARCHAR2(14) | Y |  |  |
| 165 | IDENT_MODELO_COF | NUMBER(12) | Y |  |  |
| 166 | SERIE_DOCFIS_COF | VARCHAR2(3) | Y |  |  |
| 167 | NUM_DOCFIS_COF | VARCHAR2(12) | Y |  |  |
| 168 | ANO_MES_COF | VARCHAR2(6) | Y |  |  |
| 169 | COD_HASH_COF | VARCHAR2(32) | Y |  |  |
| 170 | DAT_CRIACAO | DATE | Y |  |  |
| 171 | DAT_ALTERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_CLASSE_CONSUMO → DWT_CLASSE_CONSUMO(IDENT_CLASSE_CONSUMO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_UF_CONSUMO, COD_MUNIC_CONSUMO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_CLASSE_CONSUMO_SEF_PE → DWT_CLASSE_CONSUMO(IDENT_CLASSE_CONSUMO)
- COD_BANCO → DWT_BANCOS(COD_BANCO)
- IDENT_MODELO_RESSARC → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)
- IDENT_MODELO_SUBST → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_UF_TERMINAL_TEL → ESTADO(IDENT_ESTADO)
- IDENT_UF_EMIT_FATURAMENTO → ESTADO(IDENT_ESTADO)

**Indexes**:
- IX2_X42_CAPA_TELECOM: (COD_EMPRESA, NUM_DOCFIS, DAT_FISCAL, COD_ESTAB, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR)
- IX_FK_SAF_1367: (IDENT_FIS_JUR)
- IX_FK_SAF_2107: (IDENT_OBSERVACAO)
- IX_X42_CAPA_TELECOM: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL)
- IX_X42_CAPA_TELECOM_CICLO: (NUM_CICLO, DAT_FISCAL, COD_EMPRESA, SERIE_DOCFIS, COD_ESTAB, SUB_SERIE_DOCFIS, COD_CLASS_DOC_FIS, NUM_DOCFIS)
- IX_X42_CAPA_TELECOM_D: (COD_EMPRESA, COD_ESTAB, DAT_VENCTO)
- IX_X42_CAPA_TELECOM_VENCTO: (DAT_VENCTO, NUM_CICLO, COD_EMPRESA, SERIE_DOCFIS, COD_ESTAB, SUB_SERIE_DOCFIS, COD_CLASS_DOC_FIS, NUM_DOCFIS)
- IX_X42_CAPA_TEL_CTA: (IDENT_CONTA)

---

## X431_ITEM_TELECOM_NEG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_ITEM | NUMBER(7) | N |  |  |
| 9 | IND_ITEM_DED | CHAR(1) | Y |  |  |
| 10 | NUM_ITEM_CONSOL | NUMBER(7) | Y |  |  |
| 11 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 12 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 13 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 14 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 15 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 16 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  |  |
| 17 | QTD_CONTRATADA | NUMBER(17,6) | Y |  |  |
| 18 | QTD_FORNECIDA | NUMBER(17,6) | Y |  |  |
| 19 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 20 | VLR_OUTRAS_DESP | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 22 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 24 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 27 | DSC_PRD_SERV | VARCHAR2(50) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 30 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 31 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 33 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 34 | IND_DESC_JUD | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X42_CAPA_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## X432_ITEM_TELECOM_PROC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_ITEM | NUMBER(7) | N |  |  |
| 9 | IND_TP_PROCESSO | CHAR(1) | N |  |  |
| 10 | NUM_PROCESSO_NF | VARCHAR2(60) | N |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM, IND_TP_PROCESSO, NUM_PROCESSO_NF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM → X43_ITEM_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM)

---

## X433_CTRL_CRED_EE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_APURACAO | DATE | N |  |  |
| 4 | NUM_INSTAL_INJ | VARCHAR2(12) | N |  |  |
| 5 | DAT_REF_INJ | DATE | N |  |  |
| 6 | COD_POSTO_INJ | VARCHAR2(2) | N |  |  |
| 7 | VLR_TARIFA_INJ | NUMBER(11,6) | Y |  |  |
| 8 | QTD_ENERGIA_INI | NUMBER(13,3) | Y |  |  |
| 9 | QTD_ENERGIA_INJ | NUMBER(12,3) | Y |  |  |
| 10 | QTD_ENERGIA_SAI | NUMBER(12,3) | Y |  |  |
| 11 | QTD_ENERGIA_FIM | NUMBER(13,3) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |
| 14 | USUARIO | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, NUM_INSTAL_INJ, DAT_REF_INJ, COD_POSTO_INJ

---

## X43_ITEM_TELECOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | NUM_ITEM | NUMBER(7) | N |  |  |
| 9 | IND_TP_REGISTRO | CHAR(1) | Y |  |  |
| 10 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 11 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 12 | DAT_SERVICO | DATE | Y |  |  |
| 13 | HR_SERVICO | VARCHAR2(6) | Y |  |  |
| 14 | TM_DURACAO | VARCHAR2(8) | Y |  |  |
| 15 | TEL_DESTINO | VARCHAR2(15) | Y |  |  |
| 16 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 17 | VLR_SERVICO | NUMBER(17,2) | Y |  |  |
| 18 | IND_ADIC_DESC | CHAR(1) | Y |  |  |
| 19 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 20 | VLR_TRIB_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_ICMS_1 | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_ICMS_2 | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ICMS_3 | NUMBER(17,2) | Y |  |  |
| 24 | VLR_BASE_ICMS_4 | NUMBER(17,2) | Y |  |  |
| 25 | VLR_BASE_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 26 | VLR_TRIB_ICMS_DEST | NUMBER(17,2) | Y |  |  |
| 27 | VLR_ALIQ_ICMS_DEST | NUMBER(7,4) | Y |  |  |
| 28 | DSC_PRD_SERV | VARCHAR2(50) | Y |  |  |
| 29 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 30 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 31 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 32 | COD_CLASS_SERV | CHAR(1) | Y |  |  |
| 33 | TEL_ACESSO | VARCHAR2(15) | Y |  |  |
| 34 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 35 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 36 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 37 | VLR_SUBST_TRIB | NUMBER(17,2) | Y |  |  |
| 38 | VLR_BASE_SUB_TRIB | NUMBER(17,2) | Y |  |  |
| 39 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 40 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 41 | VLR_DESC_COND | NUMBER(17,2) | Y |  |  |
| 42 | COD_CLASS_ITEM | VARCHAR2(4) | Y |  | CONVENIO 115, ATO COTEPE 70 - reg C750, D450 : Classificação do Item. Preenchimento conforme tabela 11.5 do Convênio 115/133 (energia elétrica, gás, água, telecomunicação, comunicação). |
| 43 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 44 | QTD_CONTRATADA | NUMBER(17,6) | Y |  |  |
| 45 | QTD_FORNECIDA | NUMBER(17,6) | Y |  |  |
| 46 | VLR_OUTRAS_DESP | NUMBER(17,2) | Y |  |  |
| 47 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 48 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 49 | VLR_BASE_ISS_2 | NUMBER(17,2) | Y |  |  |
| 50 | VLR_BASE_ISS_3 | NUMBER(17,2) | Y |  |  |
| 51 | CONTRATO | VARCHAR2(14) | Y |  |  |
| 52 | CNPJ_OPERADORA | VARCHAR2(14) | Y |  | MEIO MAGNÉTICO - REG 77, ATO COTEPE 70 - reg C750, D450 : CNPJ do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 53 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 54 | CPF_OPERADORA | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C750, D450 : CPF do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 55 | IDENT_UF_OPERADORA | NUMBER(12) | Y |  | ATO COTEPE 70 - reg C750, D450 : UF do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 56 | INS_EST_OPERADORA | VARCHAR2(14) | Y |  | ATO COTEPE 70 - reg C750, D450 : Inscrição Estadual do receptor da receita, terceiro da operação (energia elétrica, gás, telecomunicação, comunicação). |
| 57 | IND_ESPECIF_RECEITA | CHAR(1) | Y |  | ATO COTEPE 70 - reg C750, D450 : Especificação do Tipo de Receita (energia elétrica, gás, água, telecomunicação, comunicação). Valores Assumidos: 0 - Receita Própria - serviços prestados; 1 - Receita Própria - cobrança de débitos; 2 - Receita Própria - venda de mercadorias; 3 - Receita Própria - venda de serviço pré-pago; 4 - Outras Receitas Próprias; 5 - Receita de Terceiros (co-faturamento); 9 - Outras Receitas de Terceiros. |
| 58 | VLR_UNIT | NUMBER(19,4) | Y |  | ATO COTEPE 70 - reg C750, D450 : Valor Unitário (energia elétrica, gás, água, telecomunicação, comunicação). Valores Assumidos: 0 - Receita Própria - serviços prestados; 1 - Receita Própria - cobrança de débitos; 2 - Receita Própria - venda de mercadorias; 3 - Receita Própria - venda de serviço pré-pago; 4 - Outras Receitas Próprias; 5 - Receita de Terceiros (co-faturamento); 9 - Outras Receitas de Terceiros. |
| 59 | IND_SERV_PPAGO | CHAR(1) | Y |  | Indicador se o item é referente a serviço pré-pago |
| 60 | NUM_CARTAO_PPAGO | VARCHAR2(20) | Y |  | Número do cartão/PIN/assemelhado - serviço pré-pago |
| 61 | COD_MODALIDADE_PPAGO | VARCHAR2(2) | Y |  | Modalidade de ativação do credito - serviço pré-pago: 01 - Cartão físico; 02 - On-line sem PIN; 03 - Eletrônica com PIN; 04 - Por conta e ordem de terceiros; 05 - Outras modalidades |
| 62 | HORA_DISP_CRED_PPAGO | NUMBER(6) | Y |  | hora de disponibilização do crédito - serviço pré-pago  |
| 63 | DATA_DISP_CRED_PPAGO | DATE | Y |  | data de disponibilização do crédito - serviço pré-pago  |
| 64 | UF_ACESSO | VARCHAR2(2) | Y |  |  |
| 65 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 66 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 67 | DATA_DOCFIS_REF | DATE | Y |  |  |
| 68 | AG_ARREC | VARCHAR2(20) | Y |  | agente arrecadador |
| 69 | UF_RECARGA | VARCHAR2(2) | Y |  |  |
| 70 | DT_PRIM_RECARGA | DATE | Y |  |  |
| 71 | HR_PRIM_RECARGA | NUMBER(6) | Y |  |  |
| 72 | DT_ULT_RECARGA | DATE | Y |  |  |
| 73 | HR_ULT_RECARGA | NUMBER(6) | Y |  |  |
| 74 | NUM_LOTE_PIN | VARCHAR2(20) | Y |  |  |
| 75 | VLR_TERCEIROS | NUMBER(17,2) | Y |  | Valor de Terceiros ATO COTEPE - REG C700 |
| 76 | COD_CLASS_IT_CTP | VARCHAR2(3) | Y |  | Cod. Classificacao do Item p/ ATO COTEPE - REG C750 |
| 77 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 78 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 79 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 80 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 81 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 82 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 83 | IDENT_FIS_RECEITA | NUMBER(12) | Y |  |  |
| 84 | VLR_ALIQ_ICMS_ST | NUMBER(7,4) | Y |  |  |
| 85 | IND_TP_SERV | CHAR(1) | Y |  |  |
| 86 | DAT_INIC_SERV | DATE | Y |  |  |
| 87 | DAT_FINAL_SERV | DATE | Y |  |  |
| 88 | COD_AREA_TERM_FAT | VARCHAR2(14) | Y |  |  |
| 89 | COD_TERM_FAT | VARCHAR2(20) | Y |  |  |
| 90 | COD_OBS_VCONT_COMP | VARCHAR2(10) | Y |  | Código do Amparo/Texto/Ocorrência para ICMS Próprio |
| 91 | VLR_ICMS_NDESTAC | NUMBER(17,2) | Y |  |  |
| 92 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 93 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 94 | IND_TP_REC_PIS_COFINS | CHAR(1) | Y |  |  |
| 95 | IND_TIPO_JUD | CHAR(1) | Y |  |  |
| 96 | VLR_BASE_ICMS_JUD | NUMBER(17,2) | Y |  |  |
| 97 | VLR_ICMS_JUD | NUMBER(17,2) | Y |  |  |
| 98 | VLR_ICMS_EST_RET | NUMBER(17,2) | Y |  |  |
| 99 | HIPOTESE_ESTORNO | VARCHAR2(1) | Y |  |  |
| 100 | MOTIVO_ESTORNO | VARCHAR2(200) | Y |  |  |
| 101 | NUM_CTRL_RECL | VARCHAR2(20) | Y |  |  |
| 102 | VLR_ICMS_FECEP | NUMBER(17,2) | Y |  |  |
| 103 | VLR_ALIQ_ICMS_FECEP | NUMBER(7,4) | Y |  |  |
| 104 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 105 | VLR_BC_ICMS_UF | NUMBER(17,2) | Y |  |  |
| 106 | VLR_ICMS_UF | NUMBER(17,2) | Y |  |  |
| 107 | VLR_ACUM_DE_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 108 | VLR_ACUM_DE_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 109 | NUM_ITEM_REAL | NUMBER(7) | Y |  |  |
| 110 | NUM_CONTRATO | VARCHAR2(15) | Y |  |  |
| 111 | QTD_FATURADA | NUMBER(17,6) | Y |  |  |
| 112 | VLR_TARIFA | NUMBER(21,6) | Y |  |  |
| 113 | IND_TIPO_RED | VARCHAR2(2) | Y |  |  |
| 114 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 115 | VLR_ICMS_ST_FECEP | NUMBER(17,2) | Y |  |  |
| 116 | VLR_SERV_N_TRIB | NUMBER(17,2) | Y |  |  |
| 117 | COD_GRUPO_CCLASS | VARCHAR2(3) | Y |  |  |
| 118 | VLR_OUTRAS_DED | NUMBER(17,2) | Y |  |  |
| 119 | VLR_ENERGIA_COMP | NUMBER(17,2) | Y |  |  |
| 120 | IDENT_OBSERVACAO | NUMBER(12) | Y |  |  |
| 121 | COD_AUTENTIC_NFE_ANT | VARCHAR2(44) | Y |  |  |
| 122 | NUM_ITEM_NFE_ANT | VARCHAR2(3) | Y |  |  |
| 123 | COD_CCLASS | VARCHAR2(7) | Y |  |  |
| 124 | CPNPJ_OPER_LD | VARCHAR2(14) | Y |  |  |
| 125 | DAT_EXPIRA_CRED | DATE | Y |  |  |
| 126 | PERC_RED_BC | NUMBER(5,2) | Y |  |  |
| 127 | VLR_ICMS_DESONERADO | NUMBER(17,2) | Y |  |  |
| 128 | COD_BENEF_FISCAL | VARCHAR2(10) | Y |  |  |
| 129 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 130 | PERC_FCP_DEST | NUMBER(5,2) | Y |  |  |
| 131 | VLR_FCP_DEST | NUMBER(17,2) | Y |  |  |
| 132 | VLR_ICMS_UF_EMIT | NUMBER(17,2) | Y |  |  |
| 133 | COD_BENEF_FISCAL_DEST | VARCHAR2(10) | Y |  |  |
| 134 | VLR_BC_FUST | NUMBER(17,2) | Y |  |  |
| 135 | VLR_ALIQ_FUST | NUMBER(7,4) | Y |  |  |
| 136 | VLR_FUST | NUMBER(17,2) | Y |  |  |
| 137 | VLR_BC_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 138 | VLR_ALIQ_FUNTTEL | NUMBER(7,4) | Y |  |  |
| 139 | VLR_FUNTTEL | NUMBER(17,2) | Y |  |  |
| 140 | VLR_PIS_RETIDO | NUMBER(23,8) | Y |  |  |
| 141 | VLR_COFINS_RETIDO | NUMBER(23,8) | Y |  |  |
| 142 | VLR_CSLL_RETIDO | NUMBER(23,8) | Y |  |  |
| 143 | VLR_BC_IRRF | NUMBER(23,8) | Y |  |  |
| 144 | VLR_IRRF_RETIDO | NUMBER(23,8) | Y |  |  |
| 145 | VLR_UNIT_PROC | NUMBER(23,8) | Y |  |  |
| 146 | QTD_FAT_PROC | NUMBER(19,4) | Y |  |  |
| 147 | VLR_ITEM_PROC | NUMBER(23,8) | Y |  |  |
| 148 | VLR_DESC_PROC | NUMBER(17,2) | Y |  |  |
| 149 | VLR_OUT_DESP_PROC | NUMBER(17,2) | Y |  |  |
| 150 | IND_DEV_PROC | VARCHAR2(1) | Y |  |  |
| 151 | VLR_BC_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 152 | VLR_ALIQ_ICMS_PROC | NUMBER(7,4) | Y |  |  |
| 153 | VLR_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 154 | VLR_PIS_PROC | NUMBER(17,2) | Y |  |  |
| 155 | VLR_COFINS_PROC | NUMBER(17,2) | Y |  |  |
| 156 | IND_TP_RESSARC | VARCHAR2(2) | Y |  |  |
| 157 | DATA_REF_RESSARC | DATE | Y |  |  |
| 158 | NUM_PROC_RESSARC | VARCHAR2(60) | Y |  |  |
| 159 | NUM_PROT_RESSARC | VARCHAR2(60) | Y |  |  |
| 160 | DSC_OBS_RESSARC | VARCHAR2(100) | Y |  |  |
| 161 | DSC_ADIC_RESSARC | VARCHAR2(500) | Y |  |  |
| 162 | IND_NF_ANT | VARCHAR2(1) | Y |  |  |
| 163 | VLR_FCP_ICMS_PROC | NUMBER(17,2) | Y |  |  |
| 164 | DAT_CRIACAO | DATE | Y |  |  |
| 165 | DAT_ALTERACAO | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X42_CAPA_TELECOM(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- IDENT_FIS_RECEITA → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_UF_DESTINO → ESTADO(IDENT_ESTADO)
- COD_CCLASS → CAD_CCLASS_NFCOM(COD_CCLASS_NFCOM)

**Indexes**:
- IX_FK_SAF_2178: (IDENT_FIS_RECEITA)
- IX_X43_ITEM_TELECOM: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL)

---

## X44_ITENS_CHASSI

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
| 12 | NUM_CHASSI | VARCHAR2(17) | N |  |  |
| 13 | COD_COR | VARCHAR2(4) | Y |  |  |
| 14 | DSC_COR | VARCHAR2(40) | Y |  |  |
| 15 | DSC_POTENCIA | VARCHAR2(4) | Y |  |  |
| 16 | DSC_POTENCIA_CM3 | VARCHAR2(4) | Y |  |  |
| 17 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 18 | PESO_BRUTO | NUMBER(14,3) | Y |  |  |
| 19 | SERIE_VEIC | VARCHAR2(9) | Y |  |  |
| 20 | DSC_TP_COMBUSTIVEL | VARCHAR2(8) | Y |  |  |
| 21 | NUM_MOTOR | VARCHAR2(21) | Y |  |  |
| 22 | DSC_CMKG | VARCHAR2(9) | Y |  |  |
| 23 | DSC_DISTANCIA_EIXO | VARCHAR2(4) | Y |  |  |
| 24 | NUM_RENAVAM | NUMBER(14) | Y |  |  |
| 25 | NUM_MARCA_MODELO | NUMBER(6) | Y |  |  |
| 26 | NUM_ANO_MODELO | NUMBER(4) | Y |  |  |
| 27 | NUM_ANO_FABRIC | NUMBER(4) | Y |  |  |
| 28 | IND_TP_PINTURA | CHAR(1) | Y |  |  |
| 29 | NUM_TP_VEIC | NUMBER(2) | Y |  |  |
| 30 | NUM_ESPECIE_VEIC | NUMBER(1) | Y |  |  |
| 31 | IND_CONDICAO_VIN | CHAR(1) | Y |  |  |
| 32 | IND_CONDICAO_VEIC | CHAR(1) | Y |  |  |
| 33 | PLACA_VEICULO | VARCHAR2(7) | Y |  |  |

**PK**: DATA_FISCAL, COD_ESTAB, MOVTO_E_S, COD_EMPRESA, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_CHASSI

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X08_ITENS_MERC(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

**Indexes**:
- IX_X44_CHASSI: (NUM_CHASSI)

---

## X46_RE_DOCTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_ENTRADA_RE | DATE | N |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DATA_EMISSAO | DATE | N |  |  |
| 9 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 10 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 11 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 12 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 13 | DATA_SAIDA_MINUTA | DATE | Y |  |  |
| 14 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 15 | IDENT_FIS_JUR_T | NUMBER(12) | Y |  |  |
| 16 | DAT_INTERN_AM | DATE | Y |  |  |
| 17 | INTERNA_SUFRAMA | VARCHAR2(14) | Y |  |  |
| 18 | PLACA_VEICULO | VARCHAR2(10) | Y |  |  |
| 19 | NUM_MINUTA | VARCHAR2(12) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ENTRADA_RE, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DATA_EMISSAO, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)

**Indexes**:
- IX_FK_SAF_1928: (IDENT_FIS_JUR)

---

## X47_DEBITO_IMP
**Comment**: Tabela de Declaração de Importação criada para atendimento a IN nr 13 DRP - 2006, RS.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_DI | DATE | N |  |  |
| 4 | NUM_DI | VARCHAR2(15) | N |  |  |
| 5 | DATA_DESEMB_ADUAN | DATE | Y |  |  |
| 6 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 7 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 8 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_DI, NUM_DI

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_X47_DEB_IMP: (COD_EMPRESA, COD_ESTAB, DATA_DESEMB_ADUAN)

---

## X481_OPER_REM_EXP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_RE_OPER | DATE | N |  |  |
| 4 | NUM_RE_OPER | VARCHAR2(15) | N |  |  |
| 5 | DAT_NF_OPER | DATE | N |  |  |
| 6 | IDENT_FIS_JUR_OPER | NUMBER(12) | N |  |  |
| 7 | NUM_NF_OPER | VARCHAR2(12) | N |  |  |
| 8 | SERIE_NF_OPER | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_NF_OPER | VARCHAR2(2) | N |  |  |
| 10 | IDENT_PRODUTO_OPER | NUMBER(12) | N |  |  |
| 11 | NUM_ITEM_OPER | NUMBER(5) | N |  |  |
| 12 | NUM_RE_REM | VARCHAR2(15) | N |  |  |
| 13 | DAT_FISCAL_REM | DATE | N |  |  |
| 14 | IDENT_FIS_JUR_REM | NUMBER(12) | N |  |  |
| 15 | NUM_DOCFIS_REM | VARCHAR2(12) | N |  |  |
| 16 | SERIE_DOCFIS_REM | VARCHAR2(3) | N |  |  |
| 17 | SUB_SERIE_DOCFIS_REM | VARCHAR2(2) | N |  |  |
| 18 | IDENT_PRODUTO_REM | NUMBER(12) | N |  |  |
| 19 | QTD_EXPORTADA | NUMBER(17,3) | Y |  |  |
| 20 | IND_EXP_SIMPL | CHAR(1) | Y |  |  |
| 21 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 23 | NUM_CONHEC_EMB_OPER | VARCHAR2(18) | N |  |  |
| 24 | NUM_MEMO_EXP_REM | VARCHAR2(50) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_RE_OPER, NUM_RE_OPER, DAT_NF_OPER, IDENT_FIS_JUR_OPER, NUM_NF_OPER, SERIE_NF_OPER, SUB_SERIE_NF_OPER, IDENT_PRODUTO_OPER, NUM_ITEM_OPER, NUM_RE_REM, DAT_FISCAL_REM, IDENT_FIS_JUR_REM, NUM_DOCFIS_REM, SERIE_DOCFIS_REM, SUB_SERIE_DOCFIS_REM, IDENT_PRODUTO_REM, NUM_CONHEC_EMB_OPER, NUM_MEMO_EXP_REM

---

## X48_OPER_EXP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_RE | DATE | N |  |  |
| 4 | NUM_RE | VARCHAR2(15) | N |  |  |
| 5 | DAT_NF | DATE | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | NUM_NF | VARCHAR2(12) | N |  |  |
| 8 | SERIE_NF | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_NF | VARCHAR2(2) | N |  |  |
| 10 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 11 | NUM_ITEM | NUMBER(5) | N |  |  |
| 12 | DAT_SAIDA | DATE | Y |  |  |
| 13 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 14 | COD_EX | VARCHAR2(3) | Y |  |  |
| 15 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 16 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 17 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 18 | AG_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 19 | ANO_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 20 | NUM_ATO_CONCES | VARCHAR2(6) | Y |  |  |
| 21 | DIG_ATO_CONCES | VARCHAR2(1) | Y |  |  |
| 22 | PESO_BRUTO | NUMBER(17,6) | Y |  |  |
| 23 | PESO_LIQUIDO | NUMBER(17,6) | Y |  |  |
| 24 | VLR_UNIT | NUMBER(17,6) | Y |  |  |
| 25 | QTD_UND_MED | NUMBER(17,6) | Y |  |  |
| 26 | QTD_UND_COM | NUMBER(17,6) | Y |  |  |
| 27 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 28 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 29 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 30 | VLR_DESP_ACRESC | NUMBER(17,2) | Y |  |  |
| 31 | VLR_DESP_COMIS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_DESP_ARMAZ | NUMBER(17,2) | Y |  |  |
| 33 | VLR_DESP_ROYAL | NUMBER(17,2) | Y |  |  |
| 34 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 35 | VLR_NF | NUMBER(17,2) | Y |  |  |
| 36 | BASE_IPI | NUMBER(17,2) | Y |  |  |
| 37 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 38 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 39 | VLR_ISENTA_IPI | NUMBER(17,2) | Y |  |  |
| 40 | VLR_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |
| 41 | BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 42 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 43 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 44 | VLR_ISENTA_ICMS | NUMBER(17,2) | Y |  |  |
| 45 | VLR_OUTRAS_ICMS | NUMBER(17,2) | Y |  |  |
| 46 | BASE_IE | NUMBER(17,2) | Y |  |  |
| 47 | VLR_ALIQ_IE | NUMBER(7,4) | Y |  |  |
| 48 | VLR_IE | NUMBER(17,2) | Y |  |  |
| 49 | NUM_DDE_DSE | VARCHAR2(14) | Y |  |  |
| 50 | DAT_DDE_DSE | DATE | Y |  |  |
| 51 | VLR_DESPACHO | NUMBER(17,2) | Y |  |  |
| 52 | DAT_EMBARQUE | DATE | Y |  |  |
| 53 | DAT_AVERBACAO | DATE | Y |  |  |
| 54 | PAIS_DEST | VARCHAR2(3) | Y |  |  |
| 55 | MOEDA_OPER | VARCHAR2(10) | Y |  |  |
| 56 | VLR_LIQ_MERC | NUMBER(17,2) | Y |  |  |
| 57 | VLR_MERC_DOLAR | NUMBER(17,2) | Y |  |  |
| 58 | VLR_MERC_MOEDA | NUMBER(17,2) | Y |  |  |
| 59 | NUM_FAT_COM | VARCHAR2(12) | Y |  |  |
| 60 | DAT_FAT_COM | DATE | Y |  |  |
| 61 | OBS | VARCHAR2(120) | Y |  |  |
| 62 | IND_TP_OP | CHAR(1) | Y |  |  |
| 63 | IND_PRD_SER_DIR | CHAR(1) | Y |  |  |
| 64 | PRECO_MED_UNIT | NUMBER(17,2) | Y |  |  |
| 65 | IND_AJUSTE_EFET | CHAR(1) | Y |  |  |
| 66 | IND_MET_AJUSTE | CHAR(1) | Y |  |  |
| 67 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 68 | IND_COND_PES | CHAR(1) | Y |  |  |
| 69 | IND_TP_VENDA | VARCHAR2(2) | Y |  |  |
| 70 | CNPJ_ESTAB_BENEF | VARCHAR2(14) | Y |  |  |
| 71 | COMP_EXPORT | VARCHAR2(15) | Y |  |  |
| 72 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 73 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 74 | DAT_COMP_EXPORT | DATE | Y |  |  |
| 75 | NUM_CONHEC_EMB | VARCHAR2(18) | N |  |  |
| 76 | DAT_CONHEC_EMB | DATE | Y |  |  |
| 77 | COD_TP_CONHEC | VARCHAR2(2) | Y |  |  |
| 78 | IND_AVERBACAO | CHAR(1) | Y | 'N' |  |
| 79 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 80 | IDENT_FIS_JUR_EXP | NUMBER(12) | Y |  |  |
| 81 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 82 | VLR_REINTEGRA | NUMBER(17,2) | Y |  |  |
| 83 | IND_EXP_SERVICO | CHAR(1) | Y |  |  |
| 84 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 85 | IND_CLASS_SEGURO | CHAR(1) | Y |  |  |
| 86 | IND_CLASS_FRETE | CHAR(1) | Y |  |  |
| 87 | IND_CLASS_ACRES | CHAR(1) | Y |  |  |
| 88 | IND_CLASS_COMIS | CHAR(1) | Y |  |  |
| 89 | IND_CLASS_ARMAZ | CHAR(1) | Y |  |  |
| 90 | IND_CLASS_ROYALTIES | CHAR(1) | Y |  |  |
| 91 | IDENT_CFO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_RE, NUM_RE, DAT_NF, IDENT_FIS_JUR, NUM_NF, SERIE_NF, SUB_SERIE_NF, IDENT_PRODUTO, NUM_ITEM, NUM_CONHEC_EMB

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- PAIS_DEST → PAIS(COD_PAIS)
- MOEDA_OPER → Y2046_INDICE(COD_INDICE)
- IDENT_FIS_JUR_EXP → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

**Indexes**:
- IX_FK_SAF_1382: (IDENT_FIS_JUR)
- IX_FK_SAF_2174: (IDENT_FIS_JUR_EXP)

---

## X49_OPER_IMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_DI | DATE | N |  |  |
| 4 | NUM_DI | VARCHAR2(15) | N |  |  |
| 5 | DAT_NF | DATE | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | NUM_NF | VARCHAR2(12) | N |  |  |
| 8 | SERIE_NF | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_NF | VARCHAR2(2) | N |  |  |
| 10 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 11 | NUM_ITEM | NUMBER(5) | N |  |  |
| 12 | DAT_ENTRADA | DATE | Y |  |  |
| 13 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 14 | COD_EX | VARCHAR2(3) | Y |  |  |
| 15 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 16 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 17 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 18 | AG_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 19 | ANO_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 20 | NUM_ATO_CONCES | VARCHAR2(20) | Y |  |  |
| 21 | DIG_ATO_CONCES | VARCHAR2(1) | Y |  |  |
| 22 | PESO_BRUTO | NUMBER(17,6) | Y |  |  |
| 23 | PESO_LIQUIDO | NUMBER(17,6) | Y |  |  |
| 24 | VLR_UNIT | NUMBER(17,6) | Y |  |  |
| 25 | QTD_UND_MED | NUMBER(17,6) | Y |  |  |
| 26 | QTD_UND_COM | NUMBER(17,6) | Y |  |  |
| 27 | VLR_PRODUTO | NUMBER(17,2) | Y |  |  |
| 28 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 29 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 30 | VLR_DESP_ADUAN | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg C060: Valor das despesas aduaneiras que integram a base de cálculo de ICMS. |
| 31 | VLR_DESP_ACRESC | NUMBER(17,2) | Y |  |  |
| 32 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 33 | VLR_NF | NUMBER(17,2) | Y |  |  |
| 34 | BASE_IPI | NUMBER(17,2) | Y |  |  |
| 35 | VLR_ALIQ_IPI | NUMBER(7,4) | Y |  |  |
| 36 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 37 | VLR_ISENTA_IPI | NUMBER(17,2) | Y |  |  |
| 38 | VLR_OUTRAS_IPI | NUMBER(17,2) | Y |  |  |
| 39 | BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 40 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 41 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 42 | VLR_ISENTA_ICMS | NUMBER(17,2) | Y |  |  |
| 43 | VLR_OUTRAS_ICMS | NUMBER(17,2) | Y |  |  |
| 44 | BASE_II | NUMBER(17,2) | Y |  |  |
| 45 | VLR_ALIQ_II | NUMBER(7,4) | Y |  |  |
| 46 | VLR_II | NUMBER(17,2) | Y |  |  |
| 47 | PAIS_ORIG | VARCHAR2(3) | Y |  |  |
| 48 | MOEDA_ORIG | VARCHAR2(10) | Y |  |  |
| 49 | VLR_LIQ_MERC | NUMBER(17,2) | Y |  |  |
| 50 | VLR_MERC_DOLAR | NUMBER(17,2) | Y |  |  |
| 51 | VLR_MERC_MOEDA | NUMBER(21,6) | Y |  |  |
| 52 | OBS | VARCHAR2(120) | Y |  |  |
| 53 | IND_TP_OP | CHAR(1) | Y |  |  |
| 54 | IND_PRD_SER_DIR | CHAR(1) | Y |  |  |
| 55 | IND_AJUSTE_EFET | CHAR(1) | Y |  |  |
| 56 | IND_MET_AJUSTE | CHAR(1) | Y |  |  |
| 57 | VLR_AJUSTE | NUMBER(17,2) | Y |  |  |
| 58 | IND_COND_PES | CHAR(1) | Y |  |  |
| 59 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 60 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 61 | MOEDA_OP_FRETE | VARCHAR2(10) | Y |  |  |
| 62 | VLR_FRETE_MOEDA | NUMBER(21,6) | Y |  |  |
| 63 | MOEDA_OP_SEGURO | VARCHAR2(10) | Y |  |  |
| 64 | VLR_SEGURO_MOEDA | NUMBER(21,6) | Y |  |  |
| 65 | VLR_UNIT_REAL | NUMBER(17,6) | Y |  |  |
| 66 | COD_FORN_ORIG | VARCHAR2(14) | Y |  |  |
| 67 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 68 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 69 | VLR_IOF | NUMBER(17,2) | Y |  |  |
| 70 | VLR_ADUAN_SEM_ICMS | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg C060: Valor das despesas aduaneiras que não integram a base de cálculo de ICMS. |
| 71 | DAT_DESEMBARACO | DATE | Y |  | ATO COTEPE 70 - reg C060: Data do Desembaraço. |
| 72 | TIPO_DI | CHAR(1) | Y |  |  |
| 73 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 74 | INCOTERM | VARCHAR2(5) | Y |  |  |
| 75 | IND_TP_INTERMEDIO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_DI, NUM_DI, DAT_NF, IDENT_FIS_JUR, NUM_NF, SERIE_NF, SUB_SERIE_NF, IDENT_PRODUTO, NUM_ITEM

**FKs**:
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- PAIS_ORIG → PAIS(COD_PAIS)
- MOEDA_ORIG → Y2046_INDICE(COD_INDICE)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- MOEDA_OP_FRETE → Y2046_INDICE(COD_INDICE)
- MOEDA_OP_SEGURO → Y2046_INDICE(COD_INDICE)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IDX_X49_DI_VALORES: (COD_EMPRESA, COD_ESTAB)
- IX_FK_SAF_1645: (IDENT_FIS_JUR)
- IX_X49_DAT_ENTRADA: (COD_EMPRESA, COD_ESTAB, DAT_ENTRADA, NUM_DI, NUM_NF, IDENT_MODELO)
- IX_X49_DAT_NF: (COD_EMPRESA, COD_ESTAB, DAT_NF, IDENT_FIS_JUR, NUM_NF, SERIE_NF, SUB_SERIE_NF, IDENT_PRODUTO, NUM_ITEM)

---

## X500_TIT_RECEBER_DOC

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
| 10 | NUM_DOCFIS_NF | VARCHAR2(12) | N |  |  |
| 11 | SERIE_DOCFIS_NF | VARCHAR2(3) | N |  |  |
| 12 | SUB_SERIE_DOCFIS_NF | VARCHAR2(2) | N |  |  |
| 13 | DATA_FISCAL_NF | DATE | N |  |  |
| 14 | MOVTO_E_S_NF | CHAR(1) | N |  |  |
| 15 | NORM_DEV_NF | CHAR(1) | N |  |  |
| 16 | IDENT_DOCTO_NF | NUMBER(12) | N |  |  |
| 17 | IDENT_FIS_JUR_NF | NUMBER(12) | N |  |  |
| 18 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 19 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_DOCFIS_NF, SERIE_DOCFIS_NF, SUB_SERIE_DOCFIS_NF, DATA_FISCAL_NF, MOVTO_E_S_NF, NORM_DEV_NF, IDENT_DOCTO_NF, IDENT_FIS_JUR_NF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X05_TIT_RECEBER(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

---

## X501_TIT_RECEBER_PARC

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
| 10 | NUM_PARCELA | NUMBER(3) | N |  |  |
| 11 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 12 | ARQUIVAMENTO | VARCHAR2(50) | Y |  |  |
| 13 | DATA_VENCTO | DATE | Y |  |  |
| 14 | VLR_PARCELA | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | VLR_JUROS | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg Z035 - Valor dos Juros/Multa pagos |
| 18 | VLR_DESCONTO | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg Z035 - Valor de Desconto recebido |
| 19 | VLR_IRRF | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg Z035 - Valor do IR |
| 20 | DATA_PGTO | DATE | Y |  | ATO COTEPE 70 - reg Z035 - Data de pagamento da parcela |
| 21 | IND_PGTO | CHAR(1) | Y |  | ATO COTEPE 70 - reg Z035 - Indicador da forma de pagamento. Valores: 0, 1, 2, 3, 4, 5, 9 |
| 22 | DESC_PGTO | VARCHAR2(100) | Y |  | ATO COTEPE 70 - reg Z035 - Descricao complementar da forma de pagamento |
| 23 | NUM_LANCAMENTO | VARCHAR2(40) | Y |  | ATO COTEPE 70 - reg Z035 - Número do Lançamento Contábil |
| 24 | COD_SIT_PIS | NUMBER(2) | Y |  |  |
| 25 | VLR_DESC_PIS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE_PIS | NUMBER(17,2) | Y |  |  |
| 27 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 28 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 29 | VLR_ALIQ_PIS_R | NUMBER(19,4) | Y |  |  |
| 30 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 31 | COD_SIT_COFINS | NUMBER(2) | Y |  |  |
| 32 | VLR_DESC_COFINS | NUMBER(17,2) | Y |  |  |
| 33 | VLR_BASE_COFINS | NUMBER(17,2) | Y |  |  |
| 34 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 35 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 36 | VLR_ALIQ_COFINS_R | NUMBER(19,4) | Y |  |  |
| 37 | VLR_COFINS | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM, NUM_PARCELA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM → X05_TIT_RECEBER(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DISCRI_ITEM)

**Indexes**:
- IX_FK_SAF_2069: (IDENT_FIS_JUR)

---

## X502_VEIC_COMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_ESCR_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_TRANSP | NUMBER(12) | N |  |  |
| 12 | PLACA_VEICULO | VARCHAR2(17) | N |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | NUM_VOLUME | VARCHAR2(50) | Y |  |  |
| 15 | PESO_BRUTO | NUMBER(14,3) | Y |  |  |
| 16 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_TRANSP, PLACA_VEICULO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_TRANSP → X50_TRANSP_DOCFIS(COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_TRANSP)

---

## X50_TRANSP_DOCFIS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_ESCR_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_TRANSP | NUMBER(12) | N |  |  |
| 12 | IDENT_VIA_TRANSP | NUMBER(12) | Y |  |  |
| 13 | QTD_VOLUMES | NUMBER(17,6) | Y |  |  |
| 14 | IDENT_VOLUME | NUMBER(12) | Y |  |  |
| 15 | PESO_BRUTO | NUMBER(14,3) | Y |  |  |
| 16 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 17 | DESPESA_FRETE | NUMBER(17,2) | Y |  |  |
| 18 | MODALIDADE_FRETE | CHAR(1) | Y |  |  |
| 19 | DESPESA_SEGURO | NUMBER(17,2) | Y |  |  |
| 20 | NUM_CFRETE_DESPAC | VARCHAR2(12) | Y |  |  |
| 21 | PLACA_VEICULO | VARCHAR2(17) | Y |  |  |
| 22 | PRE_NUM_CONHEC | VARCHAR2(12) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 25 | CNH_MOTORISTA | NUMBER(11) | Y |  |  |
| 26 | NOME_MOTORISTA | VARCHAR2(40) | Y |  |  |
| 27 | PLACA_CARRETA | VARCHAR2(7) | Y |  |  |
| 28 | DAT_ENT_VEIC | DATE | Y |  |  |
| 29 | HORA_ENT_VEIC | VARCHAR2(4) | Y |  |  |
| 30 | HORA_SAI_VEIC | VARCHAR2(4) | Y |  |  |
| 31 | ORDEM_CARREG | NUMBER(6) | Y |  |  |
| 32 | IDENT_UF_CAM | NUMBER(12) | Y |  |  |
| 33 | CIDADE_CAM | VARCHAR2(18) | Y |  |  |
| 34 | NUM_VIAGEM | NUMBER(15) | Y |  |  |
| 35 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 36 | VLR_ICMSS | NUMBER(17,2) | Y |  |  |
| 37 | IDENT_UF_VEIC | NUMBER(12) | Y |  |  |
| 38 | PLACA_REBOQUE | VARCHAR2(17) | Y |  |  |
| 39 | IDENT_UF_REBOQ | NUMBER(12) | Y |  |  |
| 40 | MARCA_VOLUME | VARCHAR2(50) | Y |  | marca dos volumes transportados - ato cotepe 35/05 |
| 41 | NUM_VOLUME | VARCHAR2(50) | Y |  | numeração dos volumes transportados - ato cotepe 35/05 |
| 42 | IDENT_FIS_JUR_CONSIG | NUMBER(12) | Y |  | Ato Cotepe 70 - reg D050, D060, D080: pessoa fis. jur consignatária |
| 43 | IDENT_FIS_JUR_REDESP | NUMBER(12) | Y |  | Ato Cotepe 70 - reg D050, D080: pessoa fis. jur redespachante |
| 44 | IDENT_VEIC_TRANSP | NUMBER(12) | Y |  | Ato Cotepe 70 - reg D030, D050, D060, D070, D080: Ident p/ o cadastro de veículos. |
| 45 | IND_TP_NAVEGACAO | CHAR(1) | Y |  | Ato Cotepe 70 - reg D060: tipo de navegação: 0 - interior; 1 - cabotagem. |
| 46 | IND_TARIFA_AEREA | CHAR(1) | Y |  | Ato Cotepe 70 - reg D070: tipo de tarifa aérea: 0 - Exp; 1 - Enc; 2 - C.I.; 9 - Outra |
| 47 | IND_NATUREZA_FRETE | CHAR(1) | Y |  | Ato Cotepe 70 - reg D080: tipo de natureza do frete: 0 - negociável; 1 - não negociável |
| 48 | REGISTRO_OPERADOR | VARCHAR2(30) | Y |  | Ato Cotepe 70 - reg D080: registro do operador de transporte multimodal |
| 49 | VLR_FRETE_PV | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D050, D080: valor do frete por peso/volume. |
| 50 | VLR_FRETE_LIQ | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D060: valor líquido do frete |
| 51 | VLR_FRETE_BRUTO | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D060: valor bruto do frete. |
| 52 | VLR_FRETE_MM | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D060: valor do frete para renovação da Marinha Mercante. |
| 53 | VLR_SEC_CAT | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D050: valor de SEC/CAT |
| 54 | VLR_DESPACHO | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D050: valor de despacho |
| 55 | VLR_PEDAGIO | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D050, D080: valor de pedágio |
| 56 | VLR_DESPESA_PORT | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D060: valor das despesas portuárias |
| 57 | VLR_DESPESA_CARGA | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D060: valor das despesas com carga e descarga |
| 58 | VLR_PESO_TAXADO | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D070: valor do peso taxado |
| 59 | VLR_TAXA_TERRESTRE | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D070: valor da taxa terrestre |
| 60 | VLR_TAXA_REDESPACHO | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D070: valor da taxa de redespacho |
| 61 | VLR_TAXA_ADV | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D070: valor da taxa ad valorem |
| 62 | VLR_GRIS | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D080: valor do gris (transporte multimodal) |
| 63 | VLR_TARIFA | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D210: valor da tarifa (bilhete de transporte). |
| 64 | COD_LINHA_TRANSP | VARCHAR2(10) | Y |  | Ato Cotepe 70 - reg D210: código do prefixo da linha de transporte (bilhete). |
| 65 | DSC_LINHA_TRANSP | VARCHAR2(50) | Y |  | Ato Cotepe 70 - reg D210: descrição da linha de transporte (bilhete). |
| 66 | POLTRONA | VARCHAR2(10) | Y |  | Ato Cotepe 70 - reg D210: número da poltrona ou cabine (bilhete). |
| 67 | AGENTE | VARCHAR2(30) | Y |  | Ato Cotepe 70 - reg D210: identificação do agente (bilhete). |
| 68 | IDENT_FIS_JUR_COLETA | NUMBER(12) | Y |  | Ato Cotepe 70 - reg C250: dados de coleta e entrega |
| 69 | IDENT_FIS_JUR_ENTREGA | NUMBER(12) | Y |  | Ato Cotepe 70 - reg C250: dados de coleta e entrega |
| 70 | VLR_OUTROS | NUMBER(17,2) | Y |  | ATO COTEPE 70 - reg D050, D060, D070, D080 E D210 |
| 71 | MATRICULA | VARCHAR2(16) | Y |  |  |
| 72 | COD_AUTORIZ_SEFAZ | VARCHAR2(21) | Y |  |  |
| 73 | NUM_PASSE_FISCAL | VARCHAR2(20) | Y |  |  |
| 74 | TEMPERATURA | NUMBER(5,2) | Y |  |  |
| 75 | CPF_MOTORISTA | VARCHAR2(11) | Y |  |  |
| 76 | MODAL_FRETE_REDESP | CHAR(1) | Y |  |  |
| 77 | IND_VAGAO_BALSA | CHAR(1) | Y |  |  |
| 78 | COD_VAGAO_BALSA | VARCHAR2(20) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_TRANSP

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_VIA_TRANSP → X2047_VIA_TRANSP(IDENT_VIA_TRANSP)
- IDENT_VOLUME → X2042_ESP_VOLUME(IDENT_VOLUME)
- IDENT_TRANSP → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_VEIC_TRANSP → X2049_VEIC_TRANSP(IDENT_VEIC_TRANSP)
- IDENT_FIS_JUR_CONSIG → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_REDESP → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_COLETA → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_ENTREGA → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_1830: (IDENT_TRANSP)
- IX_FK_SAF_2095: (IDENT_FIS_JUR_CONSIG)
- IX_FK_SAF_2096: (IDENT_FIS_JUR_REDESP)
- IX_FK_SAF_2123: (IDENT_FIS_JUR_COLETA)
- IX_FK_SAF_2124: (IDENT_FIS_JUR_ENTREGA)

---

## X51_ITENS_FRETE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_ESCR_FISCAL | DATE | N |  |  |
| 4 | MOVTO_E_S | CHAR(1) | N |  |  |
| 5 | NORM_DEV | CHAR(1) | N |  |  |
| 6 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 11 | IDENT_DOCTO_TRANSP | NUMBER(12) | N |  |  |
| 12 | NUM_DOCFIS_TRANSP | VARCHAR2(12) | N |  |  |
| 13 | SER_DOCFIS_TRANSP | VARCHAR2(3) | N |  |  |
| 14 | S_SER_DOCFIS_TRANS | VARCHAR2(2) | N |  |  |
| 15 | DATA_EMIS_TRANSP | DATE | N |  |  |
| 16 | CGC_CPF_REMET | VARCHAR2(14) | N |  |  |
| 17 | VLR_TOT_DOCFIS | NUMBER(17,2) | Y |  |  |
| 18 | INSC_UF_REMET | VARCHAR2(14) | Y |  |  |
| 19 | RAZAO_REMET | VARCHAR2(70) | Y |  |  |
| 20 | MUNICIPIO_REMET | VARCHAR2(30) | Y |  |  |
| 21 | CEP_REMET | NUMBER(8) | Y |  |  |
| 22 | IDENT_ESTADO_REMET | NUMBER(12) | Y |  |  |
| 23 | CPF_CGC_DEST | VARCHAR2(14) | Y |  |  |
| 24 | INSC_ESTADUAL_DEST | VARCHAR2(14) | Y |  |  |
| 25 | RAZAO_DEST | VARCHAR2(70) | Y |  |  |
| 26 | MUNICIPIO_DEST | VARCHAR2(30) | Y |  |  |
| 27 | CEP_DEST | NUMBER(8) | Y |  |  |
| 28 | IDENT_ESTADO_DEST | NUMBER(12) | Y |  |  |
| 29 | DOCFIS_SIM_NAO | CHAR(1) | Y |  |  |
| 30 | IDENT_VIA_TRANSP | NUMBER(12) | Y |  |  |
| 31 | QTD_VOLUME | NUMBER(17,6) | Y |  |  |
| 32 | IDENT_VOLUME | NUMBER(12) | Y |  |  |
| 33 | PESO_BRUTO | NUMBER(14,3) | Y |  |  |
| 34 | PESO_LIQUIDO | NUMBER(14,3) | Y |  |  |
| 35 | DESPESA_FRETE | NUMBER(17,2) | Y |  |  |
| 36 | MODALIDADE_FRETE | CHAR(1) | Y |  |  |
| 37 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 38 | OBSERVACAO_FRETE | VARCHAR2(45) | Y |  |  |
| 39 | IDENT_TRANSP | NUMBER(12) | Y |  |  |
| 40 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 41 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 42 | COD_MUNIC_COLETA | NUMBER(5) | Y |  |  |
| 43 | COD_MUNIC_DEST | NUMBER(5) | Y |  |  |
| 44 | DISTANCIA_EM_KM | NUMBER(6) | Y |  |  |
| 45 | QTD_MERCADORIA | NUMBER(17,6) | Y |  |  |
| 46 | IND_FORMA_CALC | CHAR(1) | Y |  |  |
| 47 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 48 | VLR_PRODUTO | NUMBER(17,2) | Y |  | Ato Cotepe 70 - reg D180 - Valor das mercadorias constantes no documento fiscal |
| 49 | NAT_VOLUME | VARCHAR2(30) | Y |  | Ato Cotepe 70 - reg D180 - Natureza dos volumes transportados. |
| 50 | VOLUME | VARCHAR2(30) | Y |  | Ato Cotepe 70 - reg D180 - Volume transportado. |
| 51 | MARCA_VOLUME | VARCHAR2(50) | Y |  | Ato Cotepe 70 - reg D180 - Marca dos volumes transportados |
| 52 | NUM_VOLUME | NUMBER(30) | Y |  | Ato Cotepe 70 - reg D180 - Numeração dos volumes transportados |
| 53 | COD_MODELO_COTEPE | VARCHAR2(2) | Y |  | Codigo do Modelo da Nota Fiscal conforme Quadro 4.1.1 do Ato Cotepe 70/05 |
| 54 | NUM_CHAVE_NFE | VARCHAR2(80) | Y |  |  |
| 55 | NUM_DESPACHO | VARCHAR2(12) | Y |  |  |
| 56 | CPF_CNPJ_COLETA | VARCHAR2(14) | Y |  |  |
| 57 | INSCR_EST_COLETA | VARCHAR2(14) | Y |  |  |
| 58 | CPF_CNPJ_ENTREGA | VARCHAR2(14) | Y |  |  |
| 59 | INSCR_EST_ENTREGA | VARCHAR2(14) | Y |  |  |
| 60 | COD_MUNIC_REMET | NUMBER(5) | Y |  |  |
| 61 | COD_MUNIC_ENTREGA | NUMBER(5) | Y |  |  |
| 62 | IDENT_ESTADO_COLETA | NUMBER(12) | Y |  |  |
| 63 | IDENT_ESTADO_ENTREGA | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_DOCTO_TRANSP, NUM_DOCFIS_TRANSP, SER_DOCFIS_TRANSP, S_SER_DOCFIS_TRANS, DATA_EMIS_TRANSP, CGC_CPF_REMET

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_ESCR_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IDENT_DOCTO_TRANSP → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_VIA_TRANSP → X2047_VIA_TRANSP(IDENT_VIA_TRANSP)
- IDENT_VOLUME → X2042_ESP_VOLUME(IDENT_VOLUME)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)
- IDENT_TRANSP → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_ESTADO_COLETA, COD_MUNIC_COLETA → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_ESTADO_DEST, COD_MUNIC_DEST → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_ESTADO_ENTREGA, COD_MUNIC_ENTREGA → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

**Indexes**:
- IX_FK_SAF_0247: (IDENT_TRANSP)

---

## X520_INVENT_SIT_TRB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INVENTARIO | DATE | N |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | IDENT_NAT_ESTOQUE | NUMBER(12) | N |  |  |
| 7 | DISCRI_INVENTARIO | VARCHAR2(74) | N |  |  |
| 8 | IDENT_SITUACAO_A | NUMBER(12) | N |  |  |
| 9 | IDENT_SITUACAO_B | NUMBER(12) | N |  |  |
| 10 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_ICMS | NUMBER(17,6) | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, GRUPO_CONTAGEM, IDENT_PRODUTO, IDENT_NAT_ESTOQUE, DISCRI_INVENTARIO, IDENT_SITUACAO_A, IDENT_SITUACAO_B

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, GRUPO_CONTAGEM, IDENT_PRODUTO, IDENT_NAT_ESTOQUE, DISCRI_INVENTARIO → X52_INVENT_PRODUTO(COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, GRUPO_CONTAGEM, IDENT_PRODUTO, IDENT_NAT_ESTOQUE, DISCRI_INVENTARIO)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)

---

## X52_INVENT_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INVENTARIO | DATE | N |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | IDENT_NAT_ESTOQUE | NUMBER(12) | N |  |  |
| 7 | DISCRI_INVENTARIO | VARCHAR2(74) | N |  |  |
| 8 | IDENT_UND_PADRAO | NUMBER(12) | Y |  |  |
| 9 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 10 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 11 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 12 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 13 | VLR_UNIT | NUMBER(18,6) | Y |  |  |
| 14 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 15 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 19 | VLR_ICMS | NUMBER(21,6) | Y |  |  |
| 20 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 21 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 22 | DESCRICAO_RIPI | VARCHAR2(25) | Y |  |  |
| 23 | VLR_ICMS_MEDIO | NUMBER(18,6) | Y |  |  |
| 24 | VLR_ICMSS_MEDIO | NUMBER(18,6) | Y |  |  |
| 25 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |
| 26 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 27 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_BASE_ISENTO | NUMBER(17,2) | Y |  |  |
| 29 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 30 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 31 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 35/05 |
| 32 | VLR_CUSTO_DCA | NUMBER(21,6) | Y |  |  |
| 33 | IDENT_PROD_RASTRO | NUMBER(12) | Y |  |  |
| 34 | QUANTIDADE_DCA | NUMBER(17,6) | Y |  |  |
| 35 | IND_GRAVACAO_SAICS | CHAR(1) | Y |  |  |
| 36 | VLR_IPI | NUMBER(17,2) | Y |  |  |
| 37 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 38 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 39 | VLR_TRIB_NC | NUMBER(17,2) | Y |  |  |
| 40 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 41 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 42 | IND_MOT_INV | VARCHAR2(2) | Y |  |  |
| 43 | IND_SIT_TRIB | CHAR(1) | Y |  |  |
| 44 | VLR_IR | NUMBER(17,2) | Y |  |  |
| 45 | VLR_BASE_ICMSS_MEDIO | NUMBER(18,6) | Y |  |  |
| 46 | VLR_FCP_MEDIO | NUMBER(18,6) | Y |  |  |
| 47 | VLR_RESERVADO1 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_RESERVADO2 | NUMBER(17,2) | Y |  |  |
| 49 | VLR_RESERVADO3 | NUMBER(17,2) | Y |  |  |
| 50 | DSC_RESERVADO4 | VARCHAR2(50) | Y |  |  |
| 51 | DSC_RESERVADO5 | VARCHAR2(50) | Y |  |  |
| 52 | DSC_RESERVADO6 | VARCHAR2(50) | Y |  |  |
| 53 | DSC_RESERVADO7 | VARCHAR2(50) | Y |  |  |
| 54 | DSC_RESERVADO8 | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, GRUPO_CONTAGEM, IDENT_PRODUTO, IDENT_NAT_ESTOQUE, DISCRI_INVENTARIO

**FKs**:
- IDENT_NAT_ESTOQUE → X2010_NAT_ESTOQUE(IDENT_NAT_ESTOQUE)
- IDENT_UND_PADRAO → X2017_UND_PADRAO(IDENT_UND_PADRAO)
- IDENT_ALMOX → X2021_ALMOXARIFADO(IDENT_ALMOX)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL → ICT_ESTAB_IESTAD(COD_EMPRESA, COD_ESTAB, INSC_ESTADUAL)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)

**Indexes**:
- IX_FK_SAF_1788: (IDENT_FIS_JUR)
- IX_FK_SAF_2079: (IDENT_OBSERVACAO)
- IX_X52_INVENT_PRODUTO_01: (COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, IND_MOT_INV, GRUPO_CONTAGEM, IDENT_PRODUTO)
- IX_X52_INVENT_PROD_CTA: (IDENT_CONTA)

---

## X52_LOG_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INVENTARIO | DATE | N |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 5 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 6 | IDENT_NAT_ESTOQUE | NUMBER(12) | N |  |  |
| 7 | DISCRI_INVENTARIO | VARCHAR2(64) | N |  |  |
| 8 | IND_PRODUTO | CHAR(1) | N |  |  |
| 9 | COD_PRODUTO | VARCHAR2(60) | N |  |  |
| 10 | COD_NBM | VARCHAR2(10) | Y |  |  |
| 11 | COD_UND_PADRAO | VARCHAR2(8) | Y |  |  |
| 12 | COD_ALMOX | VARCHAR2(20) | Y |  |  |
| 13 | COD_CUSTO | VARCHAR2(50) | Y |  |  |
| 14 | COD_MEDIDA | VARCHAR2(8) | Y |  |  |
| 15 | QUANTIDADE | VARCHAR2(17) | Y |  |  |
| 16 | VLR_TOT | VARCHAR2(17) | Y |  |  |
| 17 | VLR_UNIT | VARCHAR2(18) | Y |  |  |
| 18 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 19 | VLR_ICMS | VARCHAR2(17) | Y |  |  |
| 20 | COD_CONTA | VARCHAR2(70) | Y |  |  |
| 21 | IND_DEB_CRE | CHAR(1) | Y |  |  |
| 22 | DESCRICAO_RIPI | VARCHAR2(25) | Y |  |  |
| 23 | VLR_ICMS_MEDIO | VARCHAR2(18) | Y |  |  |
| 24 | VLR_ICMSS_MEDIO | VARCHAR2(18) | Y |  |  |
| 25 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 26 | INSC_ESTADUAL | VARCHAR2(14) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, GRUPO_CONTAGEM, IDENT_PRODUTO, IDENT_NAT_ESTOQUE, DISCRI_INVENTARIO, IND_PRODUTO, COD_PRODUTO

---

## X530_RETIFICACAO_IRRF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 3 | DATA_MOVTO | DATE | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 5 | IDENT_DOCTO | NUMBER(12) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 9 | IDENT_OPERACAO | NUMBER(12) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 10 | IDENT_DARF | NUMBER(12) | N |  | Dado da Chave de Identificacao da retencao. PK da X53_RETENCAO_IRRF. |
| 11 | DATA_RETIFICACAO | DATE | N |  | Data de ocorrencia da Retificacao. Carregado pela SAX53 - DATA_RETIFICACAO. |
| 12 | ANO_COMPETENCIA | NUMBER(4) | Y |  |  |
| 13 | MES_COMPETENCIA | NUMBER(2) | Y |  |  |
| 14 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 16 | VLR_IR_RETIDO | NUMBER(17,2) | Y |  |  |
| 17 | ALIQUOTA | NUMBER(5,2) | Y |  |  |
| 18 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 19 | NUM_AP | VARCHAR2(10) | Y |  |  |
| 20 | IND_TIPO_QUITACAO | CHAR(1) | Y |  |  |
| 21 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 22 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 23 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 24 | DATA_INI_COMPET | DATE | Y |  |  |
| 25 | DATA_FIM_COMPET | DATE | Y |  |  |
| 26 | DATA_FATOR_GERADOR | DATE | Y |  |  |
| 27 | DATA_VENCTO | DATE | Y |  |  |
| 28 | IDENT_CENTRO_RESP | NUMBER(12) | Y |  |  |
| 29 | VLR_PREV_PRIVADA | NUMBER(17,2) | Y |  |  |
| 30 | VLR_PENS_ALIMENT | NUMBER(17,2) | Y |  |  |
| 31 | DSC_PENS_ALIMENT | VARCHAR2(50) | Y |  |  |
| 32 | VLR_SALARIO_FAM | NUMBER(17,2) | Y |  |  |
| 33 | VLR_APOSENT_ISENTA | NUMBER(17,2) | Y |  |  |
| 34 | VLR_AJUDA_CUSTO | NUMBER(17,2) | Y |  |  |
| 35 | VLR_PENS_INVALID | NUMBER(17,2) | Y |  |  |
| 36 | VLR_LUCRO_PJ | NUMBER(17,2) | Y |  |  |
| 37 | VLR_OUTROS_SOCIO | NUMBER(17,2) | Y |  |  |
| 38 | VLR_OUTROS_DIRF | NUMBER(17,2) | Y |  |  |
| 39 | DSC_OUTROS_DIRF | VARCHAR2(50) | Y |  |  |
| 40 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 41 | VLR_DED_INSS_TERC | NUMBER(17,2) | Y |  |  |
| 42 | VLR_DED_DEP_TERC | NUMBER(17,2) | Y |  |  |
| 43 | VLR_OUTROS_TRIB_EXCL | NUMBER(17,2) | Y |  |  |
| 44 | IND_VENCTO_CALC | CHAR(1) | Y |  |  |
| 45 | NUM_REF | VARCHAR2(17) | Y |  |  |
| 46 | NUM_REF_CORRESP | VARCHAR2(2) | Y |  |  |
| 47 | VLR_SALARIO_13 | NUMBER(17,2) | Y |  |  |
| 48 | VLR_TRIBUTO_13 | NUMBER(17,2) | Y |  |  |
| 49 | DATA_PAGTO | DATE | Y |  |  |
| 50 | TP_RENDIMENTO | VARCHAR2(3) | Y |  |  |
| 51 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |
| 52 | OBSERVACAO | VARCHAR2(50) | Y |  |  |
| 53 | NUM_VOUCHER | VARCHAR2(50) | Y |  |  |
| 54 | DATA_RETIFICACAO_REF | DATE | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf Complementar/Compensacao Credito. Identifica o registro (retencao pai ou retificacao) que foi comparado com a propria retificacao, resultando na geracao de um dédito ou crédito. |
| 55 | NRO_REFERENCIA_X751 | VARCHAR2(15) | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf Complementar/Compensacao Credito. Identifica o Darf Complementar ou a Compensacao de Credito que a retificacao gerou. |
| 56 | IND_PROC_X751 | CHAR(1) | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf Complementar/Compensacao Credito. Indica se a retificacao foi processada pela Geracao do Darf Complementar/Compensacao. Domínio: S (processada), N (nao processada). |
| 57 | SITUACAO_X751 | CHAR(1) | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf Complementar/Compensacao Credito. Indica a situacao da retificacao em relacao a Geracao do Darf Complementar/Compensacao de Credito. Dominio: nulo ou N (nao gerada), G (gerada), P (paga), C (compensada). |
| 58 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 59 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 60 | IND_CTRL_RET_MIN | CHAR(1) | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf . Identifica se a retenção nao alcancou valor minimo de pagto valores:(S) ou (N). |
| 61 | VLR_VOLUNTARIO_COPA | NUMBER(17,2) | Y |  |  |
| 62 | VLR_VOLUNTARIO_COPA_13 | NUMBER(17,2) | Y |  |  |
| 63 | VLR_BOLSA_MEDICO_RESID | NUMBER(17,2) | Y |  |  |
| 64 | VLR_BOLSA_MEDICO_RESID_13 | NUMBER(17,2) | Y |  |  |
| 65 | VLR_DEP_JUD | NUMBER(17,2) | Y |  |  |
| 66 | NUM_CNPJ_OPER | CHAR(14) | Y |  |  |
| 67 | VLR_PG_TITULAR | NUMBER(17,2) | Y |  |  |
| 68 | IND_TIPO_ISENCAO | VARCHAR2(2) | Y |  |  |
| 69 | DSC_RENDIMENTO | VARCHAR2(100) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, DATA_RETIFICACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF → X53_RETENCAO_IRRF(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF)

**Indexes**:
- IX_X530_RETIFICACA0: (COD_EMPRESA, DATA_RETIFICACAO, COD_ESTAB)

---

## X531_REND_DEC_JUDICIAL

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
| 11 | IND_TIPO_REND | CHAR(1) | N |  | 1 – Rendimento Recebido Acumuladamente 2 – Demais Rendimentos de Decisão Judicial.   |
| 12 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 13 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 14 | VLR_DESP_JUD | NUMBER(17,2) | Y |  |  |
| 15 | VLR_DESP_ADVOGADO | NUMBER(17,2) | Y |  |  |
| 16 | DSC_NAT_REND | VARCHAR2(50) | Y |  |  |
| 17 | QTDE_MESES | NUMBER(5,1) | Y |  |  |
| 18 | IND_ORIG_REC | CHAR(1) | Y |  | 1 - Recursos do próprio declarante 2 - Recursos de terceiros  |
| 19 | NUM_CNPJ_ORIG_REC | VARCHAR2(14) | Y |  |  |
| 20 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 21 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 22 | DSC_PROC_JUD | VARCHAR2(50) | Y |  |  |
| 23 | VLR_N_RETIDO_IR | NUMBER(17,2) | Y |  |  |
| 24 | VLR_DEP_JUD_IR | NUMBER(17,2) | Y |  |  |
| 25 | VLR_COMP_ANO_CAL_IR | NUMBER(17,2) | Y |  |  |
| 26 | VLR_COMP_ANO_ANT_IR | NUMBER(17,2) | Y |  |  |
| 27 | VLR_REND_EXIG_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 28 | VLR_BASE_SUSP_IR | NUMBER(17,2) | Y |  |  |
| 29 | VLR_BASE_SUSP_CSLL | NUMBER(17,2) | Y |  |  |
| 30 | VLR_N_CSLL | NUMBER(17,2) | Y |  |  |
| 31 | VLR_DEP_CSLL | NUMBER(17,2) | Y |  |  |
| 32 | VLR_BASE_SUSP_COFINS | NUMBER(17,2) | Y |  |  |
| 33 | VLR_N_COFINS | NUMBER(17,2) | Y |  |  |
| 34 | VLR_DEP_COFINS | NUMBER(17,2) | Y |  |  |
| 35 | VLR_BASE_SUSP_PIS_PASEP | NUMBER(17,2) | Y |  |  |
| 36 | VLR_N_PIS_PASEP | NUMBER(17,2) | Y |  |  |
| 37 | VLR_DEP_PIS_PASEP | NUMBER(17,2) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF → X53_RETENCAO_IRRF(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF)
- IDENT_PROC_ADJ → X2058_PROC_ADJ(IDENT_PROC_ADJ)
- IDENT_SUSP_TBT → X2059_SUSP_TBT(IDENT_SUSP_TBT)

**Indexes**:
- UK_X531_REND_DEC_JUDICIAL_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT)

---

## X532_IDENTIF_ADVOGADO

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
| 11 | IND_TIPO_REND | CHAR(1) | N |  |  |
| 12 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 13 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 14 | CPF_CNPJ_ADVOGADO | VARCHAR2(14) | N |  |  |
| 15 | VLR_DESP_ADVOGADO | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT → X531_REND_DEC_JUDICIAL(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT)

**Indexes**:
- UK_X532_IDENTIF_ADVOGADO_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT, CPF_CNPJ_ADVOGADO)

---

## X533_RIMUN_RISEN

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
| 10 | ANO_COMPETENCIA | NUMBER(4) | Y |  |  |
| 11 | MES_COMPETENCIA | NUMBER(2) | Y |  |  |
| 12 | IND_IMUNE_ISENTO | VARCHAR2(1) | Y |  |  |
| 13 | VLR_RENDIMENTO | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)

**Indexes**:
- IX_FK_SAF_3225: (IDENT_FIS_JUR)
- IX_X533_RIMUN_RISEN: (COD_EMPRESA, COD_ESTAB, ANO_COMPETENCIA, MES_COMPETENCIA)

---

## X534_DED_EXIG_SUSP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 5 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 10 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 11 | IND_TIPO_REND | CHAR(1) | Y |  |  |
| 12 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 13 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 14 | NUM_SEQ | NUMBER(2) | Y |  |  |
| 15 | IND_TP_DEDUCAO | VARCHAR2(1) | Y |  |  |
| 16 | VLR_DED_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT → X531_REND_DEC_JUDICIAL(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT)

**Indexes**:
- UK_X534_DED_EXIG_SUSP_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT, NUM_SEQ)

---

## X535_DED_SUSP_DEP_PENS_ALIM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_MOVTO | DATE | Y |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 5 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 9 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 10 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 11 | IND_TIPO_REND | CHAR(1) | Y |  |  |
| 12 | IDENT_PROC_ADJ | NUMBER(12) | Y |  |  |
| 13 | IDENT_SUSP_TBT | NUMBER(12) | Y |  |  |
| 14 | NUM_SEQ | NUMBER(2) | Y |  |  |
| 15 | CPF_DEP | VARCHAR2(11) | Y |  |  |
| 16 | VLR_DEPEN_SUSP | NUMBER(17,2) | Y |  |  |
| 17 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 18 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT, NUM_SEQ → X534_DED_EXIG_SUSP(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT, NUM_SEQ)

**Indexes**:
- UK_X535_DED_SUS_DEP_PEN_AL_001 (UNIQUE): (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, IND_TIPO_REND, IDENT_PROC_ADJ, IDENT_SUSP_TBT, NUM_SEQ, CPF_DEP)

---

## X536_DED_DEP_PENS_ALIM

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
| 11 | CPF_DEP | VARCHAR2(11) | N |  |  |
| 12 | VLR_DEPEN | NUMBER(17,2) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IND_GRAVACAO | VARCHAR2(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF, CPF_DEP

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF → X53_RETENCAO_IRRF(COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF)

---

## X53_RETENCAO_IRRF

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
| 11 | ANO_COMPETENCIA | NUMBER(4) | Y |  |  |
| 12 | MES_COMPETENCIA | NUMBER(2) | Y |  |  |
| 13 | VLR_BRUTO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_DEDUCAO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_IR_RETIDO | NUMBER(17,2) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 18 | ALIQUOTA | NUMBER(5,2) | Y |  |  |
| 19 | COD_CTRL_INT | VARCHAR2(12) | Y |  |  |
| 20 | NUM_AP | VARCHAR2(10) | Y |  |  |
| 21 | IND_TIPO_QUITACAO | CHAR(1) | Y |  |  |
| 22 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 23 | ESP_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 24 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 25 | DATA_INI_COMPET | DATE | Y |  |  |
| 26 | DATA_FIM_COMPET | DATE | Y |  |  |
| 27 | DATA_FATOR_GERADOR | DATE | Y |  |  |
| 28 | DATA_VENCTO | DATE | Y |  |  |
| 29 | IDENT_CENTRO_RESP | NUMBER(12) | Y |  |  |
| 30 | VLR_PREV_PRIVADA | NUMBER(17,2) | Y |  |  |
| 31 | VLR_PENS_ALIMENT | NUMBER(17,2) | Y |  |  |
| 32 | DSC_PENS_ALIMENT | VARCHAR2(50) | Y |  |  |
| 33 | VLR_SALARIO_FAM | NUMBER(17,2) | Y |  |  |
| 34 | VLR_APOSENT_ISENTA | NUMBER(17,2) | Y |  |  |
| 35 | VLR_AJUDA_CUSTO | NUMBER(17,2) | Y |  |  |
| 36 | VLR_PENS_INVALID | NUMBER(17,2) | Y |  |  |
| 37 | VLR_LUCRO_PJ | NUMBER(17,2) | Y |  |  |
| 38 | VLR_OUTROS_SOCIO | NUMBER(17,2) | Y |  |  |
| 39 | VLR_OUTROS_DIRF | NUMBER(17,2) | Y |  |  |
| 40 | DSC_OUTROS_DIRF | VARCHAR2(50) | Y |  |  |
| 41 | IND_TP_LANCTO_DIRF | CHAR(1) | Y |  |  |
| 42 | VLR_DED_INSS_TERC | NUMBER(17,2) | Y |  |  |
| 43 | VLR_DED_DEP_TERC | NUMBER(17,2) | Y |  |  |
| 44 | IND_PROC_DARF | CHAR(1) | Y | 'N' |  |
| 45 | VLR_OUTROS_TRIB_EXCL | NUMBER(17,2) | Y |  |  |
| 46 | IND_VENCTO_CALC | CHAR(1) | Y |  | Indica quando a data de vencimento foi calculada automaticamente na geração do DARF |
| 47 | SITUACAO | CHAR(1) | Y | 'N' | Indica se a situação da Retencao é (N) Branco, (G) Gerado ou (P) Pago |
| 48 | NUM_REF | VARCHAR2(17) | Y |  | Quando preenchido indica que o tributo deverá ser recolhido separadamente |
| 49 | NUM_REF_CORRESP | VARCHAR2(2) | Y |  | Identifica para qual situação o numero de referencia foi utilizado |
| 50 | NRO_REFERENCIA_DARF | VARCHAR2(15) | Y |  | Campo interno usado para relacionar as retenções as DARF geradas pelo MSAF |
| 51 | VLR_SALARIO_13 | NUMBER(17,2) | Y |  |  |
| 52 | VLR_TRIBUTO_13 | NUMBER(17,2) | Y |  |  |
| 53 | DATA_PAGTO | DATE | Y |  |  |
| 54 | TP_RENDIMENTO | VARCHAR2(3) | Y |  |  |
| 55 | TP_TRIBUTACAO_IR | VARCHAR2(2) | Y |  |  |
| 56 | OBSERVACAO | VARCHAR2(50) | Y |  |  |
| 57 | DATA_CANCELAMENTO | DATE | Y |  |  |
| 58 | IND_CANCELAMENTO | CHAR(1) | Y |  |  |
| 59 | NUM_VOUCHER | VARCHAR2(50) | Y |  |  |
| 60 | NRO_REFERENCIA_X751 | VARCHAR2(15) | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf Complementar/Compensacao Credito. Identifica o Darf Complementar ou a Compensacao de Credito que a retencao cancelada gerou. |
| 61 | IND_PROC_X751 | CHAR(1) | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf Complementar/Compensacao Credito. Indica se a retencao cancelada foi processada pela Geracao do Darf Complementar/Compensacao. Domínio: S (processada), N (nao processada). |
| 62 | SITUACAO_X751 | CHAR(1) | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf Complementar/Compensacao Credito. Indica a situacao da retencao cancelada em relacao a Geracao do Darf Complementar/Compensacao de Credito. Dominio: nulo ou N (nao gerada), G (gerada), P (paga), C (compensada). |
| 63 | IND_CTRL_RET_MIN | CHAR(1) | Y |  | Campo de controle interno do Msaf. Preenchido na Geracao do Darf . Identifica se a retenção nao alcancou valor minimo de pagto valores:(S) ou (N). |
| 64 | IND_ESTORNO | CHAR(1) | Y |  |  |
| 65 | DATA_ESTORNO | DATE | Y |  |  |
| 66 | NRO_REFERENCIA_DARF_ESTORNO | VARCHAR2(15) | Y |  |  |
| 67 | VLR_VOLUNTARIO_COPA | NUMBER(17,2) | Y |  |  |
| 68 | VLR_VOLUNTARIO_COPA_13 | NUMBER(17,2) | Y |  |  |
| 69 | VLR_BOLSA_MEDICO_RESID | NUMBER(17,2) | Y |  |  |
| 70 | VLR_BOLSA_MEDICO_RESID_13 | NUMBER(17,2) | Y |  |  |
| 71 | VLR_DEP_JUD | NUMBER(17,2) | Y |  |  |
| 72 | NUM_CNPJ_OPER | CHAR(14) | Y |  |  |
| 73 | VLR_PG_TITULAR | NUMBER(17,2) | Y |  |  |
| 74 | IND_TIPO_ISENCAO | VARCHAR2(2) | Y |  |  |
| 75 | DSC_RENDIMENTO | VARCHAR2(100) | Y |  |  |
| 76 | COD_NAT_REND | VARCHAR2(9) | Y |  |  |
| 77 | CNPJ_FUND_INV | VARCHAR2(14) | Y |  |  |
| 78 | NOME_FUND_INV | VARCHAR2(150) | Y |  |  |
| 79 | NUM_INSC_PREV | VARCHAR2(14) | Y |  |  |
| 80 | NUM_INSC_FAPI | VARCHAR2(14) | Y |  |  |
| 81 | NOME_FAPI | VARCHAR2(150) | Y |  |  |
| 82 | VLR_FAPI | NUMBER(17,2) | Y |  |  |
| 83 | NUM_INSC_FUNPRESP | VARCHAR2(14) | Y |  |  |
| 84 | NOME_FUNPRESP | VARCHAR2(150) | Y |  |  |
| 85 | VLR_FUNPRESP | NUMBER(17,2) | Y |  |  |
| 86 | NUM_INSC_CONTRIB | VARCHAR2(14) | Y |  |  |
| 87 | NOME_CONTRIB | VARCHAR2(150) | Y |  |  |
| 88 | VLR_CONTRIB | NUMBER(17,2) | Y |  |  |
| 89 | REG_ANS | VARCHAR2(6) | Y |  |  |
| 90 | VLR_BASE_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 91 | VLR_RET_IRRF | NUMBER(17,2) | Y |  |  |
| 92 | VLR_DED_IR_EXIG_SUSP | NUMBER(17,2) | Y |  |  |
| 93 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 94 | VLR_BASE_EXIG_SUSP_PIS | NUMBER(17,2) | Y |  |  |
| 95 | VLR_RET_NEFE_IRRF_PIS | NUMBER(17,2) | Y |  |  |
| 96 | VLR_DEP_JUD_PIS | NUMBER(17,2) | Y |  |  |
| 97 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 98 | VLR_BASE_EXIG_SUSP_COFINS | NUMBER(17,2) | Y |  |  |
| 99 | VLR_RET_NEFE_IRRF_COFINS | NUMBER(17,2) | Y |  |  |
| 100 | VLR_DEP_JUD_COFINS | NUMBER(17,2) | Y |  |  |
| 101 | VLR_CSLL | NUMBER(17,2) | Y |  |  |
| 102 | VLR_BASE_EXIG_SUSP_CSLL | NUMBER(17,2) | Y |  |  |
| 103 | VLR_RET_NEFE_IRRF_CSLL | NUMBER(17,2) | Y |  |  |
| 104 | VLR_DEP_JUD_CSLL | NUMBER(17,2) | Y |  |  |
| 105 | CNPJ_SCP | VARCHAR2(14) | Y |  |  |
| 106 | PERCENTUAL_SCP | NUMBER(7,4) | Y |  |  |
| 107 | TP_FONTE_PAGADORA | VARCHAR2(3) | Y |  |  |
| 108 | VLR_APOSENT_ISENTA_13 | NUMBER(17,2) | Y |  |  |
| 109 | VLR_JUROS_MORA | NUMBER(17,2) | Y |  |  |
| 110 | VLR_RESG_PREV_COMPL | NUMBER(17,2) | Y |  |  |
| 111 | VLR_REND_S_RET_IR | NUMBER(17,2) | Y |  |  |
| 112 | COD_SERVICO_NAT_REND | VARCHAR2(10) | Y |  |  |
| 113 | DATA_ESCR_CONT | DATE | Y |  |  |
| 114 | VLR_DESC_SIMPL_MENSAL | NUMBER(17,2) | Y |  |  |
| 115 | VLR_BASE | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_DARF → X2019_COD_DARF(IDENT_DARF)
- COD_TRIBUTO, ESP_TRIBUTO → DWT_TRIBUTO_ESP(COD_TRIBUTO, ESP_TRIBUTO)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)
- IDENT_CENTRO_RESP → X2094_CENTRO_RESP(IDENT_CENTRO_RESP)

**Indexes**:
- IX_FK_SAF_0249: (IDENT_FIS_JUR)
- IX_X53RETECAODARF: (NRO_REFERENCIA_DARF)
- IX_X53RETENCAOIRRF: (COD_EMPRESA, DATA_MOVTO, IDENT_FIS_JUR, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_OPERACAO, IDENT_DARF)
- IX_X53RETENCAO_IRRF_02: (COD_EMPRESA, COD_ESTAB, DATA_MOVTO, ANO_COMPETENCIA, MES_COMPETENCIA)
- IX_X53RETENCAO_IRRF_03: (COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, IDENT_DARF, ANO_COMPETENCIA, MES_COMPETENCIA)
- IX_X53RETENCAO_IRRF_04: (COD_EMPRESA, DATA_FATOR_GERADOR, SITUACAO)
- IX_X53RETENCAO_IRRF_05: (COD_EMPRESA, COD_ESTAB, IDENT_DARF)
- IX_X53RETENCAO_IRRF_06: (COD_EMPRESA, IDENT_DARF)
- IX_X53_RETENCAO_COMP: (COD_EMPRESA, COD_ESTAB, ANO_COMPETENCIA, COD_TRIBUTO)

---

## X54_FICHA_REG_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | IDENT_OCORRENCIA | NUMBER(12) | N |  |  |
| 6 | DATA_OCORRENCIA | DATE | N |  |  |
| 7 | IDENT_FUNCAO | NUMBER(12) | Y |  |  |
| 8 | IDENT_SINDICATO | NUMBER(12) | Y |  |  |
| 9 | DATA_INI_REF | DATE | Y |  |  |
| 10 | DATA_FIM_REF | DATE | Y |  |  |
| 11 | DATA_INI_OCORR | DATE | Y |  |  |
| 12 | DATA_FIM_OCORR | DATE | Y |  |  |
| 13 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 14 | VLR_OCORRENCIA | NUMBER(17,2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, IDENT_OCORRENCIA, DATA_OCORRENCIA

**FKs**:
- IDENT_OCORRENCIA → X2034_COD_OCORR(IDENT_OCORRENCIA)
- IDENT_FUNCAO → X2036_FUNCAO(IDENT_FUNCAO)
- IDENT_SINDICATO → X2048_SINDICATO(IDENT_SINDICATO)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)

---

## X55_DEPEND_FUNC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_FUNC | VARCHAR2(14) | N |  |  |
| 4 | VALID_FUNC | DATE | N |  |  |
| 5 | COD_DEPEND | NUMBER(2) | N |  |  |
| 6 | VALID_DEPEND | DATE | N |  |  |
| 7 | IDENT_TIPO_DEPEND | NUMBER(12) | Y |  |  |
| 8 | NOME | VARCHAR2(50) | Y |  |  |
| 9 | DATA_NASC | DATE | Y |  |  |
| 10 | DATA_FIM_IR | DATE | Y |  |  |
| 11 | DATA_FIM_SF | DATE | Y |  |  |
| 12 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 13 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 14 | NUM_CPF | VARCHAR2(11) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC, COD_DEPEND, VALID_DEPEND

**FKs**:
- IDENT_TIPO_DEPEND → X2035_TP_DEPEND(IDENT_TIPO_DEPEND)
- COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC → X15_FUNCIONARIO(COD_EMPRESA, COD_ESTAB, COD_FUNC, VALID_FUNC)

---

## X56_INDICE_CONV

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_INDICE | VARCHAR2(10) | N |  |  |
| 2 | DATA_INI | DATE | N |  |  |
| 3 | VLR_INDICE | NUMBER(14,6) | Y |  |  |
| 4 | DATA_FIM | DATE | Y |  |  |
| 5 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 6 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_INDICE, DATA_INI

**FKs**:
- COD_INDICE → Y2046_INDICE(COD_INDICE)

---

## X57_DOCFIS_HOTEL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | MOVTO_E_S | CHAR(1) | N |  |  |
| 4 | NORM_DEV | CHAR(1) | N |  |  |
| 5 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | DATA_EMISSAO | DATE | N |  |  |
| 11 | NUM_LANCTO | NUMBER(12) | N |  |  |
| 12 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 13 | DATA_OPER | DATE | Y |  |  |
| 14 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 15 | VLR_LANCTO | NUMBER(17,2) | Y |  |  |
| 16 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 17 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 18 | HISTORICO | VARCHAR2(100) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_ESTAB, DATA_EMISSAO, COD_EMPRESA, IDENT_FIS_JUR, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_LANCTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_SAF_1779: (IDENT_FIS_JUR)
- IX_X57_DOCFIS_HOT: (IDENT_SERVICO)

---

## X58_SE_DIC_GRP_PRD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_GRP_PROD | NUMBER(12) | N |  |  |
| 2 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 3 | COD_GRP_PROD | VARCHAR2(12) | Y |  |  |
| 4 | VALID_COD_GRUPO | DATE | Y |  |  |
| 5 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 6 | IDENT_GRP_PROD_DIC | NUMBER(12) | Y |  |  |

**PK**: IDENT_GRP_PROD

**FKs**:
- GRUPO_PRODUTO → GRUPO_ESTAB(GRUPO_ESTAB)
- IDENT_GRP_PROD_DIC → EST_SE_DIC_GRP_PRD(IDENT_GRP_PROD_DIC)

**Indexes**:
- IX_X58_SEDIC_GRPRD (UNIQUE): (GRUPO_PRODUTO, COD_GRP_PROD, VALID_COD_GRUPO)

---

## X59_CONHECIMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | NUM_CONHEC | VARCHAR2(12) | N |  |  |
| 5 | SERIE_CONHEC | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_CONHEC | VARCHAR2(2) | N |  |  |
| 7 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 8 | VLR_CONHEC | NUMBER(17,2) | Y |  |  |
| 9 | COD_TRIBUTO | VARCHAR2(6) | Y |  |  |
| 10 | COD_TRIBUTACAO | CHAR(1) | Y |  |  |
| 11 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 12 | VLR_ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_ICMS_DEBITADO | NUMBER(17,2) | Y |  |  |
| 14 | VLR_ICMS_CREDITADO | NUMBER(17,2) | Y |  |  |
| 15 | VLR_REDUCAO | NUMBER(17,2) | Y |  |  |
| 16 | DATA_EMISS_CONHEC | DATE | Y |  |  |
| 17 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 18 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 19 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 20 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 21 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 24 | NUM_DOCFIS_REF | VARCHAR2(12) | Y |  |  |
| 25 | SERIE_DOCFIS_REF | VARCHAR2(3) | Y |  |  |
| 26 | S_SERIE_DOCFIS_REF | VARCHAR2(2) | Y |  |  |
| 27 | NUM_LOTE | NUMBER(6) | Y |  |  |
| 28 | IDENT_UF_ORIGEM | NUMBER(12) | Y |  |  |
| 29 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 30 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 31 | VLR_OUTRAS_ICMS | NUMBER(17,2) | Y |  |  |
| 32 | MODALIDADE_FRETE | CHAR(1) | Y |  |  |
| 33 | SITUACAO | CHAR(1) | Y |  |  |
| 34 | IDENT_DET_OPERACAO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, NUM_CONHEC, SERIE_CONHEC, SUB_SERIE_CONHEC, IDENT_FIS_JUR

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- IDENT_DET_OPERACAO → DETALHE_OPERACAO(IDENT_DET_OPERACAO)
- IDENT_MODELO → X2024_MODELO_DOCTO(IDENT_MODELO)

**Indexes**:
- IX_FK_SAF_0765: (IDENT_FIS_JUR)

---

## X59_LOTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 4 | NUM_LOTE | NUMBER(6) | N |  |  |
| 5 | IDENT_VIA_TRANSP | NUMBER(12) | Y |  |  |
| 6 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 7 | IDENT_DET_OPERACAO | NUMBER(12) | Y |  |  |
| 8 | IDENT_UF_ORIGEM | NUMBER(12) | Y |  |  |
| 9 | IDENT_UF_DESTINO | NUMBER(12) | Y |  |  |
| 10 | TIPO_TRANSACAO | VARCHAR2(5) | Y |  |  |
| 11 | TIPO_DESTINACAO | NUMBER(2) | Y |  |  |
| 12 | VLR_TOT_CONHEC | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_FIS_JUR, NUM_LOTE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- IDENT_VIA_TRANSP → X2047_VIA_TRANSP(IDENT_VIA_TRANSP)
- IDENT_DET_OPERACAO → DETALHE_OPERACAO(IDENT_DET_OPERACAO)
- TIPO_TRANSACAO, TIPO_DESTINACAO → EFT_TRANS_DEST(TIPO_TRANSACAO, TIPO_DESTINACAO)

**Indexes**:
- IX_FK_SAF_1313: (IDENT_FIS_JUR)

---

## X60_CARTAO_TELECOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ANO_REFERENCIA | NUMBER(4) | N |  |  |
| 4 | MES_REFERENCIA | NUMBER(2) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_TEL | VARCHAR2(15) | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 8 | END_TEL | VARCHAR2(60) | Y |  |  |
| 9 | CID_TEL | VARCHAR2(25) | Y |  |  |
| 10 | LEITURA_INICIAL | NUMBER(6) | Y |  |  |
| 11 | LEITURA_FINAL | NUMBER(6) | Y |  |  |
| 12 | QTD_PULSO | NUMBER(6) | Y |  |  |
| 13 | QTD_CREDITO | NUMBER(6) | Y |  |  |
| 14 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ANO_REFERENCIA, MES_REFERENCIA, IDENT_FIS_JUR, NUM_TEL, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_FK_SAF_1839: (IDENT_FIS_JUR)

---

## X62_INVENTARIO_NBM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INVENTARIO | DATE | N |  |  |
| 4 | GRUPO_CONTAGEM | CHAR(1) | N |  |  |
| 5 | IDENT_NBM | NUMBER(12) | N |  |  |
| 6 | IDENT_NAT_ESTOQUE | NUMBER(12) | N |  |  |
| 7 | DISCRI_INVENTARIO | VARCHAR2(32) | N |  |  |
| 8 | IDENT_ALMOX | NUMBER(12) | Y |  |  |
| 9 | IDENT_CUSTO | NUMBER(12) | Y |  |  |
| 10 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 11 | QUANTIDADE | NUMBER(17,6) | Y |  |  |
| 12 | VLR_UNIT | NUMBER(18,6) | Y |  |  |
| 13 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 16 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 17 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 18 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 20 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_BASE_ISENTO | NUMBER(17,2) | Y |  |  |
| 22 | VLR_BASE_OUTRAS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_BASE_ICMSS | NUMBER(17,2) | Y |  |  |
| 24 | IDENT_OBSERVACAO | NUMBER(12) | Y |  | código da observação da x2009_observacao - ato cotepe 35/05 |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, GRUPO_CONTAGEM, IDENT_NBM, IDENT_NAT_ESTOQUE, DISCRI_INVENTARIO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- IDENT_NAT_ESTOQUE → X2010_NAT_ESTOQUE(IDENT_NAT_ESTOQUE)
- IDENT_ALMOX → X2021_ALMOXARIFADO(IDENT_ALMOX)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_OBSERVACAO → X2009_OBSERVACAO(IDENT_OBSERVACAO)

**Indexes**:
- IX_FK_SAF_1789: (IDENT_FIS_JUR)
- IX_FK_SAF_2080: (IDENT_OBSERVACAO)

---

## X63_FUNRURAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 5 | TIPO_MOV_ES | CHAR(1) | N |  |  |
| 6 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 11 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 12 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 13 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 14 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 15 | TIPO_OP | VARCHAR2(6) | Y |  |  |
| 16 | OBS | VARCHAR2(45) | Y |  |  |
| 17 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_PROD | NUMBER(17,2) | Y |  |  |
| 19 | COD_TRIB | CHAR(1) | Y |  |  |
| 20 | VLR_BASE_CALCULO | NUMBER(17,2) | Y |  |  |
| 21 | ALIQ_CONTRIB | NUMBER(7,4) | Y |  |  |
| 22 | VLR_CONTRIB | NUMBER(17,2) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 25 | ALIQ_SENAR | NUMBER(7,4) | Y |  |  |
| 26 | VLR_SENAR | NUMBER(17,2) | Y |  |  |
| 27 | IND_SIT_ESP | VARCHAR2(2) | Y |  |  |
| 28 | IND_TIPO_DEP | VARCHAR2(2) | Y |  |  |
| 29 | NUM_PROC_SIT | VARCHAR2(50) | Y |  |  |
| 30 | VLR_GILRAT | NUMBER(17,2) | Y |  | Informar o valor do GILRAT |
| 31 | ALIQ_GILRAT | NUMBER(7,4) | Y |  |  |
| 32 | IND_TIPO_AQUIS | VARCHAR2(1) | Y |  | Valores Válidos: 1, 2, 3, 4, 5, 6 |
| 33 | IND_TRIB_PRODUTOR_CP | VARCHAR2(1) | Y |  | Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária. 1 - Sobre a comercialização da sua produção; 2 - Sobre a folha de pagamento. Valores Válidos: 1, 2. |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_DOCTO, TIPO_MOV_ES, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_NATUREZA_OP → X2006_NATUREZA_OP(IDENT_NATUREZA_OP)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

**Indexes**:
- IX_FK_SAF_0437: (IDENT_FIS_JUR)

---

## X64_AFRMM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 7 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 8 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 9 | COD_TRIBUTACAO | NUMBER(1) | Y |  |  |
| 10 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 11 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 12 | VLR_AFRMM | NUMBER(17,2) | Y |  |  |
| 13 | VLR_REDUCAO_BASE | NUMBER(17,2) | Y |  |  |
| 14 | IDENT_DET_OPERACAO | NUMBER(12) | Y |  |  |
| 15 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_DET_OPERACAO → DETALHE_OPERACAO(IDENT_DET_OPERACAO)

**Indexes**:
- IX_FK_SAF_0345: (IDENT_FIS_JUR)

---

## X65_CPRES_IPI_PEXP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | IND_ETIQ_PROD | CHAR(1) | N |  |  |
| 8 | COD_ETIQ_PROD | VARCHAR2(60) | N |  |  |
| 9 | MES_ANO_APUR | VARCHAR2(6) | Y |  |  |
| 10 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 11 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 12 | IND_VENDA | CHAR(1) | Y |  |  |
| 13 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 14 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 15 | NUM_EMBARQUE | VARCHAR2(12) | Y |  |  |
| 16 | DAT_EMBARQUE | DATE | Y |  |  |
| 17 | NUM_DESPACHO | VARCHAR2(11) | Y |  |  |
| 18 | VLR_DESP_MOEDA_EST | NUMBER(17,2) | Y |  |  |
| 19 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 20 | NUM_RE | VARCHAR2(15) | Y |  |  |
| 21 | CGC_ESTAB_BENEF | VARCHAR2(14) | Y |  |  |
| 22 | NUM_FAT_COMERC | VARCHAR2(12) | Y |  |  |
| 23 | DAT_FAT_COMERC | DATE | Y |  |  |
| 24 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 25 | QTD_MERC | NUMBER(14,3) | Y |  |  |
| 26 | PESO_LIQ_MERC | NUMBER(14,3) | Y |  |  |
| 27 | PESO_BRUTO_MERC | NUMBER(14,3) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 30 | DAT_SAIDA | DATE | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_ETIQ_PROD, COD_ETIQ_PROD

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- COD_PAIS → PAIS(COD_PAIS)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_INDICE → Y2046_INDICE(COD_INDICE)

**Indexes**:
- IX_FK_SAF_0540: (IDENT_FIS_JUR)
- IX_X65_CP_IPI_PEX2: (COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IND_VENDA, IND_GRAVACAO)
- IX_X65_CP_IPI_PEXP: (COD_EMPRESA, COD_ESTAB, MES_ANO_APUR)

---

## X66_SELO_CONTROLE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_GRUPO_SELO | NUMBER(2) | N |  |  |
| 4 | COD_SUB_GRUPO_SELO | NUMBER(2) | N |  |  |
| 5 | COR_SELO | VARCHAR2(15) | N |  |  |
| 6 | SERIE_SELO | VARCHAR2(3) | N |  |  |
| 7 | TIPO_OPERACAO | CHAR(1) | N |  |  |
| 8 | DATA_OPERACAO | DATE | N |  |  |
| 9 | NRO_GUIA | VARCHAR2(12) | Y |  |  |
| 10 | DATA_GUIA | DATE | Y |  |  |
| 11 | QTDE_OPERACAO | NUMBER(11) | Y |  |  |
| 12 | NRO_INICIAL | NUMBER(12) | Y |  |  |
| 13 | NRO_FINAL | NUMBER(12) | Y |  |  |
| 14 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 15 | DATA_VALIDADE | DATE | Y |  |  |
| 16 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 17 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_GRUPO_SELO, COD_SUB_GRUPO_SELO, COR_SELO, SERIE_SELO, TIPO_OPERACAO, DATA_OPERACAO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_GRUPO_SELO, COD_SUB_GRUPO_SELO → SUBGRUPO_SELO(COD_GRUPO_SELO, COD_SUBGRUPO_SELO)

---

## X67_INVENT_SELO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_INVENTARIO | DATE | N |  |  |
| 4 | COD_GRUPO_SELO | NUMBER(2) | N |  |  |
| 5 | COD_SUBGRUPO_SELO | NUMBER(2) | N |  |  |
| 6 | COR_SELO | VARCHAR2(15) | N |  |  |
| 7 | SERIE_SELO | VARCHAR2(3) | N |  |  |
| 8 | QTDE_INVENT_SELO | NUMBER(11) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_INVENTARIO, COD_GRUPO_SELO, COD_SUBGRUPO_SELO, COR_SELO, SERIE_SELO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_GRUPO_SELO, COD_SUBGRUPO_SELO → SUBGRUPO_SELO(COD_GRUPO_SELO, COD_SUBGRUPO_SELO)

---

## X68_IMPRESSAO_AIDF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_ENTREGA | DATE | N |  |  |
| 4 | NRO_AIDF | VARCHAR2(12) | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 6 | IDENT_DOCTO_CONF | NUMBER(12) | Y |  |  |
| 7 | FORMATO_DOC | VARCHAR2(30) | Y |  |  |
| 8 | SERIE_DOC | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOC | VARCHAR2(2) | N |  |  |
| 10 | NRO_INICIAL | VARCHAR2(12) | Y |  |  |
| 11 | NRO_FINAL | VARCHAR2(12) | Y |  |  |
| 12 | IND_TIPO_FORMA | CHAR(1) | Y |  |  |
| 13 | ESPECIE | VARCHAR2(10) | Y |  |  |
| 14 | QTD_DOCTO | NUMBER(12) | Y |  |  |
| 15 | QTD_BLOCOS | NUMBER(12) | Y |  |  |
| 16 | QTD_DOCTO_BLOCOS | NUMBER(12) | Y |  |  |
| 17 | NRO_VIAS | NUMBER(1) | Y |  |  |
| 18 | IND_AIDF_UNICA | CHAR(1) | Y |  |  |
| 19 | NRO_CGF | NUMBER(14) | Y |  |  |
| 20 | NRO_FORM_AIDF | NUMBER(14) | Y |  |  |
| 21 | IDENT_DOCTO | NUMBER(12) | Y |  |  |
| 22 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 23 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 24 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 25 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 28 | DATA_AUTORIZACAO_AIDF | DATE | Y |  | Campo criado para atender a DES BH. |
| 29 | VALIDADE_AIDF | DATE | Y |  | Campo criado para atender a DES BH. |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ENTREGA, NRO_AIDF, SERIE_DOC, SUB_SERIE_DOC

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_DOCTO → X2005_TIPO_DOCTO(IDENT_DOCTO)
- IDENT_DOCTO_CONF → X2005_TIPO_DOCTO(IDENT_DOCTO)

**Indexes**:
- IX_FK_SAF_0334: (IDENT_FIS_JUR)

---

## X69_MOV_ESTORNO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_ESTORNO | VARCHAR2(2) | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | IDENT_INSUMO | NUMBER(12) | N |  |  |
| 6 | DATA_MOVTO | DATE | N |  |  |
| 7 | QTDE_CONSUMIDA | NUMBER(18,4) | Y |  |  |
| 8 | FATOR_CONSUMO | NUMBER(10,7) | Y |  |  |
| 9 | VLR_CONS_UNITARIO | NUMBER(17,2) | Y |  |  |
| 10 | VLR_UNITARIO | NUMBER(17,2) | Y |  |  |
| 11 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 12 | ALIQ_ICMS | NUMBER(7,4) | Y |  |  |
| 13 | VLR_ESTORNO | NUMBER(17,2) | Y |  |  |
| 14 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 15 | VLR_PRODUCAO_MES | NUMBER(17,2) | Y |  |  |
| 16 | VLR_FATURA_MES | NUMBER(17,2) | Y |  |  |
| 17 | DESCRICAO | VARCHAR2(50) | Y |  |  |
| 18 | IDENT_DET_OPERACAO | NUMBER(12) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_ESTORNO, IDENT_PRODUTO, IDENT_INSUMO, DATA_MOVTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_EMPRESA, COD_ESTAB, COD_ESTORNO → TIPO_ESTORNO(COD_EMPRESA, COD_ESTAB, COD_ESTORNO)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_DET_OPERACAO → DETALHE_OPERACAO(IDENT_DET_OPERACAO)
- IDENT_INSUMO → X2013_PRODUTO(IDENT_PRODUTO)

---

## X700_ITENS_MEDICAMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_MOVTO | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | TIPO_OPERACAO | NUMBER(2) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | NUM_FAB_LOTE | VARCHAR2(50) | N |  |  |
| 12 | QTD_LOTE | NUMBER(17,6) | Y |  |  |
| 13 | DAT_FABRIC | DATE | Y |  |  |
| 14 | DAT_VALIDADE | DATE | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, MOVTO_E_S, TIPO_OPERACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR, NUM_FAB_LOTE

**FKs**:
- COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, MOVTO_E_S, TIPO_OPERACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR → X70_MOV_SUBST_CONT(COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, MOVTO_E_S, TIPO_OPERACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR)

---

## X701_VOO_PASSAG

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
| 11 | IDENT_VOO | VARCHAR2(10) | N |  |  |
| 12 | IDENT_UF_DOCFIS_EMIT | NUMBER(12) | Y |  |  |
| 13 | QTD_PASSAG_VOO | NUMBER(4) | Y |  |  |
| 14 | IDENT_CONEXAO | VARCHAR2(10) | Y |  |  |
| 15 | IND_CLASSE | CHAR(1) | Y |  |  |
| 16 | NUM_POLTRONA | VARCHAR2(4) | Y |  |  |
| 17 | CPF_PARTICIPANTE | VARCHAR2(11) | Y |  |  |
| 18 | NOME_PARTICIPANTE | VARCHAR2(100) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_VOO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS → X07_DOCTO_FISCAL(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)

---

## X702_DESEMB_PASSAG

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
| 11 | IDENT_VOO | VARCHAR2(10) | N |  |  |
| 12 | COD_MUNICIPIO_ORIG | NUMBER(5) | N |  |  |
| 13 | COD_MUNICIPIO_DEST | NUMBER(5) | N |  |  |
| 14 | IDENT_UF_ORIG | NUMBER(12) | N |  |  |
| 15 | IDENT_UF_DEST | NUMBER(12) | N |  |  |
| 16 | QTD_PASSAG_DEST | NUMBER(4) | Y |  |  |
| 17 | VLR_TOT | NUMBER(17,2) | Y |  |  |
| 18 | VLR_TAXA | NUMBER(17,2) | Y |  |  |
| 19 | VLR_DESC | NUMBER(17,2) | Y |  |  |
| 20 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 21 | VLR_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 23 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 24 | COD_IATA_ORIG | VARCHAR2(3) | Y |  |  |
| 25 | COD_IATA_DEST | VARCHAR2(3) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_VOO, COD_MUNICIPIO_ORIG, COD_MUNICIPIO_DEST, IDENT_UF_ORIG, IDENT_UF_DEST

**FKs**:
- IDENT_UF_DEST, COD_MUNICIPIO_DEST, COD_IATA_DEST → DWT_COD_IATA(IDENT_ESTADO, COD_MUNICIPIO, COD_IATA)
- IDENT_UF_ORIG, COD_MUNICIPIO_ORIG, COD_IATA_ORIG → DWT_COD_IATA(IDENT_ESTADO, COD_MUNICIPIO, COD_IATA)
- COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_VOO → X701_VOO_PASSAG(COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_VOO)

---

## X70_MOV_SUBST_CONT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_MOVTO | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | TIPO_OPERACAO | NUMBER(2) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | TIPO_VISTO | NUMBER(6) | Y |  |  |
| 12 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 13 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 14 | TIPO | VARCHAR2(6) | Y |  |  |
| 15 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 16 | REFERENCIA | VARCHAR2(45) | Y |  |  |
| 17 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 18 | IND_ESPEC_MAT | CHAR(1) | Y |  |  |
| 19 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 20 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 21 | GUIA_TRAFEGO | VARCHAR2(40) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | NUM_RECEITA | NUMBER(15) | Y |  |  |
| 25 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 26 | NUM_REG_EXP_IMP | VARCHAR2(15) | Y |  |  |
| 27 | IDENT_FIS_JUR_TRANSP | NUMBER(12) | Y |  |  |
| 28 | DATA_EMISSAO | DATE | Y |  |  |
| 29 | IDENT_FIS_JUR_ARMAZEM | NUMBER(12) | Y |  |  |
| 30 | IND_TP_FRETE | VARCHAR2(1) | Y |  |  |
| 31 | DAT_EMBARQUE | DATE | Y |  |  |
| 32 | DAT_CONHEC_EMB | DATE | Y |  |  |
| 33 | IDENT_FIS_JUR_ENTREGA | NUMBER(12) | Y |  |  |
| 34 | IDENT_FIS_JUR_ADQ | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, MOVTO_E_S, TIPO_OPERACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_CFO, IDENT_NATUREZA_OP → X2081_EXTENSAO_CFO(IDENT_CFO, IDENT_NATUREZA_OP)
- IDENT_FIS_JUR_TRANSP → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_ARMAZEM → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_ENTREGA → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FIS_JUR_ADQ → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)

**Indexes**:
- IX_FK_SAF_0459: (IDENT_FIS_JUR)
- IX_FK_SAF_2006: (IDENT_FIS_JUR_TRANSP)
- IX_FK_SAF_3167: (IDENT_FIS_JUR_ARMAZEM)
- IX_X70_MOV_SUST: (DATA_MOVTO, TIPO_OPERACAO, COD_ESTAB, IDENT_PRODUTO, COD_EMPRESA)
- IX_X70_MOV_SUST_DT_EMIS: (DATA_EMISSAO, TIPO_OPERACAO, COD_ESTAB, IDENT_PRODUTO, COD_EMPRESA)

---

## X71_PARAM_SUBST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_OBRIGACAO | VARCHAR2(2) | N |  |  |
| 2 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 3 | IND_PSICOTROPICO | CHAR(1) | Y |  |  |
| 4 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 5 | DSC_PROD | VARCHAR2(50) | Y |  |  |
| 6 | OBSERVACAO | VARCHAR2(45) | Y |  |  |
| 7 | COD_VENDA | VARCHAR2(35) | Y |  |  |
| 8 | COD_CLASS_PRD | VARCHAR2(15) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 11 | NUM_REGISTRO | NUMBER(10) | Y |  |  |
| 12 | DSC_CONCENTRACAO | VARCHAR2(15) | Y |  |  |
| 13 | DSC_FORMULACAO | VARCHAR2(40) | Y |  |  |
| 14 | DSC_ORG_FED | VARCHAR2(40) | Y |  |  |
| 15 | PESO_VOLUME | VARCHAR2(20) | Y |  |  |
| 16 | COD_ING_ATIVO_PRIN | VARCHAR2(35) | Y |  |  |
| 17 | IDENT_MARCA_COM | NUMBER(12) | Y |  |  |

**PK**: TIPO_OBRIGACAO, IDENT_PRODUTO

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- TIPO_OBRIGACAO, COD_CLASS_PRD → SCT_CLASS_PRD(TIPO_OBRIGACAO, COD_CLASS_PRD)
- IDENT_MARCA_COM → X2025_MARCA_COMERC(IDENT_MARCA_COM)
- TIPO_OBRIGACAO, COD_ING_ATIVO_PRIN → X127_ING_ATIVO(TIPO_OBRIGACAO, COD_ING_ATIVO)

**Indexes**:
- IX_X71_MARCA: (IDENT_MARCA_COM, TIPO_OBRIGACAO)

---

## X72_SALDO_SUBST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_MOVTO | DATE | N |  |  |
| 4 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 5 | QTD_SALDO | NUMBER(17,6) | Y |  |  |
| 6 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 7 | TIPO | VARCHAR2(6) | Y |  |  |
| 8 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 9 | IND_ESPEC_MAT | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_MOVTO, IDENT_PRODUTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

---

## X73_RELAT_SUBST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | DATA_RELATORIO | DATE | N |  |  |
| 5 | SEQUENCIA | NUMBER(3) | N |  |  |
| 6 | OBSERVACAO_1 | VARCHAR2(45) | Y |  |  |
| 7 | OBSERVACAO_2 | VARCHAR2(45) | Y |  |  |
| 8 | OBSERVACAO_3 | VARCHAR2(45) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO, DATA_RELATORIO, SEQUENCIA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## X74_TERMOS_SUBST

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TIPO_LIVRO | VARCHAR2(3) | N |  |  |
| 4 | PORTARIA_A | VARCHAR2(10) | Y |  |  |
| 5 | PORTARIA_B | VARCHAR2(10) | Y |  |  |
| 6 | PORTARIA_C | VARCHAR2(10) | Y |  |  |
| 7 | RESP_TECNICO | VARCHAR2(50) | Y |  |  |
| 8 | RESP_LEGAL | VARCHAR2(50) | Y |  |  |
| 9 | RESP_PREENCHIM | VARCHAR2(50) | Y |  |  |
| 10 | NRO_CRF | VARCHAR2(14) | Y |  |  |
| 11 | IDENT_ESTADO_CRF | NUMBER(12) | Y |  |  |
| 12 | REGIAO | VARCHAR2(10) | Y |  |  |
| 13 | NRO_AUTORIZACAO | VARCHAR2(14) | Y |  |  |
| 14 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 15 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TIPO_LIVRO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TIPO_LIVRO → TIPO_LIVRO_FISCAL(COD_TIPO_LIVRO)

---

## X750_REDARF

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
| 23 | NUM_QUOTA | NUMBER(2) | N | 0 |  |
| 24 | NUM_QUOTA_DARF | NUMBER(2) | Y | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA, DATA_REDARF

**FKs**:
- COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA → X75_DCTF(COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA)

---

## X751_DCTF_COMPL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_APURACAO | DATE | N |  |  |
| 4 | IDENT_DARF | NUMBER(12) | N |  |  |
| 5 | NRO_REFERENCIA | VARCHAR2(15) | N |  |  |
| 6 | NUM_QUOTA | NUMBER(2) | N | 0 |  |
| 7 | NRO_REFERENCIA_X751 | VARCHAR2(15) | N |  |  |
| 8 | DATA_APURACAO_X751 | DATE | N |  |  |
| 9 | IND_DEB_CRED | CHAR(1) | N |  |  |
| 10 | DT_INI_APURACAO | DATE | Y |  |  |
| 11 | VLR_REC_ACUMUL | NUMBER(17,2) | Y |  |  |
| 12 | DATA_VENCTO | DATE | Y |  |  |
| 13 | VLR_PRINCIPAL | NUMBER(17,2) | Y |  |  |
| 14 | VLR_MULTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 16 | VLR_TOTAL | NUMBER(17,2) | Y |  |  |
| 17 | DATA_PAGTO | DATE | Y |  |  |
| 18 | NRO_PROCESSO_ADM | VARCHAR2(24) | Y |  |  |
| 19 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 20 | ALIQ_TRIBUTO | NUMBER(7,4) | Y |  |  |
| 21 | OBSERVACAO | VARCHAR2(180) | Y |  |  |
| 22 | NRO_BANCO | NUMBER(3) | Y |  |  |
| 23 | NRO_AGENCIA | NUMBER(5) | Y |  |  |
| 24 | NRO_PAGTO | VARCHAR2(14) | Y |  |  |
| 25 | SIT_PROCESSO | VARCHAR2(6) | Y |  |  |
| 26 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 27 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 28 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 29 | DATA_ENV_BCO | DATE | Y |  |  |
| 30 | AUTENT_BANCARIA | VARCHAR2(50) | Y |  |  |
| 31 | COD_TRIBUTO | VARCHAR2(2) | Y |  |  |
| 32 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 33 | SITUACAO | CHAR(1) | Y | 'A' |  |
| 34 | STATUS | CHAR(1) | Y | 'A' |  |
| 35 | NUM_REF_DARF | VARCHAR2(17) | Y |  |  |
| 36 | IND_POR_EMPRESA | CHAR(1) | Y | 'N' |  |
| 37 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 38 | ID_GER | NUMBER(12) | Y |  |  |
| 39 | SEQ_GER_ARQ | NUMBER(12) | Y |  |  |
| 40 | TXT_GER_ARQ | VARCHAR2(4000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA, NRO_REFERENCIA_X751, DATA_APURACAO_X751

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DARF → X2019_COD_DARF(IDENT_DARF)
- COD_TRIBUTO → DWT_TRIBUTO(COD_TRIBUTO)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)
- COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA → X75_DCTF(COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA)

**Indexes**:
- IX_X751_DCTF_COMPL: (NRO_REFERENCIA_X751)

---

## X75_DCTF

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
| 28 | SITUACAO | CHAR(1) | Y | 'A' |  |
| 29 | STATUS | CHAR(1) | Y | 'A' |  |
| 30 | NUM_REF_DARF | VARCHAR2(17) | Y |  |  |
| 31 | IND_POR_EMPRESA | CHAR(1) | Y | 'N' |  |
| 32 | NUM_QUOTA | NUMBER(2) | N | 0 |  |
| 33 | IDENT_OPERACAO | NUMBER(12) | Y |  |  |
| 34 | ID_GER | NUMBER(12) | Y |  |  |
| 35 | SEQ_GER_ARQ | NUMBER(12) | Y |  |  |
| 36 | TXT_GER_ARQ | VARCHAR2(4000) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_APURACAO, IDENT_DARF, NRO_REFERENCIA, NUM_QUOTA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_DARF → X2019_COD_DARF(IDENT_DARF)
- COD_TRIBUTO → DWT_TRIBUTO(COD_TRIBUTO)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)
- IDENT_OPERACAO → X2001_OPERACAO(IDENT_OPERACAO)

**Indexes**:
- IX_X75_NRO_REF: (NRO_REFERENCIA)

---

## X76_CPRES_IPI_CEXP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 5 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 6 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 7 | IND_ETIQ_PROD | CHAR(1) | N |  |  |
| 8 | COD_ETIQ_PROD | VARCHAR2(60) | N |  |  |
| 9 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 10 | NUM_EMBARQUE | VARCHAR2(12) | Y |  |  |
| 11 | DAT_EMBARQUE | DATE | Y |  |  |
| 12 | NUM_DESPACHO | VARCHAR2(11) | Y |  |  |
| 13 | VLR_DESPACHO | NUMBER(17,2) | Y |  |  |
| 14 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 15 | NUM_RE | VARCHAR2(15) | Y |  |  |
| 16 | IDENT_FISJUR_AQUIS | NUMBER(12) | Y |  |  |
| 17 | IDENT_FISJUR_VENDA | NUMBER(12) | Y |  |  |
| 18 | IND_TOT_PARC | CHAR(1) | Y |  |  |
| 19 | VLR_PARCIAL | NUMBER(17,2) | Y |  |  |
| 20 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 21 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 22 | IND_COMPRA_VENDA | CHAR(1) | Y |  |  |
| 23 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 24 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 25 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IND_ETIQ_PROD, COD_ETIQ_PROD

**FKs**:
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- COD_PAIS → PAIS(COD_PAIS)
- IDENT_FISJUR_AQUIS → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_FISJUR_VENDA → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_FK_SAF_0517: (IDENT_FISJUR_AQUIS)
- IX_FK_SAF_0518: (IDENT_FISJUR_VENDA)

---

## X77_DRBK_ENTRADA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | IND_CONTROLE | CHAR(1) | N |  |  |
| 6 | NUM_CONTROLE | VARCHAR2(15) | N |  |  |
| 7 | IND_COD_CONTROLE | CHAR(1) | N |  |  |
| 8 | COD_CONTROLE | VARCHAR2(60) | N |  |  |
| 9 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 13 | COD_AG_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 14 | ANO_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 15 | NUM_ATO_CONCES | VARCHAR2(6) | Y |  |  |
| 16 | DIG_ATO_CONCES | CHAR(1) | Y |  |  |
| 17 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 18 | PESO_BRUTO_MERC | NUMBER(17,3) | Y |  |  |
| 19 | PESO_LIQ_MERC | NUMBER(17,3) | Y |  |  |
| 20 | QTD_MERC | NUMBER(17,6) | Y |  |  |
| 21 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 22 | VLR_FRETE | NUMBER(17,2) | Y |  |  |
| 23 | VLR_SEGURO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_OUTRAS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_MERC_LOC_EMB | NUMBER(17,2) | Y |  |  |
| 26 | VLR_MERC | NUMBER(17,2) | Y |  |  |
| 27 | VLR_MERC_US | NUMBER(17,4) | Y |  |  |
| 28 | IND_MERCADO | CHAR(1) | Y |  |  |
| 29 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 30 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 31 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 32 | NUM_DI | VARCHAR2(15) | Y |  |  |
| 33 | DAT_DI | DATE | Y |  |  |
| 34 | OBS_COMPLEMENTAR | VARCHAR2(200) | Y |  |  |
| 35 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 36 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, IND_CONTROLE, NUM_CONTROLE, IND_COD_CONTROLE, COD_CONTROLE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- COD_PAIS → PAIS(COD_PAIS)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES → FDT_ATO_CONCES(COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- IX_FK_SAF_0533: (IDENT_FIS_JUR)

---

## X78_DRBK_SAIDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IND_CONTROLE | CHAR(1) | N |  |  |
| 5 | NUM_CONTROLE | VARCHAR2(15) | N |  |  |
| 6 | IND_COD_CONTROLE | CHAR(1) | N |  |  |
| 7 | COD_CONTROLE | VARCHAR2(60) | N |  |  |
| 8 | NUM_DOCFIS | VARCHAR2(12) | Y |  |  |
| 9 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 10 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 11 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 12 | IDENT_FIS_JUR | NUMBER(12) | Y |  |  |
| 13 | COD_AG_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 14 | ANO_ATO_CONCES | VARCHAR2(4) | Y |  |  |
| 15 | NUM_ATO_CONCES | VARCHAR2(6) | Y |  |  |
| 16 | DIG_ATO_CONCES | CHAR(1) | Y |  |  |
| 17 | VLR_DOCFIS | NUMBER(17,2) | Y |  |  |
| 18 | PESO_BRUTO_MERC | NUMBER(17,3) | Y |  |  |
| 19 | PESO_LIQ_MERC | NUMBER(17,3) | Y |  |  |
| 20 | VLR_UNITARIO | NUMBER(17,2) | Y |  |  |
| 21 | QTD_MERC | NUMBER(17,6) | Y |  |  |
| 22 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 23 | VLR_COMISSAO | NUMBER(17,2) | Y |  |  |
| 24 | VLR_DESCONTO | NUMBER(17,2) | Y |  |  |
| 25 | VLR_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 26 | VLR_MERC_LOC_EMB | NUMBER(17,2) | Y |  |  |
| 27 | VLR_MERC | NUMBER(17,2) | Y |  |  |
| 28 | VLR_MERC_US | NUMBER(17,4) | Y |  |  |
| 29 | IND_MERCADO | CHAR(1) | Y |  |  |
| 30 | IDENT_NBM | NUMBER(12) | Y |  |  |
| 31 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 32 | COD_INDICE | VARCHAR2(10) | Y |  |  |
| 33 | NUM_RE | VARCHAR2(15) | Y |  |  |
| 34 | DAT_EMBARQUE | DATE | Y |  |  |
| 35 | NUM_DESPACHO | VARCHAR2(11) | Y |  |  |
| 36 | VLR_DESPACHO | NUMBER(17,2) | Y |  |  |
| 37 | OBS_COMPLEMENTAR | VARCHAR2(200) | Y |  |  |
| 38 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 39 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IND_CONTROLE, NUM_CONTROLE, IND_COD_CONTROLE, COD_CONTROLE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_NBM → X2043_COD_NBM(IDENT_NBM)
- COD_PAIS → PAIS(COD_PAIS)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_INDICE → Y2046_INDICE(COD_INDICE)
- COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES → FDT_ATO_CONCES(COD_EMPRESA, COD_ESTAB, COD_AG_ATO_CONCES, ANO_ATO_CONCES, NUM_ATO_CONCES, DIG_ATO_CONCES)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)

**Indexes**:
- IX_FK_SAF_0525: (IDENT_FIS_JUR)

---

## X79_SALDOS_FORNEC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IND_PAG_REC | CHAR(1) | N |  |  |
| 4 | DAT_SALDO | DATE | N |  |  |
| 5 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 6 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 7 | VLR_SALDO_CONTAB | NUMBER(17,2) | Y |  |  |
| 8 | IND_DEB_CRED | CHAR(1) | Y |  |  |
| 9 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IND_PAG_REC, DAT_SALDO, IDENT_FIS_JUR, IDENT_CONTA

**FKs**:
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_FK_SAF_0837: (IDENT_FIS_JUR)
- IX_X79_SALDOS_F_CTA: (IDENT_CONTA)

---

## X80_SALDOS_CCUSTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_SALDO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IDENT_CUSTO | NUMBER(12) | N |  |  |
| 6 | VLR_SALDO_CONT_ANT | NUMBER(19,2) | Y |  |  |
| 7 | IND_DEB_CRED_ANT | CHAR(1) | Y |  |  |
| 8 | VLR_TOT_DEB | NUMBER(19,2) | Y |  |  |
| 9 | VLR_TOT_CRED | NUMBER(19,2) | Y |  |  |
| 10 | VLR_SALDO_CONT_ATU | NUMBER(19,2) | Y |  |  |
| 11 | IND_DEB_CRED_ATU | CHAR(1) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 14 | IDENTIF_SALDO | VARCHAR2(128) | Y |  |  |
| 15 | COD_SISTEMA_ORIG | VARCHAR2(4) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_CUSTO

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_CUSTO → X2003_CENTRO_CUSTO(IDENT_CUSTO)

**Indexes**:
- IX_X80_SALDOS_CC_CTA: (IDENT_CONTA)

---

## X81_SALDOS_SCONTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_SALDO | DATE | N |  |  |
| 4 | IDENT_CONTA | NUMBER(12) | N |  |  |
| 5 | IDENT_SUB_CONTA | NUMBER(12) | N |  |  |
| 6 | VLR_SALDO_CONT_ANT | NUMBER(17,2) | Y |  |  |
| 7 | IND_DEB_CRED_ANT | CHAR(1) | Y |  |  |
| 8 | VLR_TOT_DEB | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TOT_CRED | NUMBER(17,2) | Y |  |  |
| 10 | VLR_SALDO_CONT_ATU | NUMBER(17,2) | Y |  |  |
| 11 | IND_DEB_CRED_ATU | CHAR(1) | Y |  |  |
| 12 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 13 | NUM_PROCESSO | NUMBER(12) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_SALDO, IDENT_CONTA, IDENT_SUB_CONTA

**FKs**:
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_SUB_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)

**Indexes**:
- IX_X81_SALDOS_SC_CTA: (IDENT_CONTA)
- IX_X81_SALDOS_SUBCTA: (IDENT_SUB_CONTA)

---

## X90_MOV_TRIBUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | COD_TRIBUTO | VARCHAR2(2) | N |  |  |
| 4 | ESP_TRIBUTO | VARCHAR2(2) | N |  |  |
| 5 | IND_TRIB_INCENT | VARCHAR2(1) | N |  |  |
| 6 | COD_CLASSE_OPER | VARCHAR2(1) | N |  |  |
| 7 | DAT_MOVTO | DATE | N |  |  |
| 8 | TP_ORIGEM | VARCHAR2(2) | N |  |  |
| 9 | DOCTO_ORIGEM | VARCHAR2(25) | N |  |  |
| 10 | REF_ORIGEM | VARCHAR2(5) | N |  |  |
| 11 | IDENT_AREA_NEGOC | NUMBER(12) | Y |  |  |
| 12 | IDENT_UNID_NEGOC | NUMBER(12) | Y |  |  |
| 13 | IDENT_CENTRO_RESP | NUMBER(12) | Y |  |  |
| 14 | COD_LOCALIDADE | NUMBER(5) | Y |  |  |
| 15 | GRUPO_SERVICO | VARCHAR2(9) | Y |  |  |
| 16 | COD_SERVICO | VARCHAR2(4) | Y |  |  |
| 17 | GRUPO_PRODUTO | VARCHAR2(9) | Y |  |  |
| 18 | IND_PRODUTO | CHAR(1) | Y |  |  |
| 19 | COD_PRODUTO | VARCHAR2(60) | Y |  |  |
| 20 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 21 | COD_PAIS | VARCHAR2(3) | Y |  |  |
| 22 | IND_MERCADO | VARCHAR2(1) | Y |  |  |
| 23 | IND_DEB_CRED | VARCHAR2(1) | Y |  |  |
| 24 | COD_INDICE_CORREC | VARCHAR2(10) | Y |  |  |
| 25 | VLR_MOVTO | NUMBER(17,2) | Y |  |  |
| 26 | VLR_PRINC_REC | NUMBER(17,2) | Y |  |  |
| 27 | VLR_JUROS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_MULTA_MORAT | NUMBER(17,2) | Y |  |  |
| 29 | VLR_MULTA_INFRAC | NUMBER(17,2) | Y |  |  |
| 30 | VLR_CORRECAO | NUMBER(17,2) | Y |  |  |
| 31 | VLR_DEDUCOES | NUMBER(17,2) | Y |  |  |
| 32 | VLR_COMPENS | NUMBER(17,2) | Y |  |  |
| 33 | VLR_TOT_REC | NUMBER(17,2) | Y |  |  |
| 34 | DAT_INI_COMPET | DATE | Y |  |  |
| 35 | DAT_FIM_COMPET | DATE | Y |  |  |
| 36 | DAT_APURAC_INI | DATE | Y |  |  |
| 37 | DAT_APURAC_FIM | DATE | Y |  |  |
| 38 | DAT_VENCTO | DATE | Y |  |  |
| 39 | VLR_IND_ATUALIZ | NUMBER(9,6) | Y |  |  |
| 40 | VLR_RECOLH | NUMBER(17,2) | Y |  |  |
| 41 | DAT_RECOLH | DATE | Y |  |  |
| 42 | ORG_ARRECAD | VARCHAR2(30) | Y |  |  |
| 43 | OBS | VARCHAR2(320) | Y |  |  |
| 44 | IDENT_DARF | NUMBER(12) | Y |  |  |
| 45 | COD_RECEITA | VARCHAR2(6) | Y |  |  |
| 46 | COD_ARREC_MUNIC | VARCHAR2(4) | Y |  |  |
| 47 | COD_ARREC_ESTAD | VARCHAR2(4) | Y |  |  |
| 48 | IND_PROD_PROPRIO | CHAR(1) | Y |  |  |
| 49 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 50 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 51 | COD_USUARIO | VARCHAR2(40) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, COD_TRIBUTO, ESP_TRIBUTO, IND_TRIB_INCENT, COD_CLASSE_OPER, DAT_MOVTO, TP_ORIGEM, DOCTO_ORIGEM, REF_ORIGEM

**FKs**:
- COD_EMPRESA → EMPRESA(COD_EMPRESA)
- COD_TRIBUTO, ESP_TRIBUTO → DWT_TRIBUTO_ESP(COD_TRIBUTO, ESP_TRIBUTO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_UNID_NEGOC → X2095_UNID_NEGOC(IDENT_UNID_NEGOC)
- IDENT_CENTRO_RESP → X2094_CENTRO_RESP(IDENT_CENTRO_RESP)
- GRUPO_SERVICO, COD_SERVICO → PLT_SERVICO(GRUPO_SERVICO, COD_SERVICO)
- GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO → PLT_PRODUTO(GRUPO_PRODUTO, IND_PRODUTO, COD_PRODUTO)
- COD_PAIS → PAIS(COD_PAIS)
- COD_INDICE_CORREC → Y2046_INDICE(COD_INDICE)
- IDENT_DARF → X2019_COD_DARF(IDENT_DARF)
- COD_RECEITA → DWT_COD_RECEITA(COD_RECEITA)
- IDENT_AREA_NEGOC → X2096_AREA_NEGOC(IDENT_AREA_NEGOC)

---

## X91_SUBEMPREIT_ISS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 9 | VLR_ALIQ_ISS | NUMBER(7,4) | Y |  |  |
| 10 | VLR_ISS | NUMBER(17,2) | Y |  |  |
| 11 | VLR_SALDO_ISS | NUMBER(17,2) | Y |  |  |
| 12 | DAT_EMISSAO | DATE | Y |  |  |
| 13 | NUM_CONTRATO | VARCHAR2(14) | N |  |  |
| 14 | COD_MUNIC_ISS | NUMBER(7) | Y |  |  |
| 15 | COD_OBRA | VARCHAR2(15) | Y |  |  |
| 16 | DAT_APROP_ABAT | DATE | Y |  |  |
| 17 | IND_SITUACAO_ABAT | CHAR(1) | Y |  |  |
| 18 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 19 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 20 | IND_COMPROVANTE | CHAR(1) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_CONTRATO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_FIS_JUR → X04_PESSOA_FIS_JUR(IDENT_FIS_JUR)
- COD_MUNIC_ISS → X2097_MUNIC_ISS(COD_MUNIC_ISS)

**Indexes**:
- IX_FK_SAF_0990: (IDENT_FIS_JUR)

---

## X91_SUBEMPR_ABAT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DAT_FISCAL | DATE | N |  |  |
| 4 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 5 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 6 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 7 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 8 | DAT_APURACAO | DATE | N |  |  |
| 9 | VLR_ISS_ABAT | NUMBER(17,2) | Y |  |  |
| 10 | IND_DIG_CALC | CHAR(1) | Y |  |  |
| 11 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 12 | NUM_CONTRATO | VARCHAR2(14) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, DAT_APURACAO, NUM_CONTRATO

**FKs**:
- COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_CONTRATO → X91_SUBEMPREIT_ISS(COD_EMPRESA, COD_ESTAB, DAT_FISCAL, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_CONTRATO)

---

## X96_GRP_COMB_PROD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 2 | VALID_GRP_COMB_PRD | DATE | N |  |  |
| 3 | IDENT_GRP_COMB | NUMBER(12) | Y |  |  |
| 4 | FATOR_CONV_GAS_A | NUMBER(7,6) | Y |  |  |
| 5 | FATOR_PERDA | NUMBER(7,6) | Y |  |  |
| 6 | FATOR_GANHO | NUMBER(7,6) | Y |  |  |
| 7 | COD_PROD_OFICIAL | VARCHAR2(10) | Y |  |  |
| 8 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 9 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 10 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 11 | FATOR_DIV_GAS_A | NUMBER(7,6) | Y |  |  |

**PK**: IDENT_PRODUTO, VALID_GRP_COMB_PRD

**FKs**:
- IDENT_GRP_COMB → CBT_GRP_COMB(IDENT_GRP_COMB)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)

**Indexes**:
- IX_X96_GRP_COMP_PR: (IDENT_GRP_COMB)

---

## X97_SITUACAO_AIDF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_ENTREGA | DATE | N |  |  |
| 4 | NRO_AIDF | VARCHAR2(12) | N |  |  |
| 5 | COD_SITUACAO | VARCHAR2(2) | N |  |  |
| 6 | DAT_OCOR | DATE | N |  |  |
| 7 | IDENT_MODELO | NUMBER(12) | N |  |  |
| 8 | NUM_CTR_DISP_INI | VARCHAR2(12) | N |  |  |
| 9 | SERIE_CTR_DISP | VARCHAR2(3) | N |  |  |
| 10 | SUB_SERIE_CTR_DISP | VARCHAR2(3) | N |  |  |
| 11 | COD_TP_DISP_SEG | VARCHAR2(2) | N |  |  |
| 12 | NUM_CTR_DISP_FIM | VARCHAR2(12) | Y |  |  |
| 13 | COD_OPERACAO | VARCHAR2(2) | Y |  |  |
| 14 | COD_TIPO_REGISTRO | VARCHAR2(2) | Y |  |  |
| 15 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 16 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 17 | NUM_CAIXA | NUMBER(6) | Y | 0 |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_ENTREGA, NRO_AIDF, COD_SITUACAO, DAT_OCOR, IDENT_MODELO, NUM_CTR_DISP_INI, SERIE_CTR_DISP, SUB_SERIE_CTR_DISP, COD_TP_DISP_SEG

---

## X98_MOVTO_SINDAG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_PRODUTO | NUMBER(12) | N |  |  |
| 4 | DATA_MOVTO | DATE | N |  |  |
| 5 | MOVTO_E_S | CHAR(1) | N |  |  |
| 6 | TIPO_OPERACAO | NUMBER(2) | N |  |  |
| 7 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 8 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 9 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 10 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 11 | TIPO_VISTO | NUMBER(6) | Y |  |  |
| 12 | QTD_MOVTO | NUMBER(17,6) | Y |  |  |
| 13 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 14 | TIPO | VARCHAR2(6) | Y |  |  |
| 15 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 16 | REFERENCIA | VARCHAR2(45) | Y |  |  |
| 17 | OBSERVACAO | VARCHAR2(90) | Y |  |  |
| 18 | IND_ESPEC_MAT | CHAR(1) | Y |  |  |
| 19 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 20 | IDENT_NATUREZA_OP | NUMBER(12) | Y |  |  |
| 21 | GUIA_TRAFEGO | VARCHAR2(40) | Y |  |  |
| 22 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 23 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 24 | NUM_RECEITA | NUMBER(15) | Y |  |  |
| 25 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, IDENT_PRODUTO, DATA_MOVTO, MOVTO_E_S, TIPO_OPERACAO, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, IDENT_FIS_JUR

---

## X991_CAPA_REDUCAO_ECF
**Comment**: Movimento da Redução Z (Capa) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_CRZ | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 7 | NUM_CRO | VARCHAR2(6) | Y |  |  |
| 8 | DATA_EMISSAO | DATE | Y |  |  |
| 9 | HORA_EMISSAO | NUMBER(6) | Y |  |  |
| 10 | NUM_COO_INI | VARCHAR2(9) | Y |  |  |
| 11 | NUM_COO_FIM | VARCHAR2(9) | Y |  |  |
| 12 | VLR_GT_INI | NUMBER(17,2) | Y |  |  |
| 13 | VLR_GT_FIM | NUMBER(17,2) | Y |  |  |
| 14 | VLR_VENDA_BRUTA | NUMBER(17,2) | Y |  |  |
| 15 | VLR_VENDA_LIQ | NUMBER(17,2) | Y |  |  |
| 16 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 17 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 18 | VLR_BASE_ICMS | NUMBER(17,2) | Y |  |  |
| 19 | VLR_TRIBUTO_ICMS | NUMBER(17,2) | Y |  |  |
| 20 | VLR_OPER_ICMS_ST | NUMBER(17,2) | Y |  |  |
| 21 | VLR_OPER_ISENTA_ICMS | NUMBER(17,2) | Y |  |  |
| 22 | VLR_OPER_N_INCID_ICMS | NUMBER(17,2) | Y |  |  |
| 23 | VLR_OPER_DESC_ICMS | NUMBER(17,2) | Y |  |  |
| 24 | VLR_OPER_ACRES_ICMS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_OPER_CANC_ICMS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_OPER_IOF | NUMBER(17,2) | Y |  |  |
| 27 | VLR_BASE_ISS | NUMBER(17,2) | Y |  |  |
| 28 | VLR_TRIBUTO_ISS | NUMBER(17,2) | Y |  |  |
| 29 | VLR_OPER_ISS_ST | NUMBER(17,2) | Y |  |  |
| 30 | VLR_OPER_ISENTA_ISS | NUMBER(17,2) | Y |  |  |
| 31 | VLR_OPER_N_INCID_ISS | NUMBER(17,2) | Y |  |  |
| 32 | VLR_OPER_DESC_ISS | NUMBER(17,2) | Y |  |  |
| 33 | VLR_OPER_ACRES_ISS | NUMBER(17,2) | Y |  |  |
| 34 | VLR_OPER_CANC_ISS | NUMBER(17,2) | Y |  |  |
| 35 | VLR_OPER_N_FISCAL | NUMBER(17,2) | Y |  |  |
| 36 | VLR_OPER_DESC_N_FISCAL | NUMBER(17,2) | Y |  |  |
| 37 | VLR_OPER_ACRES_N_FISCAL | NUMBER(17,2) | Y |  |  |
| 38 | VLR_OPER_CANC_N_FISCAL | NUMBER(17,2) | Y |  |  |
| 39 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 40 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 41 | IDENT_SCP | NUMBER(12) | Y |  |  |

**PK**: DATA_FISCAL, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_CRZ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CAIXA_ECF → X2087_EQUIPAMENTO_ECF(IDENT_CAIXA_ECF)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

---

## X992_ITEM_REDUCAO_ECF
**Comment**: Movimento da Redução Z (Item) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_CRZ | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | IDENT_TOTALIZADOR_ECF | NUMBER(12) | N |  |  |
| 7 | VLR_OPER | NUMBER(17,2) | Y |  |  |
| 8 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 9 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: DATA_FISCAL, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, IDENT_TOTALIZADOR_ECF, NUM_CRZ

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CAIXA_ECF → X2087_EQUIPAMENTO_ECF(IDENT_CAIXA_ECF)
- IDENT_TOTALIZADOR_ECF → X996_TOTALIZADOR_PARCIAL_ECF(IDENT_TOTALIZADOR_ECF)
- DATA_FISCAL, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_CRZ → X991_CAPA_REDUCAO_ECF(DATA_FISCAL, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_CRZ)

---

## X993_CAPA_CUPOM_ECF
**Comment**: Movimento de Cupom (Capa) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_COO | VARCHAR2(9) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | NOME_CLIENTE | VARCHAR2(40) | Y |  |  |
| 7 | CPF_CNPJ_CLIENTE | VARCHAR2(14) | Y |  |  |
| 8 | IND_TIPO_CUPOM | CHAR(1) | Y |  |  |
| 9 | IND_SITUACAO_CUPOM | CHAR(1) | Y |  |  |
| 10 | COD_DENOMINACAO | VARCHAR2(2) | Y |  |  |
| 11 | NUM_COO_VINCULADO | VARCHAR2(9) | Y |  |  |
| 12 | NUM_CCF_CVC_CBP | VARCHAR2(9) | Y |  |  |
| 13 | NUM_GNF | VARCHAR2(9) | Y |  |  |
| 14 | NUM_GRG | VARCHAR2(9) | Y |  |  |
| 15 | NUM_CDC | VARCHAR2(6) | Y |  |  |
| 16 | NUM_CRZ | VARCHAR2(6) | Y |  |  |
| 17 | DATA_EMISSAO_FIM | DATE | Y |  |  |
| 18 | HORA_EMISSAO_FIM | NUMBER(6) | Y |  |  |
| 19 | IDENT_ESTADO | NUMBER(12) | Y |  |  |
| 20 | COD_MUNICIPIO | NUMBER(5) | Y |  |  |
| 21 | VLR_LIQ_ITEM | NUMBER(17,2) | Y |  |  |
| 22 | VLR_DESC_CAPA | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ACRES_CAPA | NUMBER(17,2) | Y |  |  |
| 24 | VLR_TOTAL_LIQ | NUMBER(17,2) | Y |  |  |
| 25 | VLR_ACRES_CAPA_CANC | NUMBER(17,2) | Y |  |  |
| 26 | VLR_IOF | NUMBER(17,2) | Y |  |  |
| 27 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 28 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 29 | DSC_CHAVE_CFE | VARCHAR2(80) | Y |  |  |
| 30 | NUM_CONTADOR_CFE | VARCHAR2(9) | Y |  |  |
| 31 | DATA_TRAB | DATE | Y | CASE  WHEN ("DATA_EMISSAO"=TRUNC("DATA_EMISSAO"... |  |

**PK**: DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CAIXA_ECF → X2087_EQUIPAMENTO_ECF(IDENT_CAIXA_ECF)
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

**Indexes**:
- IX_X993_CAPA_CUPOM_ECF_01: (DATA_TRAB, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO)
- IX_X993_CAPA_CUPOM_ECF_02: (IDENT_CAIXA_ECF)

---

## X994_ITEM_CUPOM_ECF
**Comment**: Movimento de Cupom (Item) do Equipamento Emissor de Cupom Fiscall

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_COO | VARCHAR2(9) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | NUM_ITEM | NUMBER(5) | N |  |  |
| 7 | IDENT_PRODUTO | NUMBER(12) | Y |  |  |
| 8 | IDENT_SERVICO | NUMBER(12) | Y |  |  |
| 9 | IND_SITUACAO_ITEM | CHAR(1) | Y |  |  |
| 10 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 11 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 12 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 13 | IDENT_TOTALIZADOR_ECF | NUMBER(12) | Y |  |  |
| 14 | QTDE | NUMBER(17,4) | Y |  |  |
| 15 | IDENT_MEDIDA | NUMBER(12) | Y |  |  |
| 16 | VLR_UNIT | NUMBER(19,4) | Y |  |  |
| 17 | VLR_ITEM | NUMBER(17,2) | Y |  |  |
| 18 | VLR_DESC | NUMBER(17,2) | Y |  |  |
| 19 | VLR_ACRES | NUMBER(17,2) | Y |  |  |
| 20 | VLR_LIQ_ITEM | NUMBER(17,2) | Y |  |  |
| 21 | QTDE_CANC | NUMBER(17,4) | Y |  |  |
| 22 | VLR_ITEM_CANC | NUMBER(17,2) | Y |  |  |
| 23 | VLR_ACRES_CANC | NUMBER(17,2) | Y |  |  |
| 24 | VLR_PIS | NUMBER(17,2) | Y |  |  |
| 25 | VLR_COFINS | NUMBER(17,2) | Y |  |  |
| 26 | VLR_BASE | NUMBER(17,2) | Y |  |  |
| 27 | VLR_TRIBUTO | NUMBER(17,2) | Y |  |  |
| 28 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 29 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 30 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 31 | COD_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 32 | COD_SIT_TRIB_PIS | NUMBER(2) | Y |  |  |
| 33 | VLR_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 34 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 35 | COD_SIT_TRIB_COFINS | NUMBER(2) | Y |  |  |
| 36 | VLR_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 37 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |
| 38 | QTD_BASE_PIS | NUMBER(18,3) | Y |  |  |
| 39 | VLR_ALIQ_ESPEC_PIS | NUMBER(19,4) | Y |  |  |
| 40 | IDENT_CONTA | NUMBER(12) | Y |  |  |
| 41 | QTD_BASE_COFINS | NUMBER(18,3) | Y |  |  |
| 42 | VLR_ALIQ_ESPEC_COFINS | NUMBER(19,4) | Y |  |  |
| 43 | COD_NAT_REC | NUMBER(3) | Y |  |  |
| 44 | IDENT_SCP | NUMBER(12) | Y |  |  |
| 45 | COD_AMPARO_LEGAL | VARCHAR2(10) | Y |  |  |

**PK**: DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO, NUM_ITEM

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CAIXA_ECF → X2087_EQUIPAMENTO_ECF(IDENT_CAIXA_ECF)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)
- IDENT_MEDIDA → X2007_MEDIDA(IDENT_MEDIDA)
- IDENT_PRODUTO → X2013_PRODUTO(IDENT_PRODUTO)
- IDENT_SERVICO → X2018_SERVICOS(IDENT_SERVICO)
- IDENT_TOTALIZADOR_ECF → X996_TOTALIZADOR_PARCIAL_ECF(IDENT_TOTALIZADOR_ECF)
- DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO → X993_CAPA_CUPOM_ECF(DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO)
- IDENT_CONTA → X2002_PLANO_CONTAS(IDENT_CONTA)
- IDENT_SCP → X2057_COD_SCP(IDENT_SCP)

**Indexes**:
- IX_X994_ITEM_CUPOM_CTA: (IDENT_CONTA)

---

## X995_PAGTO_CUPOM_ECF
**Comment**: Movimento de Cupom (Pagamento) do Equipamento Emissor de Cupom Fiscal

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | IDENT_CAIXA_ECF | NUMBER(12) | N |  |  |
| 4 | NUM_COO | VARCHAR2(9) | N |  |  |
| 5 | DATA_EMISSAO | DATE | N |  |  |
| 6 | IDENT_MEIO_PAGTO | NUMBER(12) | N |  |  |
| 7 | VLR_PAGO | NUMBER(17,2) | Y |  |  |
| 8 | IND_ESTORNO | CHAR(1) | Y |  |  |
| 9 | VLR_ESTORNO | NUMBER(17,2) | Y |  |  |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |
| 12 | NUM_COMPROVANTE | VARCHAR2(18) | Y |  |  |
| 13 | IND_NAT_OPERACAO | NUMBER(1) | Y |  |  |
| 14 | IND_TIPO_OPERACAO | NUMBER(1) | Y |  |  |
| 15 | CEP | NUMBER(8) | Y |  |  |

**PK**: DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO, IDENT_MEIO_PAGTO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_CAIXA_ECF → X2087_EQUIPAMENTO_ECF(IDENT_CAIXA_ECF)
- IDENT_MEIO_PAGTO → DWT_MEIO_PAGTO_ECF(IDENT_MEIO_PAGTO)
- DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO → X993_CAPA_CUPOM_ECF(DATA_EMISSAO, COD_ESTAB, IDENT_CAIXA_ECF, COD_EMPRESA, NUM_COO)

---

## X996_TOTALIZADOR_PARCIAL_ECF
**Comment**: Cadastro do Totalizador Parcial do ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_TOTALIZADOR_ECF | NUMBER(12) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 5 | COD_MODELO | VARCHAR2(2) | N |  |  |
| 6 | COD_CAIXA_ECF | VARCHAR2(3) | N |  | Número do Caixa do ECF cadastrado na X2087_EQUIPAMENTO_ECF. |
| 7 | COD_TOTALIZADOR_ECF | VARCHAR2(7) | N |  | Código do Totalizador utilizado no ECF do cliente. |
| 8 | VALID_TOTALIZADOR_ECF | DATE | N |  |  |
| 9 | DSC_TOTALIZADOR_ECF | VARCHAR2(50) | Y |  |  |
| 10 | NUM_SEQ_TOTALIZADOR | VARCHAR2(2) | Y |  |  |
| 11 | DSC_SIT_TRIBUTARIA | VARCHAR2(50) | Y |  |  |
| 12 | VLR_ALIQ | NUMBER(7,4) | Y |  |  |
| 13 | IDENT_SITUACAO_A | NUMBER(12) | Y |  |  |
| 14 | IDENT_SITUACAO_B | NUMBER(12) | Y |  |  |
| 15 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 16 | COD_CFPS | VARCHAR2(4) | Y |  |  |
| 17 | COD_TRIB_ISS | VARCHAR2(2) | Y |  |  |
| 18 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 19 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: IDENT_TOTALIZADOR_ECF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- IDENT_SITUACAO_A → Y2025_SIT_TRB_UF_A(IDENT_SITUACAO_A)
- IDENT_SITUACAO_B → Y2026_SIT_TRB_UF_B(IDENT_SITUACAO_B)
- IDENT_CFO → X2012_COD_FISCAL(IDENT_CFO)

**Indexes**:
- IX_X996_TOT_PARCIAL_ECF: (COD_ESTAB, COD_CAIXA_ECF, COD_TOTALIZADOR_ECF, COD_EMPRESA, COD_MODELO, GRUPO_MODELO, VALID_TOTALIZADOR_ECF)

---

## X99_TOTALIZADOR_ECF
**Comment**: Parametrização do Totalizador Parcial do ECF para as Obrigações Fiscais

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | GRUPO_MODELO | VARCHAR2(9) | N |  |  |
| 4 | COD_MODELO | VARCHAR2(2) | N |  | Código do Modelo do documento (X2024_MODELO_DOCTO) emitido pelo ECF.Código do Modelo e Número do Caixa do ECF cadastrados na X2087_EQUIPAMENTO_ECF. |
| 5 | COD_CAIXA_ECF | VARCHAR2(3) | N |  | Número do Caixa do ECF cadastrado na X2087_EQUIPAMENTO_ECF. |
| 6 | IND_TIPO_OBRIG | CHAR(1) | N |  | Indicador do Tipo de Obrigação Fiscal cadastrado na DWT_TOTALIZADOR_OBRIG_ECF. DOMÍNIO: 1 - REDF, 2 - EFD. |
| 7 | COD_TOTALIZADOR_ECF | VARCHAR2(7) | N |  | Código do Totalizador utilizado no ECF do cliente, cadastrado na X996_TOTALIZADOR_PARCIAL_ECF. |
| 8 | VALID_X99_TOT_ECF | DATE | N |  |  |
| 9 | COD_TOTALIZADOR_OBRIG | VARCHAR2(7) | Y |  | Código do Totalizador das Obrigações Fiscais, cadastrado na DWT_TOTALIZADOR_OBRIG_ECF. |
| 10 | NUM_PROCESSO | NUMBER(12) | Y |  |  |
| 11 | IND_GRAVACAO | CHAR(1) | Y |  |  |

**PK**: COD_ESTAB, COD_CAIXA_ECF, COD_TOTALIZADOR_ECF, COD_EMPRESA, IND_TIPO_OBRIG, COD_MODELO, GRUPO_MODELO, VALID_X99_TOT_ECF

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- COD_TOTALIZADOR_OBRIG, IND_TIPO_OBRIG → DWT_TOTALIZADOR_OBRIG_ECF(COD_TOTALIZADOR_OBRIG, IND_TIPO_OBRIG)

---

