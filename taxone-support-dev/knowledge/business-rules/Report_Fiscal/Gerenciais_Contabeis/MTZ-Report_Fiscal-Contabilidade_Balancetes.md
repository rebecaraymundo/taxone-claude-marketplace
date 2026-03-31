---
source: "MTZ-Report_Fiscal-Contabilidade_Balancetes.docx"
category: Report_Fiscal
converted: auto
---

# Report Fiscal – Balancete



Módulo: Básicos – Report Fiscal
Menu: Gerenciais – Contábil – Geral – Balancete
Balancete c/ Diário por Conta Contábil


DOCUMENTO DE REQUISITO




## REGRAS DE NEGÓCIO





Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:


Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:








---

| DR | Nome | Descrição |
| --- | --- | --- |
| OS2827 | Demonstrar os saldos das contas antes do encerramento na emissão do Balancete. | Incluir no processo de geração do relatório Balancete uma opção para visualização dos saldos das contas de resultado antes do encerramento. |
| OS3443 | Balancete nas Contas Sintéticas NÃO FOI DESENVOLVIDA | Correção na geração do relatório de balancete sintético, pois ao gerar este relatório, ele trás a informação Sem Movimento sabendo-se que existe a movimentação. |
| CH119168 | DW - BÁSICOS - REPORT FISCAL - Balancetes Geral consolidado por empresa e tipo analítico está somando as contas contábeis NÃO FOI DESENVOLVIDA | O objetivo desta demanda é consolidar as contas analíticas apenas pelo estabelecimento, sem somar os valores. |
| CH16795_2015 | Alteração da composição de Saldos Antes do Encerramento para balancete Sintético | Este documento tem como objetivo alterar a regra de composição de Saldos Antes do Encerramento para balancete Sintético. |
| MFS3790 | Inclusão de parâmetro para considerar saldos por centro de custo | Este documento tem o objetivo alterar o relatório para que tenha a opção de gerar os saldos por centro de custo. |
| CH23683_2017 (MFS13225) | Alteração Saldo Anterior e Saldo Atual | Este documento tem como objetivo alterar o preenchimento das colunas Saldo Anterior e Saldo Atual para geração com intervalo de períodos. |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Na tela de geração do balancete existente nos menus: ‘Gerenciais > Contábil > Geral > Balancete’ e ‘Gerenciais > Contábil > Geral > Balancete c/ Diário por Conta Contábil’ deve ser adicionado:  [ALTERADA – MFS3790] Um checkbox com a descrição ‘Saldos Antes do Encerramento’. Esse checkbox deve ser adicionado imediatamente abaixo da opção ‘Imprime Contas Zeradas’ e deve vir por default desmarcado. Um checkbox com a descrição ‘Considerar Saldo por Centro de Custo’ Esse checkbox deve ser adicionado imediatamente abaixo da opção ‘Saldo antes do Encerramento’ e deve vir por default desmarcado. | OS2827 MFS3790 |
| RN01 | Quando na tela de emissão do balancete existente nos menus: ‘Gerenciais > Contábil > Geral > Balancete’ e ‘Gerenciais > Contábil > Geral > Balancete c/ Diário por Conta Contábil’ for selecionada a opção ‘Saldos Antes do Encerramento’, deve ser adicionada uma coluna no relatório com a descrição ‘Saldo Antes do Encerramento’. Essa coluna deve ser adicionada após a coluna ‘Saldo Final’ e a recuperação dos valores para preenchê-la está especificada na RN02. Na totalização dos valores do balancete também deve ser adicionada a totalização dos saldos antes do encerramento, quando for o caso. A totalização do Saldo Antes do Encerramento seguirá a mesma regra de totalização do Saldo Final. | OS2827 |
| RN02 | Quando a opção ‘Saldos Antes do Encerramento’ estiver marcada na tela de emissão do balancete será adicionado o seguinte processamento (além do processamento já realizado atualmente):  Para cada conta, buscar na X01_CONTABIL todos os lançamentos de encerramento que estiverem dentro do período de geração do balancete e que pertencerem à empresa e estabelecimento selecionados na tela de geração (podem existir vários lançamentos de encerramento para uma mesma conta porque o encerramento pode ser feito por centro de custo). Depois de recuperados os lançamentos, sumarizar os valores encontrados (total de créditos – total de débitos) e o resultado dessa sumarização é o valor a ser demonstrado no relatório para aquela conta. Além do valor, o balancete deve demonstrar também o indicador (débito ou crédito), o indicador do saldo antes do encerramento será sempre o inverso do resultado da sumarização dos lançamentos de encerramento, ou seja, se após a sumarização obteve-se um valor de R$1000,00 a Crédito, no relatório será apresentado R$1000,00 a Débito.  Tratamento: Se na tela de geração o usuário tiver escolhido a opção ‘Analítico’, o processamento acima deve ser feito apenas para as contas analíticas;  Se na tela de geração o usuário tiver escolhido a opção ‘Sintético’, o processamento acima deve ser feito para as contas sintéticas da seguinte forma: Totalizar o valor dos lançamentos de encerramento das contas analíticas “filhas” da conta sintética e quando houver mais de uma conta sintética no ramo, sumariza-las na ordem superior da conta, ou seja, supondo que exista a conta 1 lançada, com os ramos na ordem 1.01 e 1.01.01, então a conta 1 sumarizaria a conta 1.01 e a conta 1.01 sumarizaria a conta 1.01.01. Exemplo da totalização de contas analíticas e sintéticas: Conta Analítica = 1.00.00.00.01 Conta Sintética = 1.00.00.00 Contabilidade de 06/2015 Saldo da Conta Analítica Saldo Inicial = 1.000,00 Total Débitos = 1.500,00 Total Créditos = 2.500,00 Indicador = D Saldo Final = 0,00 Saldo da Conta Sintética Saldo Inicial = 1.000,00 Total Débitos = 1.500,00 Total Créditos = 2.500,00 Indicador = D Saldo Final = 0,00 Lançamentos para Conta Sintética Crédito Conta Contábil = 1.00.00.00.01 Tipo de Lançamento = Normal Valor Lançamento = 500,00 Débito Conta Contábil = 1.00.00.00.01 Tipo de Lançamento = Normal Valor Lançamento = 1.500,00 Crédito Conta Contábil = 1.00.00.00.01 Tipo de Lançamento = Encerramento Valor Lançamento = 2.000,00 Geração do relatório Analítico:  Geração do relatório Sintético:   Se na tela de geração tiverem sido informadas as contas inicial e final a serem consideradas no relatório, todo o processamento descrito acima será feito apenas para esse intervalo de contas (assim como os outros valores do relatório). | OS2827 CH16795_2015 |
| RN03 | NÃO FOI DESENVOLVIDA  Regra para Balancete – Sintético:  Módulo: Básicos → Report Fiscal Menu: Gerenciais → Balancete                            → Balancete c/ Diário por Conta Contábil   O relatório do Balancete, tipo Sintético, deve gerar valores consolidados das Contas Analíticas referente à Conta Sintética superior, utilizando os níveis, ou seja, os valores das contas analíticas devem ser sumarizados e carregados para a sua respectiva conta sintética. | OS3443 |
| RN04 | NÃO FOI DESENVOLVIDA  Regra para Balancete – Analítco:  O relatório do Balancete, tipo Analítico, deve gerar as contas consolidadas apenas para os estabelecimentos, quando o campo Estabelecimentos – Todos Consolidados estiver marcado, sem somar os valores das contas analíticas. A soma apenas deve ser realizada para consolidação de contas sintéticas conforme regra RN03. | CH119168 |
| RN05 | Quando a opção considerar “Saldos por Centro de Custo” estiver marcada na tela de emissão do balancete será adicionado o seguinte processamento (além do processamento já realizado atualmente):  Será adicionada uma coluna com o nome “Centro de Custo” (nesse caso haverá mudança de layout do relatório e a coluna Descrição ficará como linha abaixo do código da conta e o centro de custo será demonstrado na coluna ao lado do código da conta). A Recuperação dos valores quando esta opção estiver marcada será feita por meio de duas tabelas, pela SAFX02 e SAFX80, porém quando o registro de saldo estiver demonstrado na SAFX80 não demonstrar os saldos dos registros contidos na SAFX02. | MFS3790 |
| RN06 | Campo Saldo Anterior  Na geração do campo Saldo Anterior com Tipo de Balancete igual Analítico ou Sintético e Estabelecimentos iguais a Discriminados ou Todos Consolidados, recuperar a informação da totalização das contas da seguinte forma:  Se o parâmetro “Considerar Saldos por Centro de Custo” estiver desmarcado: Considerar o Saldo Inicial da SAFX02 do período informado na Data Inicial da tela de geração do balancete considerando a Data da Operação da conta contábil.  Se o parâmetro “Considerar Saldos por Centro de Custo” estiver marcado: Considerar o Saldo Inicial da SAFX80 do período informado na Data Inicial da tela de geração do balancete considerando a Data da Operação da conta contábil.  Exemplo:    O Saldo Anterior está considerando o Saldo Inicial do período de Janeiro porque a geração é de um ano inteiro.   O Saldo Anterior está considerando o Saldo Inicial do período de Janeiro porque a geração é de Janeiro à Março.   O Saldo Anterior está considerando o Saldo Inicial do período de Junho porque a geração é de Junho à Dezembro.  A totalização será feita na linha abaixo demonstrando o período inicial e final do saldo.  Veja que o Saldo Inicial é a soma dos valores daquele período inicial e não do período todo em que está sendo gerado, exemplo da mesma conta utilizada para vários estabelecimentos no período de Janeiro/ 2014 na planilha “BALANCETE_EXEMPLO_CONTA_1.1.1.02.0006.111012.xlsx”. | CH23683_2017 (MFS-13225) |
| RN07 | Campo Débito  Na geração do campo Débito com Tipo de Balancete igual Analítico ou Sintético e Estabelecimentos iguais a Discriminados ou Todos Consolidados, recuperar a informação da totalização das contas da seguinte forma:  Se o parâmetro “Considerar Saldos por Centro de Custo” estiver desmarcado: Considerar a soma do total dos débitos da SAFX02 do período informado na tela de geração do balancete considerando a Data da Operação da conta contábil.  Se o parâmetro “Considerar Saldos por Centro de Custo” estiver marcado: Considerar a soma do total dos débitos da SAFX80 do período informado na tela de geração do balancete considerando a Data da Operação da conta contábil.  Exemplo:    O Débito está considerando a soma do período de Janeiro a Dezembro porque a geração é de um ano inteiro.   O Débito está considerando a soma do período de Janeiro a Março porque a geração tem intervalo.   O Débito está considerando a soma do período de Junho a Dezembro porque a geração tem intervalo.  A totalização será feita na linha de cima demonstrando a soma de todo o período especificado.  Veja que o Débito é a soma dos valores daquele período em que está sendo gerado, exemplo da mesma conta utilizada para vários estabelecimentos no período de Janeiro/ 2014 na planilha “BALANCETE_EXEMPLO_CONTA_1.1.1.02.0006.111012.xlsx”. | CH23683_2017 (MFS-13225) |
| RN08 | Campo Crédito  Na geração do campo Crédito com Tipo de Balancete igual Analítico ou Sintético e Estabelecimentos iguais a Discriminados ou Todos Consolidados, recuperar a informação da totalização das contas da seguinte forma:  Se o parâmetro “Considerar Saldos por Centro de Custo” estiver desmarcado: Considerar a soma do total dos créditos da SAFX02 do período informado na tela de geração do balancete considerando a Data da Operação da conta contábil.  Se o parâmetro “Considerar Saldos por Centro de Custo” estiver marcado: Considerar a soma do total dos créditos da SAFX80 do período informado na tela de geração do balancete considerando a Data da Operação da conta contábil.  Exemplo:    O Crédito está considerando a soma do período de Janeiro a Dezembro porque a geração é de um ano inteiro.   O Crédito está considerando a soma do período de Janeiro a Março porque a geração tem intervalo.   O Crédito está considerando a soma do período de Junho a Dezembro porque a geração tem intervalo.  A totalização será feita na linha de cima demonstrando a soma de todo o período especificado.  Veja que o Crédito é a soma dos valores daquele período em que está sendo gerado, exemplo da mesma conta utilizada para vários estabelecimentos no período de Janeiro/ 2014 na planilha “BALANCETE_EXEMPLO_CONTA_1.1.1.02.0006.111012.xlsx”. | CH23683_2017 (MFS-13225) |
| RN09 | Campo Saldo Atual  Na geração do campo Saldo Atual com Tipo de Balancete igual Analítico ou Sintético e Estabelecimentos iguais a Discriminados ou Todos Consolidados, recuperar a informação da totalização das contas da seguinte forma:  Se o parâmetro “Considerar Saldos por Centro de Custo” estiver desmarcado: Considerar o Saldo Final da SAFX02 do período informado na Data Final da tela de geração do balancete considerando a Data da Operação da conta contábil.  Se o parâmetro “Considerar Saldos por Centro de Custo” estiver marcado: Considerar o Saldo Final da SAFX80 do período informado na Data Final da tela de geração do balancete considerando a Data da Operação da conta contábil.  Exemplo:    O Saldo Atual está considerando o Saldo Final do período de Dezembro porque a geração é de um ano inteiro.   O Saldo Atual está considerando o Saldo Final do período de Março porque a geração é de Janeiro à Março.   O Saldo Atual está considerando o Saldo Final do período de Dezembro porque a geração é de Junho à Dezembro.  A totalização será feita na linha abaixo demonstrando o período inicial e final do saldo.  Veja que o Saldo Final é a soma dos valores daquele período inicial e não do período todo em que está sendo gerado, exemplo da mesma conta utilizada para vários estabelecimentos no período de Janeiro/ 2014 na planilha “BALANCETE_EXEMPLO_CONTA_1.1.1.02.0006.111012.xlsx”. | CH23683_2017 (MFS-13225) |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

