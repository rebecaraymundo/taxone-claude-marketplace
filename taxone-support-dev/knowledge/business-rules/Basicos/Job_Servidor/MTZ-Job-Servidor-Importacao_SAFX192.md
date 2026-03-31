# MTZ-Job-Servidor-Importacao_SAFX192

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX192.docx
- **Modificado:** 2022-04-07
- **Tamanho:** 95 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX192

Tabela de Referências de Documentos Fiscais

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS9512

Tratamento das Devoluções de Saídas p/ atendimento à Portaria CAT 158/2015\.

Criação da SAFX192 para o tratamento das operações de devolução na rotina de pré\-geração do registro C176 da EFD\. 

14/02/2017

__MFS28381__

Novo tipo de referência \(2\)

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>Alteração da SAFX192 para a criação de um novo tipo de referência \(Saída x NF’s de entrada da aquisição do produto\), que será utilizado no cálculo do Valor de Confronto da Portaria CAT 42/2018\.

14/06/2019

__MFS29704__

Inclusão do tipo de referência \(3\)

Alteração na SAFX192 para criação de um novo tipo de referência 3 \(Entrada de mercadoria adquirida de remetente indireto \(substituído\) x NF’s Emitidas pelos Substitutos Tributários\)

O tipo “3” significa que para uma entrada de mercadoria adquirida de remetente indireto \(contribuinte substituído\), o usuário poderá informar a\(s\) nota\(s\) originária\(s\) da quantidade da mercadoria comercializada, que foram adquiridas pelo remetente indireto e emitidas por contribuintes Substitutos Tributários\.

20/12/2019

__MFS61955__

Inclusão do tipo de referência \(4\)

Alteração na SAFX192 para criação de um novo tipo de referência 4 \- “Devolução \(Entrada\) x Documento de Origem \(Cupom Fiscal Saída\)”, e inclusão dos campos: \- 27 – Modelo, 28 \- Número do Caixa, 29 – COO  e 30 – Data Emissão\.

19/05/2021

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX192__ 🡪 vide manual de layout

A SAFX192 é uma tabela “filha” da SAFX08, e seu objetivo é informar para uma determinada nota fiscal \(identificada pelos campos 01 a 15\), as notas fiscais de referência \(campos 17 a 22\)\. Para cada item da SAFX08, poderão ser informados um ou vários itens das notas fiscais de referência\.

As referências podem ser de vários tipos, e utilizadas em obrigações diversas\. Para detalhes sobre o objetivo e utilização desta tabela, consultar o manual de layout \(aba Indice e Tabelas SAFX\)\.

__Campos que compõe a chave da tabela:__

                           __                      Campos chave da SAFX08 \(campo 01 ao 15\)__

__                                                                               \+__

__                                                        Tipo de Referência \(campo 16\)__

__                                                                               \+__

__                            Campos de identificação do item da nota fiscal de referência do Tipo Referência = ‘1’ e ‘2’ \(campo 17 ao 23\)__

__                                                                               \+__

__                            Campos de identificação do item da nota fiscal de referência do Tipo Referência = ‘3’ \(campo 23, 25 e 26\)__

__                                                                               \+ \[MFS61955\]__

__                            Campos de identificação do item do cupom fiscal de referência do Tipo Referência = ‘4’ \(campo 23, 27 ao 30\)__

A manutenção da tabela é feita na tela de manutenção dos documentos fiscais, na aba “Item Mercadoria”, através da opção “Documentos Referenciados”\.

__Crítica da existência do item na SAFX08:__

Após a validação dos campos que identificam o item do documento fiscal \(campo 01 ao 15\), conforme as regras descritas abaixo, será verificado se o item existe na base de dados \(SAFX08\)\. 

Caso o item não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                          “O item do documento fiscal informado não foi identificado na Tabela de Itens de Documentos Fiscais”*

Para facilitar a identificação do problema, o log deve informar os dados básicos do item informado nos campos 01 ao 15\.  

__Crítica da existência do item DE REFERÊNCIA na SAFX08:__

Após a validação dos campos que identificam o item do documento fiscal DE REFERÊNCIA \(campo 17 ao 23\), conforme as regras descritas abaixo, será verificado se o item DE REFERÊNCIA existe na base de dados \(SAFX08\)\. 

Esta crítica depende do tipo de referência \(campo 16\)\. 

<a id="OLE_LINK12"></a>Para o Tipo de Referência = “1”:

    Critérios para recuperar o item na base de dados:

    \- \-\-Utilizar o mesmo Código de Empresa do campo 01;

    \- \-\-Utilizar o mesmo Código de Estabelecimento do campo 02;

    \- Utilizar o mesmo Indicador do Produto do campo 12;

    \- Utilizar o mesmo Código do Produto do campo 13;

    \- Para o indicador de entrada/saída \(MOVTO\_E\_S\), considerar o conteúdo = “9”;

    \- Para o indicador de devolução \(NORM\_DEV\), considerar o conteúdo = “1”;

<a id="OLE_LINK18"></a>    \- Para os demais campos chave do item, considerar a informação dos campos 17 à 23;

     Caso o item não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*     “O item do documento fiscal de referência não existe na Tabela de Itens de Documentos Fiscais, ou não atende aos requisitos*

*     básicos \(consultar o Manual de Layout\)”*

   Para facilitar a identificação do problema, o log deve informar os dados básicos do item de referência informado nos campos 17 ao 23\.

__\(MFS28381:__ Alteração nas regras da importação devido à inclusão de um novo Tipo de Referência \(Tipo “2”\)\)

Para o Tipo de Referência = “2”:

    Critérios para recuperar o item na base de dados:

    \- Utilizar o mesmo Código de Empresa do campo 01;

    \- Utilizar o mesmo Código de Estabelecimento do campo 02;

    \- Utilizar o mesmo Indicador do Produto do campo 12;

    \- Utilizar o mesmo Código do Produto do campo 13;

    \- Para o indicador de entrada/saída \(MOVTO\_E\_S\), considerar o conteúdo __<>__ “9”;

    \- Para os demais campos chave do item, considerar a informação dos campos 17 à 23;

<a id="OLE_LINK17"></a>     Caso o item não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*     “O item do documento fiscal de referência não existe na Tabela de Itens de Documentos Fiscais, ou não atende aos requisitos*

*     básicos \(consultar o Manual de Layout\)”*

    Para facilitar a identificação do problema, o log deve informar os dados básicos do item de referência informado nos campos 17 ao 23\.

__\(MFS29704:__ Alteração nas regras da importação devido à inclusão de um novo Tipo de Referência \(Tipo “3”\)\)

Para o Tipo de Referência = “3”:

O item do documento fiscal DE REFERÊNCIA \(campo 17 ao 23\) __não__ será verificado se existe na base de dados \(SAFX08\)\. 

Isso porque o tipo “3” refere\-se a documento que não está na base do cliente, mas sim na base o remetente do documento \(indireto\)\. 

Sendo assim, a identificação do item do documento fiscal DE REFERÊNCIA para o tipo “3”, não é carregada nos campos 17 ao 23, mas sim nos campos 23, 25 e 26\. Os campos 17 ao 22 não são utilizados para o tipo “3”\.

__\[MFS61955\]__

__Crítica da existência do item do Cupom Fiscal DE REFERÊNCIA na SAFX994:__

Após a validação dos campos que identificam o item do cupom fiscal DE REFERÊNCIA \(campo 23, 27 ao 30\), conforme as regras descritas abaixo, será verificado se o item DE REFERÊNCIA existe na base de dados \(SAFX994\)\. 

Esta crítica só deve ser feita para o tipo de referência \(campo 16\) = 4\.

Para o Tipo de Referência = “4”:

    Critérios para recuperar o item na base de dados na SAFX994:

    \- Código da Empresa \(campo 01 SAFX994\) = Código de Empresa \(campo 01 da SAFX192\);

    \- Código do Estabelecimento \(campo 02 SAFX994\) = Código do Estabelecimento \(campo 02 da SAFX192\);

    \- Modelo Documento \(campo 03 SAFX994\) = Modelo do Cupom Fiscal de Referência \(campo 27 da SAFX192\);

    \- Número do Caixa \(campo 04 SAFX994\) = Número do Caixa do Cupom Fiscal de Referência \(campo 28 da SAFX192\);

    \- COO \(campo 05 SAFX994\) = COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência \(campo 29 da SAFX192\);

    \- Data da emissão \(campo 06 SAFX994\) = Data de Emissão do Cupom Fiscal de Referência \(campo 30 da SAFX192\);

    \- Número do item \(campo 07 SAFX994\) = Item da Nota Fiscal de Referência \(campo 23 da SAFX192\);

    \- Indicador do Produto \(campo 08 SAFX994\) = Indicador do Produto \(campo 12 da SAFX192\);

    \- Código do Produto \(campo 09 SAFX994\) = Código do Produto \(campo 13 da SAFX192\);

   

     Caso o item não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*     93417 “O item do cupom fiscal de referência não existe na Tabela de Itens de Cupons Fiscais \(SAFX994\), ou não atende aos requisitos básicos \(consultar o Manual de Layout\)”*

    Para facilitar a identificação do problema, o log deve informar os dados básicos do item de referência informado nos campos 27 ao 30\.

MFS28381

MFS29704

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

__RN03__

__Campo Data da Escrita Fiscal__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Data da Escrita Fiscal não preenchida ou inválida”*

__RN04__

__Campo Movimento Entrada/Saída __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '9'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

Outras críticas:

__\[MFS61955\]__

<a id="OLE_LINK14"></a>Quando o campo “__16\-Tipo de Referência” = ‘1’ __ou ‘4’, o conteúdo deste campo deve ser __<>__ ‘9’, ou seja, deve ser uma nota de entrada\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

92858* “Quando o Tipo de Referência = “1” ou “4”, o campo Movimento E/S deve ser = 1, 2, 3, 4 ou 5 \(apenas notas de entrada\)”*

Quando o campo __“16\-Tipo de Referência” = ‘2’__, o conteúdo deste campo deve ser __=__ ‘9’, ou seja, deve ser uma nota de saída\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                “Quando o Tipo de Referência = “2”, o campo Movimento E/S deve ser = 9 \(apenas notas de saída\)”*

Quando o campo “__16\-Tipo de Referência” = ‘3’__, o conteúdo deste campo deve ser __<>__ ‘9’, ou seja, deve ser uma nota de entrada\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                “Quando o Tipo de Referência = “3”, o campo Movimento E/S deve ser = 1, 2, 3, 4 ou 5 \(apenas notas de entrada\)”*

MFS28381

MFS29704

__RN05__

__Campo Normal ou Devolução __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

Outras críticas:

__\[MFS61955\]__

Quando o campo “16\-Tipo de Referência” = ‘1’ ou ‘4’, o conteúdo deste campo deve ser = ‘2’ \(nota de devolução\)\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                       *92859* “Quando o Tipo de Referência = “1” ou “4”, o campo Normal/Devolução deve ser = 2” \(nota de devolução\)”*

Quando o campo “16\-Tipo de Referência” = ‘3’, o conteúdo deste campo deve ser = ‘1’ \(nota normal\)\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                       “Quando o Tipo de Referência = “3”, o campo Normal/Devolução deve ser = “1” \(nota normal\)”*

MFS29704

__RN06__

__Campo Tipo de Documento __

Campo de preenchimento __*obrigatório*__\.

Deve ser um código existente na Tabela de Tipos de Documento \(SAFX2005\)\.

Quando o campo não for preenchido, ou o código informado não existir na SAFX2005, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou que não foi encontrado na Tabela de Tipos de Documento \(mensagem padrão\)\.

__RN07__

__Campo Indicador da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

__RN08__

__Campo Código da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

A partir do conteúdo dos campos 07 e 08 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela \(mensagem padrão\)\.

__RN09__

__Campo Número do Documento Fiscal__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

Ver na __RN00 __como será realizada a crítica de existência do documento e item informados na SAFX08\.

__RN10__

__Campo Série do Documento Fiscal__

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

__RN11__

__Campo Subsérie do Documento Fiscal__

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

__RN12__

__Campo Indicador do Produto__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '6', '7', '8'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

__RN13__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Código do Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

A partir do conteúdo dos campos 12 e 13 \(indicador e código do produto\) será verificada a existência do produto informado na Tabela de Cadastro dos Produtos \(SAFX2013\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

__RN14__

__Campo Unidade Padrão__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

O código informado deve existir na Tabela das Unidades de Medida Padrão \(SAFX2017\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade padrão não existe na tabela \(mensagem padrão\)\.

__RN15__

__Campo Item da Nota Fiscal__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

__RN16__

__Campo Tipo de Referência__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: “1” ou “2” ou “3”, ou “4”

     1 \- Devolução \(Entrada\) x Documentos de Origem \(SaÍdas\)

     2 \- Saída x Entradas \(Cálculo do Valor de Confronto da Portaria  CAT 42/18\)                    \(novo tipo incluído na__ MFS26714__\)

     3 \- Entrada de mercadoria adquirida de remetente indireto \(substituído\) x NF’s Emitidas pelos Substitutos Tributários \(incluído __MFS29704__\)

    4 \- Devolução \(Entrada\) x Documento de Origem \(Cupom Fiscal Saída\)__ \[MFS61955\]__

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido\. Exemplo: “*Tipo de Referência não preenchido ou inválido*”\.

Obs: Este campo indica o tipo de referência existente entre as notas\. As referências podem ser de vários tipos, e utilizadas em obrigações diversas\.

MFS28381

MFS29704

__RN17__

__Campo Número do Documento Fiscal de Referência__

Campo de preenchimento __*obrigatório para os Tipos de Referência “1” e “2” *__

Para o Tipo de Referência = “1” e “2”:

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido\. 

A mensagem deve seguir o mesmo texto da mensagem utilizada para o campo 09, mas indicando que se trata do campo referente ao documento fiscal de referência\. Exemplo: “*Numero do Documento Fiscal de Referência não preenchido*”\.

Ver na __RN00 __como será realizada a crítica de existência do documento/item REFERENCIADO informados, na SAFX08\.

Para os Tipos de Referência = “3” e“4”: __\[MFS61955\]__

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

 93318 “*Quando o Tipo de Referência = “3” ou “4”, o campo Numero do Documento Fiscal de Referência não pode ser preenchido*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS29704

__RN18__

__Campo Série do Documento Fiscal de Referência__

Para o Tipo de Referência = “1” e “2”:

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando este campo não for preenchido, será gravado um caracter __branco__ \(“ “\), pois faz referência a Série da SAFX07, que grava branco por ser chave\.

Para o Tipo de Referência = “3” e“4”: __\[MFS61955\]__

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

 93319 “*Quando o Tipo de Referência = “3” ou “4”, o campo Série do Documento Fiscal de Referência não pode ser preenchido*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS29704

__RN19__

__Campo Subsérie do Documento Fiscal de Referência__

Para o Tipo de Referência = “1” e “2”:

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando este campo não for preenchido, será gravado um caracter __branco__ \(“ “\), pois faz referência a Série da SAFX07, que grava branco por ser chave\.

Para o Tipo de Referência = “3” e“4”: __\[MFS61955\]__

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

 93320 “*Quando o Tipo de Referência = “3” ou “4”, o campo Subsérie do Documento Fiscal de Referência não pode ser preenchido*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS29704

__RN20__

__Campo Data da Escrita Fiscal do Documento de Referência__

Para o Tipo de Referência = “1” e “2”:

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“Data da Escrita Fiscal do Documento Fiscal de Referência não preenchida ou inválida”\.*

* *

Esta data deve ser <= a data fiscal do documento \(campo 03\)\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“A Data da Escrita Fiscal do Documento de Referência \(campo 20\) deve ser menor ou igual à Data Fiscal do Documento \(campo 03\)”\.*

Para o Tipo de Referência = “3” e“4”: __\[MFS61955\]__

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

 93321 “*Quando o Tipo de Referência = “3” ou “4”, o campo Data da Escrita Fiscal do Documento Fiscal de Referência não pode ser preenchido*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS29704

__RN21__

__Campo Indicador da Pessoa Física/Jurídica \(Destinatário/Emitente\) do Documento Fiscal de Referência __

Para o Tipo de Referência = “1” e “2”:

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando a pessoa fis/jur do documento fiscal de referência *não* for informada, os campos serão gravados com a informação da pessoa fis/jur do documento \(campos 07 e 08\)\. Assim, a validação deste campo é feita da seguinte forma:

Se o campo for preenchido,

    Deve ser um dos valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\. Caso contrário, o registro não será importado, e no log de erros será 

    gravada uma mensagem de erro \( “*Indicador da Pessoa Fis/Jur do Documento Fiscal de Referência com conteúdo inválido*”\)\.

Se o campo *não* for preenchido, 

     Neste caso, o campo será gravado com o conteúdo do indicador da pessoa fis/jur informada no campo 07\.

Para o Tipo de Referência = “3” e“4”: __\[MFS61955\]__

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

 93322 “*Quando o Tipo de Referência = “3” ou “4”, o campo Indicador da Pessoa Fis/Jur do Documento Fiscal de Referência não pode ser preenchido*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS29704

__RN22__

__Campo Código da Pessoa Física/Jurídica \(Destinatário/Emitente\) do Documento Fiscal de Referência __

Para o Tipo de Referência = “1” e “2”:

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando a pessoa fis/jur do documento fiscal de referência *não* for informada, os campos serão gravados com a informação da pessoa fis/jur do documento \(campos 07 e 08\)\. Assim, a validação deste campo é feita da seguinte forma:

Se o campo for preenchido,

     A partir do conteúdo dos campos 21 e 22 \(indicador e código da pessoa fis/jur do documento de referência\) será verificada a

     existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e

     no log de erros será gravada uma mensagem de erro \(“*Pessoa Fis/Jur do documento fiscal de referência não cadastrada*”\)\.

Se o campo *não* for preenchido, 

     O campo será gravado com o conteúdo do código da pessoa fis/jur informada no campo 08\. Lembrando que neste caso, a crítica

     sobre a existência da pessoa na SAFX04 já foi realizada na validação dos campos 07 e 08\. 

Para o Tipo de Referência = “3” e“4”: __\[MFS61955\]__

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

 93323 “*Quando o Tipo de Referência = “3” ou “4”, o campo Código da Pessoa Fis/Jur do Documento Fiscal de Referência não pode ser preenchido*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS29704

__RN23__

__Campo Item da Nota Fiscal de Referência__

Campo de preenchimento __*obrigatório*__\.

__\[MFS61955\]__

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(92866 “*Item da Nota/Cupom Fiscal de Referência não preenchido*”\)\.

__RN24__

__Campo Quantidade da Devolução ou Proporcional à Aquisição de Remetente Indireto__

Campo de preenchimento __*não obrigatório*__\.

__Para Tipo de Referência = ‘1’__ e“4”: __\[MFS61955\]__

<a id="OLE_LINK16"></a>Quando o campo “16\-Tipo de Referência” = ‘1’ e ‘4’, este campo é de preenchimento obrigatório\. Neste caso, quando a quantidade não for informada, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                         *92867* “Quando o Tipo de Referência = “1” ou “4”, a Quantidade da Devolução deve ser informada”*

__Para Tipo de Referência = ‘2’:__

Quando o campo “16\-Tipo de Referência” = ‘2’, este campo não deve ser preenchido\. Neste caso, se a quantidade for informada, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                          *93256* “O campo “Quantidade da Devolução” não deve ser informado para o Tipo de Referência = “2”*

__Para Tipo de Referência = ‘3’:__

Quando o campo “16\-Tipo de Referência” = ‘3’, este campo é de preenchimento obrigatório\. Neste caso, quando a quantidade não for informada, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93324* “Quando o Tipo de Referência = “3”, a Quantidade Proporcional a Aquisição de Remetente Indireto deve ser informada”*

MFS28381

MFS29704

__RN25__

__Campo Chave de Acesso da Nfe Emitida pelo Substituto Tributário__

Para o Tipo de Referência = “1”, “2” e“4”: __\[MFS61955\]__

Campo não deve ser preenchido\.

Neste caso, se o campo for preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93325* “Quando o Tipo de Referência = “1”, “2” ou “4”, o campo “Chave de Acesso da Nfe Emitida pelo Substituto Tributário” não deve ser preenchido*

Não preencher este campo \(gravar com nulo\)\.

Para o Tipo de Referência = “3”:

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido\.

93326 “*Quando o Tipo de Referência = “3”, o campo “Chave de Acesso da Nfe Emitida pelo Substituto Tributário” deve ser preenchido*”\.

MFS29704

__RN26__

__Campo CNPJ do Substituto Tributário__

Para o Tipo de Referência = “1”, “2” e“4”: __\[MFS61955\]__:

Campo não deve ser preenchido\.

Neste caso, se o campo for preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93327* “Quando o Tipo de Referência = “1”, “2” ou “4”, o campo “CNPJ do Substituto Tributário” não deve ser preenchido*

Não preencher este campo \(gravar com nulo\)\.

Para o Tipo de Referência = “3”:

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido\.

93328 “*Quando o Tipo de Referência = “3”, o campo “CNPJ do Substituto Tributário” deve ser preenchido*”\.

Quando preenchido, validar o CNPJ\. Caso o mesmo não esteja válido, o registro não será importado, e no log de erros será gravada a mensagem informando que o CNPJ é inválido\.

93329 “*O CNPJ do Substituto Tributário não é válido*”\.

MFS29704

__RN27__

__Campo Modelo do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório para o Tipo de Referência “4” *__

Para o Tipo de Referência = “1”, “2” e “3”:

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

   *93455 “Quando o Tipo de Referência = “1”, “2” ou “3”, o campo Modelo do Cupom Fiscal de Referência não pode ser preenchido*”

Para os Tipos de Referência = “4”: 

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido\. 

 *93456 “Quando o Tipo de Referência = “4”, o campo Modelo do Cupom Fiscal de Referência deve ser preenchido*”\.

Quando preenchido, o código informado será validado na Tabela de Modelos de Documentos Fiscais \(SAFX2024\), e caso não exista, o registro não será importado, e no log de erros será gravada uma mensagem \(*93410 “O Modelo do Cupom Fiscal de Referência deve estar cadastrado na Tabela de Modelos de Documentos Fiscais \(SAFX2024\)*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS61955

__RN28__

__Campo Número do Caixa do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório para o Tipo de Referência “4” *__

Para o Tipo de Referência = “1”, “2” e “3”:

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

*   93457 “Quando o Tipo de Referência = “1”, “2” ou “3”, o campo Número do Caixa do Cupom Fiscal de Referência não pode ser preenchido*”

Para os Tipos de Referência = “4”: 

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido\. 

* 93458 “Quando o Tipo de Referência = “4”, o campo Número do Caixa do Cupom Fiscal de Referência deve ser preenchido*”\.

Quando preenchido, o número do caixa informado será validado na Tabela de Equipamentos ECF \(SAFX2087\), e caso não exista, o registro não será importado, e no log de erros será gravada uma mensagem \(*93412 “O Modelo do Cupom Fiscal de Referência deve estar cadastrado na Tabela de Modelos de Documentos Fiscais \(SAFX2024\)*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS61955

__RN29__

__Campo COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório para o Tipo de Referência “4” *__

Para o Tipo de Referência = “1”, “2” e “3”:

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

   *93459 “Quando o Tipo de Referência = “1”, “2” ou “3”, o campo COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência não pode ser preenchido*”

Para os Tipos de Referência = “4”: 

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido\. 

 *93460 “Quando o Tipo de Referência = “4”, o campo COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência deve ser preenchido*”\.

Não preencher este campo \(gravar com nulo\)\.

MFS61955

__RN30__

__Campo Data de Emissão do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório para o Tipo de Referência “4” *__

Para o Tipo de Referência = “1”, “2” e “3”:

Quando preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não pode ser preenchido\. 

*  93462 “Quando o Tipo de Referência = “1”, “2” ou “3”, o campo Data Emissão do Cupom Fiscal de Referência não pode ser preenchido*”

Para os Tipos de Referência = “4”: 

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido\. 

 *93461 “Quando o Tipo de Referência = “4”, o campo Data Emissão do Cupom Fiscal de Referência deve ser preenchido*”\.

Quando preenchido e se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:  

    *93421 \- “Data de Emissao do Cupom Fiscal de Referencia invalida”\.*

Não preencher este campo \(gravar com nulo\)\.

MFS61955

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

