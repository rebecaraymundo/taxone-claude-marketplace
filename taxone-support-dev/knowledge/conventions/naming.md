# TAX ONE - Convencoes de Nomenclatura

Convencoes de nomenclatura para todos os tipos de objetos do TAX ONE.
Todos os nomes devem ser em MAIUSCULO no banco Oracle (padrao Oracle).

---

## Regras Gerais

1. **MAIUSCULO** para nomes de objetos Oracle (tabelas, colunas, packages, etc.)
2. **snake_case** separado por underscore
3. **Maximo 30 caracteres** (limite Oracle para identificadores)
4. **Sem acentos** ou caracteres especiais
5. **Prefixo** indica o tipo do objeto
6. **Sufixo** pode indicar modulo ou funcionalidade

---

## Tabelas

### Formato: `TB_{MODULO}_{DESCRICAO}`

| Prefixo de Modulo | Descricao | Exemplo |
|-------------------|-----------|---------|
| `TB_NF_` | Notas Fiscais | `TB_NF_NOTA_FISCAL` |
| `TB_NF_` | Itens de Nota | `TB_NF_ITEM_NOTA` |
| `TB_AP_` | Apuracao | `TB_AP_APURACAO_ICMS` |
| `TB_AP_` | Ajustes de Apuracao | `TB_AP_AJUSTE` |
| `TB_OB_` | Obrigacoes Acessorias | `TB_OB_SPED_FISCAL` |
| `TB_OB_` | Registros SPED | `TB_OB_REGISTRO_SPED` |
| `TB_CD_` | Cadastros | `TB_CD_EMPRESA` |
| `TB_CD_` | Participantes | `TB_CD_PARTICIPANTE` |
| `TB_CD_` | Produtos | `TB_CD_PRODUTO` |
| `TB_IM_` | Importacao | `TB_IM_ARQUIVO_XML` |
| `TB_IM_` | Lote de Importacao | `TB_IM_LOTE` |
| `TB_CL_` | Calculo | `TB_CL_IMPOSTO_CALC` |
| `TB_CL_` | Base de Calculo | `TB_CL_BASE_CALCULO` |
| `TB_RL_` | Relatorios | `TB_RL_RELATORIO` |
| `TB_IN_` | Integracao | `TB_IN_MSG_SEFAZ` |
| `TB_CF_` | Configuracao | `TB_CF_PARAMETRO` |
| `TB_CF_` | Tabelas Auxiliares | `TB_CF_CFOP`, `TB_CF_CST` |
| `TB_LG_` | Log/Auditoria | `TB_LG_LOG_ERRO` |
| `TB_LG_` | Log de Processamento | `TB_LG_PROCESSAMENTO` |

### Tabelas Temporarias

- Formato: `TB_TMP_{DESCRICAO}`
- Exemplo: `TB_TMP_CALCULO_LOTE`, `TB_TMP_IMPORTACAO`

### Tabelas de Historico

- Formato: `TB_HT_{TABELA_ORIGINAL}`
- Exemplo: `TB_HT_NF_NOTA_FISCAL`

---

## Colunas

### Formato: `{PREFIXO}_{DESCRICAO}`

| Prefixo | Tipo de Dado | Exemplo |
|---------|-------------|---------|
| `CD_` | Codigo / Identificador | `CD_EMPRESA`, `CD_NOTA`, `CD_CFOP` |
| `DS_` | Descricao (texto) | `DS_EMPRESA`, `DS_PRODUTO` |
| `DT_` | Data | `DT_EMISSAO`, `DT_COMPETENCIA` |
| `VL_` | Valor monetario | `VL_TOTAL`, `VL_IMPOSTO`, `VL_BASE_CALCULO` |
| `QT_` | Quantidade | `QT_ITENS`, `QT_REGISTROS` |
| `NR_` | Numero | `NR_NOTA`, `NR_SERIE`, `NR_LOTE` |
| `ST_` | Status (1 char) | `ST_NOTA` (A=Ativa, C=Cancelada) |
| `TP_` | Tipo (1-2 chars) | `TP_OPERACAO` (E=Entrada, S=Saida) |
| `FL_` | Flag booleano | `FL_ATIVO` (S/N), `FL_PROCESSADO` |
| `PC_` | Percentual / Aliquota | `PC_ALIQUOTA`, `PC_REDUCAO` |
| `SG_` | Sigla | `SG_UF`, `SG_PAIS` |

### Colunas de Auditoria (padrao em todas as tabelas)

```sql
DT_INCLUSAO    DATE DEFAULT SYSDATE NOT NULL,  -- Data de inclusao
DS_USR_INCLUSAO VARCHAR2(50) NOT NULL,          -- Usuario que incluiu
DT_ALTERACAO   DATE,                            -- Data da ultima alteracao
DS_USR_ALTERACAO VARCHAR2(50)                   -- Usuario que alterou
```

---

## Packages

### Formato: `PKG_{MODULO}_{FUNCIONALIDADE}`

| Exemplo | Descricao |
|---------|-----------|
| `PKG_APURACAO_ICMS` | Apuracao do ICMS |
| `PKG_APURACAO_PIS_COFINS` | Apuracao de PIS/COFINS |
| `PKG_CALCULO_IMPOSTO` | Calculo de impostos |
| `PKG_CALCULO_ST` | Calculo de Substituicao Tributaria |
| `PKG_CADASTRO_NF` | Cadastro de notas fiscais |
| `PKG_IMPORTACAO_XML` | Importacao de arquivos XML |
| `PKG_OBRIGACAO_SPED` | Geracao do SPED Fiscal |
| `PKG_CONSULTA_NF` | Consultas de notas fiscais |
| `PKG_RELATORIO_APURACAO` | Relatorios de apuracao |
| `PKG_INTEGRACAO_SEFAZ` | Integracao com SEFAZ |
| `PKG_UTIL_GERAL` | Utilitarios gerais |
| `PKG_LOG_SISTEMA` | Logging do sistema |

### Arquivos

- Spec: `PKG_{NOME}_SPEC.sql`
- Body: `PKG_{NOME}_BODY.sql`

---

## Procedures

### Formato: `PRC_{ACAO}_{COMPLEMENTO}`

O nome deve descrever a acao executada.

| Prefixo de Acao | Descricao | Exemplo |
|----------------|-----------|---------|
| `PRC_APURAR_` | Apuracao | `PRC_APURAR_ICMS_PERIODO` |
| `PRC_CALCULAR_` | Calculo | `PRC_CALCULAR_IMPOSTO_NF` |
| `PRC_IMPORTAR_` | Importacao | `PRC_IMPORTAR_XML_NFE` |
| `PRC_GERAR_` | Geracao | `PRC_GERAR_SPED_FISCAL` |
| `PRC_VALIDAR_` | Validacao | `PRC_VALIDAR_NOTA_FISCAL` |
| `PRC_PROCESSAR_` | Processamento | `PRC_PROCESSAR_LOTE` |
| `PRC_CANCELAR_` | Cancelamento | `PRC_CANCELAR_NOTA` |
| `PRC_ESTORNAR_` | Estorno | `PRC_ESTORNAR_APURACAO` |
| `PRC_FECHAR_` | Fechamento | `PRC_FECHAR_COMPETENCIA` |
| `PRC_REABRIR_` | Reabertura | `PRC_REABRIR_COMPETENCIA` |
| `PRC_LOG_` | Logging | `PRC_LOG_ERRO` |
| `PRC_ATUALIZAR_` | Atualizacao | `PRC_ATUALIZAR_STATUS` |
| `PRC_EXCLUIR_` | Exclusao | `PRC_EXCLUIR_NOTA` |

---

## Functions

### Formato: `FNC_{CALCULO}_{COMPLEMENTO}`

O nome deve descrever o que retorna.

| Prefixo | Descricao | Exemplo |
|---------|-----------|---------|
| `FNC_CALCULAR_` | Calculo | `FNC_CALCULAR_ICMS` |
| `FNC_OBTER_` | Busca de valor | `FNC_OBTER_ALIQUOTA` |
| `FNC_VALIDAR_` | Validacao (retorna BOOLEAN) | `FNC_VALIDAR_CNPJ` |
| `FNC_FORMATAR_` | Formatacao | `FNC_FORMATAR_CHAVE_NFE` |
| `FNC_CONVERTER_` | Conversao | `FNC_CONVERTER_UF_IBGE` |
| `FNC_VERIFICAR_` | Verificacao | `FNC_VERIFICAR_COMPETENCIA` |
| `FNC_CONSULTAR_` | Consulta (retorna TYPE) | `FNC_CONSULTAR_APURACAO` |
| `FNC_CONTAR_` | Contagem | `FNC_CONTAR_NOTAS_PERIODO` |

---

## Triggers

### Formato: `TRG_{TABELA}_{EVENTO}`

| Evento | Descricao | Exemplo |
|--------|-----------|---------|
| `_BIR` | Before Insert Row | `TRG_NF_NOTA_FISCAL_BIR` |
| `_BUR` | Before Update Row | `TRG_NF_NOTA_FISCAL_BUR` |
| `_BDR` | Before Delete Row | `TRG_NF_NOTA_FISCAL_BDR` |
| `_AIR` | After Insert Row | `TRG_NF_NOTA_FISCAL_AIR` |
| `_AUR` | After Update Row | `TRG_NF_NOTA_FISCAL_AUR` |
| `_ADR` | After Delete Row | `TRG_NF_NOTA_FISCAL_ADR` |
| `_AUD` | Auditoria (insert+update+delete) | `TRG_NF_NOTA_FISCAL_AUD` |

### Uso Tipico

```sql
-- Trigger de auditoria (populacao automatica de campos)
CREATE OR REPLACE TRIGGER TRG_NF_NOTA_FISCAL_BIR
BEFORE INSERT ON TB_NF_NOTA_FISCAL
FOR EACH ROW
BEGIN
  :NEW.DT_INCLUSAO := SYSDATE;
  :NEW.DS_USR_INCLUSAO := USER;
END;
/

-- Trigger de auditoria em update
CREATE OR REPLACE TRIGGER TRG_NF_NOTA_FISCAL_BUR
BEFORE UPDATE ON TB_NF_NOTA_FISCAL
FOR EACH ROW
BEGIN
  :NEW.DT_ALTERACAO := SYSDATE;
  :NEW.DS_USR_ALTERACAO := USER;
END;
/
```

---

## Views

### Formato: `VW_{DESCRICAO}`

| Exemplo | Descricao |
|---------|-----------|
| `VW_NOTAS_FISCAIS` | Consulta consolidada de notas fiscais |
| `VW_APURACAO_ICMS_RESUMO` | Resumo da apuracao de ICMS |
| `VW_ITENS_NOTA_IMPOSTO` | Itens de nota com impostos calculados |
| `VW_PARTICIPANTES_ATIVOS` | Participantes com status ativo |
| `VW_SPED_REGISTRO_C100` | Dados formatados para registro C100 do SPED |
| `VW_OBRIGACOES_PENDENTES` | Obrigacoes acessorias pendentes de geracao |

---

## Materialized Views

### Formato: `MV_{DESCRICAO}`

| Exemplo | Descricao |
|---------|-----------|
| `MV_APURACAO_RESUMO` | Cache de apuracoes consolidadas |
| `MV_NF_TOTAIS_PERIODO` | Totais de notas por periodo |
| `MV_IMPOSTO_CONSOLIDADO` | Impostos consolidados por empresa/periodo |

---

## Indices

### Formato: `IDX_{TABELA}_{COLUNAS}`

- Abreviar nomes de tabela e coluna quando necessario (limite 30 chars)
- Indices unicos: prefixo `UDX_`
- Indices bitmap: prefixo `BDX_`

| Exemplo | Descricao |
|---------|-----------|
| `IDX_NF_EMPRESA_DT` | Indice em (CD_EMPRESA, DT_EMISSAO) |
| `IDX_NF_CHAVE_NFE` | Indice na chave da NFe |
| `UDX_NF_CHAVE_UNICA` | Indice unico de constraint |
| `BDX_NF_STATUS` | Indice bitmap no status da nota |
| `IDX_IT_NOTA_CFOP` | Indice em item_nota por CFOP |

---

## Sequences

### Formato: `SEQ_{TABELA}` ou `SEQ_{DESCRICAO}`

| Exemplo | Descricao |
|---------|-----------|
| `SEQ_NF_NOTA_FISCAL` | Sequence para PK de notas fiscais |
| `SEQ_LG_LOG_ERRO` | Sequence para PK de log de erros |
| `SEQ_IM_LOTE` | Sequence para lotes de importacao |

---

## Constraints

### Formato: `{TIPO}_{TABELA}_{DESCRICAO}`

| Tipo | Prefixo | Exemplo |
|------|---------|---------|
| Primary Key | `PK_` | `PK_NF_NOTA_FISCAL` |
| Foreign Key | `FK_` | `FK_NF_ITEM_NOTA` |
| Unique | `UK_` | `UK_NF_CHAVE_NFE` |
| Check | `CK_` | `CK_NF_STATUS` |

---

## Synonyms

### Formato: `SYN_{OBJETO}`

- Usar quando objetos de outro schema precisam ser acessados sem prefixo de schema

---

## PowerBuilder

### Windows

- Formato: `w_{descricao}` (minusculo)
- Exemplo: `w_cadastro_nf`, `w_consulta_apuracao`, `w_importacao_xml`

### DataWindows

- Formato: `dw_{descricao}` (minusculo)
- Exemplo: `dw_notas_fiscais`, `dw_itens_nota`, `dw_apuracao_icms`

### User Objects

- Visual: `uo_{descricao}`
- Nao-visual: `nvo_{descricao}`
- Exemplo: `uo_toolbar_fiscal`, `nvo_validacao_fiscal`

### Funcoes Globais

- Formato: `gf_{descricao}`
- Exemplo: `gf_formatar_cnpj`, `gf_validar_data`

---

## Java

### Classes

- **DAO:** `{Entidade}DAO` - `NotaFiscalDAO`, `ApuracaoDAO`
- **Service:** `{Funcionalidade}Service` - `ApuracaoService`, `ImportacaoService`
- **Model/Entity:** `{Entidade}` - `NotaFiscal`, `ItemNota`, `Empresa`
- **Exception:** `{Contexto}Exception` - `ApuracaoException`, `ImportacaoException`
- **Util:** `{Contexto}Utils` - `FiscalUtils`, `DateUtils`

### Pacotes Java

- `com.thomsonreuters.taxone.dao`
- `com.thomsonreuters.taxone.service`
- `com.thomsonreuters.taxone.model`
- `com.thomsonreuters.taxone.exception`
- `com.thomsonreuters.taxone.util`
- `com.thomsonreuters.taxone.integration`

---

## Resumo Rapido

| Objeto | Formato | Exemplo |
|--------|---------|---------|
| Tabela | `TB_{MOD}_{DESC}` | `TB_NF_NOTA_FISCAL` |
| View | `VW_{DESC}` | `VW_NOTAS_FISCAIS` |
| Mat. View | `MV_{DESC}` | `MV_APURACAO_RESUMO` |
| Package | `PKG_{MOD}_{FUNC}` | `PKG_APURACAO_ICMS` |
| Procedure | `PRC_{ACAO}_{COMP}` | `PRC_APURAR_ICMS_PERIODO` |
| Function | `FNC_{CALC}_{COMP}` | `FNC_CALCULAR_ICMS` |
| Trigger | `TRG_{TAB}_{EVT}` | `TRG_NF_NOTA_FISCAL_BIR` |
| Indice | `IDX_{TAB}_{COLS}` | `IDX_NF_EMPRESA_DT` |
| Sequence | `SEQ_{TAB}` | `SEQ_NF_NOTA_FISCAL` |
| PK | `PK_{TAB}` | `PK_NF_NOTA_FISCAL` |
| FK | `FK_{TAB}_{DESC}` | `FK_NF_ITEM_NOTA` |
| UK | `UK_{TAB}_{DESC}` | `UK_NF_CHAVE_NFE` |
