---
pattern_id: "basicos-duvida-tecnica"
vertical: basicos
root_cause: duvida_tecnica
module: geral
ticket_count: 40
ticket_ids: [95024, 129245, 146252, 146012, 147390, 147357, 147212, 147884, 149354, 149069, 148970, 152244, 153186, 154669, 154534, 157250, 156829, 158166, 157950, 157892, 157825, 157671, 158578, 161033, 160840, 160509, 161961, 162776, 162221, 164092, 167973, 167969, 167920, 167822, 167726, 168901, 171558, 174335, 176030, 175472]
last_occurrence: "2026-03-06"
keywords: ["integra\u00e7\u00e3o", "xml", "tax", "analyser", "52916", "problema", "rdp", "mastersaf", "cteep", "shopee"]
is_not_bug: false
---

# GERAL: Duvida Tecnica

## Descricao do Padrao
Clientes reportam problemas relacionados a: #52916| Problema RDP MasterSAF - CTEEP; Acesso OBI - ONESOURCE Brasil Integration; Configuração do OBI para buscar NF-e no Portal DFE

## Causa Raiz
Duvida Tecnica — classificacao baseada em 40 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Olá Renan, boa tarde!
&nbsp;
Infelizmente, não dispomos de um exemplo no momento. No entanto, as tags do XML referentes ao evento de cancelamento devem ser incorporadas ao XML completo da autorização.
&nbsp;
O arquivo final deve ser único, o que significa na prática é que o XML da nota fiscal (autorização) precisa ser complementado com as informações do evento de cancelamento que retornam da SEFAZ. Ou seja, o XML da nota autorizada deve ser editado para incluir as tags do evento de...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 176030 | 2026-02-27 | TOKEN ( CIAM ) p |
| 175472 | 2026-02-24 | Integração de XML Cancelado - OBI |
| 174335 | 2026-02-13 | Endpoint vazio |
| 171558 | 2026-01-27 | Falha no processamento do OBI ao identificar linhas com... |
| 168901 | 2026-01-12 | SAFX3007 - REGRA PARA PREENCHIMENTO DO CAMPO 27 -... |
| 167973 | 2026-01-06 | Credenciais para utilização do OBI na FINEP |
| 167969 | 2026-01-06 | Exemplo de delimitador de Perfil de Entrada - INTEGRADOR DFE |
| 167920 | 2026-01-05 | IFOOD | Liberação OBI |
| 167822 | 2026-01-05 | Integração - OBI |
| 167726 | 2026-01-05 | LINKs OBI GATEWAY PRODUÇÃO |

## Keywords para Matching
integração, xml, tax, analyser, 52916, problema, rdp, mastersaf, cteep, shopee
