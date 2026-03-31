# MTZ-Job-Servidor-Importacao-SAFX310

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX310.docx
- **Modificado:** 2020-08-23
- **Tamanho:** 81 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX310

Tabela dos Processos / Documentos de Arrecadação vinculados ao Débito Especial da Apuração do ICMS / ICMS\-ST

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS40160

Criação da SAFX310

Criação da SAFX310 para a importação dos Processos/Documentos de Arrecadação vinculados ao débitos especiais 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

A tabela SAFX310 foi criada pela MFS40160 com objetivo de carregar os dados dos Processos/Documentos de Arrecadação vinculados aos Débitos Especiais da apuração do ICMS ou ICMS\-ST \(aba “Débitos Especiais”\) do Módulo ICMS\.

Tabelas envolvidas na importação do débito especial, e dos Processos/Doc\. Arrecadação e Documentos Fiscais vinculados :

SAFX309 – Débitos Especiais

ICT\_DEBITO\_ESP                     \(se apuração do ICMS\)

ICT\_DEBITO\_ESP\_ST               \(se apuração do ICMS\-ST\)

SAFX310 – Processos / DA Vinculados 

ICT\_DEBITO\_ESP\_PROC          \(se apuração do ICMS\)

ICT\_DEBITO\_ESP\_ST\_PROC   \(se apuração do ICMS\-ST\)

SAFX311 \- Documentos Fiscais Vinculados 

ICT\_DEBITO\_ESP\_AJ               \(se apuração do ICMS\)

ICT\_DEBITO\_ESP\_ST\_AJ        \(se apuração do ICMS\-ST\)

Este documento descreve *apenas* as regras da importação da __SAFX310__\. Para consultar as regras das demais tabelas, ver os documentos específicos de cada SAFX\.  

Estrutura da tabela __SAFX310__ 🡪 vide manual de layout

Campos que compõe a chave da tabela:

Código da Empresa 

        Campos chave do Débito Especial 

                  \(tabela “mãe” SAFX309\)

Código do Estabelecimento

Obrigação Fiscal

Data da Apuração 

Indicador da Apuração

UF

Número Discriminação 

Sequencial 

Sequencial do Processo / DA vinculado 

A __SAFX310__ é utilizada para importação dos Processos/Documentos de Arrecadação vinculados ao débito especial, tanto da apuração do ICMS, como do ICMS\-ST\. Por isso, possui os campos “*Indicador da Apuração*” e “*UF*”\. Quando se tratar da apuração do ICMS\-ST \(campo Indicador de Apuração = 2\), o campo UF indicará a UF ser considerada para o débito especial\. 

Campos obrigatórios 🡪 todos os que aparecem com \(__\*__\) no Manual de Layout 

Tabelas de destino 🡪 Os dados serão gravados na tabela da apuração do ICMS, ou da apuração do ICMS\-ST, dependendo do campo “Indicador de Apuração”, da seguinte forma:

    \- Se Indicador de Apuração = 1 \(ICMS\)  🡪 o débito especial será gravado na __ICT\_DEBITO\_ESP\_PROC__

 

    \- Se Indicador de Apuração = 2 \(ICMS\-ST\) 🡪 o débtio especial será gravado na __ICT\_DEBITO\_ESP\_ST\_PROC__

A seguir estão definidas as regras de validação de cada campo \(__RN01__ a __RN13__\)\.

Na __RN14__ estão descritas as regras para a gravação dos campos nas tabelas definitivas \(ICT\_DEBITO\_ESP\_PROC e ICT\_DEBITO\_ESP\_ST\_PROC\)\.

__RN01__

__ao__

__RN07__

__Código da Empresa__

__Código do Estabelecimento __

__Obrigação Fiscal__

__Data da Apuração __

__Indicador da Apuração __

__UF__

__Número de Discriminação__

Os campos 01 ao 07 são os campos que identificam a chave da tabela “mãe” __SAFX309__ \(ICT\_DEBITO\_ESP/ICT\_DEBITO\_ESP\_ST\), por isso, as críticas referentes a estes campos são exatamente as mesmas descritas para a __SAFX309__ \(ver documento de regras da __SAFX309__\)\.

Quando algum destes campos for invalidado pela crítica, o registro *não* será importado e será gravada no log a mensagem de erro correspondente, conforme definido nas regras\.

__Crítica da existência do débito especial:__

Quando todos estes campos forem validados, será verificada a existência do débito especial na base de dados, da seguinte forma:

    \- Se campo “05\-Indicador de Apuração” = 1 \(ICMS\) 🡪 pesquisar o débito especial na tabela dos débitos especiais

                                                                                           da apuração do ICMS \(__ICT\_DEBITO\_ESP__\)

 

    \- Se campo “05\-Indicador de Apuração” = 2 \(ICMS\-ST\) 🡪 pesquisar o débito especial na tabela dos débitos especiais

                                                                                                da apuração do ICMS\-ST \(__ICT\_DEBITO\_ESP\_ST__\)

Caso o débito especial *não exista*, o registro não será importado e no log de erros será gravada a seguinte mensagem:

*                                                                          “Débito Especial não cadastrado” *

__RN08__

__Sequencial__

Campo obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                   “O sequencial é de preenchimento obrigatório”*

                                                          \(mensagem 92645 da CAT\_ERRO\)

__RN09__

__Número do Documento de Arrecadação__

Campo *nã*o obrigatório\.

Os campos Número do Documento de Arrecadação e do Número do Processo __*não*__ são obrigatórios, pois o usuário poderá informar apenas um dos dois\. No entanto, é necessário que um dos dois esteja preenchido\.

Assim, será realizada a seguinte crítica:

Se os campos “09\-Número do Documento de Arrecadação” __e__ “10\-Número do Processo” não estiverem preenchidos:

  

      Neste caso o registro não será importado e no log de erros será gravada a seguinte mensagem:

*       “O número do documento de arrecadação e/ou o número do processo deve estar preenchido” *

                                                     \(mensagem 92646 da CAT\_ERRO\)

__RN10__

__Número do Processo__

Campo *nã*o obrigatório\.

Os campos Número do Documento de Arrecadação e Número do Processo __*não*__ são obrigatórios, pois o usuário poderá informar apenas um dos dois\. No entanto, é necessário que um dos dois esteja preenchido, por isso, será realizada a crítica descrita na __RN09__\. 

Caso o campo “*11\-Origem do Processo*” tenha sido informado, o preenchimento deste campo passa a ser obrigatório, por isso, será realizada a seguinte crítica:

Se campo “*11\-Origem do Processo*”  <> nulo e campo “*10\-Número do Processo*” = nulo:

      Neste caso, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

         *“Ao informar a origem do processo, é obrigatório informar também o campo número do processo”*

                                                     \(mensagem 92647 da CAT\_ERRO\)

__RN11__

__Origem do Processo__

Campo *não* obrigatório\.

Quando preenchido, deve ser = “0”, “1”, “2” ou “9”\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                  “Origem do processo inválida\. Informar 0, 1, 2 ou 9”*

  

                                                               \(mensagem 93346 da CAT\_ERRO\)

Caso o campo “*10\-Número do Processo*” tenha sido informado, o preenchimento deste campo passa a ser obrigatório, por isso, será realizada a seguinte crítica:

Se campo “*10\-Número do Processo*” <> nulo e campo “*11\-Origem do Processo*” = nulo:

      Neste caso, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

          *“Ao informar o número do processo, é obrigatório informar também o campo origem”*

                                                     \(mensagem 92649 da CAT\_ERRO\)

__RN12__

__Descrição do Processo__

Campo *não* obrigatório\.

__RN13__

__Descrição Complementar__

Campo *não* obrigatório\.

__RN14__

__Gravação dos Dados__:

Segue a descrição do conteúdo a ser gravado em cada coluna das tabelas definitivas:

    \- Se campo “05\-Indicador de Apuração” = 1 \(ICMS\)  🡪 o débito especial será gravado na __ICT\_DEBITO\_ESP\_PROC;__

 

    \- Se campo “05\-Indicador de Apuração” = 2 \(ICMS\-ST\) 🡪 o débtio especial será gravado na __ICT\_DEBITO\_ESP\_ST\_PROC;__

__    ICT\_DEBITO\_ESP\_PROC__

__  ICT\_DEBITO\_ESP\_ST\_PROC__

__                    Conteúdo a ser gravado:__

__                     \(campos da SAFX310\)__

COD\_EMPRESA

COD\_EMPRESA

01\-Código da Empresa 

COD\_ESTAB

COD\_ESTAB

02\-Código do Estabelecimento

COD\_TIPO\_LIVRO

COD\_TIPO\_LIVRO

03\-Obrigação Fiscal

DAT\_APURACAO

DAT\_APURACAO

04\-Data da Apuração 

                     \- \- \- \- \-

IDENT\_ESTADO

Ident referente à UF do campo “06\-UF”

NUM\_DISCRIMINACAO

NUM\_DISCRIMINACAO

07\-Número de Discriminação 

COD\_AJUSTE\_ICMS

COD\_AJUSTE\_ICMS

\(não será preenchido\)

Este campo não é utilizado\.

*Observação*:

*Estas tabelas não precisariam ter o COD\_AJUSTE\_ICMS, pois a tela dos  Processos/Doc\.Arrecad não têm esta informação\. Além disso, observar também que o código de ajuste não compõe a chave do Débito Especial, logo, não é por causa da chave da tabela mãe\. Provavelmente, deve ter sido um equívoco na criação da tabela\.*

*A chave da tabela mãe, a ICT\_DEBITO\_ESP ou ICT\_DEBITO\_ESP\_ST,  é apenas a chave da Apuração \+ N\.Discriminação \(ou seja, não tem nenhum cód\. Ajuste\)\.*

*Na criação da SAFX310, esta coluna não foi criada no layout da SAFX justamente para não confundir o usuário, pois isso poderia ocasionar problemas na importação\. O usuário poderia preencher corretamente os campos chave do débito especial \(campo 01 ao 07\), mas com um código de ajuste diferente\. *

SEQ\_PROC\_ARRECAD

SEQ\_PROC\_ARRECAD

08\-Sequencial

NUM\_DOC\_ARRECAD

NUM\_DOC\_ARRECAD

09\-Número do Documento de Arrecadação

NUM\_PROC

NUM\_PROC

10\-Número do Processo

ORIGEM\_PROC

ORIGEM\_PROC

11\-Origem do Processo

DSC\_PROC

DSC\_PROC

12\-Descrição do Processo

DSC\_COMPLEMENTAR

DSC\_COMPLEMENTAR

13\-Descrição Complementar

IND\_DIG\_CALCULADO __\(\*\*\*\)__ 

IND\_DIG\_CALCULADO __\(\*\*\*\)__

“I” \(=Importado\)

__\(\*\*\*\) __As colunas IND\_DIG\_CALCULADO foram criadas nestas tabelas na MFS40160, quando foi criada a SAFX310 para importação destes dados\.

