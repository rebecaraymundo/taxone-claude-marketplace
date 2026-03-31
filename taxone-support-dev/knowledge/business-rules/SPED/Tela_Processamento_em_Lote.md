# Tela_Processamento_em_Lote

> Fonte: Tela_Processamento_em_Lote.doc

THOMSON REUTERS

Tela Processamento em Lote
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		11/10/2017	MFS-12633	Criação do Documento 	Alessandra Cristina Navatta		

Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc497322760" 1.	INTRODUÇÃO	 PAGEREF _Toc497322760 \h 3
 HYPERLINK \l "_Toc497322761" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc497322761 \h 3
 HYPERLINK \l "_Toc497322762" 3.	TELAS	 PAGEREF _Toc497322762 \h 3
 HYPERLINK \l "_Toc497322763" 3.1.	Regras dos Campos Tela Principal	 PAGEREF _Toc497322763 \h 3
 HYPERLINK \l "_Toc497322764" 3.2.	Demais Regras	 PAGEREF _Toc497322764 \h 7


	


INTRODUÇÃO

Objetivo desta especificação é criar a tela de parametrização das informações de processamento em lote.

DOCUMENTOS DE REFERÊNCIA


Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
Tela_Informacoes_ECF.doc
Tela_Abertura_de_Apuracao.doc
MTZ_Processamento_em_Lote.docx


TELAS

Regras dos Campos Tela Principal  


Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Processamento em Lote
Título da tela: Processamento em Lote

Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Processar	Botão	-	-	Desabilitado	Ver regra  HYPERLINK  \l "rn000" RN000 e  HYPERLINK  \l "rn002" RN0002 do item  HYPERLINK  \l "item3_2" 3.2 Demais Regras, deste documento.	MFS-12633		Tela: Principal(*)Titulo: Processamento em Lote		Componente Opções de Processamento(*)Título: Opções de Processamento		Exercício	Lista	S	S	AAAA	Permite que o usuário visualize/informe o exercício para seleção dos registros de abertura da apuração	MFS-12633		 Transcrição dos Valores Empresa para Referenciais Fisco	CheckBox	N	S	Marcado	Transcrição dos Valores Empresa para Referenciais FiscoPermite que o usuário realize a importação dos saldos das contas associadas às tabelas do fisco	MFS-12633		Manter Ajustes Manuais Realizados	CheckBox	N	S	 Desmarcado	Manter os Ajustes Manuais RealizadosPermite que o usuário escolha manter ou remover os ajustes manuais inseridos na tela de “Entrada Manual de Valores” durante a execução da rotina de “Importação dos Saldos”.Tratamentos:Quando a opção “ Transcrição dos Valores Empresa para Referenciais Fisco” for selecionada, habilitar este campo.Se o parâmetro “Manter os Ajustes Manuais Realizados” estiver selecionado e for desmarcada a seleção do parâmetro “ Transcrição dos Valores Empresa para Referenciais Fisco”, limpar e desabilitar o campo “Manter os Ajustes Manuais Realizados”.Com a seleção deste parâmetro, durante o processamento ocorrerá alterações em valores e status da apuração. Para este item verificar o MTZ_Processamento_em_Lote.docx RNIS 10, 10.01,  e 10.02.	MFS-12633		Cálculo dos Registros e Fórmulas	CheckBox	N	S	Desmarcado	Cálculo dos Registros e Fórmulas Permite que o usuário realize os cálculos contidos nas fórmulas das tabelas disponibilizadas pelo fisco	MFS-12633		Componente Períodos de Apuração (*)Título: Períodos de Apuração dos Estabelecimentos		Selecionar	Botão	-	-	-	Permite que o usuário selecione os registros das aberturas da apuração.Tratamentos:Recuperar todas as aberturas, conforme RN001 do item 3.2 Demais Regras, deste documento, apresentando os conteúdos, conforme descrito abaixo.Campos de Pesquisa do Modal 'Selecionar Períodos de Apuração dos Estabelecimentos:Descrição'Botões do Modal 'Selecionar Períodos de Apuração dos Estabelecimentos': Critério, Cancelar, OK e Salvar- Permite a seleção de vários registros por vez.- Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem DW00053.- Ao selecionar o botão 'Cancelar', nada será feito e o modal será fechado. - Ao selecionar o botão 'Critério', as apurações que foram recuperadas poderão ser filtradas,pelos campos: 'Estabelecimento' e 'Identificação da Abertura da Apuração', este ultimo campo o formato das informações serão apresentadas com "Código do Estabelecimento - Nome - Data Inicial da Apuração -  Código da Aberura da Apuração".-Ao confirmar a seleção dos registros, apresentá-los no componente  " Períodos de Apuração dos Estabelecimentos” da tela Principal-Ao selecionar o botão salvar, o sistema salva as informações recuperadas das apurações em formato txt (no diretório local que o usuário informar).	MFS-12633		Marcar Todos	CheckBox	Check-box	S	Desmarcado	Permite selecionar todos os registros da grid do componente 'Períodos de Apuração dos Estabelecimentos". 	MFS-12633		ABERTURAS DAS APURAÇÕES (*)		(CheckBox)	-	-	-	Default Selecionado	CheckBoxPermite que o usuário selecione uma ou mais linhas do componente “ Períodos de Apuração dos Estabelecimentos”.	MFS-12633		Apurações (*)	Texto	S	N	Código Estab - CGC - Exercício -  Data Inicial da Escrituração -  Código Abertura - Descrição da Aberura da Apuração(076 - XXXXXXXXXXXXXX -  01/03/2017 - A04 - Abril)	Ver regra  HYPERLINK  \l "rn001" RN001 do item  HYPERLINK  \l "item3_2" 3.2 Demais Regras, deste documento.	MFS-12633		Demais Regras 

Voltar Botão  HYPERLINK  \l "processar" Processar
Voltar  HYPERLINK  \l "Apuracoes" Apurações

Número	Regras	MFS		RN000	Botão que permite submeter as parametrizações para processamento.Se não existir nenhuma abertura selecionada  no componente "Períodos de Apuração dos Estabelecimentos", emitir a seguinte mensagem: DW00054 Transcrição dos Valores Empresa para Referenciais Fisco: Se o campo “ Transcrição dos Valores Empresa para Referenciais Fisco”” estiver selecionado e o campo “Manter Ajustes Manuais Realizados” não estiver selecionado, ao clicar em Processar, exibir a mensagem de confirmação DW00064, se clicar em 'sim',  utilizar as orientações contidas em:  “MTZ_Processamento_em_Lote.docx” item REGRAS – IMPORTAÇÃO DE SALDOS , sobrepondo as informações correspondentes aos processamentos anteriores e efetuando a limpeza dos ajustes manuais realizados ”, se clicar em 'não', nada será processado.Manter Ajustes Manuais Realizados:Se o campo o campo “Manter Ajustes Manuais Realizados” estiver selecionado, não efetuar a limpeza dos ajustes manuais    realizados na tela “Entrada Manual de Valores” que deverão ser mantidos conforme parametrização anterior à realização da “ Transcrição dos Valores Empresa para Referenciais Fisco””.Cálculo dos Registros e Fórmula:Se o campo “Cálculo dos Registros e Fórmulas” estiver preenchidoVer documento “MTZ_Processamento_em_Lote.docx” item REGRAS – CÁLCULO  , sobrepondo as informações correspondentes as processamentos anteriores.No caso de mais de uma opção estar selecionada, a ordem de execução do processamento é: 1.  Transcrição dos Valores Empresa para Referenciais Fisco”1.1 Manter os Ajustes Manuais Realizados2. Cálculo_________________
Voltar botão  HYPERLINK  \l "processar" Processar
	MFS-12633		RN001	Apresenta  as possíveis aberturas das apurações para processamento.Tratamentos:Status permitidos para o processamento:Se no componente  “Opções de Processamento” estiver selecionado:•  Apenas a opção “ Transcrição dos Valores Empresa para Referenciais Fisco” e/ou "Manter Ajustes Manuais Realizados" , OU • “ Transcrição dos Valores Empresa para Referenciais Fisco ”  e “Cálculo dos Registros e Fórmulas”:Disponibilizar no componente " Períodos de Apuração dos Estabelecimentos" a primeira abertura de apuração do exercício (selecionado no componente  “Opções de Processamento”) cujo status seja diferente de “Cálculo Realizado” para cada estabelecimento que existir uma informação ECF.Exemplos:Ex 1:Janeiro: Cálculo RealizadoFevereiro: Cálculo RealizadoMarço: Aguardando Alteração ManualAbril: ReapurarNeste caso, demonstrar apenas a apuração de Março.Ex 2:Janeiro: Importação dos Saldos RealizadaFevereiro: ReapurarMarço: Reapurar Neste caso, demonstrar apenas a apuração de Janeiro.•Se no componente “Opções de Processamento” estiver selecionada apenas a opção “Cálculo dos Registros e Fórmulas" :Disponilizar a primeira abertura de apuração (para cada estabelecimento que possuir informações ECF)do exercício (selecionado na aba “Opções de Processamento”) cujo status seja diferente de “Cálculo Realizado” e  se a abertura selecionada é diferente de “Apuração em Aberto” e “Aguardando Alteração Manual”. Caso positivo, disponibiliza a abertura da apuração na grid. Caso negativo, não demonstra nenhuma abertura de apuração .Exemplos:Ex 1:Janeiro: Cálculo RealizadoFevereiro: Cálculo RealizadoMarço: Aguardando Alteração ManualAbril: ReapurarNeste caso, não demonstrar nenhuma abertura de apuração.Ex 2:Janeiro: Cálculo RealizadoFevereiro: Cálculo RealizadoMarço: ReapurarAbril: ReapurarNeste caso, demonstrar apenas a apuração de Março.Ex 3:JAneiro: Apuração em AbertoFevereiro: Não existeNeste caso, não demonstrar nenhuma abertura de apuração.Ex 4:Janeiro: Alteração Manual RealizadaFevereiro: ReapurarNeste caso, demonstrar apenas a apuração de Janeiro.Apresentar as apurações recuperadas ordenadas por  Código do Estabelecimento, Data Inicial e Código de Apuração.


Voltar  HYPERLINK  \l "Apuracoes" Apurações	MFS-12633		RN002	Observações para realizar o Processamento:Não é permitido fazer nenhum processamento para períodos posteriores se o período imediatamente anterior não estiver com status “Cálculo Realizado”, devido a este motivo existem algumas situações em que não demonstraremos nenhuma abertura de apuração para os estabelecimentos que possuem uma Informação ECF para o exercício. Para que o usuário refaça qualquer processo após o status “Cálculo Realizado”, será necessário reabrir a apuração através do botão “Ajustar Apuração” na tela de Abertura da Apuração.

_________________
Voltar botão  HYPERLINK  \l "processar" Processar
	MFS-12633