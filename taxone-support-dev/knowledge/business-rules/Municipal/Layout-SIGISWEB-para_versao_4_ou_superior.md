# Layout-SIGISWEB-para versão 4 ou superior

> Fonte: Layout-SIGISWEB-para versão 4 ou superior.doc

S.I.G.I.S.S. Web para versão 4 ou superior

Registro 3 – O campo alíquota que anteriormente possuía apenas uma posição agora passou a ter 12 posições, indo assim da coluna 772 à 783. Isso devido a alíquota do novo simples que tem 10 casas decimais.


 		LAY-OUT ARQUIVO REMESSA

O Nome do arquivo TXT a ser gerado de ser composto pelo CPF/CNPJ da Empresa responsável o Mês e Ano de Competência.TXT. O mês e ano devem vir no formato MMAAAA. O padrão de gravação deve ser ANSI.

Exemplo: 12345678901234012000. txt

Registro tipo “0” READER DO SISTEMA (Primeira linha do arquivo)

Nome do campo	Posição Inicial	Posição Final	Tamanho do Campo	Formato	Conteúdo		Tipo	1	7	7	 A	0SIGISS		Nome Prefeitura	8	57	50	A		Data Geração	58	65	8	D	ddmmyyyy		CNPJ Prefeitura	66	79	14	N		Nome Software gerador das informações	80	89	10	A	Verificar observação abaixo		Versão Layout	90	99	10	A	4		Informativo para sobreposição	100	100	1	A	1 ou branco
(Ver observação abaixo)		
Observação
 	
	Para as empresas que tem desenvolvimento próprio, este campo deve conter a palavra “PRÓPRIO”. No caso de software comercial deve ser colocado nestas posições o nome do software abreviado, exemplo “FOLHAMATIC”.

	Caso o arquivo for substituir os lançamentos que existem no mesmo período na prefeitura, o arquivo deve conter todos os movimentos do período sem exceção e na coluna 100 o número 1 (um) deve ser informado.


Registro tipo “1” EMPRESA RESPONSÁVEL PELAS INFORMAÇÕES

Nome do campo	Posição Inicial	Posição Final	Tamanho do Campo	Formato	Conteúdo		Tipo	1	1	1	N	“1”		Razão Social	2	101	100	A		Nome Fantasia	102	181	80	A		Endereço	182	241	60	A		Numero	242	251	10	A		Complemento	252	291	40		Bairro	292	391	100	A		Município	392	491	100	A		UF	492	493	2	A	SP, RJ, MT, MG e etc.		CEP	494	501	8	N	Ver. Obs. item 1		CNPJ da Empresa	502	515	14	N	Ver. Obs. item 1		Inscrição Municipal	516	530	15	N	Ver. Obs. item 1		Inscrição Estadual	531	545	15	N	Ver. Obs. item 1		Fone	546	589	44	A		E-Mail	590	709	120	A	Ver. Obs. item 10		Data Geração	710	717	8	D	DDMMAAAA		Mês Apuração	718	719	2	N	MM		Ano Apuração	720	723	4	N	AAAA		


Registro tipo “2” REGISTRO DECLARANTE

Nome do campo	Posição Inicial	Posição Final	Tamanho do Campo	Formato	Conteúdo		Tipo	1	1	1	N	“2”		Razão Social	2	101	100	A		Nome Fantasia	102	181	80	A		Endereço	182	241	60	A		Numero	242	251	10	A		Complemento	252	291	40		Bairro	292	391	100	A		Município	392	491	100	A		UF	492	493	2	A	SP, RJ, MT, MG e etc.		CEP	494	501	8	N	Ver. Obs. item 1		CNPJ da Empresa	502	515	14	N	Ver. Obs. item 1		Inscrição Municipal	516	530	15	N	Ver. Obs. item 1		Inscrição Estadual	531	545	15	N	Ver. Obs. item 1		Fone	546	589	44	A		Email	590	709	120	A		Tomador/Prestador	710	710	1	A	T/P
(Ver. Obs. Item 5)		Regime do Declarante	711	711	1	A	E/V/O/S
(Ver. Obs. Item 4)		Movimentação	712	712	1	A	S/N
(Ver. Obs. Item 3)		


Registro tipo “3” REGISTRO DE MOVIMENTO

Nome do campo	Posição Inicial	Posição Final	Tamanho do Campo	Formato	Conteúdo		Tipo	1	1	1	 N	3		Inscrição Municipal 
declarante	2	16	15	N		Nº Documento Fiscal	17	26	10	N		Série do Documento Fiscal	27	29	3	A		Data do Documento Fiscal	30	37	8	D	DDMMAAAA		Nome ou Razão Social Destinatário	38	137	100	A		CPF/CNPJ	138	151	14	N	Ver. Obs. item 1		Inscrição Municipal	152	166	15	N	Ver. Obs. item 1		Inscrição Estadual	167	181	15	N	Ver. Obs. item 1		Endereço	182	241	60	A		Numero	242	251	10		Complemento	252	291	40	A		Bairro	292	391	100	A		Cidade	392	491	100	A		UF	492	493	2	A	SP, RJ, MT, MG e etc.		CEP	494	501	8	N	Ver. Obs. item 1		Fone	502	565	64	A		Email	566	685	120	A	Ver. Obs. item 10		Estrangeiro	686	686	1		S/N		País	687	726	40	A		Valor Documento Fiscal	727	741	 12,2=15	N	0,00		Deduções Legais	742	756	 12,2=15	N	0,00		Valor Serviços	757	771	 12,2=15	N	0,00		Alíquota	772	783	0,0000000000=12	N	0,0000		Valor Imposto	784	798	 12,2=15	N	0,00		ISS retido na Fonte	799	799	1	A	S/N		Documento Fiscal Cancelado	800	800	1	A	S/N		Código Classif. Serviço	801	807	7	A	Texto. Ex "14.01 ", “7.01  ”		


Registro tipo “9” FOOTER DO ARQUIVO

Nome do campo	Posição Inicial	Posição Final	Tamanho do Campo	Formato	Conteúdo		Tipo	1	1	1	N	“9”		Qtde de Registros do Tipo “3”	2		N		
O campo Qtde de Registros 3. Não está especificado o tamanho do campo, pois o mesmo deve conter a quantidade de dígitos necessários para representar a quantidade de registros 3.


Observações

Campos como CPF/CNPJ, CEP, Inscrição Municipal não devem ser preenchidos com formatação e nem com zeros a esquerda (somente deverão vir os zeros relevante a esquerda). Quando o lançamento for para “AO CONSUMIDOR”, deve-se informar “0” (um único zero) e os demais campos referentes ao tomador deste registro devem ficar em branco.                                                                                                          
Preenchimento do campo Regime do declarante
		E - Estimado
		V - Variável
		O - Quando o declarante for tomador
		S - Simples
Preenchimento do campo Movimentação
		S – Quando o declarante Tomador ou Prestador teve movimentação de 		documentos fiscais.
		N - Quando o declarante Tomador ou Prestador não teve movimentação 		de documentos fiscais.
Preenchimento do campo Tomador/Prestador
		P - Prestador
		T – Tomador
Se o declarante possuir lançamentos tanto como Tomador e Prestador no mesmo período o arquivo deverá conter dois registros 2 seguido de seus registros 3 respectivamente.

Para os campos que contém dados referentes a datas devem estar no formato DDMMAAAA (duas casas para o dia, duas casas para o mês e quatro casas para o ano). Isto também se aplica para os campos onde os componentes da data devem ser informados separadamente.
Para cada registro do tipo “2” deve existir 01 (um) ou mais registros do tipo “3”.
Quando o registro do tipo “2” for informado sem movimento os campos do registro tipo “3” alfanuméricos e datas deverão ser preenchidos com espaços vazios e os campos de formato valor da moeda devem vir preenchidos com zeros (0,00).
Os campos monetários devem sempre vir formatados com duas casas decimais.
 O campo deve vir preenchido com zeros à esquerda
  Neste campo deve vir sempre endereço de emails válidos. Quando houver mais de um endereço, os mesmos devem vir separados por ‘,’  (virgula).