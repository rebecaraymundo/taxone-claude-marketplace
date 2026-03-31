# MTZ-Job-Servidor-Importacao_SAFX296

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX296.docx
- **Modificado:** 2021-10-21
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX296

__                   Tabela das Informações Complementares das Operações Sujeitas ao ST __

__                                                           \(EFD \- C180, C185 e C380\)__

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS32062

Sped Fiscal – Atualização Legal da versão 1\.13, vigência Jan/2020

Criação da tabela SAFX296 para carga das informações complementares de ST, a serem utilizadas na geração dos registros C180, C185 e C380 do Sped Fiscal\. 

20/11/2019

MFS40615

Andréa Rocha

Alteração da regra dos campos 19, 21 e 22\.

28/10/2020

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX296__ 🡪 vide manual de layout

A SAFX296 é uma tabela complementar da SAFX08 \(Itens dos Documentos Fiscais\)\.

__Campos que compõe a chave da tabela: __Os campos chave são os mesmos campos que compõem a chave da X08, por se tratar de uma tabela complementar, com ocorrência de apenas um registro para cada item da X08\.

A manutenção da tabela é feita na tela de manutenção dos documentos fiscais \(módulo DW\), através da opção “__*Informações Complementares Oper\. ST \(Sped Fiscal\)*__”\.

As informações da SAFX296 são utilizadas na geração do Sped Fiscal, registros C180 \(Entradas\), C185 \(Saídas\) e C380 \(Saídas, modelo 02\)\.

__Crítica da existência do item do documento fiscal:__

Por se tratar de uma tabela complementar à SAFX08, só é permitida a inclusão de informações complementares na SAFX296 quando o item do documento fiscal já existir\. Assim, após a validação dos campos de identificação do item \(campo 01 ao 15\) conforme as regras descritas abaixo, será verificado se o item em questão existe na SAFX08\. Caso não exista, o registro *não* será importado, e no log de erros será gravada uma mensagem de erro \(“*Item do documento fiscal inexistente”*\)\.

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação do item do documento fiscal, para permitir ao usuário a identificação do registro com erro\.

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

Deve ser = “1” ou “2”;

Quando não preenchido, ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 901309: “*O Campo Normal ou Devolução não está preenchido ou preenchido com informação inválida”*\)\.

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

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90132: “*O Número do Item do Documento Fiscal não esta preenchido*\.”\)\.

__RN16__

__Campo Quantidade Convertida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido ou = zeros, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*A quantidade deve ser preenchida com valor maior que zero*”\)\.

<a id="_Hlk25589382"></a>__RN17__

__Campo Unidade de Medida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90149: “*O Campo Unidade de Medida não esta preenchido*\.”\)\.

O código informado deve existir na Tabela das Unidades de Medida \(SAFX2007\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade de medida não existe na tabela \(mensagem padrão código 90150: “*A Unidade de Medida não esta cadastrada*”\)\.

__RN18__

__Campo Valor Unitário Conv:__

Campo de preenchimento __*obrigatório*__\. Deve ser um valor > zeros\.

Quando não preenchido ou = zero, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*O campo Valor Unitário Conv\. deve ser preenchido com valor maior que zero*\.”\)\.

__RN19__

__Campo Valor Unitário ICMS Conv:__

__\[MFS40615\]__

Campo de preenchimento não obrigatório\.

Campo de preenchimento obrigatório apenas quando se tratar de operações de entrada \(campo 04\-Movimento E/S <> 9\)\.

\(Conforme regra do GP vrs 3\.0\.3, registro C180\) 

Nesse caso, quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*O campo Valor Unitário ICMS Conv\. deve ser preenchido nas operações de entrada*\.”\)\.

MFS40615

__RN20__

__Campo 20\-Responsável Retenção \(Entradas\):__

__Se__ operação de entrada \(campo 04\-Movimento E/S __<>__ 9\):

     Nesse caso o campo é de preenchimento obrigatório, e deve ser = “1”, “2” ou “3”\. Caso contrário, o registro não será importado,

    e no log de erros será gravada uma mensagem \(“*O campo Responsável Retenção deve ser preenchido com “1”, “2” ou “3”*\)\.

__Senão__

     Nesse caso o campo *não* deve ser preenchimento\. Caso contrário, o registro não será importado, e no log de erros será 

     gravada uma mensagem \(“*O campo Responsável Retenção deve ser informado apenas nas operações de entrada”*\)\.

__RN21__

__Campo Valor Unitário BC ICMS\-ST Conv\.\(Entradas\):__

__\[MFS40615\]__

__Se__ operação de entrada \(campo 04\-Movimento E/S __<>__ 9\):

     Campo de preenchimento não obrigatório\.

     Nesse caso o campo é de preenchimento obrigatório e deve ser um valor > zeros\. Quando não informado ou = 0, o registro não

     será importado, e no log de erros será gravada uma mensagem \(“*O campo Valor Unitário BC ICMS\-ST Conv \(Entradas\) deve *

*     ser preenchido com valor maior que zero”*\)\.

__Senão__

     Nesse caso o campo *não* deve ser preenchimento\. Caso contrário, o registro não será importado, e no log de erros será 

     gravada uma mensagem \(“*O campo Valor Unitário BC ICMS\-ST Conv \(Entradas\) deve ser informado apenas nas operações*

*     de entrada”*\)\.

MFS40615

__RN22__

__Campo Valor Unitário ICMS\-ST Conv\. \(Entradas\):__

__\[MFS40615\]__

__Se__ operação de entrada \(campo 04\-Movimento E/S __<>__ 9\):

     Campo de preenchimento não obrigatório\.

     Nesse caso o campo é de preenchimento obrigatório e deve ser um valor > zeros\. Quando não informado ou = 0, o registro não

     será importado, e no log de erros será gravada uma mensagem \(“*O campo Valor Unitário ICMS\-ST Conv \(Entradas\) deve ser*

*     preenchido com valor maior que zero”*\)\.

__Senão__

     Nesse caso o campo *não* deve ser preenchimento\. Caso contrário, o registro não será importado, e no log de erros será 

     gravada uma mensagem \(“*O campo Valor Unitário ICMS\-ST Conv \(Entradas\) deve ser informado apenas nas operações*

*     de entrada”*\)\.

MFS40615

__RN23__

__Campo Valor Unitário FCP\-ST Conv\. \(Entradas\):__

__ __

Este campo pode ser informado *apenas* nas entradas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas saídas, não deve ser preenchido\.

__Se__ operação de saída \(campo 04\-Movimento E/S __=__ 9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário FCP\-ST *

*    Conv \(Entradas\) deve ser informado apenas nas operações de entrada”*\)\.

__RN24__

__Campo 24\-Código Motivo \(Saídas\):__

__Se__ operação de entrada \(campo 04\-Movimento E/S __<>__ 9\):

     Nesse caso o campo *não* deve ser preenchimento\. Caso contrário, o registro não será importado, e no log de erros será 

     gravada uma mensagem \(“*O campo Código Motivo \(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

__Senão__

     Nesse caso o campo é de preenchimento obrigatório\. Quando não informado, o registro não será importado, e no log de erros 

     será gravada uma mensagem \(“*O campo Código Motivo \(Saídas\) deve ser preenchido*\)\. 

     O código informado será validado na “Tabela de Códigos de Motivo de Restituição / Complementação de ICMS” \(módulo DW\),

     considerando apenas os códigos referentes à UF do estabelecimento \(as duas primeiras posições devem ser = UF do

     Estabelecimento\)\. Quando não identificado na   tabela, o registro não será importado, e no log de erros será gravada uma

     mensagem \(“*Código Motivo \(Saídas\) não cadastrado na Tabela de Códigos de Motivo de Restituição/Complementação de ICMS”*\)\.

__RN25__

__Campo Valor Unitário ICMS na Oper\. Conv \(Saídas\):__

Este campo pode ser informado *apenas* nas saídas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas entradas, não deve ser preenchido\.

__Se__ operação de entrada \(campo 04\-Movimento E/S __<> __9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário ICMS na Oper\. *

*    Conv \(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

__RN26__

__Campo Valor Unitário ICMS Estoque Conv \(Saídas\):__

Este campo pode ser informado *apenas* nas saídas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas entradas, não deve ser preenchido\.

__Se__ operação de entrada \(campo 04\-Movimento E/S __<> __9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário ICMS Estoque *

*    Conv \(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

__RN27__

__Campo Valor Unitário ICMS\-ST Estoque Conv \(Saídas\):__

Este campo pode ser informado *apenas* nas saídas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas entradas, não deve ser preenchido\.

__Se__ operação de entrada \(campo 04\-Movimento E/S __<> __9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário ICMS\-ST  *

*    Estoque Conv \(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

__RN28__

__Campo Valor Unitário FCP\-ST Estoque Conv \(Saídas\):__

Este campo pode ser informado *apenas* nas saídas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas entradas, não deve ser preenchido\.

__Se__ operação de entrada \(campo 04\-Movimento E/S __<> __9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário FCP\-ST*

*    Estoque Conv \(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

__RN29__

__Campo Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\):__

Este campo pode ser informado *apenas* nas saídas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas entradas, não deve ser preenchido\.

__Se__ operação de entrada \(campo 04\-Movimento E/S __<> __9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário ICMS\-ST*

*    Conv\.Rest\.\(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

__RN30__

__Campo Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\):__

Este campo pode ser informado *apenas* nas saídas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas entradas, não deve ser preenchido\.

__Se__ operação de entrada \(campo 04\-Movimento E/S __<> __9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário FCP\-ST*

*    Conv\.Rest\.\(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

__RN31__

__Campo Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\):__

Este campo pode ser informado *apenas* nas saídas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas entradas, não deve ser preenchido\.

__Se__ operação de entrada \(campo 04\-Movimento E/S __<> __9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário ICMS\-ST*

*    Conv\.Compl\.\(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

__RN32__

__Campo Valor Unitário FCP\-ST Conv\. Compl\. \(Saídas\):__

Este campo pode ser informado *apenas* nas saídas, mas seu preenchimento *não* é obrigatório \(conforme regra do GP vrs 3\.0\.3\)\.

Nas entradas, não deve ser preenchido\.

__Se__ operação de entrada \(campo 04\-Movimento E/S __<> __9\) __e__ o campo estiver preenchido,

     Nesse caso o registro não será importado, e no log de erros será gravada uma mensagem: \(“*O campo Valor Unitário FCP\-ST*

*    Conv\.Compl\.\(Saídas\) deve ser informado apenas nas operações de saída”*\)\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

