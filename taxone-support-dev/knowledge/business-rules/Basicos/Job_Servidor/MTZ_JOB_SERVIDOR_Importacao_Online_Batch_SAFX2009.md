# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2009

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2009.docx
- **Modificado:** 2021-08-23
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX2009

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4806

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX2009\.

CH6909\_2016

Julyana Perrucini

Alteração do nome do campo “Observação Lei 5005” para acrescentar a Portaria 228/15\.

MFS58212

Andréa Rocha

Alteração da regra do campo “Tipo de Observação”

MFS68496

Liliane Assaf

Inclusão do campo CFOP Portaria CAT 66/2018 – SP \(RN06\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2009 \- Cadastro de Observações \- Ato Cotepe/ICMS 35/05, que deve ser criada com a seguinte estrutura:

__\[ALTERADA – OS4806/ CH6909\_2016\]__

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Observação

A

008

NÃO

NÃO

Data Início/Inclusão/Alteração

N

008

NÃO

NÃO

Descrição da Observação

A

500

NÃO

NÃO

Tipo de Observação

N

001

NÃO

NÃO

Observação Lei 5005/ Port\. 228/15

A

025

NÃO

NÃO

CFOP Portaria CAT 66/2018 – SP

A

004

NÃO

NÃO

 

OS4806

CH6929\_2016

MFS68496

RN04

__Campo Tipo de Observação__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

Quando preenchido, <a id="OLE_LINK43"></a><a id="OLE_LINK44"></a><a id="OLE_LINK45"></a>deve ser = <a id="OLE_LINK47"></a><a id="OLE_LINK48"></a><a id="OLE_LINK49"></a>“1” ou “9”\. <a id="OLE_LINK50"></a>Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “Tipo de Observação inválido\. Favor informar 1 ou 9”

__Obs\.:__ O campo Tipo de Observação já existia na tabela mas não estava sendo utilizado\.

MFS58212

RN05

__Campo Observação Lei 5005/ Port\. 228/15__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

OS4806

CH6929\_2016

RN06

__Campo CFOP Portaria CAT 66/2018 – SP__

Campo de preenchimento não obrigatório\.

Caso seja preenchido, deve ser verificado se o código está cadastrado na Tabela de Códigos Fiscais \(SAFX2012\)\. Caso não esteja cadastrado, mensagem deve ser gerada:

90029 \- CFOP \- Codigo Fiscal de Operacao e Prestacao nao cadastrado\.

MFS68496

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

