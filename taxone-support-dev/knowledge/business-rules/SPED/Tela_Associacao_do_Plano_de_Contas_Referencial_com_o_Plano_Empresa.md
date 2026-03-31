# Tela_Associacao_do_Plano_de_Contas_Referencial_com_o_Plano_ Empresa

> Fonte: Tela_Associacao_do_Plano_de_Contas_Referencial_com_o_Plano_ Empresa.doc

THOMSON REUTERS

Tela Associação do Plano de Contas Referencial com o Plano Empresa 
	ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		15/09/2017	MFS-12706	Criação do Documento	Alessandra Cristina Navatta		01/10/2018	MFS-21397	Exclusão da data inicial e final da associação das contas contábeis (na grid do Plano de Contas da Empresa e no modal Adicionar Informação Complementar)	Alessandra Cristina Navatta		

Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc497322460" 1.	INTRODUÇÃO	 PAGEREF _Toc497322460 \h 3
 HYPERLINK \l "_Toc497322461" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc497322461 \h 3
 HYPERLINK \l "_Toc497322462" 3.	TELAS	 PAGEREF _Toc497322462 \h 3
 HYPERLINK \l "_Toc497322463" 3.1.	Pesquisa de Registros	 PAGEREF _Toc497322463 \h 3
 HYPERLINK \l "_Toc497322464" 3.2.	Regras dos Campos Tela Principal	 PAGEREF _Toc497322464 \h 4
 HYPERLINK \l "_Toc497322465" 3.3.	Modais	 PAGEREF _Toc497322465 \h 13


	


INTRODUÇÃO

Objetivo desta especificação é documentar a tela de associação do plano de contas referencial com o plano empresa.

DOCUMENTOS DE REFERÊNCIA


Mensagens_Sistema_DWECF.xlsx

Regras_Gerais_DWECF.docx


TELAS

Pesquisa de Registros 

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Parâmetros >> Mapeamento >> Associação do Plano de Contas Referencial com o Plano Empresa


Campo	Tipo	Regra		Código 	Lista	Exibe as associações (pelo código)


		Descrição	Descrição	Exibe as descrições das associações

		Data Inicial	DD/MM/AAAA	O usuário poderá informar a data inicial da Associação.		Versão	Código - Descrição	Aplicar a RNG00004 (Versão de Layout)		

Regras dos Campos Tela Principal


Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Parâmetros >> Mapeamento >> Associação do Plano de Contas Referencial com o Plano Empresa


Regra Geral: Nesta tela poderá incluir, editar, consultar e excluir um registro.


Campo	Tipo	Obrig.	Edit.	Formato / Default	Regra	MFS		 Excluir	Botão	-	-	 	Permite excluir toda a associação.Tratamentos:- Só será possível excluir uma associação se ela não estiver vinculada a nenhuma Informação ECF. Caso esteja vinculada, não permitir a exclusão e exibir a mensagem DW00043.	MFS-12706		Cabeçalho da Tela (*)Título: Associação do Plano Referencial com o Plano Empresa	 	 	 	 	 	 		Data Inicial	Data	S	S	DD/MM/AAAA	-Na inclusão de registro, se houver mudança de informação no campo Data Inicial, limpar todas as informações dos campos.-Se não for encontrada nenhuma versão de tabela referencial vigente na data inicial da parametrização, exibir a mensagem DW00005.	MFS-12706		Código	Texto	S	S	 	-Informar o código da associação.	MFS-12706		Descrição	Texto	S	S	 	-Informar a descrição da associação.	MFS-12706		Grupo	Lista	S	S	Código -Descrição	-Se não for encontrado nenhum grupo de estabelecimento  vigente na data inicial da parametrização, exibir a mensagem DW00046 e não abrir a tela de grupo.-Na inclusão de registro, se for alterado o grupo, o cabeçalho seguirá com os mesmos dados cadastrados. 	MFS-12706		Versão	Lista	S	S	Código -Descrição	-Recuperar a versão vigente (da TFIX90) que está compreendida na data inicial da parametrização.-Na inclusão de registro, se for alterado a versão da tabela referencial, o cabeçalho seguirá com os mesmos dados cadastrados anteriormente. O campo Registro será limpo, se preenchido.	MFS-12706		Componte(*) Título: Plano de Contas Referencial	 		 		 		(*) Recuperação dos Registros e Demais Validações	 	 	 	 	Recuperação de Registros:Considerando a Data Inicial da parametrização, a  Versão informada e o Registro selecionado, recuperar as contas referenciais vigentes ( da TFIX92), cuja as contas seja do tipo analítica.Considerar as Contas Referenciais com Data Final nula ou >= Data Inicial da parametrização.	MFS-12706		Registro	Lista	S	S	ListaCódigo do Registro -Descrição do Registro(Ex: U150A - Balanço Patrimonial)	-Recuperar as informações do código e descrição de registro da tabela de plano referencial (TFIX91). Ao selecionar um registro, carregar as informações na Grid de Plano de Contas Referenciais.-Na inclusão de registro, se for alterado o campo Código do Registro, o cabeçalho seguirá com os mesmos dados cadastrados anteriormente.	MFS-12706		Mostrar Apenas com Associações	Check-box	S	S	Desmarcado	Permite visualização das contas referencias que possuem associação com plano de contas da empresa.Tratamento:Exibir apenas os registros que possuam quantidade diferente de zero no campo Associação de Contas Contábeis.	MFS-12706		Ícone Pesquisar	Botão	-	-	Apresentar  tooltip	Permite pesquisar as contas referenciais (dentro do range de contas do registro selecionado), utilizando como filtro os campos: Código, Descrição e  Natureza.- Apresentar como tooltip o texto 'Pesquisar'.- Este botão de ação, poderá ser acionado também com o botão direito do mouse.	MFS-12706		Ícone Associar Conta Empresa	Botão	-	-	Apresentar  tooltip	Permite associar uma ou mais conta contábil à conta referencial selecionada. Abre o modal " HYPERLINK  \l "ModalAssociarConta" Associar Contas da Empresa".- Apresentar como tooltip o texto 'Associar Conta Empresa'.- Este botão de ação poderá ser acionado também com o botão direito do mouse.	MFS-12706		Ícone Remover Associação	Botão	-	-	Apresentar  tooltip	 Permite remover toda a associação feita nesta conta referencial (exclusão das contas contábeis e centros de custos). Se não for encontrada nenhuma associação, exibir a mensagem DW00042.- Apresentar como tooltip o texto 'Remover Associação'.- Este botão de ação poderá ser acionado também com o botão direito do mouse.- Só será permitida a exclusão de uma associação de conta referencial por vez.	MFS-12706		Exibição da GRID de Plano de Contas Referencial (*)	 	 	 	 	 	 		Contas Referenciais	Texto	S	N	Codigo -Descrição	Apresenta o código e a descrição da conta referencial (TFIX92).Exemplo: 1 - ATIVOTratamento:Ao selecionar um registro é possível associar uma conta contábil, na conta referencial. Esta ação é permitida usando o botão  na barra de ação, ou com o botão direito do mouse ("Associar Conta Empresa")	MFS-12706		Natureza	Texto	S	N	Codigo -Descrição	Apresenta a natureza da conta referencial. TFIX92Exemplo: 1 - ATIVO	MFS-12706		Associação de Contas Contábeis	Texto	S	N	XXX	Apresenta a quantidade das contas contábeis que estão associados na conta referencial.Exemplo: 100	MFS-12706		Componte(*) Título: Plano de Contas da Empresa 
 
 		Marcar Todos	Check-box	S	S	Desmarcado	Permite selecionar todos os registros da grid. Funcionalidades que podem se valer desta opção são: Remover Associação e Associar Informação Complementar.	MFS-12706		Mostrar Apenas com Associações	Check-box	S	S	Desmarcado	Permite visualização das contascontábeis que possuem associação com centro de custo.Tratamento:Exibir apenas os registros que possuam quantidade diferente de zero no campo Associação de Centro de Custo.	MFS-12706		Ícone Pesquisar	Botão	-	-	Apresentar  tooltip	Permite pesquisar as contas contábeis, utilizando como filtro os campos: Código, Descrição e Natureza.- Apresentar como tooltip o texto 'Pesquisar'.- Este botão de ação poderá ser acionado também com o botão direito do mouse.-Só será aberto o modal de "Pesquisa do Plano de Contas Empresa", se existir pelo menos uma conta contábil no componente de Plano de Contas Empresa.	MFS-12706		Ícone Associar Centro de Custo	Botão	-	-	Apresentar  tooltip	Permite adicionar na conta contábil selecionada um ou mais centro de custo. Abre modal " HYPERLINK  \l "ModalAssociarCentro" Associar Centro de Custo".- Apresentar como tooltip o texto 'Associar Centro de Custo'.- Este botão de ação poderá ser acionado também com o botão direito do mouse.	MFS-12706		Ícone Remover Associação	Botão	-	-	Apresentar  tooltip	Permite remover a conta contábil vinculada na conta referencial. Caso a conta contenha um ou mais centro de custo, este(s) será(ão) removido(s). Se não for selecionado nenhuma conta contábil, apresentar a mensagem DW00041.- Apresentar como tooltip o texto 'Remover Associação'.- Este botão de ação, poderá ser acionado também com o botão direito do mouse.-Será possível excluir uma associação de conta contábil, selecionando o registro (usando o check-box ou apenas marcando-o). Para remover a associação de mais de uma conta contábil, utilizar obrigatoriamente o check-box.	MFS-12706		Ícone Adicionar Informação Complementar	Botão	-	-	Apresentar  tooltip	 Abre modal " HYPERLINK  \l "ModalAdicionarInf" Adicionar Informação Complementar".- Apresentar como tooltip o texto 'Adicionar Informação Complementar'.- Este botão de ação, poderá ser acionado também com o botão direito do mouse.	MFS-12706		Exibição da GRID de Plano de Contas da Empresa (*)		Check-Box	-	 	 	Default Desmarcado	Permite selecionar uma ou mais conta(s) contábil(eis) para ser(em) removida(s) da associação. 	MFS-12706		Contas da Empresa	Texto	S	N	Codigo -Descrição	Apresenta o código e a descrição da conta contábil (SAFX2002).Tratamento:Ao selecionar um registro é possível associar um centro de custo, na conta contábil. Esta ação é permitida usando o botão  na barra de ação, ou com o botão direito do mouse ("Associar Centro de Custo")	MFS-12706		Natureza	Texto	S	N	Codigo -Descrição	Apresenta a natureza da conta contábil (SAFX2002).	MFS-12706		Data Inicial	Texto	S	N	DD/MM/AAAA	Apresenta a data informada.	MFS-12706		Data Final	Texto	S	N	DD/MM/AAAA	Apresenta a data informada.	MFS-12706		Associação de Centro de Custo	Texto	S	N	XXX	Apresenta a quantidade dos centros de custos que estão associados na conta contábil.Exemplo: 100	MFS-12706		Componte(*) Título: Centro de Custo	 	 	 	 	 	 		Marcar Todos	Check-box	S	S	Desmarcado	Permite selecionar todos os registros da grid. Funcionalidade que pode se valer desta opção é a Remover Associação.	MFS-12706		Ícone Pesquisar 	Botão	-	-	 	Permite pesquisar os centros de custos, podendo utilizar como filtro os campos: Código e Descrição.- Apresentar como tooltip o texto 'Pesquisar'.- Este botão de ação, poderá ser acionado também com o botão direito do mouse.	MFS-12706		Ícone Remover Associação	Botão	-	-	 	.Permite remover um centro de custo  vinculados na conta contábil. Se não for selecionado nenhum centro de custo, apresentar a mensagem DW00041.- Apresentar como tooltip o texto 'Remover Associação'.- Este botão de ação, poderá ser acionado também com o botão direito do mouse.-Será possível excluir uma associação de centro de custo, selecionando o registro (usando o check-box ou apenas marcando-o). Para remover a associação de mais de um centro de custo, utilizar obrigatoriamente o check-box.	MFS-12706		Exibição da GRID de Centro de Custo (*)	 	 	 	 	 	 		Check-Box	-	 	 	Default Desmarcado	Permite selecionar um ou mais centro de custo, para ser(em)  removido(s) da associação.	MFS-12706		Centro de Custo	Texto	S	N	Código -Descrição	Apresenta o código e a descrição do centro de custo (SAFX2003)	MFS-12706		

Modais

Modal (*)Título:  Associar Contas da Empresa


Voltar  HYPERLINK  \l "ÍconeAssociarContaEmpresa" Ícone Associar Conta Empresa	 

	 	 	 	 	 		(*) Recuperação dos Registros e Demais Validações	 	 	 	 	Recuperação de Registros:Considerar os registros vigentes da tabela de contas contábeis  (SAFX2002) de acordo com o Grupo de Estabelecimento informado na tela cuja as contas seja do tipo analítica.Considerar as Contas Contábeis de tipo Analítica.Se existir mais de um registro considerar o registro de maior validade sendo igual ou anterior a Data Inicial da parametrização.- Se o Registro selecionado no campo Registros possuir Códigos de Natureza iguais  a “01 - Ativo”, “02 - Passivo” ou “03 - Patrimônio Líquido” na tabela de plano referencial, recuperar apenas as  contas contábeis  que possuem códigos de natureza (da tabela de plano de contas) igual a “1 - Ativo”, “2 - Passivo” ou “7 - Patrimônio Líquido”.- Se o Registro selecionado no campo Registros, possuir  Código de Natureza igual a “04 - Resultado”, na tabela de plano referencial, recuperar apenas as contas contábeis que possuem códigos de natureza (da tabela de plano de contas) igual a “3 - Despesa”, “4 - Receita” ou “8 - Custo”.Alteração de Conta Contábil:Ao mudar a seleção da conta contábil, exibir a mensagem DW00007.	MFS-12706		Código	Texto	N	S	 	Permite filtrar as contas contábeis pelo código.	MFS-12706		Descrição	Texto	N	S	 	Permite filtrar as contas contábeis pela descrição.	MFS-12706		Natureza	Texto	N	S	 	Permite filtrar as contas contábeis pela natureza.	MFS-12706		OK	Botão		
Permite gravar as informações.

	MFS-12706		Cancelar	Botão		Cancela a operação.
	MFS-12706		Modal (*)Título: Associar Centro de Custo

Voltar  HYPERLINK  \l "ÍconeAssociarCentrodeCusto" Ícone Associar Centro de Custo	 	 	 	 	 	 		(*) Recuperação dos Registros e Demais Validações	 	 	 	 	Considerar os registros vigentes da tabela de centro de custo (SAFX2003) de acordo com o Grupo de Estabelecimento informado na tela.Se existir mais de um registro considerar o registro de maior validade sendo igual ou anterior a Data Inicial da parametrização.	MFS-12706		Código	 	N	S	 	Permite filtrar os centros de custos pelo código.	MFS-12706		Descrição	 	N	S	 	Permite filtrar os centros de custos pela descrição.	MFS-12706		OK	Botão		
Permite gravar as informações.

	MFS-12706		Cancelar	Botão		Cancela a operação.
	MFS-12706		Modal (*)Título: Adicionar Informação Complementar

Voltar  HYPERLINK  \l "ÍconeAdicionaInformaçãoComplementar" Ícone Adicionar Informação Complementar	 	 	 	 	 	 		Data Inicial	Data	N	S	DD/MM/AAAA	A data inicial da vigência da conta,  deve ser igual ou maior que a data inicial da parametrização. Caso contrário, exibir a mensagem DW00010.	MFS-12706		Data Final	Data	N	S	DD/MM/AAAA	A data final deve ser igual ou maior que a data inicial da vigência da conta contábil. Caso contrário, exibir a mensagem DW00010.-Só permitir preencher este campo, se o campo data inicial da vigência da conta estiver preenchido.	MFS-12706		OK	Botão		
Permite gravar as informações.

	MFS-12706		Cancelar	Botão		Cancela a operação.
	MFS-12706