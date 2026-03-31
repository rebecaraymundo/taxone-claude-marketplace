# MTZ_ECF_BlocoM

> Fonte: MTZ_ECF_BlocoM.doc

THOMSON REUTERS

Geração do Bloco M


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		12/03/2018	MFS-17089	Criação do Documento	Alessandra Cristina Navatta		
 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc510007804" 1.	INTRODUÇÃO	 PAGEREF _Toc510007804 \h 3
 HYPERLINK \l "_Toc510007805" 2.	Regras de Negócio	 PAGEREF _Toc510007805 \h 3
 HYPERLINK \l "_Toc510007806" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc510007806 \h 3
 HYPERLINK \l "_Toc510007807" 2.2	Registros Identificadores	 PAGEREF _Toc510007807 \h 3
 HYPERLINK \l "_Toc510007808" 2.2.1	Registro M001: Abertura do Bloco M	 PAGEREF _Toc510007808 \h 7
 HYPERLINK \l "_Toc510007809" 2.2.2	Registro M010: IDENTIFICAÇÃO DA CONTA NA PARTE B DO e-LALUR E DO e-LACS	 PAGEREF _Toc510007809 \h 7
 HYPERLINK \l "_Toc510007810" 2.2.3	Registro M030: IDENTIFICAÇÃO DOS PERÍODOS E FORMAS DE APURAÇÃO DO IRPJ E DA CSLL DAS EMPRESAS TRIBUTADAS PELO LUCRO REAL	 PAGEREF _Toc510007810 \h 9
 HYPERLINK \l "_Toc510007811" 2.2.4	Registro M300: LANÇAMENTOS DA PARTE A DO e-LALUR	 PAGEREF _Toc510007811 \h 12
 HYPERLINK \l "_Toc510007812" 2.2.5	Registro M305: CONTA DA PARTE B DO e-LALUR	 PAGEREF _Toc510007812 \h 14
 HYPERLINK \l "_Toc510007813" A partir da versão 3.00 CONTAS DA PARTE B RELACIONADAS AO LANÇAMENTO DA PARTE A DO E-LALUR	 PAGEREF _Toc510007813 \h 14
 HYPERLINK \l "_Toc510007814" 2.2.6	Registro M310: CONTAS CONTABEIS RELACIONADAS AO LANÇAMENTO DA PARTE A DO e-LALUR	 PAGEREF _Toc510007814 \h 15
 HYPERLINK \l "_Toc510007815" 2.2.7	Registro M312: Números dos Lançamentos Relacionados à Conta Contábil	 PAGEREF _Toc510007815 \h 17
 HYPERLINK \l "_Toc510007816" 2.2.8	Registro M315: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento	 PAGEREF _Toc510007816 \h 17
 HYPERLINK \l "_Toc510007817" 2.2.9	Registro M350: LANÇAMENTOS DA PARTE A DO e-LACS	 PAGEREF _Toc510007817 \h 18
 HYPERLINK \l "_Toc510007818" 2.2.10	Registro M355: Conta da Parte B do e-Lacs	 PAGEREF _Toc510007818 \h 20
 HYPERLINK \l "_Toc510007819" 2.2.11	Registro M360: Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lacs	 PAGEREF _Toc510007819 \h 22
 HYPERLINK \l "_Toc510007820" 2.2.12	Registro M362: Números dos Lançamentos Relacionados à Conta Contábil	 PAGEREF _Toc510007820 \h 23
 HYPERLINK \l "_Toc510007821" 2.2.13	Registro M365: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento	 PAGEREF _Toc510007821 \h 24
 HYPERLINK \l "_Toc510007822" 2.2.14	Registro M410: LANÇAMENTOS NA CONTA DA PARTE “B” DO e-LALUR e do e-LACS SEM REFLEXO NA PARTE A	 PAGEREF _Toc510007822 \h 25
 HYPERLINK \l "_Toc510007823" 2.2.15	Registro M415: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento	 PAGEREF _Toc510007823 \h 27
 HYPERLINK \l "_Toc510007824" 2.2.16	Registro M990: Encerramento do Bloco M	 PAGEREF _Toc510007824 \h 28

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO
Livro Eletrônico de Apuração do Lucro Real (e-Lalur) e Livro Eletrônico de Apuração da Base de Cálculo da CSLL (e-Lacs).
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-M	Período de recuperação dos registros: Data Inicial e Final do Período de Apuração informada na tela de Abertura da Apuração durante o Processamento em Lote.

Data Inicial e Data Final informadas da tela de Geração da ECF.

Só serão geradas informações neste bloco se o campo Forma de Tributação for “Lucro Real” da tela informações do ECF.

Saldos das Contas da Parte B

Tabela de Lançamento da Parte A

Tabela de Ajustes da Parte B

- A exibição do conteúdo referente “Cód. do Registro” deve respeitar a sequência da coluna Ordem.

-  Aplicar a RNG00051 – Geração dos Registros

-Na tela de Perfil de geração o registro deve estar selecionado para a geração.
		MFS-17089		
Registros Identificadores
Relação de Registros a serem gerados:

		Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência
		M001	1	Abertura do Bloco M – Livro Eletrônico de Apuração do Lucro Real (e-Lalur) e Livro Eletrônico de Apuração da Base de Cálculo da CSLL (e-Lacs)	F	O	[1:1]		 HYPERLINK \l "RL010" M010	2	Identificação da Conta na Parte B e-Lalur e do e-Lacs	F	OC
Obrigatório se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
[0:N]
Senão
[0]		 HYPERLINK \l "RL030" M030	2	Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real 	F	OC
Obrigatório se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
N
Senão, não deve existir.
	Se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
 [1:13]
Senão
[0]		 HYPERLINK \l "M300" M300	3	Lançamentos da Parte A do e-Lalur	F	OC
Obrigatório se 
0010. FORMA_TRIB_PER = “R” ou “E”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB_PER = “R” ou “E” 
[1:N]
Senão
[0] 		 HYPERLINK \l "M305" M305	4	Até versão 2.00:

Conta da Parte B do e-Lalur

A partir da versão 3.00:

Contas da Parte B Relacionadas ao Lançamento da Parte A do e-Lalur	F	OC
Obrigatório se 
M300.IND_RELACAO = “1” ou “3”
N
Senão, não deve existir.


	Se 
M300.IND_RELACAO = “1” ou “3”
[1:N]
Senão
[0]		 HYPERLINK \l "M310" M310	4	Até versão 2.00:

Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lalur.

A partir da versão 3.00:

Contas Contábeis Relacionadas ao Lançamento da Parte A
do e-Lalur	F
	OC
Obrigatório se 
M300.IND_RELACAO = “2” ou “3”
N
Senão, não deve existir.	Se 
M300.IND_RELACAO = “2” ou “3”
[1:N]
Senão
[0]		 HYPERLINK \l "M312" M312	5	Números dos Lançamentos Relacionados à Conta Contábil	F	OC
Obrigatório se 
M310.VL_CTA < M300.VR_LAN_LAL
M310.VL_CTA < K155.VL_SLD_FIN; ou 
M310.VL_CTA < (K155.VL_SLD_FIN – K155.VL_SLD_INI); ou 
M310.VL_CTA < K155.VL_DEB; ou 
M310.VL_CTA < K155.VL_CRED
N
Senão, não deve existir.	Se 
M310.VL_CTA < M300.VR_LAN_LAL
M310.VL_CTA < K155.VL_SLD_FIN; ou 
M310.VL_CTA < (K155.VL_SLD_FIN – K155.VL_SLD_INI); ou 
M310.VL_CTA < K155.VL_DEB; ou 
M310.VL_CTA < K155.VL_CRED.
[1:N]
Senão
[0]		 HYPERLINK \l "L315" M315	4	Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento	F	F	[0:N]		 HYPERLINK \l "M350" M350	3	Lançamentos da Parte A do e-Lacs	F	OC
Obrigatório se 
0010. FORMA_TRIB_PER = “R” ou “E”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB_PER = “R” ou “E” 
[1:N]
Senão
[0] 		 HYPERLINK \l "M355" M355	4	Até versão 2.00:

Conta da Parte B do e-Lacs

A partir da Versão 3.00: 
Contas da Parte B Relacionadas ao Lançamento da Parte A do e-Lacs
	F	OC
Obrigatório se 
M350.IND_RELACAO = “1” ou “3”
N
Senão, não deve existir.	Se 
M350.IND_RELACAO = “1” ou “3”
[1:N]
Senão
[0]		 HYPERLINK \l "M310" M360	4	Até versão 2.00:

Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lacs.

A partir da versão 3.00:
Contas Contábeis Relacionadas ao Lançamento da Parte A
do e-Lacs	F
	OC
Obrigatório se 
M350.IND_RELACAO = “2” ou “3”
N
Senão, não deve existir.	Se 
M350.IND_RELACAO = “2” ou “3”
[1:N]
Senão
[0]		 HYPERLINK \l "M362" M362	5	Números dos Lançamentos Relacionados à Conta Contábil	F	Até versão 2.00:

OC
Obrigatório se 
M360.VL_CTA < M350.VR_LAN_LAL
M360.VL_CTA < K155.VL_SLD_FIN; ou 
M360.VL_CTA < (K155.VL_SLD_FIN – K155.VL_SLD_INI); ou 
M360.VL_CTA < K155.VL_DEB; ou 
M360.VL_CTA < K155.VL_CRED.
N
Senão, não deve existir.

A partir da versão 3.00

F	Até versão 2.00

Se 
M360.VL_CTA < M350.VR_LAN_LAL
M360.VL_CTA < K155.VL_SLD_FIN; ou 
M360.VL_CTA < (K155.VL_SLD_FIN – K155.VL_SLD_INI); ou 
M360.VL_CTA < K155.VL_DEB; ou 
M360.VL_CTA < K155.VL_CRED.
[1:N]
Senão
[0]

A partir da versão 3.00


[0:N]		 HYPERLINK \l "M365" M365	4	Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento	F	F	[0:N]		 HYPERLINK \l "M410"  M410	3	Lançamentos na Conta da Parte B do e-Lalur e do e-Lacs Sem Reflexo na Parte A	F	F	 [0:N]
 		 HYPERLINK \l "M415" M415	4	Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento	F	F	[0:N]		M990	1	Encerramento do Bloco M	F	O	[1:1]		

Registro M001: Abertura do Bloco M
Campo(s) chave: REG 
Ocorrência – 1:1
Nível Hierárquico – 1
Considerações Gerais:

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM001-01	REG – Tipo de Registro

Gerar fixo ‘M001’	Sim	MFS-17089		RNGM001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco M (registros M010, M030, M300, M305, M3010, M312, M315 M350, M355, M360, M362, M365, M410, M415, M500), preencher com “0”, caso contrário, preencher com “1”.
	Sim	MFS-17089 		

Registro M010: IDENTIFICAÇÃO DA CONTA NA PARTE B DO e-LALUR E DO e-LACS
Campo(s) chave: COD_CTA_B + TRIBUTO 
Ocorrência – 0:N

Considerações Gerais:

As informações a serem geradas neste registro terão como base os campos e rotinas definidas na tela Saldos das Contas da Parte B.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM010	As informações a serem geradas neste registro terão como base os campos e rotinas definidas na tela Saldos das Contas da Parte B e informações do ECF.

Seleção dos registros da tabela de Saldos das Contas da Parte B:

Recuperar todas as contas que possuem saldos na tela de Saldos das Contas da Parte B utilizando para base de seleção o Exercício e Data Inicial informados para a Escrituração (tela de Informações ECF).
	- 	MFS-17089		RNGM010-01	REG - Tipo de Registro

Gerar fixo “M010”.
	Sim	MFS-17089		RNGM010-02	COD_CTA_B - Código da conta da Parte B

Recuperar o código da Conta da Parte B.	Sim	MFS-17089		RNGM010-03	DESC_CTA_LAL- Descrição

Recuperar a Descrição da Conta da Parte B RNGM010-02.	Sim	MFS-17089		RNGM010-04	DT_AP_LAL - Data de Criação

Recuperar a data Validade (Data Inicial) da conta da parte B.
	Sim	MFS-17089		RNGM010-05	COD_LAN_ORIG - Código do Lançamento de Origem da Conta

Gerar com o código da Linha da tela Saldos das Contas da Parte B.
	Não	MFS-17089		RNGM010-06	DESC_LAN_ORIG - Descrição do Tipo de Lançamento

Gerar com a Descrição da Linha da tela Saldos das Contas da Parte B.	Não	MFS-17089		RNGM010-07	DT_LIM_LAL - Data Limite para a Exclusão, Adição ou Compensação do Valor Controlado.

Recuperar a data Validade (Data final) da conta da parte B.	Não	MFS-17089		RNGM010-08	COD_TRIBUTO - Tipo de Tributo

Se para a conta recuperada pela RNGM010-02 o campo “Tipo de Tributo” estiver preenchido com:

“I – Imposto de Renda Pessoa Jurídica”, gerar “I”.

“C – Contribuição Social sobre o Lucro Líquido”, gerar “C”.
	Sim	MFS-17089		RNGM010-09	VL_SALDO_INI - Saldo Inicial


Se a data recuperada pela RNGM010-04 estiver dentro da Data Inicial e Data Final informada na tela geração da ECF, gerar 0, caso contrário, recuperar o conteúdo do campo “Saldo Inicial” da conta cadastrada.	Sim	MFS-17089		RNGM010-10	IND_Vl_SALDO_INI - Indicador do Saldo Inicial

Recuperar o indicador do saldo correspondente ao campo recuperado pela RNGM010-09

Se o valor do campo Vl_SALDO_INI for igual a 0, gravar “C”.	Sim	MFS-17089		RNGM010-11	CNPJ_SIT_ESP – CNPJ

Recuperar o conteúdo do campo “CNPJ Origem”.	Não	MFS-17089		
Registro M030: IDENTIFICAÇÃO DOS PERÍODOS E FORMAS DE APURAÇÃO DO IRPJ E DA CSLL DAS EMPRESAS TRIBUTADAS PELO LUCRO REAL
Campo(s) chave: PER_APUR
Ocorrência – 0:13

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM030	Só serão geradas informações neste bloco se o campo 05 – FORMA_TRIB do registro 0010 estiver preenchido com “1”, ”2”, ”3” ou “04” conforme RNP01 documento MTZ_Processamento_em_Lote.docx.  

Forma de Tributação = ‘Anual’ 


Deverá ser gerado um registro M030 A01 à A12 conforme recuperação da RNP01 – para o Período da Apuração = “Anual” e parâmetro Tipo (aba Tipo de Receita) da tela Complementares = ‘Balanço Suspensão ou Redução’ ou Tipo (aba Tipo de Receita) da tela Complementares = ‘Comparativo’ e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado para a Abertura de Apuração correspondente. Neste caso, o registro A01...A12 deverá ser criado considerando o ‘período de apuração’ seguindo ordem cronológica (Janeiro a Dezembro), onde:

Janeiro = A01
Fevereiro = A02
Março = A03
.
.
.
Dezembro = A12.


Deverá ser gerado um registro M030 A00 conforme recuperação da RNP01 – para o Período da Apuração = “Anual”, utilizando como base os valores do último período calculado no processamento em lote (status da abertura da apuração igual a “Cálculo Realizado”), independente do tipo de receita informado na tela Complementares e da origem de geração do registro (processamento ou tela).

Forma de Tributação = ‘Trimestral’ 

Deverá ser gerado um registro M030 para cada abertura de apuração da escrituração, com forma de tributação = ‘Lucro Real’. Neste caso, o registro T01...T04 deverá ser criado considerando o ‘período de apuração’ seguindo ordem cronológica (1º a 4º trimestre), onde:

1º Trimestre = T01
2 º Trimestre = T02
3 º Trimestre = T03
4 º Trimestre = T04

	Sim	MFS-17089 		RNGM030-01	REG – Tipo de Registro

Gerar fixo ‘M030’	Sim	MFS-17089		RNGM030-02	DT_INI - Data do Saldo Inicial 

A00, A01...A12 
Preencher este campo com a data inicial da primeira abertura de apuração encontrada no período parametrizado na tela de geração do ECF para o estabelecimento.
Exemplo: 
A02 - Data inicial: 01/01/2014

T01...T04
Preencher este campo com a data inicial da abertura de apuração do período que está sendo gerado para o estabelecimento.

Exemplo: 
T02 - Data inicial: 01/04/2014

	Sim	MFS-17089		RNGM030-03	DT_FIN- Data do Saldo Final

A00, A01...A12 e T01...T04

Preencher este campo com a data final da abertura de apuração do período que está sendo gerado para o estabelecimento.

Exemplo: 
A02 - Data final: 28/02/2014
T02 - Data final: 30/06/2014
	Sim	MFS-17089		RNGM030-04	PER_APUR – Período de Apuração:

Preencher conforme RNGM030.	Sim	MFS-17089		Registro M300: LANÇAMENTOS DA PARTE A DO e-LALUR 
Campo(s) chave: CODIGO
Ocorrência – 1:N
Nível Hierárquico – 3

Considerações Gerais:

Apresenta os lançamentos da parte A do e-LALUR. Este registro demonstrará a apuração da base de cálculo da IRPJ anual, trimestral e nos meses com estimativa apurada com base no balanço/balancete.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM300	Para a geração deste registro, recuperar informações conforme abaixo:

Recuperar da tabela de resultado do processamento (tela de demonstração de resultado do processamento dos registros) das apurações processadas pela rotina de processamentos em lote conforme o documento MTZ_Processamento_em_Lote.docx com base na RNP17.

As informações recuperadas também poderão ser identificadas pela tabela de lançamentos da parte A.	-	MFS-17089 		RNGM300-01	REG – Tipo de Registro

Gerar fixo ‘M300’
	Sim	MFS-17089		RNGM300-02	CODIGO- Código do Lançamento

Recuperar da tabela de resultado do processamento o o Códígo do Registro/Linha associados aos Registros M300A, M300B e M300C. que possuam os tipos de lançamentos válidos para recuperação conforme RNGM300-04.
	Não	MFS-17089		RNGM300-03	DESCRICAO- Descrição

Recuperar da tabela de resultado do processamento o conteúdo do campo “Códígo do Registro/Linha” com base nos códigos recuperados pela  RNGM300-02.
	Não	MFS-17089		RNGM300-04	TIPO_LANCAMENTO - Tipo de Lançamento

Recuperar o tipo de lançamento corresponde a cada Cód. do Registro recuperado pela RNGM300-02.

Tipos válidos para a recuperação:

A- Adição
E - Exclusão.
P - Compensação de Prejuízo
L - Lucro

	Não	MFS-17089		RNGM300-05	IND_RELACAO - Tipo de Relacionamento

Recuperar o conteúdo do campo “Tipo de Relacionamento” o tipo correspondente a cada Cód. do Registro recuperado pela RNGM300-02.

Tipos Válidos para recuperação:

1 - Com Conta da Parte B
2 - Com Conta Contábil
3 – Com Conta da parte B e Conta Contábil
4 - Sem Relacionamento
	Não	MFS-17089		RNGM300-06	VALOR – Valor

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGM300-02 e que possuam os tipos de lançamento recuperados pela RNGM300-04.
	Não	MFS-17089		RNGM300-07	HIST_LAN_LAL- Histórico do lançamento no e-Lalur

Recuperar o conteúdo do campo “Histórico” a informação correspondente se houver, para cada Cód. do Registro recuperado pela RNGM300-02.	Não	MFS-17089		Registro M305: CONTA DA PARTE B DO e-LALUR
A partir da versão 3.00 CONTAS DA PARTE B RELACIONADAS AO LANÇAMENTO DA PARTE A DO E-LALUR
Campo(s) chave: COD_CTA_B
Ocorrência – 0:N
Nível Hierárquico – 4

Considerações Gerais:
Relacionamento do lançamento da parte A do e-Lalur com a conta da parte B do e-Lalur.


CÓD	DESCRIÇÃO	
OBRIG		RNGM305
	Para a geração deste registro, recuperar os lançamentos da parte A que possuam Tipo de Relacionamento = 1 - Com Conta da Parte B ou 3 – Com Conta da parte B e Conta Contábil conforme RNGM300-05.

	-	MFS-17089		RNGM305-01	REG – Tipo de Registro

Gerar fixo ‘M305’	Sim	MFS-17089		RNGM305-02	COD_CTA_B - Código da Conta da Parte B

Recuperar a contas da parte B utilizando os mesmos critérios de recuperação executado pela RNGM010-02 para o “Tipo de Tributo” conforme RNGM010-08 igual a “I – Imposto de Renda Pessoa Jurídica”, gerar “I”.	
Sim	MFS-17089		RNGM305-03	VL_CTA - Valor Total dos Lançamentos
Para cada conta recuperada pela RNGM305-02, recuperar o “Valor a Considerar” dos registros cujo campo origem seja igual a parte A .	

Sim	MFS-17089		RNGM305-04	IND_ VL_CTA - Indicador do Lançamento

Exibir o indicador identificado pela RNGM305-03.

	


Sim	MFS-17089		
Registro M310: CONTAS CONTABEIS RELACIONADAS AO LANÇAMENTO DA PARTE A DO e-LALUR
A partir da versão 3.00: CONTAS CONTÁBEIS RELACIONADAS AO LANÇAMENTO DA PARTE A DO E-LALUR

Campo(s) chave: COD_CTA + COD_CCUS
Ocorrência – 0:N
Nível Hierárquico – 4

Considerações Gerais:

Relaciona os lançamentos da parte A do e-Lalur com as contas contábeis.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM310
	Para a geração deste registro, recuperar informações conforme abaixo:

Recuperar de lançamentos da parte A que possuam Tipo de Relacionamento = 2 - Com Conta Contábil ou 3 – Com Conta da parte B e Conta Contábil conforme RNGM300-05 na aba Contas Contábeis da tabela de lançamentos da parte A conforme o documento MTZ_Processamento_em_Lote.docx com base na RNP20.
Verificar se a Conta Contábil recuperada possui parametrização de Lançamento de Adição e Exclusão da Tela Recuperação dos Valores - Apuração IRPJ/CSLL diferente de “Não se Aplica” ou Nulo. Caso positivo, deve ser gerado o Registro M310 apenas para a linha da parte A que recebeu valor na opção entre Adição ou Exclusão.

As informações recuperadas também poderão ser identificadas na aba Contas Contábeis da tabela de lançamentos da parte A.

	-	MFS-17089		RNGM310-01	REG – Tipo de Registro

Gerar fixo ‘M310’
	Sim	MFS-17089		RNGM310-02	COD_CTA - Código de Conta Contábil

Recuperar o conteúdo do campo “Conta Contábil” código de cada conta contábil.	Sim	MFS-17089		RNGM310-03	COD_CCUS - Código do Centro de Custos

Recuperar o conteúdo do campo “Centro Custos” se houver para cada código da conta contábil recuperada pela RNGM310-02.	Não	MFS-17089		RNGM310-04	VL_CTA - Valor da Conta
Recuperar o conteúdo do campo “Saldo” de cada código de conta contábil recuperado pela RNGM310-02
	
Sim	MFS-17089		RNGM310-05	IND_VL_CTA - Indicador do Saldo da Conta

Recuperar o conteúdo do campo “IND” de cada saldo recuperado pela RNGM310-04.
	
Sim	MFS-17089 MFS-17089 		
Registro M312: Números dos Lançamentos Relacionados à Conta Contábil
Campo(s) chave: NUM_LCTO
Ocorrência – 0:N
Nível Hierárquico – 5
Considerações Gerais:

Apresenta o número dos lançamentos contábeis relacionados ao lançamento da conta da parte A.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM312
	Para a geração deste registro, recuperar conforme RNGM310-02 informações da tabela de lançamentos da parte A que possuam informações de Lançamentos Contábeis na aba Contas Contábeis.

	-	MFS-17089		RNGM312-01	REG – Tipo de Registro

Gerar fixo ‘M312’
	Sim	MFS-17089		RNGM312-02	NUM_LCTO – Número do Lançamento

Recuperar o conteúdo do campo “Número do Lançamento”.	Sim	MFS-17089		
Registro M315: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento 
Campo(s) chave: IND_PROC + NUM_PROC
Ocorrência – 0:N
Nível Hierárquico – 4

Considerações Gerais:

Identifica os processos judiciais e administrativos utilizados que embasaram adições menores que as previstas na legislação ou falta de adição e exclusões maiores que as previstas na legislação na parte A do e-Lalur (tratamento diverso do regramento fiscal). 

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM315
	Para a geração deste registro, recuperar informações da tabela de lançamentos da parte A conforme RNGM300-05 que possuam informações de Processos Judiciais na aba Processos da tabela de lançamentos da parte A.

	-	MFS-17089		RNGM315-01	REG – Tipo de Registro

Gerar fixo ‘M315’
	Sim	MFS-17089		RNGM315-02	IND_PROC - Tipo do Processo

Recuperar o conteúdo do campo “Tipo de Processo”.

Se na tela estiver selecionada a opção “Judicial”, gerar “1”.
Se estiver selecionada opção “Administrativo”, gerar “2”.
	Sim	MFS-17089		RNGM315-03	NUM_PROC – Número do Processo

Recuperar o conteúdo do campo “Número do Processo” de acordo com o tipo o processo recuperado pela RNGM315-02.	Sim	MFS-17089		
Registro M350: LANÇAMENTOS DA PARTE A DO e-LACS
Campo(s) chave: CODIGO
Ocorrência – 1:N
Nível Hierárquico – 3

Considerações Gerais:

Apresenta os lançamentos da parte A do e-Lacs. Este registro demonstrará a apuração da base de cálculo da CSLL anual, trimestral e nos meses com estimativa apurada com base no balanço/balancete.
CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM350	Para a geração deste registro, recuperar informações conforme abaixo:

Recuperar da tabela de resultado do processamento (tela de demonstração de resultado do processamento dos registros) das apurações processadas pela rotina de processamentos em lote conforme o documento MTZ_Processamento_em_Lote docx com base na RNP18.

As informações recuperadas também poderão ser identificadas pela tabela de lançamentos da parte A.	-	MFS-17089		RNGM350-01	REG – Tipo de Registro

Gerar fixo ‘M350’
	Sim	MFS-17089		RNGM350-02	CODIGO- Código do Lançamento

Recuperar da tabela de resultado do processamento o Códígo do Registro/Linha associados aos Registros M350A, M350B e M350C que possuam os tipos de lançamentos válidos para recuperação conforme RNGM350-04

	Não	MFS-17089		RNGM350-03	DESCRICAO- Descrição

Recuperar da tabela de resultado do processamento a descrição do campo “Códígo do Registro/Linha” com base nos códigos recuperados pela RNGM350-02.
	Não	MFS-17089		RNGM350-04	TIPO_LANCAMENTO - Tipo de Lançamento

Recuperar o tipo de lançamento corresponde a cada Cód. do Registro recuperado pela RNGM350-02.

Tipos válidos para a recuperação:

A- Adição
E - Exclusão.
P - Compensação de Prejuízo
L – Lucro
	Não	MFS-17089		RNGM350-05	IND_RELACAO - Tipo de Relacionamento

Recuperar o conteúdo do campo “Tipo de Relacionamento” o tipo correspondente a cada Cód. do Registro recuperado pela RNGM350-02.

Tipos Válidos para recuperação:

1 - Com Conta da Parte B
2 - Com Conta Contábil
3 – Com Conta da parte B e Conta Contábil
4 - Sem Relacionamento
	Não	MFS-17089		RNGM350-06	VALOR – Valor

Recuperar o conteúdo do campo “Valor” para cada Cód. do Registro recuperado pela RNGM350-02 e que possuam os tipos de lançamento recuperados pela RNGM350-04.
	Não	MFS-17089		RNGM350-07	HIST_LAN_LAL- Histórico do lançamento no e-Lacs

Recuperar o conteúdo do campo “Histórico” a informação correspondente se houver, para cada Cód. do Registro recuperado pela RNGM350-02.	Não	MFS-17089		
Registro M355: Conta da Parte B do e-Lacs
A partir da versão 3.00: Contas da Parte B Relacionadas ao Lançamento da Parte A do e-Lacs


Campo(s) chave: COD_CTA_B
Ocorrência – 0:N
Nível Hierárquico – 4

Considerações Gerais:

Relacionamento do lançamento da parte A do e-Lacs com a conta da parte B do e-Lacs.


CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM355
	Para a geração deste registro, recuperar informações da tabela de lançamentos da parte A que possuam Tipo de Relacionamento = 1 - Com Conta da Parte B ou 3 – Com Conta da parte B e Conta Contábil conforme RNGM350-05.
	-	MFS-17089		RNGM355-01	REG – Tipo de Registro

Gerar fixo ‘M355’
	Sim	MFS-17089		RNGM355-02	COD_CTA_B - Código da Conta da Parte B

Recuperar a contas da parte B utilizando os mesmos critérios de recuperação executado pela RNGM010-02 para o “Tipo de Tributo” conforme RNGM010-08 igual a “C – Contribuição Social sobre o Lucro Líquido”, gerar “C”.
	
Sim	MFS-17089		RNGM355-03	VL_CTA - Valor Total dos Lançamentos

Para cada conta recuperada pela RNGM355-02, recuperar “Valor a Considerar” dos registros cujo campo origem seja igual a parte A .	

Sim	MFS-17089		RNGM355-04	IND_ VL_CTA - Indicador do Lançamento

Exibir o indicador identificado pela RNGM355-03.	

Sim	MFS-17089		Registro M360: Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lacs
A partir da versão 3.00:  Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lacs 
Campo(s) chave: COD_CTA + COD_CCUS
Ocorrência – 0:N
Nível Hierárquico – 4

Considerações Gerais:

Relaciona os lançamentos da parte A do e-Lacs com as contas contábeis.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM360
	Para a geração deste registro, recuperar informações conforme abaixo:

Recuperar de lançamentos da parte A que possuam Tipo de Relacionamento = 2 - Com Conta Contábil ou 3 – Com Conta da parte B e Conta Contábil conforme RNGM350-05 na aba Contas Contábeis da tabela de lançamentos da parte A conforme o documento  MTZ_Processamento_em_Lote.docx com base na RNP21.
Verificar se a Conta Contábil recuperada possui parametrização de Lançamento de Adição e Exclusão da Tela Recuperação dos Valores - Apuração IRPJ/CSLL diferente de “Não se Aplica” ou Nulo. Caso positivo, deve ser gerado o Registro M360 apenas para a linha da parte A que recebeu valor na opção entre Adição ou Exclusão.

As informações recuperadas também poderão ser identificadas na aba Contas Contábeis da tabela de lançamentos da parte A.


	-	 MFS-17089 		RNGM360-01	REG – Tipo de Registro

Gerar fixo ‘M360’	Sim	MFS-17089		RNGM360-02	COD_CTA - Código de Conta Contábil

Recuperar o conteúdo do campo “Conta Contábil” código de cada conta contábil.	Sim	MFS-17089		RNGM360-03	COD_CCUS - Código do Centro de Custos

Recuperar o conteúdo do campo “Centro Custos” se houver, para cada código da conta contábil recuperada pela RNGM360-02.	Não	MFS-17089		RNGM360-04	VL_CTA - Valor da Conta
Recuperar o conteúdo do campo “Saldo” de cada código de conta contábil recuperado pela RNGM360-02
	
Sim	MFS-17089		RNGM360-05	IND_VL_CTA - Indicador do Saldo da Conta

Recuperar o conteúdo do campo “IND” de cada saldo recuperado pela RNGM360-04.

	
Sim	
MFS-17089		
Registro M362: Números dos Lançamentos Relacionados à Conta Contábil 
Ocorrência – 0:N
Nível Hierárquico – 5
Campo(s) chave: NUM_LCTO

Considerações Gerais:

Apresenta o número dos lançamentos contábeis relacionados ao lançamento da conta da parte A.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM362
	Para a geração deste registro, recupera conforme RNGM360-02 informações da tabela de lançamentos da parte A que possuam informações de Lançamentos Contábeis na aba Contas Contábeis.

	-	MFS-17089 		RNGM362-01	REG – Tipo de Registro

Gerar fixo ‘M362’	Sim	MFS-17089 		RNGM362-02	NUM_LCTO – Número do Lançamento

Recuperar o conteúdo do campo “Número do Lançamento”.	Sim	MFS-17089		
Registro M365: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento 
Campo(s) chave: IND_PROC + NUM_PROC
Ocorrência – 0:N
Nível Hierárquico – 4

Considerações Gerais:

Identifica os processos judiciais e administrativos utilizados que embasaram adições menores que as previstas na legislação ou falta de adição e exclusões maiores que as previstas na legislação na parte A do e-Lalur (tratamento diverso do regramento fiscal). 

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM365
	Para a geração deste registro, recuperar informações da tabela de lançamentos da parte A conforme RNGM350-05 que possuam informações de Processos Judiciais na aba Processos da tabela de lançamentos da parte A. 

	-	MFS-17089		RNGM365-01	REG – Tipo de Registro

Gerar fixo ‘M365’
	Sim	MFS-17089		RNGM365-02	IND_PROC - Tipo do Processo

Recuperar o conteúdo do campo “Tipo de Processo”.

Se na tela estiver selecionada a opção “Judicial”, gerar “1”.
Se estiver selecionada opção “Administrativo”, gerar “2”.
	


Sim	MFS-17089		RNGM365-03	NUM_PROC – Número do Processo

Recuperar o conteúdo do campo “Número do Processo” de acordo com o tipo o processo recuperado pela RNGM365-02.	
Sim	MFS-17089		
Registro M410: LANÇAMENTOS NA CONTA DA PARTE “B” DO e-LALUR e do e-LACS SEM REFLEXO NA PARTE A
Campo(s) chave: 
Ocorrência – 0:N
Nível Hierárquico – 3

Considerações Gerais:

Apresenta os lançamentos em contas da parte B sem reflexos na parte A da tela Ajustes da Parte B (aba M410).


CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM410
	Para a geração deste registro, recuperar os registros com campo origem igual à parte B na tabela de ajustes da parte B relacionados as contas da parte B de acordo com a regra de seleção da RNGM010.
	-	MFS-17089  MFS-17089 		RNGM410-01	REG – Tipo de Registro

Gerar fixo ‘M410’
	Sim	MFS-17089		RNGM410-02	COD_CTA_B -Código da Conta do Lançamento

Recuperar o código do campo “Conta da Parte B”.
	Não	MFS-17089		RNGM410-03	COD_TRIBUTO - Código do Tributo

Recuperar o conteúdo do campo “Tipo de Tributo” para cada conta encontrada pela RNGM410-02.

Se para a conta recuperada pela RNGM410-02 o campo “Tipo de Tributo” estiver preenchido com:

“I – Imposto de Renda Pessoa Jurídica”, gerar “I”.

“C – Contribuição Social sobre o Lucro Líquido”, gerar “C”.
	


Sim	MFS-17089		RNGM410-04	VAL_LAN_LALB_PB - Valor do Lançamento

Para cada conta recuperada pela RNGM410-02, recuperar o conteúdo do campo “Valor”.
	
Sim	MFS-17089		RNGM410-05	IND_VAL_LAN_LALB_PB - Indicador do Lançamento

Recuperar o conteúdo do campo “Ind. do Valor” referente ao ajuste efetuado.

Indicadores válidos para recuperação:

CR – Crédito
DB – Débito
PF - Prejuízo do exercício.
BC - Base de cálculo negativa da CSLL

	
Sim	
MFS-17089		RNGM410-06	COD_CTA_B_CTP - Código da Conta de Contrapartida 

Recuperar o código do campo “Contrapartida”
	
Não	MFS-17089		RNGM410-07	HIST_LAN_LALB – Histórico

Recuperar o conteúdo do campo “Histórico” para cada conta encontrada pela RNGM410-02.
	
Sim	MFS-17089		RNGM410-08	IND_LAN_ANT - Realização de Valores cuja Tributação Tenha Sido Diferida

Recuperar o conteúdo do campo “Tributação Diferida” para cada RNGM410-02 recuperada.

Se na tela estiver selecionada a opção “Sim”, gerar “S”.
Se estiver selecionada opção “Não”, gerar “N”.
	
Sim	MFS-17089		Registro M415: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento 
Campo(s) chave: IND_PROC + NUM_PROC
Ocorrência – 0:1
Nível Hierárquico – 4

Considerações Gerais:

 Identifica os processos judiciais e administrativos utilizados que embasaram o lançamento na parte B.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM415
	Para a geração deste registro, recuperar na tabela de ajustes da parte B os processos associados aos ajustes efetuados para as contas recuperadas pelo registro M410 conforme tela “Adicionar Lançamento da Parte B” - grid  “Dados dos Processos” 

Se o registro M410 foi agrupado/copiado, todos os processos envolvidos (associados em todos os lançamentos), devem ser gerados no M415.

Agrupamento do registro:
Gerar um registro por Tipo do Processo e Número do Processo. 

	-	MFS-17089		RNGM415-01	REG – Tipo de Registro

Gerar fixo ‘M415’
	Sim	MFS-17089		RNGM415-02	IND_PROC - Tipo do Processo

Recuperar o conteúdo do campo “Tipo de Processo”.

Se na tela estiver selecionada a opção “Judicial”, gerar “1”.
Se estiver selecionada opção “Administrativo”, gerar “2”.
	


Sim	MFS-17089		RNGM415-03	NUM_PROC – Número do Processo

Recuperar o conteúdo do campo “Número do Processo” de acordo com o tipo o processo recuperado pela RNGM415-02.	
Sim	MFS-17089		
Registro M990: Encerramento do Bloco M 
Campo(s) chave: REG
Ocorrência – 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGM990-01
	REG – Tipo de Registro

Gerar fixo ‘M990’	Sim	MFS-17089		RNGM990-02	QTD_LIN – Quantidade Total de Registro do Bloco M

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco M e informar o total.
Considerando que Campo 1: Texto fixo contendo "M990", e campo 2: Quantidade total de linhas do bloco M.

Exemplo: |M990|25|	Sim	MFS-17089		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN