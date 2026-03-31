# MTZ_Tela_Manutenção_Fornecimento_de_Energia_Eletrica_Agua_Canalizada_Gas_Consolidados_SAFX190_SAFX191

> Fonte: MTZ_Tela_Manutenção_Fornecimento_de_Energia_Eletrica_Agua_Canalizada_Gas_Consolidados_SAFX190_SAFX191.doc

EFD-Escrituração Fiscal Digital das Contribuições – Fornecimento de Energia Elétrica, Água Canalizada e Gás - Consolidados (SAFX190/191)

Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Manutenção >> Notas de Fornecimento de Energia Elétrica, Água Canalizada e Gás (C600)

DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS4316	Inclusão de campo	Incluir o campo Código e Descrição da SCP		CH1749_2017
(MFS-9515)	Alteração do campo 12-Valor Total acumulado dos documentos	Alteração do campo Valor Total acumulado da capa dos documentos e do campo Valor Acumulado do Item para não obrigatório.		MFS29621	Andréa Rocha	Alterar a regra do campo Modelo de documento		MFS33637	Andréa Rocha	Inclusão do modelo 66 para o campo Modelo de documento		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Regra Geral		RN01	Deverá ser criado o campo Código da SCP, acompanhado da pasta de seleção da informação e o campo de texto para demonstração da descrição vinculada ao código.

Quando acionada a pasta, serão demonstrados os registros da tabela SAFX2057 – Cadastro da SCP. Para o código selecionado, será demonstrada também a descrição da SCP.

Nome do campo em tela: “Código da SCP:”

Caso o usuário informe um código que não tenha cadastro correspondente na SAFX2057, retornar a mensagem de erro: “Cadastro da SCP não encontrado”.	OS4316		RN02	Campo Valor Total Acumulado – Capa

[ALTERADA - CH1749_2017 (MFS-9515)]
Preenchimento não obrigatório do valor total acumulado da capa dos documentos fiscais. Caso não preenchido emitir a mensagem na tela: “O campo Valor Total Acumulado dos documentos é obrigatório e deverá ser maior que zero.”.	CH1749_2017
(MFS-9515)		RN03	Campo Valor Acumulado do Item – Item

[ALTERADA - CH1749_2017 (MFS-9515)]
Preenchimento não obrigatório do valor acumulado do item dos documentos fiscais. Caso não preenchido emitir a mensagem na tela: “O campo Valor do Total do Item é obrigatório e deverá ser maior que zero.”.	CH1749_2017
(MFS-9515)		RN04	Campo Modelo – Capa

[MFS29621]
[MFS33637] – Inclusão do modelo 66

Este campo trabalha com janela de seleção dos códigos de modelo da Tabela de Modelos de Documento (SAFX2024), somente serão disponibilizados os códigos de modelos iguais a “01”, “06”, “28”, “29”, “55” e “66”.

Serão disponibilizados para seleção apenas os códigos do Grupo em questão (de acordo com o Estabelecimento e a data do documento)

Quando o código for digitado, será validada a sua existência na SAFX2024. Caso não exista, a operação não será salva e será exibida mensagem de erro padrão.
	MFS29621/
MFS33637		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN