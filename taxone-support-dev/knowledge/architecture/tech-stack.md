# TAX ONE - Tech Stack Completa

## Resumo

| Camada | Tecnologia | Versao Tipica |
|--------|-----------|---------------|
| Backend / Negocio | PL/SQL | Oracle 12c+ |
| Database | Oracle Database | 12c / 19c |
| Desktop UI | PowerBuilder | 12.x+ |
| Integracao / Web | Java | 8+ |
| Controle de Versao | GitHub | - |
| Work Items | Azure DevOps (ADO) | - |
| Testes Automatizados | Nenhum framework | - |

---

## PL/SQL (Camada de Negocio)

PL/SQL e a linguagem principal do TAX ONE. Toda logica de negocio fiscal reside
em packages, procedures e functions Oracle.

### Objetos PL/SQL Utilizados

| Objeto | Uso no TAX ONE |
|--------|---------------|
| **Package Spec** | Interface publica - declaracao de procedures, functions, types, constants, exceptions |
| **Package Body** | Implementacao da logica de negocio - procedures privadas, cursores, variaveis |
| **Procedure** | Operacoes que modificam dados (INSERT, UPDATE, DELETE), processamentos em lote |
| **Function** | Calculos que retornam valor (impostos, validacoes, formatacoes) |
| **Trigger** | Auditoria automatica, validacoes de integridade, populacao de campos derivados |
| **Type / Type Body** | Tipos customizados para pipelined functions e collections |
| **Exception** | Excecoes customizadas para regras de negocio |

### Features PL/SQL Mais Utilizadas

- `BULK COLLECT` / `FORALL` - Processamento em lote eficiente
- `PRAGMA AUTONOMOUS_TRANSACTION` - Logging independente de rollback
- `PIPELINED FUNCTION` - Retorno de resultsets como tabela
- `REF CURSOR` / `SYS_REFCURSOR` - Cursores dinamicos para PowerBuilder
- `EXECUTE IMMEDIATE` - SQL dinamico (com bind variables obrigatorias)
- `DBMS_OUTPUT` - Debug e logging
- `UTL_FILE` - Leitura/escrita de arquivos no servidor
- `DBMS_LOB` - Manipulacao de CLOBs e BLOBs (XMLs, PDFs)
- `XMLTYPE` - Parsing de XML (notas fiscais eletronicas)
- `DBMS_SCHEDULER` - Jobs agendados

---

## Oracle Database (Camada de Dados)

### Objetos de Banco Utilizados

| Objeto | Uso no TAX ONE | Quantidade Estimada |
|--------|---------------|---------------------|
| **Tables** | Dados transacionais e cadastrais | Centenas por modulo |
| **Views** | Consultas otimizadas para telas e relatorios | Dezenas por modulo |
| **Materialized Views** | Cache de apuracoes e consolidacoes | Por modulo de apuracao |
| **Packages** | Logica de negocio encapsulada | Dezenas por modulo |
| **Procedures** | Processamentos standalone | Variavel |
| **Functions** | Calculos e validacoes | Variavel |
| **Triggers** | Auditoria e integridade | Por tabela critica |
| **Sequences** | Auto-numeracao de registros e documentos | Por tabela com PK numerica |
| **Indices** | Performance de acesso | Multiplos por tabela |
| **Partitions** | Tabelas de grande volume (por periodo) | Tabelas de movimento |
| **Synonyms** | Acesso cross-schema | Por objeto compartilhado |
| **Database Links** | Acesso a bancos remotos | Por integracao |
| **Jobs (DBMS_SCHEDULER)** | Processamentos agendados | Por modulo |

### Estrategias de Particionamento

- **Range Partition** por data de competencia (mais comum)
- **List Partition** por estado/UF (obrigacoes estaduais)
- **Composite Partition** range-list para tabelas de alto volume
- **Interval Partition** para criacao automatica de particoes

### Estrategias de Indexacao

- **B-tree** - Padrao para colunas de alta cardinalidade
- **Bitmap** - Colunas de baixa cardinalidade (status, tipo, UF)
- **Function-based** - Indices em expressoes (UPPER, TRUNC, TO_CHAR)
- **Composite** - Indices multi-coluna para padroes de acesso frequentes
- **Compressed** - Reducao de espaco para indices com prefixo repetitivo
- **Local** - Indices particionados alinhados com tabela
- **Global** - Indices nao-particionados em tabelas particionadas

### Tablespaces Tipicos

- **DATA** - Tabelas transacionais
- **INDEX** - Indices
- **LOB** - Large Objects (XMLs, arquivos)
- **TEMP** - Operacoes temporarias (sorts, hash joins)

---

## PowerBuilder (Interface Desktop)

### Componentes Utilizados

| Componente | Uso no TAX ONE |
|-----------|---------------|
| **Application Object** | Ponto de entrada da aplicacao |
| **Window** | Telas de cadastro, consulta, processamento |
| **DataWindow** | Grids e formularios com SQL embutido - conexao direta ao Oracle |
| **DataStore** | DataWindow sem interface visual (processamento em background) |
| **User Object** | Componentes reutilizaveis (visual e nao-visual) |
| **Menu** | Estrutura de navegacao da aplicacao |
| **Global Functions** | Funcoes utilitarias globais |
| **Structures** | Tipos de dados compostos |

### Conexao com Oracle

- PowerBuilder conecta diretamente ao Oracle via driver nativo
- DataWindows executam SQL direto ou chamam procedures/functions PL/SQL
- REF CURSORs sao consumidos por DataWindows para consultas dinamicas

---

## Java (Integracao e Web)

### Componentes Utilizados

| Componente | Uso no TAX ONE |
|-----------|---------------|
| **JDBC** | Conexao com Oracle Database |
| **DAO Pattern** | Acesso a dados encapsulado |
| **Service Layer** | Logica de integracao |
| **Web Services (SOAP)** | Comunicacao com SEFAZ, Receita Federal |
| **REST APIs** | Integracoes modernas |
| **Batch Processing** | Processamentos agendados |
| **XML Processing** | Parsing/geracao de XMLs fiscais (DOM, SAX, JAXB) |
| **Digital Certificates** | Assinatura digital de documentos fiscais |

### Bibliotecas Comuns

- Apache Axis / CXF (Web Services SOAP)
- JAXB (XML binding)
- Bouncy Castle (certificados digitais)
- Log4j (logging)
- Oracle JDBC Driver (ojdbc)

---

## Ferramentas de Desenvolvimento

### Controle de Versao

- **GitHub** - Repositorios de codigo-fonte
- Branches por feature/bugfix
- Pull Requests para code review

### Gestao de Trabalho

- **Azure DevOps (ADO)** - Work items, bugs, user stories, sprints
- Boards para acompanhamento de tarefas
- Vinculo entre work items e commits/PRs

### IDEs e Ferramentas

| Ferramenta | Uso |
|-----------|-----|
| **Oracle SQL Developer** | Desenvolvimento PL/SQL, debug, explain plan |
| **TOAD** | Administracao Oracle, tuning |
| **PowerBuilder IDE** | Desenvolvimento de interface desktop |
| **IntelliJ / Eclipse** | Desenvolvimento Java |
| **DBeaver** | Consultas e administracao de banco alternativa |

---

## Testes

### Estado Atual

- **NAO ha framework de testes automatizados** para PL/SQL ou PowerBuilder
- Validacao e feita manualmente em ambiente QA
- Testes de regressao sao manuais
- Scripts SQL de validacao sao criados ad-hoc para cenarios criticos

### Estrategia de Validacao

1. Desenvolvedor testa localmente em DEV
2. Deploy em QA para validacao funcional
3. Tester valida cenarios principais e de borda
4. Deploy em HML para validacao com dados reais (anonimizados)
5. Aprovacao para deploy em PRD

---

## Deploy

### Processo de Deploy

1. Scripts SQL gerados pelo desenvolvedor (DDL + DML + PL/SQL)
2. Scripts revisados em code review (PR)
3. Scripts executados manualmente em cada ambiente (DEV -> QA -> HML -> PRD)
4. Rollback scripts preparados para cada mudanca

### Artefatos de Deploy Tipicos

```
deploy/
├── 01_ddl/          --> CREATE/ALTER TABLE, INDEX, SEQUENCE
├── 02_plsql/        --> CREATE OR REPLACE PACKAGE, PROCEDURE, FUNCTION
├── 03_views/        --> CREATE OR REPLACE VIEW
├── 04_triggers/     --> CREATE OR REPLACE TRIGGER
├── 05_dml/          --> INSERT, UPDATE, DELETE (dados de configuracao)
├── 06_grants/       --> GRANT, SYNONYM
└── rollback/        --> Scripts de rollback para cada step
```
