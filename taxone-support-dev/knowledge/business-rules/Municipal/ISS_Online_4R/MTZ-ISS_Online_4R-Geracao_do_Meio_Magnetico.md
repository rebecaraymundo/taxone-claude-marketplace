# MTZ-ISS_Online_4R-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-ISS_Online_4R-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-03-04
- **Tamanho:** 57 KB

---

__ISS Online 4R__

__Geração do Meio Magnético__

__ __

__DOCUMENTO DE REQUISITO__

###### DR

###### Nome

__Descrição__

OS4107\-A

Criação do meio magnético __ISS Online 4R\.__

Este documento tem como objetivo tratar a geração do meio magnético para atendimento aos municípios de São Manuel – SP\.

OS4107

Criação do meio magnético __ISS Online 4R\. __Inclusão de novos municípios\.

Este documento tem como objetivo tratar a geração do meio magnético ISS Online 4R, para atendimento aos novos municípios incluídos: Adamantina, Governador Valadares, Andradina, Itanhaém, Porto Feliz e Itatinga\.

OS4426

DW \- MUNICIPAL \- ISS ONLINE 4R \- SÃO MANUEL \- Alteração para gerar meio magnético pela Data de Emissão\.  

Este documento tem como objetivo incluir o novo parâmetro Quebrar Arquivos por Data de Emissão na tela de geração do meio magnético\.

__OS4458__

DW \- MUNICIPAL \- ISS ONLINE 4R – Inclusão das informações, referente a Construção Civil\. 

Inclusão das informações faltantes referentes a construção civil – Obras\.

OS4600

DW \- MUNICIPAL – ISS Online 4R \- Atendimento a construção civil/telecom/utilities

Incluir ao menu o Atendimento a construção civil/telecom/utilities

MFS3203

Criação do meio magnético ISS Online 4R\.__ __Inclusão de novos municípios\.

Este documento tem como objetivo tratar a geração do meio magnético ISS Online 4R, para atendimento ao novo município __Peruíbe\.__

MFS4265

Criação do meio magnético ISS Online 4R\.__ __Inclusão de novos municípios\.

Este documento tem como objetivo tratar a geração do meio magnético ISS Online 4R, para atendimento ao novo município __Itapetininga\-SP\.__

__MFS\_2071__

DW \- MUNICIPAL – ISS Online 4R – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

__MFS8230__

DW \- MUNICIPAL – ISS Online 4R \- Inclusão de novo município\.

Este documento tem como objetivo tratar a geração do meio magnético ISS Online 4R, para atendimento ao novo município __Tatuí\-SP\.__

__MFS11041__

DW \- MUNICIPAL – ISS Online 4R \- Inclusão de novos municípios\.

Este documento tem como objetivo tratar a geração do meio magnético ISS Online 4R, para atendimento dos novos municípios __Cerquilho\-SP __e__ Boituva\-SP\.__

__MFS\-65255__

Rogério Ohashi

Este documento tem como objetivo alterar a regra de recuperação dos serviços tomados para o município de Tatuí\. \(__RN08__\)\.

__MFS\-589312__

Rosemeire Santos

Este documento tem como objetivo incluir no validador ISS Online 4R o município de Monte Mor/SP, para atendimento da obrigação acessória, conforme determinação legal\. 

__MFS\-839828__

Rosemeire Santos

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-1001145__

Alessandra Navatta

Ajuste na regra do campo Situação\. Inserida uma nova condição para Situação = 0 \(local de prestação do serviço <> COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\) \(RN12\)

__MFS\-1043071__

Rosemeire Santos

Este documento tem como objetivo incluir os municípios de Taquarivai/SP, Buri/SP, Cajati/SP, Cesario Lange/SP, Igarata/SP, Ilha Comprida/SP, Ipero/SP, Iporanga/SP, Itariri/SP, Lucelia/SP, Miracatu/SP, Osvaldo Cruz/SP, Pereiras/SP, Pratania/SP, Ribeirao Branco/SP, Sarapui/SP e Uchoa/SP, no validador ISS Online 4R\.

__MFS\-1059696__

Rosemeire Santos

Este documento tem como objetivo incluir os municípios de Ribeira\-SP e Sagres\-SP, no validador ISS Online 4R\.

__REGRAS DE NEGÓCIO__

####    Cód\.

###   Descrição

### DR

RN01

__Regra p/ inclusão do novo módulo no Manager:__

__São Manuel__

O novo módulo “São Manuel” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de São Manuel”\.

__OS4107\-A__

RN02

__Regra p/ abertura do novo módulo no Manager:__

__São Manuel__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “50100” \(São Manuel\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a SÃO MANUEL/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4107\-A__

RN03

__Estrutura de menus do módulo ISS Online 4R:__

Deverão ser criados os seguintes menus e sub\-menus no módulo ISS Online:

- Arquivo
- Obrigações
	-  Meio Magnético
	- Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\) 
- Janela 
- Ajuda

__OS4107\-A__

OS4600

RN04

__Regra de criação do nome do arquivo:__

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\.TXT__, onde:

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

       __\.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.TXT

__ISSONLINE4R\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\. Deve ser preenchido com o nome do município selecionado no manager\.

__       ISSONLINE4R__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.

__Ex:__ ISSONLINE4R\_SAOMANUEL\_01092013\.txt

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA \_MMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

       __\.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__      ISSONLINE4R\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.txt__, onde:

__       ISSONLINE4R__: representa a obrigação que está sendo gerada\.

__       MUNICIPIO__: representa o município que está sendo gerado\. Deve ser preenchido com o nome do município                  selecionado no manager\.

       __DDMMAAAA__: representa a data inicial da geração

       __MMAAAA__: mês da competência referente a nota gerada

       __\.txt__: extensão do arquivo\.

__Ex:__ ISSONLINE4R\_SAOMANUEL\_01092013\_082013\.txt

Obs: Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__OBS\.:Este novo parâmetro \(Quebrar Arquivos por Data de Emissão\) será válido, apenas para Notas de Serviços Tomados__

__OS4107\-A__

__OS4426__

__MFS\-839828__

RN05

__Regra p/ tela da Geração do Meio Magnético__

__Menu:  __Obrigações > Geração do Meio Magnético

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\. 

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

__Gerar Serviços Prestados__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Serviços Tomados__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. Quando a opção “Gerar Serviços Tomados” não estiver selecionada, deve ser desabilitado\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ neste campo devem ser listados todos os estabelecimentos que deverão ser considerados na geração do arquivo\.

__OS4107\-A__

__OS4426__

__MFS\_2071__

RN06

__Regra p/ preenchimento dos campos do arquivo magnético__

\- Todos os campos deverão ser alinhados a esquerda e preenchidos com espaços em branco, a partir da primeira posição não utilizada no caso de campo tipo texto\. No caso de campo numérico, deverá ser preenchido com zeros a partir da primeira posição não utilizada\.

\- Campos de valores não devem ter ponto e nem vírgula, com duas casas decimais\.

__OS4107\-A__

RN07

__Regra p/ recuperar notas fiscais de serviços prestados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

Quando a nota não tiver itens não deve ser recuperada\.

__OS4107\-A__

__MFS589312__

RN08

__Regra p/ recuperar notas fiscais de serviços tomados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços tomados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

__\[ALTERADA – MFS65255/MFS589312\] \- __Incluir município de Monte Mor/SP e Tatuí na regra abaixo\.

- Não selecionar os documentos fiscais de entrada desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal E o campo código de modelo cadastrado na nota fiscal for igual a “55” OU o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\.

Quando a nota não tiver itens não deve ser recuperada\.

__OS4107\-A__

__MFS65255__

__MFS589312__

RN09

__Tipo do Registro: __Identificação do Registro\.

Preencher com o valor fixo __“C”\.__

__Campo obrigatório\.__

__OS4107\-A__

RN10

__Tipo da Escrituração: __Identificação do tipo de escrituração\.

Para notas de serviços Prestados, preencher com:  

__“1”__ \- Escrituração de Prestador

Para notas de serviços Tomados, preencher com:

__“2”__ \- Escrituração de Tomador

__Campo obrigatório\.__

__OS4107\-A__

RN11

__Data da N\.F\. : __ Data que foi emitida a Nota Fiscal\.

Preencher com a data informada no campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FIS, 

no formato “AAAAMMDD”\.

Ex: 20090127

 

__Campo obrigatório\.__

__OS4107\-A__

RN12

__Situação: __Identificação da situação da nota fiscal

Preencher com:

__“3” – Isenta __

__Para notas Emitidas:__ Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido, verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”;

__Para notas Recebidas:__  Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__“0” – Tributada__

__Para notas Emitidas: __ Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495” ou  local da prestação do serviço <> COD\_MUNIC\_ISS da tabela ESTABELECIMENTO

__Para notas Recebidas:__  Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495” ou  local da prestação do serviço <> COD\_MUNIC\_ISS da tabela ESTABELECIMENTO

__“1” – Cancelada__

Se campo SITUACAO = “S” da SAFX07\.

__“4” – Retida__

__Para notas Emitidas:__ É necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2” e se o local da prestação do serviço = município do módulo selecionado\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido e se o local da prestação do serviço = município do módulo selecionado
- e se o local da prestação do serviço = município do módulo selecionado

__Para notas Recebidas:__  recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__“2” – Anulada__

Não será tratada nesta OS\.

__Campo obrigatório\.__

__OS4107\-A__

__MFS\-1011145__

RN13

__Nº N\.F\. Inicial:__ Número da nota emitida\. 

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Formate com zeros à esquerda\. Ex:"0000000001"

__Campo Não obrigatório__\.

__OS4107\-A__

RN14

__Nº N\.F\. Final:__ Número da nota emitida\.

Se "Tipo da Escrituração" = “2” repetir "Nº N\.F\. Inicial"

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Formate com zeros à esquerda\. Ex:"0000000001"

Se "Tipo da Escrituração" = “1” não informar\. Preencher com zeros\.

 

__Campo Não obrigatório__\.

__OS4107\-A__

RN15

__Série da N\.F\.:  Informe a série da N\.F\.__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Campo obrigatório\. __

__OS4107\-A__

RN16

__Valor do Serviço: __ Informe o valor do Serviço sem formatação com zeros à esquerda\. 

Ex: \(R$100,00\) 000000010000__ __

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__Campo obrigatório\.__

__OS4107\-A__

RN17

__Código da atividade/serviço:__

Informe o código da atividade/serviço, com a máscara\. 

Ex: 10\.01

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

__Campo obrigatório\.__

__OS4107\-A__

RN18

__Tipo de Pessoa: __

Para notas Emitidas, preencher com:

“0” = Física\.  Quando o campo CGC da tabela ESTABELECIMENTO referente a pessoa fis/jur tiver 11 posições\.

“1” = Jurídica\.  Quando o campo CGC da tabela ESTABELECIMENTO referente a pessoa fis/jur tiver 14 posições\.

Para notas Recebidas, preencher com:

“0” = Física\.  Quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur tiver 11 posições\.

“1” = Jurídica\.  Quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur tiver 14 posições\.

__Campo obrigatório\.__

__OS4107\-A__

RN19

__CNPJ/CPF : __

Para notas emitidas

Preencher com o campo CGC da tabela ESTABELECIMENTO\.

Para notas recebidas

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Informe somente números, sem máscara\.

__Campo obrigatório\.__

__OS4107\-A__

RN20

__Nome/Razão Social: __

Para notas Emitidas:

Corresponde ao campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

Para notas Recebidas:

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota

__Campo obrigatório\.__

__OS4107\-A__

RN21

__Cidade :  __

Para notas Emitidas:

Preencher com o campo CIDADE da tabela ESTABELECIMENTO

Para notas Recebidas:

Preencher com o campo CIDADE da tabela SAFX04\.

__Campo obrigatório\.__

__OS4107\-A__

RN22

__Estado :  __

Para notas Emitidas:

Preencher com o campo COD\_ESTADO da tabela ESTABELECIMENTO

Para notas Recebidas: 

Preencher com o campo UF da tabela SAFX04\.

__Campo obrigatório\.__

__OS4107\-A__

RN23

__Endereço:  __

Para notas Emitidas:

Preencher com o campo ENDERECO da tabela ESTABELECIMENTO\.

Para notas Recebidas: 

Preencher com o campo ENDERECO da tabela SAFX04\.

__Campo obrigatório\.__

__OS4107\-A__

RN24

__Número:  __

Para notas Emitidas:

Preencher com o campo NUM\_ENDERECO da tabela ESTABELECIMENTO\.

Para notas Recebidas: 

Preencher com o campo NUM\_ENDERECO da tabela SAFX04\.

__Campo obrigatório\.__

__OS4107\-A__

RN25

__CEP: __Só números referentes ao campo "CEP"  

Para notas Emitidas:

Preencher com o campo CEP da tabela ESTABELECIMENTO\.

Para notas Recebidas: 

Preencher com o campo CEP da tabela SAFX04\.

__Campo obrigatório\.__

__OS4107\-A__

RN26

__Local da Prestação: __

Considerar o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

__Preencher com:__

__“0” – Para Município\. __

Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO, preencher com __“0”__

__“1” \-  Fora do Município__

Se o campo COD\_MUNICIPIO da tabela S DWT\_DOCTO\_FISCAL for diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO, preencher com __“1”\.__

__Campo obrigatório\.__

__OS4107\-A__

RN27

__País: __

__Informe "010"__

__Campo obrigatório\.__

__OS4107\-A__

RN28

__Resultado: __

__Informe branco__

__Campo Não obrigatório\.__

__OS4107\-A__

RN29

__Nome da Empresa Estrangeira: __

__Informe brancos  __

__Campo Não obrigatório\.__

__OS4107\-A__

RN30

__Endereço da Empresa Estrangeira: __

 __Informe brancos  __

__Campo Não obrigatório\.__

__OS4107\-A__

__RN31__

__Localização da Obra__

__Preencher com:__

__“1” – Para Município\. __

Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO, e campo IND\_TP\_SERVICO for = 1 da SAFX2018, preencher com __“1”__

__“2” \- Fora do Município__

Se o campo COD\_MUNICIPIO da tabela S DWT\_DOCTO\_FISCAL for diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO, preencher com __“2”\.__

Caso não for de construção Civil, informar Brancos\.

__Campo Não obrigatório\.__

__OS4107\-A__

__OS4458__

__RN32__

__Cnpj/Cpf Proprietário da Obra: __

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR, que esteja relacionado ao campo Código de Obra da tela de Fornecedores x Obras, disponibilizado através do menu da tela de Cadastro de Pessoa Física/Jurídica\. O Código da Obra deve ser referente ao código informando no campo “Canal Distrib/Obra” da capa da nota fiscal\. 

Caso não for de construção Civil, informar Brancos\.

__Campo Não obrigatório\.__

__OS4107\-A__

__OS4458__

__RN33__

__Nome do Proprietário da Obra:__  

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR, que esteja relacionado ao campo Código de Obra da tela de Fornecedores x Obras, disponibilizado através do menu da tela de Cadastro de Pessoa Física/Jurídica\. O Código da Obra deve ser referente ao código informando no campo “Canal Distrib/Obra” da capa da nota fiscal\. 

Caso não for de construção Civil, informar Brancos\.

__Campo Não obrigatório\.__

__OS4107\-A__

__OS4458__

__RN34__

__Dt\. Início da Obra:__  

Preencher com o campo “Data de Contratação” informada na tela de “Novo Canal de Distribuição Aba”  localizada em,  Básicos > Mastersaf DW, menu__:__  Manutenção > Cadastros > Canais de Distribuição/ Obra\.

Inserir no formato AAAA/MM/DD\. Caso não seja um serviço de construção civil, informar Brancos\.

Caso não for de construção Civil, informar Brancos\.

__Campo Não obrigatório\. __

__OS4107\-A__

__OS4458__

__RN35__

__Nome/Identificação da Obra : __ 

Preencher com a informação do campo “Descrição” da tela de “Novo Canal de Distribuição/Obra”, localizada em,  Básicos > Mastersaf DW, menu__:__  Manutenção > Cadastros > Canais de Distribuição/ Obra\.

Caso não seja um serviço de construção civil, informar Brancos\.

__Campo Não obrigatório \.__

__OS4107\-A__

__OS4458__

__RN36__

__Local da Obra : __ 

Preencher com a informação da tabela Safx37, campo “Endereço” da tela de “Novo Canal de Distribuição/Obra” \(Menu__:__ Manutenção > Cadastros > Canais de Distribuição/ Obra\), localizada em, Básicos > Mastersaf DW, devendo estar relacionado com o número da obra da capa da nota da Safx07\. 

Caso não seja um serviço de construção civil, informar Brancos\.

__Campo Não obrigatório \.__

__OS4107\-A__

__OS4458__

__RN37__

__Número da Obra : __ 

Preencher com a informação da tabela Safx37, campo “Numero”  da tela de “Novo Canal de Distribuição/Obra”, \( Menu__:__ Manutenção > Cadastros > Canais de Distribuição/ Obra\), localizada em,  Básicos > Mastersaf DW, devendo estar relacionado com o número da obra da capa da nota da Safx07\. 

Caso não seja um serviço de construção civil, informar Brancos\.

__Campo Não obrigatório \.__

__OS4107\-A__

__OS4458__

__RN38__

__Alíquota do Simples: __ 

Informe apenas quando for alíquota do Simples Nacional\. 

Formato: "\#\.\#\#" Exemplo: "2\.25"

Preencher com o campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV\.

Preencher quando o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual a “01”\.

Preencher quando o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual a “04”\.

Para o município de “SÃO MANUEL” informar Brancos quando o valor estiver zerado\.

__Campo Não obrigatório\.__

__OS4107\-A__

__MFS\-63475__

__RN39__

__Base de Cáculo : __ 

Informe o valor da Base de Cáculo sem formatação e com zeros à esquerda\. 

Ex:\(R$100,00\) 000000010000__ __

Preencher com o somatório do campo VLR\_BASE\_ISS\_1  da tabela DWT\_ITENS\_SERV\.

__Campo Não obrigatório \.__

__OS4107\-A__

__RN40__

__Deduções :__  

Informe o valor das Deduções sem formatação e com zeros à esquerda\. 

Ex: \(R$100,00\) 000000010000

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV \(campo 59 da SAFX09\)\.

__Campo Não obrigatório \.__

__OS4107\-A__

__RN41__

__Imposto de Renda :__  

Informe o valor do Imposto de Renda sem formatação e com zeros à esquerda\. 

Ex: \(R$100,00\) 000000010000 

Preencher com o campo VLR\_IR da DWT\_ITENS\_SERV\.

__Campo Não obrigatório \.__

__OS4107\-A__

__RN42__

__I\.N\.S\.S : __ 

Não será tratado, não preencher\.

__Campo Não obrigatório \.__

__OS4107\-A__

__RN43__

__CONFINS : __ 

Informe o valor do COFINS sem formatação e com zeros à esquerda\.

Ex: \(R$100,00\)  000000010000

Preencher com o campo VLR\_COFINS da DWT\_ITENS\_SERV\.

__Campo Não obrigatório \.__

__OS4107\-A__

__RN44__

__C\.S\.L\.L : __ 

Informe o valor do CSLL sem formatação e com zeros à esquerda\.

Ex:\(R$100,00\) 000000010000

Preencher com o campo VLR\_CSLL da DWT\_ITENS\_SERV\.

__Campo Não obrigatório \.__

__OS4107\-A__

__RN45__

__P\.I\.S: __

 Informe o valor do PIS sem formatação e com zeros à esquerda\.

 Ex: \(R$100,00\) 000000010000

Preencher com o campo VLR\_PIS da DWT\_ITENS\_SERV\.

__Campo Não obrigatório \.__

__OS4107\-A__

__RN46__

__Email:  __Informe um email para o envio da nota\.

__Notas Emitidas__

Preencher com o campo EMAIL da X04\_PESSOA\_FIS\_JUR\.

__Notas Recebidas__

Preencher com o campo EMAIL da tabela ESTABELECIMENTO\.

__Campo Não obrigatório \. __

__OS4107\-A__

__RN47__

__Discriminação: __ 

Descrição do serviço e  informações gerais\.

Preencher com o campo DSC\_SERV\_LEI\_116  da tabela  DWT\_SERVICO\_LEI\_116, referente a descrição do tipo de serviço\.

__Campo Não obrigatório\.__

__OS4107\-A__

__RN48__

__Alíquota de Fora: __ 

Informe a Alíquota utilizada No Município da prestação do Serviço\.

Se o município da capa for diferente do municipio do estabelecimento, preencher com o campo 32 \- VLR\_ALIQ\_ISS da tabela SAFX09\.  Essa regra será válida, para serviços Tomados e Prestados\.

Senão, 

Não preencher\.

Caso o município da nota não for preenchido, também deverá informar em branco\.

__Campo Não obrigatório\.__

__OS4107\-A__

__RN49__

__Tipo Abatimento:__  

Informe o código do abatimento realizado caso exista\.

Não será tratado, Não Preencher\.

__Campo Não obrigatório\.__

__OS4107\-A__

RN50

__Regra p/ inclusão do novo módulo no Manager:__

__Adamantina__

O novo módulo “Adamantina” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será:  “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de Adamantina”\.

__OS4107__

RN51

__Regra p/ abertura do novo módulo no Manager:__

__Adamantina__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “105” \(Adamantina\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a ADAMANTINA/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4107__

RN52

__Regra p/ inclusão do novo módulo no Manager:__

__Andradina__

O novo módulo “Andradina” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de Andradina”\.

__OS4107__

RN53

__Regra p/ abertura do novo módulo no Manager:__

__Andradina__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “2101” \(Andradina\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a ANDRADINA/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4107__

RN54

__Regra p/ inclusão do novo módulo no Manager:__

__Governador Valadares__

O novo módulo “Governador Valadares” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será:  “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de  Governador Valadares ”\.

__OS4107__

RN55

__Regra p/ abertura do novo módulo no Manager:__

__Governador Valadares__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “27701” \(Governador Valadares\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Governador Valadares/MG\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4107__

RN56

__Regra p/ inclusão do novo módulo no Manager:__

__Itanhaém__

O novo módulo “Itanhaem” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de Itanhaem”\.

__OS4107__

RN57

__Regra p/ abertura do novo módulo no Manager:__

__Itanhaém__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “22109” \(Itanhaem\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a ITANHAEM/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4107__

RN58

__Regra p/ inclusão do novo módulo no Manager:__

__Itatinga__

O novo módulo “Itatinga” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será:  “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de  Itatinga ”\.

__OS4107__

RN59

__Regra p/ abertura do novo módulo no Manager:__

__Itatinga__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “23503” \(Itatinga\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a ITATINGA/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4107__

RN60

__Regra p/ inclusão do novo módulo no Manager:__

__Porto Feliz__

O novo módulo “Porto Feliz” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será:  “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de  Porto Feliz ”\.

__OS4107__

RN61

__Regra p/ abertura do novo módulo no Manager:__

__Porto Feliz__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “40606” \(Porto Feliz\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a PORTO FELIZ/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4107__

RN62

__Regra p/ inclusão do novo módulo no Manager:__

__Peruíbe__

O novo módulo “Peruibe” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será:  “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de   Peruibe \.

__MFS\_3203__

RN63

__Regra p/ abertura do novo módulo no Manager:__

__Peruíbe__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “37602” \(Peruíbe\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Peruíbe/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\_3203__

RN64

__Regra p/ inclusão do novo módulo no Manager:__

__Itapetininga__

O novo módulo “Itapetininga” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de  Itapetininga\.

__MFS\_4265__

RN65

__Regra p/ abertura do novo módulo no Manager:__

__Itapetininga__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “22307” \(Itapetininga\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Itapetininga/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\_4265__

RN66

__Regra p/ inclusão do novo módulo no Manager:__

__Tatuí__

O novo módulo “Tatuí” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de Tatuí”\.

__MFS8230__

RN67

__Regra p/ abertura do novo módulo no Manager:__

__Tatuí__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “54003” \(Tatuí\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Tatuí/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS8230__

RN68

__Regra p/ inclusão do novo módulo no Manager:__

__Cerquilho__

O novo módulo “Cerquilho” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de Cerquilho”\.

__MFS11041__

RN69

__Regra p/ abertura do novo módulo no Manager:__

__Cerquilho__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “11508” \(Cerquilho\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Cerquilho/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS11041__

RN70

__Regra p/ inclusão do novo módulo no Manager:__

__Boituva__

O novo módulo “Boituva” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados, tomados e bancários do município de Boituva”\.

__MFS11041__

RN71

__Regra p/ abertura do novo módulo no Manager:__

__Boituva__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “7001” \(Boituva\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Boituva/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS11041__

RN72

__Regra p/ abertura do módulo no Manager:__

__Monte Mor__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “31803” \(Monte Mor\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Monte Mor/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados do município de Monte Mor”\.

__MFS589312__

RN73

__Regra p/ abertura do módulo no Manager:__

__Para cada município dessa lista deverá ser criado um modulo\.__

__MUNICÍPIO__

__ESTADO__

__CÓDIGO MUNICÍPIO__

__IPORANGA__

__SP__

21200

__TAQUARIVAI__

__SP__

47007

__BURI__

__SP__

8009

__CAJATI__

__SP__

9254

__CESARIO LANGE__

__SP__

11607

__IGARATA__

__SP__

20202

__ILHA COMPRIDA__

__SP__

20426

__IPERO__

__SP__

21002

__ITARIRI__

__SP__

23305

__LUCELIA__

__SP__

27405

__MIRACATU__

__SP__

29906

__OSVALDO CRUZ__

__SP__

34609

__PEREIRAS__

__SP__

34609

__PRATANIA__

__SP__

41059

__RIBEIRAO BRANCO__

__SP__

43006

__SARAPUI__

__SP__

51108

__UCHOA__

__SP__

55604

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “xxxxx” \(Nome do munícipio\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Nome do município/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados do município de xxxxxx\.

__MFS\-1043071__

RN74

__Regra p/ abertura do módulo no Manager:__

__Para cada município dessa lista deverá ser criado um modulo\.__

__MUNICÍPIO__

__ESTADO__

__CÓDIGO MUNICÍPIO__

__RIBEIRA__

__SP__

42800

__SAGRES__

__SP__

44707

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “xxxxx” \(Nome do munícipio\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

 “Este estabelecimento não pertence a Nome do município/SP\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados do município de xxxxxx\.

__MFS\-1059696__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

