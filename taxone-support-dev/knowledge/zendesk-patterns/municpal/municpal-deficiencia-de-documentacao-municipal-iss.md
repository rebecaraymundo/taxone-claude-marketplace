---
pattern_id: "municpal-deficiencia-de-documentacao-municipal-iss"
vertical: municpal
root_cause: deficiencia_de_documentacao
module: municipal_iss
ticket_count: 5
ticket_ids: [23769, 23963, 25682, 28497, 65829]
last_occurrence: "2023-05-02"
keywords: ["erro", "importa\u00e7\u00e3o", "munic\u00edpio", "tatui", "campo", "cidade", "rio", "verde", "gera\u00e7\u00e3o", "arquivos"]
is_not_bug: false
---

# MUNICIPAL ISS: Deficiencia De Documentacao

## Descricao do Padrao
Clientes reportam problemas relacionados a: Arquivo txt  - Ribeirão Preto (Obrigações municipais); Campo Cidade - Rio Verde (GO); Erro na Importação do Município de Tatui

## Causa Raiz
Deficiencia De Documentacao — classificacao baseada em 5 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Bruno, boa tarde!
&nbsp;
Segue abaixo a regra de geração no DW dos campos com erros na validação:
&nbsp;
Erro Campo CFPS: Conforme Layout do validador ISS.WEB (em anexo) não é aceito 12 como código CFPS, deve-se preencher com um código valido conforme consta no Manual.
Origem do campo: Campo COD_CFPS da tabela DWT_ITENS_SERV (SAFX09)
&nbsp;

&nbsp;
&nbsp;
Erro imposto retido "N" não é válido: Conforme layout o campo Imposto retido pode ser preenchido com (S) Imposto Retido (N) Imposto Nao...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 65829 | 2023-04-11 | ISS - NOVA LIMA |
| 28497 | 2021-12-09 | Arquivo txt  - Ribeirão Preto (Obrigações municipais) |
| 25682 | 2021-11-05 | Erro na geração de arquivos ISS tomado para município de... |
| 23963 | 2021-10-11 | Campo Cidade - Rio Verde (GO) |
| 23769 | 2021-10-07 | Erro na Importação do Município de Tatui |

## Keywords para Matching
erro, importação, município, tatui, campo, cidade, rio, verde, geração, arquivos
