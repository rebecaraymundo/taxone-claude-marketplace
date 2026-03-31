# MTZ-Emissao_dos_relatorios_Analitico_e_Sintetico

> Fonte: MTZ-Emissao_dos_relatorios_Analitico_e_Sintetico.doc

SPED CONTÁBIL – Geração dos relatórios Analíticos e Sintéticos


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		CH8425_2013	Correção na geração dos relatórios analíticos e sintéticos.
	Correção na recuperação dos valores para a geração dos relatórios analíticos e sintéticos.
		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Descrição da Regra de Negócio 00	OSNNNN		RN01	Alteração na recuperação dos valores demonstrados nos relatórios analíticos e sintéticos na geração CENTRALIZADA :

Na geração dos valores dos relatórios analíticos e sintéticos da geração CENTRALIZADA, deve ser recuperado de acordo com a parametrização realizada no menu: “Plano de contas Referencial x Plano de contas da Empresa” pertinentes ao saldo final do período solicitado na geração do relatório. Deverá ser recuperado os saldos das SAFX02 de todos os estabelecimentos, no caso de haver mais que uma SAFX02 (além do CENTRALIZADOR) os saldos deverão ser sumarizados para a obtenção dos valores demonstrados. Na hipótese de NÃO HAVER INFORMAÇÕES NA SAFX02 nem para o estabelecimento CENTRALIZADOR e nem para nenhum estabelecimento CENTRALIZADO, deverá ser verificado os saldos da SAFX01 tanto do estabelecimento CENTRALIZADOR quanto do estabelecimento CENTRALIZADO para a sumarização dos valores.
	CH8425_2013		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN