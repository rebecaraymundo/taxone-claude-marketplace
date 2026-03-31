# MTZ-Job_Servidor-Carga_da_SAFX157

- **Fonte:** MTZ-Job_Servidor-Carga_da_SAFX157.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 43 KB

---

# <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK5"></a>Módulo Job Servidor –  Garga SAFX157

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS4657

Criação da SAFX157

Será criada uma tabela para atendimento do Registro 50 – Nota Carioca\.

    26/11/2014

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

<a id="_Hlk407355282"></a>__RN01__

__Campo 01 – Código da Empresa__

 

__Item: __01

__Nome do Campo:__ Verificar com o A&D__ __

__Descrição: __Código da Empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.\.

__Chave Primária__

__Obrigatório__

OS4657

__RN02__

__Campo 02 – Código do Estebelecimento__

 

__Item: __02

__Nome do Campo:__ Verificar com o A&D__ __

__Descrição: __Código do Estebelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__Chave Primária__

__Obrigatório__

OS4657

__RN03__

__Campo 03 – Data Emissão__

__Item: __11

__Nome do Campo: __Verificar com o A&D

__Descrição: __Data de emissão das notas de materiais\.

__Tipo:__ A

__Tamanho: __008

__Comentário: __Campo destinado a data de emissão das notas de materiais\.

__Chave Primária__

__Obrigatório__

OS4657

__RN04__

__Campo 04 – Movimento Entrada/Saída__

 

__Item: __03

__Nome do Campo:__ Verificar com o A&D__ __

__Descrição: __Movimento Entrada/Saída

__Tipo:__ A

__Tamanho: __001

__Comentário: __Campo destinado ao tipo de movimento de entreda e saída\.

__Chave Primária__

__Obrigatório__

OS4657

__RN05__

__Campo 05 – Normal ou Devolução__

 

__Item: __04

__Nome do Campo:__ Verificar com o A&D__ __

__Descrição: __Normal ou Devolução

__Tipo:__ A

__Tamanho: __001

__Comentário: __Qualifica o motivo da Entrada e Saída da Nota Fiscal\.

__Chave Primária__

__Obrigatório__

OS4657

__RN06__

__Campo 06 – Tipo do Documento__

 

__Item: __05

__Nome do Campo:__ Verificar com o A&D__ __

__Descrição: __Tipo do Documento

__Tipo:__ A

__Tamanho: __005

__Comentário: __Tipo de Documento de acordo com a Tabela de Tipo de Documentos  \(SAFX2005\)\.

__Chave Primária__

__Obrigatório__

OS4657

__RN07__

__Campo 07 – Indicador Pessoa Física/Jurídica__

 

__Item: __06

__Nome do Campo:__ Verificar com o A&D__ __

__Descrição: __Indicador Pessoa Física/Jurídica

__Tipo:__ A

__Tamanho: __001

__Comentário: __Campo que deverá ser preenchido com o Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\)\.

__Chave Primária__

__Obrigatório__

OS4657

__RN08__

__Campo 08 – Código/Destinatário/Emitente/ Remetente__

 

__Item: __07

__Nome do Campo:__ Verificar com o A&D__ __

__Descrição: __Código/Destinatário/Emitente/ Remetente

__Tipo:__ A

__Tamanho: __014

__Comentário: __Deve estar registrado na Tabela de Pessoa Física/Jurídica \(SAFX04\)\.

__Chave Primária__

__Obrigatório__

OS4657

__RN09__

__Campo 09 – Número da Nota__

 

__Item: __08

__Nome do Campo:__ Verificar com o A&D__ __

__Descrição: __Número da Nota de Materias/Remessa

__Tipo:__ N

__Tamanho: __012

__Comentário: __Campo destinado ao Número da Nota de Materias/Remessa\.

__Chave Primária__

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a>__Obrigatório__

OS4657

__RN10__

__Campo 10 – Série Doc\. Fiscal__

__Item:__ 09

__Nome do Campo: __Verificar com o A&D

__Descrição: __Série do documento fiscal

__Tipo:__ A

__Tamanho: __003

__Conteúdo do Campo: __Informar a Série do documento fiscal

__Chave Primária__

__Obrigatório__

OS4657

__RN11__

__Campo 11 – Subsérie do Documento Fiscal__

__Item:__ 10

__Nome do Campo: __Verificar com o A&D

__Descrição: __Subsérie do Documento Fiscal

__Tipo:__ A

__Tamanho: __002

__Conteúdo do Campo: __Campo destinado a subsérie do documento fiscal\.

__Chave Primária__

__Obrigatório__

OS4657

__RN12__

__Campo 12 – Espécie__

__Item: __13

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Tipo de espécie da nota fiscal

__Tipo:__ N

__Tamanho: __003

__Conteúdo do Campo: __Informar a Espécie do documento fiscal

__Obrigatório__

OS4657

__RN13__

__Campo 13 \- Código da Obra Origem__

__Item: __14

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código da Obra de Origem\.

__Tipo:__ A

__Tamanho: __015

__Conteúdo do Campo: __Informar o Código da Obra de Origem\.

OS4657

__RN14__

__Campo 14 \- Código da Obra Destino__

__Item: __15

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código da Obra de Destino\.

__Tipo:__ A

__Tamanho: __015

__Conteúdo do Campo: __Informar o Código da Obra de Destino\.

OS4657

__RN15__

__Campo 15 – Valor Uso e Consumo__

__Item: __17

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Valor do material destinado para uso e consumo na obra ou estoque

__Tipo:__ N

__Tamanho: __015

__Conteúdo do Campo: __Informar o valor do material destinado para uso e consumo na obra ou estoque\.

__Obrigatório__

__ __

OS4657

__RN16__

__Campo 16 – Valor Incorporado__

__Item: __16

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Valor do material a ser incorporado na obra ou estoque\.

__Tipo:__ N

__Tamanho: __015

__Conteúdo do Campo: __Informar o valor do material a ser incorporado na obra ou estoque\.

__Obrigatório__

OS4657

