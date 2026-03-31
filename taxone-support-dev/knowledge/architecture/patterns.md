# TAX ONE - Patterns de Desenvolvimento

Patterns recorrentes no codigo do TAX ONE organizados por tecnologia.

---

## PL/SQL Patterns

### 1. Package Spec/Body

O pattern principal do TAX ONE. Toda logica de negocio e encapsulada em packages
com separacao clara entre interface publica (spec) e implementacao (body).

```sql
-- SPEC: Interface publica
CREATE OR REPLACE PACKAGE PKG_APURACAO_ICMS AS

  -- Constantes publicas
  C_MODULO CONSTANT VARCHAR2(30) := 'APURACAO_ICMS';

  -- Tipos publicos
  TYPE t_rec_apuracao IS RECORD (
    cd_empresa     NUMBER,
    dt_competencia DATE,
    vl_debito      NUMBER(15,2),
    vl_credito     NUMBER(15,2),
    vl_saldo       NUMBER(15,2)
  );

  TYPE t_tab_apuracao IS TABLE OF t_rec_apuracao;

  -- Excecoes customizadas
  e_competencia_fechada EXCEPTION;
  PRAGMA EXCEPTION_INIT(e_competencia_fechada, -20001);

  -- Procedures e Functions publicas
  PROCEDURE prc_apurar_periodo(
    p_cd_empresa     IN NUMBER,
    p_dt_competencia IN DATE,
    p_cd_usuario     IN VARCHAR2,
    p_msg_retorno    OUT VARCHAR2
  );

  FUNCTION fnc_calcular_saldo(
    p_cd_empresa     IN NUMBER,
    p_dt_competencia IN DATE
  ) RETURN NUMBER;

END PKG_APURACAO_ICMS;
/

-- BODY: Implementacao
CREATE OR REPLACE PACKAGE BODY PKG_APURACAO_ICMS AS

  -- Variaveis privadas do package
  g_cd_usuario VARCHAR2(50);

  -- Procedures privadas (nao expostas no spec)
  PROCEDURE prc_validar_competencia(
    p_cd_empresa     IN NUMBER,
    p_dt_competencia IN DATE
  ) IS
  BEGIN
    -- Validacao interna
    NULL;
  END prc_validar_competencia;

  -- Implementacao das procedures publicas
  PROCEDURE prc_apurar_periodo(
    p_cd_empresa     IN NUMBER,
    p_dt_competencia IN DATE,
    p_cd_usuario     IN VARCHAR2,
    p_msg_retorno    OUT VARCHAR2
  ) IS
  BEGIN
    g_cd_usuario := p_cd_usuario;
    prc_validar_competencia(p_cd_empresa, p_dt_competencia);
    -- Logica de apuracao
    p_msg_retorno := 'Apuracao concluida com sucesso';
  EXCEPTION
    WHEN e_competencia_fechada THEN
      p_msg_retorno := 'Competencia ja fechada. Reabrir antes de apurar.';
    WHEN OTHERS THEN
      p_msg_retorno := 'Erro na apuracao: ' || SQLERRM;
      -- Logging via autonomous transaction
      prc_log_erro(C_MODULO, 'prc_apurar_periodo', SQLERRM, DBMS_UTILITY.FORMAT_ERROR_BACKTRACE);
      RAISE;
  END prc_apurar_periodo;

  FUNCTION fnc_calcular_saldo(
    p_cd_empresa     IN NUMBER,
    p_dt_competencia IN DATE
  ) RETURN NUMBER IS
    v_saldo NUMBER(15,2);
  BEGIN
    SELECT NVL(SUM(vl_debito),0) - NVL(SUM(vl_credito),0)
      INTO v_saldo
      FROM tb_apuracao_icms
     WHERE cd_empresa = p_cd_empresa
       AND dt_competencia = p_dt_competencia;

    RETURN v_saldo;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      RETURN 0;
  END fnc_calcular_saldo;

END PKG_APURACAO_ICMS;
/
```

**Quando usar:** Sempre. Toda logica de negocio nova deve ser criada em packages.

---

### 2. Cursor Processing (FOR .. IN cursor)

Pattern padrao para iterar sobre resultsets.

```sql
PROCEDURE prc_processar_notas(
  p_cd_empresa     IN NUMBER,
  p_dt_competencia IN DATE
) IS
  CURSOR c_notas IS
    SELECT nf.cd_nota, nf.vl_total, nf.cd_cfop
      FROM tb_nota_fiscal nf
     WHERE nf.cd_empresa = p_cd_empresa
       AND TRUNC(nf.dt_emissao, 'MM') = TRUNC(p_dt_competencia, 'MM')
       AND nf.st_nota = 'A'; -- Ativa
BEGIN
  FOR rec IN c_notas LOOP
    -- Processar cada nota
    prc_calcular_imposto(rec.cd_nota, rec.vl_total, rec.cd_cfop);
  END LOOP;
END prc_processar_notas;
```

**Quando usar:** Processamentos simples com baixo volume de registros.

---

### 3. Bulk Collect / FORALL

Pattern para processamento em lote com alta performance.

```sql
PROCEDURE prc_atualizar_impostos_lote(
  p_cd_empresa     IN NUMBER,
  p_dt_competencia IN DATE
) IS
  TYPE t_tab_notas IS TABLE OF tb_nota_fiscal.cd_nota%TYPE;
  TYPE t_tab_valores IS TABLE OF NUMBER(15,2);

  v_notas   t_tab_notas;
  v_valores t_tab_valores;

  C_BATCH_SIZE CONSTANT PLS_INTEGER := 1000;

  CURSOR c_notas IS
    SELECT cd_nota, vl_base_calculo
      FROM tb_nota_fiscal
     WHERE cd_empresa = p_cd_empresa
       AND TRUNC(dt_emissao, 'MM') = TRUNC(p_dt_competencia, 'MM');
BEGIN
  OPEN c_notas;
  LOOP
    FETCH c_notas BULK COLLECT INTO v_notas, v_valores LIMIT C_BATCH_SIZE;
    EXIT WHEN v_notas.COUNT = 0;

    FORALL i IN 1..v_notas.COUNT
      UPDATE tb_imposto_calculado
         SET vl_imposto = v_valores(i) * 0.18, -- Exemplo: aliquota ICMS
             dt_calculo = SYSDATE
       WHERE cd_nota = v_notas(i);

    COMMIT; -- Commit por batch para evitar undo excessivo
  END LOOP;
  CLOSE c_notas;
END prc_atualizar_impostos_lote;
```

**Quando usar:** Processamentos com grande volume de registros (> 1000 rows).

---

### 4. Autonomous Transaction (Logging)

Pattern para gravar logs independente de COMMIT/ROLLBACK da transacao principal.

```sql
PROCEDURE prc_log_erro(
  p_modulo     IN VARCHAR2,
  p_procedure  IN VARCHAR2,
  p_mensagem   IN VARCHAR2,
  p_backtrace  IN VARCHAR2 DEFAULT NULL
) IS
  PRAGMA AUTONOMOUS_TRANSACTION;
BEGIN
  INSERT INTO tb_log_erro (
    cd_log, dt_log, ds_modulo, ds_procedure, ds_mensagem, ds_backtrace, ds_usuario
  ) VALUES (
    seq_log_erro.NEXTVAL, SYSDATE, p_modulo, p_procedure,
    SUBSTR(p_mensagem, 1, 4000), SUBSTR(p_backtrace, 1, 4000), USER
  );
  COMMIT; -- Commit independente
END prc_log_erro;
```

**Quando usar:** Sempre para logging de erros. O log persiste mesmo se a transacao principal fizer ROLLBACK.

---

### 5. Pipelined Function

Pattern para retornar resultsets como tabela virtual (usado em consultas complexas).

```sql
-- No Package Spec:
TYPE t_rec_resultado IS RECORD (
  cd_empresa     NUMBER,
  ds_empresa     VARCHAR2(200),
  vl_total       NUMBER(15,2)
);
TYPE t_tab_resultado IS TABLE OF t_rec_resultado;

FUNCTION fnc_consulta_apuracao(
  p_dt_inicio IN DATE,
  p_dt_fim    IN DATE
) RETURN t_tab_resultado PIPELINED;

-- No Package Body:
FUNCTION fnc_consulta_apuracao(
  p_dt_inicio IN DATE,
  p_dt_fim    IN DATE
) RETURN t_tab_resultado PIPELINED IS
  v_rec t_rec_resultado;
BEGIN
  FOR r IN (
    SELECT a.cd_empresa, e.ds_empresa, SUM(a.vl_saldo) AS vl_total
      FROM tb_apuracao a
      JOIN tb_empresa e ON e.cd_empresa = a.cd_empresa
     WHERE a.dt_competencia BETWEEN p_dt_inicio AND p_dt_fim
     GROUP BY a.cd_empresa, e.ds_empresa
  ) LOOP
    v_rec.cd_empresa := r.cd_empresa;
    v_rec.ds_empresa := r.ds_empresa;
    v_rec.vl_total   := r.vl_total;
    PIPE ROW(v_rec);
  END LOOP;
  RETURN;
END fnc_consulta_apuracao;

-- Uso:
-- SELECT * FROM TABLE(PKG_CONSULTA.fnc_consulta_apuracao(DATE '2026-01-01', DATE '2026-12-31'));
```

**Quando usar:** Consultas complexas que precisam ser consumidas como tabela por PowerBuilder ou views.

---

### 6. REF CURSOR (Para PowerBuilder)

Pattern para retornar cursores dinamicos consumidos pelo frontend PowerBuilder.

```sql
PROCEDURE prc_consultar_notas(
  p_cd_empresa     IN NUMBER,
  p_dt_inicio      IN DATE,
  p_dt_fim         IN DATE,
  p_cd_cfop        IN VARCHAR2 DEFAULT NULL,
  p_cursor         OUT SYS_REFCURSOR
) IS
  v_sql VARCHAR2(4000);
BEGIN
  v_sql := 'SELECT cd_nota, dt_emissao, vl_total, ds_participante
               FROM tb_nota_fiscal
              WHERE cd_empresa = :p_empresa
                AND dt_emissao BETWEEN :p_inicio AND :p_fim';

  IF p_cd_cfop IS NOT NULL THEN
    v_sql := v_sql || ' AND cd_cfop = :p_cfop';
    OPEN p_cursor FOR v_sql USING p_cd_empresa, p_dt_inicio, p_dt_fim, p_cd_cfop;
  ELSE
    OPEN p_cursor FOR v_sql USING p_cd_empresa, p_dt_inicio, p_dt_fim;
  END IF;
END prc_consultar_notas;
```

**Quando usar:** Sempre que PowerBuilder precisar consumir dados de procedures.
**IMPORTANTE:** Sempre usar bind variables (:param), NUNCA concatenar valores.

---

## Oracle Patterns

### 7. Particionamento por Periodo

```sql
CREATE TABLE tb_nota_fiscal (
  cd_nota        NUMBER       NOT NULL,
  cd_empresa     NUMBER       NOT NULL,
  dt_emissao     DATE         NOT NULL,
  vl_total       NUMBER(15,2),
  st_nota        VARCHAR2(1),
  -- ...demais colunas
  CONSTRAINT pk_nota_fiscal PRIMARY KEY (cd_nota, dt_emissao)
)
PARTITION BY RANGE (dt_emissao)
INTERVAL (NUMTOYMINTERVAL(1, 'MONTH'))
(
  PARTITION p_inicial VALUES LESS THAN (DATE '2020-01-01')
);
```

**Quando usar:** Tabelas de movimento com crescimento continuo (notas fiscais, lancamentos, logs).

---

### 8. Estrategia de Indexacao

```sql
-- Indice composto para padrao de acesso frequente
CREATE INDEX idx_nf_empresa_dt ON tb_nota_fiscal(cd_empresa, dt_emissao)
  LOCAL -- Alinhado com particionamento
  TABLESPACE ts_index;

-- Indice function-based para buscas case-insensitive
CREATE INDEX idx_part_nome ON tb_participante(UPPER(ds_nome))
  TABLESPACE ts_index;

-- Indice bitmap para colunas de baixa cardinalidade
CREATE BITMAP INDEX idx_nf_status ON tb_nota_fiscal(st_nota)
  LOCAL
  TABLESPACE ts_index;

-- Indice covering para evitar table access
CREATE INDEX idx_nf_consulta ON tb_nota_fiscal(cd_empresa, dt_emissao, vl_total, st_nota)
  LOCAL
  TABLESPACE ts_index;
```

---

### 9. Materialized Views

```sql
CREATE MATERIALIZED VIEW mv_apuracao_resumo
  BUILD IMMEDIATE
  REFRESH FAST ON DEMAND
  ENABLE QUERY REWRITE
AS
  SELECT a.cd_empresa,
         TRUNC(a.dt_competencia, 'MM') AS dt_competencia,
         SUM(a.vl_debito) AS vl_total_debito,
         SUM(a.vl_credito) AS vl_total_credito,
         SUM(a.vl_debito) - SUM(a.vl_credito) AS vl_saldo,
         COUNT(*) AS qt_registros
    FROM tb_apuracao a
   GROUP BY a.cd_empresa, TRUNC(a.dt_competencia, 'MM');

-- Refresh manual apos processamento de apuracao
BEGIN
  DBMS_MVIEW.REFRESH('MV_APURACAO_RESUMO', 'C'); -- Complete refresh
END;
```

---

## PowerBuilder Patterns

### 10. DataWindow com Procedure PL/SQL

```
// No DataWindow, SQL Source:
// SELECT ... (pode ser stored procedure via REF CURSOR)

// No script do Window (ex: cb_consultar.clicked):
Long ll_rows
String ls_erro

// Setar parametros
dw_notas.SetTransObject(SQLCA)
dw_notas.Retrieve(il_empresa, idt_inicio, idt_fim)

ll_rows = dw_notas.RowCount()
IF ll_rows = 0 THEN
   MessageBox("Consulta", "Nenhum registro encontrado.")
END IF
```

### 11. User Objects (Componentes Reutilizaveis)

```
// User Object nao-visual para validacoes fiscais
// uo_validacao_fiscal

PUBLIC FUNCTION Boolean of_validar_cfop(String as_cfop):
  // Validar formato e existencia do CFOP
  Long ll_count

  SELECT COUNT(*) INTO :ll_count
    FROM tb_cfop
   WHERE cd_cfop = :as_cfop
     AND st_ativo = 'S'
  USING SQLCA;

  RETURN (ll_count > 0)
END FUNCTION
```

---

## Java Patterns

### 12. DAO Pattern (Acesso a Dados)

```java
public class NotaFiscalDAO {

    private Connection getConnection() throws SQLException {
        return DataSourceManager.getConnection();
    }

    public List<NotaFiscal> buscarPorPeriodo(long cdEmpresa, Date dtInicio, Date dtFim)
            throws SQLException {
        String sql = "SELECT cd_nota, dt_emissao, vl_total " +
                     "FROM tb_nota_fiscal " +
                     "WHERE cd_empresa = ? AND dt_emissao BETWEEN ? AND ?";

        List<NotaFiscal> notas = new ArrayList<>();

        try (Connection conn = getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setLong(1, cdEmpresa);
            ps.setDate(2, new java.sql.Date(dtInicio.getTime()));
            ps.setDate(3, new java.sql.Date(dtFim.getTime()));

            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    NotaFiscal nf = new NotaFiscal();
                    nf.setCdNota(rs.getLong("cd_nota"));
                    nf.setDtEmissao(rs.getDate("dt_emissao"));
                    nf.setVlTotal(rs.getBigDecimal("vl_total"));
                    notas.add(nf);
                }
            }
        }
        return notas;
    }
}
```

### 13. Service Layer

```java
public class ApuracaoService {

    private final ApuracaoDAO apuracaoDAO;
    private final NotaFiscalDAO notaFiscalDAO;

    public ApuracaoService() {
        this.apuracaoDAO = new ApuracaoDAO();
        this.notaFiscalDAO = new NotaFiscalDAO();
    }

    public ResultadoApuracao apurarPeriodo(long cdEmpresa, Date dtCompetencia)
            throws ApuracaoException {
        try {
            // Chamar procedure PL/SQL de apuracao
            String msgRetorno = apuracaoDAO.executarApuracao(cdEmpresa, dtCompetencia);

            if (msgRetorno.contains("Erro")) {
                throw new ApuracaoException(msgRetorno);
            }

            return apuracaoDAO.buscarResultado(cdEmpresa, dtCompetencia);

        } catch (SQLException e) {
            throw new ApuracaoException("Erro ao apurar periodo: " + e.getMessage(), e);
        }
    }
}
```

---

## Anti-Patterns (Evitar)

| Anti-Pattern | Problema | Pattern Correto |
|-------------|----------|-----------------|
| SQL dinamico com concatenacao | SQL Injection | Usar bind variables |
| SELECT * em queries | Performance, fragilidade | Listar colunas explicitas |
| WHEN OTHERS sem RAISE | Excecao engolida, bug silencioso | WHEN OTHERS THEN log + RAISE |
| Cursor FOR LOOP com UPDATE | Row-by-row processing lento | BULK COLLECT + FORALL |
| COMMIT dentro de loop | Dados inconsistentes em erro | COMMIT por batch ou no final |
| Hardcode de valores fiscais | Manutencao impossivel | Tabela de parametros |
| View com subquery correlacionada | Performance degradada | JOIN ou Materialized View |
