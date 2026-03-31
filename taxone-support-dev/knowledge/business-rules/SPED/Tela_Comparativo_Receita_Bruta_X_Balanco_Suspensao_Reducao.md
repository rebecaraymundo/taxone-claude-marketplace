# Tela_Comparativo_Receita_Bruta_X_ Balanco_Suspensao_Reducao

> Fonte: Tela_Comparativo_Receita_Bruta_X_ Balanco_Suspensao_Reducao.doc

THOMSON REUTERS
 
Tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução 
 ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		01/03/2018	MFS-16929	Criação do documento	Alessandra Cristina Navatta		29/05/2018	MFS-18706	Considerar os valores calclulados do PAT (apenas referente ao registro N620) no momento da escolha entre Receita Bruta ou Balanço de Suspensão/Redução, além disso, o valor que foi calculado para a opção não escolhida, deve ser desconsiderado (inclusive o PAT utilizado de períodos anteriores).	Alessandra Cristina Navatta		

Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc511135410" 1.	INTRODUÇÂO	 PAGEREF _Toc511135410 \h 3
 HYPERLINK \l "_Toc511135411" 2.	DOCUMENTOS DE REFERÊNCIAS	 PAGEREF _Toc511135411 \h 3
 HYPERLINK \l "_Toc511135412" 3.	TELA/MODAIS	 PAGEREF _Toc511135412 \h 3
 HYPERLINK \l "_Toc511135413" 3.1	Pesquisa de Registros	 PAGEREF _Toc511135413 \h 3
 HYPERLINK \l "_Toc511135414" 3.2	Regras dos Campos Tela Principal	 PAGEREF _Toc511135414 \h 3

INTRODUÇÂO

O objetivo desta especificação é criar uma tela onde o usuário possa conferir os valores de impostos calculados por tipo de receita (receita bruta ou balanço de suspensão/redução) a fim de identificar e optar pela opção mais vantajosa para a empresa.

DOCUMENTOS DE REFERÊNCIAS

Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
Tela_Informacoes_ECF.docx
Tela_Abertura_de_Apuracao.doc
MTZ_Processamento_em_Lote.docx
Tela_Lucro_Real–Registros_de_Tabela_Dinamica.doc

TELA/MODAIS 

Pesquisa de Registros

Não se aplica.

Regras dos Campos Tela Principal

Localização da tela: 
ECF - Escrituração Contábil Fiscal >>Apuração >> Lucro Real >> Comparativo 
Título da tela: Comparativo entre Receita Bruta X Balanço de Suspensão/Redução


Campo	Tipo	Obrigatoriedade	Ed	Formato/Default	Regra	MFS		Filtros		Estabelecimento	LOV	S	S	Tipo – Código – Descrição	Permite que o usuário selecione um estabelecimento.

Tratamentos:
Exibir os estabelecimentos que possuem informações ECF com forma de tributação igual a Lucro Real, Lucro Presumido, Lucro Arbitrado.


	MFS-16929		Todos os Estabelecimentos	Check-box		Desmarcado	Permite que o usuário selecione todos os estabelecimentos que possuem informações ECF com forma de tributação igual a Lucro Real, Lucro Presumido, Lucro Arbitrado.


Tratamento:

Ao marcar este campo, o campo Estabelecimento deve ser limpo e ficar desabilitado.
	MFS-16929		Exercício	Texto	S	S	AAAA	Permite que o usuário visualize o exercício, do registro da tela de Informação ECF, caso apenas um estabelecimento seja recuperado.
Tratamentos:

Se for selecionado todos os estabelecimentos, não exibir esse campo.

Se for selecionado apenas um registro de estabelecimento, apresentar o exercício da Informação ECF recuperada.
	MFS-16929		Data Inicial	Data	N	S	DD/MM/AAAA	Permite que o usuário visualize a data inicial da informação ECF, do registro da tela de Informação ECF, caso apenas um estabelecimento seja recuperado.

Tratamentos:

Se for selecionado todos os estabelecimentos, não exibir esse campo.

Se for selecionado apenas um registro de estabelecimento, apresentar a data inicial da Informação ECF recuperada.
	MFS-16929		Exercício	
Texto	
N	S	AAAA	Permite que o usuário informe o ano a ser considerado na recuperação das informações, caso seja selecionado todos os estabelecimentos no campo acima.

Tratamentos:
Este campo é de preenchimento obrigatório se for selecionado todos os estabelecimentos. Caso não esteja preenchido, aplicar RNG00010 – Campo Obrigatório

Só mostrar este campo na tela, se for selecionado todos os estabelecimentos no campo Estabelecimento.

		Período de Apuração	Lista	N	S	Descrição	Permite que o usuário selecione um período de apuração.

Tratamentos:

Se o campo for preenchido, escolher uma opção válida:

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
4º Trimestre
	MFS-16929		Pesquisar	Botão		Permite que o usuário confirme a busca da abertura de apuração com base nos parâmetros preenchidos.

Recuperação dos Registros:

Recuperar e apresentar as aberturas de apuração (com status diferente de Apuração em Aberto), considerando o preenchimento dos parâmetros acima, das Informações ECF cujo tipo de receita igual a comparativo.

Os registros devem ser apresentados ordenados por estabelecimento, exercício, data inicial e período de apuração.	MFS-16929		Subtítulo: COMPARATIVO ENTRE RECEITA BRUTA X BALANÇO DE SUSPENSÃO/REDUÇÃO		Receita Bruta X Balanço de Supensão/Redução	Lista		Desmarcado	
Permite que o usuário selecione para o período a forma que será considerado para apurar o imposto (Receita Bruta ou Balanço de Suspensão/Redução).

Tratamentos:


Aplicar RNG00050 - Menor Valor


Só permitir marcar o campo se a abertura de apuração estiver com o campo tipo de receita = comparativo, status da apuração = Cálculo Realizado, e se existir abertura posterior, a mesma deve ser diferente de Cálculo Realizado. Caso contrário, o campo deve ficar desabilitado.

Se o campo for selecionado, atualizar as informações na tela Lucro Real, para os registros N620 e ou N660) com as informações correspondentes a opção escolhida.

Se foi calculado pelo processamento em lote as informações do PAT, considerar todos os valores calculado referente a opção escolhida (inclusive o valor do PAT utilizado no período de períodos anteriores (VALOR DO PAT DE PERÍODOS ANTERIORES) e também o valor do PAT que ficou acumulado a ser utilizados em períodos posteriores (VLR. DISPONÍVEL DE PERÍODOS ANTERIORES)).
Obs. Os valores calculados para a outra visão (que não foi escolhida), devem ser desprezados. Esta regra se aplica apenas ao registro N620.
	MFS-16929
MFS-18706		Estabelecimento	Texto	S	N	Tipo – Código – Descrição	Permite que o usuário visualize o estabelecimento do(s) registro(s) recuperado(s).	MFS-16929		Exercício	Texto
	S	N	AAAA	Permite que o usuário visualize o exercício, referente ao(s) registro(s) recuperado(s).	MFS-16929		Data Inicial	Texto	S	N	DD/MM/AAAA	Permite que o usuário visualize a data inicial, referente ao(s) registro(s) recuperado(s).	MFS-16929		Forma de Tributação	Texto
	S	N	Descrição	Permite que o usuário visualize a forma de tributação, referente ao(s) registro(s) recuperado(s).	MFS-16929		Apuração	Texto
	S	N	Descrição	Permite que o usuário visualize a apuração, do(s) registro(s) recuperado.	MFS-16929		PERÍODO	Texto	S	N	Descrição	Permite que o usuário visualize o período de cada abertura de apuração do(s) registro(s) selecionado(s). 	MFS-16929		Status	Texto	S	N	Descrição	Permite que o usuário visualize o status de cada abertura de apuração do(s) registro(s) selecionado(s). 	MFS-16929		Subtítulo: RECEITA BRUTA		IRPJ	Texto	S	N		Permite que o usuário visualize o valor da linha 26 do registro N620 de cada abertura de apuração cujo status seja igual a “Cálculo Realizado” ou “Reapurar” correspondente a Informação do ECF selecionada e cujo tipo de receita seja igual a “Receita Bruta”.
Atenção: Nas apurações com status = ‘Importação de Saldos Realizada’, ‘Aguardando Alteração Manual’ ou ‘Alteração Manual Realizada’, essa linha estará zerada, pois a mesma é obtida por fórmula no processo de Cálculo.
	MFS-16929		CSLL	Texto	S	N		Permite que o usuário visualize o valor da linha 18 do registro N660 de cada abertura de apuração cujo status seja igual a “Cálculo Realizado” ou “Reapurar” correspondente a Informação do ECF selecionada e cujo tipo de receita seja igual a “Receita Bruta”.
Atenção: Nas apurações com status = ‘Importação de Saldos Realizada’, ‘Aguardando Alteração Manual’ ou ‘Alteração Manual Realizada’, essa linha estará zerada, pois a mesma é obtida por fórmula no processo de Cálculo.
	MFS-16929		TOTAL	Texto	S	N		Permite que o usuário visualize o total de imposto a ser pago em cada período.

Tratamentos:
Exibir a somatória dos campos “IRPJ” e “CSLL”, cujo tipo de receita seja igual a “Receita Bruta”.	MFS-16929		Subtítulo: BALANÇO DE SUSPENSÃO/REDUÇÃO		IRPJ	Texto	S	N		Permite que o usuário visualize o valor da linha 26 do registro N620 de cada abertura de apuração cujo status seja igual a “Cálculo Realizado” ou “Reapurar” correspondente a Informação do ECF selecionada e cujo tipo de receita seja igual a “Balanço de Suspensão/Redução”.
Atenção: Nas apurações com status = ‘Importação de Saldos Realizada’, ‘Aguardando Alteração Manual’ ou ‘Alteração Manual Realizada’, essa linha estará zerada, pois a mesma é obtida por fórmula no processo de Cálculo.
	MFS-16929		CSLL	Texto	S	N		Permite que o usuário visualize o valor da linha 18 do registro N660 de cada abertura de apuração cujo status seja igual a “Cálculo Realizado” ou “Reapurar” correspondente a Informação do ECF selecionada e cujo tipo de receita seja igual a “Balanço de Suspensão/Redução”.
Atenção: Nas apurações com status = ‘Importação de Saldos Realizada’, ‘Aguardando Alteração Manual’ ou ‘Alteração Manual Realizada’, essa linha estará zerada, pois a mesma é obtida por fórmula no processo de Cálculo.
	MFS-16929		TOTAL	Texto	S	N		Permite que o usuário visualize o total de imposto a ser pago em cada período.

Tratamentos:
Exibir a somatória dos campos “IRPJ” e “CSLL”, cujo tipo de receita seja igual a “Balanço de Suspensão/Redução”.	MFS-16929