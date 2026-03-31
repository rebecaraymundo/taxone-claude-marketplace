# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX222

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX222.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 67 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4710

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX222\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX222 \- Tabela de Profissionais Habilitados, que deve ser criada com a seguinte estrutura:

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

Período

N

006

SIM

SIM

CPF do Profissional

A

011

SIM

SIM

Indicador de habilitação

A

001

NÃO

NÃO

Indicador de escolaridade

A

001

NÃO

NÃO

Indicador da participação societária

A

001

NÃO

NÃO

Nome do Profissional

A

060

NÃO

NÃO

 

OS4710

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4710

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4710

RN04

__Campo Período__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4710

RN05

__CPF do Profissional__

Como o campo é obrigatório de preenchimento, <a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido:

- Se o campo não for preenchido ou for preenchido com menos de 11 posições, emitir a mensagem: “O Campo CPF é de preenchimento Obrigatório”\.

Mesmo o campo sendo alfanumérico só permitirá o preenchimento numérico, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido totalmente como numérico:

- Verificar se o campo é numérico e se for preenchido com alfanumérico, emitir a mensagem: “Valor Decimal ou Numerico com formato invalido”\.

OS4710

RN06

__Indicador de habilitação __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Só serão permitidos os seguintes indicadores de habilitação:

- 0 \- Profissional habilitado
- 1 \- Profissional não habilitado

OS4710

RN07

__Indicador de escolaridade __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Só serão permitidos os seguintes indicadores de escolaridade:

- 0 \- Nível superior
- 1 \- Nível médio

OS4710

RN08

__Indicador da participação societária __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Só serão permitidos os seguintes indicadores de participação societária:

- 0 \- Sócio
- 1 \- Não sócio

OS4710

RN09

__Nome do Profissional__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4710

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

