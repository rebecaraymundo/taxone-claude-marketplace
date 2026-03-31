# Módulo: RDF (RDF) - 32 tabelas

## RDF_ALERTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ALERTA | NUMBER(15) | N |  |  |
| 2 | ID_RDF_LOG_ENVIO | NUMBER(15) | N |  |  |
| 3 | DESC_ALERTA | VARCHAR2(200) | N |  |  |

**PK**: ID_ALERTA, ID_RDF_LOG_ENVIO

**Indexes**:
- IX_RDF_ALERTAS_01: (ID_RDF_LOG_ENVIO)

---

## RDF_ARQGERADOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ARQUIVO | NUMBER(15) | N |  |  |
| 2 | ID_DIRETORIO | NUMBER(15) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | ID_TIPO | NUMBER(10) | N |  |  |
| 6 | DATA_GERACAO | DATE | N |  |  |
| 7 | NOM_ARQUIVO | VARCHAR2(100) | Y |  |  |
| 8 | FLG_DATA_MOV | DATE | Y |  |  |
| 9 | DATA_TRANSMISSAO | DATE | Y |  |  |
| 10 | PROTOCOLO_SEFAZ | VARCHAR2(15) | Y |  |  |
| 11 | ID_DIRETORIO_MOV | NUMBER(15) | Y |  |  |
| 12 | FLG_PROCESSADO | CHAR(1) | Y |  |  |
| 13 | FLG_STATUS_ARQUIVO | NUMBER(1) | Y |  |  |
| 14 | PROC_ID | NUMBER(22) | N |  |  |

**PK**: ID_ARQUIVO

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- ID_TIPO → RDF_TIPO_ARQUIVO(ID_TIPO)

**Indexes**:
- IX_RDF_ARQGERADOS_01: (PROC_ID)
- IX_RDF_ARQGERADOS_02: (COD_EMPRESA, COD_ESTAB)
- IX_RDF_ARQGERADOS_03: (ID_DIRETORIO, COD_EMPRESA, COD_ESTAB)

---

## RDF_ARQGERAR_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | DATA_FISCAL | DATE | N |  |  |
| 4 | ID_TIPO | NUMBER(10) | N |  |  |
| 5 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 6 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 9 | CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 10 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 11 | SERIE_DOCFIS | VARCHAR2(3) | N |  |  |
| 12 | DATA_EMISSAO | DATE | Y |  |  |
| 13 | SUB_SERIE_DOCFIS | VARCHAR2(2) | N |  |  |
| 14 | NUM_DOCFIS | VARCHAR2(14) | N |  |  |
| 15 | MOVTO_E_S | CHAR(1) | N |  |  |
| 16 | NORM_DEV | CHAR(1) | N |  |  |
| 17 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 18 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 19 | DAT_RECEBIMENTO | DATE | Y |  |  |
| 20 | PROC_ID | NUMBER(22) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS, PROC_ID

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- ID_TIPO → RDF_TIPO_ARQUIVO(ID_TIPO)

**Indexes**:
- IX_RDF_ARQGERAR_TEMP_01: (ID_TIPO)
- IX_RDF_ARQGERAR_TEMP_02: (COD_EMPRESA, COD_ESTAB)

---

## RDF_ARQGERA_CUPOM_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | Y |  |  |
| 3 | DATA_EMISSAO | DATE | Y |  |  |
| 4 | IDENT_CAIXA_ECF | NUMBER(12) | Y |  |  |
| 5 | NUM_COO_INI | VARCHAR2(9) | Y |  |  |
| 6 | NUM_COO_FIM | VARCHAR2(9) | Y |  |  |
| 7 | IDENT_FIS_JUR_APLIC | NUMBER(12) | Y |  |  |
| 8 | COD_FABRICACAO_ECF | VARCHAR2(20) | Y |  |  |
| 9 | DATA_EMISSAO_INI | DATE | Y |  |  |
| 10 | DATA_EMISSAO_FIM | DATE | Y |  |  |
| 11 | PROC_ID | NUMBER | Y |  |  |
| 12 | HORA_EMISSAO | NUMBER(6) | Y |  |  |
| 13 | NUM_COO | VARCHAR2(9) | Y |  |  |
| 14 | NUM_CRZ | VARCHAR2(6) | Y |  |  |
| 15 | NUM_CRO | VARCHAR2(6) | Y |  |  |
| 16 | DATA_FISCAL | DATE | Y |  |  |
| 17 | VLR_VENDA_BRUTA | NUMBER(17,2) | Y |  |  |
| 18 | VLR_OPER_DESC_ICMS | NUMBER(17,2) | Y |  |  |

---

## RDF_ARQUIVOS_ECF_MDF_TEMP

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | PROC_ID | NUMBER(22) | Y |  |  |
| 2 | NOM_ARQUIVO | VARCHAR2(255) | Y |  |  |
| 3 | DATA_ARQUIVO | DATE | Y |  |  |
| 4 | QTD_BYTES | NUMBER(8) | Y |  |  |
| 5 | FLG_METODO_COPIA_LE_ECF | NUMBER(1) | Y |  |  |
| 6 | SERVIDOR_LE_ECF | VARCHAR2(40) | Y |  |  |
| 7 | PORTA_LE_ECF | VARCHAR2(4) | Y |  |  |
| 8 | USUARIO_LE_ECF | VARCHAR2(40) | Y |  |  |
| 9 | HOST_LE_ECF | VARCHAR2(80) | Y |  |  |
| 10 | DIRETORIO_LE_ECF | VARCHAR2(1000) | Y |  |  |
| 11 | SENHA_LE_ECF | VARCHAR2(40) | Y |  |  |
| 12 | ID | NUMBER(22) | Y |  |  |
| 13 | FLG_METODO_COPIA | NUMBER(1) | Y |  |  |
| 14 | SERVIDOR | VARCHAR2(40) | Y |  |  |
| 15 | PORTA | VARCHAR2(4) | Y |  |  |
| 16 | USUARIO | VARCHAR2(40) | Y |  |  |
| 17 | HOST | VARCHAR2(80) | Y |  |  |
| 18 | CAMINHO | VARCHAR2(1000) | Y |  |  |
| 19 | SENHA | VARCHAR2(40) | Y |  |  |
| 20 | TIPO_ARQUIVO | VARCHAR2(3) | Y |  |  |

**Indexes**:
- IX_RDF_ARQUIVOS_ECF_MDF_TMP_01: (PROC_ID)

---

## RDF_ARQUIVOS_ECF_MFD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ARQUIVOS_CMFD | NUMBER(22) | N |  |  |
| 2 | CNPJ_ESTABELECIMENTO | VARCHAR2(20) | Y |  |  |
| 3 | IE_ESTABELECIMENTO | VARCHAR2(20) | Y |  |  |
| 4 | FLG_METODO_COPIA_LE_ECF | NUMBER(1) | Y |  |  |
| 5 | NOM_ARQUIVO | VARCHAR2(255) | Y |  |  |
| 6 | ID_DIRETORIO | NUMBER(15) | Y |  |  |
| 7 | DATA_ULT_MODIFICACAO | DATE | Y |  |  |
| 8 | QTD_BYTES | NUMBER(15) | Y |  |  |
| 9 | SERIE_EQUIPAMENTO | VARCHAR2(20) | Y |  |  |
| 10 | DATA_EMISSAO | DATE | Y |  |  |
| 11 | COD_EQUIPAMENTO | VARCHAR2(6) | Y |  |  |
| 12 | FLG_STATUS | NUMBER(1) | Y |  |  |
| 13 | DATA_INDEXACAO | DATE | Y |  |  |
| 14 | DATA_ENVIO | DATE | Y |  |  |
| 15 | FLG_METODO_COPIA | NUMBER(1) | Y |  |  |
| 16 | SERVIDOR | VARCHAR2(40) | Y |  |  |
| 17 | PORTA | VARCHAR2(4) | Y |  |  |
| 18 | USUARIO | VARCHAR2(40) | Y |  |  |
| 19 | HOST | VARCHAR2(80) | Y |  |  |
| 20 | CAMINHO | VARCHAR2(1000) | Y |  |  |
| 21 | SENHA | VARCHAR2(40) | Y |  |  |
| 22 | TIPO_ARQUIVO | VARCHAR2(3) | Y |  |  |

**PK**: ID_ARQUIVOS_CMFD

**Indexes**:
- IX_RDF_ARQUIVOS_ECF_MFD_01: (ID_DIRETORIO)
- IX_RDF_ARQUIVOS_ECF_MFD_02: (CNPJ_ESTABELECIMENTO)

---

## RDF_COMP_NOTA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_COMP_NOTA | NUMBER(10) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | VLR_COMP | NUMBER(12,2) | Y |  |  |
| 5 | DIAS_COMP | NUMBER(3) | Y |  |  |
| 6 | FLG_DEMAIS | CHAR(1) | Y |  |  |
| 7 | FLG_DATA_SERV | CHAR(1) | Y |  |  |
| 8 | FLG_MES_COM | NUMBER(2) | Y |  |  |

**PK**: ID_COMP_NOTA

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RDF_CONTA_EMAIL
**Comment**: TABELA PARA CONTER OS ENDEREÇOS DE EMAILS QUE RECEBERÃO COMUNICAÇÕES DE ACORDO COM O EVENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_EVENTO_EMAIL | NUMBER(15) | N |  |  |
| 2 | ID_CONTA | NUMBER(15) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | PARA | VARCHAR2(4000) | Y |  |  |
| 6 | COMCOPIA | VARCHAR2(4000) | Y |  |  |
| 7 | FLG_FORMATO | CHAR(1) | Y | 'H' | FORMATO DO EMAIL  H-  MIME HTML / T - TEXTO |
| 8 | FLG_STATUS | VARCHAR2(2) | Y |  |  |

**PK**: ID_CONTA

**FKs**:
- ID_EVENTO_EMAIL → RDF_EVENTOS_EMAIL(ID_EVENTO_EMAIL)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RDF_DASHBOARD

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | STATUS | NUMBER | Y |  |  |
| 2 | STATUSSEFAZCODIGO | NUMBER | Y |  |  |
| 3 | STATUSSEFAZ | VARCHAR2(100) | Y |  |  |
| 4 | CONTROLE | VARCHAR2(100) | Y |  |  |
| 5 | CONTROLECODIGO | NUMBER | Y |  |  |
| 6 | CODEMPRESA | VARCHAR2(3) | Y |  |  |
| 7 | NOMEEMPRESA | VARCHAR2(100) | Y |  |  |
| 8 | CNPJESTABELECIMENTO | VARCHAR2(20) | Y |  |  |
| 9 | NOMEESTABELECIMENTO | VARCHAR2(100) | Y |  |  |
| 10 | USUARIO | VARCHAR2(100) | Y |  |  |
| 11 | DATATRANSMISSAO | DATE | Y |  |  |
| 12 | DATARETORNO | DATE | Y |  |  |
| 13 | NOMEARQUIVO | VARCHAR2(255) | Y |  |  |
| 14 | PROTOCOLO | VARCHAR2(20) | Y |  |  |
| 15 | TIPO | VARCHAR2(20) | Y |  |  |
| 16 | REFERENCIA | VARCHAR2(30) | Y |  |  |
| 17 | PROC_ID | NUMBER(22) | Y |  |  |
| 18 | ID_ARQUIVOS_CMFD | NUMBER(22) | Y |  |  |
| 19 | FLG_ENVIO_CONS | NUMBER(1) | Y |  |  |
| 20 | FLG_STATUS_RECB | NUMBER(1) | Y |  |  |
| 21 | FLG_STATUS_PROCES | NUMBER(1) | Y |  |  |
| 22 | FLG_STATUS | NUMBER(1) | Y |  |  |
| 23 | DATA_EMISSAO | DATE | Y |  |  |
| 24 | ID_ALERTA | NUMBER(22) | Y |  |  |

---

## RDF_DIRETORIOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_DIRETORIO | NUMBER(15) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | DATA_VALIDADE | DATE | N |  |  |
| 5 | FLG_METODO_COPIA_GRAVA_NF | NUMBER(1) | Y |  |  |
| 6 | SERVIDOR_GRAVA_NF | VARCHAR2(40) | Y |  |  |
| 7 | PORTA_GRAVA_NF | VARCHAR2(4) | Y |  | Número da Porta de acesso do host de ftp |
| 8 | USUARIO_GRAVA_NF | VARCHAR2(40) | Y |  | Usuario que será utilizado para conexão ao diretorio solicitado |
| 9 | SENHA_GRAVA_NF | VARCHAR2(40) | Y |  | Senha associada ao usuario para conexão ao diretório solicitado |
| 10 | HOST_GRAVA_NF | VARCHAR2(80) | Y |  | IP da maquina remota caso o metodo de acesso seja ftp |
| 11 | FLG_METODO_COPIA_GRAVA_ECF | NUMBER(1) | Y |  |  |
| 12 | SERVIDOR_GRAVA_ECF | VARCHAR2(40) | Y |  |  |
| 13 | PORTA_GRAVA_ECF | VARCHAR2(4) | Y |  |  |
| 14 | USUARIO_GRAVA_ECF | VARCHAR2(40) | Y |  |  |
| 15 | SENHA_GRAVA_ECF | VARCHAR2(40) | Y |  |  |
| 16 | HOST_GRAVA_ECF | VARCHAR2(80) | Y |  |  |
| 17 | FLG_METODO_COPIA_LE_ECF | NUMBER(1) | Y |  |  |
| 18 | SERVIDOR_LE_ECF | VARCHAR2(40) | Y |  |  |
| 19 | PORTA_LE_ECF | VARCHAR2(4) | Y |  |  |
| 20 | USUARIO_LE_ECF | VARCHAR2(40) | Y |  |  |
| 21 | SENHA_LE_ECF | VARCHAR2(40) | Y |  |  |
| 22 | HOST_LE_ECF | VARCHAR2(80) | Y |  |  |
| 23 | FLG_METODO_COPIA_SUCESS | NUMBER(1) | Y |  |  |
| 24 | SERVIDOR_SUCESS | VARCHAR2(40) | Y |  |  |
| 25 | PORTA_SUCESS | VARCHAR2(4) | Y |  |  |
| 26 | USUARIO_SUCESS | VARCHAR2(40) | Y |  |  |
| 27 | SENHA_SUCESS | VARCHAR2(40) | Y |  |  |
| 28 | HOST_SUCESS | VARCHAR2(80) | Y |  |  |
| 29 | DIRETORIO_GRAVA_NF | VARCHAR2(1000) | Y |  |  |
| 30 | DIRETORIO_GRAVA_ECF | VARCHAR2(1000) | Y |  |  |
| 31 | DIRETORIO_LE_ECF | VARCHAR2(1000) | Y |  |  |
| 32 | DIRETORIO_SUCESS | VARCHAR2(1000) | Y |  |  |
| 33 | SERVIDOR_LE_ECFSMFD | VARCHAR2(40) | Y |  |  |
| 34 | PORTA_LE_ECFSMFD | VARCHAR2(4) | Y |  |  |
| 35 | USUARIO_LE_ECFSMFD | VARCHAR2(40) | Y |  |  |
| 36 | SENHA_LE_ECFSMFD | VARCHAR2(40) | Y |  |  |
| 37 | HOST_LE_ECFSMFD | VARCHAR2(80) | Y |  |  |
| 38 | DIRETORIO_LE_ECFSMFD | VARCHAR2(1000) | Y |  |  |
| 39 | FLG_METODO_COPIA_ECFSMFD | NUMBER(1) | Y |  |  |

**PK**: ID_DIRETORIO, COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

**Indexes**:
- IX_RDF_DIRETORIOS_01: (COD_EMPRESA, COD_ESTAB)

---

## RDF_ENVIA_EMAIL
**Comment**: CONTEM OS E-MAILS ENVIADOS, LOG DE ENVIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ENVIA_EMAIL | NUMBER(20) | N |  |  |
| 2 | ID_EVENTO_EMAIL | NUMBER(15) | Y |  |  |
| 3 | ASSUNTO | VARCHAR2(2000) | Y |  |  |
| 4 | CORPO | BLOB | Y |  |  |
| 5 | DAT_SOLICITACAO | DATE | Y |  |  |
| 6 | DAT_ENTREGA | DATE | Y |  |  |
| 7 | COD_EMPRESA | VARCHAR2(3) | Y |  |  |
| 8 | COD_ESTAB | VARCHAR2(6) | Y |  |  |

**PK**: ID_ENVIA_EMAIL

**FKs**:
- ID_EVENTO_EMAIL → RDF_EVENTOS_EMAIL(ID_EVENTO_EMAIL)

---

## RDF_EVENTOS_EMAIL
**Comment**: TABELA PARA OS EVENTOS MONITORADOS NO SISTEMA DE E-MAIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_EVENTO_EMAIL | NUMBER(15) | N |  | CHAVE PRIMARIA DA TABELA |
| 2 | DESCRICAO | VARCHAR2(200) | N |  | DESCRICAO DO EVENTO |
| 3 | ASSUNTO | VARCHAR2(500) | Y |  | ASSUNTO PADRAO PARA O EMAIL DO EVENTO |
| 4 | CORPO | VARCHAR2(4000) | Y |  | CORPO PADRAO PARA O EMAIL DO EVENTO |

**PK**: ID_EVENTO_EMAIL

---

## RDF_JOB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_JOB | NUMBER(15) | N |  | ID |
| 2 | ID_JOB_AGRUPA | NUMBER(15) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  | CODIGO DA EMPRESA |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  | CODIGO DA EMPRESA |
| 5 | FLG_ECF | NUMBER(1) | Y | 0 | INDICA QUE A CONFIGURAÇÃO É DE ECF 0=NAO USADO 1=USADO |
| 6 | FLG_NOTA | NUMBER(1) | Y | 0 | INDICA QUE A CONFIGURAÇÃO É DE NOTA 0=NAO USADO 1=USADO |
| 7 | FLG_STATUS_JOB | VARCHAR2(1) | Y |  | A = ATIVO ; I = INATIVO |
| 8 | DTA_PROGRAMADA | DATE | N |  |  |
| 9 | HORA_PROGRAMADA | VARCHAR2(5) | N |  |  |
| 10 | DTA_EMISSAO_INI | DATE | N |  |  |
| 11 | DTA_EMISSAO_FIM | DATE | N |  |  |
| 12 | FLG_CONTROLE | VARCHAR2(1) | Y |  | A=ANDAMENTO / F=FINALIZADO /  E = ERRO / S = JOB ESQUEDULADO |
| 13 | DESC_ERRO | VARCHAR2(155) | Y |  | DESCRIÇÃO DO ERRO NO PROCESSAMENTO DO JOB |
| 14 | DTA_INI_EXEC | DATE | Y |  | DATA E HORA DO INICIO DO PROCESSAMENTO |
| 15 | DTA_FIM_EXEC | DATE | Y |  | DATA E HORA DO FIM DA EXECUÇÃO DO JOB |
| 16 | FLG_COMP_NOTA | VARCHAR2(100) | Y |  | INDICA OS VALORES PARA GERAÇÃO DE NOTAS FISCAIS G=SUPERIOR OU IGUAL L=INFERIOR T=TODOS |
| 17 | FLG_TIPO_JOB | VARCHAR2(1) | N |  | E=ENVIO / G=GERAÇAO |
| 18 | IND_CONFLITO | CHAR(1) | Y |  |  |

**PK**: ID_JOB

**Indexes**:
- IX_RDF_JOB_01: (ID_JOB_AGRUPA)

---

## RDF_LOG_ENVIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_RDF_LOG_ENVIO | NUMBER(15) | N |  |  |
| 2 | ID_ARQUIVOS_CMFD | NUMBER(22) | N |  |  |
| 3 | FLG_ENVIO_CONS | NUMBER(1) | Y |  |  |
| 4 | FLG_STATUS_RECB | NUMBER(1) | Y |  |  |
| 5 | DATA_RECEBIMENTO | DATE | Y |  |  |
| 6 | NUM_LOTE | VARCHAR2(7) | Y |  |  |
| 7 | COD_SITU_LOTE | NUMBER(3) | Y |  |  |
| 8 | DESC_SITU_LOTE | VARCHAR2(50) | Y |  |  |
| 9 | COD_ERRO | NUMBER(3) | Y |  |  |
| 10 | DESC_ERRO | VARCHAR2(255) | Y |  |  |
| 11 | PROTOCOLO_SEFAZ | VARCHAR2(20) | Y |  |  |
| 12 | STATUS | VARCHAR2(3) | Y |  |  |
| 13 | ALERTAS | VARCHAR2(50) | Y |  |  |
| 14 | CNPJ | VARCHAR2(18) | Y |  |  |
| 15 | RAZAO_SOCIAL | VARCHAR2(70) | Y |  |  |
| 16 | RESPONSAVEL_ENVIO | VARCHAR2(15) | Y |  |  |
| 17 | TIPO_PROCESSAMENTO | VARCHAR2(50) | Y |  |  |
| 18 | NOME_ARQUIVO | VARCHAR2(50) | Y |  |  |
| 19 | TAMANHO_ARQUIVO_BYTE | NUMBER(6) | Y |  |  |
| 20 | HASH_ARQUIVO | VARCHAR2(50) | Y |  |  |
| 21 | OBSERVACOES | VARCHAR2(200) | Y |  |  |
| 22 | DATA_RECEBIMENTO_SEFAZ | DATE | Y |  |  |
| 23 | DATA_PROCESSAMENTO | DATE | Y |  |  |
| 24 | TEMPO_PROC_SEGD | NUMBER(5) | Y |  |  |
| 25 | DATA_REFERENCIA | DATE | Y |  |  |
| 26 | NUM_CFS_PROC | NUMBER(4) | Y |  |  |
| 27 | VLR_PROC | NUMBER(12,2) | Y |  |  |
| 28 | ID_ALERTA | NUMBER(15) | Y |  |  |
| 29 | DATA_ENVIO | DATE | Y |  |  |
| 30 | FLG_NOTIFICACAO_ERRO | NUMBER(4) | Y |  |  |
| 31 | FLG_TRANSFERIDOS | NUMBER(4) | Y |  |  |

**PK**: ID_RDF_LOG_ENVIO

**FKs**:
- ID_ARQUIVOS_CMFD → RDF_ARQUIVOS_ECF_MFD(ID_ARQUIVOS_CMFD)

**Indexes**:
- IX_RDF_LOG_ENVIO_01: (FLG_ENVIO_CONS, FLG_STATUS_RECB)
- IX_RDF_LOG_ENVIO_02: (PROTOCOLO_SEFAZ)

---

## RDF_LOG_ERRO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LOG_ERRO | NUMBER(15) | N |  |  |
| 2 | COD_ERRO | NUMBER(6) | N |  |  |

**FKs**:
- COD_ERRO → CAT_ERRO(COD_ERRO)

**Indexes**:
- IX_RDF_LOG_ERRO_01: (COD_ERRO)

---

## RDF_LOG_GERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_RDF_LOG_GERACAO | NUMBER(15) | N |  |  |
| 2 | ID_TIPO | NUMBER(10) | N |  |  |
| 3 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 4 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 5 | DATA_FISCAL | DATE | N |  |  |
| 6 | ID_ARQUIVO | NUMBER(15) | Y |  |  |
| 7 | IDENT_DOCTO | NUMBER(12) | N |  |  |
| 8 | MOVTO_E_S | VARCHAR2(1) | N |  |  |
| 9 | NORM_DEV | VARCHAR2(1) | N |  |  |
| 10 | SERIE_DOCFIS | VARCHAR2(3) | Y |  |  |
| 11 | SUB_SERIE_DOCFIS | VARCHAR2(2) | Y |  |  |
| 12 | FLG_STATUS_GERACAO | NUMBER(1) | N |  |  |
| 13 | COD_DOCTO | VARCHAR2(5) | Y |  |  |
| 14 | IDENT_FIS_JUR | NUMBER(12) | N |  |  |
| 15 | COD_FIS_JUR | VARCHAR2(14) | Y |  |  |
| 16 | NUM_DOCFIS | VARCHAR2(12) | N |  |  |
| 17 | DATA_EMISSAO | DATE | Y |  |  |
| 18 | COD_CLASS_DOC_FIS | CHAR(1) | Y |  |  |
| 19 | IDENT_MODELO | NUMBER(12) | Y |  |  |
| 20 | CONTRIB_FINAL | CHAR(1) | Y |  |  |
| 21 | IDENT_CFO | NUMBER(12) | Y |  |  |
| 22 | DATA_GERACAO | DATE | Y |  |  |
| 23 | DATA_ALERTA | DATE | Y |  |  |
| 24 | DATA_RECEBIMENTO | DATE | Y |  |  |
| 25 | ID_LOG_ERRO | NUMBER(15) | Y |  |  |
| 26 | DATA_RETIFICACAO | DATE | Y |  |  |
| 27 | VLR_TOT_NOTA | NUMBER(17,2) | Y |  |  |
| 28 | FLG_FUNCAO_REGISTRO | CHAR(1) | Y |  |  |

**PK**: ID_RDF_LOG_GERACAO

**FKs**:
- ID_ARQUIVO → RDF_ARQGERADOS(ID_ARQUIVO)
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)
- ID_TIPO → RDF_TIPO_ARQUIVO(ID_TIPO)

**Indexes**:
- IX_RDF_LOG_GERACAO_01: (COD_EMPRESA, COD_ESTAB, DATA_FISCAL, MOVTO_E_S, NORM_DEV, IDENT_DOCTO, IDENT_FIS_JUR, NUM_DOCFIS, SERIE_DOCFIS, SUB_SERIE_DOCFIS)
- IX_RDF_LOG_GERACAO_02: (ID_TIPO)
- IX_RDF_LOG_GERACAO_03: (ID_ARQUIVO)

---

## RDF_LOG_GERACAO_CUPOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_LOG_GERACAO_CUPOM | NUMBER | N |  | SEQUENCIAL |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  | CODIGO DA EMPRESA |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  | CODIGO DO ESTABELECIMENTO |
| 4 | IDENT_CAIXA_ECF | NUMBER | N |  | IDENTIFICADOR DO ECF |
| 5 | NUM_CRZ_COO | VARCHAR2(6) | Y |  | CÓDIGO DA REDUÇÃO Z OU DO CUPOM FISCAL |
| 6 | DATA_FISCAL | DATE | N |  | DATA FISCAL DA REDUÇÃO Z OU DATA DA EMISSAO DO CUPOM FISCAL |
| 7 | ID_ARQUIVO | NUMBER | N |  | ID DO ARQUIVO |
| 8 | ID_LOG_ERRO | NUMBER | Y |  | ID DO LOG DE ERRO |
| 9 | DATA_GERACAO | DATE | N | SYSDATE | DATA DA GERAÇÃO |
| 10 | FLG_STATUS_GERACAO | NUMBER | N |  | STATUS DA GERAÇÃO |
| 11 | ID_TIPO | NUMBER | N |  |  |

---

## RDF_MENS_EMAIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_TIPO | NUMBER(10) | N |  |  |
| 2 | ID_TIPO_MENS | NUMBER(1) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(400) | Y |  |  |

**PK**: ID_TIPO, ID_TIPO_MENS

**FKs**:
- ID_TIPO → RDF_TIPO_ARQUIVO(ID_TIPO)

**Indexes**:
- IX_RDF_MENS_EMAIL_01: (ID_TIPO)

---

## RDF_MIDIA_DIGITAL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SEQ_MIDIA | NUMBER(15) | N |  |  |
| 4 | STATUS_GERACAO | NUMBER(15) | N |  |  |
| 5 | DT_GERACAO_ARQUIVO | TIMESTAMP(6) | N |  |  |
| 6 | ARQUIVO | BLOB | Y |  |  |
| 7 | TIPO_GERACAO | NUMBER(15) | N |  |  |
| 8 | TIPO_NF | NUMBER(15) | N |  |  |
| 9 | FLAG_RETIFICADORA | NUMBER(15) | N |  |  |
| 10 | DT_PERIODO_INICIAL | DATE | N |  |  |
| 11 | DT_PERIODO_FINAL | DATE | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, SEQ_MIDIA

---

## RDF_MIDIA_DIGITAL_ECF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ID_EQUIPAMENTO | NUMBER(15) | N |  |  |
| 4 | SEQ_MIDIA | NUMBER(15) | N |  |  |
| 5 | STATUS_GERACAO | NUMBER(15) | N |  |  |
| 6 | DT_GERACAO_ARQUIVO | TIMESTAMP(6) | N |  |  |
| 7 | ARQUIVO | BLOB | Y |  |  |
| 8 | FLAG_RETIFICADORA | NUMBER(15) | N |  |  |
| 9 | MES_ANO_REFERENCIA | VARCHAR2(50) | Y |  |  |
| 10 | TIPO_ORIGEM | NUMBER(15) | Y |  |  |
| 11 | RESPOSTA_SEFAZ | VARCHAR2(50) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, ID_EQUIPAMENTO, SEQ_MIDIA

---

## RDF_MIDIA_DIGITAL_ECF_LOG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | ID_EQUIPAMENTO | NUMBER(15) | N |  |  |
| 4 | SEQ_MIDIA | NUMBER(15) | N |  |  |
| 5 | SEQ_LOG | NUMBER(15) | N |  |  |
| 6 | ID_SEVERIDADE | NUMBER(15) | N |  |  |
| 7 | DESCRICAO | VARCHAR2(1000) | N |  |  |
| 8 | DATA_HORA | TIMESTAMP(6) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, SEQ_MIDIA, ID_EQUIPAMENTO, SEQ_LOG

**FKs**:
- COD_EMPRESA, COD_ESTAB, ID_EQUIPAMENTO, SEQ_MIDIA → RDF_MIDIA_DIGITAL_ECF(COD_EMPRESA, COD_ESTAB, ID_EQUIPAMENTO, SEQ_MIDIA)

---

## RDF_MIDIA_DIGITAL_LOG

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | SEQ_MIDIA | NUMBER(15) | N |  |  |
| 4 | SEQ_LOG | NUMBER(15) | N |  |  |
| 5 | ID_SEVERIDADE | NUMBER(15) | N |  |  |
| 6 | DESCRICAO | VARCHAR2(1000) | N |  |  |
| 7 | DATA_HORA | TIMESTAMP(6) | N |  |  |

**PK**: COD_EMPRESA, COD_ESTAB, SEQ_MIDIA, SEQ_LOG

**FKs**:
- COD_EMPRESA, COD_ESTAB, SEQ_MIDIA → RDF_MIDIA_DIGITAL(COD_EMPRESA, COD_ESTAB, SEQ_MIDIA)

---

## RDF_PARAMETROS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_PARAM | NUMBER | N |  |  |
| 2 | COD_PARAM | VARCHAR2(50) | N |  |  |
| 3 | VAL_PARAM | VARCHAR2(1000) | Y |  |  |

---

## RDF_REGR_ENVIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_ENVIO | NUMBER(12) | N |  |  |
| 2 | FLG_ENVI_TODAS | NUMBER(1) | N |  |  |
| 3 | FLG_DESTINATARIO | CHAR(1) | Y |  |  |

**PK**: ID_ENVIO

---

## RDF_SERV_EMAIL

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 2 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 3 | END_SERVIDOR | VARCHAR2(50) | Y |  |  |
| 4 | MIME_TYPE | NUMBER(1) | Y |  |  |
| 5 | CONTA_EMAIL_ENVIO | VARCHAR2(70) | Y |  |  |
| 6 | CONTA_EMAIL_RECT | VARCHAR2(70) | Y |  |  |

**PK**: COD_EMPRESA, COD_ESTAB

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RDF_TIPO_ARQUIVO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_TIPO | NUMBER(10) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(50) | N |  |  |

**PK**: ID_TIPO

---

## RDF_TRANSF_ARQUIVOS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID | NUMBER(15) | N |  |  |
| 2 | NOME_ARQUIVO | VARCHAR2(100) | N |  |  |
| 3 | DATA_TRANSF | DATE | N |  |  |
| 4 | PATH_ORIGEM | VARCHAR2(100) | Y |  |  |
| 5 | PATH_DESTINO | VARCHAR2(100) | Y |  |  |
| 6 | FLG_TIPO_TRANSF | VARCHAR2(1) | Y |  |  |
| 7 | TIPO_TRANSF | VARCHAR2(3) | Y |  | JOB - ATUALIZAÇÃO COM QUARTZ, APP - ATUALIZAÇÃO VIA APLICAÇÃO |

**PK**: ID

---

## RDF_USUARIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | LOGIN | VARCHAR2(10) | N |  |  |
| 2 | SENHA | VARCHAR2(25) | N |  |  |
| 3 | NOME | VARCHAR2(50) | N |  |  |
| 4 | ULTIMOACESSO | DATE | N |  |  |

**PK**: LOGIN

---

## RDF_WEBSERVICE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_WEBSERVICE | NUMBER(15) | N |  |  |
| 2 | COD_EMPRESA | VARCHAR2(3) | N |  |  |
| 3 | COD_ESTAB | VARCHAR2(6) | N |  |  |
| 4 | END_PROD | VARCHAR2(200) | Y |  |  |
| 5 | END_CONT | VARCHAR2(200) | Y |  |  |
| 6 | USUARIO | VARCHAR2(70) | Y |  |  |
| 7 | SENHA | VARCHAR2(70) | Y |  |  |
| 8 | CATEGORIA_USUARIO | NUMBER(1) | Y |  |  |
| 9 | TIPO_ENVIO | NUMBER(1) | Y |  |  |
| 10 | NAMESPACE | VARCHAR2(255) | Y |  |  |

**PK**: ID_WEBSERVICE

**FKs**:
- COD_EMPRESA, COD_ESTAB → ESTABELECIMENTO(COD_EMPRESA, COD_ESTAB)

---

## RDF_WEBSERVICE_CFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UF | VARCHAR2(2) | N |  |  |
| 2 | END_POINT_WSDL | VARCHAR2(500) | Y |  |  |
| 3 | USUARIO | VARCHAR2(25) | Y |  |  |
| 4 | SENHA | VARCHAR2(25) | Y |  |  |
| 5 | CATEGORIA_USUARIO | NUMBER(15,5) | Y |  |  |

**PK**: UF

---

## RDF_WEBSERVICE_NFE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | UF | VARCHAR2(2) | N |  |  |
| 2 | END_POINT_WSDL | VARCHAR2(500) | Y |  |  |
| 3 | USUARIO | VARCHAR2(25) | Y |  |  |
| 4 | SENHA | VARCHAR2(25) | Y |  |  |
| 5 | CATEGORIA_USUARIO | NUMBER(15,5) | Y |  |  |

**PK**: UF

---

## RDF_WS_ESTADO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_ESTADO | VARCHAR2(2) | N |  |  |
| 2 | END_WS_PRODUCAO | VARCHAR2(4000) | N |  |  |
| 3 | END_NAMESPACE | VARCHAR2(4000) | N |  |  |
| 4 | END_WS_CONTINGENCIA | VARCHAR2(4000) | Y |  |  |

**PK**: COD_ESTADO

---

