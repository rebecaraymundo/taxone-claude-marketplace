# MTZ_JOB_SERVIDOR_Exportacao_SAFX993

- **Fonte:** MTZ_JOB_SERVIDOR_Exportacao_SAFX993.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Regras de Exportação SAFX993

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4835

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho dos campos “COO \(Contador de Ordem de Operação\)” e “Número do COO Vinculado” de 006 para 009 posições\.

MFS2898

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho dos campos “CCF, CVC ou CBP, conforme o documento emitido”, “GNF\-Contador Geral de Operação Não Fiscal” e “GRG\-Contador Geral de Relatório Gerencial” de 6 para 9 posições\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX993 \- Capa Cupom Fiscal, que deve ser criada com a seguinte estrutura:

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

<a id="OLE_LINK65"></a><a id="OLE_LINK66"></a><a id="OLE_LINK67"></a><a id="OLE_LINK68"></a><a id="OLE_LINK69"></a><a id="OLE_LINK70"></a>009

NÃO

NÃO

CCF, CVC ou CBP, conforme o documento emitido

A

<a id="OLE_LINK71"></a><a id="OLE_LINK72"></a><a id="OLE_LINK73"></a>006

009

NÃO

NÃO

GNF \(Contador Geral de Operação Não Fiscal\)

A

006

009

NÃO

NÃO

GRG \(Contador Geral de Relatório Gerencial\)

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

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

