# MTZ_EFD_Manutencao_Registro_E115_Valores_Declaratorios

> Fonte: MTZ_EFD_Manutencao_Registro_E115_Valores_Declaratorios.doc

Módulo Sped Fiscal – Manutenção do Registro E115 – Valores Declaratórios


Localização: Menu SPED, Módulo EFD – Escrituração Fiscal Digital, item Geração ( Manutenção ( Registro E115 (Valores Declaratórios)

DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS2931-F	Geração dos Novos Registros das Sub Apurações do ICMS	O objetivo desta OS é efetuar a geração dos novos registros do Bloco 1 (1900 e “filhos”) referentes às Sub Apurações do ICMS. Nesta OS também foram especificadas diversas alterações no Mastersaf para possibilitar a geração dos novos registros.  	03/12/2010		OS4261	Alterações do Ato Cotepe 43/2013	Aumento na quantidade das sub-apurações.	01/11/2013		MFS8105	Aumento do campo Sequencial	Aumento do tamanho do campo Sequencial de 2 para 4 posições	23/03/2017		
REGRAS DE NEGÓCIO


Regra 	Descrição	DR		RN00	
Regras gerais

(espaço reservado para regras genéricas, que não dizem respeito a campos específicos)

		

RN01	
Campo “Sequencial”:

Alteração da MFS8105: O tamanho deste campo foi aumentado de 2 para 4 posições.

	

MFS8105		


RN02	Campo “Sub-Apuração do Sped Fiscal”:  
(campo incluído pela OS2931-F, em Dez/2010)

Este campo é uma lista das sub-apurações do Sped Fiscal (conforme Ato Cotepe 22/2010),  mais a opção  “branco”, conforme o exemplo abaixo:

Alteração da OS4261: O Ato Cotepe 43/2013 aumentou a quantidade de sub-apurações de três para seis.


 Sub-Apuração 1

 Sub-Apuração 2

 Sub-Apuração 3

 Sub-Apuração 4

 Sub-Apuração 5

 Sub-Apuração 6


Default   ( <branco> 
O campo é de preenchimento não obrigatório, e internamente, poderá ter os valores: nulo, 1, 2, 3, 4, 5 ou 6.
	


OS2931-F
OS4261