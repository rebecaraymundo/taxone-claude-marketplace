# MTZ_JOB_SERVIDOR_CARGA_SAFX2009

- **Fonte:** MTZ_JOB_SERVIDOR_CARGA_SAFX2009.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Regras de Carga SAFX2009

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4806

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de Carga da SAFX2009\.

CH6909\_2016

Julyana Perrucini

Alteração do nome do campo “Observação Lei 5005” para acrescentar a Portaria 228/15\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2009 \- Cadastro de Observações \- Ato Cotepe/ICMS 35/05, que deve ser criada com a seguinte estrutura:

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

001

NÃO

NÃO

Observação Lei 5005/ Port\. 228/15

A

025

NÃO

NÃO

 

OS4806

CH6929\_2016

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

