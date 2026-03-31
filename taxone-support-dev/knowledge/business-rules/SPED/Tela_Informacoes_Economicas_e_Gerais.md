# Tela_Informacoes_Economicas_e_Gerais

> Fonte: Tela_Informacoes_Economicas_e_Gerais.doc

THOMSON REUTERS

Tela Informações Econômicas e Gerais (Bloco X e Y)
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO
Data	MFS	Descrição	Autor		02/05/2018	MFS-12630	Criação do Documento	Alessandra Cristina Navatta		10/05/2018	MFS-18350	Inclusão das regras de permissão de inclusão dos registros X291 e X292	Alessandra Cristina Navatta		14/05/2018	MFS-18357	Inclusão das regras de permissão de inclusão dos registros X300 e X310	Alessandra Cristina Navatta		02/10/2018	MFS-21399	Inclusão dos demais registros do bloco X (X320,X330,X340,X350,X351,X352,X353,X354,X355,X356,X390,X400,X410, X420,X430,X450, X460, X470, X480, X490, X500 e X510)	Alessandra Cristina Navatta		
Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc526258449" 1.	INTRODUÇÃO	 PAGEREF _Toc526258449 \h 3
 HYPERLINK \l "_Toc526258450" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc526258450 \h 3
 HYPERLINK \l "_Toc526258451" 3.	TELA/MODAIS	 PAGEREF _Toc526258451 \h 3
 HYPERLINK \l "_Toc526258452" 3.1	Pesquisa de Registros	 PAGEREF _Toc526258452 \h 3
 HYPERLINK \l "_Toc526258453" 3.2	Regras dos Campos Tela Principal	 PAGEREF _Toc526258453 \h 4
 HYPERLINK \l "_Toc526258454" 3.3	Modais	 PAGEREF _Toc526258454 \h 18
 HYPERLINK \l "_Toc526258455" 4.	Permissão de exibição dos registros na tela	 PAGEREF _Toc526258455 \h 20


	


INTRODUÇÃO

Objetivo desta especificação é criar a tela ‘Informações Econômicas e Gerais (Blocos X e Y)’.

DOCUMENTOS DE REFERÊNCIA


Layout_ECF.xlsx
Regras_Gerais_DWECF.docx
Tela_Informacoes_ECF.docx
Mensagens_Sistema_DWECF.xlsx
Validacao_Bloco_Y.xlsx
Validacao_Bloco_X.xlsx


TELA/MODAIS

Pesquisa de Registros 

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração>> Bloco X e Y – Informações Econômicas e Gerais >> Manutenção 
Título da tela:  Informações Econômicas e Gerais (Blocos X e Y)


Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.

Campo	Tipo	Regra		Estabelecimento	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
AAAA	

O usuário poderá informar o exercício. 

		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código -Descrição)	Aplicar a RNG00004 -Versão de Layout		Forma de Tributação	Lista
(Código -Descrição)	Exibe as opções abaixo:

-Lucro Real, Lucro Presumido, Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 


		Apuração	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral

		

Regras dos Campos Tela Principal


Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração>> Bloco X e Y – Informações Econômicas e Gerais>> Manutenção 
Título da tela:  Informações Econômicas e Gerais (Blocos X e Y)

Condições Gerais: Quando o usuário acessar a tela de consulta, apresentar todos os registros da tela Informações ECF.
Desabilitar os botões “Novo”, “Excluir” e “Copiar” na toolbar.

As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		DADOS GERAIS
As informações são referentes a um registro cadastrado na tela Informações ECF. (*)
		Estabelecimento	Texto	S	N	Tipo - Código - Descrição	Permite que o usuário visualize o estabelecimento correspondente ao registro selecionado na tabela de Informações ECF.	MFS-12630		Exercício	Texto
	S	N		Permite que o usuário visualize o exercício.	MFS-12630		Data Inicial	Texto
	S	N		Permite que o usuário visualize a data inicial da escrituração.

	MFS-12630		Versão	Texto	S	N		Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar RNG00004 - Versão de Layout.	MFS-12630		Forma de Tributação	Texto
	S	N		Permite que o usuário visualize a forma de tributação.
	MFS-12630		Apuração	Texto
	S	N		Permite que o usuário visualize a Apuração.	MFS-12630		Data Final do Último Período da Escrituração	Texto
	S	N		Permite que o usuário visualize a data final do último período da escrituração.

	MFS-12630		SELEÇÃO DO REGISTRO
		Registro	Lista	S	S	 (Código -Descrição)	Permite que usuário selecione um registro correspondente na tabela dinâmica de acordo com a versão.

Tratamento: 

Valores Válidos:

X280 - XXX
X291- XXX
X292- XXX
X300- XXX
X310- XXX
X320
X330
X340
X390
X400
X410
X420
X430
X450
X460
X470
X480
X490
X500
X510
Y520
Y540
Y550
Y560
Y570
Y580
Y590
Y600
X320- XXX
X330- XXX
X340- XXX
X350- XXX
X351- XXX
X352- XXX
X353- XXX
X354- XXX
X355- XXX
X356- XXX
X390- XXX
X400- XXX
X410- XXX
X420- XXX
X430- XXX
X450- XXX
X460- XXX
X470- XXX
X480- XXX
X490- XXX
X500- XXX
X510- XXX
Y520- XXX
Y540- XXX
Y550- XXX
Y560- XXX
Y570- XXX
Y580- XXX
Y590- XXX
Y600- XXX
Y611 (Registro válido até a versão 1.0)
Y612
Y620
Y630
Y640
Y650
Y660
Y665
Y671 
Y672
Y680
Y682
Y690
Y612- XXX
Y620- XXX
Y630- XXX
Y640- XXX
Y650- XXX
Y660- XXX
Y665- XXX
Y671 - XXX
Y672- XXX
Y680- XXX
Y682- XXX
Y690- XXX
Y700 (Registro válido até a versão 1.0)
Y710 (Registro válido até a versão 1.0)
Y720
Y800
Y720- XXX
Y800- XXX

Onde ’XXX’ é a descrição do registro

Se o usuário digitar um registro que não teve condições prévias satisfeitas para sua ocorrência, (conforme informado no tópico  HYPERLINK  \l "Permissaodeexibicaodosreg" 4. Permissão de exibição dos registros na tela), exibir a mensagem DW00203 para cada registro encontrado.

-Recuperar apenas os registros de nível 2 (ver a hierarquia no documento: Layout_ECF. xlsx), 


Identificação dos Registros Tabela Interna x Tabela Dinâmica:

Tabela Interna:

X280
X300
X310
X320
X330
X340
X350
X351
X352
X353
X354
X355
X356
X410
X420
X430
X450
Y520
Y540
Y550
Y560
Y570
Y580
Y590
Y600
Y612
Y620
Y630
Y640
Y650
Y660
Y665
Y671 
Y672
Y680
Y682
Y690
Y800

X320
X330
X340
X410
X420
X430
X450
Y520
Y540
Y550
Y560
Y570
Y580
Y590
Y600
Y611 (Registro válido até a versão 1.0)
Y612
Y620
Y630
Y640
Y650
Y660
Y665
Y671 
Y672
Y680
Y682
Y690
Y700 (Registro válido até a versão 1.0)
Y710 (Registro válido até a versão 1.0)
Y800

Tabela Dinâmica:

X291,
X292,
X390,
X400,
X460,
X470,
X480,
X490,
X500,
X510

X390,
X400,
X460,
X470,
X480,
X490,
X500,
X510,
	MFS-12630
MFS-21399		Título do Registro (*)	Texto	S	N		Tratamento:

-O título só deve ser exibido, se for selecionado um registro na tela principal.  

-Exibir o Título ‘OCORRÊNCIAS DO REGISTRO XXXX– DSC REGISTRO’, onde o XXXX é o código do registro apresentado na grid. 
Ex. Selecionado o registro X310, nome a ser Exibido ‘OCORRÊNCIAS DO REGISTRO X300 - Operações com o Exterior - Exportações (Entradas de Divisas)’
	MFS-12630		Pesquisar/Filtrar	Botão		Permite ao usuário pesquisar/filtrar o registro.

Tratamentos:
Exibir no filtro os campos chaves do registro.	MFS-12630		Adicionar	Botão		Permite ao usuário adicionar uma linha no registro.

Tratamentos:

Este botão deve ser exibido, se o registro selecionado for de tabela Interna, caso contrário, não exibir este botão.

Ao selecionar este botão exibir o  HYPERLINK  \l "ModalTabelaInterna_AddeAlterar" modal de adicionar tabela interna.
	MFS-12630		Alterar	Botão		Permite ao usuário altere uma linha no registro.

Tratamentos:

Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido, se o registro selecionado for de tabela interna, caso contrário, este botão não deve ser exibido na tela. 

Ao selecionar este botão exibir o  HYPERLINK  \l "ModalTabelaInterna_AddeAlterar" modal de alterar tabela interna.
	MFS-12630		Remover	Botão		Permite ao usuário, remover um ou mais registros.

Tratamentos:

Registros de Tabela Interna

Este botão só deve ser exibido se o registro selecionado for de tabela Interna, caso contrário não exibir este botão. 
-Pelo menos, um registro da grid deve ser selecionado, caso contrário, exibir a mensagem DW00149.
-Ao selecionar o botão, se pelo menos um registro for selecionado na grid, aplicar a RG00041 – Botão Remover. Se o registro selecionado possuir filhos, exibir a mensagem DW00211. Se a opção selecionada for ‘Sim’, apaga o registro pai e seus filhos. Se a opção for ‘Não’, os registros não serão apagados.	MFS-12630		Exportar	Botão		Tratamento:

Realiza a exportação dos dados da grid no formato CSV CSV nomeado como “Export_ <Registro>.csv”, conforme padrão do framework.

Este botão deve ser habilitado apenas quando existir pelo menos um registro na grid. 	MFS-12630		GRID Registros de Tabela Interna (*)


		Check-box	botão		Desmarcados	Permite ao usuário selecionar um ou mais registros, para ser(em) excluído(s) da base.

Tratamentos:

Só deve ser exibido o check-box, se o registro selecionado for de tabela Interna, caso contrário não exibir.

Este campo será exibido em todas as linhas que serão apresentadas na grid.
Quando um ou mais registro for selecionado e o botão ‘Remover’, acionado, os registros marcados serão removidos e excluídos da grid, conforme regras do  HYPERLINK  \l "Remover" botão Remover .	MFS-12630		Campos (*)	Texto	S	N		Para os registros da Tabela Interna:

A grid será exibida com todos os campos listados nas tabelas “Validacao_Bloco_Y.xlsx” e “Validacao_Bloco_X.xlsx”, com exceção do campo “REG”,considerando como filtro a seleção do campo Versão e Registro. O label dos campos deve corresponder com a informação da coluna Rótulo.
	MFS-12630		GRID Tabela Dinâmica(*)		Campos (*)		A grid será exibida com todos os campos listados nas tabelas Dinâmicas, considerando como filtro a seleção do campo Registro.

Todas as linhas deverão ser apresentadas na grid da tela, porém as linhas com tipo = ‘R’ e ‘CNA’ devem ficar desabilitadas. 
As linhas de rótulo, devem ser sempre nulas.
Toda vez que uma linha do tipo CNA possuir uma fórmula cujos valores utilizados para a execução da fórmula estejam dentro do mesmo registro, deverá ser exibido na linha, o valor resultante da fórmula executada. 
Apenas o campo Valor, poderá ser alterado pelo usuário (através da tela).
	MFS-12630		Cód. do Registro	
Texto	
S	
N		
Exibe os ‘códigos’ de todas as linhas das tabelas dinâmicas.	MFS-12630		Desc. do Registro	
Texto	
S	
N		
Exibe a descrição das linhas das tabelas dinâmicas.	MFS-12630		Valor	Texto	S	S		Exibe o valor referente a linhas da tabela dinâmica. 

As linhas de tipo ‘R’, não terão valor (serão sempre desabilitadas e nulas).O valor calculado nas linhas do tipo CNA será gravado com a ação no Botão Salvar.

Para os campos de valor com formato ‘NS’, exibir do lado esquerdo do campo, o ícone  EMBED PBrush  e o tooltip ‘Para valores negativos, insira o sinal ‘-‘’.
	MFS-12630		GRID Registros Filhos(*)
		Apresentar as informações do registro filho (*)		S	S	Código do Registro	Permite ao usuário, inserir ou visualizar os registros filhos do registro pai selecionado, logo abaixo da grid principal.

Tratamentos:

Exibir em abas os registros filhos do registro pai que está sendo apresentado na grid principal. Só devem ser apresentadas os registros cujo os parâmetros estejam condizentes com o tópico  HYPERLINK  \l "Permissaodeexibicaodosreg" 4. Permissão de exibição dos registros na tela. As grids dos registros filhos serão apresentadas logo abaixo do registro pai. 

As abas devem ser exibidas em ordem crescente pelo campo código do registro.	MFS-12630		Título do Registro (*)	Texto	S	N		Exibir o Texto ‘OCORRÊNCIAS DO REGISTRO FILHO XXXX – DSC REGISTRO’, onde o XXXX é o código do registro apresentado na grid. 

Este título só deve ser exibido, se for selecionado um registro no modal de registro filho.  
	MFS-12630		Pesquisar/Filtrar	Botão		Permite ao usuário pesquisar/filtrar o registro.

Tratamentos:
Exibir no filtro os campos chaves do registro.	MFS-12630		Adicionar	Botão		Permite ao usuário adicionar uma linha no registro.

Tratamentos:

Este botão deve ser exibido, se o registro selecionado for de tabela Interna, caso contrário, não exibir este botão.

Ao selecionar este botão exibir o  HYPERLINK  \l "ModalTabelaInterna_AddeAlterar" modal de adicionar tabela interna.
	MFS-12630		Alterar	Botão		Permite ao usuário altere uma linha no registro.

Tratamentos:

Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido, se o registro selecionado for de tabela interna, caso contrário, este botão não deve ser exibido na tela. 


Ao selecionar este botão exibir o  HYPERLINK  \l "ModalTabelaInterna_AddeAlterar" modal de alterar tabela interna.
	MFS-12630		Remover	Botão		Permite ao usuário, remover um ou mais registros.

Tratamentos:

Registros de Tabela Interna

Este botão só deve ser exibido se o registro selecionado for de tabela Interna, caso contrário não exibir este botão. 
-Pelo menos, um registro da grid deve ser selecionado, caso contrário, exibir a mensagem DW00149.
-Ao selecionar o botão, se pelo menos um registro for selecionado na grid, aplicar a RG00041 – Botão Remover. Se o registro selecionado possuir filhos, exibir a mensagem DW00211. Se a opção selecionada for ‘Sim’, apaga o registro pai e seus filhos. Se a opção for ‘Não’, os registros não serão apagados.	MFS-12630		Campos (*)	Texto	S	S		Exibir os campos de acordo com o registro selecionado.

Tratamentos:

Apresentar os campos e botões de acordo com o tipo de registro: 

 HYPERLINK  \l "GRIDRegTabelaDinamica" Tabela dinâmica, verificar as regras e definições dos campos.

 HYPERLINK  \l "GRIDRegTabelaInterna" Tabela Interna, verificar as regras e definições dos campos.	MFS-12630		Exibição do Registro Y800(*)		Adicionar Arquivo	Botão		Permite ao usuário Adicionar uma linha no registro.

Este botão deve ser habilitado apenas quando os campos Versão e Registro = ‘Y800 ‘estiverem preenchidos.

Este botão abre o modal da funcionalidade padrão ‘Adicionar Arquivo’ (item 12) (‘MTZ_Funcionalidades_Padroes.doc’) . 

Tratamentos adicionais:
Apenas arquivos com extensão RTF devem ser aceitos.
		Baixar Arquivo(s)	Botão	-	-	Desabilitado	Quando acionado, efetua o download dos arquivos selecionados por meio do checkbox.

Tratamento:

Deve ser habilitado somente quando houver pelo menos uma linha da grid, selecionada.

Se houver um arquivo selecionado, o sistema deverá fazer o download com a nomenclatura e a extensão de acordo com o arquivo.

Se houver mais de um arquivo selecionado, o sistema deverá fazer download no formato ZIPADO, com a nomenclatura da pasta de acordo com o nome da tela, contendo todos os artefatos gerados em cada processo.
		Remover	Botão		Permite ao usuário remover uma ou mais linhas do registro.

Tratamento:

Este botão só deve ser habilitado se pelo menos um registro selecionado na grid. 		Check-Box	-	S	S		Permite ao usuário selecionar um ou mais registros para ser removido da grid.

Tratamentos:
Apresentar o check-box para os registros que estão adicionados na grid.		TIPO DE REGISTRO	Texto	S	N		O sistema preenche automaticamente este campo com a informação ‘Y800’, quando o arquivo for inserido do modal de Adicionar Arquivo, na grid.
		SEQUÊNCIA DE BYTES	Texto	S	N		Apresenta o nome do arquivo anexado, com a extensão.		INDICADOR DE FIM DE ARQUIVO	Texto	S	N		O sistema preenche automaticamente este campo com a informação ‘Y800FIM’, quando o arquivo for inserido do modal de Adicionar Arquivo, na grid.
		Confirma	Botão	-	-		Permite ao usuário salvar os dados referentes aos registros.

Aplicar a RNG00012 - Salvar

Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido e algum registro for adicionado na grid.

Para os registros de Tabela Interna:
Considerar também as validações dos documentos ‘Validacao_Bloco_X.xlsx’ e ‘Validacao_Bloco_Y.xlsx’

Para os registros de Tabela Dinâmica:

As linhas com tipo ‘CNA’, devem ser atualizadas (calculadas), de acordo com o campo fórmula da tabela dinâmica.
	MFS-12630		     (*)Não exibir a descrição na tela.

Modais

Modal da Tabela Interna: Adicionar/Alterar 

Este modal deve ser exibido se for selecionado os botões Adicionar ou Alterar na grid de tabela Interna (*)

Ao selecionar o botão Adicionar, apresentar o título: Adicionar 
Ao selecionar o botão Alterar, apresentar o título: Alterar 

Voltar ao  HYPERLINK  \l "BotaoAdd" botão Adicionar
Voltar ao  HYPERLINK  \l "BotaoAlterar" botão Alterar 		Campos (*)		
A grid será exibida com todos os campos listados nas tabelas “Validacao_Bloco_Y.xlsx” e “Validacao_Bloco_X.xlsx” com exceção do campo “REG”, considerando como filtro a seleção do campo Versão e Registro. O label dos campos deve corresponder com a informação da coluna Rótulo.

Se o usuário acessar o modal pelo botão adicionar, os campos devem ser exibidos sem informação, caso a seleção seja pelo alterar, trazer os dados já preenchidos, para que o usuário efetue a alteração desejada.
	MFS-12630		Vincular	Botão		Habilitado	Permite ao usuário vincular (adicionar) os dados na grid

Validações:
Aplicar as regras abaixo:
RNG00011 - Duplicidade de registro;
E as validações dos campos recuperados conforme arquivos “Validacao_Bloco_Y.xlsx” e “Validacao_Bloco_X.xlsx”
	MFS-12630		Cancelar	Botão		Habilitado	Permite ao usuário cancelar as informações que não foram vinculadas na tela.	MFS-12630		

Modal Fórmulas -Tabela Dinâmica:

Este modal deverá ser exibido quando a linha da tabela dinâmica selecionada possuir fórmulas (duplo click na linha) (*).
Título: Visualizar Detalhamento do Cálculo		
Fórmula
		Exibição das Fórmulas (*)	Texto	S	N	-	Exibe a fórmula utilizada para identificação do valor do código do registro selecionado conforme a coluna “Fórmula” da planilha [Tabelas_Dinamicas.xls] 	MFS-12630		

Permissão de exibição dos registros na tela


Reg.	Descrição	Regra de Exibição do Registro na Tela	MFS		HYPERLINK \l "RX280"X280	Atividades Incentivadas - PJ em Geral	Apresentar a mensagem DW00203 se na tela Informações ECF,os campos ‘Lucro da Exploração’ e ‘Isenção e Redução do Imposto para Lucro Presumido’ estiverem desmarcados 
	MFS-12630		X291	Operações com o Exterior - Pessoa Vinculada/Interposta/País com Tributação Favorecida.	Apresentar a mensagem DW00203 se na tela Informações ECF, os campos ‘Operações com o Exterior’ ou ‘Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida’ estiverem desmarcados 
	MFS-18350		X292	Operações com o Exterior - Pessoa Não Vinculada/ Não Interposta/País sem Tributação Favorecida	Apresentar a mensagem DW00203 se na tela Informações ECF, os campos ‘Operações com o Exterior’ estiver desmarcado ou ‘Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida’ estiver marcado. 
	MFS-18350		X300	Operações com o Exterior - Exportações (Entradas de Divisas)	Apresentar a mensagem DW00203 se na tela Informações ECF, os campos ‘Operações com o Exterior’ ou ‘Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida’ estiverem desmarcados 	MFS-18357		X310	Operações com o Exterior - Contratantes das Exportações 


	Apresentar a mensagem DW00203 se na tela Informações ECF, os campos ‘Operações com o Exterior’ ou ‘Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida’ estiverem desmarcados 	MFS-18357		X320	Operações com o Exterior - Importações (Saídas de Divisas)


	Apresentar a mensagem DW00203 se na tela Informações ECF, os campos ‘Operações com o Exterior’ ou ‘Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida’ estiverem desmarcados 	MFS-21399		HYPERLINK \l "RX330"X330	Operações com o Exterior - Contratantes das Importações	Apresentar a mensagem DW00203 se na tela Informações ECF, os campos ‘Operações com o Exterior’ ou ‘Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida’ estiverem desmarcados	MFS-21399		HYPERLINK \l "RX340"X340	Identificação da Participação no Exterior 	
Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Participações no Exterior’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX350"X350	Participações no Exterior - Resultado do Período de Apuração


	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Participações no Exterior’ estiver desmarcado.	MFS-21399		X351	Demonstrativo de Resultados e de Imposto a Pagar no Exterior 	Apresentar a mensagem DW00271, se o registro X340 possuir o campo IND_CONTROLE = “6.	MFS-21399		X352	Demonstrativo de Resultados no Exterior Auferidos por Intermédio de Coligadas em Regime de Caixa	Apresentar a mensagem DW00271, se o registro X340 possuir o campo IND_CONTROLE `"  6.	MFS-21399		X353	Demonstrativo de Consolidação 	Apresentar a mensagem DW00271, se o registro X340 possuir o campo IND_CONTROLE =  6.	MFS-21399		X354	Demonstrativo de Prejuízos Acumulados 	Apresentar a mensagem DW00271, se o registro X340 possuir o campo IND_CONTROLE = “6.	MFS-21399		X355	Demonstrativo de Rendas Ativas e Passivas 	Apresentar a mensagem DW00271, se o registro X340 possuir o campo IND_CONTROLE = “6.	MFS-21399		X356	Demonstrativo de Estrutura Societária 	Apresentar a mensagem DW00271, se o registro X340 possuir o campo IND_CONTROLE = “6.	MFS-21399		HYPERLINK \l "RX390"X390	Origem e Aplicação de Recursos - Imunes ou Isentas	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Forma de Tributação’ for diferente de ‘Imune de IRPJ’ ou ‘Isento de IRPJ’.	MFS-21399		HYPERLINK \l "RX400"X400	Comércio Eletrônico e Tecnologia da Informação – Informações das Vendas	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Comércio Eletrônico e Tecnologia da Informação’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX410"X410	Comércio Eletrônico – Informação de Homepage/Servidor	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Comércio Eletrônico e Tecnologia da Informação’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX420"X420	Royalties Recebidos ou Pagos a Beneficiários do Brasil e do Exterior	Apresentar a mensagem DW00203 se na tela Informações ECF, os campos ‘Royalties Pagos a Beneficiários do Brasil e do Exterior ‘ e ‘Royalties Recebidos do Brasil e do Exterior’ estiverem desmarcados.	MFS-21399		HYPERLINK \l "RX430"X430	Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior 	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX450"X450	Pagamentos/Remessas Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Pagamentos ou Remessas a Titulo de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX460"X460	Inovação Tecnológica e Desenvolvimento Tecnológico	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Inovação Tecnológica e Desenvolvimento Tecnológico’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX470"X470	Capacitação de Informática e Inclusão Digital	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Capacitação de Informática e Inclusão Digital’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX480"X480	Repes, Recap, Padis, PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa do Mundo, Retid, REPNBL-Redes, Reif e Olimpíadas
	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘PJ Habilitada no Repes, Recap, Padis, ... (vide ícone “i”)’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX490"X490	Pólo Industrial de Manaus e Amazônia Ocidental	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Polo Industrial Manaus e Amazônia Ocidental’ estiver desmarcado.	MFS-21399		HYPERLINK \l "RX500"X500	Zonas de Processamento de Exportação (ZPE)	Apresentar a mensagem DW00203 se