# MTZ_DESXML_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_DESXML_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-03-03
- **Tamanho:** 123 KB

---

### DES XML \- GERAÇÃO DO MEIO MAGNÉTICO

### Controle das Alterações

__Data__

__OS/CH__

__Nome__

__Descrição__

08/10/2014

OS4630

Jefferson Mota

Criação do Documento

08/07/2015

OS4831

Jefferson Mota

Inclusão do Município de Itapecerica da Serra\-SP no validador DES XML

10/05/2016

MFS\-2071

João Henrique

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

01/08/2016

CH16938\_2016

Julyana Perrucini

Este documento tem como objetivo tratar a formatação do preenchimento da TAG CodigoServico, especificamente para o município de Limeira/ SP\.

16/08/2016

CH16938\_2016

Lara Aline

Este chamado tem o objetivo de ajustar as tags de XML de importação para o município de Limeira/SP

27/09/2016

MFS\-6770

Jorge Neto

Alteração na tag DataPrestacaoServico de data fiscal para data de emissão

30/09/2016

MFS\-6718/6807

João Henrique 

Este documento tem como o objetivo ajustar o formato da tag <CodigoServico>

03/10/2016

MFS\-6727

João Henrique

Este documento tem o objetivo de retirar as tags de cabeçalho da obrigação\.

03/10/2016

MFS\-6798 

João Henrique

Este documento tem o objetivo de retirar a tag </in\_dectomados> da obrigação acessória DES XML

04/10/2016

MFS\-6796 e 6729

João Henrique

Este documento tem o objetivo de alterar a tag <Situacao> para contemplar a opção ‘5’ – Nota Não Tributada\.

18/10/2016

MFS\-7448

João Henrique

Este documento tem como objetivo implementar um novo parâmetro para que seja possível realizar a quebra do arquivo por data de emissão\.

01/11/2016

MFS\-6325

Julyana Perrucini

Inclusão dos municípios de Jaú/ SP, Taubaté/ SP e Taboão da Serra/ SP no validador DES XML\.

03/11/2016

CH23311\_2016

Julyana Perrucini

Este documento tem como objetivo alterar o preenchimento da TAG <BaseCalculo>\.

18/11/2016

MFS\-7981

Julyana Perrucini

Inclusão dos municípios de Poá/ SP, Boituva/ SP, Caieiras/ SP e Petrópolis/ RJ no validador DES XML\.

23/11/2016

MFS\-8203

Julyana Perrucini

Inclusão dos municípios de Bebedouro/ SP, Ferraz de Vasconcelos/ SP e Mairiporã/ SP no validador DES XML\.

19/12/2016

CH23311\_2016

João Henrique 

Este documento tem o objetivo de alterar a tag <Situacao> para contemplar a opção ‘3’ – Extraviada e ‘4’ – Nota de Devolução\.

06/02/2016

MFS9372

João Henrique

Inclusão do Municipio de Varginha\-MG no validador DES XML\.

02/03/2017

CH2856\_2017

João Henrique

Alteração na recuperação das notas de serviços para o município de Itapecerica da Serra/SP\.

28/06/2017

CH5198\_2017 \(MFS\-11991\)

Julyana Perrucini

Este documento tem como objetivo incluir a parametrização de Classificação de Serviços por PFJ\.

22/02/2018

CH3298\_2018 \(MFS\-16732\)

João Henrique

Esse documento tem como objetivo preencher com espaço ou zero as tags do tipo numérica e string que forem obrigatórias no arquivo da DES\_XML\.

16/04/2018

MFS17822

João Henrique

Tratamento para o campo <ISSDevido> para o município de Itapecerica da Serra\-SP\.

22/05/2018

CH12469\_2018 \(MFS\-18661\)

Julyana Perrucini

Este documento tem como objetivo alterar a tag <AliqISS> para quando não houver informação de valor gerar igual a 0\.00\.

29/10/2018

MFS\-21666

João Henrique

Inclusão do Município de Caçapava\-SP no validador DES XML\.

29/05/2020

MFS\-36471 / MFS\-36472

Andréa Rocha

Alteração da regra de recuperação dos dados para o município de Bebedouro e Varginha

26/01/2021

[MFS\-58606](https://jira.thomsonreuters.com/browse/MFS-58606)

Rogério Ohashi

Alteração da regra de recuperação de Notas Fiscais de serviços tomados dentro no município de Bebedouro\. \(Conforme Decreto n° 10\.519/13 que regulamenta a Declaração e a Nota Fiscal Eletrônica de Serviços no município de Bebedouro/SP, os contribuintes que emitem NFS\-e ficam dispensados da Declaração Eletrônica de Serviços\. Portanto, as notas não devem ser geradas no arquivo\)\.

25/02/2021

MFS\-47227

Rogério Ohashi

Este documento tem como objetivo alterar a recuperação das informações de Serviços Tomados do município de Taubaté, passando a desconsiderar as Notas Fiscais de Prestadores de Serviços do mesmo município\. 

12/04/2021

MFS\-60871

Rogério Ohashi

Este documento tem como objetivo alterar a recuperação das informações de Serviços Tomados do município de Caçapava, passando a desconsiderar as Notas Fiscais de Prestadores de Serviços do mesmo município\.

10/11/2022

MFS\-96398

Elisabete Costa

Inclusão do Município de Itirapina\-SP no validador DES XML\.

08/08/2023

MFS\-

Rosemeire Santos

Inclusão do Município de Cabreúva\-SP no validador DES XML\.

08/08/2023

MFS\-556192

Rosemeire Santos

Inclusão do Município de Bragança Paulista\-SP no validador DES XML\.

<a id="_Hlk197507159"></a>09/08/2023

MFS\-556212

Rosemeire Santos

Inclusão do Município de Mococa\-SP no validador DES XML\.

06/12/2024

MFS\-713532

Bruna Ribeiro 

Este documento tem como objetivo alterar a geração das notas fiscais que serão consideradas na geração do meio magnético, passando a não gerar notas fiscais sem valores de ISS\. 

07/05/2025

MFS\-788069

Rosemeire Santos

Inclusão do Município de Itapeva/SP no validador DES XML\.

24/06/2025

MFS834676

Andréa Rocha

Tratamento para o campo <ISSDevido> para o município de Cabreúva\.

18/08/2025

MFS\-839828

Rosemeire Santos

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

25/08/2025

MFS\-875362

Rosemeire Santos

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador DES\-XML\.

22/09/2025

MFS\-907248

Andréa Rocha

Inclusão do tratamento para os campos <BaseCalculo> e <AliqISS>, para passar a considerar o valor do ISS retido e a sua alíquota\.

25/11/2025

MFS\-966788

Rafael Fabiano

Inclusão do Município de Cambé/PR no validador DES XML\.

14/01/2026

MFS\-1000524

Klemer Monteiro

Este documento tem como objetivo alterar a regra __RN 51__, e acrescentar a __RN51\.a __para o municipio ITAPEVA/SP para considerar o valor total da nota preenchido quando não tem campo preenchido na base de cáculo\.

22/01/2026

MFS\-1014874

Rosemeire Santos

Este documento tem como objetivo alterar a recuperação das informações de Serviços Tomados do município de Cambé, passando a desconsiderar as Notas Fiscais de Prestadores de Serviços do mesmo município\.

28/02/2025

__MFS\-1059645__

Rosemeire Santos

Este documento tem como objetivo, a inclusão dos municípios de Cajuru\-SP, Nova Campina\-SP e Santa Cruz Da Esperanca\-SP, no validador DES XML\.

 

### REGRAS DE NEGÓCIOS

###### __Regras__

###### __DESCRIÇÃO__

__OS/CH/MFS__

RN01

__Estrutura de menus do módulo DES XML:__

Deverão ser criado o seguinte menu e sub\-menus no módulo DES XML:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)__
- Janela
- Ajuda

OS4630

__MFS\-875362__

RN02

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__\[ALTERADO CH22247\_2016\]__

Quando o parâmetro ‘__Quebrar Arquivos por Data de Emissão__’ estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\.XML__, onde:

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

       __\.XML__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.XML

__ST\_DES\_MUNICIPIO\_DDMMAAAA\.XML__, onde:

__ST\_DES__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

__MUNICIPIO__: representa o município que está sendo gerado\.

__DDMMAAAA__: representa a data inicial da geração

__\.XML__: extensão do arquivo\.

Ex: ST\_DES\_PIRASSUNUNGA\_01012010\.XML

Quando o parâmetro ‘Quebrar Arquivos por Data de Emissão’ estiver marcado, deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser conforme abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

       __\.XML__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.XML

__ST\_DES\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.XML__, onde:

__ST\_DES__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

__MUNICIPIO__: representa o município que está sendo gerado\.

__DDMMAAAA__: representa a data inicial da geração

__\_MMAAAA: __mês e ano da competência referente à nota gerada\.

__\.XML__: extensão do arquivo\.

Ex: ST\_DES\_PIRASSUNUNGA\_01012010\_122009\.XML

Obs: Neste caso o arquivo normal__ também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

OS4630

__MFS7448__

__MFS\-839828__

__MFS\-875362__

RN03

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

__Tipo da operação:__ O campo deve ser tipo combo com as seguintes opções: “__Inclusão__”, “__Alteração__” e “__Exclusão__"\. 

Valor default: “__Inclusão__”\.

__Código Usuário: __O__ __campo deve ser um tex box, para a inclusão do código\.

__Código Contribuinte:__ O__ __campo deve ser um tex box, para a inclusão do código do Contribuinte\.

__\[ALTERADO CH22247\_2016\]__

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox, por default desmarcado\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município em questão, que estejam licenciados e que o usuário possua acesso no PowerLock\.

OS4630

__MFS2071__

__MFS7448__

RN04

__Regras referentes à formatação dos registros gerados no meio magnético:__

Abaixo seguem algumas formatações de dados que devem ser seguidas para geração correta na estrutura dos arquivos\.

O arquivo a ser gerado para importação dever ser no formato __‘XML’;__

Não incluir comentários no arquivo XML;

Não incluir anotação e documentação no arquivo XML \(TAG annotation e TAG documentation\);

Não incluir caracteres de formatação no arquivo XML \("line\-feed", "carriage return", "tab", caractere de "espaço" entre as TAGs\);

Acentos e caracteres especiais devem ser suprimidos do arquivo, conforme exigência do validador\.

__Campo de Valores Decimais__

Os valores decimais devem ser no formato: “__0\.00”__\.

Não deve ser utilizado separador de milhar\. O ponto \(__\.__\) deve ser utilizado para separar a parte inteira da fracionária:

Exemplo: 48\.562,25 = 48562\.25 / 1,00 = 1\.00 ou 1 / 0,50 = 0\.50 ou 0\.5

__Campo de Valores Percentuais__

Os valores percentuais devem ser preenchidos no formato: “0\.000”\.

O formato em percentual presume o valor percentual em sua forma fracionária, contendo 5 dígitos\. O ponto \(\.\) separa a parte inteira da fracionária\.

Exemplo: 62% = 62 / 150% = 150 / 25,32% = 25\.32

__Campo tipo Numérico__

Não incluir “zeros não significativos” para campos numéricos;

Não incluir “espaços” no início ou no final de campos numéricos

A posição do campo é definida na estrutura do documento XML através de TAGs \(<tag>conteúdo</tag>\);

__Campo tipo Texto__

Não deve ser inseridos espaços em branco após o preenchimento

Não inserir espaços no início ou fim dos campos;

A posição do campo é definida na estrutura do documento XML através de TAGs \(<tag>conteúdo</tag>\);

As tags que permitirem valores nulos devem ser omitidas da estrutura XML a ser enviada quando seus valores forem nulos\.

OS4630

__RN05__

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)__

Considerar todas as notas com as seguintes características:

- Documentos de entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2, 3 e 9 \(RPA\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência informado na tela de geração
- Considerar notas canceladas\.

__\[ALTERADO CH2856\_2017\] – Para o município de Itapecerica da Serra/SP: __

Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\. OU

Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\. 

Se o COD\_SERVICO \(SAFX09\) for <> de 3\.05, 7\.02, 7\.04, 7\.05, 7\.09, 7\.10, 7\.11, 7\.12, 7\.14, 7\.15, 7\.16, 7\.17, 7\.18, 7\.19, 11\.01, 11\.02, 11\.04,12\. 01 a 12\.17, 16\.01, 17\.05, 17\.10, 20\.01, 20\.02 e 20\.03, o sistema deverá ignorar a nota fiscal\.

__\[MFS36471 e MFS36472\] – Para o município de Bebedouro e Varginha:__

 \- Desconsiderar os itens da nota que não possuírem Valor de Base ISS, deve\-se verificar as 3 bases de ISS \(quando a tributação for igual a 1 – Normal ou 2 – Isento ou 3 – Realizado por Terceiros\)\.

Quando a nota não tiver itens não deve ser recuperada\.

__\[[MFS\-58606](https://jira.thomsonreuters.com/browse/MFS-58606)\] – Regra Específica para o município de Bebedouro/SP: Código Município ‘6102’__

 \- Desconsiderar as Notas Fiscais de Prestadores de Serviços quando forem do Município de Bebedouro/SP\.

       

__SE__ Estabelecimento for de São Paulo e do município de Bebedouro:  ESTABELECIMENTO\.COD\_MUNICIPIO = __6102;__

   __E__ Prestador de Serviço for de São Paulo e do município de Bebedouro: X04\_PESSOA\_FIS\_JUR\.COD\_MUNICIPIO = __6102\.__

                       

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

__\[MFS\-47227\] – Regra Específica para o município de Taubaté/SP: Código Município ‘54102’__

 \- Desconsiderar as Notas Fiscais de Prestadores de Serviços quando forem do Município de Taubaté/SP\.

       

__SE__ Estabelecimento for de São Paulo e do município de Taubaté:  ESTABELECIMENTO\.COD\_MUNICIPIO = __54102;__

   __E__ Prestador de Serviço for de São Paulo e do município de Taubaté: X04\_PESSOA\_FIS\_JUR\.COD\_MUNICIPIO = __54102\.__

                       

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

__\[MFS\-60871\] – Regra Específica para o município de Caçapava/SP: Código Município ‘8504’__

 \- Desconsiderar as Notas Fiscais de Prestadores de Serviços quando forem do Município de Caçapava/SP\.

       

__     SE __o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal;

__       E o__ campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.__ __

__                      __

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

__\[MFS\-96398\] – Regra Específica para o município de Itirapina/SP: Código Município ‘23602’__

 \- Desconsiderar as Notas Fiscais de Prestadores de Serviços quando forem do Município de Itirapina/SP\.

       

__     SE __o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal;

__       E o__ campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.__ __

__                      __

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

__\[MFS\-556212\] – Regra Específica para o município de Mococa/SP: Código Município ‘30508’__

 \- Desconsiderar as Notas Fiscais de Prestadores de Serviços quando forem do Município de Mococa/SP\.

       

__     SE __o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal;

__       E o__ campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.__ __

__                      __

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

__\[MFS\- 713532\] – Regra Específica para o município de Bragança Paulista/SP:__

\- Desconsiderar as notas fiscais que não possuírem valores de ISS em algum dos conjuntos de campos abaixo:

\- Base ISS ou Base Isenta ISS e Alíquota ISS e Valor de ISS\.

__OU__

\- Base ISS Retido e Alíquota ISS Retido e Valor de ISS Retido\.

__\[MFS\-1014874/ MFS\-1059645\] – Regra Específica para os municípios de Cambé/PR \(Código Município ‘3701’\), Cajuru\-SP \(Código Muniicpio ‘9403’\), Nova Campina\-SP \(Código Muniicpio ‘32827’\),  e Santa Cruz Da Esperanca\-SP \(Código Muniicpio ‘46256\): __

 \- Desconsiderar as Notas Fiscais de Prestadores de Serviços quando forem do Município de Cambé/PR\.

       

__     SE __o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal;

__       E o__ campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.__ __

__                      __

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

OS4630

CH2856\_2017

MFS\-36471

MFS\-36472

[MFS\-58606](https://jira.thomsonreuters.com/browse/MFS-58606)

MFS\-47227

MFS\-60871

MFS\-96398

MFS\-556212

MFS\-713532

__MFS\-1014874__

__MFS\-1059645__

RN06

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\] __

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag <?xml version="1\.0"?> exceto para o Município de Limeira:__

Tag relacionada à formatação do arquivo deve conter o texto fixo: ‘__<?xml version="1\.0"?>’\.__

209

Campo obrigatório\.

OS4630

CH18331\_2016

MFS6727

RN07

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag <in\_dectomados xmlns="NFe"> exceto para o Município de Limeira:__

Tag relacionada à formatação do arquivo deve conter o texto fixo: ‘__<in\_dectomados xmlns="NFe">’\.__

Campo obrigatório\.

OS4630

CH18331\_2016

MFS6727

RN08

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag <login> exceto para o Município de Limeira:__

TAG que indica abertura das informações do código do contribuinte, sendo aberta no início do XML\.

TAG obrigatória\.

OS4630

CH18331\_2016

MFS6727

RN09

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag <CodigoUsuario> </CodigoUsuario> exceto para o Município de Limeira:__

Preencher com o código usuário inserido na tela de geração do meio magnético\. Caso não for preenchido deverá exibir a seguinte mensagem no Log: 

“Não foi localizado o código usuário\. Efetuar o preenchimento na tela de geração do meio magnético\.”

Campo obrigatório\.

Tipo: Alfanumérico

Tam\.: 64 caracter

 

OS4630

CH18331\_2016

MFS6727

RN10

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag <CodigoContribuinte> </CodigoContribuinte> exceto para o Município de Limeira:__

Preencher com o Código Contribuinte inserido na tela de geração do meio magnético\. Caso não for preenchido deverá exibir a seguinte mensagem no Log: 

“Não foi localizado o código contribuinte\. Efetuar o preenchimento na tela de geração do meio magnético\.”

Campo obrigatório\.

Tipo: Alfanumérico   Tam\.: 64 caracter

OS4630

CH18331\_2016

MFS6727

RN11

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag <\\login> exceto para o Município de Limeira:__

TAG que indica o fechamento das informações do código do contribuinte\.

TAG obrigatória\.

OS4630

CH18331\_2016

MFS6727

RN12

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag <Movimento> exceto para o Município de Limeira:__

TAG que indica a data de movimento da geração do arquivo\.

TAG obrigatória\.

OS4630

CH18331\_2016

MFS6727

RN13

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag  <Ano> </Ano> exceto para o Município de Limeira:__

Deverá preecnher com a ano informado na tela de geração do meio magnético\.

TAG obrigatória\.

Tipo: Numérico

Tam\.: 4 dígitos

OS4630

CH18331\_2016

MFS6727

RN14

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag  <Mes> </Mes> exceto para o Município de Limeira:__

Deverá preecnher com o mês informado na tela de geração do meio magnético\.

TAG obrigatória\.

Tipo: Numérico

Tam\.: 2 dígitos

OS4630

CH18331\_2016

MFS6727

RN15

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20943\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra para tag </Movimento> exceto para o Município de Limeira:__

TAG que indica o fechamento das informações de data de geração\.

TAG obrigatória\.

OS4630

CH18331\_2016

MFS6727

 

__Regra para tag <DeclaracaoTomados> exceto para o Município de Limeira:__

Tag relacionada à formatação do arquivo com o texto fixo: ‘__<DeclaracaoTomados>’\.__

TAG obrigatória\.

OS4630

CH18331\_2016

MFS6727

RN16\.a

__Regra para tag <DeclaracaoTomados xmlns="NFe"> __Tag relacionada à formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: ‘__<DeclaracaoTomados xmlns="NFe">’\.__

TAG obrigatória\.

OS4630

CH18331\_2016

MFS6727

__MFS\-1059645__

RN17

__Regra p/ tag <Versao> </Versao>__

Identifica o layout do arquivo\. Preencher com o conteúdo fixo: “__1\.00”__ 

Campo obrigatório\.

OS4630

RN18

__Regra p/ tag <NotasFiscais>__

Tag que deve conter as notas fiscais tomadas\. 

Campo obrigatório\.

OS4630

RN19

__Regra p/ tag <Nota>__

Tag que deve conter os dados de uma determinada nota fiscal tomada\. 

Campo obrigatório\.

OS4630

RN20

__Regra p/ tag <IdentificadorNota> </IdentificadorNota> __

Preencher com número sequencial que identifica a nota no arquivo\. Deve iniciar sempre com __1__ na primeira nota e seguir de forma crescente, sempre somando \+1 para a próxima nota\.

Campo obrigatório\.

OS4630

RN21

__Regra p/ tag <OperacaoNota> </OperacaoNota>  __

Preencher com:

__“I” –__ Inclusão: Quando o campo Tipo da Operação da tela de geração, estiver selecionado com a opção “__Inclusão__”\.

__“A”__ – Alteração: Quando o campo Tipo da Operação da tela de geração, estiver selecionado com a opção “__Alteração__”\.

“__E” –__ Exclusão:  Quando o campo Tipo da Operação da tela de geração, estiver selecionado com a opção “__Exclusão__”\.

Campo obrigatório\.

Tipo: Alfanumérico

OS4630

RN22

__Regra p/ tag <DadosNota>__

Abertura da tag que contém dados referente a Nota Fiscal\. 

Campo obrigatório\.

Tag 

obrigatório\.

OS4630

RN23

__Regra p/ tag <DataEmissao> </DataEmissao>__

Será gerado com o conteúdo do campo DATA\_EMISSAO da SAFX07\.

Tag 

obrigatório\.

Tipo Alfanumérico\.  

__Formato: DD/MM/AAAA__

OS4630

RN24

__Regra p/ tag <DataPrestacaoServico> </DatPrestacaoServico> __

Recuperar o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tag 

obrigatório\.

Tipo Alfanumérico\.  

__Formato: DD/MM/AAAA__

OS4630

MFS6770

RN25

__Regra p/ tag <TipoNF> </TipoNF>  __

Preencher com o campo Tipo Docto da tela Parâmetros por Município / Parâmetros / Tipo Docto Msaf x Tipo Docto, referente ao documento cadastrado na nota fiscal\.

Obs\.: Caso o documento não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log: "Documento não parametrizado em Parâmetros por Município\. Favor verificar\!”

Caso esse campo não tenha informação, preencher com espaço na tag:

Exemplo: <TipoNF> </TipoNF>

Tag 

obrigatório\.

Tipo Alfanumérico\.  

OS4630

CH3298\_2018

MFS\-16732

RN26

__Regra p/ tag <Serie> </Serie>__

Será gerado com o conteúdo do campo SERIE\_DOCFIS da SAFX07\.

Caso esse campo não tenha informação, preencher com espaço na tag:

Exemplo: <Serie> </Serie>

Tag 

obrigatório\.

Tipo Alfanumérico\.  

OS4630

CH3298\_2018

MFS\-16732

RN27

__Regra p/ tag <Número> </Número>__

Será gerado com o conteúdo do campo NUM\_DOCFIS da SAFX07, desconsiderando zeros à esquerda\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <Número>0</Número>

Tag 

obrigatório\.

Tipo Numérico\.

Tam\.: 9 caracteres 

 

OS4630

CH3298\_2018

MFS\-16732

RN28

__Regra p/ tag <Situacao> </Situacao>__

Deverá preencher com uma das opções abaixo:

__1 \- __Nota __Normal__:

Se campo SITUACAO = “N” da SAFX07\.

__2 \- __Nota __Cancelada__:

Se campo SITUACAO = “S” da SAFX07\.

__3 \- __Nota __Extraviada__:

Se campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL = ‘E’\.

__4 \- __Nota de __Devolução__:

Se campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 04 da SAFX07\)\.

__\[ALTERADA \- CH5198\_2017 \(MFS\-11991\)\]__

__5 \- __Nota __Não Tributada__:

Buscar informação do campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, e COD\_PARAM = “433” da tela Parâmetros – Classificação de Serviços – __por Pessoa Fis/Jur ou por Município__ \(módulo Parâmetros para Município\) referente ao serviço e ao município do prestador \(Pessoa Fis/Jur\) cadastrado na nota fiscal, mais o código do prestador \(em casos de parametrização por Pessoa Fis/Jur\)\.

Se o campo IND\_CLASSE\_PFJ da tabela SAFX04 referente a Pessoa Física/ Jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” – \(Serviços Isentos\) na tela Classificação de Serviços de Parâmetros\.

Tag 

obrigatório\.

Tipo Numérico\.  

OS4630

MFS6729

MFS6796

CH23311\_2016

CH5198\_2017 \(MFS\-11991\)

RN29

__Regra p/ tag <RpsSerie> </RpsSerie>__

Não será tratada nessa OS\.

Caso esse campo não tenha informação, preencher com espaço na tag:

Exemplo: <RpsSerie> </RpsSerie>

OS4630

CH3298\_2018

MFS\-16732

RN30

__<RpsNumero> </RpsNumero> __

Não será tratada nessa OS\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <RpsNumero>0</RpsNumero>

OS4630

CH3298\_2018

MFS\-16732

RN31

__Regra p/ tag </DadosNota>__

Fechamento da tag Dados da Nota\. 

Tag 

obrigatório\.

OS4630

RN32

__Regra p/ tag <DadosPrestador>__

Abertura da tag que contém dados referentes ao prestador da Nota Fiscal\.  

Tag 

obrigatório\.

OS4630

RN33

__Regra p/ tag <TipoPessoa> </TipoPessoa>__

Deve preencher com uma das opções abaixo:

__F – Pessoa Física \- __Se o conteúdo do campo CPF\_CGC da SAFX04 tiver 11 posições\.

__J – Pessoa Jurídica \- __Se o conteúdo do campo CPF\_CGC da SAFX04 tiver 14 posições\.

__E – Pessoa do Exterior__ \- Se o conteúdo do campo COD\_ESTADO for igual a “EX”\.

OS4630

MFS\-96398

RN34

__Regra p/ tag <CpfCnpjPrestador> </CpfCnpjPrestador>__

Será gerado com o conteúdo do campo CPF\_CGC da SAFX04\.

SE

A TAG “TipoPessoa” for igual a “__EX__” colocar como “__EXTERIOR__”

Tag 

obrigatório\.

Tipo Alfanumérico

Tam\.: 14 caracters\.  

OS4630

MFS\-96398

RN35

__Regra p/ tag <RazaoSocial> </RazaoSocial>__

Será gerado com o conteúdo do campo RAZAO\_SOCIAL da SAFX04\.

Tag 

obrigatório\.

Tipo Alfanumérico

OS4630

RN36

__Regra p/ tag <InscricaoMunicipal> </InscricaoMunicipal>__

Será gerado com o conteúdo do campo INSC\_MUNICIPAL da SAFX04\.

Caso esse campo não tenha informação, preencher com zero na tag::

Exemplo: <InscricaoMunicipal> </InscricaoMunicipal>

Tag 

obrigatório\.

Tipo Alfanumérico

OS4630

CH3298\_2018

MFS\-16732

RN37

__Regra p/ tag <Cep> </Cep>__

Será gerado com o conteúdo do campo CEP da SAFX04\.

Caso esse campo não tenha informação preencher com zero na tag::

Exemplo: <Cep> </Cep>

Tag 

obrigatório\.

Tipo Alfanumérico

OS4630

CH3298\_2018

MFS\-16732

RN38

__Regra p/ tag <CodIbgeMunicipio> </CodIbgeMunicipio>__

Concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <CodIbgeMunicipio>0</CodIbgeMunicipio>

Tag 

obrigatório\.

Tipo Numérico\.

OS4630

CH3298\_2018

MFS\-16732

RN39

__Regra p/ tag <Logradouro> </Logradouro>__

Será gerado com o conteúdo do campo ENDERECO da SAFX04\.

Caso esse campo não tenha informação preencher com zero na tag::

<Logradouro> </Logradouro>

Tag 

obrigatório\.

Tipo Alfanumérico

OS4630

CH3298\_2018

MFS\-16732

RN40

__Regra p/ tag <NumeroEndereco> </NumeroEndereco>__

Será gerado com o conteúdo do campo NUM\_ENDERECO da SAFX04\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <NúmeroEndereco> </NumeroEndereco>

Tag 

obrigatório\.

Tipo Alfanumérico

OS4630

CH3298\_2018

MFS\-16732

RN41

__Regra p/ tag <ComplementoEndereco> </ComplementoEndereco>__

Será gerado com o conteúdo do campo COMPL\_ENDERECO da SAFX04

Caso esse campo não tenha informação, preencher com zero na tag::

Exemplo: <ComplementoEndereco> </ComplementoEndereco>

Tag 

obrigatório\.

Tipo Alfanumérico

OS4630

CH3298\_2018

MFS\-16732

RN42

__Regra p/ tag <Bairro> </Bairro>__

Será gerado com o conteúdo do campo BAIRRO da SAFX04\.

Caso esse campo não tenha informação, preencher com zero na tag::

Exemplo: <Bairro> </Bairro>

Tag 

obrigatório\.

Tipo Alfanumérico

OS4630

CH3298\_2018

MFS\-16732

RN43

__Regra p/ tag </DadosPrestador>__

Fechamento da tag </DadosPrestador>\.  

Tag 

obrigatório\.

OS4630

RN44

__Regra p/ tag <LocalPrestacaoServico>__

Abertura da tag <LocalPrestacaoServico>

Tag 

obrigatório\.

OS4630

RN45

__Regra p/ tag <CodIbgeMunPrestacao> </CodIbgeMunPrestacao>__

Código IBGE do Município do Prestador 

Concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Caso esse campo não esteja preenchido considerar o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

Tag 

obrigatório\.

Tipo Numérico\.

OS4630

RN46

__Regra p/ tag </LocalPrestacaoServico>__

Fechamento da tag <LocalPrestacaoServico>

Tag 

obrigatório\.

OS4630

RN47

__Regra p/ tag <Servico>__

Abertura da tag <Servico>

Tag 

obrigatório\.

OS4630

RN48

__Regra p/ tag <CodigoServico> </CodigoServico>__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

Formato: NN\.NN

__Tratamento:__

Para os códigos iniciados de 1 a 9, deve\-se manter o 0 \(zero\) à esquerda\. 

*Exemplo:* 0101 ou 101 deve gravar 01\.01\.

Tag 

obrigatório\.

Tipo Alfanumérico\.

OS4630

MFS\-6718

MFS\-6807

RN48\.a

__Regra p/ tag <CodigoServico> </CodigoServico> para o Município de Limeira/ SP__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

Formato: NN\.NN

__Tratamento:__

Para os códigos iniciados de 1 a 9, deve\-se manter o 0 \(zero\) à esquerda\. 

*Exemplo:* 0101 ou 101 deve gravar 01\.01\.

Tag 

obrigatório\.

Tipo Alfanumérico\.

CH16938\_2016

RN49

__Regra p/ tag <ValorNota> </ValorNota>__

Preencher com o resultado da somatória do campo VLR\_TOT agrupando por serviço da SAFX09 de todos os itens vinculados à NF\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <ValorNota>0</ ValorNota>

Tag 

obrigatório\.

Tipo Numérico

OS4630

CH3298\_2018

MFS\-16732

RN50

__Regra p/ tag <ValorDeducao> </ValorDeducao>__

Preencher com o resultado da somatória do campo VLR\_DEDUCAO\_ISS agrupando por serviço da SAFX09 de todos os itens vinculados à NF\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <ValorDeducao>0</ ValorDeducao>

Tag 

obrigatório\.

Tipo Numérico

OS4630

CH3298\_2018

MFS\-16732

RN51

__Regra p/ tag <BaseCalculo> </BaseCalculo>__

__\[ALTERADA – CH23311\_2016\]__

Preencher com o resultado da somatória do campo BASE\_ISS agrupando por serviço da SAFX09 de todos os itens vinculados à NF quando a tributação for igual a 1 – Normal ou 2 – Isento ou 3 – Realizado por Terceiros \(na escrituração fiscal da nota, apenas se utiliza um tipo de tributação\)\.

Se o campo BASE\_ISS não estiver preenchido ou estiver com zeros

          Preencher com a somatória do campo VLR\_BASE\_ISS\_RETIDO \(campo 57 da SAFX09\)\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <BaseCalculo>0</ BaseCalculo>

Tag 

obrigatório\.

Tipo Numérico

__  
__

 

OS4630

CH23311\_2016

CH3298\_2018

MFS\-16732

MFS907248

__MFS\-1059645__

RN51\.a

__Regra p/ tag <BaseCalculo> </BaseCalculo> \- Regra específica para o município de Itapeva/SP:__

Preencher com o resultado da somatória do campo BASE\_ISS agrupando por serviço da SAFX09 de todos os itens vinculados à NF quando a tributação for igual a 1 – Normal ou 2 – Isento ou 3 – Realizado por Terceiros \(na escrituração fiscal da nota, apenas se utiliza um tipo de tributação\)\.

Se o campo BASE\_ISS não estiver preenchido ou estiver com zeros

          Preencher com a somatória do campo VLR\_BASE\_ISS\_RETIDO \(campo 57 da SAFX09\)\.

          Se, caso esse campo da VLR\_BASE\_ISS\_RETIDO  = 0, preencher com "__<ValorNota> </ValorNota>” \(Total do serviço\)__

MFS\-1000524

RN52

__Regra p/ tag <AliqISS> </AliqISS>__

__\[ALTERADA \- CH12469\_2018 \(MFS\-18661\)\]__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

Se o campo ALIQ\_TRIBUTO\_ISS não estiver preenchido ou estiver com zeros

     Preencher com o campo VLR\_ALIQ\_ISS\_RETIDO\(campo 97 da SAFX09\)\.

Caso não houver valor informado, preencher com 0\.00\.

Tag Não O

brigatório\.

Tipo Numérico\.

OS4630

CH12469\_2018 \(MFS\-18661\)

MFS907248

RN53

__Regra p/ tag <ISSDevido> </ISSDevido>__

Não será tratado\. Não preencher\.

Para o município de __Itapecerica da Serra\-SP__: Preencher o campo com o valor <ISSDevido>0\.00</ISSDevido>

__\[ALTERADA – MFS834676\]__

Para o município de __Cabreúva\-SP__:

     Preencher com a somatória do campo VLR\_ISS, agrupando por serviço da SAFX09 de todos os itens vinculados à NF\.

     

       Caso esse campo não tenha informação, preencher com zero na tag:

     Exemplo: <ISSDevido>0\.00</ISSDevido>

Tag Não O

brigatório\.

Tipo Numérico

OS4630

 CH8483\_2018

MFS\-17822

MFS834676

RN54

__Regra p/ tag <ISSRetido> </ISSRetido> __

Preencher com o resultado da somatória do campo VLR\_ISS\_RETIDO agrupando por serviço da SAFX09 de todos os itens vinculados à NF\.

Caso esse campo não tenha informação, preencher com zero na tag:

Exemplo: <ISSRetido>0</ISSRetido>

Tag 

obrigatório\.

Tipo Numérico

OS4630

CH3298\_2018

MFS\-16732

RN55

__Regra p/ tag <Observacao> </Observacao>__

Não será tratado nesta OS\. Não Preencher 

OS4630

RN56

__Regra p/ tag </Servico>__

Fechamento da tag </Servico>

Tag 

obrigatório\.

OS4630

RN57

__Regra p/ tag </Nota>__

Fechamento da tag </Nota>

Tag 

obrigatório\.

OS4630

RN58

__Regra p/ tag </NotasFiscais>__

Fechamento da tag </NotaFiscais>

Tag 

obrigatório\.

OS4630

RN59

__Regra p/ tag <RegistroTotalizacao>__

Tag que contém as informações referentes às quantidades totais de notas enviadas\. 

Tag 

obrigatório\.

OS4630

RN60

__Regra p/ tag  <QtdNfeIncluidas> </QtdNfeIncluidas>__

Informar a quantidade total de notas cujo campo <OperacaoNota> = “__I__” 

Tag 

obrigatório\.

Tipo Numérico\.

OS4630

RN61

__Regra p/ tag  <QtdNfeAlteradas> </QtdNfeAlteradas>__

Informar a quantidade total de notas cujo campo <OperacaoNota> = “__A__” 

Tag 

obrigatório\.

Tipo Numérico\.

OS4630

RN62

__Regra p/ tag  <QtdNfeExcluidas></QtdNfeExcluidas>__

Informar a quantidade total de notas cujo campo <OperacaoNota> = “__E__” 

Tag 

obrigatório\.

Tipo Numérico\.

OS4630

RN63

__Regra p/ tag </RegistroTotalizacao>__

Indica o fechamento da tag __</RegistroTotalizacao>__

Tag 

obrigatório\.

OS4630

RN64

__Regra p/ tag </DeclaracaoTomados>__

Indica o fechamento da tag __</DeclaracaoTomados>__

Tag 

obrigatório\.

OS4630

RN65

__\[ALTERADO CH18331\_2016\]__

__\[ALTERADO CH20965\_2016\]__

__Esta TAG deverá ser retirada do cabeçalho da obrigação\.__

__Regra p/ tag </in\_dectomados> exceto para o Município de Limeira, Itapecerica da Serra e Pirassununga/ SP:__

Indica o fechamento da tag __</in\_dectomados>__

Tag 

obrigatório\.

OS4630

CH18331\_2016

MFS\-6798

### INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__OS/CH/MFS__

__IM01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

__OS4630__

__IM02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XX/XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4630__

__IM03__

__Código IBGE: 39301 – Município/UF: Pirassununga – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Pirassununga”\.

__OS4630__

__IM04__

__Código IBGE: 26902 – Município/UF: Limeira – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Limeira”\.

__OS4630__

__IM05__

__Código IBGE: 22208 – Município/UF: Itapecerica da Serra – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Itapecerica da Serra”\.

__OS4831__

__IM06__

__Código IBGE: 25300 – Município/UF: Jaú – SP__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de Jaú”\.

__MFS\-6325__

__IM07__

__Código IBGE: 54102 – Município/UF: Taubaté – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Taubaté”\.

__MFS\-6325__

__IM08__

__Código IBGE: 52809 – Município/UF: Taboão da Serra – SP__

A descrição funcional do módulo será: : “Consiste na entrega das informações sobre os serviços tomados do município de Taboão da Serra”\.

__MFS\-6325__

__IM09__

__Código IBGE: 39806 – Município/UF: Poá – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Poá”\.

__MFS\-7981__

__IM10__

__Código IBGE: 7001 – Município/UF: Boituva – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Boituva”\.

__MFS\-7981__

__IM11__

__Código IBGE: 9007 – Município/UF: Caieiras – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Caieiras”\.

__MFS\-7981__

__IM12__

__Código IBGE: 3906 – Município/UF: Petrópolis – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Petrópolis”\.

__MFS\-7981__

__IM13__

__Código IBGE: 6102 – Município/UF: Bebedouro – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Bebedouro”\.

__MFS\-8203__

__IM14__

__Código IBGE: 15707 – Município/UF: Ferraz de Vasconcelos – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Ferraz de Vasconcelos”\.

__MFS\-8203__

__IM15__

__Código IBGE: 28502 – Município/UF: Mairiporã – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Mairiporã”\.

__MFS\-8203__

__IM16__

__Código IBGE: 70701 – Município/UF: Varginha – MG__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Varginha”\.

__MFS\-9372__

__IM17__

__Código IBGE: 23602 – Município/UF: Itirapina – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Itirapina”\.

__MFS\-96398__

__IM18__

__Código IBGE: 8405 – Município/UF: Cabreúva – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Cabreúva”\.

__MFS\-554963__

__IM19__

__Código IBGE: 7605 – Município/UF: Bragança Paulista – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Bragança Paulista”\.

__ MFS\-556192__

__IM20__

__Código IBGE: 30508 – Município/UF: Mococa – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Mococa’’\.

__MFS\-556212__

__IM21__

__Código IBGE: 22406 – Município/UF: Itapeva – SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Itapeva\.

__MFS\-788069__

__IM22__

__Código IBGE: 3701 – Município/UF: Cambé – PR__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Cambé\.

__MFS\-966788__

__IM23__

__Código IBGE: XXXX – Município/UF: XXXX – XXX__

__Para cada município dessa lista deverá ser criado um modulo\.__

__MUNICÍPIO__

__ESTADO__

__CÓDIGO MUNICÍPIO__

__CAJURU__

__SP__

9403

__NOVA CAMPINA__

__SP__

32827

__SANTA CRUZ DA ESPERANCA__

__SP__

46256

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Nome do município\.

__MFS\-1059645__

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[EXCLUÍDA – __Descrição da Regra de Negócio 01\]

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX

