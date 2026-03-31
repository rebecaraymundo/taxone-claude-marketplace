# MTZ_Processo_Armazena_linhas_Campo_Expressao_ord_SAFX2102

> Fonte: MTZ_Processo_Armazena_linhas_Campo_Expressao_ord_SAFX2102.doc

DOCPROPERTY "Company" \* MERGEFORMAT MasterSAF


Processo que armazena em linhas os campos Expressao_Ord da SAFX2102


DR	Nome	Descrição	Data Alteração		OS3420	Processo para armazenar em linhas os dados da Tabela SAFX2102.	Criação de um Processo para armazenar em linhas os dados da Tabela SAFX2102 (campos 10 A 14).  	14/02/2012		
Regras de Negócios
Cód.		DR		RN00	Devido à necessidade de armazenar mais posições no campo 10 - EXPRESSAO_ORD da SAFX2102 foram inclusos mais campos com a mesma formatação nesta tabela, pois não conseguimos usar em SAFX campos com o formato CLOB. Para melhor manutenção das rotinas envolvidas e pensando na facilitação de processos, estamos criando um processo, para armazenar em linhas as informações dos campos 10 a 14 da SAFX2102.
Este processo será transparente ao usuário. A tabela definitiva terá os campos mencionados nas regras RN01 a RN04
	OS3420		RN01	Campo 01 - Código da empresa
 
Item: 01
Nome do Campo: COD_EMPRESA
Descrição: Código da empresa
Tipo: A
Tamanho: 003
Comentário: Campo destinado ao código da Empresa.
Chave Primária
Obrigatório


	OS3420		RN02	Campo 02 - Código do estabelecimento
 
Item: 02
Nome do Campo: COD_ESTAB
Descrição: Código do estabelecimento.
Tipo: A
Tamanho: 006
Comentário: Campo destinado ao código do Estabelecimento.
Chave Primária
Obrigatório
	OS3420		RN03	Campo 03 - Código da Conta Aglutinadora
 
Item: 03
Nome do Campo: COD_CONTA_AGLUT
Descrição: Código da conta aglutinadora.
Tipo: A
Tamanho: 070
Comentário: Campo destinado ao código da conta Aglutinadora.
Chave Primária
Obrigatório
	OS3420		RN04	Campo 04 – Expressão de Ordem
 
Item: 04
Nome do Campo: EXPRESSAO_ORDL
Descrição: Código da conta aglutinadora.
Tipo: A
Tamanho: 4000
Comentário: Campo destinado a Expressão de Ordem Subtotalizador/Totalizador os Códigos de Contas de Aglutinação. Será gravado linha a linha referente aos campos 10 a 14 da SAFX2102.
Chave Primária
Obrigatório

Considerações: 
A ultima posição lida nos campos 10 à 14 devem terminar com o caracter ‘;’
Será considerada uma linha até o sistema encontrar o caracter ‘;’

	OS3420