# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX221

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX221.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 65 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4710

Julyana Perrucini

Definição das regras de importação, Online e Batch, da SAFX221\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX221 \- Tabela de Sociedade Uniprofissional, que deve ser criada com a seguinte estrutura:

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

Valor mensal das receitas auferidas pela sociedade

N

015V002

SIM

NÃO

Quantidade de profissionais habilitados

N

006

SIM

NÃO

Valor do ISS a recolher

N

015V002

NÂO

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

__Valor mensal das receitas auferidas pela sociedade__

Como o campo é obrigatório de preenchimento, o valor informado neste campo deve ser maior que zero\. Se for informado valor menor que zero, retornar mensagem de erro: “Valor mensal das receitas deve ser maior que 0”\.

OS4710

RN06

__Quantidade de profissionais habilitados __

Como o campo é obrigatório de preenchimento, a quantidade informada neste campo deve ser maior que zero\. Se for informado valor menor que zero, retornar mensagem de erro: “Quantidade de profissionais habilitados deve ser maior que 0”\.

OS4710

RN07

__Valor do ISS a recolher __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4710

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

