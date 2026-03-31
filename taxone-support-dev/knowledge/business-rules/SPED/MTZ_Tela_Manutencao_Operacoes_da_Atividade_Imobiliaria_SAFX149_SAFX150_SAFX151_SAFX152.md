# MTZ_Tela_Manutenção_Operacoes_da_Atividade_Imobiliaria_SAFX149_SAFX150_SAFX151_SAFX152

> Fonte: MTZ_Tela_Manutenção_Operacoes_da_Atividade_Imobiliaria_SAFX149_SAFX150_SAFX151_SAFX152.docx






THOMSON REUTERS

Operações da Atividade Imobiliária (F200/F205/F210)

SAFX149, SAFX150, SAFX151, SAFX152



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3


## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital das Contribuições\ Manutenção\ Operações da Atividade Imobiliária (F200/F205/F210)

Título da tela: Operações da Atividade Imobiliária (F200/F205/F210)


ABA UNIDADE IMOBILIÁRIA VENDIDA (SAFX149)



ABA VALORES RECEBIDOS (SAFX150)



ABA CUSTO INCORRIDO (SAFX151)





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316 | Inclusão de campo | Incluir o campo Código e Descrição da SCP |
| CH23678_2015 | Julyana Perrucini | Criação do documento. Inclusão de validação para campo “Percentual da receita recebida até o mês”. |
| CH7615_2015 | Julyana Perrucini | Este documento tem como objetivo alterar o preenchimento dos campos “Valor total do crédito acumulado sobre o custo incorrido PIS”, “Valor total do crédito acumulado sobre o custo incorrido COFINS” e “Parcela a descontar em períodos futuros – do PIS e COFINS”. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Código SCP | Texto | S | N | Formato:  Pastinha + Código + Descrição  Default: | Deverá ser criado o campo Código da SCP, acompanhado da pasta de seleção da informação e o campo de texto para demonstração da descrição vinculada ao código.  Quando acionada a pasta, serão demonstrados os registros da tabela SAFX2057 – Cadastro da SCP. Para o código selecionado, será demonstrada também a descrição da SCP.  Nome do campo em tela: “Código da SCP:”  Caso o usuário informe um código que não tenha cadastro correspondente na SAFX2057, retornar a mensagem de erro: “Cadastro da SCP não encontrado”. | OS4316 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Percentual da receita recebida até o mês | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Este campo é preenchido pelo o sistema com a somatória dos campos (Valor recebido acumulado até o mês anterior ao da escrituração + Valor total recebido no mês da escrituração) dividido pelo o valor do campo (Valor total de venda da unidade imobiliária).   [ALTERADA – CH23678_2015] Validação: Caso o valor inserido no campo 07 ou no campo 08 seja maior que o valor inserido no campo 06, ou ainda, a divisão resultar em zero, não importar os registros e exibir a seguinte mensagem: “A SAFX150 somente deve ser importada quando o percentual da receita total recebida até o mês da Escrituração (campo 07 + campo 08 /campo 06) for maior que zero e não maior que 100%.”. | CH23678_2015 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Valor total do crédito acumulado sobre o custo incorrido PIS | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Nesse campo será informado o valor total do crédito acumulado sobre o custo incorrido - PIS da unidade imobiliária vendida.  O usuário não terá opção de alterar o valor e o mesmo será informado via importação através da SAFX151 ou através do cálculo dos campos “Valor da Base de Cálculo do Crédito sobre o Custo Incorrido, acumulado até o período da escrituração” e “Alíquota PIS” quando preenchido manualmente (campo 09 x campo 12 /100).  [ALTERADA – CH7615_2016] Quando o campo for importado através da SAFX151, considerar o valor que estiver na carga sem acrescentar o cálculo, pois o mesmo já vem com o arredondamento recomendado, então o cálculo só deverá ser aplicado quando o usuário preencher manualmente em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891.  Atenção: O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210. | CH7615_2016 |
| Parcela a descontar em períodos futuros – PIS | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Esse campo será informado automaticamente pelo o sistema com o resultado do valor do campo Valor total do crédito acumulado sobre o custo incorrido – PIS subtraído pelos valores dos campos: Parcela do crédito descontada até o período anterior da escrituração – PIS e a Parcela a descontar no período da escrituração – PIS.   [ALTERADA – CH7615_2016] O usuário não terá opção de alterar o valor e o mesmo será calculado em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891.  Atenção: O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210. | CH7615_2016 |
| Valor total do crédito acumulado sobre o custo incorrido COFINS | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Nesse campo será informado o valor total do crédito acumulado sobre o custo incorrido - COFINS da unidade imobiliária vendida.  O usuário não terá opção de alterar o valor e o mesmo será informado via importação através da SAFX151 ou através do cálculo dos campos “Valor da Base de Cálculo do Crédito sobre o Custo Incorrido, acumulado até o período da escrituração” e “Alíquota COFINS” quando preenchido manualmente (campo 09 x campo 17 /100).  [ALTERADA – CH7615_2016] Quando o campo for importado através da SAFX151, considerar o valor que estiver na carga sem acrescentar o cálculo, pois o mesmo já vem com o arredondamento recomendado, então o cálculo só deverá ser aplicado quando o usuário preencher manualmente em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891.  Atenção: O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210. | CH7615_2016 |
| Parcela a descontar em períodos futuros – COFINS | Numérico | S | N | Formato:  0,00  Default:  Desabilitado | Esse campo será informado automaticamente pelo o sistema com o resultado do campo Valor total do crédito acumulado sobre o custo incorrido – COFINS subtraído pelo os valores dos campos: Parcela do crédito descontada até o período anterior da escrituração – COFINS e a Parcela a descontar no período da escrituração – COFINS.  [ALTERADA – CH7615_2016] O usuário não terá opção de alterar o valor e o mesmo será calculado em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891.  Atenção: O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210. | CH7615_2016 |
