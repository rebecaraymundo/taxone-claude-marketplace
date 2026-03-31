# Glossario de Colunas Recorrentes

Colunas que aparecem em 20+ tabelas do schema TAX ONE.

**Total**: 380 colunas recorrentes

## Indice por Categoria

- **Chaves de Identificacao** (15 colunas)
- **Documento Fiscal** (20 colunas)
- **Valores Fiscais** (17 colunas)
- **Controle/Processo** (13 colunas)
- **Apuracao** (9 colunas)
- **Cadastros** (25 colunas)

---

## Chaves de Identificacao

| Coluna | Freq | Tipo | Descricao |
|--------|------|------|-----------|
| COD_EMPRESA | 2500 | VARCHAR2(3) | Codigo da empresa. PK de quase todas as tabelas transacionais. |
| COD_ESTAB | 2395 | VARCHAR2(6) | Codigo do estabelecimento (filial/CNPJ). PK junto com COD_EMPRESA. |
| IDENT_FIS_JUR | 411 | NUMBER(12) | ID interno da pessoa fisica/juridica (FK X04_PESSOA_FIS_JUR). |
| COD_FIS_JUR | 315 | VARCHAR2(14) | CNPJ/CPF da pessoa fisica/juridica. |
| IND_FIS_JUR | 286 | CHAR(1) | F=Fisica, J=Juridica. |
| IDENT_ESTADO | 275 | NUMBER(12) | ID interno do estado (UF). |
| COD_ESTADO | 138 | VARCHAR2(2) | Sigla UF (SP, RJ, MG...). |
| COD_MUNICIPIO | 144 | NUMBER(7) | Codigo IBGE do municipio. |
| IDENT_PRODUTO | 171 | NUMBER(12) | ID interno do produto. |
| COD_PRODUTO | 335 | VARCHAR2(60) | Codigo do produto/mercadoria. |
| IND_PRODUTO | 325 | CHAR(1) | Indicador: 1=Mat-prima, 2=Prod acabado, etc. |
| GRUPO_PRODUTO | 146 | VARCHAR2(9) | Grupo do produto. |
| GRUPO_FIS_JUR | 66 | VARCHAR2(9) | Grupo da pessoa fisica/juridica. |
| EMPS_COD | 116 | VARCHAR2(9) | Codigo da empresa (layout legado). |
| FILI_COD | 115 | VARCHAR2(9) | Codigo da filial (layout legado). |

## Documento Fiscal

| Coluna | Freq | Tipo | Descricao |
|--------|------|------|-----------|
| NUM_DOCFIS | 534 | VARCHAR2(12) | Numero do documento fiscal. PK de X07/X08. |
| SERIE_DOCFIS | 567 | VARCHAR2(3) | Serie do documento fiscal. |
| SUB_SERIE_DOCFIS | 504 | VARCHAR2(2) | Sub-serie do documento fiscal. |
| IDENT_DOCTO | 261 | NUMBER(12) | ID interno do documento fiscal. |
| NORM_DEV | 287 | CHAR(1) | N=Normal, D=Devolucao. |
| MOVTO_E_S | 323 | CHAR(1) | Movimento: E=Entrada, S=Saida. |
| COD_CFO | 239 | VARCHAR2(4) | CFOP sem primeiro digito. |
| IDENT_CFO | 106 | NUMBER(12) | ID interno do CFO. |
| COD_DOCTO | 223 | VARCHAR2(5) | Codigo do tipo de documento. |
| COD_MODELO | 115 | VARCHAR2(2) | Modelo docfis (01=NF, 55=NF-e, 57=CT-e, etc.). |
| IDENT_MODELO | 63 | NUMBER(12) | ID interno do modelo de documento. |
| COD_NATUREZA_OP | 119 | VARCHAR2(3) | Codigo da natureza da operacao. |
| GRUPO_NATUREZA_OP | 71 | VARCHAR2(9) | Grupo da natureza da operacao. |
| COD_TIPO_LIVRO | 256 | VARCHAR2(3) | Tipo livro fiscal (001=Entradas, 002=Saidas, etc.). |
| DATA_FISCAL | 373 | DATE | Data fiscal do documento (competencia). |
| DATA_EMISSAO | 178 | DATE | Data de emissao do documento. |
| NUM_ITEM | 219 | NUMBER(5) | Numero do item na NF. |
| NUM_DOCFIS_REF | 51 | VARCHAR2(12) | Numero docfis referenciado (C176). |
| SERIE_DOCFIS_REF | 51 | VARCHAR2(3) | Serie docfis referenciada (C176). |
| DISCRI_ITEM | 98 | VARCHAR2(76) | Discriminacao/descricao do item. |

## Valores Fiscais

| Coluna | Freq | Tipo | Descricao |
|--------|------|------|-----------|
| VLR_ICMS | 190 | NUMBER | Valor do ICMS. |
| VLR_BASE_ICMS | 103 | NUMBER(17,2) | Base de calculo do ICMS. |
| VLR_PIS | 92 | NUMBER(17,2) | Valor do PIS. |
| VLR_COFINS | 90 | NUMBER(17,2) | Valor da COFINS. |
| VLR_TOT_NOTA | 92 | NUMBER(17,2) | Valor total da nota fiscal. |
| VLR_CONTABIL | 95 | NUMBER | Valor contabil do documento/item. |
| VLR_BASE_PIS | 70 | NUMBER(17,2) | Base de calculo do PIS. |
| VLR_BASE_COFINS | 65 | NUMBER(17,2) | Base de calculo da COFINS. |
| VLR_IPI | 71 | VARCHAR2(255) | Valor do IPI. |
| VLR_BASE | 73 | NUMBER(17,2) | Base de calculo generica. |
| VLR_UNIT | 76 | NUMBER(18,6) | Valor unitario. |
| VLR_DESCONTO | 52 | NUMBER(17,2) | Valor do desconto. |
| VLR_ALIQ_PIS | 78 | NUMBER(7,4) | Aliquota do PIS. |
| VLR_ALIQ_COFINS | 77 | NUMBER(7,4) | Aliquota da COFINS. |
| VLR_OUTRAS | 49 | NUMBER | Valor de outras despesas. |
| VLR_TRIBUTO | 54 | NUMBER(17,2) | Valor do tributo. |
| QUANTIDADE | 124 | NUMBER | Quantidade do item. |

## Controle/Processo

| Coluna | Freq | Tipo | Descricao |
|--------|------|------|-----------|
| NUM_PROCESSO | 1057 | NUMBER(12) | Numero do processo de execucao (job). Liga com LOG_PROCESSO. |
| NRO_PROCESSO | 71 | NUMBER(12) | Numero do processo (variante NUM_PROCESSO). |
| PROC_ID | 180 | NUMBER | ID do processo (auditoria/controle). |
| NUM_LOTE | 454 | NUMBER(12) | Numero do lote de importacao/processamento. |
| PST_ID | 451 | NUMBER | ID do PostingService (integracao). Presente em todas SAFXnn. |
| EXEC_ID | 51 | NUMBER(20) | ID da execucao. |
| USUARIO | 598 | VARCHAR2(40) | Codigo do usuario que executou a operacao. |
| COD_USUARIO | 54 | VARCHAR2(100) | Codigo do usuario (alias USUARIO). |
| DAT_GRAVACAO | 493 | DATE | Data/hora da ultima gravacao do registro. |
| IND_GRAVACAO | 534 | CHAR(1) | Indicador: C=Calculado, D=Digitado, I=Importado. |
| IND_DIG_CALC | 313 | NUMBER | 1=Digitado, 2=Gerado/Calculado, 3=Alterado apos gerado. |
| MASC_ARQUIVO | 95 | VARCHAR2(4) | Mascara do arquivo de interface. |
| COD_MODULO | 66 | VARCHAR2(8) | Modulo do sistema (EST, EFD, EPC, etc.). |

## Apuracao

| Coluna | Freq | Tipo | Descricao |
|--------|------|------|-----------|
| DAT_APURACAO | 398 | DATE | Data de apuracao do imposto/obrigacao. |
| ANO_APURACAO | 89 | NUMBER(4) | Ano de apuracao. |
| MES_APURACAO | 85 | NUMBER(2) | Mes de apuracao. |
| ANO_REF | 52 | NUMBER(4) | Ano de referencia. |
| DATA_INI | 83 | DATE | Data inicial do periodo. |
| DATA_FIM | 79 | DATE | Data final do periodo. |
| DATA_MOVTO | 108 | DATE | Data do movimento. |
| COD_OPER_APUR | 58 | VARCHAR2(5) | Cod operacao apuracao (002=Outros Deb, 006=Outros Cred). |
| IND_DEB_CRE | 51 | CHAR(1) | D=Debito, C=Credito. |

## Cadastros

| Coluna | Freq | Tipo | Descricao |
|--------|------|------|-----------|
| COD_CONTA | 142 | VARCHAR2(70) | Codigo da conta contabil. |
| IDENT_CONTA | 137 | NUMBER(12) | ID interno da conta contabil. |
| COD_NBM | 79 | VARCHAR2(10) | Codigo NCM/NBM do produto. |
| IDENT_NBM | 50 | NUMBER(12) | ID interno do NCM/NBM. |
| COD_MEDIDA | 112 | VARCHAR2(8) | Codigo da unidade de medida. |
| IDENT_MEDIDA | 71 | NUMBER(12) | ID interno da unidade de medida. |
| COD_CUSTO | 74 | VARCHAR2(50) | Codigo do centro de custo. |
| IDENT_CUSTO | 60 | NUMBER(12) | ID interno do centro de custo. |
| COD_SERVICO | 69 | VARCHAR2(4) | Codigo do servico (ISS). |
| COD_OPERACAO | 73 | VARCHAR2(6) | Codigo da operacao. |
| COD_TRIBUTO | 70 | VARCHAR2(2) | Codigo do tributo. |
| COD_RECEITA | 67 | VARCHAR2(800) | Codigo da receita (DARF). |
| COD_OBSERVACAO | 53 | VARCHAR2(8) | Codigo da observacao fiscal. |
| IDENT_OBSERVACAO | 68 | NUMBER(12) | ID interno da observacao. |
| COD_RESPONSAVEL | 48 | VARCHAR2(2) | Codigo do responsavel. |
| COD_PARAM | 53 | NUMBER(3) | Codigo do parametro de lancamento. |
| COD_BEM | 59 | VARCHAR2(60) | Codigo do bem (CIAP). |
| COD_INDICE | 51 | VARCHAR2(10) | Codigo do indice. |
| COD_AMPARO_LEGAL | 55 | VARCHAR2(10) | Codigo do amparo legal. |
| COD_UND_PADRAO | 60 | VARCHAR2(8) | Codigo da unidade padrao. |
| INSC_ESTADUAL | 213 | VARCHAR2(14) | Inscricao estadual do estabelecimento. |
| DESCRICAO | 287 | VARCHAR2(57) | Descricao textual do registro. |
| OBSERVACAO | 77 | VARCHAR2(255) | Campo de observacao textual. |
| SITUACAO | 65 | CHAR(1) | Situacao do registro. |
| VALID_INICIAL | 50 | DATE | Data inicial de validade. |

## Outras Colunas Frequentes

| Coluna | Freq | Tipo | Comment Oracle |
|--------|------|------|---------------|
| DAT_FISCAL | 59 | DATE |  |
| NUM_PROC | 48 | VARCHAR2(24) | Número do Processo vinculado ao lançamento contábil. |
| GRUPO_CONTA | 48 | VARCHAR2(9) |  |
| VLR_ALIQ_ICMS | 48 | NUMBER(7,4) |  |
| COD_CLASSE | 47 | VARCHAR2(3) |  |
| MES_REF | 46 | VARCHAR2(6) |  |
| CPF_CGC | 45 | VARCHAR2(14) |  |
| ARQUIVAMENTO | 45 | VARCHAR2(50) |  |
| SEQUENCIAL | 45 | NUMBER(3) |  |
| STATUS | 44 | VARCHAR2(30) |  |
| VLR_TOT | 44 | NUMBER(17,2) |  |
| NUM_DISCRIMINACAO | 44 | NUMBER |  |
| NUM_AUTENTIC_NFE | 44 | VARCHAR2(80) |  |
| IND_STATUS | 43 | CHAR(1) |  |
| IDENT_NATUREZA_OP | 43 | NUMBER(12) |  |
| USERNAME | 42 | VARCHAR2(30) |  |
| VLR_BASE_ICMSS | 42 | NUMBER |  |
| DSC_COMPLEMENTAR | 42 | VARCHAR2(500) |  |
| COD_TRIB_INT | 41 | NUMBER(5) |  |
| DSC_RESERVADO5 | 41 | VARCHAR2(50) |  |
| VLR_ISS | 41 | NUMBER |  |
| DSC_RESERVADO4 | 41 | VARCHAR2(50) |  |
| DAT_VENCTO | 40 | DATE |  |
| ORIGEM_PROC | 40 | CHAR(1) |  |
| CEP | 40 | NUMBER(8) |  |
| ANO_REFERENCIA | 40 | NUMBER(4) |  |
| VLR_CONTAB_ITEM | 40 | NUMBER(17,2) |  |
| VLR_BRUTO | 40 | NUMBER(17,2) |  |
| VLR_OPERACAO | 40 | NUMBER(17,2) |  |
| DATA_APURACAO | 39 | DATE |  |
| DSC_RESERVADO6 | 39 | VARCHAR2(50) |  |
| COD_ERRO | 39 | NUMBER(6) |  |
| SUB_SERIE_LIVRO | 39 | VARCHAR2(2) |  |
| SERIE_LIVRO | 39 | CHAR(1) |  |
| DSC_RESERVADO8 | 39 | VARCHAR2(50) |  |
| DSC_RESERVADO7 | 39 | VARCHAR2(50) |  |
| ID_DOCTO_FISCAL | 38 | VARCHAR2(150) |  |
| RAZAO_SOCIAL | 38 | VARCHAR2(100) |  |
| VLR_JUROS | 38 | NUMBER(17,2) |  |
| COD_PAIS | 38 | VARCHAR2(5) |  |
| IND_OPER | 38 | VARCHAR2(1) |  |
| DAT_OPERACAO | 37 | DATE |  |
| DATA_PAGTO | 37 | DATE |  |
| COD_SCP | 37 | VARCHAR2(14) |  |
| IND_DIG_CALCULADO | 37 | CHAR(1) |  |
| COD_EQUIPAMENTO | 37 | VARCHAR2(6) |  |
| IND_E_S | 37 | CHAR(1) |  |
| COD_AJUSTE_ICMS | 37 | VARCHAR2(8) |  |
| VLR_ITEM | 37 | NUMBER(17,2) |  |
| COD_NAT_REC | 37 | NUMBER(3) |  |
