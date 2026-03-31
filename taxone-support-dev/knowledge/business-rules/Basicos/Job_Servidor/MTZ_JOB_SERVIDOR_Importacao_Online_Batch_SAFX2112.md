# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2112

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2112.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 70 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS13361

Lara Aline

Definição das regras de importação, Online e Batch, da SAFX2112\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2112 \- Código de Atividade X Serviços \(CPRB\), que deve ser criada com a seguinte estrutura:

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

Código de Serviço

A

004

SIM

SIM

Código de Atividade

A

008

SIM

SIM

Código da Receita

A

006

SIM

SIM

 

MFS13361

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS13361

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS13361

RN04

__Campo Código de Serviço__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código de Serviço não informado”\.

MFS13361

RN05

__Campo Código de Atividade__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código de Atividade não informado”\.

MFS13361

RN06

__Campo Código da Receita__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código da Receita não informado”\.

MFS13361

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

