# MTZ-Job-Servidor-Importacao-SAFX309

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX309.docx
- **Modificado:** 2020-08-23
- **Tamanho:** 85 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX309

Tabela dos Débitos Especiais da Apuração do ICMS / ICMS\-ST

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS40160

Criação da SAFX309

Criação da SAFX309 para a importação dos débitos especiais da apuração 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

A tabela SAFX309 foi criada pela MFS40160 com objetivo de carregar os dados dos Débitos Especiais da apuração do ICMS ou ICMS\-ST \(aba “Débitos Especiais”\) do Módulo ICMS\.

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

Este documento descreve *apenas* as regras da importação da __SAFX309__\. Para consultar as regras das demais tabelas, ver os documentos específicos de cada SAFX\.  

Estrutura da tabela __SAFX309__ 🡪 vide manual de layout

Campos que compõe a chave da tabela:

     \- Código da Empresa

     \- Código do Estabelecimento

     \- Obrigação Fiscal

     \- Data da Apuração

     \- Indicador da Apuração          *\(1 = Apuração ICMS, 2 = Apuração ICMS\-ST\)*

     \- UF                                         *\(Identificador da UF\)*

     \- Número de Discriminação    *\(Sequencial\)*

A __SAFX309__ é utilizada para importação dos débitos especiais tanto da apuração do ICMS, como do ICMS\-ST\. Por isso, possui os campos “*Indicador da Apuração*” e “*UF*”\. Quando se tratar da apuração do ICMS\-ST \(campo Indicador de Apuração = 2\), o campo UF indicará a UF ser considerada para o débito especial\. 

Campos obrigatórios 🡪 todos os que aparecem com \(__\*__\) no Manual de Layout 

Tabelas de destino 🡪 Os dados serão gravados na tabela da apuração do ICMS, ou da apuração do ICMS\-ST, dependendo do campo “Indicador de Apuração”, da seguinte forma:

    \- Se Indicador de Apuração = 1 \(ICMS\)  🡪 o débito especial será gravado na __ICT\_DEBITO\_ESP__

 

    \- Se Indicador de Apuração = 2 \(ICMS\-ST\) 🡪 o débtio especial será gravado na __ICT\_DEBITO\_ESP\_ST__

A seguir estão definidas as regras de validação de cada campo \(__RN01__ a __RN13__\)\.

Na __RN14__ estão descritas as regras para a gravação dos campos nas tabelas definitivas \(__ICT\_DEBITO\_ESP__ e __ICT\_DEBITO\_ESP\_ST__\)\.

__RN01__

__Código da Empresa__

Campo obrigatório\.

Crítica padrão: quando o campo não estiver preenchido,* *o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O código da empresa deve ser preenchido”*

                                                               \(mensagem 9001 da CAT\_ERRO\)

__RN02__

__Código do Estabelecimento __

Campo obrigatório\.

Crítica padrão: quando o campo não estiver preenchido,* *o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                      “O código do estabelecimento deve ser preenchido”*

                                                                 \(mensagem 9002 da CAT\_ERRO\)

__RN03__

__Obrigação Fiscal__

Campo obrigatório\.

Deve ser = 108 ou 165

Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                    “O código da obrigação fiscal deve ser 108 ou 165”*

__RN04__

__Data da Apuração __

Campo obrigatório\.

Deve ser uma data válida

Crítica da existência da apuração:

Será verificada a existência da Apuração do ICMS em questão, ou seja, se já existe uma apuração gerada para a Empresa,  Estabelecimento, Obrigação Fiscal e Data da Apuração\. 

Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                           “Não existe apuração gerada p/o estabelecimento e data informados” *

*                                                               *\(mensagem 92655 da CAT\_ERRO\)

Crítica do status da apuração:

Se o status da apuração for = “Válido”, então o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                       “Não é permitida a importação de lançamentos para apurações já validadas”*

                                                              \(mensagem 92662 da CAT\_ERRO\)

__RN05__

__Indicador da Apuração __

Campo obrigatório\.

Deve ser = “1” \(Apuração do ICMS\) ou  “2” \(Apuração do ICMS\-ST\)

Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                “Indicador da apuração inválido\. Informar 1 \(Apuração ICMS\) ou 2 \(Apuração ICMS\-ST\)”*

__RN06__

__UF __

<a id="OLE_LINK27"></a>Campo não obrigatório\.

Este campo só deverá estar preenchido quando o indicador de apuração for = “2” \(Apuração do ICMS\-ST\)\.

Assim, serão feitas as seguintes críticas:

Se UF preenchida e campo indicador de apuração = 1 \(ICMS\):

      Neste caso, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*       “O campo UF só deve ser informado para os lançamentos referentes à Apuração ICMS\-ST”*

                                                    \(mensagem 92657 da CAT\_ERRO\)

Se UF *não* preenchida e campo indicador de apuração = 2 \(ICMS\-ST\):

      Neste caso, o registro não será importado, e no log de erros será  gravada a seguinte mensagem:

*      “O campo UF é de preenchimento obrigatório quando o indicador da apuração = ICMS\-ST”*

                                                    \(mensagem 92658 da CAT\_ERRO\)

O conteúdo deve ser uma UF válida, de acordo com a lista das UF’s da tabela ESTADOS\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                          * *“O Código da Unidade da Federação é inválido”*

                                                    \(mensagem 90027 da CAT\_ERRO\)

__RN07__

__Número de Discriminação__

Campo obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                         “O número de discriminação é de preenchimento obrigatório”*

                                                          \(mensagem 92660 da CAT\_ERRO\)

__RN08__

__Código de Ajuste – Sped Fiscal \(Reg\. E111/E220\)__

Campo obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                         “O Código de Ajuste – Sped Fiscal é de preenchimento obrigatório”*

As outras críticas do código informado serão realizadas de acordo com o tipo da apuração \(se ICMS ou ICMS\-ST\), da seguinte forma:

__Se indicador da apuração = 1 \(Apuração do ICMS\):__

- O código deve estar cadastrado na “Tabela dos Códigos de Ajuste do Sped Fiscal” \(módulo ICMS, menu Apuração > Apuração do ICMS > Lançamentos Complementares >  Código de Ajuste \- SPED Fiscal\)\. 
- Além disso, as duas primeiras posições \(que indicam a UF\), devem conter a sigla da UF do Estabelecimento\. 
- Caso o código não conste na tabela, ou não seja um código da UF do Estabelecimento, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                  “Código de Ajuste – Sped Fiscal inexistente ou não pertence à UF do Estabelecimento”*

                                                                           \(mensagem 92708 da CAT\_ERRO\)

- A terceira posição do código deve ser = “__0__”, o que indica __Apuração do ICMS__\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                           

*                                             “Código de Ajuste – Sped Fiscal incompatível com o tipo da apuração” *

                                                                     \(mensagem 92709 da CAT\_ERRO\)  * *

- A quarta posição do código, que indica a operação, deve ser = “__5__”, o que indica um __Débito Especial__\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                             “Código de Ajuste inválido\. A quarta posição deve ser = 5 \(Débito Especial\)”*

__Se indicador da apuração = 2 \(Apuração do ICMS\-ST\):__

- O código deve estar cadastrado na “Tabela dos Códigos de Ajuste do Sped Fiscal” \(módulo ICMS, menu Apuração > Apuração do ICMS > Lançamentos Complementares >  Código de Ajuste \- SPED Fiscal\)\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                             “Código de Ajuste – Sped Fiscal não cadastrado na Tabela dos Códigos de Ajuste do Sped Fiscal”*

*            Obs\.: No caso da Apuração do ICMS\-ST, a UF do código informado não será validada, e poderá ser qualquer uma, mesmo *

*           diferente da UF informada no campo “UF” \(regra definida conforme o funcionamento da tela de manutenção\)\. *

- A terceira posição do código deve ser = “__1__”, o que indica __Apuração do ICMS\-ST__\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                         

*                                           “Código de Ajuste – Sped Fiscal incompatível com o tipo da apuração” *

                                                                   \(mensagem 92709 da CAT\_ERRO\)  * *

- A quarta posição do código, que indica a operação, deve ser = “__5__”, o que indica um __Débito Especial__\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                             “Código de Ajuste inválido\. A quarta posição deve ser = 5 \(Débito Especial\)”*

__RN09__

__Valor do Débito__

Campo obrigatório\.

Quando não preenchido, ou = zero, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                         “Valor do débito não informado ou igual a zero”*

__RN10__

__Descrição__

Campo não obrigatório\.

__RN11__

__Sub\-Apuração do Sped Fiscal__

Campo não obrigatório\.

Quando preenchido, deve ser =  “1”, “2”, “3”, “4”, “5” ou “6”, conforme a quantidade de sub apurações tratadas no Sped Fiscal\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                      “Sub\-Apuração do Sped Fiscal inválida\. Os valores válidos são: 1, 2, 3, 4, 5 ou 6”*

                                                                \(mensagem 92974 da CAT\_ERRO\)

__RN12__

__Indicador de Lançamento Complementar do Conv\. 52/05__

Campo não obrigatório\.

<a id="OLE_LINK59"></a>

Quando preenchido, deve ser = “S” ou “N”\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

 

                            *“Indicador de Lançamento Complementar do Conv\. 52/05” inválido\. Informar S ou N”*

                                                                \(mensagem 92713 da CAT\_ERRO\)

           \(Obs\.: Acertar esta msg pois esta “cortada”\. Sugestão: tirar a palavra “Campo” do início e completar o final “S ou N”\)

Quando este campo for preenchido, será obrigatório o preenchimento do campo “UF \- Conv\. 52/05” \(campo 13\)\.

Se campo = “S” __e__ campo “UF \- Conv\. 52/05” *não* preenchido:

     Neste caso o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*          “Se Indicador Lanc\. Compl\. Conv\.52/05 = S, é obrigatório  informar a UF\-Conv\. 52/05”*

__RN13__

__UF \- Conv\. 52/05__

Campo não obrigatório\.

Quando preenchido, seu conteúdo deve ser uma UF válida, de acordo com a lista das UF’s da tabela ESTADOS\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

* *

*                                                                        “UF \- Conv\.52/05 inválida”*

                                                                  \(mensagem 92716 da CAT\_ERRO\)

Caso este campo seja preenchido, e o campo “*Indicador de Lançamento Complementar do Conv\. 52/05*” = “N” ou nulo, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                       “O campo UF\-Conv\.52/05 so deve ser informado p/lanctos referentes ao Conv\.52/05*

                                                                    \(mensagem 93131 da CAT\_ERRO\)

                                                               \(Obs\.: Acertar esta msg pois esta “cortada”\)

__RN14__

__Gravação dos Dados__:

Segue a descrição do conteúdo a ser gravado em cada coluna das tabelas definitivas:

    \- Se campo “05\-Indicador de Apuração” = 1 \(ICMS\)  🡪 o débito especial será gravado na __ICT\_DEBITO\_ESP;__

 

    \- Se campo “05\-Indicador de Apuração” = 2 \(ICMS\-ST\) 🡪 o débtio especial será gravado na __ICT\_DEBITO\_ESP\_ST;__

__         ICT\_DEBITO\_ESP__

__     ICT\_DEBITO\_ESP\_ST__

__                    Conteúdo a ser gravado:__

__                     \(campos da SAFX309\)__

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

08\- Código de Ajuste – Sped Fiscal \(Reg\. E111/E220\)

VAL\_DEBITO

VAL\_DEBITO

09\-Valor do Débito

DSC\_DEBITO

DSC\_DEBITO

10\-Descrição

IND\_DIG\_CALCULADO

IND\_DIG\_CALCULADO

“I” \(=Importado\)

IND\_SUB\_APUR

\- \- \- \- \-

11\-Sub\-Apuração do Sped Fiscal

IND\_EST\_DEB\_CONV

\- \- \- \- \-

12\-Indicador de Lançamento Complementar do Conv\. 52/05 

IDENT\_ESTADO\_CONV

\- \- \- \- \-

Ident referente à UF do campo “13\-UF \- Conv\. 52/05”

COD\_AJ\_ICMS\_CONV

\- \- \- \- \-

*\(não será preenchido\)*

*Este campo não é utilizado\.*

