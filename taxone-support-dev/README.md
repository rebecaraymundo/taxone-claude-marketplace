# taxone-support-dev

Plugin multi-agente para suporte e desenvolvimento do TAX ONE (Mastersaf Fiscal Solutions).

## Comandos

| Comando | Descricao |
|---------|-----------|
| `/taxone-auto-fix <WI_ID>` | Pipeline automatizado: ADO → analise → fix → PR → QA |
| `/taxone-bug-fix <WI_ID>` | Correcao manual de bug com fluxo completo LOCAL+QA |
| `/taxone-us-implement <WI_ID>` | Implementacao de Features/US orientado a requisitos |
| `/taxone-us-auto-implement <WI_ID>` | Pipeline automatizado de implementacao de US |
| `/taxone-suite-runner <WI_ID>` | Testes de regressao SuiteAutomation |
| `/taxone-doc-gen <escopo>` | Geracao de documentacao tecnica e funcional |
| `/taxone-compound <WI_ID>` | Compound Engineering (documentacao de solucoes) |
| `/taxone-sprint-plan <sprint>` | Sprint Planning automatizado |
| `/taxone-feature-dev <desc>` | Desenvolvimento de features (sem ADO) |
| `/query-executor-prod-uat <SQL>` | Queries SELECT em Prod/UAT via GitHub Actions |

## Agentes Especializados (21)

| Agente | Funcao |
|--------|--------|
| taxone-plsql | Desenvolvimento PL/SQL Oracle |
| taxone-pb | Desenvolvimento PowerBuilder |
| taxone-java | Desenvolvimento Java |
| taxone-angular | Desenvolvimento Angular/Frontend |
| taxone-plsql-reviewer | Code review PL/SQL |
| taxone-pb-reviewer | Code review PowerBuilder |
| taxone-java-reviewer | Code review Java |
| taxone-architect | Arquitetura e design |
| taxone-dba | Administracao de banco Oracle |
| taxone-pm | Product Management e triagem |
| taxone-sm | Scrum Master |
| taxone-n3-triage | Triagem N3 e enrichment |
| taxone-rum-analyst | Analise RUM/APM Datadog |
| taxone-e2e-tester | Testes E2E Playwright |
| taxone-suite-runner | Testes SuiteAutomation |
| taxone-tester | Testes gerais |
| taxone-test-data-engineer | Engenharia de dados de teste |
| taxone-techlead-dev | Tech Lead desenvolvimento |
| taxone-techlead-qa | Tech Lead QA |
| taxone-explorer | Exploracao de codebase |
| taxone-compliance | Scan de seguranca/compliance |

## Tech Stack

- **Backend**: PL/SQL Oracle, PowerBuilder, Java
- **Frontend**: Angular
- **Banco**: Oracle 19c (4028 tabelas documentadas)
- **Testes**: Playwright E2E, SuiteAutomation
- **CI/CD**: GitHub Actions
- **Gestao**: Azure DevOps
- **Observabilidade**: Datadog RUM/APM

## Base de Conhecimento

19 dominios documentados em `knowledge/`:

- **schema/** — 61 arquivos, 4028 tabelas, 66067 colunas, 3498 FKs
- **features/** — Documentacao funcional por modulo
- **architecture/** — Diagramas e decisoes arquiteturais
- **datadog/** — Mapas de servicos, erros conhecidos, baselines
- **conventions/** — Padroes de codigo e nomenclatura
- **team/** — Roster e especialidades
- **webhelp/** — Mapeamento de telas e menus
- **suite-automation/** — Mapeamento componente → testes

## Integracoes

- **Azure DevOps** — Work Items, queries WIQL, board columns, attachments
- **Datadog** — RUM, APM, logs, monitors, dashboards
- **Playwright** — Testes E2E automatizados
- **GitHub Actions** — Query executor Prod/UAT, CI/CD
- **SuiteAutomation** — Testes de regressao XML-based

## Requisitos

1. **Claude Code** instalado
2. **Repositorio taxone_dw** clonado em path configuravel via `.env`
3. **Variaveis de ambiente**:
   - `GITHUB_TOKEN` — Acesso ao GitHub Enterprise (tr org)
   - `ADO_PAT` — Azure DevOps Personal Access Token
   - `DD_API_KEY` / `DD_APP_KEY` — Datadog API
   - `ZENDESK_URL` / `ZENDESK_TOKEN` — Zendesk (opcional)

## Exemplos de Uso

```bash
# Corrigir bug automaticamente
/taxone-auto-fix 1083740

# Implementar user story
/taxone-us-implement 1079124

# Executar testes de regressao
/taxone-suite-runner 1058668

# Consultar dados em producao
/query-executor-prod-uat "SELECT COUNT(*) FROM X2002_PLANO_CONTAS WHERE TENANT_CODE = 'SAZ'"
```
