# MTZ_AGILIBLUE_Geracao_Meio_Magnetico

- **Fonte:** MTZ_AGILIBLUE_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-02-13
- **Tamanho:** 90 KB

---

THOMSON REUTERS

Municipal

                                  [ÁGILIBlue](http://www.rondonopolis.mt.gov.br/servicos/nfse/infos-web-service-nfse-agiliblue/) 

Declaração de serviços de prestadores estabelecidos fora do município\.

DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-708439

Rosemeire Santos

Criação do validador ÁGILIBlue\. 

MFS\-708439

Rosemeire Santos

Este documento tem como objetivo incluir o município de Rondonópolis/MT, na estrutura do validador “ÁGILIBlue”\.

MFS\-829438    

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__REGRAS DE NEGÓCIO__

__CÓD__

__DESCRIÇÃO__

__MFS/CH__

RN01

__Estrutura de menus do módulo __[__ÁGILIBlue__](http://www.rondonopolis.mt.gov.br/servicos/nfse/infos-web-service-nfse-agiliblue/)__:__

Deverão ser criados os seguintes menus e sub\-menus no módulo [ÁGILIBlue](http://www.rondonopolis.mt.gov.br/servicos/nfse/infos-web-service-nfse-agiliblue/):

- Obrigações
	- Geração do Meio Magnético
	- Geração – Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)
- Janela
- Ajuda 

MFS\-708439

RN02

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST \_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.TXT

__       ST\_AGILIBLUE\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __ST\_AGILIBLUE__: representa a obrigação que está sendo gerada\. 

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração

       __\.TXT__: extensão do arquivo\.

*Exemplo:* ST\_AGILIBLUE\_RONDONOPOLIS\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST \_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\_MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__       DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.TXT

__ST\_AGILIBLUE\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.TXT__, onde:

__        ST\_AGILIBLUE__: representa a obrigação que está sendo gerada\.    

__        MUNICIPIO__: representa o município que está sendo gerado\.   

        __DDMMAAAA__: representa a data inicial da geração\.   

__        MMAAAA:__ mês da competência referente à nota gerada

        __\.TXT__: extensão do arquivo\.

Ex: ST\_AGILIBLUE\_RONDONOPOLIS\_01012014\_122013\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

MFS\-708439

MFS\-839901  
 MFS\-829438    

RN03

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS\-708439

RN04

__Regras referentes à formatação dos registros gerados no meio magnético:__

O arquivo a ser gerado para ser importado no ÁGILIBlue NFS\-e precisa ser no formato texto \(__TXT__\) e na codificação “__UTF\-8__” e apresentar o tipo de registro conforme o layout deste documento\. É obrigatório ter no mínimo 1 registro no arquivo\. 

- 
	1. __Considerações de preenchimento de campos do layout:__
- Campo de formato numérico deverá ser preenchido com zeros à esquerda para completar o tamanho deste\. Preenchendo assim toda a posição disponibilizada para ele no arquivo\. 
- Campo de formato alfanumérico deverá ser preenchido com brancos à direita para completar o tamanho deste\. Preenchendo assim toda a posição disponibilizada para ele no arquivo\. 
	- Para campo que não tenha conteúdo para ser preenchido ao gerar o arquivo, deve seguir as regras abaixo: 

1\. Campo numérico deve ser preenchido com zeros: a\. Se o campo é tamanho N \(005\), deverá ser preenchido com “00000” \(5 zeros\)\. 

2\. Campo alfanumérico deve ser preenchido com espaços\. a\. Se o campo é tamanho A \(005\), deverá ser preenchido com “ “ \(5 espaços em branco\)\. 

MFS\-708439

RN05

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)\.__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Situação <> ‘S’

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS\-708439

RN06

__Regra geral p/ recuperar serviços tomados para o município de Rondonópolis__

\- Recuperar as Notas Fiscais Eletrônico de Serviço, considerando a parametrização da Tela de __“Notas Fiscais Eletrônicas”,__ no Menu Parâmetros por Município com as chaves de __UF__ e __Município__, conforme regras abaixo:

__Notas Fiscais eletrônicas de Serviço Tomado: __

__\- Para Prestadores Dentro do município:__

__\- Se__ parâmetro “__*Prestador Dentro do Município*__” estiver “__marcado__” desconsiderar notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

__\- Se __parâmetro “__*Prestador Dentro do Município*__” estiver “__desmarcado__” considerar as notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\) __ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

Default: Desmarcado

__ \-  Se__ a __UF__ e o __Município __do estabelecimento não estiver parametrizados no Módulo > Parâmetro por Município > no Menu Parâmetros \- na tela de “Notas Fiscais Eletrônicas”, o sistema deverá seguir conforme regra atual, considerando todas as notas\.

MFS\-708439

RN07

__Regra p/ campo Número da nota fiscal de serviço declarada__ 

Identifica o número da nota fiscal de serviço\.

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

Exemplo: 

Número da Nota é 5845, deve ser enviado como: __0000000000000005845 __

Campo obrigatório\.

Tamanho:19

Tipo: Numérico

MFS\-708439

RN08

__Regra p/ campo Série da nota fiscal de serviço declarada__ 

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)\.

Exemplo: 

Série da nota é A1, deve ser preenchido como: “__A1 __“\. Se não tiver, enviar como “ “ \(5 espaços\)\. 

Campo:

Tamanho:05

Tipo: Alfanumérico

MFS\-708439

RN09

__Regra p/ campo Data de emissão __

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

Exemplo: 

Data de emissão é 01/02/2021, deve ser preenchido como: __20210201 __

Campo obrigatório\.

Formato: YYYYMMDD\.

Tamanho: 08

Tipo: Data

MFS\-708439

RN10

__Regra p/ campo Estrutura do serviço__

Preencher o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

Formatos: “__7\.03__” e ‘__38\.01’__

Obrigatório informar a atividade econômica ou CNAE ou Item da lei 116/2003 da nota \(conforme parametrizado pelo município\)\.  Verificar com o município qual estrutura é utilizada\.

Se for Atividade econômica, deve ser preenchido com o conteúdo da tag “CodigoCompleto” conforme documentado no item “4” deste documento\.  Se for as demais estruturas, devem ser utilizados os códigos respectivos \(116/03 ou CNAE\)\. Sempre completar com espaços à direita até completar o tamanho definido do campo \(60 caracteres\)\.

Campo obrigatório\.

Formato: Alfanumérico

Tamanho: 60

MFS\-708439

RN11

__Regra p/ campo Estrutura secundária do serviço \(CNAE\)__

Preencher com o campo COD\_ATIVIDADE da tabela X04\_PESSOA\_FIS\_JUR referente ao Código da Atividade Econômica, __E __caso o campo da tabela citada estiver vazio, buscar o Código da Atividade Econômica da tabela X2018 relacionado ao serviço e Item da lei 116/2003\.

Informe esta opção caso seja obrigatório o vínculo de pelo menos um código CNAE a cada atividade econômica\. Isso é definido pela entidade pública\. Se for preenchido, deve deixar espaços à direita até completar o tamanho definido pelo campo \(40 caracteres\) senão,

preencher com espaços em todo o campo\.

Campo;

Formato: Alfanumérico

Tamanho: 40

MFS\-708439

RN12

__Regra p/ campo Estrutura secundaria de serviço \(Item da Lei 116/2003\)__

Preencher com espaços todo o campo\.

Informe esta opção caso seja obrigatório o vínculo de pelo menos um item da lei 116/2003 a cada atividade econômica definida pela entidade pública\. Isso é definido pela entidade pública\. Se for preenchido, deve deixar espaços à direita até completar o tamanho definido pelo campo \(40 caracteres\) senão, preencher com espaços todo o campo\.

Campo;

Formato: Alfanumérico

Tamanho: 40

MFS\-708439

RN13

__Regra p/ campo Valor total dos serviços__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV \(campo 15 da SAFX09\)\.

Exemplo:

Se o valor for R$ 2\.586,58, deve ser preenchido como: 0000000258658

Campo obrigatório\.

Formato: Numérico

Tamanho: 13

MFS\-708439

RN14

__Regra p/ campo Valor total dos descontos__

Preencher com o somatório do campo VLR\_DESCONTO da tabela DWT\_ITENS\_SERV

Exemplo:

Se o valor for R$ 2\.586,58, deve ser preenchido como: 0000000258658, Se não   houver   valor   de   descontos, deve   ser

preenchido como: 0000000000000

Campo;

Formato: Numérico

Tamanho: 13

MFS\-708439

RN15

__Regra p/ campo Valor total das retenções__

Preencher com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Caso o mesmo não esteja preenchido e se caracterizar retenção pelo prestador, preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Exemplo:

Se o valor for R$ 2\.586,58, deve ser preenchido como: 0000000258658\. Se não   houver   valor   de   descontos, deve   ser

preenchido como: 0000000000000

Campo;

Formato: Numérico

Tamanho: 13

MFS\-708439

RN16

__Regra p/ campo Valor total das deduções da construção civil__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV, campo 59 da SAX09\. Quando o campo 72 IND\_PREST\_SERV da SAFX07 e ou Campo 04 IND\_TP\_SERVICO da SAFX2018 estiver = 1\.

Exemplo:

Se o valor for R$ 2\.586,58, deve ser preenchido como: 0000000258658\. Se não   houver   valor   de   descontos, deve   ser

preenchido como: 0000000000000\.

Campo; 

Formato: Numérico

Tamanho: 13

MFS\-708439

RN17

__Regra p/ campo Prestador de serviços é optante pelo simples nacional__

Preencher com “__1__” se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = “S”, caso contrário, preencher com “__0__”\.

Exemplo: 

1 — Quando for optante do Simples Nacional\.

0 — Quando não for optante do Simples Nacional\.

Campo obrigatório\.

Formato: Numérico

Tamanho: 1

MFS\-708439

RN18

__Regra p/ campo Alíquota do simples nacional__

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV \(campo 34 da SAFX09\) se o campo IND\_SIMPLES\_NAC da tabela SAFX04, referente à pessoa fis/jur cadastrada na nota fiscal for igual a “S”, caso contrário gravar zerado\.

Campo deve conter conteúdo maior que zeros quando o prestador do serviço for optante do Simples Nacional e deve ser preenchido com a alíquota deste na data de emissão da NFS\-e\.

Exemplo:

Se a alíquota for 3,58% deve ser enviado como: 00358, Se não é optante do Simples Nacional, deve ser preenchido como: 00000\.

Campo obrigatório\.

Formato: Numérico

Tamanho: 5

MFS\-708439

RN19

__Regra p/ campo Tipo de prestador de serviço__

Preencher com:

__F__, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota tiver 11 posições;

__J__, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota tiver 14 posições\.

Exemplo:

J — Pessoa jurídica\.

F — Pessoa física\.

Campo; 

Formato: Alfanumérico

Tamanho: 1

MFS\-708439

RN20

__Regra p/ campo CNPJ__

Preencher o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR, referente a pessoa fis/jur cadastrada na nota tiver 14 posições\.

Informar o CNPJ quando o tipo for “Pessoa jurídica”\.

Quando Tipo do prestador do serviço = F, deve ser preenchido como: 00000000000000\.

Campo obrigatório\.

Formato: Numérico

Tamanho: 14

MFS\-708439

RN21

__Regra p/ campo CPF__

Preencher o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR, referente a pessoa fis/jur cadastrada na nota tiver 11 posições\.

Informar o CPF quando o tipo for “Pessoa física”\.

Quando Tipo do prestador do serviço = J, deve ser preenchido como: 00000000000\.

Campo obrigatório\.

Formato: Numérico

Tamanho: 11

MFS\-708439

RN22

__Regra p/ campo Nome / Razão Social__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR, referente à pessoa fis/jur cadastrada na nota fiscal

Obrigatório informar para qualquer tipo de prestador e completar com espaços à direita até completar o tamanho definido do campo \(120 caracteres\)\.

Campo obrigatório\.

Formato:120

Tamanho: Alfanumérico

MFS\-708439

RN23

__Regra p/ campo Nome fantasia__

Preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR, referente à pessoa fis/jur cadastrada na nota fiscal\.

Somente pode ser informado, quando o tipo for “Pessoa jurídica”\. Completar com espaços à direita até completar o tamanho definido do campo \(120 caracteres\) e   caso   não   tenha, informar   120 espaços em branco\.

Campo 

Formato: Alfanumérico

Tamanho: 120

MFS\-708439

RN24

__Regra p/ campo Inscrição estadual__

Preencher com o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR, referente à pessoa fis/jur cadastrada na nota fiscal\.

Somente pode ser informado quando o tipo for “Pessoa jurídica”\. Completar com espaços à direita até completar o tamanho definido do campo \(20 caracteres\) e caso não tenha, informar 20 espaços\.

em branco\.

Campo; 

Formato: Alfanumérico

Tamanho: 20

MFS\-708439

RN25

__Regra p/ campo Sexo__

Preencher fixo com “__0__”, em todas as situações\.

Exemplo: 0 \- Quando for pessoa jurídica\.

Campo;

Formato: Numérico

Tamanho: 1

MFS\-708439

RN26

__Regra p/ campo Tipo de Telefone__

Preencher fixo com “__2__”, em todas as situações\.

Exemplo: 2 – Comercial\.

Campo obrigatório\.

Formato: Numérico

Tamanho: 1

MFS\-708439

RN27

__Regra p/ campo Código DDD__

Preencher com o campo DDD da tabela X04\_PESSOA\_FIS\_JUR, referente à pessoa fis/jur cadastrada na nota fiscal\.

Informar o DDD do telefone\. Se o DDD for 43 deve ser enviado como: 00043\.

Campo obrigatório\.

Formato: Numérico

Tamanho: 5

MFS\-708439

RN28

__Regra p/ campo Número do telefone__

Preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR, referente à pessoa fis/jur cadastrada na nota fiscal\.

Informar o número do telefone\. Deve ser preenchido somente com números e deixando, se necessário, espaços à direita conforme exemplo: “33548965\.

Campo obrigatório\.

Formato: Alfanumérico

Tamanho: 14

MFS\-708439

RN29

__Regra p/ campo Ramal do telefone__

Preencher com 5 espaços\.

Campo obrigatório\.

Formato: Alfanumérico

Tamanho: 5

MFS\-708439

RN30

__Regra p/ campo E\-mail__

Preencher com o campo EMAIL da tabela X04\_PESSOA\_FIS\_JUR, referente à pessoa fis/jur cadastrada na nota fiscal\.

Preencher com conteúdo válido de e\-mail se tiver este para ser informado\. Completar com espaços à direita até completar o tamanho   definido do campo \(300 caracteres\) e caso não tenha, informar 300 espaços em branco\.

Campo; 

Formato: Alfanumérico

Tamanho: 300

MFS\-708439

RN31

__Regra p/ campo Tipo de Endereço__

Preencher fixo com “__5__”, em todas as situações\.

__Exemplo: 5 \- Comercial__

Campo obrigatório\.

Formato: Numérico

Tamanho: 1

MFS\-708439

RN32

__Regra p/ campo CEP__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR, referente a pessoa fis/jur cadastrada na nota fiscal\.

Deve ser preenchido com os 8 números do CEP do logradouro e permitido somente CEP’s do Brasil, sem separador\.

Campo obrigatório\.

Formato: Numérico

Tamanho: 8

MFS\-708439

RN33

__Regra p/ campo Sigla do estado__

Preencher com o campo UF da tabela X04\_PESSOA\_FIS\_JUR, referente a pessoa fis/jur cadastrada na nota fiscal\.

Informar a sigla do estado do endereço\.  Preencher com caracteres maiúsculos conforme exemplos abaixo:

‘PR’ para Paraná\.

‘RJ’ para Rio de Janeiro

Campo obrigatório\.

Formato: Alfanumérico

Tamanho: 2

MFS\-708439

RN34

__Regra p/ campo Munícipio__

Preencher o campo COD\_MUNICIPIO da tabela MUNICIPIO, referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR, a pessoa fis/jur cadastrada na nota fiscal\.

Informar o nome do município do endereço\. Completar com espaços à direita até completar o tamanho definido do campo \(120 caracteres\)\.

Campo obrigatório\.

Formato: Alfanumérico

Tamanho: 120

MFS\-708439

RN35

__Regra p/ campo Distrito__

Preencher com o campo DISTRITO da tabela X04\_PESSOA\_FIS\_JUR, referente a pessoa fis/jur cadastrada na nota fiscal\.

Nome do distrito do município do endereço do prestador do serviço\.  Completar com espaços à direita   até   completar   o   tamanho   definido   do campo \(120 caracteres\) e caso não tenha, informar 120 espaços em branco\.

Campo;

Formato: Alfanumérico

Tamanho: 120

MFS\-708439

RN36

__Regra p/ campo Bairro__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR, referente a pessoa fis/jur cadastrada na nota fiscal\.

Nome do bairro do município do endereço do prestador do serviço\. Completar com espaços à direita até completar o tamanho definido   do campo \(120 caracteres\) e caso não tenha, informar 120 espaços em branco\.

Campo;

Formato: Alfanumérico

Tamanho: 120

MFS\-708439

RN37

Regra p/ campo Código do tipo de Logradouro

Preencher com o código correspondente ao campo Tipo Logradouro da tela de Parâmetros por municípios – Tipo Logradouro Msaf x Tipo Logradouro \(TFIX109\_ PRT\_TP\_LOGRADOURO\_OBRIG\), associado ao tipo de logradouro informado na pessoa fis/jur da nota fiscal \(campo 42\- TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR\)\.

Informar o tipo de logradouro\. Deve ser preenchido com o conteúdo da tag “Codigo” conforme documentado no item “5” deste documento \(não é o 5\. do layout\)\. Se o código do tipo de logradouro for \-205 deve ser enviado como: \-0205

Campo obrigatório\.

Formato: Numérico

Tamanho: 5

MFS\-708439

RN38

__Regra p/ campo Logradouro__

Preencher o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

Nome do logradouro do município do endereço do prestador do serviço\. Completar com espaços à direita até completar o tamanho definido do campo \(120 caracteres\)\.

Campo obrigatório\.

Formato: Alfanumérico

Tamanho: 120

MFS\-708439

RN39

__Regra p/ campo Número do logradouro__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR, referente a pessoa fis/jur cadastrada na nota fiscal\.

Número do logradouro do endereço do prestador do serviço\.  Completar com espaços à direita até completar o tamanho definido do   campo \(10 caracteres\)\.

Campo obrigatório

Formato: Alfanumérico

Tamanho: 10

MFS\-708439

RN40

__Regra p/ campo Complemento__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR, referente a pessoa fis/jur cadastrada na nota fiscal\.

Complemento do endereço do prestador do serviço\.  Completar com espaços à direita até completar o tamanho definido do campo \(300 caracteres\) e caso não tenha não envie nada\.

Campo Opcional

Formato: Alfanumérico

Tamanho: 300

MFS\-708439

### INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__MFS__

__IM01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

MFS\-708439

__IM02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XXXXXX / XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS\-708439

__IM03__

Código IBGE: __7602 – __Município/UF:__ RONDONOPOLIS/MT__

A descrição funcional do módulo será: “Consiste na entrega da Declaração de serviços de prestadores estabelecidos fora do município”\.

MFS\-708439

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

