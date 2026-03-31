# MTZ_EFD_PIS-COFINS_Automacao_dos_Ajustes_de_Devolucao_de_Compra

> Fonte: MTZ_EFD_PIS-COFINS_Automacao_dos_Ajustes_de_Devolucao_de_Compra.doc

TITLE   \* MERGEFORMAT EFD PIS/COFINS - Automação de Devolução de Compra


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS3169-GE20	 TITLE   \* MERGEFORMAT EFD PIS/COFINS - Automação de Devolução de Compra	O objetivo é criar um processo para automatizar os ajustes de devolução de compra, quando esta operação ocorrer em período posterior a da operação da compra ou durante o mesmo período.
Esta solicitação foi feita através dos chamados 108281, 108308, 108310, 111721, 117959 e 121007.
		CH23661_2018
(MFS-21236)	 TITLE   \* MERGEFORMAT EFD PIS/COFINS - Automação de Devolução de Compra	Essa correção tem como finalidade preencher na geração automática da devolução o campo 5 – NUM_DOC com o nº da NF de devolução e demais campos como: série, subsérie e data fiscal nos registros M110 e M510.		MFS97087	Rogério Ohashi	Inclusão de parâmetro para definir o percentual do rateio que será considerado pelo sistema, para considerar o mês de referência de geração.		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN01	Deverá ser criada no módulo EFD PIS/COFINS a tela “Geração Automática dos Ajustes de Devolução de Compra
”Essa tela será criada no Menu: Obrigações >> Automação Devolução de Compra >> Geração Automática dos Ajustes de Devolução de Compra
	OS3169-GE20		RN02	Período para a Geração dos Ajustes: 
 “Nota de  Compra Fora do Período das Notas de Devolução”
“Nota de  Compra Dentro do Período das Notas de Devolução”
“Ambas”


Os seguintes campos deverão ser disponibilizados para a tela de Geração Automática dos Ajustes de Devolução de Compra:

Data Inicial Notas de Devolução: deverá ser informada a Data Inicial para recuperarmos as notas de devolução de compra. Esse campo deverá ser obrigatório de preenchimento e deverá ser do tipo DATA aceitando a informação no formato DD/MM/AAAA.
Data Final Notas de Devolução: deverá ser informada a Data Final para recuperarmos as notas de devolução de compra. Esse campo deverá ser obrigatório de preenchimento e deverá ser do tipo DATA aceitando a informação no formato DD/MM/AAAA.

[ALTERAÇÃO-MFS97087] Tratamento para considerar o percentual do rateio no mês de referência de geração

 Obter Percentual de Rateio: deverá ser informada o período a ser recuperado referente as informações de Percentual de Rateio, considerando:

Mês da Nota de Entrada Original: Caso essa opção for selecionada, o processo será gerado conforme regra original, ou seja, será considerado o Percentual de Rateio conforme período da Nota Fiscal de Origem. Default Marcado. 

Mês de Referência Informado: Caso essa opção for selecionada, o sistema passará a considerar somente o Rateio proporcional do período de Referência indicado em tela.

Obs:. Esse parâmetro foi incluído para os clientes que possuem diferença entre os períodos em relação ao percentual informado no Rateio Proporcional entre a Nota de Origem x Nota de Devolução, causando erros na geração dos Registros M100/M500 e M105/M505 por Tipo de Crédito. 

Estabelecimentos: serão informados os Estabelecimentos para Geração Automática dos Ajustes de Devolução de Compra. Serão exibidos os estabelecimentos CENTRALIZADORES e os estabelecimentos NÃO CENTRALIZADOS, conforme layout da tela.

	OS3169-GE20
MFS97087		RN03	Criticas para a Execução do Processo:

1 – Se os parâmetros de datas estiverem em meses diferentes, abortar a geração exibindo msg de erro no log.
2 – O sistema deve verificar se existe apuração realizada (com base no período informado pelo usuário) , caso não exista dar a seguinte msg no log, abortando a geração: “Não existe apuração realizada no período informado para a geração”.
3- Se status da apuração estiver diferente de ‘Apuração Realizada’, apresentar a seguinte msg no log, abortando a geração: “Para a realização desta geração o período de apuração deve estar com a situação igual a Realizada”.
 	OS3169-GE20		RN04	Limpeza dos Dados:

Realizar a exclusão dos lançamentos de redução que possuam as mesmas características dos lançamentos que foram gerados pela rotina, considerando o período de apuração e critérios abaixo:

COD_REG = “110” ou “510”
IND_AJ = “0”
COD_AJ= “06”
IND_GRAVACAO = ‘6’
	OS3169-GE20		RN05	Ao executar o processo o sistema irá realizar os filtros informados abaixo para a recuperação das informações a partir dos Documentos Fiscais dos estabelecimentos que estão selecionados na tela:

Os Documentos Fiscais serão recuperados a partir do campo DATA_FISCAL e ou DTA do LANCAMENTO PIS/COFINS que esteja dentro do período informado nos campos “Data Inicial” e “Data Final”. 
A definição de qual data será considerada, será baseada na informação do parâmetro “Registro A100, C100,C180 e C190 – Seleção das Operações Geradoras de Receita”  para definir se as notas devem ser recuperadas pela Data Fiscal ou pela Data Lancamento PIS/COFINS
IMPORTANTE: se a data utilizada for a DTA do LANCAMENTO PIS/COFINS , considerar primeiro a data informada no item, caso não esteja preenchida, considerar a data da capa da nota.
Documentos Fiscais de Mercadoria ou Mistas, referentes a operações de Saida 
Campo 03 – MOVTO_E_S = “9” da SAFX07
Documentos Fiscais de Mercadoria referentes à operações de Devolução
Campo 04 – NORM_DEV = “2” da SAFX07
Documentos Fiscais de Mercadoria com informação de NF, Série e Subsérie Referenciada
Campo 16 – NUM_DOCFIS_REF preenchido. O preenchimento dos campos 17 – SERIE_DOCFIS_REF e 18 – S_SER_DOCFIS_REF é opcional.
Documentos Fiscais de Mercadoria com informação de Data do Documento de Saída preenchida
Campo 75 – DAT_DI preenchido
	OS3169-GE20		RN06	Com base nessas informações, devemos buscar as notas de compra, utilizando os seguintes critérios:

-empresa do login
-estabelecimento selecionado na tela
- Campo 03 – MOVTO_E_S = “1” da SAFX07
- Campo 04 – NORM_DEV = “1” da SAFX07
- Notas cuja a data fiscal seja = ao campo dat_di,recuperado da nota de saída.A prioridade será a informação contida no item, caso não exista, consideraremos a da capa do documento.
- Notas cujos campos NUM_DOCFIS, SERIE_DOCFISe SUB_SERIE_DOCFIS correspondam aos campos 16 – NUM_DOCFIS_REF, 17 – SERIE_DOCFIS_REF, 18 – S_SER_DOCFIS_REF. 
-fazer uma comparação entre os itens da nota de saída (devolução), com os itens da nota de entrada (compra). Caso não exista correspondência, nada será feito.
- Ao identificarmos as notas de entrada, devemos nos certificar que a mesma foi considerada no período anterior, desta forma, a nota de entrada deve conter obrigatoriamente o campo “Data do lançamento” preenchido com uma data anterior ao mês/ano da geração dos ajustes, caso contrário, a nota não deverá ser considerada. Este passo só será realizado se a geração for feita na aba “Nota de  Compra Fora do Período das Notas de Devolução”), senão, ou seja, se o processo for executado na aba ““Nota de  Compra Dentro do Período das Notas de Devolução” a nota de entrada deve conter obrigatoriamente o campo “Data do lançamento” preenchido com uma data igual ao mês/ano da geração dos ajustes, caso contrário, a nota não deverá ser considerada.
- Caso não tenha sido encontrada a nota de entrada, apresentar msg no log, informando o ocorrido.
	OS3169-GE20		RN07	Deverá ser criada no processo de Geração Automática dos Ajustes de Devolução de Compra, uma aba para exibir um relatório contendo as notas que foram gravadas no M110 e M510.	OS3169-GE20		RN08	As informações a serem exibidas no relatório são:

Nº NF de Devolução (Saída): deverá ser exibido o número da NF de Devolução, que está informado no campo 08 – NUM_DOCFIS 16 - NUM_DOCFIS_REF da SAFX07. O preenchimento dos campos 09 - SERIE_DOCFIS e 10- SUB_SERIE_DOCFIS 17 – SERIE_DOCFIS_REF e 18 – S_SER_DOCFIS_REF são opcionais, ou da X116_docfis_ref, quando existir mais de um documento referenciado.
Data Fiscal: Deverá ser exibida a data fiscal da nota.
Código Registro: Indica se o registro é de PIS (M110) ou COFINS (M510)
Código de Tipo de Crédito: Mostra o tipo de crédito da Nota de entrada.
Base: deverá ser exibida a Base PIS/COFINS das NF’s de Entrada que foram identificadas.Essa informação deve ser recuperada do campo VLR_BASE_PIS / VLR_BASE_COFINS da SAFX08 sumarizada, ou seja, os valores dos itens deverão ser somados e exibidos juntos em uma única linha.
Alíquota: Informar a alíquota do PIS/COFINS , que deve ser recuperada da SAFX08
Valor: deverá ser exibido o Valor PIS/COFINS das NF’s de Entrada que foram identificadas.Essa informação deve ser recuperada dos campos VLR_PIS/VLR_COFINS da SAFX08 sumarizada, ou seja, os valores dos itens deverão ser somados e exibidos juntos em uma única linha.


Nº NF de Devolução (Saída)
Data Fiscal
Código Registro
Código de Tipo de Crédito
Base
Aliquota
Valor 


1010 / / 
11/01/2011
M110
101
1.000,00
1,65
1650,00


M510
101
1000,00
7,60
7600,00


	OS3169-GE20
CH23661_2018
MFS21236		RN09	
Após a recuperação dos dados, para cada correspondência correta, entre os itens da nota de saída com a nota de entrada, o sistema deve alimentar a tabela EPC_REG_AJT_M110_M510.

Definição do Tipo de Crédito:
Considerando cada tipo de crédito dos itens da nota de entrada e os demais campos da nota de saída. Temos que recuperar todas as informações necessárias para a criação de um registro C170 para então realizarmos o processo da apuração do credito deste registro, no entanto, este processo será executado com a finalidade de gravarmos o resultado final na forma de ajustes nos registros M110 e M510. Com posse destas informações, será necessário processar os cálculos para cada tipo de credito, utilizando os processos já existentes que fazem a apuração dos créditos no PIS/COFINS  (conforme RNM100-02). Devem ser inseridos os registros M110 e M510 (conforme definido abaixo), que deverão ser colocados abaixo do registro M100 ou M500 correspondente, considerando o código do tipo de credito, o indicador de origem do crédito e as alíquotas existentes na nota fiscal de entrada. O registro será gravado por nota, para garantirmos o maior numero de notas de devolução que serão consideradas sem que o Total do Crédito Disponível Relativo ao Período do registro M100 fique negativo.
Em cima do valor das operações de incidência não cumulativa, de acordo com o CST será aplicado o % do rateio, gravando um registro M110/M510 para cada código de crédito que existir no período da geração (Operações  tributadas no Mercado Interno, Não tributadas no Mercado Interno e Exportações). 
Quando a incidência tributária for exclusiva cumulativa ou cumulativa e não cumulativa o campo VL_BC_PIS_CUM: deverá ser igual ao campo 04- VL_BC_PIS_TOT do registro M105 multiplicado pelo o resultado (campo 05- REC_BRU_CUM do registro 0111 dividido pelo o campo 06- REC_BRU_TOTAL do registro 0111). Mais detalhes sobre o % do rateio, verificar a RNM105 (RNM105-05, RNM105-06, RNM105-07). 
Para a geração do processo, se o tipo de crédito da nota de origem, não existir na apuração que a nota de devolução foi criada, iremos informar no log que a nota não foi considerada no processo de automatização.
Msg log: Não foi considerada a NF XXXX, pois não foi encontrado o mesmo tipo de crédito no período. 
	OS3169-GE20		RN09	PIS/PASEP - M110

Tipo Ajuste: 0 – Redução
Valor do Ajuste: VLR_PIS da SAFX08
Código do Ajuste: 06 – Estorno
Nº Processo / Documento/Ato Concessório Vinculado: campo 08 – NUM_DOCFIS 16 - NUM_DOCFIS_REF da SAFX07. O preenchimento dos campos 09 - SERIE_DOCFIS e 10- SUB_SERIE_DOCFIS 17 – SERIE_DOCFIS_REF e 18 – S_SER_DOCFIS_REF é opcional. A gravação deve ser feita no formato numero/serie/subserie.
Descrição Resumida: Campo 14 - DSC_COMPLEMENTAR da SAFX112, quando campo 15 – VINCULACAO for igual a 2 - EFD PIS/COFINS. Caso exista mais de uma descrição complementar para a nota, deve ser considerada a 1ª descrição. Este campo possui 400 caracteres, truncar o valor caso necessário.
Data da Referencia:  Campo 75 – DAT_DI da SAFX 07, no formato: DD/MM/AAAA.
Data Fiscal da SAFX07 no formato: DD/MM/AAAA.

COFINS - M510

Tipo Ajuste: 0 – Redução
Valor do Ajuste: VLR_COFINS da SAFX08
Código do Ajuste: 06 – Estorno
Nº Processo / Documento/Ato Concessório Vinculado: campo 08 – NUM_DOCFIS 16 - NUM_DOCFIS_REF da SAFX07. O preenchimento dos campos 09 - SERIE_DOCFIS e 10- SUB_SERIE_DOCFIS 17 – SERIE_DOCFIS_REF e 18 – S_SER_DOCFIS_REF é opcional. A gravação deve ser feita no formato numero/serie/subserie.
Descrição resumida: Campo 14 - DSC_COMPLEMENTAR da SAFX112, quando campo 15 – VINCULACAO
for igual a 2 - EFD PIS/COFINS. Caso exista mais de uma descrição complementar para a nota, deve ser considerada a 1ª descrição.Este campo possui 400 caracteres, truncar o valor caso necessário.
Data da Referencia:  Campo 75 – DAT_DI da SAFX 07, no formato: DD/MM/AAAA.
Data Fiscal da SAFX07 no formato: DD/MM/AAAA.	OS3169-GE20
CH23661_2018
MFS21236		RN10	 Mensagem de Log:

Se o “Valor do Ajuste” for maior que o “Valor Total do Crédito Disponível Relativo ao Período”, dar a seguinte mensagem: 
M110/M510 – Valor Total do Crédito Disponível Relativo ao Período do registro M100 negativo.
	OS3169-GE20		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN