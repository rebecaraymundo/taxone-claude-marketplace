# MTZ-ISS_WEB-Geracao_do_Meio_Magnetico-Camacari

- **Fonte:** MTZ-ISS_WEB-Geracao_do_Meio_Magnetico-Camacari.docx
- **Modificado:** 2026-02-12
- **Tamanho:** 144 KB

---

THOMSON REUTERS

Municipal

ISS WEB \- Camaçari \- Geração do Meio Magnético

 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4130

Geração do Meio Magnético ISS WEB

Este documento tem como objetivo criar a geração para os municípios que são atendidos pelo ISS WEB\. Com essa OS estaremos criando a obrigação para o município de Camaçari\.

CH3601\_2014

Tratamento na Regra geral p/ Registro de Serviços Tomados

Esse documento tem como objetivo tratar a recuperação de notas fiscais eletrônicas para o Registro de Serviços Tomados\.

CH19613\_2018

\(MFS20124\)

Geração do Meio Magnético ISS WEB

Essa correção tem como finalidade preencher o campo "2 \- Código do Serviço" referente ao Detalhe \(itens de serviço\) da Nota fiscal com a informação do código Lei Complementar Nº 116 31 de julho/2003\.

CH19500\_2018

\(MFS20153\)

Geração do Meio Magnético ISS WEB

Essa MFS tem como correções os campos:  
5 – Versão do Arquivo \(Header\) nova versão do leiaute\.

13 – Valor Base de Cálculo \(Documento Fiscal\) o sistema deve recuperar o valor da base isenta ISS quando temos as notas não tributadas\. 

15 – Tipo de Tributação \(Documento Fiscal\) corrigido como bug técnico, pois não gerava o indicador ‘2’ isento através da parametrização de serviço por pessoa física/jurídica\.

MFS\-30327

Geração do Meio Magnético ISS WEB

Nova versão ISSWEB \(“V01\.3”\)\. Ajustes nas regras RN12 e RN49\.

MFS40154

Andréa Rocha

Atualização do campo versão para “V01\.2”, conforme o manual da versão “V01\.3”\.

MFS72336

Andréa Rocha

Alterar a regra de geração do campo Data do Fato Gerador, para tratar para a situação em que a data do fato gerador é maior que a data de emissão da nota fiscal\.

MFS75558

Rogério Ohashi

Este documento tem como objetivo incluir o parâmetro “Quebrar Arquivos por Data de Emissão” na tela de Geração do Meio Magnético\. Funcionalidade válido apenas para Notas de Serviços Tomados\.

MFS78524

Rogério Ohashi

Este documento tem como objetivo incluir o tratamento no Campo de Tipo de Tributação para as Notas Fiscais de Serviços Tomados para o código__ 0 \- ISS próprio\.__

MFS79611

Rogério Ohashi

Este documento tem como objetivo incluir o tratamento no Campo Detalhe 2  – Valor ISS do Serviço para as Notas Fiscais de Serviços Tomados, caso o Campo Detalhe 1 \- Tipo de Tributação for igual ao código__ 0 \- ISS próprio, __recuperar o campo de Valor de ISS próprio\.

MFS560148

Rogério Ohashi

Este documento tem como objetivo de incluir o parâmetro “Gerar NFs de Serviços Tomados somente com ISS Retido” para permitir o usuário que considere ou não as Notas Fiscais de Serviço Tomados sem ISS Retido\.

MFS918816

Andréa Rocha

Alteração de regra de preenchimento do campo Inscrição Municipal do Prestador do Header, para a geração do arquivo de serviços tomados\.  Esse tratamento será feito para a geração do arquivo de construção civil\.

MFS829438

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-1012339__

Rosemeire Santos

Inclusão do parâmetro “Quebrar Arquivos por Data de Emissão” para Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager \- Camaçari:__

O novo módulo “Camaçari” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados do município de Camaçari”\.

OS4130

RN02

__Regra p/ abertura do novo módulo no Manager \- Camaçari:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “BA” e ao código de município do IBGE igual a “5701” \(Camaçari\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Camaçari, Barueri\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS4130

RN03

__Estrutura de menus do módulo Camaçari:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Camaçari:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviços \(Const\. Civil / Utilities /Telecom\)
- Janela
- Ajuda

OS4130

RN04

__Regra de criação do nome do arquivo__

__Serviços Prestados:__

__SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __SP__: Apenas registros de serviços prestados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__Serviços Tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__ \[ALTERAÇÃO \- MFS75558/MFS1005903\] \- Inclusão__ regra para geração por “Quebra por Data de Emissão”\. para Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)

Caso o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, realizar a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\_MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__MMAAAA__: representa a data inicial da geração

__MMAAAA:__ mês da competência referente à nota gerada\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.TXT

Obs: Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__Obs\.: Este novo parâmetro \(Quebrar Arquivos por Data de Emissão\) será válido, apenas para Notas de Serviços Tomados__

OS4130

__MFS75558__

<a id="_Hlk210845091"></a>__MFS829438__

__MFS\-1012339__

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Gerar Serviços Prestados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\) 

Gerar Serviços Tomados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__\[MFS75558\] Incluir opção “Quebrar por Data de Emissão”__

Quebrar arquivo por Data de Emissão: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. Quando a opção “Gerar Serviços Tomados” não estiver selecionada, deve ser desabilitado\. \(Opções S = Marcado e N = Desmarcado\)

Gerar NFs de Serviços Tomados somente com ISS Retido: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Estabelecimento: o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

Obs: Devem ser gerados arquivos separados para serviços prestados e serviços tomados, ou seja, um arquivo para os registros prestados e outro para os registros tomados\.

OS4130

__MFS75558__

__MSAF560148__

RN06

__Regras referentes à formatação dos registros gerados no meio magnético:__

- O arquivo deverá possuir 3 tipos de registros – __Header__, __Detalhes__ e __Trailer__;

 

- Os campos do tipo numérico devem ser alinhados à direita, completados com zeros à esquerda até atingir o tamanho exato do campo, sem vírgula e sem ponto e os não utilizados deverão ser preenchidos com zeros;
- Para todos os campos de valores e alíquotas, deverão considerar duas casas decimais\.
- Os campos do tipo Alfanuméricos devem ser alinhados à esquerda com brancos a direita e os não utilizados deverão conter brancos;
- Informar a data de competência no formato AAAAMM \(A = ano, M = mês\);
- Informe as datas no formato AAAAMMDD \(A = ano, M = mês, D = dia\);
- Os campos do Detalhe 2\(itens de serviço\) são obrigatórios se o campo Quantidade de Itens de Serviço \( Registro Detalhe1\) for maior que 0\(zero\) e se a Situação do documento \(Registro Detalhe1\) for diferente de 'CANCELADO' e 'INUTILIZADO'\.

OS4130

RN07

__Regra geral p/ Registro de Serviços Prestados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas 

com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\);
- Classificação do Documento fiscal = 2 ou 3;
- Empresa e estabelecimentos escolhidos na tela de geração;
- Data fiscal dentro do período de referência\.
- Quando a nota não tiver itens não deve ser recuperada\.

OS4130

__Regras para o Registro Header __

RN08

__Regra p/ o campo Header – Tipo do Registro__

Preencher com valor  fixo “__1__”

Tipo: Numérico

Tamanho: 01 caracter

OS4130

RN09

__Regra p/ o campo Header – Papel do Declarante__

Preencher com:

__1 – __Prestador\. Quando o campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = ‘__9__’\.

Tipo: Numérico

Tamanho: 01 caracter

RN10

__Regra p/ o campo Header – Competência de escrituração__

Referênte ao mês e ano da escrituração\.

Preencher com:

Preencher com o mês e ano da tela de geração do Meio Magnético\. \(Formato: AAAAMM\)\.

Tipo: Numérico

Tamanho: 06 caracteres

RN11

__Regra p/ o campo Header – Inscrição Municipal do Prestador__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Tipo: Numérico

Tamanho: 10 caracteres

RN12

__Regra p/ o campo Header – Versão do Arquivo__

Preencher com o texto fixo “__V01\.1__”, __“V01\.2”, “V01\.3”\.__

Tipo: Alfanumérico

Tamanho: 05 caracteres

CH19500\_2018

\(MFS20153\)

MFS\-30327

MFS40154

RN13

__Regra p/ o campo Header – Quantidade de Documentos Fiscais no Arquivo__

Preencher com a quantidade total de documentos fiscais contidos no arquivo\.

Tipo: Numérico

Tamanho: 06 caracteres 

OS4130

RN14

__Regra p/ o campo Header – Branco__

Preencher com espaços em branco\.

Tipo: Alfanumérico

Tamanho: 696 caracteres 

OS4130

RN15

__Regras p/ campo Header \- Sequencial de registro completado com zeros à esquerda:__

Preencher com o texto fixo __“000001”__\. 

Tipo: Alfanumérico

Tamanho: 06 caracteres

OS4130

__Regras para o Registro Detalhe 1 \(Documento Fiscal\)__

RN16

__Regra p/ o campo Detalhe 1  – Tipo do Registro__

Preencher com o texto fixo “__2__”\.

Tipo: Numérico

Tamanho: 01 caracter

OS4130

RN17

__Regra p/ o campo Detalhe 1  – Espécie__

Preencher com o campo Espécie da tela Parâmetros – “Tipo Docto Msaf x Espécie”\.

Caso o campo Espécie não for parametrizado, informar no log a seguinte mensagem: “Registro Detalhe 1 \- Campo Espécie não preenchido\. Favor verificar\.”

Tipo: Numérico

Tamanho: 02 caracteres 

OS4130

RN18

__Regra p/ o campo Detalhe 1  – Situação do Documento__

Preencher com:

__01__ – emitida\. Se campo SITUACAO = “N” da tabela DWT\_DOCTO\_FISCAL

__03__ – cancelada\. Se campo SITUACAO = “S” da tabela DWT\_DOCTO\_FISCAL\. 

__02__ – substituída\. Não será tratada nesta OS\. 

__04__ – inutilizada\. Não será tratada nesta OS\. 

__05 __– extraviada\. Não será tratada nesta OS\. 

Tipo: Numérico

Tamanho: 02 caracteres 

OS4130

RN19

__Regra p/ o campo Detalhe 1  – Nome da Série__

Recuperar o campo Série da parametrização no módulo Parâmetros por Municípios – Parâmetros – Modelo Msaf x Série  referente ao código de modelo cadastrado no nota fiscal emitida\.  

__OBS\.:__ Deverá recuperar a descrição da série do campo “DSC\_SERIE\_OBRIG” da Tfix83 no lugar do código da série\. Segundo o Layout do município  de Camaçari, é exigido a descrição no lugar do código\. 

Caso o campo Série não for parametrizado, informar no log a seguinte mensagem: “Registro Detalhe 1 \- Campo Nome da Série não preenchido\. Favor verificar\.”

Tipo: Alfanumérico

Tamanho: 20 caracteres 

OS4130

RN20

__Regra p/ o campo Detalhe 1  – Tipo Entidade__

Deverá preencher com:  

 

__“8”__ – pessoa física\. Quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR  tiver 11 posições\. 

__“9”__ – pessoa juridíca\. Quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR tiver 14 posições\.

__“2”__ – inscrição municipal\.Quando  o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR estiver vazio\.

__Senão__, preencher com:

__“0”__ \- não identificado\. 

Tipo: Numérico

Tamanho: 01 caracter

OS4130

RN21

__Regra p/ o campo Detalhe 1  – Inscrição Municipal, CPF ou CNPJ__

Se o valor informado no campo  Detalhe 1 \- “Tipo Entidade” for:

“__8” \- __Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR, referente ao CPF\. 

“__9” \- __Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR, referente ao CNPJ\.

“__2” \- __Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR, referente a inscrição municipal\.

__“0”__ \- Preencher com zeros\.

Tipo: Numérico

Tamanho: 14 caracteres

OS4130

RN22

__Regra p/ o campo Detalhe 1  – Razão Social__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Numérico

Tamanho: 100 caracteres__ __

OS4130

RN23

__Regra p/ o campo Detalhe 1  – Número Inicial__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 10 caracteres__ __

OS4130

RN24

__Regra p/ o campo Detalhe 1  – Número Final__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 10 caracteres__ __

OS4130

RN25

__Regra p/ o campo Detalhe 1  – Data de Emissão__

 Preencher com o data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Alfanumérico

Tamanho: 08 caracteres__ __

OS4130

RN26

__Regra p/ o campo Detalhe 1  – Data do Fato Gerador__

__\[MFS72336\] Tratamento para a situação em que a data do fato gerador é maior que a data de emissão da nota fiscal__

Se o campo DAT\_FATO\_GERADOR for menor ou igual ao campo DATA\_EMISSAO

      Preencher com o campo DAT\_FATO\_GERADOR da tabela DWT\_DOCTO\_FISCAL

Senão

      Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL

Tipo: Alfanumérico

Tamanho: 08 caracteres__ __

OS4130

MFS72336

RN27

__Regra p/ o campo Detalhe 1  – Valor Total do Documento__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: 15 caracteres__ __

OS4130

RN28

__Regra p/ o campo Detalhe 1  – Valor Base de Cálculo__

Preencher com o campo VLR\_BASE\_ISS\_1 OU VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: 15 caracteres__ __

OS4130

CH19500\_2018

\(MFS20153\)

RN29

__Regra p/ o campo Detalhe 1  – Valor Total ISS__

Preencher com o somatório do campo “Valor ISS do Serviço” referente aos registros Detalhe 2\. Caso o campo não possuir  informações, preencher com zeros\.

Tipo: Numérico

Tamanho: 15 caracteres__ __

OS4130

RN30

__Regra p/ o campo Detalhe 1  – Tipo de Tributação__

__0 __\-  __ISS próprio\. __Para que esse campo seja preenchido com __“0”,__ é necessário que pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido , recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se

o local da prestação do serviço = município do módulo selecionado OU; 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU;

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\. 

__2__ –__ Isento\. __Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

Tipo: Alfanumérico

Tamanho: 01 caracter__ __

OS4130

RN31

__Regra p/ o campo Detalhe 1  – Observação__

Informar espaços em branco\.

Tipo: Alfanumérico

Tamanho: 500 caracteres__ __

OS4130

RN32

__Regra p/ o campo Detalhe 1  – Quantidade de Itens de Serviço__

Preencher com a quantidade de itens de serviços presentes no documento fiscal

Tipo: Numérico

Tamanho: 03 caracteres__ __

OS4130

RN33

__Regra p/ o campo Detalhe 1  – Sequencial de registro __

Neste campo, deverá informar o seguência do registro completado com zeros à esquerda, ou seja,  deverá continuar o sequencial iniciado pelo registro do cabeçalho\. 

Tipo: Numérico

Tamanho: 06 caracteres__ __

OS4130

__Regras para o Registro Detalhe 2 \(Itens de Serviço\)__

RN34

__Regra p/ o campo Detalhe 2  – Tipo do Registro __

Preencher com o texto fixo “__3__”

Tipo: Numérico

Tamanho: 01 caracter__ __

OS4130

RN35

__Regra p/ o campo Detalhe 2 – Código do Serviço__

Preencher com o campo COD\_SERVICO da DWT\_ITENS\_SERV COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116, referente ao serviço cadastrado na nota\.

Tipo: Numérico

Tamanho: 06 caracteres

OS4130

CH19613\_2018

\(MFS20124\)

RN36

__Regra p/ o campo Detalhe 2  – Valor do Serviço__

Preencher com o campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV, referente ao valor do serviço cadastrado na nota\.

Tipo: Numérico

Tamanho: 15 caracteres

OS4130

RN37

__Regra p/ o campo Detalhe 2  – Valor ISS do Serviço__

Preencher com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV, referente ao valor ISS do serviço\.

Tipo: Numérico

Tamanho: 15 caracteres

OS4130

RN38

__Regra p/ o campo Detalhe 2  – Alíquota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, referente a alíquota cadastrada na nota\.

Tipo: Numérico

Tamanho: 05 caracteres

OS4130

RN39

__Regra p/ o campo Detalhe 2  – Branco__

Preencher com espaços em branco\.

Tipo: Alfanumérico

Tamanho: 683 caracteres

OS4130

RN40

__Regra p/ o campo Detalhe 2  – Sequencial de registro\.__

Neste campo, deverá informar o seguência do registro completado com zeros à esquerda, ou seja,  deverá continuar o sequencial iniciado pelos registros anteriores\. 

Tipo: Numérico

Tamanho: 06 caracteres

OS4130

__Regras para o Registro Trailer __

RN41

__Regra p/ o campo Trailer – Tipo do Registro __

Preencher com o texto fixo “__4__”  

Tipo: Numérico

Tamanho: 01 caracter__ __

OS4130

RN42

__Regra p/ o campo Trailer – Branco __

Preencher com espaços em branco\.

Tipo: Alfanumérico

Tamanho: 724 caracteres__ __

OS4130

RN43

__Regra p/ o campo Trailer – Sequencial de registro\.__

Neste campo, deverá informar o seguência do registro completado com zeros à esquerda, ou seja,  deverá continuar o sequencial iniciado pelos registros anteriores\. 

Tipo: Numérico

Tamanho: 06 caracteres__ __

OS4130

RN44

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Parâmetro “Gerar NFs de Serviços Tomados somente com ISS Retido”, apenas se esse parâmetro estiver desmarcado\.
- Documentos de Entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.
- Quando a nota não tiver itens não deve ser recuperada\.
- __\[ALTERADA – CH3601\_2014\]__ Para considerar notas fiscais eletrônicas verificar:

Se o município do prestador \(campo COD\_MUNICIPIO da for __DIFERENTE__ do tabela X04\_PESSOA\_FIS\_JUR\) município do módulo selecionado para geração, recuperar os documentos com uma das situações abaixo:

- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU__
- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

__Regra Parâmetro: __Gerar NFs de Serviços Tomados somente com ISS Retido

__Se __o parâmetro__ “__Gerar NFs de Serviços Tomados somente com ISS Retido” estiver marcado, verificar se pelo menos uma das seguintes opções, abaixo, seja verdadeira:

  __Se __o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" 

      __E se__ o campo de COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL \(local da prestação do serviço\) for igual ao município do módulo selecionado;

__OU__;

      __Se__ o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido 

        __E se__ o campo de COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL \(local da prestação do serviço\) for igual ao município do módulo selecionado

    __Considerar somente__ as Notas Fiscais com ISS Retido

__Senão__

__  Se __o parâmetro__ “__Gerar NFs de Serviços Tomados somente com ISS Retido” estiver desmarcado

    Considerar todas as Notas Fiscais com ISS Retido e Sem Retenção, __conforme regra atual__\.

Default: N \(Desmarcado\)\.

OS4130

CH3601\_2014

__MFS560148__

__Regras para o Registro Header __

RN45

__Regra p/ o campo Header – Tipo do Registro__

Preencher com valor  fixo “__1__”

Tipo: Numérico

Tamanho: 01 caracter

OS4130

RN46

__Regra p/ o campo Header – Papel do Declarante__

Preencher com:

__0 – __Tomador\. Quando o campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> ‘__9__’;

Tipo: Numérico

Tamanho: 01 caracter

OS4130

RN47

__Regra p/ o campo Header – Competência de escrituração__

Referênte ao mês e ano da escrituração\.

Preencher com:

Preencher com o mês e ano da tela de geração do Meio Magnético\. \(Formato: AAAAMM\)\.

Tipo: Numérico

Tamanho: 06 caracteres

OS4130

RN48

__Regra p/ o campo Header – Inscrição Municipal do Prestador__

__\[MFS918816\] __Alteração do preenchimento do campo para a geração da Construção Civil

__Se __a geração do arquivo selecionada for igual a “Arquivos de Entrada de Serviços \(Const\.Civil / Utilities/ Telecom\)”

      Preencher com o campo inscrição municipal eventual da tabela X156\_CAD\_INSC\_MUN, cadastrada para o 

      Estabelecimento/município em que está sendo gerado o arquivo magnético

__Senão__

      Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Tipo: Numérico

Tamanho: 10 caracteres

OS4130

MFS918816

RN49

__Regra p/ o campo Header – Versão do Arquivo__

Preencher com o texto fixo “__V01\.1__”, __“V01\.2”, “V01\.3”\.__

Tipo: Alfanumérico

Tamanho: 05 caractere

OS4130

CH19500\_2018

\(MFS20153\)

MFS\-30327

MFS40154

RN50

__Regra p/ o campo Header – Quantidade de Documentos Fiscais no Arquivo__

Preencher com a quantidade total de documentos fiscais contidos no arquivo\.

Tipo: Numérico

Tamanho: 06 caracteres 

OS4130

RN51

__Regra p/ o campo Header – Branco__

Preencher com espaços em branco\.

Tipo: Alfanumérico

Tamanho: 696 caracteres 

OS4130

RN52

__Regras p/ campo Header \- Sequencial de registro completado com zeros à esquerda:__

Preencher com o texto fixo __“000001”__\. 

Tipo: Alfanumérico

Tamanho: 06 caracteres

OS4130

__Regras para o Registro Detalhe 1 \(Documento Fiscal\)__

RN53

__Regra p/ o campo Detalhe 1  – Tipo do Registro__

Preencher com o texto fixo “__2__”\.

Tipo: Numérico

Tamanho: 01 caracter

OS4130

RN54

__Regra p/ o campo Detalhe 1  – Espécie__

Preencher com o campo Espécie da tela Parâmetros – “Tipo Docto Msaf x Espécie”\.

Caso o campo Espécie não for parametrizado, informar no log a seguinte mensagem: “Registro Detalhe 1 \- Campo Espécie não preenchido\. Favor verificar\.”

Tipo: Numérico

Tamanho: 02 caracteres 

OS4130

RN55

__Regra p/ o campo Detalhe 1  – Situação do Documento__

Preencher com:

__01__ – emitida\. Se campo SITUACAO = “N” da tabela DWT\_DOCTO\_FISCAL 

__03__ – cancelada\. Se campo SITUACAO = “S” da tabela DWT\_DOCTO\_FISCAL\.

__02__ – substituída\. Não será tratada nesta OS\. 

__04__ – inutilizada\. Não será tratada nesta OS\. 

__05 __– extraviada\. Não será tratada nesta OS\. 

Tipo: Numérico

Tamanho: 02 caracteres

OS4130

RN56

__Regra p/ o campo Detalhe 1  – Nome da Série__

Recuperar o campo Série da parametrização no módulo Parâmetros por Municípios – Parâmetros – Modelo Msaf x Série  referente ao código de modelo cadastrado no nota fiscal emitida\.  

__OBS\.:__ Deverá recuperar a descrição da série do campo “DSC\_SERIE\_OBRIG” da Tfix83 no lugar do código da série\. Segundo o Layout do município  de Camaçari, é exigido a descrição no lugar do código\. 

Caso o campo Série não for parametrizado, informar no log a seguinte mensagem: “Registro Detalhe 1 \- Campo Nome da Série não preenchido\. Favor verificar\.”

Tipo: Alfanumérico

Tamanho: 20 caracteres 

OS4130

RN57

__Regra p/ o campo Detalhe 1  – Tipo Entidade__

Deverá preencher com:  

 

__“8”__ – pessoa física\. Quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR  tiver 11 posições\. 

__“9”__ – pessoa juridíca\. Quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR tiver 14 posições\.

__“2”__ – inscrição municipal\.Quando  o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR estiver vazio\.

__Senão__, preencher com:

__“0”__ \- não identificado\. 

Tipo: Numérico

Tamanho: 01 caracter

OS4130

RN58

__Regra p/ o campo Detalhe 1  – Inscrição Municipal, CPF ou CNPJ__

Se o valor informado no campo  Detalhe 1 \- “Tipo Entidade” for:

“__8” \- __Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR, referente ao CPF\. 

“__9” \- __Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR, referente ao CNPJ\.

“__2” \- __Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR, referente a inscrição municipal\.

__“0”__ \- Preencher com zeros\.

Tipo: Numérico

Tamanho: 14 caracteres

OS4130

RN59

__Regra p/ o campo Detalhe 1  – Razão Social__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Numérico

Tamanho: 100 caracteres__ __

OS4130

RN60

__Regra p/ o campo Detalhe 1  – Número Inicial__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 10 caracteres__ __

OS4130

RN61

__Regra p/ o campo Detalhe 1  – Número Final__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 10 caracteres__ __

OS4130

RN62

__Regra p/ o campo Detalhe 1  – Data de Emissão__

 Preencher com o data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Alfanumérico

Tamanho: 08 caracteres__ __

OS4130

RN63

__Regra p/ o campo Detalhe 1  – Data do Fato Gerador__

Preencher o campo DAT\_FATO\_GERADOR da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Alfanumérico

Tamanho: 08 caracteres__ __

OS4130

RN64

__Regra p/ o campo Detalhe 1  – Valor Total do Documento__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: 15 caracteres__ __

OS4130

RN65

__Regra p/ o campo Detalhe 1  – Valor Base de Cálculo__

Preencher com o campo VLR\_BASE\_ISS\_1 OU VLR\_BASE\_ISS\_2 OU VLR\_BASE\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: 15 caracteres__ __

OS4130

CH19500\_2018

\(MFS20153\)

__MFS560148__

RN66

__Regra p/ o campo Detalhe 1  – Valor Total ISS__

Preencher com o somatório do campo “Valor ISS do Serviço” OU “Valor do ISS Retido” referente aos registros Detalhe 2\. Caso o campo não possuir  informações, preencher com zeros\.

Tipo: Numérico

Tamanho: 15 caracteres__ __

OS4130

__MFS560148__

RN67

__Regra p/ o campo Detalhe 1  – Tipo de Tributação__

__\[MFS78524\] __Tratamento do Tipo de Tributação igual à 0 – ISS Próprio p/ serviços tomados

__1__ \-  __ISS retenção na fonte__\. Para que esse campo seja preenchido com __“1”,__ é necessário que pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido , recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado __OU__; 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__;

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \. 

__2__ –__ Isento\. __Verificar se__ __o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__Se __caso nenhuma das opões acima seja verdadeira

    __Preencher __esse campo com __0__ \- __ISS próprio__

Tipo: Alfanumérico

Tamanho: 01 caracter__ __

OS4130

__MFS78524__

RN68

__Regra p/ o campo Detalhe 1  – Observação__

Informar espaços em branco\.

Tipo: Alfanumérico

Tamanho: 500 caracteres__ __

OS4130

RN69

__Regra p/ o campo Detalhe 1  – Quantidade de Itens de Serviço__

Preencher com a quantidade de itens de serviços, presentes no documento fiscal\.

Tipo: Numérico

Tamanho: 03 caracteres__ __

OS4130

RN70

__Regra p/ o campo Detalhe 1  – Sequencial de registro __

Neste campo, deverá informar o seguência do registro completado com zeros à esquerda, ou seja,  deverá continuar o sequencial iniciado pelo registro do cabeçalho\. 

Tipo: Numérico

Tamanho: 06 caracteres__ __

OS4130

__Regras para o Registro Detalhe 2 \(Itens de Serviço\)__

RN71

__Regra p/ o campo Detalhe 2  – Tipo do Registro __

Preencher com o texto fixo “__3__”

Tipo: Numérico

Tamanho: 01 caracter__ __

OS4130

RN72

__Regra p/ o campo Detalhe 2  – Código do Serviço__

Preencher com o campo COD\_SERVICO da DWT\_ITENS\_SERV COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116, referente ao serviço cadastrado na nota\.

Tipo: Numérico

Tamanho: 06 caracteres

OS4130

CH19613\_2018

\(MFS20124\)

RN73

__Regra p/ o campo Detalhe 2  – Valor do Serviço__

Preencher com o campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV, referente ao valor do serviço cadastrado na nota\. 

  

Tipo: Numérico

Tamanho: 15 caracteres

OS4130

RN74

__Regra p/ o campo Detalhe 2  – Valor ISS do Serviço__

__\[MFS79611\] __Tratamento do Tipo de Tributação igual à 0 – ISS Próprio p/ serviços tomados

Preencher com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV, referente ao valor ISS do serviço\. 

__OU__

  __Se__ o campo__  __VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV __não__ estiver preenchido

    __E se__ o campo Detalhe 1  – Tipo de Tributação for igual à __0__ \- __ISS próprio__

Preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, referente ao valor ISS do serviço\. 

Tipo: Numérico

Tamanho: 15 caracteres

OS4130

__MFS79611__

RN75

__Regra p/ o campo Detalhe 2  – Alíquota__

__Preencher__ com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.  __Ou__

         __Se __o campo VLR\_ALIQ\_ISS\_RETIDO não estiver preenchido ou preenchido com zeros

             __Preencher__ com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: 05 caracteres

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, referente a alíquota cadastrada na nota\.

OS4130

__MFS560148__

RN76

__Regra p/ o campo Detalhe 2  – Branco__

Preencher com espaços em branco\.

Tipo: Alfanumérico

Tamanho: 683 caracteres

OS4130

RN77

__Regra p/ o campo Detalhe 2  – Sequencial de registro\.__

Neste campo, deverá informar o seguência do registro completado com zeros à esquerda, ou seja,  deverá continuar o sequencial iniciado pelos registros anteriores\. 

Tipo: Numérico

Tamanho: 06 caracteres

OS4130

__Regras para o Registro Trailer __

RN78

__Regra p/ o campo Trailer – Tipo do Registro __

Preencher com o texto fixo “__4__”  

Tipo: Numérico

Tamanho: 01 caracter__ __

OS4130

RN79

__Regra p/ o campo Trailer – Branco __

Preencher com espaços em branco\.

Tipo: Alfanumérico

Tamanho: 724 caracteres__ __

OS4130

RN80

__Regra p/ o campo Trailer – Sequencial de registro\.__

Neste campo, deverá informar o seguência do registro completado com zeros à esquerda, ou seja,  deverá continuar o sequencial iniciado pelos registros anteriores\. 

Tipo: Numérico

Tamanho: 06 caracteres__ __

OS4130

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

