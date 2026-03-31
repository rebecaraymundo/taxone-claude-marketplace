# MTZ-Job-Servidor-Importacao-SAFX311

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX311.docx
- **Modificado:** 2020-08-23
- **Tamanho:** 87 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX311

Tabela dos Documentos Fiscais vinculados ao Débito Especial 

da Apuração do ICMS / ICMS\-ST

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS40160

Criação da SAFX311

Criação da SAFX311 para a importação dos Documentos Fiscais vinculados ao débitos especiais 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

A tabela SAFX311 foi criada pela MFS40160 com objetivo de carregar os dados dos Documentos Fiscais vinculados aos Débitos Especiais da apuração do ICMS ou ICMS\-ST \(aba “Débitos Especiais”\) do Módulo ICMS\.

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

Este documento descreve *apenas* as regras da importação da __SAFX311__\. Para consultar as regras das demais tabelas, ver os documentos específicos de cada SAFX\.  

Estrutura da tabela __SAFX311__ 🡪 vide manual de layout

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

Data Fiscal

           Campos chave do documento fiscal vinculado

                                  \(SAFX07\)

Movimento Entrada/Saída

Normal/Devolução

Tipo de Documento

Indicador Pessoa Fis/Jur

Código Pessoa Fis/Jur

Número Documento Fiscal

Série Documento Fiscal

Subsérie Documento Fiscal

Número do Item __\(\*\*\*\)__

Número do item do documento fiscal vinculado

                               \(SAFX08\) 

__*\(\*\*\*\)*__* A SAFX não terá o campo DISCR\_ITEM, existente na tabela definitiva ICT\_DEBITO\_ESP\_AJ / ICT\_DEBITO\_ESP\_ST\_AJ, pois não há necessidade\. Para identificar o item, quando for o caso, a tabela *__*SAFX311*__* terá o número do item, exatamente como funciona na tela de manutenção\. Nos casos em que o item for informado, ao gravar os dados na tabela definitiva a importação gravará o campo DISCR\_ITEM com o conteúdo do DISCR\_ITEM recuperado do item \(SAFX08\), já que a importação terá que validar a existência do item na SAFX08\. *

A __SAFX311__ é utilizada para importação dos Documentos Fiscais vinculados ao débito especial, tanto da apuração do ICMS, como do ICMS\-ST\. Por isso, possui os campos “*Indicador da Apuração*” e “*UF*”\. Quando se tratar da apuração do ICMS\-ST \(campo Indicador de Apuração = 2\), o campo UF indicará a UF ser considerada para o débito especial\. 

Campos obrigatórios 🡪 todos os que aparecem com \(__\*__\) no Manual de Layout 

Tabelas de destino 🡪 Os dados serão gravados na tabela da apuração do ICMS, ou da apuração do ICMS\-ST, dependendo do campo “Indicador de Apuração”, da seguinte forma:

    \- Se Indicador de Apuração = 1 \(ICMS\)  🡪 o débito especial será gravado na __ICT\_DEBITO\_ESP\_AJ__

 

    \- Se Indicador de Apuração = 2 \(ICMS\-ST\) 🡪 o débtio especial será gravado na __ICT\_DEBITO\_ESP\_ST\_AJ__

A seguir estão definidas as regras de validação de cada campo __\(RN01 a RN18\)__\.

Na __RN19 __estão descritas as regras para a gravação dos campos nas tabelas definitivas \(ICT\_DEBITO\_ESP\_AJ e ICT\_DEBITO\_ESP\_ST\_AJ\)\.

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

__Data Fiscal do Documento Fiscal Vinculado__

Quando não preenchida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                    “A data fiscal do documento vinculado é de preenchimento obrigatório”*

                                                     \(mensagem 92664 da CAT\_ERRO\)

__RN09__

__Movimento Entrada/Saída do Documento Fiscal Vinculado__

Quando não preenchido, ou, quando seu conteúdo não estiver de acordo com as opções descritas no manual de layout, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                     “Campo Movimento E/S do documento fiscal vinculado não preenchimento ou inválido”*

                                                     \(mensagem 92665 da CAT\_ERRO\)

__RN10__

__Normal/Devolução do Documento Fiscal Vinculado__

Quando não preenchido, ou, quando seu conteúdo não estiver de acordo com as opções descritas no manual de layout, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                 “Campo Normal/Devolução do documento fiscal vinculado não preenchimento ou inválido”*

                                                     \(mensagem 92666 da CAT\_ERRO\)

__RN11__

__Tipo do Documento Fiscal Vinculado__

Este campo deve estar preenchido, e o código informado deve constar na Tabela dos Tipos de Documentos Fiscais \(SAFX2005\), caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*      “Tipo do documento fiscal vinculado não preenchido ou não cadastrado na Tabela dos Tipos de Documentos \(SAFX2005\)”*

                                                     \(mensagem 92667 da CAT\_ERRO\)

__RN12__

__Indicador da Pessoa Física/Jurídica do Documento Fiscal Vinculado__

Quando não preenchido, ou, quando seu conteúdo não estiver de acordo com as opções descritas no manual de layout, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*              “Indicador da Pessoa Fis/Jur do documento fiscal vinculado não preenchimento ou inválido”*

                                                     \(mensagem 92669 da CAT\_ERRO\)

__RN13__

__Código da Pessoa Física/Jurídica do Documento Fiscal Vinculado __

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                   “O código da Pessoa Fis/Jur do documento fiscal vinculado é de preenchimento obrigatório”*

                                                     \(mensagem 92670 da CAT\_ERRO\)

A partir do indicador e do código da pessoa fis/jur informados, será verificada a existência da pessoa na Tabela de Pessoas Físicas/Jurídicas \(SAFX04\)\. Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*         “A Pessoa Fis/Jur  do documento fiscal vinculado não consta na Tabela das Pessoas Fis/Jur \(SAFX04\)”*

                                                     \(mensagem 92668 da CAT\_ERRO\)

__RN14__

__Número do Documento Fiscal Vinculado __

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                              “O número do documento fiscal vinculado é de preenchimento obrigatório”*

                                                     \(mensagem 92671 da CAT\_ERRO\)

__RN15__

__Série do Documento Fiscal Vinculado __

Campo *não* obrigatório\.

Quando preenchido, seu conteúdo *não* será criticado\.

__RN16__

__Subsérie do Documento Fiscal Vinculado __

Campo *não* obrigatório\.

Quando preenchido, seu conteúdo *não* será criticado\.

__Crítica da existência do documento na SAFX07:__

Após a crítica de todos os campos que identificam o documento fiscal \(campos 01, 02, e 08 ao 16\), será verificado se o documento informado consta na base de dados \(SAFX07\), a partir destes campos que compõe a chave do documento\.

*\(Importante: a série e a subsérie são campos não obrigatórios, e assim, quando não preenchidos, será considerado um caracter  branco\)*

Caso o documento não seja encontrado, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                         “O documento fiscal informado não consta na Tabela de Documentos Fiscais”*

                                                     \(mensagem 92674 da CAT\_ERRO\)

__RN17__

__Número do Item do Documento Fiscal Vinculado __

Campo *não* obrigatório\.

__Crítica da existência do item na SAFX08:__

Quando preenchido, será verificada a existência do item informado na Tabela dos Itens dos Documentos Fiscais \(SAFX08\), da seguinte forma:

A partir da chave do documento fiscal validado na regra anterior \(__RN16__\), será feita uma pesquisa para identificar se o número de item informado existe na SAFX08\. A busca será feita a partir dos campos chave do documento e do campo “18\-Item Nota Fiscal” da SAFX08\.

Caso o item não seja identificado, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                 “O número do item informado não consta na Tabela de Itens de Documentos Fiscais”*

                                                     \(mensagem 92673 da CAT\_ERRO\)

__RN18__

__Valor do Ajuste __

Quando não preenchido, ou  = zero,  o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                          “Valor do ajuste não preenchido ou igual a zero”*

                                                     \(mensagem 92672 da CAT\_ERRO\)

Obs: Na tela de manutenção dos débitos especiais, o sistema compara o total do Valor de Ajuste informado nos documentos vinculados, com o valor do débito especial\. Quando não coincide, aparece uma mensagem de aviso informando sobre a diferença\.  Na importação esta crítica *não* será realizada, pelo fato dos documentos vinculados da SAFX311 serem validados individualmente\.

__RN19__

__Gravação dos Dados__:

Segue a descrição do conteúdo a ser gravado em cada coluna das tabelas definitivas:

    \- Se campo “05\-Indicador de Apuração” = 1 \(ICMS\)  🡪 o débito especial será gravado na __ICT\_DEBITO\_ESP\_AJ;__

 

    \- Se campo “05\-Indicador de Apuração” = 2 \(ICMS\-ST\) 🡪 o débtio especial será gravado na __ICT\_DEBITO\_ESP\_ST\_AJ;__

__    ICT\_DEBITO\_ESP\_AJ__

__  ICT\_DEBITO\_ESP\_ST\_AJ__

__                    Conteúdo a ser gravado:__

__                     \(campos da SAFX311\)__

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

*Estas tabelas não precisariam ter o COD\_AJUSTE\_ICMS, pois a tela dos Documentos Fiscais vinculados não têm esta informação\. Além disso, observar também que o código de ajuste não compõe a chave do Débito Especial, logo, não é por causa da chave da tabela mãe\. Provavelmente, deve ter sido um equívoco na criação da tabela\.*

*A chave da tabela mãe, a ICT\_DEBITO\_ESP ou ICT\_DEBITO\_ESP\_ST,  é apenas a chave da Apuração \+ N\.Discriminação \(ou seja, não tem nenhum cód\. Ajuste\)\.*

*Na criação da SAFX311, esta coluna não foi criada no layout da SAFX, justamente para não confundir o usuário, pois isso poderia ocasionar problemas na importação\. O usuário poderia preencher corretamente os campos chave do débito especial \(campo 01 ao 07\), mas com um código de ajuste diferente\. *

DATA\_FISCAL

DATA\_FISCAL

08\-Data Fiscal do Documento Fiscal Vinculado

MOVTO\_E\_S

MOVTO\_E\_S

09\-Movimento E/S do Documento Fiscal Vinculado

NORM\_DEV

NORM\_DEV

10\-Normal/Devolução do Documento Fiscal Vinculado

IDENT\_DOCTO

IDENT\_DOCTO

IDENT referente ao tipo do documento informado no campo “11\-Tipo do Documento Fiscal Vinculado”

IDENT\_FIS\_JUR

IDENT\_FIS\_JUR

IDENT referente a pessoa fis/jur informada nos campos 12 e 13 \(indicador e código da pessoa fis/jur\)

NUM\_DOCFIS

NUM\_DOCFIS

14\-Número do Documento Fiscal Vinculado

SERIE\_DOCFIS

SERIE\_DOCFIS

__Se__ campo “15\-Série do Documento Fiscal Vinculado” não

      preenchido:

     O campo será gravado com um caracter branco \(‘ ‘\)

__Senão__

    O campo será gravado com o conteúdo do campo 

     “15\-Série do Documento Fiscal Vinculado”;

SUB\_SERIE\_DOCFIS

SUB\_SERIE\_DOCFIS

__Se__ campo “16\-Subsérie do Documento Fiscal Vinculado”

      não preenchido:

     O campo será gravado com um caracter branco \(‘ ‘\)

__Senão__

    O campo será gravado com o conteúdo do campo 

     “16\-Subsérie do Documento Fiscal Vinculado”;

DISCRI\_ITEM

DISCRI\_ITEM

__Se__ campo “17\- Número do Item do Documento Fiscal  

      Vinculado” não preenchido:

     O campo será gravado com um caracter branco \(‘ ‘\)

__Senão__

    O campo será gravado com a informação da coluna

    DISCR\_ITEM do item da nota \(informação que será

    recuperada da SAFX08 no momento de criticar a

    existência do item\)\.

NUM\_ITEM

NUM\_ITEM

__Se__ campo “17\-Número do Item do Documento Fiscal 

      Vinculado” não preenchido:

     O campo não será preenchido

__Senão__

    O campo será gravado com o conteúdo do campo 

    “17\-Número do Item do Documento Fiscal 

      Vinculado”\.

VLR\_AJUSTE

VLR\_AJUSTE

18\-Valor do Ajuste

IND\_DIG\_CALCULADO 

IND\_DIG\_CALCULADO 

“I” \(=Importado\)

