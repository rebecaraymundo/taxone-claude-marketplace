# TAX ONE - Visao Geral da Arquitetura

## O que e o TAX ONE

TAX ONE e a solucao fiscal enterprise da Thomson Reuters (anteriormente Mastersaf),
utilizada por grandes empresas brasileiras para gestao tributaria e fiscal.
O sistema abrange apuracao de impostos, obrigacoes acessorias, calculos fiscais,
cadastros e integracoes com orgaos governamentais (SEFAZ, Receita Federal, etc.).

---

## Arquitetura de Alto Nivel

```
+------------------------------------------------------------------+
|                      CAMADA DE APRESENTACAO                       |
|                                                                   |
|  +-----------------------------+  +----------------------------+  |
|  |     PowerBuilder Desktop    |  |    Java Web (quando aplic.) |  |
|  |  - Windows / DataWindows    |  |  - Servlets / JSP          |  |
|  |  - User Objects             |  |  - Web Services            |  |
|  |  - Scripts de Evento        |  |  - REST APIs               |  |
|  +-------------+---------------+  +-------------+--------------+  |
|                |                                |                 |
+------------------------------------------------------------------+
                 |                                |
+------------------------------------------------------------------+
|                      CAMADA DE NEGOCIO                            |
|                                                                   |
|  +------------------------------------------------------------+  |
|  |                   PL/SQL (Oracle Database)                  |  |
|  |                                                             |  |
|  |  Packages -----> Logica de negocio principal                |  |
|  |  Procedures ---> Processamentos e operacoes                 |  |
|  |  Functions ----> Calculos e validacoes                      |  |
|  |  Triggers -----> Auditoria e integridade                    |  |
|  |  Types --------> Estruturas de dados                        |  |
|  +------------------------------------------------------------+  |
|                                                                   |
+------------------------------------------------------------------+
                              |
+------------------------------------------------------------------+
|                      CAMADA DE DADOS                              |
|                                                                   |
|  +------------------------------------------------------------+  |
|  |                     Oracle Database                         |  |
|  |                                                             |  |
|  |  Tabelas -----------> Dados transacionais e cadastrais      |  |
|  |  Views -------------> Consultas otimizadas                  |  |
|  |  Materialized Views -> Cache de consultas complexas         |  |
|  |  Indices -----------> Performance de acesso                 |  |
|  |  Sequences ---------> Numeracao automatica                  |  |
|  |  Partitions --------> Tabelas de grande volume              |  |
|  +------------------------------------------------------------+  |
|                                                                   |
+------------------------------------------------------------------+
                              |
+------------------------------------------------------------------+
|                      INTEGRACOES EXTERNAS                         |
|                                                                   |
|  +-------------------+  +------------------+  +----------------+  |
|  |  SEFAZ / NFe      |  | Receita Federal  |  | ERP Clientes   |  |
|  |  Web Services      |  | SPED / EFD       |  | APIs / Arquivos|  |
|  +-------------------+  +------------------+  +----------------+  |
|                                                                   |
+------------------------------------------------------------------+
```

---

## Camadas Detalhadas

### 1. PL/SQL - Camada de Negocio Principal

A logica de negocio do TAX ONE reside predominantemente em **PL/SQL**.
Esta e a camada mais critica e onde ocorre a maior parte do desenvolvimento.

**Responsabilidades:**
- Calculos tributarios (ICMS, IPI, PIS, COFINS, ISS, IRPJ, CSLL, etc.)
- Apuracao de impostos (consolidacao por periodo)
- Geracao de obrigacoes acessorias (SPED Fiscal, EFD Contribuicoes, GIA, DCTF, etc.)
- Validacoes de negocio (regras fiscais, NCM, CFOP, CST, etc.)
- Processamentos em lote (importacao, calculo massivo, fechamento)
- Auditoria e rastreabilidade (triggers de log)

**Estrutura tipica:**
```
PKG_{MODULO}_SPEC.sql    --> Interface publica (declarations)
PKG_{MODULO}_BODY.sql    --> Implementacao (logica de negocio)
PRC_{ACAO}.sql           --> Procedures standalone
FNC_{CALCULO}.sql        --> Functions standalone
TRG_{TABELA}_{EVENTO}.sql --> Triggers
VW_{CONSULTA}.sql        --> Views
```

### 2. Oracle Database - Camada de Dados

O Oracle e o unico SGBD suportado pelo TAX ONE.
O modelo de dados e extenso, refletindo a complexidade da legislacao fiscal brasileira.

**Caracteristicas:**
- Centenas de tabelas por modulo
- Particionamento por periodo (competencia/ano) em tabelas de grande volume
- Materialized Views para consultas de apuracao e relatorios
- Indices compostos otimizados para padroes de acesso fiscal
- Sequences para numeracao de documentos e registros
- Constraints de integridade referencial

### 3. PowerBuilder - Interface Desktop

PowerBuilder e a tecnologia de frontend desktop do TAX ONE.
A interface e baseada em DataWindows que se conectam diretamente ao Oracle.

**Componentes:**
- **Windows:** Telas de cadastro, consulta, processamento
- **DataWindows:** Componentes de grid/formulario com SQL embutido
- **User Objects:** Componentes reutilizaveis de interface
- **Scripts de Evento:** Logica de interface (open, close, clicked, etc.)
- **Menus:** Navegacao e atalhos

### 4. Java - Componentes de Integracao

Java e usado para componentes de integracao e funcionalidades web.

**Componentes:**
- **Web Services:** Comunicacao com SEFAZ (NFe, CTe, MDFe)
- **DAOs:** Acesso a dados Oracle via JDBC
- **Services:** Logica de integracao e orquestracao
- **Batch Jobs:** Processamentos schedulados
- **REST APIs:** Integracoes modernas com sistemas externos

---

## Modulos Funcionais

| Modulo | Descricao | Packages Principais |
|--------|-----------|---------------------|
| **Apuracao** | Apuracao de impostos por periodo | PKG_APURACAO_* |
| **Obrigacoes** | Geracao de obrigacoes acessorias | PKG_OBRIGACAO_* |
| **Cadastro** | Notas fiscais, participantes, produtos | PKG_CADASTRO_* |
| **Importacao** | Importacao de XMLs, arquivos TXT/CSV | PKG_IMPORTACAO_* |
| **Calculo** | Calculos tributarios e fiscais | PKG_CALCULO_* |
| **Consulta** | Views e consultas otimizadas | PKG_CONSULTA_* |
| **Relatorios** | Relatorios fiscais e gerenciais | PKG_RELATORIO_* |
| **Integracao** | Web services e APIs externas | PKG_INTEGRACAO_* |

---

## Fluxo Tipico de Processamento

```
1. IMPORTACAO: Dados entram via importacao de XML/TXT ou cadastro manual (PowerBuilder)
2. VALIDACAO: PL/SQL valida regras fiscais (CFOP, CST, NCM, aliquotas)
3. CALCULO: PL/SQL calcula impostos conforme legislacao vigente
4. ESCRITURACAO: Dados sao escriturados nas tabelas de movimento
5. APURACAO: PL/SQL consolida impostos por periodo (mensal/trimestral/anual)
6. OBRIGACOES: PL/SQL gera arquivos de obrigacoes acessorias (SPED, GIA, etc.)
7. INTEGRACAO: Java transmite obrigacoes para orgaos governamentais
```

---

## Ambientes

| Ambiente | Uso | Observacao |
|----------|-----|------------|
| DEV | Desenvolvimento | Dados de teste |
| QA | Testes e validacao | Dados simulados |
| HML | Homologacao | Dados de producao anonimizados |
| PRD | Producao | Dados reais de clientes |

---

## Controle de Versao e Trabalho

- **Codigo-fonte:** GitHub (repositorios por modulo/componente)
- **Work Items:** Azure DevOps (bugs, user stories, tasks)
- **CI/CD:** Processos de deploy manuais com scripts SQL
- **Testes:** Sem framework automatizado - validacao manual em QA
