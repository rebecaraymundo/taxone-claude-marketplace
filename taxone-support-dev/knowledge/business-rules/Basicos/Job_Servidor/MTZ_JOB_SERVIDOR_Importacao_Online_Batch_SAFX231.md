# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX231

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX231.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-2631

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX231\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX231 \- Transferência de Saldos de Plano de Contas Anterior por Centro de Custo em Moeda Funcional, que deve ser criada com a seguinte estrutura:

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

Conta Contábil

A

070

SIM

SIM

Centro de Custo

A

020

SIM

SIM

Data da Operação

N

008

SIM

SIM

Conta Contábil do Lançamento do Plano de Contas Anterior

A

070

SIM

SIM

Centro de Custo do Plano de Contas Anterior

A

020

NÃO

SIM

Saldo Inicial

N

015V002

NÃO

NÃO

Débito/Crédito

A

001

SIM

NÃO

 

MFS\-2631

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-2631

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-2631

RN04

__Identificação do Saldo Contábil correspondente__

Verificar através dos campos Código da Empresa, Código do Estabelecimento, Conta Débito/Crédito do Lançamento, Centro de Custo e Data da Operação se existe registro correspondente na tabela SAFX227 – Saldo Contábil por Centro de Custo em Moeda Funcional\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “92562” da TFIX22: “Saldo Mensal nao encontrado”\.

MFS\-2631

RN05

__Campo Conta Contábil do Lançamento do Plano de Contas Anterior__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem “92567” da TFIX22: “Conta Debito/Credito do Lancamento do Plano de Contas Anterior nao informado”\.

Verificar a existência do código da Conta Débito/Crédito do Lançamento do Plano de Contas Anterior na tabela SAFX2002\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “91860” da TFIX22: “Plano de Contas nao encontrado”\.

MFS\-2631

RN06

__Campo Centro de Custo do Plano de Contas Anterior__

Verificar a existência do código do Centro de Custo do Plano de Contas Anterior na tabela SAFX2003\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “92566” da TFIX22: “Nao existe cadastro para o Centro de Custo do Lancamento do Plano de Contas Anterior informado”\.

MFS\-2631

RN07

__Campo Débito/Crédito__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido ou esteja com conteúdo diferente de “D” ou “C”\. Utilizar a mensagem “90100” da TFIX22: “O Campo Debito/Credito deve ser preenchido com <D> ou <C>”\.

MFS\-2631

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

