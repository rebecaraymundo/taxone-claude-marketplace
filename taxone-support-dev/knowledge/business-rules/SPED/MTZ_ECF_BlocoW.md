# MTZ_ECF_BlocoW

> Fonte: MTZ_ECF_BlocoW.doc

THOMSON REUTERS

Geração Bloco W

DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		15/06/2018	MFS-17095	Criação do documento	Alessandra Cristina Navatta		26/09/2018	MFS-20694	Inclusão de validações no registro W200 (DW00273 e DW00277).
Ajuste no quadro do tópico 1.2 Registros Identificadores
	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc520715252" INTRODUÇÃO	 PAGEREF _Toc520715252 \h 3
 HYPERLINK \l "_Toc520715253" 1.	Regras de Negócio	 PAGEREF _Toc520715253 \h 3
 HYPERLINK \l "_Toc520715254" 1.1	Informações gerais de seleção e processamento	 PAGEREF _Toc520715254 \h 3
 HYPERLINK \l "_Toc520715255" 1.2	Registros Identificadores	 PAGEREF _Toc520715255 \h 3
 HYPERLINK \l "_Toc520715256" 1.2.1	Registro W001: Abertura do Bloco W	 PAGEREF _Toc520715256 \h 4
 HYPERLINK \l "_Toc520715257" 1.2.2	Registro W100: Informações sobre o Grupo Multinacional e a Entidade Declarante – Declaração de País a País	 PAGEREF _Toc520715257 \h 5
 HYPERLINK \l "_Toc520715258" 1.2.3	Registro  W200: Declaração País-a-País	 PAGEREF _Toc520715258 \h 7
 HYPERLINK \l "_Toc520715259" 1.2.4	Registro W250: Declaração País-a-País – Entidades Integrantes	 PAGEREF _Toc520715259 \h 10
 HYPERLINK \l "_Toc520715260" 1.2.5	Registro W300: OBSERVAÇÕES ADICIONAIS -  DECLARAÇÃO PAÍS-A-PAÍS	 PAGEREF _Toc520715260 \h 13
 HYPERLINK \l "_Toc520715261" 1.2.6	Registro W990: Encerramento do Bloco W	 PAGEREF _Toc520715261 \h 15
 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO
Este bloco tem o objetivo de apresentar as informações das declarações de Pais a Pais

Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-W	
Para geração destes registros, recuperar as informações da tela Declaração País a País (Bloco W).
Se o Registro estiver como OC no campo ‘Obrigatoriedade Saída’ (item 1.2 deste documento), for de nível igual a “2” ou superior e as regras do registro forem cumpridas, mas não existir dados na tela (mencionada na regra geral do registro), exibir a mensagem DW00247.
Os campos-chaves encontram-se descritos acima de cada grupo de registros.
Aplicar a RNG00051 - Geração dos Registros
Na tela de Perfil de geração o registro deve estar selecionado para a geração.


		MFS-17095		
Registros Identificadores
Relação de Registros a serem gerados

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		W001	1	Abertura do Bloco W – Declaração Pais a Pais
	O	O	[1:;1]		HYPERLINK \l "RY520"W100	2	Informações sobre o Grupo Multinacional e a Entidade Declarante	F	OC
Obrigatório se 
0020.PAIS_A_PAIS = S
Senão não deve existir.
.	[0;1]		HYPERLINK \l "RY540"W200	3	Declaração País a País	F	OC
Obrigatório se [W100.IND_CONTROLADORA = S e W100.IND_ENTREGA = 2] ou W100.IND_ENTREGA = 3
Senão não deve existir
	[0;N]

A partir da Versão 4.00

Observação: Quando for obrigatório, deverá aparecer, no mínimo, duas vezes.		HYPERLINK \l "RY550"

W250	4	Declaração País a País – Entidades Integrantes	F	OC
Obrigatório se [W100.IND_CONTROLADORA = S e  W100.IND_ENTREGA =2] ou W100.IND_ENTREGA = 3
Senão, não deve existir
	[0;N]
		W300	2	Observações Adicionais	F	F	[0: N]		W990	1	Encerramento do Bloco W	F	O	[1:1]		
Registro W001: Abertura do Bloco W
Campo Chave: REG
Ocorrência: 1:1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNW001-01	REG – Tipo de Registro

Gerar fixo ‘W001’	SIM	MFS-17095		RNW001-02	IND_DAD - Indicador de  Movimento

Caso existam informações nos registros do bloco W (registros W100, W200, W250, W300) preencher com “0”, caso contrário, preencher com “1”.
	SIM	MFS-17095		Registro W100: Informações sobre o Grupo Multinacional e a Entidade Declarante – Declaração de País a País 
Campo Chave: REG
Ocorrência: 0:1


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGW100	Para a geração deste registro, recuperar as informações da tela Declaração Pais a Pais (Bloco W) registro do W100,  se na tela de perfil de geração o mesmo esteja selecionado para geração.

Regra de geração do registro (que está sendo feita na tela e importação do bloco w): 

Se no campo 0020.PAIS_A_PAIS (Entidade Integrante de Grupo Multinacional – Tela de Informações ECF for marcada com “S” e se na tela de perfil de geração o Bloco W encontra-se selecionado para geração para a escrituração.


		MFS-17095		RNGW100-01	REG – Tipo de Registro

Gerar fixo ‘W100’
	Sim	MFS-17095		RNGW100-02	NOME_MULTINACIONAL - Grupo Multinacional

Preencher com os dados recuperados informados na tela.	Sim	MFS-17095		RNGW100-03	IND_CONTROLADORA - Indicador de Entidade Controladora Final

Recuperar e preencher com o valor informado para o indicador.

Se o indicador de situação especial “0000.SIT_ESPECIAL” for diferente de zero e este campo estiver preenchido, apresentar a mensagem DW00265.
	Sim	MFS-17095		RNGW100-04	NOME_CONTROLADORA - Controladora Final

Recuperar e preencher com o valor informado no campo.	Sim	MFS-17095		RNGW100-05	JURISDICAO_CONTROLADORA - Jurisdição de Residência

Recuperar e preencher com o valor informado na tela (campo CÓDIGO da tabela CBC_PAIS_ACORDO_Jurisdicao).
	Sim	MFS-17095		RNGW100-06	TIN_CONTROLADORA - Tax Identification Number (TIN) da Controladora

Recuperar e preencher com o valor informado no campo.	Sim	MFS-17095		RNGW100-07	IND_ENTREGA - Entidade Responsável pela Entrega

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW100-08	IND_MODALIDADE - Modalidade da Declaração País-a-País

Recuperar e preencher com o valor informado no campo.	Sim	MFS-17095		RNGW100-09	NOME_SUBSTITUTA - Entidade Substituta/Entidade Local

Recuperar e preencher com o valor informado no campo.	Não	MFS-17095		RNGW100-10	JURISDICAO_SUBSTITUTA -  Jurisdição de Residência da Entidade Substituta

Recuperar e preencher com o valor informado na tela (campo CÓDIGO da tabela CBC_PAIS_ACORDO_Jurisdicao).
	Não	MFS-17095		RNGW100-11	TIN_SUBSTITUTA - Tax Identification Number (TIN) da Entidade Substituta 
Recuperar e preencher com o valor informado no campo.	Não	MFS-17095		RNGW100-12	DT_INI - Data Inicial
Recuperar e preencher com o valor informado no campo.	Não	MFS-17095		RNGW100-13	DT_FIN	- Data Final

Recuperar e preencher com o valor informado no campo.

Efetuar a seguinte validação:

Se a data final for maior que a data final do registro 0000 (campo 11 DT_FIN), exibir a mensagem DW00259.
	Não	MFS-17095		RNGW100-14	TIP_MOEDA – Moeda
Recuperar e preencher com o valor informado na tela (campo TIP_MOEDA da tabela CBC_MOEDA).	Não	MFS-17095		RNGW100-15	IND_IDIOMA – Idioma

Recuperar e preencher com o valor informado no campo.	Não	MFS-17095		
Registro 	W200: Declaração País-a-País
Campo Chave: JURISDICAO 
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGW200	Para a geração deste registro, recuperar as informações da tela Declaração Pais a Pais (Bloco W) do registro W200, se na tela de perfil de geração o mesmo esteja selecionado para geração.


Regras abaixo (que estão sendo feitas na tela e importação do bloco w): 

- Se o campo IND_CONTROLADORA - Indicador de Entidade Controladora Final do registro W100 for igual a S e se o campo IND_ENTREGA - Entidade Responsável pela Entrega for igual a 2,ou
- Se o campo IND_ENTREGA - Entidade Responsável pela Entrega for igual a 3, 

Caso contrário o registro não poderá ser gerado.


Se existir registros W200, deve ter um registro com o campo 02- Jurisdição de Residência Tributária igual a ‘BR’, caso não tenha, exibir a mensagem DW00277.

A partir da versão 4.00:
Se existir registros W200, deve no mínimo ter duas ocorrências, caso contrário exibir a mensagem DW00273.

	Não	MFS-17095
MFS-20694		RNGW200-01	REG – Tipo de Registro

Gerar fixo ‘W200’
		MFS-17095		RNGW200-02	JURISDICAO - Jurisdição de Residência Tributária

Recuperar e preencher com o valor informado na tela (campo CÓDIGO da tabela CBC_PAIS_ACORDO_Jurisdicao).
	Não	MFS-17095		RNGW200-03	VL_REC_NAO_REL_EST - Receitas Provenientes de Partes Não Relacionadas em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Não	MFS-17095		RNGW200-04	VL_REC_NAO_REL - Receitas Provenientes de Partes Não Relacionadas

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-05	VL_REC_REL_EST - Receitas Provenientes de Partes Relacionadas em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Não	MFS-17095		RNGW200-06	VL_REC_REL - Receitas Provenientes de Partes Relacionadas

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-07	VL_REC_TOTAL_EST - Receita Total em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Não	MFS-17095		RNGW200-08	VL_REC_TOTAL - Receita Total

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-09	VL_LUC_PREJ_ANTES_IR_EST - Lucro ou Prejuízo Antes do IR em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Não	MFS-17095		RNGW200-10	VL_LUC_PREJ_ANTES_IR - Lucro ou Prejuízo Antes do IR

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-11	VL_IR_PAGO_EST - Imposto de Renda Pago em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-12	VL_IR_PAGO - Imposto de Renda Pago

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-13	VL_IR_DEVIDO_EST - Imposto de Renda Devido em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Não	MFS-17095		RNGW200-14	VL_IR_DEVIDO - Imposto de Renda Devido

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-15	VL_CAP_SOC_EST - Capital Social em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Não	MFS-17095		RNGW200-16	VL_CAP_SOC - Capital Social

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-17	VL_LUC_ACUM_EST - Lucros Acumulados em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Não	MFS-17095		RNGW200-18	VL_LUC_ACUM - Lucros Acumulados

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-19	VL_ATIV_TANG_EST - Ativos Tangíveis em Moeda Estrangeira

Recuperar e preencher com o valor informado no campo.
	Não	MFS-17095		RNGW200-20	VL_ATIV_TANG - Ativos Tangíveis

Recuperar e preencher com o valor informado no campo.
	Sim	MFS-17095		RNGW200-21	NUM_EMP - Número de Empregados

Recuperar e preencher com o valor informado no campo.	Sim	MFS-17095		Registro W250: Declaração País-a-País – Entidades Integrantes
Campo Chave: 
Ocorrência: 1:N

CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGW250	Para a geração deste registro, recuperar as informações da tela Declaração Pais a Pais (Bloco W) do registro W250, se na tela de perfil de geração o mesmo esteja selecionado para geração.

Regras de geração do registro (que estão sendo feitas na tela e importação do bloco w): 

- Se o campo IND_CONTROLADORA - Indicador de Entidade Controladora Final do registro W100 for igual a S e se o campo IND_ENTREGA - Entidade Responsável pela Entrega for igual a 2,ou
- Se o campo IND_ENTREGA - Entidade Responsável pela Entrega for igual a 3, 

Caso contrário o registro não poderá ser gerado.

	Não	MFS-17095		RNGW250-01	REG – Tipo de Registro

Gerar fixo ‘W250’
	Sim	MFS-17095		RNGW250-02	JUR_DIFERENTE - Jurisdição Tributária de Organização ou Incorporação

Recuperar e preencher com o valor informado na tela (campo CÓDIGO da tabela CBC_PAIS_ACORDO_Jurisdicao).
	Não	MFS-17095		RNGW250-03	NOME - Entidade Integrante

Recuperar e preencher com o valor informado no campo.	Sim	MFS-17095		RNGW250-04	TIN - Tax - Identification Number (TIN)
Recuperar e preencher com o valor informado no campo.

Validações:

Poderá ser cadastrado mais de um registro com o campo 4 (Tax Identification Number (TIN)) igual a 'NOTIN', mas, só será permitido um registro com o mesmo TIN na base. Se for identificado mais de um registro com o mesmo TIN (diferente de NOTIN), exibir a mensagem DW00263. 

	Sim	MFS-17095		RNGW250-05	JURISDICAO_TIN - Jurisdição de Emissão do TIN

Recuperar e preencher com o valor informado na tela (campo CÓDIGO da tabela CBC_PAIS_ACORDO_Jurisdicao).
	Não	MFS-17095		RNGW250-06	NI - Número de Identificação (NI)

Recuperar e preencher com o valor informado no campo.	Não	MFS-17095		RNGW250-07	JURISDICAO_NI - Jurisdição de Emissão do NI

Recuperar e preencher com o valor informado na tela (campo CÓDIGO da tabela CBC_PAIS_ACORDO_Jurisdicao).
	Não	MFS-17095		RNGW250-08	TIPO_NI - Tipo do NI

Recuperar e preencher com o valor informado no campo.	Não	MFS-17095		RNGW250-09	TIP_END - Tipo do Endereço

Recuperar e preencher com o valor informado no campo.	Sim	MFS-17095		RNGW250-10	ENDEREÇO – Endereço

Recuperar e preencher com o valor informado no campo.	Sim	MFS-17095		RNGW250-11	NUM_TEL – Telefone
Recuperar e preencher com o valor informado no campo.	Não	MFS-17095		RNGW250-12	EMAIL - E-mail
Recuperar e preencher com o valor informado no campo.	Não	MFS-17095		RNGW250-13	ATIV_1 - Pesquisa e Desenvolvimento

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-14	ATIV_2 - Gestão de Propriedade Intelectual

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-15	ATIV_3 – Compras

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-16	ATIV_4 - Manufatura ou Produção

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-17	ATIV_5 - Vendas, Marketing ou Distribuição.

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-18	ATIV_6 - Serviços Administrativos, de Gestão ou de Suporte

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-19	ATIV_7 - Prestação de Serviços a Partes Não Relacionadas

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-20	ATIV_8 - Departamento Financeiro do Grupo

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-21	ATIV_9 - Serviços Financeiros Regulamentados

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-22	ATIV_10 – Seguro

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-23	ATIV_11 - Gestão de Ações e Outros Instrumentos de Capital

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-24	ATIV_12 – Inativa

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-25	ATIV_13 – Outros

Recuperar e preencher com o valor informado no campo (S/N).	Sim	MFS-17095		RNGW250-26	DESC_OUTROS - Descrição da Atividade Econômica Desempenhada
Recuperar e preencher com o valor informado no campo	Não	MFS-17095		RNGW250-27	OBSERVAÇÃO - Outras Informações
Recuperar e preencher com o valor informado no campo	Não	MFS-17095		Registro W300: OBSERVAÇÕES ADICIONAIS -  DECLARAÇÃO PAÍS-A-PAÍS
Campo Chave: 
Ocorrência: 0:N


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGW300-00	Para a geração deste registro, recuperar as informações da tela Declaração Pais a Pais (Bloco W) do registro W300, se na tela de perfil de geração o mesmo esteja selecionado para geração.

 Regra de geração do registro (que está sendo feita na tela e importação do bloco w):

Se no campo 0020.PAIS_A_PAIS (Entidade Integrante de Grupo Multinacional – Tela de Informações ECF for marcada com “S” .

Validação:

-Se for gerado um registro W100 com o campo 7 - IND_ENTREGA (Entidade Responsável pela Entrega) igual a ‘4’ e se existir algum w300 com qualquer campo de lista preenchido com ‘S’ ou com o campo Jurisdição preenchido, exibir a mensagem DW00264

-Se não for gerado um registro W100, mas existir um registro W300 com qualquer campo de lista preenchido com ‘S’ ou com o campo Jurisdição preenchido, exibir a mensagem DW00264.
	-	MFS-17095		RNGW300-01	REG – Tipo de Registro

Gerar fixo ‘W300’
	Sim	MFS-17095		RNGW300-02	JURISDICAO

Recuperar e preencher com o valor informado na tela (campo CÓDIGO da tabela CBC_PAIS_ACORDO_Jurisdicao).
	Não	MFS-17095		RNGW300-03	IND_REC_NAO_REL - Receitas Provenientes de Partes Não Relacionadas

Recuperar e preencher com o valor informado no campo (S/N).
	Não	MFS-17095		RNGW300-04	IND_REC_REL - Receitas Provenientes de Partes Relacionadas

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-05	IND_REC_TOTAL - Receita Total

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-06	IND_LUC_PREJ_ANTES_IR - Lucro ou Prejuízo Antes do IR

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-07	IND_IR_PAGO - Imposto de Renda Pago

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-08	IND_IR_DEVIDO - Imposto de Renda Devido

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-09	
IND_CAP_SOC – Capital Social

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-10	IND_LUC_ACUM – Lucros Acumulados

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-11	IND_ATIV_TANG - Ativos Tangíveis

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-12	IND_NUM_EMP - Número de Empregados

Recuperar e preencher com o valor informado no campo (S/N).	Não	MFS-17095		RNGW300-13	OBSERVAÇÃO - Observação

Recuperar e preencher com o valor informado no campo.	Sim	MFS-17095		RNGW300-14	FIM_OBSERVACAO - Indicador de fim das observações

Texto fixo contendo “W300FIM”.	Sim	MFS-17095		
Registro W990: Encerramento do Bloco W
Campo Chave: REG
Ocorrência: 1:1


CÓD	DESCRIÇÃO	OBRIG.	MFS		RNGW990-01	REG – Tipo de Registro

Gerar fixo ‘W990’		MFS-17095		RNGW990-02	QTD_LIN – Quantidade Total de Registro do Bloco w

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco W e informar o total.
Considerando que Campo 1: Texto fixo contendo "W990", e campo 2: Quantidade total de linhas do bloco W.

Exemplo: |W990|25|		MFS-17095		
Considerações deste modelo:

Quando uma Regra de Negócio for excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN