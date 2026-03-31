# taxone-doc-gen Skill

Geracao de documentacao tecnica e funcional para features e modulos do TAX ONE.
Analisa codigo-fonte PL/SQL, estrutura Oracle, objetos PowerBuilder e componentes Java
para gerar documentacao padronizada em markdown.

---

## Visao Geral

Este skill analisa o codigo-fonte de uma feature ou modulo do TAX ONE e gera
documentacao completa salva em `${CLAUDE_PLUGIN_ROOT}/knowledge/features/[feature].md`.

A documentacao gerada serve como base de conhecimento para os demais skills
(taxone-bug-fix, taxone-compound) e agentes (taxone-developer, taxone-reviewer, taxone-dba).

---

## Processo de Geracao

### Fase 1: Identificacao do Escopo

1. Receber nome da feature ou modulo do usuario
2. Identificar packages PL/SQL relacionados (PKG_{MODULO}_*)
3. Identificar tabelas, views, triggers e sequences do modulo
4. Identificar telas PowerBuilder (se aplicavel)
5. Identificar classes Java (se aplicavel)

### Fase 2: Analise do Codigo-Fonte

**PL/SQL (fonte primaria de logica de negocio):**

1. **Package Specs:** Extrair interface publica (procedures, functions, types, constants, exceptions)
2. **Package Bodies:** Analisar logica de negocio, fluxos de processamento, regras fiscais
3. **Procedures Standalone:** Mapear entradas, saidas, dependencias
4. **Functions:** Documentar calculos, formulas fiscais, validacoes
5. **Triggers:** Identificar eventos, tabelas, logica de auditoria/validacao
6. **Views:** Documentar joins, filtros, proposito da consulta

**Oracle (modelo de dados):**

1. **Tabelas:** Colunas, tipos, constraints, particionamento
2. **Indices:** Estrategia de indexacao, colunas cobertas
3. **Materialized Views:** Refresh strategy, query rewrite
4. **Sequences:** Numeracao, uso

**PowerBuilder (interface de usuario):**

1. **DataWindows:** SQL fonte, colunas apresentadas, filtros
2. **Windows:** Telas, eventos, navegacao
3. **User Objects:** Componentes reutilizaveis

**Java (integracao):**

1. **DAOs:** Acesso a dados, queries
2. **Services:** Logica de integracao, web services
3. **Batch:** Processamentos em lote

### Fase 3: Montagem do Documento

Gerar documento markdown seguindo o template abaixo.

### Fase 4: Salvamento e Apresentacao

1. Salvar em `${CLAUDE_PLUGIN_ROOT}/knowledge/features/[feature-slug].md`
2. Usar slug em lowercase com hifens (ex: `apuracao-icms.md`, `importacao-xml.md`)
3. Apresentar resumo do que foi documentado

---

## Template do Documento

```markdown
# {Nome da Feature}

> Documentacao gerada automaticamente via taxone-doc-gen
> Data: {data}
> Modulo: {modulo}

## Visao Geral

[Descricao funcional da feature - o que faz, para quem, quando e usada]

## Arquitetura

### Diagrama de Componentes

```
[Diagrama ASCII dos componentes e suas interacoes]
```

### Packages PL/SQL

| Package | Tipo | Descricao |
|---------|------|-----------|
| PKG_XXX | Spec/Body | [descricao] |

### Procedures e Functions Principais

| Nome | Tipo | Entrada | Saida | Descricao |
|------|------|---------|-------|-----------|
| PRC_XXX | Procedure | [params] | [out params] | [descricao] |
| FNC_XXX | Function | [params] | [return type] | [descricao] |

## Modelo de Dados

### Tabelas Principais

| Tabela | Descricao | Volume Estimado | Particionamento |
|--------|-----------|-----------------|-----------------|
| TB_XXX | [descricao] | [volume] | [sim/nao] |

### Relacionamentos

```
[Diagrama ASCII de relacionamentos entre tabelas]
```

### Views

| View | Descricao | Tabelas Fonte |
|------|-----------|---------------|
| VW_XXX | [descricao] | [tabelas] |

## Fluxos de Processamento

### Fluxo Principal

1. [Passo 1]
2. [Passo 2]
3. [Passo n]

### Fluxos Alternativos

- **Cenario A:** [descricao]
- **Cenario B:** [descricao]

## Regras de Negocio

| # | Regra | Package/Procedure | Observacao |
|---|-------|-------------------|------------|
| RN01 | [descricao da regra] | PKG_XXX.PRC_YYY | [obs] |

## Calculos e Formulas

### {Nome do Calculo}

- **Formula:** [formula]
- **Implementacao:** `PKG_XXX.FNC_YYY`
- **Parametros:** [lista]
- **Excecoes:** [casos especiais]

## Interface (PowerBuilder)

### Telas

| Tela | Descricao | DataWindows |
|------|-----------|-------------|
| W_XXX | [descricao] | [DWs usados] |

## Integracao (Java)

### Servicos

| Classe | Descricao | Endpoint/Trigger |
|--------|-----------|------------------|
| XxxService | [descricao] | [endpoint] |

## Cenarios de Bug Frequentes

| # | Cenario | Causa Comum | Package Afetado |
|---|---------|-------------|-----------------|
| BG01 | [descricao] | [causa] | PKG_XXX |

## Dependencias

### Dependencias Internas
- [Outros modulos do TAX ONE que esta feature depende]

### Dependencias Externas
- [Sistemas externos, web services, arquivos]

## Historico de Mudancas

| Data | Descricao | Referencia |
|------|-----------|------------|
| {data} | Documentacao inicial gerada | taxone-doc-gen |
```

---

## Diretrizes de Qualidade

1. **Codigo como fonte primaria:** Sempre analisar o codigo real, nao assumir comportamento
2. **Portugues:** Toda documentacao deve ser escrita em portugues
3. **Precisao:** Nomes de packages, procedures e tabelas devem ser exatos (copiar do codigo)
4. **Pragmatismo:** Focar no que e util para debug e manutencao, nao em documentacao exaustiva
5. **Diagramas ASCII:** Usar diagramas simples em texto para visualizar fluxos e relacionamentos
6. **Cenarios de bug:** Incluir problemas conhecidos/recorrentes para acelerar diagnosticos futuros

---

## Exemplos de Uso

```
/taxone-doc-gen Apuracao ICMS
/taxone-doc-gen Obrigacoes Acessorias - SPED Fiscal
/taxone-doc-gen Calculo de PIS/COFINS
/taxone-doc-gen Cadastro de Notas Fiscais
/taxone-doc-gen Importacao de XMLs
/taxone-doc-gen Relatorios Fiscais
```
