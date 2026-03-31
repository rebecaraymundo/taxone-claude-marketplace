# MTZ_JOB_SERVIDOR_Exportacao_SAFX221

- **Fonte:** MTZ_JOB_SERVIDOR_Exportacao_SAFX221.docx
- **Modificado:** 2022-04-07
- **Tamanho:** 63 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4710

Julyana Perrucini

Definição das regras de exportação da SAFX221\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX221 \- Tabela de Sociedade Uniprofissional, que deve ser exportada com a seguinte estrutura:

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

Período

N

006

SIM

SIM

Valor mensal das receitas auferidas pela sociedade

N

015V002

SIM

NÃO

Quantidade de profissionais habilitados

N

006

SIM

NÃO

Valor do ISS a recolher

N

015V002

NÃO

NÃO

 

OS4710

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

