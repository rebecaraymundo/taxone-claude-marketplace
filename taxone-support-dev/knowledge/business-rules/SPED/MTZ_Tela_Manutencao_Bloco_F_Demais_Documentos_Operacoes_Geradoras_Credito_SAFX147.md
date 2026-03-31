# MTZ_Tela_Manutenção_Bloco F_Demais_Documentos_Operacoes_Geradoras_Credito_SAFX147

> Fonte: MTZ_Tela_Manutenção_Bloco F_Demais_Documentos_Operacoes_Geradoras_Credito_SAFX147.doc

EFD-Escrituração Fiscal Digital das Contribuições – Demais Documentos e Operações Geradoras de Crédito (SAFX147)

Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Manutenção >> Registro do Bloco F >> Demais Documentos e Operações Geradoras de Contribuição e Crédito (F100)


DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data		OS4316	Inclusão de campo	Incluir o campo Código e Descrição da SCP		OS4579	Alteração de Campo	Alteração no tamanho do campo Número do Lançamento		OS4368	Alteração do Relatório	Este documento tem como objetivo alterar o relatório dos demais documentos e operações geradoras de créditos incluindo a data de operação inicial e final para filtro.		MFS36163	Liiane Assaf	Inclusão dos Códigos Situação Tributária PIS e COFINS (RN13,RN14 e RN15)	15/07/2020		

REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Regra Geral da Tela
Esta tela tem como objetivo permitir incluir, alterar, excluir os registros de Demais Documentos e Operações Geradoras de Crédito. Com base nessas informações o registro F100 é gerado e apresentado no Meio Magnético do EFD-Contribuições.

Além da tela os registros de  Demais Documentos e Operações Geradoras de Crédito podem ser carregados via importação da SAFX147.

Nome da Tabela Física: X147_OPER_CRED
Campos Chave de Identificação:
- Código da Empresa
- Código do Estabelecimento
- Tipo de Documento
- Data Operação
- Numero, Série e Subsério do Documento
- Número do Lançamento
- Pessoa Fis/Jur
- Produto
- Conta Contábi
- Centro de Custo

Campos Obrigatórios:
- Código da Empresa
- Código do Estabelecimento
- Tipo de Documento
- Data Operação
		RN01	Regra do Relatório da Tela

Na opção de geração do relatório dos demais documentos e operações geradoras de créditos, localizado na manutenção dos registros, deverá conter os seguintes campos para filtro de acordo com os campos da tabela:

[ALTERADA – OS4368]
Código Empresa
Código Estabelecimento
Número do documento
Série do documento
Sub Série do documento
Número do lançamento
Código do documento
Indicador da Pessoa Física/Jurídica
Código da Pessoa Física/Jurídica
Indicador do produto
Código do produto
Data de operação
Valor da operação
Valor Base PIS
Valor alíquota PIS
Valor PIS
Valor Base COFINS
Valor alíquota COFINS
Valor COFINS
Indicador da origem do crédito
Código da conta
Código do centro de custo
Descrição complementar

Tratamento:
O campo “Data de operação” permitirá inserir um range do período devendo aceitar o conteúdo em formato DD/MM/AAAA, ou seja, condição “between XX/XX/XXXX (data inicial) and XX/XX/XXXX (data final)”.
Se período inicial maior que período final preenchidos no filtro desconsiderar todos os registros ignorando o tratamento;
Será mantido o formato anterior XX/XX/XXXX para filtro sem range trazendo apenas aquele período preenchido.

Atenção: Os tratamentos serão orientados aos usuários via manual operacional.

Observação: nome dos campos em tabela confeccionados pelo A&D.
	OS4368		RN02	Campo Estabelecimento
Lista composta pelos Estabelecimentos da Empresa de login.		RN03	Campos  Nr Documento/Operação, Série e Sub Série
Campos texto.
		RN04	Campo Número do Lançamento

Campo texto. 
Alterado para suportar até 40 caracteres.
	OS4579		RN05	Campo Data Operação
Campo obrigatório		RN06	Campo Valor Operação
Campo texto. 
		RN07	Campo Pessoa Fis/Jur:
Apresentar: Pastinha + Grupo + Código + Descrição
Origem: Tabela de Cadastro da Pessa Física Jurídica (SAFX04) 
		RN08	Campo Produto:
Apresentar: Pastinha + Grupo + Código + Descrição
Origem: Tabela de Cadastro de Produto (SAFX2013) 
		RN09	Campo Tipo de Documento:
Apresentar: Pastinha + Grupo + Código + Descrição
Origem: Tabela de Cadastro de Tipos de Documento (SAFX2005) 
		RN10	Campos Base PIS, Aliquota PIS e Valor PIS
Campo texto. 
		RN11	Campos Base COFINS, Aliquota COFINS e Valor COFINS
Campo texto. 
		RN12	Campo Orige do Crédito:
Lista composta pelos valores:
0 – Operação no Mercado Interno1 – Operação de Importação		RN13	Campo Código Situação Tributária PIS
Apresentar Pastinha + Código + Descrição
Origem: Tabela de Códigos Situação Tributária (TACES 65) - Y2027_SIT_TRIBUTARIA
Label: Cód. Sit. Trib. PIS
Nome do Campo na tabela: COD_SITUACAO_PIS

Regra de consulta à Tabela de Códigos Situação Tributária (TACES 65) - Y2027_SIT_TRIBUTARIA:
Esta regra é aplicada:
- Na recuperação dos registros via pastinha;
- Ao digitar um código no campo texto
- No relatório da tela.

A consulta à Tabela de Códigos Situação Tributária (TACES65) - Y2027_SIT_TRIBUTARIA, deve considerar os seguintes critérios:
- Data Início Validade <= Data da Operação informada;
- Indicador  = 1 – PIS
Recuperar o registro de maior validade que atenda aos critérios acima.

Caso o código do PIS informado não exista na tabela, exibir a seguinte mensagem ao salvar o registro:
91627 - Codigo da Situacao Tributaria PIS inexistente ou invalido para a data do documento.
	MFS36163		RN14	Campo Código Situação Tributária COFINS
Apresentar Pastinha + Código + Descrição
Origem: Tabela de Códigos Situação Tributária (TACES 65) - Y2027_SIT_TRIBUTARIA
Label: Cód. Sit. Trib. COFINS
Nome do Campo na tabela: COD_SITUACAO_COFINS

Regra de consulta à Tabela de Códigos Situação Tributária (TACES 65) - Y2027_SIT_TRIBUTARIA:
Esta regra é aplicada:
- Na recuperação dos registros via pastinha;
- Ao digitar um código no campo texto
- No relatório da tela.

A consulta à Tabela de Códigos Situação Tributária (TACES65) - Y2027_SIT_TRIBUTARIA, deve considerar os seguintes critérios:
- Data Início Validade <= Data da Operação informada;
- Indicador  = 2 - COFINS
Recuperar o registro de maior validade que atenda aos critérios acima.

Caso o código do COFINS informado não exista na tabela, exibir a seguinte mensagem ao salvar o registro:
91628 - Codigo da Situacao Tributaria COFINS inexistente ou invalido para a data do documento.
	MFS36163		RN15	Campo Código da Natureza da Receita

Apresentar: Pastinha + Código + Descrição
Origem: Tabela de Código da Natureza da Receita (TACES72) - DWT_NAT_REC.

Regra de consulta à Tabela de Código da Natureza da Receita (TACES72) - DWT_NAT_REC:
Esta regra é aplicada:
- Na recuperação dos registros via pastinha;
- Ao digitar um código no campo texto
- No relatório da tela.

A recuperação das informações da tabela DWT_NAT_REC, depente dos Códigos de Situação Tributária do Pis e Cofins:
Se pelo menos um dos códigos de Situação Tributária PIS ou COFINS (COD_SITUACAO_PIS, COD_SITUACAO_COFINS ) estiverem preenchidos, então:
A consulta à Tabela de Código da Natureza da Receita (TACES72) - DWT_NAT_REC, deve considerar os critérios:
- Código da Natureza da Receita = código informado via digitação.
- Data Início Validade <=  a Data da Operação informada
- Código do CST PIS/COFINS:
Se Código Situação Tributária PIS (COD_SITUACAO_PIS) estiver preenchido, então:
Código do CST PIS/COFINS = Código Situação Tributária PIS (COD_SITUACAO_PIS);
Senão
Se Código Situação Tributária COFINS (COD_SITUACAO_COFINS) estiver preenchido, então:
Código do CST PIS/COFINS = ao Código Situação Tributária COFINS (COD_SITUACAO_COFINS);
Recuperar o registro de maior validade que atenda aos critérios acima.

Se os códigos de Situação Tributária PIS e COFINS (COD_SITUACAO_PIS, COD_SITUACAO_COFINS) NÃO estiverem preenchidos, então:
A consulta à Tabela de Código da Natureza da Receita (TACES72) - DWT_NAT_REC, deve considerar os critérios:
- Código da Natureza da Receita = código informado;
- Data Início Validade <=  a Data da Operação informada;
Recuperar o registro de maior validade que atenda aos critérios acima.

Caso o código de natureza da receita digitado não exista na tabela, exibir a seguinte mensagem ao salvar o registro:
92141 - Natureza da Receita nao Cadastrada.
	MFS36163		RN16	Campo Código Conta:
Apresentar: Pastinha + Código + Descrição
Origem: Tabela do Plano de Contas (SAFX2002) 
		RN17	Campo Código Custo:
Apresentar: Pastinha + Código + Descrição
Origem: Tabela de Centro de Custo (SAFX2003) 
		RN18	Campo Código SCP:
Deverá ser criado o campo Código da SCP, acompanhado da pasta de seleção da informação e o campo de texto para demonstração da descrição vinculada ao código.

Quando acionada a pasta, serão demonstrados os registros da tabela SAFX2057 – Cadastro da SCP. Para o código selecionado, será demonstrada também a descrição da SCP.

Nome do campo em tela: “Código da SCP:”

Caso o usuário informe um código que não tenha cadastro correspondente na SAFX2057, retornar a mensagem de erro: “Cadastro da SCP não encontrado”.	OS4316		RN19	Campo Descrição Complementar

Campo texto.
		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN