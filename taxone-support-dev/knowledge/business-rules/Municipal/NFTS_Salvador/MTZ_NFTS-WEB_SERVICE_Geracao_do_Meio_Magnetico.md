# MTZ_NFTS-WEB SERVICE_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_NFTS-WEB SERVICE_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-12-29
- **Tamanho:** 127 KB

---

### NFTS WEB SERVICE \- GERAÇÃO DO MEIO MAGNÉTICO

__                                                  DOCUMENTO DE REQUISITO__

__Data__

__*MFS*__

__Nome__

__Descrição__

05/12/2025

MFS\-895592

Rosemeire Santos

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador NFTS SALVADOR, via Web Service\.

 

### REGRAS DE NEGÓCIOS

###### __Regras__

###### __DESCRIÇÃO__

__MFS__

RN01

__Estrutura de menus do módulo NFTS SALVADOR:__

Deverão ser criado o seguinte menu e sub\-menus no módulo NFTS SALVADOR:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda

__MFS\-895592__

RN02

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

Quando o parâmetro ‘__Quebrar Arquivos por Data de Emissão__’ estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\.XML__, onde:

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

       __\.XML__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_122025\.XML

Quando o parâmetro ‘Quebrar Arquivos por Data de Emissão’ estiver marcado, deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser conforme abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\_MMAAAA\.XML__, onde:

       __MMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

       __\.XML__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012025\_012025\.XML

Obs\.: Neste caso o arquivo normal__ também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__MFS\-895592__

RN03

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox, por default desmarcado\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município em questão, que estejam licenciados\.

__MFS\-895592__

RN04

__Regras de formatação dos registros gerados no meio magnético:__

Campos que representam CPF e CNPJ \(respectivamente 11 e 14 caracteres\) devem ser informados com o tamanho fixo previsto, sem formatação e com o preenchimento dos zeros não significativos; 

Campos numéricos que representam valores e quantidades são de tamanho variável, respeitando o tamanho máximo previsto para o campo e a quantidade de casas decimais \(quando houver\)\. 

O preenchimento de zeros não significativos causa erro de validação do Schema XML\. 

Os campos numéricos devem ser informados sem o separador de milhar, com uso do ponto decimal para indicar a parte fracionária \(quando houver\) respeitando\-se a quantidade de dígitos prevista no layout; 

 As datas devem ser informadas no formato “AAAA\-MM\-DD”\. 

Para reduzir o tamanho final das mensagens XML alguns cuidados de programação deverão ser assumidos: 

 Na geração das mensagens XML, excetuados os campos identificados como obrigatórios no respectivo Schema XML, não incluir as TAGs de campos zerados \(para campos tipo numérico\) ou vazios \(para campos tipo caractere\); 

Não incluir "espaços" no início e/ou no final de campos alfanuméricos; 

Não incluir comentários na mensagem XML; 

Não incluir anotação e documentação na mensagem XML \(TAG annotation e TAG documentation\); 

Não incluir caracteres de formatação na mensagem XML: “LF” \(Line Feed ou salto de linha, caractere ASCII 10\), "CR" \(Carriage Return ou retorno do carro, caractere ASCII 13\), "tab", \(caractere de "espaço" entre as TAGs\)\.

__MFS\-895592__

RN05

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)__

Considerar todas as notas com as seguintes características:

- Documentos de entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2, 3 e 9 \(RPA\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência informado na tela de geração
- Considerar notas canceladas\.

 Recuperar as Notas Fiscais Eletrônico de Serviço, considerando a parametrização da Tela de __“Notas Fiscais Eletrônicas”,__ no Menu Parâmetros por Município com as chaves de __UF__ e __Município__, conforme regras abaixo:

__Notas Fiscais eletrônicas de Serviço Tomado: __

__\- Para Prestadores Dentro do município:__

__\- Se__ parâmetro “__*Prestador Dentro do Município*__” estiver “__marcado__” desconsiderar notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

__\- Se __parâmetro “__*Prestador Dentro do Município*__” estiver “__desmarcado__” considerar as notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\) __ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

Default: Desmarcado

__ \-  Se__ a __UF__ e o __Município __do estabelecimento não estiver parametrizados no Módulo > Parâmetro por Município > no Menu Parâmetros \- na tela de “Notas Fiscais Eletrônicas”, o sistema deverá seguir conforme regra atual, considerando todas as notas\.

__MFS\-895592__

RN06

__Estrutura do Arquivo:__

<PedidoEnvioLoteNFTS xmlns:xsd="http://www\.w3\.org/2001/XMLSchema" xmlns:xsi="http://www\.w3\.org/2001/XMLSchema\-instance" xmlns="https://nfse\.salvador\.ba\.gov\.br/nfts">

<Cabecalho xmlns="" Versao="1">

<Remetente>

<CPFCNPJ>

<CNPJ>57529050000188</CNPJ>

</CPFCNPJ>

</Remetente>

<transacao>false</transacao>

<dtInicio>2014\-10\-01</dtInicio>

<dtFim>2014\-10\-03</dtFim>

<QtdNFTS>3</QtdNFTS>

<ValorTotalServicos>300</ValorTotalServicos>

<ValorTotalDeducoes>0</ValorTotalDeducoes>

</Cabecalho>

<NFTS xmlns="">

<TipoDocumento>01</TipoDocumento>

<ChaveDocumento>

<InscricaoMunicipal>13580200127</InscricaoMunicipal>

<SerieNFTS>A</SerieNFTS>

<NumeroDocumento>202</NumeroDocumento>

</ChaveDocumento>

<DataPrestacao>2014\-10\-02</DataPrestacao>

<StatusNFTS>N</StatusNFTS>

<TributacaoNFTS>T</TributacaoNFTS>

<ValorServicos>100</ValorServicos>

<ValorDeducoes>0</ValorDeducoes>

<CodigoServico>103</CodigoServico>

<AliquotaServicos>0\.03</AliquotaServicos>

<ISSRetidoTomador>false</ISSRetidoTomador>

<Prestador>

<CPFCNPJ>

<CNPJ>32250824000106</CNPJ>

</CPFCNPJ>

<RazaoSocialPrestador>Prestador Teste</RazaoSocialPrestador>

<Endereco>

<NumeroEndereco>100</NumeroEndereco>

<CEP>44020200</CEP>

</Endereco>

<Email>jose@uol\.com\.br</Email>

</Prestador>

<RegimeTributacao>0</RegimeTributacao>

<Discriminacao>Emissao de NFTS</Discriminacao>

<TipoNFTS>1</TipoNFTS>

<Assinatura> Va\+6RyBDOUAy7/VUW2PW3m663sL2mfioNTeJ7CJVA

E1VA/UO4/R68bjBo0oiZV3x\+bew\+xTU\+4tFTIctGkHXc6gDWCzqKnfFR

cV2qDR0cOSMRsFU2ZkQWZJ6S6xSoYkwAf65tECRRty31RhvLUJ4G

D/nBdyH/IMBRi0TlP/ZQwCJ24cs4CMPq4ZltQBA5WXPUYyeN0sbnyvf

5iwMuYCYwEo0AH2yNwHQ/2iiuz5lv2NnKPxMdGUYrFf0OVQNDiEwve

dWymyIMpoVS\+DHD/xizLZ1MrGBD/udG8oxBwYCmga952RJOC956w/iPp2BPgZnD/G/lOLLu38/s7tA0hH6bQ==</Assinatura>

__MFS\-895592__

RN07

__Regra para tag <PedidoEnvioLoteNFTS xmlns> __Tag relacionada à formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: ‘__<PedidoEnvioLoteNFTS xmlns>’\.__

TAG obrigatória\.

__MFS\-895592__

RN08

__Regra p/ tag <Cabecalho xmlns="" Versao="1">__

Identifica o layout do arquivo\. Preencher com o conteúdo fixo: “__1\.00”__ 

Tag obrigatório\.

__MFS\-895592__

RN09

__Regra para tag < Remetente > __Tag relacionada à abertura da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __< Remetente>\.__

__MFS\-895592__

RN10

__Regra p/ tag <CPFCNPJ> __Tag relacionada à abertura dos dados de cadastro do tomador do serviço\.

TAG obrigatória\.

__MFS\-895592__

RN11

__Regra p/ tag <CPFCNPJ></CNPJ>__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

Tag obrigatória\.

Tipo Alfanumérico

__MFS\-895592__

RN12

__Regra p/ tag <transacao></transacao>__

False \- As NFTS válidos serão emitidas, mesmo que ocorram eventos de erro durante processamento de outras NFTS deste lote\.

Tag obrigatória\.

__MFS\-895592__

RN13

__Regra p/ tag <dtInicio></dtInicio>__

Preencher com o campo “Data Inicial” da tela de geração do meio magnético\.

__Formato: __AAAA\-MM\-DD

Tag 

obrigatória\.

__MFS\-895592__

RN14

__Regra p/ tag <dtFim> </dtFim>__

Preencher com Data Final da tela de geração do meio magnético\.

__Formato: __AAAA\-MM\-DD

Tag obrigatória\.

__MFS\-895592__

RN15

__Regra p/ tag <QtdNFTS> </QtdNFTS>__

Total de NFTS contidos na mensagem XML\.

Tipo Numérico\.

Tag obrigatória\.

__MFS\-895592__

RN16

__Regra p/ tag <ValorTotalServicos> </ValorTotalServicos>__

Preencher com o somatório das NFTS\.

Valor total dos serviços das NFTS contidos na mensagem XML\.

Tipo Numérico\.

Tag obrigatória\.

__MFS\-895592__

RN17

__Regra p/ tag <ValorTotalDeducoes> </ValorTotalDeducoes>__

Preencher com o resultado da somatória das NFTS\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: < ValorTotalDeducoes >0</ ValorTotalDeducoes >

Tipo Numérico\.

Tag obrigatória\.

__MFS\-895592__

RN18

__Regra p/ tag </Cabecalho> __Tag relacionada ao fechamento cabeçalho\.

Tag obrigatória

__MFS\-895592__

RN19

__Regra p/ tag <NFTS xmlns="">__

Tag obrigatória

__MFS\-895592__

RN20

__Regra p/ tag <TipoDocumento> </TipoDocumento>  __

Preencher com o tipo de NFTS:  01 – Documento fiscal emitido por outro município;

Tipo Alfanumérico\.  

Tag 

obrigatória\.

__MFS\-895592__

RN21

__Regra p/ tag <ChaveDocumento> __Tag relacionada abertura a chave do documento fiscal\.

Tipo Alfanumérico\.  

Tag 

obrigatória\.

__MFS\-895592__

RN22

__Regra p/ tag <InscricaoMunicipal> </InscricaoMunicipal>__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da SAFX04, campo 09\.

Tipo Alfanumérico

Tag 

obrigatória\.

__MFS\-895592__

RN23

__Regra p/ tag <SerieNFTS> </SerieNFTS>__

Preencher com o conteúdo do campo SERIE\_DOCFIS da SAFX07, campo 09\.

Tipo Alfanumérico\.  

Tag 

obrigatória\.

__MFS\-895592__

RN24

__Regra p/ tag <NumeroDocumento> </NumeroDocumento> __

Preencher com o conteúdo do campo NUM\_DOCFIS da SAFX07, desconsiderando zeros à esquerda\.

Tipo Numérico\.

Tag 

obrigatória\.

__MFS\-895592__

RN25

__Regra p/ tag </ChaveDocumento> __Tag relacionada fechamento a chave do documento fiscal\.

Tag 

obrigatório\.

__MFS\-895592__

RN26

__Regra p/ tag <DataPrestacao> </DataPrestacao>__

Preencher com o conteúdo do campo DATA\_EMISSAO da SAFX07\.

Formato: AAAA\-MM\-DD

Tipo Alfanumérico\.

Tag 

obrigatória\.

__MFS\-895592__

RN27

__Regra p/ tag <StatusNFTS> </StatusNFTS>__

Preencher com o conteúdo do campo SITUACAO da SAFX07\.

Deverá preencher com uma das opções abaixo:

__N – Normal__

Se campo SITUACAO = __“N”__ da SAFX07\.

__C – Cancelada__

Se o campo SITUACAO = __“S” __da SAFX07

Tipo Alfanumérico

Tag 

obrigatória\.

__MFS\-895592__

RN28

__Regra p/ tag <TributacaoNFTS> </TributacaoNFTS>__

Deverá preencher com uma das opções abaixo:

__T – Operação Normal__

Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “471”, __preencher com “T’;__

__Ou__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”, __preencher com “T’;__

__I – Imune__

Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”, __preencher ‘I’__;

__J – ISS suspenso por decisão judicial__

Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”, __preencher com ‘J’__;

Tag 

obrigatória 

__MFS\-895592__

RN29

__Regra p/ tag <ValorServicos> </ValorServicos>__

Preencher com o conteúdo do campo VLR\_TOT da tabela SAFX09\.__ __

Tipo Numérico

Tag 

obrigatória\.

__MFS\-895592__

RN30

__Regra p/ tag <ValorDeducoes>0</ValorDeducoes>__

Preencher com o conteúdo do campo VLR\_DEDUCAO\_ISS da SAFX09\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <ValorDeducao>0</ ValorDeducao>

Tipo Numérico

Tag obrigatória\.

__MFS\-895592__

RN31

__Regra p/ tag <CodigoServico> </CodigoServico>__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

Formato:103/1701

Tipo Alfanumérico\.

 

Tag 

obrigatória

__MFS\-895592__

RN32

__Regra p/ tag <AliquotaServicos> </AliquotaServicos>__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela SAFX 09, campo 32\.

Se o campo ALIQ\_TRIBUTO\_ISS não estiver preenchido ou estiver com zeros\. Então 

Preencher com o campo VLR\_ALIQ\_ISS\_RETIDO \(campo 97 da SAFX09\)\.

Caso não houver valor informado, preencher 0\.00

<AliquotaServicos>0\.03</AliquotaServicos>

Tipo Numérico\.

Tag O

brigatória\.

__MFS\-895592__

RN33

__Regra p/ tag <ISSRetidoTomador> </ISSRetidoTomador>__

__Informe a retenção:__ True – ISS retido pelo tomador; False – NFTS sem ISS retido\.

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

__Preencher com__ “__true”__:

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__ 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, __preencher com “false”\.__ 

Tipo Alfanumérico\.

 Tag 

obrigatória\.

__MFS\-895592__

RN34

__Regra p/ tag <Prestador> __Tag relacionada a abertura dos dados do prestador

Tag obrigatória\.

__MFS\-895592__

RN35

__	Regra p/ tag <CPFCNPJ> __Tag relacionada à abertura dos dados de cadastro do prestador do serviço\.

TAG obrigatória\.

__MFS\-895592__

RN36

__Regra p/ tag <CPFCNPJ> </CPFCNPJ>__

Nesse campo será informado o CPF/CNPJ do prestador do serviço\. Preencher com o conteúdo do campo __06 \-__ __CPF\_CGC__ da tabela __SAFX04\.__

Para o prestador de serviço estrangeiro, não enviar esta TAG\.

Tipo Alfanumérico

Tag 

obrigatória\.

__MFS\-895592__

RN37

__Regra p/ tag </CPFCNPJ> __Tag de fechamento do CPF/CNPJ do prestador\.

Tag 

obrigatória\.

__MFS\-895592__

RN38

__Regra p/ tag <RazaoSocialPrestador> </RazaoSocialPrestador>__

Nesse campo será informado a razão social do Prestador de serviços\. Preencher com o campo __05 \- RAZAO\_SOCIAL__ da tabela __SAFX04__\.

Tag 

obrigatória\.

__MFS\-895592__

RN39

__Regra p/ tag <Endereco> __Tag de abertura do endereço do pescador\.

Tag 

obrigatório\.

__MFS\-895592__

RN40

__Regra p/ tag <NumeroEndereco> </NumeroEndereco>__

Nesse campo será informado o número do endereço do Prestador de serviços\. Preencher com o campo __13 \- NUM\_ENDERECO__ da tabela __SAFX04__\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <NúmeroEndereco>0</NumeroEndereco>

Tipo Número

Tag 

obrigatória\.

__MFS\-895592__

RN41

__Regra p/ tag <CEP> </CEP>__

Nesse campo será informado o CEP do endereço do Prestador de serviços\. Preencher com o campo __20 \- CEP__ da tabela __SAFX04__\.

Formato: <CEP>44020200</CEP>

Tipo Numérico

Tag 

obrigatória\.

__MFS\-895592__

RN42

__Regra p/ tag </Endereco> __Tag relacionado ao fechamento do endereço prestador\.

Tag 

obrigatória\.

__MFS\-895592__

RN43

__Regra p/ tag <Email> </Email>__

Nesse campo será informado o e\-mail do endereço do Prestador de serviços\. Preencher com o campo __40 – E\_MAIL__ da tabela __SAFX04__\.

Tag obrigatória\. 

__MFS\-895592__

__Regra p/ tag </Prestador> __Tag relacionada ao fechamento dos dados do prestador

__MFS\-895592__

RN44

__Regra p/ tag <RegimeTributacao> </RegimeTributacao>__

Preencher com o tipo do regime de tributação abaixo:

__0 – Normal;__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “__03 \- Empresa Normal, __referente o prestador cadastrado na nota fiscal\.

__4 – Simples Nacional;__

- Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR \(campo 43 da SAFX04\) for igual “S” referente o prestador cadastrado na nota fiscal

__5 – Microempreendedor Individual MEI;__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “__05 – MEI \(Microempreendedor Individual__\)” referente o prestador cadastrado na nota fiscal\.

__6 – SUP; Não Tratado\.__

Tipo Alfanumérico

Tag 

obrigatória\.

__MFS\-895592__

RN45

__Regra p/ tag <Discriminacao> </Discriminacao>__

Preencher a tag com conteúdo fixo “Emissao de NFTS”

Tag 

obrigatória\.

RN46

__Regra p/ tag <TipoNFTS> </TipoNFTS>__

Prencher a tag com conteudo fixo “__1__” – Nota Fiscal do Tomador

Tipo Numérico\.

Tag 

obrigatória\.

__MFS\-895592__

RN47

__Regra da tag <Assinatura></Assinatura> “Verificar com Campello”__

Tag 

obrigatória\.

__MFS\-895592__

RN48

__Regra da tag </Assinatura> __Tag relacionada ao fechamento da assinatura

Tag 

obrigatória\.

__MFS\-895592__

### INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__OS/CH/MFS__

__IM02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“BA”__ e ao código de município do IBGE igual a __“27408”__ __\(Salvador\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __Salvador/BA__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-895592__

__IM03__

__Código IBGE:  27408 – Município/UF: Salvador/ BA__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Salvador”\.

__MFS\-895592__

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[EXCLUÍDA – __Descrição da Regra de Negócio 01\]

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX

