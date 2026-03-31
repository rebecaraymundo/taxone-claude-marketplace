---
pattern_id: "sped-solicitacao-de-servico-sped-efd-escrituração-fiscal-digital"
vertical: sped
root_cause: solicitacao_de_servico
module: sped_efd_-_escrituração_fiscal_digital
ticket_count: 35
ticket_ids: [3229, 22671, 24016, 26307, 27943, 28619, 29167, 36460, 45600, 52367, 53144, 57716, 61051, 66815, 77862, 78766, 82419, 85308, 87405, 89223, 97287, 97581, 101250, 103261, 105824, 107402, 109742, 114495, 114383, 119814, 140381, 150641, 157117, 158807, 164691]
last_occurrence: "2026-03-04"
keywords: ["pck", "body", "efd31_dados", "libera\u00e7\u00e3o", "licenciamento", "novas", "empresas", "contrato", "certificados", "soc"]
is_not_bug: false
---

# SPED EFD - ESCRITURAÇÃO FISCAL DIGITAL: Solicitacao De Servico

## Descricao do Padrao
Clientes reportam problemas relacionados a: Adicionar o cliente/empresa na minha lista de organizações para abertura de chamados; Autorização de processamento de dados eletrônicos dos livros fiscais  na SEFAZ PR; Bloco 1400 - PI

## Causa Raiz
Solicitacao De Servico — classificacao baseada em 35 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde, Vivian, tudo certo?
&nbsp;
Identificamos que ao importar a SAFX82 com documentos que possuem valores irrisórios (centavos), que não são passíveis de rateio em 1/48 avos (ou seja, ao dividir o valor de ICMS da aquisição por 48 parcelas, o resultado não se enquadra em duas casas após a vírgula), a geração do SPED apresenta uma inconsistência.&nbsp;
&nbsp;
A geração não suporta aquisições com valores que não podem ser rateados em 1/48 avos.
&nbsp;
Dessa forma, por gentileza, verifique a...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 164691 | 2025-12-10 | Erro Bloco G125 - SPED FISCAL |
| 158807 | 2025-10-31 | [BRADO]SAFX04 - Campo 12 Endereço - Registro 0150 |
| 157117 | 2025-10-21 | Lentidão na execução do sped fiscal |
| 150641 | 2025-09-05 | Menus desabilitados no Tax Automation |
| 140381 | 2025-06-16 | Adicionar o cliente/empresa na minha lista de organizações... |
| 119814 | 2024-12-17 | Não gera o arquivo txt EFD em UAT |
| 114495 | 2024-10-30 | NOva Legislação - FECOP Rio de Janeiro |
| 114383 | 2024-10-30 | Obrigatoriedade nos registros C195 e D195 informação... |
| 109742 | 2024-09-11 | SINIEF 3/2018 |
| 107402 | 2024-08-14 | Autorização de processamento de dados eletrônicos dos... |

## Keywords para Matching
pck, body, efd31_dados, liberação, licenciamento, novas, empresas, contrato, certificados, soc
