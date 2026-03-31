# MTZ-Job-Servidor-Importacao_SAFX126

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX126.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4726

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, dos novos campos incluídos na SAFX126\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX126 \- Vendas com Cartão de Crédito/Débito, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Empresa

A

003

SIM

SIM

Estabelecimento

A

006

SIM

SIM

Data Movimento

N

008

SIM

SIM

Indicador Pessoa Física/Jurídica da Administradora

A

001

SIM

SIM

Código da Pessoa Física/Jurídica da Administradora

A

014

SIM

SIM

Total das Operações com Cartão de Crédito

N

015V002

NÃO

NÃO

Total das Operações com Cartão de Débito

N

015V002

NÃO

NÃO

Operação/ Prestação com Incidência de ICMS \- Valor do Faturamento

N

015V002

NÃO

NÃO

Operação/ Prestação com Incidência de ICMS \- Valor de Estorno

N

015V002

NÃO

NÃO

Serviço com incidência de ISS \- Valor do Faturamento

N

015V002

NÃO

NÃO

Serviço com incidência de ISS \- Valor de Estorno

N

015V002

NÃO

NÃO

 

OS4726

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4726

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4726

RN04

__Campo Data Movimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4726

RN05

__Campo Indicador Pessoa Física/Jurídica da Administradora__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4726

RN06

__Campo Código da Pessoa Física/Jurídica da Administradora__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4726

RN07

__Campo Total das Operações com Cartão de Crédito__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4726

RN08

__Campo Total das Operações com Cartão de Débito__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4726

RN09

__Campo Operação/ Prestação com Incidência de ICMS \- Valor do Faturamento__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4726

RN10

__Campo Operação/ Prestação com Incidência de ICMS \- Valor de Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4726

RN11

__Campo Serviço com incidência de ISS \- Valor do Faturamento__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4726

RN12

__Campo Serviço com incidência de ISS \- Valor de Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4726

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

