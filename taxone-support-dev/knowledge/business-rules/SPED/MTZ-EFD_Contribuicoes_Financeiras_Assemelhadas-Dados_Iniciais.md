# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Dados_Iniciais

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Dados_Iniciais.doc

TITLE   \* MERGEFORMAT EFD - Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas - Dados Iniciais 


DOCUMENTO DE REQUISITO 

DR	Nome	Descrição		OS3810-A	EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Parametrização por Conta Contábil	Essa OS tem por objetivo a geração dos dados do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Trata-se da escrituração digital dos tributos PIS e COFINS para as instituições financeiras, seguradoras, entidades de previdência privada, operadoras de planos de assistência à saúde e assemelhadas, conforme Ato Declaratório Executivo nº. 65 de 20/12/12.		OS3810-E	EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Parametrização por Conta Contábil	Inclusão do Parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” na tela de Dados Iniciais.		CH22781_2013	Tratamento campo “Contabilista Responsável”	Alteração no campo Contabilista Responsável permitindo a alteração do campo mesmo depois de salvar os dados.		OS4549	EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas	Esta OS tem como objetivo melhorar a performance na geração do bloco I. Passaremos a considerar a SAFX02 e SAFX80 quanto a busca de informações referente aos saldos, ao invés de considerar os lançamentos SAFX01.		OS4322	EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas	Esta OS tem como objetivo automatizar o processo de geração do registro M350. Folha de Salários.		MFS- 761087	EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Parametrização por Conta Contábil	O objetivo desta solicitação é incluir um parâmetro na tela de dados iniciais referente ao Registro 0110 (Regimes de Apuração da Contribuição Social e de Apropriação de Crédito) para a apuração da contribuição com base na alíquota específica.		


Cód.	


Descrição	


DR		RN01	Deverá ser criada uma tela chamada “Dados Iniciais”. Essa tela é semelhante a tela de Dados Iniciais do módulo EFD – Escrituração Fiscal Digital das Contribuições.

Essa tela será responsável pela parametrização das informações iniciais para a geração do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas.	OS3810-A		RN02	Criar uma tela para parametrização de alguns dados gerais que serão necessários para a geração do arquivo. Deverá ser feita inicialmente esta parametrização por estabelecimento, obedecendo à regra de geração centralizada, deve-se parametrizar o Estabelecimento centralizador. 

Localização: Grupo ’! Sped ’! EFD   Contribuições Financeira / Assemelhada ’! Parâmetros à Dados Iniciais

Serão disponibilizados na tela os seguintes campos:


Estabelecimento: será exibido o estabelecimento selecionado no Manager. Caso nenhum estabelecimento esteja selecionado no Manager, o sistema permitirá que o usuário selecione o Estabelecimento de acordo com a Empresa previamente selecionada no Manager. O estabelecimento será exibido/selecionado no formato Código do Estabelecimento + Descrição do Estabelecimento. Exemplo: 001 – Estabelecimento 001. Campo obrigatório de preenchimento.
Contabilista Responsável: o usuário pode selecionar o Contabilista Responsável pela empresa. A informação será recuperada do cadastro de Responsável pelas Informações do módulo Parâmetros (menu: Requisitos Legais >> Responsável por Informações). Campo obrigatório de preenchimento.

Nome: Tipo de Contribuição Apurada no Período
             Conteúdo: Criar lista de valores conforme abaixo

             1 – Apuração da Contribuição Exclusivamente a Alíquota Básica 
2 – Apuração da Contribuição a Alíquotas Específicas (Diferenciadas e/ou por Unidade de Medida de Produto)

Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS: campo do tipo checkbox onde o usuário poderá indicará se deseja ou não Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS (já existe no EFD-Contribuições normal).
Utiliza saldo por centro de custo: Este campo deverá ser um “checkbox” default “não selecionado” e não obrigatório, deverá considerar SAFX80 caso selecionado. Considerar valor default “não selecionado” para os registros existentes em tabela.

Período de encerramento: Este campo será um “Dropdown”, não obrigatório, irá listar todas as opções: “Trimestral,” “Semestral”, “Anual”. Como default irá apresentar a opção “Anual” como padrão, assim para registros já existentes em tabela.

Multiempresa: nesse flag, o usuário deverá definir se a informação da parametrização será multi-empresa ou não. Caso o parâmetro esteja desmarcado, no campo “Empresa/Estabelecimento”, serão exibidos os Estabelecimentos da empresa selecionada no Manager. Caso o parâmetro esteja selecionado, no campo “Empresa/Estabelecimento”, serão exibidos as Empresas do sistema. Campo não obrigatório de preenchimento. Quando o usuário replicar as informações para os estabelecimentos, as informações de Dados Iniciais serão replicadas para os estabelecimentos selecionados. Caso o usuário replique para as empresas, as informações de Dados Iniciais serão replicadas para todos os estabelecimentos das empresas selecionadas.
Replicar para as Empresas/Estabalecimentos: este flag será habilitado somente quando o parâmetro multiempresa for selecionado. Quando selecionado, habilita a lista Empresa/Estabelecimento para que seja possível a réplica da parametrização.
Empresa/Estabelecimento: nesse campo, o usuário deverá selecionar quais empresas ou estabelecimentos (dependendo do parâmetro Multi-Empresa) deverão ser selecionados para geração do arquivo da EFD-Contribuições Financeiras e Assemelhadas. Serão exibidos os estabelecimentos ou empresas que o usuário possui permissão de acesso. Campo não obrigatório de preenchimento.	OS3810-A/OS4549
OS3810-E
MFS-761087
		RN03	Deverá ser criado um relatório de conferência para essa tela de parametrização.	OS3810-A		RN04	Regra para campo Contabilista Responsável:

Permitir o usuário informar o código do Responsável manualmente ou pela opção de busca à informação da tela “Responsável por Informações” localizado em Módulo Básicos >> Parâmetros >> Requisitos Legais.

Este campo deve vir por default sem preenchimento e é obrigatória a informação, caso não seja preenchido emitir a mensagem na tela: “Responsável deve ser informado”.

Quando a informação for salva e inserida na tabela dos dados iniciais, esse campo NÃO deve ser bloqueado para alteração.	CH22781_2013		RN05	Registro M350 – PIS/PASEP – Folha de Salários

Campo: “Considerar Parametrização de Conta Contábil para Geração do M350"

Se selecionado usuário define que a geração será automática  (Módulo Sped ( EFD - Contribuição Financeira/Assemelhada ( Parâmetros ( Parametrização Folha de Salários.

Se não, a geração do registro será “Manual”, padrão existente no sistema (Módulo Sped ( EFD - Contribuição Financeira/Assemelhada ( Obrigações( Folha de Salário (M350))


Campo do tipo: checkbox

Defaul: não selecionado.
	OS4322		
Considerações deste modelo:


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO