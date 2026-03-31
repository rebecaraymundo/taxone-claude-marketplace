# Associacao_da_Tabela_Dinamica_com_o_Plano_Empresa-SAFX2106

> Fonte: Associacao_da_Tabela_Dinamica_com_o_Plano_Empresa-SAFX2106.doc

THOMSON REUTERS

 DOCPROPERTY  Title  \* MERGEFORMAT Regras de Importação Online e Batch SAFX2106
Associação da Tabela Dinâmica com o Plano Empresa 
ECF - Escrituração Contábil Fiscal (DW)

DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		19/10/2017	MFS-14166	Criação do documento	Alessandra Cristina Navatta		02/10/2018	MFS-21398	Exclusão dos campos de data (inicial e final) de vigência da conta contábil	Alessandra Cristina Navatta		
REGRAS DE NEGÓCIO


CÓD	DESCRIÇÃO	MFS		RN01	A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2106 - Associação da Tabela Dinâmica com o Plano Empresa.
	MFS-14166		RN02	A rotina deve contemplar os campos listados abaixo:

Campo Obrig.
Descrição Funcional
Origem

*
Código
ECF

*
Descrição


*
Data Inicial
 ECF

*
Versão
ECF

*
Registros
ECF

*
Cód. da Linha 
ECF

*
Código da Conta Contábil
ECF


Data Inicial da Vigência da Conta Contábil
Sistema


Data Final da Vigência da Conta Contábil
Sistema


Percentual da Receita Bruta (por Conta Contábil)
Sistema


Código de Centro de Custo
ECF


Percentual da Receita Bruta (por Centro de Custo)
Sistema


Os campos identificados com a origem “ECF” devem ser definidos na(s) tabela(s) criada(s) com o tipo compatível com o informado no layout da obrigação e tamanho igual ou superior ao solicitado no layout do ECF.

Os campos identificados com a origem “Sistema” devem ser definidos na(s) tabela(s) criada(s) com tamanho e tipo compatíveis com os sistemas fiscais Tax & Accounting (Mastersaf DW, Mastersaf GF e Mastersaf Smart).	MFS-14166		RN03	Campos identificadores do registro na mensagem de erro:

Código
Data Inicial
Versão 
Registro
Cód. da Linha
Código da Conta Contábil	MFS-14166		RN04	Regras Gerais:

Aplicar a regra de negócio geral <<RNG00010 - Campo Obrigatório>>
Aplicar a regra de negócio geral << RNG00027 - Validação de campos numéricos/numéricos sinalizado>>
Aplicar a regra de negócio geral <<RNG00026 - Validação de conteúdo de data>>
Aplicar a regra de negócio geral <<RNG00028 - Identificação de registros com erro>>
Aplicar a regra de negócio geral <<RNG00021 - Validação de valores dos campos de lista>>
Aplicar a regra de negócio geral << RNG00029 - Duplicidade Chave de Registro>>
	MFS-14166		RN05	Campo Cód. do Registro 


Tabela de cadastro correspondente: Tabela Dinâmica
Campos de busca: Registro, Cód. do Registro, Versão

Tratamentos: 

- Se o item da tabela dinâmica não estiver cadastrado, exibir a mensagem DW00095 

- Se Campo Tipo for igual a “R” ou “CNA”; exibir a mensagem: DW00096 

- Aplicar << RNG00001 - Associação Tabela Dinâmica x Plano Empresa>> se a regra não for respeitada, exibir a mensagem DW00099..

	MFS-14166		RN06	Campo Código Conta Contábil

Tabela de cadastro correspondente: Plano de Contas 
Campos de busca: Código Conta Contábil

Tratamentos:
- Aplicar as regras de negócio geral<<RNG00022 – Recuperar Conta Contábil>>

- Se o Código da Conta Contábil não estiver cadastrado na tabela de Plano de Contas, exibir a mensagem DW00088.

- Se a conta informada não estiver cadastrada com campo ‘Tipo Conta’ = ‘A’ – Analítica, exibir a mensagem DW00086.

- Se o Registro for igual à (M300A, M300B, M300C, M350A, M350B ou M350C) e natureza da conta contábil for diferente de (1, 2, 3, 4, 7 ou 8): DW00069. 


	MFS-14166		RN07	Campo Registros


Tabela de cadastro correspondente: Tabela Dinâmica
Campos de busca: Registro, Versão

- Se o registro da tabela dinâmica não estiver cadastrado, exibir a mensagem DW00102 

Se houver o valor a ser importado, corresponde registros dos Blocos X e Y (X291, X292, X390, X400, X450, X460, X470, X480, X490, X500, X510 ou Y681), exibir a msg: DW00104. 	MFS-14166		RN08	Campo Código de Centro de Custo

Tabela de cadastro correspondente: Centro de Custo
Campos de busca: Código Centro de Custo

- Aplicar as regras de negócio geral<<RNG00023 - Recuperar Centro de Custo>>

- Se o Código do Centro de Custo não estiver cadastrado na tabela de Centro de Custo, exibir a mensagem DW00088 
	MFS-14166		RN09	Campo Versão 

Tabela de cadastro correspondente: Versão da Tabela Dinâmica
Campos de busca: Versão
Tratamentos:

Aplicar a <<RNG00004 - Versão de Layout>>

Validação Valores:

- Se a versão não estiver cadastrada, exibir a mensagem DW00105 


Validação Data Inicial x Versão:
Aplicar a regra de negócio geral <<RNG00003 - Versão da Escrituração>>
Caso a condição não seja atendida, exibir DW00089 
	MFS-14166		RN10	Percentual da Receita Bruta (por Conta Contábil) ou Percentual da Receita Bruta (por Centro de Custo)

Se preenchido este campo, validar as opções abaixo:

Lista de valor:
1.6000
8.0000
12.0000
16.0000
32.0000
100.0000

Tratamentos:
Quando preenchido, aplicar a regra de negócio geral <<RNG00021 - Validação de valores dos campos de lista>> 

Validações:

Este campo só deve ser preenchido na linha 2 dos registros N500 ou N650, caso contrário, exibir a DW00098

Se não for informado o valor neste campo para a linha 2 dos registros N500 ou N650, gravar nulo.

Para registro iniciado com N500, verificar se o campo está com a informação: 
1.600
8.0000
16.0000
32.0000
100.0000

Se diferente do valor válido exibir DW00097

Para registro iniciado com N650 verificar se o campo está com a informação:
12.0000
32.0000
100.0000

Se diferente do valor válido exibir DW00097


Se o campo Centro de Custo for preenchido, o campo Percentual da Receita Bruta (por Conta Contábil) não pode estar preenchido, caso contrário exibir a mensagem DW00100.

Se o campo Centro de Custo não for preenchido, o campo Percentual da Receita Bruta (por Centro de Custo) não pode estar preenchido, caso contrário exibir a mensagem DW00101.
	MFS-14166		RN11	Campo Data Inicial da Vigência da Conta Contábil

A Data Inicial da Vigência da Conta Contábil deve ser maior ou igual ao campo Data Inicial da parametrização, caso contrário, exibir a mensagem DW00010.

Este campo é de preenchimento obrigatório se o campo Data Final da Vigência da Conta Contábil estiver preenchido. Caso o campo esteja nulo e o campo Data Final da Vigência da Conta Contábil preenchido, aplicar a <<RNG00010 - Campo Obrigatório>>.
	MFS-14166		RN12	Campo Data Final da Vigência da Conta Contábil

A Data Final da Vigência da Conta Contábil deve ser maior ou igual ao campo Data Inicial da Vigência da Conta Contábil, caso contrário, exibir a mensagem DW00010.
	MFS-14166		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN