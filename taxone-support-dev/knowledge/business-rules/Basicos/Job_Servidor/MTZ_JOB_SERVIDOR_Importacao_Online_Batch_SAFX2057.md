# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2057

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2057.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4316

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX2057\.

OS4745

Marcos G\. de Paula

Inclusão do campo Data Final de Validade

MFS8291

Lara Aline

Definição das regras de carga, exportação, importação Online e Batch da SAF2057\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2057 – Cadastro de SCP, que deve ser criada com a seguinte estrutura:

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

Código da SCP

A

014

SIM

SIM

Data de Validade

N

008

NÃO

NÃO

Descrição da SCP

A

150

NÃO

NÃO

Informação Complementar

A

100

NÃO

NÃO

Data de Validade Final

N

008

NÃO

NÃO

Incide DIRF

A

001

NAO

NAO

 

OS4316

OS4745

MFS8291

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4316

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4316

RN04

__Campo Código da SCP__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse campo não esteja preenchido: “Campo Código da SCP e obrigatório e nao foi informado”

OS4316

RN05

__Campo Data de Validade Final__

A data informada neste campo deve ser maior ou igual a data informada no campo Data de Validade\. Caso seja menor, retornar mensagem de erro: “A data de validade Final deve ser maior que a data de validade inicial” \(mensagem 92180 da TFIX22\)\.

OS4745

RN06

Incide DIRF

Se o campo “Incide DIRF” estiver preenchido com ‘S’, o sistema deve verificar se o campo Código da SCP corresponde a um CNPJ válido, caso o formato seja inválido exibir a seguinte mensagem:

‘Código da SCP não corresponde a um CNPJ válido, favor verificar ou desmarcar o campo “Incide DIRF” para esse código de SCP\.’

MFS8291

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

