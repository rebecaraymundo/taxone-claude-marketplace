# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX269

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX269.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX269

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-21021

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX269 para atender o Registro B350 da EFD\-ICMS/IPI/ISS\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX269 – Serviços Prestados por Instituições Financeiras, que deve ser criada com a seguinte estrutura:

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

Período da Apuração

N

006

SIM

SIM

Conta Contábil

A

070

SIM

SIM

Código COSIF

A

030

SIM

SIM

Código de Serviço da Lei 116

N

004

SIM

SIM

Alíquota do ISS

N

003V004

SIM

SIM

Quantidade de ocorrências na conta

N

005

SIM

NÃO

Valor contábil

N

015V002

SIM

NÃO

Valor da base de cálculo do ISS

N

015V002

SIM

NÃO

Valor do ISS

N

015V002

SIM

NÃO

Código da observação

A

008

NÃO

NÃO

 

MFS\-21021

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-21021

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-21021

RN04

__Campo Período da Apuração__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-21021

RN05

__Campo Conta Contábil __

Como o campo é obrigatório de preenchimento e deve ser um conteúdo válido cadastrado na SAFX2002\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Conta Contábil não preenchida ou inválida”*\.

MFS\-21021

RN06

__Campo Código COSIF__

Como o campo é obrigatório de preenchimento e deve ser um conteúdo válido cadastrado na TFIX64\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Código COSIF não preenchido ou inválido”*\.

__Tratamento:__

- Validar apenas contas referenciais iniciadas com “7” \(campo COD\_CONTA\_REF\), de entidade igual a “20” \(campo COND\_ENTIDADE\_RESP\) e versão igual a “3\.00” \(campo VERSAO\)\.

MFS\-21021

RN07

__Campo Código de Serviço da Lei 116__

Como o campo é obrigatório de preenchimento e deve ser um conteúdo válido cadastrado na TFIX60\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Código de Serviço da Lei 116 não preenchido ou inválido”*\.

MFS\-21021

RN08

__Campo Alíquota do ISS__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“Alíquota do ISS não preenchida”*\. 

MFS\-21021

RN09

__Campo Quantidade de ocorrências na conta__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“Quantidade de ocorrências na conta não preenchida”*\. 

MFS\-21021

RN10

__Campo Valor contábil__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“Valor contábil não preenchido”*\. 

MFS\-21021

RN11

__Campo Valor da base de cálculo do ISS__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“Valor da base de cálculo do ISS não preenchido”*\. 

MFS\-21021

RN12

__Campo Valor do ISS__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“Valor do ISS não preenchido”*\. 

MFS\-21021

RN13

__Campo Código da observação__

Campo de preenchimento não obrigatório e deve ser um conteúdo válido cadastrado na SAFX2009, aceitar conteúdo informado inclusive nulo\. Caso esse campo esteja preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Código da observação inválido”*\.

MFS\-21021

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

