# MTZ_Processamento_Geracao_das_Demonstracoes_Contabeis

> Fonte: MTZ_Processamento_Geracao_das_Demonstracoes_Contabeis.doc

THOMSON REUTERS

Processamento das Demonstrações Contábeis (Balanço Patrimonial, Demonstração de Resultado)

Localização: SPED >> ECD – Escrituração Contábil Digital >> Geração >> Demonstrações Contábeis>> Geração SPED


	
Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc27038219" 1.	CONTROLE DE ALTERAÇÕES	 PAGEREF _Toc27038219 \h 3
 HYPERLINK \l "_Toc27038220" 2.	INTRODUÇÃO	 PAGEREF _Toc27038220 \h 4
 HYPERLINK \l "_Toc27038221" 3.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc27038221 \h 4
 HYPERLINK \l "_Toc27038222" 4.	DEFINIÇÃO DAS REGRAS	 PAGEREF _Toc27038222 \h 4


CONTROLE DE ALTERAÇÕES


Data	Demanda	Descrição	Autor		14/10/2019	MFS-31020	Criação do processamento da Geração das Demonstrações Contábeis referente ao Balanço Patrimonial (Registro J100 da ECD)	Alessandra Cristina Navatta		18/10/2019	MFS-31022	Criação do processamento da Geração das Demonstrações Contábeis referente a Demonstração de Resultado (Registro J150 da ECD)	Alessandra Cristina Navatta		11/11/2019	MFS-31025	Criação do processamento da Geração das Demonstrações Contábeis referente a DLPA e DMPL (Registros J210 e J215 da ECD)	Alessandra Cristina Navatta		12/12/2019	MFS-32557	Ajustes nos campos de saldo da DRE (J150)	Alessandra Cristina Navatta		19/05/2021	MFS-64717	Ajustes na geração dos Campos 08 – VL_CTA_INI e 10 – VL_CTA_FIN referente ao Balanço Patrimonial (Registro J100 da ECD) - Saldos por Moeda Funcional.	Rogério Ohashi		27/07/2021	MFS-69607	Tratamento da Regra de Geração dos Registros J005/J100/J150/J210 para considerar o parâmetro “Manter Registros Trimestral e Anual” possibilitando a geração de 5 Períodos, sendo 4 conjuntos de Demonstrações Trimestrais e 1 Anual.	Rogério Ohashi		13/10/2021	MFS-70263	Tratamento da regra de geração dos Registros J005/J100/J150/J210/J215, para  efetuar a limpeza da tabela “SPED_CONT_DEM_CONTAB”, dos dados do centralizador e de seus centralizados, sempre que for efetuada uma nova geração.	Rogério Ohashi		11/05/2022	MFS-85876	Tratamento da Regra de Geração dos Registros J210/J215, que devem ser gerados quando o Saldo Inicial e/ou Final for igual a zero, porém existir movimentação de lançamentos contábeis.	Rogério Ohashi		24/06/2022	MFS-88808	Correção da regra de geração do Registro J150 do período anual, Campo Saldo Final, que deve ser a soma dos Saldos Finais dos períodos Trimestrais.	Rogério Ohashi		04/05/2023	MFS-532288	Readequação da Regra para Geração do arquivo Meio Magnético para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, recuperando o Saldo das Tabelas SAFX02/SAFX226 e SAFX80/SAFX227, da mesma conta contábil para o mesmo período.	Rogério Ohashi		


	 

INTRODUÇÃO 
Criar os processamentos das Demonstrações Contábeis (Balanço Patrimonial, Demonstrações de Resultados, DLPA, DMPL). Essa necessidade surgiu, por conta da reestruturação da ECD, para permitir ao usuário conseguir conferir essas demonstrações, antes da geração do Sped Contábil.

DOCUMENTOS DE REFERÊNCIA
Não se aplica.
DEFINIÇÃO DAS REGRAS


CAMPO	REGRA	DEMANDA		Demonstrações Contábeis – Registro J005
		RNJ005	Regra Geral – Registro J005

[EXCLUÍDA MFS-29278]
O registro J005 somente será gerado se pelo menos um dos parâmetros abaixo estiver marcado na tela de geração do meio magnético:
- Balanço Patrimonial
- Demonstração do Resultado

Obs: Esta regra só deve ser feita a partir da versão 7.00.

[Alteração MFS-29278]:
Recuperar a demonstração de acordo com o campo Período do Arquivo da ECD (tela de Geração das Demonstrações Contábeis). As demonstrações serão recuperadas se o campo do período do arquivo coincidir com o período de geração do meio magnético e o parâmetro Apenas Conferência da tela de geração das demonstrações contábeis, estiver selecionado como ‘Não’. Neste cenário, considerar a informação da geração da demonstração processada. 
[Alteração MFS-35407]
Além das regras de recuperação das demonstrações mencionadas acima, as demonstrações contábeis (bloco J) só devem ser apresentadas no arquivo, se estiverem marcadas no perfil de geração.

No caso do Início de Atividade, o campo “Data Inicio de Atividade” do Cadastro do Estabelecimento que está gerando o arquivo estará preenchido e será uma data contida no ano de geração da obrigação. Neste caso, este campo será gerado com a Data Inicio de Atividade informada no Cadastro do Estabelecimento para o primeiro J005 do arquivo. Para os próximos J005 (se existirem, conforme cenários), considerar os encerramentos do próprio ano de geração.


Observação: A data inicial das demonstrações deve ser a data posterior ao último encerramento do exercício, mesmo que essa data não esteja no período da ECD transmitida. Exemplo: Data do Último Encerramento do Exercício: 31/12/2020 Data Inicial das Demonstrações Contábeis: 01/01/2021.

[ALTERAÇÃO-MFS-69607] Inclusão de Regra para Possibilitar a Geração de 5 períodos (Trimestral e Anual)

Na tela de geração das demonstrações contábeis o sistema deverá verificar a opção ”Manter Registros Trimestral e Anual”, conforme regras abaixo:

Parâmetro Marcado: O sistema deverá manter os registros gravados na tabela “Sped_Cont_Dem_Contab”, compreendidos no período indicado na tela de geração da demonstração contábil.

Caso o parâmetro esteja “marcado” e se tratar da geração Anual , o sistema deverá verificar se os 4 Trimestres foram gerados, caso contrário deverá ser gerado um Log de AVISO: “Foram encontrados somente 'X' Trimestres. O período Anual deverá ser gerado somente após a geração dos 4 Trimestres, favor verificar se confere com a geração Anual/Trimestral.”.

Parâmetro Desmarcado: O sistema deverá limpar os registros gravados na tabela “Sped_Cont_Dem_Contab”, compreendidos no período indicado na tela de geração da demonstração contábil, conforme regra original.
Default: Desmarcado.

Os registros da Apuração Trimestral e Anual gravados na tabela “Sped_Cont_Dem_Contab”, serão gravados no arquivo Meio Magnético da ECD, possibilitando a geração das demonstrações com 5 Períodos, sendo 4 períodos Trimestrais e 1 arquivo Anual, conforme estrutura abaixo:
Balanço Patrimonial

|J005|01012019|31032019|1||  >> (Primeiro Trimestre: Sendo Saldo Inicial = 01/01 e Saldo Final = 31/03)    
|J100|1|T|1||A|ATIVO|35391974,48|D|18707928,37|D||
|J100|1.1|T|2|1|A|CIRCULANTE|33659408|D|16948125,49|D||
|J005|01042019|30062019|1||    >> (Segundo Trimestre: Sendo Saldo Inicial = 01/04 e Saldo Final = 30/06)
|J100|1|T|1||A|ATIVO|18707928,37|D|19227509,78|D||
|J100|1.1|T|2|1|A|CIRCULANTE|16948125,49|D|17323164,39|D||
|J005|01072019|30092019|1||     >> (Terceiro Trimestre: Sendo Saldo Inicial = 01/07 e Saldo Final = 30/09)
|J100|1|T|1||A|ATIVO|19227509,78|D|20233409,69|D||
|J100|1.1|T|2|1|A|CIRCULANTE|17323164,39|D|18596031,19|D||
|J005|01102019|31122019|1||    >> (--Quarto Trimestre: Sendo Saldo Inicial = 01/10 e Saldo Final = 31/12)
|J100|1|T|1||A|ATIVO|20233409,69|D|20760851,73|D||
|J100|1.1|T|2|1|A|CIRCULANTE|18596031,19|D|18309503,04|D||
|J005|01012019|31122019|1||     >> (Anual: Sendo Saldo Inicial = 01/01 e Saldo Final = 31/12)
|J100|1|T|1||A|ATIVO|35391974,48|D|20760851,73|D||
|J100|1.1|T|2|1|A|CIRCULANTE|33659408|D|18309503,04|D||

DRE

|J005|01012021|31032021|1|| >> (Primeiro Trimestre: Sendo Saldo Inicial = 01/01 e Saldo Final = 31/03)   |J150|0003|3.1.1|D|3||DESPESA 3.1.1|2000,00|D|1000,00|D|D||
|J005|01042021|30062021|1|| >> (Segundo Trimestre: Sendo Saldo Inicial = 01/04 e Saldo Final = 30/06)
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|1000,00|D|1000,00|D|D||
|J005|01072021|30092021|1|| >> (Terceiro Trimestre: Sendo Saldo Inicial = 01/07 e Saldo Final = 30/09)
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|1000,00|D|1000,00|D|D||
|J005|01102021|31122021|1|| >> (Quarto Trimestre: Sendo Saldo Inicial = 01/10 e Saldo Final = 31/12)
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|1000,00|D|1000,00|D|D||
|J005|01012021|31122021|1|| >> (Anual: Sendo Saldo Inicial = 01/01 e Saldo Final = Deverá ser a soma dos 4 Trimestres, conforme regra de validação do PVA) - Antes do Encerramento
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|2000,00|D|4000,00|D|D||

Observações: Apuração Trimestral do IRPJ: Respeitados os limites acima descritos, ainda que a apuração do IRPJ seja trimestral, o livro pode ser anual. A legislação do IRPJ obriga a elaboração e transcrição das demonstrações na data do fato gerador do tributo. Nada impede que, no mesmo livro, exista quatro conjuntos de demonstrações trimestrais e a anual.


[ALTERAÇÃO- MFS-70263] Limpeza registros gerados de Estabelecimentos Centralizador e Centralizados

Tratamento:

Sempre que for executado uma nova geração e se tratar de um estabelecimento centralizador, deve ser efetuar a limpeza da tabela “SPED_CONT_DEM_CONTAB”, dos dados do centralizador e de seus centralizados, dos Registros J005 e Registros Filhos (J100/J150/J210/J215).

	MFS-26093
MFS-29278
MFS-35407		

Campo	Regra	Demanda		Balanço Patrimonial – Registro J100		RPB00	[ALTERAÇÃO-MFS-69607] Inclusão de Regra para Possibilitar a Geração de 5 períodos (Trimestral e Anual)

Na tela de geração das demonstrações contábeis o sistema deverá verificar a opção ”Manter Registros Trimestral e Anual”, conforme regras abaixo:

Parâmetro Marcado: O sistema deverá manter os registros gravados na tabela “Sped_Cont_Dem_Contab”, compreendidos no período indicado na tela de geração da demonstração contábil.

Caso o parâmetro esteja “marcado” e se tratar da geração Anual , o sistema deverá verificar se os 4 Trimestres foram gerados, caso contrário deverá ser gerado um Log de AVISO: “Foram encontrados somente 'X' Trimestres. O período Anual deverá ser gerado somente após a geração dos 4 Trimestres, favor verificar se confere com a geração Anual/Trimestral.”.

Parâmetro Desmarcado: O sistema deverá limpar os registros gravados na tabela “Sped_Cont_Dem_Contab”, compreendidos no período indicado na tela de geração da demonstração contábil, conforme regra original.

Default: Desmarcado.

Os registros da Apuração Trimestral e Anual gravados na tabela “Sped_Cont_Dem_Contab”, serão gravados no arquivo Meio Magnético da ECD, possibilitando a geração das demonstrações com 5 Períodos, sendo 4 períodos Trimestrais e 1 arquivo Anual, seguindo com a mesma estrutura especificada na regra de Geração do Registro J005 (RNJ005)

Observações: Apuração Trimestral do IRPJ: Respeitados os limites acima descritos, ainda que a apuração do IRPJ seja trimestral, o livro pode ser anual. A legislação do IRPJ obriga a elaboração e transcrição das demonstrações na data do fato gerador do tributo. Nada impede que, no mesmo livro, exista quatro conjuntos de demonstrações trimestrais e a anual.

Premissa geração do Registro J100

No meu de Dados Iniciais na Aba de Demonstrações Contábeis a Indicação das Demonstrações deverá ser igual Tipo 1.
	MFS-31020
MFS-69607		RPB01	REG
Quando na tela da Geração das Demonstrações Contábeis (Localização: MastersafDW >> SPED >> ECD – Escrituração Contábil Digital >> Geração >> Demonstrações Contábeis>> Geração) for selecionada a opção “Balanço Patrimonial”, gerar o texto fixo J100.
	MFS-31020		RPB02
	DATA INICIAL

Preencher com a data inicial indicada na tela da geração das demonstrações contábeis.
	MFS-31020		RPB03	 DATA FINAL

Preencher com a data Final indicada na tela da geração das demonstrações contábeis.
	MFS-31020		RPB04	ORDEM

Nesse campo o sistema preenche com o número de ordem campo 04 da SAFX2102, (exibir a informação em ordem crescente).
	MFS-31020		RPB05	COD_AGL

Nesse campo o sistema preenche com o código da conta aglutinadora campo 03 da SAFX2102. 
	MFS-31020		RPB06	IND_COD_AGL

Nesse campo o sistema preenche com o tipo do código de aglutinação das linhas. As opções válidas são:

‘T’ – Totalizador (nível que totaliza um ou mais níveis inferiores da demonstração financeira).
‘D’ – Detalhe (nível mais detalhado da demonstração financeira).

Regras:
Se o código de aglutinação for classificado como “1 - Ativo” ou “2 – Passivo ou Patrimônio Líquido” campo 07 da SAFX2102, esse indicador é preenchido com a opção “D”.
Se o código de aglutinação for classificado como “3 - Subtotalizador/Totalizador do Ativo” ou “4 - Subtotalizador/Totalizador do Passivo ou PL” campo 07 da SAFX2102, esse indicador é preenchido com a opção “T”.

	MFS-31020		RPB07	NIVEL_AGL

Neste campo o sistema preenche com o nivel da conta aglutinadora, indicada no campo “nível” da SAFX2102	MFS-31020		RPB08	COD_AGL_SUP
Nesse campo o sistema preenche com o código de aglutinação sintético/grupo de código de aglutinação de nível superior. 

Regras:
Verificar os códigos de aglutinação parametrizados no campo 10 - EXPRESSAO_ORD que são totalizadores, ou seja, opções “3 - Subtotalizador/Totalizador do Ativo” ou “4 - Subtotalizador/Totalizador do Passivo ou PL” campo 07 da tabela SAFX2102 para buscar e preencher com a conta de nível superior “Conta Mãe”.
Exemplo:
	MFS-31020		RPB09	IND_GRP_BAL

Nesse campo o sistema preenche com o indicador de grupo do balanço campo 07 da SAFX2102. 
‘1’ – Ativo
‘2’ – Passivo e Patrimônio Líquido
‘3’ – Subtotalizador/Totalizador do Ativo
‘4’ – Subtotalizador/Totalizador do Passivo ou PL

	MFS-31020		RPB10	DESCR_COD_AGL

Nesse campo o sistema preenche com a descrição da conta aglutinadora campo 05 da SAFX2102. 	MFS-31020		RPB11	VL_CTA_INI (Moeda Corrente)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Inicial das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_INI será obtido com base no resultado gerado no campo VL_CTA_INI. 

Estas informações necessárias para o cálculo serão obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J100, recuperando as informações de Saldos das tabelas SAFX02/SAFX102 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J100 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

	


MFS-31020
MFS-532288		RPB12	IND_DC_CTA_INI(Moeda Corrente)

Neste campo o sistema preenche com o indicador do saldo inicial das contas contábeis que foram sumarizados na conta aglutinadora (Campo 6 da SAFX02/ Campo 7 da SAFX80), conforme cálculo  no campo indicado no campo  VL_CTA_INI.
	MFS-31020		RPB13	VL_CTA_FIN (Moeda Corrente)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Final das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data final indicada na tela de geração das demonstrações.

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_FIN será obtido com base no resultado gerado no campo VL_CTA_FIN. 

Estas informações necessárias para o cálculo serão obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J100, recuperando as informações de Saldos das tabelas SAFX02/SAFX102 e SAFX80, considerando a mesma Conta Contábil e período.


Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J100 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

	


MFS-31020
MFS-532288		RPB14	IND_DC_CTA_FIN (Moeda Corrente)

Neste campo o sistema preenche com o indicador do saldo final das contas contábeis que foram sumarizados na conta aglutinadora (Campo8 da SAFX02/ Campo 11 da SAFX80), conforme cálculo  no campo indicado no campo  VL_CTA_FIN.
	MFS-31020		RPB15	VL_CTA_INI (Moeda Funcional)

[ALTERAÇÃO- MFS-64717] Tratamento na geração dos valores de Saldos por Moeda Funcional

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Tratamento:

O sistema deverá considerar os Saldos por Moeda funcional quando o campo “IND_MOEDA_FUNC” da tabela “SPED_DADOS_INI” for igual a “S”.


Observação: Este campo será preenchido conforme parâmetro na tela de Dados Iniciais no caminho: SPED >> ECD - Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais>> ECD com Movimentação em Moeda Funcional.


Os valores que irão compor este campo serão obtidos com base no valor do Saldo Inicial das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_INI será obtido com base no resultado gerado no campo VL_CTA_INI. 

Estas informações necessárias para o cálculo serão obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.


[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.


	MFS-31020
MFS-64717
MFS-532288		Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J100, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J100 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

		RPB16	IND_DC_CTA_INI(Moeda Funcional)

Neste campo o sistema preenche com o indicador do saldo inicial das contas contábeis que foram sumarizados na conta aglutinadora (Campo 6 da SAFX226/ Campo 7 da SAFX227), conforme cálculo  no campo indicado no campo  VL_CTA_INI.
	MFS-31020		RPB17	VL_CTA_FIN (Moeda Funcional)

[ALTERAÇÃO- MFS-64717] Tratamento na geração dos valores de Saldos por Moeda Funcional

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Tratamento:

O sistema deverá considerar os Saldos por Moeda funcional quando o campo “IND_MOEDA_FUNC” da tabela “SPED_DADOS_INI” for igual a “S”.


Observação: Este campo será preenchido conforme parâmetro na tela de Dados Iniciais no caminho: SPED >> ECD - Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais>> ECD com Movimentação em Moeda Funcional.

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Final das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data final indicada na tela de geração das demonstrações.

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_FIN será obtido com base no resultado gerado no campo VL_CTA_FIN. 

Estas informações necessárias para o cálculo serão obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.


	MFS-31020
MFS-64717		Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J100, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J100 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
		RPB18	IND_DC_CTA_FIN(Moeda Funcional)

Neste campo o sistema preenche com o indicador do saldo final das contas contábeis que foram sumarizados na conta aglutinadora (Campo 8 da SAFX226/ Campo 9 da SAFX227), conforme cálculo  no campo indicado no campo  VL_CTA_FIN.
	MFS-31020		RPB19	CONTA_CONTABIL

Nesse campo o sistema preenche com o código da conta contábil, campo 01 da SAFX2002. Apresentar a conta contábil, logo abaixo da respectiva conta de aglutinação.
	MFS-31020		RPB20	DESCRICAO_CONTA_CONTABIL

Nesse campo o sistema preenche com a descrição da conta contábil campo 03 da SAFX2002. 
	MFS-31020		RPB21	VL_CTA_CONTABIL_INI (Moeda Corrente)

Neste campo o Sistema deve apresentar o saldo Inicial de cada Conta Contábil associada ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Estas informações são obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.
	MFS-31020		RPB22	IND_DC_CTA_CONTABIL_INI (Moeda Corrente)

Neste campo o Sistema deve apresentar o indicador de saldo inicial de cada Conta Contábil associada ao código de aglutinação.	MFS-31020		RPB23	VL_CTA_CONTABIL_FIN (Moeda Corrente)


Para Informações de Origem diferente de SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ desmarcado na tela de Dados Iniciais)

Considerar como origem somente a tabela SAFX01 - Arquivo Contábil somente registros que tenham o Tipo de Lançamento igual a E – Encerramento (para cada conta contábil).

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”.

Para Informações de Origem SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ marcado na tela de Dados Iniciais)

 O sistema deverá recuperar as informações da tabela SAFX169 – Saldo Antes do Encerramento para compor o registro, ou seja, considerando cada conta e centro de custo para o qual houve movimento.
	MFS-31020		RPB24	IND_DC_CTA_CONTABIL_FIN (Moeda Corrente)

Neste campo o Sistema deve apresentar o indicador do lançamento de encerramento de cada Conta Contábil associada ao código de aglutinação.	MFS-31020		RPB25	VL_CTA_CONTABIL_INI (Moeda Funcional)

Neste campo o Sistema deve apresentar o saldo Inicial de cada Conta Contábil associada ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Estas informações são obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.
	MFS-31020		RPB26	IND_DC_CTA_CONTABIL_INI(Moeda Funcional)

Neste campo o Sistema deve apresentar o indicador de saldo inicial de cada Conta Contábil associada ao código de aglutinação.	MFS-31020		RPB27	VL_CTA_CONTABIL_FIN (Moeda Funcional)


Para Informações de Origem diferente de SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ desmarcado na tela de Dados Iniciais)

Considerar como origem somente a tabela SAFX225 – Lançamento Contábil em Moeda Funcional somente registros que tenham o Tipo de Lançamento igual a E – Encerramento.

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”.

Para Informações de Origem SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ marcado na tela de Dados Iniciais)

 O sistema deverá recuperar as informações da tabela SAFX232 – Saldo Antes do Encerramento em Moeda Funcional para compor o registro, ou seja, considerando cada conta e centro de custo para o qual houve movimento.


	MFS-31020		RPB28	IND_DC_CTA_CONTABIL_FIN(Moeda Funcional)

Neste campo o Sistema deve apresentar o indicador do lançamento de encerramento de cada Conta Contábil associada ao código de aglutinação.	MFS-31020		RPB29	NOTA_EXP_REF

Neste campo o sistema preenche com a informação do campo  6 – NOTA_EXP_ REF da SAFX257, quando o IND_BALANCO_DRE = ‘B’ e estiver associados ao código de aglutinação selecionada. O período de referência para seleção dos registros é o mês e ano das datas indicadas na geração da demonstração que devem estar compreendidos na DAT_DEMONSTRACAO da tabela SAFX257 (considerar a data mais atual, limitado ao final do período de geração da demonstração).	MFS-31020		
Demonstração de Resultado – Registro J150		RPD00	Deverá ser gerada uma demonstração de resultado se:

Na tela de geração das demonstrações contábeis se for marcada a opção Demonstração de Resultado, será considerada a parametrização da tela de Códigos de Aglutinação (B. Patrimonial/D.Resultado/DLPA/DMPL), aba D.Resultado (campo 6 – Indicador de Aglutinação (IND_BALANCO_DRE) da SAFX2102, igual a “D”), para o estabelecimento que está sendo considerado na geração.

Nesta demonstração, apenas contas com naturezas com indicador igual a 3 - Despesa, 4 - Receita, 8 - Custo ou 9 – Outros serão aceitas.

Serão considerados os valores dos saldos contábeis (SAFX02 ,  SAFX80, SAFX226 ou SAFX227), das contas indicadas nas contas aglutinadoras (SAFX2103), compreendidos no período indicado na tela de geração da demonstração contábil. Ou os lançamentos de encerramento (SAFX01, SAFX169,SAFX225 ou SAFX232)

Para o cálculo serão obtidas as informações da SAFX02 ou SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, consideraremos as informações da SAFX80 ou SAFX227. Na seleção da SAFX80/SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

Para recuperar as informações dos Saldos Contábeis, caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil” estiver mercado, o sistema deverá recuperar os valores das tabelas SAFX02/SAFX226 e SAFX80/SAFX227 da mesma conta contábil e período, caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” estiver desmarcado, caso contrário  o cálculo serão obtidas somente das informações da SAFX02/SAFX226.

Em todo o processamento, serão geradas as visões Sintética (nível de contas aglutinadoras) e também a Analítica (nível de contas contábeis) e as informações de moeda corrente e moeda funcional.


Atenção: Não será mais utilizado as informações dos registros I350 para definirmos a periodicidade das demonstrações. Serão consideradas as datas indicadas na tela de Geração das Demonstrações Contábeis. (desta forma será de responsabilidade do cliente indicar a periodicidade que o estabelecimento se enquadra).


Validações Adicionais:

Se a parametrização for encontrada, porém não existir nenhuma conta com saldo para o período, exibir a mensagem na aba de log: A Demonstração de Resultado não será gerada, pois não foi encontrado saldos contábeis para o período. Estabelecimento: XXXX.

Premissa geração do Registro J150

No meu de Dados Iniciais na Aba de Demonstrações Contábeis a Indicação das Demonstrações deverá ser igual Tipo 1.


	MFS-31022
MFS-532288		RPD00.a	[ALTERAÇÃO-MFS-69607] Inclusão de Regra para Possibilitar a Geração de 5 períodos (Trimestral e Anual)

Na tela de geração das demonstrações contábeis o sistema deverá verificar a opção ”Manter Registros Trimestral e Anual”, conforme regras abaixo:

Parâmetro Marcado: O sistema deverá manter os registros gravados na tabela “Sped_Cont_Dem_Contab”, compreendidos no período indicado na tela de geração da demonstração contábil.

[MFS88808] Tratamento Saldo Final no arquivo do período Anual

Se a geração das Demonstrações for referente ao período Anual e Registro J150, o sistema deverá considerar a soma do Saldo Final dos 4 períodos Trimestrais, sendo:
 O Campo “vlr_saldo_calc” da tabela “sped_cont_dem_contab” do período Anual deverá ser a soma do Campo “vlr_saldo_calc” da tabela “sped_cont_dem_contab” dos 4 períodos Trimestrais, conforme exemplo abaixo:

|J005|01012021|31032021|1|| >> Primeiro Trimestre
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|2000,00|D|1000,00|D|D||
|J005|01042021|30062021|1|| >> Segundo Trimestre
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|1000,00|D|1000,00|D|D||
|J005|01072021|30092021|1|| >> Terceiro Trimestre
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|1000,00|D|1000,00|D|D||
|J005|01102021|31122021|1|| >> Quarto Trimestre
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|1000,00|D|1000,00|D|D||
|J005|01012021|31122021|1|| >> Anual: O Saldo Final = Deverá ser a soma do Saldo Final dos 4 períodos Trimestrais, conforme regra de validação do PVA) - Antes do Encerramento
|J150|0003|3.1.1|D|3||DESPESA 3.1.1|2000,00|D|4000,00|D|D||

Caso o parâmetro esteja “marcado” e se tratar da geração Anual , o sistema deverá verificar se os 4 Trimestres foram gerados, caso contrário deverá ser gerado um Log de AVISO: “Foram encontrados somente 'X' Trimestres. O período Anual deverá ser gerado somente após a geração dos 4 Trimestres, favor verificar se confere com a geração Anual/Trimestral.”.

Parâmetro Desmarcado: O sistema deverá limpar os registros gravados na tabela “Sped_Cont_Dem_Contab”, compreendidos no período indicado na tela de geração da demonstração contábil, conforme regra original.
Default: Desmarcado.

Os registros da Apuração Trimestral e Anual gravados na tabela “Sped_Cont_Dem_Contab”, serão gravados no arquivo Meio Magnético da ECD, possibilitando a geração das demonstrações com 5 Períodos, sendo 4 períodos Trimestrais e 1 arquivo Anual, seguindo com a mesma estrutura especificada na regra de Geração do Registro J005 (RNJ005)

Observações: Apuração Trimestral do IRPJ: Respeitados os limites acima descritos, ainda que a apuração do IRPJ seja trimestral, o livro pode ser anual. A legislação do IRPJ obriga a elaboração e transcrição das demonstrações na data do fato gerador do tributo. Nada impede que, no mesmo livro, exista quatro conjuntos de demonstrações trimestrais e a anual. No caso do Registro J150, o Saldo Final deverá ser a soma do Saldo Final de cada período, conforme regra de validação do PVA.	

MFS-69607
MFS-88808		RPD01	REG
Quando na tela da Geração das Demonstrações Contábeis (Localização: MastersafDW >> SPED >> ECD – Escrituração Contábil Digital >> Geração >> Demonstrações Contábeis>> Geração) for selecionada a opção “Demonstração de Resultado”, gerar o texto fixo J150.	MFS-31022		RPD02	DATA INICIAL

Preencher com a data inicial indicada na tela da geração das demonstrações contábeis.	MFS-31022		RPD03	 DATA FINAL

Preencher com a data Final indicada na tela da geração das demonstrações contábeis.	MFS-31022		RPD04	ORDEM

Nesse campo o sistema preenche com o número de ordem campo 04 da SAFX2102, (exibir a informação em ordem crescente).	MFS-31022		RPD05	COD_AGL

Nesse campo o sistema preenche com o código da conta aglutinadora campo 03 da SAFX2102.	MFS-31022		RPD06	IND_COD_AGL

Nesse campo o sistema preenche com o tipo do código de aglutinação das linhas. As opções válidas são:

‘T’ – Totalizador (nível que totaliza um ou mais níveis inferiores da demonstração financeira).
‘D’ – Detalhe (nível mais detalhado da demonstração financeira)

Regras:
Se o código de aglutinação for classificado como “1 – Receita/Despesa” ou “3 - Receita” ou “4 - Despesa” campo 08 da SAFX2102, esse campo é preenchido com a opção “D”.
Se o código de aglutinação for classificado como “2 - Subtotalizador/Totalizador da DRE” ou “5 - Subtotalizador/Totalizador de Receita” ou “6 - Subtotalizador/Totalizador de Despesa” campo 08 da SAFX2102, esse campo é preenchido com a opção “T”.	MFS-31022		RPD07	NIVEL_AGL

Neste campo o sistema preenche com o nivel da conta aglutinadora, indicada no campo “nível” da SAFX2102	MFS-31022		RPD08	COD_AGL_SUP

Nesse campo o sistema preenche com o código de aglutinação sintético/grupo de código de aglutinação de nível superior. 

Regras:
Verificar os códigos de aglutinação parametrizados no campo 10 - EXPRESSAO_ORD que são totalizadores, ou seja, opções “2 - Subtotalizador/Totalizador da DRE” ou “5 - Subtotalizador/Totalizador de Receita” ou “6 - Subtotalizador/Totalizador de Despesa” campo 08 da tabela SAFX2102 para buscar e preencher com a conta de nível superior “Conta Mãe”.

Exemplo: 
 EMBED PBrush  
	MFS-31022		RPD09	DESCR_COD_AGL

Nesse campo o sistema preenche com a descrição da conta aglutinadora campo 05 da SAFX2102. 	MFS-31022		RPD10	VL_CTA_INI (Moeda Corrente)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Se o período inicial da geração do arquivo for um dia a mais que o período indicado no campo ‘dia e mês do encerramento do exercício social’, na tela de Dados Iniciais:

Considerar para recuperação o saldo final do período indicado como encerramento social.

Para os demais períodos do exercício: 

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Inicial das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_INI será obtido com base no resultado gerado no campo VL_CTA_INI. Se o resultado do cálculo for positivo ou zero, gerar o indicador “C”. Se for negativo, gerar o indicador “D”.

Estas informações necessárias para o cálculo serão obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

	MFS-31022
MFS-32557		RPD11	[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J150, recuperando as informações de Saldos das tabelas SAFX02 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J150 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

IND_DC_CTA_INI (Moeda Corrente)

Nesse campo o sistema preenche com o indicador da situação do valor total do código de aglutinação. 

As opções válidas são:
D – Devedor;
C – Credor; 

Regras:
O sistema verifica qual o indicador dos saldos das 2 parcelas:
Se as parcelas são iguais (Débito com Débito, o sistema preenche com “D” ou Crédito com Crédito preenche com “C”), somam-se ou subtraem-se os saldos conforme o operador da expressão. O indicador de débito e crédito final é igual ao das parcelas.

Se as parcelas são diferentes (Débito com Crédito), não importando se a expressão indica soma ou subtração, subtraem-se os valores e o indicador final é o da parcela de maior saldo.
Exemplo: 
Se o saldo da parcela de Débito for > que a parcela do Crédito, o sistema preenche com o indicador “D” para essa aglutinação. Senão preenche com “C”.	MFS-31022
MFS-32557
MFS-532288		RPD12	VL_CTA_FIN (Moeda Corrente)


Para Informações de Origem diferente de SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ desmarcado na tela de Dados Iniciais)

Considerar como origem somente a tabela SAFX01 - Arquivo Contábil somente registros que tenham o Tipo de Lançamento igual a E – Encerramento.

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”.

Para Informações de Origem SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ marcado na tela de Dados Iniciais)

 O sistema deverá recuperar as informações da tabela SAFX169 – Saldo Antes do Encerramento para compor o registro, ou seja, considerando cada conta e centro de custo para o qual houve movimento.

Caso não se tratar de um período de encerramento (não houver SAFX01 - Tipo de Lançamento igual a E) neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Final das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data final indicada na tela de geração das demonstrações.

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_FIN será obtido com base no resultado gerado no campo VL_CTA_FIN. 

Estas informações necessárias para o cálculo serão obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

	MFS-31022
MFS-32557
MFS-532288		[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J150, recuperando as informações de Saldos das tabelas SAFX02 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J150 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
		RPD13	
IND_DC_CTA_FIN (Moeda Corrente)

Nesse campo o sistema preenche com o indicador da situação do valor total do código de aglutinação. 

As opções válidas são:
D – Devedor;
C – Credor; 

Regras:
O sistema verifica qual o indicador dos lançamentos:
Se as parcelas são iguais (Débito com Débito, o sistema preenche com “D” ou Crédito com Crédito preenche com “C”), somam-se ou subtraem-se os saldos conforme o operador da expressão. O indicador de débito e crédito final é igual ao das parcelas.

Se as parcelas são diferentes (Débito com Crédito), não importando se a expressão indica soma ou subtração, subtraem-se os valores e o indicador final é o da parcela de maior saldo.
Exemplo: 
Se o saldo da parcela de Débito for > que a parcela do Crédito, o sistema preenche com o indicador “D” para essa aglutinação. Senão preenche com “C”.	MFS-31022
MFS-32557
		RPD14	VL_CTA_INI (Moeda Funcional)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:


Se o período inicial da geração do arquivo for um dia a mais que o período indicado no campo ‘dia e mês do encerramento do exercício social’, na tela de Dados Iniciais:

Considerar para recuperação o saldo final do período indicado como encerramento social.

Para os demais períodos do exercício: 

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Inicial das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_INI será obtido com base no resultado gerado no campo VL_CTA_INI. Se o resultado do cálculo for positivo ou zero, gerar o indicador “C”. Se for negativo, gerar o indicador “D”.

Estas informações necessárias para o cálculo serão obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.


	MFS-31022
MFS-32557		[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J150, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J150 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
		RPD15	IND_DC_CTA_INI (Moeda Funcional)

Neste campo o sistema preenche com o indicador do saldo inicial das contas contábeis que foram sumarizados na conta aglutinadora , conforme cálculo  no campo indicado no campo  VL_CTA_INI.
	MFS-31022
MFS-32557		RPD16	VL_CTA_FIN (Moeda Funcional)

Para Informações de Origem diferente de SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ desmarcado na tela de Dados Iniciais)

Considerar como origem somente a tabela SAFX225 – Lançamento Contábil em Moeda Funcional somente registros que tenham o Tipo de Lançamento igual a E – Encerramento.

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”.

Para Informações de Origem SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ marcado na tela de Dados Iniciais)

 O sistema deverá recuperar as informações da tabela SAFX232 – Saldo Antes do Encerramento em Moeda Funcional para compor o registro, ou seja, considerando cada conta e centro de custo para o qual houve movimento.

	MFS-31022
MFS-32557		RPD17	IND_DC_CTA_FIN (Moeda Funcional)

Neste campo o sistema preenche com o indicador do lançamento de encerramento das contas contábeis que foram sumarizados na conta aglutinadora, conforme cálculo  no campo indicado no campo  VL_CTA_FIN.
	MFS-31022
MFS-32557		RPD18	CONTA_CONTABIL

Nesse campo o sistema preenche com o código da conta contábil, campo 01 da SAFX2002. Apresentar a conta contábil, logo abaixo da respectiva conta de aglutinação.
	MFS-31022		RPD19	DESCRICAO_CONTA_CONTABIL

Nesse campo o sistema preenche com a descrição da conta contábil campo 03 da SAFX2002. 
	MFS-31022		RPD20	VL_CTA_CONTABIL_INI (Moeda Corrente)

Se o período inicial da geração do arquivo for um dia a mais que o período indicado no campo ‘dia e mês do encerramento do exercício social’, na tela de Dados Iniciais:

Considerar para recuperação o saldo final do período indicado como encerramento social.

Para os demais períodos do exercício: 


Neste campo o Sistema deve apresentar o Saldo Inicial de cada Conta Contábil associada ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Estas informações são obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J150, recuperando as informações de Saldos das tabelas SAFX02 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J150 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

	MFS-31022
MFS-32557
MFS-532288		RPD21	IND_DC_CTA_CONTABIL_INI (Moeda Corrente)

Neste campo o Sistema deve apresentar o indicador de saldo inicial de cada Conta Contábil associada ao código de aglutinação 	MFS-31022
MFS-32557		RPD22	VL_CTA_CONTABIL_FIN (Moeda Corrente)

 Para Informações de Origem diferente de SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ desmarcado na tela de Dados Iniciais)

Considerar como origem somente a tabela SAFX01 - Arquivo Contábil somente registros que tenham o Tipo de Lançamento igual a E – Encerramento (para cada conta contábil).

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”.

Para Informações de Origem SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ marcado na tela de Dados Iniciais)

 O sistema deverá recuperar as informações da tabela SAFX169 – Saldo Antes do Encerramento para compor o registro, ou seja, considerando cada conta e centro de custo para o qual houve movimento.
	MFS-31022
MFS-32557		RPD23	IND_DC_CTA_CONTABIL_FIN (Moeda Corrente)

Neste campo o Sistema deve apresentar o indicador de saldo final de cada Conta Contábil associada ao código de aglutinação 	MFS-31022
MFS-32557		RPD24	VL_CTA_CONTABIL_INI (Moeda Funcional)


Se o período inicial da geração do arquivo for um dia a mais que o período indicado no campo ‘dia e mês do encerramento do exercício social’, na tela de Dados Iniciais:

Considerar para recuperação o saldo final do período indicado como encerramento social.

Para os demais períodos do exercício: 


Considerar para recuperação o saldo final do período indicado como encerramento social.

Neste campo o Sistema deve apresentar o Saldo Inicial de cada Conta Contábil associada ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Estas informações são obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J150, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J150 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

	MFS-31022
MFS-32557
MFS-532288		RPD25	IND_DC_CTA_CONTABIL_INI (Moeda Funcional)

Neste campo o Sistema deve apresentar o indicador de saldo inicial de cada Conta Contábil associada ao código de aglutinação.	MFS-31022
MFS-32557		RPD26	VL_CTA_CONTABIL_FIN (Moeda Funcional)

Para Informações de Origem diferente de SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ desmarcado na tela de Dados Iniciais)

Considerar como origem somente a tabela SAFX225 – Lançamento Contábil em Moeda Funcional somente registros que tenham o Tipo de Lançamento igual a E – Encerramento (cada conta contábil).

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”.

Para Informações de Origem SAFX169 (campo ‘Saldo Antes do Encerramento (SAFX169)’ marcado na tela de Dados Iniciais)

 O sistema deverá recuperar as informações da tabela SAFX232 – Saldo Antes do Encerramento em Moeda Funcional para compor o registro, ou seja, considerando cada conta e centro de custo para o qual houve movimento.
	MFS-31022
MFS-32557		RPD27	IND_DC_CTA_CONTABIL_FIN (Moeda Funcional)

Neste campo o Sistema deve apresentar o indicador de lançamento de encerramento de cada Conta Contábil associada ao código de aglutinação.	MFS-31022
MFS-32557		RPD28	IND_GRP_DRE

Nesse campo o sistema preenche com o indicador de grupo da DRE, as opções válidas são:
‘D’ – Linha totalizadora ou de detalhe da demonstração que, por sua natureza de despesa represente redução do lucro. 
‘R’ – Linha totalizadora ou de detalhe da demonstração que, por sua natureza de receita represente incremento do lucro. 

O preenchimento do indicador de grupo da DRE é baseado nas opções válidas do campo 08 da SAFX2102. 
‘1’ – Receita/Despesa
‘2’ – Subtotalizador/ Totalizador da DRE
‘3’ – Receita (novo)
‘4’ – Despesa (novo)
‘5’ – Subtotalizador/ Totalizador de Receita (novo)
‘6’ – Subtotalizador/ Totalizador de Despesa (novo)

Regras para geração do indicador:

Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘1’ ou ‘2’, o sistema deve verificar se a conta é Credora ou Devedora através do indicador IND_DC_CTA.

Se a aglutinação for “Devedora”, o IND_GRP_DRE é preenchido com ‘D’
Se a aglutinação for “Credora”, o IND_GRP_DRE é preenchido com ‘R’


Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘4’ ou ‘6’, esse campo será preenchido com o valor ‘D’.

Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘3’ ou ‘5’, esse campo será preenchido com o valor ‘R’.	MFS-31022		RPD29	NOTA_EXP_REF

Neste campo o sistema preenche com a informação do campo  6 – NOTA_EXP_ REF da SAFX257, quando o IND_BALANCO_DRE = ‘D’ e estiver associados ao código de aglutinação selecionada. O período de referência para seleção dos registros é o mês e ano das datas indicadas na geração da demonstração que devem estar compreendidos na DAT_DEMONSTRACAO da tabela SAFX257 (considerar a data mais atual, limitado ao final do período de geração da demonstração).	MFS-31022		Registro J210: DLPA – Demonstração de Lucros ou Prejuízos Acumulados/DMPL – Demonstração de Mutações do Patrimônio Líquido		RP00.0	Deverá ser gerada uma demonstração de resultado se:

Na tela de geração das demonstrações contábeis se for marcada a opção Demonstração de Resultado, será considerada a parametrização da tela de Códigos de Aglutinação (B. Patrimonial/D.Resultado/DLPA/DMPL), aba DLPA(campo 6 – Indicador de Aglutinação (IND_BALANCO_DRE) da SAFX2102, igual a “L”), para o estabelecimento que está sendo considerado na geração.

Serão considerados os valores dos saldos contábeis (SAFX02, SAFX80, SAFX226 ou SAFX227), das contas indicadas nas contas aglutinadoras (SAFX2103), compreendidos no período indicado na tela de geração da demonstração contábil. 

Para o cálculo serão obtidas as informações da SAFX02 ou SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, consideraremos as informações da SAFX80 ou SAFX227. Na seleção da SAFX80 ou SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

Para recuperar as informações dos Saldos Contábeis, caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil” estiver mercado, o sistema deverá recuperar os valores das tabelas SAFX02/SAFX226 e SAFX80/SAFX227 da mesma conta contábil e período, caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” estiver desmarcado, caso contrário  o cálculo serão obtidas somente das informações da SAFX02/SAFX226.

Em todo o processamento, serão geradas as visões Sintética (nível de contas aglutinadoras) e também a Analítica (nível de contas contábeis) e as informações de moeda corrente e moeda funcional.

Atenção: Não será mais utilizado as informações dos registros I350 para definirmos a periodicidade das demonstrações. Serão consideradas as datas indicadas na tela de Geração das Demonstrações Contábeis. (desta forma será de responsabilidade do cliente indicar a periodicidade que o estabelecimento se enquadra).

Validações Adicionais:

Se a parametrização for encontrada, porém não existir nenhuma conta com saldo para o período, exibir a mensagem na aba de log: A Demonstração de DLPA não será gerada, pois não foi encontrado saldos contábeis para o período. Estabelecimento: XXXX.	MFS-31025
MFS-532288		RP00.0.a	[ALTERAÇÃO-MFS-69607] Inclusão de Regra para Possibilitar a Geração de 5 períodos (Trimestral e Anual)

Na tela de geração das demonstrações contábeis o sistema deverá verificar a opção ”Manter Registros Trimestral e Anual”, conforme regras abaixo:

Parâmetro Marcado: O sistema deverá manter os registros gravados na tabela “Sped_Cont_Dem_Contab”, compreendidos no período indicado na tela de geração da demonstração contábil.

Caso o parâmetro esteja “marcado” e se tratar da geração Anual , o sistema deverá verificar se os 4 Trimestres foram gerados, caso contrário deverá ser gerado um Log de AVISO: “Foram encontrados somente 'X' Trimestres. O período Anual deverá ser gerado somente após a geração dos 4 Trimestres, favor verificar se confere com a geração Anual/Trimestral.”.

Parâmetro Desmarcado: O sistema deverá limpar os registros gravados na tabela “Sped_Cont_Dem_Contab”, compreendidos no período indicado na tela de geração da demonstração contábil, conforme regra original.
Default: Desmarcado.

Os registros da Apuração Trimestral e Anual gravados na tabela “Sped_Cont_Dem_Contab”, serão gravados no arquivo Meio Magnético da ECD, possibilitando a geração das demonstrações com 5 Períodos, sendo 4 períodos Trimestrais e 1 arquivo Anual, seguindo com a mesma estrutura especificada na regra de Geração do Registro J005 (RNJ005)

Observações: Apuração Trimestral do IRPJ: Respeitados os limites acima descritos, ainda que a apuração do IRPJ seja trimestral, o livro pode ser anual. A legislação do IRPJ obriga a elaboração e transcrição das demonstrações na data do fato gerador do tributo. Nada impede que, no mesmo livro, existam quatro conjuntos de demonstrações trimestrais e a anual.	

MFS-69607		RP00.1	Deverá ser gerada uma demonstração de resultado se:

Na tela de geração das demonstrações contábeis se for marcada a opção Demonstração de Resultado, será considerada a parametrização da tela de Códigos de Aglutinação (B. Patrimonial/D.Resultado/DLPA/DMPL), aba DLPL(campo 6 – Indicador de Aglutinação (IND_BALANCO_DRE) da SAFX2102, igual a “M”), para o estabelecimento que está sendo considerado na geração.

Serão considerados os valores dos saldos contábeis (SAFX02 ou SAFX80), das contas indicadas nas contas aglutinadoras (SAFX2103), compreendidos no período indicado na tela de geração da demonstração contábil. 

[MFS-85876 / MFS-532288]
Deverá ser considerado também as contas indicadas nas contas aglutinadoras (SAFX2103), compreendidos no período indicado na tela de geração da demonstração contábil, quando o Saldo Inicial e/ou Saldo Final for igual a zero (SAFX02 ou SAFX80), porém houver movimentação de Lançamentos Contábeis (SAFX01).

Para o cálculo serão obtidas as informações da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, consideraremos as informações da SAFX80. Na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

Para recuperar as informações dos Saldos Contábeis, caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil” estiver mercado, o sistema deverá recuperar os valores das tabelas SAFX02/SAFX226 e SAFX80/SAFX227 da mesma conta contábil e período, caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” estiver desmarcado, caso contrário  o cálculo serão obtidas somente das informações da SAFX02/SAFX226.

Em todo o processamento, serão geradas as visões Sintética (nível de contas aglutinadoras) e também a Analítica (nível de contas contábeis) e as informações de moeda corrente e moeda funcional.

Atenção: Não será mais utilizado as informações dos registros I350 para definirmos a periodicidade das demonstrações. Serão consideradas as datas indicadas na tela de Geração das Demonstrações Contábeis. (desta forma será de responsabilidade do cliente indicar a periodicidade que o estabelecimento se enquadra).

Validações Adicionais:

Se a parametrização for encontrada, porém não existir nenhuma conta com saldo para o período, exibir a mensagem na aba de log: A Demonstração de DLPL não será gerada, pois não foi encontrado saldos contábeis para o período. Estabelecimento: XXXX.	MFS-31025
MFS-85876
MFS-532288		RP01	REG
Quando na tela da Geração das Demonstrações Contábeis (Localização: MastersafDW >> SPED >> ECD – Escrituração Contábil Digital >> Geração >> Demonstrações Contábeis>> Geração) for selecionada a opção “DLPA” ou “DMPL”, gerar o texto fixo J210.	MFS-31025		RP02	DATA INICIAL

Preencher com a data inicial indicada na tela da geração das demonstrações contábeis.	MFS-31025		RP03	 DATA FINAL

Preencher com a data Final indicada na tela da geração das demonstrações contábeis.	MFS-31025		RP04	ORDEM

Nesse campo o sistema preenche com o número de ordem campo 04 da SAFX2102, (exibir a informação em ordem crescente).	MFS-31025		RP05	NIVEL_AGL

Neste campo o sistema preenche com o nivel da conta aglutinadora, indicada no campo “nível” da SAFX2102	MFS-31025		RP06	COD_AGL

Nesse campo o sistema preenche com o código da conta aglutinadora campo 03 da SAFX2102.	MFS-31025		RP07	DESCR_COD_AGL

Nesse campo o sistema preenche com a descrição da conta aglutinadora campo 05 da SAFX2102.	MFS-31025		RP08	VL_CTA_INI (Moeda Corrente)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Inicial das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_INI será obtido com base no resultado gerado no campo VL_CTA_INI. 

Estas informações necessárias para o cálculo serão obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX02 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	MFS-31025
MFS-532288		

RP09


	IND_DC_CTA_INI(Moeda Corrente)

Neste campo o sistema preenche com o indicador do saldo inicial das contas contábeis que foram sumarizados na conta aglutinadora (Campo 6 da SAFX02/ Campo 7 da SAFX80), conforme cálculo  no campo indicado no campo  VL_CTA_INI.	MFS-31025		RP10	VL_CTA_FIN (Moeda Corrente)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Final das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data final indicada na tela de geração das demonstrações.

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_FIN será obtido com base no resultado gerado no campo VL_CTA_FIN. 

Estas informações necessárias para o cálculo serão obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX02 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	MFS-31025
MFS-532288		RP11	IND_DC_CTA_FIN (Moeda Corrente)

Neste campo o sistema preenche com o indicador do saldo final das contas contábeis que foram sumarizados na conta aglutinadora (Campo8 da SAFX02/ Campo 11 da SAFX80), conforme cálculo  no campo indicado no campo  VL_CTA_FIN.	MFS-31025		RP12	VL_CTA_INI (Moeda Funcional)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Inicial das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_INI será obtido com base no resultado gerado no campo VL_CTA_INI. 

Estas informações necessárias para o cálculo serão obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

	MFS-31025
MFS-532288		RP13	IND_DC_CTA_INI(Moeda Funcional)

Neste campo o sistema preenche com o indicador do saldo inicial das contas contábeis que foram sumarizados na conta aglutinadora (Campo 6 da SAFX226/ Campo 7 da SAFX227), conforme cálculo  no campo indicado no campo  VL_CTA_INI.	MFS-31025		RP14	VL_CTA_FIN (Moeda Funcional)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Final das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data final indicada na tela de geração das demonstrações.

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_FIN será obtido com base no resultado gerado no campo VL_CTA_FIN. 

Estas informações necessárias para o cálculo serão obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	MFS-31025
MFS-532288		RP15	IND_DC_CTA_FIN(Moeda Funcional)

Neste campo o sistema preenche com o indicador do saldo final das contas contábeis que foram sumarizados na conta aglutinadora (Campo 8 da SAFX226/ Campo 9 da SAFX227), conforme cálculo  no campo indicado no campo  VL_CTA_FIN.	MFS-31025		RP16	CONTA_CONTABIL

Nesse campo o sistema preenche com o código da conta contábil, campo 01 da SAFX2002. Apresentar a conta contábil, logo abaixo da respectiva conta de aglutinação.	MFS-31025		RP17	DESCRICAO_CONTA_CONTABIL

Nesse campo o sistema preenche com a descrição da conta contábil campo 03 da SAFX2002. 	MFS-31025		RP18	VL_CTA_CONTABIL_INI (Moeda Corrente)

Neste campo o Sistema deve apresentar o saldo Inicial de cada Conta Contábil associada ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Estas informações são obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX02 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	MFS-31025
MFS-532288		RP19	IND_DC_CTA_CONTABIL_INI (Moeda Corrente)

Neste campo o Sistema deve apresentar o indicador de saldo inicial de cada Conta Contábil associada ao código de aglutinação.	MFS-31025		RP20	VL_CTA_CONTABIL_FIN (Moeda Corrente)

Neste campo o Sistema deve apresentar o Saldo Final de cada Conta Contábil associada ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Estas informações são obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX02 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

	MFS-31025
MFS-532288		
RP21	IND_DC_CTA_CONTABIL_FIN (Moeda Corrente)

Neste campo o Sistema deve apresentar o indicador de saldo final de cada Conta Contábil associada ao código de aglutinação.	MFS-31025		RP22	VL_CTA_CONTABIL_INI (Moeda Funcional)

Neste campo o Sistema deve apresentar o saldo Inicial de cada Conta Contábil associada ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Estas informações são obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	MFS-31025
MFS-532288		RP23	IND_DC_CTA_CONTABIL_INI(Moeda Funcional)

Neste campo o Sistema deve apresentar o indicador de saldo inicial de cada Conta Contábil associada ao código de aglutinação.	MFS-31025		RP24	VL_CTA_CONTABIL_FIN (Moeda Funcional)

Neste campo o Sistema deve apresentar o Saldo Final de cada Conta Contábil associada ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Estas informações são obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	MFS-31025
MFS-532288		RP25	IND_DC_CTA_CONTABIL_FIN(Moeda Funcional)

Neste campo o Sistema deve apresentar o indicador de saldo final de cada Conta Contábil associada ao código de aglutinação.	MFS-31025		RP26	NOTA_EXP_REF

Neste campo o sistema preenche com a informação do campo  7 – NUM_REFERENCIA da SAFX257, quando o IND_BALANCO_DRE = ‘L’ ou ‘M’ e estiver associados ao código de aglutinação selecionada. O período de referência para seleção dos registros é o mês e ano das datas indicadas na geração da demonstração que devem estar compreendidos na DAT_DEMONSTRACAO da tabela SAFX257 (considerar a data mais atual, limitado ao final do período de geração da demonstração).	MFS-31025		J215 - FATO CONTÁBIL QUE ALTERA A CONTA LUCROS ACUMULADOS OU A CONTA PREJUÍZOS ACUMULADOS OU TODO O PATRIMÔNIO LÍQUIDO		RP27	REG
Quando na tela da Geração das Demonstrações Contábeis (Localização: MastersafDW >> SPED >> ECD – Escrituração Contábil Digital >> Geração >> Demonstrações Contábeis>> Geração) for selecionada a opção “DLPA” ou “DMPL” e existir lançamentos contábeis associados à conta aglutinadora gerar o texto fixo J215.

[MFS-85876]
Deverá ser considerado também as informações do Registro J210, referente às informações geradas quando o Saldo Inicial e/ou Saldo Final for igual a zero (SAFX02 ou SAFX80), porém existir movimentação de Lançamentos Contábeis (SAFX01).
	MFS-31025
MFS-85876		RP28	COD_HIST_FAT

Nesse campo o sistema preenche com a descrição do fato contábil, campo 01 – COD_HIST_FATO_CONTABIL da SAFX2056.	MFS-31025		RP29	DESC_FAT

Nesse campo o sistema preenche com a descrição do fato contábil, campo 03 – DESCRICAO da SAFX2056.	MFS-31025		RP30	VL_FAT_CONT

Nesse campo o sistema preenche com valor do lançamento contábil associado à conta aglutinadora, campo 07 - VLR_LANCTO da SAFX01 ou da SAFX225	MFS-31025		RP31	IND_DC_FAT

Nesse campo o sistema preenche com o indicador do lançamento contábil associado à conta aglutinadora, campo 05 - IND_DEB_CRE da SAFX01 ou da SAFX225	MFS-31025