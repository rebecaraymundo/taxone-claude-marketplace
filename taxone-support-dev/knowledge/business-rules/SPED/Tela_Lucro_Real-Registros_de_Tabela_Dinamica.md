# Tela_Lucro_Real-Registros_de_Tabela_Dinamica

> Fonte: Tela_Lucro_Real-Registros_de_Tabela_Dinamica.doc

THOMSON REUTERS

Tela Lucro Real 
ECF – Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		13/10/2017	MFS-14136	Criação do Documento	Alessandra Cristina Navatta		23/01/2018	MFS-12701	Liberação das telas do bloco M (M300, M305, M310, M312/M350, M355, M360e M362) 	Alessandra Cristina Navatta		06/02/2018	MFS-12702	Liberação das telas do Bloco N (N500, N600, N610, N620, N630, N650, N660, N670)	Alessandra Cristina Navatta		06/03/2018	MFS-17046	Inclusão do filtro Visão por Tipo de Receita 	Alessandra Cristina Navatta		20/03/2018	MFS-17410	Liberação da tela do Bloco N (N615)	Alessandra Cristina Navatta		05/04/2018	MFS-17659	Exibir as Informações de Percentual de Receita Bruta (nas linhas 2 dos registros N500 e N650), quando existir essa quebra.	Alessandra Cristina Navatta		28/05/2018	MFS-18709	Exibir detalhamento do PAT para as linhas 9 do registro N620 e 8 do N630.	Alessandra Cristina Navatta		

Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc524430140" 1.	INTRODUÇÃO	 PAGEREF _Toc524430140 \h 3
 HYPERLINK \l "_Toc524430141" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc524430141 \h 3
 HYPERLINK \l "_Toc524430142" 3.	TELAS	 PAGEREF _Toc524430142 \h 3
 HYPERLINK \l "_Toc524430143" 3.1.	Pesquisa de Registros	 PAGEREF _Toc524430143 \h 3
 HYPERLINK \l "_Toc524430144" 3.2.	Regras dos Campos Tela Principal	 PAGEREF _Toc524430144 \h 5
 HYPERLINK \l "_Toc524430145" 3.3.	Detalhamentos dos Registros	 PAGEREF _Toc524430145 \h 21


	


INTRODUÇÃO

Objetivo desta especificação é criar a tela de demonstração de resultado dos registros oriundos de tabela dinâmica.

DOCUMENTOS DE REFERÊNCIA


Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
Tela_Informacoes_ECF.docx
Tela_Abertura_de_Apuracao.doc
MTZ_Processamento_em_Lote.docx


TELAS

Pesquisa de Registros 

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Lucro Real >> Demonstração
Título: Lucro Real

Quando o usuário acessar a tela de consulta, apresentar todos os registros contidos na tabela de informações ECF.
Os dados desta tela como base o processamento realizado pela rotina de processamento em lote.

Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.


Campo	Tipo	Regra		Estabelecimento	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
AAAA	

O usuário poderá informar o exercício. 

		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código-Descrição)	Aplicar a RNG00004 (Versão de Layout)		Forma de Tributação	Lista
(Código - Descrição)	Exibe as opções abaixo:

-Lucro Real, Lucro Presumido, Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 


		Apuração	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral

		


Regras dos Campos Tela Principal


Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Lucro Real >> Demonstração
Título da tela: Lucro Real


Considerações Gerais: 


Apresentar os registros cuja a forma de tributação = Lucro Real

Se durante o processamento em lote, for selecionada a opção “Manter Ajustes Manuais Realizados” os anexos inseridos nesta tela deverão ser visualizados conforme ajuste manual realizado antes da nova importação dos saldos com a opção manter ajustes manuais realizados desde que os critérios definidos na RNI10.02 sejam atendidos. 

Para os registros N500 e N650 (apurações diferentes de A00):

Quando o usuário optar pelo tipo de receita “Balanço de Suspensão/Redução” através da tela “Abertura da Apuração” ou “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, apresentar valor apenas na linha 1 se houver, a linha 2 deve ser apresentada zerada e sem detalhamento.

Quando o usuário optar pelo tipo de receita “Receita Bruta” através da tela “Abertura da Apuração” ou “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, apresentar valor apenas na linha 2 se houver, a linha 1 deve ser apresentada zerada e sem detalhamento.

Quando o usuário optar pelo tipo de receita “Comparativo” através da tela “Abertura da Apuração” e o campo “Considerar automaticamente o menor valor de imposto no comparativo” estiver selecionado, após o Processamento em Lote – execução da Rotina Cálculo das Fórmulas:

Identificar o menor valor e apresentar valor apenas na linha 1 se houver, na linha 2 deve ser apresentado zero quando o menor valor corresponder a seleção do Tipo de Receita = “Balanço de Suspensão/Redução”. Se o menor valor corresponder a seleção do Tipo de Receita = “Receita Bruta”, apresentar o valor apenas na linha 2 se houver, a linha 1 deve ser apresentada zerada e sem detalhamento.

- Quando o usuário optar pelo tipo de receita “Comparativo” através da tela “Abertura da Apuração” e o campo “Considerar automaticamente o menor valor de imposto no comparativo” estiver desmarcado e após o Processamento em Lote – execução da Rotina Cálculo das Fórmulas, não for escolhido o tipo de receita:

Apresentar as duas linhas do registro N500 e seus respectivos valores. 

Para os registros N500 e N650, linha 2 (apurações iguais a A00):

Exibir a linha, sem o detalhamento (de conta contábil e ou entrada manual), pois o valor da linha será sempre zerado.


Para os registros N620 e N660:

-Aplicar RNG00048 – Registros N620 e N660

Para os registros N630 e N670, exibir apenas a aba Anual, quando a Apuração igual a Anual, caso contrário, mostrar todos os trimestres. 

Para os registros N600, N610 e N615:

As opções correspondentes aos períodos de apuração que possuem tipo de receita igual a “Receita Bruta” selecionada através das telas “Abertura de Apuração” ou “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, não devem ser exibidas, apenas a aba anual deve ser apresentada. Esta regra é a mesma regra realizada na geração desses registros no meio magnético.


Para os registros do bloco M: M300/M350, M410, Contrapartida e M500:

As opções correspondentes aos períodos de apuração que possuem tipo de receita igual a “Receita Bruta” selecionada através das telas “Abertura de Apuração” ou “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, não devem ser exibidas. Esta regra é a mesma regra realizada na geração desses registros no meio magnético.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	OS/CH/WI		Dados Gerais		Estabelecimento
	Texto
	S	N	Tipo – Código - Descrição	Permite que o usuário visualize o Estabelecimento da apuração que foi recuperada	MFS-14136		Exercício	Texto	S	N	AAAA	Permite que o usuário visualize o ano correspondente à demonstração dos resultados.

	MFS-14136		Data Inicial	Texto
	S	N	
DD/MM/AAAA 
	Permite que o usuário visualize a data inicial, referente ao registro selecionado.	MFS-14136		Versão	Texto	S	N	Código - Descrição	Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar a RNG00004 (Versão de Layout)	MFS-14136		Forma de Tributação	Texto
	S	N	Descrição	Permite que o usuário visualize a forma de tributação, referente ao registro selecionado.
	MFS-14136		Apuração	Texto
	S	N	Descrição	Permite que o usuário visualize a apuração, referente ao registro selecionado.
	MFS-14136		Data Final do Último Período da Escrituração	Texto	S	N	DD/MM/AAAA 	Permite que o usuário visualize a data final do último período da escrituração. 

Tratamento:

Com base na escrituração recuperada, considerar neste campo a data final do último período da escrituração.
	MFS-14136		Exibição dos dados	Radiobutton	S	S	Default:
Apenas Registros com Movimento	Permite que o usuário escolha a forma de exibição das informações nas abas, se deseja visualizar apenas os registros que possuam movimento ou todos os registros.

Conteúdos Válidos:
Apenas Registros com Movimento
Todos

Tratamentos:
Quando o usuário selecionar a opção “Apenas Registros com Movimento”, apresentar nas abas apenas os registros cujo campo “Valor” seja diferente de zero.
Quando o usuário selecionar a opção “Todos”, apresentar nas abas apenas os registros todos os registros.
	MFS-14136		Subtítulo: (*)
Filtros de Registro/Apurações		Registro	Lista	S	S	Código 	Opções de Registros válidos:

Forma de Tributação = Lucro Real: 

Opções Válidas

L210
M300
M350
M410
Contrapartida
M500
N500
N600
N610
N615
N620
N630
N650
N660
N670


Tratamentos:

Registros Oriundos a tabela Dinâmica:

L210
M300
M350
N500
N600
N610
N620
N630
N650
N660
N670

Demais Registros 

M410
M500
N615


Tratamentos:

Para os registros oriundos de tabela dinâmica e Demais Registros:

A exibição dos registros deve obedecer a ordem dos registros e suas hierarquias.
(Existentes na planilha Layout_ECF.xlsx).
Apenas registros de nível 3 devem ser exibidos na treeview. Os registros filhos, desses registros, serão exibidos na tela do lado direito.

 HYPERLINK  \l "Contrapartida" Contrapartida:

Apresentar esta opção se houver na abertura algum registro criado de origem conta contrapartida (M410)
Disponibilizar esta opção abaixo do registro M410 (na lista
	MFS-14136
MFS-12701
MFS-12702
MFS-17410		Apurações
	Lista	S	S	Descrição	Opções de ‘Título’ válidas:

Anual
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
1º Trimestre
2º Trimestre
3º Trimestre
4° Trimestre


A lista será visualizada de acordo com as seguintes regras:

Forma de Tributação = Real ou Imune de IRPJ ou Isenta do IRPJ e Apuração Anual

Anual:

-No processo de Importação de Saldos, quando existir um período de apuração com forma de tributação = Real ou Imune de IRPJ ou Isenta do IRPJ e Apuração= Anual, deverá ser exibida a opção Anual.

Mensal:

- No processo de Importação de Saldos, para cada período de apuração encontrado com forma de tributação = Real ou Imune de IRPJ ou Isenta do IRPJ e Apuração= Anual.


Forma de Tributação = Real ou Presumido ou Arbitrado ou Imune de IRPJ ou Isenta do IRPJ e a Apuração Trimestral: 

- No processo de Importação de Saldos, para cada período de abertura encontrado com trimestre, exibir a opção do trimestre correspondente. Se todos os períodos de abertura de apuração do exercício gerados forem trimestrais, a opção Anual não deverá ser exibida na tela.

Conteúdo:

Deverão respeitar as regras abaixo e as regras de processamento no documento MTZ_Processamento_em_Lote.docx

	MFS-14136		‘TÍTULO’	Texto	S	N	Código - Descrição	Tratamento:

Exibe o código e a descrição do registro.
	MFS-14136		Apenas Registros com movimento	check-box	S	S	Default:
Desmarcado	Permite que o usuário escolha a forma de exibição das informações nas abas, se deseja visualizar apenas os registros que possuam movimento ou todos os registros.


Tratamentos:
Quando o usuário selecionar a opção “Apenas Registros com Movimento”, apresentar nas abas os registros cujos campos “Valor do Saldo Inicial” ou “Valor do Saldo Final” sejam maiores que zero.
Quando o usuário selecionar a opção “Todos”, apresentar nas abas apenas os registros todos os registros.
	MFS-14136		Visão por Tipo de Receita	Lista	N	S	Balanço de Suspensão/Redução	

Permite que o usuário visualize/altere as informações do registro por tipo de receita.


Tratamentos:

Opções Válidas:
Receita Bruta
Balanço de Suspensão/Redução 


Só demonstrar esse campo para os registros N620 e N660 e se a opção ‘Não se Aplica’, não estiver selecionada no campo tipo de receita da tela de Abertura de apuração.

Para as condições acima, apresentar este campo habilitado e possível de alteração se:

Na tela “Abertura da Apuração” o usuário optar por tipo de receita “Comparativo” e não efetuar a escolha por um tipo de receita (seja por meio da Tela “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, ou pelo parâmetro “Considerar automaticamente o menor valor de imposto no comparativo”) .


Se for definido um tipo de receita, mostrar este campo desabilitado com a opção escolhida selecionada (seja na tela de abertura pelo campo tipo de receita, pelo parâmetro “Considerar automaticamente o menor valor de imposto no comparativo” ou pela tela do comparativo).

 
Quando o usuário escolher a opção “Receita Bruta”, atualizar a grid dos Registros N620 e/ou N660, considerando os valores correspondente ao tipo de receita “Receita Bruta”.

Quando o usuário escolher a opção “Balanço de Suspensão/Redução”, atualizar a grid dos Registros N620 e/ou N660 considerando os valores correspondente ao tipo de receita “Balanço de Suspensão/Redução”.

- Quando o usuário fizer a opção por um tipo de receita no período através da tela de “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, ou marcar a opção “Considerar automaticamente o menor valor de imposto no comparativo”, este campo deve ficar desabilitado, com a escolha definida e devem ser demonstradas as informações do registro conforme o tipo de receita escolhido pelo usuário.
	MFS-17046		Grid dos registros de origem tabela dinâmica (L210, M300,M350, N500, N600, N610, N620, N630, N650, N660, N670)(*)
		Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.

Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-14136		Cód. do Registro	Texto	S	N
		
Exibe os códigos de todas as linhas das tabelas dinâmicas ou os códigos da conta específica associadas que possuem ou não associação com as linhas tabelas dinâmicas.	MFS-14136		Desc. do Registro	
Texto	
S	
N		
Exibe a descrição das linhas das tabelas dinâmicas ou a descrição da conta específica corresponde ao código exibido no campo Cód. do Registro.	MFS-14136		Ordem	Texto	S	N		Exibe a ordem de cada linha da tabela dinâmica.

	MFS-14136		Linha da ECF	Texto	S	N		Exibe a ordem de cada linha da tabela dinâmica. 

	MFS-14136		Valor	Texto	S	N		Exibe o valor das linhas das tabelas dinâmicas.

Tratamento:


Para cada linha da tabela dinâmica que possuam o Tipo = “R” devem ser exibidos os registros em branco.	MFS-14136		Grid Registro M410 (*)		

Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.

Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-12701		Grupo da Conta	
Texto	
S	
N		
Exibir o código e a descrição do grupo que a conta da parte B foi cadastrado.

	MFS-12701		Conta da Parte B	
Texto	
S	
N	Código - Descrição	

Exibir o código e a descrição da conta da parte B do registro M410. 

	MFS-12701		Tributo	
Texto	
S	
N	Descrição	

Exibir tributo referente ao movimento da conta do registro M410. 

	MFS-12701		Data Lançamento	Texto	
S	
N		
Exibe a data do lançamento da parte B do registro M410.	MFS-12701		Valor	
Texto	
S	
N		Exibir o valor e indicador do lançamento da parte B, do registro M410.
	MFS-12701		Contrapartida	Texto	
S	
N		

Exibir a informação do campo contrapartida, do registro M410.
	MFS-12701		Histórico	
Texto	
S	
N		
Exibir o histórico do registro M410.
	MFS-12701		Ajuste com Origem na Parte B	Texto	
S	
N	Descrição	Exibir se o ajuste com origem na parte B foi incremental ou cumulativo.

Valores Válidos:
Incremental
Cumulativo	MFS-12701		Tributação Diferida	Texto	
S	
N		
Exibir a informação de tributação diferida.

Valores Válidos:
Sim
Não	MFS-12701		Grid Registro M500 (*)		

Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.

Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-12701		Grupo da Conta	
Texto	
S	
N		Grupo

Exibir o código e a descrição do grupo que a conta da parte B foi cadastrado.

	MFS-12701		Conta da Parte B	
Texto	
S	
N	Código - Descrição	Conta da Parte B

Exibir o código e a descrição da conta da parte B do registro M500. 

	MFS-12701		Tributo	
Texto	
S	
N	Descrição	Tributo

Exibir tributo referente ao movimento da conta do registro M500. 

	MFS-12701		 SALDO INICIAL 	
Texto	
S	
N		Saldo Inicial

Exibir o saldo inicial do registro M500. 

	MFS-12701		LANÇAMENTOS DA PARTE A	
Texto	
S	
N	
0,00, 0,00C ou 0,00D	Lançamentos da Parte A

Exibir o somatório dos lançamentos da parte A. 


	MFS-12701		
LANÇAMENTOS DA PARTE B	
Texto	
S	
N	
0,00, 0,00C ou 0,00D	Lançamentos da Parte B

Exibir o somatório dos lançamentos da parte B. 


	MFS-12701		LANÇAMENTOS DA PARTE B - CONTRAPARTIDA	Texto	S	N	0,00, 0,00C ou 0,00D	Lançamentos da Parte B - Contrapartida

Exibir o somatório dos lançamentos da parte B (contrapartida). 

	MFS-12701		SALDO FINAL	
Texto	
S	
N	
0,00, 0,00C ou 0,00D	Saldo Final

Exibir o valor do saldo final. 

	MFS-12701		Grid Contrapartida (*)		

Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.

Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-12701		Grupo da Conta	
Texto	
S	
N		
Exibir o código e a descrição do grupo que a conta da parte B foi cadastrado.

	MFS-12701		Conta da Parte B	
Texto	
S	
N	Código - Descrição	

Exibir o código e a descrição da conta da parte B do registro de contrapartida. 

	MFS-12701		Tributo	
Texto	
S	
N	Descrição	

Exibir tributo referente ao movimento da conta do registro de contrapartida. 

	MFS-12701		Data Lançamento	Texto	
S	
N		
Exibe a data do lançamento da parte B do registro de contrapartida.	MFS-12701		Valor	
Texto	
S	
N		Exibir o valor e indicador do lançamento da parte B, do registro de contrapartida.
	MFS-12701		Conta Parte B Origem da Contrapartida	Texto	
S	
N	Código-Descrição	

Exibir a informação da conta parte b que deu origem ao registro de contrapartida.
	MFS-12701		Histórico	
Texto	
S	
N		
Exibir o histórico do registro de contrapartida.
	MFS-12701		Ajuste com Origem na Parte B	Texto	
S	
N	Descrição	Exibir se o ajuste com origem na parte B foi incremental ou cumulativo do registro de contrapartida.	MFS-12701		Tributação Diferida	Texto	
S	
N		
Exibir a informação de tributação diferida do registro de contrapartida.

	MFS-12701		Grid N615 (*)		

Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.

Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-17410		Base de Calculo	Texto	
S	
N	0,00	Exibir a informação da base de cálculo dos incentivos fiscais.
	MFS-17410		Percentual FINOR	Texto	
S	
N	0,0000	Exibir a informação do percentual do incentivo FINOR (até 6%).
	MFS-17410		Valor Líquido FINOR	Texto	
S	
N	0,00	Exibir a informação do valor líquido do incentivo FINOR.
	MFS-17410		Percentual FINAM	Texto	
S	
N	0,0000	Exibir a informação do percentual do incentivo FINAM (até 6%).
	MFS-17410		Valor Líquido FINAM	Texto	
S	
N	0,00	Exibir a informação do valor líquido do incentivo FINAM.
	MFS-17410		Valor Total	Texto	
S	
N	0,00	Exibir a informação do valor total dos incentivos.
	MFS-17410		   (*) Não exibir a descrição na tela.


Detalhamentos dos Registros

Registro L210, N500, N600, N610, N620, N630, N650, N660, N670:

Deverá ser exibido quando a linha da tabela dinâmica selecionada na grid, possuir associação direta com as contas contábeis (*)
Título: (*)
Detalhamento 		
Contas Contábeis e Centros de Custos Associados
		Cód. da Conta Contábil	Texto	S	N		Exibe os códigos das contascontábeis associadas à conta referencial recuperada.
	MFS-14136		Desc. da Conta Contábil	
Texto	S	N		Exibe a descrição da conta contábil associadas à conta referencial recuperada.
	MFS-14136		Cód. do Centro de Custo	
Texto	S	N		Exibe o código do centro de custo associados à conta referencial recuperada.
	MFS-14136		Desc. do Centro de Custo	Texto	S	N		Exibe a descrição do centro de custo associados à conta referencial recuperada.
	MFS-14136		Valor	

Texto	S	N		Exibe o valor do saldo ou movimento que foi considerado desta conta contábil e centro de custo, associados à conta referencial.	MFS-14136		Ind. do Valor	

Texto	S	N		Exibe o indicador do saldo ou movimento que foi considerado desta conta contábil e centro de custo, associados à conta referencial.	MFS-14136		Percentual da Receita Bruta 	

Texto	S	N		Este campo deve ser exibido para a linha2 dos registros N500 ou N650, se existir a quebra por percentual e se o valor do percentual foi considerado na importação de saldos (valor informado na associação das tabelas dinâmicas com o plano da empresa), caso contrário, não exibir este campo.
	MFS-17659		(*) Não exibir a descrição na tela.

Registro L210, M300, M350, N500, N600, N610, N620, N630, N650, N660, N670:

Deverá ser exibido quando a linha da tabela dinâmica selecionada possuir fórmulas (*)
Título: (*)
Detalhamento		
Fórmula
		Exibição das Fórmulas (*)	Texto	S	N	-	Exibe a fórmula utilizada para identificação do valor do código do registro selecionado conforme a coluna “Fórmula” da planilha [Tabelas_Dinamicas.xls], para fórmulas condicionadas, verificar na planilha a coluna “Fórmulas Condicionadas”
	MFS-14136		(*) Não exibir a descrição na tela.

Registro L210, N500, N600, N610, N620, N630, N650, N660, N670:

Deverá ser exibido quando a linha da tabela dinâmica selecionada possuir entrada manual (*)
Título: (*)
Detalhamento		
Entrada Manual
		Exibição do Valor (*)	Texto	S	N	-	Exibe o valor correspondente a entrada manual efetuada.

Tratamento:

Para a linha 2 dos registros N500 e N650, apresentar a quebra por percentual, se utilizado pelo menos um dos campos ‘Valor da Receita Bruta Sujeita a X,X%’.

Ex. Alteração manual nos campos: 
Valor da Receita Bruta Sujeita a 1,6% = 1000,00
Valor da Receita Bruta Sujeita a 16% = 500,00
 

Se a alteração manual, ocorrer apenas na linha 2 (sem utilizar os valores do campo ‘Percentuais da Receita Bruta’), exibir apenas o Valor (conforme demais linhas e registros).
	MFS-14136
MFS-12702
MFS-17659		(*) Não exibir a descrição na tela.

Registros M300 / M350:

Grid exibida no detalhamento dos registros M300/M350(*)

Esta tela deverá ser exibida quando a linha da tabela dinâmica selecionada for um registro de Lançamento da Parte A – M305/M355(*)

		 Devem ser exibidas nesta aba as Contas da Parte B que possuírem associação com os Lançamentos da Parte A. M305/M355 (*)

Título da Aba(*)
 Contas da Parte B

		Cód. Da Conta 	Texto	S	N	Código - Descrição	Exibe o código e descrição da conta da parte B, cujo registro foi selecionado na tela principal.
	MFS-12701		Valor	
Texto	S	N	-	
Exibe o valor e indicador da conta da parte B
	MFS-12701		

Devem ser exibidas nesta aba as Contas da Parte B que possuírem associação com os Lançamentos da Parte A.M310/M360(*)

Título da Aba (*):
Contas Contábeis
		Conta Contábil	Texto	S	N	Código - Descrição	Exibe o código e descrição da conta contábil associada à conta contábil recuperada.
	MFS-12701		Centro de Custo	
Texto	S	N	Código - Descrição	Exibe o código e descrição do centro de custo associado à conta contábil recuperada.
	MFS-12701		Valor	Texto	S	N	-	Exibe o valor e indicador do saldo ou movimento que foi considerado desta conta contábil e centro de custo, associados ao item da tabela dinâmica.
	MFS-12701		Recuperação de Valores	Texto	S	N	-	
Recuperação de Valores 

Exibe a origem do valor da conta contábil.

Deve exibir o conteúdo do campo Recuperação dos Valores da Tela Recuperação dos Valores – Apuração IRPJ/CSLL correspondente a conta contábil.

Saldo
Movimento
Total de Débito
Total de Crédito


	MFS-12701		Grid Lançamentos Contábeis(*)

Devem ser exibidas nesta grid os lançamentos contábeis M312/M362 (*)
		Núm. do Lançamento	Texto	S	N	-	Exibe o número do lançamento contábil associado à conta contábil e ao centro de custo.


	MFS-12701		Valor	
Texto	S	N	-	Exibe o valor e indicador do lançamento contábil/ajustes que foi considerado como saldo da conta contábil.
	MFS-12701		(*) Não exibir a descrição na tela.

Registro M410:

Grid exibida no detalhamento do registro M410 – Registros M415(*)

Título: (*)
Codigo – Descrição do Registro		TIPO DE PROCESSO	Texto	S	N		
Permite que o usuário visualize o tipo de processo

Conteúdos Válidos:

- Judicial
- Administrativo
	MFS-12701		NÚMERO DO PROCESSO	Texto	S	N		Número do Processo

Permite que o usuário visualize o número do processo a ser cadastrado.
	MFS-12701		(*) Não exibir a descrição na tela.

Registro N620 e N630:
Modal (*)

Este modal deverá ser exibido apenas quando o usuário quiser visualizar o detalhamento das linhas 9 do registro N620 e 8 do registro N630A, N630B ou N630C. (*)

Título: (*)
Detalhamento		Agrupamento (*)

ANTES DA ATUALIZAÇÃO	Texto	S	N	-	Agrupar os campos VALOR DO PAT e LIMITE DE 15% SOBRE O PAT	MFS-18709		Valor do PAT 	Texto	S	N	-	Exibe o valor da linha 9 do registro N620 ou 8 do registro N630A, N630B ou N630C antes de realizar o cálculo do PAT.
Obs.: Mesmo valor após o processamento da importação dos saldos.	MFS-18709		Limite de 15% sobre o PAT 
	
Texto	S	N	-	Exibe o limite de 15% calculado sobre o PAT antes da atualização.	MFS-18709		Valor do Imposto Devido	
Texto	S	N	-	Exibe o valor do imposto, ou seja, valor da linha 3 do registro N620 ou 8 do registro N630A, N630B ou N630C.	MFS-18709		Limite de 4% sobre o Imposto Devido	Texto	S	N	-	Exibe o limite de 4% calculado sobre o imposto devido.	MFS-18709		Valor do PDTI/PDTA	
Texto	S	N	-	Exibe o valor do PDTI/PDTA, ou seja, valor da linha 10 do registro N620 e linha 9 do registro N630A, N630B ou N630C	MFS-18709		Limite de 4% com PDTI/PDTA	
Texto	S	N	-	Exibe o limite de 4% com a dedução do incentivo PDTI/PDTA.	MFS-18709		Valor do PAT de Períodos Anteriores	
Texto	S	N	-	Exibe o valor de PAT que foi utilizado de períodos anteriores.	MFS-18709		Valor do PAT Atualizado	
Texto	S	N	-	Exibe o valor do PAT após o cálculo. 
Obs.: Mesmo valor da linha 9 do registro N620 ou 8 do registro N630A, N630B ou N630C após a realização do cálculo de registros e fórmulas.	MFS-18709		(*) Não exibir a descrição na tela.