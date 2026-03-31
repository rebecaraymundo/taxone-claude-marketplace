# MTZ-Carga_SAFX48

- **Fonte:** MTZ-Carga_SAFX48.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 61 KB

---

THOMSON REUTERS

Regras de Carga SAFX48

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4819

Jefferson Mota

Criação de indicadores na SAFX48 para categorizar a despesa como nacional e internacional\.

CH20050\_2015

Julyana Perrucini

Alteração da obrigatoriedade dos campos Despesas de Fretes, Seguros, Despesas Acrescidas, Comissões, Despesas de Armazenagem e Despesas de Royalties\.

MFS\-6443

Liliane Assaf

Inclusão do campo CFO na SAFX48\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple a inclusão dos campos na tabela SAFX48 – Operação de Exportação, que devem ser incluídos com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Classificação do Seguro

A

001

NÃO

NAO

Classificação do Frete

A

001

NÃO

NAO

Classificação das Desp\. Acrescidas

A

001

NÃO

NAO

Classificação das Desp\. Comissões

A

001

NÃO

NAO

Classificação das Desp\. Armazenagem

A

001

NÃO

NAO

Classificação das Desp\. Royalties

A

001

NÃO

NAO

Código Fiscal

A

004

NÃO

NÃO

 

OS4819

CH20050\_2015

MFS\-6443

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

