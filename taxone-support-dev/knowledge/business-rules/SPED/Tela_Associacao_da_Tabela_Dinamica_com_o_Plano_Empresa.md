# Tela_Associacao_da_Tabela_Dinamica_com_o_Plano_Empresa 

> Fonte: Tela_Associacao_da_Tabela_Dinamica_com_o_Plano_Empresa .doc

THOMSON REUTERS

Tela Associação da Tabela Dinâmica com o Plano Empresa 
	ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		28/09/2017	MFS-12705	Criação do Documento	Alessandra Cristina Navatta		26/09/2018	MFS-20763	Mudar a validação da mensagem DW00050 do modal de informação complementar do centro de custo, para o modal de associar centro de custo (quadro de plano de contas da empresa). Não permitir inserir percentual de receita bruta, na conta contábil se existir um centro de custo vinculado a mesma.	Alessandra Cristina Navatta		01/10/2018	MFS-21398	Exclusão da data inicial e final da associação das contas contábeis (na grid do Plano de Contas da Empresa e no modal Adicionar Informação Complementar)	Alessandra Cristina Navatta		

Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc497322437" 1.	INTRODUÇÃO	 PAGEREF _Toc497322437 \h 3
 HYPERLINK \l "_Toc497322438" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc497322438 \h 3
 HYPERLINK \l "_Toc497322439" 3.	TELAS	 PAGEREF _Toc497322439 \h 3
 HYPERLINK \l "_Toc497322440" 3.1.	Pesquisa de Registros	 PAGEREF _Toc497322440 \h 3
 HYPERLINK \l "_Toc497322441" 3.2.	Regras dos Campos Tela Principal	 PAGEREF _Toc497322441 \h 4
 HYPERLINK \l "_Toc497322442" 3.3.	Modais	 PAGEREF _Toc497322442 \h 11


	


INTRODUÇÃO

Objetivo desta especificação é documentar a tela de associação da tabela dinâmica com o plano empresa.

DOCUMENTOS DE REFERÊNCIA


Mensagens_Sistema_DWECF.xlsx

Regras_Gerais_DWECF.docx


TELAS

Pesquisa de Registros 

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Parâmetros >> Mapeamento >> Associação da Tabela Dinâmica com o Plano Empresa


Campo	Tipo	Regra		Código 	Lista	Exibe as associações (pelo código)


		Descrição	Descrição	Exibe as descrições das associações

		Data Inicial	DD/MM/AAAA	O usuário poderá informar a data inicial da Associação.		Versão	Código - Descrição	Aplicar a RNG00004 (Versão de Layout)		

Regras dos Campos Tela Principal


Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Parâmetros >> Mapeamento >> Associação da Tabela Dinâmica com o Plano Empresa


Regra Geral: Nesta tela poderá incluir, editar, consultar e excluir um registro.


Campo	Tipo	Obrig.	Edit.	Formato / Default	Regra	MFS		 Excluir	Botão	-	-	 	Permite excluir toda a associação.Tratamentos:- Só será possível excluir uma associação se ela não estiver vinculada a nenhuma Informação ECF. Caso esteja vinculada, não permitir a exclusão e exibir a mensagem DW00043.	MFS-12705		Cabeçalho da Tela (*)Título: Associação da Tabela Dinâmica com o Plano Empresa
	 	 	 	 	 	 		Data Inicial	Data	S	S	DD/MM/AAAA	Na inclusão de registro, se houver mudança de informação no campo Data Inicial, limpar todas as informações dos campos.-Se não for encontrada nenhuma versão de tabela dinâmica vigente na data inicial da parametrização, exibir a mensagem DW00005.	MFS-12705		Código	Texto	S	S	 	-Informar o código da associação.	MFS-12705		Descrição	Texto	S	S	 	-Informar a descrição da associação.	MFS-12705		Grupo	Lista	S	S	Código -Descrição	-Se não for encontrado nenhum grupo de estabelecimento  vigente na data inicial da parametrização, exibir a mensagem DW00046 e não abrir a tela de grupo.-Na inclusão de registro, se for alterado o grupo, o cabeçalho seguirá com os mesmos dados cadastrados. 	MFS-12705		Versão	Lista	S	S	Código -Descrição	-Recuperar a versão vigente (da TFIX87) que está compreendida na data inicial da parametrização.-Na inclusão de registro, se for alterado a versão da tabela dinâmica, o cabeçalho seguirá com os mesmos dados cadastrados anteriormente. O campo Registro será limpo, se preenchido.	MFS-12705		Componte(*) Título: Tabela Dinâmica
	 		 		 		(*) Recuperação dos Registros e Demais Validações	 	 	 	 	Recuperação de Registros:-Considerando a Data Inicial da parametrização, a  Versão informada e o Registro selecionado, recuperar os registros vigentes da tabela TFIX89.-Recuperar as linhas cujo tipo for diferente de "R" e "CNA".-Recuperar as linhas cujo campo lançamento for diferente de "P" ou "L" de acordo com as condições da RNG00001. -Considerar as linhas da tabela dinâmica com Data Final nula ou >= Data Inicial da parametrização.Alteração de Linha da Tabela Dinâmica:Ao mudar a seleção da linha de tabela dinâmica, exibir a mensagem DW00012.Se o usuário selecionar a opção 'Sim', as alterações serão desprezadas. Se 'Não', manter as informações e não mudar de linha da tabela dinâmica.	MFS-12705		Registro	Lista	S	S	ListaCódigo do Registro -Descrição do RegistroExemplo: L210 - Informativo da Composição de Custos)	-Recuperar as informações do código e descrição de registro da tabela dinâmica (TFIX88). Ao selecionar um registro, carregar as informações na Grid de Tabela Dinâmica.-Na inclusão de registro, se for alterado o campo Código do Registro, o cabeçalho seguirá com os mesmos dados cadastrados anteriormente.	MFS-12705		Mostrar Apenas com Associações	Check-box	S	S	Desmarcado	Permite visualização das linhas que possuem associação com plano de contas da empresa.Tratamento:Exibir apenas os registros que possuam quantidade diferente de zero no campo Associação de Contas Contábeis.	MFS-12705		Ícone Pesquisar	Botão	-	-	Apresentar  tooltip	Permite pesquisar as linhas da tabela dinâmica (do registro selecionado), utilizando como filtro os campos: Código e Descrição.- Apresentar como tooltip o texto 'Pesquisar'	MFS-12705		Ícone Remover Associação	Botão	-	 	Apresentar  tooltip	Este botão só é habilitado se uma linha da tabela dinâmica for selecionada. Permite remover toda a associação feita nesta linha (exclusão das contas contábeis e centros de custos).- Apresentar como tooltip o texto 'Remover Associação'.	MFS-12705		 Ícone Associar Conta Empresa	Botão	-	-	Apresentar  tooltip	Permite associar uma ou mais conta contábil à linha da tabela dinâmica selecionada. Abre o modal "Associar Conta Empresa".- Apresentar como tooltip o texto 'Associar Conta Empresa'.	MFS-12705		Exibição da GRID de Tabela Dinâmica (*)
	 	 	 	 	 	 		Linha	Texto	S	N	Codigo -Descrição	Apresenta o código e a descrição da linha da tabela dinâmica (TFIX89).Exemplo: 1 - Valor da base de cálculo do IRPJ	MFS-12705		Tipo	Texto	S	N	Codigo -Descrição	Apresenta o tipo da linha da tabela dinâmica. TFIX89Apresentar o Código - Descrição, conforme RNG00002.Exemplo: E – Editável	MFS-12705		Associação de Contas Contábeis	Texto	S	N	XXX	Apresenta a quantidade das contas contábeis que estão associados na linha da tabela dinâmica.Exemplo: 100	MFS-12705		Componte(*) Título: Plano de Contas da Empresa 
 
 		Marcar Todos	Check-box	S	S	Desmarcado	Permite selecionar todos os registros da grid. Funcionalidades que podem se valer desta opção são: Remover Associação e Associar Informação Complementar.	MFS-12705		Mostrar Apenas com Associações	Check-box	S	S	Desmarcado	Permite visualização das contas contábeis que possuem associação com centro de custo.Tratamento:Exibir apenas os registros que possuam quantidade diferente de zero no campo Associação de Centro de Custo.	MFS-12705		Ícone Pesquisar	Botão	-	-	Apresentar  tooltip	Permite pesquisar as contas contábeis, utilizando como filtro os campos: Código, Descrição e Natureza.- Apresentar como tooltip o texto 'Pesquisar'.	MFS-12705		Ícone Remover Associação	Botão	-	-	Apresentar  tooltip	Este botão só é habilitado se uma conta contábil for selecionada. Permite remover a conta contábil vinculada na linha da tabela dinâmica. Caso a conta contenha um ou mais centro de custo, este(s) será(ão) removido(s).- Apresentar como tooltip o texto 'Remover Associação'.	MFS-12705		Ícone Associar Centro de Custo	Botão	-	-	Apresentar  tooltip	Permite adicionar na conta contábil selecionada um ou mais centro de custo. Abre modal " HYPERLINK  \l "ModalAssociarCentrodeCusto" Associar Centro de Custo".- Apresentar como tooltip o texto 'Associar Centro de Custo'.	MFS-12705		Ícone Adicionar Informação Complementar	Botão	-	-	Apresentar  tooltip	Este botão só é habilitado se existir pelo menos uma conta contábil adicionada na grid. Abre modal " HYPERLINK  \l "ModalAdicionarInformaçãoComplementarnaCo" Adicionar Informação Complementar ".- Apresentar como tooltip o texto 'Adicionar Informação Complementar na Conta da Empresa'	MFS-12705		Exibição da GRID de Plano de Contas da Empresa (*)
	 	 		Check-Box	 	 	 	Default Desmarcado	Permite selecionar uma ou mais contas contábeis.	MFS-12705		Contas da Empresa	Texto	S	N	Codigo -Descrição	Apresenta o código e a descrição da conta contábil (SAFX2002).	MFS-12705		Natureza	Texto	S	N	Codigo -Descrição	Apresenta a natureza da conta contábil (SAFX2002).	MFS-12705		Data Inicial	Texto	S	N	DD/MM/AAAA	Apresenta a data informada.	MFS-12705		Data Final	Texto	S	N	DD/MM/AAAA	Apresenta a data informada.	MFS-12705		Associação de Centro de Custo	Texto	S	N	XXX	Apresenta a quantidade dos centros de custos que estão associados na conta contábil.Exemplo: 100	MFS-12705		Componte(*) Título: Centro de Custo
  	 		Marcar Todos	Check-box	S	S	Desmarcado	Permite selecionar todos os registros da grid. Funcionalidade que pode se valer desta opção é a Remover Associação.	MFS-12705		Ícone Pesquisar 	Botão	-	-	-	Permite pesquisar os centros de custos, podendo utilizar como filtro os campos: Código e Descrição.- Apresentar como tooltip o texto 'Pesquisar'.	MFS-12705		Ícone Remover Associação	Botão	-	-	-	Este botão só é habilitado se um centro de custo for selecionado.Permite remover um centro de custo  vinculados na conta contábil.- Apresentar como tooltip o texto 'Remover Associação'.	MFS-12705		Ícone Adicionar Informação Complementar	Botão	-	 	Apresentar  tooltip	Permite que o usuário associe os percentuais para o cálculo da receita bruta para a linha 2 dos registros N500 e N650.Tratamentos:Este botão só é habilitado se for selecionado a linha 2 dos registros N500 e N650 . Se selecionado, abre modal " HYPERLINK  \l "ModalAdicionarInformaçãoComplementarnoCe" Adicionar Informação Complementar".- Apresentar como tooltip o texto 'Adicionar Informação Complementar no Centro de Custo'.	MFS-12705		Exibição da GRID de Centro de Custo (*)
 	 		Check-Box	 	 	 	Default Desmarcado	Permite selecionar um ou mais centro de custo.	MFS-12705		Centro de Custo	Texto	S	N	Código -Descrição	Apresenta o código e a descrição do centro de custo (SAFX2003)	MFS-12705		

Modais

Modal (*)Título:  Associar Contas da Empresa	 	 	 	 	 	 		(*) Recuperação dos Registros e Demais Validações	 	 	 	 	Recuperação de Registros:Considerar os registros vigentes da tabela de contas contábeis  (SAFX2002) de acordo com o Grupo de Estabelecimento informado na tela cuja as contas seja do tipo analítica.Considerar as Contas Contábeis de tipo Analítica.Se existir mais de um registro considerar o registro de maior validade sendo igual ou anterior a Data Inicial da parametrização.Se o Registro selecionado (campo Registros) for igual à (M300A, M300B, M300C, M350A, M350B  ou M350C): Somente devem ser listadas contas contábeis com natureza igual à (1, 2, 3, 4, 7 ou 8).Alteração de Conta Contábil:Ao mudar a seleção da conta contábil, exibir a mensagem DW00007.	MFS-12705		Check-Box	 	 	 	Default Desmarcado	Permite selecionar o registro para ser associado à linha da tabela dinâmica.	MFS-12705		Código	Texto	N	S	 	Permite filtrar as contas contábeis pelo código.	MFS-12705		Descrição	Texto	N	S	 	Permite filtrar as contas contábeis pela descrição.	MFS-12705		Natureza	Texto	N	S	 	Permite filtrar as contas contábeis pela natureza.	MFS-12705		OK	Botão		
Permite gravar as informações.

	MFS-12705		Cancelar	Botão		Cancela a operação.
	MFS-12705		Modal (*)Adicionar Informação Complementar na Conta da Empresa


Voltar  HYPERLINK  \l "ÍconeAdicionarInformaçãoComplementarPLEM" Ícone Adicionar Informação Complementar (Plano Empresa)	 	 	 	 	 	 		Data Inicial	Data	N	 	DD/MM/AAAA	A data inicial da vigência da conta, deve ser igual ou maior que a data inicial da parametrização. Caso contrário, exibir a mensagem DW00010.	MFS-12705		Data Final	Data	N	 	DD/MM/AAAA	A data final deve ser igual ou maior que a data inicial da vigência da conta contábil. Caso contrário, exibir a mensagem DW00010.Só permitir preencher este campo, se o campo data inicial da vigência da conta estiver preenchido.	MFS-12705		Percentual da Receita Bruta	Lista	S	S	Lista	Permite que o usuário selecione o percentual que será aplicado para o cálculo da receita bruta.Tratamentos:Valores Válidos:Para registro iniciado com N500:1,6%8%16%32%100%Para registro iniciado com N650:12%32%100%-Se em pelo menos uma conta for adicionado o percentual da receita bruta, todas as contas desta linha devem ter o percentual informado (diferente de nulo). Caso contrário, exibir a DW00013
- Se existir pelo menos um centro de custo for vinculado a conta contábil, este campo deve ficar desabilitado (não deve ser permitido indicar um percentual de receita bruta).	MFS-12705
MSF-13417 MFS-20763		Texto fixo (*)	Texto	S	N	-	Poderá ser incluído um Percentual de Receita Bruta para a linha 2 dos registros N500 e N650. Se uma conta contábil associada a esta linha utilizar o percentual, tal informação deve ser adicionada a todas as demais contas. Caso a conta possua detalhamento por centro de custo, o percentual deve ser informado por centro de custo, e o valor por conta, se informado, será descartado.	MFS-13670		OK	Botão		
Permite gravar as informações.

	MFS-12705		Cancelar	Botão		Cancela a operação.
	MFS-12705		Reset	Botão		Permite apagar as informações dos campos de data inicial, data final e percentual da receita bruta	MFS-12705		Modal (*)Título: Associar Centro de Custo


Voltar  HYPERLINK  \l "ÍconeAssociarCentrodeCustoPLEmpresa" Ícone Associar Centro de Custo (Plano de Contas da Empresa)

	 

	 	 	 	 	 		(*) Recuperação dos Registros e Demais Validações	 	 	 	 	Considerar os registros vigentes da tabela de centro de custo (SAFX2003) de acordo com o Grupo de Estabelecimento informado na tela.Se existir mais de um registro considerar o registro de maior validade sendo igual ou anterior a Data Inicial da parametrização.

	MFS-12705		Check-Box	 	 	 	Default Desmarcado	Permite selecionar o registro para ser associado à conta contábil.	MFS-12705		Código	Texto	N	S	 	Permite filtrar os centros de custos pelo código.	MFS-12705		Descrição	Texto	N	S	 	Permite filtrar os centros de custos pela descrição.	MFS-12705		OK	Botão		
Permite gravar as informações.

Tratamento:

-Ao incluir um centro de custo, se foi informado o percentual na conta contábil (que este centro de custo está vinculado), o sistema deve apagar o percentual atribuído a conta e exibir a mensagem DW00050.

	MFS-12705
MFS-20763		Cancelar	Botão		Cancela a operação.
	MFS-12705		Modal (*)
Adicionar Informação Complementar no Centro de Custo


Voltar  HYPERLINK  \l "ÍconeAdicionarInformaçãoComplementarCent" Ícone Adicionar Informação Complementar	 	 	 	 	 	 		Percentual da Receita Bruta	Lista	S	S	Lista	Permite que o usuário selecione o percentual que será aplicado para o cálculo da receita bruta.Tratamentos:Valores Válidos:Para registro iniciado com N500:1,6%8%16%32%100%Para registro iniciado com N650:12%32%100%-Se for inserido todos os percentuais a uma conta contábil que possui mais de um centro de custo e esses centros de custos forem todos excluídos, apagar a informação dos percentuais e exibir a mensagem DW00052.	MFS-12705/MSF-13417		Texto fixo (*)	Texto	S	N	-	Poderá ser incluído um Percentual de Receita Bruta para a linha 2 dos registros N500 e N650. Se uma conta contábil associada a esta linha utilizar o percentual, tal informação deve ser adicionada a todas as demais contas. Caso a conta possua detalhamento por centro de custo, o percentual deve ser informado por centro de custo, e o valor por conta, se informado, será descartado.	MFS-13670		OK	Botão		
Permite gravar as informações.

	MFS-12705		Cancelar	Botão		Cancela a operação.
	MFS-12705		Reset	Botão		Permite apagar as informações dos campos de data inicial, data final e percentual da receita bruta	MFS-12705