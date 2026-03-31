# MTZ_ECF_BlocoN

> Fonte: MTZ_ECF_BlocoN.doc

THOMSON REUTERS

Geração do Bloco N


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		09/03/2018	MFS-17090	Criação do Documento	Alessandra Cristina Navatta		13/03/2018	MFS-17258	Liberação do Registro N615 	Alessandra Cristina Navatta		
 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc520716372" 1.	INTRODUÇÃO	 PAGEREF _Toc520716372 \h 3
 HYPERLINK \l "_Toc520716373" 2.	Regras de Negócio	 PAGEREF _Toc520716373 \h 3
 HYPERLINK \l "_Toc520716374" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc520716374 \h 3
 HYPERLINK \l "_Toc520716375" 2.2	Registros Identificadores	 PAGEREF _Toc520716375 \h 3
 HYPERLINK \l "_Toc520716376" 2.2.1	Registro N001: Abertura do Bloco N	 PAGEREF _Toc520716376 \h 6
 HYPERLINK \l "_Toc520716377" 2.2.2	Registro N030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real	 PAGEREF _Toc520716377 \h 6
 HYPERLINK \l "_Toc520716378" 2.2.3	Registro N500: Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos	 PAGEREF _Toc520716378 \h 9
 HYPERLINK \l "_Toc520716379" 2.2.4	Registro N600: Demonstração do Lucro da Exploração	 PAGEREF _Toc520716379 \h 10
 HYPERLINK \l "_Toc520716380" 2.2.5	Registro N610: CÁLCULO DA ISENÇÃO E REDUÇÃO DO IMPOSTO SOBRE LUCRO REAL	 PAGEREF _Toc520716380 \h 11
 HYPERLINK \l "_Toc520716381" 2.2.6	Registro N615: Informações da Base de Cálculo dos Incentivos Fiscais	 PAGEREF _Toc520716381 \h 12
 HYPERLINK \l "_Toc520716382" 2.2.7	Registro N620: CÁLCULO DO IRPJ MENSAL POR ESTIMATIVA	 PAGEREF _Toc520716382 \h 14
 HYPERLINK \l "_Toc520716383" 2.2.8	Registro N630: Cálculo do IRPJ Com Base no Lucro Real	 PAGEREF _Toc520716383 \h 15
 HYPERLINK \l "_Toc520716384" 2.2.9	Registro N650: Base de Cálculo da CSLL Após as Compensações da Base de Cálculo Negativa	 PAGEREF _Toc520716384 \h 16
 HYPERLINK \l "_Toc520716385" 2.2.10	Registro N660: Cálculo da CSLL Mensal por Estimativa	 PAGEREF _Toc520716385 \h 18
 HYPERLINK \l "_Toc520716386" 2.2.11	Registro N670: Cálculo da CSLL Com Base no Lucro Real	 PAGEREF _Toc520716386 \h 19
 HYPERLINK \l "_Toc520716387" 2.2.12	Registro N990: Encerramento do Bloco N	 PAGEREF _Toc520716387 \h 20

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO

Este bloco tem o objetivo de apresentar o Cálculo do IRPJ e da CSLL.
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-N	Período de recuperação dos registros: Data Inicial e Final do Período de Apuração informada na tela de Abertura da Apuração durante o Processamento em Lote.

Data Inicial e Data Final informadas da tela de Geração da ECF.

Só serão geradas informações neste bloco se o campo Forma de Tributação for “Lucro Real”. 

A exibição do conteúdo referente “Cód. do Registro” deve respeitar a sequência da coluna Código

Aplicar a RNG00051 - Geração dos Registros

Na tela de Perfil de geração o registro deve estar selecionado para a geração.

		MFS-17090		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		N001	1	Abertura do bloco N – Cálculo do IRPJ e da CSLL
	F	O	[1:1]		 HYPERLINK \l "N030" N030	2	Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real	F	OC
Obrigatório se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
 [1:13]
Senão
[0]		 HYPERLINK \l "N500" N500 	3	Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos	F	OC
Obrigatório se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
 [1:13]
Senão [0]		 HYPERLINK \l "N600" N600	3	Demonstração do Lucro da Exploração	F	OC
Obrigatório se
(N030.PER_APUR = “A00” OU [T01..T04] OU ([A01..A012])  E (mês correspondente  no 0010. MES_BAL_RED [1..12] = “B”) E
0020.IND_LUC_EXP  = “S”
N
Senão, não deve existir.	Se 
N030.PER_APUR = “A00” OU [T01..T04] OU ([A01..A012]  E mês correspondente  no 0010. MES_BAL_RED [1..12] = “B”) E
 0020.IND_LUC_EXP  = “S”
 [1:N]
Senão [0]		 HYPERLINK \l "N610" N610	3	Cálculo da Isenção e Redução do Imposto sobre Lucro Real	F	OC
Obrigatório se 
0020.IND_LUC_EXP  =  “S”
N
Não deve existir se 
N030.PER_APUR = [A01..A012] E mês correspondente  no 
0010. MES_BAL_RED[1..12] = “E”

	Se
N030.PER_APUR = [A01..A012] E mês correspondente  no 
0010. MES_BAL_RED [1..12] = “E”.
[0]
Senão Se 0020.IND_LUC_EXP  =  “S”
[1:N]
Senão [0:N]		N615	3	Informações da Base de Cálculo dos Incentivos Fiscais	F	OC
Obrigatório se 
Existir N030 E 0020.IND_FIN="S"
Exceto se 
N030.PER_APUR = [A01..A012] E mês correspondente  no 
0010. MES_BAL_RED [1..12] = “E”.
N
Senão, não deve existir.	Se 
N030 e 0020.IND_FIN="S"
Exceto se N030.PER_APUR = [A01..A012] E mês correspondente  no 0010. MES_BAL_RED [1..12] = “E”.
[1:1]
Senão [0]		 HYPERLINK \l "N620" N620	3	Cálculo do IRPJ Mensal por Estimativa	F	OC
Obrigatório se 
N030.PER_APUR = [A01..A12] 
N
Senão, não deve existir.	Se 
N030.PER_APUR = [A01..A12] 
[1:N] 
Senão 
[0]		N630	3	Cálculo do IRPJ Com Base no Lucro Real	F	OC
Obrigatório se
N030.PER_APUR = “A00” OU [T01..T04] 
N
Senão, não deve existir.	Se 
N030.PER_APUR = “A00” OU [T01..T04] 

 [1:N]
Senão [0]		HYPERLINK \l "N650"N650 	3	Base de Cálculo da CSLL Após Compensações das Bases de Cálculo Negativa	F	OC
Obrigatório se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
 [1:13]
Senão [0]		HYPERLINK \l "N660"N660	3	Cálculo da CSLL Mensal por Estimativa	F
	OC
Obrigatório se 
N030.PER_APUR = [A01..A12] 
N
Senão, não deve existir.	Se 
N030.PER_APUR = [A01..A12] 
[1:N] 
Senão 
[0]		HYPERLINK \l "N670"N670	3	Cálculo da CSLL Com Base no Lucro Real	F
	OC
Obrigatório se
N030.PER_APUR = “A00” OU [T01..T04] 
N
Senão, não deve existir.	Se 
N030.PER_APUR = “A00” OU [T01..T04] 

 [1:N]
Senão
[0]

		N990	1	Encerramento do Bloco N
	F	O	[1:1]		


Registro N001: Abertura do Bloco N
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGN001-01	REG – Tipo de Registro

Gerar fixo ‘N001’	Sim	MFS-17090		RNGN001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco N (registros N030,N500,N600, N610, N615, N620, N630, N650, N666, N670), preencher com “0”, caso contrário, preencher com “1”.
	Sim	MFS-17090		
Registro N030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real
Campo Chave: PER_APUR
Ocorrência: 0:13
Nível Hierárquico – 2

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGN030	
Só serão geradas informações neste bloco se o campo 05 – FORMA_TRIB do registro 0010 estiver preenchido com “1”,”2”,”3” ou “4” conforme RNP01 documento MTZ_Processamento_em_Lote.docx.

Forma de Tributação = ‘Anual’ 


Deverá ser gerado um registro N030 A00 e A01 à A12 conforme recuperação da RNP01 – para o Período da Apuração = “Anual”.


Forma de Tributação = ‘Trimestral’ 

Deverá ser gerado um registro N030 para cada abertura de apuração da escrituração, com forma de tributação = ‘Lucro Real’. Neste caso, o registro T01...T04 deverá ser criado de forma sequencial (T01....T04) considerando o ‘período de apuração’, onde:

1º  Trimestre = T01
2 º Trimestre = T02
3 º Trimestre = T03
4 º Trimestre = T04
		MFS-17090		RNGN030-01	REG – Tipo de Registro

Gerar fixo ‘N030’	Sim	MFS-17090		RNGN030-02	DT_INI - Data do Saldo Inicial 

A00, A01...A12 

Tipo de Receita da tela Abertura da Apuração = “Balanço Suspensão e Redução” ou Tipo (aba Tipo de Receita) da tela Abertura da Apuração = ‘Comparativo’ e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente.

Preencher este campo com a data inicial da primeira abertura de apuração encontrada no período parametrizado na tela de geração do ECF para o estabelecimento.
Exemplo: 
A02 - Data inicial: 01/01/2014

Tipo de Receita da tela Abertura da Apuração = “Receita Bruta” ou Tipo (aba Tipo de Receita) da tela Abertura da Apuração =  ‘Comparativo’ e Checkbox RECEITA BRUTA (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente.

Preencher este campo com a data inicial da abertura de apuração do período que está sendo gerado para o estabelecimento matriz/SCP.
Exemplo: 
A02 - Data inicial: 01/02/2014

T01...T04
Preencher este campo com a data inicial da abertura de apuração do período que está sendo gerado para o estabelecimento matriz/SCP.
Exemplo: 
T02 - Data inicial: 01/04/2014
	Sim	MFS-17090		RNGN030-03	DT_FIN- Data do Saldo Final


A00, A01...A12 e T01...T04

Preencher este campo com a data final da abertura de apuração do período que está sendo gerado para o estabelecimento matriz/SCP.

Exemplo: 
A02 - Data inicial: 28/02/2014T02 - Data final: 30/06/2014	Sim	MFS-17090		RNGN030-04	PER_APUR – Período de Apuração:

Preencher conforme RNGN030.	Sim	MFS-17090		
Registro N500: Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos
Campo Chave: REG
Ocorrência – 1:N
Nível Hierárquico – 3

Condições Gerais: 

Apresenta a base de cálculo do IRPJ após as compensações de prejuízos.

CÓD	DESCRIÇÃO	Obrig.	MFS		RNGN500	As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Recuperar os registros processados considerando a informação do campo Tipo de Receita (da Tela Abertura da Apuração), para as aberturas A01 a A12, ou seja , linha 1 (da importação de saldos, para o registro N500) quando Tipo de Receita = “Balanço Suspensão ou Redução” ou ‘Comparativo’ e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente, ou  linha 2 (da importação de saldos, para o registro N500) quando Tipo de Receita = ‘Receita Bruta’ ou ‘Comparativo’ e Checkbox RECEITA BRUTA (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente. Para as aberturas A00 e T01 a T04, considerar sempre a linha 1 (da importação de saldos, para o registro N500).
		MFS-17090		RNGN500-01	REG – Tipo de Registro

Gerar fixo ‘N500’	Sim	MFS-17090		RNGN500-02	CODIGO - Código de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Cód. do Registro” associados aos Registros N500.
	Sim	MFS-17090		RNGN500-03	DESCRICAO – Descrição de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Desc. do Registro” com base nos códigos recuperados pela  RNGN500-02.
	Não	MFS-17090		RNGN500-04	VALOR – Valor 

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGN500-02.	Não	MFS-17090		
Registro N600: Demonstração do Lucro da Exploração
Campo Chave: CÓDIGO
Ocorrência – 0:N
Nível Hierárquico – 3

Condições Gerais: 

Devem preencher este registro as pessoas jurídicas submetidas à apuração trimestral ou anual do imposto sobre a renda com base no lucro real que gozem de benefícios fiscais calculados com base no lucro da exploração.

CÓD	DESCRIÇÃO	Obrig.	MFS		RNGN600	As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Exibir na geração do arquivo, as informações que foram processadas pela RNP10, abaixo seguem os exemplos de como o arquivo deve ser apresentado: Se o campo Tipo de Receita da tela Abertura da Apuração for = “Receita Bruta” ou Tipo de Receita = ‘Comparativo’ e Checkbox RECEITA BRUTA (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente: Exibir apenas os dados da aba anual.
 
Se o campo Tipo de Receita da tela Abertura da Apuração for = “Balanço Suspensão ou Redução” ou Tipo de Receita = ‘Comparativo’ e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente:  
Exibir os dados de todos os meses que estão com essa parametrização, inclusive os dados da aba anual.

Forma de tributação = “T1 à T4”: Exibir os dados de todos os trimestres que estão com essa parametrização.
		MFS-17090		RNGN600-01	REG – Tipo de Registro

Gerar fixo ‘N600’	Sim	MFS-17090		RNGN600-02	CODIGO - Código de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Cód. do Registro” associados aos Registros N600.
	Sim	MFS-17090		RNGN600-03	DESCRICAO – Descrição de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Desc. do Registro” com base nos códigos recuperados pela  RNGN600-02.
	Não	MFS-17090		RNGN600-04	VALOR – Valor 

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGN600-02.	Não	MFS-17090		
Registro N610: CÁLCULO DA ISENÇÃO E REDUÇÃO DO IMPOSTO SOBRE LUCRO REAL
Campo Chave: CÓDIGO
Ocorrência – 1:N
Nível Hierárquico – 3

Condições Gerais: 

Este registro deve ser preenchido pelas pessoas jurídicas sujeitas à apuração do imposto de renda trimestral ou anual, que gozem dos benefícios fiscais de redução ou isenção desse imposto com base no lucro da exploração. 


CÓD	DESCRIÇÃO	Obrig.	MFS		RNGN610	As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Exibir na geração do arquivo, as informações que foram processadas pela RNP11, abaixo seguem os exemplos de como o arquivo deve ser apresentado: 
Se o campo Tipo de Receita (da Tela Abertura da Apuração) for = “Receita Bruta” ou Tipo de Receita = ‘Comparativo’ e Checkbox RECEITA BRUTA (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente: Exibir apenas os dados da aba anual.
 
Se o campo Tipo de Receita da Tela Abertura da Apuração for = “Balanço Suspensão ou Redução” ou Tipo de Receita = ‘Comparativo’ e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente:
Exibir os dados de todos os meses que estão com essa parametrização, inclusive os dados da aba anual.

Se Apuração = “Trimestral”: Exibir os dados de todos os trimestres que estão com essa parametrização.
		MFS-17090		RNGN610-01	REG – Tipo de Registro

Gerar fixo ‘N610’	Sim	MFS-17090		RNGN610-02	CODIGO - Código de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Cód. do Registro” associados aos Registros N610.
	Sim	MFS-17090		RNGN610-03	DESCRICAO – Descrição de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Desc. do Registro” com base nos códigos recuperados pela  RNGN610-02.
	Não	MFS-17090		RNGN610-04	VALOR – Valor 

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGN610-02.	Não	MFS-17090		
Registro N615: Informações da Base de Cálculo dos Incentivos Fiscais
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 3


CÓD	DESCRIÇÃO	MFS		RNGN615	

As informações a serem geradas neste registro terão como base a tabela resultado (tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.


Exibir na geração do arquivo, as informações que foram processadas pela RNP19, abaixo seguem os exemplos de como o arquivo deve ser apresentado: 
Se o campo Tipo de Receita (da Tela Abertura da Apuração) for = “Receita Bruta” ou Tipo de Receita = ‘Comparativo’ e Checkbox RECEITA BRUTA (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente: Exibir apenas os dados da aba anual.
 
Se o campo Tipo de Receita da Tela Abertura da Apuração for = “Balanço Suspensão ou Redução” ou Tipo de Receita = ‘Comparativo’ e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente:
Exibir os dados de todos os meses que estão com essa parametrização, inclusive os dados da aba anual.

Se Apuração = “Trimestral”: Exibir os dados de todos os trimestres que estão com essa parametrização.

	MFS-17258		RNGN615-01	REG – Tipo de Registro

Gerar fixo ‘N615’
	MFS-17258		RNGN615-02	BASE_CALC  Base de Cálculo

Considerar a Base de Cálculo da tela de Incentivos Fiscais
	MFS-17258		RNGN615-03	PER_INCEN_ FINOR – Percentual do incentivo FINOR (até 6%)
Considerar o Percentual do Incentivo FINOR da tela de Incentivos Fiscais
	MFS-17258		RNGN615-04	VL_LIQ_INCEN_ FINOR – Valor líquido do incentivo

Recuperar o conteúdo do campo Valor Líquido do Incentivo FINOR quando o valor informado for menor ou igual ao conteúdo do campo Valor Limite 6%.
	MFS-17258		RNGN615-05	PER_INCEN_ FINAM  – Percentual do incentivo FINAM (até 6%)

Considerar o Percentual do Incentivo Fiscal FINAM da tela de Incentivos Fiscais
	MFS-17258		RNGN615-06	VL_LIQ_INCEN_ FINAM – Valor líquido do incentivo

Recuperar o conteúdo do campo Valor Líquido do Incentivo FINAM quando o valor informado for menor ou igual ao conteúdo do campo Valor Limite 6%.

	MFS-17258		RNGN615-7	
VL_TOTAL – Total dos Incentivos

Considerar o Total de Incentivos tela de Incentivos Fiscais
	MFS-17258		
Registro N620: CÁLCULO DO IRPJ MENSAL POR ESTIMATIVA
Campo Chave: CÓDIGO
Ocorrência – 0:N
Nível Hierárquico – 3

Condições Gerais: 

Apresenta o cálculo do IRPJ mensal por estimativa.

CÓD	DESCRIÇÃO		MFS		RNGN620	As informações a serem geradas neste registro terão como base a tabela resultado do processamento (Tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Exibir na geração do arquivo, as informações que foram processadas pela RNP12, abaixo seguem os exemplos de como o arquivo deve ser apresentado: 
Se o campo Tipo de Receita (da Tela Abertura da Apuração) for = “Receita Bruta”, “Balanço Suspensão ou Redução” ou “Comparativo”: Exibir os dados de todos os meses que estão com essa parametrização, exceto os dados da aba anual.

Gerar apenas os registros cuja visão corresponda a escolha feita na tela conforme abaixo:

Tipo de Receita (da Tela Abertura da Apuração) for = Comparativo e Checkbox BALANÇO DE SUSPENSAO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura da Apuração correspondente então:
Recuperar as linhas do N620 geradas pela visão Balanço

Tipo de Receita (da Tela Abertura da Apuração) for = Comparativo e Checkbox RECEITA (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura da Apuração correspondente então:

Recuperar as linhas do N620 geradas para a visão Receita Bruta
		MFS-17090		RNGN620-01	REG – Tipo de Registro

Gerar fixo ‘N620’	Sim	MFS-17090		RNGN620-02	CODIGO - Código de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Cód. do Registro” associados aos Registros N620.
	Sim	MFS-17090		RNGN620-03	DESCRICAO – Descrição de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Desc. do Registro” com base nos códigos recuperados pela  RNGN620-02.
	Não	MFS-17090		RNGN620-04	VALOR – Valor 

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGN620-02.	Não	MFS-17090		

Registro N630: Cálculo do IRPJ Com Base no Lucro Real
Campo Chave: CÓDIGO
Ocorrência – 0:N
Nível Hierárquico – 3

Condições Gerais: 

Apresenta o cálculo do IRPJ com base no lucro real.

CÓD	DESCRIÇÃO	Obrig.	MFS		RNGN630	As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Exibir na geração do arquivo, as informações que foram processadas pela RNP13, abaixo seguem os exemplos de como o arquivo deve ser apresentado: 
Se o período de apuração for igual à A00, exibir os dados da Aba Anual.
Para a geração do T01 a T04, exibir todas as informações dos trimestres.

		MFS-17090		RNGN630-01	REG – Tipo de Registro

Gerar fixo ‘N630’	Sim	MFS-17090		RNGN620-02	CODIGO - Código de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Cód. do Registro” associados aos Registros N630.
	Sim	MFS-17090		RNGN630-03	DESCRICAO – Descrição de acordo com tabela publicada no Sped.

Recuperar o conteúdo do campo “Desc. do Registro” com base nos códigos recuperados pela  RNGN630-02.
	Não 	MFS-17090		RNGN630-04	VALOR – Valor 

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGN630-02.	Não	MFS-17090		
Registro N650: Base de Cálculo da CSLL Após as Compensações da Base de Cálculo Negativa
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 3

Condições Gerais: 

Apresenta a base de cálculo da CSLL, após as compensações da base de cálculo negativa
CÓD	DESCRIÇÃO	OBRIG	MFS		RNGN650	As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Verificar Regra RNP14

Recuperar os registros processados considerando a informação do campo Tipo de Receita ( da Tela Abertura da Apuração), para as aberturas A01 a A12, ou seja , linha 1 (da importação de saldos, para o registro N650) quando Tipo de Receita = “Balanço Suspensão ou Redução” ou “Comparativo” e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente, ou  linha 2 (da importação de saldos, para o registro N650) quando Tipo de Receita = “Receita Bruta” ou “Comparativo” e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente. Para as aberturas A00 e T01 a T04, considerar sempre a linha 1 (da importação de saldos, para o registro N650).
		MFS-17090		RNGN650-01	REG – Tipo de Registro

Gerar fixo ‘N650’	Sim	MFS-17090		RNGN650-02	CODIGO - Código 

Recuperar o conteúdo do campo “Cód. do Registro” associados aos Registros N650.

	Sim	MFS-17090		RNGN650-03	DESCRICAO – Descrição 

Recuperar o conteúdo do campo “Desc. do Registro” com base nos códigos recuperados pela  RNGN650-02.

	Não	MFS-17090		RNGN650-04	VALOR – Valor 

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGN650-02.
	Não	MFS-17090		
Registro N660: Cálculo da CSLL Mensal por Estimativa
Campo Chave: CODIGO
Ocorrência – 0:N
Nível Hierárquico – 3

Condições Gerais: 

Este registro é habilitado para a pessoa jurídica que apurou o imposto de renda com base no lucro real anual que optou por apurar a CSLL por estimativa mensal

CÓD	DESCRIÇÃO	OBRIG	MFS		RNGN660	As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Exibir na geração do arquivo, as informações que foram processadas pela RNP15, abaixo seguem os exemplos de como o arquivo deve ser apresentado: 
Se o campo Tipo de Receita (da Tela Abertura da Apuração) for = “Receita Bruta”, “Balanço Suspensão ou Redução” ou “Comparativo”: Exibir os dados de todos os meses que estão com essa parametrização, exceto os dados da aba anual.

Gerar apenas os registros cuja visão corresponda a escolha feita na tela conforme abaixo:

Tipo de Receita (da Tela Abertura da Apuração) for = Comparativo e  Checkbox BALANÇO DE SUSPENSAO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura da Apuração correspondente então:
Recuperar as linhas do N660 geradas pela visão Balanço

Tipo de Receita (da Tela Abertura da Apuração) for = Comparativo e  Checkbox RECEITA (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura da Apuração correspondente então:

Recuperar as linhas do N660 geradas para a visão Receita Bruta
		MFS-17090		RNGN660-01	REG – Tipo de Registro

Gerar fixo ‘N660’	Sim	MFS-17090		RNGN660-02	CODIGO - Código 

Recuperar o conteúdo do campo “Cód. do Registro” associados aos Registros N660.

	Sim	MFS-17090		RNGN660-03	DESCRICAO – Descrição 

Recuperar o conteúdo do campo “Desc. do Registro” com base nos códigos recuperados pela  RNGN660-02.

	Não	MFS-17090		RNGN660-04	VALOR – Valor 

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGN660-02.

	Não	MFS-17090		


Registro N670: Cálculo da CSLL Com Base no Lucro Real
Campo Chave: CODIGO
Ocorrência – 0:N
Nível Hierárquico – 3

Condições Gerais: 

Este registro apresenta o cálculo da CSLL com base no lucro real.

CÓD	DESCRIÇÃO		MFS		RNGN670	As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela Lucro Real) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Exibir na geração do arquivo, as informações que foram processadas pela RNP16, abaixo seguem os exemplos de como o arquivo deve ser apresentado: 
Se o período de apuração for igual à A00, exibir os dados da Aba Anual. 
Para a geração do T01 a T04, exibir todas as informações dos trimestres.
		MFS-17090		RNGN670-01	REG – Tipo de Registro

Gerar fixo ‘N670’	Sim	MFS-17090		RNGN670-02	CODIGO - Código 

Recuperar o conteúdo do campo “Cód. do Registro” associados aos Registros N670.

	Sim	MFS-17090		RNGN670-03	DESCRICAO – Descrição 

Recuperar o conteúdo do campo “Desc. do Registro” com base nos códigos recuperados pela  RNGN670-02.

	Não	MFS-17090		RNGN670-04	VALOR – Valor 

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGN670-02.

	Não	MFS-17090		
Registro N990: Encerramento do Bloco N
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 1

Condições Gerais: 


CÓD	DESCRIÇÃO	MFS		RNGN990-01	REG – Tipo de Registro

Gerar fixo ‘N990’	MFS-17090		RNGN990-02	QTD_LIN – Quantidade Total de Registro do Bloco N

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco N e informar o total.
Considerando que Campo 1: Texto fixo contendo "N990", e campo 2: Quantidade total de linhas do bloco N.

Exemplo: |N990|25|	MFS-17090		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN