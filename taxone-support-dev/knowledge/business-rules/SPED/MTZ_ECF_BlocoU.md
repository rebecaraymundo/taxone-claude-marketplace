# MTZ_ECF_BlocoU

> Fonte: MTZ_ECF_BlocoU.doc

THOMSON REUTERS

Geração do Bloco U


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		09/03/2018	MFS-17094	Criação do Documento. Liberado a abertura e encerramento do bloco.	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc424141936" 1.	INTRODUÇÃO	 PAGEREF _Toc424141936 \h 3
 HYPERLINK \l "_Toc424141937" 2.	Regras de Negócio	 PAGEREF _Toc424141937 \h 3
 HYPERLINK \l "_Toc424141938" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc424141938 \h 3
 HYPERLINK \l "_Toc424141939" 2.2	Registros Identificadores	 PAGEREF _Toc424141939 \h 3
 HYPERLINK \l "_Toc424141940" 2.2.1	Registro U001: Abertura do Bloco U	 PAGEREF _Toc424141940 \h 5
 HYPERLINK \l "_Toc424141941" 2.2.2	Registro U030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas	 PAGEREF _Toc424141941 \h 6
 HYPERLINK \l "_Toc424141942" 2.2.3	Registro U100: Balanço Patrimonial	 PAGEREF _Toc424141942 \h 8
 HYPERLINK \l "_Toc424141943" 2.2.4	Registro U150: Demonstração do Resultado	 PAGEREF _Toc424141943 \h 9
 HYPERLINK \l "_Toc424141944" 2.2.5	Registro U180: Cálculo do IRPJ das Empresas Imunes ou Isentas Campo Chave: CODIGO	 PAGEREF _Toc424141944 \h 11
 HYPERLINK \l "_Toc424141945" 2.2.6	Registro U182: Cálculo da CSLL das Empresas Imunes ou Isentas	 PAGEREF _Toc424141945 \h 12
 HYPERLINK \l "_Toc424141946" 2.2.7	Registro U990: Encerramento do Bloco U	 PAGEREF _Toc424141946 \h 13

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO

Este bloco tem o objetivo de apresentar os arquivos das Empresas Imunes e Isentas;
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-U	
Período de recuperação dos registros: Partindo da Escrituração ECF, foco deste processamento, devemos considerar todas as suas apurações que estão compreendidas entre a data inicial e final da tela de geração da ECF."

- Só serão geradas informações neste bloco se o campo Forma de Tributação for igual a “Imune do  IRPJ” ou “ Isenta do IRPJ”.

- A exibição do conteúdo referente “Cód. do Registro” deve respeitar a sequência da coluna Código.

-Aplicar a RNG00051 - Geração dos Registros
-Na tela de Perfil de geração o registro deve estar selecionado para a geração.


		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		HYPERLINK "../../../../../../TFS/TaxObligation/ECF/03 - Subject-Features/Geração/Requirements/Atualização de Layout/Manual_de_Orientacao_da_ECF_31_05_2015_v2 (1).docx" \l "RU001"U001	1	Abertura do Bloco U – Imunes e Isentas
	F	O	[1:1]		HYPERLINK "../../../../../../TFS/TaxObligation/ECF/03 - Subject-Features/Geração/Requirements/Atualização de Layout/Manual_de_Orientacao_da_ECF_31_05_2015_v2 (1).docx" \l "RU030"U030	2	Identificação dos Períodos e Formas de Apuração do IPRJ e da CSLL das Empresas Imunes e Isentas	F	OC
Obrigatório se 
0010. FORMA_TRIB   = “8” ou “9”
N
Senão, Não deve existir	Se 
0010. FORMA_TRIB = “8” ou “9”
[1:4]
Senão [0]		HYPERLINK "../../../../../../TFS/TaxObligation/ECF/03 - Subject-Features/Geração/Requirements/Atualização de Layout/Manual_de_Orientacao_da_ECF_31_05_2015_v2 (1).docx" \l "U100"U100	3	Balanço Patrimonial 	F	OC
Obrigatório se 
0010. FORMA_TRIB = “8” ou “9” E
(0010. FORMA_APUR_I = “A” ou “T”
OU
0010.APUR_CSLL = “A” ou “T”)
F
Senão, o campo é facultativo.	Se 
0010. FORMA_TRIB = “8” ou “9” E
(0010. FORMA_APUR_I = “A” ou “T”
OU
0010.APUR_CSLL = “A” ou “T”)
 [1:N]
Senão [0:N]		HYPERLINK "../../../../../../TFS/TaxObligation/ECF/03 - Subject-Features/Geração/Requirements/Atualização de Layout/Manual_de_Orientacao_da_ECF_31_05_2015_v2 (1).docx" \l "U150"U150	3	 Demonstração do Resultado	F	OC
Obrigatório se 
0010. FORMA_TRIB = “8” ou “9” E
(0010. FORMA_APUR_I = “A” ou “T”
OU
0010.APUR_CSLL = “A” ou “T”)
F
Senão, o registro é facultativo.	Se 
0010. FORMA_TRIB = “8” ou “9” E
(0010. FORMA_APUR_I = “A” ou “T”
OU
0010.APUR_CSLL = “A” ou “T”)
 [1:N]
Senão [0:N]		HYPERLINK "../../../../../../TFS/TaxObligation/ECF/03 - Subject-Features/Geração/Requirements/Atualização de Layout/Manual_de_Orientacao_da_ECF_31_05_2015_v2 (1).docx" \l "U180"U180	3	Cálculo do IRPJ das Empresas Imunes ou Isentas	F	OC
Obrigatório se 
0010. FORMA_TRIB = “8” ou “9” E
0010. FORMA_APUR_I = “A” ou “T”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB = “8” ou “9” E
0010. FORMA_APUR_I = “A” ou “T”
 [1:N]
Senão [0]		HYPERLINK "../../../../../../TFS/TaxObligation/ECF/03 - Subject-Features/Geração/Requirements/Atualização de Layout/Manual_de_Orientacao_da_ECF_31_05_2015_v2 (1).docx" \l "RU182"U182	3	Cálculo da CSLL das Empresas Imunes ou Isentas	F	OC
Obrigatório se 
0010. FORMA_TRIB = “8” ou “9” E
0010.APUR_CSLL = “A” ou “T” OU
0010. FORMA_APUR_I = “A” ou “T”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB = “8” ou “9” E
0010.APUR_CSLL = “A” ou “T” OU
0010. FORMA_APUR_I = “A” ou “T”
 [1:N]
Senão [0]		HYPERLINK "../../../../../../TFS/TaxObligation/ECF/03 - Subject-Features/Geração/Requirements/Atualização de Layout/Manual_de_Orientacao_da_ECF_31_05_2015_v2 (1).docx" \l "RU990"U990	1	Encerramento do Bloco U
	F	O	[1:1]		
Registro U001: Abertura do Bloco U
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGU001-01	REG – Tipo de Registro

Gerar fixo ‘U001’	Sim	
MFS-17094		RNGU001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco U (registros U030, U100, U150, U180, U182), preencher com “0”, caso contrário, preencher com “1”.	Sim	 MFS-17094		
Registro U030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas
Campo Chave: PER_APUR
Ocorrência: 0:4
Nível Hierárquico – 2

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGU030	Só serão geradas informações neste bloco se o campo 05 – FORMA_TRIB do registro 0010 estiver preenchido com “8” ou “9” conforme RNP01 documento MTZ_Processamento_em_Lote.docx.  


Forma de Tributação = ‘Anual’ 


Deverá ser gerado um registro U030 A01 à A12 conforme recuperação da RNP01 – para o Período da Apuração = “Anual” e parâmetro Tipo (aba Tipo de Receita) da tela Complementares = ‘Balanço Suspensão ou Redução’. Neste caso, o registro A01...A12 deverá ser criado de forma sequencial (A01....A12) considerando o ‘período de apuração’, onde :

Janeiro = A01
Fevereiro = A02
Março = A03
.
.
.
Dezembro = A12

Deverá ser gerado um registro U030 A00 conforme recuperação da RNP01 – para o Período da Apuração = “Anual”.


Forma de Tributação = ‘Trimestral’ 

Deverá ser gerado um registro L030 para cada abertura de apuração da escrituração, com forma de tributação = “Imune do IRPJ” ou “Isenta do IRPJ”. Neste caso, o registro T01...T04 deverá ser criado de forma sequencial (T01....T04) considerando o ‘período de apuração’, onde:

1º Trimestre = T01
2 º Trimestre = T02
3 º Trimestre = T03
4 º Trimestre = T04
		RNGU030-01	REG – Tipo de Registro

Gerar fixo ‘U030’	Sim		RNGU030-02	DT_INI - Data do Início do Período

A00, A01...A12 

Preencher este campo com a data inicial primeira abertura de apuração encontrada no período parametrizado na tela de geração do ECF para o estabelecimento matriz/SCP.
Exemplo: 
A02 - Data inicial: 01/01/2014

T01...T04
Preencher este campo com a data inicial da abertura de apuração criado para o estabelecimento matriz/SCP.
Exemplo: 
T02 - Data inicial: 01/04/2014
	Sim		RNGU030-03	DT_FIN - Data do Fim do Período

A00, A01...A12 e T01...T04


Preencher este campo com a data final da abertura de apuração do período que está sendo gerado para o estabelecimento matriz/SCP.

Exemplo: 
A02 - Data final: 28/02/2014
T02 – Data final: 30/06/2014
	Sim		RNGU030-04	PER_APUR - Período de Apuração

Preencher conforme RNGU030.	Sim		

Registro U100: Balanço Patrimonial
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG		RNGU100	
Só devem ser gerados estes registros se um dos campos 12- FORMA_APUR_I ou 13 - APUR_CSLL  do registro 0010 = ‘A’ ou ‘T’. Para as demais situações, o registro é de geração facultativa, portanto se o registro U100 foi processado na importação de saldos e estiver marcado na tela de perfil de geração, o mesmo deve ser gerado.

As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela de demonstração do resultado do processamento dos registros) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.


Regras de Recuperação:
Recuperar o saldo final dos registros que foram processados na importação de saldos, através da tabela referencial cujo campo registro seja iniciado com ‘U100’.

 		RNGU100-01	REG – Tipo de Registro

Gerar fixo ‘U100’	Sim		RNGU100-02	CODIGO - Código da Conta Referencial

Preencher com o Cód. da Conta Referencial de cada registro recuperado.	Sim		RNGU100-03	DESCRICAO - Descrição

Preencher com o Desc. da Conta Referencial de cada registro recuperado.	Não		RNGU100-04	TIPO - Tipo de Conta 

Preencher com o Tipo de Conta de cada registro recuperado.	Sim		RNGU100-05	NIVEL- Nível da Conta

Preencher com o Nível da Conta de cada registro recuperado.	Não		RNGU100-06	COD_NAT- Natureza da Conta

Preencher com a Natureza da Conta da tabela de Plano de Conta Referencial correspondente a cada registro recuperado.	Não		RNGU100-07	COD_CTA_SUP - Código Conta Superior

Preencher com o Código da Conta Superior da tabela de Plano de Conta Referencial correspondente a cada registro recuperado.	Não		RNGU100-08	VAL_CTA_REF_INI - Valor do Saldo Inicial da Conta Referencial

Preencher com o Valor do Saldo Inicial da Conta Referencial de cada registro recuperado.	Sim		RNGU100-09	IND_VAL_CTA_REF_INI - Indicador do Saldo Inicial da Conta Referencial

Preencher com o Ind. do Saldo Inicial da Conta Referencial de cada registro recuperado.	Sim		RNGU100-10	VAL_CTA_REF_FIN - Valor do Saldo Final

Preencher com o Valor do Saldo Final da Conta Referencial de cada registro recuperado.	Sim		RNGU100-11	IND_ VAL_CTA_REF_FIN - Indicador do Saldo Final

Preencher com o Ind. do Saldo Final da Conta Referencial de cada registro recuperado.	Sim		Registro U150: Demonstração do Resultado 
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGU150	
Só devem ser gerados estes registros se um dos campos 12- FORMA_APUR_I ou 13 - APUR_CSLL  do registro 0010 = ‘A’ ou ‘T’. Para as demais situações, o registro é de geração facultativa, portanto se o registro U150 foi processado na importação de saldos e estiver marcado na tela de perfil de geração, o mesmo deve ser gerado.

As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela de demonstração do resultado do processamento dos registros) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.


Regras de Recuperação:
Recuperar o saldo final dos registros que foram processados na importação de saldos, através da tabela referencial cujo campo registro seja iniciado com ‘U150’.
		RNGU150-01	REG – Tipo de Registro

Gerar fixo ‘U150’	Sim		RNGU150-02	CODIGO - Código da Conta referencial

Preencher com o Cód. da Conta Referencial de cada registro recuperado.	Sim		RNGU150-03	DESCRICAO - Descrição

Preencher com o Desc. da Conta Referencial de cada registro recuperado.	Não		RNGU150-04	TIPO - Tipo da Conta

Preencher com o Tipo de Conta de cada registro recuperado.	Sim		RNGU150-05	NIVEL - Nível da Conta

Preencher com o Nível de Conta de cada registro recuperado.	Não		RNGU150-06	COD_NAT - Natureza da Conta

Preencher com a Natureza da Conta da tabela de Plano de Conta Referencial correspondente a cada registro recuperado.	Não		RNGU150-07	COD_CTA_SUP - Código da Conta Sintética Superior

Preencher com o Código da Conta Sintética Superior da tabela de Plano de Conta Referencial correspondente a cada registro recuperado.	Não		RNGU150-08	VALOR - Valor Total

Preencher com o Valor do Saldo Final de cada registro recuperado.	Sim		RNGU150-09	IND_ VALOR - Indicador do Saldo Final da Conta 

Preencher com o Ind. do Saldo Final de cada registro recuperado.	Sim		
Registro U180: Cálculo do IRPJ das Empresas Imunes ou Isentas Campo Chave: CODIGO
Campo Chave: CODIGO
Ocorrência: 0:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGU180	Só devem ser gerados os registros se o campo 05 - FORMA_TRIB do registro 0010 = “8” ou “9” e   campo 12 - FORMA_APUR_I = “A” ou “T”

Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro U180), considerando os parâmetros da RNG-U. 

Documentação de apoio:
A regra de processamento do registro U180 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGU180-01	REG – Tipo de Registro

Gerar fixo ‘U180’	Sim		RNGU180-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGU180-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGU180-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		

Registro U182: Cálculo da CSLL das Empresas Imunes ou Isentas
Campo Chave: CODIGO
Ocorrência: 1:N
Nível Hierárquico – 3

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGU182	Só devem ser gerados os registros se o campo 05 - FORMA_TRIB do registro 0010 = “8” ou “9”  e   campo 13 - APUR_CSLL = “A” ou “T” ou se campo 12 - FORMA_APUR_I = “A” ou “T”

Para a geração deste registro, recuperar as informações da tabela de resultado do processamento (tela de demonstração do resultado tabela dinâmica - registro U182), considerando os parâmetros da RNG-U. 


Documentação de apoio:
A regra de processamento do registro U182 pode ser encontrada no documento MTZ_Processamento_em_Lote.docx.
		RNGU182-01	REG – Tipo de Registro

Gerar fixo ‘U182’	Sim		RNGU182-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGU182-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGU182-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		

Registro U990: Encerramento do Bloco U
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 1

Condições Gerais: 

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGU990-01	REG – Tipo de Registro

Gerar fixo ‘U990’	Sim	 MFS-17094		RNGU990-02	QTD_LIN – Quantidade Total de Registro do Bloco U

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco U e informar o total.
Considerando Campo 1: Texto fixo contendo "U990", e campo 2: Quantidade total de linhas do bloco U.

Exemplo: |U990|25|
	Sim	 MFS-17094		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN