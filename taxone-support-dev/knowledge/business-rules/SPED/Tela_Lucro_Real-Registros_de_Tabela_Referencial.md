# Tela_Lucro_Real-Registros_de_Tabela_Referencial

> Fonte: Tela_Lucro_Real-Registros_de_Tabela_Referencial.doc

THOMSON REUTERS

Tela Lucro Real – Registro de Tabela Referencial e Bloco K 
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		31/08/2017	MFS-12700	Criação do Documento 	Alessandra Cristina Navatta		09/10/2017	MFS-14005	Registros Bloco L (L100 e L300) 	Alessandra Cristina Navatta		10/09/2018	MFS-20783	Alteração dos campos exibidos em tela do bloco K. Será considerado, os campos que são apresentados no meio magnético desses registros.

Ajuste na recuperação e exibição dos dados (dos registros L100,L300,K155 e K355) na tela Lucro Real >> Demonstração.	Alessandra Cristina Navatta		

Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc524437838" 1.	INTRODUÇÃO	 PAGEREF _Toc524437838 \h 3
 HYPERLINK \l "_Toc524437839" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc524437839 \h 3
 HYPERLINK \l "_Toc524437840" 3.	TELAS	 PAGEREF _Toc524437840 \h 3
 HYPERLINK \l "_Toc524437841" 3.1.	Pesquisa de Registros	 PAGEREF _Toc524437841 \h 3
 HYPERLINK \l "_Toc524437842" 3.2.	Regras dos Campos Tela Principal	 PAGEREF _Toc524437842 \h 5


	


INTRODUÇÃO

Objetivo desta especificação é criar a tela de Resultados dos Registros Balanço Patrimonial (L100), Demonstrativo do Resultado do Lucro Líquido (L300) e do Bloco K (K155-K156,K355-K356).

DOCUMENTOS DE REFERÊNCIA

Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
Tela_Abertura_de_Apuracao.doc
MTZ_Processamento_em_Lote.docx


TELAS


Pesquisa de Registros

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Lucro Real >> Demonstração
Título da tela: Lucro Real


Condições Gerais:

Quando o usuário acessar a tela de consulta, apresentar todos os registros contidos na tabela de Informações ECF.  

Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.

Campo	Tipo	Regra		Estabelecimento	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do  Estabelecimento.		Exercício	Texto
AAAA	

O usuário poderá informar o exercício. 

		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código-Descrição)	Aplicar a RNG00004 (Versão de Layout)		Forma de Tributação	Lista
(Código - Descrição)	Exibe as opções abaixo:

-Lucro Real, Lucro Presumido, Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 


		Apuração	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral

		

Regras dos Campos Tela Principal

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Lucro Real >> Demonstração
Título da tela: Lucro Real

Considerações Gerais: 

Para os registros K155,K355,L100 e L300:


As opções correspondentes aos períodos de apuração que possuem tipo de receita igual a “Receita Bruta” selecionada através das telas “Abertura de Apuração” ou “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, não devem ser exibidas. Esta regra é a mesma regra realizada na geração desses registros no meio magnético.


As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Dados Gerais 
		Estabelecimento
	Texto
	S	N	Tipo – Código - Descrição	Permite que o usuário visualize o Estabelecimento da apuração que foi recuperada	MFS-12700		Exercício	Texto	S	N	AAAA	Permite que o usuário visualize o ano correspondente à demonstração dos resultados.

	MFS-12700		Data Inicial	Texto
	S	N	
DD/MM/AAAA 
	Permite que o usuário visualize a data inicial, referente ao registro selecionado na tabela das informações ecf.	MFS-12700		Versão	Texto	S	N	Código - Descrição	Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar a RNG00004 (Versão de Layout)	MFS-12700		Forma de Tributação	Texto
	S	N	Descrição	Permite que o usuário visualize a forma de tributação, referente ao registro selecionado na tabela das informações ecf.
	MFS-12700		Apuração	Texto
	S	N	Descrição	Permite que o usuário visualize a apuração, referente ao registro selecionado na tabela das informações ecf.
	MFS-12700		Data Final do Último Período da Escrituração	Texto	S	N	DD/MM/AAAA 	Permite que o usuário visualize a data final do último período da escrituração. 

Tratamento:

Com base na escrituração recuperada, considerar neste campo a data final do último período da escrituração.
	MFS-12700		Subtítulo: (*)
Filtros de Registro/Apurações		Registro	Lista	S	S	Código 	Tratamento:Exibe o título com o código do registro conforme processado.Opções Válidas:
K155
K355
L100
L300Exibir em ordem a apresentação dos registros. Caso não tenha informações referente ao registro, o mesmo não deve ser exibido na lista.
	MFS-14005
MFS-12700		Apuração
	Lista	S	S	Descrição	Opções de ‘Título’ de apurações válidas:

Anual
Janeiro
Fevereiro
Março
Abril
Maio
Junho
Julho
Agosto
Setembro
Outubro
Novembro
Dezembro
1º Trimestre
2º Trimestre
3º Trimestre
4° Trimestre


As opções serão visualizadas de acordo com as seguintes regras:

Forma de Tributação = Real ou Imune de IRPJ ou Isenta do IRPJ e Apuração Anual

Anual:

-No processo de Importação de Saldos, quando existir um período de apuração com forma de tributação = Real ou Imune de IRPJ ou Isenta do IRPJ e Apuração = Anual, deverá ser exibida a opção Anual.

Mensal:

- No processo de Importação de Saldos, para cada período de apuração encontrado com forma de tributação = Real ou Imune de IRPJ ou Isenta do IRPJ e Apuração = Anual.

Forma de Tributação = Real ou Presumido ou Imune de IRPJ ou Isenta do IRPJ e a Apuração Trimestral: 

- No processo de Importação de Saldos, para cada período de abertura encontrado com trimestre, exibir a opção do trimestre correspondente. Se todos os períodos de abertura de apuração do exercício gerados forem trimestrais, a opção Anual não deverá ser exibida na tela.

Conteúdo:

Deverão respeitar as regras abaixo e as regras de processamento no documento MTZ_Processamento_em_Lote.docx


	 MFS-12700		‘TÍTULO 	Texto	S	N	Código - Descrição	Tratamento:

Exibe o código e a descrição do registro.
	MFS-12700		Apenas Registros com movimento	check-box	S	S	Default:
Desmarcado	Permite que o usuário escolha a forma de exibição das informações nas abas, se deseja visualizar apenas os registros que possuam movimento ou todos os registros.


Tratamentos:
Quando o usuário selecionar a opção “Apenas Registros com Movimento”, apresentar nas abas os registros cujos campos “Valor do Saldo Inicial” ou “Valor do Saldo Final” sejam maiores que zero.
Quando o usuário selecionar a opção “Todos”, apresentar nas abas apenas os registros todos os registros.
	MFS-12700		Grid Principal do Registro K155(*)Título: (*)
Código do Registro - Descrição		

Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.

Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-12700		Regras de Campos que serão exibidos na grid (*)		Cód. da Conta Contábil
	Texto	S	N	Código 	Permite ao usuário visualizar o código da conta contábil associada à conta referencial recuperada.
Tratamento:

Apresentar os registros na GRID em ordem crescente (código da conta).	MFS-12700
MFS-20783		Desc. da Conta Contábil	Texto	S	N	Descrição	Permite ao usuário visualizar a descrição  da conta contábil associada à conta referencial recuperada.
	MFS-12700
MFS-20783		Cód. do Centro de Custo	Texto	S	N	Código 	Permite ao usuário visualizar o código do centro de custo associados à conta referencial recuperada.
Tratamento:
Apresentar os registros na GRID em ordem crescente (código do centro de custo).	MFS-12700
MFS-20783		Desc. do Centro de Custo	Texto	S	N	Descrição	Permite ao usuário visualizar a descrição do centro de custo associados à conta referencial recuperada.	MFS-12700
MFS-20783		Saldo Inicial 	Texto	S	N	0,00	Permite ao usuário visualizar o saldo inicial da conta contábil.

Tratamento:

Recuperar o saldo inicial que será utilizado no meio magnético (se o saldo foi alterado pelo usuário, considerar o saldo inicial informado, caso contrário o saldo inicial calculado).

	MFS-12700
MFS-20783		Ind. Do Saldo Inicial	Texto	S	N	D ou C	Permite ao usuário visualizar o indicador do saldo inicial da conta contábil.
	MFS-12700
MFS-20783		Total de Débitos	Texto	S	N	0,00	Permite ao usuário visualizar o total de débito da conta contábil.	MFS-12700
MFS-20783		Total de Créditos	Texto	S	N	0,00	Permite ao usuário visualizar o total de créditos da conta contábil.	MFS-12700
MFS-20783		Saldo Final 	Texto	S	N	0,00	Permite que o usuário visualize o valor do saldo final que foi considerado desta conta contábil e centro de custo, associados à da conta referencial.

Tratamento:

Recuperar o saldo final que será utilizado no meio magnético (se o saldo foi alterado pelo usuário, considerar o saldo final informado, caso contrário, o saldo final calculado).

Concatenar o valor com o indicador do saldo.	MFS-12700
MFS-20783		Ind. Do Saldo Final	Texto	S	N	C ou D	Permite ao usuário visualizar o indicador do saldo final da conta contábil.
	MFS-12700
MFS-20783		Tela Secundária do registro K156(*)Título: ( *)
Código -  Descrição do Registro		Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.


Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-12700
MFS-20793		Cód. da Conta Referencial	Texto	S	N	Código 	Permite que o usuário visualize os códigos das contas referenciais. Tratamento:Deve ser permitida somente a visualização das contas referenciais analíticas.Apresentar os registros na GRID em ordem crescente (código da conta).	MFS-12700
MFS-20793		Desc. Da Conta Referencial	Texto	S	N	Descrição	Permite que o usuário visualize as descrições das contas referenciais. 	MFS-12700
MFS-20793		Saldo Final	Texto	S	N	0,00	Permite que o usuário visualize o valor do saldo final da conta referencial.


Tratamento:

Recuperar o saldo final que será utilizado no meio magnético (se o saldo foi alterado pelo usuário, considerar o saldo final informado, caso contrário o saldo final calculado).

	MFS-12700
MFS-20793		Ind. Do Saldo Final	Texto	S	N	C ou D	Permite que o usuário visualize o indicador do saldo final da conta referencial.

	MFS-12700
MFS-20793		Grid Principal do Registro K355(*)Título: (*)
Código do Registro - Descrição 		

Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.

Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro. 	MFS-20783		Regras de Campos que serão exibidos na grid (*)		Conta Contábil
	Texto	S	N	Código 	Permite ao usuário visualizar a conta contábil associada à conta referencial recuperada.

Tratamento:

Apresentar os registros na GRID em ordem crescente (código da conta).
	MFS-20783		Desc. da Conta Contábil	Texto	S	N	Descrição	Permite ao usuário visualizar a descrição da conta contábil associada à conta referencial recuperada	MFS-20783		Cód. Do Centro de Custo	Texto	S	N	Código 	Permite ao usuário visualizar o centro de custo associado à conta referencial recuperada.

Tratamento:

Apresentar os registros na GRID em ordem crescente (código do centro de custo).	MFS-20783		Desc. do Centro de Custo	Texto	S	N	Descrição	Permite ao usuário visualizar a descrição do centro de custo associado à conta referencial recuperada	MFS-20783		Saldo Final 	Texto	S	N	0,00	Permite que o usuário visualize o valor do saldo final que foi considerado desta conta contábil e centro de custo, associados à da conta referencial.

Tratamento:

Recuperar o saldo final que será utilizado no meio magnético (se o saldo foi alterado pelo usuário, considerar o saldo final informado, caso contrário, o saldo final calculado).
	MFS-20783		Ind. Do Saldo Final	Texto	S	N	C ou D	Permite que o usuário visualize o indicador do saldo final da conta referencial.

	MFS-12700
MFS-20793		Tela Secundária do registro K356(*)Título: (*)
Código -  Descrição do Registro		Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.


Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-20793		Cód. da Conta Referencial	Texto	S	N	Código 	Permite que o usuário visualize o código das contas referenciais . Tratamento:Deve ser permitida somente a visualização das contas referenciais analíticas.Apresentar os registros na GRID em ordem crescente (código da conta).	MFS-20793		Desc. da Conta Referencial	Texto	S	N	Descrição	Permite que o usuário visualize a descrição dascontas referenciais . 	MFS-20793		Saldo Final	Texto	S	N	0,00
	Permite que o usuário visualize o valor do saldo final da conta referencial.

Tratamento:

Recuperar o saldo final que será utilizado no meio magnético (se o saldo foi alterado pelo usuário, considerar o saldo final informado, caso contrário o saldo final calculado).
	MFS-20793		Ind. Do Saldo Final	Texto	S	N	C ou D	Permite que o usuário visualize o indicador do saldo final da conta referencial.

	MFS-12700
MFS-20793		Grid Principal do Registro L100 e L300(*)Título: (*)
Código do Registro - Descrição 		

Pesquisar	Botão	-	-	-	Permite ao usuário pesquisar um registro.

Tratamentos:

A pesquisa pode ser realizada pelos campos chave do registro.	MFS-14005		Cód. da Conta Referencial	Texto	S	N		Permite que o usuário visualize os códigos das contas referenciais, em ordem crescente	MFS-14005		Desc. da Conta Referencial	Texto	S	N		Permite que o usuário visualize a descrição das contas referenciais.

	MFS-14005		Tipo de Conta	Texto	S	N		Permite que o usuário visualize o Tipo da 
Referencial.

Opções Válidas:
-S 
-A	MFS-14005		Nível	Texto	S	N		Permite que o usuário visualize o nível da conta referencial.
	MFS-14005		Valor do Saldo Inicial	Texto	S	N	00,00	Permite que o usuário visualize o valor do saldo inicial da conta referencial

Tratamentos:

Só apresentar este campo para os registros L100, P100 e U100
	MFS-14005		Ind. do Saldo Inicial	Texto	S	N		Permite que o usuário visualize o indicador  de débito ou crédito do valor  do saldo inicial da conta referencial.
Valores Válidos:

-‘D’
-‘C’
Tratamentos:

Só apresentar este campo para os registros L100, P100 e U100
	MFS-14005		Valor do Saldo Final	Texto	S	N	00,00	Permite que o usuário visualize o valor do saldo final  da conta referencial	MFS-14005		Ind. do Saldo Final	Texto	S	N		Permite que o usuário visualize o indicador  de débito ou crédito do valor do saldo final da conta referencial.
Valores Válidos:

-‘D’
-‘C’
	MFS-14005		 
Subtítulo:(*)
Detalhamento 
		Cód. da Conta Contábil	Texto	S	N		Permite ao usuário visualizar os códigos da contas contábeis associadas à conta referencial recuperada.

Exibir auto filter.	MFS-14005		Desc. da Conta Contábil	Texto	S	N		Permite ao usuário visualizar a descrição da conta contábil associadas à conta referencial recuperada.

Exibir auto filter.	MFS-14005		Cód. do Centro de Custo	Texto	S	N		Permite ao usuário visualizar o código do centro de custo associados à conta referencial recuperada.

Exibir auto filter.	MFS-14005		Desc. do Centro de Custo	Texto	S	N		Permite ao usuário visualizar a descrição do centro de custo associados à conta referencial recuperada.
Exibir auto filter.	MFS-14005		Valor do Saldo Inicial	Texto	S	N		Permite que o usuário visualize o valor do saldo inicial que foi considerado desta conta contábil e centro de custo, associados à conta referencial.

Tratamentos:

Só apresentar este campo para os registros L100, P100 e U100. 
	MFS-14005		Ind. do Saldo Inicial	Texto	S	N		Permite que o usuário visualize o indicador do saldo inicial que foi considerado desta conta contábil e centro de custo, associados à conta referencial.

Tratamentos:

Só apresentar este campo para os registros L100, P100 e U100.

	MFS-14005		Valor do Saldo Final	Texto	S	N		Permite que o usuário visualize o valor do saldo final que foi considerado desta conta contábil e centro de custo, associados à conta referencial.

	MFS-14005		Ind. do Saldo Final	Texto	S	N		Permite que o usuário visualize o indicador do saldo final que foi considerado desta conta contábil e centro de custo, associados à conta referencial.
	MFS-14005		(*) Não exibir a descrição na tela.