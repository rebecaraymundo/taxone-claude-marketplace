# MTZ-Job-Servidor-Importacao_SAFX308

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX308.docx
- **Modificado:** 2021-02-24
- **Tamanho:** 108 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX308

__             Tabela das Informações Complementares das Operações de Devolução Sujeitas ao ST __

__           __

__                                                           \(EFD – Registros C181 e C186\)__

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação à Execução

\- Importação Batch à Programação à Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS43963

Sped Fiscal – Atualização Legal da versão 1\.14, vigência Jan/2021

Criação da tabela SAFX308 para carga das informações complementares de ST, a serem utilizadas na geração dos registros C181e C186 Sped Fiscal\. 

08/10/2020

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX308__ à vide manual de layout

A SAFX308 é uma tabela “filha” da SAFX08 \(Itens dos Documentos Fiscais\), e assim, poderão existir ‘n’ registros para cada item da SAFX08\.

As informações da SAFX308 dão origem aos registros __C181__ e __C186__ do Sped Fiscal\. Estes registros são referentes às operações de  devolução de saídas \(__C181__\) e devolução de entradas \(__C186__\)\. Assim, o objetivo desta tabela é informar os documentos fiscais \(nota/item\) que originaram a devolução\. 

A manutenção desta tabela é feita na tela de manutenção dos itens de documentos fiscais \(aba “Item Mercadoria”\) no módulo DW, através da opção: “__*Informações Complementares Oper\. ST \(Sped Fiscal\) \-*__* *__*Devoluções*__”\.

__Os campos que compõem a chave da tabela são:__

- Campos de identificação do item da nota devolução \(campos chave da SAFX08\);

	

- Campos de identificação do item da nota fiscal, ou cupom fiscal, de referência da devolução \(documento que deu origem à  devolução\);

 Campos de identificação do item  \(SAFX08\) da nota de devolução:

                           Campos 01 ao campo 15             

Campos de identificação do item da nota fiscal, ou cupom fiscal, de referência da devolução:

                           Campos 16 ao campo  30

O tipo do documento de referência será indicado no campo “16\- Espécie do Documento de Referência da Devolução”, da seguinte forma:

   1\-Nota Fiscal \(SAFX07/08\)

   2\-Cupom Fiscal \(SAFX993/994\)

   3\-Cupom Fiscal SAT \(SAFX201/202\)

Os campos que identificam a chave do item do documento fiscal de referência, são os seguintes, dependendo da opção informada no campo 16:

	

\- Se opção = 1 \(Nota Fiscal\) à campo 17 ao 23, e campo 30;

\- Se opção = 2 \(Cupom Fiscal\) à campos 24, 25, 26, 27 e 30;

 

\- Se opção = 3 \(Cupom Fiscal SAT\) à campos 27, 28, 29 e 30;

*OBS: Para os itens de referência da SAFX08 \(campo 16 = “1”\), não foram criados os campos  MOVTO\_E\_S nem NORM\_DEV\. Isso porque o MOVTO\_E\_S será sempre o inverso do MOVTO\_E\_S da nota devolução, e o NORM\_DEV será sempre = “1”\.*

Após a validação dos campos de identificação do item da devolução, e do item do documento de referência, conforme descrito nas regras abaixo, serão feitas algumas validações:

__I \- Crítica da existência do item do documento fiscal da devolução:__

Por se tratar de uma tabela “filha” da SAFX08, só é permitida a inclusão de informações complementares na SAFX308 quando o item do documento fiscal já existir\. Assim, após a validação dos campos de identificação do item da devolução \(campo 01 ao 15\) conforme as regras descritas abaixo, será verificado se o item em questão existe na SAFX08\. Caso não exista, o registro __*não*__ será importado, e no log de erros será gravada uma mensagem de erro \(“*Item do documento fiscal inexistente”*\)\.

*\(A mensagem do log deve mostrar os dados de identificação do item do documento fiscal da devolução, para permitir ao usuário a identificação do registro com erro\) *

__II \- Crítica da existência do item do documento fiscal de referência:__

Além de verificar a existência do item do documento da devolução, também será verificada a existência do item do documento de referência informado\. Assim, após a validação dos campos que identificam o item de referência \(dependendo do campo 16, conforme descrito abaixo\), será verificado se o item do documento de referência existe na SAFX08, na SAFX994 ou na SAFX202, conforme o caso\. Quando não existir, o registro __*não*__ será importado, e no log de erros será gravada uma mensagem de erro, que depende da tabela de origem deste item, da seguinte forma:

\- Se opção = 1 à  *“O* *item do documento fiscal de referência não existe na Tabela de Itens das Notas Fiscais \(SAFX08\)”;*

\- Se opção = 2 à *“O* *item do documento fiscal de referência não existe na Tabela de Itens dos Cupons Fiscais \(SAFX994\)”;*

\- Se opção = 3 à *“O* *item do documento fiscal de referência não existe na Tabela de Itens dos Cupons Fiscais SAT \(SAFX202\)”;*

*\(O log deve mostrar os dados de identificação do item do documento fiscal da devolução, e também a identificação do item do documento de referência, para permitir ao usuário a identificação do registro com erro\) *

Os campos que compõem a identificação do item de referência, e são utilizados para montar a chave do item em cada uma das tabelas \(SAFX08, SAFX994 ou SAFX202\) são os seguintes:

- __Se espécie do documento de referência = 1 \(Nota Fiscal\)__ à campo 17 ao 23, e campo 30;

Na SAFX308 não existem os campos Movimento E/S e o Normal/Devolução do documento de referência, isso porque seus valores são pré\-determinados\. Ou seja, *uma nota de referência não pode ser uma nota de devolução*, e *o tipo da operação \(entrada ou saída\), deve ser sempre o inverso da devolução*\. Então, ao pesquisar a nota de referência na SAFX08, considerar o seguinte conteúdo para estes campos:

 \- MOVTO\_E\_S = “9”, se a nota de devolução em questão for uma entrada \(campo “04\-Movimento E/S” <> “9”\),

__   ou__

 \- MOVTO\_E\_S <> “9”, se a nota de devolução em questão for uma saída \(campo “04\-Movimento E/S” = “9”\);

    

 \- NORM\_DEV = “1” \(nota normal\); 

- __Se espécie do documento de referência = 2 \(Cupom Fiscal\)__ à campos  24, 25, 26, 27 e 30;

 

- __Se espécie do documento de referência = 3 \(Cupom Fiscal SAT\)__ à campos 27, 28, 29 e 30;

__III \- Crítica do Produto que consta no item do documento fiscal de referência:__

Além de verificar a existência do item de documento fiscal de referência informado pelo usuário, será verificado também, se o Produto que consta neste item é realmente o Produto devolvido\. Ou seja, se é o mesmo Produto da nota de devolução em questão \(campos 12 e 13\)\. 

Nesta verificação, o Indicador e o Código do Produto da devolução \(campos 12 e 13\) são comparados ao Indicador e o Código do Produto do item da nota de referência informada, através dos seguintes campos, dependendo da espécie do documento de referência:

\- Na SAFX08 \(item da nota fiscal\): campos 13 e 14;

\- Na SAFX994 \(item do cupom fiscal\): campos 08 e 09;

\- Na SAFX202 \(Item do cupom fiscal SAT\): campos 07 e 08;

*\(Ao comparar o Produto do documento de referência, com o Produto da nota de devolução, o recomendado é não trabalhar com o IDENT\_PRODUTO\. Isso porque estes dois documentos normalmente serão de datas diferentes, e pode ser que tenham IDENT’s diferentes do mesmo Produto, devido à diferentes datas de validade da SAFX2013\)  *

Caso o Produto não seja o mesmo, o registro __*não*__ será importado, e no log de erros será gravada uma mensagem de erro: *“O Produto que consta no item do documento fiscal de referência informado, não é o mesmo Produto da devolução”\.*

 

*\(O log deve mostrar os dados de identificação do item do documento fiscal da devolução, e também a identificação do item do documento de referência, para permitir ao usuário a identificação do registro com erro\) *

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo Data Escrita Fiscal__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchida, ou data inválida, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão “*Data Escrita Fiscal não preenchida ou inválida”*\)\.

__RN04__

__Campo Movimento Entrada/Saída__

Campo de preenchimento __*obrigatório*__\.

Deve ser = “1”, “2”, “3”, “4”, “5” ou “9”;

Quando não preenchido, ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 90129: “*O Campo Tipo de Movimento de Entrada/Saida não esta preenchido ou preenchido com informacão inválida”*\)\.

__RN05__

__Campo Normal/Devolução__

Campo de preenchimento __*obrigatório*__\.

A princípio, este campo deve ser sempre = “2” \(o que indica nota de devolução\);

Quando não preenchido, ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem de erro 

\(“*O campo Normal/Devolução não está preenchido, ou preenchido com informação inválida\. Deve ser = “2”, indicando nota de devolução”*\)\.

__RN06__

__Campo Tipo de Documento __

Campo de preenchimento __*obrigatório*__\.

Deve ser um código existente na Tabela de Tipos de Documento \(SAFX2005\)\.

Quando o campo não for preenchido, ou o código informado não existir na SAFX2005, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou que não foi encontrado na Tabela de Tipos de Documento, conforme as seguintes mensagens padrão:

\- Código 60853: “*O Código do Tipo de Documento deve ser preenchido*”

\- Código 90125: “*O Código do Tipo de Documento não esta cadastrado*”\.

__RN07__

__Campo Indicador da Pessoa Física/Jurídica __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão código 90088: “*O Indicador de Pessoa Fisica/Juridica não esta preenchido ou preenchido com informação inválida\.*”\)\.

__RN08__

__Campo Código da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90089: “*O Código da Pessoa Fisica/Juridica não esta preenchido*”\)\.

A partir do conteúdo dos campos 07 e 08 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela \(mensagem padrão código 90124: “*O Código da Pessoa Fisica/Juridica não esta cadastrado*”\)\.

__RN09__

__Campo Número do Documento Fiscal__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90112: “*O Campo Número do Documento não esta preenchido*\.”\)\.

__RN10__

__Campo Série do Documento Fiscal__

Campo de preenchimento __*não*__ obrigatório\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

__RN11__

__Campo Subsérie do Documento Fiscal__

Campo de preenchimento __*não*__ obrigatório\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

__RN12__

__Campo Indicador do Produto__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '6', '7', '8'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão código 90035: “*Indicador do Produto \(Produto/Insumo/Embalagem/Consumo, etc\) não esta preenchido ou preenchido com informação inválida*”\)\.

__RN13__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Código do Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 60855: “*O Código do Produto deve ser preenchido*”\)\.

A partir do conteúdo dos campos 12 e 13 \(indicador e código do produto\) será verificada a existência do produto informado na Tabela de Cadastro dos Produtos \(SAFX2013\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão código 90034: “*Código do Produto não cadastrado*”\)\.

__RN14__

__Campo Unidade Padrão__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90147: “*O Campo Unidade Padrão não esta preenchido*\.”\)\.

O código informado deve existir na Tabela das Unidades de Medida Padrão \(SAFX2017\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade padrão não existe na tabela \(mensagem padrão código 90148: “*A Unidade Padrão não esta cadastrada*”\)\.

__RN15__

__Campo Item da Nota Fiscal__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90132: “*O Número do Item do Documento Fiscal não esta preenchido*”\)\.

__Crítica da existência do item do documento fiscal da devolução:__

Após a validação dos campos 01 ao 15, será feita a verificação da existência do item do documento fiscal de devolução informado\. Caso não exista, o registro *não* será importado, e no log será gravada uma mensagem de erro\. As regras desta verificação, assim como a mensagem de erro a ser gerada, quando for o caso, estão descritas na __RN00\.__

__RN16__

__Campo Espécie do Documento de Referência da Devolução__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: “1”, “2” ou “3”

1 = Nota Fiscal \(SAFX07/08\)

2 = Cupom Fiscal \(SAFX993/994\)

3 = Cupom Fiscal SAT \(SAFX201/202\)

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(“*O campo “Espécie do Documento de Referência da Devolução” deve ser preenchido com as opções 1, 2 ou 3*”\)\.

__Crítica da opção informada X tipo da nota de devolução__:

Quando a nota de devolução em questão for uma *nota de saída* \(campo “04\-Movimento Entrada/Saída” = “9”\), e portanto, tratar\-se de uma *devolução de entrada*, o conteúdo deste campo deve ser = “1” \(Nota Fiscal\)\. Caso contrário,  o registro não será importado, e no log de erros será gravada uma mensagem \(“*O campo “Espécie do Documento de Referência da Devolução” deve ser = 1 quando se tratar de devolução de entradas*\)\.

Obs\.: Esta crítica se deve ao fato do registro C186 \(Devolução de Entrada\) só aceitar para os documentos de referência da devolução, documentos de modelo 01, 1B, 04 ou 55\. Conforme consta no GP, na validação do campo “09\-__ __COD\_MOD\_ENTRADA” do C186, os valores válidos são \[01, 1B, 04, 55\]\. Logo, não podemos ter como documento de referência um cupom fiscal\. 

O conteúdo deste campo impacta na validação dos campos 17 ao 30, conforme consta nas regras a seguir:

__RN17__

__Campo Número do Documento Fiscal de Referência __

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 1 \(Nota Fiscal\)\.

  

Quando a espécie do documento de referência = 2 ou 3, este campo *não* deve ser preenchido\. 

__Crítica__: 

Se \(não preenchido e espécie do documento de referência = 1\) __ou__ \(preenchido e espécie do documento de referência <> 1\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “17\-Número do*

*      Documento Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de referência = 1\. Para as*

*     espécies 2 ou 3 o campo não deve ser informado*”\)\.   

__RN18__

__Campo Série do Documento Fiscal de Referência __

Campo de preenchimento __*não*__ obrigatório\.

Poderá ser informado apenas quando a espécie do documento de referência \(campo 16\) = 1 \(Nota Fiscal\)\.

  

Quando a espécie do documento de referência = 2 ou 3, este campo *não* deve ser preenchido\. 

__Crítica__: 

Se preenchido e espécie do documento de referência <> 1\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “18\-Série do*

*      Documento Fiscal de Referência” só pode ser informado quando a espécie do documento de referência = 1\. Para as*

*     espécies 2 ou 3 o campo não deve ser informado*”\)\.   

__RN19__

__Campo Subsérie do Documento Fiscal de Referência __

Campo de preenchimento __*não*__ obrigatório\.

Poderá ser informado apenas quando a espécie do documento de referência \(campo 16\) = 1 \(Nota Fiscal\)\.

  

Quando a espécie do documento de referência = 2 ou 3, este campo *não* deve ser preenchido\. 

__Crítica__: 

Se preenchido e espécie do documento de referência <> 1\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “19\-Subsérie do*

*      Documento Fiscal de Referência” só pode ser informado quando a espécie do documento de referência = 1\. Para as*

*     espécies 2 ou 3 o campo não deve ser informado*”\)\.   

__RN20__

__Campo Tipo do Documento de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 1 \(Nota Fiscal\)\.

  

Quando a espécie do documento de referência = 2 ou 3, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 1\) __ou__ \(preenchido e espécie do documento de referência <> 1\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “20\-Tipo do*

*      Documento de Referência” é de preenchimento obrigatório quando a espécie do documento de referência = 1\. Para as*

*     espécies 2 ou 3 o campo não deve ser informado*”\)\.   

__Crítica 2__:

 

O código informado deve ser um código existente na Tabela de Tipos de Documento \(SAFX2005\)\. Quando for informado um código inválido, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O Tipo do Documento de Referência deve estar cadastrado na Tabela de Tipos de Documentos \(SAFX2005\)*”\.

__RN21__

__Campo Data Escrita Fiscal do Documento de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 1 \(Nota Fiscal\)\.

  

Quando a espécie do documento de referência = 2 ou 3, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 1\) __ou__ \(preenchido e espécie do documento de referência <> 1\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “21\-Data Escrita*

*     Fiscal do Documento de Referência” é de preenchimento obrigatório quando a espécie do documento de referência = 1\. Para*

*     as espécies 2 ou 3 o campo não deve ser informado*”\)\.   

__Crítica 2__: 

A data informada deve ser uma data válida\. Caso contrário, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*Data Escrita Fiscal do Documento de Referência inválida”*\)\.

__RN22__

__Campo Indicador Pessoa Física/Jurídica do Documento de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 1 \(Nota Fiscal\)\.

  

Quando a espécie do documento de referência = 2 ou 3, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 1\) __ou__ \(preenchido e espécie do documento de referência <> 1\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “22\-Indicador Pessoa*

*      Física/Jurídica do Documento Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de referência*

*      = 1\. Para as espécies 2 ou 3 o campo não deve ser informado*”\)\.   

__Crítica 2__:

O conteúdo informado deve estar de acordo com os indicadores da SAFX04 \('1', '2', ‘3’, ‘4’, ‘5’\)\. Caso contrário, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*Indicador da Pessoa Fisica/Juridica do Documento Fiscal de Referência inválido\.*”\)\.

__RN23__

__Campo Código Pessoa Física/Jurídica do Documento de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 1 \(Nota Fiscal\)\.

  

Quando a espécie do documento de referência = 2 ou 3, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 1\) __ou__ \(preenchido e espécie do documento de referência <> 1\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “23\-Código Pessoa*

*      Física/Jurídica do Documento Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de referência*

*      = 1\. Para as espécies 2 ou 3 o campo não deve ser informado*”\)\.   

__Crítica 2__:

A partir do conteúdo dos campos 22 e 23 \(indicador e código da pessoa fis/jur do documento de referência\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela \(“*O Código da Pessoa Fisica/Juridica do Documento de Referência não esta cadastrado*”\)\.

__RN24__

__Campo Modelo do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 2 \(Cupom Fiscal\)\.

  

Quando a espécie do documento de referência = 1 ou 3, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 2\) __ou__ \(preenchido e espécie do documento de referência <> 2\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “24\-Modelo do*

*     Cupom Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de referência = 2\. Para as*

*     espécies 1 ou 3 o campo não deve ser informado*”\)\.   

__Crítica 2__:

 

Quando preenchido, o código informado será validado na Tabela de Modelos de Documentos Fiscais \(SAFX2024\), e caso não exista, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O Modelo do Cupom Fiscal de Referência deve estar cadastrado na Tabela de Modelos de Documentos Fiscais \(SAFX2024\)*”\.

__RN25__

__Campo Número do Caixa do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 2 \(Cupom Fiscal\)\.

  

Quando a espécie do documento de referência = 1 ou 3, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 2\) __ou__ \(preenchido e espécie do documento de referência <> 2\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “25\-Número do*

*      Caixa do Cupom Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de referência = 2\. Para as*

*     espécies 1 ou 3 o campo não deve ser informado*”\)\.   

__Crítica 2__:

 

A partir do conteúdo dos campos 24 e 25 \(modelo e número do caixa\), será verificada a existência do equipamento na Tabela de Cadastro de Equipamentos ECF \(SAFX2087\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O Número do Caixa do Cupom Fiscal de Referência deve estar cadastrado na Tabela de Cadastro de Equipamentos ECF \(SAFX2087\)*”\.

__RN26__

__Campo COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 2 \(Cupom Fiscal\)\.

  

Quando a espécie do documento de referência = 1 ou 3, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 2\) __ou__ \(preenchido e espécie do documento de referência <> 2\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “26\-COO \(Contador*

*      de Ordem de Operação\) do Cupom Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de*

*      referência = 2\. Para as espécies 1 ou 3 o campo não deve ser informado*”\)\.   

__RN27__

__Campo Data de Emissão do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 2 ou 3 \(Cupom Fiscal ou Cupom Fiscal SAT\)\.

  

Quando a espécie do documento de referência = 1, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 2 ou 3\) __ou__ \(preenchido e espécie do documento de referência = 1\), 

     Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “27\-Data de Emissão*

*     do Cupom Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de referência = 2 ou 3*\. *Para a*

*     espécie 1 o campo não deve ser informado”*\)\.   

__RN28__

__Campo Número do Equipamento SAT do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 3 \(Cupom Fiscal SAT\)\.

  

Quando a espécie do documento de referência = 1 ou 2, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 3\) __ou__ \(preenchido e espécie do documento de referência <> 3\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “28\-Número do*

*      Equipamento SAT do Cupom Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de referência*

*      = 3\. Para as espécies 1 ou 2 o campo não deve ser informado*”\)\.   

__RN29__

__Campo Número do Cupom Fiscal de Referência__

Campo de preenchimento __*obrigatório*__ quando a espécie do documento de referência \(campo 16\) = 3 \(Cupom Fiscal SAT\)\.

  

Quando a espécie do documento de referência = 1 ou 2, este campo *não* deve ser preenchido\. 

__Crítica 1__: 

Se \(não preenchido e espécie do documento de referência = 3\) __ou__ \(preenchido e espécie do documento de referência <> 3\), 

      Neste caso, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*O campo “29\-Número do*

*      Cupom Fiscal de Referência” é de preenchimento obrigatório quando a espécie do documento de referência = 3\. Para as espécies*

*      1 ou 2 o campo não deve ser informado*”\)\.   

__RN30__

__Campo Número do Item do Documento de Referência __

Campo de preenchimento __*obrigatório*__ para todas as espécies de documento de referência \(campo 16 = 1, 2 ou 3\)\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(“*O Número do Item do Documento de Referência não esta preenchido*”\)\.

__Crítica da existência do item do documento fiscal de referência:__

Após a validação dos campos que identificam o item do documento fiscal de referência, será verificada a existência deste item na SAFX08, SAFX994 ou SAFX202, conforme a espécie do documento de referência informada no campo 16\. 

Além de verificar a existência do item do documento de referência, também será verificado se o Produto que consta neste item é realmente o Produto devolvido \(produto que consta na nota de devolução\)\.

As regras destas verificações, assim como as mensagens de erro a serem geradas, quando for o caso, estão descritas na __RN00\.__

__RN31__

__Campo Código Motivo__

Campo de preenchimento __*obrigatório*__\. 

Quando não informado, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O campo Código Motivo deve ser preenchido”*\)\.

O código informado será validado na “Tabela de Códigos de Motivo de Restituição / Complementação de ICMS” \(módulo DW\),      considerando apenas os códigos referentes à UF do estabelecimento \(as duas primeiras posições devem ser = UF do      Estabelecimento\)\. Quando não identificado na   tabela, o registro não será importado, e no log de erros será gravada uma      mensagem \(“*Código Motivo não cadastrado na Tabela de Códigos de Motivo de Restituição/Complementação de ICMS”*\)\.

__RN32__

__Campo Quantidade Convertida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido ou = zeros, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*A quantidade deve ser preenchida com valor maior que zero*”\)\.

<a id="_Hlk25589382"></a>__RN33__

__Campo Unidade de Medida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90149: “*O Campo Unidade de Medida não esta preenchido*\.”\)\.

O código informado deve existir na Tabela das Unidades de Medida \(SAFX2007\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade de medida não existe na tabela \(mensagem padrão código 90150: “*A Unidade de Medida não esta cadastrada*”\)\.

__RN34__

__Campo Valor Unitário Conv:__

Campo de preenchimento __*não obrigatório*__\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campos da EFD correspondes: 12 do C181 e 15 do C186\.

__RN35__

__Campo Valor Unitário ICMS OP Conv:__

Campo de preenchimento __*não obrigatório*__\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campos da EFD correspondes: 17 do C181 e 16 do C186\.

__RN36__

__Campo Valor Unitário Base ICMS ST Conv da Entrada:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de entrada, ou seja, quando a nota de devolução em questão for uma nota de saída \(campo “04\-Movimento Entrada/Saída” = 9\)\.

__Se__ nota de entrada \(campo 04\-Movimento E/S __<>__ 9\) __e__ o campo estiver preenchido,

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem 

    \(“*O campo Valor Unitário Base ICMS\-ST Conv \(Entradas\) deve ser informado apenas nas devoluções de entrada”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 17 do C186

__RN37__

__Campo Valor Unitário ICMS ST Conv da Entrada:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de entrada, ou seja, quando a nota de devolução em questão for uma nota de saída \(campo “04\-Movimento Entrada/Saída” = 9\)\.

__Se__ nota de entrada \(campo 04\-Movimento E/S __<>__ 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem 

     \(“*O campo Valor Unitário ICMS\-ST Conv \(Entradas\) deve ser informado apenas nas devoluções de entrada”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 18 do C186\.

__RN38__

__Campo Valor Unitário FCP ST Conv da Entrada:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de entrada, ou seja, quando a nota de devolução em questão for uma nota de saída \(campo “04\-Movimento Entrada/Saída” = 9\)\.

__Se__ nota de entrada \(campo 04\-Movimento E/S __<>__ 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem

     \(“*O campo Valor Unitário FCP ST Conv \(Entradas\) deve ser informado apenas nas devoluções de entrada”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 19 do C186\.

__RN39__

__Campo Valor Unitário ICMS OP Estoque Conv:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de saída, ou seja, quando a nota de devolução em questão for uma nota de entrada \(campo “04\-Movimento Entrada/Saída” <> 9\)\.

__Se__ nota de saída \(campo 04\-Movimento E/S = 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem

    \(“*O campo Valor Unitário ICMS OP Estoque Conv \(Saídas\) deve ser informado apenas nas devoluções de saída”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 13 do C181\.

__RN40__

__Campo Valor Unitário ICMS ST Estoque Conv:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de saída, ou seja, quando a nota de devolução em questão for uma nota de entrada \(campo “04\-Movimento Entrada/Saída” <> 9\)\.

__Se__ nota de saída \(campo 04\-Movimento E/S = 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem

    \(“*O campo Valor Unitário ICMS ST Estoque Conv \(Saídas\) deve ser informado apenas nas devoluções de saída”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 14 do C181\.

__RN41__

__Campo Valor Unitário FCP ICMS ST Estoque Conv:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de saída, ou seja, quando a nota de devolução em questão for uma nota de entrada \(campo “04\-Movimento Entrada/Saída” <> 9\)\.

__Se__ nota de saída \(campo 04\-Movimento E/S = 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem 

    \(“*O campo Valor Unitário FCP ICMS ST Estoque Conv \(Saídas\) deve ser informado apenas nas devoluções de saída”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 15 do C181\.

__RN42__

__Campo Valor Unitário ICMS na Operação Conv:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de saída, ou seja, quando a nota de devolução em questão for uma nota de entrada \(campo “04\-Movimento Entrada/Saída” <> 9\)\.

__Se__ nota de saída \(campo 04\-Movimento E/S = 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\.  O registro não será importado, e no log de erros será gravada uma mensagem

     \(“*O campo Valor Unitário ICMS OP Conv \(Saídas\) deve ser informado apenas nas devoluções de saída”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 16 do C181\.

__RN43__

__Campo Valor Unitário ICMS ST Conv Rest:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de saída, ou seja, quando a nota de devolução em questão for uma nota de entrada \(campo “04\-Movimento Entrada/Saída” <> 9\)\.

__Se__ nota de saída \(campo 04\-Movimento E/S = 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem

     \(“*O campo Valor Unitário ICMS ST Conv Rest \(Saídas\) deve ser informado apenas nas devoluções de saída”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 18 do C181\.

__RN44__

__Campo Valor Unitário FCP ST Conv Rest:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de saída, ou seja, quando a nota de devolução em questão for uma nota de entrada \(campo “04\-Movimento Entrada/Saída” <> 9\)\.

__Se__ nota de saída \(campo 04\-Movimento E/S = 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem 

     \(“*O campo Valor Unitário FCP ST Conv Rest \(Saídas\) deve ser informado apenas nas devoluções de saída”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 19 do C181\.

__RN45__

__Campo Valor Unitário ICMS ST Conv Compl:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de saída, ou seja, quando a nota de devolução em questão for uma nota de entrada \(campo “04\-Movimento Entrada/Saída” <> 9\)\.

__Se__ nota de saída \(campo 04\-Movimento E/S = 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem

    \(“*O campo Valor Unitário ICMS ST Conv Compl \(Saídas\) deve ser informado apenas nas devoluções de saída”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 20 do C181\.

__RN46__

__Campo Valor Unitário FCP ST Conv Compl:__

Campo de preenchimento __*não obrigatório*__\.

Este campo deve ser preenchido apenas quando se tratar de uma devolução de saída, ou seja, quando a nota de devolução em questão for uma nota de entrada \(campo “04\-Movimento Entrada/Saída” <> 9\)\.

__Se__ nota de saída \(campo 04\-Movimento E/S = 9\) __e__ o campo estiver preenchido

     Nesse caso o campo *não* deve ser preenchido\. O registro não será importado, e no log de erros será gravada uma mensagem

    \(“*O campo Valor Unitário FCP ST Conv Compl \(Saídas\) deve ser informado apenas nas devoluções de saída”*\)\.

Obs\.: Os campos de valor dos registros C181 e C186 que aparecem como não obrigatório no layout \(“OC”\), serão tratados como campos não obrigatórios na SAFX308\.

Campo da EFD corresponde: 21 do C181\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

