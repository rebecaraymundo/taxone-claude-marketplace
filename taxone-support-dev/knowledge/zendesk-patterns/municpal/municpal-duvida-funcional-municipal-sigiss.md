---
pattern_id: "municpal-duvida-funcional-municipal-sigiss"
vertical: municpal
root_cause: duvida_funcional
module: municipal_sigiss
ticket_count: 16
ticket_ids: [5355, 5984, 19690, 30064, 41099, 50117, 72899, 95814, 98510, 99438, 107610, 117074, 136507, 144859, 160514, 162316]
last_occurrence: "2025-12-05"
keywords: ["issqn", "marilia", "santa", "barbara", "oeste", "atualiza\u00e7\u00e3o", "layout", "londrina", "iss", "municipal"]
is_not_bug: true
---

# MUNICIPAL SIGISS: Duvida Funcional

## Descricao do Padrao
Clientes reportam problemas relacionados a: ANIMA | Duvida Geração Situação da Nota - Arquivo Pouso Alegre; De-para Série - Piracicaba; ERRO GERAÇÃO MUNICIPAL SÃO GONÇALO - CAMPO Indicador de incidência do  ISS

## Causa Raiz
Duvida Funcional — classificacao baseada em 16 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde, Renata. Tudo bem?
&nbsp;
Desejo uma ótima semana a todos!
&nbsp;
Tentei contato por telefone (número 11 96862-8420), mas não obtive sucesso.
&nbsp;
Reforço que este ticket tem como foco o campo sn_iss_tributavel — Indicador de incidência do ISS. No print enviado com os erros, não identifiquei nenhuma referência específica a esse campo. O teste solicitado precisa ser ajustado manualmente no arquivo para obter a seguinte combinação:
&nbsp;
  cd_natureza_operacao = 2 (Tributação fora do...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 162316 | 2025-11-25 | SIGISS - São João do Meriti |
| 160514 | 2025-11-12 | Municipal de Tremembé - Erro na validação do arquivo |
| 144859 | 2025-07-24 | ERRO GERAÇÃO MUNICIPAL SÃO GONÇALO - CAMPO Indicador de... |
| 136507 | 2025-05-19 | LOG municipal Maceió |
| 117074 | 2024-11-21 | De-para Série - Piracicaba |
| 107610 | 2024-08-16 | Municipal Marília-SP não gera o Meio Magnético |
| 99438 | 2024-05-14 | Geração do Magnetico SIGISS |
| 98510 | 2024-05-03 | SIGISS - LONDRINA |
| 95814 | 2024-04-05 | Municípal - Notas Retenção de ISS. |
| 72899 | 2023-07-07 | ISS - SIGISS |

## Keywords para Matching
issqn, marilia, santa, barbara, oeste, atualização, layout, londrina, iss, municipal
