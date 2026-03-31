# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX991

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX991.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3564

Tatiane Lima

Novo código de modelo de Documento Fiscal \- Manifesto Eletrônico de Documentos Fiscais \- MDF\-e\.

OS4316

Marcos Roberto

Criação dos campos Código e Descrição da SCP

OS4835

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho dos campos “COO”, “COO Inicial” e “COO Final” de 006 para 009 posições\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX991 \- Capa Redução Z, que deve ser criada com a seguinte estrutura:

__\[ALTERADA – OS4835\]__

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

Modelo Documento

A

002

SIM

NÃO

Número do Caixa

A

003

SIM

SIM

CRZ

A

006

SIM

SIM

Data do movimento

N

008

SIM

SIM

COO

A

009

SIM

NÃO

CRO

A

006

NÃO

NÃO

Data de emissão

N

008

NÃO

NÃO

Hora de emissão

N

006

NÃO

NÃO

COO Inicial

A

009

NÃO

NÃO

COO Final

A

009

NÃO

NÃO

GT Inicial

N

015V002

NÃO

NÃO

GT Final 

N

015V002

NÃO

NÃO

Venda Bruta Diária

N

015V002

NÃO

NÃO

Venda Líquida Diária

N

015V002

NÃO

NÃO

PIS

N

015V002

NÃO

NÃO

COFINS

N

015V002

NÃO

NÃO

Valor Tributado ICMS

N

015V002

NÃO

NÃO

Valor ICMS

N

015V002

NÃO

NÃO

Substituição Tributária ICMS

N

015V002

NÃO

NÃO

Isento ICMS

N

015V002

NÃO

NÃO

Não Incidência ICMS

N

015V002

NÃO

NÃO

Desconto ICMS

N

015V002

NÃO

NÃO

Acréscimo ICMS

N

015V002

NÃO

NÃO

Cancelamento ICMS

N

015V002

NÃO

NÃO

IOF

N

015V002

NÃO

NÃO

Valor Tributado ISSQN

N

015V002

NÃO

NÃO

Valor ISSQN

N

015V002

NÃO

NÃO

Substituição Tributária ISSQN

N

015V002

NÃO

NÃO

Isento ISSQN

N

015V002

NÃO

NÃO

Não Incidência ISSQN

N

015V002

NÃO

NÃO

Desconto ISSQN

N

015V002

NÃO

NÃO

Acréscimo ISSQN

N

015V002

NÃO

NÃO

Cancelamento ISSQN

N

015V002

NÃO

NÃO

Valor Operações Não Fiscais

N

015V002

NÃO

NÃO

Valor Desconto Não Fiscais

N

015V002

NÃO

NÃO

Valor Acréscimo Não Fiscais

N

015V002

NÃO

NÃO

Valor Cancelamento Não Fiscais

N

015V002

NÃO

NÃO

Código da SCP

A

014

NÃO

NÃO

 

OS4835

RN02

__Campo Modelo Documento__

Aceitar a importação do novo código de modelo “58”\.

OS3564

RN03

__Campo Código da SCP__

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

OS4316

RN04

__Campo COO__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

RN05

__Campo COO Inicial__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

RN06

__Campo COO Final__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

