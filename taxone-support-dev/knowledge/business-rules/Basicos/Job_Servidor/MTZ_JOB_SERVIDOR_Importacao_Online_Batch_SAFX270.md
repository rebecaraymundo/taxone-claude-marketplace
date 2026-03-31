# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX270

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX270.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX270

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-21021

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX270 para atender o Registro B460 da EFD\-ICMS/IPI/ISS\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX270 – Deduções ISS, que deve ser criada com a seguinte estrutura:

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

Tipo de Dedução

A

001

SIM

SIM

Indicador da Obrigação

A

001

SIM

SIM

Valor da dedução

N

015V002

SIM

NÃO

Número do processo

A

024

NÃO

NÃO

Origem do processo

A

001

NÃO

NÃO

Descrição do processo

A

050

NÃO

NÃO

Código da observação

A

008

SIM

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

__Campo Período de Referência__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-21021

RN05

__Campo Tipo de Dedução__

Como o campo é obrigatório de preenchimento e deve ser um conteúdo válido\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Tipo de Dedução não preenchido ou inválido”*\.

__Conteúdo válido:__

0 \- Compensação do ISS calculado a maior

1 \- Benefício fiscal por incentivo à cultura

2 \- Decisão administrativa ou judicial

9 \- Outros

MFS\-21021

RN06

__Campo Indicador da Obrigação __

Como o campo é obrigatório de preenchimento e deve ser um conteúdo válido\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Indicador da Obrigação não preenchido ou inválido”*\.

__Conteúdo válido:__

0 \- ISS Próprio

1 \- ISS Substituto \(devido pelas aquisições de serviços do declarante\)

2 \- ISS Uniprofissionais

MFS\-21021

RN07

__Campo Valor da dedução__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:* “Valor da dedução não preenchido”*\.

MFS\-21021

RN08

__Campo Número do processo__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-21021

RN09

__Campo Origem do processo__

Campo de preenchimento não obrigatório, mas deve ser um conteúdo válido caso preenchido\. Caso esse campo esteja preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Origem do processo inválido”*\.

__Conteúdo válido:__

0 \- Sefin

1 \- Justiça Federal

2 \- Justiça Estadual

9 \- Outros

MFS\-21021

RN10

__Campo Descrição do processo__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-21021

RN11

__Campo Código da observação__

Como o campo é obrigatório de preenchimento, deve ser um conteúdo válido cadastrado na SAFX2009\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Código da observação não preenchido ou inválido”*\.

MFS\-21021

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

