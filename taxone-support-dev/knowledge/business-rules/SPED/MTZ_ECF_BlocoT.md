# MTZ_ECF_BlocoT

> Fonte: MTZ_ECF_BlocoT.doc

THOMSON REUTERS

Geração do Bloco T 


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		09/03/2018	MFS-17093	Criação do Documento. Liberado a abertura e encerramento do bloco.	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc409608117" 1.	INTRODUÇÃO	 PAGEREF _Toc409608117 \h 3
 HYPERLINK \l "_Toc409608123" 2.	Regras de Negócio	 PAGEREF _Toc409608123 \h 3
 HYPERLINK \l "_Toc409608124" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc409608124 \h 3
 HYPERLINK \l "_Toc409608125" 2.2	Registros Identificadores	 PAGEREF _Toc409608125 \h 3
 HYPERLINK \l "_Toc409608126" 2.2.1	Registro T001: Abertura do Bloco T	 PAGEREF _Toc409608126 \h 4
 HYPERLINK \l "_Toc409608127" 2.2.2	Registro T030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Arbitrado	 PAGEREF _Toc409608127 \h 4
 HYPERLINK \l "_Toc409608128" 2.2.3	Registro T120: Apuração da Base de Cálculo do IRPJ com Base no Lucro Arbitrado	 PAGEREF _Toc409608128 \h 5
 HYPERLINK \l "_Toc409608129" 2.2.4	Registro T150: Cálculo do IRPJ com Base no Lucro Arbitrado	 PAGEREF _Toc409608129 \h 5
 HYPERLINK \l "_Toc409608130" 2.2.5	Registro T170: Apuração da Base de Cálculo da CSLL com Base no Lucro Arbitrado	 PAGEREF _Toc409608130 \h 6
 HYPERLINK \l "_Toc409608131" 2.2.6	Registro T181: Cálculo da CSLL com Base no Lucro Arbitrado	 PAGEREF _Toc409608131 \h 7
 HYPERLINK \l "_Toc409608132" 2.2.7	Registro T990: Encerramento do Bloco T	 PAGEREF _Toc409608132 \h 7

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO

Este bloco tem o objetivo de apresentar o Lucro Arbitrado
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-T	Para que seja possível recuperar os registros, é necessário ter realizado a Abertura da Apuração e posteriormente o Processamento em Lote. 

Considerar as aberturas de apurações, cuja data inicial e final esteja compreendida no período informado no registro 0000 (RNG0000-10 e RNG0000-11) e a forma de tributação seja igual a “Lucro Arbitrado”.

Para geração do arquivo, considerar todas as apurações processadas que são correspondentes às aberturas de apurações selecionadas.

- A exibição do conteúdo referente “Cód. do Registro” e deve respeitar a sequência da coluna Código.

- Aplicar a RNG00051 - Geração dos Registros

- Na tela de Perfil de geração o registro deve estar selecionado para a geração.
		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		T001	1	Abertura do Bloco P	F	O	[1:1]		T030	2	Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Arbitrado	F	O	[0:4]		T120	2	Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido	F	O	[0:4]		T150	3	Balanço Patrimonial	F		[0:N]		T170	3	Demonstrativo do Resultado do Exercício	F	O	[0:N]		T181		T990	1	Encerramento do Bloco T	F	O	[1:1]		
Registro T001: Abertura do Bloco T
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGT001-01	REG – Tipo de Registro

Gerar fixo ‘T001’	Sim	MFS-17093		RNGT001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco P (registros T001, T030, T120, T150, T170, T181 e T990), preencher com “0”, caso contrário, preencher com “1”.
	Sim	MFS-17093		
Registro T030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Arbitrado
Campo Chave: PER_APUR
Ocorrência: 1:4
Nível Hierárquico – 2

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGT030	Só serão geradas informações neste bloco se o campo 05 – FORMA_TRIB do registro 0010 estiver preenchido com “2”, “4”, “6” ou “7” conforme RNP01 documento MTZ_Processamento_em_Lote.docx e o campo 08 – FORMA_TRIB_PER do registro 0010 para os períodos que estiverem preenchidos com “A” conforme definição existente no bloco 0.

Deverá ser gerado um registro T030 para cada abertura de apuração da escrituração, conforme considerando os parâmetros da RNG-T. Neste caso, o registro T01...T04 deverá ser criado considerando o ‘período de apuração’, onde :

1º Trimestre = T01
2 º Trimestre = T02
3 º Trimestre = T03
4 º Trimestre = T04
		RNGT030-01	REG – Tipo de Registro

Gerar fixo ‘T030’	Sim		RNGT030-02	DT_INI - Data do Saldo Inicial

Preencher com a data inicial do período da abertura de apuração criado para a empresa.	Sim		RNGT030-03	DT_FIN - Data do Saldo Final

Preencher com a data final do período da abertura de apuração criado para a empresa.	Sim		RNGT030-04	PER_APUR - Período de Apuração

Preencher conforme RNGT030.	Sim		

Registro T120: Apuração da Base de Cálculo do IRPJ com Base no Lucro Arbitrado
Campo Chave: CODIGO
Ocorrência: 1:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGT120	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro T120), considerando os parâmetros da RNG-T. 

Documentação de apoio:
A regra de processamento do registro T120 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGT120-01	REG – Tipo de Registro

Gerar fixo ‘T120’	Sim		RNGT120-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGT120-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGT120-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		

Registro T150: Cálculo do IRPJ com Base no Lucro Arbitrado
Campo Chave: CODIGO
Ocorrência: 1:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGT150	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro T150), considerando os parâmetros da RNG-T. 

Documentação de apoio:
A regra de processamento do registro T150 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGT150-01	REG – Tipo de Registro

Gerar fixo ‘T150’	Sim		RNGT150-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGT150-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGT150-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		
Registro T170: Apuração da Base de Cálculo da CSLL com Base no Lucro Arbitrado 
Campo Chave: CODIGO
Ocorrência: 1:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGT170	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro T170), considerando os parâmetros da RNG-T. 

Documentação de apoio:
A regra de processamento do registro T170 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGT170-01	REG – Tipo de Registro

Gerar fixo ‘T170’	Sim		RNGT170-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGT170-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGT170-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		
Registro T181: Cálculo da CSLL com Base no Lucro Arbitrado
Campo Chave: CODIGO
Ocorrência: 1:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGT181	Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro T181), considerando os parâmetros da RNG-T. 

Documentação de apoio:
A regra de processamento do registro T181 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGT181-01	REG – Tipo de Registro

Gerar fixo ‘T181’	Sim		RNGT181-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGT181-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGT181-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		

Registro T990: Encerramento do Bloco T
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 1

Condições Gerais: 

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGT990-01	REG – Tipo de Registro

Gerar fixo ‘T990’	Sim	MFS-17093		RNGT990-02	QTD_LIN – Quantidade Total de Registro do Bloco T

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco T e informar o total.
Considerando Campo 1: Texto fixo contendo "T990", e campo 2: Quantidade total de linhas do bloco T.

Exemplo: |T990|25|
	Sim	MFS-17093		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN