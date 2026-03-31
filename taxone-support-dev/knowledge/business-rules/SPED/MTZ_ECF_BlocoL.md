# MTZ_ECF_BlocoL

> Fonte: MTZ_ECF_BlocoL.doc

THOMSON REUTERS

Geração do Bloco L


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		08/03/2018	MFS-17088	Criação do Documento	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc508291266" 1.	INTRODUÇÃO	 PAGEREF _Toc508291266 \h 3
 HYPERLINK \l "_Toc508291267" 2.	Regras de Negócio	 PAGEREF _Toc508291267 \h 3
 HYPERLINK \l "_Toc508291268" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc508291268 \h 3
 HYPERLINK \l "_Toc508291269" 2.2	Registros Identificadores	 PAGEREF _Toc508291269 \h 3
 HYPERLINK \l "_Toc508291270" 2.2.1	Registro L001: Abertura do Bloco L	 PAGEREF _Toc508291270 \h 5
 HYPERLINK \l "_Toc508291271" 2.2.2	Registro L030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário	 PAGEREF _Toc508291271 \h 6
 HYPERLINK \l "_Toc508291272" 2.2.3	Registro L100: Balanço Patrimonial	 PAGEREF _Toc508291272 \h 8
 HYPERLINK \l "_Toc508291273" 2.2.4	Registros L200: Método de Avaliação de Estoques	 PAGEREF _Toc508291273 \h 10
 HYPERLINK \l "_Toc508291274" 2.2.5	Registros L210: Informativo de Composição de Custos	 PAGEREF _Toc508291274 \h 11
 HYPERLINK \l "_Toc508291275" 2.2.6	Registros L300: Demonstração do Resultado do Lucro Líquido Fiscal	 PAGEREF _Toc508291275 \h 12
 HYPERLINK \l "_Toc508291276" 2.2.7	Registros L990: Encerramento do Bloco L	 PAGEREF _Toc508291276 \h 14

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO
Este bloco tem o objetivo de apresentar o Lucro Líquido.

Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO		RNG-L	- Período de recuperação dos registros: Partindo da Escrituração ECF, foco deste processamento, deveremos considerar todas as suas apurações que estão compreendidas entre a data inicial e final da tela de geração da ECF.

- Só serão geradas informações neste bloco se o campo Forma de Tributação for “Lucro Real”. 

- A exibição do conteúdo referente “Cód. do Registro” e “Cód. da Conta Referencial” deve respeitar a sequência da coluna Código

- Aplicar a RNG00051 - Geração dos Registros

-Na tela de Perfil de geração o registro deve estar selecionado para a geração.


		MFS-17088		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		L001	1	Abertura do Bloco L – Lucro Real
	F	O	[1:1]		L030	2	Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário	F	OC
Obrigatório se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
N
Senão, não deve existir.	Se 
0010. FORMA_TRIB = “1”, “2”, “3” ou “4”
[1:13]
Senão
[0]		L100	3	Balanço Patrimonial 	F	OC
Obrigatório se
(L030.PER_APUR = “A00” OU [T01..T04])
OU 
([A01..A012]  E mês correspondente  no 0010. MES_BAL_RED [1..12] for igual = “B”).
N
Senão, não deve existir.	Se 
L030.PER_APUR = “A00” OU [T01..T04]
OU ([A01..A012]  E mês correspondente  no 0010. MES_BAL_RED [1..12] for igual = “B”).
[1:N]

Senão
[0]
		L200	3	Método de Avaliação do Estoque Final	F	OC
Obrigatório se
(COD_QUALIF_PJ = “01”) 
E
(L030.PER_APUR = “A00”  OU [T01..T04]) 
OU  
([A01..A012]  E mês correspondente  no 0010. MES_BAL_RED [1..12] for igual = “B”)
N
Senão, não deve existir.	Se
COD_QUALIF_PJ = “01” E
(L030.PER_APUR = “A00”  OU [T01..T04])  OU 
([A01..A012] E mês correspondente  no 0010. MES_BAL_RED [1..12] for igual = “B”) 
[0:N]
Senão  
[0]

A partir da versão 3.00:

Se COD_QUALIF_PJ = “01” E (L030.PER_APUR = “A00” OU [T01..T04]) OU
([A01..A012] E mês correspondente no 0010.MES_BAL_RED [1..12] for igual = “B”)
[0:13] Senão [0]		L210	4	Informativo da Composição de Custos	F	OC
Obrigatório se
COD_QUALIF_PJ = “01” E
(L030.PER_APUR = “A00” OU
[T01..T04]) OU ([A01...A012] E  mês
correspondente no 0010. MES_BAL_RED
[1...12] for igual = “B”)
N
Senão, não deve existir.	Se
COD_QUALIF_PJ = “01” E
(L030.PER_APUR = “A00” OU
[T01..T04]) OU
([A01..A012] E  mês correspondente no
0010. MES_BAL_RED [1..12] for igual =
“B”)
[0:N]
Senão [0]		L300	3	 Demonstração do Resultado Líquido no Período Fiscal	F	OC
Obrigatório se
(L030.PER_APUR = “A00” OU [T01..T04])
OU 
([A01..A012]  E mês correspondente  no 0010. MES_BAL_RED [1..12] for igual = “B”).
N
Senão, não deve existir.	Se 
L030.PER_APUR = [A01...A012] E mês correspondente no 
0010. MES_BAL_RED[1...12] for igual a “E” ou “0”
[0]
Senão
[1:N]		L990	1	Encerramento do Bloco L
	F	O	[1:1]		

Registro L001: Abertura do Bloco L
Campo Chave: REG
Ocorrência: 1:1

CÓD	DESCRIÇÃO	MFS		RNGL001-01	REG – Tipo de Registro

Gerar fixo ‘L001’	MFS-17088		RNLG001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco L (registros L030, L100, L200, L210, L300), preencher com “0”, caso contrário, preencher com “1”.
	MFS-17088		
Registro L030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário
Campo Chave: PER_APUR
Ocorrência: 0:13

CÓD	DESCRIÇÃO	MFS		RNGL030	
Só serão geradas informações neste bloco se o campo 05 – FORMA_TRIB do registro 0010 estiver preenchido com “1”,”2”,”3” ou “4” conforme RNP01 documento MTZ_Processamento_em_Lote.docx.  

Forma de Tributação = ‘Anual’ 


Deverá ser gerado um registro L030 A01 à A12 conforme recuperação da RNP01 – para o Período da Apuração = “Anual” e parâmetro Tipo de Receita = ‘Balanço Suspensão ou Redução’ ou ‘Comparativo’ e Checkbox BALANÇO DE SUSPENSÃO/REDUÇÃO na tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução marcado para a Abertura de Apuração correspondente. Neste caso, o registro A01...A12 deverá ser criado de forma sequencial (A01....A12) considerando o ‘período de apuração’, onde:

Janeiro = A01
Fevereiro = A02
Março = A03
.
.
.
Dezembro = A12


Deverá ser gerado um registro L030 A00 conforme recuperação da RNP01 – para o Período da Apuração = “Anual”, independente do tipo de receita informado na tela Abertura da Apuração.

Forma de Tributação = ‘Trimestral’ 

Deverá ser gerado um registro L030 para cada abertura de apuração da escrituração, com forma de tributação = ‘Lucro Real’ Neste caso, o registro T01...T04 deverá ser criado de forma sequencial (T01....T04) considerando o ‘período de apuração’, onde:

1º Trimestre = T01
2 º Trimestre = T02
3 º Trimestre = T03
4 º Trimestre = T04

	MFS-17088		RNGL030-01	REG – Tipo de Registro

Gerar fixo ‘L030’	MFS-17088		RNL030-02	DT_INI - Data do Saldo Inicial 

A00, A01...A12 
Preencher este campo com a data inicial primeira abertura de apuração encontrada no período parametrizado na tela de geração do ECF para o estabelecimento matriz/SCP.Exemplo: 
A02 - Data inicial: 01/01/2014

T01...T04
Preencher este campo com a data inicial da abertura de apuração do período que está sendo gerado para o estabelecimento matriz/SCP.

Exemplo: 
T02 - Data inicial: 01/04/2014
	MFS-17088		RNL030-03	DT_FIN- Data do Saldo Final

A00, A01...A12 e T01...T04

Preencher este campo com a data final da abertura de apuração do período que está sendo gerado para o estabelecimento matriz/SCP.
.
Exemplo: 
A02 - Data final: 28/02/2014
T02 - Data final: 30/06/2014
	MFS-17088		RNL030-04	PER_APUR – Período de Apuração:

Preencher conforme RNGL030.
	MFS-17088		
Registro L100: Balanço Patrimonial
Campo Chave: CODIGO
Ocorrências: 0:N


CÓD	DESCRIÇÃO	MFS		RNGL100	Só deve ser geradas informações neste bloco se o campo 04 – PER_APUR do registro L030 estiver preenchido com ‘A00’ ou ‘T01’, ‘T02’, ’T03’, ’T04’ ou ‘A01’, ‘A02’, ‘A03’, ‘A04’, ‘A05’, ‘A06’, ‘A07’, ‘A08’, ‘A09’, ‘A10’, ‘A11’, ‘A12’ e se o campo 09 – MÊS_BAL_RED  do registro 0010 estiver preenchido com ‘B’.

As informações a serem geradas neste registro terão como base a tabela resultado do processamento “tela de demonstração do resultado do processamento dos registros” das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Regras de Recuperação: 

Recuperar o saldo inicial e final dos registros que foram processados na importação de saldos, através da tabela referencial cujo campo registro seja iniciado com ‘L100’.

	MFS-17088		RNGL100-01	REG – Tipo de Registro

Gerar fixo ‘L100’	MFS-17088		RNGL100-02	CODIGO – Código da Conta Referencial 

Considerar o código da conta referencial do registro recuperado.
	MFS-17088		RNGL100-03	DESCRICAO – Descrição

Considerar a descrição da conta referencial do registro recuperados.
	MFS-17088		RNGL100-04	TIPO – Tipo da Conta

Considerar o campo ‘tipo’ da tabela referencial, da conta referencial recuperada. 
	MFS-17088		RNGL100-05	NIVEL – Nível da Conta

Considerar o campo ‘nível’ da tabela referencial, da conta referencial recuperada. 
	MFS-17088		RNGL100-06	COD_NAT – Natureza da Conta

Considerar o campo ‘natureza’ da tabela referencial, da conta referencial recuperada. 
	MFS-17088		RNGL100-07	COD_CTA_SUP- Código da Conta Superior

Considerar o campo ‘conta superior’ da tabela referencial, da conta referencial recuperada. 
	MFS-17088		RNGL100-08	VAL_CTA_REF_INI – Valor do Saldo Inicial

Considerar o valor do campo Saldo Inicial da conta referencial recuperada. 

	MFS-17088		RNGL100-09	IND_VAL_CTA_REF_INI – Indicador do Saldo Inicial

Considerar o indicador do saldo inicial da conta referencial recuperada.	MFS-17088		RNGL100-10	VAL_CTA_REF_FIN – Valor do Saldo Final

Considerar o valor do campo Saldo Final da conta referencial recuperada. 

	MFS-17088		RNGL100-11	IND_VAL_CTA_REF_FIN – Indicador do Saldo Final
Considerar o indicador do saldo final da conta referencial recuperada.	MFS-17088		
Registros L200: Método de Avaliação de Estoques 
Campo Chave: REG
Ocorrências: 1:1


CÓD	DESCRIÇÃO	MFS		RNGL200	
Gerar um registro L200 se o campo 7 - COD_QUALIF_PJ do registro 0010 estiver preenchido com ‘01’ e campo 4 - PER_APUR do registro L030 estiver preenchido com “A00” ou “T01...T04” ou se, campo 4-PER_APUR do registro L030 estiver preenchido com “A01...A12” e campo 9 - MÊS_BAL_RED do registro 0010 estiver preenchido com ‘B’.

Este registro não passará pela rotina de processamento, logo a informação a ser gerada no campo RNL200-02 deverá ser recuperada diretamente do parâmetro informado pelo usuário na tela Abertura da apuração de acordo com o detalhamento contido no campo a ser gerado.
	MFS-17088		RNGL200-01	REG – Tipo de Registro

Gerar fixo ‘L200’	MFS-17088		RNL200-02	IND_AVAL_ESTOQ – Método de Avaliação do Estoque Final

Preencher de acordo com a informação do campo ‘Tipo de Método de Avaliação do Estoque’ na tela Abertura da Apuração.

Quando se tratar da do período de apuração = A00 conforme RNGL030 para a geração deste campo, deverá ser recuperado o conteúdo do campo ‘Tipo de Método de Avaliação do Estoque’ informado para a última apuração existente no momento da geração do arquivo.

Se campo estiver preenchido com ‘– Custo Médio Ponderado’, gravar ‘1’;
Se campo estiver preenchido ‘– PEPS (Primeiro que entra, primeiro que sai)’, gravar ‘2’;
Se campo estiver preenchido ‘– Arbitramento - art. 296, Inc. I e II, do RIR/99’, gravar ‘3’;
Se campo estiver preenchido ‘– Custo Específico’, gravar ‘4’.
Se campo estiver preenchido ‘– Valor Realizável Líquido’, gravar ‘5’.
Se campo estiver preenchido ‘– Inventario Periodico’, gravar ‘6’.
Se campo estiver preenchido ‘– Outros’, gravar ‘7’.
Se campo estiver preenchido com “Não há”, gravar ‘8’.


	MFS-17088		
Registros L210: Informativo de Composição de Custos 
Campo Chave: CODIGO
Ocorrências: 0:N

CÓD	DESCRIÇÃO	MFS		RNGL210	Gerar um registro L210 se o campo 7 - COD_QUALIF_PJ do registro 0010 estiver preenchido com ‘01’ e campo 4 - PER_APUR do registro L030 estiver preenchido com “A00” ou “T01...T04” ou se, campo 4-PER_APUR do registro L030 estiver preenchido com “A01...A12” e campo 9 - MÊS_BAL_RED do registro 0010 estiver preenchido com ‘B’.

As informações a serem geradas neste registro terão como base o processamento informado na MTZ_Processamento_em_Lote.docx.
	MFS-17088		RNGL210-01	REG – Tipo de Registro

Gerar fixo ‘L210’	MFS-17088		RNGL210-02	CODIGO – Código da Conta de Custos

Com base no item REGRAS – CÁLCULO (do documento MTZ_Processamento_em_Lote.docx), aplicar a RNC03 exibindo o conteúdo do campo Cód. do Registro conforme tabelas de associação das Tabelas Dinâmicas com Plano Empresa.
	MFS-17088		RNGL210-03	DESCRICAO – Descrição

Exibir o conteúdo do campo Desc. do Registro conforme tabelas de associação das Tabelas Dinâmicas com Plano Empresa para cada Cód. do Registro informado na RNGL210-02.
	MFS-17088		RNGL210-04	VALOR – Valor 

Com base no item REGRAS – CÁLCULO, do documento MTZ_Processamento_em_Lote.docx, aplicar a RNC03 exibindo os valores identificados para cada conteúdo exibido na RNGL210-02.
	MFS-17088		
Registros L300: Demonstração do Resultado do Lucro Líquido Fiscal 
Campo Chave: CÓDIGO
Ocorrência: 0:N


CÓD	DESCRIÇÃO	MFS		RNGL300	Só deve ser geradas informações neste bloco se o campo 04 – PER_APUR do registro L030 estiver preenchido com ‘A00’ ou ‘T01’, ‘T02’, ’T03’,’T04’, ou ‘A01’, ‘A02’, ‘A03’, ‘A04’, ‘A05’, ‘A06’, ‘A07’, ‘A08’, ‘A09’, ‘A10’, ‘A11’, ‘A12’ e se o campo 09 – MÊS_BAL_RED  do registro 0010 estiver preenchido com ‘B’.

As informações a serem geradas neste registro terão como base a tabela resultado do processamento (tela de demonstração do resultado do processamento dos registros) das apurações processadas pelas regras gerais contidas no documento MTZ_Processamento_em_Lote.docx.

Regras de Recuperação: 

Recuperar o saldo final dos registros que foram processados na importação de saldos, através da tabela referencial cujo campo registro seja iniciado com ‘L300’.

	MFS-17088		RNGL300-01	REG – Tipo de Registro

Gerar fixo ‘L300’	MFS-17088		RNGL300-02	CODIGO – Código da Conta Referencial 

Considerar o código da conta referencial do registro recuperado.
	MFS-17088		RNGL300-03	DESCRICAO – Descrição

Considerar a descrição da conta referencial do registro recuperados.
	MFS-17088		RNGL300-04	TIPO – Tipo da Conta

Considerar o campo ‘tipo’ da tabela referencial, da conta referencial recuperada. 
	MFS-17088		RNGL300-05	NIVEL – Nível da Conta

Considerar o campo ‘nível’ da tabela referencial, da conta referencial recuperada. 
	MFS-17088		RNGL300-06	COD_NAT – Natureza da Conta

Considerar o campo ‘natureza’ da tabela referencial, da conta referencial recuperada. 
	MFS-17088		RNGL300-07	COD_CTA_SUP- Código da Conta Superior

Considerar o campo ‘conta superior’ da tabela referencial, da conta referencial recuperada. 
	MFS-17088		RNGL300-08	VALOR_ Valor do Saldo Final da Conta Referencial

Considerar o valor do campo Saldo Final da conta referencial recuperada. 

	MFS-17088		RNGL300-09	IND_VALOR– Indicador do Saldo Final da Conta Referencial

Considerar o indicador do saldo final da conta referencial recuperada.	MFS-17088		

Registros L990: Encerramento do Bloco L
Campo Chave: REG
Ocorrência: 1:1


CÓD	DESCRIÇÃO	MFS		RNGL990-01	REG – Tipo de Registro

Gerar fixo ‘L990’	MFS-17088		RNGL990-02	QTD_LIN – Quantidade Total de Registro do Bloco L

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco L e informar o total.
Considerando que Campo 1: Texto fixo contendo "L990", e campo 2: Quantidade total de linhas do bloco L.

Exemplo: |L990|25|	MFS-17088		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN