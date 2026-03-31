# SPED ECD - Escrituracao Contabil Digital

Modulo responsavel pela geracao do meio magnetico da ECD (Escrituracao Contabil Digital)
do SPED (Sistema Publico de Escrituracao Digital). Gera arquivo texto com blocos de
registros conforme layout definido pela Receita Federal (Manual de Orientacao do Leiaute).

---

## Visao Geral

A ECD abrange livros contabeis digitais (Diario, Razao, Balancetes, Demonstracoes) que
as empresas devem transmitir ao SPED. O TAX ONE gera o arquivo completo a partir dos
lancamentos contabeis importados na base de dados.

**Fluxo principal:**
1. Lancamentos contabeis importados para X01_CONTABIL
2. Plano de contas em X2002_PLANO_CONTAS, centros de custo em X2003_CENTRO_CUSTO
3. Package SAF_SPED_CONTABIL_FPROC processa lancamentos e gera registros I*
4. Package SAF_SPED_CONTABIL_GRAVA formata e escreve cada registro no arquivo
5. Arquivo validado pelo PVA (Programa Validador e Assinador) da Receita Federal

---

## Arquivos e Packages Principais

### Packages PL/SQL

| Package | Funcao |
|---------|--------|
| `SAF_SPED_CONTABIL_FPROC` | Package principal — orquestra toda a geracao do meio magnetico ECD. ~14.400 linhas. Contem cursores, loops de processamento, acumulacao em work tables e chamadas ao GRAVA |
| `SAF_SPED_CONTABIL_GRAVA` | Gravacao dos registros individuais no arquivo. Procedures: reg_i001, reg_i010, ..., reg_i350, reg_i355, ..., reg_i990. Cada procedure formata uma linha do arquivo |

### Localizacao no Repo

```
artifacts/sp/msaf/SPED/ECD/
├── SAF_SPED_CONTABIL_FPROC.pck    (~14.400 linhas, ISO-8859-1, CRLF)
└── SAF_SPED_CONTABIL_GRAVA.pck
```

---

## Blocos e Registros da ECD

### Bloco I - Lancamentos Contabeis

| Registro | Descricao | Procedure FPROC | Procedure GRAVA |
|----------|-----------|-----------------|-----------------|
| I001 | Abertura Bloco I | - | reg_i001 |
| I010 | Identificacao da Entidade | - | reg_i010 |
| I020 | Campos Adicionais | - | reg_i020 |
| I030 | Termo Abertura | - | reg_i030 |
| I050 | Plano de Contas | - | reg_i050 |
| I051 | Plano Contas Referencial | - | reg_i051 |
| I052 | Indicacao Centros de Custo | - | reg_i052 |
| I075 | Tabela Historico Padronizado | - | reg_i075 |
| I100 | Centro de Custos | - | reg_i100 |
| I150 | Saldos Periodicos (Diario/Razao) | - | reg_i150 |
| I155 | Detalhe dos Saldos (mensal) | - | reg_i155 |
| **I200** | **Lancamento Contabil** | `reg_i200_i250` | reg_i200 |
| **I250** | **Partidas do Lancamento** | `reg_i200_i250` | reg_i250 |
| I300 | Demonstracoes Contabeis (Balanco) | `reg_i300_i310_i350_i355` | reg_i300 |
| I310 | Demonstracoes (subcontas) | `reg_i300_i310_i350_i355` | reg_i310 |
| **I350** | **Saldo Contas Resultado Antes Encerramento** | `reg_i300_i310_i350_i355` | reg_i350 |
| **I355** | **Detalhes dos Saldos (encerramento)** | `reg_i300_i310_i350_i355` | reg_i355 |
| I990 | Encerramento Bloco I | - | reg_i990 |

### Bloco J - Demonstracoes

| Registro | Descricao |
|----------|-----------|
| J150 | Demonstracao do Resultado do Exercicio |
| J210 | DLPA |
| J215 | DMPL |

---

## Fluxo de Dados Detalhado

### Geracao I200/I250 (Lancamentos)

```
X01_CONTABIL (lancamentos)
    ↓ opencursor (ORDER BY determinista)
reg_i200_i250
    ├── Loop EXTERNO: cada lancamento (num_lancamento)
    │   ├── Verifica IND_SITUACAO conta (X2002_PLANO_CONTAS)
    │   ├── Loop INTERNO: cada partida do lancamento
    │   │   ├── Verifica IND_SITUACAO (se inativa → GOTO skip_partida)
    │   │   ├── grava_tmp_sped_i310_i355 (acumula na work table)
    │   │   │   └── Se TIPO_LANCTO='E' e IND_NATUREZA IN ('3','4','8')
    │   │   │       → seta vlr_encerramento
    │   │   └── flush_tmp_sped_i310_i355 (MERGE bulk periodico)
    │   └── reg_i200 + reg_i250 (grava no arquivo)
    └── Proximo lancamento
```

### Geracao I350/I355 (Saldos Antes Encerramento)

```
SPED_I310_I355_WORK (populada por reg_i200_i250)
    ↓ cursor c_i300_350 (ORDER BY Data_Lancto, Cod_Conta, Cod_Custo)
reg_i300_i310_i350_i355
    ├── Para cada (data, conta, custo):
    │   ├── SUM(vlr_encerramento) → se <> 0 → ind_encer_w = 'S'
    │   ├── Se ind_encer_w = 'S':
    │   │   ├── reg_i350 (saldo antes encerramento)
    │   │   └── cursor c_i355_safx (X169_SALDO_ANTES_ENC)
    │   │       └── reg_i355 (detalhe saldo)
    │   ├── reg_i300 (demonstracao)
    │   └── reg_i310 (subcontas)
    └── Proximo grupo
```

### Pre-carregamento BP/DRE (cursor c_Encerr)

```
SPED_I310_I355_WORK
    ↓ cursor c_Encerr (ORDER BY Data_Lancto, Cod_Conta, ...)
Grava_Tmp_Sped_Contas_Custo
    → Popula dados para J150 (Demonstracao Resultado)
```

---

## Tabelas Principais

| Tabela | Tipo | Descricao |
|--------|------|-----------|
| `X01_CONTABIL` | Definitiva | Lancamentos contabeis (fonte principal) |
| `X2002_PLANO_CONTAS` | Definitiva | Plano de contas com IND_SITUACAO (A=ativa) |
| `X2003_CENTRO_CUSTO` | Definitiva | Centros de custo |
| `X169_SALDO_ANTES_ENC` | Definitiva | Saldos antes do encerramento |
| `X232_SALDO_ANTES_FUNC` | Definitiva | Saldos em moeda funcional |
| `X02_SALDOS` | Definitiva | Saldos contabeis gerais |
| `X80_SALDOS_CCUSTO` | Definitiva | Saldos por centro de custo |
| `SPED_I310_I355_WORK` | Work table | Dados agregados de lancamentos para I310/I350/I355 |
| `SPED_I050_WORK` | Work table | Plano de contas processado |

### Indices Relevantes

| Indice | Tabela | Colunas |
|--------|--------|---------|
| `IDX_SPED_I310_I355_WORK_PROC` | SPED_I310_I355_WORK | PROC_ID, DATA_LANCTO, COD_CONTA, GRUPO_CONTA, COD_CUSTO, GRUPO_CUSTO |
| `UK_SPED_I310_I355_WORK` | SPED_I310_I355_WORK | Mesmas colunas (unique) |
| `IX_X169_SALDO_ANTES_ENC` | X169_SALDO_ANTES_ENC | COD_EMPRESA, COD_ESTAB, IDENT_CONTA, IDENT_CUSTO, DATA_SALDO |

---

## Bugs Conhecidos e Solucoes

| WI | Sintoma | Causa Raiz | Fix |
|----|---------|------------|-----|
| #1058225 | I200/I250 nao gerados | RAISE Prox_Lancto_w descarta lancamento inteiro quando partida tem conta inativa | GOTO skip_partida |
| #1027128 | I350/I355 nao gerados em alguns dias | Mesmo RAISE + cursor c_Encerr sem ORDER BY | Cherry-pick #1058225 + ORDER BY no c_Encerr |
| #1053380 | Balancete ECD saldo anterior | Saldo anterior calculado incorretamente | (ver solution) |

---

## Pontos de Atencao

1. **Package muito grande**: SAF_SPED_CONTABIL_FPROC tem ~14.400 linhas. Qualquer alteracao
   deve ser minima e pontual. Usar Python binary replacement (ISO-8859-1 + CRLF).

2. **RAISE vs GOTO em loops**: RAISE Prox_Lancto_w propaga para handler do loop externo.
   Para skip de partida (loop interno), usar GOTO com label.

3. **ORDER BY obrigatorio**: Todos os cursores que leem de work tables (SPED_I310_I355_WORK)
   devem ter ORDER BY explicito. O Oracle nao garante ordem sem ORDER BY.

4. **Falha silenciosa**: A ausencia de I350/I355 nao gera excecao — o arquivo ECD e gerado
   "com sucesso" mas com dados incompletos. Nao ha log ou monitoring para detectar.

5. **IND_NATUREZA para encerramento**: Apenas contas com IND_NATUREZA IN ('3','4','8')
   (contas de resultado) participam do encerramento. Contas de ativo/passivo (1,2) nao.

6. **Servico Java**: `braccountingspedecdmessageprocessor` (Kafka consumer) orquestra a
   geracao via mensagens. Erros no PL/SQL podem ou nao ser propagados para o servico.

7. **Datadog**: Nenhum monitor cobre conteudo dos registros I350/I355. Recomendado criar
   alerta para deteccao de geracoes com bloco I350 vazio em clientes com encerramento.
