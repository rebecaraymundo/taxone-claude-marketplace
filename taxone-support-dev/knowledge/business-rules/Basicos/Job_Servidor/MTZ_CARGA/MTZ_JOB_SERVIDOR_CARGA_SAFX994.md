# MTZ_JOB_SERVIDOR_CARGA_SAFX994

- **Fonte:** MTZ_JOB_SERVIDOR_CARGA_SAFX994.docx
- **Modificado:** 2023-01-19
- **Tamanho:** 67 KB

---

THOMSON REUTERS

4

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4835

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho do campo “COO \(Contador de Ordem de Operação\)” de 006 para 009 posições\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX994 – Detalhe do Cupom Fiscal, que deve ser criada com a seguinte estrutura:

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

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

