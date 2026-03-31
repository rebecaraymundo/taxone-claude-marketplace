# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Demonstrativo_por_Tipo_de_Natureza_de_Receita

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Demonstrativo_por_Tipo_de_Natureza_de_Receita.doc

TITLE   \* MERGEFORMAT EFD Contribuições Financeiras e Assemelhadas - Demonstrativo por Tipo de Natureza de Receita 


DOCUMENTO DE REQUISITO 

DR	Nome	Descrição		OS3810-D	 TITLE   \* MERGEFORMAT EFD Contribuições Financeiras e Assemelhadas - Demonstrativo por Tipo de Natureza de Receita	Essa OS tem por objetivo permitir a geração do meio magnético do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas e permitir a geração dos Demonstrativos por Contribuição e Natureza da Receita.		


Cód.	


Descrição	


DR		RN01	Deverá ser criada uma tela chamada “Demonstrativo da Apuração por Tipo de Natureza de Receita”. 

Essa tela será responsável pela geração do relatório onde serão demonstradas as informações da apuração por Tipo de Natureza de Receita.

O menu “Demonstrativos” ficará acima do menu “Geração do Meio Magnético”.	OS3810-D		RN02	Ao clicar no menu, o sistema irá abrir a tela “Selecionar Apuração” onde o sistema irá disponibilizar todas as apurações para que o usuário selecione. Essa funcionalidade é semelhante ao módulo EFD Contribuições.

Para gerar o relatório, o usuário deverá selecionar a apuração desejada antes de selecionar os critérios de pesquisa da tela seguinte.	OS3810-D		RN03	Serão disponibilizados na tela os seguintes campos:

Registro: nesse campo, o usuário deverá selecionar quais registros deverão ser gerados. Por default, todos os registros informados nessa tela estarão selecionados.
M400 – Receitas Isentas ou Não Alcançadas pela Incidência da Contribuição ou Sujeitas a Alíquota Zero ou Suspensão – PIS/PASEP
M410 – Detalhamento das Receitas Isentas ou Não Alcançadas pela Incidência da Contribuição ou Sujeitas a Alíquota Zero ou Suspensão – PIS/PASEP
M800 – Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, sujeitas a alíquota zero ou de vendas com suspensão – COFINS
M810 – Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, sujeitas a alíquota zero ou de vendas com suspensão – COFINS

Caso o usuário desmarque os registros M400 ou M800, os seus registros filhos M410 e M810 serão automaticamente desmarcados, e o sistema não irá permitir que eles sejam marcados sem a marcação dos registros pai.	OS3810-D		RN04	Após gerar o relatório, os campos serão gerados da seguinte maneira:

Serão gerados os seguintes campos referentes aos seguintes registros:

M400
CST
Valor Total da Receita Bruta
Conta Analítica Contábil
Descrição Complementar da Natureza da Receita
M410
Natureza da Receita
Valor da Receita Bruta no Período
Conta Analítica Contábil
Alíquota PIS (Percentual)
M800
CST
Valor Total da Receita Bruta
Conta Analítica Contábil
Descrição Complementar da Natureza da Receita
M810
Natureza da Receita
Valor da Receita Bruta no Período
Conta Analítica Contábil
Alíquota COFINS (Percentual)	OS3810-D		

Considerações deste modelo:


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN