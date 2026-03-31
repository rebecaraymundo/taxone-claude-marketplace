---
pattern_id: "estadual-solicitação-de-informacao-estadual-dia-am"
vertical: estadual
root_cause: solicitação_de_informacao
module: estadual_dia_-_am
ticket_count: 5
ticket_ids: [49159, 66989, 85515, 136027, 165785]
last_occurrence: "2026-01-05"
keywords: ["diretorio", "upload", "arquivo", "matriz", "sefaz", "res", "thomson", "reuters", "ticket", "58818"]
is_not_bug: false
---

# ESTADUAL DIA - AM: Solicitação De Informacao

## Descricao do Padrao
Clientes reportam problemas relacionados a: AMCOR - Importação dos Arquivos da Sefaz-AM; DIA AM - Diretorio de Upload arquivo Matriz Sefaz; DIA-AM

## Causa Raiz
Solicitação De Informacao — classificacao baseada em 5 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Aline, bom dia!
&nbsp;
A importação do arquivo no Módulo da DIA AM deve ser feito utilizando o usuário de SFTP associado ao usuário do Tax One. Não é possível
realizar a importação com o usuário integrador do SFTP se o usuário que estiver fazendo a importação estiver logado no Tax one com outro&nbsp;
usuário. Sempre é necessário que esteja logado no mesmo usuário no SFTP e no Tax One.&nbsp;
&nbsp;
Esse procedimento é pré-requisito não só para o módulo da DIA AM, mas também para outros módulos...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 165785 | 2025-12-16 | AMCOR - Importação dos Arquivos da Sefaz-AM |
| 136027 | 2025-05-14 | DIA-AM |
| 85515 | 2023-12-05 | Geração DIA AM |
| 66989 | 2023-04-26 | RES: [Thomson Reuters] Re: Ticket 58818 - Divergência Preço... |
| 49159 | 2022-08-26 | DIA AM - Diretorio de Upload arquivo Matriz Sefaz |

## Keywords para Matching
diretorio, upload, arquivo, matriz, sefaz, res, thomson, reuters, ticket, 58818
