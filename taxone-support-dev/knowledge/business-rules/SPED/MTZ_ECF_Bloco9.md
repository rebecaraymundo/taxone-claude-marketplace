# MTZ_ECF_Bloco9

> Fonte: MTZ_ECF_Bloco9.doc

THOMSON REUTERS

Geração do Bloco 9


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		07/03/2018	MFS-17099	Criação do Documento	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc508203699" 1.	INTRODUÇÃO	 PAGEREF _Toc508203699 \h 3
 HYPERLINK \l "_Toc508203700" 2.	Regras de Negócio	 PAGEREF _Toc508203700 \h 3
 HYPERLINK \l "_Toc508203701" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc508203701 \h 3
 HYPERLINK \l "_Toc508203702" 2.2	Registros Identificadores	 PAGEREF _Toc508203702 \h 3
 HYPERLINK \l "_Toc508203703" 2.2.1	Registro 9001: Abertura do Bloco 9	 PAGEREF _Toc508203703 \h 4
 HYPERLINK \l "_Toc508203704" 2.2.2	Registro 9900: Registros do Arquivo	 PAGEREF _Toc508203704 \h 4
 HYPERLINK \l "_Toc508203705" 2.2.3	Registro 9990: Encerramento do Bloco 9	 PAGEREF _Toc508203705 \h 5
 HYPERLINK \l "_Toc508203706" 2.2.4	Registro 9999: Encerramento do Arquivo Digital	 PAGEREF _Toc508203706 \h 6

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO

Este bloco tem o objetivo de apresentar o totalizador dos registros apresentado no meio magnético.
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-9	Para geração desse bloco, considerar todos os registros gerados no arquivo.	MFS-17099		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		 HYPERLINK  \l "R9001" 9001	1	Abertura do Bloco 9
	O	O	[1:1]		HYPERLINK \l "R9099"9099	1	Encerramento do Bloco 9
	O	O	[1:1]		9100	2	Avisos da Escrituração	F	O	[0:N]		HYPERLINK \l "REG_9900"9900	2	Registros do Arquivo
	O	O	
Até versão 2.00:
[1:1]

A partir da versão 3.00:
[1:N]
		HYPERLINK \l "R9999"9999	Até versão 2.00:
0
A partir da versão 3.00:
1
	Encerramento do Arquivo Digital
	O	O	[1:1]		
Registro 9001: Abertura do Bloco 9
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNG9001-01	REG – Tipo de Registro

Gerar fixo ‘9001’	Sim	MFS-17099		RNG9001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco 0 (exceto no registro 0001 e 0990), preencher com “0”, caso contrário, preencher com “1”.
	Sim	MFS-17099		
Registro 9900: Registros do Arquivo
Campo Chave: REG
Ocorrência: Até versão 2.00: [1:1], a partir da versão 3.00: [1:N]
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNG9900	Deve ser mostrada a quantidade total de ocorrência de todos os registros que aparecem no arquivo da ECF, inclusive do próprio registro 9900, seguindo a ordem hierárquica dos registros apresentados no arquivo.		MFS-17099		RNG9900-01	REG – Tipo de Registro

Gerar fixo ‘9900’	Sim	MFS-17099		RNG9900-02	REG_BLC - Registro 

Preencher com o código de cada registro gerado no arquivo, sem duplicidade.
Exemplo: |0000|	Sim	MFS-17099		RNG9900-03	QTD_REG_BLC - Total de Registros por Tipo

Preencher com a quantidade total de registros existentes no arquivo do tipo informado na RNG9900-02.
Exemplo: |1| - Quer dizer que apenas um registro 0000 foi gerado no arquivo.	Sim	MFS-17099		RNG9900-04	VERSAO - Versão

Para os registros que são gerados a partir da tabela dinâmica, preencher com a versão da tabela dinâmica utilizada. Caso contrário, preencher com nulo.
Exemplo: 
|9900|L210|100|1.00||
|9900|0000|1|||	Não	MFS-17099		RNG9900-05	ID_TAB_DIN - Identificação de Tabela Dinâmica Utilizada

Preencher com nulo.	Não	MFS-17099		

Registro 9990: Encerramento do Bloco 9
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNG9990-01	REG – Tipo de Registro

Gerar fixo ‘9990’	Sim	MFS-17099		RNG9990-02	QTD_LIN – Quantidade Total de Registro do Bloco 9

Para geração desse registro o sistema deverá internamente contar quantas linhas do bloco 9 existem no arquivo, inclusive o registro 9999 e informar o total.
Exemplo: |9990|25|
	Sim	MFS-17099		

Registro 9999: Encerramento do Arquivo Digital
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNG9999-01	REG – Tipo de Registro

Gerar fixo ‘9999’	Sim	MFS-17099		RNG9999-02	QTD_LIN – Quantidade Total de Registros do Arquivo Digital

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo em todos os blocos, inclusive o registro 9999 e informar o total. 
Exemplo: |9999|4774|	Sim	MFS-17099		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN