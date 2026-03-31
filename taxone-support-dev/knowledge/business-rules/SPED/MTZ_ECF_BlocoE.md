# MTZ_ECF_BlocoE

> Fonte: MTZ_ECF_BlocoE.doc

THOMSON REUTERS

Geração do Registro de abertura e encerramento do Bloco E


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		07/03/2018	MFS-17085
	Criação do Documento. 	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc408911691" 1.	INTRODUÇÃO	 PAGEREF _Toc408911691 \h 3
 HYPERLINK \l "_Toc408911692" 2.	Regras de Negócio	 PAGEREF _Toc408911692 \h 3
 HYPERLINK \l "_Toc408911693" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc408911693 \h 3
 HYPERLINK \l "_Toc408911694" 2.2	Registros Identificadores	 PAGEREF _Toc408911694 \h 3
 HYPERLINK \l "_Toc408911695" 2.2.1	Registro E001: Abertura do Bloco E	 PAGEREF _Toc408911695 \h 3
 HYPERLINK \l "_Toc408911696" 2.2.2	Registro E990: Encerramento do Bloco E	 PAGEREF _Toc408911696 \h 4

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO

Este bloco E, não é preenchido pela empresa. O sistema preencherá o bloco E no momento da recuperação da ECF no período imediatamente anterior e efetuará os cálculos fiscais relativos aos dados recuperados da ECD
Regras de Negócio
Informações gerais de seleção e processamento
Não e aplica
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		E001	1	Abertura do Bloco E	F	O	[1:1]		E990	1	Encerramento do Bloco E
	F	O	[1:1]		
Registro E001: Abertura do Bloco E
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGE001-01	REG – Tipo de Registro

Gerar fixo ‘E001’	Sim	MFS-17085		RNGE001-02	IND_DAD - Indicador de  Movimento

Caso existirem informações nos registros do bloco E (registros E010, E015, E020, E030, E155, E355), preencher com “0”, caso contrário, preencher com “1”.
	Sim	MFS-17085		
Registro E990: Encerramento do Bloco E
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 1

Condições Gerais: 

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGE990-01	REG – Tipo de Registro

Gerar fixo ‘E990’	Sim	MFS-17085		RNGE990-02	QTD_LIN – Quantidade Total de Registro do Bloco E

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco E , e informar o total.
	Sim	MFS-17085		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN