# INC20260413 - Honorários Boletos Digital Banking
## Dados Consolidados do MS Teams

### Informações Básicas do Incidente
**Número:** INC20260413  
**Produto:** Digital Banking (Honorários Boletos)  
**Descrição:** Não conseguimos localizar os dados do boleto neste momento  
**Data/Hora Abertura:** 13/04/2026 09:31  
**Chamado ServiceNow:** SS: 1119156 - 13/04/2026 - 09:25  
**Mitigação:** 13/04/2026 10:15  

**Classificação:**
- Tipo: Reativo
- Severidade: Alto
- Classificação: Major
- Ambiente: PROD
- Impacta Cliente: Sim
- Acionamento Global: Não

---

### Configuração Técnica RabbitMQ

#### Padrões de Exchange
| Pattern | Nome no RabbitMQ |
|---------|------------------|
| REGISTERED | com.tr.fintech.bank.exchange.bankslip.registered.pubsub |
| PAID | com.tr.fintech.bank.exchange.bankslip.paid.pubsub |
| CANCELLED | com.tr.fintech.bank.exchange.bankslip.cancelled.pubsub |

#### Filas do Sistema
| Tipo | Nome no RabbitMQ |
|------|------------------|
| Main (registered) | com.tr.fintech.bank.subscriber.bankslip.registered |
| Retry (registered) | com.tr.fintech.bank.subscriber.bankslip.registered-retry |
| DLQ (registered) | com.tr.fintech.bank.subscriber.bankslip.registered-deadletter |
| Main (paid) | com.tr.fintech.bank.subscriber.bankslip.paid |
| Retry (paid) | com.tr.fintech.bank.subscriber.bankslip.paid-retry |
| DLQ (paid) | com.tr.fintech.bank.subscriber.bankslip.paid-deadletter |

---

### Análise Técnica Detalhada (Sporch, Ícaro)

#### Causa Raiz Identificada
**O serviço NÃO caiu por erro de aplicação. O pod foi movido de node no Kubernetes.**

**Evidências:**
- **Pod antigo:** slip-processor-6cb7855cdc-n5s56 no node ip-10-137-69-39.ec2.internal
- **Pod novo:** slip-processor-6cb7855cdc-v68kl no node ip-10-137-68-245.ec2.internal  
- **Inicialização pod novo:** 00:23:36 UTC do dia 11/04/2026
- **ReplicaSet idêntico:** slip-processor-6cb7855cdc (sem deploy)
- **Imagem idêntica:** sha256:3ab765aca40d183798e042606379dc00bd5f7daa23e34f2fcedf49126e88752d

#### Cronologia Minuto a Minuto
| Horário (UTC) | Evento |
|---------------|--------|
| 22:30 - 23:11 | Serviço normal (~2.800 logs/min, 0 warns) |
| **23:12** | Primeiros warnings "already processed", node instável, AMQP connection instável |
| 23:12 - 23:59 | Warnings crescem: 1 → 16 → 24 → 72 → 183/min |
| 00:08 | Primeiros erros (3 boletos com documento sem conta Pismo) |
| 00:20 - 00:21 | Warnings: 528-702/min, Volume: 5.400 logs/min |
| **00:22** | **EXPLOSÃO:** 2.379 warns + 11.701 info/min - pod antigo morrendo |
| **00:23** | **PICO MÁXIMO:** 4.510 warns + 20.855 info - pod novo inicia às 00:23:36 |
| **00:24** | Normalização: 3 warns + 4.825 info - transição completa |
| 00:25+ | Volume normal: ~20-160 info/min (fila drenada) |

#### Possíveis Causas da Movimentação
1. **Node drain por manutenção:** Atualizações EKS, patching SO, scaling down
2. **Spot instance reclaimed:** AWS reivindicou instância spot

**Comportamento esperado:** Kubernetes encerrou pod gracefully, RabbitMQ reenviou mensagens não-acked, novo pod consumiu normalmente. Mecanismo de idempotência descartou ~15.500 duplicatas.

---

### Dados de Produção (Datadog - Últimas 5 horas)

#### Resumo de Volumes
- **Total de logs:** 30.803
- **Logs info:** 25.908 (84%)
- **Logs error:** 3.555 (11,5%)
- **Logs warn:** 1.354 (4,4%)

#### Operações de Boleto
| Operação | Quantidade |
|----------|------------|
| Boletos Registrados | ~1.800 |
| Boletos Pagos | 1.981 |
| Tentativas Cancelamento | 1.124 |
| Mensagens para DLQ | 187 |

#### Problemas Críticos Identificados
1. **Falha massiva em cancelamentos:** 1.122 erros (99,8% taxa de falha)
   - Erro: Status Code 400 - "Não foi possível encontrar a cobrança com o externalId informado"
   - 935 rejeitados pelo consumer
   - 187 foram para DLQ após esgotar retries

2. **Feature Flag desabilitada:** Honorary Bankslip Replicator desabilitado para 1.344 dos 1.800 boletos (75%)

3. **187 mensagens na DLQ:** Precisam investigação e reprocessamento manual

---

### Configuração de Infraestrutura

#### Problema de Resiliência Identificado
- **HPA configurado com apenas 1 réplica** (problema crítico de resiliência)
- **Atual em produção:** 2 réplicas do slip-processor
- **Recomendação:** Mínimo de 2 réplicas sempre ativo

#### Fluxo de Processamento
**Registro (assíncrono):**
```
Celcoin → POST /v1/webhooks/register/v1
    ↓
Publica em RabbitMQ (BANKSLIP_EVENT_REGISTERED)  
    ↓
Consumer processa → status: PENDING_PAYMENT
```

**Pagamento (assíncrono):**
```
Celcoin → POST /v1/payment/v1
    ↓  
Publica em RabbitMQ (BANKSLIP_EVENT_PAID)
    ↓
Consumer processa → Calcula valores → Credita Pismo → status: PAID
```

---

### Reuniões e Ações Definidas

#### Reunião 1 - Investigação Inicial (13/04/2026 09:09-09:35)
**Participantes:** Sporch (Ícaro), Medeiros (Marcio), Santos (Gabriel)
**Ações:**
- Identificação do alerta na fila bankslip.paid às 08:56
- Análise inicial do serviço slip-processor

#### Reunião 2 - Causa Raiz (14/04/2026 16:00-16:28) 
**Participantes:** Sporch (Ícaro), Moreira (Anderson), Medeiros (Marcio), Dorigao (Adriana), Silva (Ebner)

**Decisões:**
1. **Ajuste HPA:** Configurar mínimo de 2 réplicas
2. **Criação de demanda:** User story associada ao incidente  
3. **Monitoramento:** 2 dias pós-ajuste para validação
4. **Deploy:** Anderson responsável pelo PR e release
5. **Encerramento:** Após monitoramento, encerrar como definitivo

#### Tarefas de Acompanhamento
| Responsável | Tarefa |
|-------------|--------|
| Anderson | Ajuste HPA para mínimo 2 réplicas + PR/release |
| Ícaro, Ebner | Criação demanda (user story) associada ao incidente |
| Adriana | Geração documento RCA + reunião validação |
| Adriana | Monitoramento 2 dias pós-ajuste |
| Ícaro, Marcio | Implementação HPA em outros serviços conforme necessário |

#### Próxima Reunião Banking
**Data:** Quinta-feira (17/04/2026)  
**Objetivo:** Validação final e encerramento definitivo

---

### Impacto e Mitigação

#### Impacto no Cliente
- **Clientes afetados:** Múltiplos clientes emitindo boletos de honorários
- **Problema:** Impossibilidade de gerar/imprimir boletos para envio aos pagadores
- **Detalhe técnico:** Boletos registrados no banco mas falha no retorno do número
- **Atraso máximo:** ~20 minutos (não impede pagamento, mas gera gap na atualização)

#### Ação de Mitigação
- **Horário:** 10:15 (13/04/2026)
- **Ação:** Restart manual do serviço slip-processor
- **Resultado:** Restabelecimento do processamento normal das filas

#### Monitoramento Recomendado
- **Responsável sugerido:** Vitor (especialista em monitoramento)
- **Objetivo:** Detectar ausência de consumers antes do impacto ao cliente
- **Alertas atuais:** Apenas DLQ monitorado, falta monitoramento de consumer ativo