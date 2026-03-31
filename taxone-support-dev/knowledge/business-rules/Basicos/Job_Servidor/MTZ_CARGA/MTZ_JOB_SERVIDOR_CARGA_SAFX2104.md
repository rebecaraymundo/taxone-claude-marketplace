# MTZ_JOB_SERVIDOR_CARGA_SAFX2104

- **Fonte:** MTZ_JOB_SERVIDOR_CARGA_SAFX2104.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3835\-C1

Marcos G\. de Paula

Definição das regras de carga da SAFX2104\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2104 \- Lançamento Contábil X Histórico do Fato Contábil, que deve ser criada com a seguinte estrutura:

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

Código de Aglutinação

A

070

SIM

SIM

Indicador de Utilização do Código de Aglutinação

A

001

SIM

SIM

Conta Débito/Crédito do Lançamento

A

070

SIM

SIM

Data da Operação

N

008

SIM

SIM

Débito/Crédito do Lançamento Contábil

A

001

SIM

SIM

Arquivamento

A

050

SIM

SIM

Código do Histórico do Fato Contábil

A

006

SIM

SIM

 

OS3835\-C1

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

