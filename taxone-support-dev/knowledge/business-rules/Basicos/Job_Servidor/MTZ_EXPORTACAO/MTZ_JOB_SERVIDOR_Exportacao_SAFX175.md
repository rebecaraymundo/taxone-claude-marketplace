# MTZ_JOB_SERVIDOR_Exportacao_SAFX175

- **Fonte:** MTZ_JOB_SERVIDOR_Exportacao_SAFX175.docx
- **Modificado:** 2022-04-07
- **Tamanho:** 71 KB

---

THOMSON REUTERS

175

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS1676

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de exportação da SAFX175\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX175 \- Registros de Estorno de Débitos, que deve ser exportada com a seguinte estrutura:

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

Código do Estabelecimento

A

006

SIM

SIM

Período de Declaração da Informação

N

006

SIM

SIM

Nº da NF Objeto do Estorno

A

012

SIM

SIM

Série da NF Objeto do Estorno

A

003

SIM

Subsérie da NF Objeto do Estorno

A

002

SIM

Data de Emissão da NF Objeto do Estorno

D

008

SIM

SIM

Ind\. PFJ da NF Objeto do Estorno

A

001

SIM

SIM

Código PFJ da NF Objeto do Estorno

A

014

SIM

SIM

Nº do Item da NF Objeto do Estorno

N

007

SIM

SIM

Nº da NF de Ressarcimento

A

012

SIM

Série da NF de Ressarcimento

A

003

SIM

Subsérie da NF de Ressarcimento

A

002

SIM

Nº do Item da NF de Ressarcimento

N

007

SIM

Data de Emissão da NF de Ressarcimento

D

008

SIM

Tipo da Informação

A

001

SIM

Modelo do Documento da NF Objeto do Estorno

A

002

SIM

Modelo do Documento da NF de Ressarcimento

A

002

Cód\. Autenticação da NF Objeto do Estorno

A

032

Nº do Terminal Faturado da NF Objeto do Estorno

A

014

Valor Total da NF Objeto do Estorno

N

015V002

BC de ICMS da NF Objeto do Estorno

N

015V002

Valor do ICMS da NF Objeto do Estorno

N

015V002

Ind\. Produto da NF Objeto do Estorno

A

001

SIM

Cód\. Produto da NF Objeto do Estorno

A

035

SIM

Valor Total do Item da NF Objeto do Estorno

N

015V002

BC de ICMS do Item da NF Objeto de Estorno

N

015V002

Valor do ICMS do Item da NF Objeto de Estorno

N

015V002

Motivo do Estorno

A

200

Nº da Reclamação

A

020

ICMS a ser Estornado

N

015V002

Hipótese de Estorno

A

001

Código do Sistema de Origem

A

004

 

MFS1676

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

