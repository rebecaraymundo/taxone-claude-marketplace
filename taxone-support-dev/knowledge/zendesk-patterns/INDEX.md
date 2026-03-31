# Zendesk Patterns Knowledge Base

> Base de conhecimento gerada automaticamente a partir de tickets Zendesk resolvidos.
> Ultima atualizacao: 2026-03-09T09:50:02Z

## Estatisticas

| Metrica | Valor |
|---------|-------|
| Total de patterns | 1226 |
| Total de tickets | 55294 |
| Patterns "Not-a-Bug" | 152 |
| Verticals cobertas | 7 |

## Por Vertical

| Vertical | Patterns | Tickets | Not-a-Bug |
|----------|----------|---------|-----------|
| [basicos](basicos/INDEX.md) | 224 | 25899 | 17 |
| [especificos](especificos/INDEX.md) | 59 | 684 | 7 |
| [estadual](estadual/INDEX.md) | 349 | 7494 | 40 |
| [federal](federal/INDEX.md) | 123 | 2282 | 19 |
| [municpal](municpal/INDEX.md) | 290 | 2544 | 45 |
| [sped](sped/INDEX.md) | 167 | 15962 | 23 |
| [utilitarios](utilitarios/INDEX.md) | 14 | 429 | 1 |

## Top Patterns "Not-a-Bug"

Patterns mais frequentes onde o problema NAO e bug (duvida funcional, parametrizacao, etc.):

| Pattern | Vertical | Tickets | Causa Raiz |
|---------|----------|---------|-----------|
| [sped-duvida-funcional-sped-efd-reinf](sped/sped-duvida-funcional-sped-efd-reinf.md) | sped | 1410 | duvida_funcional |
| [sped-duvida-funcional-sped-efd-escrituração-fiscal-digital](sped/sped-duvida-funcional-sped-efd-escrituração-fiscal-digital.md) | sped | 1046 | duvida_funcional |
| [sped-duvida-funcional-sped-efd-escrituração-fiscal-digital-das-contribuições](sped/sped-duvida-funcional-sped-efd-escrituração-fiscal-digital-das-contribuições.md) | sped | 834 | duvida_funcional |
| [estadual-duvida-funcional-estadual-icms](estadual/estadual-duvida-funcional-estadual-icms.md) | estadual | 762 | duvida_funcional |
| [basicos-duvida-funcional-basicos-job-servidor](basicos/basicos-duvida-funcional-basicos-job-servidor.md) | basicos | 623 | duvida_funcional |
| [basicos-duvida-funcional-basicos-data-warehouse](basicos/basicos-duvida-funcional-basicos-data-warehouse.md) | basicos | 435 | duvida_funcional |
| [sped-duvida-funcional-sped-escrituração-contábil-digital](sped/sped-duvida-funcional-sped-escrituração-contábil-digital.md) | sped | 430 | duvida_funcional |
| [federal-duvida-funcional-federal-obrigações-de-tributos-federais](federal/federal-duvida-funcional-federal-obrigações-de-tributos-federais.md) | federal | 352 | duvida_funcional |
| [basicos-duvida-funcional-basicos-report-fiscal](basicos/basicos-duvida-funcional-basicos-report-fiscal.md) | basicos | 280 | duvida_funcional |
| [basicos-duvida-funcional-basicos-ferramentas](basicos/basicos-duvida-funcional-basicos-ferramentas.md) | basicos | 226 | duvida_funcional |
| [estadual-duvida-funcional-estadual-ativo-permanente](estadual/estadual-duvida-funcional-estadual-ativo-permanente.md) | estadual | 139 | duvida_funcional |
| [municpal-duvida-funcional-municipal-iss](municpal/municpal-duvida-funcional-municipal-iss.md) | municpal | 112 | duvida_funcional |
| [estadual-duvida-funcional-estadual-dime-sc](estadual/estadual-duvida-funcional-estadual-dime-sc.md) | estadual | 105 | duvida_funcional |
| [municpal-duvida-funcional-municipal-giss-online](municpal/municpal-duvida-funcional-municipal-giss-online.md) | municpal | 104 | duvida_funcional |
| [estadual-duvida-funcional-estadual-gia-sp](estadual/estadual-duvida-funcional-estadual-gia-sp.md) | estadual | 102 | duvida_funcional |
| [federal-duvida-funcional-federal-ipi](federal/federal-duvida-funcional-federal-ipi.md) | federal | 88 | duvida_funcional |
| [basicos-duvida-funcional-administration](basicos/basicos-duvida-funcional-administration.md) | basicos | 86 | duvida_funcional |
| [estadual-duvida-funcional-estadual-fci](estadual/estadual-duvida-funcional-estadual-fci.md) | estadual | 76 | duvida_funcional |
| [basicos-duvida-funcional-basicos-tax-automation](basicos/basicos-duvida-funcional-basicos-tax-automation.md) | basicos | 76 | duvida_funcional |
| [federal-duvida-funcional-federal-controle-de-obrigações-federal](federal/federal-duvida-funcional-federal-controle-de-obrigações-federal.md) | federal | 75 | duvida_funcional |

## Uso

Esta knowledge base e consumida pelo `taxone-architect` (Phase 2) e pelo pipeline
`taxone-us-auto-implement` (Phase 0.6.6) para:

1. **Identificar "not a bug"** antes de iniciar implementacao
2. **Encontrar resolucoes similares** em tickets passados
3. **Enriquecer contexto** do architect com padroes conhecidos
