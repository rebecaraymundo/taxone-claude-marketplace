# MTZ_DMS_Anchieta_Geracao_Meio_Magnetico

- **Fonte:** MTZ_DMS_Anchieta_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-12-16
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Municipal

DMS ANCHIETA

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS4354

Julyana Perrucini

Criação de validador para município\.

MFS17897

João Henrique 

Alteração do validador para genérico com a inclusão dos municípios: Teixeira de Freitas\-BA e Três Corações\- MG\.

MFS19796

João Henrique

Inclusão do município de Cachoeiro de Itapemirim\-ES no validador DMS EL\.

MFS20493

João Henrique

Inclusão do município de Ibirité\-MG no validador DMS EL\.

MFS\-22855

Julyana Perrucini

Este documento tem como objetivo a inclusão do município de Itamaraju/ BA no validador DMS EL\.

MFS612426

Rogério Ohashi

Este documento tem o objetivo de incluir tratamentos para os campos de Alíquota e Base de ISS, para considerar os Campos de ISS Retido \(RN12 e RN13\)\.

__MFS\-669984__

Rosemeire Santos

Este documento tem o objetivo de incluir, os novos campos “Tipo de Recolhimento” e Código do Serviço, conforme indicado no manual layout do município de Três Corações/MG\.

__MFS\-912021__

Rafael Fabiano

Este documento tem como objetivo a inclusão do município de João Monlevade/MG no validador DMS ANCHIETA\.

MFS\-829438      

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Anchieta deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Anchieta: “Consiste na entrega das informações sobre os serviços tomados do município de Anchieta”\.

MFS4354

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “ES” e ao código de município do IBGE igual a “409” \(Anchieta\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Anchieta, Espírito Santo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS4354

RN03

__Estrutura de menus do módulo DMS:__

Deverão ser criado o seguinte menu e sub\-menus no módulo DMS:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__

MFS4354

RN04

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST \_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__       DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__ST\_DMS\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração

__MUNICIPIO__: representa o município que está sendo gerado\.

__ST\_DMS__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

__\.TXT__: extensão do arquivo\.

Ex: ST\_DMS\_ANCHIETA\_01012013\.TXT

MFS4354  
MFS\-829438    

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município de Anchieta, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS4354

RN06

__Regras referentes à formatação dos registros gerados no meio magnético:__

Abaixo seguem algumas formatações de dados que devem ser seguidas para geração correta na estrutura dos arquivos:

O arquivo a ser gerado para importação dever ser no formato __‘TXT’\.__

__Campo tipo Data__

Campos tipo Data deve ser preenchidos no seguinte formato: “AAAA\-MM\-DD”\. Deverá ter um tamanho fixo de 10 caracteres, incluindo separador\.

__Campo de Valores Decimais__

Os valores decimais devem ser no formato: “__0\.0000”__\. O campo deverá ter quatro casas decimais, separadas por ponto \(“\.”\), sem agrupamento de milhares\. Exemplo: 1\.500,00 = 1500\.0000\.

__Campo tipo Numérico__

Campo formado somente por caracteres numéricos\. Todos os campos do tipo numérico serão preenchidos alinhados pela direita\. Se necessário, serão preenchidos com zeros à esquerda até completar seu tamanho máximo\.

__Campo tipo Texto__

Todos os campos do tipo texto serão preenchidos alinhados pela esquerda\. Se necessário, serão preenchidos com espaços em branco à direita até completar seu tamanho máximo\.

Os campos deverão ser separados por ponto e vírgula \(__;__\) e as linhas separadas por quebras de linhas\. 

MFS4354

RN07

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)\.__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS4354

RN08

__Regra p/ campo Situação Fiscal__

Deverá preencher com uma das situações abaixo:

__“2”__ \- Simples Nacional\. Verificar se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = “S”;

__“3__ “\- ISS Construção Civil\. Verificar se o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘__1__’, referente ao serviço cadastrado na nota;

__“5”__ \- Não Incidência\. Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”;

__“4”__ \- Microempreendedor\. Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR = ‘04’;

__“1”__ \- ISS Normal\. Preencher com 1, quando nenhuma das opções anteriores forem verdadeiras\.

Campo obrigatório\.

Tamanho: 1

Tipo: Numérico

MFS4354

RN09

__Regra p/ campo Número da Nota__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

Se ultrapassar 10 posições, truncar à esquerda e emitir a mensagem de log: “Número da Nota ultrapassa tamanho permitido pelo layout da obrigação, foram consideradas as 10 últimas posições da nota fiscal\.”\. <<Nº NF>>, <<>Data Fiscal>>, <<Fís\./Jur\.>>\.

Campo obrigatório\.

Tamanho: 10

Tipo: Numérico

MFS4354

RN10

__Regra p/ campo Data de Emissão__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

Campo obrigatório\.

Tamanho: 10

Tipo: Data

MFS4354

RN11

__Regra p/ campo Data de Pagamento__

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL \(campo 175 da SAFX07\)\. 

__Tratamento:__

Se caso o campo estiver em branco, ou a data for menor que a data de emissão, deverá preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

Campo obrigatório\.

Tamanho: 10

Tipo: Data

MFS4354

RN12

__Regra p/ campo Alíquota da Nota__

__\[ALTERAÇÃO\-MSF612426\] __Tratamento na Regra para considerar os Campos de ISS Retido

Preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV

 Senão

     Preencher com o campo VLR\_ALIQ\_ISS da tabela DWT\_ITENS\_SERV\.

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\. 

__Tratamento:__

Truncar as duas últimas posições, pois o valor decimal deve ser gerado com duas casas decimais e sem símbolo de percentual\.

Conforme Situação Fiscal e Serviço Prestado devem ser informados as alíquotas entre 2,00% e 5,00%\. Exemplos: 2,00% = 2\.00   /    2,75% = 2\.75    /    5,00% \- 5\.00\. 

Campo obrigatório\.

Tamanho máximo: Não se aplica\. O valor decimal de alíquota deve ser no formato: “__0\.00”__\.

Tipo: Decimal

MFS4354

MFS612426

RN13

__Regra p/ campo Base de Cálculo__

__\[ALTERAÇÃO\-MFS612426\] __Tratamento na Regra para considerar os Campos de ISS Retido

__Preencher__ com o campo VLR\_BASE\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

 __Se__ o campo VLR\_BASE\_ISS\_RETIDO estiver vazio ou igual à 0

      __Preencher__ com o campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV

Preencher com o campo BASE\_ISS da tabela DWT\_ITENS\_SERV \(campo 39 da SAFX09\)\.

Tratamento:

Truncar as cinco primeiras posições,

Campo obrigatório\.

Tamanho máximo: Não se aplica\. Os valores decimais devem ser no formato: “0\.0000”\.

Tipo: Decimal

MFS4354

MFS612426

RN14

__Regra p/ campo Valor da Nota__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV \(campo 15 da SAFX09\)\.

Campo obrigatório\.

Tamanho máximo: Não se aplica\. Os valores decimais devem ser no formato: “__0\.0000”__\.

Tipo: Decimal 

MFS4354

RN15

__Regra p/ campo CPF / CNPJ Prestador__

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório\.

Tamanho: 11 a 14 posições\.

Tipo: Numérico

MFS4354

RN16

__Regra p/ campo Nome / Razão Social Prestador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 05 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

__Tratamento:__

Se ultrapassar 50 posições, truncar à direita\.

Campo obrigatório\.

Tipo: Texto

Tamanho: 50 posições

MFS4354

RN17

__Regra p/ campo Valor do Material__

Preencher com o campo VLR\_MAT\_PROP \+ VLR\_MAT\_TERC \(campos 186 \+ 187\) da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

Se o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’, referente ao serviço cadastrado na nota fiscal, preencher com zeros\.

Campo não obrigatório\.

Tamanho máximo: Não se aplica\. Os valores decimais devem ser no formato: “__0\.0000”__\.

Tipo: Decimal

MFS4354

RN18

__Regra p/ campo CPF / CNPJ Tomador__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

Campo obrigatório\.

Tamanho: 14 posições

Tipo: Numérico

MFS4354

RN19

__Regra p/ campo Tipo de Nota Fiscal__

Preencher com “__E__” quando o 	Modelo do Documento for igual a “55” \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU __o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\), referente ao modelo ou tipo de documento cadastrado na nota fiscal, caso contrário preencher com “__N__”\.

Campo obrigatório\.

Tamanho: 1

Tipo: Texto

MFS4354

RN20

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Teixeira de Freitas deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Teixeira de Freitas: “Consiste na entrega das informações sobre os serviços tomados do município de Teixeira de Freitas”\.

MFS17897

RN21

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “BA” e ao código de município do IBGE igual a “31350” \(Teixeira de Freitas\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Teixeira de Freitas, Bahia\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS17897

RN22

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Três Corações deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Três Corações: “Consiste na entrega das informações sobre os serviços tomados do município de Três Corações”\.

MFS17897

RN23

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “69307” \(Três Corações\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Três Corações, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS17897

RN24

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Cachoeiro de Itapemirim deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste na entrega das informações sobre os serviços tomados do município de Cachoeiro de Itapemirim”\.

MFS19796

RN25

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “ES” e ao código de município do IBGE igual a “1209” \(Cachoeiro de Itapemirim\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Cachoeiro de Itapemirim, Espírito Santo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS19796

RN26

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Ibirité deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste na entrega das informações sobre os serviços tomados do município de Ibirité”\.

MFS20493

RN27

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “29806” \(Ibirité\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Ibirité, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS20493

RN28

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Itamaraju deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste na entrega das informações sobre os serviços tomados do município de Itamaraju”\.

MFS\-22855

RN29

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “BA” e ao código de município do IBGE igual a “15601” \(Itamaraju\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Itamaraju, Bahia\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS\-22855

RN30

__Regra p/ campo Tipo de Recolhimento__

Informar __“R”__ para notas fiscais Retidas na Fonte e __“N”__ para notas fiscais Não Retidas, desde que seu município possibilite informar o tipo de recolhimento\. Quando não informado assume o valor __“R”\. __

Preencher com:

__“R” \- Sim\.__

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”; __OU__
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” \(campo 05 da SAFX2098\) para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO; __OU__
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) está preenchido\. 

Senão, preencher com:

__“N” \- Não\.__

Campo Opcional\.

Tamanho: 1

Tipo: Texto

__MFS\-669984__

RN31

__Regra p/ campo Código do Serviço__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

Formato: NN\.NN

__Tratamento:__

Para os códigos iniciados de 1 a 9, deve\-se manter o 0 \(zero\) à esquerda\. 

Exemplos: 01\.01,14\.01 e 17\.02\. 

Campo Opcional\.

Tamanho: 5

Tipo: Caracter

__MFS\-669984__

RN32

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo João Monlevade deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste na entrega das informações sobre os serviços tomados do município de João Monlevade”\.

__MFS\-912021__

RN33

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “36207” \(João Monlevade\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de João Monlevade, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

__MFS\-912021__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

