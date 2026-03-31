---
pattern_id: "municpal-falha-de-ambiente-do-cliente-municipal-iss"
vertical: municpal
root_cause: falha_de_ambiente_do_cliente
module: municipal_iss
ticket_count: 12
ticket_ids: [31688, 34623, 35351, 49503, 57809, 61477, 62978, 101272, 115571, 116089, 152344, 171532]
last_occurrence: "2026-02-11"
keywords: ["municipal", "hoff", "iss", "relat\u00f3rio", "apoio", "m\u00f3dulos", "municipais", "bel\u00e9m", "campo", "grande"]
is_not_bug: false
---

# MUNICIPAL ISS: Falha De Ambiente Do Cliente

## Descricao do Padrao
Clientes reportam problemas relacionados a: "Tag <ValorTotal> incorreta na primeira NF" ; Apuração de ISS realizada e não atualiza calendário para “validar” de dois estabelecimentos ; ISS Brasilia

## Causa Raiz
Falha De Ambiente Do Cliente — classificacao baseada em 12 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Olá, Mauro!&nbsp;
Espero que esteja tudo bem com você.
&nbsp;
Realizamos uma análise na parametrização do tipo de documento em sua base e identificamos que existe uma configuração para o tipo "NFS4" com a opção "1", datada de 01/02/2000. Por esse motivo, essa opção está sendo utilizada na geração do arquivo meio magnético.
&nbsp;
Efetuamos alguns testes e, ao excluir essa parametrização de fevereiro, verificamos que o campo passou a ser preenchido com a opção "4". Observamos também que a...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 171532 | 2026-01-27 | arquivos NFTS não sobem na prefeitura |
| 152344 | 2025-09-17 | Notas de serviço de importação |
| 116089 | 2024-11-12 | ORA - 12154 |
| 115571 | 2024-11-07 | Livrio 501 ISS aparece imposto devido ao inves de Imposto... |
| 101272 | 2024-06-06 | ISS Fazenda Rio Grande (PR). Log de Erro da Prefeitura com... |
| 62978 | 2023-03-03 | ISS JACAREÍ - NÃO ESTÁ SUMARIZANDO OS ITENS COM CÓDIGO DA... |
| 61477 | 2023-02-13 | "Tag <ValorTotal> incorreta na primeira NF"  |
| 57809 | 2022-12-27 | Impressão Livro ISS |
| 49503 | 2022-08-31 | ISS Brasilia |
| 35351 | 2022-03-02 | Apuração de ISS realizada e não atualiza calendário para... |

## Keywords para Matching
municipal, hoff, iss, relatório, apoio, módulos, municipais, belém, campo, grande
