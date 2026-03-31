# Módulo: CAD (Cadastros) - 39 tabelas

## CAD_ALIQ_PRODUTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIPO_ALIQUOTA_PROD | VARCHAR2(1) | N |  |  |
| 2 | GRUPO_PRODUTO_DACON | VARCHAR2(2) | N |  |  |
| 3 | COD_PRODUTO_DACON | VARCHAR2(10) | N |  |  |
| 4 | DAT_VALIDADE | DATE | N |  |  |
| 5 | VLR_ALIQ_PIS | NUMBER(7,4) | Y |  |  |
| 6 | VLR_ALIQ_COFINS | NUMBER(7,4) | Y |  |  |

**PK**: TIPO_ALIQUOTA_PROD, GRUPO_PRODUTO_DACON, COD_PRODUTO_DACON, DAT_VALIDADE

**FKs**:
- TIPO_ALIQUOTA_PROD, GRUPO_PRODUTO_DACON → DAC_GRUPO_PRODUTOS(TIPO_ALIQUOTA_PROD, GRUPO_PRODUTO_DACON)
- COD_PRODUTO_DACON → DAC_PRODUTOS(COD_PRODUTO_DACON)

---

## CAD_BLOCO_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_BLOCO | VARCHAR2(2) | N |  |  |
| 3 | DSC_BLOCO | VARCHAR2(60) | Y |  |  |
| 4 | IND_ORDENACAO | NUMBER(2) | Y |  |  |

**PK**: COD_LAYOUT, COD_BLOCO

**FKs**:
- COD_LAYOUT → CAD_LAYOUT(COD_LAYOUT)

---

## CAD_CAMPO_MSAF
**Comment**: Cadastro dos campos das tabelas do MasterSAF utilizadas pelos Grupos de Relatorios dinamicos.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_TAB_MSAF | NUMBER(12) | N |  |  |
| 2 | ID_CAMPO_MSAF | NUMBER(12) | N |  |  |
| 3 | NOM_CAMPO_BD | VARCHAR2(100) | Y |  |  |
| 4 | NOM_CAMPO_FUNC | VARCHAR2(100) | Y |  |  |
| 5 | DSC_TIPO | VARCHAR2(10) | Y |  | DATE, DECIMAL, NUMBER, VARCHAR: Informacao usada na formatacao dos dados no relatorio. |
| 6 | NUM_TAM | NUMBER(5) | Y |  | Tamanho do campo conforme definido no banco. |
| 7 | NUM_DEC | NUMBER(2) | Y |  | Numero de casas decimais conforme definido no banco, para os campos do tipo DECIMAL. Informacao usada na formatacao dos dados no relatorio. |

**PK**: ID_TAB_MSAF, ID_CAMPO_MSAF

**FKs**:
- ID_TAB_MSAF → CAD_TAB_MSAF(ID_TAB_MSAF)

---

## CAD_CCLASS_NFCOM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CCLASS_NFCOM | VARCHAR2(7) | N |  |  |
| 2 | DSC_CCLASS_NFCOM | VARCHAR2(200) | Y |  |  |

**PK**: COD_CCLASS_NFCOM

---

## CAD_CCLASS_TRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CCLASS_TRIB | VARCHAR2(6) | N |  |  |
| 2 | NOME_CCLASS_TRIB | VARCHAR2(200) | N |  |  |
| 3 | DESC_CCLASS_TRIB | VARCHAR2(1200) | N |  |  |
| 4 | LC_REDACAO | VARCHAR2(1200) | Y |  |  |
| 5 | LC_214_25 | VARCHAR2(50) | Y |  |  |

**PK**: COD_CCLASS_TRIB

---

## CAD_CST_IBS_CBS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CST_IBS_CBS | VARCHAR2(3) | N |  |  |
| 2 | DESCR_IBS_CBS | VARCHAR2(100) | N |  |  |
| 3 | IND_GIBSCBS | VARCHAR2(1) | N |  |  |
| 4 | IND_GIBSCBS_MONO | VARCHAR2(1) | N |  |  |
| 5 | IND_GREDBC | VARCHAR2(1) | N |  |  |
| 6 | IND_GRED | VARCHAR2(1) | N |  |  |
| 7 | IND_GDIF | VARCHAR2(1) | Y |  |  |
| 8 | IND_GTRANSF_CRED | VARCHAR2(1) | Y |  |  |
| 9 | IND_GCRED_PRES_IBS_ZFM | VARCHAR2(1) | N |  |  |
| 10 | IND_GAJUS_CRED | VARCHAR2(1) | N |  |  |

**PK**: COD_CST_IBS_CBS

---

## CAD_CST_IBS_CBS_X_CCLASS_TRIB

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CST_IBS_CBS | VARCHAR2(3) | N |  |  |
| 2 | DESC_CST_IBS_CBS | VARCHAR2(100) | N |  |  |
| 3 | COD_CCLASS_TRIB | VARCHAR2(6) | N |  |  |
| 4 | NOME_CCLASS_TRIB | VARCHAR2(200) | N |  |  |
| 5 | DESC_CCLASS_TRIB | VARCHAR2(1200) | N |  |  |
| 6 | LC_REDACAO | VARCHAR2(1200) | Y |  |  |
| 7 | LC_214_25 | VARCHAR2(50) | Y |  |  |
| 8 | TIPO_ALIQUOTA | VARCHAR2(50) | N |  |  |
| 9 | PERC_RED_IBS | VARCHAR2(5) | N |  |  |
| 10 | PERC_RED_CBS | VARCHAR2(5) | N |  |  |
| 11 | IND_REDUTOR_BC | VARCHAR2(5) | Y |  |  |
| 12 | IND_G_TRIB_REGULAR | VARCHAR2(1) | Y |  |  |
| 13 | IND_G_CRED_PRES_OPER | VARCHAR2(1) | N |  |  |
| 14 | IND_G_MONO_PADRAO | VARCHAR2(1) | N |  |  |
| 15 | IND_G_MONO_RETEN | VARCHAR2(1) | N |  |  |
| 16 | IND_G_MONO_RET | VARCHAR2(1) | N |  |  |
| 17 | IND_G_MONO_DIF | VARCHAR2(1) | N |  |  |
| 18 | IND_G_ESTORNO_CRED | VARCHAR2(1) | N |  |  |
| 19 | CREDITO_PARA | VARCHAR2(500) | Y |  |  |
| 20 | DT_INICIAL | DATE | N |  |  |
| 21 | DT_FIM | DATE | Y |  |  |
| 22 | DT_ATUALIZACAO | DATE | N |  |  |
| 23 | IND_NFE_ABI | VARCHAR2(1) | N |  |  |
| 24 | IND_NFE | VARCHAR2(1) | N |  |  |
| 25 | IND_NF_CE | VARCHAR2(1) | N |  |  |
| 26 | IND_CTE | VARCHAR2(1) | N |  |  |
| 27 | IND_CTE_OS | VARCHAR2(1) | N |  |  |
| 28 | IND_BPE | VARCHAR2(1) | N |  |  |
| 29 | IND_BPE_TA | VARCHAR2(1) | N |  |  |
| 30 | IND_BPE_TM | VARCHAR2(1) | N |  |  |
| 31 | IND_NF3E | VARCHAR2(1) | N |  |  |
| 32 | IND_NFSE | VARCHAR2(1) | N |  |  |
| 33 | IND_NFSE_VIA | VARCHAR2(1) | N |  |  |
| 34 | IND_NFCOM | VARCHAR2(1) | N |  |  |
| 35 | IND_NFAG | VARCHAR2(1) | N |  |  |
| 36 | IND_NFGAS | VARCHAR2(1) | N |  |  |
| 37 | IND_DERE | VARCHAR2(1) | N |  |  |
| 38 | ANEXO | VARCHAR2(2) | Y |  |  |
| 39 | LINK | VARCHAR2(100) | N |  |  |

**Indexes**:
- IU_CAD_CST_IBS_CBS_CCLASS_TRIB (UNIQUE): (COD_CST_IBS_CBS, COD_CCLASS_TRIB, DT_INICIAL, DT_FIM)

---

## CAD_EVENTO_DESIF
**Comment**: Tabela de Eventos Contabeis em Contas de Resultado DESIF - Anexo 1 - TACES 106

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_EVENTO_DESIF | VARCHAR2(3) | N |  |  |
| 2 | DSC_EVENTO_DESIF | VARCHAR2(250) | Y |  |  |
| 3 | IND_TIPO_PARTIDA | VARCHAR2(3) | Y |  |  |

**PK**: COD_EVENTO_DESIF

---

## CAD_FATOR_DACON
**Comment**: Tabela de Cadastro do Proporcionalização de Valores

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | VERSAO | VARCHAR2(30) | N | 'VER. 01.00' |  |
| 2 | NUM_FICHA | VARCHAR2(3) | N |  |  |
| 3 | NUM_LINHA | NUMBER(2) | N |  |  |
| 4 | IND_DET_SEPAR | CHAR(1) | N |  |  |
| 5 | IND_DIVISAO | NUMBER(1) | N |  | 1 - Dividendo; 2 - Divisor |
| 6 | NUM_FICHA_DIVISAO | VARCHAR2(3) | N |  |  |
| 7 | NUM_LINHA_DIVISAO | NUMBER(2) | N |  |  |
| 8 | IND_DET_SEP_DIVISAO | CHAR(1) | N |  |  |

**PK**: VERSAO, NUM_FICHA, NUM_LINHA, IND_DET_SEPAR, IND_DIVISAO, NUM_FICHA_DIVISAO, NUM_LINHA_DIVISAO, IND_DET_SEP_DIVISAO

---

## CAD_FICHA_DACON

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_FICHA | VARCHAR2(3) | N |  |  |
| 2 | DESCRICAO | VARCHAR2(400) | Y |  |  |
| 3 | IND_MERCADO | CHAR(1) | Y | ' ' |  |
| 4 | VERSAO | VARCHAR2(30) | N | 'VER. 01.00' |  |
| 5 | IND_REGIME | VARCHAR2(1) | Y |  |  |
| 6 | TIPO_ALIQUOTA_PROD | CHAR(1) | Y |  |  |
| 7 | TRIBUTO | VARCHAR2(6) | Y |  |  |
| 8 | NUM_FICHA_OLD | VARCHAR2(10) | Y |  |  |
| 9 | IND_SEPARACAO | VARCHAR2(2) | Y |  |  |

**PK**: VERSAO, NUM_FICHA

---

## CAD_GRP_REL
**Comment**: Cadastro dos Grupos de Relatorios dinamicos.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_GRP_REL | NUMBER(12) | N |  |  |
| 2 | DSC_GRP_REL | VARCHAR2(100) | Y |  |  |
| 3 | CLAUSULA_FROM | VARCHAR2(4000) | Y |  | Clausulas FROM do SQL dinamico |
| 4 | CLAUSULA_WHERE | VARCHAR2(4000) | Y |  | Clausula WHERE contendo as juncoes entre as tabelas definidas na clausula FROM. |

**PK**: ID_GRP_REL

---

## CAD_GRP_REL_CAMPO
**Comment**: Relacao dos campos das tabelas do MasterSAF disponiveis por Grupo de Relatorio dinamico

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_GRP_REL | NUMBER(12) | N |  |  |
| 2 | ID_TAB_GRP | NUMBER(12) | N |  |  |
| 3 | ID_CAMPO_GRP | NUMBER(12) | N |  |  |
| 4 | ID_TAB_MSAF | NUMBER(12) | N |  |  |
| 5 | ID_CAMPO_MSAF | NUMBER(12) | N |  |  |
| 6 | NOM_CAMPO_ALIAS | VARCHAR2(100) | Y |  |  |
| 7 | NOM_CAMPO_FUNC | VARCHAR2(100) | Y |  |  |
| 8 | IND_PERMITE_AGRUPAR | CHAR(1) | Y |  |  |
| 9 | IND_PERMITE_TOTALIZAR | CHAR(1) | Y |  |  |
| 10 | IND_SUM_SQL | CHAR(1) | Y |  |  |

**PK**: ID_GRP_REL, ID_TAB_GRP, ID_CAMPO_GRP

**FKs**:
- ID_TAB_MSAF, ID_CAMPO_MSAF → CAD_CAMPO_MSAF(ID_TAB_MSAF, ID_CAMPO_MSAF)
- ID_TAB_MSAF → CAD_TAB_MSAF(ID_TAB_MSAF)
- ID_GRP_REL → CAD_GRP_REL(ID_GRP_REL)
- ID_GRP_REL, ID_TAB_GRP → CAD_GRP_REL_TAB(ID_GRP_REL, ID_TAB_GRP)

---

## CAD_GRP_REL_TAB
**Comment**: Relacao das tabelas do MasterSAF disponiveis por Grupo de Relatorio dinamico. Para uma tabela pode haver varias instancias

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_GRP_REL | NUMBER(12) | N |  |  |
| 2 | ID_TAB_GRP | NUMBER(12) | N |  |  |
| 3 | ID_TAB_MSAF | NUMBER(12) | Y |  |  |
| 4 | NOM_TAB_ALIAS | VARCHAR2(100) | Y |  |  |
| 5 | NOM_TAB_FUNC | VARCHAR2(100) | Y |  |  |

**PK**: ID_GRP_REL, ID_TAB_GRP

**FKs**:
- ID_GRP_REL → CAD_GRP_REL(ID_GRP_REL)
- ID_TAB_MSAF → CAD_TAB_MSAF(ID_TAB_MSAF)

---

## CAD_IMP_REGRA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NOM_TAB_WORK | VARCHAR2(8) | N |  | Nome da tabela SAFX. |
| 2 | NOME_CAMPO | VARCHAR2(30) | N |  | Nome do camop na tabela SAFX. |
| 3 | IND_SOBREPOE | VARCHAR2(1) | Y |  | Indicador de sobreposicao do valor do campo da SAFX com o resultado da execucao da regra. |
| 4 | NUM_ORDEM | NUMBER(4) | Y |  | Numero de ordem de execucao das regras. |
| 5 | DSC_REGRA | VARCHAR2(4000) | Y |  | Conteudo da Regra de preenchimento. |

**PK**: NOM_TAB_WORK, NOME_CAMPO

---

## CAD_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | DSC_LAYOUT | VARCHAR2(100) | Y |  |  |
| 3 | HASH_CODE | VARCHAR2(32) | Y |  |  |
| 4 | IND_ALTERACAO | CHAR(1) | Y | 'S' |  |
| 5 | DATA_ULT_ALT | DATE | Y |  |  |
| 6 | COD_VERSAO | VARCHAR2(6) | Y |  |  |
| 7 | DSC_VERSAO | VARCHAR2(100) | Y |  | Descricao da versao do layout. Atendimento ao ECF. |
| 8 | DATA_VALID_INI | DATE | Y |  | Data de validade inicial da versao do layout. Atendimento ao ECF. |
| 9 | DATA_VALID_FIM | DATE | Y |  | Data de validade final da versao do layout. Atendimento ao ECF. |

**PK**: COD_LAYOUT

---

## CAD_LINHA_DACON

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | NUM_FICHA | VARCHAR2(3) | N |  |  |
| 2 | NUM_LINHA | NUMBER(2) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(400) | Y |  |  |
| 4 | GRUPO | VARCHAR2(100) | Y |  |  |
| 5 | ORDEM | NUMBER | Y |  |  |
| 6 | VERSAO | VARCHAR2(30) | N | 'VER. 01.00' |  |
| 7 | IND_PROPORCIONALIZA | VARCHAR2(1) | Y | 'N' |  |
| 8 | NUM_FICHA_OLD | VARCHAR2(3) | Y |  |  |

**PK**: VERSAO, NUM_FICHA, NUM_LINHA

**FKs**:
- VERSAO, NUM_FICHA → CAD_FICHA_DACON(VERSAO, NUM_FICHA)

---

## CAD_LISTA_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LISTA_MSAF | VARCHAR2(100) | N |  |  |
| 2 | DSC_LISTA_MSAF | VARCHAR2(200) | Y |  |  |

**PK**: COD_LISTA_MSAF

---

## CAD_NAT_REND_COD_RECEITA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | EVENTO | VARCHAR2(6) | N |  |  |
| 2 | COD_NAT_REND | NUMBER(5) | N |  |  |
| 3 | DESCRICAO | VARCHAR2(450) | Y |  |  |
| 4 | IND_TRIB_EXT | VARCHAR2(3) | N |  |  |
| 5 | TRIBUTO | VARCHAR2(10) | N |  |  |
| 6 | IND_CLASSIF_TRIB_85 | VARCHAR2(3) | N |  |  |
| 7 | COD_RECEITA | VARCHAR2(6) | N |  |  |
| 8 | PER_APUR | VARCHAR2(10) | N |  |  |

**PK**: EVENTO, COD_NAT_REND, IND_TRIB_EXT, TRIBUTO, IND_CLASSIF_TRIB_85, COD_RECEITA, PER_APUR

---

## CAD_NAT_SUBCONTAS

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NAT_SUBCONTAS | VARCHAR2(2) | N |  |  |
| 2 | VALID_INICIAL | DATE | N |  |  |
| 3 | DESC_NAT_SUBCONTAS | VARCHAR2(200) | Y |  |  |
| 4 | VALID_FINAL | DATE | Y |  |  |

**PK**: COD_NAT_SUBCONTAS, VALID_INICIAL

---

## CAD_PSERV_DESIF
**Comment**: Tabela de Outros Produtos e Servicos DESIF - Anexo 10  - TACES 105

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_PSERV_DESIF | VARCHAR2(4) | N |  |  |
| 2 | GRUPO_PSERV_DESIF | VARCHAR2(100) | Y |  |  |
| 3 | DSC_PSERV_DESIF | VARCHAR2(200) | Y |  |  |
| 4 | IND_OBRIG_COMPL | VARCHAR2(3) | Y |  |  |

**PK**: COD_PSERV_DESIF

---

## CAD_REG_LAYOUT

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_BLOCO | VARCHAR2(2) | N |  |  |
| 3 | COD_REGISTRO | VARCHAR2(7) | N |  |  |
| 4 | NIVEL_HIERARQ | NUMBER(2) | Y |  |  |
| 5 | DSC_REGISTRO | VARCHAR2(300) | Y |  |  |
| 6 | INF_COMPL | VARCHAR2(4000) | Y |  |  |
| 7 | COD_GRUPO | VARCHAR2(5) | Y |  |  |
| 8 | COD_CATEGORIA | VARCHAR2(30) | Y |  |  |
| 9 | IND_GERACAO | CHAR(1) | Y | 'N' |  |
| 10 | IND_OBRIGATORIO | CHAR(1) | Y | 'N' |  |
| 11 | IND_RELAT_CONF | CHAR(1) | Y | 'N' |  |
| 12 | IND_GERAR_ZERADO | CHAR(1) | Y | 'N' |  |
| 13 | IND_REG_MOVTO | VARCHAR2(1) | Y |  | Informa se o registro é do tipo movimento ou não (notas fiscais, lançamentos, movimentação de estoque etc...). |
| 14 | COD_REG_PAI | VARCHAR2(7) | Y |  |  |

**PK**: COD_LAYOUT, COD_BLOCO, COD_REGISTRO

**FKs**:
- COD_LAYOUT, COD_BLOCO → CAD_BLOCO_LAYOUT(COD_LAYOUT, COD_BLOCO)

---

## CAD_REG_LAYOUT_EFD
**Comment**: Informações de layout específicas do módulo EFD por tipo de apresentação. Informa a obrigatoriedade de geração dos registros.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LAYOUT | VARCHAR2(6) | N |  |  |
| 2 | COD_BLOCO | VARCHAR2(2) | N |  |  |
| 3 | COD_REGISTRO | VARCHAR2(7) | N |  |  |
| 4 | IND_TP_APRESENT | VARCHAR2(1) | N |  | Indica o perfil de apresentação do arquivo fiscal que será seguido pela Empresa, definido pela Receita Federal. |
| 5 | IND_OBRIGACAO | VARCHAR2(2) | Y |  | Define a obrigatoriedade de geração de um registro.(O - Obrigatório; N - Não será gerado; OE - Obrigatório se existir informação) |
| 6 | IND_OBRIG_ENTR | VARCHAR2(2) | Y |  | Define a obrigatoriedade de geração de um registro de movimento na entrada.(O - Obrigatório; N - Não será gerado; OE - Obrigatório se existir informação) |
| 7 | IND_OBRIG_SAIDA | VARCHAR2(2) | Y |  | Define a obrigatoriedade de geração de um registro de movimento na saída.(O - Obrigatório; N - Não será gerado; OE - Obrigatório se existir informação) |

**PK**: COD_LAYOUT, COD_BLOCO, COD_REGISTRO, IND_TP_APRESENT

**FKs**:
- COD_LAYOUT, COD_BLOCO, COD_REGISTRO → CAD_REG_LAYOUT(COD_LAYOUT, COD_BLOCO, COD_REGISTRO)

---

## CAD_RELATORIO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | RELATID | NUMBER | N |  |  |
| 2 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 3 | IND_EMP_ESTAB | CHAR(1) | Y |  |  |

**PK**: RELATID

---

## CAD_RELAT_ITEM

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | RELATID | NUMBER | N |  |  |
| 2 | ITEMID | NUMBER | N |  |  |
| 3 | DESCRICAO | VARCHAR2(100) | Y |  |  |
| 4 | GRUPO | VARCHAR2(100) | Y |  |  |
| 5 | ORDEM | NUMBER | Y |  |  |

**PK**: RELATID, ITEMID

**FKs**:
- RELATID → CAD_RELATORIO(RELATID)

---

## CAD_SEPARACAO_DACON

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IND_SEPARACAO | VARCHAR2(2) | N |  |  |
| 2 | IND_DET_SEPAR | CHAR(1) | N |  |  |
| 3 | TITULO_COLUNA | VARCHAR2(30) | Y |  |  |
| 4 | TIPO_VALOR | CHAR(1) | Y |  |  |
| 5 | REGRA | CHAR(1) | Y |  |  |

**PK**: IND_SEPARACAO, IND_DET_SEPAR

---

## CAD_SPED_CBC_JURISDICAO
**Comment**: Cadastro de CBC País Acordo Jurisdição - TACES33. Fonte de Origem: tabela SPED (Disponibilizada no programa da ECF no diretorio Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas) SPEDECF_LOCAL$SPEDECF_CBC_PAIS_ACORDO. 

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_JURISDICAO | VARCHAR2(2) | N |  |  |
| 2 | DSC_JURISDICAO | VARCHAR2(250) | Y |  |  |
| 3 | DATA_INICIAL | DATE | Y |  |  |
| 4 | DATA_FINAL | DATE | Y |  |  |
| 5 | COD_VERSAO | VARCHAR2(3) | Y |  | Codigo da versao da tabela CBC Pais Acordo Jurisdicao, conforme tabela do Sped.  |

**PK**: COD_JURISDICAO

---

## CAD_SPED_CBC_MOEDA
**Comment**: Cadastro de Moedas SPED - TACES31. Fonte de Origem: tabela SPED (Disponibilizada no programa da ECF no diretorio Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). Tabela: SPEDECF_CBC_MOEDA

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | TIP_MOEDA | VARCHAR2(3) | N |  |  |
| 2 | DSC_MOEDA | VARCHAR2(250) | Y |  |  |
| 3 | DATA_INICIAL | DATE | Y |  |  |
| 4 | DATA_FINAL | DATE | Y |  |  |
| 5 | COD_VERSAO | VARCHAR2(3) | Y |  |  |
| 6 | DSC_PAIS | VARCHAR2(250) | Y |  |  |

**PK**: TIP_MOEDA

---

## CAD_SPED_CNC
**Comment**: Tabela de  Consolidacao de Normas Cambiais (CNC) -TACES32. Fonte de Origem: tabela SPED (Disponibilizada no programa da ECF no diretorio Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas).

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_CNC | VARCHAR2(5) | N |  |  |
| 2 | DSC_CNC | VARCHAR2(250) | Y |  |  |
| 3 | DATA_INICIAL | DATE | Y |  |  |
| 4 | DATA_FINAL | DATE | Y |  |  |
| 5 | COD_VERSAO | VARCHAR2(3) | Y |  | Codigo da versao da tabela CNC, conforme tabela do Sped. |

**PK**: COD_CNC

---

## CAD_SPED_MOEDA
**Comment**: Tabela de Cadastro de Moedas (SPED) - TACES16. Fonte de Origem: tabela SPED (Disponibilizada no programa da ECF no diretorio Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). Tabela: SPEDECF_MOEDA.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MOEDA | VARCHAR2(3) | N |  |  |
| 2 | DSC_MOEDA | VARCHAR2(250) | Y |  |  |
| 3 | DATA_INICIAL | DATE | Y |  |  |
| 4 | DATA_FINAL | DATE | Y |  |  |
| 5 | COD_VERSAO | VARCHAR2(3) | Y |  | Codigo da versao da tabela Moeda, conforme tabela do Sped. |

**PK**: COD_MOEDA

---

## CAD_SPED_NATOPER
**Comment**: Tabela de Cadastro de Natureza de Operação (SPED) - TACES18. Utilizado no Y520 registro do ECF.  Fonte de Origem: tabela SPED (Disponibilizada no programa da ECF no diretorio Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). Tabela: SPEDECF_NATUREZA_OPERACAO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_NAT_OPER | VARCHAR2(5) | N |  |  |
| 2 | DSC_NAT_OPER | VARCHAR2(250) | Y |  |  |
| 3 | DATA_INICIAL | DATE | N |  |  |
| 4 | DATA_FINAL | DATE | Y |  |  |
| 5 | COD_VERSAO | VARCHAR2(3) | Y |  | Codigo da versao conforme tabela do Sped. |
| 6 | DSC_CONTA | VARCHAR2(250) | Y |  |  |
| 7 | COD_ORDEM | VARCHAR2(5) | Y |  |  |

**PK**: COD_NAT_OPER, DATA_INICIAL

---

## CAD_SPED_RECOLH
**Comment**: Tabela de Cadastro de Código de Receita Recolhimento na Fonte (SPED) - TACES19. Utilizado no registro Y570 do ECF Fonte de Origem: tabela SPED (Disponibilizada no programa da ECF no diretorio Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). Tabela: SPEDECF_RETENCAO_FONTE

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_RECOLH | VARCHAR2(4) | N |  |  |
| 2 | DSC_RECOLH | VARCHAR2(250) | Y |  |  |
| 3 | DATA_INICIAL | DATE | Y |  |  |
| 4 | DATA_FINAL | DATE | Y |  |  |
| 5 | COD_VERSAO | VARCHAR2(3) | Y |  | Codigo da versao conforme tabela do Sped. |
| 6 | DSC_BENEFICIO | VARCHAR2(250) | Y |  |  |
| 7 | DSC_ORGAO_PUBLICO | VARCHAR2(3) | Y |  |  |
| 8 | DSC_IRRF | VARCHAR2(3) | Y |  |  |
| 9 | DSC_CSLL | VARCHAR2(3) | Y |  |  |

**PK**: COD_RECOLH

---

## CAD_SPED_TIPATIVO
**Comment**: Tabela de Tipo de Ativo  (SPED) - TACES17 Usado no registro Y590 do ECF. Fonte de Origem: tabela SPED (Disponibilizada no programa da ECF no diretorio Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). Tabela: SPEDECF_ATIVOS_EXTERIOR

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TIP_ATIVO | VARCHAR2(14) | N |  |  |
| 2 | DSC_TIP_ATIVO | VARCHAR2(250) | Y |  |  |
| 3 | DATA_INICIAL | DATE | Y |  |  |
| 4 | DATA_FINAL | DATE | Y |  |  |
| 5 | COD_VERSAO | VARCHAR2(3) | Y |  | Codigo da versao conforme tabela do Sped. |
| 6 | COD_GRUPO | VARCHAR2(3) | Y |  |  |

**PK**: COD_TIP_ATIVO

---

## CAD_SPED_TPDOC
**Comment**: Cadastro de Tipo Documento DEREX - TACES70. Fonte de Origem: tabela SPED (Disponibilizada no programa da ECF no diretorio Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas) Tabela:  SPEDECF_DEREX_DOCUMENTO

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TPDOC | VARCHAR2(2) | N |  |  |
| 2 | DSC_TPDOC | VARCHAR2(250) | Y |  |  |
| 3 | DATA_INICIAL | DATE | Y |  |  |
| 4 | DATA_FINAL | DATE | Y |  |  |
| 5 | COD_VERSAO | VARCHAR2(3) | Y |  | Codigo da versao da tabela Tido de Documento DEREX, conforme tabela do Sped.  |

**PK**: COD_TPDOC

---

## CAD_TAB_MSAF
**Comment**: Cadastro das Tabelas do MasterSAF utilizadas pelos Grupos de Relatorios dinamicos.

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | ID_TAB_MSAF | NUMBER(12) | N |  |  |
| 2 | NOM_TAB_BD | VARCHAR2(100) | Y |  |  |
| 3 | NOM_TAB_FUNC | VARCHAR2(100) | Y |  |  |
| 4 | NOM_SAFX | VARCHAR2(10) | Y |  |  |

**PK**: ID_TAB_MSAF

---

## CAD_TARIFA_DESIF
**Comment**: Tabela de Tarifas Bancarias DESIF - Anexo 9  - TACES 104

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TARIFA_DESIF | VARCHAR2(4) | N |  |  |
| 2 | GRUPO_TARIFA_DESIF | VARCHAR2(100) | Y |  |  |
| 3 | DSC_TARIFA_DESIF | VARCHAR2(200) | Y |  |  |
| 4 | DSC_PERIODICIDADE | VARCHAR2(50) | Y |  |  |

**PK**: COD_TARIFA_DESIF

---

## CAD_TRIBUTACAO_MUNIC

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | IDENT_ESTADO | NUMBER(12) | N |  |  |
| 2 | COD_MUNICIPIO | NUMBER(5) | N |  |  |
| 3 | COD_TRIBUTACAO_MUNIC | VARCHAR2(12) | N |  |  |
| 4 | DSC_TRIBUTACAO_MUNIC | VARCHAR2(250) | Y |  |  |

**PK**: IDENT_ESTADO, COD_MUNICIPIO, COD_TRIBUTACAO_MUNIC

**FKs**:
- IDENT_ESTADO, COD_MUNICIPIO → MUNICIPIO(IDENT_ESTADO, COD_MUNICIPIO)

---

## CAD_TRIB_DESIF
**Comment**: Tabela de Codigos de Tributacao DESIF - Anexo 6

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_TRIB_DESIF | VARCHAR2(15) | N |  |  |
| 2 | DSC_TRIB_DESIF | VARCHAR2(300) | Y |  |  |
| 3 | COD_SERV_L116 | VARCHAR2(5) | Y |  |  |

**PK**: COD_TRIB_DESIF

---

## CAD_TRIB_DESIF_MUNIC
**Comment**: Tabela de Codigos de Tributacao do Municipio DESIF - Anexo 7

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_MUNICIPIO_IBGE | VARCHAR2(7) | N |  |  |
| 2 | COD_TRIB_MUNIC | VARCHAR2(20) | Y |  |  |
| 3 | COD_TRIB_DESIF | VARCHAR2(15) | N |  |  |
| 4 | ALIQ | NUMBER(5,2) | Y |  |  |
| 5 | VALID_INI | DATE | N |  |  |
| 6 | VALID_FIM | DATE | Y |  |  |

**PK**: COD_MUNICIPIO_IBGE, COD_TRIB_DESIF, VALID_INI

---

## CAD_VAL_LISTA_MSAF

| # | Coluna | Tipo | Null | Default | Comment |
|---|--------|------|------|---------|--------|
| 1 | COD_LISTA_MSAF | VARCHAR2(100) | N |  |  |
| 2 | COD_VAL_LISTA | VARCHAR2(100) | N |  |  |
| 3 | DSC_VAL_LISTA | VARCHAR2(200) | Y |  |  |

**PK**: COD_LISTA_MSAF, COD_VAL_LISTA

**FKs**:
- COD_LISTA_MSAF → CAD_LISTA_MSAF(COD_LISTA_MSAF)

---

