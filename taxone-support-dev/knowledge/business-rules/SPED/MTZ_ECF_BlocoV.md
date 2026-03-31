# MTZ_ECF_BlocoV

> Fonte: MTZ_ECF_BlocoV.doc

THOMSON REUTERS

Geração Bloco V


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		14/08/2018	MFS-20277	Criação do documento	Alessandra Cristina Navatta		19/09/2018	MFS-20964	Exclusão da mensagem DW00273 e inserido um filtro dos meses (registro V030)	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc522018697" INTRODUÇÃO	 PAGEREF _Toc522018697 \h 3
 HYPERLINK \l "_Toc522018698" 1.	Regras de Negócio	 PAGEREF _Toc522018698 \h 3
 HYPERLINK \l "_Toc522018699" 1.1	Informações gerais de seleção e processamento	 PAGEREF _Toc522018699 \h 3
 HYPERLINK \l "_Toc522018700" 1.2	Registros Identificadores	 PAGEREF _Toc522018700 \h 3
 HYPERLINK \l "_Toc522018701" 1.2.1	Registro V001: Abertura do Bloco V	 PAGEREF _Toc522018701 \h 4
 HYPERLINK \l "_Toc522018702" 1.2.2	Registro V010: REGISTRO V010: DEREX – Instituição	 PAGEREF _Toc522018702 \h 4
 HYPERLINK \l "_Toc522018703" 1.2.3	Registro V020: DEREX - Responsável pela movimentação	 PAGEREF _Toc522018703 \h 5
 HYPERLINK \l "_Toc522018704" 1.2.4	Registro V030: DEREX - Período - Mês	 PAGEREF _Toc522018704 \h 6
 HYPERLINK \l "_Toc522018705" 1.2.5	Registro V100: Demonstrativo dos recursos em moeda estrangeira decorrentes do recebimento de exportações	 PAGEREF _Toc522018705 \h 7
 HYPERLINK \l "_Toc522018706" 1.2.6	Registro V990: Encerramento do Bloco V	 PAGEREF _Toc522018706 \h 7
 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO
Este bloco tem o objetivo de apresentar as informações das declarações DEREX.

Regras de Negócio
Informações gerais de seleção e processamento do registro
CÓD	DESCRIÇÃO	MFS		RNG-V	
Período de recuperação dos registros: Data Inicial das Informações da ECF e a Data Final da última Apuração durante o Processamento em Lote.

Para geração destes registros, recuperar as informações da tela Bloco V - Declaração DEREX.

Aplicar a RNG00051 - Geração dos Registros

Se o Registro estiver como OC no campo ‘Obrigatoriedade Saída’ (item 1.2 deste documento), for de nível igual a “2” ou superior e as regras do registro forem cumpridas, mas não existir dados na tela (mencionada na regra geral do registro), exibir a mensagem DW00247.

Os campos-chaves encontram-se descritos acima de cada grupo de registros.

Na tela de Perfil de geração o registro deve estar selecionado para a geração.


		MFS-20277		
Registros Identificadores
Relação de Registros a serem gerados

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		V001	1	Abertura do Bloco V - DEREX 	F	O	[1:1]		HYPERLINK \l "RY520"V010	2	DEREX - Instituição	F	OC
Obrigatório se 020.IND_DEREX = S. Senão não deve existir.
	 [1,1]
		HYPERLINK \l "RY540"V020	3	DEREX - Responsável pela Movimentação	F	O	[1,N]
		HYPERLINK \l "RY550"

V030	3	DEREX - Período - Mês	F	O	[1,12]
		V100	4	Demonstrativo dos recursos em moeda estrangeira decorrentes do recebimento de exportações	F	O	[1,1]
		 V990	1	Encerramento do Bloco V	F	O	[1,1]
		
Registro V001: Abertura do Bloco V
Campo Chave: REG
Ocorrência: 1:1
CÓD	DESCRIÇÃO	
OBRIG	MFS		RNV001-01	REG – Tipo de Registro
Gerar fixo ‘V001’	
SIM	MFS-20277		RNV001-02	IND_DAD - Indicador de Movimento

Caso existam informações nos registros do bloco V (registros V010, V020, V030, V100), preencher com “0”, caso contrário, preencher com “1”.
	

SIM	MFS-20277		Registro V010: REGISTRO V010: DEREX – Instituição
Campo Chave: REG (Manual com informação errada. Devido a ocorrência do registro, colocamos todos os campos na chave. Teste feito no PVA)
Ocorrência: 1:N
CÓD	DESCRIÇÃO	
OBRIG.	MFS		RNGV010	Para a geração deste registro, recuperar as informações da tela Bloco V - Declaração DEREX - registro V010, considerando os parâmetros da RNG-V e se: 

Se na tela Informações ECF, o campo ‘Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX’ estiver marcado.
		MFS-20277		RNGV010-01
	REG – Tipo de Registro

Gerar fixo ‘V010’	Sim	MFS-20277		RNGV010-02	NOME_INSTITUIÇÃO – Nome da Instituição 

Preencher com os dados recuperados informados na tela.	Sim	MFS-20277		RNGV010-03	PAIS - Código do País da Instituição

Recuperar e preencher com o valor informado na tela (campo CÓDIGO da tabela CBC_PAIS_ACORDO_Jurisdicao).	Sim	MFS-20277		RNGV010-04	TIP_MOEDA – Moeda

Recuperar e preencher com o valor informado na tela (campo TIP_MOEDA da tabela CBC_MOEDA).	Sim	MFS-20277		Registro V020: DEREX - Responsável pela movimentação
Campo Chave: REG (Manual com informação errada. Devido a ocorrência do registro, colocamos os campos TIPO_DO_C e NI na chave, com base nos testes realizado no PVA)
Ocorrência: 1:N
CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGV020	Para a geração deste registro, recuperar as informações da tela Bloco V - Declaração DEREX  - registro V020, considerando os parâmetros da RNG-V, a geração do registro V010.
		MFS-20277		RNGV020-01	REG – Tipo de Registro

Gerar fixo ‘V020’	Sim	MFS-20277		RNGV020-02	NOME - Nome do responsável

Recuperar e preencher com o valor informado na tela.	Sim	MFS-20277		RNGV020-03	ENDERECO - Endereço do responsável

Recuperar e preencher com o valor informado no campo.	Sim	MFS-20277		RNGV020-04	TIPO_DO_C - Tipo de documento do responsável

Recuperar e preencher com o valor informado no campo.	Sim	MFS-20277		RNGV020-05	NI - Número do documento do responsável

Recuperar e preencher com o valor informado no campo.	Sim	MFS-20277		RNGW200-06	IDENT_CONTA - Identificação das contas

Recuperar e preencher com o valor informado no campo.	Sim	MFS-20277		Registro V030: DEREX - Período - Mês
Campo Chave: REG
Ocorrência: 1:12

CÓD	DESCRIÇÃO	
OBRIG.	
MFS		RNGV030	Para a geração deste registro, recuperar as informações da tela Bloco V - Declaração DEREX - registro V030, considerando os parâmetros da RNG-V, a geração do registro V010.
Recuperar apenas os meses que estão compreendidos na data da Informação ECF recuperada e no período da geração do meio magnético.
	Sim	MFS-20277
MFS-20964		RNGV030-01	REG – Tipo de Registro

Gerar fixo ‘V030’	Sim	MFS-20277		RNGV030-02	MES – Mês

Preencher com o Mês de cada registro recuperado.

Verifica se o campo Mês está compreendido no período informado no registro 0000 (campos 10-  DT_INI e 11-DT_FIN), caso contrário exibir a mensagem DW00273. 	Sim	MFS-20277
MFS-20964		Registro V100: Demonstrativo dos recursos em moeda estrangeira decorrentes do recebimento de exportações
Campo Chave:
Ocorrência: 1:N
CÓD	DESCRIÇÃO	
OBRIG.	MFS		RNGV100-00	Para a geração deste registro, recuperar as informações da tela Bloco V - Declaração DEREX - registro V100, considerando os parâmetros da RNG-V, a geração do registro V030.
	-	MFS-20277		RNGV100-01	REG – Tipo de Registro

Gerar fixo ‘V100’
	Sim	MFS-20277		RNGV100-02	CODIGO – Código

Preencher com o Cód. do Registro de cada registro recuperado.	Sim	MFS-20277		RNGV100-03	DESCRICAO - Descrição

Preencher com o Desc. do Registro de cada registro recuperado.	Não	MFS-20277		RNGV100-04	VALOR - Valor

Preencher com o Valor de cada registro recuperado.	Não	MFS-20277		
Registro V990: Encerramento do Bloco V
Campo Chave: REG 
Ocorrência: 1:1
CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGV990-01	REG – Tipo de Registro

Gerar fixo ‘V990’	Sim	MFS-20277		RNGV990-02	QTD_LIN – Quantidade Total de Registro do Bloco w

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco V e informar o total.
Considerando que Campo 1: Texto fixo contendo "V990", e campo 2: Quantidade total de linhas do bloco V.
Exemplo: |V990|25|	Sim	MFS-20277		
 
Considerações deste modelo:

Quando uma Regra de Negócio for excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN