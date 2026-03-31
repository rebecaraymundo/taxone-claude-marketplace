# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX227

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX227.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-2631

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX229\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX229 – Saldo Contábil Auxiliar em Moeda Funcional, que deve ser criada com a seguinte estrutura:

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

Código da Estabelecimento

A

006

SIM

SIM

Data da Operação

N

008

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

Saldo Inicial

N

015V002

 NÃO

NÃO

Débito/Crédito Saldo Inicial

A

001

SIM

NÃO

Saldo Final

N

015V002

 NÃO

NÃO

Débito/Crédito Saldo Final

A

001

SIM

NÃO

Total Crédito

N

015V002

NÃO

NÃO

Total Débito

N

015V002

NÃO

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

__Campo Data da Operação__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido\. Utilizar a mensagem “92638” da TFIX22: “Data de Saldo nao informada ou com formato invalido”\.

MFS\-2631

RN05

__Campo Conta Contábil__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido\. Utilizar a mensagem “90095” da TFIX22: “O Codigo da Conta Contabil deve ser preenchido”\.

Verificar a existência do código da Conta Débito/Crédito do Lançamento na tabela SAFX2002, com Data Início/Inclusão/Alteração menor ou igual a Data da Operação do Lançamento\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “91860” da TFIX22: “Plano de Contas nao encontrado”\.

MFS\-2631

RN06

__Campo Centro de Custo__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido\. Utilizar a mensagem “90435” da TFIX22: “Campo de Centro de Custo deve ser preenchido”\.

Verificar a existência do código do Centro de Custo na tabela SAFX2003 com Data Início/Inclusão/Alteração menor ou igual a Data da Operação do Lançamento\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “91861” da TFIX22: “Centro de Custo nao encontrado”\.

MFS\-2631

RN07

__Campo Débito/Crédito do Saldo Inicial__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido ou esteja com conteúdo diferente de “D” ou “C”\. Utilizar a mensagem “90100” da TFIX22: “O Campo Debito/Credito deve ser preenchido com <D> ou <C>”\.

MFS\-2631

RN08

__Campo Débito/Crédito do Saldo Final__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido ou esteja com conteúdo diferente de “D” ou “C”\. Utilizar a mensagem “90100” da TFIX22: “O Campo Debito/Credito deve ser preenchido com <D> ou <C>”\.

Deve ser validado o indicado aqui apresentado, considerando o valor demonstrado para o campo Saldo Final\. Considerar a seguinte regra, realizando o cálculo do Saldo Final:

Se Campo Débito/Crédito do Saldo Inicial for igual a “C”, o valor do Saldo Final deve ser igual a:

Saldo Inicial \+ Total Crédito – Total Débito\.

Se o resultado do cálculo for positivo, o campo Débito/Crédito do Saldo Final deve ser igual a “C”\. Se for negativo, deve ser igual a “D”\.

Se Campo Débito/Crédito do Saldo Inicial for igual a “D”, o valor do Saldo Final deve ser igual a:

Saldo Inicial \+ Total Débito – Total Crédito\.

Se o resultado do cálculo for positivo, o campo Débito/Crédito do Saldo Final deve ser igual a “D”\. Se for negativo, deve ser igual a “C”\.

Se o valor for diferente do esperado, retornar mensagem de erro\. Utilizar a mensagem: “90110	“ da TFIX22: “O Indicador de Debito/Credito do Saldo Final nao confere”\.

MFS\-2631

RN09

__Campo Saldo Final__

O valor informado na coluna de Saldo Final deve ser igual ao resultado do seguinte cálculo:

Se Campo Débito/Crédito do Saldo Inicial for igual a “C”, o valor do Saldo Final deve ser igual a:

Saldo Inicial \+ Total Crédito – Total Débito \(considerar sempre valor positivo\)\.

Se Campo Débito/Crédito do Saldo Inicial for igual a “D”, o valor do Saldo Final deve ser igual a:

Saldo Inicial \+ Total Débito – Total Crédito \(considerar sempre valor positivo\)\.

Se o valor for diferente do esperado, retornar mensagem de erro\. Utilizar a mensagem: “90109	“ da TFIX22: “O Valor do Saldo Final nao confere com valores informados”\.

MFS\-2631

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

