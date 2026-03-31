# MTZ_ECF_BlocoY

> Fonte: MTZ_ECF_BlocoY.doc

THOMSON REUTERS

Geração Bloco Y


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		02/07/2018	MFS-17098	Criação do Documento (Abertura e Encerramento do bloco Y)	Alessandra Cristina Navatta		
 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc431972959" INTRODUÇÃO	 PAGEREF _Toc431972959 \h 6
 HYPERLINK \l "_Toc431972960" 1.	Regras de Negócio	 PAGEREF _Toc431972960 \h 6
 HYPERLINK \l "_Toc431972961" 1.1	Informações gerais de seleção e processamento	 PAGEREF _Toc431972961 \h 6
 HYPERLINK \l "_Toc431972962" 1.2	Registros Identificadores	 PAGEREF _Toc431972962 \h 6
 HYPERLINK \l "_Toc431972963" 1.2.1	Registro Y001: Abertura do Bloco Y	 PAGEREF _Toc431972963 \h 11
 HYPERLINK \l "_Toc431972964" 1.2.2	Registro Y520: Pagamentos/Recebimentos do Exterior ou de Não Residentes	 PAGEREF _Toc431972964 \h 12
 HYPERLINK \l "_Toc431972965" 1.2.3	Registro Y540: Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica	 PAGEREF _Toc431972965 \h 13
 HYPERLINK \l "_Toc431972966" 1.2.4	Registro Y550: Vendas a Comercial Exportadora com Fim Específico de Exportação	 PAGEREF _Toc431972966 \h 14
 HYPERLINK \l "_Toc431972967" 1.2.5	Registro Y560: Detalhamento das Exportações da Comercial Exportadora	 PAGEREF _Toc431972967 \h 15
 HYPERLINK \l "_Toc431972968" 1.2.6	Registro Y570: Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte	 PAGEREF _Toc431972968 \h 16
 HYPERLINK \l "_Toc431972969" Campo Chave: CNPJ_FON + COD_REC	 PAGEREF _Toc431972969 \h 16
 HYPERLINK \l "_Toc431972970" 1.2.7	Registro Y580: Doações a Campanhas Eleitorais	 PAGEREF _Toc431972970 \h 18
 HYPERLINK \l "_Toc431972971" 1.2.8	Registro Y590: Ativos no Exterior	 PAGEREF _Toc431972971 \h 20
 HYPERLINK \l "_Toc431972972" 1.2.9	Registro Y600: Identificação de Sócios ou Titular	 PAGEREF _Toc431972972 \h 21
 HYPERLINK \l "_Toc431972973" 1.2.10	Registro Y611: Rendimentos de Dirigentes, Conselheiros, Sócios  ou Titular	 PAGEREF _Toc431972973 \h 23
 HYPERLINK \l "_Toc431972974" 1.2.11	Registro Y612: Rendimentos de Dirigentes e  Conselheiros, Imunes e Isentas	 PAGEREF _Toc431972974 \h 25
 HYPERLINK \l "_Toc431972975" 1.2.12	Registro Y620: Participações Avaliada pelo Método de Equivalência Patrimonial	 PAGEREF _Toc431972975 \h 26
 HYPERLINK \l "_Toc431972976" Campo Chave: Todos os campos do registro	 PAGEREF _Toc431972976 \h 26
 HYPERLINK \l "_Toc431972977" 1.2.13	Registro Y630: Fundos/Clubes de Investimento	 PAGEREF _Toc431972977 \h 29
 HYPERLINK \l "_Toc431972978" 1.2.14	Registro Y640: Participações em Consórcios de Empresa	 PAGEREF _Toc431972978 \h 30
 HYPERLINK \l "_Toc431972979" 1.2.15	Registro Y650: Participantes do Consórcio	 PAGEREF _Toc431972979 \h 31
 HYPERLINK \l "_Toc431972980" 1.2.16	Registro Y660: Dados de Sucessoras	 PAGEREF _Toc431972980 \h 32
 HYPERLINK \l "_Toc431972981" 1.2.17	Registro Y665: Demonstrativo das Diferenças na Adoção Inicial	 PAGEREF _Toc431972981 \h 33
 HYPERLINK \l "_Toc431972982" 1.2.18	Registro Y671: Outras Informações	 PAGEREF _Toc431972982 \h 36
 HYPERLINK \l "_Toc431972983" 1.2.19	Registro Y672: Outras Informações (Lucro Presumido ou Lucro Arbitrado)	 PAGEREF _Toc431972983 \h 39
 HYPERLINK \l "_Toc431972984" 1.2.20	Registro Y680: Mês das Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)	 PAGEREF _Toc431972984 \h 44
 HYPERLINK \l "_Toc431972985" 1.2.21	Registro Y681: Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)	 PAGEREF _Toc431972985 \h 45
 HYPERLINK \l "_Toc431972986" 1.2.22	Registro Y682: Informações de Optantes pelo Refis - Imunes ou Isentas	 PAGEREF _Toc431972986 \h 46
 HYPERLINK \l "_Toc431972987" 1.2.23	Registro Y690: Informações de Optantes pelo Paes	 PAGEREF _Toc431972987 \h 47
 HYPERLINK \l "_Toc431972988" 1.2.24	Registro Y800: Outras Informações	 PAGEREF _Toc431972988 \h 47
 HYPERLINK \l "_Toc431972989" 1.2.25	Registros Y990: Encerramento do Bloco Y	 PAGEREF _Toc431972989 \h 48
 HYPERLINK \l "_Toc431972990" 1.2.26	Registro Y720: Informações de Períodos Anteriores:	 PAGEREF _Toc431972990 \h 49
 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO
Este bloco tem o objetivo de apresentar as informações gerais da empresa, caso existam.

Regras de Negócio
Informações gerais de seleção e processamento

As regras destacadas em amarelo com fonte em vermelho não serão implementadas neste momento.

CÓD	DESCRIÇÃO	MFS		RNG-Y	Período de recuperação dos registros: Data Inicial das Informações da ECF e a Data Final da última Apuração durante o Processamento em Lote.

Recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y)

Se o Registro estiver como OC no campo ‘Obrigatoriedade Saída’ (item 1.2 deste documento), for de nível igual a “2” e as regras do registro forem cumpridas, mas não existir dados na tela (mencionada na regra geral do registro), exibir a mensagem DW00187

Se o Registro estiver como OC no campo ‘Obrigatoriedade Saída’ (item 1.2 deste documento), for de nível igual a “3” e as regras do registro forem cumpridas, mas não existir dados na tela (mencionada na regra geral do registro), exibir a mensagem DW00247.

Se o Registro estiver como O no campo ‘Obrigatoriedade Saída’ (item 1.2 deste documento), for de nível igual a “3”, o Registro pai estiver como OC no campo ‘Obrigatoriedade Saída’ e as regras do registro forem cumpridas, mas não existir dados na tela (mencionada na regra geral do registro), exibir a mensagem DW00247.


Para identificar os campos-chave para a mensagem DW00247 utilizar a tabela abaixo:

Registro
Pai
Chave Pai

Y650
Y640
CNPJ

Y681
Y680
MÊS


Na tela de Perfil de geração o registro deve estar selecionado para a geração.

		MFS-17098		
Registros Identificadores
Relação de Registros a serem gerados

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		 HYPERLINK  \l "RY001" Y001	1	Abertura do Bloco Y – Informações Gerais
	F	O	[1:1]		HYPERLINK \l "RY520"Y520	2	Pagamentos/Recebimentos do Exterior ou de Não Residentes	F	OC
Obrigatório se 
0020.IND_ REC_EXT = "S" OU 0020.IND_PGTO_EXT = "S"
N
Senão, não deve existir.	Se 
0020.IND_ REC_EXT = "S" OU
0020.IND_PGTO_EXT = "S"
[1:N]
Senão
[0]		HYPERLINK \l "RY540"Y540	2	Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica	F	 F
N
Não deve existir se 0010.TIP_ENT = “06”, “13” ou “14”


	[0:N]

Não deve existir se 0010.TIP_ENT = “06”, “13” ou “14”
		HYPERLINK \l "RY550"Y550	2	Vendas a Comercial Exportadora com Fim Específico de Exportação	F	OC
Obrigatório se 
0020. IND_VEND_EXP = "S"
N
Senão, não deve existir.	Se 
0020. IND_VEND_EXP = "S"
 [1:N]
Senão
[0]		HYPERLINK \l "RY560"Y560	2	Detalhamento das Exportações da Comercial Exportadora
	F	OC
Obrigatório se 
0020.IND_COM_EXP = "S"
N
Senão, não deve existir.	Se
0020.IND_COM_EXP = "S"
 [1:N]

Senão
[0]		HYPERLINK \l "RY570"Y570	2	Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte	F	F
N
Não deve existir se 0010.FORMA_APUR_I = “D” E 0010.APUR_CSLL = “D”
	[0:N]
Não deve existir se 0010.FORMA_APUR_I = “D” E 0010.APUR_CSLL = “D”		HYPERLINK \l "RY580"Y580	2	Doações a Campanhas Eleitorais	F	OC
Obrigatório se 
0020.IND_DOA_ELEIT = "S"N
Senão, não deve existir.	Se 
0020.IND_DOA_ELEIT = "S"
 [1:N]
Senão
[0]		HYPERLINK \l "RY590"Y590	2	Ativos no Exterior	F	OC
Obrigatório se 
0020.IND_ATIV_EXT = "S"
N
Senão, não deve existir.	Se 
0020.IND_ATIV_EXT = "S" 
[1:N]
Senão
[0:N]		HYPERLINK \l "RY600"Y600	2	Identificação de Sócios ou Titular
A partir da versão 3.0, este registro passa a se chamar:
Identificação e Remuneração de Sócios, Titulares, Dirigentes e Conselheiros
	F	Obrigatório se
0010.FORMA_TRIB = "1" a "7" E
N
Senão, não deve existir.	Se 
0010.FORMA_TRIB = "1" a "7" 
 [1:N]
Senão [0] 		HYPERLINK \l "RY611"Y611	2	Rendimentos de Dirigentes, Conselheiros, Sócios ou Titular

Versionamento [Layout 31/12/2015] – Registro deve ser considerado até versão 1.0	F
	Até versão 1.00

OC
Obrigatório se
0010.FORMA_TRIB = "1" a "7"
N
Senão, não deve existir.

Não Gerar a partir da versão 2.00	Até versão 1.00


Se 
0010.FORMA_TRIB = "1" a "7"
 [1:N]
Senão  
[0]

Não Gerar a partir da versão 2.00		HYPERLINK \l "RY612"Y612	2	Rendimentos de Dirigentes e Conselheiros - Imunes ou Isentas	F	FC
Pode ser preenchido se
0010.FORMA_TRIB = "8" ou "9"
N
Senão, não deve existir.	Se 
0010.FORMA_TRIB = “8” e “9”
[0:N]
Senão
[0]		HYPERLINK \l "RY620"Y620	2	Participações Avaliadas pelo Método de Equivalência Patrimonial	F	OC
Obrigatório se 
0020.IND_PART_COLIG = "S" 
N
Senão, não deve existir.	Se 
0020.IND_PART_COLIG = "S

 [1:N]
Senão 
[0]		HYPERLINK \l "RY630"Y630	2	Fundos/Clubes de Investimento	F	OC
Obrigatório se
0020.IND_ADM_FUN_CLU = "S"
N
Senão, não deve existir.	Se 
0020.IND_ADM_FUN_CLU = "S"
 [1:N]
Senão 
[0]		HYPERLINK \l "RY640"Y640	2	Participações em Consórcios de Empresas	F	OC
Obrigatório se 
0020.IND_PART_CONS = "S" 
N
Senão, não deve existir.	Se 
0020.IND_PART_CONS = "S"
 [1:N]
Senão 
[0]		HYPERLINK \l "RY650"Y650	3	Participantes do Consórcio
	F	OC
Obrigatório se 
Y640.COND_DECL="1" 
N
Senão, não deve existir	Se Y640.COND_DECL = “1”
[1:N]
Senão
[0]		HYPERLINK \l "RY660"Y660	2	Dados de Sucessoras	F
	OC
Obrigatório se 
0010.SIT_ESPECIAL = “2”, “3”, “5” ou “6”
N
Senão, não deve existir.


	Se 
0010.SIT_ESPECIAL = “2”, “3”, “5” ou “6”
 [1:N]
Senão 
[0]		Y665	2	Demonstrativo das Diferenças na Adoção Inicial
	F	OC
Obrigatório se 
0010.DIF_FCONT = "S"

Facultativo se
0010.FORMA_TRIB = “8” ou “9”
N
Senão, não deve existir.

Não Gerar a partir da versão 3.00	Se 
0010.DIF_FCONT = "S" E
[1:N]

Se 0010.FORMA_TRIB = “8” ou “9”
[0:N]
Senão
[0]

Não Gerar a partir da versão 3.00		HYPERLINK \l "RY671"Y671	2	Outras Informações
	F	OC
Obrigatório se
0010.FORMA_TRIB = “1”, “2”, “3” ou “4”
N
Senão, não deve existir.  	Se 
0010.FORMA_TRIB = “1”, “2”, “3” ou “4”
 [1:1]
Senão
[0]		HYPERLINK \l "Y672"Y672	2	Outras Informações (Lucro Presumido ou Lucro Arbitrado)


	F	OC
Obrigatório se
0010.FORMA_TRIB = “5”, “6” ou “7” 
N
Senão, não deve existir. 	Se 
0010.FORMA_TRIB =  5 ,  6  ou  7  
[1:1]
Senão
[0] 		HYPERLINK \l "RY680"Y680	2	Mês das Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)	F	OC
Obrigatório se 
0010.OPT_REFIS="S" E
0010.FORMA_TRIB `"  8  e  9 
N
Senão, não deve existir.	Se 
0010.OPT_REFIS="S" E
0010.FORMA_TRIB `"  8  e  9 
 [1:12]
Senão
[0] 		HYPERLINK \l "RY681"Y681	3	Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)	F	OC
Obrigatório se
0010.OPT_REFIS="S" E
0010.FORMA_TRIB `"  8  e  9 
N
Senão, não deve existir.	Se 
0010.OPT_REFIS="S" E
0010.FORMA_TRIB `"  8  e  9 
 [1:12]
Senão
[0]		HYPERLINK \l "RY682"Y682	2	Informações de Optantes pelo Refis - Imunes ou Isentas	F	OC
Obrigatório se 
0010.OPT_REFIS="S" E
0010.FORMA_TRIB =  8  e  9 (**)
N
Senão, não deve existir.

	Se 
0010.OPT_REFIS="S" E
0010.FORMA_TRIB =“8” e “9”(**)
 [1:12]
Senão
[0] 

		HYPERLINK \l "RY690"Y690	2	Informações de Optantes pelo Paes	F	OC
Obrigatório se 
0010.OPT_PAES = "S"
N
Senão, não deve existir.	Se 
0010.OPT_PAES = "S"
[1:12]
Senão
[0]		Y700	2	Declaração de Informações de Operações Relevantes (DIOR)	F	F

Não gerar a partir da versão 2.00	[0:N]

Não gerar a partir da versão 2.00		Y710	3	Tributos Vinculados a DIOR	F	F

Não gerar a partir da versão 2.00	[0:N]

Não gerar a partir da versão 2.00		Y720	2	Informação de Períodos Anteriores	F	OC
Obrigatório se a entrega da escrituração é feita com atraso.
                                    F
Senão, é facultativo	OC
Obrigatório se a entrega da escrituração é feita com atraso.   [1:1]
Senão [0]		Y800	2	Outras Informações
	F	F	[0:1]		HYPERLINK \l "RY990"Y990	1	Encerramento do Bloco Y
	F	O	[1:1]		

Registro Y001: Abertura do Bloco Y
Campo Chave: REG
Ocorrência: 1:1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGY001-01	REG – Tipo de Registro

Gerar fixo ‘Y001’	SIM	MFS-17098		RNY001-02	IND_DAD - Indicador de  Movimento

Caso existam informações nos registros do bloco Y (registros Y520,Y540,Y550,Y560,Y570,Y580,Y590,Y600,Y611,Y612,Y620,Y630,Y640,Y650,Y660,Y665,Y671,Y672,Y680,Y681, Y682,Y690, Y800) preencher com “0”, caso contrário, preencher com “1”.
	SIM	MFS-17098		Registro Y520: Pagamentos/Recebimentos do Exterior ou de Não Residentes 
Campo Chave: TIP_EXT + PAIS + FORMA + NAT_OPER
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY520	Para a geração deste registro, recuperar as informações  da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y520, considerando os parâmetros da RNG-Y 

No Registro 0020, o campo 17 – IND_REC_EXT = ‘S’ ou campo 20- IND_PGTO_EXT = ‘S’.

Outras Validações:

Verifica se o campo 17 – IND_REC_EXT  do registro 0020 = ‘S’, se existe ao menos um Y520 com o campo TIP_EXT  = ‘R’, senão exibir msg de erro TR00631

Verifica se o campo 20- IND_PGTO_EXT  do registro 0020 = ‘S’, se existe ao menos um Y520 com o campo TIP_EXT  = ‘P’, senão exibir msg de erro TR00632

Mesmo em caso de erro de validação o registro deve ser gerado.
		RNGY520-01	REG – Tipo de Registro

Gerar fixo ‘Y520’	Sim		RNGY520-02	TIP_EXT – Tipo

Preencher com o Tipo de cada registro recuperado. 	Sim		RNGY520-03	PAIS– País

Preencher com o País de cada registro recuperado.

	Sim		RNGY520-04	FORMA – Forma de Recebimento/Pagamento

Preencher com a Forma de Recebimento/Pagamento de cada registro recuperado.

	Sim		RNGY520-05	NAT_OPER – Natureza da Operação

Preencher com a Natureza da Operação de cada registro recuperado.
	Sim		RNGY520-06	VL_PERIODO – Valor

Preencher com o Valor de cada registro recuperado.
	Sim		
Registro Y540: Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica
Campo Chave: CNPJ_ESTAB + CNAE
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY540	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y540, considerando os parâmetros da RNG-Y e se

No registro 0010.TIP_ENT `"  06 ,  13  ou  14 
 

Verifica se 0010.TIP_ENT =  06 ,  13  ou  14 , se sim exibir a seguinte mensagem de erro:
TR00753		RNGY540-01	REG   Tipo de Registro

Gerar fixo  Y540 	Sim		RNGY540-02	CNPJ_ESTAB   CNPJ

Preencher com o CNPJ de cada registro recuperado.

	Sim		RNGY540-03	VL_REC_ESTAB – Receita de Vendas

Preencher com a Receita de Vendas de cada registro recuperado.

	Sim		RNGY540-04	CNAE – CNAE

Preencher com o CNAE de cada registro recuperado.

	Sim		Registro Y550: Vendas a Comercial Exportadora com Fim Específico de Exportação 
Campo Chave: CNPJ_EXP + COD_NCM
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY550	Para a geração deste registro, recuperar as informações  da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y550, considerando os parâmetros da RNG-Y e se 

No registro 0020, o campo 16 – IND_VEND_EXP = ‘S’ 

		RNGY550-01	REG – Tipo de Registro

Gerar fixo ‘Y550’	Sim		RNGY550-02	CNPJ_EXP – CNPJ

Preencher com o CNPJ de cada registro recuperado.

Se CNPJ for igual ao campo 04 -CNPJ do registro 0000, exibir a msg de erro TR00626
	Sim		RNGY550-03	COD_NCM – Código NCM

Preencher com o Código NCM de cada registro recuperado.
Verificar se o código inserido possui 8 posições, caso seja inferior exibir a TR01394.

	Sim		RNGY550-04	VL_VENDA – Valor da Venda

Preencher com o Valor da Venda de cada registro recuperado.

	Sim		Registro Y560: Detalhamento das Exportações da Comercial Exportadora 
Campo Chave: CNPJ + COD_NCM
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY560	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y560, considerando os parâmetros da RNG-Y e se 

No registro 0020, o campo 19 – IND_COM_EXP = ‘S’
		RNGY560-01	REG – Tipo de Registro

Gerar fixo ‘Y560’	Sim		RNGY560-02	CNPJ– CNPJ

Preencher com o CNPJ de cada registro recuperado.

Até versão 1.0

Se CNPJ for igual ao campo 04 -CNPJ do registro 0000, exibir a mensagem de erro TR00626.


A partir da versão 2.0, conforme alteração layout [11/03/2016]: 

O campo CNPJ permite campo igual ao 04 -CNPJ do registro 0000, pois:

Em caso de aquisição de produtor rural sem CNPJ, quando o contribuinte é obrigado a emitir nota fiscal de entrada referente à aquisição das mercadorias, utilizar o CNPJ da declarante.

	Sim		RNGY560-03	COD_NCM – Código NCM

Preencher com o Código NCM de cada registro recuperado.
Verificar se o código inserido possui 8 posições, caso seja inferior exibir a TR01394.

	Sim		RNGY560-04	VL_COMPRA – Valor da Compra

Preencher com o Valor da Compra de cada registro recuperado.

	Não		RNGY560-05	VL_EXP – Valor da Exportação

Preencher com o Valor da Exportação de cada registro recuperado.

	Não		Registro Y570: Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte 
Campo Chave: CNPJ_FON + COD_REC
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY570	Para a geração deste registro, recuperar as informações  da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y570, considerando os parâmetros da RNG-Y e se 

No registro 0010, o campo 12 FORMA_APUR_I `"  D 
		RNGY570-01	REG   Tipo de Registro

Gerar fixo  Y570 	Sim		RNGY570-02	CNPJ_FON  CNPJ

Preencher com o CNPJ de cada registro recuperado.
	Sim		RNGY570-03	NOM_EMP   Nome Empresarial

Preencher com o Nome Empresarial de cada registro recuperado.

	Sim		RNGY570-04	IND_ORG_PUB – Indicador de Órgão Público

Preencher com o Indicador de Órgão Público de cada registro recuperado.

	Sim		RNGY570-05	COD_REC – Código de Receita

Preencher com o Código de Receita de cada registro recuperado.

	Sim		RNGY570-06	VL_REND – Rendimento Bruto/Receita

Preencher com o Rendimento Bruto/Receita de cada registro recuperado.

	Sim		RNGY570-07	IR_RET – IR Retido na Fonte

Preencher com o IR Retido na Fonte de cada registro recuperado.
Se o conteúdo do campo Código de Receita (COD_REC) campo é igual a5928 ou 5936 ou 5944 ou 6147 ou 6175 ou 6188 ou 6190 ou 6256 ou 8739 ou 8767 ou 8850 ou 8863 ou 9060 ou 9997 ou 0916 ou 0924 ou 1708 ou 3277 ou 3280 ou 3426 ou 5204 ou 5232 ou 5273 ou 5557 ou 5706 ou 5928 ou 5936 ou 5944 ou 6800 ou 6813 ou 8045 ou 8468 ou 9385 ou 9999 está preenchido e Verifica, quando (N620 linha (21) ou N620 linha (23) ou N620 linha (24) forem maiores que zero); ou (campo 7 -COD_QUALIF_PJ = “1”  do registro 0010 e (N630 linha (20) ou N630 linha (21) ou N630 linha (22)) forem maiores que zero); ou (campo7- COD_QUALIF_PJ  QUOTE   “1” do registro 0010 e (N630 linha (17) ou N630 linha (18) ou N630 linha (19)) forem maiores que zero); ou (P300 linha (10) ou P300 linha (12) ou P300 linha (13) forem maiores que zero); ou (T150 linha (11) ou T150 linha (13) ou T150 linha (14) forem maiores que zero); se IR_RET (Campo 07) está preenchido, senão exibe msg TR00633

Se  IR_RET (Campo 07) está preenchido e é diferente de 0,00 quando COD_REC (Campo 05) é diferente dos códigos de receita contidos na tabela FXD00045 para o IRRF, exibe a msg de alerta TR00559.
	Não		RNGY570-08	CSLL_RET – CSLL Retido na Fonte

Preencher com o CSLL Retido na Fonte de cada registro recuperado.
Se o conteúdo do campo Código de Receita (COD_REC) campo é igual a 4085 ou 4397 ou 5928 ou 5936 ou 5944 ou 6147 ou 6175 ou 6188 ou 6190 ou 6228 ou 8739 ou 8767 ou 8850 ou 8863 ou 9060 ou 9997 ou 5952 ou 5987 ou 9998 está preenchido e Verifica, quando (N660 linha (14) ou N660 linha(15) ou N660 linha (16) ou N660 linha (17) forem maiores que zero); ou ((N670 linha (15) ou N670 linha (16) ou N670 linha (17) ou N670 linha (18)) forem maiores que zero); ou (P500 linha (9) ou P500 linha (10) ou P500 linha (11) ou P500 linha (12) forem maiores que zero); ou (T181 linha (11) ou T181 linha (12) ou T181 linha (13) ou T181 linha(14) forem maiores que zero); se CSLL_RET (Campo 08) está preenchido, senão exibe msg TR00633.

-Se CSLL_RET (Campo 08) está preenchido e é diferente de 0,00 quando COD_REC (Campo 05) é diferente dos códigos de receita contidos na tabela FXD00045 para o CSLL exibe a msg de alerta:TR00559.	Não		Registro Y580: Doações a Campanhas Eleitorais  
Campo Chave: CNPJ + FORM_DOA
 Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY580	Para a geração deste registro, recuperar as informações  da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y580, considerando os parâmetros da RNG-Y e se 

No registro 0020 o campo14- IND_DOA_ELEIT = ‘S’
		RNGY580-01	REG – Tipo de Registro

Gerar fixo ‘Y580’	Sim		RNGY580-02	CNPJ– CNPJ do Beneficiário

Preencher com o CNPJ do Beneficiário de cada registro recuperado.

Se CNPJ for igual ao campo 04 -CNPJ do registro 0000, exibir a msg de erro TR00626

	Sim		RNGY580-03	TIP_BENEF – Tipo de Beneficiário

Preencher com o Tipo de Beneficiário de cada registro recuperado.

	Sim		RNGY580-04	FORM_DOA– Forma de Doação

Preencher com a Forma de Doação de cada registro recuperado.

	Sim		RNGY580-05	VL_DOA – Valor

Preencher com o Valor de cada registro recuperado.

	Sim		
Registro Y590: Ativos no Exterior 
Até versão 2.00:  Campo Chave: Todos os campos do registro.
Na versão 3.00 : TIP_ATIVO + DISCRIMINACAO

Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY590	Para a geração deste registro, recuperar as informações  da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y590, considerando os parâmetros da RNG-Y e se 

No registro 0020, o campo 18 – IND_ATIV_EXP = ‘S’ 		RNGY590-01	REG – Tipo de Registro

Gerar fixo ‘Y590’	Sim		RNGY590-02	TIP_ATIVO– Tipo de Ativo

Preencher com o Tipo de Ativo de cada registro recuperado.
	Sim		RNGY590-03	PAIS – País

Preencher com o País de cada registro recuperado.
	Sim		RNGY590-04	DISCRIMINACAO – Discriminação

Preencher com a Discriminação de cada registro recuperado.
	Sim		RNGY590-05	VL_ANT – Valor Anterior

Preencher com o Valor Anterior de cada registro recuperado.
	Sim		RNGY590-06	VL_ATUAL – Valor Atual

Preencher com o Valor Atual de cada registro recuperado.
	Sim		Registro Y600: Identificação de Sócios ou Titular 
A partir da versão 2.0, conforme alteração layout [11/03/2016], o registro passa a denominar: Identificação e Rendimentos de Dirigentes, Conselheiros, Sócios ou Titular

Campo Chave: Todos os campos do registro.
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY600	Para a geração deste registro, recuperar as informações  da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y600, considerando os parâmetros da RNG-Y e se 

No registro 0010, o campo FORMA_TRIB = "1" a "7"
		RNGY600-01	REG – Tipo de Registro

Gerar fixo ‘Y600’	Sim		RNGY600-02	DT_ALT_SOC– Data de Inclusão no Quadro Societário

Preencher com a Data de Inclusão no Quadro Societário cada registro recuperado.
	Sim		RNGY600-03	DT_FIM_SOC – Data de Saída do Quadro Societário

Preencher com a Data de Saída do Quadro Societário cada registro recuperado.

Se a data de Saída do Quadro socientário estiver preenchida, a mesam deve estar compreendida entre a DT_INI (campo10 ) do registro0000 e a DT_FIN (campo 11) do registro 0000, caso contrário exibir a msg de erro: TR00629
	Não		RNGY600-04	PAIS – País

Preencher com o País de cada registro recuperado.
	Sim		RNGY600-05	IND_QUALIF_SOCIO – Indicador de Qualificação do Sócio

Preencher com o Indicador de Qualificação do Sócio de cada registro recuperado.
	Sim		RNGY600-06	CPF_CNPJ – CPF ou CNPJ

Preencher com o CPF ou CNPJ de cada registro recuperado.

	Não		RNGY600-07	NOM_EMP – Nome ou Nome Empresarial

Preencher com o Nome ou Nome empresarial de cada registro recuperado.
	Sim		RNGY600-08	QUALIF – Qualificação

Preencher com a Qualificação de cada registro recuperado.

Se as regras abaixo, nao forem atendidas aplicar a TR00552                                         

Se PAIS (campo4) = “105”  E IND_QUALIF_SOCIO (campo5) = “PF”, este campo só pode ser preenchido com:
01 – Acionista Pessoa Física Domiciliado no Brasil
02 – Sócio Pessoa Física Domiciliado no Brasil
09 – Titular
10 – Administrador sem Vínculo Empregatício
11 – Diretor sem Vínculo Empregatício
12 – Presidente sem Vínculo Empregatício
13 – Administrador com Vínculo Empregatício
14 – Conselheiro de Administração ou Fiscal
15 – Diretor com Vínculo Empregatício
16 – Fundador
17 – Presidente com Vínculo Empregatício

Se PAIS (campo4)= “105”  E IND_QUALIF_SOCIO (campo5)= "PJ" ou "FI", este campo só pode ser preenchido com:
03 - Acionista Pessoa Jurídica Domiciliado no Brasil
04 - Sócio Pessoa Jurídica Domiciliado no Brasil

Se PAIS (campo4) diferente de “105” E IND_QUALIF_SOCIO (campo5) = "PF", este campo só pode ser preenchido com:
05 - Acionista Pessoa Física Residente ou Domiciliado no Exterior
06 - Sócio Pessoa Física Residente ou Domiciliado no Exterior

Se PAIS (campo4) diferente de “105” E IND_QUALIF_SOCIO (campo5) = "PJ" ou "FI", este campo só pode ser preenchido com:
07 - Acionista Pessoa Jurídica Residente ou Domiciliado no Exterior
08 - Sócio Pessoa Jurídica Residente ou Domiciliado no Exterior
	Sim		RNGY600-09	PERC_CAP_TOT– Percentual sobre o Capital Total

Preencher com o Percentual sobre o Capital Total de cada registro recuperado.

Se o percentual informado for maior que 100, ou ,menor que 0, exibir a  TR00091.
	Sim		RNGY600-10	PERC_CAP_VOT– Percentual sobre o Capital Votante

Preencher com o Percentual sobre o Capital Votante de cada registro recuperado.

Se o percentual informado for maior que 100, ou ,menor que 0, exibir a  TR00091.
	Sim		RNGY600-11	CPF_REP_LEG– CPF do Representante Legal

Preencher com o CPF do Representante Legal de cada registro recuperado.
	Não		RNGY600-12	QUALIF_REP_LEG– Qualificação do Representante Legal

Preencher com a Qualificação do Representante Legal de cada registro recuperado.	Não		RNGY600-13	Campo válido a partir da versão 2.0, conforme alteração layout [11/03/2016]

VL_REM_TRAB
Preencher com a Remuneração do Trabalho de cada registro recuperado.	Não		RNGY600-14	Campo válido a partir da versão 2.0, conforme alteração layout [11/03/2016]


VL_LUC_DIV

Preencher com os  Lucros/Dividendos de cada registro recuperado. 	
Não		RNGY600-15	Campo válido a partir da versão 2.0, conforme alteração layout [11/03/2016]


VL_JUR_CAP

Preencher com o Juros Sobre o Capital Próprio de cada registro recuperado. 	
Não		RNGY600-16	Campo válido a partir da versão 2.0, conforme alteração layout [11/03/2016]


VL_DEM_REND

Preencher com Demais Rendimentos: Valor, antes da dedução do imposto de renda retido na fonte, dos demais rendimentos pagos ou creditados a sócios, a acionistas ou a titular de empresa individual, inclusive os lucros e dividendos não apurados em balanço e distribuídos.
	


Não		RNGY600-17	Campo válido a partir da versão 2.0, conforme alteração layout [11/03/2016]


VL_IR_RET

Preencher com IR Retido na Fonte para cada registro recuperado.

	

Não		Registro Y611: Rendimentos de Dirigentes, Conselheiros, Sócios  ou Titular 
Campo Chave: Todos os campos do registro.

Ocorrência: 0:N

Validação Versionamento 

O registro Y611 deve ser considerado até a versão 1.0.
A partir da versão 2.0, se o sistema  identificar esse registro na geração da ECF, o mesmo deve ser desconsiderado e ao final da geração a mensagem TR01026 deve ser exibida. (WI-890459)

CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY611	Para a geração deste registro, recuperar as informações  da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y611, considerando os parâmetros da RNG-Y e se

No registro 0010, o campo 5 – FORMA_TRIB  `"  8  ou  9    
		RNGY611-01	REG   Tipo de Registro

Gerar fixo  Y611 	Sim		RNGY611-02	PAIS   País

Preencher com o País de cada registro recuperado.
	Sim		RNGY611-03	IND_PF_PJ   Indicador de Pessoa Física ou Pessoa Jurídica

Preencher com o Indicador de Pessoa Física ou Pessoa Jurídica de cada registro recuperado.
	Sim		RNGY611-04	CPF_CNPJ – CPF ou CNPJ

Preencher com o CPF ou CNPJ de cada registro recuperado.

Se campo 03 – IND_PF_PJ (campo 03) do registro Y611  =  ‘PJ’ é diferente do campo 04 –CNPJ do registro 0000, senão exibe a msg de erro TR00626
	Não		RNGY611-05	NOM_EMP – Nome ou Nome Empresarial

Preencher com o Nome ou Nome empresarial de cada registro recuperado.
	Sim		RNGY611-06	QUALIF – Qualificação

Preencher com a Qualificação de cada registro recuperado.
	Sim		RNGY611-07	VL_REM_TRAB – Remuneração do Trabalho

Preencher com a Remuneração do Trabalho de cada registro recuperado.
	Não		RNGY611-08	VL_LUC_DIV – Lucros/Dividendos

Preencher com o Lucro/Dividendos de cada registro recuperado.
	Não		RNGY611-09	VL_JUR_CAP– Juros sobre o Capital Próprio

Preencher com os Juros sobre o Capital Próprio de cada registro recuperado.
	Não		RNGY611-10	VL_DEM_REND– Demais Rendimentos

Preencher com os Demais Rendimentos de cada registro recuperado.
	Não		RNGY611-11	VL_IR_RET– IR Retido na Fonte

Preencher com o IR Retido na Fonte de cada registro recuperado.
	Não		Registro Y612: Rendimentos de Dirigentes e  Conselheiros, Imunes e Isentas 

A partir da versão 2.0, conforme alteração layout [11/03/2016], o registro passa a denominar: Identificação e Rendimentos de Dirigentes e Conselheiros – Imunes ou Isentas

Campo Chave: CPF+QUALIF
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY612	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y612, considerando os parâmetros da RNG-Y e se

No registro 0010, o campo 5 – FORMA_TRIB   = ‘8’ ou ‘9’   
		RNGY612-01	REG – Tipo de Registro

Gerar fixo ‘Y612’	Sim		RNGY612-02	CPF – CPF 

Preencher com o CPF de cada registro recuperado.
	Sim		RNGY612-03	NOME – Nome 

Preencher com o Nome de cada registro recuperado.
	Sim		RNGY612-04	QUALIF – Qualificação

Preencher com a Qualificação de cada registro recuperado.
	Sim		RNGY612-05	VL_REM_TRAB – Rendimentos do Trabalho

Preencher com os Rendimentos do Trabalho de cada registro recuperado.
	Não		RNGY612-06	VL_DEM_REND – Demais Rendimentos

Preencher com os Demais Rendimentos de cada registro recuperado.
	Não		RNGY612-07	VL_IR_RET – IR Retido na Fonte

Preencher com o IR Retido na Fonte de cada registro recuperado.
	Não		Registro Y620: Participações Avaliada pelo Método de Equivalência Patrimonial 
Campo Chave: Todos os campos do registro
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY620	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y620, considerando os parâmetros da RNG-Y e se

No registro 0020, o campo 15- IND_PART_COLIG =  ‘S’    
		RNGY620-01	REG – Tipo de Registro

Gerar fixo ‘Y620’	Sim		RNGY620-02	DT_EVENTO

Preencher com a Data do Evento de cada registro recuperado
	Sim		RNGY620-03	IND_RELAC

Preencher com o Indicador do Tipo de Relacionamento de cada registro recuperado.
	Sim		RNGY620-04	PAIS– País 

Preencher com o País de cada registro recuperado.
	Sim		RNGY620-05	CNPJ – CNPJ 

Preencher com o CNPJ de cada registro recuperado.

Se campo 03 -CNPJ (campo 03) do registro Y620’ é diferente do campo 04 –CNPJ do registro 0000, senão exibe a msg de erro TR00626
	Não		RNGY620-06	NOM_EMP – Nome Empresarial 

Preencher com o Nome Empresarial de cada registro recuperado.
	Sim		RNGY620-07	VALOR_REAIS – Valor da Participação em Reais 

Preencher com o Valor da Participação em Reais de cada registro recuperado.
	Sim		RNGY620-08	VALOR_ESTR – Valor da Participação em Moeda Original do País 

Preencher com o Valor da Participação em Moeda Original do País de cada registro recuperado.
	Sim		RNGY620-09	PERC_CAP_TOT– Percentual sobre o Capital Total

Preencher com o Percentual sobre o Capital Total de cada registro recuperado.
	Sim		RNGY620-10	PERC_CAP_VOT– Percentual sobre o Capital Votante

Preencher com o Percentual sobre o Capital Votante de cada registro recuperado.
	Sim		RNGY620-11	RES_EQ_PAT– Resultado de Equivalência Patrimonial

Preencher com o Resultado de Equivalência Patrimonial de cada registro recuperado.	Não		RNGY620-12	DATA_AQUIS– Data da Aquisição da Participação

Preencher com a Data da Aquisição da Participação de cada registro recuperado.
	Sim		RNGY620-13	IND_PROC_CART– Sumário em Cartório

Preencher com o Sumário em Cartório de cada registro recuperado.
	Não		RNGY620-14	NUM_PROC_CART–Número do Registro no Cartório

Preencher com o Número do Registro no Cartório de cada registro recuperado.
	Não		RNGY620-15	NOME _CART–Nome do Cartório

Preencher com o Nome do Cartório de cada registro recuperado.
	Não		RNGY620-16	IND_PROC_RFB–Laudo Protocolado na RFB

Preencher com o Laudo Protocolado na RFB de cada registro recuperado.
	Não		RNGY620-17	NUM_PROC_RFB–Número do Processo

Preencher com o Número do Processo de cada registro recuperado.
	Não		
Registro Y630: Fundos/Clubes de Investimento 
Campo Chave: CNPJ
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY630	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y630, considerando os parâmetros da RNG-Y e se 

No registro 0020 o campo4- IND_ADM_FUN_CLU = ‘S’ 
		RNGY630-01	REG – Tipo de Registro

Gerar fixo ‘Y630’	Sim		RNGY630-02	CNPJ– CNPJ

Preencher com o CNPJ de cada registro recuperado.
	Sim		RNGY630-03	QTE_QUOT– Quantidade de Quotistas no Final do Período

Preencher com a Quantidade de Quotistas no Final do Período de cada registro recuperado.
	Sim		RNGY630-04	QTE_QUOTA– Quantidade de Quotas no Final do Período

Preencher com a Quantidade de Quotas no Final do Período de cada registro recuperado.

	Sim		RNGY630-05	PATR_FIN_PER– Patrimônio no Final do Período

Preencher com o Patrimônio no Final do Período de cada registro recuperado.

	Sim		RNGY630-06	DAT_ABERT– Data de Abertura

Preencher com a Data de Abertura de cada registro recuperado.

	Sim		RNGY630-07	DAT_ENCER – Data de Encerramento

Preencher com a Data de Encerramento de cada registro recuperado.

	Não		
Registro Y640: Participações em Consórcios de Empresa 
Campo Chave: CNPJ
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY640	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y640, considerando os parâmetros da RNG-Y e se 

No registro 0020 o campo5- IND_PART_CONS = ‘S’ 		RNGY640-01	REG – Tipo de Registro

Gerar fixo ‘Y640’	Sim		RNGY640-02	CNPJ– CNPJ

Preencher com o CNPJ de cada registro recuperado.
	Sim		RNGY640-03	COND_DECL– Condição do Declarante

Preencher com a Condição do declarante de cada registro recuperado.

	Sim		RNGY640-04	VL_CONS– Receita do Consórcio

Preencher com a Receita do Consórcio de cada registro recuperado.

	Não		RNGY640-05	CNPJ_LID– CNPJ da Empresa Líder

Preencher com o CNPJ da Empresa Líder de cada registro recuperado.

	Sim		RNGY640-06	VL_DECL– Receita do Declarante no Consórcio

Preencher com a Receita do declarante no consórcio de cada registro recuperado.

	Sim		

Registro Y650: Participantes do Consórcio 
Campo Chave: CNPJ
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY650	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y650, considerando os parâmetros da RNG-Y e se 

No Registro Y640, campo 3- COND_DECL = ‘1’ 


Outras Validações:

Verifica se a soma do campo 03 – VL_PART dos registros Y650, somado ao campo 6-VL_DECL do Y640 é igual ao campo 04 – VL_CONS do Y640, caso contrário exibir a msg TR00627		RNGY650-01	REG – Tipo de Registro

Gerar fixo ‘Y650’	Sim		RNGY650-02	CNPJ– CNPJ

Preencher com o CNPJ de cada registro recuperado.
	Sim		RNGY650-03	VL_PART – Receita do Participante

Preencher com a Receita do Participante de cada registro recuperado.
	Não		Registro Y660: Dados de Sucessoras 
Campo Chave: CNPJ
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY660	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y660, considerando os parâmetros da RNG-Y e se 

No Registro 0000, campo 7- SIT_ESPECIAL = ‘2’,’3’,’5’ ou ‘6’ 		RNGY660-01	REG – Tipo de Registro

Gerar fixo ‘Y660’	Sim		RNGY660-02	CNPJ– CNPJ

Preencher com o CNPJ de cada registro recuperado.	Sim		RNGY660-03	NOM_EMP – Nome Empresarial

Preencher com o Nome Empresarial de cada registro recuperado.	Sim		RNGY660-04	PERC_PAT_LIQ – Percentual do Patrimônio Líquido

Preencher com o Percentual do Patrimônio Líquido de cada registro recuperado.

Verifica, quando 0000.SIT_ESPECIAL igual a “2” (Fusão), “3” (Incorporação/Incorporada) ou “5” (Cisão Total) se o somatório de Y660.PERC_PAT_LIQ é igual a 100%, caso contrário apresentar a seguinte mensagem:
TR00752

Verifica, quando 0000.SIT_ESPECIAL igual a “6” (Cisão Parcial) se o somatório de Y660.PERC_PAT_LIQ é diferente do resultado da diferença de 100% e 0000.PAT_REMAN_CIS, caso contrário apresentar a seguinte mensagem:
TR00751	Não		

Registro Y665: Demonstrativo das Diferenças na Adoção Inicial 
Campo Chave: COD_CTA+COD_CCUS
Ocorrência: 0:N

A partir da versão 3.0, se o sistema  identificar esse registro na geração da ECF, o mesmo deve ser desconsiderado e ao final da geração a mensagem TR01298 deve ser exibida. 


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY665	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y665, considerando os parâmetros da RNG-Y e se 

No Registro 0010, o  campo 15 –DIF_FCONT = ‘S’ ou o  campo 5 – Forma_TRIB  = ‘8’ ou ‘9’

As mensagens definidas neste registro não devem ser exibidas quando a Forma_TRIB  = ‘8’ ou ‘9’ e TIP_ESC_PRE  (registro 0010) for diferente de “C”.		RNGY665-01	REG – Tipo de Registro

Gerar fixo ‘Y665’	Sim		RNGY665-02	COD_CTA– Código da Conta 

Preencher com o Código da Conta de cada registro recuperado.

Checagem somente de Conta Contábil

Verifica se o código da conta contábil recuperado está no registro J050, senão, deverá ser exibida a mensagem: TR00635. 

Checagem de Conta Contábil + Centro de Custo

Verifica se a conta contábil recuperada possui o centro de custo gerado no campo RNGY665-03 está no registro J051, senão, deverá ser exibida a mensagem: TR00635.	Sim		RNGY665-03	COD_CCUS– Código do Centro de Custos 

Preencher com o Código de Centro de Custos de cada registro recuperado.

	Não		RNGY665-04	VL_SALDO_SOC– Saldo Societário 

Preencher com o Saldo Societário de cada registro recuperado.
	Sim		RNGY665-05	IND_VL_SALDO_SOC– Indicador do Valor do Saldo Societário 

Preencher com o Indicador do Valor do Saldo Societário de cada registro recuperado.

	Sim		RNGY665-06	VL_SALDO_FIS– Saldo Fiscal 

Preencher com o Saldo Fiscal de cada registro recuperado.
	Sim		RNGY665-07	IND_VL_SALDO_FIS– Indicador do Valor do Saldo Fiscal

Preencher com o Indicador do Valor do Saldo Fiscal de cada registro recuperado.

	Sim		RNGY665-08	DIF_SALDOS– Diferença de Saldos 

Preencher com a Diferença de Saldos de cada registro recuperado.
	Sim		RNGY665-09	IND_DIF_SALDOS– Indicador da Diferença de Saldos 

Preencher com o Indicador da Diferença de Saldos de cada registro recuperado.

	Sim		RNGY665-10	MET_CONTR– Método de Controle 
Preencher com o Método de Controle de cada registro recuperado.

	Sim		RNGY665-11	
COD_SUBCONT– Código da Subconta

Preencher com o Código da Subconta de cada registro recuperado.

Checagem somente o Código da Subconta

Verifica se o código da subconta recuperado está no registro J050, senão, deverá ser exibida a mensagem: TR00637. 

Checagem de Código da Subconta + Centro de Custo

Verifica se a conta contábil recuperada possui o centro de custo gerado no campo RNGY665-12 está no registro J051, senão, deverá ser exibida a mensagem: TR00637.

	Não		RNGY665-12	
COD_CCUS_SUB– Código do Centro de Custos da Subconta

Preencher com o Código do Centro de Custos da Subconta de cada registro recuperado.

Verificação:

Se o código do centro de custo informado não estiver preenchido no registro J051, exibir a mensagem: TR00637. 

 	


Não		RNGY665-13	Campo válido a partir da versão 2.0, conforme alteração layout [11/03/2016]

COD_SUBCONT_AUX - Código da Subconta Auxiliar Contábil Analítica
	
Não		RNGY665-14	Campo válido a partir da versão 2.0, conforme alteração layout [11/03/2016]

COD_CCUS_SUB_AUX - 	Código do Centro de Custos da Subconta Auxiliar Contábil Analítica

Preencher com o Código do Centro de Custos da Subconta Auxiliar Contábil Analítica
de cada registro recuperado.

	


Não		Registro Y671: Outras Informações 
Campo Chave: REG
Ocorrência: 0:1


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY671	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y671, considerando os parâmetros da RNG-Y e se 

No Registro 0010, campo 5 – Forma_TRIB  = ‘1’,’2’,’3’ ou ‘4’’
		RNGY671-01	REG – Tipo de Registro

Gerar fixo ‘Y671’	Sim		RNGY671-02	VL_AQ_MAQ– Aquisição de Máquinas, Aparelhos, Instrumentos e Equipamentos Novos

Preencher com o valor de aquisição de máquinas, aparelhos, instrumentos e equipamentos novos de cada registro recuperado.

	Não		RNGY671-03	VL_DOA_CRIANCA– Doação aos Fundos dos Direitos da Criança e do Adolescente

Preencher com o valor de Doação aos Fundos dos Direitos da Criança e do Adolescente de cada registro recuperado.

Verifica se o campo VL_DOA_CRIANCA (Campo 03) está preenchido quando N630 linha (11) (Fundos dos Direitos da Criança e do Adolescente) for maior que zero, no caso de PJ em Geral (campo 7 do registro 0010 = ‘01’), ou N630 linha (10) (Fundos dos Direitos da Criança e do Adolescente) for maior que zero, no caso de Financeiras, Segurados, de Capitalização e Entidades Abertas de Previdências Complementar (campo 7 do registro 0010 = “02” ou ‘03’), senão exibir a msg TR01213

Se este campo está preenchido e a linha (11) (Fundos dos Direitos da Criança e do Adolescente) do registro N630 estiver sem preenchimento (zero), no caso de PJ em Geral (campo 7 do registro 0010 = ‘01’), ou N630 linha (10) (Fundos dos Direitos da Criança e do Adolescente) estiver sem preenchimento (zero), no caso de Financeiras, Segurados, de Capitalização e Entidades Abertas de Previdências Complementar (campo 7 do registro 0010 = “02” ou ‘03’), exibir a msg TR01410.


	Não		RNGY671-04	VL_DOA_IDOSO– Doação aos Fundos Nacional, Estaduais ou Municipais do Idoso 

Preencher com o valor de Doação aos Fundos Nacional, Estaduais ou Municipais do Idoso de cada registro recuperado.

Verifica se o campo VL_DOA_IDOSO (Campo 04) está preenchido quando N630 linha (12) (Fundos Nacional, Estaduais ou Municipais do Idoso) for maior que zero, no caso de PJ em Geral (campo 7 do registro 0010 = ‘01’), ou N630 linha (11) (Fundos Nacional, Estaduais ou Municipais do Idoso) for maior que zero, no caso de Financeiras, Segurados, de Capitalização e Entidades Abertas de Previdências Complementar (campo 7 do registro 0010 =“02” ou  ‘03’) , senão exibir a msg TR01213.


Se este campo está preenchido e a linha (12) (Fundos Nacional, Estaduais ou Municipais do Idoso) do registro N630 estiver sem preenchimento (zero), no caso de PJ em Geral (campo 7 do registro 0010 = ‘01’), ou N630 linha (11) (Fundos Nacional, Estaduais ou Municipais do Idoso) estiver sem preenchimento (zero), no caso de Financeiras, Segurados, de Capitalização e Entidades Abertas de Previdências Complementar (campo 7 do registro 0010 =“02” ou  ‘03’) , exibir a msg TR01410.

	Não		RNGY671-05	VL_AQ_IMOBILIZADO– Aquisições para o Ativo Imobilizado 

Preencher com o valor das aquisições para o ativo imobilizado de cada registro recuperado.
	Não		RNGY671-06	VL_BX_IMOBILIZADO– Baixas do Ativo Imobilizado 

Preencher com o valor das baixas do ativo imobilizado de cada registro recuperado.


	Não		RNGY671-07	VL_INC_INI– Bens Sujeitos ao Incentivo de que Trata a Lei no 11.051/2004 no Início do Período

Preencher com o valor dos Bens Sujeitos ao Incentivo de que Trata a Lei no 11.051/2004 no Início do Período de cada registro recuperado.
	Não		RNGY671-08	VL_INC_FIN – Bens Sujeitos ao Incentivo de que Trata a Lei no 11.051/2004 no Fim do Período

Preencher com o o valor dos Bens Sujeitos ao Incentivo de que Trata a Lei no 11.051/2004 no Fim do Período de cada registro recuperado.

	Não		RNGY671-09	VL_CSLL_DEPREC_INI – Saldo de Créditos de CSLL sobre Depreciação no Início do Período

Preencher com o   valor do Saldo de Créditos de CSLL sobre Depreciação no Início do Período de cada registro recuperado.
	Não		RNGY671-10	VL_OC_SEM_IOF – Valor das Operações de Câmbio com Isenção de IOF

Preencher com o Valor das Operações de Câmbio com Isenção de IOF de cada registro recuperado.
	Não		RNGY671-11	VL_FOLHA_ALIQ_RED – Valor Total da Folha Sujeita à Alíquota Reduzida de que Trata a Lei nº 11.774/2008

Preencher com o Valor Total da Folha Sujeita à Alíquota Reduzida de que Trata a Lei nº 11.774/2008 de cada registro recuperado.


	Não		RNGY671-12	VL_ALIQ_RED – Alíquota Reduzida de que Trata a Lei no 11.774/2008

Preencher com a Alíquota Reduzida de que Trata a Lei no 11.774/2008de cada registro recuperado.
	Não		RNGY671-13	IND_ALTER_CAPITAL – Alteração de Capital na Forma dos art. 22 e 23 da Lei no 9.249/1995

Preencher com a Alteração de Capital na Forma dos art. 22 e 23 da Lei no 9.249/1995 de cada registro recuperado.

	Não		RNGY671-14	IND_BCN_CSLL – Opção pela Escrituração, no Ativo, da Base de Cálculo Negativa da CSLL

Preencher com a Opção pela Escrituração, no Ativo, da Base de Cálculo Negativa da CSLL de cada registro recuperado.
	Não		Registro Y672: Outras Informações (Lucro Presumido ou Lucro Arbitrado)
Campo Chave: REG
Ocorrência: 0:1


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY672	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y672, considerando os parâmetros da RNG-Y e se 

No Registro 0010, campo 5 – Forma_TRIB  = ‘5’,’6’ ou ‘7’


Verificações:


Se campo 10-TIP_ESC_PRE = “L”(do registro0010) ou campo 5- FORMA.TRIB = “6” ou “7”(do registro 0010), pelo menos um dos campos abaixo deve estar preenchido: 3- VL_CAPITAL, 5- VL_ESTOQUES, 7- VL_CAIXA, 9-VL_APLIC_FIN, 11 -VL_CTA_REC, 13 - VL_CTA_PAG, 14-VL_COMPRA_MERC, 15-VL_COMPRA_ATIVO, 16-VL_RECEITAS, 17-TOT_ATIVO, 18-VL_FOLHA e 19-VL_ALIQ_RED, caso contrário exibir a seguinte msg de erro TR00639.
		RNGY672-01	REG – Tipo de Registro

Gerar fixo ‘Y672’	Sim		RNGY672-02	VL_CAPITAL_ANT– Capital Registrado do Ano Anterior 

Preencher com o valor de capital registrado do ano anterior de cada registro recuperado.

Verifica se VL_CAPITAL_ANT não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), Caso contrário emitir a seguinte mensagem:
TR00747
	Não		RNGY672-03	VL_CAPITAL– Capital Registrado 

Preencher com o valor de capital registrado de cada registro recuperado.

Verifica se o campo Y672.VL_CAPITAL não está preenchido quando o campo 0010.TIPO_ESC_PRE do registro 0010 for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido) , caso contrário emitir a seguinte mensagem:
TR00747.

Verifica se o campo Y672.VL_CAPITAL está preenchido quando 0010.FORMA_TRIB for igual a “5” (Lucro Presumido) e 0010.TIPO_ESC_PRE for igual a “L” (Livro Caixa) ou quando 0010.FORMA_TRIB for igual a “6” (Lucro Arbitrado) ou “7” (Presumido/Arbitrado), caso contrário emitir a seguinte mensagem:
TR00748	Não		RNGY672-04	VL_ESTOQUE_ANT– Estoques do Ano Anterior 

Preencher com o valor de estoques do ano anterior de cada registro recuperado.


Verifica se o campo Y672.VL_ESTOQUE_ANT não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-05	VL_ESTOQUE – Estoques 

Preencher com o valor de estoques de cada registro recuperado.

Verifica se Y672.VL_ESTOQUES não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-06	VL_CAIXA_ANT– Saldo de Caixa e Bancos do Ano Anterior 

Preencher com o valor do saldo de caixa e bancos do ano anterior de cada registro recuperado.

Verifica se Y672.VL_CAIXA_ANT não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-07	VL_CAIXA– Saldo de Caixa e Bancos 

Preencher com o valor do saldo de caixa e bancos de cada registro recuperado.

Verifica se Y672.VL_CAIXA não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-08	VL_APLIC_FIN_ANT – Saldo de Aplicações Financeiras do Ano Anterior 

Preencher com o valor do saldo de aplicações financeiras do ano anterior de cada registro recuperado.

Verifica se Y672.VL_APLIC_FIN_ANT não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-09	VL_APLIC_FIN – Saldo de Aplicações Financeiras 
Preencher com o valor do saldo de aplicações financeiras de cada registro recuperado.

Verifica se Y672.VL_APLIC_FIN não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-10	VL_CTA_REC_ANT – Contas a Receber do Ano Anterior 

Preencher com o valor de contas a receber do ano anterior de cada registro recuperado.

Verifica se Y672. VL_CTA_REC_ANT não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-11	VL_CTA_REC – Contas a Receber 

Preencher com o valor de contas a receber de cada registro recuperado.

Verifica se Y672.VL_CTA_REC não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-12	VL_CTA_PAG_ANT – Contas a Pagar do Ano Anterior 

Preencher com o valor de contas a pagar do ano anterior de cada registro recuperado.

Verifica se Y672.VL_CTA_PAG_ANT não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-13	VL_CTA_PAG – Contas a Pagar 

Preencher com o valor de contas a pagar de cada registro recuperado.

Verifica se Y672.VL_CTA_PAG não está preenchido quando 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e 0010.FORMA_TRIB = “5” (Lucro Presumido), caso contrário emitir a seguinte mensagem:
TR00747	Não		RNGY672-14	VL_COMPRA_MERC – Compras de Mercadorias no Ano-calendário 

Preencher com o valor de compras de mercadorias no ano-calendário de cada registro recuperado.

	Não		RNGY672-15	VL_COMPRA_ATIVO – Compras de Elementos do Ativo no Ano-Calendário, Exceto os Classificáveis no Ativo Circulante e Ativo Não Circulante Realizável a Longo Prazo 

Preencher com o valor de Compras de Elementos do Ativo no Ano-Calendário, Exceto os Classificáveis no Ativo Circulante e Ativo Não Circulante Realizável a Longo Prazo de cada registro recuperado.
	Não		RNGY672-16	VL_RECEITAS– Receitas e Rendimentos Não Tributáveis ou Tributados Exclusivamente na Fonte

Preencher com as Receitas e Rendimentos Não Tributáveis ou Tributados Exclusivamente na Fonte de cada registro recuperado.
	Não		RNGY672-17	TOT_ATIVO – Total do Ativo

Preencher com o Total do Ativo de cada registro recuperado.
	Não		RNGY672-18	VL_FOLHA – Valor Total da Folha Sujeita à Alíquota Reduzida de que Trata a Lei no 11.774/2008

Preencher com o Valor Total da Folha Sujeita à Alíquota Reduzida de que Trata a Lei no 11.774/2008 de cada registro recuperado.
	Não		RNGY672-19	VL_ALIQ_RED – Alíquota Reduzida de que Trata a Lei no 11.774/2008

Preencher com a Alíquota Reduzida de que Trata a Lei no 11.774/2008 de cada registro recuperado.
	Não		RNGY672-20	IND_REG_APUR – Regime de Apuração das Receitas 

Gerar este campo até a versão 2.00
Preencher com o Regime de Apuração das Receitas de cada registro recuperado.

Não gerar este campo a partir da versão 3.00
	Não		RNGY672-21	IND_AVAL_ESTOQ – Método de Avaliação de Estoques 

Preencher com o Método de Avaliação de Estoques de cada registro recuperado.
Onde: 
Se preenchido ‘Custo Médio Ponderado’, gerar ‘1’
Se preenchido ‘PEPS (Primeiro que entra, primeiro que sai)’, gerar ‘2’
Se preenchido ‘Arbitramento – art. 296, Inc. I e II, do RIR/99’, gerar ‘3’


Verifica se Y672.IND_AVAL_ESTOQ não está preenchido, quando Y672.VL_ESTOQUES for maior que zero, 0010.FORMA_TRIB for igual a “5” (Lucro Presumido) ou “7” (Lucro Presumido/Arbitrado) e 0010TIPO_ESC_PRE for igual a “L” (Livro Caixa), caso contrário emitir a seguinte mensagem:
TR00749

Verifica se Y672.IND_AVAL_ESTOQ não está preenchido, quando 0010.FORMA_TRIB for igual a “5” (Lucro Presumido) ou “7” (Lucro Presumido/Arbitrado), 0010.TIPO_ESC_PRE for igual a “C” (Contábil) e P100(“1.01.03.01.21”) diferente de zero para qualquer período informado no registro P030, caso contrário emitir a seguinte mensagem:
TR00750
OBS:
Devido a incompatibilidade no leiaute da ECF para a validação do campo IND_AVAL_ESTOQ do registro Y672 a mensagem TR00750 não poderá ser exibida até que a conta contábil 1.01.03.01.21 referenciada como pertencente ao P100 seja atualizada.	Não		
Registro Y680: Mês das Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)
Campo Chave: Mês
Ocorrência: 0:12


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY680	Para a geração deste registro, recuperar as informações  da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y680, considerando os parâmetros da RNG-Y e se  


No Registro 0010, o  campo 3 - OPT_REFIS = ‘S’ e o campo 5 – Forma_TRIB  `"  8  e  9 		RNGY680-01	REG   Tipo de Registro

Gerar fixo  Y680 	Sim		RNGY680-02	MES   Mês

Preencher com o Mês de cada registro recuperado.

Verifica se o campo Mês está compreendido no período informado no registro 0000 (campos 10-  DT_INI e 11-DT_FIN), caso contrário exibe a msg de erro TR00624, 	Sim		
Registro Y681: Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)
Campo Chave: Mês
Ocorrência: 0:12


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY681	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y681, considerando os parâmetros da RNG-Y e se  


No Registro 0010, o  campo 3 - OPT_REFIS = ‘S’ e o campo 5 – Forma_TRIB  `"  8  e  9 

		RNGY681-01	REG   Tipo de Registro

Gerar fixo  Y681 	Sim		RNGY681-02	CODIGO   Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim		RNGY681-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não		RNGY681-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não		
Registro Y682: Informações de Optantes pelo Refis - Imunes ou Isentas
Campo Chave: REG
Ocorrência: 0:12


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY682	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y682 , considerando os parâmetros da RNG-Y e se  


No Registro 0010, o  campo 3 - OPT_REFIS = ‘S’ e o campo 5 – Forma_TRIB  = ‘8’ e ‘9’ (**)

(**) Definição feita por Requisitos, pois este item não está consistente no manual de orientação (31/12/2014). A Receita já confirmou a alteração deste item no manual.

		RNGY682-01	REG – Tipo de Registro

Gerar fixo ‘Y682’	Sim		RNGY682-02	MES – Mês

Preencher com o Mês de cada registro recuperado.

Verifica se o campo Mês está compreendido no período informado no registro 0000 (campos 10-  DT_INI e 11-DT_FIN), caso contrário exibe a msg de erro TR00624,	Sim		RNGY682-03	ACRES_PATR – Acrescimo Patrimonial no Mês

Preencher com o Acréscimo Patrimonial no Mês de cada registro recuperado.	Sim		
Registro Y690: Informações de Optantes pelo Paes
Campo Chave: Mes
Ocorrência: 0:12


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY690	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y690, considerando os parâmetros da RNG-Y e se  

No Registro 0010, o  campo 4 - OPT_PAES = ‘S’ 		RNGY690-01	REG – Tipo de Registro

Gerar fixo ‘Y680’	Sim		RNGY690-02	MES – Mês

Preencher com o Mês de cada registro recuperado.

Verifica se o campo Mês está compreendido no período informado no registro 0000 (campos 10-  DT_INI e 11-DT_FIN), caso contrário exibe a msg de erro TR00624, 	Sim		RNGY690-03	VL_REC_BRU – VAlor Receita Bruta no Mês

Preencher com o Valor da Receita bruta no mês de cada registro recuperado.

 	Sim		
Registro Y800: Outras Informações 
Campo Chave: REG
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGY800	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) -registro Y800, considerando os parâmetros da RNG-Y 		RNGY800-01	REG – Tipo de Registro

Gerar fixo ‘Y800’	Sim		RNGY800-02	TIPO_DOC – Tipo do Documento

Preencher com a informação do campo Tipo do Documento.

Este campo só deve ser gerado para escriturações com versão a partir da 3.00
	Sim		RNGY800-03	DESCRIÇÂO - Descrição

Preencher com a descrição do Tipo do Documento.

Este campo só deve ser gerado para escriturações com versão a partir da 3.00
	SIM		RNGY800-04	HASH - Descrição

Gerar ||. Este campo será gerado pelo sistema da receita.

Este campo só deve ser gerado para escriturações com versão a partir da 3.00
	SIM		RNGY800-05	ARQ_RTF – Sequência de Bytes

Preencher com a Sequencia de Bytes de cada registro recuperado.

	Sim		 RNGY800-06	IND_FIM_RTF – Indicador de Fim de Arquivo

Preencher fixo ‘Y800FIM’

 	Sim		

 Registro Y720: Informações de Períodos Anteriores:
Campo Chave: REG
Ocorrência: 0:1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGY720	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y720, considerando os parâmetros da RNG-Y e se:
a entrega da escrituração estiver sendo realizada com atraso.
 
		RNGY720-01	REG – Tipo de Registro

Gerar fixo ‘Y720’	SIM		RNY720-02	LUC_LIQ – Lucro Líquido do Período de Apuração Antes da Incidência do IRPJ e da CSLL 1.515/2014, art. 183, 3º)
Gravar com a informação de lucro líquido antes da incidência do imposto sobre a renda e da contribuição social sobre o lucro líquido do último período informado, atualizado pela taxa referencial do Selic preenchido pelo usuário.
	SIM		RNY720-03	DT_LUC_LIQ – Data Final do Período de Apuração do Lucro Líquido Informado Acima
Gravar com a data do lucro líquido informando no campo do Lucro líquido do último período preenchido pelo usuário.

Para este campo, realizar a validação abaixo:

Se na base dados houver registros cuja Data Final do Período de Apuração do Lucro Líquido Informado Acima seja igual ou superior à data inicial da escrituração conforme o campo 10 -  DT_INI do registro 0000, deverá ser exibida a TR01186.
	SIM		RNY720-04	REC_BRUT_ANT - Receita Bruta do Período Anterior 

Gravar com o valor da Receita Bruta anterior preenchido pelo usuário.

Até a versão 1.0 

Campo não consta no manual leiaute, porém consta no PVA como campo de preenchimento obrigatório.

A partir da versão 2.0, conforme alteração layout [11/03/2016]:
O campo foi oficialmente incluído com alteração do nome.

	SIM		
Registro Y700: Declaração de Informações de Operações Relevantes (DIOR)

O registro Y7 deve ser considerado até a versão 1.0.
A partir da versão 2.0, se o sistema  identificar esse registro na geração da ECF, o mesmo deve ser desconsiderado e ao final da geração a mensagem TR01026 deve ser exibida. (WI-890459)

Campo Chave: Todos os campos são chaves (Adaptação necessária devido a estrutura interna do sistema, pois este registro não possui campo chave de acordo com o manual leiaute 31/08/2015)
Ocorrência: 0:N
Este registro deve ser preenchido pela pessoa jurídica com as informações de operações relevantes, conforme previsão do art. 7º da Medida Provisória nº 685, de 21 de julho de 2015.

CÓD	DESCRIÇÃO	OBRIG	MFS		RNGY700	Para a geração deste registro, recuperar as informações da tela Informações Econômicas e Gerais (Blocos X e Y) - registro Y700, considerando os parâmetros da RNG-Y
Para cada registro Y700, deve existir pelo menos um registro Y710, caso contrário, exibir a msg de aviso TR00621
		RNGY700-01	REG – Tipo de RegistroGerar fixo ‘Y700’	SIM		RNGY700-02	NUM_EDOSSIE – Número do e-DossiêGravar a informação do número do e-Dossiê relativo à DIOR preenchido pelo usuário.	NÃO		RNGY700-03	DT_INI_ATO – Data de Início do Ato ou Negócio Jurídico

Gravar a informação da Data de Início do conjunto de operações que envolvam atos ou negócios jurídicos relativos à DIOR preenchida pelo usuário.

Se Y700. DT_INI_ATO (campo 03)  for maior que 0000.DT_FIN (data final da ecf) apresentar a mensagem de erro TR00895.
	SIM		RNGY700-04	DT_FIN_ATO – Data Final do Ato ou Negócio Jurídico
Gravar a informação da Data Final do conjunto de operações que envolvam atos ou negócios jurídicos relativos à DIOR preenchida pelo usuário.

Se Y700.DT_FIN_ATO (campo 04)  for maior que 0000.DT_FIN  (data final da ecf) apresentar a mensagem de erro TR00895.	SIM		RNGY700-05	ANO_INI – Ano-Calendário Inicial da Economia Tributária

Gravar o Ano-Calendário inicial da economia tributária relativa à DIOR preenchido pelo usuário.	SIM		RNGY700-06	ANO_FIN – Ano-Calendário Final da Economia Tributária

Gravar o Ano-Calendário final da economia tributária relativa à DIOR preenchido pelo usuário.

Se Y700.ANO_FIN (campo 06) for  superior a 10 anos antes do ano da escrituração informado no registro 0000, apresentar a mensagem de erro TR00897.	SIM		RNGY700-07	OP_PDEP_BRASIL – Operações Entre Partes Dependentes no Brasil

Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente às operações entre as partes.	SIM		RNGY700-08	OP_PDEP_EXT_TNF – Operações Entre Partes Dependentes no Exterior Sem Tributação Favorecida

Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente às operações entre as partes dependentes no Exterior.	SIM		RNGY700-09	OP_PDEP_EXT_TF – Operações Entre Partes Dependentes no Exterior Com Tributação Favorecida

Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente às operações entre as partes dependentes no Exterior.	SIM		RNGY700-10	OP_PINDEP_BRASIL – Operações Entre Partes Independentes no Brasil

Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente às operações entre as partes independentes no Brasil.	SIM		RNGY700-11	OP_PINDEP_EXT_TNF - Operações Entre Partes Independentes no Exterior Sem Tributação Favorecida

Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente às operações entre as partes independentes no Exterior.	SIM		RNGY700-12	OP_PINDEP_EXT_TF - Operações Entre Partes Independentes no Exterior Com Tributação Favorecida

Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente às operações entre as partes independentes no Exterior.	SIM		RNGY700-13	GER_ATIV_FISCAL – Geração de Ativo Fiscal Diferido
Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente a geração de ativo fiscal diferido.	SIM		RNGY700-14	REORG_SOC – Reorganização Societária (Fusão, Cisão, Incoporação)
Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente reorganização societária.	SIM		RNGY700-15	GER_PAS_TERC – Geração de Passivo com Terceiros
Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente a geração de passivo com terceiros.	NÃO		RNGY700-16	BENEF_GER_PAS – Beneficiários da Geração de Passivo com Terceiros

Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente à identificação de beneficiários da geração de passivo com terceiros.	SIM		RNGY700-17	REDUC_BASE_TRIB – Redução da Base Tributária no Brasil Com Transferência Para o Exterior
Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente à informação de redução de base tributária no Brasil com transferência para o exterior.	SIM		RNGY700-18	REDUC_ATIVO – Redução de Ativos

Gravar com o valor escolhido pelo usuário da lista de valores válidos, referente à redução de ativos.
	SIM		RNGY700-19	PERC_REDUC_ATIVO – Percentual de Redução de Ativos

Gravar com o valor escolhido pelo usuário da