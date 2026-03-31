# Tela_Saldos_das_Contas_da_ParteB

> Fonte: Tela_Saldos_das_Contas_da_ParteB.doc

THOMSON REUTERS

Tela de Saldos das Contas da Parte B
ECF - Escrituração Contábil Fiscal


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		20/12/2017	MFS-15272	Criação do documento	Alessandra Cristina Navatta 		19/01/2018	MFS-15968	Ajustes referente a reformulação da tela de Lançamentos da Parte B (M410)	Alessandra Cristina Navatta		28/02/2018	MFS-16667	Substituída a mensagem DW00082 por DW00170	Alessandra Cristina Navatta		


Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc507596874" 1.	INTRODUÇÃO	 PAGEREF _Toc507596874 \h 3
 HYPERLINK \l "_Toc507596875" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc507596875 \h 3
 HYPERLINK \l "_Toc507596876" 3.	TELA/MODAIS	 PAGEREF _Toc507596876 \h 3
 HYPERLINK \l "_Toc507596877" 3.1 Pesquisa de Registros	 PAGEREF _Toc507596877 \h 3
 HYPERLINK \l "_Toc507596878" 3.2 Regras dos Campos Tela Principal	 PAGEREF _Toc507596878 \h 4
 HYPERLINK \l "_Toc507596879" 3.3 Modais	 PAGEREF _Toc507596879 \h 10


INTRODUÇÃO

Objetivo desta especificação é criar a tela de saldo inicial da escrituração das contas da Parte B.

 DOCUMENTOS DE REFERÊNCIA

Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx

TELA/MODAIS

3.1 Pesquisa de Registros

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Manutenção >> Saldos das Contas da Parte B

Título da tela: Saldos das Contas da Parte B


Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.

Campo	Tipo	Regra		Estabelecimento 	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
(AAAA)
	O usuário poderá informar o exercício. 


		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código – Descrição)	Aplicar a RNG00004 - Versão de Layout		Forma de Tributação	Lista
(Código – Descrição)	-Lucro Real, Lucro Presumido, Lucro Arbitrado
		Apuração	Lista
(Código – Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral
		


3.2 Regras dos Campos Tela Principal

Localização da tela: 
ECF – Escrituração Contábil Fiscal >> Manutenção >> Saldos das Contas da Parte B

Título da tela: Saldos das Contas da Parte B


Condições Gerais:

Só permitir adicionar, alterar ou excluir registros, enquanto o ultimo período de abertura da escrituração estiver com status diferente de ‘Calculo Realizado’. Caso status do ultimo período = Calculo Realizado, exibir a mensagem DW00170.

Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Dados Gerais		Estabelecimento	Texto	S	N	Tipo – Código – Descrição	Permite que o usuário visualize o estabelecimento correspondente ao registro selecionado na tabela de Informações ECF.	MFS-15272		Exercício	Texto	S	N	AAAA	Permite que o usuário visualize o ano correspondente ao registro selecionado na tabela de informações ecf.	MFS-15272		Data Inicial	Texto	S	N	DD/MM/AAAA	Permite que o usuário visualize a data inicial, referente ao registro selecionado na tabela das informações ecf.	MFS-15272		Versão	Texto	S	N	Código – Descrição	Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro, referente ao registro selecionado na tabela de informações ecf.	MFS-15272		Forma de Tributação	Texto	S	N	Descrição	Permite que o usuário visualize a forma de tributação, referente ao registro selecionado na tabela das informações ecf.	MFS-15272		Apuração	Texto	S	N	Descrição	Permite que o usuário visualize a apuração, referente ao registro selecionado na tabela das informações ecf.	MFS-15272		Data Final do Último Período da Escrituração	Texto	S	N	DD/MM/AAAA 	Permite que o usuário visualize a  data final do último período da escrituração. 

Tratamento:

Com base na escrituração recuperada, considerar neste campo a data final do último período da escrituração.
	MFS-15272		Título (*)
Saldo da Conta da Parte B da Escrituração		Adicionar	Botão	 	 	 	Permite ao usuário adicionar um saldo inicial da escrituração de uma conta da parte b.
Tratamentos: -Só poderá ser inserido um novo registro até o status do ultimo período da escrituração for diferente de calculo realizado. 
Ao acionar esse botão abrir o modal  HYPERLINK  \l "ModalAdicionarSaldoInicial" Adicionar Saldo Inicial da Conta da Parte B.
	MFS-15272
MFS-15968		Alterar	Botão		Permite ao usuário alterar o saldo da conta da parte B.

Tratamentos:

-Só poderá se alterado registro até o status do ultimo período da escrituração for diferente de calculo realizado.

- Se não existir saldo na base e este botão for selecionado, exibir a mensagem DW00202.


Ao acionar esse botão abrir o modal  HYPERLINK  \l "ModalAdicionarSaldoInicial" Alterar Saldo Inicial da Conta da Parte B .


	MFS-15272
MFS-15968		Remover	Botão		Permite que o usuário remova um ou mais registros de saldos que foram selecionados na grid. 

Tratamentos:

-Pelo menos, um registro da grid deve ser selecionado, caso contrário, exibir a mensagem  DW00149.

-Ao selecionar o botão, se pelo menos um registro for selecionado na grid, aplicar a RG00041 – Botão Remover, se o status do ultimo período da escrituração for diferente de calculo realizado. 


- Verificar se a Conta da Parte B possui lançamentos da parte B (Registros M410 ou Contrapartida) para algum dos períodos de apuração, se existir e todas as aberturas de apuração desta escrituração estiverem com status diferente de ‘Calculado Realizado’, exibir a mensagem DW00153. Se o usuário selecionar ‘Sim’, excluir o saldo e os registros de lançamento da parte B, desses registros. Caso o usuário selecione o ‘Não’, nada será realizado/excluído para estes registros.

	MFS-15272
MFS-15968		Marcar Todos	Check-box	S	S	Desmarcado	Permite selecionar todos os registros da grid. Funcionalidades que podem se valer desta é  Remover.

	MFS-15272		Campos Exibidos na grid (*)		Check-box	-	-	-	-	Permite ao usuário selecionar um ou mais registros para a exclusão dos saldos das contas da parte B

Tratamentos:

Apresentar o check-box, apenas para os registros que não possuem sinalizados os 
campos Parte A e Parte B com Cálculo Realizado da grid de saldos. Isso porque, os registros com esses dados não podem ser excluídos da base.
	MFS-15272
MFS-15968		Grupo	Texto	S	N	Código – Descrição	Permite que o usuário visualize o código e a descrição do grupo da conta da parte B.
	MFS-15272		
Conta da Parte B
	Texto	S	N	Código – Descrição	Permite que o usuário visualize o código e a descrição da conta da parte B.


	MFS-15272		Tributo	Texto	S	S	Descrição	Permite que o usuário visualize ou altere o tributo do saldo.


Opções Válidas:

Imposto de Renda Pessoa Jurídica
Contribuição Social sobre o Lucro Líquido
	MFS-15272		Linha 	Texto	S	S	Código – Descrição	Permite que o usuário visualize a linha da tabela dinâmica.
	MFS-15272		CNPJ Origem	Texto	N	S	xxx.xxx.xxx\xxxx-xx	Permite que o usuário visualize/altere o CNPJ Origem.

Aplicar regra de negócio geral << RNG00042 – Validação de CNPJ >>
	MFS-15272		Valor do Saldo Inicial da Escrituração		S	S	0,00
	Permite que o usuário visualize/altere o valor do saldo inicial da conta da parte B.


	MFS-15272		Ind. Do Saldo		S	S	C – Crédito ou 
D – Débito	Permite que o usuário visualize/altere o  indicador do saldo inicial da conta da parte B.

Opções Válidas:

C – Crédito
D – Débito
	MFS-15272		Lançamentos 		Parte A	Check	S	N		Permite que o usuário visualize se há lançamentos da parte A, para este saldo.	MFS-15968		Parte B com Cálculo Realizado	Check	S	N		Permite que o usuário visualize se há lançamentos da parte B, para este saldo de conta da parte B e se foi gerado o cálculo no processamento em lote para algum período de apuração da escrituração.
	MFS-15968		Parte B sem Cálculo Realizado	Check	S	N		Permite que o usuário visualize se há lançamentos da parte B, para este saldo de conta da parte B e se não foi gerado o cálculo no processamento em lote para algum período de apuração da escrituração.
	MFS-15968		
(*) Não exibir a descrição na tela.

3.3 Modais

Modal (*)Título:  Adicionar Saldo Inicial da Conta da Parte B ou Alterar Saldo Inicial da Conta da Parte B


Voltar para o  HYPERLINK  \l "BotaoAdicionar" botão Adicionar
Voltar para o  HYPERLINK  \l "BotaoAlterar" botão Alterar

 
 	 		Grupo	LOV	S	N	Código - Descrição	Permite que o usuário selecione o código e a descrição  do grupo da conta da parte B.
	MFS-15272		
Conta da Parte B
	LOV	S	N	Código - Descrição	Permite que o usuário selecione o código e a descrição da conta da parte B.


Recuperação das Contas:

Recuperar apenas as contas cuja data de criação e limite da conta esteja vigente no período da Escrituração recuperada.

	MFS-15272		Tributo	Lista	S	S	Descrição	Permite que o usuário selecione o tributo do saldo.


Opções Válidas:

Imposto de Renda Pessoa Jurídica
Contribuição Social sobre o Lucro Líquido
	MFS-15272		Linha 	LOV	N	S	Código - Descrição	Permite que o usuário selecione  a linha da tabela dinâmica.

Tratamentos:


Recuperar as linhas considerando:
a) Versão da Informação ECF selecionada
b) registro equivalente ao Tributo selecionado.
M300 ( I
M350 ( C
c) registro do grupamento A, B, C de acordo com a Qualificação PJ da Informação ECF selecionada.
d) linhas do tipo ‘E’ ou ‘CA’

	MFS-15272	
MFS-15968		CNPJ Origem	Texto	N	S	xxx.xxx.xxx\xxxx-xx	Permite que o usuário selcione o CNPJ Origem.

Aplicar regra de negócio geral << RNG00042 - Validação de CNPJ >>
	MFS-15272		Valor do Saldo da Escrituração		S	S	0,00 	Permite que o usuário informe o valor do saldo inicial da conta da parte B.


Tratamentos:

Se a data de criação da conta da parte B estiver no mesmo ano que a escrituração recuperada (data inicial) e o valor do saldo for diferente de zero, exibir a mensagem DW00167

	MFS-15272		Indicador do Saldo		S	S	

C – Crédito ou
D - Débito
	
Opções Válidas:

C - Crédito
D - Débito
	MFS-15272		OK	Botão		Permite ao usuário adicione um registro de saldo inicial de escrituração de uma conta da Parte B.Tratamentos:

Ao adicionar um registro, se a informação já existir na base, não permitir a inclusão, (aplicar a RNG00011 - Duplicidade de Registro).

Ao alterar um saldo, se a Conta da Parte B possuir Registro na Tabela M305/M355, exibir a mensagem DW00151.

Aplicar a RNG00044 - Cálculo do Registro M500, se o saldo for alterado.

	MFS-15272
MFS-15968		Cancelar	Botão		Ao acionar esse botão o sistema fecha o modal e volta para tela anterior.	MFS-15272		(*) Não exibir a descrição na tela.