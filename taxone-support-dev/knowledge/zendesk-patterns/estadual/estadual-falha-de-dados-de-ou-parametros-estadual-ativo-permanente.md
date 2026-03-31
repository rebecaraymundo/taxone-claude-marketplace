---
pattern_id: "estadual-falha-de-dados-de-ou-parametros-estadual-ativo-permanente"
vertical: estadual
root_cause: falha_de_dados_de_ou_parametros
module: estadual_ativo_permanente
ticket_count: 160
ticket_ids: [465, 4426, 4207, 4963, 8144, 8242, 9985, 13409, 13853, 16277, 17777, 18318, 20502, 20056, 22527, 26079, 26292, 27147, 27195, 28200, 28076, 28520, 29612, 29549, 29243, 30522, 31145, 31457, 32941, 37331, 38219, 38019, 39582, 44375, 44579, 45649, 46862, 46852, 46455, 50151, 51634, 51795, 52377, 52903, 53405, 53818, 54053, 55178, 55557, 55489, 56366, 56300, 56212, 57515, 58958, 58932, 58703, 59525, 59482, 59169, 59895, 59824, 60926, 60730, 61695, 61285, 62004, 64330, 65098, 65369, 65820, 66492, 66486, 66411, 66957, 68269, 70599, 70555, 70262, 71882, 71870, 72571, 74288, 75848, 75405, 82396, 85407, 87232, 87445, 88112, 88044, 88747, 93279, 94385, 95596, 96105, 97360, 100052, 100002, 100457, 101310, 103251, 104075, 104706, 104394, 107043, 108417, 112411, 112385, 112976, 113891, 113882, 114537, 115075, 115026, 116952, 117708, 117506, 118361, 120105, 122959, 124121, 125802, 125502, 130826, 134037, 133965, 134696, 137553, 139486, 140903, 141666, 142562, 142387, 144364, 147127, 147051, 148396, 148905, 148774, 152462, 153289, 158309, 159785, 159353, 160508, 161426, 162705, 162420, 163811, 163734, 163387, 165381, 166088, 167494, 170231, 170058, 172553, 175489, 176598]
last_occurrence: "2026-03-08"
keywords: ["diverg\u00eancia", "valores", "ciap", "taxone", "problemas", "baixa", "autom\u00e1tica", "erro", "cria\u00e7\u00e3o", "aliena\u00e7\u00e3o"]
is_not_bug: false
---

# ESTADUAL ATIVO PERMANENTE: Falha De Dados De Ou Parametros

## Descricao do Padrao
Clientes reportam problemas relacionados a: 33427 | Relatório das aquisições - Módulo do ativo - MICHELIN; 46855| 40023| 33427 - Relatório das aquisições - Módulo do ativo - Valores negativos -  Exemplo Nfe de ativo - MICHELIN; AF-CIAP- Ativo Permanente - Crédito aquisições

## Causa Raiz
Falha De Dados De Ou Parametros — classificacao baseada em 160 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Olá Paulo e Marco, boa tarde.
&nbsp;
Conforme validado durante o acesso remoto, realizamos o processo de cálculo das parcelas normais. Após a conclusão dos cálculos, o valor a apropriar do ICMS foi devidamente preenchido na tela de manutenção &gt; Dados do cálculo. Em seguida, procedemos com o cálculo das parcelas extemporâneas, que foram geradas corretamente.
&nbsp;
Além disso, realizamos a validação do Bloco G, confirmando que os registros G125 e G126 foram gerados corretamente.
&nbsp;
Abaixo...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 176598 | 2026-03-03 | Erro de processamento de Calculo do CIAP |
| 175489 | 2026-02-24 | Geração de nota para CIAP acusa erro |
| 172553 | 2026-02-03 | Crédito extemporâneo CIAP |
| 170231 | 2026-01-19 | Erro calculo credito expetemraneo  Ativo Permanente  |
| 170058 | 2026-01-16 | Black - Erro no processo de Bem resultante X Bem componente. |
| 167494 | 2025-12-30 | Geração de Bens Resultantes X Componentes |
| 166088 | 2025-12-17 | Divergência relatório Saldos a Creditar (II) - Report... |
| 165381 | 2025-12-13 | CIAP - Geração das Aquisições a partir de NFs - Produto a... |
| 163811 | 2025-12-04 | CIAP -  geração relatório com parcelas erradas |
| 163734 | 2025-12-04 | CIAP |

## Keywords para Matching
divergência, valores, ciap, taxone, problemas, baixa, automática, erro, criação, alienação
