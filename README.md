# Incidents RCA Generator - Thomson Reuters

Sistema avançado de geração automática de **Root Cause Analysis (RCA)** para incidentes da Thomson Reuters, com suporte a múltiplos produtos e integração multi-sistema.

## 🎯 **Visão Geral**

Este repositório contém um sistema completo para:
- **🤖 Geração automática de RCAs** usando 4 agentes especializados
- **📊 Análise técnica multi-produto** (6 produtos Thomson Reuters)
- **🔗 Integração de dados** de Azure DevOps, Zendesk, GitHub e MS Teams
- **📋 Templates padronizados** seguindo metodologias ITIL e Thomson Reuters

---

## 🏗️ **Estrutura do Projeto**

```
Incidents_RCA_Generator/
├── README.md                    # Este arquivo
├── RCA_Generator/              # 🎯 Sistema principal RCA
│   ├── agents/                 # 🤖 4 agentes automatizados
│   ├── config/                 # ⚙️ Configurações e mapeamento de produtos
│   ├── templates/              # 📋 Templates RCA padronizados
│   ├── examples/               # 💡 Exemplos práticos
│   ├── Digital_Banking/        # 🏦 Casos Digital Banking
│   └── Tax_One/               # 📊 Casos TAX ONE (incluindo INC20260413-2)
├── taxone-support-dev/         # 🔧 Plugin Claude Code (legacy)
└── scripts/                    # 🚀 Automação GitHub
    ├── create_github_repo.sh
    └── quick_github_create.sh
```

---

## 🤖 **Sistema de Agentes RCA**

### **Agentes Especializados**
1. **🔍 Azure DevOps Incident Searcher** - Extração de dados ADO
2. **📞 Zendesk Connector** - Análise de impacto ao cliente  
3. **💻 Repository Analyzer** - Análise técnica multi-repositório
4. **🎯 RCA Generator Orchestrator** - Orquestração e geração final

### **Produtos Suportados** (6 produtos Thomson Reuters)
- **📊 TAX ONE**: `tr/taxone_dw` (SQL/Oracle fiscal)
- **🏪 OCC Backend**: `tr/msaf_dfe-ora-cloud-unificado` (Java)
- **🖥️ OCC Frontend**: `tr/msaf_dfe-ora-cloud-frontend-2-0` (JavaScript)  
- **🔌 Conectores ERP**: `tr/msaf-interfaces-erp_dfe-conectores-conectores` (Java multi-ERP)
- **📄 DFE Sistema**: `tr/MSaf_DFE3` (Java documentos fiscais)
- **🏢 Mastersaf Core**: `tr/mastersaf_core` (PowerBuilder base)

---

## 🚀 **Como Usar**

### **Método Automático (Recomendado)**
```bash
# Configure as credenciais
export ADO_PAT="your_azure_devops_token"
export ZENDESK_API_TOKEN="your_zendesk_token"  
export GITHUB_TOKEN="ghp_your_github_token"

# Gere RCA automaticamente
claude --agent rca_generator_orchestrator \
  "Gerar RCA para incidente INC20260429 - [PRODUTO] - [DESCRIÇÃO]"
```

### **Resultado Automático** ✅
- **Timeline técnica** correlacionada entre múltiplas fontes
- **Impacto ao cliente** quantificado via Zendesk
- **Análise técnica** baseada em código dos 6 repositórios TR
- **Causa raiz** identificada com evidências específicas
- **Ações SMART** com responsáveis e prazos definidos

---

## 📋 **Casos Reais Incluídos**

### **🔍 INC20260413-2 - TAX ONE** (Caso Completo)
- **Problema**: Lentidão em processos SPED
- **Causa Raiz**: DBMS_LOCK.ALLOCATE_UNIQUE inadequado  
- **Impacto**: 27 clientes afetados
- **Status**: ✅ Resolvido com múltiplas evidências técnicas

### **🏦 INC20260413 - Digital Banking** 
- **Problema**: Honorários Boletos com falha
- **Causa**: Movimentação de pod Kubernetes
- **Status**: ✅ Documentado como referência

---

## ⚙️ **Configuração Rápida**

### **1. Clonar o repositório**
```bash
git clone https://github.com/rebecaraymundo/incidents-rca-generator.git
cd incidents-rca-generator
```

### **2. Configurar tokens**
```bash
# Azure DevOps
export ADO_PAT="your_ado_token"

# Zendesk  
export ZENDESK_API_TOKEN="your_zendesk_token"
export ZENDESK_EMAIL="your_email@thomsonreuters.com"

# GitHub (com SAML SSO autorizado)
export GITHUB_TOKEN="ghp_your_token"
```

### **3. Verificar configuração**
```bash
# Testar conectividade
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
```

---

## 📊 **Métricas e Benefícios**

### **⚡ Performance**
- **Tempo de geração**: 5-15 minutos (vs. horas manual)
- **Precisão**: Correlação automática multi-fonte
- **Cobertura**: 6 produtos TR vs. apenas TAX ONE anterior

### **🎯 Qualidade**
- **Completude**: Todas as seções obrigatórias preenchidas
- **Evidências**: Extração automática de código, logs e dados cliente
- **Consistência**: Validação automática de formato e conteúdo
- **Rastreabilidade**: Links diretos para work items, commits, tickets

---

## 🔧 **Integração Claude Code**

### **Plugin TAX ONE (Incluído)**
```bash
# Instalar plugin legacy
claude --plugin-dir ./taxone-support-dev

# Comandos disponíveis
/taxone-auto-fix 1083740
/taxone-bug-fix 1058668  
/taxone-us-implement 1079124
```

---

## 📚 **Documentação Adicional**

- **[Sistema de Agentes](./RCA_Generator/agents/README.md)** - Detalhes técnicos dos agentes
- **[Configuração](./RCA_Generator/config/)** - Mapeamento de produtos e configurações
- **[Templates](./RCA_Generator/templates/)** - Templates RCA padronizados
- **[Exemplos](./RCA_Generator/examples/)** - Casos práticos e guias de uso

---

## 🔒 **Segurança e Compliance**

- ✅ **Tokens protegidos** via .gitignore
- ✅ **Dados sensíveis** não expostos
- ✅ **SAML SSO** GitHub configurado
- ✅ **Logs auditáveis** para compliance ITIL

---

## 🤝 **Contribuição**

Para adicionar novos produtos ou melhorar o sistema:

1. **Fork** o repositório
2. **Configure** novo produto em `RCA_Generator/config/`
3. **Teste** com casos reais
4. **Documente** no formato estabelecido
5. **Abra PR** para revisão

---

## 📞 **Contatos e Suporte**

- **🎯 Problem Manager**: Adriana Dorigao
- **🔧 SMEs Técnicos**: Jorge Washington Silva Neto, Alceste Siqueira Junior
- **⚙️ Operations**: Bruno Fornari
- **🤖 AI Assistant**: Claude Code (desenvolvimento e manutenção)

---

## 📜 **Licença**

**Uso interno Thomson Reuters** - Todos os direitos reservados.

**Última Atualização**: 29 Abr 2026 - Renomeação para Incidents RCA Generator  
**Versão**: 3.0 - Sistema Multi-Produto Expandido