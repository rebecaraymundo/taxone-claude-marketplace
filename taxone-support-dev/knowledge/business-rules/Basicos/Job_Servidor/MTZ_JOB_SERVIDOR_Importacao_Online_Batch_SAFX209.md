# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX209

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX209.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX209

Tabela Reembolso do Plano Privado de Saúde do Dependente

__Localização__

__Módulo:__ Básicos🡪 MasterSAF DW

__Menu:__ 	Manutenção 🡪 Folha de Pagamento 🡪 Reembolso do Plano Privado de Saúde do Dependente

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-8835

Lara Aline

Definição das regras de importação, Online e Batch da SAF209\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga, importação, batch e exportação do módulo JOB Servidor devem ser ajustadas para que contemple as informações da tabela SAFX209 – Reembolso do Plano Privado de Saúde do Dependente, que deve ser criada com a seguinte estrutura:

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

Código do Dependente

N

002

SIM

SIM

CPF / CNPJ do Prestador de Serviço

A

014

SIM

SIM

Nome do Prestador de Serviço

A

150

SIM

NAO

Valor do Reembolso do Ano Competência

N 

015V002

NAO

NAO

Valor do Reembolso de Anos Anteriores ao Ano Competência

N

015V002

NAO

NAO

 

MFS\-8835

RN02

__Código da Empresa__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Empresa não está preenchido”\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS\-8835

RN03

__Código do Estabelecimento__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Estabelecimento deve ser preenchido”\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS\-8835

RN04

__Código do Funcionário__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Código do Funcionário deve ser preenchido”\.

Crítica da existência do funcionário na SAFX15:

Será verificada a existência do funcionário informado \(Código do Funcionário\) na Tabela de Cadastro de Funcionários \(SAFX15\), e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Codigo de Funcionario nao esta cadastrado”

MFS\-8835

RN05

__Ano Competência__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Ano de Competência é obrigatório \- deve ser preenchido”\.

MFS\-8835

RN06

__Mês Competência__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Mês de Competência e obrigatório \- deve ser preenchido”\.

MFS\-8835

RN07

__Código da Verba__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo código da Verba \- deve ser preenchido”\.

Crítica da existência do código da verba na SAFX2023:

Será verificada a existência do código da verba informado \(Código da Verba\) na Tabela de Verbas \(SAFX2023\), e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Codigo da Verba/Evento/Conta nao esta cadastrado”

MFS\-8835

RN08

__Data do Pagamento__

Campo de preenchimento não obrigatório, quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data de Validade com formato invalido”\.

MFS\-8835

RN09

__Código do Dependente__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Codigo do Dependente e obrigatorio \- deve ser preenchido”\.

Crítica da existência do dependente na SAFX55:

Será verificada a existência do dependente informado \(Código do Dependente\) na Tabela de Cadastro de Dependentes – SAFX55, e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Codigo de Dependente nao esta cadastrado”

MFS\-8835

RN10

__CPF / CNPJ do Prestador de Serviço __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo CPF / CNPJ do Prestador de Serviço é obrigatório \- deve ser preenchido”\.

Será verificada a formatação do CPF/CNPJ conformes regras da Receita Federal, caso o formato seja inválido exibir a seguinte mensagem: “Numero de CPF informado nao e valido, conforme regras da Receita Federal\.” ou “Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda\.”\.

MFS\-8835

RN11

__Nome do Prestador de Serviço __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Nome do Prestador de Serviço é obrigatório \- deve ser preenchido”\.

MFS\-8835

RN12

__Valor do Reembolso do Ano Competência__

Campo de preenchimento não obrigatório\.

MFS\-8835

RN13

__Valor do Reembolso de Anos Anteriores ao Ano Competência __

Campo de preenchimento não obrigatório\.

MFS\-8835

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

