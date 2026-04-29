# Análise de Causa Raiz (RCA)

## Cabeçalho
**ID do Problema:** INC20260413  
**Problema:** Honorários Boletos Digital Banking - Não conseguimos localizar os dados do boleto neste momento  
**Thomson Reuters Enterprise**

**ID do Incidente Maior:** INC20260413  
**Incidente:** Falha na geração/impressão de boletos de honorários  
**Thomson Reuters Enterprise**

**Status da ACR:** Concluído  
**Serviço / Produto Responsável:** Digital Banking - Slip Processor  
**Serviços / Produtos Impactados:** Honorários Boletos  
**Data e Horário da Reunião:** 14/04/2026 16:00-16:30 (UTC-3)  
**Nome e Função do Facilitador:** Dorigao, Adriana - Incident Manager

---

## 1. Participantes

| Nome | Função |
|------|--------|
| Dorigao, Adriana | Incident Manager |
| Sporch, Ícaro (TR Technology) | Delivery Manager |
| Moreira, Anderson (TR Technology) | DevOps |
| Medeiros, Marcio B. (TR Technology) | DevOps |
| Silva, Ebner | Tech Lead |
| Rosso, Andrei (LatAm) | Product Owner |
| Santos, Gabriel | Software Engineer |
| Thezolim, Leonardo (LatAm) | Product Owner |

---

## 2. Resultado

### Resumo da Reunião
Foi identificado que o incidente não foi causado por erro de aplicação, mas sim pela movimentação de pod do serviço slip-processor entre nodes do cluster Kubernetes. O mecanismo de failover funcionou corretamente, porém a configuração de HPA com apenas 1 réplica criou um ponto único de falha.

### Acordos
- Ajustar HPA para mínimo de 2 réplicas no slip-processor
- Implementar monitoramento de consumers inativos
- Criar user story associada ao incidente
- Monitorar por 2 dias pós-implementação antes do encerramento definitivo

---

## 3. Declaração do Problema

### Resumo
No dia 13/04/2026 às 09:31, clientes do produto Digital Banking começaram a reportar impossibilidade de gerar e imprimir boletos de honorários. Os boletos eram registrados no sistema bancário mas o retorno do número falhava, impedindo a impressão e envio aos pagadores.

### Impacto Detalhado
- **Clientes Afetados:** Múltiplos clientes utilizando emissão de boletos de honorários
- **Duração:** 44 minutos (09:31 - 10:15)
- **Funcionalidade Impactada:** Geração e impressão de boletos para honorários
- **Consequência:** Clientes impossibilitados de enviar boletos aos pagadores
- **Ambiente:** Produção
- **Chamado ServiceNow:** SS: 1119156

---

## 4. Resumo da Timeline

| Horário | Evento |
|---------|--------|
| **T0** 13/04/2026 09:25 | Abertura do chamado SS: 1119156 pelos clientes |
| **Detecção** 09:31 | Abertura oficial do incidente INC20260413 |
| **Escalação** 09:32 | Acionamento do time técnico via MS Teams |
| **Investigação** 09:32-10:14 | Análise técnica do serviço slip-processor e filas RabbitMQ |
| **Ações de Recuperação** 10:15 | Restart manual do serviço slip-processor |
| **Resolução** 10:15 | Restabelecimento completo do processamento de boletos |

### Cronologia Técnica Detalhada (Pod Kubernetes)
| Horário (UTC) | Evento |
|---------------|--------|
| 10/04 22:30-23:11 | Serviço funcionando normalmente (~2.800 logs/min) |
| **10/04 23:12** | Primeiro sinal de instabilidade - warnings "already processed" |
| 10/04 23:12-23:59 | Escalada gradual de warnings (1→183/min), conexão AMQP instável |
| **11/04 00:22** | Explosão de logs - pod antigo sendo finalizado |
| **11/04 00:23:36** | Pod novo iniciado no node ip-10-137-68-245.ec2.internal |
| **11/04 00:24** | Normalização completa do processamento |

---

## 5. Causa Raiz

**Status:** Identificada e Confirmada  
**Código:** INFRA-K8S-NODE-MIGRATION  
**Mecanismo:** Movimentação de pod entre nodes do cluster Kubernetes  

### Declaração
O incidente foi causado pela migração automática do pod slip-processor entre nodes do cluster Kubernetes. O pod slip-processor-6cb7855cdc-n5s56 foi movido do node ip-10-137-69-39.ec2.internal para o node ip-10-137-68-245.ec2.internal, sendo substituído pelo pod slip-processor-6cb7855cdc-v68kl. Durante a transição, o processamento das filas RabbitMQ foi interrompido, causando acúmulo de mensagens e falha na resposta aos clientes.

### Evidências
1. **Logs Kubernetes:** Confirmam a migração de pod sem erros de aplicação
2. **Mesmo ReplicaSet:** slip-processor-6cb7855cdc (descarta deploy)
3. **Mesma imagem:** sha256:3ab765aca40d183798e042606379dc00bd5f7daa23e34f2fcedf49126e88752d
4. **Ausência de erros:** Sem OOMKilled, CrashLoopBackOff ou health check failure
5. **Padrão temporal:** Degradação gradual seguida de recuperação automática

### Metodologia
Análise de logs do Datadog, investigação de métricas do Kubernetes, revisão de deployment history e correlação temporal dos eventos.

---

## Causas Contribuintes

| CC | Descrição | Evidência | Status |
|----|-----------|-----------|---------|
| CC-01 | HPA configurado com apenas 1 réplica mínima | Configuração atual do HPA no ambiente | Confirmada |
| CC-02 | Ausência de monitoramento de consumers inativos | Problema só detectado após impacto ao cliente | Confirmada |
| CC-03 | Node drain por manutenção ou spot instance termination | Migração automática de pod entre nodes | Provável |

---

## Soluções Preventivas

| ID | Ação | Endereça | Desafios | Status |
|----|------|----------|----------|---------|
| SP-01 | Configurar HPA com mínimo de 2 réplicas para slip-processor | CC-01 | Aprovação de custos adicionais | Aprovada |
| SP-02 | Implementar monitoramento de consumers RabbitMQ | CC-02 | Integração com ferramentas existentes | Planejada |
| SP-03 | Audit de todos os serviços com HPA de 1 réplica | CC-01 | Levantamento extenso de infraestrutura | Planejada |

---

## Soluções Corretivas

| ID | Ação | Endereça | Desafios | Status |
|----|------|----------|----------|---------|
| SC-01 | Restart manual do serviço slip-processor | Restauração imediata do serviço | Impacto durante restart | Executada |

---

## Melhorias

| ID | Ação | Endereça | Status |
|----|------|----------|---------|
| M-01 | Implementar alertas proativos para consumers inativos | Detecção precoce de problemas | Planejada |
| M-02 | Revisar política de node management no cluster | Reduzir impacto de migrações de pod | Em análise |

---

## Ações

| ID da Ação | Ação (SMART) | Responsável | Data de Vencimento | ID da PTask |
|------------|--------------|-------------|-------------------|-------------|
| A-01 | Configurar HPA do slip-processor para min: 2 réplicas até 15/04/2026 | Anderson Moreira | 15/04/2026 | TBD |
| A-02 | Criar user story associada ao incidente até 14/04/2026 | Ícaro Sporch, Ebner Silva | 14/04/2026 | TBD |
| A-03 | Implementar monitoramento de consumers RabbitMQ até 30/04/2026 | Marcio Medeiros | 15/04/2026 | TBD |
| A-04 | Realizar o monitoramento do serviços com HPA=1 até 16/04/2026 | Anderson Moreira, Marcio Medeiros | 25/04/2026 | TBD |

---

## Workaround e Erro Conhecido

**Workaround Aplicado:** Restart manual do serviço slip-processor restabeleceu o processamento normal das filas RabbitMQ.

**Erro Conhecido:** Serviços com HPA configurado para 1 réplica mínima são vulneráveis a interrupções durante migrações de pod entre nodes.

---

## Distribuição

- Incident Management Team
- Digital Banking Product Team  
- Infrastructure Engineering Team
- Platform Engineering Team

---

## Sources

- MS Teams: Fluxos de trabalho - Discussões técnicas INC20260413
- Datadog: Logs e métricas do período 10-13/04/2026
- Kubernetes Cluster: Logs de pods e events
- ServiceNow: Ticket SS: 1119156
- RabbitMQ Management: Filas e exchanges do período