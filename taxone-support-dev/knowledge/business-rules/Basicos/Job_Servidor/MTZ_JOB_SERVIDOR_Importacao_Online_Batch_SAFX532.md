# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX532

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX532.docx
- **Modificado:** 2025-05-12
- **Tamanho:** 68 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4514\-A

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX532\.

MFS10590

Elenilson Coutinho

Inclusão do campo “Código Suspensão” e alteração na regra dos campos Tipo do Processo e Número do Processo na SAFX532\.

MFS\-805178

Alessandra Cristina Navatta

Para atender a NT 01/2025 do REINF, fizemos os seguintes ajustes:

- Inclusão da opção 3\- Sem Processo, no campo Tipo de Processo \(RN04\)\. 
- Campo Número do Processo, passa a ser não obrigatório \(RN01\)

Alteração de Regra do campo Número do Processo, com relação a obrigatoriedade de preenchimento\. \(RN05\)

- Campo Código Suspensão, inclusão de validação \(RN06\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX532 – Identificação do Advogado, que deve ser criada com a seguinte estrutura:

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

SIMNão

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

RN02

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX531, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando como chave de relacionamento os campos Código da Empresa, Código do Estabelecimento, Data do Movimento, Indicador de Pessoa Física/Jurídica, Código do Fornecedor, Tipo do Documento, Número do Documento, Série do Documento, Subsérie do Documento, Código de Operação, Código do DARF, Tipo de Rendimento, Tipo do Processo, Número do Processo e Código Suspensão\. Caso não encontre, retornar a mensagem: “SAFX531 correspondente a SAFX532 não localizada”\.

__Exclusão de Registros__

Ao excluir o registro, todos os registros filhos serão excluídos também\. 

OS4514\-A

MFS\-10590

RN03

__Campo CNPJ/CPF do Advogado__

Campo de preenchimento obrigatório\. Quando não informado, retornar a mensagem: “CNPJ/CPF do Advogado não informado”\.

Deverá ser realizada a validação do conteúdo informado\. Caso seja informado um CNPJ/CPF inválido, retornar a mensagem: “Numero de CPF informado nao e valido, conforme regras da Receita Federal”\.

OS4514\-A

RN04

__Campo Tipo do Processo __

__\[ALTERAÇÃO MFS\-805178\]__ \- Inclusão de opção para Rendimento Recebido Acumuladamente\.

Se Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente:

Deve aceitar na importação apenas os conteúdos <1> – Administrativo ou <2> – Judicial ou <3> \- Sem Processo\. Caso seja informado um conteúdo diferente, retornar mensagem <<92604>>: “Tipo de Processo inválido\. Conteúdo do campo deve ser igual a <1> ou <2> ou <3>”\.

Se Tipo de Rendimento for igual a 2 – Demais Rendimentos de Decisão Judicial:

Deve aceitar na importação apenas o conteúdo <2> – Judicial\. Caso seja informado um conteúdo diferente, retornar mensagem: “Tipo de Processo inválido\. Conteúdo do campo deve ser igual a <2>”\.

Campo de preenchimento obrigatório\. Quando não informado, retornar a mensagem: “Campo Tipo do Processo deve ser preenchido”\.

Se tipo de processo não preenchido e número processo estiver preenchido exibir a seguinte mensagem: “Tipo de Processo” deve ser preenchido referente ao “Número do Processo” identificado\. 

MFS\-10590

MFS\-805178

RN05

__Campo Número do Processo__

__\[ALTERAÇÃO MFS\-805178\]__ – Regra de Obrigatoriedade do campo:

Campo de preenchimento exclusivo e obrigatório, quando:

- Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente e tipo de processo igual a  <1> – Administrativo ou <2> – Judicial 
- Tipo de Rendimento for igual a 2 – Demais Rendimentos de Decisão Judicial

Nestas condições, se não informado, retornar a mensagem: “Campo Número do Processo deve ser preenchido”\.

Caso não identificado Número do Processo para o Tipo do Processo no cadastro de processos \(SAFX2058\), exibir a seguinte mensagem: “Número do Processo não cadastrado na tabela de Processos \(SAFX2058\)”\.

Caso Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente e tipo de processo diferente de  <1> – Administrativo ou <2> – Judicial e este campo estiver preenchido, exibir a mensagem <<93775>>: Quando o Tipo de Rendimento for  1 – Rendimento Recebido Acumuladamente e Tipo de Processo igual a 3 – Sem processo, o campo Número do Processo não deve ser preenchido\.

MFS\-10590

MFS\-805178

RN06

__Campo Código Suspensão__

Campo de preenchimento exclusivo e obrigatório, quando:

- Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente e tipo de processo igual a  <1> – Administrativo ou <2> – Judicial 
- Tipo de Rendimento for igual a 2 – Demais Rendimentos de Decisão Judicial

Caso não encontrado o código de suspensão no cadastro de suspensão \(SAFX2059\) referente aos processos identificados pelos campos \(“Tipo do Processo” e “Número do Processo”\) exibir a seguinte mensagem: “Código de Suspensão” deve ser preenchido, referente ao “Tipo do Processo” e “Número do Processo” identificado\.

Caso Tipo de Rendimento for igual a 1 – Rendimento Recebido Acumuladamente e tipo de processo diferente de  <1> – Administrativo ou <2> – Judicial e este campo estiver preenchido, exibir a mensagem <<93776>>: Quando o Tipo de Rendimento for 1 – Rendimento Recebido Acumuladamente e Tipo de Processo igual a 3 – Sem processo, o campo Código Suspensão não deve ser preenchido\.

MFS\-10590

MFS\-805178

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

