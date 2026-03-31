# MTZ_ECF_BlocoK

> Fonte: MTZ_ECF_BlocoK.doc

THOMSON REUTERS

Geração do Bloco K


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		08/03/2018	MFS-17087	Criação do Documento. 	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc508288855" 1.	INTRODUÇÃO	 PAGEREF _Toc508288855 \h 3
 HYPERLINK \l "_Toc508288856" 2.	Regras de Negócio	 PAGEREF _Toc508288856 \h 3
 HYPERLINK \l "_Toc508288857" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc508288857 \h 3
 HYPERLINK \l "_Toc508288858" 2.2	Registros Identificadores	 PAGEREF _Toc508288858 \h 3
 HYPERLINK \l "_Toc508288859" 2.2.1	Registro K001: Abertura do Bloco K	 PAGEREF _Toc508288859 \h 4
 HYPERLINK \l "_Toc508288860" 2.2.2	Registro K030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário	 PAGEREF _Toc508288860 \h 4
 HYPERLINK \l "_Toc508288861" 2.2.3	Registro K155: Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)	 PAGEREF _Toc508288861 \h 7
 HYPERLINK \l "_Toc508288862" 2.2.4	Registro K156: Mapeamento Referencial do Saldo Final	 PAGEREF _Toc508288862 \h 10
 HYPERLINK \l "_Toc508288863" 2.2.5	Registro K355: Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento	 PAGEREF _Toc508288863 \h 12
 HYPERLINK \l "_Toc508288864" 2.2.6	Registro K356: Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento	 PAGEREF _Toc508288864 \h 14
 HYPERLINK \l "_Toc508288865" 2.2.7	Registro K990: Encerramento do Bloco K	 PAGEREF _Toc508288865 \h 16

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO

Este bloco tem o objetivo de apresentar os Saldos das Contas Contábeis e Referenciais.
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-K	Período de recuperação dos registros: Data Inicial e Final do Período de Apuração informada na tela de Abertura da Apuração durante o Processamento em Lote.

Data Inicial e Data Final informadas da tela de Geração da ECF.
Só serão geradas informações neste bloco se o campo Forma de Tributação for “Lucro Real”, ”Presumido”, “Imune de IRPJ” ou Isento de IRPJ”.

Recuperação das informações terão como origem as tabelas utilizadas na tela de ajuste manual do bloco K e na tabela referente à demonstração do resultado.

Aplicar a RNG00051 – Geração dos Registros

Na tela de Perfil de geração o registro deve estar selecionado para a geração.
		MFS-17087		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		K001	1	Abertura do Bloco K	F	O	[1:1]		 HYPERLINK \l "N030" K030	2	Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário	F		[0:13]		K155	3	Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)
		F	O


	[0:N]		K156	4	Mapeamento Referencial do Saldo Final
	F		[1:N]		K355	3	Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento	F		[1:N]		K356	4	Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento
	F		[1:N]		K990	1	Encerramento do Bloco K
	F	O	[1:1]		

Registro K001: Abertura do Bloco K
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico – 1

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGK001-01	REG – Tipo de Registro

Gerar fixo ‘K001’	Sim	MFS-17087		RNGK001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco K (registros K030, K155, K156, K355,356), preencher com “0”, caso contrário, preencher com “1”.
	Sim	MFS-17087		
Registro K030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário
Campo Chave: PER_APUR
Ocorrência: 0:13
Nível Hierárquico – 2

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGK030	
Só serão geradas informações neste bloco de acordo com as Informações ECF abaixo: 

Se existir pelo menos uma abertura de apuração com Forma de tributação igual a Lucro Real ou Lucro Real e Lucro Arbitrado ou Lucro Presumido e Lucro Real ou Lucro Presumido, Lucro Real e Lucro Arbitrado na mesma informações ECF ou 
Se Forma de tributação igual a Lucro Presumido ou Lucro Presumido e Arbitrado ou Imune do IRPJ ou Isenta do IRPJ e tipo de escrituração igual a Contábil.

Conforme RNP01 documento MTZ_Processamento_em_Lote.docx.

Forma de Tributação = ‘Anual’ 


Deverá ser gerado um registro K030 A00 e A01 à A12 conforme recuperação da RNP01 – para o Período da Apuração = “Anual” o registro A01...A12 deverá ser criado de forma sequencial (A01....A12) considerando o ‘período de apuração’, onde:

Janeiro = A01
Fevereiro = A02
Março = A03
.
.
.
Dezembro = A12


Exceto:

Se a empresa possuir Apurações do IRPJ e CSLL iguais a Desobrigada, neste cenário apenas o A00 deve ser gerado.


Se a Forma de Tributação da Abertura de Apuração = ‘Lucro Real’ e parâmetro Tipo de Receita L= “Receita Bruta” ou “Comparativo” e Check-box RECEITA BRUTA (tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução) marcado, para a Abertura de Apuração correspondente não deverá ser gerado o registro para o Período de Apuração correspondente:

Deverá ser gerado um registro K030 - A00 conforme recuperação da RNP01 – para o Período da Apuração = “Anual”, independente do tipo de receita informado na tela Abertura da Apuração.

Forma de Tributação = ‘Trimestral’ 

Deverá ser gerado um registro K030 T01...T04, considerando o ‘período de apuração’, onde:

1º Trimestre = T01
2 º Trimestre = T02
3 º Trimestre = T03
4 º Trimestre = T04
	SIM	MFS-17087		RNGK030-01	REG – Tipo de Registro

Gerar fixo ‘K030’	SIM	MFS-17087		RNGK030-02	DT_INI - Data do Saldo Inicial 

A00, A01...A12 

Preencher este campo com a data inicial da primeira abertura de apuração encontrada no período parametrizado na tela de geração do ECF para o estabelecimento /SCP.
Exemplo: 
A02 - Data inicial: 01/01/2014

T01...T04
Preencher este campo com a data inicial da abertura de apuração do período que está sendo gerado para o estabelecimento /SCP.

Exemplo: 
T02 - Data inicial: 01/04/2014
	SIM	MFS-17087		RNGK030-03	DT_FIN- Data do Saldo Final

A00, A01...A12 e T01...T04

Preencher este campo com a data final da abertura de apuração do período que está sendo gerado para o estabelecimento /SCP.
.
Exemplo: 
A02 - Data final: 28/02/2014
T02 - Data final: 30/06/2014
		MFS-17087		RNGK030-04	PER_APUR – Período de Apuração:

Preencher conforme RNGK030.
	SIM	MFS-17087		
Registro K155: Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)
Campo Chave: COD_CTA + COD_CCUS
Ocorrência – 0:N
Nível Hierárquico – 3

Condições Gerais: 

Registro onde devem ser informados os saldos iniciais, os saldos finais, os totais de débitos e os totais de créditos de todas as contas patrimoniais da escrituração societária da pessoa jurídica (Ativo, Passivo e Patrimonio Liquido), no período de apuração.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGK155	Para a geração deste registro, recuperar informações conforme abaixo:

Recuperar da tela de ajuste manual do bloco K e da tela de demonstração de resultado as apurações processadas pela rotina de processamentos em lote conforme o documento MTZ_Processamento_em_Lote.docx com base na RNP04.
As informações recuperadas poderão ser identificadas na tela de Ajuste Manual do Bloco K e também na tela de Demonstração do Resultado referente aos registros K155/156.
Ordenação: As contas contábeis analíticas e o centro de custo correspondente devem ser ordenados de forma crescente com base no código da conta contábil e centro de custo.	-	MFS-17087		RNGK155-01	REG – Tipo de Registro

Gerar fixo ‘K155’
	SIM	MFS-17087		RNGK155-02	COD_CTA - Código da Conta.

Recuperar o código da conta contábil conforme tela de ajuste manual do bloco K (abas Rateio e Demais Ajustes).
	SIM	MFS-17087		RNGK155-03	COD_CCUS – Código Centro Custos.

Recuperar o código centro de custo associado à conta contábil conforme RNGK155-02 conforme tela de ajuste manual do bloco K.
	NÃO	MFS-17087		RNGK155-04	VL_SLD_INI - Valor do Saldo Inicial

Considerar a conta gerada conforme RNGK155-02 correspondente a data recuperada na RNGK030-03.

Se o saldo não teve ajuste manual, considerar o campo “Saldo Inicial Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Saldo Inicial Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Inicial Informado” estiver preenchido, esse é o valor que deve ser considerado. 

Se não houver saldo, gerar zero.
	SIM	MFS-17087		RNGK155-05	IND_VL_SLD_INI - Situação do Saldo Inicial

Recuperar o indicador do saldo inicial para a conta gerada conforme RNGK155-02 de acordo com o campo “Ind. do Saldo Inicial” da tela de Demonstração do Resultado.

Se o saldo não teve ajuste manual, considerar o “Indicador do Saldo Inicial Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Indicador do Saldo Inicial Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Inicial Informado” estiver preenchido, esse valor e o respectivo indicador devem ser considerados.

Tipos válidos para a recuperação:

Se no campo “Ind. do Saldo Inicial” o conteúdo for “D” ou “C” gerar “D” para Débito ou “C” para Crédito.

Quando o saldo RNGK155-04 da conta RNGK155-02 for zero gerar o “C” para Crédito.  
	NÃO	MFS-17087		RNGK155-06	VL_DEB - Valor do Total de Débitos

Recuperar o conteúdo do campo “Valor Total de Débitos” da tela de Demonstração do Resultado para a conta gerada conforme RNGK155-02.

Se não houver valor correspondente a movimentação, gerar zero.

	SIM	MFS-17087		RNGK155-07	VL_CRED - Valor do Total de Créditos

Recuperar o conteúdo do campo “Valor Total de Créditos” da tela de Demonstração do Resultado para a conta gerada conforme RNGK155-02.

Se não houver valor correspondente a movimentação, gerar zero.
	SIM	MFS-17087		RNGK155-08	VL_SLD_FIN - Valor do Saldo Final

Considerar a conta gerada conforme RNGK155-02 correspondente a data recuperada na RNGK030-03.

Se o saldo não teve ajuste manual, considerar o campo “Saldo Final Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Saldo Final Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Final Informado” estiver preenchido, esse é o valor que deve ser considerado. 

Se não houver saldo, gerar zero. 
	SIM	MFS-17087		RNGK155-09	IND_VL_SLD_FIN - Situação do Saldo Final

Valores Válidos

“D” - Débito 
“C” - Crédito

Tratamentos:

Se o saldo não teve ajuste manual, considerar o “Indicador do Saldo Final Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Indicador do Saldo Final Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Final Informado” estiver preenchido, esse valor e o respectivo indicador devem ser considerados.

Se o saldo de uma conta for igual a zero, gerar “C” para Crédito.  

	NÃO	MFS-17087		
Registro K156: Mapeamento Referencial do Saldo Final
Campo Chave: COD_CTA_REF
Ocorrência – 1:N
Nível Hierárquico – 4

Condições Gerais: 

Registro utilizado para mapeamento, por conta referencial, dos saldos finais de todas as contas patrimoniais da escrituração societária da pessoa jurídica (Ativo, Passivo e Patrimônio Líquido), nos respectivos peeríodo de apuração. Registro obrigatório apenas para as contas contabeis/centro de custos para as quais foram mapeadas mais de uma conta referencial no registro J051.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGK156	Para a geração deste registro, recuperar informações conforme abaixo:

Recuperar da tela de ajuste manual do bloco K e da tela de demonstração de resultado as apurações processadas pela rotina de processamentos em lote conforme o documento MTZ_Processamento_em_Lote.docx com base na RNP05.

As informações recuperadas poderão ser identificadas na tela de Ajuste Manual do Bloco K e também na tela de Demonstração do Resultado referente aos registros K155/156.	-	MFS-17087		RNGK156-01	REG – Tipo de Registro

Gerar fixo ‘K156’
	SIM	MFS-17087		RNGN156-02	COD_CTA_REF - Código da Conta Referencial

Recuperar o conteúdo do campo cód. da conta referencial conforme tela de ajuste manual do bloco K (abas Rateio e Demais Ajustes).
	SIM	MFS-17087		RNGK156-03	VL_SLD_FIN – Valor do Saldo Final.

Considerar a conta gerada conforme RNGK156-02 correspondente a data recuperada na RNGK030-03.

Se o saldo não teve ajuste manual, considerar o campo “Saldo Final Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Saldo Final Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Final Informado” estiver preenchido, esse é o valor que deve ser considerado. 

Se não houver saldo, gerar zero. 	SIM	MFS-17087		RNGN156-04	IND_VL_SLD_FIN - Situação do Saldo Final.

Valores Válidos

“D” - Débito 
“C” - Crédito

Tratamentos:

Se o saldo não teve ajuste manual, considerar o “Indicador do Saldo Final Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Indicador do Saldo Final Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Final Informado” estiver preenchido, esse valor e o respectivo indicador devem ser considerados.

Se o saldo da conta referencial for igual a zero, gerar “C” para Crédito.  
	SIM	MFS-17087		
Registro K355: Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento
Campo Chave: COD_CTA + COD_CCUS
Ocorrência – 1:N
Nível Hierárquico – 3

Condições Gerais: 

Registro onde devem ser informados os saldos finais de todas as contas de resultado da escrituração societária da pessoa jurídica antes do encerramento.

CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGK355	Para a geração deste registro, recuperar informações conforme abaixo:

Recuperar da tela de ajuste manual do bloco K e da tela de demonstração de resultado as apurações processadas pela rotina de processamentos em lote conforme o documento MTZ_Processamento_em_Lote.docx com base na RNP06.
As informações recuperadas poderão ser identificadas na tela de Ajuste Manual do Bloco K e também na tela de Demonstração do Resultado referente aos registros K355/356.
Ordenação: As contas contábeis analíticas e o centro de custo correspondente devem ser ordenados de forma crescente com base no código da conta contábil e centro de custo.	-	MFS-17087		RNGK355-01	REG – Tipo de Registro

Gerar fixo ‘K355’	SIM	MFS-17087		RNGK355-02	COD_CTA - Código de Conta

Recuperar o conteúdo do campo Cód. da Conta Contábil conforme tela de ajuste manual do bloco K (abas Rateio e Demais Ajustes).	SIM	MFS-17087		RNGK355-03	COD_CCUS – Centro de Custos

Recuperar o código centro de custo associado à conta contábil conforme RNGK355-02 conforme tela de ajuste manual do bloco K.	NÃO	MFS-17087		RNGK355-04	VL_SLD_FIN - Valor do Saldo Final


Se o saldo não teve ajuste manual, considerar o campo “Saldo Final Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Saldo Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Informado” estiver preenchido, esse é o valor que deve ser considerado. 

Se não houver saldo, gerar zero.

	SIM	MFS-17087		RNGK355-05	IND_VL_SLD_FIN - Situação do Saldo Final

Valores Válidos

 “D” - Débito 
 “C” - Crédito

Tratamentos:

Se o saldo não teve ajuste manual, considerar o “Indicador do Saldo Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Indicador do Saldo Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Informado” estiver preenchido, esse valor e o respectivo indicador devem ser considerados.

Se o saldo de uma conta for igual a zero, gerar “C” para Crédito.  

	SIM	MFS-17087		
Registro K356: Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento
Campo Chave: COD_CTA_REF
Ocorrência – 1:N
Nível Hierárquico – 4

Condições Gerais: 


CÓD	DESCRIÇÃO	
OBRIG	MFS		RNGK356	Para a geração deste registro, recuperar informações conforme abaixo:

Recuperar da tela de ajuste manual do bloco K e da tela de demonstração de resultado as apurações processadas pela rotina de processamentos em lote conforme o documento MTZ_Processamento_em_Lote.docx com base na RNP07.
As informações recuperadas poderão ser identificadas na tela de Ajuste Manual do Bloco K e também na tela de Demonstração do Resultado referente aos registros K355/356.		MFS-17087		RNGK356-01	REG – Tipo de Registro

Gerar fixo ‘K356’
	SIM	MFS-17087		RNGK356-02	COD_CTA_REF - Código da Conta Referencial.

Recuperar o conteúdo do campo cód. da conta referencial conforme tela de ajuste manual do bloco K (abas Rateio e Demais Ajustes).
	SIM	MFS-17087		RNGK356-03	VL_SLD_FIN - Valor do Saldo Final 

Se o saldo não teve ajuste manual, considerar o campo “Saldo Final Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Saldo Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Informado” estiver preenchido, esse é o valor que deve ser considerado. 

Se não houver saldo, gerar zero.
	SIM	MFS-17087		RNGK356-04	IND_VL_SLD_FIN - Situação do Saldo Final

Valores Válidos

 “D” - Débito 
 “C” - Crédito

Tratamentos:

Se o saldo não teve ajuste manual, considerar o “Indicador do Saldo Calculado” para a geração do Bloco K. 

Se o saldo teve ajuste manual, considerar o campo “Indicador do Saldo Informado” para a geração do Bloco K. 

Ou seja, toda vez que o campo “Saldo Informado” estiver preenchido, esse valor e o respectivo indicador devem ser considerados.

Se o saldo de uma conta for igual a zero, gerar “C” para Crédito.  

	SIM	MFS-17087		
Registro K990: Encerramento do Bloco K
Campo Chave: REG
Ocorrência – 1:1
Nível Hierárquico – 1

Condições Gerais: 


CÓD	DESCRIÇÃO	MFS		RNGK990-01	REG – Tipo de Registro

Gerar fixo ‘K990’	MFS-17087		RNGK990-02	QTD_LIN – Quantidade Total de Registro do Bloco K

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco K e informar o total.
Considerando que Campo 1: Texto fixo contendo "K990", e campo 2: Quantidade total de linhas do bloco K.

Exemplo: |K990|25|	MFS-17087		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN