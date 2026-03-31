# MTZ_JOB_SERVIDOR_Exportacao_SAFX203

- **Fonte:** MTZ_JOB_SERVIDOR_Exportacao_SAFX203.docx
- **Modificado:** 2021-05-21
- **Tamanho:** 64 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3810\-G

Marcos G\. de Paula

Definição das regras de exportação da SAFX203\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX203 \- Lançamentos de Ajuste EFD\-Contribuições Financeiras, que deve ser exportada com a seguinte estrutura:

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

Data da Operação

N

008

SIM

SIM

Código da Situação Tributária PIS

N

002

SIM

SIM

Valor da Alíquota PIS

N

003V004

NÃO

NÃO

Código da Situação Tributária COFINS

N

002

SIM

SIM

Valor da Alíquota COFINS

N

003V004

NÃO

NÃO

Código da Receita/ Dedução/ Exclusão

A

005

SIM

SIM

Código do Atributo da Receita/ Dedução/ Exclusão

A

003

NÃO

SIM

Código do Complemento da Receita/ Dedução/ Exclusão

A

020

SIM

SIM

Código Natureza Receita

N

003

NÃO

SIM

Código da Conta Contábil

A

070

NÃO

SIM

Valor do Ajuste

N

015V002

NÃO

NÃO

Tipo do Ajuste

A

001

NÃO

NÃO

 

OS3810\-G

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

