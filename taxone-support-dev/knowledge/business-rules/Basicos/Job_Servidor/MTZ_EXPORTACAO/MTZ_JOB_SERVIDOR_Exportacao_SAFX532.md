# MTZ_JOB_SERVIDOR_Exportacao_SAFX532

- **Fonte:** MTZ_JOB_SERVIDOR_Exportacao_SAFX532.docx
- **Modificado:** 2025-05-12
- **Tamanho:** 65 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4514\-A

Marcos G\. de Paula

Definição das regras de exportação da SAFX532\.

MFS10590

Elenilson Coutinho

Inclusão do campo “Código Suspensão” e alteração na regra dos campos Tipo do Processo e Número do Processo na SAFX532\.

MFS\-805178

Alessandra Cristina Navatta

Para atender a NT 01/2025 do REINF, fizemos os seguintes ajustes:

- Campo Número do Processo, passa a ser não obrigatório \(RN01\)
- \*Inclusão da opção 3 – Sem Processo, no campo Tipo de Processo \(RN04\)\. 
- \*Alteração de Regra do campo Número do Processo, com relação a obrigatoriedade de preenchimento\. \(RN05\)
- \*Campo Código Suspensão, inclusão de validação \(RN06\)

\(\*\) Não houve impacto neste documento \(regra documentada/detalhada na matriz de importação\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX532 – Identificação do Advogado, que deve ser criada com a seguinte estrutura:

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

Data do Movimento

N

008

SIM

SIM

Indicador de Pessoa Física/Jurídica

A

001

SIM

SIM

Código do Fornecedor

A

014

SIM

SIM

Tipo do Documento

A

005

SIM

SIM

Número do Documento

A

012

SIM

SIM

Série do Documento

A

003

NÃO

SIM

Subsérie do Documento

A

002

NÃO

SIM

Código de Operação

A

006

SIM

SIM

Código do DARF

A

004

SIM

SIM

Tipo de Rendimento

A

001

SIM

SIM

Tipo do Processo

A

001

SIM NÃO

SIM

Número do processo

A

020

SIM

SIM

Código Suspensão

A

014

NÃO

SIM

CNPJ/CPF do Advogado

A

014

SIM

SIM

Despesa com o Advogado

N

015V002

NÃO

NÃO

 

OS4514\-A

MFS\-10590

MFS\-805178

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

