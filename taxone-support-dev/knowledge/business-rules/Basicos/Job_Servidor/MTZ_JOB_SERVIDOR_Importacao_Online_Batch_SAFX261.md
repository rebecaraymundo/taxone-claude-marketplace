# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX261

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX261.docx
- **Modificado:** 2020-06-02
- **Tamanho:** 71 KB

---

THOMSON REUTERS

261

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-15570

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX261\.

MFS\-23140

Julyana Perrucini

Essa MFS tem como objetivo criar campo interno para inclusão do indicador e produto como chave na tabela\.

MFS\-35780

Andréa Rocha

Essa MFS tem como objetivo incluir 3 campos novos \(número, série e subsérie do documento fiscal\) e alterar a chave da tabela\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

Estrutura da tabela SAFX261 🡪 vide manual de layout

Campos que compõe a chave da tabela:

__   Código da Empresa \+ Código do Estabelecimento \+ Número Documento Fiscal \+ Série \+  Subsérie \+ Número do Terminal \+ PFJ do Usuário \+ Data da Recarga \+ Discr\_Produto__

A manutenção desta tabela é feita no Módulo Básicos \- Data Warehouse, menu <a id="OLE_LINK54"></a><a id="OLE_LINK55"></a>Manutenção 🡪 Telecom 🡪 Terminais Telefônicos Pré\-pagos

Tabela de Destino:

A SAFX261 alimenta a tabela definitiva X261\_CRED\_TERMINAL\_TEL

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS\-35780

RN01

__Campo Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS\-15570

RN02

__Campo Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*\.

MFS\-15570

RN03

__Campo Número do Terminal Telefônico__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“O Campo Número do Terminal Telefônico deve ser preenchido”*\.

MFS\-15570

RN04

__Campo Indicador da Pessoa Física/Jurídica do Usuário __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN05

__Campo Código da Pessoa Física/Jurídica do Usuário __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN06

__Campo Data da Requisição da Recarga__

Como o campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“O Campo Data da Requisição da Recarga deve ser preenchido com um valor válido”*\.

MFS\-15570

RN07

__Campo Indicador do Produto__

Campo de preenchimento não obrigatório, aceitar conteúdo informado, inclusive nulo\.

Validar o produto com a SAFX2013\.

MFS\-15570

RN08

__Campo Código do Produto__

Campo de preenchimento não obrigatório, aceitar conteúdo informado, inclusive nulo\.

Validar o produto com a SAFX2013\.

__\[MFS\-23140\]__

__Campo Indicador do Produto\+Código do Produto \(campo interno\)__

Foi necessário criar esse campo chave concatenando o campo indicador do produto e o código do produto, pois o produto não é chave na tabela, e ocorre que alguns contribuintes emitem para um mesmo terminal telefônico produtos diferentes, ou seja, diversos produtos para uma mesma fatura\.

__Tratamento:__

- Se houver preenchimento dos campos Indicador do Produto e Código do Produto, preencher esse campo interno concatenando as informações, caso os campos Indicador do Produto e Código do Produto não estiverem preenchidos, preencher esse campo com branco\.

MFS\-15570/ MFS\-23140

RN09

__Campo Indicador da Pessoa Física/Jurídica Vendedor do Crédito__

Campo de preenchimento não obrigatório, aceitar conteúdo informado, inclusive nulo\.

Validar a pessoa fis/jur com a SAFX04\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570/

MFS\-35780

RN10

__Campo Código da Pessoa Física/Jurídica Vendedor do Crédito__

Campo de preenchimento não obrigatório, aceitar conteúdo informado, inclusive nulo\.

Validar a pessoa fis/jur com a SAFX04\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570/

MFS\-35780

RN11

__Campo Indicador da Pessoa Física/Jurídica Responsável pelo Repasse__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN12 

__Campo Código da Pessoa Física/Jurídica Responsável pelo Repasse__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Validar a pessoa fis/jur com a SAFX04\.

MFS\-15570

RN13

__Campo Valor Total da Recarga__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15570

RN14

__Campo Valor da Dedução Automática __

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15570

RN15

__Campo Valor da Taxa por Antecipação de Crédito__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15570

RN16

__Campo Valor da Multa de Atraso__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

MFS\-15570

RN17

__Campo Número Documento Fiscal__

Como o campo é obrigatório de preenchimento deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-35780

RN18

__Campo Série Documento Fiscal__

Campo de preenchimento não obrigatório, aceitar conteúdo informado, inclusive nulo\.

Se o campo não estiver preenchido, deve ser gravado com um espaço em branco, uma vez que o campo faz parte da chave\.

MFS\-35780

RN19

__Campo Subsérie Documento Fiscal__

Campo de preenchimento não obrigatório, aceitar conteúdo informado, inclusive nulo\.

Se o campo não estiver preenchido, deve ser gravado com um espaço em branco, uma vez que o campo faz parte da chave\.

MFS\-35780

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

