# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX242

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX242.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX242

Tabela Saldos das Contas Consolidadas

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-9667

Lara Aline

Definição das regras de carga, exportação, importação Online e Batch da SAF242\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX242 – Saldos das Contas Consolidadas, que deve ser criada com a seguinte estrutura:

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

Data do Saldo consolidado

N

008

SIM

SIM

Código da conta consolidada

A

070

SIM

SIM

Valor absoluto aglutinado

N

017

SIM

NAO

Indicador da situação do valor aglutinado

A

001

SIM

NAO

Valor absoluto das eliminações

N

017

SIM

NAO

Indicador da situação do valor eliminado

A

001

SIM

NAO

Valor absoluto consolidado

N

017

SIM

NAO

Indicador da situação do valor consolidado

A

001

SIM

NAO

 

MFS\-9667

RN02

__Código da Empresa__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Empresa não está preenchido”\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS\-9667

RN03

__Código do Estabelecimento__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Estabelecimento deve ser preenchido”\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS\-9667

RN04

__Data do Saldo consolidado __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data do Saldo consolidado é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data do Saldo consolidado com formato invalido”\. 

MFS\-9667

RN05

__Código da conta consolidada __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Código da conta consolidada é obrigatório \- deve ser preenchido”\. 

Crítica da existência do código da conta na SAFX2002:

Será verificada a existência do código da conta informado \(Código da Conta\) na Tabela do Plano de Contas – SAFX2002 e se é analítica \(campo 04 \- Indicador de Conta = ‘A’\), e caso não exista ou não seja analítica, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Código da conta consolidada nao esta cadastrado ou não é uma conta analítica”\. 

MFS\-9667

RN06

__Valor absoluto aglutinado __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Valor absoluto aglutinado é obrigatório \- deve ser preenchido”\. 

MFS\-9667

RN07

__Indicador da situação do valor aglutinado __

Opções válidas:

D – Devedor 

C – Credor 

Campo de preenchimento obrigatório, caso não preenchido exibir a seguinte mensagem: “O Campo Indicador da situação do valor aglutinado é obrigatório \- deve ser preenchido”\. Quando informado uma opção inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Indicador da situação do valor aglutinado com opção invalida”\.

MFS\-9667

RN08

__Valor absoluto das eliminações __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Valor absoluto das eliminações é obrigatório \- deve ser preenchido”\. 

MFS\-9667

RN09

__Indicador da situação do valor eliminado __

Opções válidas:

D – Devedor 

C – Credor 

Campo de preenchimento obrigatório, caso não preenchido exibir a seguinte mensagem: “O Campo Indicador da situação do valor eliminado é obrigatório \- deve ser preenchido”\. Quando informado uma opção inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Indicador da situação do valor eliminado com opção invalida”\.

MFS\-9667

RN10

__Valor absoluto consolidado __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Valor absoluto consolidado é obrigatório \- deve ser preenchido”\. 

MFS\-9667

RN11

__Indicador da situação do valor consolidado __

Opções válidas:

D – Devedor 

C – Credor 

Campo de preenchimento obrigatório, caso não preenchido exibir a seguinte mensagem: “O Campo Indicador da situação do valor consolidado é obrigatório \- deve ser preenchido”\. Quando informado uma opção inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Indicador da situação do valor consolidado com opção invalida”\.

MFS\-9667

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

