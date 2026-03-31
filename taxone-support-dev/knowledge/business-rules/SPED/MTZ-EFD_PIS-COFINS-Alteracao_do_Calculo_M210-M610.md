# MTZ-EFD_PIS-COFINS-Alteracao_do_Calculo_M210-M610

> Fonte: MTZ-EFD_PIS-COFINS-Alteracao_do_Calculo_M210-M610.doc

TITLE   \* MERGEFORMAT EFD PIS/COFINS - Alteração do Cálculo M210/M610


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS3551	EFD PIS/COFINS - Alteração na geração do campo 08 dos registro M210 e M610	Ao gerar os registros M210/M610, o produto calcula os créditos através da sumarização do Valor de Imposto referente ao PIS e ao COFINS. Ocorre que o validador ao validar o arquivo gerado, não considera essa sumarização, fazendo o cálculo do mesmo aplicando a alíquota sobre a Base de Cálculo de PIS ou de COFINS.

Essa diferença no momento da validação do arquivo está causando erros no validador, visto que o produto calcula o imposto item a item, enquanto que o validador considera o cálculo da alíquota aplicável sobre a Base de Cálculo, o que gera diferença de centavos.		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN01	 Ao gerar os registros M210 e M610 deverão ser exibidas as seguintes mensagens no Log de Processos da rotina de Geração dos Registros do EFD PIS/COFINS, para os casos em que forem encontradas divergências.	OS3551		RN02	
===== Registro M210 ============================================================================

Advertência: O valor do crédito de PIS, apurado com base na somatória dos valores de PIS dos itens dos documentos fiscais do período, gerou um valor menor que o apurado com base na aplicação da alíquota sobre a base de cálculo. O crédito lançado no EFD-PIS/PASEP-COFINS será o resultante da aplicação da alíquota sobre a base de cálculo do crédito.

OBS: além disso, deverá exibir a chave dos registros que tiveram divergência.	OS3551		RN03	
===== Registro M610 ============================================================================

Advertência: O valor do crédito de COFINS, apurado com base na somatória dos valores de COFINS dos itens dos documentos fiscais do período, gerou um valor menor que o apurado com base na aplicação da alíquota sobre a base de cálculo. O crédito lançado no EFD-PIS/PASEP-COFINS será o resultante da aplicação da alíquota sobre a base de cálculo do crédito.

OBS: além disso, deverá exibir a chave dos registros que tiveram divergência.	OS3551		


Considerações deste modelo:


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN