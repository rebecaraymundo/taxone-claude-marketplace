# Tela_e_Processamento_Percentuais_de_Rateio_Atividades_Mistas

> Fonte: Tela_e_Processamento_Percentuais_de_Rateio_Atividades_Mistas.doc

THOMSON REUTERS

Tela Percentuais de Rateio das Atividades Mistas 
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		09/11/2017	MFS-14486	Criação do documento 	Alessandra Cristina Navatta		Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc498086688" 1.	INTRODUÇÂO	 PAGEREF _Toc498086688 \h 3
 HYPERLINK \l "_Toc498086689" 2.	DOCUMENTOS DE REFERÊNCIAS	 PAGEREF _Toc498086689 \h 3
 HYPERLINK \l "_Toc498086690" 3.	TELAS	 PAGEREF _Toc498086690 \h 4
 HYPERLINK \l "_Toc498086691" 3.1.	Regras dos Campos Tela Principal	 PAGEREF _Toc498086691 \h 4
 HYPERLINK \l "_Toc498086692" 4.	REGRAS – PROCESSAMENTO DOS PERCENTUAIS DE RATEIO DAS ATIVIDADES MISTAS	 PAGEREF _Toc498086692 \h 8

INTRODUÇÂO

O objetivo desta especificação é criar a tela e processamento para a criação dos percentuais de rateio das atividades gerais e rural no produto ECF - Escrituração Contábil Fiscal (DW).


DOCUMENTOS DE REFERÊNCIAS


Mensagens_Sistema_DWECF.xlsx

Regras_Gerais_DWECF.docx

Tela_Abertura_de_Apuracao.doc

MTZ_ Processamento_em_Lote.docx



TELAS


Regras dos Campos Tela Principal

Localização da tela: ECF - Escrituração Contábil Fiscal >>Apuração >> Ajuste Manuais >> Percentuais de Rateio das Atividades Mistas 

Título da tela: Percentuais de Rateio das Atividades Mistas 


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Processar	Botão	-	-	Default desabilitado-	Botão que permite submeter às parametrizações para processamento. 

Tratamentos:

As regras do processamento estão no item  HYPERLINK  \l "RegrasdeProcessamento" 4. REGRAS – PROCESSAMENTO DOS PERCENTUAIS DE RATEIO DAS ATIVIDADES MISTAS deste documento.

Se nenhum registro for selecionado no componente “Períodos de Apuração dos Estabelecimentos’, exibir a mensagem DW00054 

O somatório dos campos Percentual Ajustado (Geral (%) e Rural (%)) devem totalizar 100,0000%. Caso contrário, exibir a mensagem DW00129 (log)  e não seguir com o processamento.


Após o processamento, exibir a mensagem DW00128.	MFS-14486		Tela: Principal(*)Titulo: Percentuais de Rateio das Atividades Mistas		Componente Opções de Processamento(*)Título: Opções de Processamento		Exercício	Texto	S	S	AAAA	Permite que o usuário visualize/informe o exercício para seleção dos registros de abertura da apuração	MFS-14486		Considerar Percentuais Ajustados	Check-box	-	-	Desmarcado	Permite ao usuário informar se os percentuais de rateio das atividades mistas serão ajustados ou não.

Tratamentos:

Se marcado este parâmetros os campos Percentual Ajustado Geral (%) e Percentual Ajustado Rural (%), serão habilitados e os percentuais que serão utilizados são os ajustados e não o calculado pelo sistema.

	MFS-14486		Percentual Ajustado Geral (%)	Texto	N	S	000,0000	
Permite ao usuário ajustar o percentual de rateio para a atividade geral.

Tratamentos:

Só habilitar este campo se o parâmetro ‘Considerar Percentuais Ajustados’, estiver marcado.

Aceitar só valores de 0 a 100 (antes do separador de decimal).

O valor máximo permitido para este campo é 100,0000.	MFS-14486		Percentual Ajustado Rural (%)	Texto	N	S	000,0000	Permite ao usuário ajustar o percentual de rateio para a atividade rural.


Tratamentos:

Só habilitar este campo se o parâmetro ‘Considerar Percentuais Ajustados’, estiver marcado.

Aceitar só valores de 0 a 100 (antes do separador de decimal).

O valor máximo permitido para este campo é 100,0000.
	MFS-14486		Mensagem explicativa(*):Selecione abaixo as aberturas de apuração com os percentuais que foram calculados pelo processamento em Lote (opção Transcrição de Valores).		Períodos de Apuração dos Estabelecimentos		Selecionar	LOV	N	S	-	
Permite que o usuário selecione os registros de abertura de apuração, com os percentuais que serão considerados no processamento.Tratamentos:

Recuperar as aberturas de apuração (todas exceto A00), com Forma de Tributação = ‘Lucro Real’ ou ‘Lucro Presumido’ e Status = ‘Importação dos Saldos Realizada’, ‘Reapurar’, ‘Aguardando Alteração Manual’ ou ‘Alteração Manual Realizada’, cuja Informação ECF esteja com o campo ‘Atividade Rural’ marcado.

Só apresentar os registros, que foram calculados na importação de saldos os campos de atividades (geral e rural) e os percentuais de rateio (Geral e Rural).


	MFS-14486		Marcar Todos	(CheckBox)	-	-	Default Desmarcado	Permite que o usuário selecione todos os registros de abertura de apuração da grid ‘Períodos de apuração dos Estabelecimentos’	MFS-14486		(CheckBox)	-	-	-	Default Desmarcado	Permite que o usuário selecione uma ou mais “Abertura de Apuração” dos diferentes estabelecimentos para serem processados.).	MFS-14486		Aberturas de Apurações (*)	Texto	S	N	Código Estab - CGC - Exercício -  Data Inicial da Escrituração -  Código Abertura - Descrição da Aberura da Apuração – Percentual Geral e Rural: XXX,XXXX% e XXX,XXXX%(076 - XXXXXXXXXXX - 2017 -01/03/2017 - A1 – Janeiro - Percentual Geral e Rural:90,000% e 10,0000%)	Apresenta as aberturas de apuração que foram recuperadas.	MFS-14486		
(*) Não exibir a descrição na tela.


REGRAS – PROCESSAMENTO DOS PERCENTUAIS DE RATEIO DAS ATIVIDADES MISTAS 

Voltar para as regras do  HYPERLINK  \l "BotaoProcessar" botão Processar


CÓD	DESCRIÇÃO	OS/CH/WI		RNP00	Criar uma rotina para criar os percentuais de rateio das atividades mistas.

Com base na parametrização da tela ‘Percentuais de Rateio das Atividades Mistas’ o processamento deverá ocorrer para as aberturas das apurações dos estabelecimentos selecionadas.

	MFS-14486		RNP01	
Recuperação dos Registros:

Considerar os registros que foram processados na rotina de importação de saldos, para as aberturas de apuração dos estabelecimentos, selecionadas na tela “Percentuais de Rateio das Atividades Mistas” dos saldos das contas referenciais do registro L300A (quando forma de tributação = Lucro Real) ou P150 (quando forma de tributação = Lucro Presumido) cuja uma mesma conta contábil e centro de custo (este ultimo quando existir) esteja vinculada aos referenciais 3.01 e 3.11.
A Data do Saldo Contábil deve estar compreendida entre a data inicial e final presente na Abertura da apuração.
	MFS-14486		RNP02	Ajustando os valores dos saldos:

O usuário poderá ou não ajustar os valores dos percentuais calculados pelo sistema, ajustando os valores nos campos Percentual Ajustado Geral (%) e Percentual Ajustado Rural (%)da tela “Percentuais de Rateio das Atividades Mistas”. 	MFS-14486		RNP03	Alteração dos Saldos das Contas Contábeis, campo Saldo Informado (da tela Ajuste Manual do Balanço/DRE (Bloco K) :


Campos PERC. GERAL AJUSTADO e PERC. RURAL AJUSTADO preenchidos:

Será alterado para cada conta contábil analítica e centro de custo (vinculadas às contas referenciais iniciadas por 3.01 e 3.11) a informação do saldo utilizada pela rotina de importação de saldos e não na tabela de saldos, conforme regras:

- Se a conta contábil e o centro de custo estiverem associados às contas referenciais iniciadas por 3.01, o Saldo Informado da conta contábil/centro de custo/conta referencial será o resultado do saldo calculado da conta (na importação de saldos) multiplicado pelo campo PERC. GERAL AJUSTADO dividido por 100.

-Se a conta contábil e o centro de custo estiverem associados às contas referenciais iniciadas por 3.11, o Saldo Informado da conta contábil/centro de custo/ conta referencial será o resultado do saldo calculado da conta (na importação de saldos) multiplicado pelo campo PERC. RURAL AJUSTADO dividido por 100.

- o Saldo Informado da conta contábil e centro de custo será recalculado com base na somatória dos Saldos Informados das contas referenciais associadas, após a aplicação dos percentuais acima.

O registro estará disponível na tela ‘Ajuste Manual do Balanço/DRE (Bloco K)’, aba Rateio, campo justificativa Vazio e o campo Validar Vazio.

O status da apuração deve ser alterado para ‘Aguardando Ajuste Manual’.


Campos PERC. GERAL AJUSTADO e PERC. RURAL AJUSTADO não preenchidos:

Será alterado para cada conta contábil analítica e centro de custo (vinculadas às contas referenciais iniciadas por  3.01 e 3.11) a informação do saldo utilizada pela rotina de importação de saldos e não na tabela de saldos, conforme regras:

Se os percentuais não foram alterados pelo usuário, considerar os percentuais calculados pelo sistema (campos PERC. GERAL CALCULADO ou PERC. RURAL_ CALCULADO). 

- Se a conta contábil e o centro de custo estiverem associados às contas referenciais iniciadas por 3.01, o Saldo Informado da conta contábil/centro de custo/conta referencial será o resultado do saldo calculado da conta (na importação de saldos) multiplicado pelo campo PERC. GERAL CALCULADO dividido por 100.

- Se a conta contábil e centro de custo estiverem associados às contas referenciais iniciadas por 3.11, o Saldo Informado da conta contábil/centro de custo/ conta referencial será o resultado do saldo calculado da conta (na importação de saldos) multiplicado pelo campo PERC. RURAL CALCULADO dividido por 100.

- o Saldo Informado da conta contábil e centro de custo será recalculado com base na somatória dos Saldos Informados das contas referenciais associadas, após a aplicação dos percentuais acima.

O registro estará disponível na tela ‘Ajuste Manual do Balanço/DRE (Bloco K)’, aba Rateio, campo justificativa Vazio e o campo Validar Vazio.

O status da apuração deve ser alterado para ‘Aguardando Ajuste Manual’.

Exemplos:

Cenário1: Uma conta referencial por tipo de atividade:

 Conta Referencial   | Saldo Calculado  | Percentual das Atividades
|   3.01.01.01             |   2000,00             |      50% (geral)
|   3.11.01.01             |    2000,00            |      50% (rural)


Aplicando os percentuais:
Conta Contábil |Centro de Custo| Conta Referencial   | Saldo Calculado | Saldo Informado
CTA                   | CC                    | 3.01.01.01               | 2000,00               | 2000,00 x Perc. Geral 
CTA                   | CC                    | 3.11.01.01               | 2000,00               | 2000,00 x Perc. Rural

Conta Contábil |Centro de Custo| Conta Referencial   |Saldo Calculado | Saldo Informado
CTA                   | CC                    | 3.01.01.01               |2000,00                | 1000,00 (50%)
CTA                   | CC                    | 3.11.01.01               |2000,00                | 1000,00 (50%)

Conta Contábil |Centro de Custo   |Saldo Calculado | Saldo Informado
CTA                   | CC                       | 2000,00             | 2000,00 


Conta Referencial     |Saldo Calculado | Saldo Informado (L300 / P150)
|   3.01.01.01             | 2000,00              | 1000,00 


Cenário 2: Mais de uma conta referencial por tipo de atividade:

Conta Referencial   | Saldo Calculado  | Percentual das Atividades
|   3.01.01.01             |   1000,00             |      50% (geral)
|   3.11.01.01             |    1000,00            |      50% (rural)


Aplicando os percentuais:
Conta Contábil |Centro de Custo| Conta Referencial   | Saldo Calculado | Saldo Informado
CTA                   | CC                    | 3.01.01.01               | 1000,00               | 1000,00 x Perc. Geral 
CTA                   | CC                    | 3.11.01.01               | 1000,00               | 1000,00 x Perc. Rural
CTA                   | CC                    | 3.11.01.02               | 1000,00               | 1000,00 x Perc. Rural

Conta Contábil |Centro de Custo| Conta Referencial   |Saldo Calculado | Saldo Informado
CTA                   | CC                    | 3.01.01.01               |1000,00                | 500,00 (50%)
CTA                   | CC                    | 3.11.01.01               |1000,00                | 500,00 (50%)
CTA                   | CC                    | 3.11.01.02               |1000,00                | 500,00 (50%)

Conta Contábil |Centro de Custo   |Saldo Calculado | Saldo Informado
CTA                   | CC                       | 1000,00             | 1500,00 

Conta Referencial     |Saldo Calculado | Saldo Informado (L300 / P150)
|   3.01.01.01             | 1000,00              | 500,00 

Se existir alteração do percentual. Ex. 40%:
Conta Contábil |Centro de Custo| Conta Referencial     |Saldo Calculado | Saldo Informado
CTB                   | CC                    |   3.01.01.01               | 1000,00              | 400,00 (40%)


Validação da versão

Considerando a RNG00003 - Versão da Escrituração:

Se a versão não for compatível com a data da ECF (período de vigência), exibir a DW00018
Exemplo: Data Inicial 01/01/2014 (independente se houver situação especial ou não) com versão 2.00

Se a versão for compatível com a data da ECF (período de vigência), mas a versão não for compatível com a ocorrência de situação especial, exibir a DW00019.
Exemplo: Data Inicial 01/01/2015 (com situação especial) com versão 2.00

Se a versão for compatível com a data da ECF (período de vigência), mas a versão não é compatível sem a ocorrência de situação especial, exibir a DW00020.Exemplo: Data Inicial 01/01/2015 (sem situação especial) com versão 1.00.
	MFS-14486		RNP04	Visualização dos Percentuais 

Os valores dos percentuais calculado pelo sistema e alterados pelo usuário (este último, apenas se houver alteração), quando processados pela rotina de percentuais de rateio das atividades mistas serão visualizados na tela ‘Ajuste Manual do Balanço/DRE (Bloco K)’, aba Atividades Mistas (apenas para consulta).
	MFS-14486		RNP05	Indicação que o registro foi processado pela rotina de percentuais de rateio das atividades mistas:

Ao efetuar o processo de cálculo dos percentuais de rateio das atividades mistas o registro ficará com a indicação que o cálculo foi criado pela rotina de ‘Percentuais de Rateio das Atividades Mistas’, seguindo as informações abaixo:

- O campo ‘Percentual de Rateio das Atividades Mistas’ da tela ‘Ajuste Manual do Balanço/DRE (Bloco K)’, deve ser preenchido com ‘Gerado pelo Sistema’, se o cálculo for feito e processado pela rotina e os valores não forem alterados pelo usuário. Se os campos ‘Percentual da Atividade’ (Geral e Rural) forem alterados pelo usuário (no modal ‘ Alterar Valores dos Percentuais das Atividades Mistas’), e processado pela rotina, o campo deve ser atualizado para: ‘Gerado pelo Sistema e Alterado pelo Usuário’.
	MFS-14486