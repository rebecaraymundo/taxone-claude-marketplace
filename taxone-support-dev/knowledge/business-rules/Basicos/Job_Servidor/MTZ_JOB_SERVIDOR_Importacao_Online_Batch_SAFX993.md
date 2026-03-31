# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX993

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX993.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

3

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3564

Tatiane Lima

Novo código de modelo de Documento Fiscal \- Manifesto Eletrônico de Documentos Fiscais \- MDF\-e\.

OS3983

Marcos Paula

Novos campos para atender ao Cupom Fiscal Eletrônico e inclusão de novo modelo – 60\.

OS4835

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho dos campos “COO \(Contador de Ordem de Operação\)” e “Número do COO Vinculado” de 006 para 009 posições\.

MFS2898

Julyana Perrucini

<a id="OLE_LINK63"></a><a id="OLE_LINK64"></a>Este documento tem como objetivo alterar o tamanho dos campos <a id="OLE_LINK49"></a><a id="OLE_LINK50"></a>“CCF, CVC ou CBP, conforme o documento emitido”, “GNF\-Contador Geral de Operação Não Fiscal” e “GRG\-Contador Geral de Relatório Gerencial” de 6 para 9 posições\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX993 \- Capa Cupom Fiscal, que deve ser criada com a seguinte estrutura:

__\[ALTERADA – OS4835/ MFS2898\]__

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

COO \(Contador de Ordem de Operação\)

A

009

SIM

SIM

Data da emissão

N

008

SIM

SIM

Nome do adquirente

A

040

NÃO

NÃO

CPF/CNPJ do adquirente

A

014

NÃO

NÃO

Tipo de Documento

A

001

SIM

NÃO

Situação do Documento

A

001

SIM

NÃO

Denominação

A

002

NÃO

NÃO

Número do COO Vinculado

A

<a id="OLE_LINK81"></a><a id="OLE_LINK82"></a><a id="OLE_LINK83"></a><a id="OLE_LINK84"></a><a id="OLE_LINK85"></a><a id="OLE_LINK86"></a>009

NÃO

NÃO

<a id="OLE_LINK92"></a><a id="OLE_LINK93"></a><a id="OLE_LINK94"></a><a id="OLE_LINK95"></a><a id="OLE_LINK96"></a>CCF, CVC ou CBP, conforme o documento emitido

A

<a id="OLE_LINK87"></a><a id="OLE_LINK88"></a><a id="OLE_LINK89"></a>006

009

NÃO

NÃO

<a id="OLE_LINK101"></a><a id="OLE_LINK102"></a><a id="OLE_LINK103"></a><a id="OLE_LINK104"></a>GNF \(Contador Geral de Operação Não Fiscal\)

A

006

009

NÃO

NÃO

<a id="OLE_LINK105"></a><a id="OLE_LINK106"></a><a id="OLE_LINK107"></a><a id="OLE_LINK108"></a>GRG \(Contador Geral de Relatório Gerencial\)

A

006

009

NÃO

NÃO

CDC \(Contador de Comprovante de Crédito ou Débito\)

A

006

NÃO

NÃO

CRZ \(Contador de Redução Z\)

A

006

NÃO

NÃO

Data final de emissão

N

008

NÃO

NÃO

Hora final de emissão

N

006

NÃO

NÃO

Código da Unidade da Federação

A

002

NÃO

NÃO

Código do Município

N

005

NÃO

NÃO

Valor do Subtotal do Documento

N

015V002

NÃO

NÃO

Valor do Desconto sobre subtotal

N

015V002

NÃO

NÃO

Valor do Acréscimo sobre subtotal

N

015V002

NÃO

NÃO

Valor Total Líquido

N

015V002

NÃO

NÃO

Valor do Cancelamento de Acréscimo no Subtotal

N

015V002

NÃO

NÃO

Valor do IOF

N

015V002

NÃO

NÃO

Chave do CFe

A

080

NÃO

NÃO

Nº do Contador do CFe

A

009

NÃO

NÃO

 

OS4835

MFS2898

RN02

__Campo Modelo Documento__

Aceitar a importação do novo código de modelo “58” ou “60”\.

OS3564

OS3983

RN03

__Campo COO \(Contador de Ordem de Operação\)__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

RN04

<a id="OLE_LINK90"></a><a id="OLE_LINK91"></a>__Campo Número do COO Vinculado__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

<a id="_Hlk442338981"></a>RN05

__Campo CCF, CVC ou CBP, conforme o documento emitido__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__\[ALTERADA – MFS2898\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

MFS2898

RN06

__Campo GNF \(Contador Geral de Operação Não Fiscal\)__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__\[ALTERADA – MFS2898\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

MFS2898

RN07

__Campo GRG \(Contador Geral de Relatório Gerencial\)__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__\[ALTERADA – MFS2898\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

MFS2898

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

