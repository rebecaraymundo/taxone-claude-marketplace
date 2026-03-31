# Tela_Programa_de_Alimentacao_do_Trabalhador

> Fonte: Tela_Programa_de_Alimentacao_do_Trabalhador.doc

THOMSON REUTERS

Tela Programa de Alimentação do Trabalhador – PAT
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		30/05/2018	MFS-18708	Criação da tela	Alessandra Cristina Navatta		


Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc516491024" 1.	INTRODUÇÂO	 PAGEREF _Toc516491024 \h 3
 HYPERLINK \l "_Toc516491025" 2.	DOCUMENTOS DE REFERÊNCIAS	 PAGEREF _Toc516491025 \h 3
 HYPERLINK \l "_Toc516491026" 3.	TELAS	 PAGEREF _Toc516491026 \h 3
 HYPERLINK \l "_Toc516491027" 3.1.	Pesquisa de Registros	 PAGEREF _Toc516491027 \h 3
 HYPERLINK \l "_Toc516491028" 3.2.	Regras dos Campos da Tela Principal	 PAGEREF _Toc516491028 \h 4
 HYPERLINK \l "_Toc516491029" 5.2.1	Regra dos campos	 PAGEREF _Toc516491029 \h 9

INTRODUÇÂO

O objetivo desta especificação é criar uma tela onde o usuário possa conferir os valores de PAT calculados pelo sistema.

DOCUMENTOS DE REFERÊNCIAS

Mensagens_Sistema_DWECF.xlsx

Regras_Gerais_DWECF.docx

Tela_Informacoes_ECF.doc

TELAS

Pesquisa de Registros 

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Lucro Real >> Incentivos Fiscais >> PAT

Título da tela: Programa de Alimentação do Trabalhador - PAT


Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.


Campo	Tipo	Regra		Estabelecimento	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
AAAA	

O usuário poderá informar o exercício. 

		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código -Descrição)	Aplicar a RNG00004 (Versão de Layout)		Forma de Tributação	Lista
(Código -Descrição)	Exibe as opções abaixo:

-Lucro Real, Lucro Presumido, Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 


		Apuração	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral

		


Regras dos Campos da Tela Principal

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Lucro Real >> Incentivos Fiscais >> PAT
Título da tela: Programa de Alimentação do Trabalhador – PAT

Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		DADOS GERAIS		Estabelecimento	Texto	S	N	Tipo - Código - Descrição	Permite que o usuário visualize o estabelecimento correspondente ao registro selecionado na tabela de Informações ECF.	MFS-18708		Exercício	Texto	S	N	AAAA	Permite que o usuário visualize o ano correspondente ao registro selecionado na tabela de informações ecf.	MFS-18708		Data Inicial	Texto	S	N	DD/MM/AAAA	Permite que o usuário visualize a data inicial, referente ao registro selecionado na tabela das informações ecf.	MFS-18708		Versão	Texto	S	N	Código - Descrição	Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro, referente ao registro selecionado na tabela de informações ecf.	MFS-18708		Forma de Tributação	Texto	S	N	Descrição	Permite que o usuário visualize a forma de tributação, referente ao registro selecionado na tabela das informações ecf.	MFS-18708		Apuração	Texto	S	N	Descrição	Permite que o usuário visualize a apuração, referente ao registro selecionado na tabela das informações ecf.	MFS-18708		Data Final do Último Período da Escrituração	Texto	S	N	DD/MM/AAAA	Permite que o usuário visualize a data do último período da escrituração.	MFS-18708		Aba (*)
Título: Mensal por Estimativa		REGISTRO N620 - CÁLCULO DO IRPJ MENSAL POR ESTIMATIVA		Grid Registro N620 (*)		PERÍODO	Texto	S	N	Descrição	Permite que o usuário visualize o período correspondente a cada abertura de apuração vinculada a informação da ECF.

Se a apuração for mensal, exibir a descrição de cada mês.
Se a apuração for trimestral, exibir a descrição de cada trimestre.	MFS-18708		TIPO DE RECEITA	Texto	S	N	Descrição	Permite que o usuário visualize o Tipo de Receita para a linha calculada.

No Caso do Tipo de Receita da Tela Abertura da Apuração for igual a “Comparativo”: Se já tiver sido feita a opção por um tipo de receita no período através da tela de “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, exibir a que foi escolhida. Se não foi decidida uma opção pelo tipo de receita o sistema deve exibir as duas linhas.

Valores Válidos:

“Receita Bruta”
“Balanço de Suspensão/Redução”
	MFS-18708		VALOR DO PAT DISPONÍVEL DE PERÍODOS ANTERIORES 	Texto	S	N	0,00	Permite visualização do valor acumulado do PAT de períodos anteriores disponível para utilização nos períodos posteriores. 

Tratamento:


Para a primeira abertura que está sendo processada da escrituração: 
Este valor pode ser recuperado na tela PAT– Períodos Anteriores ao DW quando houver registros, filtrando o valor dos últimos 2 anos, anteriores a escrituração que está sendo processada, ou das últimas escriturações calculadas pelo sistema (dos últimos dois anos). Sempre limitando aos dois últimos anos-calendários da escrituração que está sendo processada. 
A partir da segunda abertura da escrituração que está sendo processada, considerar o valor do PAT não utilizado da abertura anterior, mais o Valor do PAT Disponível Neste Período Para Uso Posterior. 
	MFS-18708		Agrupamento (*)
Título: Antes da Atualização		VALOR DO PAT 	Texto	S	N	0,00	Permite que o usuário visualize o valor de PAT de cada período (antes do cálculo).

Tratamento:
Exibir o valor de PAT corresponde a linha 9 do registro N620.	MFS-18708		LIMITE DE 15% SOBRE O PAT 	Texto	S	N	0,00	Permite que o usuário visualize o limite de 15% calculado sobre o PAT antes da atualização de cada período.
Tratamento:

Exibir o resultado da expressão N620 (9) * 0,15
	MFS-18708		VALOR DO IMPOSTO DEVIDO	Texto	S	N	0,00	Permite que o usuário visualize o valor do imposto de cada período.

Tratamento:

Exibir o valor do imposto corresponde a linha 3 do registro N620.	MFS-18708		LIMITE DE 4% SOBRE O IMPOSTO DEVIDO	Texto	S	N	0,00	Permite que o usuário visualize o limite de 4% calculado sobre o imposto devido de cada período.

Tratamento:
Exibir o resultado da expressão N620 (3) * 0,04
	MFS-18708		VALOR DO PDTI/PDTA	Texto	S	N	0,00	Permite que o usuário visualize o valor do incentivo PDTI/PDTA de cada período.

Tratamento:

Exibir o valor do PDTI/PDTA corresponde a linha 10 do registro N620.	MFS-18708		LIMITE DE 4% COM PDTI/PDTA	Texto	S	N	0,00	Permite que o usuário visualize o limite de 4% com a dedução do incentivo PDTI/PDTA de cada período.

Tratamento:

Exibir o resultado da expressão LIMITE DE 4% SOBRE O IMPOSTO DEVIDO - VALOR DO PDTI/PDTA	MFS-18708		VALOR UTILIZADO DO PAT DE PERÍODOS ANTERIORES	Texto	S	N	0,00	Permite que o usuário visualize o valor de PAT que foi utilizado dos períodos anteriores (dentro do período que está sendo processado).	MFS-18708		VALOR DO PAT ATUALIZADO	Texto	S	N	0,00	Permite que o usuário visualize o valor do PAT atualizado na linha 9 do registro N620 em cada período.	MFS-18708		VALOR DO PAT DISPONÍVEL NESTE PERÍODO PARA USO POSTERIOR	Texto	S	N	0,00	Permite visualização do valor do PAT não utilizado no período.

Tratamento:

O valor exibido neste campo corresponde ao valor não utilizado no período do limite de 15%.

	MFS-18708		(*) Não exibir a descrição na tela.

Regra dos campos

Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Aba Anual		Registro N630 - CÁLCULO DO IRPJ COM BASE NO LUCRO REAL		GRID registro N630(*)		PERÍODO	Texto	S	N	Descrição	Permite que o usuário visualize o período correspondente a cada abertura de apuração vinculada a informação do ECF.

Se a apuração for mensal, exibir a descrição  anual.
Se a apuração for trimestral, exibir a descrição de cada trimestre.	MFS-18708		VALOR DO PAT DISPONÍVEL DE PERÍODOS ANTERIORES 	Texto	S	N	0,00	Permite visualização do valor acumulado do PAT de períodos anteriores disponível para utilização nos períodos posteriores. 

Tratamento:


Para a primeira abertura que está sendo processada da escrituração: 
Este valor pode ser recuperado na tela PAT– Períodos Anteriores ao DW quando houver registros, filtrando o valor dos últimos 2 anos, anteriores a escrituração que está sendo processada, ou das últimas escriturações calculadas pelo sistema (dos últimos dois anos). Sempre limitando aos dois últimos anos-calendários da escrituração que está sendo processada. 
A partir da segunda abertura da escrituração que está sendo processada, considerar o valor do PAT não utilizado da abertura anterior, mais o Valor do PAT Disponível Neste Período Para Uso Posterior. 
	MFS-18708		Agrupamento (*)
Título: Antes da Atualização		VALOR DO PAT 	Texto	S	N	0,00	Permite que o usuário visualize o valor de PAT doperíodo (antes do cálculo).

Tratamento:
Exibir o valor de PAT corresponde a linha 8 do registro N630A, N630B ou N630C.	MFS-18708		LIMITE DE 15% SOBRE O PAT 	Texto	S	N	0,00	Permite que o usuário visualize o limite de 15% calculado sobre o PAT antes da atualização de cada período.

Tratamento:

Exibir o resultado da expressão N630 (8) * 0,15
	MFS-18708		VALOR DO IMPOSTO DEVIDO	Texto	S	N	0,00	Permite que o usuário visualize o valor do imposto de cada período.

Tratamento:

Exibir o valor do imposto corresponde a linha 3 do registro N630A, N630B ou N630C.	MFS-18708		LIMITE DE 4% SOBRE O IMPOSTO DEVIDO	Texto	S	N	0,00	Permite que o usuário visualize o limite de 4% calculado sobre o imposto devido de cada período.

Tratamento:
Exibir o resultado da expressão N630 (3) * 0,04
	MFS-18708		VALOR DO PDTI/PDTA	Texto	S	N	0,00	Permite que o usuário visualize o valor do incentivo PDTI/PDTA do período.

Tratamento:

Exibir o valor do PDTI/PDTA corresponde a linha 9 do registro N630A, N630B ou N630C.	MFS-18708		LIMITE DE 4% COM PDTI/PDTA	Texto	S	N	0,00	Permite que o usuário visualize o limite de 4% com a dedução do incentivo PDTI/PDTA do  período.

Exibir o resultado da expressão LIMITE DE 4% SOBRE O IMPOSTO DEVIDO - VALOR DO PDTI/PDTA	MFS-18708		VALOR UTILIZADO DO PAT DE PERÍODOS ANTERIORES	Texto	S	N	0,00	Permite que o usuário visualize o valor de PAT que foi utilizado dos períodos anteriores (dentro do período que está sendo processado).	MFS-18708		VALOR DO PAT ATUALIZADO	Texto	S	N	0,00	Permite que o usuário visualize o valor do PAT atualizado a linha 8 do registro N630A, N630B ou N630C do período.	MFS-18708		VALOR DO PAT DISPONÍVEL NESTE PERÍODO PARA USO POSTERIOR	Texto	S	N	0,00	Permite visualização do valor do PAT não utilizado no período.

Tratamento:

O valor exibido neste campo corresponde ao valor não utilizado no período do limite de 15%.

	MFS-18708		
(*) Não exibir a descrição na tela.