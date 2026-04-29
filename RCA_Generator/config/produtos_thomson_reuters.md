# Produtos Thomson Reuters - Mapeamento Técnico

## 📅 **Atualizado em**: 29 Abril 2026

Este documento mapeia cada **produto** Thomson Reuters com seu respectivo repositório Git e características técnicas para análise de incidentes.

---

## 🎯 **IMPORTANTE**
**Cada repositório representa um produto distinto da Thomson Reuters**. Esta informação é crucial para:
- Análises técnicas precisas em RCAs
- Correlação de problemas entre produtos relacionados
- Direcionamento correto dos agentes de análise

---

## 📊 **PRODUTO 1: TAX ONE**
### **Descrição**
Sistema de gestão fiscal e tributária, focado em SPED e obrigações fiscais brasileiras.

### **Repositório Git**
- **URL**: https://github.com/tr/taxone_dw
- **Nome**: `tr/taxone_dw`
- **Linguagem Principal**: SQL/Oracle PL/SQL

### **Características Técnicas**
- **Banco de Dados**: Oracle Database
- **Arquitetura**: Data Warehouse fiscal
- **Módulos**: SPED, ECD, EFD-PIS-COFINS, Datamart

### **Incidentes Típicos**
- Lentidão em procedures Oracle
- Problemas de locks (DBMS_LOCK.ALLOCATE_UNIQUE)
- Falhas na geração SPED
- Performance de consultas fiscais

---

## 🏪 **PRODUTO 2: OCC BACKEND**
### **Descrição**
Backend do conector para Oracle Cloud Commerce, responsável por integração de sistemas comerciais.

### **Repositório Git**
- **URL**: https://github.com/tr/msaf_dfe-ora-cloud-unificado
- **Nome**: `tr/msaf_dfe-ora-cloud-unificado`
- **Linguagem Principal**: Java

### **Características Técnicas**
- **Arquitetura**: Microserviços Java
- **Integração**: Oracle Cloud Commerce
- **APIs**: RESTful services

### **Incidentes Típicos**
- Falhas de integração OCC
- Performance de APIs
- Problemas transacionais
- Timeouts de conectividade

---

## 🖥️ **PRODUTO 3: OCC FRONTEND**
### **Descrição**
Frontend v2.0 do conector Oracle Cloud Commerce, interface de usuário para gestão comercial.

### **Repositório Git**
- **URL**: https://github.com/tr/msaf_dfe-ora-cloud-frontend-2-0
- **Nome**: `tr/msaf_dfe-ora-cloud-frontend-2-0`
- **Linguagem Principal**: JavaScript/Frontend

### **Características Técnicas**
- **Framework**: JavaScript moderno
- **Versão**: 2.0
- **Integração**: APIs do backend OCC

### **Incidentes Típicos**
- Problemas de interface de usuário
- Falhas de integração frontend-backend
- Experiência do usuário degradada
- Erros de renderização

---

## 🔌 **PRODUTO 4: CONECTORES ERP**
### **Descrição**
Conjunto de conectores para integração com múltiplos sistemas ERP (SAP, Oracle EBS, FixaX, Infor, Retail).

### **Repositório Git**
- **URL**: https://github.com/tr/msaf-interfaces-erp_dfe-conectores-conectores
- **Nome**: `tr/msaf-interfaces-erp_dfe-conectores-conectores`
- **Linguagem Principal**: Java

### **Características Técnicas**
- **Arquitetura**: Multi-conector
- **Sistemas Suportados**: SAP, Oracle EBS, FixaX, Infor, Retail
- **Funcionalidade**: Sincronização de dados ERP

### **Incidentes Típicos**
- Falhas de integração com ERPs específicos
- Problemas de sincronização de dados
- Performance de conectores individuais
- Mapeamento incorreto de dados entre sistemas

---

## 📄 **PRODUTO 5: DFE (Documento Fiscal Eletrônico)**
### **Descrição**
Sistema principal para geração e gestão de Documentos Fiscais Eletrônicos (NFe, NFCe, CTe).

### **Repositório Git**
- **URL**: https://github.com/tr/MSaf_DFE3
- **Nome**: `tr/MSaf_DFE3`
- **Linguagem Principal**: Java

### **Características Técnicas**
- **Versão**: 3.0
- **Documentos**: NFe, NFCe, CTe, MDFe
- **Integração**: SEFAZ, Receita Federal

### **Incidentes Típicos**
- Problemas na geração de documentos fiscais
- Falhas na comunicação com SEFAZ
- Performance no processamento de NFe/NFCe/CTe
- Problemas de validação fiscal

---

## 🏢 **PRODUTO 6: MASTERSAF CORE**
### **Descrição**
Sistema base Mastersaf, fornecendo funcionalidades core para outros produtos.

### **Repositório Git**
- **URL**: https://github.com/tr/mastersaf_core
- **Nome**: `tr/mastersaf_core`
- **Linguagem Principal**: PowerBuilder

### **Características Técnicas**
- **Arquitetura**: Sistema base
- **Tecnologia**: PowerBuilder
- **Funcionalidade**: Core do ecossistema Mastersaf

### **Incidentes Típicos**
- Problemas base do sistema
- Falhas em funcionalidades fundamentais
- Performance geral do sistema
- Compatibilidade com outros produtos

---

## 🔗 **Matriz de Correlação Entre Produtos**

| Produto | Correlaciona com | Tipo de Correlação |
|---------|------------------|-------------------|
| **TAX ONE** | DFE, Conectores ERP | Dados fiscais, integração ERP |
| **OCC Backend** | OCC Frontend | APIs, dados comerciais |
| **OCC Frontend** | OCC Backend | Interface de usuário |
| **Conectores ERP** | DFE, TAX ONE | Dados ERP para sistemas fiscais |
| **DFE** | TAX ONE, Conectores ERP | Documentos fiscais |
| **Mastersaf Core** | Todos | Base do sistema |

---

## 🎯 **Estratégias de Análise por Produto**

### **Para Problemas de Performance**
1. **TAX ONE**: Focar em procedures Oracle, locks
2. **DFE**: Analisar processamento de documentos
3. **Conectores ERP**: Verificar conectores específicos

### **Para Problemas de Integração**
1. **Conectores ERP**: Prioridade máxima
2. **OCC Backend/Frontend**: APIs e comunicação
3. **DFE ↔ TAX ONE**: Fluxo de dados fiscais

### **Para Problemas de Experiência do Usuário**
1. **OCC Frontend**: Interface e usabilidade
2. **Mastersaf Core**: Funcionalidades base
3. **Correlação Frontend ↔ Backend**: Performance end-to-end

---

**📊 Resumo**: 6 produtos distintos, 6 repositórios específicos, múltiplas correlações técnicas  
**🎯 Uso**: Direcionamento preciso de análises técnicas em RCAs multi-produto

---

**Responsável**: Jorge Washington Silva Neto via Claude Code AI Assistant  
**Última Atualização**: 29 Abr 2026