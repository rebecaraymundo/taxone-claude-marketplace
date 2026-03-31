# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX994

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX994.docx
- **Modificado:** 2023-01-19
- **Tamanho:** 70 KB

---

THOMSON REUTERS

4

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS2995\-B\-dw

\-

Inclusão dos campos de base de cálculo, alíquota e código de situação tributária do PIS e da COFINS, para atendimento ao Ato Declaratório 55 de Dez/2009, que incluiu vários arquivos novos na IN 86\.

OS4316

Marcos Roberto

Criação dos campos Código e Descrição da SCP\.

OS4835

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho do campo “COO \(Contador de Ordem de Operação\)” de 006 para 009 posições\.

MFS507186

Liliane Assaf

Inclusão do Campo Amparo/Texto/Ocorrência

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX994 – Detalhe do Cupom Fiscal, que deve ser criada com a seguinte estrutura:

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

Número do item

N

005

SIM

SIM

Indicador do Produto

A

001

SIM

NÃO

Código do Produto

A

035

SIM

NÃO

Código do Serviço

A

004

SIM

NÃO

Situação do ìtem no Cupom

A

001

SIM

NÃO

Código Situação Tributária “A”

A

001

NÃO

NÃO

Código Situação Tributária “B”

A

002

NÃO

NÃO

CFOP

A

004

NÃO

NÃO

Código do Totalizador Parcial do ECF

A

007

NÃO

NÃO

Quantidade

N

013V004

NÃO

NÃO

Unidade

A

003

NÃO

NÃO

Valor unitário

N

015V004

NÃO

NÃO

Valor do ìtem

N

015V002

NÃO

NÃO

Valor do desconto sobre item

N

015V002

NÃO

NÃO

Valor do acréscimo sobre item

N

015V002

NÃO

NÃO

Valor total líquido

N

015V002

NÃO

NÃO

Quantidade cancelada

N

013V004

NÃO

NÃO

Valor cancelado

N

015V002

NÃO

NÃO

Valor de Cancelamento de acréscimo no item

N

015V002

NÃO

NÃO

Valor do PIS

N

015V002

NÃO

NÃO

Valor do COFINS

N

015V002

NÃO

NÃO

Valor da Base de Cálculo

N

015V002

NÃO

NÃO

Valor do Imposto

N

015V002

NÃO

NÃO

Código Fiscal de Prestação de Serviço

A

004

NÃO

NÃO

Código de Tributação do ISS

A

002

NÃO

NÃO

Código de Situação Tributária PIS

N

002

NÃO

NÃO

Base de Cálculo PIS

N

015V003

NÃO

NÃO

Alíquota PIS

N

003V004

NÃO

NÃO

Código de Situação Tributária COFINS

N

002

NÃO

NÃO

Base de Cálculo COFINS

N

015V003

NÃO

NÃO

Alíquota COFINS

N

003V004

NÃO

NÃO

Quantidade \- Base de Cálculo PIS

N

015V003

NÃO

NÃO

Alíquota do PIS \- em Reais

N

015V004

NÃO

NÃO

Conta Contábil

A

070

NÃO

NÃO

Quantidade \- Base de Cálculo COFINS

N

015V003

NÃO

NÃO

Alíquota da COFINS \- em Reais

N

015V004

NÃO

NÃO

Código da Natureza da Receita 

N

003

NÃO

NÃO

Código da SCP

A

014

NÃO

NÃO

Código do Amparo/Texto/Ocorrência

A

010

NÃO

NÃO

 

OS4835

RN02

__Campo 32 – Código de Situação Tributária PIS__:

Campo não obrigatório\. Se preenchido, verificar a existência do código na TACES65 \(\*\), de acordo com a data de validade do documento, da seguinte forma:

\-Indicador do tributo = 1 \(PIS\);

\-Data de Validade = maior data de validade que seja < ou = a data do documento \(campo 06 da SAFX994\);

\-Código da Situação Tributária = código informado no documento;  

Se o código não existir na TACES65, o item não deve ser importado, e deverá ser gerada uma mensagem de erro no log de processo com a seguinte descrição: 

*              “Código da Situação Tributária PIS inexistente ou inválido para a data do documento\.”\. *

\(\*\) A TACES65 é uma nova tabela acessória para carga dos códigos de situação tributária do PIS e da COFINS, que foi criada na OS2388\-D2\.

OS2995\-B\-dw

RN03

__Campo 35 – Código de Situação Tributária COFINS__:

Campo não obrigatório\. Se preenchido, verificar a existência do código na TACES65 \(\*\), de acordo com a data de validade do documento, da seguinte forma:

\-Indicador do tributo = 2 \(COFINS\);

\-Data de Validade = maior data de validade que seja < ou = a data do documento \(campo 06 da SAFX994\);

\-Código da Situação Tributária = código informado no documento;  

Se o código não existir na TACES65, o item não deve ser importado, e deverá ser gerada uma mensagem de erro no log de processo com a seguinte descrição: 

*              “Código da Situação Tributária COFINS inexistente ou inválido para a data do documento\.”\. *

\(\*\) A TACES65 é uma nova tabela acessória para carga dos códigos de situação tributária do PIS e da COFINS, que foi criada na OS2388\-D2\.

OS2995\-B\-dw

RN04

__Campo Código da SCP__

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

OS4316

RN05

__Campo COO \(Contador de Ordem de Operação\)__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

RN06

__Campo Código do Amparo/Texto/Ocorrência __

Campo não obrigatório\.

Se preenchimento, verificar a existência do código no Cadastro do Amparo/Texto/Ocorrência \(TACES21\), de acordo com a data de emissão do cupom e a UF do Estabelecimento\. 

Caso o código não esteja cadastrado, exibir a seguinte mensagem de erro no log do processo:

*               “Codigo do Amparo Legal nao esta cadastrado ou nao existe para data fiscal\.”*

MFS507186

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

