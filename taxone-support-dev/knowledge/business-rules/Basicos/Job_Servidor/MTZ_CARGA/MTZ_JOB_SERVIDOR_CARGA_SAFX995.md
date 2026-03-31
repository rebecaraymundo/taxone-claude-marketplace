# MTZ_JOB_SERVIDOR_CARGA_SAFX995

- **Fonte:** MTZ_JOB_SERVIDOR_CARGA_SAFX995.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 67 KB

---

THOMSON REUTERS

5

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4835

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho do campo “COO \(Contador de Ordem de Operação\)” de 006 para 009 posições\.

OS4817

Jefferson Mota

O objetivo desta OS é ajustar a tela de Detalhe do Meio de Pagamento, incluíndo novos campos: “Número do Comprovante”, Natureza da Operação” e “Tipo da Operação”\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX995 – Detalhe Meio de Pagamento, que deve ser criada com a seguinte estrutura:

__\[ALTERADA – OS4835\]  / \[ALTERADA – OS4817\]__

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

Código do meio de Pagamento

A

002

SIM

SIM

Valor pago

N

015V002

NÃO

NÃO

Indicador de estorno

A

001

NÃO

NÃO

Valor estornado

N

015V002

NÃO

NÃO

Número do Comprovante

A

018

NÃO

NÃO

Natureza da Operação

N

001

SIM

NÃO

Tipo da Operação

N

001

SIM

NÃO

 

OS4835

OS4817

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

