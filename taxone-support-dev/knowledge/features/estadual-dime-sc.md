# Feature: DIME SC - Declaracao do ICMS e do Movimento Economico (Santa Catarina)

## Descricao

A DIME SC e uma obrigacao acessoria estadual de Santa Catarina que consolida informacoes
de ICMS (debitos, creditos, apuracoes) para entrega a SEFAZ-SC.

## Packages Principais

| Package | Arquivo | Funcao |
|---------|---------|--------|
| `EST_DIME_SC_FPROC` | `artifacts/sp/msaf/estadual/dime/EST_DIME_SC_FPROC.pck` | Package principal de geracao da DIME SC. ~6700 linhas. Processa quadros 01-46. |
| `SAF_DIME_SC_DCIP_FPROC` | `artifacts/sp/msaf/estadual/dime/SAF_DIME_SC_DCIP_FPROC.pck` | DCIP (Declaracao de Credito de ICMS Presumido) - complementar a DIME |

## Tabelas Chave

| Tabela | Funcao |
|--------|--------|
| `EST_GIA_INFO` | Informacoes de GIA por classe de lancamento. Alimentada por `SAF_EST_GIA_INFO` (s_oagia.sql) e TFix. Coluna `COD_CLASSE` e VARCHAR2. |
| `EST_SC_DIME_DD_INI` | Dados iniciais da DIME SC (Quadro 14 e outros) |
| `ITEM_APURAC_DISCR` | Itens de apuracao discriminada - usado em cursores REC_04050_05070 |
| `ITEM_APURAC_SUBST` | Itens de apuracao ICMS-ST |

## Estrutura do Package EST_DIME_SC_FPROC

### Tipos
- `TVETOR`: `TABLE OF NUMBER(17, 2) INDEX BY BINARY_INTEGER` — colecao indexada por inteiro usada para mapear classes de lancamento a valores de quadros.

### Colecoes Importantes
- `RG_CLASSE_TP_QUAD_ITEM`: Mapeia COD_CLASSE (numerico) → valor do quadro. Populada por `INS_DEPARA` (linha ~4899).

### Cursores Principais
- `GIA_INFO` (linhas 2157-2163): Busca COD_CLASSE e SUM(VLR_OUTROS) de EST_GIA_INFO
- `REC_04050_05070`: Registros do Quadro 04/05 e 05/07
- `CVLR_Q09_ANT`: Valores anteriores Quadro 09
- `REG_ESPECIAL_VALOR`: Valores de regimes especiais
- `DIME_DINI` (linhas 5951-5999): Dados iniciais (Quadro 14) de EST_SC_DIME_DD_INI

### Quadros Processados
Quadros 01 a 46 da DIME SC, cada um com sua logica de preenchimento.

## Fluxo de Processamento

```
1. Inicializa colecoes via INS_DEPARA (mapeia classe → quadro/item)
2. Busca dados de GIA (cursor GIA_INFO de EST_GIA_INFO)
3. Para cada COD_CLASSE, popula o quadro correspondente via SetV
4. Processa quadros 04/05, 05/07, 09, 11, 14 etc.
5. Gera registros finais da DIME SC
```

## Procedure Geradora de Dados

`SAF_EST_GIA_INFO` em `artifacts/sp/msaf/estadual/uf/s_oagia.sql`:
- Popula EST_GIA_INFO a partir dos dados de apuracao
- Usa MERGE (INSERT/UPDATE) com campos: COD_EMPRESA, COD_ESTAB, DAT_APURACAO, COD_CLASSE, VLR_OUTROS, etc.
- COD_CLASSE e gravado como string numerica valida

## Pontos de Atencao

1. **COD_CLASSE e VARCHAR2 mas usado como indice BINARY_INTEGER** — exige conversao explicita com protecao (ver solucao #1068145)
2. **TFix pode inserir dados sujos** em EST_GIA_INFO — codigo deve ser defensivo
3. **Package e muito grande (~6700 linhas)** — alteracoes requerem cuidado com compilacao
4. **37 arquivos referenciam EST_GIA_INFO** — padroes similares podem existir em GIAs de outros estados
5. **Artigos WebHelp relevantes:**
   - Erro no Log DIME SC impedindo geracao (EST_DIME_SCFPROC.executar)
   - Geracao do Quadro 11 - ICMS-ST
   - Geracao do Quadro 04 - Item 070

## Suite de Teste

Suite SuiteAutomation: `ESTADUAL/CT_DIME_SC.xml` (352 arquivos de comparacao)
