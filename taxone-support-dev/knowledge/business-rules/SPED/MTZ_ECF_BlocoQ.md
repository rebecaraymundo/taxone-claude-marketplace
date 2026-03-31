# MTZ_ECF_BlocoQ

> Fonte: MTZ_ECF_BlocoQ.doc

THOMSON REUTERS

ECF – Geração do Arquivo
Bloco Q


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		09/03/2018	MFS-17092	Criação do Documento – Liberado a abertura e encerramento do Bloco	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc477270098" INTRODUÇÃO	 PAGEREF _Toc477270098 \h 3
 HYPERLINK \l "_Toc477270099" 1.	Regras de Negócio	 PAGEREF _Toc477270099 \h 3
 HYPERLINK \l "_Toc477270100" 1.1	Informações gerais de seleção e processamento	 PAGEREF _Toc477270100 \h 3
 HYPERLINK \l "_Toc477270101" 1.2	Registros Identificadores	 PAGEREF _Toc477270101 \h 4
 HYPERLINK \l "_Toc477270102" 1.2.1	Registro Q001: Abertura do Bloco Q	 PAGEREF _Toc477270102 \h 4
 HYPERLINK \l "_Toc477270103" 1.2.2	Registro Q100: Demonstrativo do Livro Caixa (FACULTATIVO PARA O ANO-CALENDÁRIO 2015/ OBRIGATÓRIO A PARTIR DO O ANO-CALENDÁRIO 2016)	 PAGEREF _Toc477270103 \h 4
 HYPERLINK \l "_Toc477270104" 1.2.3	Registros Q990: Encerramento do Bloco Q	 PAGEREF _Toc477270104 \h 6
 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO
Este bloco tem o objetivo de apresentar as informações do livro caixa, caso existam.
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-Q	Período de recuperação dos registros: Data Inicial das Informações da ECF e a Data Final da última Apuração conforme Abertura da Apuração.

Recuperar as informações da tela Demonstrativo do Livro Caixa (Q100). Se houver registros na tela que não serão gerados por não estar dentro do período de recuperação dos registros, exibir a mensagem DW00186.
Se o Registro estiver como OC no campo ‘Obrigatoriedade Saída’ (item 1.2 deste documento), for de nível igual a “2” e as regras do registro forem cumpridas, mas não existir dados na tela (mencionada na regra geral do registro), exibir a mensagem DW00187

Não será realizada validações do registro na geração, pois os possíveis erros estão sendo validados na tela


OBS: A mensagem DW00186 e o ajuste no Período de recuperação dos registros foram criadas para o seguinte cenário: 

A tela Demonstrativo do Livro Caixa, não exige que os dados a serem importados estejam dentro do período de uma Abertura da Apuração. Logo, é possível que o usuário informe os 12 meses do ano, pois é necessário apenas Informações ECF para a inclusão de informações na tela. Sendo assim, se houver, por exemplo, alguma situação especial (Data do Evento preenchida na tela Abertura da Apuração) que foi informada no sistema após a inserção dos dados na tela Demonstrativo do Livro Caixa (Q100), tal tela não validará a informação, mas a geração garantirá que serão recuperados os dados consistentes para a geração do Bloco Q.

Na tela de Perfil de geração o registro deve estar selecionado para a geração.
		 MFS-17092		Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		 HYPERLINK  \l "RY001" Q001	1	Abertura do Bloco Q – Livro Caixa 	F	O	[1:1]		HYPERLINK \l "RY520"Q100	2	Demonstrativo do Livro Caixa 
	F	OC
Obrigatório se 
0010. TIP_ESP_PRE = “L”
N
Senão, não deve existir.	 Se 
0010. TIP_ESP_PRE = “L”
 [1:N]
Senão [0]		HYPERLINK \l "RY990"Q990	1	Encerramento do Bloco Q	F	O	[1:1]		Registro Q001: Abertura do Bloco Q
Campo Chave: REG
Ocorrência: 1:1
CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGY001-01	REG – Tipo de Registro

Gerar fixo ‘Q001’	

SIM	 MFS-17092		RNY001-02	IND_DAD - Indicador de Movimento

Caso existam informações nos registros do bloco Q (Q100) preencher com “0”, caso contrário, preencher com “1”.
	
SIM	 MFS-17092		Registro Q100: Demonstrativo do Livro Caixa (FACULTATIVO PARA O ANO-CALENDÁRIO 2015/ OBRIGATÓRIO A PARTIR DO O ANO-CALENDÁRIO 2016)
Campo Chave: Ainda não foi definido pela Receita
Ocorrência: 0:N
CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGQ100	Para a geração deste registro, recuperar as informações da tela Demonstrativo do Livro Caixa (Q100), considerando os parâmetros da RNG-Q. 

A partir da versão 3.00 incluir a na regra a verificação abaixo:

Se SOMA (P200(2) + P200(4) + P200(6) + P200(8)) > 100.000 x (Número de Meses da ECF) o bloco Q deve ser gerado.

Se o valor resultante da soma for verdadeiro e não for identificada dados na tela Demonstrativo do Livro Caixa (Q100) de acordo com o período informado para a geração do arquivo, exibir a TR01335.

A soma deve considerar isoladamente cada trimestre, ou seja, o valor das linhas no T1 + T2 + T3 + T4.
	
-		RNGQ100-01	REG – Tipo de Registro

Gerar fixo ‘Q100’	
Sim		RNGQ100-02	DATA – Data da entrada ou da saída dos recursos

Preencher com a data de cada registro recuperado. 	
Sim		RNGQ100-03	NUM_DOC – Número do documento

Preencher com o número de documento de cada registro recuperado.	
Não		RNGQ100-04	HIST – Histórico

Preencher com o Histórico de cada registro recuperado.	
Sim		RNGQ100-05	VL_ENTRADA – Valor de entrada dos recursos

Preencher com o Valor de Entrada de cada registro recuperado.	
Não		RNGQ100-06	VL_SAÍDA – Valor de saída dos recursos

Preencher com o Valor de Saída de cada registro recuperado.	
Não		RNGQ100-07	SLD_FIN – Saldo Final

Preencher com o Saldo Final de cada registro recuperado.	
Sim		Registros Q990: Encerramento do Bloco Q	
Campo Chave: REG
Ocorrência: 1:1
CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGQ990-01	REG – Tipo de Registro
Gerar fixo ‘Q990’	
SIM	
MFS-17092		RNQ990-02	QTD_LIN – Quantidade Total de Registro do Bloco Q

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco Q e informar o total.
Considerando que Campo 1: Texto fixo contendo "Q990", e campo 2: Quantidade total de linhas do bloco Q.

Exemplo: |Q990|1000|	

SIM	 MFS-17092		
Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN