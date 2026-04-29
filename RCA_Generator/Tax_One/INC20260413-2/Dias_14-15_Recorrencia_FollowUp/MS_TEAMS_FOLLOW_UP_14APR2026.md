# MS Teams Follow-up - 14 Abril 2026 - INC20260413-2

## Informações da Reunião de Follow-up

**ID do Incidente:** INC20260413-2 - TAX ONE - Lentidão nos processos  
**Data e Horário:** 14 Abr 2026, 15:00–20:38 BRT (5h 39min 2s)  
**Tipo:** CHECKPOINT - Incident 1100920: INC20261304 - TAX ONE - Lentidão nos processos  
**Status:** Reunião de acompanhamento pós-incidente  
**Facilitadora:** Adriana Dorigao

## Timeline das Comunicações - 14 Abril 2026

### 15:21 BRT - Monitoramento Processo 95R
- **Bruno Fornari**: Solicitou horário de término do processo da 95R
- **Contexto**: Verificação de impacto específico em cliente

### 16:30 BRT - Solicitação de Status
- **Simone Costa (LatAm)**: "Temos alguma atualização?"
- **Indicação**: Solicitação comercial por atualizações

### 17:05 BRT - Análise Técnica Nelson Cartaxo
- **Nelson Cartaxo**: Compartilhou arquivo "plsql_lock_timer_melhorias.html"
- **Significado**: Documentação técnica sobre melhorias nos timers de lock

### 17:15-17:28 BRT - Discussão Parâmetros FILA-EXEC
- **Filipe Lopes**: Explicou parâmetros de controle de fila
  ```
  PRT_PAR_MSAF
  NUM_THREAD_FRW: 10
  PERCENT_MAX_UTIL_T1: 80  
  NUM_MAX_PROC_EXEC_T1: 20
  ```
- **Eduardo Cunha**: Alertou sobre bug histórico no cliente IURD
- **Risco**: Desabilitar controle pode causar criação de milhares de jobs

### 17:50-17:58 BRT - Escalação e Histórico
- **Rebeca Raymundo**: Solicitou retorno de Simone Costa à sala
- **Eduardo Cunha**: Compartilhou "historico_incidente.txt" com lista de clientes afetados
- **Lista**: HNKBR, TIGRE, YARA mencionados especificamente

### 18:08-18:19 BRT - Expansão do Problema
- **Cristiane Fugii**: Reportou problema similar em PROD03
- **Questionamento**: "Temos certeza que o problema é volume de clientes?"
- **Eduardo Cunha**: Identificou jobs com >30min execução começando às 14h, disparando às 15h

### 18:13-18:26 BRT - Consultas de Monitoramento
- **Filipe Lopes**: Preparou queries para processos em status "CRIADO"
- **Marcelo Pessanha**: Desenvolveu query "select * from saf_lock_control"
- **Objetivo**: Monitoramento proativo de problemas

### 18:33 BRT - Análise de Mudanças
- **Cristiane Fugii**: 
  - "Podem confirmar quando atualizamos a lib_proc e quais as alterações?"
  - "E quais os relatórios que estavam rodando neste período de 12hs e 16hs"
- **Crítico**: Identificação de mudanças coincidentes com incidente

### 19:13-19:25 BRT - Status Operacional
- **Bruno Fornari**: "não teve ticket de PROD03"
- **Marcelo Pessanha**: Apresentou "Plano Pessanha":
  1. Script de resiliência para tenants afetados
  2. Query para monitorar status "CRIADOS"  
  3. Alteração LB_PROC para DBMS_LOCK.SLEEP com novo parâmetro

### 19:50 BRT - Decisão Executiva
- **Simone Costa (LatAm)**: 
  - **"Postergaremos PROD01 e PROD03 para quinta-feira"**
  - **"Hoje seguimos com os demais ambientes, conforme programação"**
- **Impacto**: Adiamento de manutenções críticas devido ao incidente

### 20:00 BRT - Monitoramento DataDog
- **Luis Fernando**: Compartilhou link DataDog para PROD03
- **URL**: Monitoramento de queries Oracle em ambiente de produção

### 20:38 BRT - Encerramento
- **Duração Total**: 5h 39min 2s
- **Participantes**: 15 alto-falantes
- **Deliverables**: 8 tarefas definidas
- **Gravações**: 2 gravações salvas no SharePoint

## Participantes Identificados

**Facilitadora:**
- **Adriana Dorigao** - Incident Manager

**Gestão e Liderança:**
- **Luis Fernando de Deus Lopes** - Diretor de Arquitetura
- **Nelson Cartaxo** - Gerente Sr de DBAs
- **Bruno Vianna** - Gerente Sr de Techops
- **Filipe Lopes** - Delivery Manager de Evolução Técnica
- **Rebeca Raymundo** - Chapter Leader dos Agentes de Mudança
- **Cristiane Fugii** - Gerente Sr de Corporates

**Product & Business:**
- **Simone Costa** - Product Manager de TAX ONE (quando presente)

**Especialistas Técnicos:**
- **Alceste Siqueira Junior** - DBA
- **Marcelo Pessanha** - Especialista técnico
- **Eduardo Cunha** - DBA
- **Bruno Fornari** - Especialista de Suporte ao Cliente

### Stakeholders de Negócio
- **Simone Costa (LatAm)** - Solicitação comercial por atualizações

## Descobertas Técnicas Adicionais

### Problema Expandido - PROD03
- **17:08**: Cristiane Fugii confirmou problema similar em PROD03
- **Questionamento**: Volume de clientes vs. outros fatores
- **Implicação**: Problema sistêmico, não isolado a PROD01

### Análise de Performance Detalhada
- **Jobs >30min**: Eduardo Cunha identificou padrão temporal
  - **14h**: Início do aumento
  - **15h**: Disparada crítica
- **Correlação**: Timeline precisa coincide com primeiro reporte (17:02)

### Parâmetros Críticos Identificados
```sql
-- Controle de Fila EXEC
PRT_PAR_MSAF:
  NUM_THREAD_FRW: 10
  PERCENT_MAX_UTIL_T1: 80
  NUM_MAX_PROC_EXEC_T1: 20

-- Monitoramento proposto
SELECT * FROM saf_lock_control;

-- Cliente específico identificado em execução
USER_TAXONE_SHOPEE - Job executando desde 13/04/2026 16:13:36
```

### Bug Histórico IURD (Contexto Importante)
- **Ano anterior**: Tentativa de desabilitar controle FILA-EXEC
- **Resultado**: Bug com REINF criando 10.000 jobs
- **Lição**: Controle de fila é crítico para estabilidade
- **Implicação**: Soluções devem manter controles, não removê-los

## Plano de Ação "Plano Pessanha" (19:25)

### Ações Imediatas
1. **Script Resiliência**: Para tenants na lista de afetados
2. **Query Monitoramento**: Para status "CRIADOS" em tempo real  
3. **Alteração LB_PROC**: DBMS_LOCK.SLEEP com parâmetro configurável

### Monitoramento Proativo Proposto
- **Critério**: Processos "CRIADOS" há >5 minutos
- **Threshold**: >100 processos = cenário lock timer
- **Base**: Consulta por esquema individual (não centralizada)

## Impacto Comercial Evidenciado

### Clientes Específicos Afetados
- **USER_TAXONE_SHOPEE**: Job executando desde 16:13 (>24h)
- **HNKBR, TIGRE, YARA**: Listados em histórico de incidentes
- **Múltiplos tenants**: Lista extensa em "historico_incidente.txt"

### Decisão de Adiamento (CRÍTICA)
- **PROD01 e PROD03**: Manutenções adiadas para quinta-feira
- **Motivo**: Instabilidade pós-incidente  
- **Impacto**: Interrupção de roadmap de manutenção

### Percepção do Cliente (Bruno Fornari - 3:58:54)
- **Antes**: Processos em segundos
- **Durante incidente**: >3 minutos = percepção de lentidão
- **Threshold crítico**: Qualquer coisa >2-3 minutos gera reclamação

## Evidências de Expansão do Problema

### Timeline Expandida
- **13/04 17:02**: Primeiro reporte INC20260413-2
- **14/04 14:00**: Aumento de jobs >30min (Eduardo Cunha)
- **14/04 15:00**: Disparada crítica de performance
- **14/04 18:08**: PROD03 apresenta sintomas similares

### Questões em Aberto (14/04)
1. **Cristiane Fugii (18:33)**: 
   - Quando foi atualizada lib_proc?
   - Quais alterações foram feitas?
   - Quais relatórios executavam 12h-16h?

2. **Filipe Lopes (17:28)**:
   - Histórico completo do bug IURD
   - Comportamento interno de chamadas mesmo com parâmetros desabilitados

## Transcrição de Áudio - Fragmentos Críticos

### Percepção do Cliente (3:54:13 - 3:59:34)
**Marcelo Pessanha (3:54:18)**: "com essas ações que a gente fez na Shopee, a gente consegue saber se na Shopee ficou legal?"

**Bruno Fornari (3:58:54)**: "Ela ficou 15 [minutos] no final das contas... é que é o que a percepção do cliente é exatamente essa, tipo, ele colocava para gerar, clicava no listar e já era feito depois de um tempo, depois com os incidentes, passa do tempo que ele espera... deu 3 minutos, algo que fazia em segundos. O cliente, ele já entende que há uma lentidão."

### Monitoramento Proposto (3:55:31 - 3:57:25)
**Filipe Lopes**: "tendo em vista a questão de monitorar como que a gente pega, identifica que quando os processos começam a ficar com o status criado... é um sinal de que a gente está entrando nesse cenário de Lock Timer"

**Marcelo Pessanha**: "Na minha visão, a gente teria que fazer base a base... porque a informação do criado a gente vai ter só na Leap processo, né?"

### Critério de Alerta (3:58:36 - 3:58:47)
**Nelson Cartaxo**: "O Bruno hoje reclamou que ficou mais de dois minutos. Tô falando pela percepção do cliente, tô fazendo Advogado do Diabo."

---
**Documento**: MS Teams Follow-up Day 2  
**Data**: 14 Abr 2026, 15:00–20:38 BRT  
**Duração**: 5h 39min (5x maior que reunião inicial)  
**Participantes**: 15 alto-falantes  
**Status**: Problema expandido para PROD03, manutenções adiadas  
**Próximos passos**: Implementação "Plano Pessanha"  
**Arquivo Gerado**: 15 Abr 2026