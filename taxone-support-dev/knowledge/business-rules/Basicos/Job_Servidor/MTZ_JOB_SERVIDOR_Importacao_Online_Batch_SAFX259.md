# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX259

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX259.docx
- **Modificado:** 2020-06-19
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX259

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-15570

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX259\.

MFS21354

Lara Aline

Criação de 8 novos campos Reservados\.

MFS38312

Andréa Rocha

Retirar o campo PFJ do usuário da chave primária da tabela\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX259 \- Fatura de Serviços de Comunicação e de Telecomunicações, que deve ser criada com a seguinte estrutura:

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

Valor Total da Fatura

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

RN06

__Campo Indicador da Pessoa Física/Jurídica do Usuário __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\. Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN07

__Campo Código da Pessoa Física/Jurídica do Usuário __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\. Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN08

__Campo Valor Total da Fatura__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“O Campo Valor Total da Fatura Comercial deve ser preenchido”*\.

MFS\-15570

RN09

__Campo Reservado 1__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN10

__Campo Reservado 2__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN11

__Campo Reservado 3__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN12

__Campo Reservado 4__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN13

__Campo Reservado 5__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN14

__Campo Reservado 6__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN15

__Campo Reservado 7__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

RN16

__Campo Reservado 8__

Não obrigatório\.

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

