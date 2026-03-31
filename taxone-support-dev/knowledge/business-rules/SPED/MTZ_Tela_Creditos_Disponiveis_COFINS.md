# MTZ_Tela_Creditos_Disponiveis_COFINS

> Fonte: MTZ_Tela_Creditos_Disponiveis_COFINS.doc

(EFD-PIS/PASEP – COFINS) – Créditos Disponíveis – COFINS


DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS3169-GE28	Alteração na tela Créditos Disponíveis – COFINS	Incluir na tela Créditos Disponíveis (COFINS) o critério de pesquisa Código do Tipo de Crédito.	07/11/2011		OS4106	Alteração na tela Créditos Disponíveis – COFINS	Permitir inclusão manual dos creditos, para os tipos de crédito 107, 207 e 307.	30/07/2013		CH17810-C/2013	Alteração na tela Créditos Disponíveis – PIS/PASEP	Ajuste na RN08 para incluir exceção dos tipos de crédito 107, 207 e 307.	06/03/2014		MFS28515	Alteração na tela Créditos Disponíveis – PIS/PASEP	Incluir uma nova opção para o campo Status.	18/10/2019		MFS34355	Liliane Assaf	Alteração no tratamento dos créditos prescritos com mais de 5 anos.
Desfazendo a alteração feita pela MFS28515	28/06/2020		
REGRAS DE NEGÓCIO


Cód.		DR		RN00	
Inclusão do critério de Pesquisa ‘Cód. Tipo Crédito’, na tela ‘Créditos Disponíveis’ no Menu: Obrigações ( Manutenção ( Controles dos Créditos Fiscais – COFINS
	OS3169-GE28		RN01	O Cód. Tipo Crédito deve ter as seguintes opções:

TFIX93 (101,102,103,104,105,106,108,109,199,201,202,203,204,205,206,208,209,299,301,302,303,304,305,306,308,309,399) e Em Branco.

Se o usuário escolher a opção em branco, todos os códigos deverão ser apresentados.
	OS3169-GE28		RN2	Incluir campo origem saldo com as opções 1 – DACON  2 –PER/DECOMP na tela Créditos Disponíveis no  no Menu: Obrigações ( Manutenção ( Controles dos Créditos Fiscais – COFINS	
REQ_OS_3650		RN03	Permitir a digitação de valores referentes períodos de apuração fechados somente se a opção selecionada no campo origem do saldo for igual à PERDECOMP	REQ_OS3169-DW17		A tela de Créditos Disponíveis (COFINS) deverá ter os campos descritos abaixo, permitindo a inclusão, alteração e exclusão de um ou mais registros.

Pesquisa por Período
Estabelecimento
Mês/Ano
Cód. (tipo de crédito)
Descr. Tipo de Crédito
Origem de Crédito;
CNPJ;
Crédito Apurado;
Crédito Extemporâneo;
Crédito Utilizado para Desconto;
Crédito Utilizado por Pedido de Ressarcimento;
Crédito Utilizado por Compensação intermediária;
Crédito Utilizado por Transferência (Cisão, Fusão e Incorporação);
Outros Créditos Utilizados; e
Crédito Disponível.		RN04	Após o usuário informar na Pesquisa do Período na tela de Créditos Disponíveis, o sistema de apresentar dos todos os saldos credores por tipo de crédito das escriturações de períodos anteriores que o campo Crédito Disponível desta tela, esteja com o valor maior que zero.

Para a escrituração do período atual, o sistema deve apresentar todos os saldos credores por tipo de crédito que estejam com o campo 13 (Indicador de opção de utilização do crédito disponível no período) do registro M100 igual ‘’2 ‘’.	REQ_OS3169-DW17		RN05	Na inclusão de um ou mais saldo credor por tipo de crédito, o campo CNPJ somente deve ficar habilitado na tela, se o campo origem do crédito esteja preenchido com a opção: ‘’ Crédito transferido por pessoa jurídica sucedida’’ nesta tela.	REQ_OS3169-DW17		RN06	O valor do campo Crédito Disponível será calculado através da seguinte regra:
Crédito Apurado + Crédito Extemporâneo - Crédito Utilizado para Desconto - Crédito Utilizado por Pedido de Ressarcimento - Crédito Utilizado por Compensação intermediária - Crédito Utilizado por Transferência (Cisão, Fusão e Incorporação).
	REQ_OS3169-DW17		RN07	Os saldos credores por tipo de crédito que foram incluídos pelo usuário o sistema deve permitir alterar somente os campos valores, com exceção do campo Crédito Disponível que deve ser recalculado pelo o sistema.	REQ_OS3169-DW17		RN08	O sistema somente deve permitir a inclusão de novos saldos credores disponíveis em um período que não existe apuração, se for diagnosticado que realmente o cliente está iniciando o processo de escrituração pelo módulo pelo EFD-PIS/PASEP-COFINS. Ou seja, está na sua primeira escrituração fiscal. Somente uma das duas situações é permitida:

Não existir registros de apuração gerados através da funcionalidade de Geração dos Registros para empresa, localizado: Sped ’! EFD   Escrituração Fiscal Digital - PIS/PASEP-COFINS ’! Obrigações ’! Manutenção ’! Controle de Créditos Fiscais   PIS/PASEP(Créditos Disponíveis.

Só será permitida a inclusão de novos saldos credores por tipo de crédito disponíveis, se o período (mês/ano digitado) em que o crédito será incluído for ANTERIOR ao período da PRIMEIRA APURAÇÃO e que esta esteja ABERTA ou para inclusão manual de saldo credor do tipo de crédito com código 107, 207 ou 307, permitindo a inclusão apenas em apuração aberta (códigos ‘1’ – Apuração Realizada e ‘2’ – Apuração Reaberta), conforme RN09. 
	REQ_OS3169-DW17
CH17810-C/2013
		RN09	Será permitida a inclusão manual de saldo credor por tipo de crédito em apuração aberta (códigos ‘1’ – Apuração Realizada e ‘2’ – Apuração Reaberta), para os códigos 107,207 ou 307. 	OS4106
		RN10	O sistema somente deve permitir alterar e/excluir o registro do tipo de crédito nas seguintes condições: 

A)	O registro do tipo de crédito foi inserido manualmente.
B)	O registro do tipo de crédito não foi utilizado nas escriturações do EFD Contribuições em período atual e em períodos anteriores. 
C)	O registro do tipo de crédito pertence a uma apuração que esteja ABERTA. 

Caso a condição (A) não seja atendida, o sistema deve exibir as seguintes mensagens abaixo e não gravar o registro:
Para alteração: 
Não é permitida a alteração do crédito, pois ele foi gerado pelo sistema. 
Para exclusão:
Não é permitida a exclusão do crédito, pois ele foi gerado pelo sistema. 

Caso a condição (B) não seja atendida, o sistema deve exibir as seguintes mensagens abaixo e não gravar o registro:
Para alteração:
Não é permitida a alteração do crédito, pois ele já foi utilizado em apurações. 
Para exclusão:
Não é permitida a exclusão do crédito, pois ele já foi utilizado em apurações.

Caso a condição (C) não seja atendida, o sistema deve exibir as mensagens abaixo e não gravar o registro:
Para alteração:
Não é permitida a alteração do crédito, pois a apuração para este período se encontra fechada.
Para exclusão:
Não é permitida a exclusão do crédito, pois a apuração para este período se encontra fechada.
	OS4106		RN11	Campo Status

Campo somente para consulta. 
Valores que compõe esse campo:
- Disponível
- Fechado

O campo vai ser habilitado para alteração, com as seguintes opções:
- Disponível
- Cancelado por Prazo de Prescrição
	MFS28515
MFS34355
		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:


RN01	[EXCLUÍDA – OSXPTO] De