# RCA Generator - Root Cause Analysis Report Generator

## 🎯 Visão Geral
Este projeto contém templates, agentes especializados e ferramentas para geração **automatizada** de relatórios de Análise de Causa Raiz (RCA) padronizados para incidentes da Thomson Reuters.

### 🚀 Novidade: Sistema de Agentes Automatizado
O RCA Generator agora inclui um **sistema de 4 agentes especializados** que automatizam completamente o processo de geração de RCAs:
- **Azure DevOps Agent**: Extração automática de dados de incidentes
- **Zendesk Agent**: Análise de impacto ao cliente
- **Tax One Repository Agent**: Análise técnica de código
- **RCA Generator Orchestrator**: Orquestração e geração final

## Estrutura do Projeto

```
RCA_Generator/
├── README.md                 # Este arquivo
├── agents/                  # 🤖 Sistema de Agentes (NOVO!)
│   ├── README.md
│   ├── azure_devops_incident_searcher.md
│   ├── zendesk_connector.md
│   ├── taxone_repository_analyzer.md
│   └── rca_generator_orchestrator.md
├── config/                  # ⚙️ Configurações do sistema
│   └── rca_system_config.json
├── templates/               # Templates base para RCA
│   ├── rca_template_final.md
│   └── rca_format_guide.md
├── reports/                 # Relatórios RCA gerados
│   └── INC20260413-2/
├── examples/               # 📋 Exemplos e guias de uso
│   ├── INC20260401/
│   └── generate_rca_example.md
└── docs/                   # Documentação adicional
    ├── process_guide.md
    └── best_practices.md
```

## Como Usar

### 🤖 Método 1: Geração Automática (Recomendado)

#### Configuração Rápida
```bash
# Configure as credenciais necessárias
export ADO_PAT="your_azure_devops_token"
export ZENDESK_API_TOKEN="your_zendesk_token"
export GITHUB_TOKEN="ghp_..." # Com SAML SSO autorizado
```

#### Geração Automática Completa
```bash
claude --agent rca_generator_orchestrator \
  "Gerar RCA para incidente INC20260413-2 - TAX ONE - Lentidão nos processos"
```

**Resultado**: RCA completo em 5-15 minutos com:
- ✅ Dados do Azure DevOps automaticamente extraídos
- ✅ Impacto ao cliente quantificado via Zendesk
- ✅ Análise técnica do código (produtos Tax One)
- ✅ Timeline correlacionada entre múltiplas fontes
- ✅ Causa raiz identificada com evidências técnicas
- ✅ Ações preventivas e corretivas geradas automaticamente

### 📝 Método 2: Processo Manual (Tradicional)

1. Copie o template de `templates/rca_template_final.md`
2. Colete informações dos sistemas: Azure DevOps, Zendesk, GitHub
3. Preencha todas as seções seguindo o formato estabelecido
4. Salve o relatório em `reports/[INCIDENT_ID]/`

### 2. Seções Obrigatórias
- **Informações Básicas**: ID do Problema, Incidente, Status, etc.
- **Participantes**: Gerente de Problemas e SMEs Técnicos
- **Resultado**: Resumo da reunião RCA
- **Declaração do Problema**: Resumo detalhado e impacto
- **Timeline**: T0, Detecção, Escalação, Ações, Resolução
- **Causa Raiz**: Status, Código, Mecanismo, Evidências
- **Tabelas Estruturadas**:
  - Causas Contribuintes
  - Soluções Preventivas
  - Soluções Corretivas  
  - Melhorias
  - Ações (SMART)

### 3. Padrões de Qualidade
- Use tabelas para organizar informações complexas
- Inclua evidências específicas e técnicas
- Defina ações SMART com responsáveis e prazos
- Mantenha rastreabilidade com IDs de tasks e repositórios

## Templates Disponíveis

### Template Final (rca_template_final.md)
Template completo com todas as seções e tabelas estruturadas em português, baseado nos padrões Thomson Reuters.

## Relatórios Existentes

### INC20260413-2 - TAX ONE - Lentidão nos processos
- **Status**: Concluído
- **Causa Raiz**: DBMS_LOCK.ALLOCATE_UNIQUE inadequado
- **Impacto**: 27 clientes
- **Data**: 13 Abr 2026

## Melhores Práticas

1. **Coleta de Dados**: Sempre consulte múltiplas fontes (Azure DevOps, Zendesk, GitHub)
2. **Evidências**: Documente procedures específicas, commits, logs técnicos
3. **Timeline**: Use horários específicos com fuso horário
4. **Ações**: Defina responsáveis, prazos e IDs de tasks
5. **Revisão**: Valide com SMEs técnicos antes da finalização

## 🤖 Sistema de Agentes

### Agentes Disponíveis

| Agente | Função | Input | Output |
|--------|---------|-------|--------|
| **Azure DevOps Incident Searcher** | Extração de dados ADO | Incident ID | Timeline técnica, work items |
| **Zendesk Connector** | Análise impacto cliente | Incident date/time | Clientes afetados, escalações |
| **Tax One Repository Analyzer** | Análise técnica código | Incident context | Evidências técnicas, root cause |
| **RCA Generator Orchestrator** | Orquestração e RCA final | Dados correlacionados | RCA completo formatado |

### Vantagens do Sistema Automatizado

- ⚡ **Velocidade**: Gera RCAs em 5-15 minutos (vs. horas manual)
- 🎯 **Precisão**: Correlação automática entre múltiplas fontes
- 📊 **Completude**: Garante todas as seções obrigatórias preenchidas
- 🔍 **Evidências**: Extração automática de código, logs e dados cliente
- ✅ **Qualidade**: Validação automática de consistência e formato
- 🔄 **Reprodutibilidade**: Processo padronizado e documentado

### Produtos Suportados

- ✅ **Tax One/SPED**: Análise completa com repositório tr/taxone_dw
- ✅ **Produtos Genéricos**: ADO + Zendesk (sem análise repositório)
- 🔄 **Em Desenvolvimento**: Mastersaf, OneSource, Checkpoint

Para mais detalhes, consulte: [`agents/README.md`](agents/README.md)

## Contatos

- **Facilitador Principal**: Adriana Dorigao (Problem Manager)
- **SMEs Técnicos**: Jorge Washington Silva Neto, Alceste Siqueira Junior
- **Operations**: Bruno Fornari

---
**Última Atualização**: 14 Abr 2026  
**Versão**: 2.0 (Sistema de Agentes)  
**Responsável**: Claude Code AI Assistant