# MTZ_EFD_Manutencao_Registro_E115_Valores_Declaratorios-PIM

> Fonte: MTZ_EFD_Manutencao_Registro_E115_Valores_Declaratorios-PIM.doc

Módulo Sped Fiscal – Manutenção do Registro E115/1925 – Valores Declaratórios

(opção Geração – PIM)


Localização: Menu SPED, Módulo EFD – Escrituração Fiscal Digital, item Geração – PIM ( Manutenção ( Registro E115 / 1925 (Valores Declaratórios)

DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS4593-B	Geração das Subapurações p/o Sped Fiscal da opção “PIM”	Alterações no módulo Sped Fiscal para gerar o arquivo da opção “PIM” com os registros das subapurações (1900 e “filhos”)	17/09/2014

(criação do doc)		MFS8105	Aumento do campo Sequencial	Aumento do tamanho do campo Sequencial de 2 para 4 posições	23/03/2017		
REGRAS DE NEGÓCIO


Regra 	Descrição	DR		RN00	
Regras gerais


		
RN01	
Campo “Sequencial”:

Alteração da MFS8105: O tamanho deste campo foi aumentado de 2 para 4 posições.
	
MFS8105		


RN02	Campo “Subapuração do Sped Fiscal”:

(campo incluído na OS4593-B, Set/2014)

Este campo é uma lista das subapurações do Sped Fiscal (conforme Ato Cotepe 22/2010) + opção  “branco”, conforme o exemplo abaixo:


 Subapuração 1

 Subapuração 2

 Subapuração 3

 Subapuração 4

 Subapuração 5

 Subapuração 6


Default   ( <branco> 
O campo é de preenchimento não obrigatório, e internamente, poderá ter os valores:  nulo, 1, 2, 3, 4, 5 ou 6.
	


OS4593-B