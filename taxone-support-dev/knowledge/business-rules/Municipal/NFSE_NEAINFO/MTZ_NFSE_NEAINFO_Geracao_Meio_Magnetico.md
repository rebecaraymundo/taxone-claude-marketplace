# MTZ_NFSE_NEAINFO_Geracao_Meio_Magnetico

- **Fonte:** MTZ_NFSE_NEAINFO_Geracao_Meio_Magnetico.docx
- **Modificado:** 2021-01-21
- **Tamanho:** 93 KB

---

THOMSON REUTERS

Municipal 

 Serviços Tomados 

	Geração do Meio Magnético – NFSE NEAINFO	

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS19945

Andréa Rocha

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador NFSE NEAINFO\.

MFS19945

Aline Melo

Ajuste finais no documento de geração do meio magnético\.

MFS58123

Andréa Rocha

Alteração da regra de recuperação dos serviços tomados para desconsiderar as notas fiscais emitidas no município\.

MFS57985

Andréa Rocha

Alteração da regra de preenchimento do campo Série\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão dos novos módulos no Manager:__

O novo módulo: “Três Lagoas” devem ficar localizados no grupo “Municipal”\.

A descrição funcional do módulo será: __*“Consiste na entrega das informações sobre os serviços tomados do município de Três Lagoas”\.*__

__MFS19945__

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MS” e ao código de município do IBGE igual a: “8305” \(Três Lagoas\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

__Exemplo:__ “Este estabelecimento não pertence ao município de Três Lagoas\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS19945__

__RN03__

__Estrutura de menus do módulo __

Deverão ser criados os seguintes menu e sub\-menus no módulo NFSE NEAINFO:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)__
- Janela
- Ajuda 

__MFS19945__

__RN04__

__Regra de criação do nome do arquivo:__

__Serviços Tomados:__

__       NFSENEAINFO\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __NFSENEAINFO__: representa a obrigação que está sendo gerada\. 

       __\.TXT__: extensão do arquivo\.

*Exemplo:* __NFSENEAINFO__\_TRES\_LAGOAS\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__NFSENEAINFO\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __NFSENEAINFO__: representa a obrigação que está sendo gerada\. 

       __\.TXT__: extensão do arquivo\.

       __MMAAAA__: mês da competência referente à nota gerada

*Exemplo:* __NFSENEAINFO__\_TRES\_LAGOAS\_01012010\_122009\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* __Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

__MFS19945__

__RN05__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS19945__

__RN06__

__Regra p/ Geração do Arquivo Magnético__

1. O formato do arquivo será em \.TXT\.
2. Todos os campos do tipo \(Data\) têm o formado no padrão DD/MM/AAAA\.
3. Todos os campos do tipo \(Alfanumérico\) são preenchidos com espaços em branco à direita quando não alcançar o tamanho exato do campo\.
4. Todos os campos do tipo \(Numérico\) são preenchidos com zeros à esquerda quando não alcançar o tamanho exato do campo\.

__*Observação:*__ Para os campos numéricos nenhum separador de milhar e decimal devem ser informados\.

__MFS19945__

__RN07__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\):__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.
- Recuperar apenas notas fiscais com retenção do ISS \(campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV > 0\)
- O agrupamento das notas fiscais deverá ser realizado pelos campos: Código Atividade e Alíquota\.

__\[MFS58123\]__ Desconsiderar as NFS\-e emitidas no próprio município 

- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

__MFS19945__

__MFS58123__

__RN08__

__Cabeçalho \- Regra para o campo Identificação __

Preencher o campo com o valor __“A”\.__

Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico 

__MFS19945__

__RN09__

__Cabeçalho \- Regra para o campo Tipo de Nota__

Preencher o campo com o valor __“R”\.__

Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS19945__

__RN10__

__Cabeçalho \- Regra para o campo Nome da Empresa__ 

Nesse campo será informado a Razão Social ou Nome do tomador\. Preencher com a informação do campo __RAZAO\_SOCIAL__ da tabela __ESTABELECIMENTO\.__

Obrigatório

Formato: X

Tamanho: 60 posições

Tipo: Alfanumérico

__MFS19945__

__RN11__

__Cabeçalho__ __\- Regra para o campo CPF ou CNPJ __

Nesse campo será informado o CPF ou CNPJ do tomador com 11 ou 14 caracteres respectivamente, contendo apenas números, sem nenhum separador\. Preencher com a informação do campo __CGC__ da tabela __ESTABELECIMENTO\.__

Obrigatório

Formato: XXXXXXXXXXXXXX 

Tamanho: 11\(CPF\) 14 posições \(CNPJ\)

Tipo: Alfanumérico

__MFS19945__

__RN12__

__Cabeçalho \- Regra para o campo Data Emissão Inicial__ 

Nesse campo será informado a Data inicial em que o arquivo foi gerado\. Esse campo será preenchido com a Data Inicial da tela de geração do meio magnético\.

Obrigatório

Formato: DD/MM/AAAA

Tamanho: 10 posições

Tipo: Data

__MFS19945__

__RN13__

__Cabeçalho \- Regra para o campo Data Emissão Final__ 

Nesse campo será informado a Data final em que o arquivo foi gerado\. Esse campo será preenchido com a Data Inicial da tela de geração do meio magnético\.

Obrigatório

Formato: DD/MM/AAAA

Tamanho: 10 posições

Tipo: Data

__MFS19945__

__RN14__

__Cabeçalho \- Regra para o campo Quantidade de Notas__ __ __

Esse campo deve ser preenchido com a quantidade total de notas geradas no detalhe\.

Obrigatório

Formato: 99999

Tamanho: 5 posições

Tipo: Numérico Inteiro

__MFS19945__

__RN15__

__Cabeçalho \- Regra para o campo Valor Total das Notas__ 

Esse campo deve ser preenchido com o valor total dos documentos fiscais\. O campo necessita ser preenchido com duas casas decimais, mas sem separador de milhar e decimal\.

Obrigatório

Formato: 99999999999

Tamanho: 11 posições

Tipo: Numérico Decimal__ __

__MFS19945__

__RN16__

__Detalhe \- Regra para o campo Identificação__

Preencher o campo com o valor __“B”\.__

Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS19945__

__RN17__

__Detalhe \- Regra para o campo Data de emissão__

Nesse campo será informado a Data de emissão do documento fiscal\. Preencher com o campo __11 \-__ __DATA\_EMISSAO \(SAFX07\)__ da tabela __DWT\_DOCTO\_FISCAL\.__

__ __

Obrigatório

Formato: DD/MM/AAAA 

Tamanho: 10 posições

Tipo: Data

__MFS19945__

__RN18__

__Detalhe \- Regra para o campo Série do documento Fiscal__

Preencher com o campo Série da tela Parâmetros por Município – Parâmetros – Modelo Msaf x Série referente ao modelo cadastrado na nota fiscal\.

__\[MFS57985\]__ Utilização da parametrização Série Msaf x Série

Se o campo Modelo de Documento \(COD\_MODELO\) da tabela DWT\_DOCTO\_FISCAL não estiver preenchido

    Preencher com o campo Série da tela Parâmetros por Município – Parâmetros – Série Msaf x Série referente a série cadastrada   

   na nota fiscal

   Se a Série \(SERIE\_DOCFIS\) da tabela DWT\_DOCTO\_FISCAL não estiver preenchida

        Preencher com o campo Série da tela Parâmetros por Município – Parâmetros – Série Msaf x Série referente ao campo série 

        em branco na nota fiscal \(a parametrização permite que se cadastre o campo Série Msaf com um espaço em branco e a     

        relacione a uma série da lista disponível\)

Quando não houver parametrização para o modelo da nota fiscal e para a série da nota fiscal, deve\-se exibir a seguinte mensagem: “O modelo não está parametrizado em Parâmetros por Município – Parâmetros – Modelo Msaf x Série\. Ou a série não está parametrizada em Parâmetros por Município – Parâmetros – Série Msaf x Série\. Favor verificar” e o arquivo deve ser gerado\.

Formato: XXXXX 

Tamanho: 3 posições

Tipo: Alfanumérico

__MFS19945__

__MFS57985__

__RN19__

__Detalhe \- Regra para o campo Número da Nota Fiscal__

Nesse campo será informado o número do documento fiscal\. Preencher com o campo __08 \- NUM\_DOCFIS \(SAFX07\)__ da tabela __DWT\_DOCTO\_FISCAL\.__

Obrigatório 

Formato: XXXXXXXXXXXXXX

Tamanho: 10 posições

Tipo: Alfanumérico

__MFS19945__

__RN20__

__Detalhe \- Regra para o campo Natureza de Operação __

Preencher com:

“__C__” __*\- Isenta/Não Tributável*__ 

Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município da pessoa fis/jur cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”; 

“__Y__” \-__* Com Deduções*__

Verificar se o serviço cadastrado na nota e o município da pessoa fis/jur cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = ‘550 ’e se o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV está preenchido em um dos itens do documento fiscal OU

Se o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e se o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV está preenchido no item do documento fiscal;

“__B__” \-__* Construção Civil*__

Se o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota E se o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV não  estiver preenchido no item do documento fiscal;

“__A__” \-__* Sem Deduções*__

Se o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota E se o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV  não estiver preenchido  no item do documento fiscal

OU se nenhuma das regras acima for atendida\.

Obrigatório 

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS19945__

__RN21__

__Detalhe \- Regra para o campo Valor total da NF__ 

Nesse campo será informado o valor da NF, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __VLR\_TOT__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘45678912345’\. 

- Se o campo não estiver preenchido ou ultrapassar o tamanho permitido, emitir a mensagem no log*: O campo “Valor do documento fiscal” está com tamanho acima do máximo permitido \(11 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.*

Campo Obrigatório

Formato: 99999999999 

Tamanho: 11 posições 

Tipo: Numérico Decimal

__MFS19945__

__RN22__

__Detalhe \- Regra para o campo Valor do Serviço__ 

Nesse campo será informado o valor do serviço, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __VLR\_SERVICO __da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘45678912345’\. 

- Se o campo não estiver preenchido ou ultrapassar o tamanho permitido, emitir a mensagem no log*: O campo “Valor do serviço” está com tamanho acima do máximo permitido \(11 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.*

Campo Obrigatório

Formato: 99999999999 

Tamanho: 11 posições 

Tipo: Numérico Decimal

__MFS19945__

__RN23__

__Detalhe \- Regra para o campo Alíquota ISS__

Nesse campo será informado o valor da Alíquota do ISS, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV__\. 

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 3,4 \(3 inteiros/ 4 decimais\), então para atender a obrigação deverá ser desconsiderada a primeira posição do número inteiro e as duas últimas da parte decimal para atender o tamanho exigido pela Prefeitura\. *Exemplo:* Para o valor de 123,4567 deverá ser informado: 2345
- Se o campo não estiver preenchido ou ultrapassar o tamanho permitido, emitir a mensagem no log*: O campo “Alíquota do ISS” está com tamanho acima do máximo permitido \(4 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.*

Campo Obrigatório

Formato: 9999 exemplos

Tamanho: 4 posições 

Tipo: Numérico Decimal

__MFS19945__

__RN24__

__Detalhe \- Regra para o campo Valor ISS__

Nesse campo será informado o valor do ISS, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __VLR\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘45678912345’\. 

- Se o campo não estiver preenchido ou ultrapassar o tamanho permitido, emitir a mensagem no log*:* *O campo “Valor do ISS” está com tamanho acima do máximo permitido \(12 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.*

Campo Obrigatório

Formato: 99999999999 

Tamanho: 11 posições 

Tipo: Numérico Decimal

__MFS19945__

__RN25__

__Detalhe \- Regra para o campo Tipo de Recolhimento__ 

\(A \- A Recolher, R \- ISS Retido \)

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido,

recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado

    Preencher com “A”

Senão

    Preencher com “R”

Campo Obrigatório

Formato: X 

Tamanho: 1 posição 

Tipo: Alfanumérico

__MFS19945__

__RN26__

__Detalhe \- Regra para o campo Nome do Prestador do Serviço __

Nesse campo será informado a Razão Social ou Nome do prestador\. Preencher com a informação do campo __05 \-__ __RAZAO\_SOCIAL__ da tabela __SAFX04__

Obrigatório

Formato: XXXXXXXXXXXXXX

Tamanho: 60 posições

Tipo: Alfanumérico

__MFS19945__

__RN27__

__Detalhe \- Regra para o campo Tipo de Cadastro__ 

\(F – Pessoa Física, J – Pessoa Jurídica\)

Preencher com:

F, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota tiver 11 posições 

J, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota tiver 14 posições

Obrigatório 

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS19945__

__RN28__

__Detalhe \- Regra para o campo CNPJ/CPF__ 

Nesse campo será informado o CPF ou CNPJ do prestador com 11 ou 14 caracteres respectivamente, contendo apenas números, sem nenhum separador\. Preencher com a informação do campo __06 \-__ __CPF\_CGC__ da tabela __SAFX04\.__

Obrigatório

Formato: XXXXXXXXXXXXXX

Tamanho: 11\(CPF\) 14 posições \(CNPJ\)

Tipo: Alfanumérico

__MFS19945__

__RN29__

__Detalhe \- Regra para o campo Nome de Fantasia__ 

Nesse campo será informado o nome fantasia do prestador\. Preencher com o campo __11\-__ __NOME\_FANTASIA __da tabela __SAFX04\.__

__ __

Formato: XXXXXXXXXX

Tamanho: 60 posições

Tipo: Alfanumérico

__MFS19945__

__RN30__

__Detalhe \- Regra para o campo Nome da Rua__

Nesse campo será informado o endereço do prestador\. Preencher com o campo __12 \-__ __ENDERECO __da tabela __SAFX04\.__

__ __

Obrigatório

Formato: XXXXXXXXXX 

Tamanho: 60 posições

Tipo: Alfanumérico

__MFS19945__

__RN31__

__Detalhe \- Regra para o campo Número__

Nesse campo será informado o número do endereço do prestador\. Preencher com o campo __13 \-__ __NUM\_ENDERECO __da tabela __SAFX04\.__

__ __

Formato: XXXXXXXXXX 

Tamanho: 10 posições

Tipo: Alfanumérico

__MFS19945__

__RN32__

__Detalhe \- Regra para o campo Complemento__

Nesse campo será informado o complemento do prestador\. Preencher com o campo __14 \-__ __COMPL\_ENDERECO __da tabela __SAFX04\.__

__ __

Formato: XXXXXXXXXX 

Tamanho: 30 posições 

Tipo: Alfanumérico

__MFS19945__

__RN33__

__Detalhe \- Regra para o campo CEP__

Nesse campo será informado o CEP do prestador\. Preencher com o campo __20 –__ __CEP __da tabela __SAFX04\.__

Formato: XXXXXXXX

Tamanho: 8 posições 

Tipo: Alfanumérico

__RN34__

__Detalhe \- Regra para o campo Nome do Bairro__

Nesse campo será informado o bairro do prestador\. Preencher com o campo __15 –__ __BAIRRO __da tabela __SAFX04\.__

Formato: XXXXXXXXXX

Tamanho: 40 posições 

Tipo: Alfanumérico

__MFS19945__

__RN35__

__Detalhe \- Regra para o campo Nome da Cidade__

Nesse campo será informado a cidade do prestador\. Preencher com o campo __16 –__ __CIDADE __da tabela __SAFX04\.__

Obs\.: Sem acentuação e maiúsculo 

Ex\.: Três Lagoas \- TRES LAGOAS  

Formato: XXXXXXXXXX 

Tamanho: 40 posições 

Tipo: Alfanumérico

__MFS19945__

__RN36__

__Detalhe \- Regra para o campo UF__

Nesse campo será informado a UF do prestador\. Preencher com o campo __19 – UF__ da tabela __SAFX04\.__

Formato: XX

Tamanho: 2 posições

Tipo: Alfanumérico

__MFS19945__

__RN37__

__Regra para o campo Telefone__

Nesse campo será informado o telefone do prestador\. Preencher com os campos __22 \- DDD__ \+ __23 \- TELEFONE__ da tabela __SAFX04\.__

Formato: XXXXXXXXXX

Tamanho: 20 posições

Tipo: Alfanumérico

__MFS19945__

__RN38__

__Regra para o campo E\-mail__

Nesse campo será informado o e\-mail do prestador\. Preencher com o campo __40 – E\_MAIL__ da tabela __SAFX04\.__

Formato: XXXXXXXXXX

Tamanho: 60 posições

Tipo: Alfanumérico 

__MFS19945__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

