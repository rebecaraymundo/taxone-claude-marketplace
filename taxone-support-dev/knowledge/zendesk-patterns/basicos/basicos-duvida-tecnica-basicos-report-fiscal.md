---
pattern_id: "basicos-duvida-tecnica-basicos-report-fiscal"
vertical: basicos
root_cause: duvida_tecnica
module: basicos_report_fiscal
ticket_count: 65
ticket_ids: [4977, 4706, 6622, 8165, 10734, 19025, 20713, 21720, 22869, 22706, 22565, 23493, 26634, 26525, 27184, 31285, 33016, 35527, 38762, 47387, 49046, 50163, 51285, 54782, 60300, 64950, 66621, 71966, 72678, 84480, 87562, 88557, 91060, 95582, 97684, 98636, 98630, 98527, 98287, 98973, 102160, 104714, 104597, 104481, 106866, 106847, 106576, 106554, 106513, 106512, 107262, 107174, 111749, 114458, 114826, 117703, 124725, 137759, 139039, 144353, 149111, 150982, 163523, 169419, 172760]
last_occurrence: "2026-02-20"
keywords: ["relatorio", "gera\u00e7\u00e3o", "datamart", "power", "lock", "relat\u00f3rio", "cfop", "modelo", "formato", "xls"]
is_not_bug: false
---

# BASICOS REPORT FISCAL: Duvida Tecnica

## Descricao do Padrao
Clientes reportam problemas relacionados a: Baixa do arquivo diario; Conferência de Documentos Fiscais (ICMS/IPI/PIS/COFINS) - Formato XLS; Conferência de Relatório de NF p/ CFOP - Cibrafertil

## Causa Raiz
Duvida Tecnica — classificacao baseada em 65 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Caros, bom dia!
&nbsp;
Jonathan após análise realizada na lógica e funcionamento, segue esclarecimentos:
&nbsp;
Executar a validação com intervalo menor (mensal)
&nbsp;
   A Lógica do programa, &nbsp;indica que o relatório foi projetado para faixas curtas (até 31 dias) por questões de performance.  &nbsp;   Validar mês a mês reduz o risco de encontrar lacunas causadas por notas lançadas posteriormente. Tanto que realizamos um teste interno filtrando mês a mês e o problema não foi apresentado. ...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 172760 | 2026-02-04 | Total de documentos |
| 169419 | 2026-01-14 | Inconsistência na geração de relatórios na aba de... |
| 163523 | 2025-12-03 | Relatório de Sequência de Notas - Divergência Geração |
| 150982 | 2025-09-09 | [TD Soluções] -  |
| 149111 | 2025-08-27 | Conferência de Documentos Fiscais (ICMS/IPI/PIS/COFINS) -... |
| 144353 | 2025-07-21 | Processos não finalizados |
| 139039 | 2025-06-05 | Problema é capa sem item e o item não importa, pois no... |
| 137759 | 2025-05-28 | Problemas na importacao, esta aparecendo varias vezes um... |
| 124725 | 2025-02-05 | Módulo Report Fiscal > Gerenciais > Documentos Fiscais >... |
| 117703 | 2024-11-27 | [B&D] - Valores do ICMS Origem e Destino (Partilha e... |

## Keywords para Matching
relatorio, geração, datamart, power, lock, relatório, cfop, modelo, formato, xls
