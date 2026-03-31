# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX253

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX253.docx
- **Modificado:** 2024-04-13
- **Tamanho:** 64 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX253

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-15195

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX253\.

MFS591919 

Graciela Soares 

Criação de Novos Campos – Tabela SAFX253 para atendimento à NFCom \.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX253 \- Term\. Telefônicos dos Planos de Prestações de Serviços Telefônicos Corporativos, Familiares ou Similares, que deve ser criada com a seguinte estrutura:

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

Data de Emissão/Escr\. Fiscal

N

008

SIM

SIM

Indicador Pessoa Física/Jurídica

A

001

SIM

SIM

Código/Destinatário/Emitente/Remetente

A

014

SIM

SIM

Número do Documento Fiscal

A

012

SIM

SIM

Série

A

003

NÃO

SIM

Subsérie

A

002

NÃO

SIM

Número do Terminal Telefônico

A

015

SIM

SIM

Valor Total da Fatura

N

015V002

NÃO

NÃO

 

MFS\-15195

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15195

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15195

RN04

__Campo Data de Emissão/Escr\. Fiscal__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15195

RN05

__Campo Indicador Pessoa Física/Jurídica__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15195

RN06

__Campo Código/Destinatário/Emitente/Remetente __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15195

RN07

__Campo Número do Documento Fiscal__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15195

RN08

__Campo Série__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15195

RN09

__Campo Subsérie __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15195

RN10

__Campo Número do Terminal Telefônico __

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“O Campo Número do Terminal Telefônico deve ser preenchido”*\.__ __

MFS\-15195

RN11

__Campo Valor Total da Fatura__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15195

RN12

__Campo UF do Terminal Telefônico __

Obrigatoriedade: Não obrigatório

Descrição: UF de Destino

Nome do Campo: UF\_DESTINO

Tamanho: 002

Tipo: A

Validação do campo: Caso o campo esteja preenchido no arquivo, validar seu conteúdo na tabela ESTADO\. Se o código não existir na tabela Campo “COD\_ESTADO”, gravar a seguinte mensagem no log de importação e não gravar o registro:  “O Codigo da Unidade da Federacao de Destino é invalido\.”

Reserva TFIX22: 93631

  


MFS591919

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

