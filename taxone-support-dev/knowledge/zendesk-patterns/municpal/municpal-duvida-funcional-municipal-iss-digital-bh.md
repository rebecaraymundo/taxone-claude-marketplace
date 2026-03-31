---
pattern_id: "municpal-duvida-funcional-municipal-iss-digital-bh"
vertical: municpal
root_cause: duvida_funcional
module: municipal_iss_digital_bh
ticket_count: 3
ticket_ids: [8049, 36573, 41520]
last_occurrence: "2022-06-02"
keywords: ["gera\u00e7\u00e3o", "incorreta", "m\u00f3dulo", "belo", "horizonte", "des", "notas", "recebidas", "erro", "formato"]
is_not_bug: true
---

# MUNICIPAL ISS DIGITAL BH: Duvida Funcional

## Descricao do Padrao
Clientes reportam problemas relacionados a: DES-BH Erro no formato do campo 11 Registro Tipo R; DES-BH notas recebidas; Geração incorreta - Módulo Belo Horizonte

## Causa Raiz
Duvida Funcional — classificacao baseada em 3 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Edilson. boa tarde!

Conforme analisei o erro em questão do validador, o problema não está no campo 15 e sim na alíquota que você informou, o validador não está aceitando a mesma
para empresa de regime normal (não optante do simples) com incidência do imposto em Belo Horizonte.

Como a estrutura dos campos e o arquivo está sendo gerado corretamente pelo DW, conforma Manual de Layout 3.0 (coloquei em anexo), por gentileza entrar em contato com a prefeitura
de Belo Horizonte e verificar o motivo...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 41520 | 2022-05-19 | DES-BH Erro no formato do campo 11 Registro Tipo R |
| 36573 | 2022-03-16 | DES-BH notas recebidas |
| 8049 | 2021-04-12 | Geração incorreta - Módulo Belo Horizonte |

## Keywords para Matching
geração, incorreta, módulo, belo, horizonte, des, notas, recebidas, erro, formato
