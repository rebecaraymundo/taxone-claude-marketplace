# Relatório de Análise de Causa Raiz - [INCIDENT_ID]

**ID do Problema:** [A ser gerado] | Problema | Thomson Reuters Enterprise  
**ID do Incidente Maior:** [INCIDENT_ID] | Incidente | Thomson Reuters Enterprise

**Status da ACR:** [Causa Raiz Confirmada / Em Investigação]  
**Serviço / Produto Responsável:** [PRODUTO/SERVIÇO]  
**Serviços / Produtos Impactados:** [SERVIÇOS IMPACTADOS]  
**Data e Horário da Reunião (Fuso Horário):** [DD Mmm AAAA, HH:MM–HH:MM BRT]  
**Nome e Função do Facilitador:** [NOME], [FUNÇÃO]

## Participantes

**Gerente de Problemas:** [NOME] ([DEPARTAMENTO])  
**Especialistas Técnicos (Aplicação):**
- [NOME] ([DEPARTAMENTO])
- [NOME] ([DEPARTAMENTO])  
- [NOME] ([DEPARTAMENTO])
- [NOME] ([DEPARTAMENTO])

## Resultado

[Resumo da reunião de revisão da ACR validando serviço impactado, cronograma, causa raiz e principais ações preventivas/corretivas. Incluir confirmação da equipe sobre o problema, causa raiz identificada e acordo sobre ações de follow-up.]

## Declaração do Problema

**Resumo do Problema:**  
[Descrição detalhada do problema incluindo: data/hora de início, sintomas observados, funcionalidades afetadas, duração do impacto. Ser específico sobre o que os usuários experimentaram.]

**Impacto:** [Descrição do impacto incluindo: número de clientes afetados, clientes específicos mencionados, ambiente impactado, necessidade de ações emergenciais, volume de contatos ao suporte.]

## Resumo da Timeline

- **T0 (Primeira anomalia):** [DD Mmm AAAA HH:MM BRT] — [primeira indicação do problema]
- **Detecção:** [DD Mmm AAAA HH:MM BRT] — [método de detecção]
- **Escalação / Tratamento como Incidente Maior:** [DD Mmm AAAA HH:MM BRT] — [processo de escalação]
- **Ações de Recuperação:** [DD Mmm AAAA HH:MM-HH:MM BRT] — [ações tomadas]
- **Resolução:** [DD Mmm AAAA HH:MM BRT] — [como foi resolvido]

## Causa Raiz

**Status:** [Confirmada / Em Investigação]  
**Código da Causa:** [Falha de Código/Design / Demand/Capacity failure / etc.]  

**Mecanismo de Falha:**  
[Descrição técnica detalhada de como o problema ocorreu, incluindo componentes específicos, procedures, configurações, ou arquitetura envolvida. Explicar a cadeia de eventos que levou ao problema.]

**Declaração da Causa Raiz:**  
[Statement conciso e claro da causa raiz identificada, incluindo componente específico, ação que causou o problema, e como isso resultou no impacto observado.]

**Evidências de Suporte da Causa Raiz:**
- [Evidência específica 1 - logs, análises técnicas]
- [Evidência específica 2 - confirmação de SMEs]
- [Evidência específica 3 - testes ou validações]
- [Evidência específica 4 - histórico de repositório]
- [Evidência específica 5 - métricas de sistema]

**Metodologia de ACR Aplicada:** [5 Whys / Análise Técnica / Revisão de Código]

## Causas Contribuintes

| CC  | Descrição | Evidência | Status |
|-----|-----------|-----------|---------|
| CC1 | [Descrição da causa contribuinte 1] | [Evidência que suporta esta causa] | [Acordado/Não Acordado] |
| CC2 | [Descrição da causa contribuinte 2] | [Evidência que suporta esta causa] | [Acordado/Não Acordado] |
| CC3 | [Descrição da causa contribuinte 3] | [Evidência que suporta esta causa] | [Acordado/Não Acordado] |
| CC4 | [Descrição da causa contribuinte 4] | [Evidência que suporta esta causa] | [Acordado/Não Acordado] |

## Soluções

### Soluções Preventivas:

| ID | Ação | Endereça | Desafios | Status |
|----|------|----------|----------|---------|
| P1 | [Ação preventiva 1 - o que será feito para prevenir recorrência] | [Causa Raiz, CC1, CC2] | [Desafios de implementação] | [Acordado/Não Acordado] |
| P2 | [Ação preventiva 2] | [CC2, CC3] | [Desafios de implementação] | [Acordado/Não Acordado] |
| P3 | [Ação preventiva 3] | [CC3, CC4] | [Desafios de implementação] | [Acordado/Não Acordado] |

### Soluções Corretivas:

| ID | Ação | Endereça | Desafios | Status |
|----|------|----------|----------|---------|
| C1 | [Ação corretiva 1 - o que foi feito para resolver] | [Causa Raiz, CC1] | [Limitações ou considerações] | [Concluído/Em Andamento] |
| C2 | [Ação corretiva 2] | [Causa Raiz] | [Limitações ou considerações] | [Concluído/Em Andamento] |
| C3 | [Ação corretiva 3] | [Impacto] | [Limitações ou considerações] | [Concluído/Em Andamento] |

### Melhorias:

| ID | Ação | Endereça | Status |
|----|------|----------|---------|
| I1 | [Melhoria 1 - como melhorar detecção/monitoramento] | [Causa Raiz, CC4, Lições Aprendidas] | [Acordado/Não Acordado] |
| I2 | [Melhoria 2 - como melhorar processos] | [CC1, CC2, Lições Aprendidas] | [Acordado/Não Acordado] |
| I3 | [Melhoria 3 - como melhorar arquitetura/design] | [CC2, Lições Aprendidas] | [Acordado/Não Acordado] |

## Workaround e Erro Conhecido

**Status:** [Implementado / Pendente / Não Aplicável]  
**Workaround Necessário:** [Sim / Não]  
**Workaround Disponível:** [Sim / Não]

**Workaround:**  
[Descrição do workaround implementado, incluindo limitações e instruções para clientes se aplicável.]

**Erro Conhecido Necessário e Razão:**  
[Sim/Não] - [Justificativa para manter Known Error até que mudanças permanentes sejam implementadas. Explicar se há limitações arquiteturais ou de processo que requerem acompanhamento de longo prazo.]

## Ações

| ID da Ação | Ação (SMART) | Responsável | Data de Vencimento | ID da PTask |
|------------|--------------|-------------|-------------------|-------------|
| A1 | [Ação específica, mensurável, atingível, relevante, temporizada] | [Nome Responsável] | [DD Mmm AAAA] | [PTASK ID ou "A ser criado"] |
| A2 | [Ação SMART 2] | [Nome Responsável] | [DD Mmm AAAA] | [PTASK ID ou "A ser criado"] |
| A3 | [Ação SMART 3] | [Nome Responsável] | [DD Mmm AAAA] | [PTASK ID ou "A ser criado"] |
| A4 | [Ação SMART 4] | [Nome Responsável] | [DD Mmm AAAA] | [PTASK ID ou "A ser criado"] |
| A5 | [Ação SMART 5] | [Nome Responsável] | [DD Mmm AAAA] | [PTASK ID ou "A ser criado"] |

---

## Distribuição

[Lista de equipes/pessoas que devem receber o relatório]

## Instruções de Preenchimento

### Campos Obrigatórios
- Substitua todos os campos entre [colchetes] com informações específicas
- Mantenha a estrutura de tabelas para facilitar leitura
- Use datas no formato DD Mmm AAAA (ex: 14 Abr 2026)
- Use horários no formato HH:MM BRT

### Fontes de Informação
- **Azure DevOps**: Logs técnicos, tasks, commits
- **Zendesk**: Timeline de suporte, impacto a clientes
- **GitHub**: Histórico de código, procedures específicas
- **Teams/Reuniões**: Decisões e acordo de SMEs

### Qualidade das Ações
- **S**pecific: Ação claramente definida
- **M**easurable: Resultado mensurável
- **A**chievable: Realizável com recursos disponíveis  
- **R**elevant: Relevante para prevenir recorrência
- **T**ime-bound: Prazo específico definido