# MTZ_SAATRI_NFSE_Geracao_Meio_Magnetico

- **Fonte:** MTZ_SAATRI_NFSE_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-03-02
- **Tamanho:** 97 KB

---

THOMSON REUTERS

Municipal 

 Serviços Tomados 

Geração do Meio Magnético – SAATRI NFSE 	

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Data__

__Descrição__

MFS\-17592

João Henrique

14/05/2018

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador SAATRI NFSE\.

CH26557\_2018

\(MFS\-22147\)

João Henrique

07/11/2018

Essa alteração tem como finalidade estabelecer o critério para que o sistema recupere apenas as notas fiscais dos serviços tomados\.

MFS\-22548

Julyana Perrucini

26/11/2018

Este documento tem como objetivo a inclusão do município __Dias D’Ávila__ no validador SAATRI NFSE\.

MFS\-22995

Julyana Perrucini

13/12/2018

Este documento tem como objetivo a inclusão do município __Barreiras__ no validador SAATRI NFSE\.

MFS\-28385

Andréa Rocha

03/06/2019

Este documento tem como objetivo a inclusão do município __Boa Vista__ no validador SAATRI NFSE\.

MFS\-69550

Elisabete Costa

22/07/2021

Este documento tem como objetivo a inclusão do município __Paripiranga/BA__ no validador SAATRI NFSE\.

MFS\-80404

Elisabete Costa

22/02/2022

Este documento tem como objetivo a inclusão do município __IRECE/BA__ no validador SAATRI NFSE\.

MFS\-86281

Andréa Rocha

07/06/2022

Alteração da recuperação das informações de Serviços Tomados para o município de Jacobina, que passa considerar apenas Notas Fiscais de Serviços de prestadores de outros municípios\.

MFS\-86419

Andréa Rocha

28/06/2022

Alteração da recuperação das informações de Serviços Tomados para o município de Paripiranga, que passa considerar apenas Notas Fiscais de Serviços de prestadores de outros municípios\.

MFS\-86449

Andréa Rocha

28/06/2022

Criação de uma regra geral para preencher o campo Competência, quando houver quebra por Data de Emissão, independente do município selecionado para a geração\.

MFS\-99369

Elisabete Costa

29/12/2022

Este documento tem como objetivo a inclusão do município __ITAPEBI/BA__ no validador SAATRI NFSE\.

__MFS\-527914__

Rogério Ohashi

13/04/2023

Este documento tem como objetivo corrigir a regra para recuperar somente as Notas Fiscais com Retenção, incluindo o Campo de VLR\_ISS\_RETIDO e preencher os Campos de Base ISS, Valor ISS e Alíquota de ISS, considerando os campos de ISS Retido da tabela DWT\_ITEM\_SERV\.

__MFS\-788071__

Rosemeire Santos

13/05/2025

Este documento tem como objetivo a inclusão do município __CAMPO ALEGRE DE LOURDES/BA, __no validador SAATRI NFSE\.

__MFS\-879156__

Rogério Ohashi

07/08/2025

Adequação da regra para considerar o parâmetro Notas Fiscais Eletrônica, para não considerar Notas Fiscais de prestadores dentro do mesmo município do estabelecimento

__MFS\-829438__     

Graciela Soares

05/10/2025

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-1048314__

Alessandra Navatta

02/03/2026

Este documento tem como objetivo a inclusão do município LUIS EDUARDO MAGALHÃES__/BA, __no validador SAATRI NFSE\.

__REGRAS DE NEGÓCIO__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Estrutura de menus do módulo __

Deverão ser criados os seguintes menus e sub\-menus no módulo SAATRI NFSE:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)__
- Janela
- Ajuda 

__MFS\-17592__

__RN02__

__Regra de criação do nome do arquivo:__

__Serviços Tomados:__

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__       SAATRINFSE\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __SAATRINFSE__: representa a obrigação que está sendo gerada\. 

       __\.TXT__: extensão do arquivo\.

*Exemplo:* SAATRINFSE\_CATU\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__SAATRINFSE\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __SAATRINFSE__: representa a obrigação que está sendo gerada\. 

       __\.TXT__: extensão do arquivo\.

       __MMAAAA__: mês da competência referente à nota gerada

*Exemplo:* SAATRINFSE\_CATU\_01012010\_122009\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* __Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

__MFS\-17592__

__MFS\-829438      __

__RN03__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS\-17592__

__RN04__

__Regra p/ Geração do Arquivo Magnético__

1. O formato do arquivo será em \.TXT\.
2. Todos os campos do tipo \(Data\) têm o formado no padrão DDMMAAAA ou no caso de competência MMAAAA\.
3. Todos os campos do tipo \(Alfanumérico\) são preenchidos com espaços em branco à direita quando não alcançar o tamanho exato do campo\.
4. Todos os campos do tipo \(Numérico\) são preenchidos com zeros à esquerda quando não alcançar o tamanho exato do campo\.

__*Observação:*__ Para os campos numéricos nenhum separador de milhar e decimal devem ser informados\.

__MFS\-17592__

__RN05__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\):__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.
- Recuperar apenas notas fiscais com retenção do ISS \(campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV > 0\) __Ou__

__                                                                                      __\(campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV > 0\)

- O agrupamento das notas fiscais deverá ser realizado pelos campos: Código Atividade e Alíquota\.

__\[MFS\-80404\] \- Desconsiderar as NFS\-e emitidas no próprio município__ 

__Tratamento para o município de Irece/BA:__

- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

__\[MFS\-86281\] \- Desconsiderar as NFS\-e emitidas no próprio município__ 

__Tratamento para o município de Jacobina/BA:__

- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

__\[MFS\-86419\] \- Desconsiderar as NFS\-e emitidas no próprio município__ 

__Tratamento para o município de Paripiranga/BA:__

- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

__\[MFS\-99369\] \- Desconsiderar as NFS\-e emitidas no próprio município__ 

__Tratamento para o município de Itapebi/BA:__

- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

__\[ALTERAÇÃO\-__ __MFS__\-__879156\] Inclusão regra para considerar parâmetro Notas Fiscais Eletrônica__

__Notas Fiscais eletrônicas de Serviço Tomado: __

__\- Para Prestadores Dentro do município:__

__\- Se__ parâmetro “__*Prestador Dentro do Município*__” estiver “__marcado__” desconsiderar notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\)__ ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

__\- Se __parâmetro “__*Prestador Dentro do Município*__” estiver “__desmarcado__” considerar as notas fiscais com campo movto\_e\_s <> 9 da tabela safx07, contendo modelo de documento IGUAL à 55 \(que caracteriza nota fiscal eletrônica\) __ou__ se o Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal, __e__ o código de município do prestador for __*igual*__ ao código de município do Estabelecimento;

*  *Default: Desmarcado

__Se__ a __UF__ e o __Município __do estabelecimento não estiver parametrizados no Módulo > Parâmetro para Município > no Menu Parâmetros \- na tela de “Notas Fiscais Eletrônicas”, o sistema deverá seguir conforme regra atual, considerando todas as notas\.

__MFS\-17592__

CH26557\_2018

MFS\-22147

__MFS\-80404__

__MFS\-86281__

__MFS\-86419__

__MFS\-99369__

__MFS\-527914__

__MFS__\-__879156__

__RN06__

__Header \- Regra para o campo Identificação do Registro Header __

Preencher o campo com o valor __“A”\.__

Campo: Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico 

__MFS\-17592__

__RN07__

__Header \- Regra para o campo Versão do leiaute do arquivo__

Preencher o campo com o valor __“001”\.__

Campo: Obrigatório

Formato: 999

Tamanho: 3 posições

Tipo: Numérico

__MFS\-17592__

__RN08__

__Header \- Regra para o campo Data da geração do arquivo__

Nesse campo será informado a Data em que o arquivo foi gerado\. Esse campo será preenchido com a Data Inicial da tela de geração do meio magnético\.

Campo: Obrigatório

Formato: DDMMAAAA

Tamanho: 8 posições

Tipo: Data

__MFS\-17592__

__RN09__

__Header \- Regra para o campo CPF ou CNPJ do tomador dos serviços __

Nesse campo será informado o CPF ou CNPJ do tomador com 11 ou 14 caracteres respectivamente, contendo apenas números, sem nenhum separador\. Preencher com a informação do campo __CGC__ da tabela __ESTABELECIMENTO\.__

Campo: Obrigatório

Formato: XXXXXXXXXXXXXX 

Tamanho: 11\(CPF\) 14 posições \(CNPJ\)

Tipo: Alfanumérico

__MFS\-17592__

__RN10__

__Header \- Regra para o campo Inscrição municipal do tomador dos serviços__

Nesse campo será informado a Inscrição municipal do tomador contendo apenas números, sem nenhum separador\. Preencher com a informação do campo __INSC\_MUNICIPAL__ da tabela __ESTABELECIMENTO\.__

Campo: Obrigatório

Formato: XXXXXXXXXXXXXX 

Tamanho: 20 posições

Tipo: Alfanumérico

__MFS\-17592__

__RN11__

__Header \- Regra para o campo Razão Social ou Nome Completo do tomador dos serviços __

Nesse campo será informado a Razão Social ou Nome do tomador\. Preencher com a informação do campo __RAZAO\_SOCIAL__ da tabela __ESTABELECIMENTO\.__

Campo: Obrigatório

Formato: XXXXXXXXXXXXXX

Tamanho: 70 posições

Tipo: Alfanumérico

__MFS\-17592__

__RN12__

__Header \- Regra para o campo Competência __

__\[MFS86449\] __Criação de uma regra geral para preencher o campo Competência houver quebra por Data de Emissão, independente do município da geração\.

Nesse campo será informado a Competência dos serviços tomados\. 

Se o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado

      Preencher com o mês/ano referente à data de emissão das notas fiscais contidas no arquivo

Senão

      Preencher com a informação da Data Inicial da tela de geração do meio magnético\.

Campo: Obrigatório

Formato: MMAAAA

Tamanho: 6 posições

Tipo: Data

__MFS\-17592__

__MFS\-86449__

__RN13__

__Detalhe \- Regra para o campo Identificação do Registro Detalhe__

Preencher o campo com o valor __“B”\.__

Campo: Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico 

__MFS\-17592__

__RN14__

__Detalhe \- Regra para o campo CPF ou CNPJ do prestador dos serviços __

Nesse campo será informado o CPF ou CNPJ do prestador com 11 ou 14 caracteres respectivamente, contendo apenas números, sem nenhum separador\. Preencher com a informação do campo __06 \-__ __CPF\_CGC__ da tabela __SAFX04\.__

Campo: Obrigatório

Formato: XXXXXXXXXXXXXX

Tamanho: 11\(CPF\) 14 posições \(CNPJ\)

Tipo: Alfanumérico

__MFS\-17592__

__RN15__

__Detalhe \- Regra para o campo Razão Social ou Nome Completo do prestador dos serviços __

Nesse campo será informado a Razão Social ou Nome do prestador\. Preencher com a informação do campo __05 \-__ __RAZAO\_SOCIAL__ da tabela __SAFX04__

Campo: Obrigatório

Formato: XXXXXXXXXXXXXX

Tamanho: 70 posições

Tipo: Alfanumérico

__MFS\-17592__

__RN16__

__Detalhe \- Regra para o campo Número do documento Fiscal__

Nesse campo será informado o número do documento fiscal\. Preencher com o campo __08 \- NUM\_DOCFIS \(SAFX07\)__ da tabela __DWT\_DOCTO\_FISCAL\.__

Campo: Obrigatório

Formato: XXXXXXXXXXXXXX

Tamanho: 20 posições

Tipo: Alfanumérico

__MFS\-17592__

__RN17__

__Detalhe \- Regra para o campo Série do documento Fiscal__

Nesse campo será informado a série do documento fiscal\. Preencher com o campo __09 \- SERIE\_DOCFIS \(SAFX07\)__ da tabela __DWT\_DOCTO\_FISCAL\.__

__ __

Formato: XXXXX 

Tamanho: 5 posições

Tipo: Alfanumérico

__MFS\-17592__

__RN18__

__Detalhe \- Regra para o campo Data de emissão do documento Fiscal__

Nesse campo será informado a Data de emissão do documento fiscal\. Preencher com o campo __11 \-__ __DATA\_EMISSAO \(SAFX07\)__ da tabela __DWT\_DOCTO\_FISCAL\.__

__ __

Campo: Obrigatório

Formato: DDMMAAAA 

Tamanho: 8 posições

Tipo: Data

__MFS\-17592__

__RN19__

__Detalhe \- Regra para o campo Data da quitação do documento Fiscal__

Nesse campo será informado a Data em que foi realizada a quitação dos serviços pelo tomador\. Preencher com o campo __175 –__ __DT\_PAGTO\_NF __da tabela__ \(SAFX07\)\. __Se o campo estiver em branco no documento fiscal, informe “00000000” 

__ __

Campo: Obrigatório

Formato: DDMMAAAA 

Tamanho: 8 posições

Tipo: Data

__MFS\-17592__

__RN20__

__Detalhe \- Regra para o campo Valor do documento fiscal__

Nesse campo será informado o valor da NF, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __VLR\_TOT__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘345678912345’\. 

- Se o campo não estiver preenchido ou ultrapassar o tamanho permitido, emitir a mensagem no log*: O campo “Valor do documento fiscal” está com tamanho acima do máximo permitido \(12 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.*

Campo: Obrigatório

Formato: 999999999999 

Tamanho: 12 posições 

Tipo: Numérico Decimal

__MFS\-17592__

__RN21__

__Detalhe \- Regra para o campo Valor da base de cálculo do ISS__

Nesse campo será informado o valor da base de cálculo do ISS, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __VLR\_BASE\_ISS\_1__ da tabela __DWT\_ITENS\_SERV\. Ou__

__   Se __caso__ o campo  VLR\_BASE\_ISS\_1__ da tabela __DWT\_ITENS\_SERV __estiver com zeros ou em branco\.

    __Preencher __com o campo__ VLR\_BASE\_ISS\_RETIDO__ da tabela __DWT\_ITENS\_SERV__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘345678912345’\. 

- Se o campo não estiver preenchido ou ultrapassar o tamanho permitido, emitir a mensagem no log*:* *O campo “Valor da base de cálculo do ISS” está com tamanho acima do máximo permitido \(12 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.*

Campo: Obrigatório

Formato: 999999999999 

Tamanho: 12 posições 

Tipo: Numérico Decimal

__MFS\-527914__

__RN22__

__Detalhe \- Regra para o campo Alíquota do ISS__

Nesse campo será informado o valor da Alíquota do ISS, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV__\. __Ou__

__   Se __caso__ o campo  ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV __estiver com zeros ou em branco\.

    __Preencher __com o campo__ VLR\_ALIQ\_ISS\_RETIDO__ da tabela __DWT\_ITENS\_SERV__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 3,4 \(3 inteiros/ 4 decimais\), então para atender a obrigação deverá ser desconsiderada a primeira posição do número inteiro e as duas últimas da parte decimal para atender o tamanho exigido pela Prefeitura\. *Exemplo:* Para o valor de 123,4567 deverá ser informado: 2345
- Se o campo não estiver preenchido ou ultrapassar o tamanho permitido, emitir a mensagem no log*: O campo “Alíquota do ISS” está com tamanho acima do máximo permitido \(4 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.*

Campo: Obrigatório

Formato: 9999 exemplos: 745 / 1000

Tamanho: 4 posições 

Tipo: Numérico Decimal

__MFS\-17592__

__MFS\-527914__

__RN23__

__Detalhe \- Regra para o campo Valor do ISS__

Nesse campo será informado o valor do ISS, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __VLR\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV\. Ou__

__   Se __caso__ o campo VLR\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV __estiver com zeros ou em branco\.

    __Preencher __com o campo__ VLR\_ISS\_RETIDO__ da tabela __DWT\_ITENS\_SERV__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘345678912345’\. 

- Se o campo não estiver preenchido ou ultrapassar o tamanho permitido, emitir a mensagem no log*:* *O campo “Valor do ISS” está com tamanho acima do máximo permitido \(12 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.*

Campo: Obrigatório

Formato: 999999999999 

Tamanho: 12 posições 

Tipo: Numérico Decimal

__MFS\-17592__

__MFS\-527914__

__RN24__

__Detalhe \- Regra para o campo Optante Simples Nacional__

Nesse campo será informado se o Prestador de serviço faz parte do programa Simples Nacional\. 

Preencher com:

__“S” \- Sim\.__

Verificar se o campo IND\_SIMPLES\_NAC __\(campo 43 da tabela SAFX04\)__ é igual a “S”\.

Senão, preencher com:

__“N” – Não__

Campo: Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS\-17592__

__RN25__

__Regra para o campo Código do Serviço__

Nesse campo será informado item de serviço do documento fiscal\. Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal, sem pontos ou vírgulas\. 

__Tratamento:__

Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0000 \(zeros\) e emitida a mensagem de log: “*O código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal não está preenchido, favor verificar”\.*

Campo: Obrigatório

Formato: 9999 – Exemplo: 0202

Tamanho: 4 posições

Tipo: Numérico

__MFS\-17592__

__RN26__

__Footer \- Regra para o campo Identificação do registro Footer__

Preencher o campo com o valor __“C”\.__

Campo: Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico 

__MFS\-17592__

__RN27__

__Footer \- Regra para o campo Quantidade de registros do tipo “B” \(Detalhe\)__

Esse campo deve ser preenchido com a quantidade de registros gerados no detalhe\.

Campo: Obrigatório

Formato: 999999999

Tamanho: 9 posições

Tipo: Numérico Inteiro 

__MFS\-17592__

__RN28__

__Footer \- Regra para o campo Total de ISS__

Esse campo deve ser preenchido com o valor total de ISS dos documentos fiscais\. O campo necessita ser preenchido com duas casas decimais, mas sem separador de milhar e decimal\.

*Exemplo:* 123456789123\(decimais\)

Campo: Obrigatório

Formato: 999999999999  

Tamanho: 12 posições

Tipo: Numérico Decimal

__MFS\-17592__

__INCLUSÃO – MANAGER__

__CÓD__

__DESCRIÇÃO__

__MFS__

__IM00__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

MFS\-17592

__IM01__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XXXXXX / XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS\-17592

__IM02__

__Código IBGE: 7509 – Município/UF: Catu – BA__

A descrição funcional do módulo será: : __*“*__<a id="_Hlk532471508"></a>__*Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-17592

__IM03__

__Código IBGE: 14703 – Município/UF: Itaberaba – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-17592

__IM04__

__Código IBGE: 22003 – Município/UF: Mucuri – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-17592

__IM05__

__Código IBGE: 29206 – Município/UF: São Francisco do Conde – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-17592

__IM06__

__Código IBGE: 10727 – Município/UF: Eunápolis – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-17592

__IM07__

__Código IBGE: 17508 – Município/UF: Jacobina – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-17592

__IM08__

__Código IBGE: 13200 – Município/UF: Ibotirama – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-17592

__IM09__

__Código IBGE: 17003 – Município/UF: Itiúba – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-17592

__IM10__

__Código IBGE: 10057 – Município/UF: Dias D’Avila – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-22548

__IM11__

__Código IBGE: 3201 – Município/UF: Barreiras – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-22995

__IM12__

__Código IBGE: 100 – Município/UF: Boa Vista – RR__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-28385

__IM12__

__Código IBGE: 23803 – Município/UF: Paripiranga – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-69550

__IM13__

__Código IBGE: 14604 – Município/UF: Irecê – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

MFS\-80404

__IM14__

__Código IBGE: 16302 – Município/UF: Itapebi – BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

__MFS\-99369__

__IM15__

__Código IBGE: 5909 – Município/UF:  Campo Alegre de Lourdes \- BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

__MFS\-788071__

__IM16__

__Código IBGE: 19553 – Município/UF: Luis Eduardo Magalhães \- BA__

A descrição funcional do módulo será: __*“Esse validador consiste em gerar as declarações para os documentos fiscais que tiveram retenção de ISS\. O sistema SAATRI oferece a opção de enviar um arquivo no formato \.txt contendo as declarações dos serviços tomados”\.*__

__MFS\-1048314__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

