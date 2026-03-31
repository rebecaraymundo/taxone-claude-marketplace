# MTZ_ECF_BlocoC

> Fonte: MTZ_ECF_BlocoC.doc

THOMSON REUTERS

Geração do Registro de abertura e encerramento do Bloco C


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		
07/03/2018	MFS-17084	
Criação do Documento	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc408910999" 1.	INTRODUÇÃO	 PAGEREF _Toc408910999 \h 3
 HYPERLINK \l "_Toc408911000" 2.	Regras de Negócio	 PAGEREF _Toc408911000 \h 3
 HYPERLINK \l "_Toc408911001" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc408911001 \h 3
 HYPERLINK \l "_Toc408911002" 2.2	Registros Identificadores	 PAGEREF _Toc408911002 \h 3
 HYPERLINK \l "_Toc408911003" 2.2.1	Registro C001: Abertura do Bloco C	 PAGEREF _Toc408911003 \h 3
 HYPERLINK \l "_Toc408911004" 2.2.2	Registro C990: Encerramento do Bloco C	 PAGEREF _Toc408911004 \h 4

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO

Este bloco não é preenchido pela empresa. O sistema preencherá o bloco C no momento da recuperação das Escriturações Contábeis Digitais (ECD).
Regras de Negócio
Informações gerais de seleção e processamento
Não e aplica
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		C001	1	Até versão 2.00:

Abertura do Bloco C

A partir da versão 3.00:

Abertura do Bloco C - Informações Recuperadas da ECD	Até versão 2.00:


F

A partir da versão 3.00:

O	O	[1:1]		C990	1	Encerramento do Bloco C
	Até versão 2.00:


F

A partir da versão 3.00:

O	O	[1:1]		
Registro C001: Abertura do Bloco C
A partir da versão 3.00: Abertura do Bloco C - Informações Recuperadas da ECD

Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS-		RNGC001-01	REG – Tipo de Registro

Gerar fixo ‘C001’	Sim	MFS-17084		RNGC001-02	IND_DAD - Indicador de  Movimento

Caso existirem informações nos registros do bloco C (registros C040, C050, C051, C053, C100, C150, C155, C157, C350, C355), preencher com “0”, caso contrário, preencher com “1”.
	Sim	MFS-17084		
Registro C990: Encerramento do Bloco C
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 1

Condições Gerais: 

CÓD	DESCRIÇÃO	
OBRIG	MFS-		RNGC990-01	REG – Tipo de Registro

Gerar fixo ‘C990’	Sim	MFS-17084		RNGC990-02	QTD_LIN – Quantidade Total de Registro do Bloco C

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco C e informar o total.
	Sim	MFS-17084		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN