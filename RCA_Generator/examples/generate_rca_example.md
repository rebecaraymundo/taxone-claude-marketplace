# Exemplo de Uso: Sistema RCA Generation Agents

Este documento demonstra como usar o sistema de agentes para gerar relatórios de RCA automaticamente.

## 🎯 Cenário: Incidente Tax One INC20260413-2

**Situação**: Incidente crítico de lentidão nos processamentos SPED/ECD do Tax One  
**Meta**: Gerar RCA completo com análise técnica, impacto ao cliente e ações preventivas

## 📋 Pré-requisitos

### 1. Configuração das Credenciais
```bash
# Azure DevOps
export ADO_PAT="your_azure_devops_personal_access_token"

# Zendesk
export ZENDESK_API_TOKEN="your_zendesk_api_token"
export ZENDESK_EMAIL="your_email@thomsonreuters.com"

# GitHub (com SAML SSO autorizado)
export GITHUB_TOKEN="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"
```

### 2. Verificação de Acesso
```bash
# Testar Azure DevOps
az boards work-item list --org https://dev.azure.com/thomsonreuters --project "Tax One" --top 1

# Testar Zendesk
curl -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" \
     https://thomsonreuters.zendesk.com/api/v2/tickets.json?per_page=1

# Testar GitHub
curl -H "Authorization: token $GITHUB_TOKEN" \
     https://api.github.com/repos/tr/taxone_dw
```

## 🚀 Execução Passo a Passo

### Método 1: Orquestração Completa (Recomendado)

```bash
claude --agent rca_generator_orchestrator \
  --config config/rca_system_config.json \
  "Gerar RCA completo para o incidente INC20260413-2 - TAX ONE - Lentidão nos processos SPED/ECD ocorrido em 13 Abr 2026"
```

**Output Esperado**:
```
🎯 Iniciando geração de RCA para INC20260413-2
📊 Coletando dados do Azure DevOps...
🎫 Analisando impacto no Zendesk...
🔍 Executando análise técnica do repositório Tax One...
🔄 Correlacionando dados de múltiplas fontes...
📝 Gerando relatório RCA final...
✅ RCA gerado com sucesso: reports/INC20260413-2/RCA_Report_INC20260413-2_Final.md
```

### Método 2: Execução de Agentes Individuais

#### Passo 1: Análise Azure DevOps
```bash
claude --agent azure_devops_incident_searcher \
  "Buscar todos os dados relacionados ao incidente INC20260413-2 incluindo work items, timeline e contexto técnico"
```

#### Passo 2: Análise Zendesk
```bash
claude --agent zendesk_connector \
  "Analisar impacto ao cliente para incidente INC20260413-2 no período de 13-14 Abr 2026, focando em clientes Tax One SPED/ECD"
```

#### Passo 3: Análise Técnica Tax One
```bash
claude --agent taxone_repository_analyzer \
  "Analisar repositório tr/taxone_dw para identificar causa raiz do incidente INC20260413-2 de 13 Abr 2026, focando em procedures SPED/ECD e problemas de locking"
```

#### Passo 4: Geração do RCA
```bash
claude --agent rca_generator_orchestrator \
  --input-sources "ado_analysis.json,zendesk_analysis.json,repo_analysis.json" \
  "Compilar dados coletados e gerar RCA final para INC20260413-2"
```

## 📊 Resultados Esperados

### Estrutura de Arquivos Gerados
```
reports/INC20260413-2/
├── RCA_Report_INC20260413-2_Final.md          # RCA principal
├── Azure_DevOps_Analysis.json                 # Dados técnicos ADO
├── Zendesk_Customer_Impact.json               # Dados impacto cliente
├── Tax_One_Technical_Analysis.json            # Análise técnica código
├── Timeline_Correlation.json                  # Timeline consolidada
└── Evidence_Package/
    ├── code_snippets/                         # Trechos código problemático
    ├── customer_communications/               # Comunicações cliente
    └── technical_logs/                        # Logs técnicos
```

### Conteúdo do RCA Final
O RCA gerado incluirá automaticamente:

#### ✅ Cabeçalho Executivo
- **ID do Incidente**: INC20260413-2
- **Serviço Impactado**: ONESOURCE Tax One (SPED/ECD)
- **27 Clientes Afetados**: Quantificação automática via Zendesk
- **Timeline**: 13 Abr 2026, 17:02–21:54 BRT

#### ✅ Causa Raiz Técnica
- **Mecanismo**: Implementação inadequada DBMS_LOCK.ALLOCATE_UNIQUE
- **Arquivo**: SAF_SPED_CONTABIL_FPROC.pck
- **Query Problemática**: `SELECT LOCKID FROM DBMS_LOCK_ALLOCATED WHERE NAME = :B1 FOR UPDATE`
- **Evidência**: ServiceNow INC1240692 correlacionado automaticamente

#### ✅ Tabelas Estruturadas

**Causas Contribuintes**:
| CC | Descrição | Evidência | Status |
|----|-----------|-----------|---------|
| CC1 | Implementação inadequada do DBMS_LOCK.ALLOCATE_UNIQUE | Código analisado no repositório | Confirmado |
| CC2 | Arquitetura não-SaaS para múltiplos clientes | 27 clientes causaram saturação | Confirmado |

**Ações Preventivas**:
| ID | Ação | Responsável | Prazo | Status |
|----|------|-------------|-------|---------|
| P1 | Remover DBMS_LOCK do Tax One | Jorge Washington | 15 Abr 2026 | Acordado |
| P2 | Implementar testes de carga | Equipe QA | 22 Abr 2026 | Acordado |

### Métricas de Qualidade Automáticas

O sistema valida automaticamente:
- ✅ **Timeline Consistency**: Eventos correlacionados entre fontes
- ✅ **Evidence Cross-Reference**: Múltiplas fontes confirmam causa raiz
- ✅ **Customer Impact Quantified**: 27 clientes via Zendesk + ADO
- ✅ **Technical Root Cause**: Código específico identificado
- ✅ **Actionable Items**: Ações em formato SMART com responsáveis

## 🔧 Troubleshooting

### Problema: Falha de Autenticação GitHub
```bash
# Verificar se SAML SSO está autorizado
curl -H "Authorization: token $GITHUB_TOKEN" \
     https://api.github.com/user/orgs

# Se não aparecer "tr", re-autorizar em:
# https://github.com/settings/tokens
```

### Problema: Zendesk sem Resultados
```bash
# Verificar busca manual
curl -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" \
     "https://thomsonreuters.zendesk.com/api/v2/search.json?query=created>2026-04-13%20Tax%20One"
```

### Problema: Azure DevOps sem Work Items
```bash
# Verificar projeto correto
az boards query --org https://dev.azure.com/thomsonreuters \
  --project "Tax One" \
  --wiql "SELECT [System.Id] FROM WorkItems WHERE [System.Title] CONTAINS 'INC20260413'"
```

## 📈 Exemplo de Output Real

### Console Output Durante Execução
```
🎯 RCA Generation Started for INC20260413-2
📊 [1/4] Azure DevOps Analysis...
   ✓ Found work item: Bug #892 - TAX ONE Lentidão SPED/ECD
   ✓ Timeline extracted: 17:02-21:54 BRT
   ✓ 15 related work items identified

🎫 [2/4] Zendesk Customer Impact Analysis...
   ✓ Found 13 customer tickets
   ✓ Identified 27 affected customers
   ✓ Enterprise customers: Yara, Lojas União
   ✓ Impact timeline: 17:02-21:30 BRT

🔍 [3/4] Tax One Repository Analysis...
   ✓ Repository access: tr/taxone_dw ✓
   ✓ Found problematic file: SAF_SPED_CONTABIL_FPROC.pck
   ✓ Identified root cause: DBMS_LOCK.ALLOCATE_UNIQUE
   ✓ Historical pattern: 3 similar deadlock issues

🔄 [4/4] RCA Generation and Correlation...
   ✓ Timeline correlation: 100% match
   ✓ Root cause triangulation: confirmed
   ✓ Customer impact quantified: 27 customers
   ✓ Technical evidence: code snippets included

📝 RCA Report Generated Successfully!
   📂 Location: reports/INC20260413-2/RCA_Report_INC20260413-2_Final.md
   📊 Quality Score: 98/100
   ⏱️  Generation Time: 4m 23s
   🔍 Evidence Sources: 3 (ADO, Zendesk, GitHub)
   ✅ All required sections completed
```

### Fragmento do RCA Gerado
```markdown
## Causa Raiz

**Status:** Confirmada  
**Código da Causa:** Falha de Código/Design

**Mecanismo de Falha:**  
O Tax One executava lógica de aplicação com implementação inadequada do 
DBMS_LOCK.ALLOCATE_UNIQUE na procedure SAF_SPED_CONTABIL_FPROC. Uma demanda 
ECD implementada anteriormente não seguiu melhores práticas...

**Evidências de Suporte da Causa Raiz:**
- ✓ **Repositório GitHub**: tr/taxone_dw - SAF_SPED_CONTABIL_FPROC.pck
- ✓ **ServiceNow**: INC1240692 - "enq: TX - row lock contention"
- ✓ **Query Problemática**: `SELECT LOCKID FROM DBMS_LOCK_ALLOCATED WHERE NAME = :B1 FOR UPDATE`
- ✓ **Impacto Cliente**: 27 clientes afetados (Zendesk tickets correlacionados)
- ✓ **Timeline**: Correlação perfeita entre ADO, Zendesk e código
```

## 🎉 Próximos Passos

Após a geração bem-sucedida do RCA:

1. **Review Manual**: Validar dados técnicos e timeline
2. **Stakeholder Review**: Distribuir para equipe técnica
3. **Action Tracking**: Criar tasks no Azure DevOps para ações
4. **Knowledge Base**: Adicionar RCA ao repositório de conhecimento

---
**Exemplo**: Sistema RCA Generation Agents  
**Cenário**: INC20260413-2 Tax One  
**Status**: Template de execução validado  
**Criado**: 14 Abr 2026