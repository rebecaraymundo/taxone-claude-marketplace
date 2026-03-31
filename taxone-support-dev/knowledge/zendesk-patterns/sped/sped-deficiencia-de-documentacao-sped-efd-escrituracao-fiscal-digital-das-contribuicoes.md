---
pattern_id: "sped-deficiencia-de-documentacao-sped-efd-escrituração-fiscal-digital-das-contribuições"
vertical: sped
root_cause: deficiencia_de_documentacao
module: sped_efd_-_escrituração_fiscal_digital_das_contribuições
ticket_count: 30
ticket_ids: [18713, 21332, 26411, 26567, 27179, 28841, 28834, 28401, 33573, 41341, 82065, 112955, 112751, 115954, 121201, 121110, 125627, 125567, 125521, 126311, 131291, 133219, 133763, 135528, 141729, 145252, 145654, 146992, 146975, 173242]
last_occurrence: "2026-02-25"
keywords: ["planilhas", "importa\u00e7\u00e3o", "dados", "blocos", "exclusao", "icms", "base", "calculo", "pis", "erro"]
is_not_bug: false
---

# SPED EFD - ESCRITURAÇÃO FISCAL DIGITAL DAS CONTRIBUIÇÕES: Deficiencia De Documentacao

## Descricao do Padrao
Clientes reportam problemas relacionados a: Apuração Geral PIS/COFINS; Arcom_EFD Contribuições_Uploadtxt_M110_M510; CFOPs parametrizado, porém não geram no relatório C500

## Causa Raiz
Deficiencia De Documentacao — classificacao baseada em 30 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Boa tarde Juarez,
&nbsp;
Eu realizei teste em base do suporte, inclui alguns lançamentos F600 e preenchendo o indicador Natureza da Receita, o mesmo ficou correto, após salvar, sair da tela e consultar novamente.
&nbsp;
Num dos testes que fiz eu deixei o campo em branco e salvei, ao consultar o lançamento o campo fica com o 9 atribuído.
&nbsp;
Verificado em regra e é isso mesmo, caso no momento do lançamento o campo fique em branco o sistema atribui = 9.
&nbsp;

&nbsp;
A...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 173242 | 2026-02-06 | Erro nos lançamentos do F600 |
| 146992 | 2025-08-12 | T1 - EPC - Geração de registros / Apuração |
| 146975 | 2025-08-12 | Lançamento do Registro F100, não estão populando na... |
| 145654 | 2025-07-31 | EFD Contribuições - Bug tela Status da Obrigação PRD |
| 145252 | 2025-07-28 | Vero - Erro de Estrutura D500 atualização layout |
| 141729 | 2025-06-27 | SAFX540 - Importação realizada, porém dados não foram... |
| 135528 | 2025-05-09 | Arcom_EFD Contribuições_Uploadtxt_M110_M510 |
| 133763 | 2025-04-24 | Geração dos registros M220 e M620 |
| 133219 | 2025-04-17 | Inconsistência ao GERAR EFD CONTRIBUIÇÕES 03-2025  |
| 131291 | 2025-04-02 | Cadastro de Produtos |

## Keywords para Matching
planilhas, importação, dados, blocos, exclusao, icms, base, calculo, pis, erro
