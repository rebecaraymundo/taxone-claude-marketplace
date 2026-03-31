# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX232

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX232.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX232

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-2631

Marcos de Paula

Definição das regras de importação, Online e Batch, da SAFX232\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX232 – Saldo Antes do Encerramento em Moeda Funcional, que deve ser criada com a seguinte estrutura:

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

Conta Analítica de Resultado

A

070

SIM

SIM

Centro de Custo

A

020

NÃO

SIM

Data Saldo

N

008

SIM

SIM

Débito/Crédito

A

001

SIM

NÂO

Saldo Final

N

015V002

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

__Campo Código da Conta Analítica de Resultado__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem “92630” da TFIX22: “Codigo da Conta Analitica de Resultado nao informado”\.

Verificar a existência do Código da Conta Analítica de Resultado na tabela SAFX2002, com Data Início/Inclusão/Alteração menor ou igual a Data da Operação do Lançamento\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “92631” da TFIX22: “Nao existe cadastro para o Codigo da Conta Analitica de Resultado informada”\.

MFS\-2631

RN05

__Campo Código do Centro de Custo__

Verificar a existência do código do Centro de Custo na tabela SAFX2003 com Data Início/Inclusão/Alteração menor ou igual a Data da Operação do Lançamento\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “91861” da TFIX22: “Centro de Custo nao encontrado”\.

MFS\-2631

RN06

__Campo Data Saldo__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido\. Utilizar a mensagem “92638” da TFIX22: “Data de Saldo nao informada ou com formato invalido”\.

MFS\-2631

RN07

__Campo Débito/Crédito__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido ou esteja com conteúdo diferente de “D” ou “C”\. Utilizar a mensagem “92640” da TFIX22: “Indicador da Situacao do Saldo Final invalido\. Informe <D> ou <C>”\.

MFS\-2631

RN08

__Campo Valor do Saldo Final Antes do Lançamento de Encerramento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem “92641” da TFIX22: “Valor do Saldo Final Antes do Lancamento de Encerramento nao informado”\.

MFS\-2631

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

