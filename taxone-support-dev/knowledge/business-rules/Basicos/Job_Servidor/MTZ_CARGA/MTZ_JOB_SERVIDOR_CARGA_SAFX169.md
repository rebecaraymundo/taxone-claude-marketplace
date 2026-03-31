# MTZ_JOB_SERVIDOR_CARGA_SAFX169

- **Fonte:** MTZ_JOB_SERVIDOR_CARGA_SAFX169.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 63 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4711

Elenilson Coutinho

Definição das regras de carga da SAFX169\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX169 – Saldo Antes do Encerramento, que deve ser criada com a seguinte estrutura:

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

Código da Conta Analítica de Resultado

A

070

SIM

SIM

Código do Centro de Custo

A

020

NÃO

SIM

Data Saldo

N

008

SIM

SIM

Indicador da situação do saldo final: 

D \- Devedor; 

C \- Credor\.

A

001

SIM

NÂO

Valor do saldo final antes do lançamento de encerramento

N

015V002

SIM

NÃO

 

OS4711

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

