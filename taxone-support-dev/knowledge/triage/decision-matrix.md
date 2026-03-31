# Matriz de Decisao - Triagem PM

Documento de referencia rapida para o agente `taxone-pm`.

---

## Thresholds de Scoring por Veredicto

| Veredicto | Confianca Min | Threshold de Score | Descricao |
|-----------|--------------|-------------------|-----------|
| **CONFIRMED_BUG** | 70% | NOT_A_BUG < 30, FEATURE < 25, INCOMPLETE < 30, DUPLICATE < 35 | Todos os scores abaixo dos limites |
| **NOT_A_BUG** | 75% | NOT_A_BUG >= 55 | Sinais fortes de que nao e bug |
| **FEATURE_REQUEST** | 80% | FEATURE >= 40 | Keywords e ausencia de implementacao atual |
| **INCOMPLETE_ANALYSIS** | 80% | INCOMPLETE >= 45 | Dados insuficientes para analise |
| **DUPLICATE** | 85% | DUPLICATE >= 60 | Match forte com solucao existente |
| **NEEDS_INFO** | N/A | Nenhum threshold atingido OU sinais conflitantes | Precisa de mais informacoes |

---

## Regras de Combinacao de Sinais

### Regra 1: NOT_A_BUG requer convergencia
Para emitir NOT_A_BUG com confianca >= 75%, pelo menos **2 das 3** fontes devem concordar:
- FAQ Triage (score >= 15)
- Zendesk Patterns (not-a-bug flag = true)
- Business Rules (comportamento esperado documentado)

### Regra 2: FEATURE_REQUEST requer keyword + ausencia
Para emitir FEATURE_REQUEST:
- Keywords de feature detectadas (score >= 25) **E**
- Nenhum package/procedure implementa a funcionalidade descrita

### Regra 3: DUPLICATE requer match especifico
Para emitir DUPLICATE:
- Match em solutions/ ou ado-fixes/ com **mesmo erro** (nao apenas mesmo modulo)
- Correspondencia ALTA (>= 85% de similaridade nos termos-chave)

### Regra 4: Conflito NOT_A_BUG vs CONFIRMED_BUG
Se FAQ score >= 15 **MAS** Zendesk nao tem flag not-a-bug:
- Emitir NEEDS_INFO (nao NOT_A_BUG automatico)
- Solicitar confirmacao do cenario com o usuario

### Regra 5: Prioridade de veredictos
Se multiplos thresholds atingidos simultaneamente:
1. DUPLICATE (prioridade maxima - ja resolvido)
2. INCOMPLETE_ANALYSIS (precisa de dados antes de qualquer analise)
3. NOT_A_BUG
4. FEATURE_REQUEST
5. CONFIRMED_BUG (default se nenhum outro se aplica com confianca)

---

## Sinais e Pesos Detalhados

### Sinais NOT_A_BUG

| Sinal | Peso | Fonte |
|-------|------|-------|
| FAQ score >= 15 | +30 pts | faq_triage.py |
| FAQ score 10-14 | +15 pts | faq_triage.py |
| Zendesk pattern not-a-bug > 50 tickets | +25 pts | zendesk-patterns/ |
| Zendesk pattern not-a-bug 20-50 tickets | +15 pts | zendesk-patterns/ |
| Business rule confirma comportamento esperado | +30 pts | business-rules/, webhelp/ |
| WebHelp documenta o comportamento como correto | +20 pts | webhelp/ |

### Sinais FEATURE_REQUEST

| Sinal | Peso | Fonte |
|-------|------|-------|
| Keywords primarias no titulo | +15 pts | Analise de texto |
| Keywords primarias na descricao | +10 pts | Analise de texto |
| Keywords secundarias | +10 pts | Analise de texto |
| Sem package implementando funcionalidade | +30 pts | Busca no codigo |

### Sinais DUPLICATE

| Sinal | Peso | Fonte |
|-------|------|-------|
| Match em solutions/INDEX.md | +35 pts | solutions/ |
| Match em ado-fixes/ com mesmo erro | +30 pts | ado-fixes/ |
| Titulo quase identico a WI resolvida | +25 pts | Analise de texto |

### Sinais INCOMPLETE_ANALYSIS

| Sinal | Peso | Fonte |
|-------|------|-------|
| ReproSteps vazio | +30 pts | Campo do WI |
| Sem identificacao de ambiente | +20 pts | Campo do WI |
| Sem evidencias (screenshots/logs) | +15 pts | Campo do WI |
| Sem dados de teste (CNPJ, empresa) | +10 pts | Campo do WI |
| Descricao vaga sem erro especifico | +10 pts | Analise de texto |

---

## Checklist de Qualidade N1/N2

Para avaliar se o WI tem informacoes suficientes para analise N3:

- [ ] **ReproSteps presentes** - Passos claros de reproducao (nao apenas "da erro")
- [ ] **Ambiente identificado** - Producao/Homologacao, versao do TAX ONE, banco Oracle
- [ ] **Evidencias** - Screenshots da tela de erro, logs do servidor, mensagem exata
- [ ] **Dados de teste** - CNPJ/empresa afetada, periodo fiscal, tipo de nota
- [ ] **Erro especifico** - Mensagem de erro exata (ORA-XXXX, stack trace, codigo)
- [ ] **Impacto descrito** - Quantos clientes afetados, workaround existente?
- [ ] **Comportamento esperado** - O que deveria acontecer vs o que acontece

**Score de incompletude:**
- 0-20: Aceitavel (pode ter gaps menores)
- 25-44: Incompleto (recomendavel pedir mais info)
- 45+: Muito incompleto (devolver para N1/N2)

---

## Keywords de Feature Request

### Keywords Primarias (forte sinal)
- "adicionar", "incluir", "novo campo", "nova coluna", "nova tela"
- "criar funcionalidade", "implementar novo", "desenvolver"
- "permitir que", "possibilitar", "habilitar"
- "nova regra", "novo calculo", "novo layout"

### Keywords Secundarias (sinal moderado)
- "melhorar", "aprimorar", "otimizar"
- "alterar comportamento para", "mudar regra para"
- "integrar com", "exportar para novo", "importar de novo"
- "personalizar", "configurar novo"

### Keywords de Exclusao (reduz score de feature)
- "parou de funcionar", "deixou de", "nao funciona mais"
- "erro", "exception", "ORA-", "crash", "travou"
- "regressao", "voltou a", "antes funcionava"

---

## Templates de Resposta por Veredicto

### NOT_A_BUG - Sugestao de Resposta ao Cliente
```
Prezado(a),

Apos analise detalhada, identificamos que o comportamento reportado esta funcionando
conforme projetado (As Designed).

{Explicacao do comportamento esperado}

{Orientacao de configuracao/parametrizacao se aplicavel}

Caso tenha duvidas adicionais, estamos a disposicao.

Atenciosamente,
Equipe TAX ONE
```

### FEATURE_REQUEST - Sugestao de Reclassificacao
```
Este work item descreve uma funcionalidade nova (feature request) e nao um defeito
no comportamento atual do sistema.

Sugestao: Reclassificar como User Story/Feature e direcionar para o backlog de produto.

Descricao para o backlog:
- Funcionalidade: {descricao}
- Modulo: {modulo}
- Justificativa de negocio: {extraida do WI}
```

### INCOMPLETE_ANALYSIS - Feedback para N1/N2
```
O work item #{ID} necessita de informacoes adicionais antes de ser escalado para N3.

Itens faltantes:
{lista de itens conforme template n1-n2-quality-template.md}

Por favor, complemente a analise e reabra o chamado.
```

### DUPLICATE - Referencia ao WI Original
```
Este work item e duplicata do #{ORIGINAL_ID}, que ja foi resolvido.

Solucao aplicada: {resumo da solucao}
Referencia: {link para solucao}

Recomendacao: Fechar como duplicata referenciando #{ORIGINAL_ID}.
```
