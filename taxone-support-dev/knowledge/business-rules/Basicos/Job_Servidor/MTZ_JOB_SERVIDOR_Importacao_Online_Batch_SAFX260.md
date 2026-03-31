# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX260

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX260.docx
- **Modificado:** 2025-12-01
- **Tamanho:** 73 KB

---

THOMSON REUTERS

260

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-15570

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX260\.

MFS\-22679

Julyana Perrucini

Essa MFS tem como objetivo alterar o campo Modelo da Nota Fiscal para aceitar o modelo “55”\.

MFS21354

Lara Aline

Criação de 8 novos campos Reservados\.

MFS23990

Andréa Rocha

Inclusão do modelo 65

MFS38312

Andréa Rocha

Retirar o campo PFJ do usuário da chave primária da tabela\.

MFS992323

Andréa Rocha

Incluir o código de modelo 62 para a recuperação das notas fiscais\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX260 \- Itens Fatura de Serviços de Comunicação e de Telecomunicações, que deve ser criada com a seguinte estrutura:

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

Número da Fatura Comercial

A

020

SIM

SIM

Data de Emissão da Fatura

N

008

SIM

SIM

Indicador da Pessoa Física/Jurídica do Usuário

A

001

SIM

SIM NÃO

Código da Pessoa Física/Jurídica do Usuário

A

014

SIM

SIM NÃO

Número do Item

N

007

SIM

SIM

Indicador do Produto

A

001

NÃO

NÃO

Código do Produto

A

035

NÃO

NÃO

Origem do Item

A

001

SIM

NÃO

Indicador da Pessoa Física/Jurídica do Terceiro

A

001

NÃO

NÃO

Código da Pessoa Física/Jurídica do Terceiro

A

014

NÃO

NÃO

Data de Emissão da Nota Fiscal

N

008

NÃO

NÃO

Modelo da Nota Fiscal

A

002

NÃO

NÃO

Série da Nota Fiscal

A

003

NÃO

NÃO

Número da Nota Fiscal

A

012

NÃO

NÃO

Valor Total da Nota Fiscal

N

015V002

NÃO

NÃO

Valor do Item

N

015V002

SIM

NÃO

Reservado 1

N

015V002

NÃO

NÃO

Reservado 2

N

015V002

NÃO

NÃO

Reservado 3

N

015V002

NÃO

NÃO

Reservado 4

A

050

NÃO

NÃO

Reservado 5

A

050

NÃO

NÃO

Reservado 6

A

050

NÃO

NÃO

Reservado 7

A

050

NÃO

NÃO

Reservado 8

A

050

NÃO

NÃO

__Tratamento: __

- Essa tabela será referenciada à tabela da SAFX259, então se não houver capa para o item informado, validação esta pelos campos chave da tabela, deverá ser informada a seguinte mensagem de log: *“Não existe fatura para esse item informado”*\.

MFS\-15570

MFS21354

MFS38312

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15570

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15570

RN04

__Campo Número da Fatura Comercial__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“O Campo Número da Fatura Comercial deve ser preenchido”*\.

MFS\-15570

RN05

__Campo Data de Emissão da Fatura__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15570

RN06

__Campo Indicador da Pessoa Física/Jurídica do Usuário __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN07

__Campo Código da Pessoa Física/Jurídica do Usuário __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN08

__Campo Número do Item__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-15570

RN09

__Campo Indicador do Produto__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Validar o produto com a SAFX2013\.

MFS\-15570

RN10

__Campo Código do Produto__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Validar o produto com a SAFX2013\.

MFS\-15570

RN11

__Campo Origem do Item__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“O Campo Origem do Item deve ser preenchido com os valores válidos 1 ou 2”*\.

MFS\-15570

RN12

__Campo Indicador da Pessoa Física/Jurídica do Terceiro__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN13

__Campo Código da Pessoa Física/Jurídica do Terceiro __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN14

__Campo Data de Emissão da Nota Fiscal __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15570

RN15

__Campo Modelo da Nota Fiscal__

__\[ALTERADA – MFS\-22679\]__

__\[MFS992323\] __Inclusão do modelo 62

Campo de preenchimento não obrigatório, validar com a SAFX2024 e aceitar conteúdo 21, 22, 55, 62 e 65, inclusive nulo\. Caso o conteúdo não entre nessas condições, deve ser exibida a mensagem de erro: *“O Campo Modelo do Documento deve ser: <nulo, 21, 22, 55, 62 ou 65>”\.*

MFS\-15570

MFS\-22679

MFS23990

MFS992323

RN16

__Campo Série da Nota Fiscal__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15570

RN17

__Campo Número da Nota Fiscal__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15570

RN18

__Campo Valor Total da Nota Fiscal__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15570

RN19

__Campo Valor do Item__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“O Campo Valor do Item deve ser preenchido”*\. Esse campo poderá ter sinal negativo na primeira posição do campo porque pode existir item de desconto\.

MFS\-15570

RN20

__Campo Reservado 1__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN21

__Campo Reservado 2__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN22

__Campo Reservado 3__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN23

__Campo Reservado 4__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN24

__Campo Reservado 5__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN25

__Campo Reservado 6__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN26

__Campo Reservado 7__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN27

__Campo Reservado 8__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

