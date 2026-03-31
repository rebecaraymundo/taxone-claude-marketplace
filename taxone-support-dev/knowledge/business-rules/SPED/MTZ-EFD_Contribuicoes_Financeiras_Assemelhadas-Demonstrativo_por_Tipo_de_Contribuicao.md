# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Demonstrativo_por_Tipo_de_Contribuicao

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Demonstrativo_por_Tipo_de_Contribuicao.doc

TITLE   \* MERGEFORMAT EFD Contribuições Financeiras e Assemelhadas - Demonstrativo por Tipo de Contribuição 


DOCUMENTO DE REQUISITO 

DR	Nome	Descrição		OS3810-D	 TITLE   \* MERGEFORMAT EFD Contribuições Financeiras e Assemelhadas - Demonstrativo por Tipo de Contribuição	Essa OS tem por objetivo permitir a geração do meio magnético do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas e permitir a geração dos Demonstrativos por Contribuição e Natureza da Receita.		MFS25094	Andréa Rocha	Inclusão dos campos “Vlr Tot. Ajustes Acréscimo BC”, “Vlr Tot. Ajustes Redução BC” e “Vlr BC da Contribuição” nos registros M210, e M610 
Os registros filhos dos M210, e M610 hoje não são apresentados no relatório. Logo os novos registros filhos M215 e M615 não serão demonstrados no relatório.		


Cód.	


Descrição	


DR		RN01	Deverá ser criada uma tela chamada “Demonstrativo da Apuração por Tipo de Contribuição”. 

Essa tela será responsável pela geração do relatório onde serão demonstradas as informações da apuração por Tipo de Contribuição.

O menu “Demonstrativos” ficará acima do menu “Geração do Meio Magnético”.	OS3810-D		RN02	Ao clicar no menu, o sistema irá abrir a tela “Selecionar Apuração” onde o sistema irá disponibilizar todas as apurações para que o usuário selecione. Essa funcionalidade é semelhante ao módulo EFD Contribuições.

Para gerar o relatório, o usuário deverá selecionar a apuração desejada antes de selecionar os critérios de pesquisa da tela seguinte.	OS3810-D		RN03	Serão disponibilizados na tela os seguintes campos:

Registro: nesse campo, o usuário deverá selecionar quais registros deverão ser gerados. Por default, todos os registros informados nessa tela estarão selecionados.
M200 - Consolidação da Contribuição para o PIS/PASEP do Período
M210 - Detalhamento da Contribuição para o PIS/PASEP do Período
M600 - Consolidação da Contribuição para a Seguridade Social - COFINS do Período
M610 - Detalhamento da Contribuição para a Seguridade Social - COFINS do Período

Caso o usuário desmarque os registros M200 ou M600, os seus registros filhos M210 e M610 serão automaticamente desmarcados, e o sistema não irá permitir que eles sejam marcados sem a marcação dos registros pai.	OS3810-D		RN04	Após gerar o relatório, os campos serão gerados da seguinte maneira:

	OS3810-D		RN05	Serão gerados os seguintes campos referentes aos seguintes registros:

M200
Vlr. Tot. Contrib. N. Cum. Per.
Vlr. Tot. Créd. Descto. Período
Vlr. Tot. Créd. Desc. Per. Ant.
Vlr. Tot. Contrib. N. Cum. Devida
Vlr. Ret. Fonte Deduzida Per.
Vlr. Outras Deduções Per.
Vlr. Total Contrib. N. Cum. Rec/Pag
Vlr. Total Contrib. Cum. Período
Vlr. Retido Fonte Ded. Per.
Vlr Outras Deduções Per.
Vlr. Total Contrib. N. Cum. À Rec.Pag
Vlr Total Contrib. À Rec./Pag Per.
M210
Tipo Contribuição
Vlr. Receita Bruta
Vlr. Base Cálculo
Vlr Tot. Ajustes Acréscimo BC [MFS25094]
Vlr Tot. Ajustes Redução BC [MFS25094]
Vlr BC da Contribuição [MFS25094]
Alíquota PIS (Percentual)
Alíquota do PIS (Reais)
Vlr. Total Contrib.
Vlr. Tot. Ajustes Acréscimo
Vlr. Tot. Ajustes Redução
Vlr. Tot. Contrib. Diferir Período
Vlr. Contrib. Difer. Per. Ant.
Vlr. Total Contribuição
M600
Vlr. Tot. Contrib. N. Cum. Per.
Vlr. Tot. Créd. Descto. Período
Vlr. Total Créd. Desc. Per. Ant.
Vlr. Tot. Contrib. N. Cum. Devida
Vlr. Ret. Fonte Deduzida Per.
Vlr. Outras Deduções Per.
Vlr. Total Contrib. N. Cum. Rec/Pag
Vlr. Tot. Contrib. Cum. Período
Vlr. Retido Fonte Ded. Per.
Vlr. Outras Deduções Per.
Vlr. Total Contrib. N. Cum. à Rec/Pag
Vlr. Total Contrib. à Rec/Pag Per.
M610
Tipo Contribuição
Vlr. Receita Bruta
Vlr. Base Cálculo
Vlr Tot. Ajustes Acréscimo BC [MFS25094]
Vlr Tot. Ajustes Redução BC [MFS25094]
Vlr BC da Contribuição [MFS25094]
Alíquota COFINS (Percentual)
Alíquota do COFINS (Reais)
Vlr. Total Contrib.
Vlr. Tot. Ajustes Acréscimo
Vlr. Tot. Ajustes Redução
Vlr. Tot. Contrib. Diferir Período
Vlr. Contrib. Difer. Per. Ant.
Vlr. Total Contribuição

Essas informações serão recuperadas das telas de Apuração PIS/PASEP (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) e Apuração COFINS (menu: Obrigações >> Manutenção >> Apuração COFINS) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas.	OS3810-D		

Considerações deste modelo:


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN