---
source: "MTZ_Relatorio_Conferencia_Saldo_x_Movimento.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Módulo Report Fiscal

Conferência (Saldos x Movimentos)


Localização:
MastersafDW >> Básicos >> Report Fiscal >> Gerenciais>> Contábil >>Geral >> Conferência (Saldos x Movimentos)

MastersafDW >> SPED >> Escrituração Contábil Digital>> Relatórios>> Conferência (Saldos x Movimentos)








DOCUMENTO DE REQUISITO


Sumário

**Regras Gerais	4**
1.	Definição da tela	5
2.	Layout do relatório:	10
























# Regras Gerais

- Este relatório tem por objetivo fazer algumas validações com as informações de saldos contábeis (X02), saldos por centro de custo (X80) e de lançamentos contábeis (X01). O usuário poderá escolher pelo menos uma das seguintes validações na base:
- Valida movimento (débito e crédito) entre as origens X01 (lançamentos) e X02 (saldos)
- Valida movimento (débito e crédito) entre as origens X01 (lançamentos) e X80 (saldos por centro de custo)
- Valida o saldo final do período anterior com o inicial do período, origem X02 (saldos)
- Valida o saldo final do período anterior com o inicial do período, origem X80 (saldos por centro de custo)
- Valida o saldo final do período com o inicial do período posterior, origem X02 (saldos)
- Valida o saldo final do período com o inicial do período posterior, origem X80 (saldos por centro de custo)
- Valida os saldos da X02, com os lançamentos da X01
- Valida os saldos por centro de custo da X80, com os lançamentos da X01
- Valida os valores da conta da X02 com o valor totalizado desta conta na X80
- Valida por número de lançamento se o valor de crédito e débito da X01 são iguais.
- Valida se os valores de crédito e débito da X02 são iguais


- [ALTERAÇÃO- MFS-601602] Tratamento para recuperar Lançamentos /e ou Saldos de Estabelecimentos Centralizador e Centralizadoras

Se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados, sendo assim deverão ser considerados na validação/consolidação de dados todos os Lançamentos /e ou Saldos de todos os Estabelecimentos envolvidos, o centralizador (estabelecimento selecionado como centralizador e todos os Estabelecimentos associados como centralizados), conforme parametrização do módulo de Básicos >> Parâmetros, menu “Preliminares > Centralização da Escrituração de Obrigações Federais”, conforme exemplo abaixo:





Onde:

Estabelecimento Centralizado: Refere-se a um Estabelecimento Centralizador, dessa forma o sistema deverá recuperar os movimentos de Lançamentos e Saldos do Estabelecimentos Centralizador e de TODOS os Estabelecimentos associando, ou seja, Centralizados.
Vide: Módulo de Básicos >> Parâmetros, menu “Preliminares > Centralização da Escrituração de Obrigações Federais”.

Estabelecimento Descentralizado: Refere-se a um Estabelecimento Não Centralizador ou Não Centralizado, dessa forma o sistema deverá recuperar os movimentos de Lançamentos e Saldos SOMENTE do Estabelecimentos selecionado, ou seja, o Estabelecimentos não é um Centralizador e não está associado a um Estabelecimentos Centralizador.
Vide: Módulo de Básicos >> Parâmetros, menu “Preliminares > Centralização da Escrituração de Obrigações Federais”,

Obs.: Essa regra deverá ser aplicada para TODOS os relatórios de conferências.


Este relatório, foi criado inicialmente no menu Report Fiscal, mas será disponibilizado também, no módulo Sped / ECD – Escrituração Contábil Digital


# Definição da tela




Todos os campos são de preenchimento obrigatório. Pelo menos uma validação deve ser informada.




# Layout do relatório:


O Relatório deve apresentar as informações relacionadas ao saldo de origem X02, X80 e lançamentos X01, de acordo com a validação escolhida na tela de geração.

**Se marcada a opção ‘Valida movimento (débito e crédito) entre as origens X01 (lançamentos) e X02 (saldos)’**
Será feito uma validação dos valores de débito e crédito da X02, com os totais de débito e de crédito de todos os lançamentos desta conta (X01). Se existir diferença entre esses valores será apresentado a mensagem no campo Advertência do relatório:
“Divergência no crédito e/ou débito (lançamento x saldo)”.

**Se marcada a opção ‘Valida movimento (débito e crédito) entre as origens X01 (lançamentos) e X80 (saldos por centro de custo)’**

Será feito uma validação dos valores de débito e crédito da X80, com os totais de débito e de crédito de todos os lançamentos desta conta (X01). Se existir diferença entre esses valores será apresentado a mensagem no campo Advertência do relatório:
“Divergência no crédito e/ou débito (lançamento x saldo por centro de custo)”.

**Se marcada a opção ‘Valida o saldo final do período anterior com o inicial do período, origem X02 (saldos)’**
Será feito uma validação entre o saldo inicial do período indicado em tela com o saldo final do período anterior, da X02, de todas as contas movimentadas no mês da geração do relatório. Caso seja encontrado divergências entre esses dois valores, será apresentado a mensagem no campo Advertência do relatório: “Divergência entre o saldo final do mês anterior com o saldo inicial do período da geração”.


**Se marcada a opção ‘Valida o saldo final do período anterior com o inicial do período, origem X80 (saldos por centro de custo)’**

Será feito uma validação entre o saldo inicial do período indicado em tela com o saldo final do período anterior, da X80, de todas as contas movimentadas no mês da geração do relatório. Caso seja encontrado divergências entre esses dois valores, será apresentado a mensagem no campo Advertência do relatório: “Divergência entre o saldo final do mês anterior com o saldo inicial período da geração”.


**Se marcada a opção ‘Valida o saldo final do período com o inicial do período posterior, origem X02 (saldos)’**
Será feito uma validação entre o saldo final do período indicado em tela com o saldo inicial do período posterior, da X02, de todas as contas movimentadas no mês da geração do relatório. Caso seja encontrado divergências entre esses dois valores, será apresentado a mensagem no campo Advertência do relatório: “Divergência entre o saldo final do mês com o saldo inicial do mês posterior ao período da geração”.


**Se marcada a opção ‘Valida o saldo final do período com o inicial do período posterior, origem X80 (saldos por centro de custo)’**

Será feito uma validação entre o saldo final do período indicado em tela com o saldo inicial do período posterior, da X80, de todas as contas movimentadas no mês da geração do relatório. Caso seja encontrado divergências entre esses dois valores, será apresentado a mensagem no campo Advertência do relatório: “Divergência entre o saldo final do mês com o saldo inicial do mês posterior ao período da geração”.


**Se marcada a opção ‘Valida os saldos da X02, com os lançamentos da X01’**

Será feito uma validação com os saldos da X02 e os lançamentos de débito e crédito da X01. Será verificado se o saldo inicial + os valores dos lançamentos da X01 (débitos e créditos) é igual ao saldo final da X02, caso seja encontrado divergência, será apresentado a mensagem no campo Advertência do relatório: “Há divergência entre o saldo final informado com o saldo calculado (saldo inicial + os movimentos dos lançamentos)”.

**Se marcada a opção ‘Valida os saldos por centro de custo da X80, com os lançamentos da X01’**

Será feito uma validação com os saldos da X80 e os lançamentos de débito e crédito da X01. Será verificado se o saldo inicial + os valores dos lançamentos da X01 (débitos e créditos) é igual ao saldo final da X02, caso seja encontrado divergência, será apresentado a mensagem no campo Advertência do relatório: “Há divergência entre o saldo final informado com o saldo calculado (saldo inicial + os movimentos dos lançamentos)”.



**Se marcada a opção ‘Valida os valores da conta da X02 com o valor totalizado desta conta na X80’**


Será feito uma validação, confrontando os valores da X80 (agrupando o valor por conta contábil) com as informações da X02. A Validação verifica todas as contas de natureza diferente de 1 e 2 (ativo e passivo) e valida se o somatório do saldo inicial + débitos e créditos e o saldo final da conta detalhada na X80 é igual aos valores indicados na X02.
Exemplo (sem divergência nos valores):
Origem X02:
Conta X: 	Saldo Inicial: 1000C 	Débito: 100  	Crédito: 200  	Saldo Final: 1100C
Origem X80:
Conta X, CentroCusto1: 	Saldo Inicial: 500C  	Débito:0  	Crédito:0 	Saldo Final: 500C
Conta X, CentroCusto2: 	Saldo Inicial: 500C 	Débito:100 	Crédito:200 	Saldo Final: 600C

Caso seja encontrado divergência, será apresentado a mensagem no campo Advertência do relatório: “Há divergência entre os valores do saldo da conta da X02 com o valor totalizado desta conta na X80”


**Se marcada a opção ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’**

Será feito uma validação, considerando o número de lançamento, entre os valores de crédito e débito da X01. Será verificado se esses valores são iguais, caso seja encontrado divergência, será apresentado a mensagem no campo Advertência do relatório: “Há divergência entre os valores de crédito e débito da X01 (por número de lançamento)”.


**Se marcada a opção ‘Valida se os valores de crédito e débito da X02 são iguais’**

Será feito uma validação entre os valores de crédito e débito da X02 (por conta contábil). Será verificado se esses valores são iguais, caso seja encontrado divergência, será apresentado a mensagem no campo Advertência do relatório: “Há divergência entre os valores de crédito e débito da X02”.


Apresentar no relatório (extensão CSV) as colunas:





(*) Não apresentar no relatório.







---

| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-44727 | Alessandra Cristina Navatta | Este relatório já está disponível no módulo. Esta demanda tem o objetivo apenas de documentá-lo (engenharia reversa). | 06/10/2020 |
| MFS-44727 | Alessandra Cristina Navatta | Inclusão do Centro de Custo, para considerar também origem X80 e disponibilizar o relatório também no módulo do SPED Contábil. Será alterada a extensão do relatório de XLS para CSV. | 06/10/2020 |
| MFS-44480 | Alessandra Cristina Navatta | Ajuste na tela, para desmembrar as validações que são realizadas no relatório. | 17/11/2020 |
| MFS-47660 | Alessandra Cristina Navatta | . Inclusão das validações: - saldo inicial + movimento (X01) com o saldo final (saldos de origem X02 e X80)  - saldo final do período igual ao saldo inicial do período posterior ao mês indicado na tela da geração. (Origens X02 e X80) | 21/12/2020 |
| MFS-58192 | Alessandra Cristina Navatta | Inclusão das validações:  - Valida os valores da conta da X02 com o valor totalizado desta conta na X80.  -Valida por número de lançamento se o valor de crédito e débito da X01 são iguais.  -Valida se os valores de crédito e débito da X02 são iguais. | 07/01/2021 |
| MFS-601602 | Rogério Ohashi | Alteração na regra de recuperação dos movimentos de Lançamentos e Saldos considerando Estabelecimentos Centralizador x Centralizados e alteração ao exibir os Estabelecimentos na opção de Grid de Estabelecimentos. | 17/01/2024 |


---

| Campo | Regra | Demanda |
| --- | --- | --- |
| Validações | Opções Válidas:  Valida movimento (débito e crédito) entre as origens X01 (lançamentos) e X02 (saldos) Valida movimento (débito e crédito) entre as origens X01 (lançamentos) e X80 (saldos por centro de custo) Valida o saldo final do período anterior com o inicial do período, origem X02 (saldos) Valida o saldo final do período anterior com o inicial do período, origem X80 (saldos por centro de custo) Valida o saldo final do período com o inicial do período posterior, origem X02 (saldos) Valida o saldo final do período com o inicial do período posterior, origem X80 (saldos por centro de custo) Valida os saldos da X02, com os lançamentos da X01 Valida os saldos por centro de custo da X80, com os lançamentos da X01 Valida os valores da conta da X02 com o valor totalizado desta conta na X80 Valida por número de lançamento se o valor de crédito e débito da X01 são iguais. Valida se os valores de crédito e débito da X02 são iguais | MFS-44480 MFS-47660 MFS-58192 |
| Grid Estabelecimentos | Exibir todos os estabelecimentos da empresa selecionada na tela.  [ALTERAÇÃO- MFS-601602]  Para possibilitar que o sistema considere todos os Lançamentos/Saldos do Estabelecimento Centralizador e Centralizados, o Grid de Estabelecimento deverá ser alterado, conforme informação de Estabelecimentos Centralizador x Centralizados e Estabelecimentos não centralizados, passando a exibir da seguinte forma:        - Estab. Centralizador: AA001 – Estabelecimento Centralizador      - Estab. Descentralizado: AA002 – Estabelecimento Não Centralizado  Obs.: Para maiores detalhes consultar Item de Regras Gerais. | MFS-44727 MFS601602 |
| Selecionar | Permite que o usuário selecione os Estabelecimentos que serão gerados a conferência.   Tratamentos:  Modal 'Selecionar Estabelecimentos‘ Ao ser acionado abrir o Modal 'Selecionar Estabelecimentos‘. Apresentando os campos Cód. Estab e Descrição Botões do Modal 'Selecionar Estabelecimentos': Critério, Cancelar, OK e Salvar...   Botões Critério, Cancelar, OK e Salvar  - Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Estabelecimentos‘ será fechado.  - Ao selecionar o botão 'Critério', os estabelecimentos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar.  -Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os estabelecimentos no componente “Estabelecimentos” da tela Principal - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um registro”. -Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas dos estabelecimentos (no diretório local e formato que o usuário informar). | MFS-44727 |
| Marcar Todos | Permite ao usuário selecionar ou desmarcar todos os registros da grid Estabelecimentos. | MFS-44727 |
| Executar | A empresa deve ser informada, caso contrário, será apresentada a mensagem: “Informe a empresa!”  O período deve ser informado, caso contrário, será apresentado a mensagem: “Informe o período!”  Pelo menos um estabelecimento deve ser selecionado, caso contrário, será apresentado a mensagem: “Informe o estabelecimento!”  Apenas serão realizadas as validações que o usuário marcar na tela. Pelo menos uma validação, deve ser selecionada, caso não esteja marcado, exibir a mensagem: “Informe pelo menos uma validação!” | MFS-44727 MFS-44480 |


---

| Campo | Formato / Default | Regra |
| --- | --- | --- |
| Empresa | Código. | Exibir o código da empresa. |
| Estabelecimento | Código | Exibir o código do estabelecimento. |
| Período | MM/AAAA | Exibir o período indicado na tela. |
| Código da Conta | Código | Exibir o código da conta contábil. |
| Natureza da Conta | Descrição | Exibir a descrição da natureza da conta (Conforme cadastro na X2002) |
| Código do Centro de Custo | Código | Exibir o código do centro de custo.(Conforme cadastro na X2003) |
| Saldo Final (Mês Anterior) | Se indicador do saldo for D: -0,00 Se indicador do saldo for C: 0,00 | Exibir o saldo final da conta contábil, do mês anterior ao período indicado na tela.  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Saldo Inicial | Se indicador do saldo for D: -0,00 Se indicador do saldo for C: 0,00 | Exibir o saldo inicial da conta contábil, do período indicado na tela.  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
|  | 0,00 | Exibir o total de créditos dos lançamentos da conta contábil, do período indicado na tela.  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Créditos do Período (Saldo) | 0,00 | Exibir o total de créditos do saldo da conta contábil, do período indicado na tela.  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Dif. Crédito (LançamentosxSaldo) | -0,00 (valores negativos) 0,00 (valores positivos) | Resultado da diferença entre os campos de créditos do período (lançamento) e de créditos do período (saldo)  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
|  | 0,00 | Exibir o total de débitos dos lançamentos da conta contábil, do período indicado na tela.  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Débitos do Período (Saldo) | 0,00 | Exibir o total de débitos do saldo da conta contábil, do período indicado na tela.  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Dif. Débito (LançamentosxSaldo) | -0,00 (valores negativos) 0,00 (valores positivos) | Resultado da diferença entre os campos de débitos do período (lançamento) e de débitos do período (saldo)  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Num. Lançamento |  | Apresenta o número do lançamento.  Este campo só deve ser preenchido, se for selecionado a validação:  Valida por número de lançamento se o valor de crédito e débito da X01 são iguais. |
| Total de Créditos (Num. Lançamento) | 0,00 | Apresenta o total de créditos por número de lançamento.  Este campo só deve ser calculado, se for selecionado a validação:  Valida por número de lançamento se o valor de crédito e débito da X01 são iguais. |
| Total de Débitos (Num. Lançamento) | 0,00 | Apresenta o total de débitos por número de lançamento.  Este campo só deve ser calculado, se for selecionado a validação:‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais. |
| Dif.  Créditos x Débitos (Num.Lançamento) | -0,00 (valores negativos) 0,00 (valores positivos) | Resultado da diferença entre os campos ‘Total de Créditos (Num. Lançamento)’ e ‘Total de Débitos (Num. Lançamento)’.  Este campo só deve ser calculado, se for selecionado a validação: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais. |
| Dif.  Crédito x Débito (Saldos) | -0,00 (valores negativos) 0,00 (valores positivos) | Resultado da diferença entre os campos de créditos (saldo) e de débitos (saldo).   Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Dif. Saldo Final (X02xSomatorioX80) | -0,00 (valores negativos) 0,00 (valores positivos) | Resultado da diferença entre os saldos da 02 com o saldo totalizado da X80.  Este campo só deve ser calculado, se for selecionado a validação: ‘Valida os valores da conta da X02 com o valor totalizado desta conta na X80’ |
| Saldo Final | Se indicador do saldo for D: -0,00 Se indicador do saldo for C: 0,00 | Exibir o saldo final da conta contábil, do período indicado na tela.  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Saldo Inicial (Mês Posterior) | Se indicador do saldo for D: -0,00 Se indicador do saldo for C: 0,00 | Exibir o saldo inicial da conta contábil, do mês posterior ao período indicado na tela.  Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Saldo Inicial + Movimentações (X01) | -0,00 (valores negativos) 0,00 (valores positivos) | Exibir o resultado do somatório do saldo Inicial da conta contábil, com os valores de total de débito e crédito dos lançamentos da conta do período indicado na tela.   Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Dif. Saldo Final | Se indicador do saldo for D: -0,00 Se indicador do saldo for C: 0,00 | Resultado da diferença entre os campos ‘’Saldo Inicial + Movimentações (X01)’ e ‘Saldo Final’.   Para as Validações: ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’ e ‘ Valida os valores da conta da X02 com o valor totalizado desta conta na X80’, não calcular esse campo (exibir nulo no relatório) |
| Advertências |  | Exibir as advertências conforme os cenários citados abaixo (maiores explicações dos cenário, considerar o detalhamento do item 2. Layout do relatório:  Se pelo menos uma das opções: ‘Valida o saldo final do período anterior com o inicial do período, origem X02 (saldos)’ e ou  ‘Valida o saldo final do período anterior com o inicial do período, origem X80 (saldos por centro de custo)’ estiver selecionada e -Se existir diferença entre os campos ‘Saldo Final (Mês Anterior)’ e ‘Saldo Inicial’, exibir a mensagem: “Divergência entre o saldo final do mês anterior com o saldo inicial do período da geração”.    Se pelo menos uma das opções: ‘Valida o saldo final do período com o inicial do período posterior, origem X02 (saldos)’ e ou  ‘Valida o saldo final do período com o inicial do período posterior, origem X80 (saldos por centro de custo)’ estiver selecionada e -Se existir diferença entre os campos ‘Saldo Final’ e ‘Saldo Inicial (Posterior)’, exibir a mensagem: “Divergência entre o saldo final do mês com o saldo inicial do mês posterior ao período da geração”  -Se não for encontrado saldo do período posterior (X02 ou X80, de acordo com as opções selecionadas), exibir a mensagem: “Não foi encontrado na base, dados de saldo no período posterior a geração”   Se a opção: ‘Valida movimento (débito e crédito) entre as origens X01 (lançamentos) e X02 (saldos)’ estiver selecionada e   -Se existir divergências de créditos (campo  Dif. Crédito (LançamentosxSaldo)diferente de zero), exibir a mensagem: “Divergência no crédito e/ou débito (lançamento x saldo) -Se existir divergências de débitos (campo  Dif. Débito (LançamentosxSaldo)diferente de zero), exibir a mensagem: “Divergência no crédito e/ou débito (lançamento x saldo)   Se a opção ‘Valida movimento (débito e crédito) entre as origens X01 (lançamentos) e X80 (saldos por centro de custo)’ estiver marcada e  -Se existir divergências de créditos (campo Dif. Crédito (LançamentosxSaldo) diferente de zero), exibir a mensagem: “Divergência no crédito e/ou débito (lançamento x saldo por centro de custo) -Se existir divergências de débitos (campo Dif. Débito (LançamentosxSaldo) diferente de zero), exibir a mensagem: “Divergência no crédito e/ou débito (lançamento x saldo por centro de custo)   Se pelo menos uma das opções: ‘Valida os saldos da X02, com os lançamentos da X01’ e ou ‘Valida os saldos por centro de custo da X80, com os lançamentos da X01’, estiver selecionada e  - Se existir diferença entre os campos ‘’Saldo Inicial + Movimentações (X01)’ e ‘Saldo Final’. exibir a mensagem: “Há divergência entre o saldo final informado com o saldo calculado (saldo inicial + os movimentos dos lançamentos)”   Se a opção ‘Valida os valores da conta da X02 com o valor totalizado desta conta na X80’ estiver selecionada e   -Se existir diferença entre os valores da X80 (agrupando o valor por conta contábil) com as informações da X02 das  contas de natureza diferente de 1 e 2 (ativo e passivo), exibir a mensagem: “Há divergência entre os valores do saldo da conta da X02 com o valor totalizado desta conta na X80”   Se a opção ‘Valida por número de lançamento se o valor de crédito e débito da X01 são iguais’, estiver selecionada e   - Se existir diferença por número de lançamento entre o valor de crédito e de débito, exibir a mensagem: “Há divergência entre os valores de crédito e débito da X01 (por número de lançamento)”.   Se a opção ‘Valida se os valores de crédito e débito da X02 são iguais’, estiver selecionada e  -Se existir diferenças entre os valores de crédito e débito da X02 (por conta contábil), exibir a mensagem: “Há divergência entre os valores de crédito e débito da X02”.  Obs. Se um registro se enquadrar em mais de uma inconsistência, o mesmo deve ser exibido N vezes no relatório (considerando as validações escolhidas na tela de geração). |
