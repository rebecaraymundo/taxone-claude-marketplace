---
pattern_id: "estadual-deficiencia-de-documentacao-estadual-gia-sp"
vertical: estadual
root_cause: deficiencia_de_documentacao
module: estadual_gia_-_sp
ticket_count: 9
ticket_ids: [24691, 27564, 33507, 38703, 48597, 65493, 66752, 69089, 75392]
last_occurrence: "2023-09-21"
keywords: ["erro", "importa\u00e7\u00e3o", "gia", "ref", "lan\u00e7amentos", "e113", "sped", "preenchimento", "nota", "fiscal"]
is_not_bug: false
---

# ESTADUAL GIA - SP: Deficiencia De Documentacao

## Descricao do Padrao
Clientes reportam problemas relacionados a: A geração dos registros está excluindo os dados inseridos via tela de manutenção; CFOPS de exportação não estão subindo para GIA SP; Chamados Difal outros débito e outros crédito para SP

## Causa Raiz
Deficiencia De Documentacao — classificacao baseada em 9 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Olá Humberto, boa tarde!
Tudo bem?
&nbsp;
Verificamos essa situação, e de fato, não existe opção para manter os registros digitados via tela de manutenção, uma vez que todos são "amarrados" a fim de evitar erros na obrigação, e todos refletem na geração do Registro CR=05. Da mesma forma que o CR=28 é "filho" do CR=20, praticamente todos demais registros são filhos do CR=05, o qual é reprocessado por ocasião de nova 'Geração dos Registros'.
Orientamos que as manutenções sejam pontualmente, e que...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 75392 | 2023-08-09 | A geração dos registros está excluindo os dados inseridos... |
| 69089 | 2023-05-19 | Re: Re: GIA-SP Registro 18- Zona Franca de Manaus |
| 66752 | 2023-04-20 | Re: GIA-SP Registro 18- Zona Franca de Manaus |
| 65493 | 2023-04-05 | CFOPS de exportação não estão subindo para GIA SP |
| 48597 | 2022-08-19 | Chamados Difal outros débito e outros crédito para SP |
| 38703 | 2022-04-13 | GIA- SP |
| 33507 | 2022-02-09 | GIA SP |
| 27564 | 2021-11-30 | E113 do SPED - Preenchimento da nota fiscal de... |
| 24691 | 2021-10-21 | erro na importação da gia ref. lançamentos complementares |

## Keywords para Matching
erro, importação, gia, ref, lançamentos, e113, sped, preenchimento, nota, fiscal
