# MTZ_ECF_BlocoJ

> Fonte: MTZ_ECF_BlocoJ.doc

THOMSON REUTERS

ECF – Geração do Arquivo
Bloco J


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		07/03/2018	MFS-17086	Criação do Documento	Alessandra Cristina Navatta		19/06/2018	MFS-19224	Inclusão das regras do registro J053.	Alessandra Cristina Navatta		31/07/2018	MFS-17086	Inclusão da mensagem DW00001 em todos os campos obrigatórios do registro J050, que não estão como obrigatórios na tabela X2002.	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc520794447" 1.	INTRODUÇÃO	 PAGEREF _Toc520794447 \h 3
 HYPERLINK \l "_Toc520794448" 2.	Regras de Negócio	 PAGEREF _Toc520794448 \h 3
 HYPERLINK \l "_Toc520794449" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc520794449 \h 3
 HYPERLINK \l "_Toc520794450" 2.2	Registros Identificadores	 PAGEREF _Toc520794450 \h 3
 HYPERLINK \l "_Toc520794451" 2.2.1	Registro J001: Abertura do Bloco J	 PAGEREF _Toc520794451 \h 5
 HYPERLINK \l "_Toc520794452" 2.2.2	Registro J050: Plano de Contas do Contribuinte	 PAGEREF _Toc520794452 \h 6
 HYPERLINK \l "_Toc520794453" 2.2.3	Registro J051: Plano de Contas Referencial	 PAGEREF _Toc520794453 \h 9
 HYPERLINK \l "_Toc520794454" 2.2.4	Registro J053: Subcontas Correlatas	 PAGEREF _Toc520794454 \h 10
 HYPERLINK \l "_Toc520794455" 2.2.5	Registros J100: Centro de Custos	 PAGEREF _Toc520794455 \h 12
 HYPERLINK \l "_Toc520794456" 2.2.6	Registros J990: Encerramento do Bloco J	 PAGEREF _Toc520794456 \h 14

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO
Este bloco tem o objetivo de apresentar o mapeamento do plano de contas contábil para o plano de contas referencial. Os registros deste bloco, conforme orientações do guia prático podem ser:
Digitados;
Importados;
Replicados a partir do Bloco E; ou
Recuperados da ECF do período imediatamente anterior ao período da escrituração atual, transmitida via Sped.

Regras de Negócio
Informações gerais de seleção e processamento

As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.

CÓD	DESCRIÇÃO	MFS		RNG-J	Para a geração deste bloco, o sistema deve recuperar os dados das tabelas de cadastro do plano de contas, centro de custo e plano referencial x plano empresa que são utilizados pelo estabelecimento indicado no bloco 0 e/ou as contas contábeis contidas na tela de Informações Econômicas e Gerais (Blocos X e Y) para o Registro Y665.

Serão recuperados os dados que estão nos registros gerados na importação de saldos e que estão associados à Conta Referencial, considerando o período da escrituração (data inicial do primeiro registro da abertura do período à data final do último registro da abertura do período).

Aplicar a RNG00051 - Geração dos Registros

Na tela de Perfil de geração o registro deve estar selecionado para a geração.

		MFS-17086		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		J001	1	Abertura do Bloco J – Plano de Contas e Mapeamento


	F	O
	[1:1]		J050	2	Plano de Contas do Contribuinte	F	OC
Obrigatório se (0010. FORMA_TRIB = “1”, “2”, “3” ou “4”) 
OU 
(0010. FORMA_TRIB = “5” ou “7” ou “8” ou “9” E
0010.TIP_ESC_PRE = “C”)
Senão, não deve existir.	Se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4” OU 
(0010. FORMA_TRIB = “8” ou “9” E
0010. APUR_CSLL  QUOTE   “D”) E
0020.TIP_ECF  QUOTE   2 
 [1:N]
Senão 
[0:N]		 J051	3	Plano de Contas Referencial	F	Até versão 2.00:

OC
Obrigatório se 
(J050.IND_CTA = “A”)
E
(J050_COD_NAT = “01” ou “02” ou “03” ou “04”)
N
Senão, não deve existir.

A partir da versão 3.00:

OC
Obrigatório se (J050.IND_CTA =“A”)
E (J050.COD_NAT = “01” ou “02” ou “03” ou “04”) 
OU
(0010. FORMA_TRIB = “5” ou “7”
ou “8” ou “9” E 0010.TIP_ESC_PRE
= “C”)
N
Senão, não deve existir.	Se 
J050.IND_CTA = “A”
[1:N]
Senão
[0]		J053	3	Subcontas Correlatas	F	F
	[0:N]		 J100	2	Centro de Custos
	F	FC
Facultativo se 
(0010.FORMA_TRIB = “1” ou “2” ou “3” ou “4”)
OU
(0010. FORMA_TRIB = “5” ou “7” ou “8” ou “9” E 
0010.TIP_ESC_PRE = “C”)
F
Senão, não deve existir.	[0:N]		 J990	1	Encerramento do Bloco J
	F	O	[1:1]		
Registro J001: Abertura do Bloco J
Campo Chave: REG
Ocorrência: 1:1

CÓD	DESCRIÇÃO	MFS		RNGJ001-01	REG – Tipo de Registro

Gerar fixo ‘J001’	MFS-17086		RNGJ001-02	IND_DAD - Indicador do Movimento

Caso existirem informações nos registros do bloco J (registros J050, J051ou J100), preencher com “0”, caso contrário, preencher com “1”.
	MFS-17086		Registro J050: Plano de Contas do Contribuinte
Campo Chave: DT_ALT + COD_CTA
Ocorrência: 0:N

CÓD	DESCRIÇÃO	MFS		RNGJ050	Este registro deve ser gerado quando:

Campo 05 – FORMA_TRIB (registro 0010) = “1”, “2”, “3” ou “4”) ou 
Campo 05 - FORMA_TRIB (registro 0010) = “5” ou “7” ou “8” ou “9” e campo 10 -TIP_ESC_PRE (registro 0010) = “C”, Senão, não deve existir.
Recuperação do Registro:
A recuperação deste registro deve considerar a opção selecionada no campo PLANO DE CONTAS E CENTROS DE CUSTOS da tela de Geração da ECF: 

Se estiver selecionado a opção “Completo”, o sistema deve considerar as informações da tabela de plano de contas, filtrando apenas as contas contábeis que estão associados à Conta Referencial (grupo do código da associação indicada na tela Informações ECF).

Se estiver selecionado a opção “Movimento no Período” a recuperação deste registro deve considerar as informações da tabela de plano de contas pertencentes ao estabelecimento indicado no Bloco 0, filtrando apenas as contas contábeis que estão nos registros gerados na importação de saldos e geração do arquivo e/ou contas contábeis informadas na tela Informações Econômicas e Gerais (Blocos X e Y) para o Registro Y665.

A recuperação das contas contábeis, para os filtros “Completo” e “Movimento no Período”, considerar:
Todos os registros vigentes na data inicial e data final do período da geração do arquivo magnético, compreendido na data do registro das Informações ECF recuperada (data inicial do primeiro registro da abertura do período à data final do último registro da abertura do período). Ou seja, as alterações que ocorrerem após o ano da geração do arquivo, não deve ser informado neste período do arquivo.
Para as contas contábeis recuperadas, deverão ser recuperadas também as contas sintéticas (conta superior) correspondentes as contas contábeis.

Exemplo: 
Considerando a geração do ECF do exercício de 2011 e os cadastros da conta XX:

Cadastro
Conta Contábil
Descrição
Criação/Alteração

01
XX
Desc1
01/01/2009

02
XX
Desc2
01/11/2009

03
XX
Desc3
01/05/2010

04
XX
Desc4
01/10/2010

05
XX
Desc5
01/07/2011

06
XX
Desc5
01/01/2012

Deve ser exibido um registro J050 para cada inclusão/alteração (com exceção dos cadastros 01, 02, 03 e 06), ou seja, mostrar o cadastro de uma determinada conta contábil (código) cujo:
- registros de data de validade mais próxima, menor ou igual a data inicial da apuração recuperada.  
- registros com data de validade compreendida no período das apurações recuperadas (vigente na data inicial do primeiro registro à data final do último registro das aberturas que foram recuperadas, mas compreendida no período da escrituração). 
Ordenação:
As contas sintéticas (contas superiores) e as contas analíticas correspondentes as contas sintéticas devem ser ordenadas pelo campo Nível onde primeiro serão exibidas todas as contas sintéticas e depois serão exibidas todas as contas analíticas.
 
Exemplo:

|J050|01012000|01|S|1|2328A||ATIVO|
|J050|01012000|03|S|1|2328.L||P. LIQUIDO|
|J050|01012000|02|S|1|2328.P||PASSIVO|
|J050|01012000|04|S|2|2328.10.02|2328.10|COMPRAS DE INSUMOS|
|J050|01012000|04|S|3|2328.10.002|2328.10.02|ESTOQUE NO FINAL DO PERIODO DE APURACAO|
|J050|01012000|04|S|3|2328.10.003|2328.10.03|ESTOQUE NO FINAL DO PERIODO DE APURACAO|
|J050|01012000|04|A|4|2328.11.0001|2328.11.001|OUTRAS RECEITAS OPERACIONAIS|
|J050|01012000|04|A|4|2328.11.0002|2328.11.002|OUTRAS RECEITAS OPERACIONAIS|
|J050|01012000|02|A|4|2328.5.9998|2328.5.998|TRANSITORIA - FORN. NACIONAIS|
	MFS-17086		RNGJ050-01	REG – Tipo de Registro

Gerar fixo ‘J050’
	MFS-17086		RNGJ050-02	DT_ALT -  Data de Atualização

Preencher com a informação do campo data inicial.
	MFS-17086		RNGJ050-03	COD_NAT - Código Natureza

Preencher o campo de acordo com as regras abaixo:

Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘0. Compensação’ preencher com ‘05’.
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘1. Ativo’ preencher com ‘01’.
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘2. Passivo’ preencher com ‘02’.
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘ 3 Despesa’ preencher com ‘04’.
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘4. Receita’ preencher com ‘04’.
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘5. Mutações Ativas ("Variações Patrimoniais" anuais)’ preencher com ‘09’.
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘6. Mutações Passivas ("Variações Patrimoniais" anuais)’ preencher com ‘09’.
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘7. Patrimônio Líquido’ preencher com ‘03’. 
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘8. Custo’ preencher com ‘04’.
Se o campo Indicador da Natureza (do registro recuperado) estiver preenchido com ‘9. Outros’ preencher com ‘09’.

Caso este campo não esteja preenchido, exibir a mensagem DW00001.	MFS-17086		RNGJ050-04	IND_CTA – Tipo de Conta 

Preencher de acordo com as regras abaixo:

Se o campo ‘Tipo de Conta’(do registro recuperado) estiver preenchido com ‘A - Analítica’, preencher com ‘A’
Se o campo ‘Tipo de Conta’ (do registro recuperado) estiver preenchido com ‘S- Sintética ’, preencher com ‘S’.
Caso este campo não esteja preenchido, exibir a mensagem DW00001.	MFS-17086		RNGJ050-05	NÍVEL– Nível da Conta 

Preencher com a informação do campo nível.

Caso este campo não esteja preenchido, exibir a mensagem DW00001.
	MFS-17086		RNGJ050-06	COD_CTA – Código da Conta 

Preencher com a informação do campo cód. da conta contábil.
	MFS-17086		RNGJ050-07	COD_CTA_SUP – Código da Conta Superior

Preencher com a informação do campo cód. da conta contábil sintética.
	MFS-17086		RNGJ050-08	CTA – Nome da Conta

Preencher com a descrição da conta contábil.

Caso este campo não esteja preenchido, exibir a mensagem DW00001.
	MFS-17086		

Registro J051: Plano de Contas Referencial
Campo Chave: COD_CTA_REF+COD_CCUS
Ocorrência:  0:N


CÓD	DESCRIÇÃO	MFS		RNGJ051	Este registro deve ser gerado quando:

Até versão 2.00:

Campo 04 – IND_CTA (registro J050) = “A” e Campo 03 –COD_NAT  (registro J050) = “01” ou “02” ou “03” ou “04”, Senão, não deve existir.

A partir da Versão 3.00:

Campo 04 – IND_CTA (registro J050) = “A” e Campo 03 –COD_NAT (registro J050) = “01” ou “02” ou “03” ou “04” ou se campo 05 - FORMA_TRIB (Registro 0010) = ‘5’, ou ‘7’, ou se ‘8’, ou ‘9’ e campo 10 - TIP_ESC_PRE = ‘C’ , Senão, não deve existir.
Atenção: As validações: Campo 04 – IND_CTA (registro J050) = “A” e Campo 03 –COD_NAT (registro J050) = “01” ou “02” ou “03” ou “04”, já estão sendo realizadas na integração e na tela de associação do Plano de Contas Referencial com o Plano da Empresa


Recuperação do Registro: A recuperação deste registro deve considerar o resultado da importação de saldos, considerando os grupos de Cadastros envolvendo todos os estabelecimentos da empresa, referente às informações da tabela de plano referencial x plano empresa e/ou contas contábeis informadas na tela Informações Econômicas e Gerais (Blocos X e Y) para o Registro Y665.
	MFS-17086		RNGJ051-01	REG – Tipo de Registro

Gerar fixo ‘J051’
	MFS-17086		RNGJ051-02	COD_CCUS – Código do Centro de Custo

Preencher com a informação do campo cód. do centro de custo.
	MFS-17086		RNGJ051-03	COD_CTA_REF– Código da Conta Referencial 

Preencher com a informação do campo cód. da conta referencial.
	MFS-17086		
Registro J053: Subcontas Correlatas
Campo Chave: COD_CNT_CORR 
Ocorrência: 0:N

CÓD	DESCRIÇÃO	MFS		RNGJ053	Este registro deve ser gerado para cada J050 que possuir associação na tela “Associação da subconta correlata com o plano de contas” cujo grupo corresponda ao estabelecimento que está sendo gerado e data inicial menor ou igual a data de geração do arquivo ECF 	MFS-19224		RNGJ053-01	REG – Tipo de Registro

Gerar fixo ‘J053’
	MFS-19224		RNGJ053-02	COD_IDT – Código de Identificação do Grupo Formado por Conta-Subconta(s)

Preencher com a informação do campo Cód. do Grupo.	MFS-19224		RNGJ053-03	COD_CNT_CORR– Código da Subconta Correlata

Preencher com a informação do campo Código da grid de Subconta Correlata.
	MFS-19224		RNGJ053-04	NAT_SUB_CNT - Natureza da Subconta Correlata

Preencher com a informação do campo Número da grid de Natureza da Subconta.


Lista de Valores Válidos:

A lista completa está cadastrada na Taces 90 (CAD_NAT_SUBCONTAS), sem a informação de versão.  Efetuar as validações de Valores válidos por Versão:

Para Versão 3.0:

02, 03, 10, 11, 12, 60, 65, 70, 71, 72, 73, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 90, 91, 92, 93

Caso o valor seja diferente da lista de valores válidos (por versão), exibir a mensagem DW00085.

Demais Regras a serem validadas:

Até Versão 1.0:

Caso exista mais de uma subconta de natureza “90”, “91”, “92”, “93” ou “95” para a mesma conta contábil no mesmo grupo e data inicial, exibir a mensagem DW00182.

A partir da Versão 2.0: 

Caso exista mais de duas subcontas de natureza “90”, “91”, “92”, “93” ou “95” para a mesma conta contábil no mesmo grupo e data inicial, exibir a mensagem DW00183.	MFS-19224		
Registros J100: Centro de Custos 
Campo Chave: DT_ALT + COD_CCUS
Ocorrência: 0:N

CÓD	DESCRIÇÃO	MFS		RNGJ100	Este registro deve ser gerado quando:

Campo 05 – FORMA_TRIB (registro 0010) = “1”, “2”, “3” ou “4”) ou 
Campo 05 - FORMA_TRIB (registro 0010) = “5” ou “7” ou “8” ou “9” e campo 10 -TIP_ESC_PRE (registro 0010) = “C” e se existir informações de centro de custo na base. Senão, não deve existir.

Recuperação do Registro:
A recuperação deste registro deve considerar a opção selecionada no campo PLANO DE CONTAS E CENTROS DE CUSTOS da tela de Geração da ECF: 

Se estiver selecionado a opção “Completo”, o sistema deve considerar as informações da tabela de centros de custos, filtrando apenas os centros de custos que estão associados à Conta Referencial (grupo do código da associação indicada na tela Informações ECF).

Se estiver selecionado a opção “Movimento no Período”, a recuperação deste registro deve considerar as informações da tabela de centro de custo pertencentes ao estabelecimento indicado no Bloco 0, filtrando apenas os centros de custos que estão nos registros gerados na importação de saldos e geração do arquivo e/ou contas contábeis informadas na tela Informações Econômicas e Gerais (Blocos X e Y) para o Registro Y665.

A recuperação dos centros de custos, para os filtros “Completo” e “Movimento no Período”, considerar
Todos os registros vigentes na data inicial e data final do período da geração do arquivo magnético, compreendido na data do registro da Informações ECF recuperada (data inicial do primeiro registro da abertura do período à data final do último registro da abertura do período). Ou seja, as alterações que ocorrerem após o ano da geração do arquivo, não deve ser informado neste período do arquivo.

Exemplo: 
Considerando a geração do ECF do exercício de 2011 e os cadastros do centro de custo YY:

Cadastro
Centro de Custo
Descrição
Criação/Alteração

01
YY
Desc1
01/01/2009

02
YY
Desc2
01/11/2009

03
YY
Desc3
01/05/2010

04
YY
Desc4
01/10/2010

05
YY
Desc5
01/07/2011

06
YY
Desc5
01/01/2012

Deve ser exibido um registro J100 para cada inclusão/alteração (com exceção dos cadastros 01, 02, 03 e 06), ou seja, mostrar o cadastro de um determinado centro de custo (código) cujo:
- registros de data de validade mais próxima, menor ou igual a data inicial da apuração recuperada.  
- registros com data de validade compreendida no período das apurações recuperadas (vigente na data inicial do primeiro registro à data final do último registro das aberturas que foram recuperadas, mas compreendida no período da escrituração). 
Ordenação: Os centros devem ser ordenados pelo campo código.	MFS-17086		RNGJ100-01	REG – Tipo de Registro

Gerar fixo ‘J100’
	MFS-17086		RNGJ100-02	DT_ALT -  Data de Alteração

Preencher com a informação do campo data inicial.
	MFS-17086		RNGJ100-03	COD_CCUS -  Código do Centro de Custos

Preencher com a informação do campo cód.do centro de custo.
	MFS-17086		RNGJ100-04	DT_ALT -  Nome do Centro de Custos

Preencher com a informação do campo desc.do centro de custo
	MFS-17086		Registros J990: Encerramento do Bloco J 
Campo Chave: REG
CÓD	DESCRIÇÃO	MFS		RNGJ990-01	REG – Tipo de Registro

Gerar fixo ‘J990’
	MFS-17086		RNGJ990-02	QTD_LIN – Quantidade Total de Registro do Bloco J

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco J e informar o total.
Considerando que Campo 1: Texto fixo contendo "J990", e campo 2: Quantidade total de linhas do bloco J.

Exemplo: |J990|384|	MFS-17086		 
Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN