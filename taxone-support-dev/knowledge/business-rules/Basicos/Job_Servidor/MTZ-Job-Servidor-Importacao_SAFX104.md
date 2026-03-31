# MTZ-Job-Servidor-Importacao_SAFX104

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX104.docx
- **Modificado:** 2021-03-31
- **Tamanho:** 77 KB

---

THOMSON REUTERS

104

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS2732\-A

Juliana Garcia

O objetivo desta OS é incluir o campo Data Final de Vigência para manter um histórico da parametrização com as gerações\.

CH23696\_2015

Julyana Perrucini

Alteração das regras de importação, Online e Batch, da SAFX104\.

MFS24920

Andréa Rocha

Inclusão do campo "% de Redução de BC" e dos campos reservados\.

__MFS28596__

Liliane Assaf

Inclusão do campo “Alíquota FCP” e tratamento para UF = ‘RS’ não aceitar produto associado\.

__MFS47349__

Liliane Assaf

RN08: Retirar a restrição quanto a UF = ‘RS’ não aceitar produto associado\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX104 \- Parâmetros de Produto por UF \(Ressarcimento e Complemento de ICMS\-ST\), que deve ser criada com a seguinte estrutura:

__\[ALTERADA – OS2732\-A\]__

__\[MFS24920\]__

__\[MFS28596\]__

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Tipo de Registro

A

001

SIM

SIM

UF

A

002

SIM

SIM

Indicador de Produto

A

001

SIM

SIM

Código do Produto

A

035

SIM

SIM

Início de Vigência

N

008

SIM

SIM

Alíquota Interna

N

003V004

SIM

Indicador de Produtos Associados

A

001

Código de Produto Associados

A

035

Modelo do Livro

N

001

Validade Final

N

008

% de Redução de BC

N

003V004

Reservado 1

N

015V002

Reservado 2

N

015V002

Reservado 3

N

015V002

Reservado 4

A

050

Reservado 5

A

050

Reservado 6

A

050

Reservado 7

A

050

Reservado 8

A

050

Alíquota FCP

N

003V004

 

OS2732\-A

MFS24920

RN01

__Campo Tipo de Registro__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS2732\-A

RN02

__Campo UF__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS2732\-A

RN03

__Campo Indicador de Produto__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS2732\-A

RN04

__Campo Código do Produto __

Como o campo é obrigatório de preenchimento, <a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__\[ALTERADA – CH23696\_2015\]__

__Tratamento:__

- Se o usuário incluir um produto com o código de um produto que já se encontra parametrizado e com a data inicial de vigência preenchida, o sistema deverá bloquear a gravação e emitir a mensagem de erro: *“Foi encontrada parametrização para o produto <<IND\_PRODUTO \+ hífen \(\-\) \+ COD\_PRODUTO>> com data inicial de vigência igual a <<VALID\_INICIAL: do Produto localizado>>, e que entra em conflito com as datas de vigência informadas\.”*; assim como é feita para tela de manutenção, pois só será possível incluir o produto após inclusão de data de validade final\.

OS2732\-A

CH23696\_2015

RN05

__Campo Início de Vigência __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS2732\-A

RN06

__Campo Alíquota Interna__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS2732\-A

RN07

__Campo Indicador de Produtos Associados__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS2732\-A

RN08

__Campo Código de Produto Associados__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

\[MFS47349\] Exclusão da regra que impede a importação de produtos associado para UF = RS

\[Alterada \- MFS28596\] 

__Tratamento:__

- Para UF = ‘RS’ não podem ser informados Produtos Associados\.  Caso seja informado, o sistema deverá bloquear a gravação e emitir a mensagem de erro: *“O estado do Rio Grande do Sul nao admite parametrizacao com produtos associados\.”*

OS2732\-A

MFS28596

__MFS47349__

RN09

__Campo Modelo do Livro__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS2732\-A

RN10

__\[ALTERADA – OS2732\-A\]__

__Campo Validade Final__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__Tratamento:__

- Se o usuário preencher a data final de vigência menor a data inicial de vigência, o sistema deverá bloquear a alteração do cadastro e emitir a mensagem de erro: “Data final de vigência inválida”\.

OS2732\-A

RN11

__Campo % de Redução de BC__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN12

__Campo Reservado 1__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN13

__Campo Reservado 2__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN14

__Campo Reservado 3__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN15

__Campo Reservado 4__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN16

__Campo Reservado 5__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN17

__Campo Reservado 6__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN18

__Campo Reservado 7__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN19

__Campo Reservado 8__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS24920

RN20

__Campo Alíquota FCP__

Campo de preenchimento não obrigatório\. 

Aceitar conteúdo numérico e nulo\.

Caso seja preenchido com informação não numérica apresentar mensagem de erro padrão

MFS28596

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

