# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX207

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX207.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Ficha Financeira Segregada por Plano de Previdência

__Localização__

__Módulo:__ Básicos🡪 MasterSAF DW

__Menu:__ 	Manutenção 🡪 Folha de Pagamento 🡪 Ficha Financeira Segregada por Previdência Complementar

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-8835

Elenilson Coutinho

Definição das regras de importação, Online e Batch, da SAF207\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação online e batch do módulo JOB Servidor devem ser ajustadas para que contemple as informações da tabela SAFX207 – Informações de Previdência Complementar, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Código Funcionário

A

014

SIM

SIM

Ano de Competência

N

004

SIM

SIM

Mês de Competência

N

002

SIM

SIM

Tipo de Folha

A

002

SIM

SIM

Código da Verba

A

006

SIM

SIM

Data do Pagamento

N

008

NÃO

SIM

CNPJ da Entidade de Previdência

A

014

NAO

SIM

Nome da Entidade de Previdência

A

150

NAO

NAO

Tipo de Previdência Complementar

A

001

SIM

SIM

Valor da Verba

N

015V002

SIM

NAO

 

MFS\-8835

RN02

__Código da Empresa__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Empresa não está preenchido”\.

MFS\-8835

RN03

__Código do Estabelecimento__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Estabelecimento deve ser preenchido”\.

MFS\-8835

RN04

__Data de Pagamento__

Crítica: Caso não for uma data válida exibir a seguinte mensagem: Campo Data de Pagamento com formato inválido\.

Caso não preenchido, deverá ser informado o último dia do mês e ano de competência informado\.

MFS\-8835

RN05

__Código do Funcionário__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Código do Funcionário deve ser preenchido”\.

Crítica: Caso código não existente na SAFX15 exibir a seguinte mensagem: “O Código de Funcionario nao esta cadastrado”\.

MFS\-8835

RN06

__Ano Competência__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Ano de Competência é obrigatório \- deve ser preenchido”\.

Crítica: Caso não for uma data válida exibir a seguinte mensagem: Campo Ano Competência com formato inválido\.

MFS\-8835

RN07

__Mês Competência__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Mês de Competência e obrigatório \- deve ser preenchido”\.

Crítica: Caso não for uma data válida exibir a seguinte mensagem: Campo Mês Competência com formato inválido\.

MFS\-8835

RN08

__Campo Tipo de Folha__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Tipo de Folha \- deve ser preenchido”\.

Crítica: Valor esperado 01, 02, 03, 04, 05, 06, 07, 08 e 09, caso contrário exibir a seguinte mensagem: “Tipos de Folha de Pagamento devem ser <01> ou <02> ou <03> ou <04> ou <05> ou <06> ou <07> ou <08> ou <09>”\.

MFS\-8835

RN09

__Código da Verba__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo código da Verba \- deve ser preenchido”\. 

Crítica: Caso código não existente na SAFX2023 exibir a seguinte mensagem: “O Código da Verba nao esta cadastrado”\.

MFS\-8835

RN10

__CNPJ da Entidade de Previdência__

Validação do CNPJ: Caso não seja um CNPJ válido exibir a seguinte mensagem: “Número de CNPJ informado não é válido, conforme regras da Secretaria de Fazenda”\.

MFS\-8835

RN11

__Nome da Entidade de Previdência__

MFS\-8835

RN12

__Tipo de Previdência Complementar__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Tipo de Previdência Complementar não preenchido”\.

Crítica: Valor esperado 01, 02, 03, 04, caso contrário exibir a seguinte mensagem: “Tipos de Previdência Complementar devem ser <01> ou <02> ou <03> ou <04>”\.

MFS\-8835

RN13

__Valor da Verba__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Valor da Verba não preenchido”

MFS\-8835

RN14

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX21, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando como chave de relacionamento os campos Código da Empresa, Código do Estabelecimento, Código do Funcionário, Ano de Competência, Mês de Competência, Tipo de Folha, Código da Verba, Data do Pagamento\. Caso não encontre, retornar a mensagem: “SAFX21 correspondente a SAFX207 não localizada”\.

MFS\-8835

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

