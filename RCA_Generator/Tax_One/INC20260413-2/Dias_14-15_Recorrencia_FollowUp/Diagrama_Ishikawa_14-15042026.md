# DIAGRAMA DE ISHIKAWA DETALHADO
## RECORRÊNCIA TAX ONE - 14-15/04/2026

---

## 📋 **CONTEXTUALIZAÇÃO**

**Problema Principal:** Sessões zumbis + Jobs executando >24 horas  
**Status da Análise:** ❌ **CAUSA RAIZ NÃO IDENTIFICADA**  
**Abordagem:** Mapeamento de sintomas observados e hipóteses investigadas  
**Período:** 2 dias consecutivos (14-15 Abril 2026)  

---

## 🐟 **DIAGRAMA DE ISHIKAWA EXPANDIDO**

```
                                    SESSÕES ZUMBIS + JOBS >24H
                               RECORRÊNCIA TAX ONE (14-15/04/2026)
                              ❌ CAUSA RAIZ NÃO IDENTIFICADA ❌
                                            |
                                            |
        PESSOAS                             |                        PROCESSO
            |                               |                            |
    ┌──── SMEs Técnicos ───────────────────┐|┌──────────── Threading Issues ─────────────┐
    │   • 8 especialistas mobilizados      ││|   • PL/SQL threading observado            │
    │   • Investigação não conclusiva      ││|   • Procedures com comportamento          │
    │   • Consenso: causa não identificada ││|     anômalo (não confirmado)             │
    └───────────────────────────────────────┘│└────────────────────────────────────────┘
                                            ||
    ┌──── Equipe Operacional ──────────────┐||┌──────────── Acúmulo Sessões ─────────────┐
    │   • Bruno Fornari: comunicação       ││|   • 226+ processos zumbis                │
    │   • Adriana Dorigao: facilitação     ││|   • Estado: PL/SQL Lock Timer            │
    │   • Resposta reativa eficiente       ││|   • Crescimento exponencial 15:37-17:18  │
    └───────────────────────────────────────┘│└────────────────────────────────────────┘
                                            |
                                            |
        MÉTODO                              |                        MÁQUINA
            |                               |                            |
    ┌──── Monitoramento ───────────────────┐||┌──────────── Ambiente Oracle ──────────────┐
    │   • Ausente p/ sessões >10min        ││|   • Oracle Cloud (não on-premise)         │
    │     (CORRIGIDO pós-incidente)        ││|   • Comportamento específico observado    │
    │   • 162 samples ASH coletados        ││|   • Possível diferença vs on-premise     │
    │   • Alertas implementados             ││|     (hipótese não confirmada)            │
    └───────────────────────────────────────┘│└────────────────────────────────────────┘
                                            ||
    ┌──── Investigação ────────────────────┐||┌──────────── Recursos Sistema ─────────────┐
    │   • Múltiplas hipóteses testadas     ││|   • Lock contention: enq: JG queue lock   │
    │   • Nenhuma hipótese confirmada      ││|   • 226+ processos consumindo recursos    │
    │   • Análise técnica inconclusiva     ││|   • PROD01 + PROD03 afetados             │
    │   • Solução reativa aplicada         ││|   • Degradação performance generalizada   │
    └───────────────────────────────────────┘│└────────────────────────────────────────┘
                                            |
                                            |
        MATERIAL                            |                   MEIO AMBIENTE
            |                               |                            |
    ┌──── Evidências Técnicas ─────────────┐||┌──────────── Padrão Temporal ──────────────┐
    │   • ASH: 162 samples enq: JG lock    ││|   • 2 dias consecutivos (14-15/04)        │
    │   • Jobs >24h (Shopee crítico)       ││|   • Horário: ~16h em ambos os dias       │
    │   • Threading PL/SQL suspeito        ││|   • Recorrência independente do dia 13    │
    │     (não confirmado como causa)      ││|   • Padrão não antecipado                │
    └───────────────────────────────────────┘│└────────────────────────────────────────┘
                                            ||
    ┌──── Configurações ───────────────────┐||┌──────────── Impacto Comercial ────────────┐
    │   • Oracle Cloud settings            ││|   • 40+ clientes impactados               │
    │   • DBMS_SCHEDULER behavior          ││|   • Cliente crítico: Shopee               │
    │   • Threading parameters             ││|   • Manutenções PROD01/PROD03 adiadas     │
    │   • Possíveis ajustes necessários    ││|   • 8 tickets reprocessamento enviados    │
    │     (hipótese não testada)           ││|   • Escalação executiva contida           │
    └───────────────────────────────────────┘│└────────────────────────────────────────┘
                                            |
                                            |
                                   ┌─────────────────────────────────────────┐
                                   │         RESULTADO FINAL                 │
                                   │                                         │
                                   │  ❌ CAUSA RAIZ: NÃO IDENTIFICADA       │
                                   │  ✅ SINTOMAS: Mapeados e documentados  │
                                   │  ✅ MITIGAÇÃO: Reativa e eficiente     │
                                   │  🔄 STATUS: Investigação continuada    │
                                   │  ✅ PREVENÇÃO: Monitoramento ativo     │
                                   └─────────────────────────────────────────┘
```

---

## 🔍 **LEGENDA E CLASSIFICAÇÃO**

### **✅ FATOS CONFIRMADOS**
- **226+ sessões zumbis** eliminadas manualmente
- **162 samples ASH** de lock contention documentados
- **Job Shopee >24h** (normal <2h) confirmado
- **2 dias consecutivos** de recorrência (14-15/04)
- **40+ clientes afetados** documentados

### **❓ HIPÓTESES INVESTIGADAS (NÃO CONFIRMADAS)**
- Threading PL/SQL como possível causa
- Diferenças Oracle Cloud vs On-Premise
- Configurações inadequadas para multi-tenancy
- Issues específicos em DBMS_SCHEDULER

### **🔄 AÇÕES IMPLEMENTADAS**
- **✅ Monitoramento proativo** para sessões >10min
- **✅ Critérios de intervenção** estabelecidos
- **✅ Scripts de limpeza** manual documentados
- **🔄 Investigação continuada** em andamento

---

## 📊 **ANÁLISE QUANTITATIVA DOS SINTOMAS**

### **Distribuição por Categoria Ishikawa**

| Categoria | Sintomas Confirmados | Hipóteses | Status Investigação |
|-----------|---------------------|-----------|-------------------|
| **PESSOAS** | 8 SMEs mobilizados | Expertise adequada | ✅ Confirmada |
| **PROCESSO** | 226+ sessões zumbis | Threading inadequado | ❌ Não confirmada |
| **MÉTODO** | Monitoramento ausente | Detecção tardia | ✅ Corrigida |
| **MÁQUINA** | Lock contention (162) | Oracle Cloud behavior | ❓ Investigando |
| **MATERIAL** | ASH samples coletados | Configuração inadequada | ❓ Investigando |
| **MEIO AMBIENTE** | Padrão 2 dias (~16h) | Fatores externos | ❓ Investigando |

### **Grau de Confiança por Elemento**

```
ALTA CONFIANÇA (Sintomas Confirmados):
█████████████████████ 100% - Sessões zumbis eliminadas
█████████████████████ 100% - Lock contention observado
█████████████████████ 100% - Cliente Shopee job >24h
█████████████████████ 100% - Padrão temporal 2 dias

MÉDIA CONFIANÇA (Evidências Parciais):
████████████▓▓▓▓▓▓▓▓▓ 60% - Threading PL/SQL issues
████████████▓▓▓▓▓▓▓▓▓ 60% - Oracle Cloud behavior

BAIXA CONFIANÇA (Hipóteses):
██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 30% - Configurações inadequadas
██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 30% - DBMS_SCHEDULER issues

DESCONHECIDO:
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  0% - CAUSA RAIZ FUNDAMENTAL
```

---

## 🎯 **CONCLUSÕES DO DIAGRAMA**

### **🔍 Principais Insights**
1. **Sintomas bem mapeados** mas causa raiz permanece desconhecida
2. **Padrão temporal claro** (2 dias consecutivos ~16h)
3. **Mitigação reativa eficiente** mas não preventiva
4. **Monitoramento melhorado** reduz risco de recorrência

### **⚠️ Lacunas Identificadas**
1. **Causa fundamental não identificada** = risco de nova recorrência
2. **Threading PL/SQL** permanece como hipótese não testada
3. **Oracle Cloud specifics** não completamente investigados
4. **Testes de stress** multi-tenant não realizados

### **🚀 Próximos Passos Sugeridos**
1. **Testes controlados** em ambiente similar
2. **Consulta Oracle** sobre behavior Cloud vs On-Premise  
3. **Migração threading** PL/SQL → Java (Q3-Q4/2026)
4. **Monitoramento contínuo** dos padrões identificados

---

**📅 Diagrama Criado:** 24 de Abril de 2026  
**🔄 Versão:** 1.0 (Detalhado)  
**📋 Base:** Sintomas confirmados + Hipóteses investigadas  
**⚠️ Limitação:** Causa raiz não identificada - Diagrama focado em sintomas observados