# MTZ-Importacao_SAFX130

- **Fonte:** MTZ-Importacao_SAFX130.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 33 KB

---

                                          

__           JOB SERVIDOR \- SAFX130 – NF\-e Denegadas / Inutilizadas__

__Localização __

__Módulo__: Básicos 🡪 Job Servidor

__Menu__: Importação 🡪 Programação / Execução

	Importação batch 🡪 Programação/Execução

####                                   Documentos de Requisito                                                

	

__DR__

__Nome __

__Descrição __

OS2388\-E14

Nova Tabela SAFX130 

Criação de uma nova tabela SAFX para permitir a importação e a manutenção de documentos eletrônicos denegados ou inutilizados\.

OS3564

Novo código de modelo – 58\.

Novo código de modelo de Documento Fiscal – Manifesto Eletrônico de Documentos Fiscais – MDF\-e\.

OS3673

Novo campo

Criação do campo da chave NFE\.

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

CH13035\_2015

Novo código de modelo – 65

Novo código de modelo de Documento Fiscal – Nota Fiscal Eletronica para Consumidor Final\.

MFS8937

Novo código de modelo – 67

Novo código de modelo de Documento Fiscal – CT\-e OS

MFS13290

Novo código de modelo – 63

Ato Cotepe 48/17: Inclusão dos documentos fiscais de modelo 63 \(BP\-e\) no Sped Fiscal \(registro D100\)\. RN07

                                       Regras de Negócio                                                

Cód\.

__Descrição__

__DR__

RN01

Campo Movimento Entrada/Saída

Campo obrigatório, quando não informado gravar mensagem de erro no log de processo e não importar o registro:

*“O movimento entrada/saída é de preenchimento obrigatório e não foi informado”*

O conteúdo deste campo deve ser  2, 3, 4,  5, ou 9, conforme o manual de layout\. Observar que o valor ‘1’ não é permitido, pois naturalmente notas eletrônicas denegadas ou inutilizadas de terceiros não vêm para o Mastersaf\.

Caso o valor esteja inválido, gravar mensagem de erro no log de processo e não importar o registro:

*             “Movimento entrada/saída com conteúdo inválido”*

RN02

Campo Número Documento Inicial

Campo *obrigatório*, quando não informado gravar mensagem de erro no log de processo e não importar o registro:

*   “O número do documento inicial é de preenchimento obrigatório e *

*    não foi informado”*

O conteúdo informado deve ser numérico, e caso contenha caracteres alfanuméricos, deve\-se  gravar mensagem de erro no log de processo e não importar o registro:

*   “Número do documento inicial com conteúdo inválido\. O conteúdo do*

*    campo deve ser numérico”*

\(antes de efetuar esta crítica desprezar os brancos à direta que possam existir\)

Esta crítica é necessária porque o layout permite que o usuário informe uma sequencia de documentos, do inicial ao final, e assim, podemos ter problemas caso ocorra a existência de caracteres alfanumérico, por uma situação de erro qualquer\.

OS2388\-E14

RN03

Campo Número Documento Final

Campo *não obrigatório*\. Quando preenchido, deverão ser feitas duas críticas:

1\-O conteúdo informado deve ser numérico, e caso contenha caracteres alfanuméricos, deve\-se  gravar mensagem de erro no log de processo e não importar o registro:

   “Número do documento final com conteúdo inválido\. O conteúdo do

    campo deve ser numérico”

\(antes de efetuar esta crítica desprezar os brancos à direta que possam existir\)

Esta crítica é necessária porque o layout permite que o usuário informe uma sequencia de documentos, do inicial ao final, e assim, podemos ter problemas caso ocorra a existência de caracteres alfanumérico, por uma situação de erro qualquer\.

2\-Verificar se o conteúdo é igual ou superior ao documento inicial informado\. Caso não, gravar mensagem de erro no log de processo e não importar o registro:

*    “O número do documento final não pode ser inferior ao documento*

*     inicial”*

OS2388\-E14

RN04

Campo Série do Documento

Campo *não obrigatório*\. Quando preenchido, não é criticado\.

OS2388\-E14

RN05

Campo Subsérie do Documento

Campo *não obrigatório*\. Quando preenchido, não é criticado\.

OS2388\-E14

RN06

Campo Data de Referência

Campo *obrigatório*, quando não informado gravar mensagem de erro no log de processo e não importar o registro:

* “A data de referência é de preenchimento obrigatório e não foi informada”*

Quando preenchida, verificar se é uma data válida\.

*            “Data de referência com conteúdo inválido”*

OS2388\-E14

RN07

Campo Modelo do Documento

\[Alteração – OS3564\]/\[ALTERADA – CH13035\_2015\]

Campo *obrigatório*, quando não informado gravar mensagem de erro no log de processo e não importar o registro:

*      “O modelo é de preenchimento obrigatório e não foi informado”*

Quando preenchido, o modelo informado deve existir na tabela de modelos \(SAFX2024\), e, além disso, deve ser = 55 \(NF\-e\) ou 57 \(CT\-e\) ou 58 \(MDF\-e\) ou 65 \(NFEC\-e\) ou 67 \(CT\-e OS\) __ou 63 \(BP\-e\)__*, *caso contrário, gravar mensagem de erro no log de processo \(conforme o caso\), e não importar o registro:

Se não existir na SAFX2024:

   *“O campo Codigo de Modelo de Documento não está cadastrado\.*

*na Tabela de Modelos de Documentos \(SAFX2024\)”*

Se existir na SAFX2024, mas for diferente de 55, 57, 58, 65, 67 __e 63__:

   

       *“Modelo inválido\. Informar apenas 55 \(NF\-e\) ou 57 \(CT\-e\) ou 58 \(MDF\-e\) ou 65 \(Nota Fiscal Eletrônica para Consumidor Final\) ou 67 \(CT\-e OS\) *__*ou 63 \(BP\-e\)*__*”* 

OS2388\-E14 / OS\-3564

/ CH13035\_2015/ MFS8937

MFS13290

RN08

Campo Situação da Nota

Campo *obrigatório*, quando não informado gravar mensagem de erro no log de processo e não importar o registro:

*   “A situação da nota \(denegada/inutilizada\) é de preenchimento obrigatório e não foi informada”*

Quando preenchido, o conteúdo deve ser = 1 \(denegada\) ou 2 \(inutilizada\), caso contrário, gravar mensagem de erro no log de processo e não importar o registro:

*  “Situação da nota inválida\. Informar apenas 1 \(Denegada\) ou 2 \(Inutilizada\)”* 

OS2388\-E14

RN09

Campo Inscrição Estadual

Campo *não obrigatório*\. Quando preenchido, verificar se a inscrição informada esta cadastrada para o Estabelecimento no Módulo PIM \(Módulo PIM,  menu “Cadastros 🡪 Inscrição Estadual por Estabelecimento”\)\. Caso não, gravar mensagem de erro no log de processo e não importar o registro:

            “*Inscrição Estadual não cadastrada no Módulo PIM*”

OS2388\-E14

RN12

__Campo 12 \- Chave de acesso NFE__

Campo *não obrigatório*\. Quando preenchido, não é criticado\.

OS\-3673

RN13

__Campo Código da SCP__

Alterar a rotina de exportação para que seja considerado o novo campo:

Tabela: SAFX130

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__OS4316__

