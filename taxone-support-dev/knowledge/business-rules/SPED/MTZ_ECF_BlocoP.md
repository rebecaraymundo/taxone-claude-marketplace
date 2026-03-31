# MTZ_ECF_BlocoP

> Fonte: MTZ_ECF_BlocoP.doc

THOMSON REUTERS

Geração do Bloco P


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		09/03/2018	MFS-17091	Criação do Documento – Liberado a abertura e encerramento do bloco.	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u 1.	INTRODUÇÃO	3
2.	Regras de Negócio	3
2.1	Informações gerais de seleção e processamento	3
2.2	Registros Identificadores	3
2.2.1	Registro P001: Abertura do Bloco P	4
2.2.2	Registro P030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido	4
2.2.3	Registro P100: Balanço Patrimonial	6
2.2.4	Registro P130: Demonstração das Receitas Incentivadas do Lucro Presumido	7
2.2.5	Registro P150: Demonstrativo do Resultado do Exercício	8
2.2.6	Registro P200: Apuração da Base de Cálculo do Lucro Presumido	9
2.2.7	Registro P230: Cálculo da Isenção e Redução do Lucro Presumido	10
2.2.8	Registro P300: Cálculo do IRPJ com Base no Lucro Presumido	11
2.2.9	Registro P400: Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido	11
2.2.10	Registro P500: Cálculo da CSLL com Base no Lucro Presumido	12
2.2.11	Registro P990: Encerramento do Bloco P	13

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO

Este bloco tem o objetivo de apresentar o Lucro Presumido.
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-P	Para que seja possível recuperar os registros, é necessário ter realizado a Abertura da Apuração e posteriormente o Processamento em Lote. 

Considerar as aberturas de apurações, cuja data inicial e final esteja compreendida no período informado no registro 0000 (RNG0000-10 e RNG0000-11) e a forma de tributação seja igual a “Lucro Presumido”.

Para geração do arquivo, considerar todas as apurações processadas que são correspondentes às aberturas de apurações selecionadas.

- A exibição do conteúdo referente “Cód. do Registro” deve respeitar a sequência da coluna Código.

- Aplicar RNG00051 - Geração dos Registros

- Na tela de Perfil de geração o registro deve estar selecionado para a geração.

		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		P001	1	Abertura do Bloco P	F	O	[1:1]		P030	2	Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido	F	O	[0:4]		P100	3	Balanço Patrimonial	F		[0:N]		P130	3	Demonstração das Receitas Incentivadas do Lucro Presumido	F	O	[0:N]		P150	3	Demonstrativo do Resultado do Exercício	F	O	[0:N]		P200	3	Apuração da Base de Cálculo do Lucro Presumido	F	O	[0:N]		P230	3	Cálculo da Isenção e Redução do Lucro Presumido	F	O	[0:N]		P300	3	Cálculo do IRPJ com Base no Lucro Presumido		[0:N]		P400	3	Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido		[0:N]		P500	3	Cálculo da CSLL com Base no Lucro Presumido		[0:N]		P990	1	Encerramento do Bloco P	F	O	[1:1]		
Registro P001: Abertura do Bloco P
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP001-01	REG – Tipo de Registro

Gerar fixo ‘P001’	Sim	MFS-17091		RNGP001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco P (registros P030, P100, P150, P130, P150, P200, P230, P400, P500), preencher com “0”, caso contrário, preencher com “1”.
	Sim	MFS-17091		
Registro P030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido
Campo Chave: PER_APUR
Ocorrência: 0:4
Nível Hierárquico – 2

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP030	Só serão geradas informações neste bloco se o campo 05 – FORMA_TRIB do registro 0010 estiver preenchido com “3”, “4”, “5” ou “7” conforme RNP01 documento MTZ_Processamento_em_Lote.docx e o campo 08 – FORMA_TRIB_PER do registro 0010 estiver preenchido com “P”

Deverá ser gerado um registro P030 para cada abertura de apuração da escrituração, conforme considerando os parâmetros da RNG-P. Neste caso, o registro T01...T04 deverá ser criado considerando o ‘período de apuração’, onde :

1º Trimestre = T01
2 º Trimestre = T02
3 º Trimestre = T03
4 º Trimestre = T04
		RNGP030-01	REG – Tipo de Registro

Gerar fixo ‘P030’	Sim		RNGP030-02	DT_INI - Data do Saldo Inicial

Preencher com a data inicial do período da abertura de apuração criado para a empresa.	Sim		RNGP030-03	DT_FIN - Data do Saldo Final

Preencher com a data inicial do período da abertura de apuração criado para a empresa.
	Sim		RNGP030-04	PER_APUR - Período de Apuração

Preencher conforme RNGP030.	Sim		

Registro P100: Balanço Patrimonial
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP100	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado - registro P100), considerando os parâmetros da RNG-P. 

Documentação de apoio:
A regra de processamento do registro P100 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.		RNGP100-01	REG – Tipo de Registro

Gerar fixo ‘P100’	Sim		RNGP100-02	CODIGO - Código da Conta Referencial

Preencher com o Cód. da Conta Referencial de cada registro recuperado.	Sim		RNGP100-03	DESCRICAO - Descrição

Preencher com o Desc. da Conta Referencial de cada registro recuperado.	Não		RNGP100-04	TIPO - Tipo de Conta 

Preencher com o Tipo de Conta de cada registro recuperado.	Sim		RNGP100-05	NIVEL- Nível da Conta

Preencher com o Tipo de Conta de cada registro recuperado.	Não		RNGP100-06	COD_NAT- Natureza da Conta

Preencher com a Natureza da Conta da tabela de Plano de Conta Referencial correspondente a cada registro recuperado.	Não		RNGP100-07	COD_CTA_SUP - Código conta superior

Preencher com o Código da Conta Superior da tabela de Plano de Conta Referencial correspondente a cada registro recuperado.	Não		RNGP100-08	VAL_CTA_REF_INI - Valor do Saldo Inicial

Preencher com o Valor do Saldo Inicial de cada registro recuperado.	Sim		RNGP100-09	IND_VAL_CTA_REF_INI - Indicador do Saldo Inicial

Preencher com o Ind. do Saldo Inicial de cada registro recuperado.	Sim		RNGP100-10	VAL_CTA_REF_FIN - Valor do Saldo Final

Preencher com o Valor do Saldo Final de cada registro recuperado.	Sim		RNGP100-11	IND_ VAL_CTA_REF_FIN - Indicador do Saldo Final

Preencher com o Ind. do Saldo Final de cada registro recuperado.	Sim		Registro P130: Demonstração das Receitas Incentivadas do Lucro Presumido
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP130	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro P130), considerando os parâmetros da RNG-P. 

Documentação de apoio:
A regra de processamento do registro P130 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGP130-01	REG – Tipo de Registro

Gerar fixo ‘P130’	Sim		RNGP130-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGP130-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGP130-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		
Registro P150: Demonstrativo do Resultado do Exercício
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP150	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado - registro P150), considerando os parâmetros da RNG-P. 

Documentação de apoio:
A regra de processamento do registro P150 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.		RNGP150-01	REG – Tipo de Registro

Gerar fixo ‘P150’	Sim		RNGP150-02	CODIGO - Código da Conta referencial

Preencher com o Cód. da Conta Referencial de cada registro recuperado.	Sim		RNGP150-03	DESCRICAO - Descrição

Preencher com o Desc. da Conta Referencial de cada registro recuperado.	Não		RNGP150-04	TIPO - Tipo da Conta

Preencher com o Tipo de Conta de cada registro recuperado.	Sim		RNGP150-05	NIVEL - Nível da Conta

Preencher com o Tipo de Conta de cada registro recuperado.	Não		RNGP150-06	COD_NAT - Natureza da Conta

Preencher com a Natureza da Conta da tabela de Plano de Conta Referencial correspondente a cada registro recuperado.	Não		RNGP150-07	COD_CTA_SUP - Código da Conta Superior

Preencher com o Código da Conta Superior da tabela de Plano de Conta Referencial correspondente a cada registro recuperado.	Não		RNGP150-08	VALOR - Valor do Saldo Final da Conta Referencial

Preencher com o Valor do Saldo Final de cada registro recuperado.	Sim		RNGP150-09	IND_ VALOR - Indicador do Saldo Final da Conta Referencial

Preencher com o Ind. do Saldo Final de cada registro recuperado.	Sim		Registro P200: Apuração da Base de Cálculo do Lucro Presumido
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP200	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro P200), considerando os parâmetros da RNG-P. 

Documentação de apoio:
A regra de processamento do registro P200 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGP200-01	REG – Tipo de Registro

Gerar fixo ‘P200’	Sim		RNGP200-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGP200-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGP200-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		
Registro P230: Cálculo da Isenção e Redução do Lucro Presumido
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP230	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro P230), considerando os parâmetros da RNG-P. 

Documentação de apoio:
A regra de processamento do registro P230 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGP230-01	REG – Tipo de Registro

Gerar fixo ‘P230’	Sim		RNGP230-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGP230-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGP230-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		
Registro P300: Cálculo do IRPJ com Base no Lucro Presumido
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP300	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro P300), considerando os parâmetros da RNG-P. 

Documentação de apoio:
A regra de processamento do registro P300 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGP300-01	REG – Tipo de Registro

Gerar fixo ‘P300’	Sim		RNGP300-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGP300-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGP300-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		
Registro P400: Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP400	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro P400), considerando os parâmetros da RNG-P. 

Documentação de apoio:
A regra de processamento do registro P400 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGP400-01	REG – Tipo de Registro

Gerar fixo ‘P400’	Sim		RNGP400-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGP400-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGP400-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		

Registro P500: Cálculo da CSLL com Base no Lucro Presumido
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP500	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro P500), considerando os parâmetros da RNG-P. 

Documentação de apoio:
A regra de processamento do registro P500 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGP500-01	REG – Tipo de Registro

Gerar fixo ‘P500’	Sim		RNGP500-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGP500-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGP500-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		

Registro P990: Encerramento do Bloco P
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 1

Condições Gerais: 

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGP990-01	REG – Tipo de Registro

Gerar fixo ‘P990’	Sim	MFS-17091		RNGP990-02	QTD_LIN – Quantidade Total de Registro do Bloco P

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco P e informar o total.
Considerando Campo 1: Texto fixo contendo "P990", e campo 2: Quantidade total de linhas do bloco P.

Exemplo: |P990|25|
	Sim	MFS-17091		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN