# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX264

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX264.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

264

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-19941

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX264 para atender o Registro 1050 da EFD\-Contribuições\.

MFS\-20225

Julyana Perrucini

Essa MFS tem como objetivo alterar o campo “Indicador Natureza” para seleção do conteúdo\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX264 \- Detalhamento de Ajustes de BC \- Valores Extra Escrituração, que deve ser criada com a seguinte estrutura:

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

Mês/ Ano Apuração

N

006

SIM

SIM

Data Referência

N

008

SIM

SIM

Indicador Natureza

A

002

SIM

SIM

Apropriação Ajuste

A

002

SIM

SIM

CNPJ

A

014

SIM

NÃO

Valor Total Ajuste

N

015V002

NÃO

NÃO

Valor Ajuste CST01

N

015V002

NÃO

NÃO

Valor Ajuste CST02

N

015V002

NÃO

NÃO

Valor Ajuste CST03

N

015V002

NÃO

NÃO

Valor Ajuste CST04

N

015V002

NÃO

NÃO

Valor Ajuste CST05

N

015V002

NÃO

NÃO

Valor Ajuste CST06

N

015V002

NÃO

NÃO

Valor Ajuste CST07

N

015V002

NÃO

NÃO

Valor Ajuste CST08

N

015V002

NÃO

NÃO

Valor Ajuste CST09

N

015V002

NÃO

NÃO

Valor Ajuste CST49

N

015V002

NÃO

NÃO

Valor Ajuste CST99

N

015V002

NÃO

NÃO

Nº Recibo

A

80

NÃO

NÃO

Informação Complementar

A

100

NÃO

NÃO

 

MFS\-19941

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-19941

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-19941

RN04

__Campo Mês/ Ano Apuração__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-19941

RN05

__Campo Data Referência__

Esse campo só é obrigatório porque é chave na tabela, mas nesse caso aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN06

__Campo Indicador Natureza__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou preenchido de forma incorreta\.

__\[ALTERADA – MFS\-20225\]__

__Conteúdo válido:__

01 – Vendas canceladas de receitas tributadas em períodos anteriores;

02 – Devoluções de vendas tributadas em períodos anteriores;

21 – ICMS a recolher sobre Operações próprias;

41 – Outros valores a excluir, vinculados a decisão judicial;

42 – Outros valores a excluir, não vinculados a decisão judicial\.

MFS\-19941

MFS\-20225

RN07

__Campo Apropriação Ajuste__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou preenchido de forma incorreta\.

__Conteúdo válido:__

01 – Referente ao PIS/Pasep e a Cofins;

02 – Referente unicamente ao PIS/Pasep;

03 – Referente unicamente à Cofins\.

MFS\-19941

RN08

__Campo CNPJ__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“O Campo CNPJ deve ser preenchido”*\.

MFS\-19941

RN09

__Campo Valor Total Ajuste__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN10

__Campo Valor Ajuste CST01__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN11

__Campo Valor Ajuste CST02__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN12

__Campo Valor Ajuste CST03__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN13

__Campo Valor Ajuste CST04__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN14

__Campo Valor Ajuste CST05__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN15

__Campo Valor Ajuste CST06__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN16

__Campo Valor Ajuste CST07__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN17

__Campo Valor Ajuste CST08__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN18

__Campo Valor Ajuste CST09__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN19

__Campo Valor Ajuste CST49__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN20

__Campo Valor Ajuste CST99__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN21

__Campo Nº Recibo__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

RN22

__Campo Informação Complementar__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-19941

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

