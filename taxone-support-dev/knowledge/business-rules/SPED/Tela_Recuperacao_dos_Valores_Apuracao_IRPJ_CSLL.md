# Tela_Recuperacao_dos_Valores Apuracao_IRPJ_CSLL

> Fonte: Tela_Recuperacao_dos_Valores Apuracao_IRPJ_CSLL.doc

THOMSON REUTERS

Tela Recuperação dos Valores - Apuração IRPJ/CSLL

ECF - Escrituração Contábil Fiscal (DW)


Data	MFS	Descrição	Autor		14/11/2017	MFS-14674	Criação do documento	Alessandra Cristina Navatta 		

Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc498701052" 1.	INTRODUÇÃO	 PAGEREF _Toc498701052 \h 2
 HYPERLINK \l "_Toc498701053" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc498701053 \h 2
 HYPERLINK \l "_Toc498701054" 3.	TELA/MODAIS	 PAGEREF _Toc498701054 \h 2
 HYPERLINK \l "_Toc498701055" 3.1 Pesquisa de Registros	 PAGEREF _Toc498701055 \h 2
 HYPERLINK \l "_Toc498701056" 3.2	Regras dos Campos Tela Principal	 PAGEREF _Toc498701056 \h 3
 HYPERLINK \l "_Toc498701057" 3.3	Modais	 PAGEREF _Toc498701057 \h 10
 HYPERLINK \l "_Toc498701058" 3.1.	Regras dos Campos	 PAGEREF _Toc498701058 \h 11


INTRODUÇÃO

O objetivo desta especificação é criar uma tela para parametrizar a Recuperação dos Valores – Apuração IRPJ/CSLL, com base nas opções: Saldo, Movimento, Total de Débito, Total de Crédito com o Plano Empresa.
DOCUMENTOS DE REFERÊNCIA

Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
MTZ_Processamento_em_Lote.docx
TELA/MODAIS

3.1 Pesquisa de Registros

Localização da tela: ECF - Escrituração Contábil Fiscal >>  Parâmetros >> Recuperação dos Valores – Apuração IRPJ/CSLL

Título da tela: Recuperação dos Valores – Apuração IRPJ/CSLL

Disponibilizar na tela de pesquisa e como coluna da grid de resultado os itens abaixo:

Campo	Tipo 	Regra		Código	Código	Permite a pesquisa pelo código das parametrizações.


		Descrição	Descrição	Permite a pesquisa pela descrição das parametrizações

		Cód. do Grupo 	Código	Permite a pesquisa pelo código dos grupos.


		Desc. do Grupo 	Descrição	Permite a pesquisa pela descrição dos grupos.

		Data Inicial	DD/MM/AAAA	Permite a pesquisa pela data inicial da parametrização.		


Regras dos Campos Tela Principal

Localização da tela: ECF - Escrituração Contábil Fiscal >>  Parâmetros >> Recuperação dos Valores – Apuração IRPJ/CSLL

Título da tela: Recuperação dos Valores – Apuração IRPJ/CSLL


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		DADOS GERAIS		Data Inicial	Data	S	S	-	Permite que o usuário visualize a data inicial da parametrização. 

Tratamento:

Quando acionada a tela através da opção editar, o sistema deve exibir o campo desabilitado e preenchido, com as informações recuperadas da base. Na adição, o campo ficará habilitado.
	MFS-14674		Código	Texto	S	S	 	Permite que o usuário informe o código da parametrização.	MFS-14674		Descrição	Texto	S	S	 	Permite que o usuário informe a descrição da parametrização.	MFS-14674		Grupo	LOV	S	S	Código -Descrição	Permite que o usuário informe o grupo que será utilizado na  parametrização (para recuperar as contas contábeis).

Tratamentos:

-Se não for encontrado nenhum grupo de estabelecimento vigente na data inicial da parametrização, exibir a mensagem DW00046 e não abrir a tela de grupo.-Na inclusão de registro, se for alterado o grupo, o cabeçalho seguirá com os mesmos dados cadastrados. 	MFS-14674		Exibir a orientação abaixo (*)

 
Para realizar uma parametrização, selecione a Cód da Conta Contábilatravés do botão 'Plano Empresa' e após a inserção do Cód. da Conta Contábil na Grid, selecione a Recuperação dos valores através do respectivo botão "PARAMETRIZAR.". Qualquer alteração realizada nessa tela só será salva ao clicar no botão “Salvar".		CONTAS CONTÁBEIS		Importar Ocorrências de um Arquivo	Botão	-	-	Habilitado	Permite que o usuário faça o upload de um arquivo txt, cujos valores serão atualizados na grid.

Tratamentos:

- Na inclusão, este campo deve ser habilitado após a seleção de um conteúdo no campo Central de Cadastro.

As regras de upload estão disponíveis no documento MTZ_Consistencias_Upload_Recuperação_Valores.doc		Associar Conta Empresa	LOV	-	-	Desabilitado	Com base no grupo informado na tela, permite que o usuário informe/visualize o Código e a Descrição da Conta Contábil das Contas Analíticas, somente para os Indicadores da Natureza do tipo (Ativo, Passivo, Patrimônio Liquido, Despesa, Receita e Custo) previamente cadastradas na tabela de conta contábil. 

Tratamentos:

 - Não permitir associar contas de Naturezas:
– Compensação, 
5–Mutações Ativas, 
6 – Mutações Passivas e 
9 – Outros.

- Na inclusão, este campo deve ser habilitado após a seleção de um conteúdo no campo Grupo.

Apresentar os conteúdos, conforme descrito abaixo enquanto:

- Recuperar o registro de máxima validade.

Campos de Pesquisa: Código, Descrição, Indicador da Natureza e Data. 	MFS-14674		Pesquisar	Botão		Permite o usuário selecionar as informações que estão na grid das Contas Contábeis.

Tratamentos:

A pesquisa pode ser realizada pelos campos : Cód. da Conta Contábil, Desc. Da Conta Contábil, Indicador da Natureza, Recuperação dos Valores e Lançamento A/E	MFS-14674		Adicionar Informação Complementar	Botão	--	-	Desabilitado	Permite que o usuário efetue a parametrização da Recuperação de Valores,

Tratamento:
Se o botão for acionado, e não houver nenhum item selecionado na Grid de resultados, exibir a mensagem DW00041.
Ao acionar o botão, deve ser exibido o  HYPERLINK  \l "ModalParametrizarRecup" modal – “Parametrizar Recuperação dos Valores”.
Quando for selecionado mais de um item para edição na grid e o Indicador de Natureza das contas selecionas forem de (Ativo, Passivo, Patrimônio Líquido ou Outros) e também de (Despesa, Receita ou Custo) exibir a mensagem DW00132.

	MFS-14674		Remover	Botão	-	-	-	Permite que o usuário remova da grid as contas exibidas

Tratamento:

Ao ser acionado o botão, verificar se pelo menos um item na Grid de resultados está selecionado, caso contrário exibir a DW00041.


Ao selecionar o botão, caso pelo menos um registro da grid for selecionado,  o usuário deve receber uma mensagem de confirmação padrão do sistema e se o usuário confirmar, mostrar a mensagem do sistema de Registro Excluído com Sucesso. Caso o usuário selecione ‘Não’, o registro não deve ser excluído.

	MFS-14674		(*)Grid – Contas Contábeis		(*) Checkbox –selecionar todos	Botão	-	-	Não selecionado	Permite que o usuário selecione/desmarcar todos os registros da (*)Grid – Contas Contábeis	MFS-14674		(*) Checkbox	Botão	-	-	Não selecionado	Permite que o usuário selecione/desmarcar um registros da (*)Grid – Contas Contábeis	MFS-14674		Cód. da Conta Contábil	Exibição na Grid	-	-	-	
Tratamentos: 

Exibe o Cód. da Conta Contábil selecionada por meio do LOV.
	MFS-14674		Desc. da Conta Contábil	Exibição na Grid	-	-	-	Deve ser exibido todas as descrições corresponde a Conta Contábil Selecionada.	MFS-14674		Indicador da Natureza	Exibição na Grid	-	-	-	Permite que o usuário visualize o Indicador da Natureza parametrizada para cada Cód. da Central de Cadastro.

Tratamento:
Deve ser permitida a exibição, somente dos registros conforme os valores válidos abaixo, porém sem a exibição dos números, somente o texto, a numeração é o valor gravado no banco de dados:

Conteúdos Válidos:
Ativo
Passivo
Patrimônio Liquido
Despesa
Receita
Custo
Outros 
	MFS-14674		Recuperação dos Valores	Exibição na Grid	S	N	Saldo	Permite que o usuário visualize os valores da Recuperação dos Valores parametrizada para Conta Contábil por meio do modal “Parametrizar Recuperação dos Valores”.

Conteúdos Válidos:

Saldo
Movimento
Total de Débito
Total de Crédito
Lançamentos Contábeis

Tratamento:

Se o usuário não parametrizou este campo com outro valor válido, sempre carregar as contas contábeis na grid com o valor “Saldo”.
	MFS-14674		LANÇAMENTO A/E *(Lançamento de Adição e Exclusão)	Exibição na Grid	N	N	Não se Aplica (para as naturezas de patrimônio) 

Um lançamento (Consolidando o Saldo de todas as Contas)
(para as naturezas de resultado)	Permite que o usuário visualize os valores do Lançamento de Adição e Exclusão parametrizado para Conta Contábil por meio do modal “Parametrizar Recuperação dos Valores”.

Conteúdos Válidos:

Não se Aplica
Um lançamento (Consolidando o Movimento de todas as Contas)
Dois lançamentos (Movimento de Contas a Crédito na Adição e Movimento de Contas a Débito na Exclusão)
Dois Lançamentos (Total de Crédito de todas as Contas na Adição e Total de Débito de todas as Contas na Exclusão)
Associar Lançamentos Contábeis (Lançamentos a Crédito na Exclusão e Lançamentos a Débito na Adição)
Associar Lançamentos Contábeis (Um Lançamento Consolidando todos os Lançamentos Contábeis)
Um Lançamento (Consolidando o Saldo de todas as Contas)
Dois Lançamentos (Saldo de Contas a Débito na Adição e Saldo de Contas a Crédito na Exclusão)
Dois Lançamentos (Total de Débito de todas as Contas na Adição e Total de Crédito de todas as Contas na Exclusão)
Associar Lançamentos Contábeis (Lançamentos a Crédito na Adição e Lançamentos a Débito na Exclusão)
	MFS-14674		(*) Não exibir a descrição na tela.

Modais


Modal (*) – Parametrizar Recuperação dos Valores


Voltar para o  HYPERLINK  \l "BotãoParametrizar" botão Parametrizar		Recuperação dos Valores	Lista	S	S	Saldo	Permite que o usuário selecione a Recuperação dos Valores 

Conteúdos Válidos:

Ver RN001

Tratamento:

Quando for selecionado mais de um item para edição na grid, este campo deve ser carregado Vazio. 

Se selecionado apenas um item, exibir o item correspondente ao selecionado.
	MFS-14674		Lançamento de Adição e Exclusão	Lista	N	N	-	Permite que o usuário selecione se é Lançamento de Adição e Exclusão

Conteúdos Válidos:

Ver RN001

Tratamento:

Quando for selecionado mais de um item para edição na grid este campo deve ser carregado Vazio. 

Se selecionado apenas um item, exibir o item correspondente ao selecionado.
	MFS-14674		Parametrizar	Botão	-	-	-	Permite preencher as informações do campo Recuperação dos Valores e Lançamento de Adição e Exclusão


Tratamentos:
- Aplicar a RNG00012 - Salvar
- Aplicar a RNG00010 - Campo Obrigatório
- Aplicar a RNG00011 - Duplicidade de Registro

	MFS-14674		Cancelar	Botão	-	-	-	Permite cancelar a ação.

Fechar o modal.	MFS-14674		(*) Não exibir a descrição na tela.


Regras dos Campos


REGRA	DESCRIÇÃO		RN001	Parametrizar Recuperação dos Valores 

Os Parâmetros de Recuperação de Valores e Lançamento de Adição e Exclusão deve obedecer aos critérios da tabela abaixo:

Indicador da Natureza
Recuperação dos Valores
Lançamento de Adição e Exclusão

Patrimonial(Ativo, passivo, Patrimonio Líquido e Outros)
Saldo
Não se Aplica ou Nulo


Movimento
Não se Aplica ou Nulo


Um Lançamento (Consolidando o Movimento de todas as Contas)


Dois Lançamentos (Movimento de Contas a Crédito na Adição e Movimento de Contas a Débito na Exclusão)


Dois Lançamentos (Total de Crédito de todas as Contas na Adição e Total de Débito de todas as Contas na Exclusão)


Total de Crédito
Não se Aplica ou Nulo


Total de Débito
Não se Aplica ou Nulo


Lançamentos Contábeis

Não se Aplica 


Associar Lançamentos Contábeis (Lançamentos a Crédito na Adição e Lançamentos e Débito na Exclusão).

Associar Lançamentos Contábeis (Um Lançamento Consolidando todos os Lançamentos Contábeis).

Resultado(Despesa, Receita e Custo)
Saldo
Associar Lançamentos Contábeis (Lançamentos a Crédito na Exclusão e Lançamentos a Débito na Adição)


Associar Lançamentos Contábeis (Um Lançamento Consolidando todos os Lançamentos Contábeis)


Um Lançamento (Consolidando o Saldo de todas as Contas)


Dois Lançamentos (Saldo de Contas a Débito na Adição e Saldo de Contas a Crédito na Exclusão)


Dois Lançamentos (Total de Débito de todas as Contas na Adição e Total de Crédito de todas as Contas na Exclusão)


Lançamentos Contábeis
Não se Aplica ou Nulo


Associar Lançamentos Contábeis (Lançamentos a Crédito na Exclusão e Lançamentos a Débito na Adição)


Associar Lançamentos Contábeis (Um Lançamento Consolidando todos os Lançamentos Contábeis)


	MFS-14674