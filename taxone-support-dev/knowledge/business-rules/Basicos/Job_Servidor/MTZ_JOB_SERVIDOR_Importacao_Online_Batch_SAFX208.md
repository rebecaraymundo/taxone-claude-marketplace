# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX208

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX208.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Reembolso do Plano Privado de Saúde do Funcionário

__Localização Tela__

__Módulo:__ Básicos🡪 MasterSAF DW

__Menu: __	Manutenção 🡪 Folha de Pagamento 🡪 Reembolso do Plano Privado de Saúde do Funcionário

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

Definição das regras importação online e batch da SAFX208\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação online e batch do módulo JOB Servidor devem ser ajustadas para que contemple as informações da tabela SAFX208 – Reembolso do Plano Privado de Saúde do Funcionário, que deve ser criada com a seguinte estrutura:

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

CPF/CNPJ do Prestador de Serviço

A

014

SIM

SIM

Nome do Prestador de Serviço

A

150

SIM

NAO

Valor Reembolso do Ano Competência

N

015V002

NÃO

NAO

Valor do Reembolso de Anos Anteriores ao Ano de Competência

N

015V002

NAO

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

RN09

__Código da Verba__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo código da Verba \- deve ser preenchido”\. 

Crítica: Caso código não existente na SAFX2023 exibir a seguinte mensagem: “O Código da Verba nao esta cadastrado”\.

MFS\-8835

RN04

__Data de Pagamento__

Crítica: Caso não for uma data válida exibir a seguinte mensagem: Campo Data de Pagamento com formato inválido\.

Caso não preenchido, deverá ser informado o último dia do mês e ano de competência informado\.

MFS\-8835

RN10

__CPF/CNPJ do Prestador de Serviço__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo CPF / CNPJ do Prestador de Serviço é obrigatório \- deve ser preenchido”\.

Será verificada a formatação do CPF/CNPJ conformes regras da Receita Federal, caso o formato seja inválido exibir a seguinte mensagem: “Numero de CPF informado nao e valido, conforme regras da Receita Federal\.” ou “Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda\.”\.

MFS\-8835

RN11

__Nome do Prestador de Serviço__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Nome do Prestador de Serviço é obrigatório \- deve ser preenchido”\.

MFS\-8835

RN12

__Valor do Reembolso do Ano Competência__

MFS\-8835

RN13

__Valor do Reembolso de Anos Anteriores ao Ano Competência__ 

MFS\-8835

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

