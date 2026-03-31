# TAX ONE Compliance Checklist

Regras de compliance verificadas pelo agente `taxone-compliance` apos code review.
Inspirado no Step 5 (Compliance, Code Review) do TaxPillot-Patagonia.

---

## Categorias de Verificacao

### SEC-01: SQL Injection (PL/SQL)
**Severidade padrao:** CRITICAL
**O que verificar:**
- `EXECUTE IMMEDIATE` com concatenacao de strings (sem bind variables)
- `DBMS_SQL.PARSE` com input nao sanitizado
- Procedures que recebem `VARCHAR2` e montam SQL dinamico
- `OPEN cursor FOR` com string concatenada

**Regex de deteccao:**
```
EXECUTE\s+IMMEDIATE\s+.*\|\|
DBMS_SQL\.PARSE.*\|\|
OPEN\s+\w+\s+FOR\s+.*\|\|
```

**Excecoes aceitas:**
- Concatenacao de nomes de tabela/coluna vindos de `CAT_LAYOUT_IMP` (tabelas internas do sistema)
- Queries montadas com `DBMS_ASSERT.SIMPLE_SQL_NAME` ou `DBMS_ASSERT.ENQUOTE_NAME`

---

### SEC-02: SQL Injection (PowerBuilder)
**Severidade padrao:** HIGH
**O que verificar:**
- `SetSQLSelect` com concatenacao de input do usuario
- `Retrieve` com filtros concatenados (nao parametrizados)
- DataWindow filtros usando `SetFilter` com input nao sanitizado

**Regex de deteccao:**
```
SetSQLSelect.*\+.*
SetFilter.*\+.*
```

---

### SEC-03: SQL Injection (Java/JDBC)
**Severidade padrao:** CRITICAL
**O que verificar:**
- `Statement.executeQuery` com concatenacao (deve usar `PreparedStatement`)
- `createQuery` com string concatenada (deve usar parametros nomeados)

**Regex de deteccao:**
```
executeQuery\s*\(.*\+
createQuery\s*\(.*\+
```

---

### SEC-04: Hardcoded Credentials
**Severidade padrao:** CRITICAL
**O que verificar:**
- Strings de conexao Oracle hardcoded (`user/pass@host:port/service`)
- Passwords em variaveis com nomes obvios (`password`, `passwd`, `pwd`, `token`, `secret`)
- Connection strings em codigo (nao em config/env)

**Regex de deteccao:**
```
password\s*[:=]\s*["'][^"']+["']
passwd\s*[:=]\s*["'][^"']+["']
oracledb\.connect\s*\(.*password\s*=\s*["']
jdbc:oracle:thin:.*@
\w+/\w+@\w+:\d+/\w+
```

**Excecoes aceitas:**
- Arquivos `.env.example` com valores placeholder (`your_oracle_user`)
- Testes unitarios com mock credentials
- Documentacao com exemplos genericos

---

### SEC-05: Exception Swallowing
**Severidade padrao:** HIGH
**O que verificar:**
- `WHEN OTHERS THEN NULL` (engole qualquer excecao silenciosamente)
- `WHEN OTHERS THEN` sem `RAISE` ou logging (`DBMS_OUTPUT`, `UTL_FILE`, tabela de log)
- `catch(Exception e) {}` em Java (bloco catch vazio)

**Regex de deteccao:**
```
WHEN\s+OTHERS\s+THEN\s*(NULL|COMMIT|ROLLBACK)\s*;
catch\s*\(\s*Exception\s+\w+\s*\)\s*\{\s*\}
```

**Excecoes aceitas:**
- `WHEN OTHERS THEN ROLLBACK; RAISE;` (padrao correto)
- `WHEN NO_DATA_FOUND THEN NULL;` (especifico e intencional)

---

### SEC-06: Permissoes Excessivas
**Severidade padrao:** MEDIUM
**O que verificar:**
- `GRANT EXECUTE ANY` ou `GRANT SELECT ANY TABLE`
- `GRANT DBA TO`
- DDL que concede permissoes amplas demais

**Regex de deteccao:**
```
GRANT\s+(EXECUTE|SELECT|INSERT|UPDATE|DELETE)\s+ANY
GRANT\s+DBA\s+TO
```

---

### SEC-07: Dados Sensiveis em Logs
**Severidade padrao:** MEDIUM
**O que verificar:**
- `DBMS_OUTPUT.PUT_LINE` com dados de CPF, CNPJ, senha, token
- `System.out.println` com dados pessoais
- Logging de payloads completos de request/response

---

### SEC-08: XSS em Codigo Java/Angular
**Severidade padrao:** HIGH (somente para Java servlets e Angular)
**O que verificar:**
- Output de dados do usuario sem encoding em servlets (`response.getWriter().write(userInput)`)
- `innerHTML` com dados nao sanitizados em Angular
- `bypassSecurityTrustHtml` sem justificativa

---

## Classificacao de Severidade

| Severidade | Descricao | Acao |
|-----------|-----------|------|
| **CRITICAL** | Vulnerabilidade exploravel, exposicao de credenciais | **BLOQUEIA PR** — developer deve corrigir |
| **HIGH** | Risco significativo, mas requer contexto especifico para explorar | **ALERTA** — developer deve justificar ou corrigir |
| **MEDIUM** | Ma pratica que pode levar a problemas futuros | **AVISO** — recomendacao de correcao |
| **LOW** | Sugestao de melhoria de seguranca | **INFO** — nao bloqueia |

---

## Output: compliance_report.json

```json
{
  "wi_id": "{WI_ID}",
  "generated_at": "{ISO_8601}",
  "generated_by": "taxone-compliance",
  "files_scanned": ["{lista de arquivos}"],
  "verdict": "PASS|FAIL|PASS_WITH_WARNINGS",
  "findings": [
    {
      "id": "F01",
      "rule": "SEC-04",
      "severity": "CRITICAL",
      "file": "path/to/file.pck",
      "line": 123,
      "description": "Hardcoded password in connection string",
      "evidence": "conn = oracledb.connect(password='abc123')",
      "recommendation": "Use environment variable: os.environ.get('DB_PASS')"
    }
  ],
  "summary": {
    "critical": 0,
    "high": 0,
    "medium": 0,
    "low": 0,
    "total": 0
  }
}
```

**Veredicto:**
- `PASS`: Zero findings CRITICAL ou HIGH
- `PASS_WITH_WARNINGS`: Zero CRITICAL, mas tem HIGH (developer deve justificar)
- `FAIL`: Tem pelo menos 1 CRITICAL → **BLOQUEIA PR**
