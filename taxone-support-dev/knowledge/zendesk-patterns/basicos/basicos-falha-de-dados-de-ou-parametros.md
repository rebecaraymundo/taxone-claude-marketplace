---
pattern_id: "basicos-falha-de-dados-de-ou-parametros"
vertical: basicos
root_cause: falha_de_dados_de_ou_parametros
module: geral
ticket_count: 42
ticket_ids: [145714, 147383, 147308, 147095, 147036, 146872, 150972, 153236, 153185, 153942, 155533, 155495, 156911, 158149, 158145, 158789, 159551, 159299, 159141, 158968, 161129, 161816, 161437, 161293, 162768, 162609, 163600, 163448, 163443, 165255, 164747, 166554, 168124, 167894, 167743, 170827, 170525, 170472, 170129, 174209, 174018, 175256]
last_occurrence: "2026-03-07"
keywords: ["ipiranga", "integra\u00e7\u00e3o", "obi", "job", "servidor", "nadir", "erro", "obti", "status", "processamento"]
is_not_bug: false
---

# GERAL: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: Botões reenviar e reprocessamento no integrador do OBI; Cirion - Acesso negado ao utilizar o Sender; Ctes enviadas pelo SENDER não aparecem no OBI e nem no Tax One

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 42 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde, Rogério!!
&nbsp;
Primeiro ponto identificado no lote original:&nbsp;OBI-2391b712b55e4c909555d10ea828cc43

Ao criar e enviar os arquivos estão sendo informando como codProcessamento duas vezes a SAFX08 conforme imagem de log a seguir:


Isso gera um processamento duplo da SAFX08, gerando 2 arquivos de saída para o tax one com o mesmo conteúdo e levando a mensagens de erro do lado do tax one em relação a duplicidade de envio.




Outro ponto importante identificado foi o envio de...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 175256 | 2026-02-23 | Erro integração lotes CT-es Cancelados |
| 174209 | 2026-02-12 | OBI - INTEGRAÇÃO SAFX02 |
| 174018 | 2026-02-11 | DPSP - Erro Reprocessamento OBI - Sequência Itens |
| 170827 | 2026-01-21 | Botões reenviar e reprocessamento no integrador do OBI |
| 170525 | 2026-01-20 | [Renner] - Erro ao tentar enviar dados via API do OBI |
| 170472 | 2026-01-20 | OBI - Extração não chega no OBI |
| 170129 | 2026-01-16 | Martins- Retorno endpoint com valores vazios  |
| 168124 | 2026-01-06 | Integração Oracle X OBI com erro |
| 167894 | 2026-01-05 | The taxone cannot receive data from SAP. |
| 167743 | 2026-01-05 | Identiicação de Duplicidade Processamento SAFXs OBI |

## Keywords para Matching
ipiranga, integração, obi, job, servidor, nadir, erro, obti, status, processamento
