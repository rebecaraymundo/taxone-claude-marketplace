# MTZ_JOB_SERVIDOR_Carga_SAFX202

- **Fonte:** MTZ_JOB_SERVIDOR_Carga_SAFX202.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Regras de Carga SAFX202

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4822

Elenilson Coutinho

Inclusão do Campo “Valor da Exclusão da Base de Cálculo PIS/COFINS”

MFS4455

Eric Celestrino

Alteração do tamanho do campo “Valor Unitário”

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX202 – Detalhe Cupom Fiscal Eletrônico, que deve ser criada com a seguinte estrutura:

__\[ALTERADA – MFS4455\]__

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Valor da Exclusão da Base de Cálculo PIS/COFINS

N

015V002

NÃO

NÃO

Valor Unitário

N

015V002 015V004

NÃO

NÃO

 

OS4822

MFS4455

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

