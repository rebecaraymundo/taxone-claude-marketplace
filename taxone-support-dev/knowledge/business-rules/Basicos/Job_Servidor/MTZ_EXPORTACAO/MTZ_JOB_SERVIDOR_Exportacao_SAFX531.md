# MTZ_JOB_SERVIDOR_Exportacao_SAFX531

- **Fonte:** MTZ_JOB_SERVIDOR_Exportacao_SAFX531.docx
- **Modificado:** 2025-05-13
- **Tamanho:** 68 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4514\-A

Marcos G\. de Paula

Definição das regras de exportação da SAFX531\.

MFS10590

Elenilson Coutinho

Inclusão do campo “Código Suspensão” e alteração na regra dos campos Tipo do Processo e Número do Processo  na SAFX531\.

MFS\-26562

Alessandra Cristina Navatta

Inclusão do campo “Descrição”

MFS\-79885

Alessandra Cristina Navatta

Inclusão de opção do tipo de rendimento e de campos para atendimento ao evento R\-4010 \- Pagamentos/créditos a beneficiário pessoa física\.

Campos novos \(Campos 23 à 27\)

- Valor da Retenção que Deixou de ser Efetuada – IR;
- Valor do Depósito Judicial – IR; 
- Valor da Compensação Referente ao Ano Calendário – IR; 
- Valor da Compensação Referente a Anos Anteriores – IR;
- Valor do Rendimento Com Exigibilidade Suspensa \- IR

MFS\-79890

Alessandra Cristina Navatta

Inclusão de campos para atendimento ao evento R\-4020 \- Pagamentos/créditos a beneficiário pessoa jurídica\.

Campos novos \(Campos 28 à 37\)

- Valor da Base com Exigibilidade Suspensa – IR; 
- Valor da Base com Exigibilidade Suspensa – CSLL; 
- Valor da Retenção que Deixou de ser Efetuada – CSLL;
- Valor do Depósito Judicial – CSLL; 
- Valor da base com Exigibilidade Suspensa – COFINS;
- Valor da Retenção que Deixou de ser Efetuada – COFINS; 
- Valor do Depósito Judicial – COFINS;
- Valor da base com Exigibilidade Suspensa \- PIS/PASEP;
- Valor da Retenção que Deixou de ser Efetuada \- PIS/PASEP;
- Valor do Depósito Judicial \- PIS/PASEP

MFS\-99558

Alessandra Cristina Navatta

Ajustar as validações, considerando a existência do tributo em pelo menos um registro do código de natureza da taces101 \(regra documentada/detalhada na matriz de importação\)

MFS\-577962

Alessandra Cristina Navatta

Alteração do campo Quantidade de Meses \(ajuste no formato/tamanho do campo\)\. O campo será alterado para permitir 4 inteiros e uma casa decimal\. \(RN01\)

MFS\-805178

Alessandra Cristina Navatta

Para atender a NT 01/2025 do REINF, fizemos os seguintes ajustes:

- Campo Número do Processo, passa a ser não obrigatório \(RN01\)
- \*Inclusão da opção 3 – Sem Processo, no campo Tipo de Processo \(RN04\)\. 
- \*Alteração de Regra do campo Número do Processo, com relação a obrigatoriedade de preenchimento\. \(RN05\)
- Campo Código Suspensão, inclusão de validação \(RN06\)
- \*Campo Descrição do Processo Judicial, inclusão de validação \(RN13\)

\(\*\) Não houve impacto neste documento \(regra documentada/detalhada na matriz de importação\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX531 \- Rendimentos de Decisão Judicial, que deve ser criada com a seguinte estrutura:

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

SIM

SIM

Número do processo

A

020

SIM NÃO

SIM

Código Suspensão

A

014

NÃO

SIM

Despesa com Custas Judiciais

N

015V002

NÃO

NÃO

Despesa com Advogado\(s\)

N

015V002

NÃO

NÃO

Natureza do rendimento

A

050

NÃO

NÃO

Quantidade de meses

N

004V001

NÃO

NÃO

Indicador da origem dos recursos

A

001

NÃO

NÃO

CNPJ da empresa de origem dos recursos

A

014

NÃO

NÃO

Descrição do Processo Judicial 

A

050

NÃO

NÃO

Valor da Retenção que Deixou de ser Efetuada \- IR

015V002

N

NÃO

NÃO

Valor do Depósito Judicial \- IR

015V002

N

NÃO

NÃO

Valor da Compensação Referente ao Ano Calendário \- IR

015V002

N

NÃO

NÃO

Valor da Compensação Referente a Anos Anteriores \- IR

015V002

N

NÃO

NÃO

Valor do Rendimento Com Exigibilidade Suspensa \- IR

015V002

N

NÃO

NÃO

Valor da base com Exigibilidade Suspensa \- IR 

015V002

N

NÃO

NÃO

Valor da base com Exigibilidade Suspensa \- CSLL

015V002

N

NÃO

NÃO

Valor da Retenção que Deixou de ser Efetuada \- CSLL

015V002

N

NÃO

NÃO

Valor do Depósito Judicial \- CSLL

015V002

N

NÃO

NÃO

Valor da base com Exigibilidade Suspensa \- COFINS

015V002

N

NÃO

NÃO

Valor da Retenção que Deixou de ser Efetuada \- COFINS

015V002

N

NÃO

NÃO

Valor do Depósito Judicial \- COFINS

015V002

N

NÃO

NÃO

Valor da base com Exigibilidade Suspensa \- PIS/PASEP

015V002

N

NÃO

NÃO

Valor da Retenção que Deixou de ser Efetuada \- PIS/PASEP

015V002

N

NÃO

NÃO

Valor do Depósito Judicial \- PIS/PASEP

015V002

N

NÃO

NÃO

 

OS4514\-A

MFS\-10590

MFS\-26562

MFS\-79885

MFS\-79890

MFS\-577962

MFS\-805178

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

