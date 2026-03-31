# Tela_Contas_da_ParteB

> Fonte: Tela_Contas_da_ParteB.doc

THOMSON REUTERS

Tela Contas da Parte B
ECF - Escrituração Contábil Fiscal


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		20/12/2017	MFS-15272	Criação do documento	Alessandra Cristina Navatta 		


Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc501617775" 1.	INTRODUÇÃO	 PAGEREF _Toc501617775 \h 3
 HYPERLINK \l "_Toc501617776" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc501617776 \h 3
 HYPERLINK \l "_Toc501617777" 3.	TELA/MODAIS	 PAGEREF _Toc501617777 \h 3
 HYPERLINK \l "_Toc501617778" 3.1 Pesquisa de Registros	 PAGEREF _Toc501617778 \h 3
 HYPERLINK \l "_Toc501617779" 3.2 Regras dos Campos Tela Principal	 PAGEREF _Toc501617779 \h 4


INTRODUÇÃO

Objetivo desta especificação é criar a tela de cadastro das Contas da Parte B.

 DOCUMENTOS DE REFERÊNCIA

Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx

TELA/MODAIS

3.1 Pesquisa de Registros

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Manutenção >> Contas da Parte B

Título da tela: Contas da Parte B


Campo	Tipo	Regra		Grupo	LOV
(Código – Descrição)	Permite que o usuário busque o registro pelo Código  e descrição do grupo		Conta da Parte B	Texto
	O usuário poderá pesquisar o registro pelo código da conta da parte B. 


		Descrição da Conta da Parte B	Texto	O usuário poderá pesquisar o registro pela descrição da conta da parte B. 
		Data de Criação	Data
DD/MM/AAAA	O usuário poderá pesquisar o registro pela data de criação da conta.		Data Limite	Data
DD/MM/AAAA	O usuário poderá pesquisar o registro pela data limite da conta. 		


3.2 Regras dos Campos Tela Principal

Localização da tela: 
ECF – Escrituração Contábil Fiscal >> Manutenção >> Contas da Parte B

Título da tela: Contas da Parte B


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		 Botões Toolbar		Abre	Botão		Permite ao usuário abrir um registro existente na base.

Tratamentos:

Os campos de pesquisa estão definidos no item  HYPERLINK  \l "ItemPesquisadeRegitro" 3.1 Pesquisa de Registro deste documento.
	MFS-15272		Exclui	Botão		Permite que o usuário exclua uma conta da parte B.

Tratamentos:

Aplicar a RNG00043 – Remover2

Verificar na Tela de Informações ECF se a Conta da Parte B está parametrizada na Aba LALUR e LACS para os campos “Cód. da Conta da Parte B” para Lançamento de Prejuízo ou “Cód. da Conta da Parte B” para Lançamento de Base Negativa.
Caso seja encontrada a conta na parametrização acima, exibir a mensagem DW00155. 


Verificar na Tela de Informações ECF se o campo “Cód. da Conta da Parte B” do tópico “AJUSTE DA PARTE B AUTOMÁTICO PARA INCENTIVO PAT” da Aba LALUR e LACS está preenchido e se é a mesma conta da parte B que o usuário está tentando excluir.
Caso seja encontrada a conta na parametrização acima, exibir a mensagem DW00155. 


Verificar na Tela de Associação das Contas da Parte B com Contas da Parte A se a Conta da Parte B se existe alguma associação para a conta da Parte B. 
Caso seja encontrada a conta na parametrização acima, exibir a mensagem DW00155. 


Se a conta da parte B possuir saldo, não permitir remover o registro e exibir a mensagem DW00155.

Se a conta da Parte B, está associada na tela de Associação da Conta da Parte A com Conta da Parte B, não permitir remover o registro e exibir a mensagem DW00155.


	MFS-15272		Confirma	Botão		Permite ao usuário confirmar a inserção/atualização do registro.

Tratamentos:

RNG00011 - Duplicidade de Registro.
	MFS-15272		Dados Gerais		Grupo	LOV	S	N	Código – Descrição	Permite que o usuário selecione  o código e a descrição do grupo que a conta está vinculada.	MFS-15272		Conta da Parte B	Texto	S	N	Código	Permite que o usuário informe o código da conta da Parte B.	MFS-15272		Descrição da Conta da Parte B	Texto	S	S	Descrição	Permite que o usuário informe a descrição da conta da Parte B.	MFS-15272		Data de Criação	Texto	S	S	DD/MM/AAAA	Permite que o usuário informe a data de criação da conta da parte b.

Tratamentos:

A data de criação da conta deve estar vigente no cadastro do grupo, caso contrário exibir a mensagem DW00165.


	MFS-15272		Data Limite	Texto	N	S	DD/MM/AAAA	Permite que o usuário informe/altera a data limite conta da parte b.

Tratamentos:

A data limite deve ser maior ou igual a data de criação da conta da Parte B, caso contrário exibir a mensagem  DW00164.

A data limite da conta deve estar vigente no cadastro do grupo, caso contrário exibir a mensagem DW00166.


	MFS-15272