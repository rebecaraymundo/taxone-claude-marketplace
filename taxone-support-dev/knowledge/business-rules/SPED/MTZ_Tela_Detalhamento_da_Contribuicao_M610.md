# MTZ_Tela_Detalhamento_da_Contribuicao_M610

> Fonte: MTZ_Tela_Detalhamento_da_Contribuicao_M610.docx






THOMSON REUTERS

Matriz da tela Detalhamento da Contribuição - M610



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	5

## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD-Contribuições Financeira/Assemelhada
Menu: Obrigações >> Manutenção >> Apuração COFINS

Deverá ser alterada a tela “Detalhamento da Contribuição – M610” para que seja possível realizar a geração do registro M610 da EFD-Financeira.

Esta tela será acessada através de nova aba inserida na tela de Apuração COFINS. Estará no mesmo nível da aba Detalhamento por Código de Receita– M605. Na estrutura dos registros da EFD- Financeira este é um registro filho do M600 – Consolidação da Contribuição para a Seguridade Social - COFINS do Período.

[ALTERADA – MFS25094]


* Descrição não disponível em tela


## Sugestão de Layout










| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS25094 | Andréa Rocha | Alteração da tela de Detalhamento da Contribuição – M610 para inclusão dos campos: “Valor do total dos ajustes de acréscimo da base de cálculo da contribuição a que se refere o Campo 04”, “Valor do total dos ajustes de redução da base de cálculo da contribuição a que se refere o Campo 04” e “Valor da Base de Cálculo da Contribuição, após os ajustes”. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Valor do total dos ajustes de acréscimo da base de cálculo | Numérico | N | N | Formato: ComboBox  Default: Não Informado | Nesse campo será informado o valor total dos ajustes de acréscimo à base de cálculo da contribuição social apurada no campo “Valor da Base de Cálculo da Contribuição”. O preenchimento deste campo obriga o respectivo detalhamento no registro M615, sendo que o valor deste campo deverá ser igual ao somatório do campo VL_AJ_BC dos registros M615 quando IND_AJ_BC = 0. | MFS25094 |
| Valor do total dos ajustes de redução da base de cálculo | Numérico | N | N | Formato: 0,00  Default: Não Informado | Nesse campo será informado o valor total dos ajustes de redução à base de cálculo da contribuição social apurada no campo “Valor da Base de Cálculo da Contribuição”. O preenchimento deste campo obriga o respectivo detalhamento no registro M615, sendo que o valor deste campo deverá ser igual ao somatório do campo VL_AJ_BC dos registros M615 quando IND_AJ_BC = 1. | MFS25094 |
| Valor da Base de Cálculo da Contribuição, após os ajustes | Numérico | N | N | Formato: ComboBox  Default: Não Informado | Esse campo corresponde ao valor da base de cálculo da contribuição, vinculada ao valor de Código da contribuição social apurada no período do respectivo registro, após os ajustes da base de cálculo informados nos campos “Valor do total dos ajustes de acréscimo da base de cálculo” e “Valor do total dos ajustes de redução da base de cálculo”. Assim, o campo “Valor da Base de Cálculo da Contribuição”, após os ajustes, será igual ao campo “Valor da Base de Cálculo da Contribuição” + campo “Valor do total dos ajustes de acréscimo da base de cálculo” - campo “Valor do total dos ajustes de redução da base de cálculo”. Caso não informado nenhum valor nos novos campos “Valor do total dos ajustes de acréscimo da base de cálculo” e “Valor do total dos ajustes de redução da base de cálculo”, será recuperado para o novo campo “Valor da Base de Cálculo da Contribuição”, após os ajustes, o valor calculado no campo “Valor da Base de Cálculo da Contribuição”. | MFS25094 |
