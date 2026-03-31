# MTZ_EFD_PIS-COFINS_Relatorio_de_Notas_Fiscais_de_Devolucao_de_Compra

> Fonte: MTZ_EFD_PIS-COFINS_Relatorio_de_Notas_Fiscais_de_Devolucao_de_Compra.doc

TITLE   \* MERGEFORMAT EFD PIS/COFINS - Relatório de Notas Fiscais de Devolução de Compra


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS3169-GE20	 TITLE   \* MERGEFORMAT EFD PIS/COFINS - Relatório de Notas Fiscais de Devolução de Compra	O objetivo é criar um relatório que facilitará o preenchimento dos ajustes diretamente no Bloco C, referente às notas de compra e devolução (apenas para os casos, que essas duas operações ocorrerem dentro do mesmo mês).
		MFS-693073	Alessandra Cristina Navatta 	Apenas produto TAXONE: 
 
Migração do relatório para o Servidor de Relatórios.(RN09) 
Criação do formato em Excel (XLSX) 
Considerando as mesmas colunas exibidas no formato PDF (RN10) 
 
Não foi realizada a reversa do relatório 
 		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN01	Deverá ser criado no módulo EFD PIS/COFINS um novo relatório (Demonstrativo - Notas de Devolução de Compra Dentro do Mês da Apuração), dentro do Menu: Relatórios>> 	OS3169-GE20		RN02	O filtro do relatório terá as seguintes opções:

Data Inicial das Notas de Devolução: deverá ser informada a Data Inicial para recuperarmos as notas de devolução de compra. Esse campo deverá ser obrigatório de preenchimento e deverá ser do tipo DATA aceitando a informação no formato DD/MM/AAAA.

Data Final das Notas de Devolução: deverá ser informada a Data Final para recuperarmos as notas de devolução de compra. Esse campo deverá ser obrigatório de preenchimento e deverá ser do tipo DATA aceitando a informação no formato DD/MM/AAAA.

A definição de qual data será considerada, será baseada na informação do parâmetro “Registro A100, C100,C180 e C190 – Seleção das Operações Geradoras de Receita”  para definir se as notas devem ser recuperadas pela Data Fiscal ou pela Data Lancamento PIS/COFINS

Serão consideradas as notas de devolução que estão dentro deste período cuja operação de compra, tenha ocorrido dentro do mesmo mês da nota de devolução.

Estabelecimento: O usuário deverá informar o estabelecimento que deseja emitir o relatório.
Na lista dos estabelecimentos serão listados todos os estabelecimentos da empresa, independente da parametrização de centralização dos estabelecimentos.

	OS3169-GE20		RN03	Criticas para a execução da geração:

As datas informadas nos campos “Data Inicial das Notas de Devolução:” e “Data Final das Notas de Devolução:”, deverão estar dentro do mesmo mês, caso contrário, emitir uma msg de erro no log, abortando o processo.	OS3169-GE20		RN04	Recuperação dos dados:

Com base no período informado pelo usuário, o sistema deve filtrar a partir dos Documentos Fiscais, todas as notas de devolução de compra, que possuírem uma nota de entrada  (nota de compra) referenciada e a data desta última deve estar dentro do mês da nota de devolução.

Nota de Saída:

Empresa de login
Estabelecimento selecionado para a geração
Documentos Fiscais de Mercadoria, referentes a operações de Saida 
Campo 03 – MOVTO_E_S = “9” da SAFX07
Notas de mercadoria ou mistas (campo cod_class_doc_fis = ‘1’ ou ‘3’)
Documentos Fiscais de Mercadoria referentes à operações de Devolução
Campo 04 – NORM_DEV = “2” da SAFX07
Os Documentos Fiscais serão recuperados a partir do campo DATA_FISCAL e ou DTA do LANCAMENTO PIS/COFINS (conforme parâmetro em Dados Iniciais) que esteja dentro do período informado nos campos “Data Inicial das Notas de Devolução” e “Data Final das Notas de Devolução”.
Documentos Fiscais de Mercadoria com informação de NF, Série e Subsérie Referenciada
Campo 16 – NUM_DOCFIS_REF preenchido. O preenchimento dos campos 17 – SERIE_DOCFIS_REF e 18 – S_SER_DOCFIS_REF é opcional.
Documentos Fiscais de Mercadoria com informação de Data do Documento de Saída preenchida
Campo 75 – DAT_DI preenchido (preenchidas com uma data contida no período da geração)

	OS3169-GE20		RN05	Recuperação dos dados:

Nota de Entrada:

Empresa de login
Estabelecimento selecionado para a geração
Documentos Fiscais de Mercadoria, referentes a operações de Entrada
Campo 03 – MOVTO_E_S = “1” da SAFX07
Notas de mercadoria ou mistas (campo cod_class_doc_fis = ‘1’ ou ‘3’)
Documentos Fiscais de Mercadoria referentes à operações Normais
Campo 04 – NORM_DEV = “1” da SAFX07
Notas cuja a data fiscal seja = ao campo dat_di,recuperado da nota de saída.A prioridade será a informação contida no item, caso não exista, consideraremos a da capa do documento.
Notas cujos campos NUM_DOCFIS, SERIE_DOCFISe SUB_SERIE_DOCFIS correspondam aos campos 16 – NUM_DOCFIS_REF, 17 – SERIE_DOCFIS_REF, 18 – S_SER_DOCFIS_REF da capa da nota de saída.
Fazer uma comparação entre os itens da nota de saída (devolução), com os itens da nota de entrada (compra). Caso não exista correspondência, nada será feito.
Ao identificarmos as notas de entrada, devemos nos certificar que a mesma foi considerada no período, desta forma, a nota de entrada deve conter obrigatoriamente o campo “Data do lançamento” preenchido com uma data no mês/ano da geração dos ajustes, caso contrário, a nota não deverá ser considerada.
Caso não tenha sido encontrada a nota de entrada, apresentar msg no log, informando o ocorrido: “ A nota de entrada XXX, não foi encontrada na base”
Caso exista na nota de saída algum item que não foi encontrado na nota de entrada,o mesmo deve ser exibido no relatório, porem exibir a seguinte msg no log: “ O item YYY não foi encontrado na nota de entrada XXX”.
	OS3169-GE20		RN06	Devem ser apresentados no relatório os grupos de notas que estejam associados no formato saídas/entradas.Ou seja, mostrar a nota de devolução e em seguida a nota da compra que originou a devolução.  Caso a nota de entrada não tenha sido identificada, a nota de saída tb não deve ser apresentada no relatório.
Na geração centralizada, o relatório deve apresentar as notas de saída/entrada por estabelecimento.	OS3169-GE20		RN07	Os seguintes campos deverão ser disponibilizados no relatório de Notas Fiscais de Devolução de Compra:

Nº NF de S/E
Data Fiscal
Nº Item 
Qtde
Desc Prod
Valor Unit
Aliq. PIS
Base PIS
Valor PIS
Aliq. COFINS
Base COFINS
Valor COFINS 
	OS3169-GE20		RN08	Demonstrativo de Notas de Devolução de Compra – Dentro do Mês da Apuração
Período de dd/mm/aaaa até dd/mm/aaaa


Nº NF de S/E
Data Fiscal
Nº Item
Qtde
Desc Prod
Valor Unit

Aliq.
PIS
Base

Valor

Aliq.
COFINS
Base

Valor

Saída


1010 (S)
11/01/2011
001
01
001
1.000,00
1,00
1.000,00
10,00
1,00
1.000,00
10,00


002
01
002
1.000,00
1,00
1.000,00
10,00
1,00
1.000,00
10,00

Entrada


2020 (E)
05/01/2011
001
01
001
1.000,00
1,00
1.000,00
10,00
1,00
1.000,00
10,00


002
02
002
1.000,00
1,00
2.000,00
20,00
1,00
2.000,00
20,00


Saída


1111 (S)
17/01/2011
001
01
005
5.000,00
1,00
5.000,00
50,00
1,00
5.000,00
50,00


002
02
008
5.000,00
1,00
10.000,00
100,00
1,00
10.000,00
100,00

Entrada


1015 (E)
08/01/2011
001
01
005
5.000,00
1,00
5.000,00
50,00
1,00
5.000,00
50,00


002
02
008
5.000,00
1,00
5.000,00
100,00
1,00
10.000,00
100,00


	OS3169-GE20		RN09	Apenas para Produto TAXONE 
 
Migrar o relatório para o servidor de relatórios. 
 
Incluir o campo Tipo de Geração na tela de geração do Relatório Demonstrativo – Notas de Devolução de Compra Dentro do Mês da Apuração.

Permite escolher a opção de geração. 
Lista de valores válidos: 
Arquivo PDF 
Excel (XLSX) 
  
A opção default é “Arquivo PDF” 
	MFS-693073		RN10	Formato EXCEL 

Criar o formato em Excel (XLSX), considerando as mesmas colunas apresentadas no formato em PDF. 	MFS-693073		

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN