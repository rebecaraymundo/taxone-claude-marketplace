---
pattern_id: "basicos-solicitacao-de-servico-basicos-tr-transfer-files"
vertical: basicos
root_cause: solicitacao_de_servico
module: basicos_tr_transfer_files
ticket_count: 16
ticket_ids: [66085, 73780, 89316, 91873, 96109, 96772, 97948, 102972, 105990, 106887, 108453, 109968, 109898, 116290, 118265, 171038]
last_occurrence: "2026-02-10"
keywords: ["dump", "tax", "one", "clarios", "arquivos", "safx", "carregados", "via", "transfer", "cpfl"]
is_not_bug: false
---

# BASICOS TR TRANSFER FILES: Solicitacao De Servico

## Descricao do Padrao
Clientes reportam problemas relacionados a: A TR pode compartilhar arquivos exemplos dos novos impostos da reforma (SAFX3007 - SAFX3008 - SAFX3009); Alteração de senha do usuário intg_taxone_alcon do ambiente de Testes/Produção; Arquivos (Safx) carregados via TR Transfer Files não aparecem no TAX ONE para serem importados

## Causa Raiz
Solicitacao De Servico — classificacao baseada em 16 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Bom dia Thiago, tudo bem?
&nbsp;
Conforme realizado o acesso remoto, verificamos que o problema na tela de cadastro que ficava travado em lopping, estava sendo causado por conta das variáveis de ambientes, que possui no JAVA_HOME o caminho do antigo java instalado na máquina. Após ajuste, foi possível completar o cadastro e realizar teste de envio dos arquivos pela ferramenta TR Transfer Files, onde os mesmos chegou ao tax one certinho.
&nbsp;
Com isso alinhamos o encerramento deste...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 171038 | 2026-01-23 | A TR pode compartilhar arquivos exemplos dos novos impostos... |
| 118265 | 2024-12-03 | Erro ao iniciar servicos TR Transfer files |
| 116290 | 2024-11-13 | PETROCOQUE - TRANSFER FILES |
| 109968 | 2024-09-13 | Alteração de senha do usuário intg_taxone_alcon do ambiente... |
| 109898 | 2024-09-13 | TR TRANSFER |
| 108453 | 2024-08-27 | MAGALU CLOUD| TR FILES| Ambiente de homologação indisponível |
| 106887 | 2024-08-07 | Erro de acesso ao portal do TR Transfer File de fora do... |
| 105990 | 2024-07-26 | TR Transfer File não está usando diretório configurado |
| 102972 | 2024-06-24 | NETSHOES| TAXONE| Erro instalação ferramenta TR File|... |
| 97948 | 2024-04-26 | SFTP TR TRANSFER FILES COM FALHAS |

## Keywords para Matching
dump, tax, one, clarios, arquivos, safx, carregados, via, transfer, cpfl
