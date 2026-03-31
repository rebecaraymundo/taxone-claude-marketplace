---
pattern_id: "municpal-falha-de-produto-municipal-dmste"
vertical: municpal
root_cause: falha_de_produto
module: municipal_dmste
ticket_count: 9
ticket_ids: [17183, 149379, 152129, 154859, 157723, 160418, 161468, 168078, 169519]
last_occurrence: "2026-02-26"
keywords: ["dmst", "campo", "gera\u00e7\u00e3o", "arquivo", "xml", "erro", "salvar", "dmste_canoas", "c\u00f3digo", "servi\u00e7o"]
is_not_bug: false
---

# MUNICIPAL DMSTE: Falha De Produto

## Descricao do Padrao
Clientes reportam problemas relacionados a: DMST - Campo Bom - Geração Arquivo XML; DMSTE_CANOAS - Código de serviço não preenchido (erro 5072 : O Serviço Municipal deve ser informado. (item: 1)."); Decorrente do ticket #154859 - Municipais: Eventual Canoas - Tag ImRemetente

## Causa Raiz
Falha De Produto — classificacao baseada em 9 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde, Eunice! Tudo bem?
&nbsp;
Obrigada pelo retorno.
&nbsp;
Após suas informações, refiz os testes tanto na minha base quanto na base do cliente, utilizando o mesmo parâmetro, e obtive o mesmo comportamento. Identifiquei o seguinte padrão:
&nbsp;
  No arquivo com a data de emissão do documento diferente do período de geração do arquivo, &nbsp;não apresenta a tag ImRemetente:  &nbsp;

&nbsp;
  No arquivo com a data de emissão do documento dentro do período de geração, ocorre a duplicidade...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 169519 | 2026-01-14 | Municipal - Inconsistência arquivo magnético - Prefeitura... |
| 168078 | 2026-01-06 | Municipal - Canoas - DMSTE - Tag ImRemetente gerando em... |
| 161468 | 2025-11-18 | Decorrente do ticket #154859 - Municipais: Eventual Canoas... |
| 160418 | 2025-11-11 | Municipal Caxias do Sul - Geração do arquivo por competência |
| 157723 | 2025-10-24 | Municipal Caxias do Sul |
| 154859 | 2025-10-07 | Municipais: Eventual Canoas |
| 152129 | 2025-09-16 | DMSTE_CANOAS - Código de serviço não preenchido (erro 5072... |
| 149379 | 2025-08-28 | Erro ao salvar arquivo Campo Bom |
| 17183 | 2021-07-23 | DMST - Campo Bom - Geração Arquivo XML |

## Keywords para Matching
dmst, campo, geração, arquivo, xml, erro, salvar, dmste_canoas, código, serviço
