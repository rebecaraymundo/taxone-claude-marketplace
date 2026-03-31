# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX995

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX995.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX995

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3564

Tatiane Lima

Novo código de modelo de Documento Fiscal \- Manifesto Eletrônico de Documentos Fiscais \- MDF\-e\.

OS4835

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho do campo “COO \(Contador de Ordem de Operação\)” de 006 para 009 posições\.

OS4817

Jefferson Mota

O objetivo desta OS é ajustar a tela de Detalhe do Meio de Pagamento, incluíndo novos campos: “Número do Comprovante”, Natureza da Operação” e “Tipo da Operação”\.

MFS10565

Andrea Rocha

Inclusão do novo campo CEP\. Inclusão de novas opções para o campo Tipo da Operação\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX995 – Detalhe Meio de Pagamento, que deve ser criada com a seguinte estrutura:

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

CEP

N

008

NÃO

NÃO

 

OS4835/

OS4817/

MFS10565

RN02

__Campo Modelo Documento__

Aceitar a importação do novo código de modelo “58”\.

OS3564

RN03

__Campo COO \(Contador de Ordem de Operação\)__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

RN13

__Campo 13\- Tipo da Operação:__

Campo de preenchimento obrigatório, deve ser exibida a mensagem de erro padrão caso esse campo não esteja preenchido\. 

Valores válidos: “1” ou “2”  ou “3” ou “4” ou “5’” \(“1” para Operação Eletrônica; “2” para Operação Manual, “3” para POS, “4” para \- E\-commerce, “5” para  Demais Tecnologias\)\.      

 

Quando o contéudo não for válido, o registro não será importado, e no log de erros será gravada uma mensagem informando que:

*“Tipo da Operacao deve ser preenchido com <1> ou <2> ou <3> ou <4> ou <5>\.”*

      

MFS10565

RN14

__Campo 14 \- CEP__

Campo de preenchimento não obrigatório\.

MFS10565

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

