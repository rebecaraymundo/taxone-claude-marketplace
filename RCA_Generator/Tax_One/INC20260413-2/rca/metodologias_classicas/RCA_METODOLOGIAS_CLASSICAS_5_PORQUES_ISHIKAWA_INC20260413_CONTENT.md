# ANÁLISE DE CAUSA RAIZ
## Metodologias Clássicas: 5 PORQUÊS & ESPINHA DE PEIXE

---

## 📋 DADOS DO INCIDENTE

| **Campo** | **Valor** |
|-----------|-----------|
| **Número do Incidente** | INC20260413-2 |
| **Sistema Afetado** | TAX ONE |
| **Período de Impacto** | 13-16/04/2026 (4 dias consecutivos) |
| **Descrição** | Lentidão nos processos TAX ONE |
| **Impacto Identificado** | 226+ sessões zumbis, 40+ clientes afetados |
| **Causa Raiz** | lib_proc alterado inadequadamente + spin loop EQUAL_DATAMART_FPROC |

---

## 🔍 METODOLOGIA 1: OS 5 PORQUÊS (5 WHYS)

### POR QUÊ 1:
**Pergunta:** Por que o sistema TAX ONE ficou lento?  
**Resposta:** → Sessões ficaram presas em "PL/SQL lock timer" causando lentidão generalizada no sistema

### POR QUÊ 2:
**Pergunta:** Por que as sessões ficaram presas em "PL/SQL lock timer"?  
**Resposta:** → Contenção massiva no job queue do Oracle com 162 ASH samples indicando disputa por recursos

### POR QUÊ 3:
**Pergunta:** Por que ocorreu contenção no job queue do Oracle?  
**Resposta:** → Sistema executava 500-1000 queries por segundo na view all_scheduler_jobs sobrecarregando o banco

### POR QUÊ 4:
**Pergunta:** Por que o sistema executava tantas queries na all_scheduler_jobs?  
**Resposta:** → O comando dbms_lock.sleep foi desabilitado no loop da linha 12464, criando um spin loop infinito

### POR QUÊ 5:
**Pergunta:** Por que o dbms_lock.sleep foi desabilitado?  
**Resposta:** → A biblioteca lib_proc foi alterada inadequadamente entre 13-14/04/2026 sem validação adequada do impacto

### 🎯 CAUSA RAIZ IDENTIFICADA
**Alteração inadequada da biblioteca lib_proc** que desabilitou o sleep no loop EQUAL_DATAMART_FPROC, criando um spin loop que sobrecarregou o job queue do Oracle.

---

## 🐟 METODOLOGIA 2: DIAGRAMA ESPINHA DE PEIXE (ISHIKAWA)

### ANÁLISE DOS 6Ms - FATORES CONTRIBUINTES

#### 📦 MATERIAIS (CODE)
- lib_proc alterado inadequadamente
- Loop EQUAL_DATAMART_FPROC comentado
- Processos LIB_PROCESSO órfãos
- Dependências não mapeadas
- Código legado sem documentação

#### 🔧 MÉTODOS (PROCEDURES)
- Code review inadequado
- Testes de impacto insuficientes
- Rollback parcial executado
- Processo de validação falho
- Metodologia de deploy inadequada

#### 💻 MÁQUINAS (INFRA)
- Oracle Cloud limitações
- Threads sem Resource Manager
- Infraestrutura não-SaaS
- Monitoramento insuficiente
- Capacidade de job queue limitada

#### 👥 PESSOAS (HUMAN)
- Pergunta Cristiane Fugii não respondida
- Gap na comunicação entre equipes
- Validação técnica insuficiente
- Conhecimento fragmentado
- Handover inadequado

#### 📊 MEDIÇÕES (MONITORING)
- Detecção tardia do problema
- Alertas de performance inadequados
- Correlação lib_proc não mapeada
- ASH samples não monitorados
- Métricas de job queue ausentes

#### 🌍 MEIO AMBIENTE
- Deploy em múltiplos ambientes
- Timing coincidente das alterações
- Recorrência por 3 dias consecutivos
- Ambiente produtivo não isolado
- Configurações específicas Oracle

### 🎯 PROBLEMA PRINCIPAL
**LENTIDÃO TAX ONE - INC20260413-2**  
226+ Sessões Zumbis • 40+ Clientes Afetados

---

## ✅ VALIDAÇÃO TÉCNICA E CONVERGÊNCIA

**Validação por Jorge Washington (20/04/2026):**

- ✅ Correlações técnicas confirmadas entre lib_proc e LIB_PROCESSO
- ✅ Fix implementado com 99,8% de redução nas queries
- ✅ Ambas metodologias convergem para a mesma causa raiz
- ✅ Pergunta da Cristiane Fugii foi respondida e documentada

### 🔄 CONVERGÊNCIA DAS METODOLOGIAS

Tanto a análise dos **5 Porquês** quanto o **Diagrama de Ishikawa** identificam a mesma causa raiz principal: **alteração inadequada da biblioteca lib_proc** que criou um spin loop, sobrecarregando o sistema Oracle e causando lentidão generalizada.

---

**Thomson Reuters TAX ONE** • Análise de Causa Raiz • Gerado em 20/04/2026  
Documento: RCA_METODOLOGIAS_CLASSICAS_5_PORQUES_ISHIKAWA_INC20260413