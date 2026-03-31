# MTZ_EFD_PIS-COFINS-Geracao_de_Notas_Fiscais_de_Venda_Cancelada

> Fonte: MTZ_EFD_PIS-COFINS-Geracao_de_Notas_Fiscais_de_Venda_Cancelada.doc

TITLE   \* MERGEFORMAT EFD PIS/COFINS - Geração de Notas Fiscais de Venda Cancelada


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS3169-GE27	 TITLE   \* MERGEFORMAT EFD PIS/COFINS - Geração de Notas Fiscais de Venda Cancelada	Através da OS3169-GE13 foi criado um indicador referente à “Venda Cancelada”. Esse campo tem por objetivo identificar os Documentos Fiscais de Saída que representam as Vendas Canceladas. As Vendas Canceladas são aquelas em que após a emissão da Nota Fiscal de saída das Mercadorias, o cliente comprador desiste da venda e devolve em sua totalidade as mercadorias compradas.

Segundo o Guia Prático da EFD PIS/COFINS, o cliente ao devolver a mercadoria justifica o motivo do cancelamento na própria NF que o Fornecedor emitiu. O Fornecedor por sua vez emite uma NF própria referenciando a NF de Saída da Mercadoria para que todos os efeitos da saída da Mercadoria sejam desfeitos.

Nessa OS citada acima, o Documento Fiscal de Saída deve possuir o campo de Venda Cancelada preenchido, sendo assim, as informações desse documento fiscal terão a Base, Alíquota e Valor do Imposto referente à PIS/COFINS zerados no arquivo. 

Embora o sistema já preveja essa situação, alguns clientes solicitaram a automação de um processo que faça isso de forma mais rápida, para que o cliente não precise identificar as notas fiscais uma a uma para aí preencher o campo citado no parágrafo anterior. O volume de notas fiscais canceladas desses cliente é bem alto.		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN01	Deverá ser criada no módulo EFD PIS/COFINS a tela “Geração de Notas Fiscais de Venda Cancelada”. Essa tela será criada no menu Obrigações >> Automação de Devolução/Vendas Canceladas >> Vendas Canceladas >> Geração de Notas Fiscais de Venda Cancelada.

Esse menu “Automação de Devolução/Vendas Canceladas” deverá ser disponibilizado antes do sub-menu “Geração dos Registros”.	OS3169-GE27		RN02	Os seguintes campos deverão ser disponibilizados para a geração das Notas Fiscais de Venda Cancelada:

Data Inicial: deverá ser informada a Data Inicial para geração das Notas Fiscais de Venda Cancelada. Esse campo deverá ser obrigatório de preenchimento e deverá ser do tipo DATA aceitando a informação no formato DD/MM/AAAA.
Data Final: deverá ser informada a Data Final para geração das Notas Fiscais de Venda Cancelada. Esse campo deverá ser obrigatório de preenchimento e deverá ser do tipo DATA aceitando a informação no formato DD/MM/AAAA.
Estabelecimentos: serão informados os Estabelecimentos para geração da informação das notas fiscais de venda cancelada. 

O padrão da tela deverá ser o padrão FRAMEWORK, já utilizado no produto.	OS3169-GE27		RN03	Ao executar o processo o sistema irá realizar o seguinte filtro para recuperação das informações a partir dos Documentos Fiscais:

Os Documentos Fiscais serão recuperados a partir do campo DATA_FISCAL da SAFX07 ou DAT_LANC_PIS_COFINS da SAFX08 que esteja dentro do período informado nos campos “Data Inicial” e “Data Final”.
Para que a NF seja recuperada a partir da DATA_FISCAL o flag “Data de Emissão” deverá estar selecionado no campo “Registro A100, C100, C180 e C190 – Seleção das Operações Geradoras de Receita” do menu Parâmetros >> Dados Iniciais do EFD PIS/COFINS.
Para que a NF seja recuperada a partir da DAT_LANC_PIS_COFINS o flag “Data de Lançamento EFD ´PIS/COFINS” deverá estar selecionado no campo “Registro A100, C100, C180 e C190 – Seleção das Operações Geradoras de Receita” do menu Parâmetros >> Dados Iniciais do EFD PIS/COFINS.
Documentos Fiscais de Mercadoria, referentes a operações de Entrada emitidas pelo próprio Estabelecimento referente a retorno de Mercadorias não entregues aos destinatários
Campo 03 – MOVTO_E_S = “3” da SAFX07
Documentos Fiscais de Mercadoria referentes à operações de Devolução
Campo 04 – NORM_DEV = “2” da SAFX07
Documentos Fiscais de Mercadoria com informação de NF, Série e Subsérie Referenciada
Campo 16 – NUM_DOCFIS_REF preenchido. O preenchimento dos campos 17 – SERIE_DOCFIS_REF e 18 – S_SER_DOCFIS_REF é opcional.
Documentos Fiscais de Mercadoria com informação de Data do Documento de Saída preenchida
Campo 75 – DAT_DI preenchido	OS3169-GE27		RN04	Com base nessas informações o sistema irá identificar esses Documentos de Entrada e a partir do campo 16 – NUM_DOCFIS_REF, 17 – SERIE_DOCFIS_REF, 18 – S_SER_DOCFIS_REF e 75 – DAT_DI o sistema irá identificar essas NF’s de Saída. O sistema deverá comparar as informações do Número da NF Referenciada (campos 16, 17 e 18) e verificar se existe a mesma como Nota Fiscal de Saída. Só assim a mesma poderá ser recuperada.

Após identificar essas NF’s de Saída o sistema irá alterar o campo IND_VENDA_CANC dessas notas para “S”.

Caso o estabelecimento dessa NF de Saída esteja marcado para Equalização Automática do MasterSAF, o sistema deverá atualizar também o campo IND_VENDA_CANC  para “S” na tabela DWT_DOCTO_FISCAL.	OS3169-GE27		RN05	Caso o sistema ao tentar alterar o campo IND_VENDA_CANC para “S” das NF’s de Saída e as mesmas possuírem fechamento no menu Rotinas Acessórias >> Fechamento >> Controle do módulo Ferramentas e essas NF’s possuírem o campo DATA_FISCAL <= a data informada no campo “Data Fechamento” e com o campo Grupo = 3 nessa parametrização, o sistema deverá exibir uma mensagem de erro informando no Log:

Não é permitido alterar Documentos Fiscais quando a Data Fiscal é menor ou igual a Data de Fechamento do Grupo de Documentos.

Além de exibir a mensagem, deverá ser exibida a chave da NF de Saída.	OS3169-GE27		RN06	Caso o sistema ao tentar alterar o campo IND_VENDA_CANC para “S” das NF’s de Saída e as mesmas possuírem fechamento no menu Obrigações >> Status das Obrigações do módulo EFD PIS/COFINS com o campo Situação = Apuração Fechada, o sistema deverá exibir uma mensagem de erro informando no Log:

Não é permitido alterar Documentos Fiscais quando os mesmos já possuem Fechamento para o período de apuração do PIS/COFINS.

Além de exibir a mensagem, deverá ser exibida a chave da NF de Saída.	OS3169-GE27		RN07	Caso o sistema ao alterar o campo IND_VENDA_CANC para “S” da NF de Saída e o sistema verifique que essa NF’s de Saída pertença à um período de apuração anterior ao da NF de Entrada, o sistema irá alterar o campo IND_VENDA_CANC para “S” da mesma forma.

Vale salientar que as NF’s de Saída que estejam dentro do MESMO período de apuração das NF’s de Entrada, terão o campo IND_VENDA_CANC alterado para “S”.	OS3169-GE27		RN08	As regras para geração correta dos Documentos de Vendas Canceladas nos devidos registros do EFD PIS/COFINS já foram desenvolvidas, sendo objeto da OS3169-GE27 ser apenas um facilitador para a parametrização desses documentos fiscais.

Os registros que conterão essas regras são os registros C170 (campos 26, 27, 28, 29, 30, 32, 33, 34, 35 e 36), C181 (campos 06, 07, 08, 09 e 10) e C185 (06, 07, 08, 09 e 10).	OS3169-GE27		RN09	Deverá ser criado no processo de geração das Notas Fiscais de Vendas Canceladas, uma aba para exibir um relatório contendo as informações alteradas.	OS3169-GE27		RN10	As informações a serem exibidas no relatório são:

Nº NF de Saída: deverá ser exibido as NF’s de Saída que foram identificadas (ver RN03-RN04) e que tiveram o campo IND_VENDA_CANC alterado para “S” (ver RN04). Essa informação deve ser recuperada dos campos NUM_DOCFIS, SERIE_DOCFIS e SUB_SERIE_DOCFIS da tabela SAFX07.
Nº NF de Entrada (Retorno): deverá ser exibido as NF’s de Entrada que foram identificadas (ver RN03). Essa informação deve ser recuperada dos campos NUM_DOCFIS, SERIE_DOCFIS e SUB_SERIE_DOCFIS da tabela SAFX07.
Base PIS: deverá ser exibida a Base PIS das NF’s de Saída que foram identificadas (ver RN03-RN04) e que tiveram o campo IND_VENDA_CANC alterado para “S” (ver RN04). Essa informação deve ser recuperada do campo VLR_BASE_PIS da SAFX08 sumarizada, ou seja, os valores dos itens deverão ser somados e exibidos juntos em uma única linha.
Valor PIS: deverá ser exibido o Valor PIS das NF’s de Saída que foram identificadas (ver RN03-RN04) e que tiveram o campo IND_VENDA_CANC alterado para “S” (ver RN04). Essa informação deve ser recuperada do campo VLR_PIS da SAFX08 sumarizada, ou seja, os valores dos itens deverão ser somados e exibidos juntos em uma única linha.
Base COFINS: deverá ser exibida a Base COFINS das NF’s de Saída que foram identificadas (ver RN03-RN04) e que tiveram o campo IND_VENDA_CANC alterado para “S” (ver RN04). Essa informação deve ser recuperada do campo VLR_BASE_COFINS da SAFX08 sumarizada, ou seja, os valores dos itens deverão ser somados e exibidos juntos em uma única linha.
Valor COFINS: deverá ser exibido o Valor COFINS das NF’s de Saída que foram identificadas (ver RN03-RN04) e que tiveram o campo IND_VENDA_CANC alterado para “S” (ver RN04). Essa informação deve ser recuperada do campo VLR_COFINS da SAFX08 sumarizada, ou seja, os valores dos itens deverão ser somados e exibidos juntos em uma única linha.	OS3169-GE27		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN