# MTZ_JOB_SERVIDOR_CARGA_SAFX188

- **Fonte:** MTZ_JOB_SERVIDOR_CARGA_SAFX188.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 63 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3835\-C1

Marcos G\. de Paula

Definição das regras de carga da SAFX188\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX188 \- Transferência de Saldos de Plano de Contas Anterior, que deve ser criada com a seguinte estrutura:

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

Conta Débito/Crédito do Lançamento do Plano de Contas Anterior

A

070

SIM

SIM

Centro de Custo do Plano de Contas Anterior

A

020

NÃO

SIM

Valor do Saldo Inicial do Período

N

015V002

NÃO

NÃO

Débito/Crédito do Lançamento Contábil

A

001

SIM

NÃO

 

OS3835\-C

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

