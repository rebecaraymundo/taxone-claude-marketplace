# Repositórios Git Disponíveis - Thomson Reuters

## 📅 **Atualizado em**: 29 Abril 2026

Este documento lista todos os repositórios Git da Thomson Reuters aos quais temos acesso para análise técnica e geração de RCAs.

---

## 🔄 **Conectores OCC (Oracle Cloud Commerce)**

### **Backend**
- **Nome**: Conector OCC - Backend
- **URL**: https://github.com/tr/msaf_dfe-ora-cloud-unificado
- **Descrição**: Backend do conector para Oracle Cloud Commerce
- **Uso RCA**: Análise de problemas de integração OCC, performance de APIs, logs de transações

### **Frontend**
- **Nome**: Conector OCC - FrontEnd  
- **URL**: https://github.com/tr/msaf_dfe-ora-cloud-frontend-2-0
- **Descrição**: Frontend v2.0 do conector Oracle Cloud Commerce
- **Uso RCA**: Análise de problemas de UI, integração frontend-backend, experiência do usuário

---

## 🔌 **Conectores ERP Multi-Sistema**

### **Conectores Unificados**
- **Nome**: Conectores SAP/EBS/FixaX/Infor/Retail
- **URL**: https://github.com/tr/msaf-interfaces-erp_dfe-conectores-conectores
- **Descrição**: Conectores para múltiplos sistemas ERP (SAP, Oracle EBS, FixaX, Infor, Retail)
- **Uso RCA**: 
  - Análise de falhas de integração ERP
  - Problemas de sincronização de dados
  - Performance de conectores específicos
  - Mapeamento de dados entre sistemas

---

## 📊 **DFE (Documento Fiscal Eletrônico)**

### **Sistema Principal DFE3**
- **Nome**: DFE - Sistema Principal
- **URL**: https://github.com/tr/MSaf_DFE3
- **Descrição**: Sistema principal de Documento Fiscal Eletrônico versão 3
- **Uso RCA**:
  - Análise de problemas na geração de documentos fiscais
  - Falhas na comunicação com SEFAZ
  - Performance no processamento de NFe/NFCe/CTe
  - Problemas de validação fiscal

---

## 🎯 **Repositórios Existentes (TAX ONE)**

### **TAX ONE Principal**
- **Nome**: TAX ONE Data Warehouse
- **URL**: https://github.com/tr/taxone_dw
- **Descrição**: Sistema principal TAX ONE - Data Warehouse fiscal
- **Uso RCA**: Análise de problemas SPED, procedures Oracle, performance de consultas

---

## 🔍 **Análise por Tipo de Incidente**

### **Problemas de Performance**
- **Repositórios**: `tr/taxone_dw`, `tr/MSaf_DFE3`, `tr/msaf_dfe-ora-cloud-unificado`
- **Foco**: Procedures Oracle, queries lentas, gargalos de API

### **Problemas de Integração**
- **Repositórios**: `tr/msaf-interfaces-erp_dfe-conectores-conectores`, `tr/msaf_dfe-ora-cloud-*`
- **Foco**: Falhas de conectores, sincronização, mapeamento de dados

### **Problemas Fiscais**
- **Repositórios**: `tr/MSaf_DFE3`, `tr/taxone_dw`
- **Foco**: Validações fiscais, comunicação SEFAZ, geração de documentos

### **Problemas de Frontend**
- **Repositórios**: `tr/msaf_dfe-ora-cloud-frontend-2-0`
- **Foco**: Interface de usuário, integração com APIs, experiência do cliente

---

## 🤖 **Uso nos Agentes RCA**

### **Azure DevOps Incident Searcher**
- Pode correlacionar work items com commits nos repositórios listados
- Timeline técnica baseada em histórico Git

### **Tax One Repository Analyzer**
- **EXPANDIDO**: Agora analisa todos os repositórios TR disponíveis
- Análise técnica cross-repository para incidentes multi-sistema

### **RCA Generator Orchestrator**
- Correlação automática entre repositórios relacionados
- Análise de dependências entre sistemas (OCC ↔ DFE ↔ TAX ONE)

---

## 🔄 **Próximas Integrações**

### **Em Análise**
- Verificar se há outros repositórios TR disponíveis
- Mapear dependências entre sistemas
- Configurar análise automatizada multi-repositório

### **Melhorias Planejadas**
- Script para clonagem automática de todos os repositórios
- Indexação de código para busca rápida
- Correlação automática de commits por período de incidente

---

**📊 Total de Repositórios**: 5 repositórios Thomson Reuters  
**🔧 Sistemas Cobertos**: TAX ONE, DFE, OCC, Conectores ERP  
**📈 Capacidade RCA**: Análise técnica multi-sistema expandida

---

**Última Atualização**: 29 Abr 2026 - Adicionados 4 novos repositórios OCC/DFE/Conectores  
**Responsável**: Jorge Washington Silva Neto via Claude Code AI Assistant