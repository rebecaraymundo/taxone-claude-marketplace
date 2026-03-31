# MTZ_Tela_Manutenção_Bloco F_Bens_Incorporados_ao_Ativo_Imobilizado_SAFX148

> Fonte: MTZ_Tela_Manutenção_Bloco F_Bens_Incorporados_ao_Ativo_Imobilizado_SAFX148.doc

EFD-Escrituração Fiscal Digital das Contribuições – Bens do Ativo Imobilizado Com Base nos Encargos de Depreciação e no valor de aquisição (SAFX148)

Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Manutenção >> Registro do Bloco F >> Bens Incorporados ao Ativo Imobilizado


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS4316	Inclusão de campo	Incluir o campo Código e Descrição da SCP		OS4424	Alteração no Cadastro	Incluir mais de um registro com o mesmo grupo do bem do ativo imobilizado		MFS24819	Inclusão de campo na chave	Incluir o campo Centro de Custo na chave de identificação do registro.		MFS-626368	Alessandra Cristina Navatta	Inclusão do campo Número da Parcela do CREDPIS (este campo não foi criado por esta demanda), apenas foi documentado (reversa – RN28)

Inclusão dos campos Data da Baixa (RN29) e Indicador do Motivo da Baixa (RN30) na tela.		MFS-651783	Alessandra Cristina Navatta	(APENAS PRODUTO TAXONE) Atualização da CREDPIS_CONTROLE (quando existir registro para o bem) e quando for informado os campos Data da Baixa (RN29) e Indicador do Motivo da Baixa (RN30)		MFS-677419	
Alessandra Cristina Navatta	Exclusão da regra de atualização da CREDPIS_CONTROLE, quando o campo Data da Baixa e Motivo da Baixa for preenchido pela SAFX148 e já existir na CREDPIS_CONTROLE. Essa exclusão se deu, pois, a partir desta demanda, não será possível alterar registros de indicador de origem dos dados = CREDPIS. (RN29 e RN30).
Inclusão dos campos de Data da Baixa e Indicador do Motivo da Baixa, no filtro do botão ABRIR (tollbar) e no relatório da tela (RN31 e RN32)
No campo Indicador do Motivo da baixa, apresentar o indicador e a descrição do campo no formato (RN30)		
REGRAS DE NEGÓCIO

Tela

Cód.	Descrição	DR		RN00	Regra Geral

Esta tela tem como objetivo de promover a manutenção dos registros de Bens Incorporados ao Ativo Imobilizado.
Além da manutenção, os Bens Incorporados ao Ativo Imobilizado podem ser carregados via SAFX148.
Os Processos Referenciados são registros filhos dos Bens Incorporados ao Ativo Imobilizado. A manutenção dos Processos Referenciados está disponível nesta mesma funcionalidade.
Os campos que compõe a chave de identificação dos Bens Incorporados ao Ativo Imobilizado (SAFX148) são:
- Código da Empresa
- Código do Estabelecimento
- Indicador de Operações Geradoras de Créditos
- Código do Grupo de Bens do Ativo Imobilizado
- Código do Bem do Ativo Imobilizado
- Código do Incorporador do Bem do Ativo Imobilizado
- Data de Lançamento de Crédito
- Indicador da Origem do Crédito do Bem
- Mês/Ano de Aquisição do Bem
- Código da Situação Tributária do PIS/PASEP
- Código de Situação Tributária do COFINS
- Indicador do Número de Parcelas a serem apropriadas
- Conta Contábil
- Centro de Custo

Os campos que compõe a chave de identificação dos Processos Referenciados são:
- Código da Empresa
- Código do Estabelecimento
- Indicador de Operações Geradoras de Créditos
- Código do Grupo de Bens do Ativo Imobilizado
- Código do Bem do Ativo Imobilizado
- Código do Incorporador do Bem do Ativo Imobilizado
- Data de Lançamento de Crédito
- Indicador da Origem do Crédito do Bem
- Mês/Ano de Aquisição do Bem
- Código da Situação Tributária do PIS/PASEP
- Código de Situação Tributária do COFINS
- Indicador do Número de Parcelas a serem apropriadas
- Conta Contábil
- Centro de Custo
- Número do Processo
- Indicador da Origem do Processo

Botões: Novo, Abre, Exclui, Confirma, Registro F129/F139 – Processo Referenciado, Relatório, Fecha.

Numa alteração de registro já existente, os campos chave ficam bloqueados para alteração.
	MFS24819		RN01	Regra do Campo Estabelecimento

Lista de Estabelecimentos da empresa de login.
Caso o Estabelecimento seja informado este campo deve ser apresentado bloqueado.
Campo obrigatório.
Caso o usuário não preencha este campo ao salvar o registro, o sistema deve exibir a seguinte mensagem:
“O campo Estabelecimento deve ser informado”
		RN02	Regra do Campo Data de Lançamento de Crédito

Campo obrigatório.
Caso o usuário não preencha este campo ao salvar o registro, o sistema deve exibir a seguinte mensagem:
“O campo Data de Lançamento deve ser informado”
		RN03	Regra do Campo Operações Geradoras de Créditos

Lista composta pelos seguintes itens:
1 – Com Base nos Encargos de Depreciação
2 – Com  Base nos Encargos de Amortização
3 – Com Base no Valor de Aquisição/Contribuição

Campo obrigatório.
Caso o usuário não preencha este campo ao salvar o registro, o sistema deve exibir a seguinte mensagem:
“O campo Ind. de Operações Geradoras de Crédito deve ser informado”
		RN04	Regra do Campo Grupo do Bem do Ativo Imobilizado

Grupo do Bem do Ativo Imobilizado: Será informada a Identificação dos Bens no Ativo Imobilizado de acordo com:

1- Edificações e Benfeitorias em Imóveis Próprios;
2- Edificações e Benfeitorias em Imóveis de Terceiros;
3- Instalações;
4- Máquinas;
5- Equipamentos;
6- Veículos;
99- Outras Situações. 
     
Possibilitar N cadastros de bens do ativo imobilizado com o mesmo código do grupo de bens do Ativo imobilizado, identificação do bem campo 04 (COD_GRUPO_BEM) da SAFX148, este código também será utilizado na SAFX2053 Cadastro do Grupo de Bem do Ativo Imobilizado (EFD-PIS/PASEP – COFINS).

Obs.: A identificação dos bens incorporados ao Ativo Imobilizado a ser informado pode ser realizada de forma individualizada ou por grupos de bens da mesma natureza ou destinação.
	OS4424		RN05	Regra do Campo Bem do Ativo Imobilizado

		RN06	Regra do Campo – Origem do Crédito do Bem

		RN07	Regra do Campo – Utilização do Bem

		RN08	Regra do Campo –  Valor do Encargo 
 
		RN09	Regra do Campo – Valor do Encargo a excluir da base de cálculo

		RN10	Regra do Campo – Mês/Ano de Aquisição
		RN11	Regra do Campo – Valor de Aquisição dos Bens Incorporados
		RN12	Regra do Campo – Parcela do Valor de aquisição de Depreciação no mês
		RN13	Regra do Campo – Base de cálculo do Crédito de PIS/PASEP
		RN14	Regra do Campo – Indicador do Número de Parcelas a serem apropriadas
		RN15	Regra do Campo – Código da Situação Tributária do PIS/PASEP
		RN16	Regra do Campo – Valor da Base de cálculo do PIS
		RN17	Regra do Campo – Alíquota do PIS
		RN18	Regra do Campo – Valor do PIS
		RN19	Regra do Campo – Código de Situação Tributária do COFINS
		RN20	Regra do Campo – Valor da Base de Cálculo da COFINS
		RN21	Regra do Campo – Alíquota da COFINS
		RN22	Regra do Campo – Valor da COFINS
		RN23	Regra do Campo – Conta Contábil
		RN24	Regra do Campo – Centro de Custos
Não obrigatório		RN25	Regra do Campo Código da SCP:
Código da SCP: Pastinha + código + descrição.

Origem da informação: tabela SAFX2057 – Cadastro da SCP. 

Caso o usuário informe um código que não tenha cadastro correspondente na SAFX2057, retornar a mensagem de erro: “Cadastro da SCP não encontrado”.	OS4316		RN26	Regra do Campo – Descrição complementar do bem ou grupo de bens
		RN27	
Regras de Validação:

1) Campos obrigatórios não preenchidos devem ser criticados.
2) Campos relacionados a cadastros, quando preenchidos com um valor inválido, devem ser criticados.


    		RN28	Campo Número da Parcela do CREDPIS

Atenção: O campo de item 30, não foi criado nesta demanda, foi apenas documentado.
	MFS-626368		RN29	Campo Data 

Incluir o campo na tela, conforme indicado no agrupamento Baixa, do mockup.

Tabela: SAFX148
Item: 30
Nome do Campo: Data da Baixa
Nome da tabela: DATA_BAIXA
Tipo: N
Tamanho: 08
Campo Não Obrigatório	


Validação: A data da baixa deve estar no formato correto, caso contrário, exibir a mensagem “Campo 'Data da Baixa' com formato inválido.”

[EXCLUSÃO MFS-677419] [ALTERAÇÃO MFS-651873] Atualização da CREDPIS_CONTROLE (APENAS PRODUTO TAXONE)
Quando o campo “Data da Baixa” for informado e existir o registro na CREDPIS_CONTROLE (deste bem), atualizar os campos: ‘Data da Baixa – DAT_BAIXA, ‘Indicador Motivo da Baixa – MOTIVO_BAIXA’ e o ‘indicador Baixa – IND_BAIXA’.

	MFS-626368
MFS-651873
MFS-677419		RN30	Campo Indicador do Motivo

Incluir o campo na tela, conforme indicado no agrupamento Baixa, do mockup.

Tabela: SAFX148
Item: 31
Nome do Campo: Indicador do Motivo da Baixa
Nome da tabela: IND_MOTIVO_BAIXA
Tipo: A
Tamanho: 01
Campo Não Obrigatório
Comentário: Indicador do Motivo da Baixa do bem, referente aos tributos PIS/PASEP e COFINS. 
Opções válidas: 
1 - Venda
2 - Obsolescência ou sucateamento
3 - Sinistros;
4 - Doação;
6 - Outros;
7 – Automática

[MFS-677419]Formato: Cód_Descrição

Validações: 

Este campo só deve ser habilitado, se o campo ‘Data da Baixa’ for preenchido.

O campo ‘Indicador do Motivo da Baixa’ é de preenchimento obrigatório, quando o campo ‘Data da Baixa’ for informado. Se o campo ‘Data da Baixa’ estiver preenchido e não for indicado o campo ‘Indicador do Motivo da Baixa’, exibir a mensagem: “Campo ‘Indicador do Motivo da Baixa’ é de preenchimento obrigatório, quando o campo ‘Data da Baixa’ estiver preenchido.”

[EXCLUSÃO MFS-677419] [ALTERAÇÃO MFS-651873] Atualização da CREDPIS_CONTROLE (APENAS PRODUTO TAXONE)
Quando o campo “Motivo da Baixa” for informado e existir o registro na CREDPIS_CONTROLE (deste bem), atualizar os campos: ‘Data da Baixa – DAT_BAIXA, ‘Indicador Motivo da Baixa – MOTIVO_BAIXA’ e o ‘indicador Baixa – IND_BAIXA’.


	MFS-626368
MFS-651873
MFS-677419		RN31	Botão Abrir 
Inclusão dos campos de Data da Baixa e Indicador do Motivo da Baixa, no filtro do botão ‘ABRIR’ da toolbar.	MFS-677419		RN32	Relatório da Tela
Inclusão dos campos de Data da Baixa e Indicador do Motivo da Baixa, no filtro do relatório.	MFS-677419		
Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN