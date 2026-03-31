# MTZ_NFTS_ONLINE_Geracao_Meio_Magnetico

- **Fonte:** MTZ_NFTS_ONLINE_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-03-02
- **Tamanho:** 89 KB

---

THOMSON REUTERS

Municipal 

 Serviços Tomados 

	Geração do Meio Magnético – NFTS ONLINE 	

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-17302

João Henrique

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador NFTS ONLINE\.

MFS\-829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Lauro de Freitas” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“A obrigação consiste no envio e processamento da declaração mensal das notas de serviços tomados do município de Lauro de Freitas”\.__

__MFS\-17302__

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “BA” e ao código de município do IBGE igual a “19207” \(Lauro de Freitas\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Lauro de Freitas, Bahia\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-17302__

__RN03__

__Estrutura de menus do módulo __

Deverão ser criados os seguintes menu e sub\-menus no módulo NFTS ONLINE:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda 

__MFS\-17302__

__RN04__

__Regra de criação do nome do arquivo:__

__Serviços Tomados:__

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.CSV__, onde:

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.CSV__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.CSV

__       NFTSONLINE\_MUNICIPIO\_DDMMAAAA\.CSV__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __NFTSONLINE__: representa a obrigação que está sendo gerada\. 

       __\.CSV__: extensão do arquivo\.

*Exemplo:* NFTSONLINE\_LAURODEFREITAS\_01012010\.CSV

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.CSV__, onde:

       __DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.CSV__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.CSV

__NFTSONLINE\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.CSV__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __NFTSONLINE__: representa a obrigação que está sendo gerada\. 

       __\.CSV__: extensão do arquivo\.

       __MMAAAA__: mês da competência referente à nota gerada

*Exemplo:* NFTSONLINE\_LAURODEFREITAS\_01012010\_122009\.CSV

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* __Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

__MFS\-17302__

__MFS829438__

__RN05__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS\-17302__

__RN06__

__Regra p/ Geração do Arquivo Magnético__

1. O formato do arquivo será em \.CSV, os campos serão separados por “; ” \(Ponto e Vírgula\)\.
2. Todos os campos do tipo \(Data\) terão o formado no padrão DD/MM/AAAA\.
3. Os campos de valores monetários \(Valor Total da Nota, Valor Total das Deduções e Valor do ISS\) e o campo de Alíquota serão preenchidos sem separador de milhar e utilizando virgula \(“, ”\) como separador de decimal\. 

__*Observação:*__ Os campos de valores monetários e alíquota caso não atinjam o tamanho exato de posições deverão ser preenchidos com zeros a esquerda\. Caso o conteúdo do campo não seja fornecido, preencher com zeros até atingir o tamanho do campo\.

1. Todos os demais campos numéricos serão preenchidos sem formatação__ \(sem ponto e sem vírgula\) e não serão preenchidos com__ __zeros à esquerda até completar seu tamanho máximo__\. Caso o conteúdo do campo não seja fornecido, preencher com zero\.
2. Os campos do tipo texto \(alfanumérico\) serão preenchidos com espaço em branco, se não houver informação de preenchimento\. 

__MFS\-17302__

__RN07__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\):__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.
- O agrupamento das notas fiscais deverá ser realizado pelos campos: Item Lista de Serviços, Alíquota e ISS retido\.

__MFS\-17302__

__RN08__

__Regra para o campo Tipo da Nota__

Preencher o campo com o valor __“2”__ – NFTS\.

Formato: 9 

Tamanho: 1 posição

Tipo: Numérico

__MFS\-17302__

__RN09__

__Regra para o campo CNPJ Tomador__

Nesse campo será informado o CNPJ da empresa responsável pela geração do arquivo\. Preencher com a informação do campo __CGC __da tabela __ESTABELECIMENTO__\.

Formato: 99999999999999 

Tamanho: 14 posições

Tipo: Numérico

__MFS\-17302__

__RN10__

__Regra para o campo Inscrição Municipal Tomador__

Nesse campo será informado a Inscrição Municipal da empresa responsável pela geração do arquivo\. Preencher com a informação do campo __INSC\_MUNICIPAL__ da tabela __ESTABELECIMENTO\.__

Formato: 9999999999

Tamanho: 10 posições

Tipo: Numérico

__MFS\-17302__

__RN11__

__Regra para o campo CNPJ Prestador__

Nesse campo será informado o CNPJ do Prestador de serviços\. Preencher com a informação do campo __06 \-__ __CPF\_CGC__ da tabela __SAFX04__\.

__Observação: __Se o campo __CPF\_CGC__ for preenchido com o CPF do Prestador \(11 posições\), automaticamente esse campo será preenchido com zero\.

Formato: 99999999999999 

Tamanho: 14 posições

Tipo: Numérico

__MFS\-17302__

__RN12__

__Regra para o campo CPF Prestador__

Nesse campo será informado o CPF do Prestador de serviços\. Preencher com a informação do campo __06 \-__ __CPF\_CGC__ da tabela __SAFX04__\.

__Observação: __Se o campo __CPF\_CGC__ for preenchido com o CNPJ do Prestador \(14 posições\), automaticamente esse campo será preenchido com zero\.

Formato: 99999999999 

Tamanho: 11 posições

Tipo: Numérico

__MFS\-17302__

__RN13__

__Regra para o campo Regime Especial de Tributação__

Nesse campo será informado o indicador do regime especial de tributação do Prestador de serviços\. 

Preencher com:

__“1” \- Microempresa municipal\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “04 – Microempresa \(ME\) ” referente o prestador cadastrado na nota fiscal\.

__“2” \- Estimativa\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “08 \- Regime de Estimativa” referente o prestador cadastrado na nota fiscal\.

__“3” \- Sociedade de Profissionais\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “06 \- Sociedade Profissional” referente o prestador cadastrado na nota fiscal\.

__“4” \- Cooperativa\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “02 \- Cooperativa” __OU__ “05 \- Cooperativa de Transporte” referente o prestador cadastrado na nota fiscal\.

__“5” \- Microempresário Individual \(MEI\)\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “05 – MEI \(Microempreendedor Individual\) ” referente o prestador cadastrado na nota fiscal\.

__“6” \- Microempresário e Empresa de Pequeno Porte \(ME EPP\)\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “01 \- EPP \(Empresa de Pequeno Porte\) ” referente o prestador cadastrado na nota fiscal\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“7” – Nenhum\.__

Campo Obrigatório

Formato: 9 

Tamanho: 1 posição

Tipo: Numérico

__MFS\-17302__

__RN14__

__Regra para o campo Natureza da Operação__

Nesse campo será informado a natureza da operação do Prestador de serviços\. 

Preencher com:

__“1” – Tributado no Município\.__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “471” 

__OU__

Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\) é__ IGUAL __ao município do módulo selecionado\. 

Caso o campo \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\) esteja vazio, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

__“2” – Tributado fora do Município\.__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472” 

__OU__ 

Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\) __é DIFERENTE __do município do módulo selecionado\.

Caso o campo \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\) esteja vazio, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Campo Obrigatório

Formato: 9 

Tamanho: 1 posição

Tipo: Numérico

__MFS\-17302__

__RN15__

__Regra para o campo Razão Social do Prestador__

Nesse campo será informado a razão social do Prestador de serviços\. Preencher com o campo __05 \- RAZAO\_SOCIAL__ da tabela __SAFX04__\.

Formato: XXXXXXXXXXXXXXXXX

Tamanho: 150 posições

Tipo: Texto

__MFS\-17302__

__RN16__

__Regra para o campo Logradouro do Endereço do Prestador__

Nesse campo será informado o logradouro do endereço do Prestador de serviços\. Preencher com o campo __12 \- ENDERECO__ da tabela __SAFX04__\.

Formato: XXXXXXXXXXXXXXXXX 

Tamanho: 100 posições

Tipo: Texto

__MFS\-17302__

__RN17__

__Regra para o campo Número do Endereço do Prestador__

Nesse campo será informado o número do endereço do Prestador de serviços\. Preencher com o campo __13 \- NUM\_ENDERECO__ da tabela __SAFX04__\.

Formato: XXXXXXXXXX 

Tamanho: 10 posições

Tipo: Texto

__MFS\-17302__

__RN18__

__Regra para o campo Complemento do Endereço do Prestador__

Nesse campo será informado o complemento do endereço do Prestador de serviços\. Preencher com o campo __14 \- COMPL\_ENDERECO__ da tabela __SAFX04__\.

Formato: XXXXXXXXXXXXXXXXX

Tamanho: 60 posições

Tipo: Texto

__MFS\-17302__

__RN19__

__Regra para o campo Bairro do Endereço do Prestador__

Nesse campo será informado o complemento do endereço do Prestador de serviços\. Preencher com o campo __15 \- BAIRO__ da tabela __SAFX04__\.

Formato: XXXXXXXXXXXXXXXXX

Tamanho: 60 posições

Tipo: Texto

__MFS\-17302__

__RN20__

__Regra para o campo Município do Endereço do Prestador__

Nesse campo será informado o município do endereço do Prestador de serviços\. Preencher com o campo __16 \- CIDADE__ da tabela __SAFX04__\.

Formato: XXXXXXXXXXXXXXXXX

Tamanho: 30 posições

Tipo: Texto

__MFS\-17302__

__RN21__

__Regra para o campo UF do Endereço do Prestador__

Nesse campo será informado a unidade federativa do endereço do Prestador de serviços\. Preencher com o campo __19 \- UF__ da tabela __SAFX04__\.

Formato: XX

Tamanho: 2 posições

Tipo: Texto

__MFS\-17302__

__RN23__

__Regra para o campo CEP do Endereço do Prestador__

Nesse campo será informado o CEP do endereço do Prestador de serviços\. Preencher com o campo __20 \- CEP__ da tabela __SAFX04__\.

Formato: 99999999

Tamanho: 8 posições

Tipo: Numérico

__MFS\-17302__

__RN24__

__Regra para o campo Prestador é do Simples Nacional__

Nesse campo será informado se o Prestador de serviço faz parte do programa Simples Nacional\. 

Preencher com:

__“S” \- Sim\.__

Verificar se o campo IND\_SIMPLES\_NAC __\(campo 43 da tabela SAFX04\)__ é igual a “S”\.

Senão, preencher com:

__“N” \- Não__

Campo Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Texto

__MFS\-17302__

__RN25__

__Regra para o campo DDD Telefone Prestador__

Nesse campo será informado o DDD do telefone do Prestador de serviços\. Preencher com o campo __22 \- DDD__ da tabela __SAFX04__\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 3 inteiros, então para atender a obrigação deverá ser desconsiderada a primeira posição do número inteiro para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 011, gravar 11\.

O usuário poderá preencher Ex: “11” direto no campo\.

Formato: 99

Tamanho: 2 posições

Tipo: Numérico

__MFS\-17302__

__RN26__

__Regra para o campo Número Telefone Prestador__

Nesse campo será informado o número do telefone do Prestador de serviços\. Preencher com o campo __23 \- TELEFONE__ da tabela __SAFX04__\.

Formato: 999999999

Tamanho: 9 posições

Tipo: Numérico

__MFS\-17302__

__RN27__

__Regra para o campo E\- mail Prestador__

Nesse campo será informado o e\-mail do endereço do Prestador de serviços\. Preencher com o campo __40 – E\_MAIL__ da tabela __SAFX04__\.

Formato: XXXXXXXXXXXXXXXXX

Tamanho: 80 posições

Tipo: Texto

__MFS\-17302__

__RN28__

__Regra para o campo Data da Prestação dos Serviços__

Nesse campo será informado a data da prestação do serviço\. Preencher com o campo __DATA\_FISCAL__ da tabela __DWT\_DOCTO\_FISCAL\.__

__ __

Formato: DD/MM/AAAA

Tamanho: 8 posições

Tipo: Data

__MFS\-17302__

__RN29__

__Regra para o campo__ __Tipo do Documento Fiscal__

Nesse campo o usuário poderá informar o Tipo do Documento Fiscal que este campo pode assumir, carregada na __TFIX84__ \(Cadastro dos Tipos de Documento das Obrigações \- __PRT\_TP\_DOCTO\_OBRIG__\.

Preencher com:

__“1”__ – Documento Fiscal Emitido por Outro Município\.

__“2”__ – Dispensado de Emissão de Documento Fiscal\.

__“3”__ – Sem Emissão de Documento Fiscal Embora Obrigatório\.

__Tratamento:__

- Parametrização de Tipo Docto Msaf x Tipo Documento:

Preencher com o campo Tipo Documento da tela Municipal – Parâmetros por Município – Tipo Docto Msaf x Tipo Documento referente ao Código do Tipo do Documento cadastrado na nota\.

- Se não existir parametrização para o Tipo do Documento informado na nota, o sistema deve exibir no log a seguinte mensagem: *“Para o Tipo Documento XXXXX", não foi localizada a parametrização de Tipo Docto Msaf x Tipo Documento\.  Módulo: Parâmetros para Município \- Menu: Parâmetros \-\-> Tipo Docto Msaf x Tipo Documento\. ”\.*

Campo Obrigatório\.

Formato: 9

Tamanho: 1 posições

Tipo: Numérico

__MFS\-17302__

__RN30__

__Regra para o campo Número do Documento Fiscal__

Nesse campo será informado o número do documento fiscal\. Preencher com o campo __NUM\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL\.__

__ __

Formato: XXXXXXXXXX

Tamanho: 10 posições

Tipo: Texto

__MFS\-17302__

__RN31__

__Regra para o campo Série do Documento Fiscal__

Nesse campo será informado a série do documento fiscal\. Preencher com o campo __SERIE\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL\.__

__ __

Formato: XXXXXXXXXX

Tamanho: 10 posições

Tipo: Texto

__MFS\-17302__

__RN32__

__Regra para o campo Código CNAE Prestador__

Nesse campo será o código CNAE do prestador\. Preencher com o campo 07 \- __COD\_ATIVIDADE__ da tabela __SAFX04\.__

__ __

Formato: 9999999999

Tamanho: 10 posições

Tipo: Numérico

__MFS\-17302__

__RN33__

__Regra para o campo Item Lista de Serviços__

Nesse campo será informado item de serviço do documento fiscal\. Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Tratamento:__

Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 00\.00 \(zeros\) e emitida a mensagem de log: “*O código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal não está preenchido, favor verificar”\.*

Campo Obrigatório

Formato: XX\.XX –  Exemplo: 02\.02

Tamanho: 5 posições

Tipo: Texto

__MFS\-17302__

__RN34__

__Regra para o campo Alíquota__

Nesse campo será informado a Alíquota do documento fiscal\. Preencher com o campo __32 __\- __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 3,4 \(3 inteiros/ 4 decimais\), então para atender a obrigação deverão ser desconsideradas a primeira posição do número inteiro e as duas últimas da parte decimal para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123,4567, gravar 23,45

Formato: 99,99

Tamanho: 5 Posições

Tipo: Numérico

__MFS\-17302__

__RN35__

__Regra para o campo Competência \- Ano__

Esse campo será preenchido com o Ano da Data fiscal\.

Formato: 9999

Tamanho: 4 posições

Tipo: Numérico

__MFS\-17302__

__RN36__

__Regra para o campo Competência \- Mês__

Esse campo será preenchido com o Mês da Data Fiscal\.

Formato: 99

Tamanho: 2 posições

Tipo: Numérico

__MFS\-17302__

__RN37__

__Regra para o campo ISS Retido__

Nesse campo será registrado se o ISS será retido ou não pelo município\.

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

__Preencher com__ __‘S’__:

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__ 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, __preencher com__ __“N”\.__

Campo Obrigatório

Formato: X

Tamanho: 1 Posição

Tipo: Texto

__MFS\-17302__

__RN38__

__Regra para o campo Discriminação dos Serviços__

Esse campo será preenchido com a discriminação dos serviços do documento fiscal\. Preencher com o campo __DSC\_SERV\_LEI\_116__ da tabela __DWT\_SERVICO\_LEI\_116__ referente ao\(s\) serviço\(s\) cadastrado\(s\) no item da nota fiscal\.

Formato: XXXXXXXXXXXXXXXXXX

Tamanho: 500 posições

Tipo: Texto

__MFS\-17302__

__RN39__

__Regra para o campo Outras Informações__

Esse campo será preenchido com informações referente ao documento fiscal\. Preencher com o campo __OBS\_INF\_ADIC\_NF __da tabela __DWT\_DOCTO\_FISCAL\.__

Formato: XXXXXXXXXXXXXXXXXX

Tamanho: 200 posições

Tipo: Texto

__MFS\-17302__

__RN40__

__Regra para o campo Valor Total da Nota__

Esse campo será apresentado com o Valor Total das Nota Fiscal\. Preencher com a informação do campo __VLR\_TOT__ da tabela __DWT\_ITENS\_SERV\. __

__Tratamentos:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456,45’\.

- Se o campo Valor Total da Nota estiver com o tamanho acima do máximo permitido \(13,2 posições\), exibir uma mensagem no log: *“O campo Valor Total da Nota está com o tamanho acima do permitido, favor verificar”\.*
- Se o campo não possuir valor, __preencher com zero__, conforme instrução do manual de importação\.

Formato: 9999999999999,99 \- Exemplo: 1\.234,56\.

Tamanho: 13,2 posições

Tipo: Numérico

__MFS\-17302__

__RN41__

__Regra para o campo Valor Total das Deduções __

Esse campo será apresentado com o total das deduções dos documentos fiscais\. Preencher com o somatório do campo__  __ __VLR\_DEDUCAO\_ISS __da tabela __DWT\_ITENS\_SERV__\.

__Tratamentos:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456,45’\.

- Se o campo Valor Total das Deduções estiver com o tamanho acima do máximo permitido \(13,2 posições\), exibir uma mensagem no log: *“O campo Valor Total das Deduções está com o tamanho acima do permitido, favor verificar”\.*
- Se o campo não possuir valor, __preencher com zero__, conforme instrução do manual de importação\.

Formato: 9999999999999,99 \- Exemplo: 1\.234,56\.

Tamanho: 13,2 posições

Tipo: Numérico

__MFS\-17302__

__RN42__

__Regra para o campo Valor do ISS__

Esse campo será apresentado com o Valor do ISS dos documentos fiscais\. Preencher com o somatório do campo __VLR\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamentos:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456,45’\.

- Se o campo Valor do ISS estiver com o tamanho acima do máximo permitido \(13,2 posições\), exibir uma mensagem no log: *“O campo Valor do ISS está com o tamanho acima do permitido, favor verificar”\.*
- Se o campo não possuir valor, __preencher com zero__, conforme instrução do manual de importação\.

Formato: 9999999999999,99 \- Exemplo: 1\.234,56 

Tamanho: 13,2 posições

Tipo: Numérico

__MFS\-17302__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

