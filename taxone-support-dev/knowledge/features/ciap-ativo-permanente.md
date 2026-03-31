# CIAP - Controle de Credito do Ativo Permanente

Modulo estadual responsavel pelo controle de creditos de ICMS sobre bens do ativo
permanente (imobilizado). Implementa os modelos C e D do CIAP conforme legislacao
estadual, gerando aquisicoes a partir de notas fiscais e calculando creditos de
ICMS apropriaveis ao longo de 48 meses.

---

## Visao Geral

O CIAP (Controle de Credito de ICMS do Ativo Permanente) permite que empresas
apropriem creditos de ICMS sobre bens adquiridos para o ativo imobilizado. O
credito e fracionado em 1/48 avos por mes, proporcional as saidas tributadas.

**Fluxo principal:**
1. Notas fiscais de aquisicao de ativo permanente sao identificadas
2. Procedure SAF_CIAP_AQUISICAO gera registros em APT_AQUISICAO
3. Calculo do diferencial de aliquota (DIFAL) quando aplicavel
4. Saldo de creditos e calculado por p_saldcrd.pck
5. Modelos C/D geram o demonstrativo de credito por periodo
6. Dados alimentam SPED EFD Bloco G e relatorios

---

## Arquivos e Packages Principais

### Procedure Central

| Arquivo | Procedure | Funcao |
|---------|-----------|--------|
| `artifacts/sp/msaf/estadual/ufcat/s_apquis.sql` | SAF_CIAP_AQUISICAO | Gerar aquisicoes do CIAP a partir de notas fiscais |

### Packages Downstream (Consumidores)

| Arquivo | Package/Procedure | Funcao |
|---------|-------------------|--------|
| `artifacts/sp/msaf/estadual/ufcat/p_saldcrd.pck` | p_saldcrd | Calculo de saldo de creditos CIAP |
| `artifacts/sp/msaf/estadual/ufcat/p_saldcrd2.pck` | p_saldcrd2 | Calculo de saldo de creditos CIAP (complementar) |
| `artifacts/sp/msaf/estadual/ufcat/s_apmodc.sql` | s_apmodc | Calculo CIAP Modelo C |
| `artifacts/sp/msaf/estadual/ufcat/s_apmodd.sql` | s_apmodd | Calculo CIAP Modelo D |
| `artifacts/sp/msaf/estadual/ufcat/s_apgenf.sql` | s_apgenf | Geracao de documento fiscal CIAP |
| `artifacts/sp/msaf/estadual/ufcat/s_ciapst.sql` | s_ciapst | Status/controle do CIAP |

### Integracoes

| Arquivo | Package | Funcao |
|---------|---------|--------|
| `artifacts/sp/msaf/estadual/ufcat/efd_dic_dados_ciap.pck` | efd_dic_dados_ciap | SPED EFD Bloco G (registros G110, G125, G130, G140) |
| `artifacts/sp/msaf/estadual/ufcat/EST_AP_REL_BEM_COMP_FPROC.pck` | EST_AP_REL_BEM_COMP_FPROC | Relatorio de bens e componentes |

---

## Tabelas e Campos Criticos

### Tabela Principal: APT_AQUISICAO

Armazena as aquisicoes do CIAP geradas a partir de notas fiscais.

**Campos criticos:**
- `VLR_CRED_DIF_ALIQ` -- Valor do credito de diferencial de aliquota (DIFAL)
- Campos de valor base, aliquota interna, aliquota interestadual

### Tabela de Credito por CFO: APT_CRED_CFO_102

Detalhamento do credito DIFAL por Codigo Fiscal de Operacao.

**Campos criticos:**
- `VLR_CRED_ICMS_DF` -- Valor do credito ICMS diferencial

### Tabela de Parametros: APT_ESTAB

Parametros do estabelecimento para o CIAP.

**Campos criticos:**
- `APROPRIA_DIF_ALIQ` -- Flag indicando se o estabelecimento apropria diferencial de aliquota

### Tabela de Parametros Ferramentas: PRT_PAR3_MSAF

Parametros globais de ferramentas do Mastersaf.

**Campos criticos:**
- `IND_BASE_DIF_ALIQ` -- Indicador de base para calculo do diferencial de aliquota

### Tabelas de Input (Notas Fiscais)

| Tabela | Funcao |
|--------|--------|
| `DWT_ITENS_MERC` | Itens de mercadoria (input principal) |
| `DWT_DOCTO_FISCAL` | Documentos fiscais (cabecalho) |

---

## Fluxo de Dados

```
NFs (DWT_DOCTO_FISCAL + DWT_ITENS_MERC)
         |
         v
  SAF_CIAP_AQUISICAO (s_apquis.sql)
   - Identifica itens de ativo permanente
   - Calcula DIFAL (diferencial de aliquota)
   - Trata UFs especiais (MS/FECP, PE/PB, SP SNAC)
         |
         v
  APT_AQUISICAO (VLR_CRED_DIF_ALIQ) + APT_CRED_CFO_102 (VLR_CRED_ICMS_DF)
         |
         +---> p_saldcrd.pck / p_saldcrd2.pck (saldo de credito acumulado)
         |
         +---> s_apmodc.sql (demonstrativo CIAP Modelo C)
         |
         +---> s_apmodd.sql (demonstrativo CIAP Modelo D)
         |
         +---> s_apgenf.sql (geracao documento fiscal de ajuste)
         |
         +---> efd_dic_dados_ciap.pck (SPED EFD Bloco G)
         |
         +---> EST_AP_REL_BEM_COMP_FPROC.pck (relatorio bens/componentes)
```

---

## Parametros de Configuracao

### APT_ESTAB.APROPRIA_DIF_ALIQ
- Controla se o estabelecimento deve apropriar diferencial de aliquota no CIAP
- Quando 'S', o calculo de DIFAL e executado em SAF_CIAP_AQUISICAO

### PRT_PAR3_MSAF.IND_BASE_DIF_ALIQ
- Define a base de calculo para o diferencial de aliquota
- Afeta a formula utilizada em VLR_DIF_ALIQ_W dentro de s_apquis.sql

---

## Patterns e Armadilhas Conhecidas

### ARMADILHA: DIFAL Negativo (WI #1062650)

**Problema:** A formula de calculo do diferencial de aliquota pode produzir valores
negativos quando a aliquota interestadual e maior que a aliquota interna. Isso ocorre
em operacoes interestaduais onde o estado de destino possui aliquota menor.

**Sintoma:** Campo VLR_CRED_DIF_ALIQ em APT_AQUISICAO com valor negativo, causando
distorcao no saldo de creditos e nos demonstrativos CIAP.

**Causa raiz:** A formula de DIFAL usa o pattern "base dupla" (base * aliq_interna - base * aliq_inter)
sem protecao contra resultado negativo. Sao 7 variacoes da variavel VLR_DIF_ALIQ_W
em s_apquis.sql, cada uma atendendo cenarios diferentes:
- Formula padrao
- UF MS com FECP (Fundo de Combate a Pobreza)
- UFs PE/PB com DIF_ALIQ_TRIB_ICMS
- SP para Simples Nacional (SNAC)
- Combinacoes dessas regras

**Solucao:** Aplicar `GREATEST(calculo, 0)` em todas as 7 atribuicoes de VLR_DIF_ALIQ_W.
O DIFAL negativo nao tem sentido fiscal -- quando aliquota interestadual >= interna,
nao ha diferencial a recolher, portanto o valor correto e zero.

```sql
-- ANTES (vulneravel a negativo):
VLR_DIF_ALIQ_W := (base * aliq_interna / 100) - (base * aliq_inter / 100);

-- DEPOIS (protegido):
VLR_DIF_ALIQ_W := GREATEST((base * aliq_interna / 100) - (base * aliq_inter / 100), 0);
```

**Impacto downstream:** Um DIFAL negativo em APT_AQUISICAO propaga-se para:
- p_saldcrd.pck (saldo de credito distorcido)
- s_apmodc/d.sql (demonstrativo com valores incorretos)
- efd_dic_dados_ciap.pck (SPED Bloco G com valores errados)
- Relatorios de bens/componentes

### PATTERN: Protecao de Valores Fiscais com GREATEST/LEAST

Sempre que uma formula fiscal puder produzir valores fora do dominio esperado,
usar GREATEST ou LEAST para limitar o resultado:

```sql
-- Valor que nao pode ser negativo:
valor := GREATEST(calculo, 0);

-- Valor que nao pode exceder a base:
valor := LEAST(calculo, base);

-- Valor entre 0 e base:
valor := GREATEST(LEAST(calculo, base), 0);
```

Este pattern e especialmente importante em formulas de diferencial de aliquota,
credito presumido e outros calculos que envolvem subtracao de aliquotas ou bases.

### PATTERN: UFs com Tratamento Especial no DIFAL

Ao modificar formulas de DIFAL, verificar se existe tratamento diferenciado por UF:
- **MS:** Adiciona FECP (Fundo Estadual de Combate a Pobreza) ao calculo
- **PE / PB:** Usa campo DIF_ALIQ_TRIB_ICMS para base diferenciada
- **SP (SNAC):** Tratamento para contribuintes do Simples Nacional

Qualquer correcao em DIFAL deve ser replicada em todas as variacoes da formula.

---

## Integracao SPED EFD - Bloco G

O Bloco G do SPED EFD (Escrituracao Fiscal Digital) e dedicado ao CIAP.

**Package:** `efd_dic_dados_ciap.pck`

**Registros gerados:**
- **G110:** Identificacao do documento fiscal (aquisicao do bem)
- **G125:** Movimentacao do bem (entrada, saida, transferencia)
- **G130:** Identificacao do documento fiscal do bem
- **G140:** Identificacao do item do documento fiscal

Os dados de APT_AQUISICAO (incluindo VLR_CRED_DIF_ALIQ) alimentam diretamente
esses registros. Valores incorretos no CIAP resultam em divergencias na EFD.

---

## Checklist para Manutencao do CIAP

1. **Identificar o escopo:** A alteracao afeta s_apquis.sql (geracao) ou packages downstream (consumo)?
2. **Verificar parametros:** APT_ESTAB.APROPRIA_DIF_ALIQ e PRT_PAR3_MSAF.IND_BASE_DIF_ALIQ influenciam o fluxo?
3. **Mapear variacoes por UF:** A formula tem tratamento diferenciado por estado?
4. **Proteger contra valores invalidos:** Usar GREATEST/LEAST quando aplicavel
5. **Validar impacto downstream:** Testar propagacao para saldo de creditos, modelos C/D e SPED Bloco G
6. **Testar com dados reais:** Cenarios com aliquotas interestaduais maiores que internas (ex: importacao, ZFM)
