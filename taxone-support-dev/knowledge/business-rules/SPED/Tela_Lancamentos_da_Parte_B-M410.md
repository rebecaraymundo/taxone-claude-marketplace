# Tela_Lancamentos_da_Parte_B-M410

> Fonte: Tela_Lancamentos_da_Parte_B-M410.doc

THOMSON REUTERS

Tela Ajustes da ParteB
ECF - Escrituração Contábil Fiscal

DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		13/12/2017	MFS-15272	Criação do documento	Alessandra Cristina Navatta		17/01/2017	MFS-15678	Ajuste da tela considerando apenas a inclusão do ajuste de origem parte B (M410). Os lançamentos de origem parte A, serão visualizados na tela de demonstração do Bloco M.	Alessandra Cristina Navatta		20/03/2018	MFS-17180	Inclusão de filtro Status (no botão Abre) 	Alessandra Cristina Navatta		


	
Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc524341099" 1.	INTRODUÇÃO	 PAGEREF _Toc524341099 \h 3
 HYPERLINK \l "_Toc524341100" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc524341100 \h 3
 HYPERLINK \l "_Toc524341101" 3.	TELA/MODAIS	 PAGEREF _Toc524341101 \h 3
 HYPERLINK \l "_Toc524341102" 3.1 Pesquisa de Registros	 PAGEREF _Toc524341102 \h 3
 HYPERLINK \l "_Toc524341103" 3.2 Regras dos Campos Tela Principal	 PAGEREF _Toc524341103 \h 5
 HYPERLINK \l "_Toc524341104" 3.3 Modais	 PAGEREF _Toc524341104 \h 18


INTRODUÇÃO

Objetivo desta especificação é prover o detalhamento das informações relativas aos Ajustes da Parte B (apenas os ajustes de origem parte B).

 DOCUMENTOS DE REFERÊNCIA


Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
MTZ_Processamento_em_Lote.docx
Tela_Abertura_de_Apuracao.doc
Tela_Lancamentos_Parte_A.doc


TELA/MODAIS

3.1 Pesquisa de Registros

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Ajustes Manuais >> Lançamentos da Parte B (M410)

Título da tela: Lançamentos da Parte B (M410)

Condições Gerais: Recuperar apenas as aberturas com status diferente de “Apuração em Aberto” e A00.

Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.


Campo	Tipo	Regra		Estabelecimento 	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
(AAAA)
	O usuário poderá informar o exercício. 
		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código -Descrição)	Aplicar a RNG00004 - Versão de Layout		Forma de Tributação	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Lucro Real
- Lucro Presumido,
-Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 		Apuração	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral
		Período de Apuração	Lista 
(Código -Descrição)	Exibe as opções abaixo:
 
- Se Apuração = Anual:

Janeiro
Fevereiro
Março
Abril
Maio
Junho
Julho
Agosto
Setembro
Outubro
Novembro
Dezembro

- Se Apuração = Trimestral:

1º Trimestre
2º Trimestre
3º Trimestre
4º Trimestre

Caso o campo Apuração não for preenchido, exibir todas as opções.
		Status	Lista
(Código)	Exibe a lista de Status:

- Importação dos Saldos Realizada- Cálculo Realizado- Reapurar- Alteração Manual Realizada- Aguardando Alteração Manual

		
3.2 Regras dos Campos Tela Principal

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Ajustes Manuais >> Lançamentos da Parte B (M410)

Título da tela: Lançamentos da Parte B (M410)


Condições Gerais: 

Aplicar a regra de negócio geral <<RNG00016- Acesso à Tela >>
Desabilitar os botões “Novo” e “Excluir” na toolbar.

Permitir edição do registro apenas quando o status da abertura de apuração correspondente ao registro for diferente de “Aguardando Alteração Manual” e “Cálculo Realizado”. Caso contrário, aplicar a RNG00018 - Alteração de tela com controle de status da abertura da apuração

Os dados incluídos nesta tela deverão considerados como ajuste manual.

Aplicar RNG00010- Campo Obrigatório.

Após a edição dos valores nesta tela, o status deverá ser alterado para “Alteração Manual Realizada”.

Apresentar a Mensagem Explicativa, ao abrir a tela: "Ao efetuar qualquer alteração nesta tela, será necessário executar o cálculo no Processamento em Lote para a atualização dos registros A00 e para a geração de ajustes Incrementais e Contrapartida com os dados informados”.

As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Criar cópia
	Botão	S	S		Criar cópia

Permite que o usuário copie os Ajustes da Parte B (M010).

Tratamentos:
Aplicar a regra de negócio geral <<RNG00010>>.

Importante:
Devem ser copiados os parâmetros da tela Ajustes da Parte B (M010)

Exceção:
Limpar todos os campos da grid: Origem, Histórico, Data Lancto, Saldo Disponível, Ind. do Saldo Disponível, Valor, Ind. do Valor, Saldo Final, Ind. do Saldo Final 

Limpar os seguintes campos do cabeçalho: Lançamento da Parte A e Descrição do Lançamento.

Se o campo Tipo de Tributo for ‘Imposto de Renda Pessoa Jurídica’ alterar para ‘Contribuição Social sobre o Lucro Líquido’

Se o campo Tipo de Tributo for ‘Contribuição Social sobre o Lucro Líquido’, alterar para ‘Imposto de Renda Pessoa’
		
Cabeçalho (*)
		Estabelecimento 

	Texto	S	N	Tipo - Código – Descrição	Permite que o usuário visualize o Estabelecimento da apuração que foi recuperada 	MFS-15272		Exercício 	Texto	S	N	AAAA	Exibe o exercício da escrituração.
	MFS-15272		Data Inicial	Texto	S	N	DD/MM/AAAA	Exibe a Data Inicial da escrituração.
	MFS-15272		Versão	Texto	S	N		Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar RNG00004-Versão de Layout.	MFS-15272		Forma de Tributação	Texto	S	N	Descrição	Exibe a forma de tributação do registro selecionado.

Conteúdos Válidos:
- Lucro Real
- Lucro Presumido,
-Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 
	MFS-15272		Apuração	Texto	S	N	Descrição	Exibe a apuração do registro selecionado.

Conteúdos Válidos:
- Anual
- Trimestral
	MFS-15272		Período de Apuração	Texto	S	N	Descrição	Exibe o período de apuração do registro selecionado.

Conteúdos Válidos:

- Se Apuração = Anual:

Janeiro
Fevereiro
Março
Abril
Maio
Junho
Julho
Agosto
Setembro
Outubro
Novembro
Dezembro

- Se Apuração = Trimestral:

1º Trimestre
2º Trimestre
3º Trimestre
4º Trimestre

		Filtro da Conta da Parte B com Saldos na Escrituração		Grupo (Cód/Descr)	LOV	S	S	Código - Descrição	Permite que o usuário selecione/visualize o código e a descrição do grupo do cadastro que a conta da parte B foi cadastrada.

		Tributo	Lista	S	S	Descrição	Permite que o usuário selecione/visualize o tributo que o ajuste da parte b se refere,

Opções de Lista:

 -Imposto de Renda Pessoa Jurídica
-Contribuição Social sobre o Lucro Líquido

- Este campo deve permitir ser preenchido se o campo grupo estiver com informação.		
Conta da Parte B
	LOV	S	S	Código - Descrição	Permite que o usuário selecione/visualize o código e descrição da conta da parte B.


Recuperação das Contas:

Recuperar apenas as contas cuja data de criação e limite da conta esteja vigente no período da Escrituração recuperada, que estão no grupo com o tributo selecionado e que possuam saldo no período da escrituração
Só habilitar este campo, se o campo Grupo estiver preenchido.

	MFS-15272		Data de Criação da Conta	Texto
	S
	N
	DD/MM/AAAA
Desabilitado
	

Permite que o usuário visualize a data de criação da conta da parte B que foi selecionada.

	MFS-15272		Data Limite	Texto
	N
	N
	DD/MM/AAAA
Desabilitado
	Permite que o usuário visualize a data de limite da conta da parte B que foi selecionada.
	MFS-15272		Saldo Inicial da Escrituração	Texto	S	N	xxx.xxx,xx D ou 
xxx.xxx,xx C	Saldo Inicial da Escrituração

Permite que o usuário visualize o saldo inicial da escrituração da conta selecionada. Valor e indicador.

Tratamentos:


Quando for alterado o valor do campo (na tela de Saldos das Contas da Parte B), atualizar os valores do registro M500 (conforme RNG00044 - Cálculo do Registro M500).


	MFS-15272		REGISTRO M500 – CONTROLE DE SALDOS DAS CONTAS DO E-LALUR E DO E-LACS (PARTE B)
		Campos da GRID- Registro M500(*)		 SALDO INICIAL 	
Texto	
S	
N		Saldo Inicial

Exibir o saldo inicial do registro M500. 


Tratamentos:

Conforme RNG00044 - Cálculo do Registro M500
	MFS-15272		LANÇAMENTOS DA PARTE A	
Texto	
S	
N	
0,00, 0,00C ou 0,00D	Lançamentos da Parte A

Exibir o somatório dos lançamentos da parte A. 


Tratamentos:

Conforme RNG00044 - Cálculo do Registro M500	MFS-15272		
LANÇAMENTOS DA PARTE B	
Texto	
S	
N	
0,00, 0,00C ou 0,00D	Lançamentos da Parte B

Exibir o somatório dos lançamentos da parte B. 


Tratamentos:

Conforme RNG00044 - Cálculo do Registro M500	MFS-15272		LANÇAMENTOS DA PARTE B - CONTRAPARTIDA	Texto	S	N	0,00, 0,00C ou 0,00D	Lançamentos da Parte B - Contrapartida

Exibir o somatório dos lançamentos da parte B (contrapartida). 


Tratamentos:

Conforme RNG00044 - Cálculo do Registro M500	MFS-15272		SALDO FINAL	
Texto	
S	
N	
0,00, 0,00C ou 0,00D	Saldo Final

Exibir o valor do saldo final. 


Tratamentos:

Conforme RNG00044- Cálculo do Registro M500	MFS-15272		REGISTRO M410 – LANÇAMENTOS NA CONTA DA PARTE B DO E-LALUR E DO E-LACS SEM REFLEXO NA PARTE A 
		(Botões da Grid)*		Adicionar	Botão	-	-	Habilitado	Adicionar

Permite que o usuário acesse a tela de inclusão de um ajuste (modal Adicionar Lançamentos da Parte B). 

Tratamentos:


Ao ser acionado o botão “Adicionar” o sistema exibe o modal  HYPERLINK  \l "modaladicionarlancamentosparteb" “Adicionar Lançamentos da Parte B”.


	MFS-15272		Alterar	Botão	-	-	habilitado	Alterar

Permite que o usuário acesse a tela de Alteração.

Tratamentos:
Este botão só deve ser apresentado se algum registro na grid do registro M410 for selecionado

Ao ser acionado o botão “Alterar” o sistema exibe o modal “ HYPERLINK  \l "modaladicionarlancamentosparteb" Alterar Lançamentos da Parte B”.

Apenas ajustes de origem = ‘Parte B’ que não sejam as cópias de ajustes anteriores de Origem na Parte B = “Incremental”, podem ser alterados. Os ajustes de origem = ‘Parte A’ ou cópias de Origem na Parte B = “Incremental”, não podem ser alterados/removidos, neste caso, esses registros devem ser apresentados na grid do registro M410 desabilitados.


	MFS-15272		Remover	Botão	-	-	habilitado	Remover

Permite que o usuário remova um Lançamento no Ajuste da Parte B.

Tratamentos:
Aplicar a regra de negócio geral << RNG00041 - Remover>>.


Apenas ajustes de origem = ‘Parte B’ que não sejam as cópias de ajustes anteriores de Origem na Parte B = “Incremental”, podem ser removidos. Os ajustes de origem = ‘Parte A’ ou cópias de Origem na Parte B = “Incremental”, não podem ser alterados/removidos, neste caso, esses registros devem ser apresentados na grid do registro M410 desabilitados.

Após remover o registro, atualizar e recalcular os valores da grid do registro M500 (conforme RNG00044 - Cálculo do Registro M500).

Se o valor do ajuste for removido e a Conta da Parte B possuir Registro na Tabela M305/M355 com data compreendida na apuração. Exibir a mensagem DW00151.


	MFS-15272		Campos da GRID- M410(*)		 (RadioButton)*	RadioButton	-	-	Desmarcado	Checkbox

Permite a seleção de um registro da grid.
	MFS-15272		Data Lançamento	Auto Filtro		DD/MM/AAAA	Auto Filtro

Ao incluir uma palavra neste campo, o sistema deve procurar a palavra ou parte da palavra		Texto		Data do Lançamento


Exibe a data do lançamento da parte B		VALOR	Auto Filtro	-	-	-	Auto Filtro

Ao incluir uma palavra neste campo, o sistema deve procurar a palavra ou parte da palavra nos registros existentes na coluna.	MFS-15272		Texto	S	N	0,00 ou 0,00C ou 0,00D
	Valor

Exibir o valor e indicador do lançamento da parte B, referente a empresa, exercício, período e conta da parte B em questão.

O valor do lançamento realizado não será controlado podendo ser utilizado parte do saldo da conta ou até um valor superior ao saldo da conta.

A ordenação dos registros deve ser feita pelo campo Data do Lancto. Registros com a mesma data devem seguir a ordenação do Banco de Dados.

.
		CONTRAPARTIDA	Auto Filtro	-	-	-	Auto Filtro

Ao incluir uma palavra neste campo, o sistema deve procurar a palavra ou parte da palavra nos registros existentes na coluna.	MFS-15272		Texto	S	N		Contrapartida

Exibir a informação do campo contrapartida, referente a empresa, exercício, período e conta da parte B em questão.
		HISTÓRICO	Auto Filtro	-	-	-	Auto Filtro

Ao incluir uma palavra neste campo, o sistema deve procurar a palavra ou parte da palavra nos registros existentes na coluna.	MFS-15272		Texto	S	N		Histórico

Exibir a informação do campo histórico, referente a empresa, exercício, período e conta da parte B em questão.
		Ajuste com Origem na Parte B	Auto Filtro	-	-	-	Auto Filtro

Ao incluir uma palavra neste campo, o sistema deve procurar a palavra ou parte da palavra nos registros existentes na coluna.	MFS-15272		Texto	S	N		Ajuste com Origem na Parte B

Exibe se o ajuste com origem na parte B foi incremental ou cumulativo.		Tributação Diferida	Auto Filtro	S	N		
Auto Filtro

Ao incluir uma palavra neste campo, o sistema deve procurar a palavra ou parte da palavra nos registros existentes na coluna.	MFS-15678		Texto		Tributação Diferida

Exibe a informação de tributação diferida.		DADOS DOS PROCESSOS		Adicionar	Botão		Adicionar

Permite que o usuário adicione o processo

Tratamentos:
Ao ser acionado sem ter selecionado um registro o sistema deve exibir o  HYPERLINK  \l "modaladicionarprocesos" modal “Adicionar Processo” com os campos em branco e habilitados.

Quando acionado e houver algum registro selecionado, o sistema deve desconsiderar a seleção e exibir o modal com os campos em brancos.	MFS-15272		Remover	Botão		Remover

Permite que o usuário exclua registros da grid de processos

Tratamento
Aplicar regra de negócio geral RNG00041 - Remover	MFS-15272		Campos da Grid dos Processos(*)		TIPO DE PROCESSO	Texto	N	N		Tipo de Processo

Permite que o usuário visualize o tipo de processo

Conteúdos Válidos:

- Judicial
- Administrativo
	MFS-15272		NÚMERO DO PROCESSO	Texto	N	N		Número do Processo

Permite que o usuário visualize o número do processo a ser cadastrado.	MFS-15272		
(*) Não exibir a descrição na tela.


3.3 Modais


Campos do Modal – Adicionar Lançamentos da Parte B ou Alterar Lançamentos da Parte B

Voltar ao  HYPERLINK  \l "botaoadicionarlancamentosparteb" botão Adicionar
Voltar ao  HYPERLINK  \l "botaoAlterar" botão Alterar		Data do Lançamento	Data	S	N	DD/MM/AAAA	Data do Lançamento

Permite que o usuário informe a data do Lançamento

Tratamentos

Se a data informada neste campo for anterior à “Data de Criação da Conta” Ou se a data informada neste campo for posterior à Data Limite, exibir a mensagem DW00152.


Só deve ser exibidos e aceitos lançamentos cuja data lancto esteja compreendida dentro do mês ou trimestre da apuração, posterior ou igual a Data Inicial e anterior ou igual a Data final da apuração. Na criação do ajuste, se a data de lançamento (data lancto) não estiver compreendida dentro do mês ou trimestre que o usuário está trabalhando, exibir a mensagem DW00154.

	MFS-15272		Valor	Texto	S	S	xxx.xxx,xx	Valor

Permite que o usuário informe o valor do ajuste	MFS-15272		Ind. do Valor	Lista	S	S		Ind. do valor
Permite que o usuário informe o indicador do lançamento
 
Tratamentos:


Conteúdos Validos:

Crédito
Débito
Prejuízo do Exercício.
Base de calculo negativa da CSLL.


Durante os cálculos, converter os valores conforme regra abaixo:

Crédito = C (Crédito)
Débito= D (Débito)
Prejuízo do Exercício = D (Débito)
Base de calculo negativa da CSLL = D (Débito)


	MFS-15272		Tributação Diferida	Lista	S	S		Tributação Diferida:

Permite que o usuário informe se o lançamento tem tributação diferida.

Conteúdos Validos:
Sim
 Não
	MFS-15272		Histórico	Texto	S	S		Histórico

Permite que o usuário informe um histórico para o ajuste a ser inserido.	MFS-15272		Contrapartida	LOV	N	N	Código - Descrição	Contrapartida

Permite que o usuário informe/visualize o Código e Descrição da conta da Parte B informada como contrapartida.
Considerar na busca todos os registros de contas da parte B cadastrados para o mesmo CNPJ e que possua os campos “Tipo de Tributo” e “Lançamento” iguais ao do registro que está sendo editado. A própria conta da parte B não pode ser exibida na lista para seleção.


Tratamentos:

Desabilitar este campo e não permitir o preenchimento do mesmo quando o campo Ind. do valor for igual a “PF” ou “BC”.

Campos de Pesquisa – LOV: Conta e Descrição da conta da Parte B. 	MFS-15272		Desc. da Contrapartida	Texto	N	N		Desc. Da Conta da Parte B:

Exibe a descrição da conta da parte B selecionada	MFS-15272		Data de Criação da Conta	Texto
	N	N	DD/MM/AAAA
Desabilitado
	

Permite que o usuário visualize a data de criação da conta da parte B que foi selecionada.

	MFS-15272		Data Limite	Texto
	N	N	DD/MM/AAAA
Desabilitado
	Permite que o usuário visualize a data de limite da conta da parte B que foi selecionada.
	MFS-15272		Saldo Inicial da Escrituração	Texto	N	N	xxx.xxx,xx D ou 
xxx.xxx,xx C	Saldo Inicial da Escrituração

Permite que o usuário visualize o saldo inicial da escrituração da conta selecionada. Valor e indicador.
	MFS-15272		Ajuste com Origem na Parte B	Lista	S	S	Incremental	Ajuste com Origem na Parte B

Permite que o usuário parametrize os ajustes com origem na Parte B terão seus valores Cumulativos ou Incrementais.

Conteúdos Válidos:

- Incremental
- Cumulativo

Tratamentos:

Apuração Trimestral:

Se campo Apuração da tela Informações ECF estiver preenchido com “Trimestral”, preencher o campo com a opção Incremental e desabilitá-lo. 


	MFS-15272		OK	Botão	-	-		Permite incluir ou alterar um registro na grid do registro do M410.


Tratamentos:


Aplicar a regra de negócio geral << RNG00012 - Salvar>>

Para registros duplicados existentes na base de dados:

O Sistema deve verificar se existe um mesmo ajuste da parte b (M410) para a abertura desta escrituração. Caso positivo, aplicar Regra de negócio geral <<RNG00011- Duplicidade de Registro>>


Ao inserir ou alterar um ajuste da Parte B, deve ser recalculado os campos do registro M500 (conforme RNG00044 - Cálculo do Registro M500). 


Se a Conta da Parte B possuir Registro na Tabela M305/M355 (com data compreendida na apuração), exibir a mensagem DW00151. Esta mensagem deve ser exibida na inclusão, alteração e remoção dos lançamentos que possuem registro na tabela M305/M355. 


Após adicionar o registro, atualizar os valores da grid.

	MFS-15272		Cancelar	Botão	-	-	Habilitado	Permite ao usuário cancelar a ação e voltar para a tela principal, sem salvar nada.

Aplicar regra RNG00020 – Botão Cancelar.
	MFS-15272		(*) Não exibir a descrição na tela.

Modal Adicionar Processos

Voltar para o  HYPERLINK  \l "botaoadicionarprocessos" Botão Adicionar		Tipo de Processo	Texto	N	S		Tipo de Processo

Permite que o usuário visualize o tipo de processo

Conteúdos Válidos:

- Judicial
- Administrativo
	MFS-15272		Número do Processo	Texto	N	S		Número do Processo

Permite que o usuário visualize o número do processo a ser cadastrado.
	MFS-15272		OK	Botão		Adicionar

Ao ser acionado o botão “OK”, o sistema inclui o registro na grid correspondente.
Aplicar Regra de negócio geral <<RNG00011- Duplicidade de Registro>>

Após adicionar o registro, atualizar os valores da grid.

	MFS-15272		Cancelar	Botão	-	-	Habilitado	Cancelar

Ao ser acionado o botão “Cancelar”, o sistema fecha o modal e volta para tela anterior.

Aplicar regra de negócio geral RNG00020 – Botão Cancelar	MFS-15272		
 (*) Não exibir a descrição na tela.