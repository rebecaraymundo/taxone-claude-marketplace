# Associacao_do_Plano_de_Contas_Referencial_com_o_Plano_Empresa-SAFX2107

> Fonte: Associacao_do_Plano_de_Contas_Referencial_com_o_Plano_Empresa-SAFX2107.doc

THOMSON REUTERS

 DOCPROPERTY  Title  \* MERGEFORMAT Regras de Importação Online e Batch SAFX2107
Associação do Plano de Contas Referencial com o Plano Empresa 
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		18/10/2017	MFS-14165	Criação do documento	Alessandra Cristina Navatta		02/10/2018	MFS-21397	Exclusão dos campos de data (inicial e final) de vigência da conta contábil	Alessandra Cristina Navatta		
REGRAS DE NEGÓCIO


CÓD	DESCRIÇÃO	MFS		RN01	
A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2107 - Associação do Plano de Contas Referencial com o Plano Empresa.
	MFS-14165		RN02	A rotina deve contemplar os campos listados abaixo:

Campo Obrig.
Descrição Funcional
Origem

*
Código 
Sistema

*
Descrição
Sistema

*
Data Inicial
Sistema

*
Versão 
Sistema

*
Registro
ECF

*
Código da Conta Referencial
ECF

*
Código da Conta Contábil
ECF


Data Inicial da Vigência da Conta Contábil
Sistema


Data Final da Vigência da Conta Contábil
Sistema


Código de Centro de Custo
ECF


Os campos identificados com a origem “ECF” devem ser definidos na(s) tabela(s) criada(s) com o tipo compatível com o informado no layout da obrigação e tamanho igual ou superior ao solicitado no layout da ECF.

Os campos identificados com a origem “Sistema” devem ser definidos na(s) tabela(s) criada(s) com tamanho e tipo compatíveis com os sistemas fiscais Tax & Accounting (Mastersaf DW, Mastersaf GF e Mastersaf Smart).	MFS-14165		RN03	Campos identificadores do registro na mensagem de erro:

Código
Data inicial
Versão 
Registro
Código da Conta Referencial
Código da Conta Contábil		RN04	Regras Gerais:

Aplicar a regra de negócio geral <<RNG00010 - Campo Obrigatório>>
Aplicar a regra de negócio geral << RNG00027 - Validação de campos numéricos/numéricos sinalizado>>
 Aplicar a regra de negócio geral << RNG00026 - Validação de conteúdo de data>>
Aplicar a regra de negócio geral << RNG00028 - Identificação de registros com erro >>
Aplicar a regra de negócio geral << RNG00029 - Duplicidade Chave de Registro>>
	MFS-14165		RN05	Campo Versão 

Tabela de cadastro correspondente: Versão da Tabela Referencial
Campos de busca: Versão

Tratamentos:

Aplicar a <<RNG00004 - Versão de Layout>>

Validação Valores:
- Se a versão não estiver cadastrada, exibir a mensagem DW00107 

Validação Data Inicial x Versão:
Aplicar a regra de negócio geral <<RNG00003 - Versão da Escrituração>>
Caso a condição não seja atendida, exibir DW00089 
	MFS-14165		RN06	Campo Código Conta Referencial

Tabela de cadastro correspondente: Plano de Contas Referencial
Campos de busca: Código Conta Referencial

Tratamentos 
- Se a conta informada não estiver cadastrada com campo ‘Tipo Conta’ = ‘A’ – Analítica, exibir a mensagem DW00108 

- Exibir a mensagem DW00090, se o Código da Conta Referencial não estiver cadastrado na tabela de Plano de Contas Referencial levando em consideração a versão informada no cabeçalho do arquivo importado. 

 - Aplicar a <<RNG00024 - Recuperar Conta Referencial>>

- Se a conta informada possuir natureza diferente de 01, 02, 03 ou 04, exibir a mensagem DW00109.
	MFS-14165		RN07	Campo Código Conta Contábil

Tabela de cadastro correspondente: Plano de Contas 
Campos de busca: Código Conta Contábil

Tratamentos:
- Aplicar as regras de negócio geral<<RNG00022 – Recuperar Conta Contábil>>

- Se o Código da Conta Contábil não estiver cadastrado na tabela de Plano de Contas, exibir a mensagem DW00088.

- Se a conta informada não estiver cadastrada com campo ‘Tipo Conta’ = ‘A’ – Analítica, exibir a mensagem DW00086. 

- Se a conta informada possuir natureza diferente de 1, 2, 3, 4, 7 ou 8, exibir a mensagem DW00110.

	MFS-14165		RN08	
Campo Registro


Tabela de cadastro correspondente: Tabela Referencial
Campos de busca: Registro, Versão

- Se o registro da tabela referencial não estiver cadastrado, exibir a mensagem DW00106. 

	MFS-14165		RN09	Campo Código de Centro de Custo

Tabela de cadastro correspondente: Centro de Custo
Campos de busca: Código Centro de Custo

- Aplicar as regras de negócio geral<<RNG00023 - Recuperar Centro de Custo>>

- Se o Código do Centro de Custo não estiver cadastrado na tabela de Centro de Custo, exibir a mensagem DW00088.	MFS-14165		RN10	Campo Conta Contábil X Registros X Campo Código Conta Referencial

Para todos os registros, o campo "Natureza" da tabela plano de contas referencial deve ser compatível com o campo "indicador da Natureza" do plano de contas da empresa, de acordo com a tabela abaixo:
- Se o Registro possuir Códigos de Natureza iguais a “01”, “02” ou “03” na tabela de plano referencial, permitir contas contábeis  que possuem códigos de natureza (da tabela de plano de contas) igual a “1”, “2” ou “7”.
- Se o Registro possuir Código de Natureza igual a “04”, na tabela de plano referencial, permitir contas contábeis que possuem códigos de natureza (da tabela de plano de contas) igual a “3”, “4” ou “8”.
Se for diferente da tabela acima, exibir a mensagem DW00087.	MFS-14165		RN11	Campo Data Inicial da Vigência da Conta Contábil

A Data Inicial da Vigência da Conta Contábil deve ser maior ou igual ao campo Data Inicial da parametrização, caso contrário, exibir a mensagem DW00010.

Este campo é de preenchimento obrigatório se o campo Data Final da Vigência da Conta Contábil estiver preenchido. Caso o campo esteja nulo e o campo Data Final da Vigência da Conta Contábil preenchido, aplicar a <<RNG00010 - Campo Obrigatório>>.
	MFS-14165		RN12	Campo Data Final da Vigência da Conta Contábil

A Data Final da Vigência da Conta Contábil deve ser maior ou igual ao campo Data Inicial da Vigência da Conta Contábil, caso contrário, exibir a mensagem DW00010.
	MFS-14165		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN