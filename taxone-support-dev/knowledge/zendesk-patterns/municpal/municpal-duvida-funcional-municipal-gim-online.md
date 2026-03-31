---
pattern_id: "municpal-duvida-funcional-municipal-gim-online"
vertical: municpal
root_cause: duvida_funcional
module: municipal_gim_online
ticket_count: 3
ticket_ids: [98647, 143519, 155378]
last_occurrence: "2025-11-25"
keywords: ["validador", "divergente", "utilizado", "cliente", "thomson", "erro", "arquivo", "paulinia"]
is_not_bug: true
---

# MUNICIPAL GIM ONLINE: Duvida Funcional

## Descricao do Padrao
Clientes reportam problemas relacionados a: Erro arquivo Paulinia; Re: Erro arquivo Paulinia; Validador divergente entre utilizado pelo cliente x Thomson (Município Porto Velho RO)

## Causa Raiz
Duvida Funcional — classificacao baseada em 3 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Oi Daniel, boa tarde!
Espero que esteja bem.
&nbsp;
Obrigada pelo retorno.
&nbsp;
Segue regra para gerar a tag &lt;tipos:ItemListaServico&gt;:
&nbsp;
Verificar o código de serviço informado na nota fiscal (campo COD_SERVICO da tabela SAFX09) e dele deve ser recuperado o código da Lei Complementar 116/03 (campo cod_serv_lei_116 da tabela SAFX2018 - Módulo: BÁSICOS &gt; DATA WAREHOUSE &gt; Manutenção &gt; Códigos &gt; Serviços) correspondente a esse código.
&nbsp;
Por favor...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 155378 | 2025-10-09 | Erro arquivo Paulinia |
| 143519 | 2025-07-14 | Re: Erro arquivo Paulinia |
| 98647 | 2024-05-06 | Validador divergente entre utilizado pelo cliente x Thomson... |

## Keywords para Matching
validador, divergente, utilizado, cliente, thomson, erro, arquivo, paulinia
