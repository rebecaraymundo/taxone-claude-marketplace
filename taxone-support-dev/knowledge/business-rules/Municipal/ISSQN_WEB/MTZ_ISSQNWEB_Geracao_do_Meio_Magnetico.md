# MTZ_ISSQNWEB_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_ISSQNWEB_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-01-30
- **Tamanho:** 90 KB

---

		THOMSON REUTERS

	

Municipal 

 Serviços Tomados 

	Geração do Meio Magnético – ISSQN WEB

##### 	DOCUMENTO DE REQUISITO	

__MFS/CH__

__Nome__

__Descrição__

MFS11786

João Henrique de Araujo\.

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador ISSQN WEB\.

MFS

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MSF/CH__

__RN01__

__Regra para inclusão do novo módulo no Manager:__

O módulo “Valinhos” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “Consiste na entrega das informações sobre os serviços tomados do município de Valinhos\-SP”\.__

__MFS11786__

__RN02__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “56206” \(Valinhos\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Valinhos, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS11786__

__RN03__

__Estrutura de menus do módulo:__

- Arquivo
- Obrigações
	- __Geração do Meio Magnético __
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda

__MFS11786__

__RN04__

__Regra de nomenclatura do arquivo:__

O arquivo pode ser gerado com qualquer nome, a critério do contribuinte, então colocaremos a nomenclatura padrão\.

__       ISSQNWEB\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __ISSQNWEB__: representa a obrigação que está sendo gerada\. 

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração

       __\.TXT__: extensão do arquivo\.

*Exemplo:* ISSQNWEB\_VALINHOS\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__       ISSQNWEB\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.TXT__, onde:

__        ISSQNWEB__: representa a obrigação que está sendo gerada\.    

__        MUNICIPIO__: representa o município que está sendo gerado\.   

        __DDMMAAAA__: representa a data inicial da geração\.   

__        MMAAAA:__ mês da competência referente à nota gerada

        __\.TXT__: extensão do arquivo\.

Ex: ISSQNWEB\_VALINHOS\_01012014\_122013\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* __Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

__MFS11786__

__RN05__

__Regra dos campos da Tela Obrigações – Geração Meio Magnético:__

__Menu:__  Obrigações >> Geração do Meio Magnético:

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\.

__Data Final: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\. 

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.                                  

__Quebrar arquivo por Data de Emissão:__ Deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de Gaspar, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS11786__

__RN06__

__Regra para abas existentes na geração do meio magnético:__

Após processar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. 

A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__MFS11786__

__RN07__

__Regras para geração do Meio Magnético:__

__Regras referentes à formatação dos registros gerados no meio magnético:__

A seguir formatações de dados que devem ser seguidas para geração do meio magnético na estrutura do arquivo:

- O arquivo a ser gerado para importação dever ser no formato __‘TXT’__\.
- A primeira linha do arquivo é uma linha de __‘CABEÇALHO’__
- A última linha do arquivo é uma linha de __‘RODAPÉ’__
- __Campo Caracter:__ Devem ser alinhados a esquerda\. Preencher com espaços em branco à direita, caso seja necessário\. 
- __Campo Numérico:__ Devem ser alinhados a direita\. Preencher com zeros à esquerda caso seja necessário\. 
- __Campo Decimal:__ Devem ser alinhados a direita\. Precedidos por zeros e ‘n’ casas decimais\.

__MFS11786__

__RN08__

__Regra p/ Recuperação das notas fiscais de Serviços Tomados \(só geraremos serviços tomados no arquivo\)\.__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\);
- Classificação da nota fiscal = 2, 3 ou 9 e COD\_DOCTO = 'RPA'
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Não será considerado documento sem item;

__MFS11786__

__RN09__

1. __Linha de Cabeçalho__

__Regra para o campo Tipo Registro__

Esse campo deverá ser preenchido com o valor fixo __‘1’__

Campo obrigatório\.

Formato: 9 

Tamanho: 1 posição

Tipo: Numérico

__MFS11786__

__RN10__

__Regra para o campo Versão__

Esse campo deverá ser preenchido com o valor fixo __‘001’ – __Trata\-se da versão do layout de importação

Campo obrigatório\.

Formato: 999 

Tamanho: 3 posições

Tipo: Numérico

__MFS11786__

__RN11__

__Regra para o campo CCM__

Esse campo deverá ser preenchido com a inscrição municipal do contribuinte\. Preencher com a informação do campo INSC\_MUNICIPAL da tabela de__ ESTABELECIMENTO\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 14 posições, então para atender a obrigação deverão ser consideradas as 8 primeiras posições do campo conforme layout exigido pela prefeitura\. Exemplo: 12345678912345 gravar 12345678\.
- Se o campo CCM não estiver preenchido, emitir uma mensagem padrão no log de campo obrigatório\.

Campo obrigatório\.

Formato: 99999999 

Tamanho: 8 posições

Tipo: Numérico

__MFS11786__

__RN12__

__Regra para o campo Data Inicial__

Esse campo será preenchido com a Data Inicial da tela de geração do meio magnético\.

Formato: aaaammdd

Tamanho: 8 posições

Tipo: Data

__MFS11786__

__RN13__

__Regra para o campo Data Final__

Esse campo será preenchido com a Data Final da tela de geração do meio magnético\.

Formato: aaaammdd

Tamanho: 8 posições

Tipo: Data

__MFS11786__

__RN14__

__Regra para o campo Fim da Linha__

Esse campo representa o fim da linha \(Chr\(13\) \+ Chr\(10\)\) – Fim da linha e Retorno para uma nova linha\.

__MFS11786__

__RN15__

1. __Registro de Escrituração de Serviço Tomado__

__Regra para o campo Tipo Registro__

Esse campo deverá ser preenchido com o valor fixo __‘A’__

Campo obrigatório\.

Formato: X 

Tamanho: 1 posição

Tipo: Alfanumérico 

__MFS11786__

__RN16__

__Regra para o campo Data da Emissão:__

Referente à data de emissão do documento fiscal\. Preencher com a informação do campo __DATA\_EMISSAO__ da tabela __DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)__

__Tratamento: __exemplo 20170626

Campo obrigatório\.

Formato: aaaammdd

Tamanho: 8 posições

Tipo: Data

__MFS11786__

__RN17__

__Regra para o campo Número:__

Referente ao número do documento fiscal\. Preencher com a informação do campo __NUM\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL__ __\(campo 08 da SAFX07\)__

Campo obrigatório\.

Formato: 9999999999 

Tamanho: 10 posições

Tipo: Numérico

__MFS11786__

__RN18__

__Regra para o campo Série:__

Referente à série do documento fiscal\. Preencher com a informação do campo __SERIE\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)__

Campo obrigatório\.

Formato: XXXXX 

Tamanho: 5 posições

Tipo: Alfanumérico

__MFS11786__

__RN19__

__Regra para o campo Tipo Pessoa Prestador:__

Código que identifica o tipo de pessoa do prestador do serviço\.

Preencher com:

__J: Pessoa Jurídica__

- Se na X04\_PESSOA\_FIS\_JUR o campo CPF\_CGC possuir 14 posições = ‘CNPJ’ E o campo COD\_CLASS\_DOC\_FIS for igual = ‘2’ e ‘3’ da SAFX07\.

__F: Pessoa Física não inscrita no município__

- Se na X04\_PESSOA\_FIS\_JUR o campo CPF\_CGC possuir 11 posições = ‘CPF’ E o campo COD\_CLASS\_DOC\_FIS '9' e COD\_DOCTO = 'RPA' da SAFX07\.

__I: Pessoa Física inscrita no município__

- Se na X04\_PESSOA\_FIS\_JUR o campo CPF\_CGC possuir 11 posições = ‘CPF’ E o campo COD\_CLASS\_DOC\_FIS for igual = ‘2’ e ‘3’ da SAFX07\.

__E: Prestador no Exterior__

- Se o campo UF for = ‘EX’ da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: X 

Tamanho: 1 posição

Tipo: Alfanumérico

__MFS11786__

__RN20__

__Regra para o campo CNPJ/CPF do Prestador:__

Identifica o CNPJ ou o CPF do Prestador do serviço sem formatação\. Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR __\(campo 06 da SAFX04\)__ referente ao prestador vinculado a nota fiscal\.

__Tratamento:__

- Se na X04\_PESSOA\_FIS\_JUR o campo CPF\_CGC possuir 11 posições = ‘CPF’, preencher com 3 zeros antes do número do CPF\.
- Se o campo UF for = ‘EX’ da tabela X04\_PESSOA\_FIS\_JUR preencher com zeros até o tamanho exigido pelo layout de 14 posições\.

Formato: 99999999999999

Tamanho: 11 a 14 posições

Tipo: Numérico

__MFS11786__

__RN21__

__Regra para o campo Item da Lista:__

Identifica o Código de Atividade do Serviço associado ao serviço tomado\. Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. Completar com brancos a direita\.

*Exemplo: *Lei 116 “0101” deverá ser preenchida como “01\.01 ”

__Tratamento:__

- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018 deverá ser emitida a mensagem de log: “Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.

Campo obrigatório

Formato: 999999

Tamanho: 6 posições

Tipo: Numérico

__MFS11786__

__RN22__

__Regra para o campo Valor Bruto dos Serviços:__

Identifica o valor total dos serviços constantes no documento fiscal\. Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV__ \(Campo 15 da SAFX09\)__\. 

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘345678912345645’ \(sem vírgula\)\.

- O campo Valor Bruto dos Serviços está com tamanho acima do máximo permitido \(15 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.

Campo Obrigatório

Formato: 999999999999999 

Tamanho: 15 posições 

Tipo: Numérico

__MFS11786__

__RN23__

__Regra para o campo Base de Cálculo:__

Esse campo será preenchido com a base de cálculo do documento fiscal, correspondente ao valor bruto dos serviços menos as deduções\.

Preencher com o campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘345678912345645’ \(sem vírgula\)\.

- O campo Base de Cálculo está com tamanho acima do máximo permitido \(15 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.

Campo Obrigatório

Formato: 999999999999999 

Tamanho: 15 posições 

Tipo: Numérico

__MFS11786__

__RN24__

__Regra para o campo Alíquota ISSQN__

Esse campo será preenchido com a alíquota para o serviço tomado\. Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV __\(campo 32 da SAFX09\)__\.

__Tratamento:__ 

- De acordo com o layout, o campo exige 4 posições, o preenchimento deverá ser realizado da seguinte forma, *exemplos:* para alíquota de 2,40% informe 0240, 5,00% informe 0500 e 10,00% informe: 1000
- Se o campo alíquota não estiver preenchido, o sistema deverá exibir uma mensagem padrão no log alertando o usuário: “O campo Alíquota não foi preenchido\. Campo de preenchimento obrigatório, favor verificar”\.

Campo Obrigatório

Formato: 9999

Tamanho: 4 Posições

Tipo: Numérico

__MFS11786__

__RN25__

__Regra para o campo ISSQN__

Esse campo será preenchido com o valor do ISSQN retido a ser recolhido pelo contribuinte\. Preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘345678912345645’ \(sem vírgula\)\.

- O campo ISSQN está com tamanho acima do máximo permitido \(15 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar\.

Campo Obrigatório

Formato: 999999999999999 

Tamanho: 15 posições 

Tipo: Numérico

__MFS11786__

__RN26__

__Regra para o campo ISSQN Retido__

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

Preencher com __‘S’__:

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com __“N”\.__

Campo Obrigatório

Formato: X

Tamanho: 1 Posição

Tipo: Alfanumérico

__MFS11786__

__RN27__

__Regra para o campo Prestador no Município:__

Preencher com __‘S’__

Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __IGUAL__ o município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

Senão preencher com __‘N’__

Se o prestador for estrangeiro \(UF for = ‘EX’ da tabela X04\_PESSOA\_FIS\_JUR\) utilizar o sinal “__\-__“\.

Campo Obrigatório

Formato: X

Tamanho: 1 Posição

Tipo: Alfanumérico

__MFS11786__

__RN28__

__Regra para o campo Serviço prestado no Município:__

Preencher com __‘S’ __– Sim, se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

Senão preencher com __‘N’ __– Não\.

Campo Obrigatório

Formato: X

Tamanho: 1 Posição

Tipo: Alfanumérico

__MFS11786__

__RN29__

__Regra para o campo Código de isenção de recolhimento de ISSQN:__

Esse campo indica o código de isenção do recolhimento do ISS, utilizar:

__1: prestador com ISSQN Fixo:__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495”\.

__3:__ __prestador com ISSQN estimado__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “08” OU Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

__4: prestador com Imunidade/Isenção__

- Se campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07” ou “10” OU Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” ou “433”\.

__7: serviço no exterior \(sem resultados no território nacional\)__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota, estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520”\.

Caso nenhuma das opções acima seja verdadeira, preencha com:

__0: sem isenção__

Campo Obrigatório

Formato: 9 

Tamanho: 1 Posição 

Tipo: Numérico

__MFS11786__

__RN30__

__Regra para o campo Código de tomador com regime especial:__

Preencher esse campo com as seguintes opções:

__1:__ __empresa da administração pública direta/indireta__

- Se na tabela de ESTABELECIMENTO o campo ISS estiver com a opção __“12” – Empresa da adm\. pública direta/indireta\.__

__2 Instituição financeira__

- Se na tabela de ESTABELECIMENTO o campo ISS estiver com a opção __“13” – Instituição financeira\.__

__3:__ __Inscrito no PRODEVAL__

- Se na tabela de ESTABELECIMENTO o campo ISS estiver com a opção __“14” – Inscrito no PRODEVAL\.__

Caso nenhuma das opções acima seja verdadeira, preencha com:

__0: sem regime especial__

Campo obrigatório

Formato: 9 

Tamanho: 1 Posição 

Tipo: Numérico

__MFS11786__

__RN31__

__Regra para o campo Código de prestador com regime especial:__

Preencher esse campo com as seguintes opções:

__1:__ __prestador empresa da administração pública direta/indireta__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = __“12” – Pode emitir notas totalizadoras__

__3:__ __sem regime especial__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = __“13” – Inscrito no PRODEVAL__

Caso nenhuma das opções acima seja verdadeira, preencha com:

__0: sem regime especial__

Campo obrigatório

Formato: 9 

Tamanho: 1 Posição 

Tipo: Numérico

__MFS11786__

__RN32__

__Regra para o campo Prestador enquadrado no Simples Nacional:__

Este campo indica se o prestador é optante pelo programa Simples Nacional\.

Preencher com:

__“S” \- Sim\.__

Verificar se o campo IND\_SIMPLES\_NAC __\(campo 43 da tabela SAFX04\)__ é igual a “S”\.

Senão, preencher com:

__“N” \- Não__

Formato: X

Tamanho: 1 Posição

Tipo: Alfanumérico

__MFS11786__

__RN33__

__Regra para o campo Fim da Linha__

Esse campo representa o fim da linha \(Chr\(13\) \+ Chr\(10\)\) – Fim da linha e Retorno para uma nova linha\.

Obrigatório

__MFS11786__

__RN34__

1. __Linha de Rodapé__

__Regra para o campo Tipo Registro__

Esse campo deverá ser preenchido com o valor fixo __‘9’__

Campo obrigatório\.

Formato: 9 

Tamanho: 1 posição

Tipo: Numérico

__MFS11786__

__RN35__

__Regra para o campo Número de Registros __

Esse campo deverá exibir o total de registos do arquivo sem considerar a linha de cabeçalho e rodapé\.

Campo obrigatório\.

Formato: 9999999 

Tamanho: 7 posições

Tipo: Numérico

__MFS11786__

__RN36__

__Regra para o campo Fim da Linha__

Esse campo representa o fim da linha \(Chr\(13\) \+ Chr\(10\)\) – Fim da linha e Retorno para uma nova linha\.

Obrigatório\.

__MFS11786__

