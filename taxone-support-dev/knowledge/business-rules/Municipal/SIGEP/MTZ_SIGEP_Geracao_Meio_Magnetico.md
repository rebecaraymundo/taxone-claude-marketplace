# MTZ_SIGEP_Geracao_Meio_Magnetico

- **Fonte:** MTZ_SIGEP_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-11-05
- **Tamanho:** 93 KB

---

THOMSON REUTERS

Municipal 

 Serviços Tomados 

### 	Geração do Meio Magnético – SIGEP	

### 	DOCUMENTO DE REQUISITO

### Controle das Alterações

__MFS/CH__

__Nome__

__Descrição__

MFS\-521650

Elisabete Costa

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo criar a geração do meio magnético de serviços tomados em atendimento ao novo validador __“SIGEP – Sistema Integrado de Gestão Pública”__

MFS\-571540

Rosemeire Santos

Este documento tem como objetivo ajustar os preenchimentos dos campos Valor Retenção ISS e Alíquota \(__BUG\-571540\)__

MFS\-612487

Rosemeire Santos

Este documento tem como objetivo incluir o município de Nerópolis/GO na geração do meio magnético de serviços tomados do validador __“SIGEP – Sistema Integrado de Gestão Pública”__

MFS\-629017

Denilson André Santos

Alteração da regra RN20, para que seja considerado na geração do meio magnético, o valor de ISS retido, uma vez que o indicador de retenção, estiver preenchido com a opção 1 \(Tomador\)

MFS\-871837

Rosemeire Santos

Incluir Arquivo de Entradas de Serviços \(Const\. Civil/Utilities /Telecom\) regra RN20, para que seja considerado na geração do meio magnético, o valor de ISS retido, uma vez que o indicador de retenção, estiver preenchido com a opção 1 \(Tomador\)

MFS\-829438

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

### REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS/CH__

__RN01__

__Estrutura de menus do módulo __

Deverão ser criados os seguintes menus e sub\-menus no módulo SIGEP:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/Utilities /Telecom\)__
- Janela
- Ajuda 

__MFS\-521650__

__RN02__

__Regra de criação do nome do arquivo:__

__\- SERVIÇOS TOMADOS__

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__       SIGEP\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __SIGEP__: representa a obrigação que está sendo gerada\. 

       __\.txt__: extensão do arquivo\.

*Exemplo:* __SEGIP__\___BOTUCATU__\___01012023__\.TXT

__\- QUEBRAR ARQUIVOS POR DATA DE EMISSÃO__

Quando o parâmetro __“Quebrar Arquivos por Data de Emissão”__ estiver marcado, deve ser realizada a seguinte verificação: 

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

__SIGEP\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __SIGEP__: representa a obrigação que está sendo gerada\. 

       __\.txt__: extensão do arquivo\.

       __MMAAAA__: mês da competência referente à nota gerada

*Exemplo:* __SIGEP__\___BOTUCATU__\___01012023__\___122022__\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__MFS\-521650__

__MFS\-829438     __

__RN03__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

*Observação:* Cada campo deverá exibir a mensagem padrão caso de não preenchimento\.

__MFS\-521650__

__RN04__

__Regra p/ Geração do Arquivo Magnético__

- Formato do arquivo será em TXT\. Neste formato, os campos são separados por “;” \(ponto e vírgula\)\.
- Todos os campos do tipo \(Data\) têm o formado no padrão DDMMAAAA\.
- Todos os campos do tipo \(Alfanumérico\) são preenchidos com espaços em branco à direita quando não alcançar o tamanho exato do campo\.
- Todos os campos do tipo \(Numérico\) são preenchidos com zeros à esquerda quando não alcançar o tamanho exato do campo\.
- Todos os campos do tipo \(Texto\) são preenchidos com espaços à esquerda quando não alcançar o tamanho exato do campo\.

__*Observação:*__ Para os campos numéricos nenhum separador de milhar e decimal devem ser informados\.

__MFS\-521650__

__RN05__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\):__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2, 3 ou 9 \(RPA\)
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.
- Recuperar apenas notas fiscais com retenção do ISS \(campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV > 0\)
- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

__MFS\-521650__

__RN06__

__Regra p/ o campo – Tipo de Registro 1__

Deverá ser preenchido com o valor 1, indicando a linha do cabeçalho

Preencher com fixo “__1__”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

__MFS\-521650__

__RN07__

__Regra p/ o campo – Tipo do Arquivo__

Deverá ser preenchido com o valor “__REST\_LOTE__”, referenciando o tipo do Arquivo

Preencher com fixo “__REST\_LOTE__”\.

Completar com espaço à esquerda  

Campo obrigatório

Formato: 9

Tipo: Texto

Tamanho: 12

__MFS\-521650__

__RN08__

__Regra p/ o campo – Inscrição Municipal do Tomador__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Inscrição Municipal do Tomador

Campo obrigatório

Formato: 9999999

Tipo: Numérico

Tamanho: 15

__MFS\-521650__

__RN09__

__Regra p/ o campo –  Reservado                                 __

Preencher com brancos\.                                                                                                                                                         

Tamanho: 03

__MFS\-521650__

__RN10__

__Regra p/ o campo – Data do Arquivo__

Data que o arquivo foi gerado

Preencher com SYSDATE\. Preencher no formato AAAAMMDD\.      

Campo obrigatório

                                                                                        

Tamanho: 08

__MFS\-521650__

__RN11__

__Regra p/ o campo – Tipo de Registro 2__

Deverá ser preenchido com o valor 2, indicando a linha do cabeçalho

Preencher com fixo “2”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

__MFS\-521650__

__RN12__

__Regra p/ o campo – Código do Serviço__

Informe o código do serviço, de acordo com Lei 116 de 2003

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

__Tratamento:__

\-	Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: “Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal\.  <<Subsérie>>, <<Data Fiscal>>”;

\-	Se o código de serviço da lei 116 estiver diferente para os serviços cadastrados na NF, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: “Erro: O código da Lei 116 cadastrado no serviço informado na nota fiscal difere com os demais serviços, favor verificar\! <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.

Código de serviço inserir ponto e desconsiderar zeros a esquerda\.

Completar com espaço à esquerda  

Campo obrigatório

Formato: 99\.99 e 9\.99

Tipo: Texto

Tamanho: 7

__MFS\-521650__

__RN13__

__Regra p/ o campo – Tipo de Documento – \(TFIX84\)__

Informar tipo de documento

Preencher com o campo Tipo Docto da tela Parâmetros por Município – Parâmetros – \(TFIX84\) \- Tipo Docto Msaf x Tipo Docto referente ao tipo de documento cadastrado na nota fiscal\.

Quando não houver parametrização para o tipo de documento da nota fiscal, deve\-se exibir a seguinte mensagem: “O tipo de documento não está parametrizado em Parâmetros por Município – Parâmetros – Tipo Docto Msaf x Tipo Docto\. Favor verificar” e o arquivo deve ser gerado\.                                                                                                                                                                                

Preencher com o campo COD\_DOCTO \(Campo 05\) da tabela SAFX07 referente ao tipo de documento\.

Completar com espaço à esquerda  

Campo obrigatório

Formato: 999999

Tipo: Texto

Tamanho: 02

__MFS\-521650__

__RN14__

__Regra p/ o campo – Código da cidade do serviço prestado \(Código IBGE\)__

Código Cidade Prestado \(Código IBGE\)

Preencher com o campo COD\_MUNIC\_OBRIG da tabela PRT\_MUNIC\_OBRIG\_MSAF referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 25 da safx04\)\. O campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR deve ser igual ao campo COD\_MUNIC\_MSAF da tabela PRT\_MUNIC\_OBRIG\_MSAF\.

Formato: 999999

Tipo: Numérico

Tamanho: 07

__MFS\-521650__

__RN15__

__Regra p/ o campo – Data do serviço__

Data prestação serviço

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\)\. Preencher no formato AAAAMMDD\.

Campo obrigatório

Formato: AAAAMMDD

Tipo: Numérico

Tamanho: 08

__MFS\-521650__

__RN16__

__Regra p/ o campo – Número documento__

Referente ao número do documento\.

\- COD\_CLASS\_DOC\_FIS = “2 – Serviços” ou “3 \- Mercadorias e Serviços”

\- IND\_MAT\_SERV da tabela X2018\_SERVICOS = “2 – Serviço “

\- IND\_SERVICO\_TERC da tabela X2018\_SERVICOS = “S \- Tipo de Serviço prestado por terceiros, pessoa física”

Completar com espaço à esquerda  

Campo obrigatório

Formato: 999999

Tipo: Texto

Tamanho: 15

__MFS\-521650__

__RN17__

__Regra p/ o campo – Tributado no Município __

\(0\) para sim | \(1\) para não

Se IND\_TP\_SERVICO <> ‘__1__’ do serviço cadastrado na nota:

Preencher com “1” quando o campo Imposto Retido estiver preenchido com “1” 

Senão, preencher com “__0__”\.

Se IND\_TP\_SERVICO = ‘__1__’ do serviço cadastrado na nota:

Preencher com “1” quando o campo Imposto Retido estiver preenchido com “__1__” – Sim e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL = Botucatu\.

Senão, preencher com “__0__”\.

Campo obrigatório

Formato: 999999

Tipo: Numérico

Tamanho: 08

__MFS\-521650__

__RN18__

__Regra p/ o campo – Valor do Serviço__

Identifica o valor do serviço\.

                                                                                                                                                                             

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV \(campo 14 da safx09\)\.     

Completar com zeros à esquerda                     

Campo não obrigatório

Formato: 999999999\.99

Tipo: Numérico 

Tamanho: 15

__MFS\-521650__

__RN19__

__Regra p/ o campo – Alíquota__

Identifica a Alíquota do Serviço\.

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\) SE não tiver preenchido, preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

                                

 Tratamento:

	Se o campo ultrapassar o tamanho permitido pelo layout, deverá ser truncado considerando o valor da direita para a esquerda e exibir uma mensagem de log padrão\.                                                                                                    

Campo não obrigatório

Formato: 99999

Tipo: Numérico

Tamanho: 03

__MFS\-521650__

__MFS\-571540__

__RN20__

__Regra p/ o campo – Valor Retenção ISS__

Identifica o Valor de Retenção do ISS:

Preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) pelo menos uma das situações abaixo forem verdadeiras:

	Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.

__E__

	Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Senão preencher com zeros \(0,00\)\.

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = “S”, preencher com 0,00 \(zero\)\.

__\[ALTERAÇÃO\-MFS871837\] – Regra específica para Nerópolis__

Se \(DWT\_DOCTO\_FISCAL\-IND\_TP\_RET = 1 ou 2\) e DWT\_DOCTO\_FISCAL\-SITUACAO <> “S” e DWT\_ITENS\_SERV\- VLR\_TRIBUTO\_ISS = 0,00

 Então

        Preecher o campo “Valor Retenção ISS”, com o campo DWT\_ITENS\_SERV\-VLR\_ISS\_RETIDO

Senão 

        Preencher o campo “Valor Retenção ISS” com 0,00 

Campo não obrigatório

Formato: 99999

Tipo: Numérico

Tamanho: 15

__MFS\-521650__

__MFS\-571540__

__MFS\-629017__

__MFS\-871837__

__RN21__

__Regra p/ o campo – CPF / CNPJ Prestador__

Informe o CPF / CNPJ do prestador

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.                                                                                                                                                                                  

Campo não obrigatório

Formato: 99999

Tipo: Numérico

Tamanho: 15

__MFS\-521650__

__RN22__

__Regra p/ o campo – Inscrição Municipal prestador__

Inscrição Municipal Prestador, campo opcional, quando não utilizar enviar espaços em branco\.

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 08 da SAFX04\)                                                                                                                                                      

Campo não obrigatório

Formato: 99999

Tipo: Numérico

Tamanho: 15

__MFS\-521650__

__RN23__

__Regra p/ o campo – Inscrição Estadual prestador__

Inscrição Estadual Prestador, campo opcional, quando não utilizar enviar espaços em branco\.

Preencher com o conteúdo do campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver mais que 11 posições, caso contrário preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 15

__MFS\-521650__

__RN24__

__Regra p/ o campo – Nome / Razão Social prestador__

Identifica o Nome / Razão Social Prestador\.

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 05 da SAFX04\)\.                                                                                                                                           

Completar com espaço à esquerda  

Campo não obrigatório

Formato: 999999999

Tipo: Texto

Tamanho: 100

__MFS\-521650__

__RN25__

__Regra p/ o campo – Endereço prestador__

Identifica o endereço do prestador\.

Identifica o logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 12 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

Completar com espaço à esquerda  

Campo não obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 50

__MFS\-521650__

__RN26__

__Regra p/ o campo – Número prestador __

Identifica o número do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 13 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

Completar com espaço à esquerda  

Campo não obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 10

__MFS\-521650__

__RN27__

__Regra p/ o campo – Complemento Endereço prestador__

Identifica o complemento do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 14 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

Completar com espaço à esquerda  

Campo não obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 30

__MFS\-521650__

__RN28__

__Regra p/ o campo – Bairro Prestador__

Identifica o bairro do prestador do serviço\.

Preencher com o conteúdo do campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Numérico

Tamanho: 30

__MFS\-521650__

__RN29__

__Regra p/ o campo – Código Cidade prestador__

Nesse campo será informado o código da cidade de incidência do imposto conforme a tabela do IBGE\. 

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\)\.

Senão estiver preenchido, preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\)\.

Caso não esteja preenchido será emitida uma mensagem solicitando a verificação “O código IBGE do município do prestador é obrigatório\. Favor verificar”

Campo obrigatório

Formato: XXX\.\.\.

Tipo: Numérico

Tamanho: 7   

     

__MFS\-521650__

__RN30__

__Regra p/ o campo – CEP prestador__

Identifica o estado do logradouro do local de prestação de serviço\.

Preencher com o conteúdo do campo CEP da tabela X04\_PESSOA\_FIS\_JUR \(campo 20 da SAFX04\) referente ao endereço da Pessoa Física/Jurídica cadastrada na nota fiscal\.

Campo não obrigatório

Formato: 99999999

Tipo: Numérico

Tamanho: 08

__MFS\-521650__

__RN31__

__Regra p/ o campo – Email__

Identifica o E\-mail do prestador do serviço\.

Preencher com o conteúdo do campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 100

__MFS\-521650__

__RN32__

__Regra p/ o campo – Descrição de Serviço__

Identifica a descrição do serviço\.

Preencher com o conteúdo do campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na X2018\_SERVICOS e vinculado ao item da nota fiscal\. Não é necessário preencher o restante do campo com espaços em branco\.

__Tratamento:__

\-	Se o campo não estiver preenchido, deixar a TAG vazia e emitir a seguinte mensagem de log: “A TAG Descrição de Servico é obrigatória, favor preencher o serviço da lei 116 no serviço que foi cadastrado no item da nota fiscal\.”

Campo obrigatório

Completar com espaço à esquerda  

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 2000

__MFS\-521650__

__RN33__

__Regra p/ o campo – Tipo de Registro 3__

Deverá ser preenchido com o valor 3, indicando ser Linha do Rodapé\.

Preencher com fixo “3”\.

Completar com zeros à esquerda  

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

__MFS\-521650__

### INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__MFS__

__IM01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

__MFS\-521650__

__IM02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XXXXXX / XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-521650__

__IM03__

Código IBGE: __7506 – __Município/UF:__ BOTUCATU / SP__

A descrição funcional do módulo será: __*“Consiste na entrega das informações sobre os serviços tomados do município de BOTUCATU”\.*__

__MFS\-521650__

__IM04__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Nerópolis/GO deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Nerópolis: *“Consiste na entrega das informações sobre os serviços tomados do município de Nerópolis”\.*

__MFS\-612487__

__IM05__

__Regra p/ abertura do novo módulo no Manager:__

Se o estabelecimento selecionado no Manager não pertencer ao estado de Goiás \(UF = “GO”\) e ao município de Nerópolis \(Cod Município IBGE = 14507\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Nerópolis, Goiás\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo será fechado\.

__MFS\-612487__

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – __Descrição da Regra de Negócio 01\]

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX

