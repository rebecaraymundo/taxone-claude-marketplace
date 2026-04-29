# Guia de Agentes Disponíveis - Sistema RCA

## ⚠️ CORREÇÃO IMPORTANTE

Os agentes documentados anteriormente (`rca_generator_orchestrator`, `azure_devops_incident_searcher`, etc.) são **templates conceituais**, não agentes implementados no sistema.

## 🤖 Agentes Realmente Disponíveis

### 1. **general-purpose** - Agente Principal
**Uso:** Análise completa de RCA, correlação multi-fonte, geração de relatórios

#### Exemplos Práticos:
```bash
# RCA Completo INC20260413-2
claude --agent general-purpose "Gerar RCA completo para INC20260413-2 - TAX ONE - Lentidão nos processos:

FONTES A USAR:
- Azure DevOps: Timeline técnica e work items
- Zendesk: 27 clientes impactados (Shopee, Yara, Lojas União)
- GitHub tr/taxone_dw: Análise SAF_SPED_CONTABIL_FPROC.pck
- MS Teams: Reuniões 13/04 (1h51min) e 14/04 (5h39min)
- ServiceNow: INC1240692 correlação

ANÁLISE REQUERIDA:
1. Timeline consolidada 13-14/04
2. Causa raiz técnica: DBMS_LOCK.ALLOCATE_UNIQUE
3. Problemas não resolvidos: PROD03 sem diagnóstico
4. Formato Thomson Reuters com tabelas estruturadas

Token GitHub: [SEU_TOKEN_AQUI]"
```

```bash
# Análise Correlacional Multi-Fonte
claude --agent general-purpose "Confrontar dados do incidente INC20260413-2:

ANÁLISE CORRELACIONAL:
- MS Teams (problemas técnicos identificados) vs Zendesk (problemas reportados clientes)
- Código GitHub (evidências técnicas) vs Reuniões (consensos SMEs)
- Timeline técnica vs Timeline clientes
- Gaps e inconsistências identificar

OBJETIVO: Identificar problemas não diagnosticados, correlações perdidas, evidências conflitantes"
```

### 2. **Explore** - Análise Especializada de Repositórios
**Uso:** Investigação profunda de código, busca de padrões técnicos específicos

#### Exemplos Práticos:
```bash
# Análise Tax One Repository
claude --agent Explore "Investigar repositório GitHub tr/taxone_dw relacionado ao INC20260413-2:

BUSCAR ESPECIFICAMENTE:
- SAF_SPED_CONTABIL_FPROC.pck: Problemas DBMS_LOCK.ALLOCATE_UNIQUE
- Query: SELECT LOCKID FROM DBMS_LOCK_ALLOCATED WHERE NAME = :B1 FOR UPDATE
- Commits 13-14/04/2026: Mudanças coincidentes com incidente
- lib_proc: Alterações mencionadas por Cristiane Fugii
- Padrões deadlock históricos: MFS94867, MFS842943

ANÁLISE TÉCNICA:
- Root cause identification
- Performance patterns
- Architecture issues
- Historical correlations

Token: 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"
```

```bash
# Busca de Padrões Problemáticos
claude --agent Explore "Analisar código Tax One para padrões arquiteturais problemáticos:

PADRÕES A BUSCAR:
- DBMS_LOCK usage em todos os arquivos
- FOR UPDATE queries problemáticas
- Deadlock patterns históricos
- Multi-tenant scalability issues
- Performance anti-patterns

REPOSITÓRIO: tr/taxone_dw
FOCO: Escalabilidade SaaS e arquitetura moderna"
```

### 3. **Plan** - Planejamento de Soluções
**Uso:** Criar planos de implementação, estratégias de correção, roadmaps técnicos

#### Exemplos Práticos:
```bash
# Plano de Correção Arquitetural
claude --agent Plan "Criar plano detalhado para correção dos problemas identificados no INC20260413-2:

PROBLEMAS A CORRIGIR:
1. DBMS_LOCK.ALLOCATE_UNIQUE inadequado (PROD01 confirmado)
2. Causa raiz desconhecida PROD03 (análise incompleta)
3. lib_proc changes não investigadas
4. Falta monitoramento correlacionado ambientes
5. Processo validação resolução inadequado

PLANO DEVE INCLUIR:
- Análise de riscos por correção
- Timeline de implementação
- Recursos necessários
- Testes obrigatórios
- Critérios de sucesso
- Rollback plans

ARQUITETURA ALVO: SaaS multi-tenant escalável"
```

## 🎯 Fluxo de Trabalho Recomendado

### Fase 1: Análise Inicial
```bash
# Use general-purpose para análise completa
claude --agent general-purpose "Analisar incidente [ID] com dados Azure DevOps + Zendesk + GitHub"
```

### Fase 2: Investigação Técnica Profunda  
```bash
# Use Explore para detalhes técnicos
claude --agent Explore "Investigar repositório específico para evidências técnicas do incidente"
```

### Fase 3: Planejamento de Correções
```bash
# Use Plan para estratégia de correção
claude --agent Plan "Criar plano de correção baseado nos problemas identificados"
```

## 📋 Templates de Prompt por Tipo de Análise

### Para Azure DevOps + Zendesk
```bash
claude --agent general-purpose "Extrair e correlacionar dados:
AZURE DEVOPS: Timeline, work items, deployment tracking
ZENDESK: Customer impact, tickets, escalations
CORRELAÇÃO: Timeline unified, impact quantification
FORMATO: Thomson Reuters RCA template"
```

### Para GitHub Repository Analysis
```bash
claude --agent Explore "Análise repositório [REPO]:
BUSCAR: [specific files/patterns]
ANALISAR: [technical issues]
CORRELACIONAR: [incident timeline]
TOKEN: [github_token]"
```

### Para Planning/Solutions
```bash
claude --agent Plan "Criar plano para [OBJECTIVE]:
PROBLEMAS: [identified issues]
CONSTRAINTS: [technical/business]
TIMELINE: [deadline requirements]
RESOURCES: [available team/tools]"
```

## ✅ Correção Aplicada

### Antes (Incorreto):
```bash
# Agentes que não existem
claude --agent rca_generator_orchestrator "..."
claude --agent azure_devops_incident_searcher "..."
```

### Depois (Correto):
```bash
# Agentes reais disponíveis
claude --agent general-purpose "Gerar RCA completo com dados Azure DevOps + Zendesk + GitHub..."
claude --agent Explore "Analisar repositório para evidências técnicas específicas..."
claude --agent Plan "Criar plano de correção dos problemas identificados..."
```

---
**Documento**: Guia Agentes Disponíveis  
**Status**: Corrigido para agentes reais  
**Data**: 15 Abr 2026  
**Uso**: Substitui referências aos agentes conceituais por agentes implementados