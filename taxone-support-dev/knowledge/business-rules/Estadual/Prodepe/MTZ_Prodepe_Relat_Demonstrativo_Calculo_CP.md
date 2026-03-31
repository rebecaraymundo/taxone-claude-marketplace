# MTZ_Prodepe_Relat_Demonstrativo_Calculo_CP

- **Fonte:** MTZ_Prodepe_Relat_Demonstrativo_Calculo_CP.docx
- **Modificado:** 2022-04-04
- **Tamanho:** 64 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__                                    Relatório Demonstrativo do Cálculo do Crédito Presumido__

__Localização__: Menu Estadual, Módulo Prodepe, item Relatórios 🡪 Demonstrativo do Cálculo do Crédito Presumido 🡪 Indústria

__ \(este documento de regras é específico do relatório demonstrativo do cálculo do incentivo do tipo = Indústria\)__

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4402

Tratamento das Devoluções

Alteração do cálculo do crédito presumido para tratamento das notas fiscais de devolução de vendas \(ver RN04\)

28/01/2014

\(criação do docto\)

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

O objetivo deste relatório é auxiliar a conferência dos valores gerados no processo do cálculo do crédito presumido\.

O relatório é composto por duas partes:

Parte 1 🡪__Demonstrativo do Cálculo do Crédito Presumido__:

Esta parte demonstra os valores de débitos e créditos utilizados no cálculo do crédito presumido de cada Grupo de Incentivo/Percentual, além de exibir também o valor final do crédito presumido calculado\. 

Parte 2 🡪 __Demonstrativo do Rateio do Crédito das Entradas__:

Esta parte detalha os valores de crédito utilizados no cálculo, para cada uma das faixas do Grupo de Incentivo\.

__Origem dos dados__: As informações deste relatório são geradas a partir dos dados armazenados durante o processo do cálculo do crédito presumido \(tabela ICT\_VLR\_INCENT\)\.

  

__RN01__

__                                                        Parâmetros de Tela__

__RN02__

__                                                    Recuperação dos Dados__

__RN03__

__                                                         Processamento __

__RN04__

__                                                Preenchimento dos Dados __

O preenchimento dos dados é feito a partir do conteúdo das informações da tabela que armazena os valores do cálculo do crédito presumido:  ICT\_VLR\_INCENT\. 

__Parte 1 🡪Demonstrativo do Cálculo do Crédito Presumido__:

Coluna “__Operações Incentivadas – Créditos__” – esta coluna é preenchida com a totalização dos seguintes campos:  

                                                                               VLR\_CRED\_ICMS \+ VLR\_CRED\_ICMS\_DEVOL

Este resultado reflete o valor do ICMS de todas as entradas incentivadas referentes ao Grupo de Incentivo, já rateadas em relação às diversas faixas do Grupo\.

__Alteração da OS4402: __A coluna “VLR\_CRED\_ICMS\_DEVOL” foi criada na OS4402, e armazena o valor do ICMS das devoluções, quando estas forem tratadas separadamente, de acordo com o parâmetro “*Tratamento das devoluções de vendas no rateio dos créditos*” \(menu “Dados Iniciais”\)\.

__Parte 2 🡪 Demonstrativo do Rateio do Crédito das Entradas__:

Esta parte do relatório detalha os valores de crédito utilizados no cálculo, para cada uma das faixas do Grupo de Incentivo\.

Abaixo do cabeçalho, aparece o conteúdo de alguns parâmetros utilizados no cálculo \(menu “Parâmetros 🡪 Dados Iniciais”\), da seguinte forma:

__Parâmetros de utilização dos créditos na base de cálculo do Crédito Presumido__

Considerar o Lançamento de Saldo Credor do período anterior: Sim/Não

Considerar os Lançamentos Complementares de Créditos: Sim/Não

Forma de Utilização: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Tratamento das devoluções: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      

__Alteração da OS4402:__

A opção “Tratamento das Devoluções” \(incluída na OS4402\) exibe a opção cadastrada para o parâmetro “*Tratamento das devoluções de vendas no rateio dos créditos*” da seguinte forma:

Se parâmetro nulo __ou__ = “*O crédito irá compor o total de créditos a ser rateado entre as faixas*”:

     Será exibido o conteúdo:

Tratamento das devoluções: O crédito irá compor o total de créditos a ser rateado entre as faixas

Se parâmetro = “O crédito será direcionado para uma única faixa”:

     Será exibido o conteúdo:

Tratamento das devoluções: O crédito será direcionado para uma única faixa

Coluna “__Rateio do Valor do Crédito das Operações Incentivadas__” – VLR\_CRED\_ICMS 

Coluna “__Rateio do Valor do Crédito dos Lançamentos__” – VLR\_CRED\_ICMS\_LANC 

Coluna “__Valor do Crédito das Operações Incentivadas \(Devoluções\)__” – Esta coluna será exibida no relatório __apenas__ quando o parâmetro de tratamento das devoluções \(menu “Dados Iinicias”\) for = “*O crédito será direcionado para uma única faixa*”, e será preenchida com o conteúdo do campo VLR\_CRED\_ICMS\_DEVOL\. Caso contrário, a coluna simplesmente __não existirá no relatório__\.

\(esta coluna foi incluída do relatório pela __OS442__\)

        = = = = =

