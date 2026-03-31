# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Operacoes_do_Periodo

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Operacoes_do_Periodo.doc

TITLE   \* MERGEFORMAT EFD - Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas - Operações do Período 


DOCUMENTO DE REQUISITO 

DR	Nome	Descrição		OS3810
	EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Parametrização por Conta Contábil	Essa OS tem por objetivo a criação do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Trata-se da escrituração digital dos tributos PIS e COFINS para as instituições financeiras, seguradoras, entidades de previdência privada, operadoras de planos de assistência à saúde e assemelhadas, conforme Ato Declaratório Executivo nº. 65 de 20/12/12.		OS3810-B	EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Geração dos Registros	Essa OS tem por objetivo a geração dos registros e da apuração do módulo EFD–Contribuições Financeira/Assemelhada. Trata-se da escrituração digital dos tributos PIS e COFINS para as instituições financeiras, seguradoras, entidades de previdência privada, operadoras de planos de assistência à saúde e assemelhadas, conforme Ato Declaratório Executivo nº. 65 de 20/12/12.		MFS61556	Andréa Rocha	Inclusão de novos códigos (02 a 05) para os campos de Código de Situação Tributária do PIS e Código de Situação Tributária do COFINS, de acordo com os códigos disponibilizados no Guia Prático.		


Cód.	


Descrição	


DR		RN01	Deverá ser criada uma tela chamada “Operações do Período” no módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas.

Essa tela possuirá três abas que permitirão as operações do tipo CRUD (Create/Read/Update/Delete), ou seja, será permitida a inclusão, consulta, alteração e exclusão de registros.

	OS3810-A1		RN02	Ao abrir a tela o sistema irá solicitar as informações para pesquisa dos registros I100, I200 e I300. As informações solicitadas são:

Estabelecimento: o usuário deverá selecionar o Estabelecimento para pesquisa. O estabelecimento será exibido no formato 9999 – AAAA, onde “9999” é o Código do Estabelecimento e “AAAA” é a Descrição do Estabelecimento. Campo obrigatório de preenchimento.
Período de Apuração: o usuário deverá informar o Período de Apuração para visualização dos registros I100, I200 e I300. O usuário deverá informar o período (data inicial e data final) no formato DD/MM/AAAA. Campo obrigatório de preenchimento. 

Caso o Estabelecimento não seja informado e o usuário clique em “OK”, o sistema deverá exibir a seguinte mensagem de erro: “Estabelecimento não informado. Por gentileza informar o estabelecimento.”.

Caso a data inicial e/ou final do Período de Apuração não seja informada e o usuário clique em “OK”, o sistema deverá exibir a seguinte mensagem de erro: “Data Inicial e/ou Final não informada no Período de Apuração. Por gentileza informar o Período de Apuração.”.

Caso a data final esteja inferior à data inicial e o usuário clique em “OK”, o sistema deverá exibir a seguinte mensagem de erro: “Data Final é inferior à Data Inicial no Período de Apuração. Por gentileza verificar a informação.”.	OS3810-A1
		RN03	A tela disponibilizará três abas: “I100 - Consolidação das Operações do Período”, “I200 - Composição das Receitas/Deduções/Exclusões” e “I300 - Complemento das Operações”. Os campos a seguir são referentes à aba “I100 - Consolidação das Operações do Período”. Os campos informados do registro I100 serão os seguintes:

Data Inicial: o usuário visualizará a data inicial da apuração informada na RN02. 
Data Final: o usuário visualizará a data final da apuração informada na RN02. 
Código Situação Tributária PIS/COFINS: o usuário deverá selecionar o Código da Situação Tributária PIS/COFINS cadastrado no Mastersaf DW. Será permitida a seleção de apenas um Código Situação Tributária PIS. Campo obrigatório de preenchimento. As informações serão recuperadas da tabela Y2027_SIT_TRIBUTARIA, quando o campo IND_TRIBUTACAO = “1”. Estamos considerando apenas os códigos “1” porque é indiferente, visto que os CST’s de PIS e COFINS são iguais e nunca poderão ser parametrizados diferentes. Além disso, só serão exibidos os seguintes códigos:

[MFS61556] Inclusão dos códigos 02, 03, 04 e 05, conforme a lista de códigos disponibilizada pelo Guia Prático

01 – Operação Tributável com Alíquota Básica
2 - Operação Tributável com Alíquota Diferenciada
3 - Operação Tributável com Alíquota por Unidade de Medida de Produto
4 - Operação Tributável Monofásica - Revenda a Alíquota Zero
5 - Operação Tributável por Substituição Tributária
06 – Operação Tributável a Alíquota Zero
07 – Operação Isenta da Contribuição
08 – Operação sem Incidência da Contribuição
09 – Operação com Suspensão da Contribuição
49 – Outras Operações de Saída
99 – Outras Operações
Valor da Receita: o usuário deverá informar o Valor Total do Faturamento/Receita Bruta do Período. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais.
Valor Total das Deduções e Exclusões de Caráter Geral: o usuário deverá informar o Valor Total do das Deduções e Exclusões de Caráter Geral do Período. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais.
Valor Total das Deduções e Exclusões de Caráter Específico: o usuário deverá informar o Valor Total do das Deduções e Exclusões de Caráter Específico do Período. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais.
Valor da Base de Cálculo do PIS: o usuário deverá visualizar o Valor da Base de Cálculo do PIS. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais. Campo não editável. O resultado desse campo será “Valor da Receita” – “Valor Total das Deduções e Exclusões de Caráter Geral”.
Alíquota PIS: o usuário deverá informar a Alíquota referente ao PIS. O campo deverá ser numérico de 7 posições, sendo 3 inteiras e 4 decimais.
Valor do PIS: o usuário deverá visualizar o Valor do PIS. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais.. Campo não editável. O resultado desse campo será “Valor da Base de Cálculo do PIS” * “Alíquota PIS”.
Valor da Base de Cálculo do COFINS: o usuário deverá visualizar o Valor da Base de Cálculo do COFINS. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais. Campo não editável. O resultado desse campo será “Valor da Receita” – “Valor Total das Deduções e Exclusões de Caráter Geral”.
Alíquota COFINS: o usuário deverá informar a Alíquota referente ao COFINS. O campo deverá ser numérico de 7 posições, sendo 3 inteiras e 4 decimais. 
Valor do COFINS: o usuário deverá informar o Valor do COFINS. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais.. Campo não editável. O resultado desse campo será “Valor da Base de Cálculo do COFINS” * “Alíquota COFINS”.
Informação Complementar: o usuário deverá informar a Informação Complementar. Esse campo deverá ser alfanumérico de 150 posições.
	OS3810-A1
OS3810-B
MFS61556		RN04	Para cada registro incluído na aba “I100 – Consolidação das Operações do Período”, o usuário poderá incluir de 1:N registros na aba “I200 – Composição das Receitas/Deduções/Exclusões”.	OS3810-A1		RN05	Os campos a seguir são referentes à aba “I200 – Composição das Receitas/Deduções/Exclusões”.

Número do Campo: o usuário deverá informar o Número do Campo para a declaração do registro I200. Serão exibidas para o usuário três opções para escolha:
Valor da Receita
Valor Total das Deduções e Exclusões de Caráter Geral
Valor Total das Deduções e Exclusões de Caráter Específico
Código Receita/Dedução/Exclusão: o usuário deverá selecionar o Código da Receita/Dedução/Exclusão que foi importado através da TACES82. Será permitida a seleção de apenas um Código Receita/Dedução/Exclusão.
Valor Detalhado: o usuário deverá visualizar o Valor Detalhado. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais.
Código Conta Contábil: o usuário deverá selecionar a Conta Contábil. A informação deverá ser recuperada da tabela X2002_PLANO_CONTAS.
Informação Complementar: o usuário deverá informar a Informação Complementar. Esse campo deverá ser alfanumérico de 150 posições.
	OS3810-A1		RN06	Para cada registro incluído na aba “I200 – Composição das Receitas/Deduções/Exclusões”, o usuário poderá incluir de 1:N registros na aba “I300 – Complemento das Operações – Detalhamento das Receitas, Deduções e/ou Exclusões do Período”.	OS3810-A1		RN07	Os campos a seguir são referentes à aba “I300 – Complemento das Operações – Detalhamento das Receitas, Deduções e/ou Exclusões do Período”.

Código Complemento Receita/Dedução/Exclusão: o usuário deverá selecionar o Código de Complemento da Receita/Dedução/Exclusão que foi importado através da TACES83. Será permitida a seleção de apenas um Código de Complemento da Receita/Dedução/Exclusão. Campo obrigatório de preenchimento.
OBS: vale frisar que o conteúdo desse campo será definido a partir das tabelas 7.1.3 e 7.1.4 que ainda não foram disponibilizadas pela RFB. Estamos no aguardo dessa definição. Enquanto isso, a tabela foi criada com um conteúdo fake para agilizar o processo de desenvolvimento e homologação.
Valor Detalhado: o usuário deverá visualizar o Valor Detalhado. O campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais.
Código Conta Contábil: o usuário deverá selecionar a Conta Contábil. A informação deverá ser recuperada da tabela X2002_PLANO_CONTAS.
Informação Complementar: o usuário deverá informar a Informação Complementar. Esse campo deverá ser alfanumérico de 150 posições.	OS3810-A1		RN08	Deverá ser criado um relatório de conferência para essa tela.	OS3810-A1		RN09	Vale frisar que as abas referentes aos registros I200 e I300 só serão exibidas caso sejam selecionadas. Exemplo:

Caso a aba referente ao registro I100 seja selecionado, somente os campos do registro I100 serão exibidos;
Caso a aba referente ao registro I200 seja selecionado, somente os campos dos registros I100 e I200 serão exibidos;
Caso a aba referente ao registro I300 seja selecionado, somente os campos dos registros I100, I200 e I300 serão exibidos, ou seja, todos os campos.	OS3810-A1		RN10	A coluna “Ind Tributação” deverá ser retirada, quando o usuário for selecionar o Código de Situação Tributária PIS/COFINS. Serão exibidos somente os códigos de situação tributária referentes ao PIS. 

Essa regra é importante, pois o código de PIS e COFINS sempre será o mesmo.	OS3810-B		RN11	Na tela “I100 – Consolidação das Operações do Período” ao selecionar o Código de Situação Tributária PIS/COFINS, não deverá ser exibido se o código é de PIS ou COFINS.	OS3810-B		RN12	Na tela de manutenção da Apuração PIS/PASEP, os campos “Valor do Crédito Diferido no Período” e “Código de Tipo de Crédito Diferido no Período” deverão ficar desabilitados.	OS3810-B		RN13	Na tela de manutenção da Apuração COFINS, os campos “Valor do Crédito Diferido no Período” e “Código de Tipo de Crédito Diferido no Período” deverão ficar desabilitados.	OS3810-B		

Considerações deste modelo:


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN