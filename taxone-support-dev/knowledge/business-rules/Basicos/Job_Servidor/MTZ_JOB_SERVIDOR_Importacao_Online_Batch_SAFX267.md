# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX267

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX267.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX267

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-13327

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX267 para atender os Registros K291 e K301 da EFD\-ICMS/IPI/ISS\.

MFS\-21976

Julyana Perrucini

Essa MFS tem como objetivo incluir o campo Unidade de Medida para ser utilizada na conversão de medida do Bloco K\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX267 – Produção Conjunta – Item de Produção, que deve ser criada com a seguinte estrutura:

\[ALTERADA – MFS\-21976\]

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

Estabelecimento

A

006

SIM

SIM

Período de Referência

N

006

SIM

SIM

Tipo de Produção Conjunta

N

001

SIM

SIM

Data da Produção no Terceiro

N

008

SIM

SIM

Código da Ordem de Produção

A

030

SIM

SIM

Data Início OP

N

008

SIM

SIM

Indicador Produto

A

001

SIM

NÃO

Código do Produto

A

035

SIM

NÃO

Quantidade

N

011V006

NÃO

NÃO

Unidade de Medida

A

008

SIM

NÃO

 

MFS\-13327

MFS\-21976

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-13327

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-13327

RN04

__Campo Período de Referência__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-13327

RN05

__Campo Tipo de Produção Conjunta __

Como o campo é obrigatório de preenchimento e deve ser um conteúdo válido\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Tipo de Produção Conjunta não preenchido ou inválido”*\.

__Conteúdo válido:__

1 – Própria

2 – Efetuada por Terceiros

MFS\-13327

RN06

__Campo Data da Produção no Terceiro__

Como o campo é obrigatório de preenchimento para o Tipo de Produção Conjunta igual a 2 e deve ser uma data válida\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro: *“Data da Produção no Terceiro não preenchida ou inválida”*\. Se o Tipo de Produção Conjunta for igual a 1 esse campo deve ser preenchido com “branco” \(01/01/1900\)\.

MFS\-13327

RN07

__Campo Código da Ordem de Produção__

Quando esta tabela for utilizada e a empresa não utilizar numeração para as ordens de produção e o Tipo de Produção Conjunta for igual a 1, o campo poderá ser preenchido com qualquer informação que o auxilie em um possível controle \(número de lote, por exemplo\)\.

Como o campo é obrigatório de preenchimento para o Tipo de Produção Conjunta igual a 1\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“Código da Ordem de Produção não preenchido”*\. Se o Tipo de Produção Conjunta for igual a 2 esse campo deve ser preenchido com branco\.

Se não desejar que a informação seja utilizada no arquivo da EFD, deverá selecionar o parâmetro “Não informar o número da ordem de produção / serviço” na parametrização do SPED Fiscal, no menu “Parâmetros > Dados Iniciais”\. Mas para utilizar este parâmetro, é necessário que a carga dos dados da produção seja feita com apenas um registro na SAFX266 por Período de Referência\. Caso contrário ocorrerá duplicidade na geração do registro K290\.

MFS\-13327

RN08

__Campo Data Início OP__

Como o campo é obrigatório de preenchimento para o Tipo de Produção Conjunta igual a 1 e deve ser uma data válida\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro: *“Data Início OP não preenchida ou inválida”*\. Se o Tipo de Produção Conjunta for igual a 2 esse campo deve ser preenchido com “branco” \(01/01/1900\)\.

MFS\-13327

RN09

__Campo Indicador Produto__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar o produto com a SAFX2013\.

MFS\-13327

RN10

__Campo Código do Produto __

Como o campo é obrigatório de preenchimento, <a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar o produto com a SAFX2013\.

MFS\-13327

RN11

__Campo Quantidade __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-13327

RN12

__Campo Unidade de Medida __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar o produto com a SAFX2007\.

MFS\-21976

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

