# MTZ-Job-Servidor-Importacao_SAFX169

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX169.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 65 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4711

Elenilson Coutinho

Definição das regras de importação, Online e Batch, da SAFX169\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX169 – Saldo Antes do Encerramento, que deve ser criada com a seguinte estrutura:

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

Código da Conta Analítica de Resultado

A

070

SIM

SIM

Código do Centro de Custo

A

020

NÃO

SIM

Data Saldo

N

008

SIM

SIM

Indicador da situação do saldo final: 

D \- Devedor; 

C \- Credor\.

A

001

SIM

NÂO

Valor do saldo final antes do lançamento de encerramento

N

015V002

SIM

NÃO

 

OS4711

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4711

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4711

RN05

__Campo Código da Conta Analítica de Resultado__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código da Conta Analítica de Resultado não informado”\.

Verificar a existência do Código da Conta Analítica de Resultado na tabela SAFX2002\. Caso não exista, retornar mensagem de erro: “Não existe cadastro para o Código da Conta Analítica de Resultado informada”\.

OS4711

RN06

__Campo Código do Centro de Custo__

Caso informado, verificar a existência do código do Centro de Custo na tabela SAFX2003\. Caso não exista, retornar mensagem de erro: “Não existe cadastro para o Centro de Custo informado”\.

OS4711

RN04

__Campo Data Saldo__

Como o campo é obrigatório de preenchimento, deve ser exibida a mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4711

RN08

__Campo Indicador da Situação do Saldo Final__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Indicador da Situação do Saldo Final não informado”\.

O conteúdo do campo Débito/Crédito do Lançamento Contábil deve ser igual a “D” ou “C”\. Caso seja informado conteúdo diferente, retonar mensagem de erro: “Indicador da Situação do Saldo Final inválido\. Informe <D> ou <C>”\.

OS4711

RN07

__Campo Valor do Saldo Final Antes do Lançamento de Encerramento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Valor do Saldo Final Antes do Lançamento de Encerramento não informado”\.

OS4711

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

