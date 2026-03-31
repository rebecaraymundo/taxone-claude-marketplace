---
pattern_id: "sped-falha-de-dados-de-ou-parametros-estadual-ativo-permanente"
vertical: sped
root_cause: falha_de_dados_de_ou_parametros
module: estadual_ativo_permanente
ticket_count: 2
ticket_ids: [13797, 80547]
last_occurrence: "2023-10-23"
keywords: ["registro", "0300", "efd", "icms", "ipi", "k200", "n\u00e3o", "gera", "acelen"]
is_not_bug: false
---

# ESTADUAL ATIVO PERMANENTE: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: K200 - NÃO GERA - ACELEN; REGISTRO 0300 - EFD ICMS IPI - CAMPO 07 - NUMERO TOTAL DE PARCELAS

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 2 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Renato, boa tarde!
&nbsp;
Conforme acesso remoto realizado ontem, verifiquei internamente a regra para geração do campo 07 do registro 0300 do Sped Fiscal e segue o parecer:
&nbsp;
Para considerar a parametrização do Cadastro do Estabelecimento no CIAP, o campo "Nº Parcelas a serem apropriadas com direito ao ICMS" da SAFX13 (Módulo Básicos&gt; Data Warehouse&gt; Manutenção&gt; Cadastros&gt;
Bem Patrimonial) precisa estar em branco. Se houver algum número preenchido, será considerado este número...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 80547 | 2023-10-06 | K200 - NÃO GERA - ACELEN |
| 13797 | 2021-06-16 | REGISTRO 0300 - EFD ICMS IPI - CAMPO 07 - NUMERO TOTAL DE... |

## Keywords para Matching
registro, 0300, efd, icms, ipi, k200, não, gera, acelen
