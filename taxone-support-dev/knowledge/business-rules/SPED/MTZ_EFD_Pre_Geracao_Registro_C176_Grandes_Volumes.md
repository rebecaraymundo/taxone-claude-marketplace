# MTZ_EFD_Pre_Geracao_Registro_C176_Grandes_Volumes

> Fonte: MTZ_EFD_Pre_Geracao_Registro_C176_Grandes_Volumes.doc

THOMSON REUTERS

Módulo Sped Fiscal – Pré-Geração do Registro C176 – Grandes Volumes

 (Ressarcimento de ICMS em Operações com ST)


Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração ( Registro C176 ( Geração (Grandes Volumes)
DOCUMENTO DE REQUISITO

OS/CH	Nome	Descrição	Data		MFS27340	Andréa Rocha
	Criação de uma rotina preliminar para gerar os dados do registro C176 para grandes volumes	23/05/2019 (criação do documento)		MFS67569	Liliane Assaf	Relatórios de Conferência eram gerados em arquivo PSR e passaram para arquivos formato excel (extensão CSV).	10/01/2022		


Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc9866794" 1.	Parâmetros da Tela	 PAGEREF _Toc9866794 \h 3
 HYPERLINK \l "_Toc9866795" 2.	Recuperação dos Dados e Processamento (C176)	 PAGEREF _Toc9866795 \h 5
 HYPERLINK \l "_Toc9866796" 3.	Recuperação dos Dados e Processamento (Ajustes – C195/C197)	 PAGEREF _Toc9866796 \h 5
 HYPERLINK \l "_Toc9866797" 4.	Recuperação dos Dados e Processamento (Devoluções)	 PAGEREF _Toc9866797 \h 5
 HYPERLINK \l "_Toc9866798" 5.	Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)	 PAGEREF _Toc9866798 \h 5
 HYPERLINK \l "_Toc9866799" 6.	Recuperação dos Dados e Processamento (Lançamento na Apuração do ICMS)	 PAGEREF _Toc9866799 \h 6
 HYPERLINK \l "_Toc9866800" 7.	Gravação dos Dados	 PAGEREF _Toc9866800 \h 6
 HYPERLINK \l "_Toc9866801" 8.	Gravação dos Arquivos	 PAGEREF _Toc9866801 \h 6



Parâmetros da Tela 

A geração de grandes volumes foi criada com o objetivo de gerar os dados do registro C176 de um determinado período. Os dados apurados são armazenados em tabelas auxiliares, e posteriormente utilizados na geração do arquivo do Sped Fiscal.  Os dados gerados não serão demonstrados na aba de relatório, como é feito na geração normal.  Os dados serão gravados em arquivo com a extensão PSR, em uma pasta definida pelo cliente.

Parâmetros da geração:

Campo	Tipo	Obrig	Ed	Formato/Default	Regra	OS/CH		Data Inicial	Data
	S	S		Neste campo o usuário informará a data inicial do período da geração.
		Data Final	Data
	S	S		Neste campo o usuário informará a data final do período da geração.
		Pesquisar últimas entradas até	Data
	S	S		Neste campo é informada a data limite até onde será feita a pesquisa das últimas notas de entrada do produto.

Obs: Esta pesquisa é feita desde a data da venda (data da NF da venda) até a data limite informada, sendo que ao atingir a quantidade da venda a pesquisa é interrompida. Assim, esta data é apenas um limite “genérico” para os casos em que as entradas não sejam encontradas (para evitar que a pesquisa seja feita indeterminadamente).
		Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS	Alfanumérico
	N	S	Default:

 Desmarcado	Este campo é um checkbox onde o usuário poderá optar em gerar ou não os dados para os ajustes do C197 e os lançamentos da Apuração do ICMS. 		Tratamento das saídas com notas de entrada sem valor de ICMS-ST	Alfanumérico
	N	S	Default:

 Desmarcado	Este campo é um checkbox onde o usuário informa se as saídas com entrada(s) sem valor de ICMS-ST, terão ou não os ajustes do C197 gerados. (ver help do parâmetro)		Geração p/Inscrição Estadual Única	Alfanumérico
	N	S	Default:

 Opção “Não”	Este campo apresenta duas opções: 

- Sim
- Não

As opções são alternativas.

A opção informada interfere no campo “Estabelecimentos”, conforme descrito na regra específica.
		Estabelecimentos	Alfanumérico
	S	Ver regra		Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.

A exibição dos estabelecimentos depende da opção informada no campo “Geração p/Inscrição Estadual Única”, da seguinte forma:

Se = “Sim” ( Neste caso, serão exibidos apenas os estabelecimentos centralizadores, conforme a parametrização da Inscrição Estadual Única no módulo de Controle das Obrigações Estaduais; 

Se = “Não” ( Neste caso serão exibidos todos os estabelecimentos da empresa;

Sempre que a opção do campo “Geração p/Inscrição Estadual Única” for alterada, esta lista será refeita dinamicamente, considerando a nova opção.
		


Recuperação dos Dados e Processamento (C176)

As regras de recuperação dos dados são as mesmas regras definidas no documento da pré-geração do Registro C176 (MTZ-EFD-Pre_Geracao_Registro_C176_A_partir_Jan_2017.doc).


Recuperação dos Dados e Processamento (Ajustes – C195/C197)

As regras de recuperação dos dados e processamento dos ajustes são as mesmas regras definidas no documento da pré-geração do Registro C176 (MTZ-EFD-Pre_Geracao_Registro_C176_A_partir_Jan_2017.doc).


Recuperação dos Dados e Processamento (Devoluções)

As regras de recuperação dos dados e processamento das devoluções são as mesmas regras definidas no documento da pré-geração do Registro C176 (MTZ-EFD-Pre_Geracao_Registro_C176_A_partir_Jan_2017.doc).


Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)

As regras de recuperação dos dados e processamento do estorno das devoluções são as mesmas regras definidas no documento da pré-geração do Registro C176 (MTZ-EFD-Pre_Geracao_Registro_C176_A_partir_Jan_2017.doc).


Recuperação dos Dados e Processamento (Lançamento na Apuração do ICMS)

As regras de recuperação dos dados e processamento dos lançamentos na apuração são as mesmas regras definidas no documento da pré-geração do Registro C176 (MTZ-EFD-Pre_Geracao_Registro_C176_A_partir_Jan_2017.doc).


Gravação dos Dados 


Os dados gerados para o registro C176, C197 (ajustes) e lançamentos complementares serão armazenados e posteriormente utilizados na geração do Sped Fiscal.

As informações a serem armazenados para cada caso, são as mesmas regras definidas no documento da pré-geração do Registro C176 (MTZ-EFD-Pre_Geracao_Registro_C176_A_partir_Jan_2017.doc).


Gravação dos Arquivos 


Os dados gerados para o registro C176, C197 (ajustes) e lançamentos complementares não serão demonstrados nos relatórios de conferência (Relatório de Conferência de Pré-Geração dos Dados do Registro C176 e o Relatório de Conferência das Devoluções).  Os dados serão salvos em um ou mais arquivos, com a extensão PSR CSV [MFS67569] no diretório selecionado.

As informações a serem geradas no Relatório de Conferência de Pré-Geração dos Dados do Registro C176 e o seu layout, estão definidas no documento da pré-geração do Registro C176, no item de emissão do relatório (MTZ-EFD-Pre_Geracao_Registro_C176_A_partir_Jan_2017.doc).

As informações a serem geradas no Relatório de Conferência de Pré-Geração dos Dados do Registro C176 - Devoluções e o seu layout, estão definidas no documento da pré-geração do Registro C176, no item de emissão do relatório das devoluções (MTZ-EFD-Pre_Geracao_Registro_C176_A_partir_Jan_2017.doc).