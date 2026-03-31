# MTZ_SPED_EFD_CONTRIBUICOES_Tela_Operacoes_da_Atividade_Imobiliaria_(F200_F205_F210)

> Fonte: MTZ_SPED_EFD_CONTRIBUICOES_Tela_Operacoes_da_Atividade_Imobiliaria_(F200_F205_F210).docx






THOMSON REUTERS

Operações da Atividade Imobiliária (F200/ F205/ F210)
EFD-Contribuições



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Localizar registros (Exemplo)	4
2.	Regras dos Campos	5

## Regras dos Campos


Localização da tela: SPED\ EFD – Escrituração Fiscal Digital das Contribuições\ Manutenção\ Operações das Atividades Imobiliárias (F200/F205/F210)

Título da tela: Operações das Atividades Imobiliárias (F200/F205/F210)

ABA Custo Incorrido




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| CH7615_2015 | Julyana Perrucini | Este documento tem como objetivo alterar o preenchimento dos campos “Valor total do crédito acumulado sobre o custo incorrido PIS”, “Valor total do crédito acumulado sobre o custo incorrido COFINS” e “Parcela a descontar em períodos futuros – do PIS e COFINS”. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Valor total do crédito acumulado sobre o custo incorrido PIS | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Nesse campo será informado o valor total do crédito acumulado sobre o custo incorrido - PIS da unidade imobiliária vendida.  O usuário não terá opção de alterar o valor e o mesmo será informado via importação através da SAFX151 ou através do cálculo dos campos “Valor da Base de Cálculo do Crédito sobre o Custo Incorrido, acumulado até o período da escrituração” e “Alíquota PIS” quando preenchido manualmente (campo 09 x campo 12 /100).  [ALTERADA – CH7615_2016] Quando o campo for importado através da SAFX151, considerar o valor que estiver na carga sem acrescentar o cálculo, pois o mesmo já vem com o arredondamento recomendado, então o cálculo só deverá ser aplicado quando o usuário preencher manualmente em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891.  Atenção: O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210. | CH7615_2016 |
| Parcela a descontar em períodos futuros – PIS | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Esse campo será informado automaticamente pelo o sistema com o resultado do valor do campo Valor total do crédito acumulado sobre o custo incorrido – PIS subtraído pelos valores dos campos: Parcela do crédito descontada até o período anterior da escrituração – PIS e a Parcela a descontar no período da escrituração – PIS.   [ALTERADA – CH7615_2016] O usuário não terá opção de alterar o valor e o mesmo será calculado em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891.  Atenção: O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210. | CH7615_2016 |
| Valor total do crédito acumulado sobre o custo incorrido COFINS | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Nesse campo será informado o valor total do crédito acumulado sobre o custo incorrido - COFINS da unidade imobiliária vendida.  O usuário não terá opção de alterar o valor e o mesmo será informado via importação através da SAFX151 ou através do cálculo dos campos “Valor da Base de Cálculo do Crédito sobre o Custo Incorrido, acumulado até o período da escrituração” e “Alíquota COFINS” quando preenchido manualmente (campo 09 x campo 17 /100).  [ALTERADA – CH7615_2016] Quando o campo for importado através da SAFX151, considerar o valor que estiver na carga sem acrescentar o cálculo, pois o mesmo já vem com o arredondamento recomendado, então o cálculo só deverá ser aplicado quando o usuário preencher manualmente em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891.  Atenção: O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210. | CH7615_2016 |
| Parcela a descontar em períodos futuros – COFINS | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Esse campo será informado automaticamente pelo o sistema com o resultado do campo Valor total do crédito acumulado sobre o custo incorrido – COFINS subtraído pelo os valores dos campos: Parcela do crédito descontada até o período anterior da escrituração – COFINS e a Parcela a descontar no período da escrituração – COFINS.  [ALTERADA – CH7615_2016] O usuário não terá opção de alterar o valor e o mesmo será calculado em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891.  Atenção: O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210. | CH7615_2016 |
