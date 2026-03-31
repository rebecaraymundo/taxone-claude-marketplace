# TAX ONE - Padroes de Codigo PL/SQL

Padroes de codificacao para a squad TAX ONE.
Todo codigo PL/SQL, SQL e DDL deve seguir estas convencoes.

---

## 1. Formatacao SQL

### Palavras Reservadas

- Palavras reservadas SQL e PL/SQL em **MAIUSCULO**
- Nomes de objetos (tabelas, colunas, variaveis) em **minusculo** ou **snake_case**

```sql
-- Correto
SELECT nf.cd_nota,
       nf.dt_emissao,
       nf.vl_total
  FROM tb_nota_fiscal nf
 WHERE nf.cd_empresa = p_cd_empresa
   AND nf.st_nota = 'A'
 ORDER BY nf.dt_emissao DESC;

-- Incorreto
select NF.CD_NOTA, NF.DT_EMISSAO, NF.VL_TOTAL from TB_NOTA_FISCAL NF where NF.CD_EMPRESA = p_cd_empresa
```

### Indentacao

- Usar **2 espacos** para indentacao (nao TAB)
- Alinhar clausulas SQL pela direita:

```sql
SELECT a.cd_empresa,
       a.dt_competencia,
       SUM(a.vl_debito) AS vl_total_debito
  FROM tb_apuracao a
  JOIN tb_empresa e ON e.cd_empresa = a.cd_empresa
 WHERE a.dt_competencia >= DATE '2026-01-01'
   AND a.st_apuracao = 'F'
 GROUP BY a.cd_empresa, a.dt_competencia
HAVING SUM(a.vl_debito) > 0
 ORDER BY a.cd_empresa;
```

### Alias de Tabela

- SEMPRE usar alias em queries com mais de uma tabela
- Alias curtos e significativos (2-3 letras baseadas no nome da tabela)
- Prefixar TODAS as colunas com o alias da tabela

```sql
-- Correto
SELECT nf.cd_nota, it.vl_item
  FROM tb_nota_fiscal nf
  JOIN tb_item_nota it ON it.cd_nota = nf.cd_nota;

-- Incorreto (sem alias, colunas ambiguas)
SELECT cd_nota, vl_item
  FROM tb_nota_fiscal, tb_item_nota
 WHERE tb_nota_fiscal.cd_nota = tb_item_nota.cd_nota;
```

---

## 2. Convencoes PL/SQL

### Declaracao de Variaveis

| Prefixo | Tipo | Exemplo |
|---------|------|---------|
| `v_` | Variavel local | `v_valor NUMBER;` |
| `p_` | Parametro | `p_cd_empresa IN NUMBER` |
| `g_` | Variavel global (package body) | `g_cd_usuario VARCHAR2(50);` |
| `c_` / `C_` | Constante | `C_MODULO CONSTANT VARCHAR2(30) := 'ICMS';` |
| `e_` | Excecao | `e_competencia_fechada EXCEPTION;` |
| `t_` | Type | `TYPE t_tab_notas IS TABLE OF ...;` |
| `r_` / `rec` | Record | `r_nota t_rec_nota;` ou `rec` em FOR loops |

```sql
PROCEDURE prc_exemplo(
  p_cd_empresa     IN  NUMBER,       -- Codigo da empresa
  p_dt_competencia IN  DATE,         -- Data de competencia
  p_msg_retorno    OUT VARCHAR2      -- Mensagem de retorno
) IS
  v_total       NUMBER(15,2) := 0;   -- Total calculado
  v_contador    PLS_INTEGER  := 0;   -- Contador de registros
  C_LIMITE      CONSTANT PLS_INTEGER := 1000;
BEGIN
  -- ...
END prc_exemplo;
```

### Tipos de Dados

- Usar `%TYPE` para variaveis que referenciam colunas de tabela
- Usar `%ROWTYPE` para records de tabela
- Preferir `PLS_INTEGER` sobre `NUMBER` para contadores e indices

```sql
v_cd_nota    tb_nota_fiscal.cd_nota%TYPE;
v_nota_rec   tb_nota_fiscal%ROWTYPE;
v_contador   PLS_INTEGER := 0;
```

---

## 3. Exception Handling

### Regra Geral

- SEMPRE tratar excecoes esperadas (NO_DATA_FOUND, TOO_MANY_ROWS)
- WHEN OTHERS deve SEMPRE fazer logging + RAISE (nunca engolir excecao)
- Usar excecoes customizadas para regras de negocio

```sql
-- Correto
BEGIN
  SELECT vl_aliquota
    INTO v_aliquota
    FROM tb_aliquota
   WHERE cd_imposto = p_cd_imposto
     AND cd_uf = p_cd_uf;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    -- Aliquota nao cadastrada - usar valor padrao
    v_aliquota := 0;
  WHEN TOO_MANY_ROWS THEN
    -- Cadastro inconsistente - logar e propagar erro
    prc_log_erro('CALCULO', 'fnc_obter_aliquota',
      'Multiplas aliquotas para imposto=' || p_cd_imposto || ' uf=' || p_cd_uf);
    RAISE;
  WHEN OTHERS THEN
    prc_log_erro('CALCULO', 'fnc_obter_aliquota', SQLERRM,
      DBMS_UTILITY.FORMAT_ERROR_BACKTRACE);
    RAISE; -- SEMPRE propagar
END;

-- Incorreto (excecao engolida)
EXCEPTION
  WHEN OTHERS THEN
    NULL; -- NUNCA fazer isso
```

### Excecoes Customizadas

```sql
-- No Package Spec
e_competencia_fechada  EXCEPTION;
e_nota_cancelada       EXCEPTION;
e_aliquota_invalida    EXCEPTION;

PRAGMA EXCEPTION_INIT(e_competencia_fechada, -20001);
PRAGMA EXCEPTION_INIT(e_nota_cancelada,      -20002);
PRAGMA EXCEPTION_INIT(e_aliquota_invalida,   -20003);

-- No Package Body
IF v_status = 'F' THEN
  RAISE_APPLICATION_ERROR(-20001, 'Competencia ' ||
    TO_CHAR(p_dt_competencia, 'MM/YYYY') || ' ja esta fechada.');
END IF;
```

---

## 4. Padroes de Comentarios

### Idioma

- **Todos os comentarios em portugues** (padrao da squad TAX ONE)
- Acentos sao opcionais (evitar problemas de encoding)

### Cabecalho de Package/Procedure

```sql
/******************************************************************************
 * Package: PKG_APURACAO_ICMS
 * Descricao: Rotinas de apuracao do ICMS por empresa e competencia
 * Modulo: Apuracao
 * Autor: [nome]
 * Data Criacao: [dd/mm/yyyy]
 *
 * Historico de Alteracoes:
 * Data       | Autor    | Descricao
 * -----------|----------|--------------------------------------------------
 * dd/mm/yyyy | [nome]   | [descricao da alteracao]
 ******************************************************************************/
```

### Comentarios Inline

```sql
-- Calcular base de calculo do ICMS descontando IPI quando aplicavel
v_base_icms := v_vl_produto + v_vl_frete + v_vl_seguro - v_vl_desconto;

IF v_contribuinte = 'N' THEN
  -- Nao contribuinte: IPI integra a base do ICMS (art. 13, LC 87/96)
  v_base_icms := v_base_icms + v_vl_ipi;
END IF;
```

### Comentarios de Bloco

```sql
/*
 * Regra de negocio: Calculo do ICMS-ST
 * Base legal: Art. 8, LC 87/96
 * Formula: ICMS-ST = (Base ST * Aliquota Interna) - ICMS Proprio
 * Observacao: Quando aliquota interestadual for zero, usar aliquota interna
 */
```

---

## 5. SQL Dinamico

### OBRIGATORIO: Bind Variables

```sql
-- Correto: bind variables
EXECUTE IMMEDIATE
  'SELECT COUNT(*) FROM ' || v_tabela || ' WHERE cd_empresa = :1 AND dt_emissao = :2'
  INTO v_count
  USING p_cd_empresa, p_dt_emissao;

-- Incorreto: concatenacao de valores (SQL INJECTION!)
EXECUTE IMMEDIATE
  'SELECT COUNT(*) FROM tb_nota WHERE cd_empresa = ' || p_cd_empresa; -- PROIBIDO
```

### Quando Usar SQL Dinamico

- Apenas quando o nome da tabela/coluna e dinamico (nao o valor)
- Sempre validar nomes de tabela/coluna contra uma lista conhecida (whitelist)
- Documentar o motivo do uso de SQL dinamico

---

## 6. Controle de Transacao

### Regras

- **Procedures de negocio:** NAO fazer COMMIT interno (quem chama controla a transacao)
- **Procedures de lote (batch):** COMMIT a cada N registros (batch size)
- **Logging:** SEMPRE via AUTONOMOUS_TRANSACTION
- **Savepoints:** Usar para rollback parcial dentro de processamentos complexos

```sql
-- Procedure de negocio (sem COMMIT)
PROCEDURE prc_calcular_imposto(p_cd_nota IN NUMBER) IS
BEGIN
  UPDATE tb_imposto SET vl_imposto = ... WHERE cd_nota = p_cd_nota;
  -- SEM COMMIT - quem chama decide
END;

-- Procedure de lote (com COMMIT por batch)
PROCEDURE prc_recalcular_lote(p_cd_empresa IN NUMBER) IS
  C_BATCH CONSTANT PLS_INTEGER := 500;
  v_count PLS_INTEGER := 0;
BEGIN
  FOR rec IN (SELECT cd_nota FROM tb_nota_fiscal WHERE cd_empresa = p_cd_empresa) LOOP
    prc_calcular_imposto(rec.cd_nota);
    v_count := v_count + 1;

    IF MOD(v_count, C_BATCH) = 0 THEN
      COMMIT; -- Commit por batch
    END IF;
  END LOOP;
  COMMIT; -- Commit final
END;
```

---

## 7. Performance

### Obrigatorio

- Usar `BULK COLLECT` + `FORALL` para operacoes com > 1000 registros
- Usar bind variables em TODAS as queries (evitar hard parse)
- Listar colunas explicitas (nunca `SELECT *`)
- Prefixar colunas com alias de tabela em JOINs

### Recomendado

- `NVL()` antes de operacoes aritmeticas com colunas nullable
- `TRUNC()` para comparacoes de data sem horario
- `EXISTS` em vez de `COUNT(*) > 0` para verificacoes de existencia
- `COALESCE` em vez de `NVL` encadeado
- Evitar funcoes em colunas do WHERE (impede uso de indice)

```sql
-- Correto
WHERE TRUNC(nf.dt_emissao) = TRUNC(p_dt_emissao)

-- Melhor (permite uso de indice)
WHERE nf.dt_emissao >= TRUNC(p_dt_emissao)
  AND nf.dt_emissao <  TRUNC(p_dt_emissao) + 1

-- Correto: EXISTS
IF EXISTS (SELECT 1 FROM tb_nota WHERE cd_empresa = p_cd_empresa) THEN ...

-- Incorreto: COUNT para verificar existencia
SELECT COUNT(*) INTO v_count FROM tb_nota WHERE cd_empresa = p_cd_empresa;
IF v_count > 0 THEN ...
```

---

## 8. DDL Standards

### Scripts DDL

- Todo DDL deve ter script de rollback correspondente
- Incluir comentario com numero do work item (ADO)
- Testar em DEV antes de enviar para QA

```sql
-- =============================================================================
-- Work Item: #12345
-- Descricao: Adicionar coluna de aliquota efetiva na tabela de impostos
-- Autor: [nome]
-- Data: dd/mm/yyyy
-- =============================================================================

-- DEPLOY
ALTER TABLE tb_imposto_calculado
  ADD (vl_aliquota_efetiva NUMBER(7,4));

COMMENT ON COLUMN tb_imposto_calculado.vl_aliquota_efetiva IS
  'Aliquota efetiva calculada considerando reducoes e beneficios';

-- ROLLBACK
-- ALTER TABLE tb_imposto_calculado DROP COLUMN vl_aliquota_efetiva;
```
