# ECD_Geracao_de_Saldos_por_centro_de_Custo_Requisito_V1

> Fonte: ECD_Geracao_de_Saldos_por_centro_de_Custo_Requisito_V1.doc

TITLE  "ECD - Livros SPED (Matriz)"  \* MERGEFORMAT ECD - Geração de Saldos por Centro de Custo


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		MFS46979	ECD – Geração de Saldos por Centro de Custo 	Incluído no Tax One a funcionalidade de geração de dados de saldos por centro de custo a partir dos saldos final do período anterior (safx80) e do movimento do período (safx01).

Para o correto funcionamento, é necessário a carga inicial do saldo por centro de custo, os períodos seguintes passam a ser processados por essa nova funcionalidade.
		

REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN01	Consultar o saldo anterior por centro de custo, selecionar a tabela X80 (definitiva), filtrando por empresa, estabelecimento selecionado na tela e a data de saldo compreendida no período anterior ao período informado em tela. Nesta seleção iremos considerar o saldo atual gravado na tabela e consideraremos como saldo inicial do período atual.	MFS46979		RN02	Consultar os lançamentos contábeis do período selecionado agrupando por conta, centro de custo e agrupando os valores de lançamento. Selecionar a tabela X01 (definitiva), filtrando por empresa, estabelecimento selecionado. Filtrar por todos os lançamentos cuja data do lançamento esteja compreendida dentro do período selecionado. Obter as informações de conta, centro de custo, indicador de débito/crédito e valor de lançamento.	MFS46979		RN03	Calcular o saldo atual por centro de custo com base no saldo anterior e a soma dos lançamentos. Para esse cálculo iremos considerar o saldo anterior obtido na RN01 acrescido dos valores de débito/crédito, obtidos na RN02. Lembrando que se o saldo anterior, for devedor, deverá ser somado os lançamentos de débito e subtraído de crédito, e vice-versa. Caso o saldo calculado for negativo deverá ser gravado o valor absoluto e invertido o indicador de débito e crédito.	MFS46979		RN04	Apresentar no log a quantidade de registros que serão inseridos ou atualizados. Deverá ser consultado a tabela de saldos (X80) do período atual e verificado a cada conta e centro de custo a existência de registros caso positivo deverá ser quantificado na linha de atualizados, caso contrário acrescer na linha de registros inseridos. Apresentar o LOG conforme exemplo abaixo.

	MFS46979		RN05	Gerar um relatório apresentando as informações do registro que será inserido/alterado e a respectiva operação. O relatório deverá ser salvo no formato excel e deverá contemplar as seguintes informações:
Empresa – Preencher com código da empresa
Estabelecimento – Preencher com código do estabelecimento
Data do Saldo – Preencher com a data do saldo, correspondente ao último dia do mês
ID – Grupo – Conta – Preencher com as informações da conta (Ident, grupo, código e descrição da conta)
ID – Grupo – Centro de Custo – Preencher com as informações do centro de custo (Ident, grupo, código e descrição do centro de custo)
Saldo Anterior – Preencher com saldo anterior e ao final do campo incluir se é débito ou crédito
Débitos – Preencher com total de débitos do período
Créditos – Preencher com total de créditos do período
Saldo Atual – Preencher com o saldo atual do período e ao final do campo incluir se é débito ou crédito
Operação – Preencher se é uma inclusão ou alteração
	MFS46979		RN06	Se a opção apenas simular estiver desmarcada, o processo deverá realizar a gravação de saldos por centro de custo. Nesse caso deverá fazer a inclusão ou alteração de dados na tabela de saldos por centro de custo x80 (definitiva), conforme dados recuperados anteriormente.	MFS46979