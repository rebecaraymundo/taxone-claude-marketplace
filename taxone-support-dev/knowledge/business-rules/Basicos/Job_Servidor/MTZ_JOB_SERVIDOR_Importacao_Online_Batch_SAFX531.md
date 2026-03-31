# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX531

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX531.docx
- **Modificado:** 2025-05-13
- **Tamanho:** 78 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4514\-A

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX531\.

MFS10590

Elenilson Coutinho

Inclusão do campo “Código Suspensão” e alteração na regra dos campos Tipo do Processo e Número do Processo  na SAFX531\.

MFS\-26562

Alessandra Cristina Navatta

Inclusão do campo “Descrição do processo judicial”

MFS\-35679

Alessandra Cristina Navatta

Se não for encontrado para o estabelecimento e grupo em questão, o cadastro da tabela Processo Administrativo Judicial \(REINF/eSocial\), será exibida a mensagem 90423, da tfix22

Obs\. Esta regra já estava implementada, trata\-se apenas de atualização de requisito

MFS\-79885

Alessandra Cristina Navatta

Inclusão de opção do tipo de rendimento e de campos para atendimento ao evento R\-4010 \- Pagamentos/créditos a beneficiário pessoa física\.

Campos novos \(Campos 23 à 27\)

- Valor da Retenção que Deixou de ser Efetuada – IR;
- Valor do Depósito Judicial – IR; 
- Valor da Compensação Referente ao Ano Calendário – IR; 
- Valor da Compensação Referente a Anos Anteriores – IR;
- Valor do Rendimento Com Exigibilidade Suspensa – IR

Inclusão de validação nos campos \(23 à 27\) – RN10, RN11, RN12

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

Inclusão de validação nos campos \(28 à 37\) –RN10, RN12

MFS\-99558

Alessandra Cristina Navatta

Ajustar as validações, considerando a existência do tributo em pelo menos um dos registros do código de natureza em questão da taces101 \(RN12\)

MFS\-577962

Alessandra Cristina Navatta

Alteração do campo Quantidade de Meses \(ajuste no formato/tamanho do campo\)\. O campo será alterado para permitir 4 inteiros e uma casa decimal\. \(RN01\)

MFS\-805178

Alessandra Cristina Navatta

Para atender a NT 01/2025 do REINF, fizemos os seguintes ajustes:

- Inclusão da opção 3\- Sem Processo, no campo Tipo de Processo \(RN04\)\. 
- Campo Número do Processo, passa a ser não obrigatório \(RN01\)

Alteração de Regra do campo Número do Processo, com relação a obrigatoriedade de preenchimento\. \(RN05\)

- Campo Código Suspensão, inclusão de validação \(RN06\)
- Validação no campo Descrição do Processo Judicial \(RN13\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX531 – Rendimentos de Decisão Judicial, que deve ser criada com a seguinte estrutura:

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

SIMNÃO

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

Descrição do processo judicial

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

RN02

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX53, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando como chave de relacionamento os campos Código da Empresa, Código do Estabelecimento, Data do Movimento, Indicador de Pessoa Física/Jurídica, Código do Fornecedor, Tipo do Documento, Número do Documento, Série do Documento, Subsérie do Documento, Código de Operação e Código do DARF\. Caso não encontre, retornar a mensagem: “SAFX53 correspondente a SAFX531 não localizada”\.

OS4514\-A

RN03

__Campo Tipo de Rendimento__

Deve aceitar na importação apenas os conteúdos <1> – Rendimento Recebido Acumuladamente ou <2> – Demais Rendimentos de Decisão Judicial ou <3> \- Não Retenção de Tributos ou Depósitos Judiciais\. Caso seja informado um conteúdo diferente, retornar mensagem: “Tipo de Rendimento inválido\. Conteúdo do campo deve ser igual a <1> ou <2> ou <3>”\.

__Ocorrência permitida:__

Serão permitidos apenas uma ocorrência para os tipos de rendimento 1 e 2\. Para o tipo de rendimento 3, poderão ter até 50 ocorrências\.

OS4514\-A

MFS\-79885

RN04

__Campo Tipo do Processo__

__\[ALTERAÇÃO MFS\-805178\]__ \- Inclusão de opção para Rendimento Recebido Acumuladamente\.

Se Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente:

Deve aceitar na importação apenas os conteúdos <1> – Administrativo ou <2> – Judicial ou <3> \- Sem Processo\. Caso seja informado um conteúdo diferente, retornar mensagem <<92604>>: “Tipo de Processo inválido\. Conteúdo do campo deve ser igual a <1> ou <2> ou <3>”\.

Se Tipo de Rendimento for igual a 2 – Demais Rendimentos de Decisão Judicial:

Deve aceitar na importação apenas o conteúdo <2> – Judicial\. Caso seja informado um conteúdo diferente, retornar mensagem: “Tipo de Processo inválido\. Conteúdo do campo deve ser igual a <2>”\.

Campo de preenchimento obrigatório\. Quando não informado, retornar a mensagem: “Campo Tipo do Processo deve ser preenchido”\.

Se tipo de processo não preenchido e número processo estiver preenchido exibir a seguinte mensagem: “Tipo de Processo” deve ser preenchido referente ao “Número do Processo” identificado\. 

OS4514\-A

MFS\-10590

MFS\-805178

RN05

__Campo Número do processo__

__\[ALTERAÇÃO MFS\-805178\]__ – Regra de Obrigatoriedade do campo:

Campo de preenchimento exclusivo e obrigatório, quando:

- Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente e tipo de processo igual a  <1> – Administrativo ou <2> – Judicial 
- Tipo de Rendimento for igual a 2 – Demais Rendimentos de Decisão Judicial

Nestas condições, se não informado, retornar a mensagem: “Campo Número do Processo deve ser preenchido”\.

Caso não identificado Número do Processo para o Tipo do Processo no cadastro de processos \(SAFX2058\), exibir a seguinte mensagem: “Número do Processo não cadastrado na tabela de Processos \(SAFX2058\)”\.

Caso Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente e tipo de processo diferente de  <1> – Administrativo ou <2> – Judicial e este campo estiver preenchido, exibir a mensagem <<93775>>: Quando o Tipo de Rendimento for  1 – Rendimento Recebido Acumuladamente e Tipo de Processo igual a 3 – Sem processo, o campo Número do Processo não deve ser preenchido\.

OS4514\-A

MFS\-10590

MFS\-805178

RN06

__Campo Código Suspensão__

Campo de preenchimento exclusivo e obrigatório, quando:

- Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente e tipo de processo igual a  <1> – Administrativo ou <2> – Judicial 
- Tipo de Rendimento for igual a 2 – Demais Rendimentos de Decisão Judicial

Caso não encontrado o código de suspensão no cadastro de suspensão \(SAFX2059\) referente aos processos identificados pelos campos \(“Tipo do Processo” e “Número do Processo”\) exibir a seguinte mensagem: “Código de Suspensão” deve ser preenchido, referente ao “Tipo do Processo” e “Número do Processo” identificado\.

Caso Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente e tipo de processo diferente de  <1> – Administrativo ou <2> – Judicial e este campo estiver preenchido, exibir a mensagem <<93776>>: Quando o Tipo de Rendimento for  1 – Rendimento Recebido Acumuladamente e Tipo de Processo igual a 3 – Sem processo, o campo Código Suspensão  não deve ser preenchido

MFS\-10590

MFS\-805178

RN07

__Campo Indicador da origem dos recursos__

Deve aceitar na importação apenas os conteúdos <1> – Recursos do próprio declarante, <2> – Recursos de terceiros \(Declarante é a Instituição Financeira responsável apenas pelo repasse dos valores\) ou não preenchido\. Caso seja informado um conteúdo diferente, retornar mensagem: “Indicador da origem dos recursos inválido\. Conteúdo do campo deve ser igual a <1>, <2> ou não informado”\.

OS4514\-A

RN08

__Campo CNPJ da empresa de origem dos recursos__

Deverá ser realizada a validação do conteúdo informado\. Caso seja informado um CNPJ inválido, retornar a mensagem: “Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda”\.

OS4514\-A

RN09

__Validação __

Se não for encontrado para o estabelecimento e grupo em questão, o cadastro da tabela Processo Administrativo Judicial \(REINF/eSocial\), será exibida a mensagem 90423, da tfix22\.

Mensagem: Grupo de Relacionamento da Tabela nao identificado para Data Solicitada  

MFS\-35679

RN10

__Validação__

Só deve ser permitido valores nos campos abaixo, quando a opção ‘3 \- Não Retenção de Tributos ou Depósitos Judiciais’, do tipo de rendimento estiver indicada\. Caso a opção não seja ‘3’ e um dos valores abaixo estiver preenchido, exibir a mensagem: “O campo <<nome funcional do campo>> não pode ser preenchido, pois o tipo de rendimento indicado não é igual a ‘3 \- Não Retenção de Tributos ou Depósitos Judiciais’”

Campos novos \(Campos 23 à 27\)

- Valor da Retenção que Deixou de ser Efetuada – IR;
- Valor do Depósito Judicial – IR; 
- Valor da Compensação Referente ao Ano Calendário – IR; 
- Valor da Compensação Referente a Anos Anteriores – IR;
- Valor do Rendimento Com Exigibilidade Suspensa – IR

__\[ALTERAÇÂO MFS\-79890\]__ Inclusão de campos na validação \(Campos 28 à 37\):

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

MFS\-79995

MFS\-79890

RN11

__Validação__

Os campos abaixo, devem ter as seguintes validações:

- Valor da Retenção que Deixou de ser Efetuada \- IR
- Valor do Depósito Judicial \- IR
- Valor da Compensação Referente ao Ano Calendário \- IR
- Valor da Compensação Referente a Anos Anteriores \- IR
- Valor do Rendimento Com Exigibilidade Suspensa \- IR

Validação 1:

Se informados, devem ser maiores que zero, caso contrário, exibir a mensagem: “Quando informado o campo <nome funcional>, este deve ser maior que zero\.”

MFS\-79995

RN12

Validação:

- Ao preencher o campo ‘Valor da Retenção que Deixou de ser Efetuada – IR’, ‘Valor do Depósito Judicial – IR’, ‘Valor da Compensação Referente ao Ano Calendário – IR’, ‘Valor da Compensação Referente a Anos Anteriores – IR’, ‘Valor do Rendimento Com Exigibilidade Suspensa – IR’ ou ‘Valor da Base com Exigibilidade Suspensa – IR’ e se a natureza de rendimento \(registro da taces101\) estiver preenchida, verificar se este código de natureza de rendimento possui ‘IR’ na coluna tributo em pelo menos um dos registros da taces101\. Caso não tenha, exibir a mensagem: “Este campo não pode ser preenchido, pois, a natureza de rendimento indicada, não permite o tributo IR\.”
- Ao preencher o campo ‘Valor da Base com Exigibilidade Suspensa – CSLL’, ‘Valor da Retenção que Deixou de ser Efetuada – CSLL’ ou ‘Valor do Depósito Judicial – CSLL’, e se a natureza de rendimento \(registro da taces101\) estiver preenchida, verificar se este código de natureza de rendimento possui ‘CSLL’ na coluna tributo em pelo menos um dos registros da taces101\. Caso não tenha, exibir a mensagem: “Este campo não pode ser preenchido, pois, a natureza de rendimento indicada, não permite o tributo CSLL\.”
- Ao preencher o campo ‘Valor da base com Exigibilidade Suspensa – COFINS’, ‘Valor da Retenção que Deixou de ser Efetuada – COFINS’, ou ‘Valor do Depósito Judicial – COFINS’, e se a natureza de rendimento \(registro da taces101\) estiver preenchida, verificar se este código de natureza de rendimento possui ‘COFINS’ na coluna tributo em pelo menos um dos registros da taces101\. Caso não tenha, exibir a mensagem: “Este campo não pode ser preenchido, pois, a natureza de rendimento indicada, não permite o tributo COFINS\.”
- Ao preencher o campo ‘Valor da base com Exigibilidade Suspensa \- PIS/PASEP’, ‘Valor da Retenção que Deixou de ser Efetuada \- PIS/PASEP, ‘Valor do Depósito Judicial \- PIS/PASEP’ e se a natureza de rendimento \(registro da taces101\) estiver preenchida, verificar se este código de natureza de rendimento possui ‘PP’ na coluna tributo em pelo menos um dos registros da taces101\. Caso não tenha, exibir a mensagem: “Este campo não pode ser preenchido, pois, a natureza de rendimento indicada, não permite o tributo PIS/PASEP\.”

MFS\-79995

MFS\-79890

MFS\-99558

RN13

__Descrição do Processo Judicial__

Se o Tipo de Processo = 3 – Sem Processo, não deve ser preenchido o campo\. Neste caso, exibir a mensagem <<93777>>: “Descrição do Processo Judicial, não deve ser informada, quando Tipo de Processo = 3 – Sem Processo\.”

MFS\-805178

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

