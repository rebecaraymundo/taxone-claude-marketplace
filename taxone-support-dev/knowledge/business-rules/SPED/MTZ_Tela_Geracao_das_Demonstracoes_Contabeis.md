# MTZ_Tela_Geracao_das_Demonstracoes_Contabeis

> Fonte: MTZ_Tela_Geracao_das_Demonstracoes_Contabeis.doc

THOMSON REUTERS

Tela  Geração das Demonstrações Contábeis
Localização: MastersafDW >> SPED >> ECD – Escrituração Contábil Digital >> Geração >> Demonstrações Contábeis>> 
SPED


	
Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc24114133" 1.	CONTROLE DE ALTERAÇÕES	 PAGEREF _Toc24114133 \h 3
 HYPERLINK \l "_Toc24114134" 2.	INTRODUÇÃO	 PAGEREF _Toc24114134 \h 4
 HYPERLINK \l "_Toc24114135" 3.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc24114135 \h 4
 HYPERLINK \l "_Toc24114136" 4.	DEFINIÇÃO DAS REGRAS	 PAGEREF _Toc24114136 \h 4
 HYPERLINK \l "_Toc24114137" 4.1.	Botões da Toolbar	 PAGEREF _Toc24114137 \h 4
 HYPERLINK \l "_Toc24114138" 4.2.	Layout e Campos – Tela	 PAGEREF _Toc24114138 \h 4
 HYPERLINK \l "_Toc24114139" 4.3.	Abas que podem ser geradas:	 PAGEREF _Toc24114139 \h 9


CONTROLE DE ALTERAÇÕES


Data	Demanda	Descrição	Autor		10/10/2019	MFS-31020	Criação da tela de Geração das Demonstrações Contábeis. 	Alessandra Cristina Navatta		30/12/2019	MFS-29278	Inclusão dos campos Apenas Conferência e Período do Arquivo da ECD. 
O campo de período campo indica em qual arquivo será gerada a demonstração contábil.	Alessandra Cristina Navatta		03/01/2019	MFS-32558	Inclusão de mensagens de log para os registros J100 (Balaço) e J150 (DRE).	Alessandra Cristina Navatta		29/01/2020	MFS33788	Retirar a mensagem de erro referente ao período das datas	Andréa Rocha		26/07/2021	MFS-69607	Inclusão do Parâmetro “Manter Registros Trimestral e Anual”	Rogério Ohashi		


	 

INTRODUÇÃO 
Criar uma tela para o usuário efetuar a Geração das Demonstrações Contábeis. Essa necessidade surgiu, por conta da reestruturação da ECD, para permitir ao usuário conseguir conferir essas demonstrações, antes da geração do Sped Contábil.

DOCUMENTOS DE REFERÊNCIA
Não se aplica.
DEFINIÇÃO DAS REGRAS
	
Botões da Toolbar 

Imprime, Pág.-, Pág.--, Pág.+, Pág.++ e Fecha.

Layout e Campos – Tela 


Campos de preenchimento obrigatório: Data Inicial, Data Final, pelo menos um tipo de Demonstração Contábil, Período do Arquivo da ECD (datas inicial e final da ECD) se o campo ‘Apenas Conferência’ estiver preenchido com ‘Não’ e Estabelecimentos. Caso um desses campos não esteja preenchidos, verificar a mensagem a ser exibida, nas regras abaixo.


Campo	Regra	Demanda		Data Final	

A data final deve ser maior que a data inicial. Caso não seja, exibir a mensagem: "A data final do filtro deve ser maior ou igual a data inicial".

[MFS33788] Exclusão da mensagem de validação do período
A data inicial e final devem estar compreendida dentro do mesmo ano, caso contrário, exibir a mensagem: “O campo de Data Inicial e Data Final devem estar compreendidas dentro do mesmo ano”.

	MFS-31020
MFS-33788		Apenas Conferência	Opções de Valores Válidos

Não
Sim

Opção default: Não	MFS-29278		Período do Arquivo da ECD (data final)	
Se o parâmetro Apenas Conferência estiver preenchido com ‘Sim’, desabilitar o período do arquivo da ECD (datas inicial e final da ECD), porém considerar na tabela a data de 01/01/1900 a 01/01/1900. 
Se o parâmetro Apenas Conferência estiver preenchido com ‘Não’, as datas inicial e final do período do arquivo da ECD devem ficar habilitadas para serem editadas.

A data final da ECD deve ser maior que a data inicial da ECD. Caso não seja, exibir a mensagem: "A data final da ECD deve ser maior ou igual a data inicial da ECD".
	MFS-29278		Manter Registros Trimestral e Anual	Formato: 
Check Box

Default: Habilitado e desmarcado	MFS-69607		Grid Estabelecimentos	Exibir todos os estabelecimentos da empresa selecionada no menu, que o usuário tenha acesso.


	MFS-31020		
Selecionar	Permite que o usuário selecione os Estabelecimentos que serão gerados as demonstrações contábeis.

Tratamentos:

Modal 'Selecionar Estabelecimentos‘
Ao ser acionado abrir o Modal 'Selecionar Estabelecimentos‘. Apresentando os campos Cód. Estab e DescriçãoBotões do Modal 'Selecionar Estabelecimentos': Critério, Cancelar, OK e Salvar...


Botões Critério, Cancelar, OK e Salvar- Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Estabelecimentos‘ será fechado. - Ao selecionar o botão 'Critério', os estabelecimentos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar. 
-Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os estabelecimentos no componente “Estabelecimentos” da tela Principal
- Permite a seleção de vários registros por vez.
- Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um registro”.
-Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas dos estabelecimentos (no diretório local e formato que o usuário informar).
	MFS-31020		Marcar Todos	Permite ao usuário selecionar ou desmarcar todos os registros da grid Estabelecimentos.
	MFS-31020		Executar	Mensagens que bloqueiam a geração das demonstrações contábeis:

Ao acionar este campo, verificar se na tela:

Campo Data inicial está preenchido. Caso não esteja preenchido exibir a mensagem: Informe a Data Inicial.

Campo Data Final está preenchido. Caso não esteja preenchido exibir a mensagem: Informe a Data Final.

Deve ser marcada pelo menos uma demonstração, na Grid Demonstrações. Caso contrário exibir a mensagem “Selecione pelo menos uma Demonstração”.

Deve ser marcada pelo menos um estabelecimento. Caso contrário exibir a mensagem “Selecione pelo menos um Estabelecimento”.

Se o parâmetro Apenas Conferência estiver preenchido com ‘Não’, campo de Data Inicial da ECD deve estar preenchido. Caso não esteja preenchido exibir a mensagem: Informe a Data Inicial da ECD 

Se o parâmetro Apenas Conferência estiver preenchido com ‘Não’, campo de Data Final da ECD deve estar preenchido.Caso não esteja preenchido exibir a mensagem: Informe a Data Final da ECD.

Ao acionar este campo, verificar e se necessário exibir a mensagem na aba de Logs:

Se não existir parametrização da demonstração selecionada para o estabelecimento em questão, exibir a mensagem no log para cada demonstração que não for encontrada: 

“Não há parametrização de Balanço Patrimonial. Estabelecimento: XXXX.Localização: SPED >> ECD – Escrituração Contábil Digital >> Manutenção >> Códigos de Aglutinação (B. Patrimonial/D.Resultado/DLPA/DMPL)”. Ou

“Não há parametrização de Demosntração de Resultado. Estabelecimento: XXXX.Localização: SPED >> ECD – Escrituração Contábil Digital >> Manutenção >> Códigos de Aglutinação (B. Patrimonial/D.Resultado/DLPA/DMPL)”. Ou

“Não há parametrização de DLPA. Estabelecimento: XXXX.Localização: SPED >> ECD – Escrituração Contábil Digital >> Manutenção >> Códigos de Aglutinação (B. Patrimonial/D.Resultado/DLPA/DMPL)”. Ou	MFS-31020
MFS-29278
MFS-32558		
“Não há parametrização de DMPL. Estabelecimento: XXXX.Localização: SPED >> ECD – Escrituração Contábil Digital >> Manutenção >> Códigos de Aglutinação (B. Patrimonial/D.Resultado/DLPA/DMPL)”.


Mensagens de Aviso (não vai bloquear a geração das demonstrações):

Ao ser gerada a demonstração de Balanço, verificar se há duas linhas com nível 1 (uma com Indicador de grupo do balanço: A – Ativo e outra P – Passivo e Patrimônio Líquido). Caso contrário, exibir a mensagem: “Deve existir duas linhas de nível 1, uma com indicador de grupo de balanço igual a Ativo e outra igual a Passivo.” 

Ao ser gerada a demonstração de Balanço, verificar se há pelo menos uma linha com nível 3. Caso contrário, exibir a mensagem: “Verificar a estrutura do Balanço, porque deve ter no mínimo 3 níveis.”

Ao ser gerada a Demonstração de Resultado, verificar se há uma linha com nível 1. Caso contrário, exibir a mensagem: “Deve existir uma linha de nível 1, para a Demonstração de Resultado.” 

Ao ser gerada a Demonstração de Resultado, verificar se há pelo menos uma linha com nível 3. Caso contrário, exibir a mensagem: “Verificar a estrutura da Demonstração de Resultado, porque deve ter no mínimo 3 níveis.” 
		

Abas que podem ser geradas:

Processos	 Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo.

	MFS-31020		Logs	Esta aba deve demonstrar os logs do processo. 

Na parte superior da tela exibir os parâmetros que foram indicados na tela de geração, seguindo o formato abaixo:

 EMBED PBrush  	MFS-31020		Arquivos	Esta aba deve demonstrar os arquivos de demonstrações que foram gerados durante a execução. 
O título dos arquivos serão:

Relatorio Analitico Balanco Patrimonial 
Relatorio Sintetico Balanco Patrimonial 
Relatorio Analitico DRE 
Relatorio Sintetico DRE
Relatorio Analitico DMPL 
Relatorio Sintetico DMPL
Relatorio Analitico DLPA 
Relatorio Sintetico DLPA


Além disso, o usuário poderá salvar os arquivos com ou sem o nº do processo, escolher se o arquivo será salvo em Local/Rede ou Servidor (Banco de Dados).

Os arquivos gerados, devem conter a visão analítica e sintética das demonstrações e será gerado em formato XLS.
	MFS-31020		Relatório Sintético – Balanço Patrimonial	Se a demonstração Balanço Patrimonial estiver marcada, a aba será exibida e será apresentado a visão sintética do relatório.

Layout conforme arquivo Layout-Relatorios-BP-DRE-DMPL-DLPA.xlsx
	MFS-31020		Relatório Sintético – DRE	Se a demonstração DRE estiver marcada, a aba será exibida e será apresentado a visão sintética do relatório. Layout conforme arquivo Layout-Relatorios-BP-DRE-DMPL-DLPA.xlsx
	MFS-31020		Relatório Sintético – DLPA	Se a demonstração DLPA estiver marcada, a aba será exibida e será apresentado a visão sintética do relatório.

Layout conforme arquivo Layout-Relatorios-BP-DRE-DMPL-DLPA.xlsx


	MFS-31020		Relatório Sintético – DMPL	Se a demonstração DMPL estiver marcada, a aba será exibida e será apresentado a visão sintética do relatório.

Layout conforme arquivo Layout-Relatorios-BP-DRE-DMPL-DLPA.xlsx
	MFS-31020