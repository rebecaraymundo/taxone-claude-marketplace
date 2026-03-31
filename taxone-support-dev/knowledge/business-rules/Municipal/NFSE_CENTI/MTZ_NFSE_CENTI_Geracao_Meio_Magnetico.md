# MTZ_NFSE_CENTI_Geracao_Meio_Magnetico

- **Fonte:** MTZ_NFSE_CENTI_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-10-08
- **Tamanho:** 202 KB

---

THOMSON REUTERS

 NFS\-e \- CENTI \- Geração do Meio Magnético

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS35958

Andréa Rocha

Este documento tem como objetivo criar o novo módulo que permita a geração do meio magnético CENTI, que irá conter as informações de serviços prestados e de serviços contratados, assim como serviços bancários\.

MFS47226

Andréa Rocha

Este documento tem como objetivo alterar a regra de recuperação dos serviços tomados\.

MFS66260

Elisabete Costa

Este documento tem como objetivo alterações na estrutura do layout  para o município de __Rio Verde \- GO__

MFS68229

Elisabete Costa

Este documento tem como objetivo a inclusão de um novo município para a geração do meio magnético do NFSE CENTI \-  __Itumbiara \- GO__

__MFS75582__

Rogério Ohashi

Este documento tem como objetivo alterar o preenchimento do campo “Valor do Documento” e “Valor do Serviço”, incluindo o separador da casa decimal ‘\.’ – Específico para o município de __Rio Verde__\. \(RN29\.a e RN36\.a\)

__MFS77454__

Rogério Ohashi

Este documento tem como objetivo alterar o preenchimento do campo “*Serviços – CNAE/SERVICO*” para completar com zeros a esquerda e sem pontos, se necessário – Específico para o município de __Rio Verde__\. \(RN35\.a\)

MFS80634

Alessandra Cristina Navatta 

Este documento tem como objetivo a inclusão de um novo município para a geração do meio magnético do NFSE CENTI \-  Formosa – GO\.

Tornar as regras RN11, RN29\.a, RN36\.a e RN35\.a genéricas, por consequência as RNs 29, 36 e 35 foram excluídas

\(RN11, RN29, RN29\.a, RN36, RN36\.a, RN35,RN35\.a, RN50 e RN51\)\.

MFS86515

Rogério Ohashi

Este documento tem como objetivo alterar o preenchimento do campo “Valor do Serviço”, __retirando__ o separador da casa decimal ‘\.’ – Específico para o município de __Rio Verde__\. \(RN36\.a\)\.

MFS706036

Bruna Ribeiro

Este documento tem como objetivo a readequação da regra para preenchimento do campo indicador de localização da prestação do serviço, passando a verificar também o preenchimento do campo município de destino na capa da nota fiscal\.

MFS829438

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo: “Rio Verde” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados, assim como serviços bancários\.”*\.*

__MFS35958__

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “GO” e ao código de município do IBGE igual a: “18805” \(Rio Verde\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

__Exemplo:__ “Este estabelecimento não pertence ao município de Rio Verde\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS35958__

__RN03__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo: __“Itumbiara”__ deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados, assim como serviços bancários\.”*\.*

__MFS35958__

__MFS68229__

__RN04__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“GO”__ e ao código de município do IBGE igual a: __“11503” \(Itumbiara\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

__Exemplo:__ “Este estabelecimento não pertence ao município de __Itumbiara\.__ Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS35958__

__MFS68229__

__RN05__

__Estrutura de menus do módulo __

Deverão ser criados os seguintes menu e sub\-menus no módulo NFSE CENTI:

- Arquivo
- Manutenção
	- Materiais
- Obrigações
	- Meio Magnético
	- Meio Magnético – Bancos
	- Geração – Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)
- Janela

Ajuda

__MFS35958__

__RN06__

__Regra de criação do nome do arquivo:__

__Serviços prestados:__

__SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __SP__: Apenas registros de serviços prestados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__SP\_CENTI\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __SP\_CENTI__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.

Ex: SP\_CENTI \_01012020\.txt

__Serviços bancários:__

__SB\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __SB__: Registros de Serviços Bancários\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__SB\_CENTI \_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __SB\_CENTI__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.

Ex: SB\_CENTI \_01012020\.txt

__Serviços tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__ST\_CENTI \_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __ST\_CENTI__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.

Ex: ST\_CENTI \_01012020\.txt

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__       ST\_CENTI\_DDMMAAAA\_MMAAAA\.txt__, onde:

__       ST\_CENTI__: representa a obrigação que está sendo gerada\.    \.   

        __DDMMAAAA__: representa a data inicial da geração\.   

__        MMAAAA:__ mês da competência referente à nota gerada

        __\.txt__: extensão do arquivo\.

Ex: ST\_CENTI \_01012010\_122013\.txt

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* __Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

__MFS35958__

__MFS829438__

__RN07__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial__: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final__: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Cód\. de Cidades__: deve ser exibido através de um ListBox, contendo as seguintes opções: IBGE ou SIAFI\.

__Tipo de Serviços__: deve ser exibido através de um ListBox, contendo as seguintes opções: “Cod\. Serviço Lei 116/2003” e “Cod\. de Atividade CNAE”\.

__Gerar Serviços Prestados__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Serviços Tomados__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento__: o sistema deve exibir os estabelecimentos pertencentes ao município em questão, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS35958__

__RN08__

__Regra p/ tela da Geração do Meio Magnético – Bancos__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial__: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final__: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Cód\. de Cidades__: deve ser exibido através de um ListBox, contendo as seguintes opções: IBGE ou SIAFI\.

__Estabelecimento__: o sistema deve exibir os estabelecimentos pertencentes ao município em questão, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS35958__

__RN09__

__Regra p/ Geração do Arquivo Magnético__

1. O arquivo\-texto suportado pela ferramenta de importação do arquivo deve estar conforme o padrão de codificação ANSI\.
2. As informações constantes no arquivo de declaração \(1P \- Serviços Prestados e 1T \- Serviços Tomados\) são referentes aos serviços prestados e tomados pelo declarante \(empresa que está importando o arquivo\)\. Nesse caso, quando for gerado um arquivo do tipo 1P, deverão ser listadas as empresas para as quais foram prestados os serviços\. E, quando for gerado um arquivo do tipo 1T, deverão ser listadas as empresas das quais foram tomados os serviços\.
3. As linhas do arquivo devem sempre iniciar com os algarismos 1, 2, 3, 4 ou 5\. Essa numeração é utilizada para identificar os tipos de registros a serem gravados, sendo eles observáveis na tabela: 1 \- Declaração, 2 \- Documentos, 3 \- Serviços, 4 \- Serviços bancários e 5 \- Materiais\.
4. Os tipos de registro 1, 2 e 3 serão utilizados somente por prestadores/tomadores de serviços comuns\.
5. Os tipos de registro 1 e 4 serão utilizados somente por prestadores enquadrados como declarantes por planos de contas\.
6. O tipo de registro 5 será utilizado somente por prestadores enquadrados como construtoras, possibilitando a declaração dos materiais\.
7. Um arquivo nunca poderá ter tipos de registro 2 e 4 simultaneamente\.
8. O limite de caracteres de cada campo deve sempre ser alcançado\. Quando necessário, deve\-se completá\-lo com espaços em branco\.
9. Para os campos numéricos, nenhum separador de milhar deve ser apresentado\.
10. Nos casos em que somente a declaração dos documentos fiscais seja necessária, o tipo de registro 3 não deve ser apresentado\. Como exemplo, podemos citar os casos de notas fiscais canceladas e anuladas\.
11. Para as notas que tiverem apenas valor referente à venda de mercadorias, sem prestação de serviços, deve ser informado apenas o registro 2\. Se existir venda de mercadorias e prestação de serviços, devem ser informados os registros "2" e "3"\.
12. Todos os tipos de registros de uma nota devem constar no mesmo arquivo, ou seja, cada conteúdo do documento fiscal deve estar em um único arquivo\.

__MFS35958__

__RN10__

__Regra p/ Recuperar notas fiscais de serviços prestados__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

Para cada registro do tipo 2 devem ser gerados os registros do tipo 3 em seqüência\.

2\.\.\.

3\.\.\.

2\.\.\.

3\.\.\.

__MFS35958__

__RN11__

__Regra p/ Recuperar notas fiscais serviços tomados:__

Esses registros apenas devem ser gerados no arquivo quando o campo “Gerar serviços tomados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

\[ALTERAÇÃO __MFS80624\] – Tornar a regra genérica__

__\[MFS47226\] __

__ Desconsiderar as NFS\-e emitidas no próprio município__ __– Específico para Rio Verde/GO, Itumbiara/GO __

- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

Para cada registro do tipo 2 devem ser gerados os registros do tipo 3 em seqüência\. 

2\.\.\.

3\.\.\.

2\.\.\.

3\.\.\.

__MFS35958__

__MFS47226__

__MFS66260__

__MFS68229__

__MFS80624__

__RN12__

__Regra p/ Recuperar notas fiscais de serviços bancários__

Recuperar a movimentação apenas das contas que estão relacionadas as contas referenciais__ __Parâmetros – Serviços Bancários – Plano de Conta Referencial e estas parametrizadas aos serviços na tela de Plano de Contas x Códigos de Serviços, pertencentes à UF e ao município em questão\.

__MFS35958__

__RN13__

__Regra p/ o campo Declaração – Identificador __

Preencher com “1”

Formato: 9

Tamanho: 1 posição

Tipo: Numérico 

__MFS35958__

__RN14__

__Regra p/ o campo Declaração – Tipo __

Preencher com:

P, quando o campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = ‘9’

T, quando o campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> ‘9’

Quando o arquivo for de bancos, preencher sempre com “P”\.

Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS35958__

__RN15__

__Regra p/ o campo Declaração – CodificaçãoCidades__

Preencher com:

1, quando o campo Cod\. De Cidades da tela de geração do meio magnético estiver com a opção “IBGE” escolhida\.

2, quando o campo Cod\. De Cidades da tela de geração do meio magnético estiver com a opção “SIAFI” escolhida\.

Formato: X

Tamanho: 1 posição

Tipo: Numérico

__MFS35958__

__RN16__

__Regra p/ o campo Declaração – CPF/CNPJ __

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração do meio magnético\.

Formato: XXXXXXXXXXXXXX 

Tamanho: 11\(CPF\) 14 posições \(CNPJ\)

Tipo: Alfanumérico

Obs\.: Informar apenas números sem separadores\. Caso a quantidade de caracteres for inferior à 14, completar com ‘0\(zero\)’ a esquerda\.

__MFS35958__

__RN17__

__Regra p/ o campo Declaração – Nome__

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração do meio magnético\.

Formato: X

Tamanho: 50 posições

Tipo: Alfanumérico

__MFS35958__

__RN18__

__Regra p/ o campo Declaração – DataInício__

Preencher com o campo Data Inicial da tela de geração do meio magnético\. 

Formato: DDMMAAAA

Tamanho: 8 posições

Tipo: Data

__MFS35958__

__RN19__

__Regra p/ o campo Declaração – DataFim__

Preencher com o campo Data Final da tela de geração do meio magnético\.

Formato: DDMMAAAA

Tamanho: 8 posições

Tipo: Data

__MFS35958__

__RN20__

__Regra p/ o campo Documentos – Identificador__

Preencher com “2”\.

Formato: 9

Tamanho: 1 posição

Tipo: Numérico 

__MFS35958__

__RN21__

__Regra p/ o campo Documentos – CPF/CNPJ__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

Formato: XXXXXXXXXXXXXX 

Tamanho: 11\(CPF\) 14 posições \(CNPJ\)

Tipo: Alfanumérico__ __

Obs\.: Informar apenas números sem separadores\. Caso a quantidade de caracteres for inferior à 14, completar com ‘0\(zero\)’ a esquerda\.

__MFS35958__

__RN20__

__Regra p/ o campo Documentos – Nome __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

Formato: X

Tamanho: 50 posições

Tipo: Alfanumérico

__MFS35958__

__RN23__

__Regra p/ o campo Documentos – Serie __

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Formato: X

Tamanho: 6 posições

Tipo: Alfanumérico

__MFS35958__

__    RN24__

__Regra p/ o campo Documentos – NrInicio__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

Na geração deste campo, deve ser consideradas 9 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda \(da posição 10 a 12\) devem ser zeros\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 9 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: “O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(9 posições\)\.”

\(Ex: para esta situação: Nº de NF 12345678900 será gerado 345678900\)\.

Obrigatório

Formato: XXXXX 

Tamanho: 9 posições

Tipo: Numérico

__MFS35958__

__RN25__

__Regra p/ o campo __<a id="OLE_LINK22"></a><a id="OLE_LINK23"></a><a id="OLE_LINK24"></a><a id="OLE_LINK25"></a><a id="OLE_LINK26"></a>__Documentos – NrFim__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

<a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a>__Tratamento:__

Na geração deste campo, deve ser consideradas 9 posições da direita para a esquerda do número da NF, <a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>considerando que os caracteres que serão suprimidos à esquerda \(da posição 10 a 12\) devem ser zeros\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 9 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: “O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(9 posições\)\.”

\(Ex para esta situação: Nº de NF 12345678900 será gerado 345678900\)\.

Formato: XXXXX 

Tamanho: 9 posições

Tipo: Numérico

__MFS35958__

__RN26__

__Regra p/ o campo Documentos – DataEmissão__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL

Formato: DDMMAAAA

Tamanho: 8 posições

Tipo: Data

__MFS35958__

__RN27__

__Regra p/ o campo Documentos – TipoDoc__

Preencher com o tipo de documento parametrizado na tela Parâmetros por Município – TFIX84 \- Parâmetros – Tipo Docto Msaf x Tipo Docto referente ao tipo de documento preenchido na nota fiscal\.

Se não existir parametrização para o tipo de documento informado na nota, log do sistema deve exibir a seguinte mensagem: “Para o Tipo Documento “XXX”, não foi localizada a parametrização de Tipo Docto Msaf x Tipo Docto\.”\.

Obrigatório 

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS35958__

__MFS66260__

__MFS68229__

__RN28__

__Regra p/ o campo Documentos – Status__

Preencher com:

__C__, __\(Cancelada\)__ quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

__E__, __\(Regime Especial\) __quando NF emitida em Regime Especial \(Campo 232 da SAFX07 = ‘S’\) 

__A__  __\(Anulada\) __não será tratada\.

__S__, __\(Substituta\) __verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “675”\.

__D__, __\(Descontado pela Prefeitura\)__ verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “676”\.

__T__,__ \(Não Tributável\) __quando:

Para notas emitidas:

Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “09”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “444”\.

Para notas recebidas:

Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “444”\.

__R__, __\(Retida\)__ quando:

Para notas emitida:

É necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Para notas recebidas:

É necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

__I__,  __\(Isenta\)__ quando:

Para notas emitidas:

Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

Para notas recebidas:

Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__N,  \(Normal\)__ quando nenhuma das situações acima forem verdadeiras\.

Obrigatório 

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS35958__

__MFS66260__

__RN28\.A__

__Regra p/ o campo Documentos – Status__

Preencher com:

__1 – \(Extravio__\) quando o campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL = ‘E’

__2 – \(Cancelamento\)__ quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

__8 – \(Regime Especial\) __quando NF emitida em Regime Especial \(Campo 232 da SAFX07 = ‘S’\) 

__4 – \(Anulada\) __não será tratada\.

__3 – \(Substituição\) __verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “675”\.

__9 – \(Descontado pela Prefeitura\)__ verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “676”\.

__7 \- \(Não Tributável\) __quando:

Para notas emitidas:

Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “09”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “444”\.

Para notas recebidas:

Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “444”\.

__6 – \(Retida\)__ quando:

Para notas emitida:

É necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Para notas recebidas:

É necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

__5 – \(Isenta\)__ quando:

Para notas emitidas:

Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

Para notas recebidas:

Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__0 – \(Normal\)__ quando nenhuma das situações acima forem verdadeiras\.

Obrigatório 

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS66260__

__RN29__

__\[Excluída MFS\-80634\] Regra p/ o campo Documentos – Valor __

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. Valor com duas casas decimais\.

Formato: 99999999999 

Tamanho: 15 posições \(2 decimais\) 

Tipo: Numérico Decimal

__MFS35958__

__MFS\-80634__

__RN29\.a__

__\[ALTERAÇÃO\-__ __MFS80634\] Tornar a regra genérica e não por município__

__Regra p/ o campo Documentos – Valor  \- Específico para o município de Rio Verde __

__\[ALTERAÇÃO\-__ __MFS75582\]__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. Valor com duas casas decimais, utilizar separador com ‘\.’ \(0\.00\)

Formato: 99999999999 

Tamanho: 15 posições \(2 decimais\) 

Tipo: Numérico Decimal

Obs\.: Valor do documento com duas casas decimais sem separadores de milhar e decimal\. Apenas de centavos utilizando “\.”\.

__MFS75582__

__MFS\-80634__

__RN30__

__Regra p/ o campo Documentos – Localização__

Preencher com:

D, \(Dentro do município\) quando o campo MUNICIPIO da TABELA X04\_PESSOA\_FIS\_JUR estiver preenchido com o município em questão

F, \(Fora do município\) quando o campo MUNICIPIO da TABELA X04\_PESSOA\_FIS\_JUR não estiver preenchido com o município em questão

E, \(Estrangeiro\) quando o campo UF da TABELA X04\_PESSOA\_FIS\_JUR for igual a ‘EX’\.

Campo Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS35958__

__MFS66260__

__RN30\.A__

__Regra p/ o campo Documentos – Localização__

Preencher com:

__1, \(No Município\)__ quando o campo MUNICIPIO da TABELA X04\_PESSOA\_FIS\_JUR estiver preenchido com o município em questão ou se o município de destino da capa da nota for igual ao município do estabelecimento\.

__2, \(Fora do Município\)__ quando o campo MUNICIPIO da TABELA X04\_PESSOA\_FIS\_JUR não estiver preenchido com o município em questão

Campo Obrigatório

Formato: X

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS66260__

__MFS706036__

__RN31__

__Regra p/ o campo Documentos – Cidade__

Se campo Declaração – Codificação de Cidades = ’1’ 

     Preencher com o código da UF \+ o código do município da tabela MUNICIPIO referente ao município cadastrado na pessoa fis/jur\.

O código deve ser composto por 7 caracteres e caso o código do município tenha menos do que 5 caracteres, deve ser completado com zeros à esquerda, conforme exemplo:   

UF \+ Município = 42 \+ 4202 = 4204202

Se campo Documentos – Localização for = "E" 

     Preencher com nulo\.

Campo Obrigatório

Formato: 9999999

Tamanho: 7 posições 

Tipo: Numérico 

__MFS35958__

__MFS66260__

__RN32__

__Regra p/ o campo Documentos – OptanteSimples__

Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = marcado, preencher com ‘S’,

Senão preencher com ‘N’\.

Formato: X 

Tamanho: 1 posição 

Tipo: Alfanumérico

__MFS35958__

__MFS66260__

__RN32\.A__

__Regra p/ o campo Documentos – OptanteSimples__

Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = marcado, preencher com __‘0’,__

Senão preencher com __‘1’\.__

Formato: X 

Tamanho: 1 posição 

Tipo: Alfanumérico

__MFS66260__

__RN33__

__Regra p/ o campo Documentos – MotivoCancelamento__

Preencher com branco\.__ __

Formato: XXXXXX 

Tamanho: 512 posições

Tipo: Alfanumérico

__MFS35958__

__RN34__

__Regra p/ o campo Serviços – Identificador __

Preencher com “3”

Formato: X 

Tamanho: 1 posição 

Tipo: Alfanumérico

__MFS35958__

__RN35__

__Excluída MFS\-80634\] Regra p/ o campo Serviços – CNAE/SERVICO __

Quando o campo “Tipo de Serviço” da tela de geração do meio magnético estiver selecionado com a opção “Cod\. de Serviço Lei 116/2003”:

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota\. Formato “00\.00”\. Completar com brancos à direita até completar as 7 posições\.

Quando o campo “Tipo de Serviço” da tela de geração do meio magnético estiver selecionado com a opção “Cod\. de Atividade CNAE”:

     Para notas emitidas:

     Preencher com o campo COD\_ATIVIDADE da tabela ESTABELECIMENTO referente ao Código da Atividade Econômica\. Formato “__0000000__”\. Completar com zeros à direita até completar os 7 caracteres quando necessário

     Para notas recebidas:

    Preencher com o campo COD\_ATIVIDADE da tabela X04\_PESSOA\_FIS\_JUR referente ao Código da Atividade Econômica\. Formato “__0000000__”\. Completar com zeros à direita até completar os 7 caracteres quando necessário\.

Quando o campo COD\_ATIVIDADE estiver vazio, deverá gravar __“0000000”__ e exibir a seguinte mensagem no Log: “Favor preencher o Código de Atividade no cadastro de Pessoa Física/Jurídica\.”

Obrigatório

Formato: XXXXXXX

Tamanho: 7 posições 

Tipo: Alfanumérico

__MFS35958__

__MFS\-80634__

__RN35\.a__

__ALTERAÇÃO\-__ __MFS80634\] Tornar a regra genérica e não por município __

__Regra p/ o campo Serviços – CNAE/SERVICO – Específico para o Município de Rio Verde__

__\[MFS77454\] __Tratamento para alterar o critério de preenchimento acrescentando zeros a esquerda e sem ponto \(7 posições\)

Quando o campo “Tipo de Serviço” da tela de geração do meio magnético estiver selecionado com a opção “Cod\. de Serviço Lei 116/2003”:

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota\. Formato “0000000”\. Completar com zeros a esquerda até completar as 7 posições\.

Quando o campo “Tipo de Serviço” da tela de geração do meio magnético estiver selecionado com a opção “Cod\. de Atividade CNAE”:

     Para notas emitidas:

     Preencher com o campo COD\_ATIVIDADE da tabela ESTABELECIMENTO referente ao Código da Atividade Econômica\. Formato “__0000000__”\. Completar com zeros a esquerda até completar as 7 posições quando necessário

     Para notas recebidas:

    Preencher com o campo COD\_ATIVIDADE da tabela X04\_PESSOA\_FIS\_JUR referente ao Código da Atividade Econômica\. Formato “__0000000__”\. Completar com zeros a esquerda até completar as 7 posições quando necessário\.

Quando o campo COD\_ATIVIDADE estiver vazio, deverá gravar __“0000000”__ e exibir a seguinte mensagem no Log: “Favor preencher o Código de Atividade no cadastro de Pessoa Física/Jurídica\.”

Obrigatório

Formato: 0000000

Tamanho: 7 posições 

Tipo: Alfanumérico

__Atenção: Esta regra não está totalmente de acordo com o manual\. Não estamos considerando na formatação o ‘\.’, pois, o cliente fez um teste no validador, sem utilizar no código do serviço o ponto e o arquivo foi validado sem erro\. Esta definição foi alinhada com a PO e o time\.__

__![](data:image/png;base64,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)__

__MFS77454__

__MFS80634__

__RN36__

__\[Excluída MFS\-80634\] Regra p/ o campo Serviços – Valor__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__ __

Obrigatório

Formato: 99999999999 

Tamanho: 15 posições \(2 decimais\) 

Tipo: Numérico Decimal 

__MFS35958__

__MFS\-80634__

__RN36__

__\[ALTERAÇÃO\-__ __MFS80634\] Tornar a regra genérica e não por município__

__Regra p/ o campo Serviços – Valor \- Específico para o município de Rio Verde __

__\[ALTERAÇÃO\-__ __MFS75582\]__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. Valor com duas casas decimais, utilizar separador com ‘\.’ \(0\.00\)

Formato: 99999999999 

Tamanho: 15 posições \(2 decimais\) 

Tipo: Numérico Decimal

Obs\.: Valor do Serviço com duas casas decimais sem separadores de milhar e decimal\. Apenas de centavos utilizando “\.”\.

__MFS75582__

__MFS\-80634__

__RN36\.a__

__Regra p/ o campo Serviços – Valor \- Específico para o município de Rio Verde __

__\[ALTERAÇÃO\- MFS86515\]__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__ __

Obrigatório

Formato: 99999999999 

Tamanho: 15 posições \(2 decimais\) 

Tipo: Numérico Decimal 

Obs\.: Valor do Serviço não deve utilizar separador de decimal, \(não é aceito pelo validador\)\.

__Atenção: __Esta regra não está totalmente de acordo com o manual\. O cliente fez um teste no validador, sem utilizar o separador \(“\.”\) da casa decimal e o arquivo foi validado sem erro\. 

![](data:image/png;base64,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)

__MFS86515__

__RN37__

__Regra p/ o campo Serviços – Cidade__

Se campo Declaração – Codificação de Cidades = ’1’ preencher com código do município da tabela MUNICIPIO referente ao município informado no campo MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Se campo Declaração – Codificação de Cidades = ’2’ preencher com código do município Siafi da tabela MUNICIPIO\_SIAFI referente ao município informado no campo MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

__ __

Formato: 9999999

Tamanho: 7 posições 

Tipo: Numérico 

__MFS35958__

__RN38__

__Regra p/ o campo Serviços – Alíquota__

Preencher com o campo VLR\_ALIQ\_ISS da tabela DWT\_ITENS\_SERV\.

Valor com duas casas decimais, com separadores de decimal \(ponto “\.”\) 

__ __

Formato: 9\.99 

Tamanho: 4 posições \(2 decimais\) 

Tipo: Numérico Decimal 

__MFS35958__

__RN39__

__Regra p/ o campo Serviços – MotivoAltAliquota__

Preencher com brancos\.

__ __

Formato: XXXXXXXXXX 

Tamanho: 20 posições 

Tipo: Alfanumérico

__MFS35958__

__RN40__

__Regra p/ o campo Serviços Bancários – Identificador __

Preencher com “4”

Formato: X 

Tamanho: 1 posição 

Tipo: Alfanumérico

__RN41__

__Regra p/ o campo Serviços Bancários – Banco__

Preencher com o campo Código da Instituição Financeira do cadastro de Estabelecimento\.

Obrigatório

Formato: 999999999

Tamanho: 9 posições 

Tipo: Numérico

__MFS35958__

__RN42__

__Regra p/ o campo Serviços Bancários – NrConta__

Levar Conta Referencial COSIF da Tela de parametrização Plano de Contas x Códigos de Serviços  

Obrigatório

Formato: XXXXXXXXXX 

Tamanho: 20 posições 

Tipo: Alfanumérico

Obs\.: Caso a quantidade de caracteres for inferior à 20, completar com ‘0\(zero\)’ a esquerda\.

__MFS35958__

__RN43__

__Regra p/ o campo Serviços Bancários – Valor__

Para a conta selecionada:

Caso o campo ident\_custo da tabela x2101\_contas\_ref\_ccusto esteja preenchido: preencher com campo vlr\_tot\_cre – vlr\_tot\_deb da tabela x80\_saldos\_ccusto

Caso o campo ident\_custo da tabela x2101\_contas\_ref\_ccusto não esteja preenchido: preencher com campo vlr\_tot\_cre – vlr\_tot\_deb da tabela x02\_saldos

Obrigatório

Formato: 99999999999 

Tamanho: 15 posições \(2 decimais\) 

Tipo: Numérico Decimal 

__MFS35958__

__RN44__

__Regra p/ o campo Serviços Bancários – Recolhimento__

Preencher com o campo Recolhe Imposto da Tela de parametrização Plano de Contas x Códigos de Serviços\.

Deverá utilizar __0 – Para recolhimento do imposto __e__ 1 – Para não recolhimento do imposto__\.

Obrigatório

Formato: X 

Tamanho: 1 posição 

Tipo: Alfanumérico

__MFS35958__

__MFS66260__

__RN45__

__Regra p/ recuperar informações de declaração de materiais__

Para que esse registro seja gerado a nota fiscal recebida deverá ter pelo menos um serviço de construção civil \(IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\)\.

Quando a nota for de construção civil, a geração deve verificar se existe material para essa nota no menu Manutenção – Materiais

__MFS35958__

__RN46__

__Regra p/ o campo Materiais – Identificador  __

Preencher com “5”

Formato: X 

Tamanho: 1 posição 

Tipo: Alfanumérico

__RN47__

__Regra p/ o campo Materiais –__ __Material__

Preencher com o campo “Cod\. Material”, da aba Materiais da tela de Manutenção de Materiais\.

Obrigatório

Formato: 99999999

Tamanho: 7 posições 

Tipo: Numérico

__MFS35958__

__RN48__

__Regra p/ o campo Materiais – Descrição __

Preencher com o campo “Descrição”, da aba Materiais da tela de Manutenção de Materiais\.

Obrigatório

Formato: XXXXXXXXXX 

Tamanho: 50 posições 

Tipo: Alfanumérico

__MFS35958__

__RN49__

__Regra p/ o campo Materiais – Valor __

Preencher com o campo “Valor do Material”, da aba Materiais da tela de Manutenção de Materiais\.

Obrigatório

Formato: 99999999999 

Tamanho: 15 posições \(2 decimais\) 

Tipo: Numérico Decimal

__MFS35958__

__RN50__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo: __“Formosa”__ deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados, assim como serviços bancários\.”*\.*

__MFS80634__

__RN51__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“GO”__ e ao código de município do IBGE igual a: __“8004” \(Formosa\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

__Exemplo:__ “Este estabelecimento não pertence ao município de __Formosa\.__ Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS80634__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

