# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX175

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX175.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 80 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX175

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS1676

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX175\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX175 \- Registros de Estorno de Débitos, que deve ser criada com a seguinte estrutura:

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

Período de Declaração da Informação

N

006

SIM

SIM

Nº da NF Objeto do Estorno

A

012

SIM

SIM

Série da NF Objeto do Estorno

A

003

SIM

Subsérie da NF Objeto do Estorno

A

002

SIM

Data de Emissão da NF Objeto do Estorno

D

008

SIM

SIM

Ind\. PFJ da NF Objeto do Estorno

A

001

SIM

SIM

Código PFJ da NF Objeto do Estorno

A

014

SIM

SIM

Nº do Item da NF Objeto do Estorno

N

007

SIM

SIM

Nº da NF de Ressarcimento

A

012

SIM

Série da NF de Ressarcimento

A

003

SIM

Subsérie da NF de Ressarcimento

A

002

SIM

Nº do Item da NF de Ressarcimento

N

007

SIM

Data de Emissão da NF de Ressarcimento

D

008

SIM

Tipo da Informação

A

001

SIM

Modelo do Documento da NF Objeto do Estorno

A

002

SIM

Modelo do Documento da NF de Ressarcimento

A

002

Cód\. Autenticação da NF Objeto do Estorno

A

032

Nº do Terminal Faturado da NF Objeto do Estorno

A

014

Valor Total da NF Objeto do Estorno

N

015V002

BC de ICMS da NF Objeto do Estorno

N

015V002

Valor do ICMS da NF Objeto do Estorno

N

015V002

Ind\. Produto da NF Objeto do Estorno

A

001

SIM

Cód\. Produto da NF Objeto do Estorno

A

035

SIM

Valor Total do Item da NF Objeto do Estorno

N

015V002

BC de ICMS do Item da NF Objeto de Estorno

N

015V002

Valor do ICMS do Item da NF Objeto de Estorno

N

015V002

Motivo do Estorno

A

200

Nº da Reclamação

A

020

ICMS a ser Estornado

N

015V002

Hipótese de Estorno

A

001

Código do Sistema de Origem

A

004

 

__Tratamento Geral:__

- Na carga da SAFX175 não haverá o campo Status, mas esse campo será acrescentado na tabela definitiva para trabalhar com o relatório de conciliação das notas fiscais de comunicação e telecomunicação, então na importação para a tabela definitiva esse campo será preenchido com N por default;
- Para o filtro de data na importação, será considerado o campo Período de Declaração da Informação\.

MFS1676

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS1676

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS1676

RN04

__Campo Período de Declaração da Informação__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou caso esteja preenchido com conteúdo inválido\.

- Se o campo não for preenchido, emitir a mensagem: “O campo Periodo de Declaracao da Informacao deve ser preenchido\.”;
- Se o campo for preenchido com conteúdo inválido, emitir a mensagem: “O campo Periodo de Declaracao da Informacao e invalido\.”\.

MFS1676

RN05

__Campo Nº da NF Objeto do Estorno__

Como o campo é obrigatório de preenchimento, <a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

- Se o campo não for preenchido, emitir a mensagem: “O campo Numero da NF Objeto do Estorno deve ser preenchido\.”\.

MFS1676

RN06

__Campo Série da NF Objeto do Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN07

__Campo Subsérie da NF Objeto do Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN08

__Campo Data de Emissão da NF Objeto do Estorno__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou caso esteja preenchido com conteúdo inválido\.

- Se o campo não for preenchido, emitir a mensagem: “O campo Data de Emissao da NF Objeto do Estorno deve ser preenchido\.”;
- Se o campo for preenchido com conteúdo inválido, emitir a mensagem: “O campo Data de Emissao da NF Objeto do Estorno e invalido\.”\.

MFS1676

RN09

__Campo Ind\. PFJ da NF Objeto do Estorno__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou caso esteja preenchido com conteúdo inválido\.

MFS1676

RN10

__Campo Código PFJ da NF Objeto do Estorno__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou caso esteja preenchido com conteúdo inválido<a id="OLE_LINK4"></a><a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>, fazer a verificação se não estiver cadastrado na SAFX04\.

MFS1676

RN11

__Campo Nº do Item da NF Objeto do Estorno__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS1676

RN12

__Campo Nº da NF de Ressarcimento__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN13

__Campo Série da NF de Ressarcimento__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN14

__Campo Subsérie da NF de Ressarcimento__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN15

__Campo Nº do Item da NF de Ressarcimento__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN16

__Campo Data de Emissão da NF de Ressarcimento __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN17

__Campo Tipo da Informação__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou caso esteja preenchido com conteúdo inválido\.

- Se o campo não for preenchido, emitir a mensagem: “O campo Tipo da Informacao deve ser preenchido\.”;
- Se o campo for preenchido com conteúdo inválido, emitir a mensagem: “O campo Tipo da Informacao e invalido\.”\.

Só serão permitidos os seguintes indicadores de tipo da informação <R> e <E>:

- R – ICMS Recuperado
- E – ICMS Objeto do Estorno

MFS1676

RN18

__Campo Modelo do Documento da NF Objeto do Estorno __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou caso esteja preenchido com conteúdo inválido, fazer a verificação se não estiver cadastrado na SAFX2024\.

MFS1676

RN19

__Campo Modelo do Documento da NF de Ressarcimento__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo e fazer a verificação se não estiver cadastrado na SAFX2024\.

MFS1676

RN20

__Campo Cód\. Autenticação da NF Objeto do Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN21

__Campo Nº do Terminal Faturado da NF Objeto do Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN22

__Campo Valor Total da NF Objeto do Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN23

__Campo BC de ICMS da NF Objeto do Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN24

__Campo Valor do ICMS da NF Objeto do Estorno __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN25

__Campo Ind\. Produto da NF Objeto do Estorno__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou caso esteja preenchido com conteúdo inválido\.

MFS1676

RN26

__Campo Cód\. Produto da NF Objeto do Estorno__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido ou caso esteja preenchido com conteúdo inválido, fazer a verificação se não estiver cadastrado na SAFX2013\.

MFS1676

RN27

__Campo Valor Total do Item da NF Objeto do Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN28

__Campo BC de ICMS do Item da NF Objeto de Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN29

__Campo Valor do ICMS do Item da NF Objeto de Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN30

__Campo Motivo do Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN31

__Campo Nº da Reclamação __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN32

__Campo ICMS a ser Estornado__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

RN33

__Campo Hipótese de Estorno__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Só serão permitidos os seguintes indicadores de hipóteses <1>, <2>, <3>, <4>, <5>, <6> e <7>:

- 1 – Erro de medição
- 2 – Erro de faturamento
- 3 – Erro de tarifação do serviço
- 4 – Erro de emissão do documento
- 5 – Formalização de discordância do tomador do serviço, relativamente à cobrança ou aos respectivos vaçores
- 6 – Cobrança em duplicidade
- 7 – Clonagem de linha ou terminal telefônico

MFS1676

RN34

__Campo Código do Sistema de Origem__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS1676

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

