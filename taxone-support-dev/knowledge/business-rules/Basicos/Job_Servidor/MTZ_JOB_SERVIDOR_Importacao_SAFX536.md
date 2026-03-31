# MTZ_JOB_SERVIDOR_Importacao_SAFX536

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX536.docx
- **Modificado:** 2022-10-10
- **Tamanho:** 67 KB

---

THOMSON REUTERS

 JOB SERVIDOR – CARGA E IMPORTAÇÃO \- SAFX536

##### DOCUMENTO DE REQUISITO

__*MFS*__

__Nome__

__Descrição__

MFS\-79885

Alessandra Cristina Navatta

Definição das regras de Carga, importação \(Online e Batch\) e Exportação da SAFX536\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo Job Servidor deverão ser alteradas para contemplar os campos listados abaixo na tabela SAFX536:

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

CPF do Dependente

A

011

SIM

SIM

Valor da dedução relativa a dependentes ou a pensão alimentícia

N

015V002

SIM

NÃO

 

MFS\-79885

RN02

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX53, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando as mesmas informações dos campos chave da tabela de origem\. Caso não encontre, retornar a mensagem: “SAFX53 correspondente a SAFX536 não localizada”\.

__Ocorrência permitida:__

Serão permitidos até 99 ocorrências\.

MFS\-79885

RN03

__Campo CPF do Dependente__

O dependente deve estar previamente cadastrado na Tabela de Dependentes sem Vínculo \(SAFX275\) e vigente no período da data do movimento\. Caso contrário, exibir a mensagem: O Dependente não está cadastrado na Tabela de Dependentes sem Vínculo, ou o cadastro não está vigente no período da data do movimento \(Localização: Data Warehouse >> Manutenção >> Cadastros >>Pessoas Físicas/Jurídicas>> Tela Dependentes sem Vínculo\)

MFS\-79885

RN04

__Campo Valor da Dedução Relativa a Dependentes ou a Pensão Alimentícia __

Quando informado, o valor deve ser maior que zero\. Caso contrário, exibir a mensagem: “O Valor da Dedução Relativa a Dependentes ou a Pensão Alimentícia, quando informado deve ser maior que zero” 

MFS\-79885

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

