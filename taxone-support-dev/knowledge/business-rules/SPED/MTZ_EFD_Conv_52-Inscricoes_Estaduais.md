# MTZ_EFD_Conv_52-Inscricoes_Estaduais

> Fonte: MTZ_EFD_Conv_52-Inscricoes_Estaduais.doc

Módulo Sped Fiscal – Manutenção das Inscrições Estaduais – 
Convênio ICMS 52/2005


Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Geração – Conv ICMS 52/05 ( Inscrições Estaduais

DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS3335-A	Telecom-Geração da EFD p/as UF’s dos tomadores do serviço.	Telecom - Geração da EFD p/as UF’s dos Tomadores dos Serviços de TV por Assinatura via Satélite (atendimento ao Convênio ICMS 52/2005).  	24/06/2011 (criação do docto) 		MFS-15153	Inclusão de parâmetro para gerar o Registro 1400	Inclusão de parâmetro para gerar o Registro 1400 de acordo com o Convênio 52/05. (Ver RN01)	29/01/2018		
REGRAS DE NEGÓCIO


Regra 	Descrição	DR		RN00	
Parametrização criada pela OS3335-A, para possibilitar a geração dos arquivos da EFD p/as UF’s dos tomadores do serviço, no caso das empresas de Telecom obrigadas ao Convênio 52/2005.

Campo Estabelecimento ( Este campo é uma lista com a relação de todos os estabelecimentos da empresa que atendam aos seguintes critérios:

Estabelecimentos parametrizados no módulo Sped Fiscal (menu “Dados Iniciais”);
Estabelecimentos c/o parâmetro “Obrigado ao Convênio ICMS 52/2005” = S;

Campo UF ( Lista de todas as UF’s, com exceção da UF do estabelecimento;

Campo Inscrição Estadual ( Campo com 14 posições onde será informada a inscrição estadual da UF.

Para cada estabelecimento, poderão ser cadastradas ‘n’ inscrições estaduais.

A inscrição estadual é por UF, logo, para cada UF só poderá ser cadastrada uma única inscrição.

	


OS3335-A		RN01	Grupo Registro 1400 – Informação sobre Valores Agregados

Tipo de Geração (formato Radio Button Group) com as opções:

Padrão
Específica por UF

Na mesma linha da opção “Padrão” deverá conter a opção em Check Box para informar “Calcular Valores por Produto” desmarcada por default e só será utilizada para esse tipo de geração.

Na mesma linha da opção “Específica por UF” deverá conter a opção em Check Box para informar “Utilizar a parametrização de produtos (DIPAM-B – SP)” desmarcada por default e só será utilizada para esse tipo de geração.
	MFS-15153