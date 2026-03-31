# MTZ_Tela_Manutenção_Prestacao_de_Servicos_de_Comunicacao_e_de _elecomunicacao_Consolidadas_SAFX161

> Fonte: MTZ_Tela_Manutenção_Prestacao_de_Servicos_de_Comunicacao_e_de _elecomunicacao_Consolidadas_SAFX161.doc

EFD-Escrituração Fiscal Digital das Contribuições – Prestação de Serviços de Comunicação e de Telecomunicação Consolidadas (SAFX161)

Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Manutenção >> Notas de Prestação de Serviços de Comunicação e de Telecomunicação Consolidadas (D600)

DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS4316	Inclusão de campo	Incluir o campo Código e Descrição da SCP		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Regra Geral		RN01	Deverá ser criado o campo Código da SCP, acompanhado da pasta de seleção da informação e o campo de texto para demonstração da descrição vinculada ao código.

Quando acionada a pasta, serão demonstrados os registros da tabela SAFX2057 – Cadastro da SCP. Para o código selecionado, será demonstrada também a descrição da SCP.

Nome do campo em tela: “Código da SCP:”

Caso o usuário informe um código que não tenha cadastro correspondente na SAFX2057, retornar a mensagem de erro: “Cadastro da SCP não encontrado”.	OS4316		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN