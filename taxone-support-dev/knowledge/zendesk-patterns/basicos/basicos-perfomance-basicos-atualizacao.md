---
pattern_id: "basicos-perfomance-basicos-atualizacao"
vertical: basicos
root_cause: perfomance
module: basicos_atualizacao
ticket_count: 5
ticket_ids: [80812, 97291, 98371, 109386, 125731]
last_occurrence: "2025-02-27"
keywords: ["lentid\u00e3o", "diversos", "processos", "padr\u00e3o", "customizados", "patch", "292", "instabilidade", "tax", "one"]
is_not_bug: false
---

# BASICOS ATUALIZACAO: Perfomance

## Descricao do Padrao
Clientes reportam problemas relacionados a: Erro no processo de Equalização Patch 295.1.1; Instabilidade na TAX ONE - Empresas não estão aparecendo; Lentidão em diversos processos padrão e processos customizados

## Causa Raiz
Perfomance — classificacao baseada em 5 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Prezado(a) Alaessandra
&nbsp;
Estamos verificando com nosso time de desenvolvimento a inclusão do paralell para esta crição de indice da tabela X01_CONTABIL ;
&nbsp;
A tabela "X01_CONTABIL " é uma das maiores do sistema;
O tempo de criação do índices e constraints estão relacionados ao tamanho da tabela;
&nbsp;
Nossa sugestão era seguir os passos abaixo
&nbsp;
1 - Favor conectar no SQL*Plus com o usuário dono (owner) do Mastersaf DW, executar o script abaixo;
&nbsp;
a) realizar um novo resize...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 125731 | 2025-02-12 | Lentidão na atualização de Patch |
| 109386 | 2024-09-06 | Erro no processo de Equalização Patch 295.1.1 |
| 98371 | 2024-05-02 | Instabilidade na TAX ONE - Empresas não estão aparecendo |
| 97291 | 2024-04-19 | Patch 292.0.1 |
| 80812 | 2023-10-10 | Lentidão em diversos processos padrão e processos... |

## Keywords para Matching
lentidão, diversos, processos, padrão, customizados, patch, 292, instabilidade, tax, one
